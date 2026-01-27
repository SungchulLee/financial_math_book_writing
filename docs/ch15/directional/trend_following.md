# Trend Following with Options

Trend following is a systematic strategy that capitalizes on established price momentum by entering positions aligned with the prevailing market direction. When implemented with options, this approach combines directional exposure with defined risk through strategic strike selection and position sizing.

This chapter provides a rigorous treatment of trend-following strategies, connecting behavioral finance theory with practical options implementation. We develop the mathematical framework for momentum detection, integrate Greeks management throughout the position lifecycle, and present backtesting methodology with Python implementations.

!!! abstract "Chapter Overview"
    **Prerequisites:** Black-Scholes pricing, basic Greeks understanding, technical analysis fundamentals
    
    **Learning Objectives:**
    
    - Understand the economic rationale for momentum persistence
    - Apply Greeks management to trend-following positions
    - Implement systematic entry/exit rules with proper risk controls
    - Evaluate strategy performance through backtesting

---

## 1. What is Trend Following?

Trend following is a reactive, not predictive, trading methodology. Rather than forecasting where prices will go, trend followers identify established directional movements and position themselves to profit from their continuation.

### 1.1 Core Philosophy

The fundamental principle is simple: **don't predict, react**. Let the market reveal its direction through price action, then align with it. This stands in contrast to mean-reversion strategies that bet against current momentum.

The philosophy rests on several key concepts. Trend identification uses technical analysis including moving averages, price patterns, and the sequence of higher highs with higher lows (for uptrends) or lower highs with lower lows (for downtrends). Confirmation is required before entry—waiting for clear signals rather than anticipating them. Risk control demands knowing exit conditions before entering any position. Emotional discipline means following the system mechanically regardless of gut feelings. Accepting losses is essential because trend following produces many small losses punctuated by fewer large winners. Finally, pyramiding means adding to winning positions, never to losers.

### 1.2 Why Use Options for Trend Following?

Traditional trend following employs futures or stocks, but options offer distinct advantages for this strategy.

**Advantages of Options:**

Options provide defined risk where maximum loss equals the premium paid, unlike futures with theoretically unlimited loss potential. They offer leverage by controlling large notional positions with relatively small capital outlay. Options enable time efficiency by capturing the profitable middle portion of trends without needing to ride entire moves. They provide flexibility to adjust strikes as trends evolve. Most importantly, options create asymmetric payoffs with limited loss but substantial profit potential.

**Disadvantages of Options:**

Time decay (theta) works against long option positions continuously. Timing becomes critical because entering too early or too late leads to failure. Premium cost means the underlying must move further to reach breakeven. Some options suffer from illiquidity with wide bid-ask spreads. Assignment risk exists when holding in-the-money options through expiration.

### 1.3 Trend Following vs. Reversal Trading

Understanding what trend following is requires understanding what it is not.

**Trend Following (Our Approach):**

Entry occurs after trend confirmation, riding existing momentum until the trend breaks. This produces many small losses but captures occasional large wins. Typical win rates range from 35-45%, but profit factors (gross profit divided by gross loss) of 1.5-2.5x make the strategy profitable overall.

**Reversal Trading (Not Our Approach):**

Reversal traders attempt to catch tops and bottoms, betting against momentum. While win rates may be higher (55-65%), the wins are typically small and occasional large losses can devastate returns. Fighting established trends is inherently high-risk.

!!! quote "Trading Wisdom"
    "The trend is your friend until the end."

---

## 2. Economic Rationale

### 2.1 Why Trends Persist: The Momentum Anomaly

The existence and persistence of price trends represents one of the most robust anomalies in financial markets. The seminal work of Jegadeesh and Titman (1993) documented that stocks with high returns over the past 3-12 months tend to outperform over the subsequent 3-12 months.

**Formal Definition of Momentum:**

Let $r_{t-j,t}$ denote the cumulative return from time $t-j$ to time $t$. The momentum factor is defined as:

$$r_{t,t+k}^{\text{mom}} = \alpha + \beta \cdot r_{t-j,t} + \epsilon_{t+k}$$

where $\beta > 0$ indicates positive return autocorrelation—past winners tend to continue winning.

!!! info "Empirical Evidence"
    For U.S. equities, momentum strategies using 12-month formation periods and 1-month holding periods have historically generated annualized excess returns of approximately 6-8% with Sharpe ratios around 0.5-0.7.
    
    **Source:** Asness, Moskowitz & Pedersen (2013), "Value and Momentum Everywhere," *Journal of Finance*.
    
    **Caveat:** Past performance does not guarantee future results. Momentum strategies experienced significant crashes in 2009 and other regime-change periods.

**Behavioral Explanations:**

Multiple behavioral biases contribute to trend persistence. Herding behavior causes investors to follow the crowd, creating self-reinforcing price movements. Anchoring leads to slow belief updating, causing underreaction to new information. Confirmation bias makes investors seek information supporting existing views. The disposition effect causes premature selling of winners and reluctant selling of losers. Institutional constraints mean large funds require extended periods to build or unwind positions, creating sustained order flow.

**The Return Autocorrelation Model:**

A simple AR(1) model for returns captures momentum:

$$r_t = \mu + \phi \cdot r_{t-1} + \epsilon_t, \quad \epsilon_t \sim N(0, \sigma^2)$$

where $\phi > 0$ indicates positive autocorrelation. Empirical estimates for daily stock returns typically find $\phi \in [0.02, 0.10]$—small but statistically significant and economically meaningful over time.

### 2.2 The Momentum Risk Premium

Trend following earns returns as compensation for bearing specific risks.

**Risks Borne by Trend Followers:**

Trend reversal risk occurs when trends suddenly end or reverse. Whipsaw risk involves false breakouts that trigger entry followed by immediate reversal. Theta decay risk means paying daily time premium for exposure. Gap risk involves overnight moves against the position when markets are closed. Crash risk is particularly relevant since momentum strategies historically suffer during market regime changes (e.g., 2009 momentum crash).

**Why the Market Compensates Trend Followers:**

Most investors exhibit contrarian tendencies (buy low, sell high mentality), creating demand for liquidity during momentum surges. Trend followers provide this liquidity and help markets incorporate information into prices. The market compensates those willing to bear the psychological burden of riding volatility and accepting frequent small losses.

### 2.3 Statistical Tests for Trend Existence

Before trading trends, we should test whether they exist in our target market. Several statistical approaches are relevant.

**Variance Ratio Test:**

The variance ratio tests whether returns follow a random walk:

$$VR(q) = \frac{\text{Var}(r_t + r_{t+1} + \cdots + r_{t+q-1})}{q \cdot \text{Var}(r_t)}$$

Under random walk, $VR(q) = 1$. Values greater than 1 suggest positive autocorrelation (trending), while values less than 1 suggest mean reversion.

**Hurst Exponent:**

The Hurst exponent $H$ characterizes long-term memory in time series:

$$E[R/S] \propto n^H$$

where $R/S$ is the rescaled range. $H = 0.5$ indicates random walk, $H > 0.5$ indicates trending (persistent) behavior, and $H < 0.5$ indicates mean-reverting (anti-persistent) behavior.

For major equity indices, empirical Hurst exponents typically range from 0.52-0.58, suggesting mild but exploitable trending behavior.

---

## 3. Options Payoff Structure for Trend Following

### 3.1 Long Call for Uptrends

![Long call payoff](https://github.com/SungchulLee/img/blob/main/long_call_payoff.png?raw=true){ width="400" }

*Figure 1: Long call payoff diagram showing limited downside risk (premium paid) and unlimited upside potential.*

For a call option with strike $K$ and premium $C$, the payoff at expiration is:

$$\text{Profit} = \max(S_T - K, 0) - C$$

**Breakeven:** $S_T = K + C$

**Maximum Loss:** $C$ (premium paid)

**Maximum Profit:** Unlimited (as $S_T \to \infty$)

**Illustrative Example: Uptrend Scenario**

Stock at \$150, confirmed uptrend. Buy \$155 call for \$5, 60 days to expiration.

| Stock at Expiry | Option Value | Profit/Loss | Return |
|-----------------|--------------|-------------|--------|
| \$145 | \$0 | -\$5 | -100% |
| \$155 | \$0 | -\$5 | -100% |
| \$160 | \$5 | \$0 | 0% |
| \$170 | \$15 | +\$10 | +200% |
| \$180 | \$25 | +\$20 | +400% |

### 3.2 Long Put for Downtrends

![Long put payoff](https://github.com/SungchulLee/img/blob/main/long_put_payoff.png?raw=true){ width="400" }

*Figure 2: Long put payoff diagram showing limited downside risk (premium paid) and substantial profit potential as underlying declines.*

For a put option with strike $K$ and premium $P$, the payoff at expiration is:

$$\text{Profit} = \max(K - S_T, 0) - P$$

**Breakeven:** $S_T = K - P$

**Maximum Loss:** $P$ (premium paid)

**Maximum Profit:** $K - P$ (if $S_T \to 0$)

### 3.3 Trend Following vs. Stock: Capital Efficiency

Consider a comparison between buying stock and buying calls for trend exposure.

**Scenario A: Buy Stock**

Purchase 100 shares at \$150 for total cost of \$15,000. If stock rises to \$165, profit is \$1,500 (10% return). If stock falls to \$140, loss is \$1,000 (-6.7% return).

**Scenario B: Buy Calls**

Purchase 3 contracts of \$155 calls at \$5 each for total cost of \$1,500. If stock rises to \$165, calls worth \$10 each yield profit of \$1,500 (100% return). If stock falls to \$140, calls expire worthless for loss of \$1,500 (-100% return).

**Key Observations:**

Both approaches produced identical dollar profit on the upside (\$1,500), but options required only 10% of the capital. Options provided 10:1 effective leverage. The downside dollar loss was similar (\$1,000 vs \$1,500), but as percentage of capital deployed, options performed worse. Critical distinction: stock can be held indefinitely while options have finite life.

---

## 4. Greeks Management in Trend Following

Effective trend following with options requires understanding and managing the Greeks throughout the position lifecycle.

### 4.0 Greeks Convention and Units

!!! warning "Unit Conventions"
    To avoid confusion, this chapter uses consistent conventions for all Greeks:

| Greek | Symbol | Definition | Unit Convention | Sign Convention |
|-------|--------|------------|-----------------|-----------------|
| Delta | $\Delta$ | $\partial V / \partial S$ | Per \$1 move in underlying | + for calls, − for puts |
| Gamma | $\Gamma$ | $\partial \Delta / \partial S$ | Per \$1 move in underlying | Always + for long options |
| Theta | $\Theta$ | $\partial V / \partial t$ | **Per calendar day** (÷365) | **Negative** for long options (cost) |
| Vega | $\mathcal{V}$ | $\partial V / \partial \sigma$ | **Per 1 percentage point** (1 vol point) IV change | Always + for long options |
| Rho | $\rho$ | $\partial V / \partial r$ | Per 1 percentage point rate change | + for calls, − for puts |

**Example:** If Vega = 0.15, a 1 percentage point increase in IV (e.g., 30% → 31%) increases option value by \$0.15 per share (\$15 per contract).

**Example:** If Theta = −0.05, the option loses \$0.05 per share (\$5 per contract) each calendar day due to time decay.

### 4.1 Delta: Directional Exposure

$$\Delta = \frac{\partial V}{\partial S}$$

Delta measures the option's sensitivity to underlying price changes and represents effective share exposure.

**Delta by Moneyness:**

| Moneyness | Delta (Calls) | Delta (Puts) | Use Case |
|-----------|---------------|--------------|----------|
| Deep ITM | 0.80-0.95 | -0.80 to -0.95 | Stock substitute, strong trend |
| ITM | 0.60-0.80 | -0.60 to -0.80 | High conviction, confirmed trend |
| ATM | 0.45-0.55 | -0.45 to -0.55 | Balanced risk/reward |
| OTM | 0.20-0.45 | -0.20 to -0.45 | Speculative, leveraged bet |
| Deep OTM | 0.05-0.20 | -0.05 to -0.20 | Lottery ticket (avoid) |

**Strategic Implications:**

For strong confirmed trends (ADX > 40), use ITM options with delta 0.70-0.85 to maximize trend capture. For moderate trends (ADX 25-40), use ATM options with delta around 0.50 for balanced exposure. For early-stage or speculative trends, slightly OTM options (delta 0.35-0.45) provide leverage with controlled risk.

**Example: Delta Impact**

Stock moves from \$150 to \$155 (+\$5):

- ITM call (Δ = 0.80): Gains approximately \$4.00
- ATM call (Δ = 0.50): Gains approximately \$2.50
- OTM call (Δ = 0.30): Gains approximately \$1.50

Higher delta captures more of the move but costs more premium.

### 4.2 Gamma: Delta Acceleration

$$\Gamma = \frac{\partial^2 V}{\partial S^2} = \frac{\partial \Delta}{\partial S}$$

Gamma measures how delta changes as the underlying moves. This is crucial for trend following because gamma determines how your exposure evolves as trends develop.

**Gamma Profile:**

ATM options have highest gamma—their delta changes most rapidly with underlying movement. ITM and OTM options have lower gamma because their deltas are already near their extremes or very small.

**Why Gamma Helps in Trends:**

When you hold an ATM call and the underlying trends upward:

1. Initial delta: 0.50
2. Stock moves up \$10: Delta increases to approximately 0.60
3. Stock moves up \$20: Delta increases to approximately 0.70

Your position automatically gains more exposure as the trend strengthens. This is favorable compounding: you're effectively adding to a winner without additional capital.

**Gamma Risk on Reversals:**

The same mechanism works against you on reversals. If you're holding a call that has moved ITM (delta 0.70) and the trend reverses, your delta decreases, reducing exposure as losses mount. This actually provides some natural protection, but the protection is incomplete—hence the need for explicit stop losses.

### 4.3 Theta: Time Decay

$$\Theta = \frac{\partial V}{\partial t}$$

Theta represents the daily cost of holding the option position. For trend followers holding long options, **theta is the enemy**.

!!! danger "Critical Rule: 45-60 DTE Minimum"
    Buy options with at least 45-60 days to expiration for moderate trends. Exit or roll positions before entering the last 2 weeks when theta decay accelerates dramatically.

**Theta Decay Curve:**

Theta decay is non-linear, accelerating as expiration approaches:

| Days to Expiration | Daily Theta (ATM, typical) | Cumulative 10-Day Decay |
|--------------------|---------------------------|-------------------------|
| 60-50 DTE | −\$0.05 to −\$0.08 | \$0.50-\$0.80 |
| 50-40 DTE | −\$0.08 to −\$0.12 | \$0.80-\$1.20 |
| 40-30 DTE | −\$0.12 to −\$0.18 | \$1.20-\$1.80 |
| 30-20 DTE | −\$0.18 to −\$0.25 | \$1.80-\$2.50 |
| 20-10 DTE | −\$0.25 to −\$0.40 | \$2.50-\$4.00 |
| 10-0 DTE | −\$0.40 to −\$1.00+ | Rapid decay |

**Minimum Required Move Equation:**

To breakeven, the underlying must move enough to overcome both the premium paid and ongoing theta decay:

$$\text{Required Move} = \frac{C + |\Theta| \cdot t}{\Delta}$$

where $C$ is premium paid, $|\Theta|$ is absolute daily theta (as positive cost), $t$ is holding period in days, and $\Delta$ is delta.

**Example:**

ATM call with premium \$5, delta 0.50, theta −\$0.10/day, holding 20 days:

$$\text{Required Move} = \frac{5 + 0.10 \times 20}{0.50} = \frac{7}{0.50} = \$14$$

The underlying must move \$14 just to break even after 20 days. Trends must be strong enough to overcome this drag.

### 4.4 Vega: Volatility Sensitivity

$$\mathcal{V} = \frac{\partial V}{\partial \sigma}$$

Vega measures sensitivity to implied volatility changes. This is important because trends often coincide with volatility regime changes.

**IV Behavior During Trends:**

During breakouts, IV typically increases due to uncertainty, benefiting long option positions through positive vega exposure. After trends establish, IV often decreases as the market becomes complacent about the new direction, hurting long positions. Post-earnings or post-news, IV often crushes regardless of price direction.

**IV Rank for Entry Timing:**

IV Rank measures current IV relative to its historical range:

$$\text{IV Rank} = \frac{\text{Current IV} - \text{52-week IV Low}}{\text{52-week IV High} - \text{52-week IV Low}} \times 100\%$$

**Entry Guidelines:**

| IV Rank | Interpretation | Action |
|---------|----------------|--------|
| < 30% | IV cheap | Favorable entry, room for IV expansion |
| 30-50% | IV moderate | Acceptable entry |
| 50-70% | IV elevated | Caution—consider debit spreads (see §4.6) |
| > 70% | IV expensive | Avoid naked long options; use spreads |

### 4.5 Greeks Summary for Trend Following

| Greek | Impact | Management Strategy |
|-------|--------|---------------------|
| Delta | Directional exposure | Match to trend strength (ITM for strong, ATM for moderate) |
| Gamma | Exposure acceleration | Favorable in trends, risk on reversal—use stops |
| Theta | Daily cost (negative) | Buy sufficient time (45-60 DTE), exit before decay accelerates |
| Vega | IV sensitivity | Enter when IV rank < 50%, be aware of crush risk |

### 4.6 Long Options vs. Debit Spreads: Managing the Theta/Vega Tradeoff

!!! tip "When IV Is Elevated"
    When IV rank exceeds 50%, naked long options become expensive. Debit spreads offer a compelling alternative that reduces vega exposure and theta decay at the cost of capping maximum profit.

**Long Call vs. Bull Call Spread Comparison:**

| Characteristic | Long Call | Bull Call Spread |
|----------------|-----------|------------------|
| Structure | Buy call | Buy lower strike call, sell higher strike call |
| Max Profit | Unlimited | Capped at (spread width − net debit) |
| Max Loss | Premium paid | Net debit paid |
| Theta | High negative | Reduced (short leg offsets) |
| Vega | High positive | Reduced (short leg offsets) |
| Best When | IV low, expecting large move | IV elevated, expecting moderate move |
| Capital Required | Higher | Lower |

**Example: IV = 45% (Elevated)**

Stock at \$100, moderate uptrend confirmed.

*Long Call Approach:*
- Buy \$100 call @ \$6.00
- Vega = +0.20, Theta = −\$0.08/day
- Breakeven: \$106
- Max loss: \$6.00

*Bull Call Spread Approach:*
- Buy \$100 call @ \$6.00, Sell \$110 call @ \$2.50
- Net debit: \$3.50
- Vega = +0.08, Theta = −\$0.03/day
- Breakeven: \$103.50
- Max profit: \$6.50 (if stock ≥ \$110)
- Max loss: \$3.50

**When to Use Each:**

| Condition | Preferred Structure |
|-----------|---------------------|
| IV Rank < 30% | Long options (cheap, room for expansion) |
| IV Rank 30-50% | Either (trader preference) |
| IV Rank 50-70% | Debit spreads (reduce vega/theta exposure) |
| IV Rank > 70% | Debit spreads required, or wait |
| Expecting explosive move | Long options (uncapped upside) |
| Expecting moderate move | Debit spreads (better risk/reward) |

**Debit Spread Strike Selection:**

For trend following with debit spreads:

1. **Long leg:** ATM or slightly OTM (capture initial delta)
2. **Short leg:** Place at realistic price target or next resistance
3. **Width:** 5-10% of stock price typically balances cost vs. profit potential

---

## 5. Trend Identification Methods

### 5.1 Moving Averages

**Simple Moving Average (SMA):**

$$\text{SMA}_n(t) = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}$$

**Exponential Moving Average (EMA):**

$$\text{EMA}_n(t) = \alpha \cdot P_t + (1-\alpha) \cdot \text{EMA}_n(t-1), \quad \alpha = \frac{2}{n+1}$$

**Single MA Rules:**

Price above MA indicates uptrend—consider long calls. Price below MA indicates downtrend—consider long puts. Price crossing MA suggests potential trend change—consider exit or reversal.

**Common Periods:**

20-day MA captures short-term trends, 50-day MA captures intermediate trends, and 200-day MA captures long-term trends. The relative position of these MAs provides trend context.

**Dual MA Crossover:**

$$\text{Signal}_t = \text{sign}(\text{MA}_{\text{fast}}(t) - \text{MA}_{\text{slow}}(t))$$

Golden cross occurs when 50-day MA crosses above 200-day MA (bullish). Death cross occurs when 50-day MA crosses below 200-day MA (bearish).

### 5.2 Average Directional Index (ADX)

ADX measures trend strength regardless of direction:

$$\text{ADX}_t = \text{EMA}_{14}\left(\frac{|+\text{DI} - (-\text{DI})|}{+\text{DI} + (-\text{DI})} \times 100\right)$$

where +DI and -DI are the positive and negative directional indicators.

**ADX Interpretation:**

| ADX Value | Trend Strength | Trading Implication |
|-----------|----------------|---------------------|
| < 20 | No trend | Avoid trend following strategies |
| 20-25 | Weak trend | Small positions only |
| 25-40 | Moderate trend | Standard position sizing |
| 40-50 | Strong trend | Larger positions, ITM options |
| > 50 | Very strong trend | Maximum exposure, rare opportunity |

!!! note "ADX Threshold"
    The ADX > 25 threshold is a commonly used heuristic in technical analysis literature (Wilder, 1978). While not derived from rigorous statistical testing, it serves as a practical filter to avoid trading in range-bound markets.

**Position Sizing Based on ADX:**

$$\text{Position Size} = \text{Base Size} \times \min\left(\frac{\text{ADX}}{25}, 2\right)$$

This formula scales position size with trend strength while capping at 2x base size.

### 5.3 MACD (Moving Average Convergence Divergence)

$$\text{MACD} = \text{EMA}_{12} - \text{EMA}_{26}$$
$$\text{Signal Line} = \text{EMA}_9(\text{MACD})$$
$$\text{Histogram} = \text{MACD} - \text{Signal Line}$$

**Trading Signals:**

MACD crossing above signal line is bullish—supports long calls. MACD crossing below signal line is bearish—supports long puts. Expanding histogram indicates strengthening momentum. Contracting histogram suggests weakening momentum—consider tightening stops.

**Divergence Warning:**

Price makes new high but MACD doesn't (bearish divergence)—trend may be weakening. Price makes new low but MACD doesn't (bullish divergence)—downtrend may be exhausting. Divergences are warning signals, not immediate action triggers.

### 5.4 RSI in Trend Context

$$\text{RSI} = 100 - \frac{100}{1 + \frac{\text{Average Gain}}{\text{Average Loss}}}$$

**Important: RSI Interpretation Differs in Trends**

In trend following, ignore traditional overbought/oversold interpretations. RSI > 70 in an uptrend signals strength, not a sell. RSI < 30 in a downtrend signals strength, not a buy.

**Useful RSI Signals:**

RSI crossing above 50 from below indicates momentum shift to bullish. RSI crossing below 50 from above indicates momentum shift to bearish. These centerline crosses can confirm trend changes.

### 5.5 Volume Confirmation

$$\text{Volume Ratio} = \frac{\text{Today's Volume}}{\text{20-day Average Volume}}$$

**Confirmation Rules:**

Volume ratio > 1.5 provides strong confirmation. Volume ratio > 2.0 provides very strong confirmation. Volume ratio < 1.0 indicates weak signal—proceed with caution.

**Valid Breakout Condition:**

$$\text{Valid Breakout} = (\text{Price} > \text{Resistance}) \land (\text{Volume Ratio} > 1.5)$$

Breakouts without volume confirmation have higher failure rates.

---

## 6. Strategy Implementation

### 6.1 Moving Average Trend Strategy

**Entry Conditions (Long Calls):**

1. Price crosses above 50-day MA
2. Volume above 20-day average
3. MACD positive or crossing positive
4. ADX > 25

**Entry Conditions (Long Puts):**

1. Price crosses below 50-day MA
2. Volume above 20-day average
3. MACD negative or crossing negative
4. ADX > 25

**Example Trade:**

Stock at \$350, crosses above 50-day MA (\$345) on 1.8x average volume. ADX at 28, MACD histogram positive and expanding.

Action: Buy \$355 calls, 45 DTE, at \$8 per contract.
Stop loss: Exit if price closes below 50-day MA.
Target: Next resistance level or 50-100% gain on premium.

### 6.2 Breakout Momentum Strategy

**Entry Conditions:**

1. Price breaks above resistance (calls) or below support (puts)
2. Volume > 2x average on breakout day
3. ADX > 25 and rising
4. No immediate counter-level (resistance above for calls, support below for puts)

### 6.3 Pullback Continuation Strategy

**Entry Conditions (Uptrend):**

1. Stock in established uptrend (price > 20, 50, and 200-day MAs)
2. Pullback to 20-day MA (healthy correction)
3. Bounce off MA with volume confirmation
4. ADX remains > 25 during pullback

### 6.4 Strong Momentum Strategy

**Entry Conditions:**

1. ADX crosses above 40 (very strong trend)
2. Price making new highs (uptrend) or new lows (downtrend)
3. MACD histogram expanding
4. RSI > 60 (uptrend) or RSI < 40 (downtrend)

**Strike Selection:**

Use ITM options (delta 0.70-0.85) for maximum trend capture when momentum is very strong.

---

## 7. Strike Selection Framework

### 7.1 ITM Options (Delta 0.70-0.85)

**Characteristics:**

Higher premium but lower leverage. Less sensitive to theta decay as percentage of value. Retains intrinsic value even if trend slows. Behaves more like stock ownership.

**When to Use:**

Very strong trends (ADX > 40), when you want stock-like exposure with defined risk, when you have larger capital available, or for conservative approach prioritizing trend capture over leverage.

### 7.2 ATM Options (Delta 0.45-0.55)

**Characteristics:**

Moderate premium with balanced leverage. Highest gamma—delta increases favorably as trend develops. Most liquid with tightest bid-ask spreads. Standard choice for most trend-following applications.

**When to Use:**

Moderate trends (ADX 25-40), standard approach for most traders, good risk/reward balance, or when seeking high gamma exposure.

### 7.3 OTM Options (Delta 0.20-0.40)

**Characteristics:**

Cheap premium with high leverage. Low delta means small absolute gains per dollar of underlying move. High theta decay as percentage of value. Requires larger underlying move to profit.

**When to Use:**

Strong breakout expected (ADX > 35 and rising), limited capital situations, aggressive speculation with defined risk, or high conviction short-term plays.

### 7.4 Strike Selection Decision Matrix

**Based on Trend Strength:**

| ADX Range | Recommended Strike | Delta Target | Rationale |
|-----------|-------------------|--------------|-----------|
| < 25 | Don't trade | — | Trend too weak |
| 25-35 | ATM | 0.45-0.55 | Balanced approach |
| 35-45 | ATM to ITM | 0.50-0.70 | Capture strong trend |
| > 45 | ITM | 0.70-0.85 | Maximize trend capture |

---

## 8. Time Horizon Selection

### 8.1 Short-Term (< 30 DTE)

**Characteristics:**

Cheap premium but rapid theta decay. Requires quick, strong move. High-risk, high-reward profile.

**When to Use:**

Strong momentum breakout (ADX > 40), short-term catalyst (earnings, news), very high conviction with clear near-term target.

**Caution:**

Only for experienced traders. Theta decay accelerates rapidly in final 2 weeks. Most positions will expire worthless without strong move.

### 8.2 Medium-Term (30-60 DTE) — Recommended

**Characteristics:**

Moderate premium with manageable theta decay. Sufficient time for trend to develop. Good balance of cost and time value. Allows for position management (rolling, adjustments).

**When to Use:**

Standard approach for most trend-following trades. Confirmed trends (ADX > 25). Gives trend time to overcome short-term noise.

!!! success "Recommended Default"
    **45-60 DTE is the sweet spot for trend following.** This provides sufficient time for trends to develop while avoiding the steepest portion of the theta decay curve.

### 8.3 Long-Term (60+ DTE, LEAPS)

**Characteristics:**

Higher premium but very slow theta decay. Time for major multi-month trends. Behaves like leveraged stock. Can weather intermediate pullbacks.

**When to Use:**

Very strong long-term trends, want stock exposure with defined risk, multi-month or year-long view, have patient capital.

### 8.4 Time Selection Decision Matrix

**Based on ADX:**

$$\text{Minimum DTE} = \begin{cases} 30 & \text{if ADX} > 40 \\ 45 & \text{if } 30 < \text{ADX} \leq 40 \\ 60 & \text{if } 25 < \text{ADX} \leq 30 \end{cases}$$

Stronger trends require less time buffer because the move is likely to be faster.

---

## 9. Position Sizing and Risk Management

### 9.1 Position Sizing Using Kelly Criterion

The Kelly criterion provides the mathematically optimal bet size to maximize long-term wealth growth:

$$f^* = \frac{p \cdot b - q}{b}$$

where $f^*$ is fraction of capital to bet, $p$ is probability of winning, $q = 1 - p$ is probability of losing, and $b$ is ratio of win size to loss size (payoff odds).

**Example:**

Historical win rate $p = 0.40$, average winner is 2x average loser ($b = 2$):

$$f^* = \frac{0.40 \times 2 - 0.60}{2} = \frac{0.20}{2} = 0.10 = 10\%$$

**Practical Application:**

Full Kelly is too aggressive for most traders. Use fractional Kelly (typically 1/4 to 1/2 Kelly) to reduce drawdowns:

$$f_{\text{practical}} = 0.25 \times f^* = 2.5\%$$

### 9.2 Fixed Percentage Approach

For simplicity, many traders use fixed percentage allocation:

**Conservative:** 1-2% of portfolio per position
**Moderate:** 2-3% of portfolio per position
**Aggressive:** 3-5% of portfolio per position

**Position Size Formula:**

$$\text{Contracts} = \frac{\text{Allocation} \times \text{Portfolio Value}}{\text{Premium per Contract} \times 100}$$

### 9.3 Volatility-Adjusted Position Sizing

Adjust position size based on underlying volatility using Average True Range (ATR):

$$\text{Position Size} = \frac{\text{Account Risk}}{\text{ATR} \times \text{Multiplier}}$$

This ensures roughly equal dollar risk across positions with different volatilities.

### 9.4 Stop Loss Rules

!!! danger "Hard Rule: -50% Stop Loss"
    Exit if option loses 50% of initial value. **No exceptions.** This single rule prevents catastrophic losses and preserves capital for future opportunities.

**Price-Based Stop:**

Exit if underlying closes below entry breakout level (for calls) or above breakdown level (for puts).

**Technical Stop:**

Exit if ADX drops below 20 (trend dead), price crosses back through key moving average, or MACD crosses against position direction.

**Time Stop:**

Exit if 50% of time elapsed with less than 25% progress toward target. Exit all positions within 10-14 days of expiration unless deep ITM.

### 9.5 ATR-Based Stop Placement

Rather than fixed percentage stops, use ATR for volatility-adjusted stops:

$$\text{Stop Distance} = k \times \text{ATR}_{14}$$

where $k$ typically ranges from 1.5 to 3.0.

**Example:**

Stock at \$100, ATR(14) = \$3, using $k = 2$:
Stop distance = 2 × \$3 = \$6
Stop level = \$100 - \$6 = \$94

This approach keeps stops consistent in risk terms across different volatility environments.

---

## 10. Entry and Exit Execution

### 10.1 Entry Checklist

Before entering any trend-following position, verify ALL conditions:

**Trend Confirmation:**

- [ ] Price above/below key MA (specify which)
- [ ] ADX > 25
- [ ] MACD in agreement with direction

**Volume Confirmation:**

- [ ] Breakout on > 1.5x average volume, OR
- [ ] Sustained above-average volume on trend continuation

**Technical Setup:**

- [ ] Clear support/resistance levels identified
- [ ] Breakout above resistance (calls) or below support (puts)
- [ ] No immediate counter-level within expected move

**Options Conditions:**

- [ ] IV rank < 70% (or use spreads if higher)
- [ ] Sufficient liquidity (bid-ask spread < 10% of mid price)
- [ ] Appropriate DTE (45-60 minimum for moderate trends)
- [ ] Appropriate strike for trend strength

**Risk Management:**

- [ ] Position size ≤ 2-5% of portfolio
- [ ] Stop loss level identified
- [ ] Profit target identified
- [ ] Maximum loss acceptable both financially and psychologically

!!! warning "Entry Discipline"
    **If any checkbox is unchecked, do not trade.** Partial setups lead to inconsistent results and erode discipline over time.

### 10.2 Exit Decision Framework

Execute exits in this priority order:

```
1. Option down 50%?
   → YES: Exit immediately (stop loss)
   → NO: Continue to step 2

2. Profit target reached?
   → YES: Exit full or partial position
   → NO: Continue to step 3

3. Price-based or technical stop triggered?
   → YES: Exit immediately
   → NO: Continue to step 4

4. 50% of time elapsed?
   → YES: Profit at least 25%?
      → NO: Exit (time stop)
      → YES: Hold with trailing stop
   → NO: Continue holding

5. Within 10-14 days of expiration?
   → YES: Exit (theta acceleration)
   → NO: Continue holding
```

### 10.3 Scaling In (Pyramiding)

**Rule:** Only add to winning positions when trend is strengthening.

**Method:**

1. Initial entry: 50% of planned position
2. Trend continues (+5% in underlying): Add 25%
3. Trend strengthens (+10% in underlying): Add final 25%

**Never add to losing positions.** Averaging down destroys capital.

### 10.4 Scaling Out (Profit Taking)

**Rule:** Take partial profits at predetermined targets, let remainder run.

**Method:**

1. 50% profit: Sell 50% of position
2. 100% profit: Sell 25% of position
3. Let final 25% run with trailing stop

This approach guarantees profit while maintaining upside exposure.

### 10.5 Rolling Positions

When a trend continues but expiration approaches, consider rolling:

**Roll Trigger:**

Position profitable, trend intact, but < 21 DTE remaining.

**Roll Mechanics:**

1. Close current position (take profit)
2. Open new position at same or higher strike
3. Choose new expiration 45-60 DTE out

**Roll Cost Consideration:**

Rolling incurs transaction costs (commissions + bid-ask spread on both legs). Factor in approximately 1-3% of position value as roll friction.

---

## 11. Portfolio-Level Considerations

### 11.1 Correlation Risk

Multiple trend-following positions may be correlated, especially within sectors.

**Risk Mitigation:**

Limit total sector exposure to 10-15% of portfolio. Diversify across uncorrelated assets (tech, financials, commodities, etc.). Monitor portfolio beta exposure. Consider hedging concentrated positions.

### 11.2 Beta Exposure Management

Aggregate beta exposure from all positions:

$$\beta_{\text{portfolio}} = \sum_{i} w_i \cdot \beta_i \cdot \frac{\Delta_i \cdot S_i}{P}$$

where $w_i$ is weight, $\beta_i$ is stock beta, $\Delta_i$ is option delta, $S_i$ is stock price, and $P$ is portfolio value.

Monitor to avoid excessive market exposure during risk-on periods.

### 11.3 Maximum Drawdown Considerations

Trend following can experience significant drawdowns during:

- Trend reversals
- Whipsaw markets (ADX < 20)
- Volatility regime changes

**Risk Limits:**

Set maximum portfolio drawdown tolerance (e.g., 20%). Reduce position sizes or pause trading if drawdown exceeds threshold. Maintain cash buffer for opportunities after drawdowns.

---

## 12. Backtesting Methodology

### 12.1 Backtesting Framework

Any trend-following system must be validated through rigorous backtesting before live deployment.

**Key Metrics to Track:**

| Metric | Formula | Target |
|--------|---------|--------|
| Win Rate | Winning Trades / Total Trades | 35-45% |
| Profit Factor | Gross Profit / Gross Loss | > 1.5 |
| Sharpe Ratio | (Return - Rf) / Volatility | > 0.5 |
| Sortino Ratio | (Return - Rf) / Downside Vol | > 0.7 |
| Maximum Drawdown | Peak-to-Trough Decline | < 25% |
| Calmar Ratio | CAGR / Max Drawdown | > 0.5 |
| Average Win / Average Loss | Mean Winner / Mean Loser | > 2.0 |
| Expectancy | (Win% × Avg Win) - (Loss% × Avg Loss) | > 0 |

### 12.2 Avoiding Backtest Pitfalls

**Survivorship Bias:**

Use point-in-time data that includes delisted securities. Don't backtest only on stocks that survived to present day.

**Look-Ahead Bias:**

Ensure signals use only information available at decision time. Don't use future data to make past decisions.

**Overfitting:**

Keep parameters simple and robust. Validate on out-of-sample data. Be suspicious of systems with too many optimized parameters.

**Transaction Costs:**

Include realistic bid-ask spreads (options can have wide spreads). Account for slippage on entry and exit. Include commissions if applicable.

### 12.3 Backtest Limitations Disclosure

!!! warning "Critical Limitations of Educational Backtests"
    The backtest code provided in this chapter is for **educational purposes** and has significant limitations that would affect real-world performance:
    
    **Not Modeled:**
    
    - **Implied volatility dynamics:** IV is estimated from realized volatility, not actual option market data
    - **Bid-ask spreads:** Execution assumes mid-price; real spreads can be 5-20% of premium
    - **Slippage:** Market impact not modeled; large orders move prices
    - **Early exercise risk:** American option exercise not modeled
    - **Dividend risk:** Ex-dividend drops not incorporated
    - **Liquidity constraints:** Assumes unlimited liquidity at model prices
    - **Gap risk:** Overnight/weekend gaps not explicitly modeled
    - **Roll costs:** Position rolling friction understated
    
    **Impact:** Real-world performance typically degrades 30-50% relative to frictionless backtests. Always add realistic friction before drawing conclusions.
    
    **Recommended Additions for Production:**
    
    1. Use actual historical option prices (CBOE, OptionMetrics)
    2. Add bid-ask spread: deduct 0.5 × spread on entry and exit
    3. Add slippage: 0.5-1% of premium per trade
    4. Model execution at next-day open, not signal-day close

---

## 13. Python Implementation

### 13.1 Momentum Factor Calculation

```python
import numpy as np
import pandas as pd

def calculate_momentum_factor(prices: pd.Series, 
                               formation_period: int = 252,
                               skip_period: int = 21) -> pd.Series:
    """
    Calculate momentum factor (past returns excluding recent month).
    
    Jegadeesh-Titman style momentum: returns from t-12 to t-1 months.
    
    Parameters
    ----------
    prices : pd.Series
        Price series (adjusted close)
    formation_period : int
        Lookback period in trading days (252 ≈ 12 months)
    skip_period : int
        Recent period to skip (21 ≈ 1 month) to avoid reversal
        
    Returns
    -------
    pd.Series
        Momentum factor values
    """
    # Calculate returns over formation period, skipping recent period
    momentum = (prices.shift(skip_period) / 
                prices.shift(formation_period + skip_period) - 1)
    return momentum


def momentum_autocorrelation(returns: pd.Series, 
                              lags: list = [1, 5, 21]) -> dict:
    """
    Calculate return autocorrelation at various lags.
    
    Parameters
    ----------
    returns : pd.Series
        Return series
    lags : list
        List of lag periods to test
        
    Returns
    -------
    dict
        Autocorrelation coefficients and p-values
    """
    from scipy import stats
    
    results = {}
    for lag in lags:
        # Calculate autocorrelation
        autocorr = returns.autocorr(lag=lag)
        
        # Statistical significance (approximate)
        n = len(returns) - lag
        se = 1 / np.sqrt(n)
        t_stat = autocorr / se
        p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=n-1))
        
        results[f'lag_{lag}'] = {
            'autocorrelation': autocorr,
            't_statistic': t_stat,
            'p_value': p_value,
            'significant_5pct': p_value < 0.05
        }
    
    return results
```

### 13.2 Trend Identification Indicators

```python
def calculate_sma(prices: pd.Series, window: int) -> pd.Series:
    """Simple Moving Average."""
    return prices.rolling(window=window).mean()


def calculate_ema(prices: pd.Series, span: int) -> pd.Series:
    """Exponential Moving Average."""
    return prices.ewm(span=span, adjust=False).mean()


def calculate_macd(prices: pd.Series,
                   fast: int = 12,
                   slow: int = 26,
                   signal: int = 9) -> pd.DataFrame:
    """
    Calculate MACD indicator.
    
    Returns DataFrame with MACD line, signal line, and histogram.
    """
    ema_fast = calculate_ema(prices, fast)
    ema_slow = calculate_ema(prices, slow)
    
    macd_line = ema_fast - ema_slow
    signal_line = calculate_ema(macd_line, signal)
    histogram = macd_line - signal_line
    
    return pd.DataFrame({
        'macd': macd_line,
        'signal': signal_line,
        'histogram': histogram
    })


def calculate_adx(high: pd.Series, 
                  low: pd.Series, 
                  close: pd.Series,
                  period: int = 14) -> pd.DataFrame:
    """
    Calculate ADX (Average Directional Index).
    
    Returns DataFrame with ADX, +DI, and -DI.
    """
    # True Range
    tr1 = high - low
    tr2 = abs(high - close.shift(1))
    tr3 = abs(low - close.shift(1))
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr = tr.ewm(span=period, adjust=False).mean()
    
    # Directional Movement
    up_move = high - high.shift(1)
    down_move = low.shift(1) - low
    
    plus_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0)
    minus_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0)
    
    plus_dm = pd.Series(plus_dm, index=high.index)
    minus_dm = pd.Series(minus_dm, index=high.index)
    
    # Smoothed DM
    plus_dm_smooth = plus_dm.ewm(span=period, adjust=False).mean()
    minus_dm_smooth = minus_dm.ewm(span=period, adjust=False).mean()
    
    # Directional Indicators
    plus_di = 100 * plus_dm_smooth / atr
    minus_di = 100 * minus_dm_smooth / atr
    
    # ADX
    dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di)
    adx = dx.ewm(span=period, adjust=False).mean()
    
    return pd.DataFrame({
        'adx': adx,
        'plus_di': plus_di,
        'minus_di': minus_di
    })


def calculate_rsi(prices: pd.Series, period: int = 14) -> pd.Series:
    """Calculate RSI (Relative Strength Index)."""
    delta = prices.diff()
    
    gain = delta.where(delta > 0, 0)
    loss = (-delta).where(delta < 0, 0)
    
    avg_gain = gain.ewm(span=period, adjust=False).mean()
    avg_loss = loss.ewm(span=period, adjust=False).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi
```

### 13.3 Trend Signal Generator

```python
def generate_trend_signals(prices: pd.DataFrame,
                           ma_short: int = 20,
                           ma_long: int = 50,
                           adx_threshold: float = 25,
                           volume_threshold: float = 1.5) -> pd.DataFrame:
    """
    Generate trend-following signals based on multiple indicators.
    
    Parameters
    ----------
    prices : pd.DataFrame
        OHLCV data with columns: Open, High, Low, Close, Volume
    ma_short : int
        Short-term moving average period
    ma_long : int
        Long-term moving average period
    adx_threshold : float
        Minimum ADX for trend confirmation
    volume_threshold : float
        Minimum volume ratio for signal confirmation
        
    Returns
    -------
    pd.DataFrame
        Signals and indicator values
    """
    close = prices['Close']
    high = prices['High']
    low = prices['Low']
    volume = prices['Volume']
    
    # Moving Averages
    sma_short = calculate_sma(close, ma_short)
    sma_long = calculate_sma(close, ma_long)
    
    # MACD
    macd = calculate_macd(close)
    
    # ADX
    adx = calculate_adx(high, low, close)
    
    # RSI
    rsi = calculate_rsi(close)
    
    # Volume ratio
    avg_volume = volume.rolling(window=20).mean()
    volume_ratio = volume / avg_volume
    
    # Generate signals
    signals = pd.DataFrame(index=prices.index)
    signals['close'] = close
    signals['sma_short'] = sma_short
    signals['sma_long'] = sma_long
    signals['macd'] = macd['macd']
    signals['macd_signal'] = macd['signal']
    signals['macd_histogram'] = macd['histogram']
    signals['adx'] = adx['adx']
    signals['plus_di'] = adx['plus_di']
    signals['minus_di'] = adx['minus_di']
    signals['rsi'] = rsi
    signals['volume_ratio'] = volume_ratio
    
    # Trend conditions
    uptrend = (
        (close > sma_short) & 
        (sma_short > sma_long) &
        (macd['macd'] > macd['signal']) &
        (adx['adx'] > adx_threshold) &
        (adx['plus_di'] > adx['minus_di'])
    )
    
    downtrend = (
        (close < sma_short) & 
        (sma_short < sma_long) &
        (macd['macd'] < macd['signal']) &
        (adx['adx'] > adx_threshold) &
        (adx['minus_di'] > adx['plus_di'])
    )
    
    # Entry signals (trend confirmed + volume)
    signals['buy_signal'] = uptrend & (volume_ratio > volume_threshold)
    signals['sell_signal'] = downtrend & (volume_ratio > volume_threshold)
    
    # Trend strength for position sizing
    signals['trend_strength'] = np.where(
        signals['adx'] > adx_threshold,
        np.minimum(signals['adx'] / 25, 2.0),  # Cap at 2x
        0
    )
    
    return signals
```

### 13.4 Options Greeks Calculator

```python
from scipy.stats import norm
from scipy.optimize import brentq

def black_scholes_greeks(S: float, K: float, T: float, 
                          r: float, sigma: float, 
                          option_type: str = 'call') -> dict:
    """
    Calculate Black-Scholes option price and Greeks.
    
    Parameters
    ----------
    S : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to expiration in years
    r : float
        Risk-free rate
    sigma : float
        Volatility
    option_type : str
        'call' or 'put'
        
    Returns
    -------
    dict
        Price and Greeks:
        - price: Option price
        - delta: Per $1 underlying move
        - gamma: Per $1 underlying move
        - theta: Per calendar day (negative for long)
        - vega: Per 1 percentage point IV change
        - rho: Per 1 percentage point rate change
    """
    if T <= 0:
        # At expiration
        if option_type == 'call':
            price = max(S - K, 0)
            delta = 1.0 if S > K else 0.0
        else:
            price = max(K - S, 0)
            delta = -1.0 if S < K else 0.0
        return {
            'price': price, 'delta': delta, 'gamma': 0,
            'theta': 0, 'vega': 0, 'rho': 0
        }
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    # Price
    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        delta = norm.cdf(d1)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        delta = -norm.cdf(-d1)
    
    # Greeks (same for calls and puts except delta, rho)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    
    # Theta: annual, then convert to daily
    theta_annual = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
    if option_type == 'call':
        theta_annual -= r * K * np.exp(-r * T) * norm.cdf(d2)
        rho = K * T * np.exp(-r * T) * norm.cdf(d2)
    else:
        theta_annual += r * K * np.exp(-r * T) * norm.cdf(-d2)
        rho = -K * T * np.exp(-r * T) * norm.cdf(-d2)
    
    # Convert theta to per calendar day (negative for long options)
    theta_daily = theta_annual / 365
    
    # Vega: per 1 percentage point (0.01) IV change
    vega = S * norm.pdf(d1) * np.sqrt(T) / 100
    
    # Rho: per 1 percentage point rate change
    rho = rho / 100
    
    return {
        'price': price,
        'delta': delta,
        'gamma': gamma,
        'theta': theta_daily,  # Negative for long options
        'vega': vega,          # Per 1 vol point
        'rho': rho             # Per 1% rate change
    }


def calculate_iv_rank(current_iv: float, 
                      iv_history: pd.Series,
                      lookback: int = 252) -> float:
    """
    Calculate IV Rank (percentile of current IV vs history).
    
    Parameters
    ----------
    current_iv : float
        Current implied volatility
    iv_history : pd.Series
        Historical IV values
    lookback : int
        Number of days to look back
        
    Returns
    -------
    float
        IV Rank (0-100)
    """
    recent_iv = iv_history.tail(lookback)
    iv_min = recent_iv.min()
    iv_max = recent_iv.max()
    
    if iv_max == iv_min:
        return 50.0
    
    iv_rank = (current_iv - iv_min) / (iv_max - iv_min) * 100
    return iv_rank
```

### 13.5 Position Sizing Calculator

```python
def kelly_position_size(win_rate: float, 
                        avg_win: float, 
                        avg_loss: float,
                        kelly_fraction: float = 0.25) -> float:
    """
    Calculate position size using fractional Kelly criterion.
    
    Parameters
    ----------
    win_rate : float
        Historical win rate (0-1)
    avg_win : float
        Average winning trade size
    avg_loss : float
        Average losing trade size (positive number)
    kelly_fraction : float
        Fraction of full Kelly to use (default 0.25)
        
    Returns
    -------
    float
        Recommended position size as fraction of portfolio
    """
    if avg_loss == 0:
        return 0
    
    b = avg_win / avg_loss  # Payoff ratio
    p = win_rate
    q = 1 - p
    
    # Full Kelly
    full_kelly = (p * b - q) / b
    
    # Fractional Kelly
    position_size = kelly_fraction * full_kelly
    
    # Cap at reasonable maximum
    return max(0, min(position_size, 0.10))


def calculate_position_size(portfolio_value: float,
                            premium_per_contract: float,
                            allocation_pct: float = 0.02,
                            adx: float = 25,
                            max_contracts: int = 10) -> int:
    """
    Calculate number of contracts based on allocation and trend strength.
    
    Parameters
    ----------
    portfolio_value : float
        Total portfolio value
    premium_per_contract : float
        Option premium per contract (premium × 100)
    allocation_pct : float
        Base allocation percentage
    adx : float
        Current ADX value
    max_contracts : int
        Maximum contracts allowed
        
    Returns
    -------
    int
        Number of contracts to trade
    """
    # ADX scaling factor (1.0 at ADX=25, max 2.0)
    adx_multiplier = min(adx / 25, 2.0)
    
    # Adjusted allocation
    adjusted_allocation = allocation_pct * adx_multiplier
    
    # Dollar amount
    dollar_allocation = portfolio_value * adjusted_allocation
    
    # Number of contracts
    contracts = int(dollar_allocation / premium_per_contract)
    
    return min(max(contracts, 0), max_contracts)
```

### 13.6 Backtest Engine (with Transaction Costs)

```python
class TrendFollowingBacktest:
    """
    Backtesting engine for trend-following options strategies.
    
    IMPORTANT: This is an educational prototype with significant limitations.
    See Section 12.3 for full disclosure of assumptions and limitations.
    """
    
    def __init__(self, 
                 initial_capital: float = 100000,
                 max_position_pct: float = 0.05,
                 stop_loss_pct: float = 0.50,
                 profit_target_pct: float = 1.00,
                 max_dte: int = 60,
                 min_dte: int = 14,
                 # Transaction cost parameters
                 spread_pct: float = 0.02,      # Bid-ask spread as % of premium
                 slippage_pct: float = 0.01,    # Slippage as % of premium
                 commission_per_contract: float = 0.65):  # Per contract commission
        """
        Initialize backtest parameters.
        
        Transaction Cost Model:
        - spread_pct: Deducted on entry and exit (half-spread each way)
        - slippage_pct: Additional execution cost
        - commission_per_contract: Flat fee per contract traded
        """
        self.initial_capital = initial_capital
        self.max_position_pct = max_position_pct
        self.stop_loss_pct = stop_loss_pct
        self.profit_target_pct = profit_target_pct
        self.max_dte = max_dte
        self.min_dte = min_dte
        
        # Transaction costs
        self.spread_pct = spread_pct
        self.slippage_pct = slippage_pct
        self.commission_per_contract = commission_per_contract
        
        self.reset()
    
    def reset(self):
        """Reset backtest state."""
        self.capital = self.initial_capital
        self.positions = []
        self.trades = []
        self.equity_curve = []
        self.total_commissions = 0
        self.total_slippage = 0
        
    def _apply_entry_costs(self, premium: float, contracts: int) -> float:
        """Apply transaction costs on entry, return effective cost."""
        gross_cost = premium * 100 * contracts
        
        # Spread cost (pay half the spread)
        spread_cost = gross_cost * (self.spread_pct / 2)
        
        # Slippage
        slippage_cost = gross_cost * self.slippage_pct
        
        # Commissions
        commission = self.commission_per_contract * contracts
        
        self.total_commissions += commission
        self.total_slippage += spread_cost + slippage_cost
        
        return gross_cost + spread_cost + slippage_cost + commission
    
    def _apply_exit_costs(self, premium: float, contracts: int) -> float:
        """Apply transaction costs on exit, return effective proceeds."""
        gross_proceeds = premium * 100 * contracts
        
        # Spread cost (pay half the spread)
        spread_cost = gross_proceeds * (self.spread_pct / 2)
        
        # Slippage
        slippage_cost = gross_proceeds * self.slippage_pct
        
        # Commissions
        commission = self.commission_per_contract * contracts
        
        self.total_commissions += commission
        self.total_slippage += spread_cost + slippage_cost
        
        return gross_proceeds - spread_cost - slippage_cost - commission
    
    def run_backtest(self, 
                     prices: pd.DataFrame,
                     signals: pd.DataFrame,
                     iv_data: pd.Series = None,
                     risk_free_rate: float = 0.05) -> dict:
        """
        Run backtest on historical data.
        
        Parameters
        ----------
        prices : pd.DataFrame
            OHLCV price data
        signals : pd.DataFrame
            Signal data from generate_trend_signals()
        iv_data : pd.Series
            Implied volatility data (optional, will estimate if None)
        risk_free_rate : float
            Risk-free rate for options pricing
            
        Returns
        -------
        dict
            Performance metrics and trade log
        """
        self.reset()
        
        # Estimate IV if not provided (LIMITATION: uses realized vol)
        if iv_data is None:
            returns = prices['Close'].pct_change()
            iv_data = returns.rolling(21).std() * np.sqrt(252)
        
        for i, date in enumerate(prices.index[self.max_dte:], self.max_dte):
            current_price = prices.loc[date, 'Close']
            current_iv = iv_data.loc[date] if date in iv_data.index else 0.30
            
            # Update existing positions
            self._update_positions(date, current_price, current_iv, 
                                   risk_free_rate)
            
            # Check for new signals
            if date in signals.index:
                signal_row = signals.loc[date]
                
                if signal_row.get('buy_signal', False) and len(self.positions) == 0:
                    self._enter_position(date, current_price, current_iv,
                                        risk_free_rate, 'call',
                                        signal_row.get('trend_strength', 1.0))
                
                elif signal_row.get('sell_signal', False) and len(self.positions) == 0:
                    self._enter_position(date, current_price, current_iv,
                                        risk_free_rate, 'put',
                                        signal_row.get('trend_strength', 1.0))
            
            # Record equity
            position_value = sum(p['current_value'] for p in self.positions)
            self.equity_curve.append({
                'date': date,
                'capital': self.capital,
                'position_value': position_value,
                'total_equity': self.capital + position_value
            })
        
        return self._calculate_metrics()
    
    def _enter_position(self, date, price, iv, rf, option_type, trend_strength):
        """Enter a new position with transaction costs."""
        # Calculate position size
        premium_estimate = price * 0.03  # Rough estimate
        position_size = calculate_position_size(
            self.capital, premium_estimate * 100,
            self.max_position_pct, trend_strength * 25
        )
        
        if position_size == 0:
            return
        
        # Strike selection (ATM for simplicity)
        strike = round(price / 5) * 5  # Round to nearest $5
        
        # Calculate option price
        T = self.max_dte / 365
        greeks = black_scholes_greeks(price, strike, T, rf, iv, option_type)
        premium = greeks['price']
        
        # Apply entry costs
        total_cost = self._apply_entry_costs(premium, position_size)
        
        if total_cost > self.capital * self.max_position_pct:
            return
        
        self.capital -= total_cost
        
        self.positions.append({
            'entry_date': date,
            'entry_price': price,
            'strike': strike,
            'option_type': option_type,
            'contracts': position_size,
            'entry_premium': premium,
            'entry_cost': total_cost,  # Includes transaction costs
            'current_value': premium * 100 * position_size,  # Mark-to-market
            'dte': self.max_dte
        })
    
    def _update_positions(self, date, price, iv, rf):
        """Update positions and check for exits."""
        positions_to_close = []
        
        for i, pos in enumerate(self.positions):
            # Update DTE
            pos['dte'] -= 1
            
            # Calculate current value (mark-to-market, no transaction costs)
            T = max(pos['dte'], 1) / 365
            greeks = black_scholes_greeks(
                price, pos['strike'], T, rf, iv, pos['option_type']
            )
            current_premium = greeks['price']
            pos['current_value'] = current_premium * 100 * pos['contracts']
            
            # Check exit conditions (based on entry cost for accurate P&L)
            pnl_pct = (pos['current_value'] - pos['entry_cost']) / pos['entry_cost']
            
            exit_reason = None
            
            # Stop loss
            if pnl_pct <= -self.stop_loss_pct:
                exit_reason = 'stop_loss'
            # Profit target
            elif pnl_pct >= self.profit_target_pct:
                exit_reason = 'profit_target'
            # Time stop
            elif pos['dte'] <= self.min_dte:
                exit_reason = 'time_stop'
            
            if exit_reason:
                positions_to_close.append((i, exit_reason, current_premium))
        
        # Close positions (reverse order to maintain indices)
        for i, reason, exit_premium in sorted(positions_to_close, reverse=True):
            pos = self.positions.pop(i)
            
            # Apply exit costs
            proceeds = self._apply_exit_costs(exit_premium, pos['contracts'])
            self.capital += proceeds
            
            # Calculate actual P&L including all costs
            pnl = proceeds - pos['entry_cost']
            pnl_pct = pnl / pos['entry_cost']
            
            self.trades.append({
                'entry_date': pos['entry_date'],
                'exit_date': date,
                'option_type': pos['option_type'],
                'contracts': pos['contracts'],
                'entry_premium': pos['entry_premium'],
                'exit_premium': exit_premium,
                'entry_cost': pos['entry_cost'],
                'exit_proceeds': proceeds,
                'pnl': pnl,
                'pnl_pct': pnl_pct,
                'exit_reason': reason
            })
    
    def _calculate_metrics(self) -> dict:
        """Calculate comprehensive performance metrics."""
        if not self.trades:
            return {'error': 'No trades executed'}
        
        trades_df = pd.DataFrame(self.trades)
        equity_df = pd.DataFrame(self.equity_curve)
        
        # Basic metrics
        total_trades = len(trades_df)
        winners = trades_df[trades_df['pnl'] > 0]
        losers = trades_df[trades_df['pnl'] <= 0]
        
        win_rate = len(winners) / total_trades if total_trades > 0 else 0
        
        avg_win = winners['pnl_pct'].mean() if len(winners) > 0 else 0
        avg_loss = abs(losers['pnl_pct'].mean()) if len(losers) > 0 else 0
        
        gross_profit = winners['pnl'].sum() if len(winners) > 0 else 0
        gross_loss = abs(losers['pnl'].sum()) if len(losers) > 0 else 0
        
        profit_factor = (
            gross_profit / gross_loss
            if gross_loss > 0
            else float('inf')
        )
        
        # Equity curve metrics
        final_equity = equity_df['total_equity'].iloc[-1]
        total_return = final_equity / self.initial_capital - 1
        
        # CAGR (assuming daily data)
        n_days = len(equity_df)
        n_years = n_days / 252
        cagr = (final_equity / self.initial_capital) ** (1 / n_years) - 1 if n_years > 0 else 0
        
        # Max drawdown
        rolling_max = equity_df['total_equity'].cummax()
        drawdown = (equity_df['total_equity'] - rolling_max) / rolling_max
        max_drawdown = abs(drawdown.min())
        
        # Sharpe ratio (annualized)
        equity_df['returns'] = equity_df['total_equity'].pct_change()
        daily_returns = equity_df['returns'].dropna()
        
        sharpe = (
            daily_returns.mean() / daily_returns.std() * np.sqrt(252)
        ) if daily_returns.std() > 0 else 0
        
        # Sortino ratio (downside deviation only)
        downside_returns = daily_returns[daily_returns < 0]
        downside_std = downside_returns.std() if len(downside_returns) > 0 else 0
        sortino = (
            daily_returns.mean() / downside_std * np.sqrt(252)
        ) if downside_std > 0 else 0
        
        # Calmar ratio
        calmar = cagr / max_drawdown if max_drawdown > 0 else 0
        
        return {
            'total_trades': total_trades,
            'win_rate': win_rate,
            'avg_win': avg_win,
            'avg_loss': avg_loss,
            'profit_factor': profit_factor,
            'total_return': total_return,
            'cagr': cagr,
            'max_drawdown': max_drawdown,
            'sharpe_ratio': sharpe,
            'sortino_ratio': sortino,
            'calmar_ratio': calmar,
            'expectancy': win_rate * avg_win - (1 - win_rate) * avg_loss,
            'total_commissions': self.total_commissions,
            'total_slippage': self.total_slippage,
            'total_friction': self.total_commissions + self.total_slippage,
            'trades': trades_df,
            'equity_curve': equity_df
        }
```

### 13.7 Variance Ratio Test

```python
def variance_ratio_test(returns: pd.Series, 
                        periods: list = [2, 5, 10, 20]) -> dict:
    """
    Variance ratio test for random walk hypothesis.
    
    VR > 1 suggests positive autocorrelation (trending)
    VR < 1 suggests negative autocorrelation (mean-reverting)
    VR = 1 suggests random walk
    
    Parameters
    ----------
    returns : pd.Series
        Return series
    periods : list
        Periods to test
        
    Returns
    -------
    dict
        Variance ratios and statistics for each period
    """
    from scipy import stats
    
    results = {}
    returns = returns.dropna()
    n = len(returns)
    
    # Base variance (1-period)
    var_1 = returns.var()
    
    for q in periods:
        if n < q * 2:
            continue
            
        # q-period returns
        returns_q = returns.rolling(q).sum().dropna()
        var_q = returns_q.var()
        
        # Variance ratio
        vr = var_q / (q * var_1)
        
        # Standard error (Lo-MacKinlay)
        se = np.sqrt(2 * (2 * q - 1) * (q - 1) / (3 * q * n))
        
        # Z-statistic
        z_stat = (vr - 1) / se
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        
        results[f'VR({q})'] = {
            'variance_ratio': vr,
            'z_statistic': z_stat,
            'p_value': p_value,
            'interpretation': (
                'trending' if vr > 1 else 
                'mean-reverting' if vr < 1 else 
                'random walk'
            )
        }
    
    return results
```

### 13.8 Hurst Exponent Calculation

```python
def hurst_exponent(prices: pd.Series, 
                   max_lag: int = 100) -> dict:
    """
    Calculate Hurst exponent using R/S analysis.
    
    H > 0.5: Trending (persistent)
    H = 0.5: Random walk
    H < 0.5: Mean-reverting (anti-persistent)
    
    Parameters
    ----------
    prices : pd.Series
        Price series
    max_lag : int
        Maximum lag for analysis
        
    Returns
    -------
    dict
        Hurst exponent and interpretation
    """
    returns = prices.pct_change().dropna()
    
    lags = range(10, max_lag)
    rs_values = []
    
    for lag in lags:
        # Divide into subseries
        n_subseries = len(returns) // lag
        rs_subseries = []
        
        for i in range(n_subseries):
            subseries = returns.iloc[i*lag:(i+1)*lag]
            
            # Mean-adjusted series
            mean_adj = subseries - subseries.mean()
            
            # Cumulative deviations
            cumsum = mean_adj.cumsum()
            
            # Range
            R = cumsum.max() - cumsum.min()
            
            # Standard deviation
            S = subseries.std()
            
            if S > 0:
                rs_subseries.append(R / S)
        
        if rs_subseries:
            rs_values.append((lag, np.mean(rs_subseries)))
    
    # Linear regression in log-log space
    log_lags = np.log([x[0] for x in rs_values])
    log_rs = np.log([x[1] for x in rs_values])
    
    slope, intercept = np.polyfit(log_lags, log_rs, 1)
    
    # Interpretation
    if slope > 0.55:
        interpretation = 'trending (persistent)'
    elif slope < 0.45:
        interpretation = 'mean-reverting (anti-persistent)'
    else:
        interpretation = 'random walk'
    
    return {
        'hurst_exponent': slope,
        'interpretation': interpretation,
        'confidence': 'high' if abs(slope - 0.5) > 0.1 else 'moderate'
    }
```

---

## 14. Illustrative Case Studies

!!! warning "Important Disclaimer"
    The following case studies are **hypothetical illustrations** designed to demonstrate the application of trend-following principles. They are **not** based on actual historical trades or verified backtest results.
    
    **Assumptions:**
    
    - Option prices estimated using Black-Scholes with constant IV
    - Execution at theoretical mid-price (no bid-ask spread)
    - No slippage or market impact
    - No early exercise considerations
    - Simplified Greeks (constant throughout trade)
    
    **Purpose:** Educational demonstration of entry/exit logic, risk management application, and trade lifecycle management.

### 14.1 Illustrative Example A: Successful Breakout Trade

!!! example "Hypothetical Scenario: Tech Stock Uptrend"
    **Setup (Illustrative):**
    
    - Stock: Large-cap tech at \$485
    - Technical picture: Breakout above \$480 resistance
    - ADX: 38 (strong trend)
    - Volume: 2.5x average on breakout day
    - MACD: Histogram expanding positive
    - IV Rank: 35% (favorable)

**Trade Parameters:**

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Entry | \$490 calls, 45 DTE | Slightly OTM for leverage |
| Premium | \$15/contract | Estimated via Black-Scholes |
| Position Size | 4 contracts (\$6,000) | 6% of \$100k portfolio |
| Stop Loss | -50% (\$3,000) | Hard rule |
| Target | \$520 underlying | Next resistance |

**Simulated Evolution:**

| Day | Stock | Estimated Call Value | P/L | Notes |
|-----|-------|---------------------|-----|-------|
| 0 | \$485 | \$15.00 | \$0 | Entry |
| 5 | \$495 | \$18.50 | +\$1,400 | Trend continuing |
| 10 | \$505 | \$23.00 | +\$3,200 | Strong momentum |
| 15 | \$515 | \$28.50 | +\$5,400 | Approaching target |
| 20 | \$522 | \$34.00 | +\$7,600 | Exit at target |

**Outcome:** Entry \$6,000 → Exit \$13,600 = +127% return

**Key Lessons (Illustrated):**

1. Strong entry signals (ADX > 35, volume > 2x) preceded favorable outcome
2. Sufficient DTE (45 days) allowed trend to develop
3. Disciplined exit at target captured gains

### 14.2 Illustrative Example B: Well-Managed Loss

!!! example "Hypothetical Scenario: False Breakout"
    **Setup (Illustrative):**
    
    - Stock: Social media company at \$315
    - Technical picture: Breakout above \$310 resistance
    - ADX: 26 (borderline acceptable)
    - Volume: 1.6x average (moderate)
    - MACD: Positive but not expanding strongly
    - IV Rank: 45% (moderate)

**Trade Parameters:**

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Entry | \$320 calls, 45 DTE | OTM for target |
| Premium | \$9/contract | Estimated |
| Position Size | 4 contracts (\$3,600) | 3.6% of portfolio |
| Stop Loss | -50% (\$1,800) | Hard rule |
| Target | \$335 underlying | Next resistance |

**Simulated Evolution:**

| Day | Stock | Estimated Call Value | P/L | Notes |
|-----|-------|---------------------|-----|-------|
| 0 | \$315 | \$9.00 | \$0 | Entry |
| 2 | \$318 | \$11.00 | +\$800 | Initial move |
| 5 | \$313 | \$7.50 | -\$600 | Pullback |
| 7 | \$308 | \$4.50 | -\$1,800 | **Stop triggered** |

**Outcome:** Entry \$3,600 → Exit \$1,800 = -50% return

**Why This Is a "Good" Loss:**

| Metric | With Stop | Without Stop (Hypothetical) |
|--------|-----------|----------------------------|
| Loss | \$1,800 (50%) | \$3,600 (100%) |
| Capital Preserved | \$1,800 | \$0 |
| Can Trade Again | Yes | No |

**Key Lessons (Illustrated):**

1. Borderline signals (ADX 26, volume 1.6x) indicated higher risk
2. Stop loss honored at -50% preserved capital
3. Quick exit prevented theta decay from compounding losses

### 14.3 Illustrative Example C: Discipline Failure

!!! failure "Hypothetical Scenario: Ignoring Weak Signals"
    **Setup (Illustrative):**
    
    - Stock: EV manufacturer at \$195
    - Technical picture: Above \$190 but ADX only 18 (weak!)
    - Volume: 1.1x average (insufficient confirmation)
    - MACD: Barely positive
    - **Should NOT have traded**

**Mistakes Made:**

1. ❌ ADX < 20 (no trend)
2. ❌ Insufficient volume confirmation
3. ❌ No stop loss set
4. ❌ Short DTE (30 days) for weak setup

**Simulated Evolution:**

| Day | Stock | Estimated Call Value | P/L | Notes |
|-----|-------|---------------------|-----|-------|
| 0 | \$195 | \$7.00 | \$0 | Entry (mistake) |
| 7 | \$188 | \$2.50 | -\$1,350 | Should have stopped |
| 15 | \$187 | \$1.50 | -\$1,650 | Theta accelerating |
| 30 | \$186 | \$0.00 | -\$2,100 | Total loss |

**Outcome:** -100% loss due to multiple discipline failures

**Lessons (Illustrated):**

1. Weak trend signals (ADX < 20) indicate high failure probability
2. Missing stop loss allowed full loss
3. Hope replaced discipline—never let this happen

---

## 15. Common Pitfalls

### 15.1 Trading Weak Trends

**Problem:** Entering positions when ADX < 25 or volume confirmation is absent.

**Consequence:** High failure rate, whipsaw losses, theta decay without trend progress.

**Solution:** Wait for strong signals. No trade is better than a bad trade.

### 15.2 Ignoring Stop Losses

**Problem:** Removing or ignoring predetermined stop losses when position moves against you.

**Consequence:** Small losses become large losses. Single bad trade can devastate account.

**Solution:** Set stops before entry. Make them automatic if possible. Honor them without exception.

### 15.3 Insufficient Time Premium

**Problem:** Buying short-dated options (< 30 DTE) for trends that need time to develop.

**Consequence:** Theta decay outpaces trend progress. Options expire before trend materializes.

**Solution:** Buy 45-60 DTE minimum for moderate trends. Use shorter expirations only for very strong momentum (ADX > 40).

### 15.4 Overtrading

**Problem:** Taking every marginal signal, trading too frequently.

**Consequence:** Transaction costs accumulate. Many small losses. Emotional exhaustion.

**Solution:** Be selective. Wait for high-quality setups. Quality over quantity.

### 15.5 Averaging Down

**Problem:** Adding to losing positions hoping for recovery.

**Consequence:** Concentrating risk in failing trades. Accelerating losses.

**Solution:** Only add to winners (pyramiding). Cut losers quickly.

### 15.6 Ignoring Volatility Regime

**Problem:** Entering when IV rank is high (> 70%), overpaying for options.

**Consequence:** Even if direction is correct, IV crush destroys profits.

**Solution:** Check IV rank before entry. Prefer IV rank < 50%. Use debit spreads when IV is elevated (see §4.6).

### 15.7 Position Sizing Errors

**Problem:** Risking too much on single trades (> 5% of portfolio).

**Consequence:** Single loss significantly impacts portfolio. Emotional decision-making follows.

**Solution:** Keep positions small (2-3% per trade). Scale with track record.

---

## 16. Summary

Trend following with options combines the time-tested momentum anomaly with the asymmetric risk profile of options. Success requires discipline across three dimensions: systematic entry based on confirmed trends with multiple indicator agreement, rigorous risk management through position sizing and stop losses, and Greeks-aware position management throughout the trade lifecycle.

The mathematics of momentum (positive return autocorrelation, Hurst exponents > 0.5) provide the theoretical foundation, while behavioral finance explains why these patterns persist despite being widely known.

!!! success "Key Rules Summary"
    **Entry:**
    
    - ADX > 25, volume confirmation, MACD agreement
    - IV rank < 70% (or use debit spreads)
    - 45-60 DTE minimum
    
    **Position Sizing:**
    
    - 2-3% base allocation
    - Scale with ADX (max 2x)
    - Never exceed 5% per position
    
    **Exit:**
    
    - **-50% stop loss: NO EXCEPTIONS**
    - Take profits at 50-100% gain
    - Exit before final 2 weeks

Most importantly, accept that trend following produces many small losses punctuated by occasional large wins. The strategy's edge comes not from high win rates but from favorable profit factors—letting winners run while cutting losers quickly. Risk management is not about avoiding losses; it's about keeping losses small enough that winners can outweigh them.

The key is capturing the profitable middle portion of trends—not the first 10% (too risky) or the last 10% (reversal danger), but the 60% in between where trend persistence is most reliable.

---

## References

1. Jegadeesh, N., & Titman, S. (1993). Returns to Buying Winners and Selling Losers: Implications for Stock Market Efficiency. *Journal of Finance*, 48(1), 65-91.

2. Asness, C. S., Moskowitz, T. J., & Pedersen, L. H. (2013). Value and Momentum Everywhere. *Journal of Finance*, 68(3), 929-985.

3. Moskowitz, T. J., Ooi, Y. H., & Pedersen, L. H. (2012). Time Series Momentum. *Journal of Financial Economics*, 104(2), 228-250.

4. Hurst, H. E. (1951). Long-term Storage Capacity of Reservoirs. *Transactions of the American Society of Civil Engineers*, 116, 770-799.

5. Lo, A. W., & MacKinlay, A. C. (1988). Stock Market Prices Do Not Follow Random Walks: Evidence from a Simple Specification Test. *Review of Financial Studies*, 1(1), 41-66.

6. Covel, M. (2009). *Trend Following: How to Make a Fortune in Bull, Bear, and Black Swan Markets*. FT Press.

7. Hull, J. C. (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.

8. Daniel, K., & Moskowitz, T. J. (2016). Momentum Crashes. *Journal of Financial Economics*, 122(2), 221-247.

9. Wilder, J. W. (1978). *New Concepts in Technical Trading Systems*. Trend Research.
