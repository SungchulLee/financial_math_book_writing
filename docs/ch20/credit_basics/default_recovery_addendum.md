# Default Risk and Recovery: Supplementary Content

This addendum addresses enhancement suggestions from the chapter review, including recovery rate volatility, Altman Z-score analysis, and post-COVID recovery data.

---

## Recovery Rate Volatility and Default Clusters


**Recovery rates are not fixed—they vary dramatically:**

### The Clustering Problem


**Recovery rates are negatively correlated with default rates:**

$$
\text{Corr}(\text{Recovery Rate}, \text{Default Rate}) \approx -0.5 \text{ to } -0.7
$$

**Intuition:** When many companies default simultaneously:
- Asset supply floods the market
- Fewer buyers available
- Fire-sale conditions
- Recoveries plummet

### Empirical Evidence


**Recovery rates by default rate environment:**

| Default Rate Environment | Avg Senior Unsecured Recovery | Std Dev |
|--------------------------|------------------------------|---------|
| Low (<2% HY default rate) | 48% | 22% |
| Normal (2-5%) | 42% | 24% |
| Elevated (5-8%) | 35% | 26% |
| Crisis (>8%) | 25% | 28% |

**Historical examples:**

| Year | HY Default Rate | Senior Unsecured Recovery | Notable Events |
|------|-----------------|---------------------------|----------------|
| 2006 | 1.4% | 51% | Benign credit |
| 2008 | 4.1% | 28% | Financial crisis |
| 2009 | 10.7% | 22% | Peak crisis |
| 2015 | 3.0% | 30% | Energy collapse |
| 2016 | 5.1% | 27% | Energy/retail stress |
| 2020 | 6.2% | 32% | COVID-19 |
| 2021 | 1.0% | 55% | Recovery + stimulus |

### Modeling Recovery Volatility


**Beta distribution for recovery rates:**

$$
R \sim \text{Beta}(\alpha, \beta)
$$

With parameters calibrated to historical mean and variance.

**Mean and variance:**

$$
\mathbb{E}[R] = \frac{\alpha}{\alpha + \beta}
$$

$$
\text{Var}[R] = \frac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)}
$$

**Example calibration for senior unsecured:**
- Mean recovery: 42%
- Std dev: 24%
- Implied: $\alpha \approx 2.0$, $\beta \approx 2.8$

**Simulation approach:**

1. Draw systemic factor $Z \sim N(0,1)$
2. Shift recovery mean based on $Z$: $\bar{R}(Z) = \bar{R}_0 + \gamma Z$
3. Draw individual recovery: $R_i \sim \text{Beta}(\alpha(Z), \beta(Z))$

**This captures both systematic and idiosyncratic recovery variation.**

### Portfolio Implications


**Expected loss with recovery volatility:**

For a single name:
$$
\mathbb{E}[\text{Loss}] = \text{PD} \times \mathbb{E}[1 - R] = \text{PD} \times (1 - \bar{R})
$$

For a portfolio with correlated defaults and recoveries:
$$
\mathbb{E}[\text{Loss}] = \sum_i \text{PD}_i \times \mathbb{E}[1 - R_i | \text{default cluster}]
$$

**The conditional recovery given default cluster is lower than unconditional.**

**Stress test adjustment:**

| Scenario | Default Rate | Recovery Assumption | Expected Loss |
|----------|--------------|---------------------|---------------|
| Base | 3% | 40% | 1.8% |
| Stress | 8% | 28% | 5.8% |
| Crisis | 12% | 20% | 9.6% |

**Using base-case recovery in stress scenarios understates risk by 40-50%.**

---

## Altman Z-Score and Fundamental Distress Indicators


### The Altman Z-Score Model


**Original Z-Score formula (1968):**

$$
Z = 1.2 X_1 + 1.4 X_2 + 3.3 X_3 + 0.6 X_4 + 1.0 X_5
$$

Where:
- $X_1$ = Working Capital / Total Assets
- $X_2$ = Retained Earnings / Total Assets
- $X_3$ = EBIT / Total Assets
- $X_4$ = Market Value Equity / Book Value Debt
- $X_5$ = Sales / Total Assets

**Interpretation zones:**

| Z-Score | Zone | Default Probability |
|---------|------|---------------------|
| > 2.99 | Safe | <5% (2-year) |
| 1.81 - 2.99 | Gray | 15-35% |
| < 1.81 | Distress | >50% |

### Z-Score Variants


**Z'-Score (Private Companies):**

$$
Z' = 0.717 X_1 + 0.847 X_2 + 3.107 X_3 + 0.420 X_4 + 0.998 X_5
$$

Where $X_4$ = Book Value Equity / Book Value Debt

**Zones:** Safe > 2.90, Distress < 1.23

**Z''-Score (Non-Manufacturing/Emerging Markets):**

$$
Z'' = 6.56 X_1 + 3.26 X_2 + 6.72 X_3 + 1.05 X_4
$$

**Zones:** Safe > 2.60, Distress < 1.10

### Practical Application


**Example: Analyzing a BBB Retail Company**

**Financial data:**
- Total Assets: $5,000M
- Working Capital: $400M
- Retained Earnings: $800M
- EBIT: $350M
- Market Cap: $1,800M
- Total Debt: $2,500M
- Sales: $8,000M

**Z-Score calculation:**

| Variable | Value | Weight | Contribution |
|----------|-------|--------|--------------|
| $X_1$ | 0.08 | 1.2 | 0.096 |
| $X_2$ | 0.16 | 1.4 | 0.224 |
| $X_3$ | 0.07 | 3.3 | 0.231 |
| $X_4$ | 0.72 | 0.6 | 0.432 |
| $X_5$ | 1.60 | 1.0 | 1.600 |
| **Z-Score** | | | **2.58** |

**Interpretation:** Gray zone (1.81 < 2.58 < 2.99). Elevated distress risk.

### Alternative Distress Indicators


**1. Merton Distance-to-Default (DD):**

$$
DD = \frac{\ln(V/D) + (\mu - 0.5\sigma^2)T}{\sigma\sqrt{T}}
$$

| DD | Default Probability |
|----|---------------------|
| > 3.0 | <1% |
| 2.0 - 3.0 | 1-5% |
| 1.0 - 2.0 | 5-15% |
| 0 - 1.0 | 15-30% |
| < 0 | >30% |

**2. Ohlson O-Score:**

$$
O = -1.32 - 0.407 \text{SIZE} + 6.03 \text{TLTA} - 1.43 \text{WCTA} + 0.076 \text{CLCA} - 1.72 \text{OENEG} - 2.37 \text{NITA} - 1.83 \text{FUTL} + 0.285 \text{INTWO} - 0.521 \text{CHIN}
$$

**3. Simple Financial Ratios:**

| Ratio | Healthy | Warning | Distressed |
|-------|---------|---------|------------|
| Debt/EBITDA | <3.0x | 3.0-5.0x | >5.0x |
| Interest Coverage | >4.0x | 2.0-4.0x | <2.0x |
| Current Ratio | >1.5 | 1.0-1.5 | <1.0 |
| FCF/Debt | >15% | 5-15% | <5% |

### Combining Indicators


**Multi-factor distress score:**

$$
\text{Distress Score} = w_1 \text{(Z-Score)} + w_2 \text{(DD)} + w_3 \text{(Coverage)} + w_4 \text{(Market Signal)}
$$

**Example weighting:**

| Factor | Weight | Source |
|--------|--------|--------|
| Z-Score | 25% | Accounting |
| Distance-to-Default | 25% | Market (equity) |
| Interest Coverage | 20% | Accounting |
| CDS/Bond Spread | 20% | Market (credit) |
| Rating | 10% | Agency |

**This multi-factor approach outperforms any single indicator.**

---

## Post-COVID Recovery Data (2020-2024)


### Recovery Rates by Seniority (2020-2024)


**Updated recovery statistics:**

| Seniority | 2020 | 2021 | 2022 | 2023 | 2024* | 5-Year Avg |
|-----------|------|------|------|------|-------|------------|
| Senior Secured (1st Lien) | 62% | 72% | 68% | 65% | 67% | 67% |
| Senior Secured (2nd Lien) | 38% | 55% | 48% | 42% | 45% | 46% |
| Senior Unsecured | 32% | 48% | 42% | 38% | 40% | 40% |
| Subordinated | 15% | 28% | 22% | 18% | 20% | 21% |

*2024 data preliminary

### Recovery Rates by Industry (2020-2024)


| Industry | Pre-COVID (2015-19) | 2020 | 2021-24 | Change |
|----------|---------------------|------|---------|--------|
| Energy | 25% | 18% | 45% | +20 pp |
| Retail | 30% | 22% | 35% | +5 pp |
| Healthcare | 45% | 40% | 48% | +3 pp |
| Media/Telecom | 38% | 35% | 42% | +4 pp |
| Technology | 28% | 32% | 38% | +10 pp |
| Manufacturing | 48% | 42% | 50% | +2 pp |
| Transportation | 35% | 15% | 40% | +5 pp |
| Hospitality | 40% | 12% | 45% | +5 pp |

**Key observations:**

1. **2020 anomaly:** COVID lockdowns crushed hospitality/transportation recoveries
2. **2021 rebound:** Stimulus + reopening lifted recoveries above historical
3. **2022-24 normalization:** Returning to long-term averages
4. **Energy improvement:** Post-2015/16 distress, healthier balance sheets

### COVID-19 Specific Lessons


**1. Government Support Matters:**

| Company | Sector | Initial Recovery Est | Final Recovery | Reason |
|---------|--------|---------------------|----------------|--------|
| Hertz | Car Rental | 8% | 100% | Meme stock rally, emerged |
| Latam Airlines | Airline | 15% | 65% | Chile government support |
| Neiman Marcus | Retail | 20% | 42% | DIP financing available |
| JCPenney | Retail | 12% | 28% | Sale to mall owners |

**2. Pre-pandemic Leverage Mattered:**

Companies with Debt/EBITDA > 6x pre-COVID had 40% lower recoveries than those with < 4x.

**3. Liquidity Position Critical:**

| Pre-COVID Cash/Assets | Avg Recovery |
|-----------------------|--------------|
| > 10% | 52% |
| 5-10% | 40% |
| < 5% | 28% |

### Updated Recovery Rate Recommendations


**For stress testing and analysis (post-COVID):**

| Seniority | Base Case | Stress Case | Crisis Case |
|-----------|-----------|-------------|-------------|
| Senior Secured 1L | 65% | 50% | 35% |
| Senior Secured 2L | 45% | 30% | 15% |
| Senior Unsecured | 40% | 25% | 10% |
| Subordinated | 20% | 8% | 0% |

**Industry adjustments to base case:**

| Industry | Adjustment |
|----------|------------|
| Utilities | +15% |
| Healthcare | +5% |
| Manufacturing | 0% |
| Technology | -5% |
| Retail | -10% |
| Airlines/Hospitality | -15% |

---

## Summary: Enhanced Default and Recovery Framework


### Comprehensive Analysis Checklist


**1. Default probability estimation:**
- [ ] Historical rating-based PD
- [ ] Market-implied PD (from CDS/spreads)
- [ ] Merton distance-to-default
- [ ] Altman Z-score check

**2. Recovery rate analysis:**
- [ ] Seniority-based starting point
- [ ] Industry adjustment
- [ ] Cycle adjustment (default rate environment)
- [ ] Specific collateral analysis (if secured)

**3. Stress testing:**
- [ ] Use crisis recovery rates (not averages)
- [ ] Model recovery-default correlation
- [ ] Include recovery volatility
- [ ] Test multiple scenarios

**4. Portfolio considerations:**
- [ ] Concentration limits by seniority
- [ ] Sector recovery correlation
- [ ] Systematic vs. idiosyncratic exposure

### Key Formulas Summary


**Expected loss with recovery volatility:**

$$
\text{EL} = \text{PD} \times \mathbb{E}[\text{LGD}] + \text{Cov}(\text{Default}, \text{LGD})
$$

**Conditional recovery in stress:**

$$
\mathbb{E}[R | \text{Stress}] = \mathbb{E}[R] - \beta \times (\text{Default Rate} - \text{Avg Default Rate})
$$

Where $\beta \approx 2-3$ (recovery falls 2-3% for each 1% increase in default rate).

**Multi-factor distress score:**

$$
\text{Distress} = \sum_i w_i \times \text{Normalized}(\text{Factor}_i)
$$

These enhanced frameworks ensure more robust credit risk assessment, particularly for portfolio stress testing and crisis scenario analysis.
