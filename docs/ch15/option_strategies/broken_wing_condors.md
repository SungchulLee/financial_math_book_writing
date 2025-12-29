# Broken Wing Condors

**Broken wing condors** are asymmetric, defined-risk option strategies where one side of an iron condor has unequal strike spacing, creating a directional bias while maintaining credit collection. They offer the income generation of condors with reduced capital requirements and strategic flexibility for traders with moderate directional conviction.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_bearish_broken_wing.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_broken_wing_greeks.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_brokenness_levels.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_bullish_broken_wing.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_capital_efficiency.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_risk_heatmap.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condors_symmetric_vs_broken_wing.png?raw=true" alt="long_call_vs_put" width="700">
</p>

---

## The Core Insight

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

**Before trading broken wings, understand the variations:**

### Broken Wing Iron Condor (Call Side Broken)

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

### Broken Wing Iron Condor (Put Side Broken)

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

### Skip Strike Broken Wing Condor

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

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_condor.png?raw=true" alt="broken_wing_condor" width="700">
</p>
**Figure 1:** Profit/loss diagram comparing symmetric iron condor (left) to broken wing condor (right). Note the asymmetric risk profile with concentrated risk on one side and distant max loss on the other, creating directional bias while maintaining credit collection.

---

## Economic Interpretation: Asymmetric Insurance with Directional Conviction

**Beyond the basic definition, understanding what broken wing condors REALLY are economically:**

### Broken Wing Condors as Directional Insurance Underwriting

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

### Example: Breaking Down the SPY Broken Wing Condor

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

### The Conviction-Based Capital Allocation

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

### Why This Perspective Matters

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

### The Strategic Advantage of Asymmetric Risk

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

### Bullish Broken Wing (Wide Call Side)

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

### Bearish Broken Wing (Wide Put Side)

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

## The Greeks: Understanding Broken Wing Dynamics

**How Greeks differ from regular iron condors:**

### Delta (Directional Risk)

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

### Theta (Time Decay) - Still Your Friend, But Asymmetric

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

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_theta.png?raw=true" alt="theta_asymmetry" width="600">
</p>

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

### Gamma (Delta Risk) - Asymmetric Acceleration

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

### Vega (Volatility Risk) - Similar to Regular IC

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

### Rho (Interest Rate Risk) - Still Negligible

**Impact:** ~$0.01-0.02 per 1% rate change

**Can ignore for most trading**

---

## Strike Selection Strategy

**Where you place strikes determines everything in broken wings:**

### The Asymmetric Strike Spacing Framework

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

### The Delta-Based Selection (Recommended)

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

### The Probability-Weighted Approach

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

### Credit Collection Targets

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

### The "Golden Zone" Setup

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

## Time Selection: When to Enter and Exit

### Entry Timing: The 45-60 DTE Rule for Broken Wings

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

### Exit Timing: The 50% + Danger Zone Rules

**Broken wings need more nuanced exits than regular ICs:**

#### Rule 1: Close at 50% Profit (Standard)

**Same as regular credit spreads:**

- Close when you've captured 50% of max credit
- Optimal risk/reward balance
- Frees capital for new opportunities

**Example:**

- Collected $3.00 credit
- Close when spread worth $1.50
- Take $1.50 profit, move on

#### Rule 2: The Tight Spread Alert (BWC-Specific)

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

#### Rule 3: The 30-DTE Exit

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

### Rolling Positions - When and How

**Broken wings require different rolling strategies:**

#### When Stock Threatens Tight Spread

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

#### When to NOT Roll

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

### The Multi-Month Strategy

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

### Mathematical Formulas

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

### Risk/Reward Asymmetry Analysis

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

### Return on Capital Analysis

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

### Market Conditions

**Best environments:**

#### 1. Trending Markets with Pullbacks

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

#### 2. Post-Event Stabilization

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

#### 3. Range Extension Setups

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

### Technical Setups

**Combining broken wings with technicals:**

#### Bullish BWC - Technical Signals

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

#### Bearish BWC - Technical Signals

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

### Volatility-Based Entry

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

### Position Sizing for Broken Wings

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

### Diversification Rules

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

### The Two-Tier Stop Loss System

**Broken wings need special stops:**

#### Tier 1: Tight Spread Alert (Early Warning)

**Trigger:**

- Stock within 3% of tight spread short strike
- Tight spread delta reaches 0.40
- Position down 30%

**Action:**

- Start monitoring daily (or intraday)
- Prepare to close
- Don't add to position
- Consider taking loss early

#### Tier 2: Tight Spread Emergency (Hard Stop)

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

### Wide Side Monitoring

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

### The Conviction Check-In

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

### Portfolio Level Risk

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

### The Rebalancing Rule

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

### Example 1: SPY Bullish BWC (Successful Trade)

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

### Example 2: NVDA Bearish BWC (Loss Example)

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

### Example 3: AAPL Post-Earnings BWC (Optimal Setup)

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

### Example 4: Multi-Position Portfolio Management

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

## What to Remember

### Core Concept

**Broken wing condors are directional income strategies with asymmetric risk:**

$$
\text{Broken Wing Condor} = \text{Tight Spread} + \text{Wide Spread} + \text{Directional Conviction}
$$

- Collect credit upfront (income strategy)
- Max profit = credit (limited)
- Max loss asymmetric (concentrated on one side)
- Express moderate directional conviction
- Need high win rate on tight spread side

### The Setup

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

### The Greeks

**Critical to understand:**

- **Delta:** ±0.10 to ±0.25 (directional bias)
- **Theta:** Positive, but concentrated on tight spread
- **Gamma:** Very asymmetric (tight spread high risk)
- **Vega:** Negative (IV increase hurts)

### Strike Selection

**The asymmetric spacing:**

- Tight spread: 5-delta width, 20-30 delta short strike
- Wide spread: 10-20 delta width, 15-20 delta short strike
- Ratio: 1:2 to 1:4 (tight:wide)
- Collect 40-60% of tight spread width

### Time Selection

**The 45-60 DTE standard:**

- Enter 45-60 days (longer than regular IC)
- Exit at 50% profit OR 30 DTE
- Earlier exit than regular IC (gamma risk)
- Need time for directional thesis

### Maximum Profit/Loss

**Bullish BWC:**

- Max profit: Total credit
- Max loss (tight/put): Put width - credit
- Max loss (wide/call): Call width - credit
- Break-even: Short strikes ± credit

**Asymmetric risk profile:**

- Tight side: Small loss likely
- Wide side: Large loss unlikely
- **Probability-weighted risk acceptable**

### When to Use

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

### Common Mistakes to Avoid

1. Don't use BWC just for extra credit (need conviction)
2. Don't make tight spread too tight (chasing premium)
3. Don't ignore wide spread risk (low probability ≠ zero)
4. Don't hold through earnings/events
5. Don't skip 50% profit rule
6. Don't over-concentrate in one direction
7. Don't fight the thesis when it breaks

### Risk Management

**Essential rules:**

- Position size: Max 1.5-3% per trade (conservative)
- Two-tier stops: Tier 1 at 30%, Tier 2 at 50%
- Close at 50% profit (optimal)
- Exit at 30 DTE (gamma protection)
- Diversify: both directions, sectors, times
- Monitor tight spread daily
- Have conviction review weekly

### Comparison to Regular Iron Condors

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

### Your Learning Path

**Progression:**

1. Master basic credit spreads first
2. Then learn regular iron condors
3. Understand probability and risk
4. Add broken wings when you have conviction
5. Eventually: Multiple BWCs in portfolio

**Broken wings are for INTERMEDIATE to ADVANCED traders!**

### Final Wisdom

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
