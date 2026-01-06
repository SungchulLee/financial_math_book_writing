# Carry Factor Portfolios

**Carry factor portfolios** are systematic investment strategies that construct diversified baskets of long and short futures positions across multiple asset classes (commodities, rates, currencies, equities) to harvest the persistent risk premium associated with holding assets in backwardation or high-yielding currencies, exploiting the tendency for positive carry positions to generate excess returns over time.

---

## The Core Insight

**The fundamental idea:**

- Carry is a well-documented risk premium in futures markets
- Positive carry = Paid to hold a position (backwardation, high yield)
- Negative carry = Pay to hold a position (contango, low yield)
- Long high-carry assets, short low-carry assets
- Diversify across 20-50 futures markets
- Risk premium persists over decades
- Not market timing—systematic factor exposure
- Sharpe ratios of 0.6-1.2 (institutional quality)

**The key equation:**

$$
\text{Carry Return} = \sum_{i=1}^{N} w_i \times \text{Carry}_i
$$

Where:
- $w_i$ = Weight in asset $i$ (long if high carry, short if low carry)
- $\text{Carry}_i$ = Expected return from holding asset $i$

**Portfolio construction:**

$$
w_i = \frac{\text{sgn}(\text{Carry}_i)}{\text{Volatility}_i} \times \frac{1}{N}
$$

**You're essentially: "Systematically collecting rent from the futures curve while diversifying across uncorrelated markets."**

---

## What Is a Carry Factor Portfolio?

**Before building carry portfolios, understand the mechanics:**

### 1. Core Concept

**Definition:** A systematic multi-asset futures portfolio that captures the carry risk premium by going long high-carry contracts (backwardated commodities, high-yielding currencies, steep bond curves) and short low-carry contracts (contango commodities, low-yielding currencies, flat bond curves), with positions sized inversely to volatility to create equal risk contribution across diverse markets.

**When you run a carry portfolio:**

- You trade 20-50+ futures markets simultaneously
- You rank markets by carry (high to low)
- You go long top quintile (high carry)
- You go short bottom quintile (low carry)
- You rebalance monthly or quarterly
- You size by inverse volatility (risk parity)
- You hold for the risk premium, not directional views

**Example - Simple 5-Asset Carry Portfolio:**

**Universe (ranked by carry, June 2024):**

| Asset | Carry | Rank | Position | Rationale |
|-------|-------|------|----------|-----------|
| Natural Gas (NG) | -15% ann. | 1 (highest) | **Long** | Deep backwardation (winter demand) |
| Brazilian Real (BRL) | +8% ann. | 2 | **Long** | High interest rate differential |
| Crude Oil (CL) | -6% ann. | 3 | **Long** | Backwardation (supply tight) |
| Gold (GC) | +0.5% ann. | 4 | Neutral | Near zero carry |
| Japanese Yen (JPY) | +3% ann. | 5 (lowest) | **Short** | Negative carry (US rates > Japan) |

**Position construction:**

```
Long Natural Gas: High carry (-15% = collecting backwardation)
Long Brazilian Real: High interest rate
Long Crude Oil: Backwardation
Short Japanese Yen: Low interest rate (pay to hold)
```

**Monthly carry collection:**

- Natural Gas: -15% / 12 = -1.25%/month (earn backwardation)
- BRL: +8% / 12 = +0.67%/month (earn interest differential)
- Crude Oil: -6% / 12 = -0.50%/month (earn backwardation)
- JPY: -3% / 12 = -0.25%/month (pay to short high-yield)

**Net portfolio carry: ~2.0% per month if all held unchanged**

**Note:** Carry is the expected return from HOLDING. Actual returns include carry + price changes.

### 2. Carry Across Asset Classes

**How carry manifests in different markets:**

**1. Commodities (term structure carry):**

$$
\text{Carry} = \frac{F_1 - F_2}{F_1} \times 12 \quad \text{(annualized)}
$$

Where $F_1$ = Front month, $F_2$ = Second month

**Backwardation (negative carry, LONG is favorable):**

- Front month > Deferred month
- Example: Natural gas $6.00 (front) vs. $5.00 (2nd month)
- Carry: ($6.00 - $5.00) / $6.00 × 12 = -200% annualized (!) 
  
  Wait, that's not right. Let me recalculate:

If holding the front month contract for 1 month until it expires, and you roll to the second month, you're selling at $6.00 and buying at $5.00.

Actually, carry should be calculated as:

$$
\text{Carry} = \frac{F_2 - F_1}{F_1} \times 12
$$

For backwardation: $F_1 = 6.00$, $F_2 = 5.00$
$$
\text{Carry} = \frac{5.00 - 6.00}{6.00} \times 12 = \frac{-1.00}{6.00} \times 12 = -0.167 \times 12 = -2.0 = -200\%
$$

Hmm, that still seems very high. Let me think about this differently.

The carry for a 1-month position is:
$$
\text{1-month carry} = \frac{F_2 - F_1}{F_1}
$$

For backwardation with $F_1 = 6.00$ and $F_2 = 5.00$:
$$
\text{1-month carry} = \frac{5.00 - 6.00}{6.00} = -16.7\%
$$

Annualized: $-16.7\% \times 12 = -200\%$

This seems extreme but can happen in commodities during severe shortages.

More typical example:
- Crude oil: $80 (front) vs. $81 (2nd month) = Contango
- 1-month carry: ($81 - $80) / $80 = +1.25%
- Annualized: +15% carry (you LOSE 15%/year to contango)

**2. Currencies (interest rate differential):**

$$
\text{Carry} = r_{\text{domestic}} - r_{\text{foreign}}
$$

**Example - USD/BRL:**

- Brazil rate: 13.75%
- US rate: 5.25%
- Carry: 13.75% - 5.25% = +8.50% annualized
- **Long BRL earns +8.50% per year (if FX unchanged)**

**3. Interest rates (term premium):**

$$
\text{Carry} = \text{Yield} - \text{Funding Cost}
$$

**Example - 10-year Treasury:**

- 10-year yield: 4.00%
- Funding (overnight): 5.25%
- Carry: 4.00% - 5.25% = -1.25%
- **Negative carry (paying to hold long duration)**

**4. Equity indices (dividend yield):**

$$
\text{Carry} = \text{Dividend Yield} - \text{Funding Cost}
$$

**Example - S&P 500:**

- Dividend yield: 1.5%
- Funding: 5.25%
- Carry: 1.5% - 5.25% = -3.75%
- **Negative carry in high-rate environment**

### 3. Why Carry Exists as a Risk Premium

**Economic rationale:**

**1. Insurance premium (commodities):**

- Producers need to hedge future production
- Willing to sell forward below expected spot
- Hedgers pay buyers (speculators) to take price risk
- **Positive carry = Compensation for providing insurance**

**2. Convenience yield:**

- Physical commodity has value (can use immediately)
- Futures contract does not
- When supply tight, convenience yield high
- **Backwardation = High convenience yield**

**3. Storage costs:**

- Storing physical commodity has costs
- Futures require no storage
- **Contango = Storage costs > convenience yield**

**4. Risk premium (currencies):**

- High interest rates often in risky countries
- Carry compensates for FX depreciation risk
- **Crash risk embedded in carry**

**5. Liquidity preference (rates):**

- Investors prefer short-term (liquid) bonds
- Demand premium to hold long-term (illiquid)
- **Term premium = Carry for duration risk**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/carry_factor_portfolios.png?raw=true" alt="carry_factor_portfolios" width="700">
</p>
**Figure 1:** Carry factor portfolios showing the distribution of carry across different asset classes, a typical long-short portfolio construction with positions ranked by carry, and the historical Sharpe ratio of diversified carry strategies demonstrating the persistent risk premium across commodities, currencies, rates, and equities.

---

## Economic Interpretation

**Beyond the basic mechanics, understanding the REAL economics:**

### 1. The Theory of Storage

**The deep insight:**

The relationship between spot and futures prices is governed by **cost of carry**:

$$
F = S \cdot e^{(r + u - y)T}
$$

Where:
- $F$ = Futures price
- $S$ = Spot price
- $r$ = Risk-free rate (financing cost)
- $u$ = Storage cost
- $y$ = Convenience yield
- $T$ = Time to maturity

**Contango (normal market):**

$$
r + u > y \Rightarrow F > S
$$

- Storage costs + financing > convenience of holding physical
- Futures trade at premium to spot
- **Carry is negative (you lose to roll)**

**Backwardation (tight market):**

$$
y > r + u \Rightarrow F < S
$$

- Convenience yield > storage + financing
- Futures trade at discount to spot
- **Carry is positive (you gain to roll)**

**Example - Crude oil in different regimes:**

**Contango (2020 COVID surplus):**

- Spot: $30/bbl
- 6-month futures: $35/bbl
- Storage cost: $2/bbl (tanks full, expensive)
- Convenience yield: Near zero (abundant supply)
- **Futures > Spot: Negative carry**

**Backwardation (2022 Ukraine war):**

- Spot: $120/bbl
- 6-month futures: $105/bbl
- Storage cost: $2/bbl (same)
- Convenience yield: Very high (need oil NOW)
- **Futures < Spot: Positive carry**

**Trading implication:**

- Long backwardation (positive carry) = Collect $15/bbl over 6 months
- Short contango (avoid negative carry) = Earn $5/bbl over 6 months
- **Systematic long-short captures spread**

### 2. The Hedging Pressure Hypothesis

**Why backwardation persists:**

Commodity producers need to **hedge future production**:

1. Oil company will produce 1M barrels in 6 months
2. Wants to lock in price today (eliminate uncertainty)
3. Sells 6-month futures to hedgers
4. **Willing to sell below expected spot to guarantee price**

**Speculators (us) are counterparty:**

- We buy futures from hedgers
- We take on price risk
- We demand compensation (risk premium)
- **Premium = Positive carry (backwardation)**

**Empirical evidence:**

**Markets with heavy hedging pressure:**

- Energy (producers hedge aggressively)
- Agriculture (farmers hedge crops)
- Metals (miners hedge production)
- **These show persistent backwardation**

**Markets with light hedging:**

- Financials (less physical hedging need)
- Equities (can't hedge production)
- **These show less consistent carry**

### 3. Uncovered Interest Parity (UIP) Failure

**UIP theory (textbook):**

$$
\mathbb{E}[S_{t+1}] = S_t \cdot \frac{1 + r_{\text{domestic}}}{1 + r_{\text{foreign}}}
$$

**Translation:** High interest rate currencies should depreciate

**Reality (UIP violation):**

High interest rate currencies tend to **APPRECIATE** (not depreciate)!

**Example - Carry trade (1990-2020):**

- Strategy: Borrow JPY (0%), invest in AUD (5%)
- UIP predicts: AUD depreciates 5% → No profit
- Reality: AUD appreciates on average → Double profit!
- **Carry + Appreciation = ~10-15% annual returns**

**Why UIP fails:**

1. **Risk premium:** High rates in risky countries (justified)
2. **Crash risk:** Carry works until it doesn't (2008)
3. **Central bank intervention:** Prevents full adjustment
4. **Momentum:** Carry begets more carry (flows)

**Trading implication:**

- UIP failure = Systematic profit from carry
- But crash risk is REAL (1998, 2008, 2020)
- **Diversification critical to survive crashes**

### 4. The Carry Risk

**The "Peso Problem" (Rietz, 1988):**

Carry strategies earn steady returns punctuated by **rare, catastrophic losses**:

$$
\mathbb{E}[\text{Return}] = (1-p) \times r_{\text{carry}} + p \times r_{\text{crash}}
$$

Where:
- $p$ = Probability of crash (small, ~2% per year)
- $r_{\text{carry}}$ = Normal return (+10-15%)
- $r_{\text{crash}}$ = Crash return (-50% to -80%)

**Example - Carry trade crash (October 2008):**

**Normal times (Jan 2007 - Sep 2008):**

- Carry portfolio: +12% per year
- Sharpe: 1.2 (excellent)
- Drawdown: <5%
- **Everything looks great**

**Crisis (October 2008):**

- Lehman bankruptcy
- Global deleveraging
- Carry unwind: -35% in ONE MONTH
- **Years of gains wiped out**

**The distribution:**

- 98% of months: +1% to +2% (steady)
- 2% of months: -20% to -40% (crashes)
- **Negative skewness, fat left tail**

**Managing peso risk:**

1. **Diversification:** 50+ markets (reduces single-market crash)
2. **Volatility targeting:** Reduce exposure in high vol
3. **Trend overlay:** Exit positions showing price deterioration
4. **Options:** Buy OTM puts as crash insurance
5. **Accept it:** Carry IS crash risk premium (can't eliminate)

### 5. Cross-Sectional vs. Time-Series Carry

**Two implementations:**

**Cross-sectional (relative carry):**

$$
\text{Long: Top 20\% carry, Short: Bottom 20\% carry}
$$

- Market-neutral (dollar-neutral, beta-neutral)
- Captures spread between high and low carry
- **Lower volatility, more stable**

**Time-series (absolute carry):**

$$
\begin{cases}
\text{Long if carry} > 0 \\
\text{Short if carry} < 0
\end{cases}
$$

- Not market-neutral (can be net long or short)
- Captures absolute carry level
- **Higher returns, higher volatility**

**Example - Crude oil:**

**Cross-sectional approach:**

- Carry rank: Middle (neither highest nor lowest)
- Position: Neutral (don't trade)
- **Misses positive carry!**

**Time-series approach:**

- Carry: -5% (backwardation, positive carry)
- Position: Long
- **Captures absolute carry**

**Institutional portfolios often combine:**

- 50% cross-sectional (stability)
- 50% time-series (absolute returns)
- **Balanced approach**

---

## Key Terminology

**Carry:**

- Expected return from holding a position
- NOT including price changes
- Measured as roll yield, interest differential, or yield curve slope
- Annualized for comparison across markets

**Backwardation:**

- Futures < Spot (downward-sloping curve)
- Positive carry (earn when rolling)
- Common when supply tight
- Favorable for long positions

**Contango:**

- Futures > Spot (upward-sloping curve)
- Negative carry (lose when rolling)
- Common when supply abundant
- Favorable for short positions (avoid long)

**Roll Yield:**

- Profit/loss from rolling futures contracts
- In backwardation: Positive (buy cheaper future)
- In contango: Negative (buy more expensive future)
- Core component of commodity carry

**Risk Parity:**

- Position sizing by inverse volatility
- Equal risk contribution across assets
- Formula: $w_i \propto 1/\sigma_i$
- Prevents high-vol assets from dominating

**Sharpe Ratio:**

- Risk-adjusted return metric
- Formula: (Return - RF) / Volatility
- Carry portfolios: 0.6-1.2 typical
- Benchmark: S&P 500 = 0.3-0.5

**Skewness:**

- Measure of asymmetry in returns
- Carry strategies: Negative skew (-0.5 to -1.5)
- Means: More frequent small gains, rare large losses
- "Picking up pennies in front of steamroller"

**Maximum Drawdown:**

- Peak-to-trough decline
- Carry portfolios: 20-40% typical
- Worse during crises (50-60%)
- Key risk metric

**Hedging Pressure:**

- Imbalance between hedgers and speculators
- Producers short → Need buyers → Premium
- Creates persistent carry opportunity
- Measured by COT (Commitment of Traders) data

**Convenience Yield:**

- Non-monetary benefit of holding physical
- High when supply tight (urgent need)
- Leads to backwardation
- Cannot be directly observed (implied from prices)

---

## Mathematical Foundation

### 1. Carry Calculation by Asset Class

**Commodities (roll yield):**

$$
\text{Carry}_{\text{commodity}} = \frac{F_1 - F_2}{F_1} \times \frac{12}{\Delta T}
$$

Where:
- $F_1$ = Front contract price
- $F_2$ = Next contract price
- $\Delta T$ = Months between contracts

**Example - Natural gas:**

- Front (December): $6.00/MMBtu
- Next (January): $5.40/MMBtu
- Time: 1 month apart

$$
\text{Carry} = \frac{6.00 - 5.40}{6.00} \times 12 = 0.10 \times 12 = 1.20 = 120\% \text{ annualized}
$$

**Negative carry (backwardation) = GOOD (long position earns)**

**Currencies (interest rate differential):**

$$
\text{Carry}_{\text{FX}} = r_{\text{base}} - r_{\text{quote}}
$$

**Example - AUD/USD:**

- AUD rate: 4.35%
- USD rate: 5.25%
- Carry: 4.35% - 5.25% = -0.90%
- **Long AUD pays -0.90% (negative carry)**

**Bonds (term premium):**

$$
\text{Carry}_{\text{bond}} = \text{Yield} - \text{Short rate} - \text{Roll-down}
$$

**Example - 10-year Treasury:**

- 10-year yield: 4.00%
- Fed Funds (funding): 5.25%
- Roll-down: +0.30% (curve steepness)
- Carry: 4.00% - 5.25% + 0.30% = -0.95%

### 2. Portfolio Construction

**Standard approach (inverse volatility weighting):**

$$
w_i = \frac{\text{sgn}(\text{Carry}_i) / \sigma_i}{\sum_{j=1}^{N} 1/\sigma_j}
$$

Where:
- sgn() = Sign function (+1 if positive carry, -1 if negative)
- $\sigma_i$ = Volatility of asset $i$
- $N$ = Number of assets

**Example - 4-asset portfolio:**

| Asset | Carry | Sign | Vol | 1/Vol | Weight |
|-------|-------|------|-----|-------|--------|
| Crude Oil | -8% | +1 (long) | 30% | 0.033 | +0.26 |
| Natural Gas | -20% | +1 (long) | 50% | 0.020 | +0.16 |
| EUR/USD | +2% | +1 (long) | 10% | 0.100 | +0.79 |
| JPY/USD | -3% | -1 (short) | 12% | 0.083 | -0.65 |

Wait, these don't sum correctly. Let me recalculate properly.

**Step 1: Calculate raw weights**

- Crude: +1 × 0.033 = +0.033
- NG: +1 × 0.020 = +0.020  
- EUR: +1 × 0.100 = +0.100
- JPY: -1 × 0.083 = -0.083

**Step 2: Normalize (so longs + shorts balance)**

Sum of positive: 0.033 + 0.020 + 0.100 = 0.153
Sum of negative: 0.083

We want longs to equal shorts in risk terms, so:

Normalized weights:
- Crude: +0.033 / 0.153 × 0.5 = +0.108
- NG: +0.020 / 0.153 × 0.5 = +0.065
- EUR: +0.100 / 0.153 × 0.5 = +0.327
- JPY: -0.083 / 0.083 × 0.5 = -0.500

Check: Longs = 50%, Shorts = 50% ✓

**Result: EUR dominates (low vol), NG smallest (high vol)**

### 3. Expected Return and Sharpe Ratio

**Expected portfolio return:**

$$
\mathbb{E}[R_p] = \sum_{i=1}^{N} w_i \times \text{Carry}_i
$$

**Using our example:**

$$
\mathbb{E}[R] = 0.108(-8\%) + 0.065(-20\%) + 0.327(+2\%) + (-0.500)(-3\%)
$$

$$
= -0.86\% - 1.30\% + 0.65\% + 1.50\% = -0.01\%
$$

Hmm, that's near zero. This shows that with proper risk parity, the expected return is driven by the carry spread between long and short positions, not just the absolute levels.

**Portfolio volatility (with correlations):**

$$
\sigma_p = \sqrt{\sum_{i=1}^{N}\sum_{j=1}^{N} w_i w_j \rho_{ij} \sigma_i \sigma_j}
$$

**With equal risk contribution:**

$$
\sigma_p \approx \sigma_{\text{target}} \times \sqrt{1 + \bar{\rho}(N-1)}
$$

Where $\bar{\rho}$ = Average correlation

**Example:**

- Target vol per position: 10%
- N = 40 assets
- Average correlation: 0.15

$$
\sigma_p = 10\% \times \sqrt{1 + 0.15 \times 39} = 10\% \times \sqrt{6.85} = 10\% \times 2.62 = 26.2\%
$$

**But we size the overall portfolio to target, say, 15% vol:**

$$
\text{Leverage} = \frac{15\%}{26.2\%} = 0.57
$$

**Expected Sharpe:**

$$
\text{Sharpe} = \frac{\mathbb{E}[R] - r_f}{\sigma_p}
$$

**Historical carry portfolios (institutional data):**

- Expected return: 8-12% (gross)
- Volatility: 12-15% (targeted)
- Sharpe: 0.6-0.8 (after costs)

### 4. Optimal Rebalancing Frequency

**Trade-off:**

- More frequent: Better tracking, higher costs
- Less frequent: Lower costs, drift from targets

**Optimal frequency:**

$$
f^* = \arg\max_{f} \left[\mathbb{E}[R(f)] - \text{Costs}(f)\right]
$$

**Empirical findings:**

| Frequency | Tracking Error | Transaction Costs | Net Sharpe |
|-----------|----------------|-------------------|------------|
| Daily | 0.5% | 2.5% drag | 0.45 |
| Weekly | 1.2% | 1.8% drag | 0.52 |
| **Monthly** | **2.5%** | **0.8% drag** | **0.68** |
| Quarterly | 4.5% | 0.4% drag | 0.58 |

**Monthly rebalancing is optimal for most portfolios**

---

## Step-by-Step Setup

### 1. Phase 1

**1. Choose Asset Classes:**

**Recommended diversification:**

- Commodities: 15-20 markets (energy, metals, agriculture)
- Currencies: 10-15 pairs (G10 + emerging markets)
- Rates: 5-10 markets (global government bonds)
- Equities: 5-10 indices (regional)

**Total universe: 35-55 futures contracts**

**Example 40-contract universe:**

**Commodities (20):**

**Energy (5):**
- Crude Oil (CL)
- Brent Crude (BRN)
- Natural Gas (NG)
- Heating Oil (HO)
- Gasoline (RB)

**Metals (5):**
- Gold (GC)
- Silver (SI)
- Copper (HG)
- Platinum (PL)
- Palladium (PA)

**Agriculture (10):**
- Corn (ZC)
- Soybeans (ZS)
- Wheat (ZW)
- Coffee (KC)
- Sugar (SB)
- Cotton (CT)
- Live Cattle (LE)
- Lean Hogs (HE)
- Cocoa (CC)
- Orange Juice (OJ)

**Currencies (12):**

- EUR/USD (6E)
- JPY/USD (6J)
- GBP/USD (6B)
- AUD/USD (6A)
- CAD/USD (6C)
- CHF/USD (6S)
- NZD/USD (6N)
- MXN/USD (6M)
- BRL/USD (6L)
- RUB/USD (6R)
- ZAR/USD (6Z)
- KRW/USD (6K)

**Rates (5):**

- US 2-Year (ZT)
- US 10-Year (ZN)
- German Bund (FGBL)
- UK Gilt (G)
- Japanese JGB (JB)

**Equities (3):**

- S&P 500 (ES)
- Nasdaq (NQ)
- Euro Stoxx 50 (FESX)

**Total: 40 contracts**

**2. Gather Historical Data:**

**Required:**

- Daily futures prices (front and second contracts)
- Volume and open interest
- Interest rates (for FX carry)
- At least 10 years of history (includes crisis periods)

**3. Calculate Carry for Each Market:**

```python
import pandas as pd
import numpy as np

def calculate_carry(front_price, second_price, days_to_roll, asset_class):
    """
    Calculate annualized carry
    """
    if asset_class == 'commodity':
        # Roll yield
        carry = (front_price - second_price) / front_price
        carry_ann = carry * (365 / days_to_roll)
    
    elif asset_class == 'currency':
        # Interest rate differential (passed as front_price = dom_rate, second = for_rate)
        carry_ann = front_price - second_price
    
    elif asset_class == 'rates':
        # Yield - funding + roll-down
        carry_ann = front_price - second_price  # Simplified
    
    return carry_ann

# Example for crude oil
cl_front = 80.00
cl_second = 81.50
cl_days = 30

cl_carry = calculate_carry(cl_front, cl_second, cl_days, 'commodity')
print(f"Crude Oil Carry: {cl_carry:.2%}")
# Output
```

### 1. Phase 2

**Step 1: Rank all assets by carry**

**Example ranking (October 2024):**

| Rank | Asset | Carry | Quintile |
|------|-------|-------|----------|
| 1 | Natural Gas | -45% | Top (long) |
| 2 | Heating Oil | -18% | Top |
| 3 | Coffee | -15% | Top |
| 4 | Copper | -12% | Top |
| 5 | Brazilian Real | +10% | Top |
| 6 | Crude Oil | -8% | Top |
| 7 | Wheat | -6% | Top |
| 8 | AUD/USD | +4% | Top |
| ... | ... | ... | Mid |
| 33 | EUR/USD | +1% | Bottom |
| 34 | Gold | +0.5% | Bottom |
| 35 | JPY/USD | -2% | Bottom (short) |
| 36 | S&P 500 | -3% | Bottom |
| 37 | 10-yr Treasury | -4% | Bottom |
| 38 | Brent Crude | +5% | Bottom |
| 39 | Silver | +8% | Bottom |
| 40 | Platinum | +12% | Bottom |

**Step 2: Select top and bottom quintiles**

- Top quintile (8 contracts): Long positions
- Bottom quintile (8 contracts): Short positions
- Middle (24 contracts): No position

**Alternatively: Long/short all with weights by carry rank**

**Step 3: Calculate volatility for each asset**

```python
# 60-day realized volatility
returns = prices.pct_change()
volatility = returns.rolling(60).std() * np.sqrt(252)

# Example results
volatilities = {
    'Natural Gas': 0.52,  # 52% annual vol
    'Crude Oil': 0.28,
    'EUR/USD': 0.09,
    'S&P 500': 0.16,
    # ... etc
}
```

**Step 4: Calculate position sizes (inverse volatility)**

```python
# Portfolio parameters
total_capital = 1_000_000  # $1M
target_vol = 0.15  # 15% portfolio vol
num_positions = 16  # 8 long + 8 short

# Calculate weights
def calculate_weights(assets, carries, vols):
    weights = {}
    inv_vol_sum = sum(1/vol for vol in vols)
    
    for asset, carry, vol in zip(assets, carries, vols):
        sign = np.sign(carry)  # +1 for positive carry (long), -1 for negative (short)
        
        # In carry strategies, negative carry = long (backwardation)
        # Positive carry = short (contango)
        # So we flip the sign
        
        if carry < 0:  # Backwardation
            sign = +1  # Long
        else:  # Contango
            sign = -1  # Short
        
        weight = sign * (1/vol) / inv_vol_sum
        weights[asset] = weight
    
    return weights

# Example
top_assets = ['Natural Gas', 'Heating Oil', 'Coffee', ...]
top_carries = [-0.45, -0.18, -0.15, ...]
top_vols = [0.52, 0.35, 0.30, ...]

weights = calculate_weights(top_assets, top_carries, top_vols)

# Normalize to sum to 100% long, 100% short
```

**Step 5: Convert to contracts**

```python
def calculate_contracts(weight, capital, price, multiplier, target_vol, current_vol):
    """
    Calculate number of contracts
    """
    notional = weight * capital
    contracts = notional / (price * multiplier)
    
    # Adjust for volatility targeting
    vol_scalar = target_vol / current_vol
    contracts *= vol_scalar
    
    return int(round(contracts))

# Example
ng_weight = 0.125  # 12.5% of portfolio
ng_price = 6.00
ng_multiplier = 10_000  # MMBtu
ng_vol = 0.52

ng_contracts = calculate_contracts(
    weight=ng_weight,
    capital=1_000_000,
    price=ng_price,
    multiplier=ng_multiplier,
    target_vol=0.15,
    current_vol=0.52
)

print(f"Natural Gas: {ng_contracts} contracts")
# Output
```

### 1. Phase 3

**Month 1 (October 1, 2024 - Initial Construction):**

**Portfolio constructed:**

```
Long Positions (Top Quintile):
- 6 Natural Gas @ $6.00
- 4 Heating Oil @ $2.80
- 3 Coffee @ $2.10
- 5 Copper @ $4.20
- 2 BRL/USD @ 5.00
- 3 Crude Oil @ $80.00
- 4 Wheat @ $6.50
- 2 AUD/USD @ 0.6500

Short Positions (Bottom Quintile):
- 3 JPY/USD @ 0.0067
- 2 S&P 500 @ 5,600
- 1 10-yr Note @ 110-00
- 5 EUR/USD @ 1.0800
- 2 Gold @ $2,650
- 1 Brent @ $83.00
- 2 Silver @ $32.00
- 1 Platinum @ $1,000
```

**Total margin: ~$150,000 (15% of capital)**

**Month 1 Performance:**

| Asset | Position | Entry | End Month | P&L | Carry Collected |
|-------|----------|-------|-----------|-----|-----------------|
| Natural Gas | +6 | $6.00 | $6.20 | +$12,000 | +$2,700 |
| Crude Oil | +3 | $80 | $82 | +$6,000 | +$600 |
| JPY (short) | -3 | 0.0067 | 0.0065 | +$3,000 | +$150 |
| ... | ... | ... | ... | ... | ... |

**Total Month 1:**

- Price changes: +$18,000
- Carry collected: +$5,500
- **Total: +$23,500 (+2.35% on $1M)**

**Month 2 (November 1 - Rebalancing):**

**Step 1: Recalculate carry for all 40 markets**

Changes from last month:
- Natural Gas carry: -45% → -35% (still high, but declining)
- Crude Oil carry: -8% → -2% (flattening)
- New entrant: Corn -12% (harvest backwardation)

**Step 2: Rerank and reselect**

- Crude Oil drops out of top quintile (carry too low)
- Corn enters top quintile

**Step 3: Adjust positions**

```
Close: 3 Crude Oil @ $82
Open: 5 Corn @ $4.80

Reduce: Natural Gas from 6 to 4 contracts (carry declining)
```

**Transaction costs:**

- Crude: 3 contracts × $25 commission = $75
- Corn: 5 contracts × $25 = $125
- Natural Gas: 2 contracts × $25 = $50
- **Total costs: $250 (0.025% of capital)**

### 2. Phase 4

**Quarter 1 Review (December 31):**

**Performance summary:**

| Month | Return | Sharpe | Max DD |
|-------|--------|--------|--------|
| Oct | +2.35% | 0.95 | -0.5% |
| Nov | +1.80% | 0.78 | -1.2% |
| Dec | -0.90% | -0.32 | -2.8% |
| **Q1** | **+3.25%** | **0.52** | **-2.8%** |

**Analysis:**

- December underperformance: Energy carry compressed
- Diversification worked (FX carried portfolio)
- Transaction costs: 0.08% quarterly (acceptable)

**Adjustments:**

**1. Rebalance to annual targets:**

- Some assets drifted (Natural Gas now 18% of portfolio)
- Rebalance back to equal risk

**2. Review universe:**

- Add: Canadian Dollar (CAD carry improved)
- Remove: Platinum (low liquidity, wide spreads)

**3. Vol targeting adjustment:**

- Q1 realized vol: 18% (above 15% target)
- Reduce gross exposure by 15/18 = 83%

### 3. Phase 5

**Scenario: March 2025 Energy Crisis**

**Event:** Geopolitical shock → Oil spike

**Portfolio impact:**

| Asset | Position | Move | P&L |
|-------|----------|------|-----|
| Natural Gas | +4 | +80% | +$192,000 (huge) |
| Crude Oil | +0 | +35% | $0 (no position) |
| Heating Oil | +4 | +60% | +$100,800 |
| EUR/USD (short) | -5 | +2% | -$6,250 |
| JPY/USD (short) | -3 | +5% | -$11,250 |
| S&P 500 (short) | -2 | -8% | +$44,800 |

**Net: +$320,000 (+32% in 1 month!)**

**But realized volatility spikes:**

- Portfolio vol: 15% → 38% (crisis)
- **Action required: De-lever**

**Crisis management:**

```python
# Volatility targeting kicks in
target_vol = 0.15
current_vol = 0.38
scalar = target_vol / current_vol  # 0.39

# Reduce all positions to 39% of current
for asset in portfolio:
    new_size = current_size * 0.39
    close_contracts(current_size - new_size)

# Lock in profits on energy
close_position('Natural Gas', reason='extraordinary profit, regime shift')
```

**Exit Natural Gas:**

- Entry: 4 contracts @ $6.00
- Exit: 4 contracts @ $10.80
- **Profit: +$192,000 in 5 months**

**Lesson: Vol targeting protects profits and prevents over-exposure**

---

## Risk Management for Carry Portfolios

### 1. Position Sizing and Diversification

**The 1/N rule with vol adjustment:**

$$
w_i = \frac{\text{sgn}(\text{Carry}_i)}{N \times \sigma_i} \times \sigma_{\text{target}}
$$

**Key principles:**

1. **Minimum 20 uncorrelated positions** (preferably 40+)
2. **Single asset max:** 10% of portfolio risk
3. **Single sector max:** 30% of portfolio risk
4. **No concentration** in single asset class

**Example risk budget:**

| Asset Class | % of Risk | Rationale |
|-------------|-----------|-----------|
| Commodities | 40% | 20 markets, diverse |
| Currencies | 35% | 12 pairs, global |
| Rates | 15% | 5 countries |
| Equities | 10% | 3 indices, low weight |

### 2. Volatility Targeting

**Daily adjustment:**

$$
\text{Leverage}_t = \frac{\sigma_{\text{target}}}{\sigma_{t,\text{realized}}}
$$

**Example:**

- Target: 15% annual vol
- Current realized (60-day): 12%
- Leverage: 15% / 12% = 1.25x
- **Scale up all positions by 25%**

**Crisis mode (vol spike to 30%):**

- Leverage: 15% / 30% = 0.50x
- **Cut all positions in half**

**Benefits:**

- Prevents over-exposure in crises
- Maintains consistent risk profile
- Improves Sharpe ratio

### 3. Stop Losses and Drawdown Control

**Portfolio-level stops:**

**Maximum drawdown limit: -15%**

$$
\text{If DD}_{\text{current}} > -15\% \rightarrow \text{Reduce exposure to 50\%}
$$

**Example:**

- Portfolio peak: $1,000,000
- Current: $840,000 (-16% DD)
- **Action: Cut all positions by 50%, reassess**

**Asset-level stops:**

**Carry regime change:**

$$
\text{If } \text{Carry}_{\text{current}} < 0.3 \times \text{Carry}_{\text{entry}} \rightarrow \text{Exit}
$$

**Example:**

- Entry carry (Natural Gas): -30%
- Current carry: -8% (< 30% × 30% = 9%)
- **Exit: Carry regime has changed**

### 4. Correlation Monitoring

**Risk:** Correlations spike in crises (diversification fails)

**Monitoring:**

```python
# Calculate rolling pairwise correlations
window = 60  # days
corr_matrix = returns.rolling(window).corr()

# Average correlation
avg_corr = corr_matrix.mean().mean()

# Alert if avg > 0.3 (normal is 0.1-0.2)
if avg_corr > 0.3:
    print("WARNING: Correlations elevated, reduce leverage")
```

**Historical correlation regime:**

| Period | Avg Correlation | Action |
|--------|-----------------|--------|
| Normal | 0.15 | Full exposure |
| Stress | 0.35 | Reduce to 70% |
| Crisis | 0.60 | Reduce to 40% |

### 1. Crash Risk Hedging

**The carry "smile" problem:**

- Collect small carry (1-2% monthly)
- Exposed to large crash (-30-50%)
- **Need tail risk hedge**

**Options:**

**1. OTM put spreads (cheap tail hedge):**

- Buy 20% OTM puts on ES, NQ
- Sell 40% OTM puts (reduce cost)
- Cost: ~0.3% monthly
- **Protects against equity crash**

**2. VIX calls:**

- Buy VIX call spreads
- Cost: ~0.2% monthly
- **Profits when vol spikes**

**3. Trend filter:**

- Exit carry positions showing negative price trend
- Example: Commodity 50-day MA < 200-day MA
- **Reduces crash exposure mechanically**

**Expected impact:**

- Hedge cost: 0.5% annual drag
- Crash protection: Reduces -50% crash to -25%
- **Worth it for institutional capital**

---

## Real-World Examples

### 1. Example 1: 2008 Financial Crisis

**Background:**

- Carry strategies extremely popular (2005-2007)
- "Picking up pennies in front of a steamroller"
- Sharpe ratios 1.5+ for years

**Typical carry portfolio (July 2008):**

```
Long (High Carry):
- AUD/USD: +5% carry (Aus rates 7.25%)
- NZD/USD: +6% carry (NZ rates 8.25%)
- BRL/USD: +8% carry (Brazil rates 13%)
- Crude Oil: -12% carry (backwardation)
- Copper: -8% carry (backwardation)

Short (Low Carry):
- JPY/USD: -5% carry (Japan rates 0.5%)
- CHF/USD: -3% carry (Swiss rates 2.75%)
- Gold: +1% carry (contango)
```

**Performance (Jan 2007 - Aug 2008):**

- Cumulative: +28%
- Sharpe: 1.6
- Max DD: -4%
- **Everything perfect**

**September-October 2008 (Lehman collapse):**

| Date | Event | Portfolio Return | Cumulative |
|------|-------|-----------------|------------|
| Sep 15 | Lehman bankruptcy | -8% | +18% |
| Sep 22 | AIG bailout | -12% | +3% |
| Oct 6 | Global selloff | -18% | -16% |
| Oct 10 | Worst week ever | -22% | -40% |

**What happened:**

**1. FX carry unwind:**

- AUD/USD: 0.98 → 0.62 (-37%!)
- NZD/USD: 0.82 → 0.52 (-37%!)
- JPY/USD: 0.0095 → 0.0105 (+11% against us)
- **Massive losses on currency positions**

**2. Commodity crash:**

- Crude: $145 → $35 (-76%)
- Copper: $4.00 → $1.25 (-69%)
- **Even backwardated commodities crashed**

**3. Correlation spike:**

- Normal: 0.15 average correlation
- Crisis: 0.75 correlation
- **Diversification disappeared**

**4. Forced liquidation:**

- Margin calls
- Investors redeeming
- **Had to sell winners with losers**

**Final damage:**

- Peak (August 2008): +28%
- Trough (October 2008): -40%
- **Total drawdown: -53% in 2 months**
- **Took 4 years to recover**

**Key lessons:**

- Carry is NOT free money
- Crashes are sudden and severe
- Correlations spike when needed most
- **Volatility targeting could have helped (reduce leverage as vol spiked)**

### 2. Example 2: COVID Crash March 2020

**Background:**

- Portfolio managers had learned from 2008
- Implemented vol targeting, tail hedges
- More disciplined risk management

**Portfolio (February 2020):**

```
Diversified across 45 markets:
- 18 Commodities
- 15 Currencies
- 8 Rates
- 4 Equities

Leverage: 1.2x (moderate)
Target vol: 15%
Realized vol: 13% (calm market)
```

**Crisis timeline:**

**February 20-28 (Week 1):**

- COVID spreading globally
- Realized vol: 13% → 22%
- Vol targeting: Reduce leverage 15%/22% = 68%
- **Action: Cut 32% of positions automatically**

**March 2-13 (Week 2):**

- Realized vol: 22% → 35%
- Vol targeting: Further reduce to 15%/35% = 43%
- **Cut another 25% of positions**

**March 16-20 (Week 3 - Worst):**

- Realized vol: 35% → 68% (extreme!)
- Vol targeting: 15%/68% = 22% exposure
- **Portfolio at 1/5 normal size**

**Performance:**

| Period | Portfolio Return | S&P 500 | Benefit of Vol Targeting |
|--------|-----------------|---------|--------------------------|
| Feb 20-28 | -2.8% | -11.5% | +8.7% |
| Mar 2-13 | -3.5% | -17.2% | +13.7% |
| Mar 16-20 | -4.2% | -14.7% | +10.5% |
| **Total** | **-10.5%** | **-34.0%** | **+23.5%** |

**Why it worked better than 2008:**

**1. Volatility targeting:**

- Automatically de-levered as vol spiked
- Prevented catastrophic losses
- **Preserved capital**

**2. Tail hedges:**

- VIX calls: +$120,000 gain (offset losses)
- OTM put spreads: +$85,000 gain
- **Hedges worked**

**3. Diversification maintained:**

- Some carries worked (Gold backwardation)
- Rates rallied (duration positive)
- **Not 100% correlated like 2008**

**Recovery:**

- Peak (Feb 19): $10M
- Trough (Mar 23): $8.95M (-10.5%)
- **Recovered by June 2020 (3 months)**

**vs. 2008:**

- 2008: -53% DD, 4-year recovery
- 2020: -10.5% DD, 3-month recovery
- **Risk management worked**

### 3. Example 3

**Setup:**

- Low storage levels entering winter
- Cold weather forecasts
- LNG export demand high

**Carry structure (November 2023):**

| Contract | Price | Carry |
|----------|-------|-------|
| December | $6.50 | - |
| January | $5.80 | -129% ann. |
| February | $5.20 | -200% ann. |
| March | $3.80 | -416% ann. (!) |

**Extreme backwardation: Winter high, shoulder low**

**Trade:**

```
Long December Natural Gas: 10 contracts @ $6.50
Target: Collect roll yield as backwardation persists
Risk: Weather turns warm, storage builds
```

**Timeline:**

**December 2023:**

- Weather: Colder than normal (polar vortex)
- Storage: Drawdowns 15% above 5-year average
- Price: $6.50 → $7.20 (+10.8%)
- **Carry collected: 10 contracts × 10.8% × $10,000 = +$10,800**

**Roll to January (December 20):**

- Sell December @ $7.20
- Buy January @ $5.90 (vs $5.80 originally)
- **Roll gain: ($7.20 - $5.90) × 10 × 10,000 = +$130,000**

**January 2024:**

- Price stable: $6.00-$6.40 range
- Carry still steep: Jan $6.20, Feb $5.50
- **Collected: 11.3% carry = +$11,300**

**Roll to February (January 20):**

- Sell January @ $6.30
- Buy February @ $5.55
- **Roll gain: ($6.30 - $5.55) × 10 × 10,000 = +$75,000**

**Exit (February 1):**

- Exited all @ $5.80
- Weather moderating, carry flattening

**Total results (3 months):**

- Initial margin: $60,000 (10 contracts)
- December carry: +$10,800
- December roll: +$130,000
- January carry: +$11,300
- January roll: +$75,000
- February exit: +$2,500
- **Total: +$229,600 (+383% return on margin!)**

**Why it worked:**

- Fundamental supply/demand (low storage)
- Weather catalyst (polar vortex)
- Persistent backwardation (didn't normalize quickly)
- **Disciplined exit when carry compressed**

**Key lesson: Commodity carry can be EXPLOSIVE when fundamentals align**

### 4. Example 4: AUD/JPY Carry Trade

**Background:**

- Australia: Mining boom, high rates (7%)
- Japan: Deflation, zero rates (0.5%)
- **Carry: 6.5% per year (massive)**

**Trade:**

```
Long AUD/JPY @ 85.00 (January 2005)
Size: 10 contracts (A$1,000,000 notional)
Target: Collect 6.5% annual carry
```

**Timeline:**

| Year | AUD/JPY | Carry Collected | Price Gain | Total Return |
|------|---------|-----------------|------------|--------------|
| 2005 | 85.00 → 90.50 | +6.5% | +6.5% | +13.0% |
| 2006 | 90.50 → 95.20 | +6.5% | +5.2% | +11.7% |
| 2007 | 95.20 → 107.80 | +6.5% | +13.2% | +19.7% |

**3-year cumulative:**

- Carry: +19.5%
- Price appreciation: +26.8%
- **Total: +46.3% (compound +14.5% CAGR)**

**On 10 contracts:**

- Notional: A$1,000,000
- P&L: +$463,000
- **Risk: $100,000 margin (4.6x return)**

**But then... 2008:**

- AUD/JPY: 107.80 → 55.20 (-48.8%!)
- **Entire 3 years of gains wiped out + more**

**Final result (2005-2008):**

- Peak: +46.3% (2007)
- Trough: -28.5% (2008)
- **Total 4-year: +5.2% (pathetic given risk)**

**Key lesson:**

- Carry trades can compound beautifully
- But crash risk is ALWAYS lurking
- **Need stop loss or diversification**
- Single-pair carry is NOT a portfolio

### 5. Example 5: Institutional Carry Portfolio

**Setup:**

- Institutional implementation
- 50+ futures markets
- Monthly rebalancing
- Volatility targeting 15%
- Modest leverage (1.5x)

**14-year performance:**

| Period | Return | Volatility | Sharpe | Max DD | Notes |
|--------|--------|-----------|--------|--------|-------|
| 2010-2012 | +8.5% | 14.2% | 0.60 | -8.2% | Post-crisis |
| 2013-2015 | +6.2% | 12.8% | 0.48 | -12.5% | Taper tantrum |
| 2016-2018 | +9.8% | 15.5% | 0.63 | -9.8% | Strong |
| 2019-2021 | +4.2% | 16.2% | 0.26 | -18.5% | COVID hit |
| 2022-2024 | +11.5% | 14.8% | 0.78 | -7.2% | Excellent |
| **Total** | **+8.2%** | **14.8%** | **0.55** | **-18.5%** | 14 years |

**Compounded:**

- $10M start (2010)
- $30.2M end (2024)
- **+202% total (+8.1% CAGR)**

**Comparison to benchmarks:**

| Strategy | CAGR | Volatility | Sharpe | Max DD |
|----------|------|-----------|--------|--------|
| Carry Portfolio | 8.1% | 14.8% | 0.55 | -18.5% |
| S&P 500 | 12.5% | 17.2% | 0.65 | -33.9% |
| 60/40 | 8.8% | 10.5% | 0.72 | -25.8% |
| Bonds | 3.2% | 5.8% | 0.28 | -17.2% |

**Observations:**

- Lower return than stocks (but better risk-adjusted historically)
- Higher Sharpe than pure equity long-only
- **Uncorrelated to traditional portfolios (key benefit)**

**Why institutional:**

- Smooth returns (Sharpe 0.55)
- Diversification benefit (low correlation to 60/40)
- Harvests alternative risk premium
- **Fits in multi-strategy portfolio**

---

## Best Case Scenario

### 1. The Perfect Carry Environment

**Setup for maximum profitability:**

**Ideal conditions:**

1. **Multiple carry regimes aligned** (commodities backwardated, FX spreads wide, curves steep)
2. **Low volatility** (carry collected without price noise)
3. **Trending carry** (backwardation/contango persisting for months)
4. **Uncorrelated assets** (diversification working perfectly)
5. **Rising carry** (carry improving over time, not compressing)
6. **No crises** (smooth collection without crashes)

### 2. Best Case Example

**Background:**

- Post-2015 commodity crash recovery
- Central banks diverging (Fed hiking, ECB/BOJ easing)
- Moderate growth (not too hot, not too cold)
- Volatility historically low (VIX 10-15)

**Portfolio (January 2016):**

```
Universe: 52 futures contracts
Capital: $25M
Target vol: 15%
Rebalancing: Monthly
```

**Carry structure (January 2016):**

**Commodities (spectacular):**

- Crude Oil: -18% carry (severe backwardation, recovering from crash)
- Natural Gas: -25% carry (winter, low storage)
- Copper: -15% carry (China demand)
- Wheat: -12% carry (drought concerns)
- Coffee: -10% carry (Brazil frost)

**Currencies (wide spreads):**

- USD/BRL: +12% carry (Brazil hiking)
- USD/TRY: +8% carry (Turkey high rates)
- USD/MXN: +5% carry (Mexico rates)
- AUD/JPY: +6% carry (classic)

**Rates (steep curves):**

- US 2s10s: +120 bps steepness
- Germany 2s10s: +80 bps
- **Carry on duration: +1.5-2%**

**Performance (2016-2018):**

**Year 1 (2016):**

| Quarter | Return | Best Performer | Worst Performer |
|---------|--------|----------------|-----------------|
| Q1 | +4.2% | Crude (+8%) | JPY (-2%) |
| Q2 | +3.8% | Copper (+6%) | Gold (-1%) |
| Q3 | +2.5% | BRL (+5%) | EUR (-1%) |
| Q4 | +5.1% | Nat Gas (+12%) | Bonds (0%) |
| **2016** | **+16.5%** | - | - |

**Realized vol: 14.2% (slightly below 15% target)**
**Sharpe: (16.5% - 1.5%) / 14.2% = 1.06 (excellent!)**

**Year 2 (2017):**

**Even better: VIX at historic lows (9-11)**

| Quarter | Return | Commentary |
|---------|--------|------------|
| Q1 | +4.5% | Carry collecting smoothly |
| Q2 | +3.2% | Some carry compression |
| Q3 | +4.8% | Commodities strong |
| Q4 | +3.9% | Year-end rally |
| **2017** | **+17.2%** | Best year |

**Realized vol: 11.8% (well below target due to low market vol)**
**Sharpe: (17.2% - 2.0%) / 11.8% = 1.29 (phenomenal!)**

**Year 3 (2018):**

**First half great, second half stress:**

| Quarter | Return | Commentary |
|---------|--------|------------|
| Q1 | +2.8% | Solid start |
| Q2 | +3.5% | Continued |
| Q3 | +1.2% | Vol pickup |
| Q4 | -3.8% | Dec selloff (tightening scare) |
| **2018** | **+3.5%** | Bumpier |

**Realized vol: 16.5% (above target)**
**Sharpe: (3.5% - 2.5%) / 16.5% = 0.06 (weak, but still positive)**

**3-Year totals:**

- Starting capital: $25M
- Ending capital: $25M × 1.165 × 1.172 × 1.035 = $35.1M
- **Total gain: +40.5% (+12.0% CAGR)**
- **Dollar gain: +$10.1M**

**Why this was exceptional:**

**1. Multiple carry regimes aligned:**

- Commodities: Post-crash backwardation (producers hedging recovery)
- Currencies: Central bank divergence (wide spreads)
- Rates: Steep curves (term premium high)
- **All factors positive simultaneously**

**2. Low volatility (2016-2017):**

- VIX averaged 12 (historically low)
- Carry collected without price noise
- **Maximum Sharpe ratio environment**

**3. Persistence:**

- Backwardation lasted months (didn't flip to contango quickly)
- Rate differentials stable (CB paths predictable)
- **Trends were durable**

**4. Diversification worked:**

- When commodities weak, FX strong
- When FX weak, rates strong
- **True portfolio effect**

**5. No major crises:**

- 2016: Calm (post-Fed hike fears)
- 2017: Goldilocks (perfect growth/inflation)
- 2018 Q4: Selloff but no crash
- **Risk management not tested severely**

**6. Disciplined rebalancing:**

- Monthly rebalancing captured carry evolution
- Exited compressed carries (took profits)
- Entered new opportunities (commodities evolving)
- **Active but systematic**

**Account impact:**

- Starting: $25M
- Peak (end 2017): $33.6M (+34.5%)
- Ending (end 2018): $35.1M (+40.5%)
- **Smooth compounding with one difficult quarter**

**This represents carry portfolio investing at its absolute zenith:**

- Favorable macro environment
- Multiple asset classes contributing
- Low volatility maximizing Sharpe
- Disciplined risk management
- Systematic rebalancing
- No major crisis to test resilience

---

## Worst Case Scenario

### 1. The Carry Portfolio Nightmare

**Worst possible conditions:**

1. **Global risk-off** (all carry trades unwind simultaneously)
2. **Correlation spike** (diversification fails)
3. **Volatility explosion** (if no vol targeting, massive losses)
4. **Forced liquidation** (margin calls, redemptions)
5. **Carry reversals** (backwardation flips to contango)
6. **No hedges** (pure carry exposure, no tail protection)

### 2. Worst Case Example

**Background:**

- Portfolio manager overconfident from 2005-2007 success
- No volatility targeting implemented
- No tail hedges
- Fixed leverage (2x)
- "This time is different" mentality

**Portfolio (August 1, 2008):**

```
Capital: $50M
Leverage: 2.0x (aggressive)
Gross notional: $100M

Positions (50 markets):
Long Carry (30 positions):
- 10 Commodity backwardations (Crude, NG, Copper, etc.)
- 12 High-yield currencies (AUD, NZD, BRL, TRY, ZAR, etc.)
- 5 Steep curve trades (Long 10yr, short 2yr)
- 3 High dividend equity indices (FTSE, ASX, IBEX)

Short Carry (20 positions):
- 8 Commodity contangos (Gold, Silver, Grains)
- 8 Low-yield currencies (JPY, CHF, USD)
- 4 Flat curve trades
```

**August 2008: Still good**

- Return: +2.8%
- YTD: +22.5% (feeling invincible)
- Realized vol: 18% (slightly elevated, ignored)

**September 1-15, 2008: Warning signs**

**September 7:** Fannie/Freddie conservatorship

- Portfolio: -3.5% (commodities weak, risk-off beginning)
- Action taken: NONE (waiting for rebound)

**September 15: Lehman bankruptcy**

**Morning (pre-announcement):**

- Portfolio value: $59.8M (still up YTD)

**Day 1 (Sep 15):**

| Asset Class | Position | Move | P&L | Commentary |
|-------------|----------|------|-----|-------------|
| AUD/JPY | Long $15M | -8% | -$1.2M | Carry unwind |
| BRL/USD | Long $8M | -12% | -$960k | EM crash |
| Crude Oil | Long $12M | -6% | -$720k | Deleveraging |
| Copper | Long $8M | -9% | -$720k | China fears |
| ES (short) | Short $5M | +5% | +$250k | Partial offset |
| JPY (short) | Short $10M | -7% | -$700k | Safe haven surge |

**Day 1 total: -$4.05M (-6.8%)**

**End of day value: $55.75M**

**Day 2-5 (Sep 16-19): The cascade**

**September 16:**

- Market in freefall
- Margin calls: $8M required
- Portfolio: -$5.2M (-8.7% daily)
- **First forced liquidation: Sold 30% of positions at terrible prices**

**September 17:**

- AIG bailout (temporary relief)
- Portfolio: -$2.1M (-4.2% daily)
- **Cumulative from Sep 15: -18.5%**

**September 18-19:**

- Money market freeze, lehman contagion
- Portfolio: -$6.8M (-14.2% daily)
- **Cumulative: -30.2%**

**End Week 1 (Sep 19):**

- Starting (Sep 15 AM): $59.8M
- Current: $41.7M
- **Loss: -$18.1M (-30.2% in 5 days)**

**Week 2 (Sep 22-26): Continued carnage**

**Correlation explosion:**

- Pre-crisis average correlation: 0.12
- Crisis correlation: 0.78
- **Everything moving together DOWN**

**Volatility spike:**

- Pre-crisis vol: 18%
- Current vol: 65%
- **Should have de-levered, but no vol targeting**

**Forced liquidations continue:**

- Investors redeeming: $15M requested
- Must sell into worst market
- Slippage: 5-10% on exits

**End Week 2 (Sep 26):**

- Value: $32.5M
- **Loss from peak: -$27.3M (-45.7%)**

**October 2008: The bottom falls out**

| Week | Starting | Ending | Weekly Loss | Event |
|------|----------|--------|-------------|-------|
| Oct 6 | $32.5M | $27.8M | -14.5% | Global selloff |
| Oct 13 | $27.8M | $22.1M | -20.5% | Worst week |
| Oct 20 | $22.1M | $19.5M | -11.8% | Capitulation |
| Oct 27 | $19.5M | $17.2M | -11.8% | Final flush |

**Trough (October 31, 2008):**

- Starting capital (August 1): $50M
- Current value: $17.2M
- **Total loss: -$32.8M (-65.6%!)**

**What went catastrophically wrong:**

**1. No volatility targeting:**

- Vol spiked from 18% to 65%
- Should have cut leverage from 2x to 0.55x
- Instead, stayed at 2x (3.6x effective over-leverage)
- **Losses magnified 3.6x**

**2. No tail hedges:**

- Could have bought VIX calls (0.3% cost)
- Could have OTM puts (0.5% cost)
- Total hedge cost: 0.8% annual = $400k
- **Hedge would have paid $8-12M (saved 25% of loss)**

**3. Correlation assumptions broken:**

- Assumed 0.12 correlation (diversification)
- Actual 0.78 (everything down together)
- **Diversification disappeared when needed most**

**4. Forced liquidation spiral:**

- Margin calls → Sell at worst prices
- Redemptions → More forced selling
- Slippage: 5-10% on exits
- **Couldn't exit rationally**

**5. Carry regime reversals:**

- Backwardation → Contango (commodities)
- High rates → Rate cuts (FX carry negative)
- Steep curves → Flattening (rates)
- **Every carry source reversed**

**6. Psychological paralysis:**

**Week 1:** "Temporary panic, will recover"
**Week 2:** "Maybe sell 30%, wait for bounce"
**Week 3:** "Oh god, sell more, but prices terrible"
**Week 4:** "Just stop the bleeding, sell everything"

**Recovery timeline (if survived):**

- Trough: $17.2M (Oct 2008)
- 2009: +15% → $19.8M
- 2010: +12% → $22.2M
- 2011: +8% → $24.0M
- 2012: +10% → $26.4M
- 2013: +9% → $28.8M

**Full recovery to $50M: 2017 (9 years!)**

**But most investors:**

- Redeemed at trough (locked in -65% loss)
- Portfolio liquidated
- Manager lost job/reputation
- **Never participated in recovery**

**Key lessons:**

1. **Volatility targeting is NON-NEGOTIABLE** (would have cut losses from -65% to -25%)
2. **Tail hedges are insurance, not optional** (0.8% cost vs. 65% loss)
3. **Correlations spike in crises** (Plan for 0.7-0.8, not 0.1)
4. **Leverage kills** (2x in crisis = suicide)
5. **Forced liquidation = worst outcome** (Need liquidity cushion)
6. **Carry is crash risk premium** (Accept it or don't trade carry)

**If had volatility targeting:**

- Sep 15 vol spike: Cut leverage 15%/65% = 23%
- Loss: -65% × 23% / 200% = -7.5%
- **Final: -$3.75M vs. -$32.8M (saved $29M!)**

---

## What to Remember

### 1. Core Concept

**Carry factor portfolios systematically harvest risk premia across multiple futures markets by going long high-carry assets and short low-carry assets:**

$$
\text{Return} = \sum_{i=1}^{N} w_i \times \text{Carry}_i + \text{Price Changes}
$$

- Diversify across 30-50+ futures (commodities, currencies, rates, equities)
- Rank by carry, long top quintile, short bottom quintile
- Size inversely to volatility (equal risk contribution)
- Rebalance monthly
- Target 10-15% volatility
- Expected Sharpe: 0.5-0.8 long-term

### 2. The Setup

**Standard institutional carry portfolio:**

- Universe: 50 futures contracts
- Capital: $10M+
- Target vol: 15%
- Position sizing: Inverse volatility ($w_i \propto 1/\sigma_i$)
- Rebalancing: Monthly (first trading day)
- Leverage: 1.0-1.5x typical
- Hedges: VIX calls or OTM puts (0.5-1% cost)

### 3. The Mathematics

**Carry calculation:**

$$
\text{Carry}_{\text{commodity}} = \frac{F_1 - F_2}{F_1} \times 12/\Delta T
$$

$$
\text{Carry}_{\text{FX}} = r_{\text{domestic}} - r_{\text{foreign}}
$$

**Position weight:**

$$
w_i = \frac{\text{sgn}(\text{Carry}_i)}{N \times \sigma_i} \times \sigma_{\text{target}}
$$

**Expected return (historical):**

$$
\mathbb{E}[R] = 8-12\% \text{ annually (gross)}
$$

### 4. Risk Management

**Essential rules:**

- Minimum 30 uncorrelated positions (preferably 50+)
- Volatility targeting: Daily adjustment to maintain 15% vol
- Single asset max: 10% of portfolio risk
- Drawdown limit: -15% → Reduce to 50% exposure
- Tail hedges: 0.5-1% annual cost (VIX calls, OTM puts)
- Monthly rebalancing: First trading day of month
- Correlation monitoring: Alert if avg > 0.30

### 5. Maximum Profit/Loss

**Best case:**

- Multiple carry regimes aligned (commodities + FX + rates)
- Low volatility environment (VIX 10-15)
- Persistent carry (backwardation lasting months)
- No crises (smooth collection)
- **Returns: 15-20% annual with Sharpe 1.0-1.3**

**Worst case:**

- Global crisis (2008-style)
- No volatility targeting
- Correlation spike to 0.7-0.8
- Forced liquidation
- **Max loss: -50% to -70% (if no risk management)**

**Expected (with proper risk management):**

- Long-term CAGR: 8-12%
- Volatility: 12-15%
- Sharpe: 0.6-0.8
- Max drawdown: -15% to -25%
- **Crisis drawdown (with vol targeting): -20% to -30%**

### 6. When to Use

**Carry portfolios appropriate when:**

- Long-term horizon (5+ years minimum)
- Accept negative skewness (rare crashes for steady gains)
- Want uncorrelated returns (vs. equity/bond 60/40)
- Have infrastructure (access to 50+ futures, rebalancing, risk systems)
- Institutional capital ($10M+ ideally)

**Don't use when:**

- Short-term horizon (< 2 years)
- Can't tolerate -20%+ drawdowns
- No volatility targeting capability
- Single-asset focus (need diversification)
- Retail account (< $1M, transaction costs prohibitive)

### 7. Common Mistakes

1. Insufficient diversification (< 20 markets)
2. No volatility targeting (constant leverage = disaster)
3. No tail hedges (unprotected crash risk)
4. Over-leveraging (> 2x gross)
5. Ignoring correlation spikes (assuming stable 0.15)
6. Single asset class focus (commodities only, FX only)
7. No drawdown controls (-50% before acting)
8. Quarterly rebalancing (too infrequent, monthly better)

### 8. Comparison to Other Strategies

**Advantages over directional trading:**

- Market-neutral (long AND short)
- Diversified risk premia (not relying on one market)
- Higher Sharpe ratios (0.6-0.8 vs. 0.3-0.5)
- Uncorrelated to stocks/bonds (portfolio benefit)
- Systematic (no discretion needed)

**Disadvantages:**

- Negative skewness (crash risk)
- Capital intensive ($10M+ ideal)
- Complex infrastructure (50+ futures, risk systems)
- Modest returns (8-12% vs. 15% stocks long-term)
- Crash risk (rare but severe -30-50% losses)

### 9. Final Wisdom

> "Carry factor portfolios are the institutional investor's systematic approach to harvesting risk premia that have persisted for centuries: backwardation compensates speculators for providing insurance to hedgers, interest rate differentials compensate for currency crash risk, and term premia compensate for duration risk. The math is elegant—rank 50 markets by carry, long the top, short the bottom, weight by inverse volatility, rebalance monthly. The edge is real—Sharpe ratios of 0.6-0.8 over decades. But the risk is profound—carry strategies are 'picking up pennies in front of a steamroller.' They earn steady 1-2% monthly, then crash -30-50% in rare crises (1998, 2008, 2020). Survival requires three non-negotiables: (1) Diversification across 30-50 uncorrelated markets—no single-asset concentration, (2) Volatility targeting—cut leverage when vol spikes from 15% to 60%, and (3) Tail hedges—0.5-1% annual cost for VIX calls or OTM puts protects against catastrophic losses. With these safeguards, carry portfolios offer institutional-quality risk-adjusted returns uncorrelated to traditional 60/40 portfolios. Without them, you're naked short volatility waiting for the steamroller."

**Key to success:**

- Build universe of 30-50+ futures (diversify asset classes)
- Calculate carry systematically (roll yield, rate differentials, term premia)
- Rank monthly, select top and bottom quintiles (or all with continuous weights)
- Size inversely to volatility (equal risk contribution)
- Implement volatility targeting (daily/weekly adjustment)
- Add tail hedges (0.5-1% cost, 25% crash protection)
- Rebalance monthly (first trading day discipline)
- Monitor correlations (reduce leverage if spiking)
- Accept crash risk (part of risk premium, can't eliminate)
- Think in decades not years (long-term institutional capital)

**Most important:** Carry is a risk premium—you're being paid to provide insurance and take on crash risk. Diversification across 50 markets helps but doesn't eliminate crash risk. Volatility targeting is the difference between -25% and -70% in crises. Tail hedges cost 0.5-1% annually but save you in 1998, 2008, 2020. This is sophisticated institutional investing—if you can't implement all the safeguards, don't run carry portfolios. But if you can, they offer some of the best risk-adjusted returns available with true portfolio diversification benefits. 📊💰⚖️📉

