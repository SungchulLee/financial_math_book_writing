# Pricing Exotic Options with Monte Carlo Simulation

## Introduction

**Monte Carlo simulation** is the most versatile and widely used method for pricing exotic options. By simulating complete price paths under the risk-neutral measure, Monte Carlo naturally handles **path dependency**, **multi-asset dependencies**, and **complex payoff structures** without the state-space explosion that plagues tree methods. Combined with **variance reduction techniques**, Monte Carlo provides an efficient and flexible pricing framework for virtually any exotic derivative.

!!! info "Prerequisites"
    - [Black–Scholes Formula](../../ch06/black_scholes_formula/bs_formula_statement.md) (risk-neutral pricing)
    - [Computational Examples](../../ch06/black_scholes_formula/computational_examples.md) (basic Monte Carlo for vanillas)
    - [LSM Monte Carlo](../american_options/lsm_monte_carlo.md) (simulation with early exercise)
    - [Asian Options](asian_options.md) and [Lookback Options](lookback_options.md) (payoff definitions)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Implement Monte Carlo pricing for Asian and lookback options
    2. Apply antithetic variates and control variates for variance reduction
    3. Construct confidence intervals for Monte Carlo price estimates
    4. Understand the convergence rate and its implications

---

## Monte Carlo Pricing Framework

### Risk-Neutral Simulation

Under the risk-neutral measure $\mathbb{Q}$, the price of any derivative with payoff $\Phi$ is:

$$
V_0 = e^{-rT}\, \mathbb{E}^{\mathbb{Q}}[\Phi]
$$

For path-dependent options, $\Phi$ depends on the entire path $\{S_{t_0}, S_{t_1}, \ldots, S_{t_M}\}$. We simulate this path using the GBM discretization:

$$
\boxed{
S_{t_{k+1}} = S_{t_k} \exp\left[\left(r - \tfrac{1}{2}\sigma^2\right)\Delta t + \sigma\sqrt{\Delta t}\, Z_k\right], \quad Z_k \sim N(0,1)
}
$$

where $\Delta t = T/M$ and $M$ is the number of time steps.

### Algorithm

!!! note "Monte Carlo Pricing Algorithm"
    **Step 1.** For $i = 1, 2, \ldots, N$ (number of simulations):
    
    - Generate a price path $\{S_{t_0}^{(i)}, S_{t_1}^{(i)}, \ldots, S_{t_M}^{(i)}\}$ using GBM
    - Compute the payoff $\Phi^{(i)}$ from the path (respecting barriers, averages, etc.)
    
    **Step 2.** Estimate the option price:
    
    $$\hat{V}_0 = e^{-rT} \cdot \frac{1}{N}\sum_{i=1}^{N} \Phi^{(i)}$$
    
    **Step 3.** Compute the standard error:
    
    $$\text{SE} = \frac{\hat{\sigma}_{\Phi}}{\sqrt{N}}, \quad \text{where } \hat{\sigma}_{\Phi}^2 = \frac{1}{N-1}\sum_{i=1}^{N}\left(\Phi^{(i)} - \bar{\Phi}\right)^2$$

The 95% confidence interval is $\hat{V}_0 \pm 1.96 \cdot e^{-rT} \cdot \text{SE}$.

---

## Implementation: Asian Call Option

### Arithmetic Average Asian Call

```python
import numpy as np

def asian_call_monte_carlo(S, K, T, r, sigma, M, N):
    """Price an arithmetic average Asian call via Monte Carlo."""
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

    price = np.exp(-r * T) * np.mean(payoff)
    se = np.exp(-r * T) * np.std(payoff) / np.sqrt(N)
    return price, se
```

### Lookback Call Option

The same framework adapts to lookback options by replacing the average with the extremum:

```python
def lookback_call_monte_carlo(S, K, T, r, sigma, M, N):
    """Price a fixed-strike lookback call via Monte Carlo."""
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

    price = np.exp(-r * T) * np.mean(payoff)
    se = np.exp(-r * T) * np.std(payoff) / np.sqrt(N)
    return price, se
```

---

## Variance Reduction Techniques

The standard Monte Carlo convergence rate is $O(1/\sqrt{N})$—to halve the standard error requires quadrupling the number of simulations. Variance reduction techniques improve this effective convergence rate without increasing the number of paths.

### Antithetic Variates

**Idea.** For each simulated path using random draws $\{Z_1, Z_2, \ldots, Z_M\}$, also compute the path using $\{-Z_1, -Z_2, \ldots, -Z_M\}$. Average the two payoffs:

$$
\boxed{
\hat{\Phi}^{(i)}_{\text{anti}} = \frac{1}{2}\left[\Phi(Z_1, \ldots, Z_M) + \Phi(-Z_1, \ldots, -Z_M)\right]
}
$$

**Why it works.** If $\Phi$ is a monotone function of the random inputs, the correlation between $\Phi(Z)$ and $\Phi(-Z)$ is negative, reducing the variance of the average:

$$
\text{Var}(\hat{\Phi}_{\text{anti}}) = \frac{1}{4}\left[\text{Var}(\Phi(Z)) + \text{Var}(\Phi(-Z)) + 2\,\text{Cov}(\Phi(Z), \Phi(-Z))\right]
$$

When the covariance is negative, $\text{Var}(\hat{\Phi}_{\text{anti}}) < \text{Var}(\Phi(Z))$.

```python
def asian_call_antithetic(S, K, T, r, sigma, M, N):
    """Asian call with antithetic variates."""
    dt = T / M
    payoff = np.zeros(N)

    for i in range(N):
        z = np.random.normal(size=M)

        # Original path
        increments = (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z
        S_path1 = S * np.exp(np.cumsum(increments))
        S_path1 = np.insert(S_path1, 0, S)

        # Antithetic path
        increments_anti = (r - 0.5 * sigma**2) * dt - sigma * np.sqrt(dt) * z
        S_path2 = S * np.exp(np.cumsum(increments_anti))
        S_path2 = np.insert(S_path2, 0, S)

        avg1 = np.mean(S_path1)
        avg2 = np.mean(S_path2)
        payoff[i] = 0.5 * (max(avg1 - K, 0) + max(avg2 - K, 0))

    price = np.exp(-r * T) * np.mean(payoff)
    se = np.exp(-r * T) * np.std(payoff) / np.sqrt(N)
    return price, se
```

### Control Variates

**Idea.** Use a **correlated quantity with known expectation** to reduce variance. The European call price $C_{\text{BS}}$ is known analytically, and the Monte Carlo estimate $\hat{C}_{\text{MC}}$ of the European call is computed along the same paths as the exotic option.

The **control variate estimator** adjusts the exotic price:

$$
\boxed{
\hat{V}_{\text{CV}} = \hat{V}_{\text{exotic}} + \beta\left(C_{\text{BS}} - \hat{C}_{\text{MC}}\right)
}
$$

where $\beta$ is chosen to minimize variance (often set to $\beta = 1$ in practice, which corresponds to a simple additive correction).

**Why it works.** If the exotic and vanilla payoffs are positively correlated (they are, since both depend on the same underlying paths), the systematic error in $\hat{C}_{\text{MC}}$ relative to $C_{\text{BS}}$ partially cancels the error in $\hat{V}_{\text{exotic}}$.

```python
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    """Analytical Black-Scholes call price."""
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def asian_call_control_variate(S, K, T, r, sigma, M, N):
    """Asian call with European call as control variate."""
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
```

### Geometric Asian as Control Variate

For arithmetic Asian options specifically, the **geometric average Asian option** provides an even better control variate than the European call, because the geometric average is more highly correlated with the arithmetic average:

$$
\hat{V}_{\text{arith}} = \hat{V}_{\text{arith,MC}} + \left(V_{\text{geom,exact}} - \hat{V}_{\text{geom,MC}}\right)
$$

This typically provides superior variance reduction compared to the European call control variate.

---

## Convergence and Error Analysis

### Convergence Rate

The Monte Carlo estimator converges at rate $O(1/\sqrt{N})$ regardless of the problem dimension:

$$
\text{SE} = \frac{\sigma_{\Phi}}{\sqrt{N}}
$$

This **dimension-independent** convergence rate is the key advantage of Monte Carlo over grid-based methods, which suffer from the curse of dimensionality.

### Sources of Error

| Error Source | Magnitude | Control |
|---|---|---|
| Statistical (sampling) | $O(1/\sqrt{N})$ | Increase $N$, use variance reduction |
| Discretization (time grid) | $O(\Delta t) = O(1/M)$ | Increase $M$ (number of time steps) |
| Barrier discretization bias | $O(1/\sqrt{M})$ | Apply continuous monitoring correction |

### Practical Guidelines

For a target standard error $\epsilon$:

- Required simulations: $N = \sigma_\Phi^2 / \epsilon^2$
- Antithetic variates typically reduce $N$ by a factor of 2–4
- Control variates can reduce $N$ by a factor of 10–100 (for well-correlated controls)

---

## Multi-Asset Monte Carlo

Monte Carlo extends naturally to **multi-asset options** (rainbows, baskets) by simulating correlated price paths. For $d$ assets with correlation matrix $\Sigma$:

1. Generate independent standard normals $Z = (Z_1, \ldots, Z_d)$
2. Apply Cholesky decomposition $L$ where $\Sigma = LL^\top$
3. Compute correlated normals $\tilde{Z} = LZ$
4. Simulate each asset using its own correlated random input

This is the primary reason Monte Carlo dominates for multi-asset exotics: the computational cost scales linearly in dimension $d$, while tree methods scale exponentially.

---

## Summary

$$
\boxed{
\hat{V}_0 = e^{-rT} \cdot \frac{1}{N}\sum_{i=1}^{N} \Phi^{(i)}, \quad \text{SE} = \frac{e^{-rT}\, \hat{\sigma}_\Phi}{\sqrt{N}}
}
$$

| Aspect | Description |
|---|---|
| Core method | Simulate GBM paths, compute payoffs, average and discount |
| Convergence | $O(1/\sqrt{N})$, dimension-independent |
| Antithetic variates | Pair each path with its negated random draws |
| Control variates | Use European call (or geometric Asian) to correct systematic error |
| Multi-asset | Correlated simulation via Cholesky decomposition |
| Main advantage | Handles path dependency, multi-asset, complex payoffs |
| Main limitation | Slow convergence without variance reduction; difficult for early exercise |

**Monte Carlo simulation is the dominant pricing method for exotic options due to its flexibility with path-dependent, multi-asset, and complex payoff structures, with variance reduction techniques providing the efficiency needed for practical applications.**

---

## Exercises

**Exercise 1.** For antithetic variates, show that $\text{Var}(\hat{\Phi}_{\text{anti}}) < \text{Var}(\hat{\Phi})$ whenever $\text{Cov}(\Phi(Z), \Phi(-Z)) < 0$. Under what conditions on the payoff function $\Phi$ is this covariance guaranteed to be negative? Give an example of a payoff where antithetic variates provide no variance reduction.

??? success "Solution to Exercise 1"
    **Variance of the antithetic estimator.** The standard estimator uses $N$ independent payoffs $\Phi^{(i)}$, each with variance $\sigma^2 = \text{Var}(\Phi)$:

    $$
    \text{Var}(\hat{\Phi}) = \frac{\sigma^2}{N}
    $$

    The antithetic estimator pairs each draw: $\hat{\Phi}_{\text{anti}}^{(i)} = \frac{1}{2}[\Phi(Z^{(i)}) + \Phi(-Z^{(i)})]$. Using $N$ such pairs:

    $$
    \text{Var}(\hat{\Phi}_{\text{anti}}) = \frac{1}{N}\text{Var}\!\left(\frac{\Phi(Z) + \Phi(-Z)}{2}\right) = \frac{1}{4N}\bigl[\text{Var}(\Phi(Z)) + \text{Var}(\Phi(-Z)) + 2\,\text{Cov}(\Phi(Z), \Phi(-Z))\bigr]
    $$

    Since $Z$ and $-Z$ have the same distribution, $\text{Var}(\Phi(Z)) = \text{Var}(\Phi(-Z)) = \sigma^2$:

    $$
    \text{Var}(\hat{\Phi}_{\text{anti}}) = \frac{\sigma^2 + \text{Cov}(\Phi(Z), \Phi(-Z))}{2N}
    $$

    This is less than $\frac{\sigma^2}{N}$ whenever $\text{Cov}(\Phi(Z), \Phi(-Z)) < 0$, i.e., whenever $\sigma^2 + \text{Cov} < 2\sigma^2$, which holds when the covariance is negative.

    **When is the covariance negative?** If $\Phi$ is a **monotone function** of its random inputs (e.g., an increasing function of a single normal draw), then $\Phi(Z)$ and $\Phi(-Z)$ are negatively correlated. This follows because when $Z$ is large and positive, $\Phi(Z)$ is large but $\Phi(-Z)$ is small, and vice versa.

    More precisely, if $g$ is monotone, then $\text{Cov}(g(Z), g(-Z)) \leq 0$ by the rearrangement inequality (or by noting that $-Z$ is a decreasing function of $Z$, making the composition $g(-Z)$ monotone in the opposite direction from $g(Z)$).

    **Example with no variance reduction:** Consider a payoff that depends on $|Z|$ rather than $Z$ itself, such as a straddle-like payoff $\Phi(Z) = |S_0 e^{\mu + \sigma Z} - K|$. Since $\Phi(Z) = \Phi(-Z)$ when the payoff is symmetric about $K$ (and for a pure absolute-value payoff), we get $\text{Cov}(\Phi(Z), \Phi(-Z)) = \text{Var}(\Phi) > 0$, and antithetic variates actually **increase** variance. In general, any payoff that is an even function of the random inputs gains nothing from antithetic variates.

---


**Exercise 2.** Implement a Monte Carlo pricer for an arithmetic average Asian call with $S_0 = 100$, $K = 100$, $T = 1$, $r = 5\%$, $\sigma = 20\%$, $M = 50$ time steps, and $N = 10{,}000$ paths. (a) Compute the price and 95% confidence interval without variance reduction. (b) Repeat with antithetic variates. (c) Repeat with a European call control variate. Compare the standard errors across the three methods.

??? success "Solution to Exercise 2"
    **Implementation description** for $S_0 = 100$, $K = 100$, $T = 1$, $r = 0.05$, $\sigma = 0.20$, $M = 50$, $N = 10{,}000$.

    **(a) Plain Monte Carlo.** Simulate $N = 10{,}000$ GBM paths with $M = 50$ time steps. For each path, compute the arithmetic average of all $M + 1$ price points (including $S_0$), then the payoff $\max(\bar{S} - K, 0)$. The price estimate is:

    $$
    \hat{V} = e^{-rT} \cdot \frac{1}{N}\sum_{i=1}^{N}\max(\bar{S}^{(i)} - K, 0)
    $$

    The 95% confidence interval is $\hat{V} \pm 1.96 \cdot e^{-rT} \cdot \hat{\sigma}/\sqrt{N}$. Typical results: $\hat{V} \approx 5.5$--$6.0$ with SE $\approx 0.08$--$0.10$.

    **(b) Antithetic variates.** For each of $N = 10{,}000$ pairs, generate $Z_1, \ldots, Z_M$ and compute both the original path (using $+Z_k$) and the antithetic path (using $-Z_k$). Average the two payoffs. The SE typically drops by a factor of about $1.5$--$2.0$, giving SE $\approx 0.05$--$0.07$.

    **(c) European call control variate.** Along each path, record both $\bar{S}^{(i)}$ (for the Asian payoff) and $S_T^{(i)}$ (for the European payoff). Compute:

    $$
    \hat{V}_{\text{CV}} = \hat{V}_{\text{Asian}} + (C_{\text{BS}} - \hat{C}_{\text{MC}})
    $$

    The BS call price is $C_{\text{BS}} \approx 10.45$. The control variate correction reduces SE by a factor of roughly $3$--$5$, giving SE $\approx 0.02$--$0.03$.

    **Comparison:**

    | Method | Typical SE | Relative efficiency |
    |---|---|---|
    | Plain MC | $\sim 0.09$ | 1.0x |
    | Antithetic | $\sim 0.06$ | $\sim 2$x |
    | Control variate (European) | $\sim 0.025$ | $\sim 13$x |

    The control variate method provides the best variance reduction because the European call payoff is positively correlated with the Asian call payoff (both increase when the underlying path is high).

---


**Exercise 3.** The Monte Carlo convergence rate is $O(1/\sqrt{N})$. If you need to reduce the standard error by a factor of 10, how many additional paths are required? If a control variate reduces the effective variance by a factor of 50, how does this change your answer? Explain why variance reduction techniques are essential for practical Monte Carlo pricing.

??? success "Solution to Exercise 3"
    **Paths required for a 10x reduction in SE.** The standard error is $\text{SE} = \sigma / \sqrt{N}$. To reduce SE by a factor of 10:

    $$
    \frac{\sigma}{\sqrt{N'}} = \frac{1}{10} \cdot \frac{\sigma}{\sqrt{N}} \quad \Longrightarrow \quad N' = 100\, N
    $$

    So we need **100 times** as many paths. If we started with $N = 10{,}000$, we now need $N' = 1{,}000{,}000$.

    **With a control variate reducing variance by factor 50.** The effective variance becomes $\sigma_{\text{CV}}^2 = \sigma^2 / 50$. The SE with the control variate is:

    $$
    \text{SE}_{\text{CV}} = \frac{\sigma / \sqrt{50}}{\sqrt{N}} = \frac{\sigma}{\sqrt{50\, N}}
    $$

    To achieve the same 10x reduction in SE from the **original** level:

    $$
    \frac{\sigma}{\sqrt{50\, N'}} = \frac{1}{10} \cdot \frac{\sigma}{\sqrt{N}} \quad \Longrightarrow \quad 50\, N' = 100\, N \quad \Longrightarrow \quad N' = 2\, N
    $$

    With the control variate, we only need **twice** as many paths instead of 100 times as many.

    **Why variance reduction is essential.** The $O(1/\sqrt{N})$ convergence rate means brute-force accuracy improvements are extremely expensive. Each additional decimal digit of precision requires 100x more computation. Variance reduction techniques effectively increase the convergence rate by reducing $\sigma$, making Monte Carlo practically feasible for the precision levels required in derivatives pricing (typically 1–2 basis points).

---


**Exercise 4.** For multi-asset Monte Carlo pricing of a rainbow option on $d = 3$ correlated assets, describe the Cholesky decomposition procedure. Given the correlation matrix

$$
\Sigma = \begin{pmatrix} 1 & 0.5 & 0.3 \\ 0.5 & 1 & 0.4 \\ 0.3 & 0.4 & 1 \end{pmatrix}
$$

compute the lower triangular Cholesky factor $L$ (at least the first row and column). Explain why the computational cost scales linearly in $d$ for Monte Carlo but exponentially for tree methods.

??? success "Solution to Exercise 4"
    **Cholesky decomposition procedure.** Given the correlation matrix $\Sigma$ for $d$ assets, find the lower triangular matrix $L$ such that $\Sigma = LL^\top$. Then to generate correlated normals: draw independent $Z = (Z_1, \ldots, Z_d) \sim N(0, I)$ and compute $\tilde{Z} = LZ$.

    For the given matrix:

    $$
    \Sigma = \begin{pmatrix} 1 & 0.5 & 0.3 \\ 0.5 & 1 & 0.4 \\ 0.3 & 0.4 & 1 \end{pmatrix}
    $$

    **Computing $L$ row by row:**

    Row 1: $L_{11} = \sqrt{\Sigma_{11}} = 1$

    Row 2: $L_{21} = \Sigma_{21}/L_{11} = 0.5/1 = 0.5$, and $L_{22} = \sqrt{\Sigma_{22} - L_{21}^2} = \sqrt{1 - 0.25} = \sqrt{0.75} \approx 0.8660$

    Row 3: $L_{31} = \Sigma_{31}/L_{11} = 0.3/1 = 0.3$, and $L_{32} = (\Sigma_{32} - L_{31}L_{21})/L_{22} = (0.4 - 0.3 \times 0.5)/0.8660 = 0.25/0.8660 \approx 0.2887$

    $$
    L_{33} = \sqrt{\Sigma_{33} - L_{31}^2 - L_{32}^2} = \sqrt{1 - 0.09 - 0.0833} = \sqrt{0.8267} \approx 0.9092
    $$

    So:

    $$
    L = \begin{pmatrix} 1 & 0 & 0 \\ 0.5 & 0.8660 & 0 \\ 0.3 & 0.2887 & 0.9092 \end{pmatrix}
    $$

    **Why Monte Carlo scales linearly.** For $d$ assets and $N$ paths with $M$ time steps each, the cost is $O(d \cdot M \cdot N)$ — linear in $d$. The Cholesky decomposition is a one-time $O(d^3)$ cost, negligible for moderate $d$.

    In contrast, a binomial tree for $d$ assets requires a $d$-dimensional grid. Each time step has $O(N^d)$ nodes (where $N$ is the number of spatial points per dimension), giving total cost $O(M \cdot N^d)$ — exponential in $d$. For $d = 3$ and $N = 100$ spatial points, the tree has $10^6$ nodes per time step, and for $d = 10$ it is completely infeasible.

---


**Exercise 5.** When pricing a barrier option via Monte Carlo, discrete path monitoring introduces a systematic bias. (a) Explain why the bias causes overestimation of knock-out option prices. (b) Describe the Brownian bridge correction: given simulated values $S_{t_k}$ and $S_{t_{k+1}}$, how do you compute the probability that the continuous path crossed barrier $H$ between these times? (c) How is this probability incorporated into the payoff calculation?

??? success "Solution to Exercise 5"
    **(a) Overestimation bias for knock-out options.** With discrete monitoring at times $t_0, t_1, \ldots, t_M$, the simulated path is only checked at these points. The continuous path may cross the barrier $H$ between monitoring times $t_k$ and $t_{k+1}$ without being detected, because $S_{t_k} > H$ and $S_{t_{k+1}} > H$ does not imply $\min_{t \in [t_k, t_{k+1}]} S_t > H$.

    For a knock-out option, missing a barrier crossing means the option is **not knocked out** when it should be. This leads to an artificially higher survival probability and therefore an **overestimated** knock-out price.

    **(b) Brownian bridge correction.** Given $S_{t_k} = S_k$ and $S_{t_{k+1}} = S_{k+1}$, both above $H$ (for a down-and-out), the probability that the continuous GBM path crossed $H$ in the interval $[t_k, t_{k+1}]$ is:

    $$
    P\!\left(\min_{t \in [t_k, t_{k+1}]} S_t \leq H \;\middle|\; S_{t_k} = S_k,\; S_{t_{k+1}} = S_{k+1}\right) = \exp\!\left(-\frac{2\ln(S_k/H)\ln(S_{k+1}/H)}{\sigma^2 \Delta t}\right)
    $$

    This formula uses the Brownian bridge property: conditional on endpoints, the minimum of a Brownian motion has a known distribution.

    **(c) Incorporating into payoff calculation.** For each simulated path, at each interval $[t_k, t_{k+1}]$:

    1. Check if either $S_k \leq H$ or $S_{k+1} \leq H$ — if so, the barrier is definitely breached
    2. If both are above $H$, compute the crossing probability $p_k$ using the formula above
    3. Generate a uniform random variable $U_k \sim \text{Uniform}(0,1)$; if $U_k < p_k$, declare the barrier breached

    The survival probability for the entire path is the probability of **no** crossing in any interval. In the simplest implementation, the payoff is multiplied by $\prod_{k=0}^{M-1}(1 - p_k)$ rather than using random knock-out decisions, which gives a smoother (lower variance) estimator.

---


**Exercise 6.** The geometric average Asian option price is known analytically and can serve as a control variate for the arithmetic average Asian price. Write the control variate estimator $\hat{V}_{\text{arith,CV}} = \hat{V}_{\text{arith,MC}} + (V_{\text{geom,exact}} - \hat{V}_{\text{geom,MC}})$. Explain why the geometric average is a better control variate than the vanilla European call, relating your answer to the correlation between the two estimators.

??? success "Solution to Exercise 6"
    **Control variate estimator.** For each simulated path $i$, compute both:

    - $\bar{S}_{\text{arith}}^{(i)} = \frac{1}{M+1}\sum_{k=0}^{M} S_{t_k}^{(i)}$ (arithmetic average)
    - $\bar{S}_{\text{geom}}^{(i)} = \left(\prod_{k=0}^{M} S_{t_k}^{(i)}\right)^{1/(M+1)}$ (geometric average)

    The payoffs are $\Phi_{\text{arith}}^{(i)} = (\bar{S}_{\text{arith}}^{(i)} - K)^+$ and $\Phi_{\text{geom}}^{(i)} = (\bar{S}_{\text{geom}}^{(i)} - K)^+$. The control variate estimator is:

    $$
    \hat{V}_{\text{arith,CV}} = e^{-rT}\left[\frac{1}{N}\sum_{i=1}^{N}\Phi_{\text{arith}}^{(i)}\right] + \left(V_{\text{geom,exact}} - e^{-rT}\left[\frac{1}{N}\sum_{i=1}^{N}\Phi_{\text{geom}}^{(i)}\right]\right)
    $$

    where $V_{\text{geom,exact}}$ is the closed-form geometric Asian option price. The geometric average of lognormal variables is lognormal, so the geometric Asian call has an analytical Black–Scholes-type formula with adjusted drift and volatility.

    **Why geometric Asian is a better control variate than the European call.** The effectiveness of a control variate depends on the **correlation** between the control and the target estimator. The variance reduction factor is:

    $$
    \text{Variance reduction} = 1 - \rho^2
    $$

    where $\rho$ is the correlation between the two payoffs.

    The geometric average $\bar{S}_{\text{geom}}$ and arithmetic average $\bar{S}_{\text{arith}}$ are computed from **the same set of prices** $\{S_{t_0}, \ldots, S_{t_M}\}$ along each path. They are both averages of the same path, differing only in the averaging method. Their correlation is extremely high (typically $\rho > 0.99$).

    In contrast, the European call payoff depends only on the **terminal** price $S_T$, not on the entire path. While it is positively correlated with the Asian payoff (both increase when the path is generally high), the correlation is lower (typically $\rho \approx 0.8$--$0.95$) because the Asian payoff is influenced by the entire path trajectory, not just the endpoint.

    Since higher correlation means more variance reduction, the geometric Asian control variate ($\rho^2 \approx 0.99$, variance reduction $\sim 100$x) dramatically outperforms the European call control variate ($\rho^2 \approx 0.8$, variance reduction $\sim 5$x).
