# Repo and Securities Lending


**Repo and securities lending** are short-term financing mechanisms where securities are used as collateral to borrow cash (repo) or lent to others for a fee (securities lending), forming the backbone of modern financial market liquidity.

---

## The Core Insight


**The fundamental idea:**

- Institutions need short-term financing
- Securities can be collateral for cash loans
- Repo = Sell security today, buy back tomorrow (with interest)
- Securities lending = Lend security, get fee and collateral
- Critical for leverage, short selling, and market liquidity
- Rate reflects credit risk and security scarcity

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/repo_mechanics.png?raw=true" alt="repo_mechanics" width="700">
</p>
**Figure 1:** Repo transaction mechanics showing the initial sale of securities for cash and the subsequent repurchase at a higher price, with the difference representing the repo rate (cost of borrowing).

**You're essentially asking: "How do financial institutions fund their positions and what role does collateral play?"**

---

## What Is Repo?


### 1. Basic Definition


**Repurchase agreement (repo):**

A transaction where:
- Party A sells securities to Party B for cash
- Party A agrees to repurchase securities from Party B later
- Repurchase price > Sale price (difference = interest)

**Mathematical structure:**

$$
\text{Repurchase Price} = \text{Sale Price} \times \left(1 + r_{\text{repo}} \times \frac{t}{360}\right)
$$

Where:
- $r_{\text{repo}}$ = Repo rate (annualized)
- $t$ = Days until repurchase
- $360$ = Day count convention

**Example:**
- Sell $\$10M$ bonds today
- Repo rate: 2% annually
- Term: 1 day (overnight)

**Repurchase price tomorrow:**

$$
\$10M \times \left(1 + 0.02 \times \frac{1}{360}\right) = \$10,000,556
$$

**Cost: $\$556$ for one day of financing**

### 2. Economic Substance


**What repo really is:**

**Collateralized loan:**
- Cash borrower posts securities as collateral
- If borrower defaults, lender keeps securities
- Very safe (overcollateralized typically)

**Not a true sale:**
- Accounting: Treated as secured financing
- Legal: Repo has special treatment in bankruptcy
- Economic: Temporary transfer with repurchase obligation

**Key insight:**

$$
\text{Repo} = \text{Secured Loan} + \text{Securities Collateral}
$$

### 3. Participants


**Cash lenders (reverse repo):**
- Money market funds (cash-rich)
- Corporates (excess cash)
- Central banks (monetary policy operations)
- Conservative investors (seeking safe returns)

**Cash borrowers (repo):**
- Broker-dealers (funding inventory)
- Hedge funds (leveraging positions)
- Banks (short-term liquidity)
- Market makers (financing securities holdings)

**Why they transact:**
- Lender: Safe return on cash (better than deposits)
- Borrower: Cheap financing (secured rate < unsecured)

### 4. Types of Repo


**Overnight repo:**
- 1-day term
- Most common (~70% of market)
- Rate: SOFR + spread
- Rolls daily (if needed)

**Term repo:**
- Fixed maturity (1 week to 1 year)
- Less common
- Rate: Forward rate + premium
- No daily rollover

**Open repo:**
- No fixed maturity
- Either party can terminate
- Rolls indefinitely
- Rate resets daily

**Tri-party repo:**
- Third party (custodian) manages collateral
- Automated settlement
- Reduces operational risk
- Common for large volumes

### 5. Haircut (Margin)


**Overcollateralization:**

$$
\text{Haircut} = \frac{\text{Collateral Value} - \text{Cash Loan}}{\text{Collateral Value}}
$$

**Example:**
- Post $\$105M$ bonds as collateral
- Receive $\$100M$ cash
- Haircut: $(105 - 100)/105 = 4.76\%$

**Why haircuts exist:**
- Protect lender from collateral price decline
- Higher for riskier/volatile securities
- Lower for Treasuries (~2%), higher for equities (~10-20%)

**Typical haircuts:**
- US Treasuries: 2-5%
- Investment-grade bonds: 5-10%
- High-yield bonds: 15-25%
- Equities: 10-30%
- Emerging market: 20-50%

### 6. Repo Rate Drivers


**Factors affecting repo rates:**

**General Collateral (GC) rate:**
- Typical Treasury repo rate
- Close to risk-free rate (SOFR)
- Reflects supply/demand for cash

**Special collateral rate:**
- Specific security in high demand
- Rate lower than GC (can be negative!)
- Reflects scarcity of that security

**Credit risk:**
- Counterparty quality
- Higher risk → Higher rate
- Mitigated by collateral

**Term premium:**
- Longer term → Higher rate
- Reflects rollover risk
- Typically 10-20 bps per month

### 7. Special vs General Collateral


**General Collateral (GC):**
- Any Treasury security acceptable
- Driven by funding needs
- Rate reflects cash supply/demand
- Typical: SOFR + 5-10 bps

**Special Collateral:**
- Specific security required
- Driven by short-selling demand
- Rate below GC (sometimes negative!)
- Can be 50-200 bps below GC

**Example:**
- GC rate: 2.5%
- On-the-run 10Y Treasury: 1.0% (special!)
- Traders willing to pay premium to borrow scarce security

**Specialness:**

$$
\text{Specialness} = \text{GC Rate} - \text{Special Rate}
$$

**Higher specialness = More valuable to lend**

---

## What Is Securities Lending?


### 1. Basic Definition


**Securities lending:**

A transaction where:
- Lender transfers securities to borrower
- Borrower posts collateral (cash or securities)
- Borrower pays lending fee
- Borrower returns securities later

**Key difference from repo:**
- Focus: Borrowing securities (not cash)
- Borrower typically wants to short sell
- Lender earns fee (not repo interest)

### 2. Economic Purpose


**Why lend securities:**

**For lenders:**
- Earn additional yield on holdings
- Enhance portfolio returns (10-50 bps annually)
- Minimal risk (overcollateralized)

**For borrowers:**
- Short selling (borrow to sell, buy back cheaper)
- Cover fails (settlement obligations)
- Market making (fulfill delivery obligations)
- Tax strategies (dividend arbitrage)

### 3. Lending Fee Structure


**Fee calculation:**

$$
\text{Lending Fee} = \text{Security Value} \times \text{Fee Rate} \times \frac{t}{360}
$$

**Example:**
- Lend $\$10M$ stock
- Fee rate: 1% annually (100 bps)
- Term: 30 days

**Fee earned:**

$$
\$10M \times 0.01 \times \frac{30}{360} = \$8,333
$$

**Typical fee rates:**
- Easy-to-borrow (ETB): 10-50 bps
- General collateral level: 25-100 bps
- Hard-to-borrow (HTB): 100-500 bps
- Specials: 500-2,000 bps (5-20%!)

### 4. Collateral Types


**Cash collateral:**
- Borrower posts cash (102-105% of security value)
- Lender invests cash, earns interest
- Lender rebates most interest to borrower
- Net fee = Lending fee + Rebate spread

**Securities collateral:**
- Borrower posts other securities
- No cash reinvestment needed
- Direct fee payment
- Preferred by some lenders (no reinvestment risk)

### 5. Fee Split (Agency Lending)


**Agent lender model:**

Large asset owners (pension funds, mutual funds) don't lend directly:
- Agent (custodian bank) manages lending
- Agent finds borrowers, handles operations
- Fee split between owner and agent

**Typical split:**
- Lender (asset owner): 60-80% of fee
- Agent (custodian): 20-40% of fee

**Example:**
- Gross lending fee: $\$100,000$
- Lender receives: $\$70,000$ (70% split)
- Agent receives: $\$30,000$ (30% split)

### 6. Short Interest and Utilization


**Utilization rate:**

$$
\text{Utilization} = \frac{\text{Shares on Loan}}{\text{Shares Available to Lend}}
$$

**Example:**
- Total lendable shares: 100M
- Shares on loan: 40M
- **Utilization: 40%**

**Relationship to fee:**
- Low utilization (< 20%): Low fee (ETB)
- Medium utilization (20-60%): Moderate fee
- High utilization (> 80%): High fee (HTB)
- Utilization > 100%: Impossible (can't lend what you don't have)

**Short interest:**
- Total shares sold short in market
- High short interest → High lending fees
- Indicator of bearish sentiment

### 7. Risks in Securities Lending


**Counterparty risk:**
- Borrower defaults, doesn't return securities
- Mitigated by: Overcollateralization

**Collateral reinvestment risk:**
- Cash collateral invested, loses value
- 2008 crisis: Lehman cash collateral investments failed
- Mitigated by: Conservative reinvestment

**Operational risk:**
- Settlement fails
- Recall difficulty (if borrower can't return quickly)
- Mitigated by: Automated systems

**Legal risk:**
- Bankruptcy of counterparty
- Collateral recovery delays
- Mitigated by: Legal documentation (MSLA)

---

## Repo Market Mechanics


### 1. Overnight Repo Cycle


**Daily workflow:**

**Morning:**
- Dealers assess financing needs
- Determine securities to repo
- Contact counterparties (money funds, banks)

**Afternoon (2-4 PM ET):**
- Negotiate repo rates
- Execute transactions
- Transfer securities and cash

**Next morning:**
- Unwind repo (repurchase securities)
- Interest payment calculated
- New repo for next day (if needed)

### 2. Tri-Party Repo Infrastructure


**Key players:**
- Bank of New York Mellon (BNYM)
- JP Morgan Chase
- Handle ~$4 trillion daily

**Process:**
1. Dealer and cash lender agree on terms
2. Custodian bank receives securities from dealer
3. Custodian transfers cash to dealer
4. Overnight: Custodian holds securities
5. Morning: Custodian reverses transaction

**Benefits:**
- Automated settlement
- Collateral optimization
- Operational efficiency

### 3. Repo Rate Dynamics


**SOFR (Secured Overnight Financing Rate):**
- Reference rate for US repo market
- Replaced LIBOR
- Volume-weighted median of Treasury repo

**Typical spread:**

$$
\text{Repo Rate} = \text{SOFR} + \text{Spread}
$$

**Spread components:**
- Credit risk: +0-10 bps
- Collateral quality: +0-50 bps
- Term premium: +5-20 bps per month
- Operational costs: +2-5 bps

### 4. Fails and Fails Charges


**Settlement fail:**
- Seller doesn't deliver securities on time
- Buyer doesn't receive what was purchased

**Consequences:**
- Fails charge: -3% annually (penalty rate)
- Borrower of failing security must pay penalty
- Creates incentive to cure fails quickly

**Example:**
- $\$10M$ Treasury fails to deliver
- Buyer charges: $\$10M × 0.03 / 360 = \$833$/day

### 5. Quarter-End and Year-End Effects


**Regulatory reporting:**
- Banks reduce balance sheets at reporting dates
- Less willing to lend cash in repo
- Repo rates spike

**Typical pattern:**
- Normal: SOFR = 2.5%
- Quarter-end: SOFR = 3.5% (100 bp spike!)
- Year-end: SOFR = 5.0% (250 bp spike!)

**Why:**
- Leverage ratio constraints
- Balance sheet management
- Basel III requirements

---

## Securities Lending Market


### 1. Market Size


**Global securities lending:**
- On-loan value: ~$2-3 trillion
- Annual revenue: ~$10 billion
- US equities: 60% of market
- Fixed income: 25%
- International equities: 15%

### 2. Lending Programs


**Beneficial owner programs:**
- Pension funds
- Mutual funds
- Insurance companies
- Sovereign wealth funds

**Typical returns:**
- Easy-to-borrow: 10-20 bps annually
- General collateral: 25-50 bps
- Hard-to-borrow: 100-300 bps
- Specials: Can add 100-500 bps

### 3. Short Selling Mechanics


**How short selling uses securities lending:**

1. Trader wants to short AAPL
2. Broker borrows AAPL shares (via sec lending)
3. Trader sells borrowed shares in market
4. Later: Trader buys shares, returns to lender
5. Profit if price fell, loss if price rose

**Lending enables:**
- Price discovery
- Hedging
- Arbitrage
- Market efficiency

### 4. Dividend Arbitrage


**Dividend tax strategy:**

Some investors use securities lending for tax:
- Lender sells before dividend (avoiding tax)
- Borrower receives dividend (different tax treatment)
- Share lending fee compensates

**Example:**
- US pension fund (tax-exempt) lends to foreign bank
- Foreign bank captures US dividend tax credit
- Pension earns lending fee as compensation

### 5. Equity Finance Desks


**Broker-dealer operations:**

Prime brokers run equity finance desks:
- Source securities to lend (from clients)
- Borrow securities for shorts (for other clients)
- Intermediate lending market
- Earn spread (borrow at 1%, lend at 1.5%)

**Inventory management:**
- Track lendable inventory
- Monitor utilization
- Price securities (easy vs. hard to borrow)

---

## Mathematical Framework


### 1. Repo Pricing


**Repo rate formula:**

$$
r_{\text{repo}} = r_{\text{rf}} + \text{Credit Spread} + \text{Collateral Adjustment}
$$

**For Treasury repo:**

$$
r_{\text{repo}} \approx \text{SOFR} + 5\text{-}15 \text{ bps}
$$

**For corporate bond repo:**

$$
r_{\text{repo}} \approx \text{SOFR} + 50\text{-}100 \text{ bps}
$$

### 2. Haircut Determination


**Optimal haircut:**

$$
h^* = k \times \sigma_{\text{collateral}} \times \sqrt{t}
$$

Where:
- $k$ = Risk aversion parameter (1-3)
- $\sigma_{\text{collateral}}$ = Daily volatility of collateral
- $t$ = Repo term (in days)

**Example:**
- Corporate bond: $\sigma = 1\%$ daily
- Overnight repo: $t = 1$ day
- $k = 2$ (moderate risk aversion)

**Haircut:**

$$
h^* = 2 \times 0.01 \times \sqrt{1} = 2\%
$$

### 3. Securities Lending Spread


**Net lending income:**

$$
\text{Net Income} = \text{Lending Fee} + \text{Rebate Spread}
$$

**For cash collateral:**

$$
\text{Rebate Spread} = r_{\text{investment}} - r_{\text{rebate}}
$$

**Example:**
- Lending fee: 50 bps
- Investment return: 200 bps
- Rebate to borrower: 175 bps
- **Net income: 50 + (200 - 175) = 75 bps**

### 4. Specialness Value


**Arbitrage between repo and securities lending:**

$$
\text{Specialness} = r_{\text{GC}} - r_{\text{special}}
$$

**Can convert to securities lending fee:**

$$
\text{Lending Fee} \approx \text{Specialness} \times \text{Price}
$$

**Example:**
- GC rate: 2.5%
- Special rate: 1.0%
- Specialness: 1.5% (150 bps)
- **Securities lending fee ≈ 150 bps**

### 5. Optimal Lending Strategy


**Maximize expected return:**

$$
\max \mathbb{E}[\text{Return}] = \mathbb{E}[\text{Fee Income}] - \mathbb{E}[\text{Reinvestment Loss}] - \text{OpEx}
$$

Subject to:
- Minimum collateral: 102%
- Maximum counterparty exposure
- Liquidity constraints

### 6. Collateral Velocity


**How many times collateral is reused:**

$$
\text{Velocity} = \frac{\text{Total Repo Volume}}{\text{Collateral Base}}
$$

**Pre-2008:** Velocity ≈ 3-4 (collateral rehypothecated multiple times)

**Post-2008:** Velocity ≈ 2-2.5 (reduced rehypothecation)

### 7. Break-Even Lending Fee


**Minimum fee to justify lending:**

$$
f_{\text{min}} = \frac{\text{OpEx} + \text{Capital Charge}}{\text{Security Value}}
$$

**Example:**
- OpEx: $\$50$ per loan
- Capital charge: $\$100$ (regulatory)
- Security value: $\$100,000$

**Min fee:**

$$
f_{\text{min}} = \frac{\$150}{\$100,000} = 15 \text{ bps annually}
$$

---

## Computational Tools


**Python implementations for repo and securities lending analysis:**

### 1. Repo Return Calculator

```python
import numpy as np

def calculate_repo_return(principal, repo_rate, days, haircut):
    """
    Calculate repo financing cost and effective leverage.
    
    Parameters:
    -----------
    principal : float
        Cash borrowed via repo
    repo_rate : float
        Annualized repo rate (e.g., 0.025 for 2.5%)
    days : int
        Term of repo in days
    haircut : float
        Haircut percentage (e.g., 0.05 for 5%)
    
    Returns:
    --------
    dict : Contains interest cost, collateral required, effective leverage
    """
    # Interest calculation (Actual/360 convention)
    interest = principal * repo_rate * days / 360
    
    # Collateral calculation
    collateral_required = principal / (1 - haircut)
    equity_posted = collateral_required - principal
    
    # Effective leverage
    effective_leverage = collateral_required / equity_posted
    
    # Cost as percentage of position (annualized)
    annualized_cost_pct = repo_rate * 360 / days * days / 360  # = repo_rate
    
    return {
        'interest': interest,
        'collateral_required': collateral_required,
        'equity_posted': equity_posted,
        'effective_leverage': effective_leverage,
        'repurchase_price': principal + interest,
        'annualized_cost': annualized_cost_pct
    }

# Example: $10M overnight repo at 2.5% with 5% haircut
result = calculate_repo_return(
    principal=10_000_000,
    repo_rate=0.025,
    days=1,
    haircut=0.05
)

print(f"Interest (1 day): ${result['interest']:,.2f}")
print(f"Collateral required: ${result['collateral_required']:,.0f}")
print(f"Effective leverage: {result['effective_leverage']:.1f}×")
print(f"Repurchase price: ${result['repurchase_price']:,.2f}")
```

### 2. Specialness and Carry Calculator

```python
def calculate_carry_and_specialness(bond_price, coupon_rate, days_held,
                                     gc_rate, special_rate=None):
    """
    Calculate carry for holding a bond and specialness premium.
    
    Parameters:
    -----------
    bond_price : float
        Clean price of bond
    coupon_rate : float
        Annual coupon rate (e.g., 0.04 for 4%)
    days_held : int
        Holding period in days
    gc_rate : float
        General collateral repo rate
    special_rate : float, optional
        Special repo rate if bond is special
    
    Returns:
    --------
    dict : Carry components and specialness value
    """
    # Accrued interest earned
    coupon_income = bond_price * coupon_rate * days_held / 360
    
    # Funding cost (if financing at GC)
    gc_funding_cost = bond_price * gc_rate * days_held / 360
    
    # Net carry at GC
    carry_at_gc = coupon_income - gc_funding_cost
    carry_at_gc_bps = carry_at_gc / bond_price * 360 / days_held * 10000
    
    result = {
        'coupon_income': coupon_income,
        'gc_funding_cost': gc_funding_cost,
        'carry_at_gc': carry_at_gc,
        'carry_at_gc_bps': carry_at_gc_bps
    }
    
    # If bond is special
    if special_rate is not None:
        special_funding_cost = bond_price * special_rate * days_held / 360
        carry_at_special = coupon_income - special_funding_cost
        
        # Specialness value
        specialness_bps = (gc_rate - special_rate) * 10000
        specialness_dollar = bond_price * (gc_rate - special_rate) * days_held / 360
        
        result.update({
            'special_funding_cost': special_funding_cost,
            'carry_at_special': carry_at_special,
            'specialness_bps': specialness_bps,
            'specialness_dollar_value': specialness_dollar
        })
    
    return result

# Example: 10Y Treasury at 98, 4% coupon, held 30 days
# GC rate 2.5%, special rate 1.0%
result = calculate_carry_and_specialness(
    bond_price=98,
    coupon_rate=0.04,
    days_held=30,
    gc_rate=0.025,
    special_rate=0.01
)

print(f"Coupon income (30 days): ${result['coupon_income']:,.2f}")
print(f"Carry at GC: {result['carry_at_gc_bps']:.1f} bps annualized")
print(f"Carry at special: ${result['carry_at_special']:,.2f}")
print(f"Specialness: {result['specialness_bps']:.0f} bps")
print(f"Specialness value: ${result['specialness_dollar_value']:,.2f}")
```

### 3. Securities Lending Revenue Estimator

```python
def estimate_lending_revenue(portfolio, lending_params):
    """
    Estimate annual securities lending revenue for a portfolio.
    
    Parameters:
    -----------
    portfolio : list of dict
        Each dict: {'security': str, 'value': float, 'utilization': float, 
                    'fee_bps': float}
    lending_params : dict
        {'agent_split': float, 'collateral_spread': float}
    
    Returns:
    --------
    dict : Revenue breakdown and totals
    """
    results = []
    
    for holding in portfolio:
        value = holding['value']
        utilization = holding['utilization']
        fee_bps = holding['fee_bps']
        
        # Gross lending revenue
        lent_value = value * utilization
        gross_revenue = lent_value * fee_bps / 10000
        
        # Agent takes their cut
        agent_fee = gross_revenue * lending_params['agent_split']
        net_revenue = gross_revenue - agent_fee
        
        # Collateral reinvestment (if cash collateral)
        collateral = lent_value * 1.02  # 102% collateralization
        reinvest_income = collateral * lending_params['collateral_spread']
        
        total_revenue = net_revenue + reinvest_income
        yield_enhancement_bps = total_revenue / value * 10000
        
        results.append({
            'security': holding['security'],
            'value': value,
            'lent_value': lent_value,
            'gross_revenue': gross_revenue,
            'net_revenue': net_revenue,
            'reinvest_income': reinvest_income,
            'total_revenue': total_revenue,
            'yield_enhancement_bps': yield_enhancement_bps
        })
    
    # Portfolio totals
    total_value = sum(r['value'] for r in results)
    total_revenue = sum(r['total_revenue'] for r in results)
    portfolio_yield_enhancement = total_revenue / total_value * 10000
    
    return {
        'holdings': results,
        'total_value': total_value,
        'total_revenue': total_revenue,
        'portfolio_yield_enhancement_bps': portfolio_yield_enhancement
    }

# Example portfolio
portfolio = [
    {'security': 'OTR 10Y Treasury', 'value': 50_000_000, 
     'utilization': 0.80, 'fee_bps': 100},
    {'security': 'OFR 10Y Treasury', 'value': 30_000_000, 
     'utilization': 0.40, 'fee_bps': 25},
    {'security': 'Corporate Bond', 'value': 20_000_000, 
     'utilization': 0.60, 'fee_bps': 75}
]

params = {
    'agent_split': 0.30,  # Agent takes 30%
    'collateral_spread': 0.002  # 20 bps reinvestment spread
}

result = estimate_lending_revenue(portfolio, params)

print(f"\nPortfolio Lending Revenue Analysis")
print("=" * 60)
for h in result['holdings']:
    print(f"{h['security']:20s}: ${h['total_revenue']:>12,.0f} "
          f"({h['yield_enhancement_bps']:.1f} bps)")
print("-" * 60)
print(f"{'Total':20s}: ${result['total_revenue']:>12,.0f} "
      f"({result['portfolio_yield_enhancement_bps']:.1f} bps)")
```

### 4. Haircut Stress Test

```python
def haircut_stress_test(positions, normal_haircuts, stress_multiplier=3):
    """
    Test portfolio leverage capacity under stress haircuts.
    
    Parameters:
    -----------
    positions : dict
        Asset class -> market value
    normal_haircuts : dict
        Asset class -> normal haircut %
    stress_multiplier : float
        How much haircuts increase in stress (typically 2-3×)
    
    Returns:
    --------
    dict : Normal vs stress borrowing capacity
    """
    results = {'normal': {}, 'stress': {}}
    
    total_value = sum(positions.values())
    
    normal_borrowing = 0
    stress_borrowing = 0
    
    for asset, value in positions.items():
        normal_haircut = normal_haircuts.get(asset, 0.20)  # Default 20%
        stress_haircut = min(normal_haircut * stress_multiplier, 0.80)
        
        normal_borrow = value * (1 - normal_haircut)
        stress_borrow = value * (1 - stress_haircut)
        
        normal_borrowing += normal_borrow
        stress_borrowing += stress_borrow
        
        results['normal'][asset] = {
            'value': value,
            'haircut': normal_haircut,
            'borrowing_capacity': normal_borrow
        }
        results['stress'][asset] = {
            'value': value,
            'haircut': stress_haircut,
            'borrowing_capacity': stress_borrow
        }
    
    equity_needed_normal = total_value - normal_borrowing
    equity_needed_stress = total_value - stress_borrowing
    
    max_leverage_normal = total_value / equity_needed_normal
    max_leverage_stress = total_value / equity_needed_stress
    
    return {
        'normal': results['normal'],
        'stress': results['stress'],
        'total_value': total_value,
        'normal_borrowing': normal_borrowing,
        'stress_borrowing': stress_borrowing,
        'equity_normal': equity_needed_normal,
        'equity_stress': equity_needed_stress,
        'max_leverage_normal': max_leverage_normal,
        'max_leverage_stress': max_leverage_stress,
        'leverage_reduction': (max_leverage_normal - max_leverage_stress) / max_leverage_normal
    }

# Example: $100M portfolio
positions = {
    'Treasuries': 50_000_000,
    'IG Corporates': 30_000_000,
    'HY Corporates': 20_000_000
}

haircuts = {
    'Treasuries': 0.02,
    'IG Corporates': 0.10,
    'HY Corporates': 0.25
}

stress = haircut_stress_test(positions, haircuts, stress_multiplier=3)

print(f"\nHaircut Stress Test Results")
print("=" * 60)
print(f"Total portfolio: ${stress['total_value']:,.0f}")
print(f"\nNormal conditions:")
print(f"  Borrowing capacity: ${stress['normal_borrowing']:,.0f}")
print(f"  Equity required: ${stress['equity_normal']:,.0f}")
print(f"  Max leverage: {stress['max_leverage_normal']:.1f}×")
print(f"\nStress conditions (3× haircuts):")
print(f"  Borrowing capacity: ${stress['stress_borrowing']:,.0f}")
print(f"  Equity required: ${stress['equity_stress']:,.0f}")
print(f"  Max leverage: {stress['max_leverage_stress']:.1f}×")
print(f"\nLeverage reduction in stress: {stress['leverage_reduction']:.1%}")
```

---

## Rehypothecation and Collateral Chains


**Understanding collateral reuse:**

### 1. What Is Rehypothecation?


**Definition:**

Rehypothecation is the practice where a broker-dealer or bank reuses collateral posted by clients for their own financing or trading purposes.

**Example chain:**
1. Hedge fund posts $\$100M$ Treasuries to Prime Broker A
2. Prime Broker A uses those Treasuries as collateral for repo with Bank B
3. Bank B uses same Treasuries for repo with Money Fund C
4. **Same $\$100M$ appears 3 times in the system!**

**Mathematical representation:**

$$
\text{Collateral Velocity} = \frac{\text{Total Pledged Collateral}}{\text{Original Collateral}}
$$

**Example:**
- Original: $\$100M$
- Total pledged: $\$280M$ (across 3 uses)
- **Velocity: 2.8**

### 2. Benefits and Risks


**Benefits:**
- Increases market liquidity
- Reduces funding costs
- Efficient use of high-quality collateral

**Systemic risks:**
- **Interconnectedness:** One default triggers chain of margin calls
- **Scarcity in stress:** Everyone recalls collateral simultaneously
- **Opacity:** Hard to track true ownership and claims
- **Velocity contraction:** In crisis, rehypothecation stops, funding evaporates

**2008 experience:**
- Lehman's failure triggered massive collateral disputes
- Clients couldn't recover rehypothecated assets
- $\$105B$ in customer assets at Lehman UK frozen for years

### 3. Regulatory Limits


**Post-2008 reforms:**

| Jurisdiction | Rehypothecation Limit |
|--------------|----------------------|
| US (Reg T) | 140% of client debit balance |
| UK (pre-2008) | Unlimited |
| UK (post-2015) | Limited to value of client borrowing |
| EU (SFTR) | Explicit consent required |

**Practical implications:**
- Client can limit rehypothecation rights
- Lower rehypothecation → Higher fees (prime broker charges more)
- Trade-off between cost and safety

### 4. Risk Management


**For hedge funds:**
- **Negotiate rehypothecation caps:** Limit what PB can reuse
- **Excess margin protection:** Keep excess above 140%
- **Diversify prime brokers:** Don't concentrate with single PB
- **Monitor collateral location:** Know where your assets are

**For asset owners:**
- **Prohibit rehypothecation:** In securities lending, can prohibit
- **Segregated accounts:** Assets in separate custody, not rehypothecated
- **Right of substitution:** Require immediate return, not "equivalent"

---

## Common Mistakes


**Pitfalls to avoid:**

### 1. Ignoring Counterparty Risk


**Mistake:** Assume repo is risk-free

**Why it fails:** Counterparty can default

**Example:**
- Lehman Brothers collapse (2008)
- Repo lenders stuck with securities
- Some securities declined 30-50%
- **Haircut insufficient**

**Fix:**
- Monitor counterparty credit
- Demand adequate haircuts
- Diversify counterparties
- Use tri-party repo (reduces risk)

### 2. Inadequate Haircuts


**Mistake:** Accept low haircuts to get more cash

**Why it fails:** Collateral volatility spikes

**Example:**
- Post equities with 5% haircut
- Market crashes 20% overnight
- Collateral now worth less than loan
- **Lender faces loss**

**Fix:**
- Use stress-tested haircuts
- Higher haircuts for volatile securities
- Daily mark-to-market
- Margin calls if needed

### 3. Cash Reinvestment Risk


**Mistake:** Invest cash collateral aggressively

**Why it fails:** Investments can lose value

**Example (2008):**
- Lend securities, receive cash collateral
- Invest in Lehman commercial paper (yield boost)
- Lehman defaults
- **Lost 100% of investment**

**Fix:**
- Conservative reinvestment (Treasuries, reverse repo)
- Match duration (don't invest long-term)
- Avoid credit risk
- Keep liquidity buffer

### 4. Recall Inability


**Mistake:** Lend securities without ensuring recall

**Why it fails:** Can't vote or sell when needed

**Example:**
- Pension fund lends stock
- Surprise takeover bid announced
- Try to recall to vote on deal
- Borrower can't return immediately (fails to deliver)
- **Miss critical vote**

**Fix:**
- Recall rights in agreement
- Monitor corporate actions
- Keep portion unlent for flexibility
- Automated recall systems

### 5. Ignoring Fails Charges


**Mistake:** Accept fails without penalty

**Why it fails:** Encourages sloppy settlement

**Example:**
- Lend Treasury via repo
- Borrower fails to return on time
- No penalty charged
- Borrower has no incentive to cure
- **Tied up collateral unnecessarily**

**Fix:**
- Enforce fails charges (3% penalty)
- Contractual language requiring timely settlement
- Monitor fails rate

### 6. Over-Reliance on Short-Term Funding


**Mistake:** Fund long-term positions with overnight repo

**Why it fails:** Rollover risk

**Example:**
- Buy illiquid bonds, fund via overnight repo
- Repo market seizes during crisis
- Can't roll funding
- **Forced to sell bonds at loss**

**Fix:**
- Match funding duration to position duration
- Use term repo for longer positions
- Keep liquidity buffer
- Diversify funding sources

### 7. Neglecting Operational Risk


**Mistake:** Manual processes, no automation

**Why it fails:** Settlement errors

**Example:**
- Manual repo confirmation
- Trade details wrong (amount, rate)
- Settlement fails
- **Costly reconciliation**

**Fix:**
- Automated systems
- Tri-party repo infrastructure
- Pre-trade validation
- Straight-through processing

### 8. Ignoring Regulatory Changes


**Mistake:** Don't adapt to new rules

**Why it fails:** Regulatory penalties

**Example:**
- Basel III leverage ratio introduced
- Bank doesn't reduce repo book
- Exceeds leverage limit
- **Fines and restrictions**

**Fix:**
- Monitor regulatory changes
- Adjust business model
- Balance sheet optimization
- Compliance systems

---

## Risk Management Rules


### 1. Haircut Adequacy


**Minimum haircuts by asset class:**

- **US Treasuries:** 2-5%
- **Investment-grade corporates:** 5-10%
- **High-yield bonds:** 15-25%
- **Large-cap equities:** 10-20%
- **Small-cap equities:** 20-30%
- **Emerging markets:** 25-50%

**Stress test:**
- Simulate 2008-level moves
- Ensure haircut > worst-case decline
- Add buffer (20-30% safety margin)

### 2. Counterparty Limits


**Maximum exposure per counterparty:**

$$
\text{Max Exposure} = \min\left(5\% \text{ of Capital}, \, \text{Rating-Based Limit}\right)
$$

**Rating-based limits:**
- AAA: 10% of capital
- AA: 5% of capital
- A: 2% of capital
- BBB or below: Don't transact

### 3. Collateral Reinvestment


**Conservative reinvestment:**

- **100% in:**
  - US Treasuries
  - Reverse repo (overnight)
  - Fed deposits

- **0% in:**
  - Corporate bonds
  - Equities
  - Structured products

**Duration limit:** ≤ Average loan term

### 4. Monitoring Frequency


**Daily:**
- Mark-to-market all positions
- Check margin calls
- Monitor counterparty news
- Review settlement fails

**Weekly:**
- Haircut adequacy review
- Counterparty exposure report
- Utilization rates

**Monthly:**
- Full risk review
- Stress testing
- Performance attribution

### 5. Liquidity Management


**Reserve requirement:**

$$
\text{Cash Reserve} \geq 10\% \times \text{Securities on Loan}
$$

**Purpose:**
- Handle recalls
- Meet unexpected redemptions
- Avoid forced liquidations

### 6. Documentation


**Required agreements:**
- Master Repurchase Agreement (MRA)
- Master Securities Lending Agreement (MSLA)
- Credit Support Annex (CSA)
- Tri-party repo agreement

**Key terms:**
- Haircuts
- Eligible collateral
- Margin call procedures
- Default remedies

---

## Real-World Examples


### 1. Lehman Collapse (2008)


**Setup:**
- Many lenders had repo exposure to Lehman
- Haircuts insufficient for crisis

**Outcome:**
- Lehman filed bankruptcy
- Repo lenders stuck with collateral
- Some securities fell 40-50%
- Haircuts 10-15% inadequate
- **Losses in billions**

**Lesson:** Counterparty risk is real, even with collateral

### 2. GameStop Short Squeeze (2021)


**Setup:**
- GME heavily shorted (>100% of float)
- Utilization: 100%
- Securities lending fee: 10% → 50% → 200%+

**Outcome:**
- Short squeeze drove price $20 → $480
- Lenders earned massive fees (20-30% annually)
- Some shorts forced to cover (borrowing too expensive)
- **Lenders profited from chaos**

**Lesson:** High utilization → High fees → Lender windfall

### 3. Quarter-End Repo Spike (2019)


**Setup:**
- September quarter-end approaching
- Banks reducing balance sheets
- Repo funding scarce

**Outcome:**
- Repo rate spiked: 2% → 10% (intraday!)
- Fed emergency intervention (repo operations)
- Dealers couldn't fund positions
- **Liquidity crisis averted by Fed**

**Lesson:** Balance sheet constraints create periodic stress

### 4. Tesla Securities Lending (2020)


**Setup:**
- TSLA heavily shorted
- Lending fee: 1% (low)
- Utilization: 60%

**Price surge:**
- TSLA rallied 700% in 2020
- Short squeeze dynamics
- Utilization → 85%
- **Lending fee → 5-8% (huge increase)**

**Lender benefit:**
- Pension funds earned extra 300-400 bps
- Enhanced returns on holdings
- No risk (fully collateralized)

**Lesson:** Volatile stocks with high short interest = High lending revenue

---

## Practical Steps


### 1. Initiating Repo Financing


**For borrowers:**

1. **Assess funding needs:**
   - How much cash needed?
   - For how long?
   - What securities available as collateral?

2. **Choose repo type:**
   - Overnight (most flexible, daily rollover)
   - Term (fixed period, rate locked)
   - Tri-party (operationally easier)

3. **Negotiate terms:**
   - Repo rate
   - Haircut
   - Collateral basket
   - Margin call procedures

4. **Execute:**
   - Legal documentation (MRA)
   - Settlement instructions
   - Daily monitoring

### 2. Starting Securities Lending


**For lenders (asset owners):**

1. **Select agent:**
   - Custodian bank with lending program
   - Compare fee splits (70/30, 80/20)
   - Check indemnification

2. **Define parameters:**
   - Eligible securities (which holdings to lend?)
   - Minimum fee threshold (e.g., 50 bps)
   - Collateral preferences (cash vs. securities)
   - Recall rights

3. **Monitor program:**
   - Monthly revenue reports
   - Utilization rates
   - Fee captures
   - Counterparty exposures

4. **Optimize:**
   - Review fee splits annually
   - Benchmark against peers
   - Adjust eligible securities

### 3. Risk Management Setup


**Establish framework:**

1. **Counterparty limits:**
   - Set per-counterparty caps
   - Rating-based approach
   - Daily monitoring

2. **Collateral rules:**
   - Haircut schedule
   - Eligible collateral list
   - Valuation frequency

3. **Operational controls:**
   - Automated settlement
   - Daily reconciliation
   - Exception reporting

4. **Stress testing:**
   - Quarterly scenario analysis
   - Haircut adequacy
   - Liquidity stress

---

## Final Wisdom


> "Repo and securities lending are the plumbing of modern finance - invisible to most but absolutely critical to market functioning. Repo provides the short-term leverage that allows market makers to hold inventory and investors to amplify returns, while securities lending enables short selling and price discovery. Both appear simple and safe on the surface (collateralized loans!), but contain subtle risks that have destroyed institutions when ignored. The key lessons from 2008: counterparty risk is never truly zero, haircuts must be stress-tested, and cash reinvestment must be conservative. Done right with proper risk management, these tools provide cheap funding and incremental yield with minimal risk. Done wrong, they blow up spectacularly."

**Key to success:**

- **Repo:** Use adequate haircuts (2-5% for Treasuries, 10-30% for equities), monitor counterparty credit daily, prefer tri-party repo for operational safety
- **Securities lending:** Conservative cash reinvestment (Treasuries only), negotiate fair fee splits (70/30+), maintain recall rights for corporate actions
- **Risk management:** Daily mark-to-market, enforce fails charges (3% penalty), diversify counterparties, match funding duration to position duration
- **Remember:** These are secured transactions but not risk-free - collateral can decline, counterparties can default, and markets can seize

---

## Related Topics


**Cross-references to other Chapter 25 sections:**

- **Balance Sheet Constraints (25.1.2):** Why dealer capacity for repo is limited post-Basel III; SLR impact on financing availability
- **Treasury Specials and Scarcity (25.2.2):** When specific securities command premium repo rates; specialness creates carry opportunities
- **Haircuts, Margin, and Funding Costs (25.4.1):** Detailed haircut calculation methods; stress testing framework for collateral
- **Crisis Basis Dynamics (25.3.2):** How repo market stress affects basis trades; funding liquidity during crises
