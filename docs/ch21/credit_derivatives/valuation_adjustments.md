# Valuation Adjustments


Credit derivatives pricing in practice requires **valuation adjustments** that go beyond idealized default models. These adjustments reflect counterparty risk, funding costs, and collateralization.

---

## Motivation for adjustments


Classical pricing assumes:

- default-free counterparties,
- frictionless funding,
- perfect collateralization.

Real markets violate these assumptions.

---

## Credit Valuation Adjustment (CVA)


Recall (see [§ XVA](../../ch22/valuation_adjustments_xva/cva_dva.md)): **CVA** accounts for counterparty default risk and reduces a derivative's value:

$$
\text{CVA} = \mathbb{E}[\text{Exposure} \times \text{Loss Given Default}]
$$

---

## Other XVA components


Recall (see [§ XVA](../../ch22/valuation_adjustments_xva/cva_dva.md)): the family of XVA adjustments includes **DVA** (own default), **FVA** (funding), and **MVA** (margin).

---

## Interaction with CDS pricing


For CDS:

- counterparty risk affects premium valuation,
- collateral agreements mitigate but do not eliminate XVA,
- standardized CDS reduce some complexity.

---

## Key takeaways


- Valuation adjustments are essential for realistic pricing.
- CVA, DVA, and FVA materially affect values.
- Modern pricing integrates XVA into credit models.

---

## Further reading


- Gregory, *Counterparty Credit Risk*.
- Brigo, Morini & Pallavicini, XVA theory.

---

## Exercises

**Exercise 1.** A bank enters a 5-year interest rate swap with a counterparty whose 5-year CDS spread is 200 bp and recovery rate is $R = 40\%$. The expected positive exposure (EPE) of the swap is estimated at \$5 million. Using the simplified unilateral CVA formula

$$
\text{CVA} \approx (1 - R) \times \text{Spread} \times \text{EPE} \times T
$$

compute the approximate CVA. Explain why this adjustment reduces the swap's value to the bank.

??? success "Solution to Exercise 1"

    **Given:**

    - Counterparty 5-year CDS spread: $s_C = 200$ bp $= 0.0200$
    - Recovery rate: $R = 40\%$
    - Expected Positive Exposure (EPE): \$5 million
    - Maturity: $T = 5$ years

    **Simplified unilateral CVA:**

    $$
    \text{CVA} \approx (1 - R) \times s_C \times \text{EPE} \times T
    $$

    $$
    = (1 - 0.40) \times 0.0200 \times 5{,}000{,}000 \times 5
    $$

    $$
    = 0.60 \times 0.0200 \times 5{,}000{,}000 \times 5
    $$

    $$
    = 0.012 \times 5{,}000{,}000 \times 5 = 60{,}000 \times 5 = \$300{,}000
    $$

    The approximate CVA is **\$300,000**.

    **Why CVA reduces the swap's value to the bank:**

    The bank holds a positive expected exposure (EPE = \$5 million) to the counterparty, meaning the swap is "in the money" on average for the bank. If the counterparty defaults, the bank loses some or all of this positive value. The CVA quantifies the expected cost of this potential loss:

    $$
    \text{CVA} = \text{Expected loss from counterparty default}
    $$

    The risk-free value of the swap (ignoring counterparty risk) must be reduced by the CVA to reflect the possibility that the counterparty may not honor its obligations:

    $$
    V_{\text{adjusted}} = V_{\text{risk-free}} - \text{CVA}
    $$

    The CVA acts like an insurance premium that the bank implicitly "pays" for bearing the counterparty's credit risk. The larger the counterparty's CDS spread (reflecting higher default probability), the larger the exposure, or the longer the maturity, the greater this reduction.

---

**Exercise 2.** Explain the economic meaning of Debit Valuation Adjustment (DVA). A bank with a 5-year CDS spread of 100 bp computes its DVA on a derivative portfolio. Why is DVA sometimes criticized as a "benefit from own deterioration"? Discuss whether DVA should be included in the bank's reported P&L.

??? success "Solution to Exercise 2"

    **Economic meaning of DVA:**

    The Debit Valuation Adjustment (DVA) is the mirror image of CVA from the bank's own perspective. It accounts for the possibility that **the bank itself** may default on its derivative obligations. Mathematically:

    $$
    \text{DVA} \approx (1 - R_{\text{bank}}) \times s_{\text{bank}} \times \text{ENE} \times T
    $$

    where ENE is the Expected Negative Exposure (the expected amount the bank owes to the counterparty) and $s_{\text{bank}}$ is the bank's own CDS spread.

    DVA represents the value to the bank of the option to "walk away" from its obligations through default. If the bank defaults when it owes money on a derivative, it pays only the recovery fraction---the counterparty absorbs the loss. This possibility has economic value to the bank.

    **For the bank with a 100 bp CDS spread:**

    The bank computes DVA using its own credit spread and the exposure profile where the bank owes money to counterparties. A higher bank CDS spread increases DVA.

    **"Benefit from own deterioration" criticism:**

    DVA is controversial because as the bank's credit quality worsens (CDS spread widens), DVA increases, creating a **mark-to-market profit** for the bank. This is counterintuitive and ethically questionable:

    - A bank approaching distress would report improved P&L from higher DVA
    - During the 2008 crisis, several banks reported billions in DVA "gains" as their own creditworthiness collapsed
    - The "gains" are unrealizable: the bank cannot monetize the option to default on its own obligations

    **Should DVA be included in reported P&L?**

    Arguments for inclusion:

    - Bilateral pricing theory requires both CVA and DVA for consistency
    - Without DVA, two counterparties would disagree on the fair value of a trade
    - IFRS 13 and ASC 820 accounting standards require DVA in fair value measurement

    Arguments against:

    - DVA gains are unrealizable and cannot be hedged (the bank cannot trade its own default)
    - DVA creates perverse incentives (profit from deterioration)
    - Prudential regulators (Basel III) do not allow DVA gains to count toward regulatory capital
    - Some firms exclude DVA from internal risk management P&L while including it in accounting P&L

    The current consensus in practice is to include DVA in accounting fair value (as required by standards) but to exclude or filter it from economic P&L and risk management metrics.

---

**Exercise 3.** A fully collateralized CDS with daily margining has near-zero CVA. Explain why. Then describe a scenario where residual CVA remains even with collateralization (e.g., gap risk, margin period of risk). How does the margin period of risk affect the CVA calculation?

??? success "Solution to Exercise 3"

    **Why a fully collateralized CDS with daily margining has near-zero CVA:**

    CVA arises from the possibility that the counterparty defaults while owing a positive amount. With daily collateralization:

    1. Each day, the CDS is marked to market and the losing party posts collateral equal to its obligation
    2. If the counterparty defaults, the surviving party holds collateral approximately equal to the current exposure
    3. The net uncollateralized exposure is close to zero at any point, so:

    $$
    \text{CVA} \approx (1 - R) \times \mathbb{E}\left[\int_0^T \text{Uncollateralized Exposure}_t \, d\mathbb{Q}(\tau_C \le t)\right] \approx 0
    $$

    **Scenario where residual CVA remains:**

    Even with daily margining, CVA is not exactly zero due to the **margin period of risk (MPoR)**, which is the time between the counterparty's last successful collateral posting and the close-out of the position after default. During this period, the surviving party has exposure that is not covered by posted collateral.

    Consider this timeline:

    1. Day 0: Counterparty posts full collateral (exposure = 0)
    2. Day 1: Counterparty misses margin call (first sign of trouble)
    3. Days 2--10: Legal process, close-out negotiation, replacement trade execution
    4. Day 10: Position is fully closed out

    During days 1--10 (the MPoR, typically assumed to be 10 business days for bilateral OTC, 5 days for centrally cleared), the CDS mark-to-market can move against the surviving party. For example:

    - **Gap risk:** If the reference entity in the CDS also defaults or has a credit event during the MPoR, the CDS value can jump discontinuously. The protection buyer may face a large positive exposure exactly when the protection seller (counterparty) has defaulted.
    - **Spread volatility:** CDS spreads can move significantly over 10 business days, creating uncollateralized exposure.

    **Effect of MPoR on CVA calculation:**

    The residual CVA with collateralization is:

    $$
    \text{CVA}_{\text{collateralized}} \approx (1 - R) \times \mathbb{E}\left[\int_0^T \text{MPoR Exposure}_t \, d\mathbb{Q}(\tau_C \le t)\right]
    $$

    where MPoR Exposure is the potential change in mark-to-market during the margin period of risk. This is much smaller than uncollateralized CVA but is non-zero and can be material for volatile underlyings or during periods of market stress.

---

**Exercise 4.** Funding Valuation Adjustment (FVA) arises when a derivative's collateral requirements generate funding costs above the risk-free rate. If a bank's funding spread over the risk-free rate is 50 bp and the uncollateralized derivative has an average positive value of \$20 million over 5 years, estimate the FVA. Discuss whether FVA should be passed on to the client or absorbed by the bank's treasury.

??? success "Solution to Exercise 4"

    **Given:**

    - Bank's funding spread over risk-free rate: 50 bp $= 0.50\%$
    - Average positive value of uncollateralized derivative: \$20 million
    - Time horizon: 5 years

    **FVA estimate:**

    FVA represents the cost of funding the uncollateralized derivative exposure at rates above the risk-free rate. Using a simplified calculation:

    $$
    \text{FVA} \approx \text{Funding spread} \times \text{Average positive value} \times T
    $$

    $$
    = 0.0050 \times 20{,}000{,}000 \times 5 = \$500{,}000
    $$

    The approximate FVA is **\$500,000**.

    This means the bank incurs \$500,000 in excess funding costs (above risk-free) over the life of the derivative to finance the positive exposure.

    **Should FVA be passed on to the client or absorbed by treasury?**

    **Arguments for passing FVA to the client:**

    - FVA represents a real economic cost to the bank; ignoring it underprices the derivative
    - If the bank does not charge FVA, it subsidizes clients with high funding costs
    - Competitive pricing requires reflecting all costs, including funding
    - Without FVA, the trading desk shows a "profit" that treasury must subsidize

    **Arguments for absorbing FVA in treasury:**

    - FVA is a bank-specific cost (different banks have different funding spreads), so it should not affect market-consistent (risk-neutral) pricing
    - Passing FVA to clients makes the bank's pricing uncompetitive against better-funded rivals
    - If both counterparties charge FVA, they compute different fair values for the same trade, creating a "no-trade zone"
    - FVA violates the law of one price: the same derivative has different values depending on who trades it
    - Theoretically, if the Modigliani-Miller theorem held, funding costs would not affect derivative valuation

    **Current practice:** Most large dealer banks include FVA in derivative pricing, typically through an FVA desk or central XVA desk that charges/credits trading desks for funding costs. The FVA is partially passed to clients (especially for large, long-dated, uncollateralized trades) and partially absorbed as a cost of doing business. The exact allocation depends on competitive dynamics, client relationships, and internal policies.

---

**Exercise 5.** Compare and contrast CVA, DVA, FVA, and MVA. For each adjustment, state (a) what risk or cost it captures, (b) whether it increases or decreases the derivative's value to the bank, and (c) which market data is needed for its computation.

??? success "Solution to Exercise 5"

    | Adjustment | Risk/Cost Captured | Effect on Bank's Value | Market Data Needed |
    |-----------|-------------------|----------------------|-------------------|
    | **CVA** | Counterparty default risk (loss if counterparty defaults while owing money) | **Decreases** value (cost of bearing counterparty credit risk) | Counterparty CDS spreads, recovery rates, exposure profiles (Monte Carlo simulation of underlying risk factors) |
    | **DVA** | Bank's own default risk (bank may default while owing money) | **Increases** value (benefit from the possibility of the bank's own default) | Bank's own CDS spread, recovery rate, negative exposure profiles |
    | **FVA** | Funding costs above risk-free rate for uncollateralized derivative positions | **Decreases** value when the bank funds positive exposure; **increases** value when the bank receives funding benefit from negative exposure | Bank's funding curve (treasury funding spreads), collateral agreements (CSA terms), expected funding profiles |
    | **MVA** | Cost of posting initial margin (regulatory or CCP margin) that must be funded | **Decreases** value (initial margin must be funded at the bank's borrowing cost but earns only the risk-free rate or less) | Initial margin model (SIMM or CCP model), bank's funding spread, expected margin profiles over the trade's life |

    **Summary of interactions:**

    The total XVA adjustment is approximately:

    $$
    \text{XVA} = -\text{CVA} + \text{DVA} - \text{FVA} - \text{MVA}
    $$

    In practice, these adjustments are not fully additive due to interactions (e.g., collateralization reduces CVA but increases MVA; netting reduces all XVAs). The net XVA is computed at the portfolio level, accounting for netting sets and collateral agreements.

    CVA is typically the largest adjustment for uncollateralized trades, while MVA has become increasingly important since the introduction of mandatory initial margin requirements for non-cleared derivatives.

---

**Exercise 6.** Consider a CDS where both the protection buyer and the protection seller have non-trivial default risk. Explain how bilateral CVA modifies the standard CDS pricing formula. Why does counterparty risk in a CDS create "wrong-way risk" (i.e., the protection seller is more likely to default precisely when protection is needed)?

??? success "Solution to Exercise 6"

    **Bilateral CVA modification of CDS pricing:**

    In standard CDS pricing, both the protection buyer (B) and seller (S) are assumed default-free. The fair spread equates:

    $$
    \text{PV}_{\text{prot}} = s \times N \times \text{RPV01}
    $$

    With bilateral CVA, both parties face counterparty risk. The adjusted CDS value to the buyer becomes:

    $$
    V_{\text{bilateral}} = V_{\text{default-free}} - \text{CVA}_B + \text{DVA}_B
    $$

    where:

    - $\text{CVA}_B$ is the buyer's credit valuation adjustment for the seller's default risk
    - $\text{DVA}_B$ is the buyer's debit valuation adjustment for the buyer's own default risk

    **Specifically for a CDS:**

    The protection buyer faces exposure to the seller's default primarily through the **protection leg**: if the reference entity defaults and the seller has also defaulted, the buyer loses the protection payment $(1-R)N$. The bilateral CVA adjusts for this:

    $$
    \text{CVA}_{\text{buyer}} = (1-R_S) \int_0^T \mathbb{E}\left[D(0,t) \cdot \text{Exposure}_t^+\right] \lambda_S(t) S_S(0,t) \, dt
    $$

    where $\lambda_S$ and $S_S$ are the seller's default intensity and survival probability, and $\text{Exposure}_t^+$ is the buyer's positive exposure at time $t$.

    The protection seller faces exposure to the buyer's default through the **premium leg**: if the buyer defaults while the CDS has positive value (post spread widening), the seller loses the remaining premium stream.

    **Why CDS creates wrong-way risk:**

    Wrong-way risk in a CDS arises from the correlation between the reference entity's and the protection seller's credit quality:

    1. **The protection buyer's exposure is largest when protection is most needed.** When the reference entity's credit deteriorates (spreads widen), the CDS becomes more valuable to the buyer (mark-to-market increases). The buyer's exposure to the seller's default is highest precisely when the protection payment is most likely to be triggered.

    2. **The protection seller is more likely to default during credit crises.** If the seller is a financial institution exposed to the same credit markets (e.g., a bank with exposure to the same sector as the reference entity), the seller's creditworthiness declines during market-wide credit events. This is especially severe for:
        - Monoline insurers that sold vast amounts of CDS protection (AIG in 2008)
        - Banks with concentrated credit exposure in the same sector

    3. **Positive correlation between exposure and counterparty default probability.** The exposure to the seller peaks when the reference entity is near default. If the seller's default probability is correlated with the reference entity's default (e.g., both are affected by the same systematic credit factor), then:

        $$
        \text{CVA}_{\text{wrong-way}} > \text{CVA}_{\text{independent}}
        $$

        The CVA computed under independence assumptions underestimates the true cost of counterparty risk.

    This was dramatically illustrated during the 2008 financial crisis, when AIG's inability to honor CDS protection payments created systemic risk, precisely because AIG's credit deteriorated simultaneously with the mortgage-backed securities it had insured.
