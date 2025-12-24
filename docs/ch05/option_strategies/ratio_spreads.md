# Ratio Spreads

**Ratio spreads** are unbalanced option strategies where you buy and sell different numbers of options at different strikes, creating positions with directional bias, limited cost, but potential unlimited risk on one side.

---

## The Core Insight

**The fundamental idea:**
- You have a directional view (bullish or bearish)
- But want to reduce cost (or receive credit)
- Sell MORE options than you buy
- Unbalanced position (not 1:1 ratio)
- Accept unlimited risk beyond a point for cheaper entry

**The key equation:**
$$
\text{Ratio Spread} = \text{Buy N options} + \text{Sell M options (where M > N)}
$$

Typical ratios: 1:2, 1:3, 2:3

**You're essentially betting: "The stock will move moderately in my direction, but NOT too far - I'll profit from the move while collecting premium to reduce cost."**

---

## What Is a Ratio Spread?

**The unbalanced strategy:**

### The Basic Structure

**Call Ratio Spread (Bullish with cap):**
- Buy 1 ITM or ATM call
- Sell 2 (or more) OTM calls
- Net debit or credit depending on strikes/ratio

**Example:**
- Stock at $100
- Buy 1 × $100 call for $5
- Sell 2 × $110 calls for $2 each (receive $4)
- Net cost: $1 debit (or could be credit with different strikes)

**What you've created:**
- Profit if stock rises moderately (to $110)
- Max profit at upper short strike ($110)
- **Unlimited risk if stock goes way above** ($110+)
- Cheaper than buying call alone

**Put Ratio Spread (Bearish with cap):**
- Buy 1 OTM or ATM put
- Sell 2 (or more) OTM puts (lower strikes)
- Net debit or credit

**Example:**
- Stock at $100
- Buy 1 × $100 put for $5
- Sell 2 × $90 puts for $2 each (receive $4)
- Net cost: $1 debit
- **Unlimited risk if stock crashes below $90**

### The Key Characteristic

**Unbalanced = Unlimited Risk:**

Unlike vertical spreads (1:1 ratio):
- Vertical: Buy 1, sell 1 → defined risk both sides
- Ratio: Buy 1, sell 2 → **UNCOVERED short options beyond a point**

**This is the danger and opportunity:**
- Cheaper entry (collect extra premium)
- But naked short exposure at extremes
- **Must manage actively**

---

## Call Ratio Spread: Deep Dive

### The Structure

**Standard 1:2 call ratio spread:**

**Position:**
- Long 1 call at $K_1$ (lower strike)
- Short 2 calls at $K_2$ (higher strike, where $K_2 > K_1$)

**Example:**
- Long 1 × $100 call @ $6
- Short 2 × $110 calls @ $2.50 each
- Net: $6 - $5 = **$1 debit**

### Payoff Analysis

**Below $100:**
- All calls worthless
- Loss: $1 (net debit)

**At $105:**
- Long call: $5 value
- Short calls: $0
- P&L: $5 - $1 = **+$4 profit**

**At $110 (MAX PROFIT):**
- Long call: $10 value
- Short calls: $0 (ATM, expire worthless)
- P&L: $10 - $1 = **+$9 profit (900% ROI!)**

**At $115:**
- Long call: $15 value
- Short calls: -$10 ($5 each × 2 = -$10)
- P&L: $15 - $10 - $1 = **+$4 profit**

**At $120 (Breakeven point):**
- Long call: $20
- Short calls: -$20 ($10 each × 2)
- P&L: $20 - $20 - $1 = **-$1 (breakeven)**

**Above $120:**
- **UNLIMITED LOSS**
- For every $1 stock rises, lose $1
- No protection!

### Payoff Diagram

```
    Profit
      ↑
     9 |      /\
     8 |     /  \
     6 |    /    \
     4 |   /      \___
     2 |  /          \
  ────0┼─/────────────\────→ Stock Price
    -1 |/              \
       100  110  120   \
                        ↓
                   (Unlimited loss)
```

**Sweet spot:** Stock at $110 (upper short strike)
**Danger zone:** Stock above $120 (upper breakeven)

### The Math

**Maximum profit:**
$$
\text{Max Profit} = (K_2 - K_1) - \text{Net Debit}
$$

Or if credit:
$$
\text{Max Profit} = (K_2 - K_1) + \text{Net Credit}
$$

**Upper breakeven:**
$$
\text{Upper BE} = K_2 + \frac{(K_2 - K_1) - \text{Net Debit}}{\text{Ratio} - 1}
$$

For 1:2 ratio:
$$
\text{Upper BE} = K_2 + (K_2 - K_1) - \text{Net Debit}
$$

**Example:**
- Long $100, short 2 × $110, cost $1
- Max profit: $10 - $1 = $9 (at $110)
- Upper BE: $110 + $10 - $1 = $119

---

## Put Ratio Spread: Deep Dive

### The Structure

**Standard 1:2 put ratio spread:**

**Position:**
- Long 1 put at $K_1$ (higher strike)
- Short 2 puts at $K_2$ (lower strike, where $K_2 < K_1$)

**Example:**
- Long 1 × $100 put @ $6
- Short 2 × $90 puts @ $2.50 each
- Net: $6 - $5 = **$1 debit**

### Payoff Analysis

**Above $100:**
- All puts worthless
- Loss: $1 (net debit)

**At $95:**
- Long put: $5 value
- Short puts: $0
- P&L: $5 - $1 = **+$4 profit**

**At $90 (MAX PROFIT):**
- Long put: $10 value
- Short puts: $0 (ATM)
- P&L: $10 - $1 = **+$9 profit**

**At $85:**
- Long put: $15 value
- Short puts: -$10 ($5 each × 2)
- P&L: $15 - $10 - $1 = **+$4 profit**

**At $80 (Breakeven):**
- Long put: $20
- Short puts: -$20 ($10 each × 2)
- P&L: $20 - $20 - $1 = **-$1 (breakeven)**

**Below $80:**
- **UNLIMITED LOSS** (stock can go to $0)
- Very dangerous!

### Payoff Diagram

```
    Profit
      ↑
     9 |      /\
     8 |     /  \
     6 |    /    \
     4 |   /      \___
     2 |  /          \
  ────0┼─/────────────\────→ Stock Price
    -1 |/              \
       80   90  100    ↓
      ↓               (Calls continue)
   (Puts: unlimited loss to $0)
```

**Sweet spot:** Stock at $90 (lower short strike)
**Danger zone:** Stock below $80 (lower breakeven)

---

## Types of Ratio Spreads

### 1. Standard Ratio (1:2)

**Most common:**
- Buy 1, sell 2
- Moderate risk/reward
- Typical use

### 2. Aggressive Ratio (1:3 or higher)

**Higher risk:**
- Buy 1, sell 3 or more
- **More naked exposure**
- Cheaper or larger credit
- Higher max profit
- Much riskier

**Example:**
- Buy 1 × $100 call
- Sell 3 × $110 calls
- **Very dangerous if stock moons**

### 3. Conservative Ratio (2:3)

**Lower risk:**
- Buy 2, sell 3
- Less naked exposure (only 1 uncovered)
- More expensive
- Safer

**Example:**
- Buy 2 × $100 calls
- Sell 3 × $110 calls
- Only 1 call uncovered

### 4. Ratio Call Spread (for credit)

**Receive money upfront:**
- Strikes chosen so net credit
- Example: Buy $105, sell 2 × $115
- Receive $1 credit
- Free trade (profit if in range)

**Danger:** Still unlimited risk above breakeven!

### 5. Ratio Put Spread (for credit)

**Receive money upfront:**
- Buy $95 put, sell 2 × $85 puts
- Receive credit
- Free trade
- **Still unlimited risk below breakeven**

---

## Concrete Example: Call Ratio Spread Trade

**Complete walkthrough:**

### Setup

**Stock:** TSLA at $250
**View:** Moderately bullish - expect rise to $270-280, but not $300+
**Strategy:** 45-day call ratio spread
**Implied Vol:** 50% (moderate)

### Available Options

| Strike | Call Premium |
|--------|--------------|
| $250 | $15.00 |
| $270 | $7.00 |
| $280 | $4.00 |

### The Trade: 1:2 Ratio at $250/$270

**Execute:**
- Buy 1 × $250 call @ $15.00
- Sell 2 × $270 calls @ $7.00 each = $14.00 received
- **Net debit: $1.00** ($100 total)

**Position summary:**
- Cost: $100
- Max profit: $1,900 (at $270)
- Max loss (downside): $100
- Max loss (upside): UNLIMITED (above $289)
- Upper breakeven: $289

### Scenario 1: Perfect - TSLA at $270 (Max Profit)

**At expiration:**
- TSLA exactly at $270
- $250 call worth: $20 ($2,000)
- $270 calls worth: $0 (ATM, expire worthless)
- **P&L: $2,000 - $100 = +$1,900 (1,900% ROI!)**

**Perfect outcome:** Stock at upper short strike

### Scenario 2: Good - TSLA at $265

**At expiration:**
- TSLA at $265
- $250 call worth: $15 ($1,500)
- $270 calls worth: $0
- **P&L: $1,500 - $100 = +$1,400**

**Still very profitable**

### Scenario 3: Modest - TSLA at $260

**At expiration:**
- TSLA at $260
- $250 call worth: $10 ($1,000)
- $270 calls worth: $0
- **P&L: $1,000 - $100 = +$900**

**Decent profit**

### Scenario 4: Danger - TSLA at $300 (Way Up)

**At expiration:**
- TSLA at $300 (big rally)
- $250 call worth: $50 ($5,000)
- $270 calls worth: -$60 ($30 × 2 = -$6,000)
- **P&L: $5,000 - $6,000 - $100 = -$1,100**

**Loss! Stock moved TOO MUCH**

### Scenario 5: Disaster - TSLA at $350

**At expiration:**
- TSLA at $350 (massive rally)
- $250 call worth: $100 ($10,000)
- $270 calls worth: -$160 ($80 × 2 = -$16,000)
- **P&L: $10,000 - $16,000 - $100 = -$6,100**

**Catastrophic loss from being right on direction!**

**This is the ratio spread paradox: Can lose money from being "too right"**

### Management Decision

**After 20 days:**
- TSLA now at $280 (moving up quickly)
- Near danger zone
- **Decision: Close the spread**
- Exit for small profit/loss rather than risk unlimited loss

**This is why active management is critical!**

---

## When to Use Ratio Spreads

### Favorable Conditions

**1. Moderately directional view:**
- Think stock will move, but not too far
- Have target in mind
- Confident it won't go past breakeven

**2. High implied volatility:**
- Expensive options
- Collect more premium on shorts
- Can establish for credit

**3. Reduce cost of directional bet:**
- Want long call/put exposure
- Can't afford full premium
- Accept risk for cheaper entry

**4. Range-bound conviction:**
- Stock will rise/fall to certain level
- Then stop or reverse
- Sweet spot at your target

### Unfavorable Conditions

**1. Uncertain direction:**
- If unsure, naked shorts are dangerous
- Use defined-risk spreads instead

**2. Potential for big moves:**
- Earnings ahead
- Binary events (FDA, etc.)
- High chance of exceeding breakeven
- **Very dangerous!**

**3. Low volatility:**
- Cheap options anyway
- Not much premium to collect
- Better to use straight call/put

**4. Cannot monitor:**
- Need active management
- Can't set and forget
- If busy, use defined-risk strategies

---

## Risk Management (CRITICAL!)

**Ratio spreads require strict discipline:**

### Rule 1: Position Sizing

**Never more than 2-3% of account:**
- Unlimited loss potential
- One bad trade can destroy account
- **Size very small**

**Example:**
- $50,000 account
- Max risk per ratio spread: $1,000-1,500
- Even though "max loss on downside" is $100, upside is unlimited!

### Rule 2: Stop Loss (Upper Breakeven)

**MUST have hard stop:**
- If stock approaches upper breakeven → close!
- Don't hope it comes back
- Unlimited loss awaits

**Example:**
- Upper BE at $289
- Stock hits $285 → **close immediately**
- Accept small loss rather than catastrophe

### Rule 3: Avoid Before Events

**Never hold ratio spreads through:**
- Earnings
- FDA decisions
- Acquisitions
- FOMC meetings (if relevant)
- **Gap risk is existential threat**

### Rule 4: Monitor Daily

**Active management required:**
- Check position daily
- Watch for moves toward danger
- Be ready to close
- **Not passive strategy**

### Rule 5: Close Early if Profit

**Don't be greedy:**
- If at 50% max profit → consider closing
- Max profit at upper strike is rare
- Take profits, redeploy

**Example:**
- Max profit: $1,900 at $270
- Current profit: $1,000 at $265
- **Close! Don't wait for $270**

### Rule 6: Avoid in Volatile Stocks

**Don't use ratio spreads on:**
- Meme stocks (AMC, GME)
- Biotech before FDA
- Small caps with wild swings
- **Stick to stable, large caps**

---

## Ratio Spreads vs. Other Strategies

| Strategy | Cost | Downside Risk | Upside Risk | Complexity |
|----------|------|---------------|-------------|-----------|
| **Call Ratio Spread** | Low/Credit | Limited (debit) | **UNLIMITED** | High |
| **Put Ratio Spread** | Low/Credit | **UNLIMITED** | Limited (debit) | High |
| Long Call | Medium | Limited (premium) | Unlimited | Low |
| Bull Call Spread | Low | Limited | Limited | Medium |
| Calendar Spread | Medium | Limited | Limited | Medium |
| Iron Condor | Credit | Limited | Limited | Medium |

**Key difference:**

**Ratio spreads are ONLY strategy with:**
- Unlimited risk on ONE side (not both)
- Can be established for credit
- Profit from moderate move but lose from large move

**This is unique and dangerous!**

---

## Advanced Variations

### 1. Ratio Backspread (Reverse Ratio)

**Opposite structure:**
- Sell fewer, buy more
- Example: Sell 1 × $100 call, buy 2 × $110 calls
- **Profit from big moves** (like straddle but cheaper)
- Usually credit
- Unlimited profit one direction

**Use when:**
- Expect volatility
- Want cheaper than straddle
- Accept risk on one side

### 2. Christmas Tree Spread

**Multiple ratios:**
- Buy 1 low
- Sell 2 middle
- Sell 1 high
- Like ratio + vertical

**More complex, more defined risk**

### 3. Ladder Spread

**Progressive strikes:**
- Buy 1 ATM
- Sell 1 OTM
- Sell 1 farther OTM
- Graduated profit zones

### 4. Ratio Diagonal Spread

**Different expirations:**
- Buy longer-dated
- Sell 2 shorter-dated (different strikes)
- Combines ratio + calendar

**Very complex, professional use**

---

## Common Mistakes

### Mistake 1: Underestimating Upside Risk

❌ **Wrong:**
- "Stock at $250, won't go past $300"
- Set up ratio spread
- Stock gaps to $320 on news
- **Catastrophic loss**

**Why it fails:**
- Stocks can always surprise
- News happens
- Gap risk is real
- Unlimited loss is unlimited

✅ **Better:**
- Always have stop at upper BE
- Size tiny (2% max)
- Never hold through events
- Accept you can't predict extremes

### Mistake 2: Holding Through Earnings

❌ **Wrong:**
- Set up ratio spread before earnings
- "Stock won't move more than 10%"
- Stock moves 20% (common!)
- **Disaster**

**Why it fails:**
- Earnings create gaps
- 20-30% moves happen
- Ratio spreads can't handle this
- Unlimited loss triggered

✅ **Better:**
- Close before earnings
- Never hold through binary events
- Use defined-risk strategies for events

### Mistake 3: No Stop Loss

❌ **Wrong:**
- Set up ratio spread, forget about it
- Stock drifts toward danger
- "It'll come back"
- Blows past upper BE
- **Account destroyed**

**Why it fails:**
- Unlimited loss doesn't care about hope
- Need mechanical stops
- Emotions kill you

✅ **Better:**
- Hard stop at upper BE minus buffer
- No exceptions
- Mechanical exit

### Mistake 4: Over-Sizing

❌ **Wrong:**
- $25,000 account
- Risk $5,000 on ratio spread (20%)
- "Max loss is just my debit!"
- Forgets about unlimited upside risk

**Why it fails:**
- One bad ratio spread = account blown
- Max loss isn't really max (upside unlimited)
- Overconfidence

✅ **Better:**
- 2% max sizing
- Assume worst case (loss thousands)
- Never more than few contracts

### Mistake 5: Wrong Strikes

❌ **Wrong:**
- Strikes too close (short at $105, long at $100)
- Very small profit zone
- High chance of blowing through

**Why it fails:**
- Narrow sweet spot
- Easy to overshoot
- Risk >> reward

✅ **Better:**
- Strikes at least $10 apart (for $100 stock)
- Give room to work
- Better risk/reward

---

## What to Remember

### Core Concept

**Ratio spreads are unbalanced directional bets with unlimited risk:**

$$
\text{Ratio Spread} = \text{Buy 1} + \text{Sell 2+}
$$

- Cheaper than buying options alone
- Profit from moderate moves
- **LOSE from extreme moves** (paradox!)
- Unlimited risk one direction
- Requires active management

### The Structure

**Call ratio spread:**
- Bullish with upper cap
- Unlimited risk if too bullish

**Put ratio spread:**
- Bearish with lower cap
- Unlimited risk if too bearish

**Ratio:** Typically 1:2, but can be 1:3, 2:3, etc.

### The Payoff

**Sweet spot:** Stock at upper (call) or lower (put) short strike
**Breakeven zones:** Two breakevens (one on each side)
**Danger zone:** Beyond upper/lower breakeven = unlimited loss

**Max profit:**
$$
\text{Max Profit} = \text{Strike Width} \pm \text{Net Debit/Credit}
$$

**Upper breakeven (calls):**
$$
\text{Upper BE} = \text{Short Strike} + \frac{\text{Max Profit}}{\text{Extra Shorts}}
$$

### The Risk Profile

**Unique characteristics:**
- Limited loss one side (debit paid)
- **UNLIMITED loss other side** (naked shorts)
- Can profit from being wrong
- Can LOSE from being too right
- **This is the paradox and danger**

### When to Use

**Best scenarios:**
- Moderate directional view (not extreme)
- High IV (expensive options, collect premium)
- Target price in mind
- Can monitor actively
- Stable, large-cap stocks

**Avoid:**
- Before binary events
- Volatile stocks
- If can't monitor
- If unsure of direction
- **If can't accept unlimited risk**

### Risk Management (CRITICAL!)

**Non-negotiable rules:**
1. **Size tiny** (2% max)
2. **Stop at upper BE** (mechanical, no exceptions)
3. **Never through events** (close before earnings)
4. **Monitor daily** (active strategy)
5. **Close at 50% profit** (don't be greedy)
6. **Stable stocks only** (no meme stocks!)

**Break any rule = potential disaster**

### Success Factors

**What you need:**
1. Accurate target price
2. Confidence it won't overshoot
3. High IV environment
4. Active monitoring capability
5. Iron discipline (stops, sizing)
6. Emotional control (close when needed)

### Common Mistakes

**Avoid:**
1. Underestimating upside/downside risk
2. Holding through earnings
3. No stop loss
4. Over-sizing
5. Strikes too close
6. Set and forget (needs monitoring!)

### Comparison to Similar Strategies

**vs. Vertical Spread:**
- Ratio: Unlimited risk, cheaper
- Vertical: Defined risk, more expensive

**vs. Long Call/Put:**
- Ratio: Cheaper, capped profit
- Long: More expensive, unlimited profit

**vs. Iron Condor:**
- Ratio: Directional, unlimited one side
- Iron Condor: Neutral, defined both sides

**vs. Calendar:**
- Ratio: Single expiration
- Calendar: Multiple expirations

### Your Strategy Arsenal

**Where this fits:**

```
DIRECTIONAL STRATEGIES:
1. Long Calls/Puts (simple, unlimited profit)
2. Vertical Spreads (defined risk)
3. Ratio Spreads (cheaper, UNLIMITED risk) ← You are here!
   ↓
ADVANCED:
4. Ratio Backspreads (opposite)
5. Christmas Trees, Ladders (complex)
```

**Ratio spreads are the "cheap but dangerous" directional play!**

### Practical Wisdom

- **Cheaper isn't always better** (undefined risk costs)
- **Unlimited risk is real** (not theoretical)
- **Being too right can hurt** (unique to ratio spreads)
- **Active management required** (not passive)
- **Stops are mandatory** (no exceptions)
- **Events are deadly** (gap risk)
- **Size matters enormously** (2% max, period)
- **Most pros avoid these** (risk not worth reward)

### Final Thought

**Ratio spreads are advanced and dangerous:**

> "Ratio spreads appeal to traders who want cheap directional exposure. You can get long exposure for pennies or even credits. But this 'free lunch' comes with a deadly cost: unlimited risk. You can be absolutely right on direction - stock rallies from $250 to $300 as predicted - and still lose thousands because it went 'too far.' Professional traders mostly avoid ratio spreads because one mistake, one gap, one unexpected move can destroy an account. If you must use them: tiny size, hard stops, never through events, and pray you're not unlucky. Most traders are better off with defined-risk vertical spreads and sleeping well at night."

**The harsh truth:**
- Ratio spreads are alluring (cheap/free!)
- But they're dangerous (unlimited loss!)
- Most blowups come from these
- **Better alternatives exist** (verticals, calendars)
- Only use if you understand AND accept unlimited risk
- Even then, size tiny and manage obsessively

**Master defined-risk strategies before attempting ratio spreads!** ⚠️📊
