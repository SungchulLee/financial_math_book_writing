# FX Hedging Programs

**Foreign exchange hedging programs** are systematic frameworks that multinational corporations and institutional investors use to manage currency exposure, protecting profit margins and cash flows from adverse exchange rate movements through forward contracts, options, and dynamic hedging strategies.

---

## The Core Insight

**The fundamental idea:**

- Companies with international operations face currency risk
- Exchange rate movements can erase profit margins
- Hedging provides predictable cash flows for planning
- But over-hedging destroys upside and costs money
- Need systematic approach balancing protection and flexibility
- Program design is as important as individual hedge execution

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/fx_hedging_exposure.png?raw=true" alt="fx_hedging_exposure" width="700">
</p>
**Figure 1:** FX exposure profile for a US exporter showing quarterly revenue at risk from EUR/USD movements, with hedged vs. unhedged cash flow volatility demonstrating the stabilizing effect of systematic hedging programs.

**You're essentially deciding: "How much currency risk do we want to bear versus hedge, and at what cost?"**

---

## What Is FX Hedging?

### 1. Transaction Exposure

**Near-term receivables/payables:**

**Definition:** The risk that exchange rate changes affect the value of committed transactions denominated in foreign currencies.

**When you face transaction exposure:**

- You have booked sales/purchases in foreign currency
- Payment due in 30-180 days
- Exchange rate can move unfavorably
- Affects actual cash flows directly
- Most visible and managed first

**Example:**
- US exporter sells machinery to Germany for €1M
- Payment due in 90 days
- Current rate: EUR/USD = 1.10 (expect $1.1M)
- If EUR weakens to 1.05, only receive $1.05M
- **Loss: $50,000 (4.5% margin erosion)**

### 2. Translation Exposure

**Balance sheet effects:**

**Definition:** The accounting impact when consolidating foreign subsidiaries' financial statements into the parent company's reporting currency.

**When you face translation exposure:**

- Own foreign subsidiaries or assets
- Must consolidate to home currency
- Exchange rate changes affect reported equity
- P&L impact on unrealized gains/losses
- Matters for reported EPS and ratios

**Example:**
- US parent owns UK subsidiary worth £100M
- Current rate: GBP/USD = 1.30 ($130M on books)
- GBP weakens to 1.25
- Subsidiary now worth $125M on consolidated balance sheet
- **Translation loss: $5M (hits equity via OCI)**

### 3. Economic Exposure

**Long-term competitiveness:**

**Definition:** The present value impact of exchange rate changes on a company's future cash flows, affecting competitive position and strategic planning.

**When you face economic exposure:**

- Compete with foreign firms in global markets
- Input costs vary with FX rates
- Long-term pricing power affected
- Strategic investment decisions
- Most difficult to hedge, longest time horizon

**Example:**
- US manufacturer competes with Chinese firms
- USD strengthens 20% vs CNY over 2 years
- Chinese competitors now 20% cheaper
- Must cut prices (margin squeeze) or lose market share
- **Economic impact: Multi-year revenue decline**

### 4. Types of Hedges

**Available hedging instruments:**

**Forward contracts:**
- Lock in future exchange rate today
- Obligation to transact at maturity
- No upfront cost (except credit line)
- Eliminates both upside and downside
- Most common for transaction hedging

**FX options:**
- Right (not obligation) to exchange currency
- Upfront premium payment required
- Retains upside, limits downside
- More expensive but flexible
- Used for uncertain exposures

**Currency swaps:**
- Exchange principal and interest in different currencies
- Match assets and liabilities
- Used for long-term balance sheet hedging
- Lower cost than rolling forwards
- Common for financing hedges

**Natural hedges:**
- Match revenues and costs in same currency
- Locate production near customers
- Source inputs in revenue currency
- No direct cost but operational constraints
- Strategic but slow to implement

### 5. Hedge Ratio Decision

**How much to hedge:**

$$
\text{Hedge Ratio} = \frac{\text{Hedged Amount}}{\text{Total Exposure}}
$$

**Common approaches:**

**Static hedge ratios:**
- 100%: Full hedge (no FX risk, no upside)
- 75%: Partial hedge (most common for corporates)
- 50%: Half hedged (balanced approach)
- 0%: Unhedged (full speculation on favorable moves)

**Dynamic hedge ratios:**
- Adjust based on market conditions
- Increase hedging when currency weakening
- Reduce hedging when currency strengthening
- Requires active management and discipline

**Optimal hedge ratio formula:**

$$
h^* = \rho \frac{\sigma_S}{\sigma_F}
$$

Where:
- $h^*$ = Optimal hedge ratio
- $\rho$ = Correlation between spot and futures
- $\sigma_S$ = Volatility of spot position
- $\sigma_F$ = Volatility of hedge instrument

### 6. Layered Hedging

**Rolling hedge structure:**

**The deep insight:** Instead of hedging 100% of one year's exposure at once, layer hedges over time to achieve average rate and reduce timing risk.

**Example program structure:**

```
Q1 2026:  75% hedged (locked in)
Q2 2026:  50% hedged (partial protection)  
Q3 2026:  25% hedged (beginning coverage)
Q4 2026:   0% hedged (no coverage yet)
```

**Each quarter, add hedges for quarters further out:**
- Systematically build hedge coverage
- Dollar-cost average into hedge rates
- Avoid all-or-nothing timing risk
- Management can predict rates with confidence
- Smooth out volatility in hedge P&L

**Formal layering strategy:**

$$
\text{Target Hedge at Time } t: \quad H_t(T) = w(T-t) \times E(T)
$$

Where:
- $H_t(T)$ = Hedge amount at time $t$ for exposure at time $T$
- $w(T-t)$ = Weight function increasing as $T$ approaches
- $E(T)$ = Total exposure at time $T$

**Typical weight function:**
- 12 months out: 0-25% hedged
- 9 months out: 25-50% hedged
- 6 months out: 50-75% hedged
- 3 months out: 75-100% hedged

### 7. Program vs. Ad-Hoc

**Why systematic programs work better:**

**Ad-hoc hedging (reactive):**
- Hedge when CFO gets nervous
- Subject to emotion and market timing
- Inconsistent coverage
- Hard to explain to board
- Often leads to worst outcomes

**Systematic program (proactive):**
- Predefined rules and hedge ratios
- Removes emotion from decision
- Consistent and auditable
- Board approved policy
- Better average outcomes
- Easier performance attribution

**Policy statement example:**

```
FX Hedging Policy:
- Hedge 75% of forecasted USD exposure
- Use 12-month rolling forward contracts
- Layer hedges: 50% 6mo, 25% 12mo out
- Quarterly rebalancing
- Options allowed for uncertain exposures >$5M
- Treasury committee approval for deviations
```

---

## Key Terminology

**Hedge Ratio:**
- Percentage of exposure covered by hedges
- 100% = fully hedged (no FX risk)
- 0% = unhedged (full FX risk)
- Most corporates target 50-80%

**Forward Points:**
- Difference between spot and forward rate
- Reflects interest rate differential
- Can be positive (premium) or negative (discount)
- Affects hedge cost even if no upfront payment

**Roll Cost:**
- Cost of closing and reopening hedge positions
- Occurs when rolling maturity forward
- Includes bid-ask spread and forward points
- Can accumulate over time

**Hedge Effectiveness:**
- How well hedge offsets underlying exposure
- Measured by correlation of hedge P&L to exposure P&L
- >80% is considered effective hedge
- Required for hedge accounting treatment

**Mark-to-Market (MTM):**
- Current value of hedge position
- Can show unrealized gains/losses
- Does not represent final realized P&L
- Creates accounting volatility

**Tenor:**
- Time to maturity of hedge contract
- Short tenor: 1-6 months
- Medium tenor: 6-12 months
- Long tenor: 1+ years

---

## Program Design

### 1. Exposure Forecasting

**Identify what needs hedging:**

**Transaction exposure:**
- Booked orders (contracts signed)
- Forecasted sales/purchases (pipeline)
- Recurring revenues (subscriptions)
- Seasonal patterns (retail, agriculture)

**Steps to forecast:**

1. **Historical analysis:**
   - Review past 3-5 years of FX exposure
   - Identify seasonal patterns
   - Calculate forecast accuracy
   - Adjust for business changes

2. **Bottom-up forecast:**
   - Sales team provides customer forecasts
   - Procurement provides supplier forecasts
   - Treasury consolidates by currency
   - Apply confidence levels (100% booked, 80% probable, etc.)

3. **Stress testing:**
   - Upside scenario (10% higher exposure)
   - Base case (expected)
   - Downside scenario (10% lower exposure)
   - Ensure hedge program works in all scenarios

**Example exposure forecast:**

```
EUR Revenue Forecast (USD millions):
Q1 2026: $25M (100% confidence - booked)
Q2 2026: $23M (80% confidence - pipeline)
Q3 2026: $20M (60% confidence - historical seasonality)
Q4 2026: $22M (50% confidence - early estimate)
```

### 2. Policy Definition

**Create formal hedging policy:**

**Must include:**

1. **Objectives:**
   - Protect profit margins
   - Stabilize cash flows
   - Enable accurate budgeting
   - NOT: speculate or profit from FX

2. **Hedge instruments:**
   - Permitted: Forwards, vanilla options, currency swaps
   - Prohibited: Exotic options, leveraged structures
   - Approval process for non-standard hedges

3. **Hedge ratios:**
   - Target: 75% of forecasted exposure
   - Range: 50-100% allowed
   - By confidence level: 100% booked, 75% pipeline, 50% forecast

4. **Time horizons:**
   - Maximum tenor: 18 months
   - Minimum tenor: 1 month
   - Layering schedule: defined quarterly

5. **Counterparties:**
   - Minimum credit rating: A
   - Maximum exposure per counterparty: 30%
   - Require ISDA agreement

6. **Reporting:**
   - Monthly hedge position report
   - Quarterly effectiveness testing
   - Annual policy review

7. **Governance:**
   - Treasury executes per policy
   - CFO approves deviations
   - Board audit committee oversight

### 3. Instrument Selection

**Choose right tool for each exposure:**

**Use forwards when:**
- Exposure is certain (booked orders)
- Cost minimization is priority
- Can tolerate no upside participation
- Short to medium term (< 1 year)

**Use options when:**
- Exposure is uncertain (forecasted)
- Want to retain upside potential
- Budget can afford premium
- Strategic exposure (M&A, large project)

**Use collars when:**
- Want option-like protection
- Premium budget is zero
- Willing to cap upside to pay for downside protection
- Common for commodities and FX

**Use currency swaps when:**
- Long-term exposure (>1 year)
- Match asset/liability in foreign currency
- Cheaper than rolling forwards
- Used for loans, bonds, long-term contracts

### 4. Hedge Accounting

**Qualify for hedge accounting to reduce volatility:**

**Requirements (under ASC 815 / IFRS 9):**

1. **Formal documentation:**
   - Must document hedge relationship at inception
   - Specify hedged item and hedging instrument
   - State risk management objective

2. **Effectiveness testing:**
   - Demonstrate high correlation (>80%)
   - Test prospectively and retrospectively
   - Quarterly assessment

3. **Types of hedge accounting:**
   - **Cash flow hedge:** For forecasted transactions
     - Defer gains/losses to OCI
     - Release to P&L when forecasted transaction affects earnings
   - **Fair value hedge:** For firm commitments or assets
     - Recognize hedge and hedged item on P&L
     - Offsets immediately
   - **Net investment hedge:** For foreign subsidiaries
     - Defer to CTA (cumulative translation adjustment)

**Benefits:**
- Matches hedge P&L with underlying exposure
- Reduces earnings volatility
- Better reflects economic reality
- Requires additional work and documentation

---

## Program Implementation

### 1. Rolling Forward Program

**Most common corporate structure:**

**Program design:**

```
Month 1:  Hedge 50% of Month 4 exposure
Month 2:  Hedge 25% more of Month 5 exposure (total 75%)
Month 3:  Hedge 25% more of Month 6 exposure (total 100%)
Repeat monthly
```

**Advantages:**
- Systematic dollar-cost averaging
- No all-or-nothing timing risk
- Predictable and consistent
- Easy to explain and defend
- Audit trail is clear

**Execution steps:**

1. **Monthly exposure update:**
   - Get updated forecast from sales/procurement
   - Compare to previous forecast
   - Adjust hedge targets if needed

2. **Calculate hedge amount:**
   - Current exposure for each future month
   - Multiply by target hedge ratio
   - Subtract already-hedged amount
   - Result = new hedge amount needed

3. **Execute hedges:**
   - Get quotes from 3 banks
   - Use limit orders to capture best rates
   - Execute systematically (same day each month)
   - Document all trades

4. **Update hedge book:**
   - Record all positions in system
   - Mark-to-market daily
   - Report to CFO weekly
   - Review with committee quarterly

### 2. Option Collar Program

**For companies wanting asymmetric protection:**

**Structure:**
- Buy OTM put (protection from downside)
- Sell OTM call (give up upside, fund put)
- Net cost = $0 or small premium

**Example for EUR/USD exposure:**

Current spot: 1.10

- **Buy EUR/USD put at 1.07** (downside protection)
  - Cost: 2.5% premium
- **Sell EUR/USD call at 1.14** (cap upside)
  - Receive: 2.5% premium
- **Net cost: $0** (zero-cost collar)

**Payoff:**
- If EUR/USD falls below 1.07 → protected (put ITM)
- If EUR/USD stays 1.07-1.14 → neutral (both OTM)
- If EUR/USD rises above 1.14 → capped (call ITM)

**When to use collars:**
- Uncertain exposure (forecasted, not booked)
- Zero budget for hedging premium
- Want downside protection but can cap upside
- Volatile currency pairs

### 3. Participate Forward

**Ratio forward structure:**

**For companies wanting upside participation:**

**Structure:**
- Hedge 100% with forward
- Add ratio of OTM options to participate in favorable moves

**Example:**

Hedge $10M EUR receivable:
- Sell $10M forward at 1.10 (lock in rate)
- Buy $5M EUR call option at 1.12 (50% participation)

**Payoff:**
- If EUR/USD falls → fully protected at 1.10
- If EUR/USD rises above 1.12 → participate 50% of upside
- Premium cost: ~1-2% of notional

**When to use:**
- Want guaranteed floor
- Budget allows for some premium
- Bullish bias on currency
- Used by exporters when domestic currency weakening

### 4. Dynamic Hedging

**Adjust hedge ratio based on signals:**

**Rule-based approach:**

**Increase hedging (toward 100%) when:**
- Currency moving unfavorably (momentum)
- Technical break of support/resistance
- Volatility increasing
- Exposure forecast increasing

**Decrease hedging (toward 50%) when:**
- Currency moving favorably
- Strong technical support
- Volatility decreasing
- Exposure forecast decreasing

**Example rules:**

```python
IF EUR/USD < 1.08 AND 20-day trend down:
    Target hedge ratio = 90%
ELIF EUR/USD > 1.12 AND 20-day trend up:
    Target hedge ratio = 60%
ELSE:
    Target hedge ratio = 75%
```

**Challenges:**
- Requires active monitoring
- Emotional discipline needed
- Can add whipsaw costs
- Board may question "timing" decisions
- Best for sophisticated treasury teams

---

## Common Mistakes

### 1. Under-Hedging

**Too little protection:**

- **Mistake:** Only hedge 25-50% of exposure to "participate in upside"
- **Why it fails:** One large adverse move wipes out multiple years of FX gains
- **Fix:** Hedge 75%+ of certain exposure, use options for uncertain
- **Real cost:** Full exposure to tail risk, business plan uncertainty

**Example:**
- Company hedges only 40% of €50M exposure
- EUR weakens from 1.10 to 1.00 (10% move)
- Hedged €20M at 1.10: no loss ($22M realized)
- Unhedged €30M at 1.00: $3M loss (€30M × 0.10)
- **Total loss: $3M on $55M revenues (5.5% margin hit)**

### 2. Over-Hedging

**More protection than exposure:**

- **Mistake:** Hedge 100% of optimistic forecast that doesn't materialize
- **Why it fails:** End up with naked hedge (speculation), P&L from hedge with no offset
- **Fix:** Use layered approach, hedge probability-adjusted exposure
- **Real cost:** Create FX exposure where none existed, opposite of intent

**Example:**
- Company forecasts €40M revenue, hedges 100%
- Actual revenue: €30M (customer delayed order)
- €10M hedge has no underlying exposure
- If EUR rallies from 1.10 to 1.15 (4.5% move)
- **Hedge loss: €10M × 0.05 = $500K with no revenue to offset**

### 3. Hedging Translation

**Wrong exposure to hedge:**

- **Mistake:** Use forwards/options to hedge balance sheet translation
- **Why it fails:** Creates realized losses hedging unrealized losses, double exposure
- **Fix:** Generally don't hedge translation (or use net investment hedge)
- **Real cost:** Pay transaction losses to offset accounting losses that may reverse

**Why translation hedges backfire:**
1. Translation losses are **unrealized** (OCI, not P&L)
2. Hedge losses are **realized** (actual cash costs)
3. Translation reverses if FX normalizes
4. Hedge losses are permanent
5. **Result: Convert paper loss into real cash loss**

**Exception: Net investment hedge**
- Hedge long-term subsidiary investment (not quarterly translation)
- Borrow in foreign currency to match asset
- Or use long-dated FX instruments
- Must qualify for hedge accounting
- Used by multinationals with large permanent foreign investments

### 4. Ignoring Forward Points

**Forget interest rate impact:**

- **Mistake:** Only look at spot rate, ignore forward points
- **Why it fails:** Forward points can be 2-5% of notional, erode hedge effectiveness
- **Fix:** Calculate all-in hedge cost including forward points
- **Real cost:** "Locked in" rate is actually worse than appears

**Example:**

Hedge EUR/USD exposure:
- Spot rate: 1.1000
- 12-month forward points: -0.0200 (negative carry)
- **Forward rate: 1.0800** (you get 2% less than spot)

**Economic impact:**
- If spot stays at 1.10 for 12 months
- Unhedged: Receive $1.10 per EUR
- Hedged: Receive $1.08 per EUR
- **Hedge cost: 2% of notional** (opportunity cost)

**This happens when:**
- Foreign currency has higher interest rate than home currency
- Forward points reflect this interest rate differential
- You "pay" the difference to lock in rate
- Common when hedging EM currencies vs USD

### 5. Emotional Hedging

**React to market moves:**

- **Mistake:** Increase hedges after currency already moved unfavorably (panic)
- **Why it fails:** Chase bad rates, add hedges at worst time, destroy average rate
- **Fix:** Stick to systematic program, ignore short-term moves
- **Real cost:** Buy high, sell low mentality, poor average execution prices

**Typical pattern:**

```
EUR/USD at 1.15: "No need to hedge, good rate!"
EUR/USD at 1.10: "Still okay, wait for better"
EUR/USD at 1.05: "PANIC! Hedge everything now!"
EUR/USD at 1.08: "Why did we hedge at the low?"
```

**Result:**
- Hedge 0% when EUR at 1.15 (should have hedged)
- Hedge 100% when EUR at 1.05 (terrible rate)
- Average hedge rate: 1.06 (vs could have been 1.12)
- **Gave up 5% by timing hedges emotionally**

### 6. Complex Structures

**Over-engineer the hedge:**

- **Mistake:** Use exotic options (barriers, digitals) to reduce premium cost
- **Why it fails:** Complexity obscures risks, knock-out events create gaps, hard to explain
- **Fix:** Use vanilla forwards and options only, transparent structures
- **Real cost:** Unexpected losses when exotic features trigger, audit/compliance issues

**Example of complex structure gone wrong:**

**Knock-out forward:**
- Forward at 1.10, but knocks out if EUR/USD hits 1.15
- Saves 50% of forward points (looks attractive)
- EUR rallies to 1.15 briefly (barrier hit)
- Forward cancelled (knocked out), no hedge in place
- EUR then falls to 1.05 (10% adverse move)
- **Result: Unhedged at worst time, $5M loss on $50M exposure**

---

## Best vs. Worst Case

### 1. Best Case: Success

**Layered rolling forward program:**

**Setup:**
- US exporter with €100M annual revenue
- Layer forwards: 25% each quarter rolling forward
- EUR/USD at 1.12 when program starts
- Target: 75% hedged at all times

**Scenario 1: EUR weakens gradually to 1.02 over year**

**Without hedge:**
- Q1: €25M at 1.10 = $27.5M
- Q2: €25M at 1.08 = $27.0M
- Q3: €25M at 1.05 = $26.25M
- Q4: €25M at 1.02 = $25.5M
- **Total: $106.25M (was budgeted at $112M)**
- **Loss: $5.75M vs budget (5.1% margin hit)**

**With 75% layered hedge:**
- Locked in average rate of 1.105 across quarters (dollar-cost averaging)
- 75% of €100M = €75M hedged at 1.105
- 25% unhedged receives average 1.063
- **Hedged: €75M × 1.105 = $82.875M**
- **Unhedged: €25M × 1.063 = $26.575M**
- **Total: $109.45M**
- **Loss vs budget: $2.55M (2.3% margin hit)**
- **Savings vs unhedged: $3.2M**

**Benefits realized:**
- Protected 60% of FX loss
- Stable and predictable outcomes
- No timing risk (dollar-cost averaged)
- Budget accuracy maintained

### 2. Worst Case: Failure

**Over-hedged wrong direction:**

**Setup:**
- US exporter hedges 100% of forecast
- Overly optimistic forecast (€120M actual €80M)
- Hedges at 1.08 thinking EUR will weaken
- EUR actually strengthens to 1.18

**Reality:**
- Actual revenue: €80M (not €120M)
- Hedged: €120M at 1.08
- **Over-hedged by: €40M**

**Outcome:**
- Actual €80M received: €80M × 1.18 = $94.4M (beneficial spot)
- Hedge requires delivery of €120M at 1.08
- Must buy additional €40M in market at 1.18
- **Hedge loss: €40M × (1.18 - 1.08) = $4M loss**

**Final P&L:**
- Revenues: $94.4M
- Hedge loss: -$4M
- **Net: $90.4M**
- **vs. unhedged: $94.4M**
- **Loss: $4M (4.4% of revenue) due to over-hedging**

**Lessons:**
- Over-hedging turns you into speculator
- Hedge probability-adjusted forecast, not best case
- Layer hedges as visibility improves
- Leave room for forecast errors

---

## Risk Management Rules

### 1. Hedge Ratio Limits

**By exposure type:**

$$
\begin{align*}
\text{Booked orders:} & \quad 100\% \text{ hedge allowed} \\
\text{Pipeline (high confidence):} & \quad 75\% \text{ hedge max} \\
\text{Forecast (medium confidence):} & \quad 50\% \text{ hedge max} \\
\text{Strategic (low confidence):} & \quad 25\% \text{ hedge max}
\end{align*}
$$

**Portfolio limits:**
- Total hedge notional < 110% of forecasted exposure
- Any single currency pair < 20% of total hedge book
- Maximum tenor: 18 months
- Minimum liquidity: $10M daily volume in currency pair

### 2. Counterparty Risk

**Credit limits per bank:**

$$
\text{Max Exposure}_{\text{bank}} = \frac{\text{Total Hedge Book}}{N_{\text{banks}}} \leq 30\%
$$

**Requirements:**
- Minimum 3 counterparty banks
- Each must have credit rating ≥ A
- ISDA and CSA agreements in place
- Daily mark-to-market on all positions
- Collateral posting for negative MTM > $5M

### 3. Monitoring & Reporting

**Daily:**
- Mark-to-market all hedge positions
- Check for significant moves (>2% in any pair)
- Monitor upcoming maturities (next 30 days)
- Alert CFO if MTM loss exceeds $1M

**Weekly:**
- Update hedge effectiveness ratios
- Compare hedge book to current exposure forecast
- Identify upcoming hedge execution needs
- Report to CFO: position summary and MTM P&L

**Monthly:**
- Full hedge program review
- Execute new hedges per program schedule
- Update forecasts and adjust if needed
- Prepare board report

**Quarterly:**
- Formal hedge effectiveness testing (for accounting)
- Review program performance vs. unhedged
- Stress test hedge book (±10% FX move)
- Present to audit committee

### 4. Program Metrics

**Track these KPIs:**

**Hedge effectiveness:**

$$
\text{Effectiveness} = \frac{\text{Cov}(\Delta \text{Hedge P\&L}, \Delta \text{Exposure P\&L})}{\text{Var}(\Delta \text{Exposure P\&L})}
$$

**Target: > 80%**

**Average hedge rate vs. average spot rate:**

$$
\text{Rate Performance} = \frac{\text{Avg Hedge Rate} - \text{Avg Spot Rate}}{\text{Avg Spot Rate}}
$$

**Benchmark: Within ±2% annually**

**Hedge cost:**

$$
\text{Hedge Cost} = \frac{\text{Total Premium Paid} + \text{Forward Points}}{\text{Total Notional Hedged}}
$$

**Target: < 1% annually for forward programs**

**Forecast accuracy:**

$$
\text{Forecast Error} = \frac{|\text{Actual Exposure} - \text{Forecasted Exposure}|}{\text{Forecasted Exposure}}
$$

**Target: < 10% quarterly**

---

## Real-World Examples

### 1. Apple Inc. (Tech Giant)

**Program characteristics:**

- Multiple foreign currencies (EUR, JPY, GBP, CNY, etc.)
- Massive exposure: >$100B annual foreign revenue
- Uses layered forward program
- 75-90% hedge ratios for forecasted sales
- Layers hedges up to 12 months forward

**Public disclosures (Form 10-K):**
- "Derivatives with a total notional amount of $102.8B outstanding"
- "Effective hedge of forecasted foreign currency revenue"
- Uses options for strategic M&A and long-term projects

**Performance:**
- Reduced FX impact on EPS by 70-80% vs. unhedged
- Stable gross margins despite FX volatility
- Clear audit trail and board-approved policy

### 2. Small Exporter ($50M)

**Setup:**
- US company exporting industrial equipment to Europe
- €15M annual revenue (30% of total)
- CFO worried about EUR weakness

**Initial approach (failed):**
- Ad-hoc hedging based on "feel"
- Hedged 100% when EUR at 1.05 (after already falling)
- EUR recovered to 1.12
- Gave up 7% of revenue to hedge losses

**Improved program:**
- Implemented layered forward program: 50% hedged 6 months out, add 25% every 3 months
- Result: Average rate of 1.09 vs. spot range of 1.05-1.12
- Budget now predictable within 2-3%
- CFO sleeps better!

### 3. UK Importer (Post-Brexit)

**Setup:**
- UK retailer importing from China (USD-denominated)
- $200M annual imports
- GBP/USD volatility increased post-Brexit

**Crisis event:**
- Brexit vote (June 2016): GBP crashed 15% overnight
- $200M imports suddenly cost £150M instead of £130M
- **Unhedged cost: £20M additional** (entire annual profit)

**Program implemented:**
- 12-month rolling forward program
- 80% hedge ratio (high confidence in import forecast)
- Zero-cost collars for strategic flexibility
- Saved company from bankruptcy

**Lessons:**
- Systematic program prevents catastrophic losses
- Political events create fat-tail FX risk
- Cost of hedging < cost of one major adverse event

### 4. Auto Manufacturer (Japan)

**Setup:**
- Japanese automaker with US manufacturing
- Yen costs, dollar revenues (natural hedge)
- But still exposed to JPY/USD swings

**Program:**
- Net exposure calculated after natural hedges
- Forward program for residual exposure only
- Options for strategic pricing decisions
- **Result: Hedging cost cut by 60% vs. gross exposure approach**

**Key insight:**
- First use natural hedges (operational approach)
- Only hedge residual after netting
- Saved tens of millions in hedging costs
- More efficient program

---

## Practical Steps

### 1. Program Startup

**Initial setup (first 3 months):**

1. **Exposure assessment:**
   - Conduct full audit of FX exposures by currency
   - Categorize: transaction, translation, economic
   - Quantify: Dollar amount and probability of each exposure
   - Historical analysis: 3-5 years of actual FX impact on P&L

2. **Policy creation:**
   - Draft FX hedging policy (see Program Design section)
   - Get CFO and board approval
   - Establish governance (who approves what)
   - Set hedge ratio targets and limits

3. **Infrastructure setup:**
   - Select 3-5 counterparty banks
   - Negotiate ISDA agreements and credit lines
   - Implement treasury management system (TMS)
   - Train staff on execution and reporting

4. **Initial hedge execution:**
   - Start with conservative 50% hedge ratio
   - Use forwards only (simplest)
   - Layer: Hedge 3, 6, 9 months forward
   - Build up coverage over first quarter

### 2. Monthly Execution

**Systematic process:**

**Day 1-5: Forecast update**
- Sales provides updated revenue forecast by currency
- Procurement provides updated import forecast
- Treasury consolidates and calculates net exposure
- Compare to last month, note significant changes

**Day 6-10: Hedge calculation**
- For each future month, calculate: `Target hedge - Current hedge = New hedge needed`
- Prepare execution plan: currencies, amounts, tenors
- Get quotes from all counterparty banks
- Prepare execution approval memo for CFO

**Day 11-15: Execution**
- Execute new hedges per policy
- Use limit orders to capture best rates
- Confirm all trades with counterparties
- Update hedge book in TMS

**Day 16-31: Monitoring**
- Daily MTM tracking
- Update weekly hedge report
- Alert CFO of any significant MTM moves
- Prepare for next month's cycle

### 3. Quarterly Review

**Formal program assessment:**

**Hedge effectiveness testing:**
- Calculate regression of hedge P&L vs. exposure P&L
- Must be >80% correlation for hedge accounting
- If fails, investigate: Wrong hedge instrument? Over/under hedged?

**Performance attribution:**
- Compare hedged result vs. unhedged result
- Calculate hedge cost (forward points + premium)
- Present to CFO: "Hedge saved/cost $X vs. unhedged"
- Explain any program deviations

**Forecast accuracy:**
- Compare actual exposure to forecasted
- Calculate forecast error percentage
- If >10% error, dig into root cause
- Improve forecasting process if needed

**Policy compliance:**
- Check all hedge ratios within limits
- Verify counterparty limits not breached
- Confirm all hedges documented properly
- Audit new hedges vs. policy approvals

**Board reporting:**
- One-page summary: exposures, hedges, MTM, performance
- Highlight any issues or deviations
- Recommend policy changes if needed

### 4. Annual Strategy

**Strategic review:**

**Program effectiveness:**
- Full-year performance: Hedged vs. unhedged P&L
- Calculate total hedge cost as % of revenue
- Compare to peer companies (if available)
- Decision: Continue, modify, or overhaul program?

**Policy updates:**
- Review hedge ratios: Still appropriate?
- Tenor changes needed?
- New currencies to add?
- Instrument mix (forwards vs. options)?
- Update for business changes (new markets, M&A)

**Forecast improvement:**
- Root cause analysis of forecast misses
- Implement better forecasting tools/process
- Consider scenario-based forecasting
- Engage business units for bottom-up inputs

**System upgrades:**
- Evaluate TMS functionality
- Consider automation opportunities
- Enhance reporting capabilities
- Integrate with ERP for real-time exposure data

### 5. Crisis Management

**Handling extreme events:**

**When major FX shock occurs (>5% move overnight):**

1. **Immediate assessment (same day):**
   - Calculate immediate MTM impact on hedge book
   - Estimate impact on unhedged exposure
   - Net the two: What's the actual P&L hit?
   - Alert CFO and prepare brief for CEO/Board

2. **Program review (next day):**
   - Is current hedge ratio still appropriate?
   - Need to increase/decrease hedging immediately?
   - Any hedges about to expire that need rolling?
   - Check counterparty credit risk (bank stress?)

3. **Communication (first week):**
   - Prepare investor FAQ: How are we protected?
   - Update guidance if material impact
   - Press release if public company and material
   - Internal communication: Reassure team hedge program working

4. **Medium-term response (first month):**
   - Assess if "new normal" in FX rates
   - Revise forecasts for new rate regime
   - Adjust budget/guidance for remainder of year
   - Consider program modifications (hedge ratio, tenor)

5. **Long-term adaptation (first quarter):**
   - Evaluate strategic responses: Pricing, sourcing, natural hedges
   - Consider longer-term hedging (>12 months)
   - Update risk tolerance and policy if needed
   - Implement lessons learned

---

## Final Wisdom

> "FX hedging is not about making money; it's about not losing money unexpectedly. A good FX hedge program is one you never think about because it quietly does its job of stabilizing cash flows and protecting margins. The moment you start 'hoping' for favorable moves or 'regretting' hedge costs, you've turned hedging into speculation. Stick to your program, hedge systematically, and sleep better at night knowing one less thing can blow up your quarter."

**Key to success:**

- Define clear objectives (protection, not profit)
- Systematic program, not ad-hoc decisions
- Appropriate hedge ratios (75% good starting point)
- Layer hedges to average rates over time
- Use simple instruments (forwards first)
- Monitor and report religiously
- Stick to the program in good times and bad
