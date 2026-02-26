# -*- coding: utf-8 -*-
"""
Compute implied volatilities for the Bates model using the COS method.

This script computes option prices using the Bates model (Heston model with
jumps) via the Characteristic function Option Pricing (COS) method, then
calculates implied volatilities. Results are plotted for various parameter
combinations to show sensitivity to jump intensity, jump mean, and jump
volatility.

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
# 2. COS Method Core
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


def call_put_option_price_cos_method(cf, option_type, s0, r, tau, K, N, L):
    """
    Compute option prices using the COS method.

    Parameters
    ----------
    cf : callable
        Characteristic function.
    option_type : OptionType
        Option type (CALL or PUT).
    s0 : float
        Initial stock price.
    r : float
        Risk-free interest rate.
    tau : float
        Time to maturity.
    K : ndarray
        Strike prices.
    N : int
        Number of expansion terms.
    L : float
        Truncation domain size parameter.

    Returns
    -------
    value : ndarray
        Option prices.
    """
    # Reshape K to a column vector if needed
    if K is not np.array:
        K = np.array(K).reshape((len(K), 1))

    i = np.complex(0.0, 1.0)
    x0 = np.log(s0 / K)

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
    value = np.exp(-r * tau) * K * np.real(mat.dot(temp))
    return value


# =============================================================================
# 3. Black-Scholes and Implied Volatility
# =============================================================================

def bs_call_option_price(option_type, s0, K, sigma, tau, r):
    """
    Compute Black-Scholes option prices.

    Parameters
    ----------
    option_type : OptionType
        Option type (CALL or PUT).
    s0 : float
        Initial stock price.
    K : ndarray
        Strike prices.
    sigma : float or ndarray
        Volatility.
    tau : float
        Time to maturity.
    r : float
        Risk-free interest rate.

    Returns
    -------
    value : ndarray
        Option prices.
    """
    if K is list:
        K = np.array(K).reshape((len(K), 1))
    d1 = (np.log(s0 / K) + (r + 0.5 * np.power(sigma, 2.0)) * tau) / (
        sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    if option_type == OptionType.CALL:
        value = stats.norm.cdf(d1) * s0 - stats.norm.cdf(d2) * K * np.exp(
            -r * tau)
    elif option_type == OptionType.PUT:
        value = (stats.norm.cdf(-d2) * K * np.exp(-r * tau) -
                 stats.norm.cdf(-d1) * s0)
    return value


def compute_objective_function(sigma, market_price, option_type, s0, K, tau,
                               r):
    """
    Objective function for implied volatility optimization.

    Parameters
    ----------
    sigma : float
        Volatility to test.
    market_price : float
        Market option price.
    option_type : OptionType
        Option type.
    s0 : float
        Initial stock price.
    K : float
        Strike price.
    tau : float
        Time to maturity.
    r : float
        Risk-free interest rate.

    Returns
    -------
    error : float
        Squared price difference.
    """
    return np.power(
        bs_call_option_price(option_type, s0, K, sigma, tau, r) -
        market_price, 1.0)


def implied_volatility(option_type, market_price, K, tau, s0, r):
    """
    Compute implied volatility using numerical optimization.

    Parameters
    ----------
    option_type : OptionType
        Option type (CALL or PUT).
    market_price : float
        Market option price.
    K : float
        Strike price.
    tau : float
        Time to maturity.
    s0 : float
        Initial stock price.
    r : float
        Risk-free interest rate.

    Returns
    -------
    implied_vol : float
        Implied volatility.
    """
    # Determine initial volatility via interpolation
    sigma_grid = np.linspace(0, 2, 200)
    opt_price_grid = bs_call_option_price(option_type, s0, K, sigma_grid, tau,
                                          r)
    sigma_initial = np.interp(market_price, opt_price_grid, sigma_grid)
    print("Initial volatility = {0}".format(sigma_initial))

    # Use determined input for local search (final tuning)
    func = lambda sigma: compute_objective_function(  # noqa: E731
        sigma, market_price, option_type, s0, K, tau, r)
    implied_vol = optimize.newton(func, sigma_initial, tol=1e-10)
    print("Final volatility = {0}".format(implied_vol))
    return implied_vol


# =============================================================================
# 4. Characteristic Functions
# =============================================================================

def char_func_bates_model(r, tau, kappa, gamma, vbar, v0, rho, xi_p, mu_j,
                          sigma_j):
    """
    Compute characteristic function for the Bates model.

    Parameters
    ----------
    r : float
        Risk-free interest rate.
    tau : float
        Time to maturity.
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
    xi_p : float
        Jump intensity.
    mu_j : float
        Mean of jump size.
    sigma_j : float
        Volatility of jump size.

    Returns
    -------
    cf : callable
        Characteristic function.
    """
    i = np.complex(0.0, 1.0)

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

    def a_heston_func(u):
        d1 = d1_func(u)
        return (r * i * u * tau + kappa * vbar * tau / gamma / gamma *
                (kappa - gamma * rho * i * u - d1) -
                2 * kappa * vbar / gamma / gamma *
                np.log((1.0 - g_func(u) * np.exp(-d1 * tau)) /
                       (1.0 - g_func(u))))

    def a_func(u):
        return (a_heston_func(u) - xi_p * i * u * tau *
                (np.exp(mu_j + 0.5 * sigma_j * sigma_j) - 1.0) +
                xi_p * tau *
                (np.exp(i * u * mu_j - 0.5 * sigma_j * sigma_j * u * u) -
                 1.0))

    def cf_func(u):
        return np.exp(a_func(u) + c_func(u) * v0)

    return cf_func


# =============================================================================
# 5. Visualization
# =============================================================================

def plot_implied_vol_vs_xi_p(S0, r, tau, K, N, L, kappa, gamma, vbar, v0,
                             rho, mu_j, sigma_j):
    """
    Plot implied volatility as function of jump intensity.

    Parameters
    ----------
    S0 : float
        Initial stock price.
    r : float
        Risk-free rate.
    tau : float
        Time to maturity.
    K : ndarray
        Strike prices.
    N : int
        Number of COS terms.
    L : float
        Truncation parameter.
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
    mu_j : float
        Jump mean.
    sigma_j : float
        Jump volatility.
    """
    option_type = OptionType.CALL
    plt.figure(1)
    plt.grid()
    plt.xlabel('strike, K')
    plt.ylabel('implied volatility')

    xi_p_values = [0.01, 0.1, 0.2, 0.3]
    legend = []

    for xi_p_temp in xi_p_values:
        # Compute characteristic function for Bates model
        cf = char_func_bates_model(r, tau, kappa, gamma, vbar, v0, rho,
                                   xi_p_temp, mu_j, sigma_j)

        # Compute option prices via COS method
        val_cos = call_put_option_price_cos_method(cf, option_type, S0, r, tau,
                                                   K, N, L)

        # Compute implied volatilities
        IV = np.zeros((len(K), 1))
        for idx in range(0, len(K)):
            IV[idx] = implied_volatility(option_type, val_cos[idx], K[idx],
                                         tau, S0, r)
        plt.plot(K, IV * 100.0)
        legend.append('xi_p={0}'.format(xi_p_temp))

    plt.legend(legend)


def plot_implied_vol_vs_mu_j(S0, r, tau, K, N, L, kappa, gamma, vbar, v0,
                             rho, xi_p, sigma_j):
    """
    Plot implied volatility as function of jump mean.

    Parameters
    ----------
    S0 : float
        Initial stock price.
    r : float
        Risk-free rate.
    tau : float
        Time to maturity.
    K : ndarray
        Strike prices.
    N : int
        Number of COS terms.
    L : float
        Truncation parameter.
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
    xi_p : float
        Jump intensity.
    sigma_j : float
        Jump volatility.
    """
    option_type = OptionType.CALL
    plt.figure(2)
    plt.grid()
    plt.xlabel('strike, K')
    plt.ylabel('implied volatility')

    mu_j_values = [-0.5, -0.25, 0, 0.25]
    legend = []

    for mu_j_temp in mu_j_values:
        # Compute characteristic function for Bates model
        cf = char_func_bates_model(r, tau, kappa, gamma, vbar, v0, rho, xi_p,
                                   mu_j_temp, sigma_j)

        # Compute option prices via COS method
        val_cos = call_put_option_price_cos_method(cf, option_type, S0, r, tau,
                                                   K, N, L)

        # Compute implied volatilities
        IV = np.zeros((len(K), 1))
        for idx in range(0, len(K)):
            IV[idx] = implied_volatility(option_type, val_cos[idx], K[idx],
                                         tau, S0, r)
        plt.plot(K, IV * 100.0)
        legend.append('mu_j={0}'.format(mu_j_temp))

    plt.legend(legend)


def plot_implied_vol_vs_sigma_j(S0, r, tau, K, N, L, kappa, gamma, vbar, v0,
                                rho, xi_p, mu_j):
    """
    Plot implied volatility as function of jump volatility.

    Parameters
    ----------
    S0 : float
        Initial stock price.
    r : float
        Risk-free rate.
    tau : float
        Time to maturity.
    K : ndarray
        Strike prices.
    N : int
        Number of COS terms.
    L : float
        Truncation parameter.
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
    xi_p : float
        Jump intensity.
    mu_j : float
        Jump mean.
    """
    option_type = OptionType.CALL
    plt.figure(3)
    plt.grid()
    plt.xlabel('strike, K')
    plt.ylabel('implied volatility')

    sigma_j_values = [0.01, 0.15, 0.2, 0.25]
    legend = []

    for sigma_j_temp in sigma_j_values:
        # Compute characteristic function for Bates model
        cf = char_func_bates_model(r, tau, kappa, gamma, vbar, v0, rho, xi_p,
                                   mu_j, sigma_j_temp)

        # Compute option prices via COS method
        val_cos = call_put_option_price_cos_method(cf, option_type, S0, r, tau,
                                                   K, N, L)

        # Compute implied volatilities
        IV = np.zeros((len(K), 1))
        for idx in range(0, len(K)):
            IV[idx] = implied_volatility(option_type, val_cos[idx], K[idx],
                                         tau, S0, r)
        plt.plot(K, IV * 100.0)
        legend.append('sigma_j={0}'.format(sigma_j_temp))

    plt.legend(legend)


# =============================================================================
# 6. Main
# =============================================================================

def main():
    """Run Bates model implied volatility computation."""
    # Parameters
    option_type = OptionType.CALL
    s0 = 100.0             # Initial stock price
    r = 0.0                # Risk-free rate
    tau = 1.0              # Time to maturity

    K = np.linspace(40, 180, 10)
    K = np.array(K).reshape((len(K), 1))

    N = 1000               # COS expansion terms
    L = 6                  # Truncation parameter

    # Heston model parameters
    kappa = 1.2            # Mean reversion speed
    gamma = 0.05           # Volatility of volatility
    vbar = 0.05            # Long-run variance
    rho = -0.75            # Correlation
    v0 = vbar              # Initial variance
    mu_j = 0.0             # Jump mean
    sigma_j = 0.2          # Jump volatility
    xi_p = 0.1             # Jump intensity

    # Generate plots
    plot_implied_vol_vs_xi_p(s0, r, tau, K, N, L, kappa, gamma, vbar, v0,
                             rho, mu_j, sigma_j)
    plot_implied_vol_vs_mu_j(s0, r, tau, K, N, L, kappa, gamma, vbar, v0,
                             rho, xi_p, sigma_j)
    plot_implied_vol_vs_sigma_j(s0, r, tau, K, N, L, kappa, gamma, vbar, v0,
                                rho, xi_p, mu_j)
    plt.show()


if __name__ == "__main__":
    main()
