# Credit Curve Trading


**Credit curve trading** involves exploiting mispricings in the term structure of credit spreads—the relationship between spreads at different maturities for the same issuer—through strategies such as curve steepeners, flatteners, and butterfly trades that profit from changes in curve shape rather than directional spread movements, requiring precise analysis of term structure dynamics, roll-down economics, and relative value across the maturity spectrum.

---

## The Core Insight


**The fundamental idea:**

- Credit spreads vary by maturity (the credit curve)
- Curves can steepen (long end widens vs short) or flatten (long tightens vs short)
- Curve shape changes create profit opportunities
- Trade: Long one maturity, short another (duration-neutral)
- Isolate curve slope bet from directional credit view
- Roll-down provides income even without spread changes
- Butterfly trades exploit kinks in curve
- Most active: 2s5s, 5s10s spread trades

**The key equations:**

**Curve spread (steepness):**

$$
\text{Curve Spread}_{2s10s} = S_{10y} - S_{2y}
$$

**Curve trade P&L:**

$$
\text{P\&L} = \text{Notional}_{10y} \times \Delta S_{10y} - \text{Notional}_{2y} \times \Delta S_{2y}
$$

**Duration-neutral hedge ratio:**

$$
\frac{\text{Notional}_{2y}}{\text{Notional}_{10y}} = \frac{D_{10y}}{D_{2y}}
$$

**Butterfly P&L (2s5s10s):**

$$
\text{P\&L} = w_2 \times \Delta S_2 - w_5 \times \Delta S_5 + w_{10} \times \Delta S_{10}
$$

**You're essentially trading: "I think the credit curve will flatten (10-year spreads will tighten relative to 2-year), so I'll buy 10-year protection and sell 2-year protection in a duration-neutral structure, profiting when the curve shape changes regardless of whether overall spreads widen or tighten."**

---

## What Is Credit Curve Trading?


**Before implementing curve trades, understand the mechanics:**

### 1. The Credit Spread Term Structure


**Why credit curves slope upward (normally):**

1. **Cumulative Default Risk:**
   - Longer holding period = more time for default
   - 10-year default probability > 2-year
   - Investors demand compensation

2. **Uncertainty Premium:**
   - Future fundamentals more uncertain
   - Business risk compounds over time
   - Higher premium for distant cash flows

3. **Liquidity Preference:**
   - Short-dated more liquid
   - Easier to exit
   - Lower liquidity premium at front end

**Typical credit curve shapes:**

| Issuer Quality | 2Y Spread | 5Y Spread | 10Y Spread | 2s10s Slope |
|----------------|-----------|-----------|------------|-------------|
| AAA | 15 bp | 25 bp | 40 bp | +25 bp |
| A | 40 bp | 65 bp | 95 bp | +55 bp |
| BBB | 80 bp | 120 bp | 160 bp | +80 bp |
| BB | 200 bp | 280 bp | 350 bp | +150 bp |
| B | 400 bp | 500 bp | 580 bp | +180 bp |

**Key insight:** Lower-rated issuers have steeper curves (more term premium for uncertainty).

### 2. Types of Curve Trades


**1. Curve Steepener:**

**Position:** Long short-end (sell protection), Short long-end (buy protection)

**Profit when:** 2s10s widens (curve steepens)

**Example:**
- Sell $10M 2-year CDS protection @ 80 bp
- Buy $4M 10-year CDS protection @ 160 bp
- (Duration-neutral: $10M × 1.9 ≈ $4M × 4.8)

**Scenario:** Curve steepens 2s10s from 80 bp to 120 bp
- 2Y unchanged at 80 bp → No P&L
- 10Y widens to 200 bp → Gain $4M × 4.8 × 0.40% = $76,800

**When to trade:** Late cycle (credit concerns rise at long end first), credit deterioration

**2. Curve Flattener:**

**Position:** Short short-end (buy protection), Long long-end (sell protection)

**Profit when:** 2s10s narrows (curve flattens)

**Example:**
- Buy $10M 2-year CDS protection @ 80 bp
- Sell $4M 10-year CDS protection @ 160 bp

**Scenario:** Curve flattens 2s10s from 80 bp to 40 bp
- 2Y widens to 100 bp → Gain $10M × 1.9 × 0.20% = $38,000
- 10Y unchanged → No P&L on long end

**When to trade:** Credit improvement, upgrades expected, economic recovery

**3. Butterfly (2s5s10s):**

**Position:** Long wings (2Y and 10Y), Short body (5Y)

**Profit when:** 5Y richens vs. wings (belly richening)

$$
\text{Butterfly} = S_{5y} - \frac{S_{2y} + S_{10y}}{2}
$$

**Example:**
- 2Y: 80 bp
- 5Y: 120 bp
- 10Y: 160 bp
- Butterfly: 120 - (80 + 160)/2 = 0 bp (fair value)

If 5Y widens to 130 bp (butterfly to +10 bp):
- Short 5Y protection profits
- Long wings unchanged

**When to trade:** 5Y CDS often most liquid, can be mispriced relative to curve

### 3. Duration-Neutral Hedge Ratios


**Precise calculation for curve trades:**

**Step 1: Calculate DV01 for each leg**

$$
\text{DV01}_i = \text{Notional}_i \times D_i \times 0.0001
$$

**Step 2: Set equal DV01s**

$$
\text{DV01}_{short} = \text{DV01}_{long}
$$

**Step 3: Solve for hedge ratio**

$$
\frac{\text{Notional}_{2y}}{\text{Notional}_{10y}} = \frac{D_{10y}}{D_{2y}}
$$

**Example:**
- 2Y CDS duration: 1.9 years
- 10Y CDS duration: 4.8 years
- Hedge ratio: 4.8 / 1.9 = 2.53

For $10M 10Y position:
- Need $25.3M 2Y position (duration-neutral)

**Reality check:** Not perfectly neutral (convexity differs), but close enough for most trades.

---

## Economic Interpretation: Curve Dynamics


**Understanding what drives curve shape changes:**

### 1. Credit Cycle and Curve Shape


**Early Cycle (Post-Crisis Recovery):**
- Curves steep: Long end reflects lingering concerns
- Front end tights: Immediate default unlikely
- Trade: Flattener (long end will catch up)

**Mid Cycle (Expansion):**
- Curves moderate: Balanced term structure
- Roll-down optimal: Steep enough to harvest
- Trade: Carry strategies dominate

**Late Cycle (Pre-Recession):**
- Curves can invert for distressed names
- Long end may tighten (already pricing default)
- Short end widens (imminent distress)
- Trade: Steepener on quality names

**Recession:**
- Massive curve inversion for distressed
- Flight to quality at short end
- Trade: Exit curve positions (too volatile)

### 2. Single-Name vs. Index Curve Trades


**Single-Name Curves:**
- More volatile
- Idiosyncratic factors dominate
- Higher return potential
- Lower liquidity
- Example: Trade XYZ Corp 2s10s

**Index Curves (CDX, iTraxx):**
- More liquid
- Systematic factors
- Lower bid-ask
- Easier to trade
- Example: Trade CDX IG 3s7s

**Hybrid:**
- Long single-name short end
- Hedge with index long end
- Capture idiosyncratic curve vs. market

### 3. Curve Trade Risks


**1. Parallel Shift Risk:**
- If not perfectly duration-neutral
- Residual directional exposure
- Monitor DV01 mismatch

**2. Convexity Risk:**
- Long and short ends have different convexity
- Large parallel moves create P&L
- Typically small for normal moves

**3. Default Risk:**
- Single-name can default
- Both legs affected
- Net exposure depends on timing

**4. Liquidity Risk:**
- Long end often less liquid
- Bid-ask wider
- May not be able to unwind

**5. Roll Risk:**
- CDS contracts roll (new series)
- Roll spread can move against
- Time trades around roll dates

---

## Practical Implementation


### 1. Trade Construction Example


**Trade: BBB Industrial 2s5s Flattener**

**Setup (January 2025):**

| Leg | Maturity | Spread | Duration | Action | Notional |
|-----|----------|--------|----------|--------|----------|
| Short | 2Y | 75 bp | 1.9y | Buy Protection | $26.3M |
| Long | 5Y | 120 bp | 4.5y | Sell Protection | $11.1M |

**Duration-neutral check:**
- 2Y DV01: $26.3M × 1.9 × 0.0001 = $5,000
- 5Y DV01: $11.1M × 4.5 × 0.0001 = $5,000 ✓

**Curve spread at entry:** 120 - 75 = 45 bp

**Entry rationale:**
- Historical 2s5s average: 35 bp
- Current 45 bp = 1.5 std dev steep
- Expectation: Curve flattens to 35 bp

**Cash Flows (Quarterly):**

- Receive from 5Y: $11.1M × 1.20% / 4 = $33,300
- Pay for 2Y: $26.3M × 0.75% / 4 = $49,400
- **Net quarterly carry: -$16,100** (negative carry!)

**This illustrates a key point: Curve flatteners often have negative carry.**

**Exit Scenarios (6 months later):**

**Scenario 1: Curve flattens to 35 bp**
- 2Y widens to 85 bp (+10 bp)
- 5Y unchanged at 120 bp
- 2Y P&L: +$26.3M × 1.9 × 0.10% = +$50,000
- 5Y P&L: $0
- Carry: -$32,200
- **Net: +$17,800**

**Scenario 2: Curve steepens to 55 bp**
- 2Y unchanged at 75 bp
- 5Y widens to 130 bp (+10 bp)
- 2Y P&L: $0
- 5Y P&L: -$11.1M × 4.5 × 0.10% = -$50,000
- Carry: -$32,200
- **Net: -$82,200**

**Scenario 3: Parallel shift (both widen 20 bp)**
- 2Y P&L: +$26.3M × 1.9 × 0.20% = +$100,000
- 5Y P&L: -$11.1M × 4.5 × 0.20% = -$100,000
- Carry: -$32,200
- **Net: -$32,200** (carry only, duration-neutral)

### 2. Entry Checklist


**For curve steepeners:**

1. **Curve percentile:**
   - [ ] 2s5s or 2s10s at <25th percentile (flat)
   - [ ] Historical data shows mean reversion

2. **Credit cycle:**
   - [ ] Late cycle or deterioration expected
   - [ ] Long-end vulnerable to risk-off

3. **Single-name factors:**
   - [ ] No imminent default risk
   - [ ] Stable fundamentals (curve, not direction bet)

4. **Technical:**
   - [ ] Liquid maturities available
   - [ ] Bid-ask reasonable (<5 bp each leg)
   - [ ] No roll issues

**For curve flatteners:**

1. **Curve percentile:**
   - [ ] 2s5s or 2s10s at >75th percentile (steep)
   - [ ] Carry typically negative (factor in)

2. **Credit cycle:**
   - [ ] Early cycle or recovery phase
   - [ ] Long-end should tighten

3. **Fundamental catalyst:**
   - [ ] Upgrade potential
   - [ ] Deleveraging story
   - [ ] Sector tailwinds

### 3. Risk Limits


**Position sizing:**

$$
\text{Max Notional} = \frac{\text{Max Curve Risk}}{\text{Expected Curve Volatility} \times \text{DV01}}
$$

**Example:**
- Max curve risk: $100,000
- Expected 2s10s vol: 20 bp / month
- DV01 per leg: $5,000

$$
\text{Max Notional} = \frac{100,000}{20 \times 5,000 / 10,000} = $100M \text{ per leg}
$$

**Stop-loss rules:**

- Curve moves 1.5x against position: Exit 50%
- Curve moves 2x against: Exit remaining
- Example: 2s5s trade entry at 45 bp
  - Stop at 55 bp (partial): Curve steepened 10 bp
  - Stop at 60 bp (full): Curve steepened 15 bp

---

## Case Study: The 2008 Credit Curve Inversion


**Background:**

In 2007-2008, many BBB financial credits saw dramatic curve inversions as near-term default risk spiked.

**Lehman Brothers CDS Curve (March 2008):**

| Maturity | Spread (Mar 08) | Spread (Jun 08) | Spread (Sep 12) |
|----------|-----------------|-----------------|-----------------|
| 1Y | 180 bp | 320 bp | 650 bp |
| 3Y | 170 bp | 300 bp | 580 bp |
| 5Y | 160 bp | 280 bp | 520 bp |
| 10Y | 150 bp | 250 bp | 450 bp |

**2s10s slope:** -30 bp (inverted March), -70 bp (Jun), -200 bp (Sep)

**Curve trade disaster:**

**Trader thesis (March 2008):** "Lehman curve inverted, buy flattener (bet on normalization)"

**Position:**
- Buy 2Y protection @ 180 bp ($50M)
- Sell 10Y protection @ 150 bp ($20M)

**What happened:**

The curve inverted further as Lehman approached bankruptcy. The 2Y spread rose much faster than 10Y (near-term survival uncertain, long-term already pricing default).

**September 2008 P&L:**
- 2Y: +$50M × 1.9 × (650 - 180) = +$4.47M gain
- 10Y: -$20M × 4.8 × (450 - 150) = -$2.88M loss
- **Net: +$1.59M (flattener actually worked!)**

**But wait...**

On September 15, Lehman defaulted:
- Both legs triggered credit event
- Recovery: ~8 cents
- 2Y protection payment: $50M × 92% = $46M received
- 10Y protection payment: $20M × 92% = $18.4M paid
- **Net from default: +$27.6M**

**The lesson:** Curve trades on single names can become directional default bets. The "flattener" became a net long protection position when default occurred.

**Rules derived:**
1. Don't trade curves on distressed names
2. Understand net exposure at default
3. Curve normalization requires survival
4. Index curves safer for pure curve bets

---

## What to Remember


### 1. Core Concept


**Credit curve trading isolates term structure bets from directional credit views:**

$$
\text{Curve P&L} = \Delta(\text{Long Spread} - \text{Short Spread}) \times \text{Duration}
$$

- Steepener: Long short-end, short long-end
- Flattener: Short short-end, long long-end
- Duration-neutral: Equal DV01 on each leg
- Profit from curve shape changes, not parallel shifts

### 2. Key Metrics


**Curve trade characteristics:**

| Trade | Carry | Direction | Best Cycle |
|-------|-------|-----------|------------|
| Steepener | Positive (usually) | Long-end widens | Late cycle |
| Flattener | Negative (usually) | Long-end tightens | Early cycle |
| Butterfly | Neutral | Belly vs. wings | Mispricing |

**Typical ranges:**

- IG 2s10s: 30-80 bp (historical)
- HY 2s10s: 80-200 bp
- 1 std dev move: 15-25 bp

### 3. Risk Management


**Essential rules:**

- Duration-neutral: Match DV01 within 5%
- Quality credits only: Avoid distressed (curve inverts before default)
- Size by curve vol: Use historical curve std dev
- Stop-loss: 1.5-2x expected move
- Avoid roll periods: CDS rolls can create basis
- Monitor net default exposure: Know P&L if default occurs
- Limit single-name: Use index for pure curve bets

### 4. Common Mistakes


1. **Not duration-neutral:** Creates directional bet
2. **Trading distressed curves:** Inversion means default risk, not opportunity
3. **Ignoring carry:** Flatteners have negative carry, factor in
4. **Wrong cycle:** Steepeners in early cycle = wrong direction
5. **Illiquid maturities:** Long-end often has wide bid-ask
6. **Single-name default risk:** One name defaulting can dominate P&L

### 5. Final Wisdom


> "Credit curve trading is intellectually elegant—isolating term structure views from directional credit risk. But the devil is in the execution. Duration-neutral doesn't mean risk-free. Curves can steepen or flatten much more than historical norms during regime changes. The 2008 curve inversions taught painful lessons: distressed curves don't 'normalize' to flat—they invert further and then the company defaults. Trade curves on quality credits (BBB+ and above), use indices for pure curve bets, and always know your net exposure if the worst happens. When a flattener becomes a 'the company is going to survive' bet, you've lost the curve trade and gained a directional credit position. Exit immediately."

**Keys to success:**

1. **Quality credits only:** Curves normalize; distressed defaults
2. **Duration-neutral:** Match DV01 precisely
3. **Factor in carry:** Flatteners cost money to hold
4. **Historical context:** Know percentile of current slope
5. **Cycle awareness:** Steepeners late cycle, flatteners early
6. **Index for pure curve:** Single-names have default overlay
7. **Stop-losses:** Curve can move 2-3x normal
8. **Exit distressed:** If credit deteriorates, close curve trade

**Most critical rule:**

$$
\text{Curve Trade} \neq \text{Default Bet}
$$

If your curve trade requires the company to survive for it to work, you're not trading the curve—you're trading survival. Know the difference. Curve trades should work whether the company improves, stays the same, or deteriorates modestly. If default is a realistic scenario, you're in the wrong trade. 🎯📊
