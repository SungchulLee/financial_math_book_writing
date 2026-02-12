"""
Exotic Options: Arithmetic Average Asian Call Pricing via Monte Carlo

This script prices an arithmetic average Asian call option using basic Monte Carlo
simulation. The payoff depends on the average price of the underlying over the
option's life: Payoff = max(S_avg - K, 0).

Mathematical Framework:
    - GBM path simulation:
        S_{t+dt} = S_t * exp((r - 0.5*sigma^2)*dt + sigma*sqrt(dt)*Z)
    - Arithmetic average: S_avg = (1/n) * sum(S_{t_i})
    - Option price: V = exp(-rT) * E[max(S_avg - K, 0)]

Also prices a lookback call by replacing the average with the path maximum.

References:
    - Glasserman (2003). Monte Carlo Methods in Financial Engineering.
"""

import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# 1. Asian Call Monte Carlo
# =============================================================================

def asian_call_monte_carlo(S, K, T, r, sigma, M, N, seed=None):
    """
    Price an arithmetic average Asian call via Monte Carlo.

    Parameters
    ----------
    S : float
        Current stock price.
    K : float
        Strike price.
    T : float
        Time to maturity (years).
    r : float
        Risk-free rate (annualized).
    sigma : float
        Volatility (annualized).
    M : int
        Number of time steps per path.
    N : int
        Number of simulated paths.
    seed : int, optional
        Random seed for reproducibility.

    Returns
    -------
    price : float
        Estimated option price.
    se : float
        Standard error of the estimate.
    payoffs : ndarray
        Individual discounted payoffs (for analysis).
    """
    if seed is not None:
        np.random.seed(seed)

    dt = T / M
    payoff = np.zeros(N)

    for i in range(N):
        S_path = [S]
        for _ in range(M):
            z = np.random.normal()
            S_next = S_path[-1] * np.exp(
                (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z
            )
            S_path.append(S_next)
        avg_price = np.mean(S_path)
        payoff[i] = max(avg_price - K, 0)

    disc_payoff = np.exp(-r * T) * payoff
    price = np.mean(disc_payoff)
    se = np.std(disc_payoff) / np.sqrt(N)
    return price, se, disc_payoff


# =============================================================================
# 2. Lookback Call Monte Carlo
# =============================================================================

def lookback_call_monte_carlo(S, K, T, r, sigma, M, N, seed=None):
    """
    Price a fixed-strike lookback call via Monte Carlo.
    Payoff = max(S_max - K, 0) where S_max = max over the path.
    """
    if seed is not None:
        np.random.seed(seed)

    dt = T / M
    payoff = np.zeros(N)

    for i in range(N):
        S_path = [S]
        for _ in range(M):
            z = np.random.normal()
            S_next = S_path[-1] * np.exp(
                (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z
            )
            S_path.append(S_next)
        S_max = max(S_path)
        payoff[i] = max(S_max - K, 0)

    disc_payoff = np.exp(-r * T) * payoff
    price = np.mean(disc_payoff)
    se = np.std(disc_payoff) / np.sqrt(N)
    return price, se, disc_payoff


# =============================================================================
# 3. Black-Scholes Vanilla Call (benchmark)
# =============================================================================

def black_scholes_call(S, K, T, r, sigma):
    """Analytical Black-Scholes call price."""
    from scipy.stats import norm
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


# =============================================================================
# 4. Main: Pricing and Analysis
# =============================================================================

if __name__ == "__main__":
    # Parameters
    S = 100       # Current stock price
    K = 100       # Strike price
    T = 1         # Time to maturity
    r = 0.05      # Risk-free rate
    sigma = 0.2   # Volatility
    M = 252       # Daily time steps
    N = 50000     # Number of simulations

    np.random.seed(42)

    # --- Price all three option types ---
    bs_price = black_scholes_call(S, K, T, r, sigma)
    asian_price, asian_se, asian_payoffs = asian_call_monte_carlo(
        S, K, T, r, sigma, M, N
    )
    lookback_price, lookback_se, lookback_payoffs = lookback_call_monte_carlo(
        S, K, T, r, sigma, M, N
    )

    print("=" * 65)
    print("EXOTIC OPTION PRICING: Monte Carlo Simulation")
    print("=" * 65)
    print(f"Parameters: S={S}, K={K}, T={T}, r={r}, sigma={sigma}")
    print(f"Paths: N={N}, Steps: M={M}")
    print()
    print(f"{'Option Type':<25} {'Price':>10} {'Std Error':>10} {'95% CI':>20}")
    print("-" * 65)
    print(f"{'Vanilla Call (BS)':<25} {bs_price:10.4f} {'(exact)':>10} {'':>20}")
    print(f"{'Asian Call (Arith Avg)':<25} {asian_price:10.4f} {asian_se:10.4f}"
          f" [{asian_price-1.96*asian_se:.4f}, {asian_price+1.96*asian_se:.4f}]")
    print(f"{'Lookback Call (Fixed K)':<25} {lookback_price:10.4f} {lookback_se:10.4f}"
          f" [{lookback_price-1.96*lookback_se:.4f}, {lookback_price+1.96*lookback_se:.4f}]")

    print(f"\nPrice ordering: Asian ({asian_price:.4f}) < Vanilla ({bs_price:.4f})"
          f" < Lookback ({lookback_price:.4f})")

    # --- Convergence Analysis ---
    N_values = [100, 500, 1000, 5000, 10000, 25000, 50000]
    asian_conv = []
    asian_se_conv = []

    for n in N_values:
        p, se, _ = asian_call_monte_carlo(S, K, T, r, sigma, M, n, seed=42)
        asian_conv.append(p)
        asian_se_conv.append(se)

    # --- Plots ---
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Payoff distributions
    axes[0, 0].hist(asian_payoffs[asian_payoffs > 0], bins=50, alpha=0.6,
                    label='Asian Call', density=True, color='blue')
    axes[0, 0].hist(lookback_payoffs[lookback_payoffs > 0], bins=50, alpha=0.6,
                    label='Lookback Call', density=True, color='red')
    axes[0, 0].set_xlabel('Discounted Payoff')
    axes[0, 0].set_ylabel('Density')
    axes[0, 0].set_title('Payoff Distributions (Non-Zero Payoffs)')
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # Panel 2: Convergence of Asian call price
    axes[0, 1].errorbar(N_values, asian_conv,
                        yerr=[1.96 * se for se in asian_se_conv],
                        fmt='bo-', capsize=3, markersize=5, label='MC Estimate ± 95% CI')
    axes[0, 1].axhline(y=asian_conv[-1], color='k', linestyle='--', alpha=0.5)
    axes[0, 1].set_xlabel('Number of Simulations (N)')
    axes[0, 1].set_ylabel('Asian Call Price')
    axes[0, 1].set_title('Convergence of Asian Call Price')
    axes[0, 1].set_xscale('log')
    axes[0, 1].legend()
    axes[0, 1].grid(True, alpha=0.3)

    # Panel 3: Standard error decay
    axes[1, 0].plot(N_values, asian_se_conv, 'ro-', markersize=5, label='Empirical SE')
    # Theoretical O(1/sqrt(N)) line
    se_theory = asian_se_conv[0] * np.sqrt(N_values[0]) / np.sqrt(N_values)
    axes[1, 0].plot(N_values, se_theory, 'k--', alpha=0.5, label=r'$O(1/\sqrt{N})$')
    axes[1, 0].set_xlabel('Number of Simulations (N)')
    axes[1, 0].set_ylabel('Standard Error')
    axes[1, 0].set_title('Standard Error Decay')
    axes[1, 0].set_xscale('log')
    axes[1, 0].set_yscale('log')
    axes[1, 0].legend()
    axes[1, 0].grid(True, alpha=0.3)

    # Panel 4: Price comparison bar chart
    option_types = ['Asian Call', 'Vanilla Call\n(BS)', 'Lookback Call']
    prices = [asian_price, bs_price, lookback_price]
    colors = ['steelblue', 'gray', 'coral']
    axes[1, 1].bar(option_types, prices, color=colors, edgecolor='black', alpha=0.8)
    axes[1, 1].set_ylabel('Option Price')
    axes[1, 1].set_title('Price Comparison: Asian < Vanilla < Lookback')
    axes[1, 1].grid(True, alpha=0.3, axis='y')
    for i, (ot, p) in enumerate(zip(option_types, prices)):
        axes[1, 1].text(i, p + 0.3, f'{p:.2f}', ha='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig('exotic_options_monte_carlo.png', dpi=150, bbox_inches='tight')
    plt.show()

    print("\nPlots saved to exotic_options_monte_carlo.png")
