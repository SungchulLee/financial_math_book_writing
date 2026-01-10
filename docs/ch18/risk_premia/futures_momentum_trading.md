# Futures Momentum

**Futures momentum strategies** are systematic trading approaches that exploit the empirically-validated tendency for assets with strong recent performance to continue outperforming (or underperforming) in the near future, capturing persistent trends across diversified futures markets while harvesting risk premia through rules-based position sizing and disciplined rebalancing.

---

## The Core Insight

**The fundamental idea:**

- Past returns predict future returns (momentum anomaly)
- "Winners keep winning, losers keep losing" (for 3-12 months)
- Academically validated across 100+ years of data
- Works across all asset classes (commodities, equities, bonds, FX)
- Behavioral biases create persistent mispricing
- Information diffusion is slow and gradual
- Systematic approach captures risk premium
- Diversification across markets reduces risk
- Rebalancing disciplines entry/exit

**The key equations:**

$$
\text{Momentum Signal}_t = \text{Return}_{t-12, t-1} = \frac{P_{t-1} - P_{t-12}}{P_{t-12}}
$$

$$
\text{Position}_t = \text{sign}(\text{Signal}_t) \times \text{Vol Target}
$$

$$
\text{Portfolio Return}_t = \sum_{i=1}^{N} w_i \times r_i
$$

**You're essentially betting: "Assets that have risen over the past 1-12 months will continue rising over the next 1-3 months, and assets that have fallen will continue falling, allowing me to systematically capture this persistent trend-following premium across diversified futures markets."**

---

## What Is Futures

**Before trading momentum, understand the fundamental mechanics:**

### 1. Academic

**Seminal research:**

**Jegadeesh and Titman (1993):**
- Studied equity momentum
- Buy past winners, sell past losers
- 12-month formation, 1-month hold
- **Profitable strategy for 30+ years**

**Moskowitz, Ooi, and Pedersen (2012):**
- "Time Series Momentum Everywhere"
- Tested 58 futures markets (1985-2009)
- Commodities, equities, bonds, FX
- **Momentum works across ALL asset classes**

**Key findings:**

$$
\text{Sharpe Ratio} = 0.77 \quad \text{(exceptional!)}
$$

- Works in 100+ years of data
- Robust across markets
- Low correlation to equities
- **Persistent risk premium**

### 2. Time-Series vs

**Two distinct approaches:**

**Time-Series Momentum (TSMOM):**

$$
\text{Signal}_i = \text{sign}(\text{Return}_{i,t-12,t-1})
$$

- Compare each asset to its own past
- Long if up, short if down
- Absolute momentum
- **"Trend following"**

**Example:**
- Crude oil: +15% last 12 months → Long
- Gold: -8% last 12 months → Short
- **Independent decisions**

**Cross-Sectional Momentum (XSMOM):**

$$
\text{Signal}_i = \text{Rank}(\text{Return}_{i,t-12,t-1})
$$

- Compare assets to each other
- Long top quintile, short bottom quintile
- Relative momentum
- **"Relative strength"**

**Example:**
- Crude oil: +15% (top 20%) → Long
- Gold: -8% (bottom 20%) → Short
- Nat gas: +5% (middle) → Neutral
- **Relative ranking**

**Which is better?**

| Feature | Time-Series | Cross-Sectional |
|---------|-------------|-----------------|
| Sharpe Ratio | 0.77 | 0.55 |
| Capacity | Higher | Lower |
| Simplicity | Higher | Lower |
| Research | Stronger | Weaker |

**Recommendation: Time-series momentum (TSMOM) for most traders**

### 3. Standard TSMOM

**Classic specification:**

**1. Signal calculation:**

$$
r_{i,t-12,t-1} = \frac{P_{i,t-1} - P_{i,t-12}}{P_{i,t-12}}
$$

- Use 12-month lookback (standard)
- Skip most recent month (t-2 to t-1)
- **12-1 month momentum**

**2. Position sizing:**

$$
w_i = \frac{\text{sign}(r_i)}{\sigma_i} \times \text{Vol Target}
$$

Where:
- $\text{sign}(r_i) = +1$ if $r_i > 0$, else $-1$
- $\sigma_i$ = volatility of asset $i$
- Vol Target = target portfolio volatility (10-15%)

**3. Rebalancing:**

$$
\text{Rebalance monthly (end of month)}
$$

**Example:**

**Crude oil (month-end):**
- Price 12 months ago: $65/barrel
- Price today: $75/barrel
- Return: (75-65)/65 = **+15.4%**
- Signal: **Long** (positive momentum)
- Vol: 35% annualized
- Position: $\frac{+1}{0.35} \times 0.12 = 0.343$ (34.3% of portfolio)

**Natural gas:**
- 12-month return: **-22%**
- Signal: **Short** (negative momentum)
- Vol: 60%
- Position: $\frac{-1}{0.60} \times 0.12 = -0.20$ (short 20%)

### 4. Why Momentum

**Academic explanations:**

**1. Behavioral biases:**

**Underreaction:**
- Investors slow to incorporate news
- Information diffuses gradually
- Prices adjust with lag
- **Creates trends**

**Herding:**
- Investors follow each other
- Reinforces trends
- Momentum begets momentum
- **Self-fulfilling**

**Disposition effect:**
- Investors hold losers too long
- Sell winners too early
- Prolongs trends
- **Behavioral persistence**

**2. Risk-based explanations:**

**Time-varying risk premia:**
- Momentum = compensation for risk
- Drawdowns during crises
- Crash risk embedded
- **Risk premium harvest**

**Funding liquidity:**
- Momentum requires capital
- Capital constraints slow arbitrage
- Limits to arbitrage
- **Structural edge**

**3. Structural forces:**

**Commodity producers:**
- Gradual supply response
- Cannot adjust instantly
- Creates persistence
- **Physical constraints**

**Central banks:**
- Policy changes gradual
- Forward guidance
- Creates bond/FX trends
- **Institutional inertia**

### 5. Historical

**Moskowitz et al. (2012) results:**

**1985-2009 (25 years):**

$$
\text{Annual Return} = 14.9\%
$$

$$
\text{Volatility} = 12.0\%
$$

$$
\text{Sharpe Ratio} = 1.24
$$

**Even better: 1965-2009 (45 years):**

$$
\text{Sharpe Ratio} = 0.77
$$

**Crisis performance:**

- 2008 financial crisis: +16% (positive!)
- 1987 crash: +8%
- 1998 LTCM: +12%
- **Crisis hedge properties**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/futures_momentum.png?raw=true" alt="futures_momentum" width="700">
</p>
**Figure 1:** Futures momentum strategy showing time-series momentum signals across multiple markets, volatility-weighted position sizing, and monthly rebalancing. The strategy captures persistent trends in commodities, equities, bonds, and currencies while maintaining diversification across uncorrelated markets, generating consistent risk-adjusted returns with low correlation to traditional equity portfolios.

---

## Economic

**Beyond the signals, understanding the economic rationale:**

### 1. Momentum as

**The deep insight:**

Momentum strategies earn positive returns on average but suffer **catastrophic drawdowns** during rapid reversals. Investors demand compensation for bearing this tail risk.

**Formal representation:**

$$
\mathbb{E}[R_{\text{momentum}}] = r_f + \beta_{\text{crash}} \times \lambda_{\text{crash}}
$$

Where:
- $\beta_{\text{crash}}$ = exposure to crash risk
- $\lambda_{\text{crash}}$ = crash risk premium

**Empirical evidence:**

**Normal months (95%):**
- Average return: +1.5%
- Low volatility
- **Steady profits**

**Crisis months (5%):**
- Average return: -15%
- High volatility
- **Devastating drawdowns**

**Example: 2009 Momentum Crash**

**March-April 2009:**
- Markets reversed violently
- Losers became winners overnight
- Momentum strategies: -30% in 2 months
- **Worst drawdown in history**

**Why crash happened:**

- Extreme pessimism → capitulation
- Central bank intervention
- Massive short covering
- Reversal in ALL assets
- **Coordinated unwind**

**This crash risk = reason for risk premium:**

$$
\text{Annual Return} = 14.9\% = \text{Compensation for occasional crashes}
$$

### 2. Information

**Academic model (Hong and Stein, 1999):**

**Gradual information diffusion:**

$$
P_t = P_{t-1} + \alpha \times \text{News}_t + \epsilon_t
$$

Where $\alpha < 1$ (incomplete incorporation)

**Information spreads slowly:**

- Day 1: 20% of investors learn news
- Week 1: 40% know
- Month 1: 70% know
- Month 3: 95% know
- **Gradual price adjustment**

**Creates momentum:**

- Initial underreaction
- Slow incorporation over months
- Trend persists 3-12 months
- **Predictable continuation**

**Example: OPEC Production Cut**

**Announcement (Day 0):**
- OPEC cuts 1M barrels/day
- Crude oil: +5% (initial reaction)
- **Underreaction**

**Month 1:**
- Analysts revise forecasts
- Funds rebalance portfolios
- Crude: +8% (cumulative +13%)
- **Gradual incorporation**

**Month 3:**
- Supply actually tightening
- Inventories declining
- Crude: +12% (cumulative +25%)
- **Full incorporation**

**Momentum captured this 3-month drift:**
- Entry (Month 1): $70/barrel
- Exit (Month 3): $78/barrel
- Profit: +11.4%
- **Trend following**

### 3. Momentum vs Mean

**Critical distinction:**

$$
\text{Momentum} = \text{Persistence over 1-12 months}
$$

$$
\text{Mean Reversion} = \text{Reversal over 1-5 years}
$$

**Time-scale diagram:**

| Horizon | Pattern | Strategy |
|---------|---------|----------|
| 1 day | Reversal | Intraday mean reversion |
| 1 week | Weak momentum | Skip (noise) |
| 1-12 months | **Strong momentum** | **TSMOM** |
| 1-3 years | Weak reversal | Skip |
| 3-5 years | **Mean reversion** | **Long-term contrarian** |

**Why both exist:**

**Short-term (1-12 months):**
- Underreaction dominates
- Information diffusion
- **Momentum wins**

**Long-term (3-5 years):**
- Overreaction dominates
- Valuation matters
- **Mean reversion wins**

**Example: Crude oil 2014-2020**

**2014-2015 (Momentum phase):**
- Oil falling: $100 → $50
- Momentum signal: Short
- Worked: Fell to $30
- **12-month momentum profitable**

**2016-2020 (Mean reversion phase):**
- Oil at $30 (cheap)
- Momentum signal: Still short
- But rebounded: $30 → $70
- **Long-term mean reversion**

**Lesson: Momentum and mean reversion coexist at different time scales!**

### 4. Commodity

**Commodity-specific driver:**

$$
\text{Supply Response Time} = 1\text{-}3 \text{ years}
$$

**Example: Crude oil supply shock**

**Year 0: Demand surge**
- China economy booming
- Oil demand +5%/year
- Prices rise: $60 → $80
- **Shortage developing**

**Year 1: High prices persist**
- Producers plan capex
- Exploration budgets increase
- But NO new supply yet (drilling takes time)
- Prices: $80 → $100
- **Momentum continues**

**Year 2: Supply starts responding**
- New wells coming online
- Shale production ramping
- Supply +3%
- Prices stabilize: $100 → $95
- **Momentum weakens**

**Year 3: Oversupply**
- Too much supply now
- Prices crash: $95 → $60
- **Mean reversion**

**Momentum profitable in Years 0-2:**
- Slow supply response
- Trends persist
- **Structural edge**

### 5. Currency Momentum

**FX momentum driven by carry:**

**High interest rate currency:**
- Attracts capital flows
- Appreciates
- Momentum reinforces
- **Self-reinforcing cycle**

**Example: Australian Dollar (AUD) 2003-2007**

**2003: Rates diverge**
- AUD rate: 5.5%
- USD rate: 1.0%
- Carry: +4.5%
- **Attractive**

**2003-2007: Carry trade inflows**
- Investors buy AUD (high yield)
- AUD appreciates: 0.60 → 0.95 vs USD (+58%)
- More investors attracted
- **Momentum cascade**

**2008: Crisis unwind**
- Risk-off → Carry trades liquidated
- AUD crashes: 0.95 → 0.60 (-37%)
- **Violent reversal**

**Momentum worked 2003-2007 (captured carry + appreciation)**

**But crashed 2008 (momentum risk!)**

### 6. Portfolio

**Why diversified momentum outperforms single-market:**

**Correlation across markets:**

$$
\rho(\text{Commodities}, \text{Equities}) \approx 0.2\text{-}0.3
$$

$$
\rho(\text{Bonds}, \text{Equities}) \approx -0.1\text{-}0.2
$$

**Portfolio volatility:**

$$
\sigma_P = \sqrt{\sum_i w_i^2 \sigma_i^2 + \sum_{i \neq j} w_i w_j \rho_{ij} \sigma_i \sigma_j}
$$

**Low correlation → Lower portfolio vol:**

**Single-market momentum:**
- Crude oil only
- Sharpe: 0.55
- Drawdown: -45%

**Diversified momentum (20 markets):**
- Commodities + equities + bonds + FX
- Sharpe: 0.77
- Drawdown: -25%
- **Diversification benefit**

**Moskowitz et al. result:**

Adding just 10 uncorrelated momentum strategies:

$$
\text{Sharpe}_{\text{portfolio}} \approx \sqrt{10} \times \text{Sharpe}_{\text{single}} = 3.16 \times 0.55 = 1.74
$$

**In practice: Sharpe ≈ 0.77-1.24 (excellent)**

---

## Key Terminology

**Momentum:**

$$
\text{Tendency for past winners to continue outperforming}
$$

- Empirically validated anomaly
- Works across all asset classes
- Persistence over 1-12 months
- Mean-reverts over 3-5 years

**Time-Series Momentum (TSMOM):**

$$
\text{Signal}_i = \text{sign}(\text{Return}_{i, \text{past 12 months}})
$$

- Absolute momentum
- Compare asset to itself
- Long if up, short if down
- **Trend following**

**Cross-Sectional Momentum (XSMOM):**

$$
\text{Signal}_i = \text{Rank}(\text{Return}_{i, \text{past 12 months}})
$$

- Relative momentum
- Compare assets to each other
- Long winners, short losers
- **Relative strength**

**Lookback Period:**

$$
\text{Formation Period} = t-12 \text{ to } t-1
$$

- Historical window for calculating returns
- Standard: 12 months
- Skip most recent month (t-1)
- **Signal calculation window**

**Holding Period:**

$$
\text{Hold} = 1\text{-}3 \text{ months}
$$

- How long to maintain position
- Rebalance monthly (standard)
- Allows trends to develop
- **Investment horizon**

**Volatility Scaling:**

$$
w_i = \frac{\text{Signal}_i}{\sigma_i} \times \text{Vol Target}
$$

- Position sizing by inverse volatility
- High-vol assets get smaller weights
- Equalizes risk contribution
- **Risk parity**

**Sharpe Ratio:**

$$
\text{Sharpe} = \frac{\mathbb{E}[R - r_f]}{\sigma_R}
$$

- Risk-adjusted return
- Momentum: 0.77 (exceptional)
- Equities: 0.30-0.40 (typical)
- **Key performance metric**

**Momentum Crash:**

$$
\text{Rapid simultaneous reversal of all trends}
$$

- Losers become winners
- Winners become losers
- Violent unwinding
- **Tail risk event**

**Skip-Month:**

$$
\text{Calculate return from } t-13 \text{ to } t-2
$$

- Exclude most recent month
- Reduces reversal effects
- Improves Sharpe (empirically)
- **Refinement**

**Ex-Post Volatility:**

$$
\sigma_i = \sqrt{\frac{1}{N}\sum_{t=1}^{N} (r_{i,t} - \bar{r}_i)^2}
$$

- Historical volatility estimation
- Used for position sizing
- Rolling 60-day typical
- **Risk measure**

**Risk Parity:**

$$
w_i \times \sigma_i = \text{constant for all } i
$$

- Equal risk contribution
- Not equal dollar weights
- Diversification benefit
- **Portfolio construction principle**

---

## The Greeks (Momentum

**While momentum isn't options, we can define analogous sensitivities:**

### 1. Delta

**Definition:** Exposure to absolute price movements.

**Momentum strategies are FULLY directional:**

$$
\Delta_{\text{long position}} = +1.0
$$

$$
\Delta_{\text{short position}} = -1.0
$$

**Example:**

**Portfolio (month-end):**
- Long crude oil: 30% of portfolio
- Short natural gas: 20% of portfolio
- Long gold: 15% of portfolio
- Short copper: 10% of portfolio

**Net directional exposure:**
- Energy: +30% (crude) - 20% (gas) = +10% net long
- Metals: +15% (gold) - 10% (copper) = +5% net long
- **Total: Diversified directional**

**Unlike spreads (delta-neutral), momentum is pure trend-following!**

### 2. Gamma (Trend

**Definition:** How delta changes as trends accelerate/decelerate.

$$
\Gamma_{\text{futures}} = 0 \quad \text{(linear instruments)}
$$

**But effective "gamma" from rebalancing:**

**Example: Crude oil accelerating trend**

**Month 1:**
- 12-month return: +15%
- Position: Long 30%

**Month 2:**
- 12-month return: +25% (accelerating)
- Position: Long 35%
- **Increased exposure (adding to winner)**

**This creates "positive gamma" effect:**
- Trends accelerate → Increase position
- Trends decelerate → Reduce position
- **Trend-following nature**

**Contrast with options:**
- Options gamma = convexity
- Momentum "gamma" = rebalancing
- **Similar payoff profile**

### 3. Theta (Time Decay

**Definition:** How signal strength changes over time.

$$
\Theta_{\text{momentum}} = \frac{\partial \text{Signal Strength}}{\partial t}
$$

**Momentum signals decay:**

**Example: Crude oil trend**

**Month 1:**
- Strong signal: +25% over 12 months
- High conviction
- Large position: 40%

**Month 6 (trend continuing but slowing):**
- Moderate signal: +18% over 12 months
- Weakening
- Reduced position: 30%

**Month 12 (trend exhausted):**
- Weak signal: +5% over 12 months
- Near reversal
- Small position: 10%

**Theta is negative for momentum:**
- Signals decay over time
- Must rebalance to capture fresh trends
- **Why monthly rebalancing critical**

### 4. Vega (Volatility

**Definition:** How strategy performs in different volatility regimes.

**Momentum benefits from volatility:**

$$
\text{Vega}_{\text{momentum}} > 0
$$

**Why:**

**High volatility → Bigger trends:**
- Larger price moves
- Stronger signals
- Momentum profits amplified
- **Volatility is friend**

**Example: 2008 Crisis**

**High volatility regime:**
- Crude oil: Crashed 70% in 6 months
- VIX: 80+
- Momentum captured decline
- **Profits from vol**

**Low volatility regime:**
- 2017: VIX < 10
- Crude oil: Range-bound $45-55
- Momentum: +8% (modest)
- **Lower profits in low vol**

**Empirical relationship:**

$$
\text{Momentum Return}_t \propto \text{Volatility}_{t-1}
$$

**Long volatility exposure (generally positive)**

### 5. Rho (Interest

**Definition:** Sensitivity to interest rate changes.

$$
\rho_{\text{momentum}} \approx 0
$$

**Futures have minimal rate sensitivity:**

- Marked to market daily
- No carry to expiration
- **Ignore for momentum**

**Exception: Bond futures momentum**

When trading bond futures:
- Rate changes = price changes
- Momentum signal captures rate trends
- But strategy itself not rate-sensitive
- **Indirect effect**

### 6. Beta (Market

**Definition:** Correlation to equity markets.

$$
\beta_{\text{momentum, SPX}} \approx 0.1\text{-}0.3
$$

**Low equity beta is HUGE advantage:**

**Diversification benefit:**

- Equities in crisis: -40%
- Momentum: +5-15% (often positive!)
- Low correlation
- **Portfolio hedge**

**Example: 2008 Financial Crisis**

**Equities:**
- S&P 500: -37%
- **Disaster**

**Momentum:**
- Captured oil crash (short)
- Captured bond rally (long)
- Captured dollar strength (long USD)
- Return: +16%
- **Crisis alpha**

**This low beta = why institutions love momentum!**

---

## Strategy Selection

**Not all momentum implementations are equal:**

### 1. Classic 12-1

**Specification:**

$$
\text{Signal}_t = \text{sign}\left(\frac{P_{t-1} - P_{t-12}}{P_{t-12}}\right)
$$

**Characteristics:**

- Lookback: 12 months
- Skip: 1 month (use t-13 to t-2 optionally)
- Rebalance: Monthly
- Position: Volatility-scaled
- **Gold standard**

**Historical performance:**

- Sharpe ratio: 0.77 (1965-2009)
- Max drawdown: -25% (diversified)
- Win rate: 55-60%
- **Robust**

**Pros:**

- Most academic research
- Long track record
- Proven across markets
- **Institutional quality**

**Cons:**

- Monthly rebalancing (not daily)
- Can be slow to enter trends
- Suffers in quick reversals
- **Trade-off for stability**

### 2. Fast Momentum

**Specification:**

$$
\text{Signal}_t = \text{sign}\left(\frac{P_{t-1} - P_{t-3}}{P_{t-3}}\right)
$$

**Characteristics:**

- Lookback: 3-6 months
- Faster trend capture
- Higher turnover
- **More responsive**

**Historical performance:**

- Sharpe ratio: 0.65 (lower than 12-month)
- Max drawdown: -30% (worse)
- Win rate: 52-55%
- **More volatile**

**Pros:**

- Captures trends earlier
- Adapts faster to reversals
- Can outperform in trending markets
- **Agile**

**Cons:**

- More whipsaws (false signals)
- Higher transaction costs
- Less stable
- **Noisy**

**When to use: Strong trending environments**

### 3. Slow Momentum

**Specification:**

$$
\text{Signal}_t = \text{sign}\left(\frac{P_{t-1} - P_{t-24}}{P_{t-24}}\right)
$$

**Characteristics:**

- Lookback: 24 months
- Very stable signals
- Low turnover
- **Conservative**

**Historical performance:**

- Sharpe ratio: 0.55 (lower)
- Max drawdown: -22% (better)
- Win rate: 60-65% (higher)
- **Stable but lower returns**

**Pros:**

- Fewest false signals
- Lowest transaction costs
- Smooth P&L
- **Low maintenance**

**Cons:**

- Slow to enter trends
- Slow to exit reversals
- Lower absolute returns
- **Misses opportunities**

**When to use: Low-cost, passive implementation**

### 4. Combined Signal

**Specification:**

$$
\text{Signal}_t = w_1 \times \text{Signal}_{3M} + w_2 \times \text{Signal}_{6M} + w_3 \times \text{Signal}_{12M}
$$

**Example weights:**

$$
\text{Signal}_t = 0.3 \times \text{Signal}_{3M} + 0.3 \times \text{Signal}_{6M} + 0.4 \times \text{Signal}_{12M}
$$

**Characteristics:**

- Combines multiple lookbacks
- Balanced approach
- Reduces whipsaws
- **Sophisticated**

**Historical performance:**

- Sharpe ratio: 0.85 (best!)
- Max drawdown: -23%
- Win rate: 58-62%
- **Superior risk-adjusted**

**Pros:**

- Captures trends at multiple scales
- More robust signals
- Better Sharpe
- **Institutional approach**

**Cons:**

- More complex
- Harder to implement
- Requires optimization
- **Technical**

### 5. Comparison Table

| Strategy | Lookback | Sharpe | Max DD | Turnover | Best For |
|----------|----------|--------|--------|----------|----------|
| Classic 12-1 | 12 months | 0.77 | -25% | 35%/yr | Most traders |
| Fast 3-6 | 3-6 months | 0.65 | -30% | 80%/yr | Active traders |
| Slow 24 | 24 months | 0.55 | -22% | 20%/yr | Passive/low-cost |
| Combined | 3/6/12 | 0.85 | -23% | 50%/yr | Sophisticated |

**Beginner recommendation: Classic 12-1 month (most validated, simplest, robust)**

---

## Time Selection

**Momentum is SYSTEMATIC, not discretionary:**

### 1. Entry Timing

**Standard approach:**

$$
\text{Rebalance Date} = \text{Last trading day of month}
$$

**Process:**

**Step 1: Calculate signals (month-end close)**

For each futures market:

$$
r_i = \frac{P_{i, \text{today}} - P_{i, \text{12 months ago}}}{P_{i, \text{12 months ago}}}
$$

**Step 2: Determine positions**

$$
\text{Position}_i = \begin{cases}
+1 & \text{if } r_i > 0 \\
-1 & \text{if } r_i < 0
\end{cases}
$$

**Step 3: Scale by volatility**

$$
w_i = \frac{\text{Position}_i}{\sigma_i} \times \text{Vol Target}
$$

**Step 4: Execute trades**

- Close old positions
- Open new positions
- **All on month-end close**

**Example (Jan 31 rebalance):**

**Crude oil:**
- 12-month return: +18%
- Signal: Long
- Vol: 35%
- Weight: +1/0.35 × 0.12 = 34.3%
- **Enter 34.3% long position**

**Natural gas:**
- 12-month return: -25%
- Signal: Short
- Vol: 60%
- Weight: -1/0.60 × 0.12 = -20%
- **Enter 20% short position**

### 2. Exit Timing

**No discretionary exits:**

$$
\text{Exit} = \text{Next month-end rebalance}
$$

**Example:**

- Entered long crude Jan 31
- Hold through February
- Feb 28: Recalculate signal
- If still positive: Keep position
- If now negative: Exit and reverse
- **Systematic**

**This eliminates emotion and second-guessing!**

### 3. Intra-Month

**Standard: Do nothing**

- Hold positions
- No intra-month trading
- Ignore daily noise
- **Discipline**

**Exception: Risk management stop**

$$
\text{If daily loss} > 5\% \text{ of portfolio} \Rightarrow \text{Review}
$$

**But generally: Trust the system**

### 4. Handling

**Momentum's biggest risk: Rapid reversals**

**March 2009 scenario:**

**Feb 28 positions:**
- Short equities (E-mini S&P)
- Short oil
- Long bonds
- **All losing positions**

**March 9: Bottom**
- Equities rally +20% in 3 weeks
- Oil rallies +15%
- Bonds fall
- **Violent reversal**

**March 31 rebalance:**
- Signals now reversed
- Close shorts, go long
- **Follow the system**

**P&L:**
- Feb-Mar: -12% (reversal loss)
- Apr-Jun: +8% (new trends)
- **System recovered**

**Lesson: Reversals hurt, but system adapts at next rebalance**

### 5. Alternative

**Some traders use weekly/daily:**

**Weekly rebalancing:**
- Check signals Friday close
- Rebalance Monday open
- More responsive
- Higher costs

**Daily rebalancing:**
- Recalculate signals daily
- Continuous adjustment
- Very high turnover
- **Not recommended (costs > benefits)**

**Empirical evidence:**

| Frequency | Sharpe | Turnover | Net (after costs) |
|-----------|--------|----------|-------------------|
| Monthly | 0.77 | 35%/yr | 0.72 |
| Weekly | 0.75 | 95%/yr | 0.65 |
| Daily | 0.73 | 280%/yr | 0.55 |

**Monthly is optimal (balances responsiveness and costs)**

---

## Maximum Profit and

### 1. Diversified

**Setup:**

- Account: $1,000,000
- Strategy: 12-month TSMOM
- Markets: 20 futures (commodities, equities, bonds, FX)
- Vol target: 12% annualized
- Rebalance: Monthly

**Typical Year (Expected Return):**

**Monthly returns distribution:**

- Positive months: 7-8 (58%)
- Negative months: 4-5 (42%)
- Average positive: +2.5%
- Average negative: -2.0%

**Annual calculation:**

$$
\text{Expected Annual} = 12 \times 0.58 \times 0.025 - 12 \times 0.42 \times 0.020 = 0.174 - 0.101 = 7.3\%
$$

Wait, that's lower than historical 14.9%. Let me recalculate:

$$
\text{Monthly Return} = 14.9\% / 12 = 1.24\% \text{ per month (average)}
$$

**Compounded annual:**

$$
(1.0124)^{12} - 1 = 15.9\%
$$

**On $1M account:**

$$
\text{Profit} = \$1,000,000 \times 0.159 = \$159,000
$$

**With 12% volatility:**

- Good year (+1σ): $159k + $120k = **$279k (28%)**
- Bad year (-1σ): $159k - $120k = **$39k (4%)**

**Maximum Profit (Perfect Trending Year like 2008):**

**2008 performance:**
- Financial crisis
- Strong trends everywhere
- Oil crashed (captured short)
- Bonds rallied (captured long)
- Dollar strengthened (captured long)
- **Return: +40%**

**On $1M:**

$$
\text{Profit} = \$400,000
$$

**Maximum Loss (Momentum Crash like 2009):**

**March-April 2009:**
- All trends reversed simultaneously
- Equities bottomed and rallied
- Commodities bottomed and rallied
- Safe havens reversed
- **Return: -15% in 2 months**

**On $1M:**

$$
\text{Loss} = -\$150,000
$$

**Annual drawdown: -25% (historical max)**

$$
\text{Max DD} = -\$250,000
$$

### 2. Single-Market

**Setup:**

- Account: $500,000
- Strategy: Crude oil momentum only
- Vol target: 15%
- **Concentrated**

**Typical Year:**

- Expected return: 12%
- Volatility: 35% (single market)
- **Profit: $60,000**

**Best Year (2008 oil crash):**

- Captured -70% decline
- Return: +55%
- **Profit: $275,000**

**Worst Year (2016 reversal):**

- Oil fell then reversed
- Whipsawed
- Return: -28%
- **Loss: -$140,000**

**Much higher risk than diversified!**

### 3. Real Example

**Hypothetical managed futures fund:**

**AUM: $2 billion**

**Strategy: Diversified momentum**
- 60 futures markets
- Vol target: 10%
- Monthly rebalancing

**2008 (Crisis year):**

$$
\text{Return} = +20\%
$$

$$
\text{Profit} = \$2B \times 0.20 = \$400M
$$

**S&P 500: -37% (contrast!)**

**2009 (Reversal year):**

$$
\text{Return} = -12\%
$$

$$
\text{Loss} = \$2B \times 0.12 = -\$240M
$$

**S&P 500: +26% (negative correlation!)**

**2010-2015 (Moderate years):**

- Average return: +8%
- Annual profit: ~$160M
- **Steady income**

**10-year cumulative (2008-2017):**

- Total return: +110%
- Sharpe ratio: 0.68
- **Solid performance**

---

## When to Use Momentum

### 1. Ideal Market

**Use momentum when:**

**1. Trending markets:**

$$
\text{Directional Move} > 15\% \text{ over 12 months}
$$

**Strong trends in multiple markets:**
- Commodities trending
- Equities trending
- Bonds trending
- **Momentum thrives**

**2. High volatility:**

$$
\text{VIX} > 20 \text{ or Commodity Vol} > 30\%
$$

**Volatility creates trends:**
- Larger price moves
- Stronger signals
- Better risk/reward
- **Momentum profits**

**3. Information flow changes:**

**New regimes:**
- Fed policy shift
- Geopolitical events
- Technology disruptions
- **Trends develop**

**4. Correlation breakdowns:**

**Markets decoupling:**
- Commodities ≠ equities
- Bonds ≠ equities
- Diversification works
- **Portfolio shines**

**5. Long time horizon:**

$$
\text{Investment Horizon} > 3 \text{ years}
$$

**Short-term drawdowns acceptable:**
- Focus on long-term Sharpe
- Ride through crashes
- **Patience rewarded**

### 2. Specific Use

**Use Case 1: Portfolio diversification**

**Traditional 60/40 portfolio:**
- 60% stocks
- 40% bonds
- Correlation: 0.20

**Add 20% momentum:**
- 48% stocks
- 32% bonds
- 20% momentum (funded by leverage or reduction)
- **Improved Sharpe**

**Benefit:**

- Momentum correlation to stocks: 0.15
- Momentum correlation to bonds: -0.05
- Crisis hedge (2008: +20% when stocks -37%)
- **True diversification**

**Use Case 2: Systematic CTA replication**

**Want CTA exposure without fees:**

**DIY momentum:**
- Implement 12-month TSMOM
- 20-30 liquid futures
- Monthly rebalancing
- **Replicate 70% of CTA returns**

**Cost comparison:**

| Approach | Returns | Fees | Net |
|----------|---------|------|-----|
| CTA fund | 12% | -2% | 10% |
| DIY momentum | 10% | -0.2% | 9.8% |

**Almost identical after fees!**

**Use Case 3: Crisis alpha generation**

**Long equity portfolio manager:**

**Problem:**
- Long-only equities
- Crashes hurt
- Need hedge

**Solution:**
- Allocate 10% to momentum
- Captures crash (short equities signal)
- Offsets portfolio losses
- **Dynamic hedge**

**Example (2008):**
- Equities: -37% on 90% = -33.3%
- Momentum: +20% on 10% = +2.0%
- **Net: -31.3% vs -37% (saved 5.7%!)**

**Use Case 4: Absolute return strategy**

**Goal: Positive returns regardless of market:**

**Momentum characteristics:**
- Long and short positions
- Not tied to equity direction
- Crisis-resistant
- **True absolute return**

**Track record:**
- Positive 65-70% of years
- Sharpe 0.77
- Low equity beta
- **Meets objectives**

---

## When NOT to Use

### 1. Avoid These

**1. Choppy, range-bound markets:**

$$
\text{12-Month Range} < 10\%
$$

**Example: 2015-2016**

- Crude oil: Range $35-50 (choppy)
- S&P 500: Range 1,850-2,100 (flat)
- No clear trends
- **Momentum whipsawed**

**Result:**
- Many false signals
- Constant reversals
- Return: -5%
- **Skip these years**

**2. Rapid, violent reversals:**

**March 2009 scenario:**
- V-shaped recovery
- 3-week reversal
- All trends flipped
- **Momentum disaster**

**If you see:**
- Extreme pessimism
- Capitulation volume
- Central bank intervention
- **Reduce exposure**

**3. Structural market changes:**

**Example: Oil market 2014**

- Shale revolution
- OPEC strategy shift
- Market structure changed
- Old relationships broke
- **Momentum failed temporarily**

**4. High transaction costs:**

**Illiquid futures:**
- Wide bid-ask spreads
- Low volume
- Slippage >0.5%
- **Costs eat returns**

**Minimum liquidity:**

$$
\text{Volume} > 10,000 \text{ contracts/day}
$$

**Otherwise skip**

**5. Insufficient capital:**

$$
\text{Account} < \$250,000
$$

**Why:**

- Need diversification (20+ markets)
- Each market $10-50k margin
- Total margin: $200-500k
- **Undercapitalized = concentrated risk**

**6. Can't accept drawdowns:**

**Investor psychology:**
- Momentum has 25% max drawdown
- Takes 12-18 months to recover
- If can't stomach: Don't trade
- **Emotional capacity required**

**7. Very short time horizon:**

$$
\text{Horizon} < 1 \text{ year}
$$

**Momentum needs time:**
- Drawdowns can last 12 months
- Need full cycle to profit
- Short-term: Too noisy
- **Long-term strategy**

### 2. Warning Signs to

**1. All signals aligned (crowded trade):**

**Example:**
- 18 of 20 markets long
- Very few shorts
- Extreme crowding
- **Reversal risk high**

**Action: Reduce position sizes 25-50%**

**2. Momentum crash indicators:**

**Signals:**
- VIX spike >40 then crashes
- Massive short covering
- "V" shaped reversals
- **Crash imminent**

**Action: Reduce momentum allocation temporarily**

**3. Your own signals deteriorating:**

**Portfolio metrics:**
- 3-month rolling Sharpe <0
- 4 consecutive losing months
- Drawdown >15%
- **System under stress**

**Action: Review implementation, consider reducing size**

**4. Correlation spike:**

**Normal:**
- Markets uncorrelated
- Diversification working

**Crisis:**
- Correlation →1.0
- All markets moving together
- Diversification failing
- **Risk concentration**

**Action: Reduce leverage, increase cash**

---

## Position Sizing and

### 1. The Golden Rule

**Core principle:**

$$
\text{Portfolio Volatility} = \text{Target (10-15\% annual)}
$$

**Position sizing:**

$$
w_i = \frac{\text{Signal}_i}{\sigma_i} \times \frac{\text{Vol Target}}{\sqrt{N}}
$$

Where:
- $w_i$ = weight of asset $i$
- $\sigma_i$ = volatility of asset $i$
- $N$ = number of markets
- Vol Target = 12% (example)

**Example:**

**Crude oil:**
- Signal: +1 (long)
- Volatility: 35%
- Markets: 20

$$
w_{\text{crude}} = \frac{+1}{0.35} \times \frac{0.12}{\sqrt{20}} = 2.857 \times 0.0268 = 7.7\%
$$

**Natural gas:**
- Signal: -1 (short)
- Volatility: 60%

$$
w_{\text{gas}} = \frac{-1}{0.60} \times 0.0268 = -4.5\%
$$

**This creates risk parity:**

$$
w_i \times \sigma_i \approx \text{constant}
$$

- Crude: 7.7% × 35% = 2.7%
- Gas: 4.5% × 60% = 2.7%
- **Equal risk contribution**

### 2. Portfolio

**Conservative (5-10% of total portfolio):**

**Example: $1M total portfolio**

- Core: $900k (stocks/bonds)
- Momentum: $100k (10%)
- Leverage: None or 1.5×
- **Moderate exposure**

**Moderate (10-20% of total):**

- Core: $800k
- Momentum: $200k (20%)
- Leverage: 2×
- **Active allocation**

**Aggressive (20-30% standalone):**

- Momentum: $1M (100%)
- Leverage: 3-4×
- Vol target: 15-20%
- **Dedicated strategy**

**Institutional (CTA fund):**

- Momentum: 100% of AUM
- Leverage: 4-6×
- Vol target: 10-15%
- **Professional implementation**

### 3. Diversification

**Minimum markets:**

$$
N_{\text{min}} = 20 \text{ futures markets}
$$

**Recommended allocation:**

| Asset Class | Markets | Allocation |
|-------------|---------|------------|
| Commodities | 8-10 | 35% |
| Equity Indices | 5-7 | 30% |
| Bonds | 3-5 | 20% |
| Currencies | 4-6 | 15% |

**Example 20-market portfolio:**

**Commodities (8):**
- Crude oil, Natural gas, Gold, Silver, Copper, Corn, Soybeans, Wheat

**Equities (6):**
- S&P 500, Nasdaq, DAX, FTSE, Nikkei, Hang Seng

**Bonds (3):**
- US 10Y, German Bund, Japanese JGB

**FX (3):**
- EUR/USD, GBP/USD, USD/JPY

**Correlation matrix (ideal):**

$$
\bar{\rho} \approx 0.2\text{-}0.3 \quad \text{(low average correlation)}
$$

### 4. Stop Loss

**No traditional stops for momentum:**

**Why:**
- Systematic strategy
- Signals determine positions
- No discretionary stops
- **System-based**

**But portfolio-level risk controls:**

**1. Volatility scaling:**

$$
\text{If } \sigma_{\text{portfolio}} > 1.5 \times \text{Target} \Rightarrow \text{Reduce leverage}
$$

**Example:**
- Target: 12%
- Actual: 20% (crisis)
- **Scale down positions 40%**

**2. Maximum drawdown trigger:**

$$
\text{If DD} > 20\% \Rightarrow \text{Review/reduce}
$$

**Action:**
- Review implementation
- Check for errors
- Consider reducing size 25%
- **Circuit breaker**

**3. Individual market caps:**

$$
\text{Max position} = 15\% \text{ of portfolio}
$$

**Prevents concentration**

### 5. Leverage

**Futures allow massive leverage:**

$$
\text{Notional Exposure} = 3\text{-}6 \times \text{Account Size}
$$

**Example: $1M account**

**Total notional positions:**
- 20 markets × $150k avg = $3M notional
- Leverage: 3×
- Margin requirement: ~$500k
- **Remaining capital: $500k (buffer)**

**Institutional (higher leverage):**
- Notional: $6M (6×)
- Margin: $900k
- Buffer: $100k
- **Efficient use of capital**

**Leverage limits:**

$$
\text{Max Notional} = 6 \times \text{Capital}
$$

**Beyond this: Unmanageable risk**

### 6. Account:

**Account: $1,000,000**

**Strategy: Diversified 12-month TSMOM**

**Markets: 20 futures**

**Vol target: 12%**

**Position sizing (month-end):**

| Market | Signal | Vol | Weight | Notional | Margin |
|--------|--------|-----|--------|----------|--------|
| Crude | +1 | 35% | 7.7% | $77k | $4k |
| Nat Gas | -1 | 60% | 4.5% | -$45k | $3k |
| Gold | +1 | 18% | 15.0% | $150k | $8k |
| S&P 500 | +1 | 20% | 13.5% | $135k | $15k |
| ... | ... | ... | ... | ... | ... |

**Total:**
- Sum of |positions|: $2.8M (2.8× leverage)
- Margin required: $480k
- Cash buffer: $520k
- **Conservative leverage**

**Risk metrics:**

- Portfolio vol (ex-ante): 12.0%
- Max individual position: 15% (Gold)
- Average correlation: 0.25
- **Well-diversified**

**If markets decline 10%:**
- Typical loss: 12% × 0.4 (beta) = -4.8%
- Account: $1M → $952k
- Margin call: None (buffer exists)
- **Manageable**

---

## Common Mistakes

### 1. The error: "Crude

**The error:**

- "Crude oil has great momentum!"
- Trade only crude
- No diversification
- **Concentrated risk**

**What happens:**

**2016 Crude oil:**
- Jan-Feb: Fell from $35 → $26 (-26%)
- Momentum signal: Short
- Feb-May: Rallied $26 → $48 (+85%)
- **Whipsawed, massive loss**

**If diversified (20 markets):**
- Crude loss offset by other trends
- Portfolio: -3%
- **Diversification saved**

**Correct approach:**

$$
N \geq 20 \text{ markets minimum}
$$

### 2. The error: Signal

**The error:**

- Signal says long gold
- Trader: "But I think gold will fall"
- Override signal, skip trade
- **Kills system edge**

**What happens:**

**Scenario:**
- Gold signal: Long
- Trader skips (thinks overvalued)
- Gold rallies 20%
- **Missed major trend**

**Result:**
- Only took trades that "made sense"
- Missed 40% of profits
- Sharpe collapsed from 0.77 → 0.30
- **Discretion destroyed edge**

**Correct approach:**

**Trust the system:**
- Follow ALL signals
- No cherry-picking
- Emotion-free execution
- **Systematic discipline**

### 3. The error:

**The error:**

- Backtest 100 lookback periods
- Find "optimal": 8.7 months
- Sharpe: 1.2 (in-sample)
- Use this parameter
- **Overfitting**

**What happens (forward):**

- Live trading: Sharpe 0.3
- Completely different
- Optimized to noise
- **Data mining failure**

**Correct approach:**

**Use standard parameters:**
- 12-month lookback (established)
- Monthly rebalancing (proven)
- Don't over-optimize
- **Robust > optimal**

### 4. The error:

**The error:**

- Backtest shows 15% return
- Assume net return = 15%
- Ignore commissions, slippage
- **Unrealistic**

**Reality:**

**Cost breakdown (per round-trip):**
- Commission: $2-5 per contract
- Slippage: 0.5-1 tick ($5-50)
- Total: $10-50 per round-trip

**Annual turnover: 100% (2× for buy/sell)**

**20 markets, avg 10 contracts each:**
- Trades: 20 × 10 × 2 = 400 round-trips/year
- Cost: 400 × $30 = $12,000
- On $1M: 1.2% drag
- **Net: 15% - 1.2% = 13.8%**

**Correct approach:**

**Model costs in backtest:**
- Include commissions
- Include slippage estimate
- Calculate net returns
- **Realistic expectations**

### 5. The error: $100k

**The error:**

- $100k in crude oil
- $100k in natural gas
- "Equal dollar weights"
- **Not equal risk**

**What happens:**

**Volatility:**
- Crude: 35% × $100k = $35k risk
- Nat gas: 60% × $100k = $60k risk
- **Nat gas has 71% more risk!**

**Correct approach:**

**Volatility scaling:**

$$
w_i \propto \frac{1}{\sigma_i}
$$

- Crude: Higher allocation (lower vol)
- Nat gas: Lower allocation (higher vol)
- **Equal risk contribution**

### 6. The error:

**The error:**

**Drawdown:**
- Portfolio down 15% from peak
- 6 months of losses
- Trader: "System broken!"
- Exit strategy
- **Panic**

**What happens:**

**Historical pattern:**
- Max drawdown: 25%
- Recovery time: 12-18 months
- This is NORMAL

**But trader exited:**
- Missed recovery
- Never got back in
- **Lost long-term edge**

**Correct approach:**

**Expect drawdowns:**
- 25% DD is expected
- Part of strategy
- Trust long-term Sharpe
- **Stay invested**

### 7. The error:

**The error:**

**Observation:**
- Last 12 months: Momentum +35%
- Trader: "I need this!"
- Allocates heavily NOW
- **Performance chasing**

**What happens:**

**Next 12 months:**
- Momentum: -8% (reversal)
- Bought at peak
- **Timing disaster**

**Correct approach:**

**Dollar-cost averaging:**
- Allocate over 6-12 months
- Build position gradually
- Average entry price
- **Smooth timing**

### 8. The error: Use

**The error:**

- Use 1-month momentum
- Very short-term
- Hoping for fast profits
- **Reversal risk**

**What happens:**

**1-month signals:**
- Mostly noise
- Reversal effects dominate
- Sharpe: -0.2 (negative!)
- **Doesn't work**

**Academic evidence:**

- <3 months: Reversal (negative returns)
- 3-12 months: Momentum (positive returns)
- >24 months: Slight reversal
- **Sweet spot: 6-12 months**

**Correct approach:**

$$
\text{Lookback} \in [6, 12] \text{ months}
$$

### 9. The error: Set

**The error:**

- Set positions in January
- Hold all year
- Never rebalance
- **Stale signals**

**What happens:**

**Example:**
- Jan: Long crude (momentum +20%)
- Jun: Crude momentum now -5% (reversed)
- But still holding long (no rebalance)
- **Riding reversed trend down**

**Correct approach:**

**Monthly rebalancing:**
- Recalculate signals monthly
- Update positions
- Exit dead trends
- **Fresh signals**

### 10. The error: Use

**The error:**

- Use 10× leverage
- Maximize returns
- Think: "Sharpe 0.77 × 10 = 7.7!"
- **Misunderstanding math**

**What happens:**

**Volatility scales linearly:**
- 1× leverage: 12% vol, 15% return
- 10× leverage: 120% vol, 150% return
- Sharpe: SAME (0.77)

**But ruin risk:**
- One bad month: -15% × 10 = -150%
- Account wiped out
- **Gambler's ruin**

**Correct approach:**

**Moderate leverage:**

$$
\text{Leverage} \leq 4\times
$$

- Balances return and safety
- Prevents blowup
- **Sustainable**

---



## Final Wisdom

> "Momentum is the premier risk premium in futures markets—academically validated across 100+ years, robust across all asset classes, and exhibiting a Sharpe ratio of 0.77 that puts most strategies to shame. But momentum is NOT a free lunch. It comes with catastrophic drawdown risk (25% max historically), violent reversals during market turning points (March 2009 -24% in 2 months), and the psychological challenge of following mechanical signals through drawdowns. The successful momentum trader is ruthlessly systematic (no discretion), properly diversified (20-30 markets minimum), volatility-aware (scale positions inversely), and patient (accepts drawdowns as cost of premium). Momentum works because behavioral biases (underreaction, herding) and structural forces (slow supply response, gradual information diffusion) create persistent trends. But these same forces can reverse violently when markets panic or capitulate. Trade momentum as a long-term portfolio diversifier with institutional discipline, not as a get-rich-quick scheme. The strategy's Sharpe ratio is earned through surviving multiple cycles, not chasing every trend."

**Most important principles:**

- Momentum = systematic, not discretionary
- Diversification essential (single-market fails)
- Volatility scaling critical (risk parity)
- Monthly rebalancing non-negotiable
- Drawdowns inevitable (25% historical max)
- Long-term focus (>3 year horizon)
- Low equity correlation (portfolio hedge)
- Transaction costs matter (1-2% drag)

**Why this works:**

- Behavioral biases (underreaction, herding)
- Slow information diffusion (3-12 month lag)
- Structural forces (supply response time)
- Risk premium (compensation for crash risk)
- **Persistent anomaly (100+ years)**

**But remember:**

- Momentum crashes happen (2009 style)
- Requires iron discipline (no overrides)
- Not suitable for all investors (drawdown tolerance)
- Capital intensive ($250k+ minimum)
- Complexity (30 markets to monitor)
- **Not easy money, despite academic edge**

**Implement momentum with institutional rigor or don't implement at all. Half-measures destroy the edge. 📈⚖️**