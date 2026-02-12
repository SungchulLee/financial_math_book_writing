"""
Exotic Options: Down-and-Out Barrier Call Pricing via Binomial Tree

This script implements the CRR binomial tree for a down-and-out barrier call option.
The barrier condition is enforced at every node: if the stock price falls to or below
the barrier H, the option value is set to zero (knocked out).

Mathematical Framework:
    - CRR parameters: u = exp(σ√Δt), d = 1/u, q = (exp(rΔt) - d) / (u - d)
    - Stock price at node (n,j): S_{n,j} = S₀ · u^j · d^(n-j)
    - Backward induction with barrier:
        V_{n,j} = exp(-rΔt)[q·V_{n+1,j+1} + (1-q)·V_{n+1,j}]  if S_{n,j} > H
        V_{n,j} = 0                                               if S_{n,j} ≤ H

References:
    - Cox, Ross, Rubinstein (1979). Option pricing: A simplified approach.
    - Rubinstein, Reiner (1991). Breaking down the barriers.
"""

import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# 1. Barrier Call Binomial Pricing Function
# =============================================================================

def barrier_call_binomial(S, K, H, T, r, sigma, N):
    """
    Price a down-and-out barrier call option using a CRR binomial tree.

    Parameters
    ----------
    S : float
        Current stock price.
    K : float
        Strike price.
    H : float
        Down-and-out barrier level (H < S).
    T : float
        Time to maturity (years).
    r : float
        Risk-free rate (annualized).
    sigma : float
        Volatility (annualized).
    N : int
        Number of time steps.

    Returns
    -------
    float
        Option price.
    """
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    # Build stock price tree
    ST = np.zeros((N + 1, N + 1))
    for i in range(N + 1):
        for j in range(i + 1):
            ST[j, i] = S * (u ** j) * (d ** (i - j))

    # Terminal payoffs with barrier enforcement
    C = np.maximum(ST[:, N] - K, 0)
    C[ST[:, N] <= H] = 0  # Knocked out

    # Backward induction with barrier
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            if ST[j, i] > H:
                C[j] = np.exp(-r * dt) * (p * C[j + 1] + (1 - p) * C[j])
            else:
                C[j] = 0  # Knocked out

    return C[0]


# =============================================================================
# 2. Vanilla Call Binomial (for comparison)
# =============================================================================

def vanilla_call_binomial(S, K, T, r, sigma, N):
    """Price a European call using a CRR binomial tree (no barrier)."""
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    ST = np.zeros((N + 1, N + 1))
    for i in range(N + 1):
        for j in range(i + 1):
            ST[j, i] = S * (u ** j) * (d ** (i - j))

    C = np.maximum(ST[:, N] - K, 0)

    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            C[j] = np.exp(-r * dt) * (p * C[j + 1] + (1 - p) * C[j])

    return C[0]


# =============================================================================
# 3. Main: Price and Convergence Analysis
# =============================================================================

if __name__ == "__main__":
    # Parameters
    S = 100       # Current stock price
    K = 100       # Strike price
    H = 90        # Down-and-out barrier
    T = 1         # Time to maturity
    r = 0.05      # Risk-free rate
    sigma = 0.2   # Volatility

    # --- Single Price ---
    N = 500
    barrier_price = barrier_call_binomial(S, K, H, T, r, sigma, N)
    vanilla_price = vanilla_call_binomial(S, K, T, r, sigma, N)

    print("=" * 60)
    print("DOWN-AND-OUT BARRIER CALL PRICING (Binomial Tree)")
    print("=" * 60)
    print(f"Parameters: S={S}, K={K}, H={H}, T={T}, r={r}, σ={sigma}")
    print(f"Number of steps: N={N}")
    print(f"\nVanilla Call Price:           {vanilla_price:.4f}")
    print(f"Down-and-Out Barrier Call:    {barrier_price:.4f}")
    print(f"Barrier Discount:            {vanilla_price - barrier_price:.4f}")
    print(f"Barrier/Vanilla Ratio:       {barrier_price/vanilla_price:.4f}")

    # --- Convergence Analysis ---
    N_values = list(range(50, 501, 10))
    barrier_prices = []
    vanilla_prices = []

    for n in N_values:
        barrier_prices.append(barrier_call_binomial(S, K, H, T, r, sigma, n))
        vanilla_prices.append(vanilla_call_binomial(S, K, T, r, sigma, n))

    # Plot convergence
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Panel 1: Convergence of barrier and vanilla prices
    axes[0].plot(N_values, barrier_prices, 'b-', alpha=0.7, label='Barrier Call')
    axes[0].plot(N_values, vanilla_prices, 'r-', alpha=0.7, label='Vanilla Call')
    axes[0].set_xlabel('Number of Steps (N)')
    axes[0].set_ylabel('Option Price')
    axes[0].set_title('Convergence: Barrier vs Vanilla Call')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Panel 2: Oscillation detail for barrier option
    axes[1].plot(N_values, barrier_prices, 'b-o', markersize=2, alpha=0.7)
    axes[1].axhline(y=barrier_prices[-1], color='k', linestyle='--', alpha=0.5,
                    label=f'N={N_values[-1]}: {barrier_prices[-1]:.4f}')
    axes[1].set_xlabel('Number of Steps (N)')
    axes[1].set_ylabel('Barrier Call Price')
    axes[1].set_title('Barrier Call Convergence (Oscillation Detail)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('barrier_call_binomial_convergence.png', dpi=150, bbox_inches='tight')
    plt.show()

    # --- Sensitivity to Barrier Level ---
    H_values = np.arange(70, 100, 2)
    prices_by_barrier = [barrier_call_binomial(S, K, h, T, r, sigma, 300) for h in H_values]

    plt.figure(figsize=(8, 5))
    plt.plot(H_values, prices_by_barrier, 'b-o', markersize=4)
    plt.axhline(y=vanilla_price, color='r', linestyle='--', label='Vanilla Call')
    plt.xlabel('Barrier Level (H)')
    plt.ylabel('Barrier Call Price')
    plt.title('Down-and-Out Call Price vs Barrier Level')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('barrier_call_sensitivity.png', dpi=150, bbox_inches='tight')
    plt.show()

    print("\n--- Barrier Sensitivity ---")
    print(f"{'Barrier H':>10} {'Price':>10} {'% of Vanilla':>14}")
    print("-" * 36)
    for h, p in zip(H_values[::3], prices_by_barrier[::3]):
        print(f"{h:10.0f} {p:10.4f} {p/vanilla_price*100:13.1f}%")
