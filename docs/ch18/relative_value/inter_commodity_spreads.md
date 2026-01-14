# Inter-Commodity


**Inter-commodity spreads** are futures strategies that trade the price relationship between two related but different commodities, profiting from mean reversion in processing margins, substitution ratios, or economic linkages while remaining directionally neutral to absolute price movements.

---

## The Core Insight


**The fundamental idea:**

- Related commodities have economic relationships (input/output, substitutes, complements)
- These relationships create predictable price ratios
- Price spreads deviate from fair value temporarily
- Market forces restore equilibrium (mean reversion)
- You can profit from spread normalization
- Remain neutral to absolute commodity prices
- Lower volatility than outright positions
- Structural edges from physical economics

**The key equations:**

$$
\text{Crack Spread} = \text{Gasoline Price} + \text{Diesel Price} - \text{Crude Oil Price}
$$

$$
\text{Crush Spread} = \text{Soybean Meal Price} + \text{Soybean Oil Price} - \text{Soybean Price}
$$

$$
\text{Spread P\&L} = (\text{Spread}_{\text{exit}} - \text{Spread}_{\text{entry}}) \times \text{Contract Size}
$$

**You're essentially betting: "The current processing margin (crack spread, crush spread) or price ratio (gold/silver, corn/wheat) is temporarily wide or narrow relative to historical norms, and I can profit as the spread reverts to fair value while avoiding directional risk in the underlying commodities."**

---

## What Are


**Before trading inter-commodity spreads, understand the fundamental mechanics:**

### 1. Types of


**1. Processing Spreads (Input → Outputs):**

Raw material converted to finished products:

**Crack Spread (Energy):**

$$
\text{Crack Spread} = \text{Products} - \text{Crude Oil}
$$

- Input: Crude oil
- Outputs: Gasoline, diesel, jet fuel
- Represents refiner profit margin
- **Most traded processing spread**

**Crush Spread (Agriculture):**

$$
\text{Crush Spread} = \text{Meal} + \text{Oil} - \text{Soybeans}
$$

- Input: Soybeans
- Outputs: Soybean meal (48%), soybean oil (18%)
- Represents processor profit margin
- **Second most popular**

**Spark Spread (Power):**

$$
\text{Spark Spread} = \text{Electricity} - (\text{Natural Gas} \times \text{Heat Rate})
$$

- Input: Natural gas
- Output: Electricity
- Represents power plant margin
- **Regional variations**

**2. Substitution Spreads:**

Commodities that can replace each other:

**Corn/Wheat Spread:**

$$
\text{Spread} = \text{Corn} - \text{Wheat}
$$

- Both used for livestock feed
- Substitutable based on price
- **Mean-reverting ratio**

**Gold/Silver Spread:**

$$
\text{Gold/Silver Ratio} = \frac{\text{Gold Price}}{\text{Silver Price}}
$$

- Both precious metals
- Historical ratio: 50-80
- **Mean reversion trading**

**WTI/Brent Spread:**

$$
\text{Spread} = \text{Brent} - \text{WTI}
$$

- Both crude oil benchmarks
- Typically Brent > WTI ($2-5/barrel)
- **Arbitrage opportunities**

**3. Economic Linkage Spreads:**

Commodities related through supply chains:

**Cattle/Corn Spread:**

$$
\text{Spread} = \text{Live Cattle} - (\text{Corn} \times \text{Feed Ratio})
$$

- Corn is cattle feed input
- Spread = cattle producer margin
- **Agricultural relationship**

**Copper/Gold Spread:**

$$
\text{Ratio} = \frac{\text{Copper}}{\text{Gold}}
$$

- Copper = economic growth
- Gold = safe haven
- Ratio indicates risk appetite
- **Macro indicator**

### 2. Most common crack


**Most common crack spread configuration:**

$$
\text{3-2-1 Crack} = 2 \times \text{RBOB} + 1 \times \text{HO} - 3 \times \text{CL}
$$

Where:
- RBOB = Gasoline (42,000 gallons/contract)
- HO = Heating oil/Diesel (42,000 gallons/contract)
- CL = Crude oil (1,000 barrels/contract)
- **Ratio mimics refinery yield**

**Economic meaning:**

3 barrels of crude produce:

- 2 barrels gasoline (67%)
- 1 barrel diesel (33%)
- Total: 126,000 gallons products
- Input: 3,000 barrels crude
- **Spread = refiner gross margin**

**Contract sizing:**

$$
\text{Long: } 2 \text{ RBOB} + 1 \text{ HO}
$$

$$
\text{Short: } 3 \text{ CL}
$$

**P&L calculation:**

$$
\text{Crack P\&L} = 2 \times \Delta\text{RBOB} + 1 \times \Delta\text{HO} - 3 \times \Delta\text{CL}
$$

In dollars per barrel:

$$
\text{Crack ($/bbl)} = \frac{2 \times \text{RBOB} + 1 \times \text{HO}}{3} - \text{CL}
$$

**Example:**

- Crude: $75/barrel
- Gasoline: $2.40/gallon × 42 = $100.80/barrel
- Diesel: $2.60/gallon × 42 = $109.20/barrel

$$
\text{Crack} = \frac{2 \times \$100.80 + 1 \times \$109.20}{3} - \$75 = \$28.60/\text{barrel}
$$

**This $28.60 is the refiner margin per barrel!**

### 3. Configuration:


**Configuration:**

$$
\text{Crush} = 1 \times \text{SM} + 11 \times \text{BO} - 1 \times \text{ZS}
$$

Where:
- ZS = Soybeans (5,000 bushels/contract)
- SM = Soybean meal (100 short tons/contract)
- BO = Soybean oil (60,000 lbs/contract)
- **Ratio based on processing yields**

**Economic meaning:**

1 bushel soybeans (60 lbs) produces:

- 48 lbs soybean meal (80%)
- 11 lbs soybean oil (18%)
- 1 lb waste (2%)
- **60 lbs input → 59 lbs output**

**Contract conversion:**

5,000 bushels soybeans produce:

- 240,000 lbs meal = 2.4 SM contracts (100 tons × 2,000 lbs)
- 55,000 lbs oil = 0.917 BO contracts (60,000 lbs)
- **Ratio: 1 ZS ≈ 2.4 SM + 0.917 BO**

**But traders use 1:1:11 ratio for simplicity:**

$$
\text{Long: } 1 \text{ SM} + 11 \text{ BO}
$$

$$
\text{Short: } 1 \text{ ZS}
$$

**P&L in cents per bushel:**

$$
\text{Crush (¢/bu)} = \frac{\text{Meal Price ($/ton)} \times 2000}{60} + \frac{\text{Oil Price (¢/lb)} \times 11}{1} - \text{Bean Price (¢/bu)}
$$

**Example:**

- Soybeans: $12.50/bushel = 1,250¢
- Meal: $350/ton
- Oil: 45¢/lb

$$
\text{Crush} = \frac{350 \times 2000}{60} + (45 \times 11) - 1250 = 11,667 + 495 - 1250 = 506¢/\text{bu}
$$

**This 506¢ = $5.06/bushel processing margin**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/inter_commodity_spreads.png?raw=true" alt="inter_commodity_spreads" width="700">
</p>
**Figure 1:** Inter-commodity spread relationships showing crack spread (crude oil to refined products), crush spread (soybeans to meal and oil), and substitution spreads (corn/wheat, gold/silver). The spreads represent processing margins or economic linkages that mean-revert around fair value, creating trading opportunities independent of absolute commodity price direction.

---

## Economic


**Beyond the basic mechanics, understanding the economic rationale:**

### 1. Processing


**The deep insight:**

Processing spreads represent **real business profitability** for refiners, crushers, and processors. When spreads are too wide, producers increase production. When too narrow, they reduce output. This supply response drives mean reversion.

**Formal representation:**

$$
\text{Processor Profit} = \text{Output Revenue} - \text{Input Cost} - \text{Processing Cost}
$$

**At equilibrium:**

$$
\text{Spread} = \text{Processing Cost} + \text{Normal Margin}
$$

**When spread > equilibrium:**

- High profitability
- Processors increase production
- Output supply ↑, input demand ↑
- Spread narrows
- **Mean reversion**

**When spread < equilibrium:**

- Low/negative profitability
- Processors reduce production
- Output supply ↓, input demand ↓
- Spread widens
- **Mean reversion**

### 2. Crack Spread


**Refinery decision-making:**

$$
\text{Refinery Profit} = \text{Product Sales} - \text{Crude Cost} - \text{Operating Cost}
$$

**Operating cost (fixed):**

$$
\text{OpEx} \approx \$5\text{-}\$15/\text{barrel}
$$

**Break-even crack spread:**

$$
\text{Break-even} = \text{OpEx} \approx \$10/\text{barrel (typical)}
$$

**Historical statistics:**

- Average crack spread: $15-25/barrel
- Below $10: Refineries lose money (reduce runs)
- Above $30: Excessive profits (increase runs)
- **Mean: ~$18-20/barrel**

**Supply response time:**

$$
\text{Production adjustment lag} = 2\text{-}4 \text{ weeks}
$$

**Example:**

**Crack spread widens to $35/barrel (excessive):**

**Week 1-2:**

- Refineries increase utilization: 85% → 92%
- Product output ↑ 8%
- Crude demand ↑ 8%

**Week 3-4:**

- Product supply floods market
- Gasoline/diesel prices fall
- Crude prices rise (higher demand)
- **Spread narrows to $22**

**This is why crack spreads mean-revert!**

### 3. Crush Spread


**Soybean processor decision-making:**

$$
\text{Processor Margin} = \text{Meal Revenue} + \text{Oil Revenue} - \text{Bean Cost} - \text{Processing Cost}
$$

**Processing cost:**

$$
\text{Processing} \approx 30\text{-}50¢/\text{bushel}
$$

**Break-even crush:**

$$
\text{Break-even} \approx 40¢/\text{bushel}
$$

**Historical statistics:**

- Average crush: 60-80¢/bushel
- Below 30¢: Crushers shut down
- Above 100¢: Crush at maximum capacity
- **Mean: ~70¢/bushel**

**Seasonal patterns:**

**Harvest (Sept-Nov):**

- Abundant beans
- Low bean prices
- Crush spread widens
- **Best time to short spread**

**Spring (Mar-May):**

- Tight bean supply
- High bean prices
- Crush spread narrows
- **Best time to long spread**

### 4. Substitution


**Corn/Wheat spread:**

**Economic relationship:**

$$
\text{Feed Demand} = f(\text{Corn Price}, \text{Wheat Price}, \text{Livestock Numbers})
$$

**Substitution ratio:**

$$
\text{If } \frac{\text{Corn}}{\text{Wheat}} < 0.90 \Rightarrow \text{Use corn}
$$

$$
\text{If } \frac{\text{Corn}}{\text{Wheat}} > 1.10 \Rightarrow \text{Use wheat}
$$

**Historical range:**

- Normal: Corn = 0.90-1.00 × Wheat
- Corn premium: 1.00-1.20 (drought years)
- Wheat premium: 0.70-0.90 (wheat surplus)
- **Mean-reverting around parity**

**Example:**

**2012 Drought:**

- Corn: $8.00/bushel
- Wheat: $6.50/bushel
- Ratio: 1.23 (extreme corn premium)

**Feed buyers switched to wheat:**

- Wheat demand ↑
- Corn demand ↓
- Ratio normalized to 1.05 within 6 months
- **Short corn/long wheat = profitable**

### 5. Gold/Silver Ratio


**Historical context:**

$$
\text{Gold/Silver Ratio} = \frac{\text{Gold Price}}{\text{Silver Price}}
$$

**Long-term average: 60-70**

**Mean reversion:**

- Ratio > 80: Silver undervalued → Long silver, short gold
- Ratio < 50: Silver overvalued → Short silver, long gold
- **Strong mean reversion (100+ years of data)**

**Economic drivers:**

**Industrial demand (silver):**

- 50% of silver = industrial use
- Economic growth → Silver demand ↑
- Ratio narrows (silver outperforms)

**Safe haven demand (gold):**

- Gold = pure safe haven
- Crisis → Gold demand ↑
- Ratio widens (gold outperforms)

**Example:**

**COVID crash (March 2020):**

- Gold: $1,700/oz
- Silver: $12/oz
- Ratio: 141 (all-time high!)
- **Extreme gold premium**

**Recovery (Aug 2020):**

- Gold: $2,000/oz (+18%)
- Silver: $28/oz (+133%)
- Ratio: 71 (normalized)
- **Long silver/short gold = massive profit**

### 6. Why Spreads


**Four fundamental forces:**

**1. Physical arbitrage:**

If crack spread too wide:

- Refiners profit excessively
- Increase production
- **Spread narrows**

**2. Substitution:**

If corn/wheat spread extreme:

- Buyers switch to cheaper grain
- Demand shift
- **Spread normalizes**

**3. Storage arbitrage:**

If spread wide enough:

- Store cheap commodity now
- Sell expensive later
- **Inventory builds, spread narrows**

**4. Statistical mean reversion:**

$$
\text{Spread}_t = \mu + \phi(\text{Spread}_{t-1} - \mu) + \epsilon_t
$$

Where $|\phi| < 1$ (mean-reverting)

**Half-life of deviation:**

$$
t_{1/2} = \frac{\ln(2)}{-\ln(\phi)} \approx 2\text{-}12 \text{ weeks}
$$

**Spreads revert faster than outright prices!**

---

## Key Terminology


**Inter-Commodity Spread:**

$$
\text{Spread} = \text{Price}_A - \text{Price}_B \times \text{Ratio}
$$

- Simultaneous long/short in related commodities
- Market-neutral to absolute prices
- Profits from relationship changes
- Lower volatility than outrights

**Crack Spread:**

$$
\text{Crack} = \text{Refined Products} - \text{Crude Oil}
$$

- Refinery processing margin
- 3-2-1 most common (3 crude → 2 gas + 1 diesel)
- Measured in $/barrel
- Mean-reverting around $15-25

**Crush Spread:**

$$
\text{Crush} = \text{Meal} + \text{Oil} - \text{Soybeans}
$$

- Soybean processing margin
- Measured in ¢/bushel
- Seasonal patterns (harvest/spring)
- Mean: 60-80¢/bushel

**Spark Spread:**

$$
\text{Spark} = \text{Electricity Price} - (\text{Gas Price} \times \text{Heat Rate})
$$

- Power plant profit margin
- Heat rate = efficiency (6-10 MMBtu/MWh)
- Regional variations
- Mean-reverting around costs

**Processing Margin:**

$$
\text{Margin} = \text{Output Revenue} - \text{Input Cost} - \text{Processing Cost}
$$

- What processors earn
- Drives production decisions
- Mean-reverts to break-even + normal profit
- **Economic anchor**

**Substitution Ratio:**

$$
\text{Ratio} = \frac{\text{Commodity A Price}}{\text{Commodity B Price}}
$$

- Price relationship between substitutes
- Corn/wheat typically 0.90-1.10
- Gold/silver typically 50-80
- **Mean-reverting**

**Backwardation/Contango (in spreads):**

Not the same as calendar spreads!

- Spread > historical average: "Wide" or "rich"
- Spread < historical average: "Narrow" or "cheap"
- **Reversion to mean**

**Fair Value:**

$$
\text{Fair Value} = \text{Historical Mean} + \text{Fundamental Adjustments}
$$

- Long-term average spread level
- Adjusted for structural changes
- Target for mean reversion
- **Trading anchor**

**Z-Score:**

$$
z = \frac{\text{Current Spread} - \text{Mean Spread}}{\text{Std Dev of Spread}}
$$

- Measures deviation in standard deviations
- |z| > 2: Extreme (trade opportunity)
- |z| < 1: Normal (skip)
- **Entry/exit signal**

**Basis Risk:**

- Risk that spread doesn't revert
- Structural changes
- Permanent shifts in fundamentals
- **Why stops are needed**

**Carrying Cost:**

- Interest on margin
- Contango/backwardation in each leg
- Transaction costs
- **Reduces net profit**

---

## The Greeks (Spread


**While commodity spreads don't have traditional option Greeks, we can define analogous sensitivities:**

### 1. Delta


**Definition:** How spread value changes with absolute commodity price movements.

**For a well-constructed spread:**

$$
\Delta_{\text{spread}} \approx 0 \quad \text{(market-neutral)}
$$

**Example (Crack spread):**

**Perfect hedge:**

- Long: 2 RBOB + 1 HO
- Short: 3 CL
- If crude +$10/barrel:
  - Products typically: +$10/barrel each
  - P&L: (2 × +10 + 1 × +10) - (3 × +10) = 0
- **Delta-neutral**

**In practice:**

$$
\Delta_{\text{spread}} = 0.05\text{-}0.15
$$

**Why not perfect:**

- Product-crude correlation not exactly 1.0
- Different demand drivers
- Refining capacity constraints
- **Small residual delta**

**Example:**

Crude rallies $20:

- Gasoline: +$18
- Diesel: +$19
- Crack spread change: (2 × 18 + 19)/3 - 20 = -$1.33/barrel
- **Slight negative delta to crude**

**Management:**

- Usually ignore (small impact)
- Or adjust ratio for perfect hedge
- **Focus on spread, not delta**

### 2. Gamma (Convexity)


**Definition:** How delta changes as prices move.

$$
\Gamma_{\text{spread}} \approx 0
$$

**Commodity futures are linear:**

- No gamma in individual legs
- No gamma in spread
- **Unlike options**

**Exception: Non-linear relationships**

**Spark spread with heat rate curve:**

At very high gas prices:

- Power plants become uneconomical
- Shut down (non-linear response)
- **Gamma-like effect**

**But for most spreads:**

- Linear relationships
- No gamma
- **Simpler risk profile**

### 3. Theta (Time Decay


**Definition:** How spread changes with time passage (assuming fundamentals unchanged).

$$
\Theta_{\text{spread}} = \frac{d(\text{Spread})}{dt}
$$

**For mean-reverting spreads:**

$$
\Theta = -\kappa(\text{Spread}_t - \mu)
$$

Where:
- $\kappa$ = reversion speed
- $\mu$ = long-term mean
- **Negative feedback**

**Example (wide crack spread):**

- Current: $32/barrel (wide)
- Mean: $20/barrel
- Reversion speed: $\kappa = 0.1$ per week

$$
\text{Expected weekly change} = -0.1 \times (32 - 20) = -1.2/\text{week}
$$

**Spread decays $1.20/week toward $20 mean**

**Theta is POSITIVE for spreads trading back to mean:**

- Wide spread → Short spread → Theta positive (earns as narrows)
- Narrow spread → Long spread → Theta positive (earns as widens)
- **Mean reversion = positive theta**

### 4. Vega (Volatility


**Definition:** How spread responds to changes in volatility of underlying commodities.

**Spread volatility < underlying volatility:**

$$
\sigma_{\text{spread}} = \sqrt{\sigma_A^2 + \sigma_B^2 - 2\rho\sigma_A\sigma_B}
$$

**Example (Crack spread):**

- Crude volatility: 35%
- Product volatility: 40%
- Correlation: 0.85

$$
\sigma_{\text{crack}} = \sqrt{0.40^2 + 0.35^2 - 2 \times 0.85 \times 0.40 \times 0.35} = 18\%
$$

**Spread volatility (18%) < Component volatility (35-40%)**

**Why lower:**

- Positive correlation reduces variance
- Offsetting movements
- **Natural hedge**

**Implication:**

- Lower margin requirements
- Less capital at risk
- Better risk-adjusted returns
- **Attractive characteristics**

### 5. Rho (Interest


**Definition:** How spread value changes with interest rates.

**For commodity spreads:**

$$
\rho_{\text{spread}} \approx 0
$$

**Rationale:**

- Both legs affected equally by rates
- Financing costs offset
- **Net effect minimal**

**Exception: Storage-driven spreads**

Higher rates → higher carry cost → steeper contango:

- Calendar spreads affected
- Inter-commodity spreads less so
- **Secondary effect**

### 6. Correlation Risk


**Definition:** Risk that correlation between legs changes.

$$
\text{Correlation Risk} = \frac{\partial \text{Spread Variance}}{\partial \rho}
$$

**Example:**

**Normal market:**

- Crude-product correlation: 0.85
- Spread volatility: 18%

**Crisis market:**

- Crude-product correlation: 0.65
- Spread volatility: 28% (55% increase!)

**Why correlation breaks:**

- Supply disruptions affect one commodity
- Demand shocks hit products vs crude differently
- Refining capacity constraints
- **Basis risk**

**Example: Hurricane**

- Crude supply unaffected: +0%
- Gulf Coast refineries shut: Products +30%
- **Crack spread explodes**
- **Correlation risk realized**

---

## Spread Selection


**Just as traders select securities, spread traders must select optimal spreads:**

### 1. Crack Spreads


**3-2-1 Crack Spread:**

**Characteristics:**

- Highest liquidity (10k+ spreads traded daily)
- Tightest bid-ask ($0.10-0.20/barrel)
- Clear fundamentals (refinery margins)
- Seasonal patterns (summer gas demand)
- **Best for beginners**

**Historical statistics:**

- Mean: $18-20/barrel
- Range: $5-35/barrel
- Std dev: $5-7/barrel
- Mean reversion half-life: 4-8 weeks

**When to trade:**

**Long crack (wide products, cheap crude):**

- Crack < $12/barrel (z-score < -1.5)
- Refinery utilization low (<85%)
- Gasoline demand season approaching (May-Aug)
- **Entry signal**

**Short crack (expensive products, cheap crude):**

- Crack > $28/barrel (z-score > +1.5)
- Refinery utilization high (>92%)
- Post-summer demand decline (Sept-Nov)
- **Entry signal**

**Pros:**

- Extremely liquid
- Well-understood fundamentals
- Predictable seasonality
- Institutional quality data
- **Professional-grade spread**

**Cons:**

- Refinery maintenance affects supply
- Hurricane risk (Gulf Coast)
- Regulatory changes (RIN credits)
- **Requires fundamental analysis**

### 2. Crush Spreads


**Soybean Crush:**

**Characteristics:**

- Good liquidity (1k-3k spreads/day)
- Clear fundamentals (processor margins)
- Strong seasonality (harvest/planting)
- USDA data provides transparency
- **Great for intermediate traders**

**Historical statistics:**

- Mean: 65-75¢/bushel
- Range: 20-120¢/bushel
- Std dev: 15-20¢/bushel
- Mean reversion half-life: 6-12 weeks

**Seasonal patterns:**

**Harvest (Oct-Nov):**

- Abundant beans
- Crush spread widens
- **Short crush opportunity**

**Spring (Apr-May):**

- Tight bean supply
- Crush spread narrows
- **Long crush opportunity**

**When to trade:**

**Long crush:**

- Spread < 45¢/bushel (very narrow)
- Spring tightness
- Strong meal/oil demand (China buying)
- **Entry signal**

**Short crush:**

- Spread > 95¢/bushel (very wide)
- Post-harvest
- Weak meal/oil demand
- **Entry signal**

**Pros:**

- Strong seasonality (predictable)
- USDA reports provide data
- Processor behavior well-known
- Good risk/reward
- **Reliable patterns**

**Cons:**

- South American crop affects (Brazil, Argentina)
- Chinese demand volatile
- Disease outbreaks (African swine fever)
- **Global complexity**

### 3. Gold/Silver Ratio


**Characteristics:**

- Very liquid (precious metals popular)
- 100+ years of data
- Strong mean reversion (ratio 50-80)
- Macro/safe-haven driven
- **Good for macro traders**

**Historical statistics:**

- Mean: 65-70
- Range: 40-140 (extremes rare)
- Std dev: 10-15
- Mean reversion half-life: 3-9 months

**When to trade:**

**Long silver, short gold (ratio > 80):**

- Extreme safe-haven premium in gold
- Silver undervalued vs gold
- **Reversion trade**

**Short silver, long gold (ratio < 55):**

- Excessive silver premium
- Industrial demand priced in
- **Reversion trade**

**Example:**

**COVID crash (March 2020):**

- Ratio: 125 (extreme gold premium)
- Trade: Long silver, short gold
- 6 months later: Ratio 71
- **Profit: ~40% on notional**

**Pros:**

- Very liquid
- Long historical data
- Macro indicator (informative)
- No processing/crop risk
- **Clean technical trade**

**Cons:**

- Slow mean reversion (months)
- Macro regime shifts possible
- Dollar correlation
- Central bank policy affects
- **Requires patience**

### 4. Corn/Wheat Spread


**Characteristics:**

- Moderate liquidity
- Feed demand driver
- Ratio mean-reverts 0.90-1.10
- Weather affects both
- **Agricultural specialists**

**When to trade:**

**Long corn, short wheat (ratio < 0.85):**

- Corn cheap vs wheat
- Feed buyers will switch
- **Demand shift coming**

**Short corn, long wheat (ratio > 1.15):**

- Corn expensive vs wheat
- Feed buyers switching to wheat
- **Demand shift coming**

**Pros:**

- Clear substitution economics
- Predictable switching behavior
- USDA data available
- **Mean reversion reliable**

**Cons:**

- Both affected by weather
- Global wheat market complex
- Feed demand changes
- **Correlation risk**

### 5. Comparison Table


| Spread | Liquidity | Complexity | Mean Reversion | Best For |
|--------|-----------|------------|----------------|----------|
| 3-2-1 Crack | Excellent | Medium | 4-8 weeks | All traders |
| Soy Crush | Good | Medium | 6-12 weeks | Ag specialists |
| Gold/Silver | Excellent | Low | 3-9 months | Macro traders |
| Corn/Wheat | Moderate | High | 4-12 weeks | Ag experts |
| WTI/Brent | Excellent | Medium | 2-6 weeks | Energy traders |
| Spark | Low | High | Varies | Power specialists |

**Beginner recommendation: Start with 3-2-1 crack spread (most liquid, best data, clearest fundamentals)**

---

## Time Selection


**Timing is critical for spread trading:**

### 1. Optimal Entry


**Statistical approach:**

$$
\text{Enter when: } |z\text{-score}| > 2.0
$$

$$
z = \frac{\text{Current Spread} - \text{Historical Mean}}{\text{Historical Std Dev}}
$$

**Example (Crack spread):**

- Historical mean: $19/barrel
- Std dev: $6/barrel
- Current: $31/barrel

$$
z = \frac{31 - 19}{6} = 2.0
$$

**Signal: Short crack spread (extreme wide)**

**Fundamental approach:**

**Check key indicators:**

**For crack spread:**

1. Refinery utilization (>92% = narrow, <85% = wide)
2. Product inventories (high = narrow, low = wide)
3. Crude supply (surplus = wide, tight = narrow)
4. Seasonal patterns (summer = wide, winter = narrow)

**For crush spread:**

1. Processor margins (>100¢ = short, <40¢ = long)
2. Bean supply (post-harvest = wide, spring = narrow)
3. Meal/oil demand (China buying = wide)
4. South American crop (large = narrow)

**Seasonal timing:**

**Crack spread:**

**Best long crack: February-April**

- Refineries transitioning to summer gasoline
- Demand building
- Crack tends to widen
- **Seasonal tailwind**

**Best short crack: September-October**

- End of driving season
- Refineries switching to heating oil
- Crack tends to narrow
- **Seasonal headwind**

**Crush spread:**

**Best long crush: March-May**

- Pre-planting season
- Bean supply tight
- Crush narrows
- **Spring tightness**

**Best short crush: October-November**

- Post-harvest
- Abundant beans
- Crush widens
- **Harvest pressure**

### 2. When NOT to Enter


**Avoid these situations:**

**1. During delivery/expiration weeks:**

- Spreads can behave erratically
- Delivery logistics distort prices
- Illiquidity spikes
- **Wait until after**

**2. Around major data releases:**

**Energy (DOE/EIA reports):**

- Wednesday 10:30 AM ET
- Inventory data
- Spreads gap
- **Skip Tues PM/Wed AM**

**Agriculture (USDA reports):**

- WASDE: 12 PM ET (monthly)
- Grain stocks: Quarterly
- Planting/acreage: Spring
- **Major volatility**

**3. Weather events approaching:**

**Hurricanes (crack spread):**

- Gulf Coast refineries threatened
- Spreads can explode
- Unpredictable
- **Exit positions**

**Drought/floods (crush spread):**

- Crop damage affects beans
- But also affects meal demand (livestock)
- Correlation breaks
- **Basis risk**

**4. Structural changes underway:**

**Refining capacity changes:**

- New refineries opening (Asia)
- Old refineries closing (Europe)
- Shifts crack spread equilibrium
- **Wait for new normal**

**Biofuel mandates:**

- Renewable diesel demand
- Affects diesel crack
- Structural shift
- **Reassess fair value**

### 3. Exit Strategy


**Profit target approach:**

$$
\text{Exit when: } \text{Spread} = \text{Mean} \pm 0.5\sigma
$$

**Example:**

- Entry: Short crack @ $31 (z = 2.0)
- Mean: $19
- Target: $19 + 0.5 × $6 = $22
- **Exit at $22, profit $9/barrel**

**Why not wait for mean:**

- Last 10-20% takes longest
- Risk reversal
- Opportunity cost
- **Take 70-80% of max**

**Time-based stop:**

$$
\text{Exit if no progress after } 8\text{-}12 \text{ weeks}
$$

**Rationale:**

- Mean reversion half-life 4-8 weeks
- By week 12, should see movement
- If not, something changed
- **Cut it loose**

**Fundamental shift exit:**

**Crack spread example:**

- Entered short @ $31
- Week 4: Still $30
- News: Major refinery explosion
- Capacity offline 6 months
- **Fundamental change = exit immediately**

**Don't wait for target when thesis breaks!**

**Rolling positions:**

**As front month approaches expiration:**

- Roll both legs to next month
- Maintain spread exposure
- Avoid delivery
- **Continuous position**

**Example (Crack spread roll):**

- Have: Short Mar crude, Long Mar RBOB/HO
- Feb 15: Roll to Apr contracts
- Execute spread order (better pricing)
- **Maintain exposure**

---

## Maximum Profit and


### 1. Long Crack Spread


**Setup:**

- Date: October 2024
- Crack spread: $11/barrel (very narrow, z = -1.8)
- Historical mean: $19/barrel
- Trade: Long 10 crack spreads

**Position:**

- Long: 20 RBOB + 10 HO
- Short: 30 CL
- Margin: ~$25,000 per spread = $250,000 total

**Maximum Profit (Spread Widens to Mean):**

**90 days later:**

- Crack widens: $11 → $22/barrel
- Convergence: $11/barrel

$$
\text{Profit} = \$11 \times 1,000 \times 10 = \$110,000
$$

$$
\text{Return on margin} = \frac{\$110,000}{\$250,000} = 44\%
$$

**In 90 days → Annualized: 176%**

**Maximum Loss (Spread Narrows Further):**

**Worst case scenario:**

- Refinery shutdown cascade
- Product glut
- Crack narrows: $11 → $5/barrel
- Loss: $6/barrel

$$
\text{Loss} = -\$6 \times 1,000 \times 10 = -\$60,000
$$

$$
\text{Return} = \frac{-\$60,000}{\$250,000} = -24\%
$$

**But stopped out at -$3 typically:**

$$
\text{Actual loss} = -\$3 \times 1,000 \times 10 = -\$30,000
$$

$$
\text{Return} = -12\%
$$

### 2. Short Crush


**Setup:**

- Date: November 2024 (post-harvest)
- Crush spread: 105¢/bushel (very wide, z = +2.1)
- Historical mean: 70¢/bushel
- Trade: Short 20 crush spreads

**Position:**

- Short: 20 SM + 220 BO
- Long: 20 ZS
- Margin: ~$3,000 per spread = $60,000 total

**Maximum Profit (Spread Narrows to Mean):**

**60 days later:**

- Crush narrows: 105¢ → 68¢/bushel
- Convergence: 37¢/bushel

**P&L calculation (per spread):**

$$
\text{Profit} = 37¢ \times 5,000 \text{ bu} = \$1,850
$$

$$
\text{Total} = \$1,850 \times 20 = \$37,000
$$

$$
\text{Return} = \frac{\$37,000}{\$60,000} = 62\%
$$

**In 60 days → Annualized: 372%**

**Maximum Loss (Spread Widens Further):**

**Disaster scenario:**

- Chinese buying surge
- Meal demand explodes
- Crush widens: 105¢ → 125¢/bushel
- Loss: 20¢/bushel

$$
\text{Loss} = -20¢ \times 5,000 \times 20 = -\$20,000
$$

$$
\text{Return} = \frac{-\$20,000}{\$60,000} = -33\%
$$

**With stop at 115¢:**

$$
\text{Loss} = -10¢ \times 5,000 \times 20 = -\$10,000 \text{ (-17\%)}
$$

### 3. Gold/Silver Ratio


**Setup:**

- Date: March 2020
- Ratio: 125 (extreme gold premium)
- Historical mean: 70
- Trade: Long silver, short gold

**Position:**

- Long: 40 silver futures (5,000 oz each)
- Short: 3 gold futures (100 oz each)
- Ratio: 40 × 5,000 / (3 × 100) = 666 oz silver per oz gold
- Margin: ~$80,000

**Maximum Profit (Ratio Normalizes):**

**6 months later:**

- Gold: $1,700 → $1,950 (+15%)
- Silver: $12 → $27 (+125%)
- Ratio: 125 → 72 (normalized)

**P&L:**

**Silver profit:**

$$
(27 - 12) \times 5,000 \times 40 = \$3,000,000
$$

**Gold loss:**

$$
(1,950 - 1,700) \times 100 \times 3 = -\$75,000
$$

**Net:**

$$
\$3,000,000 - \$75,000 = \$2,925,000
$$

**Wait, that's massive! Let me recalculate properly:**

**Position sizing (proper):**

- Long 10 silver @ $12 ($60,000 notional each)
- Short 2 gold @ $1,700 ($170,000 notional each)
- Net notional: ~$200,000
- Margin: $80,000

**Profit:**

$$
\text{Silver: } (27 - 12) \times 5,000 \times 10 = \$750,000
$$

$$
\text{Gold: } -(1,950 - 1,700) \times 100 \times 2 = -\$50,000
$$

$$
\text{Net: } \$700,000
$$

$$
\text{Return: } \frac{\$700,000}{\$80,000} = 875\%
$$

**This is why ratio trades can be so profitable!**

**Maximum Loss (Ratio Widens More):**

**If crisis deepens:**

- Gold → $2,000
- Silver → $10
- Ratio → 200

**Loss:**

$$
\text{Silver: } (10 - 12) \times 5,000 \times 10 = -\$100,000
$$

$$
\text{Gold: } -(2,000 - 1,700) \times 100 \times 2 = -\$60,000
$$

$$
\text{Net: } -\$160,000 \text{ (-200\%!)}
$$

**This is the risk of catching falling knives!**

---

## When to Use


### 1. Ideal Market


**Use spreads when:**

**1. Clear mean reversion opportunity:**

$$
|z\text{-score}| > 2.0
$$

**Current spread far from historical mean:**

- Crack spread at $32 (mean $19)
- Crush spread at 45¢ (mean 70¢)
- Gold/silver ratio at 90 (mean 65)
- **Statistical edge**

**2. Fundamental catalyst for reversion:**

**Crack spread narrow + summer approaching:**

- Gasoline demand will rise
- Products should rally vs crude
- **Fundamental + seasonal**

**Crush spread wide + spring planting:**

- Bean supply will tighten
- Beans should rally vs products
- **Fundamental timing**

**3. Low absolute volatility in commodities:**

**When crude, metals, ags are range-bound:**

- Spreads still mean-revert
- But less directional noise
- **Cleaner signal**

**4. Strong correlation historically:**

$$
\rho(\text{Leg A}, \text{Leg B}) > 0.70
$$

**High correlation = lower spread volatility = better risk/reward**

**5. Institutional flows supporting:**

**Refineries increasing runs:**

- Crack spread should narrow
- Physical market confirming
- **Flow alignment**

**Processors shutting down:**

- Crush spread should narrow
- Physical market confirming
- **Flow alignment**

### 2. Specific Use


**Use Case 1: Hedging production costs**

**Oil refiner:**

- Buys crude, sells products
- Natural long crack spread exposure
- Can lock in margin via futures
- **Business hedge**

**Soybean processor:**

- Buys beans, sells meal/oil
- Natural long crush exposure
- Lock in processing margin
- **Business hedge**

**Use Case 2: Macro positioning**

**Expecting economic slowdown:**

- Long gold/silver ratio (safe haven)
- Short copper/gold ratio (growth slowdown)
- **Macro view expressed**

**Expecting reflation:**

- Short gold/silver ratio (industrial demand)
- Long copper/gold ratio (growth)
- **Macro view expressed**

**Use Case 3: Pure statistical arbitrage**

**Quantitative strategy:**

- Screen all spreads daily
- Enter when |z| > 2.5
- Exit when |z| < 0.5
- **Systematic mean reversion**

**Use Case 4: Relative value in portfolio**

**Instead of outright crude oil long:**

- Long crack spread (refined products vs crude)
- Less volatility
- Lower margin
- **Better risk-adjusted**

---

## When NOT to Use


### 1. Avoid These


**1. Structural changes occurring:**

**Energy transition:**

- Electric vehicles reducing gasoline demand
- Crack spread equilibrium shifting
- **Don't fight secular trends**

**Biofuel mandates:**

- Renewable diesel competing with petroleum diesel
- Changes diesel crack permanently
- **New normal emerging**

**2. Correlation breakdown:**

**Hurricane threatening Gulf Coast:**

- Products spike
- Crude unaffected
- Crack spread explodes
- **Correlation = 0.30 instead of 0.85**

**African swine fever:**

- Meal demand collapses (less livestock)
- Oil demand unchanged
- Crush spread dynamics broken
- **Relationship severed**

**3. Both legs trending same direction:**

**Example: Both crude and products rallying:**

- War premium affects both
- Spread may not revert
- Better to trade outright
- **No spread edge**

**4. Insufficient liquidity:**

**Exotic spreads:**

- Palladium/platinum (low volume)
- Live cattle/lean hogs (niche)
- Regional power spreads
- **Wide bid-ask, poor fills**

**5. Can't monitor fundamentals:**

**Crush spread requires:**

- USDA reports
- South American crop monitoring
- Chinese demand tracking
- **Active fundamental analysis**

**If you can't dedicate time:**

- Don't trade
- Fundamentals drive these spreads
- **Requires attention**

**6. During delivery/roll weeks:**

**Delivery mechanics distort spreads:**

- Physical settlement logistics
- Basis risk
- Temporary dislocations
- **Wait until after**

**7. Regime changes:**

**COVID crash:**

- All historical correlations broke
- Spreads moved to extremes
- Mean reversion failed
- **Unprecedented times**

**2008 financial crisis:**

- Correlations→1.0 (everything fell)
- Spreads dislocated
- Liquidity vanished
- **Crisis regime**

### 2. Warning Signs to


**1. Spread moving against you AND fundamentals worsening:**

**Example:**

- Short crack @ $31
- Week 3: $34 (wrong way)
- News: Refinery capacity cuts announced
- **Exit immediately**

**2. Correlation collapsing:**

**Example:**

- Long crush spread
- Bean-meal correlation drops from 0.80 → 0.40
- Spread volatility doubles
- **Risk profile changed**

**3. Time stop triggered:**

$$
\text{Position held } > 12 \text{ weeks with no progress}
$$

- Mean reversion not happening
- Something structurally changed
- **Cut loss**

**4. Major event approaching:**

**Hurricane:**

- Threatening Gulf refineries
- Crack spread unpredictable
- **Close position**

**USDA surprise:**

- Crop size shock possible
- Crush spread could gap
- **Reduce exposure**

---

## Position Sizing and


### 1. The Golden Rule


**Standard position sizing:**

$$
\text{Contracts} = \frac{\text{Account Risk (2\%)}}{\text{Spread Risk per Contract}}
$$

**Example:**

**Account: $500,000**

**Risk tolerance: 2% = $10,000**

**Crack spread:**

- Entry: $31/barrel
- Stop: $34/barrel
- Risk: $3/barrel per spread

$$
\text{Spreads} = \frac{\$10,000}{\$3,000} = 3.3 \approx 3
$$

**Trade: 3 crack spreads**

**Crush spread:**

- Entry: 105¢/bushel
- Stop: 115¢/bushel
- Risk: 10¢ × 5,000 bu = $500 per spread

$$
\text{Spreads} = \frac{\$10,000}{\$500} = 20
$$

**Trade: 20 crush spreads**

### 2. Portfolio


**Conservative:**

- 5% of portfolio in spreads
- $500k account → $25k in spreads
- **Mostly in core positions**

**Moderate:**

- 10-15% of portfolio
- $500k → $50-75k
- **Core strategy component**

**Aggressive (specialists):**

- 20-30% of portfolio
- $500k → $100-150k
- **Primary strategy**

**Never >30% in spreads:**

- Need diversification
- Spreads can trend against you
- Require active management
- **Not set-and-forget**

### 3. Stop Loss


**Statistical stops:**

$$
\text{Stop} = \text{Entry} \pm 1.5 \times \text{Historical Std Dev}
$$

**Example (Crack spread):**

- Entry: Short @ $31
- Std dev: $6
- Stop: $31 + (1.5 × $6) = $40
- **Exit if hits $40**

**Fundamental stops:**

**If thesis breaks, exit regardless of P&L:**

**Example:**

- Short crack @ $31 (expecting narrow)
- Refinery explosion announced (capacity loss)
- **Exit immediately at market**

**Don't wait for statistical stop when fundamentals change!**

**Time-based stops:**

$$
\text{Exit if no progress after } 8\text{-}12 \text{ weeks}
$$

**Mean reversion should happen by then**

### 4. Margin Management


**Spread margin << outright margin:**

**Example:**

**Outright positions:**

- Long 3 CL: $21,000 margin
- Long 2 RBOB: $14,000 margin
- Total: $35,000

**Crack spread (same contracts):**

- Short 3 CL, Long 2 RBOB + 1 HO
- Spread margin: $25,000
- **Savings: $10,000 (29%)**

**Why lower:**

- Recognized hedge relationship
- Lower volatility
- Offsetting positions
- **Margin credit**

**Reserve requirements:**

$$
\text{Keep } 2\text{-}3\times \text{ margin in cash}
$$

**For $100k in spreads:**

- Margin posted: $100k
- Cash reserve: $200-300k
- Total capital: $300-400k
- **Coverage ratio 3:1-4:1**

### 5. Diversification


**Across spread types:**

**Don't concentrate:**

- 10 crack spreads
- 0 others
- **Too concentrated**

**Better:**

- 3 crack spreads
- 5 crush spreads
- 2 gold/silver ratios
- **Diversified**

**Across time:**

- Don't enter all on same day
- Stagger entries over weeks
- Different entry points
- **Smooth P&L**

**Across directions:**

- Some long spreads
- Some short spreads
- Natural portfolio hedge
- **Balanced**

### 6. Account: $500,000


**Account: $500,000**

**Allocation to spreads: 15% = $75,000**

**Positions:**

**Position 1: Short 3 Crack Spreads**

- Entry: $31/barrel
- Stop: $34/barrel
- Margin: $25,000 × 3 = $75,000
- Risk: $3/barrel × $1,000 × 3 = $9,000
- Account risk: 1.8%

**Position 2: Long 10 Crush Spreads**

- Entry: 48¢/bushel
- Stop: 43¢/bushel
- Margin: $3,000 × 10 = $30,000
- Risk: 5¢ × 5,000 × 10 = $2,500
- Account risk: 0.5%

**Position 3: Long Silver/Short Gold (Ratio 90)**

- Entry: Ratio 90
- Stop: Ratio 100
- Margin: $40,000
- Risk: Calculated based on delta
- Account risk: 2.0%

**Total:**

- Margin deployed: $145,000
- Cash reserve: $355,000
- Total risk: $9,000 + $2,500 + $10,000 = $21,500
- Account risk: 4.3%
- **Within 5% limit**

**Maximum drawdown scenario (all stops hit):**

$$
\text{Loss} = \$21,500 \text{ (4.3\% of account)}
$$

**Acceptable for spread trading!**

---

## Common Mistakes


### 1. The error: See


**The error:**

- See crude oil bullish
- Think: "I'll long crack spread"
- **Crack spread = long products, short crude**

**What happens:**

- Crude rallies $10
- Products rally $8
- Crack spread NARROWS
- **Loss despite being right on crude!**

**Correct approach:**

**Spread trading is relationship trading:**

- Don't care about direction
- Care about spread width
- Ignore absolute prices
- **Focus on spread level**

### 2. The error: Crack


**The error:**

- Crack spread at $32 (wide)
- z-score = +2.0 (extreme)
- Short spread blindly
- **Don't check why it's wide**

**Reality check:**

- Gulf Coast refinery fire
- 20% capacity offline for 6 months
- Spread SHOULD be wide
- **Fundamental justification**

**Result:**

- Spread stays wide at $32-35
- No mean reversion
- **Loss from ignoring fundamentals**

**Correct approach:**

**Always ask: WHY is spread extreme?**

- Temporary disruption → Trade
- Structural change → Skip
- **Fundamentals first**

### 3. The error: Crush


**The error:**

**Crush spread:**

- Long 1 SM (soybean meal)
- Long 1 BO (soybean oil)
- Short 1 ZS (soybeans)
- **Wrong ratio!**

**Correct ratio: 1 SM + 11 BO : 1 ZS**

**Or use 1:1:1 but understand hedge ratio is imperfect**

**What happens with 1:1:1:**

- Beans rally $1/bushel
- Meal rallies $20/ton
- Oil rallies 5¢/lb
- **Not perfectly hedged**

**P&L:**

$$
\text{Meal: } +\$20 \times 100 \text{ tons} = +\$2,000
$$

$$
\text{Oil: } +5¢ \times 60,000 \text{ lbs} = +\$3,000
$$

$$
\text{Beans: } -\$1.00 \times 5,000 \text{ bu} = -\$5,000
$$

$$
\text{Net: } \$0
$$

**Lucky break-even, but ratio risk exists!**

**Correct approach:**

**Use proper ratios:**

- Crack: 2 RBOB + 1 HO : 3 CL
- Crush: 1 SM + 11 BO : 1 ZS
- **Industry standard for reason**

### 4. The error: Long


**The error:**

- Long crack spread in June contracts
- June delivery week arrives
- Still holding
- **Delivery chaos**

**What happens:**

- Products delivered to NY Harbor
- Crude delivered to Cushing
- Logistics complications
- Spreads dislocate
- **Forced to roll at bad prices**

**Correct approach:**

$$
\text{Roll positions } 7\text{-}10 \text{ days before first delivery day}
$$

**Calendar dates:**

- Mark all delivery dates
- Set alerts
- Roll proactively
- **Never surprised**

### 5. The error: Short


**The error:**

- Short crack @ $31 (expecting narrow to $20)
- Widens to $35
- Think: "It MUST revert, I'll hold"
- Widens to $40
- **Still holding (denial)**

**What happens:**

**Major refinery shutdown:**

- Capacity permanently reduced
- New equilibrium = $35/barrel
- Spread never reverts to $20
- **Fundamental change**

**Loss:**

$$
(\$40 - \$31) \times 1,000 \times 10 = -\$90,000
$$

**If had stop at $34:**

$$
(\$34 - \$31) \times 1,000 \times 10 = -\$30,000
$$

**Saved $60,000 by using stop!**

**Correct approach:**

**Mean reversion is PROBABLE, not CERTAIN:**

- Always use stops
- Fundamentals can change
- **Protect capital**

### 6. The error: Crack


**The error:**

- Crack spread margin: $25k per spread
- Think: "Only $25k, I can do 10 spreads!"
- Enter 10 spreads ($250k margin)
- **Overleveraged**

**What happens:**

- Spread moves $4 against you
- Loss: $4 × 1,000 × 10 = -$40,000
- Margin call: Additional $50,000 needed
- **Can't meet it**

**Correct approach:**

**Size by RISK, not margin:**

$$
\text{Risk per spread} = \text{Stop distance} \times \$1,000
$$

$$
\text{Max spreads} = \frac{\text{Account Risk}}{\text{Risk per Spread}}
$$

**Don't be fooled by low margin requirements!**

### 7. The error: Short


**The error:**

**Short crush spread in March:**

- Crush at 75¢ (normal, z = 0)
- Think: "Will narrow"
- **Wrong season!**

**Spring crush typically narrows:**

- Bean supply tightens
- Crush should go to 50-60¢
- **Seasonal headwind**

**Result:**

- Crush narrows to 55¢ (as expected seasonally)
- Short loses money
- **Fought seasonal pattern**

**Correct approach:**

**Know the seasons:**

- Crack: Wide in summer, narrow in winter
- Crush: Wide post-harvest, narrow in spring
- Corn/wheat: Depends on crop cycle
- **Trade WITH seasons**

### 8. The error:


**The error:**

- Gold/silver ratio spikes to 125
- Think: "Wow, must short!"
- Ratio continues to 140 (COVID panic)
- **Caught falling knife**

**What happens:**

- Shorted ratio 125
- Ratio to 140
- **Loss: 12% despite being "right" on extreme**

**Correct approach:**

**Wait for confirmation:**

- Ratio peaks at 141
- Starts declining: 141 → 130
- THEN enter short ratio
- **Patience for reversal**

**Or use staged entry:**

- Short 25% at 125
- Short 25% at 135
- Short 50% on decline to 130
- **Average in**

### 9. The error: Enter


**The error:**

- Enter crush spread in old crop Nov beans
- New crop planted
- Old crop expires
- **Forced to exit**

**Better approach:**

**Roll to new crop:**

- Exit old crop Nov beans spread
- Enter new crop Nov beans spread
- **Maintain exposure**

**Timing:**

- Roll 30-60 days before expiration
- When liquidity shifts to new crop
- **Follow the market**

### 10. The error: Enter


**The error:**

- Enter crack spread
- Crude-product correlation: 0.85 (normal)
- Hurricane hits
- Correlation drops to 0.50
- Spread volatility doubles
- **Risk exploded**

**What happens:**

- Entered with 3% risk based on historical volatility
- Volatility doubles
- Now risking 6%
- Margin requirements increase
- **Unexpected risk**

**Correct approach:**

**Monitor correlation:**

- Track crude-product correlation daily
- If drops below 0.70 → Reduce size
- If crisis → Exit entirely
- **Dynamic risk management**

---



## Final Wisdom


> "Inter-commodity spreads offer one of the purest mean-reversion strategies in markets—the economic relationships between crude and products, beans and meal/oil, gold and silver are anchored by physical processing costs and substitution dynamics. When spreads deviate from fair value, supply and demand forces drive reversion. But 'mean reversion' is not a law of nature—it's a tendency that requires stable fundamentals. Structural changes (refinery closures, disease outbreaks, energy transitions) can shift equilibrium permanently. The successful spread trader combines statistical rigor (z-scores, historical ranges) with fundamental analysis (why is spread extreme?) and disciplined risk management (stops, proper sizing). Trade WITH fundamentals and seasons, not against them. Remember: spreads are lower risk than outrights, but they're not risk-free. Respect the physical economics, size conservatively, and always use stops."

**Most important principles:**

- Spreads represent real economic relationships (processing margins, substitution)
- Mean reversion requires stable fundamentals (not guaranteed)
- Lower volatility ≠ lower risk (can lose 100%+)
- Fundamentals trump statistics (check WHY spread is extreme)
- Seasonality matters (trade with patterns, not against)
- Proper ratios critical (3-2-1 crack, 1:11 crush)
- Correlation changes = risk explosion
- Stop losses mandatory (mean reversion not certain)

**Why this works:**

- Physical arbitrage (processors respond to margins)
- Substitution (buyers switch to cheaper commodity)
- Storage arbitrage (inventory builds/draws)
- Statistical mean reversion (100+ years data)
- **Multiple forces driving convergence**

**But remember:**

- Structural changes happen (energy transition, disease)
- Correlations break in crises
- Delivery mechanics can distort
- Fundamentals can shift permanently
- **Mean reversion is probable, not guaranteed**

**Trade spreads when statistics AND fundamentals align, exit when thesis breaks. The market rewards patience and punishes hubris. 📊⚖️**