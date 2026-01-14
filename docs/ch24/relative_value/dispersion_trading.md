# Dispersion Trading


**Dispersion trading** is a volatility arbitrage strategy that exploits the difference between index implied volatility and the weighted average of constituent stock implied volatilities, profiting from changes in correlation structure.

---

## The Core Insight


**The fundamental idea:**

- Index volatility depends on correlation between stocks
- When correlation is high, index moves like components
- When correlation is low, stocks move independently (dispersion)
- Index options typically cheaper than sum of stock options
- This gap widens and narrows (tradeable)
- Short index vol, long stock vol = long dispersion

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/dispersion_trading.png?raw=true" alt="dispersion_trading" width="700">
</p>
**Figure 1:** Dispersion P&L diagram showing profit when realized correlation falls below implied correlation, as individual stocks move independently while the index remains range-bound.

**You're essentially betting: "Stocks will move independently rather than together, making the index less volatile than the sum of its parts."**

---

## What Is Dispersion Trading?


### 1. Basic Definition


**The mathematical setup:**

Index variance relates to stock variances via correlation:

$$
\sigma_{\text{index}}^2 = \sum_{i=1}^{N} w_i^2 \sigma_i^2 + 2\sum_{i<j} w_i w_j \rho_{ij} \sigma_i \sigma_j
$$

Where:
- $\sigma_{\text{index}}$ = Index volatility
- $w_i$ = Weight of stock $i$ in index
- $\sigma_i$ = Volatility of stock $i$
- $\rho_{ij}$ = Correlation between stocks $i$ and $j$

**Key insight:**

$$
\sigma_{\text{index}} < \text{Weighted Average}(\sigma_i) \quad \text{when } \rho < 1
$$

**The lower the correlation, the bigger the gap!**

### 2. The Trade Structure


**Classic dispersion trade:**

**Short leg (sell index volatility):**
- Sell index options (SPX straddles or variance swaps)
- Collect index implied volatility premium
- Bet index will be calm

**Long leg (buy stock volatility):**
- Buy options on individual stocks (straddles or variance)
- Pay stock implied volatility premiums
- Bet stocks will be volatile

**Net position:**
- Long realized dispersion (stocks move, index doesn't)
- Short implied correlation
- Delta-neutral (hedged continuously)

### 3. Implied vs Realized Correlation


**Implied correlation:**

Backed out from index and stock option prices:

$$
\rho^{\text{implied}} = \text{f}(\sigma_{\text{index}}^{\text{implied}}, \sigma_i^{\text{implied}}, w_i)
$$

Typically 40-70% for SPX.

**Realized correlation:**

Computed from actual stock returns:

$$
\rho_{ij}^{\text{realized}} = \frac{\text{Cov}(r_i, r_j)}{\sigma_i \sigma_j}
$$

**Dispersion profit when:**

$$
\rho^{\text{realized}} < \rho^{\text{implied}}
$$

**Stocks move independently (low correlation) but you sold high-correlation index vol.**

### 4. Why Dispersion Exists


**Structural reasons for the gap:**

**Supply/demand imbalance:**
- High demand for index hedging (institutional portfolios)
- Index options expensive (bid up)
- Single-stock options less demand
- Creates systematic gap

**Correlation risk premium:**
- Investors fear systemic risk (all stocks down together)
- Willing to overpay for index protection
- Correlation risk priced in
- Harvested by dispersion traders

**Diversification illusion:**
- Index volatility "feels safer" (diversified)
- But implied vol doesn't fully reflect diversification benefit
- Gap between perception and reality

**Behavioral factors:**
- Herding during crises (correlation spikes)
- Fear trades correlated
- Greed more idiosyncratic

### 5. Historical Patterns


**Empirical evidence (SPX, 1996-2023):**

**Average implied correlation:**
- Normal markets: 50-60%
- Bull markets: 40-50%
- Bear markets/crises: 70-90%

**Average realized correlation:**
- Normal markets: 30-40%
- Bull markets: 20-30%
- Bear markets/crises: 60-80%

**Dispersion opportunity:**
- Implied typically 10-20% above realized
- Gap widens in calm markets
- Gap narrows (or inverts) in crises

**Performance:**
- Profitable 60-70% of months
- Loss months severe (correlation spikes)
- Sharpe ratio: 0.3-0.6 (after hedging costs)

### 6. Trade Sizing


**Vega-neutral dispersion:**

To neutralize overall volatility exposure:

$$
N_{\text{stocks}} = \frac{\sigma_{\text{index}} \times N_{\text{index}}}{\text{Weighted Avg}(\sigma_i)}
$$

**Example:**
- Short 10 SPX straddles (vega = $\$50,000$)
- Index vol = 20%
- Stock avg vol = 30%
- **Long stock vega needed:** $\$50,000 \times 20\% / 30\% = \$33,333$

**But typically underhedge slightly (60-80% vega) to:**
- Account for correlation risk premium
- Reduce hedging costs
- Express mild short volatility bias

### 7. Basket Selection


**Choosing which stocks:**

**Large-cap stocks (typical):**
- AAPL, MSFT, GOOGL, AMZN, NVDA, META, TSLA, etc.
- High liquidity in options
- Highest weights in SPX
- Represent 30-40% of index

**Criteria:**
- Liquid options (volume > 1,000/day)
- Tight bid-ask spreads (< 5% of premium)
- High index weight (> 1%)
- Low idiosyncratic risk (avoid single-stock blowups)

**Typical basket:**
- 10-20 stocks
- Replicate ~50% of index
- Weighted by index weights (modified)

---

## Dispersion Trade Variants


**Different ways to express the trade:**

### 1. Vanilla Dispersion


**Structure:**

- Short index variance swap
- Long single-stock variance swaps
- Vega-weighted (70-80% hedge)
- Hold to maturity

**Example:**
- Short 1 SPX variance, strike = 400 (20% vol)
- Long 10 stocks, avg strike = 625 (25% vol)
- Notional ratio: 1:10

**P&L at maturity:**

$$
\text{P&L} = N_{\text{idx}} \times (K_{\text{idx}} - \text{RV}_{\text{idx}}) + \sum_{i=1}^{10} N_i \times (\text{RV}_i - K_i)
$$

**Profit if:** Individual stocks realize high vol, index realizes low vol

### 2. Straddle Dispersion


**Structure:**

- Short ATM index straddles
- Long ATM stock straddles
- Delta-hedge all positions daily
- Realize gamma/theta P&L

**Example:**
- Sell 5 SPX ATM straddles
- Buy 50 stock ATM straddles (10 names, 5 each)
- Hedge delta continuously

**P&L sources:**
- Gamma gains on stocks (when volatile)
- Gamma losses on index (when volatile)
- Net theta collection
- **Profit if stocks move, index doesn't**

### 3. Calendar Dispersion


**Structure:**

- Short near-term index straddles
- Long longer-term stock straddles
- Capture term structure + dispersion
- Roll near-term monthly

**Rationale:**
- Near-term correlation higher (shorter = more correlated)
- Longer-term correlation lower (more time for divergence)
- Double alpha: dispersion + term structure

### 4. Skew Dispersion


**Structure:**

- Focus on put skew differential
- Index puts expensive (systemic risk premium)
- Stock puts less expensive
- Trade the skew gap

**Implementation:**
- Short OTM index puts
- Long OTM stock puts (weighted)
- Capture skew + correlation premium

### 5. Dynamic Dispersion


**Structure:**

- Start with standard dispersion
- Adjust hedge ratio based on realized correlation
- If correlation rises → increase stock vega
- If correlation falls → reduce stock vega

**Formula:**

$$
\text{Hedge Ratio}(t) = \text{Base Ratio} \times \left(1 + \beta \times (\rho_t^{\text{realized}} - \rho_0)\right)
$$

**Benefits:**
- Adapts to market regime
- Reduces losses when correlation spikes
- Enhances gains when dispersion widens

### 6. Cross-Sector Dispersion


**Structure:**

- Trade dispersion within sectors
- Example: Tech sector index vs. tech stocks
- Or consumer sector vs. consumer stocks

**Advantage:**
- Higher correlation baseline (same sector)
- More stable trade
- Less exposure to market-wide correlation shifts

### 7. International Dispersion


**Structure:**

- Short US index volatility
- Long emerging market stock volatility
- Or short Europe index, long European stocks

**Rationale:**
- Cross-country correlation varies
- Exploit country-specific correlation premiums
- Diversify dispersion risk

---

## Mathematical Framework


### 1. Correlation Decomposition


**Index variance formula:**

$$
\sigma_{\text{index}}^2 = \underbrace{\sum_{i=1}^{N} w_i^2 \sigma_i^2}_{\text{Idiosyncratic}} + \underbrace{2\sum_{i<j} w_i w_j \rho_{ij} \sigma_i \sigma_j}_{\text{Correlation}}
$$

**For equal-weighted index:**

$$
\sigma_{\text{index}}^2 \approx \frac{1}{N}\overline{\sigma^2} + \left(1 - \frac{1}{N}\right)\overline{\rho}\,\overline{\sigma^2}
$$

**As $N \to \infty$:**

$$
\sigma_{\text{index}}^2 \to \overline{\rho}\,\overline{\sigma^2}
$$

**Index volatility purely driven by correlation for large $N$!**

### 2. Dispersion P&L


**Net P&L from dispersion:**

$$
\text{P&L} = N_{\text{idx}} \times (\sigma_{\text{idx}}^{\text{impl}} - \sigma_{\text{idx}}^{\text{real}})^2 - \sum_{i=1}^{N} N_i \times (\sigma_i^{\text{impl}} - \sigma_i^{\text{real}})^2
$$

**Simplified (vega-neutral):**

$$
\text{P&L} \propto (\rho^{\text{impl}} - \rho^{\text{real}}) \times \overline{\sigma^2}
$$

**Profit drivers:**
1. Implied correlation > Realized correlation (primary)
2. Stock volatilities exceed implied (secondary)
3. Index volatility below implied (secondary)

### 3. Optimal Hedge Ratio


**Minimize variance of P&L:**

$$
h^* = \frac{\text{Cov}(\text{Index Vol}, \text{Stock Vol})}{\text{Var}(\text{Stock Vol})}
$$

**Empirically:**

$$
h^* \approx 0.6\text{-}0.8
$$

**Interpretation:**
- Not 100% hedge (correlation risk premium)
- Underhedge to harvest premium
- Balance risk/return

### 4. Greeks Exposure


**Delta:**

$$
\Delta_{\text{net}} = 0 \quad \text{(by construction, hedged daily)}
$$

**Gamma:**

$$
\Gamma_{\text{net}} = \sum_{i=1}^{N} \Gamma_i - \Gamma_{\text{idx}} > 0
$$

**Positive net gamma (long realized vol)**

**Vega:**

$$
\text{Vega}_{\text{net}} = \sum_{i=1}^{N} \nu_i - \nu_{\text{idx}} \approx 0
$$

**Vega-neutral (correlation bet, not vol bet)**

**Theta:**

$$
\Theta_{\text{net}} = \Theta_{\text{idx}} - \sum_{i=1}^{N} \Theta_i < 0
$$

**Negative theta (pay time decay on net)**

### 5. Correlation Sensitivity


**P&L sensitivity to correlation:**

$$
\frac{\partial \text{P&L}}{\partial \rho} \approx -N_{\text{idx}} \times 2\overline{\sigma^2} \times \sum_{i<j} w_i w_j
$$

**For SPX with typical weights:**

$$
\frac{\partial \text{P&L}}{\partial \rho} \approx -\$100,000 \text{ per 1% correlation change}
$$

**10% correlation increase → -$\$1,000,000$ loss**

**This is the main risk!**

### 6. Expected Return


**Theoretical expected return:**

$$
\mathbb{E}[\text{Return}] = \underbrace{\text{Correlation Risk Premium}}_{\text{Harvest}} - \underbrace{\text{Hedging Costs}}_{\text{Delta Hedging}} - \underbrace{\text{Theta Decay}}_{\text{Net Time Value}}
$$

**Empirical:**
- Correlation premium: +5-10% annually
- Hedging costs: -2-3% annually
- Theta decay: -2-3% annually
- **Net: +1-5% annually (small edge)**

### 7. Risk Decomposition


**Sources of risk:**

$$
\text{Var}(\text{P&L}) = \underbrace{\text{Correlation Risk}}_{\text{Dominant}} + \underbrace{\text{Volatility Risk}}_{\text{Hedging Error}} + \underbrace{\text{Idiosyncratic Risk}}_{\text{Single Stocks}}
$$

**Typical contribution:**
- Correlation risk: 70-80% of variance
- Volatility risk: 10-20%
- Idiosyncratic: 5-10%

**Correlation risk dominates!**

---

## Common Mistakes


**Pitfalls to avoid:**

### 1. Ignoring Correlation Spikes


**Mistake:** Assume correlation stable

**Why it fails:** Correlation spikes in crises

**Example:**
- Enter dispersion with $\rho = 40\%$
- Crisis hits, $\rho \to 80\%$
- Index vol explodes, stock vols converge
- **Massive losses on both legs**

**Historical spikes:**
- 2008: 40% → 85%
- 2011 (Euro crisis): 45% → 75%
- 2020 (COVID): 35% → 80%

**Fix:**
- Monitor correlation daily
- Exit when $\rho > 60\%$
- Reduce exposure in elevated correlation regimes

### 2. Oversizing Positions


**Mistake:** Large notional on dispersion

**Why it fails:** Correlation risk extreme

**Example:**
- $\$10M$ portfolio
- $\$5M$ dispersion notional (50%!)
- Correlation spikes 20%
- Loss: $\$5M \times 20\% \times 2 = \$2M$ (20% of portfolio)

**Fix:**
- Max 10-15% of portfolio in dispersion
- 5% safer for retail/smaller funds
- Scale down when correlation elevated

### 3. Poor Stock Selection


**Mistake:** Include illiquid or uncorrelated stocks

**Why it fails:** Wide spreads, poor hedging

**Example:**
- Include biotech stock (uncorrelated to SPX)
- Option bid-ask 10% wide
- Transaction costs eat profit
- Idiosyncratic risk high

**Fix:**
- Stick to large-cap liquid names
- Check correlation to index (> 0.5)
- Verify option volume > 1,000/day
- Avoid single-stock blowup risk

### 4. Neglecting Hedging Costs


**Mistake:** Ignore daily delta hedging friction

**Why it fails:** Costs compound

**Example:**
- 20 positions hedged daily
- Average cost: 0.5% per hedge
- 252 trading days
- **Annual cost: 0.5% × 20 × 252 = 252% (eats all profit!)**

**Fix:**
- Model hedging costs before entering
- Use gamma-scalping strategies
- Consider hedging every 2-3 days (not daily)
- Larger trades (lower per-unit cost)

### 5. Wrong Hedge Ratio


**Mistake:** Full 100% vega hedge

**Why it fails:** No correlation premium harvest

**Example:**
- Short $\$100k$ index vega
- Long $\$100k$ stock vega
- Fully hedged (correlation neutral)
- **No expected return!**

**Optimal:**
- 60-80% hedge ratio
- Leaves room for correlation premium
- Balance risk/return

**Fix:** Use 70% as starting point, adjust based on market regime

### 6. Ignoring Skew


**Mistake:** Trade ATM only, ignore skew

**Why it fails:** Miss valuable skew premium

**Example:**
- Index put skew 5% higher than stock put skew
- Shorting index puts captures extra premium
- But you only traded ATM straddles
- **Left money on table**

**Fix:**
- Include OTM puts (25-delta)
- Harvest index put skew premium
- Enhances dispersion returns 1-2%

### 7. No Exit Plan


**Mistake:** Hold to maturity regardless

**Why it fails:** Correlation can stay elevated

**Example:**
- Enter dispersion, $\rho = 40\%$
- 2 months later, $\rho = 70\%$
- Down 50%, hope for reversion
- **Correlation stays high, full loss**

**Fix:**
- Stop-loss at $\rho > 60\%$
- Take profit at $\rho < 30\%$
- Time stop: exit if no profit after 50% of duration

### 8. Forgetting Dividends


**Mistake:** Ignore dividend impact

**Why it fails:** Affects option pricing

**Example:**
- Large dividend payment
- Stock drops ex-dividend
- Option value shifts
- P&L distorted

**Fix:**
- Use dividend-adjusted strikes
- Monitor ex-dividend dates
- Consider dividend risk in sizing

---

## Risk Management Rules


### 1. Position Sizing


**Maximum allocation:**

$$
\text{Max Notional} = \min\left(15\% \times \text{Portfolio}, \, \frac{\text{Portfolio} \times 0.05}{\Delta \rho_{\text{max}}}\right)
$$

Where $\Delta \rho_{\text{max}}$ is maximum expected correlation move (e.g., 20%).

**Example:**
- $\$10M$ portfolio
- Max correlation move: 20% (40% → 60%)
- **Max notional:** $\$10M \times 0.05 / 0.20 = \$2.5M$

**Rule of thumb:** Never exceed 15% of portfolio

### 2. Entry Conditions


**Only enter when:**

- Implied correlation > 50%
- Realized correlation < 40% (at least 10% gap)
- VIX < 25 (not crisis)
- No major events next 2 weeks
- Option liquidity sufficient (vol > 1,000)

**Avoid when:**
- Correlation > 60% (too high)
- Recent correlation spike (persistence)
- Major macro event imminent

### 3. Stop-Loss Rules


**Hard stops:**

- **Correlation > 60% → Exit immediately**
- P&L loss > -20% → Exit
- VIX spike > 30 → Reduce by 50%
- Individual stock blowup → Exit that stock

**No waiting for mean reversion**

### 4. Dynamic Hedging


**Adjust hedge ratio based on realized correlation:**

$$
h(t) = h_{\text{base}} \times \left(1 + 0.5 \times \frac{\rho_t - \rho_0}{\rho_0}\right)
$$

**Example:**
- Base hedge: 70%
- $\rho_0 = 40\%$, current $\rho_t = 50\%$

**New hedge:**
$$
h(t) = 0.70 \times \left(1 + 0.5 \times \frac{50\% - 40\%}{40\%}\right) = 0.70 \times 1.125 = 78.75\%
$$

**Increase stock vega when correlation rises**

### 5. Monitoring


**Daily checklist:**

- Realized correlation (rolling 20-day)
- Implied correlation (from option prices)
- Delta of all positions (rehedge if needed)
- VIX level
- Individual stock news (earnings, FDA, etc.)

**Weekly review:**

- P&L attribution (correlation, vol, hedging)
- Position Greeks (gamma, vega, theta)
- Upcoming events (dividends, earnings)
- Rebalance weights if needed

### 6. Diversification


**Spread risk across:**

- Multiple baskets (tech, financials, healthcare)
- Multiple maturities (1M, 2M, 3M)
- Mix with other strategies (VRP, carry)
- Don't concentrate in single sector

**Correlation between dispersion trades:**
- Same market: ~0.8 correlation
- Different markets (US, EU, Asia): ~0.5
- Still benefits from some diversification

### 7. Hedging Tail Risk


**For extreme correlation spikes:**

- Buy OTM index calls (hedge short index vol)
- Costs 0.3-0.5% of notional
- Caps losses when correlation explodes
- Essential in large positions

**Example:**
- Short $\$2M$ index variance
- Buy 20% OTM SPX calls
- Cost: $\$10,000$
- Caps max loss at $\$500,000$ (vs. unlimited)

---

## Real-World Examples


### 1. The FANG Era (2014-2016)


**Setup:**

- FANG stocks (FB, AAPL, NFLX, GOOGL) dominating
- High idiosyncratic volatility
- Low correlation (stock-picking environment)
- Implied correlation: 55%

**Trade:**
- Short SPX variance, strike = 324 (18% vol)
- Long 10 stocks (FANG + others), avg strike = 625 (25% vol)
- Vega ratio: 1:10 (70% hedge)

**Outcome (2 years):**
- Realized correlation: 35% (20% below implied)
- SPX realized: 256 (16% vol) vs. strike 324
- Stocks realized: 550 (23.5% vol) vs. strike 625

**P&L:**
- Index leg: $\$1,000 × (324 - 256) = +\$68,000$
- Stock leg: $\$100 × 10 × (550 - 625) = -\$75,000$
- **Net: -$\$7,000$ (small loss)**

**Lesson:** Need bigger correlation gap or better timing

### 2. Post-Crisis (2010-2011)


**Setup:**

- Post-2008, markets calming
- Dispersion increasing (rotation plays)
- Implied correlation: 60%, realized: 38%

**Trade:**
- Dispersion on SPX, 3-month horizon
- $\$500,000$ notional

**Outcome:**
- Correlation fell from 60% → 35%
- Massive dispersion
- **Profit: $\$125,000$ (25%)**

**Lesson:** Post-crisis normalization ideal for dispersion

### 3. COVID Crash (March 2020)


**Setup:**

- Feb 2020: Dispersion trade on, $\rho = 45\%$
- March: Correlation spiked to 82%

**Trade:**
- Short SPX variance at 256 (16% vol)
- Long stocks at avg 625 (25% vol)

**Outcome:**
- SPX variance realized: 2,500 (50% vol!)
- Stock variances: ~2,000 (45% vol)
- Correlation collapse killed the trade

**P&L:**
- Index: $\$1,000 × (256 - 2,500) = -\$2,244,000$
- Stocks: $\$100 × 10 × (2,000 - 625) = +\$1,375,000$
- **Net: -$\$869,000$ (87% loss)**

**Lesson:** Correlation spikes destroy dispersion trades

### 4. Skew-Enhanced Dispersion (2018-2019)


**Setup:**

- Standard dispersion not working (low edge)
- Added skew component (short index puts, long stock puts)

**Trade:**
- Short SPX 10% OTM puts
- Long stock 10% OTM puts (weighted)
- 6-month horizon

**Outcome:**
- Captured index put skew premium (3% extra)
- Correlation stable around 50%
- Skew component added +$\$45,000$
- Standard dispersion added +$\$20,000$
- **Total: +$\$65,000$ (13%)**

**Lesson:** Skew enhancement improves dispersion returns

---

## Practical Steps


### 1. Pre-Trade Setup


**Before entering dispersion:**

1. **Calculate implied correlation:**
   - Get index ATM implied vol
   - Get stock ATM implied vols (weighted)
   - Back out implied correlation

2. **Measure realized correlation:**
   - Compute rolling 20-day stock correlations
   - Weight average
   - Compare to implied

3. **Check gap:**
   - Need implied > realized by 10%+ for trade
   - Larger gap = better opportunity

### 2. Stock Selection


**Choose basket:**

- 10-20 large-cap stocks
- Top index weights (AAPL, MSFT, GOOGL, etc.)
- High option liquidity (vol > 1,000/day)
- Correlation to index > 0.5
- Avoid sector concentration

**Example SPX basket:**
- AAPL, MSFT, GOOGL, AMZN, NVDA (tech)
- JPM, BAC (financials)
- JNJ, UNH (healthcare)
- XOM (energy)
- TSLA (consumer)

### 3. Position Sizing


**Calculate notionals:**

$$
N_{\text{index}} = \frac{\text{Dispersion Budget}}{\text{Expected Correlation Move} \times 2}
$$

**Example:**
- Budget: $\$500,000$ (5% of $\$10M portfolio)
- Expected correlation move: 15%
- **Index notional:** $\$500,000 / (0.15 × 2) = \$1,666,667$

**Stock notional:**
$$
N_{\text{stocks}} = N_{\text{index}} \times 0.70 = \$1,166,667
$$

### 4. Execution


**Enter positions:**

- Sell index variance swap or straddles
- Buy stock variance swaps or straddles
- Use limit orders (never market)
- Stagger entries over 2-3 days
- Check bid-ask (should be < 5%)

**Example:**
- Sell 5 SPX variance swaps at 400
- Buy 50 stock variance swaps (10 names × 5 each)
- Vega-weighted to 70% hedge

### 5. Ongoing Management


**Daily tasks:**

- Compute realized correlation
- Check P&L attribution (correlation vs. vol)
- Delta-hedge if needed
- Monitor VIX and skew

**Weekly tasks:**

- Rebalance delta hedge
- Check upcoming events (earnings)
- Review stop-loss levels
- Adjust hedge ratio if correlation shifted

### 6. Exit Discipline


**Exit immediately if:**

- Realized correlation > 60%
- P&L < -20%
- VIX > 35
- Major crisis emerging

**Take profits when:**

- P&L > +20% (take half)
- Realized correlation < 30% (target hit)
- Time decay approaching (theta bite)

**Time-based exit:**

- Exit at 80% of trade duration if flat
- Don't hold to maturity hoping for miracle

---

## Final Wisdom


> "Dispersion trading is a sophisticated correlation arbitrage that works beautifully when markets transition from risk-on to stock-picking environments. The correlation risk premium is real and persistent, but it's overwhelmed by correlation spikes during crises. The key is rigorous risk management: small position sizes, hard stop-losses when correlation rises above 60%, and constant monitoring of the correlation gap. This is not a 'set and forget' trade - it requires active management, daily hedging, and the discipline to exit when the correlation regime shifts. Treat it as harvesting a small, steady edge rather than a home-run trade."

**Key to success:**

- Only enter when implied correlation > realized by 10%+
- Position size for 20% correlation spike (max 15% portfolio)
- Stop-loss at realized correlation > 60%
- Select liquid, large-cap stocks only
- Hedge at 70% vega ratio (not 100%)
- Monitor correlation daily, rehedge weekly
- Enhance with skew trades for extra edge
- Remember: You're short correlation, which spikes in crises
