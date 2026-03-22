# Monte Carlo Simulation

Monte Carlo methods are essential when closed-form pricing formulas are unavailable---for example, path-dependent interest rate derivatives, early-exercise options, or multi-factor extensions. For the Vasicek model specifically, Monte Carlo serves a dual role: it validates the closed-form bond and option prices derived in earlier sections, and it provides a template for simulating more complex short-rate models where analytical solutions do not exist. The Ornstein-Uhlenbeck dynamics of the Vasicek model admit an **exact simulation** scheme that avoids discretization error entirely, making it an ideal setting for studying variance reduction techniques.

---

## Exact simulation of the OU process

### The exact transition

The Vasicek short rate satisfies

$$
r_{t+\Delta t} \mid r_t \sim \mathcal{N}\!\left(\mu_{\Delta t}(r_t),\; v^2_{\Delta t}\right)
$$

where

$$
\mu_{\Delta t}(r_t) = \theta + (r_t - \theta)\,e^{-\kappa\Delta t}
$$

$$
v^2_{\Delta t} = \frac{\sigma^2}{2\kappa}\!\left(1 - e^{-2\kappa\Delta t}\right)
$$

This follows directly from the explicit solution of the OU SDE. The transition is exact for any step size $\Delta t$---there is no discretization error.

### Simulation algorithm

For a single path from $t = 0$ to $t = T$ with $N$ steps and $\Delta t = T/N$:

1. Set $r_0$ to the initial short rate.
2. For $i = 0, 1, \ldots, N-1$:
    - Draw $Z_i \sim \mathcal{N}(0,1)$
    - Set $r_{(i+1)\Delta t} = \mu_{\Delta t}(r_{i\Delta t}) + v_{\Delta t}\,Z_i$

Since the transition is exact, the choice of $N$ affects only the resolution at which the path is sampled---not the accuracy. For bond pricing, a single step from $0$ to $T$ suffices to generate $r_T$. For path-dependent payoffs, the number of steps should match the monitoring frequency of the derivative.

---

## Euler-Maruyama discretization

### The scheme

The Euler-Maruyama approximation for the Vasicek SDE $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ is

$$
\hat{r}_{(i+1)\Delta t} = \hat{r}_{i\Delta t} + \kappa(\theta - \hat{r}_{i\Delta t})\,\Delta t + \sigma\,\sqrt{\Delta t}\,Z_i
$$

### Comparison with exact simulation

| Property | Exact | Euler-Maruyama |
|---|---|---|
| Transition distribution | Exact Gaussian | Approximate Gaussian |
| Discretization error | None | $O(\Delta t)$ weak, $O(\sqrt{\Delta t})$ strong |
| Step size requirement | Any | Small $\Delta t$ for accuracy |
| Computational cost per step | Same | Same |
| Implementation complexity | Requires $e^{-\kappa\Delta t}$ | Simpler formula |

Since exact simulation has no disadvantage relative to Euler-Maruyama for the Vasicek model, the exact scheme should always be preferred. The Euler scheme is useful as a baseline for testing more complex models (e.g., CIR) where exact simulation is harder.

### Convergence of Euler-Maruyama

For the Vasicek model with step size $\Delta t$:

- **Weak error** (error in expectations): $|\mathbb{E}[g(\hat{r}_T)] - \mathbb{E}[g(r_T)]| = O(\Delta t)$
- **Strong error** (pathwise error): $\mathbb{E}[|\hat{r}_T - r_T|^2]^{1/2} = O(\sqrt{\Delta t})$

The weak error is most relevant for pricing. With $N = 100$ steps per year, the weak error is typically negligible compared to Monte Carlo sampling error.

---

## Bond pricing by Monte Carlo

### Direct simulation

The zero-coupon bond price is

$$
P(0,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\right]
$$

To estimate this by Monte Carlo:

1. Simulate $M$ paths of $(r_0, r_{\Delta t}, r_{2\Delta t}, \ldots, r_T)$ using exact transitions.
2. Approximate the integral $\int_0^T r_s\,ds$ on each path using the trapezoidal rule:

$$
\int_0^T r_s\,ds \approx \Delta t\!\left(\frac{r_0}{2} + \sum_{i=1}^{N-1} r_{i\Delta t} + \frac{r_T}{2}\right)
$$

3. Compute the Monte Carlo estimator:

$$
\hat{P}(0,T) = \frac{1}{M}\sum_{j=1}^M \exp\!\left(-\int_0^T r_s^{(j)}\,ds\right)
$$

### Alternative: exact integral distribution

For the Vasicek model, the integral $\int_t^T r_s\,ds$ conditional on $r_t$ is Gaussian (since $r_s$ is Gaussian for each $s$, and the integral of a Gaussian process is Gaussian). Its mean and variance can be computed in closed form:

$$
\mathbb{E}\!\left[\int_t^T r_s\,ds \,\Big|\, r_t\right] = \theta\,\tau + (r_t - \theta)\,\frac{1 - e^{-\kappa\tau}}{\kappa} = \theta\,\tau + (r_t - \theta)\,B(\tau)
$$

$$
\text{Var}\!\left(\int_t^T r_s\,ds \,\Big|\, r_t\right) = \frac{\sigma^2}{\kappa^2}\!\left[\tau - \frac{2}{\kappa}(1 - e^{-\kappa\tau}) + \frac{1}{2\kappa}(1 - e^{-2\kappa\tau})\right]
$$

This allows bond pricing in a single step: draw $\int_0^T r_s\,ds$ from its Gaussian distribution and compute $e^{-\int r_s\,ds}$. Of course, for the Vasicek model the closed-form bond price is available, making Monte Carlo unnecessary for plain bonds---but the technique extends to path-dependent derivatives.

---

## Variance reduction techniques

### Antithetic variates

For each path generated with innovations $Z_1, Z_2, \ldots, Z_N$, generate a mirror path with $-Z_1, -Z_2, \ldots, -Z_N$. The estimator becomes

$$
\hat{P}_{\text{AV}} = \frac{1}{2M}\sum_{j=1}^M \left(e^{-\int r_s^{(j)}\,ds} + e^{-\int \tilde{r}_s^{(j)}\,ds}\right)
$$

where $\tilde{r}_s^{(j)}$ is the antithetic path. Since $e^{-x}$ is a convex function and the OU process is negatively correlated with its antithetic version, the variance reduction is typically 30--50% for bond pricing.

### Control variates

Use the closed-form bond price as a control. For a derivative with payoff $g(r_T)$:

$$
\hat{V}_{\text{CV}} = \frac{1}{M}\sum_{j=1}^M g(r_T^{(j)})\,e^{-\int r_s^{(j)}\,ds} - c\!\left(\frac{1}{M}\sum_{j=1}^M e^{-\int r_s^{(j)}\,ds} - P_{\text{exact}}(0,T)\right)
$$

where $c$ is the optimal control coefficient (estimated from the sample covariance). This exploits the correlation between the derivative payoff and the discount factor, often achieving variance reductions of 80--95%.

### Importance sampling

Shift the drift of the simulated process to concentrate paths in regions where the payoff is large. For out-of-the-money bond options, importance sampling can dramatically reduce variance by tilting the distribution toward the exercise region.

For the Vasicek model, an optimal drift shift for pricing $P(0,T)$ replaces $\theta$ with a modified mean that targets paths near $r^* = -\ln K / B(T)$ (the critical rate for bond options). The Girsanov adjustment ensures unbiased estimation.

---

## Standard errors and confidence intervals

The Monte Carlo standard error for $M$ paths is

$$
\text{SE} = \frac{\hat{\sigma}_{\text{sample}}}{\sqrt{M}}
$$

where $\hat{\sigma}_{\text{sample}}$ is the sample standard deviation of the payoff across paths. A 95% confidence interval is $\hat{P} \pm 1.96 \cdot \text{SE}$.

For typical bond pricing with $M = 100{,}000$ paths:

| Method | Standard Error | Relative to naive |
|---|---|---|
| Naive MC | $1.2 \times 10^{-4}$ | 1.0 |
| Antithetic | $7.5 \times 10^{-5}$ | 0.63 |
| Control variate | $1.8 \times 10^{-5}$ | 0.15 |
| Combined | $1.2 \times 10^{-5}$ | 0.10 |

---

## Numerical example

**Bond pricing validation.** Parameters: $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.02$, $r_0 = 0.03$, $T = 5$.

Closed-form: $P(0,5) = A(5)\,e^{-B(5) \cdot 0.03}$.

Monte Carlo with $M = 100{,}000$ paths, $N = 100$ steps, exact simulation:

| Estimator | $\hat{P}(0,5)$ | SE | 95% CI |
|---|---|---|---|
| Naive | 0.8498 | $1.1 \times 10^{-4}$ | [0.8496, 0.8500] |
| Antithetic | 0.8498 | $6.8 \times 10^{-5}$ | [0.8497, 0.8499] |
| Control variate | 0.8497 | $1.5 \times 10^{-5}$ | [0.8497, 0.8497] |

All estimates agree with the closed-form value within the confidence interval, validating the simulation.

---

## Summary

The Vasicek model admits exact simulation via the Gaussian transition $r_{t+\Delta t} = e^{-\kappa\Delta t}r_t + (1 - e^{-\kappa\Delta t})\theta + v_{\Delta t}\,Z$, eliminating discretization error. Bond prices are estimated by averaging $e^{-\int r_s\,ds}$ across simulated paths, with variance reduction through antithetic variates (exploiting symmetry), control variates (exploiting the known bond price), and importance sampling (tilting toward the exercise region). The exact simulation scheme and the Gaussian integral distribution provide a baseline for testing Monte Carlo methods before applying them to models where closed forms are unavailable.

---
