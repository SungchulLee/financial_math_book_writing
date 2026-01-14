# CDS Mechanics


**Credit Default Swaps (CDS)** are derivative contracts that transfer the credit risk of a reference entity from a protection buyer to a protection seller, allowing investors to isolate, hedge, or speculate on credit risk without owning the underlying bonds, fundamentally transforming how credit risk is priced and traded in global markets.

---

## The Core Insight


**The fundamental idea:**

- CDS is insurance against default (or other credit events)
- Protection buyer pays periodic premium (spread) to protection seller
- If credit event occurs: seller pays buyer the loss
- If no credit event: buyer pays premium for contract life, seller keeps payments
- Creates liquid market for pure credit risk
- Separates credit risk from interest rate risk and bond ownership
- Enables shorting credit (impossible with cash bonds)
- Price discovery: CDS spreads reflect market's view of default probability

**The key equations:**

**CDS premium (spread):**

$$
\text{CDS Spread} \approx (1 - \text{Recovery Rate}) \times \text{Default Probability}
$$

**Mark-to-market value:**

$$
\text{MTM} = (\text{Market Spread} - \text{Contract Spread}) \times \text{Risky DV01}
$$

**Present value of protection leg:**

$$
PV_{\text{protection}} = \sum_{t} \text{PD}_t \times (1 - R) \times \text{DF}_t
$$

**Present value of premium leg:**

$$
PV_{\text{premium}} = \sum_{t} s \times \text{Survival Prob}_t \times \text{DF}_t
$$

**At fair value: $PV_{\text{protection}} = PV_{\text{premium}}$**

**You're essentially asking: "What annual premium is fair compensation for bearing the risk of this company defaulting over the next 5 years, given my estimate of default probability and expected recovery?"**

---

## What Are Credit Default Swaps?


**Before trading CDS, understand the fundamental structure:**

### 1. The Basic CDS Contract


**A CDS contract has two legs:**

**1. Premium Leg (Protection Buyer → Protection Seller):**
- Quarterly payments (typically)
- Expressed as basis points annually (e.g., 150 bp)
- On notional amount (e.g., $10 million)
- Continues until maturity or credit event
- **Protection buyer is SHORT credit risk**

**2. Protection Leg (Protection Seller → Protection Buyer):**
- Activated only if credit event occurs
- Seller pays buyer the loss: (1 - Recovery Rate) × Notional
- Buyer delivers bonds or receives cash equivalent
- **Protection seller is LONG credit risk**

**Example contract:**

```
Reference Entity: XYZ Corporation
Notional: $10,000,000
CDS Spread: 250 basis points (2.50% annually)
Maturity: 5 years
Premium: Quarterly payments

Protection Buyer pays:
- Quarterly: $10M × 2.50% / 4 = $62,500
- Annually: $250,000
- Over 5 years (if no default): $1,250,000

If default occurs (assume Recovery Rate = 40%):
Protection Seller pays:
- Loss = (1 - 0.40) × $10M = $6,000,000
```

### 2. Credit Events (ISDA Definitions)


**What triggers the CDS contract:**

**Standard credit events:**

1. **Bankruptcy:**
   - Company files for bankruptcy protection
   - Insolvency proceedings
   - Most clear-cut credit event

2. **Failure to Pay:**
   - Missed interest or principal payment
   - After grace period expires
   - Above materiality threshold ($1 million typically)

3. **Restructuring (controversial):**
   - Debt rescheduling that is adverse to creditors
   - Reduced interest rate, principal reduction, maturity extension
   - Regional differences:
     - US: Often excluded ("No R" contracts)
     - Europe: Typically included

**Not credit events:**
- Stock price falling
- Credit rating downgrade
- Company struggling but still paying
- Merger/acquisition (unless causes default)

**ISDA Credit Derivatives Determinations Committee:**
- Industry body that votes on whether credit event occurred
- 15 members (dealers and buy-side)
- Supermajority (80%) required to declare credit event

### 3. Settlement Methods


**Two ways to settle after credit event:**

**1. Physical Settlement (Traditional):**

Protection buyer:
- Delivers $10M face value of bonds (or loans)
- Any seniority in CDS documentation (typically senior unsecured)

Protection seller:
- Pays $10M cash

**Net effect:**
- Buyer gets rid of defaulted bonds at par
- Seller owns the defaulted bonds (recovery value)

**Example:**
- CDS notional: $10M
- Buyer delivers $10M of defaulted XYZ bonds
- Seller pays $10M cash
- Bonds trading at 35 cents → Seller has $3.5M asset for $10M paid
- Seller's loss: $10M - $3.5M = $6.5M
- Buyer's gain: $10M - $3.5M = $6.5M

**2. Cash Settlement (Modern Standard):**

**Auction process (ISDA):**
- Occurs ~30 days after credit event
- Dealers submit bids for defaulted bonds
- Auction determines final recovery price
- Protection seller pays: (1 - Recovery) × Notional

**Example:**
- Auction recovery: 38%
- Protection seller pays: (1 - 0.38) × $10M = $6.2M cash
- No bond delivery needed

**Advantages of cash settlement:**
- No need to source deliverable bonds
- Avoids "cheapest-to-deliver" gaming
- More efficient
- Standard since 2009 (Big Bang Protocol)

### 4. The Big Bang Protocol (2009)


**Standardization changes:**

**Before 2009:**
- Customized spreads per contract
- Varied payment dates
- Different conventions
- Hard to trade/novate

**After 2009 (North America Big Bang):**

**Standard coupons:**
- Investment grade: 100 bp running
- High yield: 500 bp running

**Upfront payment:**
- Difference between market spread and standard coupon paid upfront
- Formula: Upfront ≈ (Market Spread - Standard Coupon) × Risky Duration

**Example:**

**Old way:**
- Market spread: 350 bp
- Contract: Pay 350 bp quarterly, zero upfront

**New way (Big Bang):**
- Standard coupon: 100 bp (IG) or 500 bp (HY)
- Market spread: 350 bp
- Running: Pay 100 bp quarterly
- Upfront: Protection buyer pays ≈ (350 - 100) × 4.5 = 11.25% of notional

**If 350 bp is between 100 and 500:**
- Running: 100 bp (if IG) or 500 bp (if HY)
- Upfront adjusts accordingly

**This made CDS more liquid and standardized!**

### 5. Mark-to-Market and P&L


**CDS positions are marked daily:**

**Protection buyer perspective:**

**If spreads widen (credit deteriorates):**
- Market spread: 150 bp → 250 bp (+100 bp)
- Position gains value (insurance more valuable)
- **MTM gain:**

$$
\text{Gain} \approx \Delta \text{Spread} \times \text{Risky DV01}
$$

$$
\text{Gain} = 100 \text{ bp} \times \$40,000 = \$400,000
$$

On $10M notional with 4.0 years risky duration.

**If spreads tighten (credit improves):**
- Market spread: 150 bp → 100 bp (-50 bp)
- Position loses value
- **MTM loss:** -50 bp × $40,000 = -$200,000

**Protection seller perspective:**
- Opposite signs
- Gains when spreads tighten
- Loses when spreads widen

**P&L components:**

$$
\text{Total P/L} = \underbrace{\text{Mark-to-Market}}_{\text{Spread change}} + \underbrace{\text{Carry}}_{\text{Premium received/paid}} + \underbrace{\text{Credit Event}}_{\text{Default loss/gain}}
$$

---

## Economic Interpretation: Why CDS Exist


**Understanding the fundamental economics:**

### 1. CDS as Pure Credit Derivatives


**Bond ownership bundles multiple risks:**

$$
\text{Bond Return} = \underbrace{r_f}_{\text{Risk-free rate}} + \underbrace{\text{Credit Spread}}_{\text{Default risk}} + \underbrace{\text{Liquidity Premium}}_{\text{Trading cost}} + \underbrace{\text{Tax Effects}}_{\text{Tax treatment}}
$$

**CDS isolates credit risk:**

$$
\text{CDS Return} \approx \text{Credit Spread} - \text{Default Losses}
$$

**This unbundling creates powerful applications:**

1. **Hedge credit without selling bonds:**
   - Portfolio manager owns $100M corporates
   - Worried about credit, not rates
   - Buy $100M CDS protection
   - **Net: Rate exposure only (credit hedged)**

2. **Short credit (impossible with bonds):**
   - Analyst thinks company overleveraged
   - Can't short bonds (repo market limitations)
   - Sell CDS protection
   - **Profit if spreads widen**

3. **Leverage credit exposure:**
   - Want $100M credit exposure
   - Don't want to tie up $100M capital
   - Sell CDS protection
   - Post ~5% margin ($5M)
   - **20x leverage!**

4. **Separate credit from rates:**
   - Bullish on rates, bearish on credit
   - Long Treasuries, sell CDS protection
   - **Pure rates vs. credit positioning**

### 2. CDS as Insurance with a Twist


**Unlike traditional insurance:**

**Traditional insurance:**
- Must own asset to insure (house, car)
- Pays only if you suffer loss
- Can't profit from insurance

**CDS (financial insurance):**
- **Don't need to own bonds** (speculation allowed)
- Protection buyer profits if spreads widen (even without default)
- Can be used for hedging OR speculation
- **This creates controversy** (naked CDS = betting on company failure)

**The "empty creditor" problem:**

**Scenario:**
- Hedge fund buys $50M CDS protection on XYZ Corp
- XYZ has $100M debt outstanding
- XYZ struggling, could restructure or default

**Perverse incentive:**
- Hedge fund profits from default
- May block restructuring (as bondholder could vote)
- **Incentive misalignment**

**This is debated:**
- Proponents: Price discovery, liquidity, risk management
- Critics: Destabilizing, incentivizes defaults, "financial weapons of mass destruction" (Buffett)

### 3. CDS Pricing Relationship to Bonds


**Theoretical arbitrage relationship:**

$$
\text{CDS Spread} \approx \text{Asset Swap Spread}
$$

**In practice:**

$$
\text{Basis} = \text{CDS Spread} - \text{Z-spread}
$$

**Typical basis: 20-50 bp (positive)**

**Why basis exists:**

1. **Funding costs:**
   - Buying bond requires funding (repo cost)
   - Selling CDS requires posting margin
   - Different costs create wedge

2. **Counterparty risk:**
   - CDS exposes to counterparty default risk
   - Bond is actual claim on company
   - **Lehman crisis showed this matters!**

3. **Deliverable bonds (CTD option):**
   - Physical settlement: buyer delivers "cheapest to deliver"
   - CDS can be worth more than specific bond

4. **Regulatory capital:**
   - CDS and bonds treated differently for capital
   - Banks may prefer one over other

5. **Supply/demand technical:**
   - CDS net notional can exceed bonds outstanding
   - Imbalances create basis

**The "basis trade":**

**Negative basis arbitrage:**
- Buy bond at Z-spread
- Buy CDS at lower spread
- **Earn: Bond spread - CDS spread**
- **Risk: Basis widens (common in stress)**

**Positive basis arbitrage:**
- Sell bond (via repo)
- Sell CDS protection
- **Earn: CDS spread - Bond spread**
- **Risk: Basis narrows or goes negative**

---

## Key Terminology


**Reference Entity:**

- Company or sovereign whose credit risk is being traded
- Must be clearly defined (legal entity)
- Example: "Ford Motor Company"

**Notional Amount:**

- Face value of protection (e.g., $10 million)
- Determines payment amounts
- Not actual money exchanged at inception

**CDS Spread (Premium):**

- Annual cost of protection
- Expressed in basis points
- Example: 250 bp = 2.50% annually
- Paid quarterly typically

**Upfront Payment:**

- Cash paid at inception (post-Big Bang)
- Adjusts for difference between running spread and market spread
- Can be positive (buyer pays) or negative (seller pays)

**Running Spread:**

- Standardized coupon payment
- 100 bp (IG) or 500 bp (HY) in North America
- Paid quarterly regardless of market spread

**Protection Buyer:**

- Pays premium
- Receives payment if credit event
- **Short credit** (wants spreads to widen)
- Analogous to buying insurance or buying put option

**Protection Seller:**

- Receives premium
- Pays if credit event occurs
- **Long credit** (wants spreads to tighten)
- Analogous to selling insurance or selling put option

**Credit Event:**

- Bankruptcy, failure to pay, or restructuring (if included)
- Triggers settlement
- Determined by ISDA DC (Determinations Committee)

**Recovery Rate:**

- Percentage of notional recovered after default
- Senior secured: 60-80%
- Senior unsecured: 30-50%
- Subordinated: 10-30%
- Assumed at contract inception (typically 40% for corporates)

**Risky DV01 (CS01):**

- Dollar value change for 1 bp spread change
- Accounts for default probability
- Formula: DV01 × Survival Probability

$$
\text{Risky DV01} = \sum_{t} \text{DF}_t \times \text{Survival Prob}_t \times 0.0001
$$

**Hazard Rate:**

- Instantaneous probability of default
- Constant hazard rate: $h$
- Cumulative default probability: $1 - e^{-ht}$

**ISDA:**

- International Swaps and Derivatives Association
- Sets standards for CDS contracts
- Determines Committee (DC) for credit event rulings

**Deliverable Obligations:**

- Bonds that can be delivered in physical settlement
- Typically senior unsecured
- Cheapest-to-deliver (CTD) bond usually delivered

**Auction (Protocol):**

- Process to determine recovery rate
- Occurs ~30 days after credit event
- Dealers submit bids/offers
- Final price used for cash settlement

**Index CDS:**

- Basket of single-name CDS
- CDX (North America), iTraxx (Europe)
- Investment grade and high yield versions
- More liquid than single names

**Tranche:**

- Slices of loss distribution in CDO/index
- Equity (0-3%), Mezzanine (3-7%), Senior (7-10%), Super Senior (10-100%)
- Different risk/return profiles

---

## Basic CDS Strategies


### 1. Strategy 1: Credit Hedge (Long Protection)


**Setup:**

**Portfolio Manager owns $50M corporate bonds:**
- Company: ABC Corp
- Bonds: 10-year senior unsecured
- Current price: $98
- Credit rating: BBB+
- Concern: Potential downgrade to BBB or lower

**Hedge:**
- Buy $50M notional CDS protection
- Term: 5 years
- CDS spread: 180 bp
- Running spread: 100 bp
- Upfront: -3.6% (protection buyer pays)

**Cost:**

```
Upfront: $50M × 3.6% = $1.8M (paid at inception)
Quarterly: $50M × 100 bp / 4 = $125,000
Annual: $500,000
```

**Scenario 1: Company remains healthy (no default)**

**5-year cost:**
- Upfront: $1.8M
- Running: $500k × 5 = $2.5M
- **Total cost: $4.3M (8.6% of notional)**

**Like insurance premium—paid for protection that wasn't needed.**

**Scenario 2: Spreads widen to 300 bp (credit deteriorates)**

**MTM on CDS:**
- Bought at: 180 bp
- Now trading: 300 bp
- Gain: (300 - 180) × Risky DV01
- Risky DV01 ≈ $50M × 4.2 × 0.0001 = $21,000
- **Gain: 120 bp × $21,000 = $2.52M**

**Bond position:**
- Spread widening: -120 bp × 7.5 duration = -9.0%
- Loss: $50M × 9.0% = -$4.5M

**Net:**
- Bond loss: -$4.5M
- CDS gain: +$2.52M
- Running cost paid: -$0.5M (1 year)
- **Net: -$2.48M (protected ~56% of bond loss)**

**Why not 100% hedge?**
- DV01 mismatch (bond 7.5, CDS risky DV01 ~4.2)
- Running cost drag
- Basis risk

**Scenario 3: Default occurs in Year 3**

**Recovery: 40% (assumed)**

**CDS settlement:**
- Protection seller pays: (1 - 0.40) × $50M = $30M
- Protection buyer receives: $30M

**Bond position:**
- Bonds worth: 40% × $50M = $20M
- Loss from par: $50M - $20M = -$30M

**Net result:**
- Bond loss: -$30M
- CDS gain: +$30M
- Running cost paid: $0.5M × 2.5 years = -$1.25M
- Upfront: -$1.8M
- **Net: -$3.05M (protected principal, lost premium)**

**Perfect hedge of default risk!**

### 2. Strategy 2: Short Credit (Sell Protection)


**Setup:**

**Hedge Fund View:**
- XYZ Corp (A-rated) fundamentals strong
- CDS spread: 120 bp (75th percentile - wide)
- Historical average: 80 bp
- Expect spread tightening to 80 bp

**Trade:**
- Sell $20M notional CDS protection
- 5-year maturity
- CDS spread: 120 bp
- Running: 100 bp
- Upfront: Protection seller receives 0.9% (positive carry)

**Expected return (no default scenario):**

**Upfront received:** $20M × 0.9% = $180,000

**Annual running received:** $20M × 100 bp = $200,000

**5-year total received (if no default):** $180k + ($200k × 5) = $1.18M

**Return on collateral:**
- Collateral posted: ~$2M (10% initial margin)
- Earned: $1.18M over 5 years
- **ROE: 59% over 5 years = 9.5% annualized**

**Scenario 1: Spreads tighten to 80 bp (view correct)**

**MTM gain:**
- Sold protection at: 120 bp
- Now trading: 80 bp
- Position gained value
- Gain: (120 - 80) × $20M × 4.3 × 0.0001 = $344,000

**Can close position:**
- Upfront received: $180,000
- MTM gain: $344,000
- Running received (1 year): $200,000
- **Total gain: $724,000 on $2M collateral = 36% return in 1 year**

**Scenario 2: Company defaults (Year 3)**

**Disaster for protection seller:**

**Recovery: 35% (worse than assumed 40%)**

**Settlement:**
- Must pay: (1 - 0.35) × $20M = $13M
- Received upfront: $180,000
- Received running: $200,000 × 2.5 = $500,000
- **Net loss: $13M - $0.68M = -$12.32M**

**On $2M collateral: -616% return (wipe out + debt)**

**This is the risk of selling protection—unlimited downside!**

### 3. Strategy 3: Curve Trade (Long/Short)


**Setup:**

**Single issuer, two maturities:**
- DEF Corp 5-year CDS: 150 bp
- DEF Corp 10-year CDS: 220 bp
- Slope: 70 bp (steep)

**Historical analysis:**
- Average slope: 50 bp
- Current at 90th percentile (very steep)

**View:** Curve will flatten (5s-10s spread will narrow)

**Trade (curve flattener):**
- Buy protection 10-year: $10M notional at 220 bp
- Sell protection 5-year: $10M notional at 150 bp
- **Net:** Long 10y, short 5y (flattener)

**DV01-neutral:**
- 10y risky DV01: $42,000
- 5y risky DV01: $23,000
- Ratio: 42/23 = 1.83
- Adjust: Sell $18.3M 5y protection to match DV01

**Scenario 1: Curve flattens (view correct)**

**3 months later:**
- 10-year: 220 → 200 bp (-20 bp)
- 5-year: 150 → 140 bp (-10 bp)
- Slope: 70 → 60 bp (flattened)

**P/L:**
- Long 10y (bought protection): Lost value (-20 bp tightening)
  - Loss: -20 × $42,000 = -$840,000
- Short 5y (sold protection): Gained value (-10 bp tightening)
  - Gain: -10 × $42,000 (DV01-matched) = +$420,000
- **Net: -$420,000**

**Wait, lost money even though view correct?**

**Problem: Parallel shift down hurt more than curve flattening helped.**

**Better trade: Focus on slope change:**

**Scenario 2: Rates unchanged, curve flattens**
- 10-year: 220 → 210 bp (-10 bp)
- 5-year: 150 → 150 bp (unchanged)
- Slope: 70 → 60 bp

**P/L:**
- Long 10y: -10 × $42,000 = -$420,000
- Short 5y: 0
- **Net: -$420,000**

**Still lost! The problem is directionality.**

**Correct implementation (DV01-neutral flattener):**

Actually need:
- Long protection 10y: Lose when tightens
- Short protection 5y: Gain when tightens
- **Net: Need 10y to outperform (tighten more or widen less)**

**Winning scenario:**
- 10-year: 220 → 200 bp (-20 bp)
- 5-year: 150 → 135 bp (-15 bp)
- 10y outperformed by 5 bp

**Or:**
- 10-year: 220 → 230 bp (+10 bp)
- 5-year: 150 → 165 bp (+15 bp)
- 10y outperformed by 5 bp (widened less)

### 4. Strategy 4: Index vs. Single-Name Arbitrage


**Setup:**

**CDX IG Index (125 names):**
- Spread: 65 bp
- Includes XYZ Corp (weight 0.8%)

**XYZ Corp single-name CDS:**
- Spread: 95 bp
- 30 bp wider than index

**Analysis:**
- XYZ fundamentals similar to index average
- Historical basis: XYZ trades 10-15 bp wider than index
- Current: 30 bp wider (2x historical)

**Trade (relative value):**
- Buy protection on XYZ: $10M notional at 95 bp
- Sell protection on Index: $1,250M notional (to match XYZ weight)
  - XYZ is 0.8% of index → $10M / 0.8% = $1,250M

**This is huge notional for small bet! Better approach:**

**Simplified trade:**
- Buy protection XYZ: $10M at 95 bp
- Sell protection on index: $100M at 65 bp (approximate)
- **Net bet:** XYZ spread vs. index spread narrows

**Scenario: Basis normalizes**
- XYZ: 95 → 80 bp (-15 bp)
- Index: 65 → 65 bp (unchanged)
- Basis: 30 → 15 bp (normalized)

**P/L:**
- Long protection XYZ: -15 bp × DV01 = -$63,000 (lost from tightening)
- Short protection index: 0 = $0
- **Net: -$63,000**

**Again lost! Need XYZ to outperform index, not just normalize.**

**Winning scenario:**
- XYZ: 95 → 75 bp (-20 bp)
- Index: 65 → 70 bp (+5 bp)
- XYZ outperformed by 25 bp

**Or simpler: Just bet on XYZ tightening more if view is single-name specific.**

---

## Greeks in CDS


**Understanding CDS sensitivities:**

### 1. CS01 (Credit Spread 01)


**Definition:**

$$
\text{CS01} = \frac{\partial V}{\partial s} \times 0.0001
$$

**Dollar value change for 1 bp spread change.**

**Also called "Risky DV01" or "Spread DV01"**

**Calculation:**

$$
\text{CS01} = \sum_{t=1}^{n} \text{DF}_t \times \text{Survival Prob}_t \times \frac{\text{Notional}}{10,000}
$$

**Approximation:**

$$
\text{CS01} \approx \text{Notional} \times \text{Risky Duration} \times 0.0001
$$

**Example:**

- Notional: $10M
- Maturity: 5 years
- Hazard rate: 2% (implies ~90% 5-year survival)
- Risky duration: 4.2 years (< 5 years due to default risk)

$$
\text{CS01} = \$10M \times 4.2 \times 0.0001 = \$4,200
$$

**Meaning: Position value changes $4,200 for every 1 bp spread change.**

**For protection buyer:**
- Spreads widen 50 bp: Gain $4,200 × 50 = $210,000
- Spreads tighten 50 bp: Lose $210,000

**For protection seller (opposite signs):**
- Spreads widen 50 bp: Lose $210,000
- Spreads tighten 50 bp: Gain $210,000

### 2. Carry (Theta)


**For protection buyer:**

$$
\text{Daily Carry} = -\frac{\text{Running Spread} \times \text{Notional}}{365}
$$

**Example:**
- Running spread: 100 bp
- Notional: $10M
- Daily carry: -$10M × 1% / 365 = -$2,740/day

**This is negative carry (paying premium daily).**

**For protection seller:**

$$
\text{Daily Carry} = +\frac{\text{Running Spread} \times \text{Notional}}{365}
$$

**Positive carry = $2,740/day received.**

**Breakeven spread move:**

$$
\text{Breakeven} = \frac{\text{Running Spread}}{365 \times \text{CS01}}
$$

**Example:**
- Running: 100 bp annually
- CS01: $4,200
- Days held: 30

$$
\text{Breakeven daily} = \frac{100}{365 \times 4.2} = 0.065 \text{ bp/day}
$$

Over 30 days: 0.065 × 30 = 1.95 bp

**Protection seller needs spreads to stay within 1.95 bp (not widen more) to breakeven over 30 days.**

### 3. Jump-to-Default Risk (Gamma)


**CDS have discontinuous payoff at default:**

**Protection seller exposure:**

Before default:
- Mark-to-market value based on spreads
- Carry positive

At default (instantaneous):
- Must pay: (1 - Recovery) × Notional
- **Jump loss!**

**Example:**
- Notional: $10M
- Recovery: 30% (worse than expected)
- Spread before default: 500 bp (distressed)
- MTM before: -$2M (seller is underwater already)

**At default:**
- Must pay: (1 - 0.30) × $10M = $7M
- Already marked at -$2M
- **Additional loss: $7M - $2M = $5M jump loss**

**This "jump-to-default" risk is unique to credit derivatives:**

- Similar to gamma risk in options (discontinuous)
- But credit has only downside (default)
- No upside equivalent

**Modeling:**

$$
\text{Jump Risk} = \text{Hazard Rate} \times (1 - \text{Recovery}) \times \text{Notional}
$$

**Example:**
- Hazard rate: 5% annually (distressed)
- Recovery: 40%
- Notional: $10M

$$
\text{Expected annual jump loss} = 5\% \times 60\% \times \$10M = \$300,000
$$

**Protection seller must earn at least $300k/year from carry to compensate for jump risk.**

### 4. Recovery Rate Sensitivity


**CDS value depends on assumed recovery:**

$$
\frac{\partial V}{\partial R} = -\text{Default Leg Sensitivity}
$$

**Higher recovery → Lower default loss → Lower CDS value (for protection buyer)**

**Example:**

**Assume recovery = 40%:**
- CDS spread: 250 bp
- Fair value

**If recovery actually = 30% (worse):**
- CDS worth more (protection more valuable)
- Spread widening equivalent: ~25-30 bp
- **Protection buyer gains, seller loses**

**Recovery risk is one-sided:**
- Protection buyer wants low recovery (more valuable payout)
- Protection seller wants high recovery (lower payout)

**Typical recovery assumptions:**
- Senior secured: 70%
- Senior unsecured: 40%
- Subordinated: 20%

**But in crisis, recoveries can be much lower:**
- Lehman Brothers: 9% (senior unsecured)
- Enron: 15-20%
- **Recovery risk is significant!**

---

## CDS Payoff Analysis


### 1. Protection Buyer Payoff


**Setup:**
- Buy $10M protection
- 5-year maturity
- CDS spread: 200 bp
- Running: 100 bp
- Upfront: -4.5% ($450,000 paid)

**Scenario 1: No default, spreads unchanged**

**5-year cost:**
- Upfront: $450,000
- Running: $100,000 × 5 = $500,000
- **Total cost: $950,000 (9.5% of notional)**

**Lost premium like insurance.**

**Scenario 2: No default, spreads widen to 400 bp**

**MTM gain:**
- Bought at: 200 bp
- Now: 400 bp
- Gain: 200 bp × $40,000 CS01 = $800,000

**Net:**
- MTM gain: +$800,000
- Running paid (1 year): -$100,000
- Upfront: -$450,000
- **Net: +$250,000 (2.5% return)**

**Can sell protection to close and lock in gain.**

**Scenario 3: Default in Year 2, recovery 35%**

**Settlement:**
- Receive: (1 - 0.35) × $10M = $6.5M

**Costs:**
- Upfront: $450,000
- Running: $100,000 × 1.5 = $150,000
- **Total cost: $600,000**

**Net:**
- Received: $6.5M
- Paid: $0.6M
- **Net gain: $5.9M (59% return on notional)**

**But only gain if owned bonds:**
- Bonds at 35%: Worth $3.5M
- Par value: $10M
- Bond loss: $6.5M
- CDS gain: $6.5M
- Running/upfront: -$0.6M
- **Net: -$0.6M (cost of insurance)**

**Perfect hedge!**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/cds_protection_buyer_payoff.png?raw=true" alt="cds_protection_buyer_payoff" width="700">
</p>
**Figure 1:** Protection buyer P/L profile showing limited downside (premium paid) and large upside from spread widening or default, similar to long put option on credit.

### 2. Protection Seller Payoff


**Same setup, opposite side:**

**Scenario 1: No default, spreads unchanged**

**5-year gain:**
- Upfront received: $450,000
- Running received: $500,000
- **Total: $950,000 (9.5% gain on $10M notional)**

**On collateral posted ($1M):**
- Return: 95% over 5 years = 14.3% annualized

**Scenario 2: No default, spreads widen to 400 bp**

**MTM loss:**
- Sold at: 200 bp
- Now: 400 bp
- Loss: -$800,000

**Net:**
- MTM loss: -$800,000
- Running received: +$100,000
- Upfront: +$450,000
- **Net: -$250,000 (-2.5%)**

**Scenario 3: Default in Year 2, recovery 35%**

**Disaster:**
- Must pay: $6.5M
- Received: $450k + $150k = $600k
- **Net loss: -$5.9M (-59% on notional, -590% on $1M collateral)**

**This is why selling protection can be catastrophic!**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/cds_protection_seller_payoff.png?raw=true" alt="cds_protection_seller_payoff" width="700">
</p>
**Figure 2:** Protection seller P/L profile showing limited upside (premium collected) and large downside from spread widening or default, similar to short put option on credit.

---

## Real-World CDS Examples


### 1. Example 1: Corporate Hedge - Ford Motor (Winner)


**Setup:**

- **Date:** March 2020 (COVID crisis)
- **Institution:** Pension fund with $200M Ford bonds
- **Bonds:** 10-year senior unsecured, trading at $95
- **Rating:** BBB- (lowest investment grade)

**Concern:**
- Auto industry shut down
- Ford cash flow under stress
- Downgrade to high yield likely
- **Want to hedge credit risk**

**Hedge implementation:**

**Buy CDS protection:**
- Notional: $200M
- Maturity: 5 years
- CDS spread: 650 bp (distressed!)
- Running: 500 bp
- Upfront: -$30M (15% of notional)

**Cost:**
- Upfront: $30M (paid immediately)
- Annual running: $200M × 5% = $10M/year

**Trade evolution:**

**Month 1 (March-April 2020):**
- Ford shuts factories
- CDS spreads spike to 1,100 bp
- Bonds fall to $78

**P/L:**

| Position | Change | Value |
|----------|--------|-------|
| Bonds | $95 → $78 | -$34M |
| CDS MTM | 650 → 1,100 bp (+450 bp) | +$36M |
| Running cost | 1 month | -$0.83M |
| **Net** | | **+$1.17M** |

**CDS hedge working perfectly!**

**Month 2-6 (May-September):**
- Government stimulus
- Auto demand rebounds
- Ford stabilizes

**Spreads improve:**
- CDS: 1,100 → 450 bp (-650 bp from peak)
- Bonds: $78 → $92

**Decision point (September):**

**Close hedge:**
- Bought protection at: 650 bp (upfront adjusted)
- Close at: 450 bp
- **Realize gain: $16M (MTM from peak)**

**Or hold?**
- If confident recovery continues, close
- If still worried, hold

**Manager's decision: Close 50% of hedge**

- Close $100M protection at 450 bp
- Lock in $8M gain (on half)
- Keep $100M protection as tail risk hedge

**Final outcome (1 year later, March 2021):**

**Ford upgraded, spreads normalize:**
- CDS: 450 → 180 bp (investment grade normalized)
- Bonds: $92 → $101

**Closed remaining $100M protection:**
- Spread gain: (650 - 180) × CS01 = $38M
- Running paid: $10M × 1 year = $10M
- Upfront: $30M
- **Net: $38M - $40M = -$2M cost**

**Total hedge results:**

| Component | P/L |
|-----------|-----|
| First $100M closed (peak) | +$8M |
| Second $100M closed (end) | -$2M |
| **Net hedge cost** | **+$6M** |

**Bond position:**
- Started: $190M (95% of par)
- Ended: $202M (101% of par)
- Gain: +$12M

**Combined:**
- Bond gain: +$12M
- Hedge cost: -$6M net
- **Total: +$6M (3% return during crisis)**

**Without hedge:**
- Bonds: $190M → $156M (low) → $202M (end)
- Would have survived but with -17% drawdown
- Hedge reduced max drawdown from -17% to -3%

**Why it worked:**

1. **Perfect timing:** Bought protection just before spreads spiked
2. **Scaled exit:** Closed half at peak, kept half
3. **Survived crisis:** Pension fund didn't face redemptions
4. **Discipline:** Paid premium even when hurt (cost drag)

### 2. Example 2: Basis Trade - Lehman Disaster (Loser)


**Setup:**

- **Date:** June 2008 (pre-crisis)
- **Hedge Fund:** Relative value credit fund
- **Strategy:** Negative basis arbitrage on Lehman Brothers

**Basis trade analysis:**

**Lehman Brothers:**
- 5-year CDS: 220 bp
- 5-year bond (senior): Z-spread 280 bp
- **Negative basis: -60 bp** (CDS cheaper than bond)

**Historical basis: -20 to -30 bp**
**Current: -60 bp (2x normal) → Opportunity?**

**Trade:**
- Buy Lehman bonds: $50M face value at $98 (yield 3.20%)
- Buy CDS protection: $50M notional at 220 bp
- **Net position: Earn basis (280 - 220 = 60 bp)**

**Expected return:**
- Basis earned: 60 bp annually
- Funding cost (repo): 2.50%
- CDS premium: -220 bp
- Bond yield: +320 bp
- **Net carry: 60 bp = 0.60% annually**

**Seemed conservative:**
- Hedged default risk (own bonds + bought protection)
- Just betting on basis normalization
- **What could go wrong?**

**Evolution - The Disaster:**

**July-August 2008:**
- Bear Stearns already failed (March)
- Lehman stress increasing
- CDS: 220 → 350 bp (+130 bp)
- Bonds: Z-spread 280 → 400 bp (+120 bp)
- Basis: -60 → -50 bp (improved slightly)

**P/L (2 months):**

| Position | Change | P/L |
|----------|--------|-----|
| Bonds | -$3.5M | -$3.5M |
| CDS (long protection) | +130 bp × $20k CS01 | +$2.6M |
| Running/carry | | -$0.3M |
| **Net** | | **-$1.2M (-2.4%)** |

**Painful but manageable. Manager held on.**

**September 2008: Lehman Files Bankruptcy**

**Chaos:**

1. **Bonds freeze:**
   - Trading halts
   - No bid
   - **Stuck holding worthless bonds**

2. **CDS should pay out:**
   - Protection should be worth (1 - Recovery) × $50M
   - Expected recovery: 40%
   - Expected payout: $30M

3. **BUT: Counterparty risk!**
   - CDS protection sold by... Lehman's own desk (!)
   - **CDS contract worthless** (counterparty defaulted)

**Even if different counterparty:**
- Market freeze
- Unclear who has exposure
- Settlement uncertainty

**Auction (October 2008):**
- Lehman bonds recovery: **8.6%** (much worse than 40%)
- Should receive: (1 - 0.086) × $50M = $45.7M from CDS

**But actual outcome:**

| Component | Expected | Actual | Notes |
|-----------|----------|--------|-------|
| CDS payout | $45.7M | $0M | Counterparty defaulted |
| Bonds value | | $4.3M | 8.6% recovery |
| **Net** | +$45.7M | -$45.7M | **Total wipeout** |

**$50M position → $4.3M recovered**
**Loss: -$45.7M (-91%)**

**What went wrong:**

1. **Counterparty risk:**
   - Bought protection from Lehman itself (!)
   - Even if from other dealer, systemic risk
   - **CDS hedge failed when needed most**

2. **Basis blow-out:**
   - Assumed basis mean reverts
   - In crisis, basis exploded
   - Negative basis went to -500 bp+

3. **Liquidity freeze:**
   - Couldn't sell bonds
   - Couldn't exit CDS
   - **Trapped in position**

4. **Wrong-way risk:**
   - Hedging Lehman with Lehman CDS
   - Classic mistake
   - Should have hedged with index or peers

5. **Recovery assumption:**
   - Expected 40%, got 8.6%
   - **Recovery risk underestimated**

**Lessons:**

- **Counterparty risk is real** (post-crisis, central clearing mandated)
- **Basis can blow out in crisis** (not mean reverting)
- **Never buy protection from the reference entity**
- **Systemic risk affects all hedges**

### 3. Example 3: Naked CDS Speculation - Tesla (Winner)


**Setup:**

- **Date:** January 2019
- **Trader:** Discretionary macro hedge fund
- **View:** Tesla overleveraged, Musk erratic, burn rate high

**Analysis:**
- Tesla debt: $10B
- Cash burn: $1B/quarter
- Production hell (Model 3)
- SEC investigation
- **High bankruptcy risk (in trader's view)**

**Trade:**
- Buy CDS protection: $25M notional
- 5-year maturity
- CDS spread: 380 bp (already distressed)
- Running: 500 bp
- Upfront: -$5M (20% of notional)

**Capital:**
- Collateral posted: $2.5M
- Upfront paid: $5M
- **Total capital: $7.5M**

**Note: Trader does NOT own Tesla bonds!**
- This is "naked CDS" (pure speculation)
- Betting on default or spread widening
- Like buying put options on Tesla credit

**Trade evolution:**

**Months 1-6 (Jan-Jun 2019):**
- Tesla struggles continue
- Model 3 production issues
- Musk tweets erratically
- **Spreads widen: 380 → 650 bp (+270 bp)**

**MTM:**
- Gain: 270 bp × $90k CS01 = $2.43M
- Running paid: $25M × 5% × 0.5 = -$625k
- **Net: +$1.8M (+24% on $7.5M capital)**

**Month 7-12 (Jul-Dec 2019): The Reversal**

**Tesla turns around:**
- Model 3 production ramped successfully
- Profitability achieved (Q3 surprise)
- Stock price rallies
- Credit concerns fade

**Spreads collapse:**
- CDS: 650 → 280 bp (-370 bp)

**MTM disaster:**
- Loss from entry: (280 - 380) = -100 bp → +$900k gain
- But from peak (650 bp): -370 bp loss = -$3.33M

**Decision:** Cut position at loss
- Closed at 280 bp
- Total received from premium: $1.25M (from peak $25M for 1 year)
- Paid upfront: $5M
- MTM from entry (380 → 280): +$900k
- **Net: +$900k + $1.25M - $5M = -$2.85M**

**Loss: -38% on $7.5M capital**

**Why it failed:**

1. **Timing:** Entered too late (380 bp already distressed)
2. **Company improved:** Fundamentals turned around
3. **No catalyst:** Default didn't materialize
4. **Negative carry:** Paying 500 bp/year premium
5. **Gave back gains:** Should have closed at peak (650 bp)

**Lessons:**
- Naked CDS is pure speculation (not hedging)
- Need catalyst for default, not just weak fundamentals
- Negative carry hurts if spreads don't widen further
- **Companies can recover** (Tesla is still here!)

---

## Best Case Scenario


### 1. The Perfect CDS Trade - AIG Rescue (2008)


**Setup:**

- **Date:** July 2008
- **Sophisticated Hedge Fund**
- **View:** AIG exposure to CDS on mortgage-backed securities is catastrophic

**Background:**
- AIG sold billions in CDS protection on AAA-rated CDOs
- CDOs backed by subprime mortgages
- Housing market collapsing
- AIG doesn't have capital to cover losses
- **Bankruptcy or bailout inevitable**

**The Trade:**

**Buy CDS protection on AIG:**
- Notional: $100M
- Maturity: 5 years
- CDS spread: 350 bp (July 2008)
- Running: 500 bp
- Upfront: -$8M

**Capital required:**
- Collateral: $10M
- Upfront: $8M
- **Total: $18M**

**This is a BET on AIG default or severe distress.**

**Month 1 (July-August 2008):**

- Lehman Brothers fails (September)
- Systemic panic
- **AIG spreads explode:**

| Date | AIG CDS | Change | Position MTM |
|------|---------|--------|--------------|
| July 1 | 350 bp | Entry | $0 |
| Aug 1 | 580 bp | +230 bp | +$9.2M |
| Sep 1 | 1,200 bp | +850 bp | +$34M |
| Sep 15 | 2,400 bp | +2,050 bp | +$82M |

**September 16, 2008: AIG Bailout Announced**

**Government rescue:**
- Fed provides $85B credit line
- Takes 79.9% equity stake
- AIG will NOT default

**CDS spreads:**
- Peak: 2,400 bp (imminent default priced)
- After bailout: 800 bp (stabilized)

**Trader's decision: SELL at 2,400 bp (perfect timing!)**

**Final P/L:**

| Component | Amount |
|-----------|--------|
| MTM gain | +$82M |
| Running paid (3 months) | -$1.25M |
| Upfront | -$8M |
| **Net profit** | **+$72.75M** |

**Return on capital:**
- Capital: $18M
- Profit: $72.75M
- **Return: 404% in 3 months**

**Why this was best case:**

1. **Perfect timing:** Entered before crisis peaked
2. **Correct fundamental view:** AIG exposure was catastrophic
3. **Systemic catalyst:** Lehman bankruptcy triggered panic
4. **Exit discipline:** Sold at peak (2,400 bp)
5. **Bailout understood:** Knew government wouldn't let AIG actually default

**The key insight:**

- AIG wouldn't technically default (too big to fail)
- BUT spreads would spike to default levels (2,000+ bp)
- **Trade was spread widening, not actual default**
- Perfect asymmetry: Limited downside (premium), massive upside (systemic panic)

**Comparison to actual default:**

If AIG had defaulted:
- Recovery: ~20% (financial company)
- Payout: (1 - 0.20) × $100M = $80M
- Less premiums paid: ~$80M - $9M = $71M

**Similar to actual spread gain! But timing was everything.**

---

## Worst Case Scenario


### 1. The CDS Seller Apocalypse - Magnetar (2008-2009)


**Setup:**

- **Fund:** Highly leveraged credit hedge fund
- **Strategy:** Sell CDS protection (collect premiums)
- **Date:** 2007 (peak of credit bubble)

**Portfolio:**

**Sold $5 billion notional CDS protection on:**
- CDX IG Index: $2B at 35 bp (seemed safe - investment grade)
- CDX HY Index: $1B at 280 bp (higher premium)
- Single-name corporates: $2B at avg 150 bp

**Expected annual premium:**

| Position | Notional | Spread | Annual Premium |
|----------|----------|--------|----------------|
| IG Index | $2B | 35 bp | $7M |
| HY Index | $1B | 280 bp | $28M |
| Single-names | $2B | 150 bp | $30M |
| **Total** | **$5B** | | **$65M/year** |

**Capital structure:**
- Equity: $200M
- Leverage: 25x (!) on $5B notional
- Collateral: $200M + mark-to-market adjustments

**Expected return:**
- Premium: $65M annually
- On equity: $200M
- **ROE: 32.5% annually**

**"Free money" in benign environment!**

**2007: Everything Perfect**

**Year 1 results:**
- Premium collected: $65M
- No defaults
- Spreads generally tightened
- MTM gains: +$45M
- **Total: +$110M (+55% ROE)**

**Management: "This is easy! Let's scale up!"**

**Mistake #1: Increased leverage to 35x**

**New portfolio (early 2008):**
- Sold $7B notional protection
- Premium: $95M annually
- Equity: $200M (didn't raise more)
- **Leverage: 35x**

**2008: The Collapse**

**March-September 2008:**

**IG Index:**
- Spread: 35 bp → 250 bp (+215 bp)
- MTM loss: 215 bp × $2B × 4.5 / 10,000 = -$193.5M

**HY Index:**
- Spread: 280 bp → 1,800 bp (+1,520 bp)
- MTM loss: 1,520 bp × $1B × 3.5 / 10,000 = -$532M

**Single-names (worse):**
- Multiple defaults: Lehman, Bear Stearns, WaMu, Wachovia
- Average spread: 150 bp → 900 bp
- MTM loss: -$315M
- **Plus actual defaults: -$180M (net of recovery)**

**Total portfolio MTM: -$1.22 billion**

**Margin calls:**

**September 15, 2008 (Lehman bankruptcy):**

- Mark-to-market loss: -$1.22B
- Equity: $200M
- **Equity wiped out + $1.02B debt**

**Counterparties demand margin:**
- Immediate margin call: $800M
- Fund has: $50M in cash
- **Default on margin = forced liquidation**

**Forced Liquidation:**

**Week of September 15:**
- Must close positions to meet margin
- Market illiquid, bid-ask spreads enormous
- **Forced to buy back protection at worst prices**

**Liquidation prices:**

| Position | Entry | Liquidation | Loss Realized |
|----------|-------|-------------|---------------|
| IG Index | 35 bp sold | 280 bp bought | -$441M |
| HY Index | 280 bp sold | 2,100 bp bought | -$637M |
| Single-names | 150 bp avg | 1,200 bp avg | -$420M |

**Total realized loss: -$1.498 billion**

**Final outcome:**

- Started with: $200M equity
- Ended with: -$1.3B debt
- **Total destruction: -$1.5B**

**Fund declares bankruptcy, investors lose 100% + clawbacks**

**Counterparty exposure:**
- Banks try to recover from fund
- Long legal battle
- Recover ~15 cents on dollar

**What went wrong:**

**Mistake #1: Extreme leverage (35x)**
- $7B exposure on $200M equity
- One bad year = wipeout
- No margin of safety

**Mistake #2: Sold protection at cycle peak**
- Spreads at all-time tights (2007)
- No upside, all downside
- Terrible risk/reward

**Mistake #3: Concentrated in financial crisis**
- All positions correlated
- Financial sector collapsed together
- No diversification benefit

**Mistake #4: No hedges**
- Pure short credit (sold protection only)
- No offsetting longs
- **Full exposure to systemic risk**

**Mistake #5: Ignored tail risk**
- Modeled 2-3 standard deviation moves
- Crisis was 10+ standard deviations
- **VaR models useless**

**Mistake #6: Forced liquidation**
- Couldn't meet margin calls
- Sold at worst prices
- Would have recovered somewhat if could hold

**Comparison to holding through:**

**Hypothetical: If had unlimited capital, held through crisis:**

**By 2010 (2 years later):**
- IG Index: 250 bp → 90 bp (normalized)
- HY Index: 1,800 bp → 450 bp
- MTM recovery: +$900M

**But couldn't survive to see recovery!**

**Lessons:**

1. **Leverage kills:** 35x leverage = no room for error
2. **Selling protection is short volatility:** Collect premium until you don't
3. **Correlation goes to 1 in crisis:** All positions fail together
4. **Liquidity matters:** Forced selling at worst prices
5. **Tail risk is real:** Fat tails, not normal distribution
6. **CDS can amplify losses:** Notional far exceeds capital

**The CDS seller's dilemma:**

$$
\text{Collect \$1 in premiums for years} \rightarrow \text{Lose \$100 in one month}
$$

**"Picking up pennies in front of a steamroller."**

---

## What to Remember


### 1. Core Concept


**CDS transfers credit risk from buyer to seller:**

$$
\text{Protection Buyer} \xrightarrow{\text{Premium}} \text{Protection Seller}
$$

$$
\text{Protection Seller} \xrightarrow{\text{If default}} \text{Protection Buyer}
$$

- Buyer: Short credit (wants spreads to widen)
- Seller: Long credit (wants spreads to tighten)
- Liquid market for pure credit risk
- Enables hedging, speculation, arbitrage

### 2. Key Equations


**CDS spread approximation:**

$$
\text{CDS Spread} \approx (1 - R) \times \lambda
$$

Where $R$ = Recovery rate, $\lambda$ = Hazard rate

**Mark-to-market:**

$$
\text{MTM} = (\text{Market Spread} - \text{Contract Spread}) \times \text{CS01}
$$

**CS01 (Credit Spread 01):**

$$
\text{CS01} = \text{Notional} \times \text{Risky Duration} \times 0.0001
$$

**Fair value condition:**

$$
PV_{\text{premium leg}} = PV_{\text{protection leg}}
$$

### 3. Contract Structure


**Standard terms (post-Big Bang):**

- **Running spread:** 100 bp (IG) or 500 bp (HY)
- **Upfront payment:** Adjusts for market spread
- **Payment frequency:** Quarterly
- **Maturity:** Typically 5 years
- **Settlement:** Cash (auction-based)

**Credit events:**
- Bankruptcy
- Failure to pay
- Restructuring (regional)

### 4. Payoff Profiles


**Protection buyer (long protection):**
- Limited downside: Premium paid
- Large upside: Spread widening or default
- **Analogous to: Long put on credit**

**Protection seller (short protection):**
- Limited upside: Premium collected
- Large downside: Spread widening or default
- **Analogous to: Short put on credit**

### 5. Position Sizing


**Conservative (recommended):**

$$
\text{Notional} = \frac{0.02 \times \text{Portfolio}}{\text{Expected Loss Rate}}
$$

**Where Expected Loss = PD × LGD**

**Example:**
- Portfolio: $100M
- Max risk: 2% = $2M
- Expected loss: 5% (PD 10% × LGD 50%)
- **Max notional: $2M / 5% = $40M**

**Leverage guideline:**
- Equity: $100M
- CDS notional sold: <$500M
- **Max leverage: 5x** (conservative)
- Absolute max: 10x (aggressive)

### 6. Risk Metrics


**Daily monitoring:**

- **CS01:** Spread sensitivity
- **Carry:** Daily premium P/L
- **Jump-to-default:** Potential loss if immediate default
- **Counterparty exposure:** Mark-to-market with each dealer

**Portfolio limits:**

- Max single-name: 5% of equity
- Max sector: 20% of equity
- Max leverage: 5-10x
- Min liquidity: 3 months premium coverage

### 7. Entry Checklist


**For buying protection (shorting credit):**

1. [ ] Fundamental view: Credit deteriorating
2. [ ] Technical: Spreads at low end of range
3. [ ] Catalyst: Identified event/trend
4. [ ] Liquidity: Tight bid-ask (<5 bp)
5. [ ] Counterparty: Strong credit rating

**For selling protection (long credit):**

1. [ ] Spreads at wide end of range (>75th percentile)
2. [ ] Fundamentals stable or improving
3. [ ] Recovery rate assumption validated
4. [ ] Portfolio not overleveraged
5. [ ] Understand jump-to-default risk

### 8. Exit Rules


**Stop losses:**

**Protection buyer:**
- Spread tightens 50 bp from entry → Exit (-loss)
- Time decay: 50% of time with no progress → Exit
- Fundamentals improve → Close position

**Protection seller:**
- Spread widens 100 bp from entry → Exit (-loss)
- Rating downgrade → Consider exit
- MTM loss > 20% of collateral → Exit

**Profit targets:**

**Protection buyer:**
- Spread widens 100+ bp → Take profit
- Default event priced in → Close
- Achieved return target (>30%) → Exit

**Protection seller:**
- Spread tightens 50+ bp → Lock in gain
- Upgrade announced → Take profit
- Collected >75% of potential premium → Close

### 9. Common Mistakes to Avoid


1. **Selling protection without understanding jump risk**
   - Can lose far more than premium collected
   - Need margin of safety

2. **Overleveraging as protection seller**
   - 25x+ leverage = wipeout in crisis
   - Max 5-10x recommended

3. **Ignoring counterparty risk**
   - AIG, Lehman showed this matters
   - Use central clearing (mandatory now)

4. **Wrong-way risk**
   - Buying protection from reference entity itself
   - Hedge fails when needed

5. **Naked CDS speculation without catalyst**
   - Need default catalyst, not just weak fundamentals
   - Negative carry hurts

6. **Assuming basis mean reverts**
   - Cash-CDS basis can blow out in crisis
   - Not risk-free arbitrage

7. **Ignoring recovery rate assumptions**
   - 40% assumption common
   - Reality can be 10-80%

8. **No exit plan**
   - Set stops and targets before entry
   - Don't marry positions

### 10. Comparison to Cash Bonds


| CDS | Cash Bonds |
|-----|------------|
| Pure credit exposure | Credit + rates + liquidity |
| Can short credit | Hard to short |
| Leverage (5-10x) | Leverage (2-3x max) |
| Quarterly premium | Semi-annual coupon |
| No principal at risk | Principal at risk |
| Counterparty risk | Issuer risk only |
| Easy to exit | May be illiquid |
| Jump-to-default risk | Gradual price changes |

### 11. Performance Expectations


**Protection seller (typical):**

- Carry: 100-300 bp annually
- Default losses: 20-50 bp annually
- MTM volatility: 200-500 bp annually
- **Net expected: 50-200 bp (0.5-2% on notional)**
- **On leveraged equity: 2.5-20% ROE**

**Protection buyer (speculation):**

- Carry: -100 to -300 bp cost
- Need spread widening or default
- Win rate: 20-30%
- Avg win: 200-500 bp
- **Positive expectancy if good credit selection**

### 12. Regulation Post-2008


**Dodd-Frank Act changes:**

- **Central clearing:** Most CDS must clear through CCPs
- **Trade reporting:** All trades reported to repositories
- **Margin requirements:** Standardized initial and variation margin
- **Counterparty limits:** Position limits with any dealer

**Benefits:**
- Reduced counterparty risk
- Greater transparency
- Safer market overall

**Costs:**
- Higher collateral requirements
- Less flexibility
- Some basis risk (standardization)

### 13. Your Learning Path


**Phase 1 (Months 1-3): Fundamentals**
- Understand contract mechanics
- Calculate CS01, MTM manually
- Study credit events, settlements
- Paper trade single-name CDS

**Phase 2 (Months 4-6): Hedging**
- Hedge bond portfolios with CDS
- Analyze basis (cash vs CDS)
- Practice spread scenario analysis
- Small real-money hedges

**Phase 3 (Months 7-12): Trading**
- Speculative long/short positions
- Index vs single-name arbitrage
- Curve trades (2s5s, 5s10s)
- Position sizing discipline

**Phase 4 (Year 2+): Advanced**
- Tranche trading
- Capital structure arbitrage
- Structured credit
- Portfolio management

### 14. Final Wisdom


> "CDS are the most powerful credit instruments ever created—and the most dangerous. They allow precise isolation of credit risk, but they also enable catastrophic leverage. The protection buyer pays a modest premium for potentially enormous gains. The protection seller collects steady income until the day they don't, and that one day can erase years of profits and more. Master the mechanics, respect the leverage, understand the counterparty risk, and never forget: you're not trading statistics, you're trading the risk of real companies defaulting. When they do, the losses are not theoretical—they're very, very real."

**Keys to success:**

1. **Understand contract mechanics cold** (premium, settlement, credit events)
2. **Calculate CS01 and MTM** (know your position sensitivity)
3. **Respect leverage** (max 5-10x for sellers)
4. **Use central clearing** (eliminate counterparty risk)
5. **Set stops and targets** (exits before entry)
6. **Diversify reference entities** (correlation kills)
7. **Monitor jump-to-default** (especially as seller)
8. **Never assume basis mean reverts** (can blow out)

**Most critical truth:**

$$
\text{Selling CDS protection} = \text{Collecting pennies in front of steamroller}
$$

Great returns in calm markets, devastating losses in crisis. If you sell protection:
- Size conservatively (assume max loss = notional)
- Diversify obsessively (no single-name >5%)
- Leverage modestly (max 5x)
- Hedge tail risk (buy index protection)
- Have liquidity for margin calls

The traders who survived 2008 followed these rules. Those who didn't are no longer in business. Choose wisely. 🎯📊
