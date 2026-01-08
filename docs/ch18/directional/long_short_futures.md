# Long and Short Futures

**Long and short futures** are standardized contracts to buy or sell an asset at a predetermined price on a future date, giving you direct linear exposure to price movements with symmetrical unlimited risk and reward.

---

## The Core Insight

**The fundamental idea:**

- Futures provide pure, leveraged price exposure
- Symmetric profit and loss (unlimited both ways)
- No premium cost (unlike options)
- Obligation to perform (not optional)
- Mark-to-market daily (gains/losses realized daily)
- Leverage through margin (typically 3-20% of notional)

**The key equation:**

$$
\text{P&L}_{\text{Long}} = (\text{Current Price} - \text{Entry Price}) \times \text{Contract Multiplier} \times \text{Number of Contracts}
$$

$$
\text{P&L}_{\text{Short}} = (\text{Entry Price} - \text{Current Price}) \times \text{Contract Multiplier} \times \text{Number of Contracts}
$$

**You're essentially betting: "The price will move in my direction, and I can handle unlimited risk in the other direction."**

---

## What Are Futures?

**Before trading futures, understand what you're entering:**

### 1. Long Futures Position

**Definition:** An obligation to BUY the underlying asset at price $F$ on delivery date $T$ (or cash settle).

**When you go long futures:**

- No premium paid (unlike options)
- Post initial margin (performance bond)
- Variation margin paid/received daily (mark-to-market)
- Profit if price goes UP
- Loss if price goes DOWN
- Both profit and loss are UNLIMITED
- Must either close position before expiration or accept delivery

**Example:**

- E-mini S&P 500 futures at 4500
- Contract multiplier: $50 per point
- Notional value: 4500 × $50 = $225,000
- Initial margin: ~$12,000 (5.3% of notional)
- You control $225,000 exposure for $12,000

**Price movements:**

- Price → 4550: Profit = (4550 - 4500) × $50 = $2,500
- Price → 4450: Loss = (4450 - 4500) × $50 = -$2,500

### 2. Short Futures Position

**Definition:** An obligation to SELL the underlying asset at price $F$ on delivery date $T$ (or cash settle).

**When you go short futures:**

- No premium paid (unlike options)
- Post initial margin (performance bond)
- Variation margin paid/received daily
- Profit if price goes DOWN
- Loss if price goes UP
- Both profit and loss are UNLIMITED
- Must either close position before expiration or deliver asset

**Example:**

- Crude oil futures at $75/barrel
- Contract size: 1,000 barrels
- Notional value: $75 × 1,000 = $75,000
- Initial margin: ~$5,000 (6.7% of notional)
- You control $75,000 exposure for $5,000

**Price movements:**

- Price → $70: Profit = ($75 - $70) × 1,000 = $5,000
- Price → $80: Loss = ($75 - $80) × 1,000 = -$5,000

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/long_short_futures.png?raw=true" alt="long_short_futures" width="700">
</p>
**Figure 1:** Profit/loss comparison between long and short futures, showing perfectly symmetric linear payoffs with unlimited risk and reward in both directions, contrasting with options' asymmetric payoffs.

---

## Economic

**Beyond the basic definition, understanding what futures REALLY are economically:**

### 1. The Fundamental Nature of Futures

**A futures contract is a pure price exposure instrument:**

$$
\text{Futures} = \text{Synthetic Asset Position} + \text{Leverage} + \text{Daily Settlement}
$$

**Key differences from spot (cash) markets:**

1. **No capital outlay:** Don't pay full price upfront
2. **Leverage:** Control large notional with small margin
3. **Mark-to-market:** Daily settlement of gains/losses
4. **Standardization:** Exchange-traded, liquid, transparent
5. **No ownership:** No dividends, voting rights, storage costs (until delivery)

### 2. Futures vs. Spot

**The no-arbitrage relationship:**

$$
F = S \cdot e^{(r-q)T}
$$

Where:
- $F$ = Futures price
- $S$ = Spot price
- $r$ = Risk-free rate
- $q$ = Dividend yield (or convenience yield)
- $T$ = Time to expiration

**Economic interpretation:**

$$
\text{Futures Price} = \text{Spot Price} + \text{Financing Cost} - \text{Income/Benefits}
$$

**Why this matters:**

For stocks:
$$
F = S \cdot e^{(r-q)T} \approx S \cdot (1 + (r-q)T) \text{ for small } T
$$

**Example (S&P 500):**
- Spot: 4500
- Risk-free rate: 5% annual
- Dividend yield: 1.5% annual
- Time: 3 months (0.25 years)

$$
F = 4500 \cdot e^{(0.05-0.015) \times 0.25} = 4500 \cdot e^{0.00875} \approx 4539.4
$$

**Futures trade at premium of ~39 points (called "contango")**

### 3. The Cost of Carry Relationship

**The fundamental arbitrage:**

**If $F > S \cdot e^{(r-q)T}$ (futures overpriced):**

1. Buy spot asset at $S$
2. Short futures at $F$
3. Borrow at rate $r$
4. Collect dividends at rate $q$
5. **Guaranteed profit at expiration**

**If $F < S \cdot e^{(r-q)T}$ (futures underpriced):**

1. Short spot asset at $S$
2. Long futures at $F$
3. Lend at rate $r$
4. Pay dividend equivalent at rate $q$
5. **Guaranteed profit at expiration**

**Market makers constantly monitor this to prevent arbitrage opportunities!**

### 4. Futures vs. Forwards

**Forward contracts (OTC, customized):**
- Credit risk (counterparty can default)
- Illiquid (hard to exit)
- Settlement at maturity only
- No daily margin

**Futures contracts (exchange-traded):**
- Clearinghouse guarantee (no credit risk)
- Highly liquid (easy to exit)
- Daily mark-to-market
- Daily margin requirements

**The economic equivalence:**

For risk-neutral investors with no credit concerns:

$$
\text{Long Futures} \equiv \text{Long Forward} \text{ (same expected payoff)}
$$

But in practice:

$$
\text{Futures Value} > \text{Forward Value} \text{ (due to liquidity and reduced risk)}
$$

### 5. The Margin System

**Initial margin:** Performance bond deposited at entry

$$
\text{Initial Margin} = \text{Notional Value} \times \text{Margin Requirement \%}
$$

**Maintenance margin:** Minimum equity to maintain position

$$
\text{Maintenance Margin} \approx 0.75 \times \text{Initial Margin}
$$

**Margin call trigger:**

$$
\text{Account Equity} < \text{Maintenance Margin} \implies \text{Margin Call}
$$

**Example: E-mini S&P 500**

- Entry: 4500 × $50 = $225,000 notional
- Initial margin: $12,000 (5.3%)
- Maintenance margin: $9,000
- Current equity: $12,000

**After one-day move to 4440:**
- Loss: (4440 - 4500) × $50 = -$3,000
- Account equity: $12,000 - $3,000 = $9,000
- **Margin call! Must deposit $3,000 to restore to $12,000**

**The leverage ratio:**

$$
\text{Effective Leverage} = \frac{\text{Notional Value}}{\text{Initial Margin}} = \frac{\$225,000}{\$12,000} = 18.75\times
$$

**This means:**
- 1% move in futures = 18.75% return on margin
- **High reward potential, but also high risk!**

### 6. Convergence at Expiration

**The fundamental theorem of futures:**

$$
\lim_{t \to T} F_t = S_T
$$

**At expiration, futures price MUST equal spot price:**

- If $F_T > S_T$: Arbitrage (buy spot, short futures)
- If $F_T < S_T$: Arbitrage (short spot, long futures)
- Market forces ensure $F_T = S_T$ at maturity

**This convergence drives the basis:**

$$
\text{Basis}_t = S_t - F_t
$$

$$
\lim_{t \to T} \text{Basis}_t = 0
$$

### 7. Why This Perspective Matters

**Understanding futures as pure price commitments helps you:**

1. **Compare to spot markets:**
   - Futures = Spot + Leverage + No ownership benefits
   - Choose based on capital efficiency vs. ownership needs

2. **Understand basis risk:**
   - Spot and futures don't always move perfectly together
   - Basis widens/narrows creating hedging imperfections

3. **Manage roll risk:**
   - When rolling contracts, pay the "roll yield"
   - Contango hurts long positions (buy high, sell low)
   - Backwardation helps long positions (buy low, sell high)

4. **See synthetic positions:**
   - Long futures + Short puts = Synthetic long stock
   - Short futures + Long calls = Synthetic long stock
   - Futures are building blocks for complex strategies

### 8. The Strategic Advantage of Futures

**Why traders prefer futures over spot:**

**Scenario: Want $100,000 exposure to S&P 500**

**Option A: Buy SPY (spot ETF)**
- Capital required: $100,000
- Leverage: None (1:1)
- Costs: Bid-ask spread, commission
- Benefits: Own underlying, receive dividends
- Risk: Limited to capital invested

**Option B: Buy E-mini S&P futures**
- Capital required: ~$12,000 (margin)
- Leverage: ~8:1 effective
- Costs: Very tight spreads, low commissions
- Benefits: Capital efficiency, tax advantages (60/40 rule)
- Risk: **Unlimited, plus margin calls**

**The futures provide:**
- 8× capital efficiency (use $88,000 elsewhere)
- Lower transaction costs (futures more liquid)
- Favorable tax treatment (in US)
- 24-hour trading (futures markets open longer)
- **BUT: Unlimited downside + margin call risk**

**This is why sophisticated traders view futures as "pure, leveraged price exposure for tactical positioning."**

---

## Key Terminology

**Contract Specifications:**

**Underlying Asset:**
- What the futures contract represents
- Can be financial (stock indices, bonds, currencies) or physical (commodities)
- Defines delivery specifications

**Contract Size/Multiplier:**
- Standardized quantity per contract
- E-mini S&P: $50 per point
- Crude Oil: 1,000 barrels
- Gold: 100 troy ounces
- **Know this to calculate P&L!**

**Tick Size:**
- Minimum price fluctuation
- E-mini S&P: 0.25 points = $12.50
- Crude Oil: $0.01/barrel = $10
- Determines granularity of pricing

**Tick Value:**
- Dollar value of one tick

$$
\text{Tick Value} = \text{Tick Size} \times \text{Contract Multiplier}
$$

**Expiration/Delivery Date:**
- When contract expires
- Quarterly for financial futures (Mar, Jun, Sep, Dec)
- Various cycles for commodities
- Must close or roll before expiration (for financial futures)

**Settlement Method:**
- **Cash settlement:** No physical delivery (e.g., stock index futures)
- **Physical delivery:** Actual commodity delivered (e.g., crude oil, corn)
- Most traders close before expiration (avoid delivery)

**Margin Requirements:**

**Initial Margin:**
- Performance bond to enter position
- Typically 3-15% of notional value
- Set by exchange based on volatility
- Higher for volatile products

**Maintenance Margin:**
- Minimum equity to keep position open
- Usually 75-80% of initial margin
- Fall below this → Margin call

**Variation Margin:**
- Daily settlement of P&L
- Credited (gains) or debited (losses) from account
- Must maintain maintenance margin level

**Mark-to-Market:**
- Daily valuation at settlement price
- Unrealized P&L becomes realized daily
- Cash flows in/out of account daily

**Trading and Price Terminology:**

**Contango:**
- Futures price > Spot price
- Normal market structure for storable commodities
- Reflects carrying costs (storage, insurance, financing)
- Hurts long futures positions on rolls

$$
F > S \implies \text{Contango Market}
$$

**Backwardation:**
- Futures price < Spot price
- Inverted market structure
- Reflects convenience yield or supply shortage
- Benefits long futures positions on rolls

$$
F < S \implies \text{Backwardation Market}
$$

**Basis:**
- Difference between spot and futures price

$$
\text{Basis} = S_t - F_t
$$

- Basis → 0 as expiration approaches
- Basis risk = uncertainty in basis changes

**Spread:**
- Difference between two futures contracts
- Calendar spread: Same underlying, different months
- Inter-commodity spread: Related products (crack spread, crush spread)

**Roll Yield:**
- Gain or loss from rolling to next contract
- Positive in backwardation (buy low, sell high)
- Negative in contango (buy high, sell low)

$$
\text{Roll Yield} = \frac{F_{\text{near}} - F_{\text{far}}}{F_{\text{near}}} \times \frac{1}{T_{\text{roll}}}
$$

**Open Interest:**
- Total number of outstanding contracts
- Measure of liquidity and market participation
- Increases when new positions opened
- Decreases when positions closed

**Volume:**
- Number of contracts traded per day
- Measure of trading activity
- High volume = liquid, tight spreads

**Position Limits:**
- Maximum number of contracts per trader
- Prevents market manipulation
- Set by exchange and regulators
- Important for large traders

---

## Contract Specifications

**Understanding specifications is crucial for proper risk management:**

### 1. Popular Financial Futures

**E-mini S&P 500 (ES):**
- Underlying: S&P 500 Index
- Multiplier: $50 per index point
- Tick size: 0.25 points = $12.50
- Trading hours: Nearly 24/5
- Margin: ~$12,000 initial
- Settlement: Cash
- Expiration: Quarterly (H, M, U, Z)

**Example P&L:**
- Long 1 contract at 4500
- Price → 4520
- P&L: (4520 - 4500) × $50 = **+$1,000**
- On margin of $12,000 = **+8.3% return**

**E-mini Nasdaq 100 (NQ):**
- Underlying: Nasdaq 100 Index
- Multiplier: $20 per index point
- Tick size: 0.25 points = $5
- Margin: ~$17,000 initial
- More volatile than ES
- Tech-heavy exposure

**Example P&L:**
- Short 1 contract at 15000
- Price → 15100 (wrong direction!)
- P&L: (15000 - 15100) × $20 = **-$2,000**
- On margin of $17,000 = **-11.8% loss**

**10-Year Treasury Note (ZN):**
- Underlying: $100,000 face value T-note
- Tick size: 1/64 of point = $15.625
- Quote: 110-16 means 110 16/32 = 110.50
- Margin: ~$1,500 initial
- Settlement: Physical delivery (but most close)
- Inverse relationship to interest rates

**Example P&L:**
- Long 1 contract at 110-00 (110.00)
- Rates rise, price → 109-00 (109.00)
- Loss: (110 - 109) × $1,000 = **-$1,000**

### 2. Popular Commodity Futures

**Crude Oil (CL):**
- Contract size: 1,000 barrels
- Tick size: $0.01/barrel = $10
- Margin: ~$5,000 initial
- Settlement: Physical delivery at Cushing, OK
- Quote: $75.50/barrel = $75,500 notional

**Example P&L:**
- Long 1 contract at $75.00
- Price → $78.00
- Profit: ($78 - $75) × 1,000 = **+$3,000**
- On margin of $5,000 = **+60% return** (highly leveraged!)

**Gold (GC):**
- Contract size: 100 troy ounces
- Tick size: $0.10/oz = $10
- Margin: ~$10,000 initial
- Settlement: Physical delivery
- Quote: $2000/oz = $200,000 notional

**Example P&L:**
- Short 1 contract at $2000
- Price → $2050 (wrong direction!)
- Loss: ($2000 - $2050) × 100 = **-$5,000**
- On margin of $10,000 = **-50% loss**

**Corn (ZC):**
- Contract size: 5,000 bushels
- Tick size: 1/4 cent/bushel = $12.50
- Margin: ~$1,500 initial
- Settlement: Physical delivery in Chicago
- Quote: $4.50/bushel = $22,500 notional

**Example P&L:**
- Long 1 contract at $4.50/bushel
- Harvest comes in strong, price → $4.00
- Loss: ($4.00 - $4.50) × 5,000 = **-$2,500**
- On margin of $1,500 = **-167% loss (beyond initial margin!)**

### 3. Currency Futures

**Euro FX (6E):**
- Contract size: €125,000
- Tick size: $0.00005/€ = $6.25
- Margin: ~$2,500 initial
- Settlement: Physical delivery (rare)
- Quote: 1.1000 means $1.10 per euro

**Example P&L:**
- Long 1 contract at 1.1000
- Euro weakens to 1.0900
- Loss: (1.0900 - 1.1000) × 125,000 = **-$1,250**

### 4. Micro Contracts (Smaller Size)

**Many futures now have "micro" versions:**

- **Micro E-mini S&P (MES):** 1/10 size of ES ($5/point)
- **Micro E-mini Nasdaq (MNQ):** 1/10 size of NQ ($2/point)
- **Micro Gold (MGC):** 10 oz vs. 100 oz
- **Micro Crude (MCL):** 100 barrels vs. 1,000

**Benefits:**
- Lower margin requirements
- Better for smaller accounts
- Practice with real money, lower risk
- Scale position size more precisely

**Example:**
- Micro E-mini S&P at 4500
- Multiplier: $5 per point (vs. $50 for regular)
- Margin: ~$1,200 (vs. $12,000)
- 20-point move: $100 profit (vs. $1,000)

---

## Maximum Profit and Loss

### 1. Understanding the Symmetry

**Unlike options, futures have symmetric unlimited risk:**

$$
\text{P\&L}_{\text{Long}} = (S_T - F_0) \times M \times N
$$

$$
\text{P\&L}_{\text{Short}} = (F_0 - S_T) \times M \times N
$$

Where:
- $S_T$ = Settlement price at time $T$
- $F_0$ = Entry futures price
- $M$ = Contract multiplier
- $N$ = Number of contracts

### 2. Long Futures

**Maximum profit:**

$$
\text{Max Profit}_{\text{Long}} = +\infty
$$

**Theoretical maximum:**
- Stock index futures: Unlimited (indices can go to infinity)
- Commodity futures: Practically limited but very large
- Currency futures: Can double, triple, etc.

**Example (E-mini S&P):**
- Long 1 contract at 4500
- If price → 5000: Profit = (5000 - 4500) × $50 = $25,000
- If price → 6000: Profit = (6000 - 4500) × $50 = $75,000
- **No cap on upside**

**Maximum loss:**

$$
\text{Max Loss}_{\text{Long}} = -F_0 \times M \times N \text{ (if price → 0)}
$$

**Practical maximum:**
- Stock indices: Can't go to zero, but can fall 50%+
- Individual stock futures: Can approach zero
- Commodity futures: Prices can collapse (e.g., oil went negative in 2020!)

**Example (Crude Oil):**
- Long 1 contract at $75
- If price → $0: Loss = ($0 - $75) × 1,000 = **-$75,000**
- On margin of $5,000: **-1,500% loss!**
- **You owe the exchange the difference**

### 3. Short Futures

**Maximum profit:**

$$
\text{Max Profit}_{\text{Short}} = F_0 \times M \times N \text{ (if price → 0)}
$$

**Example (Gold):**
- Short 1 contract at $2000
- If price → $0 (impossible but theoretical): 
- Profit = ($2000 - $0) × 100 = **+$200,000**
- Realistically, maybe $1000 drop → **+$100,000**

**Maximum loss:**

$$
\text{Max Loss}_{\text{Short}} = -\infty
$$

**The nightmare scenario for shorts:**
- Price can go to infinity
- Unlimited loss potential
- Margin calls can wipe out account AND MORE

**Example (Natural Gas):**
- Short 1 contract at $3.00/MMBtu
- Sudden supply disruption, price → $15.00
- Loss = ($3.00 - $15.00) × 10,000 = **-$120,000**
- On margin of $2,000: **-6,000% loss**
- **Owe $118,000 beyond margin**

### 4. The Margin Call Reality

**Critical understanding: Futures losses can EXCEED your account balance!**

**The process:**

1. **Initial position:**
   - Account: $20,000
   - Long 1 E-mini S&P at 4500
   - Initial margin: $12,000
   - Available: $8,000

2. **Adverse move (4500 → 4400):**
   - Loss: (4400 - 4500) × $50 = -$5,000
   - Account equity: $20,000 - $5,000 = $15,000
   - Maintenance margin: $9,000
   - Still above maintenance ✓

3. **Continued adverse move (4400 → 4300):**
   - Additional loss: -$5,000
   - Account equity: $15,000 - $5,000 = $10,000
   - Still above maintenance ✓

4. **Further decline (4300 → 4250):**
   - Additional loss: -$2,500
   - Account equity: $10,000 - $2,500 = $7,500
   - **Below maintenance margin ($9,000)!**
   - **MARGIN CALL: Must deposit $4,500 immediately**

5. **If you don't meet margin call:**
   - Broker liquidates your position
   - Locked in loss of -$12,500
   - If slippage in liquidation, could lose more
   - **Account now at $7,500 (lost $12,500 of $20,000)**

**Worst case: Account goes negative!**

6. **Extreme move (4500 → 4200 overnight):**
   - Loss: (4200 - 4500) × $50 = -$15,000
   - Account equity: $20,000 - $15,000 = $5,000
   - **Position automatically liquidated**
   - But if market gaps and fills at 4150:
   - Actual loss: (4150 - 4500) × $50 = -$17,500
   - **Account now -$2,500 (YOU OWE THE BROKER!)**

### 5. Comparing to Options

**Long Call (for comparison):**
- Max loss: Premium paid ($500)
- Max profit: Unlimited
- Can't lose more than premium
- **No margin calls**

**Long Futures:**
- Max loss: Unlimited (down to zero)
- Max profit: Unlimited
- Can lose MORE than account
- **Margin calls can destroy you**

**The key difference:**

$$
\text{Options: Capped downside} \quad \text{vs.} \quad \text{Futures: Unlimited downside}
$$

**Risk comparison for $100,000 notional S&P exposure:**

| Scenario | Long Call Option | Long Futures |
|----------|-----------------|-------------|
| Capital required | $2,000 premium | $12,000 margin |
| -10% move | Lose $2,000 (100%) | Lose $10,000 (-83%) |
| -20% move | Lose $2,000 (100%) | Lose $20,000 (-167%, owe $8k!) |
| -30% move | Lose $2,000 (100%) | Lose $30,000 (-250%, owe $18k!) |
| +30% move | Gain $28,000 | Gain $30,000 |

**Notice:**
- Option losses capped at premium
- Futures losses can EXCEED initial margin
- Both have unlimited upside
- **Futures much riskier on downside**

---

## Entry and Exit Strategies

### 1. Entry Strategies

**1. Trend Following Entry**

**Setup:**
- Identify strong trend (moving averages, trendlines)
- Enter on pullback to support/resistance
- Use momentum indicators (RSI, MACD)

**Example (E-mini S&P):**
- Strong uptrend, 50-day MA at 4450
- Price pulls back to 4455 (near MA)
- Enter long at 4455
- Stop loss at 4430 (below MA)
- Target: 4550 (previous high)

**Risk management:**
- Position size: 1 contract max (on $50k account)
- Risk: 25 points × $50 = $1,250 (2.5% of account)
- Reward: 95 points × $50 = $4,750
- R:R = 3.8:1 ✓

**2. Breakout Entry**

**Setup:**
- Identify consolidation range
- Enter on breakout with volume confirmation
- Avoid false breakouts (wait for close above/below)

**Example (Crude Oil):**
- Trading range: $73-$77 for 2 weeks
- Breakout above $77 with high volume
- Enter long at $77.20 (confirmation)
- Stop at $76.50 (below breakout)
- Target: $80 (measured move)

**Position sizing:**
- Risk: $0.70 × 1,000 = $700 per contract
- On $30k account, max 3 contracts
- Total risk: $2,100 (7% of account - aggressive!)

**3. Mean Reversion Entry**

**Setup:**
- Identify overbought/oversold conditions
- Enter counter-trend expecting reversion
- Use Bollinger Bands, RSI, or standard deviations

**Example (Gold):**
- Gold at $2050 (upper Bollinger Band)
- RSI > 70 (overbought)
- Enter short at $2050
- Stop at $2070 (above recent high)
- Target: $2020 (middle Bollinger Band)

**Risk management:**
- Risk: $20 × 100 = $2,000 per contract
- On $50k account, 1 contract max
- Risk: 4% of account
- Reward: $30 × 100 = $3,000
- R:R = 1.5:1 (acceptable for mean reversion)

**4. Economic Data/Event Entry**

**Setup:**
- Trade around scheduled events (Fed announcements, employment data)
- Position before or immediately after
- Understand consensus expectations vs. actual

**Example (10-Year Treasury):**
- CPI report expected at 8:30am
- Consensus: +0.3%, Actual: +0.5% (hotter than expected)
- Rates likely to spike → Bond prices fall
- Enter short immediately at 110-16
- Stop at 110-24 (8/32 = $250 risk)
- Target: 109-24 (24/32 = $750 reward)

**Execution:**
- Use limit orders in fast markets (avoid slippage)
- Be prepared for volatility
- Size smaller (news trades are high risk)

**5. Spread Entry (Pairs Trading)**

**Setup:**
- Trade relative value between related contracts
- Calendar spreads (same underlying, different months)
- Inter-commodity spreads (related products)

**Example (Calendar Spread - Crude Oil):**
- Front month (March) at $75
- Back month (June) at $72
- Contango too wide (normal is $1.50 difference)
- Trade: Long June, Short March
- Bet: Spread narrows to $1.50

**P&L:**
- If spread narrows to $1.50:
- March → $74.50 (loss $0.50)
- June → $73 (gain $1.00)
- Net: +$0.50 × 1,000 = **+$500 per spread**

### 2. Exit Strategies

**1. Profit Targets (Planned Exits)**

**Fixed point targets:**
- Predetermined price level
- Based on technical levels (resistance, Fibonacci, previous highs)
- Don't be greedy, take profits when hit

**Example:**
- Long E-mini S&P at 4500
- Target: 4550 (resistance level)
- Hit target → Exit at 4550
- Profit: 50 × $50 = $2,500 ✓

**Percentage targets:**
- Exit at X% gain on notional
- Common: 2-5% for index futures, 5-10% for commodities

**Example:**
- Long Gold at $2000 ($200k notional)
- 3% target = $2060
- Hit target → Exit
- Profit: $60 × 100 = $6,000 ✓

**2. Stop Losses (Risk Management Exits)**

**Technical stop losses:**
- Below support (long) or above resistance (short)
- Below moving averages
- Based on volatility (ATR-based stops)

**Example:**
- Long Crude Oil at $75
- Support at $73.50
- Stop at $73.40 (10 cents below support)
- If hit: Loss = $1.60 × 1,000 = -$1,600

**Percentage stop losses:**
- Fixed % from entry (e.g., -2% or -3%)
- Adjust for contract volatility
- Non-negotiable rule

**Example:**
- Short E-mini Nasdaq at 15000
- 2% stop = 15300
- If hit: Loss = -300 × $20 = -$6,000
- On $100k account = -6% (acceptable max loss)

**Time stops:**
- Exit if position hasn't moved in your favor after X days
- Avoid dead money (capital tied up unproductively)

**Example:**
- Long position for 5 days, no progress
- Exit at breakeven or small loss
- Free up capital for better opportunity

**3. Trailing Stops (Protect Profits)**

**Fixed point trailing:**
- Move stop up by fixed points as profit increases
- Locks in gains while allowing upside

**Example:**
- Long E-mini S&P at 4500
- Price now 4560 (+60 points profit)
- Move stop to 4535 (guarantee +35 point profit)
- Price continues to 4580
- Move stop to 4555 (guarantee +55 point profit)
- Price reverses, stopped at 4555
- Final profit: 55 × $50 = **$2,750** (protected!)

**Percentage trailing:**
- Move stop by X% of current profit
- More dynamic, adapts to volatility

**ATR-based trailing:**
- Use Average True Range for stops
- Accounts for current volatility
- Wider stops in volatile markets, tighter in calm markets

**Example:**
- ATR (14-day) = 50 points
- Trail stop 2× ATR = 100 points
- Long at 4500, now 4600
- Stop at 4500 (100 points trailing)
- Gives room for noise while protecting

**4. Time-Based Exits**

**Before expiration (rollover):**
- Close current month, open next month
- Avoid delivery (for physical commodities)
- Typically 1-2 weeks before expiration

**Example:**
- Long December Crude Oil at $75
- November 15: Roll to January contract
- December at $76, January at $75.50
- Close December (+$1 profit)
- Open January at $75.50
- **Pay the roll cost (contango)**

**Weekly/monthly rebalancing:**
- Review all positions regularly
- Close underperforming positions
- Reposition if thesis changed

**5. Fundamental Exits**

**When fundamentals change:**
- Economic data contradicts thesis
- Company/sector news (for stock index futures)
- Geopolitical events (for commodities)

**Example:**
- Long Corn futures expecting crop shortage
- USDA report shows bumper crop
- Thesis invalidated → Exit immediately
- Don't fight the fundamentals

**6. Forced Exits (Margin Calls)**

**When equity falls below maintenance:**
- Broker issues margin call
- Deposit more funds OR close position
- If no action: Broker liquidates (at worst price!)

**How to avoid:**
- Size positions appropriately
- Use stop losses (don't rely on margin calls)
- Maintain buffer above maintenance margin
- Monitor account daily (or intraday for volatile products)

### 3. Exit Discipline

**The biggest mistake: Not having exit plan before entry**

**Professional approach:**

1. **Before entry, determine:**
   - Profit target (where to take gains)
   - Stop loss (maximum acceptable loss)
   - Time stop (how long to give the trade)

2. **Write it down:**
   - Entry: 4500
   - Target: 4550
   - Stop: 4475
   - Time: 5 days max

3. **Execute mechanically:**
   - No emotions
   - No "just a little more"
   - No "it will come back"
   - **Follow the plan!**

**Example of disciplined trading:**

**Entry:** Long E-mini S&P at 4500 (11/1)
- **Target:** 4550 (50-point gain = $2,500)
- **Stop:** 4475 (25-point loss = $1,250)
- **Time stop:** 5 trading days (11/8)
- **R:R:** 2:1 ✓

**Scenario A: Hit target on 11/3**
- Exit at 4550
- Profit: $2,500 ✓
- **Don't wait for more, TAKE IT**

**Scenario B: Hit stop on 11/2**
- Exit at 4475
- Loss: -$1,250
- **Accept it, move on**

**Scenario C: Sideways until 11/8**
- Price at 4510 (small gain)
- Time stop hit → Exit at 4510
- Profit: $500 (better than nothing)
- **Free up capital for next trade**

---



## Final Wisdom

> "Futures are the purest expression of market opinion—no time decay, no premium, just you versus price. This simplicity is both their power and their danger. With 10-20× leverage and unlimited risk, futures demand ironclad discipline. They reward the skilled and disciplined, and ruthlessly punish the reckless. Master risk management before seeking returns, or the market will teach you at the cost of your capital."

**Key to success:**

- Start small (1 contract, micro contracts)
- Rigorous position sizing (2% rule)
- Always use stops (no exceptions)
- Keep margin buffer (50% of capital unused)
- Accept losses quickly (don't hope)
- Scale up only after consistency

**Most important:** 

Futures can make you rich OR destroy you financially. The difference is discipline, risk management, and emotional control. Respect the instrument or it will humble you. 🎯📉📈

**Final warning:** Unlike options where you can only lose your premium, futures can create DEBT. You can owe money beyond your account balance. This is why professional futures traders are often MORE conservative than option traders, despite futures being "simpler." Never forget the unlimited risk! ⚠️