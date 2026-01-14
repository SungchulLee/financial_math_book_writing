# Variance Risk Premium


**Variance risk premium (VRP)** is the difference between implied variance (from option prices) and realized variance (from actual stock returns), representing the compensation investors demand for bearing volatility risk.

---

## The Core Insight


**The fundamental idea:**

- Option prices embed expected future volatility
- Implied variance typically exceeds realized variance
- Investors overpay for volatility protection
- This creates systematic profit opportunity
- VRP exists as compensation for tail risk
- Selling volatility harvests this premium

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/variance_risk_premium.png?raw=true" alt="variance_risk_premium" width="700">
</p>
**Figure 1:** Time series of variance risk premium showing persistent positive gap between implied and realized variance, with occasional spikes during market crashes representing the cost of selling volatility insurance.

**You're essentially asking: "How much do investors overpay for volatility insurance, and can I systematically profit from this?"**

---

## What Is VRP?


### 1. Definition


**The formal definition:**

The variance risk premium is:

$$
\text{VRP} = \text{Implied Variance} - \mathbb{E}[\text{Realized Variance}]
$$

Or more precisely:

$$
\text{VRP}_t = \mathbb{E}_t^Q[\text{RV}_{t,t+\tau}] - \mathbb{E}_t^P[\text{RV}_{t,t+\tau}]
$$

Where:
- $\mathbb{E}^Q$ = Risk-neutral expectation (from option prices)
- $\mathbb{E}^P$ = Physical expectation (actual future realized variance)
- $\text{RV}_{t,t+\tau}$ = Realized variance from time $t$ to $t+\tau$
- $\tau$ = Time horizon (typically 1-3 months)

**Practical measurement:**

$$
\text{VRP}_t = \text{IV}^2_t - \text{RV}_{t,t+\tau}
$$

Where:
- $\text{IV}_t$ = Implied volatility from ATM options at time $t$
- $\text{RV}_{t,t+\tau}$ = Actual realized volatility over next $\tau$ period

**Units:** Variance points (annualized)

### 2. Why VRP Exists


**Economic rationale:**

**Supply/demand imbalance:**

- Demand: Investors want volatility protection (hedging)
- Supply: Limited capital willing to short volatility (tail risk)
- Result: Implied variance > realized variance (most of the time)

**Tail risk aversion:**

- Markets occasionally crash (fat tails)
- Long volatility protects in crashes
- Investors overpay for this insurance
- Short volatility sellers demand compensation

**Leverage constraints:**

- Institutions cannot easily replicate volatility payoffs
- Options provide unique convexity
- Premium paid for this unique exposure

**Behavioral factors:**

- Fear overvalued vs. greed
- Recency bias after crashes
- Loss aversion drives hedging demand

### 3. Historical Magnitudes


**Empirical evidence:**

**S&P 500 (1990-2020 average):**

- Average implied volatility: 19.5%
- Average realized volatility: 16.0%
- **Variance risk premium: ~90-100 variance points**
- **Vol premium: ~3.5% annualized**

**Translation:**

- Implied variance: $19.5^2 = 380$
- Realized variance: $16.0^2 = 256$
- **VRP: $380 - 256 = 124$ variance points**

**Time variation:**

- Normal markets: VRP ≈ 100-150 variance points
- Crisis periods: VRP ≈ -500 to -1,000 (negative!)
- Post-crisis: VRP ≈ 200-300 (elevated)

**Other assets:**

- Individual stocks: VRP ≈ 150-200 variance points
- Emerging markets: VRP ≈ 200-400 variance points
- Currencies: VRP ≈ 50-100 variance points

### 4. Risk-Neutral vs Physical


**Two probability measures:**

**Risk-neutral measure ($\mathbb{Q}$):**

- Derived from option prices
- Includes risk premium
- What market prices imply
- $\mathbb{E}^Q[\text{RV}]$ = Implied variance

**Physical measure ($\mathbb{P}$):**

- Actual probability distribution
- What will actually happen
- Historical realized variance
- $\mathbb{E}^P[\text{RV}]$ = Expected realized variance

**The gap:**

$$
\text{VRP} = \mathbb{E}^Q[\text{RV}] - \mathbb{E}^P[\text{RV}]
$$

**This is the risk premium for bearing volatility risk.**

### 5. Measurement Challenges


**Practical issues:**

**Forward-looking realized variance unknown:**

- We observe $\text{IV}_t$ today
- But $\text{RV}_{t,t+\tau}$ only known after $\tau$ periods
- Must estimate $\mathbb{E}^P[\text{RV}]$ using historical data

**Approaches:**

1. **Ex-post VRP (common):**
   - $\text{VRP}_t = \text{IV}^2_t - \text{RV}_{t,t+\tau}$
   - Uses actual realized variance
   - Includes estimation error

2. **Model-based VRP:**
   - Estimate $\mathbb{E}^P[\text{RV}]$ using GARCH, HAR, etc.
   - $\text{VRP}_t = \text{IV}^2_t - \widehat{\mathbb{E}^P[\text{RV}]}$
   - Reduces noise but adds model risk

3. **Survey-based VRP:**
   - Use analyst forecasts for expected vol
   - Rare and subjective

**Maturity matching:**

- Match option maturity to realized variance window
- 30-day options → 30-day realized variance
- Avoid mixing horizons

### 6. VRP Across Maturities


**Term structure of VRP:**

VRP varies by maturity:

$$
\text{VRP}(\tau) = \text{IV}^2(\tau) - \mathbb{E}[\text{RV}_\tau]
$$

**Typical pattern:**

- **Short-term (1M):** High VRP (150-200 variance points)
  - Near-term fears priced in
  - High hedging demand

- **Medium-term (3M):** Moderate VRP (100-150 variance points)
  - Most liquid
  - Balanced supply/demand

- **Long-term (6M+):** Lower VRP (50-100 variance points)
  - Mean reversion expected
  - Less hedging demand

**Trading implication:**

- Short short-term variance (highest premium)
- Long long-term variance (cheaper)
- Harvest term structure

### 7. VRP Predictability


**Is VRP predictable?**

**Evidence:**

- VRP exhibits time-variation
- High when VIX low (complacency)
- Low/negative when VIX high (crisis)
- Mean-reverting over quarters

**Predictive factors:**

1. **VIX level:**
   - Low VIX → High VRP
   - High VIX → Low/negative VRP
   - Inverse relationship

2. **VIX term structure:**
   - Contango → Positive VRP
   - Backwardation → Negative VRP

3. **Market conditions:**
   - Bull markets → High VRP
   - Bear markets → Low VRP

4. **Economic uncertainty:**
   - Low uncertainty → High VRP
   - High uncertainty → Low VRP

**Practical use:**

- Scale VRP harvesting with VIX
- Reduce exposure when VIX > 30
- Increase when VIX < 15

---

## VRP Harvesting Strategies


**How to profit from VRP:**

### 1. Short Variance Swaps


**Systematic selling:**

**Strategy:**

- Continuously short 1-3 month variance swaps
- Roll monthly
- Collect VRP each period
- Expect positive return (most periods)
- Occasional large losses (crashes)

**Example:**

- Short 3M variance, strike = 400 (20% vol)
- Average realized variance = 300 (17.3% vol)
- **VRP harvest: 100 variance points per trade**

**With $\$1,000$ variance notional:**

- Average profit: $\$1,000 \times 100 = \$100,000$ per quarter
- Annualized: ~$\$400,000$

**Risk:**

- Flash crash: variance spikes to 2,500
- **Loss:** $\$1,000 \times (400 - 2,500) = -\$2,100,000$
- **One bad quarter wipes out 5+ years of profits**

**Risk management critical:**

- Small position size (1-2% of portfolio)
- Stop-losses
- Tail hedges (OTM puts)
- Dynamic scaling (reduce when VIX high)

### 2. Short Volatility ETPs


**Levered short vol:**

**Instruments:**

- XIV (shut down after 2018 crash)
- SVXY (short VIX futures)
- ZIV (short mid-term VIX futures)

**Strategy:**

- Buy short-vol ETPs
- Harvest VIX futures contango
- Collect roll yield + VRP

**Historical performance (2011-2017):**

- SVXY: +200% per year (geometric)
- But: -90% drawdown in Feb 2018
- XIV: Terminated after losing 95% in one day

**Current alternatives:**

- Short VIX futures directly
- Short volatility options
- More controlled than ETPs

### 3. Sell ATM Straddles


**Delta-neutral premium collection:**

**Strategy:**

- Sell ATM straddles monthly
- Delta hedge continuously
- Collect theta + VRP
- Profit if realized vol < implied vol

**Example:**

- SPX at 4,500
- Sell 30-day ATM straddle for $150 (20% IV)
- Implied variance: 400
- Realized variance: 300 (if typical VRP)

**Profit sources:**

- Theta decay: ~$5/day
- VRP: Realized vol lower than implied
- **Total:** $50-100 per straddle

**Risk:**

- Gamma exposure during large moves
- Hedging costs eat profits
- Tail events catastrophic

**Better:** Combine with protective options

### 4. Short Put Spreads


**Limited risk VRP harvest:**

**Strategy:**

- Sell OTM put spreads (bull put spread)
- Collect premium (includes VRP)
- Limited downside (spread width)
- Harvest VRP with defined risk

**Example:**

- SPX at 4,500
- Sell 4,400/4,300 put spread
- Collect $30 premium
- Max loss: $70 (spread width - premium)
- Risk/reward: $30 profit vs. $70 loss

**Probability of profit:**

- If implied vol = 20%, realized = 17%
- Higher probability of expiring worthless
- **VRP tilts odds in your favor**

**Advantages:**

- Defined risk
- Lower capital requirement
- Scales easily

### 5. Ratio Call Spreads


**Skew exploitation:**

**Strategy:**

- Sell OTM call spreads
- Use call skew (lower IV than puts)
- Less VRP but less risk
- Bet on upside not realized

**Example:**

- Sell 2x 4,600 calls
- Buy 1x 4,700 call
- Net credit: $20

**VRP component:**

- Calls also have VRP (smaller)
- Upside moves less frequent than feared
- Collect small premium repeatedly

### 6. Covered Calls


**Equity + short calls:**

**Strategy:**

- Own stock (or index ETF)
- Sell monthly OTM calls
- Collect premium enhanced by VRP
- Give up some upside

**Example:**

- Own 100 SPY shares at $450
- Sell $460 call for $5
- Collect $500/month
- Annualized: ~13% yield (if not called)

**VRP contribution:**

- Call IV > expected realized
- Repeated premium collection
- Enhance returns by 2-4% annually

### 7. Dispersion Trading


**Index vs single stocks:**

**Strategy:**

- Short index variance
- Long single-stock variances (weighted)
- Harvest VRP on index (lower)
- Pay VRP on stocks (higher) but capture correlation

**Example:**

- Short SPX variance, strike = 400
- Long 10 stocks average variance = 450
- Weight ratio 1:10

**If correlation falls:**

- Index variance realizes 350 (low)
- Stock variances realize 425 (average)

**P&L:**

- Index: $(400 - 350) \times \$1,000 = +\$50,000$
- Stocks: $(425 - 450) \times 10 \times \$100 = -\$25,000$
- **Net: +$\$25,000$**

**VRP component:**

- Both legs have VRP
- Net exposure depends on correlation bet

---

## Mathematical Framework


### 1. VRP Decomposition


**Components of VRP:**

$$
\text{VRP} = \underbrace{\text{Jensen's Inequality}}_{\text{Convexity}} + \underbrace{\text{Jump Risk Premium}}_{\text{Tail Risk}} + \underbrace{\text{Correlation Risk Premium}}_{\text{Diversification}}
$$

**Jensen's inequality:**

$$
\mathbb{E}[\sigma_t^2] \neq (\mathbb{E}[\sigma_t])^2
$$

Variance of variance contributes to VRP.

**Jump risk premium:**

- Markets have fat tails (excess kurtosis)
- Investors fear jumps
- Pay premium for jump protection
- Options expensive in wings

**Correlation risk premium:**

- Index options expensive (systemic risk)
- Single stocks less so
- Correlation risk priced

### 2. GARCH Model


**Modeling VRP with GARCH:**

Realized variance follows:

$$
\sigma_t^2 = \omega + \alpha \epsilon_{t-1}^2 + \beta \sigma_{t-1}^2
$$

Physical expectation:

$$
\mathbb{E}^P[\sigma_{t+1}^2 | \mathcal{F}_t] = \omega + \alpha \epsilon_t^2 + \beta \sigma_t^2
$$

Risk-neutral (with risk premium):

$$
\mathbb{E}^Q[\sigma_{t+1}^2 | \mathcal{F}_t] = \mathbb{E}^P[\sigma_{t+1}^2] + \lambda \sigma_t^2
$$

Where $\lambda$ is the variance risk premium parameter.

**Empirical estimate:**

- $\lambda \approx 0.2$ to $0.4$ for SPX
- Time-varying
- Higher in crises

### 3. Sharpe Ratio of VRP


**Risk-return profile:**

VRP harvesting strategies have:

$$
\text{Sharpe} = \frac{\mathbb{E}[\text{VRP}]}{\text{Std}[\text{VRP}]}
$$

**Typical values:**

- **Mean VRP:** 100-150 variance points
- **Std VRP:** 300-500 variance points
- **Sharpe:** 0.2-0.5 (before tail events)
- **Including tail events:** Often negative!

**Why?**

- VRP positive 80-90% of time (small gains)
- VRP hugely negative 10-20% of time (large losses)
- Negative skewness kills risk-adjusted returns

**Skewness:**

$$
\text{Skew}[\text{VRP}] \approx -2 \text{ to } -4
$$

**Highly negatively skewed = tail risk**

### 4. Time-Varying VRP


**VRP as function of VIX:**

$$
\text{VRP}_t = \alpha + \beta \times \frac{1}{\text{VIX}_t} + \epsilon_t
$$

**Empirical finding:**

- $\beta > 0$ (inverse relationship)
- Low VIX → High VRP
- High VIX → Low/negative VRP

**Trading rule:**

$$
\text{Position Size}_t = \max\left(0, \, \gamma \times \left(\frac{1}{\text{VIX}_t} - \text{threshold}\right)\right)
$$

Where:
- $\gamma$ = Scaling factor
- threshold = VIX level to start reducing (e.g., $1/30 \approx 0.033$)

### 5. VRP Persistence


**Autocorrelation:**

VRP exhibits serial correlation:

$$
\text{VRP}_{t+1} = \rho \times \text{VRP}_t + \epsilon_{t+1}
$$

**Empirical:**

- $\rho \approx 0.3$ to $0.5$ (monthly)
- Mean-reverting over quarters
- Regime-dependent (crises vs. normal)

**Implication:**

- Current VRP predicts next period VRP (weakly)
- High VRP periods cluster
- Can time exposure somewhat

### 6. Cross-Asset VRP


**VRP correlation:**

VRP across assets:

$$
\text{Corr}(\text{VRP}_{\text{SPX}}, \text{VRP}_{\text{Stock}}) \approx 0.6\text{-}0.8
$$

**Diversification:**

- VRP harvesting across multiple assets
- Reduces (but doesn't eliminate) tail risk
- Still correlated in crashes

**Optimal portfolio:**

- Mix equity, FX, commodity VRP
- Weight by Sharpe and correlation
- Rebalance monthly

### 7. VRP and Momentum


**Interaction with factors:**

VRP strategies correlate with:

$$
\text{Return}_{\text{VRP}} = \alpha + \beta_1 \times \text{Market} + \beta_2 \times \text{Momentum} + \beta_3 \times \text{Carry} + \epsilon
$$

**Findings:**

- $\beta_1 < 0$ (negative market beta in crashes)
- $\beta_2 < 0$ (negative momentum exposure)
- $\beta_3 > 0$ (positive carry exposure)

**Interpretation:**

- VRP is a carry trade
- Loses during risk-off
- Complements long equities poorly

---

## Common Mistakes


**Pitfalls to avoid:**

### 1. Ignoring Tail Risk


**Mistake:** Treat VRP as "free money"

**Why it fails:** Tail events destroy capital

**Example:**

- Short variance for 5 years
- Collect $\$100,000/year average
- Total: $\$500,000$

**Then Feb 2018 VIX spike:**

- Single day loss: $\$2,000,000$
- **Net: -$\$1,500,000$ (5 years wiped out + more)**

**Fix:**

- Size positions for tail events
- Use stop-losses
- Buy tail hedges (OTM puts)
- Never risk more than can afford to lose

### 2. Oversizing Positions


**Mistake:** Allocate 10-20% to short vol

**Why it fails:** One crash = blown account

**Kelly criterion:**

$$
f^* = \frac{\mu}{\sigma^2}
$$

For VRP with negative skew:

$$
f^* \approx 1\text{-}2\% \text{ of portfolio max}
$$

**Fix:**

- Max 1-2% allocation
- Lower if using leverage
- Dynamic scaling (reduce in high VIX)

### 3. No Hedges


**Mistake:** Naked short variance

**Why it fails:** Unlimited downside

**Example:**

- Short variance at 400
- Black Monday: variance hits 10,000
- **Loss:** $N_{\text{var}} \times 9,600$

**Fix:**

- Buy 30-40% OTM puts
- Costs 0.5-1% annually
- Caps maximum loss
- Essential risk management

### 4. Ignoring VIX Level


**Mistake:** Constant position regardless of VIX

**Why it fails:** VRP predictably varies with VIX

**Evidence:**

- VIX < 15: VRP ≈ 150 variance points
- VIX > 30: VRP ≈ -100 variance points (negative!)

**Fix:**

$$
\text{Position} = \max\left(0, \, c \times (30 - \text{VIX})\right)
$$

- Zero position when VIX > 30
- Scale up when VIX < 15
- Linear interpolation between

### 5. Forgetting Carry Costs


**Mistake:** Ignore financing and margin

**Why it fails:** Erodes returns

**Costs for short variance:**

- Margin requirement: 20-30% of notional
- Opportunity cost: ~5% annually on margin
- **Total drag: 1-1.5% annually**

**Fix:**

- Account for financing in expected return
- Use capital-efficient instruments
- Consider variance swaps (no upfront margin)

### 6. Mismatched Horizons


**Mistake:** Mix 1-month options with 3-month VRP

**Why it fails:** Different risk characteristics

**Example:**

- Measure VRP using 1M options
- But trade 3M variance swaps
- Mismatch in duration and risk

**Fix:**

- Match option maturity to trading horizon
- If trading monthly, use 30-day options
- If quarterly, use 90-day options

### 7. Neglecting Transaction Costs


**Mistake:** Ignore bid-ask spreads

**Why it fails:** Frequent rebalancing = high costs

**Example:**

- Variance swap bid-ask: 5-10 variance points
- Roll monthly: 12 times/year
- **Cost:** $10 \times 12 = 120$ variance points
- **Eats most of VRP!**

**Fix:**

- Trade less frequently (quarterly)
- Negotiate better spreads (larger size)
- Use liquid underlyings (SPX not small caps)

### 8. Overconfidence in Models


**Mistake:** Trust GARCH forecasts blindly

**Why it fails:** Models fail in crises

**Example:**

- GARCH predicts realized vol = 15%
- Implied vol = 18%
- Model says VRP = 100 points

**Reality:**

- Crisis hits, realized vol = 35%
- **Actual VRP: -600 points (lost money)**

**Fix:**

- Use models as guide, not gospel
- Stress test for extreme scenarios
- Keep positions small enough to survive model failure

---

## Risk Management Rules


### 1. Position Sizing


**Maximum allocation:**

$$
\text{Max Position} = \min\left(2\%, \, \frac{\text{Portfolio}}{\text{10} \times \sigma_{\text{var}}}\right)
$$

Where $\sigma_{\text{var}}$ is standard deviation of VRP.

**Example:**

- $\$10M$ portfolio
- VRP std dev = 300 variance points
- Max variance notional: $\$10M / (10 \times 300) = \$3,333$

**Rule of thumb:**

- Never exceed 2% of portfolio in vega terms
- 1% safer for retail
- 0.5% if using leverage

### 2. Stop-Loss Rules


**Hard stops:**

- **MTM loss > 50% → Exit immediately**
- VIX > 35 → Reduce to zero
- Realized variance > 2× strike → Cut position

**Example:**

- Short variance at 400
- If realized variance hits 800 → Exit
- Don't wait for further deterioration

### 3. Dynamic Scaling


**VIX-based adjustment:**

$$
\text{Exposure}(t) = \text{Base} \times \max\left(0, \, \frac{25 - \text{VIX}_t}{10}\right)
$$

**Translation:**

- VIX = 15 → 100% of base exposure
- VIX = 25 → 0% exposure
- VIX = 35 → 0% exposure (stay out)

**Linear scaling between 15-25**

### 4. Tail Hedging


**Required hedges:**

- **Put options:** Buy 30-40% OTM puts
- **Cost:** 0.5-1% of notional annually
- **Benefit:** Caps losses in crashes

**Example:**

- Short $\$5,000$ variance notional
- Buy SPX 30% OTM puts
- Cost: $\$25,000/year
- Max loss capped at $\$500,000 (vs. unlimited)

### 5. Diversification


**Spread across:**

- **Assets:** SPX, NDX, single stocks, FX
- **Maturities:** 1M, 3M, 6M
- **Strategies:** Variance swaps, straddles, spreads

**Correlation in crashes:**

- All VRP strategies correlate near 1.0 in crashes
- Diversification helps in normal times only
- Still useful to reduce non-tail volatility

### 6. Monitoring


**Daily checklist:**

- VIX level and percentile
- Realized variance vs. strike (MTM)
- Forward variance (implied vol changes)
- Skew and term structure shifts
- Macro risk events (earnings, Fed, geopolitics)

**Weekly review:**

- P&L attribution (theta vs. vega vs. gamma)
- Position size vs. risk limits
- Hedge effectiveness
- Rebalancing needs

---

## Real-World Examples


### 1. The Quiet Period (2012-2017)


**Setup:**

- VIX averaging 12-15
- Persistent contango in VIX futures
- High VRP environment

**Strategy:**

- Systematic short 3M variance
- $\$2,000$ variance notional
- Roll quarterly

**Outcome:**

- Average quarterly VRP: 120 variance points
- Quarterly profit: $\$240,000$
- Annualized: ~$\$960,000$
- **5-year total: ~$\$4.8M$**

**Lesson:** VRP harvesting works in low-vol regimes

### 2. Brexit Vote (2016)


**Setup:**

- Pre-Brexit: VIX at 15
- Short variance, strike = 225 (15% vol)
- $\$3,000$ notional

**Outcome:**

- Brexit passed, volatility spiked
- Realized variance = 625 (25% vol)
- **Loss:** $\$3,000 \times (225 - 625) = -\$1,200,000$

**But:**

- Had bought 30% OTM puts (tail hedge)
- Put payoff: +$\$800,000$
- **Net loss: -$\$400,000$ (contained)**

**Lesson:** Tail hedges essential for event risk

### 3. Volmageddon (Feb 2018)


**Setup:**

- Jan 2018: VIX at 9 (extreme low)
- XIV (short VIX ETP) at all-time high
- Investors piled into short vol

**Outcome:**

- Feb 5, 2018: VIX spiked from 9 to 50+
- XIV lost 95% in one day (terminated)
- SVXY lost 90%
- Short variance positions: -500 to -1,000% losses

**Lesson:**

- Crowded trades explode
- Leverage = death in tail events
- No position size too small for short vol

### 4. COVID Crash (March 2020)


**Setup:**

- Feb 2020: VIX at 15
- Short variance, strike = 225
- $\$1,000$ notional

**Outcome:**

- March: VIX hit 80+
- Realized variance = 4,900 (70% vol)
- **Loss:** $\$1,000 \times (225 - 4,900) = -\$4,675,000$

**Actual trader:**

- Had 1% position size cap
- Used stop-loss at VIX 30
- Exited early at $\$500,000$ loss
- **Saved from catastrophic loss**

**Lesson:** Risk management determines survival

---

## Practical Steps


### 1. Initial Setup


**Before trading VRP:**

1. **Backtest thoroughly:**
   - 20+ years of data
   - Include 2008, 2018, 2020
   - Understand worst-case scenarios

2. **Choose instruments:**
   - Variance swaps (most direct)
   - Short straddles (need delta hedging)
   - Put spreads (defined risk)

3. **Set risk limits:**
   - Max 1-2% portfolio allocation
   - Stop-loss rules
   - VIX-based scaling

### 2. Entry Conditions


**Start small when:**

- VIX < 20 (preferably < 15)
- VRP > 100 variance points (historical average)
- No major events in next month
- Skew reasonable (not inverted)
- Term structure in contango

**Avoid when:**

- VIX > 25 (VRP low/negative)
- Major events imminent (elections, Fed, earnings)
- Backwardation (fear in market)
- Recent crash (aftershocks common)

### 3. Position Sizing


**Calculate notional:**

$$
N_{\text{var}} = \frac{\text{Portfolio} \times 0.01}{\text{Max Variance Move}}
$$

**Example:**

- $\$5M$ portfolio
- Max variance move: 1,500 points (conservative)
- **Notional:** $\$5M \times 0.01 / 1,500 = \$33$ per variance point

**Very small to survive crashes!**

### 4. Hedging Setup


**Required hedges:**

- Buy OTM puts (3-4 standard deviations)
- Cost: 0.5-1% of portfolio annually
- Roll quarterly

**Example:**

- Short variance notional: $\$100$ per point
- Buy SPX 30% OTM puts, 3-month maturity
- Cost: ~$\$2,000$ per quarter

### 5. Monitoring & Rebalancing


**Daily:**

- Check VIX (reduce if > 25)
- Monitor MTM P&L
- Scan for event risks

**Monthly:**

- Roll variance swaps
- Rebalance position size
- Review hedge performance

**Quarterly:**

- Full performance attribution
- Stress test portfolio
- Adjust strategy if needed

### 6. Exit Discipline


**Exit immediately if:**

- MTM loss > 50%
- VIX > 35
- Major crisis unfolding
- Stop-loss triggered

**Take profits when:**

- VRP harvested (variance settles below strike)
- VIX spiking (future VRP will be low)
- Position size grown too large (from profits)

---

## Final Wisdom


> "The variance risk premium is real, persistent, and economically significant - but it's not free money. It's compensation for selling insurance against market crashes, and occasionally those crashes happen. VRP harvesting can be highly profitable for those with rigorous risk management, small position sizes, and disciplined hedging. But it has destroyed countless traders who got greedy, overleveraged, or complacent. Treat short volatility with the respect it deserves: assume the worst will happen, size accordingly, and hedge the tail. If you can't afford to lose it all in a single crash, your position is too large."

**Key to success:**

- Position size for survival (1-2% max)
- Dynamic scaling based on VIX
- Mandatory tail hedges (OTM puts)
- Stop-losses (no exceptions)
- Diversify across assets and maturities
- Respect the fat tails (they will happen)
- Remember: VRP is compensation for bearing risk, not alpha
