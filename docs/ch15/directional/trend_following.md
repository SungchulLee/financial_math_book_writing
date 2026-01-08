# Trend Following

**Trend following** strategies use options to capitalize on established price momentum by entering positions that profit from the continuation of an existing trend, combining directional exposure with controlled risk through strategic strike selection and position sizing.

---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/long_call_payoff.png?raw=true" alt="long_call_payoff" width="400">
</p>

**Figure 1:** Long call payoff diagram showing limited downside risk (premium paid) and unlimited upside potential for trend-following bullish positions.

### 1. Downtrend Put Strategy

**Setup:**

**The fundamental idea:**

- Markets trend: uptrends, downtrends, or sideways

- Trends tend to persist (momentum effect)

- You want to ride the trend, not predict reversals

- Enter when trend is confirmed, not at the beginning

- Use options for leverage and defined risk

- Scale in as trend strengthens, scale out as it weakens

**The key equation:**

$$
\text{Trend Signal} = \text{Price Action} + \text{Volume} + \text{Technical Confirmation}
$$

$$
\text{Position Size} \propto \text{Trend Strength} \times \text{Time Remaining}
$$

**You're essentially betting: "The current trend will continue long enough and strong enough to overcome the premium I'm paying and transaction costs."**

---

## What is Trend Following?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/long_put_payoff.png?raw=true" alt="long_put_payoff" width="400">
</p>

**Figure 2:** Long put payoff diagram showing limited downside risk (premium paid) and substantial upside potential for trend-following bearish positions.

### 1. Trend Following vs. Buy-and-Hold

**Comparison: AAPL uptrend over 60 days**

**Before implementing trend-following option strategies, understand the philosophy:**

### 2. The Trend Following Philosophy

**Core principle:** Don't predict, react. Let the market tell you what's happening, then align with it.

**Key concepts:**

- **Trend identification:** Use technical analysis (moving averages, price patterns, higher highs/higher lows)

- **Confirmation required:** Wait for clear signal, don't jump in early

- **Risk control:** Always know your exit before entry

- **Emotional discipline:** Follow the system mechanically

- **Accept losses:** Many small losses, few big winners

- **Pyramiding:** Add to winners, not losers

### 3. Why Options for Trend Following?

**Traditional trend following uses futures or stocks, but options offer unique advantages:**

**Advantages:**

1. **Defined risk:** Max loss = premium (unlike futures with unlimited loss)

2. **Leverage:** Control large position with small capital

3. **Time efficiency:** Don't need to ride entire trend, capture the "meaty middle"

4. **Flexibility:** Can adjust strikes as trend evolves

5. **Asymmetric payoff:** Limited loss, large profit potential

**Disadvantages:**

1. **Time decay:** Theta works against you

2. **Timing critical:** Enter too early or late = failure

3. **Premium cost:** Need bigger move to breakeven

4. **Illiquidity:** Some options have wide spreads

5. **Assignment risk:** If holding ITM at expiration

### 4. Trend vs. Reversal Trading

**Critical distinction:**

**Trend Following (What We Do):**

- Enter AFTER trend confirmed

- Ride existing momentum

- Exit when trend breaks

- Many small losses, few big wins

- Win rate: 40-50%

- Profit factor: 2-3x

**Reversal Trading (What We DON'T Do):**

- Try to catch tops/bottoms

- Bet against momentum

- High risk (fighting the trend)

- Win rate: Higher (60%+) but small wins

- Profit factor: Often <1x

- **"The trend is your friend until the end"**

---

## Economic

**Understanding the deeper economic logic of trend following:**

### 1. Why Trends Persist

**Markets trend due to systematic behavioral biases:**

1. **Herding:** Investors follow the crowd (FOMO)

2. **Anchoring:** Slow to update beliefs

3. **Confirmation bias:** See what they want to see

4. **Momentum begets momentum:** Winners attract capital

5. **Institutional flows:** Large funds take time to build positions

**The result:**

$$
\text{Price}_t = \text{Price}_{t-1} + \alpha \cdot \text{Trend}_{t-1} + \epsilon_t
$$

Where $\alpha > 0$ indicates **momentum autocorrelation**.

**Translation:** Yesterday's price movement predicts (slightly) today's movement. This is the edge we exploit.

### 2. The Trend Premium

**Trend following earns a premium for bearing specific risks:**

**Risks you bear:**

1. **Trend reversal risk:** Trend suddenly ends

2. **Whipsaw risk:** False breakouts

3. **Theta decay risk:** Paying daily for exposure

4. **Gap risk:** Overnight moves against you

**Why you get paid:**

- Most investors are contrarian (buy low, sell high mentality)

- You provide liquidity during momentum surges

- You help discover fair value through trend

- **Market compensates those willing to ride volatility**

### 3. Options as Trend-Following Derivatives

**An option position in a trend is economically equivalent to:**

$$
\text{Trend Call} = \underbrace{\text{Leveraged Stock}}_{\text{Directional Exposure}} + \underbrace{\text{Trend Filter}}_{\text{Entry Discipline}} + \underbrace{\text{Stop Loss}}_{\text{Premium as Risk Limit}}
$$

**Key insight:** The premium you pay is simultaneously:

- Cost of leverage (like borrowing)

- Cost of limited liability (like insurance)

- Cost of time (theta decay)

- **Net cost of mechanical trend exposure**

**Example: AAPL in confirmed uptrend**

- Stock at $150, trending from $130

- Buy $155 call (slightly OTM) for $5, 60 days to expiration

- You're essentially saying: "I expect this trend to continue, taking AAPL above $160 within 60 days"

**Decomposition:**

$$
\begin{align}
\text{Economic Position} &= \text{Long \$150 of stock (via delta)} \\
&+ \text{Short put protection (limited downside)} \\
&+ \text{Trend confirmation filter (entered at \$150, not \$130)} \\
&+ \text{Time decay cost (\$5 premium)}
\end{align}
$$

---

## Key Terminology

**Trend:**

- Sustained directional movement in price

- Identified by: higher highs & higher lows (uptrend) or lower highs & lower lows (downtrend)

- Confirmed by: volume, moving averages, breakouts

**Momentum:**

- Rate of change in trend

- Strong momentum = steep trend

- Weak momentum = shallow trend or consolidation

**Breakout:**

- Price moves above resistance (uptrend) or below support (downtrend)

- Valid breakout requires volume confirmation

- False breakouts are common (whipsaws)

**Support/Resistance:**

- Support: Price level where buying pressure prevents further decline

- Resistance: Price level where selling pressure prevents further advance

- Key levels for trend confirmation

**Moving Averages:**

- Simple moving average (SMA): Average price over N periods

- Exponential moving average (EMA): Weighted toward recent prices

- Common: 20-day, 50-day, 200-day

- Trend signals: Price above MA = uptrend, below = downtrend

**ADX (Average Directional Index):**

- Measures trend strength (not direction)

- Scale: 0-100

- ADX < 20: Weak trend (consolidation)

- ADX 20-40: Moderate trend

- ADX > 40: Strong trend

- **Use ADX to decide position size**

**MACD (Moving Average Convergence Divergence):**

- Momentum indicator

- Signal line crossover: Bullish (MACD crosses above) or bearish (crosses below)

- Histogram: Strength of momentum

- **Use for entry/exit timing**

**Volume:**

- Number of shares traded

- Confirms trend validity

- Breakout on high volume = reliable

- Trend continuation requires sustained volume

---

## Basic Trend Following Strategies

### 1. Strategy 1

**Setup:**

**Uptrend signal:**

- Price crosses above 50-day MA

- Volume above average

- MACD positive

- → Buy ATM or slightly OTM calls

**Downtrend signal:**

- Price crosses below 50-day MA

- Volume above average

- MACD negative

- → Buy ATM or slightly OTM puts

**Example:**

- MSFT at $350

- Crosses above 50-day MA ($345) on high volume

- Buy $355 call, 45 days out, for $8

- Stop loss: Close if price breaks back below MA

**Parameters:**

- **Entry:** Confirmed crossover + volume

- **Strike:** 1-2 strikes OTM (delta ~0.40-0.50)

- **Expiration:** 45-60 days

- **Exit:** Price breaks back through MA, or 50% profit, or -50% loss

### 2. Strategy 2

**Setup:**

**Resistance breakout:**

- Stock breaks above key resistance

- Volume > 2x average

- ADX > 25 (confirming trend)

- → Buy calls slightly OTM

**Support breakdown:**

- Stock breaks below key support

- Volume > 2x average

- ADX > 25

- → Buy puts slightly OTM

**Example:**

- NVDA at $485, resistance at $480

- Breaks to $487 on 3x volume

- ADX = 32 (strong trend)

- Buy $490 call, 30 days, for $12

- Target: Next resistance at $510

**Parameters:**

- **Entry:** Close above resistance + volume

- **Strike:** 1 strike OTM

- **Expiration:** 30-45 days (shorter for breakouts)

- **Exit:** Next resistance level, or price back below breakout level

### 3. Strategy 3

**Setup:**

**Strong uptrend:**

- Stock in established uptrend (price > 20-day, 50-day, 200-day MAs)

- Pullback to 20-day MA (healthy correction)

- Bounce off MA with volume

- → Buy ATM calls

**Strong downtrend:**

- Stock in established downtrend (price < MAs)

- Rally to 20-day MA (dead cat bounce)

- Rejection at MA with volume

- → Buy ATM puts

**Example:**

- TSLA trending from $200 to $250 over 2 months

- Pulls back to $235 (20-day MA)

- Bounces with volume confirmation

- Buy $240 call, 60 days, for $10

- Anticipating resumption to $260+

**Parameters:**

- **Entry:** Bounce confirmation (1-2 green candles after touching MA)

- **Strike:** ATM for high delta

- **Expiration:** 60-90 days (more time for trend to resume)

- **Exit:** New high achieved, or MA broken

### 4. Strategy 4

**Setup:**

**Strong momentum:**

- ADX crosses above 40 (very strong trend)

- Price making new highs (uptrend) or new lows (downtrend)

- MACD histogram expanding

- → Buy ITM options for high delta

**Example:**

- META at $320, ADX just crossed 45

- Stock up 15% in 3 weeks

- Strong momentum likely to continue near-term

- Buy $315 call (ITM), 30 days, for $18

- Delta = 0.75 (high sensitivity to stock moves)

**Parameters:**

- **Entry:** ADX > 40 + expanding momentum

- **Strike:** ITM for delta > 0.70

- **Expiration:** 30-45 days (momentum trades are shorter)

- **Exit:** ADX drops below 30, or 50% profit

---

## Greeks in Trend Following

**Understanding how Greeks affect trend-following options:**

### 1. Delta

$$
\Delta = \frac{\partial V}{\partial S}
$$

**In trend following:**

- **Higher delta = more direct trend exposure**

- ATM calls/puts: Delta ~0.50 (balanced)

- ITM calls/puts: Delta ~0.70-0.90 (stock-like)

- OTM calls/puts: Delta ~0.20-0.40 (leveraged but risky)

**Strategy implications:**

- **Strong confirmed trend:** Use ITM (high delta) to maximize trend capture

- **Early trend:** Use ATM (medium delta) for balanced risk/reward

- **Speculative trend:** Use OTM (low delta) as lottery ticket

**Example:**

AAPL trending upward:

- Stock moves $150 → $155 (+$5)

- ITM call (delta 0.80): Gains $4

- ATM call (delta 0.50): Gains $2.50

- OTM call (delta 0.30): Gains $1.50

**Trade-off:** Higher delta = higher premium, less leverage.

### 2. Theta

$$
\Theta = \frac{\partial V}{\partial t}
$$

**In trend following:**

- **Theta is your ENEMY**

- Trends take time to develop

- You pay daily for the option

- Must overcome theta + breakeven

**Theta decay curve:**

- Days 60-30: Slow decay (~$0.05-$0.10/day)

- Days 30-10: Moderate decay (~$0.15-$0.25/day)

- Days 10-0: Rapid decay (~$0.30-$0.50/day)

**Strategy implications:**

**For trend following:**

- **Buy 45-60 DTE minimum** (gives trend time to develop)

- **Avoid last 2 weeks** (theta accelerates)

- **Exit if 50% of time elapsed with no progress**

**Example:**

60-day ATM call on MSFT:

- Premium: $10

- Theta: -$0.08/day (first 30 days)

- After 30 days: Lost $2.40 to decay

- Stock must move from $350 → $360 just to breakeven after 30 days

**Critical equation:**

$$
\text{Minimum Required Move} = \frac{\text{Premium} + \text{Theta Decay}}{\text{Delta}}
$$

For call with $10 premium, delta 0.50, theta -$0.10:

- After 10 days: Stock must move $(10 + 1)/(0.50) = $22 just to breakeven

- **Trends must be strong enough to overcome this drag**

### 3. Gamma

$$
\Gamma = \frac{\partial^2 V}{\partial S^2} = \frac{\partial \Delta}{\partial S}
$$

**In trend following:**

- **Gamma helps in strong trends**

- As trend strengthens, your delta increases

- More exposure as you need it

- But also risky on reversals

**Gamma profile:**

- **ATM options:** Highest gamma (delta changes fastest)

- **ITM options:** Low gamma (delta already high, ~0.80-0.90)

- **OTM options:** Low gamma (delta stays low until closer to strike)

**Strategic use:**

**In strong trend:**

1. Start with ATM option (high gamma)

2. As trend develops, delta increases from 0.50 → 0.70

3. You automatically get more exposure

4. **This is favorable for trend following!**

**Example:**

NVDA uptrend:

- Buy $500 ATM call (delta 0.50, gamma 0.03)

- Stock moves to $510: Delta now 0.53

- Stock moves to $520: Delta now 0.56

- Stock moves to $530: Delta now 0.60

- **Your position gains momentum with the trend**

**Danger:**

On reversal:

- Stock at $530, your delta = 0.60

- Reversal to $520: Delta drops to 0.56

- Reversal to $510: Delta drops to 0.53

- **Gamma works AGAINST you on reversals** (this is why stops are critical)

### 4. Vega

$$
\text{Vega} = \frac{\partial V}{\partial \sigma}
$$

**In trend following:**

- Trends often see **increasing volatility** (favorable)

- Breakouts typically increase IV

- You benefit from vega if IV rises

- But post-breakout, IV can collapse

**IV behavior in trends:**

**During breakout:**

- IV increases (uncertainty)

- Your calls/puts gain value from vega

- **This helps your position**

**After trend established:**

- IV often decreases (complacency)

- Your options lose vega value

- **This hurts your position**

**Strategy implications:**

1. **Enter when IV is low-moderate (IV rank < 50%)**

   - Don't overpay for options

   - Leave room for IV expansion during breakout

2. **Be aware of IV crush risk**

   - After earnings

   - After major news

   - After volatility spike

3. **Check IV percentile before entry**

   - IV rank > 70%: Options expensive, avoid

   - IV rank 30-50%: Moderate, acceptable

   - IV rank < 30%: Cheap, favorable

**Example:**

TSLA breakout:

- Before breakout: IV rank = 35%

- Buy $240 call for $10 (IV = 40%)

- During breakout: IV spikes to 55%

- Call gains from stock move AND vega

- New value: $15 ($3 from stock, $2 from vega)

- **Vega boost amplifies trend gain**

---

## Trend Identification Tools

### 1. Moving Average Systems

**Single MA:**

$$
\text{MA}_n = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}
$$

**Rules:**

- Price > MA: Uptrend → Buy calls

- Price < MA: Downtrend → Buy puts

- Price crosses MA: Trend change → Exit

**Common periods:**

- 20-day: Short-term trends

- 50-day: Intermediate trends

- 200-day: Long-term trends

**Dual MA Crossover:**

$$
\text{Signal} = \text{Sign}(\text{MA}_{\text{fast}} - \text{MA}_{\text{slow}})
$$

**Rules:**

- Fast MA crosses above slow MA: Bullish → Buy calls

- Fast MA crosses below slow MA: Bearish → Buy puts

**Common pairs:**

- 20/50: Aggressive

- 50/200: Conservative (golden cross/death cross)

### 2. ADX (Average Directional Index)

**Formula:**

$$
\text{ADX}_t = \text{MA}_{14}\left(\frac{|\text{DI}^+ - \text{DI}^-|}{\text{DI}^+ + \text{DI}^-} \times 100\right)
$$

**Interpretation:**

- ADX < 20: No trend (don't trade)

- ADX 20-25: Weak trend (small positions)

- ADX 25-40: Moderate trend (normal positions)

- ADX > 40: Strong trend (larger positions)

- ADX > 50: Very strong trend (rare, maximize exposure)

**Usage in trend following:**

$$
\text{Position Size} = \text{Base Size} \times \left(\frac{\text{ADX}}{25}\right)
$$

Example:

- Base size = 2% of portfolio

- ADX = 35

- Position size = 2% × (35/25) = 2.8%

### 3. MACD (Moving Average Convergence Divergence)

**Formula:**

$$
\text{MACD} = \text{EMA}_{12} - \text{EMA}_{26}
$$

$$
\text{Signal Line} = \text{EMA}_9(\text{MACD})
$$

$$
\text{Histogram} = \text{MACD} - \text{Signal Line}
$$

**Trading signals:**

- MACD crosses above signal: Bullish → Buy calls

- MACD crosses below signal: Bearish → Buy puts

- Histogram expanding: Momentum increasing (add to position)

- Histogram contracting: Momentum decreasing (consider exit)

**Divergence (advanced):**

- Price makes new high, MACD doesn't: Bearish divergence (trend weakening)

- Price makes new low, MACD doesn't: Bullish divergence (trend reversal possible)

### 4. RSI (Relative Strength Index)

**Formula:**

$$
\text{RSI} = 100 - \frac{100}{1 + \frac{\text{Avg Gain}}{\text{Avg Loss}}}
$$

**In trend following (NOT for overbought/oversold!):**

- **Ignore traditional overbought/oversold levels in strong trends**

- RSI > 70 in uptrend: Trend is strong (not a sell signal!)

- RSI < 30 in downtrend: Trend is strong (not a buy signal!)

**Useful signals:**

- RSI breaks above 50 from below: Momentum shift bullish

- RSI breaks below 50 from above: Momentum shift bearish

### 5. Volume Analysis

**Volume confirmation:**

$$
\text{Volume Ratio} = \frac{\text{Volume}_{\text{today}}}{\text{Avg Volume}_{20\text{-day}}}
$$

**Rules:**

- Volume ratio > 1.5: Strong confirmation

- Volume ratio > 2.0: Very strong confirmation

- Volume ratio < 1.0: Weak signal (be cautious)

**Breakout volume rule:**

$$
\text{Valid Breakout} = (\text{Price} > \text{Resistance}) \land (\text{Volume Ratio} > 1.5)
$$

---

## Trend Following Payoff Diagrams

### 1. Uptrend Call Strategy

**Setup:**

- Stock at $100, trending upward

- Buy $105 call for $4, 60 days

- Entry: Confirmed breakout above $100

**Payoff at expiration:**

$$
\text{Profit} = \max(S_T - 105, 0) - 4
$$

| Stock Price at Expiry ($S_T$) | Option Value | Profit/Loss | Return |
|-------------------------------|--------------|-------------|---------|
| $90 | $0 | -$4 | -100% |
| $100 | $0 | -$4 | -100% |
| $105 | $0 | -$4 | -100% |
| $109 | $4 | $0 | 0% |
| $115 | $10 | +$6 | +150% |
| $125 | $20 | +$16 | +400% |
| $135 | $30 | +$26 | +650% |

**Key points:**

- Breakeven: $105 + $4 = $109

- Max loss: $4 (100% of premium)

- Max profit: Unlimited

- Risk/reward: $4 risk for unlimited upside

- Stock at $100, trending downward

- Buy $95 put for $3, 60 days

- Entry: Confirmed breakdown below $100

**Payoff at expiration:**

$$
\text{Profit} = \max(95 - S_T, 0) - 3
$$

| Stock Price at Expiry ($S_T$) | Option Value | Profit/Loss | Return |
|-------------------------------|--------------|-------------|---------|
| $110 | $0 | -$3 | -100% |
| $100 | $0 | -$3 | -100% |
| $95 | $0 | -$3 | -100% |
| $92 | $3 | $0 | 0% |
| $85 | $10 | +$7 | +233% |
| $75 | $20 | +$17 | +567% |
| $65 | $30 | +$27 | +900% |

**Key points:**

- Breakeven: $95 - $3 = $92

- Max loss: $3 (100% of premium)

- Max profit: $92 (if stock → $0)

- Risk/reward: $3 risk for $92 maximum gain


**Scenario A: Buy stock**

- Buy 100 shares at $150: Cost $15,000

- Stock rises to $165: Profit $1,500 (10%)

- Stock falls to $140: Loss $1,000 (-6.7%)

**Scenario B: Buy calls (trend following)**

- Buy 3 contracts of $155 call at $5: Cost $1,500

- Stock rises to $165: Calls worth $10 → Profit $1,500 (100%)

- Stock falls to $140: Calls worthless → Loss $1,500 (-100%)

**Analysis:**

- **Same upside profit:** Both made $1,500

- **Capital requirement:** Options used 10% of stock capital

- **Downside:** Stock lost $1,000, options lost $1,500 (but as % of capital: -6.7% vs. -10%)

- **Leverage:** Options provided 10:1 effective leverage

- **Time sensitivity:** Stock can hold forever, options expire in 60 days

---

## Real-World Trend Following Examples

### 1. Pension Duration Cut via Futures

**Setup:**

- **Stock:** NVDA

- **Date:** January 2, 2025

- **Price:** $485

- **Technical setup:**

  - Breaking above $480 resistance (previous high)

  - 50-day MA = $460, price well above

  - ADX = 38 (strong trend)

  - Volume 2.5x average on breakout day

  - MACD histogram expanding positive

**Trade execution:**

- **Entry:** Buy $490 calls, 45 DTE, at $15

- **Contracts:** 4 contracts = $6,000 total cost

- **Stop loss:** Close if price breaks back below $475

- **Target:** $520 (next resistance level)

**Trade evolution:**

| Day | Stock Price | Call Value | P/L | Notes |
|-----|-------------|------------|-----|-------|
| 0 | $485 | $15.00 | $0 | Entry on breakout |
| 5 | $495 | $18.50 | +$1,400 | Trend continuing |
| 10 | $505 | $23.00 | +$3,200 | Strong momentum |
| 15 | $515 | $28.50 | +$5,400 | Approaching target |
| 20 | $522 | $34.00 | +$7,600 | **Exit at target** |

**Final result:**

- **Entry:** $6,000

- **Exit:** $13,600

- **Profit:** $7,600 (127% return)

- **Time held:** 20 days

- **Stock move:** $485 → $522 (+7.6%)

- **Option leverage:** 127% / 7.6% = 16.7x

**Why it worked:**

1. Clear breakout on high volume

2. Strong trend confirmed by ADX

3. Momentum expanding (MACD)

4. Gave it time (45 DTE, not weekly)

5. Had clear target and exit discipline

6. Trend was strong enough to overcome theta decay

### 2. Transition Risk Hedge

**Setup:**

- **Stock:** JPM (bank stock)

- **Date:** March 10, 2025

- **Price:** $152

- **Technical setup:**

  - Breaking below $155 support (banking sector stress)

  - 20/50 death cross (20-day MA crossed below 50-day)

  - ADX = 29 (moderate trend building)

  - Volume 1.8x average on breakdown

  - RSI crossed below 50

**Trade execution:**

- **Entry:** Buy $148 puts, 60 DTE, at $4

- **Contracts:** 5 contracts = $2,000 total cost

- **Stop loss:** Close if price reclaims $155

- **Target:** $135 (next support level)

**Trade evolution:**

| Day | Stock Price | Put Value | P/L | Notes |
|-----|-------------|-----------|-----|-------|
| 0 | $152 | $4.00 | $0 | Entry on breakdown |
| 7 | $148 | $6.50 | +$1,250 | Downtrend accelerating |
| 14 | $143 | $9.50 | +$2,750 | Banking fears spreading |
| 21 | $138 | $13.00 | +$4,500 | Near target |
| 28 | $136 | $14.50 | +$5,250 | **Exit near target** |

**Final result:**

- **Entry:** $2,000

- **Exit:** $7,250

- **Profit:** $5,250 (263% return)

- **Time held:** 28 days

- **Stock move:** $152 → $136 (-10.5%)

- **Option leverage:** 263% / 10.5% = 25x

**Why it worked:**

1. Clear breakdown below support

2. Death cross confirmed trend reversal

3. Sector-wide catalyst (banking stress)

4. Sufficient time (60 DTE)

5. Trend strong enough to reach target

6. Didn't get greedy, exited near target

### 3. Portable Alpha with Futures

**Setup:**

- **Stock:** TSLA

- **Date:** February 15, 2025

- **Price:** $195

- **Technical setup:**

  - Breaking above $190 resistance

  - BUT: ADX = 18 (weak trend!)

  - Volume only 1.1x average (weak confirmation)

  - MACD barely positive

  - **Should NOT have traded (weak signals)**

**Trade execution:**

- **Entry:** Buy $200 calls, 30 DTE, at $7

- **Contracts:** 3 contracts = $2,100 total cost

- **Stop loss:** Should be $190, but didn't set one!

- **Target:** $210 (overly optimistic)

**Trade evolution:**

| Day | Stock Price | Call Value | P/L | Notes |
|-----|-------------|------------|-----|-------|
| 0 | $195 | $7.00 | $0 | Entry (mistake!) |
| 2 | $198 | $9.00 | +$600 | Brief momentum |
| 4 | $193 | $5.00 | -$600 | Whipsaw down |
| 7 | $188 | $2.50 | -$1,350 | Trend failed |
| 10 | $190 | $3.00 | -$1,200 | Weak bounce |
| 15 | $187 | $1.50 | -$1,650 | Should exit! |
| 20 | $185 | $0.50 | -$1,950 | Stubbornly holding |
| 25 | $188 | $1.00 | -$1,800 | False hope |
| 30 | $186 | $0.00 | -$2,100 | **Total loss** |

**Final result:**

- **Entry:** $2,100

- **Exit:** $0

- **Loss:** -$2,100 (-100%)

- **Stock move:** $195 → $186 (-4.6%)

- **Mistakes:** Ignored weak signals, no stop loss, hope trading

**Why it failed:**

1. **Weak trend signals (ADX < 20)**

2. **Low volume confirmation**

3. **No stop loss discipline**

4. **Held through reversal hoping for recovery**

5. **Too short expiration for weak trend**

6. **Let theta decay eat entire position**

**Lessons:**

- Don't trade weak trends (ADX < 20)

- Always set and respect stop losses

- Accept losses early (should have exited at -50%)

- Volume confirmation is critical

- Hope is not a strategy

### 4. Tactical Duration Extension

**Setup:**

- **Stock:** META

- **Date:** April 5, 2025

- **Price:** $315

- **Technical setup:**

  - Breaking above $310 resistance

  - ADX = 26 (acceptable)

  - Volume 1.6x average (moderate)

  - MACD positive

  - **Looked good, but turned out to be false breakout**

**Trade execution:**

- **Entry:** Buy $320 calls, 45 DTE, at $9

- **Contracts:** 4 contracts = $3,600 total cost

- **Stop loss:** Exit if stock closes below $310 (proper risk management!)

- **Target:** $335

**Trade evolution:**

| Day | Stock Price | Call Value | P/L | Notes |
|-----|-------------|------------|-----|-------|
| 0 | $315 | $9.00 | $0 | Entry on breakout |
| 2 | $318 | $11.00 | +$800 | Looking good |
| 5 | $313 | $7.50 | -$600 | Pulling back |
| 7 | $308 | $4.50 | -$1,800 | **Stop triggered!** |

**Final result:**

- **Entry:** $3,600

- **Exit:** $1,800

- **Loss:** -$1,800 (-50%)

- **Time held:** 7 days

- **Stock move:** $315 → $308 (-2.2%)

**Why it's a GOOD loss:**

1. **Recognized false breakout quickly**

2. **Honored stop loss at -50%**

3. **Preserved 50% of capital**

4. **Can trade again with remaining capital**

5. **Didn't let it go to zero**

**Without stop loss:** Would have watched calls decay to $0 (100% loss) as stock drifted to $300 over next 30 days.

**Comparison:**

| With Stop Loss | Without Stop Loss |
|----------------|-------------------|
| Loss: $1,800 (50%) | Loss: $3,600 (100%) |
| Remaining capital: $1,800 | Remaining capital: $0 |
| Can make next trade | Out of capital |
| Psychological damage: Moderate | Psychological damage: Severe |

**This is why stop losses are MANDATORY in trend following!**

---

## Strike Selection for Trend Following

### 1. ITM (In-the-Money)

**Characteristics:**

- Delta: 0.70-0.85

- Expensive premium

- Lower leverage

- More like stock ownership

- Less theta decay (relative to value)

**When to use:**

- Very strong trend (ADX > 40)

- Want stock-like exposure with defined risk

- Have larger capital

- Conservative approach

**Example:**

Stock at $100, strong uptrend:

- Buy $95 call (ITM) for $8

- Delta = 0.80

- If stock → $110, call → $16 (doubles)

- If stock → $95, call → $2 (75% loss, but retains intrinsic value)

**Pros:**

- High delta (captures most of stock move)

- Less sensitive to IV changes

- Retains value better if trend slows

**Cons:**

- Expensive (requires more capital)

- Lower leverage

- Higher dollar loss if wrong

### 2. ATM (At-the-Money)

**Characteristics:**

- Delta: 0.45-0.55

- Moderate premium

- Balanced leverage

- Highest gamma

- Moderate theta decay

**When to use:**

- Moderate trend (ADX 25-40)

- Standard approach

- Most common choice

- Good risk/reward balance

**Example:**

Stock at $100, confirmed trend:

- Buy $100 call (ATM) for $5

- Delta = 0.50

- If stock → $110, call → $11 (120% gain)

- If stock → $95, call → $1 (80% loss)

**Pros:**

- Balanced cost and leverage

- High gamma (delta increases with trend)

- Reasonable theta decay

- Most liquid (tightest spreads)

**Cons:**

- Still significant theta decay

- Can lose quickly if wrong

- Needs decent move to profit

### 3. OTM (Out-of-the-Money)

**Characteristics:**

- Delta: 0.20-0.40

- Cheap premium

- High leverage

- Lower gamma

- High theta decay (as % of value)

**When to use:**

- Strong breakout expected (ADX > 35)

- Limited capital

- Aggressive speculation

- High conviction, short-term play

**Example:**

Stock at $100, breakout setup:

- Buy $105 call (OTM) for $2

- Delta = 0.30

- If stock → $115, call → $11 (450% gain)

- If stock → $100, call → $0.50 (75% loss)

**Pros:**

- Cheap (can buy more contracts)

- Huge leverage if right

- Small dollar loss if wrong

**Cons:**

- Low delta (captures less of move)

- High theta decay (as % of value)

- Needs big move to profit

- Often expires worthless

### 4. Strike Selection Decision Framework

**Based on trend strength (ADX):**

$$
\text{Strike Selection} = 
\begin{cases}
\text{ITM} & \text{if ADX} > 40 \text{ (strong trend)} \\
\text{ATM} & \text{if } 25 < \text{ADX} < 40 \text{ (moderate trend)} \\
\text{Avoid} & \text{if ADX} < 25 \text{ (weak trend)}
\end{cases}
$$

**Based on capital available:**

| Capital for Trade | Strike Choice | Reasoning |
|-------------------|---------------|-----------|
| $5,000+ | ITM | Can afford higher premium |
| $2,000-$5,000 | ATM | Standard approach |
| $500-$2,000 | OTM | Limited capital, higher risk |
| <$500 | Wait | Too small for proper risk management |

**Based on conviction level:**

| Conviction | Strike Choice | Position Size |
|------------|---------------|---------------|
| Very high | ITM | Larger position |
| High | ATM | Normal position |
| Moderate | ATM or OTM | Smaller position |
| Low | Don't trade | Wait for better setup |

---

## Time Selection for Trend Following

### 1. Short-term (< 30 DTE)

**Characteristics:**

- Cheap premium

- High theta decay

- Need quick move

- High risk

**When to use:**

- Strong momentum breakout (ADX > 40)

- Short-term catalyst (news event)

- Day trading or swing trading

- Have high conviction

**Pros:**

- Low cost

- High leverage

- Can catch explosive moves

**Cons:**

- Very fast theta decay

- No time for trend to develop

- High probability of total loss

- Stressful to manage

**Example:**

- TSLA breakout on delivery numbers

- Stock at $200, buy $205 call, 14 DTE, for $3

- If delivery beats expectations → stock to $220 in 1 week

- But if neutral or miss → call worthless in 2 weeks

**Recommendation:** Only for experienced traders with strong technical analysis skills.

### 2. Medium-term (30-60 DTE)

**Characteristics:**

- Moderate premium

- Balanced theta decay

- Time for trend to develop

- Good risk/reward

**When to use:**

- Confirmed trend (ADX > 25)

- Standard approach

- Most recommended timeframe

- Gives trend time to work

**Pros:**

- Reasonable theta decay

- Time for pullbacks and consolidation

- Can manage position actively

- Multiple exit opportunities

**Cons:**

- More expensive than short-term

- Still need trend to move fairly quickly

- Theta still significant

**Example:**

- NVDA in uptrend, ADX = 32

- Stock at $500, buy $510 call, 45 DTE, for $15

- Trend continues to $540 over 30 days

- Exit at $32 for 113% profit

**Recommendation:** This is the sweet spot for trend following. Start here.

### 3. Long-term (60+ DTE, LEAPS)

**Characteristics:**

- Expensive premium

- Slow theta decay

- Time for major trend

- Stock substitute

**When to use:**

- Very strong long-term trend

- Large capital available

- Want exposure without tying up stock capital

- Multi-month or year-long view

**Pros:**

- Low theta decay (daily)

- Time for major trends

- Can weather pullbacks

- Almost like owning stock

**Cons:**

- Very expensive

- Ties up capital

- Still has expiration (unlike stock)

- Lower leverage

**Example:**

- AAPL long-term uptrend

- Stock at $150, buy $140 LEAPS call (12 months), for $25

- Delta = 0.75 (stock-like)

- Trend continues to $180 over 8 months

- Exit at $45 for 80% profit (stock gained 20%)

**Recommendation:** Good for strong trends with patient capital. Use as stock substitute with defined risk.

### 4. Time Selection Framework

**Based on trend maturity:**

| Trend Stage | DTE Choice | Reasoning |
|-------------|------------|-----------|
| Early breakout | 30-45 DTE | Need time to develop |
| Mid-trend | 45-60 DTE | Standard |
| Late trend | < 30 DTE | Momentum play, don't overpay |
| Multi-month trend | 90+ DTE (LEAPS) | Long-term position |

**Based on ADX (trend strength):**

$$
\text{Minimum DTE} = 
\begin{cases}
30 & \text{if ADX} > 40 \text{ (strong, can use shorter)} \\
45 & \text{if } 30 < \text{ADX} < 40 \text{ (moderate)} \\
60 & \text{if } 25 < \text{ADX} < 30 \text{ (weak, need more time)}
\end{cases}
$$

---

## Entry and Exit Rules

### 1. Entry Checklist

**Must have ALL of the following:**

1. **Trend confirmation:**

   - [ ] Price above/below key MA (20/50/200-day)

   - [ ] ADX > 25

   - [ ] MACD in agreement with direction

2. **Volume confirmation:**

   - [ ] Breakout on >1.5x average volume

   - [ ] OR sustained volume on trend continuation

3. **Technical setup:**

   - [ ] Clear support/resistance levels identified

   - [ ] Breakout above resistance (calls) or below support (puts)

   - [ ] No immediate overhead resistance (calls) or support (puts)

4. **Options conditions:**

   - [ ] IV rank < 70% (not overpaying)

   - [ ] Sufficient liquidity (bid-ask spread < 10% of mid)

   - [ ] Appropriate time (45-60 DTE minimum)

   - [ ] Appropriate strike (ATM or slightly OTM)

5. **Risk management:**

   - [ ] Position size = 2-5% of portfolio max

   - [ ] Stop loss level identified (price or %)

   - [ ] Profit target identified

   - [ ] Max loss acceptable psychologically

**If ANY checkbox not checked → DON'T TRADE!**

### 2. Exit Rules (Must Have All Three Types)

**Type 1: Stop Loss Exits (Prevent Disaster)**

1. **Price-based stop:**

   - Stock closes below entry breakout level

   - Example: Bought call on break of $100, exit if close below $98

2. **Percentage stop:**

   - Option loses 50% of value

   - **Hard rule: Exit at -50%, no exceptions**

3. **Technical stop:**

   - ADX drops below 20 (trend dead)

   - Price crosses back below MA

   - Volume dries up

**Type 2: Profit Taking Exits (Lock in Gains)**

1. **Target price:**

   - Stock reaches identified resistance/support

   - Example: Target $120, exit when hit

2. **Percentage target:**

   - Option gains 50-100%

   - Scale out: Exit half at +50%, let rest run with trailing stop

3. **Risk/reward target:**

   - Made 2x or 3x initial risk

   - Example: Risked $500, exit when profit = $1,000-$1,500

**Type 3: Time Exits (Avoid Theta Trap)**

1. **Time-based:**

   - 50% of time elapsed with <25% progress → exit

   - Entering last 2 weeks → exit unless deep ITM

2. **Theta acceleration:**

   - Daily theta > $0.20 per contract → too expensive to hold

3. **Expiration proximity:**

   - 10 days before expiration → exit all positions regardless

### 3. Systematic Exit Framework

**Exit decision tree (check in this order):**

```

1. Is option down 50%?
   → YES: EXIT IMMEDIATELY (stop loss)
   → NO: Continue to #2

2. Has profit target been hit?
   → YES: EXIT (full or partial)
   → NO: Continue to #3

3. Has stop loss been triggered (price or technical)?
   → YES: EXIT IMMEDIATELY
   → NO: Continue to #4

4. Has 50% of time elapsed?
   → YES: Is profit at least 25%?
      → NO: EXIT (time stop)
      → YES: Continue to hold with trailing stop
   → NO: Continue to hold

5. Are you within 10 days of expiration?
   → YES: EXIT (theta too high)
   → NO: Continue to hold
```

### 4. Position Sizing Formula

**Conservative approach (recommended):**

$$
\text{Position Size} = \min\left(\frac{0.02 \times \text{Portfolio}}{\text{Premium per Contract}}, \frac{0.05 \times \text{Portfolio}}{\text{Premium per Contract}}\right)
$$

Where:

- 2% of portfolio per position (very conservative)

- 5% of portfolio maximum per position (aggressive)

**Example:**

Portfolio = $50,000
Premium per contract = $500

Conservative: (0.02 × $50,000) / $500 = 2 contracts
Aggressive: (0.05 × $50,000) / $500 = 5 contracts

**Start with 2 contracts, increase to 5 only with proven track record.**

### 5. Scaling In/Out Strategy

**Scaling in (adding to winners):**

**Rule:** Only add if trade profitable AND trend strengthening.

Example:

- Initial: Buy 2 ATM calls at $100

- Stock moves to $105 (+5%): Add 1 more call

- Stock moves to $110 (+10%): Add 1 more call

- Total: 4 contracts, average entry ~$102

**Scaling out (taking profits):**

**Rule:** Take partial profits at targets, let rest run.

Example:

- Own 4 contracts, profit target $120

- Stock hits $115: Sell 2 contracts (50% off)

- Stock hits $120: Sell 1 contract (25% off)

- Let final contract run with trailing stop

**Never scale in to losers!** This is averaging down = capital destruction.

---



## Final Wisdom

> "The trend is your friend, but only if you follow it with discipline. Trend following with options is NOT about predicting the future—it's about reacting to the present and managing risk ruthlessly. Most traders fail not because they can't identify trends, but because they lack the discipline to exit losing trades and the patience to let winners run. Master these two skills, and you'll be in the top 10% of options traders."

**Keys to success:**

1. **Wait for strong signals** (ADX > 25, volume confirmation)

2. **Size positions conservatively** (2-5% max)

3. **Always use stop losses** (-50% rule)

4. **Take profits systematically** (scale out at targets)

5. **Accept losses gracefully** (many small losses are normal)

6. **Let winners run** (with trailing stops)

7. **Never revenge trade** (emotion is the enemy)

8. **Track your statistics** (know your win rate and profit factor)

**Most important lesson:** Trend following works because trends persist longer than most people expect. But they also reverse faster than you think. The key is catching the middle 60% of the trend, not the first 10% or last 10%. Enter late with confirmation, exit early with profits. This is the path to consistent profitability.

**Remember:** 80% of your profits will come from 20% of your trades. Your job is to survive the other 80% with small losses so you can capture the big winners. Risk management is not about avoiding losses—it's about keeping losses small enough that winners can outweigh them. 🎯📈