# Reflection Principle

The reflection principle exploits the path symmetry of Brownian motion to compute probabilities of extremal events, yielding the distribution of the running maximum and first passage times.

## Definition

For standard Brownian motion and $a > 0$, the **reflection principle** states

$$
\mathbb{P}\!\left(\max_{0 \leq s \leq t} W_s \geq a\right) = 2\,\mathbb{P}(W_t \geq a) = 2\!\left(1 - \Phi\!\left(\frac{a}{\sqrt{t}}\right)\right)
$$

where $\Phi$ is the standard normal CDF. The **joint distribution** of the maximum $M_t = \max_{s \leq t} W_s$ and the terminal value $W_t$ is

$$
\mathbb{P}(M_t \geq a,\, W_t \leq b) = \mathbb{P}(W_t \geq 2a - b) \quad \text{for } b \leq a
$$

## Explanation

The proof constructs a bijection between paths. Given a path that reaches level $a$ at time $\tau_a$ and ends at $W_t = b < a$, reflect the segment after $\tau_a$ across level $a$. The reflected path ends at $2a - b > a$, and by the strong Markov property and symmetry of Brownian increments, reflected paths have the same probability as original paths.

This implies $\mathbb{P}(M_t \geq a, W_t \leq a) = \mathbb{P}(W_t \geq a)$. Since $\{W_t \geq a\} \subset \{M_t \geq a\}$, we obtain $\mathbb{P}(M_t \geq a) = \mathbb{P}(M_t \geq a, W_t \leq a) + \mathbb{P}(W_t \geq a) = 2\mathbb{P}(W_t \geq a)$.

Applications include barrier option pricing (the probability that a stock price crosses a barrier) and the distribution of drawdowns in portfolio management.

## Examples

Verify the reflection principle by Monte Carlo simulation.

```python
import numpy as np
from scipy.stats import norm

np.random.seed(42)
t, a = 1.0, 1.5
n_paths, n_steps = 200000, 1000
dt = t / n_steps

# Simulate paths and compute running maximum
dW = np.sqrt(dt) * np.random.randn(n_paths, n_steps)
W = np.cumsum(dW, axis=1)
M_t = np.max(W, axis=1)  # running maximum
W_t = W[:, -1]            # terminal value

# P(max >= a): simulation vs theory
p_sim = np.mean(M_t >= a)
p_theory = 2 * (1 - norm.cdf(a / np.sqrt(t)))
print(f"P(max >= {a}): sim={p_sim:.4f}, theory={p_theory:.4f}")

# Joint distribution: P(max >= a, W_t <= b) = P(W_t >= 2a - b)
b = 0.5
p_joint_sim = np.mean((M_t >= a) & (W_t <= b))
p_joint_theory = 1 - norm.cdf((2*a - b) / np.sqrt(t))
print(f"P(max>={a}, W_t<={b}): sim={p_joint_sim:.4f}, "
      f"theory={p_joint_theory:.4f}")
```
