# Asian Options

## Introduction

**Asian options** (also called **average-rate options**) are path-dependent derivatives whose payoff depends on the **average price** of the underlying asset over a specified period, rather than the terminal price alone. This averaging mechanism reduces the impact of price manipulation near expiry and stabilizes payoff variability, making Asian options natural hedging instruments for entities with continuous exposure to commodity or currency prices.

Asian options are among the most common exotic options in commodity and FX markets, where exposure accumulates gradually over time.

!!! info "Prerequisites"
    - [Black–Scholes Formula](../black_scholes_formula/bs_formula_statement.md) (vanilla pricing baseline)
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
