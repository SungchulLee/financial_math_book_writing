"""
Exotic Options: Asian Call Pricing with Control Variates

This script demonstrates variance reduction via control variates for pricing
an arithmetic average Asian call. The European call (with known Black-Scholes
price) serves as the control variate, correcting systematic Monte Carlo errors.

Mathematical Framework:
    - Control variate estimator:
        V_asian_adj = V_asian_MC + (C_BS - C_MC)
    - The correction (C_BS - C_MC) removes the systematic error shared
      between the Asian and European payoff estimates.
    - Variance reduction is proportional to Corr(Asian_payoff, Euro_payoff)^2.

Also demonstrates using the geometric average Asian option as a superior
control variate (higher correlation with the arithmetic average).

References:
    - Glasserman (2003). Monte Carlo Methods in Financial Engineering, Ch. 4.
    - Kemna, Vorst (1990). A pricing method for options based upon average values.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# =============================================================================
# 1. Black-Scholes Call Price
# =============================================================================

def black_scholes_call(S, K, T, r, sigma):
    """Analytical Black-Scholes European call price."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


# =============================================================================
# 2. Standard Asian Call Monte Carlo (baseline)
# =============================================================================

def asian_call_standard(S, K, T, r, sigma, M, N, seed=None):
    """Standard MC for Asian call."""
    if seed is not None:
        np.random.seed(seed)

    dt = T / M
    asian_payoff = np.zeros(N)

    for i in range(N):
        S_path = [S]
        for _ in range(M):
            z = np.random.normal()
            S_next = S_path[-1] * np.exp(
                (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z
            )
            S_path.append(S_next)
        avg_price = np.mean(S_path)
        asian_payoff[i] = np.exp(-r * T) * max(avg_price - K, 0)

    price = np.mean(asian_payoff)
    se = np.std(asian_payoff) / np.sqrt(N)
    return price, se


# =============================================================================
# 3. Control Variate: European Call
# =============================================================================

def asian_call_control_variate(S, K, T, r, sigma, M, N, seed=None):
    """
    Asian call with European call as control variate.

    Uses the known Black-Scholes price to correct the MC estimate:
        V_asian_adj[i] = V_asian[i] + (C_BS - C_MC_mean)

    Parameters
    ----------
    S, K, T, r, sigma : float
        Standard option parameters.
    M : int
        Number of time steps per path.
    N : int
        Number of simulated paths.

    Returns
    -------
    price : float
        Control-variate-adjusted price.
    se : float
        Standard error of the adjusted estimate.
    """
    if seed is not None:
        np.random.seed(seed)

    dt = T / M
    euro_payoff = np.zeros(N)
    asian_payoff = np.zeros(N)

    for i in range(N):
        S_path = [S]
        for _ in range(M):
            z = np.random.normal()
            S_next = S_path[-1] * np.exp(
                (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z
            )
            S_path.append(S_next)

        avg_price = np.mean(S_path)
        euro_final = S_path[-1]

        asian_payoff[i] = np.exp(-r * T) * max(avg_price - K, 0)
        euro_payoff[i] = np.exp(-r * T) * max(euro_final - K, 0)

    # Control variate adjustment
    euro_mc = np.mean(euro_payoff)
    euro_bs = black_scholes_call(S, K, T, r, sigma)
    adj_asian = asian_payoff + (euro_bs - euro_mc)

    price = np.mean(adj_asian)
    se = np.std(adj_asian) / np.sqrt(N)
    return price, se


# =============================================================================
# 4. Control Variate: Geometric Average Asian Call
# =============================================================================

def geometric_asian_call_exact(S, K, T, r, sigma):
    """
    Exact price of a continuous geometric average Asian call.

    Under GBM, the geometric average is lognormal with adjusted parameters:
        sigma_hat = sigma / sqrt(3)
        r_hat = 0.5 * (r - sigma^2/6)
    """
    sigma_hat = sigma / np.sqrt(3)
    r_hat = 0.5 * (r - sigma**2 / 6)
    S_hat = S * np.exp((r_hat - r) * T)

    d1 = (np.log(S_hat / K) + (r_hat + 0.5 * sigma_hat**2) * T) / (sigma_hat * np.sqrt(T))
    d2 = d1 - sigma_hat * np.sqrt(T)

    return np.exp(-r * T) * (S_hat * np.exp(r_hat * T) * norm.cdf(d1) - K * norm.cdf(d2))


def asian_call_geometric_cv(S, K, T, r, sigma, M, N, seed=None):
    """
    Asian call with geometric average Asian call as control variate.

    The geometric average is more highly correlated with the arithmetic
    average than the European terminal price, providing superior variance
    reduction.
    """
    if seed is not None:
        np.random.seed(seed)

    dt = T / M
    arith_payoff = np.zeros(N)
    geom_payoff = np.zeros(N)

    for i in range(N):
        S_path = [S]
        for _ in range(M):
            z = np.random.normal()
            S_next = S_path[-1] * np.exp(
                (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z
            )
            S_path.append(S_next)

        arith_avg = np.mean(S_path)
        geom_avg = np.exp(np.mean(np.log(S_path)))

        arith_payoff[i] = np.exp(-r * T) * max(arith_avg - K, 0)
        geom_payoff[i] = np.exp(-r * T) * max(geom_avg - K, 0)

    # Control variate adjustment
    geom_mc = np.mean(geom_payoff)
    geom_exact = geometric_asian_call_exact(S, K, T, r, sigma)
    adj_arith = arith_payoff + (geom_exact - geom_mc)

    price = np.mean(adj_arith)
    se = np.std(adj_arith) / np.sqrt(N)
    return price, se


# =============================================================================
# 5. Main: Comparison
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

    print("=" * 70)
    print("ASIAN CALL PRICING: Control Variate Methods")
    print("=" * 70)
    print(f"Parameters: S={S}, K={K}, T={T}, r={r}, sigma={sigma}")
    print(f"Paths: N={N}, Steps: M={M}")
    print()

    # --- Run all three methods ---
    std_price, std_se = asian_call_standard(S, K, T, r, sigma, M, N, seed=42)
    cv_euro_price, cv_euro_se = asian_call_control_variate(
        S, K, T, r, sigma, M, N, seed=42
    )
    cv_geom_price, cv_geom_se = asian_call_geometric_cv(
        S, K, T, r, sigma, M, N, seed=42
    )

    # Reference values
    bs_price = black_scholes_call(S, K, T, r, sigma)
    geom_price = geometric_asian_call_exact(S, K, T, r, sigma)

    print(f"Reference: BS Call = {bs_price:.4f}, Geometric Asian = {geom_price:.4f}")
    print()

    print(f"{'Method':<30} {'Price':>10} {'Std Err':>10} {'Var Ratio':>10}")
    print("-" * 62)
    print(f"{'Standard MC':<30} {std_price:10.4f} {std_se:10.4f} {'1.00':>10}")
    print(f"{'CV: European Call':<30} {cv_euro_price:10.4f} {cv_euro_se:10.4f}"
          f" {std_se**2/cv_euro_se**2:10.2f}")
    print(f"{'CV: Geometric Asian':<30} {cv_geom_price:10.4f} {cv_geom_se:10.4f}"
          f" {std_se**2/cv_geom_se**2:10.2f}")

    # --- Convergence comparison ---
    N_values = [500, 1000, 2000, 5000, 10000, 25000, 50000]
    results = {'Standard': [], 'CV Euro': [], 'CV Geom': []}

    for n in N_values:
        _, se1 = asian_call_standard(S, K, T, r, sigma, M, n, seed=42)
        _, se2 = asian_call_control_variate(S, K, T, r, sigma, M, n, seed=42)
        _, se3 = asian_call_geometric_cv(S, K, T, r, sigma, M, n, seed=42)
        results['Standard'].append(se1)
        results['CV Euro'].append(se2)
        results['CV Geom'].append(se3)

    # --- Plots ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Panel 1: Standard error comparison
    axes[0].plot(N_values, results['Standard'], 'ro-', markersize=5, label='Standard MC')
    axes[0].plot(N_values, results['CV Euro'], 'go-', markersize=5, label='CV: European')
    axes[0].plot(N_values, results['CV Geom'], 'bo-', markersize=5, label='CV: Geometric')
    axes[0].set_xlabel('Number of Simulations (N)')
    axes[0].set_ylabel('Standard Error')
    axes[0].set_title('Standard Error Comparison')
    axes[0].set_xscale('log')
    axes[0].set_yscale('log')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Panel 2: Variance reduction ratios
    ratios_euro = [s**2 / e**2 for s, e in zip(results['Standard'], results['CV Euro'])]
    ratios_geom = [s**2 / g**2 for s, g in zip(results['Standard'], results['CV Geom'])]

    x = np.arange(len(N_values))
    width = 0.35
    axes[1].bar(x - width/2, ratios_euro, width, label='CV: European',
                color='green', alpha=0.7, edgecolor='black')
    axes[1].bar(x + width/2, ratios_geom, width, label='CV: Geometric',
                color='blue', alpha=0.7, edgecolor='black')
    axes[1].set_xticks(x)
    axes[1].set_xticklabels([str(n) for n in N_values], rotation=45)
    axes[1].set_xlabel('Number of Simulations (N)')
    axes[1].set_ylabel('Variance Reduction Ratio')
    axes[1].set_title('Variance Reduction: Euro vs Geometric CV')
    axes[1].axhline(y=1, color='r', linestyle='--', alpha=0.5)
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('asian_call_control_variate.png', dpi=150, bbox_inches='tight')
    plt.show()

    print("\nPlot saved to asian_call_control_variate.png")
