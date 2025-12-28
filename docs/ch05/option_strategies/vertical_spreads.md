# Vertical Spreads

**Vertical spreads** are directional option strategies where you simultaneously buy and sell options of the same type (both calls or both puts) at different strike prices but the same expiration date, creating defined risk and defined reward.

---

## The Core Insight

**The fundamental idea:**

- Single options have unlimited risk (if selling) or 100% loss (if buying)
- What if you could limit BOTH sides?
- Buy one option, sell another at different strike
- Create "spread" between strikes
- Defined maximum profit AND maximum loss
- Much safer than naked options

**The key equation:**

$$
\text{Max Risk} = \text{Spread Width} - \text{Credit Received (or + Debit Paid)}
$$

$$
\text{Max Reward} = \text{Spread Width} - \text{Max Risk}
$$

**You're essentially betting: "Stock will move in my direction, but I'll give up extreme moves to limit risk."**

---

## Types of Vertical Spreads

**Four main types:**

### 1. Bull Call Spread (Debit Spread)

**Bullish, pay net debit**

**Structure:**

- BUY lower strike call
- SELL higher strike call
- Same expiration
- Net debit (pay money)

**Example:**

- Stock at $100
- Buy $100 call for $5
- Sell $110 call for $2
- **Net cost: $3 (debit)**

**Max profit:** $110 - $100 - $3 = $7

**Max loss:** $3 (debit paid)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/bull_call_spread.png?raw=true" alt="Bull Call Spread" width="700">
</p>
**Figure 1:** Bull call spread profit/loss diagram showing the defined risk-reward profile of buying a lower strike call and selling a higher strike call, illustrating capped profit potential and limited downside.

### 2. Bear Put Spread (Debit Spread)

**Bearish, pay net debit**

**Structure:**

- BUY higher strike put
- SELL lower strike put
- Same expiration
- Net debit (pay money)

**Example:**

- Stock at $100
- Buy $100 put for $5
- Sell $90 put for $2
- **Net cost: $3 (debit)**

**Max profit:** $100 - $90 - $3 = $7

**Max loss:** $3 (debit paid)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/bear_put_spread.png?raw=true" alt="Bear Put Spread" width="700">
</p>
**Figure 2:** Bear put spread profit/loss diagram demonstrating the bearish strategy with defined risk, showing how buying a higher strike put and selling a lower strike put creates a capped profit structure.

### 3. Bull Put Spread (Credit Spread)

**Bullish, receive net credit**

**Structure:**

- SELL higher strike put
- BUY lower strike put
- Same expiration
- Net credit (receive money)

**Example:**

- Stock at $100
- Sell $100 put for $5
- Buy $90 put for $2
- **Net credit: $3**

**Max profit:** $3 (credit received)

**Max loss:** $100 - $90 - $3 = $7

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/bull_put_spread.png?raw=true" alt="Bull Put Spread" width="700">
</p>
**Figure 3:** Bull put spread profit/loss diagram illustrating the credit spread structure where selling a higher strike put and buying a lower strike put generates immediate income with defined maximum loss.

### 4. Bear Call Spread (Credit Spread)

**Bearish, receive net credit**

**Structure:**

- SELL lower strike call
- BUY higher strike call
- Same expiration
- Net credit (receive money)

**Example:**

- Stock at $100
- Sell $100 call for $5
- Buy $110 call for $2
- **Net credit: $3**

**Max profit:** $3 (credit received)

**Max loss:** $110 - $100 - $3 = $7

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/bear_call_spread.png?raw=true" alt="Bear Call Spread" width="700">
</p>
**Figure 4:** Bear call spread profit/loss diagram showing the bearish credit spread payoff, demonstrating how selling a lower strike call and buying a higher strike call creates income with capped risk.

---

## Why Vertical Spreads Exist

### 1. Define Risk

**Problem with naked options:**

- Sell naked call → unlimited loss
- Buy single call → 100% loss possible

**Solution with spreads:**

- Defined max loss on both sides
- Can't lose more than spread width
- Sleep better

### 2. Reduce Cost

**Problem:**

- ATM calls expensive ($8)
- Hard to afford many

**Solution:**

- Bull call spread costs only $3
- Can do 2-3x more trades
- Better capital efficiency

### 3. Lower Probability Required

**Single call:**

- Need stock to move from $100 to $108+ to profit

**Bull call spread ($100/$110 for $3):**

- Only need stock above $103 to profit
- Lower bar = higher probability

### 4. Better Risk/Reward in Some Scenarios

**Selling credit spreads:**

- Collect premium immediately
- High win rate (60-70%)
- Defined risk (unlike naked)
- Professional approach

---

## The Portfolio Structures

### Bull Call Spread

$$
\Pi = C(K_1) - C(K_2) \quad \text{where } K_1 < K_2
$$

**At expiration:**

$$
\text{P&L} = \begin{cases}
-\text{Debit} & S \leq K_1 \\
(S - K_1) - \text{Debit} & K_1 < S < K_2 \\
(K_2 - K_1) - \text{Debit} & S \geq K_2
\end{cases}
$$



### Bear Put Spread

$$
\Pi = P(K_2) - P(K_1) \quad \text{where } K_2 > K_1
$$

**Symmetrical to bull call spread, just puts**

### Bull Put Spread (Credit Spread)

$$
\Pi = -P(K_2) + P(K_1) \quad \text{where } K_2 > K_1
$$

**At expiration:**

$$
\text{P&L} = \begin{cases}
\text{Credit} & S \geq K_2 \\
\text{Credit} - (K_2 - S) & K_1 < S < K_2 \\
\text{Credit} - (K_2 - K_1) & S \leq K_1
\end{cases}
$$



---

## Debit vs. Credit Spreads

**Key comparison:**

| Aspect | Debit Spread | Credit Spread |
|--------|--------------|---------------|
| **Cash flow** | Pay upfront | Receive upfront |
| **Max profit** | Spread width - debit | Credit received |
| **Max loss** | Debit paid | Spread width - credit |
| **Requires** | Stock to move | Stock to NOT move (or move favorably) |
| **Win rate** | Lower (30-40%) | Higher (60-70%) |
| **R:R ratio** | Better (2:1 to 3:1) | Worse (1:2 to 1:3) |
| **Psychology** | Easier (risking less) | Harder (risking more) |
| **Beginner** | Better starting point | More advanced |

**Example with same strikes ($100/$110):**

**Debit spread (bull call):**

- Cost: $3
- Max profit: $7
- R:R = 7:3 = 2.3:1

**Credit spread (bull put $90/$100):**

- Credit: $3
- Max loss: $7
- R:R = 3:7 = 0.43:1

**Choose based on:**

- Risk tolerance
- Market conditions
- Win rate preference

---

## Strike Selection

**Critical decision for spreads:**

### Spread Width

**Narrow spreads (5 points):**

- Lower capital requirement
- Lower profit potential
- Higher R:R ratio
- Less risky
- **Good for beginners**

**Wide spreads (20 points):**

- Higher capital requirement
- Higher profit potential
- Lower R:R ratio
- More risky
- **For experienced traders**

**Example:**

- Stock at $100

**Narrow spread:**

- $100/$105 bull call for $2
- Max profit: $3 (R:R = 1.5:1)
- Breakeven: $102 (easier to reach)

**Wide spread:**

- $100/$120 bull call for $8
- Max profit: $12 (R:R = 1.5:1)
- Breakeven: $108 (harder to reach)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/call_spread_width_comparison.png?raw=true" alt="call_spread_width_comparison" width="700">
</p>
**Figure 5:** Call spread width comparison showing how narrow spreads (5-point) versus wide spreads (20-point) affect capital requirements, profit potential, and risk-reward ratios for bull call spreads.

### Strike Positioning

**For debit spreads:**

**ATM/slightly OTM:**

- Buy ATM, sell OTM
- Balanced approach
- Most common

**OTM:**

- Both strikes OTM
- Cheaper
- Lower probability
- Speculative

**For credit spreads:**

**OTM (Most Common):**

- Sell OTM, buy further OTM
- High probability of keeping credit
- Standard approach

**ATM:**

- Higher credit
- Lower probability
- More aggressive

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/put_spread_aggressiveness_comparison.png?raw=true" alt="put_spread_aggressiveness_comparison" width="700">
</p>
**Figure 6:** Put spread aggressiveness comparison illustrating the trade-off between conservative (far OTM) and aggressive (ATM) strike selections for bull put credit spreads, showing impact on probability and premium collected.

---

## Time Frame Selection

**Vertical spreads across timeframes:**

### Short-Term (< 30 days)

**Pros:**

- Higher theta decay rate (credit spreads benefit)
- Less capital tied up
- Quick resolution

**Cons:**

- Less time to be right
- Higher gamma risk (price swings)
- More rebalancing needed

### Medium-Term (30-60 days)

**Pros:**

- Balanced theta/time
- More room for thesis to work
- Standard approach

**Cons:**

- More capital required
- Slower resolution

### Long-Term (60+ days)

**Pros:**

- Plenty of time
- Lower gamma risk
- Can weather volatility

**Cons:**

- Expensive (for debit spreads)
- Capital tied up longer
- Slower theta decay (credit spreads)

**Recommendation:** 30-45 days for credit spreads, 45-60 days for debit spreads

---

## Concrete Example 1: Bull Call Spread

**Setup:**

- **Stock:** AMD at $110
- **View:** Earnings coming, expect rally to $125
- **Time:** 45 days to earnings

**The Trade: $110/$120 Bull Call Spread**

**Structure:**

- Buy $110 call for $8.00
- Sell $120 call for $2.50
- **Net debit: $5.50 per share**
- Cost per contract: $550
- Buy 5 contracts = $2,750 total

**Position details:**

- Max profit: ($120 - $110) - $5.50 = $4.50/share = $2,250 total
- Max loss: $5.50/share = $2,750 total
- Breakeven: $115.50
- R:R ratio: 2,250:2,750 = 0.82:1

**Scenario 1: Strong Rally (AMD → $130)**

After 45 days:

- Stock at $130 (strong earnings beat)
- Both calls deep ITM
- Spread at max value: $10
- **Profit: $10 - $5.50 = $4.50/share**
- **Total: $2,250 (82% return)**

**Key insight:** Gains capped at $120, missed move from $120 to $130

**Scenario 2: Moderate Rally (AMD → $120)**

After 45 days:

- Stock exactly at $120
- Long call worth $10, short call worthless
- **Profit: $10 - $5.50 = $4.50/share**
- **Total: $2,250 (82% return)**

**Perfect outcome!**

**Scenario 3: Small Rally (AMD → $115)**

After 45 days:

- Stock at $115
- Long call worth $5, short call worthless
- **Loss: $5 - $5.50 = -$0.50/share**
- **Total: -$250 (9% loss)**

**Moved in your direction but not enough**

**Scenario 4: No Movement (AMD → $110)**

After 45 days:

- Stock unchanged
- Both calls worthless (ATM → OTM)
- **Loss: Full debit of $5.50/share**
- **Total: -$2,750 (100% loss)**

**Scenario 5: Decline (AMD → $95)**

After 45 days:

- Stock down to $95
- Both calls expire worthless
- **Loss: Full debit of $5.50/share**
- **Total: -$2,750 (100% loss)**

**Compare to single call:**

- If bought $110 call only for $8
- Loss would be $4,000 (45% worse!)
- **Spread limited loss**

---

## Concrete Example 2: Bull Put Credit Spread

**Setup:**

- **Stock:** AAPL at $180
- **View:** Bullish, expect support at $170
- **Market:** Earnings passed, IV elevated

**The Trade: $165/$175 Bull Put Spread**

**Structure:**

- Sell $175 put for $6.00
- Buy $165 put for $2.00
- **Net credit: $4.00 per share**
- Credit per contract: $400
- Sell 5 contracts = $2,000 credit received

**Position details:**

- Max profit: $4.00/share = $2,000 total
- Max loss: ($175 - $165) - $4 = $6/share = $3,000 total
- Breakeven: $171
- R:R ratio: 2,000:3,000 = 0.67:1
- Probability of profit: ~65% (both strikes OTM)

**Scenario 1: Stock Stable or Up (AAPL → $180+)**

After 30 days:

- Stock at $180 or higher
- Both puts expire worthless
- **Keep full credit: $4/share**
- **Total profit: $2,000 (100% of max)**
- **Return: 67% on $3,000 buying power**

**This is the goal outcome!**

**Scenario 2: Small Decline (AAPL → $175)**

After 30 days:

- Stock at $175 (short put strike)
- Both puts expire worthless
- **Keep full credit: $4/share**
- **Total profit: $2,000**

**Still winning!**

**Scenario 3: Moderate Decline (AAPL → $170)**

After 30 days:

- Stock at $170 (between strikes)
- Short put worth $5 intrinsic
- Long put worthless
- **P&L: $4 credit - $5 loss = -$1/share**
- **Total loss: -$500 (16.7% loss on buying power)**

**Manageable loss**

**Scenario 4: Large Decline (AAPL → $160)**

After 30 days:

- Stock crashed to $160
- Short put worth $15
- Long put worth $5
- Net loss from spread: $10
- **P&L: $4 credit - $10 spread loss = -$6/share**
- **Total loss: -$3,000 (max loss)**

**Long put protected from worse losses!**

**Risk Management Move (at $170 after 15 days):**

- Stock approaching $170
- Spread losing value
- **Close early for -$1 loss instead of risking -$6**
- Exit discipline saves capital

---

## Advanced: Adjusting Spreads

**When trades go against you:**

### Rolling

**For losing credit spread:**

- Close current spread at loss
- Open new spread further out in time
- Collect additional credit
- More time to be right

**Example:**

- Bull put spread $90/$100 losing
- Stock at $92
- Close for -$6 loss
- Roll to next month $85/$95 for $5 credit
- Net: -$1 debit, but more time

### Closing Early

**For winning credit spreads:**

- Reached 50% of max profit
- Close rather than hold for last 50%
- Reduce risk, free up capital
- Redeploy in new trade

**Example:**

- Sold spread for $4 credit
- Now can close for $2 debit
- **Lock in $2 profit (50%)**
- Don't risk it going back

**Professional approach:** Take 50% profits consistently

---

## Spreads vs. Single Options

**Key comparison:**

| Aspect | Single Long Call | Bull Call Spread |
|--------|------------------|------------------|
| **Cost** | $8 | $5.50 |
| **Max loss** | $8 (100%) | $5.50 (100%) |
| **Max profit** | Unlimited | $4.50 (82%) |
| **Breakeven** | $108 | $115.50 |
| **Leverage** | Higher | Lower |
| **Risk/Reward** | Unlimited:$8 | $4.50:$5.50 |
| **Best when** | Expect huge move | Expect moderate move |

**When single option better:**

- Expect explosive move (> 20%)
- Want maximum leverage
- Can handle 100% loss

**When spread better:**

- Expect moderate move (5-15%)
- Want defined risk both sides
- Prefer higher probability

---

## Pros and Cons

### Debit Spreads - Advantages ✓

**1. Defined risk both sides**

- Can't lose more than debit
- Can't gain more than spread width
- Predictable outcomes

**2. Lower cost than single options**

- Debit spread cheaper
- Can afford more contracts
- Better capital efficiency

**3. Lower breakeven**

- Need smaller move to profit
- Higher probability
- More forgiving

**4. No naked exposure**

- Long option protects short
- No margin calls
- Simple to manage

### Debit Spreads - Disadvantages ✗

**1. Capped upside**

- Miss huge moves
- Limited profit potential
- Opportunity cost

**2. Still can lose 100%**

- If wrong direction
- Total loss of debit
- Not "safer" on loss side

**3. Two commissions**

- Two legs to trade
- Higher transaction costs
- Wider spreads to overcome

### Credit Spreads - Advantages ✓

**1. Immediate income**

- Receive credit upfront
- Positive cash flow
- Can deploy elsewhere

**2. High win rate**

- 60-70% typical
- OTM strikes = probability
- Time decay helps

**3. Flexible strikes**

- Choose probability
- Adjust risk/reward
- Customize to view

### Credit Spreads - Disadvantages ✗

**1. Risk > reward**

- Risking $6 to make $4
- Unfavorable ratio
- Need high win rate

**2. Margin requirement**

- Buying power held
- Can't use for other trades
- Less capital efficient than seems

**3. Psychological difficulty**

- Watching spread against you
- Temptation to close early
- Requires discipline

**4. Assignment risk**

- Can be assigned on short leg
- Pin risk at expiration
- Complicated to manage

---

## When to Use Spreads

### Bull Call Spreads

**Best when:**

- Moderately bullish (expect 10-20% move)
- Low IV (debit spreads cheaper)
- Clear catalyst (earnings, product launch)
- Want defined risk

### Bear Put Spreads

**Best when:**

- Moderately bearish (expect 10-20% decline)
- Low IV (debit spreads cheaper)
- Technical breakdown
- Want defined risk

### Bull Put Spreads (Credit)

**Best when:**

- Bullish but not aggressive
- High IV (credit spreads better)
- Strong support level below
- Want income + defined risk

### Bear Call Spreads (Credit)

**Best when:**

- Bearish but not aggressive
- High IV (credit spreads better)
- Strong resistance above
- Want income + defined risk

**General rule:**
- **Debit spreads:** Directional bets, moderate conviction
- **Credit spreads:** Income generation, high probability

---

## Common Mistakes

**Top mistakes with spreads:**

### 1. Wrong Spread Width

- **Mistake:** Always use $5 wide or $10 wide
- **Why fails:** Doesn't match risk tolerance or stock price
- **Fix:** Adjust width to capital and risk appetite

### 2. Ignoring Liquidity

- **Mistake:** Trade illiquid strikes
- **Why fails:** Wide bid-ask, can't exit efficiently
- **Fix:** Only trade liquid options (vol > 100)

### 3. Holding to Expiration

- **Mistake:** Wait for max profit on credit spreads
- **Why fails:** Risk last 50% for last 50% reward
- **Fix:** Close at 50% profit

### 4. Not Managing Losers

- **Mistake:** Let losing spread go to max loss
- **Why fails:** Hope it recovers, usually doesn't
- **Fix:** Close at 2x credit received

### 5. Wrong Direction

- **Mistake:** Selling put spreads in downtrend
- **Why fails:** Fighting the trend
- **Fix:** Align with trend or stay out

### 6. Over-Sizing

- **Mistake:** "Spreads are safer, I'll do 20 contracts"
- **Why fails:** Max loss × 20 can blow up account
- **Fix:** Size by max loss (2-5% per trade)

### 7. Spreads in Low IV

- **Mistake:** Sell credit spreads when IV at lows
- **Why fails:** Low premium, not worth risk
- **Fix:** Sell spreads when IV > 50th percentile

### 8. Ignoring Pin Risk

- **Mistake:** Hold spread into expiration with stock at short strike
- **Why fails:** Assignment uncertainty
- **Fix:** Close before expiration Friday

---

## Real-World Examples

### Example 1: NVDA Bull Call Spread (Jan 2024)

**Setup:**

- NVDA at $480
- AI boom continuing
- Want leveraged exposure with defined risk

**Trade:** $480/$520 bull call spread, 60 days

- Buy $480 call: $35
- Sell $520 call: $18
- **Net debit: $17**

**Outcome after 60 days:**

- NVDA rallied to $560
- Spread at max value: $40
- **Profit: $40 - $17 = $23** (135% return)

**Comparison:**

- Single $480 call would've made $80 - $35 = $45
- But spread used less capital
- Spread breakeven lower

### Example 2: SPY Bull Put Spread (Mar 2024)

**Setup:**

- SPY at $510
- Pullback to strong support
- High IV from volatility

**Trade:** $490/$500 bull put spread, 45 days

- Sell $500 put: $7
- Buy $490 put: $3
- **Net credit: $4**

**Outcome after 30 days:**

- SPY stayed above $505
- Closed spread for $1 debit
- **Profit: $4 - $1 = $3** (75% of max, 30% return on BP)

**Closed early:**

- Got 75% of max profit
- Freed up capital
- Reduced risk of reversal

---

## What to Remember

### Core Concept

**Vertical spreads = defined risk + defined reward:**

- Buy one option, sell another (same type, different strikes)
- Creates "floor" and "ceiling"
- Much safer than naked options
- Lower cost than single long options

### Four Types

**Debit spreads (pay money):**

1. **Bull call spread:** Buy lower call, sell higher call
2. **Bear put spread:** Buy higher put, sell lower put

**Credit spreads (receive money):**

3. **Bull put spread:** Sell higher put, buy lower put
4. **Bear call spread:** Sell lower call, buy higher call

### Key Formulas

**For all spreads:**

$$
\text{Max Profit} + \text{Max Loss} = \text{Spread Width}
$$

**Debit spreads:**

- Max loss = Debit paid
- Max profit = Spread width - Debit

**Credit spreads:**

- Max profit = Credit received
- Max loss = Spread width - Credit

### Strike Selection

**Spread width:**

- Narrow (5-10 points): Lower risk, lower reward
- Wide (15-20 points): Higher risk, higher reward

**Positioning:**

- ATM/slightly OTM: Balanced
- Far OTM (credit spreads): High probability, low premium

### Debit vs. Credit

**Use debit spreads when:**

- Directional conviction
- Lower IV environment
- Want better R:R ratio

**Use credit spreads when:**

- Want high probability
- Higher IV environment
- Want immediate income

### Management

**For credit spreads:**

- Close at 50% profit
- Close at 2x credit loss
- Don't hold to expiration

**For debit spreads:**

- Exit at 50-75% of max
- Cut losses at -50%
- Can hold longer if thesis intact

### Comparison to Single Options


**Spreads are better when:**

- Expect moderate move (not explosive)
- Want defined risk both sides
- Need capital efficiency
- Want higher probability

**Single options better when:**

- Expect huge move (> 20%)
- Want unlimited upside
- Very high conviction

### Risk Management

**Position sizing:**

- Max loss = 2-5% of portfolio
- Not spread cost (for credit spreads)
- Calculate max loss first

**Diversification:**

- Multiple spreads different stocks
- Mix of time frames
- Don't concentrate

### Final Wisdom

> "Vertical spreads are the 'Goldilocks' of option strategies - not too risky (like naked), not too expensive (like single longs), but just right. They offer defined risk, reasonable capital requirements, and moderate profit potential. Master these before complex multi-leg strategies. Many professional traders use spreads almost exclusively."

**Keys to success:**

- Align with market direction
- Choose appropriate width
- Manage at 50% profit/loss
- Only trade liquid options
- Don't over-size
- Learn from every trade

**Most important:** Vertical spreads bridge the gap between beginner (single options) and advanced (complex strategies). Master these and you have a solid foundation! 🎯📊
