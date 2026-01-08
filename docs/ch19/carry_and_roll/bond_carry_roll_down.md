# Bond Carry and Roll-Down

**Bond carry and roll-down** are fundamental fixed income return sources where carry represents the income earned from holding a bond (coupon payments plus financing costs), while roll-down captures the price appreciation that occurs as a bond ages and "rolls down" the yield curve toward shorter maturities, together forming a predictable, low-volatility return stream that works best in stable, upward-sloping curve environments and forms the foundation of many institutional fixed income strategies.

---

## The Core Insight

**The fundamental idea:**

- Total return = Carry + Roll-down + Yield change
- Carry = Coupon income - Financing cost
- Roll-down = Price gain as bond approaches maturity
- Upward-sloping curve creates automatic roll-down profits
- Predictable return in stable yield environments
- Works without taking directional rate views
- Low volatility, steady income generation
- Leverageable for enhanced returns
- Forms basis of many hedge fund strategies

**The key equations:**

$$
\text{Total Return} = \text{Carry} + \text{Roll-down} + \text{Yield Change}
$$

$$
\text{Carry} = \text{Coupon Yield} - \text{Financing Cost}
$$

$$
\text{Roll-down} = \text{Price}_{t, y_{t-1}} - \text{Price}_{t-1, y_{t-1}}
$$

$$
\text{Forward Rate} = \frac{(1+y_n)^n}{(1+y_{n-1})^{n-1}} - 1
$$

**You're essentially capturing: "The mechanical price appreciation that occurs as bonds age and move to lower yields on an upward-sloping curve, combined with coupon income that exceeds financing costs, creating a reliable return stream that requires no forecasting of yield changes and works through the mathematical structure of the yield curve itself."**

---

## What Are Bond Carry and Roll-Down?

**Before trading carry and roll, understand the fundamental mechanics:**

### 1. Carry Component

**Definition:**

$$
\text{Carry} = \frac{\text{Coupon Income}}{\text{Price}} - \text{Repo Rate}
$$

**Example: 10-year Treasury**

**Bond characteristics:**
- Price: $98.50
- Coupon: 4.00% ($40 annual per $1,000 face)
- Repo rate (financing): 5.25%

**Annual carry calculation:**

$$
\text{Current Yield} = \frac{40}{985} = 4.06\%
$$

$$
\text{Carry} = 4.06\% - 5.25\% = -1.19\%
$$

**Negative carry! (Financing cost > income)**

**This is common when:**
- Fed hiking (repo rates elevated)
- Trading at discount
- Short-maturity bonds
- **Need roll-down to compensate**

**Positive carry example: Investment-grade corporate**

**Bond characteristics:**
- Price: $102.00
- Coupon: 5.50% ($55 annual)
- Repo rate: 5.25%

**Carry:**

$$
\text{Current Yield} = \frac{55}{1020} = 5.39\%
$$

$$
\text{Carry} = 5.39\% - 5.25\% = +0.14\%
$$

**Small positive carry**

### 2. Roll-Down Component

**Definition:**

The price appreciation that occurs as a bond ages and moves to a lower yield point on the curve (assuming curve unchanged).

**Mechanics:**

**Today:**
- Bond: 10-year maturity
- Yield: 4.50%
- Price: $96.00

**One year later (curve unchanged):**
- Bond: Now 9-year maturity
- 9-year yield on curve: 4.30% (lower, upward-sloping curve)
- Price: $98.20

**Roll-down gain:**

$$
\text{Roll-down} = 98.20 - 96.00 = \$2.20 \text{ per } \$100 \text{ face}
$$

$$
\text{Roll-down return} = \frac{2.20}{96.00} = 2.29\%
$$

**Example: Detailed 10-year Treasury roll-down**

**Yield curve (upward-sloping):**

| Maturity | Yield |
|----------|-------|
| 9 years  | 4.20% |
| 10 years | 4.50% |

**Initial position:**
- 10-year bond at 4.50% yield
- Modified duration: 8.5
- Price: $96.18

**After 1 year (yields unchanged):**
- Bond now has 9 years to maturity
- Yield: 4.20% (9-year point on curve)
- Price: $97.82

**Roll-down calculation:**

$$
\text{Price change} = 97.82 - 96.18 = \$1.64
$$

$$
\text{Roll-down return} = \frac{1.64}{96.18} = 1.70\%
$$

**This happens automatically if curve stays the same!**

### 3. Total Return Decomposition

**Complete framework:**

$$
\text{Total Return} = \underbrace{\text{Coupon}}_{\text{Income}} - \underbrace{\text{Financing}}_{\text{Cost}} + \underbrace{\text{Roll-down}}_{\text{Curve}} + \underbrace{\text{Yield Change}}_{\text{Market}}
$$

**Example: Full year return**

**10-year Treasury:**
- Coupon: 4.00%
- Financing (repo): 5.25%
- Roll-down: 1.70%
- Yield change: 0% (stable)

**Total return:**

$$
4.00\% - 5.25\% + 1.70\% + 0\% = 0.45\%
$$

**Modest but positive despite negative carry!**

**If yields rise 25 bps:**

- Duration: 8.5
- Price impact: -8.5 × 0.25% = -2.125%

**Total return:**

$$
4.00\% - 5.25\% + 1.70\% - 2.125\% = -1.675\%
$$

**Loss from yield rise dominates**

### 4. Forward Rates and Roll-Down

**Forward rate formula:**

$$
f_{n-1,1} = \frac{(1+y_n)^n}{(1+y_{n-1})^{n-1}} - 1
$$

**Where:**
- $f_{n-1,1}$ = 1-year forward rate starting in year n-1
- $y_n$ = n-year spot yield
- $y_{n-1}$ = (n-1)-year spot yield

**Example:**

**Yield curve:**
- 9-year yield: 4.20%
- 10-year yield: 4.50%

**Implied 1-year forward rate 9 years from now:**

$$
f_{9,1} = \frac{(1.045)^{10}}{(1.042)^9} - 1
$$

$$
= \frac{1.5530}{1.4449} - 1 = 7.48\%
$$

**This forward rate represents the market's break-even:**

- If the 1-year rate 9 years from now is 7.48%, then holding the 10-year yields the same as holding a 9-year
- If actual rate < 7.48%, the 10-year outperforms (roll-down profits)
- If actual rate > 7.48%, the 10-year underperforms

**Key insight:**

Roll-down profits accrue if future yields are lower than forward rates predict.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/carry_rolldown.png?raw=true" alt="carry_rolldown" width="700">
</p>

**Figure 1:** Carry and roll-down return components showing how a bond "rolls down" the yield curve as it ages. On an upward-sloping curve, a 10-year bond priced to yield 4.50% will trade at the 9-year yield (4.20%) after one year if the curve remains unchanged, generating automatic price appreciation. This roll-down return combines with coupon income (minus financing costs) to create total return that can be earned without any forecast of yield changes.

---

## Economic

**Beyond the mechanics, understanding the economic rationale:**

### 1. Term Premium and Upward-Sloping Curves

**The deep insight:**

Upward-sloping yield curves exist because investors demand a **term premium** for bearing duration risk. This premium creates the mechanical roll-down return.

**Term structure decomposition:**

$$
y_n = \mathbb{E}[\text{average short rates}] + \text{Term Premium}_n
$$

**Example:**

**Expectations:**
- Current 1-year rate: 5.00%
- Expected 1-year rate next year: 4.50%
- Expected 1-year rate in 2 years: 4.00%
- Average: 4.50%

**But observed 3-year yield: 4.80%**

**Term premium:**

$$
4.80\% = 4.50\% + 0.30\%
$$

**Term premium = 30 bps**

**This premium creates roll-down:**

As the 3-year bond becomes a 2-year bond, it loses some term premium, causing the yield to fall (price to rise).

### 2. Risk-Return Trade-Off

**Duration risk compensation:**

**Short bonds (2-year):**
- Low duration (≈2)
- Low volatility
- Low yield (4.00%)
- **Low risk, low return**

**Long bonds (10-year):**
- High duration (≈8.5)
- High volatility
- Higher yield (4.50%)
- **Higher risk, higher return**

**The extra 50 bps (4.50% - 4.00%) compensates for:**
- Interest rate risk (prices fluctuate more)
- Liquidity risk (harder to trade large size)
- Reinvestment risk (uncertainty about future rates)
- **Risk premium**

**This risk premium is the source of roll-down returns.**

### 3. Supply and Demand Dynamics

**Issuance patterns:**

**Government bonds:**
- Treasury issues across curve
- But more long-end supply (30-year)
- Demand from pension funds, insurers
- **Supply/demand imbalance**

**Result:**

Long-end yields higher to attract buyers → Upward-sloping curve → Roll-down opportunities

**Example: 2010-2019**

**Average 10-year yield: 2.50%**
**Average 2-year yield: 0.75%**
**Average slope: 175 bps**

**Consistently upward-sloping:**
- Pension funds need long duration
- Insurers need asset-liability matching
- Structural demand for long end
- **Persistent term premium**

### 4. Fed Policy and Curve Shape

**Fed funds rate as anchor:**

$$
\text{Short end} \approx \text{Fed Funds} + \text{small spread}
$$

**Long end:**

$$
\text{Long end} = \mathbb{E}[\text{avg future Fed Funds}] + \text{Term Premium}
$$

**Normal environment:**

- Fed Funds: 5.00%
- Expected average next 10 years: 4.00%
- Term premium: 0.50%
- 10-year yield: 4.50%
- **Curve slopes up (4.50% > 5.00% seems wrong...)**

Actually, let me reconsider. If Fed Funds is 5.00% currently but expected to average 4.00% over next 10 years, then:

- 2-year yield ≈ 5.00% (close to current Fed Funds)
- 10-year yield ≈ 4.00% + 0.50% = 4.50%

So 10-year (4.50%) < 2-year (5.00%), which is inverted, not upward-sloping.

Let me use a more typical scenario:

**Normal upward-sloping curve:**

- Fed Funds: 3.00%
- Expected average Fed Funds next 10 years: 3.50% (mild hiking expected)
- Term premium: 1.00%
- 10-year yield: 3.50% + 1.00% = 4.50%
- 2-year yield: ≈3.25% (between current and expected)

**Slope: 4.50% - 3.25% = 125 bps (upward-sloping)**

**This creates roll-down:**

As 10-year → 9-year → 8-year, it moves down the curve toward lower yields.

### 5. Convexity and Roll-Down Enhancement

**Positive convexity helps roll-down:**

**Linear approximation:**

$$
\Delta P = -D \times \Delta y
$$

**But actual (with convexity):**

$$
\Delta P = -D \times \Delta y + \frac{1}{2} C \times (\Delta y)^2
$$

**Roll-down scenario:**

- Yield falls from 4.50% to 4.20% (-30 bps)
- Duration: 8.5
- Convexity: 95

**Linear estimate:**

$$
\Delta P = -8.5 \times (-0.003) = +2.55\%
$$

**With convexity:**

$$
\Delta P = 2.55\% + \frac{1}{2} \times 95 \times (0.003)^2 = 2.55\% + 0.04\% = 2.59\%
$$

**Convexity adds 4 bps to roll-down return!**

**Over time, convexity consistently enhances roll-down.**

---

## Key Terminology

**Carry:**

$$
\text{Carry} = \text{Coupon Yield} - \text{Financing Rate}
$$

- Income component of total return
- Can be positive or negative
- Critical for leveraged strategies
- **Daily accrual**

**Roll-Down:**

$$
\text{Roll-down return if curve unchanged}
$$

- Price appreciation from aging
- Mechanical on upward curve
- Zero on flat curve
- Negative on inverted curve
- **Curve structure dependent**

**Forward Rate:**

$$
f_{t,T} = \text{Market's implied future rate}
$$

- Break-even for holding longer maturity
- Derived from spot curve
- Typically > expected future spot
- **Contains term premium**

**Repo Rate:**

$$
\text{Repo} = \text{Short-term borrowing rate for bond financing}
$$

- Typically Fed Funds + 10-25 bps
- Used to leverage carry trades
- Daily financing cost
- **Funding consideration**

**Term Premium:**

$$
\text{Term Premium} = y_n - \mathbb{E}[\text{avg short rates}]
$$

- Compensation for duration risk
- Source of roll-down profits
- Varies over time (50-150 bps typical)
- **Risk premium**

**Horizon Return:**

$$
\text{Horizon Return} = \text{Carry} + \text{Roll} + \text{Yield Change}
$$

- Total return over holding period
- If yields unchanged: Carry + Roll
- **Key metric**

**Breakeven Yield Change:**

$$
\text{Breakeven} = \frac{\text{Carry} + \text{Roll}}{-\text{Duration}}
$$

- How much yields can rise before loss
- Higher for steep curves
- Key risk measure
- **Safety margin**

**Riding the Yield Curve:**

$$
\text{Strategy of buying longer maturity to maximize roll}
$$

- Buy 10-year, not 2-year
- Harvest term premium
- Classic carry/roll trade
- **Duration extension**

**Bullet vs Barbell:**

- Bullet: Concentrated maturity (maximize roll at one point)
- Barbell: Short + Long (convexity but less roll)
- **Structure choice**

**Running Yield:**

$$
\text{Running Yield} = \frac{\text{Coupon}}{\text{Current Price}}
$$

- Not same as YTM
- Relevant for carry calculation
- **Income measure**

---

## The Greeks (Carry and Roll Dynamics)

**Carry and roll strategies have specific risk characteristics:**

### 1. Delta (Interest Rate Sensitivity)

**Directional exposure:**

$$
\Delta = -\text{Duration} \times \text{Position Size}
$$

**Example: $100M 10-year Treasuries**

- Duration: 8.5 years
- Delta: -8.5 × $100M = -$850M

**Interpretation:**

- For 1% (100 bps) yield rise: -8.5% loss = -$8.5M
- For 1 bp yield rise: -0.085% loss = -$85k
- **DV01 = $85k**

**This is the primary risk:**

Carry and roll strategies are NOT hedged against parallel shifts. They profit in stable/falling yield environments but suffer in rising yield environments.

**Breakeven analysis:**

**10-year position:**
- Carry: -1.19% (negative)
- Roll-down: +1.70%
- Net carry + roll: +0.51%
- Duration: 8.5

**Breakeven yield rise:**

$$
\text{Breakeven} = \frac{0.51\%}{8.5} = 0.06\% = 6 \text{ bps}
$$

**If yields rise > 6 bps over the year, strategy loses money!**

### 2. Gamma (Convexity)

**Second-order effect:**

$$
\Gamma = \text{Convexity} \times \text{Position Size}
$$

**For $100M position:**

- Convexity: 95
- Gamma: 95 × $100M = $9.5B

**Always positive for bonds:**

- Yields fall: Profit more than duration predicts
- Yields rise: Lose less than duration predicts
- **Beneficial asymmetry**

**Roll-down benefits from convexity:**

As yields fall during roll-down, convexity enhances the price gain beyond linear duration effect.

**Example:**

**Roll-down: Yield 4.50% → 4.20% (-30 bps)**

- Duration effect: +2.55%
- Convexity add-on: +0.04%
- Total: +2.59%
- **Convexity bonus**

### 3. Theta (Time Decay / Carry)

**Time value:**

$$
\Theta = \text{Carry per day} + \text{Roll per day}
$$

**Positive theta for carry/roll strategies:**

**Daily accrual:**

- Coupon accrues: +$11 per day (4% annual / 365)
- Financing cost: -$14 per day (5.25% annual / 365)
- Net carry: -$3 per day

**Roll-down accrual:**

- Annual roll: +1.70%
- Daily roll: +$47 per day (on $100k position)

**Net daily theta:**

$$
\Theta = -\$3 + \$47 = +\$44 \text{ per day}
$$

**Positive theta = earning money from passage of time (if yields stable)**

This is the beauty of carry/roll strategies!

### 4. Vega (Volatility Sensitivity)

**Not traditional vega (no options), but volatility impacts:**

**High yield volatility (bad for carry/roll):**

- Yields swing ±50 bps monthly
- Carry/roll (+0.51% annually = 4 bps/month) swamped by noise
- Cannot harvest predictable return
- **Overwhelmed by vol**

**Low yield volatility (good for carry/roll):**

- Yields stable ±10 bps monthly
- Carry/roll (4 bps/month) meaningful
- Predictable return stream
- **Optimal environment**

**Carry/roll prefers low volatility environments.**

### 5. Rho (Rate Level Sensitivity)

**Financing cost sensitivity:**

$$
\rho = \frac{\partial \text{Carry}}{\partial r_{\text{repo}}}
$$

**If repo rates rise:**

- Financing cost increases
- Carry declines
- Strategy less attractive
- **Negative rho**

**Example:**

**Initial:**
- Repo: 5.25%
- Carry: -1.19%
- Net (with roll): +0.51%

**Repo rises to 6.00%:**
- Carry: -1.94%
- Net (with roll): -0.24%
- **Now unprofitable!**

**Carry strategies vulnerable to rising financing costs.**

---

## Strategy Selection

**Different bonds offer different carry/roll profiles:**

### 1. Maximum Roll Strategy (10-Year Point)

**Optimal maturity for roll-down:**

Empirically, the 10-year maturity point typically offers the best roll-down per unit of duration.

**Why 10-year:**

**Curve shape:**
- 2-5 year: Curve steep (good roll)
- 10-15 year: Curve also steep (good roll)
- 20-30 year: Curve flattens (less roll)

**Roll per unit of duration:**

| Maturity | Duration | Annual Roll | Roll/Duration |
|----------|----------|-------------|---------------|
| 2-year | 1.9 | 0.30% | 0.16 |
| 5-year | 4.5 | 0.90% | 0.20 |
| 10-year | 8.5 | 1.70% | 0.20 |
| 30-year | 18.0 | 2.00% | 0.11 |

**10-year offers good roll per unit of duration taken.**

**Implementation:**

- Buy 10-year Treasuries
- Hold for 6-12 months
- Roll as maturity shortens
- **Classic strategy**

### 2. High Carry Strategy (Credit Bonds)

**Maximize carry component:**

**Investment-grade corporates:**

- Coupon: 5.50%
- Price: 102
- Current yield: 5.39%
- Repo: 5.25%
- **Carry: +0.14%**

**Plus credit spread compression potential:**

- Buy A-rated at 120 bps over Treasuries
- If spread tightens to 100 bps: +20 bps capital gain
- **Total: Carry + Roll + Spread compression**

**Example: Microsoft 10-year bond**

- Coupon: 5.25%
- Yield: 4.95% (30 bps over Treasuries)
- Carry: +0.00% (coupon ≈ repo)
- Roll-down: +1.70% (similar to Treasuries)
- Spread tightening potential: +0.30%
- **Total expected: +2.00%**

### 3. Leveraged Carry/Roll (Hedge Fund Strategy)

**Amplify returns via leverage:**

**Base case:**
- 10-year Treasury
- Carry + Roll: +0.51%
- **Modest return**

**With 5× leverage (repo financing):**

**Position:**
- $500M 10-year bonds
- Financed via repo ($500M borrowed)
- Equity capital: $100M

**Returns:**

- Carry: -1.19% × 5 = -5.95%
- Roll: +1.70% × 5 = +8.50%
- Net: +2.55%
- **On $100M equity: 2.55% (vs 0.51% unleveraged)**

Wait, that doesn't look right. Let me recalculate.

If I have $100M equity and borrow $400M to buy $500M bonds (5× leverage):

- Coupon income: 4.00% × $500M = $20M
- Financing cost: 5.25% × $400M = $21M
- Net carry: -$1M (-1% on $100M equity)

- Roll-down: 1.70% × $500M = $8.5M (+8.5% on equity)

- Total: -1% + 8.5% = **+7.5% on equity**

That's better! Leverage amplifies the roll-down component significantly.

**Risk:**

- Duration exposure: 8.5 × 5 = 42.5 years (effective)
- If yields rise 18 bps: Loss = 42.5 × 0.18% = 7.5% (wipes out entire return)
- **Very sensitive to rates**

### 4. Barbell vs Bullet for Roll

**Bullet (concentrated):**

- 100% in 10-year bonds
- Maximum roll at 10-year point
- Simple management
- **Roll optimization**

**Barbell (diversified):**

- 50% in 2-year bonds
- 50% in 30-year bonds
- Weighted duration: ≈10 years
- **Higher convexity, less roll**

**Roll comparison:**

**Bullet:**
- 10-year roll: 1.70%
- **Total: 1.70%**

**Barbell:**
- 2-year roll: 0.30% × 50% = 0.15%
- 30-year roll: 2.00% × 50% = 1.00%
- **Total: 1.15% (33% less!)**

**But barbell has higher convexity:**

- Bullet convexity: 95
- Barbell convexity: 177
- **Convexity premium**

**Trade-off: Roll vs Convexity**

---

## Time Selection

**Carry/roll strategies are time-sensitive:**

### 1. Ideal Market Conditions

**1. Stable yield environment:**

$$
\sigma(\Delta y) < 10 \text{ bps/month}
$$

**Why:**

- Carry/roll generates 4-5 bps/month
- If yield volatility >50 bps/month, noise dominates signal
- **Need stability**

**Example: 2003-2006**

**Market conditions:**
- Fed hiking slowly (predictable)
- Yield volatility low (8 bps/month)
- Curve steep (150 bps average)
- **Perfect for carry/roll**

**Results:**
- Typical carry/roll strategy: +6-8% annually
- With 3× leverage: +15-20% annually
- **Golden era**

**2. Upward-sloping curve:**

$$
\text{10yr yield} - \text{2yr yield} > 100 \text{ bps}
$$

**Why:**

- Steeper curve = more roll-down
- Term premium higher
- **Maximum roll potential**

**Historical ranges:**

- Very steep: >200 bps (rare, excellent)
- Normal: 100-150 bps (good)
- Flat: 50-100 bps (marginal)
- Inverted: <0 bps (avoid)

**3. Low financing costs:**

$$
\text{Repo rate} < \text{10yr yield}
$$

**Why:**

- Positive carry on leveraged positions
- Can use leverage profitably
- **Financing advantage**

**Example:**

**Favorable (2020-2021):**
- 10-year yield: 1.50%
- Repo rate: 0.10%
- Carry: +1.40% (huge!)
- **Carry alone profitable**

**Unfavorable (2023):**
- 10-year yield: 4.50%
- Repo rate: 5.50%
- Carry: -1.00%
- **Need roll to overcome**

### 2. Entry Signals

**1. Fed pause after hiking cycle:**

$$
\text{Fed done hiking} \Rightarrow \text{Yields stable} \Rightarrow \text{Enter carry/roll}
$$

**Example: July 2006**

**Setup:**
- Fed hiked to 5.25% (terminal rate)
- Curve steep (200+ bps)
- Signaled pause

**Action:**
- Enter carry/roll strategies
- Curve stayed steep for 18 months
- **Profitable period**

**2. Curve steepening events:**

$$
\text{2s10s widening} \Rightarrow \text{More roll potential}
$$

**Example: Post-recession**

**2009-2010:**
- Fed at zero, committed
- Curve steepened to 270 bps
- Maximum roll-down
- **Enter for multi-year harvest**

**3. VIX normalization:**

$$
\text{VIX} < 15 \Rightarrow \text{Low volatility} \Rightarrow \text{Carry/roll works}
$$

**Stable environment indicator**

### 3. Exit Signals

**1. Fed tightening cycle beginning:**

$$
\text{Fed hiking} \Rightarrow \text{Yields rising} \Rightarrow \text{Exit carry/roll}
$$

**Why:**

- Rising yields overwhelm carry/roll
- Curve may invert (negative roll)
- Losses mount
- **Wrong environment**

**Example: 2022**

**Fed started hiking aggressively:**
- Yields rose 250 bps
- Carry/roll strategies -20% to -30%
- Should have exited early 2022
- **Disaster**

**2. Curve flattening:**

$$
\text{2s10s} < 50 \text{ bps} \Rightarrow \text{Minimal roll} \Rightarrow \text{Exit}
$$

**3. Volatility spike:**

$$
\text{VIX} > 30 \Rightarrow \text{Unstable} \Rightarrow \text{Reduce/exit}
$$

**4. Financing costs rise above coupon:**

$$
\text{Repo} > \text{Coupon} + \text{Roll} \Rightarrow \text{Negative net carry} \Rightarrow \text{Exit}
$$

---

## Maximum Profit and Loss

### 1. Maximum Profit (2010-2011 QE2 Era)

**Setup:**

- Date: November 2010
- Strategy: Leveraged carry/roll in 10-year Treasuries
- Capital: $100M
- Position: $400M 10-year bonds (4× leverage)

**Market conditions:**

**November 2010:**
- 10-year yield: 2.75%
- Repo rate: 0.15%
- 2s10s spread: 240 bps (very steep)
- Fed doing QE2 ($600B)

**Position details:**

- 10-year bonds at 2.75% yield
- Coupon: 2.625% (slightly below yield)
- Duration: 8.7 years
- Price: $99.10

**Annual return calculation:**

**Carry:**
- Coupon income: 2.625% × $400M = $10.5M
- Financing cost: 0.15% × $300M = $0.45M (borrowing $300M)
- Net carry: $10.05M on $100M = **+10.05%**

**Roll-down (steep curve):**
- 10-year → 9-year: Yield 2.75% → 2.45% (30 bps)
- Duration 8.7 × 30 bps = 2.61% price gain
- On $400M: $10.44M
- On $100M equity: **+10.44%**

**Yield compression (QE2 effect):**
- Fed buying pressure
- 10-year fell from 2.75% → 1.90% (85 bps)
- Price gain: 8.7 × 0.85% = 7.40%
- On $400M: $29.6M
- On $100M equity: **+29.6%**

**Total return (12 months):**

$$
10.05\% + 10.44\% + 29.6\% = 50.09\%
$$

**Extraordinary performance in perfect conditions!**

**Why this worked perfectly:**

1. ✅ Extremely steep curve (240 bps roll potential)
2. ✅ Near-zero financing costs (0.15% repo)
3. ✅ Fed QE pushing yields down
4. ✅ Low volatility (VIX 15-20)
5. ✅ Leverage amplified all three components
6. ✅ Perfect alignment of factors
7. **Once-in-decade opportunity**

### 2. Maximum Loss (2022 Fed Hiking Cycle)

**Setup:**

- Date: January 2022
- Strategy: Carry/roll in 30-year Treasuries
- Capital: $50M
- Position: $150M 30-year bonds (3× leverage)

**Market conditions:**

**January 2022:**
- 30-year yield: 2.00%
- Repo rate: 0.05%
- Curve steep (180 bps)
- Inflation 7%, Fed about to hike aggressively

**Position details:**

- 30-year bonds at 2.00% yield
- Coupon: 2.375%
- Duration: 18 years
- Price: $104.00

**The disaster (Jan-Oct 2022):**

**Fed hiking:**
- Jan: 0.25% Fed Funds
- Oct: 4.00% Fed Funds (+375 bps in 9 months!)

**Yield explosion:**
- 30-year: 2.00% → 4.50% (+250 bps)

**P&L calculation:**

**Carry (9 months):**
- Coupon: 2.375% × 9/12 = 1.78%
- Financing (avg 2%): 2.00% × 9/12 = 1.50%
- Net carry: +0.28% on $150M = +$420k
- On $50M equity: **+0.84%**

**Roll-down (9 months):**
- Minimal (overwhelmed by yield rise)
- ~+0.50% on equity

**Yield rise disaster:**
- Duration: 18 years
- Yield rise: 250 bps
- Price decline: -18 × 2.50% = -45%
- On $150M: -$67.5M
- On $50M equity: **-135%**

**Total return:**

$$
0.84\% + 0.50\% - 135\% = -133.66\%
$$

**Account wiped out, margin call, forced liquidation!**

**Final outcome:**

- Capital: $50M → $5M (if cut losses)
- Or $0 if held too long (margin call)
- **-90% to -100% loss**

**What went catastrophically wrong:**

1. ❌ Ignored inflation threat (7% CPI)
2. ❌ Ignored Fed hawkish signals
3. ❌ Used long duration (30-year) in hiking cycle
4. ❌ Leveraged 3× (amplified disaster)
5. ❌ No stop-loss (rode it down)
6. ❌ Fought the Fed (never works)
7. ❌ Carry/roll strategy in WORST possible environment
8. **Textbook failure**

---

## When to Use Carry and Roll-Down Strategies

### 1. Ideal Applications

**1. Stable macro environment:**

- Fed on hold (no hiking or cutting expected)
- Inflation stable (2-3%)
- Economic growth steady
- **Low volatility regime**

**2. Post-recession recovery:**

- Fed at zero/low rates
- Curve very steep (200+ bps)
- Committed to accommodation
- **Maximum roll potential**

**Example: 2009-2013**

- Fed Funds: 0-0.25% (committed)
- 2s10s: 200-270 bps (steep)
- Carry/roll strategies: +6-10% annually
- **Optimal period**

**3. Portfolio income generation:**

- Need steady returns
- Can't tolerate equity volatility
- Liability matching (pensions)
- **Fixed income alternative**

**4. Low financing environment:**

- Repo <2%
- Can leverage profitably
- Enhance returns via leverage
- **Hedge fund favorite**

**5. Risk-on environment:**

- Credit spreads tight
- Economic optimism
- Carry trades working globally
- **Favorable backdrop**

### 2. Specific Use Cases

**Use Case 1: Pension fund liability matching**

**Goal: Match 6% actuarial return assumption**

**Strategy:**
- Buy 10-year Treasuries
- Unleveraged (regulatory constraints)
- Hold for roll-down

**Current environment:**
- 10-year yield: 4.50%
- Carry: -0.50%
- Roll-down: +1.70%
- Net: +1.20%
- **Not enough!**

**Alternative: Add credit**
- 70% Investment-grade corporates (6.00% yield)
- 30% Treasuries (4.50% yield)
- Blended carry: 5.55%
- Roll-down: +1.50%
- **Total: ~7% (achieves target)**

**Use Case 2: Absolute return fund**

**Goal: Consistent 5-7% with low volatility**

**Strategy:**
- 10-year Treasury carry/roll base
- 3× leverage via repo
- Active curve positioning

**Returns:**
- Unleveraged carry/roll: +2.00%
- With 3× leverage: +6.00%
- **Target achieved**

**Risk:**
- Duration: 8.5 × 3 = 25.5 years
- Breakeven yield rise: 6% / 25.5 = 23 bps
- **Tight risk budget**

**Use Case 3: Barbell income strategy**

**Goal: Income + convexity protection**

**Portfolio:**
- 50% 2-year Treasuries (income)
- 50% 30-year Treasuries (roll + convexity)

**Returns:**
- 2-year carry: +1.50%
- 30-year carry + roll: +2.50%
- Weighted: +2.00%
- **Plus convexity optionality**

---

## When NOT to Use Carry/Roll

### 1. Avoid These Situations

**1. Fed hiking cycle:**

$$
\text{Fed Funds rising} \Rightarrow \text{Avoid carry/roll}
$$

**Why:**

- Yields rising overwhelms carry/roll
- Typical hikes: 200-400 bps
- Duration losses: -20% to -40%
- Carry/roll (+2%) can't compensate
- **Disaster scenario**

**Example: 2022 (already covered)**

**2. Inverted yield curve:**

$$
\text{2s10s} < 0 \Rightarrow \text{Negative roll-down}
$$

**Why:**

- Roll-down works in reverse
- As 10-year → 9-year, yield rises (inverted curve)
- Price falls instead of rising
- **Anti-roll**

**Example:**

**Inverted curve:**
- 10-year: 3.80%
- 9-year: 4.00% (higher!)

**Roll effect:**
- 10-year bond rolls to 9-year point
- Yield: 3.80% → 4.00% (+20 bps)
- Duration: 8.5
- Price decline: -8.5 × 0.20% = **-1.70%**
- **Negative roll-down!**

**3. High volatility environment:**

$$
\text{VIX} > 30 \text{ OR } \sigma(\Delta y) > 50 \text{ bps/month}
$$

**Why:**

- Carry/roll (+0.5% monthly) swamped by volatility
- Cannot harvest predictable return
- Risk dominates
- **Wrong regime**

**4. Flat yield curve:**

$$
\text{2s10s} < 30 \text{ bps}
$$

**Why:**

- Minimal roll-down potential
- Risk/reward poor
- Better opportunities elsewhere
- **Insufficient term premium**

**5. Rising financing costs:**

$$
\text{Repo rate rising faster than yields}
$$

**Why:**

- Negative carry expands
- Leverage becomes expensive
- Profit margin compressed
- **Margin squeeze**

**Example:**

**2023:**
- 10-year yield: 4.50% (stable)
- Repo rate: 5.50% (Fed hiking)
- Carry: -1.00% and widening
- **Unprofitable**

**6. Credit stress environment:**

**If using corporate bonds:**

- Credit spreads widening
- Default risk rising
- Spread widening > carry + roll
- **Credit losses dominate**

**Example: March 2020**

- IG spreads: 100 bps → 350 bps (+250 bps)
- Duration 7 × 2.50% = -17.5% loss
- Carry/roll (+3%) can't compensate
- **-14.5% loss**

---

## Position Sizing and Risk Management

### 1. The Golden Rule

**Position sizing formula:**

$$
\text{Position Size} = \frac{\text{Risk Budget}}{\text{Duration} \times \sigma(\Delta y) \times \sqrt{12}}
$$

**Example:**

**Portfolio: $100M**
**Monthly risk budget: 1% = $1M**

**10-year Treasuries:**
- Duration: 8.5 years
- Monthly yield volatility: 15 bps (1σ)

**Max position:**

$$
\text{Position} = \frac{\$1M}{8.5 \times 0.0015} = \$78.4M
$$

**This is unleveraged.**

**With 2× leverage:**

- Duration exposure: 17 years
- Position: $78.4M / 2 = **$39.2M** (unleveraged equivalent)
- Actual notional: $78.4M (leveraged 2×)

### 2. Leverage Guidelines

**Conservative (pension fund):**

- 0× leverage (unleveraged)
- Buy bonds with cash
- No repo financing
- **Safety first**

**Moderate (insurance company):**

- 1-2× leverage
- Modest repo financing
- DV01 limits strict
- **Balanced approach**

**Aggressive (hedge fund):**

- 3-5× leverage
- Maximize capital efficiency
- Active management
- **Return optimization**

**Dangerous (LTCM-style):**

- 10-25× leverage
- Minimal capital buffer
- Disaster waiting to happen
- **Avoid!**

### 3. Diversification Requirements

**Don't concentrate:**

**Bad:**
- 100% in 10-year Treasuries
- Single maturity
- Single curve point
- **Concentration risk**

**Good:**
- 40% in 10-year Treasuries
- 30% in 5-year Treasuries
- 30% in IG corporates
- **Diversified**

**Across curve:**

- Short (2-5 year): 30%
- Intermediate (5-10 year): 40%
- Long (10-30 year): 30%
- **Curve diversification**

### 4. Stop-Loss Discipline

**Yield-based stop:**

$$
\text{Exit if yields rise} > 50 \text{ bps from entry}
$$

**Example:**

- Entry: 10-year at 4.50%
- Stop: 5.00%
- **If yields hit 5.00%, exit**

**Loss at stop:**

- Duration: 8.5
- Yield rise: 50 bps
- Loss: -8.5 × 0.50% = -4.25%
- **Controlled loss**

**Time-based stop:**

$$
\text{Exit after 12 months regardless}
$$

**Why:**

- Carry/roll accrues over time
- If not profitable after 1 year, wrong environment
- Cut losses
- **Discipline**

### 5. Rebalancing Strategy

**Monthly roll-down harvest:**

**Process:**

1. **Month-end:** Calculate current maturity
2. **If maturity < original by 1 year:** Sell and buy new
3. **Example:**
   - Bought 10-year in January
   - December: Now 9-year bond
   - Sell 9-year, buy new 10-year
   - **Harvest roll, reset position**

**Curve repositioning:**

**Quarterly assessment:**

- Review curve slope
- If flattened materially: Reduce position
- If steepened: Consider adding
- **Adaptive sizing**

---

## Common Mistakes Beginners Make

### 1. Mistake #1

**The error:**

- Calculate return using only coupon + roll
- Forget repo financing cost
- **Overestimate returns**

**Example:**

**Trader thinks:**
- Coupon: 4.00%
- Roll: 1.70%
- Total: 5.70% (amazing!)

**Reality:**
- Repo cost: 5.25%
- Net carry: -1.25%
- Actual: -1.25% + 1.70% = 0.45%
- **Vastly different!**

**Correct approach:**

- Always subtract financing
- Calculate net carry
- **Realistic expectations**

### 2. Mistake #2

**The error:**

- See steep curve (good roll)
- Enter carry/roll strategy
- But Fed hiking aggressively
- **Fighting the Fed**

**What happens:**

**2022 example:**
- Curve steep (150 bps)
- Roll potential: 1.50%
- Entered carry/roll
- Fed hiked 425 bps
- Yields rose 250 bps
- Loss: -20% to -40%
- **Disaster**

**Correct approach:**

- Check Fed policy first
- If hiking: Avoid carry/roll
- Wait for pause/cuts
- **Policy awareness**

### 3. Mistake #3

**The error:**

- "Carry/roll is low risk, I can lever 10×"
- Small account: $1M
- Position: $10M (10× leverage)
- **Excessive**

**What happens:**

**Minor yield rise (50 bps):**
- Duration: 8.5 years
- Loss per $: -4.25%
- On $10M: -$425k
- On $1M equity: -42.5%
- **Margin call**

**Correct approach:**

- Max 3-5× leverage
- Keep cash buffer
- **Prudent sizing**

### 4. Mistake #4

**The error:**

- "30-year has most roll-down!"
- Buy 30-year for maximum roll
- **High duration risk**

**Reality:**

**Roll per unit of duration:**
- 30-year: 2.00% roll, 18 duration = 0.11 roll/duration
- 10-year: 1.70% roll, 8.5 duration = 0.20 roll/duration
- **10-year more efficient!**

**Plus:**
- 30-year has 2× duration risk
- Small yield move = large loss
- Not worth extra roll
- **Inefficient**

**Correct approach:**

- Focus on roll per unit of duration
- 10-year sweet spot typically
- **Optimization**

### 5. Mistake #5

**The error:**

- Estimate roll using only duration
- Large yield change
- Convexity impact ignored
- **Inaccurate P&L**

**Example:**

**Roll: Yield 4.50% → 3.50% (-100 bps)**

**Duration-only estimate:**
- Duration: 8.5
- Price gain: +8.5%

**Actual (with convexity 95):**
- Convexity add: +0.5 × 95 × 0.01² = +0.48%
- Total: +8.98%
- **Underestimated by 0.48%!**

**Correct approach:**

- Include convexity for large moves
- Use full pricing models
- **Accuracy**

### 6. Mistake #6

**The error:**

- Enter carry/roll
- "I'll hold forever"
- Environment changes (Fed hikes)
- Still holding
- **Giving back all gains**

**Example:**

**2010-2021:**
- Carry/roll worked perfectly
- Accumulated +50% over decade
- 2022: Fed hiked, lost -30%
- **Gave back 3 years of gains!**

**Correct approach:**

- Set exit triggers
- Monitor Fed closely
- Exit when environment shifts
- **Disciplined exits**

### 7. Mistake #7

**The error:**

- Bond yields 4.50%
- Think "I'll make 4.50%"
- **Wrong!**

**Reality:**

**Total return:**
- Yield: 4.50%
- Financing: -5.25%
- Roll: +1.70%
- Yield change: -2.00% (rates rose)
- **Total: -1.05% (loss!)**

**Correct approach:**

- Calculate total return components
- Not just yield
- **Comprehensive analysis**

### 8. Mistake #8

**The error:**

- Try to time exact curve movements
- Enter when curve "should" steepen
- **Speculation, not carry/roll**

**Better approach:**

**Systematic:**
- Enter when curve >100 bps steep
- Exit when <50 bps
- No timing, rules-based
- **Mechanical**

### 9. Mistake #9

**The error:**

- Buy premium bond (above par)
- Calculate carry using coupon
- Forget pull-to-par effect
- **Overestimate return**

**Example:**

**Bond trading at $108:**
- Coupon: 5.00%
- Years to maturity: 4
- Repo: 5.25%

**Naive calculation:**
- Carry: 5.00% - 5.25% = -0.25%

**Correct (including pull-to-par):**
- Coupon: +5.00%
- Pull-to-par: -$8/$108 / 4 years = -1.85% annually
- Financing: -5.25%
- **Net: -2.10% annually!**

**Much worse than thought**

### 10. Mistake #10

**The error:**

- Buy off-the-run bonds (cheap!)
- Expect same roll as on-the-runs
- **Liquidity penalty**

**Reality:**

**Off-the-run:**
- Wider bid-ask (0.5-1.0 bps)
- Harder to finance (higher repo)
- Exit difficult (spread widens in stress)
- **Hidden costs**

**Better:**
- Stick to on-the-runs (2, 5, 10, 30 year)
- Pay up for liquidity
- **Trade-off worth it**

---



## Final Wisdom

> "Carry and roll-down are the most reliable sources of fixed income returns—mechanical, predictable, and harvestable without forecasting yield changes. A 10-year Treasury on a 150 bps upward-sloping curve delivers 1.5-2.0% annual roll-down automatically if the curve stays unchanged, combining with coupon income (minus financing) to generate steady returns that formed the foundation of successful hedge fund strategies for decades. But this reliability exists ONLY in specific regimes: stable curves (yield volatility <15 bps/month), Fed on hold (no aggressive hiking), and positive term premium (upward slope >100 bps). The 2003-2006 period delivered 15%+ annually on 3× leveraged carry/roll, while 2022 destroyed -30% to -40% when the Fed hiked 425 bps in nine months. Carry/roll is simultaneously 'safe' income generation (in right environment) and catastrophic blowup risk (in wrong environment). Success requires ruthless regime awareness: exit immediately when Fed turns hawkish, avoid during hiking cycles entirely, size positions by duration × yield volatility, cap leverage at 3-5×, and maintain disciplined stop-losses at 50 bps yield rise. The strategy works beautifully 70% of the time (stable periods) and fails catastrophically 30% (hiking cycles, crises). Know which regime you're in—that's the entire game. 📊💰"

**Most important principles:**

- Total return = Carry + Roll + Yield change
- Roll-down requires upward-sloping curve (>100 bps)
- Financing costs critical (subtract from carry)
- 10-year maturity typically optimal (roll per duration)
- Steep curve = more roll (150-250 bps ideal)
- Leverage amplifies both gains and losses (cap at 3-5×)
- Fed policy dominates (hiking = exit, hold = enter)
- Stop-losses mandatory (50 bps yield rise = exit)

**Why this works:**

- Term premium compensates duration risk
- Forward rates exceed expected future rates
- Curve persistently upward-sloping (historical)
- **Structural risk premium**

**But remember:**

- 2022 worst bond year in history (-30%)
- Fed hiking overwhelms carry/roll
- Leverage amplifies disasters
- Inverted curves = negative roll
- Volatility regime changes fast
- **Active management required**

**Harvest carry and roll in stable, steep-curve environments. Exit immediately when Fed turns aggressive. Never over-leverage. This is income generation, not speculation—but it requires regime discipline. 📈🏦**