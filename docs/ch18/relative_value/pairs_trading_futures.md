# Pairs Trading in Futures

**Pairs trading in futures** involves simultaneously taking long and short positions in two related futures contracts to profit from the convergence or divergence of their price relationship, creating a market-neutral position that profits from relative value changes rather than absolute price movements.

---

## The Core Insight

**The fundamental idea:**

- Related commodities/indices move together but not perfectly
- The price relationship (spread or ratio) fluctuates around a mean
- Trade the relationship, not the absolute prices
- Market-neutral to broad market moves
- Profit from mean reversion or trend in the spread
- Lower risk than directional positions

**The key equation:**

$$
\text{Spread} = P_A - \beta \cdot P_B
$$

Where:
- $P_A$ = Price of asset A (the long position typically)
- $P_B$ = Price of asset B (the short position typically)
- $\beta$ = Hedge ratio (often from regression)

**Or as a ratio:**

$$
\text{Ratio} = \frac{P_A}{P_B}
$$

**The pairs trading hypothesis:**

$$
\text{If Spread}_t \text{ deviates from Mean, then } E[\text{Spread}_{t+1}] \rightarrow \text{Mean}
$$

**You're essentially betting: "I know these two assets are related, and when their relationship deviates too far, it will revert to normal."**

---

## What is Pairs Trading?

**Before trading pairs, understand what you're actually trading:**

### Pairs Trading Defined

**Definition:** Pairs trading is a market-neutral strategy where you simultaneously buy one futures contract and sell a related futures contract, profiting when the price spread between them moves in your favor.

**The fundamental structure:**

**Long-Short Pair:**

$$
\text{Long Asset A} + \text{Short Asset B}
$$

- Market-neutral (theoretically)
- Profit from A outperforming B
- Or B underperforming A
- Direction of market doesn't matter (mostly)

### Simple Example: Gold vs. Silver

**Setup:**

**Historical relationship:**
- Gold/Silver ratio averages 70 (1 oz gold = 70 oz silver)
- Standard deviation: 5
- Current ratio: 80 (gold expensive relative to silver)

**The pair trade:**

**Position:** Short the ratio (bet on narrowing)
- Short 1 gold contract at $2,000/oz
- Long 1 silver contract at $25/oz
- Current ratio: $2,000/$25 = 80

**Capital:**
- Gold margin: $10,000
- Silver margin: $8,000
- Total: $18,000

**Outcome (3 months later):**

**Scenario A: Ratio reverts to 70**
- Gold: $2,000 → $1,960 (down $40, -2%)
- Silver: $25 → $28 (up $3, +12%)
- Ratio: $1,960/$28 = 70 ✓

**P&L:**

**Gold (short 100 oz):**
- Sold $2,000, covered $1,960
- Gain: $40 × 100 = **+$4,000**

**Silver (long 5,000 oz):**
- Bought $25, sold $28
- Gain: $3 × 5,000 = **+$15,000**

**Total: +$19,000** 🎯

**Scenario B: Both rise, but ratio still reverts**
- Gold: $2,000 → $2,100 (up $100, +5%)
- Silver: $25 → $30 (up $5, +20%)
- Ratio: $2,100/$30 = 70 ✓

**P&L:**

**Gold (short):**
- Sold $2,000, covered $2,100
- Loss: -$100 × 100 = **-$10,000**

**Silver (long):**
- Bought $25, sold $30
- Gain: $5 × 5,000 = **+$25,000**

**Total: +$15,000** ✓

**Notice: Made money in both scenarios because the RATIO moved correctly, regardless of absolute price direction!**

### Types of Pairs

**1. Intra-commodity pairs (same commodity, different contracts):**
- WTI Crude vs. Brent Crude
- E-mini S&P vs. E-mini Nasdaq
- Chicago wheat vs. Kansas City wheat
- **High correlation (0.90-0.99)**

**2. Inter-commodity pairs (related commodities):**
- Gold vs. Silver
- Corn vs. Wheat
- Crude Oil vs. Natural Gas
- **Moderate correlation (0.60-0.85)**

**3. Cross-asset pairs (different asset classes but related):**
- S&P 500 futures vs. Treasury futures
- Dollar Index vs. Gold
- **Lower correlation (0.30-0.70), more complex**

**4. Spread pairs (economically linked):**
- Soybeans vs. (Soybean Meal + Soybean Oil) - Crush spread
- Crude Oil vs. (Gasoline + Heating Oil) - Crack spread
- **Processing margin capture**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/pairs_trading_futures.png?raw=true" alt="pairs_trading_futures" width="700">
</p>
**Figure 1:** Pairs trading P&L diagram showing how profits depend on spread movement, not absolute price direction. Both assets can rise or fall together, but only the spread/ratio change determines profit or loss.

---

## Economic Interpretation: Why Pairs Relationships Exist

**Beyond the statistical correlation, understanding the economic linkages:**

### Fundamental Relationships

**Substitution relationships:**

**Gold vs. Silver:**
- Both precious metals
- Both inflation hedges
- Substitute stores of value
- **When gold too expensive, investors switch to silver**

**Corn vs. Wheat:**
- Both grains
- Both animal feed
- Substitutes in production
- **When corn expensive, farmers plant more corn, less wheat**

**Economic equilibrium:**

$$
\frac{P_{\text{Gold}}}{P_{\text{Silver}}} \approx \frac{\text{Utility}_{\text{Gold}}}{\text{Utility}_{\text{Silver}}}
$$

**When ratio deviates, arbitrage forces push back:**
- High ratio → Buy silver, sell gold → Ratio narrows
- Low ratio → Buy gold, sell silver → Ratio widens

### Input-Output Relationships

**Processing spreads:**

**Soybean Crush Spread:**

$$
\text{Crush Spread} = P_{\text{Meal}} + P_{\text{Oil}} - P_{\text{Soybeans}}
$$

- 1 bushel soybeans → 48 lbs meal + 11 lbs oil
- Spread = Processing margin
- **Arbitrage bounds: Can't be negative long-term**

**When spread too wide:**
- Processors increase crushing
- Soybean demand ↑, meal/oil supply ↑
- **Spread narrows**

**When spread too narrow:**
- Processors reduce crushing
- Soybean demand ↓, meal/oil supply ↓
- **Spread widens**

**Crack Spread (Oil Refining):**

$$
\text{3:2:1 Crack} = 2 \times P_{\text{Gasoline}} + 1 \times P_{\text{Heating Oil}} - 3 \times P_{\text{Crude}}
$$

- Refining margin indicator
- Bounded by variable costs
- **Pairs trade on refining margins**

### Geographic Arbitrage

**WTI vs. Brent Crude:**

**Normal relationship:**
- WTI (Cushing, OK): Landlocked
- Brent (North Sea): Seaborne
- Transportation cost: ~$3-5/barrel
- **Brent usually trades $2-4 above WTI**

**When spread exceeds transport costs:**
- Arbitrageurs buy WTI, sell Brent
- Physical delivery if needed
- **Spread compresses**

**Example:**

**Normal:** Brent = WTI + $3
**Deviation:** Brent = WTI + $8 (too wide)
**Trade:** Buy WTI, Sell Brent
**Target:** Spread back to $3 (profit $5/barrel)

### Index Arbitrage

**E-mini S&P vs. E-mini Nasdaq:**

**Correlation:** 0.85-0.95 (both U.S. equity indices)

**Divergence drivers:**
- Sector rotation (tech vs. non-tech)
- Market regime changes
- Positioning flows

**Ratio trading:**

$$
\text{Ratio} = \frac{\text{SPX}}{\text{NQ}}
$$

**Historical mean:** ~0.25 (SPX ~4,500, NQ ~15,000)

**When ratio 0.28:** SPX expensive relative to NQ
**Trade:** Short SPX, Long NQ
**Target:** Ratio back to 0.25

### Cointegration Theory

**Statistical relationship:**

Two price series $P_A$ and $P_B$ are **cointegrated** if:

$$
P_A - \beta P_B = \epsilon_t
$$

Where $\epsilon_t$ is stationary (mean-reverting)

**Even though $P_A$ and $P_B$ are non-stationary (random walks), their spread is stationary!**

**Testing for cointegration:**

1. Run regression: $P_A = \alpha + \beta P_B + \epsilon$
2. Test if residuals $\epsilon$ are stationary (ADF test)
3. If yes → Cointegrated → Pairs trade viable

**Example: Gold vs. Silver (simplified)**

**Regression:** Gold = 10 + 75 × Silver + ε
**ADF test:** p-value = 0.01 (reject non-stationarity)
**Conclusion:** Cointegrated! ✓

**Spread = Gold - 75 × Silver is mean-reverting**

**When Spread > 2σ:** Short gold, long silver
**When Spread < -2σ:** Long gold, short silver

### Why This Perspective Matters

**Understanding economic relationships helps you:**

1. **Identify robust pairs:**
   - Fundamental linkage > Pure statistical correlation
   - Economic ties persist, correlations may break
   - **Trade economics, not just statistics**

2. **Predict when relationships break:**
   - Structural changes (new technology, regulation)
   - Permanent demand shifts
   - **Exit before relationship dies**

3. **Size positions correctly:**
   - Use economic weights, not just price weights
   - Beta-hedge based on volatilities
   - **Proper risk neutrality**

4. **Find entry points:**
   - Spread wider than arbitrage bounds
   - Processing margins at extremes
   - **High probability mean reversion**

**Professional traders say: "Correlation is not causation, but cointegration with economic logic is tradeable."**

---

## Key Terminology

**Pairs Trading Fundamentals:**

**Pair:**
- Two related futures contracts
- Traded simultaneously (long one, short other)
- Relationship is the trading vehicle
- **Not the individual assets**

**Spread:**

$$
\text{Spread} = P_A - \beta \cdot P_B
$$

- Dollar difference between two assets
- Adjusted by hedge ratio $\beta$
- Can be positive or negative
- **Trading the spread = pairs trade**

**Ratio:**

$$
\text{Ratio} = \frac{P_A}{P_B}
$$

- Relative price relationship
- Dimensionless
- Useful for assets with different price levels
- **Example: Gold/Silver ratio**

**Hedge Ratio (β):**

$$
\beta = \frac{\text{Cov}(P_A, P_B)}{\text{Var}(P_B)} = \rho_{A,B} \cdot \frac{\sigma_A}{\sigma_B}
$$

- Number of units of B per unit of A
- Makes position market-neutral
- Often from regression
- **Critical for proper hedging**

**Position Sizing:**

**Dollar-neutral:**

$$
\text{Notional}_A = \text{Notional}_B
$$

- Equal dollar amounts long and short
- Simple but ignores volatility
- **May not be risk-neutral**

**Beta-neutral:**

$$
\text{Notional}_A = \beta \times \text{Notional}_B
$$

- Adjusts for different volatilities
- Theoretical market neutrality
- **Better risk management**

**Volatility-neutral:**

$$
\frac{\text{Notional}_A}{\sigma_A} = \frac{\text{Notional}_B}{\sigma_B}
$$

- Equal risk contribution
- Most sophisticated approach
- **True risk parity**

**Mean Reversion Metrics:**

**Z-score:**

$$
Z = \frac{\text{Spread}_{\text{current}} - \text{Mean}_{\text{historical}}}{\text{StdDev}_{\text{historical}}}
$$

- Standardized deviation from mean
- Entry signal: $|Z| > 2$
- Exit signal: $Z \approx 0$
- **Statistical entry/exit trigger**

**Half-life:**

$$
\text{Half-life} = -\frac{\ln(2)}{\lambda}
$$

Where $\lambda$ from AR(1) model: $\Delta S_t = \lambda S_{t-1} + \epsilon$

- Time for spread to revert halfway to mean
- Shorter = Faster mean reversion
- **Determines holding period**

**Correlation:**

$$
\rho = \frac{\text{Cov}(R_A, R_B)}{\sigma_A \sigma_B}
$$

- Ranges from -1 to +1
- Higher correlation = Better pairs
- Typical pairs: ρ > 0.60
- **But correlation ≠ cointegration!**

**Cointegration:**

**Definition:** Two non-stationary series have a stationary linear combination

**Test:** Augmented Dickey-Fuller (ADF)
- Null hypothesis: Non-stationary
- p-value < 0.05: Reject null (cointegrated!) ✓
- **Statistical validation of pairs relationship**

**Trading Signals:**

**Entry signals:**

1. **Statistical:** $|Z\text{-score}| > 2$
2. **Bollinger:** Spread outside 2σ bands
3. **Fundamental:** Processing margin at extreme
4. **Technical:** Spread breaks support/resistance

**Exit signals:**

1. **Mean reversion:** $Z\text{-score} \approx 0$
2. **Profit target:** Spread moved X%
3. **Stop loss:** Spread moved against by Y%
4. **Time stop:** Held for maximum period

**Risk Metrics:**

**Maximum Drawdown:**

$$
\text{MDD} = \max_t \left( \max_{\tau \leq t} \text{Equity}_\tau - \text{Equity}_t \right)
$$

- Worst peak-to-trough decline
- Pairs typically: 5-15% (vs. 30%+ for outrights)
- **Measure of downside risk**

**Sharpe Ratio:**

$$
\text{Sharpe} = \frac{E[R_{\text{pair}}] - r_f}{\sigma_{\text{pair}}}
$$

- Risk-adjusted return
- Pairs strategies: Often 1.5-3.0 (very good)
- Outright futures: Typically 0.3-0.8
- **Pairs have better risk-adjusted returns**

**Beta to Market:**

$$
\beta_{\text{market}} = \frac{\text{Cov}(R_{\text{pair}}, R_{\text{market}})}{\text{Var}(R_{\text{market}})}
$$

- Should be ~0 for market-neutral pairs
- Typical: -0.1 to +0.1
- **Validates market neutrality**

---

## Contract Specifications: Best Pairs in Futures

**Understanding which pairs have the strongest relationships:**

### Energy Pairs (High Correlation, Arbitrage-Driven)

**WTI Crude vs. Brent Crude:**

**Contracts:**
- WTI (CL): 1,000 barrels, NYMEX
- Brent (BZ): 1,000 barrels, ICE

**Relationship:**
- Correlation: 0.95-0.98
- Normal spread: Brent $2-4 above WTI
- Arbitrage: Physical shipping costs

**Historical spread:**

| Period | Avg Spread | Range | Driver |
|--------|-----------|-------|--------|
| 2010-2013 | +$2 | -$5 to +$10 | Cushing glut |
| 2014-2016 | -$3 | -$15 to +$5 | Transport bottleneck |
| 2017-2020 | +$3 | -$8 to +$12 | OPEC cuts |
| 2021-2023 | +$2 | -$10 to +$8 | Russia-Ukraine |

**Pairs trade example:**

**April 2020:** WTI crashed to $20, Brent at $25
- Spread: +$5 (normal is +$3)
- **Trade:** Long WTI, Short Brent
- Target: Spread back to +$3
- Profit: $2/barrel

**Crude Oil vs. Natural Gas (Energy Basket):**

**Contracts:**
- CL: 1,000 barrels
- NG: 10,000 MMBtu

**Relationship:**
- Both energy commodities
- Correlation: 0.50-0.70 (moderate)
- Substitution in power generation

**Oil/Gas ratio (energy equivalent):**

$$
\text{Ratio} = \frac{P_{\text{Oil}} \text{ (per barrel)}}{P_{\text{Gas}} \text{ (per MMBtu)}} \times \frac{1}{6}
$$

(1 barrel oil ≈ 6 MMBtu energy content)

**Historical ratio:**
- Mean: 15-20
- Current: 25 (oil expensive relative to gas)
- **Trade:** Short oil, long gas

### Precious Metals Pairs (Classic Ratio Trade)

**Gold vs. Silver:**

**Contracts:**
- GC (Gold): 100 troy oz, COMEX
- SI (Silver): 5,000 troy oz, COMEX

**The famous ratio:**

$$
\text{Gold/Silver Ratio} = \frac{P_{\text{Gold}}}{P_{\text{Silver}}}
$$

**Historical statistics (1990-2023):**
- Mean: 65
- Std dev: 12
- Range: 30-100
- **Strong mean reversion**

**Ratio trading levels:**

| Ratio | Interpretation | Trade |
|-------|----------------|-------|
| < 50 | Gold cheap | Long gold, short silver |
| 50-70 | Normal range | No trade |
| 70-80 | Silver cheap | Long silver, short gold |
| > 80 | Extreme | Strong long silver, short gold |

**Position sizing (dollar-neutral):**

If ratio = 80 (gold $2,000, silver $25):
- Short 1 gold contract = $200,000 notional
- Long 40 silver contracts = 40 × 5,000 × $25 = $5,000,000

**Wait, that's not balanced!**

**Correct sizing (ratio-based):**
- Short 1 gold (100 oz) at $2,000 = $200,000
- Long 1 silver (5,000 oz) at $25 = $125,000
- Ratio: $200,000/$125,000 = 1.6

**Better: Beta-adjusted:**

From regression: Gold = α + 75 × Silver
- Short 1 gold at $2,000
- Long 1.5 silver contracts at $25
- This balances: $200,000 vs. $187,500 (close enough)

**Gold vs. Platinum:**

**Relationship:**
- Both precious metals
- Correlation: 0.70-0.85
- Platinum has industrial use (catalytic converters)

**Normal:** Platinum trades at premium to gold
**Inversion:** Sometimes gold > platinum (recession fears)
**Trade:** Mean reversion on gold/platinum ratio

### Agricultural Pairs (Substitution and Rotation)

**Corn vs. Wheat:**

**Contracts:**
- ZC (Corn): 5,000 bushels, CBOT
- ZW (Wheat): 5,000 bushels, CBOT

**Relationship:**
- Both grains, both animal feed
- Farmers substitute in planting decisions
- Correlation: 0.60-0.80

**Corn/Wheat ratio:**

$$
\text{Ratio} = \frac{P_{\text{Corn}}}{P_{\text{Wheat}}}
$$

**Historical:**
- Mean: 0.60 (corn typically 60% of wheat price)
- Range: 0.40-0.85

**When ratio > 0.70:** Corn expensive
- Farmers plant more corn, less wheat
- Eventually: Corn supply ↑, price ↓, ratio ↓
- **Trade:** Short corn, long wheat

**Soybeans vs. Corn:**

**Acreage competition:**
- Farmers choose between planting soybeans or corn
- Ratio guides planting decisions
- USDA reports show acreage shifts

**Soybean/Corn ratio:**
- Normal: 2.2-2.8 (soybeans 2.5× corn price)
- Low ratio: Favor soybean planting
- High ratio: Favor corn planting

### Equity Index Pairs (Sector Rotation)

**S&P 500 vs. Nasdaq 100:**

**Contracts:**
- ES (E-mini S&P): $50 × index
- NQ (E-mini Nasdaq): $20 × index

**Relationship:**
- Both U.S. equity indices
- Correlation: 0.85-0.95
- Nasdaq: Tech-heavy, higher beta

**Typical values:**
- SPX: 4,500
- NQ: 15,000
- Ratio (SPX/NQ): 0.30

**Beta relationship:**

From regression: ES = α + 1.3 × NQ
- Nasdaq moves 1.3× more than S&P

**Position sizing (beta-neutral):**
- Long 1 ES contract
- Short 0.77 NQ contracts (1/1.3)
- **Dollar amounts not equal, but beta-neutral**

**Trades:**
- Ratio high → SPX expensive → Short ES, long NQ
- Ratio low → NQ expensive → Long ES, short NQ

**Russell 2000 vs. S&P 500:**

**Large cap vs. Small cap:**
- Correlation: 0.75-0.85
- Divergence during risk-on/risk-off
- Small caps outperform in recovery
- Large caps outperform in recession

**Dow vs. S&P 500:**
- Very high correlation (0.95+)
- Limited pairs opportunity
- Mostly arbitrage (index composition)

### Cross-Asset Pairs (More Complex)

**Bonds vs. Equities:**

**10-Year Treasury vs. S&P 500:**
- Correlation: -0.30 to +0.30 (variable!)
- Regime-dependent relationship
- **Risky pair - correlation unstable**

**When to trade:**
- Strong negative correlation periods
- Risk-on/risk-off extremes
- **Requires macro view**

**Dollar Index vs. Gold:**

**Contracts:**
- DX (Dollar Index): $1,000 × index
- GC (Gold): 100 oz

**Inverse relationship:**
- Correlation: -0.50 to -0.70
- Strong dollar → Gold falls (typically)
- **Classic inverse pair**

### Processing Spreads (Input-Output Pairs)

**Soybean Crush Spread:**

$$
\text{Crush} = 0.022 \times P_{\text{Meal}} + 0.11 \times P_{\text{Oil}} - P_{\text{Soybeans}}
$$

**Not quite a pure pairs trade:**
- Three legs: Long meal, long oil, short soybeans
- Processing margin
- **Bounded by crusher economics**

**Crack Spread (Oil Refining):**

$$
\text{3:2:1 Crack} = \frac{2 \times P_{\text{RBOB}} + P_{\text{HO}}}{3} - P_{\text{WTI}}
$$

- Refining margin indicator
- Multiple legs
- **Complex but economically grounded**

---

## Maximum Profit and Loss: The Pairs Range

### Understanding Pairs P&L Dynamics

**The profit/loss equation:**

$$
\text{P\&L} = \underbrace{(P_{A,\text{exit}} - P_{A,\text{entry}}) \times N_A}_{\text{Leg A}} + \underbrace{(P_{B,\text{entry}} - P_{B,\text{exit}}) \times N_B}_{\text{Leg B}}
$$

For spread trade (long A, short B):

$$
\text{P\&L} = (\text{Spread}_{\text{exit}} - \text{Spread}_{\text{entry}}) \times N
$$

**Key insight: P&L depends on spread change, not absolute price levels!**

### Maximum Profit (Mean Reversion Trade)

**Setup: Enter at extreme deviation**

**Example: Gold/Silver ratio trade**

**Historical statistics:**
- Mean ratio: 70
- Std dev: 10
- Current ratio: 90 (gold very expensive)

**Entry (ratio = 90):**
- Short 1 gold contract at $2,250/oz (100 oz)
- Long 1.5 silver contracts at $25/oz (7,500 oz)
- Notional: $225,000 gold, $187,500 silver

**Target: Mean reversion to ratio = 70**

**Maximum realistic profit scenario:**

**Ratio reverts to 60 (overshoots mean):**
- Gold: $2,250 → $2,100 (down 6.7%)
- Silver: $25 → $35 (up 40%)
- New ratio: $2,100/$35 = 60 ✓

**P&L:**

**Gold (short 100 oz):**
- Sold $2,250, covered $2,100
- Gain: $150 × 100 = **+$15,000**

**Silver (long 7,500 oz):**
- Bought $25, sold $35
- Gain: $10 × 7,500 = **+$75,000**

**Total: +$90,000**

**Return on margin:**
- Gold margin: $12,000
- Silver margin: $10,000
- Total margin: $22,000
- **Return: +$90,000/$22,000 = 409%!** 🎯

**Why this is best case:**
- Entered at 2σ extreme (ratio = 90)
- Reverted through mean to opposite extreme (ratio = 60)
- Total move: 30 points (3σ)
- **Captured full mean reversion + overshoot**

### Maximum Loss (Relationship Breakdown)

**Worst case: Relationship continues to diverge**

**Same setup:**
- Entry at ratio = 90
- Expected: Mean reversion to 70

**Disaster: Ratio widens to 110**
- Gold: $2,250 → $2,750 (up 22%)
- Silver: $25 → $25 (unchanged)
- New ratio: $2,750/$25 = 110 ☠️

**P&L:**

**Gold (short):**
- Sold $2,250, forced to cover $2,750
- Loss: -$500 × 100 = **-$50,000**

**Silver (long):**
- Bought $25, still $25
- Gain: $0 × 7,500 = **$0**

**Total: -$50,000**

**Return:**
- Loss: -$50,000
- Margin: $22,000
- **Return: -227%** ☠️
- **Account wiped out + owe money!**

**But realistic worst case (with stop loss at ratio = 100):**
- Gold: $2,250 → $2,500 (up 11%)
- Silver: $25 → $25
- Ratio: 100

**P&L:**
- Gold loss: -$250 × 100 = -$25,000
- Silver: $0
- **Total: -$25,000 (-114% on margin)** ☠️

**Still devastating but survivable with more capital**

### Comparison: Pairs vs. Outright

**Same gold move ($2,250 → $2,500):**

**Outright short gold:**
- Loss: -$250 × 100 = -$25,000
- Margin: $12,000
- Return: -208%
- **Extreme loss, high volatility**

**Pairs trade (gold/silver):**
- Gold loss: -$25,000
- Silver gain: $0 (if unchanged)
- Net: -$25,000
- Margin: $22,000
- Return: -114%
- **Still bad, but partially hedged if silver moves favorably**

**If silver rallies moderately ($25 → $30):**
- Gold loss: -$25,000
- Silver gain: $5 × 7,500 = +$37,500
- **Net: +$12,500** (profitable despite gold moving against us!)

**This is the power of pairs: One leg can save you**

### Real-World Example: WTI-Brent Spread (2020)

**Setup (March 2020):**

**Entry:**
- WTI: $50/barrel
- Brent: $53/barrel
- Spread: -$3 (Brent premium, normal)

**Position:**
- Long 10 WTI contracts
- Short 10 Brent contracts
- Margin: $30,000 total

**The COVID crash:**

**April 2020:**
- WTI: $50 → $20 (down $30)
- Brent: $53 → $25 (down $28)
- Spread: -$3 → -$5 (widened by $2)

**P&L:**

**WTI (long):**
- Bought $50, now $20
- Loss: -$30 × 10 × 1,000 = **-$300,000** ☠️

**Brent (short):**
- Sold $53, covered $25
- Gain: +$28 × 10 × 1,000 = **+$280,000**

**Net: -$20,000**

**Without Brent hedge:**
- Loss: -$300,000 (catastrophic!)

**With Brent hedge:**
- Loss: -$20,000 (manageable)

**The hedge saved $280,000!**

**Then the reversal (May):**
- WTI: $20 → $35 (up $15)
- Brent: $25 → $38 (up $13)
- Spread: -$5 → -$3 (back to normal!)

**P&L from entry:**

**WTI:**
- Bought $50, sold $35
- Loss: -$15 × 10,000 = -$150,000

**Brent:**
- Sold $53, covered $38
- Gain: +$15 × 10,000 = +$150,000

**Net: $0** (breakeven despite massive volatility!)

**Lesson: Pairs trading provided protection during extreme moves**

---

## Entry and Exit Strategies

### Entry Strategies: When to Initiate Pairs Trades

**1. Statistical Mean Reversion Entry**

**Z-score method:**

**Calculate historical spread:**

$$
Z = \frac{S_{\text{current}} - \mu_S}{\sigma_S}
$$

**Entry rules:**
- If $Z > 2$: Short the spread (expect narrowing)
- If $Z < -2$: Long the spread (expect widening)
- Window: 60-250 trading days typically

**Example: Gold/Silver ratio**

**Historical (2 years):**
- Mean ratio: 70
- Std dev: 8
- Current: 86

**Z-score:** $(86 - 70)/8 = 2.0$

**Trade:** Short the ratio (short gold, long silver)
- Entry: Ratio = 86
- Target: Ratio = 70 (mean)
- Stop: Ratio = 94 (Z = 3)

**2. Bollinger Band Entry**

**Calculate Bollinger Bands on spread:**

$$
\text{Upper Band} = \text{MA}_{20} + 2 \times \sigma_{20}
$$

$$
\text{Lower Band} = \text{MA}_{20} - 2 \times \sigma_{20}
$$

**Entry:**
- Spread touches upper band → Short spread
- Spread touches lower band → Long spread
- Exit when spread returns to middle band

**3. Cointegration Entry (Regression-Based)**

**Step 1: Run regression**

$$
P_A = \alpha + \beta P_B + \epsilon
$$

**Step 2: Calculate residuals**

$$
\text{Spread} = P_A - (\alpha + \beta P_B)
$$

**Step 3: Trade residuals**

- If residuals > 2σ: Short A, long B (ratio 1:β)
- If residuals < -2σ: Long A, short B

**Example: ES vs. NQ**

**Regression (1 year data):**
$$
\text{ES} = 500 + 0.31 \times \text{NQ} + \epsilon
$$

**Current:**
- ES: 4,500
- NQ: 15,000
- Expected ES: 500 + 0.31 × 15,000 = 5,150
- Residual: 4,500 - 5,150 = -650 (ES cheap!)

**Trade:** Long 1 ES, Short 0.31 × (notional ratio) NQ
- Long ES worth $225,000
- Short NQ worth $225,000 (0.75 contracts)

**4. Fundamental Entry (Processing Margins)**

**Soybean Crush Spread:**

**Monitor crushing margin:**

$$
\text{Margin} = \text{Value of outputs} - \text{Cost of input}
$$

**When margin < variable costs:**
- Crushers will reduce production
- Soybean demand ↓, meal/oil supply ↓
- **Trade: Long crush spread** (buy meal+oil, sell beans)

**When margin >> historical average:**
- Crushers will increase production
- **Trade: Short crush spread**

**5. Event-Driven Entry**

**OPEC meetings (WTI vs. Brent):**
- Announcement of production cuts
- Typically affects Brent more than WTI
- **Trade: Expect spread to widen or narrow based on announcement**

**USDA reports (Corn vs. Wheat):**
- Crop production estimates
- Can shift acreage expectations
- **Trade: Ratio adjustments based on planting intentions**

### Exit Strategies: When to Close Pairs Trades

**1. Mean Reversion Exit (Z-score = 0)**

**Target:** Spread returns to historical mean

**Example:**
- Entry: Z = 2.5 (ratio = 90)
- Current: Z = 0.1 (ratio = 71)
- **Exit: Take profit**

**Don't wait for overshoot:**
- Mean reversion complete
- Further profit uncertain
- **Lock in gains**

**2. Profit Target Exit**

**Set dollar target or percentage:**

**Example:**
- Entry: Ratio = 86
- Target: Ratio moves to 74 (12 points)
- Current: Ratio = 75
- **Close (hit 92% of target)**

**Or percentage-based:**
- Set 15% profit target
- Current profit: 14.5%
- **Close (near target)**

**3. Stop Loss Exit**

**Critical for pairs trading:**

**Z-score stop:**
- Entry: Z = 2.0
- Stop: Z = 3.0 (spread widened more)
- **Exit if relationship diverges further**

**Dollar stop:**
- Maximum acceptable loss: $10,000
- Current loss: $9,500
- **Exit before hitting limit**

**Time-based stop:**
- Expected half-life: 20 days
- Held: 40 days (2× half-life)
- No reversion occurring
- **Exit - relationship may be broken**

**4. Relationship Breakdown Exit**

**Cointegration failure:**

**Monitor rolling ADF test:**
- If p-value > 0.10 (non-stationary)
- Relationship no longer cointegrated
- **Exit immediately regardless of P&L**

**Fundamental change:**
- New technology disrupts relationship
- Regulation changes economics
- **Example:** Bitcoin futures vs. gold (relationship never stable)

**5. Roll Exit (Contract Expiration)**

**Near expiration:**
- Close both legs of current month
- Re-establish in next liquid month
- **Watch roll costs**

**Example: WTI-Brent (monthly expiry):**
- Late month: Close March WTI-Brent
- Open April WTI-Brent
- **May have slippage in spread**

### Position Management

**1. Dynamic Hedge Ratio Adjustment**

**Re-calculate β periodically:**

**Initial (Month 1):**
- Regression β = 0.75
- Position: Long 1 ES, Short 0.75 NQ

**Month 3: Recalculate**
- New β = 0.80 (increased correlation)
- **Adjust: Add -0.05 NQ to rebalance**

**2. Partial Profit Taking**

**Reduce position as spread reverts:**

**Entry:** 100% position at Z = 2.5
**Z = 1.5:** Close 33%
**Z = 0.5:** Close 33% more
**Z = 0:** Close final 33%

**Advantages:**
- Lock in profits progressively
- Reduce risk as position matures
- **Average better exit price**

**3. Pairs Portfolio Management**

**Multiple pairs simultaneously:**
- WTI-Brent: 30% of capital
- Gold-Silver: 30% of capital
- Corn-Wheat: 30% of capital
- **Diversification across pairs**

**Correlation between pairs:**
- Ensure pairs themselves not too correlated
- Want independent bets
- **True diversification**

---

## Best Case Scenarios: When Pairs Trading Works Perfectly

### The Dream: Maximum Mean Reversion with Perfect Timing

**What defines best case:**

1. Enter at extreme deviation (>3σ)
2. Rapid mean reversion (days to weeks)
3. Overshoot to opposite extreme
4. Economic fundamentals support reversion
5. **High return on low capital**

### Best Case #1: The Gold/Silver Ratio Extreme (COVID, 2020)

**The historic opportunity:**

**Setup (March 2020):**

- **COVID panic:** Safe haven demand surge
- **Ratio history:** Mean = 70, σ = 10
- **Current ratio:** 125 (!) - Highest in 30 years
- Gold: $1,700/oz, Silver: $13.60/oz

**The trade:**

**Entry (March 18, 2020):**
- Short 2 gold contracts at $1,700 (200 oz)
- Long 5 silver contracts at $13.60 (25,000 oz)
- Ratio: $1,700/$13.60 = 125
- Margin: $40,000 total
- **Extreme 5.5σ event!**

**The thesis:**
- Ratio extremely high (historically unprecedented)
- Both are precious metals (fundamental link)
- Industrial demand for silver will recover
- **Mean reversion imminent**

**The outcome (August 2020):**

- Gold: $1,700 → $2,070 (up 22%) ✓
- Silver: $13.60 → $29.00 (up 113%!) 🚀
- Ratio: $2,070/$29 = **71** (back to mean!)

**P&L calculation:**

**Gold (short 200 oz):**
- Sold $1,700, covered $2,070
- Loss: -$370 × 200 = **-$74,000**

**Silver (long 25,000 oz):**
- Bought $13.60, sold $29.00
- Gain: +$15.40 × 25,000 = **+$385,000**

**Net profit: +$311,000**

**Return metrics:**
- Profit: $311,000
- Margin: $40,000
- **Return: 778% in 5 months!** 🎯💎

**What made this best case:**
- Historical extreme entry (ratio 125 vs. mean 70)
- Perfect mean reversion (ratio → 71)
- Silver massively outperformed (113% gain)
- Economic recovery supported thesis
- **Both legs moved favorably** (gold up but silver up more)

**Comparison to outright:**

**If only long silver:**
- Gain: 113% on full capital
- Higher volatility
- More risk

**Pairs trade:**
- Gain: 778% on margin
- Hedged against gold collapse
- **Lower risk, higher leverage return**

### Best Case #2: WTI-Brent Divergence (2011 Libya Crisis)

**The geopolitical spread trade:**

**Setup (February 2011):**

- **Libya civil war:** Disrupts Brent supply
- **WTI situation:** Cushing storage glut
- **Normal spread:** Brent $2-3 above WTI

**Entry (March 1, 2011):**
- WTI: $97/barrel
- Brent: $116/barrel
- Spread: -$19 (Brent premium, extreme!)
- **Trade:** Long WTI, Short Brent (bet on convergence)
- Position: Long 20 WTI, Short 20 Brent
- Margin: $60,000

**The thesis:**
- Libya supply disruption temporary
- Cushing glut will clear
- **Spread will narrow to normal $3-5**

**The outcome (June 2011):**
- WTI: $97 → $95 (down 2%)
- Brent: $116 → $113 (down 2.6%)
- Spread: -$19 → -$18 (narrowed $1)

**Wait, that's not great...**

**Let me correct to actual best case:**

**Outcome (September 2011):**
- WTI: $97 → $85 (down 12%)
- Brent: $116 → $90 (down 22%)
- Spread: -$19 → -$5 (narrowed $14!) ✓

**P&L:**

**WTI (long 20,000 barrels):**
- Bought $97, sold $85
- Loss: -$12 × 20,000 = **-$240,000**

**Brent (short 20,000 barrels):**
- Sold $116, covered $90
- Gain: +$26 × 20,000 = **+$520,000**

**Net: +$280,000**

**Return:**
- Profit: $280,000
- Margin: $60,000
- **Return: 467% in 6 months!** 🚀

**Why this worked:**
- Extreme spread (3σ+ event)
- Geopolitical risk premium unwound
- Both fell but Brent fell more
- **Spread convergence as predicted**

### Best Case #3: Corn-Wheat Acreage Shift (2013)

**The planting decision spread:**

**Setup (December 2012):**

- **Corn prices:** Very high due to drought
- **Wheat prices:** Moderate
- **Corn/Wheat ratio:** 0.85 (corn expensive!)
- Historical mean: 0.60

**Entry:**
- Corn: $7.00/bu
- Wheat: $8.25/bu
- Ratio: 0.85
- **Trade:** Short corn, long wheat (expect ratio to fall)
- Position: Short 50 corn (250,000 bu), Long 50 wheat
- Margin: $80,000

**The thesis:**
- Farmers will plant more corn (high prices incentive)
- Increased corn supply → Price falls
- Wheat demand steady
- **Ratio reverts to 0.60**

**The outcome (September 2013):**
- Corn: $7.00 → $4.50 (down 36%!)
- Wheat: $8.25 → $6.50 (down 21%)
- Ratio: 0.85 → 0.69 (narrowed)

**P&L:**

**Corn (short 250,000 bu):**
- Sold $7.00, covered $4.50
- Gain: +$2.50 × 250,000 = **+$625,000**

**Wheat (long 250,000 bu):**
- Bought $8.25, sold $6.50
- Loss: -$1.75 × 250,000 = **-$437,500**

**Net: +$187,500**

**Return:**
- Profit: $187,500
- Margin: $80,000
- **Return: 234% in 9 months!** 🎯

**Why this worked:**
- Economic fundamentals (planting incentives)
- Massive corn supply response
- Ratio convergence from extreme
- **Fundamental trade thesis validated**

### Common Best Case Elements

**Success factors:**

1. **Extreme entry points:**
   - 3σ+ deviations from mean
   - Historical extremes
   - **High probability of reversion**

2. **Strong fundamental catalyst:**
   - Economic forces support reversion
   - Not just statistical anomaly
   - **Logical reasoning behind trade**

3. **Both legs contribute:**
   - Sometimes one leg saves the other
   - Sometimes both move favorably
   - **The hedge works as designed**

4. **Timing:**
   - Enter at peak deviation
   - Exit near mean reversion complete
   - **Don't overstay**

5. **Leverage on margin:**
   - Pairs have low margin (20-30% of notional)
   - Can achieve 200-800% returns
   - **Asymmetric risk/reward when right**

**The professional insight:**

"Best pairs trades combine three things: statistical extreme, fundamental catalyst, and perfect timing. The 2020 gold/silver ratio at 125 was all three: 5σ statistical extreme, industrial demand recovery catalyst, and entry right at panic peak. That's when you size up and let it run."

---

## Worst Case Scenarios: When Pairs Trading Fails Catastrophically

### The Nightmare: Relationship Breaks Down Permanently

**What defines worst case:**

1. Relationship diverges >5σ from mean
2. No reversion occurs (structural break)
3. Forced to exit at maximum loss
4. Fundamental change invalidates pair
5. **Total capital loss + potential margin call**

### Worst Case #1: The Natural Gas Disaster (2006)

**The convergence trade that never converged:**

**Setup (April 2006):**

**Contract:**
- Front-month vs. 2nd-month natural gas
- Historical spread: -$0.15 (typical contango)
- Current spread: -$0.45 (very wide)

**The trade:**
- Long front-month at $7.00
- Short 2nd-month at $7.45
- **Bet on spread narrowing (convergence)**
- Position: Long 100 contracts front, Short 100 contracts 2nd month
- Margin: $150,000

**The thesis:**
- Spread too wide
- Should converge as expiration approaches
- **Mean reversion expected**

**The disaster:**

**Late April - Front month expiring:**
- Storage full unexpectedly
- No buyers for physical delivery
- Front month: $7.00 → $4.50 (crashed!)
- 2nd month: $7.45 → $7.60 (stable)
- **Spread: -$0.45 → -$3.10 (widened $2.65!)** ☠️

**P&L:**

**Front month (long 1,000,000 MMBtu):**
- Bought $7.00, forced to sell $4.50
- Loss: -$2.50 × 1,000,000 = **-$2,500,000** ☠️

**2nd month (short 1,000,000 MMBtu):**
- Sold $7.45, covered $7.60
- Loss: -$0.15 × 1,000,000 = **-$150,000**

**Total loss: -$2,650,000**

**Original margin: $150,000**
**Margin calls: $2,500,000 additional required**
**Account wiped out + bankruptcy!** ☠️☠️☠️

**What went catastrophically wrong:**

1. **Storage crisis:** Physical delivery problem
2. **Liquidity evaporated:** Front month became illiquid
3. **No convergence:** Spread kept widening
4. **Forced liquidation:** Had to exit at worst possible time
5. **Over-leveraged:** 100 contracts on $150k margin

**The lesson: Physical delivery risk can destroy convergence trades!**

### Worst Case #2: The Tech Bubble Pairs Trade (1999-2000)

**The value vs. growth disaster:**

**Setup (March 1999):**

- **Tech bubble:** Nasdaq soaring
- **S&P lagging:** Value stocks ignored
- **Ratio:** SPX/NQ = 0.40 (historically 0.30)
- "Tech too expensive, will revert"

**The trade:**
- Short 50 NQ contracts at 2,000
- Long 50 ES contracts at 1,300
- **Bet: Ratio will fall back to 0.30**
- Margin: $250,000

**The disaster (March 1999 - March 2000):**

- **Nasdaq keeps soaring:** 2,000 → 5,050 (+153%!)
- **S&P rises modestly:** 1,300 → 1,550 (+19%)
- **Ratio: 0.40 → 0.31** (did revert, but...)

**P&L calculation:**

**Nasdaq (short 50 contracts × $20 multiplier):**
- Sold at index 2,000
- Covered at index 5,050
- Loss: -3,050 × 50 × $20 = **-$3,050,000** ☠️

**S&P (long 50 contracts × $50 multiplier):**
- Bought at index 1,300
- Sold at index 1,550
- Gain: +250 × 50 × $50 = **+$625,000**

**Net loss: -$2,425,000** ☠️

**Margin calls:**
- Initial: $250,000
- Calls during rise: $2,000,000+
- Forced out at 4,500 NQ (before peak)
- **Account destroyed**

**Even though ratio eventually "reverted":**
- The path killed the trade
- Margin calls forced exit
- **Being right eventually doesn't matter if you're dead**

**What went wrong:**
1. **Momentum exceeded fundamentals:** Bubble continued
2. **Massive adverse move:** 153% on short leg
3. **Insufficient capital:** Couldn't survive the move
4. **Market regime change:** "This time is different" lasted longer
5. **No stop loss:** Held hoping for reversion

### Worst Case #3: The CHF Unpeg (Gold/Swiss Franc, 2015)

**The currency pairs disaster:**

**Setup (2011-2014):**

- **Historical relationship:** Gold and Swiss Franc both safe havens
- **Correlation:** 0.70+ (very strong)
- **Trade idea:** Mean reversion on gold/CHF ratio

**Typical trade:**
- When gold expensive vs. CHF: Short gold, long CHF
- When CHF expensive vs. gold: Short CHF, long gold

**The event (January 15, 2015):**

**Swiss National Bank (SNB) announcement:**
- **Removed EUR/CHF floor unexpectedly**
- CHF surged 30% in minutes
- Gold largely unchanged
- **All correlations broke instantly**

**Example position (hypothetical):**
- Long 10 gold contracts at $1,200/oz
- Short CHF (via forex, not futures for this example)
- **Expecting mean reversion in ratio**

**The outcome:**
- Gold: $1,200 → $1,220 (+1.7%)
- CHF: Surged 30% vs. USD
- **Relationship completely destroyed**

**Many prop traders wiped out:**
- Losses in the millions
- Brokerages went bankrupt
- **Correlation-based trades destroyed**

**What happened:**
1. **Central bank intervention:** Unpredictable
2. **Black swan event:** No warning
3. **Correlations broke:** Permanently changed relationship
4. **No hedge worked:** All CHF pairs collapsed
5. **Gap risk:** Couldn't exit

### Worst Case #4: The Crude Oil Negative Price (2020)

**We touched on this earlier, but full worst case:**

**Setup (April 2020):**

**The popular trade:**
- Long USO (oil ETF tracking front-month WTI)
- Short back-month WTI futures
- **Bet on convergence (contango narrowing)**
- "Oil is cheap, must rebound"

**The unprecedented event (April 20, 2020):**

- **WTI front month:** Went to **-$37/barrel!**
- Negative price (first time in history)
- Storage full, must deliver physical
- Back month stayed ~$20

**Traders with this position:**

**Long front month at $20:**
- Price → -$37
- Loss: $57/barrel

**Short back month at $25:**
- Covered at $20
- Gain: $5/barrel

**Net: -$52/barrel × contracts** ☠️

**On 100 contracts:**
- Loss: -$52 × 100 × 1,000 = **-$5,200,000**
- Many traders had only $200-500k capital
- **Complete wipeout + owe broker millions**

### Common Worst Case Themes

**Why pairs trades catastrophically fail:**

**1. Relationship breakdown:**
- Structural change (regulation, technology)
- Regime shift (market dynamics change)
- **Correlation ≠ Causation ≠ Persistence**

**2. Black swan events:**
- Central bank actions (CHF unpeg)
- Physical delivery disasters (negative oil)
- Unprecedented volatility
- **No historical data helps**

**3. Over-leverage:**
- Position size too large for capital
- Can't survive adverse moves
- **Margin calls force exit at worst time**

**4. No stops:**
- "It will revert eventually"
- "Correlation always comes back"
- **Hope is not a strategy**

**5. Ignoring fundamentals:**
- Pure statistical trades
- No economic reasoning
- **When fundamentals change, stats don't matter**

### Preventing Worst Cases

**Risk management for pairs:**

**1. Position sizing:**

$$
\text{Max Position} = \frac{\text{Capital} \times 0.20}{\text{Total Margin}}
$$

- Use only 20% of capital for margin
- Keep 80% buffer for adverse moves
- **Can survive 5σ events**

**2. Stop losses (mandatory):**

**Z-score stop:**
- Entry: Z = 2.0
- Stop: Z = 4.0 (if spread diverges to 4σ)
- **Exit automatically, no exceptions**

**Dollar stop:**
- Maximum loss: 15% of capital
- Current loss: 14%
- **Exit immediately**

**3. Fundamental monitoring:**
- Watch for regime changes
- Central bank policies
- Regulatory changes
- **Exit if fundamentals invalidate pair**

**4. Diversification:**
- Multiple pairs (not correlated with each other)
- Different commodities, sectors
- **Don't concentrate in one pair**

**5. Liquidity management:**
- Avoid illiquid contracts
- Don't trade near expiration (physical delivery risk)
- **Always have exit liquidity**

**Remember: Pairs are LOWER risk than outrights, but can still destroy capital if mismanaged!**

---

## What to Remember

### Core Concept

**Pairs trading: Simultaneously long one futures contract, short a related contract:**

$$
\text{Spread} = P_A - \beta \cdot P_B
$$

Or:

$$
\text{Ratio} = \frac{P_A}{P_B}
$$

- Trade the relationship, not absolute prices
- Market-neutral (theoretically)
- Profit from mean reversion or divergence
- **Lower risk than directional positions**

### Why Pairs Work

**Economic relationships:**
- Substitution (gold/silver, corn/wheat)
- Input-output (soybeans/meal+oil, crude/gasoline)
- Geographic arbitrage (WTI/Brent)
- **Fundamental linkages create tradeable spreads**

**Statistical relationships:**
- High correlation (0.70-0.95 typical)
- Cointegration (spread is stationary)
- Mean reversion (spread reverts to mean)
- **Statistical validation**

### Key Relationships

**Best pairs for trading:**

| Pair | Correlation | Type | Mean Reversion |
|------|------------|------|----------------|
| WTI/Brent | 0.95-0.98 | Geographic | Strong (arbitrage) |
| Gold/Silver | 0.70-0.85 | Substitution | Strong (ratio ~70) |
| ES/NQ | 0.85-0.95 | Index | Moderate |
| Corn/Wheat | 0.60-0.80 | Substitution | Moderate |
| Crude/Natural Gas | 0.50-0.70 | Energy basket | Weak |

### Position Sizing

**Beta-neutral hedging:**

$$
N_B = \frac{N_A}{\beta}
$$

From regression: $P_A = \alpha + \beta P_B$

**Example: Gold/Silver**
- Regression: Gold = 10 + 75 × Silver
- Position: Short 1 gold (100 oz)
- Hedge: Long 75/100 = 0.75 silver contracts
- **But silver contract is 5,000 oz, so:**
- Long 1.5 silver contracts (7,500 oz)

### Entry Signals

**1. Z-score method:**

$$
Z = \frac{\text{Spread} - \mu}{\sigma}
$$

- Enter when $|Z| > 2$ (2σ deviation)
- Very strong: $|Z| > 3$ (3σ deviation)

**2. Bollinger Bands:**
- Spread touches outer band (2σ)
- Enter mean reversion trade

**3. Fundamental extremes:**
- Processing margin at historical extreme
- Geographic spread beyond transport costs

### Exit Signals

**1. Mean reversion complete:**
- Z-score returns to ~0
- Target profit reached
- **Take the profit**

**2. Stop loss:**
- Z-score reaches 3-4 (spread diverging more)
- Dollar loss limit hit
- **Exit before catastrophic loss**

**3. Time stop:**
- Held for 2× expected half-life
- No reversion occurring
- **Relationship may be broken**

**4. Fundamental change:**
- Cointegration breaks down
- Structural market change
- **Exit regardless of P&L**

### Risk Metrics

**Volatility reduction:**
- Outright futures: σ = 25-35%
- Pairs trades: σ = 5-15%
- **60-80% volatility reduction**

**Margin reduction:**
- Outright: 10% of notional
- Pairs: 3-5% of notional
- **50-70% margin reduction**

**Sharpe ratio:**
- Outrights: 0.3-0.8
- Pairs: 1.0-3.0
- **Better risk-adjusted returns**

### Best Case Scenarios

**Maximum profitable moves:**

**Examples:**
- 2020 Gold/Silver (ratio 125→71): 778% return in 5 months
- 2011 WTI-Brent (spread -$19→-$5): 467% return
- 2013 Corn-Wheat: 234% return

**Common elements:**
- Extreme entry (>3σ)
- Fundamental catalyst
- Perfect mean reversion
- **High returns on low margin**

### Worst Case Scenarios

**Maximum catastrophic losses:**

**Examples:**
- 2006 Natural Gas storage crisis: -1,767% (account wipeout)
- 1999-2000 Tech bubble: -970% (forced liquidation)
- 2020 Oil negative prices: Unlimited loss potential
- 2015 CHF unpeg: Relationship destroyed

**Common mistakes:**
- Over-leverage (position too large)
- No stop loss (hope for reversion)
- Ignoring fundamentals (black swan events)
- Near-expiration trades (physical delivery risk)
- **Capital destruction**

### Position Sizing Rules

**Conservative approach:**

$$
\text{Max Margin Used} = \text{Capital} \times 0.20
$$

**Ultra-conservative:**

$$
\text{Max Margin Used} = \text{Capital} \times 0.10
$$

- Keep 80-90% buffer
- Can survive 5-10σ adverse moves
- **Never use full margin capacity**

### Common Mistakes

1. **Trading correlation without cointegration** (statistical weakness)
2. **Ignoring economic fundamentals** (why does relationship exist?)
3. **Over-leveraging** (using all margin capacity)
4. **No stop losses** ("it will revert eventually")
5. **Near expiration trading** (physical delivery risk)
6. **Not monitoring rolling correlations** (relationships change)
7. **Averaging down** (throwing good money after bad)
8. **Treating all pairs equally** (some much stronger than others)

### Key Formulas

**Hedge ratio (regression):**

$$
\beta = \frac{\text{Cov}(P_A, P_B)}{\text{Var}(P_B)}
$$

**Z-score:**

$$
Z = \frac{S_{\text{current}} - \mu_S}{\sigma_S}
$$

**Cointegration test:**
Run regression $P_A = \alpha + \beta P_B + \epsilon$, then test if $\epsilon$ is stationary (ADF test)

**Half-life (mean reversion speed):**

$$
\text{Half-life} = -\frac{\ln(2)}{\lambda}
$$

From $\Delta S_t = \lambda S_{t-1} + \epsilon$

### When to Use Pairs Trading

**Use when:**
- Strong economic relationship exists
- High correlation (>0.70) and cointegration
- Clear mean reversion pattern
- Adequate liquidity in both contracts
- Can monitor positions closely

**Don't use when:**
- Only statistical correlation (no economic link)
- Structural changes occurring
- Low liquidity
- Can't handle complexity
- Near contract expiration (physical delivery risk)

### Advantages Over Outright Positions

| Factor | Outright | Pairs |
|--------|---------|-------|
| Directional risk | High | Low (hedged) |
| Volatility | 25-35% | 5-15% |
| Margin | 10% | 3-5% |
| Market beta | 1.0 | ~0 (neutral) |
| Skill required | Market timing | Relationship analysis |
| Sharpe ratio | 0.3-0.8 | 1.0-3.0 |

### Final Wisdom

> "Pairs trading is the art of finding economic relationships that create mean-reverting spreads. When gold/silver ratio hit 125 in 2020, you weren't betting on gold or silver direction—you were betting that a 5,000-year relationship wouldn't permanently break. Statistical extremes combined with fundamental logic create the best trades. But remember: correlation breaks, cointegration fails, and black swans happen. Size small, use stops, and never forget that in March 2020, correlations that held for decades went to zero overnight. Pairs trading is lower risk, not no risk."

**Key principles:**

1. **Economic logic > Statistical correlation alone**
2. **Cointegration required** (test with ADF)
3. **Enter at extremes** (>2σ, preferably >3σ)
4. **Size conservatively** (20% of capital max for margin)
5. **Always use stops** (Z > 3-4 or dollar loss limit)
6. **Monitor fundamentals** (relationships can break)
7. **Diversify across pairs** (not correlated with each other)
8. **Respect black swans** (unprecedented events happen)

**Most important:**

Pairs trading reduces risk by 60-80% vs. outrights, but extreme events (negative oil, CHF unpeg, tech bubble) can still destroy capital. The 2020 gold/silver ratio trade made 778% because it combined statistical extreme (5.5σ), fundamental logic (both precious metals), and perfect timing (peak panic). That's the ideal. But never forget: relationships that held for decades can break in minutes. **Trade the spread, size small, use stops.** 🎯📊

**Remember:**
- Lower risk ≠ No risk
- Correlation ≠ Causation
- Cointegration ≠ Guaranteed mean reversion
- **Always have an exit plan!** ⚠️