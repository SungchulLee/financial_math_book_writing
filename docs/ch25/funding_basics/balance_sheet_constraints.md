# Balance Sheet Constraints

**Balance sheet constraints** are regulatory and economic limitations on bank and broker-dealer leverage, capital, and liquidity that restrict their ability to intermediate trades, provide financing, and make markets.

---

## The Core Insight

**The fundamental idea:**

- Post-2008, strict regulations on financial institutions
- Capital requirements, leverage ratios, liquidity rules
- Limits on balance sheet expansion
- Makes certain activities uneconomical
- Affects market liquidity and trading costs
- Creates periodic funding stress (quarter-ends)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/balance_sheet_constraints.png?raw=true" alt="balance_sheet_constraints" width="700">
</p>
**Figure 1:** Evolution of broker-dealer balance sheets showing post-2008 regulatory compression, with assets declining from $4 trillion to $3 trillion despite growing markets, illustrating the impact of leverage ratio and capital requirements.

**You're essentially asking: "What limits prevent banks from expanding their trading and financing activities, and how does this affect markets?"**

---

## Why Balance Sheet Matters

### 1. Pre-Crisis vs Post-Crisis

**Pre-2008:**
- Banks levered 30-40x
- Minimal capital requirements
- Easy balance sheet expansion
- Market-making profitable
- Abundant repo financing

**Post-2008:**
- Leverage capped at ~10-12x
- Basel III capital requirements
- Supplementary Leverage Ratio (SLR)
- Liquidity Coverage Ratio (LCR)
- Net Stable Funding Ratio (NSFR)

**Result:**
- Constrained intermediation
- Higher trading costs
- Periodic funding stress
- Less market-making

### 2. Key Regulations

**Basel III (2010-2019 implementation):**

**Risk-weighted capital:**

$$
\text{Tier 1 Capital Ratio} = \frac{\text{Tier 1 Capital}}{\text{Risk-Weighted Assets}} \geq 6\%
$$

**Supplementary Leverage Ratio:**

$$
\text{SLR} = \frac{\text{Tier 1 Capital}}{\text{Total Leverage Exposure}} \geq 3\%
$$

**For US G-SIBs: ≥ 5%**

**Liquidity Coverage Ratio:**

$$
\text{LCR} = \frac{\text{High-Quality Liquid Assets}}{\text{Net Cash Outflows (30 days)}} \geq 100\%
$$

**Net Stable Funding Ratio:**

$$
\text{NSFR} = \frac{\text{Available Stable Funding}}{\text{Required Stable Funding}} \geq 100\%
$$

### 3. Economic Impact

**Activities constrained:**

- **Repo financing:** Balance sheet intensive
- **Client facilitation:** Inventory holding costly
- **Market-making:** Less capital for positions
- **Derivatives clearing:** Central clearing consumes balance sheet

**Market consequences:**

- Wider bid-ask spreads (10-30% wider post-crisis)
- Reduced liquidity during stress
- Higher funding costs (repo rates elevated)
- Quarterly/year-end spikes (window dressing)

### 4. G-SIB Surcharge

**Global Systemically Important Banks:**

Additional capital surcharge based on size, complexity, interconnectedness:

$$
\text{Total Requirement} = \text{Basel III Minimum} + \text{G-SIB Surcharge}
$$

**G-SIB buckets:**
- Bucket 1: +1.0% capital
- Bucket 2: +1.5% capital
- Bucket 3: +2.0% capital
- Bucket 4: +2.5% capital
- Bucket 5: +3.5% capital (highest)

**US G-SIBs (2024):**
- JPMorgan: Bucket 4 (2.5%)
- Bank of America, Citigroup: Bucket 3 (2.0%)
- Goldman Sachs, Morgan Stanley: Bucket 2 (1.5%)

**Creates incentive to reduce size and complexity**

### 5. Leverage Exposure Calculation

**What counts as leverage:**

$$
\text{Leverage Exposure} = \text{On-Balance Sheet} + \text{Off-Balance Sheet} + \text{Derivatives}
$$

**Key inclusions:**
- Cash and securities (full notional)
- Repo and reverse repo (gross, not net!)
- Derivatives (potential future exposure)
- Securities financing transactions
- Loan commitments

**Example bank:**
- Assets: $\$1 trillion$
- Repo assets: $\$200 billion$
- Derivatives exposure: $\$100 billion$
- **Total leverage exposure: $\$1.3 trillion$**

**Required Tier 1 capital (5% SLR):**

$$
\$1.3T \times 0.05 = \$65 \text{ billion}
$$

### 6. Cost of Capital

**Opportunity cost:**

Banks must hold expensive equity capital:

$$
\text{Cost of Equity} \approx 10\text{-}15\% \text{ annually}
$$

**Return on Equity (ROE) requirement:**

$$
\text{ROE} = \frac{\text{Net Income}}{\text{Equity Capital}} \geq \text{Cost of Equity}
$$

**For activity to be worthwhile:**

$$
\frac{\text{Activity Profit}}{\text{Capital Consumed}} \geq 10\text{-}15\%
$$

**Example:**
- Repo transaction: $\$100M$ for 1 day
- Capital charge: $\$5M$ (5% SLR)
- Profit: $\$100$ (1 bp spread)

**ROE:**

$$
\text{ROE} = \frac{\$100 \times 365}{\$5M} = 0.73\%
$$

**Way below cost of capital! Uneconomic.**

### 7. Reporting Window Dressing

**Quarter-end and year-end:**

Banks temporarily shrink balance sheets:
- Reduce repo book (don't roll positions)
- Wind down derivatives (if possible)
- Convert illiquid to liquid assets (meet LCR)

**Impact on markets:**
- Repo rates spike (scarce funding)
- Bid-ask spreads widen (less market-making)
- Settlement fails increase (reduced intermediation)

**Example (Dec 31, 2019):**
- Normal repo rate: 2.5%
- Year-end spike: 5.0% (250 bp jump!)
- Dealer balance sheets fell $\$200 billion in last week

---

## Specific Constraints

### 1. Supplementary Leverage Ratio (SLR)

**Most binding constraint:**

$$
\text{SLR} = \frac{\text{Tier 1 Capital}}{\text{Total Leverage Exposure}} \geq 5\% \text{ (US G-SIBs)}
$$

**Why it binds:**
- No risk-weighting (treats Treasuries = Corporate bonds)
- Includes low-risk activities (repo, client clearing)
- Gross exposure (no netting)

**Example impact:**

**Activity:** Client reverse repo (borrow $\$100M$ Treasuries)

**Leverage exposure:** $\$100M$ (full notional)

**Capital required:** $\$100M \times 5\% = \$5M$

**Cost (10% ROE target):** $\$500,000$ annually

**Revenue from 1 bp spread:** $\$100M \times 0.01\% = \$10,000$

**Net:** -$\$490,000$ loss!

**Economically impossible to offer.**

### 2. Liquidity Coverage Ratio (LCR)

**30-day stress test:**

$$
\text{LCR} = \frac{\text{HQLA}}{\text{Net Cash Outflows (30 days)}} \geq 100\%
$$

**High-Quality Liquid Assets (HQLA):**
- Level 1: Cash, Treasuries, reserves (100% credit)
- Level 2A: Agency MBS, high-rated bonds (85% credit)
- Level 2B: Lower-rated corporates, equities (50% credit)

**Net Cash Outflows:**
- Assumed deposit runoff (stable = 3%, less stable = 10%)
- Wholesale funding maturity (100% if unsecured)
- Committed credit lines (drawdown assumptions)

**Constraint impact:**
- Must hold more cash/Treasuries (low-yielding)
- Reduces profitability
- Limits matched-book repo (cash outflow in stress)

### 3. Net Stable Funding Ratio (NSFR)

**Long-term structural liquidity:**

$$
\text{NSFR} = \frac{\text{Available Stable Funding}}{\text{Required Stable Funding}} \geq 100\%
$$

**Available Stable Funding (ASF):**
- Retail deposits: 90-95% credit
- Long-term wholesale funding: 50-100%
- Short-term wholesale: 0-50%

**Required Stable Funding (RSF):**
- Cash: 0%
- Treasuries: 5%
- Agency MBS: 10%
- Corporates: 15%
- Loans: 85%

**Constraint impact:**
- Favors deposits over wholesale funding
- Makes long-term illiquid assets expensive
- Affects term repo economics

### 4. Risk-Based Capital Requirements

**Risk-weighting by asset class:**

$$
\text{RWA} = \sum \text{Exposure}_i \times \text{Risk Weight}_i
$$

**Risk weights:**
- Cash: 0%
- Treasuries: 0%
- Agency MBS: 20%
- Corporate bonds (AA): 20%
- Corporate bonds (BBB): 50%
- High-yield bonds: 100%
- Equities: 100-400%

**Example portfolio:**
- $\$100M$ Treasuries: RWA = $0
- $\$100M$ IG corporates: RWA = $\$50M$ (50% weight)
- $\$100M$ equities: RWA = $\$100M$ (100% weight)
- **Total RWA: $\$150M$**

**Required capital (8% minimum):**

$$
\text{Capital} = \$150M \times 0.08 = \$12M
$$

### 5. Derivatives Capital

**SA-CCR (Standardized Approach for Counterparty Credit Risk):**

Complex calculation including:
- Replacement Cost (current mark-to-market)
- Potential Future Exposure (volatility-based)
- Netting benefits (limited)
- Collateral offsets (partial)

**Example:**
- $\$1 billion notional interest rate swap
- Potential Future Exposure: 0.5% × $\$1B = $\$5M$
- Current exposure: -$\$2M$ (in your favor)
- **Capital charge: ~$\$3M$**

**More expensive than pre-crisis (was ~$\$1M$)**

### 6. Client Clearing Costs

**Central clearing (Dodd-Frank requirement):**

Banks clear derivatives for clients:
- Post initial margin to CCP
- Post variation margin daily
- Guarantee client trades

**Balance sheet impact:**
- Initial margin: Asset on balance sheet
- Leverage exposure: Full notional
- Capital charge: Based on SA-CCR

**Economics:**
- Capital consumed: High
- Revenue: Low (tight competition)
- Many banks exited client clearing

### 7. Securities Financing Transactions

**Repo and securities lending:**

Gross accounting (no netting):
- Lend $\$100M$ → $\$100M$ asset
- Borrow $\$100M$ → $\$100M$ liability
- **Leverage exposure: $\$200M$ (not $0!)**

**Capital required (5% SLR):**

$$
\$200M \times 0.05 = \$10M
$$

**Makes matched-book repo uneconomic:**
- Tight spreads (1-5 bps)
- High capital charge
- ROE below cost of capital

**Result: Dealers reduced repo intermediation**

---

## Market Implications

### 1. Reduced Liquidity

**Empirical evidence:**

**Treasury market:**
- Bid-ask spreads: 0.5 bp (pre-crisis) → 1.0 bp (post-crisis)
- Market depth: Down 30-50%
- Price impact: 2-3× larger per trade

**Corporate bonds:**
- Bid-ask spreads: Up 50-100%
- Dealer inventory: Down 70%
- Liquidity premium: Up 20-30 bps

**Derivatives:**
- Clearing costs up 40-60%
- Less dealer facilitation
- Wider CDS spreads

### 2. Periodic Stress

**Quarter-end and year-end spikes:**

**Repo rates:**
- Normal: SOFR = 2.5%
- Quarter-end: SOFR = 3.5% (100 bp spike)
- Year-end: SOFR = 5.0% (250 bp spike)

**Settlement fails:**
- Normal: $\$5-10 billion daily
- Quarter-end: $\$50-100 billion daily

**Why:**
- Banks reduce balance sheets for reporting
- Less intermediation capacity
- Funding scarce

### 3. Central Bank Intervention

**Federal Reserve responses:**

**Standing Repo Facility (SRF):**
- Fed lends cash against Treasuries
- Rate: SOFR + 25 bps
- Backstop for funding stress

**Treasury buyback program:**
- Fed buys Treasuries to inject reserves
- Reduces balance sheet constraint

**Temporary SLR exemption (2020-2021):**
- Excluded Treasuries and reserves from leverage ratio
- Eased constraints during COVID
- Expired March 2021

### 4. Activity Migration

**Shift to non-banks:**

- Hedge funds: More Treasury market-making
- Private credit: Direct lending (bypass banks)
- Money funds: Direct repo lending
- Electronic platforms: Replace dealer intermediation

**Concerns:**
- Non-banks less regulated
- Potential instability
- Different risk management

### 5. Cost Pass-Through

**Higher client costs:**

- Wider bid-ask spreads
- Higher derivatives clearing fees
- Repo rate spikes at quarter-ends
- Less favorable execution

**Example:**
- Large client trade: $\$100M$ corporate bonds
- Pre-crisis: 10 bp spread
- Post-crisis: 20-30 bp spread
- **Extra cost: $\$100-200k per trade**

### 6. Product Innovation

**Capital-efficient alternatives:**

**Synthetic prime brokerage:**
- Use derivatives instead of cash financing
- Lower balance sheet consumption

**Sponsored repo:**
- Non-bank clears with Fed directly
- Bank earns fee, no balance sheet hit

**Total return swaps:**
- Derivative replicates financing
- More capital-efficient than repo

### 7. Market Structure Changes

**Fragmentation:**
- Less centralized dealer intermediation
- More peer-to-peer (hedge fund to hedge fund)
- Electronic platforms growing
- Multiple liquidity pools

**Impact:**
- Price discovery harder
- Execution complexity
- But: Technology improving efficiency

---

## Common Mistakes

**Pitfalls to avoid:**

### 1. Ignoring Quarter-End Effects

**Mistake:** Don't plan for periodic stress

**Why it fails:** Surprised by funding cost spikes

**Example:**
- Levered portfolio funded via overnight repo
- December 31st year-end approaching
- Repo rate spikes 2.5% → 5.0%
- **Funding cost doubles overnight!**

**Fix:**
- Secure term funding over quarter/year-ends
- Reduce leverage before reporting dates
- Budget for higher costs

### 2. Underestimating Capital Costs

**Mistake:** Compare pre-crisis to post-crisis economics

**Why it fails:** Activities now uneconomic

**Example:**
- Market-making in IG corporate bonds
- Pre-crisis: 5 bp spread, 30x leverage, 15% ROE
- Post-crisis: 5 bp spread, 10x leverage, 5% ROE
- **Below cost of capital, unprofitable**

**Fix:**
- Model capital charges accurately
- Require wider spreads
- Focus on high-margin activities

### 3. Assuming Infinite Liquidity

**Mistake:** Expect dealers to always make markets

**Why it fails:** Dealers constrained

**Example:**
- Large bond sale order ($\$500M$)
- Expect dealer to take full position
- Dealer now limited to $\$50M$ (balance sheet)
- **Order unfilled, market impact huge**

**Fix:**
- Break large orders into smaller pieces
- Use multiple dealers
- Accept longer execution time

### 4. Neglecting Regulatory Calendar

**Mistake:** Don't track reporting dates

**Why it fails:** Miss predictable stress

**Regulatory dates:**
- March 31 (Q1)
- June 30 (Q2)
- September 30 (Q3)
- December 31 (year-end, worst!)

**Fix:**
- Mark calendar
- Adjust positions 1-2 weeks before
- Avoid initiating large trades near dates

### 5. Overlooking Derivatives Capital

**Mistake:** Think derivatives "off balance sheet"

**Why it fails:** Capital charges high

**Example:**
- $\$1B$ notional swap with dealer
- Assume no balance sheet impact
- Dealer faces $\$5-10M$ capital charge
- Dealer must charge high spread to cover
- **Your cost much higher than expected**

**Fix:**
- Negotiate clearing fees upfront
- Understand dealer capital costs
- Consider compression (reduce notional)

### 6. Ignoring Netting Limitations

**Mistake:** Assume full netting benefit

**Why it fails:** Regulations limit netting

**Example:**
- Long $\$100M$ Treasuries (repo financed)
- Short $\$100M$ Treasuries (reverse repo)
- Think net exposure = $0
- SLR: Gross exposure = $\$200M$!
- **Capital charge on both legs**

**Fix:**
- Model gross exposure
- Account for limited netting
- Use compression where possible

### 7. Misjudging Dealer Willingness

**Mistake:** Assume dealers compete aggressively

**Why it fails:** Dealers ration balance sheet

**Example:**
- Large hedge fund, great credit
- Request $\$5B$ repo financing
- Dealer says no (balance sheet cap)
- **Stuck without financing**

**Fix:**
- Diversify dealer relationships (5-10 dealers)
- Negotiate balance sheet allocation upfront
- Pay for guaranteed capacity

### 8. Forgetting Liquidity Requirements

**Mistake:** Focus only on capital, ignore liquidity

**Why it fails:** LCR and NSFR bind too

**Example:**
- Bank accepts large deposit
- LCR requires matching HQLA
- Must buy Treasuries (low-yielding)
- **Deposit unprofitable**

**Fix:**
- Model LCR and NSFR impact
- Understand all constraints
- Price products accordingly

---

## Risk Management Rules

### 1. Capital Planning

**Annual capital allocation:**

$$
\text{Business Unit Allocation} = f(\text{Profitability}, \text{Risk}, \text{Strategic Fit})
$$

**Prioritize activities:**
- High ROE (> 15%)
- Low capital consumption
- Stable revenue streams

**Exit or reduce:**
- Low ROE (< 10%)
- High capital consumption
- Volatile earnings

### 2. Balance Sheet Optimization

**Techniques:**

**Netting:**
- Maximize legally enforceable netting
- Bilateral netting agreements
- Multilateral compression (derivatives)

**Collateralization:**
- Post margin to reduce exposures
- Bilateral CSA agreements

**Securitization:**
- Move assets off balance sheet
- Reduce RWA and leverage exposure

**Synthetic positions:**
- Use derivatives instead of cash
- Lower balance sheet footprint

### 3. Stress Testing

**Quarterly scenarios:**

- Extreme market moves (2008-level)
- Funding stress (repo market seizure)
- Leverage ratio compression
- Liquidity drawdowns

**Key metrics:**
- SLR under stress
- LCR under stress
- RWA sensitivity

**Action triggers:**
- If SLR < 6% (buffer violated) → Reduce balance sheet
- If LCR < 110% → Increase HQLA

### 4. Intraday Monitoring

**Real-time dashboards:**

- Current leverage ratio
- LCR usage
- NSFR position
- G-SIB score

**Alerts:**
- Approaching limits (within 10%)
- Large position changes
- Concentrated exposures

### 5. Product Pricing

**Include capital cost:**

$$
\text{Price} = \text{Base Cost} + \frac{\text{ROE Target} \times \text{Capital Charge}}{\text{Notional}}
$$

**Example:**
- Client derivative: $\$100M$ notional
- Capital charge: $\$5M$
- ROE target: 15%
- Annual capital cost: $\$5M × 0.15 = \$750,000$

**Minimum spread:**

$$
\frac{\$750,000}{\$100M} = 0.75\% \text{ (75 bps)}
$$

### 6. Regulatory Engagement

**Active dialogue:**

- Monitor proposed rules
- Comment on regulatory changes
- Quantify impact
- Suggest alternatives

**Industry coordination:**
- Work with SIFMA, IIF
- Share best practices
- Collective advocacy

### 7. Technology Investment

**Efficiency improvements:**

- Automated balance sheet optimization
- Real-time capital tracking
- Algorithmic trading (reduce inventory)
- Electronic platforms (principal → agency)

**ROI:**
- 10-20% reduction in capital usage
- 5-10% improvement in ROE
- Faster regulatory reporting

---

## Real-World Examples

### 1. September 2019 Repo Crisis

**Setup:**
- Quarter-end approaching
- Treasury issuance elevated (funding need)
- Bank balance sheets full

**Outcome:**
- Repo rate spiked 2% → 10% (intraday!)
- Fed emergency intervention ($\$75B$ overnight repo)
- Exposed fragility of repo market
- **SLR constraint prevented dealer intermediation**

**Lesson:** Balance sheet constraints create systemic fragility

### 2. COVID-19 Dash for Cash (March 2020)

**Setup:**
- Pandemic panic, everyone selling
- Even Treasuries dumped (need cash)
- Dealer balance sheets full (can't buy more Treasuries)

**Outcome:**
- Treasury yields spiked 50 bps (should fall in flight-to-quality!)
- Fed suspended SLR temporarily
- Fed bought $\$1 trillion$ Treasuries
- **Market dysfunction due to dealer constraints**

**Lesson:** Even safest assets become illiquid when intermediation constrained

### 3. Client Clearing Exodus (2014-2016)

**Setup:**
- Basel III derivatives capital rules
- Client clearing uneconomic for most dealers

**Outcome:**
- Many banks exited client clearing business
- Clients forced to consolidate (fewer options)
- Clearing costs up 40-60%
- **Reduced competition due to capital requirements**

**Lesson:** Regulations can shrink market provision

### 4. Goldman Sachs Balance Sheet Reduction (2018)

**Setup:**
- Enhanced SLR requirements (G-SIB surcharge)
- Balance sheet at $\$950 billion

**Actions:**
- Reduced repo book by $\$100B$
- Exited certain commodity businesses
- Compressed derivatives notional
- Raised deposits (stable funding)

**Outcome:**
- SLR improved 4.5% → 5.5%
- But: Lower revenues ($\$2-3B$ impact)
- **Chose compliance over growth**

**Lesson:** Banks actively manage to constraints

---

## Practical Steps

### 1. Understanding Your Exposures

**For users of dealer services:**

1. **Identify activities consuming dealer balance sheet:**
   - Prime brokerage financing
   - Derivatives clearing
   - Repo/reverse repo
   - Market-making in cash bonds

2. **Quantify capital charges:**
   - Ask dealers for capital cost estimates
   - Model SLR and RWA impact
   - Understand pricing implications

3. **Plan for quarter-ends:**
   - Mark calendar (Q1, Q2, Q3, Q4)
   - Secure term funding before dates
   - Reduce leverage if possible

### 2. Dealer Relationship Management

**Optimize dealer interactions:**

1. **Diversify counterparties:**
   - 5-10 prime brokers
   - Multiple repo dealers
   - Don't rely on single relationship

2. **Negotiate capacity:**
   - Request committed balance sheet
   - Pay for guaranteed service
   - Senior-level discussions

3. **Minimize capital consumption:**
   - Bilateral compression (derivatives)
   - Post margin promptly
   - Use capital-efficient products

### 3. Product Selection

**Choose capital-light alternatives:**

- **Financing:** Sponsored repo vs. traditional repo
- **Derivatives:** Listed futures vs. OTC swaps
- **Execution:** Agency vs. principal trades
- **Leverage:** Total return swaps vs. margin loans

### 4. Timing Trades

**Avoid quarter/year-end:**

- Don't initiate large positions week before
- Roll financing before reporting dates
- Accept higher costs if unavoidable

**Best timing:**
- Mid-quarter (Jan, April, July, Oct)
- After reporting dates (first week of quarter)

### 5. For Dealers: Capital Allocation

**Optimize balance sheet:**

1. **Measure profitability:**

$$
\text{RAROC} = \frac{\text{Net Income}}{\text{Economic Capital}}
$$

2. **Rank activities:**
   - High RAROC → Expand
   - Low RAROC → Exit

3. **Continuous optimization:**
   - Weekly balance sheet meetings
   - Real-time capital tracking
   - Dynamic pricing

---

## Final Wisdom

> "Balance sheet constraints are the invisible force shaping modern finance - they determine which markets function smoothly and which periodically seize up. The post-2008 regulations achieved their goal of making banks safer, but at the cost of reduced intermediation capacity. This creates a delicate balance: markets are less liquid but financial institutions are more resilient. The key for market participants is understanding these constraints are real, permanent, and binding - dealers can't simply expand balance sheets to meet demand. Plan around quarter-ends, diversify counterparties, and recognize that the pre-2008 world of infinite dealer liquidity is gone forever. The new normal requires more sophisticated planning and acceptance of higher costs during periodic stress."

**Key to success:**

- **Understand constraints:** SLR (most binding), LCR, NSFR, G-SIB surcharge all matter
- **Plan for quarter-ends:** Mark calendar, secure term funding, expect 50-200 bp repo rate spikes
- **Diversify relationships:** 5-10 dealers minimum, don't rely on single counterparty
- **Choose efficient products:** Sponsored repo, listed derivatives, agency trades when possible
- **Monitor regulations:** New rules constantly evolving, stay informed
- **Accept new reality:** Pre-crisis liquidity isn't coming back, adjust strategies accordingly
- **Remember:** These constraints make the system safer but markets less liquid - trade-off is permanent
