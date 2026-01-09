# Variance Swaps

**Variance swaps** are forward contracts on realized variance where you exchange a fixed strike (agreed upfront) for the realized variance of an underlying asset over a specified period, providing pure volatility exposure without directional risk.

---

## The Core Insight

**The fundamental idea:**

- Stock returns have variance (volatility squared)
- You want pure exposure to volatility, not direction
- Traditional options have delta and gamma contamination
- Variance swaps give clean volatility-only exposure
- Pay/receive difference between realized and strike variance
- No delta hedging required during life of swap

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/variance_swap_payoff.png?raw=true" alt="variance_swap_payoff" width="700">
</p>
**Figure 1:** Variance swap payoff diagram showing linear exposure to realized variance minus strike variance, with notional measured in variance units (annualized percentage squared).

**You're essentially betting: "Realized volatility will differ significantly from the strike volatility I'm locking in."**

---

## What Are Variance Swaps?

### 1. Pure Vol Exposure

**No directional contamination:**

**Definition:** A forward contract where at maturity you receive:

$$
\text{Payoff} = N_{\text{var}} \times (\sigma_{\text{realized}}^2 - K_{\text{var}})
$$

Where:
- $N_{\text{var}}$ = Variance notional (in currency per variance point)
- $\sigma_{\text{realized}}^2$ = Realized variance over the period (annualized)
- $K_{\text{var}}$ = Strike variance (agreed at inception)

**Key properties:**

- No premium paid upfront (mark-to-market swap)
- Payoff linear in variance (not volatility)
- No delta exposure to underlying
- No need for continuous hedging
- Settlement based on actual realized variance

### 2. Variance vs Volatility

**Critical distinction:**

**Variance** = $\sigma^2$ (volatility squared)

- Unit: percent-squared (e.g., 400 = 20% vol squared)
- Linear exposure: Payoff proportional to variance points
- More intuitive for hedging
- Easier to replicate with options

**Volatility** = $\sigma$ (square root of variance)

- Unit: percent (e.g., 20%)
- Non-linear exposure: Convex payoff structure
- What traders actually think about
- Requires volatility swaps (different instrument)

**Example:**

- Strike variance: $K_{\text{var}} = 400$ (20% vol)
- Realized variance: $\sigma_{\text{realized}}^2 = 625$ (25% vol)
- Variance notional: $N_{\text{var}} = \$1,000$ per variance point

**Payoff:**

$$
\text{Payoff} = \$1,000 \times (625 - 400) = \$225,000
$$

**You're long variance when you receive realized and pay strike.**

### 3. Realized Variance Calc

**How realized variance is computed:**

Given discrete observations of log returns:

$$
\sigma_{\text{realized}}^2 = \frac{252}{n} \sum_{i=1}^{n} r_i^2
$$

Where:
- $r_i = \ln(S_i/S_{i-1})$ = Log return on day $i$
- $n$ = Number of observations
- $252$ = Annualization factor (trading days)

**Key measurement details:**

- Typically use daily closing prices
- Some contracts use intraday sampling (every 30 min)
- More frequent sampling → lower estimation error
- Log returns assumed (not arithmetic returns)
- No drift adjustment in calculation
- Excludes weekends and holidays

**Example calculation:**

- 3-month swap, 63 trading days
- Daily log returns: $r_1, r_2, \ldots, r_{63}$
- Sum of squared returns: $\sum r_i^2 = 0.0952$

**Realized variance:**

$$
\sigma_{\text{realized}}^2 = \frac{252}{63} \times 0.0952 = 380
$$

**Realized volatility:** $\sqrt{380} = 19.5\%$

### 4. Strike Setting

**How strike variance is set:**

At inception, strike is set so that swap has zero value:

$$
K_{\text{var}} = \mathbb{E}^Q[\sigma_{\text{realized}}^2]
$$

**In practice:**

- Strike derived from option prices (variance replication)
- Uses a strip of OTM calls and puts
- Approximately equals ATM implied variance
- Includes variance risk premium

**Typical relationship:**

$$
K_{\text{var}} \approx \sigma_{\text{implied}}^2 + \text{Variance Risk Premium}
$$

**Historical pattern:**

- Strike typically > realized variance (on average)
- Reflects investor willingness to pay for volatility insurance
- Variance risk premium ranges from 100-400 variance points
- Long variance historically loses money (like insurance)

### 5. Variance Notional

**Converting volatility views to variance notional:**

Traders think in volatility, but swaps are in variance:

**Vega notional (what you want):**

$$
N_{\text{vega}} = \text{Currency amount per 1% volatility change}
$$

**Variance notional (what you need):**

$$
N_{\text{var}} = \frac{N_{\text{vega}}}{2\sigma_{\text{strike}}}
$$

Where $\sigma_{\text{strike}} = \sqrt{K_{\text{var}}}$

**Example:**

- Want $\$100,000$ vega (per 1% vol)
- Strike variance: $K_{\text{var}} = 400$ (20% vol)

**Required variance notional:**

$$
N_{\text{var}} = \frac{\$100,000}{2 \times 20\%} = \$2,500 \text{ per variance point}
$$

**If realized vol = 25%:**

- Variance difference: $625 - 400 = 225$
- **Payoff:** $\$2,500 \times 225 = \$562,500$

### 6. Mark-to-Market

**Daily P&L before settlement:**

Variance swaps are marked daily based on forward variance:

$$
\text{MTM} = N_{\text{var}} \times \left(K_{\text{var}}^{\text{forward}} - K_{\text{var}}\right) \times e^{-r(T-t)}
$$

Where:
- $K_{\text{var}}^{\text{forward}}$ = Current forward variance strike
- Derived from option prices at time $t$
- Discounted to present value

**P&L sources:**

1. **Realized variance accrual:**
   - As trading days pass, realized variance accrues
   - Locked-in contribution to final payoff

2. **Forward variance changes:**
   - If implied vol rises → long position gains
   - If implied vol falls → long position loses
   - Reflects change in expected future variance

**Example:**

- Long variance swap, strike = 400
- After 1 month, forward variance = 450
- Variance notional = $\$1,000$
- Time to maturity = 2 months, $r = 5\%$

**MTM gain:**

$$
\text{MTM} = \$1,000 \times (450 - 400) \times e^{-0.05 \times 2/12} = \$49,585
$$

### 7. Replication Portfolio

**How dealers hedge variance swaps:**

A variance swap can be replicated by a portfolio of options:

$$
\text{Variance Swap} \approx \frac{2e^{rT}}{T} \left[\int_0^{S_0} \frac{P(K)}{K^2}dK + \int_{S_0}^{\infty} \frac{C(K)}{K^2}dK\right]
$$

**Practical implementation:**

- Buy strip of OTM puts below current price
- Buy strip of OTM calls above current price
- Weight each option by $1/K^2$ (strike squared)
- Hold to maturity without rebalancing
- More strikes → better replication

**Why this works:**

- Variance is sum of all convexity
- $1/K^2$ weighting captures gamma at each strike
- Static hedge (no rebalancing needed)
- Price equals expected variance under risk-neutral measure

**Dealer perspective:**

- Sell variance swap to client
- Buy replicating portfolio
- Lock in profit = variance risk premium
- No delta risk, pure vol arbitrage

---

## Why Trade Variance?

**Use cases for variance exposure:**

### 1. Pure Vol Speculation

**Directional volatility views:**

**Long variance when:**

- Expect volatility to rise (crisis, uncertainty)
- Current implied vol seems too low
- Political/macro events approaching
- Market complacency at extremes

**Example:**

- VIX at 12, historically low
- Geopolitical tensions rising
- Buy 3-month variance swap, strike = 144 (12% vol)

**If realized vol = 20%:**

- Variance payoff: $400 - 144 = 256$ variance points
- With $\$1,000$ notional: **Profit = $\$256,000**

**Short variance when:**

- Expect volatility to decline
- Post-crisis normalization
- Implied vol elevated after event
- Mean reversion trade

**Risk:** Losses can be very large if volatility explodes

### 2. Vol Arbitrage

**Exploit relative mispricings:**

**Variance swap vs. straddle:**

- If variance swap cheap vs. straddle, buy variance
- If variance swap expensive vs. straddle, sell variance
- More efficient than delta-hedged straddle
- No continuous rehedging costs

**Cross-asset arbitrage:**

- If SPX variance cheap vs. sector variances
- Long SPX variance, short sector variances
- Bet on correlation structure

**Term structure arbitrage:**

- Short-term variance vs. long-term variance
- Bet on mean reversion of volatility term structure
- Example: Short 1-month, long 6-month variance

### 3. VRP Harvesting

**Systematic short volatility:**

Historical pattern: Realized vol < Implied vol

- Average variance risk premium: ~3-5% vol annually
- Short variance swaps systematically profit
- Collect insurance premium from vol buyers

**Strategy:**

- Continuously short 3-month variance
- Roll monthly
- Size position conservatively (tail risk!)
- Expect long periods of steady gains
- Interrupted by catastrophic losses

**Risk management critical:**

- Position size small (1-2% portfolio)
- Use stop-losses
- Hedge tail risk with OTM puts
- Diversify across assets and maturities

### 4. Portfolio Hedging

**Pure volatility insurance:**

Traditional put buying has disadvantages:

- Costs premium upfront
- Decays with theta
- Has delta exposure
- Needs constant rolling

**Variance swaps instead:**

- No upfront premium (mark-to-market)
- Linear payoff in variance (unlimited upside)
- No delta contamination
- Single trade for entire period

**Example hedge:**

- $\$10M$ equity portfolio
- Buy 3-month variance, notional = $\$50,000$ vega
- If market crashes and vol spikes 10%:

**Hedge profit:** $\$500,000$ (offsets portfolio drawdown)

**Advantages:**

- Cheaper than rolling puts
- Payoff during volatility spike (when you need it)
- No need to delta hedge
- Set and forget

### 5. Dispersion Trading

**Trade correlation structure:**

**Setup:**

- Index variance vs. single-stock variances
- Index variance < Sum of single-stock variances (correlation < 1)

**Trade:**

- Short index variance swap
- Long variance swaps on individual stocks (weighted)
- Profit if correlation falls (dispersion increases)

**Example:**

- Short SPX variance
- Long variance on AAPL, MSFT, GOOGL, AMZN, NVDA
- If stocks move independently → dispersion widens → profit

**When it works:**

- Market transitions from risk-on to stock-specific stories
- Correlation breakdown
- Sector rotation periods

### 6. Vol Curve Trading

**Exploit term structure:**

**Contango trade:**

- Short long-term variance (expensive)
- Long short-term variance (cheap)
- Profit from term structure normalization

**Backwardation trade:**

- Long long-term variance (cheap)
- Short short-term variance (expensive)
- Bet on volatility persistence

**Example:**

- 1-month variance strike = 625 (25% vol)
- 6-month variance strike = 400 (20% vol)
- Backwardation (fear in near-term)

**Trade:** Long 1-month, short 6-month (calendar spread)

**Profit if:** Near-term vol stays elevated, long-term normalizes

### 7. Event-Driven Trades

**Before binary events:**

**Scenario:** Earnings, FDA decision, election

**Long variance if:**

- Market underpricing event volatility
- Historical precedent for large moves
- Consensus views too narrow

**Advantage over straddles:**

- Pure vol bet (no gamma P&L)
- Captures realized vol over entire period
- Not just one-day move

**Example:**

- Biotech with FDA decision in 2 months
- Buy 3-month variance swap
- Captures both pre-event drift and post-event volatility

---

## Mathematical Framework

### 1. Payoff Structure

**At maturity $T$:**

$$
\text{Payoff}_{\text{long}} = N_{\text{var}} \times \left(\sigma_{\text{realized}}^2 - K_{\text{var}}\right)
$$

**For short variance:**

$$
\text{Payoff}_{\text{short}} = N_{\text{var}} \times \left(K_{\text{var}} - \sigma_{\text{realized}}^2\right)
$$

**Key properties:**

- Linear in variance (not volatility!)
- Symmetric payoff structure
- No premium paid upfront
- Settlement in cash at maturity

### 2. Fair Value Pricing

**Variance swap fair value:**

Under risk-neutral measure:

$$
K_{\text{var}} = \mathbb{E}^Q\left[\frac{1}{T}\int_0^T \sigma_t^2 dt\right]
$$

**Using option replication:**

$$
K_{\text{var}} = \frac{2e^{rT}}{T}\left[\int_0^{S_0} \frac{P(K)}{K^2}dK + \int_{S_0}^{\infty} \frac{C(K)}{K^2}dK\right] - \frac{1}{T}\left(\frac{S_T}{S_0} - 1 - \ln\frac{S_T}{S_0}\right)^2
$$

**Last term is negligible for typical parameters.**

**Practical approximation:**

$$
K_{\text{var}} \approx \sigma_{\text{ATM}}^2 + \text{Skew Adjustment}
$$

Where skew adjustment depends on option smile structure.

### 3. Convexity Adjustment

**Variance vs. volatility notional:**

Since payoff is linear in variance but traders think in volatility:

$$
\Delta \text{Variance} = (\sigma_2^2 - \sigma_1^2) = (\sigma_2 - \sigma_1)(\sigma_2 + \sigma_1) \approx 2\sigma(\sigma_2 - \sigma_1)
$$

For small volatility changes $\Delta\sigma$:

$$
\Delta \text{Variance} \approx 2\sigma \Delta\sigma
$$

**This gives the conversion:**

$$
N_{\text{var}} = \frac{N_{\text{vega}}}{2\sigma}
$$

**Higher strike volatility → lower variance notional needed for same vega.**

### 4. Greeks

**Variance vega (sensitivity to vol):**

$$
\text{Vega} = N_{\text{var}} \times 2\sigma
$$

**Variance gamma (convexity):**

$$
\text{Gamma} = N_{\text{var}} \times 2
$$

**Delta:**

$$
\text{Delta} = 0 \quad \text{(by construction)}
$$

**Time decay (theta):**

As time passes, variance accrues:

$$
\theta = N_{\text{var}} \times \frac{252}{n_{\text{remaining}}} \times r_{\text{today}}^2
$$

Where $r_{\text{today}}$ is today's log return.

### 5. Realized Variance Process

**Under physical measure:**

Realized variance follows approximately:

$$
\sigma_{\text{realized}}^2 = \frac{252}{T}\sum_{i=1}^n r_i^2
$$

**Properties:**

- Increases with time (more observations)
- Converges to true variance as $n \to \infty$
- Non-negative by construction
- Higher frequency sampling → faster convergence

**Variance of realized variance:**

$$
\text{Var}(\sigma_{\text{realized}}^2) \approx \frac{2\sigma^4}{n}
$$

**Estimation error decreases with more observations.**

### 6. Variance Risk Premium

**Definition:**

$$
\text{VRP} = K_{\text{var}} - \mathbb{E}^P[\sigma_{\text{realized}}^2]
$$

Where:
- $\mathbb{E}^Q$ = Risk-neutral expectation (option-implied)
- $\mathbb{E}^P$ = Physical expectation (realized)

**Empirical facts:**

- VRP typically positive (3-5% vol points)
- Varies with market conditions
- Higher in bear markets
- Compensation for volatility risk

**Why VRP exists:**

- Investors pay premium for volatility insurance
- Short vol exposed to tail risk (crashes)
- Market makers demand compensation
- Supply/demand imbalance

### 7. Replication Error

**Discrete strike replication:**

In practice, use finite number of strikes:

$$
K_{\text{var}}^{\text{approx}} = \sum_{i=1}^n w_i \times \text{Option}_i
$$

Where $w_i = \frac{2e^{rT}}{TK_i^2}\Delta K_i$

**Sources of error:**

- Finite number of strikes (missing wings)
- Bid-ask spread on each option
- Discrete strike spacing
- Illiquid far OTM options

**Typical error:** 1-3 variance points

**Improvement strategies:**

- Use more strikes (every $5, not $10)
- Extrapolate tail (fit wings)
- Weight liquid strikes more
- Adjust for bid-ask

---

## Common Mistakes

**Pitfalls to avoid:**

### 1. Confusing Variance/Vol

**Mistake:** Think payoff linear in volatility

**Why it fails:** Payoff is in variance (squared)

- If vol goes 20% → 25%, variance goes 400 → 625 (+225)
- If vol goes 25% → 30%, variance goes 625 → 900 (+275)
- **Same 5% vol increase, different variance payoff!**

**Fix:** Always convert to variance for payoff calculations

$$
\text{Payoff} = N_{\text{var}} \times (\sigma_{\text{real}}^2 - K_{\text{var}})
$$

### 2. Ignoring Var Notional

**Mistake:** Use vega notional directly in calculations

**Why it fails:** Variance notional ≠ vega notional

**Example:**

- Vega notional: $\$100,000$
- Strike vol: 20%
- Forget to convert

**Wrong payoff (if realized vol = 25%):**

$$
\$100,000 \times (25\% - 20\%) = \$5,000 \quad \text{WRONG!}
$$

**Correct approach:**

$$
N_{\text{var}} = \frac{\$100,000}{2 \times 20\%} = \$2,500 \text{ per var point}
$$

$$
\text{Payoff} = \$2,500 \times (625 - 400) = \$562,500
$$

**Fix:** Always compute variance notional first

### 3. Overlooking Tail Risk

**Mistake:** Sell variance without position limits

**Why it fails:** Unlimited downside if volatility explodes

**Example:**

- Short variance at strike = 400
- Flash crash: realized vol = 60%
- Variance = 3,600

**Loss per $\$1,000$ notional:**

$$
\$1,000 \times (400 - 3,600) = -\$3,200,000
$$

**Fix:**

- Position size conservatively (max 1-2% portfolio)
- Use stop-losses
- Hedge with OTM puts
- Never sell more variance than you can afford to lose

### 4. Mispricing Jumps

**Mistake:** Assume continuous diffusion only

**Why it fails:** Jumps contribute disproportionately to variance

**Example:**

- Stock at $100, one jump to $80 (-20%)
- Single day return: $r = \ln(80/100) = -22.3\%$
- Contribution to variance: $(-0.223)^2 \times 252 = 12.5$ variance points!

**Fix:**

- Account for jump risk in pricing
- Long variance benefits from jumps
- Skew reflects jump probability
- Use variance swaps (not vol swaps) to capture jumps

### 5. Neglecting MTM

**Mistake:** Ignore interim P&L volatility

**Why it fails:** Large MTM swings before settlement

**Example:**

- Long 6-month variance, strike = 400
- After 1 month, implied vol spikes to 30%
- Forward variance = 900

**MTM gain (even though not realized yet):**

$$
\$1,000 \times (900 - 400) \times e^{-0.05 \times 5/12} = \$490,000
$$

**But if vol drops back, you lose this gain!**

**Fix:**

- Monitor forward variance daily
- Understand MTM driven by implied vol changes
- Set risk limits on MTM, not just final payoff
- Consider taking profits on large MTM gains

### 6. Wrong Notional Scaling

**Mistake:** Size position in dollars, not variance notional

**Why it fails:** Leverage varies with volatility level

**Example:**

- $\$1M$ position at 20% vol strike
- Variance notional = $\$1M / (2 \times 20\%) = \$2,500,000$ per point
- If vol moves to 40%, your vega exposure doubles!

**Fix:**

- Set variance notional based on maximum acceptable loss
- Back out position size:

$$
\text{Max Loss} = N_{\text{var}} \times \text{Max Variance Move}
$$

- Don't scale by current volatility level alone

### 7. Ignoring VRP

**Mistake:** Systematically long variance without edge

**Why it fails:** Variance buyers historically lose money

**Example:**

- Over 10 years, average VRP = 3-4% vol
- Strike = 400 (20% vol), realized = 361 (19% vol) on average
- **Lose 39 variance points per trade**

**With $\$1,000$ notional:**

- Average loss: $\$1,000 \times (-39) = -\$39,000$ per trade

**Fix:**

- Only buy variance when you have edge
- Compare current strike to historical realized
- If strike > historical average + VRP, avoid
- Or size very small, treat as cheap insurance

### 8. Misunderstanding Settlement

**Mistake:** Expect daily realized variance to match strike

**Why it fails:** Settlement is based on cumulative realized variance

**Example:**

- 3-month swap, strike = 400
- First month: realized variance = 900 (very high)
- Second month: realized variance = 100 (very low)
- Third month: realized variance = 400 (at strike)

**Average realized variance:**

$$
\frac{900 + 100 + 400}{3} = 467
$$

**Payoff:** $N_{\text{var}} \times (467 - 400) = 67 \times N_{\text{var}}$

**Long variance profits even though ended at strike!**

**Fix:**

- Understand cumulative nature of realized variance
- Early volatility matters for final payoff
- Can't just look at spot vol at maturity

---

## Risk Management Rules

### 1. Position Sizing

**Conservative guideline:**

$$
N_{\text{var}} = \frac{\text{Max Acceptable Loss}}{\text{Worst Case Variance Move}}
$$

**Example:**

- Max loss: $\$100,000$ (1% of portfolio)
- Worst case: Variance moves from 400 to 1,600 (vol: 20% → 40%)
- Variance move: 1,200 points

**Variance notional:**

$$
N_{\text{var}} = \frac{\$100,000}{1,200} = \$83 \text{ per variance point}
$$

**Rule of thumb:** Never exceed 2% of portfolio in variance notional (in vega terms)

### 2. Hedging Tail Risk

**For short variance positions:**

- Buy OTM puts (3-4 standard deviations)
- Costs 0.5-1% of notional
- Caps maximum loss
- Example: Short variance + long 30% OTM put

**For long variance positions:**

- Less critical (upside unlimited)
- Consider stop-loss if implied vol rises sharply
- Take profits at 100-200% gain

### 3. Monitoring

**Daily risk checks:**

- MTM P&L (from forward variance changes)
- Accrued realized variance so far
- Remaining days to settlement
- Implied volatility level
- Jump risk indicators (VIX, skew)

**Action triggers:**

- MTM loss > 50% → Review thesis
- Implied vol spike > 10% → Consider exit
- Realized variance tracking far from strike → Adjust expectations

### 4. Diversification

**Spread risk across:**

- Multiple underlyings (SPX, single stocks)
- Multiple maturities (1M, 3M, 6M)
- Long and short positions (dispersion)
- Combine with other vol strategies (straddles, VIX options)

**Never:**

- Concentrate more than 20% of vol exposure in single swap
- Sell variance without tail hedges
- Ignore correlation (index vs. single stock)

---

## Real-World Examples

### 1. VIX Spike (Feb 2018)

**Setup:**

- SPX at all-time highs
- VIX at 10 (historically low)
- 3-month variance strike = 100 (10% vol)
- Complacency extreme

**Trade:** Long variance swap, $\$500$ notional

**Outcome:**

- VIXplosion: VIX spiked to 50
- Realized variance over 3 months = 900 (30% vol)
- **Payoff:** $\$500 \times (900 - 100) = \$400,000$

**Lesson:** Cheap vol before crisis can pay off enormously

### 2. COVID Crash (Mar 2020)

**Setup:**

- February 2020: SPX at 3,400
- Bought 3-month variance, strike = 196 (14% vol)
- Variance notional = $\$1,000$

**Outcome:**

- March crash: SPX dropped to 2,200 (-35%)
- VIX hit 80+
- Realized variance = 2,500 (50% vol)
- **Payoff:** $\$1,000 \times (2,500 - 196) = \$2,304,000$

**Lesson:** Variance swaps are ultimate tail hedge

### 3. VRP Harvest Strategy

**Setup:**

- Systematic strategy: Short 3-month variance
- Roll monthly
- Position size: 1% portfolio

**Outcome (2015-2019):**

- 48 months of trades
- 44 months profitable (steady premium collection)
- 4 months large losses (vol spikes)
- Average monthly return: +0.5%
- Maximum drawdown: -15% (during 2015 flash crash)
- **Sharpe ratio: 0.8**

**Lesson:** Short vol harvesting works but requires strict risk management

### 4. Dispersion Trade (2021)

**Setup:**

- Post-COVID: High index correlation
- Anticipated rotation to stock-picking
- Trade: Short SPX variance, long single-stock variances
- Ratio: 1 SPX vs. 10 single stocks (weighted)

**Outcome:**

- Correlation fell from 0.7 to 0.4
- SPX variance fell 100 points
- Single-stock variances rose average 50 points each
- **Net profit:** $(10 \times 50) - 100 = 400$ variance points

**Lesson:** Dispersion trades profit from correlation changes

---

## Practical Steps

### 1. Pre-Trade Analysis

**Before entering, evaluate:**

1. **Market conditions:**
   - Current implied volatility level (VIX percentile)
   - Historical realized volatility
   - Variance risk premium (strike vs. historical)

2. **Directional view:**
   - Bullish or bearish on volatility?
   - Expected magnitude of move
   - Time horizon for view

3. **Fair value check:**
   - Compare strike to historical realized variance
   - Assess variance risk premium
   - Check option smile for jump risk

### 2. Contract Specification

**Key parameters to set:**

- **Maturity:** 1-month, 3-month, or 6-month?
- **Notional:** Calculate variance notional from vega exposure
- **Strike:** Accept quoted strike or negotiate?
- **Underlying:** Index (SPX) or single stock?

**Example:**

- Want $\$100,000$ vega exposure to SPX
- 3-month maturity
- Current strike = 400 (20% vol)

**Variance notional:**

$$
N_{\text{var}} = \frac{\$100,000}{2 \times 20\%} = \$2,500 \text{ per variance point}
$$

### 3. Execution

**Best practices:**

- Request quotes from multiple dealers
- Compare strikes (should be similar)
- Check bid-ask on replicating portfolio
- Negotiate notional based on liquidity
- Confirm settlement calculation methodology

**Typical bid-ask:**

- SPX: 5-10 variance points
- Single stocks: 10-20 variance points
- Illiquid names: 20-50 variance points

### 4. Monitoring

**Daily tracking:**

- Realized variance accrued so far
- Forward variance (from option prices)
- MTM P&L
- Implied volatility changes
- Days remaining to settlement

**Tools:**

- Bloomberg: VCURVE, HIVG
- Option pricing data
- Custom spreadsheets for accrual

### 5. Exit Strategies

**When to exit early:**

**For long variance:**

- MTM profit > 100% (take gains)
- Implied vol spiked (forward variance increased)
- Thesis invalidated (expected catalyst didn't materialize)
- Better opportunity elsewhere

**For short variance:**

- MTM loss > 50% (cut losses)
- Implied vol rising dangerously
- Jump risk increasing
- Approaching tail risk threshold

**For dispersion:**

- Correlation reached target
- One leg significantly underperforming
- Index variance diverged from single stocks

### 6. Settlement Prep

**Final week checklist:**

- Verify realized variance calculation
- Check if any adjustments needed (corporate actions)
- Confirm settlement amount with dealer
- Prepare cash for settlement (if short and lost)
- Document trade for tax purposes

---

## Final Wisdom

> "Variance swaps are the purest form of volatility trading - linear exposure to realized variance with no delta contamination. They're powerful tools for directional vol bets, dispersion trades, and tail hedging, but the leverage is extreme. A seemingly small move in volatility translates to massive variance changes. Master the variance-volatility relationship before trading, size positions conservatively, and never short variance without tail hedges. The variance risk premium tempts systematic shorting, but one volatility explosion can wipe out years of premiums."

**Key to success:**

- Understand variance ≠ volatility (squared relationship!)
- Calculate variance notional correctly
- Size positions for maximum acceptable loss
- Use variance swaps for views on volatility, not direction
- Monitor mark-to-market daily
- Never short variance without risk limits
- Combine with other vol instruments for robust strategies
