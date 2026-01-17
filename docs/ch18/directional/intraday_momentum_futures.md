# Intraday Momentum with Futures

**Intraday momentum trading with futures** exploits short-horizon directional persistence within the trading day using highly liquid, leveraged instruments, relying on execution efficiency, volatility-adjusted sizing, and disciplined risk management to capture profits from systematic price continuation patterns that emerge from opening imbalances, news events, and institutional order flow.

---

## The Core Insight

**The fundamental idea:**

- Intraday price movements exhibit autocorrelation (momentum persists within the day)
- Opening imbalances signal direction for the session
- Institutional order flow creates predictable price impact
- News-driven moves tend to continue as information diffuses
- Futures provide efficient, low-cost access to intraday momentum
- Flat overnight eliminates gap risk and overnight funding costs
- Transaction costs are the primary edge erosion factor

**The key equation:**

$$
\text{Signal}_t = f(r_{t-\Delta,t}, V_{t-\Delta,t}, \text{Market Context}_t)
$$

Where short-horizon return momentum combines with volume and market regime:

$$
\text{Momentum Signal} = \text{sign}(P_t - P_{t-\Delta}) \times \mathbb{1}_{\{V_t > \bar{V}\}}
$$

**You're essentially betting: "The direction established in the first portion of the trading day will continue, and I can capture a portion of this move before reversal or session close."**

---

## What Is Intraday Momentum?

**Before implementing intraday momentum, understand the strategy mechanics:**

### 1. Core Concept

**Definition:** A day trading strategy that identifies directional price movements during the trading session and takes positions in the direction of that momentum, exiting by session close to avoid overnight exposure.

**When you trade intraday momentum with futures:**

- You identify momentum direction using early session activity
- You confirm signals with volume and volatility
- You enter positions after confirmation
- You hold until target, stop, or session close
- You flat all positions before market close
- You size positions based on intraday volatility

**Example - E-mini S&P 500 (ES):**

- Opening price (9:30 AM): 4,520
- First 30-minute high: 4,535
- First 30-minute low: 4,515
- Opening range: 20 points
- Price at 10:00 AM: 4,540 (breaks above range)
- Signal: Long (upside breakout)
- Intraday volatility: 15 points/hour (typical)
- Target: 4,560 (20 points = 1 opening range)
- Stop: 4,525 (below breakout level)

**Trade setup:**

- Entry: Long ES at 4,540
- Stop: 4,525 (-15 points, 0.33%)
- Target: 4,560 (+20 points, 0.44%)
- Exit: By 3:30 PM regardless of P&L

### 2. Opening Range Momentum

**Definition:** Trading breakouts from the initial price range established in the first 15-30 minutes.

**The opening range:**

$$
\text{OR} = [\text{Low}_{9:30-10:00}, \text{High}_{9:30-10:00}]
$$

**Entry signals:**

$$
\text{Signal} = \begin{cases}
+1 & \text{if } P_t > \text{OR}_{\text{High}} + \epsilon \\
-1 & \text{if } P_t < \text{OR}_{\text{Low}} - \epsilon \\
0 & \text{otherwise}
\end{cases}
$$

Where $\epsilon$ is a small buffer (1-2 ticks) to filter noise.

**Example - Nasdaq 100 (NQ):**

- 9:30 AM open: 15,800
- OR high (by 10:00 AM): 15,850
- OR low (by 10:00 AM): 15,750
- OR width: 100 points
- 10:05 AM price: 15,860 (+10 above OR high)
- Signal: Long confirmed
- Entry: 15,860
- Stop: 15,740 (below OR low)
- Target 1: 15,960 (1x OR width)
- Target 2: 16,060 (2x OR width)

### 3. First-Hour Momentum

**Definition:** Extending momentum signals beyond opening range to include first-hour trends.

**The statistic:**

$$
\text{First-Hour Return} = \frac{P_{10:30} - P_{9:30}}{P_{9:30}}
$$

**Empirical finding:**

$$
\text{Corr}(\text{First-Hour Return}, \text{Rest-of-Day Return}) \approx 0.15-0.25
$$

**Trading rule:**

- If first-hour return > +0.5%: Go long
- If first-hour return < -0.5%: Go short
- Hold until session close or stop hit

**Example - Crude Oil (CL):**

- 9:00 AM open: $78.00
- 10:00 AM price: $78.75 (+0.96%)
- Signal: Long (strong first-hour momentum)
- Entry: $78.75
- Stop: $78.25 (-0.64%)
- Target: Trailing stop or 2:00 PM exit

### 4. Tick Momentum and Market Internals

**Definition:** Using market breadth and order flow indicators to confirm momentum.

**NYSE TICK indicator:**

$$
\text{TICK} = \text{Upticks} - \text{Downticks} \quad \text{(across all NYSE stocks)}
$$

**Signal interpretation:**

- TICK > +500: Strong buying pressure
- TICK < -500: Strong selling pressure
- Sustained readings signal persistent momentum

**Trading integration:**

$$
\text{Entry Confidence} = \text{Price Signal} \times \text{TICK Confirmation}
$$

**Example:**

- ES breaks above opening range (+1 signal)
- TICK readings consistently > +400
- Confirmation: High confidence long entry
- If TICK diverges (falling while price rises): Reduce size or skip

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/intraday_momentum_futures.png?raw=true" alt="intraday_momentum_futures" width="700">
</p>
**Figure 1:** Intraday momentum trading showing opening range formation, breakout entry, volume confirmation, and the characteristic pattern of continuation with entry, stop, and target levels marked.

---

## Economic Rationale

**Beyond the basic mechanics, understanding WHY intraday momentum exists:**

### 1. The Information Diffusion Model

**The deep insight:**

Intraday momentum exists because information gets incorporated into prices gradually, not instantaneously:

1. **News release:** Information enters the market
2. **Early movers:** Informed traders act first
3. **Price impact:** Initial move occurs
4. **Diffusion:** Other participants observe and react
5. **Continuation:** Additional buying/selling extends the move
6. **Equilibrium:** Price eventually stabilizes at new level

**Formal representation:**

$$
P_t = P_0 + \sum_{s=1}^{t} \lambda^{t-s} I_s + \epsilon_t
$$

Where $I_s$ is information arriving at time $s$ and $\lambda < 1$ represents gradual incorporation.

**Key insight:** The partial adjustment creates autocorrelation in returns.

$$
\text{Autocorrelation} = \text{Corr}(r_t, r_{t-1}) > 0
$$

### 2. The Institutional Order Flow Effect

**Why large orders create momentum:**

Institutional investors cannot execute large orders instantaneously:

$$
\text{Institutional Order} = \sum_{t=1}^{T} q_t
$$

Where $q_t$ is the quantity executed in period $t$.

**Price impact model:**

$$
\Delta P_t = \gamma \sqrt{\frac{q_t}{V_t}} + \epsilon_t
$$

Where $V_t$ is market volume and $\gamma$ is the impact coefficient.

**Result:** Large orders execute over hours, creating sustained price pressure and momentum.

**Example:**

- Pension fund needs to buy $500M of ES futures
- Average daily volume: $50B
- Order represents 1% of daily volume
- Executed over 4 hours
- Creates consistent buying pressure
- Momentum traders can profit by front-running the continuation

### 3. The Opening Imbalance Mechanism

**Why opening ranges predict daily direction:**

**Pre-market information:**

$$
\text{Opening Price} = \text{Prior Close} + \text{Overnight Information} + \text{Gap}
$$

**First 30 minutes:**

- Market digests overnight news
- Institutional orders arrive
- Price discovery occurs
- Range establishes support/resistance

**Breakout interpretation:**

$$
P > \text{OR}_{\text{High}} \Rightarrow \text{Demand exceeds supply at OR levels}
$$

This signals that buyers are willing to pay higher prices, indicating continued upward pressure.

**Empirical statistics (ES futures, 2015-2024):**

| Breakout Type | Follow-Through Rate | Average Move |
|---------------|---------------------|--------------|
| Upside breakout | 58% | +0.42% |
| Downside breakout | 56% | -0.38% |
| No breakout | 50% (random) | ±0.15% |

### 4. The Volatility Clustering Effect

**Intraday volatility clustering:**

$$
\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2
$$

**Implication:**

- High volatility begets high volatility (within day)
- Strong morning moves predict volatile afternoons
- Momentum strategies work better in trending volatile environments

**Regime identification:**

$$
\text{Morning Volatility} = \text{Range}_{9:30-11:00} / \text{20-day Average Range}
$$

- Ratio > 1.2: High volatility day (trade momentum aggressively)
- Ratio 0.8-1.2: Normal day (standard position sizes)
- Ratio < 0.8: Low volatility day (reduce activity)

### 5. The Feedback Loop Mechanism

**Why momentum is self-reinforcing:**

1. **Initial move:** Price rises on buying
2. **Stop triggers:** Shorts cover at stops (more buying)
3. **FOMO entries:** Momentum traders join (more buying)
4. **Algorithmic participation:** Momentum algos detect signal (more buying)
5. **Acceleration:** Price continues rising

**Formal model:**

$$
r_t = \alpha + \beta r_{t-1} + \gamma \cdot \text{Stop Density}_{t-1} + \epsilon_t
$$

Higher stop density above current price predicts stronger upward momentum.

---

## Signal Construction

**Building robust intraday momentum signals:**

### 1. The Complete Signal Framework

**Multi-factor signal:**

$$
\text{Composite Signal} = w_1 \cdot S_{\text{OR}} + w_2 \cdot S_{\text{VWAP}} + w_3 \cdot S_{\text{Vol}} + w_4 \cdot S_{\text{Tick}}
$$

Where:
- $S_{\text{OR}}$ = Opening range breakout signal
- $S_{\text{VWAP}}$ = VWAP deviation signal
- $S_{\text{Vol}}$ = Volume confirmation signal
- $S_{\text{Tick}}$ = Market internals signal

**Typical weights:**

| Component | Weight | Description |
|-----------|--------|-------------|
| OR breakout | 0.40 | Primary signal |
| VWAP | 0.25 | Institutional reference |
| Volume | 0.20 | Confirmation |
| TICK | 0.15 | Breadth |

### 2. Opening Range Breakout Signal

**Standard OR signal:**

$$
S_{\text{OR}} = \begin{cases}
+1 & \text{if } P_t > \text{OR}_{\text{High}} + 0.1\% \\
-1 & \text{if } P_t < \text{OR}_{\text{Low}} - 0.1\% \\
0 & \text{otherwise}
\end{cases}
$$

**Enhanced OR signal with failed breakout filter:**

$$
S_{\text{OR,enhanced}} = S_{\text{OR}} \times \mathbb{1}_{\{\text{No prior failed breakout}\}}
$$

If price already broke and reversed, skip the second attempt.

### 3. VWAP Deviation Signal

**Volume-Weighted Average Price:**

$$
\text{VWAP}_t = \frac{\sum_{i=1}^{t} P_i \times V_i}{\sum_{i=1}^{t} V_i}
$$

**Signal based on deviation:**

$$
S_{\text{VWAP}} = \begin{cases}
+1 & \text{if } P_t > \text{VWAP}_t + 1\sigma_{\text{VWAP}} \\
-1 & \text{if } P_t < \text{VWAP}_t - 1\sigma_{\text{VWAP}} \\
0 & \text{otherwise}
\end{cases}
$$

**Interpretation:**

- Price above VWAP + 1σ: Strong buying, institutions paying up
- Price below VWAP - 1σ: Strong selling, institutions liquidating

### 4. Volume Confirmation Signal

**Relative volume:**

$$
\text{RVOL}_t = \frac{V_t}{\bar{V}_{t,\text{historical}}}
$$

Where $\bar{V}_{t,\text{historical}}$ is the average volume at that time of day.

**Confirmation rule:**

$$
S_{\text{Vol}} = \begin{cases}
+1 & \text{if RVOL} > 1.5 \text{ and price rising} \\
-1 & \text{if RVOL} > 1.5 \text{ and price falling} \\
0 & \text{if RVOL} < 1.2
\end{cases}
$$

**Key insight:** Breakouts on low volume often fail. Require RVOL > 1.5 for confirmation.

### 5. Market Internals Signal

**NYSE TICK-based signal:**

$$
S_{\text{Tick}} = \begin{cases}
+1 & \text{if 5-min TICK average} > +300 \\
-1 & \text{if 5-min TICK average} < -300 \\
0 & \text{otherwise}
\end{cases}
$$

**TICK divergence warning:**

$$
\text{Divergence} = \text{sign}(r_t) \neq \text{sign}(\text{TICK}_t)
$$

If price rising but TICK falling: Caution, potential reversal.

### 6. Regime Filter

**Trade only in favorable regimes:**

**VIX filter:**

$$
\text{Trade} = \mathbb{1}_{\{\text{VIX} > 12 \text{ and VIX} < 35\}}
$$

- VIX < 12: Too quiet, momentum weak
- VIX > 35: Too chaotic, whipsaws likely

**Trend filter:**

$$
\text{Trade Long} = \mathbb{1}_{\{\text{ES} > \text{5-day MA}\}}
$$
$$
\text{Trade Short} = \mathbb{1}_{\{\text{ES} < \text{5-day MA}\}}
$$

Trade momentum in direction of short-term trend.

---

## Position Sizing

**Critical for intraday trading due to high frequency:**

### 1. Intraday Volatility-Based Sizing

**The formula:**

$$
\text{Position Size} = \frac{R^* \times \text{Account}}{\sigma_{\text{intraday}} \times \text{Contract Value}}
$$

Where:
- $R^*$ = Target risk per trade (typically 0.5-1%)
- $\sigma_{\text{intraday}}$ = Expected intraday volatility

**Example - ES futures:**

- Account: $100,000
- Target risk: 0.5% = $500
- Intraday volatility: 30 points
- Contract value: $50 per point
- Dollar volatility: 30 × $50 = $1,500
- Position size: $500 / $1,500 = 0.33 contracts → 1 contract minimum

### 2. ATR-Based Position Sizing

**Using Average True Range:**

$$
\text{ATR}_{\text{intraday}} = \text{Average of hourly true ranges}
$$

**Position calculation:**

$$
\text{Contracts} = \frac{\text{Max Risk}}{\text{Stop Distance} \times \text{Dollar per Point}}
$$

**Example - NQ futures:**

- Max risk: $750
- Stop distance: 30 points (1.5 × hourly ATR)
- Dollar per point: $20
- Contracts: $750 / (30 × $20) = 1.25 → 1 contract

### 3. Kelly Criterion for Intraday

**Optimal position sizing:**

$$
f^* = \frac{p \cdot b - (1-p)}{b}
$$

Where:
- $p$ = Win rate
- $b$ = Average win / Average loss ratio

**Example:**

- Win rate: 55%
- Average win: $400
- Average loss: $300
- b = $400 / $300 = 1.33
- f* = (0.55 × 1.33 - 0.45) / 1.33 = 0.21

**Interpretation:** Optimal to risk 21% of capital per trade.

**Practical adjustment:** Use half-Kelly (10%) to account for estimation error.

### 4. Scaling Based on Conviction

**Tiered position sizing:**

| Signal Strength | Confirmation | Position Size |
|-----------------|--------------|---------------|
| OR + VWAP + Vol + Tick | All aligned | 1.0x (full) |
| OR + VWAP + Vol | 3 of 4 | 0.75x |
| OR + Vol | 2 of 4 | 0.50x |
| OR only | 1 of 4 | 0.25x or skip |

**Example:**

- Full position: 4 contracts
- High conviction (all signals): 4 contracts
- Medium conviction (3 signals): 3 contracts
- Low conviction (2 signals): 2 contracts
- Very low (1 signal): Skip or 1 contract

### 5. Daily Risk Limits

**Aggregate risk management:**

$$
\text{Daily Loss Limit} = 2\% \text{ of Account}
$$

**Implementation:**

- After 2% daily loss, stop trading
- After 2 consecutive losing days, reduce size by 50%
- After 5% weekly loss, stop trading for the week

**Example:**

- Account: $100,000
- Daily limit: $2,000
- First loss: -$800 (continue)
- Second loss: -$700 (continue, total -$1,500)
- Third loss: -$600 (stop, total -$2,100 > limit)

---

## Entry and Exit Rules

**Precise execution is critical for intraday trading:**

### 1. Entry Timing Rules

**Optimal entry windows:**

| Window | Time (ET) | Character | Entry Quality |
|--------|-----------|-----------|---------------|
| Opening | 9:30-10:00 | High vol, establish range | Setup formation |
| Early momentum | 10:00-11:00 | Breakout confirmation | Best entry |
| Midday | 11:00-14:00 | Low vol, range-bound | Avoid entries |
| Afternoon momentum | 14:00-15:30 | Second wave | Secondary entry |
| Close | 15:30-16:00 | Position squaring | Exit only |

**Rule: 80% of entries should occur 10:00-11:00 AM**

### 2. Entry Execution

**Market vs. Limit:**

**Market order scenarios:**

- Strong momentum with volume
- Missing the move is worse than slippage
- Signal confidence high

**Limit order scenarios:**

- Testing breakout level
- Pullback entry after confirmation
- Signal confidence moderate

**Example - Limit entry:**

- OR high: 4,520
- Breakout confirmed at 4,525
- Place limit buy at 4,522 (pullback to OR high)
- If not filled in 5 minutes, market buy at current price

### 3. Stop Loss Placement

**Fixed stop:**

$$
\text{Stop} = \text{Entry} - k \times \text{ATR}_{\text{hourly}}
$$

Where $k$ typically 1.5-2.5.

**Structural stop:**

- Long entry: Stop below OR low or prior swing low
- Short entry: Stop above OR high or prior swing high

**Example:**

- Long entry: 4,540
- OR low: 4,515
- ATR stop (2x): 4,540 - 2×10 = 4,520
- Structural stop: 4,512 (below OR low)
- **Use**: 4,520 (tighter, but above key level)

### 4. Profit Target Strategies

**Fixed target:**

$$
\text{Target} = \text{Entry} + R \times \text{Stop Distance}
$$

Where R is the reward-to-risk ratio (typically 1.5-2.0).

**OR-based target:**

- Target 1: 1 × OR width (take 50% off)
- Target 2: 2 × OR width (take remaining)

**Trailing stop:**

$$
\text{Trail} = \max(\text{Highest Price Since Entry}) - k \times \text{ATR}
$$

**Example:**

- Entry: 4,540
- Stop: 4,520 (20-point risk)
- Target 1: 4,570 (30 points, 1.5R) - exit 50%
- Trail remainder: High water mark - 15 points

### 5. Time-Based Exits

**Mandatory exits:**

- 3:45 PM: Begin closing all positions
- 4:00 PM: Must be flat

**Conditional time exits:**

- If in profit at 2:00 PM: Move stop to breakeven
- If flat (not triggered) at 2:30 PM: Consider skip

### 6. Exit Execution

**Scaling out:**

| Price Level | Action | Position |
|-------------|--------|----------|
| Entry | Full position | 100% |
| Target 1 | Sell 50% | 50% |
| Target 2 | Sell 25% | 25% |
| Trail stop hit | Sell remaining | 0% |

**Emergency exit:**

If broader market tanks (ES down 2%+ intraday):
- Exit immediately regardless of P&L
- Reassess before re-entry

---

## Transaction Cost Analysis

**Costs are critical for intraday strategies:**

### 1. Cost Components

**Total cost per round-trip:**

$$
\text{Cost} = 2 \times (\text{Commission} + \text{Half Spread} + \text{Slippage})
$$

**ES futures example:**

| Component | Cost per Side | Round-Trip |
|-----------|---------------|------------|
| Commission | $2.50 | $5.00 |
| Half spread | $12.50 (1 tick) | $25.00 |
| Slippage | $6.25 (0.5 tick) | $12.50 |
| **Total** | **$21.25** | **$42.50** |

### 2. Cost as Percentage of Trade

**Break-even analysis:**

$$
\text{Break-even Move} = \frac{\text{Round-Trip Cost}}{\text{Contract Value}}
$$

**ES example:**

- Cost: $42.50
- Contract value: $50 per point
- Break-even: $42.50 / $50 = 0.85 points

**Implication:** Need 0.85+ point move just to break even.

### 3. Annual Cost Impact

**Estimate for active trader:**

- Trades per day: 4
- Trading days: 250
- Annual trades: 1,000
- Cost per trade: $42.50
- **Annual cost: $42,500**

On $100,000 account: **42.5% annual drag from costs!**

### 4. Cost-Adjusted Strategy Design

**Implications:**

1. Fewer trades: Quality over quantity
2. Larger targets: Need 2R+ to overcome costs
3. Better instruments: Liquid futures with tight spreads
4. Optimal execution: Limit orders where possible

**Cost-adjusted expected value:**

$$
\mathbb{E}[\text{Net Profit}] = p \times W - (1-p) \times L - C
$$

Where $C$ is cost per trade.

**Example:**

- Win rate: 55%
- Average win: $300
- Average loss: $200
- Cost: $42.50

Net = 0.55 × $300 - 0.45 × $200 - $42.50 = $165 - $90 - $42.50 = $32.50

Still positive, but costs eat 56% of gross edge!

---

## Risk Management

**Survival is the first priority:**

### 1. Position-Level Risk

**Maximum risk per trade:**

$$
\text{Max Risk} = 0.5\% \times \text{Account Equity}
$$

**Example:**

- Account: $100,000
- Max risk: $500 per trade
- Stop distance: 20 points (ES)
- Dollar risk: 20 × $50 = $1,000 per contract
- Position limit: 0.5 contracts → round to 1 but accept higher risk

### 2. Daily Risk Limits

**Hard stop rules:**

| Metric | Limit | Action |
|--------|-------|--------|
| Daily loss | 2% | Stop trading |
| Consecutive losses | 3 trades | Stop for 30 minutes |
| Win streak | 5 trades | Take break, avoid overconfidence |

**Example implementation:**

- Start of day: $100,000
- Trade 1: -$400
- Trade 2: -$500
- Trade 3: -$600
- **Stop**: -$1,500 < 2% limit, but 3 consecutive losses. Take 30-minute break.
- Trade 4: +$700
- Trade 5: -$800
- **Total: -$1,600 (1.6%)**: Continue cautiously.

### 3. Drawdown Management

**Equity curve monitoring:**

$$
\text{Drawdown} = \frac{\text{Peak Equity} - \text{Current Equity}}{\text{Peak Equity}}
$$

**Response protocol:**

| Drawdown | Response |
|----------|----------|
| 0-5% | Normal trading |
| 5-10% | Reduce size by 25% |
| 10-15% | Reduce size by 50% |
| 15-20% | Paper trade only |
| >20% | Stop, review strategy |

### 4. Correlation with Market

**Avoid correlated losses:**

Track correlation of your P&L with ES:

$$
\rho(\text{P\&L}, \text{ES return})
$$

- If ρ > 0.5: You're essentially long the market
- Diversify by trading other products (bonds, commodities)

### 5. Circuit Breakers

**Personal circuit breakers:**

1. **Loss limit hit**: No more trading today
2. **Consecutive losses**: Break before next trade
3. **Fat finger check**: Confirm size before execution
4. **Tech failure**: Close all positions, assess
5. **News surprise**: Exit immediately, reassess

---

## Regime Analysis

**Performance varies dramatically by market regime:**

### 1. Favorable Regimes

**High momentum environments:**

- FOMC announcement days
- NFP release days
- Earnings season (sector momentum)
- VIX 15-25 (enough movement, not chaotic)

**Example - FOMC day:**

- Pre-announcement range: Narrow (waiting)
- Post-announcement: Explosive move
- Continuation rate: 65%+ (higher than normal)
- **Strategy**: Wait for decision, trade the breakout aggressively

### 2. Unfavorable Regimes

**Low momentum environments:**

- Summer doldrums (July-August)
- Holiday weeks
- VIX < 12 (no volatility)
- Range-bound markets (50-day range compression)

**Strategy adjustments:**

- Reduce position size by 50%
- Require stronger confirmation
- Accept fewer trades
- Consider taking the day off

### 3. Dangerous Regimes

**Avoid trading entirely:**

- VIX > 35 (too chaotic)
- Flash crash conditions
- Liquidity crises
- Technical failures at exchanges

**Warning signs:**

- Bid-ask spreads widening 3x normal
- ES moving 10+ points per minute
- Circuit breakers triggered
- News of major failures

### 4. Regime Detection Framework

**Daily regime assessment:**

| Indicator | Trending Day | Range Day | Avoid |
|-----------|--------------|-----------|-------|
| VIX | 15-25 | 10-15 | >30 |
| First hour range | >0.7% | <0.4% | >1.5% |
| Volume | >1.2x average | <0.8x | >2x spike |
| Gap | <0.5% | >1% (often fades) | >2% |

**Decision matrix:**

- 3+ trending indicators: Full activity
- 2 trending, 1 range: Normal activity
- 2+ range indicators: Reduced activity
- 1+ avoid indicators: Do not trade

---

## Case Studies

**Real-world examples of intraday momentum:**

### 1. Classic Opening Range Breakout - September 2023

**Setup:**

- Date: September 13, 2023 (CPI release day)
- Pre-market: ES at 4,480, awaiting 8:30 AM CPI
- CPI release: Higher than expected
- Immediate reaction: Gap down to 4,450

**Opening range (9:30-10:00 AM):**

- OR high: 4,465
- OR low: 4,440
- OR width: 25 points

**Trade:**

- 10:05 AM: Price breaks below 4,437 (below OR low)
- Entry: Short at 4,435
- Stop: 4,468 (above OR high)
- Risk: 33 points = $1,650/contract

**Execution:**

| Time | Price | Action |
|------|-------|--------|
| 10:05 | 4,435 | Enter short |
| 10:45 | 4,410 | Target 1 hit (1x OR), exit 50% |
| 11:30 | 4,395 | Trail stop triggered, exit remaining |

**Result:**

- First half: +25 points × $50 = +$1,250
- Second half: +40 points × $50 = +$2,000
- **Total: +$3,250 on 2 contracts (before costs)**
- **Risk-adjusted: 1.97R**

**Key lessons:**

- CPI days have high momentum potential
- Wait for OR to form, don't anticipate
- Scale out to lock profits

### 2. Failed Breakout - October 2023

**Setup:**

- Date: October 5, 2023 (quiet day, no major news)
- ES overnight range: Tight
- VIX: 18

**Opening range (9:30-10:00 AM):**

- OR high: 4,320
- OR low: 4,305
- OR width: 15 points (narrow)

**Trade attempt:**

- 10:10 AM: Price breaks to 4,323 (above OR high)
- Entry: Long at 4,322
- Stop: 4,302 (below OR low)
- Target: 4,345 (1.5x OR)

**What happened:**

| Time | Price | Situation |
|------|-------|-----------|
| 10:10 | 4,322 | Enter long |
| 10:25 | 4,328 | High of move (+6 points) |
| 10:45 | 4,318 | Back in OR range |
| 11:00 | 4,305 | Test OR low |
| 11:15 | 4,301 | Stop hit |

**Result:**

- Loss: -21 points × $50 = -$1,050
- **Risk-adjusted: -1.0R (full loss)**

**What went wrong:**

1. Narrow OR (15 points) → More prone to false breaks
2. No volume surge on breakout (RVOL = 0.9)
3. TICK reading: Only +200 (weak)
4. VIX at 18 but falling → Momentum dying

**Key lessons:**

- Narrow ORs require extra confirmation
- Volume must confirm breakout
- Check TICK for breadth support
- Some days just don't work

### 3. News-Driven Momentum - March 2023

**Setup:**

- Date: March 10, 2023
- Event: SVB bank failure news breaks
- Time: Pre-market (before open)
- ES futures: Gapping down 60+ points

**Opening range (9:30-10:00 AM):**

- Open: 3,880 (major gap down)
- OR high: 3,905
- OR low: 3,850
- OR width: 55 points (huge!)

**Trade:**

- Decision: Wait for OR to form given extreme volatility
- 10:15 AM: Price at 3,840 (below OR low)
- Entry: Short at 3,838
- Stop: 3,910 (above OR high)
- Risk: 72 points = $3,600/contract (too large!)
- **Adjustment**: Reduce to half size

**Execution:**

| Time | Price | Action |
|------|-------|--------|
| 10:15 | 3,838 | Enter short (half size) |
| 11:00 | 3,780 | Down 58 points, trail stop to 3,850 |
| 12:00 | 3,750 | Lunch, trail to 3,800 |
| 14:00 | 3,720 | Trail to 3,760 |
| 15:30 | 3,750 | Trail stop hit, exit |

**Result:**

- Gain: 88 points × $50 × 0.5 = +$2,200
- **On reduced risk due to volatility**

**Key lessons:**

- Crisis days have massive momentum
- Reduce size when OR is extremely wide
- Trail stops aggressively on trend days
- Don't try to pick bottom/top in panic

---

## Common Errors

### 1. Trading Before OR Forms

**The error:**

- 9:35 AM: "Looks like it's going up!"
- Enter long immediately
- Price reverses, stops out

**Why it fails:**

First 15-30 minutes is chaotic price discovery. No directional information yet.

**Correct approach:**

- Wait for full OR formation (minimum 15 min, prefer 30 min)
- Let the market tell you its direction
- Patience beats prediction

### 2. Ignoring Volume Confirmation

**The error:**

- Price breaks OR high by 2 ticks
- Enter immediately
- Volume is 60% of average
- Price drifts back into range

**Why it fails:**

Low-volume breakouts lack conviction. No institutional participation.

**Correct approach:**

- Require RVOL > 1.5 for entry
- If volume absent, skip the trade
- Volume is the fuel for momentum

### 3. Oversizing Positions

**The error:**

- Account: $50,000
- "This setup looks great!"
- Enter 5 ES contracts
- Stop hit: -$3,000 (6% loss)

**Why it fails:**

Even great setups fail 40% of the time. One bad trade shouldn't hurt this much.

**Correct approach:**

- Risk max 0.5-1% per trade
- On $50,000: Max risk $250-500
- That's 1-2 contracts ES, not 5

### 4. Trading Through Lunch

**The error:**

- Morning trade working well
- 11:30 AM: "Let it run"
- 12:30 PM: Gives back all gains
- Exit at breakeven or loss

**Why it fails:**

11:00 AM - 2:00 PM is low volume, choppy, mean-reverting.

**Correct approach:**

- Take profits before 11:00 AM
- Or tighten stops significantly
- Consider closing and re-evaluating at 2:00 PM

### 5. Revenge Trading After Losses

**The error:**

- Trade 1: -$500
- Trade 2: -$400
- "I need to make it back!"
- Trade 3: Double size
- Trade 3: -$1,200

**Why it fails:**

Emotional decisions, oversizing, chasing = recipe for disaster.

**Correct approach:**

- After 2 consecutive losses: 30-minute break
- After daily loss limit: Stop trading
- Accept that some days don't work

### 6. Holding Overnight

**The error:**

- 3:45 PM: Position in profit
- "It's working, let's hold overnight"
- Overnight news: Gap against position
- Next morning: Big loss

**Why it fails:**

Gap risk is unmanageable. Overnight events can reverse any trend.

**Correct approach:**

- Close all positions by 3:45-4:00 PM
- Intraday means INTRADAY
- Start fresh each day

### 7. Trading Low Volatility Days

**The error:**

- VIX at 11
- OR width: 8 points (tiny)
- Force trades anyway
- Whipsaw losses

**Why it fails:**

No volatility = no momentum = no edge. Costs eat any small gains.

**Correct approach:**

- Check VIX and OR width before trading
- If OR < 15 points (ES) or VIX < 13: Consider skip
- Some days, doing nothing is the best trade

---

## Final Wisdom

> "Intraday momentum trading with futures is a high-frequency battle against transaction costs, noise, and your own psychology. The statistical edge is real but small—perhaps 55% win rate with 1.2:1 reward-risk. After accounting for commissions, spreads, and slippage, that edge becomes razor-thin. Success requires impeccable execution, disciplined risk management, and the emotional stability to accept that 40% of your trades will lose and some days will be complete failures. The key is to trade selectively: wait for high-quality setups (OR breakout with volume confirmation), trade during optimal windows (10:00-11:00 AM), size appropriately (0.5-1% risk), and exit by session close. Avoid the classic traps: don't trade before the OR forms, don't hold through lunch, don't revenge trade after losses, and never hold overnight. The most successful intraday traders are not the most aggressive—they're the most selective. They take 1-3 high-quality trades per day, manage risk religiously, and understand that preserving capital on bad days is more important than maximizing profits on good days."

**Key to success:**

- Wait for the setup (OR must form completely)
- Confirm with volume (RVOL > 1.5)
- Size appropriately (0.5-1% risk per trade)
- Trade optimal windows (10:00-11:00 AM)
- Exit by close (no overnight holds)
- Respect daily limits (2% max daily loss)
- Accept losing days (40% of trades will lose)

**Most important:** Intraday momentum is not about capturing every move—it's about selectively participating in high-probability setups with controlled risk. The edge is small, so costs and discipline matter enormously. Trade less, trade better, and live to trade another day. 📊⏰🎯
