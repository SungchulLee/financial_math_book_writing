# Volatility Smile and Skew Trading

**Volatility smile and skew trading** is a strategy where you profit from mispricing across different option strikes by exploiting the fact that options at different strikes trade at different implied volatilities.

---

## The Core Insight

**The fundamental idea:**
- Black-Scholes theory says: all options on the same stock should have the same implied volatility
- Reality: options at different strikes trade at DIFFERENT implied volatilities
- This creates a pattern called the "volatility smile" or "volatility skew"
- You can trade the SHAPE of this curve, not just the level
- Profit from relative mispricing across strikes

**The key observation:**
$$
\text{IV}_{\text{OTM put}} > \text{IV}_{\text{ATM}} < \text{IV}_{\text{OTM call}} \quad \text{(smile)}
$$
or
$$
\text{IV}_{\text{OTM put}} > \text{IV}_{\text{ATM}} > \text{IV}_{\text{OTM call}} \quad \text{(skew)}
$$

**You're essentially betting: "The market has the wrong shape for implied volatility across strikes."**

---

## What Is the Volatility Smile/Skew?

**Before trading it, we need to understand what it is:**

### The Black-Scholes Expectation

**Theory says:**
- All options on the same underlying, same expiration should have the same implied volatility
- Volatility is a property of the stock, not the strike
- Plot IV vs. Strike → should be flat line

**Example (theoretical):**
- Stock at $100
- ATM call (K=$100): IV = 20%
- OTM call (K=$110): IV = 20%
- OTM put (K=$90): IV = 20%
- **All the same!**

### The Market Reality

**In practice:**
- Different strikes trade at DIFFERENT implied volatilities
- Plot IV vs. Strike → curved line (smile or skew)
- This violates Black-Scholes assumptions

**Example (real market - equities):**
- Stock at $100
- OTM put (K=$90): IV = 25% (high!)
- ATM call (K=$100): IV = 20%
- OTM call (K=$110): IV = 18% (low!)
- **Downward sloping → "volatility skew"**

**Example (real market - FX):**
- EUR/USD at 1.10
- OTM put (K=1.05): IV = 12% (high)
- ATM (K=1.10): IV = 10%
- OTM call (K=1.15): IV = 12% (high)
- **U-shaped → "volatility smile"**

### Visualizing the Patterns

```
Equity Skew (typical):          FX Smile (typical):
    IV                              IV
     ↑                               ↑
  25%|  \                        12%|    /‾‾\
  20%|   \___                    10%|___/   \___
  15%|       \                    8%|
     |________\___→ Strike            |___________→ Strike
     90  100  110                    1.05 1.10 1.15
    OTM  ATM  OTM                    OTM  ATM  OTM
    Put      Call                    Put      Call
```

### Types of Patterns

**1. Volatility Skew (Equities, Indices)**
- Downward sloping from left to right
- OTM puts more expensive than OTM calls
- "Crash protection premium"

**2. Volatility Smile (FX, Some Commodities)**
- U-shaped curve
- Both wings elevated
- Symmetric or asymmetric

**3. Reverse Skew (Rare)**
- Upward sloping
- OTM calls more expensive than OTM puts
- Sometimes in takeover situations

---

## Why Does the Smile/Skew Exist?

**Several reasons why reality differs from Black-Scholes:**

### 1. Crash Fear (Equity Skew)

**Post-1987 phenomenon:**
- 1987 crash traumatized markets
- Deep fear of large downward moves
- Investors pay premium for downside protection
- OTM puts expensive (high IV)

**Supply/Demand:**
- Everyone wants to buy puts (protection)
- Limited sellers
- Price (IV) gets bid up

### 2. Fat Tails (Smile)

**Reality vs. Theory:**
- Black-Scholes assumes log-normal returns
- Reality: returns have fatter tails (more extreme moves)
- Both large ups AND downs more likely than theory
- Both wings (OTM puts and calls) elevated

### 3. Stochastic Volatility

**Volatility itself is random:**
- Black-Scholes assumes constant volatility
- Reality: volatility changes over time
- Volatility clustering (high vol persists)
- Creates smile pattern naturally

### 4. Jump Risk

**Discrete jumps:**
- Stocks can gap (earnings, news, takeovers)
- Black-Scholes assumes continuous price movement
- Jumps create demand for OTM options
- Elevates wings

### 5. Leverage Effect

**Stock down → volatility up:**
- When stock drops, leverage increases (debt/equity)
- Company becomes riskier
- Volatility increases
- Creates negative correlation between price and vol
- Produces skew

### 6. Supply/Demand Imbalances

**Structural demand:**
- Portfolio managers buy puts for insurance
- Covered call writers sell calls
- Corporate buybacks reduce call supply
- Creates persistent skew

---

## The Basic Idea

**What you do:**

### Identify Mispricing

**Compare current skew to:**
1. Historical average skew
2. Theoretical "fair" skew (model-based)
3. Cross-sectionally (this stock vs. others)
4. Intertemporally (front month vs. back month)

### Construct Trade

**Three main approaches:**

**A. Directional Skew Bet**
- Believe skew will steepen or flatten
- Trade structures that profit from shape changes
- Example: Butterfly spreads, risk reversals

**B. Relative Value**
- One strike looks cheap vs. another
- Buy cheap, sell expensive
- Hedge the net vega/delta

**C. Volatility Surface Arbitrage**
- Exploit inconsistencies across strikes AND maturities
- Complex multi-leg trades
- Statistical arbitrage

### Delta Hedge

**As always:**
- Maintain delta neutrality
- Focus on the skew exposure
- Not betting on stock direction

---

## The Portfolio

Your smile/skew trading portfolio consists of:

$$
\Pi = \sum_i w_i \cdot \text{Option}_i(K_i) + \text{Delta Hedge}
$$

where you hold options at multiple strikes $K_i$ with weights $w_i$.

**Why this structure?**
- Multiple strikes → exposure to skew shape
- Weights chosen to target specific skew sensitivity
- Delta hedge → isolate skew risk from directional risk
- Often vega-neutral too (trade pure skew)

**What you're exposed to:**
- ✓ Skew changes (your bet)
- ✓ Some gamma (from option positions)
- ✗ Delta (hedged away)
- ✗ Vega level (often hedged to be neutral)

---

## Common Skew Trading Strategies

### 1. Butterfly Spread

**The classic skew trade:**

**Structure:**
- Buy 1 OTM put (low strike)
- Sell 2 ATM options (middle strike)  
- Buy 1 OTM call (high strike)

**Example:**
- Stock at $100
- Buy 1 put K=$90 (IV = 25%)
- Sell 2 calls K=$100 (IV = 20%)
- Buy 1 call K=$110 (IV = 18%)

**Position characteristics:**
- Delta-neutral (approximately)
- Limited risk (max loss = net debit)
- Profits if realized vol is low (stock stays near middle)
- **Skew exposure:** Short the wings (high IV), long the body (low IV)

**When to use:**
- Believe smile is too pronounced (wings too expensive)
- Expect stock to stay in range
- Volatility will be realized mostly at-the-money

**P&L at expiry:**
```
    P&L
     ↑
     |      /‾‾\
     |     /    \
  ---+----/------\----
     |   /        \
     |__/          \___
        90  100  110  Strike
```

Maximum profit if stock exactly at $100 at expiry.

### 2. Risk Reversal (Collar)

**Directional skew bet:**

**Structure:**
- Buy OTM call
- Sell OTM put (same distance from ATM)

**Example:**
- Stock at $100
- Buy call K=$110 (IV = 18%)
- Sell put K=$90 (IV = 25%)

**Position characteristics:**
- Positive delta (bullish bias)
- Skew exposure: Short the steep part (put), long the flat part (call)
- **Zero cost or small credit** (put premium > call premium due to skew)

**When to use:**
- Believe skew will flatten
- Bullish on stock (positive delta is feature, not bug)
- Puts are overpriced relative to calls

**Skew bet:**
- If skew flattens (put IV drops, call IV rises) → profit
- If skew steepens (put IV rises, call IV drops) → loss

### 3. Call Spread vs. Put Spread Arbitrage

**Relative value between call spreads and put spreads:**

**Structure:**
- Buy call spread (buy low strike call, sell high strike call)
- Sell put spread (sell low strike put, buy high strike put)

**Example:**
- Buy $100-110 call spread
- Sell $90-100 put spread

**Position characteristics:**
- Delta-neutral (if strikes chosen appropriately)
- Profits from skew mispricing
- Put spread expensive → sell it
- Call spread cheap → buy it

**When to use:**
- Put-call parity violations due to skew
- Statistical arbitrage

### 4. Skew Straddle/Strangle

**Modified straddle exploiting skew:**

**Structure:**
- Instead of buying ATM straddle (call + put same strike)
- Buy OTM put (expensive, high IV)
- Sell OTM call (cheap, low IV)
- Approximately delta-neutral

**When to use:**
- Capture skew premium
- Neutral to slightly bearish
- Collect from expensive puts, pay less for calls

### 5. Vertical Spread Compression

**Trade relative richness within same side:**

**Structure:**
- Within puts: Sell near-ATM put, buy far-OTM put
- The spread in IV between them may be too wide

**Example:**
- Stock at $100
- Sell put K=$95 (IV = 23%)
- Buy put K=$85 (IV = 28%)
- Skew says $85 put too expensive relative to $95 put

**When to use:**
- Skew is too steep even within one wing
- Believe spread will compress

---

## Measuring Skew

**How to quantify skew:**

### 1. 25-Delta Risk Reversal

**Market standard:**

$$
\text{25Δ RR} = \text{IV}_{25\Delta \text{ call}} - \text{IV}_{25\Delta \text{ put}}
$$

**What it measures:**
- Difference in IV between 25-delta call and put
- Positive value → puts more expensive (typical equity skew)
- More negative → steeper skew

**Example:**
- 25Δ put IV = 25%
- 25Δ call IV = 18%  
- RR = 18% - 25% = -7%
- Steep skew (typical equities)

### 2. 25-Delta Butterfly

**Market standard for smile:**

$$
\text{25Δ BF} = \frac{\text{IV}_{25\Delta \text{ call}} + \text{IV}_{25\Delta \text{ put}}}{2} - \text{IV}_{\text{ATM}}
$$

**What it measures:**
- How elevated the wings are vs. the body
- Higher value → more pronounced smile

### 3. Skew Slope

**Simple measure:**

$$
\text{Skew Slope} = \frac{\text{IV}_{90\% \text{ strike}} - \text{IV}_{110\% \text{ strike}}}{20\%}
$$

**Normalized by moneyness.**

### 4. At-The-Money vs. Out-of-The-Money Spread

$$
\text{Skew Spread} = \text{IV}_{\text{OTM put}} - \text{IV}_{\text{ATM}}
$$

**Direct measure of downside protection premium.**

---

## The P&L Sources

**Your P&L from skew trading comes from:**

### 1. Skew Change (Primary)

$$
\text{Skew P\&L} = \sum_i \text{Vega}_i \times \Delta \text{IV}_i
$$

**In plain English:**
- Each option position has vega at its strike
- IV at each strike can change independently
- Your P&L depends on relative IV changes

**Example (Butterfly):**
- Long wings (high IV strikes): Vega × (-ΔIV) if wings compress
- Short body (low IV strike): Vega × (+ΔIV) if body expands  
- Net: Profit if smile flattens

### 2. Realized Volatility vs. Implied (Secondary)

**Still have gamma exposure:**
- Multiple option positions → net gamma
- Stock moves → rebalancing P&L
- Similar to gamma scalping but with skew bias

### 3. Time Decay (Theta)

**Net theta depends on structure:**
- Butterflies: usually positive theta (short ATM, long wings)
- Risk reversals: depends on specifics
- Must manage this

### 4. Vega Changes (If Not Neutral)

**Overall IV level changes:**
- If not vega-neutral, exposed to parallel shifts
- Separate from skew changes

**Complete P&L:**

$$
\delta \Pi \approx \sum_i \text{Vega}_i \cdot \delta \text{IV}_i + \frac{1}{2}\Gamma(\delta S)^2 - \theta \, \delta t
$$

**Primary bet:** The $\sum_i \text{Vega}_i \cdot \delta \text{IV}_i$ term where IVs at different strikes change differently.

---

## Concrete Example: Trading a Steep Skew

**Setup:**

**Stock:** Tech company at $100
**Your analysis:**
- Current skew is historically steep
- OTM put IV = 30%
- ATM IV = 22%
- OTM call IV = 18%
- **Skew spread: 30% - 22% = 8%** (vs. historical average of 5%)

**Your view:** "Skew will normalize (flatten) toward 5% spread"

**The Trade: Butterfly Spread**

**Positions:**
1. Buy 10 OTM puts K=$90 at IV=30%
   - Cost: $2.50 per contract
   - Vega: 0.15 per contract
   - Total cost: $2,500

2. Sell 20 ATM calls K=$100 at IV=22%
   - Receive: $4.00 per contract
   - Vega: -0.25 per contract (short)
   - Total receive: $8,000

3. Buy 10 OTM calls K=$110 at IV=18%
   - Cost: $1.50 per contract
   - Vega: 0.15 per contract
   - Total cost: $1,500

**Net cost:** $2,500 - $8,000 + $1,500 = **-$4,000** (credit!)

**Delta hedge:** Position is approximately delta-neutral initially

**Scenario 1: Skew Normalizes (You're Right!)**

After 30 days:
- Stock still at $100 (no movement)
- Skew flattens toward historical average
- OTM put IV: 30% → 27% (-3%)
- ATM IV: 22% → 22% (unchanged)
- OTM call IV: 18% → 20% (+2%)

**Your P&L:**
- **Wing puts:** 10 × 0.15 × (-3%) = -0.45 per share = -$450
- **ATM calls:** 20 × (-0.25) × 0 = 0
- **Wing calls:** 10 × 0.15 × (+2%) = +0.30 per share = +$300
- **Net from skew change:** -$450 + $300 = **-$150** (small loss from skew)

**But also:**
- **Theta earned:** Positive (short ATM, long wings) ≈ +$600
- **Gamma P&L:** Small (stock didn't move) ≈ $0
- **Total P&L:** -$150 + $600 = **+$450**

Plus you initially collected $4,000, so total profit!

**Scenario 2: Skew Steepens (You're Wrong)**

After 30 days:
- Stock still at $100
- Skew gets even steeper (crisis fear)
- OTM put IV: 30% → 35% (+5%)
- ATM IV: 22% → 23% (+1%)
- OTM call IV: 18% → 17% (-1%)

**Your P&L:**
- **Wing puts:** 10 × 0.15 × (+5%) = +0.75 per share = +$750
- **ATM calls:** 20 × (-0.25) × (+1%) = -0.05 per share × 20 = -$500
- **Wing calls:** 10 × 0.15 × (-1%) = -0.15 per share = -$150
- **Net from skew change:** +$750 - $500 - $150 = **+$100**

Wait, you made money? That's because wings moved more than body!

**But:**
- **Theta earned:** +$600
- **Total:** +$100 + $600 = **+$700**

Actually still profitable due to theta! (This shows butterflies can be complex.)

---

## Smile/Skew Trading vs. Other Strategies

| Strategy | What You Trade | Primary Exposure | Need Multiple Strikes? |
|----------|---------------|------------------|----------------------|
| **Delta Hedging** | Nothing (risk mgmt) | None | No |
| **Gamma Scalping** | Realized vol (level) | Gamma | No (single ATM) |
| **Vega Trading** | Implied vol (level) | Vega | No (single strike) |
| **Smile/Skew Trading** | Implied vol (shape) | Relative vega | **YES (multiple strikes)** |
| **Dispersion** | Correlation | Multi-asset | YES (many assets) |
| **Variance Swaps** | Realized variance | Pure variance | No (single contract) |

### Key Differences

**Smile/Skew vs. Vega Trading:**

| Aspect | Vega Trading | Smile/Skew Trading |
|--------|-------------|-------------------|
| **What you trade** | IV level (all strikes move together) | IV shape (strikes move independently) |
| **Position** | Single strike (typically ATM) | Multiple strikes |
| **Hedging** | Delta hedge | Delta hedge + often vega-neutral |
| **Exposure** | Parallel shift in IV | Twist/curve in IV |
| **Example bet** | "IV will go from 20% to 25%" | "OTM puts will cheapen relative to ATM" |

**Smile/Skew vs. Gamma Scalping:**

| Aspect | Gamma Scalping | Smile/Skew Trading |
|--------|---------------|-------------------|
| **Profit source** | Realized volatility | Implied volatility shape |
| **What matters** | How much stock moves | Relative pricing across strikes |
| **Hedging** | Delta only | Delta + often vega |
| **Time horizon** | Hold to expiry (weeks-months) | Can be shorter (days-weeks) |

---

## Why Smile/Skew Trading Exists

**Why do opportunities persist?**

### 1. Structural Demand

**Persistent forces:**
- Portfolio insurance (demand for puts)
- Covered call writing (supply of calls)
- Corporate hedging
- Creates sustained skew

### 2. Behavioral Biases

**Market psychology:**
- Fear is stronger than greed (put demand)
- Crash fear persists (post-1987)
- Recency bias
- Loss aversion

### 3. Model Limitations

**Black-Scholes inadequacy:**
- Real returns aren't log-normal
- Volatility isn't constant
- Jumps exist
- Smile reflects these realities

### 4. Supply/Demand Imbalances

**Temporary dislocations:**
- Hedging flows (OpEx, rebalancing)
- Dealer positioning
- Market microstructure

### 5. Information Asymmetry

**Different market participants:**
- Some understand skew dynamics
- Others just buy/sell for hedging
- Creates opportunities for informed traders

---

## Pros and Cons

### Advantages ✓

**1. Additional dimension to trade**
- Beyond just "high vol" or "low vol"
- Can trade the curve, not just the level
- More opportunities

**2. Mean reversion**
- Skew tends to revert to historical averages
- Provides statistical edge
- Quantifiable with data

**3. Can be delta-neutral and vega-neutral**
- Pure skew exposure
- Minimal directional or level risk
- Focused bet

**4. Multiple strategies available**
- Butterflies, risk reversals, spreads
- Different risk/reward profiles
- Flexibility

**5. Structural edges**
- Persistent supply/demand imbalances
- Behavioral biases
- Market inefficiencies

**6. Lower capital requirements than dispersion**
- Single asset (not 10-50)
- More accessible than full dispersion

**7. Shorter time horizons possible**
- Skew can change in days/weeks
- Don't need to wait months
- More dynamic trading

### Disadvantages ✗

**1. Complexity**
- Must understand multi-leg options
- Greeks across strikes
- More moving parts than single-strike trades

**2. Transaction costs multiply**
- Trading multiple strikes
- Each leg has bid-ask spread
- Can erode profits

**3. Model risk**
- What's the "right" skew?
- How to define mispricing?
- Model-dependent

**4. Multiple risk factors**
- Still have gamma, theta, vega level
- Not purely skew exposure
- Complex risk management

**5. Can be wrong on direction**
- Skew can steepen when you expect flattening
- Mean reversion can take time
- Structural changes can shift "normal"

**6. Liquidity varies**
- ATM most liquid
- Wings can be illiquid
- Wider spreads on OTM

**7. Requires sophistication**
- Not beginner-friendly
- Need advanced options knowledge
- Risk management crucial

**8. Gamma can dominate**
- If stock moves a lot, gamma P&L > skew P&L
- Your skew bet becomes secondary
- Hard to isolate pure skew

---

## When Smile/Skew Trading Works Best

### For "Short Skew" (Skew Flattening Bets)

**Favorable conditions:**
- **Historically steep skew** (high percentile)
- **Post-crisis environment** (fear elevated)
- **VIX elevated but declining**
- **Put IV elevated relative to calls**
- **Strong trend or low realized vol**

**Example trades:**
- Butterflies (short wings, long body)
- Long risk reversals (if also bullish)

**Markets:**
- Equities after panic
- Indices post-crash
- Individual stocks after earnings fear

### For "Long Skew" (Skew Steepening Bets)

**Favorable conditions:**
- **Historically flat skew** (low percentile)
- **Complacent markets** (extended rally)
- **VIX low and grinding lower**
- **Put IV cheap relative to calls**
- **Building fragility**

**Example trades:**
- Reverse butterflies
- Short risk reversals (also hedges downside)

**Markets:**
- Equities in late bull market
- Before earnings or events
- When protection is cheap

### For Relative Value

**Favorable conditions:**
- Clear mispricing between strikes
- Mean reversion expected
- Liquid markets (tight spreads)
- Statistical edge identified

**Example trades:**
- Calendar spreads across skew
- Vertical spread arb
- Cross-strike relative value

---

## Measuring Success: Skew P&L Attribution

**How to know if you made money from skew vs. other factors:**

### P&L Decomposition

$$
\text{Total P\&L} = \underbrace{\text{Skew P\&L}}_{\text{your bet}} + \underbrace{\text{Parallel Vega P\&L}}_{\text{level change}} + \underbrace{\text{Gamma P\&L}}_{\text{realized vol}} + \underbrace{\text{Theta P\&L}}_{\text{time decay}}
$$

**Isolating skew P&L:**

1. **Mark IVs at each strike** at entry and exit
2. **Calculate parallel shift:** Average IV change across strikes
3. **Calculate skew change:** IV changes relative to average
4. **Attribute P&L:**
   - Parallel: $\sum \text{Vega}_i \times \text{Average IV change}$
   - Skew: $\sum \text{Vega}_i \times (\Delta \text{IV}_i - \text{Average IV change})$

**Example:**
- Entry: Put IV=30%, ATM IV=22%, Call IV=18%
- Exit: Put IV=32%, ATM IV=25%, Call IV=23%
- **Parallel shift:** Average increase = +3%
- **Skew changes:** Put: +2%-3%=-1%, ATM: +3%-3%=0%, Call: +5%-3%=+2%
- Skew flattened (call caught up)!

---

## Advanced: Skew Dynamics

**How skew changes over time:**

### Sticky Strike vs. Sticky Delta

**Two models for skew behavior:**

**Sticky Strike:**
- IV at each fixed strike stays constant
- As stock moves, new strikes become ATM
- Skew curve shifts with spot

**Sticky Delta:**
- IV at each delta level stays constant
- 25-delta put always has same IV
- Skew curve moves with spot

**Reality:** Somewhere in between, market-dependent

### Term Structure of Skew

**Skew varies by maturity:**
- Front-month: often steeper
- Back-month: often flatter
- Can trade term structure of skew

**Example structure:**
- 1-month skew: 8% spread
- 3-month skew: 6% spread
- 6-month skew: 5% spread

**Trade:** Calendar spread exploiting term structure differences

---

## Real-World Examples

### Example 1: Post-Earnings Skew Crush

**Before earnings:**
- Implied volatility elevated across all strikes
- Skew steep (fear of downside surprise)

**After earnings (stock moves 5%):**
- IV collapses across all strikes
- Skew normalizes
- Butterfly profits from both IV decline and skew normalization

### Example 2: 2008 Financial Crisis

**Pre-crisis:**
- Equity skew moderate
- OTM puts relatively cheap

**During crisis:**
- Skew steepened dramatically
- Put IV exploded
- Long skew positions (long OTM puts) highly profitable

**Post-crisis:**
- Skew remained elevated for years
- "New normal" for equity skew
- Structural shift

### Example 3: GameStop Short Squeeze (Jan 2021)

**During squeeze:**
- Call IV exploded (everyone wanted calls)
- Put IV elevated but less so
- **Reverse skew:** Calls more expensive than puts!
- Rare opportunity

**Trade:**
- Short risk reversals (sell expensive calls, buy cheaper puts)
- Profit as skew normalized

---

## Practical Implementation

### 1. Skew Screening

**Identify opportunities:**
- Calculate current skew metrics (RR, BF)
- Compare to historical percentiles
- Flag extreme readings
- Check liquidity

**Tools:**
- Bloomberg: SKEW function
- Option analytics platforms
- Custom Python scripts

### 2. Position Construction

**Choose structure based on:**
- View (steepening vs. flattening)
- Risk appetite
- Capital available
- Liquidity constraints

**Common structures:**
- Conservative: Butterflies (limited risk)
- Aggressive: Naked skew bets
- Balanced: Risk reversals with delta hedge

### 3. Risk Management

**Monitor:**
- Skew metrics daily
- Delta drift (rebalance as needed)
- Net vega (manage level exposure)
- P&L attribution

**Limits:**
- Maximum vega per strike
- Maximum net vega (level exposure)
- Stop-loss on skew widening beyond threshold

### 4. Exit Discipline

**Exit when:**
- Skew normalizes to target
- Structural change invalidates thesis
- Better opportunities elsewhere
- Risk/reward deteriorates

---

## What to Remember

### Core Concept

**The volatility smile/skew is the pattern of implied volatilities across strikes:**

$$
\text{IV}(K) \neq \text{constant}
$$

- Black-Scholes says it should be flat
- Reality: curved (smile or skew)
- You trade the SHAPE, not just the LEVEL

### Why It Exists

**Violations of Black-Scholes assumptions:**
1. Fat tails (extreme moves more likely)
2. Stochastic volatility (vol changes)
3. Jumps (discrete price moves)
4. Leverage effect (price-vol correlation)
5. Supply/demand (structural hedging demand)

### Two Main Patterns

**Equity Skew:**
- Downward sloping (OTM puts > ATM > OTM calls)
- Crash fear premium
- Most common in equities/indices

**FX Smile:**
- U-shaped (both wings elevated)
- Fat tails on both sides
- Symmetric or asymmetric

### Common Strategies

**1. Butterflies:**
- Trade smile richness/cheapness
- Long wings + short body or vice versa
- Limited risk

**2. Risk Reversals:**
- Trade skew slope
- Long call + short put or vice versa
- Directional bias

**3. Spread Arb:**
- Relative value within one wing
- Exploit steep skew within puts or calls

### Measuring Skew

**Market standards:**
- **25Δ Risk Reversal:** Call IV - Put IV
- **25Δ Butterfly:** (Call IV + Put IV)/2 - ATM IV
- **Skew spread:** OTM put IV - ATM IV

### Comparison to Other Strategies

| What You Trade | Strategy |
|---------------|----------|
| Volatility **level** | Vega trading, gamma scalping |
| Volatility **shape** | Smile/skew trading |
| Volatility **term structure** | Calendar spreads |
| **Multi-asset** correlation | Dispersion trading |

**All build on delta hedging foundation!**

### Success Factors

**What you need:**
1. **Statistical edge:** Historical analysis of skew
2. **Market view:** Will skew steepen or flatten?
3. **Execution:** Manage transaction costs
4. **Risk management:** Multiple Greeks to monitor
5. **Patience:** Mean reversion takes time

### The Deep Insight

**Smile/skew trading reveals:**
- Markets are smarter than Black-Scholes
- Risk is multidimensional (not just "high" or "low" vol)
- Strike matters (not all options are created equal)
- Shape contains information (market's view of tail risk)

**The pattern reflects:**
- Collective market fears (crash protection)
- Real return distribution (fat tails)
- Structural supply/demand (portfolio insurance)

### Your Complete Toolkit Now

**Seven strategies, all built on delta hedging:**

1. **Delta Hedging** → Risk management
2. **Gamma Scalping** → Realized vol (level)
3. **Vega Trading** → Implied vol (level)
4. **Smile/Skew Trading** → Implied vol (shape) ✓
5. **Dispersion Trading** → Multi-asset correlation
6. **Convertible Arb** → Multi-factor
7. **Variance Swaps** → Pure realized variance

**Each adds a dimension:**
- Level (gamma, vega)
- Shape (smile/skew) ← New!
- Time (calendar spreads - next?)
- Assets (dispersion)
- Factors (convertibles)

### Practical Wisdom

- **Skew mean-reverts** but slowly
- **Extreme readings** are opportunities
- **Transaction costs** matter (multiple legs)
- **Gamma can dominate** your skew bet
- **Liquidity varies** across strikes
- **Model risk** is significant

### Final Thought

**Smile/skew trading is about understanding that:**

"Not all volatility is created equal. The market pays different prices for different strikes because risk is multidimensional. Trade the curve, not just the level."

**This is sophisticated volatility trading:**
- Beyond single-strike bets
- Exploiting rich/cheap relationships
- Capturing structural inefficiencies
- But with complexity comes the need for discipline

**You're now trading the topology of the volatility surface!** 📈
