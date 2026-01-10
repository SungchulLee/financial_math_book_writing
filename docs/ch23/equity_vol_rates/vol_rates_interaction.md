# Vol vs Rates Interaction

**Volatility and interest rates interact** through multiple channels where rising rates typically increase equity volatility (higher discount rates, tighter financial conditions), decrease bond prices while increasing bond volatility (duration effect), affect option pricing directly through the risk-free rate term in Black-Scholes, and create complex cross-asset dynamics where Fed policy drives both rate and volatility regimes, making swaption volatility, MOVE index (bond market VIX), and rate-vol correlation critical for cross-asset positioning and risk management.

---

## The Core Insight

**The fundamental idea:**

- Rates and volatility linked through multiple channels
- Fed policy drives both (tight policy → higher rates + higher vol)
- Rising rates increase equity volatility (tightening conditions)
- Rising rates increase bond volatility (duration effect)
- Option pricing sensitive to rates (risk-free rate in Black-Scholes)
- Volatility surfaces shift with rate regime
- Cross-asset strategies exploit rate-vol relationships

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/rates_vol_interaction.png?raw=true" alt="rates_vol_interaction" width="700">
</p>
**Figure 1:** Three-dimensional surface showing interaction between interest rates, equity volatility (VIX), and bond volatility (MOVE index) across different Fed policy regimes, illustrating how tightening cycles increase both volatility measures while rate cuts reduce uncertainty, with correlation dynamics varying between normal periods (ρ ≈ 0.3) and crisis periods (ρ ≈ 0.8).

**You're essentially asking: "How do interest rates affect volatility across asset classes, and how do I trade these relationships?"**

---

## What Is the Rate-Vol Link?

### 1. Fed Policy Channel

**Central bank affects both:**

**Tight policy (hiking rates):**
- Higher interest rates
- Tighter financial conditions
- Slower economic growth
- **Higher uncertainty** (equity vol up)
- **Higher bond vol** (rate changes frequent)

**Loose policy (cutting rates):**
- Lower interest rates
- Easier financial conditions
- Stimulus for economy
- **Lower uncertainty** (equity vol down)
- **Lower bond vol** (rate stability)

**Example—2022-2023 hiking cycle:**

**2022:**
- Fed funds: 0% → 4.5% (rapid hikes)
- VIX: Average 25 (elevated)
- MOVE: Average 120 (elevated bond vol)

**2023:**
- Fed funds: 4.5% → 5.5% (slower pace)
- VIX: Average 18 (calming)
- MOVE: Average 100 (normalizing)

**Correlation:** Rate changes and volatility positive during transitions

### 2. Discount Rate Channel

**Equity valuation:**

$$
P = \frac{E[\text{Dividends}]}{r - g}
$$

Where $r$ = discount rate (risk-free rate + equity premium)

**Higher rates → Lower P (mechanical)**

**But also:**
- Higher uncertainty about future rates
- Higher volatility in discount factor
- **Higher equity volatility**

**Example:**

10-year Treasury: 2% → 5% (rapid rise)
- Equity valuations compressed (P/E down)
- Uncertainty about future rates high
- VIX elevated throughout transition

### 3. Bond Duration Channel

**Bond price sensitivity:**

$$
\Delta P \approx -D \times \Delta r
$$

Where $D$ = duration

**Higher rate volatility:**

$$
\text{Bond Price Vol} = D \times \text{Rate Vol}
$$

**Example:**

- 10-year Treasury, duration = 8
- Rate vol: 10 bps/day
- Bond price vol: $8 \times 0.10\% = 0.8\%$ daily

**If rate vol doubles to 20 bps/day:**
- Bond price vol: $8 \times 0.20\% = 1.6\%$ daily
- **MOVE index doubles**

### 4. Option Pricing Channel

**Black-Scholes formula:**

$$
C = S N(d_1) - K e^{-rT} N(d_2)
$$

**Rate appears directly in:**
- Discount factor: $e^{-rT}$
- Forward price: $S e^{(r-q)T}$
- $d_1, d_2$ calculations

**Higher rates:**
- Increase call values (forward price higher)
- Decrease put values (discount factor smaller)
- Affect put-call parity

**Example:**

ATM call, strike $100, 1 year, vol 25%

**At r = 2%:**
- Call value: $10.45

**At r = 5%:**
- Call value: $11.20
- **Difference: +7.2%**

**For puts:**
- At r = 2%: $8.47
- At r = 5%: $7.25
- **Difference: -14.4%**

### 5. MOVE Index

**Bond market volatility gauge:**

$$
\text{MOVE} = \text{Weighted average of implied vol on Treasury options}
$$

**Similar to VIX but for bonds:**
- Based on 1-month Treasury options
- Across 2Y, 5Y, 10Y, 30Y
- Reflects bond market uncertainty

**Typical levels:**
- Normal: 80-100
- Elevated: 120-150
- Crisis: 150-200+
- 2020 peak: 264

**Relationship to VIX:**

**Normal times:** $\rho_{\text{VIX, MOVE}} \approx 0.3$ (weakly correlated)
**Crisis times:** $\rho_{\text{VIX, MOVE}} \approx 0.8$ (strongly correlated)

### 6. Swaption Volatility

**Volatility of interest rate swaps:**

**ATM swaption vol:**
- Implied volatility of options on swap rates
- Quoted in basis points
- Reflects rate uncertainty

**Example:**

5Y into 5Y swaption (option to enter 5Y swap in 5 years)
- Vol: 80 bps (normal)
- Vol: 120 bps (elevated)

**Drivers:**
- Fed policy uncertainty
- Economic data surprises
- Financial conditions

**Relationship to equity vol:**

Positive correlation (0.4-0.6) because:
- Both reflect macro uncertainty
- Fed policy affects both
- Risk-off moves affect both

### 7. Volatility Surface Skew

**Rates affect skew:**

**Low rate environment:**
- Equity skew: Steep (put vol >> call vol)
- Investors demand crash protection
- Zero lower bound concern

**Rising rate environment:**
- Equity skew: Flattens
- Less crash fear (soft landing hope)
- Put demand moderates

**Example—Skew (25-delta put vol - 25-delta call vol):**

**2020 (rates near zero):**
- Skew: 8 vol points (steep)

**2023 (rates at 5%):**
- Skew: 5 vol points (flatter)

**Mechanism:**
- Low rates → tail risk fears
- Higher rates → normalized risk pricing

---

## Key Terminology

**MOVE Index:**
- Bond market volatility gauge
- Treasury option implied vols
- "VIX for bonds"
- Normal: 80-100, Crisis: 150+

**Swaption:**
- Option on interest rate swap
- Reflects rate uncertainty
- Quoted in basis points
- Key for rate vol trading

**Duration:**
- Bond price sensitivity to rates
- Measured in years
- Higher duration = more rate risk
- Links rates to bond volatility

**Fed Put:**
- Belief Fed will ease if markets crash
- Affects rate-vol correlation
- Asymmetric relationship
- Broken during some hiking cycles

**Rate Volatility:**
- Daily changes in interest rates
- Measured in basis points
- Drives bond price volatility
- Key input for swaptions

**Convexity:**
- Non-linear rate sensitivity
- Second derivative of price
- Positive for bonds (beneficial)
- Amplifies vol at extremes

**Real Rates:**
- Nominal rates - inflation
- Affect equity valuations
- Drive growth expectations
- Interact with volatility regime

---

## Rate-Vol Strategies

### 1. Equity Vol + Rate Positioning

**Exploit positive correlation:**

**Strategy:** When Fed hiking aggressively
- Long equity volatility (VIX calls)
- Long rate volatility (MOVE exposure)
- Both benefit from uncertainty

**Example (2022):**

**March 2022:** Fed begins hiking
- Long VIX 25 calls: Cost $3
- Long MOVE through swaptions: Cost 2% of notional

**June 2022:** Fed hikes 75 bps (shock)
- VIX: 20 → 32
- MOVE: 100 → 140
- VIX calls: $3 → $10 (233%)
- Swaptions: 2% → 6% (200%)
- **Both profitable**

**Rationale:** Fed uncertainty drives both volatilities

### 2. Duration-Adjusted Equity Hedging

**Account for rate impact:**

**Traditional hedge:**
- Buy equity puts (protect against equity fall)

**Enhanced hedge:**
- Buy equity puts (equity protection)
- Long duration bonds (rate cut benefit)
- In equity crash, Fed likely to cut
- Duration gains offset some equity loss

**Example:**

**Portfolio:** $10M equity
**Crash scenario:** S&P -20%

**Traditional:**
- Equity: -$2M
- Puts: +$1.5M
- **Net: -$500K**

**With duration:**
- Equity: -$2M
- Puts: +$1.5M
- Long 30Y Treasury: +$800K (rates fall 50 bps, duration 20)
- **Net: +$300K** (profitable in crash!)

### 3. Volatility Carry with Rate Hedging

**Sell vol, hedge rate risk:**

**Strategy:**
- Sell equity volatility (collect premium)
- Hedge with rate volatility (if Fed hiking)

**Example:**

- Short VIX futures: Collect 2 points/month
- Long MOVE (swaptions): Cost 1 point/month equivalent
- **Net carry: 1 point/month**

**Protection:**
- If macro shock hits → Both spike together
- MOVE gains partially offset VIX losses
- Reduced tail risk

### 4. Rate-Vol Dispersion

**Index rate vol vs. single-maturity:**

**Strategy:**
- Short swap rate vol index
- Long individual maturity vols (e.g., 2Y, 10Y, 30Y)
- Bet on dispersion (yield curve twist)

**Example:**

- Short aggregate swaption vol: Receive 80 bps
- Long 2Y vol, 10Y vol, 30Y vol: Pay 90 bps
- Net: Pay 10 bps upfront

**Payoff:**
- If yield curve steepens dramatically (2Y down, 30Y up)
- Individual maturities' vol spikes
- Aggregate vol rises less
- **Dispersion trade wins**

### 5. Options on Bond Futures

**Trade bond vol directly:**

**Strategy:** Volatility expectations on rates
- Buy options on Treasury futures
- Isolate rate volatility
- Delta-hedge to remove directional

**Example:**

10Y Treasury futures at 110
- Buy 110 straddle (call + put): $3.00
- Delta-hedge daily

**If rate volatility rises:**
- Gamma scalping profits
- Pure rate vol exposure

**If rate volatility falls:**
- Theta decay losses

### 6. Cross-Asset Volatility Arbitrage

**Relative value across assets:**

**Observation:** Equity vol rich, bond vol cheap

**Strategy:**
- Short equity vol (VIX futures)
- Long bond vol (MOVE exposure)
- Bet on convergence

**Example:**

- VIX/MOVE ratio: 0.20 (elevated)
- Historical average: 0.18
- Trade: Short VIX, long MOVE
- When ratio reverts to 0.18 → Profit

**Risk:** Correlations unstable (can diverge further)

### 7. Fed Meeting Volatility

**Event-driven:**

**Strategy:** Trade around FOMC meetings
- Vol spikes before meetings
- Crushes after (resolution)

**Implementation:**
- Sell short-dated options before meeting
- Cover immediately after
- Collect event premium

**Example:**

Week before FOMC:
- 1-week ATM straddle: 2% of spot
- Historic average: 1.5%
- **Event premium: 0.5%**

**After meeting:**
- Vol crushes back to 1.5%
- Close position
- **Profit: 0.5%** (on notional)

**Risk:** Surprise decision (shock) = losses

---

## Common Mistakes

### 1. Ignoring Rate Impact on Options

**Forgetting risk-free rate:**

- **Mistake:** Price options using old rate assumptions
- **Why it fails:** Rates moved 300 bps, changes pricing
- **Fix:** Update risk-free rate in models
- **Real cost:** 5-15% mispricing on long-dated options

**Example:**

1-year call priced at r = 1% (2020)
- Fair value: $10

**2023, r = 5%:**
- Fair value: $11.50
- Market: $11.50
- Your model: $10 (stale)
- **Underpricing: 13%**

### 2. Assuming Stable Correlation

**Rate-vol correlation time-varying:**

- **Mistake:** Use average correlation (0.3)
- **Why it fails:** Spikes to 0.8 in crisis
- **Fix:** Model regime-dependent correlation
- **Real cost:** Hedge fails in crisis

**Example:**

Hedged equity with bonds (assuming negative correlation)
- Normal: Stocks down, bonds up ✓
- Crisis (March 2020): Both down! ✗
- **Correlation flipped positive**

### 3. Duration Mismatch

**Tenor mismatch:**

- **Mistake:** Hedge 10-year equity risk with 2-year rate vol
- **Why it fails:** 2Y rates driven by Fed, 10Y by growth/inflation
- **Fix:** Match tenor to economic sensitivity
- **Real cost:** Hedge uncorrelated with risk

**Example:**

Equity sensitive to growth (10Y real rates)
- Hedged with 2Y swaptions (Fed driven)
- 10Y rates spike, 2Y stable
- **Hedge ineffective**

### 4. Ignoring Convexity

**Linear approximation breaks:**

- **Mistake:** Use duration only (linear)
- **Why it fails:** Large rate moves = convexity matters
- **Fix:** Include convexity in calculations
- **Real cost:** 20-30% error on large moves

**Example:**

Bond portfolio, duration = 10, convexity = 100

**100 bps rate rise:**
- Duration estimate: -10%
- With convexity: -10% + 0.5 × 100 × (0.01)² = -9.5%
- **Convexity benefit: 0.5%**

**300 bps rate rise:**
- Duration: -30%
- With convexity: -30% + 0.5 × 100 × (0.03)² = -25.5%
- **Convexity benefit: 4.5%** (significant!)

### 5. Fed Put Overconfidence

**Assuming Fed always eases:**

- **Mistake:** "Equity crash = Fed cuts = long duration always works"
- **Why it fails:** 2022 example (Fed hiking despite equity down)
- **Fix:** Consider inflation regime
- **Real cost:** Duration losses compound equity losses

**Example (2022):**

Equity -20%, bought duration expecting Fed cuts
- But Fed prioritized inflation fight
- Continued hiking despite equity weakness
- Rates: 1% → 5%
- Duration: -30% (30-year Treasury)
- **Both equity and bonds down** (6/40 portfolio ≠ safe)

### 6. MOVE vs. VIX Spread Trading

**Naive correlation trades:**

- **Mistake:** Trade MOVE/VIX ratio mechanically
- **Why it fails:** Regimes differ (QE vs. QT, etc.)
- **Fix:** Understand macro regime
- **Real cost:** Ratio diverges further

**Example:**

MOVE/VIX historically 0.18, currently 0.25
- Trade: Short MOVE, long VIX (bet on convergence)
- But QT regime means structurally higher MOVE
- Ratio stays elevated
- **Loss on carry while waiting**

### 7. Event Premium Misjudgment

**Wrong side of event vol:**

- **Mistake:** Sell vol before big Fed meeting (collect premium)
- **Why it fails:** Surprise decision = massive vol spike
- **Fix:** Only sell if truly expect no surprise
- **Real cost:** 5-10× premium collected

**Example:**

Sold 1-week straddle before FOMC for 1.5%
- Expected: Normal meeting, crush to 1%
- Reality: 75 bps hike (shock!), vol → 3%
- **Loss: 1.5%** (100% of premium + then some)

---

## Best vs. Worst Case

### 1. Best Case: Success

**2022 rate-vol trade:**

**Setup (January 2022):**
- Portfolio: $50M equity
- Fed beginning to hike (from zero)
- High uncertainty about pace

**Strategy:**
1. **Long equity vol:** Buy VIX 20/30 call spreads
   - Cost: $2 per spread × 1,000 = $200K

2. **Long rate vol:** Buy swaptions (2Y)
   - Notional: $50M
   - Cost: 1% = $500K

3. **Total hedge cost:** $700K (1.4% of portfolio)

**March-June 2022:**

**March:** 25 bps hike (dovish)
- VIX: 20 (flat)
- MOVE: 95 (slight rise)
- Hedge: -$100K (time decay)

**May:** 50 bps hike (hawkish)
- VIX: 30 (spike!)
- MOVE: 115 (elevated)
- Hedge: +$500K (VIX spreads profitable)

**June:** 75 bps hike (shock!)
- VIX: 32 (sustained)
- MOVE: 140 (spike!)
- Hedge: +$1.2M (both legs profitable)

**Portfolio impact:**

**Equity:** -15% = -$7.5M (rate fears)
**VIX hedge:** +$1M (20/30 spreads maxed out)
**Swaptions:** +$1.8M (rate vol spike)
**Total hedge:** +$2.8M
**Net loss:** -$7.5M + $2.8M = **-$4.7M** (37% hedged)

**Q3-Q4 2022:**
- Continued hedging as Fed stayed aggressive
- Additional gains from vol
- **Full-year equity:** -18%
- **Full-year with hedges:** -8%
- **Hedges saved 10%**

**Success factors:**
1. Recognized rate-vol correlation in hiking cycle
2. Diversified between equity vol and rate vol
3. Sized appropriately (1.4% upfront)
4. Held through volatility
5. Used spreads to cap cost

### 2. Worst Case: Disaster

**Long duration + short vol disaster (2022):**

**Setup:**
- Hedge fund, $1B AUM
- "Balanced" portfolio: 60/40 stocks/bonds
- Plus: Short volatility overlay (income)

**Positions (January 2022):**
1. **$600M equity** (S&P 500 index)
2. **$400M long-duration bonds** (20+ year Treasuries)
3. **Short VIX futures:** $100M notional (collect roll yield)
4. **Short rate vol:** Sold swaptions, $500M notional

**Rationale:**
- "Diversified" across stocks and bonds
- Vol strategies low correlation (collect premium)
- Worked great 2010-2021

**Q1 2022: Fed begins hiking**

**January-March:**
- Equity: -5% = -$30M
- Bonds: -8% (rates rising) = -$32M
- Short VIX: -10% (contango) = +$10M
- Short swaptions: -5% (vol rising) = -$25M
- **Net: -$77M** (-7.7%)

**Losses accelerate:**

**April-June:**
- Equity: Additional -10% = -$60M
- Bonds: Additional -12% = -$48M
- Short VIX: VIX spike to 32 = -$40M (futures jumped)
- Short swaptions: Rate vol spike = -$80M
- **Net additional: -$228M** (-22.8%)

**Cumulative (6 months):**
- **Total loss: -$305M (-30.5%)**

**What went wrong:**

1. **Positive correlation:** Stocks AND bonds fell together (rare!)
2. **Vol spikes:** Both equity vol and rate vol spiked
3. **Leverage:** Short vol positions amplified losses
4. **Forced unwind:** Margin calls forced buying vol at worst prices

**Investor panic:**

**July 2022:**
- Redemption requests: 40% of AUM
- Forced to liquidate at losses
- Sold equities at bottom
- Covered vol shorts at tops
- **Additional losses: $150M**

**Total losses: $455M (45.5% down)**

**Aftermath:**
- Fund shut down October 2022
- Lawsuits from investors
- "Diversified" portfolio all lost simultaneously

**Lessons:**
1. 60/40 correlation can flip positive in rate shock
2. Short vol overlays amplify pain in vol spikes
3. Rate vol and equity vol correlate in Fed transitions
4. "Income strategies" are often hidden leverage
5. Diversification fails when risk is macro (Fed policy)

---

## Risk Management Rules

### 1. Rate Sensitivity Monitoring

**Daily tracking:**

$$
\Delta V = \text{Duration} \times \Delta r
$$

**Equity options:**

$$
\Delta V_{\text{option}} = \text{Rho} \times \Delta r
$$

**Limits:**

- Portfolio rho (rate sensitivity): Monitor daily
- If $|\text{Rho}| > 10\%$ of portfolio value per 100 bps → Hedge

### 2. Correlation Regime Detection

**Monitor rolling correlation:**

$$
\rho_t = \text{Corr}_{t-60:t}(\Delta \text{VIX}, \Delta \text{MOVE})
$$

**Regime classification:**
- If $\rho < 0.3$: Independent (normal)
- If $0.3 \leq \rho < 0.6$: Moderate correlation
- If $\rho \geq 0.6$: High correlation (risk-off)

**Hedge ratios increase with correlation**

### 3. Fed Policy Tracking

**Monitor:**
- Fed dots (rate projections)
- Fed minutes (policy direction)
- Inflation data (CPI, PCE)
- Financial conditions (credit spreads, equity levels)

**If Fed in tightening mode:**
- Reduce short vol exposure
- Increase rate vol hedges
- Expect higher equity vol

### 4. Duration Limits

**By strategy:**

- Equity portfolio: Max duration 5 (bonds)
- Vol selling: Max duration 3 (conservative)
- Directional rate: Max duration 15 (aggressive)

**Example:**

Equity portfolio $10M
- Max bond allocation: $3M (30%)
- Max duration 5: Use 6-year Treasury (duration ≈ 5.5)

### 5. Event Risk Management

**FOMC meetings:**

- Reduce short vol positions 1 week before
- Consider event hedges (cheap OTM options)
- Size for 50 bps surprise

**Other events:**
- Employment reports
- Inflation data
- Fed speeches

### 6. Cross-Asset Stress Testing

**Scenarios:**

1. **Rates up 100 bps, VIX +10 points**
2. **Rates up 200 bps, VIX +20 points**
3. **Rates down 100 bps, VIX +15 points** (crisis)
4. **Rates flat, VIX +25 points** (equity-specific)

**Maximum loss:**

$$
\text{Max Stress Loss} \leq 15\% \text{ of Capital}
$$

### 7. Volatility Budget

**Allocate vol risk across assets:**

- Equity vol risk: 50%
- Rate vol risk: 30%
- FX vol risk: 20%

**Don't concentrate:** Both equity and rate vol high simultaneously

---

## Real-World Examples

### 1. Taper Tantrum (2013)

**Fed announces QE taper:**

**May 2013:** Bernanke mentions tapering

**Market reaction:**
- 10Y Treasury: 1.6% → 3.0% (rapid rise)
- MOVE: 60 → 110 (spike)
- VIX: 12 → 20 (moderate rise)
- Correlation: VIX-MOVE spiked to 0.7

**Winners:**
- Long rate vol: +50%
- Long MOVE index: +80%

**Losers:**
- Long duration bonds: -15%
- Short rate vol: -60%

### 2. COVID Response (2020)

**Fed cuts to zero + QE infinity:**

**March 2020:**
- Fed funds: 1.5% → 0% (emergency)
- VIX: 80 (panic)
- MOVE: 160 (bond panic)

**Both equities and bonds crushed:**
- S&P: -35%
- 30Y Treasury: -10% (shocking!)
- Correlation: Positive (unusual)

**April-May:**
- Fed QE = $120B/month
- Volatilities collapsed
- VIX: 80 → 25
- MOVE: 160 → 60

**Winners (after stabilization):**
- Long duration: +30% (rates pinned)
- Short vol (if started after panic): +40%

### 3. 2022 Hiking Cycle

Described in detail in Worst Case above.

**Key lesson:** Rate vol and equity vol both spike in aggressive hiking

### 4. 2018 Q4 Correction

**Fed hiking despite equity weakness:**

**Setup:** Fed on autopilot (rate hikes + QT)

**December 2018:**
- S&P: -19.8% (near bear market)
- VIX: 36 (spiked)
- MOVE: 70 (elevated but not extreme)

**Fed reaction:** Pivoted dovish (January 2019)

**Q1 2019:**
- S&P: +13% (recovered)
- VIX: 15 (normalized)
- MOVE: 50 (calm)

**Trade:** Long equity, long duration (both rallied on Fed pivot)

---

## Practical Steps

### 1. Monitor Key Indicators

**Daily:**
- VIX level and term structure
- MOVE index
- 2Y and 10Y Treasury yields
- Swaption vols

**Weekly:**
- Rolling VIX-MOVE correlation (60-day)
- Fed funds futures (policy expectations)
- Credit spreads (financial conditions)

### 2. Calculate Sensitivities

**Portfolio rho:**

$$
\text{Rho}_{\text{portfolio}} = \sum_{i} w_i \times \text{Rho}_i
$$

**Example:**

- 60% equity (rho ≈ +5% per 100 bps)
- 40% bonds (duration 7 = -7% per 100 bps)

$$
\text{Rho} = 0.6 \times 5 + 0.4 \times (-7) = 3 - 2.8 = +0.2\%
$$

**Portfolio gains 0.2% per 100 bps rate rise** (slight positive sensitivity)

### 3. Set Hedge Ratios

**Based on correlation regime:**

**Normal ($\rho = 0.3$):**
- Equity vol hedge: 50% of desired protection
- Rate vol hedge: 20% of desired protection

**Elevated ($\rho = 0.6$):**
- Equity vol hedge: 70%
- Rate vol hedge: 50%

### 4. Implement Hedges

**Equity vol:** VIX call spreads or put options
**Rate vol:** Swaptions or bond options
**Combined:** Straddles on rate-sensitive sectors (banks, REITs)

### 5. Rebalance

**Triggers:**
- Correlation crosses threshold (±0.2)
- Fed policy shift
- Quarterly scheduled rebalance
- Rate move > 50 bps in month

### 6. Attribution

**Decompose P&L:**

$$
\text{P&L} = \text{Equity} + \text{Rates} + \text{Equity Vol} + \text{Rate Vol} + \text{Interactions}
$$

**Example:**

Monthly: +1.5%

**Attribution:**
- Equity: +2.0%
- Rates (duration): -0.5%
- Equity vol (short): -0.3%
- Rate vol (long): +0.5%
- Interaction: -0.2%
- **Total: 1.5%**

### 7. Review and Learn

**Quarterly:**
- Were rate-vol correlations as expected?
- Did hedges perform as designed?
- Update correlation assumptions
- Adjust hedge ratios
- Document lessons

---

## Final Wisdom

> "The rate-volatility interaction is the axis around which modern cross-asset markets rotate—Fed policy simultaneously drives interest rates and uncertainty, creating a fundamental coupling that most investors understand intellectually but fail to internalize operationally. Rising rates don't just mechanically reduce bond prices through duration and equity valuations through discount rates; they increase volatility across all assets by tightening financial conditions and introducing uncertainty about the path forward. The 2022 debacle taught us that the classic 60/40 portfolio can fail catastrophically when rate shocks are large enough—both stocks and bonds fell together, a correlation regime that shattered decades of diversification assumptions. The VIX-MOVE correlation is time-varying and regime-dependent: it's 0.3 in normal times (different drivers), but spikes to 0.8 in crisis (common macro fear factor). Option pricing formulas embed this dependency through the risk-free rate term, but practitioners often forget that a 300 bps rate rise changes option values by 10-20% even holding volatility constant. Swaptions and the MOVE index are the unsung heroes of cross-asset volatility trading—they allow pure bets on rate uncertainty decoupled from direction, creating triangulation opportunities with equity vol. The deepest insight: short volatility strategies—whether equity vol, rate vol, or both—are structurally short the Fed put, meaning they profit from stability but catastrophically lose when the Fed must tighten or ease aggressively. Every major vol blow-up (LTCM, 2008, XIV 2018, 2022 60/40) traces back to underestimating the Fed's impact on volatility across assets. Manage rate-vol interaction not as two separate risks but as a unified macro regime: track Fed policy, monitor correlation regimes, diversify vol exposure across equity and rates, and never, ever short both simultaneously without understanding you're making a massive bet on stable, predictable Fed policy—which history shows is the exception, not the rule."

**Key to success:**

- Monitor Fed policy as primary driver (affects both rates and vol)
- Track VIX-MOVE correlation regime (0.3 normal, 0.8 crisis)
- Update risk-free rate in models (material impact on options)
- Diversify vol exposure (equity vol + rate vol, not just one)
- Account for duration in equity hedges (use long bonds in equity crash)
- Size for rate shocks (stress test 200 bps moves)
- Remember 60/40 can fail (positive correlation possible in rate shocks)
- Never short both equity vol and rate vol simultaneously (doubling down on stability)
