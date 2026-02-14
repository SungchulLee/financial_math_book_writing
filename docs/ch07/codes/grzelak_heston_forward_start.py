# -*- coding: utf-8 -*-
"""
Compute implied volatilities for forward-start options under the Heston model.

This script computes forward-start option prices using the Heston stochastic
volatility model via the Characteristic function Option Pricing (COS) method.
Forward-start options are options whose strike is set relative to the stock
price at an intermediate time T1. Implied volatilities are computed for various
pairs of times to show model behavior.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import enum
from scipy import optimize


# =============================================================================
# 1. Option Type Definition
# =============================================================================

class OptionType(enum.Enum):
    """Enumeration for option types."""
    CALL = 1.0
    PUT = -1.0


# =============================================================================
# 2. COS Method Core for Forward-Start Options
# =============================================================================

def call_put_coefficients(option_type, a, b, k):
    """
    Compute COS method coefficients for put and call options.

    Parameters
    ----------
    option_type : OptionType
        Option type (CALL or PUT).
    a : float
        Lower truncation bound.
    b : float
        Upper truncation bound.
    k : ndarray
        Expansion term indices.

    Returns
    -------
    h_k : ndarray
        COS method coefficients.
    """
    if option_type == OptionType.CALL:
        c = 0.0
        d = b
        coef = chi_psi(a, b, c, d, k)
        chi_k = coef["chi"]
        psi_k = coef["psi"]
        if a < b and b < 0.0:
            h_k = np.zeros((len(k), 1))
        else:
            h_k = 2.0 / (b - a) * (chi_k - psi_k)
    elif option_type == OptionType.PUT:
        c = a
        d = 0.0
        coef = chi_psi(a, b, c, d, k)
        chi_k = coef["chi"]
        psi_k = coef["psi"]
        h_k = 2.0 / (b - a) * (-chi_k + psi_k)

    return h_k


def chi_psi(a, b, c, d, k):
    """
    Compute chi and psi functions for COS method.

    Parameters
    ----------
    a : float
        Lower bound.
    b : float
        Upper bound.
    c : float
        Lower integration bound.
    d : float
        Upper integration bound.
    k : ndarray
        Expansion term indices.

    Returns
    -------
    value : dict
        Dictionary with 'chi' and 'psi' keys containing the computed arrays.
    """
    psi = (np.sin(k * np.pi * (d - a) / (b - a)) -
           np.sin(k * np.pi * (c - a) / (b - a)))
    psi[1:] = psi[1:] * (b - a) / (k[1:] * np.pi)
    psi[0] = d - c

    chi = 1.0 / (1.0 + np.power(k * np.pi / (b - a), 2.0))
    expr1 = (np.cos(k * np.pi * (d - a) / (b - a)) * np.exp(d) -
             np.cos(k * np.pi * (c - a) / (b - a)) * np.exp(c))
    expr2 = (k * np.pi / (b - a) * np.sin(k * np.pi * (d - a) / (b - a)) -
             k * np.pi / (b - a) * np.sin(k * np.pi * (c - a) / (b - a)) *
             np.exp(c))
    chi = chi * (expr1 + expr2)

    value = {"chi": chi, "psi": psi}
    return value


def call_put_option_price_cos_method_frwd_start(cf, option_type, r, T1, T2, K,
                                                N, L):
    """
    Compute forward-start option prices using the COS method.

    Parameters
    ----------
    cf : callable
        Characteristic function.
    option_type : OptionType
        Option type (CALL or PUT).
    r : float
        Risk-free interest rate.
    T1 : float
        Time when strike is set.
    T2 : float
        Option maturity time.
    K : ndarray
        Relative strike prices.
    N : int
        Number of expansion terms.
    L : float
        Truncation domain size parameter.

    Returns
    -------
    value : ndarray
        Option prices.
    """
    tau = T2 - T1

    # Reshape K to a column vector if needed
    if K is not np.array:
        K = np.array(K).reshape((len(K), 1))

    # Adjust strike
    K = K + 1.0

    i = np.complex(0.0, 1.0)
    x0 = np.log(1.0 / K)

    # Truncation domain
    a = 0.0 - L * np.sqrt(tau)
    b = 0.0 + L * np.sqrt(tau)

    # Summation from k = 0 to k=N-1
    k = np.linspace(0, N - 1, N).reshape((N, 1))
    u = k * np.pi / (b - a)

    # Determine coefficients
    h_k = call_put_coefficients(option_type, a, b, k)
    mat = np.exp(i * np.outer(x0 - a, u))
    temp = cf(u) * h_k
    temp[0] = 0.5 * temp[0]
    value = np.exp(-r * T2) * K * np.real(mat.dot(temp))
    return value


# =============================================================================
# 3. Black-Scholes and Implied Volatility
# =============================================================================

def bs_call_option_price_frwd_start(K, sigma, T1, T2, r):
    """
    Compute Black-Scholes forward-start option prices.

    Parameters
    ----------
    K : ndarray
        Relative strike prices.
    sigma : float or ndarray
        Volatility.
    T1 : float
        Time when strike is set.
    T2 : float
        Option maturity time.
    r : float
        Risk-free interest rate.

    Returns
    -------
    value : ndarray
        Option prices.
    """
    if K is list:
        K = np.array(K).reshape((len(K), 1))
    K = K + 1.0
    tau = T2 - T1
    d1 = (np.log(1.0 / K) + (r + 0.5 * np.power(sigma, 2.0)) * tau) / (
        sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    value = (np.exp(-r * T1) * stats.norm.cdf(d1) -
             stats.norm.cdf(d2) * K * np.exp(-r * T2))
    return value


def compute_objective_function(sigma, market_price, K, T1, T2, r):
    """
    Objective function for implied volatility optimization.

    Parameters
    ----------
    sigma : float
        Volatility to test.
    market_price : float
        Market option price.
    K : float
        Relative strike price.
    T1 : float
        Time when strike is set.
    T2 : float
        Option maturity time.
    r : float
        Risk-free interest rate.

    Returns
    -------
    error : float
        Squared price difference.
    """
    return np.power(
        bs_call_option_price_frwd_start(K, sigma, T1, T2, r) - market_price,
        1.0)


def implied_volatility_frwd_start(market_price, K, T1, T2, r):
    """
    Compute implied volatility for forward-start options.

    Parameters
    ----------
    market_price : float
        Market option price.
    K : float
        Relative strike price.
    T1 : float
        Time when strike is set.
    T2 : float
        Option maturity time.
    r : float
        Risk-free interest rate.

    Returns
    -------
    implied_vol : float
        Implied volatility.
    """
    # Determine initial volatility via interpolation
    sigma_grid = np.linspace(0, 2, 200)
    opt_price_grid = bs_call_option_price_frwd_start(K, sigma_grid, T1, T2, r)
    sigma_initial = np.interp(market_price, opt_price_grid, sigma_grid)
    print("Initial volatility = {0}".format(sigma_initial))

    # Use determined input for local search (final tuning)
    func = lambda sigma: compute_objective_function(  # noqa: E731
        sigma, market_price, K, T1, T2, r)
    implied_vol = optimize.newton(func, sigma_initial, tol=1e-15)
    print("Final volatility = {0}".format(implied_vol))
    return implied_vol


# =============================================================================
# 4. Characteristic Functions
# =============================================================================

def char_func_heston_model_forward_start(r, T1, T2, kappa, gamma, vbar, v0,
                                         rho):
    """
    Compute characteristic function for Heston model in forward-start context.

    Parameters
    ----------
    r : float
        Risk-free interest rate.
    T1 : float
        Time when strike is set.
    T2 : float
        Option maturity time.
    kappa : float
        Mean reversion speed.
    gamma : float
        Volatility of volatility.
    vbar : float
        Long-run variance.
    v0 : float
        Initial variance.
    rho : float
        Correlation between price and variance.

    Returns
    -------
    cf : callable
        Characteristic function.
    """
    i = np.complex(0.0, 1.0)
    tau = T2 - T1

    def d1_func(u):
        return np.sqrt(np.power(kappa - gamma * rho * i * u, 2) +
                       (u * u + i * u) * gamma * gamma)

    def g_func(u):
        d1 = d1_func(u)
        return (kappa - gamma * rho * i * u - d1) / (
            kappa - gamma * rho * i * u + d1)

    def c_func(u):
        d1 = d1_func(u)
        return ((1.0 - np.exp(-d1 * tau)) /
                (gamma * gamma * (1.0 - g_func(u) * np.exp(-d1 * tau))) *
                (kappa - gamma * rho * i * u - d1))

    def a_func(u):
        d1 = d1_func(u)
        return (r * i * u * tau + kappa * vbar * tau / gamma / gamma *
                (kappa - gamma * rho * i * u - d1) -
                2 * kappa * vbar / gamma / gamma *
                np.log((1.0 - g_func(u) * np.exp(-d1 * tau)) /
                       (1.0 - g_func(u))))

    def c_bar_func(t1, t2):
        return gamma * gamma / (4.0 * kappa) * (1.0 - np.exp(-kappa * (t2 - t1)))

    delta = 4.0 * kappa * vbar / gamma / gamma

    def kappa_bar_func(t1, t2):
        return (4.0 * kappa * v0 * np.exp(-kappa * (t2 - t1)) /
                (gamma * gamma * (1.0 - np.exp(-kappa * (t2 - t1)))))

    def term1_func(u):
        return (a_func(u) + c_func(u) * c_bar_func(0.0, T1) *
                kappa_bar_func(0.0, T1) /
                (1.0 - 2.0 * c_func(u) * c_bar_func(0.0, T1)))

    def term2_func(u):
        return np.power(1.0 / (1.0 - 2.0 * c_func(u) * c_bar_func(0.0, T1)),
                        0.5 * delta)

    def cf_func(u):
        return np.exp(term1_func(u)) * term2_func(u)

    return cf_func


# =============================================================================
# 5. Visualization
# =============================================================================

def plot_implied_vol_pair_set_1(r, kappa, gamma, vbar, v0, rho, K, N, L):
    """
    Plot implied volatility for first set of T1, T2 pairs.

    Parameters
    ----------
    r : float
        Risk-free rate.
    kappa : float
        Mean reversion speed.
    gamma : float
        Volatility of volatility.
    vbar : float
        Long-run variance.
    v0 : float
        Initial variance.
    rho : float
        Correlation.
    K : ndarray
        Relative strike prices.
    N : int
        Number of COS terms.
    L : float
        Truncation parameter.
    """
    option_type = OptionType.CALL
    t_mat1 = [[1.0, 3.0], [2.0, 4.0], [3.0, 5.0], [4.0, 6.0]]

    plt.figure(1)
    plt.grid()
    plt.xlabel('strike, K')
    plt.ylabel('implied volatility')
    legend = []

    for t_pair in t_mat1:
        T1 = t_pair[0]
        T2 = t_pair[1]
        cf = char_func_heston_model_forward_start(r, T1, T2, kappa, gamma,
                                                  vbar, v0, rho)
        # Forward-start option prices from COS method
        val_cos = call_put_option_price_cos_method_frwd_start(
            cf, option_type, r, T1, T2, K, N, L)
        # Implied volatilities
        IV = np.zeros((len(K), 1))
        for idx in range(0, len(K)):
            IV[idx] = implied_volatility_frwd_start(val_cos[idx], K[idx], T1,
                                                    T2, r)
        plt.plot(K, IV * 100.0)
        legend.append('T1={0} & T2={1}'.format(T1, T2))

    plt.legend(legend)


def plot_implied_vol_pair_set_2(r, kappa, gamma, vbar, v0, rho, K, N, L):
    """
    Plot implied volatility for second set of T1, T2 pairs.

    Parameters
    ----------
    r : float
        Risk-free rate.
    kappa : float
        Mean reversion speed.
    gamma : float
        Volatility of volatility.
    vbar : float
        Long-run variance.
    v0 : float
        Initial variance.
    rho : float
        Correlation.
    K : ndarray
        Relative strike prices.
    N : int
        Number of COS terms.
    L : float
        Truncation parameter.
    """
    option_type = OptionType.CALL
    t_mat2 = [[1.0, 2.0], [1.0, 3.0], [1.0, 4.0], [1.0, 5.0]]

    plt.figure(2)
    plt.grid()
    plt.xlabel('strike, K')
    plt.ylabel('implied volatility')
    legend = []

    for t_pair in t_mat2:
        T1 = t_pair[0]
        T2 = t_pair[1]
        cf = char_func_heston_model_forward_start(r, T1, T2, kappa, gamma,
                                                  vbar, v0, rho)
        # Forward-start option prices from COS method
        val_cos = call_put_option_price_cos_method_frwd_start(
            cf, option_type, r, T1, T2, K, N, L)
        # Implied volatilities
        IV = np.zeros((len(K), 1))
        for idx in range(0, len(K)):
            IV[idx] = implied_volatility_frwd_start(val_cos[idx], K[idx], T1,
                                                    T2, r)
        plt.plot(K, IV * 100.0)
        legend.append('T1={0} & T2={1}'.format(T1, T2))

    plt.legend(legend)


# =============================================================================
# 6. Main
# =============================================================================

def main():
    """Run forward-start option implied volatility computation."""
    # Parameters
    option_type = OptionType.CALL
    r = 0.00               # Risk-free rate

    K = np.linspace(-0.4, 4.0, 50)
    K = np.array(K).reshape((len(K), 1))

    N = 500                # COS expansion terms
    L = 10                 # Truncation parameter

    # Heston model parameters
    kappa = 0.6            # Mean reversion speed
    gamma = 0.2            # Volatility of volatility
    vbar = 0.1             # Long-run variance
    rho = -0.5             # Correlation
    v0 = 0.05              # Initial variance

    # Generate plots
    plot_implied_vol_pair_set_1(r, kappa, gamma, vbar, v0, rho, K, N, L)
    plot_implied_vol_pair_set_2(r, kappa, gamma, vbar, v0, rho, K, N, L)
    plt.show()


if __name__ == "__main__":
    main()
