# Credit Spreads and OAS


**Credit spreads** measure the excess yield investors demand for holding a risky bond over a risk-free alternative, compensating for default risk, liquidity risk, and other credit-related factors. **Option-Adjusted Spread (OAS)** refines this measure by stripping out the value of embedded options, providing a cleaner measure of pure credit risk compensation.

---

## The Core Insight


**The fundamental idea:**

- Corporate bonds yield more than Treasuries (the risk-free rate)
- This excess yield is the "credit spread"
- Spreads compensate for default risk, liquidity risk, tax treatment, and other factors
- Wider spreads = higher compensation for risk (or deteriorating credit quality)
- Embedded options (calls, puts) distort raw spreads
- OAS removes option value to isolate pure credit spread
- Spreads are the primary signal for credit market conditions
- Spread changes drive the majority of corporate bond returns

**The key equations:**

**Nominal spread (simple but crude):**

$$
\text{Nominal Spread} = \text{YTM}_{\text{corporate}} - \text{YTM}_{\text{Treasury}}
$$

**Z-spread (zero-volatility spread):**

$$
P = \sum_{t=1}^{n} \frac{CF_t}{(1 + r_t + Z)^t}
$$

Where $Z$ is the constant spread added to each spot rate.

**Option-Adjusted Spread (OAS):**

$$
P = \mathbb{E}\left[\sum_{t=1}^{n} \frac{CF_t}{(1 + r_t + \text{OAS})^t}\right]
$$

Expected value accounts for option exercise scenarios.

**The fundamental relationship:**

$$
\text{Z-spread} = \text{OAS} + \text{Option Cost}
$$

**You're essentially asking: "How much extra yield am I getting for taking credit risk, after removing the confounding effects of embedded options, and is this compensation adequate for the risk I'm bearing?"**

---

## What Are Credit Spreads and OAS?


**Before trading credit or analyzing bonds, understand the spread framework:**

### 1. The Hierarchy of Spreads


**Credit spreads measure excess yield over risk-free rate, but there are multiple definitions:**

**1. Nominal Spread (G-spread):**

$$
\text{G-spread} = \text{YTM}_{\text{corporate}} - \text{YTM}_{\text{benchmark Treasury}}
$$

**Example:**
- 10-year corporate bond: YTM = 5.50%
- 10-year Treasury: YTM = 4.00%
- **G-spread = 1.50% or 150 basis points**

**Problems with nominal spread:**
- Ignores term structure (yield curve shape)
- Assumes flat curve
- Not additive across different maturities
- **Too simplistic for professional use**

**2. Z-Spread (Zero-Volatility Spread):**

$$
P_{\text{corporate}} = \sum_{t=1}^{n} \frac{CF_t}{(1 + r_t + Z)^t}
$$

Where:
- $P_{\text{corporate}}$ = Current market price
- $CF_t$ = Cash flow at time $t$
- $r_t$ = Treasury spot rate for maturity $t$
- $Z$ = Z-spread (constant added to each spot rate)

**Interpretation:** The constant spread added to each Treasury spot rate that makes the present value equal the market price.

**Example:**

- Corporate bond price: $98.00
- Cash flows: $5 annually for 10 years + $100 principal
- Treasury spot curve: $r_1 = 3.5\%$, $r_2 = 3.7\%$, ..., $r_{10} = 4.2\%$
- Find $Z$ such that:

$$
98 = \frac{5}{(1.035+Z)} + \frac{5}{(1.037+Z)^2} + ... + \frac{105}{(1.042+Z)^{10}}
$$

**Solution: Z ≈ 1.62% or 162 bp**

**Advantages:**
- Uses full term structure
- Properly accounts for curve shape
- Industry standard for bullet bonds

**3. Option-Adjusted Spread (OAS):**

$$
P = \mathbb{E}_{\text{paths}}\left[\sum_{t=1}^{n} \frac{CF_t(\text{path})}{(1 + r_t(\text{path}) + \text{OAS})^t}\right]
$$

**For bonds with embedded options:**
- Simulate many interest rate paths
- On each path, determine if option exercised (call/put)
- Calculate cash flows accordingly
- Discount at spot rates + OAS
- Average across all paths

**Example: Callable bond**

- Z-spread: 180 bp
- Option value: 30 bp
- **OAS = 180 - 30 = 150 bp**

**The 30 bp difference is the value the issuer pays for the call option.**

**4. I-Spread (Interpolated Spread):**

$$
\text{I-spread} = \text{YTM}_{\text{corporate}} - \text{Swap Rate}_{\text{interpolated}}
$$

**Used when:**
- Comparing to swap curve instead of Treasuries
- International markets (Treasuries not universal benchmark)
- Preferred by many European investors

**5. Asset Swap Spread (ASW):**

$$
\text{ASW} = \text{Fixed leg spread over LIBOR such that bond + swap = par}
$$

**Converts fixed-rate bond into floating-rate equivalent.**

**Example:**
- Buy bond at $98
- Enter asset swap
- Receive: Bond coupons
- Pay: LIBOR + spread
- Net: Floating rate exposure at LIBOR + ASW spread

### 2. Why OAS Matters


**The problem with Z-spread on callable bonds:**

**Example: Two bonds, same issuer, same maturity**

| Bond | Type | Price | YTM | Z-spread |
|------|------|-------|-----|----------|
| A | Bullet (non-callable) | $100 | 5.00% | 100 bp |
| B | Callable @ $105 | $98 | 5.75% | 175 bp |

**Naive conclusion:** Bond B has higher spread (175 bp vs. 100 bp), therefore better value!

**WRONG!**

**Correct analysis with OAS:**

| Bond | Z-spread | Option Value | OAS |
|------|----------|--------------|-----|
| A | 100 bp | 0 bp | 100 bp |
| B | 175 bp | 85 bp | 90 bp |

**Real conclusion:** Bond A offers better credit compensation (100 bp OAS vs. 90 bp OAS). Bond B's higher Z-spread is mostly option premium, not credit compensation.

**OAS reveals true credit value by stripping out option effects.**

### 3. OAS Calculation Process


**Step-by-step for callable bond:**

**1. Build interest rate model:**
- Calibrate to current Treasury curve
- Include volatility (from swaptions, caps/floors)
- Generate 1,000+ rate scenarios

**2. For each scenario:**
- Simulate path of short rates
- Determine call decision at each date
  - Call if bond price > call price
  - Don't call otherwise
- Calculate cash flows based on call/no-call

**3. Solve for OAS:**
- Find constant spread such that:
- Average PV across all scenarios = market price
- Iterate until convergence

**Example output:**

```
Scenario 1 (rates low): Bond called at year 3, PV = $102.50
Scenario 2 (rates high): Bond not called, runs to maturity, PV = $96.80
...
Scenario 1000: PV = $99.20

Average PV across 1000 scenarios = $98.00 (market price)
OAS that achieves this: 152 bp
```

**Computational intensity:**
- 1,000 scenarios × 10 years × quarterly timesteps = 40,000 calculations
- Must iterate to find OAS
- Requires sophisticated modeling software

**This is why OAS matters: It properly prices embedded options.**

---

## Economic Interpretation: Why Credit Spreads Exist


**Understanding the fundamental economics of credit spreads:**

### 1. The Credit Spread Decomposition


**Credit spread compensates for multiple risks:**

$$
\text{Credit Spread} = \underbrace{\text{Default Risk}}_{\text{Expected Loss}} + \underbrace{\text{Liquidity Premium}}_{\text{Trading cost}} + \underbrace{\text{Tax Premium}}_{\text{Tax disadvantage}} + \underbrace{\text{Systemic Risk}}_{\text{Beta to market}} + \underbrace{\alpha}_{\text{Mispricing}}
$$

**1. Default Risk (Expected Loss):**

$$
\text{Expected Loss} = \text{PD} \times \text{LGD}
$$

Where:
- PD = Probability of Default (annualized)
- LGD = Loss Given Default (1 - Recovery Rate)

**Example:**
- Corporate bond: 10-year maturity
- PD: 2.0% cumulative (0.20% annual)
- LGD: 60% (40% recovery)
- **Expected loss: 0.20% × 60% = 0.12% annually = 12 bp**

**But actual spread: 150 bp**

**The other 138 bp compensates for other risks!**

**2. Liquidity Premium:**

**Corporates are less liquid than Treasuries:**
- Wider bid-ask spreads
- Less frequent trading
- Harder to exit large positions
- **Investors demand compensation: 20-50 bp typically**

**Measurement:**
$$
\text{Liquidity Premium} \approx \text{Bid-Ask Spread} \times \text{Turnover Factor}
$$

**Example:**
- Treasury: 1/32 bid-ask ($0.03 per $100)
- Corporate: 1/4 point bid-ask ($0.25 per $100)
- **Extra cost: 0.22 points or ~22 bp for 1-year holding period**

**3. Tax Premium:**

**Treasury interest is state/local tax-exempt:**
- Corporate bonds: Fully taxable
- For high-tax investors: 10-30 bp disadvantage

**Example:**
- Investor in California: State tax 13.3%
- Federal tax: 37%
- **Combined tax on corporates >> Treasuries**
- Demands extra 15-25 bp compensation

**4. Systemic Risk Premium:**

**Corporate bonds have equity-like beta:**
- Correlate with stock market
- Fall during recessions
- **Systemic risk premium: 30-60 bp**

**CAPM framework:**

$$
\text{Required Return} = r_f + \beta_{\text{credit}} \times (\text{Market Return} - r_f)
$$

**Corporate bond beta ≈ 0.25-0.40** to equities.

**5. Alpha (Mispricing):**

**The residual after accounting for all compensated risks:**

$$
\alpha = \text{Observed Spread} - \text{Fair Spread}
$$

**This is what credit analysts seek:**
- Positive alpha: Bond cheap (buy!)
- Negative alpha: Bond rich (sell/avoid)

**Example decomposition:**

| Component | Basis Points | % of Total |
|-----------|--------------|------------|
| Expected default loss | 12 bp | 8% |
| Liquidity premium | 30 bp | 20% |
| Tax premium | 18 bp | 12% |
| Systemic risk | 45 bp | 30% |
| **Fair spread** | **105 bp** | **70%** |
| **Observed spread** | **150 bp** | **100%** |
| **Alpha (mispricing)** | **+45 bp** | **30%** |

**Conclusion: This bond offers +45 bp of excess value!**

### 2. The Relationship Between Spreads and Default Risk


**Merton model framework:**

Corporate bond = Risk-free bond - Put option on firm assets

$$
\text{Corporate Bond} = \text{Treasury} - \text{Put}(V_{\text{assets}}, K = \text{Debt})
$$

**Implications:**

**As firm value decreases:**
- Put option value increases
- Corporate bond value decreases
- **Credit spread widens**

**As volatility increases:**
- Put option value increases
- **Credit spread widens** (even with no change in current value)

**Distance to default:**

$$
DD = \frac{\ln(V/K) + (\mu - \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
$$

**Higher distance to default → Lower spread**

**Empirical relationship:**

$$
\text{Spread} \approx a \times e^{-b \times DD}
$$

**Credit spreads follow exponential decay with distance to default.**

### 3. OAS as Pure Credit Compensation


**Think of Z-spread as contaminated:**

$$
\text{Z-spread} = \underbrace{\text{Credit Compensation}}_{\text{What we want}} + \underbrace{\text{Option Value}}_{\text{Confounding factor}}
$$

**OAS removes the option value:**

$$
\text{OAS} = \text{Z-spread} - \text{Option Value}
$$

**Now we can compare across bonds:**

**Example: Three bonds from same issuer**

| Bond | Type | Z-spread | Option Value | OAS | Conclusion |
|------|------|----------|--------------|-----|------------|
| A | Bullet | 120 bp | 0 bp | 120 bp | Reference |
| B | Callable | 185 bp | 70 bp | 115 bp | Slightly cheap |
| C | Putable | 95 bp | -15 bp | 110 bp | Rich |

**OAS allows apples-to-apples comparison despite different option features.**

**Bond B offers best relative value (115 bp OAS vs. 120 bp reference).**

---

## Key Terminology


**Credit Spread:**

- Excess yield over risk-free rate
- Measured in basis points (bp)
- Wider spread = higher risk or better value
- Primary metric for credit analysis

**G-spread (Government Spread):**

- Simple YTM difference vs. Treasury
- Ignores curve shape
- Benchmark-maturity specific
- **Least sophisticated measure**

**Z-spread (Zero-Volatility Spread):**

- Constant spread over entire spot curve
- Proper term structure accounting
- Industry standard for bullet bonds
- **No option adjustment**

**OAS (Option-Adjusted Spread):**

- Spread after removing embedded option value
- Requires interest rate model
- Industry standard for callable/putable bonds
- **Pure credit compensation**

**I-spread (Interpolated Spread):**

- Spread over swap curve (not Treasury)
- Used internationally
- Avoids sovereign-specific distortions
- Common in Europe

**ASW (Asset Swap Spread):**

- Converts fixed bond to floating
- Spread over LIBOR (historically) or SOFR (now)
- Used by relative value traders
- Reflects funding costs

**Spread Duration:**

$$
\text{Spread Duration} = -\frac{1}{P} \frac{\partial P}{\partial s}
$$

Where $s$ = credit spread.

**Interpretation:** Price change for 1 bp spread change.

**Effective Duration:**

- Duration accounting for embedded options
- Changes as rates move (for callables)
- **Lower than modified duration for callables**

**Option Cost:**

$$
\text{Option Cost} = \text{Z-spread} - \text{OAS}
$$

**Positive for callable bonds (issuer owns call)**
**Negative for putable bonds (investor owns put)**

**Spread Volatility:**

- Historical standard deviation of spread changes
- Used in risk models
- Varies by rating (HY > IG), sector, and liquidity

**Credit Curve:**

- Relationship between spread and maturity
- Typically upward sloping (longer = wider)
- Can invert during stress

**CDS-Cash Basis:**

$$
\text{Basis} = \text{CDS Spread} - \text{Z-spread}
$$

**Typically 20-40 bp, represents arbitrage/funding frictions.**

---

## Basic Spread Analysis Strategies


### 1. Strategy 1: Relative Value via OAS Comparison


**Setup:**

**Compare bonds from same issuer with different structures:**

**Company XYZ (A-rated industrial):**

| Bond | Maturity | Coupon | Price | YTM | Z-spread | OAS | Feature |
|------|----------|--------|-------|-----|----------|-----|---------|
| A | 10-year | 5.00% | $100 | 5.00% | 120 bp | 120 bp | Bullet |
| B | 10-year | 5.50% | $102 | 5.10% | 175 bp | 125 bp | Callable @ 105 |
| C | 10-year | 4.50% | $99 | 4.65% | 95 bp | 100 bp | Putable @ 98 |

**Analysis:**

**Bond A (Bullet):**
- OAS: 120 bp
- **Reference point** (no options)

**Bond B (Callable):**
- Z-spread: 175 bp (looks attractive!)
- BUT: Option cost = 175 - 125 = 50 bp
- OAS: 125 bp (only 5 bp over reference)
- **Conclusion: Fair value, not cheap**

**Bond C (Putable):**
- OAS: 100 bp (20 bp below reference)
- Put option worth: 95 - 100 = -5 bp (negative because investor owns it)
- **Conclusion: Rich, avoid**

**Trade recommendation:**
- Buy Bond B (callable): 125 bp OAS, slight pickup over reference
- Avoid Bond C (putable): Only 100 bp OAS, undercompensated

### 2. Strategy 2: Sector Rotation via Spread Analysis


**Setup:**

**Comparing sectors at same rating level (BBB):**

| Sector | Avg OAS | Historical Avg | Percentile | View |
|--------|---------|----------------|------------|------|
| Utilities | 135 bp | 145 bp | 35th | Slightly rich |
| Industrials | 165 bp | 155 bp | 70th | Slightly wide |
| Financials | 185 bp | 160 bp | 85th | Wide (cheap) |
| Energy | 220 bp | 190 bp | 90th | Very wide |

**Analysis:**

**Financials: 185 bp OAS at 85th percentile**
- Currently 25 bp wider than historical average
- 85th percentile suggests spreads are wide
- **Potential opportunity if no fundamental deterioration**

**Energy: 220 bp at 90th percentile**
- Extremely wide relative to history
- But: Oil prices volatile, sector stress possible
- **High risk, high potential return**

**Trade:**
- Overweight Financials (wide spreads, stable fundamentals)
- Underweight Utilities (tight spreads, limited upside)
- Neutral Energy (wide but risky)

### 3. Strategy 3: Credit Curve Positioning


**Setup:**

**Single issuer (BBB-rated) credit curve:**

| Maturity | OAS | Historical 5-year avg | Z-score | Attractiveness |
|----------|-----|----------------------|---------|----------------|
| 3-year | 95 bp | 105 bp | -0.8 | Rich |
| 5-year | 125 bp | 130 bp | -0.4 | Slightly rich |
| 7-year | 155 bp | 150 bp | +0.3 | Fair |
| 10-year | 195 bp | 175 bp | +1.2 | Cheap |
| 30-year | 245 bp | 220 bp | +1.5 | Very cheap |

**Analysis:**

**Front end (3-5 year): Rich**
- Trading 10-15 bp inside historical averages
- Limited upside, downside risk if spreads normalize
- **Avoid or underweight**

**Long end (10-30 year): Cheap**
- Trading 20-25 bp wider than historical averages
- Z-score > +1.0 suggests value
- **Overweight opportunity**

**Trade:**
- Barbell: Long 10-year and 30-year, underweight 5-year
- Capture carry from long end
- Benefit from curve normalization (long end tightening)

### 4. Strategy 4: OAS-to-Rating Analysis


**Setup:**

**Check if OAS is appropriate for credit rating:**

**BBB-rated corporate universe:**

| Percentile | OAS | Interpretation |
|------------|-----|----------------|
| 10th (tight) | 110 bp | Rich |
| 25th | 135 bp | Somewhat rich |
| 50th (median) | 155 bp | Fair value |
| 75th | 180 bp | Somewhat cheap |
| 90th (wide) | 210 bp | Cheap |

**Individual bonds:**

| Bond | Rating | OAS | Percentile | Action |
|------|--------|-----|------------|--------|
| XYZ Corp | BBB | 140 bp | 30th | Slightly rich, hold |
| ABC Inc | BBB | 195 bp | 80th | Cheap, buy |
| DEF Co | BBB | 115 bp | 5th | Very rich, sell |

**Trade:**
- Buy ABC Inc (195 bp at 80th percentile)
- Sell/avoid DEF Co (115 bp at 5th percentile)

---

## Greeks in Credit Spreads


**Understanding the sensitivities:**

### 1. Spread Duration (DV01)


$$
\text{Spread Duration} = -\frac{1}{P} \frac{\partial P}{\partial s}
$$

**Interpretation:** Percentage price change for 1% (100 bp) change in credit spread.

**Also measured as spread DV01:**

$$
\text{Spread DV01} = -\frac{\partial P}{\partial s} \times 0.0001
$$

**Dollar change for 1 bp spread change.**

**Example:**

- Corporate bond: Price $100, Duration 7.0 years
- Spread duration ≈ Duration (for parallel shifts)
- **If spread widens 50 bp: Price falls ≈ 3.5%**

**Calculation:**

$$
\Delta P \approx -\text{Spread Duration} \times P \times \Delta s
$$

$$
\Delta P = -7.0 \times 100 \times 0.005 = -3.5
$$

**New price: $96.50**

**Key insight:** Spread duration ≈ Modified duration for corporate bonds.

**But for different scenarios:**

| Scenario | Rate Duration | Spread Duration | Total |
|----------|--------------|----------------|-------|
| Rates unchanged, spreads +50 bp | 0 | -3.5% | -3.5% |
| Rates +50 bp, spreads unchanged | -3.5% | 0 | -3.5% |
| Rates +50 bp, spreads +50 bp | -3.5% | -3.5% | -7.0% |
| Rates -50 bp, spreads +50 bp | +3.5% | -3.5% | 0% |

**Last scenario is typical in flight-to-quality: Rates rally, spreads widen, net flat.**

### 2. Effective Duration for Callables


**Standard duration assumes no cash flow changes:**

$$
\text{Modified Duration} = -\frac{1}{P} \frac{\partial P}{\partial y}
$$

**But callable bonds' cash flows DO change:**

**Effective duration accounts for this:**

$$
\text{Effective Duration} = \frac{P_{-} - P_{+}}{2 \times P_0 \times \Delta y}
$$

Where:
- $P_{-}$ = Price if yields fall by $\Delta y$
- $P_{+}$ = Price if yields rise by $\Delta y$
- $P_0$ = Current price

**Example: Callable bond**

- Current price: $102
- If yields -25 bp: Price $103 (capped by call price $105)
- If yields +25 bp: Price $98.50

$$
\text{Effective Duration} = \frac{103 - 98.5}{2 \times 102 \times 0.0025} = \frac{4.5}{0.51} = 8.82
$$

**Compare to non-callable bullet with same maturity:**
- Modified duration: 9.50 years

**Callable has lower effective duration (8.82 vs. 9.50) because call caps upside.**

### 3. OAS Duration


**Duration with respect to OAS changes:**

$$
\text{OAS Duration} = -\frac{1}{P} \frac{\partial P}{\partial \text{OAS}}
$$

**For most bonds: OAS duration ≈ Effective duration**

**But they differ when:**
1. OAS and rates not perfectly correlated
2. Embedded options present
3. Credit quality changes (duration shifts)

**Example:**

- Investment-grade bond: OAS duration = 6.8 years
- If OAS widens 50 bp: Price falls ≈ 3.4%

**High-yield bond: OAS duration often < Modified duration**
- Credit deterioration reduces duration (maturity shortens in default)
- Expected recovery pulls price toward recovery value

### 4. Spread Convexity


$$
\text{Convexity} = \frac{1}{P} \frac{\partial^2 P}{\partial s^2}
$$

**For corporate bonds:**

**Positive convexity (normal bonds):**
- Spreads widen 100 bp: Price falls 6.8%
- Spreads tighten 100 bp: Price rises 7.2%
- **Asymmetric benefit to investor**

**Negative convexity (callables near call price):**
- Spreads tighten → Price capped at call price
- Spreads widen → Full downside
- **Asymmetric harm to investor**

**Example: Callable bond near call price**

- Current price: $104, Call price: $105
- Spread tightens 50 bp: Price → $105 (capped!)
- Spread widens 50 bp: Price → $100.50
- **Negative convexity hurts investor**

---

## Credit Spread Payoff Analysis


### 1. Spread Change Impact on Returns


**Setup:**
- Corporate bond: Price $100, Duration 7.0, OAS 150 bp
- 1-year holding period
- Treasury yields unchanged

**Scenarios:**

| Spread Change | Price Impact | Coupon | Total Return | Annualized |
|---------------|-------------|--------|--------------|------------|
| -50 bp (tightening) | +3.5% | +5.5% | +9.0% | +9.0% |
| -25 bp | +1.75% | +5.5% | +7.25% | +7.25% |
| 0 bp (unchanged) | 0% | +5.5% | +5.5% | +5.5% |
| +25 bp | -1.75% | +5.5% | +3.75% | +3.75% |
| +50 bp (widening) | -3.5% | +5.5% | +2.0% | +2.0% |
| +100 bp | -7.0% | +5.5% | -1.5% | -1.5% |
| +200 bp (crisis) | -14.0% | +5.5% | -8.5% | -8.5% |

**Key observations:**

1. **Carry offsets moderate widening:**
   - Spreads can widen 50 bp before negative total return
   - 5.5% carry cushions against spread moves

2. **Tightening is highly profitable:**
   - 50 bp tightening → +9% return
   - Asymmetric upside vs. downside (until default)

3. **Crisis widening devastating:**
   - 200 bp widening → -8.5% return
   - Wipes out 1.5 years of carry

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/credit_spread_return_profile.png?raw=true" alt="credit_spread_return_profile" width="700">
</p>
**Figure 1:** Total return profile showing how credit spread changes impact returns, with carry providing cushion against moderate spread widening.

### 2. OAS vs. Z-spread in Callable Bond Returns


**Setup:**
- Two bonds, same issuer, same maturity (10-year)
- Bond A: Bullet, OAS 120 bp
- Bond B: Callable, OAS 120 bp, Z-spread 180 bp

**Scenario: Rates fall 100 bp (bullish for bonds)**

**Bond A (Bullet):**

| Component | Impact | Value |
|-----------|--------|-------|
| Duration gain | 7.0 × 1% | +7.0% |
| Carry | | +5.0% |
| **Total** | | **+12.0%** |

**Bond B (Callable):**

| Component | Impact | Value |
|-----------|--------|-------|
| Effective duration gain | 5.5 × 1% | +5.5% |
| Called at par | Lost future coupons | -1.5% |
| Carry | | +5.5% |
| **Total** | | **+9.5%** |

**Bond A outperformed by 2.5% due to no call risk.**

**Even though both had same OAS (120 bp), the bullet provided better returns in rally.**

**Lesson: OAS measures credit compensation, but option features still affect total returns.**

---

## Real-World Credit Spread Examples


### 1. Example 1: Investment Grade Spread Tightening (Winner)


**Setup:**

- **Date:** January 2025
- **Portfolio:** $500M BBB-rated corporate bonds
- **Average OAS:** 180 bp (75th percentile - wide)
- **Average duration:** 7.5 years
- **Strategy:** Buy and hold, expecting spread tightening

**Market environment:**
- Post-recession recovery beginning
- Corporate earnings improving
- Credit metrics strengthening
- Fed maintaining accommodative policy

**Entry analysis:**

| Metric | Current | 5-year Avg | Percentile |
|--------|---------|-----------|------------|
| BBB OAS | 180 bp | 145 bp | 75th |
| Default rate | 0.8% | 1.2% | 40th (lower is better) |
| Upgrade/downgrade ratio | 1.5x | 1.0x | Good |

**View:** Spreads are wide relative to fundamentals. Room for 30-40 bp tightening.

**Trade evolution (6 months):**

**Month 1-2:**
- Spreads stable at 180 bp
- Earning carry: +5.8% annualized
- **Monthly return:** +0.97%

**Month 3 (March):**
- Strong corporate earnings
- Credit metrics continue improving
- **Spreads tighten to 165 bp (-15 bp)**

| Component | Impact |
|-----------|--------|
| Spread tightening | 7.5 × 0.15% = +1.13% |
| Carry | +0.48% |
| **Total** | **+1.61%** |

**Month 4-5:**
- Continued strength
- Multiple upgrades in portfolio (BBB → A)
- **Spreads tighten to 150 bp (another -15 bp)**

| Component | 2-month Impact |
|-----------|----------------|
| Spread tightening | 7.5 × 0.15% = +1.13% |
| Carry | +0.96% |
| Upgrade benefit | +0.5% |
| **Total** | **+2.59%** |

**Month 6 (June):**
- Spreads stabilize at 145 bp
- Now at historical average (50th percentile)
- **No further tightening, just carry**

**6-month results:**

| Component | Contribution | Calculation |
|-----------|--------------|-------------|
| Carry | +2.90% | 5.8% annualized × 0.5 years |
| Spread tightening | +2.625% | (180-145) × 7.5 × 0.01 |
| Upgrades | +0.50% | Several BBB → A |
| **Total return** | **+6.025%** | |

**Annualized:** 12.05%

**Why it worked:**

1. **Entry at wide spreads (75th percentile):**
   - 180 bp OAS well above historical average
   - Mean reversion potential clear

2. **Fundamental support:**
   - Earnings growth
   - Credit metrics improving
   - No recession risk

3. **Tightening materialized:**
   - 35 bp tightening over 6 months
   - Generated +2.625% from spread alone

4. **Carry collection:**
   - 5.8% yield provided cushion
   - Would still be positive even without tightening

5. **Upgrades bonus:**
   - Several bonds upgraded BBB → A
   - Tightened more than index

**Risk management:**
- Position sized at 5% of fund
- Diversified across 30+ issuers
- No single-name risk
- Duration hedged (removed rate risk)

### 2. Example 2: OAS Arbitrage - Callable vs. Bullet (Winner)


**Setup:**

- **Company:** XYZ Corp (A-rated)
- **Trade:** Buy callable bond (cheap), sell bullet bond (rich)
- **Strategy:** Relative value within same issuer

**Bonds:**

**Bond A (Bullet):**
- 10-year maturity
- Price: $100.50
- YTM: 4.80%
- **OAS: 105 bp (30th percentile - rich)**

**Bond B (Callable @ $105):**
- 10-year maturity, callable in 3 years
- Price: $101.25
- YTM: 5.40%
- Z-spread: 165 bp
- **OAS: 115 bp (60th percentile - fair/slightly cheap)**

**Analysis:**

**OAS differential:** 115 - 105 = **10 bp**

**Historical norm:** Callable typically trades 0-5 bp wider in OAS than bullet

**Current: 10 bp wider → Callable is cheap OR bullet is rich**

**Trade:**
- Long $10M Bond B (callable) at OAS 115 bp
- Short $10M Bond A (bullet) at OAS 105 bp
- **Net investment:** ≈ $0 (matched long/short)
- **Target:** Convergence of OAS differential from 10 bp → 5 bp

**Evolution (3 months):**

**Month 1:**
- OAS differential unchanged at 10 bp
- Earning carry differential: (5.40% - 4.80%) = +0.60% annualized
- **Monthly P/L:** +$5,000

**Month 2:**
- Market re-rates callable bonds
- Callable Bond B: OAS tightens to 110 bp (-5 bp)
- Bullet Bond A: OAS unchanged at 105 bp

**P/L calculation:**

| Position | OAS Change | Duration | P/L |
|----------|-----------|----------|-----|
| Long callable | -5 bp | 6.5 | +$32,500 |
| Short bullet | 0 bp | 7.0 | $0 |
| **Net** | | | **+$32,500** |

**Month 3:**
- Differential continues converging
- Callable: 108 bp (-2 bp more)
- Bullet: 104 bp (-1 bp)
- **Differential now: 4 bp** (normalized!)

**Final P/L:**

| Component | P/L |
|-----------|-----|
| Spread convergence | +$45,000 |
| Carry differential | +$15,000 |
| **Total** | **+$60,000 (+0.60%)** |

**Closed trade at 4 bp differential (historical norm).**

**Why it worked:**

1. **Identified relative value:**
   - OAS differential abnormal (10 bp vs. 5 bp norm)
   - Callable bond undervalued relative to bullet

2. **Convergence catalyst:**
   - Market recognized mispricing
   - Callable OAS tightened more than bullet

3. **Positive carry:**
   - Callable had higher yield (5.40% vs. 4.80%)
   - Earned carry while waiting for convergence

4. **Hedged:**
   - Duration-matched positions
   - No directional interest rate bet
   - Pure relative value trade

### 3. Example 3: Financial Crisis Spread Blowout (Loser)


**Setup:**

- **Date:** August 2025
- **Portfolio:** $250M BBB-rated financial sector bonds
- **Average OAS:** 140 bp (40th percentile - fair value)
- **Duration:** 6.5 years
- **View:** Financials fundamentally sound, spreads stable

**Month 1 (August):**
- Normal conditions
- Spreads stable
- Earning carry
- **Return:** +0.46%

**Month 2 (September): The Shock**

**Event:** Regional bank failure announced
- Contagion fears
- Bank runs on social media
- Flight to quality

**Market reaction:**

- **Day 1:** Financial spreads +50 bp (140 → 190 bp)
- **Day 2:** Another +75 bp (190 → 265 bp)
- **Day 3:** Continued widening +60 bp (265 → 325 bp)

**Portfolio P/L (3 days):**

| Day | Spread Change | Price Impact | Cumulative Loss |
|-----|---------------|--------------|-----------------|
| 1 | +50 bp | -3.25% | -$8.125M |
| 2 | +75 bp | -4.875% | -$20.31M |
| 3 | +60 bp | -3.90% | -$30.06M |

**Total 3-day loss: -$30.06M (-12.0%)**

**Manager decisions:**

**Day 3:** Panic decision
- Sold 40% of portfolio ($100M) at 325 bp spreads
- **Realized loss:** -$12M
- Remaining position: $150M

**Mistake: Sold at the worst point!**

**Month 3 (October): Reversal**

- Government announces backstop for banks
- Contagion fears subside
- Spreads begin to normalize

**Spread retracement:**
- Week 1: 325 → 280 bp (-45 bp recovery)
- Week 2: 280 → 245 bp (-35 bp more)
- Week 3: 245 → 210 bp (-35 bp more)
- Week 4: 210 → 185 bp (-25 bp more)

**Final month spread: 185 bp (still 45 bp wider than start)**

**P/L for remaining $150M position:**

| Component | Impact |
|-----------|--------|
| Recovery (325 → 185 bp) | 6.5 × 1.40% = +9.1% |
| Carry | +0.65% |
| **Total** | **+9.75%** |

**Gain on $150M:** +$14.625M

**Total portfolio outcome:**

| Component | Amount |
|-----------|--------|
| Loss on $100M sold | -$12.0M (realized) |
| Gain on $150M held | +$14.625M |
| **Net** | **+$2.625M (+1.05%)** |

**BUT: If hadn't sold anything:**

**Hypothetical (held all $250M):**

| Component | Impact on $250M |
|-----------|-----------------|
| Carry (3 months) | +$3.19M |
| Peak drawdown (unrealized) | -$30.06M |
| Recovery (325 → 185 bp) | +$22.75M |
| **Net** | **-$4.12M (-1.65%)** |

**Wait, holding would have been worse?**

**Let's recalculate to end of year (6 months total):**

**Months 4-6: Continued recovery**
- Spreads: 185 → 155 bp (normalized)
- Additional gain: 6.5 × 0.30% = +1.95%
- Carry: +3 months worth

**Full 6-month if held entire portfolio:**

| Period | P/L |
|--------|-----|
| Month 1 | +0.46% |
| Month 2 (crisis) | -12.0% |
| Month 3 (recovery) | +9.75% |
| Months 4-6 (normalization) | +4.85% |
| **Total** | **+3.06%** |

**Actual result (with panic selling):**

| Component | P/L |
|-----------|-----|
| $100M sold at loss | -$12.0M |
| $150M held | +$23.2M |
| $100M reinvested at 185 bp | +$5.8M |
| **Total** | **+$17.0M (+6.8%)** |

**Panic selling actually helped!** (Reinvested proceeds at wider spreads)

**But this required:**
1. Lucky timing (sold near widest)
2. Courage to reinvest at 185 bp
3. Didn't happen by skill, happened by accident

**Lessons:**

1. **Financial spreads can gap violently:**
   - 140 → 325 bp in 3 days (unprecedented)
   - Contagion risk is real
   - Sector concentration dangerous

2. **Mark-to-market pain is brutal:**
   - -12% in 3 days tests nerves
   - Many managers forced to sell (margin, redemptions)

3. **Crisis creates opportunity:**
   - If can hold through, recovery often sharp
   - But not everyone can hold (leverage, liquidity)

4. **Diversification crucial:**
   - 100% financial concentration = disaster
   - Should have been 20-30% max

### 4. Example 4: OAS Misanalysis - Ignored Fundamentals (Loser)


**Setup:**

- **Bond:** ABC Corp 10-year (BBB-rated)
- **OAS:** 240 bp (95th percentile - very wide!)
- **Z-spread:** 245 bp
- **Historical OAS:** 150-170 bp average

**Analyst view:**
- "240 bp is way above historical average!"
- "Clear mean reversion trade"
- "Buy at 240 bp, target 170 bp tightening"
- **IGNORED: Deteriorating fundamentals**

**What analyst missed:**

| Metric | Current | 1 Year Ago | Trend |
|--------|---------|-----------|-------|
| Leverage | 5.5x | 3.8x | Worsening |
| Interest coverage | 2.1x | 3.5x | Worsening |
| Free cash flow | -$200M | +$150M | Negative |
| Rating outlook | Negative | Stable | Downgrade risk |

**Trade:**
- Bought $20M at OAS 240 bp
- Expected mean reversion to 170 bp
- **Duration: 8.0 years**

**Evolution:**

**Month 1:**
- Spreads stable at 240 bp
- Carry: +0.6%
- **Return: +0.6%**

**Month 2:**
- Rating agency announces review for downgrade
- **Spreads widen to 280 bp (+40 bp)**
- Loss: 8.0 × 0.40% = -3.2%
- **Net: -2.6%**

**Month 3:**
- Downgraded BBB → BB (high yield!)
- **Spreads gap to 450 bp (+170 bp)**
- Loss: 8.0 × 1.70% = -13.6%
- **Net: -16.2% cumulative**

**Final outcome:**
- Sold at 450 bp to limit further losses
- **Total loss: -$3.24M (-16.2%)**

**What went wrong:**

1. **Mechanical OAS analysis:**
   - Looked at percentile, ignored fundamentals
   - Wide spreads were WARNING, not opportunity
   - Market was correctly pricing deterioration

2. **Ignored credit metrics:**
   - Leverage rising (5.5x is high for BBB)
   - Cash flow negative
   - Rating downgrade imminent (outlook negative)

3. **Mean reversion fallacy:**
   - Assumed spreads would revert to 170 bp
   - But company quality had deteriorated
   - **New equilibrium was 400-500 bp (BB-rated)**

4. **Fallen angel risk:**
   - Didn't anticipate downgrade to high yield
   - HY spreads are 300-500 bp wider than IG
   - Massive re-rating when crosses threshold

**Correct approach:**

**Should have analyzed:**

$$
\text{Fair OAS} = \text{Base BBB spread} + \text{Leverage adjustment} + \text{Sector adjustment} + \text{Downgrade risk}
$$

$$
\text{Fair OAS} = 140 + 50 + 20 + 80 = 290 \text{ bp}
$$

**Actual OAS: 240 bp**
**Fair OAS: 290 bp**
**Conclusion: Bond was RICH at 240 bp, not cheap!**

**Lesson: OAS percentiles are just starting point. Must analyze fundamentals!**

---

## Best Case Scenario


### 1. The Perfect Credit Cycle Trade


**Setup:**

- **Date:** Q1 2024 (Post-recession trough)
- **Portfolio Manager:** Credit hedge fund
- **Capital:** $1 billion
- **Strategy:** Overweight credit at cycle trough

**Market environment:**
- Recession just ended
- Default rates peaked at 3.5%, now falling
- BBB spreads at 95th percentile (240 bp OAS)
- High yield at 98th percentile (650 bp OAS)
- Fed beginning to ease (bullish for credit)

**Portfolio construction:**

**70% Investment Grade ($700M):**
- BBB-rated corporates
- Average OAS: 235 bp (95th percentile)
- Average duration: 7.2 years
- Sectors: Industrials, Consumer, Technology

**30% High Yield ($300M):**
- BB-rated (top of HY)
- Average OAS: 580 bp (97th percentile)
- Average duration: 4.5 years
- Focused on fallen angels (recent downgrades from IG)

**Historical analysis:**

| Metric | Current | Trough Avg | Peak Avg | Percentile |
|--------|---------|-----------|----------|------------|
| BBB OAS | 235 bp | 240 bp | 95 bp | 95th |
| HY OAS | 580 bp | 600 bp | 280 bp | 97th |
| Default rate | 3.2% | 3.5% | 0.8% | Falling |
| Upgrade/downgrade | 0.6x | 0.5x | 2.0x | Improving |

**View:** Credit at widest spreads in 10 years. Recovery beginning. Room for 100+ bp tightening in IG, 250+ bp in HY.

**Year 1 (2024): Early Recovery**

**Q1:**
- Spreads stable (digesting recession)
- Default rate: 3.2% → 2.9%
- Upgrade/downgrade: 0.6x → 0.8x
- **Quarterly return:** +2.1% (mostly carry)

**Q2:**
- Economic data strengthening
- Fed cuts rates 25 bp (supportive)
- **BBB OAS: 235 → 215 bp (-20 bp tightening)**
- **HY OAS: 580 → 540 bp (-40 bp)**

**Q2 P/L:**

| Portfolio | Spread Change | Duration | P/L | Carry | Total |
|-----------|---------------|----------|-----|-------|-------|
| IG ($700M) | -20 bp | 7.2 | +1.44% | +1.5% | +2.94% |
| HY ($300M) | -40 bp | 4.5 | +1.80% | +3.8% | +5.60% |
| **Weighted avg** | | | | | **+3.7%** |

**Q3-Q4:**
- Continued strength
- Multiple upgrades (BB → BBB)
- **IG OAS: 215 → 185 bp (-30 bp)**
- **HY OAS: 540 → 480 bp (-60 bp)**

**Q3-Q4 P/L (6 months):**

| Portfolio | Tightening | Duration | P/L | Carry | Total |
|-----------|-----------|----------|-----|-------|-------|
| IG | -30 bp | 7.2 | +2.16% | +3.0% | +5.16% |
| HY | -60 bp | 4.5 | +2.70% | +7.6% | +10.3% |
| **Weighted** | | | | | **+6.9%** |

**Year 1 total return: +14.8%**

**Year 2 (2025): Mid-Cycle**

**Environment:**
- Recovery well established
- Default rate: 1.8% (normalized)
- Upgrades exceeding downgrades 2:1

**Continued tightening:**
- **IG OAS: 185 → 140 bp (-45 bp over year)**
- **HY OAS: 480 → 380 bp (-100 bp over year)**

**Year 2 P/L:**

| Portfolio | Tightening | Duration | P/L | Carry | Total |
|-----------|-----------|----------|-----|-------|-------|
| IG | -45 bp | 7.0 | +3.15% | +6.0% | +9.15% |
| HY | -100 bp | 4.3 | +4.30% | +15.2% | +19.5% |
| **Weighted** | | | | | **+12.2%** |

**Year 3 (2026): Late Cycle Positioning**

**Q1-Q2:**
- Spreads approaching tight end of range
- **IG OAS: 140 → 120 bp** (40th percentile now)
- **HY OAS: 380 → 340 bp** (45th percentile)
- Time to reduce exposure

**Q1-Q2 P/L:**

| Component | Return |
|-----------|--------|
| Spread tightening | +2.1% |
| Carry | +3.2% |
| **Total** | **+5.3%** |

**Q3: Exit Strategy**

**Action: Reduce credit overweight**
- Sell 50% of BBB exposure ($350M)
- Sell 70% of HY exposure ($210M)
- Lock in profits
- Redeploy to lower-risk assets

**Locks in:**
- IG gains: $350M at avg +35% = +$122.5M
- HY gains: $210M at avg +48% = +$100.8M

**3-year total performance:**

**Initial capital:** $1,000M

| Year | IG Return | HY Return | Blended | Cumulative |
|------|-----------|-----------|---------|------------|
| 2024 | +12.8% | +20.3% | +14.8% | +14.8% |
| 2025 | +9.15% | +19.5% | +12.2% | +28.8% |
| 2026 (H1) | +4.5% | +7.8% | +5.3% | +35.6% |

**Final capital:** $1,356M
**Total return:** +35.6% over 2.5 years
**Annualized:** 12.8%
**Sharpe ratio:** 1.85

**Comparison to benchmarks:**

| Strategy | Total Return | Annualized | Sharpe |
|----------|--------------|------------|--------|
| **Our credit overweight** | **+35.6%** | **12.8%** | **1.85** |
| IG index | +18.2% | 6.9% | 0.95 |
| HY index | +27.3% | 10.2% | 1.22 |
| 60/40 stocks/bonds | +22.1% | 8.3% | 0.78 |

**Why this was best case:**

1. **Perfect entry timing:**
   - Bought at 95th percentile spreads
   - Maximum room for tightening
   - Cycle trough identification

2. **Correct macro view:**
   - Recession ending (default rate peaked)
   - Fed easing (supportive for credit)
   - Economic recovery beginning

3. **Full tightening captured:**
   - IG: 240 → 120 bp (120 bp tightening)
   - HY: 580 → 340 bp (240 bp tightening)
   - Both exceeded expectations

4. **Upgrades bonus:**
   - Multiple fallen angels upgraded back to IG
   - Upgrade boost: +3-5% per upgrade

5. **Disciplined exit:**
   - Reduced exposure at 40-45th percentile
   - Didn't get greedy at tight spreads
   - Locked in 3 years of gains

6. **Carry collection:**
   - IG: 6% avg yield × 2.5 years = 15% carry
   - HY: 12% avg yield × 2.5 years = 30% carry
   - Total return = tightening + carry

**Attribution:**

| Component | Contribution |
|-----------|--------------|
| Spread tightening | +18.5% |
| Carry collection | +15.8% |
| Upgrades | +1.3% |
| **Total** | **+35.6%** |

---

## Worst Case Scenario


### 1. The Credit Crisis Spread Explosion


**Setup:**

- **Date:** Q2 2025
- **Portfolio:** $500M corporate bond fund
- **Allocation:** 100% investment-grade corporate (average BBB+)
- **Average OAS:** 155 bp (50th percentile - fair value)
- **Duration:** 7.8 years
- **Manager view:** "Fundamentals stable, economy strong, maintain full exposure"

**Month 1 (April): Warning Signs Ignored**

**Events:**
- Corporate earnings miss expectations (multiple sectors)
- Leverage ratios ticking up
- Some analysts warning of cycle peak

**Spread changes:**
- **OAS: 155 → 170 bp (+15 bp)**

**Manager reaction:**
- "Just temporary volatility"
- "Fundamentals still okay"
- **No action taken** (Mistake #1)

**P/L:**
- Spread widening: -7.8 × 0.15% = -1.17%
- Carry: +0.43%
- **Net: -0.74%**

**Month 2 (May): Acceleration**

**Events:**
- Major industrial company announces bankruptcy
- Contagion fears
- Credit market deleveraging begins

**Spread changes:**
- **OAS: 170 → 225 bp (+55 bp)**

**P/L:**
- Spread widening: -7.8 × 0.55% = -4.29%
- Carry: +0.43%
- **Net: -3.86%**
- **Cumulative: -4.6%**

**Manager reaction:**
- "This is overdone, time to add!"
- **Bought another $100M at 225 bp** (Mistake #2)
- New portfolio: $600M
- New average OAS: 168 bp (weighted)

**Month 3 (June): The Crisis**

**Cascading events:**

**Week 1:**
- Rating agencies downgrade multiple issuers
- Wave of fallen angels (BBB → BB)
- Mutual fund redemptions spike
- **OAS: 225 → 290 bp (+65 bp)**

| Position | Size | Spread Change | P/L |
|----------|------|---------------|-----|
| Original $500M | $500M | +135 bp total | -$52.65M |
| New $100M | $100M | +65 bp | -$5.07M |
| **Total** | **$600M** | | **-$57.72M (-9.6%)** |

**Week 2:**
- Liquidity crisis
- Bid-ask spreads blow out
- Forced selling accelerates
- **OAS: 290 → 380 bp (+90 bp)**

**Additional loss:** -7.8 × 0.90% × $600M = -$42.12M
**Cumulative: -$99.84M (-16.6%)**

**Week 3: Margin Calls**

**Portfolio marked down:**
- Original value: $600M
- Current value: $500M
- **Unrealized loss: $100M**

**Fund structure:**
- 20% leverage via repo
- Repo lender demands margin
- **Must post additional $50M collateral or reduce positions**

**Manager decision: Forced selling**
- Liquidated $200M at 380 bp spreads
- **Realized loss:** $200M × -16.6% = -$33.2M
- Remaining position: $400M

**Week 4: Capitulation**

**More redemptions:**
- Investors panic, redeem $150M
- Must sell more bonds into illiquid market
- **Spreads now: 380 → 420 bp** (everyone selling)

**Additional forced sale:**
- Sold $150M at 420 bp
- **Realized loss:** $150M × -19.5% = -$29.25M

**Remaining portfolio: $250M**

**Month 3 total damage:**

| Component | Amount |
|-----------|--------|
| Mark-to-market loss (Week 1-2) | -$99.84M |
| Forced sales (Week 3) | -$33.2M |
| Redemption sales (Week 4) | -$29.25M |
| **Month 3 total** | **-$162.29M** |

**Cumulative loss: -$162.29M (-27.0%)**

**Month 4 (July): Aftermath**

**Remaining portfolio:**
- Size: $250M (down from $600M peak)
- Average OAS: 420 bp (now 99th percentile)
- **Ironically, now attractively valued!**

**But:**
- Fund constrained by redemptions
- Can't add to positions
- Must maintain high cash (30%) for future redemptions

**Recovery begins:**
- Government announces support measures
- **Spreads: 420 → 360 bp (-60 bp)**

**Gain on $250M:** +7.8 × 0.60% × $250M = +$11.7M

**But redemptions continue:**
- Another $80M redeemed
- **More forced selling**

**Net Month 4:** +$11.7M - $15.6M = -$3.9M

**6-month total outcome:**

| Period | Event | P/L |
|--------|-------|-----|
| Month 1 | Initial widening (+15 bp) | -$3.7M |
| Month 2 | Acceleration (+55 bp) | -$19.3M |
| Month 2 | Bought more (mistake) | - |
| Month 3 Week 1-2 | Crisis (+155 bp) | -$99.84M |
| Month 3 Week 3 | Forced sale ($200M) | -$33.2M |
| Month 3 Week 4 | Redemption sale ($150M) | -$29.25M |
| Month 4 | Recovery +$11.7M, redemptions -$15.6M | -$3.9M |
| **Total** | | **-$188.19M** |

**On original $500M:** -37.6%
**On peak $600M:** -31.4%

**Final fund status:**
- Started: $500M
- Peak (after adding): $600M
- Ending: $311.81M
- **Destruction: -37.6%**

**Comparison if sold early:**

**Hypothetical: Sold everything at 170 bp in Month 1**
- Loss: -$5.85M (-1.17%)
- **vs. Actual: -$188.19M (-37.6%)**
- **Difference: $182.34M saved!**

**What went wrong:**

1. **Ignored early warning (Month 1):**
   - +15 bp widening was signal
   - Should have reduced exposure
   - Instead held for "mean reversion"

2. **Averaged down (Month 2):**
   - Bought $100M more at 225 bp
   - "Catching falling knife"
   - Made problem 20% larger

3. **Overleveraged:**
   - 20% repo leverage
   - Forced selling at worst prices
   - Margin calls compounded losses

4. **No stop loss:**
   - No predetermined exit point
   - Let losses run to -16% before selling
   - Should have sold at -5% to -10%

5. **Liquidity mismatch:**
   - Daily redemption fund
   - Illiquid corporate bonds
   - **Classic structure problem**

6. **Concentration:**
   - 100% corporate credit
   - No diversification (Treasuries, cash)
   - Single risk factor destroyed fund

**How it should have been managed:**

**Month 1 (OAS 155 → 170 bp):**
- **Action:** Reduce exposure by 30%
- Sell $150M, raise cash to 30%
- **Result:** -0.8% loss, but positioned defensively

**Month 2 (OAS 170 → 225 bp):**
- **Action:** With 30% cash, weather the storm
- Don't add (no averaging down)
- **Result:** -2.7% on remaining 70%, total -3.5%

**Month 3 (Crisis):**
- With cash buffer, can meet redemptions
- No forced selling
- Hold remaining positions through crisis
- **Result:** -10% to -15% (vs. -37.6% actual)

**Month 4 (Recovery):**
- Still have positions to benefit from recovery
- Can redeploy cash into 420 bp spreads
- **Result:** Recover to -5% to -8% total**

**Proper risk management:**

$$
\text{Maximum OAS widening tolerance} = \frac{\text{Cash Buffer}}{\text{Duration} \times \text{Portfolio}}
$$

$$
\text{Example: } \frac{30\%}{7.8 \times 70\%} = 5.5\% \text{ or } 550 \text{ bp widening capacity}
$$

**With proper cash buffer, could withstand entire crisis without forced selling.**

**Final lesson:** The worst losses in credit come not from spread widening alone, but from forced selling during widening. Cash is king in credit crisis.

---

## What to Remember


### 1. Core Concept


**Credit spreads measure compensation for credit risk:**

$$
\text{Credit Spread} = \text{YTM}_{\text{corporate}} - \text{YTM}_{\text{risk-free}}
$$

**OAS refines this by removing embedded option value:**

$$
\text{OAS} = \text{Z-spread} - \text{Option Value}
$$

- Wider spreads = higher compensation or deteriorating credit
- OAS enables apples-to-apples comparison across bonds
- Spread changes drive majority of corporate bond returns
- Spreads decompose into default risk, liquidity, tax, and systemic risk

### 2. The Spread Hierarchy


**From simplest to most sophisticated:**

1. **G-spread (Nominal):** YTM difference vs. Treasury
2. **Z-spread:** Constant spread over spot curve
3. **OAS:** Z-spread minus option value
4. **I-spread:** Spread over swap curve
5. **ASW spread:** Asset swap spread over LIBOR/SOFR

**For analysis:**
- Bullet bonds: Use Z-spread
- Callable/putable: Use OAS
- International: Consider I-spread
- Relative value: Compare OAS

### 3. Key Equations


**Z-spread calculation:**

$$
P = \sum_{t=1}^{n} \frac{CF_t}{(1 + r_t + Z)^t}
$$

**OAS relationship:**

$$
\text{Z-spread} = \text{OAS} + \text{Option Cost}
$$

**Expected loss:**

$$
\text{Expected Loss} = \text{PD} \times \text{LGD}
$$

**Spread duration:**

$$
\text{Spread DV01} = -\frac{\partial P}{\partial s} \times 0.0001
$$

**Total return:**

$$
R = \text{Carry} + (\Delta S \times \text{Spread Duration}) + (\Delta r \times \text{Rate Duration})
$$

### 4. Spread Analysis Framework


**Entry checklist:**

1. **OAS percentile check:**
   - [ ] Calculate current OAS
   - [ ] Compare to historical range
   - [ ] Identify percentile (1-100)

2. **Fundamental analysis:**
   - [ ] Leverage ratio acceptable
   - [ ] Interest coverage adequate
   - [ ] Free cash flow positive
   - [ ] No imminent downgrade risk

3. **Relative value:**
   - [ ] OAS vs. peers in sector
   - [ ] OAS vs. same rating class
   - [ ] OAS vs. historical norm

4. **Technical factors:**
   - [ ] Liquidity adequate (bid-ask <0.25 pts)
   - [ ] No forced sellers in market
   - [ ] Supply/demand balanced

### 5. Position Sizing


**Conservative approach:**

$$
\text{Position Size} = \min\left(5\% \text{ of portfolio}, \frac{2\% \text{ of portfolio}}{\text{Spread Duration}}\right)
$$

**Example:**
- Portfolio: $100M
- Bond spread duration: 7.0
- Max position: min(5%, 2%/7.0) = min($5M, $0.286M) = $286K

**Or if spread duration low:**
- Spread duration: 3.0
- Max position: min($5M, $0.67M) = $0.67M

### 6. Monitoring Rules


**Daily:**
- Mark positions
- Check spread changes >10 bp
- Monitor liquidity (bid-ask spreads)

**Weekly:**
- Calculate portfolio OAS
- Compare to benchmark
- Check rating outlooks

**Monthly:**
- Full fundamental review
- Rebalance if OAS percentile shifted >20 points
- Review diversification

### 7. Exit Rules


**Sell signals:**

1. **Fundamental deterioration:**
   - Leverage increasing
   - Coverage decreasing
   - Negative outlook from agencies
   - **Exit before downgrade**

2. **Spread tightening:**
   - OAS reaches <30th percentile
   - Below historical average
   - Limited upside remaining

3. **Stop loss:**
   - Position down >10%
   - OAS widened >100 bp from entry
   - Fundamental view violated

4. **Liquidity concerns:**
   - Bid-ask >0.50 points
   - Can't trade full size
   - Market depth evaporating

### 8. Common Mistakes to Avoid


1. **Using G-spread instead of OAS** for callables
   - Distorted by option value
   - Not comparable across bonds

2. **Ignoring fundamentals** (only looking at percentiles)
   - Wide spreads may be justified
   - Cheap can get cheaper

3. **Overleveraging credit exposure**
   - Forced selling magnifies losses
   - Maintain 20-30% cash buffer

4. **Averaging down** on widening spreads
   - Catching falling knife
   - Wait for stabilization

5. **Sector concentration**
   - Single sector can blow out
   - Diversify across 5+ sectors

6. **No stop loss discipline**
   - Let winners run, cut losers
   - Exit at -10% maximum

7. **Liquidity mismatch** (daily redemptions, illiquid bonds)
   - Recipe for forced selling
   - Match liquidity profiles

8. **Chasing yield** without credit analysis
   - High yield may signal distress
   - Analyze why spread is wide

### 9. Performance Expectations


**Investment-grade corporates:**

| Scenario | OAS Change | Return | Frequency |
|----------|-----------|--------|-----------|
| Best case | -50 bp | +9% | 10% |
| Good | -25 bp | +6% | 25% |
| Base | 0 bp | +4.5% | 40% |
| Widening | +25 bp | +2% | 20% |
| Crisis | +100 bp | -5% | 5% |

**Expected return:** 4.5-5.5% annually

**High-yield:**

| Scenario | OAS Change | Return | Frequency |
|----------|-----------|--------|-----------|
| Best case | -100 bp | +15% | 10% |
| Good | -50 bp | +10% | 25% |
| Base | 0 bp | +7% | 35% |
| Widening | +50 bp | +2% | 20% |
| Default | -100% | -100% | 10% |

**Expected return:** 6-8% annually (after defaults)

### 10. Spread Decomposition (Typical BBB Corporate)


| Component | Basis Points | % of Total |
|-----------|--------------|------------|
| Expected loss | 15 bp | 10% |
| Liquidity premium | 25 bp | 17% |
| Tax premium | 15 bp | 10% |
| Systemic risk | 45 bp | 30% |
| **Fair spread** | **100 bp** | **67%** |
| Actual spread | 150 bp | 100% |
| **Alpha** | **+50 bp** | **33%** |

### 11. OAS vs. Z-spread (When to Use)


| Bond Type | Metric | Reason |
|-----------|--------|--------|
| Bullet bond | Z-spread | No embedded options |
| Callable bond | OAS | Remove call option value |
| Putable bond | OAS | Remove put option value |
| Sinkable bond | OAS | Account for sinking fund |
| MBS/ABS | OAS | Prepayment optionality |
| Convertible | OAS | Conversion option |

### 12. Comparison to Other Assets


**Credit spreads vs. equities:**

| Credit (IG) | Equities |
|-------------|----------|
| 4-6% expected return | 8-10% expected return |
| Lower volatility (3-5%) | Higher volatility (15-20%) |
| Senior in capital structure | Junior (residual claim) |
| Limited upside (par) | Unlimited upside |
| Contractual cash flows | Discretionary dividends |

**Better for:** Income, capital preservation, lower volatility

### 13. Your Learning Path


**Phase 1 (Months 1-3): Foundations**
- Calculate G-spread, Z-spread manually
- Understand OAS concept
- Compare bonds with different structures
- Build spread database

**Phase 2 (Months 4-6): Analysis**
- Fundamental credit analysis
- Spread percentile tracking
- Sector rotation based on spreads
- Historical spread patterns

**Phase 3 (Months 7-12): Trading**
- Relative value trades
- Spread tightening/widening bets
- Callable vs. bullet arbitrage
- Portfolio construction

**Phase 4 (Year 2+): Advanced**
- OAS modeling for complex structures
- Credit derivatives (CDS)
- Capital structure arbitrage
- Systematic credit strategies

### 14. Final Wisdom


> "Credit spreads are the market's collective assessment of risk. A wide spread tells you the market is worried—your job is to determine if that worry is justified or overdone. OAS strips away the noise of embedded options to reveal the true credit compensation. The investor who understands spread decomposition—default risk, liquidity, tax, systemic risk—can identify where the market is mispricing risk. But never forget: a spread can always go wider. The widest spreads often precede defaults, not mean reversion. Cheap can get cheaper when fundamentals deteriorate. Always know why a spread is wide before calling it an opportunity."

**Keys to success:**

1. **Use OAS for callable/putable bonds** (never just Z-spread)
2. **Check fundamentals, not just percentiles** (wide may be justified)
3. **Diversify across sectors** (don't concentrate)
4. **Maintain cash buffer** (avoid forced selling)
5. **Set stop losses** (exit at -10%)
6. **Scale into positions** (don't rush)
7. **Understand spread drivers** (default, liquidity, tax, systemic)
8. **Monitor rating outlooks** (exit before downgrade)

**Most critical rule:** 

$$
\text{Wide spreads} + \text{Strong fundamentals} = \text{Opportunity}
$$

$$
\text{Wide spreads} + \text{Weak fundamentals} = \text{Value trap}
$$

Always know which situation you're in. The market is usually smarter than you think. When everyone else is selling and spreads are blowing out, ask yourself: "What do they know that I don't?" Sometimes the answer is "nothing, it's panic." Sometimes the answer is "everything, it's about to default." Learning to tell the difference is the art of credit investing. 🎯📊

