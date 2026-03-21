# -*- coding: utf-8 -*-
"""
Delta hedging with jumps using the Merton model.

Demonstrates delta hedging when underlying asset exhibits jump behavior,
analyzing profit and loss from hedging errors in presence of discontinuous moves.

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
# 2. Path Generation
# =============================================================================

def generate_paths_merton(num_paths, num_steps, s0, maturity, jump_intensity, jump_mean,
                         jump_std, r, sigma):
    """
    Generate Merton jump-diffusion paths.

    Parameters
    ----------
    num_paths : int
        Number of sample paths.
    num_steps : int
        Number of time steps.
    s0 : float
        Initial stock price.
    maturity : float
        Time to maturity (T).
    jump_intensity : float
        Poisson jump intensity (xi).
    jump_mean : float
        Mean of log-jump size.
    jump_std : float
        Standard deviation of log-jump size.
    r : float
        Risk-free rate.
    sigma : float
        Volatility.

    Returns
    -------
    paths : dict
        Dictionary with keys 'time', 'X' (log-price), 'S' (price).
    """
    # Create empty matrices for paths
    x = np.zeros((num_paths, num_steps + 1))
    s = np.zeros((num_paths, num_steps + 1))
    time = np.zeros(num_steps + 1)

    dt = maturity / float(num_steps)
    x[:, 0] = np.log(s0)
    s[:, 0] = s0

    # Expectation E(e^J) for J ~ N(jump_mean, jump_std^2)
    exp_jump = np.exp(jump_mean + 0.5 * jump_std * jump_std)
    z_poisson = np.random.poisson(jump_intensity * dt, (num_paths, num_steps))
    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    j = np.random.normal(jump_mean, jump_std, (num_paths, num_steps))

    for i in range(num_steps):
        # Ensure samples from normal have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        # Merton model: drift-adjusted for jump contribution
        x[:, i + 1] = (x[:, i] + (r - jump_intensity * (exp_jump - 1) - 0.5 * sigma * sigma) * dt
                       + sigma * np.sqrt(dt) * z[:, i] + j[:, i] * z_poisson[:, i])
        time[i + 1] = time[i] + dt

    s = np.exp(x)
    paths = {"time": time, "X": x, "S": s}
    return paths


def generate_paths_gbm(num_paths, num_steps, maturity, r, sigma, s0):
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
    x = np.zeros((num_paths, num_steps + 1))
    w = np.zeros((num_paths, num_steps + 1))
    time = np.zeros(num_steps + 1)

    x[:, 0] = np.log(s0)

    dt = maturity / float(num_steps)
    for i in range(num_steps):
        # Ensure samples from normal have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        x[:, i + 1] = x[:, i] + (r - 0.5 * sigma * sigma) * dt + sigma * (w[:, i + 1] - w[:, i])
        time[i + 1] = time[i] + dt

    # Compute stock prices from log-prices
    s = np.exp(x)
    paths = {"time": time, "S": s}
    return paths


# =============================================================================
# 3. Black-Scholes Pricing Functions
# =============================================================================

def bs_call_put_option_price(option_type, s0, strikes, sigma, t, maturity, r):
    """
    Black-Scholes Call/Put option price.

    Parameters
    ----------
    option_type : OptionType
        CALL or PUT.
    s0 : float
        Current stock price.
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
        Current stock price.
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
    # Handle numerical issues near maturity
    if t - maturity > 10e-20 and maturity - t < 10e-7:
        t = maturity

    strikes = np.array(strikes).reshape([len(strikes), 1])
    d1 = (np.log(s0 / strikes) + (r + 0.5 * np.power(sigma, 2.0)) * (maturity - t)) / (sigma * np.sqrt(maturity - t))
    if option_type == OptionType.CALL:
        value = st.norm.cdf(d1)
    elif option_type == OptionType.PUT:
        value = st.norm.cdf(d1) - 1.0
    return value


# =============================================================================
# 4. Visualization
# =============================================================================

def plot_single_path_results(time, stock_prices, call_prices, deltas, pnl):
    """
    Plot results for a single sample path.

    Parameters
    ----------
    time : ndarray
        Time grid.
    stock_prices : ndarray
        Stock prices along path.
    call_prices : ndarray
        Option prices along path.
    deltas : ndarray
        Delta values along path.
    pnl : ndarray
        Profit and loss along path.
    """
    plt.figure(1, figsize=(10, 6))
    plt.plot(time, stock_prices, label='Stock')
    plt.plot(time, call_prices, label='Call Price')
    plt.plot(time, deltas, label='Delta')
    plt.plot(time, pnl, label='P&L')
    plt.legend()
    plt.grid()
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Single Path Hedging Results (Merton Model with Jumps)')
    plt.tight_layout()


def plot_pnl_histogram(pnl_final):
    """
    Plot histogram of final P&L across all paths.

    Parameters
    ----------
    pnl_final : ndarray
        Final P&L values for all paths.
    """
    plt.figure(2, figsize=(10, 6))
    plt.hist(pnl_final, 100)
    plt.grid()
    plt.xlim([-0.1, 0.1])
    plt.xlabel('Final P&L')
    plt.ylabel('Frequency')
    plt.title('Distribution of Final Hedging P&L (with Jumps)')
    plt.tight_layout()


# =============================================================================
# 5. Main
# =============================================================================

def main():
    """Run delta hedging simulation with Merton jump-diffusion model."""
    # ===== Parameters =====
    num_paths = 1000
    num_steps = 5000
    maturity = 1.0
    r = 0.1  # Risk-free rate
    sigma = 0.2  # Volatility (diffusion)
    jump_intensity = 1.0  # Poisson jump intensity
    jump_mean = 0.0  # Mean of log-jump size
    jump_std = 0.25  # Std dev of log-jump size
    s0 = 1.0  # Initial stock price
    strikes = [0.95]
    option_type = OptionType.CALL

    np.random.seed(7)
    paths = generate_paths_merton(num_paths, num_steps, s0, maturity, jump_intensity,
                                  jump_mean, jump_std, r, sigma)
    time = paths["time"]
    stock = paths["S"]

    # ===== Hedging Setup =====
    # Define callable functions for option pricing and delta
    def option_price_func(t, strike, spot):
        return bs_call_put_option_price(option_type, spot, strike, sigma, t, maturity, r)

    def delta_func(t, strike, spot):
        return bs_delta(option_type, spot, strike, sigma, t, maturity, r)

    # Initialize portfolio
    pnl = np.zeros((num_paths, num_steps + 1))
    delta_init = delta_func(0.0, strikes, s0)
    pnl[:, 0] = option_price_func(0.0, strikes, s0) - delta_init * s0

    # Track option prices and deltas
    call_matrix = np.zeros((num_paths, num_steps + 1))
    call_matrix[:, 0] = option_price_func(0.0, strikes, s0)
    delta_matrix = np.zeros((num_paths, num_steps + 1))
    delta_matrix[:, 0] = delta_func(0.0, strikes, s0)

    # ===== Dynamic Hedging Loop =====
    for i in range(1, num_steps + 1):
        dt = time[i] - time[i - 1]
        delta_old = delta_func(time[i - 1], strikes, stock[:, i - 1])
        delta_curr = delta_func(time[i], strikes, stock[:, i])

        # Update P&L: accrue interest and rehedge
        pnl[:, i] = pnl[:, i - 1] * np.exp(r * dt) - (delta_curr - delta_old) * stock[:, i]
        call_matrix[:, i] = option_price_func(time[i], strikes, stock[:, i])
        delta_matrix[:, i] = delta_curr

    # Final settlement: pay option payoff and liquidate hedge
    pnl[:, -1] = pnl[:, -1] - np.maximum(stock[:, -1] - np.array(strikes), 0) + delta_matrix[:, -1] * stock[:, -1]

    # ===== Results Analysis =====
    path_id = 10
    plot_single_path_results(time, stock[path_id, :], call_matrix[path_id, :],
                            delta_matrix[path_id, :], pnl[path_id, :])
    plot_pnl_histogram(pnl[:, -1])
    plt.show()

    # Print sample results
    print("Path Analysis (Merton Model with Jumps):")
    print("path_id={0}, S0={1}, PnL(T-1)={2}, S(T)={3}, max(S(T)-K,0)={4}, PnL(T)={5}".format(
        path_id, s0, pnl[path_id, -2], stock[path_id, -1],
        np.maximum(stock[path_id, -1] - np.array(strikes), 0.0)[0], pnl[path_id, -1]))


if __name__ == "__main__":
    main()
