# Treasury Specials and Scarcity

**Treasury specials and scarcity** refers to high-demand Treasury securities that trade at premium repo rates (lower than general collateral), creating arbitrage opportunities and funding challenges for those who need to borrow these specific securities.

---

## The Core Insight

**The fundamental idea:**

- Some Treasury securities in high demand (short-selling, hedging)
- High demand → Low repo rate (borrowers compete)
- General Collateral (GC) rate: 2.5%
- Special rate: 1.0% or lower (even negative!)
- Specialness = GC rate - Special rate
- Lenders profit, borrowers pay premium

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/treasury_specials.png?raw=true" alt="treasury_specials" width="700">
</p>
**Figure 1:** Time series of repo specialness for on-the-run 10Y Treasury showing periodic spikes to 200+ bps below GC rate during auctions, supply scarcity, and quarter-end periods.

**You're essentially asking: "Why do some Treasuries trade special, and how do I profit from or manage this scarcity?"**

---

## What Are Treasury Specials?

### 1. Basic Definition

**General Collateral (GC):**
- Any Treasury acceptable as repo collateral
- Repo rate reflects funding costs
- Typical: SOFR + 5-10 bps

**Special Collateral:**
- Specific Treasury security required
- High demand for that particular security
- Repo rate below GC (sometimes negative!)
- Reflects scarcity premium

**Specialness:**

$$
\text{Specialness} = \text{GC Rate} - \text{Special Rate}
$$

**Example:**
- GC repo rate: 2.5%
- On-the-run 10Y repo rate: 1.0%
- **Specialness: 1.5% (150 bps)**

### 2. Why Securities Go Special

**High borrowing demand:**

**Short-selling:**
- Bears want to short specific Treasury
- Borrow via repo to deliver short
- Compete for scarce security

**Hedging:**
- Derivatives dealers hedge positions
- Need specific Treasury for hedge
- Create demand

**Failed trades:**
- Settlement fails (seller didn't deliver)
- Buyer needs to borrow to cover fail
- Urgent demand

**Arbitrage:**
- Basis trades (futures vs. cash)
- Cheapest-to-deliver (CTD) bond in high demand
- Everyone wants same bond

**Auctions:**
- New issue oversubscribed
- Winners want to flip immediately
- Need to borrow to short

### 3. On-the-Run vs Off-the-Run

**On-the-run (OTR):**
- Most recently issued Treasury of each maturity
- Highest liquidity (benchmark)
- Most demand for hedging
- **Typically goes special**

**Off-the-run (OFR):**
- Older issues
- Less liquid
- Less hedging demand
- **Usually trades GC or mild special**

**Specialness comparison:**
- OTR 10Y: 100-200 bps special
- OFR 10Y (1 year old): 20-50 bps special
- OFR 10Y (3 years old): GC rate

### 4. Measurement

**Repo rate levels:**

- **At GC:** Special rate = GC rate (0 bps special)
- **Mildly special:** 20-50 bps below GC
- **Special:** 50-150 bps below GC
- **Very special:** 150-300 bps below GC
- **Super special:** > 300 bps below GC (rare)

**Historical examples:**
- Normal times: OTR 10Y at 50 bps special
- Auction periods: OTR 10Y at 150 bps special
- Crisis (2008): OTR 10Y at 400 bps special!
- COVID (March 2020): OTR 10Y at 300 bps special

### 5. Duration Patterns

**By maturity:**

**2Y Treasury:**
- Less special (lower hedging demand)
- Typical: 20-50 bps special

**10Y Treasury:**
- Most special (benchmark for swaps, hedging)
- Typical: 50-150 bps special

**30Y Treasury:**
- Moderately special
- Typical: 30-100 bps special

**TIPS:**
- Can be very special (smaller float)
- Typical: 50-200 bps special

### 6. Time Patterns

**Auction cycle:**

**Pre-auction (week before):**
- "When issued" (WI) trading starts
- Specialness modest (30-50 bps)

**Auction day:**
- High demand from winners
- Specialness spikes (100-200 bps)

**Post-auction (1-2 weeks):**
- Remains special (50-100 bps)
- Gradual normalization

**Seasoning (months later):**
- New OTR issued
- Old OTR becomes OFR
- Specialness disappears (→ GC)

### 7. Quarter-End Effects

**Reporting date impact:**

**Normal days:**
- OTR 10Y: 80 bps special

**Quarter-end (last 3 days):**
- Banks reduce balance sheets
- Less repo supply
- OTR 10Y: 200 bps special!
- **All Treasuries go more special**

**Year-end:**
- Worst period
- OTR 10Y: 300+ bps special
- Even OFR securities become special

---

## Trading Strategies

**How to profit from specials:**

### 1. Lend Specials

**Most straightforward:**

**Position:**
- Own the special Treasury
- Lend via repo
- Collect premium rate

**Example:**
- Own $10M OTR 10Y
- GC rate: 2.5%
- Special rate: 1.0%
- Lend at 1.0%

**Opportunity cost:**
- Could lend at GC (2.5%)
- Actually lend at 1.0%
- **Give up 1.5% to lender**

**But:**
- Borrower pays 1.5% premium
- **You earn GC + 1.5% specialness benefit as securities lender!**

**Correct accounting:**
- Lend at 1.0% repo rate
- Earn specialness as securities lending fee
- Net: GC rate + specialness

### 2. Buy and Lend

**Active strategy:**

**Position:**
- Buy special Treasury in cash market
- Immediately lend in repo market
- Capture spread

**Example:**
- Buy $10M OTR 10Y @ 98-16
- Borrow $10M at GC (2.5%)
- Lend OTR 10Y at 1.0% (special)

**P&L:**
- Pay: 2.5% on borrowed cash
- Receive: 1.0% when lending bond
- **Net cost: -1.5%**

**Wait, this loses money! Rethink...**

**Actually:**
- Hold the bond (no repo)
- Lend bond via securities lending
- Earn specialness as lending fee

**Or:**
- Buy bond
- Finance at GC via reverse repo (pay 2.5%)
- Lend same bond via repo as special (receive 1.0%)
- This is a "box trade" (fails economic)

**Better approach:**
- Own bond long-term (portfolio holding)
- Lend via securities lending program
- Earn 150 bps lending fee

### 3. Relative Value Trade

**Exploit specialness differential:**

**Setup:**
- OTR 10Y: 150 bps special
- OFR 10Y (similar duration): GC
- Yield spread: 5 bps (small)

**Position:**
- Long OFR (cheaper repo)
- Short OTR (expensive repo)
- Duration-neutral

**Carry:**
- OFR funding: 2.5% (GC)
- OTR lending: 1.0% (special)
- **Negative carry: -1.5%**

**But:**
- If OTR specialness normalizes (150 → 50 bps)
- OTR rallies relative to OFR
- **Capital gain: ~0.30 (price)**

**Trade-off: Negative carry vs. convergence gain**

### 4. CTD Arbitrage

**Exploit futures basis:**

**Setup:**
- CTD bond: 200 bps special
- Basis trade (long CTD, short futures) uses special repo

**Position:**
- Long CTD @ 98-00
- Short 10Y futures @ 120-00
- Finance CTD at special rate (0.5%)

**Carry:**
- Implied repo from basis: 1.8%
- Actual repo (special): 0.5%
- **Positive carry: 1.3%**

**Gain from financing advantage**

### 5. Securities Lending Program

**For asset owners:**

**Setup:**
- Own Treasury portfolio ($100M)
- Lend via agent (custodian bank)

**Lending fees (specialness):**
- OTR securities: 100-200 bps
- OFR securities: 10-50 bps
- Average: 50-75 bps

**Annual revenue:**
- $100M × 0.50% = $500,000$
- Agent takes 30%: $150,000
- **Net to owner: $350,000**

**Enhances portfolio return by 35 bps**

### 6. Fails Arbitrage

**Exploit settlement fails:**

**Setup:**
- Bond fails to deliver (high demand)
- Fails charge: 3% annually
- Buyer of failing bond benefits

**Position:**
- Buy bond that likely to fail
- Seller can't deliver (it's special)
- Receive fails charge

**Example:**
- Buy $10M OTR 10Y
- Seller fails for 10 days
- Fails charge: $10M × 0.03 / 360 × 10 = $8,333$
- **Free money while waiting!**

**Risk:**
- May get delivered (no fails charge)
- Capital tied up

### 7. Auction Flipping

**Short-term special trade:**

**Pre-auction:**
- Auction announced
- Buy WI (when-issued)
- Expect to win in auction

**Post-auction (if won):**
- Receive bonds
- Immediately lend at special rate
- Hold 1-2 weeks (specialness peak)
- Sell in cash market

**Profit sources:**
- Lending fees (specialness)
- Potential price appreciation (OTR premium)

---

## Mathematical Framework

### 1. Specialness Value

**Annual value of lending special:**

$$
\text{Value} = (\text{GC Rate} - \text{Special Rate}) \times \text{Notional} \times \frac{t}{360}
$$

**Example:**
- GC: 2.5%
- Special: 1.0%
- Notional: $10M
- Days: 30

**Value:**

$$
(0.025 - 0.010) \times \$10M \times \frac{30}{360} = \$12,500
$$

### 2. Implied Specialness from Price

**Bond premium due to scarcity:**

**On-the-run premium:**

$$
\text{Premium} = \text{Price}_{\text{OTR}} - \text{Price}_{\text{OFR}}
$$

**Implied specialness:**

$$
\text{Specialness} \approx \frac{\text{Premium}}{\text{Duration}} \times 100
$$

**Example:**
- OTR price: 100-08 (100.25)
- OFR price: 99-24 (99.75)
- Premium: 0.50
- Duration: 8 years

**Implied specialness:**

$$
\frac{0.50}{8} \times 100 = 6.25\% \text{ (way too high!)}
$$

**More accurate method uses repo model**

### 3. Optimal Lending Strategy

**Maximize expected revenue:**

$$
\max \mathbb{E}[\text{Revenue}] = \mathbb{E}[\text{Lending Fees}] - \text{Operational Costs} - \text{Reinvestment Risk}
$$

**Decision:**
- Lend if: Expected specialness > Minimum threshold (10 bps)
- Keep unlent if: Near corporate action (vote, tender)

### 4. Fails Charge P&L

**Value of fails:**

$$
\text{Fails Benefit} = \text{Notional} \times 0.03 \times \frac{\text{Days Failed}}{360}
$$

**Example:**
- $10M fails for 5 days
- **Benefit: $10M × 0.03 × 5/360 = $4,167$**

### 5. Box Trade Analysis

**Locked-in profit:**

$$
\text{Box Profit} = (\text{Special Rate} - \text{GC Rate}) \times \text{Notional} \times \frac{t}{360}
$$

**Only works if you own the bond already (no acquisition cost)**

### 6. Carry from Basis Trade

**With special financing:**

$$
\text{Carry} = (\text{IRR} - \text{Special Rate}) \times \text{Notional} - \text{Coupon Income}
$$

**Example:**
- IRR: 1.8%
- Special rate: 0.5%
- Notional: $10M
- Net carry: $(1.8\% - 0.5\%) × $10M = $130,000$ annually

### 7. Duration-Neutral Hedge

**OTR vs OFR trade:**

$$
\text{Hedge Ratio} = \frac{\text{DV01}_{\text{OTR}}}{\text{DV01}_{\text{OFR}}}
$$

**Example:**
- OTR DV01: $850
- OFR DV01: $820
- **Hedge ratio: 850/820 = 1.037**

**For $10M OTR long, need $10.37M OFR short**

---

## Common Mistakes

**Pitfalls to avoid:**

### 1. Ignoring Financing Costs

**Mistake:** Think special rate is what you earn

**Why it fails:** Confuse lending rate with profit

**Example:**
- Lend bond at 1.0% (special)
- Think earning 1.0%

**But:**
- Opportunity cost: Could lend at 2.5% (GC)
- Actually giving up 1.5%!

**Correct view:**
- As securities lender, earn specialness (1.5%)
- As repo lender, receive 1.0% (low)

**Fix:** Understand securities lending vs. repo lending

### 2. Buying Expensive Bonds

**Mistake:** Buy OTR expecting to profit from lending

**Why it fails:** Pay premium in cash market

**Example:**
- OTR trades 0.50 rich (price premium)
- Buy at 100.50
- Lend and earn 150 bps specialness annually
- But: Paid 0.50 upfront (equal to 3 months lending!)

**Fix:** Buy OFR securities (cheaper), lend those instead

### 3. Neglecting Recall Risk

**Mistake:** Lend securities, forget can be recalled

**Why it fails:** Need security back, can't get it

**Example:**
- Lend $10M OTR 10Y
- Decide to sell portfolio next week
- Try to recall from borrower
- Borrower can't return (fails)
- **Stuck without bonds, miss sale opportunity**

**Fix:**
- Keep portion unlent (50-70% lendable)
- Monitor recall times (1-3 days typical)
- Use automated recall systems

### 4. Misunderstanding Securities Lending

**Mistake:** Confuse with repo

**Why it fails:** Different economics

**Repo (borrowing cash):**
- I post bond, receive cash
- Pay repo rate (interest on cash)

**Securities lending (lending bonds):**
- I lend bond, receive cash collateral
- Borrower pays lending fee
- I rebate most interest on cash collateral

**Fix:** Know which side you're on

### 5. Ignoring Fails Charges

**Mistake:** Accept fails without collecting

**Why it fails:** Free money left on table

**Example:**
- Sold $10M bond, counterparty fails
- Don't claim fails charge
- Counterparty profits from free financing

**Fix:**
- Enforce fails charges (3% penalty)
- Contractual language requiring payment
- Monitor settlement

### 6. Over-Reliance on Specialness

**Mistake:** Build entire strategy on specials

**Why it fails:** Specialness disappears

**Example:**
- Buy CTD bond at 200 bps special
- Build basis trade assuming 200 bps advantage
- Supply increases, specialness falls to 50 bps
- **Carry evaporates, trade unprofitable**

**Fix:**
- Don't assume specialness persists
- Model scenario with specialness at GC
- Keep conservative assumptions

### 7. Quarter-End Surprise

**Mistake:** Don't prepare for quarter-end scarcity

**Why it fails:** Specialness spikes dramatically

**Example:**
- Funding $10M position via repo
- Normal rate: 2.0%
- Quarter-end rate spikes: 5.0%
- **Funding cost triples overnight!**

**Fix:**
- Secure term repo through quarter-end
- Reduce leverage before reporting dates
- Budget for higher costs

### 8. Concentration Risk

**Mistake:** Lend entire portfolio

**Why it fails:** Operational stress

**Example:**
- Lend 100% of $100M portfolio
- Multiple recalls same day (corporate action)
- Can't retrieve all securities fast enough
- **Operational nightmare**

**Fix:**
- Lend maximum 70% of portfolio
- Keep 30% buffer for flexibility
- Stagger recall terms

---

## Risk Management Rules

### 1. Lending Limits

**Maximum to lend:**

- **By security:** 80% of holdings (keep 20% buffer)
- **By portfolio:** 70% of total (keep 30% unlent)
- **By counterparty:** 10% of portfolio per borrower

**Example:**
- Own $10M OTR 10Y
- Lend maximum: $8M (80%)
- Keep unlent: $2M (for flexibility)

### 2. Counterparty Limits

**Diversify borrowers:**

- No single borrower > 20% of lent securities
- Minimum 5 borrowers for large programs
- Credit quality: A-rated or better

**Example:**
- $100M securities lending program
- Max per borrower: $20M
- Require: 5-10 borrowers

### 3. Recall Procedures

**Establish protocols:**

- Standard recall: 1-2 business days
- Priority recall: Same day (emergency)
- Automated systems for efficiency
- Monitor corporate actions calendar

### 4. Collateral Management

**For cash collateral:**

- Accept 102-105% of security value
- Reinvest conservatively (Treasuries, reverse repo)
- Daily mark-to-market
- Margin calls for shortfalls

**For securities collateral:**
- Accept 100-110% of value
- Eligible: Treasuries, agencies
- Daily revaluation

### 5. Monitoring

**Daily:**
- Repo rates (GC and specials)
- Utilization rates
- Collateral valuations
- Fails tracking

**Weekly:**
- Counterparty exposures
- Lending revenue
- Specialness levels
- Corporate actions calendar

**Monthly:**
- Performance review
- Fee benchmarking
- Agent performance
- Risk reports

### 6. Auction Calendar

**Pre-auction preparation:**

- Identify which holdings become OTR
- Anticipate specialness spike
- Prepare to lend
- Consider temporary sales (auction flip)

**Post-auction:**
- Lend new OTR securities
- Capture elevated specialness
- Monitor normalization (1-2 weeks)

### 7. Quarter-End Planning

**Prepare 2 weeks before:**

- Reduce reliance on overnight repo
- Secure term funding
- Lend more securities (higher specialness)
- Budget for 2-3× normal funding costs

**Example:**
- Normal repo: 2.5%
- Quarter-end budget: 5-7%
- Lock term repo at 3.5% (better than 7%!)

---

## Real-World Examples

### 1. COVID Dash for Cash (March 2020)

**Setup:**
- Panic selling, everyone needs cash
- Even Treasuries dumped
- OTR 10Y: 300 bps special!

**Outcome:**
- Huge demand to short Treasuries (sell, then cover)
- Lenders earned massive fees (300 bps annually)
- Some earned 2-3% in one month!
- **Securities lending windfall**

**Lesson:** Crisis → extreme specialness → lender bonanza

### 2. 10Y Auction Flip (2019)

**Setup:**
- 10Y auction oversubscribed
- Won $50M at auction
- Expected OTR to go 150 bps special

**Trade:**
- Received bonds at auction price
- Immediately lent at 1.0% (GC = 2.5%)
- Held 2 weeks, earned specialness
- Sold bonds in market

**Outcome:**
- Specialness: 150 bps for 14 days
- Lending revenue: $50M × 1.5% × 14/360 = $29,167$
- Price appreciation: +0.125 (2 ticks)
- **Total profit: $91,667 (0.18% in 2 weeks!)**

**Lesson:** Auction timing creates short-term specials

### 3. CTD Special (2018)

**Setup:**
- 10Y futures CTD goes 200 bps special
- Basis traders need CTD to hedge

**Impact on basis trade:**
- Normal basis trade: IRR 2.0%, repo 2.5% (negative carry)
- With CTD special: IRR 2.0%, repo 0.5% (positive carry!)
- **Basis trade becomes profitable due to financing**

**Outcome:**
- Many traders piled into basis trade
- CTD specialness increased demand
- Eventually specialness normalized
- **First movers profited, late entrants lost**

**Lesson:** Specials create basis trade opportunities (and crowded trades)

### 4. Quarter-End Squeeze (Dec 2019)

**Setup:**
- Year-end approaching
- Bank balance sheet constraints
- All Treasuries became special

**Rates:**
- Normal: OTR 80 bps special, OFR at GC
- Dec 31: OTR 300 bps special, OFR 100 bps special!
- Even TIPS went special

**Impact:**
- Securities lenders: Windfall week (300 bps annual → 6 bps for 1 week!)
- Securities borrowers: Massive costs
- Fed intervened (repo operations)

**Lesson:** Year-end effects are extreme, plan accordingly

### 5. TIPS Scarcity (2020-2021)

**Setup:**
- Inflation fears, high TIPS demand
- TIPS supply limited (smaller float than nominals)
- Many TIPS became super special

**Specialness:**
- 5Y TIPS: 200 bps special (persistent)
- 10Y TIPS: 150 bps special
- 30Y TIPS: 100 bps special

**Impact:**
- TIPS lenders earned massive fees
- Inflation traders paid premium to short
- Break-even inflation rates distorted
- **TIPS appeared expensive due to specialness, not inflation views**

**Lesson:** Scarcity affects pricing (TIPS look rich, but it's technical)

---

## Practical Steps

### 1. Monitoring Specialness

**Daily tracking:**

```
Download repo rates:
- OTR 2Y, 5Y, 10Y, 30Y
- Compare to GC rate (SOFR)
- Calculate specialness

Create dashboard:
- Current specialness
- Historical percentile
- Trend (improving or worsening)
```

**Example spreadsheet:**
```
Security    | GC Rate | Special Rate | Specialness | Percentile
OTR 10Y     | 2.50%   | 1.00%       | 150 bps     | 85th
OFR 10Y     | 2.50%   | 2.40%       | 10 bps      | 20th
OTR 30Y     | 2.50%   | 1.80%       | 70 bps      | 60th
```

### 2. Securities Lending Setup

**For asset owners ($50M+ portfolio):**

1. **Select agent:**
   - Custodian bank (BNY, State Street, JPM)
   - Compare fee splits (70/30, 80/20)
   - Check indemnification terms

2. **Define parameters:**
   - Which securities lendable (all Treasuries)
   - Minimum fee (e.g., 10 bps)
   - Recall rights (1-2 days)
   - Collateral type (cash or securities)

3. **Monitor program:**
   - Monthly revenue reports
   - Utilization rates (% on loan)
   - Specialness capture
   - Compare to benchmarks

### 3. Exploiting Specials (For Traders)

**Identify opportunities:**

1. **Scan for rich specials:**
   - Specialness > 100 bps
   - Historically elevated
   - Near auction dates

2. **Evaluate trade:**
   - Own the security already? → Lend it
   - Don't own? → Consider buying OFR instead
   - Need to borrow? → Budget for special rate

3. **Execute:**
   - Lend via agent or directly
   - Monitor daily rates
   - Capture revenue

### 4. Managing Financing

**For repo borrowers:**

1. **Identify needs:**
   - Which Treasuries to finance?
   - Check if any are special

2. **Budget appropriately:**
   - Normal: SOFR + 10 bps
   - Special: SOFR - 100 bps (pay premium!)
   - Quarter-end: SOFR + 200 bps

3. **Alternatives:**
   - If special too expensive, use OFR instead
   - Term repo through quarter-ends
   - Reduce leverage before reporting dates

### 5. Auction Strategy

**Around auction dates:**

1. **Pre-auction (1 week before):**
   - Monitor WI specialness
   - Plan to participate if profitable

2. **Auction day:**
   - Submit bids
   - If won, prepare to lend

3. **Post-auction (days 1-14):**
   - Lend at special rate (peak specialness)
   - Earn elevated fees
   - Monitor normalization

4. **After 2 weeks:**
   - Consider selling OTR
   - Or hold and continue lending (lower fees)

---

## Final Wisdom

> "Treasury specials are the plumbing of the market - invisible to most but critical to understanding financing costs and arbitrage opportunities. Securities that go special create wealth for those who own them (lenders profit) and pain for those who need them (borrowers pay up). The key insights: (1) on-the-run Treasuries are always somewhat special due to hedging demand, (2) specialness spikes around auctions and quarter-ends when scarcity intensifies, and (3) the value of owning specials is real but temporary - every OTR eventually becomes OFR and specialness evaporates. Smart investors lend their Treasury holdings through securities lending programs, earning 20-100 bps annually with minimal risk. Smart traders avoid shorting OTR securities unless absolutely necessary, and always budget for special repo rates."

**Key to success:**

- **For lenders:** Enable securities lending on Treasury portfolio (earn 20-100 bps annually), keep 20-30% buffer unlent for flexibility
- **For borrowers:** Budget for special rates (100-200 bps below GC for OTR), consider using OFR securities instead if special too expensive
- **Monitor calendar:** Auctions create 1-2 week specialness spikes, quarter-ends create 3-7 day extreme scarcity
- **Understand economics:** Specialness = GC rate - Special rate, this is the value to lender (or cost to borrower)
- **Track OTR vs OFR:** On-the-run trades 50-150 bps special (normal), off-the-run at GC (normal), know which you're trading
- **Plan quarter-ends:** Secure term funding 2 weeks before, expect 2-3× normal costs, or reduce leverage entirely
- **Remember:** Specialness is temporary, mean-reverting, and cyclical - profit from extremes but don't assume persistence
