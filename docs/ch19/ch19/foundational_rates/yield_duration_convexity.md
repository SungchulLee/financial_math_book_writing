# Yield, Duration, and Convexity

**Yield, duration, and convexity** are the fundamental quantitative measures for understanding and managing fixed income securities, where yield captures the expected return, duration measures linear interest rate sensitivity (first-order risk), and convexity measures the curvature of the price-yield relationship (second-order risk), together forming the complete framework for bond pricing, hedging, and portfolio construction.

---

## The Core Insight

**The fundamental idea:**

- Bond prices and yields move inversely (fundamental relationship)
- Duration quantifies this sensitivity (price change per yield change)
- Convexity captures the non-linearity (acceleration of price changes)
- All bonds have positive convexity (beneficial asymmetry)
- Longer maturity = higher duration = higher interest rate risk
- Lower coupon = higher duration = higher sensitivity
- Convexity is always valuable (pure optionality)
- Can construct hedges using duration matching
- Portfolio immunization possible via duration/convexity

**The key equations:**

$$
\text{Price} = \sum_{t=1}^{N} \frac{C}{(1+y)^t} + \frac{F}{(1+y)^N}
$$

$$
\text{Duration} = -\frac{1}{P} \frac{dP}{dy} \quad \text{(interest rate sensitivity)}
$$

$$
\text{Convexity} = \frac{1}{P} \frac{d^2P}{dy^2} \quad \text{(curvature)}
$$

$$
\Delta P \approx -D \times P \times \Delta y + \frac{1}{2} C \times P \times (\Delta y)^2
$$

**You're essentially learning: "Bond prices decline when yields rise, with the magnitude determined by duration (linear effect) and convexity (non-linear enhancement), allowing precise measurement of interest rate risk, construction of hedged portfolios, and optimization of risk-return trade-offs through mathematical quantification of fixed income exposures."**

---

## What Are Yield, Duration, and Convexity?

**Before trading bonds, understand the fundamental metrics:**

### 1. Bond Pricing Fundamentals

**Present value framework:**

$$
P = \sum_{t=1}^{N} \frac{C}{(1+y)^t} + \frac{F}{(1+y)^N}
$$

Where:
- $P$ = Bond price (present value)
- $C$ = Coupon payment (annual or semi-annual)
- $y$ = Yield to maturity (discount rate)
- $F$ = Face value (par, typically $1,000)
- $N$ = Number of periods to maturity

**Example: 5-year bond**

**Bond characteristics:**
- Face value: $1,000
- Coupon rate: 5% (annual, so $50/year)
- Yield to maturity: 6%
- Maturity: 5 years

**Price calculation:**

$$
P = \frac{50}{1.06^1} + \frac{50}{1.06^2} + \frac{50}{1.06^3} + \frac{50}{1.06^4} + \frac{50}{1.06^5} + \frac{1000}{1.06^5}
$$

$$
P = 47.17 + 44.50 + 41.98 + 39.60 + 37.36 + 747.26 = \$957.87
$$

**Trading at discount (below par) because yield > coupon**

### 2. Yield Measures

**Multiple yield concepts:**

**1. Current Yield:**

$$
\text{Current Yield} = \frac{\text{Annual Coupon}}{\text{Price}}
$$

**Example:**
- Price: $957.87
- Coupon: $50

$$
\text{Current Yield} = \frac{50}{957.87} = 5.22\%
$$

**Simple but incomplete (ignores capital gain/loss)**

**2. Yield to Maturity (YTM):**

$$
\text{YTM} = y \text{ such that } P = \sum_{t=1}^{N} \frac{C}{(1+y)^t} + \frac{F}{(1+y)^N}
$$

**Internal rate of return of the bond**

**Most commonly used yield measure**

**3. Yield to Call (YTC):**

$$
\text{YTC} = y \text{ such that } P = \sum_{t=1}^{T_c} \frac{C}{(1+y)^t} + \frac{P_c}{(1+y)^{T_c}}
$$

Where:
- $T_c$ = Time to call date
- $P_c$ = Call price

**Relevant for callable bonds**

**4. Yield to Worst (YTW):**

$$
\text{YTW} = \min(\text{YTM}, \text{YTC}_1, \text{YTC}_2, \ldots)
$$

**Conservative measure (worst-case yield)**

### 3. Duration

**Macaulay Duration (original concept):**

$$
D_{\text{Mac}} = \frac{\sum_{t=1}^{N} t \times \frac{CF_t}{(1+y)^t}}{P}
$$

**Weighted average time to receive cash flows**

**Example (same 5-year bond):**

| Period | Cash Flow | PV | Weight | $t \times$ Weight |
|--------|-----------|-------|--------|-------------------|
| 1 | $50 | $47.17 | 4.92% | 0.0492 |
| 2 | $50 | $44.50 | 4.65% | 0.0930 |
| 3 | $50 | $41.98 | 4.38% | 0.1314 |
| 4 | $50 | $39.60 | 4.13% | 0.1652 |
| 5 | $1,050 | $784.62 | 81.91% | 4.0955 |

$$
D_{\text{Mac}} = 0.0492 + 0.0930 + 0.1314 + 0.1652 + 4.0955 = 4.53 \text{ years}
$$

**Modified Duration (price sensitivity):**

$$
D_{\text{Mod}} = \frac{D_{\text{Mac}}}{1+y}
$$

**For our example:**

$$
D_{\text{Mod}} = \frac{4.53}{1.06} = 4.27
$$

**Interpretation:**

$$
\frac{\Delta P}{P} \approx -D_{\text{Mod}} \times \Delta y
$$

**If yields rise 1% (100 bps):**

$$
\frac{\Delta P}{P} \approx -4.27 \times 0.01 = -4.27\%
$$

**Expected price change: -4.27%**

**Actual calculation:**

**New price at 7% yield:**

$$
P_{7\%} = \sum_{t=1}^{5} \frac{50}{1.07^t} + \frac{1000}{1.07^5} = \$918.00
$$

**Price change:**

$$
\frac{918.00 - 957.87}{957.87} = -4.16\%
$$

**Close to duration estimate (-4.27%)!**

**Difference due to convexity (see below)**

### 4. Convexity

**Mathematical definition:**

$$
C = \frac{1}{P} \frac{d^2P}{dy^2} = \frac{1}{P(1+y)^2} \sum_{t=1}^{N} CF_t \times t(t+1) \times (1+y)^{-t}
$$

**For our 5-year bond:**

| Period | Cash Flow | $t(t+1)$ | PV Factor | Contribution |
|--------|-----------|----------|-----------|--------------|
| 1 | $50 | 2 | $(1.06)^{-1}$ | 4.44 |
| 2 | $50 | 6 | $(1.06)^{-2}$ | 12.54 |
| 3 | $50 | 12 | $(1.06)^{-3}$ | 23.63 |
| 4 | $50 | 20 | $(1.06)^{-4}$ | 37.27 |
| 5 | $1,050 | 30 | $(1.06)^{-5}$ | 1,119.03 |

$$
\sum = 1,196.91
$$

$$
C = \frac{1,196.91}{957.87 \times (1.06)^2} = 1,196.91 / 1,076.17 = 23.52
$$

**Enhanced price change formula:**

$$
\frac{\Delta P}{P} \approx -D_{\text{Mod}} \times \Delta y + \frac{1}{2} C \times (\Delta y)^2
$$

**For 1% yield increase:**

$$
\frac{\Delta P}{P} \approx -4.27 \times 0.01 + \frac{1}{2} \times 23.52 \times (0.01)^2
$$

$$
= -0.0427 + 0.00118 = -4.15\%
$$

**Matches actual (-4.16%) almost perfectly!**

**Convexity improved estimate from -4.27% to -4.15%**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/duration_convexity.png?raw=true" alt="duration_convexity" width="700">
</p>
**Figure 1:** Price-yield relationship showing positive convexity. Duration (tangent line) provides linear approximation of price changes, while convexity (curvature) captures the acceleration. All option-free bonds exhibit positive convexity, meaning price increases when yields fall exceed price decreases when yields rise by the same amount—a valuable asymmetry that becomes more pronounced for longer-duration bonds.

---

## Economic Interpretation

**Beyond the mathematics, understanding the economics:**

### 1. Duration as Weighted Average Maturity

**The deep insight:**

Duration is NOT just a derivative—it's the **weighted average time** until you receive your money back, where weights are the present values of cash flows.

**Intuition:**

**Zero-coupon bond:**
- Only one cash flow (at maturity)
- All weight on final payment
- Duration = Maturity (exactly)
- **Pure example**

**Example: 10-year zero-coupon bond**

$$
D_{\text{Mac}} = 10 \text{ years} \quad \text{(duration equals maturity)}
$$

**Coupon bond:**
- Multiple cash flows
- Earlier payments reduce average time
- Duration < Maturity (always)
- **Mix of timings**

**Example: 10-year 5% coupon**

- Macaulay duration ≈ 8.0 years
- Less than maturity (10 years)
- **Earlier coupons reduce duration**

**High-coupon bond:**
- Large early cash flows
- Even shorter duration
- Duration << Maturity
- **Front-loaded**

**Example: 10-year 10% coupon**

- Macaulay duration ≈ 7.0 years
- Significantly less than maturity
- **High coupons = lower duration**

### 2. Duration as Interest Rate Elasticity

**Economic parallel:**

$$
\text{Duration} = \text{Price elasticity with respect to yield}
$$

**Just like demand elasticity:**

$$
\varepsilon_{\text{demand}} = \frac{\% \Delta Q}{\% \Delta P}
$$

**Duration:**

$$
D = -\frac{\% \Delta P}{\Delta y}
$$

**Interpretation:**

- High duration = High sensitivity (elastic)
- Low duration = Low sensitivity (inelastic)
- **Analogous to economics**

### 3. Convexity as Optionality

**The deep insight:**

Convexity represents **inherent optionality** in fixed income. It's the mathematical manifestation of the asymmetric payoff structure.

**Option analogy:**

**Long bond = Long gamma:**

- Yields fall 1%: Price rises >4.27% (convexity helps)
- Yields rise 1%: Price falls <4.27% (convexity helps)
- **Both directions beneficial**

**This is like long option:**

- Underlying rallies: Delta increases (more upside)
- Underlying falls: Delta decreases (less downside)
- **Convexity = Gamma**

**Mathematical proof:**

**For small yield changes:**

$$
\Delta P = -D \times P \times \Delta y
$$

**For large yield changes:**

$$
\Delta P = -D \times P \times \Delta y + \frac{1}{2} C \times P \times (\Delta y)^2
$$

**The second term is ALWAYS positive:**

- $(\Delta y)^2$ is always positive (squared)
- $C$ is positive for all bonds
- **Convexity always helps**

**Example (100 bps move):**

**Yields fall 1%:**

$$
\Delta P = -4.27 \times 957.87 \times (-0.01) + \frac{1}{2} \times 23.52 \times 957.87 \times (0.01)^2
$$

$$
= +40.90 + 1.13 = +42.03 \quad (+4.39\%)
$$

**Yields rise 1%:**

$$
\Delta P = -4.27 \times 957.87 \times (+0.01) + \frac{1}{2} \times 23.52 \times 957.87 \times (0.01)^2
$$

$$
= -40.90 + 1.13 = -39.77 \quad (-4.15\%)
$$

**Asymmetry:**

- Upside: +4.39%
- Downside: -4.15%
- Difference: 0.24%
- **Convexity bonus!**

### 4. Term Structure and Economic Expectations

**Duration changes with yield curve:**

**Flat curve (all yields 5%):**
- 2-year bond: Duration ≈ 1.9 years
- 10-year bond: Duration ≈ 7.5 years
- 30-year bond: Duration ≈ 15 years
- **Linear relationship**

**Upward sloping curve:**
- 2-year yield: 3%
- 10-year yield: 5%
- 30-year yield: 6%
- **Duration more spaced out**

**Inverted curve (recession signal):**
- 2-year yield: 5%
- 10-year yield: 4%
- 30-year yield: 4.5%
- Short duration bonds more sensitive
- **Unusual dynamics**

**Economic interpretation:**

**Normal upward curve:**
- Investors demand premium for long-term risk
- Duration ≈ maturity risk
- **Risk compensation**

**Inverted curve:**
- Expect rate cuts (recession)
- Long bonds rally (falling yields)
- Duration strategy: Go long
- **Recessionary positioning**

### 5. Immunization Theory

**Pioneering concept (Redington, 1952):**

Match duration of assets and liabilities to immunize against interest rate risk.

**Pension fund example:**

**Liability:**
- Pay $10M in 8 years (single payment)
- Liability duration: 8 years
- **Fixed obligation**

**Asset strategy:**

**Option 1: Buy 8-year zero-coupon bond**
- Duration: 8 years (exact match)
- Amount: $10M discounted to today
- **Perfect immunization**

**Option 2: Portfolio of bonds**
- Mix of shorter and longer bonds
- Weighted duration: 8 years
- **Also immunized**

**Why immunization works:**

**Parallel shift in yield curve:**

- Yields rise: Bond prices fall (loss)
- But: Reinvestment at higher rates (gain)
- If duration matched: Gains = Losses
- **Net zero impact**

**Yields fall: Opposite**

- Bond prices rise (gain)
- Reinvestment at lower rates (loss)
- If duration matched: Gains = Losses
- **Net zero impact**

**This is profound:**

Portfolio immunized against parallel shifts when:

$$
D_{\text{Assets}} = D_{\text{Liabilities}}
$$

**AND:**

$$
C_{\text{Assets}} \geq C_{\text{Liabilities}}
$$

**(Higher asset convexity preferred for non-parallel shifts)**

---

## Key Terminology

**Yield to Maturity (YTM):**

$$
\text{YTM} = \text{Internal rate of return of bond}
$$

- Discount rate equating PV of cash flows to price
- Assumes reinvestment at YTM (unrealistic)
- Most common yield measure
- **Standard metric**

**Current Yield:**

$$
\text{Current Yield} = \frac{\text{Annual Coupon}}{\text{Price}}
$$

- Income return only
- Ignores capital gain/loss
- Useful for income investors
- **Simple measure**

**Macaulay Duration:**

$$
D_{\text{Mac}} = \frac{\sum t \times PV(CF_t)}{P}
$$

- Weighted average time to cash flows
- Units: Years
- Original duration concept (1938)
- **Time measure**

**Modified Duration:**

$$
D_{\text{Mod}} = \frac{D_{\text{Mac}}}{1+y}
$$

- Price sensitivity to yields
- Units: Percentage per 1% yield change
- **Risk measure**

**Effective Duration:**

$$
D_{\text{Eff}} = \frac{P_{y-\Delta y} - P_{y+\Delta y}}{2 \times P \times \Delta y}
$$

- Numerical derivative (finite difference)
- Handles embedded options (callability)
- More general than modified duration
- **Practical measure**

**Dollar Duration (DV01):**

$$
\text{DV01} = D_{\text{Mod}} \times P \times 0.0001
$$

- Dollar change per 1 bp yield move
- Units: Dollars
- Used for hedging
- **Hedging metric**

**Convexity:**

$$
C = \frac{1}{P} \frac{d^2P}{dy^2}
$$

- Curvature of price-yield relationship
- Always positive for option-free bonds
- Higher for longer maturity
- **Second-order risk**

**Basis Point Value (BPV):**

$$
\text{BPV} = \frac{D_{\text{Mod}} \times P}{10,000}
$$

- Price change per 1 bp yield change
- Same as DV01
- **Hedging metric**

**Dispersion:**

$$
\text{Dispersion} = \frac{\sum (t - D_{\text{Mac}})^2 \times PV(CF_t)}{P}
$$

- Variance of cash flow timing
- Related to convexity
- Higher dispersion = higher convexity
- **Distribution measure**

**Key Rate Duration:**

$$
D_{k} = \frac{\partial P}{\partial y_k}
$$

- Sensitivity to specific maturity point
- Handles non-parallel shifts
- Portfolio immunization tool
- **Curve risk measure**

---

## The Greeks (Bond Risk Metrics)

**Fixed income has its own "Greeks" analogous to options:**

### 1. Delta (Duration)

**Definition:** Price sensitivity to parallel yield curve shifts.

$$
\Delta_{\text{bond}} = -D_{\text{Mod}} \times P
$$

**Example: $10M portfolio of 10-year bonds**

**Characteristics:**
- Modified duration: 7.5 years
- Price: $103 (per $100 face)
- Position: $10M face value

**Delta calculation:**

$$
\Delta = -7.5 \times 10,300,000 = -\$77,250,000
$$

**Interpretation:**

- For 1% (100 bps) yield rise: Loss of 7.5% = $772,500
- For 0.01% (1 bp) yield rise: Loss of 0.075% = $7,725
- **DV01 = $7,725**

**This is like equity delta:**

- Equity delta: $\Delta P / \Delta S$
- Bond delta: $\Delta P / \Delta y$
- **Directional sensitivity**

**Positive duration = Short rates:**

- Long bonds = Short interest rates
- Rates up → Bonds down
- **Inverse relationship**

### 2. Gamma (Convexity)

**Definition:** Rate of change of duration as yields change.

$$
\Gamma_{\text{bond}} = C \times P
$$

**For our $10M portfolio:**

$$
\Gamma = 95 \times 10,300,000 = \$978,500,000
$$

**Interpretation:**

**Small move (10 bps):**

$$
\Delta P = -77,250,000 \times 0.001 + \frac{1}{2} \times 978,500,000 \times (0.001)^2
$$

$$
= -77,250 + 489 = -\$76,761
$$

**Convexity reduced loss by $489**

**Large move (100 bps):**

$$
\Delta P = -77,250,000 \times 0.01 + \frac{1}{2} \times 978,500,000 \times (0.01)^2
$$

$$
= -772,500 + 48,925 = -\$723,575
$$

**Convexity reduced loss by $48,925 (6.3%!)**

**This is like option gamma:**

- Option gamma: $\partial \Delta / \partial S$
- Bond convexity: $\partial D / \partial y$
- **Curvature risk**

**Always positive for bonds:**

- Options can have negative gamma (short positions)
- Bonds ALWAYS have positive convexity
- **Inherent advantage**

### 3. Theta (Carry/Roll-down)

**Definition:** Price change as time passes (assuming unchanged yields).

**Positive theta for premium bonds:**

**Example: Bond trading at $103 (above par)**

- Current: $103
- Maturity: $100 (par)
- Time to maturity: 5 years
- **Gradual decline to par**

**Annual theta:**

$$
\Theta \approx \frac{103 - 100}{5} = \$0.60 \text{ per year}
$$

**Premium bonds pull to par (negative theta)**

**Discount bonds have positive theta:**

**Example: Bond trading at $97**

- Current: $97
- Maturity: $100
- Time to maturity: 5 years

$$
\Theta \approx \frac{100 - 97}{5} = \$0.60 \text{ per year (positive)}
$$

**Roll-down return:**

**If yield curve upward sloping:**

- Buy 10-year bond at 5% yield
- After 1 year → Now 9-year bond
- If 9-year yield = 4.8% (lower on curve)
- Bond appreciates from yield decline
- **Plus coupon income**

**Total return = Coupon + Roll-down + Yield change**

### 4. Vega (Volatility Risk)

**Bonds have no volatility Greek in traditional sense:**

**But analogous concept:**

**Negative convexity from embedded options:**

**Callable bond:**
- Issuer can call if rates fall
- Caps upside
- **Option sold = short vega**

**Mortgage-backed securities (MBS):**
- Homeowners prepay if rates fall
- Negative convexity
- **Short prepayment option**

**Option-free bonds:**
- No vega (no embedded options)
- Convexity always positive
- **Pure exposure**

### 5. Rho (Level Risk)

**In bonds, rho = duration:**

- Interest rate is the underlying
- Duration measures rate sensitivity
- **Primary risk factor**

**All bond Greeks collapse to duration/convexity!**

---

## Strategy Selection

**Different duration strategies for different views:**

### 1. Long Duration (Bullish on Bonds)

**When to use:**

**Expect falling rates:**
- Recession fears
- Disinflation/deflation
- Fed rate cuts anticipated
- **Bullish bonds**

**Implementation:**

**Buy long-maturity bonds:**
- 20-30 year Treasuries
- Duration: 15-20 years
- Maximum sensitivity
- **TLT ETF or long bond futures**

**Example: 30-year Treasury**

- Price: $100
- YTM: 4.5%
- Duration: 18 years
- **High sensitivity**

**Rate scenario (100 bp decline):**

$$
\Delta P = -18 \times 100 \times (-0.01) = +18\%
$$

**Potential gain: +18% on 1% rate decline**

**Risk:**

- If rates rise 1%: -18%
- **Symmetrically risky**

**Historical performance:**

- 2008 crisis: Long bonds +34% (rates crashed)
- 2020 COVID: Long bonds +21%
- **Crisis hedge**

### 2. Short Duration (Bearish on Bonds)

**When to use:**

**Expect rising rates:**
- Economic growth accelerating
- Inflation rising
- Fed tightening cycle
- **Bearish bonds**

**Implementation:**

**Short long-maturity bonds:**
- Sell TLT ETF
- Short bond futures
- **Or buy inverse ETF (TMV)**

**Or rotate to short-duration:**
- 1-3 year Treasuries
- Duration: 1-2 years
- Minimal sensitivity
- **Defensive**

**Example: 2-year Treasury**

- Price: $100
- YTM: 4.5%
- Duration: 1.9 years
- **Low sensitivity**

**Rate scenario (100 bp rise):**

$$
\Delta P = -1.9 \times 100 \times 0.01 = -1.9\%
$$

**Small loss despite 1% rate rise**

**2022 example:**

- Long bonds (TLT): -40% (rates rose 2.5%)
- Short duration: -5%
- **Duration protected**

### 3. Barbell Strategy (High Convexity)

**Structure:**

$$
\text{Barbell} = 50\% \text{ Short Duration} + 50\% \text{ Long Duration}
$$

**Example:**

- 50% in 2-year Treasuries (Duration 1.9)
- 50% in 30-year Treasuries (Duration 18)
- **Weighted duration: 10 years**

**Comparison to bullet:**

- 100% in 10-year Treasury (Duration 8.5)
- **Same duration as barbell**

**But convexity differs:**

**Barbell convexity:**

- 2-year convexity: 5
- 30-year convexity: 350
- Weighted: 177.5
- **Higher convexity**

**Bullet convexity:**

- 10-year convexity: 95
- **Much lower**

**Performance comparison:**

**Large rate moves (±1%):**

- Barbell benefits from convexity
- Outperforms bullet
- **Convexity advantage**

**Small moves (±10 bps):**

- Similar performance
- Duration dominates
- **Neutral**

**Cost:**

- Barbell has lower yield (concave curve)
- Sacrifice ~10-20 bps yield
- **Convexity premium paid**

### 4. Bullet Strategy (Maximum Yield)

**Structure:**

$$
\text{Bullet} = 100\% \text{ in single maturity}
$$

**Example:**

- 100% in 10-year Treasuries
- Duration: 8.5 years
- Convexity: 95
- **Concentrated**

**Advantage:**

- Maximum yield for duration
- Simple to manage
- **Yield maximization**

**Disadvantage:**

- Lower convexity
- Underperforms in volatile markets
- **Less optionality**

### 5. Ladder Strategy (Cash Flow Matching)

**Structure:**

$$
\text{Ladder} = \text{Equal amounts in each maturity}
$$

**Example: 10-year ladder**

- 10% in 1-year bonds
- 10% in 2-year bonds
- ...
- 10% in 10-year bonds
- **Evenly distributed**

**Duration:**

$$
D_{\text{ladder}} = \frac{1 + 2 + \cdots + 10}{10} = 5.5 \text{ years}
$$

**Advantages:**

- Reinvestment risk reduced
- Annual maturities provide liquidity
- Rate averaging over time
- **Stability**

**Disadvantages:**

- Moderate convexity
- Not optimized for rate view
- **Neutral positioning**

### 6. Comparison Table

| Strategy | Duration | Convexity | Yield | Best For |
|----------|----------|-----------|-------|----------|
| Long Duration | High (15-20) | High (300+) | Low | Falling rates |
| Short Duration | Low (1-2) | Low (5-10) | Varies | Rising rates |
| Barbell | Medium (8-10) | Very High (150-200) | Medium-Low | Volatility |
| Bullet | Medium (8-10) | Medium (80-100) | High | Yield maximization |
| Ladder | Medium (5-6) | Medium (50-70) | Medium | Cash flow matching |

**Beginner recommendation: Ladder (diversified, stable, easy to understand)**

---

## Time Selection

**Duration management is tactical:**

### 1. Economic Cycle Timing

**Recession → Recovery:**

**Early recession:**
- Extend duration (long bonds rally)
- Fed cuts rates
- Flight to quality
- **Bullish bonds**

**Late recession → Early recovery:**
- Maintain long duration
- Fed on hold (low rates)
- Growth still weak
- **Still bullish**

**Mid recovery:**
- Reduce duration
- Fed considering hikes
- Growth accelerating
- **Neutral to bearish**

**Late cycle:**
- Minimum duration
- Fed hiking actively
- Inflation rising
- **Bearish bonds**

**Example: 2007-2010**

**2007 (late cycle):**
- Short duration (1-3 years)
- Rates at 5%+
- **Defensive**

**2008 (crisis):**
- Extend duration (10-20 years)
- Fed cutting to zero
- Long bonds +34%
- **Perfect timing**

**2009-2010 (recovery):**
- Maintain long duration
- Fed at zero, QE ongoing
- Still profitable
- **Extended position**

### 2. Federal Reserve Policy

**Fed tightening cycle:**

$$
\text{Fed Hiking} \Rightarrow \text{Shorten Duration}
$$

**Indicators:**

- FOMC minutes hawkish
- Dot plot showing hikes
- CPI >2% (inflation target)
- Unemployment <4% (tight labor)
- **Bearish bonds**

**Example: 2022-2023**

- Fed hiked 5.25% (from 0%)
- Long bonds -40%
- Should have been in 1-3 year bonds
- **Catastrophic for long duration**

**Fed easing cycle:**

$$
\text{Fed Cutting} \Rightarrow \text{Extend Duration}
$$

**Indicators:**

- Yield curve inversion (recession signal)
- Weakening economic data
- Inflation falling
- Fed forward guidance dovish
- **Bullish bonds**

**Example: 2019**

- Fed cut rates 3× (Aug, Sep, Oct)
- Long bonds +15%
- Extend duration worked
- **Profitable**

### 3. Inflation Regime

**High inflation (>3%):**

$$
\text{Inflation Rising} \Rightarrow \text{Shorten Duration}
$$

**Real yields eroded:**

- Nominal bond returns eaten by inflation
- Need inflation-protected (TIPS)
- Or very short duration
- **Bearish nominal bonds**

**Low inflation (<2%):**

$$
\text{Disinflation} \Rightarrow \text{Extend Duration}
$$

**Real yields attractive:**

- Nominal returns preserved
- Central banks may cut (support)
- Deflation risk → bond rally
- **Bullish bonds**

### 4. Yield Curve Signals

**Inverted curve:**

$$
\text{2-year yield} > \text{10-year yield} \Rightarrow \text{Recession warning}
$$

**Action:**

- Extend duration (anticipate Fed cuts)
- Recession → Flight to quality
- **Bullish long bonds**

**Steep curve:**

$$
\text{10-year yield} - \text{2-year yield} > 200 \text{ bps}
$$

**Action:**

- Normal environment
- Carry trade profitable (borrow short, lend long)
- **Neutral to bullish**

**Flattening curve:**

$$
\text{Spread narrowing over time}
$$

**Action:**

- Economic concerns building
- Consider extending duration
- **Transition to bullish**

---

## Maximum Profit and Loss

### 1. Long Duration Trade (2008 Crisis)

**Setup:**

- Date: September 15, 2008 (Lehman collapse)
- Position: Long $1M 30-year Treasuries
- Yield: 4.5%
- Price: $100
- Modified duration: 18 years

**The rally:**

**September 2008 → March 2009:**

- Yields: 4.5% → 3.0% (-150 bps)
- Economic collapse
- Fed cuts to zero
- **Maximum flight to quality**

**Price change estimate:**

$$
\Delta P = -18 \times 100 \times (-0.015) + \frac{1}{2} \times 350 \times 100 \times (0.015)^2
$$

$$
= +27.0 + 3.94 = +30.94\%
$$

**Actual price:**

- September: $100
- March 2009: $133
- Actual gain: **+33%**
- **(Duration + convexity underestimated slightly)**

**Profit:**

$$
\$1,000,000 \times 0.33 = \$330,000
$$

**In 6 months → Annualized: +66%**

**Maximum Loss (2022 Rate Hikes):**

**Setup:**

- Date: January 2022
- Position: Long $1M 30-year Treasuries
- Yield: 2.0%
- Price: $100
- Duration: 18 years

**The disaster:**

**January 2022 → October 2022:**

- Yields: 2.0% → 4.5% (+250 bps!)
- Fed hiked 425 bps in 9 months
- Inflation 9%
- **Worst bond market in 40 years**

**Price change:**

$$
\Delta P = -18 \times 100 \times 0.025 + \frac{1}{2} \times 350 \times 100 \times (0.025)^2
$$

$$
= -45.0 + 10.94 = -34.06\%
$$

**Actual price:**

- January: $100
- October: $65
- Actual loss: **-35%**

**Loss:**

$$
\$1,000,000 \times (-0.35) = -\$350,000
$$

**Devastating for buy-and-hold**

### 2. Duration-Neutral Barbell (Volatility Play)

**Setup:**

- Portfolio: $2M
- Strategy: Barbell vs Bullet (both 10-year duration)

**Barbell:**

- $1M in 2-year bonds (Duration 1.9, Convexity 5)
- $1M in 30-year bonds (Duration 18, Convexity 350)
- Weighted duration: 9.95 ≈ 10
- Weighted convexity: 177.5

**Bullet:**

- $2M in 10-year bonds (Duration 8.5, Convexity 95)
- **Lower convexity**

**Scenario: Large rate volatility**

**Yields fall 100 bps:**

**Barbell P&L:**

- 2-year: $1M × (-1.9 × -0.01 + 0.5 × 5 × 0.01²) = +$19,025
- 30-year: $1M × (-18 × -0.01 + 0.5 × 350 × 0.01²) = +$197,500
- Total: +$216,525

**Bullet P&L:**

- 10-year: $2M × (-8.5 × -0.01 + 0.5 × 95 × 0.01²) = +$179,500

**Barbell outperformance: $37,025 (20% better!)**

**Yields rise 100 bps:**

**Barbell P&L:**

- 2-year: $1M × (-1.9 × 0.01 + 0.5 × 5 × 0.01²) = -$18,975
- 30-year: $1M × (-18 × 0.01 + 0.5 × 350 × 0.01²) = -$162,500
- Total: -$181,475

**Bullet P&L:**

- 10-year: $2M × (-8.5 × 0.01 + 0.5 × 95 × 0.01²) = -$160,500

**Barbell underperformance: -$20,975**

**But:**

- Upside: +20% better
- Downside: -13% worse
- **Asymmetric in barbell's favor**

**This is convexity value!**

---

## When to Use Duration/Convexity Analysis

### 1. Ideal Applications

**Use duration when:**

**1. Portfolio hedging:**

- Need to immunize interest rate risk
- Match asset/liability durations
- Pension fund management
- **Classic application**

**2. Relative value trading:**

- Compare bonds with similar duration
- Identify mispriced securities
- Spread trades (corporates vs Treasuries)
- **Security selection**

**3. Interest rate forecasting:**

- Bullish rates → Extend duration
- Bearish rates → Shorten duration
- Tactical allocation
- **Active management**

**4. Risk budgeting:**

- Allocate risk across portfolios
- DV01 limits
- VaR calculations
- **Risk management**

**Use convexity when:**

**1. Volatile rate environment:**

- Expect large rate moves
- Direction uncertain
- Convexity provides edge
- **Volatility play**

**2. Barbell vs bullet decisions:**

- Sacrifice yield for convexity
- Expected volatility high
- Long-term positioning
- **Structure optimization**

**3. MBS/callable bond analysis:**

- Negative convexity (bad)
- Avoid in volatile markets
- **Option-adjusted analysis**

**4. Immunization refinement:**

- Match convexity as well as duration
- Better protection against non-parallel shifts
- **Advanced hedging**

### 2. Specific Use Cases

**Use Case 1: Pension fund liability matching**

**Liability:**
- Pay $500M in 15 years
- Liability duration: 15 years
- **Fixed obligation**

**Asset strategy:**

- Buy bonds with 15-year duration
- Mix of maturities (barbell)
- Higher convexity preferred
- **Immunization**

**Result:**

- Parallel shifts: Matched
- Non-parallel shifts: Convexity helps
- **Hedged**

**Use Case 2: Rate view expression**

**View: Fed cutting rates next 12 months**

**Strategy:**

- Extend portfolio duration 10 → 15 years
- Rotate from 5-7 year to 20-30 year
- Increase rate sensitivity
- **Directional bet**

**Result:**

- Rates fall 1%: Portfolio +15%
- Rates rise 1%: Portfolio -15%
- **Leveraged expression**

**Use Case 3: Yield curve steepener**

**View: Curve will steepen (long - short widens)**

**Strategy:**

- Long 30-year bonds (Duration 18)
- Short 2-year bonds (Duration 1.9)
- Net duration: Depends on weighting
- **Curve trade**

**Example:**

- Long $10M 30-year
- Short $10M 2-year

**Scenario (curve steepens 50 bps):**

- 30-year yield -25 bps: +$450k
- 2-year yield +25 bps: -$47.5k
- Net: +$402.5k
- **Profitable**

---

## When NOT to Use Duration/Convexity

### 1. Limitations and Failures

**Avoid duration-only analysis when:**

**1. Large rate moves expected:**

$$
\text{If } |\Delta y| > 200 \text{ bps} \Rightarrow \text{Convexity essential}
$$

**Duration alone:**

- Accurate for small moves (±50 bps)
- Increasingly inaccurate beyond ±100 bps
- Convexity required
- **Linear approximation breaks down**

**2. Embedded options present:**

**Callable bonds:**

- Negative convexity when rates fall
- Duration extends (bad!)
- Use option-adjusted metrics
- **Standard duration misleading**

**MBS:**

- Prepayment risk
- Negative convexity at low rates
- Effective duration required
- **Modified duration wrong**

**3. Non-parallel yield curve shifts:**

**Twist scenario:**

- Short end +100 bps
- Long end -50 bps
- **Portfolio duration meaningless**

**Better: Key rate durations**

$$
\Delta P = \sum_{i} D_i \times \Delta y_i
$$

**4. Credit risk dominant:**

**Corporate bonds in crisis:**

- Credit spreads exploding
- Duration irrelevant
- Default risk primary
- **Interest rate risk secondary**

**Example: 2008**

- Lehman bonds: Credit risk 100%
- Treasury duration: Worked perfectly
- **Asset class matters**

**5. Inflation volatility high:**

**Nominal bonds:**

- Real return = Nominal return - Inflation
- If inflation volatile, real return uncertain
- Duration measures nominal risk only
- **Real duration needed (TIPS)**

### 2. Warning Signs to Avoid

**1. Extremely low yields:**

$$
\text{If } y < 1\% \Rightarrow \text{Convexity math breaks}
$$

**Japan 2016:**

- Yields negative (-0.1%)
- Duration infinite at zero
- Mathematical issues
- **Avoid zero bound**

**2. Illiquid bonds:**

- Theoretical duration vs trading reality
- Cannot hedge at model prices
- Bid-ask spreads dominate
- **Liquidity premium required**

**3. Currency mismatch:**

**US investor holding Japanese bonds:**

- Duration measures JGB yield risk
- But currency risk may dominate
- USD/JPY volatility > yield moves
- **FX risk primary**

**4. Leverage constraints:**

**Repo market stress:**

- Cannot borrow to hedge
- Leverage unavailable
- Duration hedge impossible
- **Funding risk**

---

## Position Sizing and Risk Management

### 1. The Golden Rule

**Position sizing by DV01:**

$$
\text{Position Size} = \frac{\text{Risk Budget (dollars)}}{\text{DV01 per bond}}
$$

**Example:**

**Portfolio: $10M**

**Risk budget: 0.5% per day (1σ)**

$$
\text{Daily Risk} = \$10M \times 0.005 = \$50,000
$$

**Bond characteristics:**

- 10-year Treasury
- DV01: $850 per $1M face
- **Sensitivity known**

**Position sizing:**

$$
\text{Max Position} = \frac{\$50,000}{\$850} = \$58.8M \text{ face value}
$$

**This is 5.88× leverage!**

**But:**

- Uses full risk budget
- No diversification
- **Aggressive**

**Conservative: Use 50% of budget**

$$
\text{Position} = \frac{\$25,000}{\$850} = \$29.4M \text{ face}
$$

**2.94× leverage, more prudent**

### 2. Portfolio Duration Management

**Target duration approach:**

$$
D_{\text{portfolio}} = \sum w_i D_i = D_{\text{target}}
$$

**Example: Target 5-year duration**

**Current portfolio:**

| Asset | Weight | Duration | Contribution |
|-------|--------|----------|--------------|
| 2-year | 30% | 1.9 | 0.57 |
| 5-year | 40% | 4.5 | 1.80 |
| 10-year | 30% | 8.5 | 2.55 |

$$
D_{\text{current}} = 0.57 + 1.80 + 2.55 = 4.92 \text{ years}
$$

**Close to target (5 years), no adjustment needed**

**If target changes to 7 years:**

**Action:**

- Reduce 2-year: 30% → 20%
- Increase 10-year: 30% → 40%
- Keep 5-year: 40%

**New duration:**

$$
D_{\text{new}} = 0.20 \times 1.9 + 0.40 \times 4.5 + 0.40 \times 8.5 = 6.98 \approx 7
$$

**Rebalanced to target**

### 3. Hedging with Futures

**Treasury futures for duration hedging:**

**Example: Long $100M corporate bonds**

**Characteristics:**

- Corporate duration: 7.2 years
- DV01: $7,200 per $1M face
- Total DV01: $720,000
- **Want to hedge rate risk**

**10-year Treasury futures:**

- Duration: 8.5 years
- DV01: $85 per contract
- **Hedging instrument**

**Hedge ratio:**

$$
\text{Contracts} = \frac{\text{Portfolio DV01}}{\text{Futures DV01}} = \frac{720,000}{85} = 8,471 \text{ contracts}
$$

**Round to 8,500 contracts short**

**Result:**

- Rates rise 1%: Corporate bonds -$7.2M
- Rates rise 1%: Futures gain +$7.225M
- Net: +$25k (slight overhedge)
- **Hedged!**

**Beta adjustment:**

$$
\text{Hedge Ratio} = \frac{\text{Portfolio DV01}}{\text{Futures DV01}} \times \beta
$$

Where $\beta$ = correlation between corporates and Treasuries

**If β = 0.85:**

$$
\text{Contracts} = 8,471 \times 0.85 = 7,200
$$

**Partial hedge (credit spread risk remains)**

### 4. Convexity Budgeting

**Allocate convexity across portfolio:**

**Example: $500M multi-asset fund**

**Convexity targets:**

- Treasuries: 80 (per $100 face)
- Corporates: 60 (lower convexity)
- MBS: -20 (negative convexity!)
- **Weighted average target: 50**

**Current allocation:**

| Asset | Weight | Convexity | Contribution |
|-------|--------|-----------|--------------|
| Treasuries | 50% | 80 | 40 |
| Corporates | 30% | 60 | 18 |
| MBS | 20% | -20 | -4 |

$$
C_{\text{portfolio}} = 40 + 18 - 4 = 54
$$

**Above target (good!), positive convexity**

**Adjustment if too low:**

- Reduce MBS (negative convexity)
- Increase Treasuries (positive convexity)
- Or use barbell (high convexity)
- **Optimization**

### 5. Stop-Loss Strategies

**Duration-based stop:**

$$
\text{If Loss} > D_{\text{Mod}} \times P \times 0.5\% \Rightarrow \text{Review position}
$$

**Example: 10-year bond position**

- Modified duration: 8.5 years
- Position: $10M
- Stop level: 8.5 × $10M × 0.005 = $425k

**If rates rise 50 bps:**

- Loss: $425k
- **Trigger stop review**

**Action:**

- Reduce position 50%
- Or hedge with futures
- **Risk management**

### 6. Example

**Portfolio: $100M pension fund**

**Liability: $100M due in 10 years**

**Immunization strategy:**

**Step 1: Match duration**

- Liability duration: 10 years
- Asset target duration: 10 years

**Step 2: Asset allocation**

| Asset | Amount | Duration | DV01 | Convexity |
|-------|--------|----------|------|-----------|
| 5-year | $30M | 4.5 | $1,350k | $1,200k |
| 10-year | $40M | 8.5 | $3,400k | $3,800k |
| 20-year | $30M | 15 | $4,500k | $13,500k |

**Portfolio metrics:**

$$
D_{\text{portfolio}} = \frac{1,350 + 3,400 + 4,500}{10,000} = 9.5 \text{ years}
$$

**Close to target (10 years)**

$$
C_{\text{portfolio}} = \frac{1,200 + 3,800 + 13,500}{1,000} = 185
$$

**High convexity (good!)**

**Step 3: Rebalancing rules**

$$
\text{If } |D_{\text{portfolio}} - D_{\text{target}}| > 0.5 \Rightarrow \text{Rebalance}
$$

**Quarterly review, annual major rebalancing**

**Step 4: Risk limits**

- Maximum daily loss: $500k (0.5%)
- DV01 limit: $1M (100 bps = 1% loss)
- Current DV01: $925k
- **Within limits**

**Result:**

- Parallel shifts: Immunized
- Non-parallel shifts: Convexity helps
- Crisis protection: High convexity
- **Well-managed**

---

## Common Mistakes Beginners Make

### 1. Mistake #1

**The error:**

- Calculate price change using duration only
- Large yield move (200 bps)
- Convexity effect 15% of total
- **Underestimate significantly**

**Example:**

**Bond: Duration 10, Convexity 120**

**Yield falls 2%:**

**Duration-only estimate:**

$$
\Delta P = -10 \times (-0.02) = +20\%
$$

**Actual with convexity:**

$$
\Delta P = -10 \times (-0.02) + \frac{1}{2} \times 120 \times (0.02)^2 = +20\% + 2.4\% = +22.4\%
$$

**Error: 2.4% absolute (10% relative)**

**Correct approach:**

- Always include convexity for moves >50 bps
- Essential for accuracy
- **Both terms matter**

### 2. Mistake #2

**The error:**

- Callable bond has embedded option
- Use standard modified duration
- **Wrong metric**

**Example: Callable bond**

- Modified duration: 7 years
- But if rates fall, issuer calls
- Effective duration: 3 years (much lower!)
- **Negative convexity**

**What happens:**

**Rates fall 1%:**

**Expected (using modified duration):**

$$
\Delta P = -7 \times (-0.01) = +7\%
$$

**Actual:**

$$
\Delta P = +2\% \quad \text{(capped by call price)}
$$

**Disappointed investor!**

**Correct approach:**

- Use effective duration (option-adjusted)
- Account for call option
- **OAS analysis**

### 3. Mistake #3

**The error:**

- Duration assumes parallel yield curve shift
- Actual shifts often non-parallel
- **Steepening/flattening missed**

**Example: Curve steepener**

**Portfolio: 100% 10-year bonds**

- Duration: 8.5 years
- **Single maturity**

**Scenario:**

- 2-year yield: +100 bps
- 10-year yield: +50 bps
- 30-year yield: 0 bps
- **Curve flattening**

**Expected loss (assuming parallel +50 bps avg):**

$$
\Delta P = -8.5 \times 0.005 = -4.25\%
$$

**Actual loss (10-year moved +50 bps):**

$$
\Delta P = -8.5 \times 0.005 = -4.25\%
$$

**Lucky! Parallel assumption happened to work**

**But if held 30-year:**

- Expected: -4.25%
- Actual: 0% (yields unchanged)
- **Big difference**

**Correct approach:**

- Use key rate durations
- Model non-parallel shifts
- **Curve risk explicit**

### 4. Mistake #4

**The error:**

- Buy premium bond at $110
- Hold to maturity
- Expect $110 at maturity
- **Nope! Only get $100**

**Example: 5-year bond @ $110**

- Annual pull-to-par: -$2/year
- This is negative theta
- **Reduces total return**

**Total return calculation:**

- Coupon income: +$60 (5 years × $12)
- Pull-to-par: -$10
- Net: +$50
- Yield: Much lower than coupon suggests
- **Hidden cost**

**Correct approach:**

- Calculate YTM (includes pull-to-par)
- Don't rely on current yield alone
- **Total return focus**

### 5. Mistake #5

**The error:**

- Short-duration bond (Duration 2)
- Think "low risk, can leverage 10×"
- Leverage to 10× position
- **Concentration risk**

**What happens:**

**Credit event:**

- Rates unchanged (duration fine)
- But credit spread widens 200 bps
- Loss: 20% on bond
- With 10× leverage: -200%
- **Wiped out**

**Correct approach:**

- Duration measures rate risk only
- Credit risk, liquidity risk remain
- Leverage conservatively
- **Holistic risk view**

### 6. Mistake #6

**The error:**

- All bonds have positive convexity, right?
- **Wrong! Callable bonds and MBS have negative**

**Example: MBS in low-rate environment**

**Rates fall 100 bps:**

- Expected (positive convexity): Big gains
- Actual: Small gains (prepayment accelerates)
- **Negative convexity**

**Rates rise 100 bps:**

- Expected: Small losses (positive convexity)
- Actual: Big losses (prepayment stops)
- **Inverse of normal bonds**

**Correct approach:**

- Check for embedded options
- Negative convexity = bad
- Avoid in volatile markets
- **Convexity sign matters**

### 7. Mistake #7

**The error:**

- Macaulay duration: 5.0 years
- Use in price change formula
- **Wrong duration measure**

**Correct:**

$$
\frac{\Delta P}{P} = -D_{\text{Mod}} \times \Delta y
$$

**NOT Macaulay!**

**Modified duration:**

$$
D_{\text{Mod}} = \frac{D_{\text{Mac}}}{1+y} = \frac{5.0}{1.05} = 4.76
$$

**Error magnitude:**

- 10% yield: 5% vs 4.76% (4.8% error)
- Small but compounds
- **Use correct measure**

### 8. Mistake #8

**The error:**

- Bond pays semi-annual coupons
- Calculate duration using annual formula
- **Frequency mismatch**

**Semi-annual bonds:**

$$
D_{\text{Mod}} = \frac{D_{\text{Mac}}}{1 + y/2}
$$

**Annual bonds:**

$$
D_{\text{Mod}} = \frac{D_{\text{Mac}}}{1 + y}
$$

**Different!**

**Correct approach:**

- Match frequency to coupon payments
- Semi-annual most common in US
- **Consistency essential**

### 9. Mistake #9

**The error:**

- Calculate duration at purchase
- Never update
- Years later, duration changed significantly
- **Stale metric**

**Example:**

- Bought 10-year bond (Duration 8.5)
- 5 years pass
- Now 5-year bond (Duration 4.5)
- Portfolio duration drifted
- **Unintended positioning**

**Correct approach:**

- Recalculate duration monthly
- Rebalance to target
- **Active management**

### 10. Mistake #10

**The error:**

- Corporate bond
- Calculate Treasury-based duration
- Credit spread moves ignored
- **Incomplete analysis**

**Example:**

**Investment-grade corporate:**

- Treasury duration: 7 years
- Credit spread duration: 7 years
- Total duration: 14 years (effectively)
- **Both components matter**

**Scenario:**

- Treasury yields flat
- Credit spreads widen 50 bps
- Loss: 7 × 0.005 = 3.5%
- **Duration applied to spread too**

**Correct approach:**

- Recognize spread duration
- Corporate bond has two risk factors
- **Dual duration framework**

---

## Best Case Scenario

### 1. The Perfect Duration Trade (2008 Crisis)

**Trader profile:**

- Experience: 15 years fixed income
- Capital: $50M
- Strategy: Duration extension ahead of crisis
- Discipline: Excellent

**Setup (June 2008):**

**Early warning signals:**

- Housing market collapsing
- Bear Stearns rescued (March)
- Credit spreads widening
- Fed still at 2% (too high)
- **Recession imminent**

**Analysis:**

- Fed will cut to 0-0.25%
- Flight to quality coming
- Long duration will benefit massively
- **Extend duration**

**Position (July 1, 2008):**

**Before:**

- 50% 5-year Treasuries (Duration 4.5)
- 50% 10-year Treasuries (Duration 8.5)
- Portfolio duration: 6.5 years
- **Moderate duration**

**After (extended):**

- 100% 30-year Treasuries
- Price: $100
- YTM: 4.5%
- Duration: 18 years
- **Maximum extension**

**Trade progression:**

**July-September 2008:**

- Yields: 4.5% → 4.2%
- Small gains: +5.4%
- **Early positioning profitable**

**September 15, 2008 (Lehman collapse):**

**Panic:**

- Yields: 4.2% → 3.5% (in days)
- Flight to quality
- Price gains: Additional +12.6%
- **Crisis accelerates**

**October-December 2008:**

- Fed cuts to 0%
- QE1 announced
- Yields: 3.5% → 3.0%
- Additional gains: +9.0%
- **Maximum rally**

**Total return (July-December):**

$$
\text{Total} = 5.4\% + 12.6\% + 9.0\% = 27.0\%
$$

**Plus coupon income: +2.25% (half-year)**

$$
\text{Final return} = 29.25\% \quad \text{in 6 months}
$$

**On $50M:**

$$
\text{Profit} = \$50M \times 0.2925 = \$14.625M
$$

**Annualized: +58.5%**

**vs equities:**

- S&P 500 (July-Dec 2008): -30%
- **Absolute and relative outperformance**

**Why this worked perfectly:**

1. ✅ Anticipated Fed cuts (recession)
2. ✅ Extended to maximum duration (30-year)
3. ✅ Timed entry before crisis peak
4. ✅ High convexity position (benefited from large moves)
5. ✅ Flight to quality amplified gains
6. ✅ Held through volatility
7. ✅ Perfect risk management
8. **Textbook execution**

**Exit (March 2009):**

- Yields bottomed at 2.5%
- Sold 50% at $140 (+40% from entry)
- Rotated to credit (recovery trade)
- **Tactical rebalancing**

---

## Worst Case Scenario

### 1. The Duration Disaster

**Trader profile:**

- Experience: 3 years
- Capital: $10M
- Strategy: "Bonds always safe"
- Discipline: Poor

**Setup (January 2022):**

**Misguided thinking:**

- "Bonds have gone up for 40 years"
- "Duration = safety"
- "Fed won't really hike much"
- **Normalcy bias**

**Position (January 3, 2022):**

**Concentrated long duration:**

- 100% in 30-year Treasuries
- Price: $100
- YTM: 2.0%
- Duration: 18 years
- Convexity: 350
- **Maximum duration exposure**

**Ignored warnings:**

- Inflation at 7% (highest in 40 years)
- Fed signaling hikes
- Real yields deeply negative
- **All red flags**

**The disaster:**

**Q1 2022 (January-March):**

- Fed hikes 25 bps (March)
- Yields: 2.0% → 2.5% (+50 bps)
- Price change: -9%
- Portfolio: $10M → $9.1M
- **Ouch, but holding**

**Q2 2022 (April-June):**

- Fed hikes 50 bps + 75 bps (unprecedented)
- Yields: 2.5% → 3.5% (+100 bps)
- Price change: Additional -18%
- Portfolio: $9.1M → $7.46M
- **Getting painful**

**Q3 2022 (July-September):**

- Fed hikes another 150 bps
- Yields: 3.5% → 4.0% (+50 bps)
- Price change: Additional -9%
- Portfolio: $7.46M → $6.79M
- **Catastrophic**

**Q4 2022 (October-December):**

- Fed continues hiking
- Yields: 4.0% → 4.5% (+50 bps)
- Price change: Additional -9%
- Portfolio: $6.79M → $6.18M
- **Worst bond year in history**

**Total devastation:**

**Final position:**

- Starting: $10.0M
- Ending: $6.18M
- Loss: **-$3.82M (-38.2%)**

**Actual price:**

- January: $100
- December: $62
- **38% decline in "safe" Treasuries**

**Comparison:**

- S&P 500 (2022): -18%
- Bonds WORSE than stocks!
- **"Safe" bonds destroyed portfolio**

**What went catastrophically wrong:**

1. ❌ Ignored inflation (7% CPI)
2. ❌ Ignored Fed hawkish signals
3. ❌ Maximum duration at worst time
4. ❌ No stop-loss discipline
5. ❌ Concentrated position (100% long bonds)
6. ❌ "Bonds always safe" fallacy
7. ❌ Ignored negative real yields
8. ❌ No diversification
9. **Complete strategy failure**

**Emotional journey:**

**Q1:** "Just volatility, bonds recover"

**Q2:** "Down 25%, can't sell now"

**Q3:** "This is unprecedented, must end soon"

**Q4:** "Everything is lost"

**What should have been done:**

**January 2022 (Fed signals hikes):**

- Exit long duration immediately
- Rotate to short duration (1-3 years)
- Or even cash
- **Defensive positioning**

**Alternative allocation:**

- 50% Short-duration bonds (Duration 2)
- 30% TIPS (inflation protection)
- 20% Cash

**Hypothetical 2022 performance:**

- Short bonds: -4%
- TIPS: -12% (also suffered but better)
- Cash: +1% (rising rates helped)
- Weighted: -5.4%
- **vs -38.2% actual**

**Saved 32.8%!**

**Lessons:**

- Duration is two-sided risk
- "Safe" bonds can crash
- Monitor rate environment always
- Fed policy dominates everything
- **Risk management essential**

---

## What to Remember

### 1. Core Concept

**Price-yield inverse relationship quantified by duration and convexity:**

$$
\Delta P = -D_{\text{Mod}} \times P \times \Delta y + \frac{1}{2} C \times P \times (\Delta y)^2
$$

- Duration: First-order (linear) sensitivity
- Convexity: Second-order (curvature) effect
- Both essential for accurate pricing
- **Mathematical framework**

### 2. Key Formulas

**Bond pricing:**

$$
P = \sum_{t=1}^{N} \frac{C}{(1+y)^t} + \frac{F}{(1+y)^N}
$$

**Modified duration:**

$$
D_{\text{Mod}} = \frac{D_{\text{Mac}}}{1+y}
$$

**Convexity:**

$$
C = \frac{1}{P(1+y)^2} \sum CF_t \times t(t+1) \times (1+y)^{-t}
$$

**DV01:**

$$
\text{DV01} = D_{\text{Mod}} \times P \times 0.0001
$$

### 3. Duration Drivers

**Increases with:**

- Longer maturity ↑
- Lower coupon ↓
- Lower yield ↓
- **More sensitive bonds**

**Zero-coupon bond:**

- Duration = Maturity (maximum)
- **Pure time exposure**

### 4. Convexity Properties

**Always positive for option-free bonds:**

- Yields fall: Price rises more (convexity helps)
- Yields rise: Price falls less (convexity helps)
- **Beneficial asymmetry**

**Higher convexity = better:**

- Longer maturity
- Lower coupon
- Lower yield
- **Valuable optionality**

### 5. Strategy Applications

**Extend duration when:**

- Expect falling rates (recession)
- Fed cutting/QE
- Flight to quality likely
- **Bullish bonds**

**Shorten duration when:**

- Expect rising rates (growth/inflation)
- Fed hiking
- Risk-on environment
- **Bearish bonds**

**Barbell strategy:**

- Maximize convexity
- Sacrifice yield (10-20 bps)
- Benefits from volatility
- **Optionality play**

### 6. Risk Management

**Position sizing:**

$$
\text{Max Position} = \frac{\text{Risk Budget}}{\text{DV01}}
$$

**Hedging:**

- Match duration (assets = liabilities)
- Include convexity for refinement
- Use futures for tactical hedges
- **Immunization**

**Portfolio limits:**

- DV01 limits (dollar risk per bp)
- Duration range targets
- Convexity minimums
- **Risk budgeting**

### 7. Common Mistakes

1. Ignoring convexity (large moves)
2. Using modified duration for callables
3. Assuming parallel yield shifts
4. Forgetting pull-to-par
5. Over-leveraging (duration ≠ total risk)
6. Ignoring convexity sign (negative = bad)
7. Mixing Macaulay and Modified
8. Wrong coupon frequency
9. Static duration (not updating)
10. Ignoring credit duration

### 8. Maximum Returns

**Best case (2008):**

- Extended to 30-year bonds
- Duration 18, Convexity 350
- Rates fell 150 bps
- Return: +29.25% (6 months)
- **Perfect timing**

**Worst case (2022):**

- Long 30-year bonds
- Rates rose 250 bps
- Loss: -38.2%
- **Duration disaster**

### 9. Success Factors

**Three pillars:**

1. **Understanding** (math + economics)
2. **Measurement** (accurate duration/convexity)
3. **Management** (active positioning)

**Formula:**

$$
\text{Success} = \text{Knowledge} \times \text{Discipline} \times \text{Timing}
$$

### 10. Final Wisdom

> "Duration and convexity are the foundation of all fixed income analysis—duration quantifies linear interest rate risk (first derivative), while convexity captures the valuable curvature that makes bonds superior to linear instruments (second derivative). Every bond investor must master these metrics: a 10-year bond with duration 8.5 will lose 8.5% when yields rise 100 bps, but convexity of 95 adds back +0.5%, creating asymmetry that favors long positions. This mathematics enabled pension funds to immunize liabilities since 1952 (Redington), guided institutional portfolios through rate cycles, and quantified the exact risk-return trade-offs in barbell vs bullet strategies. But mathematics alone isn't enough—2022 proved that -38% losses occur when duration is maximized exactly when rates are rising. Master the math, understand the economics (yield curve expectations, Fed policy, inflation), and manage dynamically. Duration is simultaneously your most important risk measure and your primary tool for expressing rate views. Use it wisely, update it constantly, and never forget that duration works both ways—helping in rallies, hurting in selloffs. The asymmetry from convexity is valuable, but can't overcome directional mistakes. Know your duration, manage your risk, adjust to environment. 📊📐"

**Most important principles:**

- Duration = weighted average time to cash flows
- Modified duration = price sensitivity per yield change
- Convexity = second derivative = valuable asymmetry
- Always positive for option-free bonds
- Longer maturity/lower coupon = higher duration
- Barbell > bullet for convexity (but lower yield)
- Match duration for immunization
- Include convexity for accuracy (>50 bp moves)

**Why this works:**

- Mathematical relationship (present value)
- First-order (duration) dominates small moves
- Second-order (convexity) essential large moves
- Parallel shift assumption reasonable short-term
- **Present value framework**

**But remember:**

- Duration assumes parallel shifts (often wrong)
- Callable bonds have negative convexity
- Credit risk separate from duration
- Rate environment determines success
- 2022 showed duration = double-edged sword
- **Active management required**

**Master duration and convexity to understand bonds, measure risk precisely, construct optimal portfolios, and navigate rate cycles successfully. 📈💰**
