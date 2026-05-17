# Least-Squares Monte Carlo (LSM)

### Introduction

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

### The Optimal Stopping Problem

Recall (see [§ Risk-neutral valuation](../../ch04/risk_neutral/risk_neutral_valuation_principle.md)) and (see [§ Stopping times](../../ch02/filtration_and_martingale/stopping_time.md)) for the underlying $\mathbb{Q}$-expectation and stopping-time machinery. The American option price at $t_0 = 0$ is:

$$
V_0 = \sup_{\tau \in \mathcal{T}} \mathbb{E}^{\mathbb{Q}}\left[e^{-r\tau} \Phi(S_\tau)\right]
$$

At each exercise date $t_k$, the holder compares:

- **Immediate payoff**: $\Phi(S_{t_k})$
- **Continuation value**: $C(t_k, S_{t_k}) = \mathbb{E}^{\mathbb{Q}}\left[e^{-r\Delta t} V_{t_{k+1}} \mid S_{t_k}\right]$

Exercise is optimal when $\Phi(S_{t_k}) \geq C(t_k, S_{t_k})$.

The challenge is that $C(t_k, S_{t_k})$ is a **conditional expectation** that depends on the current state—it cannot be computed directly from simulated paths without some form of approximation.

---

### The LSM Algorithm

#### Overview

1. **Simulate** $M$ stock price paths on a discrete time grid $\{t_0, t_1, \ldots, t_N\}$
2. **Work backward** from maturity, estimating the continuation value at each time step via least-squares regression
3. **Compare** immediate payoff vs. estimated continuation value to determine the optimal exercise policy
4. **Price** the option by averaging the discounted payoffs under the estimated policy

#### Detailed Steps

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

### Choice of Basis Functions

The regression quality depends critically on the **basis functions** $\{\psi_p\}_{p=0}^{P}$.

#### Common Choices

| Basis | Functions | Notes |
|---|---|---|
| **Monomials** | $1, S, S^2, S^3, \ldots$ | Simple, prone to multicollinearity |
| **Laguerre** | $L_0(S), L_1(S), L_2(S), \ldots$ | Recommended by Longstaff–Schwartz |
| **Chebyshev** | $T_0(x), T_1(x), T_2(x), \ldots$ | Good numerical conditioning |
| **Hermite** | $H_0(x), H_1(x), H_2(x), \ldots$ | Natural for Gaussian distributions |

!!! tip "Practical Recommendation"
    For single-asset American options, **$P = 3$ to $5$ polynomial terms** (e.g., $1, S, S^2, S^3$) typically suffice. Using more than 5–6 terms rarely improves accuracy and can introduce overfitting.

---

### Python Implementation

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

### Bias Structure

#### Low Bias of LSM

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

#### High-Biased Estimator

A **high-biased** (dual) estimator can be constructed using the **Andersen–Broadie** approach, which provides an upper bound. The true price lies between the low and high estimates:

$$
\hat{V}_{\text{low}} \leq V_{\text{American}} \leq \hat{V}_{\text{high}}
$$

---

### Convergence

#### Error Decomposition

The total error has three components:

$$
\text{Total Error} = \underbrace{O(1/\sqrt{M})}_{\text{Monte Carlo}} + \underbrace{O(1/N)}_{\text{time discretization}} + \underbrace{O(P^{-\alpha})}_{\text{regression bias}}
$$

where $\alpha > 0$ depends on the smoothness of the continuation value function.

#### Practical Guidance

| Parameter | Typical Range | Effect |
|---|---|---|
| Paths $M$ | $10{,}000$–$100{,}000$ | Reduces MC variance |
| Time steps $N$ | $30$–$100$ | Finer exercise grid |
| Basis degree $P$ | $3$–$5$ | Better continuation approximation |

---

### Advantages and Limitations

#### Strengths

- **High-dimensional**: Scales to multi-asset options (baskets, spread options)
- **Path-dependent**: Handles lookback, barrier, and Asian features
- **Flexible**: Works with any stochastic model (stochastic volatility, jumps)
- **No grid**: Avoids the curse of dimensionality affecting tree/FD methods

#### Limitations

- **Low bias**: Systematically underestimates the true price
- **Variance**: Requires large $M$ for stable estimates
- **Regression quality**: Sensitive to basis function choice in tails
- **Computational cost**: Slower than trees for single-asset options

---

### Summary

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

---

## Exercises

**Exercise 1.** Describe the LSM algorithm step by step for an American put with 3 exercise dates. At each exercise date, explain what regression is performed, what the dependent and independent variables are, and how the exercise decision is made.

??? success "Solution to Exercise 1"
    Consider an American put with 3 exercise dates $t_1, t_2, t_3 = T$ (equally spaced). Suppose we simulate $M$ stock price paths $\{S_{t_k}^{(m)}\}$.

    **At $t_3 = T$ (maturity):** Set the cash flow for each path:

    $$
    \text{CF}^{(m)} = (K - S_T^{(m)})^+, \quad \tau^{(m)} = T
    $$

    No regression is needed at maturity since there is no continuation.

    **At $t_2$:** Identify in-the-money paths: $\mathcal{I}_2 = \{m : K - S_{t_2}^{(m)} > 0\}$.

    For each ITM path, compute the discounted future cash flow:

    $$
    Y^{(m)} = e^{-r(T - t_2)} \text{CF}^{(m)}, \quad m \in \mathcal{I}_2
    $$

    **Regression:** The dependent variable is $Y^{(m)}$ (discounted future payoff). The independent variable is $S_{t_2}^{(m)}$ (current stock price). Fit:

    $$
    \hat{C}(t_2, S) = \hat{\beta}_0 + \hat{\beta}_1 S + \hat{\beta}_2 S^2 + \hat{\beta}_3 S^3
    $$

    by ordinary least squares on the ITM paths.

    **Exercise decision:** For each $m \in \mathcal{I}_2$, if $K - S_{t_2}^{(m)} \geq \hat{C}(t_2, S_{t_2}^{(m)})$, update: $\text{CF}^{(m)} = K - S_{t_2}^{(m)}$ and $\tau^{(m)} = t_2$.

    **At $t_1$:** Repeat the same procedure. Identify $\mathcal{I}_1 = \{m : K - S_{t_1}^{(m)} > 0\}$. Compute discounted future cash flows $Y^{(m)} = e^{-r(\tau^{(m)} - t_1)}\text{CF}^{(m)}$ for $m \in \mathcal{I}_1$. Regress $Y$ on polynomial basis functions of $S_{t_1}$ to get $\hat{C}(t_1, S)$. Exercise if $K - S_{t_1}^{(m)} \geq \hat{C}(t_1, S_{t_1}^{(m)})$.

    **Final price:** Discount all cash flows to time 0:

    $$
    \hat{V}_0 = \frac{1}{M}\sum_{m=1}^M e^{-r\tau^{(m)}} \text{CF}^{(m)}
    $$

---


**Exercise 2.** In LSM, the continuation value at time $t_k$ is approximated as $\hat{C}(S_{t_k}) = \sum_{j=0}^{M} a_j \phi_j(S_{t_k})$ where $\phi_j$ are basis functions. Common choices include polynomials, Laguerre polynomials, and Chebyshev polynomials. Discuss the trade-off between using more basis functions (larger $M$) and the risk of overfitting. What is a typical choice of $M$ in practice?

??? success "Solution to Exercise 2"
    The continuation value is approximated by:

    $$
    \hat{C}(S_{t_k}) = \sum_{j=0}^{P} a_j \phi_j(S_{t_k})
    $$

    where $P$ is the number of basis functions (not to be confused with the number of paths $M$).

    **Trade-off between more basis functions and overfitting:**

    - **Too few basis functions ($P$ small):** The regression underfits the true continuation value. The approximation $\hat{C}$ may be biased, leading to systematically wrong exercise decisions. For example, with only a constant and linear term ($P = 1$), the regression cannot capture the curvature of the continuation value near the exercise boundary.

    - **More basis functions ($P$ moderate):** Better approximation of $\hat{C}$, more accurate exercise decisions, and a price closer to the true value.

    - **Too many basis functions ($P$ large):** The regression fits noise in the simulated data rather than the true conditional expectation. Overfitting produces unstable coefficient estimates, especially in the tails where there are few ITM paths. The exercise decisions become erratic, potentially increasing the low bias.

    Additionally, with large $P$, the design matrix $A$ becomes ill-conditioned (especially for monomial bases), causing numerical instability in the least-squares solve. Orthogonal polynomial bases (Laguerre, Chebyshev) mitigate this.

    **Typical choice in practice:** $P = 3$ to $5$ polynomial terms (e.g., $1, S, S^2, S^3$) for single-asset options. Longstaff and Schwartz originally used $P = 2$ (three Laguerre polynomials). For multi-asset options, cross-terms are added (e.g., $S_1, S_2, S_1 S_2, S_1^2, S_2^2$), but the total number of basis functions should be kept moderate relative to the number of ITM paths.

---


**Exercise 3.** LSM produces a low-biased estimate of the American option price (i.e., $\hat{V}_{\text{LSM}} \leq V_{\text{true}}$). Explain why the suboptimal exercise strategy identified by the regression leads to a lower bound rather than an upper bound.

??? success "Solution to Exercise 3"
    The LSM estimator uses a suboptimal exercise policy derived from estimated continuation values. This suboptimality guarantees a **lower bound** rather than an upper bound.

    **Detailed argument:** Let $\tau^*$ be the true optimal stopping time and $\hat{\tau}$ be the stopping time produced by the LSM algorithm. By definition:

    $$
    V_{\text{true}} = \mathbb{E}\left[e^{-r\tau^*}\Phi(S_{\tau^*})\right] \geq \mathbb{E}\left[e^{-r\hat{\tau}}\Phi(S_{\hat{\tau}})\right]
    $$

    The inequality holds because $\tau^*$ is optimal (it maximizes the expected discounted payoff over all stopping times), while $\hat{\tau}$ is one particular stopping time. Any suboptimal exercise strategy yields an expected payoff that is less than or equal to the optimal one.

    The LSM price is:

    $$
    \hat{V}_{\text{LSM}} = \frac{1}{M}\sum_{m=1}^M e^{-r\hat{\tau}^{(m)}}\Phi(S_{\hat{\tau}^{(m)}}^{(m)}) \approx \mathbb{E}\left[e^{-r\hat{\tau}}\Phi(S_{\hat{\tau}})\right] \leq V_{\text{true}}
    $$

    **Why not an upper bound?** An upper bound would require showing that the estimator overvalues the option. But the regression introduces errors in both directions:

    - Sometimes it overestimates $\hat{C}$, causing the holder to continue when exercise is optimal (missed exercise opportunity, reducing value)
    - Sometimes it underestimates $\hat{C}$, causing exercise when continuation is optimal (premature exercise, also reducing value)

    Both types of errors lead to a **suboptimal** exercise policy, which by the definition of the optimal stopping problem, produces a value **below** the true price. The key is that using the same paths for both fitting the regression and making exercise decisions introduces a downward bias. This is sometimes called the "in-sample" bias.

---


**Exercise 4.** For a max-call option on two assets with payoff $(\max(S_1, S_2) - K)^+$, explain how LSM handles the two-dimensional state space. What basis functions would you use for the regression at each exercise date?

??? success "Solution to Exercise 4"
    For a max-call on two assets with payoff $(\max(S_1, S_2) - K)^+$, the state at each exercise date is the pair $(S_1, S_2)$, which is two-dimensional.

    **How LSM handles the two-dimensional state:**

    1. **Path simulation:** Simulate $M$ correlated paths for both assets $(S_1^{(m)}, S_2^{(m)})$ using a bivariate geometric Brownian motion with correlation $\rho$:

        $$
        S_i^{(m)}(t_{k+1}) = S_i^{(m)}(t_k) \exp\left[\left(r - \frac{1}{2}\sigma_i^2\right)\Delta t + \sigma_i \sqrt{\Delta t}\, Z_i^{(m)}\right]
        $$

        where $Z_1$ and $Z_2$ are correlated standard normals with $\text{Corr}(Z_1, Z_2) = \rho$.

    2. **ITM identification:** At each step $t_k$, identify ITM paths where $\max(S_1^{(m)}, S_2^{(m)}) > K$.

    3. **Regression on two-dimensional basis:** The regression approximates $\hat{C}(t_k, S_1, S_2)$ using basis functions of **both** state variables.

    **Recommended basis functions:** A polynomial basis up to degree 2 or 3 in two variables:

    $$
    \{1, \, S_1, \, S_2, \, S_1^2, \, S_2^2, \, S_1 S_2, \, S_1^3, \, S_2^3, \, S_1^2 S_2, \, S_1 S_2^2\}
    $$

    This gives 10 basis functions for a cubic expansion. Alternatively, one can use:

    - $\max(S_1, S_2)$ and $\min(S_1, S_2)$ as state variables (exploiting the payoff structure)
    - Laguerre or Chebyshev polynomials in the transformed variables for better conditioning
    - The intrinsic value $(\max(S_1, S_2) - K)^+$ itself as an additional basis function

    The rest of the algorithm (backward induction, exercise decision, final pricing) proceeds identically to the one-dimensional case. The advantage of LSM is that it scales linearly with the number of paths, regardless of the dimensionality of the state space, whereas tree and finite difference methods suffer from the curse of dimensionality.

---


**Exercise 5.** Compare the LSM method with the binomial tree for pricing a single-asset American put with $S_0 = 100$, $K = 100$, $r = 5\%$, $\sigma = 30\%$, $T = 1$. Discuss the relative strengths of each method in terms of accuracy, computational cost, and ease of implementation. In what situation would you prefer LSM over a binomial tree?

??? success "Solution to Exercise 5"
    For a single-asset American put with $S_0 = 100$, $K = 100$, $r = 0.05$, $\sigma = 0.30$, $T = 1$:

    **Accuracy:**

    - **Binomial tree:** Converges to the true price at rate $O(1/\sqrt{N})$ with oscillatory behavior. With $N = 500$ steps, achieves 4th-decimal accuracy. The method is unbiased in the limit and has no systematic bias direction.
    - **LSM:** Has a systematic **low bias** because the regression-based exercise policy is suboptimal. With $M = 100{,}000$ paths and $N = 50$ steps, typical accuracy is 2--3 decimal places. The Monte Carlo standard error is $O(1/\sqrt{M})$.

    **Computational cost:**

    - **Binomial tree:** $O(N^2)$ time and $O(N)$ space (array method). With $N = 1000$, this is about $10^6$ operations, essentially instantaneous.
    - **LSM:** $O(MN)$ for path simulation plus $O(MNP)$ for regression. With $M = 100{,}000$ and $N = 50$, this is about $5 \times 10^6$ operations, plus the cost of $N$ least-squares solves. Significantly slower for single-asset problems.

    **Ease of implementation:**

    - **Binomial tree:** Very simple: a double loop with a $\max$ condition. About 20 lines of code.
    - **LSM:** More involved: requires path simulation, regression setup, backward updating of cash flows and exercise times. About 40--50 lines of code.

    **When to prefer LSM over binomial trees:** LSM is preferred when:

    1. **Multiple underlyings:** For options on 2+ assets (basket options, spread options, rainbow options), trees suffer the curse of dimensionality ($O(N^d)$ nodes in $d$ dimensions). LSM scales as $O(MN)$ regardless of dimension.
    2. **Path-dependent features:** Lookback, Asian, or barrier features combined with early exercise are naturally handled by LSM since it simulates full paths.
    3. **Complex dynamics:** Stochastic volatility, jumps, or other non-standard models are easily incorporated into the simulation step, while tree construction becomes cumbersome.

    For a single-asset vanilla American put, the binomial tree is clearly superior in both speed and accuracy.
