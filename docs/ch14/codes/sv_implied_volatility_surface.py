"""
Stochastic Volatility Model and Implied Volatility Surface Analysis

This module provides a pedagogical introduction to stochastic volatility models.
Unlike classical Black-Scholes where volatility is constant, here we implement
a GBM model where the volatility itself is random, drawn from a normal distribution.

The SDE is:
    dS_t = r * S_t dt + sigma_t * S_t dW_t
    where sigma_t ~ N(mu_sigma, sigma_sigma)

This demonstrates how different securities can have different implied volatilities
(the "smile" or "skew") even when fundamentally priced by the same model.

Based on: QuantPie Lecture Notes
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.stats import norm


def generate_sample_path(num_paths, num_steps, S0, T, mu_J, sigma_J, r, seed=None):
    """
    Generate sample paths under stochastic volatility GBM.

    Parameters
    ----------
    num_paths : int
        Number of Monte Carlo paths
    num_steps : int
        Number of time steps
    S0 : float
        Initial stock price
    T : float
        Time to maturity (in years)
    mu_J : float
        Mean of volatility distribution
    sigma_J : float
        Standard deviation of volatility distribution
    r : float
        Risk-free rate
    seed : int, optional
        Random seed for reproducibility

    Returns
    -------
    t : ndarray
        Time grid (num_steps + 1,)
    X : ndarray
        Log prices (num_paths, num_steps + 1)
    S : ndarray
        Stock prices (num_paths, num_steps + 1)
    J : ndarray
        Volatilities for each path (num_paths,)

    Notes
    -----
    The volatility for each path is drawn once at t=0 and held constant
    along that path. The process is:
        dS/S = r dt + J dW
    which gives:
        X = log(S) evolves as dX = (r - 0.5*J^2) dt + J dW
    """
    if seed is not None:
        np.random.seed(seed)

    # Draw volatilities for each path (constant along each path)
    J = np.random.normal(mu_J, sigma_J, (num_paths,))

    # Draw Brownian increments
    Z = np.random.normal(0.0, 1.0, (num_paths, num_steps))

    # Initialize log-price paths
    X = np.ones((num_paths, num_steps + 1)) * np.log(S0)

    # Time grid
    t = np.linspace(0, T, num_steps + 1)
    dt = t[1] - t[0]
    sqrt_dt = np.sqrt(dt)

    # Euler discretization
    for i in range(num_steps):
        # Standardize increments for better numerical stability
        if num_paths > 1:
            Z[:, i] = (Z[:, i] - Z[:, i].mean()) / Z[:, i].std()

        # dX = (r - 0.5*J^2) dt + J * sqrt(dt) * Z
        X[:, i+1] = X[:, i] + (r - 0.5 * J**2) * dt + J * sqrt_dt * Z[:, i]

    S = np.exp(X)
    return t, X, S, J


def bs_call_price(S, K, T, r, sigma):
    """
    Black-Scholes call option price.

    Parameters
    ----------
    S : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to expiration (in years)
    r : float
        Risk-free rate
    sigma : float
        Volatility (annualized)

    Returns
    -------
    float
        Call option price
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return price


def bs_put_price(S, K, T, r, sigma):
    """Black-Scholes put option price."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return price


def bs_vega(S, K, T, r, sigma):
    """
    Black-Scholes vega (derivative of price w.r.t. volatility).

    Returns
    -------
    float
        Vega per 1% change in volatility
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T)
    return vega / 100  # Per 1% volatility


def implied_volatility(market_price, S, K, T, r, option_type='call', initial_guess=0.2):
    """
    Compute implied volatility using Brent's method.

    Parameters
    ----------
    market_price : float
        Observed option price
    S : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to expiration
    r : float
        Risk-free rate
    option_type : str
        'call' or 'put'
    initial_guess : float
        Initial volatility guess

    Returns
    -------
    float
        Implied volatility
    """
    if option_type == 'call':
        def objective(sigma):
            return bs_call_price(S, K, T, r, sigma) - market_price
    else:
        def objective(sigma):
            return bs_put_price(S, K, T, r, sigma) - market_price

    try:
        # Brent's method on interval [0.01, 5.0]
        iv = brentq(objective, 0.01, 5.0)
        return iv
    except ValueError:
        # If no solution found in bracket, return NaN
        return np.nan


def main():
    """
    Demonstrate stochastic volatility model and implied volatility surface.

    This function:
    1. Generates MC paths under stochastic volatility
    2. Compares terminal distributions with constant volatility baseline
    3. Computes an implied volatility smile/skew
    """
    np.random.seed(42)

    # Parameters
    num_paths = 500
    num_steps = 100
    S0 = 100.0
    K = 100.0
    T = 1.0
    r = 0.05
    mu_J = 0.20  # Mean volatility
    sigma_J = 0.08  # Volatility of volatility

    print("=" * 70)
    print("Stochastic Volatility Model Demonstration")
    print("=" * 70)
    print(f"Parameters: S0={S0}, K={K}, T={T} years, r={r}, mu_vol={mu_J}, sigma_vol={sigma_J}")
    print()

    # Generate paths under stochastic volatility
    t, X, S, J = generate_sample_path(num_paths, num_steps, S0, T, mu_J, sigma_J, r, seed=42)

    # For comparison: generate paths with constant volatility (mean of the distribution)
    np.random.seed(42)
    Z_const = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    X_const = np.ones((num_paths, num_steps + 1)) * np.log(S0)
    dt = T / num_steps
    sqrt_dt = np.sqrt(dt)
    for i in range(num_steps):
        if num_paths > 1:
            Z_const[:, i] = (Z_const[:, i] - Z_const[:, i].mean()) / Z_const[:, i].std()
        X_const[:, i+1] = X_const[:, i] + (r - 0.5 * mu_J**2) * dt + mu_J * sqrt_dt * Z_const[:, i]
    S_const = np.exp(X_const)

    # Print volatility statistics
    print(f"Realized volatility statistics across paths:")
    print(f"  Mean:   {J.mean():.4f}")
    print(f"  Std:    {J.std():.4f}")
    print(f"  Min:    {J.min():.4f}")
    print(f"  Max:    {J.max():.4f}")
    print()

    # Terminal payoffs
    terminal_prices_sv = S[:, -1]
    terminal_prices_cv = S_const[:, -1]
    call_payoff = np.maximum(terminal_prices_sv - K, 0)

    call_price_sv = np.exp(-r * T) * np.mean(call_payoff)
    call_price_cv = bs_call_price(S0, K, T, r, mu_J)

    print(f"Call option price (K={K}):")
    print(f"  Stochastic Vol (MC):  {call_price_sv:.4f}")
    print(f"  Constant Vol (BS):    {call_price_cv:.4f}")
    print()

    # Compute implied volatility surface
    strikes = np.linspace(80, 120, 9)
    market_prices = []
    implied_vols = []

    print("Implied Volatility Smile (computed from SV model prices):")
    print(f"  Strike  |  Market Price  |  Implied Vol")
    print("  " + "-" * 45)

    for K_test in strikes:
        payoff = np.maximum(terminal_prices_sv - K_test, 0)
        market_price = np.exp(-r * T) * np.mean(payoff)
        market_prices.append(market_price)

        # Compute IV
        if market_price > 1e-6:
            iv = implied_volatility(market_price, S0, K_test, T, r, option_type='call')
        else:
            iv = np.nan

        implied_vols.append(iv)
        print(f"  {K_test:6.1f}  |    {market_price:8.4f}    |  {iv:7.4f}")

    print()

    # Create visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Plot 1: Sample paths colored by volatility
    ax = axes[0, 0]
    sample_indices = np.arange(0, num_paths, max(1, num_paths // 50))
    for idx in sample_indices:
        color = plt.cm.viridis(J[idx] / J.max())
        ax.plot(t, S[idx, :], alpha=0.3, color=color, linewidth=0.8)
    sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis,
                                norm=plt.Normalize(vmin=J.min(), vmax=J.max()))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Volatility')
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('Stock Price')
    ax.set_title('Sample Paths (Colored by Volatility)')
    ax.grid(True, alpha=0.3)

    # Plot 2: Terminal distribution comparison
    ax = axes[0, 1]
    ax.hist(terminal_prices_sv, bins=40, alpha=0.6, label='Stochastic Vol', density=True)
    ax.hist(terminal_prices_cv, bins=40, alpha=0.6, label='Constant Vol', density=True)
    ax.axvline(K, color='red', linestyle='--', linewidth=2, label=f'Strike (K={K})')
    ax.set_xlabel('Stock Price at T')
    ax.set_ylabel('Density')
    ax.set_title('Terminal Distribution: Stochastic vs Constant Volatility')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 3: IV Smile
    ax = axes[1, 0]
    valid_mask = ~np.isnan(implied_vols)
    ax.plot(np.array(strikes)[valid_mask], np.array(implied_vols)[valid_mask],
            'bo-', linewidth=2, markersize=8)
    ax.axhline(mu_J, color='red', linestyle='--', linewidth=2, label=f'Mean Vol = {mu_J:.3f}')
    ax.set_xlabel('Strike Price')
    ax.set_ylabel('Implied Volatility')
    ax.set_title('Implied Volatility Smile')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 4: Distribution of realized volatilities
    ax = axes[1, 1]
    ax.hist(J, bins=30, alpha=0.7, density=True, edgecolor='black')
    x_range = np.linspace(J.min(), J.max(), 100)
    theoretical = norm.pdf(x_range, mu_J, sigma_J)
    ax.plot(x_range, theoretical, 'r-', linewidth=2, label='Theoretical N(μ,σ²)')
    ax.set_xlabel('Volatility')
    ax.set_ylabel('Density')
    ax.set_title('Distribution of Realized Volatilities')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('sv_implied_volatility_surface.png', dpi=150, bbox_inches='tight')
    print("Figure saved as 'sv_implied_volatility_surface.png'")
    plt.show()


if __name__ == '__main__':
    main()
