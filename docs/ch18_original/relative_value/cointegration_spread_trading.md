# Cointegration-Based Spread Trading

**Cointegration-based spread trading** involves identifying pairs or groups of futures contracts that share a long-term equilibrium relationship (cointegration), then trading the temporary deviations from this equilibrium, profiting from the statistical tendency of the spread to revert to its mean while being market-neutral to directional price movements.

---

## The Core Insight

**The fundamental idea:**

- Some futures contracts move together over long periods (cointegrated)
- Their spread is mean-reverting (stationary)
- Temporary deviations from equilibrium create trading opportunities
- Trade the spread, not the individual contracts
- Statistical edge from mean reversion
- Market-neutral to overall market direction

**The key equation:**

$$
Y_t = \beta X_t + \epsilon_t
$$

Where:
- $Y_t$ = Price of one futures contract
- $X_t$ = Price of related futures contract
- $\beta$ = Hedge ratio (cointegration coefficient)
- $\epsilon_t$ = Stationary spread (mean-reverting)

**The cointegration property:**

$$
\epsilon_t = Y_t - \beta X_t \sim I(0)
$$

- $\epsilon_t$ is stationary (mean-reverting)
- Even though $Y_t$ and $X_t$ are non-stationary $I(1)$
- **This is the magic of cointegration!**

**You're essentially betting: "I've found two contracts with a stable long-term relationship. When they deviate from this relationship, they will converge back, regardless of which direction the market moves."**

---

## What is Cointegration?

**Before trading cointegration, understand what it actually means:**

### Cointegration Defined

**Definition:** Two or more time series are cointegrated if:

1. Each series is non-stationary (has a unit root, $I(1)$)
2. A linear combination of them IS stationary ($I(0)$)

**Mathematically:**

If $Y_t \sim I(1)$ and $X_t \sim I(1)$, but:

$$
\epsilon_t = Y_t - \beta X_t \sim I(0)
$$

Then $Y_t$ and $X_t$ are **cointegrated** with cointegration vector $[1, -\beta]$.

### Stationary vs. Non-Stationary

**Stationary process $I(0)$:**

$$
E[Y_t] = \mu \text{ (constant mean)}
$$

$$
\text{Var}(Y_t) = \sigma^2 \text{ (constant variance)}
$$

$$
\text{Cov}(Y_t, Y_{t-k}) = f(k) \text{ (depends only on lag, not time)}
$$

**Properties:**
- Mean-reverting
- Fluctuates around constant mean
- Shocks are temporary
- **Tradeable for mean reversion**

**Non-stationary process $I(1)$:**

$$
Y_t = Y_{t-1} + \epsilon_t \quad \text{(random walk)}
$$

**Properties:**
- No mean reversion
- Wanders without bounds
- Shocks are permanent
- **Not tradeable for mean reversion**

### Correlation vs. Cointegration

**Correlation:** Measures contemporaneous co-movement

$$
\rho = \frac{\text{Cov}(Y_t, X_t)}{\sigma_Y \sigma_X}
$$

**Problems with correlation alone:**
- Can be high even if no long-term relationship
- Can be spurious (both trending, not related)
- Doesn't guarantee mean reversion
- **Not sufficient for pairs trading**

**Cointegration:** Measures long-term equilibrium relationship

$$
Y_t = \beta X_t + \epsilon_t, \quad \epsilon_t \sim I(0)
$$

**Advantages:**
- Captures stable long-term relationship
- Spread is stationary (mean-reverting)
- Statistical edge for trading
- **Necessary for sustainable pairs trading**

**Example: The difference**

**High correlation, NOT cointegrated:**
- $Y_t = $ NASDAQ futures
- $X_t = $ S&P 500 futures
- Correlation: 0.95 (very high!)
- But: Both trending, spread may drift
- **Spread not stationary → Poor pair**

**Lower correlation, but cointegrated:**
- $Y_t = $ WTI crude oil
- $X_t = $ Brent crude oil
- Correlation: 0.90 (high but not extreme)
- **Spread stationary → Good pair**

### Simple Example: WTI vs. Brent

**The relationship:**

WTI and Brent crude oil are cointegrated:

$$
\text{WTI}_t = \beta \cdot \text{Brent}_t + \epsilon_t
$$

**Historical hedge ratio:** $\beta \approx 1.02$

**The spread:**

$$
\text{Spread}_t = \text{WTI}_t - 1.02 \times \text{Brent}_t
$$

**Historical statistics:**
- Mean spread: -$2.00/barrel
- Std deviation: $3.00/barrel
- Half-life: 15 days

**Trading signal:**

**When spread > $1.00** (2σ above mean):
- WTI relatively expensive
- Short WTI, Long Brent (hedge ratio 1.02:1)
- Expected: Spread reverts to -$2.00
- **Profit: ~$3.00/barrel**

**When spread < -$5.00** (1σ below mean):
- WTI relatively cheap
- Long WTI, Short Brent (hedge ratio 1.02:1)
- Expected: Spread reverts to -$2.00
- **Profit: ~$3.00/barrel**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/cointegration_spread_trading.png?raw=true" alt="cointegration_spread_trading" width="700">
</p>
**Figure 1:** Illustration of cointegration-based spread trading showing two non-stationary price series (top) that create a stationary, mean-reverting spread (bottom). Trading signals generated when spread deviates beyond thresholds.

---

## Economic Interpretation: Why Cointegration Exists

**Beyond the statistical definition, understanding the economic drivers:**

### Fundamental Linkages

**Cointegration exists when two assets share:**

1. **Common production factors:**
   - WTI and Brent: Both crude oil
   - Corn and Ethanol: Input-output relationship
   - Gold and Silver: Precious metals

2. **Substitutability:**
   - Natural gas and Heating oil: Energy substitutes
   - RBOB and Ethanol: Gasoline blending
   - Different wheat contracts: Geographic arbitrage

3. **Common demand drivers:**
   - Equity indices: Macro economy
   - Commodity pairs: Industrial demand
   - Currency pairs: Trade relationships

### The Law of One Price

**Economic principle:**

$$
P_1 = \alpha + \beta P_2 + \text{Transaction Costs}
$$

**For similar assets:**
- Arbitrage enforces relationship
- Deviations create profit opportunities
- **Self-correcting mechanism**

**Example: WTI vs. Brent**

**The relationship:**
- Both price crude oil
- Quality differences: WTI (light, sweet) vs. Brent (slightly heavier)
- Location: Cushing, OK vs. North Sea
- **Expected price difference: Quality + Transportation**

**Economic forces:**
- If WTI too cheap → Refineries buy WTI instead of Brent
- If Brent too cheap → European refiners buy Brent, sell WTI
- **Arbitrage keeps spread bounded**

### Cost of Carry Relationships

**For related commodities:**

$$
F_{\text{processed}} = F_{\text{input}} + \text{Processing Costs} + \text{Margin}
$$

**Examples:**

**Crack spread (Crude → Gasoline):**

$$
\text{RBOB}_t = \alpha \cdot \text{Crude}_t + \text{Refining Margin}_t
$$

- Cointegrated due to refining process
- Spread = Refining margin
- Mean-reverts around processing costs

**Crush spread (Soybeans → Meal + Oil):**

$$
\text{Meal}_t + \text{Oil}_t = \beta \cdot \text{Soybeans}_t + \text{Processing Costs}_t
$$

- Physical transformation creates linkage
- Processors arbitrage deviations
- **Economic cointegration**

### Storage and Transportation

**Geographic price relationships:**

$$
P_{\text{Destination}} = P_{\text{Origin}} + \text{Transport Cost}
$$

**Examples:**

**Natural gas hubs:**
- Henry Hub vs. Waha Hub
- Difference = Pipeline capacity + costs
- Cointegrated with bounded spread

**Agricultural delivery points:**
- Chicago wheat vs. Kansas City wheat
- Difference = Quality + Transportation
- **Arbitrage-enforced relationship**

### Index Arbitrage

**For equity index futures:**

$$
F_{\text{Index}} = S_{\text{Index}} \cdot e^{(r-q)(T-t)}
$$

**Multiple index relationships:**

$$
\text{NASDAQ} = \alpha + \beta \cdot \text{S\&P 500} + \epsilon_t
$$

- Share many constituents
- Driven by same macro factors
- **Statistical and economic cointegration**

### Why Cointegration Breaks Down

**Regime changes can destroy cointegration:**

1. **Structural shifts:**
   - Technology changes (fracking changed WTI-Brent)
   - Regulation changes (export bans, tariffs)
   - Infrastructure changes (new pipelines)

2. **Market structure changes:**
   - New participants (index flows)
   - Liquidity shifts
   - Contract specification changes

3. **Economic shocks:**
   - Financial crises
   - Pandemics
   - Wars

**This is why cointegration must be monitored continuously!**

### Why This Perspective Matters

**Understanding cointegration economics helps you:**

1. **Select pairs:**
   - Look for fundamental linkages
   - Not just statistical correlation
   - **Economic story matters**

2. **Understand mean reversion:**
   - What drives it (arbitrage, substitution)
   - How fast (half-life)
   - **When it might fail**

3. **Manage risk:**
   - Monitor for regime changes
   - Adjust hedge ratios
   - **Exit when cointegration breaks**

4. **Identify opportunities:**
   - New cointegration relationships
   - Temporary breakdown (crisis)
   - **Structural changes create new pairs**

**Professionals say: "Trade the economics, verify with statistics. Cointegration without an economic story is just data mining."**

---

## Key Terminology

**Cointegration Fundamentals:**

**Cointegration:**

Two or more $I(1)$ series whose linear combination is $I(0)$

$$
Y_t - \beta X_t = \epsilon_t \sim I(0)
$$

- Long-term equilibrium relationship
- Spread is stationary
- **Foundation of pairs trading**

**Hedge Ratio ($\beta$):**

$$
\beta = \frac{\text{Cov}(Y, X)}{\text{Var}(X)}
$$

- Weight on second asset
- Minimizes spread variance
- **How much of X to hedge Y**

**Spread (Residual):**

$$
\epsilon_t = Y_t - \beta X_t
$$

- Stationary if cointegrated
- Mean-reverting
- **What we actually trade**

**Stationarity:**

**Weak stationarity (covariance stationary):**

1. Constant mean: $E[Y_t] = \mu$
2. Constant variance: $\text{Var}(Y_t) = \sigma^2$
3. Autocovariance depends only on lag: $\text{Cov}(Y_t, Y_{t-k}) = \gamma_k$

**Mean reversion:**
- Returns to mean after shocks
- Essential for trading

**Unit Root:**

$$
Y_t = \rho Y_{t-1} + \epsilon_t
$$

- If $\rho = 1$: Unit root (non-stationary)
- If $|\rho| < 1$: Stationary
- **Test determines tradability**

**Order of Integration:**

- $I(0)$: Stationary
- $I(1)$: Becomes stationary after first difference
- $I(2)$: Requires two differences

**Most financial prices:** $I(1)$ (random walk)
**Returns:** $I(0)$ (stationary)
**Cointegrated spread:** $I(0)$ (stationary)

**Statistical Tests:**

**Augmented Dickey-Fuller (ADF) Test:**

$$
\Delta Y_t = \alpha + \beta t + \gamma Y_{t-1} + \sum_{i=1}^{p} \delta_i \Delta Y_{t-i} + \epsilon_t
$$

**Tests:** $H_0: \gamma = 0$ (unit root)

**If reject $H_0$:** Series is stationary

**Use:**
- Test individual series (should NOT be stationary)
- Test spread (SHOULD be stationary)
- **Both conditions needed for cointegration**

**Engle-Granger Two-Step:**

**Step 1:** Estimate cointegration regression

$$
Y_t = \alpha + \beta X_t + \epsilon_t
$$

**Step 2:** Test residuals for stationarity

$$
\text{ADF test on } \epsilon_t
$$

**If residuals stationary:** Cointegrated!

**Johansen Test:**

**For multiple series:**

$$
\Delta Y_t = \Pi Y_{t-1} + \sum_{i=1}^{k-1} \Gamma_i \Delta Y_{t-i} + \epsilon_t
$$

**Tests:** Rank of $\Pi$ matrix

**Advantages:**
- Tests multiple cointegration relationships
- More powerful than Engle-Granger
- **Best for >2 series**

**Mean Reversion Metrics:**

**Half-life:**

$$
\tau_{1/2} = -\frac{\ln(2)}{\ln(\rho)}
$$

Where $\rho$ from AR(1): $\epsilon_t = \rho \epsilon_{t-1} + \nu_t$

**Interpretation:**
- Time for half of deviation to dissipate
- Faster half-life = Better for trading
- **Typical: 5-30 days for futures**

**Speed of mean reversion ($\theta$):**

$$
\Delta \epsilon_t = -\theta \epsilon_{t-1} + \nu_t
$$

$$
\theta = 1 - \rho
$$

- Higher $\theta$ = Faster reversion
- $\theta \in [0, 1]$

**Hurst Exponent:**

$$
H = \frac{\log(R/S)}{\log(n)}
$$

- $H < 0.5$: Mean-reverting
- $H = 0.5$: Random walk
- $H > 0.5$: Trending
- **Want $H < 0.5$ for spread**

**Trading Metrics:**

**Z-score:**

$$
Z_t = \frac{\epsilon_t - \mu_{\epsilon}}{\sigma_{\epsilon}}
$$

- Standardized deviation from mean
- Entry: $|Z| > 2$ (typical)
- Exit: $Z = 0$ (mean)

**Bollinger Bands:**

$$
\text{Upper} = \mu_{\epsilon} + 2\sigma_{\epsilon}
$$

$$
\text{Lower} = \mu_{\epsilon} - 2\sigma_{\epsilon}
$$

- Entry: Spread touches bands
- Exit: Spread crosses mean

**Kalman Filter:**

**Dynamic hedge ratio:**

$$
\beta_t = \beta_{t-1} + K_t (Y_t - \beta_{t-1} X_t)
$$

- Adapts to changing relationships
- Better than static $\beta$
- **More sophisticated approach**

**Rolling Window:**

**Re-estimate $\beta$ periodically:**

$$
\beta_t = \text{OLS}(Y_{t-n:t}, X_{t-n:t})
$$

- Window: 60-252 days typical
- Balance: Stability vs. adaptiveness
- **Captures regime changes**

---

## Contract Specifications: Best Cointegration Pairs

**Understanding which futures contracts are most likely to be cointegrated:**

### Energy Sector (Strong Cointegration)

**Crude Oil Pairs:**

**WTI (CL) vs. Brent (BZ):**

**Relationship:**
- Both crude oil benchmarks
- Quality slightly different
- Geographic arbitrage

**Historical parameters:**
- Hedge ratio: $\beta \approx 1.02$
- Spread mean: -$2.00/barrel
- Spread σ: $3.00/barrel
- Half-life: 10-15 days
- **Cointegration: Very strong** ✓

**Trading:**
- Entry: $|Z| > 2$ (spread ± $6 from mean)
- Exit: $Z = 0$ (spread returns to -$2)
- Position: 1.02 Brent per 1 WTI

**Crack Spreads:**

**RBOB Gasoline vs. Crude Oil:**

$$
\text{RBOB}_t = \alpha + \beta \cdot \text{CL}_t + \epsilon_t
$$

**Parameters:**
- Hedge ratio: $\beta \approx 1.5$ (1.5 barrels crude per barrel gasoline)
- Mean spread: $15/barrel
- Half-life: 20-30 days

**Heating Oil vs. Crude Oil:**

Similar relationship, seasonal variation (winter demand)

**Natural Gas Related:**

**Henry Hub (NG) vs. Regional Hubs:**

- Limited cointegration (capacity constraints)
- Better: Short-term calendar spreads
- **Cointegration weaker than crude pairs**

### Agricultural Sector (Moderate Cointegration)

**Grain Complexes:**

**Corn (ZC) vs. Wheat (ZW):**

**Relationship:**
- Both feed grains
- Partial substitutes in livestock feed
- Similar planting decisions

**Parameters:**
- Hedge ratio: $\beta \approx 0.60$ (wheat more expensive)
- Varies seasonally
- Half-life: 30-60 days
- **Cointegration: Moderate**

**Soybean Complex:**

**Soybeans (ZS) vs. Soybean Meal (ZM) + Soybean Oil (ZL):**

$$
\text{ZS}_t = \beta_1 \cdot \text{ZM}_t + \beta_2 \cdot \text{ZL}_t + \epsilon_t
$$

**Crush spread:**
- Physical transformation relationship
- Strong cointegration
- **Processors arbitrage deviations**

**Geographic Arbitrage:**

**CBOT Corn vs. MGEX Spring Wheat:**

- Different crops but related demand
- Geographic price differences
- Weaker cointegration than crude oil

### Metals Sector (Variable Cointegration)

**Precious Metals:**

**Gold (GC) vs. Silver (SI):**

$$
\text{GC}_t = \alpha + \beta \cdot \text{SI}_t + \epsilon_t
$$

**Relationship:**
- Both precious metals
- Industrial demand differs (silver)
- **Gold/Silver ratio trades**

**Parameters:**
- Hedge ratio: Variable (40-80 oz silver per oz gold)
- Mean ratio: ~60
- Half-life: Long (60+ days)
- **Cointegration: Weak to moderate**

**Caution:** Ratio can trend for years!

**Industrial Metals:**

**Copper (HG) vs. Aluminum:**

- Both industrial demand
- Different supply dynamics
- **Cointegration: Weak**

### Equity Index Futures (Strong Cointegration)

**E-mini Contracts:**

**ES (S&P 500) vs. NQ (NASDAQ-100):**

$$
\text{NQ}_t = \alpha + \beta \cdot \text{ES}_t + \epsilon_t
$$

**Relationship:**
- Overlap in constituents
- Same macro drivers
- Tech sector differences

**Parameters:**
- Hedge ratio: $\beta \approx 3.5-4.0$ (NQ higher priced)
- Half-life: 5-10 days
- **Cointegration: Very strong** ✓

**ES (S&P 500) vs. RTY (Russell 2000):**

**Large cap vs. small cap:**
- Different market cap exposure
- Correlation strong but varies
- **Cointegration: Moderate**

**International Indices:**

**ES vs. FTSE, DAX, Nikkei:**

- Common global factors
- Currency effects complicate
- Time zone differences
- **Cointegration: Moderate (currency-hedged better)**

### Currency Futures (Triangular Relationships)

**Major Pairs:**

**EUR/USD vs. GBP/USD:**

- Both vs. dollar
- Eurozone-UK economic linkage
- **Cointegration: Moderate**

**Cross-rate arbitrage:**

$$
\text{EUR/USD} = \frac{\text{EUR/GBP}}{\text{GBP/USD}}
$$

- Enforced by triangular arbitrage
- **Very strong cointegration** ✓

### Fixed Income Futures (Yield Curve)

**Treasury Futures:**

**10-Year (ZN) vs. 30-Year (ZB):**

$$
\text{ZB}_t = \alpha + \beta \cdot \text{ZN}_t + \epsilon_t
$$

**Relationship:**
- Same issuer (U.S. Treasury)
- Term structure linkage
- Monetary policy affects both

**Parameters:**
- Hedge ratio: Duration-weighted
- Half-life: Short (2-5 days)
- **Cointegration: Strong** ✓

**2-Year vs. 10-Year:**

**Yield curve steepener/flattener:**
- Monetary policy expectations
- Very strong cointegration
- **Popular institutional trade**

### Commodity Pairs to Avoid

**Weak/No cointegration:**

1. **Unrelated commodities:**
   - Gold vs. Crude oil (weak economic link)
   - Corn vs. Copper (no relationship)
   - **No cointegration** ✗

2. **Similar but independent:**
   - Coffee vs. Cocoa (both softs, but different)
   - Cattle vs. Hogs (both livestock, but different cycles)
   - **Spurious correlation** ✗

3. **Storage-constrained:**
   - Natural gas (regional basis differences too large)
   - Electricity (non-storable)
   - **Physical constraints break cointegration** ✗

### Selection Criteria

**Best cointegration pairs have:**

1. **Economic linkage:**
   - Same commodity (WTI/Brent)
   - Input-output (Crude/RBOB)
   - Substitutes (Corn/Wheat)

2. **Arbitrage mechanism:**
   - Physical delivery possible
   - Active market participants
   - **Self-correcting forces**

3. **Statistical evidence:**
   - ADF test: $p < 0.05$
   - Half-life: 5-60 days
   - Hurst < 0.5

4. **Liquidity:**
   - Both contracts liquid
   - Tight bid-ask spreads
   - **Can execute both legs efficiently**

---

## Maximum Profit and Loss: The Bounded Nature

### Understanding Cointegration Spread P&L

**The profit/loss equation:**

$$
\text{P\&L} = (\epsilon_{\text{exit}} - \epsilon_{\text{entry}}) \times \text{Multiplier} \times \text{Contracts}
$$

Where:

$$
\epsilon_t = Y_t - \beta X_t
$$

**For long spread (buy when spread low):**
- Entry: $\epsilon < \mu - 2\sigma$ (undervalued)
- Exit: $\epsilon = \mu$ (fair value)
- **Profit: $2\sigma$**

**For short spread (sell when spread high):**
- Entry: $\epsilon > \mu + 2\sigma$ (overvalued)
- Exit: $\epsilon = \mu$ (fair value)
- **Profit: $2\sigma$**

### Maximum Profit (Theoretical)

**Perfect mean reversion from extreme:**

$$
\text{Max Profit} \approx 4\sigma \text{ (from -2σ to +2σ or vice versa)}
$$

**But realistic:**

$$
\text{Typical Profit Target} = 2\sigma
$$

**Example: WTI-Brent spread**

**Parameters:**
- Mean: $\mu = -\$2.00$
- Std dev: $\sigma = \$3.00$
- Entry: $Z = -2$ (spread at -$8.00)
- Exit: $Z = 0$ (spread at -$2.00)

**P&L:**
- Spread change: $-2.00 - (-8.00) = +\$6.00$
- On 10 contracts WTI:
  - WTI: 10 × 1,000 × gain
  - Brent: 10 × 1.02 × 1,000 × loss
  - **Net: ~$6 × 10,000 = $60,000**

**Return on margin:**
- Margin: ~$16,000 (spread margin)
- Return: $60,000 / $16,000 = **375%**

**Maximum theoretical:**

If spread from -3σ to +3σ:
- Range: $6\sigma = 6 × \$3 = \$18$
- **Max profit: $18 × 10,000 = $180,000** (extreme case)

### Maximum Loss (Risk Management)

**Stop loss scenarios:**

**1. Mean fails to revert (regime change):**

**Entry:** $Z = -2$ (spread -$8)
**Stop:** $Z = -3$ (spread -$11)
**Loss:** -$3 per barrel

**On 10 contracts:**
- Loss: -$3 × 10,000 = **-$30,000**
- Return: -$30,000 / $16,000 = **-188%**

**2. Spread continues widening (no stop):**

**Historical maximum:**
- WTI-Brent spread: -$30 (2011 Cushing glut)
- Entry: -$8
- **Maximum loss if held: $22 × 10,000 = $220,000** ☠️

**This is why stops are ESSENTIAL!**

### Risk-Reward Profile

**Typical cointegration trade:**

**Entry signal:** $|Z| > 2$
**Target:** $Z = 0$
**Stop:** $|Z| > 3$

**Expected profit:** $2\sigma$
**Maximum loss:** $1\sigma$ (with stop)

**Risk-reward ratio:** 2:1 (favorable)

**Win rate:** 60-70% (mean reversion works most of the time)

**Expected value:**

$$
EV = 0.65 \times 2\sigma - 0.35 \times 1\sigma = 0.95\sigma > 0
$$

**Positive expectancy!**

### Comparison to Directional Trading

**Outright long futures:**
- Max gain: Unlimited
- Max loss: 100% (to zero)
- Direction: Must predict correctly
- Risk: High

**Cointegration spread:**
- Max gain: ~$4-6\sigma$ (bounded)
- Max loss: ~$1-2\sigma$ (with stops)
- Direction: Market-neutral
- Risk: Lower

**Example:**

**Both start with $100,000:**

**Outright trader:**
- Long crude oil at $80
- Falls to $60: **-$250,000** (wiped out + margin call) ☠️
- Rises to $100: **+$250,000** ✓

**Spread trader:**
- WTI-Brent spread at -$8
- Spread widens to -$11: **-$30,000** (stopped out) ✗
- Spread reverts to -$2: **+$60,000** ✓

**Spread trader:**
- Survived adverse move
- Lower volatility
- **Better risk-adjusted returns**

---

## Entry and Exit Strategies

### Entry Strategies: When to Initiate Spread

**1. Z-Score Entry (Most Common)**

**Calculate z-score:**

$$
Z_t = \frac{\epsilon_t - \mu_{\epsilon}}{\sigma_{\epsilon}}
$$

**Entry rules:**

**Long spread (buy Y, sell βX) when:**
- $Z < -2$ (spread undervalued)
- Y relatively cheap vs. X

**Short spread (sell Y, buy βX) when:**
- $Z > +2$ (spread overvalued)
- Y relatively expensive vs. X

**Example: WTI-Brent**

**Calculate spread:**
- WTI: $72
- Brent: $75
- Hedge ratio: $\beta = 1.02$
- Spread: $72 - 1.02 × 75 = -$4.50

**Historical stats (60-day window):**
- Mean: $\mu = -\$2.00$
- Std dev: $\sigma = \$2.50$

**Z-score:**

$$
Z = \frac{-4.50 - (-2.00)}{2.50} = -1.0
$$

**Decision:** Wait (not extreme enough)

**Next day:**
- Spread: -$7.00
- Z = (-$7.00 - (-$2.00)) / $2.50 = -2.0
- **Entry: Long WTI, Short 1.02× Brent** ✓

**2. Bollinger Band Entry**

**Calculate bands:**

$$
\text{Upper Band} = \mu + 2\sigma
$$

$$
\text{Lower Band} = \mu - 2\sigma
$$

**Entry:**
- Touch lower band → Long spread
- Touch upper band → Short spread
- **Mean: $\mu$ (exit target)**

**Advantages:**
- Visual entry signals
- Adapts to changing volatility
- Easy to implement

**3. Statistical Arbitrage Entry**

**Strict statistical criteria:**

**Requirements:**
1. Cointegration test: $p < 0.05$ (ADF on spread)
2. Half-life: 5-60 days
3. Hurst exponent: $H < 0.5$
4. Entry: $|Z| > 2$

**Example screening process:**

**Pair: ES vs. NQ**

**Step 1:** Test cointegration
- Run OLS: $\text{NQ}_t = \alpha + \beta \text{ES}_t + \epsilon_t$
- Get residuals: $\hat{\epsilon}_t$
- ADF test on $\hat{\epsilon}_t$: **$p = 0.01$** ✓ (cointegrated!)

**Step 2:** Calculate half-life
- AR(1): $\epsilon_t = \rho \epsilon_{t-1} + \nu_t$
- Estimate: $\hat{\rho} = 0.92$
- Half-life: $-\ln(2)/\ln(0.92) = 8.3$ days ✓

**Step 3:** Current z-score
- Current: $Z = -2.5$ 
- **Enter: Long NQ, Short $\beta$ × ES** ✓

**4. Kalman Filter Entry (Advanced)**

**Dynamic hedge ratio:**

**State space model:**

$$
\beta_t = \beta_{t-1} + \eta_t
$$

$$
Y_t = \beta_t X_t + \epsilon_t
$$

**Kalman filter estimates $\beta_t$ recursively**

**Entry:**
- Use current $\hat{\beta}_t$ (not static)
- Calculate spread: $\epsilon_t = Y_t - \hat{\beta}_t X_t$
- Enter when $|Z| > 2$

**Advantages:**
- Adapts to changing relationship
- Better during regime transitions
- **More robust than fixed $\beta$**

### Exit Strategies: When to Close Spread

**1. Mean Reversion Exit (Primary)**

**Target exit: Spread returns to mean**

$$
Z_t = 0 \quad \implies \quad \epsilon_t = \mu
$$

**Example:**
- Entry: $Z = -2.0$ (spread -$7.00)
- Mean: $\mu = -\$2.00$
- Exit: When spread reaches -$2.00
- **Profit: $5.00 per barrel**

**Partial exit:**
- Close 50% at $Z = -1$
- Close 50% at $Z = 0$
- **Lock partial profits early**

**2. Profit Target Exit**

**Fixed dollar target:**

**Example:**
- Entry spread: -$7.00
- Target profit: $4.00/barrel
- Exit spread: -$3.00
- **Don't wait for full mean reversion**

**Advantages:**
- Certain profit taking
- Reduces holding time risk
- Higher win rate

**Disadvantages:**
- May miss full reversion
- Lower profit per trade

**3. Stop Loss Exit (Risk Management)**

**Critical for survival:**

**Set stop based on:**

$$
\text{Stop Loss} = \epsilon_{\text{entry}} \pm 1\sigma
$$

**Example:**
- Entry: $Z = -2.0$, spread -$7.00
- Stop: $Z = -3.0$, spread -$9.50
- **Maximum loss: $2.50 per barrel**

**Why essential:**
- Cointegration can break down
- Regime changes happen
- **Protect capital**

**4. Time Exit**

**Maximum holding period:**

$$
\text{Max Hold} = 3 \times \tau_{1/2}
$$

**Example:**
- Half-life: 15 days
- Max hold: 45 days
- **Exit regardless of P&L after 45 days**

**Rationale:**
- If not reverted in 3× half-life, something wrong
- Cointegration may have broken
- **Free up capital**

**5. Cointegration Breakdown Exit**

**Monitor cointegration:**

**Re-test periodically (weekly/monthly):**
- Rolling window ADF test
- If $p > 0.10$: No longer cointegrated
- **Exit immediately**

**Example:**

**Week 1:** $p = 0.01$ ✓ (cointegrated)
**Week 2:** $p = 0.03$ ✓ (still good)
**Week 3:** $p = 0.15$ ✗ (breakdown!)
**Action:** Exit all spreads in this pair

**6. Volatility Regime Exit**

**Monitor spread volatility:**

$$
\sigma_{\text{current}} > 2 \times \sigma_{\text{historical}}
$$

**Example:**
- Historical σ: $2.50
- Current σ: $5.50 (doubled!)
- **Exit: Regime change likely**

### Position Management

**1. Hedge Ratio Adjustment**

**Re-estimate periodically:**

**Rolling window (60 days):**

$$
\beta_t = \text{OLS}(Y_{t-60:t}, X_{t-60:t})
$$

**Update:**
- Daily calculation
- Adjust position if $\beta$ changes >10%
- **Maintain proper hedge**

**2. Scaling Positions**

**Pyramid into signal:**

**Example:**
- $Z = -2.0$: Enter 33% position
- $Z = -2.5$: Add 33%
- $Z = -3.0$: Add final 33%

**Average entry:** Better than all-in

**3. Portfolio of Spreads**

**Diversify across:**
- Multiple pairs (WTI-Brent, ES-NQ, etc.)
- Different sectors (energy, equities, metals)
- **Reduce idiosyncratic risk**

**Correlation between spreads:**
- Low correlation preferred
- True diversification
- **Smoother equity curve**

---

## Best Case Scenarios: When Cointegration Works Perfectly

### The Dream: Fast Mean Reversion from Extreme

**What defines best case:**

1. Extreme spread deviation (>3σ)
2. Rapid mean reversion (< half-life)
3. Strong cointegration maintained
4. High liquidity (tight execution)
5. **Large profit on low capital**

### Best Case #1: The WTI-Brent Arbitrage (2011)

**The Cushing storage crisis:**

**Setup (April 2011):**

- **Pair:** WTI (CL) vs. Brent (BZ)
- **Normal spread:** -$2/barrel (Brent premium)
- **Hedge ratio:** $\beta = 1.02$

**The dislocation:**

**February-March 2011:**
- Cushing, OK storage near capacity
- WTI trapped (pipeline constraints)
- Brent unaffected (North Sea)
- **Spread widening dramatically**

**April 15, 2011:**
- WTI: $108/barrel
- Brent: $123/barrel
- **Spread: -$15/barrel** (7.5σ!)

**Historical stats:**
- Mean: -$2
- Std dev: $2
- Current: -$15
- **Z-score: -6.5** (extreme!)

**The trade:**

**Entry (April 15):**
- Long 20 WTI contracts at $108
- Short 20 Brent contracts at $123 (ratio 1.02:1)
- Spread: -$15
- Margin: $40,000 (spread margin)

**Thesis:**
- Spread unsustainable
- Storage constraints temporary
- **Will revert to -$2 to -$5 range**

**The reversion:**

**May-June 2011:**
- Pipeline capacity added
- Cushing inventory declining
- Spread narrowing rapidly

**June 15, 2011 (2 months later):**
- WTI: $95/barrel
- Brent: $105/barrel
- **Spread: -$10/barrel** (converged partially)

**Exit decision:** Take partial profit

**P&L Calculation:**

**WTI leg:**
- Long at $108, Exit at $95
- Loss: -$13/barrel
- P&L: -$13 × 20 × 1,000 = **-$260,000**

**Brent leg:**
- Short at $123, Cover at $105
- Gain: +$18/barrel
- P&L: +$18 × 20 × 1,000 = **+$360,000**

**Net P&L:**
- $360,000 - $260,000 = **+$100,000**

**Spread profit:**
- Entry: -$15
- Exit: -$10
- **Gain: $5/barrel**
- Check: $5 × 20 × 1,000 = **$100,000** ✓

**Return:**
- Profit: $100,000
- Margin: $40,000
- Time: 2 months
- **Return: 250%** 🎯

**If held longer (September 2011):**
- Spread narrowed to -$8
- Additional profit: $2 × 20,000 = $40,000
- **Total: $140,000 (350% return)**

**Why this was best case:**
- Extreme dislocation (6.5σ)
- Fast reversion (2 months)
- Clear fundamental driver
- High liquidity both contracts
- **Massive profit on statistical edge**

### Best Case #2: The ES-NQ Tech Crash Reversion (2022)

**The Fed rate hike divergence:**

**Setup (April 2022):**

- **Pair:** NQ (NASDAQ) vs. ES (S&P 500)
- **Relationship:** Tech-heavy NQ vs. broader ES
- **Hedge ratio:** $\beta \approx 3.8$

**The dislocation:**

**January-March 2022:**
- Fed hawkish → Rate hikes coming
- Tech stocks crushed (high duration)
- S&P 500 more defensive
- **NQ underperforming dramatically**

**April 1, 2022:**
- NQ: 14,500
- ES: 4,500
- Spread: $14,500 - 3.8 × 4,500 = -$2,600$

**Historical stats (1-year):**
- Mean spread: -$500
- Std dev: $800
- Current: -$2,600
- **Z-score: -2.625** (extreme underperformance)

**The trade:**

**Entry (April 1):**
- Long 10 NQ contracts at 14,500
- Short 38 ES contracts at 4,500 (ratio 3.8:1)
- Spread: -$2,600
- Margin: $80,000 (portfolio margin)

**Thesis:**
- Tech oversold relative to broad market
- Mean reversion imminent
- **Spread will narrow**

**The reversion:**

**April-May 2022:**
- Market stabilizes
- Tech rebounds (short covering)
- NQ outperforms ES

**May 15, 2022 (6 weeks later):**
- NQ: 12,300 (fell further!)
- ES: 4,100 (also fell)
- Spread: $12,300 - 3.8 × 4,100 = -$3,280$

**Wait, spread widened?!**

**But June 2022:**
- Bounce in tech sector
- NQ: 13,200
- ES: 4,200
- **Spread: $13,200 - 3.8 × 4,200 = -$2,760$**

**Still not great, exit?**

**Actually July 2022:**
- NQ: 14,000
- ES: 4,300
- **Spread: $14,000 - 3.8 × 4,300 = -$2,340$**

**Better! Hold for mean...**

**August 2022:**
- NQ: 13,800
- ES: 4,150
- **Spread: $13,800 - 3.8 × 4,150 = -$1,970$**

**Getting close to target**

**Exit (August 15):**
- NQ: 13,900
- ES: 4,200
- Spread: $13,900 - 3.8 × 4,200 = -$2,060$

**P&L Calculation:**

**NQ leg:**
- Long at 14,500, Exit at 13,900
- Loss: -$600/contract × $20/point
- P&L: -$600 × $20 × 10 = **-$120,000**

**ES leg:**
- Short at 4,500, Cover at 4,200
- Gain: +$300/contract × $50/point
- P&L: +$300 × $50 × 38 = **+$570,000**

**Net P&L:**
- +$570,000 - $120,000 = **+$450,000**

**Spread profit:**
- Entry: -$2,600
- Exit: -$2,060
- **Narrowing: +$540**
- Check: $540 × $20 × 10 = **$108,000**

**Wait, numbers don't match...**

**Let me recalculate properly:**

**NQ contract:** $20 per point, 10 contracts
**ES contract:** $50 per point, 38 contracts

**Hedge should be NQ vs. ES in dollar terms:**

Actually need to match dollar exposure:
- 10 NQ at 14,500 = 10 × 14,500 × $20 = $2,900,000
- Need ES: $2,900,000 / ($50 × 4,500) = 12.9 contracts

**Let me redo with correct hedging:**

**Entry:**
- Long 10 NQ at 14,500
- Short 13 ES at 4,500 (roughly dollar-matched)

**Exit:**
- NQ: 13,900
- ES: 4,200

**P&L:**
- NQ: (13,900 - 14,500) × $20 × 10 = -$120,000
- ES: (4,500 - 4,200) × $50 × 13 = +$195,000
- **Net: +$75,000**

**Return:**
- Margin: $80,000
- Profit: $75,000
- Time: 4.5 months
- **Return: 94%** ✓

**Why this was best case:**
- Statistical edge (Z = -2.6)
- Mean reversion worked (despite volatility)
- Market-neutral (both fell, still profitable)
- **Positive return in bear market**

### Best Case #3: The Gold-Silver Ratio Crash (2020)

**The COVID precious metals divergence:**

**Setup (March 2020):**

- **Pair:** Gold (GC) vs. Silver (SI)
- **Ratio:** Gold/Silver (oz/oz)
- **Normal ratio:** 60-70

**The dislocation:**

**March 2020 COVID crisis:**
- Flight to safety → Gold spikes
- Industrial demand collapse → Silver crashes
- **Ratio explodes**

**March 18, 2020:**
- Gold: $1,600/oz
- Silver: $12/oz
- **Ratio: 133** (all-time extreme!)

**Historical stats:**
- Mean ratio: 65
- Std dev: 10
- Current: 133
- **Z-score: 6.8!** (nearly 7σ)

**The trade:**

**Entry (March 18):**
- Long 50 Silver contracts at $12/oz
- Short 133/65 × 50 = 102 Gold contracts (ratio adjustment)
- Wait, this is getting complicated...

**Simpler: Trade the ratio directly**

**Entry:**
- Ratio at 133
- Thesis: Will revert to 65-80 range
- Position: Long silver (undervalued), Short gold (overvalued)

**Actually let's use dollar-neutral:**
- Long 100 Silver at $12 (100 × 5,000 oz = 500,000 oz)
- Short 38 Gold at $1,600 (38 × 100 oz = 3,800 oz)
- **Dollar match: $6M silver, $6.08M gold** ✓

**The spectacular reversion:**

**April-July 2020:**
- Stimulus announced
- Industrial recovery expectations
- Silver rockets (industrial + monetary demand)
- Gold rises but less

**July 15, 2020 (4 months later):**
- Gold: $1,800/oz (up $200)
- Silver: $19/oz (up $7!)
- **Ratio: 95** (from 133!)

**P&L:**

**Silver leg:**
- Long at $12, Exit at $19
- Gain: +$7/oz
- P&L: +$7 × 500,000 oz = **+$3,500,000**

**Gold leg:**
- Short at $1,600, Cover at $1,800
- Loss: -$200/oz
- P&L: -$200 × 3,800 oz = **-$760,000**

**Net P&L:**
- +$3,500,000 - $760,000 = **+$2,740,000**

**Return:**
- Notional: ~$6M
- Margin: ~$600,000 (10%)
- Profit: $2,740,000
- **Return: 457%!** 🚀💎

**If held to August (ratio hit 70):**
- Silver: $28/oz
- Gold: $2,000/oz
- **Additional $2M+ profit possible**

**Why this was best case:**
- Extreme ratio (133 vs. 65 mean)
- Massive Z-score (6.8σ)
- Fast, powerful reversion
- Both legs liquid
- **Unprecedented opportunity**

### Common Best Case Elements

**What makes cointegration trades work spectacularly:**

1. **Extreme deviations:**
   - Z-score > 3σ
   - Fundamental dislocations
   - **Panic or euphoria**

2. **Clear catalysts:**
   - Storage constraints (WTI-Brent)
   - Sector rotation (NQ-ES)
   - Risk-on/risk-off (Gold-Silver)

3. **Mean reversion:**
   - Half-life maintained
   - Cointegration persists
   - **Statistical edge works**

4. **Execution:**
   - High liquidity
   - Proper hedge ratios
   - **Professional execution**

5. **Patience:**
   - Hold through volatility
   - Trust the statistics
   - **Don't exit early**

**The professional wisdom:**

"Best cointegration trades are when the market panics and breaks a fundamental relationship. The spread goes to 4-6 sigma. Everyone knows it's wrong, but can't arbitrage due to capital constraints or risk limits. You step in, size appropriately, and wait. Mean reversion is inevitable. These trades can make your year in a few months."

---

## Worst Case Scenarios: When Cointegration Breaks Down

### The Nightmare: Regime Change Destroys Relationship

**What defines worst case:**

1. Cointegration permanently breaks
2. Spread continues widening (no reversion)
3. Both legs move against you
4. Forced to hold (illiquid) or exit at loss
5. **Capital destruction from "statistical edge"**

### Worst Case #1: The WTI-Brent Structural Break (2010-2012)

**The shale revolution changes everything:**

**Setup (2010):**

- **Pair:** WTI vs. Brent
- **Historical relationship:** Very stable
- **Spread mean:** +$1 to -$3 (narrow range)
- **Cointegration:** Very strong (decades of data)

**Traditional stats (2000-2009):**
- Mean: -$1.50
- Std dev: $2.00
- Half-life: 12 days
- **Perfect cointegration pair** ✓

**The trade (Early 2010):**

**Entry (January 2010):**
- WTI: $82/barrel
- Brent: $79/barrel
- Spread: +$3 (WTI premium!)
- Z-score: (+$3 - (-$1.50))/$2 = **+2.25** (overvalued)

**Position:**
- Short 50 WTI at $82
- Long 50 Brent at $79 (1:1 ratio)
- Margin: $100,000
- **Thesis: Spread will revert to -$1.50**

**The disaster:**

**2010: Shale boom accelerates**
- U.S. oil production soaring (fracking)
- WTI supply floods Cushing, OK
- Infrastructure can't handle it
- Brent unaffected (global market)

**June 2010:**
- WTI: $75 (down $7)
- Brent: $78 (down $1)
- Spread: -$3 (moved toward us!)
- **Looks good... but wait...**

**Late 2010:**
- Pipeline constraints worsen
- Storage capacity issues
- Spread: -$8
- **Still think it's temporary...**

**2011: Complete breakdown**

**February 2011:**
- WTI: $97
- Brent: $106
- Spread: -$9

**April 2011:**
- WTI: $110
- Brent: $127
- **Spread: -$17!** (Never seen before)

**The realization:**

**This is not mean reversion. This is structural change.**

**The new regime:**
- U.S. oil landlocked
- Export ban prevents arbitrage
- Brent reflects global demand
- WTI reflects local oversupply
- **Cointegration broken!**

**The horrific P&L:**

**Forced exit (April 2011):**

**WTI leg:**
- Short at $82, Cover at $110
- Loss: -$28/barrel
- P&L: -$28 × 50 × 1,000 = **-$1,400,000** ☠️

**Brent leg:**
- Long at $79, Sell at $127
- Gain: +$48/barrel
- P&L: +$48 × 50 × 1,000 = **+$2,400,000**

**Net P&L:**
- +$2,400,000 - $1,400,000 = **+$1,000,000**

**Wait, that's a profit!**

**Actually, check spread:**
- Entry spread: +$3
- Exit spread: -$17
- Change: -$20 (we were short spread)
- **Should be loss...**

**Correct P&L:**

When short spread (short WTI, long Brent):
- Lose when spread widens negatively
- Spread went from +$3 to -$17 = -$20 change
- We're short, so we lose
- **P&L: -$20 × 50 × 1,000 = -$1,000,000** ☠️

**Return:**
- Loss: -$1,000,000
- Initial margin: $100,000
- **Return: -1,000%** (account wiped + owe $900k) ☠️☠️☠️

**What went catastrophically wrong:**

1. **Structural change:** Shale revolution permanent
2. **No mean reversion:** Spread never came back
3. **Cointegration broken:** New regime, new relationship
4. **No stop loss:** Held hoping for reversion
5. **Over-leveraged:** 50 contracts too many

**The aftermath:**

**Spread remained wide for years:**
- 2012: -$15 to -$20
- 2013: -$10 to -$15
- 2014: -$5 to -$10
- 2015-2017: -$2 to -$5 (partial normalization)
- **Never returned to historical mean**

**New cointegration relationship:**
- New mean: -$5 (not -$1.50)
- Higher volatility
- Different dynamics
- **Old model completely invalid**

### Worst Case #2: The Gold-Silver Ratio Trending (2003-2011)

**When mean reversion fails for years:**

**Setup (2003):**

- **Pair:** Gold vs. Silver
- **Ratio:** 60 (normal)
- **Trade:** "Ratio too high, sell gold buy silver"

**The persistent trend:**

**2003-2008:**

| Year | Gold | Silver | Ratio | Trade P&L |
|------|------|--------|-------|-----------|
| 2003 | $400 | $6 | 67 | Enter short ratio |
| 2004 | $450 | $7 | 64 | Small profit |
| 2005 | $500 | $7.50 | 67 | Back to entry |
| 2006 | $650 | $12 | 54 | Profit! |
| 2007 | $850 | $14 | 61 | Closing in |
| 2008 | $900 | $11 | **82** | Disaster! ☠️ |

**2008 Crisis:**
- Gold: Safe haven, up to $900
- Silver: Industrial collapse, down to $11
- **Ratio exploded to 82** (from 60 entry)

**If held short ratio (sell gold at 60, buy silver):**

**Entry:** Ratio 60
- Short gold at $400
- Long silver proportionally

**Exit (forced 2008):** Ratio 82
- Gold $900 (up 125%)
- Silver $11 (up 83%)

**P&L disaster:**
- Gold loss: -125% on short
- Silver gain: +83% on long
- **Net: Approximately -40% to -60%** depending on sizing ☠️

**Then 2011:**
- Ratio went to 32 (would have been huge profit)
- **But most traders stopped out at 82**

### Worst Case #3: The Natural Gas Storage Arb Failure (2006)

**The storage trade that broke:**

**Setup (March 2006):**

- **Pair:** Natural gas front month vs. summer month
- **Historical:** Strong cointegration (seasonal pattern)
- **Trade:** Buy summer (cheap), sell winter (expensive)

**Normal pattern:**
- Winter gas: $10
- Summer gas: $6
- **Spread: $4** (winter premium)

**Historical stats:**
- Mean spread: $3
- Std dev: $1
- Current: $4
- Z-score: +1 (slightly high)

**The trade:**

**Entry (March 2006):**
- Short April contract at $8.00
- Long July contract at $5.50
- Spread: $2.50 (expecting narrowing to $2)
- Position: 100 contracts each
- Margin: $200,000

**Thesis:**
- Seasonal spread will normalize
- Summer contract undervalued
- **Easy mean reversion**

**The disaster:**

**April-May 2006:**
- Unexpected heat wave
- Early air conditioning demand
- Storage injections slow
- **Near-term tightness**

**May 2006:**
- April (now May) at $9.00
- July at $7.50
- **Spread widened to $1.50** (wrong direction!)

**Forced to roll April to June:**
- Losses mounting
- Roll costs add up
- Now June-July spread

**June 2006: Hurricane season starts**
- Supply concerns
- Front months spike
- June at $10.50
- July at $8.00
- **Spread now $2.50** (started at $2.50!)

**P&L after 3 months:**

**Front month (short):**
- Sold at $8.00 (April)
- Rolled losses plus current at $10.50
- **Cumulative loss: ~$3.00/MMBtu**

**Back month (long):**
- Bought at $5.50 (July)
- Now at $8.00
- **Gain: $2.50/MMBtu**

**Net:**
- Loss: -$3.00 × 100 × 10,000 = -$3,000,000
- Gain: +$2.50 × 100 × 10,000 = +$2,500,000
- **Net: -$500,000** ☠️

**Return:**
- Loss: -$500,000
- Margin: $200,000
- **Return: -250%** (account wiped) ☠️

**What went wrong:**

1. **Weather shock:** Unpredictable heat
2. **Roll losses:** Each roll locked in losses
3. **Seasonality failed:** Pattern broke down
4. **Leverage:** 100 contracts too many
5. **No exit discipline:** Kept hoping

### Common Worst Case Themes

**Why cointegration trades blow up:**

1. **Regime changes:**
   - Structural economic shifts
   - Technology changes
   - Regulatory changes
   - **Old relationships invalid**

2. **Trending deviations:**
   - Spread doesn't revert
   - Continues widening for months/years
   - **Mean reversion assumption fails**

3. **Black swan events:**
   - Financial crises
   - Pandemics
   - Wars
   - **Correlations go to 1, cointegration fails**

4. **Leverage kills:**
   - Over-positioned
   - Can't handle adverse moves
   - **Forced exit at worst time**

5. **No risk management:**
   - No stop losses
   - No cointegration monitoring
   - Hope instead of discipline
   - **Small edge evaporates**

### Preventing Worst Cases

**Risk management for cointegration trading:**

**1. Monitor cointegration continuously:**

**Re-test weekly/monthly:**

$$
\text{If ADF } p\text{-value} > 0.10 \implies \text{Exit all positions}
$$

**2. Use stop losses:**

**Spread-based stop:**

$$
\text{Stop} = \epsilon_{\text{entry}} \pm 1.5\sigma
$$

**Example:**
- Entry: $Z = -2.0$
- Stop: $Z = -3.5$
- **Maximum loss: 1.5σ**

**3. Position sizing:**

$$
\text{Max Position} = \frac{\text{Capital} \times 0.20}{\text{Margin per Spread}}
$$

- Use only 20% of capital
- Keep 80% buffer
- **Survive 3-4σ moves**

**4. Diversification:**

- Multiple uncorrelated pairs
- Different sectors
- **Don't concentrate**

**5. Time stops:**

$$
\text{Exit if no reversion in } 3 \times \tau_{1/2}
$$

**6. Fundamental monitoring:**

- Watch for structural changes
- Regulatory shifts
- Technology disruptions
- **Exit if story changes**

**Remember: Cointegration is statistical, not guaranteed. Protect capital first, profits second!**

---

## What to Remember

### Core Concept

**Cointegration is a long-term equilibrium relationship:**

$$
Y_t = \beta X_t + \epsilon_t, \quad \epsilon_t \sim I(0)
$$

- Two non-stationary series ($I(1)$)
- Linear combination is stationary ($I(0)$)
- **Spread mean-reverts** ✓

**Different from correlation:**
- Correlation: Contemporaneous co-movement
- Cointegration: Long-term equilibrium
- **Cointegration → Tradeable spread**

### The Trading Edge

**Statistical arbitrage:**
- Spread deviates from mean (temporary)
- Mean reversion is probabilistic
- **Positive expectancy over time**

**Market neutral:**
- Don't predict absolute prices
- Only predict spread convergence
- **Lower risk than directional**

### Key Tests

**For cointegration:**

**1. ADF test on spread:**
- $H_0$: Unit root (non-stationary)
- Want: Reject $H_0$ (p < 0.05)
- **Spread must be stationary**

**2. Engle-Granger two-step:**
- Estimate: $Y_t = \alpha + \beta X_t + \epsilon_t$
- Test: ADF on $\epsilon_t$
- **Classic cointegration test**

**3. Johansen test:**
- For multiple series
- More powerful
- **Best for >2 assets**

### Entry Signals

**Z-score based (most common):**

$$
Z_t = \frac{\epsilon_t - \mu}{\sigma}
$$

**Entry:**
- $Z < -2$: Long spread (buy Y, sell βX)
- $Z > +2$: Short spread (sell Y, buy βX)

**Target:**
- $Z = 0$ (mean reversion)

**Stop:**
- $|Z| > 3$ (regime change risk)

### Hedge Ratio

**Optimal hedge:**

$$
\beta = \frac{\text{Cov}(Y,X)}{\text{Var}(X)}
$$

**Estimate via OLS:**

$$
Y_t = \alpha + \beta X_t + \epsilon_t
$$

**Update periodically:**
- Rolling window (60-252 days)
- Kalman filter (dynamic)
- **Maintain proper hedge**

### Half-Life

**Speed of mean reversion:**

$$
\tau_{1/2} = -\frac{\ln(2)}{\ln(\rho)}
$$

**Typical ranges:**
- Fast: 5-15 days (excellent)
- Medium: 15-60 days (good)
- Slow: >60 days (marginal)

**Rule:**
- Exit if no reversion in $3 \times \tau_{1/2}$

### Best Pairs

**Strong cointegration:**

1. **WTI vs. Brent** (crude oil benchmarks)
   - Economic: Same commodity
   - Half-life: 10-15 days
   - **Excellent** ✓

2. **ES vs. NQ** (equity indices)
   - Economic: Overlapping stocks
   - Half-life: 5-10 days
   - **Excellent** ✓

3. **10Y vs. 30Y Treasuries** (yield curve)
   - Economic: Term structure
   - Half-life: 2-5 days
   - **Excellent** ✓

4. **Soybean crush spread** (input-output)
   - Economic: Physical transformation
   - Half-life: 20-40 days
   - **Very good** ✓

**Weak/avoid:**
- Gold vs. Crude (no linkage)
- Unrelated commodities
- **High correlation ≠ cointegration**

### Risk Management

**Position sizing:**

$$
\text{Position} = \frac{\text{Capital} \times 0.20}{\text{Margin}}
$$

- Use 20% max
- Keep 80% buffer
- **Survive adverse moves**

**Stop losses (essential):**

$$
\text{Stop} = \epsilon_{\text{entry}} \pm 1.5\sigma
$$

- Limit maximum loss
- Exit if cointegration breaks
- **Protect capital**

**Monitoring:**
- Re-test cointegration monthly
- Watch for regime changes
- **Exit if $p > 0.10$**

### Maximum Profit

**Typical target:**

$$
\text{Profit} = 2\sigma \text{ (from ±2σ to mean)}
$$

**Best case:**
- Extreme deviation (>3σ)
- Fast reversion (< half-life)
- **Returns: 100-500% on margin**

**Examples:**
- 2011 WTI-Brent: 250% in 2 months
- 2020 Gold-Silver: 457% in 4 months
- **Statistical edges work spectacularly sometimes**

### Maximum Loss

**With stops:**

$$
\text{Max Loss} \approx 1.5\sigma
$$

**Without stops (worst case):**
- Regime change
- Cointegration breaks
- **Losses: -100% to -1,000%** ☠️

**Examples:**
- 2010-2012 WTI-Brent structural break: -1,000%
- 2003-2008 Gold-Silver trend: -60%
- **Always use stops!**

### Common Mistakes

1. **Confusing correlation with cointegration**
2. **Not testing for stationarity** (ADF test)
3. **Using fixed hedge ratio** (should update)
4. **No stop losses** (fatal)
5. **Over-leveraging** (survive adverse moves)
6. **Ignoring regime changes** (monitor continuously)
7. **Data mining** (finding spurious relationships)
8. **No economic story** (need fundamental linkage)

### Performance Expectations

**Win rate:**
- 60-70% (mean reversion works most times)

**Average profit:**
- 1-3% per trade (on notional)
- 10-30% on margin

**Average loss:**
- 0.5-1.5% per trade (with stops)
- 5-15% on margin

**Sharpe ratio:**
- 1.5-2.5 (good strategies)
- Better than directional trading

### Time Horizon

**Holding period:**

$$
\text{Typical} = 1-3 \times \tau_{1/2}
$$

**Example:**
- Half-life: 15 days
- Typical hold: 15-45 days
- **Exit if not reverted by 45 days**

**Not suitable for:**
- Day trading (need time for reversion)
- Buy-and-hold (need active monitoring)
- **Medium-term strategy (weeks to months)**

### Capital Requirements

**Minimum:**
- $50,000+ (diversification needs)
- Better: $200,000+
- Institutional: $1M+

**Why:**
- Need multiple pairs (diversification)
- Margin requirements (20% usage max)
- Drawdown buffer
- **Small accounts can't diversify enough**

### Technology Needs

**Essential:**
- Statistical software (R, Python)
- Data feed (clean historical data)
- Cointegration testing (ADF, Johansen)
- **Not discretionary - needs quant skills**

**Nice to have:**
- Kalman filter (dynamic hedge ratio)
- Machine learning (regime detection)
- Portfolio optimization

### Final Wisdom

> "Cointegration trading is statistical arbitrage - you're betting on mean reversion of relationships that have held for years. It works beautifully until it doesn't. The edge is real but small (1-3% per trade), and you need volume, diversification, and discipline. Always test for cointegration before trading. Always use stops. Always monitor for regime changes. The best trades are when relationships break to 3+ sigma on panic, and you have the conviction to fade the crowd. But remember: past cointegration doesn't guarantee future cointegration. Markets change, relationships break. This is NOT passive income - it's active quantitative trading requiring constant monitoring and risk management."

**Key principles:**

1. **Test rigorously** (ADF, Engle-Granger, Johansen)
2. **Need economic story** (not just statistics)
3. **Use stops always** (regime changes happen)
4. **Size conservatively** (20% capital max)
5. **Monitor continuously** (re-test monthly)
6. **Diversify pairs** (multiple uncorrelated)
7. **Update hedge ratios** (rolling window or Kalman)
8. **Exit discipline** (time stops, cointegration breaks)

**Most important:**

Cointegration is probability, not certainty. The spread will mean-revert... until it doesn't. Structural changes destroy relationships. Technology, regulation, crises all break cointegration. Always have stops. Always monitor. **Never assume the past will repeat forever.** 🎯📊

**Remember:**
- Statistical edge ≠ Guaranteed profit
- Low risk ≠ No risk
- Past cointegration ≠ Future cointegration
- **Risk management is everything!** ⚠️
