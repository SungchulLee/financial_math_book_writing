# Lookback Options

## Introduction

**Lookback options** are path-dependent derivatives whose payoff depends on the **maximum** or **minimum** price of the underlying asset over the option's life. The holder effectively gets to "look back" over the entire price history and exercise at the most favorable price. This eliminates the timing risk inherent in vanilla options but comes at a significantly higher premium.

Lookback options appear in performance-linked products, executive compensation structures, and specialized hedging strategies where capturing the best achievable outcome is valued.

!!! info "Prerequisites"
    - [Black–Scholes Formula](../../ch06/black_scholes_formula/bs_formula_statement.md) (vanilla pricing)
    - [Reflection Principle](../../ch02/brownian_motion/reflection_principle.md) (distribution of Brownian motion extrema)
    - [Exotic Options Overview](exotic_options_overview.md) (classification)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Distinguish fixed-strike and floating-strike lookback options
    2. Write the payoff formulas and interpret their financial meaning
    3. State the analytical pricing formula under GBM with continuous monitoring
    4. Understand why lookback options are expensive relative to vanilla options

---

## Types of Lookback Options

### Fixed-Strike Lookback Options

A **fixed-strike lookback** option has a predetermined strike $K$ and uses the extremal price in the payoff:

$$
\boxed{
\text{Fixed-strike lookback call} = \left(S_{\max} - K\right)^+, \quad S_{\max} = \max_{0 \leq t \leq T} S_t
}
$$

$$
\text{Fixed-strike lookback put} = \left(K - S_{\min}\right)^+, \quad S_{\min} = \min_{0 \leq t \leq T} S_t
$$

The fixed-strike lookback call pays the excess of the **highest achieved price** over the strike. This is always at least as valuable as a vanilla call, since $S_{\max} \geq S_T$.

### Floating-Strike Lookback Options

A **floating-strike lookback** option uses the extremal price as the effective strike:

$$
\boxed{
\text{Floating-strike lookback call} = S_T - S_{\min}
}
$$

$$
\text{Floating-strike lookback put} = S_{\max} - S_T
$$

The floating-strike lookback call lets the holder buy at the **lowest price** and sell at the **terminal price**. Similarly, the floating-strike lookback put lets the holder sell at the **highest price**. Note that these payoffs are **always non-negative** (the option is always in the money), which is why floating-strike lookbacks are particularly expensive.

---

## Pricing Under GBM: Continuous Monitoring

Under geometric Brownian motion with continuous monitoring, analytical formulas exist based on the **joint distribution of Brownian motion and its running maximum/minimum** (derived from the reflection principle).

### Floating-Strike Lookback Call

The Goldman–Sosin–Gatto (1979) formula for the floating-strike lookback call is:

$$
C_{\text{lookback}} = S_0\, N(a_1) - S_0\, e^{-rT} \frac{\sigma^2}{2r}\, N(-a_1) - S_{\min}\, e^{-rT}\left[N(a_2) - \frac{\sigma^2}{2r}\, e^{a_3}\, N(-a_4)\right]
$$

where the parameters $a_1, a_2, a_3, a_4$ involve $S_0$, $S_{\min}$, $r$, $\sigma$, and $T$. The formula is considerably more complex than Black–Scholes due to the distribution of the running minimum.

### Key Features of the Pricing Formula

The analytical formula reveals important properties:

- **Always in the money**: For floating-strike lookbacks, the payoff $S_T - S_{\min} \geq 0$ always, so the option always has positive value
- **No strike parameter**: Floating-strike lookbacks have no fixed strike $K$; the effective strike is determined by the path
- **Higher premium**: Lookback options cost significantly more than vanilla options (typically 2–3× for floating-strike)

---

## Price Ordering

The following ordering holds for options with identical parameters:

$$
\boxed{
V_{\text{vanilla}} \leq V_{\text{fixed-strike lookback}} \leq V_{\text{floating-strike lookback}}
}
$$

The first inequality follows from $S_{\max} \geq S_T$ (for calls) or $S_{\min} \leq S_T$ (for puts). The second inequality reflects the additional flexibility of the floating strike.

!!! example "Numerical Comparison"
    For $S_0 = 100$, $K = 100$, $T = 1$, $r = 0.05$, $\sigma = 0.20$:
    
    | Option Type | Approximate Price |
    |---|---|
    | Vanilla call | $\approx 10.45$ |
    | Fixed-strike lookback call | $\approx 17.15$ |
    | Floating-strike lookback call | $\approx 15.72$ |
    
    The lookback premium over the vanilla price reflects the value of hindsight.

---

## Discrete vs. Continuous Monitoring

As with barrier options, the distinction between **discrete** and **continuous** monitoring is important:

$$
S_{\max}^{\text{discrete}} = \max_{i=1,\ldots,n} S_{t_i} \leq \max_{0 \leq t \leq T} S_t = S_{\max}^{\text{continuous}}
$$

Discrete monitoring always produces a lower (or equal) maximum and a higher (or equal) minimum, so:

- **Discrete lookback call** is cheaper than continuous lookback call
- **Discrete lookback put** is cheaper than continuous lookback put

The Broadie–Glasserman–Kou correction (similar to barrier options) adjusts for discrete monitoring:

$$
S_{\max}^{\text{continuous}} \approx S_{\max}^{\text{discrete}} \cdot e^{\beta \sigma \sqrt{T/n}}
$$

where $\beta \approx 0.5826$.

---

## Applications

**Performance-linked products.** Structured notes may offer returns based on the maximum price of an index over a year, providing investors with "best-of" payoff profiles.

**Executive compensation.** Lookback stock options allow executives to exercise at the lowest price during the vesting period, maximizing the payout. These have largely been replaced by standard restricted stock units due to accounting and governance concerns.

**Benchmark analysis.** The lookback price serves as a theoretical upper bound on what a perfect-timing trader could achieve, useful for evaluating trading strategy performance.

---

## Summary

$$
\boxed{
\text{Floating-strike lookback call payoff} = S_T - \min_{0 \leq t \leq T} S_t \geq 0
}
$$

| Aspect | Description |
|---|---|
| Definition | Payoff depends on running maximum or minimum of the underlying |
| Two types | Fixed-strike (extremum vs. $K$) and floating-strike (extremum as effective strike) |
| Key property | Floating-strike lookbacks are always in the money |
| Analytical pricing | Available under GBM with continuous monitoring (reflection principle) |
| Cost | Significantly more expensive than vanilla options (2–3× typical) |
| Ordering | $V_{\text{vanilla}} \leq V_{\text{fixed lookback}} \leq V_{\text{floating lookback}}$ |

**Lookback options provide perfect hindsight by referencing the extremal price over the option's life, offering maximum payoff potential at the cost of a substantial premium.**
