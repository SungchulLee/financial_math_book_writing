# Calendar Spreads

**Calendar spreads** (also called time spreads or horizontal spreads) are strategies where you profit from differences in implied volatility between different expiration dates by simultaneously buying and selling options at the same strike but different maturities.

---

## The Core Insight

**The fundamental idea:**

- Options with different expiration dates trade at different implied volatilities
- Near-term options often have different IV than longer-term options
- This creates a "volatility term structure"
- You can trade the SHAPE of this term structure across time
- Profit from relative mispricing between maturities

**The key equation:**

$$
\text{IV}_{\text{front month}} \neq \text{IV}_{\text{back month}}
$$

**You're essentially betting: "The relationship between front-month and back-month volatility is mispriced."**

---

## What Is the Volatility Term Structure?

**Before understanding calendar spreads, we need to understand the term structure:**

### The Concept

**Volatility term structure** is the relationship between implied volatility and time to expiration:

Plot IV vs. Time to Maturity → creates a curve

**Three common shapes:**

**1. Upward Sloping (Contango):**
```
    IV
     ↑
  25%|         /‾‾
  20%|      _/
  15%|   _/
     |__________→ Time
     1M  3M  6M
```
- Longer-dated options have higher IV
- Most common in calm markets
- Market expects volatility to rise over time

**2. Downward Sloping (Backwardation):**
```
    IV
     ↑
  35%|‾\
  30%|  \__
  25%|     \___
     |__________→ Time
     1M  3M  6M
```
- Near-term options have higher IV
- Common during crises or before events
- Market expects current high vol to calm down

**3. Humped (Event-Driven):**
```
    IV
     ↑
  25%|   _/‾\_
  20%|  /     \
  15%|_/       \__
     |__________→ Time
     1M  3M  6M
```
- Peak at specific maturity
- Often around earnings or events
- After event, vol expected to normalize

### Real Examples

**Example 1: Normal Market (Upward Sloping)**

- Stock at $100
- 1-month ATM IV: 18%
- 3-month ATM IV: 22%
- 6-month ATM IV: 25%
- **Front month cheaper than back month**

**Example 2: Before Earnings (Humped)**

- Stock at $100
- 1-month (before earnings) IV: 40%
- 3-month (after earnings) IV: 22%
- 6-month IV: 24%
- **Front month elevated due to earnings**

**Example 3: Crisis (Inverted)**

- Stock at $100 (during market panic)
- 1-month IV: 45%
- 3-month IV: 35%
- 6-month IV: 30%
- **Front month reflecting current panic**

---

## What Is a Calendar Spread?

**A calendar spread trades the relationship between two maturities:**

### Basic Structure

**Long Calendar Spread (Most Common):**

- **Sell** near-term option (front month)
- **Buy** longer-term option (back month)
- **Same strike** (typically ATM)
- **Same type** (both calls or both puts)

**Example:**

- Stock at $100
- Sell 1-month $100 call at IV=18%
- Buy 3-month $100 call at IV=22%
- Net cost: approximately $2 per share

### Why This Structure?

**Time decay asymmetry:**

- Front month decays faster (higher theta)
- You collect theta from short front month
- You pay less theta on long back month
- Net positive theta (usually)

**Volatility exposure:**

- Net long vega (back month has more vega)
- Profit if overall IV increases
- Or if back month IV rises relative to front

**The bet:**

- "Front month will decay away while back month holds value"
- Or: "Term structure will steepen (back month IV ↑ relative to front)"

---

## The Portfolio

Your calendar spread portfolio consists of:

$$
\Pi = -V_{\text{front}}(S, t_1, \sigma_1) + V_{\text{back}}(S, t_2, \sigma_2) + \text{Delta Hedge}
$$

where:

- $V_{\text{front}}$ = Front month option (short)
- $V_{\text{back}}$ = Back month option (long)
- $t_1 < t_2$ (front expires before back)
- $\sigma_1, \sigma_2$ = IVs at each maturity

**Why this structure?**

- Short front month: collect theta, short near-term vega
- Long back month: pay less theta, long longer-term vega
- Net: Usually positive theta, net long vega
- Delta hedge: isolate term structure exposure

**What you're exposed to:**

- ✓ Term structure changes (your bet)
- ✓ Net vega (usually long)
- ✓ Gamma (positive from long back, negative from short front)
- ✗ Delta (hedged)

---

## The P&L Formula

For a calendar spread:

$$
\delta \Pi \approx \underbrace{\text{Vega}_{\text{back}} \cdot \delta\sigma_{\text{back}} - \text{Vega}_{\text{front}} \cdot \delta\sigma_{\text{front}}}_{\text{term structure changes}} + \underbrace{\theta_{\text{net}} \, \delta t}_{\text{time decay (usually positive)}} + \underbrace{\text{Gamma P\&L}}_{\text{from both legs}}
$$

**Breaking it down:**

### 1. Term Structure P&L (Your Primary Bet)

**Two components:**

**A. Relative IV changes:**

- If back month IV rises more than front → profit
- If front month IV falls more than back → profit
- **This is your term structure bet**

**B. Time passage effect:**

- As time passes, back month becomes front month
- Roll-down effect on the curve
- Can profit from curve shape even if IVs don't change

### 2. Theta P&L (Usually Positive)

$$
\theta_{\text{net}} = \theta_{\text{back}} - \theta_{\text{front}}
$$

**Typically:**

- $|\theta_{\text{front}}| > |\theta_{\text{back}}|$ (front decays faster)
- Net theta positive (collect more than you pay)
- **This is positive carry**

### 3. Gamma P&L (Complex)

**Mixed gamma:**

- Long back month: $\Gamma_{\text{back}} > 0$
- Short front month: $\Gamma_{\text{front}} < 0$
- Net gamma can be positive or negative
- Depends on specifics (strikes, time, vol)

---

## Types of Calendar Spreads

### 1. Standard Calendar (ATM)

**Structure:**

- Both options at-the-money
- Most common
- Maximum theta collection
- Neutral directional view

**Example:**

- Stock at $100
- Sell 1-month $100 call
- Buy 3-month $100 call

**Characteristics:**

- Maximum profit if stock stays at $100
- Positive theta
- Net long vega
- Delta-neutral (approximately)

### 2. Diagonal Calendar

**Structure:**

- Different strikes (not same strike)
- Front month at one strike
- Back month at different strike
- Directional bias

**Example (Bullish Diagonal):**

- Stock at $100
- Sell 1-month $100 call
- Buy 3-month $105 call

**Characteristics:**

- Directional exposure (positive delta)
- Still benefits from time decay
- Combines calendar + vertical spread

### 3. Double Calendar (Iron Calendar)

**Structure:**

- Calendar spread on calls
- Calendar spread on puts
- Same expiration pairs
- Different strikes

**Example:**

- Sell 1-month $95 put + $105 call
- Buy 3-month $95 put + $105 call

**Characteristics:**

- Defined risk
- Profit range (between strikes)
- Double theta collection
- More complex

### 4. Reverse Calendar

**Structure:**

- **Buy** front month
- **Sell** back month
- Opposite of standard calendar

**When to use:**

- Expect term structure to invert
- Before major event (earnings)
- Front month vol spike expected
- Rare trade

---

## Concrete Example: Standard Calendar Spread

**Setup:**

**Stock:** Tech company at $100

**Market conditions:**

- 1-month ATM call IV: 20% (price: $3.00)
- 3-month ATM call IV: 24% (price: $5.50)
- Term structure: upward sloping (normal)

**Your view:** 

- "Stock will stay near $100 for next month"
- "After front month expires, back month retains value"
- "Or overall volatility will increase"

**The Trade:**

**Positions:**

- Sell 10 contracts 1-month $100 calls
      - Receive: $3.00 × 10 × 100 = $3,000
      - Vega: -0.25 per contract
      - Theta: +$20 per day per contract

- Buy 10 contracts 3-month $100 calls
      - Pay: $5.50 × 10 × 100 = $5,500
      - Vega: +0.35 per contract
      - Theta: -$10 per day per contract

**Net investment:** $5,500 - $3,000 = **$2,500**

**Net Greeks:**

- Delta: ≈ 0 (approximately neutral)
- Vega: +0.35 - 0.25 = **+0.10 per contract** (net long vega)
- Theta: +$20 - $10 = **+$10 per day per contract** (positive carry)
- Net daily theta: +$100

**Scenario 1: Stock Stays at $100 (Best Case)**

After 30 days (front month expires):

- Stock still at $100
- Front month expires worthless (you keep $3,000)
- Back month now has 60 days left
- Back month value: approximately $4.20 (decayed from $5.50)

**Your P&L:**

- Front month: +$3,000 (kept premium)
- Back month: -$1,300 (mark-to-market loss: $4.20 - $5.50)
- **Net P&L: +$1,700** 

**This is positive due to:**

- Theta asymmetry (front decayed faster)
- You can now sell the back month or hold

**Scenario 2: Stock Moves to $105 (Moderate Loss)**

After 30 days:

- Stock moved from $100 to $105
- Front month now worth $5.00 (ITM, intrinsic value)
- Back month worth $7.50

**Your P&L:**

- Front month: -$2,000 (sold at $3, now worth $5)
- Back month: +$2,000 (bought at $5.50, now worth $7.50)
- **Net P&L: $0** (approximately break-even)

**Why:** Both legs gained, but front gained more (higher gamma)

**Scenario 3: Volatility Spikes (Volatility Profit)**

After 15 days (front month still alive):

- Stock still at $100
- Market event causes volatility spike
- 1-month IV: 20% → 28% (+8%)
- 3-month IV: 24% → 30% (+6%)

**Your P&L:**

- Front month: -$800 (10 × -0.25 × 8% × 100 = -$800)
- Back month: +$2,100 (10 × 0.35 × 6% × 100 = +$2,100)
- **Net P&L: +$1,300** (before time decay)

**Why:** Back month has more vega, benefits more from vol increase

**Scenario 4: Stock Crashes to $90 (Large Loss)**

After 30 days:

- Stock crashed to $90
- Front month expires worthless (good!)
- Back month value: $2.00 (deep OTM)

**Your P&L:**

- Front month: +$3,000 (kept premium)
- Back month: -$3,500 (bought at $5.50, now worth $2.00)
- **Net P&L: -$500**

**Why:** Large directional move hurt more than theta helped

**Risk profile summary:**

- **Maximum profit:** Stock at $100 at front month expiry
- **Breakeven:** Slightly above/below $100
- **Maximum loss:** Stock moves far away (limited to net debit)

---

## Calendar Spreads vs. Other Strategies

| Strategy | What You Trade | Time Dimension | Number of Expiries |
|----------|---------------|----------------|-------------------|
| **Delta Hedging** | Nothing (risk mgmt) | N/A | Any |
| **Gamma Scalping** | Realized vol (level) | Single maturity | 1 |
| **Vega Trading** | Implied vol (level) | Single maturity | 1 |
| **Smile/Skew** | IV across strikes | Single maturity | 1 |
| **Calendar Spreads** | **IV term structure** | **Multiple maturities** | **2+** |
| **Dispersion** | Correlation | Single maturity | 1 |
| **Variance Swaps** | Realized variance | Single maturity | 1 |

### Key Distinctions

**Calendar Spreads vs. Gamma Scalping:**

| Aspect | Gamma Scalping | Calendar Spread |
|--------|---------------|-----------------|
| **What matters** | How much stock moves | Term structure + stock staying in range |
| **Time decay** | Negative (pay theta) | Positive (collect theta) |
| **Profit source** | Realized volatility | Theta decay + term structure |
| **Direction** | Want movement | Want stability (near strike) |
| **Maturity** | Single expiration | Multiple expirations |

**Calendar Spreads vs. Vega Trading:**

| Aspect | Vega Trading | Calendar Spread |
|--------|-------------|-----------------|
| **IV bet** | Level will change | Relationship between maturities will change |
| **Theta** | Negative (long options) | Positive (net positive theta) |
| **Structure** | Single maturity | Two maturities |
| **Profit even if IV flat** | No | Yes (theta decay) |

**Calendar Spreads vs. Smile/Skew:**

| Aspect | Smile/Skew | Calendar Spread |
|--------|-----------|-----------------|
| **Dimension traded** | Strike (space) | Time (temporal) |
| **What varies** | IV across strikes | IV across maturities |
| **Multiple of what** | Strikes (same expiry) | Expiries (same strike) |

---

## Why Calendar Spreads Exist

**Why is the term structure non-flat?**

### 1. Mean Reversion of Volatility

**Volatility reverts to long-term average:**

- Current high vol expected to decline
- Current low vol expected to increase
- Creates term structure slope

**Example:**

- Current vol: 35% (elevated)
- Long-term average: 22%
- Market expects reversion
- → Front month: 35%, Back month: 28% (flatter)
- → Downward sloping term structure

### 2. Events and Announcements

**Known events create humps:**

- Earnings in 1 month
- Front month IV elevated (event uncertainty)
- Back month IV normal
- → Humped structure

**After event:**

- Event passes
- Front month IV collapses
- Term structure normalizes

### 3. Supply and Demand

**Hedging patterns:**

- Portfolio managers hedge near-term risk more
- Demand for front month puts
- Less demand for long-dated
- → Term structure effects

### 4. Carry and Cost of Capital

**Time value of money:**

- Longer-dated options tie up capital longer
- Premium for duration
- → Upward sloping (typically)

### 5. Uncertainty Resolution

**Information arrival:**

- Near-term: less time for new information
- Long-term: more uncertainty
- → Usually upward sloping

---

## When Calendar Spreads Work Best

### For Long Calendar (Standard)

**Favorable conditions:**

**1. Normal/upward sloping term structure**

- Front month IV relatively lower
- Back month IV higher
- Collect theta while long vega

**2. Stock near the strike (ATM)**

- Maximum theta collection
- Both options at-the-money
- Symmetrical payoff

**3. Expected stability in stock**

- Stock will stay in range
- Low realized vol expected near-term
- Front month decays without being exercised

**4. Implied vol likely to rise (or stay high)**

- Protects back month value
- Net long vega benefits
- Volatility expansion expected

**5. Before events (with care)**

- Front month after event
- Back month before next event
- Capture vol crush on front

**Example environments:**

- Calm market, upward sloping term structure
- After recent volatility spike (expect calm)
- Stock trading in range
- Before event vol crush

### For Reverse Calendar (Rare)

**Favorable conditions:**

**1. Inverted term structure**

- Front month IV higher than back
- Unusual but happens
- During crises or pre-events

**2. Expected near-term vol spike**

- Event in front month
- Back month will stay calm
- Capture front month IV expansion

**3. Crisis fading**

- Front elevated (panic)
- Back more normal (expect calm)
- Short the elevated front, long the normal back

**Example:** 

- Before earnings: front month IV = 45%, back month = 25%
- Reverse calendar profits from this

---

## Pros and Cons

### Advantages ✓

**1. Positive theta (usually)**

- Collect time decay net
- Unlike most long volatility strategies
- Positive carry trade
- **Time is on your side**

**2. Limited risk**

- Maximum loss = net debit paid
- Defined risk (unlike naked short options)
- No unlimited loss scenarios
- Sleep better at night

**3. Net long vega (usually)**

- Benefit from volatility increases
- While collecting theta
- "Best of both worlds" potential

**4. Benefits from stable prices**

- Maximum profit if stock stays at strike
- Don't need perfect prediction
- Range-bound markets are good

**5. Term structure exploitation**

- Trade a different dimension (time)
- Additional profit source beyond level/shape
- Less crowded than ATM vega trades

**6. Flexibility**

- Can adjust as market moves
- Roll front month when expires
- Convert to other structures

**7. Lower capital requirement than straddles**

- Net debit smaller than outright long options
- More efficient use of capital
- Can do larger size

**8. Natural hedge against theta**

- Unlike gamma scalping (pays theta)
- Net positive theta helps
- Reduces bleed risk

### Disadvantages ✗

**1. Limited profit potential**

- Maximum gain capped
- Not unlimited like gamma scalping
- Best case: stock at strike at expiry

**2. Complexity**

- Two expiration dates to manage
- Different greeks for each leg
- More mental overhead

**3. Sensitive to large moves**

- Stock moving far from strike hurts
- Losses if stock gaps
- Directional risk remains
- **Not truly neutral to big moves**

**4. Early assignment risk (American options)**

- Short front month can be assigned
- Complicates position
- Need to manage early exercise

**5. Multiple expiry management**

- Front expires first
- Need to decide: close, roll, or let it go
- Timing decisions required

**6. Bid-ask spreads multiply**

- Two legs = two sets of spreads
- Costs add up
- Especially for less liquid strikes

**7. Path dependent**

- When stock moves matters
- Move early vs. late very different
- Hard to analyze ex-ante

**8. Vega not purely long**

- Mixed vega exposure (long back, short front)
- If front month vol spikes more, can lose
- Complex vega dynamics

**9. Correlation between maturities**

- Term structure can invert unexpectedly
- Front and back correlated but not perfectly
- Basis risk

**10. Event risk**

- Unexpected news can blow up position
- Front month can spike if near event
- Hard to fully hedge

---

## Advanced: Calendar Spread Variations

### 1. Ratio Calendar

**Structure:**

- Unequal number of contracts
- Example: Sell 2 front month, Buy 1 back month
- More theta collection
- But more risk if stock moves

### 2. Calendar with Skew

**Combine time and strike dimensions:**

- Trade both term structure AND smile
- Example: Front month OTM, Back month ATM
- Complex but powerful

### 3. Multiple Expiry Calendars

**Butterfly in time:**

- Sell front month
- Buy middle month
- Sell far month
- Trade the curve shape itself

### 4. Earnings Calendar

**Specifically for earnings:**

- Sell front month (just after earnings)
- Buy back month (before next earnings)
- Capture earnings vol crush
- Timing is everything

### 5. Perpetual Calendar

**Rolling strategy:**

- Each month, roll the front
- Always maintain calendar structure
- Systematic theta collection
- Popular with vol funds

---

## Real-World Examples

### Example 1: Pre-Earnings Calendar

**Company earnings in 3 weeks:**

**Before earnings:**

- 1-month (includes earnings) IV: 50%
- 3-month (after earnings) IV: 28%
- Inverted structure

**Trade:** Reverse calendar

- Buy 1-month calls (high IV, event)
- Sell 3-month calls (normal IV)
- Bet: Front month IV stays high, back month stays low

**After earnings:**

- Stock moves 8% on earnings
- 1-month IV: 50% → 30% (vol crush, but you're long!)
- Actually, you profit from the initial high IV if you exit before event
- Complex timing trade

### Example 2: COVID-19 Volatility (March 2020)

**During panic:**

- Front month IV: 85% (extreme)
- 3-month IV: 55% (elevated but less)
- Inverted term structure

**Trade:** Standard long calendar (brave!)

- Sell front month (extreme IV)
- Buy back month (less extreme)
- Bet: Front month IV will collapse faster

**Result:**

- As markets stabilized, front collapsed harder
- Calendar profitable despite high overall vol

### Example 3: Low Vol Grind (2017)

**Extended low volatility:**

- Front month IV: 10%
- 3-month IV: 14%
- Normal upward slope

**Trade:** Standard calendar

- Sell front month
- Buy back month
- Collect theta in range-bound market

**Result:**

- Stocks stayed in range for months
- Theta collection + multiple rolls
- Steady returns in boring market

---

## Practical Implementation

### 1. Screening for Opportunities

**Look for:**

- Unusual term structure (steep or inverted)
- High percentile readings (extreme slopes)
- Events creating dislocations
- Stocks in defined ranges

**Metrics:**

- Front/back IV ratio
- Term structure slope
- Historical percentile
- ATR (average true range) for realized vol

### 2. Position Construction

**Choose:**

- **Strike:** ATM for standard, OTM for directional
- **Maturities:** Typically 1:2 or 1:3 ratio (1 month vs. 2-3 months)
- **Size:** Based on max loss tolerance
- **Type:** Calls vs. puts (usually equivalent for ATM)

**Standard recipe:**

- Sell 1-month ATM
- Buy 2 or 3-month ATM
- Size so max loss = 1-2% of portfolio

### 3. Management

**Monitor:**

- Stock price (relative to strike)
- Term structure changes
- Time decay progression
- Delta drift

**Adjustments:**

- If stock moves: adjust strikes or close
- If term structure normalizes: close early
- As front expiry nears: roll or close

### 4. Exit Strategies

**Exit when:**

- **Target profit:** Often 25-50% of max profit
- **Front month expiry:** Decision point
- **Stock moves too far:** Stop loss (10-20% from strike)
- **Term structure normalizes:** Profit taken
- **Better opportunity:** Redeployment

**Roll or close at front expiry:**

- **Close:** Take profit/loss, done
- **Roll:** Sell new front month, keep back month
- **Let expire:** Keep long back month only

---

## Calendar Spreads in Your Toolkit

**How calendar spreads fit with other strategies:**

### Complete the 3D Volatility View

```
Volatility Trading Dimensions:

1. LEVEL (High vs. Low)
   ├── Gamma Scalping (realized)
   ├── Vega Trading (implied)
   └── Variance Swaps (pure variance)

2. SHAPE (Across Strikes)
   └── Smile/Skew Trading

3. TIME (Term Structure) ← Calendar Spreads!
   └── Calendar Spreads

4. ASSETS (Correlation)
   └── Dispersion Trading

5. FACTORS (Multiple)
   └── Convertible Arb
```

**Calendar spreads complete the volatility surface trading:**

- Level: Vega trading
- Shape: Smile/skew
- Time: Calendar spreads
- **Now you can trade the entire 3D surface!**

---

## What to Remember

### Core Concept

**Calendar spreads trade the term structure of implied volatility:**

$$
\text{Profit from: } \text{IV}_{\text{back}} \text{ vs. } \text{IV}_{\text{front}} \text{ relationship}
$$

- Sell front month (collect theta fast)
- Buy back month (pay theta slow)
- Net: Usually positive theta + long vega

### The Structure

**Standard (long) calendar:**

- Short front expiration
- Long back expiration
- Same strike (usually ATM)
- Same type (calls or puts)

**Goal:** Collect theta asymmetry + term structure normalization

### Why It Works

**Time decay asymmetry:**

- Front month decays faster (more theta per day)
- Back month decays slower
- Collect more than you pay

**Term structure opportunities:**

- Mean reversion
- Event-driven dislocations
- Supply/demand imbalances

### Maximum Profit

**Best case:**

- Stock stays exactly at strike
- Front month expires worthless (keep premium)
- Back month retains value
- **Profit = Front premium - Back decay**

### Risk Profile

**Characteristics:**

- Limited loss (max = net debit)
- Limited profit (capped)
- Benefits from stability
- Hurt by large moves
- Positive theta (usually)
- Net long vega (usually)

### Comparison to Core Strategies

| Theta | Vega | Best When |
|-------|------|-----------|
| **Gamma Scalping:** Negative | Long | Stock moves a lot |
| **Vega Trading:** Negative | Long | IV increases |
| **Calendar Spread:** **Positive** | Long | **Stock stable + IV rises** |

**Calendar spreads are unique: positive theta + long vega!**

### The 3D Volatility Surface

**Your complete toolkit now:**

| Dimension | Strategy |
|-----------|----------|
| **Vol Level** | Gamma/Vega/Variance |
| **Vol Shape** | Smile/Skew |
| **Vol Time** | **Calendars** ✓ |

**You can now trade:**

- "Vol is too high/low" → Vega/Gamma
- "Skew is too steep/flat" → Smile/Skew
- "Term structure is too steep/flat" → Calendars

**All three dimensions covered!**

### Success Factors

**What you need:**

1. **View on term structure:** Will it steepen/flatten?
2. **Stock range-bound:** Best if stays near strike
3. **Time decay patience:** Let theta work for you
4. **Event awareness:** Know when front expires vs. events
5. **Exit discipline:** Don't get greedy

### The Deep Insight

**Calendar spreads reveal:**

- Time is a tradeable dimension
- Not all maturities priced consistently
- Theta can be your friend (not just enemy)
- Volatility has a temporal structure

**The pattern reflects:**

- Expected mean reversion
- Event timing
- Uncertainty resolution over time
- Market views on future volatility path

### Your Complete Arsenal Now

**Eight strategies, one foundation:**

1. **Delta Hedging** → Foundation
2. **Gamma Scalping** → Level (realized)
3. **Vega Trading** → Level (implied)
4. **Smile/Skew** → Shape (strikes)
5. **Calendar Spreads** → **Time (maturities)** ✓ New!
6. **Dispersion** → Assets (correlation)
7. **Convertible Arb** → Multi-factor
8. **Variance Swaps** → Pure variance

**Progressive complexity:**

- Dimension 1: Level (vol high/low)
- Dimension 2: Shape (skew)
- Dimension 3: **Time (term structure)** ✓
- Multi-dimensional: Dispersion, Convertibles

### Practical Wisdom

- **Theta is your friend** in calendars (rare!)
- **Range-bound stocks** are ideal
- **Term structure mean-reverts** but slowly
- **Event timing** is crucial
- **Front month management** needs attention
- **Don't chase last dollar** (exit at 25-50% max profit)

### Final Thought

**Calendar spreads show that:**

"Time is not just a cost (theta) but also an opportunity. Different maturities trade at different IVs, and this relationship can be exploited. You can collect theta while maintaining vol exposure—a unique combination."

**This completes your volatility trading education:**

- **Level:** ✓ (Gamma, Vega, Variance)
- **Shape:** ✓ (Smile/Skew)
- **Time:** ✓ (Calendars)
- **Assets:** ✓ (Dispersion)
- **Factors:** ✓ (Convertibles)

**You now have mastery over the entire volatility surface—level, shape, time, and beyond!** 🎯📊⏰
