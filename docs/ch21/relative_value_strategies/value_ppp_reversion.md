# Value and PPP Reversion


**Value and PPP reversion** strategies exploit currency mispricings relative to fundamental economic measures,
betting that exchange rates eventually converge toward purchasing power parity and other equilibrium levels over medium to long-term horizons.

---

## The Core Insight


**The fundamental idea:**

- Currencies deviate from fair value
- PPP provides long-run anchor
- Real exchange rates mean-revert
- Overshoots create opportunities
- Patience required (months to years)
- Multiple value metrics converge

<p align="center">
<img src="https://github.com/SungchulLee/img/raw=true" alt="ppp_reversion" width="700">
</p>
**Figure 1:** Real effective exchange rate deviation from PPP equilibrium for major currencies, 
showing persistent mispricings that eventually revert, creating systematic trading opportunities with holding periods of 1-3 years.

**You're essentially betting: "Currencies far from fair value will eventually revert to equilibrium as economic fundamentals reassert."**

---

## Theoretical Foundation


### 1. Purchasing Power Parity


**The fundamental relationship:**

**Absolute PPP:**

$$
S = \frac{P_{\text{domestic}}}{P_{\text{foreign}}}
$$

Where:
- $S$ = Spot exchange rate (domestic per foreign)
- $P_{\text{domestic}}$ = Price level domestically
- $P_{\text{foreign}}$ = Price level in foreign country

**Economic interpretation:**

- Exchange rate should equal price ratio
- One currency unit buys same basket everywhere
- Law of one price extended to economy
- Arbitrage enforces equality

**Example:**

- Big Mac costs $5.50 in US
- Big Mac costs £4.00 in UK
- PPP-implied rate: $5.50 / £4.00 = 1.375 $/£
- Actual rate: 1.27 $/£
- **GBP undervalued by 8%**

### 2. Relative PPP


**More practical formulation:**

$$
\frac{S_{t+1}}{S_t} = \frac{1 + \pi_{\text{domestic}}}{1 + \pi_{\text{foreign}}}
$$

**Simplifying (for small inflation):**

$$
\Delta s \approx \pi_{\text{domestic}} - \pi_{\text{foreign}}
$$

**Economic meaning:**

- Currency change = inflation differential
- High inflation currency depreciates
- Low inflation currency appreciates
- Holds over long periods (5-10 years)

**Example (2010-2020):**

- US inflation: 1.8% avg
- Turkey inflation: 10.5% avg
- Expected depreciation: 8.7% annually
- Actual TRY depreciation: ~9.5% annually
- **Relative PPP roughly held**

### 3. Real Exchange Rate


**Deflating nominal rate:**

$$
q_t = S_t \times \frac{P_{\text{foreign}}}{P_{\text{domestic}}}
$$

**Mean reversion property:**

$$
q_t = \bar{q} \times e^{\epsilon_t}
$$

Where:
- $\bar{q}$ = Long-run equilibrium
- $\epsilon_t$ = Temporary deviation
- $E[\epsilon_t] = 0$ over time

**Statistical evidence:**

- Half-life of deviations: 3-5 years
- Mean reversion speed: 15-25% annually
- Larger deviations revert faster
- Works better for major currencies (G10)

---

## Value Measurement


**Quantifying currency mispricing:**

### 1. REER (Real Effective Exchange Rate)


**Trade-weighted real rate:**

$$
\text{REER}_t = \prod_{i=1}^{N} \left( \frac{S_{i,t} P_{i,t}}{P_{\text{domestic},t}} \right)^{w_i}
$$

Where:
- $S_{i,t}$ = Bilateral exchange rate with country $i$
- $P_{i,t}$ = Price level in country $i$
- $w_i$ = Trade weight (exports + imports share)
- $N$ = Number of trading partners

**Interpretation:**

- REER > 100 (base year) → Currency overvalued
- REER < 100 → Currency undervalued
- Normalized to trading partners
- Accounts for inflation differentials

**Using REER for trades:**

- Calculate current REER percentile (past 20 years)
- Above 80th percentile → Overvalued (short)
- Below 20th percentile → Undervalued (long)
- Exit when crosses 50th percentile (fair value)

### 2. Big Mac Index


**The Economist's measure:**

$$
\text{Value Gap} = \frac{S_{\text{actual}} - S_{\text{PPP}}}{S_{\text{PPP}}} \times 100\%
$$

**Example (Jan 2024):**

| Country | Big Mac Price | Implied Rate | Actual Rate | Over/Under |
|---------|---------------|--------------|-------------|------------|
| Norway | 58 NOK | 10.55 $/NOK | 10.85 | +2.8% |
| Switzerland | 6.50 CHF | 0.85 $/CHF | 0.88 | +3.4% |
| Japan | 450 JPY | 0.0122 $/JPY | 0.0067 | **-45%** |
| Mexico | 69 MXN | 0.080 $/MXN | 0.059 | **-26%** |

**Trading signal:**

- JPY deeply undervalued → Long JPY
- CHF overvalued → Short CHF
- But need catalyst for reversion (time + rates)

### 3. Terms of Trade


**Export/import price ratio:**

$$
\text{TOT}_t = \frac{P_{\text{exports},t}}{P_{\text{imports},t}}
$$

**Impact on currency:**

- TOT improves → Currency appreciates
- Commodity exporters benefit when prices rise
- Net importers suffer when commodity prices surge
- Strong predictor for AUD, CAD, NOK, BRL

**Example (Australia 2020-2022):**

- Iron ore: $60 → $120/ton
- Coal: $50 → $200/ton
- TOT improved 60%
- AUD strengthened 0.62 → 0.74 (19%)
- **TOT explains currency move**

### 4. Balassa-Samuelson Effect


**Productivity adjustment:**

$$
\text{PPP}_{\text{adjusted}} = \text{PPP}_{\text{raw}} \times \left( \frac{\text{Productivity}_{\text{domestic}}}{\text{Productivity}_{\text{foreign}}} \right)^{\alpha}
$$

**Key insight:**

- Rich countries have expensive currencies
- High productivity → higher wages → higher prices
- PPP must adjust for income level
- Emerging markets systematically "cheap" by raw PPP

**Practical application:**

- Don't use raw Big Mac PPP for EM
- Adjust for GDP per capita
- Compare within income cohorts
- USD tends overvalued, CNY/INR undervalued

---

## Core Strategies


**Practical implementations:**

### 1. REER Reversion Trade


**Classic value trade:**

**Setup:**

- Identify currency with extreme REER
- Above 90th percentile or below 10th percentile
- Confirm no structural shift (policy change, war)
- Establish mean reversion timeframe (1-3 years)

**Position structure:**

$$
\text{Position Size} = \frac{\text{Portfolio Risk} \times 0.03}{\text{Expected Annual Vol}}
$$

**Example (CHF 2015):**

- Swiss franc REER at 110 (90th percentile)
- Historical mean: 100
- Current: 10% overvalued
- Annual vol: 8%

**Trade:**

- Short CHF vs. EUR basket
- Size: 3% portfolio risk / 8% vol = **37% notional exposure**
- Time horizon: 2 years
- Target: REER → 100 (reversion to mean)

**Expected return:**

- Mean reversion: +10% (CHF weakens)
- Carry cost: -1.5% annually (CHF lower yield)
- **Net: +7% over 2 years (3.5% annually)**

### 2. Big Mac Arbitrage


**Consumer PPP trade:**

**Methodology:**

1. Calculate valuation gap for all currencies
2. Rank from most over/undervalued
3. Long bottom quintile (undervalued)
4. Short top quintile (overvalued)
5. Rebalance semi-annually

**Portfolio construction:**

**Long basket (undervalued):**

- JPY (-45%)
- MXN (-26%)
- ZAR (-30%)
- IDR (-35%)
- Equal weight: 25% each

**Short basket (overvalued):**

- CHF (+3%)
- NOK (+3%)
- SEK (+5%)
- Equal weight: 33% each

**Position sizing:**

- Total gross: 100% (50% long, 50% short)
- Dollar-neutral (no directional USD bet)
- Rebalance when gaps close or widen

**Expected performance:**

- Annual alpha: 2-4% (from reversion)
- Sharpe ratio: 0.5-0.8 (long-term)
- Max drawdown: 15-20% (can take years)
- Win rate: 60-65% (patience required)

### 3. Terms of Trade Trade


**Commodity currency strategy:**

**Mechanism:**

- TOT improves → Current account improves → Currency demand
- Strong correlation (ρ = 0.6-0.7 for AUD, CAD, NOK)
- Leading indicator (3-6 months)

**Implementation:**

**Long commodity exporters when TOT rising:**

- AUD (iron ore, coal)
- CAD (oil, lumber)
- NOK (oil, gas)
- BRL (soybeans, iron ore)

**Short commodity importers when TOT falling:**

- EUR (energy importer)
- JPY (imports everything)
- INR (oil importer)

**Trade example (2020-2021):**

**Observation:**

- Oil prices recovering ($40 → $70)
- Industrial metals surging (China stimulus)
- Canada's TOT improving

**Trade:**

- Long CAD/JPY
- Entry: 78.00
- Time: 12 months
- Rationale: CAD benefits (oil), JPY hurt (imports)

**Outcome:**

- CAD/JPY → 90.00 (+15%)
- Carry: +1.5%
- **Total: +16.5%**

### 4. Yield-Adjusted PPP


**Combining value and carry:**

**Formula:**

$$
\text{Attractiveness Score} = \frac{\text{Value Gap \%}}{\text{Historical Vol \%}} + \frac{\text{Yield Differential \%}}{2}
$$

**Logic:**

- Value gap = expected appreciation
- Vol = risk adjustment
- Yield = carry while waiting
- Higher score = better risk/reward

**Example (2023):**

| Pair | Value Gap | Vol | Yield Diff | Score |
|------|-----------|-----|------------|-------|
| USD/JPY | +30% | 8% | +5.25% | 6.4 |
| EUR/CHF | +8% | 6% | +3.50% | 3.1 |
| AUD/NZD | -5% | 7% | +0.50% | -0.5 |
| GBP/EUR | +12% | 7% | +1.50% | 2.5 |

**Trade:** Long USD/JPY (highest score)

- Value upside: JPY mean reversion (+30% over 2-3 years)
- Carry: +5.25% annually
- **Total expected: 15-20% annually**

**Risk:** BOJ intervention, risk-off unwind

---

## Greeks and Sensitivities


**Understanding position dynamics:**

### 1. Mean Reversion Speed (λ)


**Speed of convergence:**

$$
q_{t+1} = \bar{q} + \lambda(q_t - \bar{q}) + \epsilon_{t+1}
$$

Where:
- $\lambda$ = Persistence parameter (0 to 1)
- $1 - \lambda$ = Reversion speed

**Empirical estimates:**

- Major currencies (G10): λ = 0.80 → 20% reversion annually
- Emerging markets: λ = 0.85 → 15% reversion annually
- Half-life: $\ln(0.5) / \ln(\lambda)$ ≈ 3-5 years

**Trading implication:**

- Larger misalignment → faster reversion (non-linear)
- 10% overvaluation: 2% reversion annually
- 30% overvaluation: 8-10% reversion annually
- **Extreme values mean revert faster**

### 2. Volatility (σ)


**Position risk:**

$$
\text{Position Volatility} = \text{FX Vol} \times \text{Notional}
$$

**Typical annual vols:**

- Major pairs (EUR/USD, USD/JPY): 8-10%
- Commodity pairs (AUD/USD, USD/CAD): 10-12%
- EM currencies (USD/ZAR, USD/BRL): 15-20%
- Crisis periods: 2-3x normal

**Risk management:**

- Scale position inversely to vol
- High vol → smaller size
- Use options for tail protection in EM
- Monitor vol regime (exit if spikes > 2σ)

### 3. Carry Drag (θ)


**Time decay (or gain):**

$$
\text{Daily Carry} = \frac{\text{Notional} \times (r_{\text{long}} - r_{\text{short}})}{365}
$$

**Impact on value trades:**

**Favorable (carry enhances):**

- Long undervalued high-yield currency
- Example: Long BRL (undervalued + 10% yield)
- Earn while waiting for reversion
- Reduces breakeven (need smaller reversion)

**Unfavorable (carry hurts):**

- Long undervalued low-yield currency
- Example: Long JPY (undervalued but 0% yield)
- Pay carry while waiting
- Need larger reversion to profit

**Optimization:**

$$
\text{Optimal Position} = \frac{\text{Expected Reversion} + \text{Carry}}{\text{Risk (Vol)}}
$$

### 4. Correlation Risk (ρ)


**Cross-currency dependencies:**

**Key correlations (typical):**

- USD strength → All currencies weaken (ρ ≈ -0.6 to -0.8)
- Commodity pairs (AUD/CAD): ρ ≈ +0.7
- Safe havens (JPY/CHF): ρ ≈ +0.5
- EM basket: ρ ≈ +0.6 to +0.8

**Portfolio construction:**

- Diversify across uncorrelated pairs
- Avoid concentration in EM (all weaken together in crisis)
- Mix commodity and non-commodity pairs
- Include both value longs and shorts

**Risk-off behavior:**

- Correlations → 1 (all risk currencies crash)
- Value trades unwind simultaneously
- Leverage amplifies losses
- Diversification disappears

---

## Implementation Details


**Practical execution framework:**

### 1. Data Sources


**Essential inputs:**

**REER data:**

- BIS (Bank for International Settlements): Free, quarterly
- Central banks: Country-specific, monthly
- Bloomberg/Reuters: Real-time, comprehensive

**PPP estimates:**

- OECD: Detailed, annual
- World Bank: Broad coverage
- Economist Big Mac Index: Simple, semi-annual

**Terms of trade:**

- Country statistical agencies (monthly)
- IMF International Financial Statistics
- Bloomberg commodity indices

### 2. Valuation Thresholds


**Entry signals:**

**Strong value signal:**

- REER > 90th percentile (overvalued) OR < 10th percentile (undervalued)
- Value gap > 20% by PPP
- Terms of trade moved > 1.5σ
- Multiple metrics agree

**Moderate value signal:**

- REER 70th-90th or 10th-30th percentile
- Value gap 10-20%
- Single metric extreme
- Use smaller position size

**No signal:**

- REER 40th-60th percentile (fair value)
- Value gap < 10%
- Conflicting signals
- Stay flat

### 3. Position Sizing


**Risk-based framework:**

$$
\text{Notional} = \frac{\text{Portfolio} \times \text{Risk Target}}{\text{FX Pair Annual Vol}}
$$

**Conservative (1-2% risk per trade):**

- $1M portfolio
- 2% risk = $20,000
- USD/JPY vol: 8%
- Position: $20K / 0.08 = **$250K notional (25% of portfolio)**

**Aggressive (3-5% risk per trade):**

- Same portfolio
- 4% risk = $40,000
- Position: $40K / 0.08 = **$500K notional (50%)**

**Leverage considerations:**

- Value trades typically 1-3x leverage
- Higher for low-vol pairs (G10)
- Lower for high-vol pairs (EM)
- NEVER exceed 5x for PPP trades

### 4. Time Horizon


**Expected holding periods:**

**Major currencies (G10):**

- Minimum: 12 months
- Typical: 18-36 months
- Maximum: 5 years (if extreme misalignment persists)

**Emerging markets:**

- Minimum: 6 months
- Typical: 12-24 months
- Watch for structural breaks (policy shifts, crises)

**Rebalancing:**

- Review quarterly
- Exit if REER returns to 50th percentile (fair value)
- Exit if value gap closes > 75%
- Cut position if vol regime changes (crisis)

### 5. Hedging Approaches


**Tail risk protection:**

**Out-of-the-money options:**

- Cost: 1-2% annually for G10
- Strike: 10-15% OTM
- Tenor: 6 months, roll twice per year
- Protects against violent reversal

**Stop losses:**

- Technical: 10-15% from entry
- Fundamental: Exit if structural break (war, coup, default)
- Volatility: Exit if implied vol > 90th percentile

**Diversification hedging:**

- 5-10 positions across regions
- Mix value longs and shorts
- Include uncorrelated pairs
- Reduces single-position risk to 20-30%

---

## When It Works Best


**Optimal conditions for value trades:**

### 1. Extreme Misalignment


**Clear value signal:**

- REER at 95th+ or 5th- percentile
- 30%+ value gap by multiple metrics
- Historical precedent for reversion
- No structural change explaining deviation

**Example (GBP post-Brexit 2016):**

- GBP crashed 15% after referendum
- REER fell to 15th percentile
- No fundamental change (UK economy intact)
- Clear overreaction
- **GBP recovered 80% of loss over 2 years**

### 2. Patient Capital Environment


**Low volatility regime:**

- VIX < 20 (stable markets)
- Credit spreads tight
- Carry trades functioning
- Long time horizon viable
- No near-term crisis risk

**Why this matters:**

- Mean reversion takes time (years)
- High vol periods disrupt positioning
- Forced exits at bad prices
- Need calm seas to hold through fluctuations

### 3. Monetary Policy Alignment


**Central bank supporting reversion:**

**Overvalued currency:**

- Central bank wants weaker currency
- Verbal intervention or actual
- Rate cuts to discourage inflows
- Policy aids value trade

**Undervalued currency:**

- Central bank hiking rates
- Capital controls relaxed
- Attracting foreign investment
- Policy accelerates reversion

---

## When It Fails


**Danger signs and pitfalls:**

### 1. Structural Breaks


**Permanent regime shifts:**

**New equilibrium:**

- Brexit (GBP structurally weaker)
- China opening (CNY revaluation)
- Resource curse (commodity exporters)
- Demographic collapse (Japan aging)

**Recognition signals:**

- Policy framework changed permanently
- Productivity growth divergence
- Population trends
- Geopolitical realignment

**Action required:**

- Recalculate fair value
- Adjust REER baseline
- Exit if "mispricing" is actually new equilibrium
- Don't fight structural trends

### 2. Crisis and Risk-Off


**Violent mean reversion interruption:**

**What happens:**

- All risk currencies crash simultaneously
- Value trades unwind (forced selling)
- Correlations → 1 (no diversification)
- Leverage amplifies losses
- Liquidity vanishes

**Historical examples:**

- 1998 Asian crisis: EM value trades destroyed
- 2008 GFC: All carry/value trades unwound
- 2020 COVID: Flash crash erased positions

**Mitigation:**

- Size conservatively (max 3x leverage)
- Use options for tail protection
- Monitor VIX (exit if > 30)
- Keep 20% cash buffer
- Have pre-set circuit breakers

### 3. Central Bank Intervention


**Fighting the central bank:**

**Types of intervention:**

- Verbal (talking down/up currency)
- Direct market intervention (BOJ, SNB)
- Capital controls (China, India)
- Policy shock (Turkey rate cuts)

**Case study (CHF 2011-2015):**

- CHF overvalued by 20% (REER)
- SNB imposed 1.20 floor in EUR/CHF
- Value trade said "short CHF"
- But SNB defended floor for 4 years
- **Lesson: Central banks can delay mean reversion indefinitely**

**When abandoned (Jan 2015):**

- CHF surged 30% in minutes
- Value traders who persisted won big
- But most had exited (too early)
- Timing central bank capitulation = impossible

---

## Common Mistakes


**Frequent errors to avoid:**

### 1. Ignoring Structural Changes


**The mistake:**

- JPY "undervalued" by 30% for 10 years
- Trader keeps shorting USD/JPY
- "Mean reversion must happen!"
- Loses money for decade

**Why it fails:**

- Japan demographics (aging, low growth)
- Zero rates permanently (YCC policy)
- Trade surplus shrinking
- Fair value moved lower
- Old PPP baseline obsolete

**Fix:**

- Update fair value estimates every 2-3 years
- Consider structural factors (demographics, productivity)
- If "value" persists > 5 years, question assumption
- Accept new equilibrium exists

### 2. Insufficient Time Horizon


**The mistake:**

- Enter value trade with 6-month horizon
- Currency doesn't mean revert in time
- Exit at loss (impatient)
- Currency reverts 12 months later (missed it)

**Why it fails:**

- Mean reversion takes 2-5 years (half-life)
- Short-term noise dominates
- Transaction costs erode frequent trading
- Psychology: Can't hold losers long enough

**Fix:**

- Minimum 18-month horizon for G10
- Accept interim mark-to-market losses
- Size small enough to hold comfortably (1-2% risk)
- Don't check daily P&L (reduces anxiety)

### 3. Over-Leveraging


**The mistake:**

- "Value trade = low risk, mean reversion certain"
- Use 10x leverage
- Small adverse move wipes out
- Forced exit before reversion occurs

**Why it fails:**

- Currencies can stay mispriced for years
- Volatility underestimated
- Margin calls force exits
- Even "safe" trades have 20% drawdowns

**Fix:**

- Max 3x leverage for value trades
- Conservative: 1-2x (sleep better)
- Size for worst-case: -25% move without margin call
- Test: Can you hold this for 3 years?

### 4. Ignoring Carry


**The mistake:**

- Long JPY (undervalued) vs. USD (overvalued)
- Pay 5% carry annually
- Mean reversion takes 3 years
- Carry cost: -15% cumulative
- Need JPY to strengthen 15% just to breakeven

**Why it fails:**

- Carry costs compound
- Offsetting required appreciation
- Better alternatives exist (undervalued + positive carry)

**Fix:**

- Calculate breakeven: Value gap - Carry cost
- Prefer undervalued currencies with positive carry
- If negative carry > 3%, pass (unless extreme value)
- Use options to avoid carry bleeding

---

## Risk Management Rules


### 1. Position Limits


**Maximum exposure:**

$$
\text{Max Position} = \frac{\text{Portfolio} \times 0.05}{\text{Expected Annual Vol}}
$$

**Example:**

- $1M portfolio
- 5% max risk
- USD/JPY vol: 8%
- Max: $50K / 0.08 = **$625K notional (62%)**

**Practical limits:**

- Single position: Max 3% portfolio risk
- Total value book: Max 15% risk
- G10 only: Max 5x leverage
- Including EM: Max 3x leverage

### 2. Diversification


**Spread across:**

**Geographic:**

- Europe: EUR, GBP, CHF
- Americas: USD, CAD, BRL, MXN
- Asia: JPY, AUD, SGD
- No more than 40% in one region

**Value source:**

- PPP-based: 40%
- REER-based: 30%
- TOT-based: 20%
- Carry-adjusted: 10%

**Long/short balance:**

- 50% long undervalued
- 50% short overvalued
- Dollar-neutral (no directional USD bet)

### 3. Monitoring Framework


**Daily:**

- Major central bank announcements
- Geopolitical events (wars, elections)
- Extreme moves (> 2% daily)
- VIX level (crisis indicator)

**Weekly:**

- P&L review
- Check REER updates
- Commodity price moves (TOT)
- Implied volatility levels

**Quarterly:**

- Full revaluation of all positions
- Update PPP estimates
- Recalculate value gaps
- Rebalance to targets
- Review structural factors

### 4. Exit Discipline


**Planned exits:**

**Take profit when:**

- REER returns to 50th percentile (fair value)
- Value gap closes > 75%
- Time target reached (2-3 years)
- Better opportunity identified (rebalance)

**Stop loss when:**

- Loss exceeds -15% (hard stop)
- Structural break identified (policy shift)
- Vol regime changes (VIX > 35, crisis)
- Central bank intervention announced
- Thesis invalidated (fundamentals changed)

---

## Real-World Examples


### 1. EUR/CHF (2011-2015)


**Setup:**

- CHF massively overvalued (REER 115)
- Safe-haven flows during Eurozone crisis
- SNB imposed 1.20 floor Sept 2011
- Classic value trade: Short CHF

**Trade (theoretical, without SNB knowledge):**

- Short CHF/EUR at 1.20
- Value target: 1.35 (+12.5%)
- Time horizon: 3 years

**Reality:**

- SNB defended 1.20 for 4 years
- Value traders lost on carry (negative)
- Jan 2015: SNB abandoned peg
- CHF surged to 1.05 instantly (-13%)
- **Lesson: Central banks can maintain mispricing indefinitely**

**Outcome for traders:**

- Those who exited early: Small loss
- Those who held: Catastrophic loss
- Those who shorted AFTER SNB exit: Won big (CHF did eventually normalize)

### 2. GBP Brexit (2016-2018)


**Setup:**

- June 2016: Brexit vote, GBP crashes
- GBP/USD: 1.50 → 1.20 (-20%)
- REER fell to 10th percentile
- UK economy fundamentally unchanged

**Trade:** Long GBP (undervalued)

- Entry: 1.22 (July 2016)
- REER: 85 (deeply undervalued)
- Time horizon: 24 months
- Target: 1.35 (+10%)

**Outcome:**

- GBP recovered to 1.42 by April 2018 (+16%)
- Took 22 months
- Drawdown: -8% (fell to 1.15 briefly in Oct 2016)
- **Result: +16% gain over 2 years (8% annually)**

**Lesson:** Panic overshoots create value. Patience wins.

### 3. AUD Terms of Trade (2020-2022)


**Setup:**

- COVID crash: AUD at 0.55 (March 2020)
- Iron ore prices recovering ($60 → $120)
- China stimulus boosting demand
- Australia TOT improving rapidly

**Trade:** Long AUD/USD

- Entry: 0.62 (June 2020)
- Rationale: TOT + value (REER low)
- Time: 18 months
- Target: 0.75

**Outcome:**

- AUD rallied to 0.80 (Feb 2022)
- Gain: +29% over 20 months
- Carry: +1.5% (positive add-on)
- **Total: +30.5%**

**Lesson:** TOT + value + carry = trifecta. All factors aligned.

### 4. JPY Undervaluation (2012-2024)


**Setup:**

- JPY persistently undervalued (Big Mac Index: -45%)
- REER at 75 (30-year low)
- Abenomics policy: Weak yen deliberate
- Value traders kept betting on reversion

**Trade (repeated by many):**

- Long JPY vs. USD
- Entry: Various (110, 120, 140)
- Rationale: "Mean reversion inevitable"

**Outcome (as of 2024):**

- USD/JPY went from 80 (2012) → 150 (2024)
- Value traders lost for 12 years
- Negative carry compounded losses
- **Total: -50-70% losses**

**Lesson:**

- Structural change (demographics, YCC) created new equilibrium
- Old fair value obsolete
- Fighting BOJ policy = suicide
- Sometimes "value" is a value trap

---

## Practical Steps


**Step-by-step implementation:**

### 1. Build Valuation Dashboard


**Spreadsheet setup:**

**Columns:**

| Currency | Current | REER | Percentile | Big Mac Gap | TOT Trend | Value Score |
|----------|---------|------|------------|-------------|-----------|-------------|
| EUR/USD | 1.08 | 102 | 65% | +5% | Neutral | 0 |
| USD/JPY | 148 | 75 | 8% | -45% | Negative | +8 |
| AUD/USD | 0.67 | 92 | 35% | -12% | Positive | +3 |
| GBP/USD | 1.27 | 98 | 45% | -8% | Neutral | +1 |

**Value score formula:**

$$
\text{Score} = \frac{|\text{REER Deviation}| + |\text{PPP Gap}|}{2} \times \text{TOT Multiplier}
$$

**Interpretation:**

- Score > 5: Strong value trade
- Score 3-5: Moderate value
- Score < 3: No clear value

### 2. Screen for Opportunities


**Filtering process:**

**Step 1: Identify extremes**

- REER < 15th or > 85th percentile
- PPP gap > 15% or < -15%
- Creates 5-8 candidates typically

**Step 2: Check structural factors**

- Recent policy changes? (disqualify)
- Geopolitical crisis? (wait)
- Productivity trends? (adjust fair value)
- Demographics? (adjust fair value)

**Step 3: Rank by carry-adjusted value**

- Calculate: Value Gap + Annual Carry
- Higher = better risk/reward
- Top 3-5 become positions

### 3. Position Sizing


**For each trade:**

**Calculate position:**

$$
\text{Contracts} = \frac{\text{Portfolio} \times 0.02}{\text{Annual Vol} \times \text{Contract Size}}
$$

**Example (Long AUD/USD):**

- Portfolio: $500K
- Risk: 2% = $10K
- AUD/USD annual vol: 10%
- Contract: 100K AUD

**Position:**

$$
\frac{10,000}{0.10 \times 100,000} = 1 \text{ contract (10% portfolio)}
$$

### 4. Entry Execution


**Best practices:**

**Timing:**

- Don't chase breakouts
- Enter on pullbacks (5-10% from extreme)
- Use limit orders (save 10-20 pips)
- Avoid month-end (distortions)

**Scaling in:**

- Week 1: 40% of target size
- Week 3: Additional 30% (if thesis intact)
- Week 6: Final 30%
- Allows averaging if wrong initially

### 5. Monitoring and Rebalancing


**Quarterly review process:**

**For each position:**

1. Update REER and PPP data
2. Recalculate value gap
3. Check if thesis still valid
4. Assess carry impact (cumulative)
5. Decide: Hold, Add, Trim, or Exit

**Exit triggers:**

- Value gap closed > 75%
- REER crossed 50th percentile
- Structural break identified
- Loss > -15% (stop loss)
- Time limit: 3 years maximum

**Rebalancing:**

- Trim winners by 50% when profit > 20%
- Add to losers by 25% if down < 10% and thesis intact
- Exit losers if down > 15% or thesis broken
- Redeploy capital to better opportunities

---

## Final Wisdom


> "Value and PPP reversion is the most intellectually satisfying FX strategy—grounded in fundamental theory, statistically validated, and logically coherent. But it's also the hardest to execute: mean reversion takes years, carry bleeds, and behavioral discipline is tested repeatedly. Most traders give up before reversion occurs, or over-leverage and get stopped out. The secret is patience, conservative sizing, and constant vigilance for structural breaks. When it works, it's like watching gravity reassert itself. When it fails, it's because the world changed beneath you."

**Key success factors:**

- Extreme misalignment (> 20% value gap)
- Multiple metrics confirming (REER + PPP + TOT)
- Patient capital (2-3 year horizon minimum)
- Conservative sizing (1-2% risk per trade)
- Carry-adjusted analysis (prefer positive carry)
- Quarterly review for structural breaks (demographics, policy)
- Diversification (10+ positions across regions)
- Discipline (cut losers at -15%, take profits at fair value)
