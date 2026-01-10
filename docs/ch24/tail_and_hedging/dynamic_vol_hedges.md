# Dynamic Vol Hedges

**Dynamic volatility hedges** are adaptive risk management strategies that adjust hedge intensity, strikes, and maturities in response to changing market conditions, volatility regimes, and portfolio exposures.

---

## The Core Insight

**The fundamental idea:**

- Static hedges ignore regime changes
- Volatility clusters and mean-reverts
- Optimal hedge varies with market state
- Dynamic adjustment reduces cost and improves effectiveness
- Scale up protection when risks rise
- Scale down when markets calm

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/dynamic_vol_hedge.png?raw=true" alt="dynamic_vol_hedge" width="700">
</p>
**Figure 1:** Dynamic hedge notional adjusting with VIX level, showing increased protection during elevated volatility regimes and reduced exposure during calm periods, optimizing the cost-benefit trade-off.

**You're essentially asking: "How do I adapt my hedging to market conditions rather than using a fixed approach?"**

---

## Why Dynamic Hedging?

### 1. Static Hedge Problems

**Fixed protection inadequacies:**

**Constant notional:**
- Market calm (VIX 12): Overhedged, waste money
- Market stress (VIX 30): Underhedged, need more protection
- **One-size-fits-all fails**

**Theta bleed:**
- Static OTM puts decay constantly
- Pay whether needed or not
- Annual cost: 20-40% of premium

**Strike misalignment:**
- Fixed strike doesn't adapt to spot moves
- Far OTM after rally (useless)
- Near ITM after selloff (expensive to roll)

**Maturity rigidity:**
- Fixed maturity forces rolling schedule
- May need to roll at bad times
- Transaction costs compound

### 2. Volatility Clustering

**Key empirical fact:**

$$
\text{High vol} \to \text{High vol (short-term)}
$$

$$
\text{Low vol} \to \text{Low vol (short-term)}
$$

**Persistence (autocorrelation):**
- Vol today predicts vol tomorrow (~0.7 correlation)
- Spikes cluster (crash risk elevated after first spike)
- Calm periods extend (bull markets stable)

**Implication:**
- Increase hedge when vol rises (more needed)
- Decrease hedge when vol falls (less needed)
- Dynamic approach captures clustering

### 3. Cost Reduction

**Empirical cost savings:**

**Static hedge:**
- Constant $\$1,000$ vega
- Annual cost: $\$200,000$ (2% portfolio)
- Always on

**Dynamic hedge:**
- $\$0-2,000$ vega (VIX-dependent)
- Annual cost: $\$120,000$ (1.2% portfolio)
- **40% cost reduction!**

**Why?**
- Not hedged during calm 60% of time
- Extra hedged during stress 10% of time
- Net: Lower cost, better protection

### 4. Improved Hedge Ratio

**Optimal hedge varies with regime:**

**Low vol regime (VIX < 15):**
- Crashes rare from low vol
- Small hedge sufficient
- Optimal: 20-30% of full hedge

**Medium vol regime (VIX 15-25):**
- Normal hedge
- Optimal: 50-70% of full hedge

**High vol regime (VIX > 25):**
- Crash risk elevated
- Need more protection
- Optimal: 100-150% of full hedge

**Dynamic captures this optimality**

### 5. Gamma Scalping Integration

**Active hedge management:**

**Static approach:**
- Delta-hedge on schedule (daily/weekly)
- Ignore gamma P&L potential

**Dynamic approach:**
- Delta-hedge when favorable
- Collect gamma when market whipsaws
- Offset theta with gamma profits
- **Reduces net cost**

### 6. Path Dependency

**Returns path matters:**

**Scenario A (gradual decline):**
- Market falls 20% over 6 months
- Vol rises gradually
- Dynamic hedge scales up progressively
- **Better protection**

**Scenario B (flash crash):**
- Market falls 20% in 3 days
- Vol explodes instantly
- Dynamic hedge already elevated (pre-spike)
- **Captures crash**

**Static hedge same both scenarios (suboptimal)**

### 7. Asymmetric Payoffs

**Dynamic strategy payoff:**

**Bull market (low vol):**
- Minimal hedge cost
- Portfolio gains maximized
- **Let winners run**

**Bear market (high vol):**
- Maximum hedge protection
- Portfolio losses cushioned
- **Cut losers**

**Asymmetric upside/downside = improved Sharpe**

---

## Dynamic Hedge Strategies

**Different adaptive approaches:**

### 1. VIX-Triggered Scaling

**Rule-based adjustment:**

$$
N_{\text{hedge}}(t) = N_{\text{base}} \times f(\text{VIX}_t)
$$

**Linear scaling:**

$$
f(\text{VIX}) = \max\left(0, \, \min\left(2, \, \frac{\text{VIX} - 10}{15}\right)\right)
$$

**Example:**
- Base hedge: $\$1,000$ vega
- VIX = 10 → Hedge = $\$0$ (no hedge)
- VIX = 17.5 → Hedge = $\$1,000$ (full hedge)
- VIX = 25 → Hedge = $\$2,000$ (2x hedge)

**Benefits:**
- Simple rule
- Automatic adjustment
- Reduces cost in calm markets

### 2. Realized Vol Feedback

**Adjust based on actual volatility:**

$$
N(t) = N_{\text{base}} \times \left(\frac{\text{RV}_{20\text{-day}}}{\text{RV}_{\text{target}}}\right)
$$

**Example:**
- Target realized vol: 15%
- Current 20-day realized: 25%
- **Hedge multiplier:** $25\% / 15\% = 1.67\times$

**Interpretation:**
- Market realized vol elevated → Scale up
- Market realized vol low → Scale down
- Adapts to actual risk

### 3. Conditional Hedging

**Binary on/off approach:**

$$
N(t) = \begin{cases}
N_{\text{full}} & \text{if VIX} > 25 \\
N_{\text{partial}} & \text{if } 15 < \text{VIX} < 25 \\
0 & \text{if VIX} < 15
\end{cases}
$$

**Example:**
- No hedge when VIX < 15 (80% of time)
- Half hedge when VIX 15-25 (15% of time)
- Full hedge when VIX > 25 (5% of time)

**Cost savings:**
- Avoid 80% of normal hedging cost
- Still capture most crashes (VIX spikes first)

### 4. Term Structure Strategy

**Adjust based on VIX curve:**

**Contango (normal):**
- VIX futures upward-sloping
- Low near-term risk
- **Reduce short-term hedge, keep long-term**

**Backwardation (stress):**
- VIX futures inverted
- High near-term risk
- **Increase short-term hedge, reduce long-term**

**Implementation:**

$$
\text{Ratio}_{\text{short:long}} = \frac{F_1 / F_3}{1}
$$

Where $F_1$ = 1M VIX future, $F_3$ = 3M VIX future.

### 5. Correlation-Adjusted Hedging

**Scale with realized correlation:**

$$
N(t) = N_{\text{base}} \times \left(\frac{\rho_t}{\rho_{\text{normal}}}\right)
$$

**Rationale:**
- High correlation → Systemic risk → Need more hedge
- Low correlation → Diversification works → Need less hedge

**Example:**
- Normal correlation: 40%
- Current correlation: 60%
- **Hedge multiplier:** $60\% / 40\% = 1.5\times$

### 6. Drawdown-Triggered

**Increase hedge after losses:**

$$
N(t) = N_{\text{base}} \times \left(1 + \alpha \times \max(0, -\text{DD}_t + 5\%)\right)
$$

**Example:**
- $\alpha = 0.5$
- Portfolio down 10% (DD = -10%)
- **Hedge multiplier:** $1 + 0.5 × (-10\% + 5\%) = 1.025\times$

**Interpretation:**
- Protect after losses (stop bleeding)
- Let winners run (low hedge when up)

### 7. Option Greeks Rebalancing

**Delta-weighted dynamic hedge:**

$$
N_{\text{puts}}(t) = \frac{\text{Portfolio Delta}}{\text{Put Delta} \times 100}
$$

**As portfolio falls:**
- Portfolio delta decreases
- Need fewer puts (auto-scaling)
- Sell partial hedge, collect premium

**As portfolio rises:**
- Portfolio delta increases  
- Need more puts
- Buy additional hedge

**Self-financing mechanism**

---

## Mathematical Framework

### 1. Optimal Dynamic Rule

**Minimize expected cost + expected crash loss:**

$$
\min_{N(t)} \mathbb{E}\left[\int_0^T C(N(t))dt + L(\text{Crash}) \times \mathbb{P}(\text{Crash})\right]
$$

Subject to:
$$
N(t) \geq 0, \quad N(t) \leq N_{\max}
$$

**Solution (approximate):**

$$
N^*(t) = N_{\text{base}} \times \frac{\lambda(t)}{\bar{\lambda}}
$$

Where $\lambda(t)$ = Current crash intensity (from VIX, vol, etc.)

### 2. VIX-Based Scaling Function

**Empirically calibrated:**

$$
f(\text{VIX}) = \frac{1}{1 + e^{-k(\text{VIX} - \text{VIX}_0)}}
$$

**Parameters:**
- $k \approx 0.2$ (steepness)
- $\text{VIX}_0 \approx 20$ (midpoint)

**Properties:**
- Sigmoid shape (smooth transition)
- 0 at low VIX, 1 at high VIX
- Continuous adjustment

### 3. Cost-Benefit Analysis

**Static hedge cost:**

$$
C_{\text{static}} = N \times \theta \times T
$$

**Dynamic hedge cost:**

$$
C_{\text{dynamic}} = \int_0^T N(t) \times \theta(t) dt + \text{Transaction Costs}
$$

**Empirical:**
- $C_{\text{dynamic}} \approx 0.5\text{-}0.7 \times C_{\text{static}}$
- **30-50% cost savings**

### 4. Hedge Effectiveness Ratio

**Measure of protection:**

$$
\text{HER} = \frac{\text{Hedge Gain in Crash}}{\text{Portfolio Loss in Crash}}
$$

**Static hedge:**
- HER ≈ 0.4-0.6 (40-60% offset)

**Dynamic hedge:**
- HER ≈ 0.5-0.7 (50-70% offset)
- **Better protection when needed**

### 5. Gamma P&L Integration

**Expected gamma profit:**

$$
\mathbb{E}[\text{Gamma P&L}] = \frac{1}{2}\Gamma \times \mathbb{E}[dS^2] - \theta \times dt
$$

**Dynamic hedging exploits:**
- High realized vol → Positive gamma P&L
- Offsets theta decay partially
- **Net cost lower**

### 6. Transition Probabilities

**Regime switching model:**

$$
\mathbb{P}(\text{High Vol}_t | \text{Low Vol}_{t-1}) = p_{LH}
$$

$$
\mathbb{P}(\text{Low Vol}_t | \text{High Vol}_{t-1}) = p_{HL}
$$

**Empirical:**
- $p_{LH} \approx 0.05$ (5% chance to spike)
- $p_{HL} \approx 0.15$ (15% chance to normalize)

**Use for dynamic hedge timing**

### 7. Sharpe Ratio Improvement

**Portfolio Sharpe with dynamic hedge:**

$$
\text{Sharpe}_{\text{dynamic}} = \frac{\mu - C_{\text{dynamic}}}{\sigma \times \sqrt{1 - \rho^2}}
$$

Where $\rho$ = Correlation between portfolio and hedge.

**Empirical:**
- Unhedged: Sharpe ≈ 0.5
- Static hedge: Sharpe ≈ 0.55
- Dynamic hedge: Sharpe ≈ 0.65
- **20% improvement!**

---

## Common Mistakes

**Pitfalls to avoid:**

### 1. Over-Optimization

**Mistake:** Complex rules with many parameters

**Why it fails:** Overfitting to past data

**Example:**

$$
N(t) = f(\text{VIX}, \text{RV}, \text{Skew}, \text{Term Structure}, \rho, \text{Momentum}, ...)
$$

- 10+ parameters
- Perfect backtest (Sharpe 2.0)
- Reality: Sharpe 0.3 (worse than static!)
- **Overfitted**

**Fix:**
- Keep rules simple (1-3 inputs max)
- VIX-based scaling sufficient
- Out-of-sample testing mandatory

### 2. Too Frequent Rebalancing

**Mistake:** Adjust hedge daily

**Why it fails:** Transaction costs explode

**Example:**
- Hedge changes VIX 18 → 19 → 18
- Adjust hedge both times
- Cost: 0.1% × 252 days = 25.2%/year
- **Eats all savings!**

**Fix:**
- Rebalance threshold (VIX moves >2 points)
- Weekly/monthly schedule
- Only adjust if meaningful change

### 3. Ignoring Transaction Costs

**Mistake:** Assume frictionless trading

**Why it fails:** Spreads and commissions matter

**Example:**
- Dynamic rule requires 20 adjustments/year
- Bid-ask: 0.05 per adjustment
- Notional: $\$1M$
- **Cost: $\$1M × 0.05 × 20 = $\$1M/year (huge!)**

**Fix:**
- Model costs in backtest
- Use wider rebalancing bands
- Trade liquid instruments only

### 4. Whipsaw Losses

**Mistake:** React to every VIX move

**Why it fails:** False signals

**Example:**
- VIX 20 → 25 → 20 (spike and revert)
- Increase hedge at 25 (buy high)
- Decrease at 20 (sell low)
- **Whipsawed!**

**Fix:**
- Use moving averages (smooth VIX)
- Require persistence (2-3 days)
- Don't chase spikes

### 5. Neglecting Hedge Decay

**Mistake:** Dynamic hedge with short-dated options

**Why it fails:** Theta still bites

**Example:**
- Use 30-day puts dynamically
- Even scaled down, decay occurs
- **Cost: 30% annually (no savings)**

**Fix:**
- Use longer-dated options (90+ days)
- Or variance swaps (no theta)
- Balance flexibility vs. cost

### 6. Backtest Overfitting

**Mistake:** Optimize on same data as test

**Why it fails:** No out-of-sample validation

**Example:**
- Optimize rule on 2010-2020 data
- Test on 2010-2020 data
- Great results (Sharpe 1.5)
- **Reality: Doesn't work on new data**

**Fix:**
- Train on 2000-2015
- Test on 2015-2020 (out-of-sample)
- Use simple rules (less overfitting)

### 7. Missing Regime Shifts

**Mistake:** Assume stationary vol dynamics

**Why it fails:** Regimes change

**Example:**
- 2010-2019: Low vol regime
- Dynamic rule: Scale down when VIX < 15
- 2020+: Structural shift to higher vol
- Rule underhedges
- **Losses in new regime**

**Fix:**
- Monitor regime indicators
- Adjust thresholds over time
- Use percentile-based rules (adaptive)

### 8. Correlation Blindness

**Mistake:** Ignore hedge-portfolio correlation

**Why it fails:** Hedge effectiveness varies

**Example:**
- Dynamic hedge based on VIX alone
- But portfolio 50% bonds (low correlation)
- Overhedge equity risk
- **Inefficient**

**Fix:**
- Adjust for portfolio composition
- Only hedge equity portion dynamically
- Use correlation-weighted scaling

---

## Risk Management Rules

### 1. Rebalancing Thresholds

**Trigger adjustments when:**

$$
|\text{VIX}_t - \text{VIX}_{\text{last rebalance}}| > \Delta_{\text{threshold}}
$$

**Recommended:**
- $\Delta_{\text{threshold}} = 3$ VIX points
- Or 15% relative change
- Or weekly schedule (whichever first)

**Example:**
- Last rebalanced at VIX 18
- Trigger at VIX < 15 or VIX > 21
- Avoid whipsaw from noise

### 2. Maximum Hedge Limit

**Cap dynamic hedge:**

$$
N(t) \leq 2 \times N_{\text{base}}
$$

**Rationale:**
- Prevent over-hedging in spikes
- Diminishing returns above 2x
- Control maximum cost

**Example:**
- Base hedge: $\$1,000$ vega
- Even at VIX 50, cap at $\$2,000$ vega
- Don't chase tail

### 3. Minimum Hedge Floor

**Always maintain baseline:**

$$
N(t) \geq 0.2 \times N_{\text{base}}
$$

**Rationale:**
- Flash crashes happen from low VIX
- Keep minimum protection
- Avoid being caught naked

**Example:**
- Base: $\$1,000$ vega
- Even at VIX 10, keep $\$200$ vega hedge
- Insurance against surprises

### 4. Cost Budget Constraint

**Annual cost cap:**

$$
\int_0^T N(t) \times \text{Cost}(t) dt \leq C_{\max}
$$

**Example:**
- Max budget: 2% of portfolio = $\$200,000$
- If exceed, scale down all hedges proportionally
- Don't blow budget on dynamic adjustments

### 5. Monitoring Frequency

**Review schedule:**

**Daily:**
- Check VIX level vs. thresholds
- Compute realized vol (20-day)
- Monitor hedge MTM

**Weekly:**
- Rebalance if triggers hit
- Review P&L attribution
- Check portfolio delta

**Monthly:**
- Full performance analysis
- Adjust rules if regime changed
- Backtest updated

### 6. Diversification

**Dynamic hedges across:**

- Multiple indices (SPX, NDX, Russell)
- Multiple maturities (3M, 6M, 12M)
- Multiple strategies (variance, options, VIX futures)

**Don't:**
- Put all in single dynamic strategy
- Ignore idiosyncratic risks

### 7. Backtesting Standards

**Required checks:**

- Out-of-sample testing (50% train, 50% test)
- Transaction cost modeling (bid-ask spreads)
- Multiple regime testing (2008, 2020, bull markets)
- Sensitivity analysis (parameter ranges)
- Walk-forward optimization

**Red flags:**
- Sharpe > 1.5 (too good, likely overfit)
- Win rate > 80% (unrealistic)
- Works only on one crisis

---

## Real-World Examples

### 1. VIX-Scaled Hedge (2017-2020)

**Setup:**
- $\$50M$ portfolio
- Dynamic rule: $N = \$1,000 × \max(0, (\text{VIX} - 12) / 8)$

**Performance:**

**2017-2019 (low VIX):**
- Average VIX: 14
- Average hedge: $\$250$ vega
- Annual cost: $\$50,000$ (0.1% portfolio)
- **Very cheap**

**2020 (COVID):**
- Feb VIX: 15 → Hedge: $\$375$ vega
- March VIX: 60+ → Hedge: $\$6,000$ vega (scaled up!)
- Hedge gain: $\$3,000,000$
- Portfolio loss: $\$10,000,000$ (20% drawdown)
- **Net: -$\$7,000,000$ (30% offset)**

**Total 4 years:**
- Cost: $\$200,000$
- Gain: $\$3,000,000$
- **Net: +$\$2,800,000$ (positive!)**

**Lesson:** Dynamic scaling captured crash at low cost

### 2. Conditional Hedge (2012-2018)

**Setup:**
- Only hedge when VIX > 20
- $\$20M$ portfolio
- Full hedge: $\$2,000$ vega

**Performance:**

- VIX > 20: 15% of days (55 days/year)
- Hedged ~15% of time
- Cost: $\$100,000/year (0.5% portfolio)

**2015 Flash Crash:**
- VIX spiked to 35
- Hedge active (VIX > 20)
- Hedge gain: $\$400,000$
- Portfolio loss: $\$800,000$
- **50% offset**

**Total 7 years:**
- Cost: $\$700,000$
- Gains: $\$900,000$ (multiple mini-crashes)
- **Net: +$\$200,000$**

**Lesson:** Conditional hedging profitable over cycle

### 3. Gamma Scalping (2019)

**Setup:**
- $\$30M$ portfolio
- Dynamic delta hedging (daily)
- Exploit realized vol > implied vol

**Strategy:**
- Buy ATM straddles
- Delta-hedge daily
- Collect gamma when market moves

**Performance:**
- Implied vol: 15%
- Realized vol: 18%
- Gamma P&L: +$\$300,000$
- Theta cost: -$\$200,000$
- **Net: +$\$100,000$ (positive from vol mispricing)**

**Lesson:** Active gamma management can offset costs

### 4. Term Structure Strategy (2016-2017)

**Setup:**
- Persistent contango (VIX futures upward)
- Dynamic: Short near-term, long far-term hedges

**Implementation:**
- Short 1M VIX puts (collect premium)
- Long 6M variance (crash protection)
- Ratio adjusted by term structure slope

**Performance:**
- Collected $\$150,000$ from short puts
- Paid $\$100,000$ for long variance
- No crashes occurred
- **Net: +$\$50,000$ (funded hedge)**

**Lesson:** Term structure exploitation reduces cost

---

## Practical Steps

### 1. Design Dynamic Rule

**Choose simple rule:**

**Option A: VIX-based**

$$
N(t) = N_{\text{base}} \times \max\left(0, \, \min\left(2, \, \frac{\text{VIX} - 12}{10}\right)\right)
$$

**Option B: Realized vol-based**

$$
N(t) = N_{\text{base}} \times \frac{\text{RV}_{20d}}{15\%}
$$

**Option C: Conditional**

$$
N(t) = \begin{cases}
2 \times N_{\text{base}} & \text{if VIX} > 25 \\
N_{\text{base}} & \text{if } 15 < \text{VIX} \leq 25 \\
0 & \text{if VIX} \leq 15
\end{cases}
$$

### 2. Backtest the Rule

**Historical simulation:**

```python
import numpy as np
import pandas as pd

# Load data
vix = pd.read_csv('vix_data.csv')
returns = pd.read_csv('portfolio_returns.csv')

# Compute dynamic notional
def dynamic_notional(vix_level, base=1000):
    return base * max(0, min(2, (vix_level - 12) / 10))

# Simulate hedge P&L
hedge_pnl = []
for t in range(len(vix)):
    notional = dynamic_notional(vix[t])
    # Compute hedge payoff (simplified)
    pnl = notional * (realized_vol[t] - implied_vol[t])
    hedge_pnl.append(pnl)

# Analyze performance
total_cost = -sum([p for p in hedge_pnl if p < 0])
total_gain = sum([p for p in hedge_pnl if p > 0])
print(f"Net P&L: {sum(hedge_pnl)}")
print(f"Sharpe: {np.mean(hedge_pnl) / np.std(hedge_pnl)}")
```

### 3. Set Rebalancing Rules

**Define triggers:**

- VIX moves > 3 points from last rebalance
- Or weekly schedule
- Or drawdown > 5%

**Example:**
```python
def should_rebalance(vix_now, vix_last, days_since):
    if abs(vix_now - vix_last) > 3:
        return True
    if days_since >= 7:
        return True
    return False
```

### 4. Implement Execution

**Enter initial hedge:**

- Calculate base notional
- Execute at current VIX level
- Use limit orders

**Example:**
- Portfolio: $\$10M$
- Base hedge: $\$1,000$ vega
- VIX = 18
- Initial notional: $\$1,000 × (18-12)/10 = \$600$ vega

### 5. Monitor and Adjust

**Daily monitoring:**

- Check VIX vs. threshold
- Compute realized vol
- Monitor hedge MTM

**Rebalancing when triggered:**

- Compute new notional
- Adjust position (buy/sell)
- Record transaction

**Example:**
- VIX rises 18 → 22 (trigger!)
- Old notional: $\$600$ vega
- New notional: $\$1,000$ vega
- **Buy additional $\$400$ vega**

### 6. Performance Review

**Monthly analysis:**

- Hedge P&L (gains vs. losses)
- Cost paid (net theta + VRP)
- Effectiveness (crash offset %)
- Sharpe ratio

**Adjust if needed:**

- Rules too conservative? (missed protection)
- Too aggressive? (high cost)
- Tune parameters

---

## Final Wisdom

> "Dynamic volatility hedging is the evolution from fixed insurance to adaptive protection - adjusting to market conditions like a thermostat rather than a static shield. The key is balancing responsiveness with stability: too reactive and you whipsaw yourself to death; too static and you miss regime changes. The best dynamic rules are simple (VIX-based scaling), require infrequent rebalancing (weekly not daily), and reduce costs by 30-50% while improving protection when it matters most. Think of it as turning off the air conditioning when it's cold outside and cranking it up when it's hot - common sense risk management that compounds into significant savings over time."

**Key to success:**

- Keep rules simple (VIX or realized vol based, 1-2 parameters)
- Rebalance weekly or when VIX moves > 3 points
- Cap dynamic hedge at 2x base (prevent over-hedging)
- Maintain floor at 0.2x base (flash crash protection)
- Backtest out-of-sample with transaction costs
- Monitor monthly, adjust parameters annually
- Target 30-50% cost reduction vs. static hedge
- Remember: Simplicity beats complexity in real markets
