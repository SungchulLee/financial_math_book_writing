# Commodity Seasonality Trading

**Commodity seasonality trading** is a futures strategy that exploits predictable annual price patterns driven by crop cycles, weather patterns, demand variations, and storage costs, profiting from statistically significant recurring price movements that repeat each calendar year.

---

## The Core Insight

**The fundamental idea:**

- Commodity prices follow predictable annual cycles
- Agricultural commodities driven by planting/harvest schedules
- Energy commodities driven by heating/cooling demand
- Livestock follows biological breeding cycles
- These patterns repeat year after year (statistical edge)
- Can identify high-probability entry/exit windows
- Combine seasonal tendency with fundamentals
- Multi-decade data validates patterns
- Market structure creates self-reinforcing cycles

**The key equations:**

$$
\text{Seasonal Pattern} = \mathbb{E}[\text{Price}_{\text{month } t}] - \mathbb{E}[\text{Price}_{\text{annual}}]
$$

$$
\text{Seasonal Index}_t = \frac{\text{Average Price}_{\text{month } t}}{\text{Average Price}_{\text{annual}}} \times 100
$$

$$
\text{Win Rate}_{\text{seasonal}} = \frac{\text{Years with Expected Pattern}}{\text{Total Years}} > 70\%
$$

**You're essentially betting: "Historical price patterns driven by physical supply/demand cycles will repeat this year, allowing me to position ahead of predictable moves and profit from statistically validated seasonal tendencies."**

---

## What Are Commodity Seasonals?

**Before trading seasonal patterns, understand the fundamental mechanics:**

### 1. Types of Seasonal Drivers

**1. Agricultural Crop Cycles:**

The most reliable seasonals:

**Planting season (Spring):**

$$
\text{Uncertainty} \uparrow \Rightarrow \text{Prices} \uparrow
$$

- Will crop be planted successfully?
- Weather concerns
- Acreage uncertainty
- **Premium for uncertainty**

**Growing season (Summer):**

$$
\text{Weather Risk} \uparrow \Rightarrow \text{Volatility} \uparrow
$$

- Drought risk (June-August)
- Flood risk
- Pest pressure
- **Weather market premium**

**Harvest season (Fall):**

$$
\text{Supply} \uparrow \Rightarrow \text{Prices} \downarrow
$$

- Abundant supply hits market
- Storage begins
- Sell pressure
- **Harvest lows typical**

**Storage season (Winter):**

$$
\text{Carry Cost} \Rightarrow \text{Gradual Price Rise}
$$

- Holding inventory costs money
- Contango from storage
- Steady demand
- **Post-harvest recovery**

**2. Energy Demand Cycles:**

**Natural Gas:**

$$
\text{Heating Demand (Winter)} \gg \text{Cooling Demand (Summer)}
$$

**Seasonal pattern:**

- Oct-Mar: High demand (heating)
- Apr-Sep: Low demand (injection season)
- **Classic winter premium**

**Gasoline:**

$$
\text{Driving Season (Summer)} \gg \text{Winter Demand}
$$

**Seasonal pattern:**

- May-Sep: High demand (driving)
- Oct-Apr: Lower demand
- **Summer premium**

**Crude Oil:**

$$
\text{Refinery Demand} = f(\text{Product Demand})
$$

**Seasonal pattern:**

- Mar-May: Refinery turnarounds (low demand)
- Jun-Aug: Summer gasoline (high demand)
- Sep-Nov: Shoulder season
- Dec-Feb: Winter heating oil
- **Product-driven seasonality**

**3. Livestock Breeding Cycles:**

**Cattle cycle:**

$$
\text{Biological Constraints} \Rightarrow \text{Production Cycles}
$$

- Calves born: Spring
- Fed to market weight: 18-24 months
- Peak marketing: Summer/Fall
- **Biological seasonality**

**Hog cycle:**

$$
\text{Farrow-to-Finish} = 10 \text{ months}
$$

- Sows breed: Fall/Winter
- Piglets born: Winter/Spring
- Market ready: Summer/Fall
- **Shorter cycle than cattle**

**4. Weather-Driven Patterns:**

**Coffee (Brazilian frost risk):**

- Jun-Aug: Winter in Brazil (frost risk)
- Price premium during risk period
- Collapses after safe passage
- **Weather insurance premium**

**Cocoa (West Africa monsoon):**

- Apr-Sep: Main crop (wet season)
- Oct-Mar: Mid-crop
- **Monsoon critical**

**Sugar (Hurricane season):**

- Jun-Nov: Atlantic hurricanes
- Threatens cane production
- Price volatility increases
- **Disaster risk premium**

### 2. Example

**Annual cycle:**

| Month | Activity | Typical Price | Reason |
|-------|----------|--------------|--------|
| Jan-Feb | Winter | Neutral | Storage, steady demand |
| Mar-Apr | Planting | Rising | Planting uncertainty |
| May-Jun | Early growing | Peak | Weather market begins |
| Jul-Aug | Pollination | Volatile | Critical weather period |
| Sep-Oct | Harvest | Lowest | Supply flood |
| Nov-Dec | Post-harvest | Rising | Storage costs |

**Statistical pattern (30-year average):**

$$
\text{Corn Price}_{\text{June}} > \text{Corn Price}_{\text{October}} \quad (85\% \text{ of years})
$$

**Seasonal trade:**

- Long corn: February
- Exit: Late June (pre-harvest pressure)
- Hold through weather market
- **Capture spring rally**

**Historical win rate: 73% (22 of 30 years)**

### 3. Example

**Annual cycle:**

| Month | Activity | Demand | Price Pattern |
|-------|----------|--------|---------------|
| Jan-Feb | Peak winter | Very High | Peak prices |
| Mar-Apr | Shoulder | Declining | Falling |
| May-Sep | Injection season | Low (storage) | Lows |
| Oct | Pre-winter | Building | Rising |
| Nov-Dec | Early winter | High (heating) | Rising |

**Injection season (Apr-Oct):**

$$
\text{Storage Builds} \Rightarrow \text{Prices Decline}
$$

- Weekly EIA reports show builds
- Supply > Demand
- Inventory accumulation
- **Bearish pressure**

**Withdrawal season (Nov-Mar):**

$$
\text{Storage Draws} \Rightarrow \text{Prices Rise}
$$

- Heating demand exceeds production
- Weekly inventory declines
- Supply tightens
- **Bullish pressure**

**Seasonal trade:**

- Short natural gas: March
- Cover: September (injection season end)
- Capture summer decline
- **Historical win rate: 67%**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/commodity_seasonality.png?raw=true" alt="commodity_seasonality" width="700">
</p>
**Figure 1:** Commodity seasonality patterns showing corn's spring planting rally and fall harvest decline, natural gas winter heating demand premium and summer injection season lows, and cattle's biological production cycle. These patterns repeat annually with 65-85% reliability, creating statistical edges for informed traders.

---

## Economic Interpretation

**Beyond the patterns, understanding the economic forces:**

### 1. Agricultural Seasonals as Risk Premiums

**The deep insight:**

Agricultural seasonals represent **risk transfer** from farmers to speculators. Farmers need to lock in prices during growing season (maximum uncertainty). Speculators demand premium to bear this risk. After harvest (no more risk), premium disappears.

**Formal representation:**

$$
\text{Pre-Harvest Price} = \mathbb{E}[\text{Harvest Price}] + \text{Weather Risk Premium}
$$

**Weather risk premium:**

$$
\text{Premium} = \lambda \times \sigma_{\text{yield}} \times \text{Days to Harvest}
$$

Where:
- $\lambda$ = risk aversion coefficient
- $\sigma_{\text{yield}}$ = yield uncertainty
- Days to harvest = time until risk resolves

**Example: Corn in June**

$$
\text{June Corn} = \mathbb{E}[\text{October Harvest}] + \$0.50\text{-}\$1.00/\text{bushel}
$$

**Why premium exists:**

**Farmer perspective:**

- Planted corn in May
- Yield unknown (weather dependent)
- Need to lock in revenue
- **Willing to accept lower price for certainty**

**Speculator perspective:**

- Bear weather risk
- If drought: Prices spike, short loses
- If perfect weather: Prices fall, short wins
- **Demand premium for risk**

**Premium decays as harvest approaches:**

$$
\frac{d(\text{Premium})}{dt} < 0
$$

**June to October:**

- June: $1.00/bushel premium (maximum uncertainty)
- August: $0.50/bushel (weather largely known)
- October: $0 (harvest complete, no uncertainty)
- **Time decay of risk premium**

### 2. Storage Economics and Carry

**Post-harvest seasonality driven by storage costs:**

$$
\text{Futures Price} = \text{Spot Price} + \text{Storage Cost} + \text{Interest} - \text{Convenience Yield}
$$

**November to June (storage period):**

$$
\text{Price}_{\text{June}} = \text{Price}_{\text{Nov}} + 8 \text{ months storage}
$$

**Storage cost:**

$$
\text{Storage} \approx 3\text{-}5¢/\text{bushel/month}
$$

**Total 8-month carry:**

$$
8 \times 4¢ = 32¢/\text{bushel}
$$

**But actual appreciation:**

$$
\text{June Price} - \text{Nov Price} \approx 15\text{-}25¢ \quad \text{(less than full carry)}
$$

**Why less than full carry:**

- Convenience yield (having grain available)
- Expected new crop supply
- Demand seasonality
- **Partial recovery from harvest lows**

**This creates opportunity:**

**Calendar spread:**

- Long Nov-June spread (buy Nov, sell June)
- Expect 20¢ widening
- Actual cost of carry: 32¢
- **Spread underpriced if < 32¢**

### 3. Energy Seasonals as Demand Cycles

**Natural gas winter premium:**

**Heating degree days (HDD):**

$$
\text{HDD} = \sum \max(65°F - \text{Daily Avg Temp}, 0)
$$

**Gas demand:**

$$
\text{Demand} = \beta_0 + \beta_1 \times \text{HDD} + \epsilon
$$

Where $\beta_1 \approx 30$ Bcf/day per 1,000 HDD

**Example:**

**Summer (HDD ≈ 0):**

- Baseline demand: 60 Bcf/day
- Price: $2.50/MMBtu

**Winter (HDD ≈ 2,000):**

- Demand: 60 + (30 × 2) = 120 Bcf/day
- Price: $4.50/MMBtu
- **80% increase from demand seasonality**

**Supply relatively constant:**

- Production: ~90 Bcf/day year-round
- Difference met by storage withdrawals
- **Storage cycle drives prices**

**Inventory dynamics:**

$$
\frac{d(\text{Inventory})}{dt} = \text{Production} + \text{Imports} - \text{Demand}
$$

**Injection season (Apr-Oct):**

$$
\frac{d(\text{Inventory})}{dt} > 0 \Rightarrow \text{Prices Fall}
$$

**Withdrawal season (Nov-Mar):**

$$
\frac{d(\text{Inventory})}{dt} < 0 \Rightarrow \text{Prices Rise}
$$

**Self-reinforcing cycle:**

- Low prices → Producers reduce output
- High prices → Producers increase output
- **But with lag, perpetuating seasonality**

### 4. Livestock Biological Constraints

**Cattle cycle is biological, not discretionary:**

**Breeding dynamics:**

$$
\text{Heifers} \to \text{(9 months gestation)} \to \text{Calves} \to \text{(18-24 months)} \to \text{Market}
$$

**Total cycle: 27-33 months minimum**

**Cannot be accelerated!**

**Seasonal marketing pattern:**

**Spring calving (Feb-May):**

- Calves born
- Abundant grass (Spring)
- **Biological timing**

**Fall marketing (Sep-Nov):**

- Calves reach market weight
- Pastures drying out (Winter approaching)
- **Sell before winter feed costs**

**Price seasonality:**

$$
\text{Cattle Prices}_{\text{Spring}} > \text{Cattle Prices}_{\text{Fall}} \quad (75\% \text{ of years})
$$

**Why:**

- Spring: Tight supply (last year's cattle gone)
- Summer: Building supply (new calves growing)
- Fall: Peak supply (mass marketing)
- Winter: Supply tightens again
- **Biological production cycle**

**Hog cycle similar but faster:**

$$
\text{Breeding} \to \text{(4 months gestation)} \to \text{Piglets} \to \text{(6 months)} \to \text{Market}
$$

**Total: 10 months**

**But seasonal pattern still strong:**

- Breeding: Fall/Winter (indoor, controlled)
- Farrowing: Winter/Spring
- Marketing: Summer/Fall
- **70% win rate on seasonal trades**

### 5. Why Seasonals Persist

**Market participants can't eliminate seasonality:**

**1. Physical constraints:**

- Can't grow corn in winter (Northern Hemisphere)
- Can't speed up cattle gestation
- Can't eliminate heating demand in winter
- **Nature imposes cycles**

**2. Storage costs:**

- Carrying grain is expensive
- Can't store natural gas infinitely (capacity limits)
- Live cattle can't be "stored" (costs money to feed)
- **Economics limit arbitrage**

**3. Risk aversion:**

- Farmers must plant before knowing yield
- Speculators demand premium for risk
- Risk premium component persists
- **Behavioral component**

**4. Coordination failures:**

- Farmers plant in spring (all together)
- Creates synchronized supply
- Individual incentive ≠ collective optimal
- **Game theory prevents arbitrage**

**Historical evidence:**

$$
\text{Corn seasonal pattern (1960-2024): } 73\% \text{ win rate}
$$

$$
\text{Nat gas seasonal pattern (1995-2024): } 67\% \text{ win rate}
$$

**Over 60+ years for ag, 30+ years for energy, patterns persist!**

---

## Key Terminology

**Seasonality:**

$$
\text{Seasonal Pattern} = \text{Recurring Annual Price Behavior}
$$

- Predictable price movements tied to calendar
- Driven by crop cycles, weather, demand
- Repeats year after year
- Measurable statistical edge

**Seasonal Index:**

$$
\text{Index}_{\text{month}} = \frac{\text{Avg Price}_{\text{month}}}{\text{Avg Price}_{\text{annual}}} \times 100
$$

- Normalized price for each month
- Index > 100: Typically high month
- Index < 100: Typically low month
- **Comparison tool**

**Planting Season:**

- Spring months (Mar-May for corn/beans)
- Maximum uncertainty about crop size
- Prices typically rise
- **Risk premium period**

**Growing Season:**

- Summer months (Jun-Aug for corn/beans)
- Weather market dominant
- High volatility
- **Critical period**

**Harvest Season:**

- Fall months (Sep-Nov for corn/beans)
- Supply floods market
- Prices typically fall
- **Seasonal lows**

**Storage Season:**

- Winter months (Dec-Feb for grains)
- Inventory holding costs
- Gradual price appreciation
- **Carry costs dominate**

**Weather Market:**

- Jun-Aug for corn (pollination)
- Apr-Jun for wheat (maturation)
- Weather critically affects yield
- **High volatility period**

**Injection Season (Natural Gas):**

$$
\text{Apr-Oct: } \text{Production} > \text{Demand}
$$

- Surplus gas goes to storage
- Inventory builds
- Prices typically decline
- **Bearish seasonal**

**Withdrawal Season (Natural Gas):**

$$
\text{Nov-Mar: } \text{Demand} > \text{Production}
$$

- Storage provides supply
- Inventory declines
- Prices typically rise
- **Bullish seasonal**

**Driving Season (Gasoline):**

- Memorial Day to Labor Day
- Peak vacation travel
- High gasoline demand
- **Summer premium**

**Heating Season (Heating Oil/Nat Gas):**

- Nov-Mar (winter months)
- Heating demand dominates
- Prices typically elevated
- **Winter premium**

**Cattle Cycle:**

- 27-33 month biological production cycle
- Spring calving, fall marketing
- Predictable inventory patterns
- **Multi-year seasonality**

**Win Rate (Seasonal):**

$$
\text{Win Rate} = \frac{\text{Years Pattern Worked}}{\text{Total Years}}
$$

- Percentage of years seasonal held
- Strong seasonal: >70%
- Moderate seasonal: 60-70%
- Weak seasonal: <60%

**Seasonal Window:**

- Optimal entry/exit dates
- Based on historical analysis
- E.g., "Long corn Feb 15 to Jun 25"
- **Trading calendar**

**Counter-Seasonal:**

- Trading against typical pattern
- Used when fundamentals override
- Lower win rate
- **Higher risk/reward**

---

## The Greeks

**While seasonality isn't options, we can define analogous sensitivities:**

### 1. Delta

**Definition:** Sensitivity of position to absolute price moves.

**Seasonal trades are DIRECTIONAL:**

$$
\Delta_{\text{seasonal long}} = +1.0 \quad \text{(full directional exposure)}
$$

**Example (Long corn seasonal):**

- Long 10 corn contracts
- Corn rises $1/bushel
- P&L: +$1 × 5,000 × 10 = **+$50,000**

**Unlike spreads (delta-neutral), seasonals are pure directional bets!**

**Risk management:**

Since full delta exposure:

- Use smaller position sizes
- Tight stops
- Diversify across commodities
- **Manage directional risk**

### 2. Gamma (Acceleration)

**Definition:** How delta changes as price moves.

$$
\Gamma_{\text{futures}} = 0 \quad \text{(linear instruments)}
$$

**Futures have no gamma:**

- Delta always 1.0
- No convexity
- **Simpler than options**

**But effective gamma from volatility:**

**Weather market (Jun-Aug corn):**

- Normal move: ±2% daily
- Drought fear: ±5% daily
- Volatility doubles
- **"Effective gamma" from vol change**

**Management: Reduce size during high-vol periods**

### 3. Theta

**Definition:** How edge changes as season progresses.

$$
\Theta_{\text{seasonal}} = \frac{\partial P(\text{Pattern Holds})}{\partial t}
$$

**Seasonal theta is POSITIVE in window:**

**Example (Corn seasonal):**

- Entry: Feb 15
- Exit target: Jun 25
- Days in trade: 130

**Daily theta:**

- Feb 15: P(win) = 73% (historical)
- Jun 1: P(win) declining (harvest approaching)
- Jun 25: Exit (theta expires)

**Peak seasonal strength:**

- Apr-May (planting/early growing)
- Maximum uncertainty
- **Highest edge period**

**Theta decay analogy:**

As harvest approaches:

- Weather risk resolves
- Crop size becomes known
- Seasonal edge dissipates
- **Exit before theta decay**

### 4. Vega

**Definition:** Sensitivity to volatility changes.

**Seasonal trades benefit from volatility:**

$$
\text{Vega}_{\text{seasonal}} > 0 \quad \text{(long volatility)}
$$

**Why:**

**Weather market increases volatility:**

- June drought scare
- Corn volatility: 15% → 40%
- Prices spike
- Long corn benefits
- **Volatility = friend**

**Example:**

**Normal year:**

- Corn: $5.50 → $6.20 (+13%)
- Profit: $0.70/bushel
- **Theta-driven**

**Drought year:**

- Corn: $5.50 → $8.00 (+45%)
- Profit: $2.50/bushel
- **Volatility-driven**

**Long seasonals = long vol exposure**

### 5. Rho

**Definition:** Sensitivity to interest rate changes.

$$
\rho_{\text{futures}} \approx 0 \quad \text{(minimal)}
$$

**Futures have minimal rate sensitivity:**

- Marked to market daily
- No carry to expiration
- **Ignore for seasonals**

**Exception: Financing costs for physical storage**

Higher rates → higher carry costs → steeper contango:

- Affects calendar spreads
- Not directional seasonals
- **Secondary effect**

### 6. Fundamental Sensitivity (Unique to Seasonals)

**Definition:** Sensitivity to fundamental supply/demand changes.

$$
\beta_{\text{fundamentals}} = \frac{\partial \text{Seasonal Edge}}{\partial \text{Supply/Demand Shock}}
$$

**Seasonals can be overwhelmed by fundamentals:**

**Example: 2012 Drought**

**Normal corn seasonal:**

- Long Feb → Jun
- Expected: +10-15%
- Win rate: 73%

**2012 (worst drought in 50 years):**

- Long Feb → Jun
- Actual: +50% (massive rally)
- **Fundamentals amplified seasonal**

**Counter-example: Massive surplus**

**2016 Record Crop:**

- Long Feb → Jun (seasonal)
- Expected: +10-15%
- Actual: -5% (down)
- **Fundamentals overpowered seasonal**

**Lesson: Seasonals work best when fundamentals neutral**

$$
\text{Best case: } \text{Seasonal} + \text{Neutral Fundamentals}
$$

$$
\text{Great case: } \text{Seasonal} + \text{Supporting Fundamentals}
$$

$$
\text{Disaster: } \text{Seasonal} + \text{Opposing Fundamentals}
$$

---

## Seasonal Selection

**Not all seasonals are created equal. Selection criteria:**

### 1. Strongest Agricultural Seasonals

**Corn: Feb-Jun Long**

**Pattern:**

- Entry: Mid-February
- Exit: Late June
- Duration: ~4.5 months
- Historical win rate: **73%** (22 of 30 years)

**Economic driver:**

- Planting uncertainty (Apr-May)
- Early growing weather (Jun)
- Pre-harvest risk premium
- **Strongest ag seasonal**

**Average return:**

- Winners: +18% avg
- Losers: -8% avg
- Expectancy: +10.5% over 4.5 months
- **Annualized: 28%**

**When to skip:**

- Massive carryover (abundant supply)
- South American bumper crop
- Demand destruction (ethanol mandate change)
- **Fundamental override**

**Soybeans: Jan-May Long**

**Pattern:**

- Entry: Early January
- Exit: Mid-May
- Duration: ~4.5 months
- Historical win rate: **70%** (21 of 30 years)

**Economic driver:**

- South American weather (Jan-Feb)
- US planting intentions (Mar)
- Early growing (May)
- **Global supply concerns**

**Average return:**

- Winners: +22% avg
- Losers: -10% avg
- Expectancy: +11.4%
- **Very profitable**

**When to skip:**

- Record South American crop
- China demand collapse
- Large US stocks
- **Watch fundamentals**

**Wheat: Dec-Mar Long**

**Pattern:**

- Entry: Early December
- Exit: Late March
- Duration: ~4 months
- Historical win rate: **67%** (20 of 30 years)

**Economic driver:**

- Winter wheat dormancy concerns
- Spring thaw damage risk
- Russian/Black Sea supply concerns
- **Winter survival premium**

**Average return:**

- Winners: +15% avg
- Losers: -9% avg
- Expectancy: +7.1%
- **Moderate returns**

### 2. Strongest Energy Seasonals

**Natural Gas: Mar-Sep Short**

**Pattern:**

- Entry: Early March
- Exit: Late September
- Duration: ~7 months
- Historical win rate: **67%** (20 of 30 years)

**Economic driver:**

- Injection season (Apr-Oct)
- Low heating demand
- Storage builds
- **Bearish seasonal**

**Average return:**

- Winners: -35% avg (short = profit from decline)
- Losers: +20% avg
- Expectancy: +16.5%
- **Excellent short opportunity**

**When to skip:**

- Low storage levels (<1.5 Tcf)
- Production declines (rig count down)
- Cold summer forecast (AC demand)
- **Supply/demand override**

**Gasoline (RBOB): Feb-Jun Long**

**Pattern:**

- Entry: Mid-February
- Exit: Early June
- Duration: ~3.5 months
- Historical win rate: **68%** (23 of 34 years)

**Economic driver:**

- Refinery turnarounds complete (Mar)
- Driving season approaching
- Summer blend transition
- **Demand anticipation**

**Average return:**

- Winners: +25% avg
- Losers: -12% avg
- Expectancy: +12.0%
- **Strong seasonal**

**When to skip:**

- Crude oil in strong bear market
- Refinery capacity increased
- EV adoption accelerating (long-term)
- **Watch crude correlation**

### 3. Strongest Livestock Seasonals

**Live Cattle: Feb-Jun Long**

**Pattern:**

- Entry: Late February
- Exit: Early June
- Duration: ~3.5 months
- Historical win rate: **71%** (25 of 35 years)

**Economic driver:**

- Spring BBQ demand building
- Tight cattle supplies (multi-year cycle)
- Grass-fed cattle coming to market
- **Demand > supply**

**Average return:**

- Winners: +14% avg
- Losers: -7% avg
- Expectancy: +8.0%
- **Reliable pattern**

**Lean Hogs: Jun-Aug Long**

**Pattern:**

- Entry: Early June
- Exit: Late August
- Duration: ~3 months
- Historical win rate: **68%** (20 of 30 years)

**Economic driver:**

- Summer grilling season
- Tight supply (10-month cycle low point)
- Corn prices declining (lower feed costs)
- **Demand + favorable costs**

**Average return:**

- Winners: +18% avg
- Losers: -10% avg
- Expectancy: +8.2%
- **Good summer trade**

### 4. Comparison Table

| Commodity | Entry | Exit | Duration | Win Rate | Avg Return | Best Fit |
|-----------|-------|------|----------|----------|------------|----------|
| Corn | Mid-Feb | Late Jun | 4.5 mo | 73% | +10.5% | Most reliable |
| Soybeans | Early Jan | Mid-May | 4.5 mo | 70% | +11.4% | High return |
| Wheat | Early Dec | Late Mar | 4 mo | 67% | +7.1% | Moderate |
| Nat Gas (short) | Early Mar | Late Sep | 7 mo | 67% | +16.5% | Best short |
| Gasoline | Mid-Feb | Early Jun | 3.5 mo | 68% | +12.0% | Strong |
| Cattle | Late Feb | Early Jun | 3.5 mo | 71% | +8.0% | Consistent |
| Hogs | Early Jun | Late Aug | 3 mo | 68% | +8.2% | Summer trade |

**Beginner recommendation: Start with corn Feb-Jun (most reliable, 73% win rate, well-studied)**

---

## Time Selection

**Precise timing is critical for seasonal trades:**

### 1. Entry Timing Methodology

**Statistical approach:**

$$
\text{Entry Date} = \arg\max_t \left( \frac{\mathbb{E}[\text{Profit}_{t \to \text{exit}}]}{\sigma[\text{Profit}]} \right)
$$

**Translation: Enter when risk-adjusted expected return is maximized**

**Example (Corn seasonal):**

**Test different entry dates (30-year backtest):**

| Entry Date | Avg Return | Std Dev | Sharpe | Win Rate |
|------------|-----------|---------|--------|----------|
| Jan 15 | +8.2% | 14% | 0.59 | 67% |
| Feb 1 | +10.1% | 13% | 0.78 | 70% |
| **Feb 15** | **+10.5%** | **12%** | **0.88** | **73%** |
| Mar 1 | +9.8% | 13% | 0.75 | 70% |
| Mar 15 | +8.5% | 14% | 0.61 | 67% |

**Feb 15 is optimal: Best Sharpe ratio + highest win rate**

**Exit Timing Methodology:**

$$
\text{Exit Date} = \arg\max_t \left( \text{Cumulative Return} \right)
$$

**Test different exit dates:**

| Exit Date | Avg Return | Win Rate |
|-----------|-----------|----------|
| May 31 | +9.2% | 73% |
| Jun 15 | +10.1% | 73% |
| **Jun 25** | **+10.5%** | **73%** |
| Jul 1 | +10.0% | 70% |
| Jul 15 | +8.8% | 67% |

**Jun 25 is optimal: Peak return before harvest pressure**

### 2. Fundamental Confirmation

**Don't enter blindly on calendar date:**

**Pre-entry checklist:**

**1. Inventory levels:**

$$
\text{If Stocks/Use} < 15\% \Rightarrow \text{Bullish}
$$

**Example (Corn):**

- Feb 1 USDA report: Stocks = 8.5 billion bushels
- Usage: 14.5 billion bushels/year
- Stocks/Use = 8.5/14.5 = 59% (abundant)
- **Caution: May override seasonal**

**2. Planting intentions:**

$$
\text{If Acres}_{\text{intended}} > \text{Acres}_{\text{trend}} \Rightarrow \text{Bearish}
$$

**Example:**

- March USDA: 92 million acres corn
- Trend: 88 million acres
- +4.5% above trend
- **Caution: Large crop coming**

**3. South American crop:**

$$
\text{If SA Crop} > \text{Average} + 10\% \Rightarrow \text{Bearish}
$$

**Example (Soybeans):**

- Brazil/Argentina crop: 185 MMT
- Average: 165 MMT
- +12% above average
- **May pressure US seasonal**

**Decision matrix:**

| Stocks/Use | Planting | SA Crop | Enter Seasonal? |
|-----------|----------|---------|-----------------|
| Tight (<20%) | Normal | Normal | YES (strong) |
| Normal | Normal | Normal | YES (standard) |
| Abundant (>30%) | High | Large | NO (skip year) |

### 3. Weather Override Signals

**Exit early if weather normalizes:**

**Corn seasonal (Feb-Jun):**

**Normal progression:**

- Feb-Mar: Planting uncertainty premium
- Apr-May: Planting weather concerns
- Jun: Early growing, pollination upcoming
- **Exit late Jun before harvest pressure**

**Early exit triggers:**

**Perfect planting weather (April):**

- Moisture adequate
- Temperatures ideal
- Planting 90% complete vs 70% average
- **Uncertainty resolved early**

**Decision:** Exit early (May 1 instead of Jun 25)

**Rationale:**

- Seasonal edge was uncertainty premium
- Uncertainty gone
- Don't hold for harvest pressure
- **Lock profits**

**Late exit extension:**

**Drought developing (June):**

- GFS model: Hot/dry 2-week forecast
- Soil moisture declining
- Crop stress visible
- **Weather market escalating**

**Decision:** Hold through June (maybe to Jul 15)

**Rationale:**

- New risk premium emerging
- Weather market can spike prices
- Extend beyond seasonal exit
- **Ride the volatility**

### 4. Rolling Seasonal Positions

**Many seasonals use front-month contracts:**

**Problem: Contracts expire**

**Solution: Roll positions**

**Example (Corn seasonal Feb-Jun):**

**Entry Feb 15:**

- Use Dec futures (new crop, liquid)
- Dec expires in November (safe)
- No roll needed
- **Simple**

**Or use calendar spread:**

- Long Dec-Mar spread (buys Dec, sells Mar)
- Captures seasonal without outright risk
- Both legs expire after seasonal window
- **Spread approach**

### 5. Exit Discipline

**Three exit triggers:**

**1. Calendar exit (primary):**

$$
\text{Date} = \text{Jun 25} \Rightarrow \text{Exit}
$$

**No matter what!**

- Win or lose
- Seasonal window closed
- Edge expires
- **Take off position**

**2. Stop loss (risk management):**

$$
\text{If Loss} > 50\% \text{ of historical avg} \Rightarrow \text{Exit}
$$

**Example:**

- Corn seasonal avg return: +10.5%
- Entered Feb 15 @ $5.50
- Stop: -5% ($5.23)
- Hit May 1: Exit
- **Cut loser**

**3. Fundamental shift (override):**

**Example:**

- Entered corn seasonal Feb 15
- April 1: USDA raises planting estimate by 8%
- Massive new supply coming
- **Exit immediately, fundamental changed**

---

## Maximum Profit and Loss

### 1. Corn Seasonal (Long Feb-Jun)

**Setup:**

- Entry: Feb 15, 2024
- Price: $5.50/bushel
- Position: Long 20 contracts (100,000 bushels)
- Margin: $2,000 per contract = $40,000 total

**Maximum Profit (Drought Year):**

**2012 scenario (worst drought in 50 years):**

- Entry: $5.50
- Exit Jun 25: $8.25 (drought premium)
- Return: +50%

$$
\text{Profit} = (\$8.25 - \$5.50) \times 5,000 \times 20 = \$275,000
$$

$$
\text{Return on margin} = \frac{\$275,000}{\$40,000} = 688\%
$$

**Exceptional year, not expected!**

**Typical Profit (Normal Year):**

- Entry: $5.50
- Exit Jun 25: $6.08 (+10.5% avg)
- Return: +10.5%

$$
\text{Profit} = \$0.58 \times 5,000 \times 20 = \$58,000
$$

$$
\text{Return} = \frac{\$58,000}{\$40,000} = 145\%
$$

**In 4.5 months → Annualized: 387%**

**Maximum Loss (Record Crop Forecast):**

**Scenario: April USDA raises acres, perfect planting:**

- Entry: $5.50
- Fundamental shift evident in April
- Exit early @ $5.25 (stop loss hit)
- Loss: -4.5%

$$
\text{Loss} = -\$0.25 \times 5,000 \times 20 = -\$25,000
$$

$$
\text{Return} = \frac{-\$25,000}{\$40,000} = -62.5\%
$$

**Managed loss (with discipline)**

**Worst case (no stop, holding to Jun 25):**

- Entry: $5.50
- Exit: $5.05 (record crop fears)
- Loss: -8.2% (historical avg loser)

$$
\text{Loss} = -\$0.45 \times 5,000 \times 20 = -\$45,000
$$

$$
\text{Return} = -112.5\%
$$

**Expectancy calculation:**

$$
\mathbb{E}[\text{Return}] = 0.73 \times 145\% + 0.27 \times (-62.5\%) = 105.8\% - 16.9\% = 88.9\%
$$

**Expected 89% return over 4.5 months!**

### 2. Natural Gas Short Seasonal (Mar-Sep)

**Setup:**

- Entry: Mar 1, 2024
- Price: $3.00/MMBtu
- Position: Short 10 contracts
- Margin: $5,000 per contract = $50,000

**Maximum Profit (Normal Injection Season):**

**Typical pattern:**

- Entry: $3.00
- Exit Sep 30: $2.10 (-30% avg)
- Decline: -$0.90

$$
\text{Profit} = \$0.90 \times 10,000 \times 10 = \$90,000
$$

$$
\text{Return} = \frac{\$90,000}{\$50,000} = 180\%
$$

**In 7 months → Annualized: 309%**

**Maximum Loss (Hurricane Supply Disruption):**

**Scenario: Aug hurricane hits Gulf production:**

- Entry: $3.00
- Hurricane Aug 15: Spike to $5.50
- Stop loss: $3.75 (+25%)
- Exit at stop

$$
\text{Loss} = -\$0.75 \times 10,000 \times 10 = -\$75,000
$$

$$
\text{Return} = -150\%
$$

**This is why stops critical!**

**Expectancy:**

$$
\mathbb{E}[\text{Return}] = 0.67 \times 180\% + 0.33 \times (-150\%) = 120.6\% - 49.5\% = 71.1\%
$$

**Expected 71% return over 7 months**

### 3. Cattle Seasonal (Long Feb-Jun)

**Setup:**

- Entry: Feb 28, 2024
- Price: $185/cwt
- Position: Long 15 contracts (600,000 lbs)
- Margin: $3,500 per contract = $52,500

**Typical Profit:**

- Entry: $185
- Exit Jun 7: $199.80 (+8% avg)
- Return: +8%

$$
\text{Profit} = \$14.80 \times 400 \times 15 = \$88,800
$$

$$
\text{Return} = \frac{\$88,800}{\$52,500} = 169\%
$$

**In 3.5 months → Annualized: 579%**

**Loss scenario:**

- Entry: $185
- Beef demand collapse
- Exit (stop): $175 (-5.4%)

$$
\text{Loss} = -\$10 \times 400 \times 15 = -\$60,000
$$

$$
\text{Return} = -114\%
$$

**Expectancy:**

$$
\mathbb{E}[\text{Return}] = 0.71 \times 169\% + 0.29 \times (-114\%) = 120.0\% - 33.1\% = 86.9\%
$$

---

## When to Use Seasonal Trades

### 1. Ideal Market Conditions

**Use seasonals when:**

**1. Fundamentals neutral or supportive:**

$$
\text{Stocks/Use Ratio} \in [20\%, 30\%] \quad \text{(normal range)}
$$

**Example (Corn seasonal):**

- Feb 1: Stocks 10 billion bushels
- Usage: 14.5 billion
- Ratio: 69% (normal)
- No extreme surplus or shortage
- **Fundamentals neutral → Seasonal works**

**2. Historical pattern very strong:**

$$
\text{Win Rate} > 70\%
$$

**Corn Feb-Jun: 73%**

**Confidence high for replication**

**3. Seasonal window opening:**

**Calendar-based entry:**

- Feb 15 approaching
- Backtest says enter
- Fundamentals checked (OK)
- **Execute**

**4. Multiple commodities aligning:**

**Example (Spring rally):**

- Corn seasonal: Feb-Jun (long)
- Soybeans seasonal: Jan-May (long)
- Wheat seasonal: Dec-Mar (long)
- **Diversified seasonal portfolio**

**5. Can dedicate time to monitor:**

- USDA reports weekly/monthly
- Weather forecasts daily
- News flow
- **Active management required**

### 2. Specific Use Cases

**Use Case 1: Pure seasonal portfolio**

**Strategy:**

- Allocate 20% of portfolio to seasonals
- Enter 5-7 different commodities
- Stagger entries over year
- **Systematic approach**

**Example portfolio (annual):**

| Month | Trade | Allocation | Expected |
|-------|-------|-----------|----------|
| Jan | Long soybeans | 3% | +11% |
| Feb | Long corn, cattle | 6% | +10% |
| Mar | Short nat gas | 3% | +17% |
| Jun | Long hogs | 2% | +8% |
| Dec | Long wheat | 3% | +7% |

**Annual expected: 12-18% from seasonals**

**Use Case 2: Seasonal + fundamental combination**

**When fundamentals support seasonal:**

**Example: 2024 Corn**

- Seasonal says long Feb-Jun
- Fundamentals: Low stocks (18% S/U)
- South America poor crop
- **Double edge**

**Increase position size:**

- Normal seasonal: 3% of portfolio
- With fundamentals: 6% of portfolio
- **When stars align, press bet**

**Use Case 3: Hedging with seasonals**

**Farmer perspective:**

- Plant corn in May
- Seasonal says prices peak Jun-Jul
- Lock in sales for harvest
- **Natural hedge**

**Use Case 4: Counter-cyclical income**

**Portfolio manager:**

- Equity markets seasonal: Weak May-Oct
- Commodity seasonals: Various windows
- Diversification benefit
- **Smooth return stream**

---

## When NOT to Use Seasonal Trades

### 1. Avoid These Situations

**1. Extreme fundamental imbalance:**

$$
\text{Stocks/Use} > 40\% \text{ (massive surplus)}
$$

**Example: 2016 Corn**

- Stocks/Use: 44% (record high)
- Seasonal says long Feb-Jun
- **But fundamentals bearish**

**Result:**

- Entered seasonal: $3.80
- Exited: $3.50 (-7.9%)
- **Loser because fundamentals overrode**

**Correct decision: Skip year**

**2. Opposite seasonal already underway:**

**Example: Natural gas short (Mar-Sep)**

**But market already declined:**

- February: $4.50
- March 1 (entry): $2.00 (down 56% already!)
- **Move already happened**

**Problem:**

- Seasonal assumes normal entry
- If market pre-ran, edge gone
- **Don't chase**

**3. Major event approaching:**

**Example: Corn seasonal**

**June 30 USDA Acreage Report:**

- Biggest report of year
- Can move market 10-20%
- Unpredictable direction
- **Seasonal exit Jun 25 is 5 days before**

**If late:**

- Exit before report
- Don't risk blow-up
- **Event risk > seasonal edge**

**4. Correlation breakdown:**

**Normal: Corn & Soybeans correlated (compete for acres)**

$$
\rho(\text{Corn}, \text{Beans}) \approx 0.70
$$

**But sometimes decouple:**

- Corn: Weather issues (drought)
- Soybeans: Demand issues (China trade war)
- Correlation → 0.30
- **Both seasonals may not work**

**5. Low volatility environment:**

**Seasonal needs price movement to profit:**

**Example: Corn in tight range**

- Feb: $5.50
- Mar: $5.45
- Apr: $5.55
- May: $5.50
- Jun: $5.48
- **No movement = no profit**

**When VIX-equivalent (implied vol) < 15%:**

- Skip seasonal
- Theta too low
- **Need volatility**

**6. Can't monitor position:**

**Seasonals require attention:**

- USDA reports (surprise data)
- Weather forecasts (drought/flood)
- Fund flows (spec positioning)
- **Active management**

**If you're:**

- On vacation
- Too busy
- Can't check daily
- **Don't trade**

**7. Structural market changes:**

**Example: Ethanol mandate change**

- Corn demand historically: Food, feed, export
- 2005-2024: Ethanol became 35-40% of demand
- **Seasonality changed!**

**Old seasonal (pre-2005):**

- Different pattern
- Different fundamentals
- **Obsolete**

**New seasonal (post-2010):**

- Ethanol demand dominates
- Different time windows
- **Must adapt**

### 2. Warning Signs to Exit

**1. Fundamental reversal mid-trade:**

**Example: Drought appears (bullish)**

- Entered corn seasonal Feb 15 @ $5.50
- May 15: Drought developing
- USDA cuts yield forecast
- Prices rally to $7.00
- **But seasonal says exit Jun 25**

**Decision:**

- Exit early (lock profit at $7.00)
- Don't wait for calendar
- Fundamental changed
- **Take windfall**

**2. Seasonal failing historically:**

**Example: Win rate collapsing**

- Corn Feb-Jun historically 73%
- Last 5 years: 2 wins, 3 losses (40%)
- Pattern breaking down
- **Something changed structurally**

**Decision:**

- Skip next year
- Investigate why failing
- Reassess pattern
- **Don't force it**

**3. Position down >50% of expected return:**

**Example:**

- Corn seasonal expected +10.5%
- Currently down -6%
- Halfway through window
- **Not working**

**Decision:**

- Exit at -6%
- Don't hold hoping for recovery
- Cut loser
- **Preserve capital**

---

## Position Sizing and Risk Management

### 1. The Golden Rule

**Position sizing must account for full delta:**

$$
\text{Contracts} = \frac{\text{Account Risk (2-3\%)}}{\text{Expected Stop Distance} \times \text{Contract Size}}
$$

**Example:**

**Account: $500,000**

**Risk: 2.5% = $12,500**

**Corn seasonal:**

- Entry: $5.50/bushel
- Stop: $5.23 (-4.9%)
- Risk per contract: $0.27 × 5,000 = $1,350

$$
\text{Contracts} = \frac{\$12,500}{\$1,350} = 9.26 \approx 9
$$

**Trade: 9 corn contracts**

### 2. Portfolio Allocation

**Conservative:**

- 5-10% of portfolio in seasonals
- $500k → $25-50k
- 2-3 seasonals at a time
- **Prudent exposure**

**Moderate:**

- 10-20% of portfolio
- $500k → $50-100k
- 4-6 seasonals
- **Active seasonal trader**

**Aggressive:**

- 20-30% of portfolio
- $500k → $100-150k
- 6-10 seasonals
- **Seasonal specialist**

**Never >30% in seasonals:**

- Directional exposure
- Correlated moves possible
- Need diversification
- **Cap total exposure**

### 3. Diversification Across Seasonals

**Don't concentrate in one sector:**

**Bad allocation:**

- Corn: 10%
- Soybeans: 10%
- Wheat: 10%
- Total ags: 30%
- **All correlated!**

**Good allocation:**

- Grains (corn/beans): 10%
- Energy (nat gas): 7%
- Livestock (cattle/hogs): 8%
- Softs (coffee/cocoa): 5%
- **Diversified 30%**

### 4. Stop Loss Strategy

**Two types of stops:**

**1. Price-based (standard):**

$$
\text{Stop} = \text{Entry} - 50\% \times \mathbb{E}[\text{Return}]
$$

**Example (Corn seasonal):**

- Entry: $5.50
- Expected return: +10.5% = $0.58
- Stop: $5.50 - (0.50 × $0.58) = $5.21
- **If hits $5.21, exit**

**2. Fundamental-based (override):**

**Immediate exit if:**

- USDA report shocking surprise
- Weather pattern shifts
- Major demand change
- **Thesis broken**

**Example:**

- Long corn seasonal
- April USDA: Acres +15% above expectations
- **Exit immediately, don't wait for price stop**

### 5. Profit Targets

**Three approaches:**

**Approach 1: Calendar exit (recommended):**

$$
\text{Exit Date} = \text{Jun 25} \quad \text{(period)}
$$

**Pros:**

- Systematic
- Historically validated
- No emotion
- **Disciplined**

**Approach 2: Target-based:**

$$
\text{If Profit} \geq \mathbb{E}[\text{Return}] \times 1.5 \Rightarrow \text{Exit}
$$

**Example:**

- Expected: +10.5%
- Target: +15.75%
- Hit early (May 1) at $6.37
- **Take profit early**

**Approach 3: Trailing stop:**

**After profitable:**

- Set stop at entry (breakeven)
- Trail by 3 ATR
- Let winners run
- **Capture outliers**

### 6. Margin Management

**Commodity margin varies:**

**Initial margin (examples):**

- Corn: $2,000 per contract
- Natural gas: $5,000 per contract
- Cattle: $3,500 per contract

**Maintenance margin: ~70-80% of initial**

**Reserve requirements:**

$$
\text{Keep } 2\text{-}3\times \text{ margin in cash}
$$

**For $100k in seasonals:**

- Margin posted: $100k
- Cash reserve: $200-300k
- **Never fully invested**

**Why:**

- Adverse moves
- Margin calls
- Avoid forced liquidation
- **Safety buffer**

### 7. Example

**Account: $500,000**

**Seasonal allocation: 20% = $100,000**

**Positions:**

**Position 1: Corn Long (Feb-Jun)**

- 9 contracts @ $5.50
- Margin: $18,000
- Stop: $5.21
- Risk: $0.29 × 5,000 × 9 = $13,050
- Account risk: 2.6%

**Position 2: Nat Gas Short (Mar-Sep)**

- 6 contracts @ $3.00
- Margin: $30,000
- Stop: $3.75
- Risk: $0.75 × 10,000 × 6 = $45,000
- Account risk: 9% (high!)
- **Reduce to 3 contracts**

**Revised Position 2:**

- 3 contracts @ $3.00
- Margin: $15,000
- Risk: $0.75 × 10,000 × 3 = $22,500
- Account risk: 4.5%

**Position 3: Cattle Long (Feb-Jun)**

- 8 contracts @ $185
- Margin: $28,000
- Stop: $175
- Risk: $10 × 400 × 8 = $32,000
- Account risk: 6.4%

**Total portfolio:**

- Margin deployed: $61,000
- Cash reserve: $439,000
- Total risk: $67,550
- Account risk: 13.5%
- **Within 15% limit**

**Diversification:**

- Grains: 2.6%
- Energy: 4.5%
- Livestock: 6.4%
- **Balanced across sectors**

---

## Common Mistakes Beginners Make

### 1. Mistake #1

**The error:**

- "It's Feb 15, seasonal says long corn"
- Blind entry
- Don't check stocks, acres, weather
- **Mechanical approach**

**What happens (2016):**

- Stocks: 10.9 billion bushels (44% S/U!)
- Record surplus
- Seasonal: Long Feb-Jun
- Result: -7.9% (loser)
- **Fundamental override**

**Correct approach:**

**Pre-entry checklist:**

1. Check stocks/use ratio
2. Review planting intentions
3. Assess South American crop
4. Read USDA monthly reports
5. **Only enter if fundamentals neutral/supportive**

### 2. Mistake #2

**The error:**

- Seasonal window: Feb 15 - Jun 25
- Trader learns about it April 15
- Enters April 15 (late)
- **Missed 2 months of move**

**What happens:**

**Normal progression:**

- Feb 15 - Apr 15: +8% (missed)
- Apr 15 - Jun 25: +2% (caught)
- **Captured 20% of move**

**Why it fails:**

- Seasonal moves early (uncertainty premium)
- Late entry = already priced in
- Risk/reward terrible
- **Chasing**

**Correct approach:**

$$
\text{Only enter if} < 25\% \text{ of window elapsed}
$$

**If late:**

- Skip this year
- Wait for next cycle
- **Patience**

### 3. Mistake #3

**The error:**

- "Seasonal has 73% win rate, I don't need a stop"
- Enter without stop
- Position goes against
- Hold and hope
- **Denial**

**Disaster scenario:**

**2019 Corn:**

- Entered Feb 15 @ $3.85
- Flooded spring (delayed planting)
- Prices fell: $3.85 → $3.40 (-11.7%)
- No stop, held to Jun 25
- **Loss: -11.7% vs expected +10.5%**

**If had stop at $3.66 (5% down):**

- Loss: -4.9%
- Saved 6.8%
- **Stop protected**

**Correct approach:**

**Always use stops:**

- 73% win rate = 27% losers
- Can't predict which year
- Stop limits damage
- **Non-negotiable**

### 4. Mistake #4

**The error:**

- Corn margin: $2,000 per contract
- Think: "So cheap, I can do 50 contracts!"
- Account: $100,000
- Enter 50 contracts ($100k margin)
- **Fully leveraged**

**What happens:**

- Corn drops $0.30/bushel
- MTM loss: $0.30 × 5,000 × 50 = -$75,000
- Margin call: $50,000
- Can't meet it
- **Forced liquidation**

**Correct approach:**

**Size by RISK, not margin:**

- Risk per contract: $0.27 (stop distance)
- Account risk: 2.5% = $2,500
- Contracts: $2,500 / ($0.27 × 5,000) = 1.85 ≈ 2
- **Only 2 contracts!**

### 5. Mistake #5

**The error:**

- Seasonal: Long corn Feb 15 - Jun 25
- Jun 25: Up $0.48 (+8.7%)
- Think: "It's going higher, I'll hold!"
- Hold through July
- **Greed**

**What happens:**

**Harvest pressure begins:**

- Jun 25: $5.98 (+8.7%)
- Jul 15: $5.85
- Aug 1: $5.50 (back to entry)
- **Gave back all gains**

**Why:**

- Jun-Oct: Harvest pressure (bearish seasonal)
- Opposite of Feb-Jun
- Holding = fighting new seasonal
- **Lose edge**

**Correct approach:**

**Exit on calendar date:**

- Jun 25: Exit
- Profit: +8.7%
- **Lock it in**

**If want continued exposure:**

- Exit Jun 25
- Enter new seasonal (different commodity)
- Don't overstay
- **Follow the calendar**

### 6. Mistake #6

**The error:**

- Drought develops in June
- Corn: $5.50 → $7.00 (+27%)
- Trader: "Wow, seasonal working great!"
- Enters July 1 @ $7.00
- **Chasing**

**What happens:**

- Jul-Sep: Harvest confirms size
- Prices fall: $7.00 → $5.80
- Loss: -17%
- **Bought high**

**Why it fails:**

- Weather market over by July
- Risk premium realized
- No more uncertainty
- **Late to party**

**Correct approach:**

**Only enter in window:**

- Feb 15 - Mar 15 (early entry)
- After that: Skip
- **Discipline**

### 7. Mistake #7

**The error:**

- Entered corn seasonal Feb 15
- May 1: Perfect planting weather
- 95% planted vs 70% average
- Trader: "I'll hold to Jun 25 (calendar exit)"
- **Ignoring signal**

**What happens:**

- May 1: $6.10 (up 11%)
- Jun 25: $5.80 (down)
- **Held through reversal**

**Why:**

- Uncertainty resolved early (perfect planting)
- No weather risk premium needed
- Edge disappeared
- **Should have exited**

**Correct approach:**

**Monitor weather daily:**

- If resolves positively → Exit early
- If worsens → Hold/extend
- **Dynamic management**

### 8. Mistake #8

**The error:**

- Entered seasonal, down 5%
- Stop at 5% hit
- Think: "But historical win rate 73%!"
- Hold instead of exiting
- Down 10%, 15%, 20%
- **Denial**

**What happens:**

- This is the 1-in-4 losing year
- Final loss: -20%
- Expected: +10.5%
- Swing: -30.5%
- **Devastating**

**Correct approach:**

**Honor stops:**

- 73% win rate = 27% lose rate
- Can't know which year
- Stop preserves capital
- **Live to trade next year**

### 9. Mistake #9

**The error:**

**Portfolio:**

- Long corn (Feb-Jun)
- Long soybeans (Jan-May)
- Long wheat (Dec-Mar)
- All grains!
- **100% correlation**

**What happens:**

**If ONE fundamental shifts:**

- Drought in all grain belt
- All three spike (lucky)
- OR massive supply, all three fall
- **Portfolio volatility = individual volatility**

**Correct approach:**

**Diversify sectors:**

- Grains: 40%
- Energy: 30%
- Livestock: 30%
- **Correlation <0.50**

### 10. Mistake #10

**The error:**

- Backtest seasonal: 5 years of data
- Win rate: 80% (4 of 5)
- Think: "Great seasonal!"
- Trade it
- **Insufficient sample**

**Why it fails:**

**5 years is NOT enough:**

- Need 20-30 years minimum
- Captures full weather cycles
- Multiple fundamental regimes
- **Robust validation**

**Example:**

- 5 years (2019-2023): 80% win rate
- 30 years (1994-2023): 67% win rate
- **Cherry-picked period**

**Correct approach:**

$$
\text{Minimum data} = 20 \text{ years}
$$

**Ideally 30-50 years for agricultural commodities**

---

## Best Case Scenario

### 1. The Perfect Corn Seasonal (2012 Drought)

**Trader profile:**

- Experience: 10 years agricultural trading
- Account: $500,000
- Strategy: Corn seasonal Feb-Jun
- Discipline: Excellent

**Setup (February 2012):**

**Market analysis:**

- Stocks/use: 23% (slightly tight, good)
- South American crop: Normal
- Planting intentions: 95M acres (normal)
- La Niña pattern (potential drought)
- **Fundamentals neutral to slightly bullish**

**Entry (Feb 15, 2012):**

- Corn: $6.40/bushel
- Position: 15 contracts (75,000 bushels)
- Margin: $30,000
- Stop: $6.10 (4.7% down)
- Target: Jun 25 exit
- Expected: +10% = $6.40 × 1.105 = $7.07

**Trade progression:**

**Feb-Mar (Planting season):**

- Normal price action
- Planting concerns building
- Corn: $6.40 → $6.70
- **P&L: +$22,500 (+7.5%)**

**April (Weather market begins):**

- Dry forecast emerging
- Soil moisture declining
- Planting delayed in some areas
- Corn: $6.70 → $7.10
- **P&L: +$52,500 (+16.4%)**

**May (Drought intensifies):**

- GFS model: Hot/dry 30-day outlook
- Planting finally complete (late)
- Emerged corn stressed
- Corn: $7.10 → $7.80
- **P&L: +$105,000 (+32.8%)**

**June (Historic drought):**

- Worst drought in 50 years confirmed
- Crop conditions: 30% good/excellent (vs 70% avg)
- Yield forecasts collapsing
- Jun 15: Corn $8.10 (+26.6% from entry)
- **P&L: +$127,500 (+42.5%)**

**Decision point (Jun 15):**

**Seasonal says exit Jun 25, but...**

**Analysis:**

- Drought still intensifying
- Pollination period approaching (critical)
- USDA hasn't cut yield yet
- **More upside possible**

**Decision: Partial exit + trail remainder**

**Jun 15 action:**

- Close 10 contracts @ $8.10
- P&L: ($8.10 - $6.40) × 5,000 × 10 = +$85,000
- Keep 5 contracts with trailing stop
- **Lock majority of profit**

**June 25 (pollination crisis):**

- Record heat (100°F+ for weeks)
- Pollination failing
- Corn: $8.40
- **Extended hold working**

**July 15 (peak):**

- Corn hits $8.49 (all-time high)
- Trailing stop: $8.20
- Still holding 5 contracts

**August 1 (exit on stop):**

- Stop hit @ $8.20
- Close remaining 5 contracts

**Final P&L:**

**First 10 contracts:**

$$
(\$8.10 - \$6.40) \times 5,000 \times 10 = \$85,000
$$

**Remaining 5 contracts:**

$$
(\$8.20 - \$6.40) \times 5,000 \times 5 = \$45,000
$$

**Total:**

$$
\$85,000 + \$45,000 = \$130,000
$$

**Return:**

$$
\frac{\$130,000}{\$30,000 \text{ margin}} = 433\%
$$

**On account:**

$$
\frac{\$130,000}{\$500,000} = 26\% \text{ in 5.5 months}
$$

**Why this worked perfectly:**

1. ✅ Entered on calendar date (Feb 15)
2. ✅ Fundamentals checked (neutral/supportive)
3. ✅ La Niña = drought risk (bonus)
4. ✅ Sized appropriately (15 contracts)
5. ✅ Managed dynamically (partial exit)
6. ✅ Extended hold with trailing stop
7. ✅ Honored stop when hit
8. **Professional execution + lucky timing**

---

## Worst Case Scenario

### 1. The Failed Seasonal (2016 Corn Surplus)

**Trader profile:**

- Experience: 2 years
- Account: $200,000
- Strategy: Blind seasonal following
- Discipline: Poor

**Setup (February 2016):**

**Ignored fundamentals:**

- Stocks/use: 44% (RECORD SURPLUS!)
- South American crop: Record large
- Planting intentions: 94M acres (high)
- **All bearish, ignored**

**Entry (Feb 15, 2016):**

- Corn: $3.85/bushel
- Position: 25 contracts (way oversized!)
- Margin: $50,000 (25% of account)
- NO STOP LOSS (rookie error)
- **Mechanical seasonal entry**

**Trade progression:**

**Feb-Mar:**

- Prices declining slowly
- Corn: $3.85 → $3.75
- Trader: "Just seasonal noise"
- **Ignored warning**

**April (USDA report):**

- USDA projects massive crop
- Prices gap down
- Corn: $3.75 → $3.55
- Loss: -$37,500 (-18.8%)
- Trader: "It will recover, seasonal always works!"
- **Denial**

**May (continued decline):**

- Perfect planting weather
- 95% planted (vs 70% avg)
- No uncertainty premium needed
- Corn: $3.55 → $3.45
- **Loss: -$50,000 (-25%)**

**Jun 25 (forced calendar exit):**

- Corn: $3.55 (recovered slightly)
- Loss: -$37,500
- **Down 18.8% on $50k margin = -75% loss of capital**

**What went catastrophically wrong:**

1. ❌ Ignored fundamentals (44% stocks/use!)
2. ❌ No stop loss (held loser)
3. ❌ Oversized (25 contracts on $200k)
4. ❌ Mechanical entry (didn't think)
5. ❌ Fought the trend (denial)
6. ❌ Used 25% of account in one trade
7. **Complete failure of discipline**

**Recovery:**

- Account: $200k → $162,500
- Took 9 months to recover @ 2%/month
- **Expensive lesson**

---

## What to Remember

### 1. Core Concept

**Commodities follow predictable annual price cycles:**

$$
\text{Seasonal Edge} = \mathbb{E}[\text{Price}_{\text{month } t}] - \mathbb{E}[\text{Price}_{\text{annual}}]
$$

- Agricultural: Planting/harvest cycles
- Energy: Heating/cooling demand
- Livestock: Biological breeding cycles
- Patterns repeat with 65-85% reliability
- Combine statistics with fundamentals

### 2. Strongest Seasonals

**Agricultural:**

- Corn: Long Feb-Jun (73% win rate, +10.5% avg)
- Soybeans: Long Jan-May (70%, +11.4%)
- Wheat: Long Dec-Mar (67%, +7.1%)

**Energy:**

- Natural Gas: Short Mar-Sep (67%, +16.5%)
- Gasoline: Long Feb-Jun (68%, +12.0%)

**Livestock:**

- Cattle: Long Feb-Jun (71%, +8.0%)
- Hogs: Long Jun-Aug (68%, +8.2%)

### 3. Time Selection

**Entry:**

- Calendar-based (historical optimal)
- Confirm fundamentals neutral/supportive
- Early in seasonal window (<25% elapsed)

**Exit:**

- Calendar date (primary)
- Stop loss (risk management)
- Fundamental shift (override)
- Weather resolution (early exit)

### 4. Maximum Profit and Loss

**Typical returns:**

- Win rate: 65-75%
- Winning trades: +10-20% avg
- Losing trades: -5-10% (with stops)
- Expectancy: +7-12% per trade

**Best case:**

- 2012 Corn drought: +433% (5.5 months)
- Perfect fundamental + seasonal alignment

**Worst case:**

- 2016 Corn surplus: -75% (ignored fundamentals)
- Mechanical approach without analysis

### 5. When to Use

**Ideal conditions:**

- Fundamentals neutral or supportive
- Win rate >70% (strong pattern)
- Early in seasonal window
- Can monitor actively
- Multiple seasonals for diversification

### 6. When NOT to Use

**Avoid:**

- Extreme fundamental imbalance (stocks/use >40% or <15%)
- Late entry (>25% of window elapsed)
- Major event approaching
- Structural market changes
- Can't monitor positions

### 7. Risk Management

**Position sizing:**

$$
\text{Contracts} = \frac{\text{Account Risk (2-3\%)}}{\text{Stop Distance} \times \text{Contract Size}}
$$

**Stops (mandatory):**

- Price stop: Entry - 50% of expected return
- Fundamental stop: Exit if thesis breaks
- Calendar stop: Exit on target date

**Diversification:**

- Max 20-30% portfolio in seasonals
- Spread across grains/energy/livestock
- Correlation <0.50 between positions

### 8. Common Mistakes

1. Ignoring fundamentals (blind entry)
2. Entering late (chasing move)
3. No stop loss ("seasonal always works")
4. Overleveraging (margin ≠ risk)
5. Holding past calendar exit
6. Chasing after big move
7. Ignoring weather signals
8. Fighting losing trades
9. Correlating all seasonals (grains only)
10. Insufficient backtest data (<20 years)

### 9. Success Factors

**Three pillars:**

1. **Statistical validation** (20+ years data)
2. **Fundamental confirmation** (neutral/supportive)
3. **Disciplined execution** (calendar entry/exit, stops)

**Formula:**

$$
\text{Success} = \text{Statistics} \times \text{Fundamentals} \times \text{Discipline}
$$

### 10. Final Wisdom

> "Commodity seasonality is one of the most statistically robust edges in trading—agricultural crop cycles, energy demand patterns, and livestock breeding constraints create recurring annual price movements that have persisted for decades. But seasonality is a tendency, not a law. A 73% win rate means 27% of years fail, and those failures often coincide with extreme fundamental imbalances (massive surplus/shortage) that override seasonal patterns. The successful seasonal trader combines rigorous statistical analysis (20+ years of data, optimal entry/exit windows) with fundamental awareness (check stocks/use ratios, planting intentions, weather forecasts) and disciplined risk management (position sizing, stop losses, calendar exits). Trade WITH both statistics AND fundamentals, never against them. Honor your stops—you can't predict which year is the losing 27%. Seasonal trading is a marathon, not a sprint—consistent execution over multiple years compounds into exceptional returns."

**Most important principles:**

- Seasonality = probability, not certainty (65-85% win rates)
- Fundamentals can override seasonals (check stocks/use)
- Calendar discipline critical (enter early, exit on date)
- Stops mandatory (27-33% of years are losers)
- Weather monitoring essential (drought/flood changes everything)
- Position sizing by risk, not margin
- 20+ years backtest minimum (robust validation)
- Diversify across sectors (not all grains)

**Why this works:**

- Physical constraints (can't grow corn in winter)
- Storage costs (economic force)
- Risk premiums (farmers vs speculators)
- Biological cycles (cattle/hog breeding)
- Demand seasonality (heating/cooling)
- **Nature + Economics = persistent patterns**

**But remember:**

- Fundamentals can shift equilibrium
- Weather is unpredictable (2012 drought vs 2016 perfect)
- Structural changes happen (ethanol mandate)
- Win rates <100% (respect the 27% losers)
- Require active management (not passive)
- **Edge exists but demands discipline**

**Trade seasonals when calendar, statistics, AND fundamentals align. Exit when any one breaks. Compound small edges over decades for wealth. 🌾📅**
