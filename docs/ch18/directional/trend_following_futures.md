# Trend Following with Futures

**Trend following with futures** is a systematic trading strategy that captures sustained directional price movements across asset classes using leveraged, liquid futures contracts, relying on price momentum signals, volatility-adjusted position sizing, and diversified portfolio construction to generate returns that are uncorrelated with traditional buy-and-hold strategies.

---

## The Core Insight

**The fundamental idea:**

- Markets exhibit persistent trends due to behavioral biases and information diffusion
- Trends occur across all asset classes (equities, rates, FX, commodities)
- Futures provide efficient, leveraged access to trend capture
- Systematic rules remove emotional decision-making
- Position sizing based on volatility ensures equal risk contribution
- Diversification across uncorrelated markets smooths returns
- Trend following generates "crisis alpha" during market dislocations

**The key equation:**

$$
\text{Signal}_t = f(P_t, P_{t-1}, \ldots, P_{t-k})
$$

Where the signal function typically captures momentum:

$$
\text{TSMOM}_t = \text{sign}\left(\frac{P_t - P_{t-k}}{P_{t-k}}\right) = \text{sign}(r_{t-k,t})
$$

**You're essentially betting: "Past price movements contain information about future price movements, and trends persist long enough to capture profits after transaction costs."**

---

## What Is Trend Following?

**Before implementing trend following, understand the strategy mechanics:**

### 1. Core Concept

**Definition:** A systematic approach to capturing sustained directional price movements by going long assets that have risen and short assets that have fallen, using rule-based signals and risk-managed position sizing.

**When you trend follow with futures:**

- You identify trend direction using price-based signals
- You size positions inversely proportional to volatility
- You enter positions in the direction of the trend
- You hold until the trend reverses (or signal flips)
- You diversify across multiple uncorrelated markets
- You rebalance positions as volatility changes

**Example - E-mini S&P 500 (ES):**

- 50-day moving average: 4,450
- 200-day moving average: 4,300
- Current price: 4,520
- Signal: Long (price > 50-day > 200-day)
- 20-day realized volatility: 15% annualized
- Target volatility per position: 10%
- Position size: 10% / 15% = 0.67x notional

**Trade setup:**

- Entry: Long ES at 4,520
- Position: 0.67 × base position (volatility-adjusted)
- Stop: Below 200-day MA (4,300) or signal reversal
- Exit: When 50-day crosses below 200-day or volatility stop hit

### 2. Time-Series Momentum (TSMOM)

**Definition:** Going long/short a single asset based on its own past returns.

**The signal:**

$$
\text{TSMOM}_{i,t} = \text{sign}(r_{i,t-k,t})
$$

Where $r_{i,t-k,t}$ is the return of asset $i$ over the past $k$ periods.

**Position:**

$$
\text{Position}_{i,t} = \text{TSMOM}_{i,t} \times \frac{\sigma_{\text{target}}}{\sigma_{i,t}}
$$

**Example:**

- Crude oil (CL) 12-month return: +25%
- Signal: +1 (long)
- 30-day realized vol: 35% annualized
- Target vol: 10%
- Position size: +1 × (10%/35%) = +0.29x

**Key insight:** Each asset's trend is evaluated independently based on its own past performance.

### 3. Moving Average Crossovers

**Definition:** Generating signals when shorter-term moving averages cross longer-term moving averages.

**Common configurations:**

| System | Fast MA | Slow MA | Typical Use |
|--------|---------|---------|-------------|
| Short-term | 10-day | 30-day | Active trading |
| Medium-term | 20-day | 50-day | Standard CTA |
| Long-term | 50-day | 200-day | Position trading |
| Dual | 10/50 | 50/200 | Confirmation |

**Signal generation:**

$$
\text{Signal}_t = \begin{cases}
+1 & \text{if } \text{MA}_{\text{fast}} > \text{MA}_{\text{slow}} \\
-1 & \text{if } \text{MA}_{\text{fast}} < \text{MA}_{\text{slow}}
\end{cases}
$$

**Example - Gold futures (GC):**

- 20-day MA: $2,050
- 50-day MA: $2,025
- Current price: $2,065
- Signal: Long (20-day > 50-day)
- Entry trigger: 20-day crossed above 50-day 5 days ago

**Refinement - Signal strength:**

$$
\text{Signal Strength}_t = \frac{\text{MA}_{\text{fast}} - \text{MA}_{\text{slow}}}{\text{ATR}_n}
$$

Stronger crossovers (larger separation) may warrant larger positions.

### 4. Breakout Systems

**Definition:** Entering positions when price breaks above/below recent highs/lows.

**Donchian Channel (Turtle Trading):**

$$
\text{Upper Band}_t = \max(P_{t-1}, P_{t-2}, \ldots, P_{t-n})
$$

$$
\text{Lower Band}_t = \min(P_{t-1}, P_{t-2}, \ldots, P_{t-n})
$$

**Entry rules (Classic Turtle):**

- Long: Price > 20-day high
- Short: Price < 20-day low
- Exit long: Price < 10-day low
- Exit short: Price > 10-day high

**Example - Soybeans (ZS):**

- 20-day high: $14.25
- 20-day low: $13.50
- Current price: $14.35
- Signal: Long (broke above 20-day high)
- Stop: 10-day low at $13.85

**Position sizing (Turtle method):**

$$
\text{Unit Size} = \frac{1\% \text{ of Account}}{\text{ATR} \times \text{Dollar per Point}}
$$

**Example:**

- Account: $1,000,000
- 1% risk: $10,000
- ATR (20-day): $0.35
- Dollar per point: $50
- Unit size: $10,000 / ($0.35 × $50) = 571 contracts ≈ 5 contracts (scaled)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/trend_following_futures.png?raw=true" alt="trend_following_futures" width="700">
</p>
**Figure 1:** Trend following system showing moving average crossover signals, breakout entries, and volatility-adjusted position sizing, with the characteristic pattern of capturing large trends while incurring small whipsaw losses during ranging markets.

---

## Economic Rationale

**Beyond the basic mechanics, understanding WHY trends exist and persist:**

### 1. The Behavioral Foundations

**The deep insight:**

Trend following profits from systematic behavioral biases that cause markets to underreact to new information initially and then overreact as trends develop:

1. **Anchoring bias:** Investors anchor to past prices, slow to update
2. **Herding behavior:** Institutional managers follow each other
3. **Disposition effect:** Sell winners early, hold losers too long
4. **Confirmation bias:** Seek information supporting existing positions
5. **Slow information diffusion:** News travels through markets gradually

**Formal representation:**

$$
P_t = P_{t-1} + \theta \cdot (V_t - P_{t-1}) + \epsilon_t
$$

Where:
- $V_t$ = Fundamental value
- $\theta$ = Speed of price adjustment (typically $\theta < 1$)
- $\epsilon_t$ = Noise

**If $\theta < 1$ (underreaction):**

$$
\mathbb{E}[r_{t+1} | r_t > 0] > 0 \quad \text{(momentum)}
$$

**Why trends persist:**

**Information diffusion model:**

$$
P_t = \sum_{s=0}^{t} \lambda^{t-s} I_s
$$

Where $I_s$ is information arriving at time $s$ and $\lambda < 1$ represents gradual incorporation.

**Result:** Information gets priced in slowly, creating trends.

### 2. The Risk Premium Perspective

**Alternative explanation:**

Trend following may capture compensation for bearing macroeconomic risk during regime transitions.

**The decomposition:**

$$
\text{Trend Return} = \underbrace{\text{Risk Premium}}_{\text{Compensation for crisis exposure}} + \underbrace{\text{Behavioral Alpha}}_{\text{Exploiting biases}}
$$

**During regime shifts:**

- Risk assets decline together (crisis)
- Safe havens rally together (flight to quality)
- Trend followers position accordingly
- Capture large moves during dislocations

**Crisis alpha:**

| Period | S&P 500 | Trend Following |
|--------|---------|-----------------|
| 2008 Crisis | -37% | +18% |
| 2011 Euro Crisis | -13% | +12% |
| 2015 China Selloff | -6% | +5% |
| 2020 COVID Crash | -34% | +15% |
| 2022 Rate Shock | -18% | +25% |

**This negative correlation during crises is valuable for portfolio construction.**

### 3. The Autocorrelation Structure

**Statistical foundation:**

Trend following profits from positive autocorrelation in returns:

$$
\rho_k = \text{Corr}(r_t, r_{t-k}) > 0 \quad \text{for } k = 1, 2, \ldots, K
$$

**Empirical evidence (futures markets, 1985-2024):**

| Lookback | Autocorrelation | t-statistic |
|----------|-----------------|-------------|
| 1-month | 0.08 | 4.2 |
| 3-month | 0.11 | 5.1 |
| 6-month | 0.09 | 4.5 |
| 12-month | 0.06 | 3.8 |

**Interpretation:**

- Past returns predict future returns (modestly)
- Effect peaks around 3-6 months
- Decays at longer horizons (mean reversion kicks in)
- **Optimal trend horizon: 3-12 months**

### 4. The Convexity of Trend Following

**Key insight:**

Trend following exhibits positive convexity (option-like payoff) without explicit option positions.

**The payoff structure:**

$$
\text{Trend Return} \approx \int_{-\infty}^{\infty} |r| \cdot \text{sign}(r) \cdot p(r) \, dr
$$

This integral increases in absolute value with the magnitude of returns.

**Why convexity emerges:**

1. Cut losses quickly (small drawdowns)
2. Let winners run (large gains)
3. Net payoff: Many small losses, few large gains
4. **Similar to being long volatility**

**Comparison to long straddle:**

| Characteristic | Long Straddle | Trend Following |
|----------------|---------------|-----------------|
| Profits from large moves | Yes | Yes |
| Direction-agnostic initially | Yes | Yes |
| Time decay cost | Yes (theta) | Yes (whipsaws) |
| Explicit premium | Yes | No |
| Convexity source | Option gamma | Signal following |

### 5. The Diversification Imperative

**Why diversification is critical:**

Single-market trend following has high variance:

$$
\text{Var}(\text{Single Market}) = \sigma_{\text{trend}}^2 + \sigma_{\text{noise}}^2
$$

Portfolio trend following benefits from diversification:

$$
\text{Var}(\text{Portfolio}) = \frac{1}{N} \sigma_{\text{idiosyncratic}}^2 + \sigma_{\text{common}}^2
$$

**Empirical Sharpe ratios:**

| Number of Markets | Sharpe Ratio |
|-------------------|--------------|
| 1 market | 0.15 |
| 5 markets | 0.35 |
| 20 markets | 0.55 |
| 50+ markets | 0.70 |

**Key insight:** The edge in trend following is small per market but consistent across many markets. Diversification is not optional—it's essential for strategy viability.

---

## Position Sizing and Risk Management

**The most critical aspect of trend following:**

### 1. Volatility Targeting

**Definition:** Sizing positions inversely proportional to volatility to equalize risk contribution.

**The formula:**

$$
N_i = \frac{\text{Risk Budget}_i}{\sigma_i \times \text{Notional per Contract}_i}
$$

**Example - Multi-asset portfolio:**

Target portfolio volatility: 15% annualized
Risk budget per position: 2% of portfolio vol (15% / 7.5 positions)

| Market | Vol (Ann.) | Target Risk | Position Size |
|--------|-----------|-------------|---------------|
| ES (S&P 500) | 18% | 2% | 0.11x |
| TY (10Y Treasury) | 7% | 2% | 0.29x |
| 6E (Euro FX) | 9% | 2% | 0.22x |
| GC (Gold) | 15% | 2% | 0.13x |
| CL (Crude Oil) | 35% | 2% | 0.06x |

**Result:** Each position contributes approximately equal volatility to the portfolio.

### 2. ATR-Based Position Sizing

**Average True Range (ATR) method:**

$$
\text{ATR}_n = \frac{1}{n} \sum_{i=1}^{n} \text{TR}_i
$$

Where True Range:

$$
\text{TR}_t = \max(H_t - L_t, |H_t - C_{t-1}|, |L_t - C_{t-1}|)
$$

**Position size calculation:**

$$
\text{Contracts} = \frac{\text{Risk Amount}}{\text{ATR} \times \text{Dollar per Point}}
$$

**Example - Corn futures (ZC):**

- Account: $500,000
- Risk per trade: 0.5% = $2,500
- 14-day ATR: $0.18 (18 cents)
- Dollar per point: $50 per cent
- Position size: $2,500 / ($0.18 × $50 × 100) = 2.8 ≈ 3 contracts

### 3. The Turtle Position Sizing System

**Original Turtle rules:**

**Unit definition:**

$$
\text{Unit} = \frac{1\% \text{ of Equity}}{\text{N} \times \text{Dollar Volatility}}
$$

Where N = 20-day exponential moving average of True Range.

**Position limits:**

- Maximum 4 units per market
- Maximum 6 units in closely correlated markets
- Maximum 10 units in single direction (long or short)
- Maximum 12 units total

**Pyramid additions:**

- Add 1 unit each 0.5N profit
- Maximum 4 pyramids (4 units total)
- Stop loss: 2N from entry (applied to all units)

**Example:**

- Enter long Crude Oil at $80.00
- N = $1.50
- Add 2nd unit at $80.75 ($80 + 0.5 × $1.50)
- Add 3rd unit at $81.50
- Add 4th unit at $82.25
- Stop for all: $77.00 ($80 - 2 × $1.50)

### 4. Portfolio-Level Risk Constraints

**Correlation-aware risk management:**

$$
\sigma_{\text{portfolio}}^2 = \sum_i w_i^2 \sigma_i^2 + 2\sum_{i<j} w_i w_j \sigma_i \sigma_j \rho_{ij}
$$

**Implementation:**

1. Estimate rolling correlations (60-day window)
2. Cap correlated exposure (e.g., max 30% in energy sector)
3. Reduce positions when correlations spike
4. Maintain directional diversification (long/short balance)

**Correlation groups:**

| Group | Markets | Max Combined Weight |
|-------|---------|-------------------|
| Equity Indices | ES, NQ, RTY, YM | 30% |
| Government Bonds | TY, US, FV, TU | 25% |
| Currencies (G10) | 6E, 6J, 6B, 6A | 25% |
| Energy | CL, NG, RB, HO | 20% |
| Precious Metals | GC, SI | 15% |
| Agriculture | ZC, ZS, ZW, CT | 20% |

### 5. Drawdown Management

**Maximum drawdown limits:**

$$
\text{DD}_t = \frac{\text{Peak}_t - \text{Current}_t}{\text{Peak}_t}
$$

**Response protocol:**

| Drawdown Level | Action |
|----------------|--------|
| 0-10% | Normal operations |
| 10-15% | Reduce target vol by 25% |
| 15-20% | Reduce target vol by 50% |
| 20-25% | Reduce target vol by 75% |
| >25% | Halt new positions, close on signals only |

**Rationale:**

- Preserve capital during adverse periods
- Reduce volatility of volatility
- Maintain ability to recover
- **Survival > performance**

---

## Signal Construction and Filtering

**Improving signal quality:**

### 1. Multi-Timeframe Confirmation

**Combining signals across horizons:**

$$
\text{Composite Signal} = \sum_{k} w_k \cdot \text{Signal}_k
$$

Where $k$ indexes different lookback periods.

**Example - Triple moving average:**

| Component | Weight | Signal |
|-----------|--------|--------|
| 10/30 crossover | 0.25 | +1 (bullish) |
| 20/50 crossover | 0.50 | +1 (bullish) |
| 50/200 crossover | 0.25 | +1 (bullish) |
| **Composite** | **1.00** | **+1.00** |

**Partial signals:**

- Composite = +1.0: Full long position
- Composite = +0.5: Half long position
- Composite = 0.0: Flat (no position)
- Composite = -0.5: Half short position
- Composite = -1.0: Full short position

### 2. Volatility Regime Filters

**Adjusting for volatility regimes:**

$$
\text{Position} = \text{Signal} \times f(\sigma_t / \bar{\sigma})
$$

**Low volatility regime ($\sigma_t < 0.8 \bar{\sigma}$):**

- Trends tend to be clearer
- Increase position size (up to cap)
- Tighter stops acceptable

**High volatility regime ($\sigma_t > 1.5 \bar{\sigma}$):**

- More whipsaws likely
- Decrease position size
- Wider stops necessary
- Consider signal confirmation requirements

**Example filter:**

$$
\text{Vol Adjustment} = \min\left(1.5, \max\left(0.5, \frac{\bar{\sigma}}{\sigma_t}\right)\right)
$$

### 3. Trend Strength Filters

**ADX (Average Directional Index):**

$$
\text{ADX} = \text{EMA}_{14}(|\text{+DI} - \text{-DI}| / (\text{+DI} + \text{-DI}))
$$

**Trading rules:**

- ADX > 25: Strong trend, take positions
- ADX 20-25: Moderate trend, reduce size
- ADX < 20: No trend, avoid positions

**Example:**

- Gold: ADX = 32 (strong trend) → Full position
- Corn: ADX = 18 (no trend) → No position
- Crude: ADX = 23 (moderate) → Half position

### 4. Momentum Quality Filters

**Smooth vs. choppy momentum:**

$$
\text{Path Efficiency} = \frac{|P_t - P_{t-n}|}{\sum_{i=1}^{n}|P_{t-i+1} - P_{t-i}|}
$$

Where:
- Numerator: Direct distance traveled
- Denominator: Total path length

**Interpretation:**

- Efficiency > 0.5: Clean trend (directional)
- Efficiency < 0.3: Choppy (whipsaw-prone)

**Application:**

- High efficiency: Trade normally
- Low efficiency: Require stronger signals or skip

### 5. Cross-Market Confirmation

**Using correlated markets for confirmation:**

**Example - Equity index trend:**

Primary signal: ES (S&P 500) 50/200 bullish

Confirmation checks:
- NQ (Nasdaq) also bullish? ✓
- RTY (Russell 2000) also bullish? ✓
- VIX below 200-day MA? ✓
- Credit spreads stable? ✓

**Confirmation score:**

$$
\text{Confirmation} = \frac{\text{Confirming Signals}}{\text{Total Signals}}
$$

**Trading rule:**

- Confirmation > 0.75: Full position
- Confirmation 0.50-0.75: Half position
- Confirmation < 0.50: No position

---

## Implementation Details

**Practical considerations for live trading:**

### 1. Contract Selection and Roll Management

**Choosing contracts:**

| Criterion | Preference |
|-----------|-----------|
| Liquidity | Front month or first liquid back month |
| Open interest | Minimum 10,000 contracts |
| Bid-ask spread | < 2 ticks |
| Volume | > 50,000 contracts/day |

**Roll timing:**

**Standard approach:**

- Roll 5-7 days before expiration
- Avoid first notice day (commodities)
- Execute during high-liquidity windows

**Optimal roll timing:**

$$
\text{Roll Alpha} = \text{Expected Return} - \text{Roll Cost}
$$

Where roll cost includes:
- Bid-ask spread (both contracts)
- Market impact
- Spread between contracts

**Calendar spread approach:**

Instead of legging out and in separately:
1. Execute calendar spread (sell front, buy back)
2. Tighter markets, lower impact
3. Better execution on exchanges

### 2. Entry and Exit Execution

**Entry execution:**

**Aggressive (momentum strong):**
- Market orders at signal
- Accept slippage for certainty
- Used when signal quality high

**Passive (signal borderline):**
- Limit orders at/near signal price
- May miss entry if market moves away
- Used when cost-sensitive

**Time-weighted (large positions):**
- Split order over 30-60 minutes
- Reduce market impact
- Used for institutional size

**Exit execution:**

**Stop-loss exits:**
- Pre-placed stop orders
- May use stop-limit to avoid gaps
- Trail stops as position profits

**Signal reversal exits:**
- Execute at close or next open
- Allow for signal confirmation
- Avoid whipsaw from intraday noise

### 3. Rebalancing Frequency

**Trade-off:**

$$
\text{Net Return} = \text{Gross Return} - \text{Transaction Costs} - \text{Slippage}
$$

**Rebalancing options:**

| Frequency | Advantages | Disadvantages |
|-----------|------------|---------------|
| Daily | Tight risk control, fast reaction | High costs, overtrading |
| Weekly | Balanced approach | Standard for most CTAs |
| Monthly | Low costs | Slow reaction to vol changes |

**Optimal rebalancing:**

Use threshold-based rebalancing:
- Rebalance if position deviates > 20% from target
- Rebalance if volatility changes > 25%
- Always rebalance on signal change

### 4. Margin Management

**Margin utilization:**

$$
\text{Margin Utilization} = \frac{\text{Initial Margin Required}}{\text{Account Equity}}
$$

**Target utilization:**

| Risk Tolerance | Utilization Target |
|---------------|-------------------|
| Conservative | 15-25% |
| Moderate | 25-40% |
| Aggressive | 40-60% |

**Why not higher?**

- Margin calls during drawdowns
- Forced liquidation at worst times
- No buffer for volatility spikes

**Example:**

- Account: $1,000,000
- Target utilization: 30%
- Available for margin: $300,000
- ES margin: $12,000 per contract
- Max ES contracts: 25 (if 100% in ES)

**Practical allocation:**

Diversify across 15-25 markets with combined margin ~$300,000.

### 5. Slippage and Transaction Cost Modeling

**Total trading cost:**

$$
\text{Cost} = \text{Commission} + \frac{\text{Spread}}{2} + \text{Market Impact}
$$

**Market impact model (square root):**

$$
\text{Impact} = \sigma \sqrt{\frac{Q}{V}}
$$

Where:
- $\sigma$ = Daily volatility
- $Q$ = Order size (contracts)
- $V$ = Average daily volume

**Example - ES futures:**

- Commission: $2.50 per side
- Half spread: $12.50 (1 tick at $12.50/tick)
- Daily volume: 1,500,000 contracts
- Order: 10 contracts
- Daily vol: $50

Impact = $50 × √(10/1,500,000) = $0.13 per contract

Total cost per side: $2.50 + $12.50 + $0.13 = $15.13 per contract

**Annual cost estimation:**

- 10 contracts × 24 round trips/year × $30.26 = $7,262/year
- On $500,000 notional: 1.5% annual drag

---

## Performance Analysis

**Evaluating trend following systems:**

### 1. Historical Performance (1985-2024)

**Representative CTA returns:**

| Period | Trend Following | S&P 500 | 60/40 Portfolio |
|--------|-----------------|---------|-----------------|
| 1985-1990 | +18.2% ann. | +15.3% | +12.8% |
| 1990-2000 | +12.1% ann. | +18.2% | +14.2% |
| 2000-2010 | +9.8% ann. | -0.9% | +2.5% |
| 2010-2020 | +4.2% ann. | +13.6% | +9.8% |
| 2020-2024 | +11.5% ann. | +12.1% | +7.2% |

**Key observations:**

- Best in volatile, trending markets (2008, 2022)
- Struggles in low-vol, range-bound markets (2013-2017)
- Uncorrelated to equities (correlation ~0.0 to -0.2)
- Crisis alpha: +15-25% in major equity drawdowns

### 2. Risk-Adjusted Metrics

**Typical metrics for diversified trend following:**

| Metric | Target | Typical Range |
|--------|--------|---------------|
| Sharpe Ratio | 0.5-0.8 | 0.3-1.0 |
| Sortino Ratio | 0.7-1.2 | 0.5-1.5 |
| Max Drawdown | 15-25% | 10-40% |
| Calmar Ratio | 0.4-0.8 | 0.2-1.0 |
| Win Rate | 35-45% | 30-50% |
| Profit Factor | 1.2-1.8 | 1.0-2.5 |

**Why low win rate is acceptable:**

$$
\text{Expectancy} = (\text{Win Rate} \times \text{Avg Win}) - ((1 - \text{Win Rate}) \times \text{Avg Loss})
$$

**Example:**

- Win rate: 40%
- Average win: $5,000
- Average loss: $2,000

Expectancy = (0.40 × $5,000) - (0.60 × $2,000) = $2,000 - $1,200 = $800 per trade

**Positive expectancy despite losing more often than winning!**

### 3. Regime-Dependent Performance

**Performance varies by market regime:**

| Regime | Characteristics | Trend Performance |
|--------|-----------------|-------------------|
| Risk-on trend | Rising equities, falling vol | Moderate gains |
| Risk-off trend | Falling equities, rising vol | Strong gains |
| Range-bound | Low vol, no direction | Losses (whipsaws) |
| Volatility spike | Sudden moves, reversals | Mixed |

**Identifying regimes:**

**VIX-based classification:**

- VIX < 15: Low vol regime (range-bound likely)
- VIX 15-25: Normal (trending possible)
- VIX > 25: High vol (trending likely)

**Cross-asset trend agreement:**

$$
\text{Trend Agreement} = \frac{\sum_i |\text{Signal}_i|}{N}
$$

- Agreement > 0.7: Strong trends (good environment)
- Agreement < 0.3: No trends (difficult environment)

### 4. Drawdown Analysis

**Typical drawdown characteristics:**

| Drawdown Type | Duration | Magnitude |
|---------------|----------|-----------|
| Whipsaw | 1-4 weeks | 3-8% |
| Trend reversal | 1-3 months | 8-15% |
| Regime shift | 3-12 months | 15-25% |
| Prolonged range | 12-24 months | 20-30% |

**Recovery expectations:**

$$
\text{Recovery Time} \approx \frac{\text{Drawdown}^2}{\text{Expected Return} \times \text{Volatility}}
$$

**Example:**

- 20% drawdown
- Expected return: 8% annual
- Volatility: 15% annual

Recovery ≈ (0.20)² / (0.08 × 0.15) ≈ 3.3 years

**Key insight:** Large drawdowns require long recovery periods. Capital preservation matters!

---

## Case Studies

**Real-world examples of trend following:**

### 1. The 2008 Financial Crisis

**Background:**

- S&P 500 fell 57% peak to trough (Oct 2007 - Mar 2009)
- Lehman Brothers collapse September 2008
- Global credit crisis and equity meltdown

**Trend following performance:**

**Signal evolution (ES futures):**

| Date | 50-day MA | 200-day MA | Signal | Position |
|------|-----------|------------|--------|----------|
| Jan 2008 | 1,420 | 1,485 | Short | -0.5x |
| Apr 2008 | 1,355 | 1,420 | Short | -0.7x |
| Jul 2008 | 1,280 | 1,380 | Short | -0.8x |
| Oct 2008 | 1,050 | 1,300 | Short | -1.0x |
| Jan 2009 | 900 | 1,150 | Short | -0.9x |

**Results:**

- Diversified trend followers: +15% to +30% in 2008
- Maintained short equity, long bond positions
- Crisis alpha: Negative correlation with equities precisely when needed

**Key lesson:** Trend following delivered when traditional portfolios collapsed.

### 2. The 2010-2014 Whipsaw Period

**Background:**

- Post-crisis recovery
- Multiple "risk-on, risk-off" episodes
- QE programs creating uncertainty

**Challenges:**

- Equity trend unclear (range-bound with volatility spikes)
- Bond trend strong but reversals on Fed announcements
- Commodities super-cycle ending
- FX trends interrupted by central bank interventions

**Performance:**

| Year | Trend Following | S&P 500 |
|------|-----------------|---------|
| 2010 | +8.2% | +15.1% |
| 2011 | -3.5% | +2.1% |
| 2012 | -1.8% | +16.0% |
| 2013 | -0.5% | +32.4% |
| 2014 | +12.3% | +13.7% |

**Key lessons:**

- Extended periods of underperformance normal
- 2011-2013: Three consecutive weak years
- Discipline to maintain strategy through adversity critical
- 2014 rally in dollar and bonds rescued the strategy

### 3. The 2022 Rate Shock

**Background:**

- Fed aggressive rate hikes (0% to 5%+ in 18 months)
- 60/40 portfolios worst year in decades
- Inflation surprise, bond selloff

**Trend following opportunity:**

**Bond positions:**

- Short Treasury futures from early 2022
- TY (10-year) fell from 130 to 108
- Massive gains on short duration

**Equity positions:**

- Short equity indices mid-2022
- ES fell from 4,800 to 3,600
- Gains on short equity

**Commodity positions:**

- Long energy (crude oil, natural gas surge)
- Long agricultural commodities (wheat, corn)

**Results:**

- Diversified trend followers: +20% to +40% in 2022
- When 60/40 lost 17%, trend following gained
- Crisis alpha demonstrated again

**Key insight:** Trend following thrives when correlations break (stocks AND bonds down together).

---

## Risk Management

### 1. Position Sizing Discipline

**The cardinal rule:**

$$
\text{Position Size} \leq \frac{\text{Max Risk per Trade}}{\text{Stop Distance}}
$$

**Conservative approach:**

- Maximum 1% account risk per position
- Total portfolio risk ≤ 15% target volatility
- No single sector > 25% of risk budget

**Implementation:**

1. Calculate dollar stop distance
2. Determine max risk amount (1% of equity)
3. Position size = max risk / stop distance
4. Apply volatility adjustment
5. Check sector limits

### 2. Correlation Monitoring

**Dynamic correlation tracking:**

$$
\rho_{ij,t} = \text{Corr}(r_{i,t-60:t}, r_{j,t-60:t})
$$

**Warning signals:**

- Correlation spike > 0.6 between positions
- Reduce combined position by 30%
- Particularly important during crises

**Example:**

Normal: Crude oil (CL) vs. Canadian dollar (6C) ρ = 0.3
Crisis: ρ spikes to 0.8
Action: Reduce combined exposure by 40%

### 3. Drawdown Response Protocol

**Systematic de-risking:**

| Drawdown | Target Vol Adjustment | Position Scaling |
|----------|----------------------|------------------|
| 0-10% | 100% | Normal |
| 10-15% | 75% | 0.75x |
| 15-20% | 50% | 0.50x |
| 20-25% | 25% | 0.25x |
| >25% | Halt | Close only |

**Rationale:**

- Preserve capital
- Reduce volatility of returns
- Maintain ability to recover
- Avoid capitulation at the bottom

### 4. Stop-Loss Framework

**Multiple stop types:**

**ATR-based stop:**

$$
\text{Stop} = \text{Entry} - 2 \times \text{ATR}
$$

**Volatility-adjusted stop:**

$$
\text{Stop} = \text{Entry} - k \times \sigma
$$

Where $k$ typically 1.5-2.5 standard deviations.

**Signal-based stop:**

- Exit when signal reverses
- May be wider than technical stop
- Preferred for longer-term trends

**Time stop:**

- Exit if no progress after N days
- Releases capital for better opportunities
- Typical: 20-40 days without new highs

### 5. Liquidity Risk Management

**Pre-trade checks:**

1. Current open interest > 10× position size
2. Daily volume > 20× position size
3. Bid-ask spread < 0.1% of price
4. Market depth adequate for position

**Crisis liquidity:**

- Reduce positions as liquidity deteriorates
- Widen stops to avoid forced exits
- Accept higher costs for exit certainty

---

## Common Errors

### 1. Overfitting Historical Signals

**The error:**

- Optimize MA parameters to historical data
- Find 17/43 crossover beats 20/50 in backtest
- Live trading performance disappoints

**Why it fails:**

$$
\text{Backtest Sharpe} = \text{True Sharpe} + \text{Overfitting Bonus}
$$

The overfitting bonus disappears in live trading.

**Correct approach:**

- Use standard parameters (50/200, not 47/183)
- Out-of-sample validation
- Accept that simpler is better
- Multiple lookback horizons for robustness

### 2. Ignoring Transaction Costs

**The error:**

- Backtest shows 15% annual return
- Ignore $0.03 slippage per trade
- 200 trades/year × $0.03 × 500 contracts = $3,000
- Real return: 15% - 3% = 12%

**Correct approach:**

- Model all costs conservatively
- Include spread, commission, slippage
- Target systems with < 100 annual trades per market
- Use limit orders where possible

### 3. Insufficient Diversification

**The error:**

- Trade only S&P 500 and Nasdaq
- 0.85 correlation between markets
- Portfolio is effectively one bet

**Why it fails:**

Both markets trend together → Double loss on reversal
No diversification benefit captured

**Correct approach:**

- Minimum 15-20 markets
- Include uncorrelated assets (bonds, commodities, FX)
- Cap sector exposure
- Monitor rolling correlations

### 4. Abandoning Strategy During Drawdowns

**The error:**

- Strategy draws down 15%
- "This doesn't work anymore"
- Abandon at the bottom
- Miss the recovery

**Why it fails:**

$$
P(\text{Recovery} | \text{Strategy Valid}) >> P(\text{Strategy Failed})
$$

Most drawdowns are normal, not strategy failure.

**Correct approach:**

- Pre-commit to drawdown limits
- Follow systematic de-risking protocol
- Distinguish bad luck from bad strategy
- Maintain discipline through adversity

### 5. Over-Leverage in Low Volatility

**The error:**

- Volatility drops to 8% (VIX = 10)
- Target vol = 15%
- Lever up to 1.9x
- Flash crash hits → massive loss

**Why it fails:**

Low volatility often precedes volatility explosions.
Leverage at the top amplifies the coming decline.

**Correct approach:**

- Cap maximum leverage (3x)
- Consider forward-looking vol (VIX) not just realized
- Maintain margin buffer
- Accept lower returns in low-vol periods

---

## Final Wisdom

> "Trend following is the quintessential systematic strategy—simple in concept, difficult in execution. The math is straightforward: buy what's going up, sell what's going down, size positions by volatility. But the psychology is brutal: accept losing trades 60% of the time, endure multi-year drawdowns, maintain discipline when the strategy looks broken. The edge exists because trends exist, driven by behavioral biases and information diffusion that cause markets to underreact initially and overreact subsequently. This edge is small per market (Sharpe ~0.15) but compounds beautifully across 50+ diverse markets (Sharpe ~0.7). The key is diversification: not just across markets, but across timeframes, signal types, and even strategies. No single trade matters; no single market matters; no single year matters. What matters is the process: systematic signal generation, volatility-based position sizing, ruthless risk management, and unwavering discipline through the inevitable drawdowns. Those who master this process capture the most valuable free lunch in finance: crisis alpha that pays precisely when traditional portfolios collapse."

**Key to success:**

- Systematic signals remove emotion (rules over discretion)
- Volatility targeting equalizes risk (no single position dominates)
- Diversification creates robustness (50+ markets, multiple timeframes)
- Position limits prevent catastrophe (caps and floors)
- Drawdown protocols preserve capital (systematic de-risking)
- Transaction cost awareness maintains edge (quality over quantity)
- Discipline through adversity is non-negotiable (the strategy works, stay the course)

**Most important:** Trend following is a long-term, portfolio-level strategy, not a get-rich-quick scheme. Expected Sharpe ratio of 0.5-0.7 means periods of underperformance are mathematically certain. The value lies in the negative correlation with traditional assets during crises—exactly when you need protection most. Success requires accepting modest returns in exchange for crisis alpha and genuine portfolio diversification. 📈📉🎯
