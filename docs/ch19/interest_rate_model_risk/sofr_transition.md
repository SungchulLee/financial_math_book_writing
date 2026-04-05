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

??? success "Solution to Exercise 1"

    **Computing the compounded SOFR rate:**

    Given $r_1 = 4.30\%$, $r_2 = 4.32\%$, $r_3 = 4.28\%$, $r_4 = 4.35\%$, $r_5 = 4.31\%$, with $d_i = 1$ for each day and $\delta = 5/360$.

    **Step 1: Compute daily compounding factors.**

    $$
    1 + \frac{1}{360} \times 0.0430 = 1.000119444
    $$

    $$
    1 + \frac{1}{360} \times 0.0432 = 1.000120000
    $$

    $$
    1 + \frac{1}{360} \times 0.0428 = 1.000118889
    $$

    $$
    1 + \frac{1}{360} \times 0.0435 = 1.000120833
    $$

    $$
    1 + \frac{1}{360} \times 0.0431 = 1.000119722
    $$

    **Step 2: Compute the product.**

    $$
    \prod_{i=1}^{5}\left(1 + \frac{d_i r_i}{360}\right) = 1.000119444 \times 1.000120000 \times 1.000118889 \times 1.000120833 \times 1.000119722
    $$

    Since all factors are very close to 1, we can compute the product as:

    $$
    \approx 1 + (0.000119444 + 0.000120000 + 0.000118889 + 0.000120833 + 0.000119722) + \text{tiny cross-terms}
    $$

    $$
    \approx 1 + 0.000598889 = 1.000598889
    $$

    (The cross-terms from compounding are of order $10^{-8}$ and negligible for this short period.)

    **Step 3: Annualize.**

    $$
    R = \frac{1}{\delta}\left[\prod_{i=1}^{5}\left(1 + \frac{d_i r_i}{360}\right) - 1\right] = \frac{360}{5} \times 0.000598889 = 72 \times 0.000598889 = 4.3120\%
    $$

    **Simple arithmetic average:**

    $$
    \bar{r} = \frac{4.30 + 4.32 + 4.28 + 4.35 + 4.31}{5} = \frac{21.56}{5} = 4.312\%
    $$

    **Comparison:** The compounded rate (4.3120%) and the simple average (4.312%) are essentially identical for this 5-day period. The compounding effect is negligible ($< 0.001$ bps) because: (a) the period is very short (5 days), and (b) the daily rates are very close to each other. For longer periods (e.g., 3 months with 63 business days), the compounding effect becomes more noticeable, typically on the order of 1--2 bps above the simple average.

---

**Exercise 2.** A legacy 5-year LIBOR swap with a fixed rate of 3.80% is being converted to SOFR under ISDA fallback provisions. The fixed spread adjustment for 3-month USD LIBOR is 26.161 bps. What is the effective fixed rate the payer will pay after conversion? Is the conversion value-neutral at the time of the fallback, and why might it not be perfectly neutral in practice?

??? success "Solution to Exercise 2"

    **ISDA fallback mechanism:** The legacy swap pays 3-month LIBOR on the floating leg against a fixed rate of 3.80%. After LIBOR cessation, the floating leg references:

    $$
    \text{Fallback Rate} = \text{Compounded SOFR in Arrears} + 26.161 \text{ bps}
    $$

    **Effective fixed rate after conversion:** The swap economics are now: pay fixed 3.80%, receive SOFR + 26.161 bps. Rearranging, this is equivalent to paying a net fixed rate of:

    $$
    \text{Effective fixed rate vs. SOFR} = 3.80\% - 0.26161\% = 3.53839\%
    $$

    over SOFR. That is, the payer effectively pays $3.80\%$ and receives $\text{SOFR} + 0.26161\%$, which is equivalent to paying $3.80\% - 0.26161\% = 3.5384\%$ over SOFR flat.

    **Value-neutrality at the time of fallback:**

    The conversion was designed to be approximately value-neutral at the moment of fallback. The spread adjustment of 26.161 bps was calculated as the 5-year historical median of the difference (3M LIBOR minus compounded SOFR), frozen on March 5, 2021. At that specific moment:

    $$
    \mathbb{E}[\text{LIBOR}] \approx \mathbb{E}[\text{SOFR} + 26.161 \text{ bps}]
    $$

    based on historical averages.

    **Why it may not be perfectly neutral in practice:**

    1. **Historical median vs. current spread:** The 5-year historical median reflects past average conditions, not the current or expected future spread. At the time of fallback, the actual LIBOR-SOFR spread may be higher or lower than 26.161 bps.

    2. **Spread dynamics:** The spread adjustment is fixed forever, but the LIBOR-SOFR spread was stochastic and mean-reverting. Locking in a constant spread converts stochastic basis risk into a deterministic quantity, changing the risk profile.

    3. **Forward-looking vs. backward-looking:** LIBOR was forward-looking (set at the beginning of the period), while compounded SOFR is backward-looking (determined at the end). This difference affects the timing of cash flows and introduces a convexity adjustment that the fixed spread does not capture.

    4. **Discounting effects:** If the swap is collateralized at OIS/SOFR, the change from LIBOR to SOFR + spread on the floating leg changes the covariance between the floating rate and the discount factor, creating a small valuation difference.

---

**Exercise 3.** Explain the difference between a "lookback" convention and a "lockout" convention for SOFR-based floating payments. For a quarterly floating coupon, describe how a 5-business-day lookback works and how a 2-business-day lockout works. Which convention is preferred for syndicated loans and why?

??? success "Solution to Exercise 3"

    **Lookback convention (5-business-day lookback):**

    In a lookback convention, the SOFR rate applied to each day of the accrual period is shifted backward by 5 business days. For a quarterly accrual period $[T_s, T_e]$:

    - On accrual day $t_i$, the SOFR rate used is $r(t_i - 5\text{bd})$, where $5\text{bd}$ means 5 business days earlier.
    - The weighting (number of calendar days $d_i$) still corresponds to day $t_i$ in the accrual period, but the rate is from 5 days prior.

    $$
    R_{\text{lookback}} = \frac{1}{\delta}\left[\prod_{i=1}^{n_d}\left(1 + \frac{d_i}{360} r(t_i - 5\text{bd})\right) - 1\right]
    $$

    **Effect:** The entire rate is known 5 business days before the end of the accrual period (since the last day's rate uses the SOFR from 5 days earlier). This gives the borrower advance notice of the payment amount.

    **Lockout convention (2-business-day lockout):**

    In a lockout convention, the SOFR rate is frozen for the last 2 business days of the accrual period:

    - For accrual days $t_1, \ldots, t_{n_d - 2}$: the actual SOFR rate $r(t_i)$ is used.
    - For the last 2 business days $t_{n_d - 1}$ and $t_{n_d}$: the rate is frozen at $r(t_{n_d - 2})$.

    $$
    R_{\text{lockout}} = \frac{1}{\delta}\left[\prod_{i=1}^{n_d - 2}\left(1 + \frac{d_i}{360} r(t_i)\right) \times \left(1 + \frac{d_{n_d-1} + d_{n_d}}{360} r(t_{n_d - 2})\right) - 1\right]
    $$

    **Effect:** The payment amount is known 2 business days before the end of the accrual period.

    **Preference for syndicated loans:**

    The **lookback** convention is preferred for syndicated loans because:

    - Syndicated loans involve multiple lenders who need time to process payment instructions.
    - A 5-day lookback provides sufficient advance notice (the rate is fully known 5 business days before the payment date).
    - The lookback preserves the SOFR rate dynamics for the full accrual period (just shifted), whereas the lockout effectively shortens the observation window, potentially missing rate movements in the final days.
    - The ARRC (Alternative Reference Rates Committee) specifically recommended the lookback for syndicated loans.

---

**Exercise 4.** LIBOR contains a term credit premium while SOFR does not (being secured). For a bank that funds itself at LIBOR + 30 bps, discuss how the transition to SOFR affects the economics of making floating-rate loans. How does the credit-sensitive alternative (e.g., BSBY or Ameribor) attempt to address this issue, and what are the regulatory concerns with such alternatives?

??? success "Solution to Exercise 4"

    **Impact on floating-rate loan economics:**

    Under LIBOR, a bank that funds at LIBOR + 30 bps and makes a floating-rate loan at LIBOR + 150 bps earns a net interest margin (NIM) of:

    $$
    \text{NIM}_{\text{LIBOR}} = (L + 150) - (L + 30) = 120 \text{ bps}
    $$

    The LIBOR component cancels, providing a natural hedge between funding and lending.

    Under SOFR, the loan references SOFR while the bank's unsecured funding cost still includes a credit component:

    $$
    \text{Funding cost} = \text{SOFR} + \text{bank credit spread} + \text{term premium}
    $$

    If the loan pays SOFR + 150 bps and the bank funds at SOFR + 80 bps (where 80 bps represents the bank's credit spread plus term premium):

    $$
    \text{NIM}_{\text{SOFR}} = (\text{SOFR} + 150) - (\text{SOFR} + 80) = 70 \text{ bps}
    $$

    The SOFR cancels, but the bank's credit spread does not. The critical difference is that under LIBOR, the embedded credit premium in LIBOR partially offset the bank's own credit spread (since LIBOR reflected average bank credit risk). Under SOFR, the bank's credit spread is fully exposed---it is not hedged by the reference rate.

    **Credit-sensitive alternatives:**

    - **BSBY (Bloomberg Short-Term Bank Yield Index):** Based on bank CP/CD issuance, it embeds bank credit risk (similar to LIBOR). A loan at BSBY + spread would provide a natural hedge against the bank's own funding cost fluctuations.
    - **Ameribor:** Based on unsecured overnight lending between smaller banks, reflecting their credit conditions.

    These alternatives restore the LIBOR-like property of having a credit-sensitive reference rate that co-moves with bank funding costs.

    **Regulatory concerns:**

    - **Same vulnerabilities as LIBOR:** Credit-sensitive rates may suffer from the same problems that led to LIBOR's demise---thin underlying transaction volumes, susceptibility to manipulation, and reliance on a limited set of contributing institutions.
    - **Systemic risk:** Regulators prefer rates based on deep, liquid markets (SOFR has ~\$1 trillion daily volume) rather than thin credit markets.
    - **Pro-cyclicality:** Credit-sensitive rates rise during crises (when bank credit spreads widen), increasing borrowing costs precisely when borrowers are most stressed. SOFR, being risk-free, does not exhibit this pro-cyclical behavior.
    - **ARRC and FSB recommendation:** Both strongly recommend SOFR as the primary USD benchmark, with credit-sensitive alternatives discouraged for derivatives and large-scale lending.

---

**Exercise 5.** Term SOFR is derived from SOFR futures prices. Explain how the market prices of 1-month and 3-month SOFR futures can be used to construct a forward-looking term rate. Why did regulators recommend limiting the use of Term SOFR to certain products (primarily loans) rather than allowing it for all derivatives?

??? success "Solution to Exercise 5"

    **Constructing Term SOFR from futures:**

    **1-month Term SOFR:** Derived from 1-month SOFR futures (contracts that settle based on the arithmetic average of daily SOFR over a calendar month). If the futures price is $P_F$, the implied rate is:

    $$
    L_{\text{Term}}^{1M}(T) = \frac{100 - P_F}{100}
    $$

    For example, if the 1-month SOFR futures price for the next month is 94.70, the implied 1-month Term SOFR is $100 - 94.70 = 5.30\%$.

    **3-month Term SOFR:** Derived from 3-month SOFR futures (which settle on the compounded SOFR over a quarterly period). The CME uses an interpolation/bootstrapping methodology:

    - Identify the 3-month SOFR futures contracts whose reference periods overlap with the desired forward period.
    - Use the futures prices to extract the implied compounded rate for the target 3-month period.
    - Apply a convexity adjustment if necessary (futures vs. forwards).

    The result is a forward-looking 3-month rate:

    $$
    L_{\text{Term}}^{3M}(T) = \text{rate implied by SOFR futures for the period } [T, T+3M]
    $$

    **Why regulators limit Term SOFR usage:**

    1. **Circularity concern:** Term SOFR is derived from SOFR derivatives (futures and OIS). If derivatives themselves referenced Term SOFR, it would create a circular dependence: derivatives priced off a rate that is itself derived from derivatives. This could lead to manipulation incentives and market instability.

    2. **Liquidity and robustness:** SOFR futures markets, while growing, are less liquid than the underlying overnight SOFR market. Basing a widely-used benchmark on a derivatives market that is less deep creates robustness concerns.

    3. **Backward-looking preference:** Regulators and the ARRC strongly prefer that derivatives use compounded SOFR in arrears because it is directly tied to actual overnight transactions (~\$1 trillion daily), making it more robust and harder to manipulate.

    4. **Transition incentive:** Allowing Term SOFR for all products would reduce incentives for market participants to develop infrastructure for backward-looking rates, potentially perpetuating dependence on forward-looking rates that may be less robust.

    The ARRC recommends Term SOFR primarily for **business loans** (where borrowers need payment certainty), **trade finance**, and certain **consumer products**, while discouraging its use for **derivatives** and **capital markets instruments**.

---

**Exercise 6.** Under the LIBOR framework, the forward LIBOR rate $L_i(t)$ was a martingale under $\mathbb{Q}^{T_{i+1}}$, leading to Black's caplet formula. In the SOFR framework, the compounded rate over $[T_i, T_{i+1}]$ is backward-looking and only known at $T_{i+1}$. Discuss how this affects the measure-theoretic setup for pricing SOFR caplets and whether Black's formula can still be applied (with appropriate modifications).

??? success "Solution to Exercise 6"

    **LIBOR framework (forward-looking):**

    Under the LIBOR framework, the forward LIBOR rate $L_i(t) = L(t; T_i, T_{i+1})$ is defined as the rate fixed at $T_i$ for the period $[T_i, T_{i+1}]$. It is an $\mathcal{F}_{T_i}$-measurable random variable. Under the $T_{i+1}$-forward measure $\mathbb{Q}^{T_{i+1}}$:

    $$
    L_i(t) \text{ is a martingale for } t \leq T_i
    $$

    This means $\mathbb{E}^{T_{i+1}}[L_i(T_i) | \mathcal{F}_t] = L_i(t)$. At $T_i$, the rate is known, and the caplet payoff $\delta(L_i(T_i) - K)^+$ paid at $T_{i+1}$ can be priced using Black's formula since $L_i(T_i)$ has a lognormal (or normal) distribution under $\mathbb{Q}^{T_{i+1}}$.

    **SOFR framework (backward-looking):**

    The compounded SOFR rate for $[T_i, T_{i+1}]$ is:

    $$
    R_i = \frac{1}{\delta_i}\left[\prod_{j}\left(1 + \frac{d_j}{360}r(t_j)\right) - 1\right]
    $$

    where $r(t_j)$ are daily SOFR rates observed during $[T_i, T_{i+1}]$. Crucially, $R_i$ is only $\mathcal{F}_{T_{i+1}}$-measurable (not $\mathcal{F}_{T_i}$-measurable) because it depends on rates observed throughout the period, including rates at dates after $T_i$.

    **Measure-theoretic implications:**

    Under $\mathbb{Q}^{T_{i+1}}$, the forward value of $R_i$ at time $t < T_i$ is:

    $$
    R_i^{\text{fwd}}(t) = \mathbb{E}^{T_{i+1}}[R_i | \mathcal{F}_t]
    $$

    This expectation is well-defined, and $R_i^{\text{fwd}}(t)$ is a $\mathbb{Q}^{T_{i+1}}$-martingale. However, the distribution of $R_i$ is more complex than that of a simple forward rate because $R_i$ is a product (or approximately a sum) of correlated daily rates.

    **Can Black's formula be applied?**

    Yes, with appropriate modifications:

    1. Replace the forward LIBOR rate with the forward SOFR rate: $L_i(0) \to R_i^{\text{fwd}}(0) = \frac{1}{\delta_i}\left(\frac{P^{\text{OIS}}(0,T_i)}{P^{\text{OIS}}(0,T_{i+1})} - 1\right)$.

    2. Use the same Black (or Bachelier) formula with this forward rate as the underlying.

    3. The key assumption is that $R_i^{\text{fwd}}(t)$ follows a lognormal (or normal) diffusion under $\mathbb{Q}^{T_{i+1}}$, which is an approximation---the compounded rate is a nonlinear function of daily rates, not a simple diffusion.

    4. A **convexity adjustment** may be needed if the payment date differs from $T_{i+1}$ or if the lookback/lockout convention modifies the rate. For standard cases (payment at $T_{i+1}$, no lockout), the convexity correction is small (< 0.1 bps for short periods).

    In practice, SOFR caplets are priced using Black's or Bachelier's formula with the SOFR forward rate, and the approximation is considered adequate for most purposes.

---

**Exercise 7.** The transition from multi-curve (OIS + multiple LIBOR tenors) to essentially single-curve (SOFR) simplifies the modeling framework. Describe three specific simplifications that arise in a SOFR-only world and one new complexity that the backward-looking nature of SOFR introduces compared to forward-looking LIBOR.

??? success "Solution to Exercise 7"

    **Three simplifications in a SOFR-only world:**

    1. **Single discount and projection curve:** Under LIBOR, one needed an OIS curve for discounting and a separate LIBOR curve (per tenor) for projection. Under SOFR, the same OIS/SOFR curve serves both purposes:

        $$
        P^{\text{discount}}(0,T) = P^{\text{OIS}}(0,T) = P^{\text{projection}}(0,T)
        $$

        This eliminates the need to build, maintain, and hedge multiple curves, significantly reducing infrastructure complexity.

    2. **No tenor basis modeling:** Under LIBOR, the 3M/6M/12M basis spreads were additional stochastic variables requiring modeling, calibration, and hedging. In a SOFR world, all tenors are derived from the same overnight rate via compounding, so there is no structural basis:

        $$
        R^{6M}(T_i, T_{i+1}) \approx \text{compounded}(R^{3M}(T_i, T_{i+3M}), R^{3M}(T_{i+3M}, T_{i+1}))
        $$

        This eliminates an entire dimension of risk factors.

    3. **Simplified calibration:** Multi-curve LMMs required calibration to both the volatility surface and the basis spread dynamics. A single-curve SOFR model calibrates only to SOFR cap/swaption volatilities and the SOFR yield curve, reducing the number of parameters and improving calibration stability.

    **One new complexity from backward-looking rates:**

    **Cash flow uncertainty and convexity adjustments:** Under LIBOR, the forward rate $L_i(T_i)$ was known at the start of the accrual period $T_i$, making the caplet payoff a function of an $\mathcal{F}_{T_i}$-measurable quantity. Under SOFR, the compounded rate $R_i$ is only determined at $T_{i+1}$. This creates:

    - **Operational complexity:** Payment amounts cannot be calculated until the end of the accrual period, requiring lookback, lockout, or payment delay conventions.
    - **Modeling complexity:** The compounded rate is a product of correlated daily rates, not a single forward rate. Pricing requires either (a) treating the forward compounded rate as the primitive variable (an approximation) or (b) modeling the full path of daily rates (computationally expensive).
    - **Convexity corrections:** If the payment date is shifted relative to $T_{i+1}$ (e.g., with a payment delay), or if a lookback convention is used, the rate and the discount factor are no longer naturally aligned, creating convexity adjustments that did not exist in the LIBOR framework.

    This backward-looking complexity is a genuine new challenge that did not arise with forward-looking LIBOR, and it has required significant infrastructure development across the industry.
