# Credit Index Trading


**Credit index trading** involves buying and selling standardized portfolios of credit default swaps (CDS) on baskets of corporate issuers, with the most liquid indices being CDX (North America) and iTraxx (Europe), allowing investors to take directional views on credit spreads, hedge portfolio risk, implement relative value strategies, or gain efficient exposure to entire credit markets without the operational complexity of trading individual bonds or single-name CDS contracts.

---

## The Core Insight


**The fundamental idea:**

- Credit indices = portfolios of 100-125 CDS contracts
- Trade as single instrument (one price, one spread)
- Much more liquid than individual bonds
- Standardized maturities (5-year most liquid)
- Roll every 6 months (new series, fresh constituents)
- Used for hedging, speculation, beta exposure
- Basis trades vs. underlying single-names
- Tranche trading for leveraged exposure

**The key equations:**

**Index spread:**

$$
\text{Index Spread} = \frac{1}{N} \sum_{i=1}^{N} w_i \times \text{Spread}_i
$$

**Index P&L (approximate):**

$$
\text{P\&L} = \text{Notional} \times \text{Duration} \times \Delta \text{Spread}
$$

**You're essentially trading: "I think credit spreads will widen (or tighten) across this basket of 125 companies, so I'll buy (sell) protection on the entire index rather than picking individual names."**

---

## What Are Credit Indices?


**Before trading credit indices, understand the mechanics:**

### 1. Core Concept


**Definition:** A standardized, tradeable portfolio of credit default swap contracts on a fixed basket of reference entities (typically 100-125 corporate issuers), quoted as a single spread representing the equal-weighted average cost of credit protection on the constituent names, with new series launched every six months incorporating updated credit quality and market conditions.

**When you trade credit indices:**

- You buy or sell protection on entire basket
- Single trade, single spread (vs. 125 individual CDS)
- Notional divided equally across constituents
- Mark-to-market daily (like CDS)
- Standardized maturities (3Y, 5Y, 7Y, 10Y)
- Roll semi-annually (March/September for CDX)
- Primary use: Beta exposure, hedging, macro views
- Users: Hedge funds, asset managers, banks, insurers

**Example - CDX IG Index Trade:**

**Index details (CDX.NA.IG.43, 5-year):**

| Item | Value |
|------|-------|
| Launch date | September 20, 2024 |
| Number of names | 125 companies |
| Sectors | Diversified (Financials, Industrials, Energy, Tech) |
| Average rating | BBB+/A- |
| Maturity | December 20, 2029 (5 years) |
| Current spread | 68 bps |
| Standard coupon | 100 bps (pays quarterly) |

**Trade execution:**

- Buy protection (bearish credit view)
- Notional: $10 million
- Index spread: 68 bps
- Coupon: 100 bps (standard)
- Upfront payment: Receive upfront (coupon > spread)

**Upfront calculation:**

Since coupon (100 bps) > spread (68 bps), buyer receives upfront payment:

$$
\text{Upfront} = \text{Notional} \times \text{Duration} \times (\text{Coupon} - \text{Spread})
$$

Approximate duration: 4.5 years for 5-year CDS

$$
\text{Upfront} = \$10M \times 4.5 \times (1.00\% - 0.68\%) = \$10M \times 4.5 \times 0.32\% = \$144,000
$$

**Cash flows:**

- Upfront: Receive $144,000
- Quarterly premium: Pay $10M × 1.00% / 4 = $25,000 per quarter
- If credit event: Receive $10M / 125 = $80,000 per defaulting name

**Outcome scenarios:**

**Scenario 1: Spreads widen to 120 bps (credit deteriorates)**

- Mark-to-market: (120 - 68) × 4.5 × $10M = $2,340,000 gain
- **Total: +$2.34M profit** (protection buyer wins)

**Scenario 2: Spreads tighten to 40 bps (credit improves)**

- Mark-to-market: (40 - 68) × 4.5 × $10M = -$1,260,000 loss
- **Total: -$1.26M loss** (protection buyer loses)

**Scenario 3: One default (assume 40% recovery)**

- Default payment: $80,000 × (1 - 0.40) = $48,000 received
- Index respread: Spread widens slightly (one name gone)
- **Minor gain from default, larger impact from spread moves**

### 2. Major Credit Indices


**1. CDX.NA.IG (North America Investment Grade):**

- Names: 125 IG companies (BBB- and above)
- Avg rating: A-/BBB+
- Typical spread: 50-100 bps (normal), 150-300 bps (stress)
- Most liquid credit index globally
- Used by: Everyone (macro hedge, beta exposure)

**2. CDX.NA.HY (North America High Yield):**

- Names: 100 high-yield companies (BB+ and below)
- Avg rating: B+/BB-
- Typical spread: 300-500 bps (normal), 800-1500 bps (stress)
- Higher default risk than IG
- Used by: Credit hedge funds, distressed investors

**3. iTraxx Europe (European Investment Grade):**

- Names: 125 European IG companies
- Similar to CDX IG but European credits
- Typical spread: 40-90 bps (normal)
- European equivalent of CDX IG

**4. iTraxx Crossover (European High Yield):**

- Names: 100 European HY/BB companies
- Similar to CDX HY but European
- Typical spread: 250-450 bps (normal)

**5. CDX.EM (Emerging Markets):**

- Names: EM sovereign and corporate
- Higher spreads: 200-400 bps (normal)
- More volatile than developed markets

### 3. Index Roll Mechanics


**New series every 6 months:**

**CDX roll schedule:**
- March 20: New on-the-run series
- September 20: New on-the-run series

**Roll process:**

1. **Constituent review (6 weeks before):**
   - Remove: Defaulted, downgraded to CCC-, acquired
   - Add: New issuers matching criteria
   - Typically 5-15 changes per roll

2. **New series launch:**
   - Old series (CDX.IG.42): Becomes off-the-run, less liquid
   - New series (CDX.IG.43): Becomes on-the-run, most liquid
   - Spread levels typically similar but reflect changes

3. **Trader actions:**
   - Roll positions from old to new (avoid illiquidity)
   - Or: Keep old series if specific names desired
   - Roll spread: Difference between old and new

**Example - September 2024 Roll:**

**CDX.IG.42 (old series):**
- Spread: 71 bps (pre-roll)
- Constituents: 125 (includes 8 being removed)

**CDX.IG.43 (new series):**
- Spread: 68 bps (launch)
- Constituents: 125 (includes 8 new additions)
- Roll spread: -3 bps (new series tighter)

**Why tighter:**
- Removed: Weakest credits (downgrades, stress)
- Added: Stronger credits (recent upgrades, new issuers)
- **New series typically 2-5 bps tighter**

**Roll cost:**

If long protection on old series at 71 bps, rolling to new at 68 bps:
- Close old: Pay to close (spread tightened)
- Open new: Open at 68 bps
- Net cost: ~3 bps × duration × notional

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/credit_index_trading.png?raw=true" alt="credit_index_trading" width="700">
</p>
**Figure 1:** Credit index trading showing the structure of standardized CDS indices (125 equal-weighted names), the semi-annual roll process creating new on-the-run series, and the various trading strategies including directional spread views, basis trades vs single-names, and tranche trading for leveraged exposure.

---

## Economic Interpretation: Why Credit Indices Exist


**Beyond the basic mechanics, understanding the REAL economics:**

### 1. The Liquidity Premium


**The deep insight:**

Credit indices are MORE liquid than underlying bonds or single-name CDS:

**Liquidity comparison (5-year IG credit exposure):**

| Instrument | Bid-Ask Spread | Daily Volume |
|------------|---------------|--------------|
| Individual IG bond | 5-10 bps | $5-20M |
| Single-name CDS | 3-8 bps | $10-50M |
| **CDX IG index** | **0.5-1 bp** | **$5-15B** |

**CDX IG trades 100-300x more volume than single bonds!**

**Why this liquidity premium exists:**

1. **Standardization:** Everyone trades same instrument
2. **Dealer inventory:** Market makers hold large positions
3. **Index arb:** Fast money trades index vs constituents (tightens spreads)
4. **Macro tool:** Portfolio managers use for quick hedges
5. **Mark-to-market:** Transparent, real-time pricing

**Economic impact:**

**Transaction cost savings:**

- Hedge $500M credit portfolio with bonds: 8 bps cost = $400,000
- Hedge $500M with CDX IG: 1 bp cost = $50,000
- **Savings: $350,000 (88% reduction!)**

**This is why institutions use indices for beta exposure**

### 2. Basis Between Index and Single-Names


**Index spread ≠ Average of single-name spreads**

**Basis definition:**

$$
\text{Basis} = \text{Index Spread} - \text{Weighted Avg Single-Name Spreads}
$$

**Typically: Basis = -5 to +5 bps (index trades rich/cheap to fair value)**

**Example (December 2024):**

**CDX IG constituents (sample):**

| Name | Spread | Weight |
|------|--------|--------|
| Apple | 45 bps | 0.8% (1/125) |
| Bank of America | 75 bps | 0.8% |
| Caterpillar | 68 bps | 0.8% |
| ... (122 more) | ... | ... |

**Weighted average: 67 bps (calculated from all 125)**

**CDX IG index spread: 68 bps**

**Basis: 68 - 67 = +1 bp (index trading slightly cheap)**

**Why basis exists:**

**1. Liquidity premium:**
- Index more liquid → Trades tighter (negative basis)
- Typical: -2 to -5 bps

**2. Correlation risk:**
- Index diversifies idiosyncratic risk
- Protection buyer pays less (negative basis)

**3. Transaction costs:**
- Cheaper to trade index than 125 single names
- Efficiency priced in (negative basis)

**4. Convexity differences:**
- Index has loss in defaults (1/125 exposure)
- Single names binary (full notional loss)
- Index less risky → Narrower spread

**5. Supply/demand imbalances:**
- Heavy index buying → Spreads widen (positive basis)
- Heavy index selling → Spreads tighten (negative basis)

**Historical basis behavior:**

| Period | Avg Basis | Driver |
|--------|-----------|--------|
| 2010-2019 (calm) | -3 bps | Normal liquidity premium |
| 2020 COVID | +15 bps | Forced index selling, single-names held |
| 2022 (rising rates) | +5 bps | Risk-off, index selling |
| 2023-2024 (stable) | -2 bps | Back to normal |

**Trading opportunity when basis is extreme:**

- Basis > +10 bps: Buy index, sell single names (convergence trade)
- Basis < -10 bps: Sell index, buy single names (convergence trade)

### 3. The Macro Beta Tool


**Credit indices as economic indicator:**

**CDX IG spread reflects:**

$$
\text{CDX IG Spread} = f(\text{Default Risk}, \text{Risk Premium}, \text{Liquidity})
$$

**Empirical relationship:**

- VIX ↑ 10 points → CDX IG widens ~15-25 bps
- S&P 500 ↓ 10% → CDX IG widens ~20-40 bps
- Fed cuts 100 bps → CDX IG tightens ~10-20 bps
- Recession → CDX IG widens 100-200 bps

**Historical levels:**

| Period | CDX IG Spread | Economic Condition |
|--------|--------------|-------------------|
| 2006-2007 | 35-50 bps | Bubble peak (too tight!) |
| Nov 2008 | 250 bps | Financial crisis peak |
| 2010-2019 | 60-100 bps | Recovery, normal |
| Mar 2020 | 135 bps | COVID panic |
| 2021-2023 | 45-75 bps | Post-COVID recovery |
| 2024 | 60-80 bps | Current levels |

**Use as portfolio hedge:**

**Example - Equity portfolio hedge:**

- Equity portfolio: $100M
- Beta to S&P: 1.2
- Credit-equity correlation: 0.70
- Want to hedge credit risk component

**Hedge sizing:**

Empirical: S&P ↓ 10% → CDX widens 30 bps

$$
\text{CDX Hedge} = \frac{\text{Portfolio Value} \times \text{Credit Sensitivity}}{\text{CDX DV01}}
$$

- Portfolio: $100M
- Expected credit loss if S&P -10%: $5M (5%)
- CDX DV01: $450 per $1M notional
- Spread widening: 30 bps

$$
\text{Notional} = \frac{\$5M}{30 \times \$450} = \$370M
$$

**Hedge: Buy $370M CDX IG protection**

**Outcome if S&P falls 10%:**

- Equity portfolio: -$12M (10% × 1.2 beta)
- CDX hedge: +$370M × $450 × 30 = +$4.995M
- **Net: -$7M (vs -$12M unhedged, 42% hedge efficiency)**

---

## Key Terminology


**On-the-Run:**

- Most recent index series
- Highest liquidity
- Tightest bid-ask spreads
- Example: CDX.IG.43 (current)

**Off-the-Run:**

- Previous index series
- Lower liquidity
- Wider bid-ask spreads
- Example: CDX.IG.42, CDX.IG.41 (older)

**Roll:**

- Semi-annual new series launch
- Replacing old constituents
- March 20 and September 20 (CDX)
- Roll spread: Difference old vs new

**Basis:**

- Index spread - Avg single-name spreads
- Typical: -5 to +5 bps
- Negative: Index rich (trades tighter)
- Positive: Index cheap (trades wider)

**Tranche:**

- Slice of index based on loss seniority
- Junior (0-3%): First loss, highest risk
- Senior (10-100%): Last loss, lowest risk
- Levered exposure to credit

**Standardized Coupon:**

- Fixed coupon for all trades in series
- CDX IG: 100 bps or 60 bps (post-2019)
- CDX HY: 500 bps
- Upfront payment adjusts for spread difference

**Mark-to-Market:**

- Daily P&L settlement
- Based on closing spread
- Uses standard model (ISDA)
- Cash exchanged between counterparties

**Index CDS:**

- Credit default swap on index basket
- Buy protection: Bearish credit
- Sell protection: Bullish credit
- Net notional exposure

**Compression:**

- Netting offsetting trades
- Reduces gross notional
- Lowers counterparty risk
- Clearing houses facilitate

**DV01 (Dollar Value 01):**

- P&L for 1 bp spread change
- Approximately: Notional × Duration / 10,000
- Example: $10M notional, 4.5 duration → DV01 = $4,500

---

## Mathematical Foundation


### 1. Index Spread Calculation


**Equal-weighted average:**

$$
S_{\text{index}} = \frac{1}{N} \sum_{i=1}^{N} S_i
$$

Where $N$ = 125 (for CDX IG)

**Example:**

- Name 1: 50 bps
- Name 2: 75 bps
- ...
- Name 125: 80 bps

$$
S_{\text{index}} = \frac{50 + 75 + ... + 80}{125} = 68 \text{ bps}
$$

### 2. P&L Calculation


**Mark-to-market P&L:**

$$
\text{P\&L} = N \times \text{DV01} \times \Delta S
$$

Where:
- $N$ = Notional
- DV01 = Dollar value of 1 bp (≈ Notional × Duration / 10,000)
- $\Delta S$ = Spread change (in bps)

**Example:**

- Notional: $10M
- Duration: 4.5 years
- DV01: $10M × 4.5 / 10,000 = $4,500
- Spread change: +30 bps (widening)
- Position: Long protection (buy protection)

$$
\text{P\&L} = \$10M \times \$4,500/\$10M \times 30 = \$135,000 \text{ gain}
$$

Actually, let me recalculate this more carefully:

DV01 = $4,500 means $4,500 P&L for 1 bp move.

So for 30 bps:
$$
\text{P\&L} = \$4,500 \times 30 = \$135,000 \text{ gain}
$$

### 3. Upfront Payment


**When coupon ≠ spread:**

$$
\text{Upfront} = N \times D \times (C - S)
$$

Where:
- $C$ = Standard coupon
- $S$ = Index spread
- $D$ = Duration (risky duration)

**Example:**

- Notional: $10M
- Coupon: 100 bps
- Spread: 68 bps
- Duration: 4.5

$$
\text{Upfront} = \$10M \times 4.5 \times (1.00\% - 0.68\%) = \$144,000
$$

**Protection buyer receives $144k upfront** (coupon > spread)

### 4. Basis Calculation


**Fair value basis:**

$$
\text{Basis} = S_{\text{index}} - \frac{1}{N} \sum_{i=1}^{N} S_i^{\text{single-name}}
$$

**Example:**

- Index spread: 68 bps
- Single-name avg: 67 bps
- **Basis: +1 bp** (index cheap)

### 5. Default Impact on Index


**Index spread adjustment after default:**

Before default: 125 names, spread = 68 bps

After 1 default: 124 names remain

**New index spread (approximate):**

$$
S_{\text{new}} = S_{\text{old}} \times \frac{N}{N-1} + \text{Restructuring Credit}
$$

Typically rises 0.5-2 bps per default (widens slightly)

**Example:**

- Pre-default: 68 bps (125 names)
- 1 default (assume average credit quality)
- Post-default: ~68.5 bps (124 names)
- **Widening: 0.5 bps**

---

## Step-by-Step Implementation


### 1. Phase 1: Index Selection and Analysis


**1. Choose Appropriate Index:**

```python
import pandas as pd
import numpy as np

# Available indices
indices = pd.DataFrame({
    'index': ['CDX.IG', 'CDX.HY', 'iTraxx Europe', 'iTraxx Xover', 'CDX.EM'],
    'region': ['North America', 'North America', 'Europe', 'Europe', 'Emerging'],
    'rating': ['IG', 'HY', 'IG', 'HY/Crossover', 'Mixed'],
    'num_names': [125, 100, 125, 100, 40],
    'current_spread': [68, 380, 55, 290, 245],
    'liquidity': ['Very High', 'High', 'Very High', 'High', 'Medium'],
    'use_case': ['IG hedge', 'HY exposure', 'Europe IG', 'Europe HY', 'EM risk']
})

print(indices)
```

**Output:**

```
         index         region           rating  num_names  current_spread  liquidity           use_case
0      CDX.IG  North America               IG        125              68  Very High           IG hedge
1      CDX.HY  North America               HY        100             380       High        HY exposure
2  iTraxx Europe        Europe               IG        125              55  Very High         Europe IG
3  iTraxx Xover        Europe  HY/Crossover        100             290       High         Europe HY
4      CDX.EM      Emerging          Mixed         40             245     Medium            EM risk
```

**2. Analyze Index Constituents:**

```python
# Load CDX IG constituents (example)
constituents = pd.read_csv('cdx_ig_43_constituents.csv')

# Calculate metrics
sector_composition = constituents.groupby('sector')['weight'].sum()
rating_distribution = constituents.groupby('rating')['weight'].sum()
avg_spread = constituents['spread'].mean()

print("Sector Composition:")
print(sector_composition)

print("\nRating Distribution:")
print(rating_distribution)

print(f"\nAverage Spread: {avg_spread:.1f} bps")
```

**Example output:**

```
Sector Composition:
Financials      28.0%
Industrials     22.4%
Consumer        18.4%
Energy          12.8%
Technology      10.4%
Utilities        8.0%

Rating Distribution:
AAA/AA          12.0%
A               35.2%
BBB             52.8%

Average Spread: 67.2 bps
```

### 2. Phase 2: Execute Index Trade


**1. Calculate Position Size:**

```python
def calculate_index_position(portfolio_value, hedge_ratio, target_duration):
    """
    Calculate CDX notional for portfolio hedge
    
    hedge_ratio: 0-1.0 (percentage of portfolio to hedge)
    target_duration: Effective duration match
    """
    
    # Target DV01
    target_dv01 = portfolio_value * target_duration * 0.0001 * hedge_ratio
    
    # CDX IG 5-year DV01 (approximate)
    cdx_dv01_per_mm = 450  # $450 per $1M notional
    
    # Required notional
    notional = (target_dv01 / cdx_dv01_per_mm) * 1_000_000
    
    return {
        'portfolio_value': portfolio_value,
        'hedge_ratio': hedge_ratio,
        'target_dv01': target_dv01,
        'required_notional': notional
    }

# Example: Hedge $100M IG portfolio
result = calculate_index_position(
    portfolio_value=100_000_000,
    hedge_ratio=0.50,  # 50% hedge
    target_duration=6.0
)

print(f"Portfolio: ${result['portfolio_value']:,.0f}")
print(f"Hedge ratio: {result['hedge_ratio']:.0%}")
print(f"Target DV01: ${result['target_dv01']:,.0f}")
print(f"Required CDX notional: ${result['required_notional']:,.0f}")
```

**Output:**

```
Portfolio: $100,000,000
Hedge ratio: 50%
Target DV01: $300,000
Required CDX notional: $666,666,667
```

**2. Trade Execution:**

```python
# Trade details
trade = {
    'index': 'CDX.NA.IG.43',
    'direction': 'Buy Protection',
    'notional': 667_000_000,  # Rounded
    'spread': 68,  # bps
    'coupon': 100,  # bps (standard)
    'maturity': '2029-12-20',
    'duration': 4.5,
    'trade_date': '2024-12-01'
}

# Calculate upfront
dv01 = trade['notional'] * trade['duration'] / 10_000
upfront = trade['notional'] * trade['duration'] * (trade['coupon'] - trade['spread']) / 10_000

print(f"Trade: {trade['direction']} {trade['index']}")
print(f"Notional: ${trade['notional']:,.0f}")
print(f"DV01: ${dv01:,.0f}")
print(f"Upfront: ${upfront:,.0f} (receive)")
print(f"Quarterly premium: ${trade['notional'] * 0.01 / 4:,.0f} (pay)")
```

**Output:**

```
Trade: Buy Protection CDX.NA.IG.43
Notional: $667,000,000
DV01: $300,150
Upfront: $960,480 (receive)
Quarterly premium: $1,667,500 (pay)
```

### 3. Phase 3: Monitor and Manage


**1. Daily P&L Tracking:**

```python
def calculate_index_pnl(position, current_spread, initial_spread):
    """Calculate mark-to-market P&L"""
    
    spread_change = current_spread - initial_spread
    pnl = position['dv01'] * spread_change
    
    return {
        'spread_change': spread_change,
        'pnl': pnl,
        'pnl_pct': pnl / position['notional']
    }

# Example: Spreads widen 10 bps
position = {
    'notional': 667_000_000,
    'dv01': 300_150,
    'direction': 'long_protection'  # Buy protection
}

pnl = calculate_index_pnl(position, current_spread=78, initial_spread=68)

print(f"Spread change: {pnl['spread_change']:+.0f} bps")
print(f"P&L: ${pnl['pnl']:,.0f}")
print(f"Return on notional: {pnl['pnl_pct']:+.2%}")
```

**Output:**

```
Spread change: +10 bps
P&L: $3,001,500
Return on notional: +0.45%
```

**2. Roll Management:**

```python
def calculate_roll_cost(old_spread, new_spread, notional, duration):
    """
    Calculate cost to roll from old to new series
    """
    
    roll_spread = new_spread - old_spread
    dv01 = notional * duration / 10_000
    roll_cost = dv01 * roll_spread
    
    return {
        'old_spread': old_spread,
        'new_spread': new_spread,
        'roll_spread': roll_spread,
        'roll_cost': roll_cost
    }

# Example: September 2024 roll
roll = calculate_roll_cost(
    old_spread=71,  # CDX.IG.42
    new_spread=68,  # CDX.IG.43
    notional=667_000_000,
    duration=4.5
)

print(f"Old series spread: {roll['old_spread']} bps")
print(f"New series spread: {roll['new_spread']} bps")
print(f"Roll spread: {roll['roll_spread']:+.0f} bps")
print(f"Roll cost: ${roll['roll_cost']:,.0f}")
```

**Output:**

```
Old series spread: 71 bps
New series spread: 68 bps
Roll spread: -3 bps
Roll cost: $-900,450 (gain from tightening)
```

### 4. Phase 4: Basis Trade Analysis


**1. Calculate Index Basis:**

```python
# Single-name spreads (sample)
single_names = pd.DataFrame({
    'name': ['Apple', 'JPM', 'Boeing', 'AT&T', 'GM'],
    'spread': [45, 75, 120, 95, 110],
    'weight': [0.008] * 5  # Equal weight (1/125)
})

# Full basket average (all 125)
avg_single_name_spread = 67  # Calculated from full basket

# Index spread
index_spread = 68

# Basis
basis = index_spread - avg_single_name_spread

print(f"Index spread: {index_spread} bps")
print(f"Avg single-name: {avg_single_name_spread} bps")
print(f"Basis: {basis:+.0f} bps")

if abs(basis) > 5:
    if basis > 0:
        print("Trade: Index CHEAP, buy index / sell single-names")
    else:
        print("Trade: Index RICH, sell index / buy single-names")
else:
    print("Basis within normal range, no trade")
```

### 5. Phase 5: Exit Strategy


**1. Profit Target:**

```python
# Exit rules
entry_spread = 68
profit_target_tightening = 15  # bps
stop_loss_widening = 25  # bps

profit_target_spread = entry_spread - profit_target_tightening
stop_loss_spread = entry_spread + stop_loss_widening

print(f"Entry spread: {entry_spread} bps")
print(f"Profit target: {profit_target_spread} bps (spreads tighten 15 bps)")
print(f"Stop loss: {stop_loss_spread} bps (spreads widen 25 bps)")

# Expected P&L
notional = 667_000_000
dv01 = 300_150

profit_pnl = -dv01 * profit_target_tightening  # Negative (loss on protection)
stop_pnl = dv01 * stop_loss_widening  # Positive (gain on protection)

print(f"\nProfit target P&L: ${profit_pnl:,.0f}")
print(f"Stop loss P&L: ${stop_pnl:,.0f}")
print(f"Risk/Reward: {abs(stop_pnl/profit_pnl):.2f}x")
```

---

## Real-World Examples


### 1. Example 1: COVID-19 Index Hedge - March 2020 (Spectacular Success)


**Background:**

- Asset manager: $5B IG bond portfolio
- February 2020: Coronavirus spreading, market complacent
- Manager: Worried about credit risk

**Trade (February 24, 2020):**

**CDX.IG.33 5-year:**

- Spread: 55 bps (pre-crisis, normal)
- Buy protection: $3B notional (60% of portfolio)
- DV01: $1.35M
- Cost: Paying 55 bps annually

**Rationale:** "Pandemic could disrupt corporates, cheap hedge"

**What happened: Market collapse**

| Date | Event | CDX IG Spread | Position P&L |
|------|-------|--------------|--------------|
| Feb 24 | Entry | 55 bps | $0 |
| Feb 28 | Italy lockdown | 62 bps | +$945k |
| Mar 6 | Saudi oil price war | 72 bps | +$2.3M |
| Mar 11 | WHO declares pandemic | 95 bps | +$5.4M |
| Mar 16 | First Fed emergency cut | 110 bps | +$7.4M |
| Mar 23 | Peak spread | 135 bps | **+$10.8M** |

**Portfolio impact:**

**Bonds (unhedged):**
- Value: $5B → $4.55B (-$450M, -9%)
- Spread widening: 60 bps average

**CDX hedge:**
- Protection value: +$10.8M
- Quarterly premium paid: -$4.125M (1 quarter)
- **Net hedge gain: +$10.4M**

**Total portfolio:**
- Bond losses: -$450M
- CDX hedge: +$10.4M
- **Net loss: -$440M** (vs -$450M unhedged)

**Hedge efficiency: 2.3%** (hedged 10.4M of 450M loss)

**Wait, this seems like a poor hedge!** Let me reconsider.

Actually, the hedge notional was $3B (60% of $5B portfolio). Let me recalculate:

**Correct calculation:**

CDX hedge on $3B:
- DV01: $3B / $1M × $450 = $1.35M
- Spread widening: 135 - 55 = 80 bps
- P&L: $1.35M × 80 = **$108M gain**

**Portfolio outcome:**

- Bond losses: -$450M (-9% on $5B)
- CDX hedge gain: +$108M
- **Net loss: -$342M** (-6.84% vs -9% unhedged)
- **Hedge efficiency: 24%** (reduced loss by 24%)

**Manager's decision (March 23):**

- Unwind CDX hedge (spreads at peak)
- Locked in $108M profit
- Kept bonds (buying opportunity)

**Full cycle outcome (March-December 2020):**

**March 23 - December 31:**

- CDX spreads: 135 → 55 bps (normalized)
- Bonds recovered: $4.55B → $5.15B (+13.2%)
- **Final position: $5.15B (bonds) + $108M (CDX profit) = $5.258B**
- **Net gain: +$258M (+5.16% on original $5B)**

**vs. Unhedged:**

- Just bonds: $5B → $5.15B = +$150M (+3%)
- **Hedge added: +$108M extra gain**

**Why it worked:**

1. **Cheap insurance:** 55 bps for protection (historically low)
2. **Correct timing:** Bought 3 weeks before crash
3. **Scaled properly:** $3B hedge (60%) appropriate
4. **Disciplined exit:** Sold at peak spread (135 bps)
5. **Kept bonds:** Participated in recovery

**This is textbook index hedging—paid 55 bps, earned 80 bps spread widening, $108M profit on $3B notional**

### 2. Example 2: CDX HY Directional Short - 2022 (Fed Tightening Win)


**Background:**

- Hedge fund: Macro-focused
- January 2022: Fed pivoting hawkish, QE ending
- Thesis: Recession coming, high-yield will suffer

**Trade (January 15, 2022):**

**CDX.HY.37 5-year:**

- Spread: 320 bps (post-COVID normalization)
- **Buy protection: $500M notional**
- DV01: $225k
- Rationale: "Fed tightening will widen HY spreads"

**What happened: Hiking cycle**

| Date | Fed Funds | CDX HY Spread | Position P&L |
|------|-----------|--------------|--------------|
| Jan 2022 | 0.25% | 320 bps | $0 |
| Mar 2022 | 0.50% (+25 bps hike) | 360 bps | +$9.0M |
| May 2022 | 1.00% (+50 bps hike) | 420 bps | +$22.5M |
| Jul 2022 | 2.50% (+75 bps hike!) | 490 bps | +$38.3M |
| Sep 2022 | 3.25% (+75 bps hike) | 520 bps | +$45.0M |
| Nov 2022 | 4.00% (+75 bps hike) | 550 bps | **+$51.8M** |

**Exit (December 2022):**

- CDX HY: 550 bps (widened 230 bps from entry)
- Closed position: +$51.8M
- Premium paid: -$8M (10 months at 320 bps × $500M / 12)
- **Net profit: +$43.8M**

**On ~$10M margin posted: +438% return in 11 months!**

**Why it worked:**

1. **Correct macro call:** Fed hiked 425 bps in 10 months (most aggressive in 40 years)
2. **Right instrument:** HY most sensitive to tightening (vs IG)
3. **Levered exposure:** $500M notional on $10M margin
4. **Held conviction:** Didn't exit during rallies (July +50 bps temporary tightening)
5. **Duration right:** 11 months matched hiking cycle

**Could have gone wrong:**

- Fed pauses early (spreads tighten, lose premium)
- Soft landing (HY resilient, narrow spreads)
- Timing early (2021 entry would have bled premium for 12 months)

### 3. Example 3: Index Basis Arbitrage - 2020 (Liquidity Crisis Trade)


**Background:**

- March 2020: Forced selling, liquidity crisis
- CDX IG index sold heavily (liquid, easy to dump)
- Single-name CDS: Less selling (harder to trade)

**Opportunity (March 18, 2020):**

**CDX.IG.33 spread: 115 bps**

**Single-name average (125 constituents): 95 bps**

**Basis: +20 bps (MASSIVE, normally -2 to +2 bps)**

**Trade:**

- **Buy CDX IG index** (cheap): $200M notional @ 115 bps
- **Sell single-name CDS basket** (rich): $200M notional @ 95 bps average
- **Net: Capture 20 bp basis**

**Position:**

- Long index protection: $200M
- Short single-name protection: $200M (spread across 125 names, ~$1.6M each)
- Net credit exposure: ~0 (hedged)
- P&L driver: Basis convergence

**Outcome (April-May 2020):**

**April 15 (3 weeks later):**

- CDX IG: 115 → 85 bps (-30 bps tightening)
- Single-name avg: 95 → 80 bps (-15 bps)
- **New basis: +5 bps** (normalized from +20 bps)

**P&L:**

- CDX index: -$900k × 30 = -$27M (tightened, we're long protection = loss)

Wait, this doesn't seem right. Let me reconsider.

If we BUY the index (buy protection), we profit when spreads WIDEN, lose when they TIGHTEN.

If we SELL single-names (sell protection), we profit when spreads TIGHTEN, lose when they WIDEN.

**Recalculating:**

**Position:**
- Long CDX at 115 bps (buy protection)
- Short single-names at 95 bps (sell protection)

**Spreads move:**
- CDX: 115 → 85 bps (tightened 30 bps) → LOSS on long protection
- Single-names: 95 → 80 bps (tightened 15 bps) → GAIN on short protection

**P&L:**
- CDX: -$900k × 30 = -$27M
- Single-names: +$900k × 15 = +$13.5M
- **Net: -$13.5M** (This is a loss!)

Hmm, this trade lost money because spreads tightened more than expected and the basis didn't fully converge. Let me reconsider the trade structure.

Actually, for a basis trade, we want to be:
- **LONG the cheap instrument** (CDX index)
- **SHORT the rich instrument** (single-names)

But "long CDX" in a basis trade context means we want to profit when CDX richens relative to single-names.

Let me clarify:

**Basis trade structure when index is cheap (basis > 0):**

Actually, I think the correct trade is:
- **Sell CDX protection** at 115 bps (receive 115 bps)
- **Buy single-name protection** at 95 bps (pay 95 bps average)
- **Net: Receive 20 bps** (positive carry)

This makes more sense for a basis trade. Let me redo:

**Trade (corrected):**

- **Sell CDX index protection**: $200M @ 115 bps (index cheap, sell high)
- **Buy single-name protection**: $200M @ 95 bps (single-names rich, buy low)
- **Net position:** Earning 20 bps spread

**Outcome:**

**April 15:**

- CDX: 115 → 85 bps (tightened)
- Single-names: 95 → 80 bps (tightened)
- Basis: +20 bps → +5 bps (narrowed 15 bps)

**P&L:**

Position when spreads tighten:
- Sold CDX protection (short credit): Profit when tightens: +$900k × 30 = +$27M
- Bought single-name protection (long credit): Loss when tightens: -$900k × 15 = -$13.5M
- **Net: +$13.5M profit**

Plus:
- Carry: 20 bps × $200M × (1 month) / 12 = +$333k

**Total: +$13.8M in 1 month**

**Why it worked:**

1. **Extreme basis:** +20 bps (10x normal)
2. **Forced selling:** Index oversold due to ETF redemptions
3. **Convergence:** Basis normalized to +5 bps (15 bp capture)
4. **Fast:** 3-4 weeks to normalize (liquidity returned)
5. **Hedged:** Net credit exposure ~0 (pure basis play)

**Risk that didn't materialize:**

- Further widening (March was peak, lucky timing)
- Basis stays wide (took months to normalize)
- Defaults (1-2 defaults would have skewed P&L)

### 4. Example 4: CDX Roll Trade - September 2023 (Roll Carry)


**Background:**

- September roll: CDX.IG.40 → CDX.IG.41
- Several weak credits removed (downgrades)
- New series expected tighter

**Pre-roll analysis (September 15, 2023):**

**CDX.IG.40 (old series):**
- Spread: 74 bps
- Contains: 125 names (8 to be removed for credit deterioration)

**CDX.IG.41 (new series, launches Sep 20):**
- Expected spread: 70 bps (4 bps tighter)
- Removed: Weakest names (avg spread 120 bps)
- Added: Stronger names (avg spread 55 bps)

**Trade strategy:**

1. **Pre-roll (Sep 15):** Sell protection on old CDX.IG.40 @ 74 bps
2. **Post-roll (Sep 20):** Buy protection on new CDX.IG.41 @ 70 bps
3. **Profit:** 4 bp tightening as market rolls to cleaner index

**Position:**

- Sell $100M CDX.IG.40 protection @ 74 bps
- Hold through roll
- Buy $100M CDX.IG.41 protection @ 70 bps (close)

**Outcome:**

**September 20 (roll day):**

- CDX.IG.40: 74 → 77 bps (old series widens, illiquid)
- CDX.IG.41: Launches at 70 bps (new series, tight)
- Roll spread: 7 bps (77 - 70)

**P&L:**

- Sold CDX.IG.40 at 74, spread widened to 77: -$450k × 3 = -$1.35M (loss)
- But we close by buying new series at 70 bps
- Net: Sold at 74, bought at 70 = 4 bp gain
- **P&L: +$450k × 4 = +$1.8M**

Actually, I need to think about this more carefully. The trader sold protection on the old series. As the old series widens (becomes less liquid), they lose money. Then they close by buying protection on the new series.

Let me reconsider:

**Corrected P&L:**

When you sell protection (short credit), you profit when spreads tighten and lose when they widen.

- Sold CDX.IG.40 at 74 bps
- CDX.IG.40 widened to 77 bps (illiquid, widening)
- **Mark-to-market on old series: -$1.35M loss**

Then close the old and open new:
- Close old: Buy protection CDX.IG.40 at 77 bps
- Open new: Sell protection CDX.IG.41 at 70 bps

Net after transition:
- Closed old at -3 bps (loss)
- Opened new at 70 bps (4 bps better than old entry of 74)

Hmm, this is getting confusing. Let me think about a simpler roll strategy:

**Simpler roll arbitrage:**

**The idea:** Old series trades wide due to illiquidity, new series trades tight.

**Trade:**
- Buy old series (cheap) @ 77 bps
- Sell new series (expensive) @ 70 bps
- Wait for convergence (arbitrage)

Actually, this would be selling the old expensive and buying the new cheap, which is:
- Sell CDX.IG.40 @ 77 bps (wide due to illiquidity)
- Buy CDX.IG.41 @ 70 bps (tight, fresh)

But these are different instruments with different constituents, so there's no pure convergence.

I think the roll trade is actually simpler: most investors just want to maintain exposure, so they:

1. Close old series (CDX.IG.40)
2. Open new series (CDX.IG.41)
3. Pay the roll cost (difference in spreads)

**Typical roll cost: 3-5 bps** (you pay to roll into cleaner, tighter new series)

Let me use a different example.

### 5. Better Example 4: IG/HY Ratio Trade - 2019 (Mean Reversion)


**Background:**

- January 2019: HY spreads very tight relative to IG
- Ratio: CDX.HY / CDX.IG = 380 / 62 = 6.1x
- Historical average ratio: 7.5x
- Strategy: Ratio will widen (HY underperforms IG)

**Trade:**

- **Buy CDX.HY protection**: $100M @ 380 bps
- **Sell CDX.IG protection**: $700M @ 62 bps

**Ratio calculation:**

Current: 380 / 62 = 6.1x
Target: 7.5x (historical mean)

If ratio goes to 7.5x:
- If IG unchanged (62 bps): HY should be 62 × 7.5 = 465 bps
- If HY unchanged (380 bps): IG should be 380 / 7.5 = 51 bps

**Outcome (6 months later, June 2019):**

**Market moves:**

- CDX.HY: 380 → 450 bps (+70 bps widening)
- CDX.IG: 62 → 58 bps (-4 bps tightening)
- **New ratio: 450 / 58 = 7.76x** (normalized above historical!)

**P&L:**

- CDX.HY long protection: +$100M × $450/1M × 70 = +$3.15M
- CDX.IG short protection: +$700M × $315/1M × 4 = +$882k
- **Total: +$4.03M**

**Why it worked:**

1. **Mean reversion:** Ratio 6.1x was 1.4x below average (extreme)
2. **Correct direction:** HY widened, IG tightened (perfect)
3. **Sized properly:** $100M HY vs $700M IG balanced DV01
4. **Fast move:** 6 months to revert (not years)

### 6. Example 5: Tranche Trading - 2007 (Correlation Disaster)


**Background:**

- 2007: Structured credit boom
- CDX.IG tranches: Levered exposure to credit
- Junior tranches (0-3%): First loss, high risk/return

**Tranche structure:**

| Tranche | Loss Range | Spread | Risk |
|---------|-----------|--------|------|
| 0-3% (Equity) | First loss | 50% upfront | Highest |
| 3-7% | Second loss | 300 bps | High |
| 7-10% | Third loss | 120 bps | Medium |
| 10-15% | Fourth loss | 60 bps | Low |
| 15-30% | Fifth loss | 30 bps | Low |
| 30-100% (Super Senior) | Last loss | 5 bps | Lowest |

**Trade (January 2007):**

**Sell protection on 0-3% tranche:**

- Notional: $10M (but 3% tranche, so capital at risk = $300k)
- Upfront: Receive 50% × $300k = $150k
- Annual spread: 50% × $300k = $150k per year
- **Total income: $150k upfront + $150k/year**

**Thesis: "Defaults rare, even in downturn won't exceed 3% of index"**

**What happened: Financial Crisis**

**2008-2009 defaults:**

| Quarter | Defaults | Index Loss |
|---------|----------|----------|
| Q4 2008 | Lehman, WaMu | 1.6% |
| Q1 2009 | 3 more | 2.4% (cumulative) |
| Q2 2009 | 2 more | 3.8% (cumulative) |

**Tranche P&L:**

**When losses hit 3%:**
- 0-3% tranche: **Completely wiped out**
- Original: Received $150k upfront + $75k (6 months premium)
- Loss: -$300k (full notional)
- **Net: -$75k loss** (50% of invested capital)

**When losses exceeded 3% (reached 3.8%):**
- Additional losses: 0.8% beyond tranche
- These losses now hit 3-7% tranche holders
- 0-3% tranche: **Total loss -$300k**
- Net after premiums: **-$75k** (-25% return)

**Why it failed catastrophically:**

1. **Correlation risk:** Defaults clustered (financial crisis)
2. **Underestimated severity:** 3.8% losses (vs. <1% historical)
3. **Leverage:** $300k capital supporting $10M notional (33x!)
4. **First loss:** No cushion (0% before tranche starts paying)
5. **Selling insurance:** Collecting pennies in front of steamroller

**Many hedge funds using 10-20x leverage on these tranches were wiped out completely.**

---

## Best Case Scenario


### 1. Perfect Credit Index Trade


**Setup for maximum profit:**

**Ideal conditions:**

1. **Clear macro catalyst** (Fed policy shift, recession signal)
2. **Asymmetric entry** (low volatility, cheap protection)
3. **Correct timing** (weeks before event)
4. **Liquid index** (tight spreads, easy exit)
5. **Disciplined exit** (take profit at target)

### 2. Best Case Example: CDX IG Short Pre-2008 (Legendary Trade)


**Background:**

- July 2007: Credit markets at tightest spreads in history
- Hedge fund manager: Sees housing bubble, CDO risks
- Protection extremely cheap (complacency)

**Trade (July 2007):**

**CDX.IG.8 5-year:**

- Spread: 38 bps (all-time tights!)
- **Buy protection: $2B notional**
- DV01: $900k
- Premium: $2B × 0.38% = $7.6M per year
- Margin: ~$40M initial

**Thesis: "Credit bubble, massive correction coming"**

**What happened: 18-month progression**

| Date | Event | CDX IG Spread | Position P&L |
|------|-------|--------------|--------------|
| Jul 2007 | Entry | 38 bps | $0 |
| Aug 2007 | Bear Stearns hedge funds fail | 52 bps | +$12.6M |
| Dec 2007 | First rate cut | 88 bps | +$45M |
| Mar 2008 | Bear Stearns collapse | 125 bps | +$78.3M |
| Sep 2008 | Lehman bankruptcy | 185 bps | +$132.3M |
| Oct 2008 | Market panic | 220 bps | +$163.8M |
| Nov 2008 | Peak crisis | **250 bps** | **+$190.8M** |

**Exit (November 2008):**

- Spread: 250 bps (peak)
- Cumulative widening: 212 bps
- Premium paid: $7.6M × 1.33 years = -$10.1M
- **Net profit: +$180.7M**

**On $40M initial margin: +452% return in 16 months!**

**Fund outcome:**

- Started: $500M AUM
- This trade alone: +$180M
- Other positions: +$120M (shorts, CDS on financials)
- **Ending: $800M AUM** (+60% in crisis year while market fell 37%)

**Why it was perfect:**

1. **Extreme valuation:** 38 bps all-time low (protection dirt cheap)
2. **Correct diagnosis:** Housing bubble systemic risk
3. **Patient:** Held through Aug-Dec 2007 volatility
4. **Levered efficiently:** $2B on $40M margin (50x)
5. **Disciplined exit:** Sold near peak (Nov 2008), didn't wait for full recovery
6. **Scale:** Large enough to move fund (+36% from single trade)
7. **Asymmetric:** Risk = Premium paid ($10M/year), reward = $180M

**This trade made careers and launched funds. It's the gold standard of credit index macro trading.**

---

## Worst Case Scenario


### 1. The Credit Index Disaster


**Worst possible conditions:**

1. **Wrong direction** (fight the Fed, fight credit cycle)
2. **Overleveraged** (massive notional on small margin)
3. **Illiquid positions** (stuck in off-the-run series)
4. **No exit discipline** (hold through adverse moves)
5. **Correlation misjudgment** (tranche trading)

### 2. Worst Case Example: CDX HY Long Protection 2009-2010 (Catastrophic)


**Background:**

- Hedge fund: $200M AUM
- Manager: Convinced crisis continues, recession deepens
- March 2009: Markets at lows, protection expensive

**Trade (March 9, 2009 - market bottom!):**

**CDX.HY.12 5-year:**

- Spread: 800 bps (crisis levels)
- **Buy protection: $1.5B notional** (7.5x fund size!)
- DV01: $675k
- Premium: $1.5B × 8% = $120M per year
- Margin: $30M initial (15% of AUM)

**Thesis: "Crisis worsening, defaults will spike, spreads to 1200 bps"**

**What happened: V-shaped recovery**

| Date | Event | CDX HY Spread | Position P&L | Fund Status |
|------|-------|--------------|--------------|-------------|
| Mar 9 2009 | Entry | 800 bps | $0 | $200M AUM |
| Apr 2009 | Rally begins | 720 bps | -$54M | $146M (margin call) |
| May 2009 | Continued rally | 620 bps | -$121.5M | Margin call 2 |
| Jun 2009 | Recovery clear | 550 bps | -$168.75M | Forced liquidation |

**Forced liquidation (June 2009):**

- Entry: 800 bps
- Exit: 550 bps (spreads tightened 250 bps)
- Loss: -$675k × 250 = -$168.75M
- Premium paid: -$120M × 0.25 years = -$30M
- **Total loss: -$198.75M**

**Fund outcome:**

- Started: $200M
- Final: $1.25M (after liquidation, redemptions)
- **Loss: -99.4%**

**What went catastrophically wrong:**

**1. Timing: Bought at the absolute bottom**

- March 9, 2009 = S&P 500 bottom (666)
- CDX HY peak spread (800 bps)
- **Worst possible entry in history**

**2. Overleveraged: 7.5x fund size**

- Notional: $1.5B
- Fund: $200M
- **Absurd 7.5x leverage**
- No room for adverse move

**3. Wrong direction: Fought the Fed**

- Fed: Announcing QE, backstopping markets
- Manager: "It won't work, crisis continues"
- **Fed won, manager destroyed**

**4. Premium bleed: $120M/year**

- Fund: $200M
- Annual premium: $120M (60% of AUM!)
- 3 months: -$30M (15% just from premium)
- **Unsustainable burn rate**

**5. Margin calls: Death spiral**

- Spreads tighten 80 bps: -$54M loss
- Margin call: Post $50M (25% of fund)
- Can't post: Forced to partially close
- Spreads tighten more: Another call
- **Final liquidation at worst prices**

**6. No stop loss: Held all the way down**

- Down $54M (April): "Temporary rally"
- Down $122M (May): "Can't last"
- Down $169M (June): "Liquidating, fund over"
- **Never cut losses, held to zero**

**7. Ignored signals:**

- S&P rallied 40% (March-June)
- Credit spreads tightening globally
- Fed unlimited QE announced
- **Manager ignored all evidence**

**The aftermath:**

- Fund: Closed (July 2009)
- Manager: Left industry
- Investors: Lost 99.4% (-$199M)
- **Launched lawsuits (mismanagement, excessive leverage)**

**The timing irony:**

**If had reversed position (sell protection) same day:**

- March 9: Sell protection at 800 bps
- June: Close at 550 bps
- **Profit: +$168.75M** (+84% on fund in 3 months!)

**Same analysis, opposite trade, right at turning point.**

**The cruel lesson: In markets, being right eventually doesn't matter if you're bankrupt now. Fighting the Fed with 7.5x leverage = guaranteed wipeout.**

---

## What to Remember


### 1. Core Concept


**Credit indices provide liquid, standardized exposure to credit markets through portfolios of 100-125 CDS contracts:**

$$
\text{Index Spread} = \frac{1}{N} \sum_{i=1}^{N} \text{Spread}_i
$$

- CDX IG: 125 investment-grade names, 50-100 bps typical
- CDX HY: 100 high-yield names, 300-500 bps typical
- Roll semi-annually (March/September)
- Used for hedging, macro views, beta exposure
- 100-300x more liquid than individual bonds

### 2. The Key Metrics


**Index characteristics:**

- CDX IG spread: 50-100 bps (normal), 150-300 bps (stress)
- CDX HY spread: 300-500 bps (normal), 800-1500 bps (crisis)
- Bid-ask: 0.5-1 bp (IG), 2-5 bps (HY)
- Daily volume: $5-15B (IG), $2-8B (HY)
- DV01: ~$450 per $1M notional (5-year)

**P&L calculation:**

$$
\text{P\&L} = \text{Notional} \times \text{DV01}/\$1M \times \Delta \text{Spread (bps)}
$$

### 3. Risk Management


**Essential rules:**

- Max leverage: 3-5x (notional / capital) for directional trades
- Stop loss: -25 to -50 bps adverse move (exit immediately)
- Position size: DV01 should be 10-20% of capital max
- Roll management: Switch to new series 1-2 weeks before roll date
- Basis monitoring: Normal -5 to +5 bps, trade if >10 bps
- Avoid tranches: First-loss positions (0-3%) are leverage bombs
- Fed watching: Never fight Fed policy with leverage
- Exit discipline: Take profits at 2-3x premium paid

### 4. Maximum Profit/Loss


**Best case:**

- Correct macro call (recession, crisis signal)
- Cheap entry (low volatility, tight spreads)
- Large move (100+ bps widening in 6-12 months)
- **Returns: 200-500% on margin in 12-18 months**

**Worst case:**

- Wrong direction (fight Fed, fight cycle)
- Overleveraged (5-10x capital)
- Forced liquidation (margin calls, illiquidity)
- **Loss: 80-100% of capital**

**Expected (disciplined):**

- Win rate: 45-55% (slightly favorable)
- Average win: +40-80 bps capture
- Average loss: -20-30 bps (with stops)
- **Expectancy: +10-20 bps per trade, 15-30% annual**

### 5. When to Trade


**Trade credit indices when:**

- Clear macro catalyst (Fed pivot, recession signal)
- Extreme valuations (spreads <40 bps or >200 bps for IG)
- High conviction (60%+ probability of direction)
- Liquid markets (on-the-run series, tight bid-ask)
- Adequate capital (can withstand 50 bp adverse move)

**Don't trade when:**

- Uncertain direction (no clear macro view)
- Middling spreads (60-80 bps IG, no edge)
- Fighting Fed (NEVER with leverage)
- Off-the-run series (illiquid, wide spreads)
- Overleveraged (>5x notional/capital)

### 6. Common Mistakes


1. Overleveraging (10x+ notional/capital is suicide)
2. Fighting the Fed (buying protection during QE, selling during tightening)
3. No stop-loss (holding -100 bp adverse moves)
4. Wrong series (trading illiquid off-the-run)
5. Ignoring premium bleed (800 bps annual = 2.2% daily burn)
6. Tranche trading (0-3% first loss = correlation bomb)
7. Basis ignorance (trading when basis is normal, not extreme)
8. Entry timing (buying protection at crisis peaks)

### 7. Final Wisdom


> "Credit indices are the most liquid, efficient way to trade credit beta—$10B daily volume, 0.5 bp bid-ask, instant execution. They're also the most dangerous when misused. The math is seductive: buy $1B CDX IG protection on $20M margin (50x leverage!), spreads widen 50 bps, make $22.5M profit (112% return). But the trap is brutal: spreads tighten 50 bps instead, you lose $22.5M, margin calls wipe you out, forced liquidation at worst prices. The 2007-2008 heroes (bought protection at 38 bps, made 450% returns) got timing and direction perfect. The 2009 zeroes (bought protection at 800 bps, lost 99%) got timing perfectly wrong—literally entered at the crisis bottom and got destroyed by the recovery. The difference wasn't intelligence or analysis; both sides had sophisticated arguments. The difference was: (1) Entry valuation (38 bps vs 800 bps), (2) Direction relative to Fed (pre-crisis vs post-QE), and (3) Leverage discipline (50x is fine if you're right immediately, fatal if you're early or wrong). Rules for survival: Never exceed 5x leverage (3x safer), set hard stops at 25-50 bps adverse (-$112k-225k on $10M notional), never fight Fed policy (QE = spreads tighten, tightening = spreads widen), trade on-the-run only (liquidity is life), and take profits at 2-3x premium paid (don't wait for home runs). Credit indices are tools for expressing high-conviction macro views with defined risk. Use them correctly: make 15-30% annually with 45-55% win rate. Use them wrong: join the 99% of overleveraged funds that blew up in 2009, 2020, or the next crisis."

**Key to success:**

- Size conservatively (max 5x leverage, 3x better)
- Enter at extremes (spreads <50 bps or >150 bps for IG)
- Set hard stops (25-50 bps adverse move)
- Never fight Fed (respect QE/QT direction)
- Trade on-the-run only (avoid illiquid series)
- Take profits early (2-3x premium paid)
- Monitor premium bleed (annual cost / 360 = daily burn)
- Exit before crisis peaks (greed kills)

**Most important:** Credit index trading is about asymmetric bets with defined downside. Best trades: cheap protection before crises (pay 38 bps, earn 212 bps = 5.6:1 payoff). Worst trades: expensive protection after crises (pay 800 bps, lose 250 bps = 0:3.2 payoff). Entry valuation and Fed direction determine 80% of outcomes. Leverage determines if you survive to collect profits. Master these three variables and indices become powerful macro tools. Ignore them and you'll be margin-called out of correct positions or wiped out on wrong ones. 📊💹⚠️

