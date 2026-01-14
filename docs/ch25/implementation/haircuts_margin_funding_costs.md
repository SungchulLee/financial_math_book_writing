# Haircuts, Margin, and Funding Costs


**Haircuts, margin, and funding costs** are the collateral requirements, daily cash flows, and interest expenses that determine the true cost and leverage available for trading strategies, with costs rising dramatically during stress periods.

---

## The Core Insight


**The fundamental idea:**

- Leverage requires collateral (haircut/margin)
- Haircuts reduce borrowing capacity
- Margin calls create cash flow risk
- Funding costs eat returns
- All three worsen in stress (haircuts up, margin calls up, funding costs up)
- True leverage ≠ Notional leverage

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/haircuts_margin.png?raw=true" alt="haircuts_margin" width="700">
</p>
**Figure 1:** Evolution of haircuts and repo rates during stress showing dramatic increases - haircuts rising from 2% to 20%+ and repo rates spiking 200-500 bps above normal, dramatically reducing leverage capacity and increasing funding costs.

**You're essentially asking: "What are the real costs of using leverage, and how do they change during stress?"**

---

## Haircuts


### 1. Basic Definition


**Haircut:**

$$
\text{Haircut} = \frac{\text{Collateral Value} - \text{Loan Amount}}{\text{Collateral Value}}
$$

**Example:**
- Post $\$105$ of bonds
- Receive $\$100$ cash loan
- **Haircut: $(105-100)/105 = 4.76\%$**

**Interpretation:**
- Haircut = Cushion for lender
- Protects against collateral price decline
- Higher haircut = More conservative lending

### 2. Effective Leverage


**Maximum leverage from haircut:**

$$
\text{Max Leverage} = \frac{1}{1 - \text{Haircut}}
$$

**Example:**
- Haircut: 10%
- **Max leverage: $1/(1-0.10) = 1.11×$**

**Lower haircut → Higher leverage:**
- Haircut: 2% → Max leverage: 50×
- Haircut: 5% → Max leverage: 20×
- Haircut: 10% → Max leverage: 10×
- Haircut: 20% → Max leverage: 5×
- Haircut: 50% → Max leverage: 2×

### 3. Haircut Levels by Asset


**Normal market haircuts:**

**US Treasuries:**
- On-the-run: 2-3%
- Off-the-run: 3-5%
- Very safe collateral

**Agency MBS:**
- AAA-rated: 5-8%
- Lower-rated: 10-15%
- Prepayment risk

**Investment-grade corporates:**
- High-rated (AA/A): 8-12%
- Mid-rated (BBB): 12-18%
- Credit risk matters

**High-yield corporates:**
- Liquid names: 20-30%
- Less liquid: 30-50%
- Significant risk

**Equities:**
- Large-cap (S&P 100): 15-25%
- Mid-cap: 25-35%
- Small-cap: 35-50%
- Volatile collateral

**Emerging markets:**
- Sovereigns: 20-40%
- Corporates: 30-60%
- Currency risk adds

### 4. Stress Haircuts


**Crisis increases:**

**2008 Financial Crisis:**

**Treasuries:**
- Normal: 2-3%
- Crisis: 5-10% (2-3× higher)

**IG Corporates:**
- Normal: 10-15%
- Crisis: 30-50% (3-5× higher)

**HY Corporates:**
- Normal: 25-35%
- Crisis: 60-100% (3-4× higher, essentially unfunded)

**Equities:**
- Normal: 20-30%
- Crisis: 50-80% (3-4× higher)

**2020 COVID Crisis:**

Similar patterns:
- Treasury haircuts: 3% → 8%
- IG corporate: 12% → 35%
- HY corporate: 30% → 75%

### 5. Haircut Calculation


**Risk-based formula:**

$$
\text{Haircut} = k \times \sigma \times \sqrt{T_{\text{liquidation}}}
$$

Where:
- $k$ = Risk aversion (1.5-3.0)
- $\sigma$ = Daily volatility
- $T_{\text{liquidation}}$ = Days to liquidate

**Example:**
- Corporate bond: $\sigma = 1.5\%$ daily
- Liquidation: 5 days
- $k = 2$ (moderate risk aversion)

**Haircut:**

$$
2 \times 0.015 \times \sqrt{5} = 6.7\%
$$

**Stress haircut (higher $k$ and $\sigma$):**
- $k = 3$
- $\sigma = 3\%$ (crisis vol)
- **Haircut: $3 \times 0.03 \times \sqrt{5} = 20.1\%$**

### 6. Impact on Returns


**Cost of haircut:**

$$
\text{Opportunity Cost} = \text{Haircut} \times \text{Return on Equity}
$$

**Example:**
- Position: $\$100$
- Haircut: 10%
- Need $\$10$ equity (can't borrow)
- ROE target: 15%
- **Annual cost: $\$10 × 0.15 = $\$1.50$ (1.5% of position)**

### 7. Procyclicality


**Feedback loop:**

$$
\text{Price Fall} \to \text{Higher Haircut} \to \text{Less Borrowing} \to \text{Forced Sales} \to \text{More Price Falls}
$$

**Example:**
- Start: 10% haircut, $\$100$ position, $\$90$ borrowed
- Price falls 10% → Position worth $\$90$
- Haircut increases to 20%
- Can now borrow: $\$90 × (1-0.20) = $\$72$
- Borrowed: $\$90$, can borrow: $\$72$
- **Need to repay $\$18$ → Force sell**

---

## Margin Requirements


### 1. Initial Margin


**Upfront collateral:**

$$
\text{Initial Margin} = \text{Notional} \times \text{IM Rate}
$$

**Example (futures):**
- 10Y Treasury futures: $\$100,000$ notional
- IM rate: 3.5%
- **Initial margin: $\$3,500$**

**Typical IM rates:**
- Treasury futures: 2-4%
- Equity futures: 5-10%
- Commodity futures: 5-15%
- FX futures: 2-5%

### 2. Variation Margin


**Daily settlement:**

$$
\text{VM} = \text{Current Value} - \text{Previous Value}
$$

**Example:**
- Long 10 SPX futures @ 4,500
- Next day: 4,480 (down 20 points)
- VM: $(4,480 - 4,500) \times 10 \times \$50 = -\$10,000$
- **Must post $\$10,000$ cash**

**Daily cash flow risk:**
- Winners receive cash
- Losers post cash
- Can create liquidity stress

### 3. Maintenance Margin


**Minimum account balance:**

$$
\text{Maintenance Margin} = \text{Initial Margin} \times 0.75 \text{ (typical)}
$$

**Margin call triggered when:**

$$
\text{Account Equity} < \text{Maintenance Margin}
$$

**Example:**
- Initial margin: $\$10,000$
- Maintenance: $\$7,500$
- Current equity: $\$7,000$ (after losses)
- **Margin call: Must add $\$3,000$ to get back to IM**

### 4. Portfolio Margining


**Cross-collateralization:**

$$
\text{Portfolio Margin} = f(\text{Net Risk}) < \sum \text{Individual Margins}
$$

**Example:**

**Reg T margining (separate):**
- Long 100 SPY: $\$25,000$ margin
- Short 100 IWM: $\$15,000$ margin
- **Total: $\$40,000$**

**Portfolio margining:**
- Net delta: Nearly zero (hedged)
- Net risk: $\$5,000$ (basis risk only)
- **Portfolio margin: $\$5,000$ (87.5% less!)**

**Benefits:**
- Much higher leverage
- Recognizes hedges
- More capital-efficient

**Requirements:**
- Minimum $\$100,000$ account
- Sophisticated risk management
- Not available for all investors

### 5. Margin in Stress


**Crisis increases:**

**Normal (2019):**
- S&P futures IM: 5%
- Treasury futures IM: 3%

**Crisis (March 2020):**
- S&P futures IM: 12% (2.4× higher)
- Treasury futures IM: 6% (2× higher)

**Impact:**
- Need more cash to hold same position
- Or reduce position (forced deleveraging)

### 6. Margin Calls


**Frequency and size:**

**Normal markets:**
- Infrequent (maybe weekly)
- Small ($1,000s$)
- Easy to meet

**Crisis markets:**
- Daily (sometimes intraday!)
- Large ($100,000s$ to $millions$)
- Liquidity strain

**Example (2008):**
- Hedge fund: $\$1B$ portfolio, 50% levered
- Market falls 10% (portfolio → $\$900M$)
- Equity: $\$500M$ → $\$400M$
- Margin call: Restore to 50% leverage
- **Need to post $\$50M$ cash (or sell $\$100M$)**

### 7. Margin Models


**Risk-based calculation:**

**SPAN (futures):**

$$
\text{SPAN Margin} = \max_{\text{scenarios}} (\text{Portfolio Loss})
$$

- Simulate 16 scenarios (price, vol moves)
- Take worst-case loss
- Add liquidity charge

**Example:**
- Scenario 1: -$\$10,000$
- Scenario 2: -$\$12,000$
- ... (14 more scenarios)
- **Margin: $\$12,000$ + liquidity**

**VaR-based:**

$$
\text{Margin} = \text{VaR}_{99\%}^{10\text{-day}} + \text{Stressed VaR}
$$

- 10-day horizon
- 99% confidence
- Stressed period calibration

---

## Funding Costs


### 1. Repo Financing


**Cost of borrowing cash:**

$$
\text{Funding Cost} = \text{Borrowed Amount} \times r_{\text{repo}} \times \frac{t}{360}
$$

**Example:**
- Borrow $\$10M$ via repo
- Repo rate: 2.5%
- Term: 30 days

**Cost:**

$$
\$10M \times 0.025 \times \frac{30}{360} = \$20,833
$$

**Annual cost: $\$250,000$ (2.5% of $\$10M$)**

### 2. Repo Rate Components


**Total repo rate:**

$$
r_{\text{repo}} = \text{SOFR} + \text{Collateral Adjustment} + \text{Term Premium} + \text{Credit Spread}
$$

**Example:**
- SOFR: 2.0%
- Collateral (IG corporate): +0.40%
- Term (3 months): +0.15%
- Credit spread: +0.10%
- **Total repo rate: 2.65%**

### 3. Funding Cost Impact


**Return reduction:**

$$
\text{Net Return} = \text{Asset Return} - \text{Funding Cost} \times \text{Leverage}
$$

**Example:**
- Asset return: 5%
- Funding cost: 2.5%
- Leverage: 5×

**Gross return:**

$$
5\% \times 5 = 25\%
$$

**Net return:**

$$
25\% - 2.5\% \times (5-1) = 25\% - 10\% = 15\%
$$

**Funding cost ate 40% of gross return!**

### 4. Negative Carry


**When funding > asset yield:**

$$
\text{Carry} = \text{Asset Yield} - \text{Funding Rate}
$$

**Example:**
- Treasury yield: 1.5%
- Repo rate: 2.0%
- **Carry: -0.5% (negative!)**

**Annual loss from carry:**

$$
-0.5\% \times \text{Borrowed Amount}
$$

**Only profitable if:**
- Capital gain > Negative carry
- Or other strategy benefits (hedge, arbitrage)

### 5. Stress Funding Costs


**Crisis spikes:**

**Normal (2019):**
- GC repo: SOFR + 10 bps = 2.5%
- IG corporate repo: SOFR + 40 bps = 2.8%

**Crisis (March 2020):**
- GC repo: SOFR + 200 bps = 5.0% (2× higher!)
- IG corporate repo: SOFR + 500 bps = 7.0% (2.5× higher!)

**Impact:**
- Holding costs explode
- Negative carry becomes huge
- Forces deleveraging

### 6. Quarter-End Effects


**Reporting date spikes:**

**Normal days:**
- Repo rate: 2.5%

**Quarter-end (last 3 days):**
- Repo rate: 3.5% (100 bp spike)

**Year-end (Dec 31):**
- Repo rate: 5.0% (250 bp spike!)

**Annual impact:**
- 4 quarter-ends × 3 days × 100 bps = 3.3 bps
- 1 year-end × 3 days × 250 bps = 2.1 bps
- **Total drag: ~5-6 bps annually**

**Not huge but predictable**

### 7. Funding Diversification


**Multiple sources:**

**Prime broker financing:**
- Overnight margin loans
- Rate: Fed Funds + 50-100 bps
- Easy but expensive

**Repo market:**
- Bilateral or tri-party
- Rate: SOFR + 10-50 bps
- Cheaper but requires relationships

**Securities lending:**
- Lend securities, receive cash
- Reinvest cash
- Net: Positive if securities special

**Credit lines:**
- Bank credit facilities
- Backup liquidity
- Expensive (unused fee + rate)

---

## Combined Impact


### 1. True Cost of Leverage


**All-in cost:**

$$
\text{Total Cost} = \text{Funding Cost} + \text{Haircut Opportunity Cost} + \text{Margin Maintenance Cost}
$$

**Example:**

**Strategy:** Levered Treasury basis trade
- Position: $\$10M$
- Haircut: 5% (need $\$500K$ equity)
- Funding rate: 2.5%
- ROE target: 15%

**Costs:**

1. **Funding:** $\$10M × 0.025 = $\$250,000$ annually

2. **Haircut opportunity:** $\$500K × 0.15 = $\$75,000$ annually

3. **Margin maintenance:** $\$10,000$ annually (admin, calls)

**Total cost: $\$335,000$ (3.35% of position)**

**Strategy must earn > 3.35% to be profitable**

### 2. Leverage Ratio Calculation


**Effective leverage:**

$$
\text{Effective Leverage} = \frac{\text{Gross Notional}}{\text{Equity at Risk}}
$$

**Equity at risk = Haircut + Potential margin calls**

**Example:**
- Notional: $\$10M$
- Haircut: 5% = $\$500K$
- Expected max margin call: $\$200K$
- **Equity at risk: $\$700K$**
- **Effective leverage: $\$10M / $\$700K = 14.3×$**

**Not $\$10M / $\$500K = 20×$ (naïve calculation)**

### 3. Break-Even Analysis


**Required return:**

$$
\text{Required Return} = \frac{\text{Total Costs}}{\text{Equity}} + \text{Risk-Free Rate}
$$

**Example:**
- Equity: $\$1M$
- Total costs: $\$350K$ annually
- Risk-free: 2%

**Required return:**

$$
\frac{\$350K}{\$1M} + 0.02 = 37\%
$$

**Very high hurdle!**

### 4. Stress Impact


**Normal → Crisis change:**

**Normal case:**
- Haircut: 5%, Funding: 2.5%
- Max leverage: 20×
- Funding cost: 2.5%
- **Net return (assuming 5% asset return, 10× leverage): 25%**

**Crisis case:**
- Haircut: 20%, Funding: 6%
- Max leverage: 5×
- Funding cost: 6%
- **Net return (same 5% asset return, 5× leverage): 1%**

**Return collapsed 96%!**

---

## Common Mistakes


**Pitfalls to avoid:**

### 1. Ignoring Haircut Costs


**Mistake:** Focus only on funding rate

**Why it fails:** Haircut ties up equity

**Example:**
- Think: "2.5% funding is cheap"
- Ignore: 10% haircut = $\$100K$ equity tied up
- Opportunity cost: $\$100K × 15% = $\$15K$ annually
- **Total cost: $\$25K$ + $\$15K$ = $\$40K$ (4% of position!)**

**Fix:** Calculate all-in cost including haircut opportunity cost

### 2. Underestimating Margin Calls


**Mistake:** Only budget for initial margin

**Why it fails:** Variation margin unpredictable

**Example:**
- Initial margin: $\$10K$ (budgeted)
- Market moves 5% against position
- Variation margin: $\$50K$ (surprise!)
- **Cash crunch, forced liquidation**

**Fix:** Reserve 3-5× initial margin for VM

### 3. Assuming Constant Haircuts


**Mistake:** Use normal-market haircuts in models

**Why it fails:** Haircuts spike in stress

**Example:**
- Model with 10% haircut (normal)
- Max leverage: 10×
- Actual crisis haircut: 40%
- Max leverage: 2.5×
- **Forced to deleverage 75%!**

**Fix:** Stress test with 3-5× higher haircuts

### 4. Quarter-End Blindness


**Mistake:** Don't plan for reporting dates

**Why it fails:** Funding costs spike

**Example:**
- Normal funding: 2.5%
- Quarter-end: 5% (for 3 days)
- Position: $\$100M$
- Extra cost: $\$100M × 0.025 × 3/360 = $\$20,833$
- **Unexpected cash drain**

**Fix:** Mark calendar, budget for 2-3× costs

### 5. Overleveraging


**Mistake:** Max out leverage capacity

**Why it fails:** No buffer for stress

**Example:**
- Haircut: 10%, max leverage 10×
- Use full 10× (no buffer)
- Market falls 5%, haircut → 15%
- New max leverage: 6.7×
- **Forced to deleverage 33%**

**Fix:** Use 50-70% of max leverage (keep buffer)

### 6. Funding Concentration


**Mistake:** Single repo dealer

**Why it fails:** Dealer pulls back in stress

**Example:**
- $\$50M$ funded via one dealer
- Crisis: Dealer reduces capacity to $\$10M$
- **Must liquidate $\$40M$ at distressed prices**

**Fix:** 5+ dealers, diversify funding

### 7. Ignoring Negative Carry


**Mistake:** Hold negative carry position too long

**Why it fails:** Bleed from carry compounds

**Example:**
- Negative carry: -0.5% monthly
- Hold 12 months
- **Loss: -6% (even if price unchanged!)**

**Fix:** Exit negative carry trades quickly or have strong directional view

### 8. Poor Margin Forecasting


**Mistake:** Don't model worst-case VM

**Why it fails:** Surprised by cash needs

**Example:**
- Futures position: $\$20M$ notional
- Model 1% daily move (expect $\$200K$ VM)
- Actual crash: 5% move
- Actual VM: $\$1M$ (5× expected)
- **Cash shortage, forced exit**

**Fix:** Model 5-10% moves for VM stress test

---

## Risk Management Rules


### 1. Haircut Limits


**Maximum leverage by asset class:**

- **Treasuries:** Max 10× (10% haircut)
- **IG corporates:** Max 6× (15% haircut)
- **HY corporates:** Max 3× (30% haircut)
- **Equities:** Max 4× (25% haircut)

**Stress capacity:**
- Reserve for haircut doubling
- If normal 10%, reserve for 20%
- Use 50% of max leverage (buffer)

### 2. Margin Reserves


**Cash buffer sizing:**

$$
\text{Reserve} = \text{Initial Margin} \times 3 + \text{Max Expected VM}
$$

**Example:**
- IM: $\$50K$
- Max VM (5% adverse move): $\$200K$
- **Reserve: $\$50K × 3 + $\$200K = $\$350K$**

### 3. Funding Cost Budget


**Maximum annual funding cost:**

$$
\text{Max Funding Cost} \leq 25\% \times \text{Expected Strategy Return}
$$

**Example:**
- Strategy expected return: 8%
- Max funding cost: 2%
- **If funding > 2%, strategy uneconomic**

### 4. Leverage Ratio


**Conservative target:**

$$
\text{Leverage} \leq \min\left(\frac{1}{2\times \text{Haircut}}, \, 5\right)
$$

**Example:**
- Haircut: 10%
- Max: $\min(1/(2×0.10), 5) = \min(5, 5) = 5×$
- **Use maximum 5× leverage**

### 5. Diversification


**Funding sources:**
- Minimum 5 repo dealers
- No single dealer > 30% of funding
- Mix overnight (50%) and term (50%)
- Credit line backup (10% of portfolio)

**Collateral:**
- Multiple asset classes
- Don't rely on single collateral type
- Treasuries always valuable (flight to quality)

### 6. Stress Testing


**Quarterly stress scenarios:**

1. **Haircut shock:**
   - All haircuts double
   - Can still meet requirements?

2. **Funding shock:**
   - Repo rates triple
   - Strategy still profitable?

3. **Margin shock:**
   - 10% adverse move
   - Can meet VM without selling?

4. **Combined shock:**
   - All three together
   - Survival check

### 7. Monitoring Dashboard


**Daily tracking:**
- Current leverage ratio
- Available borrowing capacity
- Funding costs (weighted average)
- Margin utilization
- Cash reserves vs. VM buffer

**Alert triggers:**
- Leverage > 70% of max
- Funding cost > Budget × 1.5
- Cash reserve < 50% of IM
- Haircut increase > 20%

---

## Real-World Examples


### 1. LTCM Collapse (1998)


**Setup:**
- 30× leverage (tiny haircuts)
- Multiple strategies
- Assumed normal haircuts persist

**Crisis:**
- Haircuts spiked 5-10×
- Repo capacity collapsed
- Margin calls: $\$2B$ in one day
- **Couldn't meet calls, liquidated**

**Lesson:** Excessive leverage + stress haircuts = Death

### 2. Lehman Repo Run (2008)


**Setup:**
- Funded via overnight repo
- Collateral: Diverse (some illiquid)

**Crisis (Sept 2008):**
- Repo lenders pulled back
- Haircuts rose dramatically
- Couldn't roll overnight repo
- **Liquidity crisis → Bankruptcy**

**Lesson:** Overnight funding + stress = Disaster

### 3. COVID Margin Calls (March 2020)


**Setup:**
- Many funds running levered strategies
- Normal margins: $\$100K$ per fund

**Crisis:**
- Margins doubled (IM increase)
- VM from adverse moves: $\$500K-1M$ daily
- Many funds received $\$2-5M$ total calls
- **Forced liquidations widespread**

**Lesson:** Margin reserves essential

### 4. Basis Trade Blowup (2020)


**Setup:**
- Treasury basis trades (levered 10-15×)
- Haircut: 5%
- Funding: 1.8%

**Crisis:**
- Haircut → 15% (3× higher)
- Funding → 5% (3× higher)
- Max leverage: 6.7× (down from 20×)
- **Forced to deleverage 50%+**

**Outcome:**
- Sell into illiquid market
- Realized losses
- Many funds lost 20-40%

**Lesson:** Stress capacity planning crucial

### 5. GameStop Margin Freeze (Jan 2021)


**Setup:**
- Retail buying frenzy
- Brokers allowing margin

**Crisis:**
- Margin requirements spiked 100%
- Clearing houses demanded extra capital
- Brokers froze buying (couldn't fund)
- **Customers angry but necessary**

**Lesson:** System-wide margin stress affects everyone

---

## Practical Steps


### 1. Calculate True Cost


**Comprehensive cost model:**

```python
def calculate_true_cost(position_size, haircut, funding_rate, 
                        roe_target, term_days):
    # Borrowing capacity
    equity_needed = position_size * haircut
    borrowed = position_size - equity_needed
    
    # Funding cost
    funding_cost = borrowed * funding_rate * term_days / 360
    
    # Haircut opportunity cost
    opportunity_cost = equity_needed * roe_target * term_days / 360
    
    # Administrative (margin calls, operations)
    admin_cost = 0.001 * position_size  # 10 bps
    
    # Total
    total_cost = funding_cost + opportunity_cost + admin_cost
    
    # As percentage
    cost_pct = total_cost / position_size
    
    return {
        'funding_cost': funding_cost,
        'opportunity_cost': opportunity_cost,
        'admin_cost': admin_cost,
        'total_cost': total_cost,
        'cost_pct': cost_pct
    }

# Example
costs = calculate_true_cost(
    position_size=10_000_000,
    haircut=0.10,
    funding_rate=0.025,
    roe_target=0.15,
    term_days=90
)

print(f"Total cost: ${costs['total_cost']:,.0f}")
print(f"Cost %: {costs['cost_pct']:.2%}")
```

### 2. Margin Reserve Planning


**Buffer calculation:**

```python
def calculate_margin_reserve(notional, initial_margin_pct, 
                             max_adverse_move_pct):
    # Initial margin
    initial_margin = notional * initial_margin_pct
    
    # Max variation margin
    max_vm = notional * max_adverse_move_pct
    
    # Reserve (3× IM + max VM)
    reserve = 3 * initial_margin + max_vm
    
    return {
        'initial_margin': initial_margin,
        'max_vm': max_vm,
        'required_reserve': reserve,
        'reserve_pct': reserve / notional
    }

# Example
reserve = calculate_margin_reserve(
    notional=20_000_000,
    initial_margin_pct=0.05,
    max_adverse_move_pct=0.10
)

print(f"Required reserve: ${reserve['required_reserve']:,.0f}")
print(f"As % of notional: {reserve['reserve_pct']:.1%}")
```

### 3. Stress Testing


**Haircut shock scenario:**

```python
def haircut_stress_test(position, normal_haircut, equity):
    # Normal capacity
    normal_max = position / (1 - normal_haircut)
    normal_leverage = position / equity
    
    # Stress haircuts (3× higher)
    stress_haircut = min(normal_haircut * 3, 0.80)
    stress_max = equity / stress_haircut
    
    # Required deleveraging
    excess = position - stress_max
    deleverage_pct = excess / position if excess > 0 else 0
    
    return {
        'normal_leverage': normal_leverage,
        'normal_max': normal_max,
        'stress_haircut': stress_haircut,
        'stress_max': stress_max,
        'excess_position': max(0, excess),
        'deleverage_pct': deleverage_pct
    }

# Example
stress = haircut_stress_test(
    position=10_000_000,
    normal_haircut=0.10,
    equity=1_000_000
)

print(f"Must deleverage: {stress['deleverage_pct']:.1%}")
print(f"Must sell: ${stress['excess_position']:,.0f}")
```

### 4. Position Sizing


**Maximum safe position:**

```python
def max_safe_position(equity, haircut, stress_multiplier, 
                     target_leverage_utilization=0.70):
    # Max in theory
    max_theoretical = equity / haircut
    
    # Max under stress
    stress_haircut = min(haircut * stress_multiplier, 0.80)
    max_stress = equity / stress_haircut
    
    # Safe position (70% of stress capacity)
    safe_position = max_stress * target_leverage_utilization
    
    return {
        'max_theoretical': max_theoretical,
        'max_stress': max_stress,
        'recommended': safe_position,
        'recommended_leverage': safe_position / equity
    }

# Example
sizing = max_safe_position(
    equity=1_000_000,
    haircut=0.10,
    stress_multiplier=3
)

print(f"Recommended position: ${sizing['recommended']:,.0f}")
print(f"Leverage: {sizing['recommended_leverage']:.1f}×")
```

---

## Final Wisdom


> "Haircuts, margin, and funding costs are the friction that converts theoretical leverage into real-world returns - and this friction increases 3-10× during stress when you need it most. The 2008 crisis showed that 2% Treasury haircuts can become 10%, 10% corporate haircuts can become 50%, and 2% funding costs can become 7%. LTCM's 30× leverage worked beautifully until haircuts spiked and it didn't. The key lessons: (1) stress-test assuming haircuts triple and funding costs double, (2) maintain margin reserves of 3-5× initial margin to handle variation margin shocks, (3) diversify funding across 5+ dealers so no single relationship is critical, and (4) use 50-70% of maximum leverage capacity to keep buffer for stress. Remember: Leverage is rented not owned - the landlord (your prime broker) can change terms dramatically when markets turn."

**Key to success:**

- **Calculate true cost:** Funding + haircut opportunity cost + margin admin = 2-5% annually, not just repo rate
- **Stress haircuts:** Assume 3× increase during crisis (10% → 30%), test if can survive
- **Margin reserves:** Keep cash = 3× initial margin + max expected VM, don't assume only IM needed
- **Conservative leverage:** Use 50-70% of max capacity (if 10% haircut allows 10×, use 5-7×)
- **Diversify funding:** 5+ repo dealers, no single source > 30%, mix overnight and term
- **Quarter-end planning:** Repo rates spike 100-250 bps for 3 days each quarter/year, budget accordingly
- **Monitor daily:** Track leverage ratio, available capacity, funding costs, margin utilization, cash reserves
- **Remember:** Stress makes everything worse simultaneously - haircuts up, funding costs up, margin calls up, leverage down
