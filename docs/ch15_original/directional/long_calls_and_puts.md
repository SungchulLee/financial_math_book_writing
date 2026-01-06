# Long Calls and Puts

**Long calls and puts** are the simplest option strategies 
where you buy the right (but not the obligation) to purchase (call) or sell (put) a stock at a predetermined price, 
giving you directional exposure with limited downside risk.

---

## The Core Insight

**The fundamental idea:**

- Stocks can go up or down (or sideways)
- You want directional exposure (bullish or bearish)
- But don't want unlimited downside risk
- Options give you leverage with limited loss
- Pay premium upfront, max loss is that premium
- Profit can be unlimited (calls) or substantial (puts)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/long_call_vs_put.png?raw=true" alt="long_call_vs_put" width="700">
</p>
**Figure 1:** Profit/loss comparison between long calls and long puts, 
showing symmetric payoff structures with limited downside (premium paid) and unlimited (calls) or substantial (puts) upside potential.

**You're essentially betting: "The stock will move significantly in my direction, more than the premium I'm paying."**

---

## What Are Calls and Puts?

### 1. Leverage

**Control more shares with less capital:**

### 2. Portfolio Hedge (Insurance)

**Protect stock portfolio from crash:**

**Definition:** The right (not obligation) to BUY stock at strike price $K$ by expiration date $T$.

**When you buy a call:**

- You pay premium upfront
- You control 100 shares per contract
- You profit if stock goes UP above strike + premium
- Max loss = premium paid
- Max profit = unlimited

### 3. Cheaper Than Shorting

**Bearish play without margin:**

**Definition:** The right (not obligation) to SELL stock at strike price $K$ by expiration date $T$.

**When you buy a put:**

- You pay premium upfront
- You control 100 shares per contract
- You profit if stock goes DOWN below strike - premium
- Max loss = premium paid
- Max profit = strike - premium (stock can't go below $0)

### 4. Theta (Θ): Time Decay

**How much option loses per day (all else equal):**

**The deep insight:**

A call option is economically equivalent to a **leveraged stock purchase with automatic bankruptcy protection**. When you buy a call, you're essentially:

1. **Borrowing money** to buy the stock (at strike $K$)
2. **Buying the stock** with that borrowed money
3. **Getting automatic exit** if the stock crashes (limited liability)
4. **Selling at maturity** or whenever you choose

**Formal decomposition:**

$$
\underbrace{\text{Long Call}}_{\text{Premium } C} \quad\equiv\quad \underbrace{\text{Stock}}_{\text{Current Price } S} +\quad \underbrace{\text{Borrow}}_{\text{Strike } K} \quad+\quad \underbrace{\text{Put Protection}}_{\text{Downside Insurance}}
$$

**Why this matters:**

**Traditional leverage (margin):**

- Borrow $15,000, buy 100 shares at $150
- If stock → $50, you lose $10,000 AND still owe the loan
- **Potential for catastrophic loss beyond your capital**

**Call option (leveraged with protection):**

- Pay $800 premium for $150 call
- If stock → $50, you simply walk away
- **Maximum loss: $800 (the premium)**

**The premium you pay ($8) is the cost of this "limited liability feature" - the automatic stop-loss built into the contract.**

**Similarly, a put option is:**

$$
\underbrace{\text{Long Put}}_{\text{Premium } P} \quad\equiv\quad \underbrace{\text{Short Stock}}_{\text{Sell at } K} \quad+\quad \underbrace{\text{Call Protection}}_{\text{Upside Insurance}}
$$

**Traditional shorting:**

- Borrow stock, sell at $100
- If stock → $200, you must buy back at $200
- **Loss: $100 per share (unlimited potential)**

**Put option:**

- Pay $5 premium for $100 put
- If stock → $200, you walk away
- **Loss: $5 per share (premium only)**

**The put premium is the cost of capping your upside risk when betting on downside.**

### 5. Put-Call Parity

**The most important equation in options:**

$$
C + Ke^{-rT} = S + P
$$

Where:

- $C$ = Call premium
- $K$ = Strike price
- $r$ = Risk-free rate
- $T$ = Time to expiration
- $S$ = Stock price
- $P$ = Put premium

**Rearranging to see the financing structure:**

$$
C = S - Ke^{-rT} + P
$$

**Translation:**

$$
\text{Call} \quad = \underbrace{\text{Stock}}_{\text{Long position}} - \quad\underbrace{\text{Present Value of Strike}}_{\text{Borrowed money}}\quad + \underbrace{\text{Put}}_{\text{Downside protection}}
$$

**This is EXACTLY the "borrow + buy stock + insurance" interpretation!**

### 6. Why This Matters

**Understanding options as financing structures helps you:**

1. **Compare to alternatives:**

      - Should I buy stock on margin or buy calls?
      - Should I short stock or buy puts?
      - **Options = Leverage + Automatic Risk Control**

2. **Understand premium pricing:**

      - Premium = Cost of leverage + Cost of limited liability
      - Higher strikes (more leverage) → Higher cost
      - Longer time → More insurance cost

3. **See synthetic positions:**

      - Long stock + Long put = Long call (economically identical)
      - Short stock + Long call = Long put (economically identical)

4. **Recognize arbitrage opportunities:**

      - If put-call parity violated → Free money!
      - Market makers constantly monitor this

### 7. Strategic Advantage

**Why traders prefer options over pure leverage:**

**Scenario: Bullish on AAPL, want 100-share exposure**

**Option A: Margin Trading**

- Borrow $7,500 (50% margin)
- Buy 100 shares at $150
- Your capital: $7,500
- Margin interest: ~8% annually
- **Risk: Margin call if stock drops, potential loss exceeds capital**

**Option B: Call Options**

- Buy 1 ATM call for $8 ($800 total)
- Your capital: $800
- No margin interest
- **Risk: Maximum loss = $800, cannot exceed**

**The call option is like getting a non-recourse loan:**

- If stock crashes, lender (option seller) bears the tail risk
- You pay upfront premium instead of ongoing interest
- No margin calls, no liquidation risk
- **Predefined, capped maximum loss**

**This is why sophisticated investors view options as "strategic financing vehicles with embedded risk management."**

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
- $10,000 in stock: 67 shares at $150
- $10,000 in calls: 12 contracts = 1,200 shares of exposure!
- **18x leverage**

**Trade-off:**

- More upside potential
- But options expire (time decay)
- Need to be right on timing AND direction

### 2. Limited Downside

**Protect against catastrophic loss:**

- Downside risk is limited to the premium paid (see **The Core Insight**).

### 3. Earnings/Event Play

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
- Own $100,000 stock portfolio (SPY)
- Worried about downturn
- Buy OTM puts for $2,000 (2%)

**If market crashes 20%:**

- Portfolio value: $80,000 (-$20,000)
- Puts gain: ~$18,000
- **Net loss: $4,000 (4%) instead of 20%**

**This is how pros hedge!**

- Shorting requires margin account
- Unlimited loss potential
- Borrowing costs
- **Puts: No margin, defined risk, similar upside**

### 2. Cannot Short

**Some stocks hard to borrow:**

- Heavily shorted already
- Small cap with low float
- Recent IPO
- **Puts are the alternative**

---

## The Greeks (Simplified)

### 1. Delta (Δ): Directional

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


**All long options have negative theta:**

- You pay theta every day
- Accelerates near expiration
- ATM options have highest theta

**Example:**

- Buy call with Θ = -$0.10/day
- After 10 days (stock unchanged): lost $1
- Last 30 days: decay accelerates significantly

**Time decay curve:**

**Key insight:** Theta accelerates as you approach expiration!

### 2. Vega (ν): Volatility Exposure

**How much option price changes per 1% change in implied volatility:**

**All long options have positive vega:**

- Options gain value when IV rises
- Options lose value when IV falls (IV crush)
- ATM options have highest vega

**Example:**

- Buy call with ν = +0.30
- IV rises from 20% → 30% (+10%)
- Call gains: 0.30 × 10 = $3 per share

**Critical concept: IV crush**

- Before earnings: IV = 60%, call costs $10
- After earnings: IV = 30%, even if stock flat
- Call now worth $6 (40% loss from IV alone!)

### 3. Gamma (Γ): Delta Sensitivity

**How much delta changes per $1 stock move:**

**Long options have positive gamma:**

- Delta increases as stock moves in your favor
- Delta decreases as stock moves against you
- ATM options have highest gamma

**Example:**

- Buy call with Δ = 0.40, Γ = 0.05
- Stock rises $5
- New delta: 0.40 + (0.05 × 5) = 0.65
- Now more sensitive to further moves!

---

## Strike Selection (Critical!)

**Choosing the right strike determines your payoff profile:**

### 1. ITM Calls/Puts

**Characteristics:**

- **Higher premium** (has intrinsic value)
- **Higher delta** (0.70-0.90) - moves almost with stock
- **Lower leverage** - less bang for buck
- **Lower risk** - less likely to expire worthless
- **Better for:** Conservative plays, stock replacement

**Example (Stock at $100):**

- Buy $90 ITM call for $12
- Delta = 0.80
- Behaves like 80 shares of stock
- Stock to $110 → call to $20 (67% gain)

### 2. ATM Calls/Puts

**Characteristics:**

- **Moderate premium**
- **Delta ≈ 0.50** - balanced directional exposure
- **Highest theta** - most time decay
- **Highest gamma** - most sensitive to moves
- **Highest vega** - most IV exposure
- **Better for:** Standard directional play, balanced approach

**Example (Stock at $100):**

- Buy $100 ATM call for $5
- Delta = 0.50
- Stock to $110 → call to $10 (100% gain)
- **Lowest premium** (cheap!)
- **Low delta** (0.20-0.40) - needs big move
- **Highest leverage** - huge % gains if right
- **High risk** - likely to expire worthless
- **Better for:** Lottery tickets, defined small risk, huge potential

**Example (Stock at $100):**

- Buy $110 OTM call for $1
- Delta = 0.25
- Stock needs to reach $111 just to break even!
- Stock to $120 → call to $10 (900% gain!)
- But 75% chance expires worthless

### 3. The Trade-off

**Strike selection is probability vs. payout:**

$$
\text{High Probability (ITM)} \leftrightarrow \text{Low Leverage}
$$

$$
\text{Low Probability (OTM)} \leftrightarrow \text{High Leverage}
$$

**Beginner recommendation: Start with ATM (balanced approach)**

---

## Time Selection (Crucial!)

### 1. Short-Term (<1 month)

**Pros:**

- Cheap premium
- High leverage if you're right quickly

**Cons:**

- Massive theta decay
- Very little room for error
- Stock must move NOW

**Use when:**

- Immediate catalyst (earnings this week)
- High conviction on timing
- Small position size (high risk)

**Example:**

- Buy 2-week call for $0.50
- Theta = -$0.10/day (20% per day!)
- Need immediate move or lose fast

### 2. Medium-Term (1-3 months)

**Pros:**

- Reasonable premium
- Moderate theta decay
- Time for thesis to play out
- Most liquid

**Cons:**

- More expensive than short-term
- Still significant theta

**Use when:**

- Catalyst in 1-2 months
- Normal directional bet
- Standard approach

**Example:**

- Buy 60-day call for $5
- Theta = -$0.05/day (1% per day)
- Balanced risk/reward

**This is the sweet spot for most traders!**

### 3. Long-Term (3+ months)

**LEAPS = Long-term Equity Anticipation Securities (1-2 years out)**

**Pros:**

- Lots of time to be right
- Lower theta per day
- Can use as stock substitute
- Less timing pressure

**Cons:**

- Expensive premium (high capital)
- Lower leverage
- Opportunity cost

**Use when:**

- Long-term bullish/bearish thesis
- Want stock exposure with less capital
- Can afford to wait

**Example:**

- Buy 1-year call for $20
- Theta = -$0.02/day (0.1% per day)
- Acts like leveraged stock position

---

## When NOT to Buy Calls/Puts

### 1. High IV Environment

**Problem:**

- Options overpriced
- Vega will hurt you when IV normalizes
- Even if stock moves your way, IV crush can negate gains

**Example:**

- Stock at $100, IV at 80% (very high)
- Buy $100 call for $12
- Stock rises to $105
- But IV drops to 40%
- Call worth only $7 (lost money despite being right!)

**Solution:** Wait for IV to drop, or sell premium instead

### 2. Sideways Market

**Problem:**

- Long options need movement
- theta decay accumulates each day (see **Theta (Θ)**)
- Stock going nowhere = you lose

**Example:**

- Buy call expecting rally
- Stock trades $98-$102 for 30 days
- Theta decay: -$0.08/day × 30 = -$2.40
- Lost $2.40 despite stock being "near" your strike

**Solution:** Use neutral strategies (iron condors) or stay in stock

### 3. No Catalyst

**Problem:**

- Random hoping stock moves
- No reason for movement = theta bleeds
- You're just gambling

**Example:**

- "Stock at $50 feels cheap, I'll buy calls"
- No earnings, no news, no reason for move
- Stock stays $50, you lose to theta

**Solution:** Only trade around catalysts (earnings, FDA, etc.)

### 4. Long-Term Hold

**Problem:**

- Options expire
- Theta compounds over time
- Stock might take years to reach target

**Example:**

- Stock at $100, you think it hits $150 in 2 years
- Buy 3-month calls repeatedly
- Stock slowly grinds to $150 over 24 months
- You lose money on every option that expires
- Would've been better in stock or 2-year LEAPS

**Solution:** Use stock or deep ITM LEAPS (1-2 years)

### 5. Already Priced In

**Problem:**

- Everyone knows the catalyst
- IV already elevated
- Move already priced into option

**Example:**

- AAPL earnings tomorrow
- Everyone bullish, IV at 60%
- Stock beats but only rises 3%
- IV crashes to 25%
- Calls lose value despite positive news

**Solution:** Enter 1-2 weeks before event when IV still low

---

## Advanced Considerations

### 1. IV Percentile

**Before buying ANY option, check IV percentile:**

**What it is:**

- Where current IV ranks historically (0-100%)
- IV Percentile = % of days in past year IV was lower

**Interpretation:**

- <25%: IV is cheap (good for buying)
- 25-75%: IV is normal
- \>75%: IV is expensive (bad for buying, good for selling)

**Example:**

- Stock's IV = 40%
- IV percentile = 85%
- **This is expensive! Only 15% of days had higher IV**
- **Don't buy options here, they're overpriced**

**Where to check:** Most broker platforms show IV rank/percentile

### 2. Position Sizing Math

**Calculate position size based on risk:**

**Formula:**

$$
\text{Number of Contracts} = \frac{\text{Dollar Risk per Trade}}{\text{Premium per Contract}}
$$

**Example:**

- Account size: $50,000
- Risk per trade: 2% = $1,000
- Option premium: $5/share = $500/contract
- **Max contracts: 2**

**This ensures no single trade wipes you out!**

### 3. Adjusting Positions

**What to do when trade moves against you:**

**Option 1: Accept Loss**

- Stock moved wrong way
- Thesis invalidated
- **Best choice:** Exit, take loss, move on
- **Don't:** Hold hoping for miracle

**Option 2: Roll Out**

- Stock moved slowly, need more time
- Roll = Close current, open longer-dated
- **Only if:** Thesis still valid, just need time
- **Cost:** Additional premium

**Example:**

- Bought 30-day $100 call for $5
- 20 days passed, stock at $98
- Sell call for $2 (loss $3)
- Buy 60-day $100 call for $6
- Net cost: $4 more
- **Only do if confident stock will move!**

**Option 3: Add to Winner**

- Stock moving your way
- Delta increasing (positive gamma)
- **Can add:** Small additional position
- **Risk:** Concentration, timing

### 4. The Greeks in Action

**Real scenario showing all Greeks:**

**Setup:**

- Stock at $100
- Buy $100 call, 30 days out
- Premium: $5
- Delta = +0.50, Theta = -$0.08, Vega = +0.15, Gamma = +0.03
- IV = 30%

**Scenario 1: Stock rises to $105**

- Profit from delta: +0.50 × $5 = +$2.50
- New delta (gamma): 0.50 + (0.03 × 5) = 0.65
- Call now worth ~$7.50 (50% gain)

**Scenario 2: Stock unchanged, 10 days pass**

- Loss from theta: -$0.08 × 10 = -$0.80
- Call now worth ~$4.20 (16% loss)

**Scenario 3: Stock unchanged, IV spikes to 50%**

- Gain from vega: +0.15 × 20 = +$3.00
- Call now worth ~$8.00 (60% gain)
- **This is why options spike before earnings!**

**Scenario 4: Stock up $2, IV drops to 20%, 5 days pass**

- Gain from delta: +0.50 × $2 = +$1.00
- Loss from vega: +0.15 × (-10) = -$1.50
- Loss from theta: -$0.08 × 5 = -$0.40
- **Net: -$0.90 (lost money despite stock rising!)**
- **This is IV crush in action**

---

## Common Mistakes

### 1. Buying OTM Lottery Tickets

- **Mistake:** Consistently buying far OTM options because "they're cheap"
- **Why it fails:** Low delta (0.10-0.20), stock needs 20%+ move, 80%+ lose money
- **Fix:** Buy ATM or slightly OTM (delta 0.40-0.50)
- **Counter-Strategy:** **Sell far OTM premium** - collect from those buying lottery tickets (e.g., sell OTM calls/puts in low-volatility environments)

### 2. Holding Through Expiration

- **Mistake:** "Diamond hands" - holding losing options hoping for miracle
- **Why it fails:** Time decay accelerates, 99% expire worthless
- **Fix:** Set stop loss (-50%), exit early if wrong
- **Counter-Strategy:** **Sell theta in final 30 days** - when decay is steepest, sell options to those holding too long

### 3. Ignoring IV (IV Blindness)

- **Mistake:** Buying options without checking IV percentile
- **Why it fails:** Overpay when IV high, lose to IV crush
- **Fix:** Check IV percentile, only buy when <50%
- **Counter-Strategy:** **Sell high IV options** - when IV percentile >75%, sell premium to those buying expensive options (e.g., sell spreads, iron condors during earnings season)

### 4. Over-Leveraging

- **Mistake:** "I can control 1000 shares for $5,000!" (using entire account)
- **Why it fails:** One bad trade = account blown up
- **Fix:** Risk only 2-5% per trade, position sizing discipline
- **Counter-Strategy:** **Fade over-leveraged retail** - when open interest spikes dramatically in one direction, consider the opposite side

### 5. Trading Illiquid Options

- **Mistake:** Buying options with wide bid/ask ($2.00 bid, $2.40 ask)
- **Why it fails:** Lose 20% instantly to spread, can't exit cleanly
- **Fix:** Only trade volume >100, tight spreads (<10%)

### 6. Buying Before Earnings

- **Mistake:** "Stock will beat earnings, I'll buy calls today!"
- **Why it fails:** IV already elevated, crushes even if you're right
- **Fix:** Buy 1-2 weeks before (IV still low) or after (IV crushed)
- **Counter-Strategy:** **Sell options right before earnings** - collect from those buying into elevated IV, let IV crush work for you (sell iron condors or credit spreads)

### 7. Chasing After Big Moves

- **Mistake:** Stock up 15% → "I'll buy calls, momentum!" (FOMO)
- **Why it fails:** Often buying the top, IV spiked, theta high
- **Fix:** Wait for pullback, let IV settle
- **Counter-Strategy:** **Sell to FOMO buyers** - after parabolic moves, sell calls to late chasers; after panic drops, sell puts to late bears

### 8. No Catalyst Trading

- **Mistake:** "Stock looks cheap, I'll buy calls" (no reason why)
- **Why it fails:** FOMO entry, buying tops
- **Fix:** Have thesis before trade, stick to plan
- **Counter-Strategy:** **Fade the move** - sell options to panicking buyers after large moves (e.g., sell calls after parabolic rallies, sell puts after panic drops when IV spikes)

### 9. Confusing Probability

- **Mistake:** "I'm up 100%, this always works!"
- **Why it fails:** One big win doesn't mean skill, could be luck
- **Fix:** Track all trades, understand win rate needed

### 10. No Exit Plan

- **Mistake:** Enter trade without profit target or stop loss
- **Why it fails:** Hold too long (theta) or panic sell bottoms
- **Fix:** Set targets: exit at 50% profit, -50% loss

---

## Risk Management Rules

### 1. Position Sizing

**Rule of thumb:**

$$
\text{Position Size} = \frac{\text{Risk Capital} \times 0.02}{\text{Option Premium}}
$$

**Example:**

- $50,000 account
- 2% risk per trade = $1,000
- Option costs $5/share = $500/contract
- **Max size: 2 contracts**

### 2. Diversification

**Don't concentrate:**

- Max 5-10% of portfolio in options
- Max 2-5% per trade
- Spread across multiple positions
- Different sectors, timeframes

### 3. Exit Rules

**Set upfront:**

- **Take profit:** 50-100% gain
- **Stop loss:** -50% loss (don't hold to zero)
- **Time stop:** Exit if 50% of time passed with no move
- **IV exit:** Exit on IV spike even if stock flat

### 4. Avoid These

- Never "double down" on losing position
- Never "roll down and out" hoping for recovery (usually fails)
- Never risk more than 5% on single trade
- Never trade illiquid options (vol < 100)
- Never buy day before earnings (IV crush)

---

## Real-World Examples

### 1. AAPL (Sept 2023)

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

### 2. TSLA (Oct 2023)

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

### 3. COVID (Feb 2020)

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

### 4. Small Cap Biotech

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

## Practical Steps

**Step-by-step implementation framework:**

### Step 1: Market Assessment

**Before entering, evaluate:**

1. **Market environment:**

      - Overall trend direction (bull/bear/sideways)
      - Sector rotation and momentum
      - Market volatility level (VIX)

2. **Stock-specific analysis:**

      - Technical setup (support/resistance)
      - Fundamental catalyst (earnings, FDA, product launch)
      - Volume and liquidity (>100 daily option volume)

3. **Timing considerations:**

      - Time until catalyst (weeks, not months)
      - Current position in cycle
      - Macro backdrop (Fed, geopolitics)

### Step 2: Strategy Selection

**Enter long calls when:**

- Strong bullish catalyst identified within 1-2 months
- IV rank < 50% (options not overpriced)
- Technical confirmation (breakout, bounce off support)
- Clear risk/reward setup
- Strong volume and momentum
- Sector tailwind present

**Enter long puts when:**

- Bearish catalyst imminent (negative earnings, regulations)
- IV rank < 50% (not expensive)
- Technical breakdown confirmed
- Need portfolio hedge
- Overvalued fundamentals
- Sector weakness

**Avoid this strategy when:**

- No clear catalyst (random directional bet)
- IV rank > 70% (options very expensive)
- Earnings tomorrow (IV crush risk)
- Illiquid options (wide bid-ask)
- More than 3 months needed for thesis
- Unclear conviction

### Step 3: Position Sizing

**Calculate maximum position size:**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times 0.02}{\text{Premium Per Contract}}
$$

**Conservative guidelines:**

- Risk 1-2% per trade when learning
- Max 3-5% on high-conviction trades
- Never more than 10% of portfolio in options total
- Start with 1 contract to learn

**Example:**

- $50,000 portfolio
- 2% risk = $1,000
- Option premium: $500/contract

- **Max size: 2 contracts**

### Step 4: Entry Execution

**Best practices:**

1. **Strike selection:**

      - Beginners: Start with ATM (delta ~0.50)
      - Experienced: OTM for leverage (delta 0.30-0.40)
      - Conservative: Slightly ITM (delta 0.60-0.70)

2. **Time selection:**

      - Minimum 60 days to expiration (DTE)
      - Ideal: 60-90 DTE for catalyst trades
      - LEAPS: 6+ months for stock substitute

3. **IV check:**

      - Use IV rank or percentile
      - Prefer IVR < 50% (not expensive)
      - Avoid IVR > 70% (overpriced)

4. **Order execution:**

      - Use limit orders (never market)
      - Bid-ask spread < 10% of mid-price
      - Avoid first/last 30 minutes of day
      - Check option volume > 100 daily

### Step 5: Position Management

**Active management rules:**

**Profit targets:**

- Take 50% profit on quick moves (days)
- Take 100% profit if achieved smoothly
- Scale out: Half at 50%, let rest run
- Don't be greedy beyond 100-150% gain

**Loss limits:**

- Exit at -50% loss (hard stop, non-negotiable)
- Exit if stock breaks key support/resistance
- Exit if thesis invalidated
- Never let options go to zero hoping for miracle

**Time-based exits:**

- Exit if 50% of time elapsed with no progress
- Exit if 2 weeks before expiration with no move
- Don't hold through expiration unless deep ITM

### Step 6: Adjustment Protocols

**When to adjust:**

- Position down 30-50% (decision point)
- Thesis still valid but timing off
- Stock moving but too slowly
- IV spike hurts position

**How to adjust:**

- **Roll out:** Extend expiration, same strike (costs premium)
- **Roll out and down/up:** Extend time, improve strike (costs more)
- **Add to winner:** Scale in if thesis playing out
- **Take loss and re-enter:** Often better than rolling

**When to take loss instead:**

- Down more than 50% (cut it)
- Thesis invalidated (catalyst failed, broke support)
- Better opportunity elsewhere
- IV spiked making rolls expensive
- Less than 30 DTE remaining

### Step 7: Record Keeping

Track every trade:

- Entry/exit dates and prices
- Strike, expiration, premium paid
- Rationale: What was the catalyst?
- Market conditions: IV rank, stock technicals
- P&L and what you learned
- Mistakes made (for improvement)

### Common Execution Mistakes

1. **Not checking IV before buying** (pay too much)
2. **Buying options too close to expiration** (theta kills)
3. **Ignoring liquidity** (wide spreads eat profits)
4. **Over-sizing positions** (one loss devastates)
5. **No stop loss discipline** (holding losers to zero)
6. **Buying day before earnings** (IV crush destroys)
7. **Trading without catalyst** (random directional bets lose)
8. **Fighting the trend** (catching falling knives)

---

## Final Wisdom

> "Long calls and puts are the simplest option strategies, but don't mistake simple for easy. They require you to be right on BOTH direction and timing, and theta decay is relentless. Use them for high-conviction, short-term directional bets with defined risk. Master these before attempting any complex strategies. If you can't make money with simple long options, you won't make money with complex spreads either."

**Key to success:**

- High-conviction trades only
- Proper position sizing (2-5% max)
- Exit discipline (take profits, cut losses)
- Understand Greeks (especially theta and delta)
- Check IV before entering (avoid expensive options)
- Have catalyst (don't just hope)