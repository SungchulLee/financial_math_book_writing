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

---

## Exercises

**Exercise 1.** Prove the price ordering $V_{\text{vanilla call}} \leq V_{\text{fixed-strike lookback call}}$ by showing that $(S_{\max} - K)^+ \geq (S_T - K)^+$ for every path. Under what condition on the path does equality hold?

??? success "Solution to Exercise 1"
    For any path $\omega$, we have $S_{\max}(\omega) = \max_{0 \leq t \leq T} S_t(\omega) \geq S_T(\omega)$ since the maximum over the entire path is at least as large as the terminal value.

    Since $f(x) = (x - K)^+$ is non-decreasing in $x$ (it is zero for $x \leq K$ and equals $x - K$ for $x > K$), applying $f$ to both sides of $S_{\max} \geq S_T$:

    $$
    (S_{\max} - K)^+ \geq (S_T - K)^+
    $$

    for every path $\omega$. Taking risk-neutral expectations and discounting:

    $$
    V_{\text{fixed-strike lookback call}} = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_{\max} - K)^+] \geq e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+] = V_{\text{vanilla call}}
    $$

    **Equality holds** when $S_{\max} = S_T$, i.e., when the stock price reaches its maximum exactly at the terminal time $T$. This occurs on paths where the price is monotonically increasing (or at least the final price equals the all-time high). In a GBM model, this event has positive but not full probability, so the inequality is strict in expectation.

---


**Exercise 2.** A floating-strike lookback call has payoff $S_T - S_{\min}$, which is always non-negative. Explain why this payoff is never zero (assuming continuous paths and $\sigma > 0$), and why this property makes floating-strike lookbacks particularly expensive. Estimate the option value as a multiple of the vanilla call price for typical parameters.

??? success "Solution to Exercise 2"
    The payoff $S_T - S_{\min}$ is always non-negative since $S_{\min} = \min_{0 \leq t \leq T} S_t \leq S_T$.

    **Why the payoff is never zero (for continuous paths with $\sigma > 0$):** The payoff equals zero only if $S_T = S_{\min}$, meaning the terminal price is the minimum over the entire path. For a continuous GBM path with $\sigma > 0$, the stock price fluctuates continuously, so the probability that the minimum occurs exactly at the terminal time $T$ is zero. More precisely, for Brownian motion, $\mathbb{P}(\inf_{0 \leq t \leq T} W_t = W_T) = 0$ (the infimum of a Brownian path on $[0, T]$ is almost surely attained at an interior point). Therefore $S_T - S_{\min} > 0$ almost surely.

    **Why this makes floating-strike lookbacks expensive:** Since the payoff is strictly positive with probability 1, the option is always in the money. There is no chance of the option expiring worthless, unlike a vanilla call (which expires worthless when $S_T < K$). The holder is guaranteed a positive payout, and this guarantee carries a substantial premium.

    **Cost estimate:** For typical parameters ($\sigma = 20\%$, $T = 1$), the floating-strike lookback call costs approximately **1.5 to 2 times** the ATM vanilla call price. For higher volatility, the multiple increases because $S_{\min}$ tends to be further below $S_T$, widening the guaranteed spread.

---


**Exercise 3.** For discrete monitoring with $n$ observation dates, explain why $S_{\max}^{\text{discrete}} \leq S_{\max}^{\text{continuous}}$. Derive the Broadie-Glasserman-Kou correction $S_{\max}^{\text{continuous}} \approx S_{\max}^{\text{discrete}} \cdot e^{\beta \sigma \sqrt{T/n}}$ and compute the correction factor for $\sigma = 0.25$, $T = 1$, $n = 52$ (weekly monitoring).

??? success "Solution to Exercise 3"
    **Why $S_{\max}^{\text{discrete}} \leq S_{\max}^{\text{continuous}}$:** The continuous maximum considers the supremum over all $t \in [0, T]$, while the discrete maximum considers only the values at observation dates $\{t_1, \ldots, t_n\}$. Since the set of observation dates is a subset of $[0, T]$:

    $$
    S_{\max}^{\text{discrete}} = \max_{i=1,\ldots,n} S_{t_i} \leq \sup_{0 \leq t \leq T} S_t = S_{\max}^{\text{continuous}}
    $$

    The maximum over a subset is always at most the maximum over the full set.

    **BGK correction derivation:** The correction relates the expected discrete maximum to the continuous maximum via the overshoot distribution of Brownian motion crossing a level. The asymptotic analysis of Broadie, Glasserman, and Kou shows:

    $$
    \mathbb{E}[\log S_{\max}^{\text{continuous}} - \log S_{\max}^{\text{discrete}}] \approx \beta \sigma \sqrt{T/n}
    $$

    where $\beta = -\zeta(1/2)/\sqrt{2\pi} \approx 0.5826$. This leads to the correction:

    $$
    S_{\max}^{\text{continuous}} \approx S_{\max}^{\text{discrete}} \cdot e^{\beta \sigma \sqrt{T/n}}
    $$

    **Numerical computation for $\sigma = 0.25$, $T = 1$, $n = 52$:**

    $$
    \beta \sigma \sqrt{T/n} = 0.5826 \times 0.25 \times \sqrt{1/52} = 0.5826 \times 0.25 \times 0.13868 = 0.02020
    $$

    The correction factor is $e^{0.02020} \approx 1.0204$, meaning the continuous maximum is approximately **2.04% higher** than the discrete weekly maximum.

---


**Exercise 4.** Consider a fixed-strike lookback put with payoff $(K - S_{\min})^+$ where $K = 100$ and suppose $S_{\min} = 75$ over the option's life. Compare this payoff with a vanilla put that expires with $S_T = 90$. Which option pays more and by how much? Explain why the lookback put is sometimes described as providing "insurance at the best possible price."

??? success "Solution to Exercise 4"
    **Fixed-strike lookback put payoff:** With $K = 100$ and $S_{\min} = 75$:

    $$
    (K - S_{\min})^+ = (100 - 75)^+ = 25
    $$

    **Vanilla put payoff:** With $K = 100$ and $S_T = 90$:

    $$
    (K - S_T)^+ = (100 - 90)^+ = 10
    $$

    The lookback put pays **\$25** while the vanilla put pays **\$10**, so the lookback put pays **\$15 more**.

    The lookback put is described as providing "insurance at the best possible price" because its payoff is based on $S_{\min}$, the lowest price the stock ever reached. No matter when the stock hit its trough, the lookback put captures that worst-case level. A vanilla put only captures the price at expiry, which may have recovered from the low. The lookback effectively lets the holder exercise at the moment most favorable for them (the minimum), providing the maximum insurance payout. In this example, even though the stock recovered from 75 to 90 by expiry, the lookback holder still receives the benefit of the 75 level.

---


**Exercise 5.** The Goldman-Sosin-Gatto formula for floating-strike lookback calls involves the joint distribution of $(S_T, S_{\min})$. Explain the connection between this joint distribution and the reflection principle for Brownian motion. Why does the analytical formula require continuous monitoring, and what modifications are needed for discrete monitoring?

??? success "Solution to Exercise 5"
    The Goldman-Sosin-Gatto formula requires the **joint distribution of $(S_T, S_{\min})$** (or equivalently $(W_T, \inf_t W_t)$ under the log transform). This joint distribution is derived from the **reflection principle** for Brownian motion.

    The reflection principle provides, for standard Brownian motion starting at 0:

    $$
    \mathbb{P}(W_T \leq x,\, \inf_{0 \leq t \leq T} W_t \geq -a) = N\!\left(\frac{x}{\sqrt{T}}\right) - e^{-2ax/T}\,N\!\left(\frac{x - 2a}{\sqrt{T}}\right)
    $$

    for $a \geq 0$. Under GBM, $\log S_t$ is drifted Brownian motion, and the running minimum of $S_t$ corresponds to the running minimum of $\log S_t$. The Girsanov measure change accounts for the drift, introducing the power-law factor $\lambda = (r - \frac{1}{2}\sigma^2)/\sigma^2 + 1$ into the formulas.

    **Why continuous monitoring is required:** The reflection principle gives the exact distribution of the running extremum only for a **continuous** process. In continuous time, every barrier level between the initial and terminal values must be crossed, and the reflection bijection is exact. With discrete monitoring, the process can "jump over" levels between observation dates, breaking the reflection argument.

    **Modifications for discrete monitoring:**

    1. Use Monte Carlo simulation with sufficiently many time steps to approximate continuous monitoring.
    2. Apply the Broadie-Glasserman-Kou correction $S_{\max}^{\text{cont}} \approx S_{\max}^{\text{disc}} \cdot e^{\beta\sigma\sqrt{T/n}}$ to adjust the discrete extremum to an effective continuous value.
    3. Use Spitzer's identity or Wiener-Hopf factorization for exact discrete-monitoring formulas, though these are computationally more involved.

---


**Exercise 6.** A partial lookback option only monitors the running maximum over a subinterval $[t_1, t_2] \subset [0, T]$, with payoff $(S_{\max}^{[t_1, t_2]} - K)^+$. Explain why this option is cheaper than a full lookback and more expensive than a vanilla call. Describe how you would price it using Monte Carlo simulation.

??? success "Solution to Exercise 6"
    **Why cheaper than a full lookback:** The full lookback monitors $S_{\max}^{[0,T]} = \max_{0 \leq t \leq T} S_t$, while the partial lookback monitors $S_{\max}^{[t_1, t_2]}$ over a subinterval. Since $[t_1, t_2] \subset [0, T]$:

    $$
    S_{\max}^{[t_1, t_2]} \leq S_{\max}^{[0,T]}
    $$

    path by path. Therefore $(S_{\max}^{[t_1, t_2]} - K)^+ \leq (S_{\max}^{[0,T]} - K)^+$, and the partial lookback is cheaper.

    **Why more expensive than a vanilla call:** Since $S_{\max}^{[t_1, t_2]} \geq S_{t_2}$ (the maximum over a period is at least the endpoint), and the price at any single time $t_2$ has the same marginal distribution as $S_T$ (adjusting for drift), the partial lookback payoff dominates a vanilla call payoff in a similar sense: $(S_{\max}^{[t_1, t_2]} - K)^+ \geq (S_{t^*} - K)^+$ for any single time $t^* \in [t_1, t_2]$.

    **Monte Carlo pricing:**

    1. Simulate $N$ price paths $\{S_{t_0}^{(i)}, S_{t_1}^{(i)}, \ldots, S_{t_M}^{(i)}\}$ under GBM with fine time steps.
    2. For each path $i$, compute the running maximum over the monitoring subinterval: $S_{\max}^{(i)} = \max_{t_k \in [t_1, t_2]} S_{t_k}^{(i)}$.
    3. Compute the payoff: $\Phi^{(i)} = (S_{\max}^{(i)} - K)^+$.
    4. Estimate the price: $\hat{V} = e^{-rT} \frac{1}{N}\sum_{i=1}^N \Phi^{(i)}$.
    5. Use fine time steps within $[t_1, t_2]$ to minimize discrete-monitoring bias, or apply the BGK correction to adjust $S_{\max}^{\text{discrete}}$ to approximate $S_{\max}^{\text{continuous}}$.
