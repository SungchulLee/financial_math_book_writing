# Binomial Model for American Options

## Introduction

The **binomial tree** is the most natural numerical framework for American option pricing. Its node-by-node structure allows the early-exercise decision to be evaluated at every point in the tree via **backward induction with a maximum condition**.

This section develops the full binomial pricing algorithm for American options, demonstrates convergence, and shows how the method naturally identifies the early-exercise boundary.

!!! info "Prerequisites"
    - [Multi-Period Binomial Model](../binomial_model/multi_period_binomial_model.md) (backward induction)
    - [Risk-Neutral Measure](../binomial_model/risk_neutral_measure.md) (binomial risk-neutral pricing)
    - [Early Exercise](early_exercise.md) (when exercise is optimal)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Implement backward induction with early-exercise checks
    2. Compare American and European option values on the same tree
    3. Identify the early-exercise boundary from the tree
    4. Analyze convergence as the number of steps increases

---

## European Pricing: Recap

In the CRR binomial model with $N$ time steps:

$$
\Delta t = \frac{T}{N}, \quad u = e^{\sigma\sqrt{\Delta t}}, \quad d = \frac{1}{u}, \quad q = \frac{e^{r\Delta t} - d}{u - d}
$$

For a **European** option, backward induction gives:

$$
V_{n,j} = e^{-r\Delta t}\left[q \, V_{n+1,j+1} + (1 - q) \, V_{n+1,j}\right]
$$

starting from terminal payoffs $V_{N,j} = \Phi(S_{N,j})$.

---

## American Pricing: The Maximum Condition

For an **American** option, at each node $(n, j)$ we compare the **continuation value** with the **immediate exercise value**:

$$
\boxed{
V_{n,j} = \max\left(\Phi(S_{n,j}), \; e^{-r\Delta t}\left[q \, V_{n+1,j+1} + (1 - q) \, V_{n+1,j}\right]\right)
}
$$

where:

- $\Phi(S_{n,j})$ is the intrinsic value (e.g., $K - S_{n,j}$ for a put)
- The discounted expectation is the continuation value
- The $\max$ operator enforces the early-exercise constraint

### Algorithm

!!! note "Backward Induction with Early Exercise"
    **Step 1.** Build the stock price tree: $S_{n,j} = S_0 \cdot u^j \cdot d^{n-j}$
    
    **Step 2.** Set terminal values: $V_{N,j} = \Phi(S_{N,j})$ for $j = 0, 1, \ldots, N$
    
    **Step 3.** For $n = N-1$ down to $0$, for $j = 0, 1, \ldots, n$:
    
    $$
    \begin{aligned}
    \text{Continuation} &= e^{-r\Delta t}\left[q \, V_{n+1,j+1} + (1-q) \, V_{n+1,j}\right] \\
    \text{Exercise} &= \Phi(S_{n,j}) \\
    V_{n,j} &= \max(\text{Exercise}, \text{Continuation})
    \end{aligned}
    $$
    
    **Step 4.** The American option price is $V_{0,0}$.

---

## Implementation: American Put

### Efficient Array-Based Algorithm

Rather than storing the full tree, we can work with a single array that is updated backward in time.

**`american_put_binomial.py`**

```python
import numpy as np

def american_put_binomial(S, K, T, r, sigma, N):
    """
    Price an American put option using the CRR binomial tree.

    Parameters
    ----------
    S : float — Current stock price
    K : float — Strike price
    T : float — Time to maturity (years)
    r : float — Risk-free rate (continuous)
    sigma : float — Volatility
    N : int — Number of time steps

    Returns
    -------
    float — American put option price
    """
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    q = (np.exp(r * dt) - d) / (u - d)

    # Terminal stock prices
    ST = np.array([S * (u ** j) * (d ** (N - j)) for j in range(N + 1)])

    # Terminal payoff
    P = np.maximum(K - ST, 0)

    # Backward induction with early-exercise check
    for i in range(N - 1, -1, -1):
        # Continuation value (discounted expectation)
        P = np.exp(-r * dt) * (q * P[1:i + 2] + (1 - q) * P[0:i + 1])

        # Stock prices at time step i
        ST = np.array([S * (u ** j) * (d ** (i - j)) for j in range(i + 1)])

        # Early exercise check
        P = np.maximum(K - ST, P)

    return P[0]


# === Example ===
if __name__ == "__main__":
    S, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.20

    for N in [50, 100, 200, 500, 1000]:
        price = american_put_binomial(S, K, T, r, sigma, N)
        print(f"  N = {N:5d}:  American Put = {price:.4f}")
```

!!! example "Sample Output"
    ```
      N =    50:  American Put = 6.0860
      N =   100:  American Put = 6.0781
      N =   200:  American Put = 6.0826
      N =   500:  American Put = 6.0808
      N =  1000:  American Put = 6.0814
    ```
    The price converges to approximately $6.08$ as $N$ increases.

---

## Comparing American and European Puts

The difference between American and European put prices is the **early exercise premium**:

```python
from scipy.stats import norm

def european_put_bs(S, K, T, r, sigma):
    """Black-Scholes European put price."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

S, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.20

P_am = american_put_binomial(S, K, T, r, sigma, 500)
P_eu = european_put_bs(S, K, T, r, sigma)

print(f"European Put:          {P_eu:.4f}")
print(f"American Put:          {P_am:.4f}")
print(f"Early Exercise Premium: {P_am - P_eu:.4f}")
```

---

## Identifying the Early-Exercise Boundary

At each node, the tree reveals **whether exercise is optimal**. By collecting nodes where $\Phi(S_{n,j}) > \text{Continuation Value}$, we can trace the exercise boundary.

```python
import matplotlib.pyplot as plt

def early_exercise_boundary(S, K, T, r, sigma, N):
    """
    Compute the early-exercise boundary from a binomial tree.
    Returns arrays of (time, stock_price) where exercise is optimal.
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

    boundary = []

    # Backward induction
    for n in range(N - 1, -1, -1):
        for j in range(n + 1):
            continuation = np.exp(-r * dt) * (
                q * tree_V[j + 1, n + 1] + (1 - q) * tree_V[j, n + 1]
            )
            exercise = K - tree_S[j, n]
            tree_V[j, n] = max(continuation, exercise)

            if exercise > continuation and exercise > 0:
                boundary.append((n * dt, tree_S[j, n]))

    return np.array(boundary)


# === Plot the boundary ===
S, K, T, r, sigma, N = 100, 100, 1.0, 0.05, 0.20, 200

bd = early_exercise_boundary(S, K, T, r, sigma, N)

plt.figure(figsize=(10, 6))
plt.scatter(bd[:, 0], bd[:, 1], s=3, alpha=0.5, color="steelblue")
plt.axhline(K, color="gray", linestyle="--", linewidth=0.8, label=f"Strike K = {K}")
plt.xlabel("Time (years)")
plt.ylabel("Stock Price at Exercise")
plt.title("Early-Exercise Boundary for American Put (Binomial Tree)")
plt.gca().invert_xaxis()
plt.legend()
plt.tight_layout()
plt.show()
```

The boundary shows:

- Early exercise occurs at **low stock prices** (deep ITM for puts)
- The boundary $S^*(t)$ **rises toward** $K$ as maturity approaches
- At $t = T$, the boundary equals $K$ (exercise whenever ITM at expiry)

---

## Convergence Analysis

The CRR binomial tree converges to the continuous-time American option price, but with **oscillatory behavior** due to the discrete grid:

$$
V_{\text{binomial}}(N) = V_{\text{American}} + O\left(\frac{1}{\sqrt{N}}\right) + \text{oscillatory terms}
$$

### Richardson Extrapolation

To accelerate convergence, use prices from two step sizes:

$$
V_{\text{extrapolated}} = 2 \, V(2N) - V(N)
$$

This eliminates the leading error term and often yields fourth-decimal accuracy with moderate $N$.

### Convergence Behavior

| Steps $N$ | American Put Price | Change |
|---|---|---|
| 50 | 6.0860 | — |
| 100 | 6.0781 | $-0.0079$ |
| 200 | 6.0826 | $+0.0045$ |
| 500 | 6.0808 | $-0.0018$ |
| 1000 | 6.0814 | $+0.0006$ |

---

## Summary

$$
\boxed{
V_{n,j} = \max\left(\Phi(S_{n,j}), \; e^{-r\Delta t}\left[q \, V_{n+1,j+1} + (1-q) \, V_{n+1,j}\right]\right)
}
$$

| Aspect | Description |
|---|---|
| Method | Backward induction with $\max$ operator |
| Complexity | $O(N^2)$ time, $O(N)$ space (array method) |
| Convergence | $O(1/\sqrt{N})$ with oscillation |
| Boundary | Naturally identified from exercise decisions |
| Strength | Simple, robust, handles dividends and exotics |

**The binomial tree remains the workhorse method for American option pricing: intuitive, flexible, and easily extended to handle dividends, time-varying parameters, and path-dependent features.**
