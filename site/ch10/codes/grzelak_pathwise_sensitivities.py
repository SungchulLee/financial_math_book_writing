# -*- coding: utf-8 -*-
"""
Pathwise estimation of delta and vega for Black-Scholes model.

Demonstrates pathwise (likelihood ratio) method for computing option Greeks,
showing convergence with respect to number of Monte Carlo paths.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import enum


# =============================================================================
# 1. Enum Definition
# =============================================================================

class OptionType(enum.Enum):
    """Enumeration for option type."""
    CALL = 1.0
    PUT = -1.0


# =============================================================================
# 2. Black-Scholes Pricing Functions
# =============================================================================

def bs_call_put_option_price(option_type, s0, strikes, sigma, t, maturity, r):
    """
    Black-Scholes Call/Put option price.

    Parameters
    ----------
    option_type : OptionType
        CALL or PUT.
    s0 : float
        Initial stock price.
    strikes : array_like
        Strike prices.
    sigma : float
        Volatility.
    t : float
        Current time.
    maturity : float
        Maturity (T).
    r : float
        Risk-free rate.

    Returns
    -------
    value : ndarray
        Option price.
    """
    strikes = np.array(strikes).reshape([len(strikes), 1])
    d1 = (np.log(s0 / strikes) + (r + 0.5 * np.power(sigma, 2.0)) * (maturity - t)) / (sigma * np.sqrt(maturity - t))
    d2 = d1 - sigma * np.sqrt(maturity - t)
    if option_type == OptionType.CALL:
        value = st.norm.cdf(d1) * s0 - st.norm.cdf(d2) * strikes * np.exp(-r * (maturity - t))
    elif option_type == OptionType.PUT:
        value = st.norm.cdf(-d2) * strikes * np.exp(-r * (maturity - t)) - st.norm.cdf(-d1) * s0
    return value


def bs_delta(option_type, s0, strikes, sigma, t, maturity, r):
    """
    Black-Scholes delta (first derivative w.r.t. spot).

    Parameters
    ----------
    option_type : OptionType
        CALL or PUT.
    s0 : float
        Initial stock price.
    strikes : array_like
        Strike prices.
    sigma : float
        Volatility.
    t : float
        Current time.
    maturity : float
        Maturity (T).
    r : float
        Risk-free rate.

    Returns
    -------
    delta : ndarray
        Option delta.
    """
    strikes = np.array(strikes).reshape([len(strikes), 1])
    d1 = (np.log(s0 / strikes) + (r + 0.5 * np.power(sigma, 2.0)) * (maturity - t)) / (sigma * np.sqrt(maturity - t))
    if option_type == OptionType.CALL:
        value = st.norm.cdf(d1)
    elif option_type == OptionType.PUT:
        value = st.norm.cdf(d1) - 1
    return value


def bs_gamma(s0, strikes, sigma, t, maturity, r):
    """
    Black-Scholes gamma (second derivative w.r.t. spot).

    Parameters
    ----------
    s0 : float
        Initial stock price.
    strikes : array_like
        Strike prices.
    sigma : float
        Volatility.
    t : float
        Current time.
    maturity : float
        Maturity (T).
    r : float
        Risk-free rate.

    Returns
    -------
    gamma : ndarray
        Option gamma.
    """
    strikes = np.array(strikes).reshape([len(strikes), 1])
    d1 = (np.log(s0 / strikes) + (r + 0.5 * np.power(sigma, 2.0)) * (maturity - t)) / (sigma * np.sqrt(maturity - t))
    return st.norm.pdf(d1) / (s0 * sigma * np.sqrt(maturity - t))


def bs_vega(s0, strikes, sigma, t, maturity, r):
    """
    Black-Scholes vega (derivative w.r.t. volatility).

    Parameters
    ----------
    s0 : float
        Initial stock price.
    strikes : array_like
        Strike prices.
    sigma : float
        Volatility.
    t : float
        Current time.
    maturity : float
        Maturity (T).
    r : float
        Risk-free rate.

    Returns
    -------
    vega : ndarray
        Option vega.
    """
    d1 = (np.log(s0 / strikes) + (r + 0.5 * np.power(sigma, 2.0)) * (maturity - t)) / (sigma * np.sqrt(maturity - t))
    return s0 * st.norm.pdf(d1) * np.sqrt(maturity - t)


# =============================================================================
# 3. Path Generation
# =============================================================================

def generate_paths_gbm_euler(num_paths, num_steps, maturity, r, sigma, s0):
    """
    Generate GBM paths using Euler discretization.

    Parameters
    ----------
    num_paths : int
        Number of sample paths.
    num_steps : int
        Number of time steps.
    maturity : float
        Time to maturity (T).
    r : float
        Risk-free rate.
    sigma : float
        Volatility.
    s0 : float
        Initial stock price.

    Returns
    -------
    paths : dict
        Dictionary with keys 'time' and 'S'.
    """
    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))

    # Stock price and log-price
    s = np.zeros((num_paths, num_steps + 1))
    s[:, 0] = s0

    x = np.zeros((num_paths, num_steps + 1))
    x[:, 0] = np.log(s0)

    time = np.zeros(num_steps + 1)

    dt = maturity / float(num_steps)
    for i in range(num_steps):
        # Ensure samples from normal have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]

        x[:, i + 1] = x[:, i] + (r - 0.5 * sigma ** 2.0) * dt + sigma * (w[:, i + 1] - w[:, i])
        time[i + 1] = time[i] + dt

    s = np.exp(x)
    paths = {"time": time, "S": s}
    return paths


# =============================================================================
# 4. Pathwise Sensitivity Estimation
# =============================================================================

def pathwise_delta(s0, paths, strikes, maturity, r):
    """
    Estimate delta using pathwise method.

    Parameters
    ----------
    s0 : float
        Initial stock price.
    paths : ndarray
        Stock price paths (num_paths, num_steps+1).
    strikes : array_like
        Strike prices.
    maturity : float
        Maturity (T).
    r : float
        Risk-free rate.

    Returns
    -------
    delta_est : float
        Estimated delta.
    """
    strikes = np.array(strikes).reshape([len(strikes), 1])
    in_the_money = paths[:, -1] > strikes.T
    return np.exp(-r * maturity) * np.mean(paths[:, -1] / s0 * in_the_money)


def pathwise_vega(s0, paths, sigma, strikes, maturity, r):
    """
    Estimate vega using pathwise method.

    Parameters
    ----------
    s0 : float
        Initial stock price.
    paths : ndarray
        Stock price paths (num_paths, num_steps+1).
    sigma : float
        Volatility.
    strikes : array_like
        Strike prices.
    maturity : float
        Maturity (T).
    r : float
        Risk-free rate.

    Returns
    -------
    vega_est : float
        Estimated vega.
    """
    strikes = np.array(strikes).reshape([len(strikes), 1])
    in_the_money = paths[:, -1] > strikes.T
    temp2 = (1.0 / sigma) * paths[:, -1] * (np.log(paths[:, -1] / s0) - (r + 0.5 * sigma ** 2.0) * maturity)
    return np.exp(-r * maturity) * np.mean(in_the_money * temp2)


# =============================================================================
# 5. Visualization
# =============================================================================

def plot_delta_convergence(num_paths_vec, delta_pathwise, delta_exact):
    """
    Plot delta convergence vs number of paths.

    Parameters
    ----------
    num_paths_vec : ndarray
        Vector of path counts.
    delta_pathwise : ndarray
        Pathwise delta estimates.
    delta_exact : ndarray
        Exact delta value.
    """
    plt.figure(1, figsize=(10, 6))
    plt.grid()
    plt.plot(num_paths_vec, delta_pathwise, '.-r', label='Pathwise estimate')
    plt.plot(num_paths_vec, delta_exact * np.ones_like(num_paths_vec), label='Exact')
    plt.xlabel('Number of paths')
    plt.ylabel('Delta')
    plt.title('Convergence of pathwise delta w.r.t. number of paths')
    plt.legend()
    plt.tight_layout()


def plot_vega_convergence(num_paths_vec, vega_pathwise, vega_exact):
    """
    Plot vega convergence vs number of paths.

    Parameters
    ----------
    num_paths_vec : ndarray
        Vector of path counts.
    vega_pathwise : ndarray
        Pathwise vega estimates.
    vega_exact : ndarray
        Exact vega value.
    """
    plt.figure(2, figsize=(10, 6))
    plt.grid()
    plt.plot(num_paths_vec, vega_pathwise, '.-r', label='Pathwise estimate')
    plt.plot(num_paths_vec, vega_exact * np.ones_like(num_paths_vec), label='Exact')
    plt.xlabel('Number of paths')
    plt.ylabel('Vega')
    plt.title('Convergence of pathwise vega w.r.t. number of paths')
    plt.legend()
    plt.tight_layout()


# =============================================================================
# 6. Main
# =============================================================================

def main():
    """Run pathwise sensitivity analysis for Black-Scholes model."""
    # ===== Parameters =====
    option_type = OptionType.CALL
    s0 = 1.0  # Initial spot price
    r = 0.06  # Risk-free rate
    sigma = 0.3  # Volatility
    maturity = 1.0  # Time to maturity
    strikes = np.array([s0])
    t = 0.0  # Current time

    num_steps = 1000
    delta_exact = bs_delta(option_type, s0, strikes, sigma, t, maturity, r)
    vega_exact = bs_vega(s0, strikes, sigma, t, maturity, r)

    # ===== Convergence with respect to paths =====
    num_paths_vec = np.round(np.linspace(5, 1000, 50)).astype(int)
    delta_pathwise_vec = np.zeros(len(num_paths_vec))
    vega_pathwise_vec = np.zeros(len(num_paths_vec))

    for idx, num_paths in enumerate(num_paths_vec):
        print('Running simulation with {0} paths'.format(num_paths))
        np.random.seed(3)
        paths = generate_paths_gbm_euler(num_paths, num_steps, maturity, r, sigma, s0)
        s = paths["S"]

        delta_pathwise_vec[idx] = pathwise_delta(s0, s, strikes, maturity, r)
        vega_pathwise_vec[idx] = pathwise_vega(s0, s, sigma, strikes, maturity, r)

    plot_delta_convergence(num_paths_vec, delta_pathwise_vec, delta_exact[0, 0])
    plot_vega_convergence(num_paths_vec, vega_pathwise_vec, vega_exact[0, 0])
    plt.show()


if __name__ == "__main__":
    main()
