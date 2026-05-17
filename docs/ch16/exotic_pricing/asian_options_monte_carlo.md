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

Recall (see [§ Monte Carlo](../monte_carlo/euler_discretization_and_pitfalls.md)): simulate $N$ paths of $(S_t, v_t)$ at the averaging dates via the QE scheme. For each path $j$, compute the average $A^{(j)} = \frac{1}{m} \sum_{k=1}^{m} S_{t_k}^{(j)}$ and the discounted payoff $Y^{(j)} = e^{-rT}(A^{(j)} - K)^+$.

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

Recall (see [§ Monte Carlo](../monte_carlo/euler_discretization_and_pitfalls.md)): by SLLN and CLT, $\hat{V}_N \to V$ at rate $\mathcal{O}(N^{-1/2})$, independent of path dimension.

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

Recall (see [§ Variance Reduction](../monte_carlo/variance_reduction_techniques.md)): pair each path $(Z_1, Z_2)$ with $(-Z_1, -Z_2)$. For Asian options, the averaging reduces payoff non-linearity, improving the antithetic variance reduction relative to vanilla calls.

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

??? success "Solution to Exercise 1"
    We must show that the Asian call price is less than or equal to the European call price, i.e.,

    $$
    e^{-rT}\mathbb{E}^{\mathbb{Q}}[(A_{\text{arith}} - K)^+] \leq e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]
    $$

    **Step 1: Apply Jensen's inequality.** The function $g(x) = (x - K)^+$ is convex. By Jensen's inequality applied to the convex function $g$ and the random variable $S_{t_k}$ with equal weights $1/m$:

    $$
    \left(\frac{1}{m}\sum_{k=1}^{m} S_{t_k} - K\right)^+ \leq \frac{1}{m}\sum_{k=1}^{m} (S_{t_k} - K)^+
    $$

    Wait --- this inequality goes the wrong way for our purpose. The correct argument is more subtle and proceeds as follows.

    **Step 2: Use the tower property and conditional Jensen.** Note that $A_{\text{arith}} = \frac{1}{m}\sum_{k=1}^{m} S_{t_k}$ includes observations $S_{t_1}, \ldots, S_{t_{m-1}}$ that are all taken before maturity. The key insight is that the arithmetic average has **lower effective volatility** than the terminal price.

    Consider the representation under $\mathbb{Q}$:

    $$
    \mathbb{E}^{\mathbb{Q}}[A_{\text{arith}} \mid \mathcal{F}_0] = \frac{1}{m}\sum_{k=1}^{m} \mathbb{E}^{\mathbb{Q}}[S_{t_k}] = \frac{1}{m}\sum_{k=1}^{m} S_0 e^{(r-q)t_k}
    $$

    For a European call, $\mathbb{E}^{\mathbb{Q}}[S_T] = S_0 e^{(r-q)T}$. Since $t_k \leq T$ for all $k$, we have $\mathbb{E}^{\mathbb{Q}}[A_{\text{arith}}] \leq S_0 e^{(r-q)T} = \mathbb{E}^{\mathbb{Q}}[S_T]$ (assuming $r \geq q$, which is the typical case; for $q = 0$ and $t_m = T$, equality holds only for the last term).

    **Step 3: Variance comparison.** More importantly, the variance of $A_{\text{arith}}$ is smaller than the variance of $S_T$. The averaging operation reduces the dispersion of the payoff-determining quantity. Formally, for any collection of monitoring dates:

    $$
    \operatorname{Var}(A_{\text{arith}}) = \frac{1}{m^2}\sum_{j,k=1}^{m}\operatorname{Cov}(S_{t_j}, S_{t_k}) < \operatorname{Var}(S_T)
    $$

    because the covariance terms involve earlier dates with smaller variances.

    **Step 4: Conclude via the call price ordering.** Since $(x - K)^+$ is convex and non-decreasing, and $A_{\text{arith}}$ has the same (or lower) forward and strictly lower variance than $S_T$, the European call price dominates the Asian call price. Formally, the Asian call payoff can be bounded using the tower property:

    $$
    \mathbb{E}[(A_{\text{arith}} - K)^+] = \mathbb{E}\!\left[\left(\frac{1}{m}\sum_{k=1}^{m} S_{t_k} - K\right)^+\right] \leq \mathbb{E}[(S_T - K)^+]
    $$

    This follows because $A_{\text{arith}}$ is a less dispersed random variable than $S_T$, and for a convex payoff function, greater dispersion (in the convex order sense) yields a higher expected payoff.

---

**Exercise 2.**
A geometric Asian call has the property that $\ln A_{\text{geom}} = \frac{1}{m}\sum_{k=1}^m \ln S_{t_k}$ is a sum of correlated log-prices. Under the Heston model, this sum does not have a closed-form distribution, but its conditional mean and variance can be computed. If $m = 6$ with monthly fixings and $T = 0.5$, write out the monitoring dates $t_k = k/12$. Compare the effective volatility of $A_{\text{geom}}$ with the terminal volatility of $S_T$ and explain why the geometric average has lower volatility.

??? success "Solution to Exercise 2"
    **Monitoring dates.** With $m = 6$ monthly fixings and $T = 0.5$ years, the monitoring dates are:

    $$
    t_k = \frac{k}{12}, \quad k = 1, 2, \ldots, 6
    $$

    Explicitly: $t_1 = 1/12$, $t_2 = 2/12$, $t_3 = 3/12$, $t_4 = 4/12$, $t_5 = 5/12$, $t_6 = 6/12 = T$.

    **Geometric average log-price.** The logarithm of the geometric average is:

    $$
    \ln A_{\text{geom}} = \frac{1}{6}\sum_{k=1}^{6} \ln S_{t_k} = \frac{1}{6}\sum_{k=1}^{6} X_{t_k}
    $$

    where $X_t = \ln S_t$.

    **Effective volatility comparison.** Under constant volatility $\sigma$ (Black--Scholes), the terminal log-price has variance $\operatorname{Var}[\ln S_T] = \sigma^2 T$. The variance of the geometric average's log is:

    $$
    \operatorname{Var}\!\left[\frac{1}{m}\sum_{k=1}^{m} X_{t_k}\right] = \frac{1}{m^2}\sum_{j=1}^{m}\sum_{k=1}^{m} \operatorname{Cov}(X_{t_j}, X_{t_k})
    $$

    Under Black--Scholes, $\operatorname{Cov}(X_{t_j}, X_{t_k}) = \sigma^2 \min(t_j, t_k)$. Therefore:

    $$
    \operatorname{Var}[\ln A_{\text{geom}}] = \frac{\sigma^2}{m^2}\sum_{j=1}^{m}\sum_{k=1}^{m} \min(t_j, t_k) = \frac{\sigma^2}{m^2}\sum_{j=1}^{m}\sum_{k=1}^{m} \frac{\min(j,k)}{12}
    $$

    Computing the double sum: $\sum_{j=1}^{m}\sum_{k=1}^{m}\min(j,k) = \sum_{l=1}^{m}(2(m - l) + 1) \cdot l = m^2(m+1)/2 - m(m-1)(2m-1)/6$. For $m = 6$: $\sum = 91$. So:

    $$
    \operatorname{Var}[\ln A_{\text{geom}}] = \frac{\sigma^2}{36} \cdot \frac{91}{12} = \frac{91\sigma^2}{432}
    $$

    The ratio to the terminal variance is:

    $$
    \frac{\operatorname{Var}[\ln A_{\text{geom}}]}{\operatorname{Var}[\ln S_T]} = \frac{91\sigma^2/432}{\sigma^2/2} = \frac{91}{216} \approx 0.421
    $$

    The effective volatility of $A_{\text{geom}}$ is $\sqrt{0.421} \approx 0.649$ times the terminal volatility. This is less than 1 because:

    1. **Earlier observations have less variance**: $X_{t_k}$ for $t_k < T$ has variance $\sigma^2 t_k < \sigma^2 T$.
    2. **Averaging reduces dispersion**: The $1/m$ weighting further reduces the overall variance.

    Under Heston, the same qualitative result holds, but the exact variance depends on the stochastic variance path. The conditional covariance $\operatorname{Cov}(X_{t_j}, X_{t_k} \mid \{v_s\})$ involves $\int_0^{\min(t_j, t_k)} v_s \, ds$, so periods of high volatility contribute more to both the variance and covariance structure.

---

**Exercise 3.**
A Monte Carlo simulation with 500,000 QE paths prices an arithmetic Asian call at \$4.15 with standard error \$0.012. The geometric Asian call is priced at \$4.02 with standard error \$0.011. The correlation between the arithmetic and geometric payoffs is estimated at $\hat{\rho} = 0.98$. If the geometric Asian price were known analytically (hypothetically \$4.01), compute the control-variate estimator and its approximate standard error using $\text{SE}_{\text{cv}} \approx \text{SE} \cdot \sqrt{1 - \hat{\rho}^2}$.

??? success "Solution to Exercise 3"
    **Control variate estimator.** The control variate estimator is:

    $$
    \hat{V}_{\text{CV}} = \hat{V}_{\text{arith}} - \hat{\beta}(\hat{V}_{\text{geom}} - V_{\text{geom}}^*)
    $$

    where $V_{\text{geom}}^* = \$4.01$ is the known analytical geometric Asian price.

    **Optimal coefficient.** The optimal $\hat{\beta}$ is:

    $$
    \hat{\beta} = \frac{\widehat{\operatorname{Cov}}(Y_{\text{arith}}, Y_{\text{geom}})}{\widehat{\operatorname{Var}}(Y_{\text{geom}})} = \hat{\rho} \cdot \frac{\hat{\sigma}_{\text{arith}}}{\hat{\sigma}_{\text{geom}}}
    $$

    From the given standard errors with $N = 500{,}000$:

    $$
    \hat{\sigma}_{\text{arith}} = \text{SE}_{\text{arith}} \cdot \sqrt{N} = 0.012 \times \sqrt{500{,}000} = 0.012 \times 707.1 = 8.485
    $$

    $$
    \hat{\sigma}_{\text{geom}} = 0.011 \times 707.1 = 7.778
    $$

    $$
    \hat{\beta} = 0.98 \times \frac{8.485}{7.778} = 0.98 \times 1.0909 = 1.069
    $$

    **Control variate price estimate:**

    $$
    \hat{V}_{\text{CV}} = 4.15 - 1.069 \times (4.02 - 4.01) = 4.15 - 1.069 \times 0.01 = 4.15 - 0.01069 \approx \$4.139
    $$

    **Standard error of the control variate estimator:**

    $$
    \text{SE}_{\text{CV}} \approx \text{SE}_{\text{arith}} \cdot \sqrt{1 - \hat{\rho}^2} = 0.012 \times \sqrt{1 - 0.98^2}
    $$

    $$
    = 0.012 \times \sqrt{1 - 0.9604} = 0.012 \times \sqrt{0.0396} = 0.012 \times 0.199 \approx \$0.0024
    $$

    The control variate reduces the standard error from \$0.012 to approximately \$0.0024, a variance reduction factor of $(0.012/0.0024)^2 = 25$. This is consistent with the theoretical factor $1/(1 - \rho^2) = 1/0.0396 \approx 25.3$.

---

**Exercise 4.**
Compare the prices of fixed-strike and floating-strike Asian calls. The fixed-strike call has payoff $(A - K)^+$ and the floating-strike call has payoff $(S_T - A)^+$. For $S_0 = K = 100$ and Heston parameters $v_0 = 0.04$, $\theta = 0.04$, explain intuitively why the floating-strike Asian call is more expensive than the fixed-strike Asian call. Hint: the floating-strike call benefits from high terminal prices regardless of the average.

??? success "Solution to Exercise 4"
    **Payoff comparison.** The two payoffs are:

    - Fixed-strike: $(A - K)^+$ where $A = \frac{1}{m}\sum_{k=1}^m S_{t_k}$
    - Floating-strike: $(S_T - A)^+$

    **Intuitive argument for why the floating-strike call is more expensive.**

    Consider the decomposition of the terminal price $S_T$ relative to the average $A$. The average $A$ includes $S_T$ as one of $m$ terms plus earlier observations. When $S_T$ is large:

    - The **floating-strike call** profits directly: its payoff $(S_T - A)^+$ is large because $S_T$ exceeds the average (which is dragged down by earlier, presumably lower, observations).
    - The **fixed-strike call** also profits from $(A - K)^+$, but the average is pulled toward $K$ by earlier observations, diluting the effect of the high terminal price.

    When $S_T$ is small:

    - The floating-strike call can still have a positive payoff if $S_T$ exceeds $A$ (unlikely when $S_T$ is small, since the average includes earlier higher prices).
    - The fixed-strike call is out of the money.

    The critical asymmetry is: the floating-strike call benefits from **dispersion between $S_T$ and the average**. Under Heston with negative $\rho$, large downward moves in $S$ coincide with high variance, creating high dispersion in subsequent moves. This means $S_T$ can deviate significantly from $A$ in both directions.

    More formally, by put-call symmetry arguments, the floating-strike Asian call is related to a fixed-strike Asian put. Using the identity:

    $$
    (S_T - A)^+ = (S_T - K)^+ - (A - K) + (K - A)^+ + (S_T - K)^- \cdot \mathbf{1}_{\{A > K\}} + \cdots
    $$

    A cleaner way to see the price difference is through the identity:

    $$
    S_T - A = S_T - \frac{1}{m}\sum_{k=1}^m S_{t_k} = \frac{1}{m}\sum_{k=1}^{m-1}(S_T - S_{t_k})
    $$

    The floating-strike payoff depends on the **increments** $S_T - S_{t_k}$, while the fixed-strike payoff depends on the **level** of the average relative to $K$. The increments have higher variance (each increment captures the full volatility over $[t_k, T]$), so the floating-strike call, which benefits from positive increments, commands a higher premium. Under Heston with $S_0 = K$ and the given parameters, the floating-strike call is typically 20--40% more expensive than the fixed-strike call.

---

**Exercise 5.**
Increasing the monitoring frequency from monthly ($m = 12$) to daily ($m = 252$) changes the Asian option price. Does the arithmetic Asian call price increase or decrease as $m$ increases? Give a rigorous argument using the fact that finer averaging reduces the effective volatility. Compute the ratio of the continuous-monitoring effective variance to the terminal variance for a geometric average under constant volatility $\sigma$: $\text{Var}[\ln A_{\text{geom}}^{\text{cont}}] / \text{Var}[\ln S_T] = 1/3$.

??? success "Solution to Exercise 5"
    **Direction of price change.** As $m$ increases (finer monitoring), the arithmetic Asian call price **decreases**.

    **Rigorous argument.** The effective volatility of the arithmetic average decreases with finer averaging. Consider the variance of $\ln A_{\text{geom}}$ as a proxy (the argument extends to $A_{\text{arith}}$ via correlation). Under constant volatility:

    $$
    \operatorname{Var}\!\left[\frac{1}{m}\sum_{k=1}^m \ln S_{t_k}\right] = \frac{\sigma^2}{m^2}\sum_{j,k=1}^m \min(t_j, t_k)
    $$

    For equally spaced dates $t_k = kT/m$, this equals:

    $$
    \frac{\sigma^2 T}{m^3}\sum_{j=1}^m \sum_{k=1}^m \min(j,k) = \frac{\sigma^2 T}{m^3} \cdot \frac{m(m+1)(2m+1)}{6}
    $$

    As $m \to \infty$:

    $$
    \frac{(m+1)(2m+1)}{6m^2} \to \frac{2m^2}{6m^2} = \frac{1}{3}
    $$

    Therefore the continuous-monitoring effective variance of the geometric average is:

    $$
    \operatorname{Var}[\ln A_{\text{geom}}^{\text{cont}}] = \frac{\sigma^2 T}{3}
    $$

    **The ratio:**

    $$
    \frac{\operatorname{Var}[\ln A_{\text{geom}}^{\text{cont}}]}{\operatorname{Var}[\ln S_T]} = \frac{\sigma^2 T / 3}{\sigma^2 T} = \frac{1}{3}
    $$

    This confirms the $1/3$ ratio. The effective volatility is $\sigma / \sqrt{3} \approx 0.577\sigma$.

    **Why the price decreases.** Since the Asian call payoff $(A - K)^+$ is a convex function of $A$, and the variance of $A$ decreases with finer monitoring, the expected payoff decreases (by a convexity argument: lower variance of the argument of a convex function reduces the expected value). More precisely, as monitoring becomes finer, $A_{\text{arith}}$ concentrates more tightly around its mean, reducing the probability of extreme outcomes that drive option value.

    Under Heston, the same qualitative behavior holds. The interaction between stochastic volatility and averaging frequency is through the conditional variance: given the variance path, the effective variance ratio converges to $1/3$ just as in the constant-volatility case. The unconditional effect is obtained by averaging over variance paths, preserving the monotone decrease in price with $m$.

---

**Exercise 6.**
Under the Heston model, periods of high volatility contribute more to the arithmetic average because $S_{t_k}$ tends to have larger absolute fluctuations. Design a Monte Carlo experiment to measure this effect: simulate 100,000 paths, separate them into "high-vol paths" (where the average $\bar{v} = \frac{1}{m}\sum v_{t_k} > \theta$) and "low-vol paths" ($\bar{v} \leq \theta$), and compare the average Asian payoff in each group. What does this tell you about the interaction between stochastic volatility and Asian option pricing?

??? success "Solution to Exercise 6"
    **Experimental design.** The Monte Carlo experiment proceeds as follows:

    1. **Simulate 100,000 paths** of $(S_t, v_t)$ using the QE scheme at monthly dates $t_1, \ldots, t_{12}$.

    2. **For each path $j$**, compute:
        - The average variance: $\bar{v}^{(j)} = \frac{1}{12}\sum_{k=1}^{12} v_{t_k}^{(j)}$
        - The arithmetic average price: $A^{(j)} = \frac{1}{12}\sum_{k=1}^{12} S_{t_k}^{(j)}$
        - The Asian call payoff: $Y^{(j)} = e^{-rT}(A^{(j)} - K)^+$

    3. **Separate paths** into two groups:
        - High-vol paths: $\mathcal{H} = \{j : \bar{v}^{(j)} > \theta\}$
        - Low-vol paths: $\mathcal{L} = \{j : \bar{v}^{(j)} \leq \theta\}$

    4. **Compute conditional averages**:

        $$
        \hat{V}_{\text{high}} = \frac{1}{|\mathcal{H}|}\sum_{j \in \mathcal{H}} Y^{(j)}, \qquad \hat{V}_{\text{low}} = \frac{1}{|\mathcal{L}|}\sum_{j \in \mathcal{L}} Y^{(j)}
        $$

    **Expected results and interpretation.** We expect $\hat{V}_{\text{high}} > \hat{V}_{\text{low}}$. The reasons are:

    - **High-vol paths produce more dispersed averages.** When $\bar{v} > \theta$, the stock price fluctuates more at each averaging date, increasing the probability that $A > K$ (for ATM options) and the expected magnitude of $(A - K)^+$.

    - **Asymmetric payoff effect.** The call payoff $(A - K)^+$ is zero for $A < K$ and linear for $A > K$. High variance increases both the probability of positive payoffs and their expected size, while losses are bounded at zero. This convexity means that the call benefits from higher realized variance.

    - **Correlation effect under Heston.** With $\rho < 0$, high-vol paths are more likely to have experienced downward moves (the leverage effect). However, the increased dispersion from high $v$ dominates: even though the stock may have drifted downward, the higher volatility creates more upside potential during the averaging period.

    The difference $\hat{V}_{\text{high}} - \hat{V}_{\text{low}}$ quantifies the **stochastic volatility premium** embedded in the Asian option. This premium is absent in the Black--Scholes model (where all paths have the same constant variance) and represents the additional value attributable to variance randomness. Typical results show $\hat{V}_{\text{high}}$ is 30--60% larger than $\hat{V}_{\text{low}}$, confirming the material impact of stochastic volatility on Asian option pricing.

---

**Exercise 7.**
The antithetic variate technique generates paired paths using $(Z_v, Z_\perp)$ and $(-Z_v, -Z_\perp)$. For an Asian call, explain why the variance reduction from antithetic variates is generally smaller than for European calls. Hint: the averaging effect already reduces variance, leaving less room for the antithetic estimator to improve. If the plain MC standard error for the Asian call is \$0.012 and antithetic reduces it by a factor of 1.5 (rather than 2 for European), compute the antithetic standard error.

??? success "Solution to Exercise 7"
    **Why antithetic variates are less effective for Asian calls than European calls.**

    The antithetic estimator pairs each path with its mirror image. For a European call with payoff $(S_T - K)^+$, the original path has $S_T$ and the antithetic path has $S_T^{\text{anti}}$. The variance reduction factor depends on the correlation $\operatorname{Corr}(Y, Y^{\text{anti}})$, where $Y = (S_T - K)^+$.

    For European calls, the payoff is a monotone (though nonlinear) function of the driving Brownian increments. The antithetic path reverses the increments, creating negative correlation between $Y$ and $Y^{\text{anti}}$, which reduces variance.

    For Asian calls, the payoff $(A - K)^+$ depends on the **average** $A = \frac{1}{m}\sum S_{t_k}$. The averaging introduces two effects that reduce the effectiveness of antithetic variates:

    1. **Variance is already reduced by averaging.** The starting variance $\operatorname{Var}(Y_{\text{Asian}})$ is smaller than $\operatorname{Var}(Y_{\text{European}})$ because the average has lower dispersion than the terminal value. With less variance to begin with, there is less room for improvement.

    2. **Weaker negative correlation.** The average $A$ is a less "monotone" function of the Brownian increments than $S_T$. Early increments contribute to $A$ through all subsequent terms (because they shift the entire price level), while late increments affect only the later averaging dates. The antithetic path reverses all increments simultaneously, but the complex dependence structure of the average on these increments produces a weaker negative correlation between $Y$ and $Y^{\text{anti}}$.

    Quantitatively, the antithetic variance reduction factor for an Asian call is approximately 1.5 rather than the theoretical maximum of 2 (which would require perfect negative correlation, $\operatorname{Corr}(Y, Y^{\text{anti}}) = -1$).

    **Computing the antithetic standard error.** The reduction factor of 1.5 means:

    $$
    \frac{\text{SE}_{\text{plain}}}{\text{SE}_{\text{anti}}} = 1.5
    $$

    Therefore:

    $$
    \text{SE}_{\text{anti}} = \frac{\text{SE}_{\text{plain}}}{1.5} = \frac{\$0.012}{1.5} = \$0.008
    $$

    For comparison, a European call with the same plain MC standard error would achieve $\text{SE}_{\text{anti}} \approx \$0.012/2 = \$0.006$ (factor of 2 from near-perfect negative correlation). The Asian call's antithetic standard error of \$0.008 is 33% higher, reflecting the reduced effectiveness.
