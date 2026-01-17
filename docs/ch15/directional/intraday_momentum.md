# Intraday Momentum


**Intraday momentum** is an options trading strategy that capitalizes on strong directional moves within a single trading session, using short-term options to capture amplified gains from rapid price acceleration with defined risk.

---

## The Core Insight


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/intraday_momentum_example.png?raw=true" alt="intraday_momentum_example" width="700">
</p>

**Figure 1:** Typical intraday momentum trade showing entry on breakout, position growth during acceleration phase, and exit before close to avoid overnight risk and theta decay.

---

## Economic


**Beyond the basic strategy, understanding the REAL economic dynamics:**

**The fundamental idea:**

- Stocks sometimes move significantly in one direction during a trading day

- Strong momentum often continues for hours (not just minutes)

- Options provide leverage to amplify these moves

- You want maximum gamma and delta exposure

- Hold position for hours, not days (avoid overnight risk)

- Exit before close to avoid assignment and theta decay

**The key equation:**

$$
\text{Intraday Profit} = \Delta \cdot \Delta S + \frac{1}{2}\Gamma \cdot (\Delta S)^2 + \mathcal{V} \cdot \Delta \sigma
$$

Where:

- $\Delta S$ = Stock price change during the session

- $\Delta \sigma$ = Implied volatility change

- Time decay (theta) minimal over hours

**You're essentially betting: "This stock will move sharply in one direction TODAY, and I'll capture it with leveraged options exposure."**

---

## Intraday Momentum Trading


**Before executing this strategy, understand the mechanics:**

### 1. Core Strategy


**Definition:** Trading options based on strong directional moves that develop during the trading session, typically holding positions for 1-6 hours and exiting before market close.

**When you trade intraday momentum:**

- You identify developing momentum (breakout, news, unusual volume)

- You buy short-dated options (often 0-7 DTE)

- You capture amplified gains from rapid moves

- You exit same day (no overnight exposure)

- Max loss = premium paid

- Profit potential = substantial for multi-point moves

**Example:**

- TSLA opens at $250, no position

- 10:30 AM: TSLA breaks $252 on heavy volume after analyst upgrade

- Strong bullish momentum developing

- Buy $252 calls (expiring Friday) for $2.50

- Cost: $2.50 × 100 = $250 per contract

**During the session:**

- 12:00 PM → TSLA at $256 → Calls now $5.50 (up 120%)

- 2:00 PM → TSLA at $258 → Calls now $7.20 (up 188%)

- 3:30 PM → Exit at $7.20 → Profit $470 per contract

### 2. Put Version


**Definition:** Using puts to capture sharp downward moves during the session.

**When you trade bearish momentum:**

- You identify weakness developing (breakdown, bad news, heavy selling)

- You buy short-dated puts

- You profit from rapid decline

- You exit same day

- Max loss = premium paid

- Profit potential = substantial for multi-point drops

**Example:**

- NVDA at $900, showing weakness

- 11:00 AM: Breaks support at $895 on volume spike

- Buy $900 puts (0 DTE) for $4.00

- Cost: $4.00 × 100 = $400

**During the session:**

- 12:30 PM → NVDA at $888 → Puts now $13.00 (up 225%)

- 2:00 PM → NVDA at $885 → Puts now $16.50 (up 313%)

- 3:45 PM → Exit at $15.00 → Profit $1,100 per contract


### 3. Momentum Options


**The deep insight:**

Intraday momentum trading is economically equivalent to **buying gamma exposure to capture price acceleration**. When you buy options for intraday moves, you're essentially:

1. **Buying convexity** (gamma) for the session

2. **Leveraging delta** for directional exposure

3. **Minimizing theta** by holding briefly

4. **Capturing volatility expansion** if momentum creates fear/greed

**Formal decomposition:**

$$
\underbrace{\text{Intraday Position Value}}_{\text{P\&L}} = \underbrace{\Delta \cdot \Delta S}_{\text{Linear gain}} + \underbrace{\frac{1}{2}\Gamma \cdot (\Delta S)^2}_{\text{Gamma gain}} + \underbrace{\mathcal{V} \cdot \Delta\sigma}_{\text{Vega gain}} - \underbrace{\Theta \cdot \Delta t}_{\text{Tiny decay}}
$$

**Why this matters:**

**Traditional day trading (stock):**

- Need $25,000 account (pattern day trader rule)

- Buy 100 shares at $250 = $25,000 exposure

- If stock → $255, gain = $500 (2% return on capital)

- **Linear exposure only, no leverage**

**Intraday options (momentum):**

- Buy 1 ATM call for $2.50 = $250 capital

- If stock → $255, call $2.50 → $7.50 gain = $500 (200% return)

- **Leveraged AND convex exposure**

**The option's gamma creates exponential P&L as momentum accelerates:**

- First $2 move → Call gains $2

- Next $2 move → Call gains $3 (delta increased!)

- Next $2 move → Call gains $4 (delta increased more!)

- **P&L accelerates with momentum (convexity)**

### 4. Example


**Setup:**

- AAPL at $180.50 at 10:00 AM

- Strong volume breakout above $180 resistance

- Buy $180 calls (2 DTE) for $3.00

- Delta = 0.55, Gamma = 0.08, Theta = -$0.15/day

**What you're really buying:**

$$
\begin{array}{lll}
\text{Economic Position} &=& \text{Delta exposure: 0.55 shares per \$1 move} \\
&+& \text{Gamma exposure: delta increases 0.08 per \$1 move} \\
&+& \text{Vega exposure: benefits from IV expansion} \\
&-& \text{Theta decay: only \$0.15/day = \$0.006/hour minimal}
\end{array}
$$

**Scenarios over 3 hours:**

| Stock Move | Stock P&L (100 shares) | Option P&L (1 contract) |
|-----------|----------------------|----------------------|
| +$5 | $500 gain | $650 gain (delta + gamma) |
| +$3 | $300 gain | $380 gain |
| +$1 | $100 gain | $110 gain |
| -$2 | $200 loss | $250 loss (max risk if exit) |

**The gamma effect:** For +$5 move:

- Simple delta: $3.00 + (0.55 × $5) = $5.75

- With gamma: $3.00 + (0.55 × $5) + (0.5 × 0.08 × 25) = $6.75

- **Actual: $6.50 (gamma adds $0.75 extra)**

### 5. Time Decay vs. Gamma


**Key relationship:**

$$
\text{Theta per hour} = \frac{\text{Theta per day}}{6.5} \quad \text{(market hours)}
$$

**For typical intraday trade:**

- Theta = -$0.20/day

- Theta per hour = -$0.03/hour

- Hold 4 hours → Theta cost = -$0.12

**Versus gamma gain:**

- Stock moves $5 in 4 hours

- Gamma gain ≈ 0.5 × 0.08 × 25 = $1.00

- **Gamma gain ($1.00) >> Theta cost ($0.12)**

**This is why intraday works:**

- Theta requires TIME to erode value

- Over hours, theta is negligible

- But gamma amplifies PRICE MOVES immediately

- **You capture gamma before theta matters**

### 6. Volatility Expansion


**The IV boost effect:**

When strong momentum develops:

$$
\text{Option Price Change} = \Delta \cdot \Delta S + \mathcal{V} \cdot \Delta \sigma
$$

**Example:**

- TSLA call at $2.50 (IV = 45%, Vega = 0.30)

- Strong breakout → IV spikes to 55% (+10 points)

- Stock moves $5 → Delta gain = 0.55 × $5 = $2.75

- IV expansion → Vega gain = 0.30 × 10 = $3.00

- **Total gain: $2.75 + $3.00 = $5.75 (vs. $2.75 without IV)**

**Why momentum creates IV expansion:**

1. Rapid moves create uncertainty

2. Market makers widen spreads

3. Demand for options spikes

4. IV rises 5-15% during strong moves

5. **Your option benefits from both price AND volatility**

### 7. Strategic Timing Advantage


**Why intraday horizon is optimal:**

**Scenario: Same $5 move over different timeframes**

**Option A: Overnight Hold**

- Buy call at close

- Hold through overnight risk

- Theta costs $0.20

- Gap risk (could open down $3)

- **Risk: Undefined, theta hurts**

**Option B: Intraday (This Strategy)**

- Buy call at 10:30 AM

- Exit at 3:30 PM

- Theta costs $0.15 (5 hours)

- No overnight risk

- **Risk: Defined, theta minimal**

**The intraday advantage:**

| Factor | Overnight | Intraday |
|--------|-----------|----------|
| Theta cost | -$0.20+ | -$0.15 |
| Gap risk | Yes (unlimited) | No |
| IV crush risk | Yes (morning) | Minimal |
| Control | Low (can't exit) | High (monitor & exit) |
| Sleep quality | Terrible | Perfect |

**This is why professionals prefer intraday momentum over swing trading options.**

---

## Key Terminology


**Momentum:**

- Persistent directional price movement

- Usually 1-3% move over hours

- Driven by volume, news, or technical breakouts

- The "fuel" for the strategy

**0 DTE (Zero Days to Expiration):**

- Options expiring same day

- Maximum gamma, maximum risk

- Ultra-sensitive to price moves

- Preferred by aggressive intraday traders

**DTE (Days to Expiration):**

- Number of days until option expires

- 0-7 DTE common for intraday

- Shorter DTE = higher gamma, lower premium

- Balance risk vs. cost

**Entry Signal:**

- Technical trigger to enter trade

- Examples: breakout, volume spike, news

- Must be objective and repeatable

- Defines risk (stop below entry)

**Exit Signal:**

- Trigger to close position

- Time-based (3:30 PM exit rule)

- Profit target (+100%, +200%)

- Stop loss (-50%)

- Momentum exhaustion (volume drop, reversal)

**Gamma Scalping:**

- Trading technique using gamma exposure

- Buy ATM options, hedge delta

- Profit from stock movement

- Related but distinct from pure momentum

**Pattern Day Trader (PDT) Rule:**

- SEC rule requiring $25k for frequent day trading

- Applies to stocks, not options (usually)

- Reason many traders use options for intraday

- Know your broker's rules

---

## Mathematical Foundation


### 1. The Profit Equation


**Intraday P&L decomposition:**

$$
\text{P\&L} = \underbrace{N \cdot \Delta \cdot \Delta S}_{\text{Delta profit}} + \underbrace{N \cdot \frac{1}{2}\Gamma \cdot (\Delta S)^2}_{\text{Gamma profit}} + \underbrace{N \cdot \mathcal{V} \cdot \Delta\sigma}_{\text{Vega profit}} - \underbrace{N \cdot \Theta \cdot \Delta t}_{\text{Theta cost}}
$$

Where:

- $N$ = Number of contracts

- $\Delta$ = Option delta

- $\Gamma$ = Option gamma

- $\mathcal{V}$ = Option vega

- $\Theta$ = Option theta

- $\Delta S$ = Stock price change

- $\Delta\sigma$ = IV change

- $\Delta t$ = Time elapsed (in days)

**For typical 4-hour hold:**

$$
\Delta t = \frac{4 \text{ hours}}{6.5 \text{ market hours}} \approx 0.62 \text{ days}
$$

**Example calculation:**

- 2 contracts, ATM calls

- Stock moves from $100 → $104 in 3 hours

- Initial: Delta = 0.50, Gamma = 0.10, Vega = 0.25, Theta = -$0.30

- IV rises from 40% → 48% (+8 points)

$$
\begin{align}
\text{Delta profit} &= 2 \times 0.50 \times 4 = \$4.00 \\
\text{Gamma profit} &= 2 \times 0.5 \times 0.10 \times 16 = \$1.60 \\
\text{Vega profit} &= 2 \times 0.25 \times 8 = \$4.00 \\
\text{Theta cost} &= 2 \times 0.30 \times 0.46 = -\$0.28
\end{align}
$$

$$
\text{Total P\&L} = \$4.00 + \$1.60 + \$4.00 - \$0.28 = \$9.32 \text{ per share}
$$

**Per contract (100 shares): $932 profit**

### 2. Why Short-Dated Options


**Gamma comparison across expirations:**

For ATM option on $100 stock:

| DTE | Gamma | Delta | Theta/day | Premium |
|-----|-------|-------|-----------|---------|
| 1 | 0.12 | 0.50 | -$0.40 | $2.00 |
| 7 | 0.08 | 0.50 | -$0.25 | $3.50 |
| 30 | 0.04 | 0.50 | -$0.15 | $5.50 |
| 90 | 0.02 | 0.50 | -$0.08 | $8.00 |

**For $4 move in 4 hours:**

$$
\text{Gamma P\&L} = \frac{1}{2}\Gamma \cdot (\Delta S)^2 = 0.5 \times \Gamma \times 16
$$

| DTE | Gamma Profit | Theta Cost (4h) | Net Benefit |
|-----|--------------|-----------------|-------------|
| 1 | $0.96 | -$0.25 | $0.71 |
| 7 | $0.64 | -$0.15 | $0.49 |
| 30 | $0.32 | -$0.09 | $0.23 |
| 90 | $0.16 | -$0.05 | $0.11 |

**Conclusion: Shorter DTE → Better for intraday due to higher gamma**

### 3. Expected Value Framework


**For profitable intraday trading:**

$$
\mathbb{E}[\text{P\&L}] = P(\text{win}) \cdot \overline{\text{Win}} - P(\text{loss}) \cdot \overline{\text{Loss}} > 0
$$

**Typical statistics for momentum traders:**

- Win rate: 40-50% (many small losses, few big wins)

- Average win: $500 per contract

- Average loss: $150 per contract (stop at -50%)

- Trades per week: 5-10

**Example expectancy:**

$$
\mathbb{E}[\text{P\&L}] = 0.45 \times \$500 - 0.55 \times \$150 = \$225 - \$82.50 = \$142.50 \text{ per trade}
$$

**This is POSITIVE expectancy despite <50% win rate!**

**Why it works:**

- Winners are 3-4x larger than losers

- Gamma amplifies big moves (fat right tail)

- Stop losses keep losers small

- **Asymmetric payoff structure**

### 4. The Break-Even Move


**Minimum move needed for profit:**

$$
\text{Breakeven} = \frac{\text{Premium} + \text{Theta cost}}{\Delta + \text{Gamma adjustment}}
$$

**For typical trade:**

- Premium: $2.50

- Theta for 4 hours: $0.15

- Delta: 0.55

- Gamma: 0.08

**Simple approximation:**

$$
\text{Breakeven move} \approx \frac{2.50 + 0.15}{0.55} \approx \$4.82
$$

**With gamma (for large move):**

$$
\text{For } \Delta S = 5: \text{Value} = 2.50 + 0.55(5) + 0.5(0.08)(25) - 0.15 = \$5.85
$$

**Profit = $5.85 - $2.50 = $3.35 per share = $335 per contract**

### 5. Risk-Reward Ratio


**Typical intraday momentum trade:**

$$
\text{Risk-Reward} = \frac{\text{Target profit}}{\text{Max loss (stop loss)}} = \frac{1.5 \times \text{premium}}{0.5 \times \text{premium}} = 3:1
$$

**Conservative version:**

- Premium: $2.50

- Stop at -50%: Max loss = $1.25 (per share)

- Target at +100%: Target profit = $2.50

- **Risk-Reward = 2:1**

**Aggressive version:**

- Premium: $2.00

- Stop at -50%: Max loss = $1.00

- Target at +200%: Target profit = $4.00

- **Risk-Reward = 4:1**

**Key insight:** Even with 40% win rate, 3:1 RR yields profit!

---

## Step-by-Step Setup


### 1. Pre-Market Scan


**1. Identify Candidates (5-10 stocks):**

- High relative volume (>2x average)

- Strong pre-market move (>1%)

- News catalyst or upcoming event

- Liquid options (tight spreads)

- Examples: TSLA, NVDA, AAPL, SPY, QQQ

**Screening criteria:**

```
Relative Volume > 2.0
Price > $50
Average Volume > 5M shares
Option Volume > 10,000 contracts
Bid-Ask Spread < $0.10 on ATM options
```

**2. Check Technical Levels:**

- Key support/resistance

- Previous day high/low

- VWAP level

- Round numbers ($100, $150, $200)

- **These become entry triggers**

**3. Review News:**

- Earnings reports

- FDA approvals

- Analyst upgrades/downgrades

- Sector rotation

- Macro events

**4. Check IV Environment:**

- Current IV percentile

- Expected moves

- Avoid IV > 80% (too expensive)

- Prefer IV 30-60% (reasonable pricing)

### 2. Opening Setup


**1. Observe First 30 Minutes:**

- Let opening volatility settle

- Watch for direction

- Identify strong trends

- **Never trade in first 15 minutes** (too chaotic)

**2. Identify Pattern:**

- **Bullish:** Higher highs, strong volume, breaks resistance

- **Bearish:** Lower lows, heavy selling, breaks support

- **Neutral:** Choppy, low volume → Skip this stock

**3. Wait for Setup:**

- Clear breakout/breakdown

- Volume confirmation (2x average on breakout)

- No immediate reversal

- **This is your entry signal**

### 3. Trade Construction


**1. Select Strike and Expiration:**

**For breakouts:**

- **Conservative:** ATM or 1 strike ITM (higher delta, lower gamma)

- **Standard:** ATM (balanced)

- **Aggressive:** 1 strike OTM (higher gamma, cheaper)

**For expiration:**

- **0 DTE:** If Friday, very aggressive

- **1-3 DTE:** Most common

- **7 DTE:** More conservative, lower gamma

**Example:**

- AAPL breaks $180 on volume

- Currently $180.50

- Buy $180 calls (2 DTE) for $3.20

- Delta = 0.58, Gamma = 0.09

**2. Determine Position Size:**

$$
\text{Contracts} = \frac{\text{Risk capital} \times \text{Risk \%}}{\text{Premium} \times 100}
$$

**Example:**

- Account: $50,000

- Risk per trade: 2% = $1,000

- Premium: $3.20

- **Max contracts: $1,000 / $320 = 3 contracts**

**3. Place Order:**

- Use limit orders (never market!)

- Bid-ask spread: $3.10 / $3.30

- Place limit at $3.20 (mid or slightly above)

- Fill quickly on momentum (don't chase)

**4. Set Mental Stops:**

- Stop loss: -50% (exit at $1.60)

- Profit target 1: +100% (exit at $6.40)

- Profit target 2: +200% (exit at $9.60)

- Time stop: 3:30 PM (no matter what)

### 4. Active Management


**1. Monitor Price Action:**

- Check every 15-30 minutes

- Don't obsess (avoid over-trading)

- Watch for momentum continuation or exhaustion

**2. Scaling Out Strategy:**

**Conservative:**

- Exit 50% at +100%

- Exit 50% at +200% or 3:30 PM

- **Locks in profit, lets winners run**

**Aggressive:**

- Hold full position until +200% or stop

- All or nothing

- Higher variance

**3. Adjust Stops:**

**If at +100% profit:**

- Move stop to breakeven ($3.20)

- Now risk-free trade

- Let remainder run

**If momentum accelerates:**

- Trail stop: -30% from peak

- Example: Peak at $8.00 → Stop at $5.60

- Captures most of move

**4. Exit Discipline:**

**Must exit if:**

- Hit stop loss (-50%)

- Hit time stop (3:30 PM)

- Momentum reverses (volume drops, opposite move)

- IV starts collapsing (bid-ask widens)

### 5. End-of-Day Exit


**1. Plan Exit Time:**

**By 3:30 PM:**

- Close all positions

- Avoid assignment risk

- Avoid after-hours gaps

- Take profits/losses

**2. Execute Exit:**

- Use limit orders

- Don't hold for "perfect" price

- Accept 95% of current bid

- **GET OUT before close**

**3. Record Trade:**

- Entry: Time, price, reasoning

- Exit: Time, price, P&L

- What worked? What didn't?

- Learn for next trade

### 6. Worked Example


**Pre-Market (8:00 AM):**

- TSLA at $245, news of China sales beat

- Pre-market high: $248

- Resistance at $250 (yesterday's high)

- Plan: Buy calls if breaks $250 after 10 AM

**Market Open (9:30-10:00 AM):**

- TSLA opens $247, immediately rallies to $249

- Heavy volume (3x average)

- Pullback to $247.50 at 10:00 AM

- Watch for $250 break

**Entry (10:45 AM):**

- TSLA breaks $250.20 on huge volume

- Buy $250 calls (3 DTE) for $4.50

- 2 contracts = $900 total risk

- Stop: $2.25 (-50%)

- Target 1: $9.00 (+100%)

- Target 2: $13.50 (+200%)

**Position Management:**

- 11:30 AM: TSLA at $253, calls at $7.00 (+55%)

- 12:15 PM: TSLA at $256, calls at $10.00 (+122%) → **Exit 1 contract at $10.00**

- 1:30 PM: TSLA at $258, calls at $12.50 (+178%)

- 2:30 PM: TSLA peaks at $259, calls at $13.00 (+189%)

- 3:15 PM: TSLA at $257.50, calls at $11.50

**Exit (3:25 PM):**

- Close remaining contract at $11.50

- Total P&L:

  - Contract 1: ($10.00 - $4.50) × 100 = $550

  - Contract 2: ($11.50 - $4.50) × 100 = $700

  - **Total: $1,250 profit on $900 risk (+139%)**

**Post-Trade:**

- Win: Yes

- Why worked: Clear breakout, volume confirmation, sustained momentum

- What next: Look for similar setups tomorrow

---

## Greeks Analysis


### 1. Delta


**What it means:**

$$
\Delta = \frac{\partial C}{\partial S} \approx \frac{\Delta C}{\Delta S}
$$

**In words:** How much option price changes for $1 stock move.

**For intraday momentum:**

- **High delta (0.60-0.80)** = More stock-like, less leverage

- **Medium delta (0.45-0.60)** = Balanced, most common

- **Low delta (0.25-0.45)** = High leverage, riskier

**Typical values:**

| Strike Type | Delta (Call) | Meaning |
|------------|-------------|---------|
| Deep ITM | 0.80-0.95 | Nearly stock equivalent |
| ATM | 0.45-0.55 | Standard choice |
| OTM | 0.25-0.45 | Lottery ticket |
| Far OTM | 0.05-0.25 | Avoid (too much decay risk) |

**Example:**

- Stock moves $3

- Delta = 0.55

- **Expected gain: 0.55 × $3 = $1.65 per share**

**Delta for puts:** Always negative (benefits from down moves)

- Put delta = -0.55

- Stock drops $3

- **Put gains: 0.55 × $3 = $1.65**

### 2. Gamma


**What it means:**

$$
\Gamma = \frac{\partial \Delta}{\partial S} = \frac{\partial^2 C}{\partial S^2}
$$

**In words:** How much delta increases as stock moves in your favor.

**Why gamma is CRITICAL for intraday:**

Gamma creates **convexity** = P&L accelerates as momentum continues.

**Example:**

- Start: Delta = 0.50, Gamma = 0.10

- Stock moves $1 → Delta becomes 0.60

- Stock moves another $1 → Delta becomes 0.70

- **Each dollar move makes next dollar more valuable**

**Gamma profit calculation:**

$$
\text{Gamma P\&L} = \frac{1}{2} \Gamma \cdot (\Delta S)^2
$$

**For $5 move with Gamma = 0.10:**

$$
\text{Gamma profit} = 0.5 \times 0.10 \times 25 = \$1.25 \text{ extra per share}
$$

**Gamma across expirations:**

| DTE | ATM Gamma | 
|-----|----------|
| 0 | 0.15-0.20 |
| 1 | 0.12 |
| 7 | 0.08 |
| 30 | 0.04 |

**For intraday: Prefer 0-3 DTE for maximum gamma**

### 3. Theta


**What it means:**

$$
\Theta = \frac{\partial C}{\partial t}
$$

**In words:** How much option loses in value per day from time decay.

**Why theta is MANAGEABLE intraday:**

$$
\text{Theta per hour} = \frac{\Theta_{\text{day}}}{6.5 \text{ hours}}
$$

**Example:**

- Theta = -$0.30/day

- Hold 4 hours

- **Cost: $0.30 × (4/6.5) = $0.18**

**Theta comparison:**

| Holding Period | Theta Cost (@ -$0.30/day) |
|---------------|--------------------------|
| 4 hours | -$0.18 |
| 1 day | -$0.30 |
| 3 days | -$0.90 |
| 1 week | -$2.10 |

**This is why holding overnight KILLS you:**

- Intraday (4h): Lose $0.18

- Overnight: Lose $0.30 (67% more!)

- Weekend: Lose $0.90 (3 days of decay)

**Important: When does theta actually accrue?**

Theta is a continuous mathematical concept, but in practice:
- Options markets are only open ~6.5 hours per day
- Theta decay is priced into market hours, not overnight
- However, overnight theta "catches up" at market open
- Weekend decay (Friday to Monday) is often priced in by Friday close

**Practical implication:**
- Friday afternoon options often cheaper (weekend decay priced in)
- Monday morning may not see additional decay beyond Friday's price
- This creates tactical opportunities for Friday afternoon shorts

**Strategy: Exit before close to avoid theta bleed**

### 4. Vega


**What it means:**

$$
\mathcal{V} = \frac{\partial C}{\partial \sigma}
$$

**In words:** How much option gains from 1% increase in IV.

**Why vega helps in momentum:**

Strong moves often expand IV:

$$
\text{Vega profit} = \mathcal{V} \times \Delta \sigma
$$

**Example:**

- Vega = $0.30

- IV rises from 45% → 55% (+10 points)

- **Vega profit: $0.30 × 10 = $3.00 per share**

**Typical IV expansion in momentum:**

| Move Size | IV Change | Vega Profit (@Vega=0.30) |
|-----------|-----------|-------------------------|
| $2 (weak) | +2-3% | $0.60-$0.90 |
| $5 (medium) | +5-8% | $1.50-$2.40 |
| $10 (strong) | +10-15% | $3.00-$4.50 |

**BUT: Vega can hurt if IV collapses:**

- Enter during IV spike (IV = 60%)

- Move stalls, IV drops to 45%

- **Vega loss: $0.30 × 15 = -$4.50**

**Best practice:** Enter when IV is NORMAL (40-50%), benefit from expansion

### 5. Greeks in Action


**Setup:**

- NVDA at $900, breakout setup

- Buy $900 calls (2 DTE) for $12.00

- Delta = 0.52, Gamma = 0.09, Theta = -$0.35, Vega = $0.28

**Scenario: Strong momentum (+$15 in 4 hours)**

**Delta contribution:**

$$
\Delta \text{ profit} = 0.52 \times 15 = \$7.80
$$

**Gamma contribution:**

$$
\Gamma \text{ profit} = 0.5 \times 0.09 \times 15^2 = 0.5 \times 0.09 \times 225 = \$10.13
$$

**Vega contribution (IV: 50% → 58%):**

$$
\mathcal{V} \text{ profit} = 0.28 \times 8 = \$2.24
$$

**Theta cost (4 hours = 0.62 days):**

$$
\Theta \text{ cost} = 0.35 \times 0.62 = -\$0.22
$$

**Total P&L:**

$$
\text{Total} = 7.80 + 10.13 + 2.24 - 0.22 = \$19.95 \text{ per share}
$$

**Call value: $12.00 → $31.95 (+166% in 4 hours)**

**Greeks summary for intraday:**

✅ **Gamma:** Your best friend (amplifies profit)
✅ **Delta:** Your baseline exposure
✅ **Vega:** Bonus if IV expands
⚠️ **Theta:** Minimal over hours, but exit before close

---

## Real-World Examples


### 1. Duration Cut via Futures


**Background:**

- Date: March 15, 2024

- TSLA closed previous day at $175

- Pre-market: Morgan Stanley upgrades to $250 target

- Opens at $178, immediate momentum

**Setup:**

- 10:15 AM: TSLA breaks $180 on huge volume

- Clear uptrend, higher highs

- Buy $180 calls (0 DTE - Friday) for $3.50

- Position: 3 contracts = $1,050 total

**Greeks at entry:**

- Delta: 0.55

- Gamma: 0.12 (0 DTE = high gamma)

- Theta: -$0.45/day

- Vega: $0.22

**Timeline:**

| Time | Stock Price | Call Value | P&L | Action |
|------|------------|-----------|-----|--------|
| 10:15 AM | $180.50 | $3.50 | $0 | Enter |
| 11:00 AM | $183.00 | $6.20 | +$810 | Hold |
| 12:00 PM | $186.50 | $9.80 | +$1,890 | Exit 1 @ $9.80 |
| 1:00 PM | $188.00 | $11.50 | - | Hold |
| 2:30 PM | $189.50 | $13.20 | - | Hold |
| 3:15 PM | $188.50 | $12.00 | - | Exit 2 @ $12.00 |

**Final results:**

- Contract 1: ($9.80 - $3.50) × 100 = $630

- Contracts 2-3: ($12.00 - $3.50) × 100 × 2 = $1,700

- **Total profit: $2,330 on $1,050 risk (+222%)**

**Why it worked:**

- Strong catalyst (upgrade)

- Clear technical breakout

- Sustained momentum

- Exited before close (avoided theta overnight)

- Used 0 DTE for maximum gamma

**Key lesson:** Let winners run but scale out to lock profits

### 2. Transition Risk Hedge


**Background:**

- Date: June 8, 2024

- AAPL at $185, weak market

- No specific news, just technical weakness

**Setup:**

- 10:30 AM: AAPL breaks $184 support on volume

- Lower lows forming

- Buy $184 puts (3 DTE) for $2.80

- Position: 4 contracts = $1,120 total

**Greeks at entry:**

- Delta: -0.48 (puts have negative delta)

- Gamma: 0.08

- Theta: -$0.25/day

- Vega: $0.30

**Timeline:**

| Time | Stock Price | Put Value | P&L | Action |
|------|------------|----------|-----|--------|
| 10:30 AM | $183.50 | $2.80 | $0 | Enter |
| 11:30 AM | $182.00 | $4.50 | +$680 | Hold |
| 12:45 PM | $180.50 | $6.80 | +$1,600 | Exit 2 @ $6.80 |
| 2:00 PM | $179.00 | $8.50 | - | Hold |
| 3:20 PM | $178.80 | $8.20 | - | Exit 2 @ $8.20 |

**Final results:**

- Contracts 1-2: ($6.80 - $2.80) × 100 × 2 = $800

- Contracts 3-4: ($8.20 - $2.80) × 100 × 2 = $1,080

- **Total profit: $1,880 on $1,120 risk (+168%)**

**Why it worked:**

- Technical breakdown clear

- Volume confirmed selling

- No countertrend rallies

- Scaled out to lock gains

**Key lesson:** Bearish momentum can be just as profitable as bullish

### 3. Portable Alpha with Futures


**Background:**

- Date: April 22, 2024

- SPY at $515, testing resistance

- Looks like breakout forming

**Setup:**

- 11:00 AM: SPY briefly touches $516 on light volume

- Buy $515 calls (5 DTE) for $4.20

- Position: 2 contracts = $840 total

**Greeks at entry:**

- Delta: 0.52

- Gamma: 0.06

- Theta: -$0.20/day

- Vega: $0.35

**Timeline:**

| Time | Stock Price | Call Value | P&L | Action |
|------|------------|-----------|-----|--------|
| 11:00 AM | $515.80 | $4.20 | $0 | Enter |
| 11:30 AM | $515.20 | $3.60 | -$120 | Hold (hope) |
| 12:15 PM | $514.50 | $2.90 | -$260 | Still hoping |
| 1:00 PM | $513.50 | $2.10 | -$420 | **Hit -50% stop** |
| 1:05 PM | - | $2.10 | -$420 | Exit @ $2.10 |

**Final result:**

- Loss: ($2.10 - $4.20) × 100 × 2 = -$420 (-50%)

**What went wrong:**

- False breakout (no volume confirmation)

- Entered too early (should wait for sustained break)

- Correctly cut loss at -50% (could've been -100%)

**Key lessons:**

- Not every breakout is real

- Volume confirmation essential

- Stop losses SAVE YOU from bigger losses

- -50% loss is acceptable (part of the game)

- **Discipline to exit saved $420 more**

### 4. Tactical Duration Extension


**Background:**

- Date: May 24, 2024

- NVDA at $1,000 before earnings

- Expecting beat and rally

**Setup:**

- 3:30 PM (day before earnings): Buy $1,000 calls (7 DTE) for $45

- IV at 75% (expensive!)

- Position: 1 contract = $4,500 total

- **Mistake: Bought expensive options**

**Earnings (after hours):**

- NVDA beats estimates

- Stock rallies to $1,050 (+5%)

- **Should be winning, right?**

**But:**

- IV crushes from 75% → 40% (-35 points)

- Call value: $45 → $38 (-15%)

**Result:**

- Stock up 5%, call DOWN 15%

- **Loss: $700 despite being RIGHT**

**Greeks explain it:**

**Vega impact:**

$$
\mathcal{V} \text{ loss} = 0.40 \times (-35) = -\$14.00
$$

**Delta gain:**

$$
\Delta \text{ profit} = 0.55 \times 50 = \$27.50
$$

**Net:**

$$
\text{Net} = 27.50 - 14.00 - \text{theta} = +\$13.00 \text{ intrinsic}
$$

**But:** Option was $45, now worth only $38 (extrinsic crushed)

**Key lessons:**

- NEVER buy options when IV > 70%

- IV crush can negate directional wins

- Check IV percentile before entering

- For earnings, sell options (collect IV), don't buy

### 5. Duration Hedge Failure


**Background:**

- Date: July 10, 2024

- QQQ at $455, sideways all morning

- No clear direction

**Morning observation:**

- 9:30-11:00 AM: QQQ in $454-$456 range

- Low volume, no momentum

- Multiple failed breakouts both ways

**Decision:**

- **NO TRADE**

- Wait for clear setup

- Preserve capital

**Afternoon:**

- Still choppy, range-bound

- No position taken

- $0 risk, $0 P&L

**Key lessons:**

- Not every day has tradeable setups

- Discipline to NOT trade is crucial

- Forcing trades = losing money

- **Best trade is sometimes no trade**

- Wait for A+ setups only

---

## Risk Management


### 1. Position Sizing Framework


**The cardinal rule:**

$$
\text{Max risk per trade} = \text{Account size} \times \text{Risk \%}
$$

**Conservative:**

- Risk 1-2% per trade

- $50k account → $500-$1,000 per trade

- Survive 50+ consecutive losses

**Standard:**

- Risk 2-3% per trade

- $50k account → $1,000-$1,500 per trade

- Survive 30+ consecutive losses

**Aggressive:**

- Risk 3-5% per trade

- $50k account → $1,500-$2,500 per trade

- Survive 20 consecutive losses

**Example calculation:**

**Account: $50,000, Risk: 2% = $1,000**

- Option premium: $3.50 per contract

- Per contract risk: $3.50 × 100 = $350

- **Max contracts: $1,000 / $350 = 2.8 → 2 contracts**

**Never round up! Always round down for safety.**

### 2. Stop Loss Rules


**Mandatory stop loss:**

$$
\text{Exit when: } \frac{\text{Current value} - \text{Entry}}{\text{Entry}} \leq -50\%
$$

**Example:**

- Entry: $4.00

- Stop: $2.00 (-50%)

- **No exceptions, no hoping**

**Why -50%?**

- Balances giving trade room vs. protecting capital

- Can recover 2 losers with 1 winner (+100%)

- Prevents complete wipeouts

- Forces discipline

**Mental vs. actual stops:**

**Mental stop (recommended):**

- You monitor and exit manually

- Flexibility if conditions change

- No stop hunting by algos

**Actual stop (risky for options):**

- Can get filled at terrible prices

- Wide bid-ask spreads = slippage

- Often better to manually monitor

**But:** Use actual stop if you can't watch constantly

### 3. Profit Taking Strategy


**Scaling out approach (recommended):**

**Level 1 (+100%):**

- Exit 50% of position

- Locks in profit equal to original risk

- Now playing with "house money"

**Level 2 (+200%):**

- Exit remaining 50%

- **Or trail stop at -30% from peak**

**Example:**

- Enter 4 contracts at $3.00 ($1,200 total)

- Hit +100%: Sell 2 at $6.00 (+$600)

- Hit +200%: Sell 2 at $9.00 (+$1,200)

- **Total: $1,800 profit (+150% on total position)**

**Alternative: All-or-nothing:**

- Hold full position until +200% or stop

- Higher variance, higher potential

- Requires strong conviction

### 4. Time-Based Stops


**Mandatory exit times:**

**Intraday close rule:**

- Exit ALL positions by 3:30 PM

- No exceptions

- Avoid overnight risk, theta decay, assignment

**Time decay rule:**

- If no significant move by 2:00 PM → Exit

- Don't hope for late-day miracle

- Preserve remaining value

**Half-time rule:**

- If 50% of trading day passed with <25% profit → Consider exit

- Example: At 1:00 PM (mid-day), still near entry → Bail

### 5. Diversification Rules


**Never concentrate:**

- Max 3 positions simultaneously

- Different sectors (not 3 tech stocks)

- Mix of calls and puts (if opportunities)

- Different expirations (reduce event risk)

**Correlation risk:**

**Bad:**

- 3 positions: NVDA, AMD, AVGO (all semiconductors)

- All move together → Concentrated risk

**Good:**

- TSLA (auto), AAPL (tech), XLE (energy)

- Different sectors → True diversification

### 6. The Kelly Criterion


**Optimal position size:**

$$
f^* = \frac{p \cdot b - q}{b}
$$

Where:

- $f^*$ = Fraction of capital to risk

- $p$ = Win probability

- $q$ = Loss probability = $1 - p$

- $b$ = Win/loss ratio

**Example:**

- Win rate: 45% ($p = 0.45$)

- Loss rate: 55% ($q = 0.55$)

- Avg win: $500, Avg loss: $150

- $b = 500/150 = 3.33$

$$
f^* = \frac{0.45 \times 3.33 - 0.55}{3.33} = \frac{1.50 - 0.55}{3.33} = 0.285
$$

**Interpretation: Risk 28.5% of capital per trade**

**But:** This is too aggressive for most! Use **Half Kelly:**

$$
\text{Half Kelly} = 0.285 / 2 = 14.25\% \text{ (still very aggressive)}
$$

**Conservative Kelly: Use 1/4 to 1/10 of Kelly**

$$
\text{Conservative} = 0.285 / 4 = 7.1\%
$$

**For $50k account: $3,550 per trade (still quite aggressive)**

**Practical: Most traders use fixed 2-3% regardless of Kelly**

### 7. Risk Management Checklist


**Before entering trade:**

✅ Is position size ≤ 2-3% of account?
✅ Is stop loss clearly defined (-50%)?
✅ Is profit target realistic (+100% minimum)?
✅ Is there clear entry signal (breakout, volume)?
✅ Is IV reasonable (<60%)?
✅ Can I monitor trade during session?
✅ Is there a time stop (3:30 PM)?
✅ Am I diversified (not all in one sector)?

**If ANY answer is NO → Don't trade**

**During trade:**

✅ Is stop loss still valid?
✅ Is momentum continuing?
✅ Should I scale out (at +100%)?
✅ Is it approaching 3:30 PM?

**At end of day:**

✅ All positions closed by 3:30 PM?
✅ Trade logged with notes?
✅ What worked? What didn't?
✅ Emotional state check (revenge trading)?

---



## Final Wisdom


> "Intraday momentum trading is the most time-intensive but also one of the most rewarding option strategies. It requires you to be right on direction AND timing, demands constant monitoring, and is unforgiving of mistakes. BUT it offers maximum gamma exposure with minimum theta cost, no overnight risk, and the ability to compound capital quickly. Master this and you have a powerful tool in your arsenal. The key is discipline: honor your stops, exit before close, and never let a winner turn into a loser overnight."

**Key to success:**

- High-conviction trades only (clear setups)

- Proper position sizing (2-3% max)

- Ironclad discipline (stops, time stops)

- Active monitoring (can't be passive)

- Exit by 3:30 PM (no exceptions)

- Learn from every trade (keep journal)

**Most important:** This strategy is for active traders who can watch positions during market hours. If you can't monitor actively, use longer-term strategies instead! 🎯📊⚡

**CRITICAL RULE: Never, ever hold intraday positions overnight. This single rule prevents 90% of disasters.**