# Least-Squares Monte Carlo (LSM)

## Introduction

The **Least-Squares Monte Carlo (LSM)** method, introduced by **Longstaff and Schwartz (2001)**, prices American options by combining **Monte Carlo simulation** with **regression-based estimation** of the continuation value. It is the dominant method for high-dimensional American-style derivatives where tree and finite difference methods become computationally intractable.

The key insight is that the optimal exercise decision at each time step requires only the **conditional expectation** of the continuation value, which can be approximated by **least-squares regression** on the simulated paths.

!!! info "Prerequisites"
    - [American Option Definition](american_option_definition.md) (optimal stopping formulation)
    - [Early Exercise](early_exercise.md) (when exercise is optimal)
    - [Monte Carlo Pricing](../../ch06/black_scholes_formula/computational_examples.md) (basic simulation methods)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Explain the LSM algorithm step by step
    2. Implement LSM for American put pricing
    3. Choose basis functions for the regression
    4. Understand the bias structure and convergence properties

---

## The Optimal Stopping Problem

The American option price at time $t_0 = 0$ is:

$$
V_0 = \sup_{\tau \in \mathcal{T}} \mathbb{E}^{\mathbb{Q}}\left[e^{-r\tau} \Phi(S_\tau)\right]
$$

At each exercise date $t_k$, the holder compares:

- **Immediate payoff**: $\Phi(S_{t_k})$
- **Continuation value**: $C(t_k, S_{t_k}) = \mathbb{E}^{\mathbb{Q}}\left[e^{-r\Delta t} V_{t_{k+1}} \mid S_{t_k}\right]$

Exercise is optimal when $\Phi(S_{t_k}) \geq C(t_k, S_{t_k})$.

The challenge is that $C(t_k, S_{t_k})$ is a **conditional expectation** that depends on the current state—it cannot be computed directly from simulated paths without some form of approximation.

---

## The LSM Algorithm

### Overview

1. **Simulate** $M$ stock price paths on a discrete time grid $\{t_0, t_1, \ldots, t_N\}$
2. **Work backward** from maturity, estimating the continuation value at each time step via least-squares regression
3. **Compare** immediate payoff vs. estimated continuation value to determine the optimal exercise policy
4. **Price** the option by averaging the discounted payoffs under the estimated policy

### Detailed Steps

!!! note "LSM Algorithm"
    **Step 1: Simulate paths.** Generate $M$ paths of the underlying:
    
    $$S_{t_{k+1}}^{(m)} = S_{t_k}^{(m)} \exp\left[\left(r - \tfrac{1}{2}\sigma^2\right)\Delta t + \sigma\sqrt{\Delta t}\, Z_k^{(m)}\right]$$
    
    for $m = 1, \ldots, M$ and $k = 0, \ldots, N-1$, where $Z_k^{(m)} \sim N(0,1)$.
    
    **Step 2: Initialize at maturity.** Set the cash flow:
    
    $$\text{CF}^{(m)} = \Phi(S_T^{(m)}), \quad \tau^{(m)} = T$$
    
    **Step 3: Backward induction.** For $k = N-1, N-2, \ldots, 1$:
    
    (a) Identify **in-the-money paths**: $\mathcal{I}_k = \{m : \Phi(S_{t_k}^{(m)}) > 0\}$
    
    (b) For ITM paths, compute **discounted future cash flows**:
    
    $$Y^{(m)} = e^{-r(\tau^{(m)} - t_k)} \text{CF}^{(m)}, \quad m \in \mathcal{I}_k$$
    
    (c) **Regress** $Y$ on basis functions of $S_{t_k}$:
    
    $$\hat{C}(t_k, S_{t_k}^{(m)}) = \sum_{p=0}^{P} \hat{\beta}_p \, \psi_p(S_{t_k}^{(m)})$$
    
    where $\hat{\boldsymbol{\beta}}$ minimizes $\sum_{m \in \mathcal{I}_k} (Y^{(m)} - \hat{C}^{(m)})^2$.
    
    (d) **Exercise decision**: for $m \in \mathcal{I}_k$, if $\Phi(S_{t_k}^{(m)}) \geq \hat{C}(t_k, S_{t_k}^{(m)})$:
    
    $$\text{CF}^{(m)} = \Phi(S_{t_k}^{(m)}), \quad \tau^{(m)} = t_k$$
    
    **Step 4: Compute the price.**
    
    $$\hat{V}_0 = \frac{1}{M} \sum_{m=1}^{M} e^{-r\tau^{(m)}} \text{CF}^{(m)}$$

---

## Choice of Basis Functions

The regression quality depends critically on the **basis functions** $\{\psi_p\}_{p=0}^{P}$.

### Common Choices

| Basis | Functions | Notes |
|---|---|---|
| **Monomials** | $1, S, S^2, S^3, \ldots$ | Simple, prone to multicollinearity |
| **Laguerre** | $L_0(S), L_1(S), L_2(S), \ldots$ | Recommended by Longstaff–Schwartz |
| **Chebyshev** | $T_0(x), T_1(x), T_2(x), \ldots$ | Good numerical conditioning |
| **Hermite** | $H_0(x), H_1(x), H_2(x), \ldots$ | Natural for Gaussian distributions |

!!! tip "Practical Recommendation"
    For single-asset American options, **$P = 3$ to $5$ polynomial terms** (e.g., $1, S, S^2, S^3$) typically suffice. Using more than 5–6 terms rarely improves accuracy and can introduce overfitting.

---

## Python Implementation

```python
import numpy as np

def lsm_american_put(S0, K, T, r, sigma, M=50000, N=50, poly_degree=3):
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

    Returns
    -------
    float — Estimated American put price
    """
    dt = T / N
    discount = np.exp(-r * dt)

    # Simulate paths
    Z = np.random.randn(M, N)
    S = np.zeros((M, N + 1))
    S[:, 0] = S0
    for k in range(N):
        S[:, k + 1] = S[:, k] * np.exp(
            (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[:, k]
        )

    # Initialize cash flows at maturity
    payoff = np.maximum(K - S[:, N], 0)
    cashflow = payoff.copy()
    exercise_time = np.full(M, N)

    # Backward induction
    for k in range(N - 1, 0, -1):
        itm = np.where(K - S[:, k] > 0)[0]

        if len(itm) == 0:
            continue

        # Discounted future cash flows for ITM paths
        discount_steps = exercise_time[itm] - k
        Y = cashflow[itm] * np.exp(-r * dt * discount_steps)

        # Basis: polynomial in S
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

    # Discount all cash flows to time 0
    price = np.mean(
        cashflow * np.exp(-r * dt * exercise_time)
    )
    return price


# === Example ===
if __name__ == "__main__":
    np.random.seed(42)
    S0, K, T, r, sigma = 100, 100, 1.0, 0.05, 0.20

    price = lsm_american_put(S0, K, T, r, sigma, M=100000, N=50)
    print(f"LSM American Put Price: {price:.4f}")
```

!!! example "Sample Output"
    ```
    LSM American Put Price: 6.0523
    ```
    Compare with the binomial result ($\approx 6.08$). LSM has a slight **low bias** due to using estimated (rather than true) continuation values.

---

## Bias Structure

### Low Bias of LSM

The LSM estimator uses the **same paths** for regression and exercise decisions. This introduces a subtle bias:

- The estimated continuation value $\hat{C}$ is a noisy approximation of the true $C$
- Exercise decisions based on $\hat{C}$ are **suboptimal** compared to decisions based on $C$
- Suboptimal exercise means **lower payoffs** on average

Therefore:

$$
\boxed{
\hat{V}_{\text{LSM}} \leq V_{\text{American}} \quad \text{(low-biased)}
}
$$

### High-Biased Estimator

A **high-biased** (dual) estimator can be constructed using the **Andersen–Broadie** approach, which provides an upper bound. The true price lies between the low and high estimates:

$$
\hat{V}_{\text{low}} \leq V_{\text{American}} \leq \hat{V}_{\text{high}}
$$

---

## Convergence

### Error Decomposition

The total error has three components:

$$
\text{Total Error} = \underbrace{O(1/\sqrt{M})}_{\text{Monte Carlo}} + \underbrace{O(1/N)}_{\text{time discretization}} + \underbrace{O(P^{-\alpha})}_{\text{regression bias}}
$$

where $\alpha > 0$ depends on the smoothness of the continuation value function.

### Practical Guidance

| Parameter | Typical Range | Effect |
|---|---|---|
| Paths $M$ | $10{,}000$–$100{,}000$ | Reduces MC variance |
| Time steps $N$ | $30$–$100$ | Finer exercise grid |
| Basis degree $P$ | $3$–$5$ | Better continuation approximation |

---

## Advantages and Limitations

### Strengths

- **High-dimensional**: Scales to multi-asset options (baskets, spread options)
- **Path-dependent**: Handles lookback, barrier, and Asian features
- **Flexible**: Works with any stochastic model (stochastic volatility, jumps)
- **No grid**: Avoids the curse of dimensionality affecting tree/FD methods

### Limitations

- **Low bias**: Systematically underestimates the true price
- **Variance**: Requires large $M$ for stable estimates
- **Regression quality**: Sensitive to basis function choice in tails
- **Computational cost**: Slower than trees for single-asset options

---

## Summary

$$
\boxed{
\hat{V}_0 = \frac{1}{M} \sum_{m=1}^{M} e^{-r\tau^{*(m)}} \Phi(S_{\tau^{*(m)}}^{(m)})
}
$$

| Aspect | Description |
|---|---|
| Key idea | Estimate continuation value via regression |
| Basis functions | Polynomials of degree 3–5 |
| Bias | Low-biased (suboptimal exercise) |
| Convergence | $O(1/\sqrt{M})$ Monte Carlo + regression error |
| Best for | Multi-asset and path-dependent American options |

**LSM transforms the American pricing problem from an intractable high-dimensional optimal stopping problem into a sequence of regressions, making it the method of choice for complex derivatives with early-exercise features.**
