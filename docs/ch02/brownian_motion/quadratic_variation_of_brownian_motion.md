# Quadratic Variation of Brownian Motion

The quadratic variation of Brownian motion equals $t$, a non-vanishing second-order contribution that distinguishes stochastic from classical calculus and gives rise to the Ito correction term.

## Definition

For a partition $\Pi = \{0 = t_0 < t_1 < \cdots < t_n = t\}$ of $[0, t]$, the **quadratic variation** of Brownian motion is

$$
[W]_t = \lim_{|\Pi| \to 0} \sum_{k=0}^{n-1} (W_{t_{k+1}} - W_{t_k})^2 = t
$$

where $|\Pi| = \max_k(t_{k+1} - t_k)$ is the mesh size. The convergence holds in $L^2$ and in probability. More precisely, if $\Delta_k = t_{k+1} - t_k$, then

$$
\mathbb{E}\!\left[\sum_k (W_{t_{k+1}} - W_{t_k})^2\right] = t, \qquad \operatorname{Var}\!\left[\sum_k (W_{t_{k+1}} - W_{t_k})^2\right] = 2\sum_k \Delta_k^2 \to 0
$$

## Explanation

The heuristic $(dW_t)^2 = dt$ encapsulates the quadratic variation result and is the fundamental rule of Ito calculus. While individual increments $W_{t_{k+1}} - W_{t_k}$ are random with variance $\Delta_k$, their squares sum deterministically to $t$ in the limit. This happens because the variance of the sum of squared increments vanishes as the partition refines.

By contrast, the **first variation** (total variation) $\sum |W_{t_{k+1}} - W_{t_k}|$ is almost surely infinite: each $|W_{t_{k+1}} - W_{t_k}| \sim \sqrt{\Delta_k}$, so the sum scales as $n\sqrt{\Delta_k} \sim \sqrt{n} \to \infty$.

This non-vanishing quadratic variation is why second-order terms survive in Taylor expansions of functions of Brownian motion, producing the Ito correction $\tfrac{1}{2}\sigma^2 S^2 f''(S)$ in Ito's lemma.

## Examples

Numerically verify that the quadratic variation converges to $t$.

```python
import numpy as np

np.random.seed(42)
T = 1.0

# Simulate one Brownian path at high resolution
n_fine = 100000
dt_fine = T / n_fine
dW = np.sqrt(dt_fine) * np.random.randn(n_fine)
W = np.concatenate([[0], np.cumsum(dW)])

# Compute quadratic variation for different partition sizes
for n in [10, 100, 1000, 10000, 100000]:
    step = n_fine // n
    W_partition = W[::step]
    increments = np.diff(W_partition)
    qv = np.sum(increments**2)
    fv = np.sum(np.abs(increments))  # first variation
    print(f"n={n:6d}: QV={qv:.6f} (expect {T}), "
          f"FV={fv:.4f} (diverges)")
```
