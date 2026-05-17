# Timing Adjustments

A **timing adjustment** (or **payment delay convexity adjustment**) arises whenever a rate is observed at one date but paid at a different date that is not the rate's natural payment date. In standard derivatives, the LIBOR rate $L(T_i)$ fixing at $T_i$ is paid at $T_{i+1}$ --- the "natural" payment date. When payment occurs at some other date $T_p \neq T_{i+1}$, the expectation of the rate under the $T_p$-forward measure differs from the forward rate, and a correction is needed. This section derives the general timing adjustment formula, illustrates it with concrete examples, and connects it to the broader convexity adjustment framework.

---

## Natural vs. Unnatural Payment Dates

### The Natural Setup

A standard caplet fixes the rate $L_i(T_i)$ at time $T_i$ and pays $\delta_i (L_i(T_i) - K)^+$ at time $T_{i+1}$. Under the $T_{i+1}$-forward measure $\mathbb{Q}^{T_{i+1}}$:

$$
\mathbb{E}^{\mathbb{Q}^{T_{i+1}}}[L_i(T_i)] = L_i(0)
$$

The forward rate equals the forward rate --- no adjustment is needed.

### The Unnatural Setup

Suppose instead the payment occurs at time $T_p \neq T_{i+1}$. We need to compute

$$
\mathbb{E}^{\mathbb{Q}^{T_p}}[L_i(T_i)]
$$

Since $L_i(t)$ is a martingale under $\mathbb{Q}^{T_{i+1}}$ but **not** under $\mathbb{Q}^{T_p}$, this expectation differs from $L_i(0)$:

$$
\mathbb{E}^{\mathbb{Q}^{T_p}}[L_i(T_i)] = L_i(0) + \text{timing adjustment}
$$

---

## Derivation of the Timing Adjustment

### General Formula via Measure Change

The Radon--Nikodym derivative from $\mathbb{Q}^{T_{i+1}}$ to $\mathbb{Q}^{T_p}$ is

$$
\frac{d\mathbb{Q}^{T_p}}{d\mathbb{Q}^{T_{i+1}}}\bigg|_{\mathcal{F}_t} = \frac{P(t, T_p) / P(0, T_p)}{P(t, T_{i+1}) / P(0, T_{i+1})}
$$

Using the change-of-measure formula:

$$
\mathbb{E}^{\mathbb{Q}^{T_p}}[L_i(T_i)] = \mathbb{E}^{\mathbb{Q}^{T_{i+1}}}\!\left[L_i(T_i) \cdot \frac{P(T_i, T_p) / P(0, T_p)}{P(T_i, T_{i+1}) / P(0, T_{i+1})}\right]
$$

### Girsanov Drift Adjustment

Under $\mathbb{Q}^{T_{i+1}}$, $L_i(t)$ satisfies

$$
\frac{dL_i(t)}{L_i(t)} = \sigma_i(t) \, dW_i^{T_{i+1}}(t)
$$

Under $\mathbb{Q}^{T_p}$, a drift correction appears via Girsanov's theorem:

$$
dW_i^{T_{i+1}}(t) = dW_i^{T_p}(t) + \bigl[\Sigma(t, T_p) - \Sigma(t, T_{i+1})\bigr] \rho_i(t) \, dt
$$

where $\Sigma(t, U) = \int_t^U \sigma_f(t, u) \, du$ is the bond volatility and $\rho_i(t)$ is the correlation between the forward rate $L_i$ and the bond price ratio.

### Result: Lognormal Case

For lognormal forward rates with constant volatility $\sigma_i$ and deterministic bond volatilities, the timing adjustment to first order is

$$
\boxed{\mathbb{E}^{\mathbb{Q}^{T_p}}[L_i(T_i)] \approx L_i(0) + L_i(0) \, \sigma_i \, \sigma_{P}(T_{i+1}, T_p) \, \rho \, T_i}
$$

where $\sigma_P(T_{i+1}, T_p)$ is the volatility of the bond price ratio $P(t, T_p)/P(t, T_{i+1})$ and $\rho$ is the correlation between $L_i$ and this ratio.

### Simplified Formula for Adjacent Dates

When $T_p$ is close to $T_{i+1}$, a common approximation uses

$$
\sigma_P(T_{i+1}, T_p) \approx \sigma_i \cdot \frac{\delta_i L_i(0)}{1 + \delta_i L_i(0)} \cdot |T_p - T_{i+1}|
$$

leading to

$$
\text{Timing Adjustment} \approx L_i(0) \cdot \frac{\sigma_i^2 \, \delta_i \, L_i(0)}{1 + \delta_i L_i(0)} \cdot |T_p - T_{i+1}| \cdot T_i
$$

---

## Special Cases

### Early Payment (T_p < T_{i+1})

When payment occurs before the natural date (e.g., at $T_i$), the adjustment is the **LIBOR-in-arrears correction**, Recall (see [§ LIBOR in Arrears](libor_in_arrears.md)). The adjustment is **positive** because paying earlier at a higher rate benefits the receiver (convexity effect).

### Late Payment (T_p > T_{i+1})

When payment is delayed beyond the natural date, the adjustment has the opposite sign:

$$
\text{Adjustment} \approx -L_i(0) \cdot \sigma_i \cdot \sigma_{P} \cdot \rho \cdot T_i
$$

The sign depends on the correlation between the rate and the discount factor for the delay period.

### Payment at Fixing Date (T_p = T_i)

This is the LIBOR-in-arrears case; see [§ LIBOR in Arrears](libor_in_arrears.md) for the full derivation. The timing adjustment is the largest of the common cases.

---

## General Timing Adjustment Formula

### For an Arbitrary Rate R Observed at T_fix, Paid at T_p

The general formula is

$$
\mathbb{E}^{\mathbb{Q}^{T_p}}[R(T_{\text{fix}})] = \mathbb{E}^{\mathbb{Q}^{T_{\text{nat}}}}[R(T_{\text{fix}})] + \text{Cov}^{\mathbb{Q}^{T_{\text{nat}}}}\!\left(R(T_{\text{fix}}), \frac{P(T_{\text{fix}}, T_p)}{P(T_{\text{fix}}, T_{\text{nat}})}\right) \cdot \frac{P(0, T_{\text{nat}})}{P(0, T_p)}
$$

where $T_{\text{nat}}$ is the natural payment date for the rate $R$.

This formula shows that the timing adjustment is determined by the **covariance** between the rate and the bond price ratio. When the rate and the bond ratio are positively correlated, the adjusted expectation exceeds the forward rate.

---

## Worked Example

??? example "Timing Adjustment for Delayed Payment"

    **Setup:** LIBOR rate $L_i(T_i)$ for the 6-month period starting at $T_i = 2.0$, with natural payment at $T_{i+1} = 2.5$, but actual payment delayed to $T_p = 3.0$.

    **Parameters:**

    - $L_i(0) = 3.5\%$, $\delta_i = 0.5$
    - $\sigma_i = 18\%$ (Black vol)
    - Bond volatility for the delay period: $\sigma_P(T_{i+1}, T_p) \approx 0.5\%$
    - Correlation $\rho = 0.85$

    **Timing adjustment:**

    $\text{Adj} = L_i(0) \times \sigma_i \times \sigma_P \times \rho \times T_i$

    $= 0.035 \times 0.18 \times 0.005 \times 0.85 \times 2.0 = 0.0000054 = 0.054$ bp

    **Adjusted expectation:**

    $\mathbb{E}^{\mathbb{Q}^{T_p}}[L_i(T_i)] \approx 3.5\% + 0.054$ bp $= 3.5005\%$

    For this short delay (6 months) and moderate volatility, the timing adjustment is small (less than 0.1 bp). For longer delays or higher volatilities, the adjustment can be several basis points.

---

## When Timing Adjustments Matter

Timing adjustments are typically small for standard derivatives but become significant in:

- **Non-standard payment schedules:** Cross-currency swaps with mismatched payment dates
- **Structured products:** Range accruals, snowballs with delayed coupons
- **CMS products:** Where the rate and payment date are structurally misaligned
- **Exotic options:** Path-dependent products with observation dates differing from payment dates

!!! tip "Rule of Thumb"
    The timing adjustment scales as $\sigma^2 \times T_{\text{fix}} \times |T_p - T_{\text{nat}}|$. It is negligible for short-dated products with nearby payment dates but can accumulate to several basis points for long-dated products with large payment delays.

---

## Key Takeaways

- A **timing adjustment** corrects for the difference between a rate's natural payment date and the actual payment date
- The adjustment arises from a measure change (Girsanov) between forward measures associated with different payment dates
- The general formula involves the **covariance** between the rate and the bond price ratio for the delay period
- For lognormal rates, the adjustment is proportional to $\sigma^2 T_{\text{fix}} |T_p - T_{\text{nat}}|$
- **Early payment** produces a positive adjustment; **late payment** typically produces a smaller or negative adjustment
- Timing adjustments are a special case of the broader convexity adjustment framework

---

## Further Reading

- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 13
- Pelsser (2000), *Efficient Methods for Valuing Interest Rate Derivatives*, Chapter 5
- Hunt & Kennedy (2004), *Financial Derivatives in Theory and Practice*, Chapter 14

---

## Exercises

**Exercise 1.** A 6-month LIBOR rate fixes at $T_i = 4.0$ with natural payment at $T_{i+1} = 4.5$, but actual payment is at $T_p = 5.0$. The forward rate is $L_i(0) = 3.0\%$, Black volatility is $\sigma_i = 22\%$, the bond volatility for the delay period is $\sigma_P(T_{i+1}, T_p) = 0.6\%$, and the correlation is $\rho = 0.90$. Compute the timing adjustment and the adjusted expectation $\mathbb{E}^{\mathbb{Q}^{T_p}}[L_i(T_i)]$.

??? success "Solution to Exercise 1"

    **Given:** $T_i = 4.0$, $T_{i+1} = 4.5$, $T_p = 5.0$, $L_i(0) = 0.03$, $\sigma_i = 0.22$, $\sigma_P(T_{i+1}, T_p) = 0.006$, $\rho = 0.90$.

    Using the timing adjustment formula:

    $$
    \text{Adj} = L_i(0) \times \sigma_i \times \sigma_P(T_{i+1}, T_p) \times \rho \times T_i
    $$

    Substituting:

    $$
    \text{Adj} = 0.03 \times 0.22 \times 0.006 \times 0.90 \times 4.0
    $$

    Computing step by step:

    - $0.03 \times 0.22 = 0.0066$
    - $0.0066 \times 0.006 = 0.0000396$
    - $0.0000396 \times 0.90 = 0.00003564$
    - $0.00003564 \times 4.0 = 0.00014256$

    $$
    \text{Adj} = 0.00014256 = 1.43 \text{ bp}
    $$

    Note that since $T_p = 5.0 > T_{i+1} = 4.5$ (delayed payment), and the correlation between the rate and the bond ratio is positive, the sign of this adjustment depends on the direction convention. In the general formula, a delayed payment with positive correlation between the rate and the forward bond price ratio leads to a **positive** adjustment (the rate must compensate for late payment when high rates coincide with high discount factors for the delay period).

    **Adjusted expectation:**

    $$
    \mathbb{E}^{\mathbb{Q}^{T_p}}[L_i(T_i)] \approx 3.0\% + 1.43 \text{ bp} = 3.0143\%
    $$

    This adjustment of 1.43 bp is larger than the 0.054 bp in the worked example because: (1) the fixing time is longer ($T_i = 4$ vs $T_i = 2$), (2) the delay is longer ($T_p - T_{i+1} = 0.5$ years vs $0.5$ years, but with higher bond volatility $0.6\%$ vs $0.5\%$), and (3) the rate volatility is higher ($22\%$ vs $18\%$).

---

**Exercise 2.** Derive the timing adjustment formula starting from the Radon--Nikodym derivative

$$
\frac{d\mathbb{Q}^{T_p}}{d\mathbb{Q}^{T_{i+1}}}\bigg|_{\mathcal{F}_t} = \frac{P(t, T_p) / P(0, T_p)}{P(t, T_{i+1}) / P(0, T_{i+1})}
$$

by applying Girsanov's theorem to the lognormal forward rate dynamics. Show explicitly how the drift correction depends on the covariance between the forward rate and the bond price ratio $P(t, T_p)/P(t, T_{i+1})$.

??? success "Solution to Exercise 2"

    **Starting point:** Under $\mathbb{Q}^{T_{i+1}}$, the forward rate follows lognormal dynamics:

    $$
    \frac{dL_i(t)}{L_i(t)} = \sigma_i \, dW_i^{T_{i+1}}(t)
    $$

    The Radon--Nikodym derivative is:

    $$
    \frac{d\mathbb{Q}^{T_p}}{d\mathbb{Q}^{T_{i+1}}}\bigg|_{\mathcal{F}_t} = \frac{P(t, T_p)/P(0, T_p)}{P(t, T_{i+1})/P(0, T_{i+1})} = \frac{P(0, T_{i+1})}{P(0, T_p)} \cdot \frac{P(t, T_p)}{P(t, T_{i+1})}
    $$

    Define the ratio $R(t) = P(t, T_p)/P(t, T_{i+1})$. This ratio is a $\mathbb{Q}^{T_{i+1}}$-martingale (as a ratio of tradeable assets normalized by the numéraire $P(t, T_{i+1})$). Under $\mathbb{Q}^{T_{i+1}}$:

    $$
    \frac{dR(t)}{R(t)} = \sigma_R(t) \, dW_R^{T_{i+1}}(t)
    $$

    where $\sigma_R(t) = \sigma_P(t, T_p) - \sigma_P(t, T_{i+1})$ is the volatility of the bond price ratio, and $W_R^{T_{i+1}}$ is a Brownian motion under $\mathbb{Q}^{T_{i+1}}$ with $dW_i^{T_{i+1}} \cdot dW_R^{T_{i+1}} = \rho \, dt$.

    **Applying Girsanov's theorem:** The measure change $\mathbb{Q}^{T_{i+1}} \to \mathbb{Q}^{T_p}$ is given by the Radon--Nikodym derivative proportional to $R(T_i)$. By Girsanov's theorem:

    $$
    dW_i^{T_{i+1}}(t) = dW_i^{T_p}(t) - \rho \, \sigma_R(t) \, dt
    $$

    Substituting into the forward rate dynamics:

    $$
    \frac{dL_i(t)}{L_i(t)} = \sigma_i \left(dW_i^{T_p}(t) - \rho \, \sigma_R(t) \, dt\right) = -\sigma_i \, \rho \, \sigma_R(t) \, dt + \sigma_i \, dW_i^{T_p}(t)
    $$

    The drift correction under $\mathbb{Q}^{T_p}$ is:

    $$
    \mu(t) = -\sigma_i \, \rho \, \sigma_R(t)
    $$

    Identifying $\sigma_R(t) \approx -\sigma_P(T_{i+1}, T_p)$ (with appropriate sign conventions for the bond volatility of the delay period), the expectation becomes:

    $$
    \mathbb{E}^{\mathbb{Q}^{T_p}}[L_i(T_i)] = L_i(0) \exp\!\left(\int_0^{T_i} \mu(t) \, dt\right) \approx L_i(0)(1 + \sigma_i \, \sigma_P(T_{i+1}, T_p) \, \rho \, T_i)
    $$

    The covariance structure is explicit: the drift depends on $\text{Cov}(dL_i/L_i, dR/R) = \sigma_i \sigma_R \rho \, dt$, which is the instantaneous covariance between the forward rate and the bond price ratio. $\square$

---

**Exercise 3.** A floating-rate note pays quarterly coupons, but due to a settlement convention, each coupon is paid 5 business days (approximately 1 week) after the end of the accrual period. The forward rate for a typical period is $L_i(0) = 4.5\%$, $\sigma_i = 15\%$, and the fixing time is $T_i = 7$ years. Estimate the timing adjustment for this 1-week delay and argue whether it is material enough to warrant explicit computation in practice.

??? success "Solution to Exercise 3"

    **Given:** $L_i(0) = 0.045$, $\sigma_i = 0.15$, $T_i = 7$ years, delay $= 1/52 \approx 0.0192$ years (5 business days $\approx$ 1 week).

    **Estimate bond volatility for the delay period:**

    $$
    \sigma_P(T_{i+1}, T_p) \approx \sigma_i \cdot \frac{\delta_i L_i(0)}{1 + \delta_i L_i(0)} \cdot |T_p - T_{i+1}|
    $$

    With $\delta_i = 0.25$ (quarterly) and $|T_p - T_{i+1}| = 1/52$:

    $$
    \sigma_P \approx 0.15 \times \frac{0.25 \times 0.045}{1 + 0.25 \times 0.045} \times \frac{1}{52} = 0.15 \times \frac{0.01125}{1.01125} \times 0.0192
    $$

    $$
    = 0.15 \times 0.01112 \times 0.0192 = 0.0000320
    $$

    **Timing adjustment** (assuming $\rho \approx 0.90$):

    $$
    \text{Adj} = L_i(0) \times \sigma_i \times \sigma_P \times \rho \times T_i = 0.045 \times 0.15 \times 0.0000320 \times 0.90 \times 7
    $$

    $$
    = 0.045 \times 0.15 \times 0.000202 = 0.00000136 \approx 0.014 \text{ bp}
    $$

    **Assessment:** The timing adjustment is approximately $0.014$ basis points, which is less than $0.02$ bp. This is well below the typical bid-ask spread for interest rate products (usually 0.5--2 bp) and below the precision of most market data inputs.

    **Conclusion:** A 1-week payment delay does **not** warrant explicit computation in practice. The adjustment is negligible because it scales as $|T_p - T_{i+1}|^2$ (the bond volatility itself is proportional to the delay period, and the adjustment is proportional to the bond volatility times the rate volatility). Only when the delay becomes several months or longer, or when the portfolio is very large, does the timing adjustment become material.

---

**Exercise 4.** Explain qualitatively why the LIBOR-in-arrears convexity correction (payment at $T_i$ instead of $T_{i+1}$) is always positive, while a payment delay beyond $T_{i+1}$ can produce a correction of either sign depending on the correlation. Use the general covariance formula to support your argument.

??? success "Solution to Exercise 4"

    **LIBOR-in-arrears (early payment at $T_i$):**

    The general covariance formula states:

    $$
    \text{Adj} = \text{Cov}^{\mathbb{Q}^{T_{i+1}}}\!\left(L_i(T_i), \frac{P(T_i, T_i)}{P(T_i, T_{i+1})}\right) \cdot \frac{P(0, T_{i+1})}{P(0, T_i)}
    $$

    Since $P(T_i, T_i) = 1$ and $P(T_i, T_{i+1}) = 1/(1 + \delta_i L_i(T_i))$, the ratio is:

    $$
    \frac{P(T_i, T_i)}{P(T_i, T_{i+1})} = 1 + \delta_i L_i(T_i)
    $$

    This is an **increasing function** of $L_i(T_i)$. Therefore:

    $$
    \text{Cov}^{\mathbb{Q}^{T_{i+1}}}\!\left(L_i(T_i), 1 + \delta_i L_i(T_i)\right) = \delta_i \, \text{Var}^{\mathbb{Q}^{T_{i+1}}}(L_i(T_i)) > 0
    $$

    The covariance is always **strictly positive** because the bond price ratio is a monotonically increasing function of the rate itself. This is why the LIBOR-in-arrears adjustment is always positive, regardless of any correlation assumptions.

    **Delayed payment beyond $T_{i+1}$ (e.g., $T_p > T_{i+1}$):**

    The relevant covariance is:

    $$
    \text{Cov}^{\mathbb{Q}^{T_{i+1}}}\!\left(L_i(T_i), \frac{P(T_i, T_p)}{P(T_i, T_{i+1})}\right)
    $$

    The ratio $P(T_i, T_p)/P(T_i, T_{i+1})$ is a forward discount factor for the period $[T_{i+1}, T_p]$. When rates rise, this discount factor can move in either direction relative to $L_i$, depending on:

    - The **correlation** between the short-term rate $L_i$ and the forward rate spanning $[T_{i+1}, T_p]$
    - The **term structure dynamics**: in a parallel shift model, all rates move together ($\rho = 1$), and the covariance has a definite sign. But in a multi-factor model, short and long rates can move independently or even in opposite directions

    If $L_i$ and the forward rate for $[T_{i+1}, T_p]$ are negatively correlated (yield curve steepening scenario), the covariance can be negative, making the timing adjustment negative. If they are positively correlated but the bond volatility is small, the adjustment is positive but small.

    **Summary:** The LIBOR-in-arrears correction is structurally positive (it involves $\text{Var}(L_i) > 0$), while the delayed payment correction involves a genuine cross-rate covariance that can have either sign.

---

**Exercise 5.** Consider two structured notes, both referencing 3-month LIBOR:

- Note A fixes at $T_i = 5$ and pays at $T_p = 5$ (in-arrears).
- Note B fixes at $T_i = 5$ and pays at $T_p = 6$ (delayed by 1 year).

With $L_i(0) = 4\%$, $\sigma_i = 20\%$, and $\delta_i = 0.25$, compute the timing adjustment for each note. Use the LIBOR-in-arrears formula for Note A and the general timing adjustment formula (with $\sigma_P = 0.8\%$ and $\rho = 0.80$) for Note B. Which adjustment is larger and why?

??? success "Solution to Exercise 5"

    **Note A: In-arrears payment at $T_p = T_i = 5$.**

    Using the LIBOR-in-arrears formula:

    $$
    \text{Adj}_A = \frac{\delta_i \, L_i(0)^2 \, \sigma_i^2 \, T_i}{1 + \delta_i L_i(0)} = \frac{0.25 \times 0.04^2 \times 0.04 \times 5}{1 + 0.25 \times 0.04}
    $$

    $$
    = \frac{0.25 \times 0.0016 \times 0.04 \times 5}{1.01} = \frac{0.00008}{1.01} = 0.0000792 = 0.792 \text{ bp}
    $$

    **Note B: Delayed payment at $T_p = 6$.**

    Natural payment date: $T_{i+1} = T_i + \delta_i = 5.25$. Delay: $T_p - T_{i+1} = 0.75$ years.

    Using the general timing adjustment formula:

    $$
    \text{Adj}_B = L_i(0) \times \sigma_i \times \sigma_P \times \rho \times T_i = 0.04 \times 0.20 \times 0.008 \times 0.80 \times 5
    $$

    $$
    = 0.04 \times 0.20 \times 0.008 \times 0.80 \times 5 = 0.04 \times 0.0064 \times 5 = 0.00000256 \times 5000
    $$

    Let me recompute carefully:

    - $0.04 \times 0.20 = 0.008$
    - $0.008 \times 0.008 = 0.000064$
    - $0.000064 \times 0.80 = 0.0000512$
    - $0.0000512 \times 5 = 0.000256$

    $$
    \text{Adj}_B = 0.000256 = 2.56 \text{ bp}
    $$

    **Comparison:** Note B has a larger timing adjustment (2.56 bp) than Note A (0.79 bp).

    **Why Note B's adjustment is larger:** Although the in-arrears correction (Note A) benefits from the structural positive covariance between the rate and its own discount factor, the adjustment scales as $L_i(0)^2 \sigma_i^2$ which involves the relatively small factor $L_i(0)^2 = 0.0016$. For Note B, the 1-year delay ($T_p - T_{i+1} = 0.75$ years) combined with a non-negligible bond volatility ($0.8\%$) and high correlation ($0.80$) creates a larger effect. The general timing adjustment scales linearly in $L_i(0)$ rather than quadratically, and the bond volatility for a longer delay period is substantial. In this parameter configuration, the delayed payment effect dominates the in-arrears effect.

---

**Exercise 6.** The general timing adjustment formula involves the covariance

$$
\text{Cov}^{\mathbb{Q}^{T_{\text{nat}}}}\!\left(R(T_{\text{fix}}),\;\frac{P(T_{\text{fix}}, T_p)}{P(T_{\text{fix}}, T_{\text{nat}})}\right)
$$

Under what conditions on the rate $R$ and the yield curve dynamics does this covariance equal zero, making the timing adjustment vanish? Give a concrete example of a model or market scenario where this could approximately hold.

??? success "Solution to Exercise 6"

    The covariance equals zero when the rate $R(T_{\text{fix}})$ and the bond price ratio $P(T_{\text{fix}}, T_p)/P(T_{\text{fix}}, T_{\text{nat}})$ are **uncorrelated**.

    **Conditions for zero covariance:**

    1. **Independence of rate and discount factor:** If the rate $R$ and the yield curve dynamics governing the bond prices between $T_{\text{nat}}$ and $T_p$ are driven by independent factors, the covariance vanishes. In a multi-factor term structure model, this can occur when the short-term rate (driving $R$) and the forward rates for the period $[T_{\text{nat}}, T_p]$ load on orthogonal factors.

    2. **Zero correlation ($\rho = 0$):** In the lognormal model, if the Brownian motions driving $R$ and the bond price ratio are uncorrelated, the timing adjustment is exactly zero.

    3. **Deterministic bond price ratio:** If the ratio $P(T_{\text{fix}}, T_p)/P(T_{\text{fix}}, T_{\text{nat}})$ is deterministic (i.e., known at time $0$), then it has zero variance and hence zero covariance with any random variable. This occurs if the yield curve between $T_{\text{nat}}$ and $T_p$ is deterministic, even if $R$ is stochastic.

    **Concrete example:** Consider a two-factor interest rate model where Factor 1 drives short-term rates (and hence $R$) and Factor 2 drives the term spread for maturities beyond $T_{\text{nat}}$. If the two factors are independent and $P(T_{\text{fix}}, T_p)/P(T_{\text{fix}}, T_{\text{nat}})$ depends only on Factor 2, then the covariance is zero.

    A practical scenario where this approximately holds: when the delay $|T_p - T_{\text{nat}}|$ is very short (e.g., a few days), the bond price ratio $P(T_{\text{fix}}, T_p)/P(T_{\text{fix}}, T_{\text{nat}})$ is nearly deterministic (close to 1), so its variance and hence its covariance with $R$ is negligible. This is essentially the reason why timing adjustments for short payment delays are immaterial (as shown in Exercise 3).

---

**Exercise 7.** A cross-currency swap pays USD LIBOR quarterly but EUR EURIBOR semiannually, with mismatched payment dates. For a specific EUR coupon, the EURIBOR rate $L^f$ fixes at $T = 3$ with natural payment at $T + 0.5 = 3.5$, but the actual payment (aligned with the USD schedule) occurs at $T_p = 3.25$. Using $L^f(0) = 2.5\%$, $\sigma^f = 16\%$, and appropriate estimates for the bond volatility and correlation, estimate the timing adjustment and discuss whether it should be combined with any other convexity or quanto adjustments.

??? success "Solution to Exercise 7"

    **Timing adjustment estimate:**

    The EURIBOR rate fixes at $T = 3$ with natural payment at $T_{\text{nat}} = 3.5$, but actual payment at $T_p = 3.25$. Since $T_p < T_{\text{nat}}$, payment is **early** (by 0.25 years).

    **Bond volatility estimate:** For the period $[T_p, T_{\text{nat}}] = [3.25, 3.5]$, the bond volatility is:

    $$
    \sigma_P(T_{\text{nat}}, T_p) \approx \sigma^f \cdot \frac{\delta L^f(0)}{1 + \delta L^f(0)} \cdot |T_p - T_{\text{nat}}|
    $$

    With $\delta = 0.5$ (semiannual), $L^f(0) = 0.025$:

    $$
    \sigma_P \approx 0.16 \times \frac{0.5 \times 0.025}{1 + 0.5 \times 0.025} \times 0.25 = 0.16 \times \frac{0.0125}{1.0125} \times 0.25 = 0.16 \times 0.01235 \times 0.25 = 0.000494
    $$

    **Timing adjustment** (assuming $\rho \approx 0.85$):

    $$
    \text{Adj} = L^f(0) \times \sigma^f \times \sigma_P \times \rho \times T = 0.025 \times 0.16 \times 0.000494 \times 0.85 \times 3
    $$

    $$
    = 0.025 \times 0.16 \times 0.000494 \times 2.55 = 0.025 \times 0.000202 = 0.00000504
    $$

    $$
    \approx 0.05 \text{ bp}
    $$

    Since $T_p < T_{\text{nat}}$ (early payment), the sign is positive: $\mathbb{E}^{\mathbb{Q}^{T_p}}[L^f(T)] \approx 2.5\% + 0.05$ bp $= 2.5005\%$.

    **Interaction with other adjustments:**

    In a cross-currency swap, the EUR EURIBOR rate paid in USD requires **multiple adjustments**:

    1. **Timing adjustment** (computed above): corrects for the payment date mismatch. This is approximately $0.05$ bp --- small but conceptually important.

    2. **Quanto adjustment:** Since the EUR rate is paid in USD, a quanto adjustment is needed. This depends on the correlation between EURIBOR and the EUR/USD exchange rate, and is typically 1--5 bp for a 3-year horizon, dominating the timing adjustment.

    3. **Potential LIBOR-in-arrears correction:** Not applicable here since the rate is not paid at the fixing date.

    The adjustments should be **combined** because they arise from different aspects of the measure change. The timing adjustment corrects for the payment date mismatch within the EUR curve, while the quanto adjustment corrects for the cross-currency settlement. In principle, one performs a single composite measure change from $\mathbb{Q}^{f,T_{\text{nat}}}$ to $\mathbb{Q}^{d,T_p}$, which incorporates both effects simultaneously. To first order, the adjustments are additive, so the total correction is approximately the sum of the timing and quanto adjustments. For the parameters given, the quanto adjustment would dominate (likely 2--4 bp), making the timing adjustment a secondary but non-negligible correction.
