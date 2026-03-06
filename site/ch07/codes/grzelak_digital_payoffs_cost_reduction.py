# -*- coding: utf-8 -*-
"""
Price digital (cash-or-nothing) options with barrier features.

This script demonstrates Monte Carlo pricing of digital options and barrier
options using the Euler scheme for geometric Brownian motion. Digital options
have binary payoffs (cash-or-nothing), and barrier options have constraints
on the path taken by the stock price. Results include comparison of digital
option prices and up-and-out barrier option valuations.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
"""

import numpy as np
import matplotlib.pyplot as plt


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

def digital_payoff_valuation(S, T, r, payoff):
    """
    Compute discounted expected payoff for digital options.

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


def up_and_out_barrier(S, T, r, payoff, s_upper):
    """
    Compute up-and-out barrier option price.

    Parameters
    ----------
    S : ndarray
        Stock price paths of shape (num_paths, num_steps+1).
    T : float
        Time to maturity.
    r : float
        Risk-free interest rate.
    payoff : callable
        Payoff function at maturity.
    s_upper : float
        Upper barrier level.

    Returns
    -------
    V_0 : float
        Barrier option price.
    """
    # Handling of barrier constraint
    n1, n2 = S.shape
    barrier = np.zeros((n1, n2)) + s_upper

    hit_M = S > barrier
    hit_vec = np.sum(hit_M, 1)
    hit_vec = (hit_vec == 0.0).astype(int)

    V_0 = np.exp(-r * T) * np.mean(payoff(S[:, -1] * hit_vec))

    return V_0


# =============================================================================
# 3. Visualization
# =============================================================================

def plot_payoff_function(s_grid, payoff, K):
    """
    Plot the payoff function over a range of stock prices.

    Parameters
    ----------
    s_grid : ndarray
        Stock price grid.
    payoff : callable
        Payoff function.
    K : float
        Strike price (used in title).
    """
    plt.figure(1)
    plt.plot(s_grid, payoff(s_grid))
    plt.xlabel('Stock Price')
    plt.ylabel('Payoff')
    plt.title('Call Option Payoff (K={0})'.format(K))
    plt.grid()
    plt.tight_layout()


# =============================================================================
# 4. Main
# =============================================================================

def main():
    """Run digital option and barrier option pricing demonstration."""
    # Parameters
    num_paths = 10000      # Number of Monte Carlo paths
    num_steps = 250        # Number of time steps

    s0 = 100.0             # Initial stock price
    r = 0.05               # Risk-free rate
    T = 5.0                # Time to maturity
    sigma = 0.2            # Volatility
    s_upper = 150.0        # Upper barrier level

    # Generate paths
    paths = generate_paths_gbm_euler(num_paths, num_steps, T, r, sigma, s0)
    s_paths = paths["S"]
    s_T = s_paths[:, -1]

    # Payoff setting
    K = 100.0              # Strike price
    K2 = 140.0             # Second strike (for commented payoff)

    # Payoff specification (call option payoff)
    payoff = lambda S: np.maximum(S - K, 0.0)

    # Plot payoff function
    s_grid = np.linspace(50, s0 * 1.5, 200)
    plot_payoff_function(s_grid, payoff, K)

    # Valuation of digital option
    val_t0 = digital_payoff_valuation(s_T, T, r, payoff)
    print("Value of the contract at t0 ={0}".format(val_t0))

    # Barrier pricing (up-and-out barrier option)
    barrier_price = up_and_out_barrier(s_paths, T, r, payoff, s_upper)
    print("Value of the barrier contract at t0 ={0}".format(barrier_price))

    plt.show()


if __name__ == "__main__":
    main()
