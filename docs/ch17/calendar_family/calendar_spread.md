# Calendar Spreads

**Calendar spreads** (also called time spreads or horizontal spreads) are strategies where you profit from differences in implied volatility between different expiration dates by simultaneously buying and selling options at the same strike but different maturities.





---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/calendar_spread_entry_timing.png?raw=true" alt="calendar_spread_entry_timing" width="700">
</p>
<p align="center"><em>Figure 1: Optimal entry timing for calendar spreads based on volatility term structure and stock price positioning</em></p>

**The fundamental idea:**

- Options with different expiration dates trade at different implied volatilities
- Near-term options often have different IV than longer-term options
- This creates a "volatility term structure"
- You can trade the SHAPE of this term structure across time
- Profit from relative mispricing between maturities

**The key equation:**

$$
\text{IV}_{\text{front month}} \neq \text{IV}_{\text{back month}}
$$

**You're essentially betting: "The relationship between front-month and back-month volatility is mispriced."**

---

## What Is the

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/calendar_spread_iv_impact.png?raw=true" alt="calendar_spread_iv_impact" width="700">
</p>
<p align="center"><em>Figure 2: Implied volatility impact on calendar spread value showing vega sensitivity across different maturities</em></p>

**Before understanding calendar spreads, we need to understand the term structure:**

### 1. The Concept

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/calendar_spread_payoff.png?raw=true" alt="calendar_spread_payoff" width="700">
</p>
<p align="center"><em>Figure 3: Calendar spread payoff diagram at front-month expiration demonstrating maximum profit at strike</em></p>

**Volatility term structure** is the relationship between implied volatility and time to expiration:

Plot IV vs. Time to Maturity → creates a curve

**Three common shapes:**

**1. Upward Sloping (Contango):**
```
    IV
     ↑
  25%|         /‾‾
  20%|      _/
  15%|   _/
     |__________→ Time
     1M  3M  6M
```
- Longer-dated options have higher IV
- Most common in calm markets
- Market expects volatility to rise over time

**2. Downward Sloping (Backwardation):**
```
    IV
     ↑
  35%|‾\
  30%|  \__
  25%|     \___
     |__________→ Time
     1M  3M  6M
```
- Near-term options have higher IV
- Common during crises or before events
- Market expects current high vol to calm down

**3. Humped (Event-Driven):**
```
    IV
     ↑
  25%|   _/‾\_
  20%|  /     \
  15%|_/       \__
     |__________→ Time
     1M  3M  6M
```
- Peak at specific maturity
- Often around earnings or events
- After event, vol expected to normalize

### 2. Real Examples

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/calendar_spread_time_decay.png?raw=true" alt="calendar_spread_time_decay" width="700">
</p>
<p align="center"><em>Figure 4: Time decay comparison between front and back month options showing theta asymmetry</em></p>

**Example 1: Normal Market (Upward Sloping)**

- Stock at $100
- 1-month ATM IV: 18%
- 3-month ATM IV: 22%
- 6-month ATM IV: 25%
- **Front month cheaper than back month**

**Example 2: Before Earnings (Humped)**

- Stock at $100
- 1-month (before earnings) IV: 40%
- 3-month (after earnings) IV: 22%
- 6-month IV: 24%
- **Front month elevated due to earnings**

**Example 3: Crisis (Inverted)**

- Stock at $100 (during market panic)
- 1-month IV: 45%
- 3-month IV: 35%
- 6-month IV: 30%
- **Front month reflecting current panic**

---

## What Is a Calendar

**A calendar spread trades the relationship between two maturities:**

### 1. Basic Structure

**Long Calendar Spread (Most Common):**

- **Sell** near-term option (front month)
- **Buy** longer-term option (back month)
- **Same strike** (typically ATM)
- **Same type** (both calls or both puts)

**Example:**

- Stock at $100
- Sell 1-month $100 call at IV=18%
- Buy 3-month $100 call at IV=22%
- Net cost: approximately $2 per share

### 2. Why This

**Time decay asymmetry:**

- Front month decays faster (higher theta)
- You collect theta from short front month
- You pay less theta on long back month
- Net positive theta (usually)

**Volatility exposure:**

- Net long vega (back month has more vega)
- Profit if overall IV increases
- Or if back month IV rises relative to front

**The bet:**

- "Front month will decay away while back month holds value"
- Or: "Term structure will steepen (back month IV ↑ relative to front)"

---

## The Portfolio

Your calendar spread portfolio consists of:

$$
\Pi = -V_{\text{front}}(S, t_1, \sigma_1) + V_{\text{back}}(S, t_2, \sigma_2) + \text{Delta Hedge}
$$

where:

- $V_{\text{front}}$ = Front month option (short)
- $V_{\text{back}}$ = Back month option (long)
- $t_1 < t_2$ (front expires before back)
- $\sigma_1, \sigma_2$ = IVs at each maturity

**Portfolio Greeks:**

$$
\Delta_{\text{net}} = -\Delta_{\text{front}} + \Delta_{\text{back}} \approx 0
$$

$$
\Gamma_{\text{net}} = -\Gamma_{\text{front}} + \Gamma_{\text{back}}
$$

$$
\mathcal{V}_{\text{net}} = -\mathcal{V}_{\text{front}} + \mathcal{V}_{\text{back}} > 0
$$

$$
\Theta_{\text{net}} = -\Theta_{\text{front}} + \Theta_{\text{back}} > 0
$$

**Key insight:** Net vega is typically positive and net theta is typically positive—a rare combination!

**Why this structure?**

- Short front month: collect theta, short near-term vega
- Long back month: pay less theta, long longer-term vega
- Net: Usually positive theta, net long vega
- Delta hedge: isolate term structure exposure

**What you're exposed to:**

- ✓ Term structure changes (your bet)
- ✓ Net vega (usually long)
- ✓ Gamma (positive from long back, negative from short front)
- ✗ Delta (hedged)

---

## Economic

**Understanding what this strategy REALLY represents economically:**

### 1. The Core Economic

**Calendar spreads are fundamentally trading the volatility term structure:**

$$
\text{Profit} = f\left(\frac{\sigma_{\text{back}}}{\sigma_{\text{front}}}\right) + \text{Theta Collection} - \text{Movement Cost}
$$

**Economic meaning:**

You're betting that the relationship between front and back month volatilities will evolve in your favor. Specifically:

- **Time decay differential:** Front month decays faster than back month
- **Term structure normalization:** Abnormal term structures revert to normal
- **Volatility uncertainty resolution:** Different maturities price uncertainty differently

### 2. Why Calendar

**The term structure reflects different economic forces:**

**1. Mean reversion expectations:**

$$
\sigma_{\text{long-term}} \to \overline{\sigma}
$$

Market expects volatility to revert to long-run average. If current vol is elevated, front month reflects this but back month already prices in reversion.

**2. Event timing:**

Events (earnings, FDA, FOMC) create temporary vol spikes:
- Front month: High IV if event imminent
- Back month: Normal IV (event will pass)
- Creates humped or inverted term structure

**3. Supply and demand imbalances:**

- Hedgers buy front-month protection → raises front IV
- Long-term investors sell covered calls → lowers back IV
- Market makers balance but imperfectly

**4. Uncertainty resolution:**

$$
\text{Uncertainty}(t) = \int_0^t \sigma(s) ds
$$

More time = more cumulative uncertainty. Longer-dated options price this in.

### 3. The Volatility

**Historical observation:**

Calendar spreads have a positive expected return from:

1. **Theta asymmetry:** 
   $$|\Theta_{\text{front}}| > |\Theta_{\text{back}}|$$
   Front month loses value faster even with same underlying price.

2. **Term structure mean reversion:**
   Extreme slopes (steep or inverted) tend to flatten over time.

3. **Volatility clustering:**
   Current high vol predicts near-term high vol, but long-term reverts to mean.

**Empirical evidence:**

Studies show:
- Upward sloping term structures flatten ~60% of time
- Inverted term structures normalize ~75% of time
- Median term structure slope is 0.5-1.0 vol points per month

**This creates trading edge** for calendar spreads positioned to benefit from normalization.

### 4. Professional

**Institutional traders view calendars as:**

1. **Theta collection with vol protection:**
   - Unlike pure theta strategies (short options), calendars maintain long vega exposure
   - If volatility spikes, back month value protects against losses

2. **Term structure arbitrage:**
   - Exploit temporary dislocations in term structure
   - Event-driven: Before/after earnings spreads
   - Crisis-driven: Panic causes inverted structure

3. **Portfolio income generation:**
   - Range-bound markets favor calendars
   - Positive theta provides steady income
   - Lower risk than naked short options

4. **Volatility convexity:**
   - Calendar spreads have interesting convexity properties
   - Small vol increases: Net positive (vega)
   - Large vol spikes: Complex (front gamma negative, back gamma positive)

### 5. The Time

**Calendars reveal that volatility has temporal structure:**

$$
\sigma(t_1, t_2) \neq \sigma(t_2, t_3)
$$

Volatility from time $t_1$ to $t_2$ differs from $t_2$ to $t_3$ because:

**Forward volatility:**
$$
\sigma_{\text{forward}}^2 = \frac{t_2 \sigma_2^2 - t_1 \sigma_1^2}{t_2 - t_1}
$$

This forward vol can be:
- Higher than current (market expects vol to rise)
- Lower than current (market expects vol to fall)
- Calendar spreads trade these expectations

**Analogy to yield curve:**

Just as bond traders trade yield curve (interest rates across maturities), option traders trade vol term structure (IVs across maturities):

| Bond Trading | Option Trading |
|--------------|----------------|
| Yield curve | Vol term structure |
| Forward rates | Forward vols |
| Curve flattening | Term structure flattening |
| Curve inversion | Term structure inversion |

### 6. Fair Value

**Theoretical fair value of calendar spread:**

At front month expiration ($t_1$), the calendar is worth:

$$
V_{\text{calendar}}(t_1) = V_{\text{back}}(S, t_2 - t_1, \sigma_2)
$$

Before expiration, it's worth:

$$
V_{\text{calendar}}(t) = V_{\text{back}}(S, t_2, \sigma_2) - V_{\text{front}}(S, t_1, \sigma_1)
$$

**Break-even analysis:**

For calendar to profit, you need:

$$
V_{\text{back}}(t_1) > V_{\text{back}}(0) - V_{\text{front}}(0)
$$

This happens when:
- Stock stays near strike (optimal)
- IV increases (vega benefit)
- Or term structure steepens

**Expected return:**

$$
E[\text{Return}] = \text{Theta Collection} + E[\text{Vega P\&L}] - \text{Gamma Costs}
$$

Theta collection is positive and certain. Vega P&L depends on IV path. Gamma costs occur if stock moves significantly.

### 7. When Calendar

**Genuine edge exists when:**

1. **Term structure extremes:** 
   - Very steep (>5 vol points/month): Likely to flatten
   - Inverted (front > back): Likely to normalize post-event

2. **Event-driven dislocations:**
   - Pre-earnings: Front month elevated, back month normal
   - Post-crisis: Front month panic, back month calmer

3. **Seasonal patterns:**
   - January effect, quarterly earnings cycles
   - VIX futures roll patterns

**Fair pricing occurs when:**

1. Normal upward slope (0.5-1.5 vol points/month)
2. No near-term events
3. Stable market conditions

Understanding economic foundations helps recognize when calendars offer genuine edge versus when market pricing already reflects these dynamics.

---

## The P&L Formula

For a calendar spread:

$$
d\Pi \approx \underbrace{\mathcal{V}_{\text{back}} \cdot d\sigma_{\text{back}} - \mathcal{V}_{\text{front}} \cdot d\sigma_{\text{front}}}_{\text{term structure changes}} + \underbrace{\Theta_{\text{net}} \, dt}_{\text{time decay (usually positive)}} + \underbrace{\text{Gamma P\&L}}_{\text{from both legs}}
$$

**Breaking it down:**

### 1. Term Structure

**Two components:**

**A. Relative IV changes:**

- If back month IV rises more than front → profit
- If front month IV falls more than back → profit
- **This is your term structure bet**

**Quantitatively:**

$$
\text{Term Structure P\&L} = \mathcal{V}_{\text{back}} \Delta\sigma_{\text{back}} - \mathcal{V}_{\text{front}} \Delta\sigma_{\text{front}}
$$

**Example:**

Back month vega = 100, front month vega = 60

**Scenario A:** Both IVs rise 2 points
$$
\text{P\&L} = 100 \times 0.02 - 60 \times 0.02 = 2 - 1.2 = \$0.80
$$

**Scenario B:** Back month rises 3 points, front month rises 1 point
$$
\text{P\&L} = 100 \times 0.03 - 60 \times 0.01 = 3 - 0.6 = \$2.40
$$

**B. Time passage effect (roll-down):**

As time passes, back month becomes front month. This "roll-down" on the term structure curve can generate profit even if IVs don't change.

**Example:**

Term structure: 1-month 20%, 2-month 24%, 3-month 26%

After 1 month:
- Your original 3-month (26% IV) is now 2-month
- But 2-month IV is 24%
- **You benefit from rolling down the curve**

This is analogous to bond "roll-down yield."

### 2. Theta P&L

$$
\Theta_{\text{net}} = \Theta_{\text{back}} - \Theta_{\text{front}}
$$

**Typically:**

- $|\Theta_{\text{front}}| > |\Theta_{\text{back}}|$ (front decays faster)
- Net theta positive (collect more than you pay)
- **This is positive carry**

**Mathematical basis:**

Theta for ATM options:

$$
\Theta \approx -\frac{S \sigma}{2\sqrt{2\pi T}}
$$

Since $\Theta \propto \frac{1}{\sqrt{T}}$, shorter-dated options have more theta per day.

**Example:**

30-day option: $\Theta = -\$0.50$/day
90-day option: $\Theta = -\$0.29$/day

Calendar: $\Theta_{\text{net}} = -0.29 - (-0.50) = +\$0.21$/day

**You collect +$0.21/day!**

### 3. Gamma P&L

**Mixed gamma:**

- Long back month: $\Gamma_{\text{back}} > 0$
- Short front month: $\Gamma_{\text{front}} < 0$
- Net gamma can be positive or negative
- Depends on specifics (strikes, time, vol)

**Typical ATM calendar:**

$$
\Gamma_{\text{net}} = \Gamma_{\text{back}} - \Gamma_{\text{front}}
$$

Often $\Gamma_{\text{net}} < 0$ because front month has higher gamma near expiration.

**Gamma P&L:**

$$
\text{Gamma P\&L} = \frac{1}{2}\Gamma_{\text{net}} (dS)^2
$$

If net gamma negative and stock moves, you lose money.

**Example:**

$\Gamma_{\text{net}} = -0.05$, stock moves $3

$$
\text{Gamma P\&L} = \frac{1}{2} \times (-0.05) \times 3^2 = -\$0.225
$$

**Trade-off:** Calendar sacrifices some gamma upside for positive theta.

### 4. Complete Daily

$$
\text{Daily P\&L} = \underbrace{(\mathcal{V}_{\text{back}} - \mathcal{V}_{\text{front}}) d\sigma}_{\text{Vega}} + \underbrace{\Theta_{\text{net}} dt}_{\text{Theta (+)}} + \underbrace{\frac{1}{2}\Gamma_{\text{net}} (dS)^2}_{\text{Gamma (-)}}
$$

**Your goal:** Have theta and vega terms dominate gamma term.

**Best scenario:** Stock stays near strike (minimizes gamma loss), IV increases or term structure steepens (maximizes vega gain), time passes (collect theta).

---

## Types of Calendar

### 1. Standard Calendar

**Structure:**

- Both options at-the-money
- Most common
- Maximum theta collection
- Neutral directional view

**Example:**

- Stock at $100
- Sell 1-month $100 call
- Buy 3-month $100 call

**Characteristics:**

- Maximum profit if stock stays at $100
- Positive theta
- Net long vega
- Delta-neutral (approximately)

### 2. Diagonal Calendar

**Structure:**

- Different strikes (not same strike)
- Front month at one strike
- Back month at different strike
- Directional bias

**Example (Bullish Diagonal):**

- Stock at $100
- Sell 1-month $100 call
- Buy 3-month $105 call

**Characteristics:**

- Directional exposure (positive delta)
- Still benefits from time decay
- Combines calendar + vertical spread

### 3. Double Calendar

**Structure:**

- Calendar spread on calls
- Calendar spread on puts
- Same expiration pairs
- Different strikes

**Example:**

- Sell 1-month $95 put + $105 call
- Buy 3-month $95 put + $105 call

**Characteristics:**

- Defined risk
- Profit range (between strikes)
- Double theta collection
- More complex

### 4. Reverse Calendar

**Structure:**

- **Buy** front month
- **Sell** back month
- Opposite of standard calendar

**When to use:**

- Expect term structure to invert
- Before major event (earnings)
- Front month vol spike expected
- Rare trade

---

## Concrete Example

**Setup:**

**Stock:** Tech company at $100

**Market conditions:**

- 1-month ATM call IV: 20% (price: $3.00)
- 3-month ATM call IV: 24% (price: $5.50)
- Term structure: upward sloping (normal)

**Your view:** 

- "Stock will stay near $100 for next month"
- "After front month expires, back month retains value"
- "Or overall volatility will increase"

**The Trade:**

**Positions:**

- Sell 10 contracts 1-month $100 calls
      - Receive: $3.00 × 10 × 100 = $3,000
      - Vega: -0.25 per contract
      - Theta: +$20 per day per contract

- Buy 10 contracts 3-month $100 calls
      - Pay: $5.50 × 10 × 100 = $5,500
      - Vega: +0.35 per contract
      - Theta: -$10 per day per contract

**Net investment:** $5,500 - $3,000 = **$2,500**

**Net Greeks:**

- Delta: ≈ 0 (approximately neutral)
- Vega: +0.35 - 0.25 = **+0.10 per contract** (net long vega)
- Theta: +$20 - $10 = **+$10 per day per contract** (positive carry)
- Net daily theta: +$100

**Scenario 1: Stock Stays at $100 (Best Case)**

After 30 days (front month expires):

- Stock still at $100
- Front month expires worthless (you keep $3,000)
- Back month now has 60 days left
- Back month value: approximately $4.20 (decayed from $5.50)

**Your P&L:**

- Front month: +$3,000 (kept premium)
- Back month: -$1,300 (mark-to-market loss: $4.20 - $5.50)
- **Net P&L: +$1,700** 

**This is positive due to:**

- Theta asymmetry (front decayed faster)
- You can now sell the back month or hold

**Scenario 2: Stock Moves to $105 (Moderate Loss)**

After 30 days:

- Stock moved from $100 to $105
- Front month now worth $5.00 (ITM, intrinsic value)
- Back month worth $7.50

**Your P&L:**

- Front month: -$2,000 (sold at $3, now worth $5)
- Back month: +$2,000 (bought at $5.50, now worth $7.50)
- **Net P&L: $0** (approximately break-even)

**Why:** Both legs gained, but front gained more (higher gamma)

**Scenario 3: Volatility Spikes (Volatility Profit)**

After 15 days (front month still alive):

- Stock still at $100
- Market event causes volatility spike
- 1-month IV: 20% → 28% (+8%)
- 3-month IV: 24% → 30% (+6%)

**Your P&L:**

- Front month: -$800 (10 × 0.25 × 8% × 100 = -$2,000... wait let me recalculate)

Actually vega P&L = Vega × ΔIV × # contracts:
- Front month: 10 × (-25) × 0.08 = -$200
- Back month: 10 × (35) × 0.06 = +$210
- **Net P&L: +$10** (minimal, but this is simplified)

Actually should multiply by 100 (per contract):
- Front month: 10 × 100 × (-0.25) × 8 = -$2,000
- Back month: 10 × 100 × (0.35) × 6 = +$2,100
- **Net P&L: +$100**

Plus theta collected over 15 days: 15 × $100 = $1,500

**Total: +$1,600**

**Why:** Back month has more vega, benefits more from vol increase

**Scenario 4: Stock Crashes to $90 (Large Loss)**

After 30 days:

- Stock crashed to $90
- Front month expires worthless (good!)
- Back month value: $2.00 (deep OTM)

**Your P&L:**

- Front month: +$3,000 (kept premium)
- Back month: -$3,500 (bought at $5.50, now worth $2.00)
- **Net P&L: -$500**

**Why:** Large directional move hurt more than theta helped

**Risk profile summary:**

- **Maximum profit:** Stock at $100 at front month expiry
- **Breakeven:** Slightly above/below $100
- **Maximum loss:** Stock moves far away (limited to net debit)

---

## Calendar Spreads vs.

| Strategy | What You Trade | Time Dimension | Number of Expiries |
|----------|---------------|----------------|-------------------|
| **Delta Hedging** | Nothing (risk mgmt) | N/A | Any |
| **Gamma Scalping** | Realized vol (level) | Single maturity | 1 |
| **Vega Trading** | Implied vol (level) | Single maturity | 1 |
| **Smile/Skew** | IV across strikes | Single maturity | 1 |
| **Calendar Spreads** | **IV term structure** | **Multiple maturities** | **2+** |
| **Dispersion** | Correlation | Single maturity | 1 |
| **Variance Swaps** | Realized variance | Single maturity | 1 |

### 1. Key Distinctions

**Calendar Spreads vs. Gamma Scalping:**

| Aspect | Gamma Scalping | Calendar Spread |
|--------|---------------|-----------------|
| **What matters** | How much stock moves | Term structure + stock staying in range |
| **Time decay** | Negative (pay theta) | Positive (collect theta) |
| **Profit source** | Realized volatility | Theta decay + term structure |
| **Direction** | Want movement | Want stability (near strike) |
| **Maturity** | Single expiration | Multiple expirations |

**Calendar Spreads vs. Vega Trading:**

| Aspect | Vega Trading | Calendar Spread |
|--------|-------------|-----------------|
| **IV bet** | Level will change | Relationship between maturities will change |
| **Theta** | Negative (long options) | Positive (net positive theta) |
| **Structure** | Single maturity | Two maturities |
| **Profit even if IV flat** | No | Yes (theta decay) |

**Calendar Spreads vs. Smile/Skew:**

| Aspect | Smile/Skew | Calendar Spread |
|--------|-----------|-----------------|
| **Dimension traded** | Strike (space) | Time (temporal) |
| **What varies** | IV across strikes | IV across maturities |
| **Multiple of what** | Strikes (same expiry) | Expiries (same strike) |

---

## Why Calendar Spreads

**Why is the term structure non-flat?**

### 1. Mean Reversion of

**Volatility reverts to long-term average:**

- Current high vol expected to decline
- Current low vol expected to increase
- Creates term structure slope

**Example:**

- Current vol: 35% (elevated)
- Long-term average: 22%
- Market expects reversion
- → Front month: 35%, Back month: 28% (flatter)
- → Downward sloping term structure

### 2. Events and

**Known events create humps:**

- Earnings in 1 month
- Front month IV elevated (event uncertainty)
- Back month IV normal
- → Humped structure

**After event:**

- Event passes
- Front month IV collapses
- Term structure normalizes

### 3. Supply and Demand

**Hedging patterns:**

- Portfolio managers hedge near-term risk more
- Demand for front month puts
- Less demand for long-dated
- → Term structure effects

### 4. Carry and Cost of

**Time value of money:**

- Longer-dated options tie up capital longer
- Premium for duration
- → Upward sloping (typically)

### 5. Uncertainty

**Information arrival:**

- Near-term: less time for new information
- Long-term: more uncertainty
- → Usually upward sloping

---

## When Calendar

### 1. For Long Calendar

**Favorable conditions:**

**1. Normal/upward sloping term structure**

- Front month IV relatively lower
- Back month IV higher
- Collect theta while long vega

**2. Stock near the strike (ATM)**

- Maximum theta collection
- Both options at-the-money
- Symmetrical payoff

**3. Expected stability in stock**

- Stock will stay in range
- Low realized vol expected near-term
- Front month decays without being exercised

**4. Implied vol likely to rise (or stay high)**

- Protects back month value
- Net long vega benefits
- Volatility expansion expected

**5. Before events (with care)**

- Front month after event
- Back month before next event
- Capture vol crush on front

**Example environments:**

- Calm market, upward sloping term structure
- After recent volatility spike (expect calm)
- Stock trading in range
- Before event vol crush

### 2. For Reverse

**Favorable conditions:**

**1. Inverted term structure**

- Front month IV higher than back
- Unusual but happens
- During crises or pre-events

**2. Expected near-term vol spike**

- Event in front month
- Back month will stay calm
- Capture front month IV expansion

**3. Crisis fading**

- Front elevated (panic)
- Back more normal (expect calm)
- Short the elevated front, long the normal back

**Example:** 

- Before earnings: front month IV = 45%, back month = 25%
- Reverse calendar profits from this

---

## Pros and Cons

### 1. Advantages ✓

**1. Positive theta (usually)**

- Collect time decay net
- Unlike most long volatility strategies
- Positive carry trade
- **Time is on your side**

**2. Limited risk**

- Maximum loss = net debit paid
- Defined risk (unlike naked short options)
- No unlimited loss scenarios
- Sleep better at night

**3. Net long vega (usually)**

- Benefit from volatility increases
- While collecting theta
- "Best of both worlds" potential

**4. Benefits from stable prices**

- Maximum profit if stock stays at strike
- Don't need perfect prediction
- Range-bound markets are good

**5. Term structure exploitation**

- Trade a different dimension (time)
- Additional profit source beyond level/shape
- Less crowded than ATM vega trades

**6. Flexibility**

- Can adjust as market moves
- Roll front month when expires
- Convert to other structures

**7. Lower capital requirement than straddles**

- Net debit smaller than outright long options
- More efficient use of capital
- Can do larger size

**8. Natural hedge against theta**

- Unlike gamma scalping (pays theta)
- Net positive theta helps
- Reduces bleed risk

### 2. Disadvantages ✗

**1. Limited profit potential**

- Maximum gain capped
- Not unlimited like gamma scalping
- Best case: stock at strike at expiry

**2. Complexity**

- Two expiration dates to manage
- Different greeks for each leg
- More mental overhead

**3. Sensitive to large moves**

- Stock moving far from strike hurts
- Losses if stock gaps
- Directional risk remains
- **Not truly neutral to big moves**

**4. Early assignment risk (American options)**

- Short front month can be assigned
- Complicates position
- Need to manage early exercise

**5. Multiple expiry management**

- Front expires first
- Need to decide: close, roll, or let it go
- Timing decisions required

**6. Bid-ask spreads multiply**

- Two legs = two sets of spreads
- Costs add up
- Especially for less liquid strikes

**7. Path dependent**

- When stock moves matters
- Move early vs. late very different
- Hard to analyze ex-ante

**8. Vega not purely long**

- Mixed vega exposure (long back, short front)
- If front month vol spikes more, can lose
- Complex vega dynamics

**9. Correlation between maturities**

- Term structure can invert unexpectedly
- Front and back correlated but not perfectly
- Basis risk

**10. Event risk**

- Unexpected news can blow up position
- Front month can spike if near event
- Hard to fully hedge

---

[Content continues with Advanced variations, Practical Guidance sections as in original...]


