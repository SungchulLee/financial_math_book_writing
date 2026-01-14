# Cross Rates and Triangular Arbitrage


**Cross rates and triangular arbitrage** exploit temporary pricing discrepancies across three currency pairs,
capturing risk-free profits when the implied cross rate deviates from the quoted market rate through rapid, automated execution.

---

## The Core Insight


**The fundamental idea:**

- Three currencies create relationships
- Cross rates must be internally consistent
- Pricing inefficiencies arise briefly
- Arbitrage restores equilibrium instantly
- Technology enables microsecond execution
- Risk-free profit if fast enough

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/triangular_arbitrage.png?raw=true" alt="triangular_arbitrage" width="700">
</p>
**Figure 1:** Triangular arbitrage mechanism showing the three-leg trade path (USD → EUR → GBP → USD) 
with pricing discrepancies creating a closed loop with positive net profit when executed simultaneously across all three pairs.

**You're essentially betting: "I can identify and execute on cross-rate inconsistencies faster than the market corrects them."**

---

## Theoretical Foundation


### 1. Cross Rate Definition


**The fundamental relationship:**

**Direct cross rate:**

$$
\text{EUR/GBP} = \frac{\text{EUR/USD}}{\text{GBP/USD}}
$$

**Example:**

- EUR/USD = 1.0800
- GBP/USD = 1.2700
- Implied EUR/GBP = 1.0800 / 1.2700 = **0.8504**

**If market quotes EUR/GBP = 0.8520:**

- Discrepancy: 0.8520 - 0.8504 = **0.0016 (16 pips)**
- Arbitrage opportunity exists!

### 2. No-Arbitrage Condition


**Triangular consistency:**

$$
S_{A/B} \times S_{B/C} \times S_{C/A} = 1
$$

Where:
- $S_{A/B}$ = Exchange rate of currency A per unit of B
- Must form closed loop (return to starting currency)
- Any deviation = arbitrage opportunity

**Proof by example:**

$$
\frac{\text{USD}}{\text{EUR}} \times \frac{\text{EUR}}{\text{GBP}} \times \frac{\text{GBP}}{\text{USD}} = 1
$$

**Numerical check:**

- USD/EUR = 0.9259 (1/1.08)
- EUR/GBP = 0.8504
- GBP/USD = 1.2700

$$
0.9259 \times 0.8504 \times 1.2700 = 1.0000 \,\checkmark
$$

**If product ≠ 1, arbitrage exists!**

### 3. Arbitrage Profit Formula


**Expected profit:**

$$
\text{Profit \%} = \left| 1 - (S_1 \times S_2 \times S_3) \right| - \text{Transaction Costs}
$$

**Breakeven condition:**

$$
\text{Discrepancy} > \text{Bid-Ask Spread}_1 + \text{Bid-Ask Spread}_2 + \text{Bid-Ask Spread}_3
$$

**Example:**

- Product of rates: 1.0008 (should be 1.0000)
- Discrepancy: 0.08% = 8 bps
- Transaction costs: 2 + 2 + 2 = 6 bps
- **Net profit: 2 bps**

---

## Cross Rate Mechanics


**Understanding the relationships:**

### 1. Major Cross Rates


**Most liquid crosses:**

**EUR crosses:**

- EUR/GBP: Most traded cross (50% of cross volume)
- EUR/JPY: High liquidity
- EUR/CHF: European majors
- EUR/CAD: Commodity overlay

**JPY crosses:**

- GBP/JPY: "Beast" (high volatility)
- AUD/JPY: Carry trade favorite
- EUR/JPY: Safe haven dynamics
- CAD/JPY: Oil proxy

**Other major crosses:**

- AUD/NZD: Regional trade
- GBP/CAD: Commodity-developed
- EUR/AUD: Risk on/off

### 2. Implied vs. Quoted


**Two ways to obtain cross rate:**

**Method 1: Direct quote**

- Market maker quotes EUR/GBP directly
- Bid: 0.8500, Ask: 0.8504
- Spread: 4 pips
- Fastest execution (single trade)

**Method 2: Synthetic (implied)**

- Buy EUR/USD, Sell GBP/USD
- Two separate trades
- Spread: Sum of both spreads (wider)
- Slower execution (2 legs)

**Comparison:**

| Method | EUR/GBP | Spread | Speed | Use Case |
|--------|---------|--------|-------|----------|
| Direct | 0.8502 | 4 pips | Instant | Normal trading |
| Synthetic | 0.8504 | 6 pips | 2 steps | Arbitrage or illiquid |

**Arbitrage condition:** Direct price ≠ Synthetic price

### 3. Bid-Ask Considerations


**Real-world friction:**

**Bid-ask spreads by pair:**

| Pair | Typical Spread | Crisis Spread |
|------|----------------|---------------|
| EUR/USD | 0.1-0.5 pips | 2-5 pips |
| GBP/USD | 0.5-1.0 pips | 5-10 pips |
| USD/JPY | 0.1-0.5 pips | 3-8 pips |
| EUR/GBP | 1-2 pips | 10-20 pips |
| GBP/JPY | 2-5 pips | 20-50 pips |

**Total transaction cost (triangular):**

$$
\text{Total Cost} = \text{Spread}_1 + \text{Spread}_2 + \text{Spread}_3
$$

**Example (USD → EUR → GBP → USD):**

- EUR/USD: 0.5 pips
- EUR/GBP: 2 pips  
- GBP/USD: 1 pip
- **Total: 3.5 pips minimum profit needed**

---

## Triangular Arbitrage


**The core strategy:**

### 1. Identifying Opportunities


**Scanning algorithm:**

**Step 1: Calculate implied cross**

```python
implied_eur_gbp = eur_usd / gbp_usd
```

**Step 2: Compare to market quote**

```python
discrepancy = abs(market_eur_gbp - implied_eur_gbp)
```

**Step 3: Check profitability**

```python
if discrepancy > total_transaction_cost:
    execute_arbitrage()
```

**Real-time example:**

**Market data (time: 10:30:15.234):**

- EUR/USD: 1.0805 / 1.0807
- GBP/USD: 1.2698 / 1.2700
- EUR/GBP: 0.8510 / 0.8514

**Calculation:**

- Implied EUR/GBP (mid): 1.0806 / 1.2699 = 0.8508
- Market EUR/GBP (mid): 0.8512
- **Discrepancy: 4 pips**

**Transaction cost:**

- EUR/USD: 2 pips (bid-ask)
- GBP/USD: 2 pips
- EUR/GBP: 4 pips
- **Total: 8 pips**

**Conclusion: No arbitrage (discrepancy < cost)**

### 2. Execution Strategy


**Three-leg simultaneous trade:**

**Direction 1: USD → EUR → GBP → USD**

**Leg 1:** Buy EUR/USD at 1.0807

- Start: $1,000,000
- Get: €925,925

**Leg 2:** Sell EUR/GBP at 0.8510

- Have: €925,925
- Get: £788,062

**Leg 3:** Sell GBP/USD at 1.2698

- Have: £788,062
- Get: **$1,000,786**

**Profit: $786 (7.86 bps)**

**Direction 2: USD → GBP → EUR → USD**

**If discrepancy favors opposite direction:**

**Leg 1:** Buy GBP/USD at 1.2700

- Start: $1,000,000
- Get: £787,402

**Leg 2:** Buy EUR/GBP at 0.8514

- Have: £787,402
- Get: €924,682

**Leg 3:** Sell EUR/USD at 1.0805

- Have: €924,682
- Get: **$999,005**

**Loss: -$995 (must reverse direction!)**

**Key insight: Direction matters—calculate both paths, execute profitable one.**

### 3. Speed Requirements


**Time-sensitive execution:**

**Opportunity lifespan:**

- High-frequency: 1-50 milliseconds
- Retail: 100-500 milliseconds
- Manual: Impossible (too slow)

**Technology requirements:**

- Co-located servers (exchange proximity)
- Direct market access (DMA)
- Sub-millisecond order routing
- Automated position management
- Microsecond price feeds

**Latency breakdown:**

| Component | Time | Cumulative |
|-----------|------|------------|
| Price feed | 0.5 ms | 0.5 ms |
| Calculation | 0.1 ms | 0.6 ms |
| Decision | 0.1 ms | 0.7 ms |
| Order send | 0.5 ms | 1.2 ms |
| Exchange process | 0.3 ms | 1.5 ms |
| Fill confirmation | 0.5 ms | **2.0 ms total** |

**Competition:**

- HFT firms: < 1 ms
- Prop traders: 1-5 ms
- Retail: 50-500 ms (too slow)
- Manual: 1,000+ ms (impossible)

---

## Greeks and Sensitivities


**Understanding risk exposures:**

### 1. Price Delta (Δ)


**Instantaneous price movement:**

$$
\Delta_{\text{arbitrage}} = \frac{\partial \text{P&L}}{\partial S_i}
$$

**Ideally: Δ = 0 (delta-neutral)**

- All three legs executed simultaneously
- No directional exposure
- Pure arbitrage (risk-free)

**Reality: Δ ≠ 0 (execution risk)**

- Leg 1 filled, Leg 2 delayed
- Exposed to price change
- Can turn profit into loss
- **Most common failure mode**

**Example of execution risk:**

**Plan:**

1. Buy EUR/USD at 1.0807 (filled instantly)
2. Sell EUR/GBP at 0.8510 (delay 10ms)
3. Sell GBP/USD at 1.2698 (filled)

**Problem:** In 10ms, EUR/GBP moves to 0.8505

- Planned profit: $786
- Actual profit: $786 - $500 = **$286**
- **Execution risk reduced profit by 64%**

### 2. Gamma (Γ)


**Sensitivity to volatility:**

$$
\Gamma = \frac{\partial^2 \text{P&L}}{\partial S^2}
$$

**During normal conditions:**

- Γ ≈ 0 (flat arbitrage payoff)
- Volatility doesn't matter (if instant execution)

**During execution delay:**

- Γ becomes significant (convexity risk)
- High volatility → higher execution risk
- VIX > 25: Avoid triangular arbitrage
- Spreads widen, opportunities vanish

### 3. Liquidity Theta (θ_L)


**Time decay of opportunity:**

$$
\theta_L = \frac{\partial \text{Profit}}{\partial t}
$$

**Decay rate:**

- Opportunity half-life: 10-50 ms
- Every millisecond reduces expected profit
- Competition arbitrages away edge
- First mover wins

**Empirical observation:**

- t = 0 ms: 10 bps opportunity
- t = 10 ms: 6 bps remaining
- t = 20 ms: 3 bps remaining  
- t = 50 ms: Opportunity gone
- **Exponential decay**

### 4. Correlation (ρ)


**Price co-movement:**

**Ideal: ρ = 1 (perfect correlation)**

- Three pairs move together instantly
- No arbitrage possible
- Market efficient

**Reality: ρ < 1 (imperfect correlation)**

- Temporary divergence
- Creates opportunities
- Faster arbitrage → ρ closer to 1
- HFT made ρ = 0.9999+ (almost perfect)

---

## Implementation Details


**Practical execution framework:**

### 1. Technology Stack


**Essential components:**

**Infrastructure:**

- Co-located servers (< 1 ms to exchange)
- 10+ Gbps network connections
- FPGA-based order routing (microseconds)
- Redundant systems (no downtime)

**Software:**

- Real-time data feeds (direct from exchanges)
- C++ or Rust (low-latency languages)
- Custom execution algorithms
- Automated risk management

**Data sources:**

- EBS, Reuters D3, Currenex (institutional FX)
- Prime broker feeds
- ECN aggregators
- Tick-by-tick data (every price change)

**Capital requirements:**

- Technology: $500K-$5M setup
- Colocation: $10K-$50K monthly
- Data feeds: $50K-$200K monthly
- Minimum trading capital: $1M+

### 2. Opportunity Detection


**Real-time monitoring:**

**Algorithm:**

```python
for each (triplet in currency_triplets):
    # Get bid/ask prices
    eur_usd_bid, eur_usd_ask = get_price('EUR/USD')
    gbp_usd_bid, gbp_usd_ask = get_price('GBP/USD')
    eur_gbp_bid, eur_gbp_ask = get_price('EUR/GBP')
    
    # Calculate implied cross (Path 1)
    implied_eur_gbp = eur_usd_bid / gbp_usd_ask
    
    # Check arbitrage
    if implied_eur_gbp > eur_gbp_ask + total_cost:
        execute_arbitrage(path=1)
    
    # Calculate reverse (Path 2)
    implied_reverse = gbp_usd_bid / eur_usd_ask
    reverse_eur_gbp = 1 / implied_reverse
    
    if eur_gbp_bid > reverse_eur_gbp + total_cost:
        execute_arbitrage(path=2)
```

**Frequency:**

- Check every price update (1000+ per second)
- Sub-millisecond decision
- Automated execution (no human)

### 3. Order Execution


**Simultaneous order placement:**

**Optimal strategy:**

- Send all three orders simultaneously (single packet)
- Use limit orders at best bid/ask
- IOC (Immediate or Cancel) orders
- No partial fills (all or nothing)

**Risk controls:**

- Maximum position size: $10M per trade
- Maximum slippage: 1 pip per leg
- Abort if any leg fails
- Automatic unwind if incomplete

**Example order flow:**

```
Time 0.0 ms: Detect opportunity
Time 0.1 ms: Calculate optimal path
Time 0.2 ms: Generate three orders
Time 0.3 ms: Send orders (single packet)
Time 1.5 ms: All three fills confirmed
Time 1.6 ms: Realize profit
```

### 4. Position Management


**Handling partial fills:**

**Scenario 1: All legs filled**

- Perfect execution
- Realize profit immediately
- No residual position
- **Success**

**Scenario 2: One leg unfilled**

- Exposed to directional risk
- Immediately hedge (buy/sell opposite)
- Accept small loss from slippage
- **Risk management worked**

**Scenario 3: Two legs unfilled**

- Major execution failure
- Unwind filled leg
- Accept transaction cost loss
- **Better than holding directional risk**

### 5. Performance Monitoring


**Key metrics:**

**Success rate:**

- Percent of attempted arbitrages profitable
- Target: > 95%
- Below 90%: Technology upgrade needed

**Average profit per trade:**

- Typical: 0.5-2.0 bps
- Minimum: Must exceed transaction costs
- If < 0.5 bps: Not worth capital/technology cost

**Sharpe ratio:**

- Annual Sharpe: 5-15 (very high)
- Daily volatility: < 0.1% (very low)
- Risk-adjusted returns: Excellent

**Opportunity frequency:**

- HFT era: 10-50 per day per triplet
- Pre-HFT (2000s): 100-500 per day
- Manual trading era (1990s): Continuous opportunities

---

## When It Works Best


**Optimal market conditions:**

### 1. Market Stress


**Temporary dislocations:**

**During crises:**

- 2008 GFC: Spreads widened to 50+ pips
- 2020 COVID: Flash crashes created gaps
- 2016 Brexit: EUR/GBP vs. crosses diverged
- Central bank interventions: Sudden moves

**Why opportunities arise:**

- Liquidity fragmentation
- Market makers pull quotes
- Spreads blow out
- Information asymmetry increases
- Coordination breaks down

**Example (March 2020 COVID):**

- Normal: 3-5 arbitrage opportunities daily
- March 12-13: 200+ opportunities
- Profit per trade: 5-10 bps (vs. 1-2 bps normal)
- **Crisis = bonanza for arbitrage**

### 2. Low Competition


**Before HFT dominance:**

**Pre-2005:**

- Manual/semi-automated trading
- Opportunities lasted seconds
- Average profit: 5-10 bps
- Frequency: 50-100 daily

**2005-2010:**

- Early HFT adoption
- Opportunities lasted 100-500 ms
- Average profit: 2-5 bps
- Frequency: 20-50 daily

**Post-2010:**

- HFT dominated
- Opportunities last < 10 ms
- Average profit: 0.5-2 bps
- Frequency: 5-20 daily

**Current (2024):**

- Ultra-HFT with FPGAs
- Opportunities last < 1 ms
- Average profit: 0.2-1 bps
- Frequency: 2-10 daily
- **Only accessible to top-tier firms**

### 3. Fragmented Markets


**Multiple venues:**

**Regulatory arbitrage:**

- US vs. European exchanges
- Onshore vs. offshore rates (CNY vs. CNH)
- Retail vs. institutional pricing
- Different regulatory regimes

**Geographic arbitrage:**

- Tokyo vs. London vs. New York
- Time zone transitions (liquidity shifts)
- Regional holidays (thin liquidity)

---

## When It Fails


**Challenges and limitations:**

### 1. Technology Arms Race


**Speed competition:**

**Evolution:**

- 2000: Milliseconds sufficient
- 2010: Microseconds needed  
- 2020: Nanoseconds emerging
- Future: Quantum computing?

**Capital requirements escalate:**

- 2005: $100K technology setup
- 2015: $1M setup
- 2024: $5M+ setup
- Continuous upgrades required

**Result:**

- Only well-capitalized firms compete
- Retail/small firms squeezed out
- Profitability declining (more competition)
- **Market increasingly efficient**

### 2. Execution Risk


**The primary failure mode:**

**Partial fills:**

- Leg 1 filled, Legs 2-3 rejected
- Now have directional exposure
- Market moves against position
- Arbitrage becomes speculative loss

**Example of failure:**

**Attempt:**

- Buy EUR/USD at 1.0807 (filled)
- Sell EUR/GBP at 0.8510 (rejected - no liquidity)
- Left long EUR, short USD

**Market moves:**

- EUR/USD drops to 1.0795 in 5 seconds
- Loss: 12 pips × $1M = **-$1,200**
- Expected profit was only $786
- **Net: -$414 (failure)**

**Frequency:**

- 5-10% of attempts fail (good system)
- 20-30% fail (poor system/volatile markets)
- Must have robust risk controls

### 3. Market Efficiency


**Arbitrage erodes itself:**

**Feedback loop:**

- Arbitrage profits discovered
- More firms enter
- Competition increases
- Execution speed improves
- Discrepancies shrink
- Opportunities vanish
- **Profits approach zero**

**Evidence:**

- 1990s: 10+ bps average profit
- 2000s: 3-5 bps
- 2010s: 1-2 bps
- 2020s: 0.5-1 bps
- **Declining returns over time**

**Economic interpretation:**

- This is exactly what should happen
- Efficient markets theorem
- Arbitrage keeps prices aligned
- But profits disappear for arbitrageurs

---

## Common Mistakes


**Frequent errors to avoid:**

### 1. Ignoring Transaction Costs


**The mistake:**

- Identify 2 bps discrepancy
- Execute arbitrage
- Each leg: 1 pip spread
- Total cost: 3 pips (3 bps)
- **Net: -1 bps loss**

**Why it fails:**

- Bid-ask spread is real cost
- Can't trade at mid-price
- Must cross spread to execute
- Small discrepancies unprofitable

**Fix:**

- Always calculate total round-trip cost
- Minimum profit threshold = 1.5x costs
- Example: 6 bps cost → need 9 bps discrepancy
- Be conservative in estimates

### 2. Sequential Execution


**The mistake:**

- Identify arbitrage opportunity
- Execute Leg 1 (filled)
- Start Leg 2 (0.5 seconds later)
- Price moved, opportunity gone
- Execute Leg 3 anyway
- Now exposed to risk

**Why it fails:**

- Prices move in milliseconds
- Sequential = guaranteed execution risk
- No longer arbitrage (speculation)
- Can lose significantly

**Fix:**

- Simultaneous execution (same microsecond)
- Use smart order routers (SORs)
- All-or-nothing approach
- If any leg fails, abort all

### 3. Insufficient Speed


**The mistake:**

- Retail trader spots 5 bps opportunity
- Manually enters three orders
- Takes 3-5 seconds
- All orders filled but prices changed
- **Result: Loss instead of profit**

**Why it fails:**

- Human reaction time: 200+ ms
- Order entry: 1-2 seconds
- By then, HFT firms took opportunity
- You're trading at stale prices

**Fix:**

- Don't compete with HFT (you'll lose)
- Need sub-millisecond automation
- Or find different opportunities (EM, less liquid)
- Accept triangular arbitrage not viable for retail

### 4. Over-Leveraging


**The mistake:**

- "Arbitrage is risk-free!"
- Use 50x leverage
- Execution slips by 2 pips
- 2 pips × 50x = 100 pips equivalent loss
- **Account blown up**

**Why it fails:**

- Execution risk exists (partial fills)
- Technology failures happen
- Even "risk-free" has tail risk
- Leverage amplifies disasters

**Fix:**

- Max 5-10x leverage (institutional)
- 1-3x for conservative (retail, if attempting)
- Always have circuit breakers
- Risk < 1% of capital per trade

---

## Risk Management Rules


### 1. Position Limits


**Conservative sizing:**

$$
\text{Max Position} = \min\left(\frac{\text{Capital} \times 0.01}{\text{Avg Spread}}, \text{Daily Venue Limit}\right)
$$

**Example:**

- $10M capital
- 1% risk = $100K
- Avg spread: 5 pips = 0.05% = $500 per $1M
- Max position: $100K / $500 = **$200M notional**

**But venue limit:**

- EBS max clip size: $50M
- **Actual max: $50M** (smaller of two)

### 2. Execution Monitoring


**Real-time checks:**

**Pre-trade:**

- Verify all three quotes fresh (< 10 ms old)
- Check liquidity depth (enough size)
- Confirm network latency normal
- Calculate expected profit > threshold

**During trade:**

- Monitor fill confirmations (< 50 ms)
- Detect partial fills immediately
- Calculate realized P&L
- Abort if any red flag

**Post-trade:**

- Verify all legs filled
- Reconcile expected vs. actual profit
- Log execution quality metrics
- Feed into ML model for optimization

### 3. Circuit Breakers


**Automatic safeguards:**

**Stop trading when:**

- Spreads > 3x normal (liquidity crisis)
- Execution success rate < 90%
- VIX > 30 (market stress)
- Cumulative daily loss > -0.5%
- Technology latency > 2x baseline

**Resume when:**

- Conditions normalize for 30+ minutes
- Manual review and approval
- Risk limits reset

### 4. Diversification


**Spread across:**

**Currency triplets:**

- EUR/USD/GBP
- USD/JPY/AUD  
- EUR/CHF/GBP
- GBP/JPY/AUD
- 10-20 active triplets (monitor all)

**Venues:**

- EBS, Reuters, Currenex
- Multiple prime brokers
- Regional exchanges
- Reduces single-venue risk

**Time of day:**

- London session (highest liquidity)
- Overlap periods (London/NY)
- Avoid Asia-only (lower volume)

---

## Real-World Examples


### 1. Crisis Opportunity


**Setup:**

- September 2008: Lehman bankruptcy
- FX market dislocation
- Spreads exploded (10-50 pips)
- Liquidity fragmented

**Opportunity:**

- EUR/USD: 1.4200 / 1.4230 (30 pip spread!)
- GBP/USD: 1.7800 / 1.7840 (40 pip spread)
- EUR/GBP: 0.7950 / 0.8000 (50 pip spread!)

**Arbitrage:**

- Implied EUR/GBP: 1.4215 / 1.7820 = 0.7976
- Market EUR/GBP mid: 0.7975
- **Discrepancy: Minimal mid-to-mid BUT...**

**The real opportunity:**

- Could buy EUR/GBP at 0.8000 (ask)
- Synthetic cost: 1.4230 / 1.7800 = 0.7994
- **Save 6 pips by using synthetic!**

**Profit:**

- $10M position
- 6 pips = 0.06% × $10M = **$6,000 profit**
- Multiple opportunities per hour
- Daily profits: $50-100K

**Lesson:** Crises create massive arbitrage opportunities. But need capital + technology to capture.

### 2. Brexit Flash Crash (2016)


**Setup:**

- June 24, 2016: Brexit vote result
- GBP crashed 1.50 → 1.32 in minutes
- Electronic market fragmented
- Price feeds diverged

**Triangular breakdown:**

- EUR/GBP spiked 0.82 → 0.86 (cross rate)
- But EUR/USD and GBP/USD still adjusting
- Temporary 20-30 pip discrepancies

**Example arbitrage (8:15 AM BST):**

- GBP/USD on EBS: 1.3350
- EUR/USD on Reuters: 1.1200
- EUR/GBP should be: 0.8390
- Market quote: 0.8450
- **Discrepancy: 60 pips!**

**Execution:**

- Sell EUR/GBP at 0.8450
- Buy EUR/USD at 1.1200
- Sell GBP/USD at 1.3350
- **Profit: ~0.7% on round-trip**

**Challenge:**

- Venues kept flashing
- Orders getting rejected
- Manual intervention needed
- High stress, high reward

**Outcome for prepared firms:**

- Top HFT firms: $5-20M profits that day
- Slower firms: Losses (caught wrong direction)
- **Speed and technology separated winners from losers**

### 3. Swiss Franc Unpegging (2015)


**Setup:**

- January 15, 2015: SNB abandoned 1.20 floor
- EUR/CHF crashed 1.20 → 0.85 in minutes
- Fastest FX move in modern history
- Complete market breakdown

**What happened to arbitrage:**

- EUR/CHF direct quotes: None (no liquidity)
- USD/CHF, EUR/USD: Wildly divergent
- Triangular relationships broken completely
- Discrepancies: 200-500 pips (absurd)

**Example (9:30:05 AM):**

- EUR/USD: 1.1600 (unchanged initially)
- USD/CHF: 0.8500 (from 0.8300, up 200 pips)
- Implied EUR/CHF: 0.9860
- Market EUR/CHF (when quoted): 0.9500
- **Discrepancy: 360 pips!**

**But execution impossible:**

- No liquidity (no one willing to trade CHF)
- Orders rejected
- If filled, couldn't complete triangle
- **Theoretical arbitrage but practically impossible**

**Lesson:**

- Extreme events break arbitrage
- Liquidity vanishes exactly when needed
- Risk controls must abort trading
- Some markets are "un-arbitrageable" temporarily

### 4. Algorithmic Competition (2018)


**Setup:**

- Normal market conditions
- Top 5 HFT firms competing
- Average opportunity: 0.5-1.0 bps
- Speed differential: < 100 microseconds

**Daily patterns:**

- 10:00 AM: EUR/USD vs. EUR/GBP misalignment (0.8 bps)
- Firm A detects at 10:00:00.000500
- Firm B detects at 10:00:00.000650 (150 μs slower)
- Firm A executes, opportunity gone
- Firm B orders rejected (stale price)

**Monthly performance:**

- Firm A: 150 successful arbitrages, $75K profit
- Firm B: 80 successful arbitrages, $40K profit
- Firm C-E: < 50 each

**Technology breakdown:**

- Firm A: $8M technology investment, co-located
- Firm B: $4M investment, slightly slower hardware
- Firm C-E: $1-2M investment, no co-location

**Profit per dollar invested:**

- Firm A: $75K / $8M = 0.9% monthly ROI
- Firm B: $40K / $4M = 1.0% monthly ROI  
- **Firm B actually more efficient!**

**Lesson:**

- Diminishing returns to technology spending
- Winner-take-all at the margin
- Market saturated with competitors
- Profitability declining structurally

---

## Practical Steps


**Step-by-step implementation (institutional):**

### 1. Infrastructure Setup


**Phase 1: Technology (6-12 months):**

**Hardware:**

- Co-located servers at primary exchanges (EBS, Reuters)
- FPGA-based order routers ($500K+)
- Redundant systems (no single point of failure)
- 10-40 Gbps network connections

**Software:**

- Real-time pricing engine (C++/Rust)
- Arbitrage detection algorithm
- Smart order router
- Risk management system
- Automated position reconciliation

**Data feeds:**

- EBS, Reuters D3, Currenex subscriptions
- Tick-by-tick data (every price update)
- Order book depth (L2/L3 data)
- **Cost: $50-200K annually**

### 2. Algorithm Development


**Core logic:**

**Step 1: Price ingestion**

```python
def ingest_prices():
    prices = {
        'EUR/USD': get_live_price('EURUSD'),
        'GBP/USD': get_live_price('GBPUSD'),
        'EUR/GBP': get_live_price('EURGBP'),
    }
    return prices
```

**Step 2: Arbitrage detection**

```python
def detect_arbitrage(prices):
    # Path 1: USD → EUR → GBP → USD
    path1_product = (
        prices['EUR/USD']['bid'] *
        prices['EUR/GBP']['bid'] *
        prices['GBP/USD']['bid']
    )
    
    if path1_product > 1.0 + threshold:
        return 'PATH1', path1_product - 1.0
    
    # Path 2: Reverse
    path2_product = (
        1 / prices['EUR/USD']['ask'] *
        1 / prices['EUR/GBP']['ask'] *
        1 / prices['GBP/USD']['ask']
    )
    
    if path2_product > 1.0 + threshold:
        return 'PATH2', path2_product - 1.0
    
    return None, 0
```

**Step 3: Execution**

```python
def execute_arbitrage(path, size):
    if path == 'PATH1':
        orders = [
            create_order('BUY', 'EURUSD', size),
            create_order('SELL', 'EURGBP', size),
            create_order('SELL', 'GBPUSD', size),
        ]
    
    # Send simultaneously
    send_orders_atomic(orders)
    
    # Monitor fills
    fills = wait_for_fills(timeout=50ms)
    
    if not all_filled(fills):
        abort_and_hedge()
```

### 3. Backtesting and Simulation


**Historical analysis:**

**Data collection:**

- 1+ years of tick data
- Bid/ask for all relevant pairs
- Timestamp precision: microseconds
- Reconstruct order book states

**Simulation:**

- Replay historical data
- Apply detection algorithm
- Simulate execution (add latency)
- Calculate hypothetical P&L

**Metrics to validate:**

- Opportunity frequency (10-50 daily?)
- Average profit per trade (0.5-2 bps?)
- Success rate (> 90%?)
- Sharpe ratio (> 5?)

### 4. Paper Trading


**Live testing without risk:**

**Setup:**

- Connect to live market data
- Run detection algorithm real-time
- Send orders to simulator (not exchange)
- Log performance

**Duration:**

- Minimum 3 months
- Across different market conditions
- Validate technology stability
- Fine-tune parameters

**Go-live criteria:**

- Paper trading Sharpe > 5
- Success rate > 92%
- No system crashes
- Latency < 2 ms consistently

### 5. Live Trading


**Gradual ramp-up:**

**Week 1-2: Small size**

- $1M per trade (test execution)
- Monitor closely
- Verify P&L matches expectations

**Month 1: Scale to 25%**

- Increase to $5-10M per trade
- Add more currency triplets
- Refine risk controls

**Month 3-6: Full deployment**

- Scale to target size ($50M+)
- Optimize execution algorithms
- Monitor competitive dynamics

---

## Final Wisdom


> "Triangular arbitrage is the purest form of trading—theoretically risk-free, economically sound, and intellectually satisfying. But it's also a technological arms race where milliseconds determine winners and losers. In the 1990s, smart traders made fortunes with simple algorithms. Today, only firms with tens of millions in technology and microsecond execution compete. For retail traders, it's a fascinating concept but practically inaccessible. The lesson: some opportunities exist only for those with the fastest infrastructure. Market efficiency is real, and it's enforced by those who can trade in nanoseconds."

**Key success factors:**

- Ultra-low latency (< 1 ms total)
- Co-located servers (exchange proximity)
- Simultaneous execution (all three legs)
- Robust risk controls (abort on partial fill)
- Massive technology investment ($5M+)
- Continuous optimization (algorithm improvement)
- Accept declining profitability (competition intensifies)
- Know when to exit (returns insufficient for capital required)
