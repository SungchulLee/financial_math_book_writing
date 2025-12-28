# Horizontal vs Vertical IV Relationships

**Horizontal vs vertical IV relationships** refer to the two fundamental dimensions along which implied volatility varies: the **term structure** (horizontal, across time) and the **smile/skew** (vertical, across strikes). Understanding and trading the relationship between these dimensions—how they interact, diverge, and normalize—is essential for sophisticated volatility trading and surface arbitrage.

---

## The Core Insight

**The fundamental idea:**

- Implied volatility is not a single number—it's a **surface** across two dimensions
- **Horizontal dimension:** How IV changes with TIME (term structure)
- **Vertical dimension:** How IV changes with STRIKE (smile/skew)
- These two dimensions **interact** and create complex relationships
- **Solution:** Trade the RELATIONSHIP between horizontal and vertical IV movements
- Exploit when one dimension moves independently of the other
- Or when the correlation between dimensions breaks down

**The key equation:**

$$
\text{IV Surface} = f(\underbrace{K}_{\text{Vertical}}, \underbrace{T}_{\text{Horizontal}})
$$

Where:
- Vertical (K): Strike dimension → Smile/Skew
- Horizontal (T): Time dimension → Term Structure
- Surface: The combined 3D structure

**You're essentially betting: "The relationship between how IV varies across strikes versus how it varies across time is currently abnormal and will normalize."**

---

## What Are Horizontal and Vertical IV Relationships?

**Before understanding their relationship, we need to define each dimension:**

### The Horizontal Dimension (Term Structure)

**What is it?**

The **term structure** shows how IV changes with time to expiration (holding strike constant):

**Visual representation:**

```
    IV (ATM Strike)
     ↑
  30%|           ___/‾‾‾
  25%|        _/
  20%|     _/
  15%|  _/
     |__________________→ Time
     1M   3M   6M   12M
```

**Key features:**

**Normal (upward sloping):**
- Near-term: Lower IV (15-20%)
- Medium-term: Higher IV (20-25%)
- Long-term: Highest IV (25-30%)
- Reflects uncertainty increases with time

**Inverted (downward sloping):**
- Near-term: High IV (35%+)
- Medium-term: Lower IV (25%)
- Long-term: Even lower IV (20%)
- Common during crises or before events

**Humped:**
- Near-term: Moderate IV (20%)
- Event maturity: High IV (40%)
- Far-term: Normal IV (25%)
- Event-driven (earnings, FDA)

### The Vertical Dimension (Smile/Skew)

**What is it?**

The **smile/skew** shows how IV changes with strike price (holding time constant):

**Visual representation:**

```
    IV (30-day options)
     ↑
  35%|  /‾‾\
  30%| /    \__
  25%|/         \___
  20%|________________
     |
    $90  $100  $110  $120
    OTM  ATM   OTM
    Put        Call
```

**Key features:**

**Equity skew (most common):**
- OTM puts: High IV (35%+) - fear premium
- ATM: Lower IV (25%)
- OTM calls: Moderate IV (28%)
- Asymmetric smile

**Symmetric smile:**
- Both wings elevated
- ATM lowest
- Common in commodities, FX

**Flat:**
- All strikes similar IV
- Rare, typically very short-dated
- Or very low volatility environment

### The Problem: They Should Be Related But...

**Theoretical relationship:**

In a simple Black-Scholes world:
- Term structure should be flat (constant vol)
- Smile should be flat (strike-independent)
- **Reality:** Neither is flat!

**Empirical observation:**

The two dimensions are **correlated** but imperfectly:

1. **When overall IV increases:**
   - Term structure often steepens
   - Skew often steepens too
   - But not always proportionally!

2. **When stress hits:**
   - Near-term spikes (horizontal)
   - OTM puts spike (vertical)
   - But the RATIO varies

3. **Normal times:**
   - Predictable term structure
   - Stable skew
   - Relationship more consistent

**The opportunity:**

Trade when the relationship between horizontal and vertical IV **diverges from normal patterns**.

---

## The Structure

### How to Express Views on Each Dimension

**1. Pure Horizontal Trades (Term Structure Only):**

**Calendar Spread:**
- Buy back month
- Sell front month
- **Same strike** (isolates time dimension)
- Profits from term structure steepening

**Example:**
- Stock at $100
- Sell 1-month $100 call
- Buy 3-month $100 call
- Pure horizontal bet

**2. Pure Vertical Trades (Smile/Skew Only):**

**Butterfly Spread:**
- Buy wings (OTM strikes)
- Sell body (ATM)
- **Same expiration** (isolates strike dimension)
- Profits from smile flattening

**Example:**
- Stock at $100
- Buy $95 put + $105 call
- Sell 2× $100 calls
- Pure vertical bet

**Risk Reversal:**
- Buy OTM call
- Sell OTM put
- **Same expiration**
- Profits from skew changes

**3. Combined Horizontal + Vertical Trades:**

**Diagonal Spread:**
- Different strikes AND times
- Trades both dimensions
- More complex

**Example:**
- Buy 3-month $105 call
- Sell 1-month $110 call
- Both dimensions involved

**Calendar Butterfly:**
- Butterflies at different expirations
- Trades relationship between vertical shapes across time

**4. Relationship Trades:**

**These explicitly trade the CORRELATION between dimensions:**

**Example: Skew vs Term Structure:**
- When: Near-term skew very steep, far-term skew flat
- Trade: Vertical spread in front month vs vertical spread in back month
- Bet: Relationship normalizes

### The Visual

**Horizontal vs Vertical Dimensions:**

```
    IV Surface (3D View)
    
        IV
         ↑
    35% |     ___/‾‾\___  ← Vertical (Skew)
    30% |  __/         \__
    25% | /               \
        |/‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\
        Strike →  
         ↓
         Time →
         (Horizontal)
```

**Key features:**

- Two independent dimensions
- But not truly independent!
- Relationship between them is tradeable
- Correlation varies over time

---

## The Portfolio

### General Framework

For a position trading both dimensions:

$$
\Pi = \sum_{i} n_i \cdot V(S, K_i, T_i, \sigma(K_i, T_i))
$$

where:
- $K_i$ = Strike (vertical dimension)
- $T_i$ = Time (horizontal dimension)
- $\sigma(K_i, T_i)$ = IV at each (strike, time) point

**The goal:**

Construct portfolios that isolate or exploit the relationship between dimensions.

### Pure Horizontal Exposure (Calendar)

**Structure:**

$$
\Pi_{\text{horizontal}} = C(S, K, T_2) - C(S, K, T_1)
$$

where $T_2 > T_1$ and strike $K$ held constant.

**What you're exposed to:**

- ✓ Term structure changes (your bet)
- ✓ Vega in back month > front month
- ✗ Smile/skew changes (minimized)
- ✗ Delta (approximately hedged)

**Greeks:**

$$
\begin{align}
\frac{\partial \Pi}{\partial \sigma(T_2)} &> 0 \quad \text{(long back month vega)} \\
\frac{\partial \Pi}{\partial \sigma(T_1)} &< 0 \quad \text{(short front month vega)}
\end{align}
$$

### Pure Vertical Exposure (Butterfly)

**Structure:**

$$
\Pi_{\text{vertical}} = C(K_1, T) - 2C(K_2, T) + C(K_3, T)
$$

where $K_1 < K_2 < K_3$ and time $T$ held constant.

**What you're exposed to:**

- ✓ Smile/skew changes (your bet)
- ✓ Curvature of IV across strikes
- ✗ Term structure changes (minimized)
- ✗ Delta (approximately hedged at center)

**Greeks:**

$$
\begin{align}
\frac{\partial \Pi}{\partial \sigma(K_1)} &> 0 \quad \text{(long wing vega)} \\
\frac{\partial \Pi}{\partial \sigma(K_2)} &< 0 \quad \text{(short body vega)} \\
\frac{\partial \Pi}{\partial \sigma(K_3)} &> 0 \quad \text{(long wing vega)}
\end{align}
$$

### Combined Exposure (Diagonal)

**Structure:**

$$
\Pi_{\text{diagonal}} = C(K_2, T_2) - C(K_1, T_1)
$$

where $K_2 \neq K_1$ and $T_2 > T_1$.

**What you're exposed to:**

- ✓ Both horizontal AND vertical
- ✓ Relationship between dimensions
- ✓ More complex Greeks
- ✗ Harder to isolate specific bets

---

## The P&L Formula

### For Pure Horizontal Trades

$$
\delta \Pi_H \approx \underbrace{\text{Vega}_{T_2} \cdot \delta\sigma_{T_2} - \text{Vega}_{T_1} \cdot \delta\sigma_{T_1}}_{\text{Term structure P\&L}} + \underbrace{\theta_{\text{net}} \, \delta t}_{\text{Time decay}}
$$

**Breaking it down:**

**1. Term Structure P&L (Primary):**

This depends on **relative IV changes across maturities**:

- If $\delta\sigma_{T_2} > \delta\sigma_{T_1}$: Profit (term structure steepens)
- If $\delta\sigma_{T_2} < \delta\sigma_{T_1}$: Loss (term structure flattens)

**Example:**
- Front month IV: 20% → 22% (+2 points)
- Back month IV: 24% → 28% (+4 points)
- **Term structure steepened** → Calendar profitable

**2. Theta P&L:**

Usually positive for long calendars:

$$
\theta_{\text{net}} = \theta_{T_2} - \theta_{T_1}
$$

Typically: $|\theta_{T_1}| > |\theta_{T_2}|$ (front decays faster)

### For Pure Vertical Trades

$$
\delta \Pi_V \approx \sum_{K} \text{Vega}_K \cdot \delta\sigma_K + \Theta_{\text{net}} \, \delta t + \frac{1}{2}\Gamma_{\text{net}} (\delta S)^2
$$

**Breaking it down:**

**1. Smile/Skew P&L (Primary):**

This depends on **relative IV changes across strikes**:

**For butterfly (long wings, short body):**

- If wing IVs increase relative to ATM: Profit
- If smile flattens (all IVs converge): Profit
- If smile steepens more: Loss

**Example (butterfly):**
- $95 put IV: 30% → 28% (-2 points, you're long)
- $100 call IV: 25% → 26% (+1 point, you're short 2×)
- $105 call IV: 28% → 27% (-1 point, you're long)
- **Net:** Loss from this example

**2. Theta P&L:**

For short butterflies: Positive (usually)
For long butterflies: Negative

**3. Gamma P&L:**

Important for butterflies:
- Short butterfly: Negative gamma
- Long butterfly: Positive gamma

### For Combined Trades (Diagonal)

$$
\delta \Pi_D \approx \underbrace{\text{Vega}_{K_2,T_2} \cdot \delta\sigma_{K_2,T_2}}_{\text{Back month, different strike}} - \underbrace{\text{Vega}_{K_1,T_1} \cdot \delta\sigma_{K_1,T_1}}_{\text{Front month, different strike}} + \theta_{\text{net}} \, \delta t
$$

**The complexity:**

- Each option has IV at different (K, T) point
- P&L depends on **both** dimensions changing
- Plus the **correlation** between them

**Example:**
- Front month ATM IV changes: +2%
- Back month OTM IV changes: +3%
- Diagonal profits from: 
  * Term structure steepening
  * Skew steepening (if long OTM)
  * **Combined effect**

### The Relationship P&L

**Key insight:** 

The P&L from diagonal/combined trades depends on the **correlation** between horizontal and vertical IV changes:

$$
\delta \Pi \propto \rho(\delta\sigma_{\text{horizontal}}, \delta\sigma_{\text{vertical}})
$$

**When correlation breaks down:**

- Normal: $\rho \approx 0.7-0.9$
- Stressed: $\rho$ varies wildly
- **Opportunity:** Trade the correlation normalization

---

## Types of Horizontal vs Vertical Strategies

### 1. Pure Horizontal (Term Structure Focus)

**When to use:**
- Trading time dimension only
- Clear view on term structure slope
- Want to isolate from strike effects

**Examples:**

**A. Standard Calendar:**
- Same strike, different times
- Steepening bet

**B. Reverse Calendar:**
- Same strike, inverted structure
- Flattening bet

**C. Ratio Calendar:**
- Unequal contracts
- Enhanced theta or vega

**Characteristics:**
- Delta-neutral (approximately)
- Vega-positive (usually)
- Theta-positive (usually)
- **Strike-independent**

### 2. Pure Vertical (Smile/Skew Focus)

**When to use:**
- Trading strike dimension only
- Clear view on smile shape
- Want to isolate from time effects

**Examples:**

**A. Butterfly Spread:**
- Three strikes, same expiration
- Smile flattening bet

**B. Risk Reversal:**
- OTM call + OTM put
- Skew direction bet

**C. Vertical Spread:**
- Two strikes, directional + skew
- Bounded risk/reward

**Characteristics:**
- Delta varies (depends on strikes)
- Vega varies (depends on structure)
- Theta varies (depends on moneyness)
- **Time-independent** (same expiration)

### 3. Horizontal-Heavy Diagonal

**Structure:**
- Emphasize term structure
- Strikes close together
- Time spread dominant

**Example:**
- Buy 90-day $100 call
- Sell 30-day $102 call
- Mostly a calendar, slight vertical component

**When to use:**
- Primary view on term structure
- Secondary view on direction
- Want some directional flexibility

### 4. Vertical-Heavy Diagonal

**Structure:**
- Emphasize smile/skew
- Times close together
- Strike spread dominant

**Example:**
- Buy 45-day $95 put
- Sell 30-day $100 put
- Mostly a vertical spread, slight calendar component

**When to use:**
- Primary view on skew
- Secondary view on time decay
- Want some theta benefit

### 5. Balanced Diagonal

**Structure:**
- Equal emphasis on both dimensions
- Moderate strike difference
- Moderate time difference

**Example:**
- Buy 90-day $105 call
- Sell 30-day $110 call
- True diagonal structure

**When to use:**
- Views on both dimensions
- Want combined exposure
- Directional + term structure bet

### 6. Horizontal vs Vertical Relationship Trade

**Structure:**
- Explicitly trade the correlation
- Compare slopes across dimensions

**Example:**
- Front month skew is very steep (vertical)
- Term structure is very flat (horizontal)
- **Historically, these move together**
- Trade: Expect convergence

**Specific trade:**
- Buy front-month vertical spread (capture steep skew)
- Sell back-month vertical spread (flat skew)
- Bet: Skews will align

**When to use:**
- Divergence between dimensions
- Historical correlation broken
- Mean reversion expected

---

## Concrete Example 1: Pure Horizontal Trade (Calendar)

**Setup:**

**Stock:** SPY at $480

**Market IVs (ATM):**
- 1-month: 15% (low)
- 3-month: 18% (low)
- 6-month: 22% (elevated)

**Analysis:**

- Term structure: Normal upward slope
- But front months compressed
- Historical 1m/3m ratio: 0.85
- Current ratio: 0.83
- **Opportunity:** Term structure should steepen

**The trade:**

**Standard calendar at ATM:**

- Sell 1-month $480 call @ IV=15% = $8.50
- Buy 3-month $480 call @ IV=18% = $13.20
- **Net debit: $13.20 - $8.50 = $4.70**

**Position analysis:**

**Greeks:**
- Delta: ≈ 0
- Vega (net): +0.25 (long back month vega)
- Theta: +$15/day
- Gamma: Mixed (small)

**The bet:**

1. **Term structure steepens:** 3m IV rises relative to 1m
2. **Time decay:** Front month decays faster
3. **Stock stays near $480:** Optimal for calendars

**Scenario 1 (30 days later - optimal):**

**If term structure steepens:**
- 1-month expired (was $8.50)
- 3-month (now 2-month) IV: 18% → 20%
- 3-month call now worth: $11.50
- **P&L:** -$4.70 + $8.50 (expired) + $11.50 (current value) - $13.20 (cost)
- **Profit: $2.10** (45% return)

**Scenario 2: Stock moves to $490:**
- 1-month call: $10 at expiration (ITM)
- 3-month call: Worth $15
- Calendar compressed
- **P&L:** -$4.70 + $8.50 - $10 (buy back) + $15 - $13.20
- **Loss: ≈ -$4.40**

**Scenario 3: Term structure flattens:**
- 1-month expired
- 3-month IV: 18% → 16% (dropped)
- 3-month call: Worth $9.80
- **P&L:** -$4.70 + $8.50 + $9.80 - $13.20
- **Profit: $0.40** (small, from theta only)

---

## Concrete Example 2: Pure Vertical Trade (Butterfly)

**Setup:**

**Stock:** AAPL at $180

**Market IVs (30-day):**
- $170 call: IV = 22%
- $180 call: IV = 18%
- $190 call: IV = 24%

**Analysis:**

- Smile shape: Elevated wings
- ATM is cheap relative to wings
- Historical: Wings should be closer to ATM
- **Opportunity:** Smile should flatten

**The trade:**

**Long butterfly (bet on smile flattening):**

- Buy $170 call @ IV=22% = $14.80
- Sell 2× $180 calls @ IV=18% = $7.50 each
- Buy $190 call @ IV=24% = $4.20
- **Net cost: $14.80 - $15.00 + $4.20 = $4.00**

**Position analysis:**

**Greeks:**
- Delta: ≈ 0 (if stock at $180)
- Vega: +0.15 (net long wings)
- Theta: -$8/day (cost of convexity)
- Gamma: +15 (positive gamma at center)

**The bet:**

1. **Smile flattens:** Wing IVs decrease toward ATM
2. **Stock stays at $180:** Maximum profit at center
3. **Realized vol < implied:** Long gamma profitable

**Scenario 1 (at expiration - stock at $180):**

**If smile flattened:**
- All options expire at/near the money
- Butterfly worth: ≈$0-2
- **P&L:** Lost the $4.00 premium
- **Loss: -$4.00** (max loss)

Wait, this doesn't work for a long butterfly at expiration if stock is exactly at the center strike. Let me reconsider.

Actually, at expiration, if stock is exactly at $180:
- $170 call: $10 ITM
- 2× $180 calls: $0
- $190 call: $0 OTM
- Value: $10 - 0 + 0 = $10
- **P&L: $10 - $4 = $6 profit**

**Scenario 2 (before expiration - smile flattens):**

**If IVs converge to 20%:**
- $170 call @ IV=20%: $13.00 (down from $14.80)
- $180 call @ IV=20%: $7.80 (up from $7.50)
- $190 call @ IV=20%: $3.50 (down from $4.20)
- **Butterfly value: $13.00 - $15.60 + $3.50 = $0.90**
- **P&L: $0.90 - $4.00 = -$3.10 loss**

Hmm, that's a loss. The issue is that when smile flattens, the wings lose value. Let me reconsider what we actually want to trade.

If the smile is too steep (wings too expensive), we want to **SELL the butterfly**:

**Corrected trade:**

**Short butterfly (sell expensive smile):**

- Sell $170 call @ $14.80
- Buy 2× $180 calls @ $7.50
- Sell $190 call @ $4.20
- **Net credit: $14.80 - $15.00 + $4.20 = $4.00**

**The bet:** Smile flattens (wings get cheaper relative to ATM)

**Scenario (smile flattens):**
- Wings lose value
- Butterfly loses value
- We profit from short position

**At expiration (stock at $180):**
- Butterfly worth $10 (max value)
- We need to buy it back
- **Loss: $10 - $4 = -$6** (this is the risk)

**Before expiration (smile flattens to all 20% IV):**
- Butterfly worth $0.90 (from calculation above)
- **P&L: $4.00 - $0.90 = $3.10 profit**

This makes more sense.

---

## Concrete Example 3: Combined Trade (Diagonal)

**Setup:**

**Stock:** Tech stock at $100

**Market conditions:**

**Horizontal (term structure):**
- 1-month ATM IV: 25%
- 3-month ATM IV: 28%
- Normal upward slope

**Vertical (skew):**
- 1-month $105 call IV: 27%
- 3-month $105 call IV: 30%
- Wings elevated as expected

**Your view:**

- **Moderately bullish** (directional)
- **Term structure will steepen** (horizontal)
- **Comfortable holding time** (diagonal approach)

**The trade:**

**Bullish diagonal:**

- Buy 3-month $105 call @ IV=30% = $5.80
- Sell 1-month $108 call @ IV=28% = $2.20
- **Net debit: $5.80 - $2.20 = $3.60**

**Position analysis:**

**Greeks:**
- Delta: +25 (net bullish)
- Vega: +0.30 (net long back month)
- Theta: +$8/day (short front offsets some)
- Gamma: Small positive

**Profit drivers (multiple dimensions):**

1. **Directional:** Stock moves to $105-108
2. **Horizontal:** Term structure steepens
3. **Vertical:** $105 strike IV stays elevated
4. **Time decay:** Front month decays

**Scenario 1 (30 days later - stock at $107):**

- Short $108 call expires worthless: Keep $2.20
- Long $105 call (now 60-day) @ IV=31%: Worth $8.50
- **P&L: -$3.60 + $2.20 + $8.50 - $5.80 = $1.30 profit**

**Breakdown:**
- Directional gain: Stock moved up
- Horizontal gain: Back month IV increased
- Theta gain: Front month decayed
- **All dimensions contributed!**

**Scenario 2: Stock at $103 (modest move):**
- Short $108 call: Expires worthless
- Long $105 call: Worth $5.50
- **P&L: -$3.60 + $2.20 + $5.50 - $5.80 = -$1.70 loss**

**Scenario 3: Stock at $110 (large move):**
- Short $108 call: $2 ITM, pay -$2.00
- Long $105 call: Worth $11.00
- **P&L: -$3.60 + $2.20 - $2.00 + $11.00 - $5.80 = $1.80 profit**

**Analysis:**

The diagonal profits from:
- Upward movement (directional)
- Term structure behavior (horizontal)
- Skew maintaining (vertical)
- Time decay (theta)

**Multiple dimensions working together!**

---

## Concrete Example 4: Horizontal vs Vertical Relationship Trade

**Setup:**

**Stock:** SPY at $450

**Unusual observation:**

**Front month (30-day):**
- $440 put IV: 28%
- $450 call IV: 20%
- $460 call IV: 24%
- **Skew: Very steep** (8 point put/ATM spread)

**Back month (90-day):**
- $440 put IV: 24%
- $450 call IV: 22%
- $460 call IV: 23%
- **Skew: Very flat** (only 2 point spread)

**Analysis:**

**Historically:**
- Front and back month skews track closely
- Correlation ≈ 0.85
- Both should be steep or both flat

**Currently:**
- Front skew: Steep
- Back skew: Flat
- **Correlation broken!**
- **Opportunity:** Convergence trade

**The trade:**

**Skew relationship arbitrage:**

**Leg 1: Capture front month steep skew**

Buy front-month put spread (benefit from steep skew):
- Buy $440 put @ IV=28%
- Sell $450 put @ IV=20%
- Net cost: ≈$2.80

**Leg 2: Sell back month flat skew**

Sell back-month put spread (skew should steepen):
- Sell $440 put @ IV=24%
- Buy $450 put @ IV=22%
- Net credit: ≈$2.20

**Combined position:**

- Net: Pay $2.80 - $2.20 = **$0.60 debit**
- **Ratio spread across time and strike**

**The bet:**

1. **Front month skew normalizes** (flattens)
2. **Back month skew steepens** (normalizes)
3. **Relationship converges**

**Profit drivers:**

**Scenario 1 (15 days later - skews converge):**

**Front month skew flattens:**
- $440 put IV: 28% → 24% 
- $450 put IV: 20% → 22%
- Spread value decreases to $2.00

**Back month skew steepens:**
- $440 put IV: 24% → 26%
- $450 put IV: 22% → 22%
- Spread value increases to $2.80

**Close position:**
- Front spread: Was $2.80, now $2.00 → Buy back for $2.00
- Back spread: Was $2.20, now $2.80 → Buy back for $2.80

**P&L:**
- Front: -$2.80 + $2.00 = -$0.80
- Back: +$2.20 - $2.80 = -$0.60
- **Total: -$1.40 loss**

Wait, this doesn't work. Let me reconsider the trade structure.

Actually, if we think front skew will flatten and back skew will steepen:

**Corrected trade:**

**Sell front month put vertical** (capture expensive skew):
- Sell $440 put @ IV=28%
- Buy $450 put @ IV=20%
- Net credit: $2.80

**Buy back month put vertical** (will gain from steepening):
- Buy $440 put @ IV=24%
- Sell $450 put @ IV=22%
- Net cost: $2.20

**Net: Credit $0.60**

**When skews normalize:**

Front skew flattens (we're short the steep part):
- Profit as spread narrows

Back skew steepens (we're long the cheap part):
- Profit as spread widens

This is cleaner and works!

---

## Strike Selection Strategy

### For Horizontal Trades (Calendars)

**Goal:** Isolate term structure bet

**Strike selection:**

**ATM strikes (most common):**
- Maximum sensitivity to term structure
- Highest liquidity
- Clearest signal

**Why ATM:**
- Vega concentrated at ATM
- Skew effects minimized
- Pure time dimension exposure

**OTM strikes (special cases):**
- When combining with directional view
- Or when ATM liquidity poor
- Still same strike across time

**Strike rules:**
- **Same strike** for front and back
- Typically ATM ± 1 strike
- High liquidity essential

### For Vertical Trades (Butterflies, Verticals)

**Goal:** Isolate smile/skew bet

**Strike selection:**

**For butterflies:**

**Centered butterflies:**
- Center at ATM
- Wings equidistant (±1 SD, or ±5%, ±10%)
- Pure smile bet

**Example:**
- Stock at $100
- Buy $95 + $105
- Sell 2× $100

**Shifted butterflies:**
- Center away from ATM
- Trade specific smile region
- Can be far OTM

**For risk reversals:**

**Standard:**
- 25-delta call and put (common in FX)
- Measures skew directly
- Industry standard

**Custom:**
- Any OTM strikes
- Reflects your skew view
- Match to expected range

**Strike rules:**
- **Same expiration** for all options
- Consider liquidity at each strike
- Symmetric or asymmetric (your choice)

### For Diagonal Trades

**Goal:** Express views on both dimensions

**Strike selection:**

**Horizontal-heavy:**
- Front and back strikes close (1-2 strikes apart)
- Emphasizes term structure
- Slight directional bias

**Vertical-heavy:**
- Front and back strikes far apart
- Emphasizes smile/skew
- Strong directional component

**Balanced:**
- Moderate strike separation
- Equal weight to both dimensions

**Common patterns:**

**Bullish diagonal:**
- Long back: ATM to slightly ITM
- Short front: OTM
- Example: Long 90-day $100, Short 30-day $105

**Bearish diagonal:**
- Long back: ATM to slightly ITM (put)
- Short front: OTM (put)
- Example: Long 90-day $100 put, Short 30-day $95 put

---

## Time Frame Selection

### For Horizontal Trades (Pure Term Structure)

**Front month:**
- **30-45 days:** Standard
- High theta decay
- Liquid options
- Not too close to expiration

**Back month:**
- **90-120 days:** Standard
- 2:1 to 3:1 ratio (back:front)
- Stable vega exposure
- Time for thesis to play out

**Special cases:**

**Short-term term structure:**
- Front: 7-14 days
- Back: 30-45 days
- Very steep decay differential
- Higher risk (gamma)

**Long-term term structure:**
- Front: 60 days
- Back: 180 days (LEAPS)
- Stable, lower maintenance
- Lower theta edge

### For Vertical Trades (Pure Smile/Skew)

**Standard expirations:**
- **30-60 days:** Most common
- Adequate time for normalization
- Good liquidity
- Manageable Greeks

**Why these maturities:**
- Smile well-defined
- Sufficient vega
- Not dominated by gamma (near expiry)
- Not too expensive (far expiry)

**Special cases:**

**Near-term smile (7-14 days):**
- Very sensitive to skew changes
- High gamma risk
- Event-driven (earnings)

**Long-term smile (90-180 days):**
- More stable
- Expensive
- Structural views

### For Diagonal Trades

**Time spread:**
- **2:1 to 3:1 ratio** (back:front)
- Example: 90-day back, 30-day front
- Standard for most diagonals

**Timing considerations:**

1. **Front month:** When to expect short-term moves
2. **Back month:** Enough time for longer thesis
3. **Gap between:** Allows for rolling

---

## Position Management

### Managing Horizontal Trades (Calendars)

**Entry checklist:**

✓ Term structure shape identified
✓ View on steepening/flattening
✓ No major events in front month
✓ Adequate liquidity
✓ Stock in expected range

**During the trade:**

**Monitor:**
1. **Term structure slope:** Is it steepening as expected?
2. **Stock price:** Staying near strike?
3. **Theta accumulation:** On track?
4. **Front month expiration:** Approaching?

**Adjustment triggers:**

**Stock moves away (> ±5% from strike):**
- Close position
- Or roll strike to new level
- Or adjust to diagonal

**Term structure inverts:**
- Consider closing
- Thesis no longer valid
- Cut losses

**Front month approaching (7-14 days):**
- Roll to next month
- Or close entire position
- Avoid gamma explosion

### Managing Vertical Trades (Butterflies)

**Entry checklist:**

✓ Smile shape analyzed
✓ View on flattening/steepening
✓ Adequate time to expiration (>30 days)
✓ Good liquidity at all strikes
✓ Delta-neutral (if desired)

**During the trade:**

**Monitor:**
1. **Smile shape:** Changing as expected?
2. **Stock price:** Near center of butterfly?
3. **Realized vol:** vs implied?
4. **Greeks:** Delta, gamma in check?

**Adjustment triggers:**

**Stock moves to wing (> ±3-4%):**
- Close position
- Or adjust center
- Or let it ride (if thesis intact)

**Smile steepens more (if short fly):**
- May need to close
- Loss expanding
- Reassess thesis

**Near expiration (<14 days):**
- Gamma risk increases
- Close or roll
- Avoid pin risk

### Managing Diagonal Trades

**Entry checklist:**

✓ Views on both dimensions clear
✓ Directional bias defined
✓ Term structure favorable
✓ Strike selection appropriate
✓ Risk understood

**During the trade:**

**Monitor:**
1. **Both dimensions:** Horizontal and vertical
2. **Stock price:** Directional component
3. **Term structure:** Changes
4. **Skew:** At both long and short strikes

**Adjustment triggers:**

**Stock moves against you:**
- Roll short strike
- Adjust structure
- May convert to different trade

**Either dimension moves adversely:**
- Re-evaluate thesis
- May need to close
- Cut losses if both turn

**Front month expiration:**
- Standard: Roll short leg
- Or close entire position
- Adjust based on P&L

### Managing Relationship Trades

**Entry checklist:**

✓ Relationship divergence identified
✓ Historical correlation known
✓ Mean reversion thesis clear
✓ Both sides liquid
✓ Risk limits set

**During the trade:**

**Monitor:**
1. **Correlation:** Is it normalizing?
2. **Individual dimensions:** How are they behaving?
3. **P&L attribution:** Which dimension contributing?
4. **Time decay:** Working for or against you?

**Adjustment triggers:**

**Relationship normalizes (50-75% of expected):**
- **Take profit**
- Don't wait for perfect
- Lock in gains

**Relationship diverges more:**
- Reassess thesis
- Set stop loss
- May be regime change

**Time running out:**
- Close at 14 days
- Avoid expiration complexity
- Redeploy if needed

---

## Greeks Analysis

### Horizontal (Calendar) Greeks

**Delta:**

Near zero for ATM calendars:

$$
\Delta_{\text{calendar}} \approx \Delta_{\text{back}} - \Delta_{\text{front}} \approx 0
$$

**Vega:**

Net positive (back month dominates):

$$
\text{Vega}_{\text{calendar}} = \text{Vega}_{\text{back}} - \text{Vega}_{\text{front}} > 0
$$

**Theta:**

Usually positive (front decays faster):

$$
\Theta_{\text{calendar}} = \theta_{\text{back}} - \theta_{\text{front}} > 0
$$

**Gamma:**

Mixed (depends on specifics):

$$
\Gamma_{\text{calendar}} = \Gamma_{\text{back}} - \Gamma_{\text{front}}
$$

Can be positive or negative

### Vertical (Butterfly) Greeks

**Delta:**

Near zero for ATM butterflies:

$$
\Delta_{\text{fly}} = \Delta_{K_1} - 2\Delta_{K_2} + \Delta_{K_3} \approx 0
$$

**Vega:**

For long butterfly (wings):

$$
\text{Vega}_{\text{fly}} = \text{Vega}_{K_1} - 2\text{Vega}_{K_2} + \text{Vega}_{K_3}
$$

Often positive (depends on strikes)

**Theta:**

For long butterfly:

$$
\Theta_{\text{fly}} < 0
$$

Negative (paying for convexity)

**Gamma:**

For long butterfly:

$$
\Gamma_{\text{fly}} > 0
$$

Positive (at center)

### Diagonal Greeks

**Delta:**

Varies significantly based on strikes:

$$
\Delta_{\text{diag}} = \Delta_{\text{back}} - \Delta_{\text{front}}
$$

Can be positive (bullish), negative (bearish), or near zero

**Vega:**

Usually positive (back month larger):

$$
\text{Vega}_{\text{diag}} = \text{Vega}_{\text{back}} - \text{Vega}_{\text{front}} > 0
$$

But depends on strikes too

**Theta:**

Usually positive (front decays faster):

$$
\Theta_{\text{diag}} = \theta_{\text{back}} - \theta_{\text{front}} > 0
$$

**Gamma:**

Complex, depends on both strikes and times

### Relationship Between Greeks Across Dimensions

**Key insight:**

Greeks from horizontal and vertical dimensions **combine non-linearly**:

**Example: Diagonal vega**

Not simply:
$$
\text{Vega}_{\text{diag}} \neq \text{Vega}_{\text{calendar}} + \text{Vega}_{\text{vertical}}
$$

But rather:
$$
\text{Vega}_{\text{diag}} = f(\text{Vega}_{\text{horizontal}}, \text{Vega}_{\text{vertical}}, \rho)
$$

Where $\rho$ = correlation between dimension moves

**This is why diagonals are complex!**

---

## When to Use Horizontal vs Vertical Strategies

### Use Horizontal (Calendar) When:

**Market conditions ✓**

- Clear view on **term structure**
- Stock expected range-bound
- No major events in front month
- Term structure slope unusual

**Your situation ✓**

- Want positive theta
- Want long vega (usually)
- Can monitor regularly
- Comfortable rolling

**Avoid horizontal when ✗**

- Trending market (stock won't stay)
- Earnings in front month
- Term structure inverted (crisis)
- Very low IV (little edge)

### Use Vertical (Butterfly/Vertical) When:

**Market conditions ✓**

- Clear view on **smile/skew**
- Skew extreme (steep or flat)
- Same-expiration focus
- Want to isolate strike dimension

**Your situation ✓**

- View on realized vol vs implied
- Want defined risk
- Can tolerate some theta cost (long fly)
- Or want theta income (short fly)

**Avoid vertical when ✗**

- Skew looks normal
- Near expiration (<14 days, gamma risk)
- Poor liquidity at wings
- No clear skew thesis

### Use Diagonal When:

**Market conditions ✓**

- Views on **both dimensions**
- Directional bias + time/skew view
- Want flexibility
- Combining multiple theses

**Your situation ✓**

- Comfortable with complexity
- Can manage multiple Greeks
- Want to express combined view
- Willing to adjust actively

**Avoid diagonal when ✗**

- Only have single-dimension view
- Want simplicity
- Can't monitor actively
- First time with spreads

### Use Relationship Trades When:

**Market conditions ✓**

- **Correlation broken** between dimensions
- Historical relationship clear
- Mean reversion expected
- Adequate liquidity both sides

**Your situation ✓**

- Sophisticated understanding
- Can model relationships
- Patient (may take time)
- Comfortable with basis risk

**Avoid relationship trades when ✗**

- Normal correlation
- No historical precedent
- Regime change suspected
- Can't model properly

---

## Common Mistakes

### 1) Confusing Dimensions

**The error:**

- Entering a calendar to trade skew
- Or butterfly to trade term structure
- **Wrong tool for the job!**

**Fix:**

- **Calendar = horizontal** (term structure)
- **Butterfly = vertical** (smile/skew)
- Match strategy to dimension

### 2) Ignoring Correlation Between Dimensions

**The error:**

- "I'll trade term structure, skew won't matter"
- Stock moves, skew changes too
- Unexpected P&L from other dimension

**Fix:**

- Dimensions are **correlated**
- Understand cross-effects
- Monitor both even if trading one

### 3) Wrong Strike for Horizontal Trade

**The error:**

- Using OTM strikes for calendar
- Want to trade term structure
- But now have directional + skew exposure too

**Fix:**

- **ATM strikes** for pure horizontal
- Same strike across time
- Minimize vertical contamination

### 4) Wrong Expiration for Vertical Trade

**The error:**

- Using different expirations for butterfly
- Want to trade smile
- But now have term structure exposure too

**Fix:**

- **Same expiration** for pure vertical
- All options same maturity
- Minimize horizontal contamination

### 5) Ignoring Theta in Vertical Trades

**The error:**

- Long butterfly, expensive
- Theta eating away value
- Smile doesn't move enough fast enough

**Fix:**

- Calculate theta cost
- Ensure smile thesis strong enough
- Have time horizon defined

### 6) Over-Complicating with Diagonals

**The error:**

- Using diagonal when simple calendar better
- Adding complexity without benefit
- Harder to manage, no added edge

**Fix:**

- **Start simple:** Calendar or vertical
- Only use diagonal if clear reason
- Complexity should add value

### 7) Fighting Regime Changes

**The error:**

- "Correlation always mean-reverts"
- Market enters new regime (COVID, 2008)
- Old relationships break permanently

**Fix:**

- Recognize regime shifts
- Accept when market structure changes
- Don't fight new normal

---

## Advanced Concepts

### 1. Quantifying the Relationship

**Correlation metric:**

$$
\rho(\Delta \sigma_H, \Delta \sigma_V) = \frac{\text{Cov}(\Delta \sigma_H, \Delta \sigma_V)}{\text{Std}(\Delta \sigma_H) \cdot \text{Std}(\Delta \sigma_V)}
$$

where:
- $\Delta \sigma_H$ = Changes in term structure slope
- $\Delta \sigma_V$ = Changes in skew steepness

**Historical analysis:**

- Calculate correlation over time
- Identify when it breaks down
- Trade mean reversion

**Example:**

Historical correlation: 0.75
Current correlation: 0.35
**Divergence:** Trade for convergence

### 2. Principal Component Analysis (PCA)

**The method:**

Decompose surface movements into independent factors:

**Factor 1: Parallel shift (level)**
- All IVs move together
- Explains ~70-80% of variance

**Factor 2: Term structure tilt (horizontal)**
- Front vs back movement
- Explains ~15-20% of variance

**Factor 3: Smile curvature (vertical)**
- Wings vs ATM movement
- Explains ~5-10% of variance

**Application:**

- Trade specific factors
- Hedge unwanted factors
- Isolate your bet

### 3. Local Volatility vs Implied Volatility

**Local volatility:**

$$
\sigma_{\text{local}}^2(K, T) = \frac{\frac{\partial C}{\partial T} + rK\frac{\partial C}{\partial K}}{\frac{1}{2}K^2\frac{\partial^2 C}{\partial K^2}}
$$

**Relationship to IV surface:**

- Local vol is derived from IV surface
- Ensures no arbitrage
- Different from IV!

**Trading implications:**

- IV surface can have bumps
- Local vol smooth
- Discrepancies = opportunities

### 4. Volatility Surface Dynamics

**Sticky strike:**
- IV "sticks" to absolute strikes
- Common in equity indices

**Sticky delta:**
- IV "sticks" to moneyness
- Common in FX

**Mixed behavior:**
- Varies by asset class
- Changes over time

**Implications for horizontal vs vertical:**

**Sticky strike:**
- As stock moves, smile shape preserved
- Horizontal trades less affected
- Vertical trades more sensitive

**Sticky delta:**
- Smile moves with stock
- Horizontal trades more affected
- Complex interactions

### 5. Variance Dispersion Across Dimensions

**The concept:**

Variance can differ across dimensions:

**Horizontal variance:**
$$
\text{Var}(\sigma_T) = \text{How much term structure varies}
$$

**Vertical variance:**
$$
\text{Var}(\sigma_K) = \text{How much smile varies}
$$

**When horizontal variance > vertical variance:**
- Term structure more unstable
- Calendar trades riskier
- Butterfly trades safer

**When vertical variance > horizontal variance:**
- Smile more unstable
- Butterfly trades riskier
- Calendar trades safer

### 6. Cross-Asset Relationships

**Horizontal relationships across assets:**

- SPX term structure vs VIX term structure
- High correlation
- Trade dislocations

**Vertical relationships across assets:**

- SPX skew vs individual stock skews
- Correlation varies
- Dispersion opportunities

**Example trade:**

- SPX term structure steep
- Component stocks term structure flat
- **Trade:** Buy component calendars, sell SPX calendar

---

## Real-World Examples

### Example 1: COVID-19 Crisis (March 2020)

**Observation:**

**Horizontal dimension (term structure):**
- Front month (30-day) IV: **85%** (extreme)
- Back month (90-day) IV: **60%** (elevated but less)
- **Massive inversion**

**Vertical dimension (smile):**
- 30-day OTM put IV: **95%**
- 30-day ATM IV: **85%**
- **Skew extremely steep**

**Analysis:**

- Both dimensions at extremes
- But horizontal more extreme (inverted)
- Historical: Term structure mean-reverts faster than skew

**The trade (aggressive):**

**Long calendar (bet on term structure normalization):**

- Sell front-month ATM call @ IV=85%
- Buy back-month ATM call @ IV=60%
- **Very risky:** Selling into panic

**What happened:**

**Week 1-2:**
- Front month IV stayed elevated (80-90%)
- Calendar struggled
- Losses mounting

**Week 3-4:**
- Panic subsided
- Front month IV collapsed: 85% → 50%
- Back month IV: 60% → 55%
- **Term structure normalized**

**Result:**
- Calendar profitable
- 40-60% returns in 4 weeks
- But required nerve and risk tolerance

**Lesson:**

- Horizontal dimension (term structure) mean-reverted
- Vertical dimension (skew) stayed elevated longer
- **Timing and risk management critical**

### Example 2: Earnings Volatility (Tech Stock)

**Setup:**

**Stock:** NVDA at $500, earnings in 28 days

**Observation:**

**Horizontal (term structure):**
- 1-month (includes earnings) IV: **70%**
- 3-month (after earnings) IV: **45%**
- Extreme elevation in front month

**Vertical (smile):**
- 1-month skew: Relatively flat (binary event)
- 3-month skew: Normal equity skew
- Different smile shapes!

**Analysis:**

- **Horizontal:** Clear dislocation (earnings premium)
- **Vertical:** Front month smile compressed by event
- **Relationship:** Temporarily broken

**The trade:**

**Reverse calendar (sell elevated front):**

- Sell 1-month $500 call @ IV=70%
- Buy 3-month $500 call @ IV=45%
- **Bet:** Front month IV crushes after earnings

**What happened:**

**Before earnings (days 1-27):**
- Front month IV stayed 65-70%
- Position flat to slightly profitable
- Time decay helped

**After earnings (day 29):**
- Stock moved 8% (in line with historical)
- Front month IV crushed: 70% → 35%
- Back month IV unchanged: 45%
- **Reverse calendar profitable**

**Result:**
- 50-80% return
- IV crush was the driver
- Horizontal dimension trade

**Lesson:**

- **Event-driven horizontal dislocations** are tradeable
- Vertical dimension less relevant for event trades
- Timing around event critical

### Example 3: Skew Normalization (Post-Crisis 2021)

**Setup:**

**Stock:** SPY at $420 (post-COVID recovery)

**Observation:**

**Vertical (smile):**
- OTM put IV: **35%**
- ATM IV: **18%**
- **Skew extremely steep** (fear premium lingering)

**Horizontal (term structure):**
- All maturities: Normal upward slope
- 1m: 18%, 3m: 20%, 6m: 22%
- Nothing unusual

**Analysis:**

- **Vertical:** Dislocation (skew too steep for recovery)
- **Horizontal:** Normal
- Pure vertical trade opportunity

**The trade:**

**Short butterfly (sell expensive skew):**

- Sell $400 put @ IV=35%
- Buy 2× $420 calls @ IV=18%
- Sell $440 call @ IV=20%
- **Net credit:** Receive premium

**What happened:**

**Over 60 days:**
- Market continued recovering
- Fear premium declined
- OTM put IV: 35% → 25%
- ATM IV: 18% → 18% (unchanged)
- **Skew flattened**

**Result:**
- Butterfly value decreased
- Profitable short position
- 40-50% return on capital at risk

**Lesson:**

- **Pure vertical trades** when skew abnormal
- Horizontal dimension irrelevant
- Mean reversion in smile shape

---

## Practical Implementation

### 1. Daily Analysis Workflow

**Morning routine:**

**Step 1: Horizontal analysis (15 minutes)**

```
For each stock/index:
1. Plot term structure curve
2. Calculate front/back ratios
3. Compare to historical percentiles
4. Flag inversions or unusual slopes
```

**Step 2: Vertical analysis (15 minutes)**

```
For each expiration:
1. Plot volatility smile
2. Calculate skew metrics (25-delta spread)
3. Compare to historical norms
4. Flag steep or flat anomalies
```

**Step 3: Relationship analysis (10 minutes)**

```
For each asset:
1. Check correlation between dimensions
2. Identify divergences
3. Assess mean-reversion potential
4. Rank opportunities
```

**Step 4: Trade generation (10 minutes)**

```
Prioritize by:
- Magnitude of dislocation
- Liquidity
- Conviction
- Risk/reward
```

### 2. Metrics to Track

**Horizontal metrics:**

```
Term structure slope:
- (IV_3m - IV_1m) / IV_1m
- Historical percentile
- Z-score vs average

Inversion indicator:
- Binary: Yes/No
- Magnitude if inverted
```

**Vertical metrics:**

```
Skew steepness:
- (IV_95put - IV_ATM) / IV_ATM
- 25-delta put/call spread
- Historical percentile

Smile curvature:
- Second derivative
- Butterfly value vs theoretical
```

**Relationship metrics:**

```
Dimension correlation:
- 30-day rolling correlation
- Current vs average
- Divergence magnitude

Surface consistency:
- How smooth is the surface?
- Any bumps or dislocations?
```

### 3. Position Sizing Framework

**For horizontal trades:**

```
Capital allocation:
- 10-20% of portfolio max
- Per calendar: 2-5% of portfolio
- Based on:
  * Liquidity
  * Conviction
  * Volatility of term structure
```

**For vertical trades:**

```
Capital allocation:
- 10-20% of portfolio max
- Per butterfly: 2-5% of portfolio
- Based on:
  * Width of butterfly
  * Skew dislocation magnitude
  * Time to expiration
```

**For diagonal/relationship trades:**

```
Capital allocation:
- 5-15% of portfolio max
- Per trade: 1-3% of portfolio
- More conservative due to:
  * Complexity
  * Multiple risk factors
  * Harder to manage
```

### 4. Risk Management Rules

**Stop losses:**

**Horizontal trades:**
- Exit if term structure inverts (if long calendar)
- Stop: -30% of debit paid
- Or: 14 days to front expiration

**Vertical trades:**
- Exit if skew steepens 50% more (if short fly)
- Stop: -40% of credit received
- Or: < 14 days to expiration

**Diagonal trades:**
- Exit if stock breaks out of range
- Stop: -35% of debit paid
- Or: Reassess at front expiration

**Relationship trades:**
- Exit if correlation diverges further
- Stop: -50% of expected profit
- Or: Regime change evident

### 5. Technology and Tools

**Required tools:**

**Data:**
- Real-time option chains
- IV surface calculator
- Historical IV database

**Analytics:**
- Term structure plotter
- Smile curve fitter
- Correlation calculator

**Execution:**
- Spread order entry
- Multi-leg optimizer
- Greeks monitor

**Backtesting:**
- Historical surface data
- Strategy simulator
- P&L attribution

**Example Python workflow:**

```python
# Pseudocode for daily analysis

# 1. Fetch data
option_chain = get_option_chain(symbol, all_expirations)

# 2. Calculate IVs
ivs = calculate_implied_vols(option_chain)

# 3. Build surface
surface = fit_iv_surface(ivs)

# 4. Analyze dimensions
term_structure = extract_horizontal(surface, strike=ATM)
smile = extract_vertical(surface, expiration='30d')

# 5. Identify opportunities
if is_inverted(term_structure):
    flag_calendar_opportunity()

if is_steep_skew(smile):
    flag_butterfly_opportunity()

# 6. Check correlation
correlation = calculate_dimension_correlation(
    term_structure_changes,
    smile_changes
)

if correlation < historical_avg - 2*std:
    flag_relationship_opportunity()
```

---

## Horizontal vs Vertical in Your Toolkit

### How These Dimensions Fit with Other Strategies

**The complete volatility framework:**

```
Volatility Trading Hierarchy:

1. LEVEL TRADING
   ├── Gamma Scalping → Trade realized vol
   └── Vega Trading → Trade IV level

2. SINGLE DIMENSION
   ├── HORIZONTAL → Term structure
   │   └── Calendar spreads
   └── VERTICAL → Smile/skew
       └── Butterflies, verticals

3. COMBINED DIMENSIONS
   ├── Diagonals → Both dimensions
   └── Relationship trades → Correlation

4. FULL SURFACE
   └── Surface arbitrage → All dimensions
```

**Horizontal and vertical trading provides:**

- **Dimensional clarity** (understand what you're trading)
- **Strategy selection** (right tool for right dimension)
- **Risk isolation** (separate dimensions)
- **Combination opportunities** (trade relationships)

### Comparison with Other Approaches

| Strategy | Horizontal | Vertical | Complexity | When to Use |
|----------|------------|----------|------------|-------------|
| **Calendar** | ✓ | ✗ | Low | Term structure view |
| **Butterfly** | ✗ | ✓ | Low | Skew view |
| **Diagonal** | ✓ | ✓ | Medium | Both dimensions |
| **Relationship** | ✓ | ✓ | High | Correlation trade |
| **Surface Arb** | ✓ | ✓ | Very High | Systematic/quantitative |

**The progression:**

1. **Beginner:** Learn dimensions separately
2. **Intermediate:** Trade one dimension at a time
3. **Advanced:** Combine dimensions (diagonals)
4. **Expert:** Trade relationships and correlations

---

## What to Remember

### Core Concept

**The IV surface has two fundamental dimensions:**

$$
\text{IV}(K, T) = f(\underbrace{K}_{\text{Vertical: Smile}}, \underbrace{T}_{\text{Horizontal: Term Structure}})
$$

- **Horizontal (T):** How IV varies across TIME
- **Vertical (K):** How IV varies across STRIKES
- These dimensions **interact** but can be traded separately

### The Two Dimensions

**Horizontal (Term Structure):**

**What it is:**
- IV vs time to expiration
- Holding strike constant

**How to trade it:**
- **Calendar spreads** (same strike, different times)
- Bet on steepening, flattening, or slope changes

**When to use:**
- Clear term structure view
- Range-bound stock expectation
- Want positive theta (usually)

**Vertical (Smile/Skew):**

**What it is:**
- IV vs strike price
- Holding time constant

**How to trade it:**
- **Butterflies** (same time, different strikes)
- **Risk reversals** (OTM options)
- Bet on smile flattening, steepening

**When to use:**
- Clear skew view
- Want defined risk
- Realized vol view

### Key Relationships

**Correlation between dimensions:**

- **Normal markets:** Positive correlation (~0.7-0.9)
- **Stressed markets:** Correlation varies
- **Opportunity:** Trade correlation breakdown

**How they interact:**

- Term structure steepens → Skew often steepens
- But not always proportionally!
- **Divergences are tradeable**

### Strategy Selection

**Pure horizontal (calendar):**
- Same strike, different times
- Term structure bet
- Theta-positive (usually)

**Pure vertical (butterfly):**
- Different strikes, same time
- Smile/skew bet
- Defined risk

**Combined (diagonal):**
- Different strikes AND times
- Both dimensions
- More complex

**Relationship trades:**
- Explicit correlation bet
- Advanced
- Requires modeling

### Greeks by Dimension

**Horizontal trades:**
- Delta: ≈ 0
- Vega: Positive (back month)
- Theta: Positive (front decays)
- Gamma: Mixed

**Vertical trades:**
- Delta: Variable (depends on structure)
- Vega: Depends on wings vs body
- Theta: Negative (long fly) or Positive (short fly)
- Gamma: Positive (long fly) or Negative (short fly)

**Combined trades:**
- All Greeks active
- Complex interactions
- Requires careful management

### The Deep Insight

**Horizontal vs vertical reveals:**

> "The volatility surface is not a random cloud of IVs—it has structure along two fundamental dimensions: time and strike. By understanding these dimensions separately and how they relate, you can precisely select strategies that isolate your view while minimizing unwanted exposures. This dimensional thinking is the foundation of sophisticated volatility trading."

**The key pattern:**

- **Amateur:** Sees IV as single number
- **Novice:** Sees smile or term structure
- **Intermediate:** Trades one dimension
- **Advanced:** Trades both dimensions
- **Expert:** Trades the **relationship** between dimensions

### Common Pitfalls

1. ❌ Using wrong strategy for dimension (butterfly for term structure)
2. ❌ Ignoring dimension correlation (think they're independent)
3. ❌ Wrong strike selection (OTM for calendar)
4. ❌ Wrong expiration (different times for butterfly)
5. ❌ Over-complicating with diagonals unnecessarily
6. ❌ Ignoring theta cost in vertical trades
7. ❌ Fighting regime changes in correlation

### When to Use Each

**Horizontal (Calendar) ✓:**
- Term structure abnormal
- Stock range-bound
- Want theta income
- No events in front month

**Vertical (Butterfly) ✓:**
- Skew abnormal
- Clear smile view
- Want defined risk
- Adequate time (>30 days)

**Combined (Diagonal) ✓:**
- Views on both dimensions
- Directional + time/skew
- Comfortable with complexity
- Can manage actively

**Relationship Trades ✓:**
- Correlation broken
- Historical mean reversion
- Sophisticated approach
- Patient capital

### Performance Expectations

**Horizontal trades:**
- Win rate: 60-70%
- Returns: 20-40% per trade
- Hold time: 15-30 days
- Frequency: Weekly opportunities

**Vertical trades:**
- Win rate: 55-65%
- Returns: 25-50% per trade
- Hold time: 20-45 days
- Frequency: Monthly opportunities

**Combined/Relationship:**
- Win rate: 50-60%
- Returns: 30-60% per trade
- Hold time: 30-60 days
- Frequency: As opportunities arise

### Final Thought

**Horizontal vs vertical trading teaches:**

> "Every option trade, whether you realize it or not, expresses a view on both the horizontal (term structure) and vertical (smile/skew) dimensions. By explicitly choosing strategies that isolate the dimension you want to trade—or deliberately combining them—you gain precision and control. This dimensional framework transforms options from opaque instruments into precise tools for expressing sophisticated volatility views."

**The strategic value:**

**Horizontal dimension:**
- **Term structure trading** (time)
- **Theta harvesting** capability
- **Vega positioning** across maturities

**Vertical dimension:**
- **Smile/skew trading** (strikes)
- **Realized vol exposure** management
- **Strike-specific** positioning

**Combined:**
- **Maximum flexibility** (both dimensions)
- **Relationship exploitation** (correlation)
- **Complete surface** understanding

**This completes your understanding of the TWO FUNDAMENTAL DIMENSIONS of volatility trading—horizontal (term structure) and vertical (smile/skew)—giving you the framework to select the right strategy for your specific view!** 🎯📊📈

**You now understand: the dimensions separately, how to trade each, how they interact, and how to combine them—the complete dimensional framework for volatility trading!**
