# -*- coding: utf-8 -*-
"""
Price Asian options using Monte Carlo simulation with cost reduction.

This script demonstrates Monte Carlo pricing of Asian (average) options,
which depend on the average of the stock price over the option's life rather
than just the final price. A cost reduction technique (variance reduction) is
demonstrated by comparing the variance of the final stock price (European option)
with the variance of the arithmetic average (Asian option).

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
"""

import numpy as np


# =============================================================================
# 1. Path Generation
# =============================================================================

def generate_paths_gbm_euler(num_paths, num_steps, T, r, sigma, s0):
    """
    Generate sample paths for geometric Brownian motion using Euler scheme.

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths.
    num_steps : int
        Number of time steps.
    T : float
        Time to maturity.
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility.
    s0 : float
        Initial stock price.

    Returns
    -------
    paths : dict
        Dictionary containing:
        - 'time': time grid (ndarray of shape (num_steps+1,))
        - 'S': stock price paths (ndarray of shape (num_paths, num_steps+1))
    """
    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    w = np.zeros((num_paths, num_steps + 1))

    # Euler Approximation
    s1 = np.zeros((num_paths, num_steps + 1))
    s1[:, 0] = s0

    time = np.zeros(num_steps + 1)

    dt = T / float(num_steps)
    for i in range(0, num_steps):
        # Standardize samples to ensure mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]

        s1[:, i + 1] = (s1[:, i] + r * s1[:, i] * dt +
                        sigma * s1[:, i] * (w[:, i + 1] - w[:, i]))
        time[i + 1] = time[i] + dt

    paths = {"time": time, "S": s1}
    return paths


# =============================================================================
# 2. Valuation
# =============================================================================

def payoff_valuation(S, T, r, payoff):
    """
    Compute discounted expected payoff using Monte Carlo samples.

    Parameters
    ----------
    S : ndarray
        Stock prices at maturity (1D array of final prices).
    T : float
        Time to maturity.
    r : float
        Risk-free interest rate.
    payoff : callable
        Payoff function taking stock price(s) as argument.

    Returns
    -------
    value : float
        Discounted expected payoff.
    """
    return np.exp(-r * T) * np.mean(payoff(S))


# =============================================================================
# 3. Main
# =============================================================================

def main():
    """Run Asian option pricing demonstration."""
    # Parameters
    num_paths = 5000       # Number of Monte Carlo paths
    num_steps = 250        # Number of time steps

    s0 = 100.0             # Initial stock price
    r = 0.05               # Risk-free rate
    T = 5.0                # Time to maturity
    sigma = 0.2            # Volatility

    # Generate paths
    paths = generate_paths_gbm_euler(num_paths, num_steps, T, r, sigma, s0)
    s_paths = paths["S"]
    s_T = s_paths[:, -1]

    # Payoff setting
    K = 100.0              # Strike price

    # Payoff specification (call option payoff)
    payoff = lambda S: np.maximum(S - K, 0.0)

    # Valuation of European call option
    val_t0 = payoff_valuation(s_T, T, r, payoff)
    print("Value of the contract at t0 ={0}".format(val_t0))

    # Valuation of Asian option
    A_T = np.mean(s_paths, 1)
    val_asian_t0 = payoff_valuation(A_T, T, r, payoff)
    print("Value of the Asian option at t0 ={0}".format(val_asian_t0))

    # Variance comparison
    print('variance of S(T) = {0}'.format(np.var(s_T)))
    print('variance of A(T) = {0}'.format(np.var(A_T)))


if __name__ == "__main__":
    main()
