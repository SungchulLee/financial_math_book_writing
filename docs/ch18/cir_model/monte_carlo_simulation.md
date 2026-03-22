# Monte Carlo Simulation for the CIR Model

While the CIR model provides closed-form formulas for zero-coupon bonds and European bond options, many practical applications require pricing path-dependent derivatives --- such as range accruals, barrier options on rates, or mortgage-backed securities --- for which no analytical solution exists. Monte Carlo simulation fills this gap by generating a large number of CIR rate paths and averaging discounted payoffs. This section develops the Monte Carlo framework for CIR bond pricing, presents variance reduction techniques that dramatically improve efficiency, and quantifies convergence through standard errors and confidence intervals.

---

## Monte Carlo bond pricing estimator

Under the risk-neutral measure $\mathbb{Q}$, the zero-coupon bond price is

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int_t^T r_s\,ds\right)\,\bigg|\,\mathcal{F}_t\right]
$$

The Monte Carlo estimator replaces the expectation with a sample average over $M$ independent paths:

$$
\hat{P}(t,T) = \frac{1}{M}\sum_{m=1}^{M}\exp\!\left(-\sum_{k=0}^{N-1} r_{t_k}^{(m)}\,\Delta t_k\right)
$$

where $r_{t_0}^{(m)}, r_{t_1}^{(m)}, \ldots, r_{t_N}^{(m)}$ is the $m$-th simulated path on the time grid $t = t_0 < t_1 < \cdots < t_N = T$, and $\Delta t_k = t_{k+1} - t_k$. The integral $\int_t^T r_s\,ds$ is approximated by the left-point Riemann sum; the trapezoidal rule

$$
\int_t^T r_s\,ds \approx \sum_{k=0}^{N-1}\frac{r_{t_k}^{(m)} + r_{t_{k+1}}^{(m)}}{2}\,\Delta t_k
$$

provides higher-order accuracy for smooth paths.

---

## Path generation

Each path is generated using one of the simulation schemes from the exact simulation section:

1. **Exact simulation**: At each step, sample $r_{t_{k+1}} \mid r_{t_k}$ from the non-central chi-squared distribution. No discretization bias.
2. **Euler with truncation**: Use the Euler-Maruyama recursion with full truncation to prevent negative rates. Simple but biased.

For bond pricing, exact simulation is strongly preferred because it eliminates the systematic bias from time discretization, leaving only the statistical error from finite sample size.

### Time grid design

The time grid should include:

- All payoff observation dates (coupon dates, barrier monitoring dates)
- Sufficient intermediate points for accurate integral approximation
- For exact simulation, only the dates needed by the payoff (minimal grid)

!!! tip "Minimal grids with exact simulation"
    Since exact simulation produces the correct conditional distribution regardless of step size, a zero-coupon bond price can be estimated with a single time step from $t$ to $T$ if only the terminal discount factor $e^{-\int_t^T r_s\,ds}$ is needed. However, approximating the integral requires intermediate points. A grid of 50--100 steps per year typically suffices for bond pricing.

---

## Standard error and confidence intervals

The sample mean $\hat{P}$ has standard error

$$
\text{SE} = \frac{\hat{s}}{\sqrt{M}}
$$

where $\hat{s}^2 = \frac{1}{M-1}\sum_{m=1}^M(Y_m - \hat{P})^2$ and $Y_m = \exp(-\sum_k r_{t_k}^{(m)}\Delta t_k)$. An approximate 95% confidence interval is

$$
\hat{P} \pm 1.96\,\frac{\hat{s}}{\sqrt{M}}
$$

By the central limit theorem, the error decreases as $O(1/\sqrt{M})$: halving the standard error requires quadrupling the number of paths.

---

## Variance reduction techniques

### Antithetic variates

For each path generated with random inputs $Z_1, Z_2, \ldots, Z_N$, generate a second path using $-Z_1, -Z_2, \ldots, -Z_N$. The antithetic estimator is

$$
\hat{P}_{\text{anti}} = \frac{1}{M}\sum_{m=1}^{M}\frac{Y_m + Y_m'}{2}
$$

where $Y_m'$ is the discount factor from the antithetic path. Since the CIR discount factor is a convex function of the driving noise (through the exponential), $Y_m$ and $Y_m'$ are negatively correlated, and the variance of the average $(Y_m + Y_m')/2$ is less than the variance of $Y_m$ alone.

**Variance reduction factor**: Typically 30--60% for bond pricing.

### Control variates

Use the known closed-form bond price $P^{\text{exact}}(t,T)$ as a control. For each path $m$, define

$$
\hat{Y}_m^{\text{CV}} = Y_m - \beta\left(\bar{r}^{(m)} - \mathbb{E}^{\mathbb{Q}}[\bar{r}]\right)
$$

where $\bar{r}^{(m)} = \frac{1}{N}\sum_k r_{t_k}^{(m)}$ is the average rate along path $m$, and $\beta$ is the optimal control coefficient estimated by regression. The conditional mean $\mathbb{E}^{\mathbb{Q}}[\bar{r}]$ can be computed from the CIR moment formulas:

$$
\mathbb{E}^{\mathbb{Q}}[r_s\,|\,r_t] = r_t\,e^{-\kappa(s-t)} + \theta(1 - e^{-\kappa(s-t)})
$$

**Variance reduction factor**: Typically 80--95% for bond pricing, making it the most effective single technique.

### Combined approach

Antithetic variates and control variates can be combined: first generate antithetic pairs, then apply the control variate correction to each pair average. The combined reduction is multiplicative, often achieving 90--98% variance reduction.

---

## Pricing path-dependent derivatives

Monte Carlo is indispensable for derivatives whose payoffs depend on the entire rate path.

### Example: discretely monitored range accrual

A range accrual note pays a coupon proportional to the fraction of fixing dates on which the rate falls within a range $[L, U]$:

$$
\text{Payoff} = N\,c\,\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}_{\{L \leq r_{T_i} \leq U\}}
$$

The Monte Carlo price is

$$
V(0) = \frac{1}{M}\sum_{m=1}^{M}\exp\!\left(-\sum_k r_{t_k}^{(m)}\Delta t_k\right)\cdot Nc\,\frac{1}{n}\sum_{i=1}^{n}\mathbf{1}_{\{L \leq r_{T_i}^{(m)} \leq U\}}
$$

No closed-form solution exists for this product under CIR, making Monte Carlo the standard approach.

### Example: interest rate cap with discrete monitoring

While individual caplets have closed-form CIR prices, a cap with knock-out barriers or path-dependent features requires Monte Carlo:

$$
\text{Caplet}_i^{\text{KO}} = N\delta_i(L(T_i, T_{i+1}) - K)^+\,\mathbf{1}_{\{r_s < H \;\forall\; s \in [0, T_i]\}}
$$

The knock-out condition requires monitoring the rate path, which is naturally handled by path simulation.

---

## Convergence verification

A reliable Monte Carlo implementation should be verified against known analytical results before being applied to exotic products.

**Verification protocol**:

1. Price a zero-coupon bond using MC and compare to the closed-form CIR formula
2. Price a European bond option using MC and compare to the chi-squared formula
3. For each test, verify that the closed-form price falls within the 95% confidence interval
4. Check that the standard error scales as $O(1/\sqrt{M})$ by doubling $M$

| $M$ (paths) | $\hat{P}(0,5)$ | SE | 95% CI | $P^{\text{exact}}$ |
|:-----------:|:---------------:|:---:|:------:|:------------------:|
| 1,000 | 0.7685 | 0.0028 | [0.7630, 0.7740] | 0.7700 |
| 10,000 | 0.7703 | 0.0009 | [0.7685, 0.7721] | 0.7700 |
| 100,000 | 0.7699 | 0.0003 | [0.7693, 0.7705] | 0.7700 |

The exact price falls within all three confidence intervals, and the SE decreases by a factor of $\approx \sqrt{10}$ with each 10-fold increase in $M$.

---

## Summary

Monte Carlo simulation for the CIR model combines path generation (preferably exact via non-central chi-squared sampling) with discounted payoff averaging. The method converges at rate $O(1/\sqrt{M})$, with standard errors quantifying the statistical uncertainty. Antithetic variates provide 30--60% variance reduction, while control variates using the known CIR moments achieve 80--95% reduction. For path-dependent derivatives --- range accruals, barrier products, callable bonds --- Monte Carlo is the only feasible pricing approach. Verification against closed-form bond and option prices should always precede application to exotic products.
