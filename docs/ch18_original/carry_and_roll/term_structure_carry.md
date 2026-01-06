# Term Structure Carry

**Term structure carry** is a futures strategy that profits from the natural price decay or roll yield in futures markets by selling expensive near-term contracts and buying cheaper far-term contracts, exploiting predictable convergence patterns in contango or backwardation structures while remaining market-neutral.

---

## The Core Insight

**The fundamental idea:**

- Futures contracts of different expirations trade at different prices
- This creates a "term structure" (curve of prices across time)
- In contango: Near-term expensive, far-term cheap (upward sloping spot to futures)
- In backwardation: Near-term cheap, far-term expensive (downward sloping)
- Futures must converge to spot price at expiration
- This convergence creates predictable "decay" or "roll yield"
- You can profit from this decay without taking directional risk
- Collect carry while remaining market-neutral

**The key equation:**

$$
\text{Contango: } F_t^{T_1} > F_t^{T_2} \quad \text{where } T_1 < T_2
$$

$$
\text{Roll Yield} = \frac{F_{\text{near}} - F_{\text{far}}}{F_{\text{far}}} \times \frac{365}{T_{\text{near}} - T_{\text{far}}}
$$

$$
\text{Calendar Spread P\&L} = (F_{\text{front}} - F_{\text{back}})_{\text{entry}} - (F_{\text{front}} - F_{\text{back}})_{\text{exit}}
$$

**You're essentially betting: "The spread between near and far-term futures will narrow over time as near-term converges toward spot, and I can profit from this predictable convergence without taking a view on absolute price direction."**

---

## What Are Futures Term Structures?

**Before trading term structure carry, understand the mechanics:**

### Futures Term Structure Basics

**Definition:** The relationship between futures prices across different expiration dates for the same underlying commodity or financial instrument.

**Two fundamental shapes:**

**Contango (upward sloping):**

$$
\text{Spot} < F_1 < F_2 < F_3 < F_4
$$

- Near-term futures cheaper than far-term
- Normal for financial futures (cost of carry)
- Common in crude oil (storage costs)
- Negative roll yield for long positions

**Example (Crude Oil WTI):**

| Contract | Price | Days to Expiry |
|----------|-------|----------------|
| Spot | $75.00 | 0 |
| Feb | $76.50 | 30 |
| Mar | $77.80 | 60 |
| Apr | $78.90 | 90 |
| May | $79.80 | 120 |

**Backwardation (downward sloping):**

$$
\text{Spot} > F_1 > F_2 > F_3 > F_4
$$

- Near-term futures more expensive than far-term
- Indicates supply shortage or strong demand
- Positive roll yield for long positions
- Common in agricultural markets during harvest

**Example (Natural Gas):**

| Contract | Price | Days to Expiry |
|----------|-------|----------------|
| Spot | $4.50 | 0 |
| Feb | $4.30 | 30 |
| Mar | $4.10 | 60 |
| Apr | $3.95 | 90 |
| May | $3.85 | 120 |

### The Cost of Carry Model

**For financial futures:**

$$
F_t = S_t e^{(r-q)(T-t)}
$$

Where:
- $F_t$ = Futures price at time $t$
- $S_t$ = Spot price
- $r$ = Risk-free rate
- $q$ = Dividend yield (for equities) or convenience yield (for commodities)
- $T-t$ = Time to expiration

**For commodities:**

$$
F_t = S_t e^{(r+s-c)(T-t)}
$$

Where:
- $s$ = Storage costs
- $c$ = Convenience yield (benefit of physical ownership)

**Interpretation:**

**When $r + s > c$:** Contango (storage + financing costs dominate)

**When $r + s < c$:** Backwardation (convenience yield dominates)

### Calendar Spreads in Futures

**Definition:** The price difference between two futures contracts on the same underlying with different expiration dates.

**Long calendar spread (in contango):**

- Buy near-term contract (cheaper)
- Sell far-term contract (more expensive)
- Profit as spread narrows (convergence)
- Market-neutral position

**Example:**

- Buy Feb crude @ $76.50
- Sell Apr crude @ $78.90
- Spread: -$2.40 (long is cheaper)
- **Profit if spread narrows to -$1.80**

**Short calendar spread (in backwardation):**

- Sell near-term contract (expensive)
- Buy far-term contract (cheaper)
- Profit as spread narrows
- Market-neutral position

**Example:**

- Sell Feb nat gas @ $4.30
- Buy Apr nat gas @ $3.95
- Spread: +$0.35 (short is expensive)
- **Profit if spread narrows to +$0.20**

### Roll Yield Explained

**Roll yield:** The profit or loss from continuously rolling futures positions as contracts approach expiration.

**In contango (negative roll yield for longs):**

You own Feb futures @ $76.50:

- Feb expiring soon
- Must roll to Mar @ $77.80
- **Cost to roll: $1.30 (negative roll yield)**
- This is "contango bleed"

**In backwardation (positive roll yield for longs):**

You own Feb nat gas @ $4.30:

- Feb expiring soon
- Roll to Mar @ $4.10
- **Profit from roll: $0.20 (positive roll yield)**
- This is "backwardation boost"

**Calendar spread captures this roll yield:**

Instead of rolling at expiration, you trade the spread itself:

- Enter spread early
- Exit as convergence happens
- Capture roll yield without directional exposure
- **Pure term structure trade**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/term_structure_carry.png?raw=true" alt="term_structure_carry" width="700">
</p>
**Figure 1:** Term structure carry illustration showing contango (upward sloping curve from spot to far-dated futures) and backwardation (downward sloping). Calendar spreads profit from the predictable convergence as near-term futures approach expiration, capturing roll yield without directional market exposure.

---

## Economic Interpretation: Calendar Spreads as Structural Arbitrage

**Beyond the basic mechanics, understanding the economic rationale:**

### Calendar Spreads as Carry Arbitrage

**The deep insight:**

Calendar spreads in futures are **structural arbitrage** trades exploiting the mechanical convergence of futures to spot, not based on views of absolute price direction.

**Formal representation:**

$$
\text{Futures Price} = \text{Spot Price} + \text{Cost of Carry}
$$

$$
\text{As } T \to 0: \quad F_t \to S_t
$$

**This convergence is GUARANTEED by arbitrage:**

If $F_t > S_t$ at expiration:

- Buy spot, sell futures
- Deliver spot into futures
- Risk-free profit
- **Arbitrage eliminates gap**

**Calendar spread captures this convergence:**

$$
\text{Spread}(t) = F_1(t) - F_2(t)
$$

$$
\text{As } t \to T_1: \quad \text{Spread}(t) \to 0
$$

**You profit from the RATE of convergence, not the direction!**

### Why Term Structures Exist

**Economic forces creating term structure:**

**1. Storage costs (commodities):**

Physical commodities require storage:

$$
\text{Futures Premium} = \text{Storage Cost} \times \text{Time}
$$

**Example: Crude oil**

- Storage: $0.50/barrel/month
- 6-month futures premium: ~$3.00/barrel
- **Contango reflects storage economics**

**2. Financing costs (financial futures):**

Buying futures = delayed payment:

$$
\text{Futures Premium} = S \times r \times T
$$

**Example: S&P 500 futures**

- Spot: 4,500
- Interest rate: 5%
- 3-month futures: 4,500 × (1 + 0.05 × 0.25) = 4,556
- **Contango from financing**

**3. Convenience yield (commodities):**

Benefit of physical ownership:

- Can meet unexpected demand
- Avoid production disruptions
- Maintain operations
- **Creates backwardation when high**

**Example: Natural gas winter**

- High current demand (heating)
- Low storage
- Spot expensive relative to summer futures
- **Strong backwardation**

**4. Supply/demand dynamics:**

**Shortage now, expected surplus later:**

- Current tight supply
- New production coming online
- Spot high, futures lower
- **Backwardation**

**Surplus now, expected tightness later:**

- Current oversupply
- Future constraints expected
- Spot low, futures higher
- **Contango**

### The Convergence Trade Economics

**Why convergence is profitable:**

**Mathematical certainty:**

At expiration $T$:

$$
F_T = S_T \quad \text{(by arbitrage)}
$$

**Before expiration:**

$$
F_t = S_t + \text{Carry Cost}(T-t)
$$

**As time passes:**

$$
\frac{dF}{dt} = -\frac{d(\text{Carry Cost})}{dt} < 0 \quad \text{(in contango)}
$$

**Calendar spread captures this:**

$$
\frac{d(\text{Spread})}{dt} = \frac{dF_1}{dt} - \frac{dF_2}{dt}
$$

**Since near-term decays faster:**

$$
\left|\frac{dF_1}{dt}\right| > \left|\frac{dF_2}{dt}\right|
$$

**Spread narrows predictably!**

### Example: Contango Calendar Economics

**Setup:**

- Crude oil term structure
- Jan futures: $76.00 (30 days)
- Mar futures: $78.00 (90 days)
- Spot: $75.50
- Storage cost: $0.50/month

**Carry costs:**

$$
\text{Jan premium} = 30 \text{ days} \times \frac{\$0.50}{30} = \$0.50
$$

$$
\text{Mar premium} = 90 \text{ days} \times \frac{\$0.50}{30} = \$1.50
$$

**Expected convergence:**

In 30 days (Jan expiration):

- Jan → $S_{30}$ (spot in 30 days)
- Mar → $S_{30}$ + $0.50$ (now 60 days to expiry)
- Spread was: -$2.00 (Jan $76, Mar $78)
- Spread becomes: -$0.50
- **Spread narrows by $1.50**

**Calendar trade:**

- Buy Jan @ $76
- Sell Mar @ $78
- Entry spread: -$2.00

After 30 days:

- Close Jan @ $76.50 (spot + small premium)
- Close Mar @ $77.00 (spot + 2-month premium)
- Exit spread: -$0.50
- **Profit: $1.50 per contract**

**Return:**

Margin required: ~$4,000 per spread

$$
\text{Return} = \frac{\$1,500}{\$4,000} = 37.5\% \text{ in 30 days}
$$

**This is the power of calendar spreads—capturing guaranteed convergence!**

### Institutional Use of Calendar Spreads

**Why professionals trade calendars:**

**1. Hedgers managing roll costs:**

Oil company needs continuous long exposure:

- Own Mar futures
- Mar expiring
- Must roll to May

**Problem:**

- Contango: May futures @ $79, Mar @ $77
- Roll cost: $2 per barrel
- **Expensive to maintain hedge**

**Solution:**

- Month before roll: Short Mar/May calendar
- Profit from convergence
- Offsets roll cost
- **Reduces hedging expense**

**2. Market makers providing liquidity:**

- Quote spreads to clients
- Manage term structure risk
- Delta-hedge directional exposure
- **Earn bid-ask spread**

**3. Commodity Trading Advisors (CTAs):**

- Pure term structure strategies
- No directional bias
- Systematic programs
- **Harvest structural edge**

**4. Basis traders:**

- Exploit temporary dislocations
- Arbitrage spot vs futures
- Calendar spreads complement
- **Multi-strategy approach**

### The Roll Yield Harvesting Strategy

**Continuous calendar trading:**

Instead of one-off trades, systematic rolling:

**Month 1:**

- Long Feb/Apr crude calendar
- Collect convergence
- Close before Feb expiry

**Month 2:**

- Long Mar/May crude calendar
- Repeat process
- Continuous income

**Month 3:**

- Long Apr/Jun crude calendar
- Keep rolling forward

**Annual return from systematic rolling:**

Assume avg $1.00/barrel/month convergence:

$$
\text{Annual profit} = \$1.00 \times 12 = \$12/\text{barrel}
$$

On $4,000 margin:

$$
\text{Return} = \frac{\$12 \times 1,000}{$4,000} = 300\% \text{ annually}
$$

**Of course, this assumes:**

- Persistent contango (not always true)
- No adverse moves
- Perfect execution
- **Theoretical maximum**

**Realistic expectations: 20-50% annually with discipline**

---

## Key Terminology

**Term Structure:**

$$
\{F_t^{T_1}, F_t^{T_2}, ..., F_t^{T_n}\} \quad \text{where } T_1 < T_2 < ... < T_n
$$

- Relationship between futures prices and expiration dates
- Also called "forward curve"
- Shape indicates market expectations
- Key to calendar strategies

**Contango:**

$$
F_t^{T_1} < F_t^{T_2} \quad \text{for } T_1 < T_2
$$

- Near-term cheaper than far-term
- Upward sloping curve (spot to futures)
- Storage/carry costs dominate
- Negative roll yield for longs

**Backwardation:**

$$
F_t^{T_1} > F_t^{T_2} \quad \text{for } T_1 < T_2
$$

- Near-term more expensive than far-term
- Downward sloping curve
- Convenience yield or shortage
- Positive roll yield for longs

**Calendar Spread:**

$$
\text{Spread} = F_{\text{near}}^T - F_{\text{far}}^T
$$

- Difference between two futures expirations
- Long spread = buy near, sell far
- Short spread = sell near, buy far
- Market-neutral position

**Roll Yield:**

$$
\text{Roll Yield} = \frac{F_t^{T_1} - F_t^{T_2}}{F_t^{T_2}} \times \frac{365}{T_2 - T_1}
$$

- Profit/loss from rolling futures
- Negative in contango (for longs)
- Positive in backwardation (for longs)
- Annualized return component

**Cost of Carry:**

$$
\text{Carry} = \text{Storage} + \text{Financing} - \text{Convenience Yield} - \text{Dividends}
$$

- Economic reason for contango
- Storage costs (commodities)
- Interest costs (financial futures)
- Minus benefits of ownership

**Convenience Yield:**

$$
c = \text{Benefit of Physical Ownership}
$$

- Value of having commodity available
- Avoid stockouts
- Operational flexibility
- Creates backwardation when high

**Convergence:**

$$
\lim_{t \to T} F_t^T = S_T
$$

- Futures price approaches spot at expiration
- Guaranteed by arbitrage
- Source of calendar spread profit
- Mechanical, not speculative

**Basis:**

$$
\text{Basis} = \text{Spot Price} - \text{Futures Price}
$$

- For near-term contracts
- Negative in contango
- Positive in backwardation
- Narrows to zero at expiration

**Carry Trade:**

- Profiting from term structure
- Calendar spreads = pure carry
- No directional exposure
- Structural edge

**Front Month:**

- Nearest expiration futures contract
- Most liquid
- About to converge to spot
- Higher gamma, lower theta (options analogy)

**Back Month:**

- Further expiration contract
- Less liquid (usually)
- More time to expiration
- Lower gamma, higher theta (options analogy)

**Roll Date:**

- When front month expires
- Must close/roll positions
- Predictable (third Friday typically)
- Key risk management point

---

## The Greeks (Calendar Spread Dynamics)

**While futures don't have traditional Greeks like options, we can define analogous sensitivities:**

### Delta (Directional Sensitivity)

**Definition:** How spread value changes with absolute price movement.

**For a perfectly market-neutral calendar:**

$$
\Delta_{\text{calendar}} = \Delta_{\text{long front}} + \Delta_{\text{short back}} = +1 - 1 = 0
$$

**In theory, delta-neutral.**

**In practice:**

$$
\Delta_{\text{calendar}} \approx 0.05 \text{ to } 0.10
$$

**Why not exactly zero:**

**Different durations:**

- Front month closer to expiry
- More sensitive to spot moves
- Beta to spot slightly different
- **Small residual delta**

**Example:**

Spot moves $1.00:

- Front month: +$1.05 (slight premium)
- Back month: +$1.00 (tracks spot)
- **Net: +$0.05 per spread**

**This is negligible compared to spread movement from convergence.**

**Managing delta:**

- Rebalance if spot moves >10%
- Adjust number of contracts
- Or accept small delta (part of strategy)
- **Usually ignore for pure carry trades**

### Gamma (Convexity in Spread)

**Definition:** How delta changes as price moves (second-order effect).

$$
\Gamma_{\text{calendar}} \approx 0
$$

**Futures are linear instruments:**

- Delta always 1.0
- No gamma in individual futures
- **Calendar spread also no gamma**

**Contrast with options calendars:**

- Options have gamma
- Calendars have negative gamma
- Price moves hurt

**Futures calendars:**

- No gamma risk
- Only theta and basis risk
- **Simpler risk profile**

### Theta (Time Decay / Convergence)

**Definition:** Daily profit from spread narrowing due to time passage.

$$
\Theta_{\text{calendar}} = \frac{d(\text{Spread})}{dt}
$$

**In contango:**

$$
\Theta > 0 \quad \text{(spread narrows, profitable)}
$$

**Example:**

- Entry spread: -$2.00
- Expected spread in 30 days: -$0.50
- Daily theta: $1.50 / 30 = **$0.05/day**

**On 10 contracts:**

$$
\text{Daily profit} = \$0.05 \times 1,000 \times 10 = \$500/\text{day}
$$

**In backwardation:**

$$
\Theta > 0 \quad \text{(spread narrows, profitable for short calendars)}
$$

**Theta is the PRIMARY driver of calendar P&L.**

**Acceleration near expiration:**

As front month approaches expiry:

- Convergence accelerates
- Theta increases
- Last 2 weeks = fastest decay
- **Profit concentrated late**

### Vega (Volatility Sensitivity)

**Futures don't have vega (no volatility component in pricing).**

**But calendar spreads affected by volatility indirectly:**

**High volatility → wider spreads:**

- Uncertainty about future spot
- Risk premium in far months
- Spreads widen
- **Short calendars benefit**

**Low volatility → tighter spreads:**

- Predictable convergence
- Less risk premium
- Spreads narrow
- **Long calendars benefit**

**Example:**

Calm market:

- Spread: -$1.50 (tight)
- Convergence smooth
- **Good for long calendar**

Volatile market:

- Spread: -$2.50 (wide)
- Fear of large moves
- **Good for short calendar**

**Vega effect is INDIRECT and smaller than theta.**

### Rho (Interest Rate Sensitivity)

**Definition:** How spread value changes with interest rate changes.

**For financial futures:**

$$
\rho_{\text{calendar}} = \frac{\partial (\text{Spread})}{\partial r}
$$

**Higher rates → steeper contango:**

$$
F = S e^{r(T-t)}
$$

Higher $r$ → larger premium on far months → wider spread

**Example:**

S&P 500 futures:

- Rates: 3% → Spread: -20 points
- Rates: 5% → Spread: -33 points
- **Spread widened by 13 points**

**For commodity futures:**

Interest rate effect mixed with storage costs:

- Higher rates → higher carry cost
- But convenience yield unchanged
- Net effect depends on ratio

**Generally:**

- Rising rates → contango steepens
- Falling rates → contango flattens
- **Rho exists but manageable**

**Management:**

- Monitor Fed policy
- Adjust positions before rate changes
- Or accept rho risk (small compared to theta)
- **Secondary consideration**

---

## Contract Selection: Which Spreads to Trade

**Just as stock traders select securities, calendar traders select optimal spreads:**

### Crude Oil (CL) - The Gold Standard

**Characteristics:**

- Ticker: /CL
- Contract size: 1,000 barrels
- Tick size: $0.01 ($10 per contract)
- Margin: ~$4,000 per spread
- Liquidity: Excellent (100k+ contracts/day)

**Typical term structure:**

- Strong contango (storage costs)
- $1-3/barrel between months
- Persistent pattern
- **Ideal for calendars**

**Example:**

- Feb $76.50, Apr $78.50
- Spread: -$2.00
- Expected convergence: 30-60% in 1 month
- **Target: -$1.20, profit $0.80**

**Pros:**

- Most liquid commodity
- Predictable term structure
- Well-studied patterns
- Tight spreads (easy execution)
- **Best starter spread**

**Cons:**

- Geopolitical risk (supply shocks)
- OPEC decisions impact structure
- Can flip to backwardation quickly
- **Needs monitoring**

### Natural Gas (NG) - The Seasonal Specialist

**Characteristics:**

- Ticker: /NG
- Contract size: 10,000 MMBtu
- Tick size: $0.001 ($10 per contract)
- Margin: ~$3,500 per spread
- Liquidity: Good

**Typical term structure:**

- Strong seasonality
- Winter (backwardation): near expensive
- Summer (contango): near cheap
- **Trade the seasons**

**Example (Winter):**

- Jan $4.50 (heating demand)
- Apr $3.80 (shoulder season)
- Spread: +$0.70 (backwardation)
- **Short calendar profits from narrowing**

**Example (Summer):**

- Jul $3.20 (low demand)
- Oct $3.90 (pre-winter)
- Spread: -$0.70 (contango)
- **Long calendar profits from narrowing**

**Pros:**

- Extreme term structure moves
- Seasonal predictability
- Large profit potential
- **Great for experienced traders**

**Cons:**

- Very volatile
- Weather-dependent
- Can gap on forecasts
- Requires expertise
- **Not for beginners**

### S&P 500 E-mini (ES) - The Financial Standard

**Characteristics:**

- Ticker: /ES
- Contract size: $50 × index
- Tick size: 0.25 points ($12.50)
- Margin: ~$2,000 per spread
- Liquidity: Massive (1M+ contracts/day)

**Typical term structure:**

- Mild contango (financing costs)
- 3-8 points per quarter
- Very predictable
- Interest rate driven
- **Stable carry**

**Example:**

- Mar 4,500, Jun 4,508
- Spread: -8 points
- Expected convergence: 50% in 2 months
- **Target: -4 points, profit 4 points = $200**

**Pros:**

- Extremely liquid
- Low margin
- Predictable (no commodity risk)
- Cash-settled (no delivery)
- **Safest calendar spread**

**Cons:**

- Small spreads (lower profit potential)
- Needs size for meaningful profit
- Competition (efficient pricing)
- **Lower returns than commodities**

### Gold (GC) - The Contango Stable

**Characteristics:**

- Ticker: /GC
- Contract size: 100 troy ounces
- Tick size: $0.10 ($10 per contract)
- Margin: ~$5,000 per spread
- Liquidity: Good

**Typical term structure:**

- Persistent contango (storage + financing)
- $5-15/oz per year
- Very stable
- No convenience yield (gold doesn't spoil)
- **Textbook carry**

**Example:**

- Feb $2,050, Aug $2,065
- Spread: -$15 (6 months)
- Monthly convergence: ~$2.50
- **Profit $15 over 6 months**

**Pros:**

- Very stable term structure
- Predictable carry
- Low volatility
- Good for conservative traders
- **Steady income**

**Cons:**

- Lower profit potential
- Slow convergence
- Ties up capital longer
- **Boring but safe**

### Agricultural Futures (Corn, Soybeans, Wheat)

**Characteristics:**

- Contract sizes: 5,000 bushels
- Seasonal patterns (planting/harvest)
- Weather dependent
- USDA reports impact

**Typical term structure:**

**Pre-harvest (Spring):**

- Backwardation (tight supply)
- Near-term expensive
- **Short calendars**

**Post-harvest (Fall):**

- Contango (abundant supply)
- Storage costs dominate
- **Long calendars**

**Example (Corn):**

**May (pre-harvest):**

- May $6.00, Jul $5.75
- Spread: +$0.25 (backwardation)
- Short calendar

**November (post-harvest):**

- Nov $5.50, Jan $5.70
- Spread: -$0.20 (contango)
- Long calendar

**Pros:**

- Strong seasonal patterns
- Predictable cycles
- USDA data provides clarity
- **Good for systematic strategies**

**Cons:**

- Weather risk (droughts, floods)
- USDA reports = volatility spikes
- Less liquid than energy
- **Requires ag knowledge**

### Comparison Table

| Futures | Typical Spread | Margin/Spread | Liquidity | Volatility | Difficulty | Best For |
|---------|---------------|---------------|-----------|------------|------------|----------|
| Crude Oil (CL) | $1-3/barrel | $4,000 | Excellent | High | Medium | Most traders |
| Nat Gas (NG) | $0.30-1.00 | $3,500 | Good | Very High | High | Experienced |
| S&P 500 (ES) | 3-8 points | $2,000 | Excellent | Low | Low | Beginners |
| Gold (GC) | $5-15/oz | $5,000 | Good | Low | Low | Conservative |
| Corn (ZC) | $0.10-0.30 | $2,500 | Moderate | Medium | Medium | Seasonal |

**Beginner recommendation: Start with ES (S&P 500) or CL (Crude Oil) calendars.**

---

## Time Selection: When to Enter and Exit

**Just as options traders select expiration dates, calendar traders must time their entries:**

### Optimal Entry Timing

**Best time to enter calendar spreads:**

**1. When term structure is wide (steep contango/backwardation):**

$$
\text{Wide spread} = \text{More convergence potential}
$$

**Example:**

Crude oil spread normally -$1.50:

- Current: -$2.50 (unusually wide)
- **Enter long calendar**
- Target: -$1.50 (normal)
- Profit: $1.00/barrel

**Why wide:**

- Temporary dislocation
- Supply/demand shock
- Market overreaction
- **Opportunity**

**2. After roll period (3-5 days after expiration):**

$$
\text{Post-roll} = \text{Spreads reset, less crowded}
$$

During roll week:

- Everyone rolling at once
- Spreads compressed
- Poor entry point
- **Wait**

After roll:

- Spreads normalize
- Less volume pressure
- Better pricing
- **Good entry**

**3. Before seasonal patterns (for commodities):**

**Natural gas example:**

- August: Enter long Nov/Mar calendar
- Anticipate winter backwardation
- **Position early for seasonal move**

**Crude oil example:**

- December: Enter long Feb/May calendar
- Anticipate refinery maintenance (spring)
- **Seasonal widening**

**4. When front month has 30-60 days to expiry:**

$$
\text{Front month DTE} = 30\text{-}60 \text{ days (optimal)}
$$

**Too close (<21 days):**

- Fast convergence but
- Execution risk
- Rollover complications
- **Rushed**

**Too far (>90 days):**

- Slow convergence
- Capital tied up longer
- Opportunity cost
- **Inefficient**

**Sweet spot: 30-60 days**

- Predictable convergence
- Good liquidity
- Time to manage
- **Best risk/reward**

### When NOT to Enter

**Avoid entering calendar spreads when:**

**1. Just before major reports:**

- OPEC meetings (oil)
- EIA inventory (oil/gas)
- USDA crop reports (ag)
- Fed meetings (financial futures)
- **Uncertainty spikes**

**Why:**

- Spreads can gap
- Unpredictable moves
- Term structure shifts violently
- **Wait for clarity**

**2. During roll week (last week before expiration):**

**Example:**

Front month expires Friday:

- Monday-Friday: Roll week
- Massive volume in calendar spreads
- Everyone trying to roll
- **Spreads compressed, poor pricing**

**Wait until following week:**

- Spreads normalize
- Better execution
- Less competition
- **Patience pays**

**3. When term structure is inverted abnormally:**

**Crude example:**

- Normal backwardation: Feb $76, Apr $74 ($2)
- Extreme: Feb $80, Apr $70 ($10!)
- **This is NOT normal carry**

**Likely causes:**

- War/embargo
- Natural disaster
- Refinery shutdown
- **Fundamental disruption**

**Don't trade:**

- Not term structure, it's crisis
- Calendar spread won't behave normally
- **Skip this market**

**4. Low liquidity periods:**

- Between Christmas and New Year
- Asian holidays (for Asian commodities)
- Thin summer trading
- **Wide spreads, poor execution**

### Exit Strategy

**Three exit approaches:**

**Approach 1: Hold to front expiration (maximum convergence)**

**Process:**

- Enter when front = 45 days
- Hold through convergence
- Close 3-5 days before expiration
- **Capture full theta**

**Example:**

- Entry: -$2.00 spread
- Day 40: -$0.60 spread
- Profit: $1.40
- **Close and repeat**

**Pros:**

- Maximum profit potential
- Full convergence captured
- **Best if spread behaves**

**Cons:**

- Must monitor daily
- Rollover risk
- Tied up longer
- **Requires attention**

**Approach 2: Take profit at 50-75% of expected convergence**

$$
\text{If profit} = 60\% \text{ of max} \Rightarrow \text{Close}
$$

**Example:**

- Entry: -$2.00
- Expected final: -$0.50 (convergence $1.50)
- 60% target: $0.90 profit
- Exit at: -$1.10 spread
- **Close early, lock profit**

**Pros:**

- Locks profit early
- Reduces risk
- Can redeploy capital
- **Professional approach**

**Cons:**

- Leaves money on table
- May regret if full convergence happens
- **Opportunity cost**

**Approach 3: Roll to new calendar (continuous strategy)**

**Process:**

- Front month expires
- Back month becomes new front
- Sell new back month
- **Maintain position**

**Example:**

Cycle 1:

- Long Feb/Apr crude
- Cost: -$2.00
- Feb expires: -$0.40
- Profit: $1.60

Cycle 2 (roll):

- Apr now front (40 days)
- Sell new Jun back
- New spread: -$1.80
- **Restart cycle**

**Continuous rolling generates:**

$$
\text{Annual return} = 12 \times 40\% = 480\% \quad \text{(theoretical)}
$$

**Realistic: 30-60% annually with discipline**

### Management During Trade

**Daily monitoring checklist:**

**1. Spread width:**

- Track daily spread value
- Compare to entry
- Calculate unrealized P&L
- **Know your position**

**2. Term structure shape:**

- Has contango steepened or flattened?
- Any inversion appearing?
- **Structure changes matter**

**3. Front month days to expiry:**

- <10 days: High risk period
- <5 days: Plan rollover
- **Calendar management**

**4. Absolute price moves:**

- Large spot moves affect spreads
- >10% move: Reassess position
- **Directional impact**

**5. News/events upcoming:**

- Check economic calendar
- OPEC, EIA, USDA dates
- **Avoid surprises**

**Adjustment triggers:**

**Spread widening (opposite of expected):**

- Entry: -$2.00
- Now: -$2.50 (widened)
- **Consider closing if >20% adverse move**

**Front month <7 days:**

- Roll risk increasing
- Liquidity may decline
- **Close or roll proactively**

**Fundamental change:**

- War breaks out (oil)
- Polar vortex (nat gas)
- Drought (ag)
- **Exit if structure broken**

---

## Maximum Profit and Loss

### Calendar Spread Outcomes

**Setup:**

- Crude oil calendar
- Buy Feb futures @ $76.50 (30 DTE)
- Sell Apr futures @ $78.50 (90 DTE)
- Entry spread: -$2.00
- Position: 10 contracts
- Margin: $4,000 per spread = $40,000 total

**Maximum Profit:**

Occurs when spread narrows completely:

- Feb expires at spot: $76.00
- Apr at expiry pricing: $76.60 (spot + 60-day carry)
- Exit spread: -$0.60
- **Convergence: $1.40**

$$
\text{Profit per contract} = (\$2.00 - \$0.60) \times 1,000 = \$1,400
$$

$$
\text{Total profit} = \$1,400 \times 10 = \$14,000
$$

$$
\text{Return on margin} = \frac{\$14,000}{\$40,000} = 35\%
$$

**In 30 days → Annualized: 420%**

**Maximum Loss:**

Occurs if spread widens instead of narrows:

- Geopolitical crisis
- Feb spikes to $82 (backwardation)
- Apr at $80 (less responsive)
- Exit spread: +$2.00 (reversed!)
- **Spread moved $4.00 against us**

$$
\text{Loss per contract} = (-\$2.00 - (+\$2.00)) \times 1,000 = -\$4,000
$$

$$
\text{Total loss} = -\$4,000 \times 10 = -\$40,000
$$

$$
\text{Loss on margin} = \frac{-\$40,000}{\$40,000} = -100\%
$$

**Complete wipeout (rare but possible!)**

**Breakeven:**

$$
\text{Spread stays at} -\$2.00
$$

No convergence, no divergence → No profit, no loss

### Realistic Scenarios

**Scenario 1: Normal Convergence (70% of trades)**

**Day 0 (Entry):**

- Spread: -$2.00
- Spot: $75.50

**Day 15:**

- Spread: -$1.50 (minor convergence)
- Spot: $76.00
- **Progress: $0.50 profit**

**Day 30 (Front expiration):**

- Spread: -$0.70 (strong convergence)
- Spot: $76.20
- **Final profit: $1.30**

$$
\text{Profit} = \$1.30 \times 1,000 \times 10 = \$13,000 \text{ (32.5\% return)}
$$

**Scenario 2: Slow Convergence (20% of trades)**

**Day 30:**

- Spread: -$1.50 (minimal convergence)
- Spot stable around $75-76
- **Profit: $0.50**

$$
\text{Profit} = \$0.50 \times 1,000 \times 10 = \$5,000 \text{ (12.5\% return)}
$$

**Decision:**

- Low return but still positive
- Close and redeploy elsewhere
- **Small win acceptable**

**Scenario 3: Spread Widening - Loss (10% of trades)**

**Day 15:**

- OPEC cuts production
- Supply concerns
- Front month spikes more than back
- Spread: -$2.80 (widened $0.80)

**Day 20:**

- Decide to cut loss
- Exit at -$2.90
- **Loss: -$0.90**

$$
\text{Loss} = -\$0.90 \times 1,000 \times 10 = -\$9,000 \text{ (-22.5\% return)}
$$

**This is why stops are critical!**

### Position Sizing Impact

**Conservative (3 contracts):**

- Margin: $12,000
- Normal profit: $3,900 (32.5%)
- Max loss scenario: -$12,000 (100%)
- **Lower risk, lower absolute return**

**Moderate (10 contracts):**

- Margin: $40,000
- Normal profit: $13,000 (32.5%)
- Max loss scenario: -$40,000 (100%)
- **Balanced approach**

**Aggressive (30 contracts):**

- Margin: $120,000
- Normal profit: $39,000 (32.5%)
- Max loss scenario: -$120,000 (100%)
- **High risk, high absolute return**

**Professional sizing:**

$$
\text{Contracts} = \frac{\text{Account Risk (2-5\%)}}{\text{Expected Spread Movement}}
$$

For $500,000 account, risking 3%:

$$
\text{Contracts} = \frac{\$15,000}{\$2,000 \text{ (expected max adverse)}} = 7.5 \approx 7
$$

---

## When to Use Term Structure Carry

### Ideal Market Conditions

**Use calendar spreads when:**

**1. Persistent term structure exists:**

$$
\text{Contango or backwardation stable for } > 6 \text{ months}
$$

**Example:**

Crude oil in steady contango:

- 2023: -$2.00 avg spread
- 2024: -$2.20 avg spread
- Pattern established
- **Reliable carry opportunity**

**2. No major disruptions expected:**

- Geopolitical stability
- No OPEC decisions imminent
- Normal supply/demand
- **Predictable environment**

**3. Term structure steeper than historical average:**

$$
\text{Current spread} > 1.2 \times \text{Average spread}
$$

**Example:**

- Historical avg crude spread: -$1.50
- Current: -$2.30 (53% wider)
- **Opportunity for reversion + convergence**

**4. Clear seasonality approaching (commodities):**

**Natural gas in summer:**

- Entering contango season
- Winter months show backwardation
- **Trade the seasonal pattern**

**Agricultural examples:**

- Corn pre-harvest: backwardation
- Post-harvest: contango
- **Predictable cycles**

**5. You can monitor daily:**

- Futures move 24/5
- Need to watch positions
- Can't set and forget
- **Active management required**

### Best Markets for Calendar Spreads

**Energy (Crude Oil, Natural Gas):**

**Why best:**

- Deepest liquidity
- Clearest term structures
- Storage costs create contango
- **Most reliable patterns**

**Stats:**

- Crude contango 75% of time
- Nat gas seasonal 90% predictable
- **High probability setups**

**Financial Futures (ES, NQ, Bonds):**

**Why good:**

- Very liquid
- Low margin
- Predictable (interest rate driven)
- **Safe starter markets**

**Stats:**

- Contango 95% of time (stock indices)
- Small but consistent spreads
- **Lower returns but safer**

**Metals (Gold, Silver, Copper):**

**Why moderate:**

- Stable contango (storage costs)
- Lower volatility
- Good for conservative traders
- **Steady but slow**

**Agricultural (Corn, Wheat, Soybeans):**

**Why challenging:**

- Weather dependent
- Seasonal extremes
- USDA reports volatile
- **Requires expertise**

**But profitable if you understand the cycles.**

### Specific Use Cases

**Use Case 1: Hedging roll costs**

You're a hedger needing continuous long crude exposure:

**Problem:**

- Must roll monthly: Mar → Apr → May
- Contango costs $1.50-2.00 per roll
- Annual cost: $18-24/barrel

**Solution:**

- Short calendar spreads to offset
- Mar/May spread @ -$3.00
- Profit $1.50 as converges
- **Reduces hedging cost by 60-75%**

**Use Case 2: Yield enhancement on cash**

You have $500k sitting in cash:

**Traditional:**

- Money market: 5% = $25k/year

**Alternative:**

- Deploy 20% to calendars ($100k margin)
- Conservative 30% annual return
- Earn: $30k on $100k
- Plus $20k on remaining $400k @ 5%
- **Total: $50k (10% on full $500k)**

**Use Case 3: Market-neutral strategy**

You want exposure to futures markets without directional risk:

**Calendar spreads provide:**

- Pure term structure alpha
- No correlation to equity markets
- Consistent returns
- **Portfolio diversification**

**Combine with:**

- 60% stocks
- 30% bonds
- 10% calendar spreads
- **Smooth overall returns**

---

## When NOT to Use Term Structure Carry

### Avoid These Situations

**1. Inverted or flat term structures:**

$$
\text{Spread} \approx 0 \text{ or reversed}
$$

**Example:**

Crude oil spread: -$0.20 (nearly flat)

- No convergence potential
- No carry to harvest
- **Skip this market**

**Wait for spread to widen to -$1.50+ before entering**

**2. High geopolitical risk:**

**Crude oil during:**

- Middle East conflicts
- OPEC surprise cuts
- Pipeline attacks
- Russian sanctions

**Why skip:**

- Term structures can flip overnight
- Backwardation appears suddenly
- Spreads gap violently
- **Unpredictable**

**3. Just before major reports:**

**Energy:**

- EIA inventory (Wednesdays)
- OPEC meetings
- **Weekly volatility**

**Agricultural:**

- USDA crop reports
- Planting/harvest updates
- **Monthly bombs**

**Wait 24-48 hours after reports for structure to settle**

**4. Extreme weather events:**

**Natural gas:**

- Polar vortex approaching
- Hurricane in Gulf
- **Parabolic moves**

**Agricultural:**

- Drought conditions
- Flooding
- **Supply shocks**

**These break normal term structure patterns!**

**5. Market in backwardation when expecting contango:**

**Example:**

You want to trade crude calendars (expecting contango):

- Current: Backwardation (front $78, back $75)
- This is OPPOSITE of normal
- **Don't fight it**

**Either:**

- Trade the backwardation (short calendars)
- Or skip entirely
- **Don't force your thesis**

**6. You can't monitor regularly:**

**Calendar spreads require:**

- Daily P&L checks
- Spread movement monitoring
- News awareness
- **Active management**

**If you're:**

- On vacation
- Too busy with day job
- Can't check positions daily
- **Don't trade calendars**

**7. Insufficient capital:**

$$
\text{Account} < \$50,000 \Rightarrow \text{Too small for futures calendars}
$$

**Why:**

- Minimum 1 spread = $4,000 margin
- Need 10-20 contracts for diversification
- Position sizing requires size
- **Under-capitalized = high risk**

**Consider:**

- Mini futures calendars (smaller size)
- Options calendars instead
- Build account first
- **Size matters**

---

## Position Sizing and Risk Management

### The Golden Rule: Margin is Not Risk

**Critical misunderstanding:**

$$
\text{Margin required} \neq \text{Amount at risk}
$$

**Example:**

- Margin per spread: $4,000
- Think: "I'm only risking $4,000"
- **WRONG!**

**Actual risk:**

- Spread can move $3-5 against you
- Loss: $3,000-5,000 per contract
- **Can lose more than margin!**

**Proper risk calculation:**

$$
\text{Risk per spread} = \text{Expected Maximum Adverse Move} \times \text{Contract Size}
$$

**Crude oil calendar:**

$$
\text{Risk} = \$3.00 \text{ (max adverse)} \times 1,000 = \$3,000 \text{ per spread}
$$

**Position sizing:**

$$
\text{Contracts} = \frac{\text{Account Risk Tolerance}}{\text{Risk per Spread}}
$$

**For $200,000 account, 5% risk ($10,000):**

$$
\text{Contracts} = \frac{\$10,000}{\$3,000} = 3.3 \approx 3
$$

### Portfolio Allocation

**Conservative approach:**

- 30% of account in margin for calendars
- $200k account → $60k margin
- $60k / $4k per spread = 15 spreads max
- **But risk-adjust to 5-8 spreads across markets**

**Moderate approach:**

- 50% of account available for calendars
- $200k → $100k margin
- **10-15 spreads actively traded**

**Aggressive (professionals):**

- 80% of account in calendars
- $200k → $160k margin
- **20-30 spreads, heavy leverage**

**Beginner recommendation:**

$$
\text{Start with: } 2\text{-}3 \text{ spreads only}
$$

**Learn the mechanics before scaling up!**

### Diversification Across Markets

**Don't concentrate in one commodity:**

**Bad:** 10 crude oil calendars

**Good:** 

- 3 crude oil calendars
- 2 natural gas calendars
- 3 S&P 500 calendars
- 2 gold calendars

**Why diversify:**

- Crude shock doesn't kill entire portfolio
- Different term structure drivers
- Uncorrelated returns
- **Risk reduction**

**Correlation matrix (approximate):**

|  | Crude | Nat Gas | S&P | Gold |
|--|-------|---------|-----|------|
| Crude | 1.00 | 0.30 | 0.20 | 0.10 |
| Nat Gas | 0.30 | 1.00 | 0.15 | -0.05 |
| S&P | 0.20 | 0.15 | 1.00 | -0.10 |
| Gold | 0.10 | -0.05 | -0.10 | 1.00 |

**Low correlations = good diversification!**

### Stop Loss Strategy

**Calendar spreads need stops despite being "carry trades":**

**Method 1: Spread-based stop**

$$
\text{Exit if spread widens } > 40\% \text{ from entry}
$$

**Example:**

- Entry: -$2.00
- Stop: -$2.80 (40% wider)
- Loss per contract: $800
- **Hard exit rule**

**Method 2: Time-based stop**

$$
\text{Exit if no convergence by Day 20}
$$

**Rationale:**

- Expected convergence in 30 days
- By day 20, should see progress
- If not, something wrong
- **Cut it loose**

**Method 3: Absolute dollar stop**

$$
\text{Exit if down } \$X \text{ per spread}
$$

**Example:**

- Maximum loss tolerance: $1,500 per spread
- Spread moves $1.50 against us
- **Exit immediately**

**Professional approach: Combine all three**

Exit if ANY trigger hits:

- Spread >40% wider
- Day 20 with no progress
- Down $1,500 per spread

**First one to hit = exit signal**

### Profit Targets

**Realistic expectations:**

$$
\text{Target} = 50\text{-}70\% \text{ of expected convergence}
$$

**Example:**

- Entry spread: -$2.00
- Expected final: -$0.50
- Full convergence: $1.50
- **Target: 60% = $0.90 profit**
- **Exit at -$1.10 spread**

**Why not hold for full convergence:**

- Last 20% takes longest
- Risk increases near expiration
- Can redeploy capital
- **Professional profit taking**

### Leverage Management

**Futures are inherently leveraged:**

$$
\text{Leverage} = \frac{\text{Notional Value}}{\text{Margin Required}}
$$

**Crude oil example:**

- Price: $76/barrel
- Contract: 1,000 barrels = $76,000 notional
- Margin: $4,000
- **Leverage: 19:1**

**This is DANGEROUS if not managed!**

**Safe leverage guidelines:**

$$
\text{Total Notional} < 3\times \text{Account Size}
$$

**For $200k account:**

$$
\text{Max notional} = \$600,000
$$

$$
\text{Crude contracts} = \frac{\$600,000}{\$76,000} = 7.9 \approx 8 \text{ spreads}
$$

**This limits maximum drawdown to manageable levels**

### Example: Complete Risk Management

**Account: $200,000**

**Allocation:**

- Available for calendars: $80,000 (40%)
- Reserved for margin calls: $20,000
- Active trading: $60,000

**Positions:**

**Position 1: Crude Oil**

- 3 Feb/Apr calendars
- Entry: -$2.00
- Margin: $12,000
- Risk per spread: $3,000
- Total risk: $9,000 (4.5% of account)
- Stop: -$2.80

**Position 2: S&P 500**

- 5 Mar/Jun calendars
- Entry: -8 points
- Margin: $10,000
- Risk per spread: $400 ($200/point × 2)
- Total risk: $2,000 (1% of account)
- Stop: -12 points

**Position 3: Gold**

- 2 Apr/Aug calendars
- Entry: -$15
- Margin: $10,000
- Risk per spread: $1,500
- Total risk: $3,000 (1.5% of account)
- Stop: -$25

**Total deployed:**

- Margin: $32,000
- Risk: $14,000 (7% of account)
- **Within limits**

**Maximum loss scenario (all stops hit):**

$$
\text{Max drawdown} = \$14,000 = 7\% \text{ of account}
$$

**Acceptable for this strategy!**

**Expected profit (60% of convergence):**

- Crude: 3 × $900 = $2,700
- S&P: 5 × $200 = $1,000
- Gold: 2 × $600 = $1,200
- **Total: $4,900 (2.45% return in 30 days)**

**Risk/reward: 1:0.35 per trade, but 70% win rate makes it positive expectancy**

---

## Examples: Term Structure Carry Trades in Action

### Example 1: Classic Crude Oil Contango Harvest

**Background:**

- Date: January 5, 2025
- Market: Crude oil in normal contango
- Reason: Adequate supply, storage available
- Geopolitical: Stable

**Term structure:**

| Contract | Price | Days to Expiry | Carry |
|----------|-------|----------------|-------|
| Spot | $75.00 | 0 | - |
| Feb | $76.50 | 30 | $1.50 |
| Mar | $77.40 | 60 | $2.40 |
| Apr | $78.20 | 90 | $3.20 |

**Trade setup:**

- Entry: Buy Feb @ $76.50, Sell Apr @ $78.20
- Spread: -$1.70
- Expected convergence: 60% = $1.02
- Target spread: -$0.68
- Position: 10 contracts
- Margin: $40,000

**Entry Greeks:**

- Delta: ~0 (market-neutral)
- Theta: +$50/day (10 contracts × $0.05/day/contract)
- Expected return: 25% in 30 days

**Trade progression:**

**Week 1 (January 12):**

- Feb: $76.30 (slight drop)
- Apr: $77.80 (dropped more)
- Spread: -$1.50 (narrowed $0.20)
- P&L: $0.20 × 1,000 × 10 = **+$2,000**
- On track

**Week 2 (January 19):**

- Feb: $76.80 (recovering)
- Apr: $78.00
- Spread: -$1.20 (narrowed $0.50 total)
- P&L: **+$5,000**
- Ahead of schedule!

**Week 3 (January 26):**

- Feb: $77.00
- Apr: $77.90
- Spread: -$0.90 (narrowed $0.80)
- P&L: **+$8,000**
- Near target

**Week 4 (February 2):**

- Feb: $77.20 (7 DTE, close to spot)
- Apr: $77.80
- Spread: -$0.60 (exceeded target!)
- P&L: **+$11,000**

**Decision: Close early (day 28)**

**Rationale:**

- Target exceeded
- Feb approaching expiration (risk)
- Profit secured
- **Take the win**

**Final exit:**

- Close spread @ -$0.60
- Total profit: $1.70 - $0.60 = $1.10
- Profit: $1.10 × 1,000 × 10 = **$11,000**
- Return: $11,000 / $40,000 = **27.5% in 28 days**
- Annualized: **359%**

**Why it worked:**

1. ✅ Normal contango structure
2. ✅ No disruptions
3. ✅ Predictable convergence
4. ✅ Closed before final week risk
5. ✅ Disciplined profit taking
6. **Textbook execution**

### Example 2: Natural Gas Seasonal Backwardation

**Background:**

- Date: November 1, 2024
- Market: Natural gas entering winter
- Weather: Cold forecasts
- Storage: Below 5-year average

**Term structure (backwardation):**

| Contract | Price | Days to Expiry |
|----------|-------|----------------|
| Spot | $4.20 | 0 |
| Dec | $4.50 | 30 |
| Jan | $4.30 | 60 |
| Feb | $3.95 | 90 |

**Trade setup (SHORT calendar):**

- Entry: Sell Dec @ $4.50, Buy Feb @ $3.95
- Spread: +$0.55 (backwardation)
- Expected convergence: $0.35
- Target spread: +$0.20
- Position: 5 contracts
- Margin: $17,500

**This is opposite of crude example—we're SHORT the spread!**

**Trade progression:**

**Week 1:**

- Dec: $4.60 (winter premium growing)
- Feb: $4.00
- Spread: +$0.60 (widened!)
- P&L: -$0.05 × 10,000 × 5 = **-$2,500**
- **Against us initially**

**Week 2:**

- Dec: $4.80 (spike on cold snap)
- Feb: $4.10 (less responsive)
- Spread: +$0.70 (widening more)
- P&L: **-$7,500**
- **Getting nervous**

**Week 3:**

- Dec: $4.70 (forecast moderating)
- Feb: $4.15
- Spread: +$0.55 (back to entry)
- P&L: **$0**
- **Breakeven**

**Week 4 (approaching Dec expiration):**

- Dec: $4.30 (converging to spot)
- Feb: $4.10
- Spread: +$0.20 (target hit!)
- P&L: +$0.35 × 10,000 × 5 = **+$17,500**

**Exit:**

- Close @ +$0.20 spread
- Profit: $17,500
- Return: 100% in 28 days!
- **Annualized: 1,300%**

**Lessons learned:**

1. Backwardation spreads volatile
2. Initial adverse move common (winter premium)
3. Convergence happens rapidly near expiration
4. **Patience rewarded**
5. Higher risk than contango but higher return

### Example 3: S&P 500 Steady Grind (Conservative)

**Background:**

- Date: March 1, 2025
- Market: Equity indices in mild contango
- VIX: 14 (low)
- Fed: Stable policy

**Term structure:**

| Contract | Price | Days to Expiry |
|----------|-------|----------------|
| Mar | 5,200 | 15 |
| Jun | 5,208 | 105 |

**Spread: -8 points (normal)**

**Trade setup:**

- Entry: Buy Mar @ 5,200, Sell Jun @ 5,208
- Spread: -8 points ($400 per spread)
- Expected convergence: 60% = 4.8 points
- Target: -3.2 points ($160 per spread)
- Position: 20 spreads
- Margin: $40,000

**Trade progression (daily):**

| Day | Mar | Jun | Spread | P&L |
|-----|-----|-----|--------|-----|
| 1 | 5,200 | 5,208 | -8.0 | $0 |
| 3 | 5,205 | 5,210 | -5.0 | +$6,000 |
| 7 | 5,210 | 5,213 | -3.0 | +$10,000 |
| 10 | 5,208 | 5,210 | -2.0 | +$12,000 |
| 14 | 5,212 | 5,213 | -1.0 | +$14,000 |

**Exit (Day 14, one day before Mar expiration):**

- Close @ -1.0 spread
- Profit: 8.0 - 1.0 = 7.0 points
- P&L: 7 × $50 × 20 = **$7,000**
- Return: $7,000 / $40,000 = **17.5% in 14 days**
- Annualized: **456%**

**Why S&P 500 calendars are attractive:**

1. Very liquid (easy entry/exit)
2. Predictable (interest rate driven)
3. Low volatility (smooth P&L)
4. Lower absolute returns but safer
5. **Great for risk-averse traders**

### Example 4: The Disaster - Crude Oil War Premium

**Background:**

- Date: September 15, 2024
- Market: Normal contango
- Trader: Confident after 5 winning trades
- Position: Oversized

**Entry:**

- Buy Oct @ $78, Sell Dec @ $80
- Spread: -$2.00
- Position: 30 contracts (TOO MANY!)
- Margin: $120,000

**Week 1-2: Normal progression**

- Spread narrowing to -$1.60
- P&L: +$12,000
- Feeling great

**Week 3: Disaster strikes (September 28)**

**Breaking news: Major Middle East conflict**

- Saudi oil facilities attacked
- 5M barrels/day offline
- Global supply shock

**Market reaction:**

- Crude gaps up $15 overnight
- Oct (front month) → $95 (massive spike)
- Dec (back month) → $88 (less spike)
- **Spread REVERSED to +$7 (backwardation!)**

**P&L catastrophe:**

- Entry spread: -$2.00
- Current spread: +$7.00
- Movement against: $9.00 per barrel
- Loss: $9 × 1,000 × 30 = **-$270,000**

**But only had $120k margin!**

**Margin call:**

- Broker demands $150,000 additional margin
- Must deposit immediately or liquidated
- **Devastating**

**Forced liquidation (can't meet margin call):**

- Broker closes positions at +$7.20 spread
- Realized loss: **-$276,000**
- Account: $200,000 starting → **$0** (wiped out completely)

**Plus owed: $76,000 to broker**

**What went catastrophically wrong:**

1. ❌ Over-sized position (30 contracts way too many)
2. ❌ Ignored geopolitical risk
3. ❌ No stop loss
4. ❌ Didn't have capital for margin call
5. ❌ Assumed contango would persist
6. ❌ Leveraged 3:1 (reckless)
7. **Complete risk management failure**

**Lessons:**

- Calendar spreads can reverse violently
- Geopolitical events break term structures
- Margin calls can wipe you out
- **Size appropriately!**
- Never risk more than 5-10% of account
- Always have excess capital for margin calls
- **This is why risk management is everything**

---

## Common Mistakes Beginners Make

### Mistake #1: Ignoring Geopolitical Risk

**The error:**

- Trading crude oil calendars
- Middle East tensions escalating
- Think: "Term structure will hold"
- **Ignoring obvious risk**

**What happens:**

- War breaks out
- Supply disrupted
- Backwardation appears
- Contango calendars crushed
- **Loss: 100%+**

**Correct approach:**

$$
\text{Geopolitical risk} \Rightarrow \text{Reduce or exit calendars}
$$

**Crude oil risk factors:**

- OPEC meetings
- Middle East conflicts
- Russia/Ukraine situation
- Sanctions
- Pipeline disruptions

**If ANY are elevated: Reduce size or skip**

### Mistake #2: Not Tracking Roll Dates

**The error:**

- Enter calendar Feb/Apr
- Forget about expiration
- Feb expires (3rd Friday)
- **Still holding position!**

**What happens:**

- Auto-rolled or assigned
- Unexpected position
- Margin requirements change
- **Confusion and loss**

**Correct approach:**

**Calendar for all futures expirations:**

- Mark all roll dates
- Set alerts 7 days before
- Close or roll proactively
- **Never surprised**

**Example calendar:**

| Month | Expiration | Action Day |
|-------|-----------|------------|
| Jan | Jan 19 | Jan 12 |
| Feb | Feb 16 | Feb 9 |
| Mar | Mar 15 | Mar 8 |
| Apr | Apr 19 | Apr 12 |

### Mistake #3: Treating Margin as Risk Capital

**The error:**

- Margin: $4,000 per spread
- Think: "I can risk $4,000"
- Enter 10 spreads with $40k margin
- **Massively under-estimating risk**

**Actual risk:**

Spread can move $5 against you:

$$
\text{Risk} = \$5.00 \times 1,000 \times 10 = \$50,000
$$

**Greater than margin deposited!**

**Result: Margin call and forced liquidation**

**Correct approach:**

$$
\text{Risk} = \text{Max Expected Adverse Move} \times \text{Contract Size} \times \text{Contracts}
$$

Position size based on RISK, not margin!

### Mistake #4: Entering During Roll Week

**The error:**

**Wednesday before Friday expiration:**

- Front month about to expire
- Everyone rolling positions
- Massive calendar volume
- Spreads compressed
- **Enter anyway**

**Why it fails:**

- Bid-ask spreads wide ($0.10-0.20 vs normal $0.02)
- Slippage on entry: -$150
- Poor fill
- **Starting behind**

**Correct approach:**

$$
\text{Wait until } > 5 \text{ days after roll week}
$$

**Next Monday after expiration:**

- Spreads normalized
- Liquidity good
- Better pricing
- **Patience pays**

### Mistake #5: No Stop Loss ("It Will Converge Eventually")

**The error:**

- Entry spread: -$2.00
- Widens to -$2.80
- Think: "It HAS to converge, I'll wait"
- Widens to -$3.50
- Still holding
- **Denial**

**What happens:**

- Fundamental change occurred (didn't notice)
- Structure broken
- Spread: -$4.00
- **Loss: $2.00 per barrel = $20,000 on 10 contracts**

**If had stop at -$2.80:**

- Loss: $0.80 per barrel = $8,000
- **Saved $12,000 by cutting loss**

**Correct approach:**

$$
\text{Stop loss} = \text{Entry} \pm 40\% \text{ of entry spread}
$$

For -$2.00 entry:

$$
\text{Stop} = -\$2.00 \times 1.40 = -\$2.80
$$

**Execute stop, no exceptions!**

### Mistake #6: Trading Illiquid Months

**The error:**

- Sees "amazing" spread in far-dated contracts
- Oct/Apr spread: -$5.00 (super wide!)
- Volume: 50 contracts/day (very low)
- **Enter 10 spreads**

**Why it fails:**

**Liquidity problems:**

- Bid-ask: -$4.80 / -$5.20 ($0.40 wide!)
- Slippage on entry: -$2,000
- Can't exit when needed
- Forced to hold to expiration
- **Illiquidity trap**

**Correct approach:**

Only trade:

- Front 3 months (highest liquidity)
- Volume > 1,000 contracts/day
- Bid-ask < $0.05
- **Liquid markets only**

### Mistake #7: Revenge Trading After Loss

**The error:**

**Trade 1 (Crude calendar):**

- Lost $8,000 on geopolitical event
- Emotional: Angry, frustrated

**Trade 2 (Revenge):**

- Immediately enter new calendar (20 contracts!)
- Oversized to "make it back"
- Marginal setup (spread only -$1.20)
- **All discipline abandoned**

**What happens:**

- Trade 2 also fails (poor setup)
- Loss: $6,000 more
- Now down $14,000 total
- **Spiral**

**Correct approach after loss:**

1. Accept the loss (part of trading)
2. Review what went wrong
3. Wait 3-5 days minimum
4. Only enter HIGH quality setup next
5. Standard size (don't size up)
6. **Emotion-free**

### Mistake #8: Ignoring Fundamental Changes

**The error:**

- Entered crude calendar in contango
- OPEC announces surprise production cut
- Term structure shifts to backwardation
- Trader thinks: "It'll flip back"
- **Ignoring fundamental change**

**What happens:**

- Backwardation persists (new normal)
- Contango calendar bleeds
- Loss mounts
- **Should have exited immediately**

**Correct approach:**

$$
\text{If term structure flips} \Rightarrow \text{EXIT regardless of P\&L}
$$

**Fundamental changes that matter:**

- OPEC policy shifts
- Major supply disruptions
- Demand collapse/surge
- Storage capacity changes
- **Market regime changed → Strategy invalid**

### Mistake #9: Betting the Farm (Over-Concentration)

**The error:**

- Account: $100,000
- Enters 25 crude calendars
- Margin: $100,000 (100% of account!)
- **All eggs in one basket**

**Why it fails:**

**One bad event:**

- Crude gaps $10
- All 25 calendars crushed
- Margin call: $50,000
- Can't meet it
- **Liquidated, account blown**

**Correct approach:**

$$
\text{Max in one market} = 30\text{-}40\% \text{ of account}
$$

$$
\text{Spread across } \geq 3 \text{ uncorrelated markets}
$$

**Better allocation:**

- 40% crude calendars
- 30% S&P 500 calendars
- 30% gold/nat gas
- **Diversified**

### Mistake #10: Not Calculating True Returns

**The error:**

- Made $5,000 on crude calendar
- Margin: $20,000
- Think: "25% return!"
- **But tied up 60 days**

**Actual annualized:**

$$
\text{Annualized} = \frac{\$5,000}{\$20,000} \times \frac{365}{60} = 152\%
$$

**Good, but not 25% per 60 days!**

**Also ignores:**

- Opportunity cost
- Time value of money
- Could have made 3 trades in 60 days
- **True comparison matters**

**Correct approach:**

**Always annualize:**

$$
\text{Annualized Return} = \left(1 + \frac{\text{Profit}}{\text{Margin}}\right)^{\frac{365}{\text{Days}}} - 1
$$

**Compare across strategies on annualized basis**

---

## Best Case Scenario

### The Perfect Calendar Trading Year

**Trader profile:**

- Experience: 3 years
- Account: $200,000
- Strategy: Systematic calendar spreads
- Discipline: Excellent

**Systematic approach:**

**Portfolio allocation:**

- 40% crude oil calendars (4-6 spreads)
- 30% S&P 500 calendars (10-15 spreads)
- 20% gold calendars (2-3 spreads)
- 10% natural gas (seasonal, 2-3 spreads)

**Entry rules:**

- Only when spread > 1.2× historical avg
- Post-roll periods only
- 30-60 DTE front month
- No geopolitical red flags

**Exit rules:**

- 60% of expected convergence
- OR 25 days elapsed
- Stop loss: 40% widening
- **Disciplined execution**

**Monthly results (Year 1):**

| Month | Trades | Wins | Losses | P&L | Return |
|-------|--------|------|--------|-----|--------|
| Jan | 4 | 3 | 1 | +$8,500 | 4.25% |
| Feb | 5 | 4 | 1 | +$9,200 | 4.60% |
| Mar | 6 | 5 | 1 | +$11,000 | 5.50% |
| Apr | 4 | 3 | 1 | +$7,800 | 3.90% |
| May | 5 | 4 | 1 | +$10,200 | 5.10% |
| Jun | 4 | 4 | 0 | +$12,000 | 6.00% |
| Jul | 3 | 2 | 1 | +$5,500 | 2.75% |
| Aug | 4 | 3 | 1 | +$8,800 | 4.40% |
| Sep | 5 | 4 | 1 | +$9,500 | 4.75% |
| Oct | 6 | 5 | 1 | +$13,200 | 6.60% |
| Nov | 5 | 4 | 1 | +$10,800 | 5.40% |
| Dec | 4 | 3 | 1 | +$8,500 | 4.25% |
| **Total** | **55** | **44** | **11** | **+$115,000** | **57.5%** |

**Statistics:**

- Win rate: 80% (44/55)
- Average win: $2,875
- Average loss: -$1,091
- **Expectancy: +$2,091 per trade**

**Account growth:**

$$
\$200,000 \times 1.575 = \$315,000
$$

**Year 2 (compounding):**

Starting with $315,000:

- Monthly avg: 4.8%
- Annual: 75%
- **Ending: $551,250**

**Year 3:**

Starting with $551,250:

- Monthly avg: 4.5% (slower, larger size)
- Annual: 69%
- **Ending: $931,613**

**Three-year summary:**

- Started: $200,000
- Ended: $931,613
- **Total gain: 366%**
- CAGR: 66.7%

**Why this worked:**

1. ✅ Systematic approach (no emotion)
2. ✅ Diversified across markets
3. ✅ Strict entry/exit rules
4. ✅ Position sizing consistent
5. ✅ High win rate maintained
6. ✅ No revenge trading
7. ✅ Disciplined profit taking
8. **Professional execution**

### The Compounding Mathematics

**Key insight: Monthly compounding is POWERFUL**

$$
\text{Annual Return} = (1 + r_{\text{monthly}})^{12} - 1
$$

At 4% monthly:

$$
(1.04)^{12} - 1 = 60\%
$$

At 5% monthly:

$$
(1.05)^{12} - 1 = 80\%
$$

**Even small monthly edge compounds dramatically!**

**Realistic expectations:**

- Beginners: 2-3% monthly (30-40% annually)
- Intermediate: 3-5% monthly (40-80% annually)
- Advanced: 5-7% monthly (80-125% annually)
- **Professionals: 4-6% monthly sustained**

**These are EXCEPTIONAL returns for:**

- Defined risk
- No overnight exposure (mostly)
- Market-neutral strategy
- **Structural edge**

---

## Worst Case Scenario

### The Nightmare: Commodity Super-Cycle Reversal

**Trader profile:**

- Experience: 2 years (thinks expert)
- Account: $500,000
- Overconfident after 18-month winning streak
- **About to learn expensive lesson**

**Setup (June 2025):**

- Crude oil in DEEP contango ($10/barrel spread!)
- Trader: "This is the trade of the decade!"
- Enters MASSIVE position

**Position:**

- 100 crude oil Feb/Dec calendars
- Entry spread: -$10.00
- Margin: $400,000 (80% of account!)
- Think: "$10 spread will narrow to $3, easy $700k profit"
- **Fatal overconfidence**

**Week 1-4: Looking amazing**

- Spread narrowing: -$10 → -$8.50
- Unrealized profit: $150,000
- Think: "I'm a genius!"
- **Confirmation bias**

**Month 2: The Turn**

**Breaking: Global recession declared**

- Demand collapse
- China GDP crashes
- Manufacturing PMI plunges
- **Oil demand crater**

**Market reaction:**

- Spot crude: $75 → $55 (27% crash)
- But contango STEEPENS (recession = weak demand now, hope later)
- Feb drops to $56
- Dec drops to $58
- **Spread: -$2 (flipped from -$8.50!)**

**P&L catastrophe:**

Entry: -$10.00

Current: -$2.00

**Movement: +$8.00 (spread widened massively)**

Loss per contract: $8 × 1,000 = $8,000

Total loss: $8,000 × 100 = **-$800,000**

**But only had $500k account!**

**Margin call:**

- Broker demands $300,000 additional
- Trader can't meet
- **Forced liquidation**

**Liquidation (can't meet margin call):**

- Broker closes all 100 spreads at -$1.50 spread
- Realized loss: -$8.50 × 1,000 × 100 = **-$850,000**
- Account: $500,000 → **$0**
- **Plus owes broker: $350,000**

**Personal bankruptcy filing follows**

### The Psychological Destruction

**Emotional journey:**

**Weeks 1-4 (Euphoria):**

- "This is it! I'll make millions!"
- Telling friends about "guaranteed" trade
- Planning early retirement
- **Delusional optimism**

**Month 2 (Denial):**

- "Just a temporary dip"
- "Spread will narrow again"
- "I'll hold through it"
- **Refusing to accept reality**

**Margin call day (Panic):**

- "No, no, no, this can't be happening"
- Scrambling for capital
- Calling banks, family
- **Desperation**

**Post-liquidation (Depression):**

- Lost everything
- Owes $350k
- Career destroyed
- Relationships strained
- **Complete devastation**

**Long-term damage:**

- Bankruptcy: 7 years on credit
- Can't get another trading account
- PTSD around markets
- **Never recovers**

### What Went Catastrophically Wrong

**Mistake #1: Over-leveraging (FATAL)**

$$
\text{Position size} = 80\% \text{ of account (INSANE!)}
$$

Should have been max 30-40%

**Mistake #2: Assuming spread MUST narrow**

- Spread widened instead
- Recession changed fundamentals
- **No guaranteed convergence**

**Mistake #3: Ignoring macro risks**

- Global slowdown signs visible
- Ignored recession probability
- **Macro > term structure**

**Mistake #4: No stop loss**

- Could have cut at -$11 spread (10% loss)
- Would have lost $100k (painful but survivable)
- Instead held to -$1.50 (170% loss!)
- **Denial killed account**

**Mistake #5: Not understanding leverage**

$$
\text{Notional exposure} = 100 \times \$75,000 = \$7.5M
$$

$$
\text{Leverage} = \frac{\$7.5M}{\$500k} = 15:1
$$

**Any 7% adverse move = account gone**

**Mistake #6: Confusing luck with skill**

- 18-month streak was bull market for calendars
- Thought it was skill
- **Randomness looked like edge**

**How to prevent this nightmare:**

**Rule #1: Never use >40% of account for calendars**

$$
\text{Max allocation} = 40\%
$$

**Rule #2: Hard stop losses**

$$
\text{Exit if spread widens} > 20\%
$$

**Rule #3: Monitor macro regime**

$$
\text{Recession indicators} \Rightarrow \text{Reduce or exit}
$$

**Rule #4: Diversify across markets**

$$
\text{Max in one commodity} = 30\%
$$

**Rule #5: Keep reserve capital**

$$
\text{Never commit } > 50\% \text{ to margin}
$$

**The difference between success and ruin is risk management. One trade, no matter how "sure," should never be able to destroy your account. This trader violated every rule and paid the ultimate price.**

---

## What to Remember

### Core Concept

**Term structure carry exploits predictable futures convergence:**

$$
\text{Calendar Spread P\&L} = (\text{Spread}_{\text{entry}} - \text{Spread}_{\text{exit}}) \times \text{Contract Size} \times \text{Contracts}
$$

- Futures must converge to spot at expiration
- Calendar spreads capture this convergence
- Market-neutral (no directional bet)
- Profit from time decay / roll yield
- Requires active management

### The Setup

**Standard structure:**

- Buy near-term futures (cheaper in contango)
- Sell far-term futures (more expensive)
- Delta-neutral position
- Profit as spread narrows

**In contango:**

- Long calendar (buy front, sell back)
- Expect spread to narrow
- Positive theta (roll yield)

**In backwardation:**

- Short calendar (sell front, buy back)
- Expect spread to narrow
- Positive theta (opposite structure)

### Contract Selection

**Best for beginners:**

- Crude Oil (CL): Most liquid, $1-3 spreads
- S&P 500 (ES): Safest, predictable, small spreads
- Gold (GC): Stable contango, conservative

**Avoid initially:**

- Natural Gas (too volatile)
- Agricultural (complex seasonality)
- Illiquid contracts (wide spreads)

### Time Selection

**Enter when:**

- Term structure wider than normal
- Post-roll period (5+ days after expiration)
- Front month 30-60 DTE
- No major reports imminent

**Exit when:**

- 50-70% of expected convergence achieved
- Front month <7 DTE (roll risk)
- Fundamental change occurs
- Stop loss triggered

### Maximum Profit and Loss

**Typical expectations:**

- Win rate: 70-80%
- Average return per trade: 20-40% (on margin)
- Holding period: 20-40 days
- Annualized: 60-200% (with discipline)

**Maximum loss:**

- Can lose multiples of margin!
- Spread can widen 2-3× entry
- Margin calls possible
- **Risk management critical**

### When to Use

**Ideal conditions:**

- Persistent contango or backwardation
- Stable geopolitical environment
- Clear seasonal patterns (commodities)
- High liquidity in contracts
- You can monitor daily

### When NOT to Use

**Avoid:**

- Flat or inverted term structure
- High geopolitical risk
- Just before major reports
- During roll week
- Illiquid markets
- Can't monitor positions

### Risk Management

**Position sizing:**

$$
\text{Max per market} = 30\text{-}40\% \text{ of account}
$$

$$
\text{Contracts} = \frac{\text{Risk Tolerance}}{\text{Expected Max Adverse Move}}
$$

**Stop losses:**

$$
\text{Exit if spread widens} > 40\% \text{ from entry}
$$

**Diversification:**

- Spread across 3+ uncorrelated markets
- Energy + financial + metals
- Different roll cycles
- **Reduce concentration risk**

### Common Mistakes

1. Ignoring geopolitical risk
2. Not tracking roll dates
3. Treating margin as risk capital
4. Entering during roll week
5. No stop loss ("will converge eventually")
6. Trading illiquid months
7. Revenge trading after loss
8. Ignoring fundamental changes
9. Over-concentration (betting farm)
10. Not calculating true annualized returns

### The Numbers That Matter

**Crude oil typical:**

- Spread: $1.50-$2.50 in contango
- Margin: $4,000 per spread
- Expected profit: $800-1,200 per trade
- Return: 20-30% per trade
- **Annualized: 150-250%**

**S&P 500 typical:**

- Spread: 5-10 points per quarter
- Margin: $2,000 per spread
- Expected profit: $150-300 per trade
- Return: 7-15% per trade
- **Annualized: 80-150%**

### Success Factors

**Three pillars:**

1. **Term structure analysis** (enter when wide)
2. **Risk management** (size conservatively, use stops)
3. **Discipline** (systematic execution, no emotion)

**Formula:**

$$
\text{Success} = \text{Quality Setups} \times \text{Proper Sizing} \times \text{Discipline}
$$

### Your Learning Path

**Month 1:** Paper trade (learn mechanics, track live spreads)

**Month 2:** Real money, 1 spread only (ES or CL)

**Month 3-4:** 2-3 spreads if profitable

**Month 6:** Full allocation (up to 40% of account)

**Year 1:** Systematic approach, multiple markets

### Final Wisdom

> "Term structure carry is one of the few remaining structural edges in markets—the mechanical convergence of futures to spot creates predictable profit opportunities. But this edge comes with a price: geopolitical risk, margin calls, and the potential for catastrophic losses if over-leveraged. The successful calendar trader is paranoid about risk, diversified across markets, and disciplined about sizing. They enter when term structures are wide, exit when convergence targets are hit, and NEVER bet the farm on one trade. Master these principles, and calendar spreads can generate consistent double-digit monthly returns. Violate them, and you'll join the graveyard of over-leveraged traders who thought convergence was guaranteed. It's not the strategy that determines success—it's the risk management."

**Most important principles:**

- Margin is NOT your risk (can lose multiples)
- Geopolitical events break term structures
- Diversification is mandatory (3+ markets)
- Stop losses are survival tools
- Size conservatively (30-40% max per market)
- Convergence is likely, not guaranteed
- Roll dates must be tracked religiously
- Macro regime changes invalidate setups

**Why this works:**

- Arbitrage forces ensure convergence
- Cost of carry creates structure
- Physical constraints (storage, delivery)
- **Structural, not speculative edge**

**But remember:**

- Requires active management (daily monitoring)
- Geopolitical risk can destroy positions
- Leverage cuts both ways
- One bad trade can wipe out months of gains
- **Respect the risk**

**Trade calendars when spreads are wide, exit when targets hit, and always keep capital reserved for margin calls. The graveyard is full of traders who over-leveraged "guaranteed" convergence trades. 📈⚖️**
