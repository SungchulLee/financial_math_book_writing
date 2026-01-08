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

### 1. Calendar Spread Defined

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

### 2. Simple Example

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

### 3. Why Calendar Spreads Exist

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

## Economic

**Beyond the mechanical definition, understanding the economic drivers:**

### 1. The Theory of Storage

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

### 2. Inventory Dynamics

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

### 3. Seasonal Patterns

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

### 4. Natural Gas

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

### 5. The Convergence Property

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

### 6. Why This Perspective Matters

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

## Contract Specifications

**Understanding which commodities have the best spread trading opportunities:**

### 1. Energy Commodities (High Spread Volatility)

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

### 2. Agricultural Commodities (Harvest Patterns)

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

### 3. Precious Metals (Interest Rate Driven)

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

### 4. Livestock (Production Cycles)

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

### 5. Spread Liquidity Considerations

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

## Maximum Profit and Loss

### 1. Understanding Calendar Spread P&L

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

### 2. Maximum Profit (Long Spread)

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

### 3. Maximum Loss (Long Spread)

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

### 4. Real-World Example

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

### 5. Calendar Spread Risk vs. Outright Risk

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

### 1. Entry Strategies

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

### 2. Exit Strategies

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

### 3. Position Management Techniques

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



## Final Wisdom

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