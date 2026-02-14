# -*- coding: utf-8 -*-
"""
Heston model discretization: Euler scheme vs. Almost Exact Scheme (AES).

Compares Euler and AES discretization methods for the Heston stochastic
volatility model. Analyzes convergence properties and compares option prices
to exact COS method values across different discretization timesteps.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import enum


# =============================================================================
# 1. Enums and Option Types
# =============================================================================

class OptionType(enum.Enum):
    """Option type enumeration."""
    CALL = 1.0
    PUT = -1.0


# =============================================================================
# 2. Core Computation Functions
# =============================================================================

def chi_psi(a, b, c, d, k):
    """
    Compute chi and psi functions for COS method.

    Parameters
    ----------
    a : float
        Lower truncation boundary.
    b : float
        Upper truncation boundary.
    c : float
        Lower integration limit.
    d : float
        Upper integration limit.
    k : ndarray
        Series indices of shape (num_terms, 1).

    Returns
    -------
    value : dict
        Dictionary with keys 'chi' and 'psi', each of shape (num_terms, 1).
    """
    psi = (np.sin(k * np.pi * (d - a) / (b - a)) -
           np.sin(k * np.pi * (c - a) / (b - a)))
    psi[1:] = psi[1:] * (b - a) / (k[1:] * np.pi)
    psi[0] = d - c

    chi = 1.0 / (1.0 + np.power((k * np.pi / (b - a)), 2.0))
    expr1 = (np.cos(k * np.pi * (d - a) / (b - a)) * np.exp(d) -
             np.cos(k * np.pi * (c - a) / (b - a)) * np.exp(c))
    expr2 = (k * np.pi / (b - a) * np.sin(k * np.pi * (d - a) / (b - a)) -
             k * np.pi / (b - a) * np.sin(k * np.pi * (c - a) / (b - a)) *
             np.exp(c))
    chi = chi * (expr1 + expr2)

    value = {"chi": chi, "psi": psi}
    return value


def call_put_coefficients(option_type, a, b, k):
    """
    Determine coefficients for Put and Call option prices.

    Parameters
    ----------
    option_type : OptionType
        Option type (CALL or PUT).
    a : float
        Lower truncation boundary.
    b : float
        Upper truncation boundary.
    k : ndarray
        Series indices of shape (num_terms, 1).

    Returns
    -------
    h_k : ndarray
        Fourier coefficients of shape (num_terms, 1).
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


def call_put_option_price_cos_method(cf, option_type, s0, r, tau, k,
                                      num_terms, l_bound):
    """
    Price a European option using the COS method.

    Parameters
    ----------
    cf : callable
        Characteristic function of log-asset returns.
    option_type : OptionType
        Option type (CALL or PUT).
    s0 : float
        Initial stock price.
    r : float
        Risk-free interest rate.
    tau : float
        Time to maturity.
    k : array-like
        List of strikes.
    num_terms : int
        Number of expansion terms.
    l_bound : float
        Size of truncation domain (typically 8-10).

    Returns
    -------
    value : ndarray
        Option prices of shape (num_strikes, 1).
    """
    # Reshape K to a column vector
    if k is not np.array:
        k = np.array(k).reshape((len(k), 1))

    # Assign i=sqrt(-1)
    i = np.complex128(0.0 + 1.0j)
    x0 = np.log(s0 / k)

    # Truncation domain
    a = 0.0 - l_bound * np.sqrt(tau)
    b = 0.0 + l_bound * np.sqrt(tau)

    # Summation from k = 0 to k=num_terms-1
    k_vec = np.linspace(0, num_terms - 1, num_terms).reshape((num_terms, 1))
    u = k_vec * np.pi / (b - a)

    # Determine coefficients for put/call prices
    h_k = call_put_coefficients(option_type, a, b, k_vec)
    mat = np.exp(i * np.outer((x0 - a), u))
    temp = cf(u) * h_k
    temp[0] = 0.5 * temp[0]
    value = np.exp(-r * tau) * k * np.real(mat.dot(temp))
    return value


def characteristic_function_heston(r, tau, kappa, gamma, vbar, v0, rho):
    """
    Characteristic function for the Heston model.

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
        Long-term mean variance.
    v0 : float
        Initial variance.
    rho : float
        Correlation between asset and variance.

    Returns
    -------
    cf : callable
        Characteristic function.
    """
    i = np.complex128(0.0 + 1.0j)

    def d1(u):
        return np.sqrt(np.power(kappa - gamma * rho * i * u, 2) +
                       (u * u + i * u) * gamma * gamma)

    def g(u):
        return ((kappa - gamma * rho * i * u - d1(u)) /
                (kappa - gamma * rho * i * u + d1(u)))

    def c(u):
        return ((1.0 - np.exp(-d1(u) * tau)) /
                (gamma * gamma * (1.0 - g(u) * np.exp(-d1(u) * tau))) *
                (kappa - gamma * rho * i * u - d1(u)))

    def a(u):
        return (r * i * u * tau +
                kappa * vbar * tau / gamma / gamma *
                (kappa - gamma * rho * i * u - d1(u)) -
                2 * kappa * vbar / gamma / gamma *
                np.log((1.0 - g(u) * np.exp(-d1(u) * tau)) / (1.0 - g(u))))

    # Characteristic function for the Heston model
    def cf(u):
        return np.exp(a(u) + c(u) * v0)

    return cf


def cir_sample(num_paths, kappa, gamma, vbar, s, t, v_s):
    """
    Sample from the CIR distribution (exact sampling).

    Parameters
    ----------
    num_paths : int
        Number of samples.
    kappa : float
        Mean reversion speed.
    gamma : float
        Volatility of volatility.
    vbar : float
        Long-term mean variance.
    s : float
        Start time.
    t : float
        End time.
    v_s : ndarray
        Current variance values of shape (num_paths,).

    Returns
    -------
    sample : ndarray
        CIR samples of shape (num_paths,).
    """
    delta = 4.0 * kappa * vbar / gamma / gamma
    c = (1.0 / (4.0 * kappa) * gamma * gamma *
         (1.0 - np.exp(-kappa * (t - s))))
    kappa_bar = (4.0 * kappa * v_s * np.exp(-kappa * (t - s)) /
                 (gamma * gamma * (1.0 - np.exp(-kappa * (t - s)))))
    sample = c * np.random.noncentral_chisquare(delta, kappa_bar, num_paths)
    return sample


def eu_option_price_from_mc_paths_generalized(option_type, s, k, t, r):
    """
    Compute European option price from Monte Carlo paths.

    Parameters
    ----------
    option_type : OptionType
        Option type (CALL or PUT).
    s : ndarray
        Asset prices at maturity of shape (num_paths,).
    k : ndarray
        Strike prices of shape (num_strikes,).
    t : float
        Time to maturity.
    r : float
        Risk-free interest rate.

    Returns
    -------
    result : ndarray
        Option prices of shape (num_strikes, 1).
    """
    result = np.zeros((len(k), 1))
    if option_type == OptionType.CALL:
        for (idx, strike) in enumerate(k):
            result[idx] = (np.exp(-r * t) *
                          np.mean(np.maximum(s - strike, 0.0)))
    elif option_type == OptionType.PUT:
        for (idx, strike) in enumerate(k):
            result[idx] = (np.exp(-r * t) *
                          np.mean(np.maximum(strike - s, 0.0)))
    return result


def generate_paths_heston_euler(num_paths, num_steps, t, r, s0, kappa, gamma,
                                rho, vbar, v0):
    """
    Generate Heston model paths using Euler discretization.

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths.
    num_steps : int
        Number of time steps.
    t : float
        Terminal time.
    r : float
        Risk-free interest rate.
    s0 : float
        Initial stock price.
    kappa : float
        Mean reversion speed.
    gamma : float
        Volatility of volatility.
    rho : float
        Correlation between asset and variance.
    vbar : float
        Long-term mean variance.
    v0 : float
        Initial variance.

    Returns
    -------
    paths : dict
        Dictionary containing:
        - 'time': time grid of shape (num_steps+1,)
        - 'S': stock prices of shape (num_paths, num_steps+1)
    """
    z1 = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    z2 = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w1 = np.zeros((num_paths, num_steps + 1))
    w2 = np.zeros((num_paths, num_steps + 1))
    v = np.zeros((num_paths, num_steps + 1))
    x = np.zeros((num_paths, num_steps + 1))
    v[:, 0] = v0
    x[:, 0] = np.log(s0)

    time = np.zeros(num_steps + 1)

    dt = t / float(num_steps)

    for i in range(0, num_steps):
        # Ensure samples from normal have mean 0 and variance 1
        if num_paths > 1:
            z1[:, i] = (z1[:, i] - np.mean(z1[:, i])) / np.std(z1[:, i])
            z2[:, i] = (z2[:, i] - np.mean(z2[:, i])) / np.std(z2[:, i])

        z2[:, i] = rho * z1[:, i] + np.sqrt(1.0 - rho**2) * z2[:, i]

        w1[:, i + 1] = w1[:, i] + np.sqrt(dt) * z1[:, i]
        w2[:, i + 1] = w2[:, i] + np.sqrt(dt) * z2[:, i]

        # Truncated boundary condition
        v[:, i + 1] = (v[:, i] + kappa * (vbar - v[:, i]) * dt +
                       gamma * np.sqrt(v[:, i]) * (w1[:, i + 1] - w1[:, i]))
        v[:, i + 1] = np.maximum(v[:, i + 1], 0.0)

        x[:, i + 1] = (x[:, i] + (r - 0.5 * v[:, i]) * dt +
                       np.sqrt(v[:, i]) * (w2[:, i + 1] - w2[:, i]))
        time[i + 1] = time[i] + dt

    # Compute exponent
    s = np.exp(x)
    paths = {"time": time, "S": s}
    return paths


def generate_paths_heston_aes(num_paths, num_steps, t, r, s0, kappa, gamma,
                              rho, vbar, v0):
    """
    Generate Heston model paths using Almost Exact Scheme (AES).

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths.
    num_steps : int
        Number of time steps.
    t : float
        Terminal time.
    r : float
        Risk-free interest rate.
    s0 : float
        Initial stock price.
    kappa : float
        Mean reversion speed.
    gamma : float
        Volatility of volatility.
    rho : float
        Correlation between asset and variance.
    vbar : float
        Long-term mean variance.
    v0 : float
        Initial variance.

    Returns
    -------
    paths : dict
        Dictionary containing:
        - 'time': time grid of shape (num_steps+1,)
        - 'S': stock prices of shape (num_paths, num_steps+1)
    """
    z1 = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w1 = np.zeros((num_paths, num_steps + 1))
    v = np.zeros((num_paths, num_steps + 1))
    x = np.zeros((num_paths, num_steps + 1))
    v[:, 0] = v0
    x[:, 0] = np.log(s0)

    time = np.zeros(num_steps + 1)

    dt = t / float(num_steps)

    for i in range(0, num_steps):
        # Ensure samples from normal have mean 0 and variance 1
        if num_paths > 1:
            z1[:, i] = (z1[:, i] - np.mean(z1[:, i])) / np.std(z1[:, i])

        w1[:, i + 1] = w1[:, i] + np.sqrt(dt) * z1[:, i]

        # Exact samples for the variance process
        v[:, i + 1] = cir_sample(num_paths, kappa, gamma, vbar, 0, dt,
                                 v[:, i])
        k0 = (r - rho / gamma * kappa * vbar) * dt
        k1 = (rho * kappa / gamma - 0.5) * dt - rho / gamma
        k2 = rho / gamma
        x[:, i + 1] = (x[:, i] + k0 + k1 * v[:, i] + k2 * v[:, i + 1] +
                       np.sqrt((1.0 - rho**2) * v[:, i]) *
                       (w1[:, i + 1] - w1[:, i]))
        time[i + 1] = time[i] + dt

    # Compute exponent
    s = np.exp(x)
    paths = {"time": time, "S": s}
    return paths


def bs_call_put_option_price(option_type, s0, k, sigma, t, t_mat, r):
    """
    Black-Scholes call/put option price.

    Parameters
    ----------
    option_type : OptionType
        Option type (CALL or PUT).
    s0 : float
        Initial stock price.
    k : array-like
        Strike prices.
    sigma : float
        Volatility.
    t : float
        Current time.
    t_mat : float
        Maturity time.
    r : float
        Risk-free interest rate.

    Returns
    -------
    value : ndarray
        Option prices.
    """
    k = np.array(k).reshape((len(k), 1))
    d1 = ((np.log(s0 / k) + (r + 0.5 * np.power(sigma, 2.0)) *
           (t_mat - t)) / (sigma * np.sqrt(t_mat - t)))
    d2 = d1 - sigma * np.sqrt(t_mat - t)
    if option_type == OptionType.CALL:
        value = st.norm.cdf(d1) * s0 - st.norm.cdf(d2) * k * np.exp(-r *
                                                                     (t_mat - t))
    elif option_type == OptionType.PUT:
        value = (st.norm.cdf(-d2) * k * np.exp(-r * (t_mat - t)) -
                 st.norm.cdf(-d1) * s0)
    return value


# =============================================================================
# 3. Plotting Functions
# =============================================================================

def plot_option_prices(k, opt_value_exact, opt_price_euler, opt_price_aes):
    """
    Plot option prices comparison.

    Parameters
    ----------
    k : ndarray
        Strike prices.
    opt_value_exact : ndarray
        Exact option values from COS method.
    opt_price_euler : ndarray
        Euler scheme option prices.
    opt_price_aes : ndarray
        AES option prices.

    Returns
    -------
    None
    """
    plt.figure()
    plt.plot(k, opt_value_exact, '-r')
    plt.plot(k, opt_price_euler, '--k')
    plt.plot(k, opt_price_aes, '.b')
    plt.legend(['Exact (COS)', 'Euler', 'AES'])
    plt.grid()
    plt.xlabel('strike, K')
    plt.ylabel('option price')


# =============================================================================
# 4. Main Computation
# =============================================================================

def main():
    """Run Heston discretization comparison demo."""
    # Parameters
    num_paths = 2500
    num_steps = 500

    # Heston model parameters
    gamma = 1.0
    kappa = 0.5
    vbar = 0.04
    rho = -0.9
    v0 = 0.04
    t_mat = 1.0
    s0 = 100.0
    r = 0.1
    option_type = OptionType.CALL

    # ===== Comparison across different strikes =====

    # Define a range of strikes
    k = np.linspace(80, s0 * 1.5, 30)

    # Exact solution with the COS method
    cf = characteristic_function_heston(r, t_mat, kappa, gamma, vbar, v0,
                                        rho)

    # The COS method
    opt_value_exact = call_put_option_price_cos_method(
        cf, option_type, s0, r, t_mat, k, 1000, 8)

    # Euler simulation
    paths_euler = generate_paths_heston_euler(
        num_paths, num_steps, t_mat, r, s0, kappa, gamma, rho, vbar, v0)
    s_euler = paths_euler["S"]

    # Almost exact simulation
    paths_aes = generate_paths_heston_aes(
        num_paths, num_steps, t_mat, r, s0, kappa, gamma, rho, vbar, v0)
    s_aes = paths_aes["S"]

    opt_price_euler = eu_option_price_from_mc_paths_generalized(
        option_type, s_euler[:, -1], k, t_mat, r)
    opt_price_aes = eu_option_price_from_mc_paths_generalized(
        option_type, s_aes[:, -1], k, t_mat, r)

    plot_option_prices(k, opt_value_exact, opt_price_euler, opt_price_aes)

    # ===== Convergence analysis =====

    # Analyze convergence for particular dt
    dt_vec = np.array([1.0, 1.0 / 4.0, 1.0 / 8.0, 1.0 / 16.0,
                       1.0 / 32.0, 1.0 / 64.0])
    num_steps_vec = [int(t_mat / x) for x in dt_vec]

    # Specify strike for analysis
    k = np.array([140.0])

    # Exact
    opt_value_exact = call_put_option_price_cos_method(
        cf, option_type, s0, r, t_mat, k, 1000, 8)
    error_euler = np.zeros((len(dt_vec), 1))
    error_aes = np.zeros((len(dt_vec), 1))

    for (idx, num_steps) in enumerate(num_steps_vec):
        # Euler
        np.random.seed(3)
        paths_euler = generate_paths_heston_euler(
            num_paths, num_steps, t_mat, r, s0, kappa, gamma, rho, vbar, v0)
        s_euler = paths_euler["S"]
        opt_price_euler = eu_option_price_from_mc_paths_generalized(
            option_type, s_euler[:, -1], k, t_mat, r)
        error_euler[idx] = opt_price_euler - opt_value_exact

        # AES
        np.random.seed(3)
        paths_aes = generate_paths_heston_aes(
            num_paths, num_steps, t_mat, r, s0, kappa, gamma, rho, vbar, v0)
        s_aes = paths_aes["S"]
        opt_price_aes = eu_option_price_from_mc_paths_generalized(
            option_type, s_aes[:, -1], k, t_mat, r)
        error_aes[idx] = opt_price_aes - opt_value_exact

    # Print the results
    for i in range(0, len(num_steps_vec)):
        print("Euler Scheme, K = {0}, dt = {1} = {2}".format(
            k, dt_vec[i], error_euler[i]))

    for i in range(0, len(num_steps_vec)):
        print("AES Scheme, K = {0}, dt = {1} = {2}".format(
            k, dt_vec[i], error_aes[i]))


if __name__ == "__main__":
    main()
