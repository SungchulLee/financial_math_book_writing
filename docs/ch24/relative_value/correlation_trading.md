# Correlation Trading

**Correlation trading** is the practice of taking directional or relative value positions on the correlation structure between assets, profiting from changes in how assets move together or independently.

---

## The Core Insight

**The fundamental idea:**

- Asset correlations vary over time (not constant)
- High correlation in crises (flight to quality)
- Low correlation in normal times (dispersion)
- Correlation is tradeable (via options, swaps, futures)
- Mean-reverting but regime-dependent
- Multiple forms: equity, FX, rates, cross-asset

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/correlation_trading.png?raw=true" alt="correlation_trading" width="700">
</p>
**Figure 1:** Time series of SPX realized correlation showing mean reversion around 40-50% with spikes to 80%+ during crises, illustrating the cyclical nature of correlation and trading opportunities.

**You're essentially betting: "Correlation will increase/decrease from current levels, and I can profit from that change."**

---

## What Is Correlation Trading?

### 1. Basic Definition

**Correlation between two assets:**

$$
\rho_{12} = \frac{\text{Cov}(r_1, r_2)}{\sigma_1 \sigma_2} = \frac{\mathbb{E}[(r_1 - \mu_1)(r_2 - \mu_2)]}{\sigma_1 \sigma_2}
$$

Where:
- $r_1, r_2$ = Returns of assets 1 and 2
- $\sigma_1, \sigma_2$ = Volatilities of assets 1 and 2
- $\rho_{12} \in [-1, 1]$

**Properties:**
- $\rho = +1$: Perfect positive correlation (move together)
- $\rho = 0$: No correlation (independent)
- $\rho = -1$: Perfect negative correlation (move opposite)

**Average correlation (portfolio):**

$$
\bar{\rho} = \frac{2}{N(N-1)} \sum_{i<j} \rho_{ij}
$$

### 2. Implied vs Realized Correlation

**Implied correlation:**

Backed out from option prices using:

$$
\rho^{\text{implied}} = \frac{\sigma_{\text{index}}^2 - \sum w_i^2 \sigma_i^2}{2 \sum_{i<j} w_i w_j \sigma_i \sigma_j}
$$

**Realized correlation:**

Computed from historical returns:

$$
\rho_{ij}^{\text{realized}} = \frac{\sum_{t=1}^T (r_{i,t} - \bar{r}_i)(r_{j,t} - \bar{r}_j)}{\sqrt{\sum (r_{i,t} - \bar{r}_i)^2 \sum (r_{j,t} - \bar{r}_j)^2}}
$$

**Trading opportunity when:**

$$
\rho^{\text{implied}} \neq \rho^{\text{realized}}
$$

### 3. Why Correlation Changes

**Regime shifts:**

**Normal markets:**
- Correlation: 30-50%
- Stock-picking works
- Fundamentals matter
- Diversification works

**Crisis markets:**
- Correlation: 70-90%
- Everything moves together
- Risk-on/risk-off dominates
- Diversification fails

**Drivers of correlation changes:**

1. **Volatility regime:**
   - High vol → High correlation
   - Low vol → Low correlation
   - Mechanical relationship

2. **Market stress:**
   - Liquidity crunch → Forced selling → High correlation
   - Calm → Selective buying → Low correlation

3. **Macro vs. Micro:**
   - Macro dominance → High correlation (everyone reacts to Fed)
   - Micro dominance → Low correlation (company-specific news)

4. **Information flow:**
   - Common shocks → High correlation
   - Idiosyncratic news → Low correlation

### 4. Correlation Products

**Ways to trade correlation:**

**Variance swaps (indirect):**
- Short index variance + Long stock variances = Long dispersion
- Implicit correlation bet

**Correlation swaps (direct):**
- Payoff: $N \times (\rho^{\text{realized}} - K_\rho)$
- Direct exposure to correlation level
- Less common, illiquid

**Options on correlation:**
- Call/put options on correlation index
- Defined risk correlation bets
- Very illiquid

**Synthetic (straddles):**
- Index straddles vs. stock straddles
- Delta-hedge and manage gamma
- Most liquid approach

### 5. Historical Patterns

**Empirical evidence (SPX, 1996-2023):**

**Average realized correlation:**
- Normal: 35-45%
- Bull markets: 25-35%
- Bear markets: 60-80%
- Crashes: 80-95%

**Mean reversion:**
- Half-life: ~3-6 months
- Reverts to 40% long-term average
- Faster reversion from extremes

**Predictability:**
- High correlation predicts low future correlation (weakly)
- VIX level strong predictor (negative relationship)
- Term structure shape informative

**Asymmetry:**
- Correlation rises faster than it falls
- Spikes during crashes (days)
- Normalizes slowly (months)

### 6. Correlation vs Volatility

**Strong empirical relationship:**

$$
\rho_t \approx \alpha + \beta \times \text{VIX}_t
$$

**Typical values:**
- $\alpha \approx 0.15$ (15% when VIX = 0)
- $\beta \approx 0.015$ (1.5% correlation per VIX point)

**Example:**
- VIX = 15 → Predicted $\rho = 15\% + 1.5\% \times 15 = 37.5\%$
- VIX = 50 → Predicted $\rho = 15\% + 1.5\% \times 50 = 90\%$

**Implication:**
- Can't separate correlation from volatility completely
- Trading correlation = Trading vol regime

### 7. Cross-Asset Correlation

**Beyond equities:**

**FX correlations:**
- EUR/USD vs. GBP/USD: 0.6-0.8 (typical)
- Risk-on: Lower correlation (carry trades diverse)
- Risk-off: Higher correlation (flight to USD)

**Equity-Bond correlation:**
- Normal: -0.2 to -0.4 (diversification)
- Crisis: -0.6 to -0.8 (flight to quality)
- Inflation fears: +0.2 to +0.4 (both fall)

**Commodity correlations:**
- Oil vs. Copper: 0.5-0.7 (growth proxy)
- Gold vs. Silver: 0.7-0.9 (precious metals)
- During USD moves: All rise/fall together

---

## Correlation Trade Strategies

**How to profit from correlation:**

### 1. Long Correlation Trade

**Betting correlation will rise:**

**Setup:**
- Buy index volatility (index variance swap or straddles)
- Sell stock volatility (stock variance swaps or straddles)
- Net: Long correlation

**When to use:**
- Correlation at historical lows (< 30%)
- Crisis brewing (geopolitical, financial)
- Market transitioning risk-on → risk-off
- VIX rising

**Example:**
- Buy SPX variance swap, strike = 400 (20% vol)
- Sell 10 stock variances, avg strike = 625 (25% vol)
- If correlation rises 40% → 70%:

**P&L:**
- Index variance realizes 900 (30% vol)
- Stock variances realize 800 (avg 28% vol)
- Index leg: $\$1,000 × (900 - 400) = +\$500,000$
- Stock leg: $\$100 × 10 × (800 - 625) = +\$175,000$
- **Net: +$\$675,000$**

### 2. Short Correlation Trade

**Betting correlation will fall:**

**Setup:**
- Sell index volatility
- Buy stock volatility
- Net: Short correlation (dispersion trade)

**When to use:**
- Correlation elevated (> 60%)
- Post-crisis normalization
- Market transitioning risk-off → risk-on
- VIX falling

**Example:**
- Sell SPX variance, strike = 625 (25% vol, elevated)
- Buy stocks, avg strike = 900 (30% vol)
- If correlation falls 70% → 40%:

**P&L:**
- Index realizes 400 (20% vol)
- Stocks realize 750 (avg 27% vol)
- Index: $\$1,000 × (625 - 400) = +\$225,000$
- Stocks: $\$100 × 10 × (750 - 900) = -\$150,000$
- **Net: +$\$75,000$**

### 3. Correlation Spreads

**Relative value on correlation:**

**Setup:**
- Long correlation in one sector
- Short correlation in another sector
- Bet on relative correlation changes

**Example:**
- Short tech sector correlation (high, expected to fall)
- Long financials correlation (low, expected to rise)

**When financials hit by regulation:**
- Financials correlation spikes
- Tech correlation stable or falls
- **Profit on spread widening**

### 4. Correlation Mean Reversion

**Fade extremes:**

**Setup:**
- When correlation > 70%, go short correlation
- When correlation < 30%, go long correlation
- Bet on reversion to 40-50% mean

**Example:**
- Post-crisis: $\rho = 75\%$ (extreme high)
- Short correlation (dispersion trade)
- Over 6 months, $\rho \to 45\%$
- **Profit from mean reversion**

**Risk:**
- Correlation can stay extreme longer than you can stay solvent
- Use time stops (exit after 3-6 months regardless)

### 5. Event-Driven Correlation

**Trade around events:**

**Before major events:**
- Correlation tends to rise (uncertainty)
- Long correlation before FOMC, elections, Brexit
- Exit right after event

**After events:**
- Correlation tends to fall (clarity)
- Short correlation after resolution
- Harvest normalization

**Example:**
- 2 weeks before election: Long correlation
- Day after election: Flip to short correlation
- **Profit from cycle**

### 6. Volatility-Adjusted Correlation

**Account for vol regime:**

**Setup:**
- Adjust correlation target by VIX level
- Don't short correlation when VIX > 30
- Don't long correlation when VIX < 12

**Dynamic rule:**

$$
\text{Position} = \begin{cases}
\text{Long } \rho & \text{if } \rho < 0.3 + 0.01 \times \text{VIX} \\
\text{Flat} & \text{if middle} \\
\text{Short } \rho & \text{if } \rho > 0.5 + 0.01 \times \text{VIX}
\end{cases}
$$

### 7. Cross-Asset Correlation

**Trade correlation between asset classes:**

**Equity-Bond correlation:**
- Typically negative (diversification)
- Goes positive during stagflation

**Trade:**
- When $\rho_{\text{Equity-Bond}} < -0.5$, bet on rise
- When $\rho_{\text{Equity-Bond}} > -0.2$, bet on fall

**FX correlation:**
- EUR/USD vs. GBP/USD typically 0.7
- During Brexit uncertainty, fell to 0.3
- Long correlation trade (bet on reversion to 0.7)

---

## Mathematical Framework

### 1. Correlation Dynamics

**Stochastic correlation model:**

$$
d\rho_t = \kappa(\theta - \rho_t)dt + \sigma_\rho \sqrt{\rho_t(1-\rho_t)} dW_t
$$

Where:
- $\kappa$ = Mean reversion speed (~0.5-1.0 annually)
- $\theta$ = Long-term mean (~0.40)
- $\sigma_\rho$ = Vol of correlation (~0.3-0.5)

**Bounded between -1 and 1 (by construction)**

### 2. Index Variance Decomposition

**Exact formula:**

$$
\sigma_{\text{index}}^2 = \sum_{i=1}^N w_i^2 \sigma_i^2 + 2\sum_{i<j} w_i w_j \rho_{ij} \sigma_i \sigma_j
$$

**Simplified (equal weights):**

$$
\sigma_{\text{index}}^2 = \frac{1}{N}\bar{\sigma}^2 + \frac{N-1}{N}\bar{\rho}\bar{\sigma}^2
$$

**Rearranging for correlation:**

$$
\bar{\rho} = \frac{N \sigma_{\text{index}}^2 - \bar{\sigma}^2}{(N-1)\bar{\sigma}^2}
$$

### 3. Correlation Risk Premium

**Expected return from shorting correlation:**

$$
\mathbb{E}[\text{Return}] = \lambda_\rho \times \sigma_\rho \times \text{Notional}
$$

Where:
- $\lambda_\rho$ = Sharpe ratio of correlation trades (~0.2-0.4)
- $\sigma_\rho$ = Vol of correlation (~30%)

**Empirical:**
- Average excess return: 3-5% annually
- Std dev: 15-20%
- **Sharpe: 0.2-0.3 (modest)**

### 4. Greeks Exposure

**For dispersion (short correlation):**

**Correlation delta:**

$$
\frac{\partial P\&L}{\partial \rho} = -N_{\text{index}} \times 2\bar{\sigma}^2 \sum_{i<j} w_i w_j
$$

**Volatility vega (net):**

$$
\text{Vega}_{\text{net}} \approx 0 \quad \text{(if vega-hedged)}
$$

**Gamma (net):**

$$
\Gamma_{\text{net}} = \sum \Gamma_i - \Gamma_{\text{index}} > 0
$$

**Positive net gamma (benefits from realized vol)**

### 5. Optimal Hedge Ratio

**Minimize P&L variance:**

$$
h^* = \frac{\text{Cov}(\sigma_{\text{index}}, \bar{\sigma}_{\text{stocks}})}{\text{Var}(\bar{\sigma}_{\text{stocks}})}
$$

**Empirically:**

$$
h^* = \frac{\bar{\rho} \times \sigma_{\text{index}}}{\bar{\sigma}_{\text{stocks}}} \approx 0.6\text{-}0.8
$$

**Not 100% due to correlation risk premium**

### 6. Correlation Carry

**Expected P&L from correlation term structure:**

$$
\text{Carry} = \rho^{\text{implied}}_{\text{short-term}} - \rho^{\text{implied}}_{\text{long-term}}
$$

**Typical:**
- Short-term implied correlation: 55%
- Long-term implied correlation: 45%
- **Carry: +10% correlation points**

**Harvest by:**
- Short short-term correlation
- Long long-term correlation

### 7. Correlation Beta

**Sensitivity to market factors:**

$$
\rho_t = \alpha + \beta_{\text{VIX}} \times \text{VIX}_t + \beta_{\text{Vol}} \times \bar{\sigma}_t + \epsilon_t
$$

**Empirical estimates:**
- $\beta_{\text{VIX}} \approx 0.015$ (1.5% per VIX point)
- $\beta_{\text{Vol}} \approx 0.8$ (correlation rises with volatility)

**Use for forecasting:**
- Given VIX = 20, $\bar{\sigma} = 25\%$
- Predicted $\rho \approx 0.15 + 0.015 \times 20 + 0.8 \times 0.25 = 65\%$

---

## Common Mistakes

**Pitfalls to avoid:**

### 1. Assuming Stable Correlation

**Mistake:** Treat correlation as constant

**Why it fails:** Correlation highly time-varying

**Example:**
- Long-term average: 40%
- Enter dispersion assuming 40% will persist
- Crisis hits, $\rho \to 85\%$
- **Massive loss**

**Fix:**
- Monitor correlation daily
- Exit when correlation > 60% (2 std dev from mean)
- Don't fight regime changes

### 2. Ignoring Vol-Correlation Link

**Mistake:** Trade correlation without considering volatility

**Why it fails:** $\rho$ and $\sigma$ strongly correlated

**Example:**
- Short correlation at $\rho = 50\%$, VIX = 15
- VIX spikes to 40
- Correlation mechanically rises to 75%
- **"Correlation rose due to vol, not fundamentals"**

**Fix:**
- Adjust correlation trades for VIX level
- Scale position inversely with VIX
- Exit correlation shorts when VIX > 30

### 3. Overleveraging

**Mistake:** Large correlation notional

**Why it fails:** Correlation moves can be huge

**Example:**
- $\$5M$ correlation notional
- Correlation moves 30% (40% → 70%)
- Loss: $\$5M \times 30\% \times 2 = \$3M$

**Fix:**
- Max 10% portfolio in correlation trades
- Size for 20-30% correlation moves
- Reduce leverage in elevated vol regimes

### 4. Poor Timing

**Mistake:** Short correlation right after spike

**Why it fails:** Correlation persistence

**Example:**
- Correlation spikes 40% → 75% (crisis)
- "Must mean-revert, short it now"
- Stays at 70-80% for months
- **Continued losses**

**Fix:**
- Wait for correlation to fall back below 60%
- Don't catch falling knives
- Use time stops (exit after 3 months if no profit)

### 5. Ignoring Sector Correlation

**Mistake:** Assume all stocks have same correlation

**Why it fails:** Sector correlations differ

**Example:**
- Tech stocks: correlation 60%
- Utilities: correlation 40%
- Mix both in basket
- **Correlation estimate wrong, hedging off**

**Fix:**
- Stick to one sector for clean trades
- Or compute sector-adjusted correlation
- Don't mix low-correlation and high-correlation stocks

### 6. Forgetting Hedging Costs

**Mistake:** Ignore daily delta hedging friction

**Why it fails:** Costs compound quickly

**Example:**
- 20 stock positions, hedge daily
- 0.5% cost per hedge × 20 × 252 days = 252%/year
- **Eats all profit!**

**Fix:**
- Model costs before entering
- Hedge every 2-3 days (not daily)
- Use larger position sizes (lower per-unit costs)

### 7. No Exit Plan

**Mistake:** Hold correlation trade to maturity

**Why it fails:** Correlation can stay extreme

**Example:**
- Short correlation at 50%
- Spikes to 70%, down 40%
- Hold hoping for mean reversion
- Expires at 70%, full loss

**Fix:**
- Stop-loss at 20% loss
- Time stop: exit at 50% of duration
- Take profit at 10% gain (correlation mean-reverts slowly)

### 8. Misunderstanding Correlation Products

**Mistake:** Treat dispersion = pure correlation bet

**Why it fails:** Dispersion has vol exposure too

**Example:**
- Short dispersion (thinking short correlation)
- Both index vol and stock vol rise
- Lose on volatility exposure, not just correlation

**Fix:**
- Understand dispersion = correlation + vol
- For pure correlation, need correlation swaps (illiquid)
- Or use vol-adjusted dispersion strategies

---

## Risk Management Rules

### 1. Position Sizing

**Maximum allocation:**

$$
\text{Max Notional} = \frac{\text{Portfolio} \times 0.05}{\text{Max Correlation Move}}
$$

**Example:**
- $\$10M$ portfolio
- Max correlation move: 25% (e.g., 40% → 65%)
- **Max notional:** $\$10M \times 0.05 / 0.25 = \$2M$

**Rule of thumb:**
- Max 10% portfolio in correlation trades
- 5% safer for retail

### 2. Entry Conditions

**Long correlation (bet on increase):**
- Current $\rho < 35\%$ (low)
- VIX rising or > 20
- Crisis indicators flashing
- No recent spike (avoid persistence)

**Short correlation (bet on decrease):**
- Current $\rho > 55\%$ (high)
- VIX falling or < 20
- Post-crisis normalization
- No major events imminent

**Avoid when:**
- $\rho$ near 40-50% (mean, no edge)
- VIX > 35 (too risky)
- Major uncertainty (Brexit, elections during voting)

### 3. Stop-Loss Rules

**For short correlation:**
- **Realized $\rho > 65\%$ → Exit immediately**
- P&L loss > -20% → Exit
- VIX > 35 → Exit

**For long correlation:**
- **Realized $\rho < 30\%$ → Exit**
- P&L loss > -20% → Exit
- VIX < 12 → Exit

**Time stops:**
- Exit at 50% of trade duration if flat
- Don't hold to maturity hoping

### 4. Dynamic Hedging

**Adjust hedge ratio based on realized correlation:**

$$
h(t) = h_{\text{base}} \times \left(1 + k \times \frac{\rho_t - \rho_0}{\rho_0}\right)
$$

**Example:**
- Base hedge ratio: 70%
- $k = 0.5$ (adjustment factor)
- $\rho_0 = 40\%$, current $\rho_t = 50\%$

**New hedge:**
$$
h(t) = 0.70 \times \left(1 + 0.5 \times \frac{50 - 40}{40}\right) = 0.70 \times 1.125 = 78.75\%
$$

### 5. Monitoring

**Daily checklist:**
- Realized correlation (20-day rolling)
- Implied correlation (from option prices)
- VIX level and change
- Delta of all positions
- Upcoming events

**Weekly review:**
- P&L attribution (correlation vs. vol)
- Position Greeks
- Rebalance if needed
- Check stop-loss triggers

### 6. Diversification

**Spread risk across:**
- Multiple markets (US, Europe, Asia)
- Multiple sectors (tech, financials, healthcare)
- Multiple maturities (1M, 3M, 6M)
- Mix with other strategies (VRP, carry)

**Correlation between correlation trades:**
- Same market: 0.8-0.9 (high)
- Different markets: 0.5-0.6 (moderate)
- Still benefits from diversification

### 7. Hedging Tail Risk

**For short correlation positions:**
- Buy OTM index calls (hedge against correlation spike)
- Cost: 0.3-0.5% of notional
- Caps losses when correlation explodes

**Example:**
- Short $\$2M$ correlation exposure
- Buy 20% OTM SPX calls
- Cost: $\$10,000$
- Max loss: $\$500,000$ (capped vs. unlimited)

---

## Real-World Examples

### 1. Brexit Vote (June 2016)

**Setup:**
- Pre-Brexit: Correlation at 45% (normal)
- Uncertainty rising
- Long correlation trade

**Trade:**
- Buy index variance (SPX and FTSE)
- Sell stock variances
- $\$500,000$ notional

**Outcome:**
- Brexit passed (surprise)
- Correlation spiked 45% → 75%
- Index vol exploded, stock vol rose less
- **Profit: $\$375,000$ (75%)**

**Lesson:** Long correlation before major binary events

### 2. Post-2008 Normalization (2010-2011)

**Setup:**
- 2009: Correlation at 80% (crisis peak)
- 2010: Starting to normalize
- Short correlation trade

**Trade:**
- Short dispersion on SPX
- Start when $\rho = 65\%$ (May 2010)

**Outcome:**
- Correlation fell 65% → 38% over 18 months
- Steady profits each quarter
- **Total return: +45%**

**Lesson:** Post-crisis normalization ideal for short correlation

### 3. COVID Crash (March 2020)

**Setup:**
- Feb 2020: Correlation at 40%
- Short correlation position on

**Event:**
- March crash: Correlation spiked 40% → 82%

**Outcome:**
- Index variance exploded
- Stock variances rose but less
- **Loss: -65%** (without stop-loss)

**Disciplined trader:**
- Stop-loss at $\rho = 60\%$
- Exit in early March
- Loss contained: -18%

**Lesson:** Stop-losses essential for correlation trades

### 4. Tech Bubble Burst (2000-2001)

**Setup:**
- Late 1999: Tech stocks highly correlated (bubble)
- $\rho_{\text{tech}} = 70\%$
- Short tech correlation

**Trade:**
- Short Nasdaq correlation
- Long individual tech stock volatility

**Outcome:**
- Bubble burst (selective)
- Some stocks crashed, others held
- Correlation fell 70% → 40%
- **Profit: +55%** over 12 months

**Lesson:** Bubble bursts often reduce correlation

---

## Practical Steps

### 1. Measuring Correlation

**Calculate realized correlation:**

```python
import numpy as np
import pandas as pd

# Get stock returns
returns = pd.DataFrame({'stock1': r1, 'stock2': r2})

# Compute correlation matrix
corr_matrix = returns.corr()

# Average correlation
avg_corr = corr_matrix.values[np.triu_indices_from(corr_matrix.values, 1)].mean()
```

**Implied correlation:**
- Get index ATM vol: $\sigma_{\text{idx}}$
- Get stock ATM vols: $\sigma_1, \sigma_2, \ldots$
- Compute weighted average: $\bar{\sigma}$
- Back out implied correlation

### 2. Entry Analysis

**Before entering:**

1. **Check correlation level:**
   - Current realized: compute from returns
   - Historical percentile (where in distribution?)
   - Mean: ~40%, 1 std dev: ±15%

2. **Assess regime:**
   - VIX level (< 20 or > 20?)
   - Recent trend (rising or falling?)
   - Upcoming events

3. **Calculate edge:**
   - Implied vs. realized gap
   - Need > 10% gap for trade
   - Larger gap = better opportunity

### 3. Position Construction

**For short correlation:**

- Sell index variance or straddles
- Buy stock variance or straddles (weighted)
- Hedge ratio: 70% of index vega

**Example:**
- Sell 5 SPX variance swaps at 400
- Buy 50 stock variance (10 names × 5 each)
- Check vega: Index $\$50k$, stocks $\$35k$ (70%)

### 4. Execution

**Enter positions:**
- Use limit orders (never market)
- Stagger over 2-3 days
- Check liquidity (volume > 1,000)
- Monitor bid-ask (< 5% of mid)

**Example:**
- Day 1: Sell 2 SPX variance
- Day 2: Buy 20 stock variances
- Day 3: Sell 3 more SPX, buy 30 more stocks

### 5. Management

**Daily tasks:**
- Compute realized correlation
- Check P&L attribution
- Delta-hedge if needed
- Monitor VIX

**Weekly tasks:**
- Rebalance delta
- Adjust hedge ratio if $\rho$ changed
- Check upcoming events
- Review stop-losses

### 6. Exit Execution

**Exit when:**

**Short correlation:**
- Realized $\rho > 60\%$ (stop-loss)
- Profit > 15% (take some off)
- 3 months elapsed (time stop)

**Long correlation:**
- Realized $\rho < 30\%$ (stop-loss)
- Profit > 20% (take half)
- Crisis resolved

**Exit process:**
- Close all legs simultaneously
- Use limit orders
- Don't leave one leg open (correlation risk!)

---

## Final Wisdom

> "Correlation trading is the art of betting on how assets move together - a subtle but powerful concept that drives portfolio diversification, risk management, and volatility arbitrage. Correlation is mean-reverting around 40% but spikes violently during crises, rising from 30% to 80% in days. The key to success is recognizing correlation regimes: short when elevated after crises, long when depressed before events, and always respect the correlation-volatility link. This is not a 'set and forget' trade - it requires constant monitoring, disciplined stops, and the humility to exit when the regime shifts against you."

**Key to success:**

- Understand correlation is time-varying and regime-dependent
- Short correlation when $\rho > 55\%$ and VIX falling
- Long correlation when $\rho < 35\%$ and VIX rising
- Position size for 25% correlation moves (max 10% portfolio)
- Hard stop-loss when realized correlation crosses 60% (short) or 30% (long)
- Adjust for VIX level (correlation and volatility linked)
- Monitor daily, rebalance weekly
- Remember: Correlation spikes faster than it normalizes
