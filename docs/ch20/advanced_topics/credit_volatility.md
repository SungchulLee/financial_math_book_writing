# Credit Volatility


**Credit volatility trading** involves strategies that profit from changes in the implied or realized volatility of credit spreads, rather than from directional spread movements, using instruments such as CDS options (swaptions), index tranche positions, and spread straddles that gain value when credit markets become more volatile regardless of whether spreads widen or tighten.

---

## The Core Insight


**The fundamental idea:**

- Credit spreads have volatility just like equity prices
- Implied vol priced into credit options and tranches
- Realized vol = actual spread movements
- When implied < realized: Buy vol (options cheap)
- When implied > realized: Sell vol (collect premium)
- Vol spikes during crises (VIX of credit)
- Vol trades can be directionally neutral
- Key instruments: CDS swaptions, index tranches, spread options

**The key equations:**

**Spread volatility:**

$$
\sigma_s = \text{Std}(\Delta S) \times \sqrt{252} \quad \text{(annualized)}
$$

**Option premium approximation:**

$$
\text{CDS Swaption Premium} \approx 0.4 \times \sigma_s \times \sqrt{T} \times \text{Notional} \times \text{Duration}
$$

**Gamma P&L from spread moves:**

$$
\text{Gamma P\&L} = \frac{1}{2} \times \Gamma \times (\Delta S)^2
$$

**Vol arbitrage:**

$$
\text{P\&L} = \frac{1}{2} \times \text{Vega} \times (\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2)
$$

**You're essentially trading: "I think credit spread volatility is too low (or too high) relative to what will actually happen. I'll structure a position that profits from vol increasing (decreasing) regardless of whether spreads widen or tighten directionally."**

---

## What Is Credit Volatility?


**Before trading credit vol, understand the instruments:**

### 1. Credit Spread Volatility Defined


**Spread volatility measures:**

$$
\sigma_{\text{spread}} = \text{Annualized standard deviation of daily spread changes}
$$

**Typical levels (5-year IG):**

| Market Regime | Daily Vol (bp) | Annualized Vol (bp) | Vol Index Equiv |
|---------------|----------------|---------------------|-----------------|
| Low vol | 1-2 bp | 15-30 bp | VIX ~12 |
| Normal | 3-4 bp | 45-65 bp | VIX ~18 |
| Elevated | 5-8 bp | 80-125 bp | VIX ~25 |
| Crisis | 15-30 bp | 240-480 bp | VIX ~40+ |

**Historical perspective:**

- 2006-2007 (pre-crisis): 25-40 bp annual
- 2008-2009 (crisis): 400-600 bp annual
- 2010-2019 (QE era): 30-60 bp annual
- 2020 (COVID): 300+ bp spike
- 2021-2024: 35-55 bp annual

**Key insight:** Credit vol is regime-dependent and mean-reverting.

### 2. Credit Vol Instruments


**1. CDS Swaptions (Payer and Receiver):**

**Definition:** Option to enter into a CDS contract at a specified spread.

**Payer swaption:**
- Right to BUY protection at strike spread
- Profits if spreads widen above strike
- Long credit risk (vol buyer)

**Receiver swaption:**
- Right to SELL protection at strike spread
- Profits if spreads tighten below strike
- Short credit risk (vol buyer)

**Example: 3M × 5Y CDX IG Payer Swaption**

- Underlying: CDX.NA.IG 5-year
- Option expiry: 3 months
- Strike: 65 bp (ATM)
- Premium: 0.30% of notional
- If CDX at 90 bp at expiry: Exercise, buy protection at 65 bp
- Intrinsic value: (90 - 65) × 4.5 = 112.5 bp = 1.125% of notional

**2. CDS Straddles:**

**Position:** Payer + Receiver at same strike

**Profit when:** Spreads move significantly in either direction

**Example:**
- Buy 3M payer @ 65 bp strike (cost 0.30%)
- Buy 3M receiver @ 65 bp strike (cost 0.25%)
- Total premium: 0.55%
- Breakeven: Spread must move ±0.55% / 4.5 ≈ ±12 bp

**If spreads widen to 85 bp:**
- Payer: +20 bp × 4.5 = 0.90% gain
- Receiver: Expires worthless
- Net: +0.90% - 0.55% = **+0.35%**

**If spreads tighten to 50 bp:**
- Payer: Expires worthless
- Receiver: +15 bp × 4.5 = 0.675% gain
- Net: +0.675% - 0.55% = **+0.125%**

**3. Index Tranches:**

**Definition:** Slices of credit index loss distribution

**Tranche structure (CDX IG):**

| Tranche | Attachment | Detachment | Leverage | Vol Exposure |
|---------|------------|------------|----------|--------------|
| Equity | 0% | 3% | 15-20x | Very high |
| Mezzanine | 3% | 7% | 5-8x | High |
| Senior | 7% | 15% | 2-3x | Moderate |
| Super Senior | 15% | 30% | <1x | Low |

**Equity tranche (0-3%):**
- First loss position
- Highly leveraged to spread moves
- Long correlation (benefits if defaults cluster)
- High gamma (non-linear response)

**Mezzanine tranche (3-7%):**
- Second loss
- Still leveraged
- Correlation exposure
- Popular for vol trades

**4. Spread Options on Indices:**

**Similar to equity options but on spread level:**

- Call on spread (payer-like): Profits if spread rises
- Put on spread (receiver-like): Profits if spread falls
- Available on CDX, iTraxx indices
- OTC market (dealer quotes)

### 3. Implied vs. Realized Volatility


**The core vol trade:**

$$
\text{Vol P\&L} \approx \text{Vega} \times (\sigma_{\text{realized}} - \sigma_{\text{implied}})
$$

**Implied volatility:**
- Priced into options/swaptions
- Market expectation of future vol
- Derived from option premiums
- Forward-looking

**Realized volatility:**
- Actual spread movements
- Historical measurement
- Backward-looking

**Vol premium:**

$$
\text{Vol Premium} = \sigma_{\text{implied}} - \sigma_{\text{realized}}
$$

**Historical average: Implied > Realized by 15-25%**

This is the "volatility risk premium" that sellers earn.

---

## Economic Interpretation: Why Credit Vol Matters


### 1. Vol as Fear Gauge


**Credit vol spikes indicate:**

1. **Uncertainty about defaults:**
   - Will this company survive?
   - What's the recovery rate?

2. **Liquidity concerns:**
   - Can I sell bonds?
   - What's the bid-ask?

3. **Systemic risk:**
   - Is this idiosyncratic or contagion?
   - Will other names follow?

4. **Economic uncertainty:**
   - Recession probability
   - Central bank response

**Vol spikes precede spread widening:**

Research shows vol typically rises 2-4 weeks before major spread moves.

### 2. Correlation and Vol Interaction


**In credit markets, correlation matters:**

**Low correlation environment:**
- Defaults are independent
- Diversification works
- Senior tranches safe
- Vol moderate

**High correlation environment:**
- Defaults cluster
- Diversification fails
- Senior tranches at risk
- Vol spikes

**The correlation trade:**

$$
\text{Equity Tranche Value} \propto \frac{1}{\rho}
$$

$$
\text{Senior Tranche Value} \propto \rho
$$

Where $\rho$ = default correlation.

**Long correlation:** Long equity tranche, short mezzanine
**Short correlation:** Long mezzanine, short equity

### 3. Volatility Smile in Credit


**Like equity options, credit options have a smile:**

**Typical credit vol smile:**

| Strike (vs ATM) | Implied Vol |
|-----------------|-------------|
| 80% (OTM Put/Receiver) | +10-15% |
| 90% | +5% |
| 100% (ATM) | Baseline |
| 110% | +5% |
| 120% (OTM Call/Payer) | +15-25% |

**Payer skew is steeper** because:
- Spread widening is more violent
- Fat left tail in credit
- Default = discontinuous jump
- Protection buyers pay premium

**Arbitrage between strikes:**
- Risk reversals (long OTM payer, short OTM receiver)
- Butterflies across strikes
- Calendar spreads

---

## Practical Implementation


### 1. Long Vol Strategy


**When to be long credit vol:**

1. **Vol at historical lows:**
   - Implied vol < 30th percentile
   - Vol premium negative or zero

2. **Event risk approaching:**
   - FOMC meetings
   - Earnings season
   - Geopolitical tensions

3. **Complacency indicators:**
   - Tight spreads
   - Low VIX
   - Risk-on sentiment

**Implementation: Straddle on CDX IG**

**Trade setup (January 2025):**

| Parameter | Value |
|-----------|-------|
| Underlying | CDX.NA.IG.43 5Y |
| Current spread | 55 bp |
| 3M ATM implied vol | 45 bp |
| Historical realized vol | 52 bp |
| Observation | Implied < Realized (vol cheap) |

**Position:**
- Buy 3M Payer @ 55 bp strike, premium 0.28%
- Buy 3M Receiver @ 55 bp strike, premium 0.22%
- Total premium: 0.50% on $100M = $500,000
- Notional: $100M

**Greeks:**
- Delta: ~0 (straddle balanced at ATM)
- Gamma: +$4,200 per bp² move
- Vega: +$8,500 per 1 bp vol increase
- Theta: -$5,500 per day

**Scenario Analysis (at expiry):**

| Spread at Expiry | Payer Value | Receiver Value | Total | P&L |
|------------------|-------------|----------------|-------|-----|
| 40 bp | $0 | $67,500 | $67,500 | -$432,500 |
| 50 bp | $0 | $22,500 | $22,500 | -$477,500 |
| 55 bp | $0 | $0 | $0 | -$500,000 |
| 60 bp | $22,500 | $0 | $22,500 | -$477,500 |
| 70 bp | $67,500 | $0 | $67,500 | -$432,500 |
| 85 bp | $135,000 | $0 | $135,000 | -$365,000 |
| 100 bp | $202,500 | $0 | $202,500 | -$297,500 |
| 120 bp | $292,500 | $0 | $292,500 | -$207,500 |
| 150 bp | $427,500 | $0 | $427,500 | -$72,500 |
| 180 bp | $562,500 | $0 | $562,500 | +$62,500 |

**Breakeven:** Spread must move approximately ±28 bp from 55 bp.

**Key insight:** You need a 50%+ spread move to break even. That's why long vol is expensive.

### 2. Short Vol Strategy


**When to be short credit vol:**

1. **Vol at historical highs:**
   - Implied vol > 70th percentile
   - Post-crisis spike normalizing

2. **No near-term catalysts:**
   - Quiet calendar
   - Earnings done
   - Fed on hold

3. **Risk premium analysis:**
   - Implied >> Realized
   - Sell premium, collect theta

**Implementation: Sell Straddle on CDX IG**

**WARNING:** Selling vol has unlimited downside. Size very conservatively.

**Trade setup:**

- Sell 3M Payer @ 55 bp, receive 0.28%
- Sell 3M Receiver @ 55 bp, receive 0.22%
- Total premium: 0.50% on $50M = $250,000
- Max profit: $250,000 (if spread = 55 at expiry)
- Max loss: Unlimited

**Greeks:**
- Delta: ~0 (balanced)
- Gamma: -$2,100 per bp² (negative gamma!)
- Theta: +$2,750 per day

**Risk management for short vol:**

1. **Position limits:** Max 1-2% of capital at risk
2. **Dynamic hedging:** Delta hedge as spread moves
3. **Stop-loss:** Exit if spread moves 20 bp
4. **Vol spike stops:** Exit if implied vol rises 20%

### 3. Tranche Vol Trades


**Equity tranche as vol instrument:**

The 0-3% equity tranche has embedded gamma and vega.

**Long equity tranche position:**

$$
\text{Tranche Return} \approx \text{Carry} + \text{Spread Beta} \times \Delta S + \frac{1}{2} \times \text{Gamma} \times (\Delta S)^2 + \text{Correlation} \times \Delta \rho
$$

**The "vol" comes from gamma:**
- Equity tranche gains convexity as spreads widen
- Protection value accelerates
- Like being long options

**Mezzanine short vol:**
- Mezzanine tranches have negative gamma at extremes
- Selling mezzanine is similar to selling vol
- Collect carry until crisis

**Correlation vs. Spread Trade:**

| Position | Spread View | Correlation View | Vol View |
|----------|-------------|------------------|----------|
| Long Equity | Bearish | Long | Long |
| Short Equity | Bullish | Short | Short |
| Long Mezz | Bearish | Short | Short |
| Short Mezz | Bullish | Long | Long |

---

## Case Study: March 2020 Vol Spike


**Background:**

In March 2020, COVID-19 triggered the fastest vol spike in credit history.

**Vol evolution:**

| Date | CDX IG Spread | Implied Vol | Realized Vol (20d) |
|------|---------------|-------------|-------------------|
| Feb 19 | 48 bp | 35 bp | 28 bp |
| Feb 28 | 68 bp | 52 bp | 45 bp |
| Mar 9 | 95 bp | 85 bp | 90 bp |
| Mar 18 | 152 bp | 180 bp | 200 bp |
| Mar 23 | 160 bp | 200 bp | 280 bp |
| Apr 1 | 125 bp | 120 bp | 180 bp |
| Apr 30 | 85 bp | 65 bp | 80 bp |

**Vol trade outcomes:**

**Long vol (entered Feb 19):**

Position: 3M straddle @ 48 bp, premium 0.35%

| Date | Spread | Payer Value | Receiver Value | Total | P&L |
|------|--------|-------------|----------------|-------|-----|
| Entry | 48 bp | 0.18% | 0.17% | 0.35% | 0 |
| Mar 23 | 160 bp | 5.04% | 0% | 5.04% | **+4.69%** |

**Return: +1,340% on premium paid!**

**Short vol (entered Feb 19):**

Position: Sold 3M straddle @ 48 bp, received 0.35%

| Date | Spread | Payer Liability | Net P&L |
|------|--------|-----------------|---------|
| Entry | 48 bp | - | +0.35% |
| Mar 23 | 160 bp | -5.04% | **-4.69%** |

**Loss: -1,340% on premium received** (massive loss)

**The lesson:**

- Long vol was a genius trade (if you had it)
- Short vol was a disaster
- Vol premium earned slowly, lost quickly
- Size short vol positions for worst case

**Post-crisis opportunity (April 2020):**

Implied vol at 200+ bp was extreme. Selling vol after the peak:

| Entry | Implied Vol | 3M Later | Realized Vol | P&L |
|-------|-------------|----------|--------------|-----|
| Apr 1 | 120 bp | 65 bp | 80 bp | +55 bp vega gain |

**Selling vol after crisis spikes has historically been profitable.**

---

## What to Remember


### 1. Core Concept


**Credit volatility trading profits from vol changes, not direction:**

$$
\text{Vol P\&L} \approx \text{Vega} \times (\sigma_{\text{realized}} - \sigma_{\text{implied}})
$$

- Long vol: Buy options/straddles, profit when spreads move
- Short vol: Sell options, collect premium, profit when spreads stable
- Neutral to direction if properly structured
- Vol spikes in crises, normalizes after

### 2. Key Instruments


| Instrument | Vol Exposure | Leverage | Liquidity |
|------------|--------------|----------|-----------|
| CDS Swaptions | Vega | 5-10x | Moderate |
| Straddles | Gamma + Vega | 5-10x | Moderate |
| Equity Tranche (0-3%) | High gamma | 15-20x | Lower |
| Mezzanine Tranche | Moderate | 5-8x | Lower |
| Index Options | Vega | 3-5x | Best |

### 3. Risk Management


**For long vol:**
- Premium is your max loss (defined risk)
- Time decay works against you
- Need significant moves to profit
- Size for 0% outcome (all premium lost)

**For short vol:**
- Max profit = premium received
- Max loss = unlimited (theoretically)
- Position limits: 1-2% of capital max
- Dynamic hedging required
- Stop-losses mandatory

### 4. Entry Criteria


**Long vol when:**
- Implied vol < 30th percentile
- Event risk approaching
- Vol premium negative
- Complacency indicators

**Short vol when:**
- Implied vol > 70th percentile
- Post-crisis normalization
- Catalyst calendar clear
- Vol premium > 25%

### 5. Common Mistakes


1. **Selling vol without stops:** Unlimited risk
2. **Oversizing long vol:** Time decay destroys
3. **Ignoring vol premium:** Systematic seller edge
4. **Wrong strike selection:** OTM options expire worthless
5. **Holding through expiry:** Delta hedging stops working
6. **Tranche correlation risk:** Different from spread vol
7. **Liquidity assumption:** Vol products widen in crisis
8. **Curve/smile ignorance:** Skew matters

### 6. Final Wisdom


> "Credit volatility is the fear gauge of corporate credit markets. When vol is low, complacency reigns and spreads are tight. When vol spikes, panic sets in and spreads blow out. The natural trade is to sell vol—collect premium from fearful hedgers during normal times, then lose it all in the next crisis. The survivors do two things: (1) size short vol for worst-case (March 2020 showed 5x normal moves are possible), and (2) flip to long vol when implied is cheap and catalysts approach. The 2020 COVID vol spike created 1,000%+ returns for long vol traders and wiped out short vol desks. The secret is knowing when to be on each side. Sell vol when implied is extreme (post-crisis), buy vol when implied is cheap (pre-crisis complacency). Simple to describe, hard to time. When in doubt, be flat—vol is not a trade you want to be wrong on."

**Keys to success:**

1. **Respect the regime:** Vol mean-reverts but can stay extreme
2. **Size for disaster:** Short vol can lose 10-20x premium
3. **Trade the premium:** Implied vs. realized spread
4. **Event calendar:** Know when catalysts are
5. **Use stops:** Exit short vol if moves against
6. **Post-crisis opportunity:** Sell vol after spikes
7. **Pre-crisis opportunity:** Buy vol when cheap
8. **Delta hedge:** Don't let vol trade become directional

**Most critical rule:**

$$
\text{Short Vol Size} = \frac{\text{Max Loss Tolerance}}{10 \times \text{Normal Vol}}
$$

If you can lose $1M max and normal vol is 50 bp, size for 10 × 50 = 500 bp move.

That means $1M / (500 bp × Duration × Notional) = very small position.

Short vol is picking up nickels in front of steamrollers. Size accordingly. 🎯📊⚠️
