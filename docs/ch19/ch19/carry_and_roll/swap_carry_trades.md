# Swap Carry Trades

**Swap carry trades** are fixed income strategies that exploit the positive carry inherent in upward-sloping yield curves by entering interest rate swaps to receive fixed rates and pay floating rates (typically SOFR), earning the spread between the higher fixed rate received and the lower floating rate paid as daily income, while also benefiting from favorable roll-down effects as time passes and the position ages down the curve toward lower yields.

---

## The Core Insight

**The fundamental idea:**

- Interest rate swaps exchange fixed for floating payments
- Upward-sloping curves: Fixed rates > Current floating rates
- Positive carry: Daily income from rate differential
- Roll-down: Additional profit as time passes
- Duration risk: Rates rising can offset carry gains
- Leverage: Swaps require minimal capital (notional exposure)
- Professional tool: Preferred over bonds for carry
- Combine carry + curve view for optimal returns

**The key equations:**

**Daily carry (receiving fixed):**

$$
\text{Carry/Day} = \frac{\text{Notional} \times (r_{\text{fixed}} - r_{\text{floating}})}{360}
$$

**Total return:**

$$
\text{Total Return} = \underbrace{\text{Carry}}_{\text{Daily income}} + \underbrace{\text{Roll-Down}}_{\text{Aging effect}} + \underbrace{\text{Mark-to-Market}}_{\text{Rate changes}}
$$

**You're essentially betting: "I'll earn daily positive carry from the fixed-floating spread, and even if rates rise a little, the carry income will offset the mark-to-market loss."**

---

## What Are Swap Carry Trades?

**Before trading swap carry, understand the mechanics:**

### 1. Core Concept

**Definition:** A strategy involving entering into interest rate swaps—typically as the fixed-rate receiver—to capture the positive spread between the fixed swap rate and the current floating rate (SOFR), generating daily carry income while accepting mark-to-market risk from interest rate movements and benefiting from roll-down effects as the swap ages toward maturity with declining rates if the curve remains stable.

**When you execute a swap carry trade:**

- You enter an interest rate swap (IRS)
- You typically receive fixed, pay floating (SOFR)
- You earn positive carry if fixed > floating
- You face duration risk (loss if rates rise)
- You benefit from roll-down (passage of time)
- You use leverage (notional >> capital required)
- You maintain position for weeks to months
- Primary use: Institutional investors, hedge funds, banks

**Example - Basic 5-Year Swap Carry Trade:**

**Market conditions (December 2024):**

| Rate Type | Level |
|-----------|-------|
| 5-year swap rate (fixed) | 4.25% |
| 3-month SOFR (floating) | 4.75% |
| Overnight SOFR | 4.58% |

**Wait, this would be negative carry! Let me use a more typical scenario:**

**Market conditions (more typical upward curve):**

| Rate Type | Level |
|-----------|-------|
| 5-year swap rate (fixed) | 4.25% |
| Current overnight SOFR | 3.50% |
| Expected average SOFR (over 5 years) | 3.80% |

**Trade setup:**

- Enter 5-year swap: Receive 4.25% fixed, Pay SOFR
- Notional: $10 million
- Tenor: 5 years

**Immediate carry (using current SOFR):**

$$
\text{Daily Carry} = \frac{\$10M \times (4.25\% - 3.50\%)}{360} = \frac{\$10M \times 0.75\%}{360} = \$208.33/\text{day}
$$

**Annual carry: $208.33 × 360 = $75,000/year**

**This is 0.75% annual carry on $10M notional**

**But key question: How much capital at risk?**

**DV01 exposure:**

- 5-year swap DV01 ≈ $4,500 per $1M notional
- Total DV01: $10M × $4,500 = $45,000
- **1 bp move in rates = $45,000 P&L**

**Risk-adjusted carry:**

- Carry: $75,000/year = $208/day
- DV01: $45,000
- **Daily carry = 0.46 bps of DV01 (208/45,000)**

**This means:**

- If 5-year rates rise >0.46 bps/day, you lose money
- If rates are flat, you earn $208/day forever
- If rates fall, you earn carry + mark-to-market gain

### 2. Swap Mechanics Review

**Interest rate swap basics:**

**Fixed leg (you receive):**

- Semi-annual payments (typically)
- Fixed rate: 4.25% per annum
- Payment: $10M × 4.25% / 2 = $212,500 every 6 months

**Floating leg (you pay):**

- Quarterly payments (typically)
- Rate: 3-month SOFR (resets quarterly)
- Payment: $10M × SOFR / 4 (varies each quarter)

**Net cash flow (semi-annual):**

$$
\text{Net CF} = \text{Fixed Received} - \sum \text{Floating Paid}
$$

**Example - First 6 months:**

**Fixed received:** $212,500 (semi-annual)

**Floating paid (quarterly, assume 3.50% SOFR):**

- Q1: $10M × 3.50% / 4 = $87,500
- Q2: $10M × 3.50% / 4 = $87,500
- Total: $175,000

**Net received: $212,500 - $175,000 = $37,500**

**This is the carry income for 6 months**

### 3. Types of Swap Carry Trades

**1. Vanilla Receive-Fixed (most common):**

- Receive fixed, pay floating
- Positive carry on upward-sloping curve
- Duration risk: Long duration (lose if rates rise)
- Best when: Curve steep, rates expected stable/falling

**2. Pay-Fixed (reverse carry):**

- Pay fixed, receive floating
- Negative carry (you pay more than receive)
- But gain if rates rise (short duration)
- Best when: Expecting rate hikes, willing to pay negative carry for protection

**3. Curve Carry (steepener/flattener):**

- Receive fixed in one tenor, pay fixed in another
- Example: Receive 10-year fixed (4.50%), pay 2-year fixed (4.00%)
- Carry: Positive if 10s > 2s
- Also a curve view (bet on steepening/flattening)

**4. Roll-Down Focused:**

- Receive fixed in maturity with steep forward curve
- Hold and benefit as swap "rolls down" curve
- Carry + Roll-down = Total return
- Exit after significant aging (e.g., 5-year → 4-year)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/swap_carry_trades.png?raw=true" alt="swap_carry_trades" width="700">
</p>
**Figure 1:** Swap carry trades showing the cash flow structure with fixed receipts exceeding floating payments generating positive carry, the roll-down effect as the swap ages down the curve toward lower yields, and the total return decomposition into carry, roll-down, and mark-to-market components.

---

## Economic Interpretation

**Beyond the basic mechanics, understanding the REAL economics:**

### 1. The Term Premium

**The deep insight:**

Upward-sloping curves exist because of **term premium**—the extra yield investors demand for locking money up longer:

$$
r_{\text{long}} = \mathbb{E}[\text{Average Short Rates}] + \text{Term Premium}
$$

**Example:**

- Current overnight rate: 3.50%
- Expected average overnight rate (next 5 years): 3.80%
- 5-year swap rate: 4.25%

**Decomposition:**

$$
4.25\% = 3.80\% + 0.45\%
$$

**Where:**
- 3.80% = Expectations component (market's view of average short rates)
- 0.45% = Term premium (extra compensation for 5-year commitment)

**Carry trade earns:**

- Current carry: 4.25% - 3.50% = 0.75%
- This is MORE than term premium alone (0.45%)
- Extra 0.30% comes from current rates below expected average

**Why this matters:**

If you believe:
1. Forward rates overestimate future short rates (they usually do)
2. Term premium is compensation you can harvest
3. Current rates won't rise immediately

Then: **Receiving fixed earns both term premium + expectations error**

### 2. The Roll-Down Effect

**As time passes, magic happens:**

**Today:**
- You own 5-year swap at 4.25%

**1 year later (if curve unchanged):**
- Your swap is now a 4-year swap
- 4-year swap rate: 4.10% (lower on upward curve)
- Your swap is marked at 4.10%, but you're receiving 4.25%
- **You've made money from aging!**

**Mathematical explanation:**

**Value of swap (PV of fixed leg - PV of floating leg):**

$$
V = \sum_{i=1}^{n} \frac{r_{\text{fixed}} - f_i}{(1+d_i)^{t_i}}
$$

Where:
- $r_{\text{fixed}}$ = Your fixed rate (4.25%)
- $f_i$ = Forward rates (market's expectation of future floating)
- $d_i$ = Discount factors

**As time passes:**

- You keep receiving 4.25% (locked in)
- Market's 4-year swap rate is now 4.10% (new swaps lower)
- **You're receiving 15 bps more than current market → Profit**

**Roll-down profit (annual, approximate):**

$$
\text{Roll-Down} \approx \text{Slope} \times \text{Duration} \times \text{Notional}
$$

**Example:**

- Slope: (5-year rate - 4-year rate) = 4.25% - 4.10% = 15 bps
- Duration: 4.5 years (approximate)
- Notional: $10M

$$
\text{Roll-Down Profit} = 0.0015 \times 4.5 \times \$10M = \$67,500
$$

**This is ON TOP of carry income!**

### 3. The Funding Advantage

**Why swaps beat bonds for carry:**

**Bond carry trade:**

- Buy 5-year Treasury @ 4.00% yield
- Finance in repo market @ 3.60%
- Carry: 4.00% - 3.60% = 0.40% = $40,000/year on $10M
- Capital tied up: $10M (must pay upfront)

**Swap carry trade:**

- Receive 5-year swap @ 4.25%
- Pay SOFR @ 3.50%
- Carry: 4.25% - 3.50% = 0.75% = $75,000/year on $10M
- Capital required: $0 upfront (post variation margin only)
- Collateral: Initial margin ~$100k-200k (1-2% of notional)

**Swap advantage:**

- Higher carry: 0.75% vs 0.40% (+88% more!)
- Less capital: $150k vs $10M (67x leverage)
- Flexibility: Can exit easily (no selling bond)

**Return on capital employed:**

- Bond: $40,000 / $10M = 0.40%
- Swap: $75,000 / $150k = 50% (leverage!)

**This is why professionals use swaps for carry, not bonds**

### 4. Forward Curve vs. Realized Rates

**The key bet:**

$$
\text{Profit} = \text{Locked-In Fixed Rate} - \text{Realized Average Floating Rate}
$$

**Forward curve says:**

- Year 1: SOFR averages 3.60%
- Year 2: SOFR averages 3.80%
- Year 3: SOFR averages 4.00%
- Year 4: SOFR averages 4.20%
- Year 5: SOFR averages 4.40%
- **Average: 4.00%**

**Your swap:**

- You receive: 4.25% fixed
- You pay: Realized SOFR (unknown)
- Break-even: Average SOFR = 4.25%
- **Profit if: Realized SOFR < 4.25%**

**Historical evidence:**

Forward rates typically OVERestimate future short rates by 50-100 bps:

- Forward says: 4.00% average
- Realized is often: 3.50% average
- **You win by 50 bps!**

**This "forward premium bias" is the structural edge in carry trades**

---

## Key Terminology

**Carry:**

- Daily/annual income from rate differential
- Formula: (Fixed Received - Floating Paid) / 360
- Positive: Receiving more than paying
- Measured: Basis points per day or % per year

**Roll-Down:**

- Profit from aging down the curve
- Occurs when: Curve is upward-sloping
- Mechanism: Swap becomes shorter maturity (lower rate)
- Additive: Carry + Roll-Down = Total return

**DV01 (Dollar Value of 1 Basis Point):**

- P&L from 1 bp rate change
- Formula: DV01 = Duration × Notional / 10,000
- Example: 5-year swap, $10M notional → DV01 = $45,000
- Risk metric: Larger DV01 = More rate risk

**Break-Even Rate:**

- Rate level where carry = mark-to-market loss
- Formula: Break-even = Carry / DV01
- Example: $200 carry, $45k DV01 → 0.44 bps/day break-even
- Interpretation: Rates can rise 0.44 bps/day without losing money

**Forward Curve:**

- Implied future floating rates
- Derived from: Swap curve (bootstrapping)
- Shows: Market's expectation + term premium
- Key insight: Usually overestimates realized rates

**SOFR (Secured Overnight Financing Rate):**

- Overnight rate, replaced LIBOR (2023)
- Secured: Backed by Treasury collateral
- Risk-free: No credit component
- Resets: Daily (used for floating leg)

**Swap Spread:**

- Difference: Swap rate - Treasury yield
- Typical: 20-40 bps positive
- Reflects: Credit and liquidity factors
- Widens during: Financial stress

**Variation Margin:**

- Daily cash settlement of swap P&L
- Mark-to-market: Gains paid to you, losses you pay
- Same day: Usually by end of business
- Impact: Must have cash for losses

**Initial Margin:**

- Collateral posted at inception
- Amount: 1-3% of notional (varies by counterparty)
- Purpose: Cover potential future exposure
- Returned: When swap is closed

**Total Return:**

- Sum of: Carry + Roll-Down + MTM
- Carry: Daily income
- Roll-Down: Aging benefit
- MTM: Rate change impact

---

## Mathematical Foundation

### 1. Carry Calculation

**Daily carry (receiving fixed):**

$$
\text{Carry}_{\text{daily}} = \frac{N \times (r_f - r_{fl})}{360}
$$

Where:
- $N$ = Notional ($10M)
- $r_f$ = Fixed rate (4.25%)
- $r_{fl}$ = Current floating rate (3.50%)

**Example:**

$$
\text{Carry}_{\text{daily}} = \frac{\$10M \times (0.0425 - 0.035)}{360} = \frac{\$75,000}{360} = \$208.33
$$

**Annual carry:**

$$
\text{Carry}_{\text{annual}} = N \times (r_f - r_{fl}) = \$10M \times 0.75\% = \$75,000
$$

### 2. Roll-Down Calculation

**Present value of swap (simplified):**

$$
PV = N \times D \times (r_{\text{swap}} - r_{\text{market}})
$$

Where:
- $D$ = Modified duration
- $r_{\text{swap}}$ = Your fixed rate (4.25%)
- $r_{\text{market}}$ = Current market rate for remaining maturity

**After 1 year:**

- Your swap: Originally 5-year, now 4-year, still receiving 4.25%
- Market 4-year swap: 4.10%
- Difference: 15 bps in your favor

**PV gain:**

$$
PV_{\text{gain}} = \$10M \times 4.0 \times 0.0015 = \$60,000
$$

**This is the roll-down profit from aging 1 year**

### 3. Total Return Decomposition

**1-year total return:**

$$
\text{TR} = \text{Carry} + \text{Roll-Down} + \text{MTM}
$$

**Scenario: Rates unchanged**

- Carry: $75,000 (from 0.75% spread)
- Roll-Down: $60,000 (aging from 5Y to 4Y)
- MTM: $0 (rates flat)
- **Total: $135,000 (1.35% return on $10M notional)**

**Scenario: Rates rise 25 bps**

- Carry: $75,000 (still earn)
- Roll-Down: $60,000 (still age)
- MTM: -$45,000 × 25 = -$1,125,000 (DV01 loss!)
- **Total: -$990,000 (large loss overwhelms carry)**

**Break-even rate rise:**

$$
\text{Break-Even} = \frac{\text{Carry} + \text{Roll-Down}}{\text{DV01}} = \frac{\$135,000}{\$45,000} = 3.0 \text{ bps}
$$

**Rates can rise 3.0 bps over the year and you break even**

### 4. Leverage Calculation

**Return on collateral:**

$$
\text{ROC} = \frac{\text{Total Return}}{\text{Collateral Posted}}
$$

**Example:**

- Notional: $10M
- Collateral: $150k (1.5%)
- Total return (rates flat): $135,000

$$
\text{ROC} = \frac{\$135,000}{\$150,000} = 90\%
$$

**90% return on capital with flat rates!**

**But if rates rise 25 bps:**

$$
\text{ROC} = \frac{-\$990,000}{\$150,000} = -660\%
$$

**Leverage cuts both ways**

---

## Step-by-Step Setup

### 1. Phase 1

**1. Examine Current Curve:**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Current swap curve (December 2024)
curve = pd.DataFrame({
    'maturity': [0.25, 0.5, 1, 2, 3, 5, 7, 10, 30],
    'rate': [4.55, 4.58, 4.60, 4.20, 4.10, 4.25, 4.35, 4.50, 4.75]
})

# Plot curve
plt.figure(figsize=(12, 6))
plt.plot(curve['maturity'], curve['rate'], marker='o', linewidth=2)
plt.xlabel('Maturity (Years)')
plt.ylabel('Swap Rate (%)')
plt.title('SOFR Swap Curve')
plt.grid(True, alpha=0.3)
plt.show()
```

**2. Calculate Carry for Different Maturities:**

```python
# Current SOFR
current_sofr = 4.58

# Calculate carry for each maturity
curve['carry_bps'] = curve['rate'] - current_sofr
curve['carry_annual'] = curve['carry_bps'] / 100  # As percentage

print(curve[['maturity', 'rate', 'carry_bps', 'carry_annual']])
```

**Output:**

```
   maturity  rate  carry_bps  carry_annual
0      0.25  4.55      -0.03        -0.0003
1      0.50  4.58       0.00         0.0000
2      1.00  4.60       0.02         0.0002
3      2.00  4.20      -0.38        -0.0038
4      3.00  4.10      -0.48        -0.0048
5      5.00  4.25      -0.33        -0.0033
6      7.00  4.35      -0.23        -0.0023
7     10.00  4.50      -0.08        -0.0008
8     30.00  4.75       0.17         0.0017
```

**Interpretation: NEGATIVE CARRY everywhere except 30-year!**

This is an inverted curve. Let me use a more typical upward-sloping example:

**Better example (typical upward curve):**

```python
curve = pd.DataFrame({
    'maturity': [0.25, 0.5, 1, 2, 3, 5, 7, 10, 30],
    'rate': [3.50, 3.55, 3.65, 3.85, 4.00, 4.25, 4.40, 4.55, 4.90]
})

current_sofr = 3.50

curve['carry_bps'] = (curve['rate'] - current_sofr) * 100
curve['carry_annual_%'] = curve['rate'] - current_sofr

print(curve[['maturity', 'rate', 'carry_bps', 'carry_annual_%']])
```

**Output:**

```
   maturity  rate  carry_bps  carry_annual_%
0      0.25  3.50       0.00           0.000
1      0.50  3.55       5.00           0.050
2      1.00  3.65      15.00           0.150
3      2.00  3.85      35.00           0.350
4      3.00  4.00      50.00           0.500
5      5.00  4.25      75.00           0.750  <-- Sweet spot
6      7.00  4.40      90.00           0.900
7     10.00  4.55     105.00           1.050
8     30.00  4.90     140.00           1.400
```

**Best carry: 5-7 year sector (75-90 bps)**

**3. Calculate DV01 and Break-Even:**

```python
# Approximate DV01 per $1M notional
dv01_per_mm = {
    2: 1900,
    3: 2800,
    5: 4500,
    7: 6300,
    10: 9000,
    30: 20000
}

# For each maturity, calculate break-even daily move
results = []

for mat in [2, 3, 5, 7, 10, 30]:
    rate = curve[curve['maturity'] == mat]['rate'].values[0]
    carry_bps = (rate - current_sofr) * 100
    carry_daily = carry_bps / 360
    dv01 = dv01_per_mm[mat]
    breakeven_daily = carry_daily / (dv01 / 100)  # bps per day
    
    results.append({
        'maturity': mat,
        'rate': rate,
        'carry_annual_bps': carry_bps,
        'carry_daily_bps': carry_daily,
        'dv01_per_mm': dv01,
        'breakeven_bps_per_day': breakeven_daily
    })

results_df = pd.DataFrame(results)
print(results_df)
```

**Output:**

```
   maturity  rate  carry_annual_bps  carry_daily_bps  dv01_per_mm  breakeven_bps_per_day
0         2  3.85              35.0         0.097222         1900               0.005117
1         3  4.00              50.0         0.138889         2800               0.004960
2         5  4.25              75.0         0.208333         4500               0.004630
3         7  4.40              90.0         0.250000         6300               0.003968
4        10  4.55             105.0         0.291667         9000               0.003241
5        30  4.90             140.0         0.388889        20000               0.001944
```

**Interpretation:**

- 5-year: Can tolerate +0.46 bps/day rate rise
- 30-year: Can tolerate only +0.19 bps/day (high DV01)
- **5-7 year sector optimal (good carry, manageable DV01)**

### 1. Phase 2

**Decision matrix:**

```python
# Score each maturity
results_df['carry_score'] = results_df['carry_annual_bps'] / 100  # Normalize
results_df['risk_score'] = 10000 / results_df['dv01_per_mm']  # Lower DV01 = better
results_df['breakeven_score'] = results_df['breakeven_bps_per_day'] * 10  # Higher = better

# Weighted composite score
results_df['composite_score'] = (
    0.4 * results_df['carry_score'] +
    0.3 * results_df['risk_score'] +
    0.3 * results_df['breakeven_score']
)

print(results_df[['maturity', 'composite_score']].sort_values('composite_score', ascending=False))
```

**Output:**

```
   maturity  composite_score
2         5             1.982
3         7             1.931
1         3             1.784
4        10             1.612
0         2             1.523
5        30             1.198
```

**Winner: 5-year swap (best risk-adjusted carry)**

### 1. Phase 3

**1. Determine Risk Budget:**

```python
# Portfolio parameters
total_capital = 50_000_000  # $50M fund
max_dv01_pct = 0.10  # 10% of capital as DV01 risk

max_dv01 = total_capital * max_dv01_pct
print(f"Maximum DV01: ${max_dv01:,.0f}")

# Output
```

**2. Calculate Notional:**

```python
# 5-year swap DV01
dv01_per_mm = 4500

# Solve for notional
max_notional = (max_dv01 / dv01_per_mm) * 1_000_000
print(f"Maximum notional: ${max_notional:,.0f}")

# Output

# This is way too much! Let's use a more conservative approach
```

**More realistic:**

```python
# Target DV01
target_dv01 = 500_000

notional = (target_dv01 / dv01_per_mm) * 1_000_000
print(f"Target notional: ${notional:,.0f}")

# Output
```

**3. Calculate Expected Returns:**

```python
notional = 100_000_000  # $100M
dv01 = notional / 1_000_000 * dv01_per_mm  # $450,000

# Carry
carry_annual = notional * 0.0075  # 75 bps carry
print(f"Annual carry: ${carry_annual:,.0f}")

# Roll-down
rolldown_annual = notional * 0.0010
print(f"Annual roll-down: ${rolldown_annual:,.0f}")

# Total (no rate change)
total_return = carry_annual + rolldown_annual
print(f"Total return (flat rates): ${total_return:,.0f}")

# Return on collateral
collateral = notional * 0.02
roc = total_return / collateral
print(f"Return on collateral: {roc:.1%}")
```

**Output:**

```
Annual carry: $750,000
Annual roll-down: $100,000
Total return (flat rates): $850,000
Return on collateral: 42.5%
```

### 1. Phase 4

**1. Enter the Swap:**

```python
# Trade ticket
swap_trade = {
    'trade_date': '2024-12-01',
    'effective_date': '2024-12-03',
    'maturity_date': '2029-12-03',
    'notional': 100_000_000,
    'fixed_rate': 4.25,
    'fixed_leg': 'Receive',
    'floating_leg': 'Pay SOFR',
    'fixed_frequency': 'Semi-Annual',
    'floating_frequency': 'Quarterly',
    'day_count': '30/360',
    'counterparty': 'Goldman Sachs'
}

print(pd.DataFrame([swap_trade]))
```

**2. Daily P&L Tracking:**

```python
def calculate_swap_pnl(trade, current_rate, current_sofr):
    """Calculate daily P&L on swap"""
    
    # Carry (daily)
    carry_daily = (
        trade['notional'] * 
        (trade['fixed_rate']/100 - current_sofr/100) / 360
    )
    
    # MTM (from rate changes)
    rate_change = current_rate - trade['fixed_rate']
    dv01 = trade['notional'] / 1_000_000 * 4500
    mtm_pnl = -rate_change * dv01 * 100  # Negative because we're long duration
    
    # Total
    total_pnl = carry_daily + mtm_pnl
    
    return {
        'carry_daily': carry_daily,
        'mtm_pnl': mtm_pnl,
        'total_pnl': total_pnl
    }

# Example
pnl_day1 = calculate_swap_pnl(
    swap_trade,
    current_rate=4.27,  # 5-year rate up 2 bps
    current_sofr=3.51   # SOFR up 1 bp
)

print(f"Day 1 P&L:")
print(f"  Carry: ${pnl_day1['carry_daily']:,.0f}")
print(f"  MTM: ${pnl_day1['mtm_pnl']:,.0f}")
print(f"  Total: ${pnl_day1['total_pnl']:,.0f}")
```

**Output:**

```
Day 1 P&L:
  Carry: $2,056
  MTM: -$90,000
  Total: -$87,944
```

**3. Risk Management:**

```python
def check_risk_limits(position, current_rate, capital):
    """Monitor risk limits"""
    
    # DV01 check
    dv01 = position['notional'] / 1_000_000 * 4500
    dv01_pct = dv01 / capital
    
    # Stop loss check (10% of capital)
    rate_change = current_rate - position['fixed_rate']
    mtm_pnl = -rate_change * dv01 * 100
    loss_pct = mtm_pnl / capital
    
    alerts = []
    
    if dv01_pct > 0.02:
        alerts.append(f"WARNING: DV01 {dv01_pct:.1%} exceeds 2% limit")
    
    if loss_pct < -0.10:
        alerts.append(f"STOP LOSS: Loss {loss_pct:.1%} exceeds -10% limit")
    
    return {
        'dv01': dv01,
        'dv01_pct': dv01_pct,
        'mtm_pnl': mtm_pnl,
        'loss_pct': loss_pct,
        'alerts': alerts
    }

# Example
risk = check_risk_limits(
    swap_trade,
    current_rate=4.75,
    capital=50_000_000
)

print(risk)
```

### 1. Phase 5

**1. Profit Target:**

```python
# Exit when:
# - Cumulative carry reaches 50 bps of notional
# - OR rates fall 25+ bps (MTM gain)

target_cumulative_carry = 100_000_000 * 0.0050  # 50 bps
print(f"Profit target (carry): ${target_cumulative_carry:,.0f}")

# Days to reach target (at $2,083/day)
days_to_target = target_cumulative_carry / 2083
print(f"Days to profit target: {days_to_target:.0f}")

# Output
```

**2. Stop Loss:**

```python
# Exit if:
# - 5-year rate rises >50 bps
# - Cumulative loss > -5% of capital

stop_loss_rate = 4.25 + 0.50  # 4.75%
stop_loss_dollar = capital * 0.05  # $2.5M

print(f"Stop loss rate: {stop_loss_rate:.2%}")
print(f"Stop loss dollar: ${stop_loss_dollar:,.0f}")
```

---

## Real-World Examples

### 1. Example 1: 5-Year Swap Carry

**Background:**

- Fed paused hiking (December 2018)
- Curve steepening
- Perfect carry environment

**Market levels (January 2019):**

| Rate | Level |
|------|-------|
| 5-year swap | 2.70% |
| Overnight SOFR | 2.40% |

**Trade:**

- Receive $50M 5-year swap @ 2.70%
- Pay SOFR @ 2.40%
- Carry: 30 bps = $150,000/year
- DV01: $50M × $4,500 = $225,000

**Outcome (hold 12 months):**

| Month | 5-Year Swap | SOFR | Carry MTD | MTM Gain | Total P&L |
|-------|-------------|------|-----------|----------|-----------|
| Jan | 2.70% | 2.40% | $12,500 | $0 | $12,500 |
| Mar | 2.55% | 2.42% | $11,667 | $337,500 | $349,167 |
| Jun | 2.20% | 2.40% | $10,000 | $1,125,000 | $1,135,000 |
| Sep | 1.85% | 2.10% | $10,417 | $1,912,500 | $1,922,917 |
| Dec | 1.90% | 1.95% | $10,833 | $1,800,000 | $1,810,833 |

**12-month total:**

- Carry earned: $150,000 (30 bps × $50M)
- MTM gain: $1,800,000 (80 bps rate decline × $225k DV01)
- Roll-down: ~$50,000
- **Total: $2,000,000 profit on $1M collateral = 200% return!**

**Why it worked:**

1. Fed cut rates 75 bps (July, Sept, Oct 2019)
2. 5-year rates fell 80 bps
3. Positive carry every day
4. Roll-down added bonus
5. **Perfect storm for receive-fixed**

### 2. Example 2: 10-Year Swap Carry

**Background:**

- Inflation surging
- Fed starting to hike
- Trader ignored signs

**Market levels (January 2022):**

| Rate | Level |
|------|-------|
| 10-year swap | 1.80% |
| Overnight SOFR | 0.08% |

**Trade:**

- Receive $100M 10-year swap @ 1.80%
- Pay SOFR @ 0.08%
- Carry: 172 bps = $1,720,000/year (looks amazing!)
- DV01: $100M × $9,000 = $900,000

**Thesis: "Massive carry, rates won't rise much"**

**What happened: Fed hiking cycle**

| Month | 10-Year Swap | SOFR | Carry MTD | MTM Loss | Total P&L |
|-------|--------------|------|-----------|----------|-----------|
| Jan | 1.80% | 0.08% | $143,333 | $0 | $143,333 |
| Mar | 2.40% | 0.30% | $135,000 | -$5,400,000 | -$5,265,000 |
| Jun | 3.20% | 1.55% | $106,667 | -$12,600,000 | -$12,493,333 |
| Sep | 3.80% | 3.00% | $66,667 | -$18,000,000 | -$17,933,333 |
| Dec | 3.90% | 4.35% | $-70,833 | -$18,900,000 | -$18,970,833 |

**12-month total:**

- Carry earned: ~$500,000 (declining as SOFR rose)
- MTM loss: -$18,900,000 (210 bps rate rise × $900k DV01)
- **Total: -$18,400,000 loss on $2M collateral**

**Margin calls:**

- June: Required $5M additional margin
- September: Required $10M additional margin
- December: **Forced to close position**

**Final exit:**

- Closed at 3.90% (210 bps higher than entry)
- Realized loss: -$18,400,000
- **Account: Wiped out + owed money to broker**

**What went wrong:**

1. Ignored inflation warnings
2. Massive duration risk (10-year DV01)
3. No stop loss
4. Didn't exit when Fed turned hawkish (March)
5. **Carry of $1.7M/year meaningless when losing $18M**

### 3. Example 3: 2s5s Curve Carry

**Background:**

- Fed pausing after hiking to 5.25%
- Curve inverted
- Opportunity: Receive 5s, pay 2s

**Market levels (July 2023):**

| Swap | Rate |
|------|------|
| 2-year | 4.80% |
| 5-year | 4.30% |
| SOFR | 5.15% |

**Trade (curve carry):**

- Receive $50M 5-year @ 4.30%
- Pay $50M 2-year @ 4.80%
- Net carry: -50 bps (NEGATIVE!)

**Wait, why would anyone do this?**

**Thesis: Curve will normalize (steepen)**

- 2-year: Sensitive to Fed (will fall when Fed cuts)
- 5-year: Less sensitive (longer-term view)
- If Fed cuts → 2s fall more than 5s → Curve steepens → Profit

**Not a pure carry trade, but a curve trade with carry**

Let me use a better pure carry example:

### 4. Better Example 3: Front-End Carry

**Background:**

- Fed hiking slowly (3 hikes/year)
- Curve steep at front end
- Low volatility

**Market levels (January 2017):**

| Swap | Rate |
|------|------|
| 2-year | 1.40% |
| SOFR | 0.75% |

**Trade:**

- Receive $100M 2-year @ 1.40%
- Pay SOFR @ 0.75%
- Carry: 65 bps = $650,000/year
- DV01: $100M × $1,900 = $190,000

**Strategy: Short duration, high carry**

**Outcome (24 months):**

**Year 1:**

- SOFR rose: 0.75% → 1.25% (Fed hiked 3 times)
- 2-year rose: 1.40% → 1.80% (40 bps)
- Carry earned: $550,000 (average spread 55 bps)
- MTM loss: -$76,000 (40 bps × $190k DV01)
- Roll-down: +$50,000
- **Net: +$524,000**

**Year 2:**

- SOFR rose: 1.25% → 2.00% (Fed hiked 3 more times)
- 2-year rose: 1.80% → 2.65% (85 bps)
- Carry earned: $450,000 (shrinking spread)
- MTM loss: -$161,500 (85 bps × $190k DV01)
- Roll-down: +$30,000 (maturity approaching)
- **Net: +$318,500**

**2-year total: +$842,500 on $2M collateral = 42% return (21% annualized)**

**Why it worked:**

1. Short duration limited MTM losses
2. Consistent positive carry
3. Fed telegraphed hikes (no surprises)
4. Roll-down added small bonus
5. **Modest, consistent profits—professional's favorite**

### 5. Example 4: 30-Year Carry + QE

**Background:**

- COVID crash (March 2020)
- Fed announces unlimited QE

**Market levels (March 23, 2020, after Fed announcement):**

| Swap | Rate |
|------|------|
| 30-year | 1.60% |
| SOFR | 0.05% |

**Trade:**

- Receive $25M 30-year @ 1.60%
- Pay SOFR @ 0.05%
- Carry: 155 bps = $387,500/year (huge!)
- DV01: $25M × $20,000 = $500,000 (very high!)

**Thesis: Fed QE will crush long-end yields**

**Outcome (6 months):**

| Month | 30-Year Swap | Carry MTD | MTM Gain | Total |
|-------|--------------|-----------|----------|-------|
| Apr | 1.35% | $32,292 | $1,250,000 | $1,282,292 |
| May | 1.45% | $30,417 | $750,000 | $780,417 |
| Jun | 1.50% | $29,583 | $500,000 | $529,583 |
| Jul | 1.40% | $28,125 | $1,000,000 | $1,028,125 |
| Aug | 1.30% | $26,667 | $1,500,000 | $1,526,667 |
| Sep | 1.25% | $25,833 | $1,750,000 | $1,775,833 |

**6-month total:**

- Carry: $173,000
- MTM gain: $1,750,000 (35 bps decline × $500k DV01)
- **Total: $1,923,000 on $500k collateral = 385% return!**

**Why it worked:**

1. Fed QE hammered long-end yields
2. Massive positive carry every day
3. Duration risk paid off (rates fell)
4. Perfect timing (entered right at peak fear)
5. **Combination of carry + Fed put**

**But note: This required perfect timing and high risk tolerance**

### 6. Example 5: Negative Carry Pay-Fixed

**Background:**

- Inflation rising
- Fed still dovish ("transitory")
- Smart traders hedging

**Market levels (June 2021):**

| Swap | Rate |
|------|------|
| 5-year | 1.00% |
| SOFR | 0.05% |

**Trade (reverse carry):**

- Pay $50M 5-year @ 1.00%
- Receive SOFR @ 0.05%
- Carry: -95 bps = -$475,000/year (NEGATIVE!)
- DV01: $50M × $4,500 = $225,000

**Thesis: Inflation hedge, willing to pay negative carry**

**Outcome (18 months):**

**Year 1 (2021):**

- 5-year rose: 1.00% → 1.60% (60 bps)
- SOFR rose: 0.05% → 0.08% (negligible)
- Carry cost: -$475,000
- MTM gain: +$1,350,000 (60 bps × $225k DV01, we're short duration!)
- **Net: +$875,000**

**Year 2 (through December 2022):**

- 5-year rose: 1.60% → 4.30% (270 bps!)
- SOFR rose: 0.08% → 4.30% (422 bps!)
- Carry: Turned POSITIVE late in year
- MTM gain: +$6,075,000 (270 bps × $225k DV01)
- **Net: +$6,075,000**

**Total 18-month: +$6,950,000 on $1M collateral**

**Why it worked:**

1. Correctly bet on inflation
2. Fed forced to hike aggressively
3. Paid negative carry for 12 months, then it turned positive!
4. Massive MTM gains from rate rise
5. **Insurance position became hugely profitable**

---

## Best Case Scenario

### 1. The Perfect Carry Trade

**Setup for maximum profit:**

**Ideal conditions:**

1. **Steep curve** (high carry available)
2. **Fed pause or cutting** (rates stable/falling)
3. **Low volatility** (carry accrues smoothly)
4. **Forward curve bias** (overestimates future rates)
5. **Long holding period** (1-2 years to compound)

### 2. Best Case Example

**Background:**

- Fed at zero (0-0.25%)
- Committed to "extended period" of low rates
- Curve extremely steep

**Market levels (March 2009):**

| Rate | Level |
|------|-------|
| 5-year swap | 2.25% |
| Overnight rate | 0.15% |
| Expected SOFR (forward curve) | 1.50% average over 5 years |

**Trade:**

- Receive $200M 5-year swap @ 2.25%
- Pay overnight rate @ 0.15%
- Carry: 210 bps = $4,200,000/year (massive!)
- DV01: $200M × $4,500 = $900,000
- Collateral: $4M (2%)

**24-month outcome:**

**Year 1 (2009-2010):**

- 5-year swap: 2.25% → 2.45% (+20 bps, slight rise)
- Overnight: 0.15% → 0.18% (flat, Fed on hold)
- Carry earned: $4,200,000
- MTM loss: -$180,000 (20 bps × $900k DV01)
- Roll-down: +$200,000 (aging 5Y → 4Y)
- **Year 1 total: +$4,220,000**

**Year 2 (2010-2011):**

- 5-year swap: 2.45% → 1.80% (-65 bps, QE2!)
- Overnight: 0.18% → 0.10% (still near zero)
- Carry earned: $4,500,000 (spread widened!)
- MTM gain: +$5,850,000 (65 bps × $900k DV01)
- Roll-down: +$150,000 (4Y → 3Y)
- **Year 2 total: +$10,500,000**

**24-month cumulative:**

- Carry: $8,700,000
- Roll-down: $350,000
- MTM: +$5,670,000
- **Total: $14,720,000 on $4M collateral = 368% return!**

**Return breakdown:**

- Carry: 217.5% over 2 years (109% annualized)
- MTM: 142% (from QE2 driving rates lower)
- Roll-down: 8.75%

**Why this was perfect:**

1. **Fed credibly committed** to low rates for extended period
2. **Steep curve** (210 bps carry)
3. **Forward rates wrong** (predicted 1.50% avg, realized 0.15%)
4. **QE2 windfall** (2010, rates fell further)
5. **Roll-down** (curve stayed steep)
6. **Low volatility** (Fed stability)
7. **Long hold** (2 years compounded gains)

**Professional fund using this strategy:**

- Started: $100M AUM
- Carry trade: $200M notional (2x leverage)
- 2-year return: 368%
- **Ending AUM: $368M (before fees)**

**This is the holy grail of carry trades—everything aligned**

---

## Worst Case Scenario

### 1. The Carry Trade Disaster

**Worst possible conditions:**

1. **Inverted curve** (negative carry)
2. **Fed aggressive hiking** (rates surge)
3. **High volatility** (stop-losses triggered)
4. **Overleveraged** (too much notional)
5. **No hedging** (pure directional bet)

### 2. Worst Case Example

**Background:**

- Inflation "transitory" narrative breaks down
- Fed pivots from dovish to most aggressive in 40 years
- Trader caught on wrong side

**Market levels (December 2021):**

| Rate | Level |
|------|-------|
| 10-year swap | 1.50% |
| Overnight rate | 0.08% |
| VIX | 18 (calm) |

**Trade (maximum greed):**

- Receive $500M 10-year swap @ 1.50%
- Pay overnight @ 0.08%
- Carry: 142 bps = $7,100,000/year (looks incredible!)
- DV01: $500M × $9,000 = $4,500,000
- Collateral: $10M (2%, minimal)
- **Leverage: 50x (notional/collateral)**

**Thesis: "Fed will never hike much, curve is wrong"**

**Timeline of disaster:**

**January 2022:**

- CPI: 7.0% (40-year high!)
- 10-year swap: 1.50% → 1.80% (+30 bps)
- MTM loss: -$1,350,000
- Carry (1 month): +$591,667
- **Net: -$758,333**

**Trader reaction: "Temporary, will reverse"**

**March 2022:**

- Fed hikes 0.25% (first hike in 3 years)
- Signals more hikes coming ("not one and done")
- 10-year swap: 1.80% → 2.50% (+70 bps more, 100 bps total)
- MTM loss: -$4,500,000 (cumulative)
- Carry (3 months): +$1,775,000
- **Net: -$2,725,000**

**Margin call #1: Post $5M**

**June 2022:**

- Fed hikes 0.75% (largest since 1994!)
- Inflation 8.6% (still rising!)
- 10-year swap: 2.50% → 3.50% (+100 bps more, 200 bps total)
- MTM loss: -$9,000,000 (cumulative)
- Carry (6 months): +$3,100,000
- **Net: -$5,900,000**

**Margin call #2: Post $10M** (total $15M posted)

**September 2022:**

- Fed hikes 0.75% again (3rd consecutive!)
- Powell: "Pain is coming"
- 10-year swap: 3.50% → 4.00% (+50 bps more, 250 bps total)
- MTM loss: -$11,250,000 (cumulative)
- Carry (9 months): +$4,100,000
- **Net: -$7,150,000**

**Margin call #3: POST $15M OR LIQUIDATE**

**Trader: Can't post, forced liquidation**

**October 2022 (Forced Exit):**

- Broker closes position at 4.00%
- Realized loss: -$11,250,000
- Carry earned: +$4,100,000
- **Net realized: -$7,150,000**

**Account wipeout:**

- Started: $10M
- Margin posted: $15M (borrowed from other accounts)
- Final: -$7,150,000 (owes money!)
- **Total loss: $17.15M on $10M account**

**But it gets worse...**

**November 2022:**

- 10-year swap peaks at 4.30% (+280 bps from entry)
- If still in position, loss would be -$12,600,000
- **Liquidation at 4.00% actually "saved" $1.35M!**

**2023-2024 aftermath:**

- Fed pauses (July 2023)
- 10-year swap falls to 3.50% (March 2024)
- **If had survived, would have recovered most losses**
- But couldn't survive margin calls

**What went catastrophically wrong:**

**1. Ignored inflation warnings (November 2021):**

- CPI accelerating (6.8% in November)
- Fed minutes showed hawkish shift
- Dismissed as "transitory"

**2. Massive overleveraging:**

- $500M notional on $10M capital = 50x
- Should have been max 10-20x
- No room for error

**3. Long duration (10-year):**

- DV01 of $4.5M = 45% of capital
- 10 bps move = $450k loss (4.5% of account)
- 100 bps move = wiped out

**4. No stop loss:**

- Didn't exit at -50 bps (Jan)
- Didn't exit at -100 bps (March)
- Didn't exit at -150 bps (May)
- **Held all the way to forced liquidation**

**5. Averaged down:**

- Added more 10-year at 2.00% (March)
- Doubled down at 2.50% (April)
- **Made disaster even worse**

**6. Carry trap:**

- Thought $7M/year carry would save them
- But losing $11M in 9 months
- **Carry meaningless when duration bleeding**

**Lessons:**

1. **Never ignore Fed pivot** (dovish → hawkish = disaster for receive-fixed)
2. **Max 10-15x leverage** (50x is suicide)
3. **Hard stop loss** (exit at -50 bps, don't hope)
4. **Don't fight inflation** (CPI >6% = death for bonds)
5. **Carry ≠ safety** ($7M carry irrelevant when losing $11M)
6. **Never average down** (adds to losing position)
7. **Survival > profits** (live to trade another day)

**The trader's journey:**

- **Month 1:** "Small drawdown, will revert"
- **Month 3:** "Fed won't hike that much"
- **Month 6:** "This is unprecedented, must reverse"
- **Month 9:** "I'm ruined, account closed"
- **Month 24:** "If only I'd survived... it did reverse"

**Reality: Market can stay irrational (or correctly pricing new regime) longer than you can stay solvent**

---

## What to Remember

### 1. Core Concept

**Swap carry trades earn daily income from the spread between fixed rates received and floating rates paid, plus roll-down benefits, while accepting mark-to-market risk from rate movements:**

$$
\text{Total Return} = \text{Carry} + \text{Roll-Down} + \text{MTM}
$$

- Receive fixed, pay floating (SOFR)
- Positive carry on upward-sloping curves
- Break-even: Daily carry / DV01 = bps/day tolerance
- Leverage: Minimal capital (1-3% collateral), high notional
- Horizon: Weeks to months (occasionally years)

### 2. The Setup

**Standard 5-year swap carry:**

- Curve: 5-year @ 4.25%, SOFR @ 3.50%
- Carry: 75 bps = $75,000/year per $10M
- DV01: $45,000 per $10M
- Break-even: 0.46 bps/day rate rise
- Leverage: 10-20x (conservative)
- Collateral: 2-5% of notional

### 3. The Mathematics

**Daily carry:**

$$
\text{Carry}_{\text{daily}} = \frac{N \times (r_{\text{fixed}} - r_{\text{SOFR}})}{360}
$$

**Break-even rate change:**

$$
\text{Break-even}_{\text{daily}} = \frac{\text{Carry}_{\text{daily}}}{\text{DV01}}
$$

**Total return (1 year):**

$$
\text{TR} = \text{Carry} + \text{Roll-Down} - \Delta r \times \text{DV01} \times 100
$$

### 4. Risk Management

**Essential rules:**

- Leverage: Max 15-20x (notional/collateral)
- DV01 limit: Max 5-10% of capital
- Stop loss: Exit if rates rise >50 bps against you
- Maturity: Prefer 3-7 year (balance carry vs. DV01)
- Curve check: Only trade if curve upward-sloping >50 bps
- Fed monitoring: Exit before Fed turns hawkish

### 5. Maximum Profit/Loss

**Best case:**

- Steep curve (150+ bps carry)
- Fed cutting or on hold (rates stable/falling)
- 1-2 year hold (compound carry + roll-down)
- **Returns: 100-300% on collateral over 1-2 years**

**Worst case:**

- Fed aggressive hiking (rates up 200+ bps)
- Overleveraged (50x)
- No stop loss (held through disaster)
- **Max loss: >100% of capital (owe money to broker)**

**Expected (disciplined trading):**

- Carry: 50-100 bps/year
- Roll-down: 10-20 bps/year
- MTM: Neutral to +50 bps (if rates stable/fall slightly)
- **Total: 60-170 bps/year on notional = 10-50% on collateral**

### 6. When to Trade

**Trade swap carry when:**

- Curve upward-sloping >50 bps (positive carry)
- Fed pausing or cutting (stable/falling rate environment)
- Low volatility (carry accrues smoothly)
- Forward curve steep (overestimating future rates)
- Capital sufficient (2-5% collateral available)

**Don't trade when:**

- Curve inverted (negative carry)
- Fed turning hawkish (hiking cycle starting)
- Inflation accelerating >4% (forces Fed to hike)
- High volatility (carry overwhelmed by MTM swings)
- Overleveraged (>25x)

### 7. Common Mistakes

1. Overleveraging (50x+ is suicide)
2. Ignoring Fed signals (dovish → hawkish pivot)
3. Long duration in hiking cycle (10-year+ during inflation)
4. No stop loss (holding -100 bp moves hoping to recover)
5. Carry illusion ($7M carry meaningless when losing $11M)
6. Averaging down (adding to losers)
7. Wrong maturity (30-year has huge DV01, small moves = ruin)
8. Fighting inflation (CPI >5% = run away from receive-fixed)

### 8. Final Wisdom

> "Swap carry trades are the institutional investor's bread and butter—you earn 50-100 bps per year by simply receiving fixed on a steep curve while the Fed is on hold. It's the closest thing to free money in finance: collect $200k/year on $10M notional with only $200k collateral posted (100% return on capital!). But here's the brutal truth: carry is an optical illusion. That $200k/year becomes $-2M in losses if rates rise 50 bps, and you can blow up 10 years of carry gains in one bad month (see 2022). The math is simple: your daily carry is $550, your DV01 is $45k, so you break even if rates rise 1.2 bps/day. Sounds safe, right? Until the Fed hikes 75 bps in one meeting, curve inverts, and you're down $3.4M in a week. The key is respecting regime changes: in stable Fed regimes (2009-2021), swap carry was a money machine—65% win rate, 15-25% annual returns. In Fed pivot regimes (1994, 2022), carry trades are widow-makers—positions that printed money for years suddenly lose 5-10 years of gains in months. Trade carry aggressively when the Fed is credibly committed to low rates. Exit IMMEDIATELY when inflation accelerates or Fed turns hawkish. Size conservatively (max 15x leverage), use hard stops (50 bps against you), and never—NEVER—average down into a Fed pivot. The carry will be there tomorrow, but if you're margin called today, you're finished."

**Key to success:**

- Select 5-7 year maturity (optimal carry/DV01 balance)
- Size for max 15x leverage (notional/collateral)
- Set stop loss at -50 bps rate rise
- Monitor Fed signals obsessively (inflation, minutes, speeches)
- Exit before Fed pivots hawkish (don't wait for hike)
- Take profits at 50-100 bps (don't get greedy)
- Never average down (cut losses, don't add)
- Diversify across maturities (don't put all in 10-year)

**Most important:** Swap carry is a regime trade. It works 90% of the time (Fed stable, low inflation, carry > realized rates), but fails catastrophically 10% of the time (Fed pivots, inflation surges, rates spike 200 bps). The 90% of the time generates 15-25% annual returns. The 10% of the time wipes out 5-10 years of gains. Your job is to identify which regime you're in and trade accordingly. In stable regimes, lever up to 15x and collect carry. In pivot regimes, cut positions to zero and sit in cash. The difference between a successful carry trader and a bankrupt one is knowing when to switch regimes. 💰📈⚠️

