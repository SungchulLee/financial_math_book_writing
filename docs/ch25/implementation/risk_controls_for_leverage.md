# Risk Controls for Leverage


**Risk controls for leverage** are the policies, limits, and monitoring systems that prevent excessive risk-taking through borrowed capital, protecting portfolios from catastrophic losses when markets turn against levered positions.

---

## The Core Insight


**The fundamental idea:**

- Leverage amplifies both gains and losses
- Small adverse move + high leverage = Catastrophic loss
- Need hard limits to prevent disaster
- Monitor continuously (not just monthly)
- Stress test regularly
- Preserve capital = Survival

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/leverage_controls.png?raw=true" alt="leverage_controls" width="700">
</p>
**Figure 1:** Leverage ratio and loss scenarios showing how 10× leverage turns 10% market decline into 100% portfolio wipeout, while 3× leverage maintains 70% capital preservation, demonstrating critical importance of leverage limits.

**You're essentially asking: "How do I safely use leverage without blowing up my account?"**

---

## Fundamental Leverage Concepts


### 1. Leverage Definition


**Gross leverage:**

$$
\text{Leverage} = \frac{\text{Gross Notional}}{\text{Equity}}
$$

**Example:**
- Positions: $\$10M$ notional
- Equity: $\$2M$
- **Leverage: 5×**

**Net leverage:**

$$
\text{Net Leverage} = \frac{\text{Net Exposure}}{\text{Equity}}
$$

**Example:**
- Long: $\$10M$
- Short: $\$6M$
- Net: $\$4M$
- Equity: $\$2M$
- **Net leverage: 2×**

### 2. Loss Magnification


**Leverage multiplier:**

$$
\text{Portfolio Loss \%} = \text{Market Loss \%} \times \text{Leverage}
$$

**Examples:**

**2× leverage:**
- Market: -5%
- Portfolio: -10%

**5× leverage:**
- Market: -10%
- Portfolio: -50%

**10× leverage:**
- Market: -10%
- Portfolio: -100% (wipeout!)

**30× leverage (LTCM):**
- Market: -3.3%
- Portfolio: -100% (wipeout!)

### 3. Return Impact


**Positive leverage:**

$$
\text{Return} = r_{\text{asset}} \times L - r_{\text{funding}} \times (L-1)
$$

Where:
- $r_{\text{asset}}$ = Asset return
- $r_{\text{funding}}$ = Funding cost
- $L$ = Leverage ratio

**Example:**
- Asset: 8% return
- Funding: 3%
- Leverage: 5×

**Return:**

$$
8\% \times 5 - 3\% \times 4 = 40\% - 12\% = 28\%
$$

**But if asset returns -5%:**

$$
-5\% \times 5 - 3\% \times 4 = -25\% - 12\% = -37\%
$$

### 4. Maximum Safe Leverage


**Kelly Criterion adaptation:**

$$
L^* = 1 + \frac{\mu - r_f}{\sigma^2}
$$

Where:
- $\mu$ = Expected return
- $r_f$ = Funding rate
- $\sigma$ = Volatility

**Example:**
- $\mu = 10\%$
- $r_f = 3\%$
- $\sigma = 15\%$

**Optimal leverage:**

$$
L^* = 1 + \frac{0.10 - 0.03}{0.15^2} = 1 + \frac{0.07}{0.0225} = 4.1×
$$

**But Kelly is aggressive; use 50% Kelly:**

**Safe leverage: $2.0×$**

### 5. Time to Ruin


**Expected time until wipeout:**

$$
T_{\text{ruin}} = \frac{1}{p \times f}
$$

Where:
- $p$ = Probability of loss exceeding capital
- $f$ = Trading frequency

**Example:**
- 10× leverage
- 10% adverse move = Wipeout
- Probability: 2% monthly
- **Time to ruin: $1/(0.02 \times 12) = 4.2$ years**

**Lower leverage extends survival:**
- 5× leverage: 10 years
- 3× leverage: 50 years
- 2× leverage: Never (practically)

### 6. Volatility Scaling


**Adjust leverage to volatility:**

$$
L(t) = L_{\text{base}} \times \frac{\sigma_{\text{target}}}{\sigma_t}
$$

**Example:**
- Base leverage: 5×
- Target vol: 10%
- Current vol: 20%
- **Adjusted: $5 × (10\%/20\%) = 2.5×$**

**Reduces leverage when risk rises**

### 7. Drawdown Dynamics


**Maximum drawdown with leverage:**

$$
\text{DD}_{\text{levered}} = 1 - (1 - \text{DD}_{\text{unlevered}})^L
$$

**Example:**
- Unlevered max DD: 20%
- Leverage: 3×

**Levered DD:**

$$
1 - (1-0.20)^3 = 1 - 0.512 = 48.8\%
$$

**Much worse than $20\% × 3 = 60\%$ (linear assumption)**

---

## Core Risk Limits


### 1. Gross Leverage Limit


**Maximum ratio:**

$$
\text{Max Gross Leverage} = \min\left(5, \, \frac{1}{2\times \text{Haircut}}\right)
$$

**By asset class:**
- **Treasuries:** Max 5× (low vol)
- **IG corporates:** Max 4× (moderate vol)
- **Equities (diversified):** Max 3× (higher vol)
- **HY/EM:** Max 2× (high vol)

**Example:**
- Portfolio: IG corporates
- Haircut: 10%
- Theoretical max: 10×
- **Safe limit: 4× (conservatively)**

### 2. Net Leverage Limit


**Separate tracking:**

$$
\text{Max Net Leverage} \leq \text{Max Gross Leverage} \times 0.60
$$

**Example:**
- Max gross: 5×
- **Max net: 3×**

**Rationale:**
- Hedges aren't perfect
- Correlation breaks in stress
- Need cushion

### 3. VaR Limit


**Risk-based constraint:**

$$
\text{Leverage} \leq \frac{\text{Max Acceptable Loss}}{\text{VaR per Unit}}
$$

**Example:**
- Max loss: 20% of equity
- 1-day VaR (unleveraged): 2%
- **Max leverage: $20\% / 2\% = 10×$**

**But apply safety factor (0.5):**

**Practical limit: 5×**

### 4. Concentration Limit


**Single position cap:**

$$
\text{Max Position} = \text{Equity} \times \text{Max Leverage} \times 0.20
$$

**Example:**
- Equity: $\$10M$
- Max leverage: 5×
- Max gross exposure: $\$50M$
- **Max single position: $\$10M$ (20%)**

### 5. Sector/Geography Limits


**Diversification requirements:**

- Max 40% in single sector
- Max 30% in single country (ex-US)
- Max 50% in single currency
- Max 60% in single asset class

**Prevents concentrated blowup**

### 6. Liquidity-Adjusted Limit


**Account for liquidation:**

$$
\text{Max Position} = \text{Daily Volume} \times \text{Max Days} \times 0.30
$$

**Example:**
- Daily volume: $\$10M$
- Max liquidation: 10 days
- **Max position: $\$10M × 10 × 0.30 = $\$30M$**

**Ensures can exit in stress (at 30% of normal volume)**

### 7. Correlation Adjustment


**Leverage scaling:**

$$
L_{\text{adj}} = L_{\text{base}} \times (1 - \rho_{\text{avg}})
$$

**Example:**
- Base max leverage: 5×
- Average correlation: 0.70 (high!)
- **Adjusted: $5 × (1-0.70) = 1.5×$**

**High correlation = Less diversification = Lower leverage**

---

## Dynamic Controls


### 1. Drawdown-Based


**Reduce leverage after losses:**

$$
L(t) = L_{\text{max}} \times \max\left(0, \, 1 - \frac{\text{DD}_t}{\text{DD}_{\text{max}}}\right)
$$

**Example:**
- Max leverage: 5×
- Max allowed DD: 20%
- Current DD: 10%

**Current leverage:**

$$
5 × \left(1 - \frac{10\%}{20\%}\right) = 5 × 0.5 = 2.5×
$$

**Halved leverage due to losses**

### 2. Volatility-Based


**Scale to target volatility:**

$$
L(t) = L_{\text{base}} \times \frac{\sigma_{\text{target}}}{\sigma_{\text{realized}}}
$$

**Daily recalculation:**

```python
def calculate_leverage(base_leverage, target_vol, realized_vol):
    # 20-day realized volatility
    current_vol = realized_vol[-20:].std() * np.sqrt(252)
    
    # Adjusted leverage
    adjusted = base_leverage * (target_vol / current_vol)
    
    # Cap at max
    return min(adjusted, base_leverage * 1.5)
```

### 3. VIX-Triggered


**Market stress adjustment:**

$$
L(t) = L_{\text{max}} \times \begin{cases}
1.0 & \text{if VIX} < 15 \\
0.75 & \text{if } 15 \leq \text{VIX} < 25 \\
0.50 & \text{if } 25 \leq \text{VIX} < 35 \\
0.25 & \text{if } 35 \leq \text{VIX} < 50 \\
0.0 & \text{if VIX} \geq 50
\end{cases}
$$

**Example:**
- Max leverage: 6×
- VIX = 30
- **Current: $6 × 0.50 = 3×$**

### 4. Margin Utilization


**Preserve buffer:**

$$
L(t) = L_{\text{max}} \times \left(1 - \frac{\text{Margin Used}}{\text{Margin Available}}\right)
$$

**Example:**
- Max leverage: 5×
- Margin used: 60% of available
- **Current: $5 × (1 - 0.60) = 2×$**

### 5. P&L-Based


**Lock in gains:**

$$
L(t) = L_{\text{base}} \times \left(1 + 0.5 \times \frac{\text{YTD Gain}}{\text{Initial Equity}}\right)^{-1}
$$

**Example:**
- Base: 4×
- YTD gain: +20%
- **Current: $4 / (1 + 0.5 × 0.20) = 3.6×$**

**Reduce leverage after gains (protect profits)**

### 6. Time-Based


**Cycle awareness:**

$$
L(t) = L_{\text{base}} \times \text{Cycle Factor}(t)
$$

**Example:**
- Early bull market: 1.2× (increase)
- Late bull market: 0.8× (reduce)
- Bear market: 0.5× (cut)
- Crisis: 0.2× (minimal)

### 7. Regime Switching


**Detect regime changes:**

```python
def regime_detection(returns, window=60):
    # Markov switching model or simpler:
    recent_vol = returns[-window:].std()
    long_vol = returns.std()
    
    if recent_vol > 1.5 * long_vol:
        return 'high_vol'  # Reduce leverage
    elif recent_vol < 0.7 * long_vol:
        return 'low_vol'   # Can increase leverage
    else:
        return 'normal'    # Base leverage

# Adjust leverage by regime
leverage_multipliers = {
    'low_vol': 1.2,
    'normal': 1.0,
    'high_vol': 0.6
}
```

---

## Monitoring Systems


### 1. Real-Time Dashboard


**Key metrics (updated constantly):**

- Current gross leverage
- Current net leverage
- Available borrowing capacity
- Margin utilization %
- VaR (1-day, 10-day)
- Largest position (% of equity)
- Correlation matrix
- Liquidity score

### 2. Alert Triggers


**Immediate action required:**

**Level 1 (Warning):**
- Leverage > 80% of max
- VaR > 15% of equity (1-day)
- Margin used > 75%
- Largest position > 25%

**Level 2 (Urgent):**
- Leverage > 90% of max
- VaR > 20% of equity
- Margin used > 85%
- Correlation > 0.80

**Level 3 (Critical):**
- Leverage > 100% of max (breach!)
- VaR > 25% of equity
- Margin call received
- Cannot meet funding

### 3. Daily Reporting


**End-of-day review:**

```
LEVERAGE REPORT - [DATE]
==================================================
Gross Leverage:        3.2× (Limit: 5×)    ✓
Net Leverage:          1.8× (Limit: 3×)    ✓
1-Day VaR:            $250K (Limit: $500K) ✓
Margin Used:           62% (Limit: 80%)    ✓
Largest Position:      18% (Limit: 20%)    ✓
Avg Correlation:       0.45 (Watch: 0.60)  ✓

STATUS: ALL CLEAR
==================================================
```

### 4. Weekly Stress Test


**Scenario analysis:**

**Scenario 1: Market selloff**
- Equities: -10%
- Bonds: -2%
- Result: Portfolio -18%, leverage → 3.8×
- Action: None (within limits)

**Scenario 2: Volatility spike**
- VIX: 20 → 40
- Haircuts double
- Result: Max leverage → 2.5×, need deleverage 20%
- Action: Prepare to reduce positions

**Scenario 3: Funding stress**
- Repo unavailable
- Result: Cannot roll, forced liquidation
- Action: CRITICAL - diversify funding

### 5. Monthly Risk Review


**Comprehensive analysis:**

- Historical leverage vs. performance
- VaR backtesting (actual vs. predicted)
- Limit breaches (if any)
- Stress test results
- Correlation changes
- Liquidity assessment
- Funding sources review
- Recommendations for limit changes

### 6. Limit Exception Process


**Rare breaches:**

1. **Identify breach:**
   - Auto-alert triggered
   - Risk team notified

2. **Document reason:**
   - Market move?
   - Position error?
   - Funding change?

3. **Remediation plan:**
   - Immediate (hours)
   - Short-term (days)
   - Permanent fix

4. **Executive approval:**
   - CRO signoff required
   - Board notification if material

### 7. Backtesting


**Quarterly validation:**

```python
def backtest_var(portfolio_returns, var_estimates, confidence=0.99):
    # Number of breaches
    breaches = (portfolio_returns < -var_estimates).sum()
    
    # Expected breaches
    expected = len(portfolio_returns) * (1 - confidence)
    
    # Statistical test
    breach_rate = breaches / len(portfolio_returns)
    
    if breach_rate > (1-confidence) * 1.5:
        return "FAIL - VaR model inadequate"
    else:
        return "PASS - VaR model adequate"
```

---

## Common Mistakes


**Pitfalls to avoid:**

### 1. Static Leverage


**Mistake:** Set leverage once, never adjust

**Why it fails:** Markets change

**Example:**
- Start: 5× leverage, VIX = 15 (calm)
- Crisis: VIX = 45 (chaos)
- Still 5× levered
- **Losses catastrophic**

**Fix:** Dynamic leverage based on volatility/VIX

### 2. Gross-Only Focus


**Mistake:** Monitor gross, ignore net

**Why it fails:** Hedges fail in stress

**Example:**
- Gross: 10× (5× long, 5× short)
- Net: 0.5× (nearly hedged)
- Think: "Safe, low net leverage"
- Crisis: Correlation → 1, both sides lose
- **Massive losses despite low net**

**Fix:** Monitor both gross and net

### 3. No Stress Testing


**Mistake:** Assume normal conditions

**Why it fails:** Stress happens

**Example:**
- VaR: 2% (99%, 1-day)
- Leverage: 10×
- Think: "Max loss 20%"
- Actual stress: 10% move (5-sigma)
- **Loss: 100% (wipeout)**

**Fix:** Stress test 5-10 sigma events

### 4. Ignoring Correlation


**Mistake:** Diversify then lever up

**Why it fails:** Correlation rises in stress

**Example:**
- 10 positions, correlation 0.3 (normal)
- Leverage: 5× (think diversified)
- Stress: Correlation → 0.9
- Effective positions: 2-3 (not 10!)
- **Losses concentrated**

**Fix:** Adjust leverage for stress correlation

### 5. Overleveraging Winners


**Mistake:** Add leverage after gains

**Why it fails:** Mean reversion

**Example:**
- Start: 3×, up 50%
- Increase to 6× (feeling invincible)
- Market reverses
- **Give back all gains + principal**

**Fix:** Reduce leverage after gains (lock in)

### 6. No Liquidity Check


**Mistake:** Lever illiquid positions

**Why it fails:** Can't exit in stress

**Example:**
- Small-cap stocks, 10× levered
- Crisis: Margin call
- Try to sell: No bids
- **Forced liquidation at terrible prices**

**Fix:** Leverage only liquid positions

### 7. Assuming Unlimited Funding


**Mistake:** No funding contingency

**Why it fails:** Repo seizes in stress

**Example:**
- 8× leverage, overnight repo
- Crisis: Dealers pull back
- Can't roll funding
- **Forced liquidation**

**Fix:** Secure term funding, multiple sources

### 8. Reactive Deleveraging


**Mistake:** Wait for margin call

**Why it fails:** Too late, worst prices

**Example:**
- Leverage at max (5×)
- Market falls 15%
- Margin call
- Forced to sell at lows
- **Realize losses**

**Fix:** Preemptive deleveraging (reduce at 80% of max)

---

## Risk Management Rules


### 1. Maximum Leverage Matrix


**By asset class and account size:**

| Asset Class | <$1M | $1-10M | >$10M |
|-------------|------|---------|--------|
| Treasuries  | 3×   | 4×      | 5×     |
| IG Corp     | 2×   | 3×      | 4×     |
| Equities    | 2×   | 2.5×    | 3×     |
| HY/EM       | 1.5× | 2×      | 2×     |

**Larger accounts get slightly more leverage (sophistication)**

### 2. Leverage Ramp


**Gradual increase:**

- **Month 1-3:** Max 2× (learning)
- **Month 4-6:** Max 3× (gaining confidence)
- **Month 7-12:** Max 4× (experienced)
- **Year 2+:** Max 5× (proven track record)

**Don't start at max leverage**

### 3. Volatility Budget


**Target portfolio volatility:**

$$
\sigma_{\text{portfolio}} = \sigma_{\text{assets}} \times L \leq \sigma_{\text{target}}
$$

**Example:**
- Asset volatility: 10%
- Target portfolio vol: 15%
- **Max leverage: $15\% / 10\% = 1.5×$**

**Keeps risk constant**

### 4. Stop-Loss Integration


**Forced deleveraging:**

- **Loss > 10%:** Reduce leverage by 25%
- **Loss > 20%:** Reduce leverage by 50%
- **Loss > 30%:** Exit all leverage (1× only)

**Example:**
- Start: 5× leverage
- Down 15%: Cut to 3.75×
- Down 25%: Cut to 2.5×
- Down 35%: Cut to 1.0×

### 5. Funding Diversity


**Required sources:**

- Minimum 5 repo dealers
- No single source > 30%
- Term funding ≥ 50% in normal times
- Term funding ≥ 70% in stress
- Credit line = 10% of portfolio (backup)

### 6. Margin Buffer


**Never use 100% of capacity:**

$$
\text{Used Margin} \leq 75\% \times \text{Available Margin}
$$

**Reserves for:**
- Variation margin (adverse moves)
- Initial margin increases
- Emergency needs

### 7. Quarterly Audit


**Independent review:**

- Limit compliance (any breaches?)
- Stress test adequacy
- Model performance (VaR accuracy)
- Control effectiveness
- Recommendations for changes

---

## Real-World Examples


### 1. LTCM (1998)


**Setup:**
- Leverage: 25-30× (extreme!)
- Nobel laureates running it
- "Sophisticated models"

**Crisis:**
- Russian default
- Spreads widened
- Margin calls: Billions
- **Total collapse, Fed rescue**

**Lesson:** Even geniuses fail with excessive leverage

### 2. Bear Stearns Hedge Funds (2007)


**Setup:**
- Subprime mortgage funds
- Leverage: 10-15×
- "Investment grade assets"

**Crisis:**
- Mortgage values fell 10%
- Levered loss: 100%+
- Margin calls: Couldn't meet
- **Liquidated, total loss**

**Lesson:** Leverage magnifies small moves

### 3. Archegos (2021)


**Setup:**
- Total return swaps (hidden leverage)
- Leverage: 5-7× (estimated)
- Concentrated positions

**Crisis:**
- ViacomCBS capital raise
- Stock fell 25%
- Margin call: $\$20B+
- **Forced liquidation, -$\$10B loss**

**Lesson:** Concentrated + leverage = Disaster

### 4. Disciplined Fund (2008-2020)


**Setup:**
- Max leverage: 3×
- Dynamic adjustment (VIX-based)
- Diversified funding

**2008 Crisis:**
- Reduced leverage 3× → 1.5×
- Survived, down 25% (peers -60%)

**2020 COVID:**
- Reduced leverage 3× → 1.5×
- Survived, down 15% (peers -40%)

**Outcome:**
- 12-year track record
- Annualized: 12% (vs. 8% unleveraged)
- **Max DD: -25% (vs. -15% unleveraged)**

**Lesson:** Conservative leverage + discipline = Survival

### 5. Vol Control Funds (2010s)


**Strategy:**
- Target 10% volatility
- Adjust leverage daily
- VIX-based scaling

**Performance:**
- Consistent returns (8-12% annually)
- Low volatility (10% realized)
- Survived 2011, 2015, 2018, 2020 selloffs
- **Max DD: -15%**

**Lesson:** Volatility-targeting works

---

## Practical Steps


### 1. Implement Leverage Ladder


**Tiered system:**

```python
def calculate_leverage_limit(equity, risk_tolerance, experience):
    # Base limit
    base = {
        'conservative': 2,
        'moderate': 3,
        'aggressive': 4
    }[risk_tolerance]
    
    # Experience adjustment
    exp_factor = min(experience / 2, 1.5)  # Cap at 1.5×
    
    # Size adjustment (smaller = lower)
    size_factor = min(equity / 1_000_000, 1.0)
    
    # Combined
    max_leverage = base * exp_factor * size_factor
    
    return round(max_leverage, 1)

# Example
limit = calculate_leverage_limit(
    equity=500_000,
    risk_tolerance='moderate',
    experience=1  # years
)
print(f"Max leverage: {limit}×")  # e.g., 2.0×
```

### 2. Dynamic Adjustment System


**Real-time scaling:**

```python
def adjust_leverage(base_leverage, vix, realized_vol, 
                   target_vol, drawdown, max_dd):
    # VIX adjustment
    if vix < 15:
        vix_factor = 1.0
    elif vix < 25:
        vix_factor = 0.75
    elif vix < 35:
        vix_factor = 0.50
    else:
        vix_factor = 0.25
    
    # Volatility adjustment
    vol_factor = target_vol / max(realized_vol, target_vol)
    
    # Drawdown adjustment
    dd_factor = max(0, 1 - drawdown / max_dd)
    
    # Combined (take most conservative)
    factor = min(vix_factor, vol_factor, dd_factor)
    
    return base_leverage * factor

# Example
current = adjust_leverage(
    base_leverage=4.0,
    vix=30,
    realized_vol=0.18,
    target_vol=0.12,
    drawdown=0.08,
    max_dd=0.20
)
print(f"Adjusted leverage: {current:.1f}×")
```

### 3. Risk Monitoring Dashboard


**Daily tracking:**

```python
import pandas as pd

def risk_dashboard(positions, equity, limits):
    # Calculate metrics
    gross_notional = positions['notional'].abs().sum()
    net_notional = positions['notional'].sum()
    gross_leverage = gross_notional / equity
    net_leverage = abs(net_notional) / equity
    
    # Largest position
    max_position_pct = positions['notional'].abs().max() / equity
    
    # Check limits
    checks = {
        'Gross Leverage': (gross_leverage, limits['max_gross'], 
                           gross_leverage <= limits['max_gross']),
        'Net Leverage': (net_leverage, limits['max_net'],
                         net_leverage <= limits['max_net']),
        'Max Position': (max_position_pct, limits['max_position'],
                         max_position_pct <= limits['max_position'])
    }
    
    # Display
    print("RISK DASHBOARD")
    print("=" * 60)
    for metric, (value, limit, ok) in checks.items():
        status = "✓" if ok else "✗ BREACH"
        print(f"{metric:20s}: {value:5.2f} (Limit: {limit:.2f}) {status}")
    
    return checks

# Usage
dashboard = risk_dashboard(
    positions=portfolio_df,
    equity=1_000_000,
    limits={'max_gross': 4.0, 'max_net': 2.5, 'max_position': 0.25}
)
```

---

## Final Wisdom


> "Leverage is the most powerful tool in finance and the most dangerous. It has created fortunes and destroyed more. The difference between success and catastrophe isn't intelligence or market insight - it's discipline in leverage limits. LTCM had two Nobel laureates and failed at 30× leverage. The Medallion Fund uses 1-2× leverage and has never had a down year in 30+ years. The lesson is clear: conservative leverage (2-4×), dynamic adjustment to volatility, hard limits that aren't violated, stress testing for 5-10 sigma events, and preemptive deleveraging before forced liquidations. The goal isn't to maximize returns (leverage → ∞) but to maximize long-run wealth (survival × compounding). As Warren Buffett says: 'Rule 1 is don't lose money. Rule 2 is don't forget rule 1.' Leverage makes both rules harder to follow."

**Key to success:**

- **Conservative base:** Max 2-4× leverage for most strategies (not 10-30× like LTCM, Archegos)
- **Dynamic adjustment:** Scale leverage inversely with volatility (VIX-based or realized vol)
- **Hard limits enforced:** Not suggestions - automatic deleveraging when breached
- **Stress test regularly:** Assume 5-10 sigma events (2008, 2020 showed they happen)
- **Diversify funding:** 5+ sources, no single dependency, 50%+ term funding
- **Monitor continuously:** Daily dashboard, real-time alerts, don't wait for month-end
- **Preemptive deleveraging:** Reduce at 80% of limits (don't wait for forced margin call)
- **Remember:** More funds die from overleveraging than bad strategy - survival beats optimization
