# Basis Trading

**Basis trading** involves taking positions in both the spot (cash) market and futures market simultaneously to profit from the difference between the two prices, exploiting predictable patterns in how spot and futures prices converge, diverge, and respond to supply-demand imbalances.

---

## The Core Insight

**The fundamental idea:**

- Futures and spot prices aren't identical—they differ by "basis"
- Basis = Spot Price - Futures Price
- Basis changes predictably due to carry costs, convenience yield, seasonality
- Trade the relationship, not the absolute price direction
- Profit when basis moves as expected (strengthens or weakens)
- Market-neutral: Don't care if prices go up or down, only care about the spread

**The key equation:**

$$
\text{Basis}_t = S_t - F_t
$$

**Where:**
- $S_t$ = Spot (cash) price at time $t$
- $F_t$ = Futures price at time $t$

**At expiration, basis must converge to zero:**

$$
\lim_{t \to T} \text{Basis}_t = 0
$$

**You're essentially betting: "I know how spot and futures will move relative to each other, regardless of their absolute direction."**

---

## What is Basis Trading?

**Before trading basis, understand what you're actually trading:**

### The Basis Defined

**Definition:** Basis is the difference between the spot (cash) price and the futures price at any given moment.

$$
\text{Basis} = \text{Spot} - \text{Futures}
$$

**Sign conventions:**

- **Negative basis (contango):** $S < F$ (futures higher than spot)
  - Normal for storable commodities
  - Reflects carrying costs (storage, insurance, financing)
  
- **Positive basis (backwardation):** $S > F$ (spot higher than futures)
  - Indicates supply shortage
  - Reflects convenience yield
  - Spot premium for immediate delivery

**Example:**

- Crude oil spot: $75.00/barrel
- Crude oil futures (3-month): $76.50/barrel
- **Basis = $75.00 - $76.50 = -$1.50 (negative, contango)**

### What Basis Trading Is

**A basis trade is NOT:**
- A directional bet on price going up or down
- A speculation on absolute price levels
- An unhedged position

**A basis trade IS:**
- A simultaneous long-short position (long spot, short futures OR vice versa)
- A bet on the spread between spot and futures
- Market-neutral to absolute price movements
- A relative value trade

**The two basic basis trades:**

**1. Long Basis Trade (Buy the Basis):**

$$
\text{Long Spot} + \text{Short Futures}
$$

- Buy physical commodity (or spot position)
- Simultaneously sell futures
- Profit if basis strengthens (becomes more positive/less negative)
- **Example:** Buy oil at spot $75, sell futures at $77, basis = -$2
- **Profit if:** Basis moves from -$2 to -$1 (strengthened)

**2. Short Basis Trade (Sell the Basis):**

$$
\text{Short Spot} + \text{Long Futures}
$$

- Sell physical commodity (or short spot position)
- Simultaneously buy futures
- Profit if basis weakens (becomes more negative/less positive)
- **Example:** Sell oil at spot $75, buy futures at $77, basis = -$2
- **Profit if:** Basis moves from -$2 to -$3 (weakened)

### Example: Simple Basis Trade

**Setup (Long Basis Trade):**

- **Month 1:**
  - Crude oil spot: $75.00/barrel
  - 3-month futures: $77.00/barrel
  - **Basis: $75 - $77 = -$2.00**
  - Trade: Buy spot at $75, Short futures at $77

- **Month 3 (convergence at expiration):**
  - Spot: $80.00 (price went up!)
  - Futures: $80.00 (also went up, converges at expiration)
  - **Basis: $80 - $80 = $0.00**

**P&L Calculation:**

**Spot position:**
- Bought at $75, now worth $80
- P&L: +$5.00

**Futures position:**
- Short at $77, now $80
- P&L: -$3.00 (loss on short)

**Net P&L:**
- Total: +$5.00 - $3.00 = **+$2.00**
- **This equals the basis change: $0 - (-$2) = +$2.00** ✓

**Notice:**
- Absolute prices went UP ($75 → $80)
- Still made money because basis strengthened (-$2 → $0)
- **Didn't need to predict direction, only predicted convergence**

**Alternative scenario (prices fall):**

- **Month 3:**
  - Spot: $70.00 (price went down!)
  - Futures: $70.00 (also went down, still converges)
  - **Basis: $70 - $70 = $0.00**

**P&L:**

**Spot:** $70 - $75 = -$5.00 (loss)
**Futures:** $77 - $70 = +$7.00 (gain on short)
**Net:** -$5 + $7 = **+$2.00** ✓

**Same profit regardless of direction!**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/basis_trading.png?raw=true" alt="basis_trading" width="700">
</p>
**Figure 1:** Long and short basis trading strategies, showing how the convergence of spot and futures prices creates profit opportunities independent of absolute price direction. The basis trade profits from the spread movement, not from directional price changes.

---

## Economic Interpretation: Why Basis Exists and Changes

**Beyond the simple definition, understanding the economic forces behind basis:**

### The Cost of Carry Model

**For storable commodities, basis reflects the cost of carrying the physical commodity:**

$$
F_t = S_t \cdot e^{(r + u - y)(T-t)}
$$

Where:
- $F_t$ = Futures price
- $S_t$ = Spot price
- $r$ = Risk-free interest rate
- $u$ = Storage cost (% per annum)
- $y$ = Convenience yield
- $T-t$ = Time to expiration

**Rearranging for basis:**

$$
\text{Basis}_t = S_t - F_t = S_t(1 - e^{(r+u-y)(T-t)}) \approx -S_t(r+u-y)(T-t)
$$

**For small $(T-t)$:**

$$
\text{Basis}_t \approx -S_t \cdot \text{(Net Carry Cost)} \cdot \text{(Time)}
$$

**Components:**

1. **Interest cost ($r$):** Opportunity cost of capital tied up in commodity
2. **Storage cost ($u$):** Physical storage, insurance, handling
3. **Convenience yield ($y$):** Benefit of holding physical vs. futures

**Normal contango (typical for most commodities):**

If $r + u > y$ (carry costs exceed convenience yield):

$$
F > S \quad \implies \quad \text{Basis} < 0
$$

**Backwardation (shortage conditions):**

If $y > r + u$ (convenience yield exceeds carry costs):

$$
S > F \quad \implies \quad \text{Basis} > 0
$$

### Example: Gold Basis Calculation

**Given:**
- Spot gold: $2,000/oz
- Risk-free rate: 5% annual
- Storage cost: 0.5% annual
- Convenience yield: 0% (gold has no convenience yield)
- Time: 3 months (0.25 years)

**Fair futures price:**

$$
F = 2000 \cdot e^{(0.05 + 0.005 - 0)(0.25)} = 2000 \cdot e^{0.01375} \approx \$2,027.63
$$

**Fair basis:**

$$
\text{Basis} = \$2,000 - \$2,027.63 = -\$27.63
$$

**If actual futures trades at $2,040:**
- Actual basis: $2,000 - $2,040 = -$40
- Fair basis: -$27.63
- **Basis too wide (futures overpriced) → Arbitrage opportunity!**

### The Convergence Theorem

**The fundamental law of basis trading:**

$$
\lim_{t \to T} \text{Basis}_t = 0
$$

**At expiration:**
- Futures = Spot (by definition of futures settlement)
- Any deviation → Instantaneous arbitrage
- **This convergence is GUARANTEED**

**The convergence path:**

$$
\text{Basis}_t = \text{Basis}_0 \cdot \frac{T-t}{T}
$$

**For contango (-$2 basis with 3 months to expiration):**

| Time | Days to Expiry | Expected Basis | Convergence |
|------|---------------|----------------|-------------|
| Month 0 | 90 | -$2.00 | 0% |
| Month 1 | 60 | -$1.33 | 33% |
| Month 2 | 30 | -$0.67 | 67% |
| Month 3 | 0 | $0.00 | 100% ✓ |

**This predictable convergence is the foundation of basis trading!**

### Basis Risk Components

**Why basis doesn't follow theory perfectly:**

**1. Location basis:**

$$
\text{Local Basis} = \text{Local Spot} - \text{Futures (Delivery Point)}
$$

**Example:**
- NYMEX crude oil futures: Delivery at Cushing, OK
- Actual oil: At Midland, TX
- Transportation cost: $2.00/barrel
- **Expected local basis: -$2.00 wider than Cushing basis**

**2. Quality basis:**

$$
\text{Quality Basis} = \text{Actual Grade} - \text{Futures Grade}
$$

**Example:**
- Corn futures: #2 Yellow Corn
- Farmer's corn: #1 Yellow (premium grade)
- Premium: +$0.10/bushel
- **Quality basis: +$0.10**

**3. Timing basis:**

$$
\text{Timing Basis} = \text{Actual Delivery Date} - \text{Futures Delivery Month}
$$

**Example:**
- Farmer harvests: October 15
- Futures delivery: December 1-30
- Storage cost: $0.05/bushel per month
- **Timing basis: -$0.08 (1.5 months storage)**

**Total basis:**

$$
\text{Total Basis} = \text{Theoretical} + \text{Location} + \text{Quality} + \text{Timing}
$$

### Economic Forces That Change Basis

**1. Supply shocks (strengthen basis → backwardation):**

**Example: Oil refinery fire**
- Immediate supply shortage
- Spot price spikes
- Futures less affected (future supply normal)
- **Basis: -$2 → +$5 (strengthened dramatically)**

**2. Demand surges (strengthen basis):**

**Example: Harsh winter for natural gas**
- Immediate heating demand
- Spot price spikes
- Futures (summer months) unaffected
- **Basis strengthens**

**3. Storage capacity (weaken basis → contango):**

**Example: Bumper crop harvest**
- Abundant supply now
- Storage facilities full
- Spot price depressed
- Futures (future delivery) less affected
- **Basis weakens (more negative contango)**

**4. Seasonality (predictable patterns):**

**Example: Agricultural commodities**
- At harvest: Spot prices low (abundant supply)
- Post-harvest: Futures higher (reflect storage costs)
- **Basis most negative at harvest**

**5. Interest rates (affect carry costs):**

$$
\frac{\partial F}{\partial r} > 0 \quad \implies \quad \frac{\partial \text{Basis}}{\partial r} < 0
$$

- Higher rates → Higher futures (more carry cost)
- **Basis weakens (more negative)**

### Convenience Yield: The Hidden Factor

**Definition:** The benefit of holding physical commodity vs. futures contract.

$$
y = r + u - \frac{1}{T-t} \ln\left(\frac{F}{S}\right)
$$

**When convenience yield is high:**
- Processing/industrial use valuable
- Stockouts costly
- Inventory low
- **Spot premium (backwardation)**

**Example: Crude oil convenience yield:**

**Normal times:**
- Inventories adequate
- Convenience yield: ~1-2%
- Basis: Slight contango (-$1 to -$2)

**Supply disruption:**
- Inventories critical
- Refineries need oil NOW
- Convenience yield spikes: 10%+
- **Basis: Strong backwardation (+$5 to +$10)**

### Arbitrage and Basis Bounds

**The no-arbitrage bounds:**

**Upper bound (storage arbitrage):**

If $F > S \cdot e^{(r+u)(T-t)}$ (futures too high):

1. Buy spot at $S$
2. Short futures at $F$
3. Store until delivery
4. Deliver into futures
5. **Guaranteed profit: $F - S - \text{Carry Costs}$**

**Lower bound (reverse cash-and-carry):**

If $F < S \cdot e^{(r-y)(T-t)}$ (futures too low):

1. Short spot at $S$
2. Long futures at $F$
3. Invest proceeds at $r$
4. Take delivery from futures
5. **Guaranteed profit: $S + \text{Interest} - F$**

**These bounds keep basis within limits:**

$$
-S \cdot (r+u)(T-t) \leq \text{Basis} \leq -S \cdot (r-y_{\max})(T-t)
$$

**Market makers constantly monitor for violations!**

### Why This Perspective Matters

**Understanding basis economics helps you:**

1. **Predict basis movements:**
   - Supply shock → Basis strengthens
   - Harvest flood → Basis weakens
   - Rate hikes → Basis weakens (higher carry)

2. **Identify arbitrage:**
   - Basis outside theoretical bounds
   - Mispricing creates opportunity
   - **True arbitrage (riskless profit)**

3. **Understand seasonality:**
   - Agricultural commodities: Harvest patterns
   - Energy commodities: Winter/summer demand
   - **Predictable basis cycles**

4. **Manage risk better:**
   - Hedgers understand basis risk
   - Traders time entries/exits
   - **Basis trading complements hedging**

**This is why sophisticated traders view basis as "the only thing that matters in commodity markets—absolute price is just noise."**

---

## Key Terminology

**Basis Fundamentals:**

**Basis:**

$$
\text{Basis} = S_t - F_t
$$

- Difference between spot and futures
- Can be positive or negative
- Converges to zero at expiration
- **Core concept of commodity markets**

**Spot Price (Cash Price):**
- Current price for immediate delivery
- Physical commodity transaction
- Local market conditions
- "What you can buy/sell TODAY"

**Futures Price:**
- Price for standardized future delivery
- Exchange-traded, liquid
- Reflects expectations + carry costs
- "What you can lock in for FUTURE"

**Convergence:**
- Basis → 0 as expiration approaches
- Spot and futures prices merge
- Guaranteed by arbitrage
- **Foundation of basis trading**

**Market Structure Terms:**

**Contango:**

$$
F > S \quad \implies \quad \text{Basis} < 0
$$

- Futures trade above spot
- Normal for storable commodities
- Reflects positive carry costs
- **Hurts long futures (negative roll yield)**

**Example:**
- Spot crude: $75
- 3-month futures: $77
- Basis: -$2 (contango)

**Backwardation:**

$$
S > F \quad \implies \quad \text{Basis} > 0
$$

- Spot trades above futures
- Indicates supply shortage or high convenience yield
- Abnormal market condition
- **Helps long futures (positive roll yield)**

**Example:**
- Spot crude: $75
- 3-month futures: $72
- Basis: +$3 (backwardation)

**Normal Contango:**
- Equilibrium state for storable commodities
- Futures higher by carry costs
- **Typical market structure**

**Normal Backwardation:**
- Historical theory (Keynes)
- Futures below expected spot
- Hedgers pay risk premium
- **Less common in modern markets**

**Basis Changes:**

**Basis Strengthening (Basis Increases):**
- Basis becomes more positive (or less negative)
- Spot rises faster than futures
- Or futures falls faster than spot

$$
\text{Basis}_{\text{new}} > \text{Basis}_{\text{old}}
$$

**Example:**
- Old basis: -$2.00
- New basis: -$1.00
- **Strengthened by $1.00**

**Profits:**
- Long basis traders (long spot, short futures)
- Hedgers who are long physical commodity

**Basis Weakening (Basis Decreases):**
- Basis becomes more negative (or less positive)
- Futures rises faster than spot
- Or spot falls faster than futures

$$
\text{Basis}_{\text{new}} < \text{Basis}_{\text{old}}
$$

**Example:**
- Old basis: -$2.00
- New basis: -$3.00
- **Weakened by $1.00**

**Profits:**
- Short basis traders (short spot, long futures)

**Basis Risk:**
- Uncertainty in basis changes
- Difference between expected and actual basis
- Main risk for hedgers and basis traders

$$
\text{Basis Risk} = \text{Actual Basis}_T - \text{Expected Basis}_T
$$

**Carry Costs and Yield:**

**Cost of Carry:**

$$
\text{Carry} = r + u - y
$$

- $r$ = Interest/financing cost
- $u$ = Storage cost
- $y$ = Convenience yield
- **Net cost of holding physical commodity**

**Full Carry:**
- Futures price = Spot + Full carry costs
- Maximum contango
- No arbitrage opportunity

$$
F = S \cdot e^{(r+u)(T-t)}
$$

**Convenience Yield:**

$$
y = r + u - \frac{1}{T-t} \ln\left(\frac{F}{S}\right)
$$

- Benefit of holding physical vs. futures
- High when inventories low
- Causes backwardation when $y > r + u$
- **"Shadow benefit" of physical ownership**

**Examples:**
- Oil refinery needs oil NOW (high $y$)
- Grain elevator has storage space (low $y$)

**Basis Trading Positions:**

**Long Basis (Buy the Basis):**

$$
\text{Long Spot} + \text{Short Futures}
$$

- Profit if basis strengthens
- Market-neutral to absolute price
- Example: Buy physical gold, short gold futures

**Short Basis (Sell the Basis):**

$$
\text{Short Spot} + \text{Long Futures}
$$

- Profit if basis weakens
- Market-neutral to absolute price
- Example: Short physical copper, long copper futures

**Basis Spread:**
- P&L of basis position
- Change in basis × position size

$$
\text{P\&L} = \Delta \text{Basis} \times \text{Quantity} \times \text{Position}
$$

**Local Basis:**
- Basis at specific location (not delivery point)
- Includes transportation costs
- Varies by geography

**Example:**
- Chicago corn futures: $4.50
- Iowa spot corn: $4.20
- **Iowa local basis: -$0.30**

**Quality Basis:**
- Difference due to commodity grade/quality
- Premium or discount to futures grade

**Example:**
- Futures: #2 Yellow Corn
- Actual: #1 Yellow Corn (+$0.10 premium)
- **Quality basis: +$0.10**

**Calendar Spread:**
- Difference between two futures months
- Related but not identical to basis
- Reflects storage costs over time

$$
\text{Calendar Spread} = F_{\text{near}} - F_{\text{far}}
$$

**Intercommodity Spread:**
- Difference between related commodities
- Example: Crude vs. gasoline (crack spread)
- Example: Soybeans vs. soy meal + soy oil (crush spread)

**Basis Trading Strategies:**

**Cash-and-Carry Arbitrage:**

If futures overpriced ($F > S \cdot e^{(r+u)(T-t)}$):

1. Buy spot
2. Short futures
3. Store and carry
4. Deliver into futures
5. **Lock in arbitrage profit**

**Reverse Cash-and-Carry:**

If futures underpriced ($F < S \cdot e^{r(T-t)}$):

1. Short spot (if possible)
2. Long futures
3. Invest proceeds
4. Cover short with futures delivery
5. **Lock in arbitrage profit**

**Basis Convergence Trade:**
- Bet on normal convergence to zero
- Long basis if basis negative (contango)
- Hold until expiration
- **Profit from predictable convergence**

**Basis Reversion Trade:**
- Bet basis will revert to historical mean
- If basis unusually wide → Long basis
- If basis unusually narrow → Short basis
- **Mean reversion strategy**

**Seasonal Basis Trade:**
- Exploit predictable seasonal patterns
- Agricultural: Harvest/post-harvest cycles
- Energy: Winter/summer demand
- **Calendar-based strategy**

---

## Contract Specifications: Where Basis Trading Happens

**Understanding which contracts are suitable for basis trading:**

### Agricultural Commodities (Strong Seasonality)

**Corn (ZC - CBOT):**

**Contract specs:**
- Size: 5,000 bushels
- Delivery: Chicago
- Months: March, May, July, September, December

**Typical basis patterns:**

| Period | Basis | Reason |
|--------|-------|--------|
| Pre-harvest (Sep) | -$0.20 to -$0.30 | Anticipation of supply |
| Harvest (Oct-Nov) | -$0.40 to -$0.60 | Abundant supply, negative carry |
| Post-harvest (Dec-Feb) | -$0.25 to -$0.35 | Storage costs, tightening |
| Spring (Mar-May) | -$0.15 to -$0.25 | Inventories declining |

**Basis trade opportunity:**

**September:** Basis at -$0.25 (pre-harvest)
**October:** Expect basis to weaken to -$0.50 (harvest pressure)
**Trade:** Short basis (short spot, long futures)
**Target:** Profit from $0.25 basis weakening

**Example P&L:**
- Short spot at $4.50, Long futures at $4.75 (basis -$0.25)
- At harvest: Spot $4.00, Futures $4.50 (basis -$0.50)
- Spot P&L: -($4.00 - $4.50) = +$0.50 (covered short lower)
- Futures P&L: -($4.50 - $4.75) = -$0.25 (futures fell less)
- **Net: +$0.50 - $0.25 = +$0.25 per bushel**
- On 50,000 bu (10 contracts): **+$12,500** ✓

**Wheat (ZW - CBOT):**

**Basis characteristics:**
- Similar harvest patterns to corn
- Three types: Chicago (soft red), KC (hard red), Minneapolis (spring)
- Inter-market basis trades possible

**Soybeans (ZS - CBOT):**

**Basis notes:**
- Crush spread relationship (soybeans → meal + oil)
- More complex basis dynamics
- Harvest patterns similar to corn

### Energy Commodities (Strong Contango/Backwardation Swings)

**Crude Oil (CL - NYMEX):**

**Contract specs:**
- Size: 1,000 barrels
- Delivery: Cushing, Oklahoma
- Months: All months (12 months liquid)

**Typical basis patterns:**

**Normal contango:**
- Inventories adequate
- Basis: -$1.50 to -$2.50 per barrel
- Reflects storage + financing

**Example:**
- Spot: $75.00
- 3-month futures: $77.00
- Basis: -$2.00 (contango)

**Supply disruption (backwardation):**
- Inventories critical
- Immediate demand high
- Basis: +$3.00 to +$10.00 (spot premium)

**Example:**
- Spot: $80.00
- 3-month futures: $75.00
- Basis: +$5.00 (backwardation)

**Basis trade opportunity (contango collapse):**

**Setup:** Basis at -$3.00 (steep contango)
**Expectation:** Supply concerns will strengthen basis
**Trade:** Long basis (buy spot, short futures)

**Outcome:**
- Basis moves to -$1.00 (strengthened by $2.00)
- Profit: $2.00/barrel × 1,000 × contracts

**Natural Gas (NG - NYMEX):**

**Extreme seasonality:**

| Season | Basis Pattern | Reason |
|--------|--------------|--------|
| Summer (low demand) | -$1.00 to -$2.00 | Contango, storage filling |
| Fall (shoulder) | -$0.50 to -$1.00 | Moderate |
| Winter (high demand) | +$0.50 to +$2.00 | Backwardation, draw season |
| Spring (shoulder) | -$0.50 to -$1.00 | Moderate |

**Basis trade: Winter-Summer spread**

**October:** Winter contract (Dec) at $5.00, Summer (July) at $3.00
**Spread:** $2.00 (winter premium)
**Historical average:** $1.50
**Trade:** Sell winter premium (short Dec, long July)
**Target:** Spread narrows to $1.50, profit $0.50 per MMBtu

**Heating Oil (HO) and RBOB Gasoline (RB):**

**Refining margins:**
- Crack spread: Crude oil → refined products
- Basis relationship between crude and products
- Seasonal demand patterns (heating oil winter, gasoline summer)

### Metals (Stable Contango)

**Gold (GC - COMEX):**

**Contract specs:**
- Size: 100 troy ounces
- Delivery: New York
- Very liquid, tight basis

**Typical basis:**
- Consistent contango
- Reflects only interest + storage (no convenience yield)
- Basis: -$2 to -$3 per oz for 3-month

$$
\text{Fair Basis} \approx -S \times r \times (T-t)
$$

**Example:**
- Spot: $2,000
- 3-month futures: $2,025
- Basis: -$25
- Fair basis (5% rate): -$2,000 × 0.05 × 0.25 = -$25 ✓

**Basis trade opportunity (mispricing):**

If futures at $2,035 (basis -$35 vs. fair -$25):
- Futures overpriced by $10
- **Arbitrage:** Buy spot $2,000, Short futures $2,035
- Carry cost: $25
- Lock in: $2,035 - $2,000 - $25 = **$10 profit** per oz

**Silver (SI - COMEX):**

**Similar to gold but:**
- Higher storage costs (bulkier)
- Industrial demand → Some convenience yield
- Wider basis spreads

**Copper (HG - COMEX):**

**Industrial metal:**
- Strong convenience yield (manufacturing use)
- Often in backwardation (supply tight)
- Basis reflects production/inventory cycles

### Stock Index Futures (Dividend-Driven Basis)

**E-mini S&P 500 (ES):**

**Basis calculation:**

$$
F = S \times e^{(r-q)(T-t)}
$$

Where $q$ = dividend yield

**Typical basis:**
- Slight contango (interest rate > dividend yield)
- Very tight basis (highly liquid, low carry costs)
- Basis: -5 to -15 points for quarterly contract

**Example:**
- Spot (SPX): 4500
- 3-month futures: 4510
- Basis: -10 points

**Fair value:**

$$
4500 \times e^{(0.05-0.015) \times 0.25} \approx 4539
$$

**If futures at 4520:**
- Below fair value by ~19 points
- **Arbitrage:** Buy spot, short futures

**Basis trading less common (arbitrageurs dominant):**
- Program trading keeps basis very tight
- Small retail traders can't compete
- Basis trades here are "index arbitrage"

### Commodity Spreads

**Crack Spread (Crude → Refined Products):**

$$
\text{Crack Spread} = \text{Products Price} - \text{Crude Price}
$$

**3:2:1 Crack:**
- 3 barrels crude → 2 barrels gasoline + 1 barrel heating oil
- Measures refining margin
- Basis-like relationship

**Crush Spread (Soybeans → Meal + Oil):**

$$
\text{Crush Spread} = (\text{Meal Price} + \text{Oil Price}) - \text{Soybean Price}
$$

- Measures processing margin
- Basis relationship within complex

---

## Maximum Profit and Loss: The Basis Trading Payoff

### Understanding Basis Trade Payoffs

**The fundamental payoff equation:**

$$
\text{P\&L}_{\text{basis trade}} = \Delta \text{Basis} \times \text{Quantity} \times \text{Direction}
$$

Where:
- $\Delta \text{Basis} = \text{Basis}_{\text{exit}} - \text{Basis}_{\text{entry}}$
- Direction: +1 for long basis, -1 for short basis

**Key insight: Payoff depends ONLY on basis change, not absolute price movement.**

### Long Basis (Buy the Basis) Payoffs

**Position:** Long Spot + Short Futures

**Maximum profit:**

$$
\text{Max Profit} = \text{Maximum Basis Strengthening} \times \text{Quantity}
$$

**Theoretical maximum:**
- Basis starts highly negative (steep contango)
- Moves to highly positive (strong backwardation)
- Change could be $5-$10 in extreme cases

**Practical maximum (oil example):**
- Entry: Basis -$3.00 (steep contango)
- Exit: Basis +$2.00 (backwardation from supply shock)
- **Basis strengthened by $5.00**
- On 10,000 barrels (10 contracts): **$50,000 profit**

**Maximum loss:**

$$
\text{Max Loss} = \text{Maximum Basis Weakening} \times \text{Quantity}
$$

**Practical maximum:**
- Entry: Basis -$2.00
- Exit: Basis -$5.00 (contango steepens, storage glut)
- **Basis weakened by $3.00**
- On 10,000 barrels: **-$30,000 loss**

**Convergence trade (common):**

**Setup:**
- Entry: Basis -$2.00 (3 months to expiration)
- Exit: Basis $0.00 (at expiration, convergence)
- **Guaranteed basis strengthening of $2.00** (if held to expiry)

**P&L:**
- Basis change: $0 - (-$2) = +$2.00
- On 10,000 barrels: **+$20,000 profit** ✓

**Notice: Convergence trade has known maximum profit!**

### Short Basis (Sell the Basis) Payoffs

**Position:** Short Spot + Long Futures

**Maximum profit:**

$$
\text{Max Profit} = \text{Maximum Basis Weakening} \times \text{Quantity}
$$

**Example (harvest trade):**
- Entry (pre-harvest): Basis -$0.25
- Exit (harvest glut): Basis -$0.60
- **Basis weakened by $0.35**
- On 50,000 bushels corn: **+$17,500 profit**

**Maximum loss:**

$$
\text{Max Loss} = \text{Maximum Basis Strengthening} \times \text{Quantity}
$$

**Example (supply disruption):**
- Entry: Basis -$2.00
- Exit: Basis +$3.00 (unexpected shortage)
- **Basis strengthened by $5.00**
- On 10,000 barrels: **-$50,000 loss**

### Detailed P&L Examples

**Example 1: Long Basis, Prices Rise**

**Entry:**
- Spot crude: $75/barrel
- Futures: $77/barrel
- Basis: -$2.00
- Position: Long 10,000 barrels spot, Short 10 futures

**Exit (3 months later, bullish market):**
- Spot: $85/barrel (up $10)
- Futures: $86/barrel (up $9)
- Basis: -$1.00

**P&L breakdown:**

**Spot position:**
- Bought: $75, Sold: $85
- P&L: +$10/barrel × 10,000 = **+$100,000**

**Futures position:**
- Sold: $77, Covered: $86
- P&L: -$9/barrel × 10,000 = **-$90,000**

**Net P&L:**
- +$100,000 - $90,000 = **+$10,000**

**Basis P&L check:**
- Basis change: -$1 - (-$2) = +$1 (strengthened)
- P&L: +$1 × 10,000 = **+$10,000** ✓

**Notice:** Made money even though had to cover futures short higher!

**Example 2: Long Basis, Prices Fall**

**Entry:**
- Same as above: Basis -$2.00

**Exit (3 months later, bearish market):**
- Spot: $65/barrel (down $10)
- Futures: $66/barrel (down $11)
- Basis: -$1.00 (same strengthening!)

**P&L breakdown:**

**Spot:**
- Bought: $75, Sold: $65
- P&L: -$10/barrel × 10,000 = **-$100,000**

**Futures:**
- Sold: $77, Covered: $66
- P&L: +$11/barrel × 10,000 = **+$110,000**

**Net P&L:**
- -$100,000 + $110,000 = **+$10,000**

**Basis P&L check:**
- Basis change: -$1 - (-$2) = +$1
- P&L: +$1 × 10,000 = **+$10,000** ✓

**Key insight: Same profit whether prices rise or fall!**

**Example 3: Short Basis, Harvest Trade**

**Entry (September, pre-harvest):**
- Spot corn: $4.50/bu
- December futures: $4.75/bu
- Basis: -$0.25
- Position: Short 50,000 bu spot, Long 10 futures (50,000 bu)

**Exit (November, post-harvest):**
- Spot: $4.00/bu (harvest pressure)
- Futures: $4.55/bu (fell less)
- Basis: -$0.55

**P&L breakdown:**

**Spot (short):**
- Sold: $4.50, Covered: $4.00
- P&L: +$0.50/bu × 50,000 = **+$25,000**

**Futures (long):**
- Bought: $4.75, Sold: $4.55
- P&L: -$0.20/bu × 50,000 = **-$10,000**

**Net P&L:**
- +$25,000 - $10,000 = **+$15,000**

**Basis P&L check:**
- Basis change: -$0.55 - (-$0.25) = -$0.30 (weakened)
- Short basis profits from weakening
- P&L: +$0.30 × 50,000 = **+$15,000** ✓

### Risk Comparison to Outright Positions

**Scenario: $10 absolute price move**

**Outright long (10,000 barrels):**
- If price +$10: Profit +$100,000
- If price -$10: Loss -$100,000
- **Variance: Very high**

**Long basis (long spot, short futures):**
- If prices both +$10, basis unchanged: Profit $0
- If prices both +$10, basis +$1: Profit $10,000
- If prices both -$10, basis +$1: Profit $10,000
- **Variance: Much lower (only basis risk)**

**Risk reduction factor:**

If basis volatility = 20% of price volatility:

$$
\text{Basis Trade Risk} \approx 0.04 \times \text{Outright Position Risk}
$$

**Example:**
- Outright position std dev: $50,000
- Basis trade std dev: $10,000
- **80% risk reduction from hedging price risk!**

---

## Entry and Exit Strategies

### Entry Strategies: When to Initiate Basis Trades

**1. Convergence Trade Entry**

**Setup:** Basis in contango, approaching expiration

**Entry criteria:**
- Basis negative (futures > spot)
- 1-3 months to expiration
- Historical basis pattern shows reliable convergence

**Example:**

| Time to Expiry | Typical Basis | Trade |
|---------------|---------------|--------|
| 3 months | -$2.00 | Enter long basis |
| 2 months | -$1.33 | Monitor |
| 1 month | -$0.67 | Monitor |
| Expiry | $0.00 | Exit (profit $2.00) ✓ |

**Risk:** Basis might not converge smoothly (basis risk)

**2. Mean Reversion Entry**

**Setup:** Basis deviated significantly from historical average

**Historical analysis:**
- Calculate average basis for same period over 5 years
- Calculate standard deviations
- Entry when basis > 2 std dev from mean

**Example (crude oil):**

**Historical 3-month basis:**
- Mean: -$1.80
- Std dev: $0.40
- Current: -$3.00
- Z-score: (-$3.00 - (-$1.80)) / $0.40 = -3.0

**Trade:** Long basis (basis too weak, expect reversion)
**Entry:** Current basis -$3.00
**Target:** Mean -$1.80
**Profit potential:** $1.20/barrel

**3. Seasonal Pattern Entry**

**Agricultural commodities exhibit predictable basis patterns:**

**Corn basis seasonal pattern:**

| Month | Expected Basis | Action |
|-------|---------------|---------|
| Sep (pre-harvest) | -$0.25 | Setup short basis |
| Oct-Nov (harvest) | -$0.50 to -$0.60 | Peak weakness, exit short |
| Dec-Feb (post-harvest) | -$0.35 | Setup long basis |
| Mar-May (spring) | -$0.20 to -$0.25 | Exit long |

**Trade setup (harvest weakness):**

**August:** Basis -$0.20
**September:** Basis -$0.25 (starting to weaken)
**Entry:** Short basis (short spot, long futures) at -$0.25
**October:** Basis -$0.55 (harvest pressure)
**Exit:** Cover basis trade, profit $0.30/bu

**4. Carry Arbitrage Entry**

**When basis deviates from cost of carry:**

**Fair value calculation:**

$$
\text{Fair Basis} = -S \times (r + u - y) \times (T-t)
$$

**Example (gold):**
- Spot: $2,000/oz
- Interest rate: 5%
- Storage: 0.5%
- Time: 3 months (0.25 years)
- Fair basis: -$2,000 × 0.055 × 0.25 = -$27.50

**If actual basis: -$40 (futures overpriced)**
- **Entry:** Long basis (buy spot, short futures)
- **Hold:** 3 months to convergence
- **Profit:** $40 - $27.50 (carry cost) = **$12.50/oz profit**

**5. Supply/Demand Shock Entry**

**Unexpected events create basis opportunities:**

**Example (refinery outage):**

**Normal:**
- Crude spot: $75
- Futures: $77
- Basis: -$2.00

**Refinery fire announced:**
- Crude spot: $78 (immediate shortage)
- Futures: $77 (future supply OK)
- Basis: +$1.00 (strengthened to backwardation)

**If expecting basis to strengthen further:**
- **Entry:** Long basis at +$1.00
- **Thesis:** Shortage will worsen
- **Target:** Basis to +$3.00
- **Profit potential:** $2.00/barrel

### Exit Strategies: When to Close Basis Trades

**1. Expiration Exit (Convergence Complete)**

**Natural exit:** Hold to futures expiration

**Process:**
- Basis automatically → $0 at expiration
- Close both legs simultaneously
- Realize full convergence profit

**Example:**
- Entry: Basis -$2.00
- Exit (expiration): Basis $0.00
- **Profit: $2.00 locked in** ✓

**Pros:**
- Guaranteed convergence
- No timing risk

**Cons:**
- Tie up capital until expiration
- Miss other opportunities
- Carry costs accumulate

**2. Target Exit (Profit Taking)**

**Set profit target before entry:**

**Example:**
- Entry: Basis -$2.50
- Target: Basis -$1.50 (strengthening by $1.00)
- Current: Basis reaches -$1.50
- **Exit: Take $1.00 profit** ✓

**Risk of early exit:**
- Miss additional convergence ($1.50 more to $0)
- But locked in substantial profit
- Freed capital for next trade

**Decision framework:**

$$
\text{Exit if: Current Profit} > \text{Expected Remaining Profit} \times P(\text{success})
$$

**3. Stop-Loss Exit (Loss Limiting)**

**Set maximum loss tolerance:**

**Example:**
- Entry: Long basis at -$2.00
- Stop-loss: If basis weakens to -$3.00
- Maximum acceptable loss: $1.00/barrel

**Trigger scenarios:**
- Unexpected supply glut
- Storage capacity saturated
- Demand collapse

**Execute stop:**
- Close both legs immediately
- Accept $1.00 loss per barrel
- Preserve capital for better opportunities

**4. Reversion Exit (Mean Reversion Complete)**

**For mean reversion trades:**

**Entry:** Basis -$3.50 (extreme)
**Mean:** -$1.80
**Current:** Basis reaches -$1.90 (near mean)
**Exit:** Close trade, profit $1.60/barrel ✓

**Don't be greedy:**
- Mean reversion trades profit from extreme → normal
- Normal → opposite extreme is gambling
- **Exit when normalization complete**

**5. Roll Exit (Extend Duration)**

**If thesis still valid but expiration approaching:**

**Process:**
- Close front-month basis trade
- Open next-month basis trade
- Pay/collect roll cost

**Example:**

**Month 1:**
- Long basis: Long spot $75, Short March futures $77 (basis -$2)

**Late February:**
- Basis now -$1.00 (strengthened $1.00)
- March futures converging
- Still bearish on basis

**Roll:**
- Close March: Realize $1.00 profit
- Open June: Spot $76, June futures $78.50 (basis -$2.50)
- Continue basis trade with new expiration

**Cost:** Transaction costs + potential basis slippage

**6. Event Exit (Thesis Change)**

**Exit if fundamental thesis invalidated:**

**Example:**

**Original thesis:** Harvest will pressure basis
**Entry:** Short basis at -$0.25
**Unexpected:** Drought destroys crop
**New reality:** Supply shortage → Basis strengthening likely
**Exit:** Immediately close trade
**Small loss acceptable** vs. potential large loss

**7. Calendar Exit (Time Decay)**

**For convergence trades:**

**Problem:** Basis not converging as expected

**Decision rule:**

$$
\text{Exit if: } \frac{\text{Actual Convergence}}{\text{Time Elapsed}} < \frac{\text{Expected Convergence}}{\text{Time Remaining}}
$$

**Example:**
- Entry: Basis -$2.00, 90 days to expiry
- Expected: Linear convergence, $0.022/day
- Day 45: Basis should be -$1.00
- Actual: Basis -$1.70 (only $0.30 convergence)
- **Behind schedule → Exit**

### Position Management

**Dynamic adjustment strategies:**

**1. Scaling In/Out:**

**Initial position:** 50% of planned size
**If basis moves favorably:** Add 25% more
**If thesis confirmed:** Add final 25%
**Total:** 100% position over time

**Advantage:** Average better entry price if volatile

**2. Pyramiding (Adding to Winners):**

**Entry:** Long basis at -$2.00 (10 contracts)
**Basis → -$1.50:** Add 5 contracts (profit cushion)
**Basis → -$1.00:** Add 5 contracts (20 total)
**Exit:** $0.00 basis

**Weighted profit:**
- 10 contracts: $2.00 profit = $20,000
- 5 contracts: $1.50 profit = $7,500
- 5 contracts: $1.00 profit = $5,000
- **Total: $32,500** (vs. $20,000 if no pyramid)

**3. Pair Trade Management:**

**Monitor both legs separately:**

**Example:**
- Long basis: Long spot, Short futures
- Spot position: 100 barrels physical oil
- Futures position: 1 contract (1,000 barrels)
- **Mismatch:** 10:1 ratio

**Solution:**
- Proper sizing: 10 contracts for 10,000 barrels spot
- OR: Adjust spot to 1,000 barrels

**Critical:** Keep legs balanced to maintain basis exposure

---

## Best Case Scenarios: When Basis Trades Work Perfectly

### The Dream: Maximum Basis Movement in Your Favor

**What defines best case for basis traders:**

1. Large, rapid basis movement in predicted direction
2. No adverse price movements that stress capital
3. Low transaction costs and slippage
4. Perfect timing (enter at extreme, exit at reversal)
5. **Large profit from small initial capital**

### Best Case #1: The Supply Shock (Long Basis)

**Setup:**

- **Position:** Long basis in crude oil
- **Entry (Month 0):**
  - Spot crude: $75/barrel
  - 3-month futures: $77/barrel
  - **Basis: -$2.00 (normal contango)**
  - Position: Long 10,000 barrels spot + Short 10 futures
  - Capital: $100,000 (margin for both legs)

**The event:**

**Week 1: Geopolitical crisis**
- Major oil pipeline explosion
- Immediate supply disruption
- Spot market chaos, futures less affected

**Market reaction:**
- Spot crude: $75 → $85 (up $10)
- Futures: $77 → $82 (up $5, less reactive)
- **Basis: -$2 → +$3 (strengthened by $5!)**

**The perfect timing:**

**Week 2: Peak panic**
- Spot: $88
- Futures: $83
- **Basis: +$5 (maximum strengthening)**
- **Exit here!**

**P&L calculation:**

**Spot position:**
- Long at $75, Sell at $88
- Profit: $13/barrel × 10,000 = **+$130,000**

**Futures position:**
- Short at $77, Cover at $83
- Loss: $6/barrel × 10,000 = **-$60,000**

**Net P&L:**
- $130,000 - $60,000 = **+$70,000**

**Basis profit:**
- Basis change: $5 - (-$2) = **+$7 strengthening**
- Profit: $7 × 10,000 = **+$70,000** ✓

**Return:**
- Capital: $100,000
- Profit: $70,000
- **Return: 70% in 2 weeks!** 🎯

**Why this is best case:**
- Extreme basis move ($7 total)
- Rapid (2 weeks, not months)
- Perfect exit at peak
- Low carry costs (held briefly)
- Both legs profitable or manageable

**Comparison to alternatives:**

| Strategy | Entry | Exit | P&L |
|----------|-------|------|-----|
| Long spot only | $75 | $88 | +$130k |
| Long futures only | $77 | $83 | +$60k |
| **Long basis** | Basis -$2 | Basis +$5 | **+$70k** |
| Unhedged exposed | - | - | High risk |

**The basis trade:**
- Lower profit than perfect directional call
- But MUCH lower risk
- Didn't need to predict $10 price spike
- Only needed to predict basis strengthening

### Best Case #2: The Harvest Crush (Short Basis)

**Setup:**

- **Position:** Short basis in corn
- **Entry (September, pre-harvest):**
  - Spot corn: $4.50/bu
  - December futures: $4.75/bu
  - **Basis: -$0.25 (pre-harvest normal)**
  - Position: Short 100,000 bu spot + Long 20 futures
  - Capital: $50,000 margin

**The perfect storm:**

**October: Record harvest**
- Perfect weather all season
- Yields 10% above forecast
- Storage facilities filling rapidly

**Market reaction:**
- Spot corn: $4.50 → $3.90 (down $0.60, harvest pressure)
- Futures: $4.75 → $4.50 (down $0.25, less affected)
- **Basis: -$0.25 → -$0.60 (weakened by $0.35)**

**The peak:**

**November: Storage crisis**
- Elevators at capacity
- Farmers desperate to sell
- Spot: $3.75 (down $0.75 total)
- Futures: $4.40 (down $0.35 total)
- **Basis: -$0.65 (weakened by $0.40 total)**

**Exit at basis extreme!**

**P&L calculation:**

**Spot (short):**
- Short at $4.50, Cover at $3.75
- Profit: $0.75/bu × 100,000 = **+$75,000**

**Futures (long):**
- Long at $4.75, Sell at $4.40
- Loss: $0.35/bu × 100,000 = **-$35,000**

**Net P&L:**
- $75,000 - $35,000 = **+$40,000**

**Basis profit check:**
- Basis change: -$0.65 - (-$0.25) = -$0.40 (weakened)
- Short basis profits from weakening
- Profit: $0.40 × 100,000 = **+$40,000** ✓

**Return:**
- Capital: $50,000
- Profit: $40,000
- **Return: 80% in 2 months!** 🎯

**Why this is best case:**
- Predictable seasonal pattern (harvest = weakness)
- Amplified by record crop (bonus!)
- Perfect exit at peak weakness
- Risk management successful (futures hedge protected)

### Best Case #3: The Arbitrage Lock (Cash-and-Carry)

**Setup:**

- **Market inefficiency detected**
- Gold futures mispriced relative to spot + carry

**Entry conditions:**

- Spot gold: $2,000/oz
- 3-month futures: $2,040/oz
- **Actual basis: -$40**

**Fair value calculation:**

- Interest rate: 5% annual
- Storage: 0.5% annual  
- Total carry: 5.5% annual
- Time: 0.25 years (3 months)

$$
\text{Fair Basis} = -\$2,000 \times 0.055 \times 0.25 = -\$27.50
$$

**Mispricing:**
- Actual basis: -$40
- Fair basis: -$27.50
- **Futures overpriced by $12.50!**

**The arbitrage:**

**Trade:** Long basis (buy spot, short futures)
- Buy 1,000 oz spot at $2,000 = $2,000,000
- Short 10 futures at $2,040
- Storage cost: $27.50/oz
- Capital: $100,000 margin (borrowed $1.9M at 5%)

**Hold to expiration (convergence guaranteed):**

**Exit (3 months later):**
- Spot: $2,100 (price rose!)
- Futures: $2,100 (converged)
- Basis: $0 (converged as guaranteed)

**P&L:**

**Spot:**
- Buy $2,000, Sell $2,100
- Profit: $100/oz × 1,000 = **+$100,000**

**Futures:**
- Short $2,040, Cover $2,100
- Loss: $60/oz × 1,000 = **-$60,000**

**Carry costs:**
- Interest: $2,000,000 × 0.05 × 0.25 = -$25,000
- Storage: $2,000 × 0.005 × 0.25 × 1,000 = -$2,500
- **Total carry: -$27,500**

**Net P&L:**
- Spot: +$100,000
- Futures: -$60,000
- Carry: -$27,500
- **Net: +$12,500** (exactly the mispricing!) ✓

**Alternative (prices fell):**
- Spot: $1,900
- Futures: $1,900 (still converges)
- Spot P&L: -$100,000
- Futures P&L: +$140,000
- Carry: -$27,500
- **Net: Still +$12,500** ✓

**Return:**
- Capital: $100,000
- Profit: $12,500
- Time: 3 months
- **Return: 12.5% in 3 months = 50% annualized**
- **RISK-FREE (arbitrage)!** 🎯💎

**Why this is best case:**
- True arbitrage (guaranteed profit)
- Market-neutral (direction doesn't matter)
- Locked in at entry
- Zero basis risk (held to convergence)

### Best Case #4: The Mean Reversion Jackpot

**Setup:**

- **Position:** Long basis in crude oil
- Basis extremely negative (unusual)

**Historical analysis:**

- 3-month basis average: -$1.80
- Standard deviation: $0.40
- Current: -$3.50 (4.25 std dev below mean!)
- **Extremely oversold on basis**

**Entry:**
- Spot: $75
- Futures: $78.50
- **Basis: -$3.50 (record weakness)**
- Position: Long 20,000 barrels + Short 20 futures
- Capital: $200,000

**The reversion:**

**Week 1-2: Storage concerns ease**
- New pipeline capacity announced
- Basis: -$3.50 → -$3.00

**Week 3-4: Demand picks up**
- Refinery utilization increases
- Basis: -$3.00 → -$2.30

**Week 5-6: Market normalizes**
- Basis: -$2.30 → -$1.80 (back to mean!)

**Exit at mean:**

**P&L:**

Assume prices ended roughly where they started:
- Spot: $75.50 (up $0.50)
- Futures: $77.30 (down $1.20)
- **Basis: -$1.80** (strengthened from -$3.50)

**Spot:** +$0.50 × 20,000 = **+$10,000**
**Futures:** +$1.20 × 20,000 = **+$24,000**
**Net:** **+$34,000**

**Basis check:**
- Change: -$1.80 - (-$3.50) = **+$1.70**
- P&L: $1.70 × 20,000 = **+$34,000** ✓

**Return:**
- Capital: $200,000
- Profit: $34,000
- Time: 6 weeks
- **Return: 17% in 6 weeks = 148% annualized!** 🎯

**Why this is best case:**
- Entered at statistical extreme
- Mean reversion is powerful force
- Didn't need prices to move favorably
- Pure basis reversion play

### What Makes These Best Cases Work

**Common success factors:**

1. **Large basis movement:**
   - $5-$7 moves in oil
   - $0.35-$0.40 moves in grains
   - Multiple standard deviations

2. **Predictable patterns:**
   - Supply shocks strengthen basis
   - Harvest gluts weaken basis
   - Convergence to zero at expiration
   - Mean reversion from extremes

3. **Perfect timing:**
   - Enter at basis extremes
   - Exit before reversal
   - Hold through maximum movement

4. **Capital efficiency:**
   - Returns 50-150% annualized
   - Much lower risk than outright positions
   - Leverage through futures

5. **Market neutrality:**
   - Works in up or down markets
   - Only basis movement matters
   - Reduced directional risk

**The key lesson:**

Best case for basis trading ≠ massive absolute price moves

Best case = large RELATIVE price moves (basis changes)

**Professional traders focus on basis because:**
- More predictable than absolute prices
- Lower risk than directional bets
- Exploitable patterns (seasonal, mean reversion, convergence)
- **Consistent profits from market inefficiencies**

---

## Worst Case Scenarios: When Basis Trades Go Wrong

### The Nightmare: Basis Moves Against You

**What defines worst case for basis traders:**

1. Large basis movement in WRONG direction
2. Extended time (carry costs accumulate)
3. Forced liquidation (margin calls on physical position)
4. Unexpected fundamental change (thesis invalidated)
5. **Capital destruction from "safe" relative value trade**

### Worst Case #1: The Backwardation Collapse (Long Basis)

**Setup:**

- **Position:** Long basis in crude oil
- **Entry (supply tight, backwardation):**
  - Spot: $85/barrel
  - 3-month futures: $82/barrel
  - **Basis: +$3 (backwardation)**
  - Thesis: Supply shortage will worsen, basis strengthen further
  - Position: Long 20,000 barrels spot + Short 20 futures
  - Capital: $300,000

**The disaster:**

**Week 1: Unexpected announcement**
- OPEC+ announces production increase
- Strategic reserves release
- **Immediate supply flood**

**Market reaction:**
- Both prices fall, BUT
- Spot crashes faster (immediate oversupply)
- Futures fall less (future supply already expected tight)
- **Basis collapses!**

**The brutal timeline:**

**Week 2:**
- Spot: $85 → $78 (down $7)
- Futures: $82 → $79 (down $3)
- **Basis: +$3 → -$1 (weakened by $4!)**

**Week 3-4: Continued deterioration**
- Storage tanks filling
- Contango steepens
- Spot: $78 → $73
- Futures: $79 → $78
- **Basis: -$1 → -$5 (now steep contango!)**

**Forced exit (margin pressures):**

**Final (Week 4):**
- Spot: $73 (down $12 from entry)
- Futures: $78 (down $4 from entry)
- **Basis: -$5 (weakened by $8 total!)**

**The horror P&L:**

**Spot position (long):**
- Bought: $85, Forced to sell: $73
- Loss: $12/barrel × 20,000 = **-$240,000** ☠️

**Futures position (short):**
- Short: $82, Covered: $78
- Gain: $4/barrel × 20,000 = **+$80,000**

**Carry costs (4 weeks):**
- Storage: $0.50/barrel/month × 20,000 × 1 = -$10,000
- Financing: $85 × 20,000 × 0.05/12 = -$7,083
- **Total carry: -$17,083**

**Net P&L:**
- -$240,000 + $80,000 - $17,083 = **-$177,083** ☠️

**Basis check:**
- Change: -$5 - (+$3) = **-$8 (massive weakening)**
- Loss: $8 × 20,000 = **-$160,000**
- Plus carry costs: **-$177,083** ✓

**Disaster metrics:**
- Capital: $300,000
- Loss: -$177,083
- **Return: -59% in 1 month** ☠️
- Nearly wiped out!

**What went catastrophically wrong:**

1. **Wrong direction:** Basis weakened instead of strengthened
2. **Extreme move:** -$8 basis change (5+ standard deviations)
3. **Physical exposure:** Spot position has real carry costs
4. **Forced exit:** Couldn't wait for reversion
5. **Thesis destroyed:** Supply shortage → glut

### Worst Case #2: The Harvest That Didn't Happen (Short Basis)

**Setup:**

- **Position:** Short basis in corn (betting on harvest weakness)
- **Entry (August, pre-harvest):**
  - Spot: $4.50/bu
  - December futures: $4.75/bu
  - **Basis: -$0.25**
  - Thesis: Record harvest will pressure spot, weaken basis
  - Position: Short 100,000 bu spot + Long 20 futures
  - Capital: $100,000

**The disaster:**

**September: Weather catastrophe**
- Unexpected severe drought
- Crop failure across Midwest
- Yield forecasts slashed 30%

**Market panic:**

**Week 1-2:**
- Spot: $4.50 → $5.50 (up $1.00, immediate shortage)
- Futures: $4.75 → $5.30 (up $0.55, less reactive)
- **Basis: -$0.25 → +$0.20 (strengthened by $0.45!)**

**October: Harvest confirms shortage**
- Actual yields worst in 10 years
- Basis continues strengthening
- Spot: $5.50 → $6.00
- Futures: $5.30 → $5.60
- **Basis: +$0.20 → +$0.40**

**November: Forced to cover (can't deliver short spot)**
- Spot: $6.25 (up $1.75 total)
- Futures: $5.70 (up $0.95 total)
- **Basis: +$0.55 (strengthened by $0.80 total!)**

**The nightmare P&L:**

**Spot (short):**
- Short: $4.50, Forced to cover: $6.25
- Loss: $1.75/bu × 100,000 = **-$175,000** ☠️

**Futures (long):**
- Long: $4.75, Sell: $5.70
- Gain: $0.95/bu × 100,000 = **+$95,000**

**Net P&L:**
- -$175,000 + $95,000 = **-$80,000** ☠️

**Basis check:**
- Change: +$0.55 - (-$0.25) = **+$0.80 (strengthened)**
- Short basis loses from strengthening
- Loss: $0.80 × 100,000 = **-$80,000** ✓

**Disaster metrics:**
- Capital: $100,000
- Loss: -$80,000
- **Return: -80% in 3 months** ☠️
- Account nearly destroyed

**What went wrong:**

1. **Seasonal bet failed:** No harvest pressure
2. **Fundamental reversal:** Supply shortage vs. expected glut
3. **Short squeeze:** Had to cover spot at worst prices
4. **No exit plan:** Thesis invalidated but held too long

### Worst Case #3: The Convergence That Didn't (Basis Stays Wide)

**Setup:**

- **Position:** Long basis convergence trade in WTI crude
- **Entry (3 months to expiration):**
  - Spot: $75/barrel
  - Futures: $78/barrel (March contract)
  - **Basis: -$3 (steep contango)**
  - Thesis: Normal convergence to zero at expiry
  - Position: Long 10,000 barrels + Short 10 futures
  - Capital: $150,000

**The problem:**

**Month 1: Basis barely moves**
- Expected: Basis -$3 → -$2 (linear convergence)
- Actual: Basis -$3 → -$2.90 (almost no convergence)
- **Warning sign ignored**

**Month 2: Basis actually WIDENS**
- Storage glut worsens
- New supply comes online
- Basis: -$2.90 → -$3.40 (widened!)
- Spot: $74, Futures: $77.40
- **Moving AWAY from convergence!**

**Month 3: Approaching expiration, still wide**
- 1 week to expiry: Basis should be -$0.20
- Actual: -$2.80 (barely converged at all!)
- Physical delivery problems (no storage available)

**Forced to close early (can't take delivery):**
- Spot: $73.50
- Futures: $76.20 (1 week before expiry)
- **Basis: -$2.70**

**The disappointing P&L:**

**Spot:**
- Long: $75, Sell: $73.50
- Loss: $1.50/barrel × 10,000 = **-$15,000**

**Futures:**
- Short: $78, Cover: $76.20
- Gain: $1.80/barrel × 10,000 = **+$18,000**

**Carry costs (3 months):**
- Storage: $1.00/barrel × 10,000 = -$10,000
- Financing: $75 × 10,000 × 0.05 × 0.25 = -$9,375
- **Total: -$19,375**

**Net P&L:**
- -$15,000 + $18,000 - $19,375 = **-$16,375**

**Basis:**
- Expected: $0 (full convergence)
- Actual: -$2.70 (minimal convergence)
- Change: only $0.30 vs. expected $3.00
- **Convergence failed!**

**Result:**
- Expected profit: ~$30,000 (full convergence minus carry)
- Actual: **-$16,375 loss**
- **Swing: -$46,375 from expected!** ☠️

**What went wrong:**

1. **Convergence assumption failed:** Basis stayed wide
2. **Storage market broken:** Physical constraints
3. **Carry costs exceeded gains:** Time worked against trade
4. **No adjustment:** Held losing trade assuming convergence "must" happen

### Worst Case #4: The Roll Disaster (Extended Basis Trade)

**Setup:**

- **Position:** Long basis in natural gas (seasonal play)
- **Entry (Summer, for winter):**
  - Spot: $3.00/MMBtu
  - December futures: $4.50/MMBtu
  - **Basis: -$1.50 (summer contango to winter)**
  - Thesis: Winter demand will strengthen basis
  - Position: Long physical gas + Short futures
  - Capital: $100,000

**The problem: Must roll futures monthly**

**Month 1: Roll from Dec to Jan**
- Dec futures: $4.50 → $4.60
- Jan futures: $4.80 (more contango!)
- **Roll cost: $0.20/MMBtu**
- Position: 100,000 MMBtu
- Cost: $20,000

**Month 2: Roll from Jan to Feb**
- Jan: $4.70
- Feb: $4.95
- **Roll cost: $0.25/MMBtu = $25,000**

**Month 3: Roll from Feb to Mar**
- Feb: $4.85
- Mar: $5.15
- **Roll cost: $0.30/MMBtu = $30,000**

**Total roll costs: $75,000!**

**Meanwhile, basis barely strengthens:**
- Entry: -$1.50
- Exit (after 3 months): -$1.00
- Basis strengthened: $0.50
- Gross profit: $50,000

**Net P&L:**
- Basis profit: $50,000
- Roll costs: -$75,000
- Storage costs: -$10,000
- **Net: -$35,000 loss** ☠️

**What went wrong:**

1. **Persistent steep contango:** Roll costs unsustainable
2. **Multi-month hold:** Accumulated massive costs
3. **Basis moved right direction:** But not enough to cover rolls
4. **Should have exited:** After first expensive roll

### Worst Case #5: The Margin Call Death Spiral

**Setup:**

- **Position:** Long basis in copper
- **Entry:**
  - Spot: $4.00/lb
  - 3-month futures: $4.10/lb
  - Basis: -$0.10
  - Position: Long 250,000 lbs + Short 10 futures (25,000 lbs each)
  - Capital: $50,000

**The cascade:**

**Week 1: Prices crash**
- Recession fears
- Spot: $4.00 → $3.60 (down $0.40)
- Futures: $4.10 → $3.75 (down $0.35)
- Basis: -$0.10 → -$0.15 (slightly worse)

**Spot position loss:**
- $0.40 × 250,000 = **-$100,000**
- Margin call: Deposit $50,000!

**Week 2: Continued decline**
- Spot: $3.60 → $3.30
- Futures: $3.75 → $3.50
- Basis: -$0.15 → -$0.20

**Another margin call:**
- Additional $30,000 needed
- **Total deposited: $130,000** (vs. $50k initial)

**Week 3: Forced liquidation**
- Can't meet more margin calls
- Broker liquidates at $3.30 spot, $3.50 futures
- Basis: -$0.20 (barely moved from -$0.10!)

**Final P&L:**

**Spot:**
- Long $4.00, Forced out $3.30
- Loss: $0.70 × 250,000 = **-$175,000**

**Futures:**
- Short $4.10, Cover $3.50
- Gain: $0.60 × 250,000 = **+$150,000**

**Net:**
- -$175,000 + $150,000 = **-$25,000**

**Plus: Margin interest and stress:**
- Interest on $130k borrowed: -$2,000
- **Total: -$27,000**

**But here's the tragedy:**

**After forced liquidation (Week 4-6):**
- Market stabilizes
- Spot: $3.40
- Futures: $3.45
- Basis: -$0.05 (strengthened from -$0.20!)
- **If held on, would have made $37,500 profit**

**Instead:**
- Forced out at worst point
- Lost $27,000
- Missed the recovery
- **Swing: -$64,500** ☠️

**What went wrong:**

1. **Over-leveraged:** Too much position for capital
2. **Physical commodity:** Real margin calls on spot
3. **No buffer:** No cash reserves for margin
4. **Forced exit:** At worst possible time
5. **Right thesis:** But couldn't survive the volatility

### Common Worst-Case Themes

**Why basis trades blow up:**

1. **Wrong direction (most common):**
   - Basis strengthens when you're short basis
   - Basis weakens when you're long basis
   - **Fundamental thesis wrong**

2. **Carry costs exceed profits:**
   - Storage, financing, insurance add up
   - Especially in extended trades
   - **Time enemy of physical positions**

3. **Roll costs in contango:**
   - Long physical + rolling short futures
   - Bleeding money every roll
   - **Death by thousand cuts**

4. **Convergence failure:**
   - Basis doesn't converge as expected
   - Market structure broken
   - **Theory doesn't match reality**

5. **Margin pressure:**
   - Physical commodity positions need real capital
   - Large price moves trigger calls
   - **Forced exit at worst time**

6. **Thesis invalidation:**
   - Expected event doesn't happen
   - Opposite event occurs
   - **Hold losing trade hoping for reversal**

### Preventing Worst Cases

**Risk management essentials:**

1. **Position sizing:**
   - Never use full capital for margin
   - Keep 50% cash buffer
   - **Survive adverse moves**

2. **Stop losses:**
   - Exit if basis moves 1.5-2× against you
   - Example: Enter at -$2.00, stop at -$3.50
   - **Don't let small loss become large**

3. **Time limits:**
   - Set maximum holding period
   - If no progress by halfway point → Exit
   - **Don't let carry costs accumulate**

4. **Monitor convergence:**
   - If convergence tracking poorly → Exit early
   - Don't assume it "must" converge
   - **Reality trumps theory**

5. **Have exit plan:**
   - Know conditions for stopping out
   - Execute mechanically
   - **Don't hope, act**

**Remember:** Basis trades seem "safe" (market-neutral), but can still destroy capital if mismanaged!

---

## What to Remember

### Core Concept

**Basis trading profits from the difference between spot and futures prices:**

$$
\text{Basis} = S_t - F_t
$$

**Two fundamental trades:**

**Long basis:**
$$
\text{Long Spot} + \text{Short Futures} \quad \rightarrow \quad \text{Profit if basis strengthens}
$$

**Short basis:**
$$
\text{Short Spot} + \text{Long Futures} \quad \rightarrow \quad \text{Profit if basis weakens}
$$

### Why Basis Exists

**Carry costs:**
$$
F = S \cdot e^{(r+u-y)(T-t)}
$$

- $r$ = Interest rate
- $u$ = Storage cost
- $y$ = Convenience yield

**Normal contango:** $F > S$ (basis negative)
**Backwardation:** $S > F$ (basis positive)

### The Convergence Guarantee

$$
\lim_{t \to T} \text{Basis}_t = 0
$$

- At expiration: Spot = Futures
- Creates predictable profit opportunity
- **Foundation of convergence trades**

### Market Neutral Nature

**Key insight:**
- Basis trades profit from RELATIVE moves
- Don't care if absolute prices rise or fall
- Only care about spread change

**Example:**
- Prices up 10%: Can profit if basis strengthens
- Prices down 10%: Still profit if basis strengthens
- **Direction-independent returns**

### Common Basis Patterns

**Seasonality (agriculture):**
- Harvest: Basis weakest (spot pressure)
- Post-harvest: Basis strengthens (storage costs)

**Supply shocks:**
- Shortage → Basis strengthens (backwardation)
- Glut → Basis weakens (contango steepens)

**Convergence:**
- Basis → 0 as expiration approaches
- Predictable pattern

### Entry Strategies

**Convergence trade:**
- Enter when basis negative (contango)
- Hold to expiration
- Profit from convergence to zero

**Mean reversion:**
- Enter when basis at extremes (>2 std dev)
- Exit when returns to mean
- Statistical edge

**Seasonal:**
- Agricultural: Short basis before harvest
- Energy: Trade winter/summer patterns

**Arbitrage:**
- When basis outside fair value bounds
- Lock in riskless profit
- True arbitrage opportunity

### Exit Strategies

**Target profit:**
- Set basis change target
- Exit when reached
- Don't be greedy

**Stop loss:**
- Exit if basis moves against by X
- Preserve capital
- Live to trade another day

**Time stop:**
- Exit if no progress after Y days
- Avoid excessive carry costs

**Convergence:**
- Hold to expiration for full convergence
- Guaranteed (but ties up capital)

### Maximum Profit Scenarios

**Best case (long basis):**
- Supply shock strengthens basis dramatically
- $5-$7 moves in oil
- 50-150% returns possible
- Market-neutral to direction

**Best case (arbitrage):**
- True mispricing
- Lock in profit at entry
- Riskless return
- Perfect hedge

### Maximum Loss Scenarios

**Worst case (wrong direction):**
- Basis moves opposite of prediction
- Large adverse move (multiple std dev)
- -50% to -80% losses possible
- **Position sizing prevents disaster**

**Worst case (carry bleed):**
- Hold too long
- Carry costs exceed basis profit
- Roll costs in contango
- **Time stops prevent this**

**Worst case (forced exit):**
- Margin calls on physical position
- Liquidated at worst prices
- Right thesis but couldn't survive
- **Capital buffer essential**

### Risk Management

**Position sizing:**
$$
\text{Max Position} = \text{Capital} \times 0.50 / \text{Margin per Unit}
$$

- Use only 50% of capital
- Keep buffer for adverse moves

**Stop losses:**
- Basis moves 1.5-2× against → Exit
- Example: Long at -$2.00, stop at -$3.50
- Non-negotiable

**Carry cost awareness:**
- Calculate full carrying costs
- Storage + financing + insurance
- Must overcome these to profit

**Time management:**
- Set maximum hold period
- Monitor convergence progress
- Exit if not tracking

### Common Mistakes

1. Over-leveraging (using all capital for margin)
2. No stop loss (hoping for reversal)
3. Ignoring carry costs (time bleeds value)
4. Holding losers (thesis invalidated but hoping)
5. Not monitoring convergence (assuming it "must" happen)
6. Rolling in steep contango (death spiral)
7. Treating as "safe" (market-neutral ≠ risk-free)

### Comparison to Other Strategies

| Strategy | Direction Risk | Basis Risk | Carry Cost | Convergence |
|----------|---------------|------------|------------|-------------|
| Long spot | YES (high) | NO | HIGH | NO |
| Long futures | YES (high) | NO | NONE | YES (expiry) |
| **Basis trade** | **NO** | **YES** | **HIGH** | **YES** |
| Hedged producer | NO | YES (same as basis) | Varies | YES |

**Basis trade = Pure relative value**

### When to Trade Basis

**Trade when:**
- Strong conviction on basis direction
- Pattern is reliable (seasonal, convergence)
- Can handle carry costs
- Have capital buffer for margin

**Don't trade when:**
- Better directional opportunity exists
- Can't handle carry costs
- Insufficient capital buffer
- Basis pattern breaking down

### Key Success Factors

**The professionals' checklist:**

1. ✓ **Size appropriately** (50% capital max)
2. ✓ **Set stops** (1.5-2× adverse move)
3. ✓ **Calculate carry** (know full costs)
4. ✓ **Monitor convergence** (track progress)
5. ✓ **Have exit plan** (profit target, stop, time)
6. ✓ **Understand fundamentals** (why basis moves)
7. ✓ **Keep capital buffer** (survive adverse moves)

### The Fundamental Truth

**Basis trading is NOT:**
- Speculation on price direction
- A free lunch
- Risk-free arbitrage (usually)
- Suitable for everyone

**Basis trading IS:**
- Relative value strategy
- Market-neutral to absolute price
- Requiring capital for carry costs
- Demanding discipline and risk management

### Final Wisdom

> "Basis trading is the purest form of commodity market efficiency arbitrage. You're not betting on whether oil goes to $80 or $70—you're betting on whether spot and futures maintain their proper relationship. It's market-neutral, it's predictable in aggregate, and it can generate consistent returns. But it's not magic: carry costs are real, margin calls hurt, and basis can stay irrational longer than you can stay solvent. Trade it small, trade it disciplined, and never forget that 'market-neutral' doesn't mean 'risk-free'."

**Key principles:**

- Basis converges to zero (guarantee)
- Carry costs must be overcome (reality)
- Position sizing prevents disasters (survival)
- Stop losses protect capital (discipline)
- Time can be enemy or friend (understand convergence)
- **Trade the spread, not the direction** (core insight)

**Most important:**

Basis trading is a professional strategy requiring:
- Deep understanding of commodity markets
- Access to physical commodity (or proxies)
- Substantial capital for carry costs
- Disciplined risk management
- **Patience and precision, not speculation** 🎯📊
