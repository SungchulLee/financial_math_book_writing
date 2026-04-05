# Asian Options

## Introduction

**Asian options** (also called **average-rate options**) are path-dependent derivatives whose payoff depends on the **average price** of the underlying asset over a specified period, rather than the terminal price alone. This averaging mechanism reduces the impact of price manipulation near expiry and stabilizes payoff variability, making Asian options natural hedging instruments for entities with continuous exposure to commodity or currency prices.

Asian options are among the most common exotic options in commodity and FX markets, where exposure accumulates gradually over time.

!!! info "Prerequisites"
    - [Black–Scholes Formula](../../ch06/black_scholes_formula/bs_formula_statement.md) (vanilla pricing baseline)
    - [Exotic Options Overview](exotic_options_overview.md) (classification of exotics)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Distinguish arithmetic and geometric average Asian options
    2. Write the payoff formulas for average-price and average-strike options
    3. Explain why arithmetic Asian options have no simple closed form
    4. Understand moment-matching and Monte Carlo pricing approaches

---

## Types of Asian Options

Asian options are classified along two dimensions: the **type of average** (arithmetic or geometric) and the **role of the average** in the payoff (average-price or average-strike).

### Average-Price vs. Average-Strike

An **average-price** option replaces the terminal price $S_T$ in the payoff with the average:

$$
\boxed{
\text{Average-price call payoff} = \left(\bar{S} - K\right)^+
}
$$

An **average-strike** option uses the average as the strike:

$$
\boxed{
\text{Average-strike call payoff} = \left(S_T - \bar{S}\right)^+
}
$$

where $\bar{S}$ denotes the average of the underlying price over the option's life.

### Arithmetic vs. Geometric Average

The **arithmetic average** is:

$$
\bar{S}_{\text{arith}} = \frac{1}{n}\sum_{i=1}^{n} S_{t_i} \quad \text{(discrete)}, \qquad \bar{S}_{\text{arith}} = \frac{1}{T}\int_0^T S_t\, dt \quad \text{(continuous)}
$$

The **geometric average** is:

$$
\bar{S}_{\text{geom}} = \left(\prod_{i=1}^{n} S_{t_i}\right)^{1/n} \quad \text{(discrete)}, \qquad \bar{S}_{\text{geom}} = \exp\left(\frac{1}{T}\int_0^T \ln S_t\, dt\right) \quad \text{(continuous)}
$$

| Average Type | Closed-Form Under GBM? | Practical Use |
|---|---|---|
| Geometric | Yes (lognormal distribution preserved) | Benchmark, control variate |
| Arithmetic | No (sum of lognormals is not lognormal) | Most common in practice |

---

## Pricing: The Fundamental Challenge

Under geometric Brownian motion, the arithmetic average $\bar{S}_{\text{arith}}$ is a **sum of correlated lognormal variables**, which does not have a lognormal distribution. This is why no simple closed-form formula exists for arithmetic Asian options—unlike vanilla options or geometric Asian options.

### Geometric Asian Options: Closed Form

For a continuous geometric average under GBM, the average $\bar{S}_{\text{geom}}$ is itself lognormally distributed. The geometric Asian call price is:

$$
C_{\text{geom}} = e^{-rT}\left[\hat{S}_0\, N(\hat{d}_1) - K\, N(\hat{d}_2)\right]
$$

where the adjusted parameters are:

$$
\hat{S}_0 = S_0\, e^{(\hat{r} - r)T}, \quad \hat{r} = \frac{1}{2}\left(r - \frac{\sigma^2}{6}\right), \quad \hat{\sigma} = \frac{\sigma}{\sqrt{3}}
$$

$$
\hat{d}_1 = \frac{\ln(\hat{S}_0/K) + (\hat{r} + \frac{1}{2}\hat{\sigma}^2)T}{\hat{\sigma}\sqrt{T}}, \quad \hat{d}_2 = \hat{d}_1 - \hat{\sigma}\sqrt{T}
$$

The volatility reduction factor $1/\sqrt{3}$ reflects the averaging effect: the geometric average has lower variance than the terminal price.

### Arithmetic Asian Options: Approximation Methods

Several approaches approximate arithmetic Asian option prices:

**Moment matching.** Match the first two moments of $\bar{S}_{\text{arith}}$ to a lognormal distribution:

$$
\mathbb{E}[\bar{S}_{\text{arith}}] = M_1, \quad \mathbb{E}[\bar{S}_{\text{arith}}^2] = M_2
$$

Then price using a Black–Scholes-like formula with the matched parameters $\hat{\mu}$ and $\hat{\sigma}^2 = \ln(M_2/M_1^2)$.

**Control variate using geometric average.** Since $\bar{S}_{\text{geom}}$ has a known price, we can use it to reduce variance in Monte Carlo estimation of the arithmetic Asian price (see [Variance Reduction](pricing_monte_carlo.md)).

---

## Properties of Asian Options

### Variance Reduction Through Averaging

The averaging mechanism reduces the variance of the payoff relative to the vanilla option:

$$
\text{Var}(\bar{S}) < \text{Var}(S_T)
$$

This implies that Asian options are **cheaper** than their vanilla counterparts:

$$
\boxed{
C_{\text{Asian}} \leq C_{\text{vanilla}}
}
$$

The inequality follows from Jensen's inequality applied to the convex payoff function and the lower variance of the averaged price.

### Resistance to Manipulation

Because the payoff depends on an average over many observation dates, it is difficult for a market participant to manipulate the payoff by trading aggressively near expiry. This makes Asian options particularly suitable for:

- Commodity hedging (oil, gas, metals)
- Currency exposure management
- Settlement of energy contracts

### Convergence to Vanilla

As the averaging period shrinks relative to the option's life, the Asian option converges to the vanilla option. Specifically, if averaging occurs only over the final instant, $\bar{S} \to S_T$ and the Asian payoff becomes the vanilla payoff.

---

## Discrete vs. Continuous Averaging

In practice, Asian options use **discrete** averaging over $n$ fixing dates $\{t_1, t_2, \ldots, t_n\}$:

$$
\bar{S}_{\text{discrete}} = \frac{1}{n}\sum_{i=1}^{n} S_{t_i}
$$

As $n \to \infty$ with uniform spacing, this converges to the continuous average. Typical contracts use **monthly** or **daily** fixings.

!!! note "Partially Elapsed Averaging"
    For an Asian option where some fixing dates have already passed, the average is partially determined:
    
    $$\bar{S} = \frac{1}{n}\left(\sum_{i=1}^{k} S_{t_i}^{\text{observed}} + \sum_{i=k+1}^{n} S_{t_i}^{\text{unknown}}\right)$$
    
    The pricing problem then involves only the remaining unknown fixings, with the observed portion acting as a known offset.

---

## Summary

$$
\boxed{
\text{Asian call payoff} = \left(\frac{1}{n}\sum_{i=1}^{n} S_{t_i} - K\right)^+
}
$$

| Aspect | Description |
|---|---|
| Definition | Payoff depends on average price over the option's life |
| Two dimensions | Arithmetic/geometric average × average-price/average-strike |
| Closed form | Geometric average only; arithmetic requires approximation or Monte Carlo |
| Key property | $C_{\text{Asian}} \leq C_{\text{vanilla}}$ (averaging reduces variance) |
| Main application | Commodity hedging, FX exposure, manipulation resistance |
| Pricing challenge | Sum of lognormals (arithmetic) is not lognormal |

**Asian options replace point-in-time price risk with average price risk, producing cheaper hedging instruments that are naturally resistant to manipulation and widely used in commodity and FX markets.**

---

## Exercises

**Exercise 1.** Prove that $C_{\text{Asian}} \leq C_{\text{vanilla}}$ for an average-price call by applying Jensen's inequality. Specifically, show that $\mathbb{E}[(\bar{S} - K)^+] \leq \mathbb{E}[(S_T - K)^+]$ when $\bar{S}$ and $S_T$ have the same mean. State the convexity property you use.

??? success "Solution to Exercise 1"
    We want to show $\mathbb{E}[(\bar{S} - K)^+] \leq \mathbb{E}[(S_T - K)^+]$ when $\bar{S}$ and $S_T$ have the same mean.

    The function $f(x) = (x - K)^+$ is **convex**. By Jensen's inequality applied to convex functions: for any convex $f$ and any random variable $X$ that is a conditional expectation of another random variable $Y$,

    $$
    f(\mathbb{E}[Y \mid \mathcal{G}]) \leq \mathbb{E}[f(Y) \mid \mathcal{G}]
    $$

    The arithmetic average $\bar{S} = \frac{1}{n}\sum_{i=1}^n S_{t_i}$ can be compared with $S_T$ as follows. Consider the conditional expectation approach: we can write

    $$
    (\bar{S} - K)^+ \leq \frac{1}{n}\sum_{i=1}^n (S_{t_i} - K)^+
    $$

    by Jensen's inequality, since $(x - K)^+$ is convex and $\bar{S}$ is a convex combination of the $S_{t_i}$.

    More directly, since $\bar{S}$ has lower variance than $S_T$ (averaging reduces variance) while both have the same mean under certain conditions, and since the call payoff $(x - K)^+$ is convex, a random variable with lower variance but the same mean produces a smaller expected value of a convex function. Formally, if $X$ and $Y$ have the same mean and $X$ is "less variable" than $Y$ in the convex order sense, then $\mathbb{E}[f(X)] \leq \mathbb{E}[f(Y)]$ for all convex $f$.

    The convexity property used is that $(x - K)^+$ is convex in $x$: for any $\lambda \in [0,1]$ and any $x_1, x_2$,

    $$
    (\lambda x_1 + (1-\lambda)x_2 - K)^+ \leq \lambda(x_1 - K)^+ + (1-\lambda)(x_2 - K)^+
    $$

    Discounting both sides by $e^{-rT}$ and taking expectations under $\mathbb{Q}$ gives $C_{\text{Asian}} \leq C_{\text{vanilla}}$.

---


**Exercise 2.** Under GBM, the continuous geometric average has adjusted volatility $\hat{\sigma} = \sigma/\sqrt{3}$. Derive this result by computing $\text{Var}\left(\frac{1}{T}\int_0^T \log S_t\, dt\right)$ where $\log S_t = \log S_0 + (r - \frac{1}{2}\sigma^2)t + \sigma W_t$. You will need the covariance $\text{Cov}(W_s, W_t) = \min(s, t)$.

??? success "Solution to Exercise 2"
    Under GBM, $\log S_t = \log S_0 + (r - \frac{1}{2}\sigma^2)t + \sigma W_t$. We need to compute:

    $$
    \text{Var}\left(\frac{1}{T}\int_0^T \log S_t\, dt\right)
    $$

    Since $\log S_0$ and $(r - \frac{1}{2}\sigma^2)t$ are deterministic, the variance comes only from the stochastic part:

    $$
    \text{Var}\left(\frac{1}{T}\int_0^T \sigma W_t\, dt\right) = \frac{\sigma^2}{T^2}\,\text{Var}\left(\int_0^T W_t\, dt\right)
    $$

    We compute $\text{Var}\left(\int_0^T W_t\, dt\right)$. Since $\mathbb{E}[W_t] = 0$, we have $\mathbb{E}\left[\int_0^T W_t\, dt\right] = 0$, so:

    $$
    \text{Var}\left(\int_0^T W_t\, dt\right) = \mathbb{E}\left[\left(\int_0^T W_t\, dt\right)^2\right] = \int_0^T \int_0^T \mathbb{E}[W_s W_t]\, ds\, dt
    $$

    Using $\text{Cov}(W_s, W_t) = \min(s, t)$:

    $$
    \int_0^T \int_0^T \min(s,t)\, ds\, dt = 2\int_0^T \int_0^t s\, ds\, dt = 2\int_0^T \frac{t^2}{2}\, dt = \int_0^T t^2\, dt = \frac{T^3}{3}
    $$

    Therefore:

    $$
    \text{Var}\left(\frac{1}{T}\int_0^T \log S_t\, dt\right) = \frac{\sigma^2}{T^2} \cdot \frac{T^3}{3} = \frac{\sigma^2 T}{3}
    $$

    The continuous geometric average is $\bar{S}_{\text{geom}} = \exp\left(\frac{1}{T}\int_0^T \log S_t\, dt\right)$. Since $\frac{1}{T}\int_0^T \log S_t\, dt$ is normally distributed, $\bar{S}_{\text{geom}}$ is lognormal with variance parameter $\sigma^2 T / 3$.

    The effective volatility for the geometric average satisfies $\hat{\sigma}^2 T = \sigma^2 T / 3$, giving:

    $$
    \hat{\sigma} = \frac{\sigma}{\sqrt{3}}
    $$

---


**Exercise 3.** Consider a discrete arithmetic average Asian call with $n = 12$ monthly fixings, $S_0 = 100$, $K = 100$, $T = 1$, $r = 5\%$, $\sigma = 20\%$. Suppose 6 months have elapsed and the observed fixings are $S_1 = 102, S_2 = 105, S_3 = 98, S_4 = 101, S_5 = 103, S_6 = 107$. Compute the partial average of the observed fixings and explain how the pricing problem simplifies for the remaining 6 months.

??? success "Solution to Exercise 3"
    The observed fixings are $S_1 = 102, S_2 = 105, S_3 = 98, S_4 = 101, S_5 = 103, S_6 = 107$.

    The partial average of observed fixings is:

    $$
    \bar{S}_{\text{observed}} = \frac{102 + 105 + 98 + 101 + 103 + 107}{6} = \frac{616}{6} \approx 102.67
    $$

    The full average at maturity will be:

    $$
    \bar{S} = \frac{1}{12}\left(\sum_{i=1}^{6} S_{t_i}^{\text{observed}} + \sum_{i=7}^{12} S_{t_i}^{\text{unknown}}\right) = \frac{616 + \sum_{i=7}^{12} S_{t_i}}{12}
    $$

    The Asian call payoff is:

    $$
    \left(\bar{S} - 100\right)^+ = \left(\frac{616 + \sum_{i=7}^{12} S_{t_i}}{12} - 100\right)^+ = \left(\frac{\sum_{i=7}^{12} S_{t_i} - 584}{12}\right)^+
    $$

    This simplifies to pricing an Asian call on the remaining 6 fixings with an **adjusted strike**. Define $\bar{S}_{\text{remaining}} = \frac{1}{6}\sum_{i=7}^{12} S_{t_i}$. Then:

    $$
    \text{Payoff} = \frac{6}{12}\left(\bar{S}_{\text{remaining}} - \frac{584}{6}\right)^+ = \frac{1}{2}\left(\bar{S}_{\text{remaining}} - 97.33\right)^+
    $$

    The pricing problem reduces to pricing an Asian call over the remaining 6 months with 6 fixings, an adjusted strike of $K^* \approx 97.33$, and a scaling factor of $1/2$. The initial spot for the remaining problem is $S_6 = 107$.

---


**Exercise 4.** Explain why the arithmetic average of lognormal random variables is not lognormal. Describe the moment-matching approximation: what distribution is assumed for $\bar{S}_{\text{arith}}$, how are the parameters $\hat{\mu}$ and $\hat{\sigma}^2$ determined, and what is the resulting approximate pricing formula?

??? success "Solution to Exercise 4"
    **Why the arithmetic average is not lognormal:** Under GBM, each $S_{t_i}$ is lognormally distributed, meaning $\log S_{t_i}$ is normally distributed. However, the arithmetic average $\bar{S}_{\text{arith}} = \frac{1}{n}\sum_{i=1}^n S_{t_i}$ is a **sum of correlated lognormal** random variables. The sum of lognormal random variables is **not** lognormal because the lognormal distribution is not closed under addition. (It is closed under multiplication, which is why the geometric average remains lognormal.) The distribution of $\bar{S}_{\text{arith}}$ has no simple closed form.

    **Moment-matching approximation:** We assume $\bar{S}_{\text{arith}}$ is approximately lognormal: $\bar{S}_{\text{arith}} \approx e^{Y}$ where $Y \sim N(\hat{\mu}, \hat{\sigma}^2)$.

    The parameters are determined by matching the first two moments:

    - First moment: $M_1 = \mathbb{E}^{\mathbb{Q}}[\bar{S}_{\text{arith}}] = \frac{1}{n}\sum_{i=1}^n S_0 e^{r t_i}$
    - Second moment: $M_2 = \mathbb{E}^{\mathbb{Q}}[\bar{S}_{\text{arith}}^2] = \frac{1}{n^2}\sum_{i=1}^n \sum_{j=1}^n S_0^2 e^{(r + \sigma^2\min(t_i, t_j))(t_i + t_j - \min(t_i, t_j)) + r\min(t_i, t_j)}$

    More precisely, $\mathbb{E}[S_{t_i} S_{t_j}] = S_0^2 \exp\left[r(t_i + t_j) + \sigma^2 \min(t_i, t_j)\right]$.

    The matched lognormal parameters are:

    $$
    \hat{\sigma}^2 = \ln\left(\frac{M_2}{M_1^2}\right), \quad \hat{\mu} = \ln M_1 - \frac{1}{2}\hat{\sigma}^2
    $$

    The approximate Asian call price is then given by a Black-Scholes-like formula:

    $$
    C_{\text{Asian}} \approx e^{-rT}\left[e^{\hat{\mu} + \hat{\sigma}^2/2} N(\hat{d}_1) - K\, N(\hat{d}_2)\right]
    $$

    where $\hat{d}_1 = \frac{\hat{\mu} + \hat{\sigma}^2 - \ln K}{\hat{\sigma}}$ and $\hat{d}_2 = \hat{d}_1 - \hat{\sigma}$.

---


**Exercise 5.** Compare the average-price call payoff $(\bar{S} - K)^+$ with the average-strike call payoff $(S_T - \bar{S})^+$. (a) Which option is more expensive and why? (b) For which option is the holder exposed to manipulation of the terminal price $S_T$? (c) Describe a hedging scenario where the average-strike call is more appropriate than the average-price call.

??? success "Solution to Exercise 5"
    **(a) Which option is more expensive?** In general, neither option dominates the other for all parameter values. However, for typical parameters, the **average-price call** $(\bar{S} - K)^+$ tends to be more expensive than the **average-strike call** $(S_T - \bar{S})^+$ for ATM options. The average-price call benefits when the average is high (upward trending market), while the average-strike call benefits when the terminal price significantly exceeds the average (late rally). The relative cost depends on the strike level, volatility, and interest rates.

    **(b) Exposure to terminal price manipulation:** The **average-strike call** $(S_T - \bar{S})^+$ is exposed to manipulation of the terminal price $S_T$, since its payoff depends directly on $S_T$. A market participant could inflate $S_T$ near expiry to increase the payoff. The average-price call $(\bar{S} - K)^+$ is resistant to such manipulation because the average is computed over many observations, and manipulating a single observation has limited impact on $\bar{S}$.

    **(c) Hedging scenario for average-strike call:** The average-strike call is appropriate for a company that plans to **sell an asset at a future date** and wants to ensure the selling price exceeds the average acquisition cost. For example, a commodity trader who has been accumulating inventory over the averaging period at an average cost of approximately $\bar{S}$ and plans to sell at the terminal date would benefit from the payoff $(S_T - \bar{S})^+$, which guarantees that the sale price exceeds the average cost. This is a natural hedge for a "buy-and-store" commodity strategy.

---


**Exercise 6.** The geometric average Asian option serves as a control variate for pricing arithmetic average Asian options. Explain the control variate method: write the variance-reduced estimator $\hat{V}_{\text{arith}} = \hat{V}_{\text{arith,MC}} + (V_{\text{geom,exact}} - \hat{V}_{\text{geom,MC}})$, and explain why the geometric average is a better control variate than the vanilla European call for this purpose.

??? success "Solution to Exercise 6"
    **The control variate method:** On each Monte Carlo path $i$, compute both the arithmetic Asian payoff $\Phi_{\text{arith}}^{(i)}$ and the geometric Asian payoff $\Phi_{\text{geom}}^{(i)}$. The variance-reduced estimator is:

    $$
    \hat{V}_{\text{arith}} = \hat{V}_{\text{arith,MC}} + (V_{\text{geom,exact}} - \hat{V}_{\text{geom,MC}})
    $$

    where $\hat{V}_{\text{arith,MC}} = e^{-rT}\frac{1}{N}\sum_{i=1}^N \Phi_{\text{arith}}^{(i)}$ is the crude Monte Carlo estimate of the arithmetic Asian price, $\hat{V}_{\text{geom,MC}} = e^{-rT}\frac{1}{N}\sum_{i=1}^N \Phi_{\text{geom}}^{(i)}$ is the Monte Carlo estimate of the geometric Asian price, and $V_{\text{geom,exact}}$ is the known analytical price of the geometric Asian option.

    This works because $V_{\text{geom,exact}} - \hat{V}_{\text{geom,MC}}$ estimates the Monte Carlo error. Since arithmetic and geometric Asian payoffs are computed on the same paths, their errors are highly correlated, so subtracting the known error in the geometric estimate also removes much of the error in the arithmetic estimate.

    **Why the geometric average is a better control variate than the vanilla European call:** The geometric average $\bar{S}_{\text{geom}}$ is much more highly correlated with the arithmetic average $\bar{S}_{\text{arith}}$ than the terminal price $S_T$ is. Both averages depend on the same collection of intermediate prices $\{S_{t_1}, \ldots, S_{t_n}\}$ and differ only in whether they are combined by addition or multiplication. In contrast, $S_T$ depends only on the final price, ignoring the intermediate path. The variance reduction factor is approximately $1 - \rho^2$, where $\rho$ is the correlation between the exotic and control payoffs. Since $\rho_{\text{geom-arith}} \gg \rho_{\text{vanilla-arith}}$, the geometric control variate provides far greater variance reduction.
