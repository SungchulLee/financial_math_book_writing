# Holder Continuity and Non-Differentiability

Brownian paths are Holder continuous of every order below 1/2 but nowhere differentiable almost surely, a duality that necessitates stochastic calculus in place of classical analysis.

## Definition

A function $f : [0,T] \to \mathbb{R}$ is **Holder continuous of order** $\alpha > 0$ if there exists $C > 0$ such that

$$
|f(t) - f(s)| \leq C\,|t - s|^\alpha \quad \text{for all } s, t \in [0, T]
$$

For standard Brownian motion, almost every sample path satisfies:

- Holder continuous of order $\alpha$ for every $\alpha < 1/2$
- **Not** Holder continuous of order $1/2$
- Nowhere differentiable

## Explanation

The critical exponent $\alpha = 1/2$ reflects the scaling $W_{t+h} - W_t \sim \mathcal{N}(0, h)$, so $|W_{t+h} - W_t|$ is typically of order $\sqrt{h} = h^{1/2}$. For $\alpha < 1/2$, $h^\alpha$ grows faster than $\sqrt{h}$ as $h \to 0$, giving room for the Holder condition. At $\alpha = 1/2$, the Gaussian increments occasionally exceed any constant multiple of $h^{1/2}$.

Nowhere differentiability follows because differentiability would require $|W_{t+h} - W_t|/h \to L$ for some finite $L$, but Brownian increments scale as $\sqrt{h}$, which dominates $h$ as $h \to 0$. This is precisely why Ito calculus, with its second-order correction term, is required.

## Examples

Estimate the Holder exponent of a Brownian path numerically.

```python
import numpy as np

np.random.seed(42)
n = 100000
dt = 1.0 / n
W = np.cumsum(np.sqrt(dt) * np.random.randn(n))
W = np.concatenate([[0], W])

# Estimate max increment ratio for different h values
for h_exp in range(-1, -5, -1):
    h = 10**h_exp
    k = max(1, int(h * n))
    increments = np.abs(W[k:] - W[:-k])
    max_inc = np.max(increments)
    ratio_half = max_inc / np.sqrt(k * dt)
    print(f"h=10^{h_exp}: max|dW|/sqrt(h) = {ratio_half:.3f} "
          f"(stays bounded => alpha < 1/2 holds)")

# Non-differentiability: |W(t+h)-W(t)|/h diverges
t0_idx = n // 2
for h in [1e-2, 1e-3, 1e-4]:
    k = max(1, int(h * n))
    ratio = abs(W[t0_idx + k] - W[t0_idx]) / (k * dt)
    print(f"|dW/dt| at h={h}: {ratio:.1f} (diverges)")
```
