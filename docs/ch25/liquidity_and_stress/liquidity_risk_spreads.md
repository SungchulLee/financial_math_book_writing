# Liquidity Risk and Spreads


**Liquidity risk and spreads** measure the cost and uncertainty of converting positions to cash, with bid-ask spreads widening during stress as market makers withdraw capacity, creating significant trading costs and potential forced liquidations.

---

## The Core Insight


**The fundamental idea:**

- Liquidity = Ability to trade without moving price
- Bid-ask spread = Cost of round-trip trade
- Spreads widen during stress (dealer constraints)
- Illiquidity compounds in crises
- Large positions = Large price impact
- Forced selling = Worst prices

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/liquidity_spreads.png?raw=true" alt="liquidity_spreads" width="700">
</p>
**Figure 1:** Time series of bid-ask spreads across asset classes showing dramatic widening during 2008 and 2020 crises, with corporate bond spreads spiking 10-20× normal levels as dealer balance sheets constrained and market liquidity evaporated.

**You're essentially asking: "How do I measure and manage the risk that I can't sell when I need to, or can only sell at terrible prices?"**

---

## What Is Liquidity?


### 1. Basic Definition


**Liquidity dimensions:**

**Tightness:**
- Bid-ask spread
- Cost of immediate execution
- Narrow spread = High liquidity

**Depth:**
- Size available at bid/ask
- Large size without moving price
- Deep market = High liquidity

**Resiliency:**
- Speed of recovery after trade
- How fast price returns to equilibrium
- Fast recovery = High liquidity

**Immediacy:**
- Time to execute
- Trade now vs. wait
- Instant execution = High liquidity

### 2. Bid-Ask Spread


**The basic measure:**

$$
\text{Spread} = \text{Ask Price} - \text{Bid Price}
$$

**Relative spread:**

$$
\text{Spread \%} = \frac{\text{Ask} - \text{Bid}}{\text{Mid Price}} \times 100\%
$$

**Example:**
- Bid: 99.75
- Ask: 100.25
- Mid: 100.00
- Spread: 0.50
- **Spread %: 0.5%**

**Round-trip cost:**
- Buy at ask (100.25), sell at bid (99.75)
- **Cost: 0.50 (50 bps of notional)**

### 3. Market Impact


**Price movement from large trades:**

**Kyle's Lambda:**

$$
\text{Price Impact} = \lambda \times \text{Order Size}
$$

Where $\lambda$ = Market impact coefficient

**Example:**
- $\lambda = 0.0001$ (10 bps per $\$1M traded)
- Order size: $\$10M$
- **Impact: 0.001 × 10 = 1% (100 bps)**

**Square-root law (empirical):**

$$
\text{Impact} \approx \sigma \times \sqrt{\frac{\text{Order Size}}{\text{Daily Volume}}}
$$

### 4. Liquidity by Asset Class


**Typical bid-ask spreads (normal markets):**

**US Treasuries:**
- On-the-run: 0.5-1 bp (0.005-0.01%)
- Off-the-run: 2-5 bps (0.02-0.05%)
- Very liquid

**Investment-grade corporates:**
- New issues: 10-20 bps (0.10-0.20%)
- Seasoned: 20-50 bps (0.20-0.50%)
- Moderate liquidity

**High-yield bonds:**
- Liquid names: 50-100 bps (0.50-1.00%)
- Less liquid: 100-300 bps (1-3%)
- Low liquidity

**Equities:**
- Large-cap: 1-5 bps (0.01-0.05%)
- Mid-cap: 10-30 bps (0.10-0.30%)
- Small-cap: 50-200 bps (0.50-2%)

**Emerging markets:**
- Sovereigns: 20-100 bps (0.20-1%)
- Corporates: 50-200 bps (0.50-2%)
- Very illiquid

### 5. Dealer Inventory Model


**Market makers quote bid-ask:**

**Spread components:**

$$
\text{Spread} = \text{Order Processing Cost} + \text{Inventory Cost} + \text{Adverse Selection Cost}
$$

**Order processing cost:**
- Fixed costs (operations, systems)
- Typical: 2-5 bps

**Inventory cost:**
- Risk of holding position
- Capital charges (Basel III)
- Typical: 5-20 bps

**Adverse selection cost:**
- Trading against informed counterparties
- Risk of getting picked off
- Typical: 5-15 bps

### 6. Liquidity Premium


**Yield compensation for illiquidity:**

$$
\text{Yield}_{\text{illiquid}} = \text{Yield}_{\text{liquid}} + \text{Liquidity Premium}
$$

**Example:**
- Liquid corporate: 4.0% yield
- Similar illiquid corporate: 4.5% yield
- **Liquidity premium: 50 bps**

**Empirical estimates:**
- IG corporates: 20-40 bps
- HY corporates: 50-100 bps
- Emerging markets: 100-200 bps

### 7. Liquidity Indicators


**Market-wide measures:**

**VIX:**
- Volatility index
- High VIX → Low liquidity
- VIX > 30 = Stress

**Bid-ask spread index:**
- Average spread across bonds
- Widening = Deteriorating liquidity

**Trading volume:**
- High volume = Good liquidity
- Falling volume = Warning sign

**Failed trades:**
- Settlement fails
- High fails = Liquidity stress

**Repo spreads:**
- GC spread over SOFR
- Widening = Funding stress

---

## Liquidity Risk Measurement


### 1. Liquidation Horizon


**Time to unwind position:**

$$
\text{Liquidation Time} = \frac{\text{Position Size}}{\text{Daily Trading Capacity}}
$$

**Example:**
- Position: $\$50M$ corporate bond
- Normal daily volume: $\$5M$
- **Liquidation time: 10 days**

**In stress:**
- Volume drops 50%
- Liquidation time doubles to 20 days!

### 2. Liquidity-Adjusted VaR


**Incorporate liquidation costs:**

$$
\text{LVaR} = \text{VaR} + \text{Liquidation Cost}
$$

**Liquidation cost:**

$$
\text{Cost} = \frac{\text{Spread}}{2} \times \text{Position} + \text{Market Impact}
$$

**Example:**
- VaR (10-day, 99%): $\$1M$
- Spread: 50 bps (0.5%)
- Position: $\$20M$
- Spread cost: 0.25% × $\$20M$ = $\$50,000$
- Market impact: $\$30,000$ (estimated)
- **LVaR: $\$1M$ + $\$50k$ + $\$30k$ = $\$1.08M$**

### 3. Bid-Ask Bounce


**Volatility from spread:**

Roll's estimator:

$$
\text{Spread} = 2\sqrt{-\text{Cov}(\Delta P_t, \Delta P_{t-1})}
$$

**Serial correlation in prices:**
- Bid-ask bounce creates negative autocorrelation
- Larger spread → More bounce
- Inflates measured volatility

### 4. Amihud Illiquidity Measure


**Price impact per dollar traded:**

$$
\text{ILLIQ} = \frac{1}{N}\sum_{t=1}^N \frac{|r_t|}{\text{Volume}_t}
$$

Where:
- $r_t$ = Return on day $t$
- $\text{Volume}_t$ = Dollar volume traded

**Higher ILLIQ = Less liquid**

### 5. Turnover Ratio


**Trading frequency:**

$$
\text{Turnover} = \frac{\text{Trading Volume}}{\text{Market Cap}}
$$

**Example:**
- Market cap: $\$1B$
- Daily volume: $\$10M$
- **Daily turnover: 1%**

**High turnover = More liquid**

### 6. Liquidity Beta


**Sensitivity to market liquidity:**

$$
r_i - r_f = \alpha + \beta_{\text{market}}(r_m - r_f) + \beta_{\text{liquidity}}\Delta \text{Liquidity} + \epsilon
$$

**Liquidity beta > 0:**
- Asset becomes more illiquid when market does
- Higher risk

### 7. Funding Liquidity Risk


**Ability to finance positions:**

$$
\text{Funding Gap} = \text{Repo Financing Need} - \text{Available Repo Capacity}
$$

**Stress scenario:**
- Normal capacity: $\$100M$
- Stress capacity: $\$20M$ (banks reduce)
- Position: $\$80M$
- **Funding gap: $\$60M$ (forced liquidation!)**

---

## Liquidity in Normal Markets


### 1. Treasury Market


**Most liquid asset:**

**On-the-run 10Y:**
- Bid-ask: 0.5-1 bp (0.005-0.01%)
- Daily volume: $\$30-50B$
- Depth: $\$100M+ at best bid/ask
- Liquidation: Instant (any size)

**Off-the-run:**
- Bid-ask: 2-5 bps (0.02-0.05%)
- Daily volume: $\$100M-1B$
- Depth: $\$10-20M$ at best bid/ask
- Liquidation: Minutes to hours

### 2. Corporate Bonds


**Less liquid than Treasuries:**

**Investment-grade:**
- Bid-ask: 10-50 bps (0.10-0.50%)
- Daily volume: $\$1-10M$ per bond
- Depth: $\$1-5M$ at best price
- Liquidation: Hours to days

**High-yield:**
- Bid-ask: 50-300 bps (0.50-3%)
- Daily volume: $\$0.5-5M$ per bond
- Depth: $\$0.5-2M$
- Liquidation: Days to weeks

### 3. Equities


**Varies by market cap:**

**Large-cap (S&P 100):**
- Bid-ask: 1-5 bps (0.01-0.05%)
- Daily volume: $\$100M-1B$
- Depth: $\$5-20M$
- Liquidation: Seconds to minutes

**Small-cap:**
- Bid-ask: 50-200 bps (0.50-2%)
- Daily volume: $\$1-10M$
- Depth: $\$100K-500K$
- Liquidation: Hours to days

### 4. Derivatives


**Exchange-traded vs OTC:**

**Listed futures/options:**
- Bid-ask: 1-5 ticks
- High volume (thousands/day)
- Central clearing
- Very liquid

**OTC derivatives:**
- Bid-ask: 5-50 bps of notional
- Bespoke terms
- Dealer intermediation
- Less liquid

### 5. Cost of Trading


**Round-trip transaction costs:**

**Treasuries:** 1-10 bps
**IG corporates:** 20-100 bps
**HY corporates:** 100-500 bps
**Equities (large):** 5-20 bps
**Equities (small):** 100-400 bps
**EM bonds:** 100-500 bps

**Annual impact (for active strategy):**
- 10 round-trips per year
- Average spread: 50 bps
- **Annual cost: 5% (huge drag!)**

---

## Liquidity in Stress


### 1. Crisis Dynamics


**Normal → Stress transition:**

**Phase 1: Warning signs**
- Spreads widen 50%
- Volume drops 20%
- Dealers reduce inventory

**Phase 2: Deterioration**
- Spreads widen 200%
- Volume drops 50%
- Dealers pull back significantly

**Phase 3: Crisis**
- Spreads widen 500-1,000%
- Volume collapses 70-80%
- Dealers disappear (balance sheet constraints)

**Phase 4: Seizure**
- No bid (infinite spread)
- No volume (market frozen)
- Only distressed sales possible

### 2. Spread Widening Examples


**Corporate bonds (2008 crisis):**

**Normal (2007):**
- IG spread: 10-20 bps
- HY spread: 50-100 bps

**Crisis (Oct 2008):**
- IG spread: 100-300 bps (10-15× wider!)
- HY spread: 500-2,000 bps (10-20× wider!)

**COVID (March 2020):**
- IG spread: 50-150 bps (3-5× wider)
- HY spread: 300-800 bps (5-10× wider)

### 3. Liquidation Cascade


**Forced selling creates spiral:**

$$
\text{Price Fall} \to \text{Margin Calls} \to \text{Forced Sales} \to \text{More Price Falls}
$$

**Example:**
- Hedge fund: $\$1B$ portfolio, 50% levered
- Market falls 10%
- Portfolio: $\$1B$ → $\$900M$
- Equity: $\$500M$ → $\$400M$ (down 20%)
- Margin call: Need to deleverage
- Sell $\$200M$ in illiquid market
- **Price impact: Additional 5-10% loss**

### 4. Commonality in Liquidity


**All assets become illiquid together:**

Correlations in stress:
- Normal: Correlations 0.3-0.5
- Crisis: Correlations 0.8-0.9

**Diversification fails:**
- Can't sell bonds to fund equity margin calls
- Everything illiquid simultaneously

### 5. Flight to Quality


**Liquidity concentration:**

**Into:**
- US Treasuries (especially OTR)
- Cash
- Gold

**Out of:**
- Corporates
- Equities
- Emerging markets
- Alternative investments

**Result:**
- Treasury spreads tighten (sometimes)
- Everything else spreads blow out

### 6. Dealer Balance Sheet


**Post-2008 constraints binding:**

**Normal capacity:**
- Total dealer balance sheet: $\$3T$
- Corporate bond inventory: $\$100B$
- Can intermediate $\$50B$ daily

**Crisis capacity:**
- Leverage ratio binding (5% SLR)
- Reduce risk assets
- Corporate bond inventory: $\$30B$ (down 70%!)
- Can intermediate $\$10B$ daily (down 80%!)

**Result: Market-making evaporates**

### 7. Redemption Pressure


**Mutual fund/ETF outflows:**

**Scenario:**
- Bond fund: $\$10B$ AUM
- Crisis: 20% redemptions ($\$2B$)
- Must sell bonds to meet redemptions
- But: Illiquid market, spreads wide
- Sell at poor prices
- Remaining investors hurt (first-mover advantage)

**Gates and suspensions:**
- Fund suspends redemptions
- Investors trapped
- Panic intensifies

---

## Common Mistakes


**Pitfalls to avoid:**

### 1. Assuming Constant Liquidity


**Mistake:** Use normal-market spreads in risk models

**Why it fails:** Liquidity disappears in stress

**Example:**
- Model VaR using 20 bp spread
- Crisis: Spread widens to 200 bps
- Actual liquidation cost 10× higher
- **Portfolio loss exceeds VaR by wide margin**

**Fix:** Stress-test liquidity (10× spread widening)

### 2. Ignoring Market Impact


**Mistake:** Think can sell large position at mid-price

**Why it fails:** Price moves against you

**Example:**
- Own $\$50M$ illiquid bond
- Mid-price: 100
- Daily volume: $\$5M$
- Try to sell all at once
- Market impact: -5% (move to 95)
- **Loss: $\$2.5M$ from impact alone**

**Fix:** Model impact using $\sqrt{\text{size}/\text{volume}}$

### 3. Crowded Trades


**Mistake:** Popular illiquid trade

**Why it fails:** Can't all exit together

**Example:**
- Emerging market local currency bonds
- 50 hedge funds own same bond
- Crisis hits, all try to sell
- No buyers
- **Price collapses 30-40%**

**Fix:** Avoid crowded illiquid positions

### 4. Mismatched Liquidity


**Mistake:** Liquid liabilities, illiquid assets

**Why it fails:** Can't meet redemptions

**Example:**
- Open-end fund with daily redemptions
- Invests in illiquid HY bonds (2-3 day settlement)
- Mass redemptions
- Can't sell fast enough
- **Fund gates or suspends**

**Fix:** Match liquidity of assets and liabilities

### 5. Neglecting Funding Liquidity


**Mistake:** Assume repo always available

**Why it fails:** Funding dries up in stress

**Example:**
- Levered $\$100M$ position via overnight repo
- Crisis: Dealers reduce repo capacity
- Can't roll overnight repo
- **Forced to sell at distressed prices**

**Fix:** Use term repo, diversify funding sources

### 6. Underestimating Liquidation Time


**Mistake:** Think can exit in 1 day

**Why it fails:** Need many days in stress

**Example:**
- $\$20M$ small-cap stock position
- Normal volume: $\$2M$/day
- Think: 10 days to liquidate

**In stress:**
- Volume drops 70% → $\$600K$/day
- **Liquidation time: 33 days!**

**Fix:** Use stress volume (30% of normal)

### 7. Ignoring Quarter-End Effects


**Mistake:** Don't adjust for reporting dates

**Why it fails:** Liquidity worse at quarter-ends

**Example:**
- Plan to sell $\$50M$ position on Dec 28
- Dealers reducing balance sheets
- Spreads 3× wider
- **Extra cost: $\$500K$-1M**

**Fix:** Trade mid-quarter, avoid reporting dates

### 8. Over-Diversification


**Mistake:** Spread across too many illiquid securities

**Why it fails:** Harder to sell piecemeal

**Example:**
- 200 small corporate bond positions ($\$500K$ each)
- Need to raise $\$20M$
- Try to sell 40 bonds
- Each trade costs 100 bps (small size)
- **Total cost: $\$200K$ (40 × 0.01 × $\$500K$)**

**vs. Concentrated:**
- 20 positions ($\$5M$ each)
- Sell 4 bonds
- Each trade costs 50 bps (larger size, better price)
- **Total cost: $\$100K$ (4 × 0.005 × $\$5M$)**

**Fix:** Balance diversification vs. liquidity

---

## Risk Management Rules


### 1. Liquidity Buffers


**Maintain cash reserves:**

$$
\text{Cash Buffer} \geq \max\left(10\% \times \text{AUM}, \, 2\times \text{Largest Daily Redemption}\right)
$$

**Example:**
- AUM: $\$100M$
- Largest redemption: $\$8M$
- **Required buffer: max($\$10M$, $\$16M$) = $\$16M$**

### 2. Position Limits


**Cap by liquidation horizon:**

$$
\text{Max Position} = \text{Stress Daily Volume} \times \text{Max Liquidation Days}
$$

**Example:**
- Stress volume: $\$1M$/day (30% of normal)
- Max liquidation: 10 days
- **Max position: $\$10M$**

### 3. Liquidity Classification


**Bucket all holdings:**

**Tier 1 (High liquidity):**
- Treasuries, large-cap equities
- Can sell in 1 day
- Max concentration: 50% of portfolio

**Tier 2 (Medium liquidity):**
- IG corporates, mid-cap equities
- Can sell in 1 week
- Max concentration: 30% of portfolio

**Tier 3 (Low liquidity):**
- HY bonds, small-cap, EM
- Can sell in 1 month
- Max concentration: 20% of portfolio

### 4. Stress Testing


**Monthly liquidity stress test:**

- Widen spreads 5-10×
- Reduce volumes 70%
- Compute liquidation time
- Compute total cost

**Action triggers:**
- If liquidation > 30 days → Reduce position
- If cost > 5% → Increase cash buffer

### 5. Redemption Policies


**For funds:**

**Gates:**
- Limit redemptions to 10% per month during stress
- Activate when spreads > 2× normal

**Swing pricing:**
- Redeeming investors bear liquidation costs
- Protects remaining investors

**Notice periods:**
- Require 30-90 day notice for large redemptions
- Allows orderly liquidation

### 6. Funding Diversification


**Multiple repo counterparties:**

- Minimum 5 dealers
- No single dealer > 30% of funding
- Mix term and overnight repo

**Alternative funding:**
- Credit lines (backup)
- Securities lending
- Reduce leverage before stress

### 7. Monitoring Dashboard


**Daily tracking:**

- Bid-ask spreads (by holding)
- Average spread (portfolio-wide)
- Trading volumes
- Failed trades
- Repo spreads
- VIX level

**Alert triggers:**
- Spreads > 2× normal
- Volume < 50% normal
- VIX > 30
- Repo spread > 50 bps over SOFR

---

## Real-World Examples


### 1. Lehman Collapse (Sept 2008)


**Setup:**
- Pre-crisis: IG corporate spreads 15 bps
- Market functioning normally

**Crisis (week of Sept 15):**
- Lehman bankruptcy announced
- IG spreads → 200 bps (13× wider!)
- HY spreads → 2,000 bps (20× wider!)
- **Many bonds no bid (infinite spread)**

**Impact:**
- Forced liquidations
- Fire sales
- Price declines 20-30% (not fundamental, just liquidity)

**Lesson:** Liquidity can evaporate overnight

### 2. Flash Crash (May 2010)


**Setup:**
- Normal trading day
- Large sell algorithm triggered

**Event (2:45 PM, 20 minutes):**
- Dow fell 1,000 points (-9%)
- Many stocks traded at $0.01
- Spreads widened 100-1,000×
- ETFs disconnected from NAV

**Outcome:**
- Trades reversed (clearly erroneous)
- But: Demonstrated fragility
- Stop-losses hit, margin calls triggered

**Lesson:** Algorithms can cause liquidity spirals

### 3. COVID Dash for Cash (March 2020)


**Setup:**
- Pandemic panic
- Everyone selling everything for cash

**Event:**
- Even Treasuries sold (usually safe haven)
- OTR 10Y spread: 1 bp → 5 bps (5× wider)
- IG corporate spread: 20 bps → 150 bps (7.5× wider)
- HY spread: 100 bps → 800 bps (8× wider)

**Cause:**
- Dealer balance sheets full (SLR constraint)
- Couldn't intermediate
- Fed intervened ($\$750B$ purchases)

**Lesson:** Regulatory constraints impair liquidity

### 4. Woodford Fund Suspension (2019)


**Setup:**
- UK equity income fund
- $\$4B$ AUM
- Held illiquid small-cap and unquoted stocks

**Event:**
- Large redemption request
- Tried to sell illiquid holdings
- Realized couldn't meet redemptions
- **Suspended fund (investors trapped)**

**Outcome:**
- Fund eventually wound down
- Investors lost 20-30%
- First-movers escaped, last-movers hurt

**Lesson:** Asset-liability mismatch fatal

### 5. GameStop Squeeze (Jan 2021)


**Setup:**
- Heavy short interest (>100% of float)
- Retail buying frenzy

**Event:**
- Price surged $20 → $480$
- Bid-ask spread: 1% → 20% (intraday)
- Market makers overwhelmed
- Settlement system strained

**Outcome:**
- Brokers restricted trading
- Forced liquidations of shorts
- Extreme illiquidity during spike

**Lesson:** Crowded shorts + buying frenzy = Liquidity disaster

---

## Practical Steps


### 1. Measuring Current Liquidity


**Build liquidity dashboard:**

```python
import pandas as pd

# For each holding
for holding in portfolio:
    # Calculate metrics
    spread = (ask - bid) / mid
    daily_volume = get_volume(holding)
    turnover = daily_volume / market_cap
    liquidation_days = position_size / (daily_volume * 0.3)  # Stress
    
    # Store
    liquidity_data[holding] = {
        'spread': spread,
        'volume': daily_volume,
        'liquidation_days': liquidation_days,
        'tier': classify_liquidity(liquidation_days)
    }

# Portfolio aggregates
avg_spread = weighted_average(spread, weights)
avg_liquidation = weighted_average(liquidation_days, weights)
```

### 2. Liquidity Stress Test


**Monthly scenario analysis:**

1. **Baseline scenario:**
   - Current spreads and volumes
   - Liquidation time: 5 days
   - Cost: $\$100K$

2. **Stress scenario:**
   - Spreads 5× wider
   - Volumes 70% lower
   - Liquidation time: 25 days
   - Cost: $\$750K$

3. **Severe stress:**
   - Spreads 10× wider
   - Volumes 90% lower
   - Liquidation time: 60 days
   - Cost: $\$1.5M$

4. **Action plan:**
   - If stress cost > 3% of AUM → Reduce illiquid holdings
   - If liquidation > 30 days → Increase cash buffer

### 3. Position Sizing


**Liquidity-adjusted position limits:**

$$
\text{Max Position} = \min\left(\text{Risk Limit}, \, \text{Liquidity Limit}\right)
$$

**Example:**
- Risk limit: $\$20M$ (from VaR)
- Stress daily volume: $\$2M$
- Max liquidation: 10 days
- Liquidity limit: $\$2M$ × 10 = $\$20M$
- **Max position: $\$20M$ (both limits binding)**

### 4. Portfolio Construction


**Liquidity-aware optimization:**

```python
# Objective: Maximize return
# Subject to:
# - Tier 1 (high liq) ≥ 40%
# - Tier 2 (med liq) ≤ 40%
# - Tier 3 (low liq) ≤ 20%
# - Average liquidation days ≤ 10
# - Maximum spread cost ≤ 2%

def optimize_portfolio(holdings, returns, constraints):
    # Add liquidity constraints
    constraints += [
        sum(tier1_weights) >= 0.40,
        sum(tier2_weights) <= 0.40,
        sum(tier3_weights) <= 0.20,
        weighted_avg_liquidation <= 10,
        weighted_spread_cost <= 0.02
    ]
    
    # Solve
    optimal_weights = solver.solve(returns, constraints)
    return optimal_weights
```

### 5. Redemption Management


**For fund managers:**

1. **Set redemption limits:**
   - Daily: 2% of AUM
   - Monthly: 10% of AUM
   - Quarterly: 25% of AUM

2. **Implement swing pricing:**
   - Calculate liquidation cost
   - Adjust NAV for redeeming investors
   - Protects remaining investors

3. **Notice requirements:**
   - $0-1M$: No notice
   - $1-10M$: 7 days notice
   - $10M+$: 30 days notice

### 6. Crisis Playbook


**Predetermined actions:**

**Warning signs (any 2 of):**
- Spreads > 2× normal
- Volume < 50% normal
- VIX > 30
- Failed trades spike

**Actions:**
- Increase cash to 15%
- Reduce leverage by 25%
- Cancel new position initiatives

**Crisis (any 3 of 5):**
- Spreads > 5× normal
- Volume < 30% normal  
- VIX > 40
- Repo spread > 100 bps over SOFR
- Multiple dealer calls (reducing capacity)

**Actions:**
- Increase cash to 30%
- Reduce leverage by 50%
- Sell Tier 3 holdings (before complete illiquidity)
- Activate fund gates (if available)

---

## Final Wisdom


> "Liquidity is the oxygen of markets - invisible when plentiful but lethal when absent. The fundamental mistake is assuming you can exit positions at will; in reality, liquidity is time-varying, mean-reverting, and prone to disappearing exactly when you need it most. During the 2008 crisis, investment-grade corporate bond spreads widened 10-15× normal levels, not because of credit deterioration but pure illiquidity as dealer balance sheets constrained. The key lessons: (1) measure liquidity in stress not normal times (assume spreads widen 5-10×, volumes fall 70%), (2) maintain cash buffers for redemptions and margin calls, (3) avoid crowded illiquid trades where everyone owns the same thing, and (4) diversify funding sources so you're not forced to sell at the worst moment. Remember: In a crisis, the only thing more painful than selling at bad prices is not being able to sell at all."

**Key to success:**

- **Measure constantly:** Track bid-ask spreads, volumes, liquidation times daily (not just when selling)
- **Stress test liquidity:** Model 5-10× spread widening, 70% volume decline, compute portfolio liquidation time
- **Size positions conservatively:** Max position = 10 days of stress volume, never exceed liquidity capacity
- **Maintain buffers:** Cash ≥ 10% of portfolio, can handle largest expected redemption without forced sales
- **Diversify funding:** 5+ repo counterparties, mix term and overnight, secure capacity before needing it
- **Avoid crowded trades:** Popular illiquid positions are disasters waiting to happen (everyone can't exit together)
- **Plan for stress:** Predetermined actions when spreads double, VIX spikes, volumes collapse
- **Remember:** Price you see ≠ price you get (especially for large positions in illiquid markets)

---

## Related Topics


**Cross-references to other Chapter 25 sections:**

- **Balance Sheet Constraints (25.1.2):** Why dealer intermediation capacity is limited; SLR impact on liquidity provision
- **Crisis Basis Dynamics (25.3.2):** How illiquidity cascades through basis relationships; correlation breakdown
- **Haircuts, Margin, and Funding Costs (25.4.1):** Stress haircuts increase when liquidity evaporates
- **Risk Controls for Leverage (25.4.2):** Liquidity-adjusted position limits; drawdown management
- **Repo and Securities Lending (25.1.1):** Funding liquidity as driver of market liquidity
