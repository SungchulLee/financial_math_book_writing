# Short Strangles

**Short strangles** are neutral option strategies where you simultaneously sell an out-of-the-money put and an out-of-the-money call, profiting from time decay and low volatility when the stock stays within a range.

---

## The Core Insight

**The fundamental idea:**

- Stocks often trade sideways or within a range
- You can profit from this lack of movement
- Sell both a put and call to collect double premium
- Win if stock stays between breakeven points
- High probability of profit, but unlimited risk on both sides
- Best in low volatility environments

**The key equation:**

$$
\text{Max Profit} = \text{Put Premium} + \text{Call Premium} \quad (\text{limited, collected upfront})
$$

$$
\text{Max Loss} = \text{Unlimited on both sides}
$$

**You're essentially betting: "The stock will stay within a range, and I'll profit from time decay on both options expiring worthless."**

---

## What Is a Short Strangle?

**Before trading short strangles, understand what you're selling:**

### Structure

**Definition:** Simultaneously sell an OTM put and an OTM call with the same expiration date.

**Components:**

1. **Sell OTM Put** at strike $K_P$ (below current price)
2. **Sell OTM Call** at strike $K_C$ (above current price)
3. Both expire same date
4. Collect total premium = Put premium + Call premium

**Example:**

- Stock at $100
- Sell $95 put for $2
- Sell $105 call for $2
- Total credit: $4 × 100 = $400 per contract

**At expiration:**

- Stock between $95-$105 → Both options expire worthless → Keep $400
- Stock at $90 → Put worth $5, lose $300 ($500 - $200 received)
- Stock at $110 → Call worth $5, lose $300 ($500 - $200 received)

### Key Characteristics

**Neutral strategy:**
- Profit from stock staying in a range
- Don't need directional prediction
- Win from time decay and volatility decrease

**Risk profile:**
- **Max profit:** Total premium collected (limited)
- **Max loss:** Unlimited on both sides
- **Breakeven points:** Two of them
  - Lower: Put strike - Total premium
  - Upper: Call strike + Total premium

**Probability:**
- High probability of profit (60-70% typical)
- But losses can be large when they occur
- Defined mathematically by delta of sold options

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/short_strangle_payoff.png?raw=true" alt="short_strangle_payoff" width="700">
</p>
**Figure 1:** Short strangle payoff diagram showing the profit zone between breakeven points and unlimited risk on both tails. Maximum profit occurs when stock stays between strikes at expiration.

---

## Economic Interpretation: Insurance Selling

**Beyond the basic definition, understanding what short strangles REALLY are economically:**

### The Insurance Analogy

**The deep insight:**

A short strangle is economically equivalent to **selling insurance on both tail events**. When you sell a strangle, you're essentially:

1. **Selling crash insurance** (the put) to bearish traders
2. **Selling breakout insurance** (the call) to bullish traders
3. **Collecting premiums** from both sides
4. **Hoping neither event occurs** (stock stays calm)

**Formal decomposition:**

$$
\underbrace{\text{Short Strangle}}_{\text{Credit } C_P + C_C} \equiv \underbrace{\text{Sell Put}}_{\text{Crash Insurance}} + \underbrace{\text{Sell Call}}_{\text{Rally Insurance}}
$$

**Why this matters:**

**Traditional income (dividends):**
- Wait for company to pay dividends
- Maybe 2-3% annually
- Passive income but very slow

**Short strangle (options income):**
- Collect premiums immediately
- Can earn 2-5% per month in ideal conditions
- Active management required
- **Risk: Unlimited if stock breaks out either direction**

**The premium you collect ($4 in our example) is compensation for bearing tail risk - the catastrophic loss if the stock moves dramatically.**

### Example: Breaking Down the SPY Strangle

**Setup:**
- SPY at $450
- Sell $440 put for $3
- Sell $460 call for $3
- Total credit: $6

**What you're really doing:**

$$
\begin{align}
\text{Economic Position} &= \text{Sell crash protection at \$440} \\
&+ \text{Sell breakout protection at \$460} \\
&+ \text{Collect \$600 premium} \\
&+ \text{Bear unlimited risk if wrong}
\end{align}
$$

**Scenarios:**

| SPY at Expiry | Option Values | Your P&L |
|--------------|---------------|----------|
| $450 (unchanged) | Both expire worthless | **+$600 (keep all premium)** |
| $445 (small move) | Both still OTM | **+$600 (keep all premium)** |
| $435 (down $15) | Put worth $5, Call $0 | **-$400 ($500 - $300 put premium - $300 call premium)** |
| $465 (up $15) | Call worth $5, Put $0 | **-$400 ($500 - $300 call premium - $300 put premium)** |
| $420 (crash) | Put worth $20, Call $0 | **-$1,400** (catastrophic) |
| $480 (rally) | Call worth $20, Put $0 | **-$1,400** (catastrophic) |

**This shows the core tradeoff: high probability small wins vs. low probability large losses!**

### The Volatility Perspective

**Short strangles are fundamentally short volatility positions:**

$$
\text{Short Strangle Profit} \propto -\Delta\sigma \times \text{Vega}
$$

**What this means:**

- When IV (implied volatility) increases → Position loses value
- When IV decreases → Position gains value
- You profit when market calms down
- You lose when market gets choppy

**Example:**

- Enter short strangle when IV = 20% (low)
- Stock stays at $100 but IV spikes to 40% (earnings, crisis, etc.)
- Even though stock unchanged, your short options now worth MORE
- **You can lose money even with zero stock movement!**

### Why Traders Sell Strangles

**Understanding the strategic advantage:**

**Scenario: Believe SPY will be calm for next 30 days**

**Option A: Do Nothing**
- No income
- No risk
- No reward

**Option B: Sell Short Strangle**
- Collect $600 upfront (1.3% return in 30 days ≈ 16% annualized!)
- Risk: Unlimited if SPY moves >$10 (2.2%)
- **Positive expectancy if right about low volatility**

**Option C: Buy Stock and Hold**
- Expose $45,000 capital
- Hope for appreciation
- Collect dividends (maybe 1.5% annually)
- **Much lower return than strangle in sideways market**

**The short strangle is like running an insurance company:**
- Collect many small premiums
- Occasionally pay out large claims
- Profitable if you price risk correctly and manage exposures

**This is why professional option sellers view strangles as "volatility harvesting" or "theta farming."**

---

## Key Terminology

**Strike Width:**

- Distance between put and call strikes
- Wider = lower premium, higher probability of profit
- Narrower = higher premium, lower probability of profit
- Typical: 5-10% OTM on each side

**Delta Selection:**

- Put delta: Usually -0.20 to -0.30
- Call delta: Usually +0.20 to +0.30
- Total delta near zero (delta neutral)
- Determines probability of profit

**Breakeven Points:**

- Lower BE = Put strike - Total credit
- Upper BE = Call strike + Total credit
- Stock must stay between these to profit
- Wider than strike range due to collected premium

**Probability of Profit (POP):**

- Approximate probability both options expire worthless
- Calculated from delta of sold options
- Example: -0.25 delta ≈ 75% POP
- Higher than coin flip, but losses larger when they occur

**Theta Decay:**

- Daily profit from time passing
- Accelerates in last 30 days
- Positive theta (you profit daily if unchanged)
- Main income source for strangle

**Gamma Risk:**

- How delta changes as stock moves
- Negative gamma (short options)
- Small moves don't matter much
- **Large moves accelerate losses exponentially**

---

## Why Sell Short Strangles? (Neutral Strategy)

**Use cases for selling short strangles:**

### 1. Range-Bound Markets

**When stock is expected to stay calm:**

- Trading in established range
- No major catalysts upcoming
- Low volatility environment
- Sideways consolidation

**Example:** SPY consolidating between $440-$460 for weeks

- Historical range visible on chart
- No FOMC meetings, no major earnings
- Sell $435 put / $465 call
- Collect premium from time decay

### 2. Post-Volatility Contraction

**After IV spike, waiting for mean reversion:**

- Stock just had earnings (IV crush)
- Market panic subsiding
- News event passed
- IV percentile dropping

**Example:** AAPL after earnings

- IV was 60%, crushed to 25%
- Stock flat at $175
- Sell $165 put / $185 call
- Profit from continued IV decline

### 3. Income Generation

**Creating cash flow from stagnant holdings:**

- Have bullish stock portfolio
- Market going sideways
- Want extra income beyond dividends
- Willing to accept tail risk

**Example:** Own large cap stocks, market flat

- Sell strangles on SPY or IWM
- Collect 1-3% monthly premium
- Hedge portfolio or just income stream
- **Note: Risks if market crashes or rallies hard**

### 4. High Implied Volatility

**When options are "expensive":**

- IV percentile > 70%
- Options priced for large moves
- You expect calm despite high IV
- Time to "sell premium"

**Example:** VIX at 30, but you expect calm

- Options pricing in 2% daily moves
- You expect 0.5% moves
- Sell strangles to capture inflated premium
- **Risk: Market knows something you don't!**

---

## Strike Selection Strategy

**How to choose your put and call strikes:**

### Delta-Based Selection (Most Common)

**Choose strikes by delta:**

$$
\text{Sell put with delta } \approx -0.20 \text{ to } -0.30
$$

$$
\text{Sell call with delta } \approx +0.20 \text{ to } +0.30
$$

**Why this works:**

- Delta ≈ probability of being ITM at expiration
- -0.25 delta → ~75% chance OTM (expires worthless)
- Balances premium collected vs. risk
- Standard approach for professionals

**Example:** Stock at $100

- -0.25 delta put at $95 (5% OTM)
- +0.25 delta call at $105 (5% OTM)
- Each ≈25% chance of assignment
- Combined ≈50% chance one gets tested

### Standard Deviation Selection

**Use technical analysis:**

$$
\text{Strike} = S_0 \pm 1\sigma\sqrt{T}
$$

Where:
- $S_0$ = Current stock price
- $\sigma$ = Annualized volatility
- $T$ = Time to expiration (years)

**Example:** Stock at $100, IV = 20%, 30 days to expiry

$$
1\sigma \text{ move} = 100 \times 0.20 \times \sqrt{30/365} \approx \$5.73
$$

- Sell $94 put (1 SD below)
- Sell $106 call (1 SD above)
- **68% probability stock stays within range**

### Width Optimization

**Trade premium vs. risk:**

**Narrow strangle (strikes close):**
- More premium collected
- Lower probability of profit
- Breakevens closer to current price
- Better for very low volatility expectations

**Wide strangle (strikes far):**
- Less premium collected  
- Higher probability of profit
- Breakevens farther from current price
- Better when uncertain about volatility

**Example comparison:**

| Configuration | Premium | POP | Max Loss |
|--------------|---------|-----|----------|
| $90/$110 (wide) | $3 | 75% | Unlimited |
| $95/$105 (standard) | $5 | 65% | Unlimited |
| $98/$102 (narrow) | $8 | 50% | Unlimited |

### Expiration Selection

**Time decay curve:**

- **30-45 DTE:** Sweet spot - accelerating theta
- **60-90 DTE:** Slower decay but more premium
- **7-21 DTE:** Maximum decay but gamma risk high
- **Avoid < 7 DTE:** Extreme gamma risk

**Professional approach:**

- Enter at 45 DTE
- Exit at 21 DTE or 50% profit
- Roll if needed
- Never hold to expiration (gamma explosion)

---

## The Greeks: How Short Strangles Behave

**Understanding the forces affecting your position:**

### Delta: Directional Exposure

**Short strangle delta dynamics:**

$$
\Delta_{\text{strangle}} = \Delta_{\text{put}} + \Delta_{\text{call}} \approx 0
$$

**Key characteristics:**

- Initially delta-neutral (∼0 delta)
- Becomes negative if stock rises (short call dominates)
- Becomes positive if stock falls (short put dominates)
- You DON'T want delta - you want stock to stay still!

**Example:** Stock at $100

- Short $95 put: Delta = +0.25 (short put = positive delta)
- Short $105 call: Delta = -0.25 (short call = negative delta)
- **Net delta ≈ 0 (perfectly neutral)**

**What this means:**

- Small stock moves don't affect you much
- You're not betting on direction
- You're betting on NO movement
- Delta risk emerges as stock approaches strikes

### Theta: Time Decay (Your Friend!)

**The primary profit source:**

$$
\Theta_{\text{strangle}} = \Theta_{\text{put}} + \Theta_{\text{call}} > 0
$$

**Key characteristics:**

- Always positive (you profit from time decay)
- Accelerates in last 30 days
- Maximized at-the-money
- This is your INCOME - the reason you sell

**Example decay:**

| Days to Exp | Daily Theta | Weekly Decay |
|------------|-------------|--------------|
| 45 | $10 | $70 |
| 30 | $15 | $105 |
| 21 | $20 | $140 |
| 14 | $30 | $210 |
| 7 | $50 | $350 |

**Strategy:**

- Enter at 30-45 DTE for balance
- Exit at 50% profit or 21 DTE
- Don't get greedy holding to expiration
- **Theta is highest but so is gamma risk near expiry**

### Gamma: Acceleration Risk (Your Enemy!)

**The hidden danger:**

$$
\Gamma_{\text{strangle}} = \Gamma_{\text{put}} + \Gamma_{\text{call}} < 0
$$

**Key characteristics:**

- Always negative (short gamma)
- Means delta accelerates against you on large moves
- Small near strikes initially
- EXPLODES as expiration approaches
- **This is why short strangles can blow up!**

**Example:**

Day 45: Stock moves $2 → Delta changes by $20
Day 7: Stock moves $2 → Delta changes by $100
**Gamma has increased 5x!**

**Why gamma matters:**

- Small moves: Gamma doesn't matter much
- Large moves: Delta accelerates, losses mount exponentially
- Near expiration: A $5 move can turn $500 profit → $2000 loss instantly
- **This is the "picking up pennies in front of steamroller" risk**

### Vega: Volatility Risk (Also Enemy!)

**Short vol exposure:**

$$
\nu_{\text{strangle}} = \nu_{\text{put}} + \nu_{\text{call}} < 0
$$

**Key characteristics:**

- Always negative (short vega)
- You profit when IV decreases
- You lose when IV increases
- **Can lose money even if stock doesn't move!**

**Example:**

- Enter strangle with IV = 20%
- Earnings announced (IV spikes to 40%)
- Stock unchanged at $100
- Your short options now worth 2x more
- **Loss: Maybe $300 on paper even with zero stock movement!**

**Vega scenarios:**

| Event | IV Change | Strangle Impact |
|-------|-----------|-----------------|
| Normal day | 0% | No effect |
| Market calm | -5% | Profit $200 |
| Minor news | +5% | Loss $200 |
| Earnings approach | +20% | Loss $800 |
| Market panic | +50% | Loss $2,000+ |

**Defense:**

- Enter when IV percentile high (50+)
- Avoid earnings dates
- Monitor VIX for market volatility
- Exit if IV spikes unexpectedly
- Use calendar spreads instead if IV too low

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/short_strangle_greeks.png?raw=true" alt="short_strangle_greeks" width="700">
</p>
**Figure 2:** Greeks evolution of short strangle showing positive theta (income), negative gamma (acceleration risk), and negative vega (volatility risk). The Greeks are maximized when stock is between strikes at-the-money.

---

## Management and Adjustments

**What to do when things go wrong (or right):**

### Taking Profits

**Exit strategies when winning:**

**Rule 1: Take 50% profits**
- Position up 50% ($400 credit → close for $200)
- Captures most profit potential
- Avoids late-stage gamma risk
- **Standard professional approach**

**Rule 2: Time-based exit**
- Exit at 21 DTE regardless of profit
- Even if only 25% profit
- Avoids gamma explosion zone
- Re-deploy capital to new position

**Example:**

- Sold strangle for $400 credit
- After 20 days, worth $200 (50% profit)
- **Close position, take $200 profit, move on**
- Don't wait for full $400 - gamma risk not worth it

### Managing Losers

**When stock approaches a strike:**

**Option 1: Roll the tested side**
- Stock approaching $105 call
- Roll call to $110 for additional credit
- Extends duration, gives more room
- **Risk: Can turn small loss into large loss if wrong**

**Option 2: Take the loss**
- Exit at predetermined loss level (100% of credit, or 2x credit)
- Accept defeat, move on
- Prevents catastrophic loss
- **Better to take -$400 loss than risk -$2,000**

**Option 3: Convert to spread**
- Stock at $106, call getting tested
- Buy $110 call to cap risk
- Now have iron condor instead
- **Reduces max loss but costs premium**

**Example management:**

```
Day 1: Sell $95 put / $105 call for $4 credit
Day 10: Stock at $106, call ITM
Options now:
A) Roll $105 call to $110 for $2 credit (total $6 credit now)
B) Take $200 loss, exit position
C) Buy $110 call for $1, cap risk at $5 (iron condor)

Professional choice: Usually B, sometimes C, rarely A
```

### Adjusting for Events

**Handling unexpected catalysts:**

**Earnings announced:**
- Exit immediately if earnings coming up
- IV will spike (negative vega hurts)
- Don't try to "collect a bit more theta"
- **Just exit - not worth the risk**

**Market volatility spike:**
- VIX jumps from 15 to 25
- Your position showing loss even if stock flat
- Consider exiting if IV stays elevated
- Re-enter when IV normalizes

**Dividend announcement:**
- Stock going ex-dividend soon
- Calls may be exercised early
- Adjust or exit to avoid early assignment
- **Synthetic positions can emerge**

---

## Advanced Concepts

### Implied Volatility Rank (IVR)

**When to enter short strangles:**

$$
\text{IVR} = \frac{\text{Current IV} - \text{52-week IV Low}}{\text{52-week IV High} - \text{52-week IV Low}} \times 100
$$

**Strategy:**

- Enter when IVR > 50% (expensive options)
- Ideal when IVR > 70% (very expensive)
- Avoid when IVR < 30% (cheap options)
- **Sell when volatility is elevated, not depressed**

**Example:**

- Stock IV currently 30%
- 52-week range: 15% to 45%
- IVR = (30 - 15) / (45 - 15) = 50%
- **Borderline - could enter but not ideal**

### Expected Move

**Calculating market's expected range:**

$$
\text{Expected Move} = S_0 \times IV \times \sqrt{\frac{T}{365}}
$$

**Use this to set strikes:**

- If expected move is $8
- Current price $100
- Sell $92 put / $108 call (1 SD away)
- You're betting stock moves LESS than expected

**Example:**

- SPY at $450, IV = 16%, 30 days to expiry
- Expected move = $450 × 0.16 × √(30/365) = $12.87
- **Market expects SPY between $437-$463**
- Sell $435/$465 strangle (outside expected range)

### Win Rate vs. Win Size

**The mathematics of short strangles:**

$$
\text{Expected Value} = (P_{\text{win}} \times \text{Avg Win}) - (P_{\text{loss}} \times \text{Avg Loss})
$$

**Typical strangle:**
- Win rate: 65-70%
- Average win: $400
- Average loss: $800
- Expected value: (0.67 × $400) - (0.33 × $800) = $268 - $264 = **+$4**

**Key insight:**

- Win rate is high
- But losses are 2x wins
- Still profitable, but margins thin
- **Must manage losers to maintain edge!**
- One unmanaged blow-up can wipe out 5 winners

### Portfolio Approach

**How professionals trade strangles:**

**Rule: Diversification**
- Never one big position
- 5-10 strangles across different underlyings
- Different expirations (ladder)
- Different sectors

**Example portfolio:**

| Symbol | Strikes | Premium | Days |
|--------|---------|---------|------|
| SPY | 440/460 | $400 | 35 |
| IWM | 190/210 | $300 | 42 |
| QQQ | 360/380 | $350 | 28 |
| TLT | 95/105 | $250 | 38 |
| XLE | 80/90 | $200 | 31 |

**Aggregate metrics:**
- Total credit: $1,500
- Total margin: ~$50,000
- Return: 3% in ~35 days (26% annualized)
- **If one blows up, others offset**

---

## Common Mistakes and How to Avoid Them

### Mistake 1: Selling Strangles Before Earnings

**The error:**
- See juicy premium
- Earnings in 2 weeks
- Think "maybe stock won't move much"
- **IV crush and/or large move destroys position**

**Why it fails:**
- IV inflated due to earnings
- Stock can gap 10-20% overnight
- Even if right on direction, IV crush hurts
- Probability math doesn't work

**Fix:**
- NEVER sell strangles before earnings
- Check earnings calendar before entering
- If earnings coming, wait until after
- **Or use defined-risk strategies like iron condors**

### Mistake 2: Holding to Expiration

**The error:**
- Think "I'll collect every penny of theta"
- Hold position to expiration day
- Gamma explodes, small move causes huge loss

**Why it fails:**
- Gamma goes exponential in last week
- $2 stock move can turn $400 profit → $1,500 loss
- Assignment risk on Friday
- Not worth collecting last $50

**Fix:**
- Exit at 21 DTE or 50% profit
- NEVER hold past 7 DTE
- Book profits and redeploy capital
- **The last 10% of profit has 90% of the risk**

### Mistake 3: Ignoring IV Percentile

**The error:**
- Sell strangles whenever
- Don't check if options cheap or expensive
- Enter when IVR = 10% (very low)

**Why it fails:**
- Premium collected is tiny
- IV likely to rise (mean reversion)
- Negative vega will hurt
- **Expected value is negative**

**Fix:**
- Only enter when IVR > 50%
- Ideal when IVR > 70%
- Use IV rank to time entries
- **Sell expensive options, don't sell cheap options**

### Mistake 4: Undefined Risk

**The error:**
- Don't set stop loss
- "I'll manage it when it happens"
- Let winners turn into losers
- Let losers turn into disasters

**Why it fails:**
- Emotions take over
- "Just one more day" syndrome
- Small loss becomes account-blowing loss
- **Unlimited risk is real!**

**Fix:**
- Set max loss at entry (e.g., 2x credit)
- If loss hits limit, EXIT immediately
- No exceptions, no "just this once"
- **Discipline > Hope**

### Mistake 5: Over-Concentration

**The error:**
- Put 50% of account in one strangle
- "This one is a sure thing"
- Blow up takes out half your capital

**Why it fails:**
- Even 70% probability means 30% failure
- Losses are larger than wins
- No diversification benefit
- **One bad trade destroys account**

**Fix:**
- Max 10% of capital per position
- Diversify across underlyings
- Use different expirations
- **Position sizing is risk management**

---

## Real-World Examples

### Example 1: SPY Range-Bound (Success)

**Setup:**

- SPY at $450, trading in $440-$460 range for 2 months
- IV rank at 60% (elevated due to Fed uncertainty)
- No major catalysts for 30 days
- VIX at 18

**Trade:** 30 DTE short strangle

- Sell $440 put for $3.50 (-0.25 delta)
- Sell $460 call for $3.50 (-0.25 delta)
- Total credit: $7 = $700 per contract

**Outcome:**

- Over next 30 days, SPY oscillated $445-$455
- At 21 DTE, strangle worth $2.00 (71% profit)
- Closed for $500 profit
- **Return: 71% on capital in 9 days ≈ 90% annualized**

**Lesson:** Patience paid off. Exited before gamma risk. Used high IV rank timing.

### Example 2: NVDA Earnings Disaster (Failure)

**Setup:**

- NVDA at $500 before earnings
- IV at 90% (very high)
- Thought "even if it moves, I'll be okay"
- **Ignored earnings risk**

**Trade:** 7 DTE short strangle (before earnings)

- Sell $480 put for $8
- Sell $520 call for $8
- Total credit: $16 = $1,600

**Outcome:**

- Earnings beat, NVDA gapped to $560
- Call worth $40 at open
- Loss: $4,000 - $1,600 = **-$2,400**
- **Loss: 150% of credit (account damaging)**

**Lesson:** NEVER sell strangles before earnings. High IV is a WARNING, not an opportunity. One mistake wiped out multiple wins.

### Example 3: VIX Spike Management (Saved)

**Setup:**

- QQQ at $370, sold $360/$380 strangle
- Collected $600 credit
- Position up $300 after 10 days

**Mid-trade event:**

- Fed surprise announcement
- VIX spiked 15 → 28
- Position now DOWN -$500 (from +$300)
- Stock still at $370 (unchanged!)

**Action:**

- Recognized vega risk
- Exited for -$500 loss
- Avoided potential -$2,000+ if held

**Outcome:**

- Took $500 loss quickly
- Re-entered 2 days later when VIX settled
- **Loss: Controlled, avoided disaster**

**Lesson:** Negative vega is real. Exit when IV spikes unexpectedly. Live to trade another day.

### Example 4: Perfect 50% Profit Exit

**Setup:**

- IWM at $200
- Sold $195/$205 strangle for $800 credit
- 35 DTE

**Management:**

Day 15: Position worth $400 (50% profit)
- Could hold for more theta
- But rule is exit at 50%
- **Took profit, closed position**

Day 35 (hypothetical): 
- IWM dropped to $196
- Original position would have lost -$100
- **By exiting early, locked in $400 instead**

**Lesson:** Discipline beats greed. 50% profit rule works over long term. Don't optimize for one trade, optimize for 100 trades.

---

## Risk Management Rules

**Essential guidelines for trading short strangles:**

### Position Sizing

**Rule of thumb:**

$$
\text{Max Contracts} = \frac{\text{Account Size} \times 0.05}{\text{Margin Required per Contract}}
$$

**Example:**

- $50,000 account
- 5% max risk per trade = $2,500
- Margin per strangle: ~$5,000
- **Max size: Never exceed 1 contract for this account size**

**Professional approach:**
- 5-10% per underlying max
- 50% total account in option selling
- Rest in cash, treasuries, or long stock
- **Never "all in" on one position**

### Stop Loss Rules

**Set before entry:**

- **Max loss: 2x credit received**
  - Collected $500? Stop at -$1,000 loss
  - No exceptions, no "let me see tomorrow"

- **Time-based stop:**
  - Exit at 21 DTE regardless
  - Don't chase last bit of theta
  - Gamma risk not worth it

- **IV-based stop:**
  - If IV spikes >50% from entry, exit
  - Don't fight volatility expansion
  - Re-enter when calmer

### Profit Targets

**Exit when winning:**

- **Standard: 50% profit**
  - Captures most edge
  - Avoids late gamma risk
  - Allows capital redeployment

- **Aggressive: 25% profit**
  - Lower risk tolerance
  - Very short duration
  - Focus on win rate over win size

- **Conservative: 75% profit**
  - Only if IV dropping rapidly
  - Never past 21 DTE
  - Requires strong market edge

### Diversification

**Spread risk across:**

- **Underlyings:** 5-10 different stocks/ETFs
- **Sectors:** Don't concentrate in tech
- **Expirations:** Ladder maturities
- **Strategies:** Mix with spreads, other strategies

**Example portfolio:**

```
25% Short strangles (5 positions)
25% Iron condors (3 positions)
25% Covered calls (stock + calls)
25% Cash or protective puts
```

---

## What to Remember

### Core Concept

**Short strangles sell both tail risks for premium income:**

$$
\text{Short Strangle} = \text{Sell OTM Put} + \text{Sell OTM Call}
$$

- Collect premium upfront from both options
- Profit if stock stays within range
- Maximum profit = Total premium collected
- Maximum loss = Unlimited on both sides
- High probability of profit, but large losses when they occur

### The Setup

**Construction:**

- Sell OTM put (below current price)
- Sell OTM call (above current price)
- Same expiration date
- Both typically -0.20 to -0.30 delta
- Collect total credit immediately

**Example:** Stock at $100
- Sell $95 put for $2 (-0.25 delta)
- Sell $105 call for $2 (-0.25 delta)
- Total credit: $4 = $400 per contract

### The Greeks

**Critical dynamics:**

- **Delta:** ~0 initially (neutral), changes as stock moves
- **Theta:** Positive and large (main profit source)
- **Gamma:** Negative (acceleration risk on large moves)
- **Vega:** Negative (lose if IV increases)

**You win from: Time decay (theta) and volatility decrease**
**You lose from: Large stock moves (gamma) and volatility increase (vega)**

### Strike Selection

**Three approaches:**

1. **Delta-based:** -0.25 delta on each side (standard)
2. **Standard deviation:** 1 SD from current price
3. **Technical:** Support/resistance levels

**Width tradeoff:**
- Wider strikes: Less premium, higher POP
- Narrower strikes: More premium, lower POP
- Sweet spot: 5-10% OTM on each side

### Expiration Selection

**Optimal timeframes:**

- **Entry: 30-45 DTE** (sweet spot for theta vs. gamma)
- **Exit: 21 DTE or 50% profit** (whichever first)
- **Avoid: <7 DTE** (gamma explosion risk)
- **Avoid: >60 DTE** (theta too slow)

### Maximum Profit/Loss

**Profit/Loss profile:**

- **Max profit:** Total premium collected (limited)
- **Max loss:** Unlimited on both sides
- **Breakevens:** 
  - Lower: Put strike - Total credit
  - Upper: Call strike + Total credit

**Example:**
- Credit: $4
- Strikes: $95 put / $105 call
- Lower BE: $91
- Upper BE: $109
- Profit zone: $91 to $109

### When to Use

**Sell short strangles when:**

- IV percentile > 50% (options expensive)
- Stock in defined range (support/resistance)
- Low volatility expected (post-event)
- No earnings or catalysts coming
- Want income from neutral view

**Don't use when:**

- Earnings approaching (IV spike + gap risk)
- Market turbulent (VIX > 30)
- IV percentile < 30% (options cheap)
- Uncertain about direction
- Can't handle unlimited risk

### Common Mistakes to Avoid

1. Selling before earnings (IV spike + gap destroys)
2. Holding to expiration (gamma explosion)
3. Ignoring IV rank (selling cheap options)
4. No stop loss (unlimited risk is real)
5. Over-concentration (one blow-up destroys account)
6. Chasing last bit of theta (not worth gamma risk)
7. Not diversifying (need multiple positions)
8. Fighting volatility spikes (exit when IV jumps)

### Risk Management

**Essential rules:**

- **Position size:** Max 5-10% of account per position
- **Stop loss:** Exit at 2x credit received
- **Profit target:** Take 50% profit or exit at 21 DTE
- **Diversification:** 5-10 positions across different underlyings
- **IV timing:** Only enter when IVR > 50%
- **No earnings:** Never sell strangles before binary events

### Comparison to Other Strategies

**vs. Iron Condor:**
- Strangle: More premium, unlimited risk
- Iron Condor: Less premium, defined risk
- Use condor when risk management priority

**vs. Short Straddle:**
- Strangle: Lower premium, higher POP
- Straddle: Higher premium, lower POP
- Strangle less aggressive

**vs. Long Stock:**
- Strangle: Income in sideways market
- Stock: Capital appreciation if bullish
- Strangle better for range-bound

### Your Learning Path

**Progression:**

1. Master short puts and calls first
2. Try iron condors (defined risk version)
3. Graduate to short strangles (once comfortable with risk)
4. Combine with other strategies for portfolio

**Short strangles are INTERMEDIATE level - need discipline and risk management!**

### Final Wisdom

> "Short strangles are high-probability income strategies that profit from time decay and low volatility. But unlimited risk on both sides means one unmanaged blow-up can wipe out months of profits. Success requires: timing entries with high IV rank, taking profits at 50%, strict stop losses, and diversification. This is not 'passive income' - it's active volatility harvesting that demands discipline and proper risk management. Done right, it can generate consistent returns. Done wrong, it can destroy your account."

**Key to success:**

- High IV rank entries only (IVR > 50%)
- Take 50% profits religiously
- Stop loss at 2x credit (no exceptions)
- Diversify across 5-10 positions
- Never hold past 21 DTE
- Avoid earnings and catalysts
- Manage negative vega and gamma risk

**Most important:** Short strangles are tools, not magic. They work in specific market conditions (low volatility, range-bound) and fail in others (high volatility, trending). Know when to use them and when to step aside! 🎯📈
