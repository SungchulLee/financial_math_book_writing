"""
Least-Squares Monte Carlo (LSM) for American Put Options
=========================================================

Implements the Longstaff-Schwartz (2001) algorithm for pricing
American put options via regression-based estimation of the
continuation value.

Includes:
  - LSM pricing with polynomial basis functions
  - Comparison with binomial tree benchmark
  - Convergence analysis (paths, time steps, basis degree)
  - Exercise region visualization
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


# ============================================================
# Core Functions
# ============================================================

def lsm_american_put(S0, K, T, r, sigma, M=50000, N=50, poly_degree=3,
                     seed=None):
    """
    Price an American put via Least-Squares Monte Carlo (LSM).

    Parameters
    ----------
    S0 : float — Initial stock price
    K : float — Strike price
    T : float — Maturity
    r : float — Risk-free rate
    sigma : float — Volatility
    M : int — Number of simulated paths
    N : int — Number of exercise dates
    poly_degree : int — Degree of polynomial basis
    seed : int or None — Random seed

    Returns
    -------
    price : float — Estimated American put price
    std_err : float — Standard error of the estimate
    exercise_info : dict — Exercise statistics
    """
    if seed is not None:
        np.random.seed(seed)

    dt = T / N

    # Simulate paths
    Z = np.random.randn(M, N)
    S = np.zeros((M, N + 1))
    S[:, 0] = S0
    for k in range(N):
        S[:, k + 1] = S[:, k] * np.exp(
            (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[:, k]
        )

    # Initialize cash flows at maturity
    payoff_mat = np.maximum(K - S[:, N], 0)
    cashflow = payoff_mat.copy()
    exercise_time = np.full(M, N)

    # Track exercise decisions for analysis
    exercise_counts = np.zeros(N + 1)
    exercise_counts[N] = np.sum(payoff_mat > 0)

    # Backward induction
    for k in range(N - 1, 0, -1):
        itm = np.where(K - S[:, k] > 0)[0]

        if len(itm) < poly_degree + 1:
            continue

        # Discounted future cash flows
        discount_steps = exercise_time[itm] - k
        Y = cashflow[itm] * np.exp(-r * dt * discount_steps)

        # Polynomial basis
        X = S[itm, k]
        A = np.column_stack([X**p for p in range(poly_degree + 1)])

        # Least-squares regression
        beta = np.linalg.lstsq(A, Y, rcond=None)[0]
        continuation = A @ beta

        # Exercise decision
        exercise_value = K - S[itm, k]
        exercise_mask = exercise_value >= continuation

        exercise_idx = itm[exercise_mask]
        cashflow[exercise_idx] = exercise_value[exercise_mask]
        exercise_time[exercise_idx] = k
        exercise_counts[k] = np.sum(exercise_mask)

    # Discount all cash flows to time 0
    discounted = cashflow * np.exp(-r * dt * exercise_time)
    price = np.mean(discounted)
    std_err = np.std(discounted) / np.sqrt(M)

    exercise_info = {
        "exercise_counts": exercise_counts,
        "exercise_time": exercise_time,
        "mean_exercise_time": np.mean(exercise_time[cashflow > 0]) * dt,
    }

    return price, std_err, exercise_info


def american_put_binomial(S, K, T, r, sigma, N):
    """CRR binomial tree benchmark."""
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    q = (np.exp(r * dt) - d) / (u - d)
    ST = np.array([S * (u ** j) * (d ** (N - j)) for j in range(N + 1)])
    P = np.maximum(K - ST, 0)
    for i in range(N - 1, -1, -1):
        P = np.exp(-r * dt) * (q * P[1:i + 2] + (1 - q) * P[0:i + 1])
        ST = np.array([S * (u ** j) * (d ** (i - j)) for j in range(i + 1)])
        P = np.maximum(K - ST, P)
    return P[0]


def european_put_bs(S, K, T, r, sigma):
    """Black-Scholes European put."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


# ============================================================
# Parameters
# ============================================================

S0 = 100
K = 100
T = 1.0
r = 0.05
sigma = 0.20


# ============================================================
# 1. Basic LSM Pricing
# ============================================================

print("=" * 60)
print("Least-Squares Monte Carlo: American Put Pricing")
print("=" * 60)
print(f"Parameters: S={S0}, K={K}, T={T}, r={r}, σ={sigma}\n")

price_lsm, se_lsm, info = lsm_american_put(S0, K, T, r, sigma,
                                             M=100000, N=50, seed=42)
price_bin = american_put_binomial(S0, K, T, r, sigma, 1000)
price_eu = european_put_bs(S0, K, T, r, sigma)

print(f"European Put (Black-Scholes):     {price_eu:.4f}")
print(f"American Put (Binomial, N=1000):  {price_bin:.4f}")
print(f"American Put (LSM, M=100000):     {price_lsm:.4f} ± {se_lsm:.4f}")
print(f"95% CI: [{price_lsm - 1.96*se_lsm:.4f}, {price_lsm + 1.96*se_lsm:.4f}]")
print(f"\nMean exercise time (exercised paths): {info['mean_exercise_time']:.3f} years")


# ============================================================
# 2. Convergence in Number of Paths
# ============================================================

print("\n" + "=" * 60)
print("Convergence Analysis: Number of Paths")
print("=" * 60)

path_counts = [1000, 5000, 10000, 50000, 100000, 200000]
prices_paths = []
errors_paths = []

print(f"\n{'M':>8} | {'Price':>8} | {'Std Err':>8} | {'vs Binomial':>12}")
print("-" * 45)

for M in path_counts:
    p, se, _ = lsm_american_put(S0, K, T, r, sigma, M=M, N=50, seed=42)
    prices_paths.append(p)
    errors_paths.append(se)
    diff = p - price_bin
    print(f"{M:>8} | {p:>8.4f} | {se:>8.4f} | {diff:>+12.4f}")


# ============================================================
# 3. Effect of Basis Degree
# ============================================================

print("\n" + "=" * 60)
print("Effect of Polynomial Basis Degree")
print("=" * 60)

degrees = [1, 2, 3, 4, 5, 6]
prices_deg = []

print(f"\n{'Degree':>8} | {'Price':>8} | {'Std Err':>8}")
print("-" * 30)

for deg in degrees:
    p, se, _ = lsm_american_put(S0, K, T, r, sigma, M=100000, N=50,
                                 poly_degree=deg, seed=42)
    prices_deg.append(p)
    print(f"{deg:>8} | {p:>8.4f} | {se:>8.4f}")


# ============================================================
# 4. Visualization
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# (a) Convergence in paths
axes[0, 0].errorbar(path_counts, prices_paths,
                     yerr=[1.96 * e for e in errors_paths],
                     fmt="o-", color="steelblue", capsize=3,
                     label="LSM estimate ± 95% CI")
axes[0, 0].axhline(price_bin, color="coral", linestyle="--", linewidth=1,
                    label=f"Binomial = {price_bin:.4f}")
axes[0, 0].set_xscale("log")
axes[0, 0].set_xlabel("Number of Paths (M)")
axes[0, 0].set_ylabel("American Put Price")
axes[0, 0].set_title("(a) LSM Convergence in Paths")
axes[0, 0].legend(fontsize=9)
axes[0, 0].grid(True, alpha=0.3)

# (b) Effect of basis degree
axes[0, 1].bar(degrees, prices_deg, color="steelblue", alpha=0.7)
axes[0, 1].axhline(price_bin, color="coral", linestyle="--", linewidth=1,
                    label=f"Binomial = {price_bin:.4f}")
axes[0, 1].set_xlabel("Polynomial Degree")
axes[0, 1].set_ylabel("American Put Price")
axes[0, 1].set_title("(b) Effect of Basis Degree")
axes[0, 1].legend(fontsize=9)
axes[0, 1].grid(True, alpha=0.3, axis="y")

# (c) Exercise time distribution
_, _, info_detail = lsm_american_put(S0, K, T, r, sigma, M=100000, N=50, seed=42)
ex_times = info_detail["exercise_time"]
ex_times_years = ex_times[ex_times < 50] * (T / 50)  # exclude maturity
axes[1, 0].hist(ex_times_years, bins=30, color="steelblue", alpha=0.7,
                edgecolor="white")
axes[1, 0].set_xlabel("Exercise Time (years)")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].set_title("(c) Distribution of Early Exercise Times")
axes[1, 0].grid(True, alpha=0.3)

# (d) Standard error vs 1/sqrt(M)
inv_sqrt_M = [1 / np.sqrt(m) for m in path_counts]
axes[1, 1].plot(inv_sqrt_M, errors_paths, "o-", color="steelblue")
axes[1, 1].set_xlabel(r"$1/\sqrt{M}$")
axes[1, 1].set_ylabel("Standard Error")
axes[1, 1].set_title(r"(d) Standard Error vs $1/\sqrt{M}$")
axes[1, 1].grid(True, alpha=0.3)

plt.suptitle("LSM Monte Carlo Analysis for American Put",
             fontsize=14, fontweight="bold", y=1.01)
plt.tight_layout()
plt.savefig("lsm_american_put_analysis.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nFigure saved: lsm_american_put_analysis.png")


# ============================================================
# 5. Comparison Table
# ============================================================

print("\n" + "=" * 60)
print("Method Comparison Summary")
print("=" * 60)

methods = [
    ("European (BS formula)", price_eu),
    ("Binomial (N=1000)", price_bin),
    ("LSM (M=100k, deg=3)", price_lsm),
]

print(f"\n{'Method':<30} | {'Price':>8} | {'vs Binomial':>12}")
print("-" * 55)
for name, p in methods:
    diff = p - price_bin
    print(f"{name:<30} | {p:>8.4f} | {diff:>+12.4f}")
