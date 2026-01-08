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

### 1. Cointegration Defined

**Definition:** Two or more time series are cointegrated if:

1. Each series is non-stationary (has a unit root, $I(1)$)
2. A linear combination of them IS stationary ($I(0)$)

**Mathematically:**

If $Y_t \sim I(1)$ and $X_t \sim I(1)$, but:

$$
\epsilon_t = Y_t - \beta X_t \sim I(0)
$$

Then $Y_t$ and $X_t$ are **cointegrated** with cointegration vector $[1, -\beta]$.

### 2. Stationary vs. Non-Stationary

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

### 3. Correlation vs. Cointegration

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

### 4. Simple Example

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

## Economic

**Beyond the statistical definition, understanding the economic drivers:**

### 1. Fundamental Linkages

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

### 2. The Law of One Price

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

### 3. Cost of Carry Relationships

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

### 4. Storage and Transportation

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

### 5. Index Arbitrage

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

### 6. Why Cointegration Breaks Down

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

### 7. Why This Perspective Matters

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

## Contract Specifications

**Understanding which futures contracts are most likely to be cointegrated:**

### 1. Energy Sector (Strong Cointegration)

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

### 2. Agricultural Sector (Moderate Cointegration)

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

### 3. Metals Sector (Variable Cointegration)

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

### 4. Equity Index Futures (Strong Cointegration)

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

### 5. Currency Futures (Triangular Relationships)

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

### 6. Fixed Income Futures (Yield Curve)

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

### 7. Commodity Pairs to Avoid

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

### 8. Selection Criteria

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

## Maximum Profit and Loss

### 1. Understanding Cointegration Spread P&L

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

### 2. Maximum Profit (Theoretical)

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

### 3. Maximum Loss (Risk Management)

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

### 4. Risk-Reward Profile

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

### 5. Comparison to Directional Trading

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

### 1. Entry Strategies

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

### 2. Exit Strategies

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

### 3. Position Management

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



## Final Wisdom

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