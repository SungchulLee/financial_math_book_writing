# First Passage Times

First passage times measure when Brownian motion first reaches a given level, with applications to barrier option pricing, credit default modeling, and optimal stopping.

## Definition

The **first passage time** (hitting time) to level $a$ for a standard Brownian motion is

$$
\tau_a = \inf\{t \geq 0 : W_t = a\}
$$

The density of $\tau_a$ is the **inverse Gaussian distribution**:

$$
f_{\tau_a}(t) = \frac{|a|}{\sqrt{2\pi t^3}}\,\exp\!\left(-\frac{a^2}{2t}\right), \quad t > 0
$$

The survival probability is $\mathbb{P}(\tau_a > t) = 2\Phi(-|a|/\sqrt{t})$, where $\Phi$ is the standard normal CDF.

## Explanation

The first passage time $\tau_a$ is a stopping time with respect to the natural filtration of Brownian motion. It is almost surely finite ($\mathbb{P}(\tau_a < \infty) = 1$) but has infinite expectation ($\mathbb{E}[\tau_a] = \infty$) for any $a \neq 0$.

The density is derived using the **reflection principle**: $\mathbb{P}(\max_{s \leq t} W_s \geq a) = 2\mathbb{P}(W_t \geq a)$ for $a > 0$. Differentiating with respect to $t$ yields the hitting time density.

For Brownian motion with drift $\mu$ (i.e., $X_t = \mu t + W_t$), the first passage time to level $a > 0$ has density

$$
f(t) = \frac{a}{\sqrt{2\pi t^3}}\,\exp\!\left(-\frac{(a - \mu t)^2}{2t}\right)
$$

This generalizes to barrier option pricing in the Black-Scholes model, where the log-price follows Brownian motion with drift.

## Examples

Simulate first passage times and compare with the theoretical distribution.

```python
import numpy as np
from scipy.stats import invgauss

a = 2.0  # target level
n_paths = 50000
dt = 0.001
T_max = 20.0
n_steps = int(T_max / dt)

# Simulate and record first passage times
np.random.seed(42)
tau_samples = []
for _ in range(n_paths):
    W = 0.0
    for k in range(1, n_steps + 1):
        W += np.sqrt(dt) * np.random.randn()
        if W >= a:
            tau_samples.append(k * dt)
            break

tau_samples = np.array(tau_samples)
print(f"P(tau < {T_max}) = {len(tau_samples)/n_paths:.4f}")
print(f"Median hitting time: {np.median(tau_samples):.4f}")

# Theoretical survival probability at t=5
from scipy.stats import norm
t_check = 5.0
surv_theory = 2 * norm.cdf(-a / np.sqrt(t_check))
surv_empirical = np.mean(tau_samples > t_check)
print(f"P(tau > {t_check}): theory={surv_theory:.4f}, sim={surv_empirical:.4f}")

# Theoretical density evaluation
t_vals = np.linspace(0.1, 10, 100)
f_theory = a / np.sqrt(2 * np.pi * t_vals**3) * np.exp(-a**2 / (2 * t_vals))
print(f"Peak density at t = {t_vals[np.argmax(f_theory)]:.2f}")
```
