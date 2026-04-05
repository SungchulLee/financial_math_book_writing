# Credit Default Swaps (CDS)

A **Credit Default Swap (CDS)** is the fundamental traded instrument for transferring and pricing credit risk. It provides insurance-like protection against the default of a reference entity, allowing market participants to isolate and trade credit risk separately from interest rate risk.

---

## Contract Structure

### Parties and Roles

- **Protection buyer:** Pays periodic premium, receives compensation at default
- **Protection seller:** Receives periodic premium, pays compensation at default
- **Reference entity:** The entity whose default triggers the contract (not a party to the CDS)

### Key Terms

- **Notional amount:** $N$ (typically \$10 million for standard CDS)
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
\text{Protection Payment} = (1 - R) \times N
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
\text{Premium Payment at } t_i = s \times \Delta_i \times N \times \mathbf{1}_{\{\tau > t_i\}}
$$

where $\Delta_i = t_i - t_{i-1}$ is the accrual fraction (typically act/360).

Payments continue until:
- Maturity $T$ (if no default), or
- Default time $\tau$ (if default occurs)

### Accrued Premium

If default occurs between payment dates at time $\tau \in (t_{i-1}, t_i]$:

$$
\text{Accrued Premium} = s \times (\tau - t_{i-1}) \times N
$$

The accrued premium is typically paid at default (standard convention).

---

## Pricing Principle

### Fair Value Condition

At inception, the CDS spread $s$ is set so that the contract has zero initial value:

$$
\text{PV(Protection Leg)} = \text{PV(Premium Leg)}
$$

This no-arbitrage condition determines the **par CDS spread**.

### Present Value of Protection Leg

$$
\text{PV}_{\text{prot}} = (1-R) \times N \times \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^{\tau} r_u du} \mathbf{1}_{\{\tau \le T\}}\right]
$$

Using the intensity framework:

$$
\text{PV}_{\text{prot}} = (1-R) \times N \times \int_0^T D(0,t) \lambda_t S(0,t) \, dt
$$

where:
- $D(0,t) = \mathbb{E}[e^{-\int_0^t r_u du}]$ is the risk-free discount factor
- $S(0,t) = e^{-\int_0^t \lambda_u du}$ is the survival probability
- $\lambda_t$ is the default intensity

### Present Value of Premium Leg

$$
\text{PV}_{\text{prem}} = s \times N \times \left[\sum_{i=1}^n \Delta_i D(0, t_i) S(0, t_i) + \int_0^T D(0,t) (t - t_{i(t)-1}) \lambda_t S(0,t) \, dt\right]
$$

where the first sum is scheduled payments and the integral is expected accrued premium.

**Simplified (ignoring accrued):**

$$
\text{PV}_{\text{prem}} \approx s \times N \times \sum_{i=1}^n \Delta_i D(0, t_i) S(0, t_i) =: s \times N \times \text{RPV01}
$$

where **RPV01** (risky PV01) is the present value of 1 basis point of premium payments.

---

## Par CDS Spread Formula

### Derivation

Setting $\text{PV}_{\text{prot}} = \text{PV}_{\text{prem}}$:

$$
s_{\text{par}} = \frac{(1-R) \int_0^T D(0,t) \lambda_t S(0,t) \, dt}{\sum_{i=1}^n \Delta_i D(0, t_i) S(0, t_i) + \text{Accrued Adjustment}}
$$

### Simplified Formula

Ignoring accrued premium and assuming continuous premium payments:

$$
s_{\text{par}} = \frac{(1-R) \int_0^T D(0,t) \lambda_t S(0,t) \, dt}{\int_0^T D(0,t) S(0,t) \, dt}
$$

### Constant Intensity Approximation

With constant $r$, $\lambda$, and continuous payments:

$$
s_{\text{par}} = (1-R) \lambda
$$

This fundamental relationship shows that the **spread is proportional to intensity**, scaled by loss given default.

---

## CDS Pricing with Piecewise-Constant Intensity

### Standard Market Approach

Assume intensity is piecewise constant:

$$
\lambda(t) = \lambda_i \quad \text{for } t \in (T_{i-1}, T_i]
$$

### Protection Leg Value

$$
\text{PV}_{\text{prot}} = (1-R) N \sum_{i=1}^n \int_{T_{i-1}}^{T_i} D(0,t) \lambda_i S(0,t) \, dt
$$

With further simplification (constant rates within periods):

$$
\text{PV}_{\text{prot}} = (1-R) N \sum_{i=1}^n \lambda_i \int_{T_{i-1}}^{T_i} e^{-(r+\Lambda_i)t} \, dt
$$

where $\Lambda_i = \sum_{j \le i} \lambda_j (T_j - T_{j-1}) / T_i$ is the average intensity.

### Premium Leg Value (Risky Annuity)

$$
\text{RPV01} = \sum_{i=1}^n \Delta_i D(0, t_i) S(0, t_i)
$$

---

## CDS Mark-to-Market

### After Inception

Once a CDS is traded, spreads move and the contract gains or loses value.

**Current value to protection buyer:**

$$
\text{MTM} = \text{PV}_{\text{prot}} - s_{\text{contract}} \times N \times \text{RPV01}
$$

where $s_{\text{contract}}$ is the contractual spread (fixed at trade).

### Spread Change Approximation

For small spread changes:

$$
\Delta \text{MTM} \approx -(s_{\text{new}} - s_{\text{old}}) \times N \times \text{RPV01}
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
\text{Upfront} = (s_{\text{par}} - s_{\text{fixed}}) \times \text{RPV01} \times N
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
s_{\text{CDS}} \approx s_{\text{bond}}
$$

### Basis = CDS Spread − Bond Spread

$$
\text{Basis} = s_{\text{CDS}} - s_{\text{bond}}
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

---

## Exercises

**Exercise 1.** A 5-year CDS has notional $N = \$10$ million, recovery $R = 40\%$, constant risk-free rate $r = 4\%$, and constant intensity $\lambda = 2\%$. Compute the survival probabilities $S(0,t) = e^{-\lambda t}$ for $t = 1, 2, 3, 4, 5$. Then compute the risky PV01 assuming annual premium payments:

$$
\text{RPV01} = \sum_{i=1}^{5} \Delta_i\, D(0, t_i)\, S(0, t_i)
$$

with $\Delta_i = 1$ and $D(0,t_i) = e^{-r\,t_i}$.

??? success "Solution to Exercise 1"

    We are given $r = 4\%$, $\lambda = 2\%$, annual payments ($\Delta_i = 1$), and maturity $T = 5$ years.

    **Survival probabilities:**

    $$
    S(0,t) = e^{-\lambda t} = e^{-0.02 t}
    $$

    Computing for each year:

    | $t$ | $S(0,t) = e^{-0.02t}$ |
    |-----|----------------------|
    | 1 | $e^{-0.02} = 0.9802$ |
    | 2 | $e^{-0.04} = 0.9608$ |
    | 3 | $e^{-0.06} = 0.9418$ |
    | 4 | $e^{-0.08} = 0.9231$ |
    | 5 | $e^{-0.10} = 0.9048$ |

    **Discount factors:**

    $$
    D(0,t) = e^{-r t} = e^{-0.04 t}
    $$

    | $t$ | $D(0,t) = e^{-0.04t}$ |
    |-----|----------------------|
    | 1 | $e^{-0.04} = 0.9608$ |
    | 2 | $e^{-0.08} = 0.9231$ |
    | 3 | $e^{-0.12} = 0.8869$ |
    | 4 | $e^{-0.16} = 0.8521$ |
    | 5 | $e^{-0.20} = 0.8187$ |

    **Risky PV01:**

    $$
    \text{RPV01} = \sum_{i=1}^{5} \Delta_i \, D(0, t_i) \, S(0, t_i) = \sum_{i=1}^{5} e^{-0.04 i} \cdot e^{-0.02 i} = \sum_{i=1}^{5} e^{-0.06 i}
    $$

    Computing term by term:

    | $i$ | $e^{-0.06 i}$ |
    |-----|--------------|
    | 1 | 0.9418 |
    | 2 | 0.8869 |
    | 3 | 0.8353 |
    | 4 | 0.7866 |
    | 5 | 0.7408 |

    $$
    \text{RPV01} = 0.9418 + 0.8869 + 0.8353 + 0.7866 + 0.7408 = 4.1914 \text{ years}
    $$

    Alternatively, using the geometric series formula:

    $$
    \text{RPV01} = \sum_{i=1}^{5} e^{-0.06 i} = e^{-0.06} \cdot \frac{1 - e^{-0.06 \times 5}}{1 - e^{-0.06}} = \frac{0.9418 \times (1 - 0.7408)}{1 - 0.9418} = \frac{0.9418 \times 0.2592}{0.0582} \approx 4.192
    $$

---

**Exercise 2.** Continuing from Exercise 1, compute the present value of the protection leg:

$$
\text{PV}_{\text{prot}} = (1-R) \cdot N \cdot \int_0^5 e^{-rt}\,\lambda\, e^{-\lambda t}\,dt
$$

Then determine the par CDS spread $s_{\text{par}} = \text{PV}_{\text{prot}} / (N \times \text{RPV01})$. Verify that the approximate formula $s \approx (1-R)\lambda$ gives a close answer.

??? success "Solution to Exercise 2"

    From Exercise 1 we have $r = 4\%$, $\lambda = 2\%$, $R = 40\%$, $N = \$10$ million, and $\text{RPV01} = 4.192$ years.

    **Protection leg PV:**

    $$
    \text{PV}_{\text{prot}} = (1-R) \cdot N \cdot \int_0^5 e^{-rt} \lambda e^{-\lambda t} \, dt = 0.6 \times 10{,}000{,}000 \times 0.02 \int_0^5 e^{-0.06 t} \, dt
    $$

    Evaluating the integral:

    $$
    \int_0^5 e^{-0.06 t} \, dt = \frac{1 - e^{-0.30}}{0.06} = \frac{1 - 0.7408}{0.06} = \frac{0.2592}{0.06} = 4.320
    $$

    Therefore:

    $$
    \text{PV}_{\text{prot}} = 6{,}000{,}000 \times 0.02 \times 4.320 = 120{,}000 \times 4.320 = 518{,}400
    $$

    **Par CDS spread:**

    $$
    s_{\text{par}} = \frac{\text{PV}_{\text{prot}}}{N \times \text{RPV01}} = \frac{518{,}400}{10{,}000{,}000 \times 4.192} = \frac{518{,}400}{41{,}920{,}000} = 0.01237 = 123.7 \text{ bp}
    $$

    **Verification with approximate formula:**

    $$
    s \approx (1-R)\lambda = 0.6 \times 0.02 = 0.012 = 120 \text{ bp}
    $$

    The approximate formula gives 120 bp, which is close to the exact answer of 123.7 bp. The small discrepancy arises because the approximate formula assumes continuous premium payments and ignores the difference between discrete and continuous annuities. In the continuous case, the ratio $\int_0^T e^{-(r+\lambda)t} \lambda \, dt / \int_0^T e^{-(r+\lambda)t} \, dt = \lambda$ exactly, giving $s = (1-R)\lambda$. With annual payments, the premium leg annuity is slightly smaller than the continuous version, pushing the par spread slightly above $(1-R)\lambda$.

---

**Exercise 3.** Under the post-2009 Big Bang conventions, a CDS trades with a fixed coupon of 100 bp. If the par spread is 180 bp and the RPV01 is 4.3 years on a notional of \$10 million, compute the upfront payment:

$$
\text{Upfront} = (s_{\text{par}} - s_{\text{fixed}}) \times \text{RPV01} \times N
$$

Who pays the upfront, the protection buyer or the protection seller?

??? success "Solution to Exercise 3"

    We are given: $s_{\text{par}} = 180$ bp $= 0.0180$, $s_{\text{fixed}} = 100$ bp $= 0.0100$, RPV01 $= 4.3$ years, $N = \$10$ million.

    **Upfront payment:**

    $$
    \text{Upfront} = (s_{\text{par}} - s_{\text{fixed}}) \times \text{RPV01} \times N
    $$

    $$
    = (0.0180 - 0.0100) \times 4.3 \times 10{,}000{,}000
    $$

    $$
    = 0.0080 \times 4.3 \times 10{,}000{,}000 = 344{,}000
    $$

    The upfront payment is **\$344,000**.

    **Who pays?** Since $s_{\text{par}} > s_{\text{fixed}}$, the protection is worth more than the fixed coupon compensates. Therefore, the **protection buyer pays** the upfront amount of \$344,000 to the protection seller. This upfront payment compensates the seller for providing protection at a running coupon (100 bp) that is below the fair par spread (180 bp).

---

**Exercise 4.** A protection buyer enters a 5-year CDS at a contractual spread of 150 bp. One year later, the par spread has widened to 250 bp and the RPV01 on the remaining 4 years is 3.6. Compute the mark-to-market value to the protection buyer:

$$
\text{MTM} = (s_{\text{current}} - s_{\text{contract}}) \times N \times \text{RPV01}
$$

for $N = \$10$ million. Explain why spread widening benefits the protection buyer.

??? success "Solution to Exercise 4"

    We are given: $s_{\text{contract}} = 150$ bp $= 0.0150$, $s_{\text{current}} = 250$ bp $= 0.0250$, RPV01 $= 3.6$ years, $N = \$10$ million.

    **Mark-to-market value to the protection buyer:**

    $$
    \text{MTM} = (s_{\text{current}} - s_{\text{contract}}) \times N \times \text{RPV01}
    $$

    $$
    = (0.0250 - 0.0150) \times 10{,}000{,}000 \times 3.6
    $$

    $$
    = 0.0100 \times 36{,}000{,}000 = 360{,}000
    $$

    The mark-to-market value to the protection buyer is **+\$360,000**.

    **Why spread widening benefits the protection buyer:** The protection buyer locked in the right to receive default protection by paying only 150 bp per year. When market spreads widen to 250 bp, the cost of purchasing equivalent new protection has increased. The buyer holds an in-the-money position because they are paying below-market premiums for the same protection. Equivalently, the buyer could close the position by selling protection at 250 bp, netting a running gain of 100 bp per year on the remaining maturity. The present value of this running gain, discounted using the risky annuity, gives the \$360,000 mark-to-market profit.

---

**Exercise 5.** Explain the difference between physical settlement and cash settlement for a CDS. In a physical settlement, suppose the protection buyer delivers bonds with a market value of \$3.8 million against a face value of \$10 million. What is the effective recovery rate, and what net amount does the protection buyer receive?

??? success "Solution to Exercise 5"

    **Physical settlement:** The protection buyer delivers bonds issued by the reference entity with a face (par) value equal to the notional $N$ to the protection seller, who pays $N$ in cash. The buyer effectively sells the defaulted bonds at par.

    **Cash settlement:** An auction determines the recovery rate $R$. The protection seller pays $(1-R) \times N$ directly to the buyer. No bonds change hands.

    **Key differences:**

    - Physical settlement requires the buyer to source deliverable bonds, which can be scarce after default.
    - Cash settlement is more standardized and avoids delivery logistics. Post-2009, cash settlement via ISDA auction is the market standard.
    - Physical settlement gives the buyer a "cheapest-to-deliver" option (ability to deliver the cheapest qualifying bond), which can have value.

    **Numerical calculation:** The buyer delivers bonds with face value $N = \$10$ million and market value \$3.8 million. The seller pays $N = \$10$ million.

    **Effective recovery rate:**

    $$
    R_{\text{effective}} = \frac{\text{Market value of bonds}}{\text{Face value}} = \frac{3{,}800{,}000}{10{,}000{,}000} = 38\%
    $$

    **Net amount received by the protection buyer:**

    $$
    \text{Net payment} = N - \text{Market value of bonds delivered} = 10{,}000{,}000 - 3{,}800{,}000 = 6{,}200{,}000
    $$

    Equivalently, this is $(1 - R_{\text{effective}}) \times N = 0.62 \times 10{,}000{,}000 = \$6{,}200{,}000$.

    The protection buyer receives a net amount of **\$6.2 million**, which represents the loss given default.

---

**Exercise 6.** Consider a CDS with quarterly premium payments and a flat intensity $\lambda$. Derive the accrued premium adjustment term in the premium leg. Specifically, show that the expected accrued premium contribution is

$$
\int_0^T D(0,t)\, (\,t - t_{i(t)-1}\,)\, \lambda\, S(0,t)\, dt
$$

where $t_{i(t)-1}$ is the last scheduled payment date before $t$. Explain why this term is typically small relative to the scheduled premium payments.

??? success "Solution to Exercise 6"

    Consider quarterly payment dates $t_0, t_1, \ldots, t_n = T$ with $\Delta = t_i - t_{i-1} = 0.25$ years.

    If default occurs at time $\tau \in (t_{i-1}, t_i]$, the protection buyer owes accrued premium for the fraction of the period before default:

    $$
    \text{Accrued} = s \cdot (\tau - t_{i-1}) \cdot N
    $$

    **Deriving the expected accrued premium contribution:**

    The expected present value of the accrued premium over the entire life of the CDS is:

    $$
    \text{PV}_{\text{accrued}} = s \cdot N \cdot \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^{\tau} r_u \, du} (\tau - t_{i(\tau)-1}) \mathbf{1}_{\{\tau \le T\}}\right]
    $$

    Conditioning on the default time and using the intensity framework, $\mathbb{Q}(\tau \in dt) = \lambda_t S(0,t) \, dt$, so:

    $$
    \text{PV}_{\text{accrued}} = s \cdot N \cdot \int_0^T D(0,t) \, (t - t_{i(t)-1}) \, \lambda_t \, S(0,t) \, dt
    $$

    where $t_{i(t)-1}$ is the last payment date before $t$, and the factor $(t - t_{i(t)-1})$ is the accrued fraction at the moment of default.

    **Why this term is small:** The accrued fraction $t - t_{i(t)-1}$ ranges from 0 to $\Delta = 0.25$ years. On average over a quarter, it equals approximately $\Delta / 2 = 0.125$ years. Therefore the accrued adjustment is roughly:

    $$
    \text{PV}_{\text{accrued}} \approx s \cdot N \cdot \frac{\Delta}{2} \int_0^T D(0,t) \lambda_t S(0,t) \, dt
    $$

    Comparing with the scheduled premium PV:

    $$
    \text{PV}_{\text{scheduled}} = s \cdot N \cdot \sum_{i=1}^{n} \Delta \, D(0, t_i) \, S(0, t_i)
    $$

    The ratio of the accrued term to the scheduled term is approximately:

    $$
    \frac{\text{PV}_{\text{accrued}}}{\text{PV}_{\text{scheduled}}} \approx \frac{\frac{\Delta}{2} \int_0^T D \lambda S \, dt}{\Delta \sum D_i S_i}
    $$

    Since $\int_0^T D(0,t) \lambda S(0,t) \, dt$ represents the expected present value of one unit payment at default and $\lambda$ is typically small (e.g., 1--3%), the density of default in any given quarter is low. For typical credit-quality names with $\lambda = 2\%$, the probability of defaulting in any particular quarter is about 0.5%, so the accrued adjustment contributes only on the order of 0.5% of $\Delta/2 = 0.125$ years, which is negligible compared to the full annuity RPV01 of roughly 4--5 years.

---

**Exercise 7.** The CDS-bond basis is defined as $\text{Basis} = s_{\text{CDS}} - s_{\text{bond}}$. Discuss conditions under which the basis is (a) positive and (b) negative. A hedge fund observes a persistent negative basis of $-30$ bp for a particular reference entity. Describe a trading strategy to exploit this and identify the risks involved.

??? success "Solution to Exercise 7"

    **Conditions for positive basis ($s_{\text{CDS}} > s_{\text{bond}}$):**

    (a) A positive basis arises when CDS protection is relatively expensive compared to the bond spread:

    - **Counterparty risk in CDS:** CDS sellers may demand higher spreads to compensate for their own counterparty exposure.
    - **Cheapest-to-deliver option:** Physical settlement CDS embed an option for the buyer to deliver the cheapest qualifying bond, increasing the CDS value relative to a specific bond.
    - **High demand for protection:** During stress periods, concentrated demand for CDS protection (e.g., from hedgers or speculators) can push CDS spreads above bond spreads.
    - **Repo specialness:** If the reference bond trades special in the repo market, its yield is depressed, making the bond spread appear narrower.

    **Conditions for negative basis ($s_{\text{CDS}} < s_{\text{bond}}$):**

    (b) A negative basis arises when CDS protection is cheap relative to the bond spread:

    - **Funding costs:** Bonds require capital to purchase; investors with high funding costs demand a wider bond spread. CDS are unfunded, so they can trade tighter.
    - **Liquidity premium in bonds:** Illiquid bonds carry a liquidity premium that widens bond spreads beyond pure default compensation.
    - **Supply pressure:** Heavy issuance by the reference entity or forced selling of bonds (e.g., rating downgrades) can push bond spreads wider without a corresponding move in CDS.

    **Negative basis trading strategy:** The hedge fund observes a persistent negative basis of $-30$ bp, meaning CDS are cheap relative to bonds. The strategy is:

    1. **Buy the corporate bond** (earning the bond spread)
    2. **Buy CDS protection** on the same reference entity (paying the CDS spread)

    This is called a "negative basis trade." The bond pays a spread of, say, $s_{\text{bond}}$ over the risk-free rate, and the CDS costs $s_{\text{CDS}} = s_{\text{bond}} - 30$ bp. The net carry is approximately:

    $$
    \text{Net carry} \approx s_{\text{bond}} - s_{\text{CDS}} - \text{funding cost above risk-free} = 30 \text{ bp} - \text{funding spread}
    $$

    If the hedge fund can fund the bond purchase at or near the risk-free rate, the strategy earns approximately 30 bp per year with default risk hedged. If the basis converges to zero, there is an additional mark-to-market gain.

    **Risks involved:**

    - **Funding risk:** The bond must be financed, and funding costs may fluctuate or increase, eroding the carry.
    - **Basis widening:** The negative basis may widen further before converging, causing mark-to-market losses.
    - **Counterparty risk:** The CDS protection seller may default precisely when protection is needed (wrong-way risk).
    - **Liquidity risk:** Unwinding either leg during market stress may be costly.
    - **Maturity mismatch:** The bond and CDS maturities may not match exactly, introducing basis risk.
    - **Restructuring risk:** CDS may not cover all credit events that affect bond prices (e.g., soft restructuring).
