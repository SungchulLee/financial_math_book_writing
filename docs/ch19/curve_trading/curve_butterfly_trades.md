# Curve Butterfly Trades


**Curve butterfly trades** are fixed income relative value strategies that exploit mispricings in the curvature of the yield curve by simultaneously taking positions in three different maturities—typically buying (or selling) the "body" (middle maturity) while selling (or buying) equal amounts of the "wings" (shorter and longer maturities)—profiting when the body becomes relatively cheaper or richer compared to a linear interpolation between the wings, while maintaining minimal exposure to parallel shifts in rates.

---

## The Core Insight


**The fundamental idea:**

- Yield curves are rarely perfectly straight lines
- Curvature (convexity) varies over time
- Three-point trade isolates curvature exposure
- Body vs. wings relationship mean-reverts
- Duration-neutral to parallel shifts
- Fed policy changes affect curvature predictably
- "Rich/cheap" analysis identifies opportunities
- Lower risk than outright directional trades

**The key equations:**

**Butterfly spread (simple):**

$$
\text{Butterfly} = r_{\text{body}} - \frac{r_{\text{short wing}} + r_{\text{long wing}}}{2}
$$

**Butterfly spread (duration-weighted):**

$$
\text{Butterfly}_{\text{DV01}} = r_{\text{body}} - \left(\frac{w_s \cdot r_{\text{short}} + w_l \cdot r_{\text{long}}}{w_s + w_l}\right)
$$

**You're essentially betting: "The middle point on the curve is too high (rich) or too low (cheap) relative to a straight line between the ends."**

---

## What Are Curve Butterfly Trades?


**Before trading curve butterflies, understand the mechanics:**

### 1. Core Concept


**Definition:** A three-legged fixed income trade structure involving a position in a "body" (middle maturity point on the yield curve) combined with offsetting positions in two "wings" (shorter and longer maturity points), typically sized to be duration-neutral, that profits from changes in the curvature or convexity of the yield curve rather than from parallel shifts in overall rate levels.

**When you trade a butterfly:**

- You select three maturities (e.g., 2-year, 5-year, 10-year)
- You identify middle as "body" (5-year)
- You identify ends as "wings" (2-year and 10-year)
- You measure if body is rich or cheap vs. wings
- You construct duration-neutral position
- You profit from mean reversion of curvature
- You maintain minimal directional exposure
- Primary drivers: Fed policy, supply/demand, technical factors

**Example - Classic 2s5s10s Butterfly:**

**Market levels (December 2024):**

| Maturity | Yield | DV01 (per $1M) |
|----------|-------|----------------|
| 2-year | 4.40% | $1,850 |
| 5-year | 4.15% | $4,350 |
| 10-year | 4.25% | $8,200 |

**Step 1: Calculate butterfly spread**

Simple average:

$$
\text{Fly} = 4.15\% - \frac{4.40\% + 4.25\%}{2} = 4.15\% - 4.325\% = -17.5 \text{ bps}
$$

**Interpretation: 5-year is 17.5 bps cheap (yields more than average)**

**This means:**

- Curve is "inverted" between 2-5 years (2s>5s)
- Curve is "normal" between 5-10 years (5s<10s)
- Overall shape: Hump at 2-year

**Step 2: Construct duration-neutral trade**

**Goal:** Buy cheap 5-year, sell rich 2-year and 10-year, DV01-neutral

**DV01 weighting:**

- Buy 5-year: Need DV01 exposure of X
- Sell 2-year: Need DV01 of 0.5X (half)
- Sell 10-year: Need DV01 of 0.5X (half)

**Calculation:**

Target: $10,000 DV01 in 5-year

- 5-year: Buy $10M / ($4,350/1M) × $10,000 = 2.3 units → Buy $2.3M face
- 2-year: Sell to offset half ($5,000 DV01): $5,000 / ($1,850/1M) = $2.7M face
- 10-year: Sell to offset half ($5,000 DV01): $5,000 / ($8,200/1M) = $0.61M face

**Trade:**

- **Buy $2.3M 5-year**
- **Sell $2.7M 2-year**
- **Sell $0.61M 10-year**

**Result: DV01-neutral, profits if 5-year cheapens (yield rises relative to wings)**

### 2. Butterfly Naming Convention


**Standard notation: XsYsZs**

- First number (X): Short wing maturity
- Second number (Y): Body maturity
- Third number (Z): Long wing maturity

**Examples:**

- **2s5s10s:** 2-year wing, 5-year body, 10-year wing (most common)
- **5s10s30s:** 5-year wing, 10-year body, 30-year wing (long end)
- **3m2s5s:** 3-month wing, 2-year body, 5-year wing (front end)

### 3. Types of Butterflies


**1. Long Butterfly (Buy the Fly):**

- **Position:** Buy body, sell wings
- **Bet:** Body will cheapen (yield rise) vs. wings
- **When:** Body is rich (low yield vs. interpolation)
- **Profit:** Body yield rises, wings yields fall (or stay flat)

**2. Short Butterfly (Sell the Fly):**

- **Position:** Sell body, buy wings
- **Bet:** Body will richen (yield fall) vs. wings
- **When:** Body is cheap (high yield vs. interpolation)
- **Profit:** Body yield falls, wings yields rise (or stay flat)

**3. Duration-Weighted vs. Equal-Notional:**

**Duration-weighted (professional):**

- Wings sized to neutralize DV01
- Pure curvature play
- No exposure to parallel shifts

**Equal-notional (simple):**

- Equal dollar amounts in each leg
- Has residual duration exposure
- Simpler to execute

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/curve_butterfly_trades.png?raw=true" alt="curve_butterfly_trades" width="700">
</p>
**Figure 1:** Curve butterfly trades showing the three-point structure with body and wings, the butterfly spread measurement as deviation from linear interpolation, and how the trade profits when the body moves relative to the wings (curve flattening, steepening, or changing curvature).

---

## Economic


**Beyond the basic mechanics, understanding the REAL economics:**

### 1. The Curvature Premium


**The deep insight:**

Yield curves have natural curvature due to:

$$
\text{Curvature} = \frac{\partial^2 r(t)}{\partial t^2}
$$

**Why curves aren't straight:**

1. **Convexity value:** Bonds with duration in the middle of the curve have higher convexity
2. **Supply/demand:** Different investors prefer different maturities
3. **Hedging flows:** Callable bonds, mortgages create demand in specific sectors
4. **Uncertainty:** Medium-term rates have highest uncertainty (not today, not long-run)

**Example - Normal positive curvature:**

```
Yield
  ^
  |                    /
  |                  /
  |                /      <- Curved line (reality)
  |        *     /
  |      /    /
  |    /   /  <- Straight line (interpolation)
  |  /  /
  |/__________> Maturity
     2  5  10
```

**Body (5-year) is BELOW straight line = negative butterfly = cheap**

### 2. Fed Policy and Butterfly


**How Fed policy affects curvature:**

**1. Hiking cycle (Fed tightening):**

```
Before hiking:
2s: 1.0%, 5s: 2.0%, 10s: 2.5%
Fly = 2.0% - (1.0%+2.5%)/2 = 2.0% - 1.75% = +25 bps (positive)

During hiking:
2s: 4.5%, 5s: 4.0%, 10s: 3.8%
Fly = 4.0% - (4.5%+3.8%)/2 = 4.0% - 4.15% = -15 bps (negative)

Curve inverts, front end rises most
Butterfly goes from +25 to -15 (40 bp move!)
```

**Trade: Short butterfly before hiking (sell body, buy wings)**

**2. Cutting cycle (Fed easing):**

```
Before cutting:
2s: 4.5%, 5s: 4.0%, 10s: 4.0%
Fly = 4.0% - (4.5%+4.0%)/2 = 4.0% - 4.25% = -25 bps (negative)

During cutting:
2s: 2.0%, 5s: 2.5%, 10s: 3.0%
Fly = 2.5% - (2.0%+3.0%)/2 = 2.5% - 2.5% = 0 bps (flat)

Curve normalizes, front end falls most
Butterfly goes from -25 to 0 (25 bp improvement)
```

**Trade: Buy butterfly before cutting (buy body, sell wings)**

### 3. Rich/Cheap Analysis


**Identifying mispricing:**

**Historical butterfly average:**

$$
\text{Fair Fly} = \text{Historical Average} \pm 1 \text{ std dev}
$$

**Example - 2s5s10s butterfly:**

**Historical data (10 years):**

- Mean: -5 bps
- Std dev: 12 bps
- Current: -25 bps

**Z-score:**

$$
Z = \frac{-25 - (-5)}{12} = \frac{-20}{12} = -1.67
$$

**Interpretation:**

- Current fly is 1.67 std dev below average
- 5-year is cheap vs. historical (yields too high)
- **Trade: Buy butterfly (bet on mean reversion)**

**Confidence:**

- |Z| < 1.0: Neutral (no trade)
- 1.0 < |Z| < 2.0: Moderate signal (consider trade)
- |Z| > 2.0: Strong signal (execute trade)

### 4. The Role of Convexity


**Why body behaves differently:**

**Convexity by maturity:**

| Maturity | Duration | Convexity |
|----------|----------|-----------|
| 2-year | 1.9 | 5 |
| 5-year | 4.5 | 25 |
| 10-year | 8.7 | 95 |

**Body (5-year) has intermediate convexity**

**When rates are volatile:**

- High convexity bonds outperform (10-year best)
- Low convexity bonds underperform (2-year worst)
- **Body underperforms on average**

**Implication:**

$$
\text{Butterfly} = \text{Fair Value} - \text{Convexity Premium} + \text{Supply/Demand}
$$

**During rate volatility:**

- Convexity premium rises (investors pay for protection)
- 10-year richens (outperforms)
- Butterfly becomes more negative (body cheaper)
- **Trade: Buy butterfly anticipating vol decline**

---

## Key Terminology


**Butterfly Spread:**

- Difference between body and interpolated wings
- Positive: Body rich (yields less than average)
- Negative: Body cheap (yields more than average)
- Typical range: -30 to +30 bps

**Body:**

- Middle maturity in butterfly
- The "1x" position
- Example: 5-year in 2s5s10s
- Focus of trade (buy or sell)

**Wings:**

- Outer maturities (short and long)
- The "2x" position (combined)
- Example: 2-year and 10-year in 2s5s10s
- Offset exposure (opposite of body)

**Buy the Fly:**

- Long body, short wings
- Profit if body cheapens (yield rises)
- Bet: Positive butterfly will become negative
- Typical: Body currently rich

**Sell the Fly:**

- Short body, long wings
- Profit if body richens (yield falls)
- Bet: Negative butterfly will become positive
- Typical: Body currently cheap

**DV01 Neutral:**

- Position has zero sensitivity to parallel shifts
- Wings DV01 = Body DV01
- Pure curvature exposure
- Professional standard

**Regression-Weighted:**

- Wings weighted by historical relationship to body
- More sophisticated than simple DV01
- Accounts for different betas
- Used by hedge funds

**Carry:**

- Daily P&L from yield differential
- Positive carry: Earning net interest
- Negative carry: Paying net interest
- Important for hold period

**Roll-Down:**

- P&L from passage of time (aging)
- Bonds move down the curve
- Can enhance or hurt butterfly
- Predict with forward curve

**Curvature:**

- Second derivative of yield curve
- Measures how "bent" curve is
- Positive curvature: Convex (upward bend)
- Negative curvature: Concave (downward bend)

---

## Mathematical Foundation


### 1. DV01-Weighted Butterfly


**Goal: Create position with zero DV01**

**Given:**

- $\text{DV01}_s$ = Short wing DV01 per $1M
- $\text{DV01}_b$ = Body DV01 per $1M
- $\text{DV01}_l$ = Long wing DV01 per $1M

**Target notional in body: $N_b$**

**Step 1: Calculate body DV01**

$$
\text{Total DV01}_b = N_b \times \text{DV01}_b
$$

**Step 2: Solve for wing notionals**

$$
N_s \times \text{DV01}_s + N_l \times \text{DV01}_l = N_b \times \text{DV01}_b
$$

**Common weighting: Equal DV01 in each wing**

$$
N_s \times \text{DV01}_s = N_l \times \text{DV01}_l = \frac{N_b \times \text{DV01}_b}{2}
$$

**Solve:**

$$
N_s = \frac{N_b \times \text{DV01}_b}{2 \times \text{DV01}_s}
$$

$$
N_l = \frac{N_b \times \text{DV01}_b}{2 \times \text{DV01}_l}
$$

**Example - 2s5s10s:**

- Body: $10M 5-year, DV01 = $4,350 per $1M → Total = $43,500
- Short wing: DV01 = $1,850 per $1M
- Long wing: DV01 = $8,200 per $1M

$$
N_s = \frac{10 \times 4,350}{2 \times 1,850} = \frac{43,500}{3,700} = 11.76M
$$

$$
N_l = \frac{10 \times 4,350}{2 \times 8,200} = \frac{43,500}{16,400} = 2.65M
$$

**Trade:**

- Buy $10M 5-year
- Sell $11.76M 2-year
- Sell $2.65M 10-year

**Verification:**

- 5-year DV01: +$43,500
- 2-year DV01: -$11.76M × $1,850 = -$21,756
- 10-year DV01: -$2.65M × $8,200 = -$21,730
- **Net DV01: +$43,500 - $21,756 - $21,730 = $14 (≈0, rounding)**

### 2. Butterfly P&L Calculation


**P&L from butterfly move:**

$$
\text{P\&L} = N_b \times \text{DV01}_b \times \Delta r_b - N_s \times \text{DV01}_s \times \Delta r_s - N_l \times \text{DV01}_l \times \Delta r_l
$$

**For DV01-neutral butterfly:**

$$
\text{P\&L} \approx N_b \times \text{DV01}_b \times \left(\Delta r_b - \frac{\Delta r_s + \Delta r_l}{2}\right)
$$

**This is the change in butterfly spread × body DV01**

**Example:**

**Initial:**

- 2s: 4.40%, 5s: 4.15%, 10s: 4.25%
- Butterfly: 4.15% - (4.40%+4.25%)/2 = -17.5 bps

**After 1 month:**

- 2s: 4.35%, 5s: 4.10%, 10s: 4.20%
- Butterfly: 4.10% - (4.35%+4.20%)/2 = -17.75 bps

**Change:**

- Butterfly: -17.5 → -17.75 = -0.25 bps (more negative)

**P&L:**

- Position: Bought fly (long body, short wings)
- Wanted body to cheapen (butterfly more negative) ✓
- Change: -2.5 bps in our favor

$$
\text{P\&L} = \$10M \times \$4,350/\text{bp} \times (-0.0025) = -\$108.75
$$

Wait, this is wrong. Let me recalculate:

If butterfly went from -17.5 to -17.75 bps, it became MORE negative (body cheapened FURTHER).

If we BOUGHT the fly (betting body would cheapen), we profit.

Actually, I need to be careful about signs:

- Bought fly = Long body, short wings
- Body yield fell: 4.15% → 4.10% (richened, NOT what we wanted)
- Wings yields fell: Average (4.40%+4.25%)/2 = 4.325% → (4.35%+4.20%)/2 = 4.275% (richened more)
- Butterfly: -17.5 → -17.75 bps (body RELATIVELY cheaper)

Let me calculate P&L properly:

$$
\text{P\&L} = (+\$43,500) \times (-0.05\%) + (-\$21,756) \times (-0.05\%) + (-\$21,730) \times (-0.05\%)
$$

$$
= -\$2,175 + \$1,088 + \$1,087 = \$0
$$

This makes sense for parallel shift. Let me redo with non-parallel move:

**After 1 month (curve flattens):**

- 2s: 4.30% (-10 bps)
- 5s: 4.12% (-3 bps)
- 10s: 4.28% (+3 bps)

**Butterfly:**

- Initial: -17.5 bps
- Final: 4.12% - (4.30%+4.28%)/2 = 4.12% - 4.29% = -17.0 bps
- **Change: +5 bps (less negative, body richened)**

**P&L:**

- Body: $10M × $4,350 × (-0.03%) = -$13,050 (loss, we're long, yield fell a little)
- 2-year wing: $11.76M × $1,850 × (-0.10%) = -$21,756 (but we're short, so GAIN)
- 10-year wing: $2.65M × $8,200 × (+0.03%) = +$6,519 (but we're short, so LOSS)

$$
\text{P\&L} = -\$13,050 + \$21,756 - \$6,519 = \$2,187
$$

**We profit because:**

- 2-year fell 10 bps (we're short, gain)
- 5-year fell 3 bps (we're long, lose)
- 10-year rose 3 bps (we're short, lose)
- Net: 2-year outperformance drove profit

### 3. Regression-Based Weights


**More sophisticated: Use historical beta**

$$
\Delta r_b = \beta_s \Delta r_s + \beta_l \Delta r_l + \epsilon
$$

**Estimate $\beta_s$ and $\beta_l$ from regression**

**Then weight:**

$$
N_s = \frac{\beta_s \times N_b \times \text{DV01}_b}{\text{DV01}_s}
$$

$$
N_l = \frac{\beta_l \times N_b \times \text{DV01}_b}{\text{DV01}_l}
$$

**This accounts for:**

- 2-year and 10-year don't move equally
- Typically $\beta_s > \beta_l$ (short end more volatile)
- Better hedge of body

---

## Step-by-Step Setup


### 1. Signal Analysis


**1. Calculate Current Butterfly:**

```python
import pandas as pd
import numpy as np

# Current market data
curve = {
    '2Y': 4.40,
    '5Y': 4.15,
    '10Y': 4.25
}

# Simple butterfly
fly = curve['5Y'] - (curve['2Y'] + curve['10Y']) / 2
print(f"Current butterfly: {fly:.2f} bps = {fly*100:.1f} bps")

# Output
```

**2. Historical Analysis:**

```python
# Load historical data
history = pd.read_csv('treasury_history.csv')
history['2s5s10s_fly'] = (
    history['5Y'] - (history['2Y'] + history['10Y']) / 2
)

# Statistics
mean_fly = history['2s5s10s_fly'].mean()
std_fly = history['2s5s10s_fly'].std()
current_fly = -0.175

# Z-score
z_score = (current_fly - mean_fly) / std_fly

print(f"Historical mean: {mean_fly:.4f} ({mean_fly*100:.1f} bps)")
print(f"Historical std: {std_fly:.4f} ({std_fly*100:.1f} bps)")
print(f"Current fly: {current_fly:.4f} ({current_fly*100:.1f} bps)")
print(f"Z-score: {z_score:.2f}")

# Example output
# Historical mean
# Historical std
# Current fly
# Z-score
```

**3. Visualize:**

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 6))
plt.plot(history.index, history['2s5s10s_fly'] * 100, label='Butterfly')
plt.axhline(mean_fly * 100, color='green', linestyle='--', label='Mean')
plt.axhline((mean_fly + std_fly) * 100, color='gray', linestyle=':', label='+1 Std')
plt.axhline((mean_fly - std_fly) * 100, color='gray', linestyle=':', label='-1 Std')
plt.axhline(current_fly * 100, color='red', linewidth=2, label='Current')
plt.xlabel('Date')
plt.ylabel('Butterfly Spread (bps)')
plt.title('2s5s10s Butterfly - Historical Analysis')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

**4. Decision:**

```python
if abs(z_score) > 2.0:
    print("STRONG SIGNAL - Execute trade")
    signal = "strong"
elif abs(z_score) > 1.0:
    print("MODERATE SIGNAL - Consider trade")
    signal = "moderate"
else:
    print("WEAK SIGNAL - Pass")
    signal = "weak"

if signal in ["strong", "moderate"]:
    if z_score < 0:
        direction = "BUY"  # Fly is cheap, buy body
    else:
        direction = "SELL"  # Fly is rich, sell body
    
    print(f"Direction: {direction} the butterfly")
```

### 2. DV01 Construction


**1. Gather DV01s:**

```python
# DV01 per $1M notional
dv01 = {
    '2Y': 1850,
    '5Y': 4350,
    '10Y': 8200
}

# Target body size
body_notional = 10_000_000  # $10M
body_dv01_total = body_notional * dv01['5Y'] / 1_000_000
print(f"Body total DV01: ${body_dv01_total:,.0f}")
```

**2. Calculate Wing Sizes:**

```python
# Equal DV01 in each wing (standard)
wing_dv01_each = body_dv01_total / 2

# Short wing (2-year) notional
short_wing_notional = (wing_dv01_each / dv01['2Y']) * 1_000_000

# Long wing (10-year) notional
long_wing_notional = (wing_dv01_each / dv01['10Y']) * 1_000_000

print(f"Body (5Y): ${body_notional:,.0f}")
print(f"Short wing (2Y): ${short_wing_notional:,.0f}")
print(f"Long wing (10Y): ${long_wing_notional:,.0f}")

# Verify DV01 neutral
net_dv01 = (
    body_dv01_total 
    - (short_wing_notional / 1_000_000 * dv01['2Y'])
    - (long_wing_notional / 1_000_000 * dv01['10Y'])
)
print(f"Net DV01: ${net_dv01:,.0f} (should be ~0)")
```

**Output:**

```
Body total DV01: $43,500
Body (5Y): $10,000,000
Short wing (2Y): $11,756,757
Long wing (10Y): $2,652,439
Net DV01: $0 (should be ~0)
```

### 3. Trade Execution


**1. Prepare Orders:**

```python
# Determine direction
if direction == "BUY":
    body_action = "BUY"
    wing_action = "SELL"
else:
    body_action = "SELL"
    wing_action = "BUY"

# Create order tickets
orders = pd.DataFrame({
    'Security': ['2Y Note', '5Y Note', '10Y Note'],
    'Action': [wing_action, body_action, wing_action],
    'Notional': [
        short_wing_notional,
        body_notional,
        long_wing_notional
    ],
    'Yield': [curve['2Y'], curve['5Y'], curve['10Y']],
    'DV01': [
        short_wing_notional / 1_000_000 * dv01['2Y'],
        body_dv01_total,
        long_wing_notional / 1_000_000 * dv01['10Y']
    ]
})

print(orders)
```

**2. Execution Strategy:**

```python
def execute_butterfly(orders, execution_style='simultaneous'):
    """
    Execute butterfly trade
    
    Styles:
    - 'simultaneous': All legs at once (best for small size)
    - 'leg_in': Body first, then wings (risk: curve moves)
    - 'spread': Submit as package trade (professional)
    """
    
    if execution_style == 'simultaneous':
        # Market orders all legs
        print("Executing all legs simultaneously...")
        # Submit orders...
        
    elif execution_style == 'leg_in':
        # Execute body first (get the view on)
        print("Executing body first...")
        # Then wings
        print("Hedging with wings...")
        
    elif execution_style == 'spread':
        # Submit as spread to dealer
        print("Requesting spread quote...")
        # Dealer prices entire butterfly
        
    return "Executed"
```

### 4. Monitoring & Exit


**1. Daily P&L Tracking:**

```python
def calculate_butterfly_pnl(initial_position, current_curve):
    """Calculate current P&L on butterfly"""
    
    # Current butterfly spread
    current_fly = (
        current_curve['5Y'] 
        - (current_curve['2Y'] + current_curve['10Y']) / 2
    )
    
    # Initial butterfly
    initial_fly = -0.0175  # From entry
    
    # Change in butterfly (bps)
    fly_change = current_fly - initial_fly
    
    # P&L (if bought the fly)
    if direction == "BUY":
        # Profit if fly becomes more negative (body cheapens)
        pnl = -fly_change * body_dv01_total * 100  # Convert to bps
    else:
        # Profit if fly becomes more positive (body richens)
        pnl = fly_change * body_dv01_total * 100
    
    return pnl, current_fly, fly_change

# Example
current_curve = {'2Y': 4.35, '5Y': 4.12, '10Y': 4.28}
pnl, curr_fly, change = calculate_butterfly_pnl(orders, current_curve)

print(f"Current butterfly: {curr_fly*100:.1f} bps")
print(f"Change: {change*100:.1f} bps")
print(f"P&L: ${pnl:,.0f}")
```

**2. Risk Monitoring:**

```python
def calculate_risk_metrics(position, current_curve):
    """Monitor ongoing risk"""
    
    # DV01 (should stay near 0)
    net_dv01 = calculate_net_dv01(position)
    
    # Carry (daily income/cost)
    carry = calculate_daily_carry(position, current_curve)
    
    # Volatility
    butterfly_vol = calculate_butterfly_volatility(history)
    
    # VaR (95%, 1-day)
    var_95 = 1.65 * butterfly_vol * body_dv01_total
    
    return {
        'Net_DV01': net_dv01,
        'Daily_Carry': carry,
        'Butterfly_Vol': butterfly_vol * 100,  # bps
        'VaR_95': var_95
    }
```

**3. Exit Criteria:**

```python
def check_exit_conditions(current_fly, entry_fly, pnl, days_held):
    """Determine if should exit"""
    
    # Profit target: 50% reversion to mean
    target_fly = entry_fly + (mean_fly - entry_fly) * 0.5
    
    # Stop loss: 2x initial mispricing
    stop_fly = entry_fly - (entry_fly - mean_fly) * 2
    
    # Time stop: 90 days
    max_days = 90
    
    if direction == "BUY":
        # Bought fly (betting body cheapens)
        if current_fly <= target_fly:
            return True, "PROFIT_TARGET"
        elif current_fly >= stop_fly:
            return True, "STOP_LOSS"
    else:
        # Sold fly (betting body richens)
        if current_fly >= target_fly:
            return True, "PROFIT_TARGET"
        elif current_fly <= stop_fly:
            return True, "STOP_LOSS"
    
    if days_held >= max_days:
        return True, "TIME_STOP"
    
    return False, "HOLD"

# Example
should_exit, reason = check_exit_conditions(
    current_fly=-0.0170,  # Current
    entry_fly=-0.0175,    # Entry
    pnl=2187,             # Current P&L
    days_held=15
)

print(f"Exit: {should_exit}, Reason: {reason}")
```

### 5. Unwind & Review


**1. Exit Execution:**

```python
# Unwind all legs simultaneously
exit_orders = orders.copy()
exit_orders['Action'] = exit_orders['Action'].apply(
    lambda x: 'SELL' if x == 'BUY' else 'BUY'
)

print("Unwinding butterfly...")
print(exit_orders)
```

**2. Trade Review:**

```python
# Document trade
trade_log = {
    'Entry_Date': '2024-12-01',
    'Exit_Date': '2024-12-15',
    'Days_Held': 14,
    'Entry_Fly': -17.5,  # bps
    'Exit_Fly': -17.0,   # bps
    'Fly_Change': +0.5,  # bps
    'Entry_Reason': 'Z-score -1.04, body cheap',
    'Exit_Reason': 'Profit target hit',
    'P&L': 2187,
    'Return_on_Risk': 2187 / 43500  # P&L / DV01
}

print(pd.DataFrame([trade_log]))

# Calculate metrics
annualized_return = (trade_log['P&L'] / body_notional) * (365 / trade_log['Days_Held'])
print(f"Annualized return: {annualized_return:.2%}")
```

---

## Real-World Examples


### 1. Duration Cut via Futures


**Background:**

- Fed hiking aggressively (4 hikes of 0.25% done, more coming)
- Curve inverting
- 2s5s10s butterfly very negative (5-year cheap)

**Market levels (June 1, 2022):**

| Maturity | Yield | DV01/1M |
|----------|-------|---------|
| 2Y | 2.70% | $1,900 |
| 5Y | 2.90% | $4,400 |
| 10Y | 2.95% | $8,300 |

**Butterfly:**

$$
\text{Fly} = 2.90\% - \frac{2.70\% + 2.95\%}{2} = 2.90\% - 2.825\% = +7.5 \text{ bps}
$$

**Historical analysis:**

- Mean: -5 bps
- Current: +7.5 bps
- **Body is RICH (12.5 bps above average)**

**Trade decision: Sell the fly**

- Sell $10M 5-year
- Buy $11.6M 2-year
- Buy $2.65M 10-year

**Thesis:**

- Fed will keep hiking
- 2-year will rise MORE than 5-year (front end sensitive)
- Butterfly will go negative
- **Profit from body cheapening**

**Outcome (3 months later, September 2022):**

| Maturity | June | September | Change |
|----------|------|-----------|--------|
| 2Y | 2.70% | 4.25% | +155 bps |
| 5Y | 2.90% | 4.00% | +110 bps |
| 10Y | 2.95% | 3.85% | +90 bps |

**New butterfly:**

$$
\text{Fly} = 4.00\% - \frac{4.25\% + 3.85\%}{2} = 4.00\% - 4.05\% = -5 \text{ bps}
$$

**Butterfly moved: +7.5 → -5.0 = -12.5 bps (body cheapened)**

**P&L:**

- Sold fly at +7.5 bps
- Bought back at -5.0 bps
- **Profit: 12.5 bps × $10M × $4,400/bp = $55,000**

**Why it worked:**

1. Correctly anticipated Fed would keep hiking
2. 2-year rose 155 bps (most sensitive to Fed)
3. 5-year rose only 110 bps
4. Body cheapened as expected

### 2. Transition Risk Hedge


**Background:**

- COVID crash
- Fed announces unlimited QE (buying long-dated Treasuries)
- Curve distorted

**Market levels (March 15, 2020):**

| Maturity | Yield | DV01/1M |
|----------|-------|---------|
| 5Y | 0.70% | $4,600 |
| 10Y | 0.85% | $9,200 |
| 30Y | 1.55% | $21,500 |

**Butterfly:**

$$
\text{Fly} = 0.85\% - \frac{0.70\% + 1.55\%}{2} = 0.85\% - 1.125\% = -27.5 \text{ bps}
$$

**Historical analysis:**

- Mean: -10 bps
- Current: -27.5 bps
- **10-year is CHEAP (17.5 bps below average)**

**Trade decision: Buy the fly**

- Buy $10M 10-year
- Sell $9.78M 5-year
- Sell $4.28M 30-year

**Thesis:**

- Butterfly mean-reverses
- 10-year will richen vs. wings
- Earn +17.5 bps reversion

**What happened: Fed QE distortion**

**Fed announces (March 23):**

- Unlimited QE
- Buying $75B/day of Treasuries
- **Heavy concentration in 10-year and 30-year**

**Outcome (April 15, 2020):**

| Maturity | March 15 | April 15 | Change |
|----------|----------|----------|--------|
| 5Y | 0.70% | 0.35% | -35 bps |
| 10Y | 0.85% | 0.65% | -20 bps |
| 30Y | 1.55% | 1.35% | -20 bps |

**New butterfly:**

$$
\text{Fly} = 0.65\% - \frac{0.35\% + 1.35\%}{2} = 0.65\% - 0.85\% = -20 \text{ bps}
$$

**Butterfly moved: -27.5 → -20.0 = +7.5 bps (body richened)**

But we BOUGHT the fly (wanted body to cheapen), so we're LOSING:

**P&L:**

- Bought fly at -27.5 bps
- Current: -20.0 bps
- **Loss: 7.5 bps × $10M × $9,200/bp = -$69,000**

Wait, let me recalculate P&L properly:

**Position:**

- Long $10M 10-year: +$92,000 DV01
- Short $9.78M 5-year: -$45,000 DV01
- Short $4.28M 30-year: -$92,000 DV01
- Net DV01: ~$0

**Changes:**

- 10-year: -20 bps (we're long, GAIN: +$92,000 × 20 = +$1,840)
- 5-year: -35 bps (we're short, LOSS: -$45,000 × 35 = -$1,575)
- 30-year: -20 bps (we're short, LOSS: -$92,000 × 20 = -$1,840)

Actually, I need to be more careful:

- 10-year fell 20 bps → Price rose → We're long → GAIN
- 5-year fell 35 bps → Price rose MORE → We're short → LOSS
- 30-year fell 20 bps → Price rose → We're short → LOSS

Net effect: 5-year outperformed (fell 35 bps vs 20 bps for body)

This HURT us because we were short 5-year.

**Simplified P&L:**

The butterfly richened (+7.5 bps), but we wanted it to cheapen.

$$
\text{Loss} \approx 7.5 \text{ bps} \times \$92,000 \text{ body DV01} = -\$6,900
$$

**Why it failed:**

1. Fed QE completely distorted normal relationships
2. Massive buying of 10-year and 30-year (richened them)
3. 5-year not as heavily targeted (cheapened relatively)
4. **Couldn't predict Fed's specific buying pattern**

**Lesson: Don't fight Fed QE programs with butterfly trades**

### 3. Portable Alpha with Futures


**Background:**

- Fed cutting for first time in 4 years
- Front end of curve expected to rally hard

**Market levels (September 17, 2024, pre-Fed):**

| Maturity | Yield | DV01/1M |
|----------|-------|---------|
| 3M | 5.30% | $250 |
| 2Y | 4.00% | $1,900 |
| 5Y | 3.75% | $4,500 |

**Butterfly (3m2s5s):**

$$
\text{Fly} = 4.00\% - \frac{5.30\% + 3.75\%}{2} = 4.00\% - 4.525\% = -52.5 \text{ bps}
$$

**Analysis:**

- 2-year is EXTREMELY cheap vs. 3-month and 5-year
- Huge inversion at front end (3-month at 5.30% vs 2-year at 4.00%)
- Fed about to cut → Front end will rally

**Trade: Buy the fly**

- Buy $10M 2-year
- Sell $76M 3-month (large notional due to low DV01!)
- Sell $4.2M 5-year

**Fed decision (September 18, 2:00 PM):**

**Cut 0.50% (surprise, expected 0.25%)**

**Immediate reaction:**

| Maturity | Pre-Fed | Post-Fed | Change |
|----------|---------|----------|--------|
| 3M | 5.30% | 4.75% | -55 bps |
| 2Y | 4.00% | 3.70% | -30 bps |
| 5Y | 3.75% | 3.60% | -15 bps |

**New butterfly:**

$$
\text{Fly} = 3.70\% - \frac{4.75\% + 3.60\%}{2} = 3.70\% - 4.175\% = -47.5 \text{ bps}
$$

**Butterfly moved: -52.5 → -47.5 = +5.0 bps (body richened)**

**P&L:**

- Bought fly at -52.5 bps
- Now at -47.5 bps
- **Profit: 5.0 bps × $10M × $1,900/bp = $9,500 in 24 hours**

**Why it worked:**

1. 3-month fell 55 bps (Fed cut + expectations for more cuts)
2. 2-year fell only 30 bps (already priced in some cuts)
3. 5-year fell 15 bps (long end less affected)
4. **2-year richened vs. wings as expected**

### 4. Tactical Duration Extension


**Background:**

- 2023: Low volatility, stable Fed policy
- Opportunity for carry trades in butterflies

**Market levels (January 2023):**

| Maturity | Yield | DV01/1M |
|----------|-------|---------|
| 2Y | 4.50% | $1,880 |
| 5Y | 4.10% | $4,380 |
| 10Y | 3.90% | $8,350 |

**Butterfly:**

$$
\text{Fly} = 4.10\% - \frac{4.50\% + 3.90\%}{2} = 4.10\% - 4.20\% = -10 \text{ bps}
$$

**Analysis:**

- Body slightly cheap (normal range -5 to +5 bps)
- But more importantly: **Positive carry**

**Carry calculation:**

**Position: Buy the fly**

- Long $10M 5-year @ 4.10% yield
- Short $11.7M 2-year @ 4.50% yield
- Short $2.62M 10-year @ 3.90% yield

**Annual carry:**

- Earn on 5-year: $10M × 4.10% = $410,000
- Pay on 2-year: $11.7M × 4.50% = -$526,500
- Pay on 10-year: $2.62M × 3.90% = -$102,180
- **Net carry: $410k - $526.5k - $102.2k = -$218,700/year**

Wait, that's negative carry! Let me reconsider.

Actually, when you're SHORT a bond, you RECEIVE the yield (repo income exceeds coupon cost typically).

Let me recalculate considering repo rates:

**Assuming repo rate = 4.75% (above short-term yields):**

- Earn on 5-year: $10M × 4.10% = $410,000
- Repo cost on 2-year short: $11.7M × (4.75% - 4.50%) = $11.7M × 0.25% = $29,250 cost
- Repo cost on 10-year short: $2.62M × (4.75% - 3.90%) = $2.62M × 0.85% = $22,270 cost

**Net carry: $410k - $29.3k - $22.3k = $358k/year**

This is still not right. Let me think about carry more carefully:

For a butterfly, carry is typically:

$$
\text{Carry} = r_{\text{body}} - \frac{r_{\text{short wing}} + r_{\text{long wing}}}{2}
$$

Which is just the butterfly spread!

So:

**Daily carry = -10 bps per year = -10/365 = -0.027 bps/day**

On $10M body:

**Daily carry = -0.027 bps × $10M × $4,380/bp = -$1.2/day**

Minimal, but negative.

**Outcome (hold for 6 months):**

- Butterfly stays at -10 bps (range-bound)
- Carry cost: -$1.2 × 180 days = -$216
- Curve doesn't move, no P&L from spread change
- **Net: Small loss from negative carry**

**Lesson: Butterflies don't offer significant carry unless spread is extreme**

### 5. Duration Hedge Failure


**Background:**

- US Treasury issuing record amounts of long-dated debt (COVID stimulus)
- 20-year sector under pressure from supply

**Market levels (May 2020):**

| Maturity | Yield | DV01/1M |
|----------|-------|---------|
| 10Y | 0.70% | $9,100 |
| 20Y | 1.15% | $16,800 |
| 30Y | 1.45% | $21,200 |

**Butterfly:**

$$
\text{Fly} = 1.15\% - \frac{0.70\% + 1.45\%}{2} = 1.15\% - 1.075\% = +7.5 \text{ bps}
$$

**Analysis:**

- 20-year is RICH (yields less than average)
- But Treasury issuing $50B of new 20-year bonds
- **Supply will cheapen 20-year**

**Trade: Sell the fly**

- Sell $10M 20-year
- Buy $13.2M 10-year
- Buy $7.92M 30-year

**Thesis: Supply pressure cheapens 20-year**

**Outcome (auction day, May 20):**

**Before auction:**

- Butterfly: +7.5 bps

**After auction (poor demand, yields spike):**

- 10Y: 0.70% → 0.68% (-2 bps, rallied)
- 20Y: 1.15% → 1.28% (+13 bps, sold off!)
- 30Y: 1.45% → 1.48% (+3 bps)

**New butterfly:**

$$
\text{Fly} = 1.28\% - \frac{0.68\% + 1.48\%}{2} = 1.28\% - 1.08\% = +20 \text{ bps}
$$

**Butterfly moved: +7.5 → +20.0 = +12.5 bps (body cheapened massively)**

**P&L:**

- Sold fly at +7.5 bps
- Now at +20.0 bps
- **Profit: 12.5 bps × $10M × $16,800/bp = $210,000 in 1 day!**

**Why it worked:**

1. Anticipated supply pressure on 20-year
2. Auction went poorly (weak demand)
3. 20-year sold off 13 bps
4. 10-year and 30-year barely moved
5. **Body cheapened dramatically as predicted**

**Lesson: Supply dynamics can create powerful butterfly opportunities**

---



## Final Wisdom


> "Butterfly trades are the fixed income equivalent of picking up nickels in front of a steamroller—most of the time you collect the nickels (small mean-reversion profits), but occasionally the steamroller runs you over (Fed QE, structural shift). The math is elegant: buy the body at -15 bps butterfly, sell at -5 bps, pocket 10 bps × your DV01. But here's the trap: the mean can shift. In 2010-2020, Fed QE permanently altered curvature relationships. Butterflies that 'always' mean-reverted to +2 bps suddenly lived at +15 bps for years. Traders who sold that fly at +7 bps thinking it was rich got steamrolled to +20 bps before Fed finally tapered. The key is respecting regime changes: during normal times (no QE, stable Fed), butterflies are reliable mean-reversion trades with 65% win rates. During QE or structural shifts, all bets are off—historical means are meaningless, and fighting the Fed is financial suicide. Trade butterflies when the regime is stable, size conservatively (2-3% DV01), use hard stops (2x initial mispricing), and for God's sake, don't average down when the Fed is distorting curves. The butterfly will mean-revert... eventually. Just make sure you're still solvent when it does."

**Key to success:**

- Calculate butterfly spread (body - average of wings)
- Compare to historical mean (use 3-5 year rolling window)
- Z-score > 1.5 for entry signal
- Construct DV01-neutral position (wings offset body)
- Size conservatively (body DV01 = 2-3% account max)
- Set stop loss (2x initial mispricing)
- Exit at 50% reversion to mean
- Never fight Fed QE (respect structural shifts)

**Most important:** Butterflies are a professional's game. The math is simple, but the regime identification is hard. Know when you're in a mean-reverting environment (stable Fed, no QE, normal markets) vs. a structural shift (QE, crisis, major policy change). In mean-reverting regimes, butterflies are money machines. In structural shifts, they're widow-makers. Size small, stop tight, and live to trade another butterfly. 🦋📉📈