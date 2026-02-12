# Credit Default Swaps (CDS)

A **Credit Default Swap (CDS)** is the fundamental traded instrument for transferring and pricing credit risk. It provides insurance-like protection against the default of a reference entity, allowing market participants to isolate and trade credit risk separately from interest rate risk.

---

## Contract Structure

### Parties and Roles

- **Protection buyer:** Pays periodic premium, receives compensation at default
- **Protection seller:** Receives periodic premium, pays compensation at default
- **Reference entity:** The entity whose default triggers the contract (not a party to the CDS)

### Key Terms

- **Notional amount:** $N$ (typically $10 million for standard CDS)
- **Maturity:** $T$ (standard maturities: 1Y, 3Y, 5Y, 7Y, 10Y)
- **CDS spread:** $s$ (annual premium rate, quoted in basis points)
- **Recovery rate:** $R$ (typically assumed 40% for senior unsecured debt)
- **Reference entity:** The obligor whose credit is being protected

### Two Legs

**Protection Leg:** Payment from seller to buyer upon default
**Premium Leg:** Payments from buyer to seller until default or maturity

---

## Protection Leg

### Payoff at Default

If default occurs at time $\tau \le T$, the protection seller pays:

$$
\text{Protection Payment} = (1 - R) \times N,
$$

where:
- $1 - R$ is the **loss given default** (LGD)
- $N$ is the notional amount

### Settlement Mechanisms

**Physical settlement:**
- Buyer delivers defaulted bonds with face value $N$
- Seller pays buyer $N$
- Net effect: buyer receives $N - \text{Bond Value} \approx (1-R) \times N$

**Cash settlement:**
- Determined by auction process (ISDA Credit Event Auction)
- Recovery rate established by dealer bids
- Seller pays buyer $(1-R) \times N$ directly

Post-2009, cash settlement via auction is standard for most CDS.

---

## Premium Leg

### Periodic Payments

The protection buyer pays the CDS spread $s$ on scheduled dates $t_1, t_2, \ldots, t_n = T$:

$$
\text{Premium Payment at } t_i = s \times \Delta_i \times N \times \mathbf{1}_{\{\tau > t_i\}},
$$

where $\Delta_i = t_i - t_{i-1}$ is the accrual fraction (typically act/360).

Payments continue until:
- Maturity $T$ (if no default), or
- Default time $\tau$ (if default occurs)

### Accrued Premium

If default occurs between payment dates at time $\tau \in (t_{i-1}, t_i]$:

$$
\text{Accrued Premium} = s \times (\tau - t_{i-1}) \times N.
$$

The accrued premium is typically paid at default (standard convention).

---

## Pricing Principle

### Fair Value Condition

At inception, the CDS spread $s$ is set so that the contract has zero initial value:

$$
\text{PV(Protection Leg)} = \text{PV(Premium Leg)}.
$$

This no-arbitrage condition determines the **par CDS spread**.

### Present Value of Protection Leg

$$
\text{PV}_{\text{prot}} = (1-R) \times N \times \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^{\tau} r_u du} \mathbf{1}_{\{\tau \le T\}}\right].
$$

Using the intensity framework:

$$
\text{PV}_{\text{prot}} = (1-R) \times N \times \int_0^T D(0,t) \lambda_t S(0,t) \, dt,
$$

where:
- $D(0,t) = \mathbb{E}[e^{-\int_0^t r_u du}]$ is the risk-free discount factor
- $S(0,t) = e^{-\int_0^t \lambda_u du}$ is the survival probability
- $\lambda_t$ is the default intensity

### Present Value of Premium Leg

$$
\text{PV}_{\text{prem}} = s \times N \times \left[\sum_{i=1}^n \Delta_i D(0, t_i) S(0, t_i) + \int_0^T D(0,t) (t - t_{i(t)-1}) \lambda_t S(0,t) \, dt\right],
$$

where the first sum is scheduled payments and the integral is expected accrued premium.

**Simplified (ignoring accrued):**

$$
\text{PV}_{\text{prem}} \approx s \times N \times \sum_{i=1}^n \Delta_i D(0, t_i) S(0, t_i) =: s \times N \times \text{RPV01},
$$

where **RPV01** (risky PV01) is the present value of 1 basis point of premium payments.

---

## Par CDS Spread Formula

### Derivation

Setting $\text{PV}_{\text{prot}} = \text{PV}_{\text{prem}}$:

$$
s_{\text{par}} = \frac{(1-R) \int_0^T D(0,t) \lambda_t S(0,t) \, dt}{\sum_{i=1}^n \Delta_i D(0, t_i) S(0, t_i) + \text{Accrued Adjustment}}.
$$

### Simplified Formula

Ignoring accrued premium and assuming continuous premium payments:

$$
s_{\text{par}} = \frac{(1-R) \int_0^T D(0,t) \lambda_t S(0,t) \, dt}{\int_0^T D(0,t) S(0,t) \, dt}.
$$

### Constant Intensity Approximation

With constant $r$, $\lambda$, and continuous payments:

$$
s_{\text{par}} = (1-R) \lambda.
$$

This fundamental relationship shows that the **spread is proportional to intensity**, scaled by loss given default.

---

## CDS Pricing with Piecewise-Constant Intensity

### Standard Market Approach

Assume intensity is piecewise constant:
$$
\lambda(t) = \lambda_i \quad \text{for } t \in (T_{i-1}, T_i].
$$

### Protection Leg Value

$$
\text{PV}_{\text{prot}} = (1-R) N \sum_{i=1}^n \int_{T_{i-1}}^{T_i} D(0,t) \lambda_i S(0,t) \, dt.
$$

With further simplification (constant rates within periods):

$$
\text{PV}_{\text{prot}} = (1-R) N \sum_{i=1}^n \lambda_i \int_{T_{i-1}}^{T_i} e^{-(r+\Lambda_i)t} \, dt,
$$

where $\Lambda_i = \sum_{j \le i} \lambda_j (T_j - T_{j-1}) / T_i$ is the average intensity.

### Premium Leg Value (Risky Annuity)

$$
\text{RPV01} = \sum_{i=1}^n \Delta_i D(0, t_i) S(0, t_i).
$$

---

## CDS Mark-to-Market

### After Inception

Once a CDS is traded, spreads move and the contract gains or loses value.

**Current value to protection buyer:**

$$
\text{MTM} = \text{PV}_{\text{prot}} - s_{\text{contract}} \times N \times \text{RPV01},
$$

where $s_{\text{contract}}$ is the contractual spread (fixed at trade).

### Spread Change Approximation

For small spread changes:

$$
\Delta \text{MTM} \approx -(s_{\text{new}} - s_{\text{old}}) \times N \times \text{RPV01}.
$$

If spreads widen:
- Protection buyer gains (insurance is more valuable)
- Protection seller loses

---

## Standard CDS Conventions (Post-2009)

### Big Bang Protocol

ISDA standardized CDS trading:

1. **Fixed coupons:** 100 bp or 500 bp running spread (not par spread)
2. **Upfront payment:** Difference between par spread and fixed coupon, PV'd
3. **Standard maturities:** IMM dates (March 20, June 20, Sept 20, Dec 20)
4. **Standard recovery:** 40% for senior, 20% for subordinated

### Upfront Payment

$$
\text{Upfront} = (s_{\text{par}} - s_{\text{fixed}}) \times \text{RPV01} \times N.
$$

If $s_{\text{par}} > s_{\text{fixed}}$: protection buyer pays upfront
If $s_{\text{par}} < s_{\text{fixed}}$: protection buyer receives upfront

---

## Credit Events

### ISDA Definitions

Standard credit events triggering CDS:

1. **Bankruptcy:** Insolvency, receivership, administration
2. **Failure to pay:** Missed payment beyond grace period
3. **Restructuring:** Debt modification adverse to creditors
4. **Obligation acceleration:** Early due upon covenant breach
5. **Repudiation/Moratorium:** Government debt-specific

### Deliverable Obligations

For physical settlement, delivered bonds must be:
- Senior pari passu with reference obligation
- Same currency (or specified currencies)
- Maturity within limits

---

## Numerical Example

**Setup:**
- Notional: $N = 10$ million
- Maturity: $T = 5$ years
- Recovery: $R = 40\%$
- Risk-free rate: $r = 3\%$ (flat)
- Intensity: $\lambda = 150$ bp = 1.5%
- Premium frequency: Quarterly

**Step 1: Survival probabilities**

$$
S(0, t) = e^{-0.015 t}
$$

At $T = 5$: $S(0,5) = e^{-0.075} = 0.9277$

**Step 2: Risky PV01**

$$
\text{RPV01} = \sum_{i=1}^{20} 0.25 \times e^{-0.03 \times t_i} \times e^{-0.015 \times t_i} = \sum_{i=1}^{20} 0.25 \times e^{-0.045 \times 0.25i}
$$

$$
\text{RPV01} = 0.25 \times \frac{1 - e^{-0.045 \times 5}}{1 - e^{-0.045 \times 0.25}} \approx 4.45 \text{ years}
$$

**Step 3: Protection leg PV**

$$
\text{PV}_{\text{prot}} = 0.6 \times 10\text{M} \times \int_0^5 e^{-0.03t} \times 0.015 \times e^{-0.015t} \, dt
$$

$$
= 6\text{M} \times 0.015 \times \frac{1 - e^{-0.225}}{0.045} = 90,000 \times 4.47 = 402,300
$$

**Step 4: Par spread**

$$
s_{\text{par}} = \frac{402,300}{10\text{M} \times 4.45} = \frac{402,300}{44,500,000} = 0.00904 = 90.4 \text{ bp}
$$

**Check:** Approximate formula: $s \approx (1-R)\lambda = 0.6 \times 150 = 90$ bp ✓

---

## CDS vs. Bond Spread Basis

### Theoretical Relationship

In theory, the CDS spread should equal the bond spread (over risk-free):

$$
s_{\text{CDS}} \approx s_{\text{bond}}.
$$

### Basis = CDS Spread − Bond Spread

$$
\text{Basis} = s_{\text{CDS}} - s_{\text{bond}}.
$$

**Positive basis:** CDS more expensive (protection costly relative to bonds)
**Negative basis:** CDS cheaper (protection cheap relative to bonds)

### Causes of Basis

- **Funding costs:** Bonds require capital; CDS are unfunded
- **Counterparty risk:** CDS have counterparty exposure
- **Liquidity differences:** CDS often more liquid
- **Cheapest-to-deliver option:** Physical settlement optionality
- **Repo specialness:** Bonds may trade special in repo

---

## Key Takeaways

- CDS transfer credit risk via premium and protection legs
- Par spread is determined by equating leg values
- Approximate relationship: $s \approx (1-R) \lambda$
- Post-2009 conventions use fixed coupons with upfront payments
- RPV01 measures spread sensitivity
- CDS-bond basis reflects funding, liquidity, and counterparty effects

---

## Further Reading

- O'Kane, D. (2008). *Modelling Single-name and Multi-name Credit Derivatives*. Wiley.
- Hull, J. C., & White, A. (2000). Valuing credit default swaps I: No counterparty default risk. *Journal of Derivatives*, 8(1), 29–40.
- Duffie, D. (1999). Credit swap valuation. *Financial Analysts Journal*, 55(1), 73–87.
- ISDA (2003). *2003 ISDA Credit Derivatives Definitions*.
