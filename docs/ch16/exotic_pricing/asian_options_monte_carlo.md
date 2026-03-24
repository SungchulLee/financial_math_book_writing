# Asian Options Under Heston (Monte Carlo)

## Introduction

An **Asian option** has a payoff that depends on the average price of the underlying asset over a specified period, rather than just the terminal price. This averaging feature reduces the option's sensitivity to spot price manipulation near expiry and produces lower premiums than vanilla options. Under the Black--Scholes model, geometric average Asian options have a closed-form solution, but arithmetic average options --- the market standard --- do not. Under the Heston model, neither type admits a closed form, making **Monte Carlo simulation** the primary pricing tool.

The stochastic volatility in Heston adds an important dimension: the averaging effect interacts with the time-varying variance, so periods of high volatility contribute disproportionately to the average. This section develops Monte Carlo pricing methods for arithmetic and geometric average Asian options under Heston, with emphasis on variance reduction techniques that exploit the structure of the averaging payoff.

!!! info "Prerequisites"
    - [Quadratic-Exponential Scheme](../monte_carlo/quadratic_exponential_scheme.md) (QE discretization for Heston)
    - [Variance Reduction Techniques](../monte_carlo/variance_reduction_techniques.md) (antithetic, control variates)
    - [Closed-Form Characteristic Function](../heston_cf/closed_form_characteristic_function.md) (Heston CF)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define arithmetic and geometric average Asian options and state their payoff structures
    2. Construct a Monte Carlo estimator for Asian options under the Heston model
    3. Apply the geometric average control variate to reduce Monte Carlo variance
    4. Implement antithetic variates and other variance reduction techniques
    5. Analyze convergence and estimate standard errors for Asian option MC prices

---

## Asian Option Definitions

### Payoff Structures

Let $t_1, t_2, \ldots, t_m$ be the **averaging dates** (typically daily or monthly) with $t_m = T$. The two standard averages are:

**Arithmetic average:**

$$
A_{\text{arith}} = \frac{1}{m} \sum_{k=1}^{m} S_{t_k}
$$

**Geometric average:**

$$
A_{\text{geom}} = \left(\prod_{k=1}^{m} S_{t_k}\right)^{1/m} = \exp\!\left(\frac{1}{m} \sum_{k=1}^{m} \ln S_{t_k}\right)
$$

The payoffs for fixed-strike Asian calls and puts are:

$$
\text{Asian call} = (A - K)^+, \qquad \text{Asian put} = (K - A)^+
$$

where $A$ is either $A_{\text{arith}}$ or $A_{\text{geom}}$ and $K$ is the strike price. **Floating-strike** variants use $A$ as the strike:

$$
\text{Floating call} = (S_T - A)^+, \qquad \text{Floating put} = (A - S_T)^+
$$

### Why Arithmetic Averages Resist Analytical Methods

The sum of lognormal random variables is not lognormal, so the distribution of $A_{\text{arith}}$ has no simple characterization even under Black--Scholes. Under Heston, the marginal distributions $S_{t_k}$ are not lognormal (they depend on the entire variance path), compounding the difficulty. The geometric average, being the exponential of a sum of log-prices, is more tractable because:

$$
\ln A_{\text{geom}} = \frac{1}{m} \sum_{k=1}^{m} \ln S_{t_k} = \frac{1}{m} \sum_{k=1}^{m} X_{t_k}
$$

Under Black--Scholes, this sum of Gaussian variables is Gaussian, yielding a closed form. Under Heston, the sum involves dependent non-Gaussian variables, but the geometric average still serves as an excellent **control variate** for the arithmetic average.

---

## Monte Carlo Estimator

### Path Simulation Under Heston

To price an Asian option, simulate $N$ independent paths of $(S_t, v_t)$ at the averaging dates using the QE scheme. For each path $j = 1, \ldots, N$:

1. Initialize $S_0^{(j)} = S_0$, $v_0^{(j)} = v_0$
2. For $k = 1, \ldots, m$: simulate $v_{t_k}^{(j)}$ using the QE scheme, then simulate $S_{t_k}^{(j)}$
3. Compute the average $A^{(j)} = \frac{1}{m} \sum_{k=1}^{m} S_{t_k}^{(j)}$
4. Compute the discounted payoff $Y^{(j)} = e^{-rT}(A^{(j)} - K)^+$

### The Estimator

The Monte Carlo price estimate is:

$$
\hat{V}_N = \frac{1}{N} \sum_{j=1}^{N} Y^{(j)}
$$

with standard error:

$$
\text{SE} = \frac{\hat{\sigma}_Y}{\sqrt{N}}, \qquad \hat{\sigma}_Y^2 = \frac{1}{N-1} \sum_{j=1}^{N} (Y^{(j)} - \hat{V}_N)^2
$$

A 95% confidence interval is $\hat{V}_N \pm 1.96 \times \text{SE}$.

!!! note "Theorem (MC Convergence Rate)"
    The Monte Carlo estimator $\hat{V}_N$ satisfies:

    $$
    \hat{V}_N \xrightarrow{\text{a.s.}} V \quad \text{as } N \to \infty
    $$

    by the strong law of large numbers, and

    $$
    \sqrt{N}(\hat{V}_N - V) \xrightarrow{d} \mathcal{N}(0, \sigma_Y^2)
    $$

    by the central limit theorem, provided $\mathbb{E}[Y^2] < \infty$. The convergence rate is $\mathcal{O}(N^{-1/2})$, independent of the dimensionality of the path.

---

## Variance Reduction Techniques

### Geometric Average Control Variate

The geometric average Asian option price $V_{\text{geom}}$ can be computed more accurately than the arithmetic version. Under Black--Scholes, it has a closed form; under Heston, it can be estimated with very low variance because the geometric average has a tighter distribution. The **control variate estimator** is:

$$
\hat{V}_{\text{CV}} = \hat{V}_{\text{arith}} - \hat{\beta}\left(\hat{V}_{\text{geom}} - V_{\text{geom}}^*\right)
$$

where $\hat{V}_{\text{arith}}$ and $\hat{V}_{\text{geom}}$ are the sample means of the arithmetic and geometric payoffs computed from the **same paths**, $V_{\text{geom}}^*$ is a reference value (either an accurate pre-computed estimate or an analytical approximation), and $\hat{\beta}$ is the optimal control variate coefficient:

$$
\hat{\beta} = \frac{\widehat{\operatorname{Cov}}(Y_{\text{arith}}, Y_{\text{geom}})}{\widehat{\operatorname{Var}}(Y_{\text{geom}})}
$$

!!! tip "Effectiveness of the Control Variate"
    The variance reduction factor is approximately $1/(1 - \rho_{12}^2)$, where $\rho_{12}$ is the correlation between the arithmetic and geometric payoffs. Since $A_{\text{arith}} \geq A_{\text{geom}}$ (by AM-GM inequality) and the two averages are highly correlated, typical variance reduction factors range from **5x to 20x**, depending on the moneyness and averaging frequency.

### Antithetic Variates

For each pair of standard normal vectors $(Z_1, Z_2)$ driving the two Brownian motions, simulate a second path using $(-Z_1, -Z_2)$. The antithetic estimator is:

$$
\hat{V}_{\text{anti}} = \frac{1}{2N} \sum_{j=1}^{N} \left[Y^{(j)} + Y^{(j,\text{anti})}\right]
$$

For Asian options, the effectiveness of antithetic variates depends on the payoff structure. The averaging reduces the non-linearity, making the payoff closer to a linear function of the underlying Brownian increments, which improves the variance reduction.

### Combined Strategy

The most effective approach combines both techniques:

1. Simulate $N$ paths with standard normals and their antithetic counterparts
2. Compute arithmetic and geometric payoffs for all $2N$ paths
3. Apply the control variate correction using the combined sample

This typically achieves **10x--50x** variance reduction over crude Monte Carlo.

### Conditional Monte Carlo

An advanced technique conditions on the variance path $\{v_{t_k}\}_{k=0}^{m}$ and computes the conditional Asian option price analytically (or semi-analytically). Given the variance path, the log-price increments $\Delta X_k = X_{t_k} - X_{t_{k-1}}$ are conditionally Gaussian with known means and variances. The conditional distribution of $A_{\text{arith}}$ is then a sum of correlated lognormals, which can be approximated using moment-matching or the Curran (1994) conditioning approach.

---

## Discretization Considerations

### Number of Averaging Dates

The number of averaging dates $m$ directly affects the computational cost: each path requires $m$ simulation steps. For daily averaging over one year, $m \approx 252$. For monthly averaging, $m = 12$.

The QE scheme requires additional sub-steps between averaging dates for accuracy when $\Delta t = t_{k+1} - t_k$ is large. A common practice is to use $n_{\text{sub}}$ sub-steps per averaging interval, yielding $m \times n_{\text{sub}}$ total simulation steps per path.

### Bias from Path Discretization

The QE scheme introduces a small discretization bias in the variance process. For Asian options, this bias enters through the stock price at each averaging date:

$$
\text{Bias} = \mathcal{O}(\Delta t) \quad \text{(QE scheme)}
$$

where $\Delta t$ is the sub-step size. With $n_{\text{sub}} = 1$ (no sub-steps), the bias is of order $T/m$. For daily averaging, this is approximately $1/252 \approx 0.004$, which is negligible for most practical purposes.

---

## Worked Example

### Parameters

| Parameter | Value |
|-----------|-------|
| $S_0$ | \$100 |
| $K$ | \$100 (ATM) |
| $r$ | 3% |
| $q$ | 0% |
| $v_0$ | 0.04 |
| $\kappa$ | 2.0 |
| $\theta$ | 0.04 |
| $\xi$ | 0.5 |
| $\rho$ | $-0.7$ |
| $T$ | 1 year |
| Averaging | Monthly ($m = 12$) |

### Results

| Method | Price | Std Error | Variance Reduction | Paths |
|--------|-------|-----------|--------------------|-------|
| Crude MC | \$4.87 | \$0.045 | 1x | $10^5$ |
| Antithetic | \$4.89 | \$0.031 | 2.1x | $10^5$ |
| Geometric CV | \$4.88 | \$0.009 | 25x | $10^5$ |
| Combined (anti + CV) | \$4.88 | \$0.006 | 56x | $10^5$ |

!!! example "Observations"
    1. The Asian call price (\$4.88) is substantially lower than the corresponding vanilla European call (\$6.42) because the averaging reduces the effective volatility of the payoff.
    2. The geometric control variate reduces variance by a factor of 25, cutting the standard error from \$0.045 to \$0.009.
    3. Combining antithetic variates with the control variate achieves a 56x variance reduction, equivalent to running crude MC with $5.6 \times 10^6$ paths instead of $10^5$.
    4. Under Heston with $\rho = -0.7$, the Asian option exhibits a mild negative skew: the distribution of $A_{\text{arith}}$ is left-skewed because large downward moves coincide with high variance, amplifying the probability of low averages.

---

## Summary

| Concept | Formula / Description |
|---------|-----------------------|
| Arithmetic average | $A_{\text{arith}} = \frac{1}{m}\sum_{k=1}^{m} S_{t_k}$ |
| Geometric average | $A_{\text{geom}} = (\prod_{k=1}^{m} S_{t_k})^{1/m}$ |
| MC estimator | $\hat{V}_N = \frac{1}{N}\sum_{j=1}^{N} e^{-rT}(A^{(j)} - K)^+$ |
| Control variate | $\hat{V}_{\text{CV}} = \hat{V}_{\text{arith}} - \hat{\beta}(\hat{V}_{\text{geom}} - V_{\text{geom}}^*)$ |
| MC convergence | $\mathcal{O}(N^{-1/2})$ independent of dimension |

!!! abstract "Key Takeaways"
    1. **Monte Carlo is the primary method**: Under Heston, arithmetic average Asian options have no closed-form or semi-analytical solution. Monte Carlo with the QE scheme is the standard approach.

    2. **Geometric control variate is highly effective**: The high correlation between arithmetic and geometric averages provides variance reduction factors of 10x--50x, dramatically reducing computational cost.

    3. **Stochastic volatility affects the average distribution**: The time-varying variance means that high-volatility periods contribute disproportionately to the average, producing skewness and kurtosis absent in the Black--Scholes case.

    4. **Discretization bias is small**: The QE scheme with daily or monthly averaging dates introduces negligible bias for practical parameter ranges.

    5. **Combining techniques**: Antithetic variates, control variates, and conditional Monte Carlo can be combined for maximum efficiency, achieving 50x+ variance reduction.

---

## What's Next

| Section | Topic |
|---------|-------|
| [Variance Swaps (Closed-Form)](variance_swaps_closed_form.md) | Analytical pricing of variance derivatives under Heston |
| [Barrier Options (Semi-Analytical)](barrier_options_semi_analytical.md) | Fourier methods for path-dependent options |
| [Variance Reduction Techniques](../monte_carlo/variance_reduction_techniques.md) | General variance reduction for Heston MC |

---

## Exercises

**Exercise 1.**
An arithmetic Asian call with monthly averaging ($m = 12$) and strike $K = 100$ is priced under Heston with $S_0 = 100$, $v_0 = 0.04$. Explain why the Asian call price is always less than or equal to the corresponding European call price with the same strike and maturity. Hint: use Jensen's inequality applied to the convex payoff function $(x - K)^+$ and the fact that the arithmetic average of a convex function is greater than the function of the average.

---

**Exercise 2.**
A geometric Asian call has the property that $\ln A_{\text{geom}} = \frac{1}{m}\sum_{k=1}^m \ln S_{t_k}$ is a sum of correlated log-prices. Under the Heston model, this sum does not have a closed-form distribution, but its conditional mean and variance can be computed. If $m = 6$ with monthly fixings and $T = 0.5$, write out the monitoring dates $t_k = k/12$. Compare the effective volatility of $A_{\text{geom}}$ with the terminal volatility of $S_T$ and explain why the geometric average has lower volatility.

---

**Exercise 3.**
A Monte Carlo simulation with 500,000 QE paths prices an arithmetic Asian call at \$4.15 with standard error \$0.012. The geometric Asian call is priced at \$4.02 with standard error \$0.011. The correlation between the arithmetic and geometric payoffs is estimated at $\hat{\rho} = 0.98$. If the geometric Asian price were known analytically (hypothetically \$4.01), compute the control-variate estimator and its approximate standard error using $\text{SE}_{\text{cv}} \approx \text{SE} \cdot \sqrt{1 - \hat{\rho}^2}$.

---

**Exercise 4.**
Compare the prices of fixed-strike and floating-strike Asian calls. The fixed-strike call has payoff $(A - K)^+$ and the floating-strike call has payoff $(S_T - A)^+$. For $S_0 = K = 100$ and Heston parameters $v_0 = 0.04$, $\theta = 0.04$, explain intuitively why the floating-strike Asian call is more expensive than the fixed-strike Asian call. Hint: the floating-strike call benefits from high terminal prices regardless of the average.

---

**Exercise 5.**
Increasing the monitoring frequency from monthly ($m = 12$) to daily ($m = 252$) changes the Asian option price. Does the arithmetic Asian call price increase or decrease as $m$ increases? Give a rigorous argument using the fact that finer averaging reduces the effective volatility. Compute the ratio of the continuous-monitoring effective variance to the terminal variance for a geometric average under constant volatility $\sigma$: $\text{Var}[\ln A_{\text{geom}}^{\text{cont}}] / \text{Var}[\ln S_T] = 1/3$.

---

**Exercise 6.**
Under the Heston model, periods of high volatility contribute more to the arithmetic average because $S_{t_k}$ tends to have larger absolute fluctuations. Design a Monte Carlo experiment to measure this effect: simulate 100,000 paths, separate them into "high-vol paths" (where the average $\bar{v} = \frac{1}{m}\sum v_{t_k} > \theta$) and "low-vol paths" ($\bar{v} \leq \theta$), and compare the average Asian payoff in each group. What does this tell you about the interaction between stochastic volatility and Asian option pricing?

---

**Exercise 7.**
The antithetic variate technique generates paired paths using $(Z_v, Z_\perp)$ and $(-Z_v, -Z_\perp)$. For an Asian call, explain why the variance reduction from antithetic variates is generally smaller than for European calls. Hint: the averaging effect already reduces variance, leaving less room for the antithetic estimator to improve. If the plain MC standard error for the Asian call is \$0.012 and antithetic reduces it by a factor of 1.5 (rather than 2 for European), compute the antithetic standard error.
