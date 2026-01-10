# Hedging Exotics (Smile and Skew)

**Hedging exotic options with volatility smile and skew** requires managing multidimensional Greeks (vanna, volga, vega) that interact with the non-flat implied volatility surface, where standard Black-Scholes delta hedging fails because option values depend not just on spot movement but on how the entire volatility surface shifts dynamically with market moves, creating path-dependent hedge ratios and requiring sophisticated cross-gamma adjustments.

---

## The Core Insight

**The fundamental idea:**

- Black-Scholes assumes flat volatility (one σ for all strikes/tenors)
- Reality: Volatility surface has smile (U-shape) and skew (tilt)
- Exotic options extremely sensitive to surface shape
- Vanilla hedges insufficient (miss surface risk)
- Need to hedge both spot (delta) AND surface (vanna/volga)
- Surface dynamics create non-linear risks
- Cross-Greeks dominate in exotics

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/volatility_surface_exotics_risk.png?raw=true" alt="volatility_surface_exotics_risk" width="700">
</p>
**Figure 1:** Volatility surface showing smile (ATM dip, OTM wings) and skew (put skew steeper than call) with exotic option exposure mapped across strikes and tenors, demonstrating how barrier, digital, and variance options have concentrated vega along specific surface regions requiring targeted hedging.

**You're essentially asking: "How do I hedge when my option's value depends on the shape of the volatility smile, not just one volatility number?"**

---

## What Is Smile/Skew Risk?

### 1. Surface vs. Flat Vol

**Black-Scholes world:**

One volatility: $\sigma = 25\%$ for all strikes and maturities

**Option value:**
$$
V = V(S, K, T, r, q, \sigma)
$$

**Hedge:** Delta-hedge with underlying, rebalance based on gamma

---

**Real world:**

Implied volatility surface: $\sigma(K, T)$

**Option value:**
$$
V = V(S, K, T, r, q, \sigma(K,T))
$$

**Hedge:** Need to hedge:
- Delta: Spot exposure
- Vega: Parallel vol shift
- Vanna: Vol sensitivity to spot moves
- Volga: Vol convexity

### 2. Smile Definition

**Volatility smile:**

$$
\sigma(K) \approx \sigma_{\text{ATM}} + a_2(K - S_0)^2 + a_4(K - S_0)^4 + ...
$$

**Typical equity smile:**
- ATM: 20% vol
- 90% strike: 28% vol (put wing)
- 110% strike: 22% vol (call wing)
- **U-shaped curve**

**Why exists:**
- Crash fears (fat left tail)
- Supply/demand (hedging pressure)
- Leverage effect (volatility increases as stock falls)
- Jump risk

### 3. Skew Definition

**Volatility skew:**

$$
\sigma(K) \approx \sigma_{\text{ATM}} + \beta(K - S_0)
$$

**Typical equity skew:**
- Negative skew: OTM puts more expensive than OTM calls
- Slope: $\beta \approx -0.15$ for equities
- Example: 90% strike at 28%, 110% strike at 16%

**Skew vs. Smile:**
- Skew: Linear tilt (first-order)
- Smile: Curvature (second-order)
- Reality: Both present (smile + skew)

### 4. Sticky Dynamics

**How does surface move with spot?**

**Sticky strike:**
- Implied vol at each strike stays constant
- $\sigma(K) = \text{constant}$
- If spot moves, ATM vol changes

**Sticky delta:**
- Implied vol at each delta stays constant
- 25-delta put always has same vol
- Surface shifts parallel with spot

**Sticky moneyness:**
- Implied vol at each $K/S$ ratio constant
- $\sigma(K/S_0) = \text{constant}$
- Surface scales with spot

**Example:**

Stock at $100, 90% strike at 28% vol

**Sticky strike:** Stock moves to $110 → 90% strike still 28%
**Sticky delta:** Stock moves to $110 → New 25-delta put (at $99) is 28%
**Sticky moneyness:** Stock moves to $110 → 99% strike (90% of new spot) is 28%

**Reality:** Mix of all three, depends on market regime

### 5. Vanna

**Cross-Greek definition:**

$$
\text{Vanna} = \frac{\partial^2 V}{\partial S \partial \sigma} = \frac{\partial \Delta}{\partial \sigma} = \frac{\partial \nu}{\partial S}
$$

**Economic meaning:**
- How delta changes when volatility changes
- Or: How vega changes when spot changes
- Critical for smile hedging

**Example:**

OTM call with positive vanna:
- If spot rises AND vol rises → Delta increases more than expected
- If spot falls AND vol falls → Delta decreases more than expected

**Sign:**
- ATM options: Vanna ≈ 0
- OTM options: Positive vanna (typically)
- ITM options: Negative vanna (typically)

### 6. Volga (Vomma)

**Volatility convexity:**

$$
\text{Volga} = \frac{\partial^2 V}{\partial \sigma^2} = \frac{\partial \nu}{\partial \sigma}
$$

**Economic meaning:**
- Convexity of option value to volatility
- Like gamma but for vol instead of spot
- Captures smile curvature

**Example:**

Long straddle with positive volga:
- Vol increases from 20% to 30% → Vega increases (captures more of move)
- Vol decreases from 20% to 10% → Vega decreases (loses less)
- **Benefits from vol-of-vol**

**Sign:**
- Long options: Positive volga (benefit from smile)
- Short options: Negative volga (hurt by smile)

### 7. Term Structure

**Volatility across maturities:**

$$
\sigma(T) = \text{Vol term structure}
$$

**Typical patterns:**

**Contango:** Short-term vol < Long-term vol
**Backwardation:** Short-term vol > Long-term vol

**Example:**

VIX term structure:
- 1-month: 25%
- 3-month: 22%
- 6-month: 20%
- 12-month: 19%

**Exotic risk:**
- Calendar spread sensitive to term structure
- Barrier options very sensitive to short-term vol
- Variance swaps sensitive to entire term structure

---

## Key Terminology

**Implied Volatility:**
- Market's expectation of future volatility
- Backed out from option prices
- Different for each strike and maturity
- The "surface" we hedge

**Vanna:**
- Cross-derivative: $\frac{\partial \Delta}{\partial \sigma}$
- Delta sensitivity to vol changes
- Zero at-the-money
- Key for smile hedging

**Volga:**
- Second derivative: $\frac{\partial^2 V}{\partial \sigma^2}$
- Vega convexity
- Always positive for long options
- Captures smile curvature

**Sticky Strike:**
- Vol at each strike constant as spot moves
- Extreme assumption
- Rare in practice
- Conservative for delta hedging

**Sticky Delta:**
- Vol at each delta constant as spot moves
- More realistic for equities
- Surface moves parallel
- Standard for FX markets

**25-Delta Strangle:**
- Spread between 25-delta put and call vols
- Measure of smile width
- Quoted in FX markets
- Key risk metric

---

## Smile Hedging Strategies

### 1. Vanna Hedging

**Problem:** Exotic has large vanna exposure

**Example:** Barrier option near barrier

**Position:** Long down-and-out call
- Barrier: $90
- Current: $95
- Vanna: -1,000 (negative, large)

**Risk:** If spot falls and vol rises (typical), delta drops faster than expected

**Hedge:**
1. Calculate vanna exposure: -1,000
2. Find vanilla with opposite vanna
3. Trade vanilla to neutralize

**Implementation:**

Buy OTM put with positive vanna of +1,000
- Strike around 25-delta
- Vanna typically positive
- Adjust quantity to match

**Result:** Vanna-neutral portfolio

**Monitoring:**
- Vanna changes with spot and vol
- Rehedge when |Vanna| > threshold
- Typically monthly or after big moves

### 2. Volga Hedging

**Problem:** Exotic sensitive to smile shape

**Example:** Long digital option

**Position:** Digital call at strike $K$
- High volga near expiration
- Loses if smile steepens

**Risk:** If vol increases with steeper smile, loses more than simple vega suggests

**Hedge:**

Create opposite volga exposure using vanilla options:

$$
\text{Volga hedge} = \frac{\text{Volga}_{\text{exotic}}}{\text{Volga}_{\text{vanilla}}}
$$

**Implementation:**

Exotic volga: -5,000 (negative)
ATM straddle volga: +200 per straddle

**Hedge:** Sell 25 straddles
- Creates volga of -5,000
- Neutralizes exotic volga

**Cost:** Now have vega exposure from straddles (need to hedge separately)

### 3. Butterfly Hedging

**Smile hedging using butterflies:**

**Idea:** Butterfly = pure volga without vega

**Structure:**
- Buy 1 call at $K - \Delta$
- Sell 2 calls at $K$
- Buy 1 call at $K + \Delta$

**Payoff:** Peaks at $K$, zero far from $K$

**Greeks:**
- Vega ≈ 0 (for small $\Delta$)
- Volga ≠ 0 (sensitive to smile curvature)
- **Pure smile exposure**

**Usage:**

To hedge exotic with volga but not vega:
1. Calculate required volga
2. Trade butterflies (not straddles)
3. Maintain vega-neutral

**Example:**

Need volga of +10,000

**Butterfly:** ATM butterfly gives +500 volga
**Hedge:** Buy 20 butterflies

**Result:** 
- Volga: +10,000 ✓
- Vega: ≈ 0 ✓
- Clean smile hedge

### 4. Risk Reversal Hedging

**Skew hedging:**

**Structure:** Buy call, sell put (or vice versa)

**Greeks:**
- Delta ≠ 0 (directional)
- Vega ≈ 0 (if ATM)
- Vanna ≠ 0 (sensitive to skew)

**Usage:**

To hedge skew risk (first-order vol surface):

**Example:**

Exotic with negative vanna: -5,000

**Hedge:** Buy risk reversal (long call, short put)
- Generates positive vanna
- Adjust strikes to match vanna
- Typically 25-delta

**Result:** Vanna-neutral

**Market standard:** Quoted as "25-delta risk reversal"
- FX markets: Key skew indicator
- Equity markets: Less standardized

### 5. Calendar Spread

**Term structure hedging:**

**Problem:** Exotic sensitive to vol term structure

**Example:** Long-dated variance swap

**Position:** 1-year variance swap
- Exposed to entire term structure
- Needs multiple tenor hedges

**Hedge:** Calendar spread
- Buy 3-month ATM straddle
- Sell 1-month ATM straddle
- Net exposure to 1-3 month term structure

**Result:** Isolate and hedge specific tenor segments

**Monitoring:**
- Term structure shape changes
- Roll hedges as time passes
- Adjust ratios based on vega distribution

### 6. Dispersion Trading

**Correlation hedging:**

**Structure:**
- Long variance on components (high vega)
- Short variance on index (high vega)
- Net: Correlation exposure

**Smile interaction:**
- Index smile different from component smiles
- Correlation affects surface dynamics
- Complex vanna/volga interactions

**Exotic example:** Worst-of basket option

**Hedge:**
1. Delta-hedge each component
2. Vega-hedge using component options
3. Dispersion overlay for correlation

**Result:** Comprehensive smile hedge

### 7. Dynamic Adjustment

**Vanna-volga approach:**

**Formula:**

$$
V_{\text{exotic}} \approx V_{\text{BS}} + \text{Vanna correction} + \text{Volga correction}
$$

**Corrections:**

$$
\text{Vanna correction} = \frac{\text{Vanna}_{\text{exotic}}}{\text{Vanna}_{\text{vanilla}}} \times (V_{\text{mkt}} - V_{\text{BS}})
$$

**Implementation:**

1. Price exotic in BS world
2. Calculate vanna/volga sensitivities
3. Adjust for market smile using vanilla options
4. Rehedge when adjustments change

**Standard in FX exotics:** Very common for barrier options

---

## Exotic-Specific Hedging

### 1. Barrier Options

**Challenges:**

- High vanna near barrier
- Gamma explosion approaching barrier
- Vol skew directly impacts probability of knockout

**Example:** Down-and-out call, barrier $90$, spot $95$

**Greeks near barrier:**
- Delta: 1.5 (exploding)
- Vanna: -2,000 (huge negative)
- Gamma: 5.0 (10× normal)

**Hedge approach:**

1. **Far from barrier ($S > 100$):**
   - Standard delta hedge
   - Light vanna hedge (25-delta put)

2. **Approaching barrier ($95 < S < 100$):**
   - Delta + vanna hedge
   - Buy OTM puts for vanna
   - Monitor smile dynamics

3. **Very close ($S < 97$):**
   - EXIT POSITION
   - Unhedgeable gamma/vanna
   - Accept small loss to avoid disaster

**Smile impact:**

Steeper skew → Higher knockout probability
- OTM put vol increases
- Barrier becomes "closer" in vol space
- Need more protection

### 2. Digital Options

**Challenges:**

- Infinite gamma at strike at expiration
- Extreme vanna sensitivity near strike
- Smile determines payout probability

**Example:** Digital call, strike $100$, spot $100.50$

**Greeks at expiration:**
- Gamma → ∞ (discontinuous)
- Vanna: -∞ or +∞ depending on side
- Unhedgeable conventionally

**Hedge approach:**

**Use spreads to approximate:**

Replace digital with tight call spread:
- Buy call at $100
- Sell call at $100.10
- Creates manageable gamma
- Sacrifice perfect payoff for hedgeability

**Smile adjustment:**

Price using skew:
- Don't use ATM vol
- Use vol at strike $100 (from smile)
- Affects payout probability

**Exit discipline:**

1 week before expiration: EXIT if near strike

### 3. Variance Swaps

**Challenges:**

- Exposed to entire vol surface
- Convexity in realized variance
- Smile affects hedging portfolio

**Position:** Long variance swap

**Exposure:**
- Vega across all strikes (weighted by $1/K^2$)
- More weight on OTM options
- Sensitive to smile wings

**Hedge using options:**

Variance swap replication:

$$
\text{Variance} \approx \frac{2}{T} \left[ \int_0^F \frac{P(K)}{K^2} dK + \int_F^\infty \frac{C(K)}{K^2} dK \right]
$$

**Implementation:**

1. Buy OTM puts (below forward)
2. Buy OTM calls (above forward)
3. Weight each by $1/K^2$
4. Dynamic rebalancing

**Smile impact:**

Steep smile → High variance swap value
- Wings are expensive
- Replication costly
- Creates basis risk

### 4. Asian Options

**Challenges:**

- Lower vega than vanilla (averaging reduces vol)
- Different smile sensitivity (average has lower vol)
- Path-dependent vanna

**Example:** Asian call, 1-year daily average

**Effective volatility:**

$$
\sigma_{\text{Asian}} = \frac{\sigma_{\text{spot}}}{\sqrt{3}} \approx 0.577 \sigma_{\text{spot}}
$$

**Hedge approach:**

1. **Calculate effective vega:**
   - Asian vega ≈ 60% of vanilla vega

2. **Smile adjustment:**
   - Use lower vol in smile (effective vol)
   - Typically ATM vol (averaging is near-ATM)

3. **Dynamic rebalancing:**
   - As average accumulates, vega decreases
   - Reduce hedge notional over time

**Smile impact:**

Less sensitive than vanilla:
- Averaging smooths extreme moves
- Smile wings less important
- Focus on ATM smile

### 5. Autocallables

**Challenges:**

- Multiple observation dates (vega at each)
- Barrier feature (vanna near barrier)
- Early termination affects surface exposure

**Example:** 3-year autocallable, quarterly observations

**Exposure:**

- Vega concentrated near current spot
- Shifts as spot moves and time passes
- Multiple barrier levels (if step-down)

**Hedge approach:**

1. **Decompose into vanilla portfolio:**
   - Each observation = digital option
   - Approximate with tight spreads
   - Creates manageable Greeks

2. **Vanna from barrier:**
   - Hedge with 25-delta options
   - Adjust as approach observation dates

3. **Term structure:**
   - Hedge each observation independently
   - Use appropriate tenor for each

**Smile impact:**

Very sensitive:
- Autocall probability depends on ATM vol
- Barrier probability depends on wing vol
- Need full smile hedge

### 6. Cliquet Options

**Challenges:**

- Forward-start structure
- Resets create new vega at each reset
- Sensitive to forward volatility

**Position:** Cliquet with annual resets

**Exposure:**

- Vega to forward vols: $\sigma_{T_1 \to T_2}$, $\sigma_{T_2 \to T_3}$, etc.
- Each reset creates new ATM option
- Sensitive to term structure

**Hedge approach:**

1. **Calendar spreads:**
   - Hedge each reset date separately
   - Match forward vol exposure

2. **Smile risk:**
   - Each reset will be ATM (by definition)
   - Hedge with ATM vol only
   - Wings less important

**Forward vol hedging:**

$$
\sigma_{T_1 \to T_2}^2 = \frac{T_2 \sigma_{T_2}^2 - T_1 \sigma_{T_1}^2}{T_2 - T_1}
$$

Trade options at $T_1$ and $T_2$ to create forward exposure

### 7. Worst-Of Options

**Challenges:**

- Multi-asset smile interactions
- Correlation affects smile shape
- Vanna on worst performer (path-dependent)

**Example:** Worst-of call on 3 stocks

**Exposure:**

- Vega to each asset's smile
- Vanna depends on which is worst
- Correlation shifts weight between assets

**Hedge approach:**

1. **Individual smiles:**
   - Hedge each asset's smile independently
   - Use single-stock options

2. **Correlation overlay:**
   - Trade dispersion (index vs. components)
   - Adjust weights dynamically

3. **Dynamic winner selection:**
   - Vanna concentrated on current worst
   - Shift hedges as worst changes

**Smile interaction:**

Complex:
- Steep skew on one asset → More likely to be worst
- Changes probability distribution
- Requires correlation-adjusted hedging

---

## Common Mistakes

### 1. Ignoring Vanna

**Flat vol assumption:**

- **Mistake:** Delta-hedge exotic assuming flat vol
- **Why it fails:** Spot moves change vol (smile effect)
- **Fix:** Explicitly hedge vanna with OTM options
- **Real cost:** Delta hedge breaks down at critical moments

**Example:**

Long down-and-out call, barrier $90$, spot $100$

**Delta hedge only:**
- Hedged with stock
- Stock falls to $95
- Vol rises from 20% → 30% (typical crash behavior)
- Delta change: -0.3 (stock) + vanna effect: -0.2
- **Total delta: -0.5** vs. expected -0.3
- Unhedged: -0.2 delta exposure
- On $10M notional: **$500K unexpected loss**

### 2. Wrong Sticky Assumption

**Sticky strike vs. sticky delta:**

- **Mistake:** Use sticky strike when market is sticky delta
- **Why it fails:** Surface moves differently than assumed
- **Fix:** Calibrate to market smile dynamics
- **Real cost:** 10-20% P&L error

**Example:**

Hedging barrier option

**Your assumption:** Sticky strike
- Spot $100 → $110$
- You assume 90% strike still at 28% vol
- Price barrier using 28%

**Reality:** Sticky delta (FX market)
- 90% of $110 = $99$ should be at 28% vol
- But 90% of $100 = $90$ is now cheaper vol (maybe 24%)
- You overestimated knockout probability
- **Overhedged: 15% too much protection**

### 3. Static Hedge

**Set-and-forget:**

- **Mistake:** Hedge smile risk once and don't update
- **Why it fails:** Vanna/volga change with spot, vol, time
- **Fix:** Rehedge monthly or after 5% move/5 vol points
- **Real cost:** Hedge degrades over time

**Example:**

Month 1: Hedge vanna with OTM puts (vanna = -1,000)

**Month 3:**
- Spot moved 10%
- Vol changed 10 points
- Vanna now = -2,500 (changed!)
- But hedge still for -1,000
- **Unhedged vanna: -1,500**

**Event:** Spot drops 5%, vol rises 5 points
- Unhedged vanna impact: -1,500 × 5% × 5 vol = -$37,500 loss

### 4. Butterfly Mispricing

**Ignoring bid-ask:**

- **Mistake:** Trade many butterflies without considering spreads
- **Why it fails:** Butterfly spreads are wide (4 legs)
- **Fix:** Use liquid strikes only
- **Real cost:** 20-30% of theoretical hedge cost

**Example:**

Need to hedge volga using butterflies

**Theoretical:**
- 20 butterflies @ mid price
- Cost: $100K

**Reality:**
- Bid-ask spread: 15% on each butterfly
- Actual cost: $115K
- **Extra cost: $15K (15% more)**

**Solution:** Use fewer, more liquid strikes (even if imperfect hedge)

### 5. Over-Hedging Tail

**Excessive wing hedging:**

- **Mistake:** Hedge far OTM exposures too precisely
- **Why it fails:** Wings are illiquid, expensive, rarely matter
- **Fix:** Accept some tail risk, focus on near-ATM
- **Real cost:** Overpay for protection that rarely activates

**Example:**

Exotic with vega spread across strikes:
- 80% strike: 100 vega
- 90% strike: 500 vega
- 100% strike: 1,000 vega (ATM)
- 110% strike: 400 vega
- 120% strike: 50 vega

**Over-hedging:** Hedge all five strikes precisely
- Cost: $150K
- 80% and 120% strikes rarely matter

**Smart approach:** Hedge 90-110 strikes only
- Cost: $120K
- **Savings: $30K (20%)**
- Accept small tail risk

### 6. Correlation Ignorance

**Multi-asset smile:**

- **Mistake:** Hedge each asset independently, ignore correlation
- **Why it fails:** Correlation affects which asset dominates
- **Fix:** Use dispersion trades to hedge correlation
- **Real cost:** Wrong asset gets hedged heavily

**Example:**

Worst-of option on AAPL and MSFT

**Independent hedging:**
- Hedge 50% AAPL smile, 50% MSFT smile

**Correlation spike (crisis):**
- Both fall together
- Need 100% hedge on worst (AAPL in this case)
- Only have 50%
- **Underhedged: 50% of needed protection**

---

## Best vs. Worst Case

### 1. Best Case: Success

**Perfect smile hedge:**

**Setup:**
- Market maker selling barrier options to clients
- Sophisticated smile hedging program
- Proper risk limits and monitoring

**Position:** Short 1,000 down-and-out calls
- Notional: $100M
- Barrier: $90 (10% below $100)
- Premium collected: $3M

**Greeks:**
- Delta: -50,000 shares
- Vanna: +20,000 (positive, large)
- Volga: +5,000
- Vega: -100,000 (short vol)

**Hedge program:**

**Week 1: Initial hedge**
1. Buy 50,000 shares (delta-neutral)
2. Buy $2M of OTM puts (vanna hedge)
3. Sell $500K ATM straddles (vega hedge)
4. Net cost: $500K

**Month 1-2: Stable market**
- Stock: $98-$102
- Vol: 20-22%
- Small adjustments only
- Theta decay collecting: $100K/month

**Month 3: Market correction**
- Stock drops: $100 → $92 (8%)
- Vol spikes: 20% → 35%

**Unhedged impact:**
- Delta loss: 50,000 × $8 = $400K
- Vanna impact: Would be +$700K loss (spot down + vol up)

**With hedge:**
- Stock hedge: Break even on delta
- OTM puts: Profit $900K (now ITM)
- Vanna: Neutralized by puts
- **Net: +$900K profit** (put gains exceed loss)

**Maturity:**
- All options expired OTM (barrier not hit)
- Total P&L: Premium $3M + Hedge profits $900K - Hedge costs $500K = **+$3.4M**
- **Return: 113% on initial hedge cost**

**Success factors:**
1. Proper vanna hedge (OTM puts)
2. Dynamic rebalancing
3. Exited when close to barrier
4. Didn't over-hedge (accepted some risk)

### 2. Worst Case: Disaster

**Smile risk ignored:**

**Setup:**
- Prop desk selling digital options
- "Easy money" from high premiums
- Only delta-hedging (ignoring smile)

**Position:** Short 10,000 digital calls
- Strike: $100
- Notional: $10 per share
- Premium collected: $4.50/share = $4.5M
- Expiration: 3 months

**Greeks (at inception):**
- Delta: -5,000 shares (hedged with stock)
- Vanna: -50,000 (huge negative, ignored)
- Volga: -20,000 (negative, ignored)

**Month 1: Calm**
- Stock: $95-$105
- Vol: 20%
- Delta-hedge working fine
- Theta collecting: $50K/day

**Month 2: Approaching strike**
- Stock drifts to $100.50
- Vol still 20%
- Getting close to strike

**Week before expiration: Disaster**

**Monday:** Stock at $100.10, vol at 22%
- Vanna kicks in
- Delta should be 0.52 (near ATM digital)
- But vol increased → Effective delta 0.62 (vanna effect)
- Underhedged by 1,000 shares per contract × 10,000 contracts
- **Underhedged: $1M delta exposure**

**Wednesday:** Stock at $99.90, vol at 25%
- Crossed strike! (now OTM)
- Delta should be 0.48
- But vol increased more → Effective delta 0.35 (vanna)
- Now overhedged
- Had to sell $1.7M stock

**Friday expiration:** Stock at $99.98 (just OTM)
- Vol at 30% (continued rise)
- Digitals expire worthless ✓
- But hedging whipsaw cost money

**Final P&L:**
- Premium collected: +$4.5M
- Stock hedge losses: -$2.2M (from whipsaw near strike)
- **Vanna/volga unhedged losses: -$3.8M**
- **Net: -$1.5M** (33% loss despite options expiring worthless!)

**Post-mortem:**
1. Ignored vanna (biggest mistake)
2. Held through expiration near strike (unhedgeable)
3. No smile hedging whatsoever
4. Excessive position size
5. Desk shut down, traders fired

---

## Risk Management Rules

### 1. Vanna Limits

**Maximum unhedged vanna:**

$$
|\text{Vanna}_{\text{unhedged}}| \leq 1\% \text{ of Delta}
$$

**Example:**

Delta: 10,000 shares

**Maximum vanna:** 100 (1% of 10,000)

**If exceeded:** Trade OTM options to neutralize

### 2. Volga Limits

**Maximum unhedged volga:**

$$
|\text{Volga}_{\text{unhedged}}| \leq 2\% \text{ of Vega}
$$

**Example:**

Vega: $50,000 per 1% vol

**Maximum volga:** $1,000 (2% of $50K)

**If exceeded:** Trade straddles or butterflies

### 3. Rehedge Triggers

**Smile hedge rebalancing:**

1. **Time-based:** Every month minimum
2. **Move-based:** After 5% spot move
3. **Vol-based:** After 5 vol point move
4. **Event-based:** After earnings, news, etc.

**Exception:** Exit instead of rehedge if near barriers

### 4. Position Limits

**Exotic notional limits:**

$$
\text{Exotic Notional} \leq 5 \times \text{Vanilla Equivalent}
$$

**Example:**

Comfortable with $100M vanilla options

**Maximum exotics:** $500M notional

**Rationale:** Higher leverage, more complex Greeks

### 5. Smile Stress Tests

**Required scenarios:**

1. **Parallel shift:** ±10 vol points
2. **Smile steepening:** Skew doubles
3. **Smile flattening:** Skew halves
4. **Vol-of-vol:** 50% increase in volga
5. **Correlation shock:** ±30% correlation change

**Maximum loss in any scenario:**

$$
\text{Scenario Loss} \leq 20\% \text{ of Position Capital}
$$

### 6. Exit Discipline

**Mandatory exits:**

**For barriers:**
- Exit if within 10% of barrier
- Never hold through barrier approach

**For digitals:**
- Exit 1 week before expiration if near strike
- Or use spreads instead of true digitals

**For exotics:**
- Exit if unhedged vanna/volga exceeds 2× limit

### 7. Documentation

**Required records:**

- Vanna/volga at trade inception
- Hedge portfolio and rationale
- Rehedge dates and triggers
- P&L attribution (delta, vanna, volga, theta)
- Smile assumptions (sticky?)
- Stress test results

---

## Real-World Examples

### 1. 2008 Crisis Vol Spike

**FX barrier options:**

**Setup:**
- Bank sold EUR/USD knock-out options
- Pre-crisis: Vol at 8-10%
- Standard delta hedging only

**Crisis:**
- EUR/USD vol spiked to 25-30%
- 3× increase in vol
- Barriers that seemed safe (15% away) suddenly close (5% away in vol space)

**Vanna impact:**
- Spot moved + vol moved = huge vanna P&L
- Banks had large negative vanna (barrier sellers)
- Losses: Billions industry-wide

**Lesson:** Vanna matters most in crisis (when spot and vol move together)

### 2. Oil Digitals (2014-2016)

**Oil binary options:**

**Structure:**
- Popular retail product
- Digital options on oil price
- Strike: "Will oil close above $80?"

**Setup (mid-2014):**
- Oil at $100
- $80 strike seemed safe (20% below)
- Vol: 20%

**Collapse:**
- Oil crashed from $100 → $30 (70% drop)
- Vol spiked to 50%
- Smile became extremely steep

**Smile impact:**
- OTM put vols at 60-70%
- Changed probability estimates drastically
- Digitals that were "90% safe" became "50-50"

**Losses:** Many retail investors lost on what they thought were "sure bets"

### 3. Variance Swap Blow-Up

**Volatility arbitrage fund (2015):**

**Strategy:**
- Long variance swaps (betting on higher vol)
- Short variance swaps in different tenors
- "Term structure arbitrage"

**Smile dependence:**
- Variance swaps replicated using options
- Smile changes affected replication cost
- Basis risk between swap and replication

**Market dislocation:**
- VIX spike in August 2015
- Smile wings widened dramatically
- Replication portfolio much more expensive
- **Basis blew out: 5 vol points**

**Fund losses:**
- Lost on the basis (swap vs. replication)
- Down 40% in one month
- Forced to liquidate

### 4. FX Vanna Success (Ongoing)

**FX options desk:**

**Approach:**
- Systematic vanna/volga hedging
- Daily rebalancing
- Proper risk limits

**Performance (2010-2020):**
- Sold exotics to clients
- Maintained vanna/volga neutral
- Survived multiple crises
- Consistent profitability

**Keys to success:**
1. Explicit vanna hedging (25-delta risk reversals)
2. Volga hedging (butterflies)
3. Dynamic rebalancing
4. Risk limits respected
5. Exited positions near barriers

**Average return:** 15% annually with Sharpe ratio of 1.8

---

## Practical Steps

### 1. Calculate Exposures

**Step-by-step:**

1. **Price exotic using smile:**
   - Get full vol surface from market
   - Price using appropriate model
   - Document assumptions

2. **Compute Greeks:**
   - Delta, vega (standard)
   - Vanna, volga (critical)
   - Use numerical methods if needed

3. **Decompose by strike/tenor:**
   - Where is vega concentrated?
   - Which strikes matter most?
   - Term structure exposure?

### 2. Design Hedge

**Based on exposures:**

**If large vanna:**
- Use 25-delta options
- Risk reversals for skew
- Match vanna magnitude

**If large volga:**
- Use butterflies (vega-neutral)
- Or ATM straddles (if okay with vega)

**If multi-asset:**
- Hedge each asset
- Add correlation overlay

### 3. Implement Hedge

**Execution:**

1. **Trade vanilla options:**
   - Use liquid strikes only
   - Mind bid-ask spreads
   - Execute in size (better pricing)

2. **Document hedge:**
   - Record each leg
   - Calculate resulting Greeks
   - Verify neutralization

3. **Check costs:**
   - Compare to budget
   - Too expensive? Adjust

### 4. Monitor Daily

**Daily surveillance:**

- Spot price vs. strikes
- Vol level and smile shape
- Recompute Greeks
- Check against limits
- Mark-to-market hedge

### 5. Rebalance

**When to rehedge:**

**Triggered by:**
- Monthly (time-based)
- 5% spot move
- 5 vol point move
- Approaching barrier/strike
- Big news event

**How:**
- Recalculate current Greeks
- Compute difference from target
- Trade difference
- Document rehedge

### 6. P&L Attribution

**Decompose P&L:**

$$
\text{Total P&L} = \text{Delta P&L} + \text{Vega P&L} + \text{Vanna P&L} + \text{Volga P&L} + \text{Theta}
$$

**Example:**

Daily P&L: +$50K

**Attribution:**
- Delta: +$10K (spot moved favorably)
- Vega: -$30K (vol increased, short vega)
- Vanna: +$70K (spot up + vol up = positive vanna profit)
- Volga: -$5K (smile steepened)
- Theta: +$5K (time decay)

**Insight:** Vanna hedge working (saved $70K)

### 7. Review and Learn

**Post-trade analysis:**

- Did hedge work as intended?
- Were costs acceptable?
- What would you do differently?
- Update procedures based on learning
- Document for future trades

---

## Final Wisdom

> "Hedging exotics with smile and skew is the difference between surviving as a derivatives dealer and blowing up spectacularly. Black-Scholes is a beautiful lie—it assumes one volatility for all strikes, when reality shows us a complex surface that shifts and twists with every market move. Vanna and volga aren't academic curiosities; they're the cross-Greeks that will either save your P&L or destroy it when markets stress. The cruel irony: smile risk matters most precisely when you can't hedge it well—near barriers, near expiration, near strikes where gamma explodes. Every blow-up in exotic options traces back to the same mistake: treating the vol surface as flat when it's actually a living, breathing, multi-dimensional beast. Delta-hedge alone is like trying to sail a ship by only watching the compass, ignoring the wind and waves. You need vanna hedges (OTM options), volga hedges (butterflies), and the discipline to exit positions that become unhedgeable. The market makers who survive decades aren't the ones with the fanciest models—they're the ones who respect the smile, hedge it systematically, and know when to exit rather than hero their way through a gamma explosion near a barrier. When in doubt, remember: vanna will kill you in crashes (when spot and vol move together), and volga will kill you when smile steepens (which also happens in crashes). So hedge both, or don't trade exotics at all."

**Key to success:**

- Never delta-hedge exotics without vanna/volga hedges (suicide mission)
- Vanna = use 25-delta options (standard market practice)
- Volga = use butterflies if vega-neutral, straddles if acceptable
- Rehedge monthly OR after 5% spot/5 vol moves (whichever first)
- Exit near barriers/strikes/expiration (don't be hero)
- Stress test at 2× current vol (always)
- Accept basis risk—perfect hedge is impossible (practicality wins)
- Document everything (future you will thank present you)
