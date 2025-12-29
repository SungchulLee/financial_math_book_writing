# Dispersion Trading

**Dispersion trading** is a strategy where you profit from the difference between index volatility and the weighted average of individual stock volatilities by exploiting the correlation structure of the market.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/dispersion_trading_correlation.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 1:** Dispersion Trading Correlation visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/dispersion_trading_pnl.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 2:** Dispersion Trading Pnl visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/dispersion_trading_realized_implied.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 3:** Dispersion Trading Realized Implied visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/dispersion_trading_vol_comparison.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 4:** Dispersion Trading Vol Comparison visualization.

---

## The Core Insight

**The fundamental idea:**

- An index (like S&P 500) has its own volatility
- Each stock in the index also has its own volatility
- **These are NOT the same thing!**
- Index volatility depends on how correlated the stocks are
- You can bet that this relationship is mispriced

**The key equation:**
$$
\sigma_{\text{index}}^2 = \sum w_i^2 \sigma_i^2 + \sum \sum w_i w_j \rho_{ij} \sigma_i \sigma_j
$$

**In plain English:**

- Index volatility = individual volatilities + correlation effects
- When correlation is high → index vol is high (stocks move together)
- When correlation is low → index vol is low (stocks offset each other)
- You can trade this relationship!

**You're essentially betting: "The market has the wrong view on how much stocks will move together."**

---

## The Volatility-Correlation Relationship

**This is CRUCIAL to understand:**

### A Simple Example: Two-Stock Index

**Imagine an index with two stocks (equal weighted):**

**Stock A:** $\sigma_A = 30\%$ volatility
**Stock B:** $\sigma_B = 30\%$ volatility

**What's the index volatility?** It depends on correlation!

**Case 1: Perfect Correlation ($\rho = +1$)**
- Stocks always move together
- Index volatility: $\sigma_{\text{index}} = 30\%$
- Index vol = Average of individual vols

**Case 2: No Correlation ($\rho = 0$)**
- Stocks move independently
- Index volatility: $\sigma_{\text{index}} = \frac{30\%}{\sqrt{2}} \approx 21\%$
- Index vol < Individual vols (diversification!)

**Case 3: Negative Correlation ($\rho = -1$)**
- Stocks move in opposite directions
- Index volatility: $\sigma_{\text{index}} = 0\%$
- Perfectly hedged!

**The key insight:** Index vol is ALWAYS less than or equal to the average individual vol (unless correlation = 1)

$$
\sigma_{\text{index}} \leq \sqrt{\sum w_i^2 \sigma_i^2}
$$

**This gap is what dispersion traders exploit!**

---

## What Is Dispersion Trading?

**Dispersion trading is betting on the CORRELATION structure:**

### The Fundamental Trade

**Classic "Long Dispersion" (Most Common):**

1. Sell index options (short index volatility) 
2. Buy individual stock options (long individual stock volatilities)
3. Delta hedge everything
4. Profit when stocks "disperse" (move independently, low correlation)

**"Short Dispersion" (Opposite):**

1. Buy index options (long index volatility)
2. Sell individual stock options (short individual stock volatilities)
3. Delta hedge everything
4. Profit when stocks "correlate" (move together, high correlation)

**What you're betting on:**

- **Long dispersion:** "Stocks will move independently (low correlation)"
- **Short dispersion:** "Stocks will move together (high correlation)"

---

## The Basic Idea

**What you do (Long Dispersion):**

1. **Choose an index** (e.g., S&P 500, but often use a smaller basket like 10-20 stocks)
2. **Sell index options** (typically ATM straddles on the index)
3. **Buy options on individual stocks** (ATM straddles on each component)
4. **Delta hedge everything** (both index and all individual stocks)
5. **Position size** to be roughly volatility-neutral overall
6. **Profit when** stocks move around independently (low correlation)

**The goal:** Profit when realized correlation is lower than what was priced into the options (implied correlation).

**Key insight:** You're not betting on whether volatility is high or low—you're betting on how TOGETHER stocks move!

---

## The Portfolio

Your dispersion trading portfolio consists of:

$$
\Pi = \text{Short Index Options} + \text{Long Individual Options} + \text{Delta Hedges}
$$

More precisely:

$$
\Pi = -V_{\text{index}}(S_{\text{index}}, t) + \sum_{i=1}^{n} w_i V_i(S_i, t) - \Delta_{\text{index}} \cdot S_{\text{index}} + \sum_{i=1}^{n} \Delta_i \cdot S_i
$$

where:
- $V_{\text{index}}$ = index option value (you're short)
- $V_i$ = individual stock option values (you're long)
- $w_i$ = weights chosen to make position volatility-neutral
- Delta hedges on both index and all stocks

**Why this structure?**
- Short index options: negative exposure to index vol
- Long individual options: positive exposure to individual vols
- Net exposure: correlation/dispersion
- Delta hedges: remove directional risk

---

## Understanding Implied Correlation

**Before we can understand dispersion trading P&L, we need implied correlation:**

### What Is Implied Correlation?

**From options, we observe:**

- Index implied volatility: $\sigma_{\text{index}}^{\text{implied}}$ (from index options)
- Individual implied volatilities: $\sigma_i^{\text{implied}}$ (from single-stock options)

**We can back out implied correlation:**

$$
\rho^{\text{implied}} = \frac{(\sigma_{\text{index}}^{\text{implied}})^2 - \sum w_i^2 (\sigma_i^{\text{implied}})^2}{\sum \sum w_i w_j \sigma_i^{\text{implied}} \sigma_j^{\text{implied}}}
$$

**This is the correlation that the market is pricing in!**

### Example: Calculating Implied Correlation

**Market data:**

- SPX (S&P 500 index) IV = 20%
- Average single-stock IV = 35%
- Equal-weighted basket of 10 stocks

**Simplified calculation:**
$$
(20\%)^2 = \frac{1}{10}(35\%)^2 + \text{correlation terms}
$$

Solving: implied correlation ≈ 50%

**Interpretation:** Market is pricing in 50% correlation among stocks.

**Your trade:**

- If you think realized correlation will be < 50% → long dispersion
- If you think realized correlation will be > 50% → short dispersion

---

## The P&L Formula

**For a dispersion trade, the P&L is complex, but conceptually:**

$$
\delta \Pi \approx \underbrace{\text{Correlation P\&L}}_{\text{primary profit source}} + \underbrace{\text{Vega P\&L}}_{\text{side effect}} + \underbrace{\text{Gamma P\&L}}_{\text{rebalancing}} - \underbrace{\text{Net Theta}}_{\text{carry}}
$$

**Breaking it down:**

### 1. Correlation P&L (Your Main Bet)

**This is what you're trading:**

$$
\text{Correlation P\&L} \approx f(\rho^{\text{realized}} - \rho^{\text{implied}})
$$

- **Long dispersion:** Profit when $\rho^{\text{realized}} < \rho^{\text{implied}}$ (stocks move independently)
- **Short dispersion:** Profit when $\rho^{\text{realized}} > \rho^{\text{implied}}$ (stocks move together)

### 2. Vega P&L (Side Effect)

**Your position has residual vega exposure:**

- Short index vega (short index options)
- Long individual vega (long stock options)
- Net vega ≠ 0 (usually slightly long vega overall)

**Can work for or against you if IVs change**

### 3. Gamma P&L (Rebalancing)

**From delta hedging rebalancing:**

- Short gamma on index
- Long gamma on individuals
- Net gamma ≈ 0 if weighted properly
- But generates P&L from rebalancing

### 4. Net Theta (Carry)

**Time decay:**

- Collect theta from short index options
- Pay theta from long individual options
- Net theta is usually close to zero (but not exactly)

**Bottom line:** You profit primarily when realized correlation differs from implied correlation in your favor.

---

## Concrete Example: Long Dispersion Trade

**Setup:**

**Index:** SPX at 4,000
- Index IV: 18%
- Implied correlation: 60%

**Basket:** 10 equal-weighted stocks
- Average individual IV: 30%
- Your view: Realized correlation will be 40% (lower than implied)

**The Trade:**

1. **Sell 10 SPX ATM straddles**
   - Receive premium from index volatility
   - Short index vega, short index gamma
   - Delta: hedge with index futures

2. **Buy 1 ATM straddle on each of 10 stocks**
   - Pay premium for individual volatility
   - Long individual vega, long individual gamma
   - Delta: hedge each stock individually

3. **Position sizing**
   - Weight individual positions so total vega ≈ index vega
   - Approximately volatility-neutral

**Scenario 1: Low Correlation (You're Right!)**

Over 30 days:
- Stocks move around independently
- Stock A up 5%, Stock B down 4%, Stock C up 6%, etc.
- Index moves only 1% (movements offset each other)
- Realized correlation: 40%

**Your P&L:**

- **Individual options (long gamma):** Profit from stocks bouncing around → +$10,000
- **Index options (short gamma):** Small loss from index not moving much → -$2,000
- **Net P&L:** +$8,000 ✓

**You profited because stocks moved independently (low correlation)!**

**Scenario 2: High Correlation (You're Wrong)**

Over 30 days:
- Stocks move together (high correlation)
- All stocks up 5% or all down 5%
- Index moves 5% (no diversification)
- Realized correlation: 80%

**Your P&L:**

- **Individual options (long gamma):** Profit from stocks moving → +$5,000
- **Index options (short gamma):** Large loss from index moving a lot → -$12,000
- **Net P&L:** -$7,000 ✗

**You lost because stocks moved together (high correlation)!**

---

## Long Dispersion vs. Short Dispersion

### Long Dispersion (Most Common)

**Position:**

- Short index options
- Long individual stock options
- Delta hedge everything

**Bet:**

- Realized correlation < Implied correlation
- "Stocks will move independently"
- "Dispersion will increase"

**When to use:**

- High market stress (correlations typically elevated)
- After crashes (correlation spike, likely to revert)
- Implied correlation > historical average
- Market pricing in too much "together" movement

**Risk profile:**

- Limited profit (can't make more than premium collected/paid difference)
- Unlimited loss if correlation spikes
- Theta is approximately neutral
- Positive convexity (gamma)

**Typical market environment:**

- Crisis aftermath
- High VIX
- Market pricing in systemic risk

### Short Dispersion

**Position:**

- Long index options
- Short individual stock options
- Delta hedge everything

**Bet:**

- Realized correlation > Implied correlation
- "Stocks will move together"
- "Dispersion will decrease"

**When to use:**

- Low market stress (correlations low)
- Calm markets (correlation likely to spike)
- Implied correlation < historical average
- Before systemic events

**Risk profile:**

- Limited profit
- Unlimited loss if correlation crashes
- Theta is approximately neutral
- Negative convexity (gamma)

**Typical market environment:**

- Calm bull markets
- Low VIX
- Complacent markets

---

## Why Dispersion Trading Exists: The Dispersion Premium

**Historical observation:**

**Dispersion premium:** Implied correlation is typically HIGHER than realized correlation.

**Why?**

1. **Flight to quality:** In crises, everyone wants index options (systemic hedges)
   - Demand drives up index option prices
   - Higher index IV → higher implied correlation
   
2. **Supply/demand imbalance:** 

   - Many institutions want to hedge systematic risk (buy index puts)
   - Fewer want to hedge individual stock risk
   - Creates structural bid for index options

3. **Behavioral bias:**

   - Market overestimates how much stocks move together
   - Fear of systemic risk is overstated

4. **Diversification illusion:**

   - Index options price in less diversification benefit than actually exists

**Result:** Long dispersion (short implied correlation) has positive expected return on average!

**This is similar to:**

- Volatility risk premium (IV > realized vol)
- But for correlation instead of volatility

---

## Dispersion Trading vs. Other Strategies

| Strategy | What You Trade | Primary Exposure | What You Want |
|----------|---------------|------------------|---------------|
| **Delta Hedging** | Nothing (hedged) | None | Stability |
| **Gamma Scalping** | Realized volatility | Gamma | Stock to move |
| **Vega Trading** | Implied volatility | Vega | IV to change |
| **Dispersion Trading** | Correlation structure | Correlation | Stocks to move independently (long) or together (short) |

**Key differences:**

### Dispersion vs. Gamma Scalping

**Similarities:**

- Both involve delta hedging
- Both have gamma exposure
- Both profit from realized movement

**Differences:**

- **Gamma scalping:** Single asset, want it to move
- **Dispersion:** Multiple assets, want them to move INDEPENDENTLY

### Dispersion vs. Vega Trading

**Similarities:**

- Both trade mispriced volatility metrics
- Both delta hedge

**Differences:**

- **Vega:** Trade level of volatility (high vs. low)
- **Dispersion:** Trade structure of volatility (together vs. independent)

### Dispersion vs. Correlation Trading

**These are almost the same!**

**Subtle difference:**

- **Dispersion trading:** Implemented via options (trade implied correlation)
- **Correlation trading:** Can use variance swaps, correlation swaps (cleaner exposure)
- Dispersion trading is really "correlation trading via options"

---

## How Dispersion Trading Works

**Step-by-step process:**

### 1. Identify Mispriced Correlation

**Analysis:**

- Calculate current implied correlation from option prices
- Compare to historical realized correlation
- Look at correlation percentile (historical ranking)
- Identify regime (crisis vs. calm)

**Tools:**

- Implied correlation calculators
- Historical correlation charts
- Correlation indices (e.g., CBOE correlation index)
- Cross-asset correlation analysis

**Rule of thumb:**

- Implied correlation > 70% → consider long dispersion
- Implied correlation < 40% → consider short dispersion

### 2. Select Your Basket

**Options:**

**Option A: Trade the full index (e.g., all S&P 500 stocks)**
- Most accurate
- Operationally complex (hedge 500 stocks!)
- Usually impractical

**Option B: Trade a representative basket**
- Select 10-30 liquid stocks
- Cover major sectors
- Highly correlated with index
- Practical and efficient

**Considerations:**

- Liquidity (need tight option spreads)
- Sector diversification
- Weighting scheme (equal-weighted or market-cap weighted)

### 3. Establish Positions

**For long dispersion:**

**Sell index options:**

- ATM straddles (max vega)
- Size based on portfolio risk
- Shorter-dated options (higher theta)

**Buy individual options:**

- ATM straddles on each stock
- Weight to match index vega
- Match maturity with index options

**Delta hedge:**

- Hedge index position (with futures or ETF)
- Hedge each stock individually
- Continuous rebalancing

### 4. Position Sizing

**Key principle: Volatility neutrality**

$$
\text{Vega}_{\text{index}} \approx \sum w_i \cdot \text{Vega}_i
$$

**Example:**

- Index straddle vega: $10,000 per 1% IV
- Each stock straddle vega: $1,000 per 1% IV
- Use 10 stock positions to match

**This ensures you're truly trading correlation, not volatility level!**

### 5. Manage the Trade

**Daily tasks:**

- Rebalance delta on index and all stocks
- Monitor implied vs. realized correlation
- Adjust weights as needed

**Risk management:**

- Set correlation stop-loss (if correlation moves against you)
- Monitor individual position risks
- Be aware of events (earnings, etc.)

### 6. Exit Strategy

**Exit when:**

- Correlation converges to your target
- Time decay becomes too large
- Risk/reward deteriorates
- Structural change invalidates thesis

**Typical hold period:** 1-3 months (enough time for correlation to realize)

---

## Challenges and Complexities

### 1. Operational Complexity

**Managing many positions:**

- Must trade and hedge 10-50 assets simultaneously
- Delta rebalancing is labor-intensive
- Requires sophisticated systems
- High execution risk

### 2. Transaction Costs

**Costs multiply:**

- Bid-ask spreads on 10-50 options
- Delta hedging costs on all assets
- Frequent rebalancing
- Can overwhelm P&L if not careful

### 3. Imperfect Correlation Exposure

**Reality:**

- Also have vega exposure (not purely correlation)
- Gamma P&L from rebalancing
- Theta drift
- Hard to get "pure" correlation bet

### 4. Model Risk

**Assumptions:**

- Implied correlation calculation has assumptions
- Basket must track index well
- Correlation is not constant (regime changes)

### 5. Liquidity Risk

**Problems:**

- Individual stock options less liquid than index
- Can't exit all positions simultaneously
- Slippage on large positions

### 6. Event Risk

**Individual stock events:**

- Earnings announcements
- Mergers, acquisitions
- Regulatory actions
- Can blow up individual positions

### 7. Tail Risk

**Extreme scenarios:**

- Market crashes → correlation spikes to 1
- Long dispersion can suffer massive losses
- "Everything correlates in a crisis"

---

## Pros and Cons

### Advantages ✓

**1. Structural edge (dispersion premium)**
- Implied correlation > realized correlation historically
- Long dispersion has positive expected return
- Statistical edge backed by data

**2. Diversification**
- Different from pure volatility bets
- Low correlation to traditional assets
- Good portfolio diversifier

**3. Crisis performance (long dispersion)**
- Profits when correlations revert after spikes
- Good hedge for systematic risk
- Benefits from market recovery

**4. Market neutral**
- Delta hedged on all assets
- No directional bet
- Isolated correlation exposure

**5. Quantifiable edge**
- Can measure implied vs. historical correlation
- Statistical analysis possible
- Backtestable strategy

**6. Multiple entry points**
- Can trade before/after crises
- Correlation cycles predictably
- Many regimes to exploit

### Disadvantages ✗

**1. Operationally complex**
- Must manage many positions simultaneously
- Intensive delta rebalancing
- Requires sophisticated systems and expertise
- Not for retail traders

**2. High transaction costs**
- Many bid-ask spreads
- Frequent rebalancing
- Can overwhelm profits
- Needs scale to be efficient

**3. Impure exposure**
- Also exposed to vega, gamma, theta
- Hard to isolate pure correlation bet
- Multiple risk factors interact

**4. Tail risk (for long dispersion)**
- Correlation can spike to 1 in crises
- "When you need diversification most, it fails"
- Unlimited loss potential

**5. Timing is crucial**
- Correlation can stay elevated for extended periods
- Theta decay while waiting
- Need catalyst for reversion

**6. Model and execution risk**
- Implied correlation calculation has assumptions
- Basket tracking error
- Liquidity issues
- Slippage on rebalancing

**7. Capital intensive**
- Need margin for many positions
- Must maintain hedges on all assets
- Requires significant capital

**8. Event risk**
- Individual stock events (earnings, M&A)
- Can create losses unrelated to correlation
- Hard to fully hedge

---

## When Dispersion Trading Works Best

### For Long Dispersion

**Favorable conditions:**

- **High implied correlation** (> 70% or historically elevated)
- **Post-crisis environment** (correlations spiked, likely to revert)
- **Market stress declining** (fear subsiding)
- **High VIX** with signs of stabilization
- **Panic has peaked** (correlation about to decline)

**Catalysts:**

- Crisis aftermath (2008-2009, COVID-2020)
- Market calming after systemic shock
- Central bank intervention (reduces systemic risk)
- Sector rotation (stocks decouple)

**Example:** March 2020 COVID crash
- Correlation spiked to 90%+
- Long dispersion positioned for reversion
- As market stabilized, correlations declined → profits

### For Short Dispersion

**Favorable conditions:**

- **Low implied correlation** (< 40% or historically depressed)
- **Calm bull market** (complacency)
- **Low VIX** (< 15)
- **Extended rally** (correlation about to spike)

**Catalysts:**

- Building systemic risk
- Overdue correction
- Macro shocks on horizon
- Fed tightening cycles

**Example:** Late 2019 (pre-COVID)
- Correlation very low (< 30%)
- Market complacent
- Short dispersion positioned for correlation spike
- COVID hit → correlations spiked → profits

### General Favorable Conditions

- Liquid options markets
- Low transaction costs
- Clear correlation regime (extreme high or low)
- Mean reversion tendency evident
- Sufficient time to expiration (1-3 months)

**Unfavorable conditions:**

- Mid-range correlation (40-60%)
- Unclear regime
- High transaction costs
- Illiquid individual options
- Near expiration (high gamma, operational risk)
- During earnings seasons (event risk)

---

## Position Sizing and Risk Management

### Correlation Stop-Loss

**Set limits:**

- If long dispersion and correlation spikes 20% → exit
- If short dispersion and correlation crashes 20% → exit
- Don't fight major correlation regime changes

### Vega Neutrality

**Maintain:**

- Monitor net vega exposure
- Adjust weights if IVs change significantly
- Goal: pure correlation exposure

### Individual Position Limits

**Risk controls:**

- Maximum loss per stock
- Event risk management (reduce size before earnings)
- Diversification across sectors

### Leverage Constraints

**Capital management:**

- Don't over-leverage
- Correlation moves can be swift
- Maintain margin cushion

---

## Advanced: Pure Correlation Products

**For institutional traders, there are cleaner alternatives to dispersion trading:**

### Correlation Swaps

**Structure:**

- Direct bet on correlation
- Payoff: (Realized correlation - Strike) × Notional
- No options, no delta hedging
- Pure correlation exposure

**Advantages:**

- No gamma, vega, theta noise
- No rebalancing needed
- Clean P&L

**Disadvantages:**

- OTC only (not exchange-traded)
- Less liquid
- Counterparty risk
- Requires institutional access

### Variance Dispersion

**Structure:**

- Trade variance (volatility squared) instead of volatility
- More mathematically clean
- Better replication properties

**Still requires options but conceptually cleaner**

---

## Real-World Applications

### Hedge Funds

**Strategy:**

- Dedicated volatility arbitrage funds
- Run long dispersion as core position
- Harvest dispersion premium
- Systematic strategies

### Market Makers

**Strategy:**

- Manage correlation risk from customer trades
- Client buys index options → creates short correlation risk
- Hedge with dispersion trades

### Risk Parity Funds

**Strategy:**

- Need to understand correlation
- Dispersion trades help manage correlation risk
- Portfolio diversification

### Proprietary Trading

**Strategy:**

- Tactical trades around events
- Exploit correlation dislocations
- Mean reversion strategies

---

## What to Remember

### Core Concepts

- **Dispersion trading bets on CORRELATION, not volatility level**
- Index vol = f(individual vols, correlation)
- When correlation ↓ → index vol ↓ relative to individual vols
- You trade this relationship

### The Fundamental Trade

**Long Dispersion (most common):**

- Short index options + Long individual options
- Profit when correlation < implied (stocks move independently)
- Structural edge (dispersion premium)

**Short Dispersion:**

- Long index options + Short individual options  
- Profit when correlation > implied (stocks move together)
- Counter-trend trade

### Key Formula

$$
\sigma_{\text{index}}^2 = \sum w_i^2 \sigma_i^2 + \text{correlation terms}
$$

**Index volatility always ≤ weighted average of individual volatilities (except if correlation = 1)**

### Comparison to Other Strategies

| Strategy | Trades |
|----------|--------|
| Gamma Scalping | Single-asset realized vol |
| Vega Trading | Single-asset implied vol |
| Dispersion | Multi-asset correlation |

**All use delta hedging, different exposures!**

### Success Factors

1. **Be right about correlation direction**
   - Long dispersion: correlation will decrease
   - Short dispersion: correlation will increase

2. **Entry timing matters**
   - Enter when correlation is extreme (high for long, low for short)
   - Mean reversion is your friend

3. **Manage complexity**
   - Operational excellence crucial
   - Systems and processes matter
   - Transaction costs kill

4. **The dispersion premium exists**
   - Implied correlation > realized correlation historically
   - Long dispersion has positive expected return
   - Similar to volatility risk premium

### Practical Wisdom

- **Correlation spikes in crises** (flights to 0.9+)
- **Correlation mean-reverts** (but slowly)
- **Transaction costs are significant** (need scale)
- **Timing is everything** (entering at extremes)
- **"All correlations go to 1 in a crisis"** (tail risk for long dispersion)

### The Deep Insight

**Dispersion trading is about DIVERSIFICATION:**

- When correlation is low → diversification works → index vol low
- When correlation is high → diversification fails → index vol high
- You're betting on whether diversification will work or fail
- **You're trading the value of diversification itself!**

### Final Thought

**Hierarchy of volatility strategies:**

1. **Delta hedging** → Trade nothing (risk management)
2. **Gamma scalping** → Trade single-asset realized vol
3. **Vega trading** → Trade single-asset implied vol
4. **Dispersion trading** → Trade multi-asset correlation

Each level adds complexity but provides new profit opportunities. Dispersion trading is the most sophisticated because you're trading **relationships between assets**, not individual assets themselves.

This is "meta-trading" at its finest—you're betting on the structure of the market, not on individual securities!
