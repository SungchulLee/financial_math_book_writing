# Duration Hedging

**Duration hedging** is the practice of neutralizing a bond portfolio's sensitivity to interest rate changes by taking offsetting positions in derivatives or other bonds, protecting the portfolio value from parallel shifts in the yield curve while maintaining exposure to other factors like credit spreads or carry.

---

## The Core Insight

**The fundamental idea:**

- Bonds lose value when interest rates rise (inverse relationship)
- Duration measures this interest rate sensitivity
- Longer duration = higher sensitivity to rate changes
- Hedging removes unwanted rate risk while keeping desired exposures
- Use liquid instruments (futures, swaps) to hedge illiquid bond positions
- Separate interest rate risk from credit risk, carry, and other factors
- Dynamic hedging required as duration changes over time

**The key equation:**

$$
\Delta P \approx -D \times P \times \Delta y
$$

Where:
- $\Delta P$ = Change in portfolio value
- $D$ = Modified duration
- $P$ = Portfolio value
- $\Delta y$ = Change in yield

**For a hedged portfolio:**

$$
\Delta P_{\text{portfolio}} + \Delta P_{\text{hedge}} \approx 0
$$

**You're essentially saying: "I want exposure to credit spreads, carry, or specific bonds, but NOT to parallel interest rate moves. I'll use liquid derivatives to neutralize my duration while keeping my fundamental positions."**

---

## What is Duration Hedging?

**Before implementing duration hedges, understand the foundation:**

### Duration as Interest Rate Sensitivity

**Modified duration definition:**

$$
D = -\frac{1}{P} \frac{\partial P}{\partial y}
$$

**Interpretation:** Duration tells you the percentage change in bond price for a 1% (100 bp) change in yield.

**Example:**

- Bond price: $1,000
- Duration: 7.0 years
- If yields rise 1%: $\Delta P = -7.0\% \times \$1,000 = -\$70$
- If yields fall 1%: $\Delta P = +7.0\% \times \$1,000 = +\$70$

**Macaulay duration:**

$$
D_{\text{Mac}} = \frac{\sum_{t=1}^{n} t \times \frac{CF_t}{(1+y)^t}}{P}
$$

**Modified duration:**

$$
D_{\text{mod}} = \frac{D_{\text{Mac}}}{1 + y}
$$

**Most practitioners use modified duration for hedging.**

### DV01: Dollar Duration

**DV01 (Dollar Value of 01 basis point):**

$$
\text{DV01} = D \times P \times 0.0001
$$

**Or equivalently:**

$$
\text{DV01} = -\frac{\partial P}{\partial y} \times 0.0001
$$

**Interpretation:** How much the position loses for a 1 basis point (0.01%) rise in yield.

**Example:**

- Bond value: $10,000,000
- Duration: 6.0 years
- DV01 = 6.0 × $10,000,000 × 0.0001 = **$6,000**
- If yields rise 1 bp: Portfolio loses $6,000
- If yields rise 50 bp: Portfolio loses $300,000

**DV01 is the key metric for hedging:**

$$
\text{Hedge Ratio} = \frac{\text{DV01}_{\text{portfolio}}}{\text{DV01}_{\text{hedge instrument}}}
$$

### Why Hedge Duration?

**Reasons portfolio managers hedge duration:**

**1. Separate interest rate risk from credit risk:**

- Portfolio: Corporate bonds (want credit spread exposure)
- Don't want: Interest rate sensitivity
- Solution: Hedge with Treasury futures (removes rate risk, keeps credit)

**2. Asset-liability matching:**

- Liability: Pay pension benefits (fixed duration)
- Assets: Bond portfolio (different duration)
- Solution: Hedge to match asset duration to liability duration

**3. Tactical positioning:**

- Fundamental view: Corporate bonds undervalued
- Rate view: Neutral or bearish
- Solution: Long corporates, hedge with futures (isolate credit view)

**4. Regulatory capital efficiency:**

- Interest rate risk consumes regulatory capital
- Hedging reduces capital requirement
- Allows more leverage or higher ROE

**5. Carry enhancement:**

- Strategy: Long high-yield bonds (carry), hedge rates
- Keep: Credit spread income
- Remove: Duration risk
- Result: Enhanced risk-adjusted carry

### Duration Hedging is NOT:

**What it doesn't do:**

1. **Protect against credit spread widening:**
   - Corporate bonds can fall even if rates flat
   - Duration hedge only neutralizes rate sensitivity
   - Credit risk remains!

2. **Protect against non-parallel shifts:**
   - Duration assumes parallel yield curve shift
   - Curve steepening/flattening not hedged
   - Need curve hedges (key rate durations)

3. **Eliminate convexity risk:**
   - Duration is linear approximation
   - Large rate moves: convexity matters
   - May need convexity hedging too

4. **Remove all risk:**
   - Basis risk between hedge and portfolio
   - Tracking error
   - Hedge needs rebalancing

---

## Economic Interpretation: Separating Risk Factors

**Understanding the economic logic of duration hedging:**

### The Decomposition of Bond Returns

**Total bond return decomposes into:**

$$
R_{\text{total}} = \underbrace{R_{\text{carry}}}_{\text{Yield income}} + \underbrace{R_{\text{roll}}}_{\text{Pull-to-par}} + \underbrace{R_{\text{rates}}}_{\text{Duration effect}} + \underbrace{R_{\text{spread}}}_{\text{Credit/liquidity}}
$$

**Example: Corporate bond over 1 year:**

| Component | Contribution | Source |
|-----------|--------------|---------|
| Carry | +4.5% | Coupon yield |
| Roll-down | +0.5% | Pull to par as maturity nears |
| Rate change | -2.0% | Treasury yields rose 50 bp |
| Spread change | -1.0% | Credit spreads widened 25 bp |
| **Total return** | **+2.0%** | Net result |

**Duration hedging isolates the components you want:**

**Hedged return:**

$$
R_{\text{hedged}} = R_{\text{carry}} + R_{\text{roll}} + R_{\text{spread}} + \underbrace{R_{\text{hedge}}}_{\text{Offsets } R_{\text{rates}}}
$$

**After hedging:**

| Component | Contribution | Notes |
|-----------|--------------|-------|
| Carry | +4.5% | Keep this |
| Roll-down | +0.5% | Keep this |
| Rate change | -2.0% | Unwanted |
| **Hedge P/L** | **+2.0%** | Offsets rate change |
| Spread change | -1.0% | Keep this (your view) |
| **Net return** | **+4.0%** | Better risk-adjusted |

**You removed the rate risk (which you had no view on) and kept the components you wanted!**

### Duration as a Factor Risk Premium

**Think of duration as exposure to the "interest rate factor":**

$$
R_{\text{bond}} = \alpha + \beta_{\text{duration}} \times F_{\text{rates}} + \beta_{\text{credit}} \times F_{\text{credit}} + \epsilon
$$

**Where:**
- $F_{\text{rates}}$ = Interest rate factor (parallel shift)
- $F_{\text{credit}}$ = Credit spread factor
- $\beta_{\text{duration}}$ = Duration (sensitivity to rates)
- $\beta_{\text{credit}}$ = Credit sensitivity (spread duration)

**Duration hedging sets $\beta_{\text{duration}} = 0$:**

$$
R_{\text{hedged}} = \alpha + 0 \times F_{\text{rates}} + \beta_{\text{credit}} \times F_{\text{credit}} + \epsilon
$$

**Now you only have credit exposure, not rate exposure.**

**This is analogous to equity long/short:**

- Long/short equity: Remove market beta, keep stock alpha
- Duration hedging: Remove rate beta, keep credit/carry alpha

### The Hedge as a Swap of Cash Flows

**Economically, a duration hedge is a cash flow swap:**

**Unhedged corporate bond:**
- Receive: Corporate bond cash flows (coupons + principal)
- Exposed to: Interest rate changes affecting PV of these flows

**With Treasury futures hedge:**
- Receive: Corporate bond cash flows
- Pay: Synthetic fixed rate on notional (futures contract)
- **Net:** Corporate spread over Treasuries (with no rate risk)

**This is almost identical to an interest rate swap!**

$$
\text{Hedged Position} \approx \text{Long corporate bond} + \text{Pay-fixed swap}
$$

**Result:** Receive corporate yield, pay Treasury yield = corporate spread.

### Basis Risk: The Cost of Hedging

**Perfect hedge requires:**

$$
\text{Duration}_{\text{portfolio}} = \text{Duration}_{\text{hedge}}
$$

AND

$$
\text{Yield change}_{\text{portfolio}} = \text{Yield change}_{\text{hedge}}
$$

**But in reality:**

**Basis risk arises from:**

1. **Different yield changes:**
   - Corporate yields ≠ Treasury yields
   - Credit spreads can change independently
   - Hedge only neutralizes Treasury component

2. **Imperfect correlation:**
   - Portfolio: 10-year corporates
   - Hedge: 10-year Treasury futures
   - Correlation typically 0.85-0.95 (not 1.0)

3. **Curve risk:**
   - Portfolio has exposure across curve
   - Hedge is single point on curve
   - Non-parallel shifts create tracking error

**The basis risk is the price you pay for:**
- Liquidity of futures vs. illiquidity of bonds
- Simplicity of hedge vs. perfect replication
- Low transaction costs vs. high precision

**Expected tracking error:** 10-30% of unhedged volatility remains even with "perfect" DV01 hedge.

---

## Key Terminology

**Duration:**

- Measure of interest rate sensitivity
- Units: Years (but really % change per 1% yield change)
- Modified duration most commonly used for hedging

**DV01 (Dollar Value of a 01):**

- Change in value for 1 basis point yield change
- Key metric for calculating hedge ratios
- Also called "PV01" or "dollar duration"

**Convexity:**

- Curvature in price-yield relationship
- Second derivative of price with respect to yield
- Important for large rate changes

$$
\text{Convexity} = \frac{1}{P} \frac{\partial^2 P}{\partial y^2}
$$

**Hedge Ratio:**

- Number of hedge contracts needed
- Formula: $\frac{\text{DV01}_{\text{portfolio}}}{\text{DV01}_{\text{hedge}}}$
- Negative for short hedge (offset long bonds)

**CTD (Cheapest-to-Deliver):**

- In futures, the cheapest bond to deliver
- Important for calculating conversion factors
- Changes as yields move (CTD switch risk)

**Conversion Factor:**

- Adjusts futures price for CTD bond characteristics
- Normalizes different bonds to 6% coupon standard
- Formula involves duration and coupon

**Basis (Cash-Futures Basis):**

- Difference between cash bond price and futures price
- Basis = Cash price - (Futures price × Conversion factor)
- Can be positive or negative

**Key Rate Duration:**

- Duration sensitivity to specific maturity buckets
- Allows hedging non-parallel shifts
- E.g., 2-year KRD, 5-year KRD, 10-year KRD

**Spread Duration:**

- Sensitivity to credit spread changes
- Similar to duration but for spreads
- Important for credit portfolios

---

## Basic Duration Hedging Strategies

### Strategy 1: Treasury Futures Hedge (Classic)

**Setup:**

**Portfolio:**
- $100 million corporate bonds
- Average duration: 7.2 years
- Average yield: 5.5%
- DV01: $100M × 7.2 × 0.0001 = **$72,000**

**Hedge instrument:**
- 10-year Treasury futures
- Contract size: $100,000 face value
- Futures price: 110-00 (110% of par = $110,000)
- CTD duration: 8.5 years
- DV01 per contract: $110,000 × 8.5 × 0.0001 = **$935**

**Hedge ratio calculation:**

$$
\text{Contracts} = \frac{\text{DV01}_{\text{portfolio}}}{\text{DV01}_{\text{futures}}} = \frac{72,000}{935} = 77 \text{ contracts}
$$

**Execute:**
- Sell 77 10-year Treasury futures contracts
- Creates short duration position
- Offsets long duration in bond portfolio

**Result:**

$$
\text{Net DV01} = 72,000 - (77 \times 935) = 72,000 - 72,000 = 0
$$

**Portfolio is now duration-neutral!**

**Example P/L:**

**Scenario 1: Rates rise 50 bp**

| Position | Value Change |
|----------|--------------|
| Corporate bonds | -$72,000 × 50 = -$3,600,000 |
| Futures (short) | +$935 × 50 × 77 = +$3,600,000 |
| **Net P/L** | **$0** |

Plus: Still have credit spread exposure, carry income.

**Scenario 2: Credit spreads widen 25 bp (rates flat)**

| Position | Value Change |
|----------|--------------|
| Corporate bonds | -$72,000 × 25 = -$1,800,000 |
| Futures (short) | $0 (no rate change) |
| **Net P/L** | **-$1,800,000** |

The hedge doesn't protect against credit risk!

### Strategy 2: Interest Rate Swap Hedge

**Setup:**

**Portfolio:**
- $50 million floating rate notes (FRN)
- Duration: 0.25 years (very short, resets quarterly)
- Want to extend duration to 5.0 years

**Hedge instrument:**
- Pay-fixed, receive-floating interest rate swap
- Notional: $50 million
- Fixed rate: 4.5% (5-year swap rate)
- Floating: 3-month LIBOR
- Swap duration: 4.75 years (approximately)

**Target duration:**

$$
D_{\text{target}} = D_{\text{FRN}} + D_{\text{swap}} = 0.25 + 4.75 = 5.0 \text{ years}
$$

**Result:**
- Portfolio now has 5-year duration
- Receive floating (offsets FRN floating receipts)
- Pay fixed at 4.5%
- **Net:** Synthetic fixed-rate bond at 4.5% with 5-year duration

**Why do this?**
- Asset manager needs duration to match liabilities
- Cheaper than selling FRNs and buying fixed-rate bonds
- More flexible (can unwind swap easily)

### Strategy 3: Cross-Hedge with Different Maturity

**Setup:**

**Portfolio:**
- $75 million 30-year corporate bonds
- Duration: 18.5 years
- DV01: $75M × 18.5 × 0.0001 = **$138,750**

**Problem:**
- No liquid 30-year futures
- Must use 10-year futures to hedge

**Hedge instrument:**
- 10-year Treasury futures
- DV01 per contract: $935 (as before)

**Hedge ratio:**

$$
\text{Contracts} = \frac{138,750}{935} = 148 \text{ contracts}
$$

**Sell 148 ten-year futures contracts**

**Basis risk:**
- 30-year yields don't move 1:1 with 10-year yields
- Typical correlation: 0.88-0.92
- Hedge effectiveness: 85-90%

**Better approach: Beta-adjusted hedge**

$$
\text{Contracts}_{\text{adjusted}} = \frac{\text{DV01}_{\text{portfolio}}}{\text{DV01}_{\text{futures}}} \times \beta
$$

Where $\beta$ = regression of 30-year yield changes on 10-year changes.

If $\beta = 0.92$:

$$
\text{Contracts} = 148 \times 0.92 = 136 \text{ contracts}
$$

### Strategy 4: Convexity Hedge

**Setup:**

**Portfolio:**
- $100 million long-dated bonds
- Duration: 15.0 years
- Convexity: 300
- DV01: $150,000

**Problem:**
- Duration hedge only linear
- Large rate moves: convexity matters
- Positive convexity helps when rates fall, hurts when rates rise

**Convexity adjustment:**

$$
\Delta P = -D \times P \times \Delta y + \frac{1}{2} C \times P \times (\Delta y)^2
$$

**For 100 bp rate rise:**

Without convexity:
- $\Delta P = -15.0 \times \$100M \times 0.01 = -\$15M$

With convexity:
- $\Delta P = -\$15M + \frac{1}{2} \times 300 \times \$100M \times (0.01)^2$
- $\Delta P = -\$15M + \$1.5M = -\$13.5M$

**Convexity helped by $1.5M!**

**Hedge:**
- Use options on bond futures
- Options have negative convexity when sold
- Selling options neutralizes positive convexity of bonds
- Creates more stable hedge for large moves

---

## Greeks in Duration Hedging

**Understanding the risk sensitivities:**

### Duration: The Primary Greek

$$
D = -\frac{1}{P} \frac{\partial P}{\partial y}
$$

**Duration in hedging context:**

**Unhedged portfolio:**
- Duration: 7.5 years
- $100M position
- DV01: $75,000
- Exposure: Loses $75k per 1 bp rate rise

**Hedged portfolio:**
- Portfolio duration: 7.5 years
- Hedge duration: -7.5 years (short futures)
- Net duration: 0 years
- DV01: $0
- Exposure: None to parallel rate shifts

**Key insight:** Duration is like delta in options.
- Delta: Sensitivity to stock price
- Duration: Sensitivity to interest rates
- Both measure linear sensitivity
- Both need hedging for neutrality

### Convexity: The Second-Order Effect

$$
C = \frac{1}{P} \frac{\partial^2 P}{\partial y^2}
$$

**Convexity in hedging:**

**Bonds have positive convexity:**
- Rates fall: Price rises more than duration predicts
- Rates rise: Price falls less than duration predicts
- **Good for bond holders!**

**Futures have low/zero convexity:**
- Linear payoff
- No curvature benefit

**Hedged portfolio convexity:**

$$
C_{\text{hedged}} = C_{\text{bonds}} - C_{\text{futures}} \approx C_{\text{bonds}}
$$

**Problem:** Even with duration hedge, portfolio has convexity exposure.

**For large rate moves (>100 bp):**
- Hedge becomes imperfect
- Need to rebalance (dynamic hedging)
- Or use options to hedge convexity

**Example:**

Portfolio: $100M bonds, duration 10, convexity 150

**Rate rise 100 bp:**
- Duration effect: -$10M
- Convexity benefit: +$0.75M
- Net: -$9.25M

**Rate fall 100 bp:**
- Duration effect: +$10M
- Convexity benefit: +$0.75M
- Net: +$10.75M

**Convexity creates asymmetry (good!)** But hedge doesn't capture this.

### Key Rate Durations: The Curve Greeks

**Standard duration assumes parallel shift:**

$$
\Delta y_1 = \Delta y_2 = \Delta y_5 = \Delta y_{10} = \Delta y_{30}
$$

**But in reality, yield curve can steepen, flatten, twist.**

**Key rate duration (KRD) decomposes:**

$$
D_{\text{total}} = \sum_{i} D_i
$$

Where $D_i$ = duration sensitivity to maturity bucket $i$.

**Example portfolio:**

| Maturity Bucket | Key Rate Duration | DV01 |
|----------------|-------------------|------|
| 2-year | 1.2 | $12,000 |
| 5-year | 2.5 | $25,000 |
| 10-year | 3.8 | $38,000 |
| 30-year | 0.5 | $5,000 |
| **Total** | **8.0** | **$80,000** |

**Single futures hedge:**
- Hedges total DV01 of $80,000
- But doesn't match key rate profile
- Exposed to non-parallel shifts

**Better hedge:**
- 2-year futures: Hedge 2-year KRD
- 10-year futures: Hedge 10-year KRD
- 30-year futures: Hedge 30-year KRD
- **Matches curve exposure better**

### Spread Duration: The Credit Greek

$$
D_{\text{spread}} = -\frac{1}{P} \frac{\partial P}{\partial s}
$$

Where $s$ = credit spread.

**Corporate bond has two durations:**

1. **Rate duration:** Sensitivity to Treasury yields
2. **Spread duration:** Sensitivity to credit spreads

**Example:**

- Corporate bond: Duration 7.0
- Treasury yield: 4.0%
- Credit spread: 1.5%
- All-in yield: 5.5%

**Rate duration ≈ 7.0**
**Spread duration ≈ 7.0** (often similar)

**Hedging with Treasuries:**
- Removes rate duration
- Keeps spread duration
- **Isolated credit exposure!**

**If credit spread widens 50 bp:**
- Loss: $7.0 × $100M × 0.005 = -$3.5M
- Treasury hedge: No help (only hedges rates)
- **This is intentional!** You want credit exposure.

---

## Duration Hedging Payoff Analysis

### Unhedged vs. Hedged Portfolio

**Setup:**
- $100M corporate bond portfolio
- Duration: 7.0 years
- Current yield: 5.5% (Treasury 4.0% + spread 1.5%)

**Scenario analysis (1 year horizon):**

| Rate Change | Spread Change | Unhedged P/L | Hedged P/L | Notes |
|-------------|---------------|--------------|------------|-------|
| -100 bp | 0 bp | +$7.0M | $0M | Rates rally, hedge loses |
| -50 bp | 0 bp | +$3.5M | $0M | Moderate rally |
| 0 bp | 0 bp | $0M | $0M | No change |
| +50 bp | 0 bp | -$3.5M | $0M | Rates rise, hedge wins |
| +100 bp | 0 bp | -$7.0M | $0M | Sharp rise |
| 0 bp | -50 bp | +$3.5M | +$3.5M | Spread tightening (good) |
| 0 bp | +50 bp | -$3.5M | -$3.5M | Spread widening (bad) |
| +50 bp | +50 bp | -$7.0M | -$3.5M | Rates up, spreads widen |
| -50 bp | -50 bp | +$7.0M | +$3.5M | Rates down, spreads tighten |

**Key insights:**

1. **Hedged portfolio:** Neutral to rate changes
2. **Full exposure:** Credit spread changes
3. **Combination moves:** Hedge helps reduce total volatility
4. **Trade-off:** Give up rate rally upside to avoid rate rise downside

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/duration_hedge_payoff.png?raw=true" alt="duration_hedge_payoff" width="700">
</p>
**Figure 1:** Comparison of unhedged vs. hedged portfolio P/L across interest rate scenarios, showing how duration hedging neutralizes rate sensitivity while maintaining credit spread exposure.

### Rolling Hedge Performance

**Hedges need rebalancing as:**

1. **Time passes:** Duration decreases (roll-down)
2. **Rates move:** DV01 changes (delta changes)
3. **Portfolio changes:** Bonds mature, new bonds bought

**Example: Monthly rebalancing**

| Month | Portfolio DV01 | Hedge DV01 | Net DV01 | Rebalance Action |
|-------|---------------|------------|----------|------------------|
| 0 | $72,000 | -$72,000 | $0 | Initial hedge |
| 1 | $70,000 | -$72,000 | -$2,000 | Reduce hedge by 2 contracts |
| 2 | $68,500 | -$70,000 | -$1,500 | Reduce hedge by 2 contracts |
| 3 | $67,000 | -$68,500 | -$1,500 | Reduce hedge by 2 contracts |

**Cost of rebalancing:**
- Transaction costs: ~$50 per futures contract
- 6 contracts adjusted: $300/month
- On $100M portfolio: 0.0036% monthly = 0.04% annually
- **Small but real drag on performance**

---

## Real-World Duration Hedging Examples

### Example 1: Corporate Bond Portfolio Hedge (Winner)

**Setup:**

- **Date:** January 1, 2025
- **Portfolio Manager:** Fixed income fund
- **Portfolio:** $500M investment-grade corporate bonds
- **Average duration:** 6.8 years
- **Average yield:** 5.2% (Treasury 4.0% + spread 1.2%)
- **DV01:** $340,000

**View:**
- Bullish on credit (spreads will tighten)
- Neutral on rates (Fed on hold)
- Want: Credit exposure only
- Don't want: Rate exposure

**Hedge implementation:**

**Instrument:** 10-year Treasury futures
- Futures price: 112-00
- CTD duration: 8.2 years
- DV01 per contract: $100,000 × 1.12 × 8.2 × 0.0001 = $918

**Hedge ratio:**

$$
\text{Contracts} = \frac{340,000}{918} = 370 \text{ contracts}
$$

**Action:** Sell 370 ten-year Treasury futures at 112-00

**Trade evolution (6 months):**

**Month 1-2:**
- Rates: Unchanged (4.0%)
- Spreads: Unchanged (1.2%)
- Portfolio: Earning carry (+0.43%/month)
- Hedge: Small cost from roll ($15k total)
- **Net P/L:** +$4.3M - $15k = **+$4.28M (+0.86%)**

**Month 3 (March):**
- **Fed announcement:** Dovish surprise
- Rates: Fall to 3.75% (-25 bp)
- Spreads: Tighten to 1.05% (-15 bp) [risk-on sentiment]

| Position | Value Change | Calculation |
|----------|--------------|-------------|
| Corporate bonds (rate) | +$8.5M | $340k × 25 bp |
| Corporate bonds (spread) | +$5.1M | $340k × 15 bp |
| **Total bonds** | **+$13.6M** | **+2.72%** |
| Futures hedge | -$8.5M | Offset rate gain |
| **Net P/L** | **+$5.1M** | **+1.02%** |

**Perfect! Hedge neutralized rate move, captured spread tightening.**

**Month 4-6:**
- Rates: Stable at 3.75%
- Spreads: Continued tightening to 0.95% (total -25 bp from start)
- Portfolio: Earning carry
- Additional spread gain: +$8.5M

**6-month results:**

| Component | P/L | Return |
|-----------|-----|--------|
| Carry (6 months) | +$13.0M | +2.60% |
| Spread tightening | +$17.0M | +3.40% |
| Rate changes (hedged) | $0M | 0.00% |
| Hedge costs | -$90k | -0.02% |
| **Total** | **+$29.9M** | **+5.98%** |

**Why it worked:**

1. **Correctly hedged rate risk:** Avoided -$8.5M loss in Month 3
2. **Isolated credit view:** Captured +$17M spread tightening
3. **Earned carry:** +$13M over 6 months
4. **Low hedge cost:** Only -$90k in transaction costs
5. **Disciplined rebalancing:** Adjusted hedge monthly as DV01 changed

**Without hedge:**

If not hedged, Month 3 would have been +$13.6M instead of +$5.1M.

But: Would have been exposed to rate risk both ways. If rates had risen instead, would have lost significantly.

**The hedge allowed focus on credit view without rate risk.**

### Example 2: Pension Fund Asset-Liability Match (Winner)

**Setup:**

- **Fund:** Corporate pension plan
- **Liabilities:** $2 billion PV, duration 12.0 years
- **Assets:** $2 billion bond portfolio, duration 8.5 years
- **Problem:** Asset duration < Liability duration
- **Risk:** If rates fall, liabilities increase more than assets (funding gap widens)

**Initial situation:**

| Item | Value | Duration | DV01 |
|------|-------|----------|------|
| Liabilities | $2,000M | 12.0 | $2,400,000 |
| Assets | $2,000M | 8.5 | $1,700,000 |
| **Gap** | **$0** | **-3.5 years** | **-$700,000** |

**Interpretation:**
- If rates fall 1%: Liabilities up $24M, assets up $17M
- **Funding deficit increases by $7M!**

**Solution: Receive-fixed interest rate swap**

**Swap details:**
- Notional: $700M
- Receive: Fixed 4.5% (12-year swap rate)
- Pay: Floating (3-month LIBOR)
- Swap duration: Approximately 10.0 years
- Swap DV01: $700M × 10.0 × 0.0001 = $700,000

**After swap:**

| Item | Value | Duration | DV01 |
|------|-------|----------|------|
| Liabilities | $2,000M | 12.0 | $2,400,000 |
| Bond assets | $2,000M | 8.5 | $1,700,000 |
| Swap | $700M notional | 10.0 | $700,000 |
| **Net assets** | **$2,000M** | **≈12.0** | **$2,400,000** |
| **Gap** | **$0** | **≈0** | **≈$0** |

**Result:** Assets and liabilities now move together!

**Rate scenario testing:**

**Rates fall 1%:**
- Liabilities: +$24.0M
- Bonds: +$17.0M
- Swap: +$7.0M (receive-fixed gains value)
- **Net change: $0** (fully hedged!)

**Rates rise 1%:**
- Liabilities: -$24.0M
- Bonds: -$17.0M
- Swap: -$7.0M
- **Net change: $0** (fully hedged!)

**Benefits:**
1. **Eliminated funding risk** from rate changes
2. **Regulatory capital relief** (lower VaR)
3. **Can focus on credit/carry** for alpha generation
4. **Low cost:** Swap is off-balance sheet, minimal capital tied up

**10-year outcome:**

Over the decade, rates fell from 4.5% to 2.5%. Without the swap, the funding gap would have widened by $350M. With the swap, the funding status remained matched throughout.

### Example 3: High-Yield Bond Hedge Gone Wrong (Loser)

**Setup:**

- **Date:** May 1, 2025
- **Portfolio:** $200M high-yield corporate bonds
- **Average duration:** 4.5 years
- **Average yield:** 8.5% (Treasury 4.0% + spread 4.5%)
- **Credit rating:** B average
- **DV01:** $90,000

**Manager's view:**
- "Spreads are wide, good value"
- "Don't want rate risk"
- **Decided to hedge with Treasury futures**

**Hedge:**

- Sell 100 ten-year Treasury futures
- DV01 per contract: $900
- Total hedge DV01: -$90,000
- **Duration-neutral on paper**

**Month 1-2:**
- Rates stable, spreads stable
- Earning carry: +$1.4M
- Hedge cost: -$20k
- **Net: +$1.38M (+0.69%)**

**Month 3 (July): Corporate Stress Event**

- **News:** Major high-yield issuer bankruptcy
- **Market reaction:**
  - Flight to quality
  - Treasuries rally: Yields fall 3.75% → 3.50% (-25 bp)
  - High-yield spreads blow out: 4.5% → 6.0% (+150 bp)

**P/L analysis:**

| Position | Change | P/L | Notes |
|----------|--------|-----|-------|
| HY bonds (rate effect) | -25 bp | +$2.25M | Duration gain from rates |
| HY bonds (spread effect) | +150 bp | -$13.5M | Massive spread widening |
| **Total bonds** | | **-$11.25M** | **-5.63%** |
| Treasury futures (short) | -25 bp | -$2.25M | Lost on rally |
| **Net P/L** | | **-$13.5M** | **-6.75%** |

**Disaster!**

**What went wrong:**

1. **Wrong correlation assumption:**
   - Assumed: HY and Treasuries move together
   - Reality: Negative correlation in stress (flight to quality)
   - **Treasury hedge made it worse!**

2. **Ignored spread duration:**
   - Spread duration (4.5 years) was the real risk
   - Rate duration (4.5 years) was minor compared to spread risk
   - **Hedged the wrong risk!**

3. **False sense of security:**
   - "Duration neutral" meant nothing
   - Credit risk dominated
   - Hedge was irrelevant to actual risk

**Aftermath:**

Manager closed hedge at loss (-$2.25M), realized total loss of -$13.5M.

**Lesson:**

**High-yield bonds should NOT be duration-hedged with Treasuries!**

Why?
- Correlation breaks down in stress
- Spread risk >> rate risk
- Hedge can make volatility worse
- Better to hedge with HY index or credit default swaps

### Example 4: MBS Portfolio Convexity Disaster (Loser)

**Setup:**

- **Portfolio:** $300M mortgage-backed securities (MBS)
- **Duration:** 5.5 years
- **Convexity:** -45 (negative!)
- **DV01:** $165,000

**Why negative convexity?**
- MBS have prepayment risk
- Rates fall → homeowners refinance → bonds prepay (bad for investor)
- Rates rise → prepayments slow → duration extends (also bad)

**Hedge attempt:**

- Sold 180 ten-year Treasury futures
- DV01: $165,000
- **Matched duration at current rates (5.0%)**

**Scenario: Rates fall sharply**

**Month 1 (June):**
- Fed cuts rates 50 bp: 5.0% → 4.5%

**Expected (if linear duration):**

| Position | Expected P/L |
|----------|-------------|
| MBS | +$165k × 50 = +$8.25M |
| Futures | -$8.25M |
| Net | $0 |

**Actual result:**

| Position | Actual P/L | Reason |
|----------|-----------|--------|
| MBS | +$4.5M | Prepayment fears limited gains (negative convexity) |
| Futures | -$8.25M | Full linear loss |
| **Net** | **-$3.75M** | **-1.25%** |

**What happened:**

**Negative convexity destroyed the hedge:**
- MBS duration shortened from 5.5 → 4.0 years (prepayment speed up)
- Futures duration stayed at 8.2 years
- **Hedge became over-hedged!**

**Month 2 (July):**
- Rates continue falling: 4.5% → 4.0% (another -50 bp)

**Before rebalancing hedge:**

| Position | P/L |
|----------|-----|
| MBS | +$3.0M (duration now only 4.0) |
| Futures | -$8.25M (still 180 contracts) |
| **Net** | **-$5.25M** |

**Cumulative loss: -$9.0M (-3.0%)**

**Manager finally rebalanced:**
- Reduced futures to 130 contracts
- But damage already done

**Total outcome (3 months):**
- Rates fell 100 bp total (very bullish for bonds!)
- Expected gain if unhedged: +$18M
- Expected gain if perfect hedge: $0
- **Actual result: -$9M (hedge made it worse)**

**Lessons:**

1. **Negative convexity needs different hedge:**
   - Can't use linear duration hedge
   - Need dynamic hedging or options
   - MBS require sophisticated convexity management

2. **Rebalancing critical:**
   - Should have rebalanced weekly, not monthly
   - Duration changed dramatically with rates
   - Static hedge became toxic

3. **Know your instruments:**
   - MBS ≠ regular bonds
   - Negative convexity is fundamental feature
   - Standard duration hedge doesn't work

---

## Entry and Exit Rules for Duration Hedging

### Entry Checklist (When to Hedge)

**Reasons to implement duration hedge:**

1. **Isolate specific exposure:**
   - [ ] Have view on credit spreads, not rates
   - [ ] Want carry, not duration risk
   - [ ] Isolating curve position (e.g., short 2s long 10s)

2. **Asset-liability matching:**
   - [ ] Duration gap between assets and liabilities
   - [ ] Need to match interest rate sensitivity
   - [ ] Regulatory requirement

3. **Risk management:**
   - [ ] Duration risk exceeds risk limit
   - [ ] Portfolio too sensitive to rate changes
   - [ ] Want to reduce VaR or volatility

4. **Tactical positioning:**
   - [ ] Bearish on rates but bullish on credit
   - [ ] Want to be short rates without selling bonds
   - [ ] Temporary hedge for specific event (FOMC, etc.)

**Pre-hedge analysis:**

5. **Calculate hedge ratio:**
   - [ ] Portfolio DV01 calculated accurately
   - [ ] Hedge instrument DV01 known
   - [ ] Conversion factors included (for futures)

6. **Assess basis risk:**
   - [ ] Correlation between portfolio and hedge > 0.85
   - [ ] Understand tracking error
   - [ ] Accept residual risk

7. **Check costs:**
   - [ ] Transaction costs calculated
   - [ ] Carry/financing costs estimated
   - [ ] Net benefit justifies hedge

**If ANY critical checkbox not checked → Reconsider hedge or use different instrument!**

### Hedge Monitoring (Ongoing)

**Daily:**

1. **Mark positions:**
   - Portfolio value
   - Hedge value
   - Net exposure

2. **Check DV01:**
   - Has portfolio DV01 changed significantly (>5%)?
   - If yes: Consider rebalancing

**Weekly:**

3. **Hedge effectiveness:**
   - Calculate realized correlation
   - Compare actual vs. expected hedge performance
   - Adjust if tracking error too high

4. **Convexity monitoring:**
   - Has convexity impact become material?
   - For large rate moves (>50 bp): Rebalance

**Monthly:**

5. **Full rebalance:**
   - Recalculate portfolio DV01
   - Adjust hedge to maintain neutral
   - Update hedge ratio for yield changes

6. **Cost analysis:**
   - Total hedge costs vs. benefit
   - Rolling costs (futures)
   - Carry impact

### Exit Rules (When to Remove Hedge)

**Planned exits:**

1. **View change:**
   - No longer need rate neutrality
   - Want to take rate exposure
   - Spread view no longer compelling

2. **End of holding period:**
   - Tactical hedge for specific event (now passed)
   - Asset-liability match no longer needed
   - Bonds maturing soon (duration naturally decreasing)

**Forced exits:**

3. **Hedge ineffective:**
   - Correlation breakdown (<0.70)
   - Basis risk too high
   - Tracking error unacceptable
   - **Exit and find better hedge instrument**

4. **Cost too high:**
   - Negative carry exceeding benefit
   - Roll costs too expensive
   - Better to just sell bonds

5. **Regulatory/risk limits:**
   - Derivative exposure limits hit
   - Margin requirements too high
   - Counterparty limits reached

### Rebalancing Rules

**Threshold rebalancing:**

$$
\text{Rebalance if: } |\text{Net DV01}| > 0.10 \times \text{Target DV01}
$$

**Example:**
- Target DV01: $0 (neutral)
- Threshold: $0 ± $20,000
- Current net DV01: -$25,000
- **Action: Rebalance (outside threshold)**

**Time-based rebalancing:**

- **Monthly:** Standard for most portfolios
- **Weekly:** For volatile portfolios or large positions
- **Daily:** For MBS or other high-convexity portfolios

**Event-based rebalancing:**

- Large rate move (>50 bp in day)
- Significant portfolio changes (new issuance, redemptions)
- CTD switch in futures
- Major central bank announcement

---

## Best Case Scenario

### The Perfect Credit Carry Trade with Duration Hedge

**Setup:**

- **Date:** Q1 2025 (January-March)
- **Portfolio Manager:** Fixed income hedge fund
- **Capital:** $1 billion
- **Strategy:** Long investment-grade credit, hedge all rate risk

**Market environment:**
- Corporate credit spreads: 140 bp (80th percentile, wide)
- Treasury yields: 4.25% (10-year)
- Fed: Expected to remain on hold for 6-12 months
- View: Spreads will tighten as economy strengthens

**Portfolio construction:**

**Long positions:**
- $1B investment-grade corporate bonds
- Average maturity: 10 years
- Average coupon: 5.65%
- Average spread: 140 bp over Treasuries
- Duration: 8.2 years
- DV01: $820,000

**Hedge positions:**
- Sell 910 contracts 10-year Treasury futures
- Futures price: 110-00
- CTD duration: 8.1 years
- DV01 per contract: $902
- Total hedge DV01: -$820,820

**Net position:**
- Rate DV01: $820k - $820k ≈ **$0** (neutral)
- Spread DV01: $820k (full exposure)
- Carry: 5.65% on $1B = $56.5M annually
- Hedge cost: Minimal (futures financing ≈ 0)

**Month 1 (January):**

**Market:**
- Rates: Unchanged at 4.25%
- Spreads: Unchanged at 140 bp
- No surprises

**P/L:**

| Position | Monthly P/L | Notes |
|----------|------------|-------|
| Corporate bonds carry | +$4.71M | 5.65% annualized |
| Mark-to-market | $0M | No rate or spread change |
| Futures cost | -$50k | Rolling/transaction costs |
| **Net** | **+$4.66M** | **+0.466%** |

**Month 2 (February):**

**Market:**
- Strong economic data released
- Risk-on sentiment
- Rates: Rise slightly to 4.35% (+10 bp)
- Spreads: **Tighten to 120 bp (-20 bp)** [risk-on!]

**P/L:**

| Position | P/L | Calculation |
|----------|-----|-------------|
| Bonds (rate effect) | -$8.2M | -10 bp × $820k DV01 |
| Bonds (spread) | +$16.4M | -20 bp spread × $820k DV01 |
| Carry | +$4.71M | Monthly coupon |
| **Total bonds** | **+$12.91M** | |
| Futures hedge | +$8.2M | Offset rate loss |
| Hedge costs | -$50k | |
| **Net** | **+$21.06M** | **+2.11%** |

**Perfect! The hedge worked exactly as intended.**

**Month 3 (March):**

**Market:**
- Continued strength
- Fed hints at dovish stance (no hikes coming)
- Rates: Fall to 4.15% (-20 bp from 4.35%)
- Spreads: Further tightening to 100 bp (-20 bp)

**P/L:**

| Position | P/L | Calculation |
|----------|-----|-------------|
| Bonds (rate effect) | +$16.4M | -20 bp × $820k DV01 |
| Bonds (spread) | +$16.4M | -20 bp spread × $820k DV01 |
| Carry | +$4.71M | Monthly coupon |
| **Total bonds** | **+$37.51M** | |
| Futures hedge | -$16.4M | Lost on rate rally |
| Hedge costs | -$50k | |
| **Net** | **+$21.06M** | **+2.11%** |

**Again, perfect execution!**

**Quarterly summary:**

| Month | Carry | Spread P/L | Rate P/L (bonds) | Hedge P/L | Net P/L | Monthly Return |
|-------|-------|------------|------------------|-----------|---------|----------------|
| Jan | +$4.71M | $0M | $0M | -$50k | +$4.66M | +0.466% |
| Feb | +$4.71M | +$16.4M | -$8.2M | +$8.2M | +$21.06M | +2.11% |
| Mar | +$4.71M | +$16.4M | +$16.4M | -$16.4M | +$21.06M | +2.11% |
| **Total** | **+$14.13M** | **+$32.8M** | **+$8.2M** | **-$8.35M** | **+$46.78M** | **+4.68%** |

**Decomposition of returns:**

$$
\begin{align}
\text{Total Return} &= \text{Carry} + \text{Spread Tightening} + \text{Net Rate Effect} \\
&= 1.41\% + 3.28\% + (-0.015\%) \\
&= 4.68\%
\end{align}
$$

**Annualized:** 4.68% × 4 = **18.7%**

**Why this was best case:**

1. **Perfect hedge execution:**
   - Rate DV01 maintained at zero
   - No tracking error
   - Hedge costs minimal (<0.02%)

2. **Correct view on spreads:**
   - Entered at wide spreads (140 bp)
   - Captured 40 bp tightening
   - Generated 3.28% from spread alone

3. **Harvested carry:**
   - 5.65% yield sustained
   - No defaults or downgrades
   - Full carry captured

4. **Hedge neutralized rates:**
   - In Feb: Rates rose, hedge protected
   - In Mar: Rates fell, hedge cost opportunity
   - **Net effect: Minimal (-0.015%)**

5. **Risk-adjusted excellence:**
   - Portfolio volatility: 1.5% monthly (mostly spread vol)
   - Unhedged volatility would have been: 3.5% monthly
   - **Sharpe ratio: 3.12** (exceptional)

**Comparison to unhedged:**

| Strategy | Return | Volatility | Sharpe |
|----------|--------|------------|--------|
| **Hedged** | **+4.68%** | **1.5%** | **3.12** |
| Unhedged | +5.51% | 3.5% | 1.57 |

**Hedged strategy:**
- Slightly lower return (gave up some rate rally upside)
- **Much lower volatility** (60% reduction)
- **Double the Sharpe ratio**
- Better risk-adjusted performance

**This is the power of duration hedging done right!**

---

## Worst Case Scenario

### The Treasury Futures Hedge Disaster

**Setup:**

- **Date:** Q2 2025 (April-June)
- **Portfolio Manager:** Regional bank investment portfolio
- **Portfolio:** $2B municipal bonds
- **Strategy:** Hedge with Treasury futures (mistake!)

**Portfolio details:**
- Municipal bonds: 10-year average maturity
- Yield: 3.5% (tax-exempt)
- Duration: 7.8 years
- DV01: $1,560,000
- Credit quality: AA average

**Initial hedge:**

- Sell 1,730 contracts 10-year Treasury futures
- Futures price: 110-00
- CTD duration: 8.1 years
- DV01 per contract: $902
- Total hedge DV01: -$1,560,000

**Seems matched on paper!**

**Month 1 (April):**

**Market:**
- Quiet month
- Rates unchanged
- Muni yields unchanged
- Carry accruing

**P/L:**

| Position | P/L |
|----------|-----|
| Muni bonds carry | +$5.83M |
| Futures cost | -$150k |
| **Net** | **+$5.68M (+0.28%)** |

**Looks good so far...**

**Month 2 (May): The Divergence Begins**

**Market events:**
- Tax revenue shortfall announced in several states
- Muni credit concerns
- **Muni-Treasury spread widening**
- But Treasury yields actually falling (flight to quality!)

**Rate changes:**
- Treasury yields: 4.25% → 4.05% (-20 bp) [rally]
- Muni yields: 3.50% → 3.70% (+20 bp) [selloff]

**P/L disaster:**

| Position | P/L | Calculation |
|----------|-----|-------------|
| Muni bonds | -$31.2M | +20 bp × $1,560k DV01 |
| Carry | +$5.83M | Monthly income |
| **Total munis** | **-$25.37M** | **-1.27%** |
| Treasury futures (short) | -$31.2M | Lost on -20 bp rally |
| **Net P/L** | **-$56.57M** | **-2.83%** |

**Catastrophic!**

**What went wrong:**

1. **Negative correlation in stress:**
   - Treasuries rallied (flight to quality)
   - Munis sold off (credit concerns)
   - **Correlation: -1.0** (worst possible!)

2. **Hedge made losses worse:**
   - Without hedge: Lost $25.37M
   - With hedge: Lost $56.57M
   - **Hedge doubled the loss!**

3. **Wrong hedge instrument:**
   - Should use muni futures (if available)
   - Or muni ETF swaps
   - Treasuries have low/negative correlation to munis in stress

**Month 3 (June): Panic and Capitulation**

**Market:**
- More state budget issues
- Muni selloff accelerates
- Treasury yields: 4.05% → 3.85% (-20 bp more)
- Muni yields: 3.70% → 4.00% (+30 bp more)

**P/L continued disaster:**

| Position | P/L |
|----------|-----|
| Muni bonds | -$46.8M (-30 bp × $1.56M) |
| Carry | +$5.83M |
| **Total munis** | **-$40.97M** |
| Treasury futures | -$31.2M (-20 bp again) |
| **Net** | **-$72.17M (-3.61%)** |

**Quarter-end total damage:**

| Month | Muni P/L | Futures P/L | Net P/L | Cumulative |
|-------|----------|-------------|---------|------------|
| Apr | +$5.68M | -$0.15M | +$5.68M | +$5.68M |
| May | -$25.37M | -$31.2M | -$56.57M | -$50.89M |
| Jun | -$40.97M | -$31.2M | -$72.17M | -$123.06M |
| **Total** | **-$60.66M** | **-$62.55M** | **-$123.06M** | **-6.15%** |

**Comparison to unhedged:**

| Strategy | Loss | Notes |
|----------|------|-------|
| **With Treasury futures hedge** | **-$123.06M (-6.15%)** | Hedge made it worse |
| Unhedged | -$60.66M (-3.03%) | Just muni losses |
| **Difference** | **-$62.4M worse!** | Hedge doubled losses |

**Bank consequences:**

1. **Regulatory issues:**
   - Capital ratio impaired
   - Regulator questions hedge strategy
   - Required to unwind hedge at worst time

2. **Mark-to-market hit:**
   - Portfolio marked down $123M
   - Quarterly earnings destroyed
   - Stock price fell 15%

3. **Reputation damage:**
   - Investment committee fired portfolio manager
   - Board implemented new risk controls
   - Banned derivatives hedging without approval

**How it should have been done:**

**Alternative 1: No hedge**
- Accept duration risk
- Loss: -$60.66M (-3.03%)
- Better than actual result!

**Alternative 2: Muni-specific hedge**
- Use muni bond index swaps
- Or muni ETF options
- Or just reduce muni holdings
- Correlation would be positive (0.85+)

**Alternative 3: Reduce position**
- If worried about rates, sell some munis
- Buy shorter-duration munis
- More capital intensive but effective

**Lessons:**

1. **Correlation is key:**
   - Never hedge with negatively correlated instrument
   - Check historical correlation in stress scenarios
   - Munis and Treasuries diverge in credit stress

2. **Use appropriate hedge:**
   - Hedge instrument should track portfolio
   - Treasury futures hedge Treasuries, not munis
   - Basis risk can be larger than duration risk!

3. **Sometimes no hedge is better:**
   - If no good hedge available, accept risk or reduce position
   - Bad hedge can make losses worse
   - Don't hedge just to say you hedged

4. **Understand your portfolio:**
   - Munis have credit risk, tax risk, liquidity risk
   - Duration is not the only risk
   - Other risks can dominate in crisis

**Final outcome:**

Bank eventually closed hedge in July after 3 months, locking in -$62.55M loss on futures. Muni portfolio recovered over next 6 months as credit fears subsided, but reputational damage and regulatory scrutiny persisted.

---

## What to Remember

### Core Concept

**Duration hedging neutralizes interest rate sensitivity:**

$$
\Delta P_{\text{portfolio}} + \Delta P_{\text{hedge}} \approx 0 \text{ for parallel yield shifts}
$$

- Duration measures bond's sensitivity to rate changes
- DV01 quantifies dollar impact per 1 bp move
- Hedge ratio: Match portfolio DV01 with hedge DV01
- Goal: Isolate non-rate exposures (credit, carry, curve)

### The Setup

**Basic duration hedge:**

$$
\text{Contracts} = \frac{\text{DV01}_{\text{portfolio}}}{\text{DV01}_{\text{hedge instrument}}}
$$

**Example:**
- Portfolio DV01: $100,000
- Futures DV01: $900
- **Contracts: 111 (short futures)**

**Common hedge instruments:**
- Treasury futures (most liquid)
- Interest rate swaps (OTC, flexible)
- Treasury bonds (cash market)
- Options on futures (for convexity)

### Key Metrics

**Duration:**

$$
D = -\frac{1}{P} \frac{\partial P}{\partial y}
$$

Measures % price change per 1% yield change.

**DV01:**

$$
\text{DV01} = D \times P \times 0.0001
$$

Dollar change per 1 bp yield change.

**Convexity:**

$$
C = \frac{1}{P} \frac{\partial^2 P}{\partial y^2}
$$

Curvature in price-yield relationship.

**Hedge effectiveness:**

$$
\text{Effectiveness} = 1 - \frac{\sigma_{\text{hedged}}}{\sigma_{\text{unhedged}}}
$$

Typically 70-95% for good hedges.

### Entry Conditions

**When to hedge:**

1. **Isolate specific exposure** (credit, carry, curve view)
2. **Asset-liability matching** (pension, insurance)
3. **Risk management** (exceed VaR limits)
4. **Tactical positioning** (bearish rates, bullish credit)

**Pre-hedge checklist:**

- [ ] Portfolio DV01 calculated
- [ ] Hedge instrument selected
- [ ] Correlation > 0.85
- [ ] Basis risk acceptable
- [ ] Costs justified

### Monitoring and Rebalancing

**Rebalance when:**

- Net DV01 > 10% of target
- Large rate moves (>50 bp)
- Portfolio changes (new bonds, maturities)
- Monthly (standard practice)
- Weekly (for convex portfolios like MBS)

**Hedge effectiveness monitoring:**

$$
\text{Tracking Error} = \sigma(\text{Portfolio Return} - \text{Expected Hedged Return})
$$

Target: <0.30% monthly

### Exit Conditions

**Remove hedge when:**

1. **View change** (want rate exposure)
2. **Hedge ineffective** (correlation <0.70)
3. **Cost too high** (negative carry exceeds benefit)
4. **Portfolio changed** (bonds matured, sold)
5. **Event passed** (tactical hedge no longer needed)

### Common Mistakes to Avoid

1. **Wrong hedge instrument** (e.g., Treasuries for munis)
   - Check correlation in stress scenarios
   - Use instrument that tracks portfolio

2. **Ignoring convexity** (especially MBS, callable bonds)
   - Duration changes as rates move
   - Need dynamic rebalancing or options

3. **Over-hedging** (hedge credit risk by mistake)
   - Duration hedge removes rate risk only
   - Credit spreads still move

4. **No rebalancing** (static hedge drifts)
   - Duration changes with time and rates
   - Needs monthly adjustment minimum

5. **Assuming correlation stable** (it breaks in stress)
   - Correlation changes in crisis
   - Back-test hedge in historical stress periods

6. **Ignoring costs** (roll costs, transaction costs)
   - Futures have roll costs
   - Bid-ask on swaps
   - May exceed benefit

7. **Hedging illiquid with liquid** (basis blowout)
   - Illiquid bonds vs. liquid futures
   - Basis can widen dramatically in stress

8. **Not understanding portfolio** (munis, HY, EM, MBS)
   - Each has unique risks
   - Standard hedge may not work

### Performance Expectations

**Well-hedged portfolio:**

- **Rate volatility:** Reduced 70-95%
- **Total volatility:** Reduced 30-60% (credit risk remains)
- **Sharpe ratio:** Typically improves 50-100%
- **Tracking error:** 0.20-0.50% monthly
- **Cost:** 0.05-0.15% annually

**Returns decomposition (example):**

| Component | Hedged | Unhedged |
|-----------|--------|----------|
| Carry | +4.5% | +4.5% |
| Spread | -1.0% | -1.0% |
| Rates | 0.0% | -2.5% |
| Hedge cost | -0.1% | 0.0% |
| **Total** | **+3.4%** | **+1.0%** |

**Hedge improved return AND reduced risk!**

### Comparison to Alternatives

**vs. Selling bonds:**

| Duration Hedge | Sell Bonds |
|---------------|------------|
| Keep credit exposure | Lose credit exposure |
| Keep carry | Lose carry |
| Low transaction cost | High transaction cost |
| Flexible (can unwind) | Permanent |
| Basis risk | No basis risk |

**vs. Rate swaps:**

| Futures Hedge | Rate Swaps |
|--------------|------------|
| Exchange-traded | OTC |
| Standardized | Customizable |
| Lower cost | Higher cost |
| Daily margin | Counterparty risk |
| Less flexible | Very flexible |

### When to Use Duration Hedging

**Ideal for:**

- Investment-grade corporate bonds
- Treasury portfolios (tactical positioning)
- Asset-liability matching
- Carry trades (credit, EM, HY with rate hedge)

**Not suitable for:**

- High-yield bonds (credit risk dominates)
- Municipal bonds (use muni-specific hedges)
- Callable bonds (convexity too complex)
- Very illiquid bonds (basis risk too high)

### Hedge Instruments Comparison

| Instrument | Liquidity | Cost | Flexibility | Best For |
|------------|-----------|------|-------------|----------|
| **Treasury futures** | Highest | Lowest | Medium | Large portfolios, short-term |
| **Rate swaps** | High | Medium | Highest | Long-term, custom notional |
| **Options on futures** | Medium | Highest | Medium | Convexity hedging |
| **Treasury bonds** | Medium | Medium | Low | Small portfolios, cash |

### Your Learning Path

**Phase 1: Understanding (Months 1-2)**
- Calculate duration, DV01 for sample bonds
- Understand futures pricing, CTD
- Study historical correlations

**Phase 2: Basic hedging (Months 3-6)**
- Hedge simple Treasury portfolio
- Practice rebalancing
- Monitor tracking error

**Phase 3: Credit portfolios (Months 7-12)**
- Hedge IG corporate bonds
- Isolate credit spreads
- Measure hedge effectiveness

**Phase 4: Advanced (Year 2+)**
- Key rate duration hedging
- Convexity management
- Dynamic hedging strategies
- Cross-market hedges

### Final Wisdom

> "Duration hedging is not about predicting interest rates—it's about choosing which risks to take. The portfolio manager who hedges duration is saying: 'I have a view on credit spreads, not rates. Let me remove the rate noise and focus on what I understand.' The manager who uses Treasury futures to hedge municipal bonds is saying: 'I don't understand correlation risk and will pay dearly for my ignorance.' Know your portfolio, know your hedge instrument, and above all, know the correlation between them. A good hedge makes you sleep better. A bad hedge makes you wish you'd just sold the bonds."

**Keys to success:**

1. **Match hedge to portfolio** (correlation >0.85)
2. **Calculate DV01 accurately** (garbage in, garbage out)
3. **Rebalance regularly** (monthly minimum)
4. **Monitor effectiveness** (tracking error <0.30%)
5. **Understand costs** (roll, transaction, carry)
6. **Accept basis risk** (perfection impossible)
7. **Use appropriate instrument** (futures vs. swaps vs. bonds)
8. **Test in stress** (check correlation in crisis)

**Most important rule:**

$$
\text{Bad hedge} < \text{No hedge} < \text{Good hedge}
$$

If you can't get a good hedge (correlation >0.85, reasonable cost, acceptable basis risk), either:
1. Don't hedge (accept the risk)
2. Reduce position (sell some bonds)
3. Find better hedge instrument

Never hedge just to say you're hedged. A bad hedge can make your losses worse, as countless portfolio managers have learned the hard way. 🎯📊
