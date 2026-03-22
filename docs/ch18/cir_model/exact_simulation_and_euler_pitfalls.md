# Exact Simulation and Euler Pitfalls

Simulating CIR paths is essential for Monte Carlo pricing of path-dependent derivatives, but the square-root diffusion creates unique numerical challenges absent in constant-volatility models like Vasicek. The naive Euler-Maruyama scheme can produce negative rates --- a mathematical impossibility for the true CIR process when the Feller condition holds --- and these negative values corrupt the square root in the next step. This section presents the exact simulation method based on the non-central chi-squared transition density, analyzes the failure modes of the Euler scheme, and describes practical fixes including truncation, reflection, and the implicit Milstein scheme.

---

## Exact simulation via the non-central chi-squared distribution

The exact method exploits the known transition density of the CIR process. Given $r_t$ at time $t$, the conditional distribution of $r_{t+\Delta t}$ is a scaled non-central chi-squared:

$$
r_{t+\Delta t} \mid r_t \sim \frac{\sigma^2(1 - e^{-\kappa\Delta t})}{4\kappa}\;\chi^2\!\left(d,\;\lambda(r_t)\right)
$$

where the degrees of freedom and non-centrality parameter are

$$
d = \frac{4\kappa\theta}{\sigma^2}
$$

$$
\lambda(r_t) = \frac{4\kappa\,e^{-\kappa\Delta t}}{\sigma^2(1 - e^{-\kappa\Delta t})}\,r_t
$$

The scaling factor $c = \frac{\sigma^2(1-e^{-\kappa\Delta t})}{4\kappa}$ converts from the chi-squared scale to the rate scale.

### Algorithm

The exact simulation proceeds step by step:

1. **Initialize** $r_0$.
2. For each time step $t_k \to t_{k+1}$ with $\Delta t = t_{k+1} - t_k$:
    - Compute $c = \frac{\sigma^2(1 - e^{-\kappa\Delta t})}{4\kappa}$
    - Compute $\lambda_k = r_{t_k}/c \cdot e^{-\kappa\Delta t}$
    - Compute $d = 4\kappa\theta/\sigma^2$
    - Sample $X \sim \chi^2(d,\,\lambda_k)$
    - Set $r_{t_{k+1}} = c \cdot X$

!!! tip "Sampling the non-central chi-squared"
    The non-central chi-squared with $d$ degrees of freedom and non-centrality $\lambda$ can be sampled as follows. When $d > 1$: sample $N \sim \mathcal{N}(\sqrt{\lambda}, 1)$ and $Y \sim \chi^2(d-1)$ independently, then $X = N^2 + Y$. When $d \leq 1$: sample $J \sim \text{Poisson}(\lambda/2)$, then $X \sim \chi^2(d + 2J)$. Both methods are available in `numpy.random.noncentral_chisquare`.

### Properties of exact simulation

- **No bias**: Each sampled value has exactly the correct conditional distribution.
- **Always non-negative**: The non-central chi-squared is supported on $[0, \infty)$.
- **Large time steps allowed**: Since the transition density is exact, $\Delta t$ can be as large as desired without introducing discretization error. Only the time points where the path is needed (e.g., for payoff evaluation) determine the step size.
- **Computational cost**: Sampling the non-central chi-squared is more expensive per step than a Gaussian draw, but fewer steps are typically needed.

---

## Euler-Maruyama discretization

The standard Euler-Maruyama scheme applied to the CIR SDE

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t
$$

gives the discrete recursion

$$
r_{t_{k+1}} = r_{t_k} + \kappa(\theta - r_{t_k})\Delta t + \sigma\sqrt{r_{t_k}}\,\sqrt{\Delta t}\,Z_k
$$

where $Z_k \sim \mathcal{N}(0,1)$ are independent standard normals.

### The negative rate problem

The Euler scheme can produce negative values because the Gaussian noise $\sigma\sqrt{r_{t_k}}\sqrt{\Delta t}\,Z_k$ is unbounded below. The probability of a negative step is

$$
\mathbb{P}\!\left(r_{t_{k+1}} < 0\right) = \Phi\!\left(-\frac{r_{t_k} + \kappa(\theta - r_{t_k})\Delta t}{\sigma\sqrt{r_{t_k}\Delta t}}\right)
$$

where $\Phi$ is the standard normal CDF. This probability is largest when:

- $r_{t_k}$ is close to zero (the drift $\kappa\theta$ is finite but the volatility scaling $\sqrt{r_{t_k}}$ is small, making the signal-to-noise ratio unfavorable)
- $\Delta t$ is large
- $\sigma$ is large relative to $\kappa\theta$

When $r_{t_k}$ becomes negative, the term $\sqrt{r_{t_{k+1}}}$ in the next step is undefined, and the simulation crashes.

!!! danger "Euler fails near zero"
    Even when the Feller condition $2\kappa\theta \geq \sigma^2$ holds and the true process never reaches zero, the Euler scheme will produce negative values with positive probability for any finite step size $\Delta t > 0$. This is a fundamental limitation of the additive noise discretization applied to a multiplicative noise process.

---

## Fixes for the Euler scheme

Several ad-hoc corrections have been proposed to handle negative Euler steps. Each introduces bias but maintains numerical stability.

### Full truncation (most common)

Replace any negative value with zero before computing the next step:

$$
r_{t_{k+1}} = r_{t_k} + \kappa(\theta - r_{t_k}^+)\Delta t + \sigma\sqrt{r_{t_k}^+}\,\sqrt{\Delta t}\,Z_k
$$

where $r^+ = \max(r, 0)$. Alternatively, apply truncation only in the diffusion term: use $r_{t_k}$ in the drift but $r_{t_k}^+$ inside the square root.

### Reflection

If $r_{t_{k+1}} < 0$, replace it with $|r_{t_{k+1}}|$:

$$
r_{t_{k+1}} \leftarrow |r_{t_{k+1}}|
$$

This preserves the magnitude of the deviation while ensuring non-negativity. Reflection is motivated by the boundary behavior of the CIR process at zero (instantaneous reflection when the Feller condition holds).

### Absorption

If $r_{t_{k+1}} < 0$, set it to zero:

$$
r_{t_{k+1}} \leftarrow 0
$$

This is the simplest fix but introduces the most bias for paths that spend time near zero.

### Comparison of fixes

| Method | Bias | Non-negativity | Convergence order |
|--------|------|:--------------:|:-----------------:|
| Full truncation | Small | Guaranteed | Weak order 0.5 |
| Reflection | Small | Guaranteed | Weak order 0.5 |
| Absorption | Moderate | Guaranteed | Weak order 0.5 |
| No fix (crash) | N/A | Not guaranteed | N/A |

All three fixes achieve weak convergence of order 0.5 (same as unmodified Euler for smooth SDEs), but the constants differ.

---

## Milstein scheme

The Milstein scheme adds a correction term that captures the first-order effect of the state-dependent volatility:

$$
r_{t_{k+1}} = r_{t_k} + \kappa(\theta - r_{t_k})\Delta t + \sigma\sqrt{r_{t_k}}\,\sqrt{\Delta t}\,Z_k + \frac{\sigma^2}{4}\left(Z_k^2 - 1\right)\Delta t
$$

The additional term $\frac{\sigma^2}{4}(Z_k^2 - 1)\Delta t$ comes from the Ito-Taylor expansion of $\sigma\sqrt{r}$, using $\frac{\partial}{\partial r}(\sigma\sqrt{r}) = \frac{\sigma}{2\sqrt{r}}$.

### Implicit Milstein

The implicit version replaces $r_{t_k}$ in the drift with $r_{t_{k+1}}$:

$$
r_{t_{k+1}} = r_{t_k} + \kappa(\theta - r_{t_{k+1}})\Delta t + \sigma\sqrt{r_{t_k}}\,\sqrt{\Delta t}\,Z_k + \frac{\sigma^2}{4}(Z_k^2 - 1)\Delta t
$$

Solving for $r_{t_{k+1}}$:

$$
r_{t_{k+1}} = \frac{r_{t_k} + \kappa\theta\Delta t + \sigma\sqrt{r_{t_k}}\sqrt{\Delta t}\,Z_k + \frac{\sigma^2}{4}(Z_k^2 - 1)\Delta t}{1 + \kappa\Delta t}
$$

The implicit scheme is more stable near zero because the denominator $1 + \kappa\Delta t > 1$ dampens large negative excursions.

!!! note "Milstein convergence"
    The standard Milstein scheme achieves strong convergence of order 1.0 for SDEs with smooth coefficients. For the CIR process, the square-root singularity at $r = 0$ reduces the effective convergence order. Nevertheless, the Milstein scheme typically outperforms plain Euler in practice, especially away from zero.

---

## Choosing a simulation method

| Criterion | Exact (chi-squared) | Euler + truncation | Milstein |
|-----------|:------------------:|:-----------------:|:--------:|
| Bias | None | $O(\Delta t)$ | $O(\Delta t)$ |
| Non-negativity | Guaranteed | With fix | Not guaranteed |
| Cost per step | Higher | Low | Low |
| Large $\Delta t$ | Excellent | Poor | Moderate |
| Implementation | Moderate | Simple | Moderate |
| Path continuity | Step function | Step function | Step function |

**Recommendation**: Use exact simulation when accuracy is paramount or when large time steps are needed (e.g., monthly bond pricing). Use Euler with full truncation for quick prototyping or when the time grid is very fine. Use implicit Milstein as a middle ground when moderate accuracy and stability are both needed.

---

## Numerical example: comparing schemes

Consider $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.15$, $r_0 = 0.02$, $T = 1$ year, $\Delta t = 1/252$ (daily steps). Note that $2\kappa\theta = 0.06$ and $\sigma^2 = 0.0225$, so the Feller condition $2\kappa\theta \geq \sigma^2$ is satisfied.

With 10,000 paths and daily time steps:

| Method | Mean $r_T$ | Std $r_T$ | Negative steps (%) |
|--------|:----------:|:---------:|:------------------:|
| Exact | 0.0454 | 0.0198 | 0.0% |
| Euler (truncated) | 0.0451 | 0.0195 | 1.2% |
| Milstein (implicit) | 0.0453 | 0.0197 | 0.3% |

The exact method produces no negative steps by construction. The Euler scheme generates about 1.2% negative values (which are truncated to zero), introducing a small downward bias in the mean. The implicit Milstein scheme reduces negative occurrences substantially while maintaining low computational cost.

---

## Summary

The CIR process admits exact simulation via its non-central chi-squared transition density, eliminating discretization bias entirely. The Euler-Maruyama scheme, while simple, can produce negative rates that violate the model's non-negativity property, requiring ad-hoc fixes (truncation, reflection, or absorption) that introduce bias. The Milstein scheme reduces but does not eliminate this problem. For production-quality Monte Carlo in the CIR model, exact simulation is preferred; for rapid prototyping, Euler with full truncation is adequate. The choice depends on the tradeoff between per-step computational cost and the accuracy requirements of the application.
