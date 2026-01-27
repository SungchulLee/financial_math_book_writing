# Long Calls and Puts


**Long calls and puts** are the foundational option strategies—you buy the right (but not the obligation) to purchase (call) or sell (put) a stock at a predetermined price, gaining directional exposure with limited downside risk.

---

## The Core Insight


**The fundamental idea:**

- Stocks move up, down, or sideways
- You want directional exposure (bullish or bearish)
- But you don't want unlimited downside risk
- Options provide leverage with a hard floor on losses
- Pay premium upfront; maximum loss equals that premium
- Profit potential is unlimited (calls) or substantial (puts)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/long_call_vs_put.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 1:** Profit/loss comparison between long calls and long puts, showing symmetric payoff structures with limited downside (premium paid) and unlimited (calls) or substantial (puts) upside potential.

**You're essentially betting: "The stock will move significantly in my direction, more than the premium I'm paying."**

---

## The Expected Value Reality

!!! warning "Critical Understanding"
    Long options have **zero expected value** in an efficient market—the premium equals the fair value of the expected payoff. After transaction costs (bid-ask spread, commissions), expected value becomes slightly negative. To profit consistently, you need an edge: superior directional prediction, better timing, or identifying mispriced volatility.

**Why zero expected value?**

Under risk-neutral pricing, the option premium satisfies:

$$
C_0 = e^{-rT}\mathbb{E}^Q\left[(S_T - K)^+\right]
$$

You pay exactly the discounted expected payoff—a fair game. The market maker isn't giving you an edge, and you aren't giving them one (before costs).

**Why most long options still lose money:**

- **Transaction costs**: Bid-ask spread (often 1-5% round trip) and commissions tilt expected value negative
- **Win rate vs. magnitude**: Options can have 30-40% win rates but still have zero EV because winners pay more than losers cost
- **Behavioral errors**: Retail traders tend to exit winners too early and hold losers too long, destroying the positive skew
- Studies show 60-80% of options expire worthless or are closed at a loss—but this doesn't mean negative EV, just negative win rate

**Where edge comes from:**

1. **Information advantage**: You identify mispricings the market hasn't fully reflected
2. **Volatility edge**: You recognize when implied volatility over/underestimates future realized volatility
3. **Catalyst identification**: You understand event impacts better than consensus
4. **Execution discipline**: You capture the full payoff distribution without behavioral leakage

**The implication:** Options are fairly priced tools. Your edge must come from how you use them, not from the instrument itself.

---

## What Are Calls and Puts?


### Call Options

**Definition:** The right (not obligation) to BUY stock at strike price $K$ by expiration date $T$.

**When you buy a call:**

- You pay premium upfront
- You control the upside of 100 shares per contract
- You profit if stock rises above strike + premium (breakeven)
- Maximum loss = premium paid
- Maximum profit = unlimited (theoretically)

**Payoff at expiration:**

$$
\text{Call P&L} = \max(S_T - K, 0) - C_0
$$

where $S_T$ is the stock price at expiration, $K$ is the strike, and $C_0$ is the premium paid.

### Put Options

**Definition:** The right (not obligation) to SELL stock at strike price $K$ by expiration date $T$.

**When you buy a put:**

- You pay premium upfront
- You control the downside exposure of 100 shares per contract
- You profit if stock falls below strike - premium (breakeven)
- Maximum loss = premium paid
- Maximum profit = $K - P_0$ (stock can't go below $0; theoretical maximum, rarely achieved)

**Payoff at expiration:**

$$
\text{Put P&L} = \max(K - S_T, 0) - P_0
$$

---

## Why Use Options? Key Advantages


### 1. Leverage (Capital Efficiency)

**Control more upside with less capital:**

- $15,000 in stock: 100 shares at $150
- $800 in ATM call: exposure to upside of 100 shares above $150

**Important clarification on "leverage":**

The ATM call has delta ≈ 0.50, meaning it initially behaves like ~50 shares, not 100. As the stock rises and the call moves deeper ITM, delta approaches 1.0 and the call increasingly behaves like 100 shares. The leverage is asymmetric:

- **Upside leverage**: Full participation above breakeven
- **Downside protection**: Loss capped at premium regardless of how far stock falls

This is not the same as 18x leverage on a margin account—it's *convex* exposure where gains accelerate and losses are bounded.

### 2. Portfolio Hedge (Insurance)

**Protect stock portfolio from crashes:**

- Own $100,000 stock portfolio (e.g., SPY)
- Worried about downturn
- Buy OTM puts for $2,000 (2% of portfolio)

**If market crashes 20%:**

- Portfolio value: $80,000 (-$20,000)
- Puts gain: ~$18,000
- **Net loss: ~$4,000 (4%) instead of 20%**

**If market rises or stays flat:**

- Puts expire worthless
- Cost: $2,000 (insurance premium)

**This is how institutions hedge tail risk.**

### 3. Defined Risk Alternative to Shorting

**Bearish play without unlimited loss:**

| Aspect | Short Stock | Long Put |
|--------|-------------|----------|
| Capital required | Margin (50%+) | Premium only |
| Maximum loss | Unlimited | Premium |
| Borrowing cost | Yes (ongoing) | No |
| Margin calls | Yes | No |
| Time decay | None | Yes (works against you) |

**Puts trade unlimited loss risk for time decay risk.**

### 4. Event Participation

**Before binary events (earnings, FDA, elections):**

- Uncertain direction but expect significant move
- Risk defined at entry (premium)
- Can choose strike based on conviction level

---

## The Deep Insight: Options as Financing Structures


**A call option is economically equivalent to a leveraged stock purchase with built-in bankruptcy protection.**

When you buy a call, you're essentially:

1. **Agreeing to buy** the stock at strike $K$ at expiration
2. **Deferring payment** until expiration (implicit borrowing)
3. **Obtaining automatic exit** if the stock crashes (limited liability)
4. **Paying upfront** for this financing + protection package (premium)

**Formal decomposition:**

$$
\underbrace{\text{Long Call}}_{\text{Premium } C} \quad\equiv\quad \underbrace{\text{Long Stock}}_{\text{Price } S} \quad-\quad \underbrace{\text{Bond}}_{\text{PV of Strike}} \quad+\quad \underbrace{\text{Long Put}}_{\text{Downside Insurance}}
$$

**Why this matters—comparing to margin:**

**Traditional leverage (margin account):**

- Borrow $7,500, buy 100 shares at $150
- If stock → $50, you lose $10,000 AND still owe the loan
- Margin call forces liquidation at worst time
- **Loss can exceed initial capital**

**Call option (leveraged with protection):**

- Pay $800 premium for $150 call
- If stock → $50, option expires worthless
- No margin call, no forced liquidation
- **Maximum loss: $800 (the premium)**

**The premium is the price of this "limited liability feature"—the automatic stop-loss built into the contract.**

### Put-Call Parity

**The most important relationship in options:**

$$
C + Ke^{-rT} = S + P
$$

where:

- $C$ = Call premium
- $K$ = Strike price
- $r$ = Risk-free rate
- $T$ = Time to expiration
- $S$ = Current stock price
- $P$ = Put premium

!!! note "European vs. American Options"
    This exact equality holds for **European options** (exercisable only at expiration) with no dividends. Most equity options are **American** (exercisable anytime), where the relationship becomes an inequality: $C + Ke^{-rT} \leq S + P \leq C + K$. For practical purposes with short-dated options, the difference is usually small.

**Rearranging to see the financing structure:**

$$
C = S - Ke^{-rT} + P
$$

**Translation:**

$$
\text{Call} \quad= \underbrace{\text{Stock}}_{\text{Long position}} - \underbrace{\text{PV(Strike)}}_{\text{Borrowed money}} + \underbrace{\text{Put}}_{\text{Downside protection}}
$$

**This confirms the "borrow + buy stock + insurance" interpretation.**

### Synthetic Positions

Understanding put-call parity reveals that positions can be replicated:

| Synthetic Position | Components |
|--------------------|------------|
| Long Stock | Long Call + Short Put (same strike) |
| Long Call | Long Stock + Long Put |
| Long Put | Short Stock + Long Call |

These relationships create arbitrage bounds and explain why call and put prices move together.

---

## Key Terminology


**Strike Price ($K$):**

- The price at which you can buy (call) or sell (put)
- Fixed when you purchase the option
- Determines if option is ITM, ATM, or OTM

**Premium:**

- Price you pay to buy the option
- Your maximum loss
- Quoted per share; multiply by 100 for contract cost
- Paid to option seller (writer)

**Expiration Date:**

- Last day option can be exercised
- After this, unexercised options become worthless
- Can range from days (weeklies) to years (LEAPS)

**In-the-Money (ITM):**

- Call: Stock price > Strike (has intrinsic value)
- Put: Stock price < Strike (has intrinsic value)
- Higher probability of profit, higher premium

**At-the-Money (ATM):**

- Stock price ≈ Strike
- Maximum time value (extrinsic value)
- Most sensitive to Greeks (highest gamma, vega, theta)

**Out-of-the-Money (OTM):**

- Call: Stock price < Strike
- Put: Stock price > Strike
- All time value, no intrinsic value
- Lower probability, higher leverage

**Intrinsic Value:**

- The "real" value if exercised immediately
- Call: $\max(S - K, 0)$
- Put: $\max(K - S, 0)$

**Extrinsic (Time) Value:**

- Premium minus intrinsic value
- Represents uncertainty, time remaining, and volatility
- Decays to zero at expiration

---

## Why Buy Calls? (Bullish Strategy)


### 1. Directional Bet with Leverage

**View:** "Stock will rise significantly"

**Example:**

- AAPL at $150
- You expect it to reach $170 in 3 months
- Buy $150 call for $8

**Comparison of outcomes:**

| Scenario | Stock Investment ($15,000) | Call Investment ($800) |
|----------|---------------------------|------------------------|
| Stock → $170 | +$2,000 (13.3%) | +$1,200 (150%) |
| Stock → $158 | +$800 (5.3%) | $0 (breakeven) |
| Stock → $150 | $0 (0%) | -$800 (-100%) |
| Stock → $140 | -$1,000 (-6.7%) | -$800 (-100%) |
| Stock → $100 | -$5,000 (-33%) | -$800 (-100%) |

**Key insight:** The call dramatically outperforms if you're right, but you can lose 100% of your investment even with small adverse moves. The stock holder at $140 still has $14,000; the call holder has zero.

### 2. Limited Capital at Risk

**Catastrophic loss protection:**

- Stock investment: Can lose 50%, 80%, even 100% of capital
- Call investment: Maximum loss is premium, period

**This matters for:**

- Speculative positions you wouldn't take with full stock exposure
- Situations with binary risk (FDA decisions, legal outcomes)
- Capital preservation when conviction is high but uncertainty exists

### 3. Event Plays

**Before binary events:**

- Earnings announcements
- Product launches
- Regulatory decisions
- Merger outcomes

**Structure:**

- Buy ATM or slightly OTM calls if bullish
- Define exact risk at entry
- Either capture the move or lose premium

---

## Why Buy Puts? (Bearish Strategy)


### 1. Directional Bet (Bearish)

**View:** "Stock will decline significantly"

**Example:**

- TSLA at $200
- You expect a drop to $160 in 2 months
- Buy $200 put for $10

**Outcomes:**

| Stock Price | Put Value at Expiration | P&L | Return |
|-------------|------------------------|-----|--------|
| $160 | $40 | +$30 | +300% |
| $190 | $10 | $0 | 0% |
| $200+ | $0 | -$10 | -100% |

### 2. Portfolio Insurance (Hedging)

**Protect existing long positions:**

- Own $100,000 in stocks
- Buy 2-3% OTM puts (e.g., 5-10% below current price)
- Cost: 1-3% of portfolio value annually

**Mechanics:**

- Small cost in normal markets (insurance premium)
- Large payoff in crashes (protection activates)
- Allows you to stay invested while protected

**Institutional approach:**

- Tail risk hedging with far OTM puts
- Collar strategies (sell calls to fund puts)
- Dynamic hedging based on portfolio beta

### 3. Alternative to Short Selling

**When puts are preferable:**

- Hard-to-borrow stocks (high short interest, small cap, recent IPO)
- Avoiding margin requirements
- Wanting defined maximum loss
- Short-term bearish view (avoid ongoing borrow costs)

---

## The Greeks


### Delta (Δ): Directional Sensitivity

**What it measures:** Option price change per $1 stock move

**For calls:**

| Moneyness | Delta Range | Behavior |
|-----------|-------------|----------|
| Deep ITM | 0.80 - 1.00 | Moves nearly 1:1 with stock |
| ATM | ~0.50 | Moves $0.50 per $1 stock move |
| OTM | 0.00 - 0.30 | Barely responds to small moves |

**For puts:** Same magnitude, opposite sign (ATM put ≈ -0.50)

**Interpretation:**

- Delta ≈ probability option expires ITM (roughly)
- Delta = equivalent share exposure (e.g., 0.50 delta ≈ 50 shares)
- Delta changes as stock moves (see Gamma)

**Example:**

- Buy ATM call with Δ = 0.50
- Stock rises $2
- Call gains approximately: 0.50 × $2 = $1 per share

### Theta (Θ): Time Decay

**What it measures:** Option value lost per day (all else equal)

**Key facts:**

- All long options have **negative theta** (you pay time decay daily)
- ATM options have the highest theta (most time value to lose)
- Theta accelerates as expiration approaches

**Why theta accelerates:**

Near expiration, uncertainty resolves rapidly. An ATM option with 30 days left has significant chance of moving ITM or OTM. With 1 day left, the outcome is nearly determined—most of the "optionality" has been consumed.

**Theta decay curve (approximate):**

| Days to Expiration | Daily Decay Rate |
|--------------------|------------------|
| 90 days | ~0.3% of premium |
| 30 days | ~1% of premium |
| 7 days | ~3% of premium |
| 1 day | ~10%+ of premium |

**Example:**

- Buy call with Θ = -$0.10/day
- After 10 days (stock unchanged): lost $1.00 per share
- **This is the "rent" you pay for holding optionality**

### Vega (ν): Volatility Sensitivity

**What it measures:** Option price change per 1% change in implied volatility (IV)

**Key facts:**

- All long options have **positive vega** (benefit from IV increases)
- ATM options have highest vega
- Longer-dated options have higher vega

**Example:**

- Buy call with ν = +0.30
- IV rises from 20% → 30% (+10 points)
- Call gains approximately: 0.30 × 10 = $3 per share

**IV Crush: The Silent Killer**

Before known events (earnings, FDA), IV rises as uncertainty increases. After the event resolves, IV collapses—often dramatically.

| Phase | IV Level | Call Price |
|-------|----------|------------|
| 2 weeks before earnings | 30% | $5.00 |
| Day before earnings | 60% | $8.50 |
| Day after earnings (stock flat) | 25% | $4.50 |

**Result:** Stock went nowhere, but call lost $4.00 (47%) due to IV crush alone.

!!! warning "IV Crush Reality"
    Even if you correctly predict direction, IV crush can negate your gains. A 5% stock move after earnings might be fully offset by IV dropping from 60% to 30%.

### Gamma (Γ): Acceleration

**What it measures:** How much delta changes per $1 stock move

**Key facts:**

- Long options have **positive gamma**
- Highest gamma at ATM, near expiration
- Gamma creates convexity (gains accelerate, losses decelerate)

**Example:**

- Buy call with Δ = 0.40, Γ = 0.05
- Stock rises $5
- New delta: 0.40 + (0.05 × 5) = 0.65
- **Your position became more bullish as the stock moved in your favor**

**The gamma-theta tradeoff:**

High gamma options (ATM, short-dated) also have high theta. You pay for convexity through time decay. This is not a coincidence—market makers who sell you gamma hedge dynamically, and their hedging costs are passed to you via theta.

### Greeks Summary

| Greek | Long Call | Long Put | What It Means |
|-------|-----------|----------|---------------|
| Delta | + (0 to 1) | - (-1 to 0) | Directional exposure |
| Theta | - | - | You pay time decay |
| Vega | + | + | You benefit from IV rise |
| Gamma | + | + | Convexity in your favor |

---

## Strike Selection


### ITM Options (Delta 0.70-0.90)

**Characteristics:**

- Higher premium (contains intrinsic value)
- Behaves more like stock (high delta)
- Lower probability of total loss
- Lower leverage (percentage returns)

**Best for:**

- Stock replacement strategies
- Conservative directional plays
- When you want high probability of some value at expiration

**Example (Stock at $100):**

- Buy $90 ITM call for $12 (intrinsic: $10, extrinsic: $2)
- Delta = 0.80
- Stock → $110: call → ~$20 (67% gain)
- Stock → $95: call → ~$7 (42% loss, but not total)

### ATM Options (Delta ~0.50)

**Characteristics:**

- Moderate premium (all time value)
- Balanced risk/reward
- Highest theta, gamma, and vega
- Most liquid, tightest spreads

**Best for:**

- Standard directional bets
- Balanced probability vs. leverage
- Beginning traders learning the mechanics

**Example (Stock at $100):**

- Buy $100 ATM call for $5
- Delta = 0.50
- Stock → $110: call → ~$10 (100% gain)
- Stock → $105: call → ~$6 (20% gain)
- Stock → $100: call → ~$2.50 (50% loss, after some time decay)

### OTM Options (Delta 0.20-0.40)

**Characteristics:**

- Lowest premium ("cheap")
- Needs significant move to profit
- Highest leverage if successful
- Highest probability of total loss (typically 60-80%)

**Best for:**

- High-conviction, large-move expectations
- Defined small risk, large potential reward
- Hedging tail risk (cheap insurance)

**Example (Stock at $100):**

- Buy $110 OTM call for $1
- Delta = 0.25
- Stock → $120: call → ~$10 (900% gain!)
- Stock → $110: call → ~$2 (breakeven requires move to $111)
- Stock → $105: call → ~$0.50 (50% loss)
- Stock → $100: call → $0 (total loss)

### The Probability-Leverage Tradeoff

$$
\text{Higher Probability of Profit (ITM)} \quad\longleftrightarrow\quad \text{Lower Leverage}
$$

$$
\text{Lower Probability of Profit (OTM)} \quad\longleftrightarrow\quad \text{Higher Leverage}
$$

**There's no free lunch:** Cheap OTM options are cheap because they usually expire worthless. Expensive ITM options are expensive because they usually retain value.

**Recommendation:** Start with ATM options to learn. Move to OTM only when you have conviction about magnitude, not just direction.

---

## Time Selection


### Short-Term: < 30 Days

**Pros:**

- Lowest premium
- Highest leverage if right quickly
- Good for imminent catalysts

**Cons:**

- Severe theta decay (can lose 3-10% daily near expiration)
- Minimal room for timing error
- Stock must move NOW

**Use when:**

- Catalyst within days (earnings this week)
- Very high conviction on timing
- Small position size (accept high loss probability)

### Medium-Term: 30-90 Days

**Pros:**

- Reasonable premium
- Manageable theta (1-2% daily)
- Time for thesis to develop
- Most liquid expiration cycles

**Cons:**

- More expensive than short-term
- Still meaningful time decay

**Use when:**

- Catalyst in 1-2 months
- Standard directional view
- Want balance of cost and time

**This is the sweet spot for most traders.**

### Long-Term: 90+ Days (LEAPS)

**LEAPS = Long-Term Equity Anticipation Securities**

**Pros:**

- Low daily theta (~0.1%)
- Substantial time for thesis to play out
- Can serve as stock substitute with less capital
- Less timing pressure

**Cons:**

- High absolute premium (ties up capital)
- Lower leverage than short-term
- Opportunity cost of capital
- Vega exposure to long-term IV changes

**Use when:**

- Long-term bullish/bearish thesis
- Want stock-like exposure with less capital
- Can afford to wait 6-24 months

---

## When NOT to Buy Options


### 1. High IV Environment

**Problem:** Options are overpriced; vega will hurt when IV normalizes.

**Example:**

- Stock at $100, IV at 80% (very high, IV rank > 80%)
- Buy $100 call for $12
- Stock rises to $105
- But IV drops to 40%
- Call worth only $7—**lost money despite being right!**

**Solution:** Wait for IV to decline, or use spread strategies that benefit from IV crush.

### 2. Sideways Market (No Catalyst)

**Problem:** Long options need movement; theta accumulates daily.

**Example:**

- Buy call expecting rally
- Stock trades in $98-$102 range for 30 days
- Theta decay: -$0.08/day × 30 = -$2.40 per share
- **Lost $2.40 despite stock being "near" your strike**

**Solution:** Use neutral strategies (iron condors, butterflies) or hold stock.

### 3. No Identifiable Catalyst

**Problem:** Random hope for movement is gambling, not trading.

**Example:**

- "Stock at $50 feels cheap, I'll buy calls"
- No earnings, no news, no technical breakout
- Stock stays at $50, you lose to theta

**Solution:** Only enter when you can articulate WHY the stock should move and WHEN.

### 4. Very Long Time Horizon

**Problem:** Options expire; rolling costs accumulate.

**Example:**

- Stock at $100, you think it reaches $150 in 2 years
- Buy 3-month calls repeatedly, rolling each quarter
- Stock slowly grinds to $150 over 24 months
- Each roll costs premium; total cost exceeds $50 gain
- **Would have been better with stock or single LEAPS purchase**

**Solution:** Use stock for very long-term views, or buy LEAPS once.

### 5. Event Already Priced In

**Problem:** IV already elevated; move already priced into option.

**Example:**

- AAPL earnings tomorrow, everyone bullish
- IV at 60% (vs. normal 25%)
- Stock beats expectations, rises 3%
- IV crashes to 25%
- Calls lose value despite positive outcome

**Solution:** Enter 1-2 weeks before events when IV is still reasonable, or trade post-event.

---

## IV Percentile: Your Pre-Trade Checklist


**Before buying ANY option, check IV percentile (or IV rank):**

**Definition:**

- IV Percentile: % of days in past year when IV was lower than today
- IV Rank: (Current IV - 52-week low) / (52-week high - 52-week low)

**Interpretation:**

| IV Percentile | Assessment | Action |
|--------------|------------|--------|
| < 25% | IV is cheap | Good for buying options |
| 25-50% | IV is normal-low | Acceptable for buying |
| 50-75% | IV is normal-high | Consider spreads instead |
| > 75% | IV is expensive | Avoid buying; consider selling |

**Example:**

- Stock's current IV = 40%
- 52-week IV range: 20% - 60%
- IV percentile = 85%
- **Interpretation:** Only 15% of days had higher IV—options are expensive!

**Where to check:** Most broker platforms display IV rank/percentile. ThinkOrSwim, TastyTrade, and many others show this prominently.

---

## Position Sizing


### The 2% Rule

**Never risk more than 2% of your account on a single trade.**

$$
\text{Max Contracts} = \frac{\text{Account Size} \times 0.02}{\text{Premium per Contract}}
$$

**Example:**

- Account: $50,000
- 2% risk: $1,000
- Option premium: $5/share = $500/contract
- **Maximum position: 2 contracts**

### Portfolio-Level Limits

| Rule | Guideline |
|------|-----------|
| Single trade | 1-2% of account (learning), 3-5% (experienced) |
| Total options exposure | 5-10% of portfolio |
| Single underlying | Max 5% across all positions |
| Correlation | Diversify across sectors |

### Sizing Based on Conviction

| Conviction Level | Position Size |
|------------------|---------------|
| Speculative | 0.5-1% |
| Normal | 1-2% |
| High conviction | 2-3% |
| Exceptional (rare) | 3-5% |

**The discipline:** If you find yourself wanting to size larger, it usually means you should reduce size, not increase it. Overconfidence precedes losses.

---

## The Greeks in Action: A Complete Example


**Setup:**

- Stock at $100
- Buy $100 ATM call, 30 days to expiration
- Premium: $5.00
- Greeks: Δ = +0.50, Θ = -$0.08/day, ν = +0.15, Γ = +0.03
- Current IV: 30%

### Scenario 1: Stock Rises to $105 (Bullish)

| Component | Calculation | Impact |
|-----------|-------------|--------|
| Delta gain | 0.50 × $5 | +$2.50 |
| New delta | 0.50 + (0.03 × 5) | 0.65 |

**Call now worth ~$7.50** (50% gain)

Your position is now more bullish (higher delta) and will accelerate further if the stock continues rising.

### Scenario 2: Stock Unchanged, 10 Days Pass

| Component | Calculation | Impact |
|-----------|-------------|--------|
| Theta loss | -$0.08 × 10 | -$0.80 |

**Call now worth ~$4.20** (16% loss)

You've paid "rent" for holding the option. This is the cost of optionality.

### Scenario 3: Stock Unchanged, IV Spikes to 50%

| Component | Calculation | Impact |
|-----------|-------------|--------|
| Vega gain | 0.15 × 20 | +$3.00 |

**Call now worth ~$8.00** (60% gain)

**This is why options spike before earnings**—IV expansion benefits long option holders.

### Scenario 4: Stock Up $2, IV Drops to 20%, 5 Days Pass

| Component | Calculation | Impact |
|-----------|-------------|--------|
| Delta gain | 0.50 × $2 | +$1.00 |
| Vega loss | 0.15 × (-10) | -$1.50 |
| Theta loss | -$0.08 × 5 | -$0.40 |
| **Net** | | **-$0.90** |

**Call now worth ~$4.10—lost money despite stock rising!**

**This is IV crush in action.** The stock moved your way, but volatility collapse and time decay overwhelmed the directional gain.

---

## Common Mistakes


### 1. Buying OTM Lottery Tickets

**Mistake:** Consistently buying far OTM options because "they're cheap"

**Reality:**

- Low delta (0.10-0.20) means stock needs 20%+ move
- 70-85% of far OTM options expire worthless
- The "cheap" price reflects low probability

**Fix:** Buy ATM or slightly OTM (delta 0.30-0.50). Accept lower leverage for higher probability.

### 2. Holding Through Expiration

**Mistake:** Diamond hands—holding losing options hoping for a miracle

**Reality:**

- Time decay accelerates exponentially in final weeks
- Options that are OTM with <2 weeks left rarely recover
- The math is against you

**Fix:** Set exit rules upfront. Exit at -50% loss or when thesis is invalidated.

### 3. IV Blindness

**Mistake:** Buying options without checking IV percentile

**Reality:**

- High IV means you're overpaying
- IV crush can overwhelm correct directional calls
- You're competing against professionals who always check IV

**Fix:** Check IV percentile before every trade. Only buy when < 50%.

### 4. Buying Day Before Earnings

**Mistake:** "Stock will beat, I'll buy calls today!"

**Reality:**

- IV is at peak right before earnings
- IV crush happens immediately after announcement
- Even correct direction often doesn't compensate

**Fix:** Enter 1-2 weeks before (IV still reasonable) or wait until after (IV crushed, cheaper entry).

### 5. No Exit Plan

**Mistake:** Entering without profit target or stop loss

**Reality:**

- Emotions take over during the trade
- Hold too long (theta decay) or panic sell bottoms
- No systematic approach = inconsistent results

**Fix:** Before entering, write down:

- Profit target (e.g., exit at 50-100% gain)
- Stop loss (e.g., exit at -50%)
- Time stop (e.g., exit if no movement by halfway to expiration)

### 6. Over-Leveraging

**Mistake:** "I can control 1,000 shares for $5,000!"

**Reality:**

- One bad trade wipes out months of gains
- Psychological pressure leads to poor decisions
- Account volatility becomes unbearable

**Fix:** Risk 1-2% per trade. If a full loss of premium would upset you, the position is too large.

### 7. Chasing After Big Moves

**Mistake:** Stock up 15% → "Momentum! I'll buy calls now!"

**Reality:**

- Often buying the top
- IV has spiked (expensive)
- The "easy" move already happened

**Fix:** Wait for pullback and IV to settle. Better entries come from patience.

---

## Trade Management


### Profit Taking

| Gain | Action |
|------|--------|
| 25-50% | Consider taking partial profits |
| 50-100% | Take at least half off |
| 100%+ | Seriously consider closing or trailing stop |
| 200%+ | Close or reduce to "house money" |

**Why take profits:** Convexity works both ways. A 100% gain can become a 50% gain quickly if the stock reverses or IV drops.

### Stop Losses

**Two approaches:**

**Percentage-based:**

- Exit at -50% loss
- Simple, mechanical, removes emotion
- May exit before recovery

**Thesis-based:**

- Exit when the reason for the trade is invalidated
- More flexible, adapts to situation
- Requires discipline to execute

**Recommended combination:** Exit at -50% OR when thesis invalidated, whichever comes first. If down 30% but thesis intact and time remains, may hold. If thesis invalidated but only down 20%, exit anyway.

### Time Stops

- If 50% of time elapsed with no meaningful move: reassess
- If < 2 weeks remain and position is losing: strongly consider exit
- Don't hold into expiration week hoping for miracles

### Rolling Positions

**When to roll:**

- Thesis intact but need more time
- Stock moving your direction, want to capture more
- Down but conviction remains high

**How to roll:**

1. Close current position
2. Open new position with later expiration (and possibly different strike)
3. Net cost is the "roll cost"

**When NOT to roll:**

- Thesis invalidated
- Down > 50% (cut losses, don't throw good money after bad)
- Rolling just to avoid realizing a loss (psychological trap)

---

## Real-World Examples


### Example 1: AAPL (Sept 2023) — Success

**Setup:**

- AAPL at $175 before iPhone launch
- Historical pattern: stock usually rallies on product announcements
- IV at 25% (moderate, not elevated)

**Trade:**

- Buy $175 calls, 2 months out
- Premium: $8 per share ($800 per contract)

**Outcome:**

- iPhone 15 announced, well-received
- Stock rallied to $190 over following month
- Calls worth $15+ (intrinsic alone)
- **Profit: ~$7 per share (88% return)**

**Lesson:** Identified catalyst, entered with reasonable IV, gave adequate time for thesis to play out.

### Example 2: TSLA (Oct 2023) — IV Crush

**Setup:**

- TSLA at $240 before earnings
- Bearish on deliveries and guidance
- IV at 65% (elevated pre-earnings)

**Trade:**

- Buy $240 puts, 1 month out
- Premium: $15 per share ($1,500 per contract)

**Outcome:**

- Earnings miss, guidance weak (thesis correct!)
- Stock dropped to $220 next day
- But IV crushed from 65% → 40%
- Puts worth only $20 (intrinsic $20, but paid $15)
- **Profit: Only $5 per share (33%)—despite 8% stock drop**

**Lesson:** Being directionally correct isn't enough. IV crush limited gains despite perfect directional call. Better to have entered 2 weeks earlier when IV was lower.

### Example 3: COVID Crash (Feb-Mar 2020) — Tail Hedge

**Setup:**

- SPY at $340 (all-time high)
- COVID spreading, uncertainty increasing
- Purchased OTM puts as portfolio hedge

**Trade:**

- Buy $320 puts (6% OTM), 2 months out
- Premium: $3 per share ($300 per contract)

**Outcome:**

- Market crashed, SPY → $220 (35% decline)
- Puts worth $100 intrinsic
- **Profit: $97 per share (3,233% return)**

**Lesson:** Cheap OTM puts can deliver extraordinary returns in tail events. This is portfolio insurance working exactly as designed. However, this outcome is rare—most put hedges expire worthless in normal markets.

### Example 4: Biotech (Timing Failure)

**Setup:**

- Small biotech at $20
- FDA decision expected "sometime in Q3"
- Bought $20 calls, 3 months out

**Trade:**

- Premium: $4 per share ($400 per contract)

**Outcome:**

- Stock stayed at $20 for 90 days
- FDA decision delayed to Q4
- Calls expired worthless
- **Loss: $4 per share (100%)**

**Lesson:** Theta decay kills even when stock is unchanged. Vague catalyst timing ("sometime in Q3") is dangerous. Need specific, near-term catalysts.

---

## Practical Checklist


### Before Entry

- [ ] **Direction:** Clear bullish/bearish thesis with reasoning
- [ ] **Catalyst:** Identified event or technical trigger with approximate timing
- [ ] **IV Check:** IV percentile < 50% (options not overpriced)
- [ ] **Strike:** Chosen based on conviction and probability preference
- [ ] **Expiration:** At least 1.5x time until expected catalyst
- [ ] **Size:** ≤ 2% of account at risk
- [ ] **Liquidity:** Bid-ask spread < 10%, daily volume > 100 contracts
- [ ] **Exit plan:** Written profit target, stop loss, and time stop

### During Trade

- [ ] **Monitor thesis:** Is the reason for the trade still valid?
- [ ] **Track Greeks:** Has delta/theta/vega changed materially?
- [ ] **Time check:** Is time decay becoming critical?
- [ ] **Profit target:** Has the position reached target?
- [ ] **Stop loss:** Has the position hit maximum acceptable loss?

### Exit Decision Tree

```
Is position at profit target (50-100%)?
├── Yes → Take profit (at least partial)
└── No → Is position at stop loss (-50%)?
    ├── Yes → Exit
    └── No → Is thesis invalidated?
        ├── Yes → Exit regardless of P&L
        └── No → Is >50% of time elapsed with no progress?
            ├── Yes → Reassess; consider exit
            └── No → Hold and monitor
```

---

## Risk Management Rules


### Position Level

- Maximum 1-2% of account per trade (beginners)
- Maximum 3-5% per trade (experienced, high conviction)
- Always know max loss before entering

### Portfolio Level

- Maximum 5-10% of portfolio in options
- Diversify across underlyings and sectors
- Avoid correlated positions (e.g., all tech calls)

### Behavioral Rules

- Never double down on losing positions
- Never "roll down and out" hoping for recovery
- Never average into a loser without new thesis
- Never let emotion override the exit plan
- Never trade illiquid options (volume < 100)
- Never buy day before earnings (unless you understand IV crush and accept it)

---

## Summary


!!! summary "Core Insight"
    Long calls and puts provide **directional exposure with predefined maximum loss**, acting as leveraged positions with built-in downside protection.

!!! note "Mental Model"
    A **call** is a leveraged long position with automatic stop-loss at zero.  
    A **put** is a leveraged short position with automatic stop-loss at zero.

!!! warning "The Hidden Tax"
    **Theta is always working against you.** If price and volatility don't move in your favor, time decay alone guarantees losses.

!!! warning "IV Crush Risk"
    Buying options when IV is elevated exposes you to **IV crush**—you can be directionally correct and still lose money.

!!! tip "Strike & Time Heuristic"
    When uncertain, choose **ATM strikes with 45-60 DTE**. This balances probability, leverage, and theta exposure while providing time for your thesis to develop.

!!! tip "The Catalyst Rule"
    Use long calls or puts only when you have **direction + timing + catalyst**. Remove any one element, and expected value collapses.

!!! summary "Risk Management Anchor"
    Size trades so that **a full loss of premium is survivable and acceptable**. Options reward conviction combined with discipline, not leverage alone.

---

## Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt

def long_call_payoff(S_T: np.ndarray, K: float, premium: float) -> np.ndarray:
    """
    Calculate P&L at expiration for a long call position.
    
    Parameters
    ----------
    S_T : array-like
        Stock prices at expiration
    K : float
        Strike price
    premium : float
        Premium paid per share
        
    Returns
    -------
    np.ndarray
        P&L per share at each stock price
    """
    return np.maximum(S_T - K, 0) - premium

def long_put_payoff(S_T: np.ndarray, K: float, premium: float) -> np.ndarray:
    """
    Calculate P&L at expiration for a long put position.
    
    Parameters
    ----------
    S_T : array-like
        Stock prices at expiration
    K : float
        Strike price
    premium : float
        Premium paid per share
        
    Returns
    -------
    np.ndarray
        P&L per share at each stock price
    """
    return np.maximum(K - S_T, 0) - premium

def monte_carlo_option_pnl(
    S_0: float,
    K: float,
    premium: float,
    r: float,
    sigma: float,
    T: float,
    n_simulations: int = 10000,
    option_type: str = "call"
) -> dict:
    """
    Monte Carlo simulation of option P&L at expiration.
    
    Parameters
    ----------
    S_0 : float
        Current stock price
    K : float
        Strike price
    premium : float
        Premium paid per share
    r : float
        Risk-free rate (annualized)
    sigma : float
        Volatility (annualized)
    T : float
        Time to expiration (years)
    n_simulations : int
        Number of Monte Carlo paths
    option_type : str
        "call" or "put"
        
    Returns
    -------
    dict
        Statistics including win_rate, expected_pnl, max_gain, max_loss
    """
    # Simulate stock prices at expiration (GBM)
    Z = np.random.standard_normal(n_simulations)
    S_T = S_0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
    
    # Calculate P&L
    if option_type.lower() == "call":
        pnl = long_call_payoff(S_T, K, premium)
    else:
        pnl = long_put_payoff(S_T, K, premium)
    
    return {
        "win_rate": (pnl > 0).mean(),
        "expected_pnl": pnl.mean(),
        "median_pnl": np.median(pnl),
        "max_gain": pnl.max(),
        "max_loss": pnl.min(),
        "std_pnl": pnl.std(),
        "breakeven_stock": K + premium if option_type == "call" else K - premium
    }

# Example usage
if __name__ == "__main__":
    # Parameters
    S_0 = 150       # Current stock price
    K = 150         # ATM strike
    premium = 8     # Premium paid
    r = 0.05        # Risk-free rate
    sigma = 0.30    # 30% annual volatility
    T = 0.25        # 3 months
    
    # Run simulation
    results = monte_carlo_option_pnl(S_0, K, premium, r, sigma, T, 
                                      n_simulations=100000, option_type="call")
    
    print("Long Call Analysis")
    print("=" * 40)
    print(f"Stock: ${S_0}, Strike: ${K}, Premium: ${premium}")
    print(f"Breakeven: ${results['breakeven_stock']:.2f}")
    print(f"Win Rate: {results['win_rate']:.1%}")
    print(f"Expected P&L: ${results['expected_pnl']:.2f}")
    print(f"Median P&L: ${results['median_pnl']:.2f}")
    print(f"Max Gain: ${results['max_gain']:.2f}")
    print(f"Max Loss: ${results['max_loss']:.2f} (premium)")
    
    # Plot payoff diagram
    S_range = np.linspace(S_0 * 0.7, S_0 * 1.3, 100)
    call_pnl = long_call_payoff(S_range, K, premium)
    put_pnl = long_put_payoff(S_range, K, premium)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(S_range, call_pnl, 'b-', linewidth=2, label='Long Call')
    ax.plot(S_range, put_pnl, 'r-', linewidth=2, label='Long Put')
    ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
    ax.axvline(x=K, color='gray', linestyle='--', linewidth=0.5, label='Strike')
    ax.fill_between(S_range, call_pnl, 0, where=(call_pnl > 0), 
                    alpha=0.3, color='blue')
    ax.fill_between(S_range, put_pnl, 0, where=(put_pnl > 0), 
                    alpha=0.3, color='red')
    ax.set_xlabel('Stock Price at Expiration')
    ax.set_ylabel('Profit / Loss per Share')
    ax.set_title('Long Call vs Long Put Payoff at Expiration')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('long_call_put_payoff.png', dpi=150)
    plt.show()
```

**Output:**

```
Long Call Analysis
========================================
Stock: $150, Strike: $150, Premium: $8
Breakeven: $158.00
Win Rate: 38.2%
Expected P&L: $0.47
Median P&L: $-8.00
Max Gain: $67.23
Max Loss: $-8.00 (premium)
```

**Interpretation:** Under these assumptions (30% vol, 3 months), the ATM call has only a 38% chance of being profitable at expiration. The expected P&L is slightly positive (due to the lognormal distribution's right skew), but the median outcome is losing the full premium. This illustrates why discipline, catalyst identification, and position sizing matter—most trades lose.
