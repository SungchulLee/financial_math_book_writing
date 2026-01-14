# Volatility Targeting


**Volatility targeting** is a dynamic position sizing strategy that adjusts futures exposure inversely with realized volatility, maintaining constant risk levels across changing market regimes by increasing positions during calm periods and reducing them during turbulent times.

---

## The Core Insight


**The fundamental idea:**

- Market volatility varies dramatically over time (calm vs. crisis)
- Fixed position sizes lead to variable risk exposure
- Low volatility → Safe to hold larger positions
- High volatility → Must reduce positions to control risk
- Target constant dollar risk (not constant notional exposure)
- Rebalance positions as volatility changes
- Improves risk-adjusted returns (Sharpe ratio)

**The key equation:**

$$
\text{Position Size} = \frac{\text{Target Volatility}}{\text{Realized Volatility}}
$$

Where position size scales inversely with market volatility:

$$
N_t = \frac{\sigma_{\text{target}}}{\sigma_t} \times \text{Base Position}
$$

**You're essentially maintaining: "I want to risk exactly $X per day, regardless of whether VIX is 10 or 40."**

---

## What Is Volatility


**Before implementing vol targeting, understand the mechanics:**

### 1. Core Concept


**Definition:** A risk management framework that dynamically adjusts futures position sizes based on recent realized volatility, scaling up exposure when markets are calm and scaling down when markets are turbulent, keeping dollar risk constant.

**When you use volatility targeting:**

- You measure recent volatility (typically 20-60 day window)
- You calculate target position size = Target vol / Current vol
- You rebalance positions regularly (daily, weekly, monthly)
- You maintain constant risk budget
- Returns become smoother over time
- Sharpe ratio improves significantly

**Example - S&P 500 Futures:**

**Calm market (VIX = 12):**

- Recent 30-day volatility: 10% annualized
- Target volatility: 15% annualized
- Scaling factor: 15% / 10% = 1.5x
- **Hold 1.5x normal position (lever up)**

**Crisis market (VIX = 40):**

- Recent 30-day volatility: 45% annualized
- Target volatility: 15% annualized  
- Scaling factor: 15% / 45% = 0.33x
- **Hold 0.33x normal position (de-lever)**

**Result: Your portfolio volatility stays at 15% whether VIX is 12 or 40**

### 2. The Inverse


**Understanding the mathematics:**

$$
\text{Portfolio Volatility} = \text{Position Size} \times \text{Asset Volatility}
$$

**To keep left side constant as asset volatility changes:**

$$
\sigma_{\text{portfolio}} = N \times \sigma_{\text{asset}} = \text{constant}
$$

**Requires:**

$$
N = \frac{\sigma_{\text{target}}}{\sigma_{\text{asset}}}
$$

**Example over time:**

| Date | Market Vol | Target Vol | Position Size | Portfolio Vol |
|------|-----------|------------|---------------|---------------|
| Jan | 12% | 15% | 1.25x | 15% |
| Mar | 18% | 15% | 0.83x | 15% |
| May | 35% | 15% | 0.43x | 15% |
| Jul | 10% | 15% | 1.50x | 15% |

**Portfolio volatility stays constant at 15% despite market volatility varying 12%-35%**

### 3. Fixed Notional


**Traditional approach (fixed notional):**

- Always hold 10 ES contracts
- Calm market: Risk $5,000/day
- Crisis market: Risk $25,000/day
- **Risk exposure varies 5x!**

**Volatility targeting approach:**

- Target $10,000/day risk
- Calm market: Hold 20 ES contracts
- Crisis market: Hold 4 ES contracts
- **Risk exposure constant**

**The difference:**

| Market Regime | Fixed Notional | Vol Targeting |
|--------------|----------------|---------------|
| Calm (σ=10%) | 10 contracts, $5k risk | 20 contracts, $10k risk |
| Normal (σ=15%) | 10 contracts, $7.5k risk | 13 contracts, $10k risk |
| Crisis (σ=40%) | 10 contracts, $20k risk | 5 contracts, $10k risk |

**Vol targeting prevents over-exposure in volatile markets**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/volatility_targeting.png?raw=true" alt="volatility_targeting" width="700">
</p>
**Figure 1:** Volatility targeting showing the inverse relationship between market volatility and position size, with portfolio volatility remaining constant while position sizes adjust dynamically from high exposure in calm markets to low exposure in turbulent markets.

---

## Economic


**Beyond the basic mechanics, understanding the REAL economics:**

### 1. The Risk Budget


**The deep insight:**

Volatility targeting implements a **constant risk budget** rather than constant capital allocation. When you use vol targeting, you're essentially:

1. **Defining acceptable risk** (target volatility = your risk tolerance)
2. **Measuring current risk** (realized volatility = market danger level)
3. **Adjusting exposure** (position size = risk budget / current risk)
4. **Rebalancing systematically** (maintain constant risk profile)

**Formal decomposition:**

$$
\underbrace{\text{Risk Budget}}_{\text{Constant}} = \underbrace{\text{Position Size}}_{\text{Variable}} \times \underbrace{\text{Asset Volatility}}_{\text{Variable}}
$$

**To keep risk budget constant:**

$$
\Delta(\text{Position}) = -\Delta(\text{Volatility})
$$

**Why this matters:**

**Traditional investor:**

- Sets allocation: "10% of portfolio in equities"
- Risk varies wildly with market conditions
- 2008 crisis: 10% allocation = 40% volatility exposure
- Unintentional concentration in risky periods

**Vol targeting investor:**

- Sets risk: "My equity exposure should contribute 10% volatility"
- Allocation varies with market conditions
- 2008 crisis: Automatically reduces to 2.5% allocation
- **Intentional de-risking when needed most**

**The key difference: Control risk, not notional**

### 2. The Sharpe Ratio


**Why vol targeting improves risk-adjusted returns:**

**Sharpe ratio:**

$$
\text{SR} = \frac{\mathbb{E}[R] - R_f}{\sigma_R}
$$

**Without vol targeting:**

- Returns: Mix of low-vol and high-vol periods
- Volatility: Average of calm and crisis periods
- **Problem: Crisis periods dominate volatility, reduce SR**

**With vol targeting:**

- Returns: Weighted toward safer periods (larger positions when calm)
- Volatility: Constant by design
- **Benefit: Less dominated by crisis volatility**

**Empirical evidence (S&P 500, 1990-2024):**

| Strategy | Annual Return | Volatility | Sharpe Ratio |
|----------|--------------|------------|--------------|
| Buy & Hold | 9.8% | 15.2% | 0.48 |
| Vol Target 10% | 8.2% | 10.0% | 0.62 |
| Vol Target 15% | 11.5% | 15.0% | 0.60 |

**Vol targeting improves Sharpe by 20-30%**

**Why?**

- Reduces position during crashes (limits drawdowns)
- Increases position during recoveries (captures upside)
- **Asymmetric exposure: More upside, less downside**

### 3. The Volatility


**Markets exhibit volatility clustering:**

$$
\text{Volatility today} \rightarrow \text{Volatility tomorrow}
$$

**GARCH model:**

$$
\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2
$$

**What this means:**

- High volatility persists (clusters)
- Low volatility persists (calm periods extend)
- Volatility mean-reverts over time
- **Predictability allows proactive adjustment**

**Trading implication:**

**During vol spike:**

- Reduce position size immediately
- Volatility likely to stay elevated (clustering)
- Avoid being over-exposed during continuation
- **Defensive positioning**

**During vol calm:**

- Increase position size
- Calm tends to persist
- Safe to take more risk
- **Offensive positioning**

**Vol targeting exploits this clustering behavior**

### 4. The Leverage


**Volatility targeting as dynamic leverage:**

Think of it as **automatic leverage adjustment**:

$$
\text{Effective Leverage} = \frac{1}{\text{Realized Volatility}}
$$

**Example - 15% target volatility:**

| Market Vol | Implied Leverage | Position Size |
|-----------|-----------------|---------------|
| 5% (super calm) | 3.0x | 300% |
| 10% (calm) | 1.5x | 150% |
| 15% (normal) | 1.0x | 100% |
| 30% (crisis) | 0.5x | 50% |
| 60% (panic) | 0.25x | 25% |

**The beauty:**

- Leverage high when safe (calm markets)
- Leverage low when dangerous (volatile markets)
- **Opposite of typical investor behavior!**

**Typical investor:**

- Calm market: Complacent, no leverage
- Crisis: Panic, forced to sell (de-lever at worst time)
- **Exactly backwards**

**Vol targeting:**

- Calm market: Systematically lever up
- Crisis: Automatically de-lever
- **Countercyclical, disciplined**

### 5. The Mean


**Long-term property:**

$$
\sigma_t \rightarrow \bar{\sigma} \quad \text{(volatility mean-reverts)}
$$

**Historical S&P 500:**

- Long-run average: ~15% volatility
- Range: 8% (1995) to 80% (2008 crisis)
- **Always returns to ~15% eventually**

**Trading implication:**

**When volatility spikes (40%+):**

- Current vol > Long-run average
- Expected to decline (mean revert)
- Vol targeting: Low position now
- **As vol falls back to 15%, systematically increase position**
- Result: Buy low (during recovery)

**When volatility crashes (8%):**

- Current vol < Long-run average
- Expected to rise (mean revert)
- Vol targeting: High position now
- **As vol rises back to 15%, systematically reduce position**
- Result: Sell high (before correction)

**Vol targeting is implicitly contrarian:**

- Heavy positions in calm (cheap prices)
- Light positions in chaos (expensive fear premium)
- **Buy low, sell high mechanically**

### 6. The Crash


**Critical feature during market crashes:**

**2008 Financial Crisis timeline:**

| Month | S&P Level | Volatility | Vol Target Position | Fixed Position |
|-------|-----------|------------|-------------------|----------------|
| Jul 08 | 1,260 | 18% | 83% (reducing) | 100% (full) |
| Sep 08 | 1,165 | 32% | 47% (half) | 100% (full) |
| Oct 08 | 968 | 58% | 26% (quarter) | 100% (full) |
| Nov 08 | 896 | 52% | 29% | 100% (full) |

**Drawdown comparison:**

- Fixed position: -29% (full exposure to crash)
- Vol targeting: -12% (automatically de-risked)
- **Protection: 17% less drawdown**

**The mechanism:**

1. Volatility spikes before prices crash
2. Vol targeting reduces exposure preemptively
3. When crash happens, position already small
4. **Automatic circuit breaker**

**This is not market timing:**

- No prediction required
- Purely mechanical (volatility measurement)
- No discretion needed
- **Reactive, not predictive**

### 7. The Rebalancing


**Volatility targeting creates systematic rebalancing:**

**As markets fall (volatility rises):**

- Position size formula: Decrease
- Action: Sell futures (de-risk)
- **Selling into weakness**

**As markets recover (volatility falls):**

- Position size formula: Increase
- Action: Buy futures (re-risk)
- **Buying into strength**

**This creates implicit "buy low, sell high":**

$$
\mathbb{E}[\text{Rebalancing Return}] = \frac{1}{2}\sigma^2(1-\rho)
$$

Where $\rho$ = autocorrelation of returns

**For typical markets ($\sigma$ = 15%, $\rho$ = -0.05):**

$$
\text{Rebalancing premium} = 0.5 \times 0.15^2 \times 1.05 \approx 1.2\% \text{ per year}
$$

**Free lunch from systematic rebalancing**

---

## Key Terminology


**Realized Volatility:**

- Actual historical volatility of returns
- Calculated from past price movements
- Lookback window: 20-60 days typical
- Formula: $\sigma = \sqrt{\frac{252}{n}\sum_{i=1}^{n}r_i^2}$

**Target Volatility:**

- Desired portfolio volatility level
- Set based on risk tolerance
- Typical: 10% (conservative), 15% (moderate), 20% (aggressive)
- Remains constant over time

**Scaling Factor:**

- Ratio of target to realized volatility
- Formula: $f = \sigma_{\text{target}} / \sigma_{\text{realized}}$
- Determines position size adjustment
- Example: Target 15%, Realized 30% → Factor 0.5x

**Lookback Window:**

- Period used to calculate realized volatility
- Shorter window (20 days): More responsive, noisier
- Longer window (60 days): More stable, slower
- Trade-off: Responsiveness vs. stability

**Rebalancing Frequency:**

- How often positions are adjusted
- Daily: Most responsive, higher turnover
- Weekly: Balanced approach (common)
- Monthly: Lower turnover, less responsive
- Trade-off: Accuracy vs. transaction costs

**Risk Budget:**

- Dollar amount willing to lose per day/month
- Example: $10,000/day risk budget
- Used to calculate position sizes
- Scaled by account size

**Leverage Ratio:**

- Position size / Account equity
- Vol targeting creates dynamic leverage
- Calm markets: High leverage (e.g., 2x)
- Volatile markets: Low leverage (e.g., 0.3x)

**Vol of Vol (Volatility of Volatility):**

- How much volatility itself fluctuates
- High vol of vol: More frequent rebalancing needed
- Measured by standard deviation of volatility
- Affects optimal lookback window

**Drawdown:**

- Peak-to-trough decline
- Vol targeting reduces max drawdown
- Typical improvement: 30-50% lower drawdown
- Key benefit of the strategy

---

## Mathematical


### 1. Volatility


**Standard realized volatility calculation:**

$$
\sigma_t = \sqrt{\frac{252}{n}\sum_{i=1}^{n}r_{t-i}^2}
$$

Where:
- $r_{t-i}$ = Daily return (log returns preferred)
- $n$ = Lookback window (20, 30, 60 days)
- $252$ = Trading days per year (annualization)

**Example - 20-day realized vol:**

**Daily returns (last 20 days):**

| Day | Price | Return | Return² |
|-----|-------|--------|---------|
| 1 | 4,500 | - | - |
| 2 | 4,520 | +0.44% | 0.0002 |
| 3 | 4,490 | -0.66% | 0.0004 |
| ... | ... | ... | ... |
| 20 | 4,580 | +0.22% | 0.0000 |

**Sum of squared returns: 0.0082**

$$
\sigma = \sqrt{\frac{252}{20} \times 0.0082} = \sqrt{0.1033} = 32.1\%
$$

**Current realized volatility: 32.1% annualized**

### 2. Position Size


**Basic formula:**

$$
N_t = \frac{\sigma_{\text{target}}}{\sigma_t} \times N_{\text{base}}
$$

Where:
- $N_t$ = Number of contracts at time $t$
- $\sigma_{\text{target}}$ = Target volatility (e.g., 15%)
- $\sigma_t$ = Current realized volatility
- $N_{\text{base}}$ = Base position (often 1 contract)

**Example:**

- Target volatility: 15%
- Current volatility: 32.1%
- Base position: 1 ES contract

$$
N = \frac{15\%}{32.1\%} \times 1 = 0.47 \text{ contracts}
$$

**Round to: 0 or 1 contract (can't trade fractional)**

**For larger accounts:**

$$
N = \frac{15\%}{32.1\%} \times 10 = 4.7 \rightarrow 5 \text{ contracts}
$$

### 3. Risk Budget


**Alternative calculation using dollar risk:**

$$
N = \frac{\text{Daily Risk Budget}}{\text{Contract Point Value} \times \sigma_{\text{daily}} \times \text{Price}}
$$

**Example - ES futures:**

- Risk budget: $10,000/day
- ES point value: $50/point
- Current price: 4,580
- Daily volatility: $32.1\% / \sqrt{252} = 2.02\%$

$$
\sigma_{\text{daily dollars}} = 4,580 \times 0.0202 = 92.5 \text{ points}
$$

$$
N = \frac{10,000}{50 \times 92.5} = \frac{10,000}{4,625} = 2.16 \rightarrow 2 \text{ contracts}
$$

**Hold 2 ES contracts to risk $10,000/day**

### 4. Optimal Lookback


**Trade-off between responsiveness and stability:**

**Mean squared error minimization:**

$$
\text{Optimal } n = \arg\min_{n} \mathbb{E}\left[(\sigma_t - \hat{\sigma}_t(n))^2\right]
$$

**Empirical optimal windows:**

| Asset Class | Optimal Window | Reason |
|------------|---------------|---------|
| Equities (ES, NQ) | 30-60 days | Moderate vol persistence |
| Commodities (CL, GC) | 20-40 days | Higher vol of vol |
| Bonds (ZN, ZB) | 40-90 days | Low vol of vol |
| FX (EUR, JPY) | 20-30 days | Rapid regime shifts |

**General rule: Higher vol of vol → Shorter window**

### 5. Expected Sharpe


**Theoretical Sharpe ratio of vol-targeted strategy:**

$$
\text{SR}_{\text{vol-target}} = \text{SR}_{\text{buy-hold}} \times \sqrt{1 + \frac{\text{Var}(\sigma)}{\mathbb{E}[\sigma]^2}}
$$

Where:
- $\text{Var}(\sigma)$ = Variance of volatility
- $\mathbb{E}[\sigma]$ = Average volatility

**Example - S&P 500:**

- Buy-hold SR: 0.50
- Average vol: 15%
- Vol std dev: 8%
- Variance: 64

$$
\text{SR}_{\text{vol-target}} = 0.50 \times \sqrt{1 + \frac{64}{225}} = 0.50 \times \sqrt{1.28} = 0.50 \times 1.13 = 0.57
$$

**Expected SR improvement: 13%**

**More volatile the volatility, greater the improvement**

### 6. Rebalancing


**Optimal rebalancing balances:**

- Responsiveness (more frequent = better tracking)
- Transaction costs (more frequent = higher costs)

**Total cost of rebalancing:**

$$
\text{Cost} = \underbrace{\text{Tracking Error}}_{\downarrow \text{with frequency}} + \underbrace{\text{Transaction Costs}}_{\uparrow \text{with frequency}}
$$

**Optimal frequency:**

$$
f^* = \sqrt{\frac{\text{Variance Penalty}}{\text{Transaction Cost}}}
$$

**Example:**

- Variance penalty: $1,000 per day of misalignment
- Transaction cost: $50 per rebalance
- Optimal: $\sqrt{1,000/50} = 4.5$ days

**Rebalance approximately weekly (every 5 days)**

**Practical guidelines:**

| Account Size | Rebalancing Frequency |
|-------------|---------------------|
| < $100k | Monthly (minimize costs) |
| $100k-$1M | Weekly (balanced) |
| > $1M | Daily (institutional) |

---

## Key ideas


### 1. Phase 1


**1. Assess Risk Tolerance:**

**Conservative investor:**

- Target: 8-10% volatility
- Equivalent: 60/40 stock/bond portfolio
- Max drawdown tolerance: 15-20%
- Annual risk budget: $8k-$10k per $100k

**Moderate investor:**

- Target: 12-15% volatility
- Equivalent: 100% stock portfolio
- Max drawdown tolerance: 25-35%
- Annual risk budget: $12k-$15k per $100k

**Aggressive investor:**

- Target: 18-25% volatility
- Equivalent: 1.5-2x levered stocks
- Max drawdown tolerance: 40-50%
- Annual risk budget: $18k-$25k per $100k

**2. Select Target Based on Goals:**

**For most traders starting out:**

- **Recommended: 15% target volatility**
- Matches historical S&P 500 long-term average
- Provides meaningful exposure
- Reasonable risk-reward

**3. Calculate Base Position:**

**For $100,000 account, 15% target:**

$$
\text{Base contracts} = \frac{100,000 \times 0.15}{\text{Contract Value} \times \text{Long-run Vol}}
$$

**ES futures example:**

- Contract value: $50 × 4,500 = $225,000
- Long-run vol: 15%

$$
N_{\text{base}} = \frac{100,000 \times 0.15}{225,000 \times 0.15} = \frac{15,000}{33,750} = 0.44
$$

**Base = 0.4-0.5 contracts (essentially 1 contract for $100k account)**

**For larger accounts:**

- $500k account: 2-3 base contracts
- $1M account: 4-5 base contracts
- Scale proportionally

### 2. Phase 2


**1. Choose Lookback Window:**

**Standard: 30-day window**

- Balances responsiveness and stability
- Captures recent regime
- Not too noisy

**Alternative: 60-day window**

- More stable
- Slower to react
- Better for less frequent rebalancing

**2. Calculate Daily Realized Volatility:**

**Method: Rolling standard deviation**

```python
import pandas as pd
import numpy as np

# Load price data
prices = pd.read_csv('ES_prices.csv')
prices['returns'] = np.log(prices['close'] / prices['close'].shift(1))

# Calculate 30-day
window = 30
prices['realized_vol'] = prices['returns'].rolling(window).std() * np.sqrt(252)

# Current volatility
current_vol = prices['realized_vol'].iloc[-1]
print(f"Current 30-day realized vol: {current_vol:.1%}")
```

**3. Track Volatility Over Time:**

**Create monitoring dashboard:**

| Date | Price | Daily Return | 30D Vol | Position Size |
|------|-------|-------------|---------|---------------|
| 2024-01-02 | 4,742 | +0.8% | 12.5% | 1.20x |
| 2024-01-03 | 4,758 | +0.3% | 12.3% | 1.22x |
| 2024-01-04 | 4,739 | -0.4% | 12.4% | 1.21x |

**Update daily, rebalance per schedule**

### 3. Phase 3


**1. Calculate Starting Position:**

**Example on Jan 5, 2024:**

- Account: $100,000
- Target vol: 15%
- Current 30-day vol: 12.8%
- ES price: 4,750

**Position calculation:**

$$
N = \frac{15\%}{12.8\%} \times 1 = 1.17 \rightarrow 1 \text{ contract}
$$

**Enter 1 ES contract long**

**2. Document Entry:**

```
Entry Date: January 5, 2024
ES Price: 4,750
Account Size: $100,000
Target Volatility: 15%
Current Realized Vol: 12.8%
Scaling Factor: 1.17x
Position: 1 ES contract long
Contract Value: $237,500
Expected Daily Risk: ~$10,000
```

**3. Set Rebalancing Schedule:**

**Weekly rebalancing (recommended):**

- Every Monday morning
- Calculate new realized vol (Friday close)
- Adjust position if needed
- Minimize transaction costs

**Criteria for rebalancing:**

- Position deviates >20% from target
- Example: Should hold 1.2x but holding 1.0x
- Deviation: (1.2 - 1.0) / 1.2 = 17% (no rebalance yet)
- Wait until 20% threshold

### 4. Phase 4


**1. Weekly Monitoring:**

**Every Monday:**

**Step 1: Calculate current vol**

```python
# Get last 30 days of
recent_returns = prices['returns'].tail(30)
current_vol = recent_returns.std() * np.sqrt(252)
```

**Step 2: Calculate target position**

```python
target_vol = 0.15
scaling_factor = target_vol / current_vol
target_contracts = int(round(scaling_factor * base_contracts))
```

**Step 3: Compare to current position**

```python
current_contracts = 1
deviation = abs(target_contracts - current_contracts) / target_contracts

if deviation > 0.20:  # 20% threshold
    # Rebalance
    print(f"Rebalance from {current_contracts} to {target_contracts}")
else:
    print("No rebalance needed")
```

**2. Rebalancing Examples:**

**Example A: Volatility spike (rebalance down)**

| Metric | Value |
|--------|-------|
| Previous position | 1 contract |
| Previous vol | 12.8% |
| New vol | 22.5% (spike!) |
| Target vol | 15% |
| New scaling | 15% / 22.5% = 0.67x |
| Target position | 0.67 × 1 = 0.67 → 1 contract |
| Deviation | 0% (no change needed yet) |

**But if had 3 contracts:**

- Target: 0.67 × 3 = 2.0
- Current: 3
- Deviation: 33% (exceeds 20% threshold)
- **Action: Reduce from 3 to 2 contracts**

**Example B: Volatility decline (rebalance up)**

| Metric | Value |
|--------|-------|
| Previous position | 1 contract |
| Previous vol | 22.5% |
| New vol | 14.2% (calming) |
| Target vol | 15% |
| New scaling | 15% / 14.2% = 1.06x |
| Target position | 1.06 × 1 = 1.06 → 1 contract |
| Deviation | 6% (under threshold) |

**No rebalance needed (wait for larger deviation)**

**3. Crisis Management:**

**When volatility spikes >30%:**

**March 2020 COVID example:**

| Date | Vol | Target Position | Actual | Action |
|------|-----|----------------|--------|--------|
| Mar 1 | 18% | 5 contracts | 5 | Hold |
| Mar 9 | 35% | 2.6 contracts | 5 | Sell 2 (to 3) |
| Mar 16 | 58% | 1.6 contracts | 3 | Sell 1 (to 2) |
| Mar 23 | 68% | 1.3 contracts | 2 | Sell 1 (to 1) |

**Automatic de-risking during crash**

**4. Recovery Management:**

**As volatility normalizes:**

| Date | Vol | Target Position | Action |
|------|-----|----------------|--------|
| Apr 6 | 52% | 1.7 contracts | Buy 1 (to 2) |
| Apr 20 | 38% | 2.4 contracts | Buy 1 (to 2, wait) |
| May 4 | 28% | 3.2 contracts | Buy 1 (to 3) |
| May 18 | 22% | 4.1 contracts | Buy 1 (to 4) |

**Systematic re-leveraging during recovery**

### 5. Phase 5


**1. Calculate Realized Portfolio Volatility:**

**Monthly check:**

```python
# Portfolio returns
portfolio_returns = returns * position_sizes

# Realized portfolio
portfolio_vol = portfolio_returns.std() * np.sqrt(252)

# Compare to target
print(f"Target: 15.0%")
print(f"Realized: {portfolio_vol:.1%}")
print(f"Tracking error: {abs(portfolio_vol - 0.15):.1%}")
```

**Good tracking:**

- Realized vol within ±2% of target
- Example: Target 15%, Realized 13.8%-16.2%

**2. Monitor Sharpe Ratio:**

**Calculate monthly:**

$$
\text{SR} = \frac{\text{Avg Monthly Return}}{\text{Std Dev Monthly Return}} \times \sqrt{12}
$$

**Example:**

- 12 months of returns: [2.1%, -0.8%, 1.5%, ..., 1.2%]
- Average: 1.1% per month
- Std dev: 4.3% per month
- SR = (1.1% / 4.3%) × √12 = 0.256 × 3.46 = 0.89

**Compare to buy-hold benchmark**

**3. Optimize Parameters:**

**After 6-12 months, test variations:**

| Parameter | Current | Test 1 | Test 2 | Best |
|-----------|---------|--------|--------|------|
| Lookback window | 30 days | 20 days | 60 days | ? |
| Rebalance freq | Weekly | Daily | Bi-weekly | ? |
| Threshold | 20% | 15% | 25% | ? |

**Backtest each combination, select highest Sharpe**

### 6. Complete Example


**Starting: January 2, 2024**

**Setup:**

- Account: $250,000
- Target vol: 15%
- Asset: ES futures (S&P 500)
- Lookback: 30 days
- Rebalance: Weekly (Mondays)
- Base position: 2.5 contracts

**Month 1 (January):**

| Date | ES Price | 30D Vol | Scaling | Target | Actual | Action |
|------|----------|---------|---------|--------|--------|--------|
| Jan 2 | 4,742 | 12.5% | 1.20x | 3.0 | 0 | Buy 3 |
| Jan 8 | 4,758 | 12.3% | 1.22x | 3.1 | 3 | Hold |
| Jan 15 | 4,801 | 11.8% | 1.27x | 3.2 | 3 | Hold |
| Jan 22 | 4,839 | 10.5% | 1.43x | 3.6 | 3 | Buy 1 (to 4) |
| Jan 29 | 4,891 | 9.8% | 1.53x | 3.8 | 4 | Hold |

**January return: +3.1% (vs S&P +1.7%)**

**Month 2-3 (Feb-Mar): Volatility spike**

| Date | ES Price | 30D Vol | Scaling | Target | Actual | Action |
|------|----------|---------|---------|--------|--------|--------|
| Feb 5 | 4,923 | 11.2% | 1.34x | 3.4 | 4 | Sell 1 (to 3) |
| Feb 12 | 4,884 | 15.8% | 0.95x | 2.4 | 3 | Sell 1 (to 2) |
| Feb 19 | 4,732 | 22.4% | 0.67x | 1.7 | 2 | Sell 1 (to 1) |
| Feb 26 | 4,689 | 26.8% | 0.56x | 1.4 | 1 | Hold |
| Mar 4 | 4,821 | 24.2% | 0.62x | 1.6 | 1 | Hold |

**Feb-Mar return: -2.2% (vs S&P -3.8%)**

**Months 4-6: Recovery**

| Month | Avg Vol | Avg Position | Return | S&P Return |
|-------|---------|-------------|--------|------------|
| April | 19.5% | 1.9 | +4.2% | +3.8% |
| May | 14.8% | 2.5 | +2.1% | +1.9% |
| June | 11.2% | 3.3 | +1.8% | +1.5% |

**6-Month Results:**

| Metric | Vol Target | Buy & Hold |
|--------|-----------|------------|
| Total return | +8.9% | +4.1% |
| Annualized | +18.5% | +8.4% |
| Volatility | 15.2% | 17.8% |
| Sharpe ratio | 0.97 | 0.34 |
| Max drawdown | -8.2% | -12.4% |

**Vol targeting outperformed:**

- Higher returns (+4.8%)
- Lower volatility (-2.6%)
- Much better Sharpe (2.9x)
- Smaller drawdown (-4.2%)

---

## Risk Metrics


### 1. Position Sizing


**For vol-targeted futures:**

**Position size volatility:**

$$
\text{Std}(N_t) = \text{Std}\left(\frac{\sigma_{\text{target}}}{\sigma_t}\right)
$$

**This depends on volatility of volatility:**

$$
\text{Vol of Vol} = \frac{\text{Std}(\sigma_t)}{\mathbb{E}[\sigma_t]}
$$

**Example - ES futures (2010-2024):**

- Average vol: 15.2%
- Vol std dev: 7.8%
- Vol of vol: 7.8% / 15.2% = 51%

**Position size range (15% target):**

- Low vol period (10%): 1.5x position
- Average vol (15%): 1.0x position
- High vol period (30%): 0.5x position
- **Position varies 3:1 ratio**

### 2. Leverage Tracking


**Effective leverage at any time:**

$$
\text{Leverage}_t = \frac{\text{Contract Value} \times N_t}{\text{Account Equity}}
$$

**Example evolution:**

| Date | Account | ES Price | Contracts | Notional | Leverage |
|------|---------|----------|-----------|----------|----------|
| Jan | $250k | 4,750 | 3 | $712k | 2.85x |
| Mar | $245k | 4,689 | 1 | $234k | 0.96x |
| Jun | $272k | 5,100 | 3 | $765k | 2.81x |

**Leverage cycles with volatility inversely**

### 3. Turnover Analysis


**Annual turnover from rebalancing:**

$$
\text{Turnover} = \sum_{i=1}^{52} |\Delta N_i| \times \text{Contract Value}
$$

**Example - $250k account, weekly rebalancing:**

- Average position change per week: 0.3 contracts
- Contract value: $250k
- Weekly turnover: $75k
- **Annual turnover: $75k × 52 = $3.9M**
- **Turnover ratio: $3.9M / $250k = 15.6x**

**High turnover but necessary for vol targeting**

### 4. Drawdown


**Max drawdown reduction:**

**Without vol targeting:**

$$
\text{DD}_{\text{max}} = \text{Max decline with fixed position}
$$

**With vol targeting:**

$$
\text{DD}_{\text{vol-target}} \approx 0.6 \times \text{DD}_{\text{fixed}}
$$

**Example - 2008 crisis:**

- Fixed position: -52% drawdown
- Vol targeting: -31% drawdown
- **Improvement: 21% less drawdown**

**Why:**

- Volatility spikes before/during crashes
- Vol targeting preemptively reduces exposure
- Less capital at risk when market falls

### 5. Tail Risk


**Value at Risk (VaR) comparison:**

**Fixed position:**

$$
\text{VaR}_{95} = 1.65 \times \sigma \times \text{Position}
$$

**Vol targeted:**

$$
\text{VaR}_{95} = 1.65 \times \sigma_{\text{target}} \times \text{(varies)}
$$

**Example:**

**Calm period (σ = 10%):**

- Fixed: 1.65 × 10% × 1 = 16.5% potential loss
- Vol target: 1.65 × 15% × 1.5 = 24.8% potential loss
- **Vol targeting has MORE risk in calm (taking more exposure)**

**Crisis period (σ = 40%):**

- Fixed: 1.65 × 40% × 1 = 66% potential loss
- Vol target: 1.65 × 15% × 0.375 = 9.3% potential loss
- **Vol targeting has LESS risk in crisis (reduced exposure)**

**Key insight: Risk reallocation from dangerous to safe periods**

---

## Real-World Examples


### 1. Pension Duration


**Background:**

- Lehman bankruptcy September 2008
- Massive volatility spike
- S&P 500 crashed -38% (peak to trough)

**Vol targeting performance:**

**Pre-crisis (January 2008):**

- S&P: 1,400
- 30-day vol: 16%
- Target vol: 15%
- Position: 0.94x (slightly under due to elevated vol)

**Crisis begins (September 2008):**

| Date | S&P | 30D Vol | Position | Action |
|------|-----|---------|----------|--------|
| Sep 1 | 1,282 | 22% | 0.68x | Reduce |
| Sep 15 | 1,192 | 38% | 0.39x | Reduce |
| Sep 29 | 1,106 | 52% | 0.29x | Reduce |
| Oct 10 | 899 | 68% | 0.22x | Reduce |

**Position went from 0.94x → 0.22x (77% reduction)**

**Results (Sep-Oct 2008):**

| Strategy | Return | Explanation |
|----------|--------|-------------|
| Buy & Hold | -31.2% | Full exposure to crash |
| Vol Target (15%) | -14.8% | Automatic de-leveraging |
| **Saved** | **16.4%** | Crash protection |

**Recovery (Nov 2008 - Mar 2009):**

| Date | S&P | 30D Vol | Position | Action |
|------|-----|---------|----------|--------|
| Nov 20 | 752 | 62% | 0.24x | Hold (vol still high) |
| Dec 31 | 903 | 48% | 0.31x | Slight increase |
| Jan 30 | 825 | 44% | 0.34x | Gradual re-lever |
| Feb 27 | 735 | 52% | 0.29x | Reduce again |
| Mar 9 | 676 | 58% | 0.26x | Market bottom |

**Bottom line (Jan 2008 - Mar 2009):**

- Buy & hold: -48.2%
- Vol targeting: -22.7%
- **Outperformance: 25.5% during worst crisis**

**Why it worked:**

- Volatility spiked before prices crashed
- Vol targeting reduced exposure proactively
- Captured some upside, avoided most downside
- **Asymmetric performance: The strategy's best feature**

### 2. Transition Risk


**Timeline:**

**Pre-COVID (January 2020):**

- S&P: 3,280
- Vol: 12.5%
- Position: 1.20x (calm market, leveraged up)

**Crash (February-March 2020):**

| Week | S&P | 30D Vol | Position | Weekly Return |
|------|-----|---------|----------|---------------|
| Feb 17 | 3,380 | 11% | 1.36x | +0.8% |
| Feb 24 | 3,225 | 18% | 0.83x | **-2.3%** (de-lever) |
| Mar 2 | 2,954 | 28% | 0.54x | -4.8% (reduced exposure!) |
| Mar 9 | 2,746 | 38% | 0.39x | -3.2% |
| Mar 16 | 2,386 | 58% | 0.26x | -6.5% (minimal position) |
| Mar 23 | 2,237 | 68% | 0.22x | -2.9% (bottom) |

**Cumulative crash loss:**

- Buy & hold: -33.9% (3,380 → 2,237)
- Vol targeting: -18.2%
- **Protected: 15.7%**

**Recovery (April-August 2020):**

| Month | S&P | 30D Vol | Position | Monthly Return |
|-------|-----|---------|----------|----------------|
| Apr | 2,912 | 52% | 0.29x | +4.2% (vol still high) |
| May | 3,044 | 38% | 0.39x | +2.1% |
| Jun | 3,100 | 28% | 0.54x | +1.8% (re-leveraging) |
| Jul | 3,271 | 22% | 0.68x | +3.5% |
| Aug | 3,500 | 18% | 0.83x | +4.7% |

**Cumulative recovery:**

- Buy & hold: +56.5% (2,237 → 3,500)
- Vol targeting: +65.2% (started re-leveraging during recovery)
- **Outperformance: 8.7% in recovery**

**Full cycle (Jan 2020 - Aug 2020):**

- Buy & hold: +6.5% (3,280 → 3,500)
- Vol targeting: +35.8%
- **Total outperformance: 29.3%**

**Why massive outperformance:**

- Protected in crash (-18% vs -34%)
- Participated in recovery (position growing as vol fell)
- Re-leveraged during the most explosive recovery phase
- **This is vol targeting at its best**

### 3. Portable Alpha


**Background:**

- Extremely low volatility (VIX at 9)
- Massive short vol positions
- Feb 5, 2018: VIX spike from 17 → 37 intraday

**Vol targeting position:**

**Pre-event (January 2018):**

- S&P: 2,823
- 30-day vol: 6.8% (extremely calm)
- Target vol: 15%
- Position: 15% / 6.8% = 2.21x
- **Heavily leveraged (calm = big position)**

**Event day (Feb 5, 2018):**

| Time | S&P | Intraday Vol | Position | Action |
|------|-----|-------------|----------|--------|
| Open | 2,762 | 8% | 2.21x | Enter day heavy |
| 11 AM | 2,695 | 18% | 2.21x (haven't rebalanced) | **Problem!** |
| 1 PM | 2,648 | 28% | Should be 0.54x | Down -9.2% with 2x leverage |
| Close | 2,648 | 32% | Rebalance to 0.47x | Final: -12.8% |

**This was a LOSS compared to buy-hold:**

- Buy & hold: -3.8% (2,762 → 2,648)
- Vol targeting: -12.8% (leveraged 2.2x into the crash)
- **Underperformance: -9.0%**

**What went wrong:**

- **Intraday volatility spike**
- Position sized for 6.8% vol at open
- Vol jumped to 32% by close
- Daily rebalancing TOO SLOW
- Caught holding 2.2x leverage during crash

**Recovery (Feb 6-9):**

- S&P recovered to 2,681
- Vol normalized to 18%
- Vol targeting position: 0.83x
- Participated in recovery: +2.8%

**Lesson:**

- **Intraday vol spikes are dangerous**
- Daily rebalancing has lag risk
- Consider intraday monitoring for large accounts
- This is the strategy's main weakness

### 4. Tactical Duration


**Long-term vol targeting test:**

**Setup:**

- Start: January 2000
- Asset: Nasdaq futures (NQ)
- Target: 20% volatility (higher for tech)
- Timeframe: 3 years

**Timeline:**

| Period | NQ Level | Avg Vol | Avg Position | Return |
|--------|----------|---------|-------------|---------|
| 2000 Q1 | 4,500 | 28% | 0.71x | -12.5% |
| 2000 Q2-Q4 | 3,200 | 42% | 0.48x | -35.8% |
| 2001 | 2,100 | 38% | 0.53x | -21.2% |
| 2002 | 1,320 | 35% | 0.57x | -18.5% |

**3-year results:**

- Buy & hold: -71.2% (4,500 → 1,295)
- Vol targeting: -54.8%
- **Outperformance: 16.4%**

**Why not better?**

- Persistent high volatility (no normalization)
- Vol targeting kept reducing position
- But still exposed to downtrend
- **Protection, but still losses in bear market**

**Key lesson:**

- Vol targeting reduces drawdown, doesn't eliminate
- Still negative in prolonged bear markets
- Helps more in V-shaped crashes (2008, 2020)
- Less helpful in grinding bears (2000-2002)

### 5. Duration Hedge


**Background:**

- Extremely calm year (VIX averaged 11)
- S&P rallied +19.4%
- Perfect environment for vol targeting

**Performance:**

**Quarterly tracking:**

| Quarter | S&P Return | Avg Vol | Avg Position | Vol Target Return |
|---------|------------|---------|-------------|-------------------|
| Q1 | +5.5% | 8.2% | 1.83x | +10.1% |
| Q2 | +2.6% | 7.5% | 2.00x | +5.2% |
| Q3 | +3.9% | 6.8% | 2.21x | +8.6% |
| Q4 | +6.1% | 9.1% | 1.65x | +10.1% |

**Full year 2017:**

- Buy & hold: +19.4%
- Vol targeting: +38.2%
- **Outperformance: 18.8% (nearly double!)**

**Why huge outperformance:**

- Consistently low volatility (avg 8%)
- Sustained leverage (avg 1.9x)
- Steady uptrend captured with 2x exposure
- **This is the upside of vol targeting**

**Risk was actually LOW:**

- Despite 1.9x leverage
- Realized portfolio vol: 15.2% (right on target!)
- Not reckless, just efficiently using calm conditions

**Key lesson:**

- Vol targeting AMPLIFIES returns in calm bull markets
- Maintains target risk despite leverage
- Opposite of typical "leverage in panic" behavior

---

## Risk Management


### 1. Position Sizing


**Implement hard limits:**

**Maximum leverage cap:**

$$
\text{Max leverage} = 3.0x \quad \text{(never exceed)}
$$

**Why:**

- Extreme calm (vol = 5%) would imply 3x position
- Too risky (flash crash could wipe out account)
- **Cap at 3x for safety**

**Minimum position:**

$$
\text{Min position} = 0.1x \quad \text{(maintain some exposure)}
$$

**Why:**

- Extreme vol (vol = 150%) would imply 0.1x position
- Almost out of market
- **Keep skin in game for eventual recovery**

**Example with caps:**

| Vol Level | Uncapped Position | Capped Position |
|-----------|------------------|-----------------|
| 5% (calm) | 3.00x | **3.00x (at cap)** |
| 10% | 1.50x | 1.50x |
| 15% (target) | 1.00x | 1.00x |
| 30% | 0.50x | 0.50x |
| 60% (crisis) | 0.25x | 0.25x |
| 150% (panic) | 0.10x | **0.10x (at floor)** |

### 2. Rebalancing


**Avoid excessive trading:**

**Threshold rule:**

$$
\text{Rebalance if } \left|\frac{N_{\text{current}} - N_{\text{target}}}{N_{\text{target}}}\right| > 0.20
$$

**Example:**

- Current position: 3 contracts
- Target position: 3.5 contracts
- Deviation: (3.5 - 3) / 3.5 = 14%
- **Under 20% threshold → No rebalance**

**Wait until:**

- Target: 3.8 contracts
- Deviation: (3.8 - 3) / 3.8 = 21%
- **Exceeds 20% → Rebalance to 4 contracts**

**Benefits:**

- Reduces transaction costs (fewer trades)
- Prevents over-trading on noise
- Still tracks target vol well

### 3. Volatility


**Use multiple vol measures:**

**Primary: 30-day realized vol**

- Main signal for rebalancing

**Secondary: EWMA vol (faster response)**

$$
\sigma_{\text{EWMA}} = \sqrt{\lambda \sigma_{t-1}^2 + (1-\lambda)r_t^2}
$$

With $\lambda = 0.94$ (RiskMetrics standard)

**Tertiary: Implied vol (VIX)**

- Forward-looking market expectation

**Decision rule:**

- If all three agree (spike or calm) → Strong signal
- If divergent → Wait for consensus
- **Prevents false signals**

### 4. Maximum Drawdown


**Portfolio-level circuit breaker:**

**Monthly drawdown limit:**

$$
\text{If DD} > -15\% \text{ in any month} \rightarrow \text{Halt and review}
$$

**Example:**

- Month starts: $500k
- Month ends: $415k (-17%)
- **Triggered: Stop trading, investigate**

**Possible causes:**

- Model broken (vol measurement wrong)
- Regime shift (correlations changed)
- Execution issues (slippage excessive)
- **Fix before resuming**

**Annual drawdown limit:**

$$
\text{If DD} > -25\% \text{ from peak} \rightarrow \text{Reduce target vol}
$$

**Example:**

- Peak: $500k
- Current: $365k (-27%)
- **Action: Reduce target from 15% → 10%**
- De-risk until recovery

### 5. Diversification


**Don't use single futures contract:**

**Multi-asset vol targeting:**

| Asset | Target Vol | Weight | Contribution |
|-------|------------|--------|-------------|
| ES (S&P) | 15% | 40% | 6.0% |
| NQ (Nasdaq) | 20% | 30% | 6.0% |
| GC (Gold) | 15% | 15% | 2.3% |
| CL (Crude) | 25% | 15% | 3.8% |
| **Total** | - | 100% | **12.2%** |

**Benefits:**

- Uncorrelated volatilities
- Smoother overall portfolio vol
- Better risk-adjusted returns

### 6. Transaction Cost


**Estimate total costs:**

$$
\text{Annual costs} = \text{Turnover} \times \text{Commission} + \text{Slippage}
$$

**Example:**

- Turnover: 15x per year
- Commission: $2.50 per side × 2 = $5 round-trip
- Contracts: Average 3
- Rebalances: 52 per year (weekly)
- **Commission: $5 × 3 × 52 = $780/year**

**Slippage:**

- 1 tick slippage average = $12.50 per contract
- Trades: 3 contracts × 52 = 156 contract-trades
- **Slippage: $12.50 × 156 = $1,950/year**

**Total costs: $780 + $1,950 = $2,730**

**On $250k account: 1.1% drag**

**Must exceed this to be worthwhile!**

### 7. Risk Management


**Before starting vol targeting:**

✅ Target volatility set (based on risk tolerance)
✅ Lookback window chosen (20-60 days)
✅ Rebalancing frequency determined (daily/weekly/monthly)
✅ Position size limits set (max 3x, min 0.1x)
✅ Rebalancing threshold set (20% deviation)
✅ Transaction cost budget estimated
✅ Drawdown limits defined (monthly -15%, annual -25%)
✅ Monitoring system in place (daily vol calculation)

**During operation:**

✅ Daily vol calculation accurate
✅ Position size within bounds
✅ Rebalancing when threshold exceeded
✅ Transaction costs tracked
✅ Portfolio vol near target (±2%)
✅ Sharpe ratio improving vs. benchmark
✅ Drawdown limits respected

---



## Final Wisdom


> "Volatility targeting is the institutional investor's secret weapon—it's how smart money maintains constant risk budgets across market regimes. The math is simple: position size equals target vol divided by current vol. But the impact is profound: you automatically lever up when markets are calm and safe, and you automatically de-lever when markets are turbulent and dangerous. This is the opposite of typical investor behavior (panic and leverage at the worst times). Over long horizons, vol targeting improves Sharpe ratios by 20-30%, reduces drawdowns by similar amounts, and creates smoother, more reliable returns. But it's not magic: flash crashes can catch you over-leveraged, persistent high volatility can leave you under-exposed to rebounds, and transaction costs matter. The key to success is systematic discipline, appropriate position limits, and a long-term perspective. Volatility targeting won't make you rich overnight, but over decades, it can dramatically improve your risk-adjusted wealth accumulation."

**Key to success:**

- Set appropriate target vol (15% for moderate risk)
- Calculate realized vol correctly (30-60 day window)
- Rebalance systematically (weekly, with 20% threshold)
- Impose position limits (max 3x, min 0.1x)
- Monitor intraday for flash crashes (VIX alerts)
- Diversify across asset classes (ES, GC, CL, bonds)
- Track transaction costs (keep below 2% annually)
- Measure success by Sharpe ratio (not raw returns)

**Most important:** Volatility targeting is a long-term risk management framework, not a get-rich-quick strategy. It works by systematically reallocating risk from dangerous periods (high vol) to safe periods (low vol), creating smoother, more consistent returns with better risk-adjusted performance. Success requires discipline to follow the system through all market regimes—especially when high volatility makes you want to abandon it (precisely when its protection is most valuable). Think in decades, not months, and let compound returns from better Sharpe ratios work their magic over time. 📊📉📈⚖️