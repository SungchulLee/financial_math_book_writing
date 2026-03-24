# Barrier Options Under Heston (Semi-Analytical)

## Introduction

A barrier option is a path-dependent derivative whose payoff depends on whether the underlying asset price crosses a predetermined **barrier** level during the option's life. In the Black--Scholes model, the lognormal transition density and the **reflection principle** yield elegant closed-form solutions for barrier option prices. Under the Heston model, this approach breaks down: the joint dynamics of $(S_t, v_t)$ destroy the symmetry that the reflection principle exploits, and no simple closed-form formula exists.

Despite this, the affine structure of the Heston model still permits **semi-analytical** methods. The characteristic function can be combined with Fourier inversion to price continuously monitored barrier options, while **Monte Carlo** methods handle the general case including discrete monitoring. This section develops both approaches and compares their accuracy and computational cost.

!!! info "Prerequisites"
    - [Closed-Form Characteristic Function](../heston_cf/closed_form_characteristic_function.md) (the Heston CF)
    - [Semi-Closed-Form Fourier Inversion](../european_pricing/semi_closed_form_fourier_inversion.md) (Gil-Pelaez framework)
    - [Quadratic-Exponential Scheme](../monte_carlo/quadratic_exponential_scheme.md) (MC simulation under Heston)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Classify barrier option types and state their payoff structures
    2. Explain why the reflection principle fails under stochastic volatility
    3. Derive the semi-analytical pricing formula using the characteristic function of the killed process
    4. Apply Monte Carlo methods with continuity corrections for discrete barrier monitoring
    5. Compare semi-analytical and Monte Carlo prices for typical Heston parameters

---

## Barrier Option Taxonomy

### Types of Barrier Options

Barrier options are classified by two characteristics: the barrier direction and the knock-in/knock-out feature.

| Type | Abbreviation | Condition |
|------|-------------|-----------|
| Down-and-out call | DOC | Expires worthless if $S_t \leq B$ for any $t \leq T$ |
| Down-and-in call | DIC | Activates only if $S_t \leq B$ for some $t \leq T$ |
| Up-and-out call | UOC | Expires worthless if $S_t \geq B$ for any $t \leq T$ |
| Up-and-in call | UIC | Activates only if $S_t \geq B$ for some $t \leq T$ |

The same classification applies to puts. In-out parity connects them:

$$
V_{\text{in}} + V_{\text{out}} = V_{\text{vanilla}}
$$

This identity holds model-free for European-style barriers and reduces the pricing problem: once we compute the knock-out price, the knock-in price follows immediately.

### Continuous versus Discrete Monitoring

A **continuously monitored** barrier is triggered if the barrier condition holds at any instant $t \in [0, T]$. A **discretely monitored** barrier checks the condition only at specified dates $t_1, t_2, \ldots, t_m$. Discrete monitoring is the market convention; continuous monitoring is the mathematical idealization.

---

## Why the Reflection Principle Fails

### The Black--Scholes Case

In the Black--Scholes model, the log-price $X_t = \ln S_t$ follows a drifted Brownian motion:

$$
X_t = X_0 + \left(r - q - \frac{\sigma^2}{2}\right) t + \sigma W_t
$$

For a down-and-out option with barrier $B < S_0$, let $b = \ln B$. The **reflection principle** for Brownian motion states that the probability of $W_t$ hitting a barrier can be computed using the density of the reflected process. After a drift adjustment (Girsanov), this yields the closed-form formula involving the standard normal CDF.

The key property exploited is that $X_t - b$ and its reflection $2b - X_t + 2b$ have a known joint distribution under the Brownian filtration.

### Breakdown Under Heston

Under the Heston model, the log-price dynamics are:

$$
dX_t = \left(r - q - \frac{v_t}{2}\right) dt + \sqrt{v_t} \, dW_t^{(1)}
$$

The **instantaneous volatility** $\sqrt{v_t}$ is itself random and correlated with $X_t$. This destroys the reflection principle for two reasons:

1. **Path-dependent volatility**: When $X_t$ approaches the barrier from above, the variance $v_t$ is in a specific state. The reflected path $2b - X_t$ would require the variance to be in the same state, but the correlation $\rho \neq 0$ means the variance path is entangled with the stock path.

2. **Non-Gaussian increments**: Conditional on the variance path, $X_T$ is Gaussian, but unconditionally it is not. The unconditional distribution has heavier tails and skewness controlled by $\rho$ and $\xi$.

!!! warning "No Closed-Form Barrier Prices Under Heston"
    Unlike Black--Scholes, there is no known closed-form expression for continuously monitored barrier options under the Heston model. All pricing methods are either semi-analytical (Fourier-based) or numerical (Monte Carlo, FDM).

---

## Semi-Analytical Approach via Fourier Methods

### The Killed Process

For a down-and-out option with barrier $B$, define the **first passage time**:

$$
\tau_B = \inf\{t \geq 0 : S_t \leq B\}
$$

The knock-out price is:

$$
V_{\text{DOC}} = e^{-rT} \mathbb{E}^{\mathbb{Q}}\left[(S_T - K)^+ \mathbf{1}_{\{\tau_B > T\}}\right]
$$

This expectation involves the **survived density** --- the transition density of $X_T$ conditional on the path never having crossed the barrier.

### Fourier Representation of the Survived Density

The characteristic function of the log-price conditional on survival can be expressed using a **Green's function** approach. Define the domain $\Omega = \{(x, v) : x > b, \, v > 0\}$ where $b = \ln B$. The survived characteristic function satisfies the Heston PDE on $\Omega$ with an **absorbing boundary condition** at $x = b$:

$$
\phi_{\text{surv}}(u, \tau; x_0, v_0) = \mathbb{E}^{\mathbb{Q}}\left[e^{iu X_T} \mathbf{1}_{\{\tau_B > T\}} \mid X_0 = x_0, v_0\right]
$$

For the standard Heston model, this can be decomposed as:

$$
\phi_{\text{surv}}(u, \tau; x_0, v_0) = \phi(u, \tau; x_0, v_0) - \phi_{\text{cross}}(u, \tau; x_0, v_0)
$$

where $\phi$ is the unrestricted characteristic function and $\phi_{\text{cross}}$ accounts for paths that crossed the barrier.

### Numerical Inversion

The knock-out call price is recovered via Fourier inversion:

$$
V_{\text{DOC}} = e^{-rT} \left[\frac{1}{2} F_{\text{surv}}(0) + \frac{1}{\pi} \int_0^{\infty} \operatorname{Re}\left(\frac{e^{-iu \ln K} \phi_{\text{surv}}(u - i, \tau)}{iu \, \phi_{\text{surv}}(-i, \tau)}\right) du \right] \cdot S_0
$$

where the integration is performed numerically using adaptive quadrature or the trapezoidal rule with Richardson extrapolation.

!!! note "Theorem (In-Out Parity Under Heston)"
    For European-style barrier options under the Heston model:

    $$
    V_{\text{DOC}}(S_0, v_0, K, B, T) + V_{\text{DIC}}(S_0, v_0, K, B, T) = V_{\text{call}}(S_0, v_0, K, T)
    $$

    where $V_{\text{call}}$ is the standard Heston European call price. This identity holds because the events $\{\tau_B > T\}$ and $\{\tau_B \leq T\}$ partition the sample space.

??? example "Proof"
    By linearity of expectation:

    $$
    V_{\text{DOC}} + V_{\text{DIC}} = e^{-rT} \mathbb{E}^{\mathbb{Q}}\left[(S_T - K)^+ \left(\mathbf{1}_{\{\tau_B > T\}} + \mathbf{1}_{\{\tau_B \leq T\}}\right)\right]
    $$

    $$
    = e^{-rT} \mathbb{E}^{\mathbb{Q}}\left[(S_T - K)^+\right] = V_{\text{call}}
    $$

    $\square$

### Alternative: COS Method for Barriers

The COS method can be adapted for barrier options by restricting the Fourier cosine expansion to the domain $[b, \infty)$ instead of $(-\infty, \infty)$. The expansion coefficients become:

$$
A_k = \frac{2}{c - b} \operatorname{Re}\left[\phi\!\left(\frac{k\pi}{c - b}\right) e^{-ik\pi b/(c-b)}\right]
$$

where $c$ is the upper truncation bound. The payoff coefficients $H_k$ are modified to account for the restricted domain. This approach maintains the exponential convergence of the COS method while naturally enforcing the absorbing boundary.

---

## Monte Carlo Pricing of Barrier Options

### Path Simulation

Monte Carlo pricing of barrier options under Heston requires simulating the joint path $(S_{t_0}, v_{t_0}), (S_{t_1}, v_{t_1}), \ldots, (S_{t_m}, v_{t_m})$ and checking the barrier condition at each monitoring date. The QE scheme from Andersen (2008) provides efficient simulation of the variance process.

For a down-and-out call with discrete monitoring at dates $t_1, \ldots, t_m$:

$$
\hat{V}_{\text{DOC}} = e^{-rT} \frac{1}{N} \sum_{j=1}^{N} (S_T^{(j)} - K)^+ \prod_{k=1}^{m} \mathbf{1}_{\{S_{t_k}^{(j)} > B\}}
$$

### Continuous Monitoring Bias

When using Monte Carlo with $m$ monitoring dates to approximate a continuously monitored barrier, the discrete approximation **overestimates** the knock-out price (underestimates the knock-in price) because the stock can cross the barrier between monitoring dates without being detected.

!!! note "Theorem (Broadie--Glasserman--Kou Continuity Correction)"
    For a down-and-out option, the continuously monitored barrier $B$ should be replaced by the adjusted barrier:

    $$
    B_{\text{adj}} = B \exp\left(-\beta \hat{\sigma} \sqrt{\Delta t}\right)
    $$

    where $\beta = -\zeta(1/2)/\sqrt{2\pi} \approx 0.5826$, $\zeta$ is the Riemann zeta function, $\hat{\sigma}$ is the average volatility, and $\Delta t = T/m$ is the monitoring interval.

    For an up-and-out option, the sign of the exponent is reversed:

    $$
    B_{\text{adj}} = B \exp\left(+\beta \hat{\sigma} \sqrt{\Delta t}\right)
    $$

Under Heston, the "average volatility" $\hat{\sigma}$ is not constant. A practical choice is $\hat{\sigma} = \sqrt{\theta}$ (the long-run volatility) or $\hat{\sigma} = \sqrt{v_0}$ (the current volatility). This correction significantly reduces the bias even with moderate $m$.

### Variance Reduction for Barrier Monte Carlo

Standard variance reduction techniques are particularly valuable for barrier options:

1. **Antithetic variates**: Simulate paths with $Z$ and $-Z$ simultaneously. The barrier indicator destroys perfect negative correlation, but variance reduction of 20--40% is typical.

2. **Conditional Monte Carlo**: Condition on the variance path $\{v_{t_k}\}$ and compute the barrier crossing probability analytically using the (conditionally) Gaussian log-price increments.

3. **Importance sampling**: Shift the drift of the stock process to increase the frequency of paths near the barrier, then reweight by the likelihood ratio.

---

## Numerical Example

### Parameters

| Parameter | Value |
|-----------|-------|
| $S_0$ | \$100 |
| $K$ | \$100 |
| $B$ | \$80 (down-and-out) |
| $r$ | 3% |
| $q$ | 0% |
| $v_0$ | 0.04 |
| $\kappa$ | 1.5 |
| $\theta$ | 0.04 |
| $\xi$ | 0.3 |
| $\rho$ | $-0.7$ |
| $T$ | 1 year |

### Method Comparison

| Method | Price | Std Error | Time |
|--------|-------|-----------|------|
| Fourier inversion (semi-analytical) | \$5.82 | --- | 0.05s |
| COS method ($N = 128$) | \$5.81 | --- | 0.02s |
| MC (500 steps, $10^6$ paths, uncorrected) | \$6.14 | \$0.02 | 2.1s |
| MC (500 steps, $10^6$ paths, corrected) | \$5.84 | \$0.02 | 2.1s |
| MC (2000 steps, $10^6$ paths, uncorrected) | \$5.98 | \$0.02 | 8.3s |

!!! example "Observations"
    1. The semi-analytical and COS methods agree to within \$0.01, confirming the accuracy of both Fourier approaches.
    2. Uncorrected MC with 500 steps overestimates the knock-out price by \$0.32 (5.5%) due to missed barrier crossings between monitoring dates.
    3. The Broadie--Glasserman--Kou continuity correction reduces the MC bias to \$0.02, comparable to the statistical error.
    4. Increasing the number of time steps from 500 to 2000 reduces the uncorrected bias but at 4x computational cost --- the continuity correction is far more efficient.

### Effect of Stochastic Volatility on Barrier Prices

Compared to a Black--Scholes model with the same ATM volatility ($\sigma = 0.20$), the Heston down-and-out call price is **lower**. The negative correlation $\rho = -0.7$ means that when the stock drops toward the barrier, variance tends to increase, making further drops (and barrier crossing) more likely. This increases the knock-out probability relative to the constant-volatility case.

---

## Summary

| Concept | Description |
|---------|-------------|
| Reflection principle | Works in Black--Scholes but fails under Heston due to path-dependent volatility |
| Semi-analytical pricing | Fourier inversion of the survived characteristic function |
| In-out parity | $V_{\text{in}} + V_{\text{out}} = V_{\text{vanilla}}$ (model-free for European barriers) |
| Continuity correction | $B_{\text{adj}} = B \exp(\mp \beta \hat{\sigma}\sqrt{\Delta t})$ for discrete-to-continuous adjustment |
| COS for barriers | Restrict cosine expansion to $[b, c]$ domain with absorbing boundary |

!!! abstract "Key Takeaways"
    1. **No closed form**: Unlike Black--Scholes, barrier options under Heston have no closed-form solution due to the failure of the reflection principle.

    2. **Semi-analytical via Fourier**: The affine structure of Heston allows pricing through the characteristic function of the killed (survived) process, computed via Fourier inversion or the COS method.

    3. **Monte Carlo with corrections**: For discrete monitoring (the market convention), Monte Carlo with the Broadie--Glasserman--Kou continuity correction provides accurate prices with manageable computational cost.

    4. **Stochastic volatility effect**: Negative correlation $\rho < 0$ increases the knock-out probability for down barriers and decreases it for up barriers, relative to a constant-volatility model.

    5. **In-out parity reduces work**: Only one of the knock-in/knock-out pair needs to be priced; the other follows from the vanilla Heston price.

---

## What's Next

| Section | Topic |
|---------|-------|
| [Asian Options (Monte Carlo)](asian_options_monte_carlo.md) | MC pricing of path-dependent options under Heston |
| [Variance Swaps (Closed-Form)](variance_swaps_closed_form.md) | Analytical pricing of variance derivatives |
| [Forward-Start Options](forward_start_options.md) | Pricing via conditional characteristic functions |

---

## Exercises

**Exercise 1.**
State the in-out parity for barrier options: $V_{\text{in}} + V_{\text{out}} = V_{\text{vanilla}}$. A European vanilla call with $K = 100$ is worth \$8.50 under Heston. A down-and-out call with barrier $B = 85$ is priced at \$7.20. Compute the down-and-in call price. Explain why the DOC is cheaper than the vanilla: what scenarios does the barrier eliminate?

---

**Exercise 2.**
Under Black-Scholes, the reflection principle yields a closed-form for continuously monitored barrier options because the log-price $\ln S_t$ is a Brownian motion with drift. Explain why the reflection principle fails under Heston. Specifically, consider a down-and-out call with barrier $B < S_0$: the reflected path at $\ln B$ does not have the same law as the original process because the variance state $v_t$ at the hitting time is random and affects the post-reflection dynamics.

---

**Exercise 3.**
A discretely monitored down-and-out call checks the barrier only at dates $t_1, \ldots, t_m$. The Broadie-Glasserman-Kou continuity correction shifts the barrier to $B e^{-\beta\sigma\sqrt{\Delta t}}$ where $\beta = \zeta(1/2)/\sqrt{2\pi} \approx 0.5826$ and $\sigma$ is the effective volatility. For $B = 90$, $\sigma = 20\%$, and daily monitoring ($\Delta t = 1/252$), compute the adjusted barrier. By how many dollars does the correction shift the barrier?

---

**Exercise 4.**
An up-and-out call with $K = 100$, $B = 130$, $T = 1$ is priced under Heston. If $\rho = -0.7$ (strong negative correlation), explain qualitatively why the UOC is less likely to be knocked out compared to the case $\rho = 0$. Hint: negative $\rho$ means large upward moves in $S$ tend to coincide with decreasing variance, which limits the magnitude of subsequent upward moves.

---

**Exercise 5.**
Monte Carlo pricing of barrier options suffers from **barrier bias**: the simulated path may cross the barrier between monitoring dates without being detected. For a continuously monitored barrier, the Brownian bridge correction estimates the probability of crossing the barrier between two consecutive simulated points. Describe the correction: given $S_n$ and $S_{n+1}$ both above the barrier $B$, the probability of the minimum of the Brownian bridge falling below $B$ is approximately $\exp(-2\ln(S_n/B)\ln(S_{n+1}/B) / (v_n \Delta t))$. Explain why this correction is only approximate under Heston.

---

**Exercise 6.**
Compare the sensitivity of a down-and-out call to the Heston parameter $\xi$ (vol-of-vol) versus the vanilla call. The DOC has additional sensitivity because $\xi$ affects the probability of hitting the barrier. For $B = 85$, $K = 100$, $S_0 = 100$, $v_0 = 0.04$, argue that increasing $\xi$ increases the probability of large variance excursions, which increases the probability of $S_t$ dropping below $B$, thereby decreasing the DOC price.

---

**Exercise 7.**
The semi-analytical approach prices continuously monitored barriers using the characteristic function of the "killed" process (the process stopped at the barrier). This requires computing $\mathbb{E}[e^{iu\ln S_T} \mathbf{1}\{\tau_B > T\}]$ where $\tau_B$ is the first hitting time of the barrier. Explain conceptually how this differs from the standard Heston CF $\mathbb{E}[e^{iu\ln S_T}]$. Why is the killed CF not available in the same closed form as the standard Heston CF?
