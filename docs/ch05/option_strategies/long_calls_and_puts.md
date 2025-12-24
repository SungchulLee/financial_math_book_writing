# Long Calls and Puts

**Long calls and puts** are the simplest option strategies where you buy the right (but not the obligation) to purchase (call) or sell (put) a stock at a predetermined price, giving you directional exposure with limited downside risk.

---

## The Core Insight

**The fundamental idea:**
- Stocks can go up or down (or sideways)
- You want directional exposure (bullish or bearish)
- But don't want unlimited downside risk
- Options give you leverage with limited loss
- Pay premium upfront, max loss is that premium
- Profit can be unlimited (calls) or substantial (puts)

**The key equation:**
$$
\text{Max Loss} = \text{Premium Paid} \quad (\text{limited, known upfront})
$$
$$
\text{Max Profit} = \text{Unlimited (call)} \text{ or } \text{Strike - Premium (put)}
$$

**You're essentially betting: "The stock will move significantly in my direction, more than the premium I'm paying."**

---

## What Are Calls and Puts?

**Before trading options, understand what you're buying:**

### Call Options

**Definition:** The right (not obligation) to BUY stock at strike price $K$ by expiration date $T$.

**When you buy a call:**
- You pay premium upfront
- You control 100 shares per contract
- You profit if stock goes UP above strike + premium
- Max loss = premium paid
- Max profit = unlimited

**Example:**
- Stock at $100
- Buy $100 call for $5
- You now have the RIGHT to buy 100 shares at $100 anytime before expiration
- Cost: $5 × 100 = $500

**At expiration:**
- Stock at $110 → Exercise, buy at $100, sell at $110 → Profit $5/share (after premium)
- Stock at $95 → Don't exercise, lose $5 premium

**Payoff diagram:**
```
Profit
   ↑
   |        /
   |       /
   |      /
───┼─────/────────→ Stock Price
  -5    /105  110
       /
      /
   Strike=$100
```

### Put Options

**Definition:** The right (not obligation) to SELL stock at strike price $K$ by expiration date $T$.

**When you buy a put:**
- You pay premium upfront
- You control 100 shares per contract
- You profit if stock goes DOWN below strike - premium
- Max loss = premium paid
- Max profit = strike - premium (stock can't go below $0)

**Example:**
- Stock at $100
- Buy $100 put for $5
- You now have the RIGHT to sell 100 shares at $100 anytime before expiration
- Cost: $5 × 100 = $500

**At expiration:**
- Stock at $90 → Exercise, buy at $90, sell at $100 → Profit $5/share (after premium)
- Stock at $105 → Don't exercise, lose $5 premium

**Payoff diagram:**
```
Profit
   ↑
   |\
   | \
   |  \
───┼───\────────→ Stock Price
  -5    \
    95   \100
      Strike
```

---

## Key Terminology

**Strike Price ($K$):**
- The price at which you can buy (call) or sell (put)
- Fixed at purchase
- Determines if option is ITM, ATM, or OTM

**Premium:**
- Price you pay to buy the option
- Your max loss
- Paid upfront
- Goes to option seller

**Expiration Date:**
- Last day option is valid
- After this, option worthless if not exercised
- Can be days, weeks, months, or years away

**In-the-Money (ITM):**
- Call: Stock price > Strike
- Put: Stock price < Strike
- Has intrinsic value

**At-the-Money (ATM):**
- Stock price ≈ Strike
- Maximum time value
- Most sensitive to Greeks

**Out-of-the-Money (OTM):**
- Call: Stock price < Strike
- Put: Stock price > Strike
- All time value, no intrinsic value

---

## Why Buy Calls? (Bullish Strategy)

**Use cases for buying calls:**

### 1. Directional Bet (Bullish)

**View:** "Stock will go up significantly"

**Example:**
- AAPL at $150
- You think it'll hit $170 in 3 months
- Buy $150 call for $8

**Why call vs. stock:**
- Stock: Need $15,000 for 100 shares
- Call: Need $800 for 100-share exposure
- **Leverage: 19x less capital for same upside**

**If right (stock → $170):**
- Stock profit: $2,000 on $15,000 (13.3%)
- Call profit: $1,200 on $800 (150%)
- **Call outperforms dramatically**

**If wrong (stock → $140):**
- Stock loss: $1,000 (6.7%)
- Call loss: $800 (100%, but limited!)
- **Call loses more % but limited absolute loss**

### 2. Leverage

**Control more shares with less capital:**
- $10,000 in stock: 67 shares at $150
- $10,000 in calls: 12 contracts = 1,200 shares of exposure!
- **18x leverage**

**Trade-off:**
- More upside potential
- But options expire (time decay)
- Need to be right on timing AND direction

### 3. Limited Downside

**Protect against catastrophic loss:**
- Stock can go to $0 → lose $15,000
- Call can go to $0 → lose $800 only
- **Predefined maximum loss**

### 4. Earnings/Event Play

**Before binary events:**
- Uncertain direction but expect big move
- Risk defined (premium)
- Can buy ATM or OTM calls if bullish lean

---

## Why Buy Puts? (Bearish Strategy)

**Use cases for buying puts:**

### 1. Directional Bet (Bearish)

**View:** "Stock will go down significantly"

**Example:**
- TSLA at $200
- You think it'll drop to $160 in 2 months
- Buy $200 put for $10

**If right (stock → $160):**
- Put value at expiration: $40 intrinsic
- Profit: $40 - $10 = $30/share
- Return: 300% on premium

**If wrong (stock → $220):**
- Put expires worthless
- Loss: $10/share (100%)
- Max loss capped

### 2. Portfolio Hedge (Insurance)

**Protect stock portfolio from crash:**
- Own $100,000 stock portfolio (SPY)
- Worried about downturn
- Buy OTM puts for $2,000 (2%)

**If market crashes 20%:**
- Portfolio value: $80,000 (-$20,000)
- Puts gain: ~$18,000
- **Net loss: $4,000 (4%) instead of 20%**

**This is how pros hedge!**

### 3. Cheaper Than Shorting

**Bearish play without margin:**
- Shorting requires margin account
- Unlimited loss potential
- Borrowing costs
- **Puts: No margin, defined risk, similar upside**

### 4. Cannot Short (Hard-to-Borrow)

**Some stocks hard to borrow:**
- Heavily shorted already
- Small cap with low float
- Recent IPO
- **Puts are the alternative**

---

## The Greeks (Simplified)

**How options behave - essential to understand:**

### Delta (Δ): Directional Exposure

**How much option price changes per $1 stock move:**

**Calls:**
- ATM call: Δ ≈ +0.50 (gains $0.50 per $1 stock rise)
- ITM call: Δ → +1.00 (moves almost 1:1 with stock)
- OTM call: Δ → 0 (barely moves)

**Puts:**
- ATM put: Δ ≈ -0.50 (gains $0.50 per $1 stock drop)
- ITM put: Δ → -1.00
- OTM put: Δ → 0

**Example:**
- Buy ATM call with Δ = 0.50
- Stock rises $2
- Call gains: 0.50 × $2 = $1 per share

### Theta (Θ): Time Decay

**How much option loses per day (all else equal):**

**All long options have negative theta:**
- You pay theta every day
- Accelerates near expiration
- ATM options have highest theta

**Example:**
- Buy call with Θ = -$0.10/day
- After 10 days (stock unchanged): lost $1
- Last 30 days: decay accelerates significantly

**Time decay curve:**
```
Value
  ↑
  |‾‾‾\___
  |       \__
  |          \_
  |            \__
  |               \___
  |___________________\→ Time
  90  60  30  15   5  0 Days
```

**Critical insight: Most decay in last 30 days!**

### Vega (ν): Volatility Sensitivity

**How much option gains per 1% increase in implied volatility:**

**All long options have positive vega:**
- IV rises → option gains value
- IV falls → option loses value
- ATM options have highest vega

**Example:**
- Buy call with ν = $0.20
- IV rises from 30% to 35% (+5%)
- Call gains: $0.20 × 5 = $1 per share

**This is why options expensive before earnings!**

### Gamma (Γ): Delta Change Rate

**How much delta changes per $1 stock move:**
- High gamma near expiration
- ATM options have highest gamma
- Long options = positive gamma (delta increases with movement)

**Less critical for simple long options, but good to know.**

---

## The Portfolio

**Your position when you buy call or put:**

### Long Call

$$
\Pi = C(S, K, T, \sigma)
$$

**At expiration:**
$$
\text{Value} = \max(S - K, 0)
$$
$$
\text{P\&L} = \max(S - K, 0) - \text{Premium Paid}
$$

**Greeks:**
- Delta: 0 to +1 (positive)
- Theta: Negative (pay decay)
- Vega: Positive (gain from IV rise)
- Gamma: Positive (delta increases if stock rises)

### Long Put

$$
\Pi = P(S, K, T, \sigma)
$$

**At expiration:**
$$
\text{Value} = \max(K - S, 0)
$$
$$
\text{P\&L} = \max(K - S, 0) - \text{Premium Paid}
$$

**Greeks:**
- Delta: -1 to 0 (negative)
- Theta: Negative (pay decay)
- Vega: Positive (gain from IV rise)
- Gamma: Positive (delta magnitude increases if stock drops)

---

## Strike Selection Strategy

**Choosing the right strike is crucial:**

### For Calls (Bullish)

**ITM Calls (Stock > Strike):**
- **Pros:** High delta (0.70-0.90), moves almost 1:1 with stock, less time decay risk
- **Cons:** Expensive, less leverage, mostly intrinsic value
- **Use when:** High conviction, want stock-like returns with less capital

**ATM Calls (Stock ≈ Strike):**
- **Pros:** Balanced delta (0.50), good leverage, not too expensive
- **Cons:** Maximum theta decay, need significant move
- **Use when:** Moderate conviction, standard bullish bet

**OTM Calls (Stock < Strike):**
- **Pros:** Cheap, maximum leverage, defined risk
- **Cons:** Low delta (0.20-0.40), high probability of expiring worthless
- **Use when:** Speculative, expect large move, lottery ticket

**Example:**
- Stock at $100, you're bullish

| Strike | Type | Premium | Delta | Leverage | Risk |
|--------|------|---------|-------|----------|------|
| $90 | ITM | $12 | 0.80 | Low | Low |
| $100 | ATM | $5 | 0.50 | Medium | Medium |
| $110 | OTM | $1 | 0.20 | High | High |

### For Puts (Bearish)

**Same logic, reversed:**

**ITM Puts (Stock < Strike):**
- Expensive, high delta, stock-like downside capture
- Use for high-conviction bearish bets

**ATM Puts (Stock ≈ Strike):**
- Balanced cost/delta
- Standard bearish bet or portfolio hedge

**OTM Puts (Stock > Strike):**
- Cheap, lottery tickets, tail risk hedge
- Low probability but cheap insurance

---

## Time Frame Selection

**Choosing expiration date:**

### Short-Dated (< 1 month)

**Pros:**
- Cheaper (less time value)
- High leverage
- Quick resolution

**Cons:**
- High theta decay
- Need to be right quickly
- Less room for error

**Use when:**
- Specific near-term catalyst (earnings)
- High conviction on timing
- Speculative trades

### Medium-Dated (1-3 months)

**Pros:**
- Balanced theta/cost
- Time for thesis to play out
- Reasonable premium

**Cons:**
- More capital required
- Still significant decay

**Use when:**
- Standard directional trades
- Event 1-2 months away
- Most common choice

### Long-Dated (3-6+ months, LEAPS)

**Pros:**
- Slow theta decay
- Time for thesis to develop
- Can weather volatility
- LEAPS (1-2 years) like stock substitute

**Cons:**
- Expensive
- Capital tied up longer
- Less leverage

**Use when:**
- Long-term bullish/bearish
- Major trend expected
- Stock substitute strategy (LEAPS)

---

## Concrete Example 1: Bullish Call Trade

**Setup:**

**Stock:** NVDA at $500
**Your view:** AI boom will push NVDA to $600+ in next 3 months
**Market conditions:** Moderate volatility, no near-term earnings

**The Trade:**

**Buy 5 contracts of 3-month $500 calls**
- Premium: $35 per share
- Cost: $35 × 5 × 100 = **$17,500**
- Delta: 0.52
- Theta: -$18/day per contract = -$90/day total
- Breakeven: $535 at expiration

**Alternative (stock):**
- Buy 500 shares at $500 = $250,000
- Huge capital requirement!

**Scenario 1: Strong Rise (Stock → $600)**

After 90 days:
- Stock at $600
- Call intrinsic value: $100
- Profit: $100 - $35 = $65 per share
- **Total profit: $65 × 500 shares = $32,500**
- **Return: 186%** on $17,500 investment

Compare to stock:
- Stock profit: $100 × 500 = $50,000
- Return: 20% on $250,000
- **Call massively outperforms on % basis!**

**Scenario 2: Moderate Rise (Stock → $550)**

After 90 days:
- Stock at $550 (+10%)
- Call intrinsic value: $50
- Profit: $50 - $35 = $15 per share
- **Total profit: $15 × 500 shares = $7,500**
- **Return: 43%** on $17,500

**Scenario 3: Small Rise (Stock → $520)**

After 90 days:
- Stock at $520 (+4%)
- Call intrinsic value: $20
- Loss: $20 - $35 = -$15 per share
- **Total loss: -$7,500**
- **Return: -43%**

**Even though stock rose, you lost!** (didn't rise enough)

**Scenario 4: Decline (Stock → $450)**

After 90 days:
- Stock at $450 (-10%)
- Calls expire worthless
- **Total loss: -$17,500** (100%)
- **Max loss achieved**

Compare to stock:
- Stock loss: -$50 × 500 = -$25,000
- **Call loss smaller in absolute terms**

**Scenario 5: Exit Early on IV Spike**

After 30 days:
- Stock still at $500 (no move)
- But IV spikes from 40% to 55% (earnings approaching)
- Vega: +$30 per contract
- Call value rises: $35 + ($0.30 × 15) = $39.50
- Theta decay: -$18 × 30 = -$540 per contract

**Profit: $4.50/share × 500 = $2,250** despite no stock movement!

---

## Concrete Example 2: Bearish Put Trade

**Setup:**

**Stock:** TSLA at $250
**Your view:** Overvalued, expect correction to $200 in 2 months
**Market conditions:** High volatility, recent run-up looks exhausted

**The Trade:**

**Buy 3 contracts of 2-month $250 puts**
- Premium: $18 per share
- Cost: $18 × 3 × 100 = **$5,400**
- Delta: -0.50
- Theta: -$15/day per contract = -$45/day total
- Breakeven: $232 at expiration

**Scenario 1: Strong Decline (Stock → $200)**

After 60 days:
- Stock at $200 (-20%)
- Put intrinsic value: $50
- Profit: $50 - $18 = $32 per share
- **Total profit: $32 × 300 shares = $9,600**
- **Return: 178%** on $5,400 investment

**Your bearish call was right!**

**Scenario 2: Moderate Decline (Stock → $230)**

After 60 days:
- Stock at $230 (-8%)
- Put intrinsic value: $20
- Profit: $20 - $18 = $2 per share
- **Total profit: $2 × 300 = $600**
- **Return: 11%**

**Small profit, needed more decline**

**Scenario 3: Sideways (Stock → $250)**

After 60 days:
- Stock unchanged at $250
- Puts expire worthless (ATM → OTM by expiry)
- **Total loss: -$5,400** (100%)

**Time decay killed you!**

**Scenario 4: Rise (Stock → $280)**

After 60 days:
- Stock at $280 (+12%)
- Puts expire worthless
- **Total loss: -$5,400** (100%)
- **Max loss, but at least capped!**

Compare to shorting:
- Short 300 shares, now need to cover at $280
- Loss: -$30 × 300 = -$9,000
- **Put loss smaller**
- Plus shorting requires margin, has unlimited risk

---

## Long Calls/Puts vs. Stock/Shorting

**When to use options vs. underlying:**

| Aspect | Long Call | Buy Stock | Long Put | Short Stock |
|--------|-----------|-----------|----------|-------------|
| **Capital** | Low ($500-$5,000) | High ($10,000+) | Low ($500-$5,000) | Margin required |
| **Leverage** | High (10-20x) | None (1x) | High (10-20x) | 2x (margin) |
| **Max Loss** | Premium (100%) | Stock to $0 | Premium (100%) | Unlimited |
| **Max Profit** | Unlimited | Unlimited | Strike - Premium | Stock to $0 |
| **Time decay** | Yes (pay theta) | No | Yes (pay theta) | No |
| **Dividends** | No | Yes (receive) | No | Yes (pay) |
| **Voting rights** | No | Yes | No | No |
| **Margin req** | None (cash paid) | 50% for margin | None (cash paid) | High (short sale) |

**Use calls/puts when:**
- Limited capital
- Want leverage
- Want defined risk
- Short-term directional view
- Don't want to hold long-term

**Use stock/shorting when:**
- Long-term horizon
- Want dividends/voting
- Low theta decay tolerance
- More capital available
- Want to wheel (sell covered calls)

---

## Pros and Cons

### Long Calls - Advantages ✓

**1. Leverage**
- Control 100 shares for fraction of cost
- 10-20x leverage common
- Small capital, big exposure

**2. Limited downside**
- Max loss = premium paid
- Known upfront
- Can't lose more than invested

**3. Unlimited upside**
- Benefit from large moves
- No cap on profits
- Asymmetric payoff (good!)

**4. No margin required**
- Pay cash upfront
- No margin calls
- No borrowing costs

**5. Flexibility**
- Can sell anytime before expiration
- Exit on IV spike
- Roll to different strikes/dates

### Long Calls - Disadvantages ✗

**1. Time decay (theta)**
- Lose value every day
- Accelerates near expiration
- Must overcome to profit

**2. Need to be right on timing AND direction**
- Stock can go up but too slowly → lose
- Stock flat or down → lose
- Higher bar than stock

**3. Can lose 100%**
- Options can expire worthless
- Total loss of premium
- High risk on % basis

**4. Volatility crush risk**
- After events, IV drops
- Even if right on direction, can lose
- Post-earnings vol crush common

**5. No dividends**
- Miss out on dividend income
- Stock holders get paid
- Especially matters for high-yield stocks

**6. Psychological difficulty**
- Watching theta decay daily
- Temptation to panic sell
- Requires discipline

### Long Puts - Similar Pros/Cons

**Additional Pros:**
- Don't need margin (vs. shorting)
- Cheaper than shorting for large positions
- Good portfolio hedge (insurance)

**Additional Cons:**
- Limited upside (stock can't go below $0)
- Pay theta while hedging (cost of insurance)

---

## When to Buy Calls

**Best scenarios:**

**1. Strong bullish catalyst ahead**
- Earnings expected to beat
- Product launch
- FDA approval pending
- M&A rumors

**2. Breakout from range**
- Technical pattern forming
- Consolidation ending
- Volume increasing

**3. Low IV environment**
- Options cheap (VIX < 15)
- Premium low
- Good risk/reward

**4. High conviction + Limited capital**
- Want leveraged exposure
- Can't afford full stock position
- Defined risk appealing

**5. Before news/event**
- Buy when IV low
- Before market prices in event
- Can exit on IV spike (don't need directional move)

**Avoid calls when:**
- IV very high (expensive)
- Stock already moved (late to party)
- Uncertain timing (theta will kill you)
- Long-term hold (use stock or LEAPS instead)

---

## When to Buy Puts

**Best scenarios:**

**1. Strong bearish catalyst ahead**
- Earnings expected to miss
- Regulatory problems
- Competitive threat
- Macro downturn

**2. Technical breakdown**
- Support levels breaking
- Trend reversal
- Weakening momentum

**3. Portfolio hedging**
- Worried about market crash
- Protect gains
- Sleep better (insurance)

**4. Cannot short (hard-to-borrow)**
- Stock unavailable to short
- Puts are alternative
- Defined risk vs. short's unlimited loss

**5. Overextended valuations**
- Bubble territory
- Unsustainable multiples
- Expect mean reversion

**Avoid puts when:**
- IV very high (expensive hedging)
- Stock already crashed (late)
- Strong bull market (fighting trend)
- Long time horizon (theta too expensive)

---

## Common Mistakes

**Top 10 beginner mistakes:**

### 1. Buying OTM Lottery Tickets

**Mistake:** Buy cheap OTM options hoping for home run
**Why it fails:** Very low probability, usually expire worthless
**Fix:** Focus on ATM or slightly OTM for better probability

### 2. Holding Until Expiration

**Mistake:** "I'll wait and see" → watch option decay to zero
**Why it fails:** Theta accelerates, need huge move to profit
**Fix:** Exit at 50% profit or cut loss early

### 3. Ignoring IV (Buying Before Earnings)

**Mistake:** Buy call day before earnings because "stock will beat"
**Why it fails:** IV crush post-earnings can negate stock gain
**Fix:** Check IV percentile, consider buying weeks before

### 4. Fighting Theta Too Long

**Mistake:** Stock hasn't moved yet, "I'll give it more time"
**Why it fails:** Every day costs money, decay accelerates
**Fix:** Use longer-dated options or accept losses early

### 5. Over-Leveraging

**Mistake:** "Options are cheap, I'll buy 50 contracts!"
**Why it fails:** High probability of total loss, blown account
**Fix:** Position size: max 2-5% of portfolio per trade

### 6. Not Understanding Greeks

**Mistake:** Ignore delta, theta, vega
**Why it fails:** Surprised by behavior, don't know when to exit
**Fix:** Learn Greeks before trading

### 7. Buying Illiquid Options

**Mistake:** Trade options with wide bid-ask spreads
**Why it fails:** Lose 10% on entry/exit just from spreads
**Fix:** Only trade liquid strikes (volume > 100/day)

### 8. Emotional Trading

**Mistake:** Chase after stock already moved
**Why it fails:** FOMO entry, buying tops
**Fix:** Have thesis before trade, stick to plan

### 9. Confusing Probability

**Mistake:** "I'm up 100%, this always works!"
**Why it fails:** One big win doesn't mean skill, could be luck
**Fix:** Track all trades, understand win rate needed

### 10. No Exit Plan

**Mistake:** Enter trade without profit target or stop loss
**Why it fails:** Hold too long (theta) or panic sell bottoms
**Fix:** Set targets: exit at 50% profit, -50% loss

---

## Risk Management Rules

**Essential guidelines:**

### Position Sizing

**Rule of thumb:**
$$
\text{Position Size} = \frac{\text{Risk Capital} \times 0.02}{\text{Option Premium}}
$$

**Example:**
- $50,000 account
- 2% risk per trade = $1,000
- Option costs $5/share = $500/contract
- **Max size: 2 contracts**

### Diversification

**Don't concentrate:**
- Max 5-10% of portfolio in options
- Max 2-5% per trade
- Spread across multiple positions
- Different sectors, timeframes

### Exit Rules

**Set upfront:**
- **Take profit:** 50-100% gain
- **Stop loss:** -50% loss (don't hold to zero)
- **Time stop:** Exit if 50% of time passed with no move
- **IV exit:** Exit on IV spike even if stock flat

### Avoid These

- Never "double down" on losing position
- Never "roll down and out" hoping for recovery (usually fails)
- Never risk more than 5% on single trade
- Never trade illiquid options (vol < 100)
- Never buy day before earnings (IV crush)

---

## Real-World Examples

### Example 1: AAPL iPhone Launch (Sept 2023)

**Setup:**
- AAPL at $175 pre-announcement
- History: stock usually rallies on iPhone launch
- IV at 25% (moderate)

**Trade:** Buy $175 calls, 2 months out
- Premium: $8
- Cost: $800 per contract

**Outcome:**
- iPhone 15 announced, well-received
- Stock rallied to $190 over next month
- Calls at $15 intrinsic
- **Profit: $7 per share (88%)**

**Lesson:** Catalyst-driven, entered when IV still reasonable

### Example 2: TSLA Earnings Miss (Oct 2023)

**Setup:**
- TSLA at $240 before earnings
- High valuation, deliveries disappointing
- IV at 65% (elevated pre-earnings)

**Trade:** Buy $240 puts, 1 month out
- Premium: $15
- Cost: $1,500 per contract

**Outcome:**
- Earnings miss, guidance weak
- Stock dropped to $220 next day
- But puts only worth $20 (IV crushed 65% → 40%)
- **Profit: Only $5/share (33%)**

**Lesson:** Even though directionally correct, IV crush limited gains. Better to have bought weeks before.

### Example 3: COVID Crash Hedge (Feb 2020)

**Setup:**
- SPY at $340 (all-time high)
- COVID spreading, uncertainty high
- Bought OTM puts as hedge

**Trade:** Buy $320 puts (5% OTM), 2 months
- Premium: $3
- Cost: $300 per contract (cheap insurance)

**Outcome:**
- Market crashed, SPY → $220
- Puts worth $100 intrinsic
- **Profit: $97 per share (3,233%!)**

**Lesson:** Cheap OTM puts can pay off huge in tail events. This is portfolio insurance in action.

### Example 4: Theta Decay Lesson (Small Cap Biotech)

**Setup:**
- Small biotech at $20
- FDA decision expected "sometime in Q3"
- Bought $20 calls, 3 months out

**Trade:** Premium: $4 per share

**Outcome:**
- Stock stayed at $20 for 90 days (no FDA decision)
- Calls expired worthless
- **Loss: $4/share (100%)**

**Lesson:** Theta decay kills even if stock unchanged. Need definite catalyst timing.

---

## What to Remember

### Core Concept

**Long calls and puts are directional bets with limited risk and leveraged exposure:**

$$
\text{Long Call} = \text{Bullish bet with defined risk and unlimited profit}
$$
$$
\text{Long Put} = \text{Bearish bet with defined risk and large profit potential}
$$

- Pay premium upfront
- Max loss = premium (known)
- Max profit = unlimited (call) or large (put)
- Need to be right on direction AND timing

### The Setup

**Long Call:**
- Buy call option
- Profit if stock rises above strike + premium
- Leverage: control 100 shares for fraction of cost
- Risk: lose 100% if wrong

**Long Put:**
- Buy put option
- Profit if stock falls below strike - premium
- Alternative to shorting (no margin, defined risk)
- Risk: lose 100% if wrong

### The Greeks

**Critical to understand:**
- **Delta:** 0.50 means $0.50 gain per $1 stock move (calls positive, puts negative)
- **Theta:** -$0.10 means lose $0.10/day (always negative for long options)
- **Vega:** +$0.30 means gain $0.30 per 1% IV rise (always positive for long options)
- **Gamma:** How delta changes (positive for long options)

### Strike Selection

**Three choices:**
- **ITM:** Expensive, high delta (0.70+), stock-like, lower leverage
- **ATM:** Balanced cost/delta (0.50), standard choice
- **OTM:** Cheap, low delta (0.20-0.40), lottery ticket, high risk

**Beginner recommendation: Start with ATM**

### Time Selection

**Three ranges:**
- **Short (<1 month):** Cheap but high theta, need quick move
- **Medium (1-3 months):** Balanced, most common
- **Long (3+ months, LEAPS):** Expensive but time to work, stock substitute

**Beginner recommendation: 2-3 months out**

### Maximum Profit/Loss

**Long Call:**
- Max loss: Premium paid (100%)
- Max profit: Unlimited (stock can go to infinity)
- Breakeven: Strike + Premium

**Long Put:**
- Max loss: Premium paid (100%)
- Max profit: Strike - Premium (stock to $0)
- Breakeven: Strike - Premium

### When to Use

**Buy calls when:**
- Bullish catalyst coming
- Low IV (options cheap)
- Want leverage
- Limited capital

**Buy puts when:**
- Bearish catalyst coming
- Portfolio hedge needed
- Can't or won't short
- Defined risk desired

**Don't use when:**
- Very high IV (expensive)
- Long-term hold (use stock/LEAPS)
- Unclear timing
- Can't handle 100% loss psychologically

### Common Mistakes to Avoid

1. Don't buy OTM lottery tickets consistently
2. Don't hold to expiration hoping for miracle
3. Don't ignore IV (check percentile)
4. Don't over-leverage (max 2-5% per trade)
5. Don't trade illiquid options (wide spreads)
6. Don't buy day before earnings (IV crush)
7. Don't double down on losers
8. Don't forget theta (pay every day)

### Risk Management

**Essential rules:**
- Position size: Max 2-5% of portfolio per trade
- Stop loss: Exit at -50% (don't hold to zero)
- Profit target: Exit at +50-100%
- Time stop: Exit if 50% time elapsed with no move
- Diversify: Multiple positions, sectors, timeframes

### Comparison to Stock

**Advantages over stock:**
- Massive leverage (10-20x)
- Defined risk (can't lose more than premium)
- Less capital required

**Disadvantages vs. stock:**
- Time decay (theta bleeds daily)
- Can expire worthless (100% loss)
- No dividends
- Need to be right on timing

### Your Learning Path

**Start here (long calls/puts), then:**
1. Master single-leg basics (this chapter)
2. Learn covered calls (income on stocks you own)
3. Progress to spreads (vertical spreads reduce risk)
4. Eventually: complex strategies (calendars, straddles, gamma scalping)

**Long calls and puts are THE FOUNDATION for everything else!**

### Final Wisdom

> "Long calls and puts are the simplest option strategies, but don't mistake simple for easy. They require you to be right on BOTH direction and timing, and theta decay is relentless. Use them for high-conviction, short-term directional bets with defined risk. Master these before attempting any complex strategies. If you can't make money with simple long options, you won't make money with complex spreads either."

**Key to success:**
- High-conviction trades only
- Proper position sizing (2-5% max)
- Exit discipline (take profits, cut losses)
- Understand Greeks (especially theta and delta)
- Check IV before entering (avoid expensive options)
- Have catalyst (don't just hope)

**Most important:** This is where EVERYONE starts in options. Master this foundation before advancing! 🎯📈
