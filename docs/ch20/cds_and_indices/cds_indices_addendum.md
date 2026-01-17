# CDS and Indices: Supplementary Content

This addendum addresses enhancement suggestions from the chapter review, including CDS index tranches, index skew dynamics, CDS index options, and the ISDA Standard Model.

---

## CDS Index Tranches


**Tranches slice credit index risk into layers with different risk-return profiles:**

### Tranche Structure


**The credit index loss distribution:**

For a portfolio of $N$ credits with recovery $R$:

$$
L = \sum_{i=1}^{N} \frac{(1-R)}{N} \times \mathbf{1}_{\{\text{Default}_i\}}
$$

**Tranches represent slices of this distribution:**

| Tranche | Attachment | Detachment | Notional Exposure |
|---------|------------|------------|-------------------|
| Equity | 0% | 3% | 3% of index |
| Junior Mezz | 3% | 7% | 4% of index |
| Senior Mezz | 7% | 15% | 8% of index |
| Senior | 15% | 30% | 15% of index |
| Super Senior | 30% | 100% | 70% of index |

### Tranche Mechanics


**Tranche payoff for protection seller:**

$$
\text{Loss to Tranche}(K_1, K_2) = \min(\max(L - K_1, 0), K_2 - K_1)
$$

Where:
- $K_1$ = attachment point
- $K_2$ = detachment point
- $L$ = portfolio loss

**Example: 3-7% Mezzanine Tranche**

| Portfolio Loss | Loss to 3-7% Tranche | Tranche Recovery |
|----------------|---------------------|------------------|
| 0% | 0% | 100% |
| 2% | 0% | 100% |
| 3% | 0% | 100% |
| 5% | 2% | 50% |
| 7% | 4% | 0% |
| 10% | 4% | 0% |

### Tranche Economics


**1. Equity Tranche (0-3%):**

- **First loss:** Bears all losses until 3% portfolio loss
- **Leverage:** ~15-20x (small notional, big exposure)
- **Spread:** Typically 30-50% upfront + 500 bp running
- **Delta:** Very high (1.5-3.0 per bp index move)
- **Correlation:** Long correlation (benefits if defaults cluster)
- **User:** Hedge funds seeking leveraged credit exposure

**Pricing intuition:** If expected loss is 5%, equity tranche (0-3%) absorbs all of it with 67% probability. Premium must be very high.

**2. Mezzanine Tranches (3-7%, 7-15%):**

- **Second/third loss:** Hit after equity exhausted
- **Leverage:** 5-10x
- **Spread:** 200-600 bp running
- **Delta:** Moderate (0.5-1.5 per bp)
- **Correlation:** Complex (depends on attachment)
- **User:** Relative value traders, structured credit funds

**3. Senior/Super Senior (15%+):**

- **Tail risk:** Only hit in severe scenarios
- **Leverage:** <2x
- **Spread:** 10-50 bp (very low)
- **Delta:** Low (<0.3 per bp)
- **Correlation:** Short correlation (benefits if defaults spread out)
- **User:** Banks (capital relief), insurance companies

### Correlation and Tranches


**The correlation paradox:**

$$
\text{Equity Value} \uparrow \text{ as } \rho \uparrow
$$

$$
\text{Senior Value} \downarrow \text{ as } \rho \uparrow
$$

**Intuition:**

- **High correlation:** Defaults cluster → Either no defaults OR many defaults
- **Equity likes this:** Either protected (no defaults) or exhausted anyway (many defaults same result)
- **Senior hates this:** In cluster scenario, senior gets hit; in no-default scenario, senior was never at risk anyway

**Correlation trading:**

- **Long correlation:** Long equity, short mezzanine
- **Short correlation:** Short equity, long mezzanine

**Base correlation:** The implied correlation that makes tranche price consistent with index.

| Tranche | Typical Base Correlation |
|---------|-------------------------|
| 0-3% | 15-25% |
| 3-7% | 25-35% |
| 7-15% | 35-45% |
| 15-30% | 45-55% |

---

## Index Skew Dynamics


**The index skew measures the difference between the index price and the theoretical value from constituents:**

### Defining Index Skew


**Theoretical index spread:**

$$
S_{\text{index}}^{\text{theory}} = \frac{1}{N} \sum_{i=1}^{N} S_i
$$

Where $S_i$ = single-name CDS spread for constituent $i$

**Index skew:**

$$
\text{Skew} = S_{\text{index}}^{\text{market}} - S_{\text{index}}^{\text{theory}}
$$

**Alternative definition (intrinsic):**

$$
\text{Intrinsic Skew} = P_{\text{index}}^{\text{market}} - \sum_{i} w_i P_i^{\text{single-name}}
$$

### Skew Drivers


**1. Liquidity Premium:**
- Index more liquid than single names
- Index trades tighter (negative skew common)
- Typical: -2 to -5 bp for CDX IG

**2. Cheapest-to-Deliver:**
- At default, protection buyer can deliver any deliverable bond
- CTD option has value
- Widens index relative to average (positive skew contribution)

**3. Hedging Demand:**
- Portfolio managers hedge with index (more liquid)
- Creates buying pressure on index protection
- Widens index (positive skew)

**4. Technical Flows:**
- Index rebalancing
- ETF creation/redemption
- Dealer inventory

### Historical Skew Patterns


| Market Condition | Typical Skew | Direction |
|------------------|--------------|-----------|
| Normal/calm | -2 to +2 bp | Neutral |
| Risk-on rally | -5 to -10 bp | Index tight |
| Stress/crisis | +10 to +30 bp | Index wide |
| Panic (2008, 2020) | +50 to +100 bp | Index very wide |

**2008 Financial Crisis:**
- Peak skew: +85 bp (Oct 2008)
- Index at 250 bp, single-name average at 165 bp
- Cause: Massive hedging demand, single-name illiquidity

**March 2020 COVID:**
- Peak skew: +45 bp
- Normalized within 4 weeks as Fed stepped in

### Trading the Skew


**Positive skew (index wide vs singles):**

- Sell index protection (receive premium)
- Buy single-name protection (pay premium)
- Net: Receive skew × notional

**Negative skew (index tight vs singles):**

- Buy index protection
- Sell single-name protection
- Net: Receive |skew| × notional

**Risks:**
- Single-name illiquidity
- Default basis (index has same recovery for all, single-name varies)
- Roll risk at index maturity
- Counterparty concentration (many single-name trades)

**Example Trade:**

**Setup:** CDX IG at 62 bp, single-name average at 55 bp, skew = +7 bp

**Position:**
- Sell $100M CDX IG protection @ 62 bp
- Buy protection on 10 representative single names @ 55 bp average ($10M each)

**Net carry:** +7 bp × $100M × duration = $31,500/year

**Exit:** When skew normalizes to 0 bp, capture 7 bp × duration = 31.5 bp return

---

## CDS Index Options


**Options on credit indices provide volatility and directional exposure:**

### Option Types


**1. Payer Swaption:**
- Right to BUY protection at strike spread
- Profits when spreads widen
- Long credit risk, long vol

**2. Receiver Swaption:**
- Right to SELL protection at strike spread
- Profits when spreads tighten
- Short credit risk, long vol

### Option Pricing


**Black-style formula for CDS swaptions:**

$$
\text{Payer} = RA \times [F \times N(d_1) - K \times N(d_2)]
$$

$$
\text{Receiver} = RA \times [K \times N(-d_2) - F \times N(-d_1)]
$$

Where:
- $RA$ = Risky annuity (PV of 1 bp running)
- $F$ = Forward spread
- $K$ = Strike spread
- $\sigma$ = Spread volatility

$$
d_1 = \frac{\ln(F/K) + 0.5\sigma^2 T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}
$$

### Typical Quotes


**CDX IG 5Y Options (Example):**

| Option | Strike | Expiry | Mid Vol | Premium |
|--------|--------|--------|---------|---------|
| Payer | 60 bp | 3M | 48% | 0.35% |
| Payer | 70 bp | 3M | 52% | 0.22% |
| Payer | 80 bp | 3M | 58% | 0.12% |
| Receiver | 50 bp | 3M | 50% | 0.28% |
| Receiver | 40 bp | 3M | 55% | 0.15% |

### Option Strategies


**1. Straddle:**
- Buy ATM payer + ATM receiver
- Profit from large moves either direction
- Cost: ~0.60% of notional for 3M

**2. Strangle:**
- Buy OTM payer + OTM receiver
- Cheaper than straddle, needs bigger move
- Cost: ~0.30% for 3M

**3. Risk Reversal:**
- Sell OTM receiver, buy OTM payer
- Net directional bet on widening
- Can be zero cost if balanced

**4. Calendar Spread:**
- Sell short-dated, buy long-dated
- Bet on vol term structure
- Positive theta if short-dated decays faster

---

## ISDA Standard Model Overview


**The industry standard for CDS pricing:**

### Model Framework


**ISDA CDS Standard Model (2009):**

**Key assumptions:**
1. Constant hazard rate between dates
2. Piecewise flat term structure of hazard rates
3. Standard recovery rate (40% for senior, 25% for subordinated)
4. Deterministic interest rates
5. No correlation between default and rates

### Pricing Formulas


**Protection leg PV:**

$$
PV_{\text{protection}} = (1-R) \sum_{i=1}^{n} Q(t_{i-1}) - Q(t_i)) \times D(t_i)
$$

Where:
- $R$ = Recovery rate
- $Q(t)$ = Survival probability to time $t$
- $D(t)$ = Risk-free discount factor

**Premium leg PV:**

$$
PV_{\text{premium}} = s \sum_{i=1}^{n} \Delta_i \times Q(t_i) \times D(t_i)
$$

Where:
- $s$ = CDS spread
- $\Delta_i$ = Accrual fraction

**Accrued premium (at default):**

$$
PV_{\text{accrued}} = s \sum_{i=1}^{n} \frac{\Delta_i}{2} \times (Q(t_{i-1}) - Q(t_i)) \times D(t_i)
$$

**Par spread:**

$$
s_{\text{par}} = \frac{PV_{\text{protection}}}{PV_{\text{premium unit}}}
$$

### Upfront and Running Spread


**Post-2009 convention:**

Standard running spread: 100 bp (IG) or 500 bp (HY)

**Upfront payment:**

$$
\text{Upfront} = (s_{\text{market}} - s_{\text{standard}}) \times RA
$$

Where $RA$ = Risky Annuity = $\sum_i \Delta_i Q(t_i) D(t_i)$

**Example:**
- Market spread: 150 bp
- Standard coupon: 100 bp
- 5Y risky annuity: 4.2
- Upfront = (0.0150 - 0.0100) × 4.2 = 2.1% of notional

**Protection buyer pays 2.1% upfront, then 100 bp running.**

### Model Limitations


**1. Constant hazard rate:**
- Real hazard rates are time-varying
- Short-term default risk differs from long-term

**2. Deterministic rates:**
- Rates and credit are correlated in practice
- Underestimates risk in stress

**3. Fixed recovery:**
- Recovery varies by issuer, sector, cycle
- 40% assumption is average, not guarantee

**4. No wrong-way risk:**
- Model ignores correlation between default and exposure

### Model Calibration


**Bootstrap hazard rates from CDS term structure:**

| Maturity | Market Spread | Hazard Rate | Survival Prob |
|----------|---------------|-------------|---------------|
| 1Y | 50 bp | 0.83% | 99.17% |
| 3Y | 75 bp | 1.25% | 96.31% |
| 5Y | 100 bp | 1.67% | 91.97% |
| 7Y | 115 bp | 1.64% | 87.22% |
| 10Y | 130 bp | 1.81% | 80.42% |

**Process:**
1. Use 1Y spread to find 1Y hazard rate
2. Given 1Y hazard, use 3Y spread to find 1Y-3Y hazard
3. Continue iteratively

---

## Summary: Enhanced CDS and Index Framework


### Comprehensive Trading Checklist


**For index trading:**
- [ ] Calculate theoretical vs. market spread (skew)
- [ ] Check skew percentile vs. history
- [ ] Monitor tranche spreads and correlations
- [ ] Track option implied volatility

**For single-name:**
- [ ] Bootstrap hazard rates from curve
- [ ] Calculate CS01, DV01
- [ ] Compare to peers in sector
- [ ] Check basis vs. cash bonds

**For tranches:**
- [ ] Understand correlation exposure
- [ ] Calculate delta and gamma to index
- [ ] Monitor base correlation
- [ ] Size for tail scenarios

### Key Formulas Summary


**Index skew:**
$$
\text{Skew} = S_{\text{index}} - \frac{1}{N}\sum_i S_i
$$

**Tranche loss:**
$$
L_{K_1,K_2} = \min(\max(L - K_1, 0), K_2 - K_1)
$$

**ISDA upfront:**
$$
\text{Upfront} = (s_{\text{market}} - s_{\text{standard}}) \times RA
$$

**Option premium (approx):**
$$
\text{Premium} \approx 0.4 \times \sigma \times \sqrt{T} \times RA
$$

These enhanced frameworks provide deeper understanding of CDS market dynamics beyond the basic mechanics covered in the main text.
