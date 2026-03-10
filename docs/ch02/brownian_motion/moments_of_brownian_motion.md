# Moments of Brownian Motion

The complete moment structure of Brownian motion follows from its Gaussian distribution via the moment generating function, connecting to Hermite polynomials and Wiener chaos decomposition.

## Definition

For standard Brownian motion $W_t \sim \mathcal{N}(0, t)$, the **moment generating function** is

$$
\mathbb{E}[e^{\theta W_t}] = \exp\!\left(\frac{1}{2}\theta^2 t\right)
$$

Expanding the MGF in a Taylor series and matching coefficients yields the moments:

$$
\mathbb{E}[W_t^{2k}] = \frac{(2k)!}{2^k\, k!}\, t^k, \qquad \mathbb{E}[W_t^{2k+1}] = 0
$$

The odd moments vanish by the symmetry $W_t \overset{d}{=} -W_t$. The even moments give $\mathbb{E}[W_t^2] = t$, $\mathbb{E}[W_t^4] = 3t^2$, $\mathbb{E}[W_t^6] = 15t^3$.

## Explanation

The formula $\mathbb{E}[W_t^{2k}] = (2k-1)!!\, t^k$ (where $(2k-1)!! = 1 \cdot 3 \cdot 5 \cdots (2k-1)$) is a standard result for Gaussian random variables. The fourth moment $\mathbb{E}[W_t^4] = 3t^2$ is particularly important: since $\operatorname{Var}(W_t^2) = \mathbb{E}[W_t^4] - (\mathbb{E}[W_t^2])^2 = 3t^2 - t^2 = 2t^2$, the excess kurtosis is $\mathbb{E}[W_t^4]/(\mathbb{E}[W_t^2])^2 - 3 = 0$, confirming Gaussianity.

The cross-moment $\mathbb{E}[W_s W_t] = \min(s,t)$ for $s \leq t$ follows from $W_s W_t = W_s(W_t - W_s) + W_s^2$, where the first term has zero expectation by independence. More generally, the Isserlis-Wick theorem computes any moment of joint Gaussian variables by summing over all pair partitions.

## Examples

Verify Brownian motion moments by Monte Carlo simulation.

```python
import numpy as np

np.random.seed(42)
t = 2.0
n_samples = 500000
W_t = np.sqrt(t) * np.random.randn(n_samples)

# Verify moments up to order 8
for k in range(1, 5):
    emp_moment = np.mean(W_t**(2*k))
    # (2k)! / (2^k k!) * t^k
    from math import factorial
    theory = factorial(2*k) / (2**k * factorial(k)) * t**k
    print(f"E[W^{2*k}]: empirical={emp_moment:.4f}, theory={theory:.4f}")

# Odd moments should be zero
for k in [1, 3, 5]:
    print(f"E[W^{k}]: {np.mean(W_t**k):.4f} (expect ~0)")

# Cross-moment: E[W_s * W_t] = min(s,t)
s, t2 = 0.5, 2.0
n = 10000
dt = 0.01
steps = int(t2 / dt)
paths = np.cumsum(np.sqrt(dt) * np.random.randn(n_samples, steps), axis=1)
s_idx, t_idx = int(s / dt) - 1, steps - 1
cov = np.mean(paths[:, s_idx] * paths[:, t_idx])
print(f"\nCov(W_{s}, W_{t2}) = {cov:.4f} (expect {min(s, t2):.4f})")
```
