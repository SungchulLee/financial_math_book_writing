# Early Exercise Boundary

## Background

Early-Exercise Boundary for American Put Options
=================================================

Visualizes the optimal early-exercise boundary S*(t) by building
a full binomial tree and identifying nodes where immediate exercise
dominates the continuation value.

Includes:

  - Full-tree computation of the exercise boundary
  - Boundary visualization for varying parameters (r, sigma, K)
  - Boundary behavior near maturity
  - Comparison across different interest rates and volatilities

---

## Code

```python
"""
Early-Exercise Boundary for American Put Options
=================================================

Visualizes the optimal early-exercise boundary S*(t) by building
a full binomial tree and identifying nodes where immediate exercise
dominates the continuation value.

Includes:
  - Full-tree computation of the exercise boundary
  - Boundary visualization for varying parameters (r, sigma, K)
  - Boundary behavior near maturity
  - Comparison across different interest rates and volatilities
"""

import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# Core Function: Exercise Boundary from Binomial Tree
# ============================================================

def compute_exercise_boundary(S, K, T, r, sigma, N):
    """
    Build a full binomial tree and identify the early-exercise boundary.

    At each time step, finds the highest stock price at which exercise
    is optimal (for a put), giving S*(t).

    Parameters
    ----------
    S : float — Current stock price
    K : float — Strike price
    T : float — Time to maturity
    r : float — Risk-free rate
    sigma : float — Volatility
    N : int — Number of time steps

    Returns
    -------
    times : array — Time points
    boundary : array — Exercise boundary S*(t) at each time
    exercise_points : list of (time, stock_price) — All exercise nodes
    """
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    q = (np.exp(r * dt) - d) / (u - d)

    # Build full tree
    tree_S = np.zeros((N + 1, N + 1))
    tree_V = np.zeros((N + 1, N + 1))

    for n in range(N + 1):
        for j in range(n + 1):
            tree_S[j, n] = S * (u ** j) * (d ** (n - j))

    # Terminal payoff
    tree_V[:, N] = np.maximum(K - tree_S[:, N], 0)

    # Collect all exercise points and per-step boundary
    exercise_points = []
    boundary = np.full(N + 1, np.nan)
    boundary[N] = K  # At maturity, exercise when S < K

    # Backward induction
    for n in range(N - 1, -1, -1):
        max_exercise_S = 0.0
        for j in range(n + 1):
            continuation = np.exp(-r * dt) * (
                q * tree_V[j + 1, n + 1] + (1 - q) * tree_V[j, n + 1]
            )
            exercise = K - tree_S[j, n]
            tree_V[j, n] = max(continuation, exercise)

            if exercise > continuation and exercise > 0:
                exercise_points.append((n * dt, tree_S[j, n]))
                max_exercise_S = max(max_exercise_S, tree_S[j, n])

        if max_exercise_S > 0:
            boundary[n] = max_exercise_S

    times = np.array([n * dt for n in range(N + 1)])
    return times, boundary, exercise_points


# ============================================================
# Parameters
# ============================================================


if __name__ == "__main__":
    S = 100
    K = 100
    T = 1.0
    r = 0.05
    sigma = 0.20
    N = 200


    # ============================================================
    # 1. Basic Boundary Visualization
    # ============================================================

    print("=" * 60)
    print("Early-Exercise Boundary for American Put")
    print("=" * 60)
    print(f"Parameters: S={S}, K={K}, T={T}, r={r}, σ={sigma}, N={N}\n")

    times, boundary, exercise_pts = compute_exercise_boundary(S, K, T, r, sigma, N)
    pts = np.array(exercise_pts)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # (a) Scatter of all exercise nodes
    axes[0].scatter(pts[:, 0], pts[:, 1], s=2, alpha=0.4, color="steelblue")
    axes[0].axhline(K, color="gray", linestyle="--", linewidth=0.8, label=f"K = {K}")
    axes[0].set_xlabel("Time (years)")
    axes[0].set_ylabel("Stock Price")
    axes[0].set_title("Exercise Nodes in Binomial Tree")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # (b) Exercise boundary S*(t)
    valid = ~np.isnan(boundary)
    axes[1].plot(times[valid], boundary[valid], "-", color="coral", linewidth=2)
    axes[1].axhline(K, color="gray", linestyle="--", linewidth=0.8, label=f"K = {K}")
    axes[1].set_xlabel("Time (years)")
    axes[1].set_ylabel("Exercise Boundary S*(t)")
    axes[1].set_title("Optimal Exercise Boundary (American Put)")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("early_exercise_boundary_basic.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Figure saved: early_exercise_boundary_basic.png")


    # ============================================================
    # 2. Effect of Interest Rate on Boundary
    # ============================================================

    print("\n" + "=" * 60)
    print("Effect of Interest Rate on Exercise Boundary")
    print("=" * 60)

    rates = [0.02, 0.05, 0.10, 0.15]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

    fig, ax = plt.subplots(figsize=(10, 6))
    for rate, color in zip(rates, colors):
        t, bd, _ = compute_exercise_boundary(S, K, T, rate, sigma, N)
        valid = ~np.isnan(bd)
        ax.plot(t[valid], bd[valid], "-", color=color, linewidth=2, label=f"r = {rate}")

    ax.axhline(K, color="gray", linestyle="--", linewidth=0.8, label=f"K = {K}")
    ax.set_xlabel("Time (years)")
    ax.set_ylabel("Exercise Boundary S*(t)")
    ax.set_title("Exercise Boundary: Effect of Interest Rate")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("early_exercise_boundary_rates.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Figure saved: early_exercise_boundary_rates.png")

    for rate in rates:
        _, bd, _ = compute_exercise_boundary(S, K, T, rate, sigma, N)
        bd_start = bd[~np.isnan(bd)][0] if any(~np.isnan(bd)) else np.nan
        print(f"  r = {rate:.2f}: S*(0) ≈ {bd_start:.2f}")


    # ============================================================
    # 3. Effect of Volatility on Boundary
    # ============================================================

    print("\n" + "=" * 60)
    print("Effect of Volatility on Exercise Boundary")
    print("=" * 60)

    vols = [0.10, 0.20, 0.30, 0.40]

    fig, ax = plt.subplots(figsize=(10, 6))
    for vol, color in zip(vols, colors):
        t, bd, _ = compute_exercise_boundary(S, K, T, r, vol, N)
        valid = ~np.isnan(bd)
        ax.plot(t[valid], bd[valid], "-", color=color, linewidth=2, label=f"σ = {vol}")

    ax.axhline(K, color="gray", linestyle="--", linewidth=0.8, label=f"K = {K}")
    ax.set_xlabel("Time (years)")
    ax.set_ylabel("Exercise Boundary S*(t)")
    ax.set_title("Exercise Boundary: Effect of Volatility")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("early_exercise_boundary_vols.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Figure saved: early_exercise_boundary_vols.png")

    for vol in vols:
        _, bd, _ = compute_exercise_boundary(S, K, T, r, vol, N)
        bd_start = bd[~np.isnan(bd)][0] if any(~np.isnan(bd)) else np.nan
        print(f"  σ = {vol:.2f}: S*(0) ≈ {bd_start:.2f}")


    # ============================================================
    # 4. Exercise Boundary for Different Strikes
    # ============================================================

    print("\n" + "=" * 60)
    print("Exercise Boundary for Different Strikes")
    print("=" * 60)

    strikes = [80, 100, 120]

    fig, ax = plt.subplots(figsize=(10, 6))
    for strike, color in zip(strikes, colors):
        t, bd, _ = compute_exercise_boundary(S, strike, T, r, sigma, N)
        valid = ~np.isnan(bd)
        ax.plot(t[valid], bd[valid], "-", color=color, linewidth=2, label=f"K = {strike}")
        ax.axhline(strike, color=color, linestyle=":", linewidth=0.5)

    ax.set_xlabel("Time (years)")
    ax.set_ylabel("Exercise Boundary S*(t)")
    ax.set_title("Exercise Boundary for Different Strikes")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("early_exercise_boundary_strikes.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Figure saved: early_exercise_boundary_strikes.png")


    # ============================================================
    # 5. Comprehensive Summary Figure
    # ============================================================

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # (a) Basic boundary with exercise nodes
    axes[0, 0].scatter(pts[:, 0], pts[:, 1], s=1, alpha=0.3, color="steelblue")
    valid = ~np.isnan(boundary)
    axes[0, 0].plot(times[valid], boundary[valid], "-", color="coral", linewidth=2,
                    label="S*(t)")
    axes[0, 0].axhline(K, color="gray", linestyle="--", linewidth=0.8)
    axes[0, 0].set_title("(a) Exercise Boundary and Nodes")
    axes[0, 0].set_xlabel("Time")
    axes[0, 0].set_ylabel("Stock Price")
    axes[0, 0].legend()
    axes[0, 0].grid(True, alpha=0.3)

    # (b) Varying r
    for rate, color in zip(rates, colors):
        t, bd, _ = compute_exercise_boundary(S, K, T, rate, sigma, N)
        valid = ~np.isnan(bd)
        axes[0, 1].plot(t[valid], bd[valid], "-", color=color, linewidth=1.5,
                        label=f"r={rate}")
    axes[0, 1].axhline(K, color="gray", linestyle="--", linewidth=0.8)
    axes[0, 1].set_title("(b) Effect of Interest Rate")
    axes[0, 1].set_xlabel("Time")
    axes[0, 1].set_ylabel("S*(t)")
    axes[0, 1].legend(fontsize=8)
    axes[0, 1].grid(True, alpha=0.3)

    # (c) Varying sigma
    for vol, color in zip(vols, colors):
        t, bd, _ = compute_exercise_boundary(S, K, T, r, vol, N)
        valid = ~np.isnan(bd)
        axes[1, 0].plot(t[valid], bd[valid], "-", color=color, linewidth=1.5,
                        label=f"σ={vol}")
    axes[1, 0].axhline(K, color="gray", linestyle="--", linewidth=0.8)
    axes[1, 0].set_title("(c) Effect of Volatility")
    axes[1, 0].set_xlabel("Time")
    axes[1, 0].set_ylabel("S*(t)")
    axes[1, 0].legend(fontsize=8)
    axes[1, 0].grid(True, alpha=0.3)

    # (d) Varying K
    for strike, color in zip(strikes, colors):
        t, bd, _ = compute_exercise_boundary(S, strike, T, r, sigma, N)
        valid = ~np.isnan(bd)
        axes[1, 1].plot(t[valid], bd[valid], "-", color=color, linewidth=1.5,
                        label=f"K={strike}")
    axes[1, 1].set_title("(d) Effect of Strike Price")
    axes[1, 1].set_xlabel("Time")
    axes[1, 1].set_ylabel("S*(t)")
    axes[1, 1].legend(fontsize=8)
    axes[1, 1].grid(True, alpha=0.3)

    plt.suptitle("Early-Exercise Boundary Analysis for American Put Options",
                 fontsize=14, fontweight="bold", y=1.01)
    plt.tight_layout()
    plt.savefig("early_exercise_boundary_comprehensive.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("\nFigure saved: early_exercise_boundary_comprehensive.png")
```

## Exercises

**Exercise 1.**
Define the early-exercise boundary $S^*(t)$ for an American put. How does it behave as $t \to T$?

??? success "Solution to Exercise 1"
    The early-exercise boundary $S^*(t)$ is the critical stock price below which immediate exercise is optimal at time $t$. For $S_t < S^*(t)$, the holder should exercise; for $S_t > S^*(t)$, the holder should continue.

    As $t \to T$: $S^*(T) = K$ (at expiration, exercise when ITM). For $t < T$: $S^*(t) < K$ because the time value of the option provides some incentive to wait.

    As $t \to 0$ (far from expiry): $S^*(0)$ approaches a finite limit that depends on $r$, $\sigma$, and $K$. For large $r$, $S^*(0)$ is closer to $K$ because the interest benefit of early exercise is stronger.

---

**Exercise 2.**
How does increasing the risk-free rate $r$ affect the early-exercise boundary? Explain intuitively.

??? success "Solution to Exercise 2"
    Increasing $r$ raises the early-exercise boundary $S^*(t)$ (makes early exercise more likely at higher stock prices). Intuitively: exercising an American put yields $K$ immediately, which can be invested at rate $r$. Higher $r$ makes the interest earned on $K$ more attractive relative to the option's time value, so the holder exercises sooner (at a higher $S$).

    In the limit $r \to \infty$, $S^*(t) \to K$ for all $t$: exercise immediately whenever ITM.

---

**Exercise 3.**
The code builds a full binomial tree to identify exercise nodes. What is the computational cost, and why is the full tree needed (unlike pricing)?

??? success "Solution to Exercise 3"
    The full tree requires $O(M^2)$ computation and $O(M^2)$ memory (storing values at all $M(M+1)/2$ nodes). This is more expensive than the $O(M)$-space pricing algorithm.

    The full tree is needed because the exercise boundary $S^*(t_n)$ is the lowest stock price at time step $n$ where the holder exercises. To find this, we need to know the exercise decision at every node, which requires storing the option value at every node for comparison with the intrinsic value.

---

**Exercise 4.**
Compare the exercise boundary for different volatilities. Does higher volatility make early exercise more or less likely?

??? success "Solution to Exercise 4"
    Higher volatility $\sigma$ lowers the early-exercise boundary $S^*(t)$ (makes early exercise less likely). This is because:

    1. Higher $\sigma$ increases the option's time value (more potential for favorable moves).
    2. The value of waiting increases with uncertainty.
    3. The insurance value of the put (protection against further drops) is greater when $\sigma$ is large.

    In the limit $\sigma \to \infty$, the American put behaves like the European put (never exercise early) because the time value dominates.
