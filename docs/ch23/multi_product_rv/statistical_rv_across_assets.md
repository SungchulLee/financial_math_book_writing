# Statistical RV Across Assets

**Statistical relative value across assets** uses quantitative models to identify and exploit mean-reverting price relationships between instruments across different asset classes—including pairs trading (two correlated stocks), basket arbitrage (index vs components), cross-commodity spreads (oil vs gas), and multi-asset statistical arbitrage—by estimating fair value relationships through cointegration, principal component analysis, or machine learning, then trading deviations with the expectation of reversion to the statistical equilibrium, generating alpha from temporary dislocations while managing the risk that relationships fundamentally break.

---

## The Core Insight

**The fundamental idea:**

- Historical price relationships encode information
- Statistical models identify "normal" relationships
- Deviations from normal create opportunities
- Mean reversion is testable (cointegration, half-life)
- No economic model required (purely statistical)
- Works across any asset classes with data
- Risk: Structural breaks (relationships change permanently)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/statistical_rv_framework.png?raw=true" alt="statistical_rv_framework" width="700">
</p>
**Figure 1:** Statistical relative value framework showing identification methods (cointegration testing, PCA factor extraction, machine learning clustering), signal generation (z-score, Kalman filter), position sizing (Kelly criterion, volatility scaling), and risk controls (half-life monitoring, correlation breakdown detection, structural break tests).

**You're essentially asking: "Can I find statistical patterns in price relationships and trade them profitably?"**

---

## What Is Statistical RV?

### 1. Pairs Trading

**Classic stat arb:**

**Concept:** Two historically correlated assets temporarily diverge

**Spread definition:**

$$
S_t = P_t^A - \beta \times P_t^B
$$

Where $\beta$ = hedge ratio (from regression)

**Trading signal:**

$$
z = \frac{S_t - \mu_S}{\sigma_S}
$$

**Rules:**
- If $z > 2$: Short spread (sell A, buy B)
- If $z < -2$: Long spread (buy A, sell B)
- If $|z| < 0.5$: Exit

**Example:**

Coca-Cola (KO) vs PepsiCo (PEP):
- Historical correlation: 0.85
- Current ratio: KO/PEP = 0.55
- Historical average: 0.60
- Z-score: -2.3 (KO cheap relative to PEP)

**Trade:**
- Buy $100K KO
- Short $100K PEP (dollar-neutral)
- Wait for ratio to revert to 0.60

### 2. Cointegration

**Statistical test for mean reversion:**

**Definition:**

Two non-stationary series are cointegrated if their linear combination is stationary

$$
P_t^A - \beta P_t^B = \epsilon_t
$$

Where $\epsilon_t$ is stationary (mean-reverting)

**Augmented Dickey-Fuller test:**

Test if $\epsilon_t$ has unit root:

$$
\Delta \epsilon_t = \alpha + \gamma \epsilon_{t-1} + \sum \beta_i \Delta \epsilon_{t-i} + u_t
$$

**If $\gamma < 0$ significantly:** Cointegrated (mean-reverting)

**Example:**

Gold (GLD) and gold miners (GDX):
- ADF test: t-stat = -4.2
- Critical value (5%): -2.86
- **Reject unit root** → Cointegrated ✓

**Trading:**
- Spread = GDX - 0.7 × GLD
- Mean reversion confirmed
- Half-life: 5 days (reverts in ~5 days)

### 3. Principal Component Analysis

**Factor extraction:**

**Method:** Decompose correlation matrix into eigenvectors

**Process:**
1. Collect returns for $n$ assets
2. Compute covariance matrix $\Sigma$
3. Find eigenvalues $\lambda_i$ and eigenvectors $v_i$
4. First PC: Direction of maximum variance

**Example—10 energy stocks:**

**PC1 (60% variance):**
- Loads heavily on all stocks (market factor)
- Eigenvector: [0.32, 0.31, 0.33, ...]

**PC2 (15% variance):**
- E&P vs refiners (sector factor)
- Eigenvector: [0.45, 0.40, -0.38, -0.42, ...]

**Trading:**
- Long stocks with high PC2 loading
- Short stocks with low PC2 loading
- Market-neutral (PC1-neutral)

### 4. Kalman Filter

**Dynamic hedge ratio estimation:**

**State-space model:**

$$
\begin{align}
\beta_t &= \beta_{t-1} + w_t \quad \text{(state equation)} \\
P_t^A &= \beta_t P_t^B + v_t \quad \text{(observation equation)}
\end{align}
$$

**Advantage:** Adapts to time-varying relationships

**Example:**

S&P 500 vs Nasdaq:
- Static beta (OLS): 1.15
- Kalman filter beta: 1.05-1.25 (time-varying)

**Trading:**
- Use dynamic beta for hedging
- Reduces tracking error by 30%

### 5. Machine Learning Clustering

**Unsupervised learning:**

**K-means clustering:**

1. Compute similarity (correlation, distance)
2. Group assets into $k$ clusters
3. Trade within-cluster deviations

**Example—100 stocks:**

**Cluster 1:** Tech growth (AAPL, MSFT, GOOGL)
**Cluster 2:** Value stocks (XOM, CVX, JPM)
**Cluster 3:** Defensive (JNJ, PG, KO)

**Trading:**
- Within cluster 1: If AAPL underperforms MSFT by 3σ
- Long AAPL, short MSFT
- Exploit intra-cluster mean reversion

### 6. Ornstein-Uhlenbeck Process

**Mean-reverting process:**

$$
dX_t = \theta(\mu - X_t)dt + \sigma dW_t
$$

Where:
- $\theta$ = Mean reversion speed
- $\mu$ = Long-run mean
- $\sigma$ = Volatility

**Half-life:**

$$
\tau_{1/2} = \frac{\ln(2)}{\theta}
$$

**Example:**

Gold-silver ratio:
- Mean: $\mu = 75$
- Speed: $\theta = 0.15$
- Half-life: $\ln(2)/0.15 = 4.6$ months

**Trading:**
- Current ratio: 90 (2σ above mean)
- Short gold, long silver
- Expected reversion time: 4.6 months

### 7. Cross-Sectional Momentum

**Relative strength:**

**Method:**
1. Rank assets by recent performance
2. Long top decile, short bottom decile
3. Rebalance monthly

**Example—S&P 500 stocks:**

**Monthly:**
- Rank by 3-month return
- Long top 50 stocks
- Short bottom 50 stocks
- Dollar-neutral, sector-neutral

**Statistical expectation:**
- Momentum persists 3-12 months
- Mean reversion beyond 12 months

---

## Key Terminology

**Cointegration:**
- Long-run equilibrium relationship
- Spread is stationary
- Essential for pairs trading
- Tested with ADF, Johansen

**Half-Life:**
- Time for 50% mean reversion
- Shorter = faster trading
- Typical: 1-30 days
- Too long = risky

**Z-Score:**
- Standardized deviation
- Z = (X - μ) / σ
- Trading trigger (|z| > 2)
- Normal distribution assumed

**PCA:**
- Principal Component Analysis
- Extracts common factors
- Reduces dimensionality
- Basis for factor models

**Kalman Filter:**
- Recursive estimation
- Adapts to time-varying parameters
- Optimal in linear case
- Used for dynamic hedging

**Sharpe Ratio:**
- Risk-adjusted return
- SR = μ / σ
- Stat arb target: 1.5-3.0
- Evaluated over full cycle

**Drawdown:**
- Peak-to-trough decline
- Max DD critical metric
- Stat arb: Expect 10-30%
- Recovery time matters

---

## Statistical RV Strategies

### 1. Classic Pairs Trading

**Implementation:**

**Universe:** S&P 500 stocks
**Method:** Rolling correlation, cointegration test

**Process:**
1. For each pair, test cointegration (last 252 days)
2. Calculate hedge ratio: $\beta = \text{Cov}(A,B) / \text{Var}(B)$
3. Compute spread: $S = A - \beta \times B$
4. Z-score: $(S - \mu_S) / \sigma_S$

**Entry:** |z| > 2
**Exit:** |z| < 0.5 or holding period > 20 days

**Example positions:**

**Pair 1:** JPM vs BAC
- Beta: 1.15
- Current spread: 2.3σ (JPM expensive)
- Trade: Short $100K JPM, long $115K BAC

**Pair 2:** WMT vs TGT
- Beta: 0.85
- Current spread: -2.1σ (WMT cheap)
- Trade: Long $100K WMT, short $85K TGT

**Portfolio:** 20-50 pairs simultaneously

### 2. Index Arbitrage

**Statistical vs fundamental:**

**Statistical approach:**
- Model index as sum of sectors (statistical weights)
- Trade when index deviates from model

**Example:**

S&P 500 statistical model:
- Input: 11 sector ETFs
- Regression weights (not market cap)
- Predicted: 4,495

**Actual:** 4,510
**Deviation:** +15 points (0.33%, 2.5σ)

**Trade:**
- Short index (SPY)
- Long sector basket (weighted by regression)
- Notional: $10M each side

**Expected:** Revert in 2-3 days

### 3. Cross-Commodity Spreads

**Energy complex:**

**Crack spread:** Crude oil → Gasoline + Heating oil

$$
\text{Crack} = 2 \times \text{RBOB} + \text{HO} - 3 \times \text{CL}
$$

**Statistical model:**
- Historical mean: $15
- Current: $8
- Z-score: -2.1

**Trade:**
- Long crack spread (buy products, sell crude)
- Notional: 100 contracts

**Spark spread:** Natural gas → Electricity

$$
\text{Spark} = \text{Electricity} - \text{Heat Rate} \times \text{Natural Gas}
$$

### 4. Volatility Surface Arbitrage

**Implied vol relationships:**

**Model:** ATM vol predicts OTM vol via smile

$$
\sigma_{\text{OTM}} = f(\sigma_{\text{ATM}}, K, \text{skew}, \text{kurtosis})
$$

**Statistical deviation:**

Expected 25-delta put vol: 23%
**Actual:** 26%
**Difference:** +3 vol points (1.5σ rich)

**Trade:**
- Sell 25-delta puts
- Buy ATM straddle (hedge)
- Collect mispricing

### 5. Multi-Asset PCA

**Cross-asset factors:**

**Universe:**
- 20 equity indices
- 10 bond indices
- 10 commodity futures
- 10 currency pairs

**PCA results:**
- PC1: Global risk-on/off (45% variance)
- PC2: USD strength (15% variance)
- PC3: Commodity cycle (10% variance)

**Trading:**
- Assets far from PC-predicted values = mispriced
- Long undervalued, short overvalued
- Factor-neutral exposure

### 6. Mean Reversion with Momentum

**Combine signals:**

**Short-term (1-5 days):** Mean reversion
**Medium-term (1-3 months):** Momentum

**Composite signal:**

$$
\text{Signal} = w_1 \times z_{\text{reversion}} + w_2 \times z_{\text{momentum}}
$$

**Example:**

Stock XYZ:
- 5-day return: -8% (z = -2.5, oversold)
- 3-month return: +15% (z = +1.8, momentum)
- Combined: Long signal

### 7. Regime-Switching Pairs

**Conditional on volatility regime:**

**Low vol (VIX < 15):**
- Pairs trade aggressively
- Tight stops (z = ±2)
- Higher leverage (2×)

**High vol (VIX > 25):**
- Reduce positions
- Wide stops (z = ±3)
- Lower leverage (1×)

**Adaptive:**
- Half-life shortens in high vol
- Adjust holding period dynamically

---

## Common Mistakes

### 1. Overfitting

**Too many parameters:**

- **Mistake:** Optimize strategy to perfection on historical data
- **Why it fails:** Fit to noise, not signal
- **Fix:** Out-of-sample testing, simplicity
- **Real cost:** Strategy fails live trading

**Example:**

Backtest pairs strategy:
- In-sample (2010-2020): Sharpe 3.2
- Optimize entry/exit levels, holding period, pair selection
- Live trading (2021): Sharpe 0.4
- **Overfitting!**

### 2. Ignoring Transaction Costs

**High turnover kills:**

- **Mistake:** Strategy trades daily, ignore costs
- **Why it fails:** Bid-ask + commissions > edge
- **Fix:** Include all costs in backtest
- **Real cost:** 30-50% of gross returns

**Example:**

Pairs strategy:
- Gross return: 15% annually
- Turnover: 500% (5× portfolio annually)
- Costs: 2 bps each side × 500% × 2 = 20 bps × 10 = **2%**
- **Net return: 13%** (costs ate 13% of return!)

### 3. Structural Breaks

**Relationship changes permanently:**

- **Mistake:** Assume cointegration persists forever
- **Why it fails:** Business models change, tech disrupts
- **Fix:** Monitor cointegration tests rolling
- **Real cost:** Losses mount as relationship diverges

**Example:**

Retail pairs (2015):
- WMT vs TGT: Cointegrated (ADF = -4.5)
- Amazon disruption (2016-2020)
- Relationship breaks: ADF = -1.2 (not cointegrated)
- Pair diverges permanently
- **Losses: 15% before exit**

### 4. Regime Changes

**Market structure shifts:**

- **Mistake:** Use parameters estimated in low-vol regime
- **Why it fails:** High-vol regime has different dynamics
- **Fix:** Regime-dependent parameters
- **Real cost:** 20-40% excess drawdown

**Example:**

Pairs trading:
- Low vol (2017): Half-life = 3 days
- High vol (2020): Half-life = 15 days (mean reversion slower!)
- Strategy assumes 3-day reversion
- Positions exit too early in 2020
- **Missed profits, took small losses**

### 5. Look-Ahead Bias

**Using future information:**

- **Mistake:** Use end-of-day close for signals, execute at that close
- **Why it fails:** Can't trade at price you used for signal
- **Fix:** Signal at close, execute next day open
- **Real cost:** 100% of backtest profit disappears

**Example:**

Backtest shows:
- Return: 20% annually (using close-to-close)

**Reality:**
- Signal at close (e.g., 4:00 PM)
- Execute next open (9:30 AM)
- Overnight gap: 5 bps average
- **Actual return: 2%** (most profit was look-ahead bias)

### 6. Survivorship Bias

**Only using stocks that survived:**

- **Mistake:** Backtest on current index constituents
- **Why it fails:** Ignores delisted stocks (usually losers)
- **Fix:** Use point-in-time universe
- **Real cost:** 2-5% annual return overstatement

**Example:**

S&P 500 pairs (backtested):
- Using current 500 stocks: Sharpe 2.0
- Using point-in-time (includes delistings): Sharpe 1.4
- **30% overstatement** from survivorship bias

### 7. Leverage Miscalculation

**Underestimating risk:**

- **Mistake:** Use historical volatility for position sizing
- **Why it fails:** Vol spikes in crisis
- **Fix:** Size for stressed volatility (2× historical)
- **Real cost:** Margin calls, forced liquidation

**Example:**

Pair position:
- Historical vol: 5%
- Size for 10% annual vol: Levered 2×
- Crisis: Vol spikes to 25%
- Realized vol: 50% (2× leverage × 25%)
- **Margin call: Liquidate at worst time**

---

## Best vs. Worst Case

### 1. Best Case: Success

**Statistical arbitrage fund (2010-2020):**

**Setup:**
- Systematic pairs trading
- 100 stocks in universe
- Daily rebalancing

**Strategy:**
1. Test 4,950 pairs daily for cointegration
2. Select top 50 pairs by z-score magnitude
3. Enter at |z| > 2, exit at |z| < 0.5
4. Maximum holding: 20 days
5. Position size: 2% per pair (total 100% gross, 50% net)

**Risk management:**
- Daily cointegration test (exit if fails)
- Stop-loss: 3σ move against (per pair)
- Regime adjustment: Reduce leverage in VIX > 20

**2010-2020 Results:**

**Annualized:**
- Return: 18%
- Volatility: 8%
- Sharpe ratio: 2.25
- Max drawdown: -12% (March 2020)
- Win rate: 62%

**Best year (2013):** +28%
**Worst year (2020):** +8%

**Monthly performance:**

**Typical month:**
- 50 pairs active
- Average holding: 8 days
- 31 winners, 19 losers
- Return: +1.4%

**2020 COVID crisis (March):**
- Volatility spike: VIX 15 → 80
- Many pairs diverged temporarily
- Leverage reduced automatically (VIX rule)
- Positions: 25 pairs (vs. 50 normal)
- Several stopped out at 3σ
- **Month: -8%** (largest DD)

**Recovery (April-December 2020):**
- Pairs converged as volatility normalized
- **+16%** (recovered DD plus profits)

**10-year total:**
- Starting capital: $100M
- Ending capital: $475M
- **CAGR: 16.8%**

**Success factors:**
1. Robust methodology (cointegration, not correlation)
2. Diversification (50 pairs, not 5)
3. Risk management (stop-loss, regime adjustment)
4. Out-of-sample testing (validated before launch)
5. Transaction cost awareness (10 bps per trade assumed)

### 2. Worst Case: Disaster

**Statistical arbitrage blow-up (2007):**

**Setup:**
- Quant fund using PCA-based stat arb
- Highly levered (5×)
- No regime adjustment

**Strategy:**
- Extract 10 principal components from 200 stocks
- Trade deviations from PC-predicted prices
- Daily rebalancing
- Leverage: 5× gross, 2.5× net

**2003-2006: Golden years**

**Performance:**
- Returns: 25-35% annually
- Sharpe: 2.8
- Drawdowns: < 5%

**August 2007: Quant Quake**

**Week of August 6:**

**Monday:**
- Unusual pattern: All models showed same signals
- Reason: Crowded trades (many quants using similar models)
- Unwinding began (unknown trigger)
- **Day 1: -5%**

**Tuesday-Wednesday:**
- Massive deleveraging across industry
- Forced selling in same stocks
- Correlations → 1 (all pairs moved together)
- Mean reversion failed completely
- **Day 2-3: -12%**

**Thursday:**
- Margin calls from prime broker
- Forced to liquidate positions
- Executed at worst prices (everyone selling same stocks)
- **Day 4: -8%**

**Friday:**
- Continued liquidation
- **Day 5: -3%**

**Weekly total: -28%** (on 2.5× net leverage = -11% on gross)

**Aftermath:**

**Month-end:**
- Investors panicked
- Redemption requests: 40%
- Forced to sell at depressed prices
- Additional losses: -15%

**Total August loss: -43%**

**September-December:**
- Reduced leverage to 1×
- Strategies slow to recover
- Investor confidence shattered
- More redemptions

**2008:** Fund shut down

**Post-mortem:**
1. Crowded trades (everyone using PCA)
2. Excessive leverage (5× amplified losses)
3. No regime detection (ignored warning signs)
4. Liquidity mismatch (daily redemptions, illiquid stocks)
5. Correlation breakdown (all pairs failed simultaneously)

**Lessons:**
- Stat arb is crowded (competitive advantage erodes)
- Leverage kills (5× turns -8% into -40%)
- Models correlate (industry-wide risk)
- Mean reversion can fail for extended periods
- Redemption spiral amplifies losses

---

## Risk Management Rules

### 1. Position Sizing

**Per pair/spread:**

$$
\text{Position Size} = \frac{\sigma_{\text{target}}}{\sigma_{\text{spread}}} \times \text{Capital}
$$

**Example:**

Target vol: 10% annually
Spread vol: 15% annually
Capital: $10M

**Position:** $(0.10 / 0.15) \times 10M = $6.67M$

### 2. Leverage Limits

**Maximum gross leverage:**

$$
\text{Gross Leverage} \leq 3 \times \text{ in normal regime}
$$

$$
\text{Gross Leverage} \leq 1 \times \text{ in high-vol regime}
$$

**Regime definition:** VIX > 25 = high-vol

### 3. Stop-Loss Discipline

**Per pair:**

$$
\text{Stop Loss} = 3 \times \sigma_{\text{spread}}
$$

**Example:**

Spread std dev: 2%

**Stop-loss:** Exit if loss > 6%

### 4. Cointegration Monitoring

**Daily test:**

- Rolling 252-day ADF test
- If p-value > 0.05 (fails): Exit pair immediately
- Retest weekly for re-entry

### 5. Correlation Matrix

**Monitor pairwise correlations:**

$$
\text{If } \rho_{ij} > 0.8 \text{ for >50\% of pairs: Reduce leverage}
$$

**Indicates:** Crowded trades, correlation spike

### 6. Half-Life Check

**Monthly recalculation:**

$$
\tau_{1/2} = \frac{\ln(2)}{\theta}
$$

**If half-life > 30 days:** Exit pair (too slow)

**If half-life < 1 day:** Reduce size (too noisy)

### 7. Drawdown Circuit Breaker

**Maximum drawdown:**

$$
\text{If DD > 15\%: Reduce to 50\% positions}
$$

$$
\text{If DD > 25\%: Stop trading, review strategy}
$$

---

## Real-World Examples

### 1. Renaissance Technologies

**Medallion Fund (1988-present):**

**Approach:**
- Pure statistical arbitrage
- Thousands of positions
- High turnover (holding periods 1-2 days)
- Extremely secretive

**Reported performance:**
- CAGR: 66% before fees (1988-2018)
- Sharpe: ~6 (extraordinary)
- Closed to outside investors (1993)

**Key factors:**
- PhD scientists (not MBAs)
- Proprietary data sets
- Fastest execution technology
- Diversification (thousands of signals)

### 2. LTCM Statistical Arbitrage

**Not all stat arb, but some:**

**Convergence trades:**
- On-the-run vs off-the-run Treasuries
- Statistical mean reversion

**1998 failure:**
- Russia default → Correlations to 1
- Flight to quality
- Mean reversion failed
- Leverage amplified
- **Lost 90%**

### 3. Quant Quake (August 2007)

Described in Worst Case above.

**Industry-wide:** $100B+ lost in week

### 4. COVID Dislocation (March 2020)

**Stat arb opportunity:**

- Correlations spiked to 1 temporarily
- Pairs diverged 5-10σ
- Mean reversion failed for 2-3 weeks
- Then snapped back violently

**Winners:** Funds that survived without forced liquidation
**Losers:** Leveraged funds with margin calls

---

## Practical Steps

### 1. Data Collection

**Requirements:**
- Tick or minute data (for HFT)
- Daily data (for pairs trading)
- Clean data (adjust for splits, dividends)
- Survivorship-bias-free

**Minimum:** 5 years of daily data

### 2. Pair Selection

**Process:**

1. **Universe definition:** S&P 500, all stocks, etc.
2. **Correlation screening:** ρ > 0.7
3. **Cointegration testing:** ADF test, p-value < 0.05
4. **Half-life calculation:** 1 < τ < 30 days
5. **Liquidity filter:** ADV > $10M

**Result:** 50-200 tradeable pairs

### 3. Parameter Estimation

**For each pair:**

$$
\beta = \text{Cov}(A, B) / \text{Var}(B)
$$

$$
\mu_S = \text{Mean}(A - \beta \times B)
$$

$$
\sigma_S = \text{Std}(A - \beta \times B)
$$

**Rolling window:** 252 days (1 year)

### 4. Signal Generation

**Z-score:**

$$
z_t = \frac{(A_t - \beta B_t) - \mu_S}{\sigma_S}
$$

**Thresholds:**
- Enter: |z| > 2
- Exit: |z| < 0.5
- Stop: |z| > 3 (wrong direction)

### 5. Position Sizing

**Volatility-scaled:**

$$
\text{Shares}_A = \frac{\text{Target Risk} \times \text{Capital}}{\sigma_{\text{spread}} \times \beta}
$$

**Example:**

Capital: $1M
Target risk: 1% per pair
Spread vol: 10% annually
Beta: 1.2

**Shares A:** $(0.01 \times 1M) / (0.10 \times 1.2) = 83,333$ shares

### 6. Execution

**Best practices:**
- Simultaneous execution (both legs)
- Limit orders (avoid market impact)
- VWAP algorithms (large size)
- Time execution (avoid open/close)

### 7. Monitoring

**Daily:**
- P&L per pair
- Cointegration test
- Correlation matrix
- VIX (regime indicator)

**Weekly:**
- Recalculate parameters
- Review stopped-out pairs
- Add new pairs (if criteria met)

**Monthly:**
- Full backtest refresh
- Out-of-sample validation
- Parameter stability check

---

## Final Wisdom

> "Statistical relative value is the industrialization of pattern recognition—instead of finding one or two pairs intuitively, you systematically screen thousands of relationships, test them rigorously for cointegration, and trade them mechanically with strict risk management. Renaissance Technologies proved it can generate 66% annual returns for 30 years, but their edge comes from (1) proprietary data that retail can't access, (2) PhDs in mathematics finding obscure patterns, (3) nanosecond execution speed, and (4) absolute secrecy. For the rest of us, stat arb is a different game: you're competing against RenTech, Two Sigma, Citadel, and DE Shaw, all with billion-dollar technology budgets. The realistic Sharpe ratio for retail stat arb today is 1.0-1.5, not 6.0, and that's only if you avoid the seven deadly sins: overfitting (memorizing noise), ignoring costs (turnover kills), missing structural breaks (Blockbuster-Netflix), assuming stable regimes (2007 Quant Quake), look-ahead bias (using information you wouldn't have), survivorship bias (ignoring failures), and overleveraging (5× turns -10% into -50%). The August 2007 Quant Quake revealed stat arb's dark secret: when everyone uses PCA, everyone owns the same trades, and unwinding becomes a death spiral. Cointegration is the foundation—without it, you're not doing stat arb, you're gambling on correlation that can break overnight. Half-life matters: 5-day reversion is tradeable, 90-day reversion ties up capital too long. The deepest truth: mean reversion is real and testable, but it's a weak force—it works over thousands of trades with small edges (0.1-0.5% per trade), not on individual bets. Success requires diversification (50+ pairs), discipline (exit failed trades), and patience (Sharpe 1.5 over decades beats Sharpe 3.0 for 3 years then blow-up). For retail investors, the lesson isn't 'build your own stat arb system' but 'understand that market efficiency is enforced by thousands of quants running cointegration tests every millisecond'—which is why obvious mispricings don't exist."

**Key to success:**

- Test for cointegration rigorously (ADF p-value < 0.05)
- Diversify across 50+ pairs minimum (single pair = gambling)
- Size conservatively (1-2% risk per pair)
- Include ALL costs in backtest (2-5 bps per trade realistic)
- Monitor regime changes (VIX > 25 = reduce leverage)
- Use out-of-sample testing (last 20% of data reserved)
- Limit leverage (3× gross maximum, 1× in high vol)
- Stop-loss discipline (3σ adverse move = exit)
