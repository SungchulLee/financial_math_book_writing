# Calendar Spread Carry

**Calendar spread carry** involves simultaneously buying one futures contract month and selling another month of the same commodity to profit from changes in the price differential (spread) between the two contracts, capturing the carry (cost or benefit of holding the spread) while being market-neutral to absolute price movements.

---

## The Core Insight

**The fundamental idea:**

- Futures curves have shape (contango or backwardation)
- The spread between months changes predictably
- Trade the spread, not the absolute price
- Market-neutral to direction (hedged position)
- Profit from curve shape changes
- Lower risk than outright futures positions

**The key equation:**

$$
\text{Calendar Spread} = F_{\text{near}} - F_{\text{far}}
$$

Where:
- $F_{\text{near}}$ = Price of nearer expiration contract
- $F_{\text{far}}$ = Price of farther expiration contract

**The carry component:**

$$
\text{Carry} = \text{Interest} + \text{Storage} - \text{Convenience Yield}
$$

**You're essentially betting: "I know how the spread between two contract months will change, regardless of whether prices go up or down."**

---

## What Are Calendar Spreads?

**Before trading calendar spreads, understand what you're actually trading:**

### Calendar Spread Defined

**Definition:** A calendar spread (also called time spread or horizontal spread) is a position where you simultaneously hold opposite positions in two different expiration months of the same futures contract.

**The two basic positions:**

**Bull Spread (Buy the Spread):**

$$
\text{Long Near Month} + \text{Short Far Month}
$$

- Profit if spread widens (becomes more positive/less negative)
- Example: Long March, Short June
- Bet: March will gain relative to June

**Bear Spread (Sell the Spread):**

$$
\text{Short Near Month} + \text{Long Far Month}
$$

- Profit if spread narrows (becomes more negative/less positive)
- Example: Short March, Long June
- Bet: June will gain relative to March

### Simple Example: Crude Oil Calendar Spread

**Setup:**

**March:** WTI crude trading at $75/barrel
**June:** WTI crude trading at $78/barrel
**Spread:** March - June = $75 - $78 = **-$3** (contango)

**Trade: Buy the spread (long March, short June)**

- Long 1 March contract at $75
- Short 1 June contract at $78
- Spread: -$3
- Capital: ~$8,000 margin (reduced for spread)

**Outcome (one month later):**

**Scenario A: Both prices rise**
- March: $75 → $80 (up $5)
- June: $78 → $82 (up $4)
- Spread: -$3 → -$2 (widened by $1)

**P&L:**
- March (long): +$5 × 1,000 = +$5,000
- June (short): -$4 × 1,000 = -$4,000
- **Net: +$1,000 (spread widened)** ✓

**Scenario B: Both prices fall**
- March: $75 → $70 (down $5)
- June: $78 → $74 (down $4)
- Spread: -$3 → -$4 (narrowed by $1)

**P&L:**
- March (long): -$5 × 1,000 = -$5,000
- June (short): +$4 × 1,000 = +$4,000
- **Net: -$1,000 (spread narrowed)** ✗

**Notice:** Scenario A made money despite both legs moving. The spread change is what matters, not the absolute price direction!

### Why Calendar Spreads Exist

**The spread reflects:**

1. **Cost of carry:**
   - Storage costs
   - Financing costs
   - Insurance

2. **Convenience yield:**
   - Value of immediate possession
   - Production flexibility
   - Stockout insurance

3. **Supply/demand imbalances:**
   - Near-term shortage
   - Future oversupply expectations
   - Seasonal patterns

4. **Roll yield dynamics:**
   - Passive index flows
   - Hedger activity
   - Market structure

**The spread equation:**

$$
\text{Spread} = S \cdot (e^{(r+u-y)(T_2-T_1)} - 1)
$$

Approximately:

$$
\text{Spread} \approx S \cdot (r + u - y) \cdot (T_2 - T_1)
$$

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/calendar_spread_carry.png?raw=true" alt="calendar_spread_carry" width="700">
</p>
**Figure 1:** Calendar spread P&L diagram showing how profits depend on spread widening or narrowing, not on absolute price direction. Both contracts can rise or fall, but only the spread change determines profit or loss.

---

## Economic Interpretation: Why Spreads Change

**Beyond the mechanical definition, understanding the economic drivers:**

### The Theory of Storage

**Full carry market:**

When storage is ample and commodities abundant:

$$
F_{\text{far}} - F_{\text{near}} = \text{Storage Cost} + \text{Financing Cost}
$$

**Example (corn with ample storage):**
- Near month: $4.50/bu
- Storage: $0.05/bu per month
- Financing: $4.50 × 0.05/12 = $0.019/bu per month
- **Expected 1-month spread: -$0.069/bu**
- Far month should trade at: $4.50 + $0.069 = $4.569

**Inverse carry market:**

When storage is tight or supply constrained:

$$
F_{\text{near}} > F_{\text{far}} + \text{Full Carry}
$$

**Convenience yield exceeds carry costs:**

- Immediate delivery valuable
- Stockout risk high
- **Backwardation (positive spread)**

### Inventory Dynamics

**High inventory → Contango → Negative spread:**

$$
\text{High Inventory} \implies \text{Low } y \implies F_{\text{far}} > F_{\text{near}}
$$

**Low inventory → Backwardation → Positive spread:**

$$
\text{Low Inventory} \implies \text{High } y \implies F_{\text{near}} > F_{\text{far}}
$$

**Example: Crude oil inventories**

**Normal (60-day supply):**
- March-June spread: -$2.00 (contango)
- Storage costs justify premium

**Tight (30-day supply):**
- March-June spread: +$3.00 (backwardation)
- Immediate need premium dominates

**The relationship is empirically strong:**

$$
\text{Spread} = \alpha + \beta \cdot \text{Inventory} + \epsilon
$$

With $\beta < 0$ typically (higher inventory → wider contango)

### Seasonal Patterns

**Agricultural commodities:**

**Harvest period:**
- Near month: Abundant supply
- Far month: Storage costs
- **Spread: Most negative (steepest contango)**

**Pre-harvest:**
- Near month: Scarce (old crop depleting)
- Far month: New crop coming
- **Spread: Less negative or positive**

**Example: Corn (December - March spread)**

| Date | Dec-Mar Spread | Phase | Driver |
|------|---------------|-------|--------|
| August | -$0.15 | Pre-harvest | Old crop scarce |
| October | -$0.50 | Harvest | New crop abundant |
| December | -$0.35 | Post-harvest | Storage costs |
| February | -$0.25 | Mid-storage | Inventory declining |

**Trading strategy:** 
- Short spread in August (expect widening to October)
- Long spread in October (expect narrowing through spring)

### Natural Gas: Extreme Seasonality

**Summer (injection season):**
- Near month: Low demand
- Winter months: Expected high demand
- **Spread: Steep contango (winter premium)**

**Winter (withdrawal season):**
- Near month: High demand NOW
- Summer months: Low demand later
- **Spread: Backwardation (immediate premium)**

**Example: November - January spread**

**September:** Planning for winter
- November: $4.00
- January: $5.00
- Spread: -$1.00 (winter premium)

**November:** In withdrawal season
- November: $5.50
- January: $5.20
- Spread: +$0.30 (immediate need premium)

**Spread moved from -$1.00 to +$0.30 = +$1.30 widening!**

### The Convergence Property

**Critical feature of calendar spreads:**

$$
\lim_{T_1 \to T_2} \text{Spread} = 0
$$

**As contracts approach each other:**
- Time difference → 0
- Carry period → 0
- **Spread must converge to zero**

**Example:**

**3 months apart:**
- March at $75, June at $78
- Spread: -$3

**1 month apart:**
- May at $76, June at $77
- Spread: -$1 (converged)

**Same month:**
- June at $77, June at $77
- Spread: $0 (fully converged)

**This convergence is NOT guaranteed to be linear or smooth, but the endpoint is certain.**

### Why This Perspective Matters

**Understanding spread economics helps you:**

1. **Predict spread movements:**
   - Inventory reports → Storage theory
   - Seasonal calendar → Patterns
   - Supply disruptions → Immediate premium

2. **Identify value:**
   - Spread too wide vs. carry costs → Sell spread
   - Spread too narrow vs. historical → Buy spread
   - **Statistical arbitrage opportunities**

3. **Manage risk:**
   - Spread trades have lower volatility than outrights
   - Directional risk largely hedged
   - **Reduced margin requirements**

4. **Capture carry:**
   - Positive carry spreads (collect over time)
   - Negative carry spreads (pay over time)
   - **Time can be friend or enemy**

**Professional traders say: "Spreads are the smart money trade - you're not betting on the market, you're betting on the market structure."**

---

## Key Terminology

**Calendar Spread Fundamentals:**

**Calendar Spread:**

$$
\text{Spread} = F_1 - F_2
$$

- Difference between two contract months
- Can be positive (backwardation) or negative (contango)
- Quoted in dollars per unit (e.g., $/barrel, $/bushel)

**Bull Spread (Buy the Spread):**

$$
\text{Long } F_1 + \text{Short } F_2
$$

- Profit if $F_1$ gains relative to $F_2$
- Spread widens (becomes more positive/less negative)
- Also called "buying the spread"

**Bear Spread (Sell the Spread):**

$$
\text{Short } F_1 + \text{Long } F_2
$$

- Profit if $F_2$ gains relative to $F_1$
- Spread narrows (becomes more negative/less positive)
- Also called "selling the spread"

**Spread Notation:**

**Standard notation:** "Month1 - Month2"

Examples:
- "Mar-Jun": March minus June
- "Dec-Mar": December minus March
- Always: Near month - Far month (typically)

**Spread Position Terminology:**

**Long the spread:**
- Buy near, sell far
- Want spread to widen

**Short the spread:**
- Sell near, buy far
- Want spread to narrow

**Carry:**

**Positive carry:**

$$
\text{Spread Income} > \text{Spread Cost}
$$

- Receive net cash flow over time
- Example: Short-term interest rates < long-term
- Time works in your favor

**Negative carry:**

$$
\text{Spread Cost} > \text{Spread Income}
$$

- Pay net cash flow over time
- Example: Contango exceeds interest earned
- Time works against you

**Full Carry:**

$$
F_2 - F_1 = \text{Storage} + \text{Financing} - \text{Income}
$$

- Maximum contango justified by costs
- When storage ample and convenience yield low
- **Arbitrage bounds the spread**

**Spread Types:**

**Intra-commodity spread:**
- Same commodity, different months
- Example: March corn vs. December corn
- Most common calendar spread

**Inter-commodity spread:**
- Related commodities
- Example: Crude oil vs. Gasoline (crack spread)
- Different risk profile

**Inter-market spread:**
- Same commodity, different exchanges
- Example: WTI vs. Brent crude
- Geographic arbitrage component

**Spread Behavior:**

**Widening:**
- Spread becomes more positive or less negative
- Near gains relative to far
- $\Delta \text{Spread} > 0$

**Narrowing:**
- Spread becomes more negative or less positive
- Far gains relative to near
- $\Delta \text{Spread} < 0$

**Spread Volatility:**

$$
\sigma_{\text{spread}} < \sigma_{\text{outright}}
$$

- Spreads less volatile than outright positions
- Both legs move similarly (correlation)
- **Lower risk, lower margin**

**Correlation:**

$$
\rho(F_1, F_2) \approx 0.80 \text{ to } 0.95
$$

- High correlation between nearby months
- Spreads capture the difference
- **Natural hedge in position**

**Performance Metrics:**

**Spread P&L:**

$$
\text{P\&L} = (S_{\text{exit}} - S_{\text{entry}}) \times \text{Multiplier} \times \text{Contracts}
$$

Where $S$ = spread value

**Return on margin:**

$$
\text{Return} = \frac{\text{Spread P\&L}}{\text{Initial Margin}}
$$

- Higher than outright due to reduced margin
- Leverage effect on spread trades

**Sharpe ratio:**

$$
\text{Sharpe} = \frac{E[\text{Return}] - r_f}{\sigma_{\text{return}}}
$$

- Often higher for spreads (lower volatility)
- Better risk-adjusted returns

**Spread Strategies:**

**Convergence trade:**
- Enter wide spread
- Exit as converges to normal
- Time-based strategy

**Seasonal trade:**
- Exploit predictable patterns
- Agricultural harvest cycles
- Energy winter/summer demand

**Inventory trade:**
- Based on storage levels
- High inventory → Sell spread
- Low inventory → Buy spread

**Curve steepener/flattener:**
- Bet on curve shape change
- Steepener: Short spread (expect more contango)
- Flattener: Long spread (expect less contango)

---

## Contract Specifications: Where Calendar Spreads Work Best

**Understanding which commodities have the best spread trading opportunities:**

### Energy Commodities (High Spread Volatility)

**Crude Oil (WTI - NYMEX):**

**Typical spreads:**

| Spread | Normal Range | Extreme Range | Driver |
|--------|-------------|---------------|--------|
| 1-2 month | -$1.50 to -$0.50 | -$5 to +$3 | Storage, demand |
| 1-6 month | -$4 to -$1 | -$15 to +$5 | Carry costs, supply |
| 1-12 month | -$8 to -$2 | -$20 to +$8 | Term structure |

**Historical examples:**

**2020 COVID (extreme contango):**
- April-May spread: -$20 (!) 
- Storage full, negative prices
- **Unprecedented widening**

**2022 Russia-Ukraine (backwardation):**
- Front-back spread: +$8
- Immediate supply shortage
- **Extreme narrowing**

**Trading strategy:**

**Mean reversion:**
- If spread < -$5: Consider buying (too wide)
- If spread > +$2: Consider selling (too narrow)
- **Historical mean: -$2**

**Natural Gas (NYMEX):**

**Extreme seasonality:**

**Summer-Winter spreads:**

| Spread | Summer (Jun) | Winter (Jan) | Swing |
|--------|-------------|-------------|-------|
| Jun-Jul | -$0.20 | N/A | Low demand |
| Oct-Nov | N/A | -$1.50 | Building premium |
| Dec-Jan | N/A | +$0.50 | Withdrawal season |
| Mar-Apr | +$0.30 | N/A | End of winter |

**Typical calendar trade:**

**September:** Sell Dec-Jan spread at -$1.50
- Expecting spread to narrow as winter approaches
- Target: -$0.50 (narrowing of $1.00)
- Risk: Early cold snap widens spread further

**Gasoline (RBOB):**

**Seasonal demand:**

**Summer driving season:**
- May-Jun spread: -$0.05 (slight premium to summer)
- Jul-Aug spread: +$0.02 (summer months valuable)

**Winter:**
- Nov-Dec spread: -$0.08 (contango in low season)

### Agricultural Commodities (Harvest Patterns)

**Corn (CBOT):**

**The harvest spread:**

| Spread | Pre-Harvest (Aug) | Harvest (Nov) | Post-Harvest (Feb) |
|--------|------------------|---------------|-------------------|
| Dec-Mar | -$0.15 | -$0.45 | -$0.30 |
| Dec-May | -$0.25 | -$0.60 | -$0.40 |
| Dec-Jul | -$0.30 | -$0.70 | -$0.45 |

**Typical trade (harvest pressure):**

**August:** Sell Dec-Mar spread at -$0.15
- Expecting widening as harvest floods market
- Target: -$0.45 (November)
- Widening: $0.30 profit

**Contract:** 5,000 bushels
**Profit:** $0.30 × 5,000 = **$1,500 per spread**

**Soybeans (CBOT):**

**Similar pattern but:**
- Later harvest (September-October)
- Crush spread considerations
- Export demand impact

**Wheat (CBOT, KCBT):**

**Multiple harvests:**
- Winter wheat: June-July
- Spring wheat: August-September
- **Less pronounced seasonality than corn**

### Precious Metals (Interest Rate Driven)

**Gold (COMEX):**

**Very stable spreads:**

**Theoretical spread:**

$$
\text{Spread} = S \times r \times \Delta T
$$

**Example:**
- Spot: $2,000/oz
- Interest rate: 5%
- Time: 3 months (0.25 years)
- Expected spread: $2,000 × 0.05 × 0.25 = **-$25**

**Actual spreads (2023):**

| Spread | Theoretical | Actual | Deviation |
|--------|------------|--------|-----------|
| Feb-Apr | -$25 | -$27 | -$2 |
| Feb-Aug | -$50 | -$52 | -$2 |
| Feb-Feb+1yr | -$100 | -$105 | -$5 |

**Trading:**
- Very tight to theory
- Small arbitrage opportunities
- High correlation (>0.99)
- **Low volatility, low risk, low return**

**Silver (COMEX):**

**Similar but:**
- Higher storage costs (bulkier)
- Some industrial demand (convenience yield)
- Slightly wider spreads than gold
- More deviation from theory

### Livestock (Production Cycles)

**Live Cattle (CME):**

**Production cycle driven:**

| Spread | Normal | Driver |
|--------|--------|--------|
| Feb-Apr | -$2 to -$4 | Feeding costs |
| Apr-Aug | -$3 to -$6 | Summer grilling season |
| Aug-Dec | -$2 to -$4 | Holiday demand |

**Lean Hogs (CME):**

**Farrowing cycle:**
- Breeding schedules
- Feed costs
- Seasonal demand (summer grilling, winter holidays)

**Spreads less predictable than grains:**
- Disease outbreaks
- Trade policy (tariffs)
- Consumer preference shifts

### Spread Liquidity Considerations

**Most liquid spreads:**

1. **Crude oil:** 1-2, 1-3, 1-6 month spreads
2. **Natural gas:** 1-2 month, winter-summer
3. **Corn:** Dec-Mar, Dec-May (new crop - old crop)
4. **Gold:** All nearby spreads

**Less liquid:**

1. **Far-dated spreads:** >12 months
2. **Livestock:** Generally lower volume
3. **Softs:** Coffee, cocoa, sugar (except major producers)

**Liquidity matters:**
- Wide bid-ask spreads on illiquid
- Slippage on entry/exit
- **Stick to liquid spreads for best execution**

---

## Maximum Profit and Loss: The Spread Range

### Understanding Calendar Spread P&L

**The profit/loss equation:**

$$
\text{P\&L} = (\text{Spread}_{\text{exit}} - \text{Spread}_{\text{entry}}) \times \text{Multiplier} \times \text{Contracts}
$$

**For long spread (buy near, sell far):**
- Profit if spread widens (becomes more positive)
- Loss if spread narrows (becomes more negative)

**For short spread (sell near, buy far):**
- Profit if spread narrows (becomes more negative)
- Loss if spread widens (becomes more positive)

**Key insight: Maximum profit/loss is LIMITED compared to outrights!**

### Maximum Profit (Long Spread)

**Theoretical maximum:**

If near goes to infinity and far goes to zero:

$$
\text{Max Profit} = +\infty - (-\infty) = +\infty
$$

**But practically impossible because:**
- High correlation (0.80-0.95)
- Both contracts track same commodity
- **Spread bounded by arbitrage**

**Realistic maximum:**

**Extreme backwardation:**

$$
\text{Max Realistic Spread} \approx S \times (y_{\max} - u)
$$

**Example: Crude oil supply crisis**
- Near month: $90
- Far month (3-month): $80
- Spread: +$10 (extreme backwardation)
- Entry: -$2 (normal contango)
- **Maximum widening: $12 ($-2 to +$10)**

**On 10 contracts:**
- $12 × 1,000 barrels × 10 = **$120,000 maximum profit**

**Historical extremes:**

| Commodity | Normal Spread | Extreme Spread | Maximum Swing |
|-----------|--------------|----------------|---------------|
| Crude oil | -$2 | +$10 | $12 |
| Natural gas | -$0.50 | +$2.00 | $2.50 |
| Corn | -$0.30 | +$0.10 | $0.40 |
| Gold | -$25 | -$15 | $10 |

### Maximum Loss (Long Spread)

**Theoretical maximum:**

If near goes to zero and far stays positive:

$$
\text{Max Loss} = 0 - F_{\text{far}} = -F_{\text{far}}
$$

**But again, practically limited:**

**Extreme contango:**

$$
\text{Max Realistic Spread} \approx -S \times (r + u)_{\max}
$$

**Example: Storage glut**
- Entry: -$2 (normal)
- Storage facilities full
- Spread widens to: -$8 (extreme contango)
- **Maximum loss: $6 (spread went wrong direction)**

**On 10 contracts:**
- -$6 × 1,000 × 10 = **-$60,000 maximum loss**

**Comparison to outright position:**

**Outright long futures (same $80 oil):**
- Max gain: Unlimited (oil to $200 = $120/barrel gain)
- Max loss: -$80/barrel (oil to $0)
- **Profit range: -$80 to +$120+**

**Calendar spread (long $-2 spread):**
- Max gain: ~$12/barrel (spread to +$10)
- Max loss: ~-$6/barrel (spread to -$8)
- **Profit range: -$6 to +$12** (much narrower!)

### Real-World Example: Corn Harvest Spread

**Trade: Sell Dec-Mar spread**

**Entry (August):**
- December corn: $4.50
- March corn: $4.65
- Spread: -$0.15
- Position: Short Dec, Long Mar
- **Sell spread at -$0.15**

**Best case (November - peak harvest):**
- December: $4.20 (down $0.30)
- March: $4.55 (down $0.10)
- Spread: -$0.35 (widened by $0.20)

**P&L:**
- December (short): +$0.30 × 5,000 = +$1,500
- March (long): -$0.10 × 5,000 = -$500
- **Net: +$1,000** ✓

**Spread P&L:**
- Sold at: -$0.15
- Bought back at: -$0.35
- Difference: -$0.35 - (-$0.15) = -$0.20 (we're short, so this is profit)
- **P&L: +$0.20 × 5,000 = +$1,000** ✓

**Worst case (drought destroys crop):**
- December: $5.50 (up $1.00 - shortage!)
- March: $5.55 (up $0.90 - less impact)
- Spread: -$0.05 (narrowed by $0.10)

**P&L:**
- December (short): -$1.00 × 5,000 = -$5,000
- March (long): +$0.90 × 5,000 = +$4,500
- **Net: -$500** ✗

**Notice:**
- Best case: +$1,000 (spread widened as expected)
- Worst case: -$500 (spread narrowed)
- **Risk-reward: 2:1** (risking $500 to make $1,000)
- Much better than outright position!

### Calendar Spread Risk vs. Outright Risk

**Volatility comparison:**

**Example: Crude oil (monthly data)**

**Outright futures:**
- Monthly volatility: 8%
- On $80 oil: ±$6.40/month
- Annual volatility: ~28%

**1-3 month calendar spread:**
- Monthly volatility: 2%
- On $2 spread: ±$0.04/month
- Annual volatility: ~7%

**Risk reduction: 75%!**

**This is why spreads have lower margin requirements:**

| Position | Notional | Outright Margin | Spread Margin | Reduction |
|----------|---------|----------------|---------------|-----------|
| 1 WTI contract | $80,000 | $8,000 | $1,500 | 81% |
| 1 Corn contract | $22,500 | $2,000 | $400 | 80% |
| 1 Gold contract | $200,000 | $10,000 | $1,000 | 90% |

---

## Entry and Exit Strategies

### Entry Strategies: When to Initiate Calendar Spreads

**1. Mean Reversion Entry**

**Setup: Spread at extreme deviation from historical average**

**Historical analysis:**
- Calculate average spread for same months over 5 years
- Calculate standard deviation
- Entry: When spread > 2 standard deviations from mean

**Example: Crude oil Mar-Jun spread**

**Historical data (5 years, March):**
- Average: -$2.00
- Std dev: $0.80
- Current: -$4.00
- Z-score: (-$4.00 - (-$2.00)) / $0.80 = -2.5

**Trade:** Buy spread (long Mar, short Jun)
- Entry: -$4.00 (abnormally wide)
- Target: -$2.00 (mean)
- Profit potential: $2.00/barrel
- Stop loss: -$5.00 (if widening continues)

**2. Seasonal Entry**

**Agricultural: Pre-harvest seasonal pattern**

**Corn: Sell Dec-Mar in August**

**Historical pattern:**

| Month | Avg Dec-Mar Spread | Action |
|-------|-------------------|--------|
| July | -$0.12 | Setup |
| August | -$0.15 | **Enter short** |
| September | -$0.25 | Monitor |
| October | -$0.40 | Target reached |
| November | -$0.45 | Peak width |

**Entry criteria:**
- Date: Early August
- Spread: -$0.15 or narrower
- Inventory reports confirm adequate crop
- **Expected widening: $0.25-$0.30**

**Natural gas: Buy winter-summer in September**

**Pattern:**
- September: Winter premium large
- November-December: Premium shrinks as we enter winter
- **Spread narrows predictably**

**3. Inventory-Driven Entry**

**Monitor storage levels:**

**Crude oil (EIA data):**

**High inventory trigger (>400M barrels):**
- Indicates oversupply
- Expect contango to steepen
- **Trade:** Sell spread (short near, long far)
- Spread should widen (more negative)

**Low inventory trigger (<300M barrels):**
- Indicates tight supply
- Expect backwardation or contango flattening
- **Trade:** Buy spread (long near, short far)
- Spread should narrow (less negative/more positive)

**Example:**

**January:** Inventory at 420M barrels (high)
- Current spread: -$2.00
- Expected: Widen to -$3.50
- **Entry:** Sell Mar-Jun spread at -$2.00
- **Target:** -$3.50 (+$1.50 profit)

**4. Curve Shape Entry (Steepener/Flattener)**

**Steepener (bet curve gets steeper):**

**Setup:** Expect contango to widen
- Sell the spread (short near, long far)
- Example: Short Mar, Long Sep crude

**When to use:**
- Storage capacity increasing
- Demand expectations weakening
- **Curve too flat relative to carry costs**

**Flattener (bet curve gets flatter):**

**Setup:** Expect contango to narrow
- Buy the spread (long near, short far)
- Example: Long Mar, Short Sep crude

**When to use:**
- Inventory declining rapidly
- Demand surge expected
- **Curve too steep relative to fundamentals**

**5. Arbitrage Entry (Spread Outside Bounds)**

**Cost of carry arbitrage:**

**Setup:** Spread wider than full carry costs

**Example: Gold**

**Theoretical spread (3 months):**
- Spot: $2,000
- Interest: 5% annual
- Storage: 0.5% annual
- Time: 0.25 years
- **Fair spread:** -$2,000 × 0.055 × 0.25 = -$27.50

**Actual spread:** -$35
**Deviation:** $7.50 too wide

**Trade:** Buy spread
- Long near month at $2,000
- Short 3-month at $2,035
- Hold to convergence
- **Lock in $7.50 profit** (after costs)

### Exit Strategies: When to Close Calendar Spreads

**1. Target Profit Exit**

**Set target based on entry thesis:**

**Example: Mean reversion trade**
- Entry: -$4.00 (2.5 std dev wide)
- Target: -$2.00 (mean)
- Current: -$2.10 (near target)
- **Exit:** Close at -$2.10
- Profit: $1.90/barrel

**Don't be greedy:**
- Captured 95% of expected move
- Further reversion uncertain
- **Take the profit**

**2. Stop Loss Exit**

**Set maximum acceptable loss:**

**Example:**
- Entry: Buy spread at -$2.00
- Stop: -$3.00 (spread widens against us)
- Maximum loss: -$1.00/barrel
- If hit: **Exit immediately**

**Why stops critical:**
- Spreads can stay wide/narrow longer than expected
- Carrying costs add up
- **Preserve capital for better opportunities**

**3. Time Exit (Convergence Approaching)**

**As contracts get closer:**

**Example: Mar-Jun spread trade**

**January:** Initiated at -$3.00
**February:** Spread at -$2.00 (profit)
**Late February:** Only 1 month between contracts
- Spread must converge to near zero
- Diminishing return potential
- **Exit before convergence completes**

**4. Fundamental Exit (Thesis Invalidated)**

**Example: Seasonal corn trade**

**Entry:** Sold Dec-Mar at -$0.15 (expecting harvest widening)
**August:** Drought announced, crop failure likely
**New reality:** Supply shortage means contango will collapse
**Action:** **Exit immediately** (cover spread)
- Small loss acceptable vs. potential large loss
- Thesis broken = get out

**5. Roll Exit (Extend Position)**

**For longer-term spread views:**

**Example: Persistent contango thesis**

**Month 1:** Short Mar-Jun at -$2.00
**Late February:** Mar expiring soon
- Close Mar-Jun spread
- Open Jun-Sep spread
- Continue betting on contango structure

**6. Seasonal Exit**

**Exit before seasonal pattern reverses:**

**Example: Natural gas winter spread**

**September:** Bought Nov-Jan spread (expecting narrowing)
**November:** In withdrawal season, spread narrowed
**Late November:** Spread reached normal winter level
**Action:** **Exit** before spring transition begins
- Pattern about to reverse
- Lock in seasonal profit

### Position Management Techniques

**1. Scaling Into Spreads**

**Build position in stages:**

**Example: Crude oil spread**

**Week 1:** Spread at -$3.00
- Enter 25% of target position (2 of 8 contracts)

**Week 2:** Spread widens to -$3.50
- Add 25% more (2 contracts)
- Average entry: -$3.25

**Week 3:** Spread peaks at -$4.00
- Add final 50% (4 contracts)
- Average entry: -$3.63

**Advantage:** Better average price if spread continues moving

**Risk:** May not fill entire position if reverses early

**2. Ratio Spreads**

**Adjust ratio for different volatilities:**

**Example: Near month more volatile**

**Standard:** 1:1 ratio (1 long, 1 short)
**Adjusted:** 2:3 ratio (2 near, 3 far)
- Accounts for volatility difference
- Better delta neutrality

**3. Multiple Spread Strategies**

**Butterfly spread:**

$$
\text{Buy } F_1, \text{ Sell } 2 \times F_2, \text{ Buy } F_3
$$

**Example: Crude oil**
- Long March at $75
- Short 2× June at $78 each
- Long September at $80

**Profit if:** June underperforms both March and September

**Condor spread:**

Four legs across different months
- More complex, requires specific curve shape

---

## Best Case Scenarios: When Calendar Spreads Work Perfectly

### The Dream: Maximum Spread Movement in Your Favor

**What defines best case:**

1. Large spread movement (>$3-5 per contract)
2. Quick movement (weeks not months)
3. Low transaction costs
4. Perfect timing (enter extreme, exit at reversal)
5. **High return on low margin capital**

### Best Case #1: The COVID Storage Crunch (2020 WTI)

**The historic calendar spread opportunity:**

**Setup (March 2020):**

- **Position:** Long April WTI, Short May WTI
- **Entry:**
  - April: $30/barrel
  - May: $31/barrel
  - **Spread: -$1** (normal contango)
  - Position: Long 10 April contracts, Short 10 May contracts
  - Margin: $20,000

**The crisis:**

**Late March:** COVID lockdowns crush demand
- Storage facilities filling rapidly
- No demand for crude
- **April contract approaching expiration**

**Early April:** Storage crisis
- Cushing, OK storage 80% full
- April holders desperate to avoid delivery
- May contract unaffected (future problem)

**April 20 (expiration day):**
- April contract: **-$37/barrel** (yes, negative!)
- May contract: $20/barrel
- **Spread: -$57** (from -$1 to -$57!)

**The theoretical P&L (if held):**

**April leg:**
- Long at $30, now -$37
- Loss: -$67/barrel × 10 × 1,000 = **-$670,000** ☠️

**May leg:**
- Short at $31, now $20
- Gain: +$11/barrel × 10 × 1,000 = **+$110,000**

**Net:** -$670,000 + $110,000 = **-$560,000** (disaster!)

**But the smart trader (exited early):**

**April 15 (before meltdown):**
- April: $15/barrel
- May: $25/barrel
- Spread: -$10

**P&L:**
- April: ($15 - $30) = -$15 × 10 × 1,000 = -$150,000
- May: ($31 - $25) = +$6 × 10 × 1,000 = +$60,000
- **Net: -$90,000** (still bad, but avoided disaster)

**The opposite trade (those who saw it coming):**

**Smart short spread trade (March 15):**

**Entry:**
- Short April at $35
- Long May at $33
- **Sell spread at -$2**
- Capital: $20,000 margin

**Exit (April 10, before negative):**
- April: $18
- May: $24
- Spread: -$6

**P&L:**
- Sold spread at -$2, bought back at -$6
- Spread widened by $4 (we were short, so profit!)
- **Profit: $4 × 10 × 1,000 = $40,000**
- Return: $40,000 / $20,000 = **200%!** 🎯

**Why this was best case:**
- Unprecedented spread widening ($-2 to $-6 = $4 gain)
- Quick (1 month)
- Predictable (storage crisis visible)
- **200% return on margin**

### Best Case #2: The Natural Gas Winter Flip (2014)

**The extreme seasonal spread:**

**Setup (October 2014):**

- **Position:** Long December, Short January
- **Entry:**
  - December: $4.00/MMBtu
  - January: $4.50/MMBtu
  - **Spread: -$0.50** (winter premium)
  - Position: Long 20 December, Short 20 January
  - Margin: $30,000

**The thesis:**
- Spread too wide (normal is -$0.20)
- Once in winter, premium disappears
- December will gain relative to January

**The polar vortex:**

**Late November:** Early severe cold hits
- Withdrawal season begins early
- December demand spikes
- January premium shrinks

**Mid-December:**
- December: $4.80/MMBtu (up $0.80)
- January: $4.60/MMBtu (up $0.10)
- **Spread: +$0.20** (flipped to backwardation!)

**P&L:**

**December (long):**
- Bought $4.00, now $4.80
- Gain: +$0.80 × 20 × 10,000 = **+$160,000**

**January (short):**
- Sold $4.50, now $4.60
- Loss: -$0.10 × 20 × 10,000 = **-$20,000**

**Net P&L:**
- +$160,000 - $20,000 = **+$140,000**

**Spread P&L check:**
- Entry: -$0.50
- Exit: +$0.20
- **Change: +$0.70 widening** (we were long)
- P&L: +$0.70 × 20 × 10,000 = **+$140,000** ✓

**Return:**
- Profit: $140,000
- Margin: $30,000
- **Return: 467%!** 🚀

**Why this was best case:**
- Massive spread swing ($-0.50 to +$0.20 = $0.70)
- Weather event accelerated move
- Seasonal pattern validated
- Perfect timing (exited mid-December before reversal)
- **467% return in 2 months**

### Best Case #3: The Corn Harvest Squeeze (2012)

**The drought calendar spread:**

**Setup (June 2012):**

- **Position:** Long July, Short December
- **Entry:**
  - July (old crop): $6.00/bushel
  - December (new crop): $5.50/bushel
  - **Spread: +$0.50** (old crop premium)
  - Position: Long 50 July, Short 50 December
  - Margin: $25,000

**The drought:**

**July:** Severe drought in Corn Belt
- Old crop almost gone
- New crop failing in fields
- **July (immediate need) becomes precious**

**August:**
- July: $8.00/bushel (up $2.00)
- December: $6.50/bushel (up $1.00)
- **Spread: +$1.50** (widened by $1.00)

**P&L:**

**July (long):**
- Bought $6.00, sold $8.00
- Gain: +$2.00 × 50 × 5,000 = **+$500,000**

**December (short):**
- Sold $5.50, covered $6.50
- Loss: -$1.00 × 50 × 5,000 = **-$250,000**

**Net:** +$500,000 - $250,000 = **+$250,000**

**Return:**
- Profit: $250,000
- Margin: $25,000
- **Return: 1,000%!** 🎯💎

**Why this was best case:**
- Extreme weather event
- Old crop scarcity premium
- Spread moved massively (+$0.50 to +$1.50 = $1.00)
- **1,000% return in 2 months**

### Common Best Case Elements

**What makes calendar spread best cases work:**

1. **Extreme events:**
   - Storage crunch (2020 oil)
   - Weather disasters (2014 gas, 2012 corn)
   - Supply disruptions

2. **Spread dislocations:**
   - >3 standard deviations from mean
   - Driven by panic or euphoria
   - **Reversion opportunity**

3. **Time-sensitive:**
   - Near contract expiration pressure
   - Seasonal deadlines
   - **Urgency creates spread volatility**

4. **Leverage on margin:**
   - Low margin requirements (10-20% of outright)
   - Large notional exposure
   - **Returns: 200-1,000%+ possible**

5. **Directional hedge:**
   - Don't need to predict absolute prices
   - Only spread direction
   - **Lower risk than outrights**

**The professional insight:**

"Calendar spreads give you asymmetric risk-reward during dislocations. When the spread is at 3-sigma, you're not betting on oil going up or down—you're betting the market structure normalizes. That's a much higher probability bet, with defined risk and massive upside."

---

## Worst Case Scenarios: When Calendar Spreads Go Wrong

### The Nightmare: Spread Moves Against You Persistently

**What defines worst case:**

1. Large adverse spread movement
2. Prolonged (months of losses)
3. Fundamental shift (thesis permanently invalidated)
4. Forced exit at worst point
5. **Losses compound from carry costs**

### Worst Case #1: The Wrong Side of Storage Glut (2015-2016 Oil)

**The persistent contango deepening:**

**Setup (January 2015):**

- **Position:** Long March, Short June (buy the spread)
- **Entry:**
  - March: $48/barrel
  - June: $52/barrel
  - **Spread: -$4** (steep contango)
  - Thesis: "Spread too wide, will narrow"
  - Position: Long 20 March, Short 20 June
  - Margin: $40,000

**The disaster:**

**Global oversupply:**
- OPEC refuses production cuts
- U.S. shale production continues
- Storage builds everywhere
- **Contango keeps steepening**

**February:**
- March: $50/barrel
- June: $55/barrel
- Spread: -$5 (widened by $1!)

**The roll forced:**

**Late February:** March expiring
- Must roll to June-September
- Close March-June at -$5
- **Loss: $1 × 20 × 1,000 = -$20,000** ☠️

**Open new spread:** June-September
- June: $54
- September: $59
- **New spread: -$5** (contango persists!)

**April:**
- June: $56
- September: $62
- Spread: -$6 (widened again!)

**Forced to roll again:**
- Close June-Sep at -$6
- **Additional loss: $1 × 20 × 1,000 = -$20,000** ☠️

**The compounding nightmare:**

**Over 12 months (2015):**

| Month | Spread | Roll Loss | Cumulative |
|-------|--------|-----------|------------|
| Jan | -$4 | Entry | $0 |
| Mar | -$5 | -$20k | -$20k |
| May | -$6 | -$20k | -$40k |
| Jul | -$7 | -$20k | -$60k |
| Sep | -$7 | $0 | -$60k |
| Nov | -$6 | +$20k | -$40k |
| Dec | -$5 | +$20k | -$20k |

**Final outcome (December 2015):**

**Total losses:** -$20,000 (after 12 months!)

**Plus carry costs:**
- Margin interest: ~$3,000
- Transaction costs: ~$2,000
- **Total: -$25,000**

**Return:**
- Loss: -$25,000
- Capital tied up: $40,000 (average)
- **Return: -63% over 12 months** ☠️

**What went wrong:**

1. **Fundamental shift:** Structural oversupply, not temporary
2. **Persistence:** Contango stayed wide for years
3. **Roll costs:** Each roll locked in losses
4. **No exit discipline:** Kept hoping for reversion
5. **Thesis broken:** Should have exited after first loss

### Worst Case #2: The Corn Spread Disaster (2016)

**The record harvest spread collapse:**

**Setup (August 2016):**

- **Position:** Buy the spread (long Dec, short Mar)
- **Entry:**
  - December: $3.50/bushel
  - March: $3.65/bushel
  - **Spread: -$0.15** (expecting harvest widening)
  - Thesis: "Normal harvest will widen spread"
  - Position: Long 100 Dec, Short 100 Mar
  - Margin: $40,000

**The disaster:**

**September:** Record harvest forecast
- Yields 10% above expectations
- Storage capacity stretched
- **Contango should widen (our trade works)**

**October (harvest):**
- December: $3.30 (down $0.20)
- March: $3.50 (down $0.15)
- Spread: -$0.20 (widened $0.05 ✓)

**So far so good:** Small profit of $0.05 × 100 × 5,000 = +$5,000

**November: The reversal:**

- Unexpected: China announces massive corn purchases
- Export demand surge
- Near-term demand spikes
- **Spread flips!**

**December:**
- December: $3.60 (up $0.30!)
- March: $3.55 (up $0.05)
- **Spread: +$0.05** (flipped from -$0.15 to +$0.05!)

**P&L disaster:**

**December (long):**
- Bought $3.50, now $3.60
- Gain: +$0.10 × 100 × 5,000 = **+$50,000**

**March (short):**
- Sold $3.65, now $3.55
- Gain: +$0.10 × 100 × 5,000 = **+$50,000**

**Wait, both profitable?**

**Spread P&L:**
- Entry: -$0.15
- Current: +$0.05
- **Change: +$0.20 (widening)**
- We were long spread, so...
- **P&L: +$0.20 × 100 × 5,000 = +$100,000!** 

**Actually this is BEST case, not worst case!**

**Let me correct to actual worst case:**

### Worst Case #2 (Corrected): The Corn Spread Disaster

**Setup (same):**
- Long Dec at $3.50, Short Mar at $3.65
- Spread: -$0.15
- Thesis: Spread will widen (more negative)

**The reversal:**

**November:** China purchases
- December: $3.70 (up $0.20)
- March: $3.90 (up $0.25 - gained MORE)
- **Spread: -$0.20** (narrowed instead of widening!)

**P&L:**

**December (long):**
- Bought $3.50, now $3.70
- Gain: +$0.20 × 100 × 5,000 = **+$100,000**

**March (short):**
- Sold $3.65, now $3.90
- Loss: -$0.25 × 100 × 5,000 = **-$125,000**

**Net:** +$100,000 - $125,000 = **-$25,000** ☠️

**Spread P&L:**
- Entry: -$0.15
- Exit: -$0.20
- **Narrowed by $0.05** (wrong direction for long spread)
- Loss: -$0.05 × 100 × 5,000 = **-$25,000** ☠️

**Return:**
- Loss: -$25,000
- Margin: $40,000
- **Return: -63%** ☠️

**What went wrong:**
- Unexpected demand shift
- Spread moved opposite direction
- Held too long hoping for reversal
- Should have exited when thesis invalidated

### Worst Case #3: The Natural Gas Summer Horror (2012)

**The wrong seasonal bet:**

**Setup (April 2012):**

- **Position:** Short the spread (bet on narrowing)
- **Entry:**
  - June: $2.50/MMBtu
  - August: $2.80/MMBtu
  - **Spread: -$0.30** (summer contango)
  - Thesis: "Spread will narrow as summer progresses"
  - Position: Short 50 June, Long 50 August
  - Margin: $50,000

**The disaster:**

**May:** Surprise heat wave
- Early summer cooling demand
- Storage injections slower than expected
- **Near-term tightness increases**

**June:**
- June: $2.80 (up $0.30)
- August: $2.90 (up $0.10)
- **Spread: -$0.10** (narrowed by $0.20 ✓)

**Looks good!** +$0.20 × 50 × 10,000 = **+$100,000**

**But then:**

**Late June:** Hurricane threatens Gulf
- Production disruptions feared
- **Front month (now July) spikes**

**Must roll spread:**

**Close June-August:**
- June: $3.00
- August: $2.95
- Spread: +$0.05 (flipped to backwardation!)

**P&L on close:**
- Entry spread: -$0.30
- Exit spread: +$0.05
- **Widened by $0.35** (we were short, so loss!)
- Loss: -$0.35 × 50 × 10,000 = **-$175,000** ☠️

**Return:**
- Loss: -$175,000
- Margin: $50,000
- **Return: -350%!** ☠️
- **Account wiped out plus owe $125,000!**

**What went catastrophically wrong:**

1. **Weather event:** Unpredictable heat wave
2. **Hurricane risk:** Additional supply concern
3. **Spread flipped:** Contango → Backwardation
4. **Massive move:** $0.35 in weeks
5. **Over-leveraged:** 50 contracts too many

### Common Worst Case Themes

**Why calendar spreads blow up:**

1. **Fundamental shift:**
   - Supply/demand paradigm changes
   - Persistent, not temporary
   - **Thesis invalidated but held**

2. **Weather/geopolitical shocks:**
   - Unpredictable events
   - Spread moves violently
   - **No time to react**

3. **Roll losses compound:**
   - Wrong spread direction
   - Each roll locks in loss
   - **Death by thousand rolls**

4. **Over-leverage:**
   - Too many contracts for capital
   - Can't handle adverse moves
   - **Margin calls force exit at worst time**

5. **No exit discipline:**
   - Hope for reversion
   - Average down
   - **Small loss becomes large loss**

### Preventing Worst Cases

**Risk management for calendar spreads:**

**1. Position sizing:**

$$
\text{Max Contracts} = \frac{\text{Capital} \times 0.30}{\text{Spread Margin}}
$$

- Use only 30% of capital for spread margin
- Keep 70% buffer
- **Can handle 2-3σ adverse moves**

**2. Stop losses on spread:**

**Set based on historical volatility:**

$$
\text{Stop} = \text{Entry} \pm 2 \times \sigma_{\text{spread}}
$$

**Example:**
- Entry: -$2.00
- Spread σ: $0.50
- Stop (long spread): -$3.00 (if widens against us)
- **Exit if spread hits -$3.00**

**3. Fundamental monitoring:**

- Watch inventory reports religiously
- Weather forecasts (agricultural, nat gas)
- Supply disruptions
- **Exit if fundamentals change**

**4. Time limits:**

- Set maximum holding period
- If no progress after 50% of time → Exit
- **Don't let hope drive decisions**

**5. Never average down:**

- Spread went wrong = Wrong analysis
- Don't add to losers
- **Cut loss and reassess**

**Remember: Calendar spreads are LOWER risk than outrights, but can still destroy capital if mismanaged!**

---

## What to Remember

### Core Concept

**Calendar spreads trade the price differential between two contract months:**

$$
\text{Calendar Spread} = F_{\text{near}} - F_{\text{far}}
$$

**Two basic positions:**

**Long spread (buy the spread):**
$$
\text{Long } F_{\text{near}} + \text{Short } F_{\text{far}} \quad \rightarrow \quad \text{Profit if spread widens}
$$

**Short spread (sell the spread):**
$$
\text{Short } F_{\text{near}} + \text{Long } F_{\text{far}} \quad \rightarrow \quad \text{Profit if spread narrows}
$$

### Market Neutral Nature

**Key insight:**
- Spread trades profit from RELATIVE price movement
- Don't care if absolute prices rise or fall
- Only care about spread change
- **Direction-independent returns (mostly)**

**Example:**
- Both contracts up 10%: Can profit if spread widens
- Both contracts down 10%: Can profit if spread widens
- **Spread change matters, not price direction**

### Why Spreads Change

**Economic drivers:**

$$
\text{Spread} = S \cdot (r + u - y) \cdot \Delta T
$$

- $r$ = Interest rate (financing)
- $u$ = Storage cost
- $y$ = Convenience yield
- $\Delta T$ = Time between contracts

**High inventory → Low $y$ → Negative spread (contango)**
**Low inventory → High $y$ → Positive spread (backwardation)**

### Risk Reduction

**Compared to outright positions:**

**Volatility:**
- Outright futures: σ = 25-35% annual
- Calendar spread: σ = 5-10% annual
- **70-80% volatility reduction**

**Margin:**
- Outright: 10% of notional
- Spread: 2-3% of notional
- **70-80% margin reduction**

**Correlation effect:**
- Both legs move similarly (ρ = 0.80-0.95)
- Natural hedge in position
- **Lower risk, lower capital requirements**

### Typical Spread Ranges

**Know the normal ranges:**

| Commodity | Normal Spread | Extreme Wide | Extreme Narrow |
|-----------|--------------|--------------|----------------|
| Crude oil (1-3 mo) | -$2 to -$0.50 | -$8 | +$5 |
| Natural gas (1-2 mo) | -$0.30 to +$0.20 | -$2 | +$2 |
| Corn (Dec-Mar) | -$0.30 to -$0.15 | -$0.60 | +$0.10 |
| Gold (3-month) | -$25 to -$20 | -$35 | -$15 |

**Entry strategy:**
- Enter when spread at extremes (>2σ from mean)
- Target: Reversion to mean
- Stop: Further extreme movement

### Seasonal Patterns (Most Predictable)

**Natural gas:**
- **Summer (Apr-Oct):** Contango -$0.30 to -$1.00
- **Winter (Nov-Mar):** Backwardation +$0.20 to +$1.00
- **Pattern reliability:** 80%+
- **Trade:** Long spread in Oct, exit in Nov-Dec

**Agricultural (corn):**
- **Pre-harvest (Jul-Sep):** Moderate contango -$0.15
- **Harvest (Oct-Nov):** Steep contango -$0.45
- **Post-harvest (Dec-Mar):** Narrowing -$0.30 to -$0.20
- **Trade:** Sell spread Aug, buy back Nov

### Entry Strategies

**1. Mean reversion:**
- Entry: Spread >2σ from historical mean
- Target: Mean
- Stop: >3σ

**2. Seasonal:**
- Entry: Based on calendar (e.g., Aug for harvest trade)
- Target: Seasonal peak/trough
- Stop: Fundamental change

**3. Inventory-driven:**
- Entry: Based on storage reports
- High inventory → Sell spread
- Low inventory → Buy spread

**4. Carry arbitrage:**
- Entry: Spread outside theoretical bounds
- Target: Fair value
- Very low risk (arbitrage)

### Exit Strategies

**1. Target profit:**
- Set based on historical moves
- Exit when hit (don't be greedy)

**2. Stop loss:**
- Spread moves >1-2σ against you
- Exit immediately
- **Protect capital**

**3. Time stop:**
- Maximum holding period
- Exit if no progress
- **Avoid carry bleed**

**4. Fundamental:**
- Thesis invalidated
- Exit regardless of P&L

### Best Case Scenarios

**Maximum positive spread moves:**

**Examples:**
- 2020 COVID oil: Spread widened $4-5 in weeks (200-500% returns)
- 2014 polar vortex gas: Spread moved $0.70 (467% return)
- 2012 drought corn: Spread moved $1.00 (1,000% return)

**Common elements:**
- Extreme events (weather, supply shocks)
- Spread >3σ from mean
- Quick reversal (weeks to months)
- **High returns on low margin capital**

### Worst Case Scenarios

**Maximum adverse spread moves:**

**Examples:**
- 2015 oil persistent contango: -63% over 12 months
- 2012 gas hurricane: -350% in weeks (account wiped)
- Wrong harvest bet: -50% to -100%

**Common mistakes:**
- Fundamental shift ignored
- No stop loss
- Over-leveraged
- Averaging down
- **Hope instead of discipline**

### Position Sizing

**Conservative approach:**

$$
\text{Max Position} = \frac{\text{Capital} \times 0.30}{\text{Spread Margin}}
$$

- Use only 30% for margin
- Keep 70% buffer
- Can handle 2-3σ adverse moves
- **Never use full capital**

### Common Mistakes

1. **Not knowing historical spread range**
2. **Ignoring seasonality**
3. **Over-leveraging** (using all margin capacity)
4. **No stop losses**
5. **Fighting fundamental shifts**
6. **Averaging down on losers**
7. **Not monitoring inventory/weather data**
8. **Holding through convergence** (diminishing returns)

### Key Formulas

**Spread:**

$$
S = F_1 - F_2
$$

**Spread P&L (long spread):**

$$
\text{P\&L} = (S_{\text{exit}} - S_{\text{entry}}) \times \text{Multiplier} \times \text{Contracts}
$$

**Theoretical spread:**

$$
S_{\text{theory}} = F_0 \cdot (r + u - y) \cdot \Delta T
$$

**Z-score (for entry):**

$$
Z = \frac{S_{\text{current}} - S_{\text{mean}}}{\sigma_S}
$$

Enter when $|Z| > 2$

### Advantages Over Outrights

| Factor | Outright | Calendar Spread |
|--------|---------|----------------|
| Directional risk | YES (high) | NO (hedged) |
| Volatility | 25-35% | 5-10% |
| Margin | 10% notional | 2-3% notional |
| Correlation to market | 1.0 | 0.1-0.3 |
| Skill required | Price direction | Market structure |

**Calendar spreads = Market structure trades, not directional bets**

### When to Use Calendar Spreads

**Use when:**
- You understand commodity fundamentals
- Can monitor inventory/weather data
- Have view on curve shape (not price direction)
- Want lower risk than outrights
- Can handle complexity

**Don't use when:**
- Need directional exposure
- Can't monitor fundamentals
- Don't understand spread drivers
- Over-leveraged (need full margin capacity)

### Final Wisdom

> "Calendar spreads are the professional's tool for trading commodity market structure without taking directional risk. You're not betting on oil going to $100 or $50—you're betting on whether the curve is too steep or too flat. When the spread is at 3-sigma, the market structure is dislocated, and reversion is highly probable. But don't confuse 'lower risk' with 'no risk'—spreads can still blow up if you ignore fundamentals, over-leverage, or lack discipline. Trade the structure, size appropriately, and always have an exit plan."

**Key principles:**

1. **Know the historical spread range** (calculate mean, σ)
2. **Enter at extremes** (>2σ from mean)
3. **Monitor fundamentals** (inventory, weather, supply)
4. **Use stops** (spread moves >1-2σ against you)
5. **Size conservatively** (30% of capital max)
6. **Seasonal patterns are your friend** (trade with them)
7. **Exit at targets** (don't be greedy)
8. **Understand both legs** (how they interact)

**Most important:**

Calendar spreads reduce risk but don't eliminate it. Spread volatility is 70% lower than outrights, but 3-sigma events still happen. The 2020 COVID oil spread moved 5-sigma in days. Over-leverage kills. Discipline and risk management are everything. **Trade the structure, not the price.** 🎯📊

**Remember:**
- Lower risk ≠ No risk
- Market neutral ≠ Risk-free
- Always have stops
- **Never over-leverage!** ⚠️
