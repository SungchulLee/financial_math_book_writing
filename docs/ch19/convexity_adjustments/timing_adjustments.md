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

When payment occurs before the natural date (e.g., at $T_i$), the adjustment is related to **LIBOR-in-arrears**:

$$
\mathbb{E}^{\mathbb{Q}^{T_i}}[L_i(T_i)] = L_i(0) + \frac{L_i(0)^2 \, \sigma_i^2 \, T_i \, \delta_i}{1 + \delta_i L_i(0)}
$$

The adjustment is **positive** because paying earlier at a higher rate benefits the receiver (convexity effect).

### Late Payment (T_p > T_{i+1})

When payment is delayed beyond the natural date, the adjustment has the opposite sign:

$$
\text{Adjustment} \approx -L_i(0) \cdot \sigma_i \cdot \sigma_{P} \cdot \rho \cdot T_i
$$

The sign depends on the correlation between the rate and the discount factor for the delay period.

### Payment at Fixing Date (T_p = T_i)

This is the LIBOR-in-arrears case, which receives its own detailed treatment in the next section. The timing adjustment is the largest of the common cases.

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
