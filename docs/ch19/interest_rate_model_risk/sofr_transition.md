# SOFR Transition

The cessation of LIBOR --- the benchmark that underpinned hundreds of trillions of dollars in derivatives, loans, and securities --- is one of the most significant structural changes in financial markets. The transition from LIBOR to risk-free rates (RFRs) such as the **Secured Overnight Financing Rate (SOFR)** in USD markets fundamentally alters the mechanics of interest rate derivatives. This section explains the rationale for the transition, defines the new rate constructions, derives the mathematical implications for pricing and hedging, and discusses the fallback provisions for legacy contracts.

---

## LIBOR and Its Problems

### What LIBOR Was

The London Interbank Offered Rate (LIBOR) was an unsecured borrowing rate for major banks, published daily for multiple tenors (overnight, 1W, 1M, 2M, 3M, 6M, 12M) and five currencies (USD, GBP, EUR, CHF, JPY).

Key properties:

- **Forward-looking:** Fixed at the beginning of the accrual period
- **Term rate:** A single number for each tenor (e.g., 3-month LIBOR)
- **Credit-sensitive:** Embedded the average credit risk of the panel banks
- **Survey-based:** Determined by submissions from panel banks, not actual transactions

### Why LIBOR Was Discontinued

- **Declining transaction volumes:** Interbank unsecured lending declined dramatically after 2008
- **Manipulation scandals:** Panel banks were found to have manipulated submissions
- **Regulatory mandate:** The Financial Stability Board recommended transition to transaction-based RFRs
- **Panel bank withdrawal:** Banks were reluctant to continue submitting rates based on expert judgment

USD LIBOR publication ceased for most tenors on June 30, 2023, with certain synthetic settings continuing temporarily.

---

## SOFR: Definition and Construction

### What SOFR Is

SOFR is a broad measure of the cost of borrowing cash overnight, collateralized by U.S. Treasury securities. It is published daily by the Federal Reserve Bank of New York.

**Key properties:**

- **Overnight rate:** A single-day rate, not a term rate
- **Secured:** Based on repurchase agreement (repo) transactions
- **Transaction-based:** Derived from actual market transactions (approximately \$1 trillion daily volume)
- **Nearly risk-free:** Secured by Treasury collateral, carrying negligible credit risk

### SOFR vs LIBOR: Fundamental Differences

| Feature | LIBOR | SOFR |
|---|---|---|
| Tenor | Multiple (1M, 3M, 6M, ...) | Overnight only |
| Credit risk | Embedded | Absent |
| Secured/Unsecured | Unsecured | Secured (Treasury repo) |
| Forward/Backward | Forward-looking | Backward-looking (by default) |
| Determination | Expert judgment (survey) | Transaction-based |
| Term structure | Built-in | Must be constructed |

---

## SOFR Rate Constructions

### Daily SOFR

The basic building block is the daily SOFR rate $r_{\text{SOFR}}(t)$, published each business day for overnight lending.

### Compounded SOFR in Arrears

The standard construction for accrual periods uses **daily compounding in arrears**. For an accrual period $[T_s, T_e]$:

$$
\boxed{R_{\text{SOFR}}(T_s, T_e) = \frac{1}{\delta}\left[\prod_{i=1}^{n_d}\left(1 + \frac{d_i}{360} r_i\right) - 1\right]}
$$

where:

- $r_i = r_{\text{SOFR}}(t_i)$ is the SOFR rate for business day $t_i$
- $d_i$ is the number of calendar days that rate $t_i$ applies (1 for weekdays, 3 for Friday-to-Monday)
- $n_d$ is the number of business days in $[T_s, T_e]$
- $\delta$ is the day count fraction for the period (ACT/360)

### Simple Average SOFR

An alternative construction uses arithmetic averaging:

$$
R_{\text{avg}}(T_s, T_e) = \frac{1}{n_c} \sum_{i=1}^{n_d} d_i \cdot r_i
$$

where $n_c$ is the total number of calendar days. This is simpler but less accurate than compounding.

### SOFR Index

The Federal Reserve Bank of New York publishes a daily SOFR Index $I(t)$:

$$
I(t) = I(t_0) \prod_{i=1}^{N}\left(1 + \frac{d_i}{360} r_i\right)
$$

where the product runs over all business days from the base date $t_0$ to $t$. The compounded rate for any period is then:

$$
R_{\text{SOFR}}(T_s, T_e) = \frac{1}{\delta}\left(\frac{I(T_e)}{I(T_s)} - 1\right)
$$

This index simplifies calculations considerably.

---

## Backward-Looking vs Forward-Looking Rates

### The Fundamental Problem

LIBOR was **forward-looking**: the rate for a 3-month period was known at the start of the period. SOFR compounded in arrears is **backward-looking**: the rate for a 3-month period is only fully determined at the end of the period.

This creates practical difficulties:

- **Cash flow uncertainty:** The borrower does not know the exact payment until the end of the accrual period
- **Discounting mismatch:** The rate used for projection differs from the rate available for discounting at the period start
- **Operational complexity:** Payment amounts cannot be calculated in advance

### Observation Lag and Lookback

To partially address the cash flow uncertainty, conventions use:

**Payment delay:** The payment is made $d$ business days after the end of the observation period (e.g., 2 business days).

**Lookback (without observation shift):** The SOFR rates are observed with a lookback of $d$ days:

$$
R_{\text{lookback}}(T_s, T_e) = \frac{1}{\delta}\left[\prod_{i=1}^{n_d}\left(1 + \frac{d_i}{360} r(t_i - d)\right) - 1\right]
$$

The rate $r(t_i - d)$ is observed $d$ days before the accrual date $t_i$, ensuring the rate is known $d$ days before the payment calculation date.

**Lockout:** The SOFR rate is frozen for the last $d$ days of the accrual period at the rate observed $d$ days before the end.

### Term SOFR

The CME Group publishes **Term SOFR** --- forward-looking SOFR rates for 1-month, 3-month, 6-month, and 12-month tenors, derived from SOFR futures prices:

$$
L_{\text{Term}}(T; \Delta) = \text{implied rate from SOFR futures settling over } [T, T+\Delta]
$$

Term SOFR is:

- **Forward-looking:** Known at the start of the accrual period (like LIBOR)
- **Based on derivatives:** Constructed from futures and OIS markets, not direct lending transactions
- **Recommended only for certain products:** The ARRC recommends Term SOFR primarily for business loans, not derivatives

---

## Fallback Provisions for Legacy Contracts

### The ISDA Fallback Protocol

For derivatives, the International Swaps and Derivatives Association (ISDA) established fallback provisions. Upon LIBOR cessation, LIBOR-referencing contracts automatically switch to:

$$
\boxed{\text{Fallback Rate} = \text{Compounded SOFR in Arrears} + \text{Spread Adjustment}}
$$

### Spread Adjustment

The spread adjustment compensates for the structural difference between LIBOR (which includes credit and term premium) and SOFR (which does not). The spread was calculated as the **5-year historical median** of the difference between LIBOR and compounded SOFR:

| Tenor | Spread Adjustment (bps) |
|---|---|
| Overnight | 0.00644 |
| 1-month | 11.448 |
| 3-month | 26.161 |
| 6-month | 42.826 |
| 12-month | 71.513 |

These spreads were fixed on March 5, 2021 (the LIBOR cessation announcement date).

### Mathematical Impact

For a legacy swap paying LIBOR that falls back to SOFR + spread:

**Before fallback:**

$$
\text{Floating leg} = \sum_{i} \delta_i \, P(0, T_{i+1}) \, \mathbb{E}^{T_{i+1}}[L_i^{\text{LIBOR}}(T_i)]
$$

**After fallback:**

$$
\text{Floating leg} = \sum_{i} \delta_i \, P(0, T_{i+1}) \, \mathbb{E}^{T_{i+1}}[R_i^{\text{SOFR}}(T_i, T_{i+1}) + s]
$$

where $s$ is the fixed spread adjustment and $R_i^{\text{SOFR}}$ is the compounded SOFR rate for period $[T_i, T_{i+1}]$.

---

## Impact on Derivatives Pricing

### Forward Rate Computation

In the LIBOR framework, the forward rate was:

$$
L(0; T_i, T_{i+1}) = \frac{1}{\delta_i}\left(\frac{P(0, T_i)}{P(0, T_{i+1})} - 1\right)
$$

In the SOFR framework, the forward rate is derived from the OIS curve:

$$
R^{\text{SOFR}}(0; T_i, T_{i+1}) = \frac{1}{\delta_i}\left(\frac{P^{\text{OIS}}(0, T_i)}{P^{\text{OIS}}(0, T_{i+1})} - 1\right)
$$

The two are related by the basis spread:

$$
L(0; T_i, T_{i+1}) \approx R^{\text{SOFR}}(0; T_i, T_{i+1}) + \text{basis spread}(\delta_i)
$$

### Convexity Adjustment for Compounding in Arrears

The compounded SOFR rate is a **backward-looking** average of overnight rates. Under the $T_{i+1}$-forward measure, the expectation of the compounded rate is:

$$
\mathbb{E}^{T_{i+1}}[R_{\text{SOFR}}(T_i, T_{i+1})] = R^{\text{fwd}}_{\text{SOFR}}(0; T_i, T_{i+1}) + \text{convexity correction}
$$

The convexity correction arises because the compounded rate is a product of daily rates, not a simple forward rate. For short accrual periods and moderate volatility, this correction is small (typically < 0.1 bps).

### Cap and Floor Pricing

SOFR caps and floors are portfolios of **SOFR caplets**. A SOFR caplet pays:

$$
\delta_i \max(R_{\text{SOFR}}(T_i, T_{i+1}) - K, 0)
$$

at $T_{i+1}$ (or with a payment delay). Pricing uses:

- **Black's formula** with the SOFR forward rate replacing the LIBOR forward rate
- The same volatility surface calibration machinery (but now to SOFR cap quotes)
- Potentially a convexity adjustment if the payment date differs from $T_{i+1}$

### Swaption Pricing

SOFR swaptions are priced analogously to LIBOR swaptions, with:

- The swap rate computed from the OIS discount curve
- The annuity factor using OIS discount factors
- Black's or Bachelier's formula with SOFR swaption volatilities

---

## Worked Example: SOFR Compounded Rate

??? example "Computing Compounded SOFR"

    **Setup:** Compute the 3-month compounded SOFR rate for the period January 2 to April 2, 2024.

    **Daily SOFR rates (simplified, 5 representative weeks):**

    | Week | Mon | Tue | Wed | Thu | Fri |
    |---|---|---|---|---|---|
    | 1 | 5.31% | 5.31% | 5.32% | 5.32% | 5.31% |
    | 2 | 5.30% | 5.31% | 5.31% | 5.30% | 5.30% |
    | 3 | 5.32% | 5.33% | 5.33% | 5.33% | 5.32% |
    | 4 | 5.31% | 5.31% | 5.30% | 5.30% | 5.31% |
    | 5 | 5.30% | 5.30% | 5.31% | 5.31% | 5.31% |

    **Step 1:** Compute the daily compounding factors. For a Monday rate of 5.31% applying for 1 day:

    $1 + \frac{1}{360} \times 0.0531 = 1.00014750$

    For a Friday rate applying for 3 days (Friday to Monday):

    $1 + \frac{3}{360} \times 0.0531 = 1.00044250$

    **Step 2:** Multiply all daily factors over the 90-day period. With approximately 63 business days:

    $\prod_{i=1}^{63}\left(1 + \frac{d_i}{360}r_i\right) \approx 1.01333$

    **Step 3:** Annualize:

    $R_{\text{SOFR}} = \frac{1}{90/360}(1.01333 - 1) = 4 \times 0.01333 = 5.332\%$

    **Observation:** The compounded rate (5.332%) is slightly higher than the simple average of daily rates (approximately 5.312%) due to the compounding effect. The difference is small for short periods but can be significant for longer tenors.

---

## Modeling Implications

### Single-Curve Framework Returns

Under SOFR, discounting and projection use the **same curve** (the OIS curve), restoring the single-curve framework that prevailed before the multi-curve era:

$$
P^{\text{discount}}(0, T) = P^{\text{OIS}}(0, T) = P^{\text{projection}}(0, T)
$$

This simplifies pricing but eliminates the basis spread as a modeling dimension.

### Overnight Rate Models

SOFR-based derivatives are naturally modeled using **short-rate models** where the short rate $r(t)$ represents the overnight SOFR rate:

$$
dr(t) = \kappa(\theta(t) - r(t)) \, dt + \sigma(t) \, dW(t)
$$

The Hull--White model is particularly natural for SOFR since:

- The short rate directly corresponds to the overnight SOFR rate
- The model can be calibrated to the full OIS curve via $\theta(t)$
- Caps, floors, and swaptions have analytical or semi-analytical prices

### Market Model Adaptations

The LIBOR Market Model can be adapted to SOFR by modeling **compounded overnight rates** over future accrual periods as the primitive variables. The dynamics are similar but the rates are backward-looking rather than forward-looking. The terminal measure framework and Rebonato's swaption approximation carry over with minor modifications.

---

## Key Takeaways

- **LIBOR cessation** is driven by declining transaction volumes, manipulation concerns, and regulatory mandate
- **SOFR** is a secured overnight rate based on Treasury repo transactions, carrying negligible credit risk
- **Compounded SOFR in arrears** is the standard rate construction: $R = \frac{1}{\delta}[\prod(1 + d_i r_i/360) - 1]$
- **Backward-looking** SOFR requires lookback, lockout, or payment delay conventions to address cash flow uncertainty
- **Term SOFR** provides forward-looking rates derived from futures, recommended primarily for loans
- **Fallback provisions** convert legacy LIBOR contracts to SOFR + fixed spread adjustment
- SOFR restores the **single-curve framework** (OIS = discount = projection)
- **Pricing** of SOFR caps, floors, and swaptions follows the same mathematical framework as LIBOR derivatives, with the OIS curve replacing the LIBOR forward curve

---

## Further Reading

- Alternative Reference Rates Committee (ARRC), "SOFR Starter Kit" and "SOFR User's Guide"
- Lyashenko & Mercurio (2019), "Looking Forward to Backward-Looking Rates"
- Piterbarg (2020), "Interest Rate Modeling Post-LIBOR"
- Henrard (2019), *Interest Rate Modelling in the Multi-Curve Framework*
- Andersen & Piterbarg (2010), *Interest Rate Modeling*, Volume I (adapted for RFRs in later editions)

---

## Exercises

**Exercise 1.** The daily SOFR rates over a 5-day accrual period are $r_1 = 4.30\%$, $r_2 = 4.32\%$, $r_3 = 4.28\%$, $r_4 = 4.35\%$, $r_5 = 4.31\%$. Compute the compounded SOFR rate using

$$
R = \frac{1}{\delta}\left[\prod_{i=1}^{5}\left(1 + \frac{d_i \, r_i}{360}\right) - 1\right]
$$

where $d_i = 1$ for each day and $\delta = 5/360$. Compare the result to the simple arithmetic average of the daily rates.

---

**Exercise 2.** A legacy 5-year LIBOR swap with a fixed rate of 3.80% is being converted to SOFR under ISDA fallback provisions. The fixed spread adjustment for 3-month USD LIBOR is 26.161 bps. What is the effective fixed rate the payer will pay after conversion? Is the conversion value-neutral at the time of the fallback, and why might it not be perfectly neutral in practice?

---

**Exercise 3.** Explain the difference between a "lookback" convention and a "lockout" convention for SOFR-based floating payments. For a quarterly floating coupon, describe how a 5-business-day lookback works and how a 2-business-day lockout works. Which convention is preferred for syndicated loans and why?

---

**Exercise 4.** LIBOR contains a term credit premium while SOFR does not (being secured). For a bank that funds itself at LIBOR + 30 bps, discuss how the transition to SOFR affects the economics of making floating-rate loans. How does the credit-sensitive alternative (e.g., BSBY or Ameribor) attempt to address this issue, and what are the regulatory concerns with such alternatives?

---

**Exercise 5.** Term SOFR is derived from SOFR futures prices. Explain how the market prices of 1-month and 3-month SOFR futures can be used to construct a forward-looking term rate. Why did regulators recommend limiting the use of Term SOFR to certain products (primarily loans) rather than allowing it for all derivatives?

---

**Exercise 6.** Under the LIBOR framework, the forward LIBOR rate $L_i(t)$ was a martingale under $\mathbb{Q}^{T_{i+1}}$, leading to Black's caplet formula. In the SOFR framework, the compounded rate over $[T_i, T_{i+1}]$ is backward-looking and only known at $T_{i+1}$. Discuss how this affects the measure-theoretic setup for pricing SOFR caplets and whether Black's formula can still be applied (with appropriate modifications).

---

**Exercise 7.** The transition from multi-curve (OIS + multiple LIBOR tenors) to essentially single-curve (SOFR) simplifies the modeling framework. Describe three specific simplifications that arise in a SOFR-only world and one new complexity that the backward-looking nature of SOFR introduces compared to forward-looking LIBOR.
