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

## Exercises

**Exercise 1.** For the exact OU transition $r_{t+\Delta t} = \theta + (r_t - \theta)e^{-\kappa\Delta t} + v_{\Delta t}\,Z$, compute $\mu_{\Delta t}$ and $v_{\Delta t}$ explicitly for $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.02$, and $\Delta t = 0.25$. Verify that the conditional mean and variance match the formulas $\mu_{\Delta t}(r_t) = \theta + (r_t - \theta)e^{-\kappa\Delta t}$ and $v_{\Delta t}^2 = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\Delta t})$.

??? success "Solution to Exercise 1"
    With $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.02$, $\Delta t = 0.25$:

    **Conditional mean:**

    $$
    \mu_{\Delta t}(r_t) = \theta + (r_t - \theta)e^{-\kappa\Delta t} = 0.04 + (r_t - 0.04)e^{-0.125}
    $$

    $$
    e^{-0.125} = 0.8825
    $$

    $$
    \mu_{\Delta t}(r_t) = 0.04 + 0.8825(r_t - 0.04) = 0.00470 + 0.8825\,r_t
    $$

    **Conditional variance:**

    $$
    v_{\Delta t}^2 = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\Delta t}) = \frac{0.0004}{1.0}(1 - e^{-0.25}) = 0.0004 \times 0.2212 = 0.00008848
    $$

    $$
    v_{\Delta t} = \sqrt{0.00008848} = 0.009407
    $$

    **Verification against the formulas:**

    The formula $\mu_{\Delta t}(r_t) = \theta + (r_t - \theta)e^{-\kappa\Delta t}$ is confirmed directly.

    The formula $v_{\Delta t}^2 = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\Delta t})$: with $\sigma^2/(2\kappa) = 0.0004$ and $1 - e^{-2 \times 0.5 \times 0.25} = 1 - e^{-0.25} = 0.2212$, the product is $0.0004 \times 0.2212 = 0.00008848$. Both formulas check out.

---

**Exercise 2.** Compare the Euler-Maruyama scheme $\hat{r}_{t+\Delta t} = \hat{r}_t + \kappa(\theta - \hat{r}_t)\Delta t + \sigma\sqrt{\Delta t}\,Z$ with the exact transition by computing the conditional mean and variance of each scheme for one step. Show that the Euler-Maruyama conditional mean differs from the exact mean by $O(\Delta t^2)$ and identify the leading error term.

??? success "Solution to Exercise 2"
    **Euler-Maruyama:** $\hat{r}_{t+\Delta t} = \hat{r}_t + \kappa(\theta - \hat{r}_t)\Delta t + \sigma\sqrt{\Delta t}\,Z$.

    The conditional mean is:

    $$
    \mathbb{E}[\hat{r}_{t+\Delta t} | \hat{r}_t] = \hat{r}_t + \kappa(\theta - \hat{r}_t)\Delta t = (1 - \kappa\Delta t)\hat{r}_t + \kappa\theta\Delta t
    $$

    The conditional variance is:

    $$
    \text{Var}(\hat{r}_{t+\Delta t} | \hat{r}_t) = \sigma^2\Delta t
    $$

    **Exact transition:** $r_{t+\Delta t} = \theta + (r_t - \theta)e^{-\kappa\Delta t} + v_{\Delta t}\,Z$.

    The conditional mean is:

    $$
    \mathbb{E}[r_{t+\Delta t} | r_t] = \theta + (r_t - \theta)e^{-\kappa\Delta t} = e^{-\kappa\Delta t}\,r_t + (1 - e^{-\kappa\Delta t})\theta
    $$

    **Comparison of means.** Taylor-expanding $e^{-\kappa\Delta t} = 1 - \kappa\Delta t + \frac{1}{2}\kappa^2\Delta t^2 + O(\Delta t^3)$:

    $$
    \text{Exact mean} = (1 - \kappa\Delta t + \tfrac{1}{2}\kappa^2\Delta t^2)\,r_t + (\kappa\Delta t - \tfrac{1}{2}\kappa^2\Delta t^2)\theta
    $$

    $$
    \text{Euler mean} = (1 - \kappa\Delta t)\,r_t + \kappa\Delta t\,\theta
    $$

    The difference is:

    $$
    \text{Exact} - \text{Euler} = \frac{1}{2}\kappa^2\Delta t^2\,(r_t - \theta) + O(\Delta t^3)
    $$

    The leading error term is $\frac{1}{2}\kappa^2(r_t - \theta)\Delta t^2$, which is $O(\Delta t^2)$. The error is proportional to the deviation from equilibrium $r_t - \theta$ and to $\kappa^2$, reflecting the curvature of the exponential mean-reversion function.

    **Comparison of variances.** The exact variance $\frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\Delta t}) = \sigma^2\Delta t - \kappa\sigma^2\Delta t^2 + O(\Delta t^3)$ differs from the Euler variance $\sigma^2\Delta t$ by $-\kappa\sigma^2\Delta t^2 + O(\Delta t^3)$, again an $O(\Delta t^2)$ error.

---

**Exercise 3.** Explain why the exact simulation scheme produces no discretization error for the marginal distribution of $r_T$, even with a single step from $0$ to $T$. Under what circumstances would you still need multiple intermediate steps?

??? success "Solution to Exercise 3"
    The exact simulation scheme draws $r_T$ from $\mathcal{N}(\mu_T(r_0), v_T^2)$ where:

    $$
    \mu_T(r_0) = \theta + (r_0 - \theta)e^{-\kappa T}, \qquad v_T^2 = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa T})
    $$

    This is the **exact** conditional distribution of $r_T$ given $r_0$, derived from the explicit solution of the OU SDE. Since the transition from $r_0$ to $r_T$ is Gaussian with these exact parameters, a single draw $r_T = \mu_T(r_0) + v_T\,Z$ produces a sample from the correct marginal distribution regardless of the step size. There is no discretization error because no approximation was made.

    **Multiple intermediate steps are needed when:**

    1. **Path-dependent payoffs**: If the derivative depends on $\int_0^T r_s\,ds$ or $\max_{0 \leq s \leq T} r_s$, the value of $r_T$ alone is insufficient. Intermediate steps $(r_{t_1}, r_{t_2}, \ldots, r_{t_{N-1}})$ are needed to approximate the integral or track the running maximum.

    2. **Early exercise features**: American or Bermudan options require knowledge of $r_t$ at each potential exercise date.

    3. **Barrier features**: If the payoff depends on whether $r_t$ crosses a threshold during $[0, T]$, intermediate sampling is essential.

    For European payoffs that depend only on $r_T$ (or on $P(T,S) = f(r_T)$), a single exact step suffices.

---

**Exercise 4.** For bond pricing via Monte Carlo, the integral $\int_0^T r_s\,ds$ is approximated by the trapezoidal rule. Using the Vasicek parameters $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.02$, $r_0 = 0.03$, compute the exact mean and variance of the Gaussian integral $\int_0^5 r_s\,ds$ conditional on $r_0$. Why does this exact distribution make trapezoidal approximation unnecessary for plain bond pricing?

??? success "Solution to Exercise 4"
    With $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.02$, $r_0 = 0.03$, $T = 5$:

    **Mean of $\int_0^5 r_s\,ds$:**

    $$
    \mathbb{E}\!\left[\int_0^5 r_s\,ds \,\Big|\, r_0\right] = \theta\,T + (r_0 - \theta)\,B(T) = 0.04 \times 5 + (0.03 - 0.04) \times \frac{1 - e^{-2.5}}{0.5}
    $$

    $$
    B(5) = \frac{1 - e^{-2.5}}{0.5} = \frac{1 - 0.0821}{0.5} = 1.8358
    $$

    $$
    = 0.20 + (-0.01) \times 1.8358 = 0.20 - 0.01836 = 0.18164
    $$

    **Variance of $\int_0^5 r_s\,ds$:**

    $$
    \text{Var}\!\left(\int_0^5 r_s\,ds\right) = \frac{\sigma^2}{\kappa^2}\!\left[T - \frac{2}{\kappa}(1 - e^{-\kappa T}) + \frac{1}{2\kappa}(1 - e^{-2\kappa T})\right]
    $$

    $$
    = \frac{0.0004}{0.25}\left[5 - \frac{2}{0.5}(1 - e^{-2.5}) + \frac{1}{1.0}(1 - e^{-5})\right]
    $$

    $$
    = 0.0016\left[5 - 4 \times 0.9179 + 0.99326\right] = 0.0016\left[5 - 3.6716 + 0.9933\right] = 0.0016 \times 2.3217 = 0.003715
    $$

    $$
    \text{SD}\!\left(\int_0^5 r_s\,ds\right) = \sqrt{0.003715} = 0.06095
    $$

    **Why trapezoidal approximation is unnecessary for plain bonds:** Since $\int_0^T r_s\,ds$ is Gaussian with known mean and variance (computable in closed form), one can directly draw $I \sim \mathcal{N}(0.18164, 0.003715)$ and compute $P(0,5) = \mathbb{E}[e^{-I}]$. In fact, for a Gaussian random variable $I \sim \mathcal{N}(\mu_I, \sigma_I^2)$, we have $\mathbb{E}[e^{-I}] = e^{-\mu_I + \sigma_I^2/2}$, which gives the bond price analytically without any simulation at all. The trapezoidal rule is only needed for path-dependent payoffs where the integral distribution is not known in closed form.

---

**Exercise 5.** In antithetic variate sampling, the estimator uses both $Z$ and $-Z$ innovations. Show that the antithetic path $\tilde{r}_T$ satisfies $\tilde{r}_T = 2\mu_T(r_0) - r_T$ for the exact one-step simulation from $0$ to $T$. Compute $\text{Cov}(e^{-\int r_s\,ds}, e^{-\int \tilde{r}_s\,ds})$ and explain why it is negative, leading to variance reduction.

??? success "Solution to Exercise 5"
    For exact one-step simulation from $0$ to $T$:

    $$
    r_T = \mu_T(r_0) + v_T\,Z, \qquad \tilde{r}_T = \mu_T(r_0) + v_T\,(-Z) = \mu_T(r_0) - v_T\,Z
    $$

    Adding these: $r_T + \tilde{r}_T = 2\mu_T(r_0)$, so $\tilde{r}_T = 2\mu_T(r_0) - r_T$.

    For the discount factors (using the Gaussian integral distribution), define $I = \int_0^T r_s\,ds$ and $\tilde{I} = \int_0^T \tilde{r}_s\,ds$. Since the antithetic path replaces all $Z_i$ with $-Z_i$, the integral satisfies $\tilde{I} = 2\mu_I - I$ where $\mu_I = \mathbb{E}[I]$.

    The covariance is:

    $$
    \text{Cov}(e^{-I}, e^{-\tilde{I}}) = \text{Cov}(e^{-I}, e^{-(2\mu_I - I)}) = e^{-2\mu_I}\,\text{Cov}(e^{-I}, e^{I})
    $$

    Now $\text{Cov}(e^{-I}, e^{I}) = \mathbb{E}[e^{-I} \cdot e^{I}] - \mathbb{E}[e^{-I}]\mathbb{E}[e^{I}] = 1 - \mathbb{E}[e^{-I}]\mathbb{E}[e^{I}]$.

    Since $I$ is Gaussian with mean $\mu_I$ and variance $\sigma_I^2$: $\mathbb{E}[e^{-I}] = e^{-\mu_I + \sigma_I^2/2}$ and $\mathbb{E}[e^{I}] = e^{\mu_I + \sigma_I^2/2}$. Their product is $e^{\sigma_I^2}$. Since $\sigma_I^2 > 0$, we have $e^{\sigma_I^2} > 1$, so $\text{Cov}(e^{-I}, e^{I}) = 1 - e^{\sigma_I^2} < 0$.

    Therefore $\text{Cov}(e^{-I}, e^{-\tilde{I}}) = e^{-2\mu_I}(1 - e^{\sigma_I^2}) < 0$.

    The negative covariance means the antithetic estimator $\frac{1}{2}(e^{-I} + e^{-\tilde{I}})$ has smaller variance than naive averaging, since $\text{Var}(\frac{1}{2}(X + Y)) = \frac{1}{4}(\text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X,Y))$ and the negative covariance reduces the total variance.

---

**Exercise 6.** A control variate estimator for a bond option uses the bond price $P(0,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_0^T r_s\,ds}]$ as the control. Write the control variate estimator explicitly for a European call on a ZCB with payoff $(P(T,S) - K)^+$. Why is the optimal control coefficient $c^*$ expected to be positive?

??? success "Solution to Exercise 6"
    The European call payoff at time $T$ on a ZCB maturing at $S$ with strike $K$ is $(P(T,S) - K)^+$. The Monte Carlo estimator for its time-0 value is:

    $$
    \hat{V} = \frac{1}{M}\sum_{j=1}^M (P(T, S; r_T^{(j)}) - K)^+\,e^{-I^{(j)}}
    $$

    where $I^{(j)} = \int_0^T r_s^{(j)}\,ds$ is the integrated short rate on path $j$.

    The control variate estimator uses the known bond price $P_{\text{exact}}(0,T) = \mathbb{E}^{\mathbb{Q}}[e^{-I}]$:

    $$
    \hat{V}_{\text{CV}} = \frac{1}{M}\sum_{j=1}^M (P(T,S; r_T^{(j)}) - K)^+\,e^{-I^{(j)}} - c^*\!\left(\frac{1}{M}\sum_{j=1}^M e^{-I^{(j)}} - P_{\text{exact}}(0,T)\right)
    $$

    The optimal control coefficient is:

    $$
    c^* = \frac{\text{Cov}((P(T,S)-K)^+ e^{-I},\; e^{-I})}{\text{Var}(e^{-I})}
    $$

    **Why $c^*$ is expected to be positive:** The payoff $(P(T,S)-K)^+$ is large when $P(T,S)$ is large, which occurs when $r_T$ is low. Low $r_T$ tends to be associated with low integrated rates $I$, which means $e^{-I}$ is large. Therefore the payoff $(P(T,S)-K)^+ e^{-I}$ and the control $e^{-I}$ are **positively correlated**: paths that produce large discount factors also tend to produce large option payoffs. This positive covariance makes $c^* > 0$.

---

**Exercise 7.** With $M$ simulation paths, the Monte Carlo standard error is $\text{SE} = \hat{\sigma}/\sqrt{M}$. If naive Monte Carlo gives $\text{SE} = 1.2 \times 10^{-4}$ with $M = 100{,}000$ paths, how many paths are needed to achieve $\text{SE} = 1.0 \times 10^{-5}$ without variance reduction? If control variates reduce variance by a factor of 50, how many paths achieve the same precision?

??? success "Solution to Exercise 7"
    The standard error is $\text{SE} = \hat{\sigma}/\sqrt{M}$ where $\hat{\sigma}$ is the sample standard deviation.

    From naive MC with $M = 100{,}000$: $\text{SE} = 1.2 \times 10^{-4}$, so $\hat{\sigma} = \text{SE} \times \sqrt{M} = 1.2 \times 10^{-4} \times \sqrt{10^5} = 1.2 \times 10^{-4} \times 316.2 = 0.03795$.

    **Without variance reduction**, to achieve $\text{SE}_{\text{target}} = 1.0 \times 10^{-5}$:

    $$
    M_{\text{new}} = \left(\frac{\hat{\sigma}}{\text{SE}_{\text{target}}}\right)^2 = \left(\frac{0.03795}{1.0 \times 10^{-5}}\right)^2 = (3795)^2 = 14{,}402{,}025
    $$

    Approximately **14.4 million** paths are needed---a 144-fold increase from the original $M = 100{,}000$.

    **With control variates** reducing variance by a factor of 50, the effective standard deviation is $\hat{\sigma}_{\text{CV}} = \hat{\sigma}/\sqrt{50}$. The required paths:

    $$
    M_{\text{CV}} = \left(\frac{\hat{\sigma}_{\text{CV}}}{\text{SE}_{\text{target}}}\right)^2 = \left(\frac{\hat{\sigma}/\sqrt{50}}{1.0 \times 10^{-5}}\right)^2 = \frac{M_{\text{new}}}{50} = \frac{14{,}402{,}025}{50} = 288{,}041
    $$

    Approximately **288,000** paths suffice with control variates---a dramatic reduction from 14.4 million. This illustrates why variance reduction is essential for achieving high-precision Monte Carlo estimates in practice.
