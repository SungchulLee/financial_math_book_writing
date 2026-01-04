# Default Risk and Recovery

**Default risk and recovery** are the fundamental building blocks of credit analysis, measuring the probability that a borrower will fail to make promised payments (default) and the percentage of principal that investors can expect to recover through bankruptcy proceedings, asset liquidation, or restructuring—with the product of default probability and loss-given-default (1 minus recovery rate) determining the expected loss that drives credit spreads and bond pricing.

---

## The Core Insight

**The fundamental idea:**

- Every bond has default risk (except risk-free Treasuries)
- Default probability varies by credit quality
- Recovery depends on seniority and collateral
- Expected loss = Probability of Default × Loss Given Default
- Credit spreads compensate for expected loss + risk premium
- Recovery rates vary dramatically (0-90%)
- Senior secured bonds recover most (60-80%)
- Subordinated bonds recover least (10-30%)

**The key equations:**

**Expected loss:**

$$
\text{Expected Loss} = \text{PD} \times \text{LGD}
$$

**Loss given default:**

$$
\text{LGD} = 1 - \text{Recovery Rate}
$$

**Credit spread (simplified):**

$$
\text{Spread} = \frac{\text{Expected Loss}}{1 - \text{Expected Loss}} + \text{Risk Premium}
$$

**You're essentially calculating: "What's the probability this bond defaults, how much will I lose if it does, and am I being paid enough spread to compensate for that risk?"**

---

## What Are Default Risk and Recovery?

**Before investing in credit, understand the fundamentals:**

### Core Concepts

**Default Risk:**

**Definition:** The probability that a borrower will fail to make interest or principal payments as contractually obligated, either through missing payments (technical default), filing for bankruptcy protection (Chapter 11 reorganization or Chapter 7 liquidation), or negotiating a debt restructuring that impairs creditor claims.

**Recovery Rate:**

**Definition:** The percentage of a bond's face value that investors ultimately receive through bankruptcy proceedings, asset sales, debt-for-equity swaps, or negotiated restructurings, typically expressed as cents on the dollar (e.g., 40% recovery = $0.40 per $1.00 face value).

**When analyzing default and recovery:**

- You estimate default probability (1-year, cumulative)
- You assess likely recovery given seniority/collateral
- You calculate expected loss (PD × LGD)
- You compare spread to expected loss
- You determine risk premium adequacy
- You size position based on loss potential
- You diversify to avoid concentration risk
- Primary focus: Avoiding permanent loss of capital

**Example - BB-Rated Corporate Bond Analysis:**

**Bond details:**

| Item | Value |
|------|-------|
| Issuer | Regional Bank Corp |
| Rating | BB (non-investment grade) |
| Maturity | 5 years |
| Coupon | 7.50% |
| Current price | 98.00 |
| Yield | 7.91% |
| Treasury yield | 4.50% |
| **Credit spread** | **341 bps** |

**Step 1: Estimate default probability**

**Historical data (Moody's 1920-2023):**

- BB 1-year default rate: 1.0%
- BB 5-year cumulative default rate: 7.5%

**Current credit cycle adjustment:**

- Late cycle, rising defaults: Multiply by 1.3
- **Adjusted 5-year PD: 9.75%**

**Step 2: Estimate recovery rate**

**Bond structure:**

- Seniority: Senior unsecured
- Collateral: None
- Historical recovery (senior unsecured): 40%

**Issuer-specific factors:**

- Asset quality: Moderate (loan portfolio diversified)
- Tangible assets: 60% of liabilities
- **Expected recovery: 35-45%, use 40%**

**Step 3: Calculate expected loss**

$$
\text{LGD} = 1 - 0.40 = 0.60
$$

$$
\text{Expected Loss} = 9.75\% \times 0.60 = 5.85\%
$$

**Step 4: Annualize expected loss**

$$
\text{Annual Expected Loss} = \frac{5.85\%}{5 \text{ years}} = 1.17\% \text{ per year}
$$

**Step 5: Compare to spread**

- Credit spread: 341 bps (3.41% per year)
- Expected loss: 117 bps (1.17% per year)
- **Risk premium: 224 bps (2.24% per year)**

**Interpretation:**

- Spread = 341 bps
- Expected loss = 117 bps (compensation for defaults)
- Risk premium = 224 bps (compensation for uncertainty/illiquidity)
- **Ratio: 224 / 117 = 1.9x (healthy risk premium)**

**Decision: BUY (adequate compensation for risk)**

### Default Probability Estimation Methods

**1. Historical Default Rates (Actuarial):**

Use historical data by rating category:

| Rating | 1-Year PD | 5-Year PD | 10-Year PD |
|--------|-----------|-----------|------------|
| AAA | 0.00% | 0.05% | 0.15% |
| AA | 0.02% | 0.15% | 0.50% |
| A | 0.05% | 0.35% | 1.20% |
| BBB | 0.18% | 1.50% | 4.50% |
| BB | 1.00% | 7.50% | 15.00% |
| B | 4.50% | 20.00% | 35.00% |
| CCC | 25.00% | 55.00% | 65.00% |

**Pros:** Long data history, stable
**Cons:** Backward-looking, doesn't capture current conditions

**2. Market-Implied (From Spreads):**

Extract PD from credit spreads:

$$
\text{Spread} \approx \text{PD} \times \text{LGD}
$$

Rearranging:

$$
\text{PD} = \frac{\text{Spread}}{\text{LGD}}
$$

**Example:**

- Spread: 300 bps
- Assumed LGD: 60%

$$
\text{PD} = \frac{3.00\%}{0.60} = 5.00\%
$$

**Pros:** Forward-looking, market-based
**Cons:** Includes risk premium (overstates true PD)

**3. Structural Models (Merton):**

Model default as option exercise:

- Firm has assets (A) and debt (D)
- Default when A < D
- Estimate volatility of assets
- Calculate "distance to default"

$$
\text{Distance to Default} = \frac{\ln(A/D) + (\mu - 0.5\sigma^2)T}{\sigma\sqrt{T}}
$$

**Pros:** Theoretically grounded
**Cons:** Requires market data, complex

**4. Reduced-Form Models (CDS-based):**

Use Credit Default Swap (CDS) spreads:

$$
\text{CDS Spread} \approx \text{PD} \times (1 - \text{Recovery})
$$

**Example:**

- 5-year CDS: 250 bps
- Recovery: 40%

$$
\text{Annual PD} = \frac{2.50\%}{(1-0.40) \times 5} = 0.83\%
$$

**Pros:** Market-based, liquid
**Cons:** CDS market not available for all issuers

### Recovery Rate Determinants

**Key factors affecting recovery:**

**1. Seniority and Security:**

| Position | Security | Typical Recovery |
|----------|----------|------------------|
| Senior Secured | Collateral (hard assets) | 60-80% |
| Senior Unsecured | General claim | 40-55% |
| Senior Subordinated | Junior claim | 25-40% |
| Subordinated | Lower claim | 15-30% |
| Junior Subordinated | Near-equity | 5-15% |
| Preferred Stock | Equity-like | 0-10% |

**2. Asset Quality:**

**High tangible asset value:**
- Manufacturing: Equipment, real estate
- Typical recovery: 50-70%

**Low tangible asset value:**
- Tech companies: Intangibles, IP
- Typical recovery: 20-40%

**3. Industry:**

| Industry | Avg Recovery (Senior Unsecured) |
|----------|--------------------------------|
| Utilities | 65-75% (regulated assets) |
| Telecommunications | 50-65% (infrastructure) |
| Retail | 35-50% (inventory, real estate) |
| Financial Services | 40-60% (loan portfolios) |
| Technology | 25-40% (intangibles) |
| Airlines | 15-30% (leased assets) |

**4. Bankruptcy Type:**

**Chapter 11 (Reorganization):**
- Company continues operating
- Creditors often get debt-for-equity
- Recovery: 40-60% (typical)

**Chapter 7 (Liquidation):**
- Company ceases operations
- Assets sold piecemeal
- Recovery: 10-30% (much lower)

**5. Economic Conditions:**

**Recession:**
- Asset sales in distressed market
- Lower recoveries (average -15 to -20%)

**Expansion:**
- Buyers willing to pay more
- Higher recoveries (average +10 to +15%)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/default_risk_recovery.png?raw=true" alt="default_risk_recovery" width="700">
</p>
**Figure 1:** Default risk and recovery showing the relationship between credit ratings and default probabilities (exponential increase from AAA to CCC), recovery rates by seniority (senior secured 60-80% down to subordinated 15-30%), and the calculation of expected loss driving credit spreads.

---

## Economic Interpretation: Why Defaults and Recoveries Matter

**Beyond the basic mechanics, understanding the REAL economics:**

### The Default Cycle

**The deep insight:**

Defaults are NOT random—they cluster in recessions:

$$
\text{Default Rate}_t = f(\text{Economic Growth}_t, \text{Credit Conditions}_{t-1}, \text{Default Rate}_{t-1})
$$

**Historical pattern (1980-2023):**

| Period | Economic Condition | Default Rate (Spec Grade) |
|--------|-------------------|---------------------------|
| 1982-1983 | Recession | 8.5% |
| 1984-1989 | Expansion | 2.5% average |
| 1990-1991 | Recession | 10.1% |
| 1992-2000 | Expansion | 3.1% average |
| 2001-2002 | Recession (Tech bust) | 9.8% |
| 2003-2007 | Expansion | 1.8% average (record low!) |
| 2008-2009 | Financial Crisis | 13.4% (peak Nov 2009) |
| 2010-2019 | Recovery | 2.9% average |
| 2020 | COVID Recession | 6.2% |
| 2021-2023 | Recovery | 1.5% average |

**Key observation: Defaults spike 4-8x during recessions**

**Why this matters for investors:**

**Late cycle (2023-2024):**

- Current default rate: 1.5% (low)
- Historical average: 4.0%
- **Expect mean reversion: Defaults will rise**

**Implication:**

- Today's 1.0% BB default rate understates risk
- Recession could push to 5-8%
- **Use 4-5% PD for conservative analysis, not 1%**

### Recovery Rate Compression During Crises

**The cruel reality:**

Recoveries fall WHEN defaults rise (worst possible correlation):

**Example - 2008-2009 Financial Crisis:**

**Pre-crisis (2007):**
- Default rate: 1.0%
- Recovery rate (senior unsecured): 45%
- Expected loss: 1.0% × 55% = 0.55%

**Crisis peak (2009):**
- Default rate: 13.4% (13.4x higher!)
- Recovery rate: 28% (fell to 28% from 45%)
- Expected loss: 13.4% × 72% = 9.65% (17.5x higher!)

**Why recoveries fall:**

1. **Excess supply:** Many companies defaulting simultaneously
2. **Fire sale prices:** Buyers demand steep discounts
3. **Credit crunch:** Distressed debt buyers can't finance purchases
4. **Industry distress:** Sector-wide problems (all banks, all retailers)

**Historical recovery rates by cycle:**

| Period | Avg Default Rate | Avg Recovery (Senior Unsec) |
|--------|------------------|----------------------------|
| Expansion (avg) | 2.5% | 48% |
| Mild recession | 6% | 38% |
| Severe recession (2008-09) | 13.4% | 28% |

**Correlation: -0.65 (strong negative)**

**Implication for pricing:**

Simple model:
- Use average PD (4%) and average recovery (45%)
- Expected loss: 4% × 55% = 2.2%

**Reality-adjusted model:**

Scenario-weighted:
- 70% probability: Expansion (PD 2%, Recovery 50%, EL 1.0%)
- 30% probability: Recession (PD 10%, Recovery 30%, EL 7.0%)

**Expected loss: 0.70 × 1.0% + 0.30 × 7.0% = 2.8%**

**27% higher than simple model!**

### The Leverage Ratchet

**How leverage drives default:**

**Company fundamentals:**

$$
\text{Interest Coverage} = \frac{EBITDA}{\text{Interest Expense}}
$$

**Safe zone: Coverage > 5x**
**Warning zone: Coverage 2-5x**
**Danger zone: Coverage < 2x (high default risk)**

**Example - Leveraged Company:**

**Initial (2019):**
- EBITDA: $100M
- Debt: $400M
- Interest rate: 6%
- Interest expense: $24M
- **Coverage: 100/24 = 4.2x (safe)**

**Shock - COVID (2020):**
- EBITDA falls to $60M (-40%, recession)
- Debt: Still $400M (can't repay easily)
- Interest: Still $24M
- **Coverage: 60/24 = 2.5x (warning)**

**Further deterioration (2021):**
- EBITDA falls to $40M (-60% from peak)
- Debt: $400M
- Interest: $24M
- **Coverage: 40/24 = 1.7x (DANGER)**

**Outcome: DEFAULT (2021)**

- Coverage below 2x for 12 months
- Covenant violations
- Lenders refuse to extend credit
- **Files Chapter 11**

**The ratchet effect:**

- Good times: Companies lever up (issue debt, do M&A)
- Bad times: Can't delever quickly (assets fall in value)
- **Leverage rises automatically as EBITDA falls**

**Debt/EBITDA evolution:**

- 2019: $400M / $100M = 4.0x
- 2020: $400M / $60M = 6.7x
- 2021: $400M / $40M = 10.0x
- **Default threshold: Typically 8-10x**

---

## Key Terminology

**Default:**

- Failure to pay interest or principal
- Can be technical (covenant breach) or payment default
- Triggers: Missed payment, bankruptcy filing
- Measured: Default rate (% of issuers defaulting)

**Recovery Rate:**

- Percentage of face value recovered
- Measured: Post-default (30-90 days after default)
- Typical: 40% (senior unsecured average)
- Expressed: Cents per dollar ($0.40 = 40%)

**Loss Given Default (LGD):**

- Percentage lost in default
- Formula: LGD = 1 - Recovery Rate
- Example: 40% recovery → 60% LGD
- Used: Expected loss calculations

**Probability of Default (PD):**

- Likelihood of default over period
- 1-year PD: Next 12 months
- Cumulative PD: Over life of bond
- Annualized: Cumulative / Years

**Expected Loss:**

- Probability-weighted loss
- Formula: PD × LGD
- Example: 5% PD × 60% LGD = 3% expected loss
- Key metric: Drives credit spreads

**Credit Spread:**

- Yield above risk-free rate
- Compensates: Expected loss + risk premium
- Example: 7% yield - 4% Treasury = 300 bps spread
- Varies: By rating, cycle, liquidity

**Distance to Default:**

- Standard deviations to insolvency
- Structural model output
- Higher = safer
- Typical: >3.0 safe, <1.0 danger

**Interest Coverage:**

- EBITDA / Interest Expense
- Measures: Ability to service debt
- Safe: >5x
- Danger: <2x

**Seniority:**

- Priority in bankruptcy
- Order: Secured → Senior Unsec → Subordinated → Equity
- Determines: Recovery rate
- Critical: 30-50% recovery difference

**Distressed Ratio:**

- Percentage of high-yield trading >1000 bps spread
- Gauge: Market stress
- Normal: <10%
- Crisis: >30%

---

## Mathematical Foundation

### Expected Loss Calculation

**Basic formula:**

$$
EL = PD \times LGD
$$

**Example:**

- 5-year cumulative PD: 8%
- Recovery rate: 40%
- LGD: 1 - 0.40 = 0.60

$$
EL = 0.08 \times 0.60 = 0.048 = 4.8\%
$$

**Annualized:**

$$
EL_{\text{annual}} = \frac{4.8\%}{5} = 0.96\% \text{ per year}
$$

### Credit Spread Decomposition

**Theoretical spread:**

$$
s = \frac{PD \times LGD}{1 - PD \times LGD} + \text{Risk Premium} + \text{Liquidity Premium}
$$

**Simplified (for low PD):**

$$
s \approx PD \times LGD + \text{Risk Premium}
$$

**Example:**

- PD: 5% (5-year cumulative)
- LGD: 60%
- Expected loss: 3% (over 5 years) = 0.60% per year
- Risk premium: 150 bps
- Liquidity premium: 50 bps

$$
s = 60 + 150 + 50 = 260 \text{ bps}
$$

**Observed spread: 280 bps (close!)**

### Distance to Default (Merton Model)

**Asset value dynamics:**

$$
dA = \mu A dt + \sigma A dW
$$

**Default occurs when $A < D$ (assets below debt)**

**Distance to default:**

$$
DD = \frac{\ln(A/D) + (\mu - 0.5\sigma^2)T}{\sigma\sqrt{T}}
$$

Where:
- $A$ = Market value of assets
- $D$ = Book value of debt
- $\mu$ = Expected asset return
- $\sigma$ = Asset volatility
- $T$ = Time horizon

**Probability of default:**

$$
PD = N(-DD)
$$

Where $N(\cdot)$ is the cumulative normal distribution.

**Example:**

- Assets: $500M (estimated from equity + debt)
- Debt: $300M
- Asset growth: 5% per year
- Asset volatility: 25%
- Time: 1 year

$$
DD = \frac{\ln(500/300) + (0.05 - 0.5 \times 0.25^2) \times 1}{0.25 \times \sqrt{1}}
$$

$$
= \frac{\ln(1.667) + 0.0188}{0.25} = \frac{0.5108 + 0.0188}{0.25} = \frac{0.5296}{0.25} = 2.12
$$

$$
PD = N(-2.12) = 0.017 = 1.7\%
$$

**Interpretation: 1.7% one-year default probability**

### Altman Z-Score (Accounting-Based)

**Formula:**

$$
Z = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E
$$

Where:
- $A$ = Working Capital / Total Assets
- $B$ = Retained Earnings / Total Assets
- $C$ = EBIT / Total Assets
- $D$ = Market Value Equity / Book Value Liabilities
- $E$ = Sales / Total Assets

**Interpretation:**

- $Z > 2.99$: Safe zone (low default risk)
- $1.81 < Z < 2.99$: Grey zone
- $Z < 1.81$: Distress zone (high default risk)

**Example Company:**

- Working Capital: $50M, Total Assets: $500M → A = 0.10
- Retained Earnings: $100M → B = 0.20
- EBIT: $75M → C = 0.15
- MV Equity: $200M, BV Liabilities: $300M → D = 0.67
- Sales: $400M → E = 0.80

$$
Z = 1.2(0.10) + 1.4(0.20) + 3.3(0.15) + 0.6(0.67) + 1.0(0.80)
$$

$$
= 0.12 + 0.28 + 0.495 + 0.402 + 0.80 = 2.097
$$

**Result: Z = 2.10 (Grey zone, moderate risk)**

---

## Step-by-Step Analysis

### Phase 1: Gather Data

**1. Company Financials:**

```python
import pandas as pd
import numpy as np

# Example: Retail company analysis
company_data = {
    'revenue': 1_500_000_000,
    'ebitda': 180_000_000,
    'ebit': 120_000_000,
    'interest_expense': 45_000_000,
    'total_assets': 800_000_000,
    'total_debt': 500_000_000,
    'market_cap': 350_000_000,
    'working_capital': 80_000_000,
    'retained_earnings': 150_000_000,
}

# Calculate key ratios
interest_coverage = company_data['ebitda'] / company_data['interest_expense']
leverage = company_data['total_debt'] / company_data['ebitda']
debt_to_assets = company_data['total_debt'] / company_data['total_assets']

print(f"Interest Coverage: {interest_coverage:.2f}x")
print(f"Debt/EBITDA: {leverage:.2f}x")
print(f"Debt/Assets: {debt_to_assets:.1%}")
```

**Output:**

```
Interest Coverage: 4.00x
Debt/EBITDA: 2.78x
Debt/Assets: 62.5%
```

**2. Credit Rating:**

```python
# Estimate rating based on metrics
def estimate_rating(coverage, leverage):
    """Estimate credit rating from metrics"""
    
    if coverage >= 10 and leverage <= 1.5:
        return 'A', 0.05  # 1-year PD
    elif coverage >= 5 and leverage <= 3.0:
        return 'BBB', 0.18
    elif coverage >= 3 and leverage <= 4.5:
        return 'BB', 1.00
    elif coverage >= 2 and leverage <= 6.0:
        return 'B', 4.50
    else:
        return 'CCC', 25.00
    
rating, pd_1yr = estimate_rating(interest_coverage, leverage)
print(f"Estimated Rating: {rating}")
print(f"1-Year PD: {pd_1yr}%")

# Output:
# Estimated Rating: BB
# 1-Year PD: 1.00%
```

### Phase 2: Calculate Default Probability

**1. Historical Method:**

```python
# Cumulative default rates by rating (Moody's historical)
cumulative_pd = {
    'AAA': {'1Y': 0.00, '5Y': 0.05, '10Y': 0.15},
    'AA': {'1Y': 0.02, '5Y': 0.15, '10Y': 0.50},
    'A': {'1Y': 0.05, '5Y': 0.35, '10Y': 1.20},
    'BBB': {'1Y': 0.18, '5Y': 1.50, '10Y': 4.50},
    'BB': {'1Y': 1.00, '5Y': 7.50, '10Y': 15.00},
    'B': {'1Y': 4.50, '5Y': 20.00, '10Y': 35.00},
    'CCC': {'1Y': 25.00, '5Y': 55.00, '10Y': 65.00},
}

rating = 'BB'
horizon = '5Y'

historical_pd = cumulative_pd[rating][horizon]
print(f"{rating} {horizon} cumulative PD: {historical_pd}%")

# Cycle adjustment (late cycle, expect higher defaults)
cycle_adjustment = 1.2
adjusted_pd = historical_pd * cycle_adjustment

print(f"Cycle-adjusted PD: {adjusted_pd}%")
```

**Output:**

```
BB 5Y cumulative PD: 7.50%
Cycle-adjusted PD: 9.00%
```

**2. Market-Implied Method:**

```python
# Extract PD from CDS spread
cds_spread_bps = 250  # 5-year CDS
recovery_rate = 0.40

# Annual PD approximation
annual_pd = (cds_spread_bps / 10000) / ((1 - recovery_rate))
print(f"Implied annual PD: {annual_pd:.2%}")

# 5-year cumulative
cumulative_pd_implied = annual_pd * 5
print(f"5-year cumulative PD (market): {cumulative_pd_implied:.1%}")
```

**Output:**

```
Implied annual PD: 4.17%
5-year cumulative PD (market): 20.8%
```

**Note: Market-implied is much higher (includes risk premium)**

### Phase 3: Estimate Recovery Rate

**1. Seniority-Based:**

```python
# Recovery rates by seniority (historical averages)
recovery_by_seniority = {
    'Senior Secured': 0.65,
    'Senior Unsecured': 0.42,
    'Senior Subordinated': 0.32,
    'Subordinated': 0.23,
    'Junior Subordinated': 0.12,
}

bond_seniority = 'Senior Unsecured'
base_recovery = recovery_by_seniority[bond_seniority]

print(f"Base recovery ({bond_seniority}): {base_recovery:.0%}")
```

**2. Industry Adjustment:**

```python
# Industry-specific recovery adjustments
industry_adjustments = {
    'Utilities': 1.15,
    'Telecom': 1.05,
    'Industrial': 1.00,
    'Retail': 0.90,
    'Tech': 0.80,
    'Airlines': 0.70,
}

industry = 'Retail'
adjustment = industry_adjustments[industry]

adjusted_recovery = base_recovery * adjustment
print(f"Industry-adjusted recovery: {adjusted_recovery:.0%}")
```

**Output:**

```
Base recovery (Senior Unsecured): 42%
Industry-adjusted recovery: 38%
```

### Phase 4: Calculate Expected Loss

**1. Expected Loss:**

```python
# Using cycle-adjusted PD and industry-adjusted recovery
pd_5yr = 0.09  # 9% (from Phase 2)
recovery = 0.38  # 38% (from Phase 3)

lgd = 1 - recovery
expected_loss_5yr = pd_5yr * lgd

print(f"5-Year Expected Loss: {expected_loss_5yr:.2%}")

# Annualized
annual_el = expected_loss_5yr / 5
print(f"Annual Expected Loss: {annual_el:.2%}")
```

**Output:**

```
5-Year Expected Loss: 5.58%
Annual Expected Loss: 1.12%
```

**2. Compare to Spread:**

```python
# Bond spread
bond_yield = 0.0750
treasury_yield = 0.0450
spread_bps = (bond_yield - treasury_yield) * 10000

print(f"Credit Spread: {spread_bps:.0f} bps")
print(f"Expected Loss: {annual_el*10000:.0f} bps")

risk_premium_bps = spread_bps - (annual_el * 10000)
print(f"Risk Premium: {risk_premium_bps:.0f} bps")

# Risk/reward ratio
ratio = risk_premium_bps / (annual_el * 10000)
print(f"Risk Premium / Expected Loss: {ratio:.2f}x")
```

**Output:**

```
Credit Spread: 300 bps
Expected Loss: 112 bps
Risk Premium: 188 bps
Risk Premium / Expected Loss: 1.68x
```

**Decision:**

- Risk premium 188 bps (1.68x expected loss)
- Adequate but not exceptional
- **HOLD or small position** (marginal opportunity)

### Phase 5: Scenario Analysis

**1. Stress Testing:**

```python
# Define scenarios
scenarios = pd.DataFrame({
    'scenario': ['Base', 'Mild Recession', 'Severe Recession'],
    'pd_multiplier': [1.0, 1.5, 2.5],
    'recovery_shock': [0, -0.05, -0.15],
    'probability': [0.60, 0.30, 0.10]
})

base_pd = 0.09
base_recovery = 0.38

# Calculate expected loss per scenario
scenarios['pd'] = base_pd * scenarios['pd_multiplier']
scenarios['recovery'] = base_recovery + scenarios['recovery_shock']
scenarios['lgd'] = 1 - scenarios['recovery']
scenarios['el_5yr'] = scenarios['pd'] * scenarios['lgd']
scenarios['el_annual'] = scenarios['el_5yr'] / 5

print(scenarios)
```

**Output:**

```
         scenario  pd_multiplier  recovery_shock  probability    pd  recovery   lgd  el_5yr  el_annual
0            Base            1.0            0.00         0.60  0.09      0.38  0.62  0.0558     0.0112
1  Mild Recession            1.5           -0.05         0.30  0.14      0.33  0.67  0.0938     0.0188
2 Severe Recession           2.5           -0.15         0.10  0.23      0.23  0.77  0.1771     0.0354
```

**2. Expected Value:**

```python
# Weighted average expected loss
weighted_el = (scenarios['el_annual'] * scenarios['probability']).sum()

print(f"Weighted Expected Loss: {weighted_el:.2%} annually")
print(f"Original Expected Loss: {annual_el:.2%} annually")
print(f"Stress adjustment: +{(weighted_el - annual_el)*10000:.0f} bps")
```

**Output:**

```
Weighted Expected Loss: 1.56% annually
Original Expected Loss: 1.12% annually
Stress adjustment: +44 bps
```

**Revised decision:**

- Stress-adjusted EL: 156 bps
- Spread: 300 bps
- Risk premium: 144 bps (300 - 156)
- **Ratio: 0.92x (INADEQUATE)**
- **Decision: PASS** (insufficient compensation for tail risk)

---

## Real-World Examples

### Example 1: Investment Grade Default - General Electric 2018 (Near-Miss)

**Background:**

- GE: Former AAA icon, one of last AAA industrials
- 2000-2015: Maintained AA rating
- 2016-2017: Series of downgrades to A
- 2018: Further downgrades to BBB (barely IG)

**Situation (October 2018):**

| Metric | Value |
|--------|-------|
| Market cap | $75B (down from $600B in 2000!) |
| Total debt | $115B |
| EBITDA | $18B (falling) |
| Interest coverage | 2.8x (dangerous) |
| Rating | BBB (on edge of junk) |
| Bond spread | 350 bps (10Y) |

**Analysis:**

**Default probability:**

- Historical BBB 5-year PD: 1.5%
- But: Coverage 2.8x suggests B rating (PD 20%)
- Market CDS: 180 bps (implies 6% annual PD)
- **Consensus: 15-20% 5-year default risk**

**Recovery estimate:**

- Senior unsecured position
- But: Massive debt pile ($115B)
- Asset quality: Industrial equipment, GE Capital legacy
- **Expected recovery: 35-40%** (below average)

**Expected loss:**

- PD: 17.5% (5-year)
- Recovery: 37.5%
- LGD: 62.5%

$$
EL = 17.5\% \times 62.5\% = 10.94\% \text{ (5-year)}
$$

$$
EL_{\text{annual}} = 2.19\%
$$

**Spread analysis:**

- Spread: 350 bps
- Expected loss: 219 bps
- **Risk premium: 131 bps (0.60x, INADEQUATE)**

**Investor decision (late 2018):** AVOID

**What happened:**

**2019: Near-default averted**

- New CEO (Larry Culp)
- Massive asset sales ($40B GE Capital disposals)
- Dividend cut to $0.01 (from $0.12, 92% cut!)
- Avoided bankruptcy by inches

**2020-2024: Recovery**

- Broke up company (Healthcare, Power, Aviation split)
- Debt reduced to $75B
- Rating: Upgraded to BBB+ (2023)
- Spreads: Tightened to 150 bps

**Bondholders who held:**

- No default (lucky!)
- Suffered mark-to-market pain (spreads 350→500 bps at worst)
- Eventually recovered

**Key lesson:**

- Fallen angels (IG→HY) are dangerous
- Low coverage ratio (2.8x) was warning sign
- Spread was insufficient (0.60x risk premium too low)
- **Avoid deteriorating IG names, even if historically strong**

### Example 2: High-Yield Default - J.C. Penney 2020 (Total Loss)

**Background:**

- Iconic American retailer (founded 1902)
- Peak: $18B revenue (2016)
- Facing: Amazon competition, mall traffic decline
- 2017-2019: Deteriorating financials

**Bond Analysis (January 2020):**

**Unsecured bond due 2036:**

| Item | Value |
|------|-------|
| Coupon | 8.625% |
| Price | 32 (cents on dollar) |
| Yield | 28% (!!) |
| Spread | 2,400 bps vs Treasury |
| Rating | CCC |

**Financial metrics:**

- Revenue: $10.7B (declining 5% annually)
- EBITDA: $800M
- Debt: $3.7B
- Interest: $350M
- Coverage: 2.3x (barely sufficient)

**Default probability:**

- CCC 1-year PD: 25% (historical)
- Market CDS: Not trading (too distressed)
- Interest coverage: Suggests 30-40% near-term PD
- **Estimate: 35% 1-year default risk**

**Recovery estimate:**

- Seniority: Senior unsecured
- But: Behind $1.5B secured debt (first lien)
- Asset value: Real estate ($2B), inventory ($3B), IP ($500M)
- Liquidation value: 40-50% of book
- After secured creditors: Little left
- **Expected recovery: 10-20%**

**Expected loss (1-year):**

- PD: 35%
- Recovery: 15%
- LGD: 85%

$$
EL = 35\% \times 85\% = 29.75\%
$$

**Spread analysis:**

- Yield: 28%
- Treasury: 2%
- Spread: 2,600 bps (26%)
- Expected loss: 2,975 bps (29.75%)
- **NEGATIVE risk premium!**

**Interpretation: Market pricing >100% expected loss**

**Possibility: Distressed debt buyers expect recovery trade if survives**

**What happened: COVID-19 Accelerated Collapse**

**March 2020:**

- Stores closed (pandemic lockdowns)
- Revenue collapsed to near-zero
- Couldn't make rent payments

**May 15, 2020: Chapter 11 Bankruptcy**

**Recovery process:**

**Asset sales:**

- Real estate: $500M (in distressed market, 25% of appraised value)
- Inventory: $1.2B (liquidation sales)
- IP/Brand: $100M (to Simon Property Group + Brookfield)
- Total: $1.8B

**Creditor waterfall:**

1. DIP financing: $450M (paid in full)
2. Secured lenders: $1.5B claim → Received $1.2B (**80% recovery**)
3. Unsecured bondholders: $2.2B claim → Received $150M (**6.8% recovery**)
4. Equity: $0

**Final recovery: 6.8% (vs. expected 15%)**

**Bondholder outcome:**

- Bought at 32 cents
- Recovered 6.8 cents
- **Loss: 25.2 cents = -79% loss**
- On $1M investment: Lost $790,000

**Why even worse than expected:**

1. **COVID timing:** Filed during worst possible market (March-May 2020)
2. **Fire sale:** Assets sold in distressed environment
3. **Secured priority:** $1.5B ahead of unsecured took most value
4. **No operating value:** Company couldn't be reorganized (liquidated instead)

**Lesson:**

- CCC bonds are extremely risky (25% default rate)
- Unsecured behind secured = tiny recovery (6.8%)
- Market pricing was accurate (28% yield implied huge loss)
- **Avoid unsecured distressed retail** (low tangible asset value)

### Example 3: Spectacular Recovery - Hertz 2020-2021 (Equity Windfall)

**Background:**

- Car rental company
- Massive debt: $19B
- 2019: Struggling but operating
- March 2020: COVID travel collapse

**May 22, 2020: Chapter 11 Bankruptcy**

**At filing:**

| Security | Amount | Initial Recovery Estimate |
|----------|--------|--------------------------|
| Secured debt | $14B | 80-90% |
| Unsecured debt | $5B | 5-15% |
| Equity | $500M (market cap) | 0% |

**Unsecured bond analysis (post-bankruptcy):**

**8.0% Notes due 2024:**

- Face value: $1B outstanding
- Trading: 12 cents on dollar (July 2020)
- Implied recovery: 12%
- Market view: Liquidation scenario

**Expected outcome (consensus):**

- Company liquidates
- Fleet sold for $10B (vs. $18B book value)
- Secured creditors: 70% recovery
- Unsecured creditors: 8-12% recovery
- **Equity: Wiped out**

**What happened: Unprecedented Recovery**

**June 2020: Used car prices SURGE**

- Rental car shortage (fleets sold during pandemic)
- Used car prices +30% (chip shortage, stimulus checks)
- Hertz fleet value RISES in bankruptcy

**January 2021: Restructuring Plan**

**New asset values:**

- Fleet: $14B (up from $10B estimate!)
- Brand value: $1.5B (Hertz, Dollar, Thrifty brands)
- Total assets: $16B (enough for everyone!)

**Final recovery:**

| Security | Recovery |
|----------|----------|
| Secured debt ($14B) | 100% (paid in full!) |
| Unsecured debt ($5B) | 100% (paid in full!) |
| **Old equity** | **$8 per share** (was $0.50 before bankruptcy!) |

**Bondholder outcome:**

- Bought unsecured at 12 cents (July 2020)
- Recovered 100 cents (June 2021)
- **Gain: 88 cents = +733% return in 11 months!**
- On $1M investment: Made $7.33M

**Why this happened:**

1. **Asset inflation:** Used cars became scarce, valuable
2. **Timing luck:** Emerged from bankruptcy at peak car prices
3. **Strong brand:** Hertz brand retained value
4. **Restructuring efficiency:** 13-month bankruptcy (fast)
5. **New capital:** Equity investors willing to invest $2B

**Historical anomaly:**

- Only 2nd time in US history equity recovered in bankruptcy (Seaboard 1991)
- Normal: Equity always wiped out
- Hertz: Equity actually made 1,600% gain!

**Lesson:**

- Distressed debt CAN have huge upside (but extremely rare)
- Asset values are uncertain (cars appreciated 30%)
- Market was wrong about liquidation (company reorganized)
- **High risk but occasionally spectacular reward**

### Example 4: Subordinated Debt Wipeout - Lehman Brothers 2008

**Background:**

- Investment bank, 158 years old
- September 15, 2008: Largest bankruptcy in US history
- $639B assets, $619B liabilities

**Capital structure (pre-bankruptcy):**

| Security | Amount | Seniority |
|----------|--------|-----------|
| Repo liabilities | $200B | Super-senior |
| Senior unsecured | $150B | Senior |
| Subordinated debt | $40B | Junior |
| Tier 1 capital | $20B | Equity-like |
| Equity | $4B | Last |

**Subordinated bond example:**

**5.75% Sub Notes due 2018:**

- Face value: $2B outstanding
- Pre-bankruptcy price (Sept 12): 70 cents
- Day of bankruptcy (Sept 15): 8 cents (collapse!)
- Expected recovery: 10-20%

**What happened: 14-year workout**

**Asset liquidation (2008-2022):**

- Initial assets: $639B
- Bankruptcy costs: $130B (!!)
- Legal fees: $2.2B
- Advisor fees: $1.5B
- Other admin: $126B

**Recovery waterfall:**

- Repo counterparties: $200B → 100% recovery (priority)
- Senior unsecured: $150B → $129B paid = **86% recovery** (2022)
- Subordinated: $40B → $7.2B paid = **18% recovery** (2022)
- Equity: $0 recovery

**Subordinated bondholder outcome:**

- Bought at 70 cents (Sept 12, before bankruptcy)
- Recovered 18 cents (over 14 years!)
- **Loss: 52 cents = -74% loss**
- On $10M investment: Lost $7.4M
- Time value: 14 years to recover 18% (terrible return)

**Why so low:**

1. **Massive bankruptcy costs:** $130B (20% of assets!)
2. **Derivatives complexity:** 900,000 derivative contracts to unwind
3. **Priority structure:** Repo and senior creditors ahead
4. **Asset value decline:** Real estate, securities fell 30-50%
5. **Subordinated = junior:** Only 18% after senior paid

**NPV of recovery:**

- 18 cents received after 14 years
- Discount rate: 10%
- NPV: 18 / (1.10)^14 = 4.7 cents

**True economic recovery: 4.7% in present value terms**

**Lesson:**

- Subordinated debt in bank failures recovers very little (10-25%)
- Bankruptcy costs are enormous (can be 20% of assets)
- Priority matters: Senior unsecured got 86%, subordinated got 18%
- **Never buy subordinated debt of financial institutions** (wipeout risk)

### Example 5: Secured Creditor Victory - Neiman Marcus 2020 (High Recovery)

**Background:**

- Luxury retailer
- Debt: $5B ($3B secured, $2B unsecured)
- 2020: Filed Chapter 11 (COVID + debt burden)

**Capital structure:**

| Security | Amount | Collateral |
|----------|--------|-----------|
| 1st Lien Term Loan | $3.0B | All assets (inventory, real estate, IP) |
| Unsecured notes | $2.0B | None |
| Equity | $800M (pre-bankruptcy) | Last |

**Secured creditor position:**

**1st Lien Term Loan:**

- Face value: $3B
- Collateral: $5B appraisal (inventory $2B, real estate $2.5B, brand $500M)
- Coverage: 5B / 3B = 1.67x (overcollateralized)
- Expected recovery: 95-105% (actually MAKE money!)

**Unsecured bondholder position:**

**7.125% Notes due 2028:**

- Face value: $2B
- Trading: 15 cents (May 2020, post-filing)
- Expected recovery: 10-20%

**What happened: Secured Lenders Win Big**

**October 2020: Reorganization Plan**

**Asset sales:**

- Inventory: Sold to new buyers for $1.5B (liquidated)
- Real estate: 22 stores + HQ sold for $1.8B
- Brand/IP: Licensed to new company for $750M
- Total: $4.05B

**Distribution:**

1. Bankruptcy costs: $150M (paid first)
2. **Secured lenders ($3B claim):**
   - Cash: $2.5B
   - New equity: $400M
   - **Total: $2.9B = 97% recovery**
3. **Unsecured bondholders ($2B claim):**
   - Cash: $100M
   - Equity warrants: $50M (estimated value)
   - **Total: $150M = 7.5% recovery**
4. Old equity: $0

**Secured lender outcome:**

- Loaned $3B
- Recovered $2.9B
- **Loss: 3% only** (vs. unsecured 92.5% loss!)
- Interest payments during bankruptcy: Received $45M
- **Effective recovery: 98.5%** (almost whole)

**Why secured did so well:**

1. **Overcollateralized:** 1.67x coverage
2. **High-quality assets:** Real estate in prime locations
3. **Strong brand:** Neiman Marcus luxury positioning
4. **Priority:** Absolute first claim on assets
5. **Control:** Dictated reorganization terms

**Lesson:**

- Secured debt is MUCH safer (97% vs 7.5% recovery)
- Overcollateralization is key (1.67x was strong cushion)
- Priority matters enormously (secured vs unsecured = 90% difference)
- **In distressed situations, seniority determines outcome**

---

## Best Case Scenario

### Perfect Default Risk Analysis

**Setup for avoiding losses:**

**Ideal conditions:**

1. **Conservative assumptions** (high PD, low recovery)
2. **Multiple methods** (historical, market, structural)
3. **Scenario analysis** (base, recession, crisis)
4. **Adequate risk premium** (2-3x expected loss)
5. **Diversification** (no single name >2% of portfolio)

### Best Case Example: High-Yield Portfolio 2010-2020 (No Defaults)

**Background:**

- Portfolio manager: Conservative high-yield specialist
- AUM: $500M
- Strategy: Avoid defaults at all costs
- Period: 2010-2020 (includes 2015-2016 energy crisis)

**Methodology:**

**1. Strict screening:**

- Interest coverage: >3.5x minimum
- Leverage: <4.5x Debt/EBITDA maximum
- Liquidity: >$200M cash + revolver
- Rating: BB+ to B+ only (avoid CCC)
- Industry: Avoid cyclical (no E&P, airlines, retail)

**2. Expected loss analysis:**

Every bond required:

$$
\text{Risk Premium} > 2.0 \times \text{Expected Loss}
$$

**Example bond that PASSED:**

**Healthcare Services Company:**

- Rating: BB
- Historical 5-year PD: 7.5%
- Cycle-adjusted PD: 9.0%
- Recovery (senior unsecured healthcare): 45%
- LGD: 55%
- Expected loss: 9.0% × 55% = 4.95% (5-year) = 0.99% annual
- Spread: 350 bps
- Risk premium: 350 - 99 = 251 bps
- **Ratio: 251 / 99 = 2.54x ✓ PASS**

**Example bond that FAILED screening:**

**Oil & Gas E&P Company:**

- Rating: BB
- Historical PD: 7.5%
- But: Cyclical industry, oil price dependent
- Adjusted PD: 15% (doubled for commodity risk)
- Recovery (E&P, low tangible assets): 25%
- LGD: 75%
- Expected loss: 15% × 75% = 11.25% = 2.25% annual
- Spread: 450 bps
- Risk premium: 450 - 225 = 225 bps
- **Ratio: 225 / 225 = 1.0x ✗ FAIL (need 2.0x+)**

**3. Portfolio construction:**

- 50 bonds (diversification)
- Max 2% per issuer ($10M max)
- Sector limits: 15% max per sector
- BB: 60%, B: 40%, CCC: 0%

**10-Year Results (2010-2020):**

| Year | # Defaults | Default Rate | Recovery (avg) | Actual Loss |
|------|-----------|--------------|----------------|-------------|
| 2010 | 0 | 0.0% | - | 0% |
| 2011 | 0 | 0.0% | - | 0% |
| 2012 | 0 | 0.0% | - | 0% |
| 2013 | 0 | 0.0% | - | 0% |
| 2014 | 0 | 0.0% | - | 0% |
| 2015 | 1 | 2.0% | 38% | 0.012% (1.2 bps!) |
| 2016 | 0 | 0.0% | - | 0% |
| 2017 | 0 | 0.0% | - | 0% |
| 2018 | 0 | 0.0% | - | 0% |
| 2019 | 0 | 0.0% | - | 0% |
| 2020 | 0 | 0.0% | - | 0% |
| **Total** | **1** | **0.18% avg** | **38%** | **0.001%** |

**One default details (2015):**

- Name: Regional telecom (pre-merger, integration failed)
- Original: 2% position ($10M)
- Time held: 3 years
- Recovery: 38 cents on dollar
- Loss: $6.2M on $500M portfolio = 1.2 bps

**Performance vs. benchmark:**

**High-Yield Index (2010-2020):**

- Default rate: 2.8% average
- Recovery rate: 42% average
- Loss rate: 2.8% × 58% = 1.62% avg annual

**Portfolio:**

- Default rate: 0.18% (6.4% of index!)
- Actual loss: 0.001% (0.6% of index!)
- **Avoided losses: 1.61% per year**

**Return attribution:**

- Gross yield: 6.8% average
- Actual losses: -0.001%
- Expenses: -0.60%
- **Net return: 6.2% annual**

**vs. Index:**

- Index gross: 6.5% average
- Index losses: -1.62%
- Index expenses: -0.50%
- **Index net: 4.38% annual**

**Outperformance: +1.82% per year from default avoidance**

**Cumulative 10-year:**

- Portfolio: 6.2% × 10 = 82% cumulative (compounded: 81.5%)
- Index: 4.38% × 10 = 54% cumulative (compounded: 54.2%)
- **Outperformance: +27.3% cumulative**

**Why it worked:**

1. **Conservative assumptions:** Used cycle-adjusted PD (higher than historical)
2. **High risk premium threshold:** 2.0x+ filter avoided marginal bonds
3. **Industry avoidance:** No E&P, airlines (saved during 2015-2016 energy, 2020 COVID)
4. **Diversification:** 50 bonds, 2% max, limited 1 default to 1.2 bps loss
5. **Discipline:** Passed on 60% of opportunities (quality over quantity)
6. **Coverage focus:** >3.5x interest coverage caught deteriorating credits early
7. **Long holding period:** Avoided trading costs, focused on fundamental quality

**This is the gold standard of credit investing: Boring, conservative, but dramatically outperformed through default avoidance.**

---

## Worst Case Scenario

### The Default and Recovery Disaster

**Worst possible conditions:**

1. **Optimistic assumptions** (low PD, high recovery)
2. **Concentration** (large positions in few names)
3. **Pro-cyclical** (bought late cycle, hold through recession)
4. **Subordinated debt** (low recovery priority)
5. **No diversification** (sector concentration)

### Worst Case Example: Energy High-Yield Fund 2014-2016 (Catastrophic)

**Background:**

- Specialized energy high-yield fund
- AUM: $1B (January 2014)
- Manager: Bullish on oil (expected $100+ oil forever)
- Strategy: Maximize yield, subordinated debt okay

**Portfolio (January 2014):**

- 100% energy sector (E&P, oilfield services, midstream)
- 20 bonds ($50M each = 5% per position)
- Rating: 40% BB, 50% B, 10% CCC
- Average yield: 8.5% (high for energy)
- Subordinated debt: 40% of portfolio

**Assumed default and recovery:**

- Expected PD (5-year): 10% (historical B average)
- Expected recovery: 50% (used historical unsecured average)
- **Expected loss: 10% × 50% = 5%**
- **Thought process: "8.5% yield - 1% annual expected loss = 7.5% return, great!"**

**What happened: Oil price collapse**

**Timeline:**

| Date | Oil Price | HY Energy Spread | Event |
|------|-----------|------------------|-------|
| Jan 2014 | $105 | 450 bps | Peak |
| Jun 2014 | $100 | 475 bps | Starting to crack |
| Dec 2014 | $60 | 750 bps | OPEC refuses to cut production |
| Mar 2015 | $45 | 1,100 bps | Panic selling |
| Jan 2016 | $28 | 1,800 bps | Capitulation |

**Portfolio destruction:**

**Phase 1 (2014): Mark-to-market pain**

- Oil: $105 → $60 (-43%)
- Bonds mark down 20-30% (spreads widen)
- Fund NAV: $1B → $750M (-25%)
- No defaults yet, but coming

**Phase 2 (2015): Defaults begin**

**Q1 2015:**
- 2 defaults (10% of portfolio, $100M)
- Both subordinated E&P companies
- Recovery estimate: 15% (assets worth little at $45 oil)
- Loss: $100M × 85% = $85M

**Q2 2015:**
- 3 more defaults ($150M)
- Oilfield services companies
- Recovery: 20% (equipment resale market collapsed)
- Loss: $150M × 80% = $120M

**Q3-Q4 2015:**
- 4 defaults ($200M)
- Mix of E&P and midstream
- Recovery: 10-25% average (20%)
- Loss: $200M × 80% = $160M

**2015 Total: 9 defaults (45% of original portfolio!), $365M losses**

**Phase 3 (2016): Final collapse**

**January 2016:** Oil touches $28

- 5 remaining distressed ($250M) default
- Recovery: 8% average (subordinated, liquidation)
- Loss: $250M × 92% = $230M

**Remaining 6 bonds ($300M):** Trading at 40 cents (distressed)

**Final tally (January 2016):**

- Original portfolio: $1B (20 bonds)
- Defaults: 14 bonds ($700M face value)
- Total recovery: $98M (14% average across all defaults)
- **Actual loss from defaults: $602M**

- Surviving 6 bonds: Trading at $120M (vs $300M face)
- **Mark-to-market: -$180M**

**Total portfolio value: $98M + $120M = $218M**

**Fund performance:**

- Started: $1B (Jan 2014)
- Ended: $218M (Jan 2016)
- **Loss: -78.2%**

**Investor outcome (typical):**

- Invested $1M (Jan 2014)
- Redeemed $218k (forced liquidation)
- **Loss: -$782,000 (-78.2%)**

**What went catastrophically wrong:**

**1. Sector concentration:**

- 100% energy (when oil collapsed, everything defaulted)
- No diversification benefit
- **Should have had <15% energy max**

**2. Optimistic recovery assumptions:**

- Assumed 50% recovery
- Actual: 14% (subordinated + commodity cyclical)
- **Error: 36% (72% worse than assumed!)**

**3. Wrong on defaults:**

- Assumed 10% 5-year PD (2% annual)
- Actual: 70% defaulted in 2 years (35% annual)
- **17.5x worse than assumed!**

**4. Subordinated debt:**

- 40% of portfolio in junior debt
- These recovered 8-12% (vs. senior unsecured 20-30%)
- **Self-inflicted wound: choosing lower recovery debt**

**5. Pro-cyclical timing:**

- Bought at peak oil prices ($105)
- Held through entire collapse ($28)
- **Couldn't sell: Liquidity dried up (spreads 1,800 bps)**

**6. No risk management:**

- No stop-loss (spreads 450→1,800 bps, held entire time)
- No hedging (didn't short oil, didn't reduce energy)
- **Rode it to -78%**

**Compounding the disaster:**

**Expected loss estimate was criminally wrong:**

- Manager's assumption: 10% PD × 50% LGD = 5% EL (5-year)
- **Reality: 70% PD × 86% LGD = 60.2% EL** (2-year!)

**12x worse than expected!**

**The psychological journey:**

- **2014: "Temporary oil correction, will rebound to $100"**
- **Early 2015: "Oil at $50 is the bottom, defaults will be limited"**
- **Mid 2015: "We've seen the worst, recovery starts now"**
- **Late 2015: "How could oil go to $30? This is unprecedented"**
- **2016: "Fund liquidating, career over"**

**Lessons:**

1. **Never concentrate:** 100% in one sector = guaranteed wipeout during sector crisis
2. **Subordinated = death:** Junior debt recovers 8-15% (vs. senior 40%+)
3. **Commodity risk:** E&P companies dependent on $100 oil = time bomb
4. **Recovery assumptions:** Use stressed scenarios (commodity cycle lows), not averages
5. **Default clustering:** Sector defaults happen together (9 in 2015!)
6. **Exit when wrong:** Spreads 450→750 bps (June 2014) was warning (should have sold then)
7. **Max sector exposure:** 15% max per sector (energy should have been $150M, not $1B)

**The fund manager was fired, sued by investors, and never worked in asset management again. This is what happens when you ignore default risk fundamentals.**

---

## What to Remember

### Core Concept

**Default and recovery analysis estimates the probability of non-payment and potential recovery, determining expected loss that drives credit spreads:**

$$
\text{Expected Loss} = \text{PD} \times (1 - \text{Recovery Rate})
$$

- PD varies by rating (AAA 0.05% to CCC 25% annually)
- Recovery varies by seniority (secured 60-80%, subordinated 15-30%)
- Expected loss must be less than spread for adequate compensation
- Risk premium = Spread - Expected Loss (target 1.5-2.5x EL)

### The Key Metrics

**Default probability (annual):**

- AAA/AA: <0.05%
- A: 0.05-0.10%
- BBB: 0.18-0.25%
- BB: 1.0-1.5%
- B: 4.0-5.0%
- CCC: 20-30%

**Recovery rates (senior unsecured):**

- Utilities: 60-70%
- Industrial: 40-50%
- Retail: 35-45%
- Technology: 25-35%
- Airlines: 15-25%

**Expected loss calculation:**

$$
\text{Spread Required} = \frac{\text{PD} \times \text{LGD}}{1 - \text{PD}} + \text{Risk Premium}
$$

### Risk Management

**Essential rules:**

- Diversification: Max 2-3% per issuer
- Sector limits: Max 15% per industry
- Rating limits: 70% BB/BBB, 30% B, 0% CCC
- Recovery analysis: Use stressed scenarios (recession recoveries)
- Risk premium: Require 1.5-2.5x expected loss
- Subordinated debt: Avoid (recovery 15-30% vs 40-60% senior)
- Covenant monitoring: Watch interest coverage <3x (danger zone)
- Exit discipline: Sell if spread widens >2x initial (fundamental deterioration)

### Maximum Profit/Loss

**Best case:**

- Conservative assumptions (high PD, low recovery estimates)
- Adequate risk premium (2.5x+ expected loss)
- Diversification (50+ issuers, <2% each)
- **Result: Near-zero default losses, 6-7% annual returns**

**Worst case:**

- Optimistic assumptions (low PD, high recovery)
- Sector concentration (100% energy, retail, airlines)
- Subordinated debt (8-15% recovery vs 40-60% senior)
- **Result: 50-80% loss during sector crisis**

**Expected (disciplined):**

- Default rate: 1-3% annually
- Recovery: 40% average
- Actual loss: 0.6-1.8% per year
- Spread: 3-4% (BB/B portfolio)
- **Net return: 1.2-3.4% above Treasuries after losses**

### When to Invest

**Invest in credit when:**

- Risk premium >2x expected loss (adequate compensation)
- Early/mid cycle (low default risk environment)
- Fundamentals strong (coverage >4x, leverage <4x)
- Diversification possible (many issuers available)
- Senior secured available (60-80% recovery potential)

**Avoid credit when:**

- Risk premium <1.5x expected loss (inadequate)
- Late cycle (defaults rising, recoveries falling)
- Sector stress (commodity collapse, regulatory change)
- Forced concentration (limited issuers, sector-specific)
- Only subordinated available (15-30% recovery)

### Common Mistakes

1. Using average recovery rates (should use recession-scenario recoveries)
2. Sector concentration (>30% in one industry)
3. Buying subordinated debt (huge recovery disadvantage)
4. Ignoring interest coverage (falling below 3x is red flag)
5. Optimistic default assumptions (use historical + cycle adjustment)
6. No risk premium threshold (buying anything with positive spread)
7. Late cycle buying (defaults cluster in recessions)
8. Large position sizes (>5% in single issuer)

### Final Wisdom

> "Default and recovery analysis is the foundation of credit investing—get this wrong and everything else fails. The math is deceptively simple: a BB bond with 7.5% default probability and 40% recovery has 4.5% expected loss over 5 years (0.9% annually). If it pays 350 bps spread, you're getting 260 bps risk premium (2.9x expected loss)—seems attractive! But here's the trap: those are average assumptions. In the actual default (2015-2016 energy crisis, 2020 retail), three things go wrong simultaneously: (1) PD spikes 5-10x (sector defaults cluster), (2) Recovery falls 15-20% (fire sale prices when everyone defaults together), (3) Mark-to-market spreads widen 3-5x (you can't exit without huge losses). That 'safe' 0.9% annual expected loss becomes 8-12% actual loss in two years, wiping out a decade of spread income. The difference between successful credit investors and blown-up funds is conservative assumptions: use recession-scenario default rates (not average), use stressed recoveries (not historical mean), and require 2.0-2.5x risk premium (not 1.0x). Diversify ruthlessly (50+ names, max 2% each, max 15% per sector), avoid subordinated debt entirely (recovers 15% vs 45% for senior), and exit when coverage falls below 3x or spreads double (don't hope for mean reversion). Done right, credit delivers 2-4% excess returns with <1% default losses annually. Done wrong, it delivers -50% to -80% losses in sector crises. The math works only if your assumptions are conservative and stress-tested."

**Key to success:**

- Use recession-scenario default rates (+50% vs average)
- Use fire-sale recovery rates (-15% vs average)
- Require risk premium 2.0-2.5x expected loss minimum
- Diversify: 50+ names, <2% each, <15% per sector
- Avoid subordinated debt (stick to senior unsecured or secured)
- Monitor interest coverage (exit if <3x)
- Sell if spreads double from purchase (fundamental deterioration)
- Stay conservative on position sizing and sector limits

**Most important:** In credit, permanent loss of capital is the enemy. Spread income is small (3-5% per year), but default losses can be 60-90% of principal. The asymmetry is brutal: you collect 3% per year for 10 years (+30%), then lose 60% in one default (-60%), netting -30% over decade. Successful credit investing is 90% avoiding losers (default avoidance), 10% picking winners (spread maximization). Be conservative on defaults, paranoid on recovery rates, diversified on exposures, and disciplined on exits. Boring credit analysis saves fortunes. 💰📊⚠️

