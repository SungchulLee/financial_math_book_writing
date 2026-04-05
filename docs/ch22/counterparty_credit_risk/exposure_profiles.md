# Exposure Profiles

Counterparty credit risk (CCR) arises from the possibility that a counterparty defaults while a derivative position has positive value. **Exposure profiles** describe how this potential loss evolves over the life of the trade.

---

## Definition of Exposure

For a derivative portfolio with value process $V_t$, the **exposure** at time $t$ is:

$$
E_t = \max(V_t, 0) = V_t^+
$$

**Interpretation:** 
- If $V_t > 0$: We are owed money; default causes loss
- If $V_t < 0$: We owe money; default causes no direct loss (ignoring replacement cost)

Exposure is **one-sided**—only positive values matter for CCR.

---

## Expected Exposure (EE)

The **Expected Exposure** at time $t$ is:

$$
\text{EE}(t) = \mathbb{E}^{\mathbb{Q}}[E_t] = \mathbb{E}^{\mathbb{Q}}[V_t^+]
$$

where the expectation is typically under the risk-neutral measure $\mathbb{Q}$.

**Properties:**
- EE is deterministic (a function of time only)
- EE depends on portfolio composition and market dynamics
- EE is always non-negative

---

## Expected Positive Exposure (EPE)

The **Expected Positive Exposure** is the time-averaged EE:

$$
\text{EPE} = \frac{1}{T} \int_0^T \text{EE}(t) \, dt
$$

**Discrete approximation:**

$$
\text{EPE} \approx \frac{1}{n} \sum_{i=1}^n \text{EE}(t_i)
$$

EPE is a single number summarizing average exposure over the portfolio's life.

---

## Effective EPE and Effective EE

Regulatory capital calculations use **non-decreasing** versions:

**Effective EE:**

$$
\text{Effective EE}(t) = \max_{s \le t} \text{EE}(s)
$$

**Effective EPE:**

$$
\text{Effective EPE} = \frac{1}{\min(1\text{ year}, T)} \int_0^{\min(1\text{ year}, T)} \text{Effective EE}(t) \, dt
$$

**Rationale:** Prevents gaming by structuring trades to have low EE at measurement dates but high EE in between.

---

## Potential Future Exposure (PFE)

**PFE** is a high-quantile measure of future exposure:

$$
\text{PFE}_\alpha(t) = \inf\{x : \mathbb{P}(E_t \le x) \ge \alpha\}
$$

Typically $\alpha = 0.95$ or $0.99$.

**Interpretation:** With probability $\alpha$, exposure at time $t$ will not exceed $\text{PFE}_\alpha(t)$.

**Relation to EE:**
- EE measures average exposure
- PFE measures tail exposure
- $\text{PFE}_\alpha(t) \ge \text{EE}(t)$ always

---

## Exposure Profile Shapes

Different products have characteristic exposure profiles:

### Interest Rate Swap

**Receiver swap (receive fixed, pay floating):**
- Exposure peaks mid-life
- "Hump-shaped" profile
- Pull-to-par effect near maturity

$$
\text{EE}(t) \text{ peaks at } t \approx T/2
$$

### FX Forward

- Exposure grows approximately linearly with time
- Maximum at maturity
- No intermediate payments to reset exposure

### Cross-Currency Swap

- Combines features of IRS and FX
- Notional exchange at maturity creates jump
- Complex profile shape

### Options

- Buyer has exposure; seller does not (after premium paid)
- Exposure depends on moneyness evolution

---

## Drivers of Exposure Profiles

### 1. Product Structure
- Payment schedules
- Optionality
- Notional exchange

### 2. Market Factors
- Interest rate volatility
- FX volatility
- Correlation structure

### 3. Portfolio Effects
- Netting benefits
- Collateral agreements
- Trade maturity mix

### 4. Time Effects
- Diffusion of market factors
- Pull-to-par for swaps
- Time decay for options

---

## Netting and Exposure

Under a **netting agreement**, exposure is calculated at the portfolio level:

$$
E_t^{\text{netted}} = \left(\sum_{i=1}^n V_{i,t}\right)^+ \le \sum_{i=1}^n V_{i,t}^+ = \sum_{i=1}^n E_{i,t}
$$

**Netting benefit:**

$$
\text{Netting Benefit} = \frac{\sum_i \text{EE}_i - \text{EE}_{\text{netted}}}{\sum_i \text{EE}_i}
$$

Netting is most valuable when trades have:
- Opposite signs (long and short)
- Different maturities
- Low correlation of values

---

## Collateralization and Exposure

**Collateral (margin)** reduces exposure:

$$
E_t^{\text{collateralized}} = \max(V_t - C_t, 0)
$$

where $C_t$ is the collateral held.

### Margin Period of Risk (MPOR)

Collateral is not instantaneously available. The **MPOR** is the time to:
- Call for additional margin
- Receive and process collateral
- Close out the position if counterparty defaults

Typical MPOR: 10 business days (bilateral), 5 days (CCP).

**Effective exposure under collateral:**

$$
\text{EE}^{\text{coll}}(t) = \mathbb{E}[\max(V_t - C_{t-\text{MPOR}}, 0)]
$$

---

## CVA and Exposure

**Credit Valuation Adjustment (CVA)** depends directly on exposure profiles:

$$
\text{CVA} = \text{LGD} \int_0^T \text{EE}(t) \cdot \lambda(t) \cdot e^{-\int_0^t (r(s) + \lambda(s)) ds} \, dt
$$

where:
- LGD = Loss Given Default (typically 60%)
- $\lambda(t)$ = default intensity (hazard rate)
- $r(t)$ = risk-free rate

**Discrete approximation:**

$$
\text{CVA} \approx \text{LGD} \sum_{i=1}^n \text{EE}(t_i) \cdot [\mathbb{Q}(\tau \le t_i) - \mathbb{Q}(\tau \le t_{i-1})] \cdot D(t_i)
$$

where $D(t)$ is the discount factor and $\mathbb{Q}(\tau \le t)$ is the default probability.

---

## Monte Carlo Simulation of Exposure

### Algorithm

1. **Simulate market scenarios:** Generate $N$ paths of risk factors $(S_t^{(j)})_{j=1}^N$
2. **Revalue portfolio:** For each path and time point, compute $V_t^{(j)}$
3. **Compute exposure:** $E_t^{(j)} = \max(V_t^{(j)}, 0)$
4. **Aggregate statistics:**
   - $\widehat{\text{EE}}(t) = \frac{1}{N} \sum_{j=1}^N E_t^{(j)}$
   - $\widehat{\text{PFE}}_\alpha(t) = $ empirical $\alpha$-quantile of $(E_t^{(j)})$

### Implementation Considerations

- **Time grid:** Balance accuracy vs. computation
- **Path count:** Typically $N = 1000$ to $10000$
- **Variance reduction:** Antithetic variates, control variates
- **Netting:** Apply at portfolio level, not trade level

---

## Peak Exposure

**Peak Exposure** is the maximum exposure over the portfolio's life:

$$
\text{Peak EE} = \max_{t \in [0,T]} \text{EE}(t)
$$

$$
\text{Peak PFE}_\alpha = \max_{t \in [0,T]} \text{PFE}_\alpha(t)
$$

Peak exposure is used for:
- Credit limit setting
- Counterparty approval
- Stress testing

---

## Key Takeaways

- Exposure is the positive part of portfolio value: $E_t = V_t^+$
- EE is expected exposure; PFE is tail exposure
- EPE (time-averaged EE) summarizes lifetime exposure
- Netting significantly reduces exposure for diversified portfolios
- Collateral reduces exposure but introduces MPOR considerations
- Exposure profiles are essential inputs to CVA calculations
- Monte Carlo simulation is the standard computation method

---

## Further Reading

- Gregory, J., *Counterparty Credit Risk and Credit Value Adjustment*
- Brigo, D., Morini, M., & Pallavicini, A., *Counterparty Credit Risk, Collateral and Funding*
- Pykhtin, M. & Zhu, S. (2007), "A Guide to Modeling Counterparty Credit Risk"
- Basel Committee, "The Standardised Approach for Measuring Counterparty Credit Risk Exposures"

---

## Exercises

**Exercise 1.** Sketch the typical exposure profile of a plain vanilla interest rate swap over its 10-year life. Explain why the exposure starts near zero, rises to a peak at approximately one-third to one-half of the swap's life, then declines back toward zero at maturity.

??? success "Solution to Exercise 1"
    The typical exposure profile of a 10-year plain vanilla interest rate swap follows a **hump-shaped** curve that can be understood through three phases.

    **Phase 1: Near zero at inception ($t \approx 0$).** At inception, the swap is priced at par (zero NPV), so the current exposure is zero. In the very short term, the swap rate has had little time to move away from the initial fixed rate, meaning the mark-to-market value is small. Thus the expected positive exposure $\text{EE}(0^+) \approx 0$.

    **Phase 2: Rising to a peak ($t \approx 3$--$5$ years).** Two competing forces shape the profile:

    - **Diffusion effect:** As time passes, interest rates diffuse away from their initial levels. Under a diffusion model, the standard deviation of rate changes grows as $\sigma\sqrt{t}$. This causes the distribution of swap values to widen, increasing the expected positive part $\mathbb{E}[V_t^+]$.
    - **Amortization effect:** As coupons are exchanged, the number of remaining cash flows decreases. A 10-year swap at year 7 behaves like a 3-year swap, which has less sensitivity (lower DV01) to rate movements.

    Early in the swap's life, the diffusion effect dominates because nearly all cash flows remain outstanding and the rate uncertainty is growing. The exposure therefore rises.

    **Phase 3: Decline toward zero at maturity ($t \to 10$ years).** As the swap approaches maturity, the remaining notional (in duration terms) shrinks rapidly. The amortization effect overtakes the diffusion effect. With only one or two coupons remaining, even a large rate move produces a small NPV change. At maturity, $V_T = 0$ (final exchange already settled), so $\text{EE}(T) = 0$.

    A commonly used approximation captures this shape:

    $$
    \text{EE}(t) \propto \sigma \sqrt{t} \cdot \frac{T - t}{T}
    $$

    The product $\sqrt{t} \cdot (T - t)$ peaks at roughly $t \approx T/3$ to $T/2$ (maximizing $\sqrt{t}(T-t)$ via calculus gives $t^* = T/5$ for the exact functional form, but in practice, discrete coupon effects shift the peak to roughly one-third to one-half of the swap's life). After this peak, the profile declines monotonically to zero.

---

**Exercise 2.** Define current exposure (CE), potential future exposure (PFE), and expected exposure (EE). For a 5-year FX forward with notional \$100 million, explain qualitatively how each measure evolves over time.

??? success "Solution to Exercise 2"
    **Definitions:**

    - **Current Exposure (CE):** The mark-to-market value of the portfolio if positive, otherwise zero:

    $$
    \text{CE} = V_0^+ = \max(V_0, 0)
    $$

    CE is a point-in-time measure of what would be lost if the counterparty defaulted right now (before recovery).

    - **Potential Future Exposure (PFE):** The maximum exposure at a future time $t$ at a given confidence level $\alpha$:

    $$
    \text{PFE}_\alpha(t) = \inf\{x : \mathbb{P}(E_t \le x) \ge \alpha\}
    $$

    PFE is a forward-looking quantile measure of tail exposure, analogous to Value-at-Risk for credit exposure.

    - **Expected Exposure (EE):** The average of the positive part of the portfolio value at future time $t$:

    $$
    \text{EE}(t) = \mathbb{E}[V_t^+]
    $$

    EE is a forward-looking average measure used in CVA calculations.

    **Evolution for a 5-year FX forward (notional \$100M):**

    An FX forward has no intermediate cash flows. Its value at time $t$ is driven by the deviation of the spot FX rate from the forward rate:

    $$
    V_t \approx N \cdot (F(t,T) - K) \cdot D(t,T)
    $$

    where $F(t,T)$ is the forward rate at time $t$ for delivery at $T$ and $K$ is the contracted rate.

    - **CE:** At inception, $V_0 = 0$, so $\text{CE} = 0$. Over time, as the spot FX rate moves, CE fluctuates. CE is always a snapshot: it could be large or small depending on current rates.

    - **PFE:** Grows approximately as $\sigma_{\text{FX}} \sqrt{t}$ because FX rate uncertainty increases with time. Since there are no intermediate payments to reset exposure, PFE increases monotonically, reaching its maximum at or near maturity $T = 5$ years. At the 95th percentile:

    $$
    \text{PFE}_{95\%}(t) \approx N \cdot \sigma_{\text{FX}} \cdot \sqrt{t} \cdot \Phi^{-1}(0.95)
    $$

    - **EE:** Also grows approximately as $\sigma_{\text{FX}} \sqrt{t}$, but is smaller than PFE because it measures the average rather than the tail:

    $$
    \text{EE}(t) \approx N \cdot \sigma_{\text{FX}} \cdot \sqrt{t} \cdot \phi(0)
    $$

    where $\phi(0) = 1/\sqrt{2\pi} \approx 0.399$.

    All three measures are monotonically increasing for the FX forward, with no hump shape, because there are no intermediate payments.

---

**Exercise 3.** An interest rate swap has a current mark-to-market value of \$5 million. Compute the current exposure. If the counterparty defaults today, what is the bank's loss assuming zero recovery? What if the mark-to-market is $-\$3$ million?

??? success "Solution to Exercise 3"
    **Case 1: MtM = +\$5 million.**

    The current exposure is:

    $$
    \text{CE} = \max(V_0, 0) = \max(5, 0) = \$5 \text{ million}
    $$

    If the counterparty defaults today with zero recovery, the bank's loss equals the current exposure:

    $$
    \text{Loss} = \text{CE} \times (1 - R) = \$5\text{M} \times (1 - 0) = \$5 \text{ million}
    $$

    The bank is owed \$5M by the counterparty, and with zero recovery, the entire amount is lost.

    **Case 2: MtM = $-$\$3 million.**

    The current exposure is:

    $$
    \text{CE} = \max(V_0, 0) = \max(-3, 0) = \$0
    $$

    The bank owes the counterparty \$3M. If the counterparty defaults, the bank still owes the \$3M to the counterparty's estate (it cannot simply walk away). Therefore the bank's loss from counterparty default is **zero** — the bank has no credit exposure because the derivative has negative value from the bank's perspective.

    Note: In practice, if netting is not in place and the counterparty's estate can selectively enforce contracts ("cherry-picking"), the situation is more complex. However, under standard close-out netting (ISDA Master Agreement), the negative-value trade is netted with other trades, and the analysis above applies to the net portfolio value.

---

**Exercise 4.** Explain why the exposure profile of a cross-currency swap differs from that of a single-currency interest rate swap. In particular, why does the cross-currency swap have a "rising then flat" profile rather than a "hump-shaped" profile?

??? success "Solution to Exercise 4"
    A **cross-currency swap** differs from a **single-currency interest rate swap** because it involves both interest rate risk and FX risk, and crucially, it includes an **exchange of notional** in different currencies at maturity.

    **Single-currency IRS profile (hump-shaped):**

    - No principal exchange (or same-currency principal that nets to zero)
    - Exposure driven solely by the present value of remaining fixed-vs-floating coupon differentials
    - Diffusion effect ($\sqrt{t}$) grows exposure early; amortization effect (fewer remaining coupons) reduces it late
    - Result: peak at roughly $T/3$ to $T/2$, then decline to zero at maturity

    **Cross-currency swap profile (rising then flat, or rising to maturity):**

    - **Coupon exchanges** in different currencies create exposure similar to an IRS, generating the hump-shaped component
    - **Notional exchange at maturity** creates a large FX exposure: at maturity, the two parties exchange principal amounts in different currencies. The value of this exchange depends on the prevailing FX rate and behaves like an FX forward
    - The FX forward component has exposure that grows as $\sigma_{\text{FX}} \sqrt{t}$, reaching its maximum at maturity

    The combined profile is the superposition of:

    1. A hump-shaped IRS-like component (from coupon differentials)
    2. A monotonically increasing FX forward-like component (from the notional exchange)

    The FX component dominates, especially for longer tenors, because the notional exchange is typically much larger than any single coupon. The result is a profile that:

    - Rises steadily as FX uncertainty accumulates
    - Does **not** decline near maturity (unlike the IRS) because the notional exchange creates peak exposure right at $T$
    - May appear "rising then flat" if the FX volatility effect stabilizes while the coupon amortization effect kicks in, but the profile remains elevated through maturity

    This is why cross-currency swaps carry significantly higher counterparty credit risk than single-currency swaps of the same tenor.

---

**Exercise 5.** A portfolio contains 50 interest rate swaps with the same counterparty. Some swaps have positive value and others negative. Explain why gross exposure (sum of positive values) overstates the actual credit exposure. How does a netting agreement change the exposure profile?

??? success "Solution to Exercise 5"
    **Gross exposure** is the sum of individual positive exposures:

    $$
    E^{\text{gross}} = \sum_{i=1}^{50} V_i^+ = \sum_{i=1}^{50} \max(V_i, 0)
    $$

    This counts every swap with a positive mark-to-market as a potential loss, ignoring the fact that swaps with negative values (amounts the bank owes) would offset positive values in the event of default.

    **Why gross exposure overstates credit exposure:**

    Consider a simple example: the bank has two swaps with the same counterparty, Swap A worth +\$10M and Swap B worth $-$\$8M. Gross exposure is $\$10\text{M} + \$0 = \$10\text{M}$. But if the counterparty defaults, under a netting agreement, only the net amount $\$10\text{M} - \$8\text{M} = \$2\text{M}$ is at risk.

    Mathematically, the netting inequality guarantees:

    $$
    E^{\text{net}} = \left(\sum_{i=1}^{50} V_i\right)^+ \le \sum_{i=1}^{50} V_i^+ = E^{\text{gross}}
    $$

    **How a netting agreement changes the exposure profile:**

    Under a bilateral netting agreement (ISDA Master Agreement), if the counterparty defaults:

    1. All 50 swaps are terminated simultaneously
    2. Their mark-to-market values are summed to a single net amount
    3. Only the positive net amount represents exposure

    For a portfolio of 50 swaps where some are receive-fixed and some are pay-fixed, the positive and negative values partially offset. The **netting benefit** increases when:

    - The portfolio contains **offsetting positions** (long and short swaps)
    - Trade values have **low or negative correlation** with each other
    - The portfolio is **diversified** across maturities and risk factors

    The netting factor $\text{NF} = \text{EE}^{\text{net}} / \text{EE}^{\text{gross}}$ is typically 0.3--0.6 for well-diversified swap portfolios, meaning netting reduces exposure by 40--70%.

    Without a netting agreement, the bank faces gross exposure (the counterparty's estate could "cherry-pick" profitable trades while defaulting on unprofitable ones), making the legal enforceability of netting critical.

---

**Exercise 6.** Describe the "amortizing" and "diffusing" effects that determine the shape of a swap's exposure profile. Why does the expected exposure initially grow (diffusion effect dominates) and then decline (amortization effect dominates)?

??? success "Solution to Exercise 6"
    The shape of a swap's expected exposure profile is determined by two competing effects:

    **Diffusion (spreading) effect:**

    As time progresses, interest rates diffuse away from their initial values. Under a standard model (e.g., mean-reverting Gaussian or lognormal), the uncertainty in the swap rate grows approximately as $\sigma\sqrt{t}$. This means the distribution of the swap's mark-to-market value $V_t$ widens over time. Since exposure is the positive part $E_t = V_t^+$, a wider distribution of $V_t$ leads to a larger expected positive part:

    $$
    \text{EE}(t) = \mathbb{E}[V_t^+] \uparrow \quad \text{as } \sigma_t = \sigma\sqrt{t} \text{ increases}
    $$

    For a normal distribution centered near zero, $\mathbb{E}[V_t^+] \approx \sigma_t \cdot \phi(0) = \sigma\sqrt{t}/\sqrt{2\pi}$, which grows as $\sqrt{t}$.

    **Amortization (pull-to-par) effect:**

    As the swap ages, the number of remaining coupon exchanges decreases. A swap with maturity $T$ observed at time $t$ behaves like a fresh swap with remaining life $T - t$. The sensitivity of the swap's value to interest rate changes (its DV01 or duration) is proportional to the remaining life. Consequently, even if rates have moved significantly, the NPV impact is smaller because fewer cash flows are affected:

    $$
    |V_t| \propto \text{DV01}(t) \cdot |\Delta r| \propto (T - t) \cdot |\Delta r|
    $$

    As $t \to T$, the DV01 shrinks to zero, pulling the exposure back toward zero.

    **Combined effect:**

    The expected exposure is approximately proportional to the product:

    $$
    \text{EE}(t) \propto \underbrace{\sigma\sqrt{t}}_{\text{diffusion}} \times \underbrace{(T - t)}_{\text{amortization}}
    $$

    - **Early in life** ($t$ small): $\sqrt{t}$ is growing rapidly while $(T-t) \approx T$ is nearly constant. The diffusion effect dominates, and EE increases.
    - **Late in life** ($t$ near $T$): $\sqrt{t}$ grows slowly (concave function) while $(T-t) \to 0$ rapidly. The amortization effect dominates, and EE decreases.
    - **Peak:** The maximum occurs where the marginal gain from diffusion equals the marginal loss from amortization. Taking the derivative and setting it to zero:

    $$
    \frac{d}{dt}\left[\sqrt{t}(T-t)\right] = \frac{T-t}{2\sqrt{t}} - \sqrt{t} = 0
    $$

    $$
    T - t = 2t \implies t^* = \frac{T}{3}
    $$

    So the peak occurs at approximately one-third of the swap's life. In practice, discrete coupon effects and mean reversion shift this peak toward $T/3$ to $T/2$.

    For a 10-year swap, the peak expected exposure occurs at roughly 3--5 years, consistent with the hump-shaped profile observed empirically.
