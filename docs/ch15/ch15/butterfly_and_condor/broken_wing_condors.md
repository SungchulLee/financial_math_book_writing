# Broken Wing Condors

**Broken wing condors** are asymmetric, defined-risk option strategies where one side of an iron condor has unequal strike spacing, creating a directional bias while maintaining credit collection. They offer the income generation of condors with reduced capital requirements and strategic flexibility for traders with moderate directional conviction.








---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_bearish_broken_wing.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**The fundamental idea:**

- Iron condors are great for range-bound trading
- But sometimes you have a directional bias (slightly bullish or bearish)
- Traditional condors are perfectly neutral (no edge)
- Broken wing condors let you express directionality while collecting premium
- By making one side "broken," you reduce risk on your favored side
- You still collect credit but with asymmetric risk profile

**The key equation:**

$$
\text{Broken Wing Condor} = \text{Regular Spread} + \text{Broken Spread}
$$

$$
\text{Max Profit} = \text{Net Credit} \quad (\text{collected upfront})
$$

$$
\text{Max Loss} = \text{Wider Spread Width} - \text{Net Credit} \quad (\text{one-sided risk})
$$

**You're essentially betting: "Stock will move in my direction OR stay flat, so I keep the premium with reduced risk on my conviction side."**

---

## What Are Broken Wing Condors?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_broken_wing_greeks.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Before trading broken wings, understand the variations:**

### 1. Broken Wing Iron Condor (Call Side Broken)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_brokenness_levels.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Definition:** Regular bull put spread + wider bear call spread, creating bullish bias.

**Structure:**

- **Bull Put Spread (normal):**

  - Sell $95 put for $2.00
  - Buy $90 put for $0.50
  - Width: $5
  
- **Bear Call Spread (broken - wider):**

  - Sell $105 call for $1.50
  - Buy $115 call for $0.25
  - Width: $10 (broken!)

- **Net Credit:** ($2.00 + $1.50) - ($0.50 + $0.25) = $2.75

**The bet:** Stock stays above $95 or rallies (bullish bias)

**Max Risk:** 

- Downside: $5 - $2.75 = $2.25 (concentrated risk)
- Upside: $10 - $2.75 = $7.25 (but unlikely - far OTM)

**Characteristics:**

- Bullish directional bias
- Lower upside risk (wider call spread)
- Concentrated downside risk (normal put spread)
- Collects larger credit than symmetric condor
- Reduced capital requirement vs. regular condor

### 2. Broken Wing Iron Condor (Put Side Broken)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_bullish_broken_wing.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Definition:** Wider bull put spread + regular bear call spread, creating bearish bias.

**Structure:**

- **Bull Put Spread (broken - wider):**

  - Sell $95 put for $2.00
  - Buy $85 put for $0.25
  - Width: $10 (broken!)
  
- **Bear Call Spread (normal):**

  - Sell $105 call for $1.50
  - Buy $110 call for $0.50
  - Width: $5

- **Net Credit:** ($2.00 + $1.50) - ($0.25 + $0.50) = $2.75

**The bet:** Stock stays below $105 or declines (bearish bias)

**Max Risk:**

- Downside: $10 - $2.75 = $7.25 (but unlikely - far OTM)
- Upside: $5 - $2.75 = $2.25 (concentrated risk)

**Characteristics:**

- Bearish directional bias
- Lower downside risk (wider put spread)
- Concentrated upside risk (normal call spread)
- Collects larger credit than symmetric condor
- Reduced capital requirement vs. regular condor

### 3. Skip Strike Broken Wing Condor

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_capital_efficiency.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Definition:** One side has a completely missing strike, creating zero-cost protection on one wing.

**Structure (extreme bullish):**

- Sell $95 put for $2.50
- Buy $90 put for $1.00
- Sell $110 call for $1.00
- Buy $120 call for $0.10 (way OTM - skip strike)

**Net Credit:** ($2.50 + $1.00) - ($1.00 + $0.10) = $2.40

**The asymmetry:**

- Put side: $5 wide, realistic risk
- Call side: $10 wide, extremely unlikely risk
- Acts almost like covered strangle with defined risk

**Figure 1:** Profit/loss diagram comparing symmetric iron condor (left) to broken wing condor (right). Note the asymmetric risk profile with concentrated risk on one side and distant max loss on the other, creating directional bias while maintaining credit collection.

---

## Economic Interpretation

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_risk_heatmap.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Beyond the basic definition, understanding what broken wing condors REALLY are economically:**

### 1. Broken Wing Condors as Directional Insurance Underwriting

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_symmetric_vs_broken_wing.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**The deep insight:**

A broken wing condor is economically equivalent to **selling insurance with conviction-weighted reinsurance**. When you construct a broken wing condor, you're essentially:

1. **Selling insurance on both sides** (collecting premium from range)
2. **Buying expensive reinsurance where you're wrong** (concentrated risk)
3. **Buying cheap reinsurance where you're right** (distant protection)
4. **Expressing directional bias through asymmetric protection**

**Formal decomposition:**

$$
\underbrace{\text{Broken Wing Condor}}_{\text{Net Credit}} \equiv \underbrace{\text{Tight Spread}}_{\text{Where Wrong}} + \underbrace{\text{Wide Spread}}_{\text{Where Right}}
$$

**Why this matters:**

**Symmetric Iron Condor (no conviction):**

- Sell $95/$90 put spread for $1.50 (risk $3.50)
- Sell $105/$110 call spread for $1.50 (risk $3.50)
- Collect $3.00 net
- **No directional edge, symmetric risk**

**Broken Wing Condor (bullish conviction):**

- Sell $95/$90 put spread for $1.50 (risk $3.50)
- Sell $105/$115 call spread for $1.75 (risk $8.25)
- Collect $3.25 net
- **Better credit, but risk concentrated where you think stock won't go**

**The wider call spread costs less in premium but provides the same protection benefit IF you're right about direction.**

### 2. Example

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condor.png?raw=true" alt="broken_wing_condor" width="700">
</p>

**Setup:**

- SPY at $450 (bullish trend)
- Technical: Support at $445, resistance at $460
- Conviction: More likely to break up than down

**Symmetric Iron Condor (no conviction):**

- Sell $440/$435 put spread for $1.50
- Sell $460/$465 call spread for $1.50
- Net credit: $3.00
- Max risk: $2.00 on either side
- Capital required: $500 per condor

**Broken Wing Condor (bullish conviction):**

- Sell $440/$435 put spread for $1.50 (same)
- Sell $460/$475 call spread for $2.00 (broken!)
- Net credit: $3.50
- Max risk: $2.00 (put side), $11.50 (call side)
- Capital required: $1,150 (on broken side)

**What you're really doing:**

$$
\begin{align}
\text{Economic Position} &= \text{Sell range insurance (\$435-\$460)} \\
&+ \text{Concentrate risk on downside} \\
&+ \text{Reduce upside risk with wide spread} \\
&+ \text{Express bullish conviction}
\end{align}
$$

**Scenarios:**

| SPY at Expiry | Symmetric IC | Broken Wing |
|--------------|--------------|-------------|
| $450 | Gain: $300 | Gain: $350 (better) |
| $445 | Gain: $300 | Gain: $350 (better) |
| $440 (short put) | Loss: ~$100 | Loss: ~$100 (same) |
| $435 (long put) | Loss: -$200 (max) | Loss: -$150 (better!) |
| $460 (short call) | Loss: ~$100 | Loss: ~$100 (same) |
| $475 (long call) | Loss: -$200 (max) | Loss: -$1,150 (worse!) |
| $490+ | Loss: -$200 (max) | Loss: -$1,150 (max) |

**The asymmetry is the key!**

If you're right about bullish bias:
- Upside move → still profit (spread very wide)
- Sideways → profit (keep credit)
- Small downside → small loss
- **Only big downside hurts (which you don't expect)**

### 3. The Conviction-Based Capital Allocation

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_theta.png?raw=true" alt="theta_asymmetry" width="600">
</p>

**Think like a portfolio manager with directional conviction:**

**When you construct a broken wing:**

- You're allocating capital asymmetrically
- More protection where you expect stock to go
- Less protection where you don't expect stock to go
- **Trading capital efficiency for directional edge**

**Capital comparison:**

**Regular Iron Condor:**

- $5-wide on both sides
- Max risk: $200 per side
- Total capital: $400
- Return on capital: $300/$400 = 75%

**Broken Wing (bullish):**

- Put side: $5-wide (risk $200)
- Call side: $10-wide (risk $650)
- Total capital: $650 (higher!)
- Return on capital: $350/$650 = 54%
- **But probability-weighted return is better if right about direction**

### 4. Why This Perspective Matters

**Understanding broken wings as conviction trades helps you:**

1. **Express directional views with defined risk:**

   - Not pure directional (like long calls)
   - Not pure neutral (like iron condors)
   - **Hybrid: directional bias + income**

2. **Optimize capital efficiency:**

   - Don't waste capital protecting unlikely moves
   - Concentrate protection where needed
   - Use saved premium to improve credit

3. **Manage risk asymmetrically:**

   - Know which side is your "danger zone"
   - Monitor the tight spread closely
   - Let wide spread take care of itself

4. **Understand probability-weighted outcomes:**

   - Better max profit (higher credit)
   - Same max loss on expected side
   - Worse max loss on unexpected side
   - **Net positive if conviction correct >60% of time**

### 5. The Strategic Advantage of Asymmetric Risk

**Why traders prefer broken wings when they have conviction:**

**Scenario: Bullish on SPY at $450, but want income too**

**Option A: Bull Call Spread (pure directional)**
- Buy $450 call, sell $460 call
- Cost: $5 (debit)
- Need rally to profit
- **Risk: Time decay if wrong**

**Option B: Regular Iron Condor (pure neutral)**
- Symmetric wings
- Collect $3.00
- No directional bias
- **Miss opportunity if rally happens**

**Option C: Broken Wing Condor (directional + income)**
- Wide call spread (allow rally)
- Tight put spread (protect downside)
- Collect $3.50
- **Profit if flat OR rallies, protected if small drop**

**The broken wing gives you:**

- Credit collection (income strategy)
- Directional bias (conviction expression)
- Defined risk (sleep at night)
- **Best of both worlds: income + directional edge**

**This is why sophisticated traders use broken wings when they have moderate conviction but want to collect premium.**

---

## Key Terminology

**Broken Wing:**

- One side with unequal strike spacing
- Creates asymmetric risk profile
- Wider spread = lower cost = less protection
- "Broken" because it's not symmetric

**Regular Side:**

- The side with normal strike spacing
- Usually where you expect stock might move
- Tighter spread = higher cost = more risk
- Your "danger zone"

**Wide Side:**

- The side with wide strike spacing
- Usually opposite your conviction
- Far OTM protection = cheap
- Acts as distant "just in case" insurance

**Skip Strike:**

- Extremely wide spacing (e.g., $10+ wide)
- Long option very far OTM
- Near-zero cost
- Essentially unhedged but technically defined risk

**Inverted Risk:**

- When broken side has MORE max loss than regular side
- Normal for broken wings
- Acceptable because probability-weighted risk lower

**Directional Skew:**

- The bias created by asymmetric wings
- Bullish skew: wide call spread
- Bearish skew: wide put spread
- Determines which direction you're favoring

---

## Why Use Broken Wing Condors?

**Use cases for different variations:**

### 1. Bullish Broken Wing (Wide Call Side)

**When to use:**

1. **Moderate bullish conviction:**

   - Uptrend intact but overbought
   - Expect consolidation or continued rally
   - Don't expect major pullback
   - Want to collect premium during rally

2. **Post-correction setups:**

   - Stock bottomed, starting recovery
   - Downside risk reduced
   - Upside potential opening
   - Want income during recovery phase

3. **Technical breakout scenarios:**

   - Stock breaking resistance
   - New uptrend forming
   - Unlikely to reverse quickly
   - Sell puts below support, wide calls above

4. **Bull market conditions:**

   - Overall market strong
   - Sector rotation favorable
   - "Buy the dip" mentality prevalent
   - Profit from bullish bias with income

5. **Reduced capital deployment:**

   - Want iron condor-like income
   - But limited capital
   - Accept more risk on unlikely upside
   - Reduce margin requirement

**Example scenario:**

- AAPL at $180 (uptrend since $160)
- Support at $175 holding strong
- Resistance at $190
- Bullish but expect consolidation
- **Action:** Bullish broken wing condor
  - Sell $175/$170 put spread (tight)
  - Sell $190/$205 call spread (wide)
- Profit if AAPL stays above $175 or rallies
- Risk concentrated below $175 (don't expect)

### 2. Bearish Broken Wing (Wide Put Side)

**When to use:**

1. **Moderate bearish conviction:**

   - Downtrend forming
   - Expect consolidation or decline
   - Don't expect major rally
   - Want to collect premium during weakness

2. **Post-rally exhaustion:**

   - Stock topped after big move
   - Upside momentum fading
   - Downside breakout unlikely (yet)
   - Collect premium as stock rolls over

3. **Resistance rejection setups:**

   - Stock failed at major resistance
   - Lower high forming
   - Unlikely to break out quickly
   - Sell calls above resistance, wide puts below

4. **Bear market conditions:**

   - Overall market weak
   - Sector under pressure
   - Rallies are short-lived
   - Profit from bearish bias with income

5. **Overvaluation plays:**

   - Stock expensive fundamentally
   - Sentiment shift underway
   - Gradual decline expected
   - Wide put side allows slow bleed

**Example scenario:**

- TSLA at $220 (down from $280)
- Resistance at $230
- Support at $200
- Bearish but consolidating
- **Action:** Bearish broken wing condor
  - Sell $230/$235 call spread (tight)
  - Sell $200/$185 put spread (wide)
- Profit if TSLA stays below $230 or declines
- Risk concentrated above $230 (don't expect)

---

## The Greeks

**How Greeks differ from regular iron condors:**

### 1. Delta (Directional Risk)

**Bullish Broken Wing:**

$$
\Delta_{\text{BWC bullish}} \approx +0.10 \text{ to } +0.25 \quad (\text{net positive})
$$

**What this means:**

- Slightly bullish delta (unlike neutral IC)
- Benefits from upward moves
- Hurt by downward moves (more than IC)
- Acts like owning 10-25 shares per condor

**Bearish Broken Wing:**

$$
\Delta_{\text{BWC bearish}} \approx -0.10 \text{ to } -0.25 \quad (\text{net negative})
$$

**What this means:**

- Slightly bearish delta
- Benefits from downward moves
- Hurt by upward moves (more than IC)
- Acts like shorting 10-25 shares per condor

**Delta evolution:**

The asymmetry creates interesting delta behavior:
- If stock moves toward tight spread → delta increases rapidly (danger!)
- If stock moves toward wide spread → delta barely changes (safe)
- This creates **path-dependent risk**

**Example - Bullish BWC:**

| Stock Move | Regular IC Delta | Bullish BWC Delta | Difference |
|-----------|-----------------|------------------|------------|
| +$5 rally | -0.05 | -0.02 | Less negative (good) |
| Flat | 0.00 | +0.15 | Slight positive (edge) |
| -$5 drop | +0.05 | +0.35 | More positive (dangerous!) |

### 2. Theta (Time Decay)

**Broken wing condors have positive theta, but distributed unevenly:**

$$
\Theta_{\text{tight spread}} \approx +0.08/\text{day} \quad (\text{concentrated})
$$

$$
\Theta_{\text{wide spread}} \approx +0.02/\text{day} \quad (\text{diffuse})
$$

**Total theta:** Similar to regular IC, but composition differs

**What this means:**

- Tight spread decays faster (good if stock cooperates)
- Wide spread decays slower (less help if stock moves wrong way)
- Net positive theta overall
- But **theta benefit concentrated on one side**

**Theta acceleration pattern:**


**Time to expiration vs. theta:**

- Regular side: High theta (normal decay)
- Broken side: Low theta (far OTM)
- **Total theta close to symmetric IC**
- But risk profile very different!

**The theta trap in broken wings:**

Unlike regular ICs where theta is symmetric, broken wings have:
- Most theta benefit on tight spread side
- If stock moves to tight spread → lose faster than theta helps
- If stock moves to wide spread → theta helps less
- **Need directional conviction to work WITH theta**

### 3. Gamma (Delta Risk)

**Broken wings have very asymmetric gamma:**

$$
\Gamma_{\text{tight spread}} \approx -0.05 \quad (\text{high risk})
$$

$$
\Gamma_{\text{wide spread}} \approx -0.01 \quad (\text{low risk})
$$

**What this means:**

- Tight spread has high gamma risk (danger zone)
- Wide spread has low gamma risk (safe zone)
- Delta accelerates quickly toward tight spread
- Delta barely moves toward wide spread

**Gamma evolution:**

| Stock Position | Tight Spread Gamma | Wide Spread Gamma | Management Need |
|---------------|-------------------|------------------|----------------|
| At tight short strike | **Extreme** | Minimal | **Emergency** |
| Near tight spread | High | Low | Close monitoring |
| In the middle | Medium | Low | Watch theta work |
| Near wide spread | Low | Medium | Comfortable hold |
| At wide short strike | Minimal | Moderate | Unlikely scenario |

**The gamma squeeze asymmetry:**

This is critical to understand:
- Stock approaching tight spread = gamma explosion
- Stock approaching wide spread = mild gamma increase
- **Risk management must focus on tight spread side!**

### 4. Vega (Volatility Risk)

**Broken wings have negative vega like all short premium strategies:**

$$
\text{Vega}_{\text{BWC}} \approx -0.25 \text{ to } -0.40
$$

**What this means:**

- IV increase hurts position (both sides)
- IV spike can create losses even if stock flat
- IV contraction helps position
- Vega risk similar magnitude to regular IC

**But vega distribution matters:**

**Regular IC:**

- Vega distributed evenly across both spreads
- Symmetric risk to IV changes

**Broken Wing:**

- Tight spread: Higher vega (closer to ATM)
- Wide spread: Lower vega (far OTM)
- **IV spike hurts tight spread more**

**Vega scenarios:**

**Bullish BWC during IV spike:**

- Put spread (tight): Vega hurts significantly
- Call spread (wide): Vega hurts minimally
- Net: Still negative vega, but concentrated on put side
- **If IV spike from fear (downside), double whammy!**

**The vega trap:**

Broken wings can suffer worse than regular ICs during panics:
- IV spikes typically from downside fear
- Puts get more expensive faster than calls
- Your tight put spread gets crushed
- Your wide call spread barely helps
- **Bearish IV spike + bullish BWC = worst case**

### 5. Rho (Interest Rate Risk)

**Impact:** ~$0.01-0.02 per 1% rate change

**Can ignore for most trading**

---

## Strike Selection Strategy

**Where you place strikes determines everything in broken wings:**

### 1. The Asymmetric Strike Spacing Framework

**Core principle:**

$$
\text{Tight Spread Width} : \text{Wide Spread Width} = 1:2 \text{ to } 1:3
$$

**Standard ratios:**

| Tight Spread | Wide Spread | Ratio | Use Case |
|-------------|-------------|-------|----------|
| $5 | $10 | 1:2 | Moderate asymmetry |
| $5 | $15 | 1:3 | Strong asymmetry |
| $5 | $20 | 1:4 | Extreme asymmetry |
| $10 | $20 | 1:2 | High-priced stocks |

**Example - Bullish BWC on $100 stock:**

**Conservative (1:2 ratio):**

- Tight put spread: $95/$90 ($5 wide)
- Wide call spread: $105/$115 ($10 wide)
- Moderate asymmetry

**Aggressive (1:3 ratio):**

- Tight put spread: $95/$90 ($5 wide)
- Wide call spread: $105/$120 ($15 wide)
- Strong asymmetry, very bullish

### 2. The Delta-Based Selection (Recommended)

**Professional approach:**

**Tight spread (danger zone):**

- Short strike: 20-30 delta
- Long strike: 10-15 delta
- Width: $5 (standard stock)
- **High probability but concentrated risk**

**Wide spread (safe zone):**

- Short strike: 15-20 delta
- Long strike: 2-5 delta (very far OTM)
- Width: $10-$20
- **Lower probability, diffuse risk**

**Example - SPY at $450:**

**Bullish BWC:**

- Short $440 put (20-delta)
- Long $435 put (12-delta)
- Short $465 call (18-delta)
- Long $480 call (3-delta) ← skip strike!

**Credit analysis:**

- Put spread: $1.50 credit (risk $3.50)
- Call spread: $1.80 credit (risk $13.20!)
- Net: $3.30 credit
- **Max risk: $13.20 on call side (unlikely)**
- **Max risk: $1.70 on put side (concentrated)**

### 3. The Probability-Weighted Approach

**Optimizing expected value:**

$$
\text{EV} = P_{\text{win}} \times \text{Credit} - P_{\text{tight loss}} \times \text{Tight Loss} - P_{\text{wide loss}} \times \text{Wide Loss}
$$

**Example calculation:**

**Bullish BWC:**

- Credit: $3.30
- Tight side (put) loss: $1.70
- Wide side (call) loss: $13.20

**Probabilities:**

- Win (between spreads): 70%
- Tight side loss: 25%
- Wide side loss: 5%

$$
\text{EV} = 0.70 \times \$3.30 - 0.25 \times \$1.70 - 0.05 \times \$13.20
$$

$$
\text{EV} = \$2.31 - \$0.43 - \$0.66 = \$1.22 \quad (\text{positive!})
$$

**The key insight:**

Even though wide side has huge max loss ($13.20), it's so unlikely (5%) that expected value is still positive. This is the mathematical justification for broken wings.

### 4. Credit Collection Targets

**How much credit should you collect?**

**For bullish BWC (tight put side):**

$$
\text{Target Credit} = 40\%-60\% \text{ of tight spread width}
$$

**Example:**

- Tight spread: $5 wide
- Target credit: $2.00-$3.00 total
- If collecting <$2.00 → strikes too far out
- If collecting >$3.50 → strikes too close (dangerous)

**Credit composition:**

Ideally:
- Tight spread contributes: 50-60% of total credit
- Wide spread contributes: 40-50% of total credit
- This balance indicates proper strike selection

**Example:**

- Total credit target: $3.00
- Put spread (tight): $1.80 (60%)
- Call spread (wide): $1.20 (40%)
- **Good balance**

### 5. The "Golden Zone" Setup

**Optimal strike configuration for bullish BWC:**

**For stock at $100:**

- **Tight put spread:** $95/$90
  - Short strike: 2-3% below current price
  - Width: 5% of stock price
  - Delta: 20-30 on short strike
  
- **Wide call spread:** $105/$120
  - Short strike: 5% above current price
  - Width: 15% of stock price
  - Long strike delta: <5 (skip strike)

**This creates:**

- Win zone: $90-$105 (15-point range)
- Small risk zone: $90-$85 (5 points)
- Large but unlikely risk: >$120 (20+ points away)

**Probability profile:**

- 75% probability between spreads
- 20% probability hit tight spread
- 5% probability hit wide spread
- **Expected value strongly positive**

---

## Time Selection

### 1. Entry Timing

**Different from regular ICs:**

**Sell broken wing condors 45-60 days to expiration:**

**Why longer than regular ICs (30-45)?**

1. **Asymmetric gamma needs more time:**

   - Tight spread has high gamma risk
   - Need time buffer for adjustments
   - 45-60 DTE gives management flexibility

2. **Directional thesis needs time to play out:**

   - Unlike neutral IC, you have conviction
   - Stock needs time to move in your favor
   - Or time to NOT move against you

3. **Better credit collection:**

   - Longer DTE = fatter premiums
   - Wide spread benefits more from time premium
   - Improves risk/reward ratio

4. **Vega protection:**

   - More time = less vega sensitivity
   - IV spikes hurt less with time buffer
   - Can ride out short-term volatility

**Comparison:**

| DTE | Theta/Day | Gamma Risk | Credit | Adjustment Time | Verdict |
|-----|-----------|------------|--------|----------------|---------|
| 60+ | Low | Very Low | High | Plenty | Good for BWC |
| 45-60 | **Optimal** | **Low** | **Good** | **Ideal** | **✓ Best** |
| 30-45 | Higher | Medium | Medium | Adequate | Acceptable |
| <30 | High | **High** | Lower | Rushed | Risky for BWC |

### 2. Exit Timing

**Broken wings need more nuanced exits than regular ICs:**

### 3. Rule 1

**Same as regular credit spreads:**

- Close when you've captured 50% of max credit
- Optimal risk/reward balance
- Frees capital for new opportunities

**Example:**

- Collected $3.00 credit
- Close when spread worth $1.50
- Take $1.50 profit, move on

### 4. Rule 2

**Close immediately if stock approaches tight spread short strike:**

**Warning signs:**

- Stock within 2% of tight spread short strike
- Tight spread delta reaches 0.50
- Gamma risk accelerating

**Action:**

- Don't wait for stop loss
- Don't try to adjust
- **Close entire condor immediately**

**Example - Bullish BWC:**

- SPY at $450
- Tight spread: Sell $440 put
- SPY drops to $442 (approaching!)
- **Close NOW, don't wait for $440**

**Why so aggressive?**

Because of asymmetric gamma:
- Tight spread gamma can explode quickly
- Wide spread won't save you
- One overnight gap through tight spread = disaster
- **Better to take small loss early than big loss later**

### 5. Rule 3

**Close broken wings at 30 DTE regardless:**

**Rationale:**

- Gamma risk increases exponentially <30 DTE
- Tight spread becomes too dangerous
- Wide spread doesn't help enough
- Theta benefit not worth gamma risk

**Comparison to regular IC:**

- Regular IC: Close at 21 DTE
- Broken wing: Close at 30 DTE
- **Earlier exit because of asymmetric gamma**

### 6. Rolling Positions

**Broken wings require different rolling strategies:**

### 7. When Stock Threatens Tight Spread

**Scenario:** Stock moving toward danger zone

**Option 1: Roll the entire condor out**
- Buy back current BWC
- Sell new BWC at same strikes, next month
- Collect additional credit
- Reset time for thesis to work

**Example:**

- Bullish BWC on SPY
- SPY dropped from $450 to $442
- Tight put spread threatened
- **Roll:** Close current, sell next month's same strikes
- Collect $0.50 additional credit
- New expiration: +30 days

**Option 2: Convert to regular IC (reduce asymmetry)**
- Close threatened tight spread
- Replace with more conservative spread
- Accept lower credit but reduce risk
- Essentially "fix the broken wing"

**Example:**

- Bullish BWC: $440/$435 put, $465/$480 call
- Put spread threatened
- **Convert:** Close $440/$435, sell $438/$433
- New put spread further out
- Now more symmetric, less risky

### 8. When to NOT Roll

**Don't roll if:**

- Thesis completely broken (fundamental change)
- Stock blasted through short strike (already lost)
- Already rolled once (don't chase)
- Better to take loss and move on

**Example of thesis break:**

- Bullish BWC on tech stock
- Fed announces rate hikes (bearish for growth)
- Your bullish thesis invalidated
- **Exit, don't roll**

### 9. The Multi-Month Strategy

**Advanced approach: Laddering broken wings**

**Concept:**

- Open multiple BWCs with different expirations
- Each month: close expiring, open new one
- Creates continuous income stream
- Diversifies time risk

**Example structure:**

- Month 1: Open 60-DTE BWC
- Month 2: Open another 60-DTE BWC (now have 2)
- Month 3: Open third 60-DTE BWC (now have 3)
- Month 4: Close first (30 DTE left), open fourth
- **Continuous 3-month rolling ladder**

**Benefits:**

- Smooth income (not lumpy)
- Time diversification
- Always have positions in sweet spot (30-60 DTE)
- Easier to manage systematically

---

## Maximum Profit and Loss Analysis

### 1. Mathematical Formulas

**Broken Wing Condor (Bullish):**

$$
\text{Max Profit} = \text{Total Credit Received}
$$

$$
\text{Max Loss (Tight Side)} = \text{Put Spread Width} - \text{Total Credit}
$$

$$
\text{Max Loss (Wide Side)} = \text{Call Spread Width} - \text{Total Credit}
$$

$$
\text{Break-Even (Put)} = \text{Short Put} - \text{Total Credit}
$$

$$
\text{Break-Even (Call)} = \text{Short Call} + \text{Total Credit}
$$

**Example:**

- Stock at $100
- Sell $95/$90 put spread for $2.00
- Sell $105/$120 call spread for $1.50
- Net credit: $3.50

**Calculations:**

- Max profit: $3.50 × 100 = $350
- Max loss (puts): ($5 - $3.50) = $1.50 × 100 = $150
- Max loss (calls): ($15 - $3.50) = $11.50 × 100 = $1,150
- Break-even (put): $95 - $3.50 = $91.50
- Break-even (call): $105 + $3.50 = $108.50

**Profit/loss table:**

| Stock Price | Put Spread | Call Spread | Total P/L |
|------------|-----------|-------------|----------|
| $120+ | $0 | -$11.50 | **-$1,150** (max loss) |
| $115 | $0 | -$6.50 | -$650 |
| $108.50 (BE) | $0 | $0 | $0 |
| $100 | $0 | $0 | **+$350** (max profit) |
| $91.50 (BE) | $0 | $0 | $0 |
| $90 | -$1.50 | $0 | **-$150** (max loss) |
| <$90 | -$1.50 | $0 | **-$150** (max loss) |

### 2. Risk/Reward Asymmetry Analysis

**The critical question: Is the asymmetry worth it?**

**Symmetric Iron Condor comparison:**

- $5 wide both sides
- Collect $3.00
- Max loss: $2.00 on either side
- Risk/reward: 2:3 = 0.67:1

**Broken Wing Condor:**

- Tight side: $5 wide
- Wide side: $15 wide
- Collect $3.50
- Max loss: $1.50 (tight), $11.50 (wide)
- Risk/reward: Complex!

**Probability-weighted analysis:**

Assume:
- 70% probability between strikes (win)
- 25% probability tight side loss
- 5% probability wide side loss

**Expected value:**

**Symmetric IC:**
$$
\text{EV} = 0.70(\$3.00) - 0.15(\$2.00) - 0.15(\$2.00) = \$2.10 - \$0.30 - \$0.30 = \$1.50
$$

**Broken Wing:**
$$
\text{EV} = 0.70(\$3.50) - 0.25(\$1.50) - 0.05(\$11.50)
$$
$$
= \$2.45 - \$0.375 - \$0.575 = \$1.50
$$

**Interesting result: Same EV if probabilities hold!**

**But the reality:**

- Symmetric IC: Predictable, consistent
- Broken wing: Higher variance, conviction-dependent
- **Broken wing better ONLY if your directional thesis correct**

### 3. Return on Capital Analysis

**The capital efficiency question:**

**Symmetric IC:**

- Max risk either side: $200
- Capital requirement: $200
- Max profit: $300
- ROC: $300/$200 = 150%

**Bullish BWC:**

- Max risk (tight): $150
- Max risk (wide): $1,150
- Capital requirement: $1,150 (broker holds for wider spread)
- Max profit: $350
- ROC: $350/$1,150 = 30%

**The capital efficiency problem:**

Broken wings require MORE capital (for wide spread) but offer same/similar profit. This seems inefficient!

**Why trade them then?**

1. **Probability-weighted capital:**

   - Wide spread loss is 5% probable
   - Real capital at risk: $150 (25%) + $1,150(5%) = $37.50 + $57.50 = $95
   - Effective ROC: $350/$95 = 368%!

2. **Directional edge:**

   - If you're right about direction >70% of time
   - Broken wing outperforms
   - Regular IC has no edge

3. **Flexibility:**

   - Can adjust tight side easily
   - Wide side unlikely to need adjustment
   - Management simpler in practice

**The verdict:**

Broken wings make sense when:
- You have directional conviction
- You're willing to accept higher capital requirement
- Your edge justifies the asymmetry
- **Not about capital efficiency, about directional conviction**

---

## When to Enter Broken Wing Condors

### 1. Market Conditions

**Best environments:**

### 2. Trending Markets with Pullbacks

**The sweet spot for broken wings:**

- Clear trend established (up or down)
- Healthy pullback within trend
- Trend likely to resume
- Want income during consolidation

**Bullish example:**

- SPY in uptrend from $420 → $460
- Pullback to $450 (normal)
- Support at $445 holding
- **Enter bullish BWC:** Sell $445/$440 puts, $470/$485 calls
- Profit from consolidation or renewed rally

**Bearish example:**

- TSLA in downtrend from $300 → $220
- Bounce to $230 (dead cat)
- Resistance at $240
- **Enter bearish BWC:** Sell $240/$245 calls, $210/$195 puts
- Profit from consolidation or continued decline

### 3. Post-Event Stabilization

**After volatility spike settles:**

- Earnings, FDA, Fed decision, etc.
- Event passed, direction clarified
- IV still elevated but dropping
- Stock finding new range

**Example:**

- NFLX earnings beat
- Stock gaps from $380 → $420
- Settles at $415 over 2 days
- IV: 60% → 40% (still elevated)
- **Enter bullish BWC:**

  - Sell $405/$400 puts (below gap)
  - Sell $440/$455 calls (above recent high)
- Profit from consolidation with bullish bias

### 4. Range Extension Setups

**When range is expanding in your favor:**

- Stock breaking out of range
- New support/resistance forming
- Direction clear but not parabolic
- Want to capture new range with income

**Example:**

- QQQ trading $360-$370 for months
- Breaks above $370 (bullish breakout)
- New support at $370
- New resistance unknown (maybe $385?)
- **Enter bullish BWC:**

  - Sell $368/$363 puts (below new support)
  - Sell $390/$405 calls (wide above)
- Profit from consolidation in new higher range

### 5. Technical Setups

**Combining broken wings with technicals:**

### 6. Bullish BWC

**1. Trendline bounces:**

- Stock pulls back to rising trendline
- Bullish reversal candle at trendline
- **Sell puts below trendline, wide calls above**

**2. Moving average support:**

- Stock riding 20/50 EMA higher
- Dip to EMA holds
- **Sell puts below EMA, wide calls above resistance**

**3. Breakout consolidations:**

- Stock breaks resistance
- Consolidates above old resistance (new support)
- **Sell puts below new support, wide calls well above**

**4. Bull flag patterns:**

- Strong rally, tight consolidation
- Expect continuation
- **Sell puts below flag, wide calls above prior high**

### 7. Bearish BWC

**1. Trendline rejections:**

- Stock bounces to falling trendline
- Bearish reversal at trendline
- **Sell calls above trendline, wide puts below**

**2. Moving average resistance:**

- Stock below declining 20/50 EMA
- Rally to EMA rejected
- **Sell calls above EMA, wide puts below support**

**3. Breakdown consolidations:**

- Stock breaks support
- Consolidates below old support (new resistance)
- **Sell calls below old support, wide puts well below**

**4. Bear flag patterns:**

- Strong drop, weak bounce
- Expect continuation down
- **Sell calls above flag, wide puts below prior low**

### 8. Volatility-Based Entry

**Using IV rank for timing:**

**Best IV conditions for broken wings:**

**Medium IV (40-60 percentile):**

- Not too high (safer entry)
- Not too low (still collectable premium)
- **Goldilocks zone for BWC**

**Why not high IV (>70%)?**
- Regular ICs better in very high IV
- Tight spread in BWC too risky in high IV
- IV crush can hurt tight spread badly
- **Use symmetric ICs instead**

**Why not low IV (<30%)?**
- Premiums too thin
- Not worth the asymmetric risk
- **Wait for better conditions**

**The IV sweet spot logic:**

Broken wings work best in moderate IV because:
- Wide spread still cheap (far OTM)
- Tight spread not too expensive (manageable risk)
- IV unlikely to spike dramatically
- Directional edge more important than IV edge

---

## When to Avoid Broken Wing Condors

### 1. Very High IV Environments

**The problem:**

- VIX >35, stock IV >70%
- Fat premiums tempting
- But tight spread too risky
- IV crush can be devastating

**Example:**

- Market panic, VIX at 40
- AAPL IV at 60%
- Sell bullish BWC: $170/$165 puts, $190/$210 calls
- Collect $5.00 (amazing!)
- But market gap down overnight
- Put spread blows through
- **Lost $500 instead of profiting**

**Why this fails:**

- High IV = high realized volatility likely
- Big moves more probable
- Tight spread gets tested
- Wide spread doesn't help enough

**Alternative:** Use symmetric IC in high IV instead

### 2. Parabolic Moves

**Never fight momentum with broken wings:**

**The disaster scenario:**

- Stock in parabolic rally
- You think "it's overdone"
- Sell bearish BWC
- Stock continues ripping
- **Tight call spread destroyed**

**Example:**

- GME at $40, rallying
- Sell bearish BWC: $50/$55 calls (tight), $35/$20 puts (wide)
- "Surely it won't go past $50..."
- GME goes to $480
- **Account blown up**

**Rule:** Wait for consolidation, never fight parabola

### 3. Binary Events Approaching

**The known-unknown trap:**

Events coming in 0-3 days:
- Earnings
- FDA decisions
- Fed meetings
- Merger votes

**Why avoid:**

- Gap risk through tight spread
- Probability models invalid
- Wide spread won't save you
- **One event can wipe out months of gains**

**Example:**

- Biotech at $40
- FDA decision tomorrow
- Sell bullish BWC
- FDA rejects → stock to $15
- **Max loss on tight put spread**

### 4. When You Have No Directional Conviction

**The most important rule:**

**If you have NO conviction:**

- Use symmetric iron condor instead
- Don't use broken wing "just for higher credit"
- Asymmetric risk requires asymmetric confidence
- **Broken wing without conviction = gambling**

**Example mistake:**

- SPY at $450, no clear direction
- "I'll sell bullish BWC for extra credit"
- No technical reason, no conviction
- Just like the credit more
- SPY drops to $430 (normal pullback)
- **Tight spread hit, regret using broken wing**

**Rule:** Broken wing = directional strategy. No direction = no broken wing.

### 5. Low Liquidity Underlyings

**The exit problem:**

- Stock with low volume
- Wide bid-ask spreads
- **Can't exit when needed**

**Issues:**

- Enter at mid-price
- Need to exit emergency
- Bid-ask $2 wide
- **Slippage kills profitability**

**Minimum liquidity requirements:**

- Stock volume: >1M shares/day
- Option volume: >500 contracts/day
- Bid-ask spread: <$0.15 for ATM options
- **Stick to major names for BWC**

---


---


---

## Economic Interpretation

**Understanding what broken wing condors REALLY represent economically:**

### 1. The Core Economic Trade-Off

Broken wing condors represent a refined economic proposition: **trading symmetric insurance for asymmetric insurance while collecting premium**, specifically tailored to exploit directional bias within defined ranges.

**Economic equivalence:**

$$
\text{BWC} = \underbrace{\text{Iron Condor}}\_{\text{Symmetric}} + \underbrace{\text{Directional Skew}}\_{\text{Asymmetric}} + \underbrace{\text{Credit Enhancement}}\_{\text{Wider Wing}}
$$

**The transformation:**
- Standard iron condor: Equal wings both sides (neutral)
- **Broken wing condor:** One wing wider (directional bias + more credit)
- **Result:** Higher credit, skewed risk matches market view

**Why this matters economically:**
- **Standard condor:** Betting stock stays in range (neutral view)
- **Broken wing condor:** Betting stock stays in range BUT has directional bias
- **Credit boost:** Extra premium from wider wing compensates for accepting more risk on one side

### 2. Why This Structure Exists Economically

Markets create broken wing condors because participants have **asymmetric risk preferences**:

**1. Directional conviction with range-bound behavior:**

Most traders face this common situation:
- **Belief:** "Stock will stay $95-$105 (range-bound)"
- **Plus:** "More likely to stay above $100 than below" (directional bias)
- **Challenge:** How to express BOTH views simultaneously?

**Standard iron condor fails:**
- Equal wings both sides = no directional bias expressed
- Symmetric risk = doesn't match asymmetric market view
- Lower credit = less attractive

**Broken wing condor succeeds:**
- Wider downside wing = "I'm comfortable with more downside risk"
- Narrow upside wing = "I want protection on upside"
- **Higher credit:** Compensated for accepting skewed risk
- **Matches view:** Range-bound + bullish bias = exactly what you want

**2. Volatility smile exploitation with directional edge:**

**The volatility skew reality (equity markets):**

$$
\text{IV}_{OTM\;Put} > \text{IV}_{ATM} > \text{IV}_{OTM\;Call}
$$

**Standard iron condor:**
- Sell equal-width put and call spreads
- Collect moderate premium from both sides
- Miss opportunity to exploit skew

**Broken wing condor (bullish):**
- **Wide put spread:** Sell expensive OTM puts (rich IV), buy far OTM puts (even richer IV)
  - But net effect: Collect more premium per width
- **Narrow call spread:** Sell OTM calls (cheap IV), buy near OTM calls
  - Less premium, but less risk
- **Net:** Collect MORE total credit by exploiting put skew

**Example:**
- Standard IC: $90/$95 put spread + $105/$110 call spread = $3.00 credit
- Broken wing: $85/$95 put spread (wider) + $105/$108 call spread (narrower) = $3.80 credit
- **Extra $0.80** from exploiting skew while matching bullish bias

**3. Capital efficiency through enhanced credit:**

**The credit collection advantage:**

Standard IC might collect $3 credit on $5 wide spreads:
- Risk: $2 per spread ($5 width - $3 credit)
- ROI potential: $3 / $2 = 150%

Broken wing IC collects $4 credit on asymmetric spreads:
- Wide wing: $10, Narrow wing: $3
- Risk: Typically $6 on wide side ($10 - $4 credit)
- ROI potential: $4 / $6 = 67%... wait that's worse.

Actually, let me reconsider. The max risk for broken wing condor is:
$$
\text{Max Risk} = \text{Wider Wing Width} - \text{Total Credit}
$$

If wider wing is $10 and total credit is $4:
- Max risk = $10 - $4 = $6
- Max profit = $4 (credit)
- ROI = $4 / $6 = 67%

Hmm, that's actually lower ROI than standard. But the advantage is **higher win probability** because:
- Wider wing = more room for stock to move on that side
- Matches directional bias = more likely to stay in profitable zone

So it's not about higher ROI per se, but about **higher probability-adjusted returns**.

### 3. Professional Institutional Perspective

**How institutions use broken wing condors:**

**1. Portfolio overlay strategies:**

**Hedging scenario:**
- Long $100M equity portfolio
- Want range-bound income
- BUT: Willing to risk more on downside (portfolio already long)
- **NOT willing to cap upside** (want to participate in rallies)

**Solution:** Sell broken wing condors with **wide put spreads, narrow call spreads**
- Collect $50k monthly premium
- Risk on downside: $150k (but offset by long equity portfolio appreciation if up)
- Risk on upside: $50k (narrow call spread limits participation slightly)
- **Net effect:** Income generation + asymmetric hedge

**2. Earnings volatility trading:**

Professionals know earnings moves follow patterns:
- **Technology stocks:** 60% stay ±5%, 30% rally 7-12%, 10% crash 7-12%
- **Optimal structure:** Broken wing with wide put spread (protect against crash), narrow call spread (participate in rallies)

**Example:**
- AAPL at $180 pre-earnings
- Sell BWC: $170/$175 put spread (wide), $185/$187 call spread (narrow)
- Credit: $3.50

**Outcomes:**
- Stock stays $175-$185 (60%): Keep $3.50 credit ✓
- Stock rallies $190+ (30%): Small loss $1.50 (not too bad)
- Stock crashes $165 (10%): Max loss $1.50 ($5 wide - $3.50 credit)

**Probability-weighted return:**
- 0.60 × $3.50 + 0.30 × (-$1.50) + 0.10 × (-$1.50) = $2.10 - $0.45 - $0.15 = **+$1.50 expected**

**3. Market-making and flow internalization:**

**Professional vol traders:**
- See customer order flow
- Know where customers want to buy/sell
- **Exploit imbalances** with broken wing structures

**Example:**
- Retail overbuying OTM puts (fear-driven)
- Professionals sell broken wing condors with **wide put spreads** (sell into demand)
- Collect enhanced premium from retail fear
- Narrow call spreads (cheap, low demand)

**4. Skew arbitrage:**

**Identifying mispricing:**
- OTM put IV: 40% (overpriced by 5%)
- OTM call IV: 25% (fairly priced)
- **Opportunity:** Sell put skew, hedge with call structure

**Structure:**
- Wide put spread: Capture rich put premium
- Narrow call spread: Cheap protection
- **Net:** Collect arbitrage profit from skew differential

### 4. The Behavioral Finance Angle

**Why BWCs offer edge:**

**1. Investor loss aversion asymmetry:**
- Losses hurt 2× more than equivalent gains feel good
- Investors OVERPAY for downside protection (puts expensive)
- Investors UNDERPAY for upside insurance (calls cheap)
- **BWC exploits this:** Sell expensive puts (wide spread), buy cheap calls (narrow spread)

**2. Recency bias:**
- After market drop: Everyone fears more drops (put IV spikes)
- **Opportunity:** Sell broken wing with wide put spreads
- After market rally: Fear low (put IV cheap)
- **Avoid:** Not optimal time for BWC

**3. Probability misestimation:**
- Retail traders overestimate tail risk (crash probability)
- Professionals correctly estimate tails
- **Broken wing captures difference:** Wider wing on overpriced tail

### 5. The Information Asymmetry Advantage

**When you know something market doesn't:**

**Example: Sector rotation insight**
- You observe: Money flowing from growth to value
- Market pricing: Still assumes equal vol both directions
- **Your edge:** Know upside limited (growth rolling over), downside limited (value catching bids)

**Optimal expression:**
- Broken wing on growth stocks with **narrow call spreads** (limited upside)
- Standard on value stocks (no edge)

**Result:** Collect enhanced premium from directional insight

### 6. Understanding the Economic Foundations

**Key insights from broken wing condors:**

**1. Asymmetric risk preferences are universal:**
- Every investor has directional bias
- Pure neutrality is rare
- **BWC acknowledges reality:** You have a view, structure should match

**2. Skew is persistent and exploitable:**
- Put skew exists because crashes happen (structural)
- Not a temporary mispricing
- **BWC systematically captures skew premium**

**3. Probability engineering:**
- Standard IC: 60-70% win rate
- Broken wing IC (well-designed): 65-75% win rate
- **Extra 5% edge = huge over time**

**4. Credit vs. risk optimization:**
- Not about maximizing ROI per trade
- About maximizing **probability-adjusted returns**
- BWC: Lower ROI but higher win rate = better long-term

**5. Matching structure to market regime:**
- Bullish markets: Use bullish BWC (wide put spreads)
- Bearish markets: Use bearish BWC (wide call spreads)
- **Dynamic adjustment = edge**

**The economic truth:**
- BWC don't create "free money"
- They **align risk with directional conviction**
- **Edge comes from:** Expressing multi-dimensional view (range + direction) better than symmetric structures
- **Success requires:** Being RIGHT about BOTH range AND direction more often than market expects

Understanding economic foundations helps you recognize:
- When BWCs offer genuine edge (directional view + volatility skew)
- When standard ICs are better (truly neutral view)
- How to customize wings to match specific market view and skew conditions


## Practical Guidance

**Step-by-step broken wing condor implementation:**

### 1. Critical Pre-Trade Checklist

☐ **Directional bias clear?** (Bullish → Wide puts/Narrow calls, Bearish → Wide calls/Narrow puts)  
☐ **IV 45-70th percentile?** (Optimal for credit collection + compression)  
☐ **Identify wide wing** (This is your risk side - can you accept it?)  
☐ **Range identified?** (Support/resistance defining profit tent)  
☐ **30-60 DTE?** (Sweet spot for theta)  
☐ **Credit ≥ $3?** (Worthwhile after costs)  
☐ **Liquid strikes?** (OI > 500, spread < 10% per leg)  
☐ **Calculate max loss:** Wide wing - Credit

### 2. Step 1

**CRITICAL: Match structure to conviction:**

**Bullish bias (expect range-bound with upside tilt):**
- **Structure:** Wide put spreads (10-wide), narrow call spreads (2-3 wide)
- **Risk:** Downside (if crashes through puts)
- **Safe:** Upside (narrow calls protect)
- **Thesis:** "Stock will stay $440-$455, more likely to drift up than down"

**Bearish bias (expect range-bound with downside tilt):**
- **Structure:** Narrow put spreads (2-3 wide), wide call spreads (10-wide)
- **Risk:** Upside (if rallies through calls)
- **Safe:** Downside (narrow puts protect)
- **Thesis:** "Stock will stay $95-$110, more likely to drift down than up"

**NO clear bias → Use standard iron condor instead** (not BWC)

### 3. Step 2

**Wing width ratios:**
- **Wide wing:** 8-12 wide (risk side, more room)
- **Narrow wing:** 2-4 wide (safe side, protection)
- **Ratio:** 3:1 to 5:1 (wide:narrow)

**Example bullish BWC on SPY at $450:**
- Put spread: $440/$430 (10-wide, risk side)
- Call spread: $455/$457 (2-wide, safe side)
- **Credit target:** $4-5

**Position Greeks target:**
- Delta: -5 to +5 (slightly directional)
- Theta: +$20-40/day
- Vega: -10 to -20 (short vol)

### 4. Step 3

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times 2\%}{\text{(Wide Wing - Credit)} \times 100}
$$

**Example:**
- Portfolio: $50,000
- Wide wing: $10
- Credit: $4.50
- Max loss per spread: $5.50 ($550)
- **Max contracts:** $50,000 × 0.02 / $550 = **1.8 → 1-2 contracts**

**Why 2% (not 3-5%)?**
- BWCs have skewed risk (one side much larger)
- "High probability" is often overestimated
- Need buffer for sequential losses

### 5. Step 4

**Order entry:**
1. **4-leg combo order** (all simultaneously)
2. **Limit at mid-price** or $0.05 better
3. **Time:** 10:30am - 3pm EST (avoid volatility)
4. **Verify:** Check which wing is wide before submitting!

**Entry checklist:**
- [ ] Calculated max loss correctly
- [ ] Position size within 2% risk limit
- [ ] Set profit target alert (+40-50% of max profit)
- [ ] Set stop loss alert (-50% of max loss)
- [ ] Set time stop (50% time elapsed)

### 6. Step 5

**Daily monitoring:**
- Stock price relative to wings
- Days to expiration (exit by 7 DTE)
- P&L as % of max profit/loss

**Exit triggers (ANY trigger → close position):**

**Profit targets:**
- **Primary:** +40-50% of max profit
  - Example: Max $4.50, exit at +$1.80-2.25
- **Secondary:** 75% time elapsed if +25% profit
  - Example: 40 DTE, at 30 DTE, if up +25%, close

**Stop losses:**
- **Primary:** -50% of max loss
  - Example: Max loss $5.50, exit at -$2.75
- **Secondary:** Stock breaches wide wing → exit same day
- **Tertiary:** 50% time passed, position negative → exit

**Time stops:**
- **Always exit by 7 DTE** regardless of P&L
- **Exit by 10 DTE if not profitable**

### 7. Step 6

**General rule: BWCs are hard to adjust effectively**

**When to adjust (rare):**
- Deeply profitable (+60%+) and want to lock gains
- Can convert to safer structure (e.g., close threatened side)
- Have VERY strong conviction direction will reverse

**Adjustment techniques:**
1. **Close threatened side:** If call side threatened, close call spread, keep put spread
2. **Roll out in time:** Add 30 DTE, collect more credit (risky!)
3. **Widen tent:** Buy back shorts, sell further OTM (expensive)

**When to take loss instead (most times):**
- Stock broke through wide wing
- Not deeply profitable (<40%)
- Less than 21 DTE remaining
- **Default:** Close and move on

**Example bad adjustment:**
- Down -$2,000 (near max loss)
- Roll to next month for $500 credit
- **Problem:** Still at risk, now committed 30 more days
- **Better:** Take -$2,000 loss, move on fresh

### 8. Step 7

| Date | Type | Strikes | Credit | DTE | IV% | Max Loss | Exit | P&L | Win? | Notes |
|------|------|---------|--------|-----|-----|----------|------|-----|------|-------|
| 1/15 | Bull | 440/430p, 455/457c | $4.50 | 45 | 55% | $5.50 | Day 38 | +$1.00 | ✓ | Exited at target |
| 2/20 | Bear | 235/233p, 245/255c | $3.80 | 40 | 62% | $6.20 | Day 5 | -$3.10 | ✗ | Breached wide call |

**Quarterly review metrics:**
- **Win rate:** Target 65-70%
- **Average winner:** +45% of max profit
- **Average loser:** -35% of max loss (stopped out)
- **Expectancy:** Should be positive

**Calculate expectancy:**
$$
E = (W\% \times \text{Avg Win}) - (L\% \times \text{Avg Loss})
$$

Example: 0.68 × $2.00 - 0.32 × $1.80 = $1.36 - $0.58 = **+$0.78 per trade**

### 9. The BWC Trading Rules (Non-Negotiable)

**Never trade BWC when:**
1. No clear directional bias
2. IV < 40th or > 75th percentile
3. Binary event within expiration (earnings, FDA)
4. < 30 DTE or > 90 DTE
5. Illiquid (OI < 500, spread > 10%)
6. After major move (already extended)
7. Can't identify wide wing clearly

**Always:**
1. Use combo orders (4 legs simultaneously)
2. Calculate max loss before entry
3. Set alerts for all exit triggers
4. Exit by 7 DTE regardless
5. Size for 2% max risk
6. Know which wing is wide!

**The golden rule:** If you can't clearly state "I'm bullish/bearish AND comfortable with more risk on [direction] side," don't trade BWC - use standard IC instead.


## Common Mistakes Beginners Make

### 1. Using Broken Wings for More Credit (No Conviction)

**The temptation:**

- See BWC collects $3.50
- Regular IC collects $3.00
- "I'll use BWC for extra $0.50!"
- No directional thesis
- **Just greedy for credit**

**The mistake:**

- Asymmetric risk without asymmetric conviction
- When tight spread hit, regret decision
- Extra $0.50 not worth the concentrated risk

**Example:**

- SPY at $450, neutral outlook
- Regular IC: Collect $3.00 (safe)
- BWC: Collect $3.50 (risky on one side)
- SPY drops to $440 (normal)
- IC: Small loss
- BWC: **Bigger loss on tight put spread**

**The fix:**

- Only use BWC when you have directional conviction
- Extra credit must be justified by thesis
- **If neutral, use symmetric IC**

### 2. Making Tight Spread Too Tight

**The greed:**

- Want maximum credit
- Place tight spread very close to current price
- Sell 40-50 delta options
- "I'm 70% sure it won't go there..."
- **Stock moves normally, spread hit**

**The mistake:**

- Confusing probability with certainty
- 70% sure = 30% wrong = too often!
- Gamma explosion destroys position

**Example - Bullish BWC:**

- AAPL at $180
- Sell $178/$173 put spread (too close!)
- Collect $2.50 (great credit!)
- AAPL drops to $175 (normal pullback)
- **Max loss on tight spread**

**The fix:**

- Stick to 20-30 delta for tight spread short strike
- Give yourself room for normal volatility
- Don't chase extra $0.50-$1.00 credit

### 3. Ignoring the Wide Side Risk

**The complacency:**

- Focus all attention on tight spread
- Wide spread "will never happen"
- Forget it even exists
- Black swan hits wide spread
- **Caught completely off guard**

**The mistake:**

- Treating wide spread as free money
- Not monitoring it at all
- Assuming <5% probability = 0% probability
- One black swan wipes out year of gains

**Example:**

- Bullish BWC on SPY
- Tight: $440/$435 puts (monitor closely)
- Wide: $470/$495 calls (ignore)
- Flash crash rallies SPY to $485
- **"Where did this $2,500 loss come from?!"**

**The fix:**

- Set price alerts on wide spread too
- Check both sides daily
- Remember: low probability ≠ no probability
- **5% events happen 1 in 20 trades**

### 4. Holding Through Earnings/Events

**The gamble:**

- Have BWC on before earnings
- "I'll just hold through..."
- "Tight spread far enough away"
- Gap through tight spread
- **Instant max loss**

**The mistake:**

- Underestimating event volatility
- Gap risk ignored
- One earnings report destroys position

**Example:**

- NVDA at $450
- Bullish BWC: $430/$425 puts, $480/$500 calls
- Earnings tonight
- Think: "$430 is safe..."
- Earnings miss, stock gaps to $400
- **Put spread at max loss instantly**

**The fix:**

- Always close before earnings
- Even if profitable, close it
- Re-enter after event settles
- **Never hold defined risk through binary events**

### 5. Not Closing at 50% Profit

**The greed:**

- BWC at 60% profit
- "Just 10 more days for last 40%..."
- Stock reverses
- Profit erodes, turns to loss
- **Greed turned winner into loser**

**The mistake:**

- Squeezing last bit of profit
- Exposing to gamma risk
- Ignoring mathematical optimal exit

**Example:**

- Collected $3.00 credit
- Position worth $1.20 (60% profit)
- "I'll wait for $0.90..."
- Stock moves toward tight spread
- Position now worth $3.50 (losing!)
- **Should have taken $1.80 profit**

**The fix:**

- 50% profit rule is LAW
- Don't get greedy
- Free up capital, move to next trade
- **Consistent small wins > rare perfect wins**

### 6. Over-Concentrating in One Direction

**The portfolio disaster:**

- Bullish on market
- Open 5 bullish BWCs
- All on correlated stocks (AAPL, MSFT, GOOGL, etc.)
- Market correction
- **All 5 tight spreads hit simultaneously**

**The mistake:**

- False diversification
- All eggs in one directional basket
- Correlation ignored

**Example:**

- 5 bullish BWCs on tech stocks
- Collected $1,500 total
- Tech selloff
- All put spreads threatened
- Max loss: $5,000
- **Account destroyed**

**The fix:**

- Mix bullish and bearish BWCs
- Diversify across sectors
- Some conservative, some aggressive
- **Don't bet entire portfolio on one direction**

### 7. Fighting the Broken Wing Thesis

**The stubborn hold:**

- Bullish BWC established
- Macro turns bearish (Fed hawkish)
- Thesis invalidated
- "But I was right before..."
- Hold position anyway
- **Loses money fighting new reality**

**The mistake:**

- Emotional attachment to original thesis
- Not updating view with new information
- Stubbornness over flexibility

**Example:**

- Bullish BWC on growth stocks
- Fed announces faster rate hikes
- Growth stocks will suffer (clear)
- Hold position anyway (stubborn)
- **Tight put spread destroyed**

**The fix:**

- Monitor thesis constantly
- If invalidated, exit immediately
- Accept small loss to avoid big loss
- **Flexibility > being right**

---

## Advanced Concepts

### 1. The Double Broken Wing

**Extreme asymmetry on both sides:**

**Structure:**

- Both put and call spreads have different widths
- Both "broken" but in opposite ways
- Creates compound asymmetry

**Example:**

- Sell $95/$85 put spread ($10 wide)
- Sell $105/$110 call spread ($5 wide)
- Collect $3.50 credit

**Characteristics:**

- Neither side symmetric
- Downside less risky (wide put spread)
- Upside more risky (tight call spread)
- **Bearish bias with both wings broken**

**When to use:**

- Very strong directional conviction
- Want maximum credit
- Accept concentrated risk on wrong side
- **Advanced traders only**

### 2. The Ratio Broken Wing

**Unequal number of contracts:**

**Structure:**

- Sell 2 contracts on tight spread
- Sell 1 contract on wide spread
- Collect substantially more credit
- **Undefined risk on tight side!**

**Example:**

- Sell 2 × $95 put for $4.00 total
- Buy 1 × $90 put for $1.50
- Sell 1 × $105 call for $1.50
- Buy 1 × $120 call for $0.25
- Net credit: $3.75

**The danger:**

- If stock below $90, losing on naked put
- Undefined risk creeping in
- Essentially hybrid of BWC and ratio spread

**When to use:**

- Very high conviction
- Very low IV (need extra credit)
- Experienced traders only
- **Dangerous - know what you're doing!**

### 3. Converting Losing ICs to Broken Wings

**The adjustment strategy:**

**Scenario:**

- Have symmetric IC
- One side threatened
- Convert to BWC by adjusting threatened side

**Example:**

- Symmetric IC on SPY
- Call side threatened (stock rallying)
- **Adjustment:**

  - Close tight call spread
  - Sell new call spread much wider
  - Now have broken wing (bullish)
  - Reduced upside risk, accept downside risk

**Pros:**

- Saves losing position
- Collects additional credit
- Reduces risk in direction of momentum

**Cons:**

- Now concentrated risk on other side
- Changing strategy mid-trade
- Thesis must support new asymmetry

### 4. Broken Wing Butterflies vs. Broken Wing Condors

**Understanding the difference:**

**Broken Wing Butterfly:**

- All options same expiration
- Three strikes (1-2-1 or 1-3-1 ratio)
- Concentrated profit zone
- More like pure directional bet

**Broken Wing Condor:**

- Four strikes (1-1-1-1 ratio)
- Wider profit zone
- More like income strategy with bias
- Better for moderate conviction

**When to choose each:**

- **High conviction, specific target:** BWB
- **Moderate conviction, range:** BWC

### 5. Time-Based Broken Wing Rolling

**The perpetual BWC strategy:**

**Concept:**

- Always have 2-3 BWCs at different expirations
- Roll each monthly
- Maintain continuous directional income

**Structure:**

- Month 1: Open 60-DTE bullish BWC
- Month 2: Open another 60-DTE (now have 2)
- Month 3: Close first at 30 DTE, open new 60-DTE
- **Rolling perpetual income stream**

**Benefits:**

- Continuous exposure
- Time diversification
- Systematic approach
- Compound small wins

**Example portfolio:**

- Position A: 60 DTE, just opened
- Position B: 45 DTE, 25% profit
- Position C: 30 DTE, 50% profit (closing)
- **Each month: close oldest, open newest**

### 6. Implied Volatility Skew Trading

**Using skew to optimize broken wings:**

**The pattern:**

- OTM puts have higher IV (put skew)
- OTM calls have lower IV
- This affects BWC construction

**Strategy for bullish BWC:**

- Sell puts (high IV, expensive)
- Buy cheaper puts (still high IV)
- Sell calls (lower IV, cheaper)
- Buy way OTM calls (very cheap)
- **Sell the expensive, buy the cheap**

**Example:**

- Stock at $100
- $95 put: IV = 35%
- $90 put: IV = 40%
- $105 call: IV = 28%
- $120 call: IV = 25%

**Optimal structure:**

- Sell $95 put (expensive due to high IV)
- Buy $90 put (protection)
- Sell $105 call (reasonable price)
- Buy $120 call (dirt cheap due to low IV)
- **Exploit the skew for better credit**

---

## Risk Management Rules

### 1. Position Sizing for Broken Wings

**More conservative than regular ICs due to asymmetric risk:**

$$
\text{Position Size} = \frac{\text{Risk Capital} \times 0.015}{\text{Max Risk (Tight Side)}}
$$

**Example:**

- $50,000 account
- Risk capital: $50,000 × 0.015 = $750 per trade
- Tight side max risk: $150 per BWC
- **Max position: 5 BWCs**

**Key differences from regular ICs:**

| Strategy | Risk per Trade | Logic |
|----------|---------------|-------|
| Regular IC | 2-5% | Symmetric risk |
| Broken Wing | 1.5-3% | Asymmetric risk, need buffer |

**Why more conservative?**
- Wide side has big max loss (unlikely but exists)
- Tight side has concentrated risk
- Correlation risk if multiple BWCs
- **Need cushion for tail events**

### 2. Diversification Rules

**Even more important for BWCs:**

**Directional diversification:**

- Max 60% in one direction (bullish or bearish)
- If running 5 BWCs, max 3 should be same bias
- Balance bullish and bearish positions

**Example portfolio:**

- 3 bullish BWCs (different sectors)
- 2 bearish BWCs (different sectors)
- Total: 5 positions
- **Directional balance with bias**

**Sector diversification:**

- Max 2 BWCs in same sector
- Avoid correlated moves
- Example: Don't have 5 tech BWCs

**Time diversification:**

- Stagger expirations
- Not all expiring same month
- Some 60 DTE, some 45 DTE, some 30 DTE
- **Smooth income stream**

### 3. The Two-Tier Stop Loss System

**Broken wings need special stops:**

### 4. Tier 1

**Trigger:**

- Stock within 3% of tight spread short strike
- Tight spread delta reaches 0.40
- Position down 30%

**Action:**

- Start monitoring daily (or intraday)
- Prepare to close
- Don't add to position
- Consider taking loss early

### 5. Tier 2

**Trigger:**

- Stock within 1% of tight spread short strike
- Tight spread delta reaches 0.60
- Position down 50%
- OR stock blasted through short strike

**Action:**

- **Close immediately, no questions**
- Don't try to adjust
- Don't hope for reversal
- Accept loss, move on

**Example - Bullish BWC:**

**Tier 1 triggers:**

- SPY at $450, tight spread sell $440 put
- SPY drops to $443 (3% away)
- **Action:** Close if losing >30%, or monitor closely

**Tier 2 triggers:**

- SPY drops to $441 (1% away)
- OR SPY gaps to $438 (through short strike)
- **Action:** Emergency exit immediately

### 6. Wide Side Monitoring

**Don't ignore the unlikely:**

**Set alerts:**

- Price alert at wide spread short strike
- Check position daily (both sides)
- Monitor news that could cause gap

**Black swan preparation:**

- Know max loss on wide side
- Have cash reserve to cover it
- Don't assume "it will never happen"
- **1 in 20 trades, wide side will activate**

### 7. The Conviction Check-In

**Weekly thesis review:**

**Every week, ask:**

1. Is my directional thesis still valid?
2. Has anything changed fundamentally?
3. Am I still comfortable with asymmetric risk?
4. Should I close early or adjust?

**If answer to #1 or #3 is NO:**

- Close position immediately
- Don't wait for technical stop
- Thesis break = exit trigger

**Example:**

- Bullish BWC on growth stocks
- Fed turns hawkish (thesis break!)
- Exit even if profitable
- **Preserve capital for better setup**

### 8. Portfolio Level Risk

**Aggregate exposure limits:**

**Total BWC exposure:**

- Max 30-40% of portfolio in all BWCs
- Max 20% in one direction
- Keep 60% cash for opportunities/adjustments

**Example $50,000 portfolio:**

- Max in all BWCs: $20,000
- Max in bullish BWCs: $10,000
- Max in bearish BWCs: $10,000
- Cash reserve: $30,000

**Correlation limit:**

- Calculate portfolio delta
- Max net delta: ±300 (like ±30 shares of SPY)
- If exceeded, close positions or hedge

**Example check:**

- 3 bullish BWCs: +20 delta each = +60
- 2 bearish BWCs: -15 delta each = -30
- Net portfolio delta: +30 (acceptable)

### 9. The Rebalancing Rule

**Quarterly portfolio check:**

**Every quarter:**

1. Review all BWC performance
2. Calculate win rate and EV
3. Adjust position sizing if needed
4. Rebalance directional bias

**If win rate <60% on BWCs:**

- Reduce position size
- Use more conservative strikes
- Or switch to symmetric ICs temporarily

**If win rate >80%:**

- Can increase position size slightly
- But don't get overconfident
- **Regression to mean is real**

---

## Real-World Examples

### 1. Example 1

**Setup (October 2024):**

- SPY at $560 (uptrend from $520)
- Healthy pullback to $555
- Support at $550 (50-day EMA)
- Resistance at $575
- IV Rank: 42% (moderate)
- Thesis: Consolidation or continued rally

**Technical analysis:**

- 200-day EMA: $540 (strong support)
- RSI: 58 (neutral, room to run)
- Volume: Declining on pullback (healthy)
- No major catalyst upcoming

**Trade: Bullish Broken Wing Condor**

**Structure:**

- **Tight put spread:**

  - Sell $545 put (22-delta) for $2.20
  - Buy $540 put (15-delta) for $1.00
  - Width: $5, Credit: $1.20
  
- **Wide call spread:**

  - Sell $580 call (18-delta) for $2.50
  - Buy $595 call (5-delta) for $0.50
  - Width: $15, Credit: $2.00

- **Total credit:** $3.20 = $320 per BWC
- **Max risk (put):** $5 - $3.20 = $1.80 = $180
- **Max risk (call):** $15 - $3.20 = $11.80 = $1,180
- **DTE:** 52 days
- **Break-evens:** $541.80 (put), $583.20 (call)

**Position sizing:**

- $50,000 account
- Risk per trade: 1.5% = $750
- Position: 4 BWCs
- Total credit: $1,280
- Total risk (tight): $720
- Total risk (wide): $4,720 (unlikely)

**Management plan:**

- Close at 50% profit ($160 per BWC)
- Stop loss if SPY < $547 (tight spread alert)
- Exit at 30 DTE regardless

**Trade progression:**

**Week 1-2:**

- SPY consolidates $555-$565
- Position: $2.50 value (22% profit)
- Action: Hold, thesis intact

**Week 3-4:**

- SPY rallies to $572
- Position: $1.80 value (44% profit)
- Action: Hold for 50%

**Week 5:**

- SPY at $575, consolidating
- Position: $1.55 value (52% profit)
- **Action: Close at 52% profit!**

**Final results:**

- Entry: $3.20 credit × 4 = $1,280
- Exit: $1.55 buy-back × 4 = $620
- **Net profit: $660**
- **ROI: 92% on tight-side risk**
- **Time: 32 days**
- **Annualized: ~1,050%**

**Lessons:**

- Bullish thesis validated
- Proper strike selection (20-delta range)
- Closed at 50%+ (discipline)
- Exited with plenty of DTE (22 left)
- **Directional edge + credit collection worked**

### 2. Example 2

**Setup (November 2024):**

- NVDA at $495 (parabolic rally from $420)
- RSI: 82 (extremely overbought)
- Broke through $480 resistance
- IV Rank: 55%
- **Mistake: Fighting the trend**

**Thesis (wrong):**

- "It's overbought, must pull back"
- "I'll sell calls above here"
- Technical divergence forming
- **Classic counter-trend mistake**

**Trade: Bearish Broken Wing Condor**

**Structure:**

- **Tight call spread:**

  - Sell $510 call (28-delta) for $8.00
  - Buy $520 call (18-delta) for $4.00
  - Credit: $4.00
  
- **Wide put spread:**

  - Sell $470 put (20-delta) for $5.50
  - Buy $450 put (8-delta) for $2.00
  - Credit: $3.50

- **Total credit:** $7.50 = $750 per BWC
- **Max risk (call):** $10 - $7.50 = $2.50 = $250
- **Max risk (put):** $20 - $7.50 = $12.50 = $1,250
- **DTE:** 45 days

**What went wrong:**

**Day 1-3:**

- NVDA continued rally to $515
- Tight call spread threatened
- Position: $9.00 (losing $1.50)
- **Should have exited here!**
- **Mistake: Held, thinking "it's overbought"**

**Day 4-7:**

- NVDA gaps to $530 on AI news
- Call spread blown through
- Position: $12.50 (max loss on calls)
- Wide put spread worthless (no help)

**Final results:**

- Entry: $7.50 credit
- Loss: $2.50 (call spread max loss)
- **Net: -$250 per BWC**
- If traded 3 BWCs: -$750 total

**Compounding mistake:**

- Held hoping for reversal
- Didn't follow stop loss
- Let winner become max loser
- Fought clear momentum

**Lessons learned:**

1. **Don't fight parabolic trends** (biggest mistake)
   - Overbought can stay overbought
   - Momentum is real
   - Wait for actual reversal, not just "looks toppy"

2. **Follow stop loss rules**
   - Should have exited when SPY hit $510 (short strike)
   - Tier 2 trigger: Close immediately
   - Instead held hoping for reversal

3. **Respect momentum over indicators**
   - RSI 82 doesn't mean immediate reversal
   - Price action > indicators
   - Trend is friend until broken

4. **Wide spread doesn't save you**
   - Put spread far away, useless
   - Asymmetric risk works against you when wrong
   - **Only works if directional thesis correct**

**What should have been done:**

- Wait for consolidation before entering
- Or use much higher strikes ($530/$545 calls)
- Or simply avoid - too much momentum
- **Better to miss trade than force bad one**

### 3. Example 3

**Setup (January 2025):**

- AAPL earnings released yesterday
- Stock at $195 (up from $185 on beat)
- Pre-earnings IV: 45%
- Post-earnings IV: 28% (crushed)
- IV Rank dropped: 60% → 35%
- Stock stabilizing in new range

**The opportunity:**

- Event risk gone
- IV still above average (28% vs. 20% normal)
- Direction clarified (bullish)
- New support at $190
- New resistance around $200

**Thesis:**

- Bullish on AAPL long-term
- Expect consolidation $190-$200
- IV will continue contracting
- **Perfect for bullish BWC**

**Trade: Bullish Broken Wing Condor**

**Structure:**

- **Tight put spread:**

  - Sell $190 put (20-delta) for $2.80
  - Buy $185 put (12-delta) for $1.20
  - Credit: $1.60
  
- **Wide call spread:**

  - Sell $205 call (16-delta) for $3.20
  - Buy $220 call (4-delta) for $0.60
  - Credit: $2.60

- **Total credit:** $4.20 = $420 per BWC
- **Max risk (put):** $5 - $4.20 = $0.80 = $80
- **Max risk (call):** $15 - $4.20 = $10.80 = $1,080
- **DTE:** 56 days
- **Prob. profit:** ~80%

**Why this works:**

**Triple benefit:**

1. **Theta decay** (time works for you)
2. **Vega contraction** (IV dropping helps)
3. **Directional edge** (post-earnings bullish)

**Position sizing:**

- 5 BWCs (conservative)
- Total credit: $2,100
- Total risk (tight): $400
- Comfortable position

**Trade progression:**

**Week 1:**

- AAPL consolidates $193-$197
- IV drops to 26%
- Position: $3.20 value (24% profit)
- Action: Hold

**Week 2:**

- AAPL drifts to $199
- IV drops to 24%
- Position: $2.40 value (43% profit)
- Action: Hold for 50%

**Week 3:**

- AAPL at $198, range-bound
- IV at 23%
- Position: $2.00 value (52% profit)
- **Action: Close at 52%!**

**Final results:**

- Entry: $4.20 × 5 = $2,100
- Exit: $2.00 × 5 = $1,000
- **Net profit: $1,100**
- **ROI: 275% on tight-side risk**
- **Time: 20 days**

**Key success factors:**

1. **Perfect timing:** Post-event entry
2. **IV edge:** Sold elevated IV, it contracted
3. **Directional edge:** Bullish thesis correct
4. **Discipline:** Closed at 50%+ profit
5. **Risk management:** Conservative sizing

**This is the IDEAL broken wing setup!**

### 4. Example 4

**Scenario: Running 6 BWCs Simultaneously**

**Portfolio:**

- $100,000 account
- 6 broken wing condors
- 3 bullish, 3 bearish
- Different sectors, different expirations

**Positions:**

**Bullish BWCs:**

1. **SPY** (45 DTE): $550/$545 puts, $580/$600 calls
   - Credit: $3.50, Risk: $150 (put), $1,650 (call)
   - Status: 25% profit
   
2. **AAPL** (52 DTE): $190/$185 puts, $210/$225 calls
   - Credit: $4.00, Risk: $100 (put), $1,100 (call)
   - Status: 15% profit
   
3. **DIS** (38 DTE): $95/$90 puts, $105/$120 calls
   - Credit: $2.80, Risk: $220 (put), $1,220 (call)
   - Status: 40% profit

**Bearish BWCs:**

4. **TSLA** (48 DTE): $240/$250 calls, $210/$190 puts
   - Credit: $3.20, Risk: $680 (call), $1,680 (put)
   - Status: 30% profit
   
5. **NVDA** (55 DTE): $510/$525 calls, $470/$445 puts
   - Credit: $6.00, Risk: $900 (call), $1,900 (put)
   - Status: 10% profit
   
6. **NFLX** (42 DTE): $420/$430 calls, $380/$360 puts
   - Credit: $4.50, Risk: $550 (call), $1,550 (put)
   - Status: -15% (loss)

**Portfolio Analysis:**

**Credits collected:** $24.00 total
**Tight-side risk:** $2,600 total
**Wide-side risk:** $9,100 total (unlikely)
**Current P/L:** +$4.80 (20% total profit)

**Management decisions:**

**Week 1 review:**

**DIS (40% profit):** 

- Close! Hit target early
- Take $1.12 profit
- Free up capital

**TSLA (30% profit):**

- Hold for 50%
- Still 48 DTE
- Plenty of time

**NFLX (-15% loss):**

- Stock moving toward tight call spread
- Thesis: Bearish on NFLX
- Action: Monitor closely, set stop at -30%

**Week 2 events:**

**NFLX update:**

- Stock rallied to $425 (tight spread threatened!)
- Loss now -25%
- **Decision: Close immediately**
- Accept -$1.13 loss
- Preserve capital

**SPY update:**

- Hit 50% profit
- Close, take $1.75 profit

**New position:**

- Open new bullish BWC on MSFT
- Different sector (software vs. index)
- Reset time decay

**Month-end results:**

**Closed positions:**

- DIS: +$1.12 (40% profit)
- SPY: +$1.75 (50% profit)
- NFLX: -$1.13 (25% loss)
- Net: +$1.74

**Open positions:**

- AAPL: 35% profit (holding)
- TSLA: 45% profit (close next week)
- NVDA: 20% profit (holding)
- MSFT: 5% profit (new)

**Overall:**

- Win rate: 67% (2 wins, 1 loss)
- Net profit: $1.74 on $24 collected = 7.25%
- Time: 1 month
- **Annualized: ~90%**

**Lessons from portfolio approach:**

1. **Diversification works**
   - Losses contained
   - Multiple positions smooth returns
   - Not correlated perfectly

2. **50% rule crucial**
   - Took profits early (DIS, SPY)
   - Reduced risk exposure
   - Freed capital for new trades

3. **Stop losses save capital**
   - NFLX stopped at -25%
   - Prevented max loss
   - Preserved capital for recovery

4. **Continuous rolling**
   - Always have 4-6 positions
   - Stagger expirations
   - Smooth income stream

5. **Mix directions**
   - 3 bullish, 3 bearish
   - Portfolio delta near neutral
   - Profit from both sides

---


---

## Worst Case Scenario

**What happens when skewed risk turns against you:**

### 1. The Nightmare Setup

**How it starts (The "High Probability" Trade):**

You enter a bullish broken wing condor on SPY:
- SPY at $450 (market consolidating)
- Thesis: "Market will stay range-bound, more likely up than down"
- **Structure:** Bullish BWC
  - **Put spread (WIDE):** Sell $440 put, buy $430 put (10-wide, risk side)
  - **Call spread (narrow):** Sell $455 call, buy $457 call (2-wide, safe side)
- **Net credit: $4.50** ($450 collected per contract)
- Max profit: $4.50 (if stays $440-$455)
- Max loss: $5.50 on put side ($10 width - $4.50 credit)
- **Win probability (calculated):** 75% (stock stays in tent)

You trade 20 contracts (aggressive but "high probability").

**But then reality strikes:**

**Day 1 - 9:30 AM (Banking Crisis News):**
- Major bank announces insolvency
- SPY gaps down: $450 → $435 (-3.3%)
- **Instantly through your wide put spread floor**
- VIX spikes: 15 → 38 (+153%)

**Your position immediately:**
- Beyond $430 (past wide wing): Max loss zone
- **Current loss:** Approaching -$5.50 per spread
- **20 contracts:** -$5.50 × 20 × 100 = **-$11,000 loss**
- Account: $50,000 → $39,000 (-22%)

**Your emotional response:** "It's high probability, this shouldn't happen!"

**The deterioration:**

**Day 1 - 2:00 PM (The Decision):**
- SPY bounces to $438 (slight recovery)
- Position: Still deep in loss zone (-$4,800)
- **Critical decision:** Exit now for -$4,800 OR hold hoping for bigger bounce?
- **You decide:** "I'll hold - probability says it should bounce more"

**Day 2-7 (The False Hope):**
- SPY bounces to $442 (above short put!)
- Your position improves: -$2,500
- **You think:** "See! I was right to hold!"
- **Mistake:** Should exit here, lock in reduced loss

**Week 2 (Second Leg Down):**
- More crisis news, contagion fears
- SPY → $428 (-4.9% total from entry)
- **Deep in max loss zone again**
- Loss: -$5,000 (approaching max loss)

**Week 3-4 (The Grind):**
- Market stays $425-$435 (below your range)
- Time decay doesn't help (beyond strikes)
- Theta: Minimal benefit when at max loss
- **You keep holding:** "Just needs to get back to $440"

**Expiration (Day 45):**
- SPY settles at $432
- All options settle at max loss
- **Final loss:** -$5.50 × 20 × 100 = **-$11,000** (22% of account)

**But the story doesn't end there...**

### 2. Maximum Loss Calculation

**Worst case mathematics:**

For broken wing condors, max loss occurs on the **wider wing side**:

$$
\text{Max Loss} = \text{Wider Wing Width} - \text{Total Credit}
$$

**Example (our trade):**
- Wider wing (put side): $440 - $430 = $10
- Total credit: $4.50
- **Max loss:** $10 - $4.50 = **$5.50 per spread**

**With 20 contracts:**
$$
\text{Total Max Loss} = \$5.50 \times 100 \times 20 = \$11,000
$$

**Impact on portfolio:**
- Started: $50,000
- After BWC disaster: $39,000 (-22%)
- **Recovery needed:** +28.2% just to break even

**The deceptive calculation:**
- "High probability" = 75% win rate
- **BUT:** 25% chance of -22% loss
- **Expected return:** 0.75 × $4,500 - 0.25 × $11,000 = $3,375 - $2,750 = **+$625** (positive, but risky)

**If you misjudged probability:**
- Real probability was 60% (not 75%)
- **Expected return:** 0.60 × $4,500 - 0.40 × $11,000 = $2,700 - $4,400 = **-$1,700** (negative!)

### 3. What Goes Wrong

The worst case for broken wing condors occurs when:

**1. Move to wide wing side (most common disaster):**
- **Your worst fear realized:** Stock breaks through wide wing
- **Probability miscalculation:** Market was 25% likely to crash, not 10%
- **Max loss hit:** Full wider wing width minus credit

**2. Violent whipsaw (brutal):**
- Day 1: Crash through put side (max loss)
- You hold, hoping for recovery
- Day 14: Rally through call side (max loss OTHER direction!)
- **Result:** Lose on BOTH sides of trade (sequential max losses)

**Example:**
- Week 1: SPY $450 → $428, loss -$5,500
- You hold
- Week 3: SPY rallies $428 → $458, new loss -$2,500 (call side now breached)
- **Total:** -$8,000 (lost on both sides separately)

**3. IV expansion amplifies loss:**
- Position is short vega (collected credit)
- Market crashes + VIX spikes to 40
- **Vega loss:** -$3,000 additional
- **Total:** -$11,000 (directional) - $3,000 (vega) = **-$14,000** (worse than theoretical max!)

**4. Pin risk at untested wing:**
- Stock pins at your narrow wing strike
- **Uncertain assignment** on Friday
- **Monday gap:** Against you
- **Extra loss:** $300-500 unexpected

**5. Rolling into deeper hole:**
- At -$5,500 loss
- Think: "I'll roll out 30 days, collect more credit"
- Roll for $2 credit
- **New position:** Still at risk, now 30 more days
- Market continues down
- **Final loss:** -$5,500 + (-$3,500 on rolled position) = **-$9,000** (rolling made it worse!)

### 4. The Cascade Effect

**Month 1: First "high probability" BWC**
- Bullish BWC on SPY: -$11,000 (22% of account)
- Account: $50,000 → $39,000
- **Emotional state:** Shock, disbelief

**Month 2: Revenge trading**
- "Can't be wrong twice, I'll recover with bigger position"
- Bearish BWC (flip direction): 30 contracts (1.5× bigger)
- Market rallies (wrong again)
- **Loss:** -$8,000 (30 contracts × $267 loss each, not full max)
- Account: $39,000 → $31,000 (-38% cumulative)
- **Emotional state:** Anger, desperation

**Month 3: Desperation sizing**
- "All-in recovery trade"
- 60 contracts (3× original)
- Wrong side again (or whipsaw)
- **Loss:** -$12,000
- Account: $31,000 → $19,000 (-62% cumulative)
- **Emotional state:** Capitulation

**Total damage:**
- Started: $50,000
- After 3 broken wings: $19,000
- **Need +163% to recover** (near impossible)
- **Psychological damage:** Fear of options, quit trading

### 5. Assignment and Pin Risk

**The Friday 4pm surprise:**

**Scenario: Expiration day, SPY at $440.08**
- Your short $440 put: $0.08 ITM (barely)
- Your long $430 put: OTM
- Your call spread: Far OTM (safe)

**What you think:** "Barely ITM, all will expire"

**What actually happens:**

**Friday after-hours:**
- SPY drops to $439.92 (8 cents below $440)
- You don't know this until Saturday

**Saturday (OCC settlement):**
- Some $440 put holders exercise early
- **Random assignment:** You might get assigned on 1 or more short puts

**Monday morning:**
- Check account: Surprise! You're **long 2,000 shares at $440** (20 contracts assigned)
- Position value: 2,000 × $440 = **$880,000** (massive position!)
- SPY opens Monday at $436 (gap down)
- **Immediate loss:** 2,000 × ($440 - $436) = **-$8,000**

**Plus liquidation:**
- Margin call forces sale at $436
- **Total loss:** -$8,000 (assignment) + original -$5,500 = **-$13,500** (worse than max loss!)

**The asymmetric assignment disaster:**
- 10 contracts assigned, 10 not (random)
- Long 1,000 shares at $440
- Still short 10 puts (not assigned)
- **Exposure:** Long shares + short puts = DOUBLE downside!
- Monday gap to $432: **-$16,000 loss** (shares + puts both losing)

### 6. Real Examples of Disasters

**Historical Example 1: COVID Crash (March 2020)**

**Setup:**
- Trader: Sold 50 bullish BWC on SPY
- SPY at $335 (Feb 20, 2020)
- Structure: $320/$310 put spread (wide), $345/$347 call spread (narrow)
- Credit: $4.50 per spread
- Max loss: $5.50 ($10 - $4.50)
- "High probability": Estimated 80% win rate

**Week 1 (Feb 24):**
- SPY drops $335 → $312 (-6.9%)
- **Through wide put floor**
- Position: Near max loss -$5.00

**Weeks 2-4:**
- Continued collapse: $312 → $290 → $260 → $240
- **Max loss locked in:** -$5.50 × 50 × 100 = **-$27,500**
- Account: $100k → $72.5k (-27.5%)

**Lesson:** "High probability" ≠ "impossible to lose". When 20% event happens, it's catastrophic.

**Historical Example 2: GME Short Squeeze (Jan 2021)**

**Setup:**
- GME at $40
- Sold bearish BWC (expecting sideways/down)
- Structure: $35/$33 put spread (narrow), $45/$55 call spread (WIDE, risk side)
- Credit: $3.00
- Max loss: $7.00 ($10 wide call - $3 credit)
- "Meme stocks don't sustain rallies"

**Week 1:**
- GME rockets: $40 → $65 (+62%!)
- **Beyond wide call wing**
- Position: Max loss -$7.00

**Week 2:**
- GME continues: $65 → $150 → $325
- **Max loss confirmed:** -$7 × 20 × 100 = **-$14,000**
- Expected profit was: $3 × 20 × 100 = $6,000
- **Swing:** $20,000 difference!

**Lesson:** Broken wing condors on "meme stocks" = playing with fire. Even wide wings insufficient for infinity squeezes.

### 7. Psychology of Losses

**Emotional stages (BWC specific):**

**1. Overconfidence: "High probability!"**
- 75% win rate feels safe
- **Miss:** 25% loss is LARGE (-22% of account)
- **Danger:** Oversize based on "probability"

**2. Denial: "It'll bounce back into range"**
- Stock $10 beyond wide wing
- "Just needs $5 bounce to reduce loss"
- **Reality:** Momentum continues, doesn't bounce

**3. Analysis paralysis: "Should I roll?"**
- Losing big, considering rolling
- Spend days analyzing
- **Meanwhile:** Stock moves further, loss grows

**4. Revenge trading: "I'll flip the direction"**
- Lost on bullish BWC (market dropped)
- Trade bearish BWC immediately (market rallies)
- **Result:** Lose on both directions

**5. Capitulation: "I'm done with options"**
- Multiple losses compound
- Quit trading entirely
- **Miss:** The learning opportunity

**Winning trader mindset:**
- **Accept:** 25% loss events WILL happen (4 out of every 16 trades)
- **Size accordingly:** Can survive 2-3 sequential losses
- **Exit fast:** At -50% max loss, don't wait for full damage
- **Learn:** What probability assessment was wrong?

### 8. Preventing Worst Case

**Risk management strategies:**

**1. Position sizing (CRITICAL):**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times 2\%}{\text{Max Loss Per Spread} \times 100}
$$

**Example:**
- Portfolio: $50,000
- Max loss per BWC: $5.50 ($550)
- **Max contracts:** $50,000 × 0.02 / $550 = **1.8 → 1-2 contracts MAX**

**Not 20, not 50 - just 1-2 contracts!**

This ensures even max loss = only -2% of account (survivable).

**2. Probability verification:**

**Before entry:**
- Market says: 75% win probability
- **You verify:** Historical data, volatility distribution
- **If your analysis:** Only 60% win probability → Don't trade OR price accordingly

**Probability check:**
- Use delta as rough probability (e.g., 25 delta = ~25% ITM probability)
- Sum deltas of all strikes to estimate total win probability
- **If < 65%:** Skip trade (not high enough edge)

**3. Stop losses (mandatory):**

**Exit triggers:**
- **-50% of max loss:** Exit immediately
  - Example: Max loss $5.50, exit at -$2.75
- **Stock breaks wide wing:** Exit same day
  - Don't wait for "bounce back"
- **25% of time passed, at -25% max loss:** Exit
  - Example: 40 DTE, at 10 DTE, if down -$1.38, exit

**4. Never hold through wide wing breach:**

**The rule:**
- Stock breaches wide wing = **EXIT IMMEDIATELY**
- Don't hope, don't wait, don't roll
- **Accept loss, move on**

**Why:**
- Theta no longer helps (beyond strikes)
- Gamma can hurt (whipsaw back)
- Max loss approaching, limited upside to holding

**5. Avoid high-risk scenarios:**

**Never trade BWC when:**
- **Binary events:** Earnings, FDA, elections (too unpredictable)
- **Low liquidity:** Can't exit at reasonable prices
- **After major move:** Already extended, risk of reversal
- **High IV (>70th percentile):** IV expansion risk
- **Low IV (<40th percentile):** No edge, narrow credit

### 9. The Ultimate Protection

$$
\text{Survivability} = \frac{\text{Capital Remaining}}{\text{Capital Initial}} > 0.90
$$

**The harsh reality:**
- BWCs are NOT "safe" because of "high probability"
- **High probability × small wins** can be outweighed by **low probability × large losses**
- **Kelly Criterion for BWCs:** Size even smaller than other strategies due to skewed payoffs

**Example expected value:**
- Win: 75% × $4.50 = +$3.38
- Loss: 25% × (-$5.50) = -$1.38
- **Net expected:** +$2.00 per spread (positive but not huge)

**If you oversize:**
- 20 contracts: Risk $11,000 for expected $4,000
- **One streak of 3 losses:** -$33,000 (wipes out account)

**Position sizing is EVERYTHING:**
- Size for 2% risk per trade
- Even 3 consecutive max losses = -6% (recoverable)
- **Survival > optimization**

**Remember:** Broken wing max loss WILL happen more often than you expect. Market's "high probability" estimate is often wrong. Your probability estimate is often also wrong. Size so you survive when BOTH probabilities are wrong simultaneously.



---

## Best Case Scenario

**When asymmetric risk pays off perfectly:**

### 1. The Perfect Setup

**Ideal entry conditions:**

Trading SPY in optimal conditions:
- **Market:** SPY at $450, consolidating after 5% rally
- **Volatility:** IV at 55th percentile (moderate, room to compress)
- **Directional bias:** Moderately bullish (Fed dovish, economy strong, no major risks)
- **Technical:** Support at $445, resistance at $460
- **Time horizon:** 45 DTE (sweet spot)
- **Catalyst:** Fed meeting in 2 weeks (expected dovish = bullish)

**The trade: Bullish broken wing condor**

**Structure:**
- **Put spread (WIDE, risk side):** Sell $440 put, buy $430 put (10-wide)
  - Premium: $2.50 collected
- **Call spread (NARROW, safe side):** Sell $455 call, buy $457 call (2-wide)
  - Premium: $2.00 collected  
- **Total credit: $4.50** ($450 per contract)
- **Position size:** 10 contracts (conservative: $5,500 max risk = 11% of $50k account)

**Max profit:** $4.50 (if stays $440-$455)  
**Max loss:** $5.50 on put side ($10 width - $4.50 credit)  
**Breakevens:** $435.50 (downside), $459.50 (upside)  
**Win probability (estimated):** 72%

**The optimal sequence:**

**Days 1-7 (The Confirmation):**
- SPY drifts up: $450 → $452 (+0.4%)
- Your position response:
  - **Theta decay:** +$12/day × 7 = +$84 (time working for you)
  - **Delta:** +$15 (small favorable move)
  - **Vega:** -$10 (IV slight uptick, minor hurt)
  - **Week 1 P&L:** +$89 on $4,500 credit = **+2% unrealized**

**Decision point:** Hold (only 7 days passed, 38 DTE remaining)

**Days 8-15 (The Catalyst):**
- Fed announces dovish stance
- Market rallies: $452 → $454 (+0.4% more)
- **IV compression:** 55th percentile → 42nd percentile
- Your position:
  - **Theta:** +$18/day × 7 = +$126
  - **Delta:** +$25 (continued favorable drift)
  - **Vega:** +$140 (IV crush helps short vega position!)
  - **Week 2 P&L:** +$291, **cumulative: +$380** (+8.4%)

**Days 16-30 (The Sweet Spot):**
- SPY consolidates: $454 → $451 (drifting back toward center!)
- **Perfect scenario:** Moving toward max profit zone ($445-$450)
- Your position:
  - **Theta accelerating:** +$25/day × 15 = +$375
  - **Delta neutral:** -$8 (small adverse move, minimal cost)
  - **Vega flat:** +$5 (IV stable now)
  - **Days 16-30 P&L:** +$372, **cumulative: +$752** (+16.7%)

**Decision point (30 DTE remaining):**
- Original target: +50% of max profit = +$2,250 ($225 per contract)
- Current profit: +$752 (17% of credit, 33% of time elapsed)
- Stock at $451 (optimal zone)
- **Professional decision:** Getting close to target, monitor closely

**Days 31-38 (Acceleration):**
- SPY stays $450-$452 (perfect range)
- Theta now +$35/day
- **Week 5 P&L:** +$245 more
- **Cumulative: +$997** (22% on credit, **target exceeded!**)

**Exit (Day 38, 7 DTE remaining):**
- Close entire position for $997 profit
- **Avoided:** Final week gamma risk
- **Realized:** 22% return in 38 days
- **Annualized:** (1.22)^(365/38) - 1 = **256% annualized** (obviously not sustainable, but shows power)

**Actual math:**
- Entry credit: $4,500 (10 contracts)
- Exit profit: $997
- **Net cash:** Kept $4,500 credit, closed for additional $997 = Actually this doesn't make sense...

Let me recalculate. When you close a credit position:
- You collected $4.50 credit initially
- To close, you need to "buy back" the spreads
- If position value dropped from $4.50 to $3.50, you buy back for $3.50
- **Net profit:** $4.50 (collected) - $3.50 (paid to close) = $1.00 profit

So if you made $997 profit on 10 contracts:
- Per contract profit: $997 / (10 × 100) = $0.997 ≈ $1.00
- Original credit: $4.50
- **You closed by paying back:** $4.50 - $1.00 = $3.50

**ROI:** $1.00 / $5.50 (max risk) × 100% = **18.2% in 38 days**

### 2. Maximum Profit Achievement

**Best case mathematics:**

For broken wing condors, max profit equals total credit:

$$
\text{Max Profit} = \text{Total Credit Collected}
$$

**If all options expire worthless:**
- Credit: $4.50 per spread
- 10 contracts: $4.50 × 10 × 100 = **$4,500 max profit**
- Max risk: $5.50 × 10 × 100 = $5,500
- **ROI at max:** $4,500 / $5,500 = **82%**

**Our actual trade (early exit):**
- Profit: $1.00 × 10 × 100 = $1,000
- On max risk: $5,500
- **Realized ROI:** $1,000 / $5,500 = **18.2%** in 38 days

**Annualized (not realistic to repeat):**
$$
\text{Annualized} = \left(1 + 0.182\right)^{365/38} - 1 = 256\%
$$

**More realistic annual projection:**
- ~9 trades per year (45 DTE each, exit at 38 days)
- Win rate: 70% (exit at +50% target)
- Average win: +$1,000
- Average loss: -$1,500 (exit at -50% max loss)
- **Expected annual:** 0.70 × 9 × $1,000 - 0.30 × 9 × $1,500 = $6,300 - $4,050 = **+$2,250** (45% return on $5k deployed)

### 3. What Makes It Perfect

Best case for BWCs requires ALL of these:

**1. Right directional bias (Essential):**
- Bullish BWC + bullish market ✓
- Stock stayed above wide put wing
- **Our trade:** Never threatened put side

**2. Right magnitude (Critical):**
- Move stayed within tent: $440-$455 range
- **Our trade:** SPY $450 → $454 → $451 ✓
- Perfect: Small favorable drift, then consolidation

**3. Right timing (Crucial):**
- Profits captured in first 80% of duration
- **Our trade:** Exited day 38 of 45 (84%) ✓
- Avoided final week gamma risk

**4. Right volatility (Bonus):**
- IV compression multiplied profits
- **Our trade:** 55th → 42nd percentile ✓
- **Vega gain:** +$140 extra profit

**The perfect combination:**
- Theta decay: +$710 (biggest contributor, 71%)
- Vega crush: +$145 (nice bonus, 15%)
- Delta gain: +$145 (favorable drift, 14%)
- **Total: $1,000** ✓

### 4. Comparison to Alternatives

**BWC vs. Standard Iron Condor:**

**Same scenario (SPY $450 → $454 → $451):**

**Standard IC (symmetric):**
- Structure: $435/$440 put spread + $455/$460 call spread
- Credit: $3.50 (both sides equal width)
- Max risk: $1.50 per side
- **At $451:** Slight loss on call side (above $450 center)
- **P&L:** ~+$0.50 (worse than BWC)

**Our BWC (asymmetric):**
- Wide puts ($10), narrow calls ($2)
- Credit: $4.50 (29% more!)
- Matched bullish bias
- **At $451:** Still in sweet spot
- **P&L:** +$1.00 (2× better!)

**BWC wins when:**
- **Directional bias correct:** Bullish structure matched bullish market
- **Credit enhancement:** Extra premium from wider wing
- **Probability optimization:** More room on risk side we're comfortable with

**BWC vs. Bull Put Spread:**

**Alternative: Bull put spread only**
- Sell $445 put, buy $440 put
- Credit: $2.50
- Max risk: $2.50
- **P&L at $451:** Keep full $2.50

**Our BWC:**
- Includes call spread (protection)
- Credit: $4.50 (80% more)
- **P&L at $451:** $1.00 realized (40% of credit)

**Bull put spread wins on:** Simplicity, higher realized percentage  
**BWC wins on:** Absolute profit, upside protection, more credit

**When to use BWC:**
- Want upside protection (not naked put side)
- Larger capital, want more credit
- **When directional + range-bound view**

### 5. Professional Profit-Taking

**When to take profits:**

Professionals don't wait for max profit - systematic exits:

**Exit trigger system:**

**1. Profit target (primary):**
- Exit at **40-50% of max profit**
- Our trade: Max $4,500, target $1,800-$2,250
- **Achieved:** $1,000 (22% of max, acceptable)

**2. Time-based:**
- Exit at **75-80% of time elapsed**
- Our trade: 45 DTE, exit at ~35 DTE
- **We exited:** 38 days = 84% ✓

**3. Greek-based:**
- Exit if **theta < $10/day** (decay slowing)
- Our trade: Theta was $35/day (strong)
- Could have held longer

**4. Technical:**
- Exit if stock approaches breakeven
- Our trade: $451 (center), no threat
- Safe to hold

**The compounding advantage:**

Early exits enable capital recycling:

**Strategy A: Hold for max profit (retail)**
- Trade 1: 45 days, +$4.50 (if perfect landing)
- Probability of perfect: 15%
- **Expected:** 0.15 × $4.50 = $0.68 per trade

**Strategy B: Exit at 50%, redeploy (professional)**
- Trade 1: 30 days (faster), +$2.00 (50% of max, 60% probability)
- Trade 2: Another 30 days, +$2.00
- **In 60 days:** 0.60 × $2.00 × 2 = $2.40 expected
- **vs. Strategy A in 60 days:** 60/45 × $0.68 = $0.91

**Professional approach wins:** 2.6× more profit through faster recycling + higher win rate

### 6. The Dream Scenario

**Extreme best case (rare):**

**Flash crash recovery trade:**
- VIX spikes to 35 (panic)
- SPY drops $450 → $435
- **You enter BWC during panic:**
  - Wide puts: $420/$410 (10-wide, far below market)
  - Narrow calls: $445/$447 (2-wide, near ATM)
  - **Credit: $6.00** (fear premium inflated!)

**Next week:**
- Market recovers: $435 → $445
- VIX collapses: 35 → 18
- **Your position:**
  - Theta: +$350
  - Vega: +$800 (IV crush massive)
  - Delta: +$300
  - **Total: +$1,450 in 7 days!**

**If closed:**
- $1,450 profit on $6,000 credit = **24% in one week**
- **Annualized:** 12,480% (obviously unsustainable)

**Why rare:**
- Panic recoveries: Few times per decade
- Timing entry perfectly: Very hard
- Having capital ready: Requires discipline
- **Probability:** <1% of opportunities

### 7. The Reality Check

**Typical BWC outcomes (100 trades, professional execution):**

- **65 winners** (exit +40-50%): +$2.00 avg = +$130
- **25 small losers** (exit -30%): -$1.50 avg = -$37.50
- **10 max losers** (hit stop -50%): -$2.75 avg = -$27.50
- **Net:** +$65 per opportunity
- **On $5,500 risk:** +$65 / $5,500 = **1.18% per trade**
- **Annual:** ~12 trades/year = **14% annual return**

**Key insights:**
- **Not get-rich-quick:** Steady, consistent returns
- **Win rate matters:** 65% winners = sustainable
- **Early exits crucial:** Don't wait for max profit
- **Position sizing:** Small enough to survive 3-5 sequential losses

**Most important:** Best case = hitting +40-50% targets consistently (65% of time), not hitting max profit occasionally (15% of time). Success comes from discipline and consistency, not home runs! 🎯


## What to Remember

### 1. Core Concept

**Broken wing condors are directional income strategies with asymmetric risk:**

$$
\text{Broken Wing Condor} = \text{Tight Spread} + \text{Wide Spread} + \text{Directional Conviction}
$$

- Collect credit upfront (income strategy)
- Max profit = credit (limited)
- Max loss asymmetric (concentrated on one side)
- Express moderate directional conviction
- Need high win rate on tight spread side

### 2. The Setup

**Bullish Broken Wing:**

- Tight put spread (5-wide)
- Wide call spread (10-15 wide)
- Bullish bias (want stock flat or up)
- Risk concentrated on downside

**Bearish Broken Wing:**

- Tight call spread (5-wide)
- Wide put spread (10-15 wide)
- Bearish bias (want stock flat or down)
- Risk concentrated on upside

### 3. The Greeks

**Critical to understand:**

- **Delta:** ±0.10 to ±0.25 (directional bias)
- **Theta:** Positive, but concentrated on tight spread
- **Gamma:** Very asymmetric (tight spread high risk)
- **Vega:** Negative (IV increase hurts)

### 4. Strike Selection

**The asymmetric spacing:**

- Tight spread: 5-delta width, 20-30 delta short strike
- Wide spread: 10-20 delta width, 15-20 delta short strike
- Ratio: 1:2 to 1:4 (tight:wide)
- Collect 40-60% of tight spread width

### 5. Time Selection

**The 45-60 DTE standard:**

- Enter 45-60 days (longer than regular IC)
- Exit at 50% profit OR 30 DTE
- Earlier exit than regular IC (gamma risk)
- Need time for directional thesis

### 6. Maximum Profit/Loss

**Bullish BWC:**

- Max profit: Total credit
- Max loss (tight/put): Put width - credit
- Max loss (wide/call): Call width - credit
- Break-even: Short strikes ± credit

**Asymmetric risk profile:**

- Tight side: Small loss likely
- Wide side: Large loss unlikely
- **Probability-weighted risk acceptable**

### 7. When to Use

**Use broken wings when:**

- Have moderate directional conviction
- Want credit collection + directional edge
- Market trending but consolidating
- Post-event stabilization
- IV Rank 40-60% (moderate)

**Don't use when:**

- No directional conviction (use symmetric IC)
- Very high IV (>70%)
- Parabolic moves happening
- Binary events approaching
- You can't handle asymmetric risk

### 8. Common Mistakes to Avoid

1. Don't use BWC just for extra credit (need conviction)
2. Don't make tight spread too tight (chasing premium)
3. Don't ignore wide spread risk (low probability ≠ zero)
4. Don't hold through earnings/events
5. Don't skip 50% profit rule
6. Don't over-concentrate in one direction
7. Don't fight the thesis when it breaks

### 9. Risk Management

**Essential rules:**

- Position size: Max 1.5-3% per trade (conservative)
- Two-tier stops: Tier 1 at 30%, Tier 2 at 50%
- Close at 50% profit (optimal)
- Exit at 30 DTE (gamma protection)
- Diversify: both directions, sectors, times
- Monitor tight spread daily
- Have conviction review weekly

### 10. Comparison to Regular Iron Condors

**Advantages over symmetric IC:**

- Directional edge (conviction pays off)
- Better credit collection (typically)
- Express market view with income
- Flexible risk allocation

**Disadvantages vs. symmetric IC:**

- Higher capital requirement (wide spread)
- More management needed (tight spread)
- Concentrated risk on one side
- Only works if directional thesis correct

### 11. Your Learning Path

**Progression:**

1. Master basic credit spreads first
2. Then learn regular iron condors
3. Understand probability and risk
4. Add broken wings when you have conviction
5. Eventually: Multiple BWCs in portfolio

**Broken wings are for INTERMEDIATE to ADVANCED traders!**

### 12. Final Wisdom

> "Broken wing condors are the bridge between neutral income strategies and directional trades. They let you express moderate conviction while still collecting premium - but this flexibility comes with asymmetric risk. The key is matching your conviction to your asymmetry: strong conviction = tighter tight spread, moderate conviction = wider tight spread. Never use a broken wing just because it collects more credit - that extra credit must be justified by a genuine directional edge. Master the 50% profit rule, the tight spread monitoring, and the conviction check-in. Remember: broken wings profit when you're right about direction OR when the stock stays in range - but they hurt badly when you're wrong about direction AND the stock moves against you."

**Key to success:**

- Only use when you have directional conviction
- Tight spread = 20-30 delta (not greedy)
- Wide spread = 1:2 to 1:3 ratio
- Enter 45-60 DTE (longer than ICs)
- Exit at 50% profit or 30 DTE
- Monitor tight spread obsessively
- Diversify across directions
- Check thesis weekly

**Most important:** Broken wings are conviction trades dressed as income strategies - if your conviction is wrong, the income won't save you! 🎯⚖️
