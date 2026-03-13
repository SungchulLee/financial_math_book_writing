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
