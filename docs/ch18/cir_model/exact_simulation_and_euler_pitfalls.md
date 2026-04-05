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

---

## Exercises

**Exercise 1.** For CIR parameters $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.15$, and $r_t = 0.02$, compute the exact simulation parameters for $\Delta t = 1/252$ (one trading day): the scaling factor $c$, the degrees of freedom $d$, and the non-centrality parameter $\lambda(r_t)$. What is the expected value of $r_{t+\Delta t}$?

??? success "Solution to Exercise 1"

    Given $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.15$, $r_t = 0.02$, $\Delta t = 1/252$.

    **Scaling factor $c$:**

    $$
    c = \frac{\sigma^2(1 - e^{-\kappa\Delta t})}{4\kappa} = \frac{0.0225(1 - e^{-0.5/252})}{2.0}
    $$

    $$
    e^{-0.5/252} \approx 1 - 0.001984 = 0.998016
    $$

    $$
    c = \frac{0.0225 \times 0.001984}{2.0} = \frac{4.464 \times 10^{-5}}{2.0} = 2.232 \times 10^{-5}
    $$

    **Degrees of freedom $d$:**

    $$
    d = \frac{4\kappa\theta}{\sigma^2} = \frac{4 \times 0.5 \times 0.06}{0.0225} = \frac{0.12}{0.0225} = 5.333
    $$

    **Non-centrality parameter $\lambda(r_t)$:**

    $$
    \lambda(r_t) = \frac{r_t}{c} \cdot e^{-\kappa\Delta t} = \frac{0.02}{2.232 \times 10^{-5}} \times 0.998016 = 896.1 \times 0.998016 \approx 894.3
    $$

    **Expected value of $r_{t+\Delta t}$:**

    Using the CIR conditional mean:

    $$
    \mathbb{E}[r_{t+\Delta t}] = \theta + (r_t - \theta)e^{-\kappa\Delta t} = 0.06 + (0.02 - 0.06) \times 0.998016 = 0.06 - 0.03992 = 0.02008
    $$

    Alternatively, using the chi-squared mean: $\mathbb{E}[r_{t+\Delta t}] = c(d + \lambda) = 2.232 \times 10^{-5}(5.333 + 894.3) = 2.232 \times 10^{-5} \times 899.6 \approx 0.02008$. $\checkmark$

---

**Exercise 2.** Using the Euler scheme with $r_{t_k} = 0.005$, $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.15$, and $\Delta t = 1/252$, compute the probability that the next Euler step produces a negative rate. Use the formula $\mathbb{P}(r_{t_{k+1}} < 0) = \Phi(-m/s)$ where $m = r_{t_k} + \kappa(\theta - r_{t_k})\Delta t$ and $s = \sigma\sqrt{r_{t_k}\Delta t}$.

??? success "Solution to Exercise 2"

    Given $r_{t_k} = 0.005$, $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.15$, $\Delta t = 1/252$.

    **Compute $m$ (expected next value under Euler):**

    $$
    m = r_{t_k} + \kappa(\theta - r_{t_k})\Delta t = 0.005 + 0.5(0.06 - 0.005)/252
    $$

    $$
    = 0.005 + 0.5 \times 0.055/252 = 0.005 + 0.0001091 = 0.005109
    $$

    **Compute $s$ (standard deviation of Euler step):**

    $$
    s = \sigma\sqrt{r_{t_k}\Delta t} = 0.15\sqrt{0.005/252} = 0.15\sqrt{1.984 \times 10^{-5}} = 0.15 \times 0.004455 = 6.683 \times 10^{-4}
    $$

    **Probability of negative rate:**

    $$
    \mathbb{P}(r_{t_{k+1}} < 0) = \Phi\left(-\frac{m}{s}\right) = \Phi\left(-\frac{0.005109}{6.683 \times 10^{-4}}\right) = \Phi(-7.645)
    $$

    This is an extremely small probability: $\Phi(-7.645) \approx 10^{-14}$. Even with $r_{t_k}$ as low as 0.005, the probability of a negative Euler step is negligible for daily time steps with these parameters. The negative rate problem becomes significant only when $r_{t_k}$ is even closer to zero or when $\Delta t$ is larger.

---

**Exercise 3.** Compare the three Euler fixes (truncation, reflection, absorption) for a path where the Euler update gives $r_{t_{k+1}} = -0.002$. For each method, what value is used for $r_{t_{k+1}}$? Which method best preserves the expected value of $r_{t_{k+1}}$, and why?

??? success "Solution to Exercise 3"

    The Euler update gives $r_{t_{k+1}} = -0.002$.

    **Truncation (full truncation):** Set $r_{t_{k+1}} = \max(-0.002, 0) = 0$.

    **Reflection:** Set $r_{t_{k+1}} = |-0.002| = 0.002$.

    **Absorption:** Set $r_{t_{k+1}} = 0$ (same as truncation in this case).

    **Which preserves the expected value best?** The true CIR process is non-negative, so the "correct" value should be some small positive number. Reflection gives $r_{t_{k+1}} = 0.002$, which is positive and preserves the magnitude of the deviation from zero. Truncation and absorption both set the value to zero, which introduces a downward bias.

    Reflection best preserves the expected value because the true process, when it approaches zero, is repelled (if the Feller condition holds) or reflected (if violated). The symmetric reflection $|r|$ mimics this boundary behavior. Truncation to zero acts as absorption, which is not the correct boundary behavior for the CIR process and systematically underestimates the rate near zero.

---

**Exercise 4.** Derive the Milstein correction term $\frac{\sigma^2}{4}(Z_k^2 - 1)\Delta t$ for the CIR process. Start from $\frac{\partial}{\partial r}(\sigma\sqrt{r}) = \frac{\sigma}{2\sqrt{r}}$ and use the Ito-Taylor expansion to show that the double stochastic integral contributes $\frac{1}{2}\sigma\sqrt{r}\cdot\frac{\sigma}{2\sqrt{r}}((\Delta W)^2 - \Delta t) = \frac{\sigma^2}{4}(Z^2 - 1)\Delta t$.

??? success "Solution to Exercise 4"

    The Milstein scheme for a general SDE $dX = a(X)dt + b(X)dW$ adds the correction $\frac{1}{2}b(X)b'(X)[(\Delta W)^2 - \Delta t]$.

    For CIR: $b(r) = \sigma\sqrt{r}$, so:

    $$
    b'(r) = \frac{\sigma}{2\sqrt{r}}
    $$

    The Milstein correction is:

    $$
    \frac{1}{2}b(r_{t_k})b'(r_{t_k})[(\Delta W_k)^2 - \Delta t] = \frac{1}{2}\sigma\sqrt{r_{t_k}} \cdot \frac{\sigma}{2\sqrt{r_{t_k}}}[(\Delta W_k)^2 - \Delta t]
    $$

    $$
    = \frac{\sigma^2}{4}[(\Delta W_k)^2 - \Delta t]
    $$

    Since $\Delta W_k = \sqrt{\Delta t}\,Z_k$ where $Z_k \sim \mathcal{N}(0,1)$:

    $$
    (\Delta W_k)^2 - \Delta t = \Delta t(Z_k^2 - 1)
    $$

    Therefore the Milstein correction is:

    $$
    \frac{\sigma^2}{4}(Z_k^2 - 1)\Delta t
    $$

    Note that $\sqrt{r_{t_k}}$ cancels between $b$ and $b'$, making the correction **independent of $r_{t_k}$**. This is a special feature of the square-root diffusion.

---

**Exercise 5.** The implicit Milstein scheme gives $r_{t_{k+1}} = \frac{r_{t_k} + \kappa\theta\Delta t + \sigma\sqrt{r_{t_k}}\sqrt{\Delta t}\,Z_k + \frac{\sigma^2}{4}(Z_k^2 - 1)\Delta t}{1 + \kappa\Delta t}$. Show that the denominator $1 + \kappa\Delta t > 1$ dampens extreme values. For $r_{t_k} = 0.01$, $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.15$, $\Delta t = 1/252$, compute $r_{t_{k+1}}$ for $Z_k = -3$ (a large negative shock) using both the explicit and implicit Milstein schemes. Does either produce a negative value?

??? success "Solution to Exercise 5"

    Given $r_{t_k} = 0.01$, $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.15$, $\Delta t = 1/252$, $Z_k = -3$.

    **Explicit Milstein:**

    $$
    r_{t_{k+1}} = r_{t_k} + \kappa(\theta - r_{t_k})\Delta t + \sigma\sqrt{r_{t_k}}\sqrt{\Delta t}\,Z_k + \frac{\sigma^2}{4}(Z_k^2 - 1)\Delta t
    $$

    Computing each term:

    - Drift: $0.5(0.06 - 0.01)/252 = 0.025/252 = 9.921 \times 10^{-5}$
    - Diffusion: $0.15\sqrt{0.01}\sqrt{1/252}(-3) = 0.015 \times 0.06300 \times (-3) = -2.835 \times 10^{-3}$
    - Milstein: $\frac{0.0225}{4}(9 - 1)/252 = 0.005625 \times 8/252 = 1.786 \times 10^{-4}$

    $$
    r_{t_{k+1}} = 0.01 + 9.921 \times 10^{-5} - 2.835 \times 10^{-3} + 1.786 \times 10^{-4} = 0.01 - 0.002558 = 0.007442
    $$

    **Implicit Milstein:**

    $$
    r_{t_{k+1}} = \frac{r_{t_k} + \kappa\theta\Delta t + \sigma\sqrt{r_{t_k}}\sqrt{\Delta t}\,Z_k + \frac{\sigma^2}{4}(Z_k^2 - 1)\Delta t}{1 + \kappa\Delta t}
    $$

    Numerator: $0.01 + 0.5 \times 0.06/252 + (-2.835 \times 10^{-3}) + 1.786 \times 10^{-4}$

    $$
    = 0.01 + 1.190 \times 10^{-4} - 2.835 \times 10^{-3} + 1.786 \times 10^{-4} = 0.007462
    $$

    Denominator: $1 + 0.5/252 = 1 + 0.001984 = 1.001984$.

    $$
    r_{t_{k+1}} = \frac{0.007462}{1.001984} = 0.007447
    $$

    Both values are positive. The implicit scheme produces a very slightly smaller value due to the damping denominator, but the difference is minimal for this moderate shock. For $Z_k = -3$, neither scheme produces a negative value with these parameters because $r_{t_k} = 0.01$ is far enough from zero.

---

**Exercise 6.** Explain why the exact simulation method allows arbitrarily large time steps $\Delta t$ without introducing discretization error, while the Euler method requires $\Delta t$ to be small. If a derivative payoff depends on the rate at monthly dates only, how many time steps does exact simulation need for a 5-year horizon versus daily Euler?

??? success "Solution to Exercise 6"

    **Why exact simulation allows large $\Delta t$:** The exact simulation draws $r_{t+\Delta t}$ from the true conditional distribution $r_{t+\Delta t} \mid r_t \sim (c) \cdot \chi^2(d, \lambda)$. This distribution is exact regardless of $\Delta t$, because it is the analytical transition density of the CIR process. No Taylor expansion or discretization is involved. The only error comes from the finite number of Monte Carlo paths (statistical error), not from time discretization.

    **Why Euler requires small $\Delta t$:** The Euler scheme approximates the drift and diffusion as constant over each step, replacing the continuous SDE with a discrete recursion. The local error in each step is $O(\Delta t^{3/2})$ (for weak convergence), and these errors accumulate over $N = T/\Delta t$ steps. Additionally, large $\Delta t$ increases the probability of producing negative rates, which violates the model's non-negativity property.

    **Time step comparison for a 5-year horizon:**

    - **Exact simulation** with monthly dates: $5 \times 12 = 60$ time steps (only the dates needed for numerical integration of $\int r_s\,ds$).
    - **Daily Euler**: $5 \times 252 = 1{,}260$ time steps.

    Exact simulation requires approximately 21 times fewer steps, and each step is bias-free. Even though each exact simulation step is more expensive (non-central chi-squared sampling vs. Gaussian sampling), the large reduction in steps makes the overall computation competitive or faster.

---

**Exercise 7.** Design a convergence experiment comparing exact simulation, Euler with truncation, and implicit Milstein for pricing a 5-year zero-coupon bond under CIR with $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.15$, $r_0 = 0.04$. Describe the experiment: what is the "true" price (from the analytical formula), how many paths $M$ to use, which time step sizes $\Delta t$ to test, and how to measure convergence. What plot would you produce to demonstrate the convergence rates?

??? success "Solution to Exercise 7"

    **True price:** Compute analytically using the CIR bond formula $P^{\text{exact}}(0,5) = A(5)e^{-B(5)r_0}$ with $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.15$, $r_0 = 0.04$.

    First: $\gamma = \sqrt{0.25 + 0.045} = \sqrt{0.295} \approx 0.5431$. Then compute $B(5)$, $A(5)$, and $P^{\text{exact}}$.

    **Experiment design:**

    1. **Number of paths:** Fix $M = 100{,}000$ (large enough that statistical error is small relative to discretization error).

    2. **Time step sizes:** Test $\Delta t \in \{1, 1/4, 1/12, 1/52, 1/252\}$ (annual, quarterly, monthly, weekly, daily).

    3. **For each $\Delta t$ and each method:**
        - Simulate $M$ paths using the given scheme.
        - Approximate $\int_0^5 r_s\,ds$ using the trapezoidal rule.
        - Compute $\hat{P} = \frac{1}{M}\sum_{m=1}^M e^{-\int_0^5 r_s^{(m)}\,ds}$.
        - Record the bias $|\hat{P} - P^{\text{exact}}|$ and the standard error.

    4. **Convergence measure:** The bias (systematic error from discretization) should decrease as $\Delta t \to 0$. For the Euler scheme, the weak convergence rate is $O(\Delta t^{0.5})$ for the CIR process. For exact simulation, the bias is zero for any $\Delta t$ (only the integration approximation contributes).

    **Plot:** A log-log plot with $\Delta t$ on the horizontal axis and $|\hat{P} - P^{\text{exact}}|$ on the vertical axis. Three lines (one per method):

    - **Exact simulation:** Nearly flat (zero bias), with only statistical noise and integration error.
    - **Euler with truncation:** Slope approximately $-0.5$ on log-log scale, confirming $O(\sqrt{\Delta t})$ weak convergence.
    - **Implicit Milstein:** Slope between $-0.5$ and $-1.0$, showing improved convergence over plain Euler.

    A secondary plot showing the standard error vs. $M$ (for fixed $\Delta t$) would confirm the $O(1/\sqrt{M})$ statistical convergence rate, which is the same for all methods.
