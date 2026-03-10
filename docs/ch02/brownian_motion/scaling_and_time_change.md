# Scaling and Time Change

Brownian motion is self-similar with no intrinsic time scale, and the Dambis-Dubins-Schwarz theorem shows that every continuous local martingale is Brownian motion evaluated at a random clock.

## Definition

Brownian motion exhibits **self-similarity** of index $1/2$: for any $c > 0$,

$$
\{W_{ct}\}_{t \geq 0} \overset{d}{=} \{\sqrt{c}\, W_t\}_{t \geq 0}
$$

as processes. Equivalently, $\tilde{W}_t = c^{-1/2} W_{ct}$ is a standard Brownian motion. More generally, a **deterministic time change** via a continuous increasing function $\phi: [0,\infty) \to [0,\infty)$ with $\phi(0) = 0$ produces $X_t = W_{\phi(t)}$, which is a Gaussian process with $\operatorname{Cov}(X_s, X_t) = \phi(\min(s,t))$.

The **Dambis-Dubins-Schwarz theorem** states: if $M_t$ is a continuous local martingale with $\langle M \rangle_\infty = \infty$ a.s., then there exists a Brownian motion $B$ such that $M_t = B_{\langle M \rangle_t}$.

## Explanation

The self-similarity $dW_t \sim \sqrt{dt}$ (not $dt$) is the fundamental scaling of stochastic calculus. Zooming into a Brownian path by a time factor $c$ rescales space by $\sqrt{c}$, so paths look statistically identical at every resolution. This explains why Brownian motion has no characteristic time scale and is fractal with Hausdorff dimension 2.

The Dambis-Dubins-Schwarz theorem is profound: it says that the only source of randomness in continuous martingales is Brownian motion, run on a random clock given by the quadratic variation $\langle M \rangle_t$. This unifies all continuous local martingales under a single framework.

## Examples

Verify self-similarity and time-change properties numerically.

```python
import numpy as np
from scipy.stats import kstest, norm

np.random.seed(42)
n = 10000
dt = 0.001
T = 10.0
steps = int(T / dt)
dW = np.sqrt(dt) * np.random.randn(steps)
W = np.concatenate([[0], np.cumsum(dW)])
t = np.arange(steps + 1) * dt

# Self-similarity: W_{ct} =^d sqrt(c) W_t
c = 4.0
# Sample W at times ct
W_ct_samples = W[::int(c)][:1000]  # W at times c*dt, 2c*dt, ...
W_t_scaled = np.sqrt(c) * W[:len(W_ct_samples)]  # sqrt(c) * W_t

# Compare distributions at a fixed time
idx = 500
print(f"W_{{ct}}: mean={np.mean(W_ct_samples[:idx]):.3f}")
print(f"sqrt(c)*W_t: mean={np.mean(W_t_scaled[:idx]):.3f}")

# Deterministic time change: X_t = W_{t^2} should have Var = t^2
t_vals = np.array([0.5, 1.0, 2.0, 3.0])
n_mc = 50000
for tv in t_vals:
    phi_t = tv**2  # time change phi(t) = t^2
    X = np.sqrt(phi_t) * np.random.randn(n_mc)
    print(f"t={tv}: Var(W_{{t^2}}) = {np.var(X):.4f} "
          f"(expect {phi_t:.4f})")
```
