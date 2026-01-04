# Interest Rate Swaps

**Interest rate swaps (IRS)** are over-the-counter derivative contracts where two parties exchange fixed and floating interest rate cash flows on a notional principal amount, allowing institutions to hedge interest rate risk, convert floating-rate debt to fixed (or vice versa), manage duration exposure, and express views on the shape and level of the yield curve without exchanging the principal itself, forming the largest and most liquid segment of the global derivatives market with over $400 trillion in notional outstanding.

---

## The Core Insight

**The fundamental idea:**

- Exchange fixed rate payments for floating rate payments
- No principal exchange (notional is reference only)
- Duration transformation (floating to fixed or fixed to floating)
- Most liquid interest rate derivative (tight bid-ask spreads)
- Zero initial value at inception (fair pricing)
- Mark-to-market daily (gains/losses from rate changes)
- Standardized documentation (ISDA Master Agreement)
- Used by corporations, banks, asset managers, governments
- Can replicate with bond portfolio but swaps more efficient

**The key equations:**

$$
\text{Swap Value} = \text{PV(Fixed Leg)} - \text{PV(Floating Leg)}
$$

$$
\text{Swap Rate} = \frac{1 - DF_n}{\sum_{i=1}^n DF_i}
$$

$$
\text{DV01}_{\text{swap}} = \text{DV01}_{\text{fixed leg}} - \text{DV01}_{\text{floating leg}}
$$

$$
\text{Pay Fixed Swap} = \text{Short Bond} + \text{Long FRN}
$$

**You're essentially using: "The mathematical equivalence between swapping cash flows and owning a portfolio of bonds to transform duration exposure, hedge interest rate risk, or express directional views on rates, all while avoiding the capital requirements and transaction costs of trading actual bonds, making swaps the preferred instrument for institutional fixed income risk management."**

---

## What Are Interest Rate Swaps?

**Before trading swaps, understand the fundamental mechanics:**

### Basic Swap Structure

**Plain vanilla interest rate swap:**

**Parties:**
- **Party A (Pay Fixed):** Pays fixed rate, receives floating
- **Party B (Receive Fixed):** Receives fixed rate, pays floating

**Example: 5-year interest rate swap**

**Terms:**
- Notional: $100 million (not exchanged)
- Fixed rate: 4.50% (annual, 30/360)
- Floating rate: 3-month SOFR (quarterly reset)
- Maturity: 5 years
- Settlement: Net payments quarterly

**Cash flows (Year 1, Quarter 1):**

**If 3-month SOFR = 4.20%:**

- Party A pays fixed: $100M × 4.50% × 0.25 = $1,125,000
- Party A receives floating: $100M × 4.20% × 0.25 = $1,050,000
- **Net payment from A to B: $75,000**

**If 3-month SOFR = 4.80%:**

- Party A pays fixed: $1,125,000
- Party A receives floating: $100M × 4.80% × 0.25 = $1,200,000
- **Net payment from B to A: $75,000**

**Only net amount exchanged!**

### Replication via Bonds

**Pay fixed swap = Short fixed-rate bond + Long floating-rate note**

**Example:**

**Instead of entering pay fixed swap, could:**

1. **Issue (short) $100M 5-year fixed bond at 4.50%**
   - Pay 4.50% annually
   - Receive $100M at inception
   - Repay $100M at maturity

2. **Buy (long) $100M 5-year FRN at SOFR**
   - Receive SOFR quarterly
   - Pay $100M at inception
   - Receive $100M at maturity

**Net effect:**
- Pay 4.50% fixed (from bond)
- Receive SOFR floating (from FRN)
- Principal cancels out
- **Identical to pay fixed swap!**

**Why use swaps instead:**

- No principal exchange (no funding needed)
- No balance sheet impact (off-balance-sheet)
- Lower transaction costs (tighter bid-ask)
- More flexible (can unwind easily)
- Standardized (liquid market)
- **Efficiency**

### Swap Pricing at Inception

**Fair swap rate (no arbitrage):**

$$
R_{\text{swap}} = \frac{1 - DF_n}{\sum_{i=1}^n DF_i \times \delta_i}
$$

Where:
- $DF_i$ = Discount factor at time $i$
- $\delta_i$ = Day count fraction for period $i$
- $n$ = Number of periods

**Example: 2-year quarterly swap**

**SOFR curve:**

| Period | Time (years) | SOFR Rate | Discount Factor |
|--------|-------------|-----------|-----------------|
| 1 | 0.25 | 4.00% | 0.9901 |
| 2 | 0.50 | 4.10% | 0.9798 |
| 3 | 0.75 | 4.20% | 0.9692 |
| 4 | 1.00 | 4.30% | 0.9583 |
| 5 | 1.25 | 4.40% | 0.9471 |
| 6 | 1.50 | 4.50% | 0.9357 |
| 7 | 1.75 | 4.60% | 0.9241 |
| 8 | 2.00 | 4.70% | 0.9124 |

**Sum of discount factors:**

$$
\sum DF_i = 0.9901 + 0.9798 + \cdots + 0.9124 = 7.6167
$$

**Swap rate:**

$$
R_{\text{swap}} = \frac{1 - 0.9124}{7.6167 \times 0.25} = \frac{0.0876}{1.9042} = 4.60\%
$$

**This is the fair 2-year swap rate given the SOFR curve.**

### Mark-to-Market Valuation

**After inception, swap value changes with rates:**

**Value to pay fixed position:**

$$
V_{\text{pay fixed}} = \text{PV}_{\text{floating leg}} - \text{PV}_{\text{fixed leg}}
$$

**Example:**

**Initial swap (entered at 4.50%):**
- Notional: $100M
- Tenor: 5 years
- Fixed rate: 4.50%
- **Initial value: $0 (by construction)**

**After 1 year, rates have risen:**
- New 4-year swap rate: 5.00% (50 bps higher)
- Remaining maturity: 4 years

**Valuation:**

**Fixed leg PV (paying 4.50% when market is 5.00%):**

Each year pay $4.5M, discount at 5.00%:

$$
PV_{\text{fixed}} = \frac{4.5}{1.05} + \frac{4.5}{1.05^2} + \frac{4.5}{1.05^3} + \frac{4.5}{1.05^4}
$$

$$
= 4.286 + 4.082 + 3.887 + 3.702 = \$15.957M
$$

**Floating leg PV:**

For a floating rate note, PV at reset = Par = $100M

But we're between resets. Simplification: PV ≈ $100M

Actually, more precise: The floating leg PV equals par at each reset date. Since we just had a reset, the next payment is locked in, and remaining payments reset to market.

For simplicity in this example: $PV_{\text{floating}} \approx \$100M$

**Swap value to pay fixed:**

$$
V = 100 - 15.957 = \$84.043M
$$

Wait, that doesn't make sense. Let me recalculate properly.

Actually, I need to think about this more carefully. The fixed leg is an annuity, and the floating leg resets to par.

**Correct approach:**

**Pay fixed swap value:**

$$
V_{\text{pay fixed}} = PV_{\text{receive floating}} - PV_{\text{pay fixed}}
$$

When rates rise from 4.50% to 5.00%:

**Fixed leg (paying below-market rate is liability):**

The present value of paying 4.50% when market is 5.00% is LESS than par (the 4.50% annuity is worth less than 5.00% annuity at par).

Using annuity formula:

$$
PV_{\text{fixed}} = \text{Notional} \times R_{\text{swap}} \times \sum DF_i + \text{Notional} \times DF_n
$$

Actually, for a swap, there's no principal repayment, so:

$$
PV_{\text{fixed}} = \text{Notional} \times R_{\text{old}} \times \sum DF_i^{\text{new}}
$$

Let me use a simpler approach:

**The value of a pay fixed swap when rates rise = POSITIVE**

Why? Because you're paying a below-market fixed rate (4.50%) when the market rate is now 5.00%. This is valuable!

**Approximation using duration:**

- Initial swap rate: 4.50%
- New swap rate: 5.00%
- Change: +50 bps
- Modified duration of 4-year swap ≈ 3.5 years

**Value change:**

$$
\Delta V \approx -\text{Duration} \times \Delta R \times \text{Notional}
$$

For pay fixed (short duration):

$$
\Delta V = -(-3.5) \times 0.005 \times 100M = +\$1.75M
$$

**Pay fixed swap gained $1.75M in value when rates rose 50 bps.**

This makes sense: paying below-market fixed rate is profitable.

### Swap Mechanics in Practice

**Typical swap lifecycle:**

**Day 1 (Trade date):**
- Agree on terms (notional, rate, tenor, floating index)
- Sign ISDA Master Agreement
- Swap has zero value (par)
- **No upfront payment**

**Day 2-T (During life):**
- Floating rate resets quarterly (or semi-annually)
- Net payments exchanged
- Mark-to-market daily (unrealized P&L)
- Collateral posted if value moves significantly
- **Active management**

**Day T (Maturity):**
- Final payment exchange
- Swap terminates
- No principal exchange
- **Clean exit**

**Early termination:**

Can unwind swap by:
- Entering offsetting swap (opposite direction)
- Novation (transfer to third party)
- Cash settlement (pay/receive MTM value)
- **Flexibility**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/interest_rate_swap.png?raw=true" alt="interest_rate_swap" width="700">
</p>

**Figure 1:** Interest rate swap cash flow structure showing Party A paying fixed 4.50% and receiving floating SOFR on $100M notional. Only net payments are exchanged each period. The swap can be replicated by shorting a fixed-rate bond and longing a floating-rate note, but the swap requires no principal exchange and is more capital efficient.

---

## Economic Interpretation: Why Swaps Exist

**Beyond the mechanics, understanding the economic rationale:**

### Asset-Liability Mismatch Hedging

**The classic use case:**

**Bank scenario:**

**Assets:**
- $1B in 30-year fixed-rate mortgages at 5.00%
- Locked in for 30 years
- **Fixed rate inflow**

**Liabilities:**
- $1B in 3-month deposit funding at SOFR + 0.50%
- Resets quarterly
- **Floating rate outflow**

**Problem: Duration mismatch**

**If SOFR rises from 4.00% to 6.00%:**
- Mortgage income: $50M/year (unchanged)
- Funding cost: 6.50% × $1B = $65M/year
- Net: -$15M annual loss
- **Underwater!**

**Solution: Enter pay fixed swap**

**Swap terms:**
- Notional: $1B
- Pay fixed: 4.75%
- Receive floating: SOFR
- Tenor: 30 years

**New economics:**

**If SOFR = 6.00%:**
- Mortgage income: +$50M (fixed)
- Pay fixed on swap: -$47.5M
- Receive floating on swap: +$60M (SOFR)
- Deposit funding: -$65M (SOFR + 0.50%)
- **Net: +$50M - $47.5M + $60M - $65M = -$2.5M**

Much better than -$15M!

**Effectively converted floating liabilities to fixed:**

- After swap: Net income = $50M - $47.5M = $2.5M
- Locked in spread regardless of SOFR
- **Hedged interest rate risk**

### Comparative Advantage and Arbitrage

**Classic swap arbitrage:**

**Company A (AAA-rated):**
- Can borrow fixed at 5.00%
- Can borrow floating at SOFR + 0.30%
- Wants floating-rate debt
- **Prefers floating**

**Company B (BBB-rated):**
- Can borrow fixed at 6.50%
- Can borrow floating at SOFR + 1.20%
- Wants fixed-rate debt
- **Prefers fixed**

**Quality spread differential:**

- Fixed: 6.50% - 5.00% = 150 bps
- Floating: (SOFR + 1.20%) - (SOFR + 0.30%) = 90 bps
- **Differential: 60 bps arbitrage!**

**Arbitrage structure:**

**Company A:**
1. Borrows fixed at 5.00% (comparative advantage)
2. Enters swap: Pay SOFR, receive 5.40%
3. **Net: Pay SOFR - 0.40%** (better than SOFR + 0.30%)
4. **Saves 70 bps!**

**Company B:**
1. Borrows floating at SOFR + 1.20%
2. Enters swap: Pay 5.40%, receive SOFR
3. **Net: Pay 6.60%** (better than 6.50%)
4. **Wait, that's worse...**

Let me recalculate. The swap rate should split the arbitrage.

**Correct structure:**

**Company A:**
1. Borrows fixed at 5.00%
2. Swap: Pay floating (SOFR), Receive fixed (5.30%)
3. Net: Pay 5.00% - 5.30% + SOFR = **SOFR - 0.30%**
4. Saves: (SOFR + 0.30%) - (SOFR - 0.30%) = **60 bps vs borrowing floating directly**

**Company B:**
1. Borrows floating at SOFR + 1.20%
2. Swap: Pay fixed (5.30%), Receive floating (SOFR)
3. Net: Pay (SOFR + 1.20%) - SOFR + 5.30% = **6.50%**
4. Saves: 6.50% - 6.50% = **0 bps... still doesn't work**

Actually, let me reconsider. The arbitrage is split between the parties and the intermediary bank.

**With intermediary bank:**

**Company A:**
- Borrows fixed at 5.00%
- Swaps with bank: Pay SOFR, Receive 5.25%
- Net: SOFR - 0.25%
- Saves: (SOFR + 0.30%) - (SOFR - 0.25%) = **55 bps**

**Company B:**
- Borrows floating at SOFR + 1.20%
- Swaps with bank: Pay 5.35%, Receive SOFR
- Net: 6.55%
- Saves: 6.50% - 6.55% = **-5 bps (worse!)**

Hmm, this classic example is tricky. Let me use the textbook version:

The total arbitrage available is 60 bps (150 - 90). This can be split:
- Company A saves: 25 bps
- Company B saves: 25 bps
- Bank earns: 10 bps

**A final cost: SOFR + 0.05% (vs SOFR + 0.30% → saves 25 bps)**
**B final cost: 6.25% (vs 6.50% → saves 25 bps)**
**Bank spread: 10 bps**

This works if the swap rates are set appropriately.

The key point: **Quality spread differential creates arbitrage opportunity that swaps can capture.**

### Speculation on Interest Rates

**Directional view expression:**

**Bullish on rates (expect rates to fall):**

$$
\text{Enter receive fixed swap (long rates)}
$$

**Example:**

- Current 10-year swap rate: 4.50%
- View: Rates will fall to 3.50%
- Enter $100M receive fixed swap at 4.50%

**If rates fall to 3.50%:**
- Duration: ~7 years
- Value gain: 7 × 1.00% × $100M = **+$7M**

**Why use swaps instead of bonds:**
- No upfront capital (vs buying $100M bonds)
- Better liquidity (can trade $100M-1B instantly)
- Lower transaction costs (2-3 bps vs 10-20 bps for bonds)
- **Leverage without repo financing**

### Curve Positioning

**Express views on curve shape:**

**Steepener using swaps:**

- Receive fixed 10-year swap (long 10-year rates)
- Pay fixed 2-year swap (short 2-year rates)
- Duration-neutral by notional adjustment
- **Profit if curve steepens**

**Example:**

- 2-year DV01: $19/bp per $1M
- 10-year DV01: $70/bp per $1M
- Ratio: 70/19 = 3.68

**Position:**
- Receive fixed $100M 10-year swap
- Pay fixed $368M 2-year swap
- **Duration-neutral, pure curve play**

---

## Key Terminology

**Fixed Leg:**

$$
\text{Fixed payment each period}
$$

- Pays/receives fixed rate (e.g., 4.50%)
- Determined at inception
- Acts like fixed-rate bond
- **Duration exposure**

**Floating Leg:**

$$
\text{Floating payment resets to index}
$$

- Typically SOFR (Secured Overnight Financing Rate)
- Resets quarterly or semi-annually
- Acts like floating-rate note
- **Minimal duration**

**Notional Principal:**

$$
\text{Reference amount (not exchanged)}
$$

- Used to calculate payments
- Never actually exchanged
- Can be amortizing or accreting
- **Calculation basis**

**Swap Rate:**

$$
R_{\text{swap}} = \frac{1 - DF_n}{\sum DF_i}
$$

- Fixed rate at inception (zero value)
- Quoted in basis points
- Varies by tenor (2yr, 5yr, 10yr, 30yr)
- **Market price**

**DV01 (Dollar Value of 01):**

$$
\text{DV01}_{\text{swap}} = \text{Change in value per 1 bp move}
$$

- Pay fixed: Positive DV01 (gains when rates rise)
- Receive fixed: Negative DV01 (gains when rates fall)
- Similar to bond DV01
- **Risk metric**

**SOFR (Secured Overnight Financing Rate):**

- Replaced LIBOR (2023)
- Overnight repo rate (secured)
- Published daily by NY Fed
- Compounds for term rates
- **Reference rate**

**ISDA Master Agreement:**

- Standard legal documentation
- International Swaps and Derivatives Association
- Defines terms, netting, collateral
- **Legal framework**

**Swap Spread:**

$$
\text{Swap Spread} = \text{Swap Rate} - \text{Treasury Yield}
$$

- Typically 20-80 bps
- Reflects credit/liquidity premium
- Varies by tenor
- **Value indicator**

**Mark-to-Market (MTM):**

$$
\text{MTM} = \text{PV(receive leg)} - \text{PV(pay leg)}
$$

- Daily valuation
- Unrealized P&L
- Determines collateral posting
- **Current value**

**Notional Reset:**

- Floating leg resets to par at each fixing
- Fixed leg value changes with rates
- **Key valuation principle**

**Day Count Convention:**

- Fixed: 30/360 or ACT/360
- Floating: ACT/360 (SOFR)
- Affects payment calculations
- **Technical detail**

---

## The Greeks (Swap Risk Metrics)

**Swaps have risk characteristics similar to bonds:**

### Delta (Interest Rate Sensitivity)

**Definition:**

$$
\Delta_{\text{swap}} = \frac{\partial V}{\partial r}
$$

**Pay fixed swap:**

- Positive delta (like short duration bond)
- Gains when rates rise
- **Bullish positioning**

**Example:**

**$100M pay fixed 10-year swap:**

- Modified duration: ~7 years
- DV01: $70,000 per bp
- **Delta = +$70,000/bp**

**If rates rise 1%:**

$$
\text{Gain} = 70,000 \times 100 = \$7,000,000
$$

**Receive fixed swap:**

- Negative delta (like long duration bond)
- Gains when rates fall
- **Bearish positioning**

**Same swap, receive fixed:**

- Delta = -$70,000/bp
- **If rates fall 1%: Gain $7M**

### Gamma (Convexity)

**Definition:**

$$
\Gamma_{\text{swap}} = \frac{\partial^2 V}{\partial r^2}
$$

**Pay fixed:**

- Negative gamma (short convexity)
- Like short bond position
- Loses from large rate moves both ways
- **Convexity sold**

**Receive fixed:**

- Positive gamma (long convexity)
- Like long bond position
- Benefits from large rate moves
- **Convexity owned**

**But gamma is small:**

Swaps have less convexity than bonds of similar duration because:
- Floating leg has near-zero duration
- Only fixed leg contributes convexity
- **Lower convexity than bonds**

### Theta (Time Decay / Carry)

**Definition:**

$$
\Theta = \frac{\partial V}{\partial t}
$$

**If swap off-market:**

**Pay fixed below market:**
- Swap has positive value
- This value decays toward zero over time
- **Negative theta (lose value with time)**

**Pay fixed above market:**
- Swap has negative value
- Negative value grows toward zero
- **Positive theta (gain value with time)**

**At-market swap:**
- Zero theta initially
- **No time decay effect**

### Vega (Volatility Sensitivity)

**Swaps have no direct vega** (no embedded options like swaptions)

**But indirectly:**

- Higher volatility → Wider bid-ask spreads
- Execution costs increase
- **Trading cost impact**

### Rho (Rate Level Sensitivity)

**Similar to delta but specifically:**

$$
\rho = \frac{\partial V}{\partial r_{\text{risk-free}}}
$$

**For swaps, rho ≈ delta**

Interest rate changes directly impact swap value.

---

## Strategy Selection: Which Swap for Which Purpose

**Different swap applications:**

### Hedging Floating-Rate Debt

**Corporate borrower with floating-rate loan:**

**Problem:**
- Issued $500M floating-rate notes at SOFR + 200 bps
- Maturity: 7 years
- Fear: Rising rates increasing interest expense
- **Rate risk exposure**

**Solution: Pay fixed swap**

**Swap terms:**
- Notional: $500M
- Pay fixed: 4.75%
- Receive: SOFR flat
- Tenor: 7 years

**Economic effect:**

**Before swap:**
- Interest expense: SOFR + 200 bps

**After swap:**
- Pay floating on debt: SOFR + 200 bps
- Pay fixed on swap: 4.75%
- Receive floating on swap: SOFR
- **Net: 6.75% fixed (locked in!)**

**Benefits:**
- Certainty of cash flows
- Budget planning possible
- No rate risk
- **Hedged**

### Hedging Fixed-Rate Assets

**Asset manager with fixed-rate bond portfolio:**

**Problem:**
- Owns $1B 10-year Treasuries at 4.50%
- Duration: 8 years
- Expect rates to rise
- Don't want to sell bonds (tax, transaction costs)
- **Want to reduce duration**

**Solution: Pay fixed swap**

**Swap terms:**
- Notional: $1B
- Pay fixed: 4.60%
- Receive: SOFR
- Tenor: 10 years

**Effect:**

**Without swap:**
- If rates rise 1%: Loss = 8 × 1% × $1B = **-$80M**

**With swap:**
- Bond loss: -$80M
- Swap gain: +$70M (duration 7 × 1% × $1B)
- Net loss: -$10M
- **Reduced duration from 8 to ~1 year**

### Duration Extension

**Pension fund with short-duration assets:**

**Problem:**
- Assets: $5B in 3-year bonds (duration 2.7)
- Liabilities: $5B in 20-year obligations (duration 15)
- **Duration mismatch: -12.3 years**

**Solution: Receive fixed long-tenor swaps**

**Swap terms:**
- Notional: $3B
- Receive fixed: 5.00%
- Pay: SOFR
- Tenor: 30 years
- Duration: 18 years

**Effect:**

**Asset duration before:** 2.7 years
**Swap duration added:** 18 × ($3B / $5B) = 10.8 years
**Combined duration:** 2.7 + 10.8 = **13.5 years**

**Much better matched to 15-year liability duration!**

### Spread Trades

**Relative value between swaps and Treasuries:**

**Swap spread trade:**

**Observation:**
- 10-year swap rate: 4.60%
- 10-year Treasury yield: 4.20%
- Swap spread: 40 bps (historically wide)
- **Mean reversion opportunity**

**Trade:**
- Receive fixed on $100M 10-year swap (4.60%)
- Short $100M 10-year Treasuries (4.20%)
- **Profit if spread narrows**

**If spread narrows to 30 bps:**
- Swap rate falls to 4.50% (gain on receive fixed)
- Treasury yield unchanged at 4.20%
- Profit from 10 bp swap spread tightening
- **Spread compression profit**

### Comparison Table

| Application | Swap Direction | Purpose | Typical User |
|-------------|---------------|---------|--------------|
| Hedge floating debt | Pay fixed | Lock in rate | Corporate borrower |
| Hedge fixed assets | Pay fixed | Reduce duration | Asset manager |
| Extend duration | Receive fixed | Match liabilities | Pension fund |
| Rate speculation | Pay/Receive | Express view | Hedge fund |
| Curve trades | Combination | Shape positioning | Macro trader |
| Spread arbitrage | Receive vs short | Relative value | Arb desk |

---

## Time Selection: When to Enter Swap Positions

**Swap timing depends on purpose:**

### Hedging Applications (Timing Less Critical)

**For hedgers:**

$$
\text{Enter when risk arises, not when rates "look good"}
$$

**Example:**

**Corporation issuing floating-rate debt:**
- Issue date: March 15
- Hedge immediately with pay fixed swap
- Don't try to time the market
- **Lock in rate certainty**

**Why:**

- Primary goal: Eliminate risk
- Speculation on timing = defeating purpose of hedge
- Basis risk from delay
- **Immediate hedging best practice**

### Speculative Applications (Timing Critical)

**For directional traders:**

**Enter pay fixed when:**

- Expect rates to rise
- Fed hiking cycle starting
- Inflation accelerating
- Economic growth strong
- **Bearish on bonds**

**Example:**

**January 2022:**
- Fed signaling aggressive hikes
- Inflation at 7%
- Enter large pay fixed swaps
- Rates rose 250 bps over year
- **Profitable trade**

**Enter receive fixed when:**

- Expect rates to fall
- Recession concerns
- Fed cutting expected
- Deflation risk
- **Bullish on bonds**

**Example:**

**August 2007:**
- Credit crisis beginning
- Fed will cut aggressively
- Enter receive fixed swaps
- Rates fell 400+ bps
- **Highly profitable**

### Curve Trades (Shape-Dependent)

**Steepener:**

$$
\text{Enter when curve flat, expect steepening}
$$

**Indicators:**
- Inverted or very flat (<50 bps)
- Recession expectations building
- Fed near terminal rate
- **Curve will steepen**

**Flattener:**

$$
\text{Enter when curve steep, expect flattening}
$$

**Indicators:**
- 2s10s > 200 bps (very steep)
- Fed starting hiking cycle
- Late economic expansion
- **Curve will flatten**

---

## Maximum Profit and Loss

### Maximum Profit (2008 Crisis Receive Fixed)

**Setup:**

- Date: September 2008
- Trader: Hedge fund macro desk
- Capital: $500M
- Strategy: Receive fixed swaps (bullish on bonds)

**Position (September 15, 2008 - Lehman collapse):**

**Entry:**
- $5B notional 10-year receive fixed swaps
- Swap rate: 3.80%
- 10-year Treasury: 3.60%
- Swap spread: 20 bps
- **Leveraged 10× (notional to capital)**

**Thesis:**
- Financial crisis will force massive Fed easing
- Rates will plummet
- Receive fixed = profit from falling rates
- **High conviction**

**The rally:**

**September-December 2008:**

- Fed cuts from 2.00% → 0.00-0.25%
- 10-year swap rate: 3.80% → 2.20% (-160 bps!)
- Flight to quality extreme

**P&L calculation:**

**Swap value change:**

- Duration: ~7 years
- Rate change: -160 bps = -1.60%
- Value per $100M: 7 × 1.60% = 11.2%

**Total gain:**

$$
\$5B \times 11.2\% = \$560M
$$

**On $500M capital:**

$$
\text{Return} = \frac{\$560M}{\$500M} = 112\%
$$

**In 3.5 months!**

**Annualized: >300%**

**Why this worked perfectly:**

1. ✅ Correct macro call (financial crisis → Fed easing)
2. ✅ Extreme rate move (160 bps in 3 months)
3. ✅ High leverage (10× via swaps vs would need 10× repo for bonds)
4. ✅ Better liquidity than bonds (could trade $5B easily)
5. ✅ No funding issues (swaps don't require financing)
6. ✅ Perfect timing (entered right at Lehman collapse)
7. ✅ Held through volatility
8. **Career-making trade**

### Maximum Loss (2022 Receive Fixed Disaster)

**Setup:**

- Date: January 2022
- Trader: Fixed income relative value fund
- Capital: $200M
- Strategy: Receive fixed (wrong direction)

**Position (January 2022):**

**Entry:**
- $2B notional 30-year receive fixed swaps
- Swap rate: 2.15%
- 30-year Treasury: 1.90%
- **10× leverage**

**Thesis:**
- "Inflation is transitory" (Fed messaging)
- Rates too low, but won't rise much
- Receive fixed is "safe income"
- **Completely wrong**

**The disaster:**

**January-October 2022:**

- Fed hiked from 0.25% → 4.00% (375 bps in 9 months!)
- 30-year swap rate: 2.15% → 4.45% (+230 bps)
- Fastest rate rise in 40 years

**P&L calculation:**

**Swap value change:**

- Duration: ~18 years
- Rate change: +230 bps = +2.30%
- Loss per $100M: 18 × 2.30% = 41.4%

**Total loss:**

$$
\$2B \times 41.4\% = \$828M
$$

**But fund only had $200M capital!**

**Margin call cascade:**

**Month 3 (April):**
- MTM loss: $300M
- Capital exhausted
- Margin call from clearinghouse
- **Forced partial liquidation**

**Month 6 (July):**
- Additional losses: $200M
- No capital remaining
- **Full liquidation at worst prices**

**Final outcome:**

- Capital: $200M → $0 (total loss)
- Fund liquidated
- Investors lost everything
- **-100% return**

**What went catastrophically wrong:**

1. ❌ Wrong macro view (inflation NOT transitory)
2. ❌ Ignored warning signs (7% CPI)
3. ❌ Fought the Fed (Fed clearly turning hawkish)
4. ❌ Maximum leverage (10×)
5. ❌ Longest duration (30-year swaps = highest risk)
6. ❌ No stop-loss
7. ❌ No risk management
8. ❌ Largest rate move in 40 years
9. **Total destruction**

---

## When to Use Interest Rate Swaps

### Ideal Applications

**1. Asset-liability management:**

- Banks (duration mismatch)
- Pension funds (extend duration)
- Insurance companies (match liabilities)
- **Core hedging**

**2. Corporate treasury:**

- Convert floating debt to fixed
- Convert fixed debt to floating
- Manage interest rate exposure
- **Risk management**

**3. Portfolio management:**

- Modify duration without trading bonds
- Express rate views efficiently
- Curve positioning
- **Tactical allocation**

**4. Relative value trading:**

- Swap spreads
- Curve trades
- Cross-currency basis
- **Arbitrage strategies**

### Specific Use Cases

**Use Case 1: Bank hedging mortgage portfolio**

**Bank:**
- Assets: $10B 30-year mortgages at 5.00%
- Liabilities: $10B deposits at SOFR + 0.50%
- Problem: Rate rise kills NIM

**Solution:**
- Enter $10B 30-year pay fixed swaps
- Pay 4.85%, receive SOFR
- Net interest margin locked in
- **Hedged**

**Use Case 2: Pension fund duration extension**

**Pension:**
- Assets: $50B (duration 6 years)
- Liabilities: $50B (duration 18 years)
- Gap: -12 years

**Solution:**
- Enter $30B 30-year receive fixed swaps
- Add 18 × (30/50) = 10.8 years duration
- New duration: 16.8 years
- **Much better matched**

**Use Case 3: Corporate converting floating to fixed**

**Corporation:**
- Issued $1B floating at SOFR + 2.50%
- CFO wants certainty for 5-year budget
- **Hedge floating exposure**

**Solution:**
- Enter $1B 5-year pay fixed swap at 4.75%
- Net cost: 4.75% + 2.50% = 7.25% fixed
- **Budget certainty achieved**

---

## When NOT to Use Swaps

### Avoid These Situations

**1. Small notional amounts:**

$$
\text{Notional} < \$10M \Rightarrow \text{Use bonds instead}
$$

**Why:**
- Minimum swap size typically $10-25M
- Documentation costs high for small sizes
- Bonds more accessible
- **Scale threshold**

**2. Short tenors (<1 year):**

- Swaps typically 2+ years
- Short end: Use futures instead (cheaper)
- **Maturity consideration**

**3. Illiquid currencies or exotics:**

- G4 currencies (USD, EUR, GBP, JPY): Excellent liquidity
- Emerging markets: Wide spreads, counterparty risk
- **Stick to liquid markets**

**4. Counterparty concerns:**

**If credit risk high:**
- Collateral requirements onerous
- Clearing costs high
- Better to use exchange-traded (futures)
- **Credit consideration**

**5. Regulatory capital constraints:**

**For banks post-crisis:**
- Swaps consume regulatory capital
- Capital charges increased
- May prefer cash bonds
- **Capital costs**

**6. Variable notional needs:**

**If notional changing:**
- Amortizing swaps available but complex
- May be simpler to use bonds
- **Complexity trade-off**

---

## Position Sizing and Risk Management

### The Golden Rule: Size by DV01 and Capital

**Position sizing:**

$$
\text{Notional} = \frac{\text{Risk Budget (dollars)}}{\text{DV01 per \$100M} \times 100}
$$

**Example:**

**Fund: $1B AUM**
**Risk budget: 2% per position = $20M**

**10-year swap DV01: $70k per $100M**

**Maximum notional:**

$$
\text{Notional} = \frac{\$20M}{\$70k} \times \$100M = \$28.6B
$$

**This is 28.6× leverage! Way too high.**

**Realistic constraint: Cap at 5× leverage**

$$
\text{Max notional} = 5 \times \$1B = \$5B
$$

**Conservative approach:**

- 2-3× leverage for hedging
- 3-5× for relative value
- >5× only for highly confident directional
- **Prudent sizing**

### Collateral Management

**Variation margin:**

**Daily MTM:**
- Swap value calculated daily
- If value moves against you: Post collateral
- If value moves for you: Receive collateral
- **Cash flow impact**

**Example:**

**$1B 10-year receive fixed swap**

**Rates rise 10 bps:**
- Value loss: $70k × 10 = -$700k
- **Must post $700k collateral**

**Rates fall 50 bps:**
- Value gain: $70k × 50 = +$3.5M
- **Receive $3.5M collateral**

**Cash management critical:**
- Need liquid funds for margin calls
- Can't assume static collateral
- **Liquidity buffer required**

### Portfolio Limits

**Institutional risk limits:**

**DV01 limit:**
- Example: $5M DV01 per portfolio
- $1B in 10-year swaps = $7M DV01
- **Exceeds limit, reduce**

**Notional limit:**
- Example: Max 10× AUM in swaps
- $1B AUM → $10B max swap notional
- **Leverage cap**

**Counterparty limit:**
- Example: Max $500M per counterparty
- Diversify across dealers
- **Credit risk management**

### Hedging Swap Positions

**Dynamic hedging:**

**If swap moves:**

**$1B 10-year receive fixed, rates fell 100 bps:**
- Swap now worth +$70M
- Duration still ~7 years
- To lock in profit: Enter $1B pay fixed
- **Offset position, lock in gains**

**Cross-hedging:**

**Swap vs futures:**
- Enter $500M 5-year pay fixed swap
- Hedge with 10-year Treasury futures
- Ratio: Duration matching
- **Partial hedge with exchange-traded**

---

## Common Mistakes Beginners Make

### Mistake #1: Ignoring Convexity

**The error:**

- Estimate P&L using duration only
- Large rate move (200 bps)
- Actual P&L differs significantly
- **Underestimation**

**Example:**

**$1B 30-year receive fixed swap**

**Rates fall 200 bps:**

**Duration-only:**
- Duration 18 × 2.00% = 36% gain
- **Expected: $360M**

**With convexity:**
- Actual gain ≈ 40%
- **Actual: $400M**

**Difference: $40M!**

**Correct approach:**

- Use full valuation models
- Don't rely on linear duration
- **Include convexity**

### Mistake #2: Wrong Tenor Selection

**The error:**

- Want to hedge 7-year debt
- Enter 10-year swap (close enough?)
- **Maturity mismatch**

**What happens:**

**After 7 years:**
- Debt matures, no more interest payments
- Swap still has 3 years remaining
- Now speculating on rates for 3 years
- **Unintended exposure**

**Correct approach:**

- Match swap tenor to hedging need exactly
- 7-year debt → 7-year swap
- **Precise matching**

### Mistake #3: Forgetting Floating Leg Resets

**The error:**

- Think "floating leg duration = zero"
- But next payment already fixed
- **Small duration exists**

**Reality:**

**3-month SOFR reset:**
- Next 3 months payment locked in
- Duration ≈ 0.25 years (until next reset)
- Not exactly zero
- **Technical precision**

**Impact:**

- Small, but matters for large notionals
- $10B position: 0.25 duration still significant
- **Be precise**

### Mistake #4: Ignoring Swap Spreads

**The error:**

- Compare swap rate directly to Treasury yield
- Forget swap spread component
- **Incomplete analysis**

**Example:**

**10-year swap: 4.60%**
**10-year Treasury: 4.20%**

"Swap is expensive vs Treasury" → Wrong!

**Correct:**

- Normal swap spread: 30-40 bps
- Current spread: 40 bps
- **Actually fair value, not expensive**

### Mistake #5: Overleveraging

**The error:**

- "Swaps have no upfront cost, I can do 20×!"
- Enter massive notional vs capital
- **Margin call disaster**

**Example:**

**$100M capital, enters $5B swaps (50×)**

**Rates move 50 bps against:**
- DV01: $35M per 100 bps (assuming 7 duration)
- Loss: $35M × 0.50 = $17.5M
- On $100M capital: -17.5%
- Multiple margin calls
- **Forced liquidation risk**

**Correct:**

- Max 5-10× leverage
- Keep cash buffer for margin
- **Prudent leverage**

### Mistake #6: No Exit Plan

**The error:**

- Enter directional swap
- "I'll know when to exit"
- Rates move against, don't exit
- **Riding losses down**

**Better:**

- Set stop-loss (e.g., 50 bps against)
- Or time-based exit (e.g., 6 months)
- **Disciplined exits**

### Mistake #7: Ignoring Counterparty Risk

**The error:**

- Enter swap with weak counterparty
- Counterparty defaults
- **Replacement cost risk**

**Example:**

**$1B receive fixed swap, rates fell 100 bps:**
- Swap worth +$70M (counterparty owes you)
- Counterparty bankrupt
- Must enter new swap at current (worse) rates
- **Loss of value**

**Correct:**

- Only trade with strong counterparties (A-rated+)
- Or use cleared swaps (central counterparty)
- **Credit risk management**

### Mistake #8: Misunderstanding Notional

**The error:**

- See "$1B notional swap"
- Think "I need $1B capital"
- **Confusion**

**Reality:**

- Notional is reference only
- Never exchanged
- Capital needed: Margin (small %)
- **Leverage instrument**

### Mistake #9: Wrong Pay/Receive Direction

**The error:**

- Want to hedge floating debt
- Accidentally enter receive fixed (opposite!)
- **Directional error**

**Check:**

- Floating debt → Enter pay fixed
- Fixed debt, want floating → Enter receive fixed
- Always verify direction
- **Critical to get right**

### Mistake #10: Ignoring Day Count**

**The error:**

- Calculate payments using wrong day count
- 30/360 vs ACT/360 vs ACT/365
- **Payment errors**

**Example:**

**Fixed leg: 30/360**
- Assumes 360-day year
- 30 days per month

**Floating leg: ACT/360**
- Actual days
- 360-day year

**Different conventions → Different amounts**

**Must use correct convention for each leg!**

---

## Best Case Scenario

### The Perfect Post-Crisis Trade (2009-2013)

**Trader profile:**

- Experience: 20 years rates trading
- Fund: $2B macro hedge fund
- Strategy: Long-term receive fixed
- Discipline: Excellent

**Setup (March 2009):**

**Market conditions:**

- Financial crisis peak
- Fed at 0-0.25%
- 10-year swap: 2.50%
- Outlook: Fed on hold for years (QE era)
- **Multi-year opportunity**

**Position:**

**Phased entry (March-June 2009):**
- $10B 10-year receive fixed swaps
- Average entry: 2.75%
- Notional: 5× fund size
- Duration: 7 years
- **Long-term positioning**

**Thesis:**

- Fed committed to zero rates (5+ years)
- QE will drive long rates lower
- Deflation risk (demand term premium)
- Flight to quality ongoing
- **Structural bull market in rates**

**Trade progression:**

**2009-2010:**
- QE1 announced ($1.75T)
- 10-year swap: 2.75% → 2.00%
- Unrealized gain: 7 × 0.75% × $10B = $525M
- **Strong start**

**2011:**
- European crisis, flight to quality
- 10-year swap: 2.00% → 1.50%
- Additional gain: $350M
- **Cumulative: $875M**

**2012:**
- QE3 announced (unlimited)
- 10-year swap: 1.50% → 1.30%
- Additional gain: $140M
- **Cumulative: $1.015B**

**Exit strategy (May 2013):**

**"Taper Tantrum" signal:**
- Fed hints at QE taper
- Rates starting to rise
- Time to exit

**Closed positions:**
- 10-year swap: 1.30% → 1.60% (rising)
- Booked profit before full reversal
- Final gain: ~$950M (gave back $65M)
- **Disciplined exit**

**4-year total:**

$$
\text{Profit} = \$950M
$$

$$
\text{Return on capital} = \frac{\$950M}{\$2B} = 47.5\%
$$

**Annualized: 10.2%**

**Why this worked perfectly:**

1. ✅ Correct structural view (Fed on hold for years)
2. ✅ Patient positioning (entered over 3 months)
3. ✅ Multi-year holding period (harvested full cycle)
4. ✅ QE amplified trade (Fed buying $85B/month at peak)
5. ✅ Disciplined exit (recognized taper tantrum signal)
6. ✅ Reasonable leverage (5×, not excessive)
7. ✅ Perfect macro environment
8. **Institutional-quality execution**

---

## Worst Case Scenario

### The Taper Tantrum Disaster (2013)

**Trader profile:**

- Experience: 8 years
- Fund: $500M fixed income fund
- Strategy: Receive fixed (wrong timing)
- Discipline: Poor

**Setup (April 2013):**

**Position:**

- $8B 30-year receive fixed swaps
- Entry rate: 3.00%
- Leverage: 16× (!)
- Duration: 18 years
- **Maximum leverage, maximum duration**

**Thesis:**

- "Rates can only go lower"
- "Fed will never taper"
- Complacency
- **Wrong**

**The disaster (May-September 2013):**

**May 22: Bernanke "Taper" testimony**

- Hints at reducing QE purchases
- Market panic

**Rate explosion:**

- 30-year swap: 3.00% → 4.00% in 3 months
- +100 bps move
- Fastest rise since 2009
- **Violent reversal**

**P&L catastrophe:**

**Daily MTM:**

**Week 1:**
- Rates +20 bps
- Loss: 18 × 0.20% × $8B = -$288M
- Margin call: $288M (fund only has $500M!)
- **Severe stress**

**Week 2-4:**
- Rates +40 bps more
- Additional loss: $576M
- Total: -$864M
- **Exceeded fund capital**

**Forced liquidation:**

- Clearinghouse demanded full collateral
- Fund couldn't meet
- Forced to close swaps at worst levels
- **Crystallized losses**

**Final outcome:**

- Started: $500M
- Ended: $50M (after liquidation)
- **-90% loss in 3 months**

**Aftermath:**

- Fund shut down
- Investors lost nearly everything
- Careers destroyed
- **Total disaster**

**What went catastrophically wrong:**

1. ❌ Extreme leverage (16×)
2. ❌ Maximum duration (30-year = highest risk)
3. ❌ Complacency ("rates can't rise")
4. ❌ Ignored warning signs (Bernanke testimony)
5. ❌ No stop-loss
6. ❌ No contingency planning
7. ❌ Insufficient capital for margin calls
8. ❌ Wrong side of massive unwind
9. **Complete risk management failure**

---

## What to Remember

### Core Concept

**Swap = Exchange of cash flows:**

$$
\text{Pay Fixed} + \text{Receive Floating} \quad \text{(or vice versa)}
$$

- No principal exchange
- Mark-to-market daily
- Most efficient duration tool
- **Fundamental derivative**

### Valuation Framework

$$
V_{\text{swap}} = PV_{\text{fixed leg}} - PV_{\text{floating leg}}
$$

- Initial value: Zero (at-market)
- Value changes with rates
- DV01 critical metric
- **Risk measurement**

### Replication

**Pay fixed swap = Short bond + Long FRN**

- Same economic exposure
- But swaps more efficient
- No funding needed
- **Capital efficiency**

### Key Applications

**Hedging:**
- Asset-liability mismatch
- Convert floating to fixed (or reverse)
- Duration management
- **Primary use**

**Speculation:**
- Directional rate views
- Curve positioning
- Leverage without capital
- **Secondary use**

### Risk Metrics

**DV01:**
- Pay fixed: Positive DV01 (gains when rates rise)
- Receive fixed: Negative DV01 (gains when rates fall)
- **Primary risk measure**

**Duration:**
- Typical: 2-18 years (by tenor)
- 10-year swap ≈ 7 years duration
- **Rate sensitivity**

### Optimal Conditions

**For hedgers:**
- Always hedge when risk arises
- Don't time the market
- **Immediate execution**

**For speculators:**
- Strong directional view (Fed policy shift)
- Clear catalysts (data, events)
- Risk-managed leverage (3-5×)
- **Disciplined positioning**

### Common Mistakes

1. Ignoring convexity (large moves)
2. Wrong tenor (maturity mismatch)
3. Forgetting floating leg duration
4. Ignoring swap spreads
5. Overleveraging (>10× dangerous)
6. No exit plan
7. Counterparty risk
8. Misunderstanding notional
9. Wrong direction (pay vs receive)
10. Day count errors

### Historical Performance

**Best environment (2009-2013):**
- Receive fixed swaps: +40-50% (4 years)
- Structural bull market in rates
- **QE era**

**Worst environment (2013 Taper, 2022 Hiking):**
- Receive fixed swaps: -40% to -90%
- Violent rate reversals
- **Leverage amplified losses**

### Success Factors

**Three pillars:**

1. **Correct View** (macro, Fed policy)
2. **Appropriate Leverage** (3-5× max for most)
3. **Risk Management** (stops, exits, collateral)

**Formula:**

$$
\text{Success} = \text{Right Direction} \times \text{Prudent Size} \times \text{Discipline}
$$

### Final Wisdom

> "Interest rate swaps are the workhorse of fixed income markets—$400 trillion notional outstanding, more liquid than bonds, more capital-efficient than repo, and essential for every major institution's interest rate risk management. A simple pay fixed swap on $100M notional provides $700k DV01 (10-year) with minimal upfront capital, equivalent to shorting $100M in bonds but without the financing cost or balance sheet impact. This makes swaps the natural choice for hedging (banks converting floating liabilities to fixed), duration management (pension funds extending duration via receive fixed swaps to match liabilities), and directional positioning (hedge funds expressing rate views with 5-10× leverage). But the same leverage that enables capital efficiency creates catastrophic risk when wrong: the 2013 Taper Tantrum destroyed leveraged receive-fixed positions (-90% for some funds), while 2022 saw similar devastation as rates rose 250 bps in nine months. Success requires matching swap tenor to hedging horizon exactly (7-year debt → 7-year swap), sizing by DV01 to capital (never exceed 5-10× leverage), maintaining liquid collateral for margin calls (rates can move 50 bps in days), and ruthless discipline on stop-losses (wrong view = exit immediately). Swaps are simultaneously the most efficient tool for rate risk management and the fastest path to blowup when overleveraged. Use for hedging first, speculation second, and always respect the leverage. 📊🔄"

**Most important principles:**

- Swap = exchange cash flows (no principal)
- Pay fixed = short duration (gains when rates rise)
- Receive fixed = long duration (gains when rates fall)
- DV01 critical for sizing (dollars per bp move)
- Leverage inherent (large notional, small capital)
- Match tenor to hedging need (exact maturity)
- Collateral management crucial (daily MTM)
- Maximum leverage 5-10× for most applications

**Why swaps dominate:**

- Capital efficiency (no principal exchange)
- Superior liquidity (tighter than bonds)
- Flexibility (customize terms)
- Off-balance-sheet treatment
- **Institutional preference**

**But remember:**

- 2013 Taper Tantrum (-90% for overleveraged)
- 2022 rate surge (-40% typical receive fixed)
- Leverage amplifies both ways
- Margin calls can force liquidation
- Counterparty risk exists
- **Risk management essential**

**Use swaps as duration tool, hedge when needed, speculate with discipline, never over-leverage. The most important derivative in finance—use it wisely. 🔀💼**
