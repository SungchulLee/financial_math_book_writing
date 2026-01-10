# Vertical Spreads

**Vertical spreads** are directional option strategies where you simultaneously buy and sell options of the same type (both calls or both puts) at different strike prices but the same expiration date, creating defined risk and defined reward.

---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/bull_call_spread.png?raw=true" alt="Bull Call Spread" width="700">
</p>

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

## Types of Vertical

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/bear_put_spread.png?raw=true" alt="Bear Put Spread" width="700">
</p>

**Four main types:**

### 1. Bull Call Spread

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/bull_put_spread.png?raw=true" alt="Bull Put Spread" width="700">
</p>

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


**Figure 1:** Bull call spread profit/loss diagram showing the defined risk-reward profile of buying a lower strike call and selling a higher strike call, illustrating capped profit potential and limited downside.

### 2. Bear Put Spread

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/bear_call_spread.png?raw=true" alt="Bear Call Spread" width="700">
</p>

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


**Figure 2:** Bear put spread profit/loss diagram demonstrating the bearish strategy with defined risk, showing how buying a higher strike put and selling a lower strike put creates a capped profit structure.

### 3. Bull Put Spread

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


**Figure 3:** Bull put spread profit/loss diagram illustrating the credit spread structure where selling a higher strike put and buying a lower strike put generates immediate income with defined maximum loss.

### 4. Bear Call Spread

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


**Figure 4:** Bear call spread profit/loss diagram showing the bearish credit spread payoff, demonstrating how selling a lower strike call and buying a higher strike call creates income with capped risk.

---

## Economic

**Understanding what vertical spreads REALLY represent economically:**

### 1. The Risk

**Vertical spreads are fundamentally about:**

1. **Trading potential for certainty** - You give up unlimited profit to cap your risk
2. **Partial position hedging** - Your short option hedges your long option (and vice versa)
3. **Probability engineering** - You're adjusting win probability vs. win size

**The economic equivalence:**

$$
\text{Vertical Spread} \equiv \text{Directional Position} + \text{Opposite Position at Different Strike}
$$

This creates a "bounded position" - you're long the market from strike $K_1$ to strike $K_2$, but neutral outside this range.

### 2. Debit Spreads

**Economic interpretation of debit spreads:**

When you buy a bull call spread ($100/$110 for $3), you're economically:

1. **Buying directional exposure** from $100 to $110 
2. **Selling away the tail** (profit beyond $110)
3. **Subsidizing the cost** by selling that tail to someone else

**The equivalence:**

$$
\text{Bull Call Spread} = \text{Long Call} - \text{OTM Call Premium Financing}
$$

**Why this matters:**

- You're not "giving up" upside - you're **selling it to finance** the position

- The buyer of your short call is essentially **co-investing** with you

- You both profit if the stock moves up (just at different ranges)

**Think of it as:**

- You own a property worth $100k to $110k

- Someone else owns appreciation beyond $110k

- You both want the property to appreciate, but you capped your interest

### 3. Credit Spreads

**Economic interpretation of credit spreads:**

When you sell a bull put spread ($90/$100 for $3), you're economically:

1. **Selling insurance** on the stock going below $100
2. **Buying insurance** on catastrophic drops below $90  
3. **Keeping the net premium** if stock stays above $100

**The equivalence:**

$$
\text{Bull Put Spread} = \text{Naked Put Sale} + \text{Downside Protection Purchase}
$$

**Why this matters:**

- You're an **insurance company** with reinsurance

- You collect premium for risk, but have catastrophic coverage

- Your edge comes from **probability** (high chance of expiring worthless)

**Think of it as:**

- Homeowner buys earthquake insurance from you ($100 deductible)

- You buy catastrophic reinsurance ($90 deductible)  

- You keep the spread ($3) if no earthquake

- You're protected if catastrophic loss occurs

### 4. The Fundamental

**Core economic insight for all vertical spreads:**

$$
\text{Win Probability} \times \text{Profit} \approx \text{Loss Probability} \times \text{Loss}
$$

This is why:

**Debit spreads:**

- Lower win probability (30-40%)

- Higher reward:risk ratio (2:1 or 3:1)

- You need big moves

**Credit spreads:**

- Higher win probability (60-70%)  

- Lower reward:risk ratio (1:2 or 1:3)

- You win on time decay and no big moves

**The market prices these fairly** - there's no inherent edge in choosing debit vs. credit. Your edge comes from:

- Better forecasting (direction, magnitude, timing)

- Better strike selection (probability vs. premium)

- Better management (when to exit, roll, adjust)

### 5. Spreads as

**Beyond directional:**

Vertical spreads are also **volatility trades**:

**Debit spreads:**

- Long vega (benefit from IV increase)

- Want volatility expansion

- Buy when IV low, sell when IV spikes

**Credit spreads:**

- Short vega (hurt by IV increase)

- Want volatility contraction  

- Sell when IV high, buy back when IV drops

**The economic reality:**

$$
\text{Spread P&L} = \text{Directional P&L} + \text{Volatility P&L} + \text{Time Decay P&L}
$$

All three components matter, not just direction.

### 6. Why Professionals

**The institutional perspective:**

1. **Capital efficiency:** Spreads use less buying power than stock or naked options
2. **Risk management:** Defined loss means easier position sizing and risk aggregation  
3. **Regulatory compliance:** Spreads often allowed where naked options aren't
4. **Scalability:** Can run 50 spreads easier than 50 naked positions

**The professional advantage:**

- Retail thinks: "I'm giving up profit by selling the other leg"

- Professionals think: "I'm financing my position and defining my risk"

This mindset shift is crucial. You're not losing opportunity - you're **managing probability and capital**.

---

## Practical Guidance

**Step-by-step implementation framework:**

### 1. Before entering

**Before entering any spread, determine:**

1. **Directional conviction:**

   - What direction? (Bull vs. Bear)

   - How strong? (Moderate vs. Strong)

   - Time frame? (Days, weeks, months)

2. **Volatility environment:**
   ```
   IV Percentile = (Current IV - 52wk Low) / (52wk High - 52wk Low) × 100
   ```

   - IV < 30th percentile → Favor debit spreads  

   - IV > 70th percentile → Favor credit spreads

   - IV 30-70th → Either works

3. **Technical/fundamental support:**

   - Support/resistance levels

   - Upcoming catalysts (earnings, Fed, etc.)

   - Trend strength

### 2. Decision tree:

**Decision tree:**

```
Bullish view?
├─ Yes → Bull spread
│  ├─ IV low? → Bull call spread (debit)
│  └─ IV high? → Bull put spread (credit)
└─ No (Bearish) → Bear spread
   ├─ IV low? → Bear put spread (debit)
   └─ IV high? → Bear call spread (credit)
```

**Alternative considerations:**

- **Want income now?** → Credit spread

- **Want better R:R?** → Debit spread  

- **Lower capital?** → Debit spread

- **Higher win rate?** → Credit spread

### 3. For debit

**For debit spreads:**

**Long strike (Buy):**

- ATM or slightly ITM (delta 0.50-0.60)

- This is your "horse in the race"

**Short strike (Sell):**

- OTM (delta 0.30-0.40)

- 1-2 standard deviation moves away

- Example: If stock at $100, sell $110 call (10% OTM)

**Spread width:**

- Narrow (5 points): Conservative, R:R ~1.5:1

- Medium (10 points): Balanced, R:R ~2:1

- Wide (20 points): Aggressive, R:R ~2.5:1

**For credit spreads:**

**Short strike (Sell):**

- OTM (delta 0.20-0.30)  

- This is your "line in the sand"

- Typically 1 standard deviation out

**Long strike (Buy):**

- Further OTM (delta 0.10-0.15)

- Protection leg, not profit leg

- Example: If stock at $100, sell $90 put, buy $85 put

**Spread width:**

- Narrow (5 points): Lower risk, lower premium

- Medium (10 points): Standard

- Wide (20 points): Higher premium, higher risk

### 4. Short-term (<30

**Short-term (<30 DTE):**

- **Pros:** Fast theta decay (credit spreads), less capital

- **Cons:** Less room for error, higher gamma risk

- **Best for:** Credit spreads, quick directional bets

**Medium-term (30-60 DTE):**

- **Pros:** Balanced theta/vega, reasonable time

- **Cons:** More capital tied up  

- **Best for:** Most spreads, standard approach

**Long-term (60-90+ DTE):**

- **Pros:** Time to be right, less theta burn early

- **Cons:** High capital requirement, slow theta

- **Best for:** Debit spreads with strong conviction

**Professional guideline:**

- Credit spreads: 30-45 DTE  

- Debit spreads: 45-75 DTE

### 5. Critical

**Critical formulas:**

**For debit spreads:**
$$
\text{Max Contracts} = \frac{\text{Portfolio} \times 0.02}{\text{Debit Paid} \times 100}
$$

Example: $50,000 portfolio, $3 debit

- Max risk: $50,000 × 0.02 = $1,000

- Contracts: $1,000 / ($3 × 100) = 3.3 → 3 contracts

**For credit spreads:**
$$
\text{Max Contracts} = \frac{\text{Portfolio} \times 0.02}{(\text{Spread Width} - \text{Credit}) \times 100}
$$

Example: $50,000 portfolio, $10 wide spread, $3 credit

- Max loss per: ($10 - $3) × 100 = $700

- Max risk: $50,000 × 0.02 = $1,000  

- Contracts: $1,000 / $700 = 1.4 → 1 contract

**Conservative sizing:**

- Risk 1-2% per trade when learning

- Max 5 uncorrelated spreads at once

- Never more than 20% of portfolio in spreads total

### 6. Best practices:

**Best practices:**

**Use limit orders:**

- Never market orders on spreads

- Calculate mid-point: (Bid + Ask) / 2

- Start slightly better than mid

- Work the order 10-15 minutes

**Check liquidity:**
```
Bid-Ask Spread < 10% of option price
AND
Volume > 100 contracts  
AND
Open Interest > 500
```

**Enter as single order:**

- Use "vertical spread" order type

- Don't leg in (risk of market moving)

- Exception: Very wide spreads may require legging

**Timing considerations:**

- Avoid first/last 30 min of trading  

- Best liquidity: 10:00am - 3:00pm ET

- Never enter minutes before major news

### 7. For credit

**For credit spreads:**

**Take profit at 50% of max:**
```
If credit = $3
Close when debit to close = $1.50
Profit = $1.50 (50% of $3)
```

**Cut losses at 2x credit:**
```
If credit = $3
Close when debit to close = $6
Loss = $3 (trying to save $4 of max $7 loss)
```

**For debit spreads:**

**Take profit at 50-75% of max:**
```
If max profit = $7, debit = $3
Close when spread worth $6-$7.25
Profit = $3-$4.25
```

**Cut losses at 50% of debit:**
```
If debit = $3
Close when spread worth $1.50
Loss = $1.50
```

**Time-based exits:**

- If 50% of time passed with no move → Consider exit

- Don't hold credit spreads past 7 DTE (gamma risk)

- Debit spreads can run longer if thesis intact

**Rolling strategies:**

**When to roll (credit spreads):**

- Tested but not broken

- Still believe in direction  

- Can collect credit

**How to roll:**
```
Close current spread
Open new spread:

- Same direction

- Further out in time  

- Same or better strikes

- Must collect net credit
```

### 8. Track for every

**Track for every trade:**

| Field | Example |
|-------|---------|
| Date | 2024-01-15 |
| Type | Bull put spread |
| Strikes | 490/500 |
| DTE | 45 |
| Debit/Credit | $4 credit |
| Contracts | 3 |
| Max loss | $1,800 |
| IV Percentile | 68% |
| Reason | SPY bounce at support, high IV |
| Exit date | 2024-02-10 |
| Exit price | $1 debit |
| P&L | +$900 |
| Notes | Closed at 75% profit |

**Analyze monthly:**

- Win rate by spread type

- Average R:R achieved

- Common mistakes  

- Best/worst setups

### 9. Common Execution

**1. Legging into spreads:**

- **Wrong:** Buy call, then try to sell other leg

- **Right:** Enter as single spread order

**2. Ignoring slippage:**

- **Wrong:** Accept wide spreads, assume mid-price fill

- **Right:** Calculate max acceptable slippage, use limits

**3. Over-managing:**

- **Wrong:** Adjust constantly, micro-manage daily

- **Right:** Set alerts, check daily, act on rules only

**4. Holding to expiration:**

- **Wrong:** Wait for max profit on credit spreads  

- **Right:** Close at 50% profit, avoid weekend/pin risk

**5. Revenge trading:**

- **Wrong:** After loss, immediately enter larger spread

- **Right:** Take break, analyze what happened, stay sized

**6. Ignoring corporate actions:**

- **Wrong:** Hold spread through dividend/split

- **Right:** Close or roll before ex-div date

### 10. Professional

**Spread selection matrix:**

| Market Condition | IV Level | Best Spread | Reasoning |
|-----------------|----------|-------------|-----------|
| Strong uptrend | Low | Bull call debit | Cheap calls, high conviction |
| Strong uptrend | High | Bull put credit | Expensive options, sell premium |
| Weak uptrend | Low | Bull call debit | Need move, cheap entry |
| Weak uptrend | High | Bull put credit | High prob, don't need big move |
| Consolidating | High | Credit spreads both sides | Sell premium to range-bound |
| Breaking out | Low | Debit spread | Ride momentum, defined risk |

**IV rank strategy:**

- IV < 25th percentile: Only debit spreads

- IV 25-50th: Prefer debit, can do credit

- IV 50-75th: Prefer credit, can do debit  

- IV > 75th percentile: Heavily favor credit spreads

**The 3-question checklist:**

Before every spread:
1. "Do I have conviction on direction AND magnitude?" → If no, skip
2. "Is IV at favorable level for this type?" → If no, wait or switch type
3. "Can I risk 100% of capital committed?" → If no, size down

---



## Common Mistakes

**Top mistakes with spreads:**

### 1. Wrong Spread

- **Mistake:** Always use $5 wide or $10 wide

- **Why fails:** Doesn't match risk tolerance or stock price

- **Fix:** Adjust width to capital and risk appetite

### 2. Ignoring

- **Mistake:** Trade illiquid strikes

- **Why fails:** Wide bid-ask, can't exit efficiently

- **Fix:** Only trade liquid options (vol > 100)

### 3. Holding to

- **Mistake:** Wait for max profit on credit spreads

- **Why fails:** Risk last 50% for last 50% reward

- **Fix:** Close at 50% profit

### 4. Not Managing

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

### 1. Pension Duration

**Setup:**

- NVDA at $480

- AI boom continuing

- Want leveraged exposure with defined risk

- IV rank at 42% (moderate)

- Technical: Broke above $470 resistance

**Trade:** $480/$520 bull call spread, 60 DTE

- Buy $480 call: $35

- Sell $520 call: $18

- **Net debit: $17 ($1,700 per contract)**

- Max profit: $40 - $17 = $23 ($2,300)

- Max loss: $17 ($1,700)

- Breakeven: $497

- Risk/reward: 1.35:1

**Management:**

- Week 1: NVDA rallies to $500, spread at $23 (up $600, 35% profit)

- Week 2: Continues to $520, spread at $32 (up $1,500, 88% profit)

- Week 3: Hits $540, spread maxes at $40

- **Closed at Week 3: +$2,300 profit (135% ROI in 21 days)**

**Outcome:**

- Perfect execution: stock moved full spread width

- Annualized ROI: ~2,200%

- Could have closed earlier at 50% for faster capital recycling

**Comparison:**

- Single $480 call would've made $60 - $35 = $25 per share (71% ROI)

- But required $3,500 capital vs $1,700

- Spread had lower breakeven ($497 vs $515)

- **Spread was more capital efficient despite capped upside**

**Lesson:** Strong trend + catalyst + defined risk = ideal debit spread setup. Take profits at max value.

### 2. Transition Risk

**Setup:**

- SPY at $510

- Pullback to strong support at $505

- High IV from recent volatility (VIX at 18)

- IV rank at 65% (elevated)

- Technical: RSI at 35 (oversold)

**Trade:** $490/$500 bull put spread, 45 DTE

- Sell $500 put: $7

- Buy $490 put: $3

- **Net credit: $4 ($400 per contract)**

- Max profit: $400

- Max loss: $10 - $4 = $6 ($600)

- Breakeven: $496

- Probability of profit: ~75%

**Management:**

- Day 10: SPY at $512, spread worth $2.50 (profit $150, 37.5%)

- Day 18: SPY at $515, spread worth $1.50 (profit $250, 62.5%)

- **Closed at Day 18 per 50%+ rule: +$250 profit**

**Outcome after 18 days:**

- Profit: $250 (62.5% of max profit)

- ROC: 41% on max risk in 18 days

- Freed capital 27 days early

- SPY continued higher (could have kept full $400)

- **But following 50% rule allows faster compounding**

**Closed early rationale:**

- Got 62.5% of max profit in 40% of time

- Remaining $150 profit requires 60% of time

- Risk/reward ratio deteriorating

- Can redeploy $600 capital to new trade

**Lesson:** High IV + support level + credit spread = high probability trade. Take 50-70% profits for capital efficiency.

### 3. Portable Alpha

**Setup:**

- TSLA at $240, seemed overvalued

- Deliveries disappointing

- Expected further decline

- IV rank at 55%

**Trade:** $240/$230 bear put spread, 45 DTE

- Buy $240 put: $12

- Sell $230 put: $7

- **Net debit: $5 ($500 per contract)**

- Max profit: $10 - $5 = $5 ($500)

- Max loss: $5 ($500)

- Breakeven: $235

- Risk/reward: 1:1

**What went wrong:**

**Week 1:**

- Elon Musk bullish tweets

- TSLA rallies to $255 (completely wrong direction)

- Spread value drops to $2 (down $300, -60%)

- **Should have cut loss at -50% here**

**Week 2:**

- Continued holding, hoping for reversal

- TSLA at $265

- Spread value: $0.50 (down $450, -90%)

- Finally cut loss at -90%

**Week 3:**

- TSLA actually drops to $230 (thesis was eventually right!)

- But too late - already exited

- **Wrong timing destroyed good thesis**

**Final outcome:**

- Loss: $450 (90% of max loss)

- Should have exited at -50% for -$250 loss

- **Extra $200 lost from "hope trading"**

- Later reversal didn't help (already out)

**Lessons learned:**

1. Stop losses exist for a reason (-50% is the line)
2. Being eventually right doesn't matter if timing wrong
3. Hope is not a strategy
4. Trends can last longer than you can stay solvent
5. **Never fight strong momentum without clear catalyst**

### 4. Tactical Duration

**Setup:**

- AAPL at $185 post-earnings

- IV rank dropped from 70% to 35% after earnings

- Stock establishing range $180-$190

- No major catalysts for 6 weeks

**Trade:** $195/$200 bear call spread, 35 DTE

- Sell $195 call: $2.50

- Buy $200 call: $1.00

- **Net credit: $1.50 ($150 per contract)**

- Max profit: $150

- Max loss: $5 - $1.50 = $3.50 ($350)

- Breakeven: $196.50

- Probability of profit: ~70%

**Management:**

- Week 1: AAPL at $182, spread at $1.00 (profit $50, 33%)

- Week 2: AAPL at $186, spread at $0.60 (profit $90, 60%)

- **Closed at Week 2: +$90 profit (60% of max in 40% of time)**

**Alternative outcome if held:**

- Week 3-5: AAPL consolidated $185-$188

- Spread expired worthless

- Would have made full $150

- But took longer and had more risk

**Why early exit was smart:**

- $90 profit in 14 days = 25% ROC

- Remaining $60 would take 21 more days

- Risk of surprise move increases over time

- **Capital recycling beats maximum profit**

**Lesson:** Post-earnings, low-IV environments favor credit spreads. Take 50-70% profits and move on.

### 5. Duration Hedge

**Setup:**

- QQQ at $370

- Tech rally momentum

- Entered 3 days before Fed announcement (MISTAKE!)

- IV rank at 40%

**Trade:** $370/$380 bull call spread, 30 DTE

- Buy $370 call: $9

- Sell $380 call: $4

- **Net debit: $5 ($500 per contract)**

- Max profit: $10 - $5 = $5 ($500)

- Max loss: $5 ($500)

**What happened:**

**Day 1-2:**

- QQQ hovering $370-$372

- Spread at $5.50 (up $50)

- Looking good

**Day 3 (Fed announcement):**

- Fed surprise hawkish

- QQQ gaps down to $360 overnight

- Spread opens at $0.50 (down $450, -90%)

- **No chance to manage - gap was instant**

**Final outcome:**

- Closed at $0.50: -$450 loss (90%)

- Just 10% salvaged

- Gap risk destroyed position instantly

- **Binary event risk realized**

**What went wrong:**

1. Entered too close to major catalyst (Fed)
2. Didn't account for gap risk
3. Should have used credit spread (less directional risk)
4. Or avoided position entirely

**Lesson:** Don't hold debit spreads through binary events (Fed, earnings, major news). Gap risk can destroy positions instantly with no chance to manage.

### 6. Setup: SPY at

**Setup:**

- SPY at $455, range-bound $450-$460

- IV rank 58% (good for credit spreads)

- Multiple positions for diversification

**Trade:** $445/$450 bull put spread, 40 DTE (5 contracts)

- Sell $450 put: $3.50

- Buy $445 put: $1.20

- **Net credit: $2.30 ($230 per contract)**

- Total credit: $1,150 (5 contracts)

- Max loss per contract: $5 - $2.30 = $2.70 ($270)

- Total max loss: $1,350

**Management timeline:**

**Day 12:**

- SPY at $458, spread at $1.10

- Profit: $1.20 × 500 = $600 (52% of max)

- **Followed 50% rule: CLOSED ALL 5 contracts**

- Freed up $1,350 buying power

- Total days held: 12

**What happened after:**

- Day 15: SPY rallied to $463 (would have been full profit)

- Day 20: SPY dropped to $452 (still full profit)

- Day 28: SURPRISE Fed hawkish, SPY crash to $440!

- Spread would have gone to max loss: -$1,350

**Outcome comparison:**

**Following 50% rule:**

- Profit: +$600 in 12 days

- Avoided disaster

- Capital redeployed to new trade

- **Second trade also hit 50%: Another +$500**

- **Total in 40 days: $1,100**

**If held for max:**

- Would have lost -$1,350 due to surprise crash

- **50% rule saved $2,450 swing!**

**Lesson:** The 50% rule isn't about maximizing single trades - it's about risk management and compounding. Greed kills. Discipline survives.

### 7. Setup: $10,000

**Setup:**

- $10,000 account (small trader)

- Bullish on IWM (Russell 2000)

- Want to risk 2% = $200 max

**Trade:** $195/$200 bull call spread, 60 DTE

- Buy $195 call: $4.50

- Sell $200 call: $2.50

- **Net debit: $2.00 ($200 per contract)**

- Max loss: $200 (1 contract only)

- Max profit: $5 - $2 = $3 ($300)

**Position sizing decision:**

**Tempting to do more:**

- Could afford 5 contracts ($1,000)

- Max profit would be $1,500

- But max loss would be $1,000 (10% of account!)

**Disciplined approach:**

- 1 contract only

- Max loss $200 (2% of account)

- **Survivability over maximum gains**

**Outcome:**

- IWM rallied to $205

- Spread maxed at $5

- **Profit: $300 (150% ROI, 3% of account)**

- Small dollar amount but proper risk management

**If had over-sized to 5 contracts:**

- Would have made $1,500 (15% of account) ✓

- But if trade went wrong: -$1,000 (10% of account) ✗

- **One bad trade would devastate small account**

**Lesson:** Position sizing discipline is MORE important with small accounts. Protect capital first, grow slow and steady. Don't let greed destroy discipline.

---

## Final Wisdom

> "Vertical spreads are the 'Goldilocks' of option strategies - not too risky (like naked), not too expensive (like single longs), but just right. They offer defined risk, reasonable capital requirements, and moderate profit potential. Master these before complex multi-leg strategies. Many professional traders use spreads almost exclusively."

**Keys to success:**

- Align with market direction

- Choose appropriate width

- Manage at 50% profit/loss

- Only trade liquid options

- Don't over-size

- Learn from every trade

**Most important:** Vertical spreads bridge the gap between beginner (single options) and advanced (complex strategies). Master these and you have a solid foundation! 🎯📊