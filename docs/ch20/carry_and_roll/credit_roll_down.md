# Roll-Down in Credit Curves


**Roll-down** in credit curves is the phenomenon where bonds gain value over time as they "roll down" the credit spread curve toward shorter maturities, providing positive returns even when credit spreads remain unchanged, creating a predictable source of excess return for investors who position strategically along upward-sloping credit curves.

---

## The Core Insight


**The fundamental idea:**

- Credit curves typically slope upward (longer maturity = wider spread)
- As time passes, bond's maturity shortens (rolls down curve)
- If curve unchanged: bond moves to lower spread (higher price)
- This creates mechanical price appreciation (roll-down return)
- Separate from carry and spread changes
- Most powerful when curve is steep
- Enhanced by buying longer maturity and holding
- Can be systematically harvested over time

**The key equations:**

**Total return decomposition:**

$$
R_{\text{total}} = \underbrace{R_{\text{carry}}}_{\text{Coupon income}} + \underbrace{R_{\text{roll}}}_{\text{Pull to par}} + \underbrace{R_{\text{roll-down}}}_{\text{Curve effect}} + \underbrace{R_{\text{spread}}}_{\text{Spread change}} + \underbrace{R_{\text{rates}}}_{\text{Interest rate}}
$$

**Roll-down return:**

$$
R_{\text{roll-down}} = \Delta P = (S_t - S_{t+\Delta t}) \times \text{Spread Duration}
$$

Where:
- $S_t$ = Spread at current maturity
- $S_{t+\Delta t}$ = Spread at shorter maturity (after time passes)

**Example:** 
- 5-year corporate: Spread 150 bp
- 4-year point on curve: Spread 130 bp
- Over 1 year: Bond rolls from 5y → 4y point
- Roll-down: (150 - 130) × 4.2 duration = **+0.84%**

**You're essentially asking: "If I buy a bond further out the credit curve and credit spreads remain exactly unchanged, how much price appreciation will I capture as the bond ages and its spread naturally tightens by rolling down to shorter maturity points on the curve?"**

---

## What is Credit Curve Roll-Down?


**Before implementing roll-down strategies, understand the mechanics:**

### 1. The Credit Spread Curve


**Definition:**

The credit spread curve plots the relationship between credit spreads and time to maturity for a single issuer or rating category.

$$
S(T) = \text{Credit Spread at maturity } T
$$

**Typical shapes:**

**1. Upward Sloping (Normal):**
- Most common (80-90% of the time)
- Longer maturity = wider spread
- Compensation for greater uncertainty over time

**Example (BBB-rated industrial):**

| Maturity | Spread | Interpretation |
|----------|--------|----------------|
| 2-year | 90 bp | Short-term relatively safe |
| 3-year | 105 bp | |
| 5-year | 130 bp | |
| 7-year | 155 bp | |
| 10-year | 180 bp | Long-term uncertainty |
| 30-year | 220 bp | Maximum uncertainty premium |

**Slope:** 220 - 90 = 130 bp over 28 years

**2. Flat Curve:**
- All maturities same spread
- Rare, transitional state
- No roll-down benefit

**3. Inverted (Downward Sloping):**
- Shorter maturity wider than longer
- Distressed credits (near-term default risk)
- Roll-down is NEGATIVE (hurts returns)

**Example (distressed CCC):**

| Maturity | Spread | Interpretation |
|----------|--------|----------------|
| 1-year | 800 bp | Imminent default risk |
| 3-year | 650 bp | If survives, recovers |
| 5-year | 580 bp | Long-term worth more (survival assumption) |

**Inverted by 220 bp!**

### 2. Roll-Down Mechanics


**The process:**

**Day 0:**
- Buy 5-year bond at spread $S_5 = 150$ bp
- Price: $P_0$
- Duration: 4.5 years

**1 Year Later (Day 365):**
- Bond is now 4-year maturity
- **If curve unchanged:** spread at 4y point = $S_4 = 130$ bp
- New price: $P_1$ (higher because spread tightened)

**Roll-down gain:**

$$
\text{Roll-down} = (S_5 - S_4) \times D \times P
$$

$$
= (150 - 130) \times 4.2 \times \$100 = \$0.84 \text{ or } 0.84\%
$$

**This is pure mechanical gain from curve shape!**

**Comparison to static spread:**

**Scenario A: Spreads unchanged (curve parallel shift 0 bp)**

| Component | Return |
|-----------|--------|
| Carry (5% coupon) | +5.0% |
| Roll-down (20 bp tightening) | +0.84% |
| Spread change | 0% |
| **Total** | **+5.84%** |

**Scenario B: Spreads widened 20 bp (curve shifts up)**

| Component | Return |
|-----------|--------|
| Carry | +5.0% |
| Roll-down | +0.84% |
| Spread change (20 bp wider) | -0.84% |
| **Total** | **+5.0%** |

**Roll-down offset spread widening!**

### 3. Roll vs. Roll-Down


**Two distinct concepts often confused:**

**1. Roll (Pull-to-Par):**

$$
\text{Roll} = \frac{\text{Par} - \text{Price}}{T}
$$

- All bonds converge to par at maturity
- Premium bonds ($P > 100$) → lose value
- Discount bonds ($P < 100$) → gain value
- Independent of credit curve shape

**Example:**
- Bond price: $102
- Maturity: 5 years
- Annual roll: $(100 - 102) / 5 = -0.4\%$ annually

**2. Roll-Down (Curve Effect):**

$$
\text{Roll-down} = \Delta S \times D
$$

- Due to credit curve slope
- Depends on curve shape
- Positive for upward-sloping curves
- Can be large (50-100+ bp for steep curves)

**Example:**
- 5y spread: 150 bp → 4y spread: 130 bp
- Roll-down: $20 \times 4.2 = +0.84\%$

**Combined effect:**

$$
\text{Total Price Change} = \text{Roll (pull-to-par)} + \text{Roll-down (curve)} + \text{Spread Change}
$$

**Example:**
- Roll: -0.4% (from $102 → $100)
- Roll-down: +0.84% (from curve)
- Spread change: 0%
- **Net: +0.44%** (in addition to carry)

### 4. Why Credit Curves Slope Upward


**Economic reasons:**

**1. Term Structure of Default Risk:**

$$
\text{PD}_{0-T} = 1 - e^{-\lambda T}
$$

Where $\lambda$ = constant hazard rate.

**Cumulative default probability increases with time:**
- 1-year PD: 0.5%
- 5-year cumulative PD: 2.4%
- 10-year cumulative PD: 4.7%

**Longer maturity = higher default risk = wider spread.**

**2. Uncertainty Premium:**

- Future is more uncertain than present
- Company fundamentals can deteriorate
- Business cycles, technology changes
- **Investors demand premium for uncertainty**

**3. Liquidity Premium:**

- Longer bonds less liquid
- Harder to sell in stress
- Wider bid-ask spreads
- **Investors demand compensation**

**4. Supply/Demand:**

- Corporations prefer long-term debt (lower rollover risk)
- Investors prefer short-term (lower duration)
- **Imbalance drives spreads wider at long end**

**Theoretical relationship:**

$$
S(T) = \text{Base Spread} + \alpha \times \sqrt{T}
$$

Where $\alpha$ captures risk premium per $\sqrt{T}$.

**This square root relationship creates upward slope that flattens at long maturities.**

---

## Economic Interpretation: Roll-Down as Risk Premium Harvesting


**Understanding what you're really earning:**

### 1. Roll-Down as Compensation for Risks


**The roll-down return compensates for:**

**1. Taking longer maturity risk:**

- Buy 10-year instead of 2-year
- Accept more duration risk
- Spread can widen more (10y more volatile than 2y)
- **Roll-down is your compensation**

**2. Credit deterioration risk:**

- Over 10 years, company can deteriorate
- Rating downgrade possible
- Default risk higher
- **Roll-down compensates for this possibility**

**3. Liquidity risk:**

- 10-year less liquid than 2-year
- Harder to sell in stress
- Wider bid-ask
- **Roll-down is liquidity premium**

**Decomposition:**

$$
\text{Roll-down} = \underbrace{\text{Default Risk Premium}}_{\text{Term structure}} + \underbrace{\text{Uncertainty Premium}}_{\text{Volatility}} + \underbrace{\text{Liquidity Premium}}_{\text{Trading costs}}
$$

**Example (BBB 10-year vs 2-year):**

| Component | Basis Points |
|-----------|--------------|
| Default risk (8 years extra) | 40 bp |
| Uncertainty premium | 30 bp |
| Liquidity premium | 20 bp |
| **Total 10y-2y slope** | **90 bp** |

**If you buy 10y and hold 8 years:**
- Roll down from 10y → 2y captures 90 bp
- Annual: 90 / 8 = 11.25 bp/year
- **This is your "harvest" for taking the risks**

### 2. Roll-Down vs. Carry


**Both are predictable returns, but different:**

**Carry:**

$$
\text{Carry} = \frac{\text{Coupon}}{\text{Price}}
$$

- Income from coupon payments
- Realized in cash
- Independent of curve shape
- Accrues linearly over time

**Roll-Down:**

$$
\text{Roll-down} = \text{Spread Tightening from Aging}
$$

- Mark-to-market gain from curve
- Unrealized (until sold or matures)
- Depends on curve slope
- Can reverse if curve steepens

**Combined "total carry":**

$$
\text{Total Carry} = \text{Carry} + \text{Roll-down}
$$

**Example:**

**BBB 5-year corporate bond:**
- Coupon: 5.5%
- Price: $100
- Current spread: 150 bp
- 1-year forward spread (4y point): 135 bp

**Annual returns (assuming unchanged curve):**

| Component | Return |
|-----------|--------|
| Carry | 5.5% |
| Roll-down | (150-135) × 4.3 = 0.65% |
| **Total carry** | **6.15%** |

**vs. 2-year bond (less roll-down):**
- Carry: 4.8%
- Roll-down: (95-90) × 1.9 = 0.10%
- **Total carry: 4.90%**

**Extra 125 bp annually from choosing 5-year!**

### 3. The Roll-Down Puzzle


**Empirical observation:**

Credit curves are persistently upward-sloping, yet investors don't arbitrage this away.

**Why?**

**Traditional explanation:**
- Risk premium for duration/credit risk
- Investors rationally demand compensation

**Behavioral explanation:**
- Institutional constraints (pension/insurance prefer short duration)
- Behavioral bias (short-term focus, loss aversion)
- **Creates persistent opportunity**

**Evidence:**
- Studies show roll-down strategies outperform over long periods
- After adjusting for risk, excess returns persist
- **Suggests some mispricing / institutional friction**

**Implication for investors:**

$$
\text{Expected Excess Return} = \beta_{\text{roll-down}} \times \text{Curve Slope}
$$

**Historically:** $\beta \approx 0.6$ to 0.8

**Meaning: Capture 60-80% of curve slope as excess return over holding period.**

---

## Key Terminology


**Credit Spread Curve:**

- Relationship between spreads and maturity
- Issuer-specific or rating-based
- Typically upward-sloping
- Measured at fixed points (2y, 5y, 10y, 30y)

**Roll-Down Return:**

- Price appreciation from aging down the curve
- Assumes curve unchanged
- Formula: $\Delta S \times D$
- Separate from carry and spread changes

**Curve Slope:**

$$
\text{Slope} = S_{\text{long}} - S_{\text{short}}
$$

- Difference between long and short maturity spreads
- Measured in basis points
- Example: 10y-2y slope = 180 bp - 90 bp = 90 bp

**Steepness:**

- Rate of change of spreads with maturity
- Steeper = more roll-down potential
- Can measure as bp/year: 90 bp / 8 years = 11.25 bp/year

**Bullet Strategy:**

- Buy bonds at one maturity point
- Hold as they roll down curve
- Reinvest at same maturity (keep exposure constant)

**Barbell Strategy:**

- Combine short and long maturities
- Avoid middle of curve
- Can capture roll-down at long end while maintaining duration target

**Curve Flattening:**

- Slope decreases (long-short spread narrows)
- Reduces roll-down potential
- Negative for roll-down strategies

**Curve Steepening:**

- Slope increases (long-short spread widens)
- Enhances roll-down potential
- But can cause immediate MTM losses

**Forwards:**

- Expected future spread implied by curve
- Formula: $F_{T_1,T_2} = $ spread at $T_2$ maturity, priced today for purchase at time $T_1$

**Breakeven Spread Change:**

$$
\text{Breakeven} = \frac{\text{Roll-down Gain}}{\text{Duration}}
$$

Amount spreads can widen before losing money over holding period.

---

## Basic Roll-Down Strategies


### 1. Strategy 1: Simple Bullet with Roll-Down Capture


**Setup:**

**Investor wants BBB credit exposure with roll-down enhancement.**

**Analysis of credit curve:**

| Maturity | Spread | Slope vs. Previous |
|----------|--------|-------------------|
| 2-year | 85 bp | - |
| 3-year | 100 bp | +15 bp |
| 5-year | 130 bp | +30 bp (over 2y) |
| 7-year | 155 bp | +25 bp (over 2y) |
| 10-year | 175 bp | +20 bp (over 3y) |

**Curve is steepest between 2y-5y (30 bp per 3 years = 10 bp/year)**

**Trade:**
- Buy $10M 5-year bonds
- Issuer: XYZ Corp (BBB-rated)
- Spread: 130 bp
- Coupon: 5.30%
- Price: $100
- Duration: 4.5 years

**1-year holding period analysis:**

**Scenario: Curve unchanged**

After 1 year:
- Bond is now 4-year maturity
- Interpolated spread at 4y: 115 bp (between 3y at 100 bp and 5y at 130 bp)
- Roll-down: 130 - 115 = 15 bp tightening

**Returns:**

| Component | Calculation | Return |
|-----------|-------------|--------|
| Carry | 5.30% | +5.30% |
| Roll-down | 15 bp × 4.3 duration | +0.65% |
| **Total** | | **+5.95%** |

**Compare to 2-year bond:**
- Carry: 4.85%
- Roll-down: (85-85) × 1.9 = 0% (curve flat at front end)
- **Total: 4.85%**

**Extra return from 5-year: 110 bp annually**

**Breakeven spread widening:**

$$
\text{Breakeven} = \frac{5.30\% + 0.65\%}{4.3} = 1.38\% = 138 \text{ bp}
$$

**Spreads can widen 138 bp before losing money over 1 year.**

### 2. Strategy 2: Rolling Bullet (Systematic Harvesting)


**Setup:**

**Portfolio strategy to continuously harvest roll-down:**

**Target:** Maintain constant 5-year maturity exposure

**Month 0:**
- Buy $50M 5-year bonds at 130 bp

**Month 12:**
- Bonds now 4-year (spread 115 bp on curve)
- **Sell $50M 4-year bonds** at 115 bp
- **Buy $50M new 5-year bonds** at 130 bp
- **Lock in roll-down gain: 15 bp**

**Month 24:**
- Repeat: Sell 4y, buy 5y
- Lock in another 15 bp

**Annual P/L (each cycle):**

| Component | Return |
|-----------|--------|
| Carry (5.30%) | +5.30% |
| Roll-down (15 bp) | +0.65% |
| Transaction costs (-2 bp) | -0.02% |
| **Net** | **+5.93%** |

**Over 5 years:**
- Captured: 15 bp × 5 = 75 bp total roll-down
- Annual: 5.93% average
- **Compounded: 33.4% total return**

**Compare to buy-and-hold 5-year:**
- Year 1: 5.95%
- Year 2: 5.85% (now 3y, less roll-down)
- Year 3: 5.50%
- Year 4: 5.00%
- Year 5: 4.85% (now at 0y, just carry)
- **Average: 5.43% (50 bp less!)**

**Rolling bullet outperforms by 50 bp annually.**

### 3. Strategy 3: Curve Positioning (Long Belly, Short Wings)


**Setup:**

**Credit curve analysis shows middle is rich:**

| Maturity | Spread | Fair Value | Rich/Cheap |
|----------|--------|------------|------------|
| 2-year | 85 bp | 90 bp | 5 bp cheap |
| 5-year | 130 bp | 120 bp | 10 bp rich |
| 10-year | 175 bp | 180 bp | 5 bp cheap |

**5-year looks rich relative to curve model!**

**Trade (curve flattener):**
- Sell $10M 5-year bonds (rich)
- Buy $5M 2-year bonds (cheap)
- Buy $5M 10-year bonds (cheap)
- **Duration-matched barbell**

**If curve normalizes (5y widens to fair value):**
- 5y: 130 → 140 bp (+10 bp)
- 2y: 85 → 85 bp (unchanged)
- 10y: 175 → 175 bp (unchanged)

**P/L:**

| Position | Spread Change | Duration | P/L |
|----------|---------------|----------|-----|
| Short 5y | 130 → 140 bp | -4.5 | +$450k |
| Long 2y | Unchanged | +1.9 | $0 |
| Long 10y | Unchanged | +7.5 | $0 |
| **Net** | | | **+$450k** |

**Plus over 1 year:**
- Short 5y: Negative carry -$530k
- Long 2y: Carry +$242.5k
- Long 10y: Carry +$287.5k
- **Net carry: $0** (roughly offset)

**Total: $450k from curve normalization**

### 4. Strategy 4: Roll-Down Enhanced with CDS


**Setup:**

**Want maximum roll-down without rate risk:**

**Portfolio:**
- Long $20M 10-year corporate bonds (BBB)
- Spread: 180 bp
- Duration: 8.5 years
- Coupon: 5.80%

**Hedges:**
- Short $20M 10-year Treasury futures (hedge rate risk)
- **Duration-neutral to rates**

**Result: Pure credit exposure with roll-down**

**1-year return (assuming curve unchanged):**

| Component | Return |
|-----------|--------|
| Bond carry | 5.80% |
| Roll-down (180 → 165 bp) | 15 bp × 8.2 = 1.23% |
| Rate hedge cost | -0.20% |
| **Total** | **6.83%** |

**Compare to:**
- 10-year Treasury: 4.0% (just carry, no credit roll-down)
- Unhedged corporate: 6.83% but exposed to rate moves
- **Hedged corporate: 6.83% isolated credit return**

**This isolates credit roll-down from rate effects!**

---

## Greeks in Roll-Down Strategies


**Understanding sensitivities:**

### 1. Duration Profile Over Time


**As bond ages, duration changes:**

$$
D(t) = D_0 - \Delta D \times t
$$

**Example: 10-year bond**

| Year | Maturity | Duration | Change |
|------|----------|----------|--------|
| 0 | 10y | 8.5 | - |
| 1 | 9y | 7.8 | -0.7 |
| 2 | 8y | 7.2 | -0.6 |
| 5 | 5y | 4.5 | -4.0 total |
| 10 | 0y | 0 | -8.5 total |

**Duration decreases as bond ages:**
- Reduces interest rate sensitivity
- Reduces spread sensitivity
- **Roll-down partially offsets this by lowering spread**

**Net sensitivity (spread × duration):**

$$
\text{Spread Risk} = S(t) \times D(t)
$$

**Example:**
- Year 0: 180 bp × 8.5 = 15.3
- Year 5: 130 bp × 4.5 = 5.85
- **Spread risk decreased by 62%**

### 2. Convexity and Roll-Down


**Roll-down creates convexity-like effect:**

**If spreads tighten:**
- Benefit from spread move
- PLUS benefit from roll-down
- **Total gain > linear (positive convexity)**

**If spreads widen:**
- Loss from spread move
- BUT partially offset by roll-down
- **Total loss < linear (positive convexity)**

**Example (1-year holding period):**

**Scenario 1: Spreads tighten 20 bp**

| Component | Return |
|-----------|--------|
| Spread tightening | 20 × 4.3 = 0.86% |
| Roll-down | 15 × 4.3 = 0.65% |
| **Total** | **1.51%** |

**Scenario 2: Spreads widen 20 bp**

| Component | Return |
|-----------|--------|
| Spread widening | -20 × 4.3 = -0.86% |
| Roll-down | 15 × 4.3 = +0.65% |
| **Total** | **-0.21%** |

**Asymmetry:**
- Upside: +1.51%
- Downside: -0.21%
- **Ratio: 7:1 (highly convex!)**

**This convexity makes roll-down strategies attractive!**

### 3. Carry-Roll Sensitivity


**Combined carry and roll-down:**

$$
\text{Total Carry-Roll} = \frac{\text{Coupon}}{P} + \frac{\Delta S \times D}{T}
$$

**Sensitivity to curve slope:**

$$
\frac{\partial \text{Roll}}{\partial \text{Slope}} = \frac{D}{T}
$$

**Example:**
- Duration: 4.5 years
- Holding period: 1 year
- **Sensitivity: 4.5 / 1 = 4.5**

**Interpretation:** 1 bp increase in slope → 4.5 bp increase in annual roll-down return.

**If curve steepens from 15 bp/year to 20 bp/year:**
- Extra roll-down: 5 bp × 4.5 = 22.5 bp
- **Extra return: 0.225%**

---

## Roll-Down Payoff Analysis


### 1. Expected Returns Across Different Curve Shapes


**Setup: BBB 5-year bond, 1-year holding period**

**Curve Scenario 1: Steep (current)**
- 5y: 150 bp
- 4y: 125 bp
- Slope: 25 bp

**Returns:**
- Carry: 5.5%
- Roll-down: 25 bp × 4.2 = 1.05%
- **Total: 6.55%**

**Curve Scenario 2: Moderate**
- 5y: 150 bp
- 4y: 140 bp
- Slope: 10 bp

**Returns:**
- Carry: 5.5%
- Roll-down: 10 bp × 4.2 = 0.42%
- **Total: 5.92%**

**Curve Scenario 3: Flat**
- 5y: 150 bp
- 4y: 150 bp
- Slope: 0 bp

**Returns:**
- Carry: 5.5%
- Roll-down: 0%
- **Total: 5.5%**

**Curve Scenario 4: Inverted (distressed)**
- 5y: 150 bp
- 4y: 175 bp
- Slope: -25 bp

**Returns:**
- Carry: 5.5%
- Roll-down: -25 bp × 4.2 = -1.05%
- **Total: 4.45%**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/credit_rolldown_return_curves.png?raw=true" alt="credit_rolldown_return_curves" width="700">
</p>
**Figure 1:** Expected returns across different credit curve shapes, showing how roll-down enhances returns on upward-sloping curves but becomes a drag on inverted curves.

### 2. Roll-Down Breakeven Analysis


**Question: How much can spreads widen before roll-down strategy loses money?**

**Setup:**
- 5-year bond: Spread 150 bp, Duration 4.5
- Expected roll-down: 25 bp over 1 year
- Carry: 5.5%

**Total cushion:**

$$
\text{Breakeven Widening} = \frac{\text{Carry} + \text{Roll-down}}{\text{Duration}}
$$

$$
= \frac{5.5\% + 1.05\%}{4.5} = \frac{6.55\%}{4.5} = 1.46\% = 146 \text{ bp}
$$

**Spreads can widen 146 bp over 1 year before losing money!**

**Comparison by maturity:**

| Maturity | Carry | Roll-down | Total | Duration | Breakeven |
|----------|-------|-----------|-------|----------|-----------|
| 2-year | 4.85% | 0.19% | 5.04% | 1.9 | 265 bp |
| 5-year | 5.50% | 1.05% | 6.55% | 4.5 | 146 bp |
| 10-year | 5.80% | 0.75% | 6.55% | 8.5 | 77 bp |

**2-year has highest breakeven (least spread-sensitive)**
**10-year has lowest breakeven (most spread-sensitive)**

**But total return similar if spreads unchanged!**

**This shows duration/maturity tradeoff in roll-down strategies.**

---

## Real-World Roll-Down Examples


### 1. Example 1: BBB Industrial Roll-Down Harvest (Winner)


**Setup:**

- **Date:** January 2019
- **Portfolio Manager:** Fixed income fund
- **Strategy:** Capture roll-down on steep BBB curve

**Market analysis:**

**BBB Industrial Credit Curve:**

| Maturity | Spread | OAS |
|----------|--------|-----|
| 2-year | 115 bp | 115 bp |
| 3-year | 135 bp | 135 bp |
| 5-year | 165 bp | 165 bp |
| 7-year | 185 bp | 185 bp |
| 10-year | 200 bp | 200 bp |

**Curve slope: 2y-10y = 85 bp**
**5y-7y slope: 20 bp over 2 years = 10 bp/year**

**View:**
- Curve unusually steep (90th percentile)
- Fundamentals stable
- Fed on hold
- **Roll-down opportunity**

**Trade:**

**Buy portfolio of 7-year bonds:**
- $100M notional across 15 issuers (diversified)
- Average spread: 185 bp
- Average coupon: 5.85%
- Average duration: 6.2 years
- Average price: $100

**Expected 1-year return:**
- Carry: 5.85%
- Roll-down (7y → 6y): Interpolate spread
  - 5y: 165 bp
  - 7y: 185 bp
  - 6y: 175 bp (linear interpolation)
  - Roll-down: 185 - 175 = 10 bp
  - Return: 10 bp × 6.0 duration = 0.60%
- **Total expected: 6.45%**

**Actual evolution (12 months):**

**Month 1-6:**
- Spreads stable
- Curve unchanged (still steep)
- Earning carry + roll-down as expected
- **6-month return: +3.15%**

**Month 7-9:**
- Trade war concerns
- Spreads widen 15 bp across curve (parallel shift)
- **BUT curve shape unchanged!**

**Impact:**
- Spread widening: -15 bp × 6.1 duration = -0.92%
- Cumulative return drops to: 3.15% - 0.92% = 2.23%

**Month 10-12:**
- Trade war fears fade
- Spreads tighten back to original levels
- **Recovery:** +0.92%
- **Back to +3.15% for 9 months**

**Final month (Month 12):**
- Bonds now 6-year maturity
- Spread: 175 bp (as expected from curve)
- Roll-down captured: 10 bp

**12-month results:**

| Component | Return | Notes |
|-----------|--------|-------|
| Carry | +5.85% | Full year coupon |
| Roll-down | +0.60% | 10 bp × 6.0 duration |
| Spread changes | 0% | Round trip |
| **Total** | **+6.45%** | Exactly as expected! |

**Compare to benchmark (BBB Index):**
- BBB Index return: +5.30% (shorter duration)
- **Outperformance: +115 bp**

**Why it worked:**

1. **Curve remained steep:**
   - Still 85 bp 2y-10y slope at year-end
   - Roll-down benefit sustained

2. **Spread volatility didn't matter:**
   - Spreads widened then tightened
   - Net zero impact
   - **Roll-down earned regardless**

3. **Diversification:**
   - 15 issuers, no defaults
   - No single-name risk

4. **Patience:**
   - Held through spread widening (Month 7-9)
   - Didn't panic sell
   - Captured full roll-down

**Manager's decision:**

**Month 12: Roll the portfolio**
- Sell all 6-year bonds at 175 bp
- Buy new 7-year bonds at 185 bp
- **Lock in 10 bp roll-down**
- **Restart strategy for Year 2**

**Year 2 (same strategy):**
- Earned another +6.45%
- **2-year cumulative: +13.3%**
- **Annualized: +6.45%**

**This is systematic roll-down harvesting!**

### 2. Example 2: High-Yield Curve Steepening Disaster (Loser)


**Setup:**

- **Date:** March 2020 (COVID crisis)
- **Trader:** Credit hedge fund
- **Strategy:** Long back-end of HY curve for roll-down

**Pre-crisis analysis:**

**High-Yield (B-rated) Curve:**

| Maturity | Spread |
|----------|--------|
| 2-year | 450 bp |
| 3-year | 500 bp |
| 5-year | 580 bp |
| 7-year | 620 bp |
| 10-year | 650 bp |

**Curve slope: Very steep (200 bp, 2y-10y)**
**Expected roll-down: 7y → 6y = ~15 bp**

**Trade:**

**Bought $50M 7-year HY bonds:**
- Spread: 620 bp
- Coupon: 8.20%
- Duration: 5.5 years
- Price: $95

**Expected 1-year return:**
- Carry: 8.20% / 0.95 = 8.63%
- Roll-down: 15 bp × 5.3 = 0.80%
- **Total: 9.43%**

**Seemed attractive!**

**What actually happened:**

**March 2020: COVID Crisis**

**Curve explosion:**

| Maturity | Before Crisis | After Crisis (3 weeks) | Change |
|----------|---------------|------------------------|--------|
| 2-year | 450 bp | 1,200 bp | +750 bp |
| 3-year | 500 bp | 1,350 bp | +850 bp |
| 5-year | 580 bp | 1,550 bp | +970 bp |
| 7-year | 620 bp | 1,700 bp | +1,080 bp |
| 10-year | 650 bp | 1,750 bp | +1,100 bp |

**Curve steepened dramatically!**

**New slope: 2y-10y = 550 bp (from 200 bp)**

**Impact on 7-year position:**

**Spread widening:**
- 620 → 1,700 bp (+1,080 bp widening)
- Loss: -1,080 bp × 5.5 duration = **-59.4%**

**Price:**
- Started: $95
- After crisis: $38.50
- **Loss: -$28.25M on $47.5M (60% loss!)**

**But wait, what about roll-down?**

**New curve shape (after crisis):**
- 7y: 1,700 bp
- 6y: ~1,620 bp (interpolated)
- **NEW expected roll-down: 80 bp** (curve steeper!)

**The problem:**
1. **Immediate massive loss** (-60%)
2. **Roll-down is long-term** (takes 1 year to earn 80 bp = 4.4%)
3. **Need 60% / 4.4% = 14 years to break even!**

**Forced decision:**

**Margin call:**
- Fund levered 3x
- -60% loss on this position
- **Must post more collateral or liquidate**

**Manager liquidated at $38.50 (locked in -60% loss)**

**The aftermath (what if held):**

**6 months later (September 2020):**
- Government stimulus
- Fed support
- HY spreads recover
- 7-year (now 6.5y): 850 bp

**Would have recovered:**
- Entry: $95 at 620 bp
- September: $78 at 850 bp
- Still down but recoverable: -18%
- Plus carry collected: +4%
- **Net: -14%** (better than -60%)

**1 year later (March 2021):**
- Full recovery
- 7-year (now 6y): 580 bp (back to entry)
- Price: $96
- Plus carry: +8.6%
- **Would have been +10% if held!**

**But couldn't hold due to leverage and margin calls.**

**What went wrong:**

1. **Ignored curve steepening risk:**
   - Assumed curve shape stable
   - Crisis steepened curve massively
   - **Long end widened MORE than front (opposite of roll-down)**

2. **Used leverage (3x):**
   - -60% loss on 3x leverage = -180% of equity
   - **Forced liquidation**

3. **High yield credit (wrong asset class):**
   - Investment grade curves flatten in stress
   - **High yield curves STEEPEN in stress** (longer maturity = higher default risk)
   - Roll-down doesn't work in HY during stress

4. **Poor timing:**
   - Entered just before crisis
   - No time for roll-down to accrue

5. **No hedges:**
   - Pure long credit exposure
   - Should have hedged with index or shorter maturity

**Lessons:**

- **Roll-down requires stable curve shape**
- **HY curves steepen in crisis** (not flatten like IG/Treasuries)
- **Leverage kills during drawdowns**
- **Roll-down is long-term strategy, not short-term trade**

### 3. Example 3: Investment Grade Curve Flattening (Breakeven)


**Setup:**

- **Date:** June 2024
- **Portfolio:** Corporate bond fund
- **Strategy:** Overweight 10-year IG for roll-down

**Credit curve (A-rated):**

| Maturity | Spread |
|----------|--------|
| 2-year | 65 bp |
| 5-year | 95 bp |
| 7-year | 110 bp |
| 10-year | 125 bp |
| 30-year | 145 bp |

**Slope: 2y-10y = 60 bp**
**Expected roll-down (10y → 9y): ~7 bp**

**Trade:**

**$200M 10-year bonds:**
- Spread: 125 bp
- Coupon: 5.25%
- Duration: 8.5 years

**Expected return:**
- Carry: 5.25%
- Roll-down: 7 bp × 8.3 = 0.58%
- **Total: 5.83%**

**Evolution (12 months):**

**Months 1-6:**
- Economic slowdown fears
- Investors extend duration (flight to quality)
- **Curve flattens:**

| Maturity | Before | After 6M | Change |
|----------|--------|----------|--------|
| 2-year | 65 bp | 70 bp | +5 bp |
| 5-year | 95 bp | 95 bp | 0 bp |
| 7-year | 110 bp | 108 bp | -2 bp |
| 10-year | 125 bp | 118 bp | -7 bp |

**10-year tightened (good!), but curve flattened:**
- Old slope (2y-10y): 60 bp
- New slope: 48 bp
- **Flattening: 12 bp**

**Impact:**

**Direct spread tightening:**
- 125 → 118 bp (-7 bp)
- Gain: 7 bp × 8.4 = 0.59%

**But roll-down potential decreased:**
- 10y → 9y roll-down now: 5 bp (not 7 bp)
- **Lost 2 bp of expected roll-down**

**6-month return:**
- Carry: 2.625% (half year)
- Spread gain: 0.59%
- **Total: 3.21%**

**vs. Expected: 2.92%**
**Beat by 0.29% (curve tightening helped)**

**Months 7-12:**

**Curve continues flattening:**
- Fed cuts rates (stimulative)
- Short end widens (rate cuts already priced)
- Long end stable
- **Curve slope: 48 → 35 bp**

**10-year position (now 9-year):**
- Spread: 118 → 115 bp (small tightening)
- Gain: 3 bp × 8.1 = 0.24%

**Roll-down captured:**
- Started year at 10y: 125 bp
- Now at 9y: 115 bp
- **Roll-down: 10 bp** (close to expected 7 bp + tightening)

**Full year results:**

| Component | Return |
|-----------|--------|
| Carry | 5.25% |
| Spread tightening | 0.83% |
| **Total** | **6.08%** |

**vs. Expected: 5.83%**
**Beat by 25 bp**

**But analysis:**

**Breakdown:**
- Expected roll-down: 0.58% (7 bp)
- Actual roll-down: 0.83% (10 bp)
- Difference: +0.25%

**This came from curve tightening (not curve shape preservation).**

**If held another year:**

**Now at 9y maturity:**
- Current spread: 115 bp
- Expected 8y spread: 108 bp (curve very flat now)
- Expected roll-down: Only 7 bp
- **Less than half of original!**

**Decision: Reduce position**

- Curve too flat now (only 35 bp slope)
- Roll-down not attractive anymore
- **Take profits, redeploy**

**Lessons:**

1. **Curve flattening reduces future roll-down**
2. **Initial spread tightening helped** (offset flattening)
3. **Need to monitor curve shape continuously**
4. **Roll-down strategies work best on steep curves**
5. **Exit when curve flattens** (opportunity diminished)

---

## Best Case Scenario


### 1. The Perfect Roll-Down Trade - Post-Crisis Steepening (2010-2012)


**Setup:**

- **Date:** January 2010 (post-financial crisis)
- **Manager:** Credit opportunities fund
- **Capital:** $500M

**Market environment:**

**Post-crisis credit curves extremely steep:**

**BBB Credit Curve (January 2010):**

| Maturity | Spread | Historical Average | Percentile |
|----------|--------|-------------------|------------|
| 2-year | 180 bp | 120 bp | 85th |
| 3-year | 220 bp | 140 bp | 90th |
| 5-year | 280 bp | 170 bp | 95th |
| 7-year | 320 bp | 195 bp | 97th |
| 10-year | 350 bp | 210 bp | 98th |

**Curve slope (2y-10y): 170 bp (historical: 90 bp)**

**Why so steep?**
- Post-crisis fear (uncertainty premium)
- Investors clustered in short maturity (safety)
- Issuers desperate for long-term funding
- **Massive supply/demand imbalance**

**Strategy:**

**Overweight belly of curve (5-7 year):**
- Maximum roll-down per unit duration
- Not too long (avoid excessive tail risk)
- Most liquid part of curve

**Portfolio construction:**

**$500M allocated:**
- $350M in 7-year BBB bonds (70%)
- $100M in 5-year BBB bonds (20%)
- $50M in 10-year AAA bonds (10% defensive)

**7-year positions (primary):**
- 25 issuers (diversified)
- Average spread: 315 bp
- Average coupon: 7.15%
- Average duration: 6.0 years
- Average price: $98

**Expected annual return:**
- Carry: 7.15% / 0.98 = 7.30%
- Roll-down (7y → 6y): 
  - 7y: 320 bp
  - 6y: 300 bp (interpolated)
  - Roll: 20 bp
  - Return: 20 bp × 5.8 = 1.16%
- **Total: 8.46% annually**

**Year 1 (2010):**

**Market recovery:**
- Economy stabilizing
- Credit spreads tightening
- **Curve shape initially maintained** (still steep)

**6-month checkpoint:**
- Spreads: 315 → 280 bp (-35 bp tightening)
- Gain: 35 bp × 6.0 = 2.10%
- Carry: 3.65%
- **Total: 5.75% (6 months)**

**12-month results:**

| Component | Return | Notes |
|-----------|--------|-------|
| Carry | 7.30% | Full coupon |
| Roll-down | 1.16% | 20 bp × 5.8 |
| Spread tightening | 2.45% | 35 bp net |
| **Total** | **10.91%** | Exceptional! |

**Year 2 (2011):**

**Continued improvement:**
- BBB spreads normalizing
- 7y (now 6y from original purchase): 280 → 220 bp
- **Curve maintaining steepness:**

| Maturity | Spread | Slope vs Previous |
|----------|--------|-------------------|
| 2-year | 130 bp | - |
| 5-year | 195 bp | +65 bp |
| 6-year | 220 bp | +25 bp |
| 10-year | 240 bp | +20 bp |

**Still steep! (110 bp, 2y-10y)**

**Year 2 return:**

| Component | Return |
|-----------|--------|
| Carry | 7.50% |
| Roll-down (6y → 5y) | 25 bp × 5.0 = 1.25% |
| Spread tightening | 60 bp × 5.2 = 3.12% |
| **Total** | **11.87%** |

**2-year cumulative: +24.2%**

**Year 3 (2012): Harvest and Reposition**

**Curve beginning to flatten:**

| Maturity | Spread | Change from 2010 |
|----------|--------|------------------|
| 2-year | 110 bp | -70 bp |
| 5-year | 180 bp | -100 bp |
| 7-year | 200 bp | -120 bp |
| 10-year | 215 bp | -135 bp |

**New slope (2y-10y): 105 bp** (from 170 bp)
**Flattening: 65 bp over 2 years**

**Current position (now 5-year from original 7-year):**
- Spread: 180 bp
- Duration: 4.5 years

**Expected forward roll-down: Only 15 bp** (curve flatter)

**Decision:**

**Q1 2012: Start reducing position**
- Sold $200M 5-year bonds at 180 bp
- Locked in gains from 3-year holding
- Redeployed to shorter duration (curve flattened)

**Remaining $150M:**
- Held to maturity over next 2 years
- Continued earning carry + roll-down

**Year 3 (partial year) results:**

| Component | Return |
|-----------|--------|
| Carry | 7.80% |
| Roll-down | 0.68% |
| Spread tightening | 1.12% |
| **Total** | **9.60%** |

**3-year total strategy results:**

**$350M original position:**

| Year | Return | Cumulative |
|------|--------|------------|
| 2010 | +10.91% | +10.91% |
| 2011 | +11.87% | +23.99% |
| 2012 | +9.60% | +36.53% |

**Total return: +36.53% over 3 years**
**Annualized: 10.95%**

**Comparison to benchmarks:**

| Strategy/Index | 3-Year Return | Annualized |
|----------------|---------------|------------|
| **7-year Roll-down** | **+36.53%** | **10.95%** |
| BBB Index (avg 5y) | +24.10% | 7.48% |
| Treasury 7-year | +15.20% | 4.83% |
| S&P 500 | +42.50% | 12.60% |

**Outperformance vs BBB Index: +12.43% total, +3.47% annually**

**Why this was best case:**

1. **Perfect entry timing:**
   - Entered at steepest curve in decades (98th percentile)
   - Post-crisis dislocation

2. **Curve remained steep:**
   - Maintained 100+ bp slope for 2+ years
   - Roll-down benefit sustained

3. **Spread tightening amplified returns:**
   - 100-120 bp tightening over 3 years
   - Roll-down + tightening = double benefit

4. **Disciplined exit:**
   - Recognized curve flattening in Year 3
   - Reduced positions before roll-down diminished
   - Locked in profits

5. **No defaults:**
   - 25 issuers, all survived
   - Post-crisis recovery, not deterioration

6. **Compounding:**
   - Earned 10-12% for 3 consecutive years
   - Reinvested proceeds into new positions

**Attribution of 36.53% total return:**

| Component | Contribution | % of Total |
|-----------|--------------|------------|
| Carry (3 years) | +23.1% | 63% |
| Roll-down | +3.1% | 8% |
| Spread tightening | +10.3% | 28% |
| **Total** | **+36.53%** | **100%** |

**Roll-down was 8% of return, but crucial for:**
- Convexity (buffered against spread widening)
- Enhanced Sharpe ratio
- Predictable component

---

## Worst Case Scenario


### 1. The Inverted Curve Trap - Energy Sector (2015-2016)


**Setup:**

- **Date:** June 2015
- **Fund:** Energy sector credit specialist
- **Capital:** $200M

**Market environment:**

**Oil prices collapsing:**
- June 2015: $60/barrel
- Concerns about shale production
- OPEC not cutting supply
- **Energy sector credit stress beginning**

**Energy Sector Credit Curve (B-rated):**

| Maturity | Spread | Notes |
|----------|--------|-------|
| 1-year | 550 bp | Near-term stress |
| 2-year | 480 bp | |
| 3-year | 420 bp | Recovery expected |
| 5-year | 380 bp | |
| 7-year | 350 bp | Long-term value |
| 10-year | 320 bp | |

**Curve INVERTED: -230 bp (1y to 10y)**

**Manager's flawed logic:**

"The curve is inverted because of near-term fear. But energy will recover. Long-dated bonds are cheap. Let's buy the back end and capture the 'normalization' as curve steepens and we roll down."

**Fatal mistakes in this thinking:**

1. **Inverted curve signals distress** (not opportunity)
2. **Roll-down is NEGATIVE on inverted curve**
3. **Long-dated bonds most at risk** in bankruptcy

**Trade (the mistake):**

**Bought $200M 7-year energy bonds:**
- $100M: Oil E&P companies
- $100M: Oil services companies
- Average spread: 350 bp
- Average coupon: 7.50%
- Duration: 5.8 years
- Price: $92

**"Expected" return:**
- Carry: 7.50% / 0.92 = 8.15%
- "Roll-down": ??? (curve inverted!)
  - Manager assumed: "Curve will steepen, then we roll down"
- **This is NOT a roll-down trade—it's speculation on curve shape change**

**What actually happened:**

**Month 1-3 (Jun-Aug 2015):**

**Oil continues falling:**
- $60 → $45/barrel

**Credit curves invert MORE:**

| Maturity | June | August | Change |
|----------|------|--------|--------|
| 1-year | 550 bp | 800 bp | +250 bp |
| 2-year | 480 bp | 700 bp | +220 bp |
| 3-year | 420 bp | 600 bp | +180 bp |
| 5-year | 380 bp | 520 bp | +140 bp |
| 7-year | 350 bp | 450 bp | +100 bp |
| 10-year | 320 bp | 400 bp | +80 bp |

**New curve slope: -400 bp (1y to 10y)**
**Even more inverted!**

**7-year position:**
- Spread: 350 → 450 bp (+100 bp)
- Loss: -100 bp × 5.8 = -5.8%
- Carry (3 months): +2.0%
- **Net: -3.8%**

**"Negative roll-down" starting:**
- Bond aging from 7y → 6.83y
- 6.83y spread on curve: 485 bp (interpolated)
- **Moving to WIDER spreads as it ages** (inverted curve)

**Month 4-9 (Sep 2015 - Jan 2016):**

**Disaster accelerates:**

**Oil crashes:**
- $45 → $28/barrel (record low)

**Defaults begin:**
- 12 energy companies file bankruptcy (Q4 2015)
- Including 2 in portfolio!

**Portfolio damage:**

**2 defaults (10% of portfolio):**
- $20M face value (2 issuers)
- Recovery: 25% (stressed market)
- **Loss: $15M (-7.5% of total portfolio)**

**Remaining bonds:**
- Spread: 450 → 850 bp (+400 bp more)
- Loss: -400 bp × 5.5 = -22%
- Carry (6 months): +4.0%
- **Net: -18%**

**Total portfolio:**
- Defaults: -7.5%
- Spread widening: -18%
- Carry: +4.0%
- **Net: -21.5%**

**Curve now:**

| Maturity | Spread |
|----------|--------|
| 1-year | 1,500 bp (default imminent for many) |
| 3-year | 1,200 bp |
| 5-year | 980 bp |
| 7-year | 850 bp |
| 10-year | 750 bp |

**Inversion: -750 bp!**

**The negative roll-down accelerating:**
- 7y bonds now 6.5y maturity
- 6.5y curve spread: 920 bp
- As bond ages, moving to WIDER spreads!
- **Negative roll-down: -70 bp over 6 months**

**Month 10-15 (Feb-Jul 2016):**

**Capitulation:**

**More defaults:**
- 3 more portfolio companies file bankruptcy
- **Total defaults: 25% of portfolio**
- Additional losses: $25M

**Remaining portfolio:**
- 75% still alive
- Spreads: 850 → 1,200 bp (distressed)
- **Loss from peak:** -60%

**Fund decision: Liquidate remaining positions**

**July 2016:**
- Sold $150M remaining bonds at average 40 cents on dollar
- Total recovered: $60M
- **Loss on this portion: -$90M**

**Total fund outcome:**

**Starting capital: $200M**

| Component | Loss |
|-----------|------|
| Defaults (25% at 25% recovery) | -$37.5M |
| Liquidated positions (75% at 40¢) | -$90M |
| Carry collected | +$12M |
| **Net** | **-$115.5M** |

**Total loss: -57.75%**

**The aftermath (what if held):**

**2017-2018: Oil recovers**
- Oil: $28 → $70/barrel
- Surviving companies recover
- Spreads: 1,200 → 350 bp

**If held survivors (impossible due to fund redemptions):**
- 75% of portfolio at 40¢ → $98 (normalized)
- Would have recovered to ~$147M total
- **Still down -26% but better than -58%**

**But couldn't hold:**
- Fund had redemptions
- Forced to liquidate
- Locked in worst prices

**What went wrong:**

1. **Inverted curve misunderstood:**
   - Inversion signals distress (not opportunity)
   - "Roll-down" is NEGATIVE on inverted curve
   - Every day, bonds moved to wider spreads

2. **Sector concentration:**
   - 100% in energy
   - No diversification
   - All positions correlated

3. **Ignored default risk:**
   - Inverted curve price in high default probability
   - Manager thought "fear overdone"
   - **25% of portfolio defaulted**

4. **Wrong maturity:**
   - Bought longest maturity (7-10 year)
   - Most exposed to bankruptcy (last to recover)
   - Should have been in 1-2 year (higher spread, lower duration)

5. **Confused speculation with roll-down:**
   - This was NOT a roll-down trade
   - This was betting on curve shape normalization
   - Pure speculation, not harvesting

6. **Negative convexity on inverted curve:**
   - If spreads tighten: Benefit less (short duration to short maturity)
   - If spreads widen: Lose more (long duration)
   - **Worst risk/reward profile possible**

**Lessons:**

1. **Inverted curves = DANGER, not opportunity**
2. **Roll-down only works on upward-sloping curves**
3. **On inverted curves: SHORT maturity, not LONG**
4. **Credit curves invert for a reason** (imminent stress)
5. **Don't fight the curve signal**
6. **Diversify across sectors** (especially distressed)

**The "anti-roll-down" calculation:**

**Year 1 holding period (if no defaults):**
- Started at 7y: 350 bp
- After 1 year at 6y: 485 bp (curve inverted)
- **"Roll-down": +135 bp WIDENING**
- Loss: -135 bp × 5.7 = **-7.7%**
- Carry: +8.15%
- **Net: +0.45%** (barely positive even without defaults)

**This shows inverted curves destroy roll-down strategies.**

---

## What to Remember


### 1. Core Concept


**Roll-down is price appreciation from aging down credit curve:**

$$
R_{\text{roll-down}} = (S_{\text{long}} - S_{\text{short}}) \times D
$$

- Works on upward-sloping curves
- Mechanical return (doesn't require spread tightening)
- Separate from carry
- Amplified by steeper curves
- Most powerful in belly of curve (5-7 year typically)

### 2. Total Return Decomposition


$$
R_{\text{total}} = R_{\text{carry}} + R_{\text{roll}} + R_{\text{roll-down}} + R_{\text{spread}} + R_{\text{rates}}
$$

**Example:**
- Carry: 5.5% (coupon)
- Roll (pull-to-par): -0.2% (premium bond)
- Roll-down: +0.8% (curve slope 20 bp)
- Spread change: +0.5% (tightening 10 bp)
- Rate change: -0.3% (hedged)
- **Total: 6.3%**

### 3. Curve Requirements


**For positive roll-down:**
- [ ] Upward-sloping curve
- [ ] Steep slope (>20 bp per 2 years minimum)
- [ ] Stable curve shape expected
- [ ] Investment grade or stable HY (not distressed)

**Warning signs (avoid roll-down):**
- [ ] Flat curve (<10 bp slope)
- [ ] Inverted curve (any amount)
- [ ] Distressed credits (CCC and below)
- [ ] Curve steepening expected

### 4. Optimal Maturity Selection


**Formula for maximum roll-down per unit duration:**

$$
\text{Efficiency} = \frac{\Delta S}{\Delta T \times D(T)}
$$

**Where:**
- $\Delta S$ = Spread change over maturity range
- $\Delta T$ = Maturity range
- $D(T)$ = Duration at maturity $T$

**Typically optimal: 5-7 year maturity**
- Steep part of curve
- Moderate duration (4-6 years)
- Liquid
- **Sweet spot for roll-down/duration tradeoff**

### 5. Position Sizing


**Conservative:**

$$
\text{Position Size} = \min\left(10\% \text{ of portfolio}, \frac{5\%}{\text{Duration}}\right)
$$

**Example:**
- Portfolio: $100M
- 7-year bond duration: 6.0
- Max position: min($10M, $5M/6.0) = min($10M, $0.83M) = **$833k**

**Or scale by curve slope:**

$$
\text{Position} = \text{Base} \times \frac{\text{Current Slope}}{\text{Historical Avg Slope}}
$$

**If curve steeper than average, can size larger.**

### 6. Monitoring Metrics


**Daily:**
- Curve slope (track changes)
- Spread levels
- Roll-down accrual

**Weekly:**
- Expected vs. actual roll-down
- Curve shape changes (flattening/steepening)
- Duration drift

**Monthly:**
- Return attribution (carry vs. roll vs. spread)
- Curve percentile ranking
- Rebalancing needs

### 7. Entry Checklist


1. **Curve analysis:**
   - [ ] Upward-sloping (positive slope)
   - [ ] Slope > 20 bp over target holding period
   - [ ] At least 50th percentile steepness (vs. history)

2. **Fundamentals:**
   - [ ] Investment grade or stable HY
   - [ ] No imminent defaults expected
   - [ ] Sector diversified (if multiple names)

3. **Technical:**
   - [ ] Curve shape expected to persist
   - [ ] No major supply/demand shifts expected
   - [ ] Liquidity adequate

4. **Position:**
   - [ ] Optimal maturity (5-7y typically)
   - [ ] Duration appropriate for risk tolerance
   - [ ] Size within limits

### 8. Exit Rules


**Close position when:**

1. **Curve flattens significantly:**
   - Slope < 10 bp over next year
   - Below 25th percentile historically

2. **Credit deterioration:**
   - Downgrade announced/likely
   - Fundamentals weakening

3. **Time-based:**
   - Held for target period (1-2 years typically)
   - Roll down the curve, sell, reinvest at longer maturity

4. **Profit target:**
   - Achieved expected roll-down + alpha
   - Take profits if > 75% of potential captured

5. **Stop loss:**
   - Total return < -5% (carry + roll should prevent this)
   - Spread widening > 100 bp

### 9. Common Mistakes to Avoid


1. **Confusing roll with roll-down**
   - Roll = pull to par (price → 100)
   - Roll-down = curve effect (spread tightening from aging)

2. **Assuming all curves have roll-down**
   - Flat curves: Zero roll-down
   - Inverted: NEGATIVE roll-down

3. **Ignoring curve shape changes**
   - Steepening/flattening can reverse gains
   - Must monitor continuously

4. **Using roll-down on distressed credits**
   - Inverted curves common in distress
   - Roll-down works against you

5. **Overleveraging**
   - Roll-down is slow (1-2% annually typically)
   - Leverage amplifies curve changes (bad)

6. **Buying too long maturity**
   - 20-30 year has high duration risk
   - Roll-down/duration ratio poor

7. **No diversification**
   - Single issuer has idiosyncratic risk
   - Defeats roll-down strategy

8. **Ignoring transaction costs**
   - Rolling strategy has costs
   - Eats into 0.5-1.0% annual roll-down

### 10. Performance Expectations


**Investment grade roll-down strategy (5-7y):**

| Market | Carry | Roll-down | Total | Notes |
|--------|-------|-----------|-------|-------|
| Best | 5-6% | 1.0-1.5% | 6.5-7.5% | Steep curve, spreads tighten |
| Good | 5-6% | 0.7-1.0% | 5.7-7.0% | Normal curve, stable spreads |
| Base | 5-6% | 0.3-0.7% | 5.3-6.7% | Moderate curve |
| Poor | 5-6% | 0% | 5.0-6.0% | Flat curve |
| Worst | 5-6% | -0.5% | 4.5-5.5% | Inverted curve |

**Sharpe ratio: 1.2-1.8** (with roll-down)
**vs. 0.8-1.2** (without roll-down positioning)

### 11. Comparison to Other Strategies


| Strategy | Carry | Roll-Down | Complexity | Risk |
|----------|-------|-----------|------------|------|
| **Long maturity (roll-down)** | High | High | Medium | Duration |
| Short maturity | Medium | Low | Low | Reinvestment |
| Barbell | Medium | Medium | High | Curve risk |
| Ladder | Medium | Medium | Low | None special |

### 12. Your Learning Path


**Phase 1 (Months 1-3): Fundamentals**
- Study credit curves (plot spreads vs. maturity)
- Calculate roll-down for sample bonds
- Understand roll vs. roll-down distinction
- Track curve changes over time

**Phase 2 (Months 4-6): Analysis**
- Identify steep vs. flat curves
- Calculate optimal maturities
- Backtest historical roll-down
- Scenario analysis (curve changes)

**Phase 3 (Months 7-12): Implementation**
- Build small roll-down portfolio (10%)
- Track attribution (carry vs. roll vs. spread)
- Practice rolling strategy (sell/buy)
- Monitor curve changes

**Phase 4 (Year 2+): Optimization**
- Dynamic maturity selection
- Curve timing (steepening/flattening)
- Combine with other strategies
- Full portfolio implementation

### 13. Final Wisdom


> "Roll-down is the most predictable source of excess return in credit markets—when the curve cooperates. An upward-sloping curve is your friend, paying you to age down from higher spreads to lower spreads. But the curse of roll-down is curve shape changes. Steep curves flatten, flat curves invert, and the mechanical return you counted on evaporates. The disciplined investor monitors the curve daily, sizes positions by slope, diversifies across issuers, and exits when the curve flattens. The greedy investor buys long-dated bonds on inverted curves thinking 'this can't last,' only to watch negative roll-down compound their losses as the curve inverts further during default cycles. Know your curve, respect its shape, and remember: roll-down is arithmetic until it becomes tragic."

**Keys to success:**

1. **Only trade roll-down on upward curves** (>20 bp slope minimum)
2. **Monitor curve shape daily** (flattening destroys strategy)
3. **Optimize maturity** (5-7 year sweet spot typically)
4. **Diversify across issuers** (10+ names minimum)
5. **Size by slope** (steeper curve = larger position)
6. **Exit when curve flattens** (<10 bp slope, get out)
7. **Never on distressed** (inverted curves = negative roll)
8. **Combine with carry** (total carry-roll strategy)

**Most critical rule:**

$$
\text{Upward curve} \Rightarrow \text{Buy for roll-down}
$$

$$
\text{Flat curve} \Rightarrow \text{Avoid (no benefit)}
$$

$$
\text{Inverted curve} \Rightarrow \text{SHORT maturity (opposite strategy)}
$$

Inverted curves are warning signs, not opportunities. They're the market telling you: "Default risk is imminent, longer maturity is more dangerous." Listen to that signal. The energy sector disaster of 2015-2016 proved definitively: you cannot harvest roll-down from an inverted curve. The negative roll-down will destroy you before any recovery occurs. Choose your curves wisely. 🎯📊
