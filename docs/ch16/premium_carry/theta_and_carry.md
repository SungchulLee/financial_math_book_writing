# Theta and Carry

**Theta and carry** are strategies where you profit from the passage of time itself by systematically collecting option premium as options decay toward expiration.


- Every option loses value as time passes (all else equal)
- This is called "time decay" or "theta"
- Most traders fight theta (pay it, try to overcome it)
- But you can profit FROM theta by being on the other side
- Sell options, collect premium, let time work for you
- "Earn rent" on volatility

**The key equation:**

$$
\text{Option Value} = \text{Intrinsic Value} + \text{Time Value}
$$

As time passes:

$$
\text{Time Value} \to 0 \text{ (at expiration)}
$$

**You're essentially betting: "I can collect more premium from time decay than I lose from adverse price movements."**

---

## What Is Theta?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/theta_and_carry_by_strike.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 1:** Theta And Carry By Strike visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/theta_and_carry_decay_curve.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 2:** Theta And Carry Decay Curve visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/theta_and_carry_pnl.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 3:** Theta And Carry Pnl visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/theta_and_carry_strategies.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 4:** Theta And Carry Strategies visualization.

---

## The Core Insight

**The fundamental idea:**

**Before understanding carry trades, understand theta:**

### 1. The Definition

**Theta (Θ)** is the rate of time decay of an option:

$$
\Theta = \frac{\partial V}{\partial t}
$$

**In practical terms:**

- How much the option loses in value per day (all else equal)
- Measured in dollars per day
- Always negative for long options (you pay)
- Always positive for short options (you collect)

**Example:**

- Buy ATM call for $5
- Theta = -$0.20 per day
- Tomorrow (if stock unchanged): option worth $4.80
- You lost $0.20 to time decay

### 2. The Decay Curve

**Time decay is NOT linear - it accelerates near expiration:**

```
Option Value
    ↑
  5 |‾‾‾\___
  4 |       \__
  3 |          \_
  2 |            \__
  1 |               \___
  0 |___________________\___→ Time
    90  60  30  15   5   0 Days
```

**Key insight:** Most decay happens in final 30 days!

**Implications:**

- Last month: rapid decay
- 90 days out: slow decay
- Theta accelerates as expiration approaches

### 3. Theta for Differe

**ATM options:**

- Highest theta (most time value)
- Maximum decay rate
- "Sweet spot" for decay

**OTM options:**

- Lower theta (less time value)
- Less decay in dollars
- But can go to zero faster (percentage)

**ITM options:**

- Lower theta (mostly intrinsic value)
- Less time value to decay
- More stable

**Near expiration:**

- Theta explodes (accelerates dramatically)
- Can lose 50% of value in last week
- "Gamma risk" increases too

---

## Time Value vs.

**Understanding this split is crucial:**

### 1. The Components

$$
\boxed{\text{Option Price} = \text{Intrinsic Value} + \text{Time Value}}
$$

**Intrinsic Value:**

- What the option is worth if exercised today
- Call: $\max(S - K, 0)$
- Put: $\max(K - S, 0)$
- This NEVER decays (only changes with stock price)

**Time Value:**

- Premium above intrinsic value
- The "hope" premium (might go ITM)
- The "volatility" premium
- This ALWAYS decays to zero at expiration

### 2. Examples

**ATM Option (S = K = $100):**

- Stock at $100
- ATM call trading at $5
- Intrinsic value: $0 (not ITM)
- Time value: $5 (all of it!)
- **100% time value = maximum theta**

**ITM Option (S = $110, K = $100):**

- Stock at $110
- $100 call trading at $12
- Intrinsic value: $10 (if exercised)
- Time value: $2 (premium above intrinsic)
- **Most value is intrinsic, less theta**

**OTM Option (S = $90, K = $100):**

- Stock at $90
- $100 call trading at $1
- Intrinsic value: $0
- Time value: $1
- **All time value, but small absolute theta**

**Key insight:** ATM options have maximum TIME VALUE in dollars, hence maximum THETA in dollars.

---

## What Are Carry

**Carry trades systematically profit from positive theta:**

### 1. The Basic Concept

**In options:**

- **Positive carry** = collect money daily (short options)
- **Negative carry** = pay money daily (long options)

**Carry trade strategy:**

- Sell options (collect premium)
- Manage the resulting risks
- Let theta work for you day after day
- Earn "income" from time decay

**The trade-off:**

- Positive theta (collect daily)
- But negative gamma (hurt by large moves)
- **Classic risk/reward balance**

### 2. Why "Carry"?

**Term comes from interest rate markets:**

- Borrow low-rate currency, invest in high-rate currency
- "Carry" the interest rate differential
- In options: "carry" the theta collection

**Options carry:**

- Short options = positive carry (collect theta)
- Long options = negative carry (pay theta)

---

## The Theta vs. Gamma

**This is THE fundamental trade-off in options:**

### 1. The Relationship

$$
\text{High Theta} \Leftrightarrow \text{High Gamma}
$$

**For ATM options:**

**If you're SHORT (collect theta):**

- ✓ Positive theta: collect $X per day
- ✗ Negative gamma: hurt if stock moves

**If you're LONG (pay theta):**

- ✗ Negative theta: pay $X per day
- ✓ Positive gamma: profit if stock moves

**There's no free lunch:**
- Can't have positive theta AND positive gamma
- Must choose: collect carry OR benefit from movement

### 2. The Mathematical

**From Black-Scholes PDE:**

$$
\Theta + r S \Delta + \frac{1}{2}\sigma^2 S^2 \Gamma = 0
$$

**Rearranging for ATM (Δ ≈ 0):**

$$
\Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma
$$

**In plain English:**

- Theta and Gamma have opposite signs
- High absolute gamma → high absolute theta
- They're two sides of same coin

**The choice:**

- Want steady income (positive theta)? → Accept risk from large moves (negative gamma)
- Want to profit from large moves (positive gamma)? → Accept daily bleed (negative theta)

---

## Common Carry Trade

### 1. Short Straddles/S

**Structure:**

- Sell ATM call + ATM put (straddle)
- Or sell OTM call + OTM put (strangle)
- Collect maximum theta

**Characteristics:**

- Maximum positive theta
- Unlimited loss potential
- Profit if stock stays in range
- **VERY RISKY**

**Example:**

- Stock at $100
- Sell $100 straddle for $10
- Collect $10 premium
- Theta: +$50/day (roughly)
- Profit if stock stays between $90-$110

**Risk:** Stock gaps to $80 or $120 = huge losses

**Use cases:**

- High IV environments (after events)
- Strong range-bound conviction
- Sophisticated risk management

### 2. Iron Condors

**Structure:**

- Sell OTM call spread + OTM put spread
- Defined risk (wings protect)
- Lower theta but safer

**Example:**

- Stock at $100
- Sell $105/$110 call spread (receive $2)
- Sell $95/$90 put spread (receive $2)
- Total credit: $4
- Max loss: $1 (spread width - credit)
- Theta: +$20/day

**Advantage:** Defined risk (max loss is $1)
**Disadvantage:** Lower theta collection, defined profit

**Use cases:**

- Risk-averse carry trades
- Range-bound expectations
- Lower theta but sleep better

### 3. Calendar Spreads

**Structure:**

- Short front month (high theta)
- Long back month (low theta)
- Net positive theta

**Example:**

- Sell 1-month ATM call (theta -$20/day)
- Buy 3-month ATM call (theta -$8/day)
- Net theta: +$12/day

**Characteristics:**

- Positive carry
- Also long vega (bonus!)
- Limited risk
- Works best in stable markets

**We covered this extensively in the calendar spreads chapter!**

### 4. Ratio Spreads

**Structure:**

- Sell more options than you buy
- Unbalanced risk
- High theta collection

**Example:**

- Buy 1 ATM call
- Sell 2 OTM calls
- Net credit (positive theta)
- But unlimited upside risk beyond second strike

**Use cases:**

- Moderately bullish view
- Willing to accept upside risk
- Maximize theta collection

### 5. Covered Calls

**Structure:**

- Own stock (long)
- Sell OTM calls against it
- Collect call premium (positive theta)

**Example:**

- Own 100 shares at $100
- Sell $110 call for $2
- Collect $200 premium
- Keep if stock stays below $110
- Give up upside above $110

**Characteristics:**

- Positive theta from short call
- Keep dividends (if any)
- Cap upside at strike
- Still have downside risk (from stock)

**Popular strategy:**

- Income generation
- "Rent out" upside optionality
- Works in flat/modestly bullish markets

### 6. Cash-Secured Puts

**Structure:**

- Sell OTM puts
- Hold cash to cover assignment
- Collect put premium

**Example:**

- Stock at $100, want to buy at $95
- Sell $95 put for $2
- If assigned: buy stock at $95 (net cost $93)
- If not assigned: keep $2 premium

**Characteristics:**

- Positive theta
- Obligated to buy if assigned
- "Get paid to place limit order"

**Use cases:**

- Want to own stock anyway
- Bullish but patient
- Willing to buy on dips

---

## The Carry Trade P&L

**For a typical short options carry trade:**

$$
\text{Daily P\&L} \approx \underbrace{\theta \, \delta t}_{\text{positive carry}} + \underbrace{\frac{1}{2}\Gamma(\delta S)^2}_{\text{negative from moves}} + \underbrace{\text{Vega} \cdot \delta\sigma}_{\text{negative from IV rise}}
$$

**Breaking it down:**

### 1. Theta Collection

**Steady, predictable income:**

- Collect theta every day
- Accelerates near expiration
- Compounds over time
- "Earn while you sleep"

**Example:**

- Short straddle: +$50/day theta
- 30 days: +$1,500 potential
- If stock stays calm: collect it all!

### 2. Gamma Loss (Your

**From price movements:**

- Stock moves → position loses value
- Quadratic in move size
- Large moves hurt disproportionately
- Can overwhelm theta quickly

**Example:**

- Stock moves 5%: lose $1,000 (gamma)
- But collected $50/day theta
- Move in 1 day wipes out 20 days of theta!

### 3. Vega Loss (IV

**From volatility increases:**

- Short options = short vega
- If IV rises → lose money
- Can happen quickly (events, panic)
- Correlated with price moves often

**Example:**

- IV rises 5%: lose $500
- Eats into theta collection
- Especially bad if combined with price move

### 4. The Math

**Expected daily P&L:**

$$
E[\text{Daily P\&L}] = \theta - \frac{1}{2}\sigma^2 S^2 |\Gamma|
$$

**For carry trade to work:**

$$
\theta > \frac{1}{2}\sigma^2 S^2 |\Gamma|
$$

**In plain English:**

- Theta collected > Expected gamma losses
- Realized vol < Implied vol (on average)
- **This is the "volatility risk premium"**

---

## The Volatility Risk

**Why do carry trades work? The vol risk premium:**

### 1. Empirical Observa

**Historical data shows:**

$$
\text{Implied Volatility} > \text{Realized Volatility} \quad \text{(on average)}
$$

**Example statistics (S&P 500):**

- Average IV (VIX): ~20%
- Average realized vol: ~15%
- Premium: ~5% points
- **Short vol earns this premium over time**

### 2. Why Does This

**Three reasons:**

**1. Insurance Premium:**

- People pay for protection (puts)
- Willing to overpay
- Supply/demand imbalance
- **Hedgers subsidize premium sellers**

**2. Risk Aversion:**

- Investors fear downside more than love upside
- Loss aversion
- Behavioral bias
- Pay up for protection

**3. Tail Risk:**

- Crashes are catastrophic
- Short vol loses huge in crashes
- Premium compensates for tail risk
- **Not a free lunch - earn premium but risk blowup**

### 3. The Trade-off

**Carry trades exploit this premium:**

- Collect theta (premium) systematically
- Most of the time: small, steady profits
- Occasionally: large losses (crashes)
- **"Picking up nickels in front of steamroller"**

**Risk profile:**
```
Frequency Distribution of Returns:
    
    Frequency
       ↑
       |     ___
       |    /   \___
       |   /        \___
       |  /             \___
  _____|_/________________\_____→ Returns
  -100%      -10% 0  +10%   +20%
   (Rare      (Common small profits)
    crash)
```

**Most days:** Small theta collection
**Rare days:** Large gamma losses

---

## Managing Carry

**How to survive as a theta collector:**

### 1. Position Sizing

**Golden rule:**

$$
\text{Max Position Size} = \frac{\text{Max Acceptable Loss}}{\text{Potential Loss per Contract}}
$$

**Never risk more than 2-5% on any single position:**

- Short straddle can lose 5-10× premium
- Size accordingly
- One blowup can wipe out months of profits

**Example:**

- Portfolio: $100,000
- Risk per trade: 2% = $2,000
- Short straddle potential loss: $10,000
- Max size: $2,000/$10,000 = 20% of full size

### 2. Defined Risk

**Use spreads instead of naked shorts:**

- Iron condors (not short straddles)
- Credit spreads (not naked puts/calls)
- Calendars (limited risk)
- **Trade off: lower theta, but defined loss**

**Example:**

- Naked short straddle: +$50/day theta, unlimited loss
- Iron condor: +$20/day theta, max loss $500
- **Choose safety over greed**

### 3. Stop Losses and

**Pre-defined exits:**

- If stock moves X% → close immediately
- If loss reaches Y% → exit
- Don't hope it comes back
- **Discipline beats hope**

**Example rules:**

- Stock moves >5% → close
- Loss exceeds 50% of max profit → close
- IV rises >10% → close
- Never "double down"

### 4. Diversification

**Don't concentrate:**

- Multiple underlyings (not just one stock)
- Multiple strategies (not just short straddles)
- Multiple timeframes
- **Don't put all eggs in one basket**

**Example:**

- 5 different stocks
- Mix of iron condors + calendars
- Different expiration dates
- Correlation < 1 between positions

### 5. Volatility Regime

**Know the environment:**

- VIX < 15: dangerous time to sell vol (premium low)
- VIX 15-25: normal environment
- VIX > 25: good time to collect premium (but risky!)
- VIX > 40: excellent premium, but risk is real

**Adjust size based on vol regime:**

- Low VIX: smaller positions
- High VIX: normal positions (more premium justifies risk)

### 6. Roll and Adjust

**Don't be static:**

- As positions move, adjust
- Roll losing side
- Take profits early (50% of max)
- **Active management required**

### 7. Event Awareness

**Avoid carry trades around:**

- Earnings announcements
- FOMC meetings
- Binary events (FDA, elections)
- Known catalysts
- **Theta collection not worth event risk**

---

## Concrete Example

**A systematic theta collection strategy:**

### 1. Setup

- **Stock:** SPY at $450
- **Market:** VIX at 18 (normal)
- **View:** Market will stay in range for next month

**Strategy:** Sell monthly iron condor

**Structure:**

- Sell $460/$465 call spread (5 points wide)
- Sell $440/$435 put spread (5 points wide)
- Total credit: $1.50
- Max loss: $3.50 ($5 - $1.50)
- Risk/reward: $3.50 risk to make $1.50

**Position Greeks:**

- Theta: +$25/day
- Gamma: -0.15 (negative)
- Vega: -$40 (negative)
- Delta: ~0 (neutral)

**Margin requirement:** ~$500 per contract

### 2. The Trade Over

**Day 1:**

- Open position, collect $150 credit (1 contract)
- Theta: +$25/day
- SPY at $450

**Week 1 (Day 7):**

- SPY drifts to $452 (small move)
- Position value: -$120 (down from -$150)
- Collected theta: $25 × 7 = $175
- Net P&L: +$30
- **Small profit, on track**

**Week 2 (Day 14):**

- SPY at $455 (moving toward short call)
- Position value: -$85
- Cumulative theta: $25 × 14 = $350
- Net P&L: +$65
- **Monitoring, but OK**

**Week 3 (Day 21):**

- SPY at $451 (back toward center)
- Position value: -$50
- Cumulative theta: $25 × 21 = $525
- Net P&L: +$100
- **Two thirds toward max profit**

**Week 4 - Expiration (Day 30):**

- SPY at $452 (between strikes)
- All options expire worthless
- **Collect full $150 credit**
- Return on margin: 30% in one month

### 3. Risk

**Alternative: Surprise Fed announcement Day 10:**

- SPY gaps to $465 (+3.3%)
- Position now losing: -$450 (near max loss)
- Decision: Close immediately
- Net loss: -$450 + ($25 × 10) = -$200
- **One bad move wipes out 1.3 months of profits**

**This illustrates:**

- Most of the time: small steady profits
- Occasionally: larger losses
- Net positive expectancy (if volatility risk premium exists)
- **Need proper risk management**

---

## Carry Trades Across

**How theta fits into strategies we've covered:**

| Strategy | Theta | Carry Trade? | Risk Management |
|----------|-------|--------------|-----------------|
| **Straddles (Long)** | Negative | No (pay theta) | Limited loss |
| **Straddles (Short)** | Positive | **Yes** (pure carry) | Unlimited loss - RISKY |
| **Gamma Scalping** | Negative | No (overcome with rebalancing) | Delta hedging |
| **Vega Trading** | Negative | No (trade IV changes) | Delta hedging |
| **Smile/Skew** | Mixed | Depends on structure | Complex |
| **Calendar Spreads** | **Positive** | **Yes** (theta differential) | Limited risk |
| **Iron Condors** | **Positive** | **Yes** (safe carry) | Defined risk |
| **Dispersion** | Mixed | No (trade correlation) | Multiple hedges |
| **Convertibles** | Some | Yes (coupon + gamma) | Complex |
| **Variance Swaps** | None | No (pure variance) | No theta |

**Pure carry strategies:**

1. Short straddles/strangles (risky!)
2. Iron condors (safer)
3. Calendar spreads (positive theta + vega)
4. Covered calls (equity income)

---

## The "Picking Up

**Often used to describe carry trades:**

### 1. The Analogy

> "Selling options is like picking up nickels in front of a steamroller"

**What it means:**

- Nickels = small theta profits daily
- Steamroller = rare but catastrophic losses
- Most days: pick up nickels (collect theta)
- Rare days: steamroller runs you over (gamma losses)

### 2. The Reality

**It's not quite that grim IF:**
1. **Position sizing:** Don't pick up too many nickels at once
2. **Risk management:** Look up for the steamroller (watch the market)
3. **Diversification:** Pick up nickels from multiple streets
4. **Stops:** Jump out of the way when steamroller comes (exit rules)
5. **Premium sizing:** Pick up quarters in high vol (not nickels in low vol)

**With discipline:**

- Small, consistent profits
- Occasional manageable losses
- Positive expectancy overall
- **Not crazy - but requires discipline**

**Without discipline:**

- One blowup erases years of profits
- Temptation to "double down"
- Eventually the steamroller wins
- **This is how vol sellers blow up**

---

## Historical Blowups

**Famous carry trade disasters:**

### 1. Option Sellers,

**Structure:**

- Retail fund selling naked options
- Claimed "safe" income strategy
- Customers thought it was conservative

**The blowup:**

- Natural gas extreme volatility (Feb 2018)
- Naked short options
- Losses exceeded account values
- Customers owed money BEYOND their investment

**Lessons:**

- Naked options = unlimited risk
- "Safe income" can be misleading
- Need defined risk structures
- Position sizing critical

### 2. James Cordier

**Same fund, November 2018:**

- Natural gas volatility again
- Account blown up entirely
- $150M+ losses
- Fund liquidated

**Video:** Founder made tearful apology video
**Result:** Investors lost everything

**Lessons:**

- Repeated mistakes (didn't learn)
- Concentration risk (too much natgas)
- Leverage magnifies disasters
- **Carry trades can destroy capital**

### 3. Victor Niederhoff

**Famous trader, sold puts on crash:**

- October 1997 Asian crisis
- Short large amounts of S&P puts
- Market crashed suddenly
- Lost everything

**Lessons:**

- Even experienced traders can blow up
- Short vol + leverage = disaster
- Tail risk is real
- Can't predict crashes

### 4. Many Hedge Funds

**Financial crisis and COVID:**

- Many vol-selling funds decimated
- Correlation went to 1
- Diversification failed
- Credit + equity + vol all collapsed together

**Lessons:**

- "Regime changes" destroy carry trades
- What works in normal times fails in crises
- Need extreme risk management
- Don't over-leverage

---

## Pros and Cons of

### 1. Advantages ✓

**1. Positive carry (time is your friend)**

- Collect money daily
- Don't need market to move
- Predictable income stream
- Compounding over time

**2. High win rate**

- Most months profitable (often 70-80%)
- Small steady gains
- Psychologically satisfying
- "Income" feel

**3. Exploit volatility risk premium**

- Structural edge (IV > realized vol)
- Market inefficiency
- ~5% annual premium historically
- Quantifiable edge

**4. Range-bound markets perfect**

- Don't need direction
- Sideways is ideal
- Most markets are range-bound
- Natural fit

**5. Multiple strategies available**

- Iron condors (safe)
- Calendars (positive theta + vega)
- Covered calls (equity income)
- Flexibility

**6. Scalable**

- Can do small or large
- Works for retail and institutions
- Liquidity in major products
- Accessible

### 2. Disadvantages ✗

**1. Tail risk (steamroller!)**

- Rare catastrophic losses
- Can lose months/years of profits in one day
- Unlimited loss (if naked)
- **This is the big one**

**2. Negative gamma (hurt by moves)**

- Large price moves deadly
- Accelerating losses
- Need to act fast
- Uncomfortable

**3. Negative vega (hurt by IV spikes)**

- Vol rises → lose money
- Often correlated with price moves
- Double whammy in crises
- Hard to hedge

**4. Requires active management**

- Can't "set and forget"
- Need monitoring
- Quick decisions required
- Stressful

**5. Low reward/risk ratio**

- Collect $1 to risk $3-5
- Asymmetric the wrong way
- Many wins needed for one loss
- Grindy

**6. Temptation to over-leverage**

- "Easy money" feel
- Encourages bigger size
- Leverage magnifies disasters
- Behavioral trap

**7. Event risk**

- Earnings, news, crashes
- Gaps over weekend
- Can't always exit
- Binary outcomes

**8. Regulatory risk (margin)**

- High margin requirements
- Margin calls possible
- Forced liquidation
- Capital intensive

---

## When Carry Trades

### 1. Favorable Conditi

**1. High implied volatility (post-event)**

- VIX > 25
- Options expensive
- Collect more premium
- Justifies the risk

**2. Stable, range-bound markets**

- Low realized volatility expected
- Consolidation phases
- Post-trend exhaustion
- Sideways grinding

**3. Post-event windows**

- After earnings (vol crush)
- After Fed meetings
- After elections
- Known catalyst past

**4. Normal vol environment (not crisis)**

- VIX 15-25 range
- Not complacent (VIX < 12)
- Not panic (VIX > 40)
- Goldilocks zone

**5. You have risk discipline**

- Stop losses defined
- Position sizing rules
- Diversification
- **Most important!**

### 2. Unfavorable

**1. Very low vol (VIX < 12)**

- Premium tiny
- Not worth the risk
- Complacency before crash
- **Most dangerous time**

**2. Before known events**

- Earnings upcoming
- Binary catalysts
- Event risk not compensated
- Avoid

**3. Crisis/panic (VIX > 40)**

- Extreme gamma risk
- Gap risk huge
- Even though premium attractive
- Too risky for most

**4. Trending markets**

- Strong directional moves
- Gamma losses accumulate
- Theta can't keep up
- Pick direction instead

**5. Low liquidity**

- Wide spreads
- Hard to exit
- Slippage kills edge
- Stick to liquid products

---

## Practical Implementa

### 1. Step 1

**Conservative (recommended for most):**

- Iron condors
- Credit spreads with defined risk
- Calendars
- Small size

**Aggressive (experienced only):**

- Short straddles with stops
- Ratio spreads
- Higher size
- **Requires discipline**

### 2. Step 2

**Before entering any trade:**

$$
\begin{align}
\text{Max Loss per Trade} &= 2-5\% \text{ of Portfolio} \\
\text{Position Size} &= \frac{\text{Max Loss}}{\text{Risk per Contract}} \\
\text{Stop Loss} &= 50\% \text{ of Max Profit} \\
\end{align}
$$

**Example:**

- $100,000 portfolio
- 2% risk = $2,000 max loss
- Iron condor risk per contract: $350
- Max contracts: 5
- Stop loss trigger: lose $75 per contract

### 3. Step 3

**When to enter:**

- 30-45 days to expiration (sweet spot)
- After vol spike (elevated IV)
- Post-event (known catalyst past)
- VIX percentile check (not too low)

**Example:**

- Earnings passed yesterday
- IV 50% → expecting crush to 30%
- Enter short straddle or iron condor
- Capture vol crush + theta

### 4. Step 4

**Daily:**

- Check position P&L
- Monitor underlying price
- Watch for approaching stops

**Weekly:**

- Adjust if needed (roll strikes)
- Take profits at 50% of max
- Review Greeks

**At trouble:**

- Stock approaching strike: roll or close
- Loss hits stop: close immediately
- IV spiking: consider exit
- **Never hope, always act**

### 5. Step 5

**Exit when:**

- Profit target hit (50% of max)
- Time to expiration < 7 days (gamma risk high)
- Stop loss triggered
- Event announced (earnings, etc.)
- Better opportunity elsewhere

**Never:**

- Hold to expiration hoping for max profit
- "Double down" on losing position
- Remove stops mid-trade
- Let ego drive decisions

---

## Systematic Carry

**A professional approach:**

### 1. The "Monthly Iron

**Strategy:**

- Sell SPY iron condors monthly
- 30-45 days to expiration
- Target $150 credit per contract
- Max risk $350 per contract
- Portfolio allocation: 20% of capital

**Entry criteria:**

- VIX > 15 (not too low)
- SPY not near major support/resistance
- No major events in next 30 days
- Historical vol < implied vol

**Position sizing:**

- $100k portfolio
- 20% = $20k allocated
- Risk per contract: $350
- Max contracts: $20k / $350 = 57 contracts
- **Actually use: 30 contracts (50% of max for safety)**

**Management:**

- Enter first week of month
- Exit at 50% profit or day 7 before expiration
- Stop loss: 100% of credit received
- Roll if stock moves toward strike
- Max 3 concurrent positions (different strikes)

**Expected results (based on backtests):**

- Win rate: 75%
- Average win: $75 per contract
- Average loss: -$150 per contract
- Expected value: 0.75($75) - 0.25($150) = $18.75 per contract
- Monthly expected: $18.75 × 30 contracts = $563
- **~6.7% per month on allocated capital (if everything goes as expected)**

**Reality:**

- Some months: lose
- Some months: win big
- Average: positive
- Black swans: painful
- **Requires discipline to stick with it**

---


---



## Economic

**Understanding what this strategy REALLY represents economically:**

### 1. The Core Economic

This strategy involves specific economic trade-offs that determine when it's most valuable. The key is understanding what you're giving up versus what you're gaining in economic terms.

**Economic equivalence:**

$$
\text{Strategy P\&L} = \text{Greeks Exposure} + \text{Rebalancing} - \text{Costs}
$$

### 2. Why This Structur

Markets create these strategies because different participants have different:
- Risk preferences (directional vs. convexity)
- Time horizons (short-term vs. long-term)
- Capital constraints (leverage limitations)
- View on volatility vs. direction

### 3. Professional

Institutional traders view this strategy as a tool for:
1. **Greeks arbitrage:** Extracting value from Greeks mispricing
2. **Risk transformation:** Converting one type of risk into another
3. **Capital efficiency:** Optimal use of buying power for Greeks exposure
4. **Market making:** Providing liquidity while managing Greeks

Understanding the economic foundations helps you recognize when the strategy offers genuine edge versus when market pricing is fair.


## Practical Guidance

**Step-by-step implementation framework:**

### 1. Step 1

**Before entering, evaluate:**

1. **Volatility environment:**
   - Current IV level and percentile
   - Implied vs. realized volatility spread
   - Term structure of volatility

2. **Greeks landscape:**
   - Which Greeks are mispriced
   - Expected Greeks P&L
   - Rebalancing frequency required

3. **Market conditions:**
   - Liquidity in options and underlying
   - Bid-ask spreads
   - Transaction cost environment

### 2. Step 2

**Enter this strategy when:**
- [Specific Greeks conditions]
- [Volatility requirements]
- [Liquidity sufficient for rebalancing]
- [Expected Greeks P&L > costs]

**Avoid this strategy when:**
- [Unfavorable Greeks environment]
- [High transaction costs]
- [Insufficient liquidity]
- [Wrong volatility regime]

### 3. Step 3

**Calculate maximum position size:**

$$
\text{Max Size} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Greeks Loss}}
$$

**For Greeks strategies, consider:**
- Greeks exposure limits
- Rebalancing capacity
- Capital for hedge adjustments
- Margin requirements

### 4. Step 4

**Best practices:**

1. **Greeks analysis:** Calculate all relevant Greeks before entry
2. **Liquidity check:** Ensure sufficient volume for rebalancing
3. **Spread analysis:** Check bid-ask spreads on all legs
4. **Hedge execution:** Enter hedges simultaneously with options

**Rebalancing framework:**
- Delta rebalance when: |Δ| > threshold
- Vega adjustment when: IV moves X%
- Gamma management when: Position size changes
- Transaction cost consideration: Balance frequency vs. cost

### 5. Step 5

**Active management rules:**

**Greeks monitoring:**
- Track delta daily (minimum)
- Monitor gamma exposure
- Watch vega for IV changes
- Calculate P&L attribution by Greek

**Rebalancing triggers:**
- Delta: Rebalance when exceeds threshold
- Vega: Adjust on IV regime changes
- Gamma: Scale position with proximity to strikes
- Theta: Monitor daily decay

**Profit/loss targets:**
- Take profit at: [Greeks P&L target]
- Cut losses at: [Max acceptable Greeks loss]
- Time-based exit: [Time decay considerations]

### 6. Step 6

**Greeks risk limits:**
- Max delta exposure: [Limit]
- Max gamma concentration: [Limit]
- Max vega exposure: [Limit]
- Theta bleed tolerance: [Limit]

**Portfolio-level controls:**
- Correlation of Greeks across positions
- Aggregate exposure monitoring
- Stress testing for market moves
- Worst-case scenario planning

### 7. Step 7

**Track for every trade:**
- Entry Greeks (delta, gamma, vega, theta)
- Rebalancing frequency and costs
- P&L by Greek component
- Actual vs. expected volatility
- Transaction costs vs. Greeks P&L
- Lessons learned

### 8. Common Execution

1. **Ignoring transaction costs** - Frequent rebalancing eats profits
2. **Wrong rebalancing frequency** - Too often or too infrequent
3. **Insufficient liquidity** - Cannot execute rebalances efficiently
4. **Over-leveraging Greeks** - Excessive exposure to single Greek
5. **Neglecting other Greeks** - Focus on one Greek, ignore others
6. **Poor hedge timing** - Waiting too long or reacting too quickly

### 9. Professional

**For delta hedging:**
- Use delta bands (don't chase every move)
- Consider transaction costs
- Rebalance at consistent intervals

**For gamma scalping:**
- Need sufficient realized vol
- Monitor gamma P&L vs. theta cost
- Scale position size with gamma exposure

**For vega trading:**
- Understand vol term structure
- Watch for regime changes
- Consider vega cross-effects (vanna, volga)


## Common Mistakes

[Common errors to avoid]



---

## Real-World Examples

[Concrete examples]


## Final Wisdom

**Carry trades can work, but:**

1. **Start small** - learn with small size
2. **Use defined risk** - spreads not naked
3. **Honor stops** - no exceptions
4. **Diversify** - don't concentrate
5. **Respect the steamroller** - it's real

**Many succeed with carry trades:**

- Professional vol sellers
- Market makers
- Disciplined hedge funds
- Systematic strategies

**Many fail spectacularly:**

- Over-leveraged retail
- No stop losses
- Hubris
- Greed

**The difference? Risk management.**

**If you take away one thing:** 
> "Positive theta is attractive, but negative gamma is dangerous. The only way to survive long-term is obsessive risk management. Size small, use stops, diversify, and never ever bet the farm. The steamroller is always coming - you just don't know when." 🎯⚠️

---

## Where This Fits in

**This is a CROSS-CUTTING theme that ties together:**

- Straddles (theta-negative if long, theta-positive if short)
- Gamma Scalping (pay theta, earn gamma)
- Calendar Spreads (theta differential = carry)
- All strategies have a theta component

**Suggested placement:**

- After Calendar Spreads (Chapter 6)
- Or as synthesis chapter at the end
- Shows the common thread: theta is everywhere!

**This completes the "dimensions of trading":**

1. Level (gamma, vega, variance)
2. Shape (smile/skew)
3. Time (calendars, **theta/carry**)
4. Assets (dispersion)
5. Factors (convertibles)

**Now students understand ALL aspects of the volatility surface!** ⏰💰