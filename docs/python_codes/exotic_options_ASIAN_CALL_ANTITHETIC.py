"""
Exotic Options: Asian Call Pricing with Antithetic Variates

This script demonstrates variance reduction via antithetic variates for pricing
an arithmetic average Asian call option. Each simulation pairs a path generated
with random draws {Z_k} with its mirror path using {-Z_k}, and averages the
two payoffs. This negative correlation between paired payoffs reduces variance.

Mathematical Framework:
    - Original path:    S_path1 using increments +sigma*sqrt(dt)*Z
    - Antithetic path:  S_path2 using increments -sigma*sqrt(dt)*Z
    - Combined payoff:  Phi_anti = 0.5 * [Phi(path1) + Phi(path2)]
    - Variance reduction: Var(Phi_anti) < Var(Phi) when Cov(Phi1, Phi2) < 0

References:
    - Glasserman (2003). Monte Carlo Methods in Financial Engineering, Ch. 4.
"""

import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# 1. Standard Monte Carlo (baseline)
# =============================================================================

def asian_call_standard(S, K, T, r, sigma, M, N, seed=None):
    """Standard Monte Carlo for Asian call (no variance reduction)."""
    if seed is not None:
        np.random.seed(seed)

    dt = T / M
    payoff = np.zeros(N)

    for i in range(N):
        z = np.random.normal(size=M)
        increments = (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z
        S_path = S * np.exp(np.cumsum(increments))
        S_path = np.insert(S_path, 0, S)
        avg_price = np.mean(S_path)
        payoff[i] = max(avg_price - K, 0)

    disc_payoff = np.exp(-r * T) * payoff
    price = np.mean(disc_payoff)
    se = np.std(disc_payoff) / np.sqrt(N)
    return price, se, disc_payoff


# =============================================================================
# 2. Antithetic Variates Monte Carlo
# =============================================================================

def asian_call_antithetic(S, K, T, r, sigma, M, N, seed=None):
    """
    Asian call with antithetic variates variance reduction.

    For each simulation, generates two paths using +Z and -Z,
    then averages the payoffs. This reduces variance when the
    payoff function is monotone in the random inputs.

    Parameters
    ----------
    S, K, T, r, sigma : float
        Standard option parameters.
    M : int
        Number of time steps per path.
    N : int
        Number of paired simulations (total paths = 2N).

    Returns
    -------
    price : float
        Estimated option price.
    se : float
        Standard error.
    payoffs : ndarray
        Averaged discounted payoffs.
    """
    if seed is not None:
        np.random.seed(seed)

    dt = T / M
    payoff = np.zeros(N)

    for i in range(N):
        z = np.random.normal(size=M)

        # Original path
        increments1 = (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z
        S_path1 = S * np.exp(np.cumsum(increments1))
        S_path1 = np.insert(S_path1, 0, S)

        # Antithetic path (negate Z)
        increments2 = (r - 0.5 * sigma**2) * dt - sigma * np.sqrt(dt) * z
        S_path2 = S * np.exp(np.cumsum(increments2))
        S_path2 = np.insert(S_path2, 0, S)

        avg1 = np.mean(S_path1)
        avg2 = np.mean(S_path2)

        payoff[i] = 0.5 * (max(avg1 - K, 0) + max(avg2 - K, 0))

    disc_payoff = np.exp(-r * T) * payoff
    price = np.mean(disc_payoff)
    se = np.std(disc_payoff) / np.sqrt(N)
    return price, se, disc_payoff


# =============================================================================
# 3. Main: Comparison and Analysis
# =============================================================================

if __name__ == "__main__":
    # Parameters
    S = 100
    K = 100
    T = 1
    r = 0.05
    sigma = 0.2
    M = 252
    N = 50000

    print("=" * 65)
    print("ASIAN CALL PRICING: Antithetic Variates vs Standard MC")
    print("=" * 65)
    print(f"Parameters: S={S}, K={K}, T={T}, r={r}, sigma={sigma}")
    print(f"Paths: N={N}, Steps: M={M}")
    print()

    # --- Run both methods ---
    std_price, std_se, std_payoffs = asian_call_standard(
        S, K, T, r, sigma, M, N, seed=42
    )
    anti_price, anti_se, anti_payoffs = asian_call_antithetic(
        S, K, T, r, sigma, M, N, seed=42
    )

    # Variance reduction ratio
    var_ratio = std_se**2 / anti_se**2

    print(f"{'Method':<25} {'Price':>10} {'Std Error':>10} {'Variance':>12}")
    print("-" * 60)
    print(f"{'Standard MC':<25} {std_price:10.4f} {std_se:10.4f} {std_se**2:12.6f}")
    print(f"{'Antithetic Variates':<25} {anti_price:10.4f} {anti_se:10.4f} {anti_se**2:12.6f}")
    print(f"\nVariance Reduction Ratio: {var_ratio:.2f}x")
    print(f"Effective sample size multiplier: {var_ratio:.2f}x")

    # --- Convergence comparison ---
    N_values = [500, 1000, 2000, 5000, 10000, 20000, 50000]
    std_ses = []
    anti_ses = []

    for n in N_values:
        _, se_s, _ = asian_call_standard(S, K, T, r, sigma, M, n, seed=42)
        _, se_a, _ = asian_call_antithetic(S, K, T, r, sigma, M, n, seed=42)
        std_ses.append(se_s)
        anti_ses.append(se_a)

    # --- Plots ---
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1: Standard error comparison
    axes[0].plot(N_values, std_ses, 'ro-', markersize=5, label='Standard MC')
    axes[0].plot(N_values, anti_ses, 'bo-', markersize=5, label='Antithetic')
    axes[0].set_xlabel('Number of Simulations (N)')
    axes[0].set_ylabel('Standard Error')
    axes[0].set_title('Standard Error: Standard vs Antithetic')
    axes[0].set_xscale('log')
    axes[0].set_yscale('log')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Panel 2: Payoff distribution comparison
    axes[1].hist(std_payoffs[std_payoffs > 0], bins=50, alpha=0.5,
                 label='Standard MC', density=True, color='red')
    axes[1].hist(anti_payoffs[anti_payoffs > 0], bins=50, alpha=0.5,
                 label='Antithetic', density=True, color='blue')
    axes[1].set_xlabel('Discounted Payoff')
    axes[1].set_ylabel('Density')
    axes[1].set_title('Payoff Distributions (Non-Zero)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    # Panel 3: Variance reduction ratio across N
    ratios = [s**2 / a**2 for s, a in zip(std_ses, anti_ses)]
    axes[2].bar(range(len(N_values)), ratios, color='steelblue',
                edgecolor='black', alpha=0.8)
    axes[2].set_xticks(range(len(N_values)))
    axes[2].set_xticklabels([str(n) for n in N_values], rotation=45)
    axes[2].set_xlabel('Number of Simulations (N)')
    axes[2].set_ylabel('Variance Reduction Ratio')
    axes[2].set_title('Antithetic Variance Reduction Factor')
    axes[2].axhline(y=1, color='r', linestyle='--', alpha=0.5, label='No reduction')
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('asian_call_antithetic.png', dpi=150, bbox_inches='tight')
    plt.show()

    print("\nPlot saved to asian_call_antithetic.png")
