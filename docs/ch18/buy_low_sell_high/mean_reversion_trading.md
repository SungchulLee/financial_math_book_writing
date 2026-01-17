# Mean Reversion Trading with Futures

**Mean reversion trading with futures** is a strategy that exploits the statistical tendency of prices to return to their average levels, using liquid futures contracts to profit from oversold or overbought conditions through direct linear exposure, with entry and exit criteria based on z-scores, Bollinger Bands, and statistical measures of extreme deviation.

---

## The Core Insight

**The fundamental idea:**

- Prices oscillate around a long-term average (mean)
- Extreme deviations tend to revert back
- When price is far from mean, probability favors return
- Futures provide direct, leveraged exposure to reversions
- Linear payoff captures full reversion move
- No premium decay (unlike options)
- Margin efficiency allows larger notional exposure

**The key equation:**

$$
z\text{-score} = \frac{P_t - \mu}{\sigma}
$$

Where probability of reversion increases with distance from mean:

$$
P(\text{Reversion}) = f(|z\text{-score}|) \quad \text{(increasing in } |z| \text{)}
$$

**You're essentially betting: "Price has moved too far, too fast. It will revert to average, and I can capture the return with a futures position."**

---

## What Is Mean Reversion?

**Before executing mean reversion strategies, understand the mechanics:**

### 1. Core Concept

**Definition:** Trading based on the statistical principle that prices oscillate around a mean and tend to revert after extreme moves, using futures to capture the return directly.

**When you trade mean reversion with futures:**

- You identify extreme price moves (2-3 standard deviations from mean)
- You bet on return to average
- You use futures for direct exposure
- You profit from snapback moves
- Linear P&L proportional to price change
- No time decay (unlike options)

**Example - E-mini S&P 500 (ES):**

- 200-day moving average: 4,500
- Standard deviation: 100 points
- Current price: 4,280 after selloff (-2.2σ)
- Historical mean reversion: 70% chance of move back to 4,400+ within 30 days

**Trade:**

- Long ES at 4,280
- Target: 4,450 (half reversion to mean)
- Stop: 4,180 (another 1σ down)
- Risk: 100 points × $50 = $5,000
- Reward: 170 points × $50 = $8,500
- R-multiple: 1.7

**Outcomes:**

- 10 days later → ES at 4,400 → Gain = +120 points × $50 = +$6,000
- Exit partial at 4,400, trail stop on remainder
- If continues to 4,500 → +$11,000 total

### 2. The Statistical Foundation

**Ornstein-Uhlenbeck Process:**

Mean-reverting prices follow:

$$
dX_t = \theta(\mu - X_t)dt + \sigma dW_t
$$

Where:
- $X_t$ = Price at time $t$
- $\mu$ = Long-term mean
- $\theta$ = Speed of reversion (mean reversion strength)
- $\sigma$ = Volatility
- $W_t$ = Brownian motion (randomness)

**Key insight: The $\theta(\mu - X_t)$ term creates pull toward $\mu$**

**Half-life of reversion:**

$$
t_{1/2} = \frac{\ln(2)}{\theta}
$$

**Example:**

- $\theta = 0.05$ (typical futures contract)
- Half-life: $\ln(2)/0.05 = 13.9$ days
- **Interpretation: Half of deviation corrects in ~14 days**

### 3. Identifying Mean Reversion Opportunities

**Z-score calculation:**

$$
z_t = \frac{P_t - \text{MA}_n}{\sigma_n}
$$

Where:
- $P_t$ = Current price
- $\text{MA}_n$ = n-period moving average
- $\sigma_n$ = n-period standard deviation

**Entry thresholds:**

| Z-score | Interpretation | Action |
|---------|----------------|--------|
| z < -2.0 | Strongly oversold | Long entry |
| z < -1.5 | Moderately oversold | Alert |
| -1.5 < z < 1.5 | Normal | No trade |
| z > 1.5 | Moderately overbought | Alert |
| z > 2.0 | Strongly overbought | Short entry |

**Example - 10-Year Treasury Futures (ZN):**

- 20-day MA: 108.50
- 20-day σ: 1.25 points
- Current price: 105.75
- Z-score: (105.75 - 108.50) / 1.25 = -2.2

**Interpretation:** Bonds are 2.2 standard deviations below mean → Long entry signal

### 4. Bollinger Band Strategy

**Definition:** Using volatility bands around a moving average to identify extremes.

**Band calculation:**

$$
\text{Upper Band} = \text{MA}_n + k \times \sigma_n
$$
$$
\text{Lower Band} = \text{MA}_n - k \times \sigma_n
$$

Where $k$ typically = 2 (captures 95% of normal moves).

**Trading rules:**

- Price touches/breaks lower band → Long entry
- Price touches/breaks upper band → Short entry
- Target: Return to MA (middle band)
- Stop: 1σ beyond entry band

**Example - Gold Futures (GC):**

- 20-day MA: $2,050
- 20-day σ: $40
- Upper Band: $2,050 + 2×$40 = $2,130
- Lower Band: $2,050 - 2×$40 = $1,970
- Current price: $1,965 (below lower band)

**Trade:**

- Entry: Long at $1,965
- Target: $2,050 (MA)
- Stop: $1,925 (1σ below entry)
- Risk: $40 × 100 oz = $4,000/contract
- Reward: $85 × 100 oz = $8,500/contract
- R-multiple: 2.1

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/mean_reversion_futures.png?raw=true" alt="mean_reversion_futures" width="700">
</p>
**Figure 1:** Mean reversion trading with futures showing price oscillation around the moving average, Bollinger Bands, entry signals at extreme deviations (±2σ), and exit targets at mean return.

---

## Economic Rationale

**Beyond the basic strategy, understanding WHY mean reversion occurs:**

### 1. The Behavioral Explanation

**The deep insight:**

Mean reversion trading exploits **emotional extremes and the statistical tendency of markets to overcorrect**:

1. **Overreaction to news:** Initial moves often too large
2. **Herding behavior:** Everyone sells at the same time
3. **Liquidity gaps:** Forced selling pushes prices beyond fair value
4. **Recovery mechanism:** Value buyers step in at extremes

**Formal decomposition:**

$$
\underbrace{P_t}_{\text{Current price}} = \underbrace{\mu}_{\text{Fair value}} + \underbrace{\epsilon_t}_{\text{Temporary deviation}}
$$

Where $\epsilon_t$ tends toward zero:

$$
\mathbb{E}[\epsilon_{t+1}|\epsilon_t] < |\epsilon_t| \quad \text{(reversion expected)}
$$

### 2. The Liquidity Premium Perspective

**Why extreme moves create opportunity:**

**During panic selloffs:**

- Forced sellers (margin calls, redemptions)
- Liquidity disappears
- Price overshoots fair value
- **Temporary discount = opportunity**

**During euphoric rallies:**

- FOMO buying
- Leverage increases
- Price overshoots fair value
- **Temporary premium = short opportunity**

**The return to fair value provides the edge.**

### 3. Statistical Evidence for Mean Reversion

**Empirical autocorrelation in futures:**

| Horizon | Autocorrelation | Implication |
|---------|-----------------|-------------|
| 1-day | +0.05 | Slight momentum |
| 5-day | +0.02 | Near random |
| 20-day | -0.08 | Slight reversion |
| 60-day | -0.15 | Stronger reversion |

**Key insight:** Negative autocorrelation at longer horizons indicates mean reversion.

**Why it happens:**

At short horizons: Momentum from information diffusion
At longer horizons: Reversion as prices return to fundamentals

### 4. Cross-Asset Mean Reversion

**Relative value opportunities:**

**Spread mean reversion:**

$$
\text{Spread}_t = P_t^A - P_t^B
$$

$$
z_{\text{spread}} = \frac{\text{Spread}_t - \mu_{\text{spread}}}{\sigma_{\text{spread}}}
$$

**Example - Crack Spread (Gasoline vs. Crude Oil):**

- Normal spread: $25/barrel
- Spread σ: $5
- Current spread: $38 (z = +2.6)

**Trade:**

- Short gasoline futures (RB)
- Long crude oil futures (CL)
- Target: Spread returns to $25
- Position: Market neutral

---

## Position Sizing and Risk Management

**Critical for mean reversion due to potential for continued extremes:**

### 1. Volatility-Based Position Sizing

**The formula:**

$$
\text{Position Size} = \frac{\text{Risk Budget}}{\sigma \times \text{Notional per Contract}}
$$

**Example - ES futures:**

- Account: $500,000
- Risk per trade: 1% = $5,000
- ES 20-day volatility: 80 points
- Notional per point: $50
- Dollar volatility: 80 × $50 = $4,000 per contract
- Position size: $5,000 / $4,000 = 1.25 → 1 contract

### 2. Z-Score-Based Position Scaling

**Larger position at more extreme levels:**

| Z-score | Position Size | Rationale |
|---------|---------------|-----------|
| 1.5-2.0 | 0.25x base | Moderate extreme |
| 2.0-2.5 | 0.50x base | Strong extreme |
| 2.5-3.0 | 0.75x base | Very strong extreme |
| >3.0 | 1.00x base | Extreme rare event |

**Example:**

- Base position: 4 contracts
- Current z-score: -2.3
- Position: 0.50 × 4 = 2 contracts
- If z falls to -2.8: Add 1 more contract (0.75x = 3 total)

### 3. Stop-Loss Placement

**Fixed volatility stop:**

$$
\text{Stop} = \text{Entry} - k \times \sigma
$$

Where $k$ typically 1.5-2.5.

**Z-score invalidation stop:**

$$
\text{Stop triggered if } z < -3.5 \text{ (for long)}
$$

**Example:**

- Long entry: ES at 4,280 (z = -2.2)
- Volatility stop: 4,280 - 1.5×80 = 4,160
- Z-score stop: If z reaches -3.5 → Price ~4,150

**Use the tighter of the two.**

### 4. Drawdown Management Protocol

**Scale down during losing streaks:**

| Consecutive Losses | Position Adjustment |
|-------------------|---------------------|
| 1 | 100% (normal) |
| 2 | 75% |
| 3 | 50% |
| 4+ | 25% or pause |

**Rationale:**

Mean reversion can fail when regimes change. Reducing size preserves capital.

### 5. Correlation Monitoring

**Mean reversion across positions:**

If holding multiple mean reversion trades:

$$
\text{Portfolio Risk} = \sqrt{\sum_i w_i^2 \sigma_i^2 + 2\sum_{i<j} w_i w_j \sigma_i \sigma_j \rho_{ij}}
$$

**Risk:** All positions can move against you simultaneously if correlations spike.

**Solution:** Cap total portfolio risk, diversify across uncorrelated assets.

---

## Entry and Exit Strategies

**Precise execution for mean reversion:**

### 1. Entry Timing

**Don't catch falling knives:**

Instead of entering at exact z-score threshold, wait for confirmation:

$$
\text{Entry} = \mathbb{1}_{\{z < -2\}} \times \mathbb{1}_{\{\text{RSI turning up}\}}
$$

**Confirmation indicators:**

- RSI crossing above 30 (oversold turning)
- Price closing above prior day's high
- Volume declining (selling exhaustion)
- MACD histogram improving

**Example:**

- Z-score hits -2.2 on Day 1
- RSI at 25, still falling
- **Wait**
- Day 3: Z-score at -2.5, RSI at 22, turning up
- Day 4: RSI crosses 25
- **Enter long**

### 2. Scaling into Positions

**Dollar-cost averaging at extremes:**

| Entry | Z-score | Position | Average |
|-------|---------|----------|---------|
| 1st | -2.0 | 25% | Entry 1 |
| 2nd | -2.5 | 50% | Avg(1,2) |
| 3rd | -3.0 | 75% | Avg(1,2,3) |
| 4th | -3.5 | 100% | Avg(1,2,3,4) |

**Benefit:** Better average price if extreme continues.

**Risk:** More exposure as losing → requires strict maximum.

### 3. Exit at Mean Return

**Partial profit taking:**

| Price Level | Action | Remaining |
|-------------|--------|-----------|
| z = -1.0 | Sell 25% | 75% |
| z = -0.5 | Sell 25% | 50% |
| z = 0 (mean) | Sell 25% | 25% |
| z = +0.5 | Sell 25% | 0% |

**Example - ES trade:**

- Entry at 4,280 (z = -2.2)
- Mean at 4,500
- σ = 100 points

| Z-score | Price | Action |
|---------|-------|--------|
| -1.0 | 4,400 | Exit 25% |
| -0.5 | 4,450 | Exit 25% |
| 0 | 4,500 | Exit 25% |
| +0.5 | 4,550 | Exit 25% |

### 4. Time-Based Exits

**Mean reversion has expected duration:**

$$
\text{Max Hold} = 3 \times t_{1/2}
$$

Where $t_{1/2}$ is the half-life of reversion.

**Example:**

- Half-life: 14 days
- Max hold: 42 days
- If no reversion by day 42: Exit regardless

**Rationale:** If reversion hasn't occurred, fundamental may have shifted.

### 5. Stop-Loss Discipline

**Hard stop (no exceptions):**

$$
\text{Exit if } z < z_{\text{entry}} - 1.5
$$

**Example:**

- Entry at z = -2.0
- Stop triggered at z = -3.5
- Accept loss, preserve capital

**Never average down beyond initial plan.**

---

## Futures Instrument Selection

**Choosing the right contracts for mean reversion:**

### 1. Equity Index Futures

**Best suited for:** Portfolio-level mean reversion

| Contract | Ticker | Mean Reversion Character |
|----------|--------|-------------------------|
| E-mini S&P 500 | ES | Strong, 20-40 day cycle |
| E-mini Nasdaq | NQ | Faster, more volatile |
| E-mini Russell | RTY | Highest volatility |
| VIX Futures | VX | Very strong reversion |

**ES mean reversion statistics (2015-2024):**

- Average z-score at local bottom: -1.8
- 30-day reversion probability: 72%
- Average reversion magnitude: 65% of move

### 2. Fixed Income Futures

**Best suited for:** Rate extremes, flight-to-quality reversals

| Contract | Ticker | Mean Reversion Character |
|----------|--------|-------------------------|
| 10-Year Note | ZN | Moderate, driven by Fed |
| 30-Year Bond | ZB | Slower, larger moves |
| 2-Year Note | ZT | Fast, Fed-driven |
| Eurodollar | GE | Very predictable |

**ZN mean reversion statistics:**

- Half-life: 18 days
- σ-reversion probability (2σ move): 68%

### 3. Commodity Futures

**Best suited for:** Supply/demand extremes, seasonal reversion

| Contract | Ticker | Mean Reversion Character |
|----------|--------|-------------------------|
| Gold | GC | Moderate, macro-driven |
| Crude Oil | CL | Strong but volatile |
| Natural Gas | NG | Extreme seasonal reversion |
| Corn | ZC | Seasonal, weather-driven |

**Natural Gas (NG) special case:**

- Highest mean reversion tendency in futures
- z > 3 events: ~5 per year
- 30-day reversion: 85% probability
- **But:** Extreme volatility, size carefully

### 4. Currency Futures

**Best suited for:** PPP reversion, rate differential extremes

| Contract | Ticker | Mean Reversion Character |
|----------|--------|-------------------------|
| Euro FX | 6E | Moderate |
| Japanese Yen | 6J | BoJ interventions create reversion |
| British Pound | 6B | Event-driven extremes |
| Swiss Franc | 6S | Safe haven extremes |

---

## Case Studies

**Real-world examples of mean reversion with futures:**

### 1. COVID Crash - March 2020

**Setup:**

- Pre-crash ES: 3,380 (Feb 19, 2020)
- 200-day MA: 3,150
- Crash low: 2,174 (March 23, 2020)
- Z-score at low: -4.5 (extreme!)

**Trade opportunity:**

- March 20: ES at 2,300 (z = -3.8)
- Entry: Long ES at 2,300
- Stop: 2,000 (-3σ further, unlikely)
- Target: 2,800 (half reversion)

**Execution:**

| Date | ES Price | Action |
|------|----------|--------|
| Mar 20 | 2,300 | Enter long (z = -3.8) |
| Mar 24 | 2,450 | Hold |
| Apr 3 | 2,650 | Exit 33% |
| Apr 17 | 2,850 | Exit 33% |
| May 8 | 2,930 | Exit remaining |

**Result:**

- Average exit: 2,810
- Gain: 510 points × $50 = $25,500 per contract

**Key lesson:** Extreme z-scores (>3) are rare but highly profitable.

### 2. Treasury Bond Reversion - October 2023

**Setup:**

- 10-year yield spiked to 5.0% (16-year high)
- ZN futures collapsed from 112 to 105
- Z-score: -2.8 (extreme oversold)
- 20-day MA: 109

**Trade:**

- Entry: Long ZN at 105.50 (z = -2.8)
- Stop: 103.00 (another 2.5 points down)
- Target: 109.00 (return to MA)

**Execution:**

| Date | ZN Price | Z-score | Action |
|------|----------|---------|--------|
| Oct 19 | 105.50 | -2.8 | Enter long |
| Oct 30 | 107.00 | -1.6 | Hold |
| Nov 14 | 109.50 | -0.4 | Exit 50% |
| Dec 1 | 111.00 | +0.8 | Exit remaining |

**Result:**

- Average exit: 110.25
- Gain: 4.75 points × $1,000 = $4,750 per contract

**Key lesson:** Fixed income mean reversion can be slow but reliable.

### 3. Failed Reversion - Crude Oil 2022

**Setup:**

- Pre-Russia invasion: CL at $90
- Post-invasion spike: $130 (z = +3.5)
- Entry: Short at $125 (z = +3.2)

**What went wrong:**

| Date | CL Price | Z-score | P&L |
|------|----------|---------|-----|
| Mar 7 | $125 | +3.2 | Entry short |
| Mar 8 | $130 | +3.8 | -$5,000 |
| Mar 9 | $110 | +2.0 | +$15,000 |
| Mar 11 | $108 | +1.8 | Exit +$17,000 |

**BUT if held longer:**

| Date | CL Price | What if held |
|------|----------|--------------|
| Mar 15 | $96 | Would be +$29,000 |
| Apr 1 | $100 | Would be +$25,000 |
| Jun 1 | $120 | Would be +$5,000 |

**Key lessons:**

1. Initial volatility was extreme (±$20/day)
2. Fundamental regime shift (war) → Mean shifted
3. Quick exit saved the trade
4. Mean reversion fails during regime changes

### 4. VIX Mean Reversion - December 2018

**Setup:**

- VIX spiked to 36 (December 24, 2018)
- 6-month average: 16
- Z-score: +3.0

**VIX mean reversion characteristics:**

- Strongest mean reversion in any futures market
- Half-life: ~5 days during spikes
- Reversion probability from >30: 90%+ within 30 days

**Trade:**

- Short VX January futures at 28
- Target: 18
- Stop: 35

**Execution:**

| Date | VIX | VX Jan | Action |
|------|-----|--------|--------|
| Dec 26 | 30 | 28 | Enter short |
| Jan 3 | 22 | 21 | Hold |
| Jan 10 | 18 | 17 | Exit |

**Result:**

- Gain: 11 points × $1,000 = $11,000 per contract

**Key lesson:** VIX mean reversion is the most reliable (but requires understanding term structure).

---

## Risk Management

### 1. Position Sizing Rules

**The cardinal rule:**

$$
\text{Risk per trade} \leq 1-2\% \text{ of account}
$$

**Why smaller for mean reversion:**

- Trades can move further against before reverting
- Need room for averaging down (if planned)
- Drawdown control is critical

**Example:**

- Account: $250,000
- Max risk: 1.5% = $3,750
- ES volatility stop: 80 points
- Max position: $3,750 / (80 × $50) = 0.94 → 1 contract

### 2. Maximum Exposure Limits

**Aggregate risk management:**

| Constraint | Limit |
|------------|-------|
| Single position | 2% of account |
| Single sector | 5% of account |
| Total mean reversion exposure | 10% of account |
| Correlated positions | 3% combined |

### 3. Regime Change Detection

**When to abandon mean reversion:**

**Warning signs:**

1. Z-score exceeds -4 or +4 (tail event)
2. Fundamental news justifying new level
3. Central bank policy shift
4. War, pandemic, or other regime change

**Action:**

- Cut position by 50% immediately
- Widen stops to avoid whipsaw
- Reassess whether mean has shifted

### 4. Correlation Risk

**Multiple mean reversion positions:**

If all positions are "buy the dip" in correlated assets:

$$
\text{Portfolio Risk} >> \text{Sum of Individual Risks}
$$

**Example:**

- Long ES (equity oversold)
- Long CL (oil oversold)
- Long HG (copper oversold)

**Problem:** All three may be oversold due to same cause (recession fear). If recession materializes, all three continue down together.

**Solution:** Limit correlated exposure, include offsetting positions (e.g., long ZN as hedge).

### 5. Liquidity Risk

**Mean reversion often occurs during stress:**

During market stress:
- Bid-ask spreads widen
- Slippage increases
- Stop orders may gap through

**Protection:**

- Trade only liquid contracts (ES, ZN, GC, CL)
- Avoid thin markets (small-cap futures, exotic commodities)
- Use limit orders for entry, accept wider stops

---

## Common Errors

### 1. Catching Falling Knives

**The error:**

- Price drops 5%
- "This must be oversold!"
- Enter immediately
- Price drops another 10%

**Why it fails:**

Z-score alone doesn't confirm reversal is starting.

**Correct approach:**

- Wait for confirmation (RSI turning, price stabilizing)
- Scale in gradually
- Have predefined maximum exposure

### 2. Ignoring Regime Changes

**The error:**

- Historical mean: $100
- Price drops to $70 (z = -3)
- Enter long expecting reversion
- Company announces bankruptcy
- Price goes to $10

**Why it fails:**

Mean reversion assumes stable distribution. Regime changes shift the mean.

**Correct approach:**

- Check for fundamental news explaining the move
- If structural change, mean has shifted
- Don't fight paradigm shifts

### 3. No Stop Loss

**The error:**

- Enter long at z = -2
- Price continues to z = -3
- "It will come back, just wait"
- Price continues to z = -4
- Catastrophic loss

**Why it fails:**

Without stops, one extreme move can destroy account.

**Correct approach:**

- Always have predefined stop
- Z-score invalidation level (e.g., z = -3.5 for z = -2 entry)
- Accept that mean reversion fails sometimes

### 4. Oversizing at Extremes

**The error:**

- "This is so oversold, it HAS to bounce!"
- Enter maximum position
- Price continues against
- No room to average or hold

**Why it fails:**

Confidence is not the same as edge. More extreme ≠ certain reversion.

**Correct approach:**

- Start with smaller position at first signal
- Reserve capacity for further extremes
- Maximum position only at most extreme levels

### 5. Exiting Too Early

**The error:**

- Enter long at z = -2.5
- Price bounces to z = -1.5
- "Good enough, take profit"
- Price continues to z = +0.5

**Why it fails:**

Left 50%+ of potential profit on table.

**Correct approach:**

- Scale out gradually
- Keep some position until mean reached
- Use trailing stops for final portion

### 6. Fighting Strong Trends

**The error:**

- Market in strong uptrend
- Every pullback looks "oversold"
- Short at z = +2
- Price continues to z = +4

**Why it fails:**

Strong trends can stay "overbought/oversold" for extended periods.

**Correct approach:**

- Trade mean reversion against weak trends
- Trade momentum WITH strong trends
- Identify trend strength before mean reversion entry

---

## Mean Reversion vs. Momentum

**Understanding when each strategy works:**

### 1. Regime Identification

| Regime | Characteristics | Strategy |
|--------|-----------------|----------|
| Trending | Autocorrelation > 0, ADX > 25 | Momentum |
| Range-bound | Autocorrelation < 0, ADX < 20 | Mean reversion |
| Transitional | Mixed signals | Reduce exposure |

### 2. When Mean Reversion Works Best

**Ideal conditions:**

- Sideways or slowly trending markets
- Stable volatility regime
- No significant fundamental news
- Extreme z-scores (>2 or <-2)
- Confirmation of reversal starting

**Market types:**

- VIX futures (strongest mean reversion)
- Interest rate futures (Fed-anchored)
- Commodity spreads (arbitrage-enforced)

### 3. When Mean Reversion Fails

**Avoid mean reversion when:**

- Strong momentum in place
- Fundamental regime shift
- Central bank policy changing
- War, pandemic, or crisis unfolding
- Volatility exploding (VIX > 35)

### 4. Combining Strategies

**Optimal approach:**

$$
\text{Portfolio} = w_{\text{MR}} \times \text{Mean Reversion} + w_{\text{MOM}} \times \text{Momentum}
$$

**Weights based on regime:**

| Market Condition | w_MR | w_MOM |
|-----------------|------|-------|
| Trending | 30% | 70% |
| Range-bound | 70% | 30% |
| Transitional | 50% | 50% |

---

## Final Wisdom

> "Mean reversion is the most mathematically sound futures strategy—price extremes have statistical pull toward average. But statistics require sample size: one trade proves nothing, but 50 trades reveal the edge. The key is discipline: enter only at extremes (z > 2), exit at stops or targets, and never let ego override math. The market doesn't care about your thesis; it only cares about supply and demand. When stretched rubber bands snap back, you profit. When means shift, you lose. Know the difference. Use futures for direct exposure—no premium decay, no gamma complexity, just pure price capture. Size positions for the worst case, not the expected case. Accept that 30% of mean reversion trades will fail, and some will fail spectacularly during regime changes. The edge comes from the 70% that work, multiplied by disciplined risk management that prevents the 30% from destroying you."

**Key to success:**

- Wait for extremes (z > 2 or z < -2)
- Confirm reversal starting (don't catch falling knives)
- Size based on volatility (not conviction)
- Scale in at deeper extremes (average down systematically)
- Exit at mean or better (scale out gradually)
- Hard stop at invalidation level (z > 3.5 = regime change likely)
- Recognize regime changes (mean shifts happen)

**Most important:** Mean reversion is a statistical edge, not a guarantee. You will have losing trades—sometimes several in a row during trending markets. Position sizing and stop discipline determine if you survive to see the edge play out over hundreds of trades. Futures provide the most capital-efficient way to capture mean reversion: direct linear exposure, no decay, and margin efficiency that lets you diversify across multiple mean reversion opportunities simultaneously. 📊🔄🎯
