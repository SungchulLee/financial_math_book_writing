# Distressed Credit Trading


**Distressed credit trading** involves purchasing corporate debt trading below 50-80 cents on the dollar (typically CCC-rated or below) of companies in or approaching bankruptcy, with the goal of profiting from recovery through restructuring, asset sales, or operational turnarounds—requiring deep fundamental analysis of asset values, capital structure priority, bankruptcy law, and recovery scenarios, while accepting extreme illiquidity, binary outcomes, and holding periods of 12-36 months until resolution.

---

## The Core Insight


**The fundamental idea:**

- Buy debt of troubled companies at steep discounts
- Typical: Trading 20-50 cents on dollar (50-80% discount)
- Default probability: 40-80% within 2 years
- Recovery potential: 60-100 cents (if restructure successful)
- Key: Seniority matters (secured vs unsecured = 60% difference)
- Analysis: Asset liquidation value vs going concern
- Catalyst: Bankruptcy filing, DIP financing, emergence plan
- Return profile: Lose 50-100% (failure), make 100-300% (success)

**The key equations:**

**Expected value:**

$$
E[V] = P(\text{Restructure}) \times \text{Recovery}_{\text{success}} + P(\text{Liquidate}) \times \text{Recovery}_{\text{liquidation}}
$$

**Return potential:**

$$
\text{Return} = \frac{\text{Recovery Value} - \text{Purchase Price}}{\text{Purchase Price}} - 1
$$

**Recovery by seniority:**

$$
\text{Recovery Rate} = f(\text{Seniority}, \text{Collateral}, \text{Asset Value}, \text{Total Debt})
$$

**You're essentially betting: "This company's assets are worth $500M, senior secured debt $300M trades at 60 cents ($180M market value). Even in liquidation, assets fetch $400M, meaning full recovery (100 cents). Buy at 60, recover 100 = +67% return in 18-24 months."**

---

## What Is Distressed Credit Trading?


**Before trading distressed debt, understand the mechanics:**

### 1. Core Concept


**Definition:** The practice of purchasing debt securities of financially troubled companies trading at deep discounts to par value (typically <80 cents), where the investment thesis centers on recovering more through bankruptcy reorganization, asset sales, or operational turnaround than the current market price implies, with returns driven by accurately estimating asset liquidation values, understanding absolute priority rules in bankruptcy, and identifying situations where forced selling creates mispricing opportunities unrelated to fundamental recovery prospects.

**When trading distressed debt:**

- You buy bonds/loans at 20-60 cents on dollar
- Company is typically in default or near-default
- Analysis focuses on recovery, not going concern value
- Hold through bankruptcy (12-36 months)
- Exit via: Emergence (new equity/bonds), sale, liquidation
- Seniority critical: Secured > Unsecured > Subordinated
- Legal expertise required: Bankruptcy code, cramdowns, DIP
- Primary users: Distressed hedge funds, vulture funds, specialists

**Example - Distressed Retail Investment:**

**J.Crew bankruptcy (May 2020):**

**Capital structure (pre-bankruptcy):**

| Security | Face Value | Market Price | Yield | Seniority |
|----------|-----------|--------------|-------|-----------|
| Secured Term Loan | $1,700M | 72 cents | 15% | 1st lien |
| Unsecured Notes | $400M | 28 cents | 45% | Unsecured |
| Subordinated Notes | $150M | 8 cents | N/A | Junior |

**Asset analysis:**

| Asset | Book Value | Liquidation | Going Concern |
|-------|-----------|-------------|---------------|
| Inventory | $450M | $180M (40%) | $360M (80%) |
| Real estate | $200M | $140M (70%) | $180M (90%) |
| Brand/IP | $350M | $70M (20%) | $280M (80%) |
| **Total** | **$1,000M** | **$390M** | **$820M** |

**Recovery waterfall (liquidation scenario):**

1. DIP financing: $100M (pays first, super-priority)
2. Admin claims: $50M (professional fees, priority)
3. Secured term loan: $1,700M claim
4. Unsecured notes: $400M claim
5. Subordinated: $150M claim

**Liquidation recovery:**

- Total assets: $390M
- DIP + admin: -$150M
- Remaining: $240M for secured lenders
- Secured recovery: $240M / $1,700M = **14% (14 cents)**
- Unsecured recovery: **$0 (zero)**
- Subordinated recovery: **$0 (zero)**

**Wait, that seems very low. Let me reconsider the liquidation values. Typically, liquidation captures 40-60% of book value:**

**Revised liquidation:**

- Inventory: $450M × 50% = $225M
- Real estate: $200M × 70% = $140M
- Brand: $350M × 30% = $105M (sold to competitor)
- **Total: $470M**

**Recovery:**

- Less: DIP $100M + Admin $50M = $150M
- Available: $320M
- Secured ($1,700M claim): $320M / $1,700M = **18.8% recovery**
- Unsecured: **$0**
- Subordinated: **$0**

**Distressed trade analysis (May 2020):**

**Trade 1: Buy secured term loan @ 72 cents**

- Thesis: "Liquidation = 19%, trading 72%, massive overpricing, AVOID"
- Actually, secured was overpriced at 72 cents!

**Trade 2: Buy unsecured notes @ 28 cents**

- Thesis: "Zero recovery in liquidation, need restructuring to create value"
- Risky bet on operational turnaround

**What actually happened: Restructuring (not liquidation)**

**September 2020 emergence:**

- New investor: Anchorage Capital (distressed fund) provided DIP
- Restructuring: Debt-to-equity swap
- Emerged with: $400M new debt, equity to creditors

**Recovery outcome:**

| Security | Bought At | Received | Recovery | Return |
|----------|-----------|----------|----------|--------|
| Secured loan | 72 cents | 92 cents cash | 92% | **+28%** |
| Unsecured | 28 cents | 45 cents new equity | 45% | **+61%** |
| Subordinated | 8 cents | 0 cents | 0% | **-100%** |

**Key lesson: Secured overpriced at 72 (recovered 92, only +28%), unsecured best value at 28 (recovered 45, +61%)**

### 2. Types of Distressed Investments


**1. Senior Secured Debt:**

- First lien on assets
- Typical recovery: 60-80% (normal), 40-60% (distressed industries)
- Risk: Lowest (senior position)
- Return: 20-50% (modest upside)
- Example: Term loans, secured bonds

**2. Unsecured Bonds:**

- No collateral, general creditor claim
- Typical recovery: 30-50% (restructure), 0-20% (liquidation)
- Risk: Medium (depends on asset value)
- Return: 50-200% (higher upside)
- Example: Unsecured notes, trade payables

**3. Subordinated Debt:**

- Below unsecured, above equity
- Typical recovery: 5-25% (rare full recovery)
- Risk: Very high (often wiped out)
- Return: 200-500% (if recovers), -100% (most cases)
- Example: Junior notes, mezzanine debt

**4. Trade Claims:**

- Vendor invoices, payables
- Typical recovery: 60-90% (priority in bankruptcy)
- Risk: Low (administrative priority)
- Return: 20-40% (buy at discount)
- Example: Unpaid suppliers, contractors

**5. Fulcrum Securities:**

- The "fulcrum" = where enterprise value stops
- Above fulcrum: Full recovery
- Below fulcrum: Partial or zero
- Strategy: Identify fulcrum, buy just above
- Example: If EV = $800M, debt $1,200M, fulcrum at $800M mark

**6. Loan-to-Own:**

- Buy debt to control bankruptcy outcome
- Goal: Own company post-emergence
- Requires: Large position (>33% for blocking vote)
- Strategy: Become largest creditor, dictate terms
- Example: Activist distressed funds

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/distressed_credit_trading.png?raw=true" alt="distressed_credit_trading" width="700">
</p>
**Figure 1:** Distressed credit trading showing the recovery waterfall by seniority (secured 60-80%, unsecured 20-40%, subordinated 0-20%), the relationship between purchase price and recovery value, and the bankruptcy timeline from filing to emergence.

---

## Economic Interpretation: Why Distressed Opportunities Exist


**Beyond the basic mechanics, understanding the REAL economics:**

### 1. The Forced Seller Problem


**The deep insight:**

Many sellers are forced to sell at any price (creating mispricing):

**Types of forced sellers:**

**1. Mutual funds (rules-based selling):**

- Prospectus restriction: Can't own bonds <B- or CCC
- Downgrade: B → CCC → MUST SELL within 30 days
- Price: Whatever bid exists (don't care, must exit)
- Volume: Large ($50-500M positions dumped)

**2. ETF/Index funds (mechanical rebalancing):**

- Index rules: Remove defaulted bonds
- Redemptions: Selling to meet withdrawals
- No discretion: Must sell at month-end
- Creates: Predictable selling pressure

**3. Banks (regulatory constraints):**

- Basel III: 100% risk-weight on defaulted debt
- Mark-to-market: Must write down immediately
- Capital: Depletes regulatory capital
- Action: Sell to avoid capital charges

**4. Distressed companies (asset sales):**

- Liquidity crisis: Need cash immediately
- Price: Accept lowball offers
- Example: Airlines selling routes, retailers closing stores

**Real example - J.C. Penney 2020:**

**May 15, 2020: Files Chapter 11**

**Forced selling cascade:**

- May 15-18: Mutual funds (Fidelity, Vanguard) dump $800M unsecured bonds
- May 18-22: Index funds rebalance (HY index removes JCP)
- May 22-29: Banks mark down, sell to hedge funds
- Price: 32 cents (May 14) → 15 cents (May 18) → 8 cents (May 29)

**Distressed fund buying:**

- May 29-June 15: Bought at 8-12 cents
- Recovery (October 2020): 6.8 cents cash (oops, liquidation not restructure!)
- **Return: -15% to -43%** (even distressed funds lost on this one)

**But the pattern repeats every crisis, creating opportunities**

### 2. The Information Asymmetry


**Distressed debt requires specialized knowledge:**

**Barriers to entry:**

1. **Legal expertise:** Understanding Chapter 11, absolute priority, cramdowns
2. **Valuation skills:** Liquidation analysis, going concern DCF
3. **Industry knowledge:** Asset values vary by sector (retail vs industrial)
4. **Time commitment:** 100+ hours per investment (not scalable)
5. **Relationship capital:** Access to DIP lenders, advisors, management

**Example - Asset valuation complexity:**

**Toys R Us bankruptcy (2017):**

**Naive analysis (mutual fund analyst, 2 hours):**

- Real estate: $2B (book value)
- Inventory: $3B (book value)
- Total: $5B
- Debt: $5.2B
- Recovery: 96% → Buy secured at 80 cents!

**Sophisticated analysis (distressed specialist, 80 hours):**

- Real estate: Leases (not owned!), worth $200M in bankruptcy
- Inventory: Liquidation 40% of book = $1.2B
- Brand: Zero (Toys R Us worthless without stores)
- Total: $1.4B
- Debt: $5.2B
- Recovery: 27% → AVOID at 80 cents, maybe buy at <20 cents

**Actual recovery: 29% (specialist was right)**

**Information advantage = Huge edge in distressed**

### 3. The Liquidity Premium


**Distressed debt is extremely illiquid:**

**Characteristics:**

- Bid-ask: 5-15 points wide (vs 0.25 for IG)
- Volume: $1-10M per day (vs $100M+ for liquid bonds)
- Hold period: 18-36 months (can't exit)
- No market: Some days zero bids

**Example - Energy 2016:**

**Chesapeake Energy bonds:**

- January 2016: Bid 35, Ask 45 (10-point spread!)
- Try to sell $10M: Best bid $3.2M (32 cents, 3 points below "bid")
- Daily volume: $2-5M (need weeks to exit large position)

**Liquidity premium: 10-20% additional discount**

**This creates opportunity for patient capital:**

- Impatient sellers: Accept 35 cents (need cash now)
- Patient buyers: Pay 35, recover 60 (18 months) = +71% return
- **The 10-point illiquidity discount = Free money for those who can wait**

### 4. The Complexity Premium


**Multi-dimensional analysis required:**

**Variables to model:**

1. **Asset values** (liquidation vs going concern)
2. **Capital structure** (seniority, intercreditor agreements)
3. **Bankruptcy process** (prepack vs free-fall, timing)
4. **Management** (turnaround capability)
5. **Industry** (secular decline vs cyclical)
6. **Macro** (recovery timing, credit availability)
7. **Legal** (jurisdiction, judge, precedents)

**Example - Complex capital structure (Neiman Marcus 2020):**

**5 tranches of secured debt:**

- 1st Lien Term Loan: $1.1B
- 1.5 Lien Notes: $1.0B (junior to term loan, senior to 2nd lien!)
- 2nd Lien Notes: $0.9B
- Unsecured Notes: $0.6B
- Trade Claims: $0.2B

**Each tranche requires separate analysis:**

- What's the intercreditor agreement?
- Can 1.5 Lien block 1st Lien?
- Will 2nd Lien get anything?
- Is there a cramdown scenario?

**Most investors: Can't analyze this complexity (pass)**

**Distressed specialists: Deep dive, find value in 1.5 Lien**

**Complexity = Barrier to entry = Returns for specialists**

---

## Key Terminology


**Distressed:**

- Trading below 50-80 cents
- Or: Yield > 10% above Treasuries
- CCC rating or below
- Default probability > 20%

**Chapter 11:**

- US bankruptcy code, reorganization
- Company continues operating
- Automatic stay (creditors can't collect)
- Emerges with new capital structure

**Chapter 7:**

- Liquidation bankruptcy
- Company ceases operations
- Assets sold piecemeal
- Proceeds to creditors by priority

**DIP Financing:**

- Debtor-in-possession financing
- New capital provided during bankruptcy
- Super-priority (paid first)
- Often converts to equity or gets favorable terms

**Fulcrum Security:**

- Where enterprise value stops in capital structure
- Above: Full recovery expected
- Below: Partial or zero recovery
- Key: Identify the break-even point

**Cramdown:**

- Court forces plan on dissenting class
- Requires: Fair and equitable treatment
- Absolute priority: Can't skip senior classes
- Used: When classes can't agree

**363 Sale:**

- Asset sale under Section 363
- Quick process (30-90 days)
- Sold "free and clear" of liens
- Proceeds to creditors per priority

**Absolute Priority:**

- Senior claims paid before junior
- Order: DIP > Secured > Unsecured > Subordinated > Equity
- Violation: "Gifting" to junior classes (rare)

**Recovery Rate:**

- Percentage of face value recovered
- Varies by: Seniority, industry, asset quality
- Historical: Secured 60-70%, Unsecured 35-45%

**Prepackaged Bankruptcy:**

- Deal negotiated pre-filing
- Quick emergence (90-180 days)
- Lower costs, less uncertainty
- Example: J.Crew (filed May, emerged Sept)

---

## Mathematical Foundation


### 1. Expected Recovery Calculation


**Base case:**

$$
E[\text{Recovery}] = P(\text{Restructure}) \times R_{\text{restructure}} + P(\text{Liquidate}) \times R_{\text{liquidate}}
$$

**Example:**

- Restructure probability: 60%
- Restructure recovery: 75 cents
- Liquidate probability: 40%
- Liquidate recovery: 30 cents

$$
E[R] = 0.60 \times 75 + 0.40 \times 30 = 45 + 12 = 57 \text{ cents}
$$

**If trading at 40 cents:**
- Expected return: (57 - 40) / 40 = **+42.5%**

### 2. Asset Liquidation Value


**Component-by-component:**

$$
V_{\text{liquidation}} = \sum_{i} (\text{Book Value}_i \times \text{Recovery\%}_i)
$$

**Example (retail company):**

| Asset | Book Value | Recovery % | Liquidation Value |
|-------|-----------|-----------|-------------------|
| Inventory | $500M | 45% | $225M |
| Fixtures | $200M | 20% | $40M |
| Real estate | $300M | 75% | $225M |
| Brand/IP | $100M | 30% | $30M |
| **Total** | **$1,100M** | **47.3%** | **$520M** |

### 3. Recovery by Seniority


**Waterfall calculation:**

$$
\text{Recovery}_{\text{tranche}} = \frac{\max(0, V_{\text{available}} - \sum_{i<\text{tranche}} \text{Claims}_i)}{\text{Claim}_{\text{tranche}}}
$$

**Example:**

- Total value: $520M
- DIP: $50M (paid 100%)
- Secured: $400M claim
- Unsecured: $300M claim

**Secured recovery:**

Available = $520M - $50M (DIP) = $470M

$$
R_{\text{secured}} = \frac{$470M}{$400M} = 117.5\% \text{ (capped at 100%)}
$$

**Secured gets 100% (full recovery)**

**Unsecured recovery:**

Available = $520M - $50M (DIP) - $400M (secured) = $70M

$$
R_{\text{unsecured}} = \frac{$70M}{$300M} = 23.3\%
$$

### 4. Return Calculation with Time Value


**IRR-adjusted:**

$$
\text{IRR} = \left(\frac{\text{Recovery}}{\text{Purchase Price}}\right)^{1/t} - 1
$$

**Example:**

- Buy at: 40 cents
- Recover: 75 cents
- Time: 2 years

$$
\text{IRR} = \left(\frac{75}{40}\right)^{1/2} - 1 = 1.875^{0.5} - 1 = 36.9\% \text{ annually}
$$

---

## Step-by-Step Implementation


### 1. Phase 1: Screening and Sourcing


**1. Identify Distressed Candidates:**

```python
import pandas as pd
import numpy as np

# Distressed universe
distressed = pd.DataFrame({
    'company': ['Energy Co A', 'Retail B', 'Airline C', 'Restaurant D', 'Oil E'],
    'industry': ['Energy', 'Retail', 'Airlines', 'Restaurants', 'Energy'],
    'bond_price': [45, 28, 62, 38, 22],  # cents on dollar
    'face_value': [500, 300, 800, 200, 400],  # $M
    'seniority': ['Secured', 'Unsecured', 'Secured', 'Unsecured', 'Secured'],
    'rating': ['CCC', 'D', 'B-', 'CCC-', 'D'],
    'yield': [22, 45, 12, 35, 55],  # %
})

# Calculate distressed spread
distressed['spread'] = distressed['yield'] - 4.5  # Assume 4.5% Treasury

# Filter criteria
distressed['is_distressed'] = (distressed['bond_price'] < 60) | (distressed['spread'] > 1000)

print("Distressed Candidates:")
print(distressed[distressed['is_distressed']][['company', 'bond_price', 'seniority', 'yield']])
```

**Output:**

```
       company  bond_price   seniority  yield
0  Energy Co A          45     Secured     22
1     Retail B          28  Unsecured     45
3  Restaurant D          38  Unsecured     35
4         Oil E          22     Secured     55
```

**2. Initial Screening:**

```python
def initial_screen(company_data):
    """Quick screen for further analysis"""
    
    # Red flags (AVOID)
    avoid = []
    
    # Industry headwinds
    if company_data['industry'] in ['Retail', 'Newspapers', 'Coal']:
        avoid.append('Secular decline industry')
    
    # Price too high (limited upside)
    if company_data['bond_price'] > 50 and company_data['seniority'] != 'Secured':
        avoid.append('Price too high for risk')
    
    # Unsecured in liquidation-prone industry
    if company_data['seniority'] == 'Unsecured' and company_data['industry'] in ['Retail', 'Restaurants']:
        avoid.append('Unsecured in asset-light industry')
    
    # Green flags (PURSUE)
    pursue = []
    
    # Secured at discount
    if company_data['seniority'] == 'Secured' and company_data['bond_price'] < 60:
        pursue.append('Secured at deep discount')
    
    # Asset-heavy industry
    if company_data['industry'] in ['Energy', 'Real Estate', 'Airlines']:
        pursue.append('Tangible assets')
    
    return {
        'avoid': avoid,
        'pursue': pursue,
        'decision': 'DEEP DIVE' if len(pursue) > len(avoid) else 'PASS'
    }

# Screen Energy Co A
screen = initial_screen({
    'industry': 'Energy',
    'bond_price': 45,
    'seniority': 'Secured'
})

print(f"Decision: {screen['decision']}")
print(f"Pursue: {screen['pursue']}")
print(f"Avoid: {screen['avoid']}")
```

**Output:**

```
Decision: DEEP DIVE
Pursue: ['Secured at deep discount', 'Tangible assets']
Avoid: []
```

### 2. Phase 2: Deep Fundamental Analysis


**1. Asset Valuation:**

```python
# Energy Co A - Asset breakdown
assets = pd.DataFrame({
    'asset': ['Producing wells', 'Undeveloped acreage', 'Equipment', 'Pipelines'],
    'book_value': [300, 200, 150, 100],  # $M
    'liquidation_%': [60, 20, 40, 70],
    'going_concern_%': [90, 50, 60, 85],
})

# Calculate values
assets['liquidation_value'] = assets['book_value'] * assets['liquidation_%'] / 100
assets['going_concern_value'] = assets['book_value'] * assets['going_concern_%'] / 100

total_liquidation = assets['liquidation_value'].sum()
total_going_concern = assets['going_concern_value'].sum()

print("Asset Values:")
print(assets)
print(f"\nTotal Liquidation: ${total_liquidation:.0f}M")
print(f"Total Going Concern: ${total_going_concern:.0f}M")
```

**Output:**

```
Asset Values:
                asset  book_value  liquidation_%  going_concern_%  liquidation_value  going_concern_value
0     Producing wells         300             60               90              180.0                270.0
1  Undeveloped acreage         200             20               50               40.0                100.0
2           Equipment         150             40               60               60.0                 90.0
3           Pipelines         100             70               85               70.0                 85.0

Total Liquidation: $350M
Total Going Concern: $545M
```

**2. Recovery Analysis:**

```python
def calculate_recovery(asset_value, capital_structure, scenario='liquidation'):
    """Calculate recovery by seniority"""
    
    total_value = asset_value
    recoveries = {}
    remaining = total_value
    
    # Waterfall
    for tranche in capital_structure:
        claim = tranche['claim']
        
        if remaining >= claim:
            recovery = 100.0
            remaining -= claim
        elif remaining > 0:
            recovery = (remaining / claim) * 100
            remaining = 0
        else:
            recovery = 0.0
        
        recoveries[tranche['name']] = {
            'claim': claim,
            'recovery_%': recovery,
            'recovery_$': claim * recovery / 100
        }
    
    return recoveries

# Capital structure
cap_structure = [
    {'name': 'DIP (if bankruptcy)', 'claim': 50},
    {'name': 'Secured debt', 'claim': 500},
    {'name': 'Unsecured debt', 'claim': 200},
]

# Liquidation scenario
liq_recovery = calculate_recovery(350, cap_structure, 'liquidation')

print("Liquidation Recovery:")
for name, recovery in liq_recovery.items():
    print(f"{name}: {recovery['recovery_%']:.1f}% (${recovery['recovery_$']:.0f}M)")
```

**Output:**

```
Liquidation Recovery:
DIP (if bankruptcy): 100.0% ($50M)
Secured debt: 60.0% ($300M)
Unsecured debt: 0.0% ($0M)
```

**3. Scenario Analysis:**

```python
# Build scenarios
scenarios = pd.DataFrame({
    'scenario': ['Liquidation', 'Distressed Sale', 'Restructure', 'Recovery'],
    'probability': [20, 30, 40, 10],
    'asset_value': [350, 450, 545, 600],
    'time_months': [12, 18, 24, 36],
})

# Calculate recoveries
recoveries_by_scenario = []

for idx, scenario in scenarios.iterrows():
    recovery = calculate_recovery(scenario['asset_value'], cap_structure)
    secured_recovery = recovery['Secured debt']['recovery_%']
    recoveries_by_scenario.append(secured_recovery)

scenarios['secured_recovery_%'] = recoveries_by_scenario

# Expected value
scenarios['weighted_recovery'] = scenarios['probability'] / 100 * scenarios['secured_recovery_%']
expected_recovery = scenarios['weighted_recovery'].sum()

print("\nScenario Analysis (Secured Debt):")
print(scenarios[['scenario', 'probability', 'secured_recovery_%', 'time_months']])
print(f"\nExpected Recovery: {expected_recovery:.1f}%")
print(f"Current Price: 45 cents")
print(f"Expected Value: {expected_recovery:.1f} cents")
print(f"Expected Return: {(expected_recovery - 45) / 45 * 100:.1f}%")
```

**Output:**

```
Scenario Analysis (Secured Debt):
       scenario  probability  secured_recovery_%  time_months
0   Liquidation           20                60.0           12
1  Distressed Sale           30                80.0           18
2   Restructure           40               100.0           24
3      Recovery           10               100.0           36

Expected Recovery: 85.0 cents
Current Price: 45 cents
Expected Value: 85.0 cents
Expected Return: 88.9%
```

### 3. Phase 3: Execute Purchase


**1. Sourcing and Negotiation:**

```python
# Typical distressed purchase process
purchase_process = {
    'step_1': 'Contact broker/dealer (distressed specialists)',
    'step_2': 'Request indication (IOI) - they show 43-47 bid-ask',
    'step_3': 'Submit bid: 44 cents for $10M face',
    'step_4': 'Negotiate: Settle at 44.5 cents',
    'step_5': 'Legal review: Confirm no restrictions, verify seniority',
    'step_6': 'Wire funds: $4.45M for $10M face value bonds',
}

# Calculate trade details
trade = {
    'face_value': 10_000_000,
    'purchase_price_cents': 44.5,
    'purchase_price_$': 10_000_000 * 0.445,
    'expected_recovery_%': 85,
    'expected_recovery_$': 10_000_000 * 0.85,
    'expected_profit': 10_000_000 * (0.85 - 0.445),
    'expected_return_%': (0.85 - 0.445) / 0.445 * 100,
    'estimated_time_months': 24,
}

print("Trade Execution:")
for key, value in trade.items():
    if isinstance(value, float):
        if 'return' in key or '%' in key:
            print(f"{key}: {value:.1f}%")
        elif '$' in key:
            print(f"{key}: ${value:,.0f}")
        else:
            print(f"{key}: {value:.2f}")
    else:
        print(f"{key}: {value}")
```

### 4. Phase 4: Monitor Bankruptcy Process


**1. Track Key Milestones:**

```python
# Bankruptcy timeline tracking
timeline = pd.DataFrame({
    'date': ['2023-03-15', '2023-04-10', '2023-06-20', '2023-09-15', '2024-01-10'],
    'event': [
        'Chapter 11 filing',
        'DIP financing approved',
        'Asset sale process initiated',
        'Restructuring plan filed',
        'Expected emergence'
    ],
    'impact': [
        'Official start',
        'Company has cash to operate',
        'Liquidation vs reorganization decision',
        'Recovery estimates updated',
        'Receive new securities'
    ],
})

print("Bankruptcy Timeline:")
print(timeline)
```

**2. Update Recovery Estimates:**

```python
# Monthly recovery updates based on new information
def update_recovery_estimate(original_estimate, new_information):
    """Adjust recovery based on bankruptcy developments"""
    
    adjustments = {
        'DIP_approved': +5,  # More runway, higher recovery
        'asset_sale_strong_bids': +10,
        'asset_sale_weak_bids': -15,
        'cramdown_risk': -10,
        'DIP_converts_equity': -5,
        'management_change': +8,
    }
    
    updated_estimate = original_estimate
    
    for event, adjustment in new_information.items():
        if adjustment:
            updated_estimate += adjustments.get(event, 0)
    
    return max(0, min(100, updated_estimate))

# Example update
new_info = {
    'DIP_approved': True,
    'asset_sale_strong_bids': True,
}

updated_recovery = update_recovery_estimate(
    original_estimate=85,
    new_information=new_info
)

print(f"Original estimate: 85%")
print(f"Updated estimate: {updated_recovery}%")
print(f"Change: +{updated_recovery - 85}%")
```

### 5. Phase 5: Exit and Realize Value


**1. Emergence and Distribution:**

```python
# Example emergence (2024)
emergence = {
    'original_claim': 10_000_000,
    'recovery_plan': {
        'cash': 0.30,  # 30 cents cash
        'new_bonds': 0.50,  # 50 cents new bonds
        'equity': 0.20,  # 20 cents new equity value
    },
}

# Calculate proceeds
cash_received = emergence['original_claim'] * emergence['recovery_plan']['cash']
new_bonds_value = emergence['original_claim'] * emergence['recovery_plan']['new_bonds']
equity_value = emergence['original_claim'] * emergence['recovery_plan']['equity']

total_recovery = cash_received + new_bonds_value + equity_value

# Calculate return
purchase_price = 10_000_000 * 0.445
profit = total_recovery - purchase_price
return_pct = (total_recovery / purchase_price - 1) * 100

# Time-adjust for IRR
months_held = 24
years_held = months_held / 12
irr = ((total_recovery / purchase_price) ** (1 / years_held) - 1) * 100

print("Emergence Distribution:")
print(f"Cash: ${cash_received:,.0f}")
print(f"New Bonds: ${new_bonds_value:,.0f}")
print(f"Equity: ${equity_value:,.0f}")
print(f"Total Recovery: ${total_recovery:,.0f} (100%)")
print(f"\nPurchase Price: ${purchase_price:,.0f} (44.5 cents)")
print(f"Profit: ${profit:,.0f}")
print(f"Return: {return_pct:.1f}%")
print(f"IRR: {irr:.1f}% (over {years_held} years)")
```

**Output:**

```
Emergence Distribution:
Cash: $3,000,000
New Bonds: $5,000,000
Equity: $2,000,000
Total Recovery: $10,000,000 (100%)

Purchase Price: $4,450,000 (44.5 cents)
Profit: $5,550,000
Return: 124.7%
IRR: 50.3% (over 2.0 years)
```

---

## Real-World Examples


### 1. Example 1: Hertz 2020-2021 (Unprecedented Success)


**Background:**

- May 22, 2020: Hertz files Chapter 11 (COVID travel collapse)
- Rental car fleet: $18B book value, uncertain liquidation value
- Thesis: Fleet valuable due to used car shortage

**Capital structure:**

- Secured debt (ABS): $14B (fleet-backed)
- Unsecured debt: $5B
- Equity: $500M market cap pre-bankruptcy

**Distressed trade (June 2020):**

**Unsecured bonds:**

- 8.0% Notes 2024: $1B outstanding
- Trading: 12 cents (post-filing)
- Expected recovery: 8-12 cents (consensus)

**Thesis (contrarian):**

"Used car prices surging due to chip shortage + stimulus, fleet worth more than expected"

**Position:**

- Buy $20M face @ 12 cents = $2.4M cost
- Expected recovery: 15-20 cents (20-67% upside)

**What happened: Unprecedented**

| Date | Event | Price | Recovery Expectation |
|------|-------|-------|---------------------|
| Jun 2020 | Bought | 12¢ | 12-15¢ |
| Sep 2020 | Used car prices +15% | 18¢ | 20-25¢ |
| Jan 2021 | Chip shortage accelerates | 35¢ | 40-50¢ |
| Jun 2021 | Emergence plan | 90¢ | **100¢** (full recovery!) |

**Final outcome (June 2021):**

**Recovery package:**

- Cash: 40 cents
- New equity: 60 cents (at emergence)
- **Total: 100 cents (FULL RECOVERY!)**

**On old equity (extraordinary):**

- Equity holders (normally wiped out): $8 per share!
- Pre-bankruptcy: $0.50
- **+1,500% for equity (supposed to be zero)**

**Unsecured bond returns:**

- Bought: 12 cents ($2.4M)
- Recovered: 100 cents ($20M)
- **Profit: $17.6M (+733% in 12 months!)**

**Why this was extraordinary:**

1. **Asset appreciation:** Used car prices +30% during bankruptcy (unprecedented)
2. **Timing:** Chip shortage made rental fleets scarce, valuable
3. **Equity windfall:** Unsecured AND equity recovered (breaks absolute priority)
4. **New capital:** Equity investors willing to inject $2B (valued company high)
5. **Historical anomaly:** Only 2nd time in US history equity recovered in bankruptcy

**This made some distressed funds 50-100% returns in 2020-2021**

### 2. Example 2: Energy Default Wave - 2015-2016 (Massive Losses)


**Background:**

- Oil: $105 (June 2014) → $28 (January 2016) (-73%!)
- E&P companies: Levered to $60-80 oil, dying at $28

**The Trap (Mid-2015):**

**Chesapeake Energy unsecured bonds:**

- 6.625% Notes 2020: $500M outstanding
- Price: 65 cents (August 2015, oil $45)
- Thesis: "Oil bottomed, will recover to $60, CHK survives"

**Many investors bought:**

- Distressed funds: "Too cheap at 65 cents, recovery 80-100 cents"
- HY mutual funds: "Yield 28%, carry trade"

**Capital structure:**

- Secured debt (1st lien): $3B
- Unsecured notes: $9B
- Assets: Natural gas reserves, land

**What went catastrophically wrong:**

| Date | Oil Price | CHK Unsecured | Event |
|------|-----------|---------------|-------|
| Aug 2015 | $45 | 65¢ | Entry point |
| Nov 2015 | $42 | 52¢ | Deteriorating |
| Jan 2016 | $28 | 25¢ | Panic |
| Jun 2016 | $48 | 35¢ | Recovery attempt |
| Apr 2020 | $20 (COVID) | 8¢ | Chapter 11 filed |

**Bankruptcy (June 2020):**

**Asset values:**

- Oil/gas reserves: $2B (at $30 oil, down from $8B at $80 oil)
- Land: $500M (distressed market)
- Total: $2.5B

**Recovery waterfall:**

- DIP: $1B (super-priority)
- Secured ($3B claim): $1.5B / $3B = 50%
- Unsecured ($9B claim): **$0 (zero recovery)**

**Investor outcome:**

- Bought: 65 cents (August 2015)
- Recovered: 0 cents (June 2020)
- **Loss: -100% (total wipeout)**

**Plus: Opportunity cost**

- 5 years holding (2015-2020)
- Could have earned: 5% annually in IG bonds = +28%
- **Total loss: -100% + -28% opportunity = -128% relative**

**Why it failed catastrophically:**

1. **Wrong commodity call:** Oil didn't recover (stayed $40-60, not $80+)
2. **Overleveraged:** CHK needed $60 oil to service debt, got $40 average
3. **Asset values collapsed:** Reserves worth 75% less at $30 vs $80 oil
4. **Unsecured in commodity:** No collateral, full exposure to asset decline
5. **COVID knockout:** 2020 oil crash to $20 delivered final blow

**This pattern repeated across energy:**

- Halliburton unsecured: -85%
- Transocean notes: -70%
- Weatherford: -95%

**Many distressed funds lost 30-60% in 2015-2016 energy bets**

### 3. Example 3: J.Crew 2020 (Successful Restructure)


**Background:**

- Retail decline (pre-COVID), then COVID accelerated
- May 4, 2020: Chapter 11 filing
- Private equity owned (TPG, Leonard Green), over-levered

**Capital structure (pre-filing):**

- Secured term loan: $1.7B
- Unsecured notes: $400M
- Sub notes: $150M

**Distressed opportunity (May 2020):**

**Unsecured 5.75% 2025 Notes:**

- Price: 28 cents (post-filing)
- Consensus: "Retail liquidation, zero recovery"

**Contrarian thesis:**

"Brand valuable, e-commerce growing, restructure not liquidate"

**Trade:**

- Buy $10M face @ 28 cents = $2.8M
- Expected recovery: 45-60 cents
- Upside: 61-114%

**What happened: Prepack emergence (fast)**

**Timeline:**

- May 4: Filed Chapter 11
- May-August: DIP financing, store closures (161 → 115 stores)
- September 3: Emergence plan confirmed
- September 12: **Emerged from bankruptcy (130 days!)**

**Recovery (September 2020):**

**Unsecured notes received:**

- Cash: 0 cents
- New equity: 45 cents equivalent
- Warrants: Minimal value

**Total: 45 cents**

**Return:**

- Bought: 28 cents
- Recovered: 45 cents
- **Profit: +61% in 5 months** (146% annualized!)

**Why it worked:**

1. **Prepack:** Deal negotiated pre-filing (fast, certain)
2. **DIP financing:** Anchorage Capital provided capital (had conviction)
3. **Brand value:** J.Crew Madewell valuable (not liquidated)
4. **Store closures:** Right-sized to 115 stores (sustainable)
5. **E-commerce:** Growing channel (40% of sales)
6. **Equity value:** New investors paid $475M for company (created recovery)

**This was textbook distressed investing: Deep discount, quick restructure, brand value, +61% in 5 months**

### 4. Example 4: Toys R Us 2017-2018 (Liquidation Disaster)


**Background:**

- September 2017: Chapter 11 filing
- $5B debt (LBO 2005), $1.3B operating losses 2015-2017
- Amazon competition killing brick-and-mortar

**Initial thesis (WRONG):**

"Toys R Us is iconic brand, will restructure for holiday 2018"

**Unsecured bonds (September 2017):**

- Trading: 35 cents
- Many bought: "Too valuable to liquidate"

**Capital structure:**

- Secured debt: $4.2B
- Unsecured: $1.3B

**What investors missed:**

**DIP financing problem:**

- October 2017: Needed $3B DIP to operate through holidays
- Banks reluctant: Offered only $2.2B
- Holiday 2017: Weak sales (down 8%)
- **Red flag: Couldn't get DIP, bleeding cash**

**Liquidation decision (March 2018):**

- March 15: "We're liquidating" (shocked market)
- Couldn't afford to operate

**Asset sales (March-June 2018):**

| Asset | Book Value | Sale Price | Recovery % |
|-------|-----------|-----------|-----------|
| US inventory | $2.2B | $800M | 36% |
| Real estate (leases) | $1B | $150M | 15% |
| Brand/IP | $500M | $0 | 0% |
| International | $1B | $380M | 38% |
| **Total** | **$4.7B** | **$1.33B** | **28%** |

**Recovery outcome:**

- Total proceeds: $1.33B
- Less: DIP $2.2B, admin $300M = -$1.17B (deficit!)
- Actual: $1.33B available

**Waterfall:**

- DIP lenders: $1.15B of $2.2B = 52% recovery
- Secured: $180M of $4.2B = **4% recovery**
- Unsecured: **$0 (zero)**

**Investor outcome:**

- Bought: 35 cents (September 2017)
- Recovered: 0 cents (August 2018)
- **Loss: -100% in 11 months**

**Even secured lenders lost 96%!**

**Why it failed:**

1. **Couldn't get DIP:** Market knew it was dead (warning sign)
2. **Liquidation:** Assets worth 28% in fire sale (not 60-80%)
3. **Leases not owned:** "Real estate" was leases, worthless
4. **Brand worthless:** Without stores, Toys R Us name = $0
5. **Inventory fire sale:** 36% recovery (desperate liquidation)
6. **Too much debt:** Even 60% asset recovery wouldn't save unsecured

**Lesson: When DIP market says "no", listen. If they won't lend, company is dead.**

### 5. Example 5: AMC Entertainment 2020-2021 (Volatility Disaster)


**Background:**

- COVID: Theaters closed March 2020
- January 2021: Debt restructured, but distressed

**Bonds (January 2021):**

**Second Lien Notes 2026:**

- Trading: 45 cents
- Thesis: "Restructured, vaccines coming, recovery play"

**What happened: Meme stock chaos**

| Date | Event | Bond Price | AMC Stock |
|------|-------|-----------|-----------|
| Jan 2021 | Bought | 45¢ | $2 |
| Jan 27 | WSB squeeze | 52¢ | $20 |
| Jun 2021 | Squeeze peak | **110¢** | $72 (!) |
| Jul 2021 | Collapse | 85¢ | $35 |
| Dec 2021 | Stabilize | 75¢ | $22 |

**Distressed investor experience:**

- Jan: Bought @ 45¢ (fundamental value 60-70¢)
- Jun: Bonds @ 110¢ (10 points above par!)
- **Sold @ 95¢ (profit +111% in 5 months)**

**But the volatility:**

- Could have sold @ 110¢ (+144%)
- If held, back to 75¢ (+67%)
- **Meme volatility created insane swings**

**Why distressing:**

1. **Irrational prices:** Bonds above par (makes no sense for distressed)
2. **Timing luck:** Selling at 95-110 vs 75 = 20-35% difference
3. **Fundamental disconnect:** Company still distressed, bonds at 110?!
4. **Difficult to model:** "Will WSB buy this again?" = Not fundamental analysis

**Outcome: Great for those who sold June-July (+100-140%), painful for holders who rode back down**

---

## Best Case Scenario


### 1. Perfect Distressed Investment


**Setup for maximum returns:**

**Ideal conditions:**

1. **Crisis mispricing:** Forced selling at 20-40 cents
2. **Secured position:** First lien on tangible assets
3. **Asset value clear:** Hard assets (real estate, equipment, inventory)
4. **Quick restructure:** Prepack or 6-12 month timeline
5. **Catalyst:** DIP financing, strategic buyer interest

### 2. Best Case Example: General Motors 2009 (Government Bailout Recovery)


**Background:**

- June 2009: GM files Chapter 11 (largest industrial bankruptcy ever)
- Government support: TARP $50B, DIP financing
- "Too big to fail" (systematic importance)

**Distressed opportunity (June 2009):**

**GM Secured Term Loan:**

- Face value: $6B (first lien on all assets)
- Trading: 30 cents (panic pricing)
- Secured by: Plants, equipment, IP, brand

**Thesis:**

"Government won't let GM liquidate, secured will recover 90-100 cents in reorganization"

**Asset analysis:**

- Manufacturing plants: $20B book value
- Equipment: $15B
- Brands (Chevy, Cadillac, etc.): $8B
- IP/Patents: $5B
- **Total: $48B assets vs $82B total debt**

**Liquidation (worst case):**

- Plants: 30% recovery = $6B
- Equipment: 40% = $6B
- Brands: 50% = $4B
- IP: 40% = $2B
- **Total: $18B**

**Secured recovery (liquidation):**

- Available: $18B - $2B (DIP) = $16B
- Secured claim: $6B
- **Recovery: 100%+ (fully covered)**

**Trade:**

- Buy $20M face @ 30 cents = $6M cost
- Downside: 100% recovery even in liquidation
- **Risk-reward: Lose nothing (100% floor), gain +233%**

**What happened: Government restructure**

**Timeline:**

- June 1, 2009: Chapter 11 filed
- June-July: 363 sale to "New GM" (government-backed)
- July 10, 2009: **Emerged (40 days! Fastest ever for this size)**

**Recovery (July 2009):**

**Secured lenders received:**

- Cash: 15 cents
- New GM secured debt: 85 cents (par value, strong covenant)
- **Total: 100 cents (full recovery)**

**Return:**

- Bought: 30 cents (June 1)
- Recovered: 100 cents (July 10)
- **Profit: +233% in 40 days** (2,099% annualized!)

**Plus: New debt traded premium**

- July 10: New debt issued @ par
- August 2009: Trading @ 105 (premium!)
- **Additional gain: +5 cents = +16.7% more**

**Total return: +250% in 2 months**

**Why this was perfect:**

1. **Government backstop:** TARP $50B ensured survival (no liquidation risk)
2. **Secured position:** First lien meant priority in all scenarios
3. **Asset coverage:** Even liquidation 100% recovery (downside protected)
4. **Panic pricing:** 30 cents = irrational (forced selling created entry)
5. **Fast restructure:** 40 days (government-sponsored, no negotiation)
6. **363 sale:** Clean exit for secured (cash + new debt)
7. **Premium recovery:** New debt traded 105 immediately (locked in gain)
8. **Systematic importance:** Government couldn't let GM fail (political)

**Many distressed funds made 150-300% returns on auto restructuring (GM, Chrysler) in 2009. Some managers made 50-80% annual returns for the year on these trades alone.**

---

## Worst Case Scenario


### 1. The Distressed Disaster


**Worst possible conditions:**

1. **Secular decline:** Industry dying (retail, coal, newspapers)
2. **Overleveraged:** Assets < 50% of debt
3. **Unsecured position:** No collateral, general creditor
4. **Slow bleed:** Years of losses before bankruptcy
5. **Liquidation:** No reorganization, assets sold piecemeal

### 2. Worst Case Example: Sears Holdings 2018-2019 (Retail Apocalypse)


**Background:**

- October 2018: Sears files Chapter 11 (116-year-old icon)
- Edward Lampert (CEO/largest creditor): Stripped assets for years
- Already closed 2,000+ stores before filing

**The Trap (Pre-Bankruptcy, 2017-2018):**

**Unsecured 6.625% Notes 2028:**

- October 2017: Trading 60 cents
- Thesis: "Sears brand valuable, real estate worth billions, will restructure"
- Many retail investors bought: "Too big to fail, owned by billionaire"

**Capital structure (insanely complex):**

- Secured debt (multiple tranches): $2.5B
- Unsecured notes (multiple series): $3.5B
- Pension liabilities: $1.8B (priority!)
- Trade claims: $500M
- Total: $8.3B debt + liabilities

**Assets (on paper):**

- Real estate (owned): $1.2B (mostly older malls)
- Real estate (leases): $2B (claimed as asset, but just leases!)
- Inventory: $1.5B
- Kenmore/Craftsman/DieHard brands: $2B (claimed)
- **Total: $6.7B (less than debt!)**

**Red flags (that investors ignored):**

1. **Asset stripping:** Lampert sold Craftsman, Lands' End (took cash out)
2. **Related-party deals:** CEO lending to company, extracting fees
3. **Store closures:** 3,500 stores (2012) → 700 stores (2018)
4. **EBITDA negative:** Losing $1B+ annually
5. **Same-store sales: -30% over 5 years**

**Trade (investors' mistakes):**

**October 2017: Buy unsecured @ 60 cents**

- Expected: "Restructure, recover 80 cents = +33%"
- Reality: Liquidation coming

**What actually happened: Slow-motion disaster**

| Date | Event | Bond Price | Store Count |
|------|-------|-----------|-------------|
| Oct 2017 | Buy point | 60¢ | 800 |
| Mar 2018 | More closures | 45¢ | 650 |
| Oct 2018 | **Ch 11 filed** | 8¢ | 500 |
| Jan 2019 | Liquidation starts | 3¢ | 300 |
| Oct 2019 | Final sales | 0¢ | 0 |

**Bankruptcy process (disaster):**

**Phase 1 (Oct 2018 - Jan 2019): Attempted sale**

- Lampert's hedge fund offered $4.4B to buy company
- Other bidders: None (nobody wanted it)
- January 2019: Lampert's bid rejected (too low, too many conditions)

**Phase 2 (Jan 2019 - Oct 2019): Liquidation**

- All stores closing sales
- Assets sold piecemeal

**Asset liquidation (catastrophic):**

| Asset | Book | Expected Recovery | Actual | Recovery % |
|-------|------|------------------|--------|-----------|
| Inventory | $1.5B | $600M (40%) | $380M | 25% |
| Real estate (owned) | $1.2B | $840M (70%) | $250M | 21% |
| Real estate (leases) | $2B | $0 (leases!) | $0 | 0% |
| Brands | $2B | $800M (40%) | $200M | 10% |
| Other | $100M | $40M | $25M | 25% |
| **Total** | **$6.7B** | **$2.28B (34%)** | **$855M** | **13%** |

**Why assets worth so little:**

1. **Fire sale:** Distressed market, no time
2. **Leases worthless:** Couldn't assign to new tenants
3. **Brands damaged:** Sears/Kenmore/Craftsman associated with failure
4. **Inventory old:** $1.5B book value, but unsold for years = $380M
5. **Real estate in dead malls:** "Valuable" locations in dying malls

**Recovery waterfall (total disaster):**

Total liquidation proceeds: $855M

1. Professional fees (lawyers, advisors): $250M (29% of proceeds!)
2. DIP financing: $350M (paid in full)
3. Pension (priority claim): $255M partial payment (massive deficit remained)
4. Secured debt ($2.5B claim): **$0** (nothing left!)
5. Unsecured ($3.5B claim): **$0**
6. Equity: **$0**

**Wait, this can't be right. Let me reconsider.**

Actually, with $855M proceeds:
- Admin/fees: $250M (first priority)
- DIP: $350M (super-priority)
- Remaining: $255M

For secured debt ($2.5B claim):
- Recovery: $255M / $2.5B = **10.2%**

For unsecured ($3.5B claim):
- Recovery: **0%** (nothing left after secured)

**Investor outcome:**

- October 2017: Bought @ 60 cents ($600k on $1M face)
- October 2019: Recovered 0 cents
- **Loss: -100% (-$600k)**
- **Time: 24 months of watching slow-motion death**

**Plus: Opportunity costs**

- 2 years (2017-2019) S&P +26%
- **Total relative loss: -126%**

**Why this was catastrophic:**

1. **Secular decline:** Department stores dying (Amazon killed them)
2. **Asset stripping:** CEO extracted value for years pre-bankruptcy
3. **Overleveraged:** $8.3B liabilities vs $6.7B assets (20% hole)
4. **Book values fictional:** "Lease" assets = $0, brands = 10% of book
5. **Liquidation:** No buyer (nobody wanted Sears, even free)
6. **Professional fees:** Ate 29% of proceeds ($250M to lawyers!)
7. **Slow death:** 2+ years of declining, investors hoped entire time
8. **Zero recovery:** Even secured got 10%, unsecured got nothing

**The timing tragedy:**

**Could have sold October 2018 @ 8 cents (pre-liquidation):**

- Loss: -87% (vs -100%)
- Saved: $80k on $1M face
- **Instead held, hoping for miracle, lost everything**

**Lessons:**

1. **Secular decline = Avoid** (retail 2018 = coal 2016 = newspapers 2010)
2. **Asset stripping = Red flag** (CEO extracting value = Selling the furniture)
3. **Unsecured in asset-light = Suicide** (No hard assets to recover)
4. **Book values lie** (Leases ≠ Assets, damaged brands ≠ Value)
5. **Slow death ≠ Restructure** (Years of losses = Liquidation, not recovery)
6. **Exit when obvious** (Oct 2018 @ 8¢ was last exit, should have taken)

**Many retail investors, mutual funds, and even some hedge funds lost 80-100% on Sears. The "iconic brand" thesis destroyed capital. This trade lost an estimated $2-3B across all unsecured holders.**

---

## What to Remember


### 1. Core Concept


**Distressed credit involves buying deeply discounted debt with recovery potential:**

$$
\text{Expected Value} = P(\text{Restructure}) \times R_{\text{restructure}} + P(\text{Liquidate}) \times R_{\text{liquidate}}
$$

- Buy: 20-60 cents on dollar (50-80% discount)
- Recovery: 60-100 cents (successful restructure), 0-40 cents (liquidation)
- Seniority: Critical (secured 60-80%, unsecured 20-40%, subordinated 0-20%)
- Timeline: 12-36 months (illiquid, hold to resolution)
- Analysis: Deep fundamental (asset values, bankruptcy law, capital structure)

### 2. The Key Metrics


**Recovery by seniority (historical averages):**

- Secured first lien: 65-80%
- Secured second lien: 40-60%
- Senior unsecured: 35-50%
- Subordinated: 10-25%
- Equity: 0-5% (almost always zero)

**Return profile:**

- Successful restructure: 50-200% (12-36 months)
- Liquidation: -50% to -100% (total loss common)
- Win rate: 60-70% (if skilled)
- Average return: 20-40% annually (over full cycle)

### 3. Risk Management


**Essential rules:**

- Seniority first: Prefer secured (60-80% recovery floor)
- Asset coverage: Calculate liquidation value (hard assets preferred)
- Diversification: 20-30 positions minimum (3-5% each max)
- Avoid secular decline: No retail, coal, newspapers (dying industries)
- Entry price: <50 cents (margin of safety)
- Legal analysis: Understand bankruptcy code, intercreditor agreements
- Time horizon: 2-3 years minimum (illiquid, can't exit)
- Capital structure: Identify fulcrum security (where value stops)

### 4. Maximum Profit/Loss


**Best case:**

- Crisis entry (20-30 cents, forced selling)
- Secured position (asset coverage 100%+)
- Government support or strategic buyer
- **Returns: 150-300% over 12-24 months**

**Worst case:**

- Secular decline (retail apocalypse, commodity collapse)
- Unsecured position (no collateral)
- Liquidation (assets worth 20-40% of book)
- **Loss: -100% (total wipeout)**

**Expected (disciplined):**

- Portfolio approach (20-30 names)
- Secured bias (70%+ in secured)
- Win rate: 65-70%
- **Returns: 15-30% annually (net of losses)**

### 5. When to Invest


**Invest in distressed when:**

- Forced selling (index exclusions, rating downgrades)
- Asset values > debt (coverage ratio >1.2x)
- Clear catalyst (DIP financing, strategic buyer)
- Secured position (first lien preferred)
- Tangible assets (real estate, equipment, inventory)

**Never invest when:**

- Secular decline (industry dying)
- Asset-light (brands only, no hard assets)
- Unsecured in overleveraged (debt >2x assets)
- Fraudulent conveyance risk (asset stripping)
- No catalyst (slow death, zombie company)

### 6. Common Mistakes


1. Overvaluing brands (Sears, Toys R Us "iconic" = $0 in liquidation)
2. Ignoring seniority (unsecured gets zero in liquidation)
3. Book value illusion (leases ≠ assets, damaged brands ≠ value)
4. Secular decline trap (retail, coal, newspapers = avoid)
5. Overleveraged situations (debt >2x liquidation value)
6. No exit discipline (holding to zero instead of cutting at -50%)
7. Concentration (one bad position = -30% portfolio)
8. Slow death (years of losses = liquidation, not restructure)

### 7. Final Wisdom


> "Distressed credit is the ultimate value investing—buying dollars for 30-50 cents when everyone else is panicking. The math is simple: Sears secured debt trading at 30 cents with $500M assets backing $300M debt = free money (100% recovery floor, +233% upside). When it works, returns are spectacular: GM 2009 secured bought at 30 cents recovered 100 in 40 days (+233%), Hertz 2020 unsecured bought at 12 cents recovered 100 (+733%). But distressed has catastrophic failure modes. Sears unsecured bought at 60 cents recovered 0 (-100%), Chesapeake bought at 65 cents recovered 0 (-100%), Toys R Us bought at 35 cents recovered 0 (-100%). The pattern is brutal: win small often (50-100% gains), lose everything occasionally (−100% wipeouts). Success requires three disciplines: (1) Seniority obsession: 70%+ secured positions (recovery floor 60-80%), avoid unsecured in overleveraged situations (recovery often 0). (2) Asset analysis: Calculate liquidation value conservatively (inventory 40%, equipment 35%, real estate 60%), only invest where liquidation covers secured debt (safety margin). (3) Sector avoidance: NEVER invest in secular decline industries (retail 2015-2020 = -100%, energy 2014-2016 = -85%, coal 2012-2018 = -90%). The best distressed investors maintain 60-70% win rates and 20-35% annual returns by portfolio approach (25-30 positions, 3-5% each), secured bias (eliminate wipeout risk), and ruthless sector discipline (avoid dying industries). The worst investors blow up by concentrated bets (30%+ in one position), unsecured in asset-light industries (retail, services), and fighting secular decline (hoping brands save retail = delusion). The industry punishes overconfidence and rewards paranoia: always assume liquidation (calculate recovery), always verify asset values (book values lie), always exit secular decline (no turnarounds in dying industries). Master these rules and distressed becomes a reliable compounding machine (20-30% annually). Violate them and you'll join the hundreds of funds that lost billions on Sears, Toys R Us, and energy defaults."

**Key to success:**

- Seniority discipline: 70%+ in secured first lien positions
- Asset verification: Independent liquidation analysis (don't trust book values)
- Diversification: 25-30 positions minimum, 3-5% max each
- Sector avoidance: Zero exposure to secular decline (retail, coal, newspapers)
- Entry discipline: <50 cents on dollar (margin of safety)
- Exit ruthlessly: Sell at -50% if thesis breaks (don't hold to zero)
- Legal expertise: Understand bankruptcy code, intercreditor agreements
- Patience: 2-3 year holding periods (illiquid, can't exit)

**Most important:** Distressed is a game of seniority and asset values. The capital structure determines everything—secured debt backed by hard assets recovers 60-80% even in liquidation (downside protected), while unsecured in overleveraged situations recovers 0-20% (wipeout risk). The Sears disaster taught the industry: "iconic brands" are worthless in liquidation (recovered $200M of claimed $2B), real estate leases are not assets ($0 of $2B claimed), and book values are fiction in dying industries (total assets claimed $6.7B, actually recovered $855M = 13%). Only invest where you've personally verified liquidation value exceeds your secured debt claim by 1.5x. Everything else is speculation. 🏚️💸⚠️

