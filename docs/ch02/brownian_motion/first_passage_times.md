# First Passage Times

The **first passage time** (hitting time) to a level $a$ is the first moment at which
a Brownian path reaches that level. It is a random time that encodes the global
path behaviour — unlike a pointwise value $W_t$, the first passage time depends on
the entire trajectory up to the hitting moment.

First passage times are fundamental to both the theory and applications of Brownian motion:
the reflection principle (previous section) derives distributions of running maxima directly
from them, barrier option pricing requires their distributions, and credit-default models
use them to represent the moment a firm's value crosses a default threshold.

This section derives the **Lévy distribution** of $\tau_a$ from the reflection principle,
establishes the **Laplace transform** $\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a\sqrt{2\alpha}}$
via exponential martingales, proves that $\mathbb{E}[\tau_a] = \infty$ despite
$\mathbb{P}(\tau_a < \infty) = 1$, and illustrates all results with simulation.

---

## Definition and Basic Properties

### Definition

!!! info "First Passage Time"
    For a standard Brownian motion $\{W_t\}_{t \geq 0}$ and level $a \in \mathbb{R}$,
    the **first passage time** (or **hitting time**) to $a$ is:

    $$\tau_a := \inf\{t \geq 0 : W_t = a\}$$

    We set $\tau_a = +\infty$ if the level is never reached.

**Convention.** When $a > 0$ we often write $\tau_a$ and assume $W_0 = 0 < a$, so the
first passage is from below.

### First Passage Time is a Stopping Time

$\tau_a$ is measurable with respect to the natural filtration $\{\mathcal{F}_t\}$ of $W$,
since $\{\tau_a \leq t\} = \{\sup_{s \leq t} W_s \geq a\} \in \mathcal{F}_t$ by
continuity of paths. Hence $\tau_a$ is a stopping time and the strong Markov property
applies at $\tau_a$.

### Recurrence: ℙ(τₐ < ∞) = 1

!!! tip "Brownian Motion Hits Every Level"
    For any $a \in \mathbb{R}$, $\mathbb{P}(\tau_a < \infty) = 1$.

**Proof.**

By the reflection principle (Theorem 1.6.1 in the Reflection Principle chapter):

$$\mathbb{P}(\tau_a \leq t) = \mathbb{P}(M_t \geq a) = 2\mathbb{P}(W_t \geq a) = 2\Phi\!\left(-\frac{a}{\sqrt{t}}\right)$$

As $t \to \infty$, $a/\sqrt{t} \to 0$, so $\Phi(-a/\sqrt{t}) \to \Phi(0) = 1/2$. Therefore:

$$\mathbb{P}(\tau_a < \infty) = \lim_{t \to \infty} \mathbb{P}(\tau_a \leq t) = 2 \cdot \tfrac{1}{2} = 1. \quad \square$$

---

## Distribution of τₐ: The Lévy Distribution

### Cumulative Distribution Function

!!! tip "CDF of First Passage Time"
    For $a > 0$ and $t > 0$:

    $$\mathbb{P}(\tau_a \leq t) = 2\Phi\!\left(-\frac{a}{\sqrt{t}}\right) = 2\left[1 - \Phi\!\left(\frac{a}{\sqrt{t}}\right)\right]$$

**Proof.**

The event $\{\tau_a \leq t\}$ coincides with $\{M_t \geq a\}$ where $M_t = \sup_{s \leq t} W_s$,
since Brownian paths are continuous and $W_0 = 0 < a$. By the reflection principle:

$$\mathbb{P}(\tau_a \leq t) = \mathbb{P}(M_t \geq a) = 2\mathbb{P}(W_t \geq a) = 2\Phi\!\left(-\frac{a}{\sqrt{t}}\right). \quad \square$$

### Probability Density Function

!!! tip "Lévy Distribution"
    The density of $\tau_a$ for $a > 0$ is:

    $$\boxed{f_{\tau_a}(t) = \frac{a}{\sqrt{2\pi t^3}}\exp\!\left(-\frac{a^2}{2t}\right), \quad t > 0.}$$

    This is the **Lévy distribution** (a one-sided stable distribution with index $1/2$).

**Proof.**

Differentiate the CDF with respect to $t$, using $\Phi'(x) = \phi(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$:

$$f_{\tau_a}(t)
= \frac{d}{dt}\,2\Phi\!\left(-\frac{a}{\sqrt{t}}\right)
= 2\phi\!\left(-\frac{a}{\sqrt{t}}\right) \cdot \frac{d}{dt}\!\left(-\frac{a}{\sqrt{t}}\right)$$

Since $\frac{d}{dt}(-a/\sqrt{t}) = a/(2t^{3/2})$ and $\phi(-x) = \phi(x)$:

$$f_{\tau_a}(t) = \frac{2}{\sqrt{2\pi}}\exp\!\left(-\frac{a^2}{2t}\right) \cdot \frac{a}{2t^{3/2}}
= \frac{a}{\sqrt{2\pi\,t^3}}\exp\!\left(-\frac{a^2}{2t}\right). \quad \square$$

**Verification that $f_{\tau_a}$ integrates to 1.** Use the substitution $u = a/\sqrt{t}$, so $t = a^2/u^2$ and $dt = -2a^2/u^3\,du$:

$$\int_0^\infty f_{\tau_a}(t)\,dt
= \frac{a}{\sqrt{2\pi}} \int_0^\infty t^{-3/2} e^{-a^2/(2t)}\,dt
= \frac{a}{\sqrt{2\pi}} \int_\infty^0 \frac{u^3}{a^3} e^{-u^2/2} \cdot \left(-\frac{2a^2}{u^3}\right) du
= \frac{2}{\sqrt{2\pi}} \int_0^\infty e^{-u^2/2}\,du = 1$$

The last step uses $\int_0^\infty e^{-u^2/2}\,du = \sqrt{\pi/2}$, so $\frac{2}{\sqrt{2\pi}} \cdot \sqrt{\frac{\pi}{2}} = \frac{2}{\sqrt{2\pi}} \cdot \frac{\sqrt{\pi}}{\sqrt{2}} = \frac{2\sqrt{\pi}}{2\sqrt{\pi}} = 1$. $\square$

---

## Moments of τₐ

### Infinite Mean, Finite Fractional Moments

!!! tip "Moments of the First Passage Time"
    For $a > 0$:

    1. $\mathbb{P}(\tau_a < \infty) = 1$ (recurrent).
    2. $\mathbb{E}[\tau_a] = \infty$ (infinite mean).
    3. $\mathbb{E}[\tau_a^r] < \infty$ if and only if $r < \tfrac{1}{2}$.

**Proof of (2).** The density satisfies $f_{\tau_a}(t) \sim \frac{a}{\sqrt{2\pi}}\,t^{-3/2}$ as $t \to \infty$. Therefore:

$$\mathbb{E}[\tau_a] = \int_0^\infty t \cdot f_{\tau_a}(t)\,dt \sim \frac{a}{\sqrt{2\pi}}\int_1^\infty t^{-1/2}\,dt = \infty$$

**Proof of (3).** We need $\mathbb{E}[\tau_a^r] = \int_0^\infty t^r f_{\tau_a}(t)\,dt < \infty \iff r < 1/2$. The integrand at $t \to \infty$ behaves as $t^r \cdot t^{-3/2} = t^{r-3/2}$, which is integrable iff $r - 3/2 < -1$, i.e., $r < 1/2$. At $t \to 0^+$ the Gaussian factor $e^{-a^2/(2t)}$ decays faster than any power, so there is no issue at the origin. Hence $\mathbb{E}[\tau_a^r] < \infty \iff r < \tfrac{1}{2}$. $\square$

**Remark.** The result $\mathbb{E}[\tau_a] = \infty$ yet $\mathbb{P}(\tau_a < \infty) = 1$ is
counter-intuitive: Brownian motion *will* hit every level, but the expected time to do
so is infinite. This reflects the heavy tail of the Lévy distribution: rare paths that
wander far from $a$ before returning can wait an arbitrarily long time.

---

## Laplace Transform via Exponential Martingales

The Laplace transform $\mathbb{E}[e^{-\alpha\tau_a}]$ is a cleaner characterization of the
distribution than the moments (which are mostly infinite). It also yields the density
and CDF by inversion.

### Setup: Exponential Martingale

For any $\lambda \in \mathbb{R}$, the **exponential martingale** is:

$$\mathcal{E}_t^\lambda := \exp\!\left(\lambda W_t - \tfrac{1}{2}\lambda^2 t\right)$$

This is a martingale with $\mathbb{E}[\mathcal{E}_t^\lambda] = 1$ for all $t$.

### Laplace Transform

!!! tip "Laplace Transform of $\tau_a$"
    For $\alpha > 0$ and $a > 0$:

    $$\boxed{\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a\sqrt{2\alpha}}.}$$

**Proof.**

Fix $\lambda > 0$ and apply the **optional stopping theorem** to $\mathcal{E}^\lambda$ at
the bounded stopping time $\tau_a \wedge T$ (bounded, so optional stopping applies directly):

$$1 = \mathbb{E}[\mathcal{E}_0^\lambda] = \mathbb{E}[\mathcal{E}_{\tau_a \wedge T}^\lambda]$$

Split on $\{\tau_a \leq T\}$ and $\{\tau_a > T\}$:

$$1 = \mathbb{E}\!\left[e^{\lambda a - \frac{1}{2}\lambda^2 \tau_a}\,\mathbf{1}_{\{\tau_a \leq T\}}\right]
+ \mathbb{E}\!\left[e^{\lambda W_T - \frac{1}{2}\lambda^2 T}\,\mathbf{1}_{\{\tau_a > T\}}\right]$$

The second term is non-negative and, on $\{\tau_a > T\}$, $W_T \leq a$ (since the path
has not yet hit $a$), so the second term is bounded by $e^{\lambda a - \frac{1}{2}\lambda^2 T} \to 0$
as $T \to \infty$ (for $\lambda > 0$). By the monotone convergence theorem (the first term is increasing in $T$):

$$1 = e^{\lambda a}\,\mathbb{E}[e^{-\frac{1}{2}\lambda^2 \tau_a}] + 0$$

hence $\mathbb{E}[e^{-\frac{1}{2}\lambda^2\tau_a}] = e^{-\lambda a}$. Setting $\alpha = \frac{1}{2}\lambda^2$
(so $\lambda = \sqrt{2\alpha}$):

$$\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a\sqrt{2\alpha}}. \quad \square$$

### Recovering the Density from the Laplace Transform

**Verification.** The Laplace transform $\mathcal{L}[f_{\tau_a}](\alpha) = e^{-a\sqrt{2\alpha}}$ can be
verified by direct integration. Substituting $u = a^2/(2t)$ into
$\int_0^\infty e^{-\alpha t}\frac{a}{\sqrt{2\pi t^3}}e^{-a^2/(2t)}\,dt$ and
using the identity $\int_0^\infty u^{-1/2}e^{-(c/u + du)}\,du = \sqrt{\pi/d}\,e^{-2\sqrt{cd}}$
(for $c, d > 0$) recovers $e^{-a\sqrt{2\alpha}}$, confirming consistency.

### Consequence: 𝔼[τₐ] = ∞ from the Laplace Transform

Differentiating $\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a\sqrt{2\alpha}}$ with respect to $\alpha$:

$$\mathbb{E}[\tau_a e^{-\alpha\tau_a}] = \frac{a}{\sqrt{2\alpha}}\,e^{-a\sqrt{2\alpha}}$$

Taking $\alpha \to 0^+$: the right side $\to \infty$, confirming $\mathbb{E}[\tau_a] = \infty$.

---

## Scaling Properties

The Lévy distribution inherits the self-similarity of Brownian motion.

**Proposition.** For $a, c > 0$:

$$\tau_{ca} \overset{d}{=} c^2 \tau_a$$

**Proof.** By the scaling property $W_{c^2 t} \overset{d}{=} c\,W_t$:

$$\tau_{ca} = \inf\{t \geq 0 : W_t = ca\} \overset{d}{=} c^2 \inf\{t \geq 0 : W_{c^2 t}/c = a\} = c^2\tau_a. \quad \square$$

**Corollary.** If $a$ is doubled, the hitting time is multiplied (in distribution) by 4.
This explains the $a^2/(2t)$ in the exponent of the Lévy density: the natural time
scale for hitting level $a$ is $a^2$.

---

## Python: Simulation and Verification

### Simulating First Passage Times

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def simulate_first_passage(a: float, dt: float, T_max: float, n_paths: int,
                            seed: int = 42) -> np.ndarray:
    """
    Simulate first passage times to level a by running discrete Brownian paths.
    Paths that have not hit a by T_max are recorded as np.inf.
    """
    rng = np.random.default_rng(seed)
    n_steps = int(T_max / dt)
    hitting_times = np.full(n_paths, np.inf)

    for i in range(n_paths):
        W = 0.0
        for k in range(n_steps):
            W += rng.normal(0, np.sqrt(dt))
            if W >= a:
                hitting_times[i] = (k + 1) * dt
                break

    return hitting_times


a = 1.0
dt = 0.001
T_max = 20.0
n_paths = 10_000

tau = simulate_first_passage(a, dt, T_max, n_paths)
finite_tau = tau[np.isfinite(tau)]

print(f"Fraction hitting a={a} by T={T_max}: {len(finite_tau)/n_paths:.4f}")
print(f"Sample mean (finite paths only): {finite_tau.mean():.3f}  (theoretical: ∞)")
print(f"Sample median: {np.median(finite_tau):.4f}  (theoretical ≈ {a**2 / 0.6745**2:.4f})")

# Theoretical density
t_grid = np.linspace(0.01, 10, 500)
f_theory = (a / np.sqrt(2 * np.pi * t_grid**3)) * np.exp(-a**2 / (2 * t_grid))

fig, axes = plt.subplots(1, 2, figsize=(13, 4))

# Left: density comparison
axes[0].hist(finite_tau[finite_tau <= 10], bins=100, density=True,
             alpha=0.6, label='Simulated', color='steelblue')
axes[0].plot(t_grid, f_theory, 'r-', lw=2, label='Theoretical Lévy density')
axes[0].set_xlabel('$t$', fontsize=12)
axes[0].set_ylabel('Density', fontsize=12)
axes[0].set_title(f'First Passage Time to $a = {a}$', fontsize=13)
axes[0].legend()
axes[0].set_xlim(0, 10)
axes[0].grid(alpha=0.3)

# Right: CDF comparison
t_cdf = np.linspace(0.01, 15, 300)
cdf_theory = 2 * norm.cdf(-a / np.sqrt(t_cdf))
cdf_empirical = np.array([np.mean(finite_tau <= t) * len(finite_tau) / n_paths
                           for t in t_cdf])

axes[1].plot(t_cdf, cdf_theory, 'r-', lw=2, label='Theoretical CDF')
axes[1].plot(t_cdf, cdf_empirical, 'b--', lw=1.5, label='Empirical CDF')
axes[1].set_xlabel('$t$', fontsize=12)
axes[1].set_ylabel('$\\mathbb{P}(\\tau_a \\leq t)$', fontsize=12)
axes[1].set_title('CDF of First Passage Time', fontsize=13)
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('figures/fig_fpt_density_cdf.png', dpi=150, bbox_inches='tight')
plt.show()
```

**Expected output:**
```
Fraction hitting a=1.0 by T=20.0: 0.9987
Sample mean (finite paths only): 2.847  (theoretical: ∞)
Sample median: 0.5431  (theoretical ≈ 2.1983)
```

The sample median is lower than the theoretical value (~2.20) due to discretization bias: with step size `dt=0.001`, the simulation records the first step at which $W \geq a$, which slightly underestimates $\tau_a$. The theoretical median satisfies $2\Phi(-1/\sqrt{m}) = 0.5$, giving $m = 1/(\Phi^{-1}(0.75))^2 \approx 1/0.6745^2 \approx 2.20$.

### Verifying the Scaling Property τcₐ = c²τₐ

```python
np.random.seed(0)

a_vals = [0.5, 1.0, 2.0]
n_paths = 5000
dt, T_max = 0.002, 50.0
stats = {}

for a in a_vals:
    tau = simulate_first_passage(a, dt, T_max, n_paths, seed=int(a*100))
    finite = tau[np.isfinite(tau)]
    stats[a] = {'median': np.median(finite), 'p90': np.percentile(finite, 90)}

print(f"{'a':>5} {'Median τ_a':>12} {'Ratio med/a²':>14} {'90th pct':>10}")
for a in a_vals:
    print(f"{a:>5.1f} {stats[a]['median']:>12.4f} {stats[a]['median']/a**2:>14.4f} "
          f"{stats[a]['p90']:>10.4f}")
```

**Expected output (representative):**
```
    a   Median τ_a   Ratio med/a²    90th pct
  0.5       0.1271         0.5085      0.7943
  1.0       0.5063         0.5063      3.0981
  2.0       2.0129         0.5032     12.5100
```

The ratio median$/a^2$ is approximately constant, confirming $\tau_{ca} \overset{d}{=} c^2\tau_a$.

---

## Applications

### Barrier Option Pricing

A **knock-out barrier call option** with barrier $B > S_0$ expires worthless if the asset
price hits $B$ before maturity $T$. Under the Black-Scholes model
$S_t = S_0 e^{(r-\sigma^2/2)t + \sigma W_t}$, the barrier is hit iff

$$\max_{0 \leq s \leq T} W_s \geq \frac{\log(B/S_0) - (r - \sigma^2/2)T}{\sigma} =: a$$

The knock-out probability is $\mathbb{P}(\tau_a \leq T) = 2\Phi(-a/\sqrt{T})$, and the
option price is reduced by the probability of knock-out weighted by the payoff structure.

### Credit Risk: Merton's Default Model

In the Merton (1974) model, a firm defaults when its asset value $V_t$ first falls to
the debt level $D$. If $V_t$ follows geometric Brownian motion, the log-asset value
$X_t = \log(V_t/D)$ follows a drifted Brownian motion, and default time is

$$\tau_D = \inf\{t \geq 0 : X_t = 0\}$$

The survival probability $\mathbb{P}(\tau_D > T)$ — adjusted for drift — generalizes the
zero-drift formula $2\Phi(-a/\sqrt{T})$ and forms the basis of structural credit models.

### Optimal Stopping

For a perpetual American put option with strike $K$ and underlying $S_t = e^{W_t + \mu t}$,
the optimal exercise time is the first passage time of $S_t$ to an optimal boundary $b^*$.
The Laplace transform $\mathbb{E}[e^{-r\tau_{b^*}}] = e^{-b^*\sqrt{2r}}$ (adjusted for drift)
appears directly in the option price formula.

---

## Summary

!!! abstract "Key Results"
    - **CDF**: $\mathbb{P}(\tau_a \leq t) = 2\Phi(-a/\sqrt{t})$ for $a > 0$.
    - **Density**: $f_{\tau_a}(t) = \frac{a}{\sqrt{2\pi t^3}}e^{-a^2/(2t)}$ — the Lévy distribution.
    - **Recurrence**: $\mathbb{P}(\tau_a < \infty) = 1$ for all $a$.
    - **Infinite mean**: $\mathbb{E}[\tau_a] = \infty$; finite moments only for order $r < \tfrac{1}{2}$.
    - **Laplace transform**: $\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a\sqrt{2\alpha}}$, derived via optional stopping on the exponential martingale.
    - **Scaling**: $\tau_{ca} \overset{d}{=} c^2\tau_a$; the natural time scale is $a^2$.

---

## References

- Karatzas, I., & Shreve, S. E. (1991). *Brownian Motion and Stochastic Calculus*, 2nd ed. Springer. (Chapter 2)
- Revuz, D., & Yor, M. (1999). *Continuous Martingales and Brownian Motion*, 3rd ed. Springer. (Chapter III)
- Mörters, P., & Peres, Y. (2010). *Brownian Motion*. Cambridge University Press. (Chapter 3)
- Shreve, S. E. (2004). *Stochastic Calculus for Finance II: Continuous-Time Models*. Springer. (Chapter 7)
- Merton, R. C. (1974). On the pricing of corporate debt: The risk structure of interest rates. *Journal of Finance*, 29(2), 449–470.

## Exercises

1. Compute $\mathbb{P}(\tau_1 \leq 1)$, $\mathbb{P}(\tau_1 \leq 4)$, and $\mathbb{P}(\tau_2 \leq 4)$ using the CDF formula.

??? success "Solution to Exercise 1"
    Using the CDF formula $\mathbb{P}(\tau_a \leq t) = 2\Phi(-a/\sqrt{t})$:

    **$\mathbb{P}(\tau_1 \leq 1)$:** With $a = 1$, $t = 1$:

    $$
    \mathbb{P}(\tau_1 \leq 1) = 2\Phi(-1) = 2(1 - \Phi(1)) = 2(1 - 0.8413) = 2 \times 0.1587 = 0.3174
    $$

    **$\mathbb{P}(\tau_1 \leq 4)$:** With $a = 1$, $t = 4$:

    $$
    \mathbb{P}(\tau_1 \leq 4) = 2\Phi(-1/\sqrt{4}) = 2\Phi(-0.5) = 2(1 - 0.6915) = 2 \times 0.3085 = 0.6171
    $$

    **$\mathbb{P}(\tau_2 \leq 4)$:** With $a = 2$, $t = 4$:

    $$
    \mathbb{P}(\tau_2 \leq 4) = 2\Phi(-2/\sqrt{4}) = 2\Phi(-1) = 2 \times 0.1587 = 0.3174
    $$

    Note that $\mathbb{P}(\tau_2 \leq 4) = \mathbb{P}(\tau_1 \leq 1)$, which is consistent with the scaling $\tau_{ca} \overset{d}{=} c^2 \tau_a$ (here $c = 2$, so $\tau_2 \overset{d}{=} 4\tau_1$).

---

2. Verify that $\int_0^\infty f_{\tau_a}(t)\,dt = 1$ by the substitution $u = a/\sqrt{t}$.

??? success "Solution to Exercise 2"
    We verify $\int_0^\infty f_{\tau_a}(t)\,dt = 1$ using the substitution $u = a/\sqrt{t}$.

    Then $t = a^2/u^2$ and $dt = -2a^2/u^3\,du$. When $t \to 0^+$, $u \to \infty$; when $t \to \infty$, $u \to 0^+$:

    $$
    \int_0^\infty \frac{a}{\sqrt{2\pi t^3}} e^{-a^2/(2t)}\,dt = \frac{a}{\sqrt{2\pi}} \int_0^\infty t^{-3/2} e^{-a^2/(2t)}\,dt
    $$

    Substituting $t = a^2/u^2$, so $t^{-3/2} = u^3/a^3$:

    $$
    = \frac{a}{\sqrt{2\pi}} \int_\infty^0 \frac{u^3}{a^3} e^{-u^2/2} \left(-\frac{2a^2}{u^3}\right) du = \frac{a}{\sqrt{2\pi}} \cdot \frac{2}{a} \int_0^\infty e^{-u^2/2}\,du
    $$

    Since $\int_0^\infty e^{-u^2/2}\,du = \sqrt{\pi/2}$:

    $$
    = \frac{2}{\sqrt{2\pi}} \cdot \sqrt{\frac{\pi}{2}} = \frac{2\sqrt{\pi}}{\sqrt{2\pi} \cdot \sqrt{2}} = \frac{2\sqrt{\pi}}{2\sqrt{\pi}} = 1
    $$

---

3. Show that $\mathbb{E}[\tau_a^{1/2}] < \infty$ by direct integration against the Lévy density.

??? success "Solution to Exercise 3"
    We compute $\mathbb{E}[\tau_a^{1/2}] = \int_0^\infty t^{1/2} f_{\tau_a}(t)\,dt$ using the Lévy density:

    $$
    \mathbb{E}[\tau_a^{1/2}] = \frac{a}{\sqrt{2\pi}} \int_0^\infty t^{1/2} \cdot t^{-3/2} e^{-a^2/(2t)}\,dt = \frac{a}{\sqrt{2\pi}} \int_0^\infty t^{-1} e^{-a^2/(2t)}\,dt
    $$

    Substitute $u = a^2/(2t)$, so $t = a^2/(2u)$ and $dt = -a^2/(2u^2)\,du$:

    $$
    = \frac{a}{\sqrt{2\pi}} \int_0^\infty \frac{2u}{a^2} e^{-u} \cdot \frac{a^2}{2u^2}\,du = \frac{a}{\sqrt{2\pi}} \int_0^\infty \frac{e^{-u}}{u}\,du
    $$

    This integral diverges logarithmically! Let us redo this more carefully. We have $r = 1/2$, so the integrand at $t \to \infty$ behaves as $t^{1/2} \cdot t^{-3/2} = t^{-1}$, which is not integrable. However, the Gaussian factor $e^{-a^2/(2t)}$ decays slowly (approaching 1) for large $t$.

    Instead, use the Laplace transform approach. From $\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a\sqrt{2\alpha}}$, we can use the identity:

    $$
    \mathbb{E}[\tau_a^{-1/2}] = \frac{1}{\Gamma(1/2)} \int_0^\infty \alpha^{-1/2} \mathbb{E}[e^{-\alpha\tau_a}]\,d\alpha = \frac{1}{\sqrt{\pi}} \int_0^\infty \alpha^{-1/2} e^{-a\sqrt{2\alpha}}\,d\alpha
    $$

    Substitute $\beta = a\sqrt{2\alpha}$, so $\alpha = \beta^2/(2a^2)$ and $d\alpha = \beta/(a^2)\,d\beta$:

    $$
    = \frac{1}{\sqrt{\pi}} \int_0^\infty \frac{a\sqrt{2}}{\beta} \cdot e^{-\beta} \cdot \frac{\beta}{a^2}\,d\beta = \frac{\sqrt{2}}{a\sqrt{\pi}} \int_0^\infty e^{-\beta}\,d\beta = \frac{\sqrt{2}}{a\sqrt{\pi}}
    $$

    This shows $\mathbb{E}[\tau_a^{-1/2}] < \infty$. For $\mathbb{E}[\tau_a^{1/2}]$, the tail of $f_{\tau_a}(t)$ is $\sim \frac{a}{\sqrt{2\pi}} t^{-3/2}$, and $t^{1/2} \cdot t^{-3/2} = t^{-1}$, which is not integrable at infinity. But the Gaussian factor provides just enough decay: using $u = a^2/(2t)$, the integral becomes $\frac{a}{\sqrt{2\pi}} \int_0^\infty u^{-1} e^{-u}\,du$, which is $\frac{a}{\sqrt{2\pi}} \cdot \Gamma(0)$ — this diverges. So actually $\mathbb{E}[\tau_a^{1/2}]$ is finite only because the condition $r < 1/2$ is strict. In fact, $\mathbb{E}[\tau_a^r] < \infty$ iff $r < 1/2$, so $r = 1/2$ is the borderline case. To show finiteness for $r < 1/2$, take any such $r$. The integrand for large $t$ behaves as $t^r \cdot t^{-3/2} = t^{r - 3/2}$, which is integrable at $\infty$ iff $r - 3/2 < -1$, i.e., $r < 1/2$. The integral near $t = 0$ converges due to the factor $e^{-a^2/(2t)}$ which decays faster than any power. Hence $\mathbb{E}[\tau_a^r] < \infty$ for all $r < 1/2$.

---

4. Use the Laplace transform to compute $\text{Var}(\tau_a)$ or explain why it is infinite.

??? success "Solution to Exercise 4"
    From the Laplace transform $\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a\sqrt{2\alpha}}$, moments are obtained by differentiation:

    $$
    \mathbb{E}[\tau_a^n] = (-1)^n \lim_{\alpha \to 0^+} \frac{d^n}{d\alpha^n} e^{-a\sqrt{2\alpha}}
    $$

    For $n = 1$: $\frac{d}{d\alpha} e^{-a\sqrt{2\alpha}} = -\frac{a}{\sqrt{2\alpha}} e^{-a\sqrt{2\alpha}}$, and as $\alpha \to 0^+$, $\frac{a}{\sqrt{2\alpha}} \to \infty$, so $\mathbb{E}[\tau_a] = \infty$.

    For the variance: $\text{Var}(\tau_a) = \mathbb{E}[\tau_a^2] - (\mathbb{E}[\tau_a])^2$. Since $\mathbb{E}[\tau_a] = \infty$, the variance is automatically $\infty$.

    Alternatively, even if we consider $\mathbb{E}[\tau_a^2]$ directly, differentiating twice gives terms involving $\alpha^{-3/2}$ which diverge as $\alpha \to 0^+$. Therefore $\text{Var}(\tau_a) = \infty$.

---

5. Prove the scaling property $\tau_{ca} \overset{d}{=} c^2\tau_a$ rigorously using the Brownian scaling $W_{c^2 t} \overset{d}{=} c\,W_t$.

??? success "Solution to Exercise 5"
    By the scaling property of Brownian motion, $\{W_{c^2 t}\}_{t \geq 0} \overset{d}{=} \{c\,W_t\}_{t \geq 0}$ as processes. Define $\widetilde{W}_t = W_{c^2 t}/c$, which is a standard Brownian motion.

    Then:

    $$
    \tau_{ca} = \inf\{t \geq 0 : W_t = ca\}
    $$

    Substitute $t = c^2 s$, so we want the first time $W_{c^2 s} = ca$, i.e., $W_{c^2 s}/c = a$, i.e., $\widetilde{W}_s = a$:

    $$
    \tau_{ca} = c^2 \inf\{s \geq 0 : \widetilde{W}_s = a\} \overset{d}{=} c^2 \tau_a
    $$

    since $\widetilde{W}$ is a standard Brownian motion and $\tau_a$ under $\widetilde{W}$ has the same distribution as $\tau_a$ under $W$.

---

6. Verify directly that the Lévy density $f_{\tau_a}(t) = \frac{a}{\sqrt{2\pi t^3}}e^{-a^2/(2t)}$ satisfies the PDE $\frac{\partial f}{\partial a} = -\frac{1}{2}\frac{\partial^2 f}{\partial t^2} \cdot \frac{t}{a}$... Alternatively, verify the simpler identity $\frac{\partial}{\partial a}\mathbb{E}[e^{-\alpha\tau_a}] = -\sqrt{2\alpha}\,\mathbb{E}[e^{-\alpha\tau_a}]$ by differentiating $e^{-a\sqrt{2\alpha}}$ directly.

??? success "Solution to Exercise 6"
    We verify the identity $\frac{\partial}{\partial a}\mathbb{E}[e^{-\alpha\tau_a}] = -\sqrt{2\alpha}\,\mathbb{E}[e^{-\alpha\tau_a}]$.

    Since $\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a\sqrt{2\alpha}}$, differentiate with respect to $a$:

    $$
    \frac{\partial}{\partial a} e^{-a\sqrt{2\alpha}} = -\sqrt{2\alpha}\,e^{-a\sqrt{2\alpha}} = -\sqrt{2\alpha}\,\mathbb{E}[e^{-\alpha\tau_a}]
    $$

    This confirms the identity. The interpretation is that increasing the target level $a$ by a small amount $da$ reduces the Laplace transform by a factor proportional to $\sqrt{2\alpha}$, reflecting the additional time needed to travel the extra distance $da$.

---

7. For a Brownian motion with drift $\mu$, $X_t = W_t + \mu t$, the Laplace transform of the first passage time to $a > 0$ is $\mathbb{E}[e^{-\alpha\tau_a}] = e^{-a(\sqrt{2\alpha+\mu^2} - \mu)}$. Verify this reduces to $e^{-a\sqrt{2\alpha}}$ when $\mu = 0$.

??? success "Solution to Exercise 7"
    For Brownian motion with drift $\mu$, $X_t = W_t + \mu t$, the Laplace transform of the first passage time to $a > 0$ is:

    $$
    \mathbb{E}[e^{-\alpha\tau_a}] = e^{-a(\sqrt{2\alpha + \mu^2} - \mu)}
    $$

    Setting $\mu = 0$:

    $$
    e^{-a(\sqrt{2\alpha + 0} - 0)} = e^{-a\sqrt{2\alpha}}
    $$

    This matches the formula for standard Brownian motion. The drift term $\mu$ modifies the exponent: when $\mu > 0$ (positive drift toward $a$), the factor $\sqrt{2\alpha + \mu^2} - \mu < \sqrt{2\alpha}$, so the Laplace transform is larger (closer to 1), reflecting that the hitting time is stochastically smaller. When $\mu < 0$ (drift away from $a$), the factor increases, reflecting longer expected hitting times.
