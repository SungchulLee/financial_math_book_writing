# Brownian Motion

Brownian motion (the Wiener process) is the unique continuous-time process with continuous paths, independent stationary Gaussian increments, and it serves as the fundamental building block for stochastic calculus and mathematical finance.

## Definition

A stochastic process $\{W_t\}_{t \geq 0}$ is a **standard Brownian motion** if:

1. $W_0 = 0$
2. **Independent increments**: for $0 \leq t_1 < t_2 < \cdots < t_n$, the increments $W_{t_2} - W_{t_1}, W_{t_3} - W_{t_2}, \ldots$ are independent
3. **Gaussian increments**: $W_t - W_s \sim \mathcal{N}(0, t - s)$ for $0 \leq s < t$
4. **Continuous paths**: $t \mapsto W_t(\omega)$ is continuous for almost every $\omega$

The covariance structure is $\operatorname{Cov}(W_s, W_t) = \min(s, t)$, and the moment generating function is $\mathbb{E}[e^{\theta W_t}] = \exp(\tfrac{1}{2}\theta^2 t)$.

## Explanation

Brownian motion is the unique process that is simultaneously continuous, Markov, and has stationary independent Gaussian increments. It arises as the scaling limit of any random walk with finite variance via Donsker's theorem.

Key properties include: $\mathbb{E}[W_t] = 0$, $\mathbb{E}[W_t^2] = t$, and more generally the even moments $\mathbb{E}[W_t^{2k}] = (2k)!/(2^k k!)\, t^k$ (with odd moments zero by symmetry). The process is a martingale, and $W_t^2 - t$ is also a martingale.

Brownian motion has the **Markov property**: given $W_s$, the future process $\{W_t - W_s : t > s\}$ is independent of $\{W_u : u \leq s\}$. This means the current value contains all information relevant for predicting future behavior.

The increments scale as $W_{t+\Delta t} - W_t \sim \mathcal{N}(0, \Delta t)$, so the typical displacement is of order $\sqrt{\Delta t}$. This $\sqrt{\Delta t}$ scaling (not $\Delta t$) is the fundamental reason why stochastic calculus differs from ordinary calculus.

## Examples

Simulate Brownian motion paths and verify the distributional properties.

```python
import numpy as np

np.random.seed(42)
T, n, n_paths = 1.0, 1000, 5
dt = T / n
t = np.linspace(0, T, n + 1)

# Simulate paths
dW = np.sqrt(dt) * np.random.randn(n_paths, n)
W = np.column_stack([np.zeros(n_paths), np.cumsum(dW, axis=1)])

# Verify E[W_T] = 0 and Var(W_T) = T via many paths
n_mc = 100000
W_T = np.sqrt(T) * np.random.randn(n_mc)
print(f"E[W_T] = {W_T.mean():.4f} (expect 0)")
print(f"Var(W_T) = {W_T.var():.4f} (expect {T})")
print(f"E[W_T^4] = {np.mean(W_T**4):.4f} (expect {3*T**2:.4f})")

# Verify covariance: Cov(W_s, W_t) = min(s,t)
s_idx, t_idx = 300, 700  # s=0.3, t=0.7
W_full = np.sqrt(dt) * np.random.randn(n_mc, n)
W_full = np.column_stack([np.zeros(n_mc), np.cumsum(W_full, axis=1)])
cov_emp = np.mean(W_full[:, s_idx] * W_full[:, t_idx])
print(f"Cov(W_0.3, W_0.7) = {cov_emp:.4f} (expect {min(0.3, 0.7):.4f})")
```
