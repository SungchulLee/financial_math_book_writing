# American Put (Binomial Tree)

## Background

American Put Option Pricing via Binomial Tree (CRR Model)
=========================================================

Prices an American put option using the Cox–Ross–Rubinstein binomial tree.
At each node, the algorithm compares the continuation value (discounted
risk-neutral expectation) against the immediate exercise value, selecting
the maximum. This maximum condition is the key extension beyond European
pricing.

Includes:

  - Array-based binomial pricing (efficient O(N) space)
  - Convergence analysis across step counts
  - Comparison with European put (Black-Scholes formula)
  - Richardson extrapolation for accelerated convergence

---

## Code

```python
"""
American Put Option Pricing via Binomial Tree (CRR Model)
=========================================================

Prices an American put option using the Cox–Ross–Rubinstein binomial tree.
At each node, the algorithm compares the continuation value (discounted
risk-neutral expectation) against the immediate exercise value, selecting
the maximum. This maximum condition is the key extension beyond European
pricing.

Includes:
  - Array-based binomial pricing (efficient O(N) space)
  - Convergence analysis across step counts
  - Comparison with European put (Black-Scholes formula)
  - Richardson extrapolation for accelerated convergence
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


# ============================================================
# Core Pricing Functions
# ============================================================

def american_put_binomial(S, K, T, r, sigma, N):
    """
    Price an American put option using the CRR binomial tree.

    Parameters
    ----------
    S : float — Current stock price
    K : float — Strike price
    T : float — Time to maturity (years)
    r : float — Risk-free rate (continuous compounding)
    sigma : float — Volatility (annualized)
    N : int — Number of time steps

    Returns
    -------
    float — American put option price
    """
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    q = (np.exp(r * dt) - d) / (u - d)

    # Terminal stock prices: S * u^j * d^(N-j) for j = 0, ..., N
    ST = np.array([S * (u ** j) * (d ** (N - j)) for j in range(N + 1)])

    # Terminal payoff
    P = np.maximum(K - ST, 0)

    # Backward induction with early-exercise check
    for i in range(N - 1, -1, -1):
        # Continuation value
        P = np.exp(-r * dt) * (q * P[1:i + 2] + (1 - q) * P[0:i + 1])

        # Stock prices at step i
        ST = np.array([S * (u ** j) * (d ** (i - j)) for j in range(i + 1)])

        # Early exercise check: max(payoff, continuation)
        P = np.maximum(K - ST, P)

    return P[0]


def european_put_bs(S, K, T, r, sigma):
    """Black-Scholes European put price."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


def european_put_binomial(S, K, T, r, sigma, N):
    """Price a European put using the CRR binomial tree (no early exercise)."""
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    q = (np.exp(r * dt) - d) / (u - d)

    ST = np.array([S * (u ** j) * (d ** (N - j)) for j in range(N + 1)])
    P = np.maximum(K - ST, 0)

    for i in range(N - 1, -1, -1):
        P = np.exp(-r * dt) * (q * P[1:i + 2] + (1 - q) * P[0:i + 1])

    return P[0]


# ============================================================
# Parameters
# ============================================================


if __name__ == "__main__":
    S = 100       # Current stock price
    K = 100       # Strike price
    T = 1.0       # Time to maturity (1 year)
    r = 0.05      # Risk-free rate
    sigma = 0.20  # Volatility


    # ============================================================
    # 1. Basic Pricing
    # ============================================================

    print("=" * 60)
    print("American Put Option Pricing via Binomial Tree")
    print("=" * 60)
    print(f"\nParameters: S={S}, K={K}, T={T}, r={r}, σ={sigma}\n")

    N_basic = 500
    price_am = american_put_binomial(S, K, T, r, sigma, N_basic)
    price_eu = european_put_bs(S, K, T, r, sigma)

    print(f"European Put (Black-Scholes):     {price_eu:.4f}")
    print(f"American Put (Binomial, N={N_basic}):  {price_am:.4f}")
    print(f"Early Exercise Premium:           {price_am - price_eu:.4f}")


    # ============================================================
    # 2. Convergence Analysis
    # ============================================================

    print("\n" + "=" * 60)
    print("Convergence Analysis")
    print("=" * 60)

    steps = [10, 20, 50, 100, 200, 500, 1000, 2000]
    prices_am = []
    prices_eu_bin = []

    print(f"\n{'N':>6} | {'American':>12} | {'European(Bin)':>14} | {'EEP':>8} | {'EU Error':>10}")
    print("-" * 60)

    for N in steps:
        p_am = american_put_binomial(S, K, T, r, sigma, N)
        p_eu = european_put_binomial(S, K, T, r, sigma, N)
        prices_am.append(p_am)
        prices_eu_bin.append(p_eu)
        eep = p_am - price_eu
        eu_err = p_eu - price_eu
        print(f"{N:>6} | {p_am:>12.4f} | {p_eu:>14.4f} | {eep:>8.4f} | {eu_err:>+10.4f}")


    # ============================================================
    # 3. Richardson Extrapolation
    # ============================================================

    print("\n" + "=" * 60)
    print("Richardson Extrapolation")
    print("=" * 60)

    pairs = [(100, 200), (200, 400), (500, 1000)]
    for N1, N2 in pairs:
        p1 = american_put_binomial(S, K, T, r, sigma, N1)
        p2 = american_put_binomial(S, K, T, r, sigma, N2)
        p_rich = 2 * p2 - p1
        print(f"  N={N1},{N2}: V(N1)={p1:.4f}, V(N2)={p2:.4f}, "
              f"Richardson={p_rich:.4f}")


    # ============================================================
    # 4. Visualization: Convergence Plot
    # ============================================================

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # (a) Price vs Steps
    axes[0].plot(steps, prices_am, "o-", color="steelblue", label="American Put (Binomial)")
    axes[0].axhline(price_eu, color="gray", linestyle="--", linewidth=0.8,
                    label=f"European Put (BS) = {price_eu:.4f}")
    axes[0].set_xlabel("Number of Steps (N)")
    axes[0].set_ylabel("Option Price")
    axes[0].set_title("Convergence of American Put Price")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # (b) Early Exercise Premium vs Steps
    eep_values = [p - price_eu for p in prices_am]
    axes[1].plot(steps, eep_values, "s-", color="coral", label="Early Exercise Premium")
    axes[1].set_xlabel("Number of Steps (N)")
    axes[1].set_ylabel("EEP = American − European")
    axes[1].set_title("Early Exercise Premium vs Steps")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("american_put_binomial_convergence.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("\nFigure saved: american_put_binomial_convergence.png")


    # ============================================================
    # 5. Sensitivity Analysis: Vary Spot Price
    # ============================================================

    print("\n" + "=" * 60)
    print("American vs European Put: Varying Spot Price")
    print("=" * 60)

    N_sens = 500
    spots = np.linspace(60, 140, 50)
    am_prices = [american_put_binomial(s, K, T, r, sigma, N_sens) for s in spots]
    eu_prices = [european_put_bs(s, K, T, r, sigma) for s in spots]
    intrinsic = np.maximum(K - spots, 0)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # (a) Option values
    axes[0].plot(spots, am_prices, "-", color="steelblue", linewidth=2, label="American Put")
    axes[0].plot(spots, eu_prices, "--", color="coral", linewidth=2, label="European Put")
    axes[0].plot(spots, intrinsic, ":", color="gray", linewidth=1, label="Intrinsic Value")
    axes[0].set_xlabel("Stock Price")
    axes[0].set_ylabel("Option Price")
    axes[0].set_title("American vs European Put Values")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # (b) Early exercise premium
    eep_curve = [a - e for a, e in zip(am_prices, eu_prices)]
    axes[1].plot(spots, eep_curve, "-", color="coral", linewidth=2)
    axes[1].set_xlabel("Stock Price")
    axes[1].set_ylabel("Early Exercise Premium")
    axes[1].set_title("Early Exercise Premium vs Spot Price")
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("american_put_binomial_sensitivity.png", dpi=150, bbox_inches="tight")
    plt.show()
    print("Figure saved: american_put_binomial_sensitivity.png")
```

## Exercises

**Exercise 1.**
Explain the early exercise condition for an American put at a binomial tree node. Why might early exercise be optimal for puts but not for calls (on non-dividend stocks)?

??? success "Solution to Exercise 1"
    At each node, the holder compares: **exercise value** $\max(K - S, 0)$ versus **continuation value** $e^{-r\Delta t}[q V_u + (1-q)V_d]$. Early exercise is optimal when the exercise value exceeds the continuation value.

    For puts: when $S$ is very low, the exercise value $K - S$ is large and the stock cannot go below 0, so the upside of waiting is limited. Meanwhile, continuing means receiving $K - S$ later, which is worth less due to discounting. The interest earned on $K$ (received upon exercise) can exceed the option's time value.

    For calls on non-dividend stocks: $S - K$ increases as $S$ rises, and there is no upper bound. Waiting always preserves optionality and avoids paying $K$ early (which loses interest). Therefore early exercise is never optimal.

---

**Exercise 2.**
With $S_0 = 100$, $K = 100$, $T = 1$, $r = 0.05$, $\sigma = 0.20$, compute the CRR parameters $u$, $d$, and $q$ for $M = 4$ steps.

??? success "Solution to Exercise 2"
    $\Delta t = 1/4 = 0.25$.

    $$
    u = e^{\sigma\sqrt{\Delta t}} = e^{0.20\sqrt{0.25}} = e^{0.10} \approx 1.10517
    $$

    $$
    d = 1/u \approx 0.90484
    $$

    $$
    q = \frac{e^{r\Delta t} - d}{u - d} = \frac{e^{0.0125} - 0.90484}{1.10517 - 0.90484} = \frac{1.01258 - 0.90484}{0.20033} = \frac{0.10774}{0.20033} \approx 0.5379
    $$

---

**Exercise 3.**
The code uses an $O(N)$-space array-based method instead of storing the full tree. Describe this optimization and its memory savings for $M = 1000$ steps.

??? success "Solution to Exercise 3"
    Instead of a 2D array of size $M \times (M+1)$ storing all node values, only a 1D array of size $M+1$ is maintained. At each backward step, values are updated in-place from left to right.

    Memory for full tree: $1000 \times 1001 \times 8 \approx 8$ MB. Memory for array method: $1001 \times 8 \approx 8$ KB. The savings factor is approximately 1000x.

    The trade-off is that intermediate node values (needed for Greeks or exercise boundary computation) are lost. For just the option price at $t = 0$, the array method is sufficient.

---

**Exercise 4.**
Richardson extrapolation combines prices from $M$ and $M+1$ steps. Explain why this accelerates convergence from $O(1/M)$ to $O(1/M^2)$.

??? success "Solution to Exercise 4"
    The binomial price has an asymptotic expansion $V_M = V_{\text{exact}} + c_1/M + c_2/M^2 + \ldots$ where the $O(1/M)$ term oscillates between even and odd $M$.

    The Richardson extrapolation $V_R = 2V_{2M} - V_M$ eliminates the $O(1/M)$ term because the leading error has opposite signs for $M$ and $2M$. More precisely: $V_R = V_{\text{exact}} + O(1/M^2)$.

    For the simpler "average of consecutive" approach: $\bar{V} = (V_M + V_{M+1})/2$ also reduces the oscillation, giving approximately $O(1/M^2)$ convergence. This is simpler and nearly as effective.
