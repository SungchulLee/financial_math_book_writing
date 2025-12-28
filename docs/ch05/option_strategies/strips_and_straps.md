# Strips and Straps

**Strips and straps** are directional volatility strategies that combine unequal ratios of puts and calls at the same strike, expressing both a directional bias and a volatility bet - strips favor downside (2 puts : 1 call) while straps favor upside (1 put : 2 calls).

---

## The Core Insight

**The fundamental idea:**

- Straddles are neutral: 1 put + 1 call (no directional bias)
- Ratio spreads are directional: Unlimited risk on one side
- **Strips/Straps are in-between:** Directional + volatility combined
- Strip: Bearish bias (2 puts, 1 call)
- Strap: Bullish bias (1 put, 2 calls)
- Profit from large move in EITHER direction (but more if it goes your way)
- Less capital than buying 2× straddles

**The key equation:**

$$
\text{Strip} = 1 \text{ ATM Call} + 2 \text{ ATM Puts} \quad \text{(bearish volatility)}
$$

$$
\text{Strap} = 2 \text{ ATM Calls} + 1 \text{ ATM Put} \quad \text{(bullish volatility)}
$$

**You're essentially betting: "The stock will make a BIG move, and I think it's more likely to go in MY direction (down for strips, up for straps), but I'm hedged if wrong."**

---

## What Are Strips and Straps?

**Before trading strips/straps, understand the structure:**

### Strip (Bearish Volatility Strategy)

**Definition:** Buy 1 ATM call + 2 ATM puts at the same strike.

**Structure:**

- **Buy 1×** ATM call at strike $K$ (e.g., $100 call)
- **Buy 2×** ATM puts at strike $K$ (e.g., 2× $100 puts)
- Same expiration
- Net: Debit (pay premium)

**Example:**

- Stock at $100
- Buy 1× $100 call for $5
- Buy 2× $100 puts for $5 each = $10 total
- **Total cost: $15 ($1,500 per position)**

**Payoff at expiration:**

| Stock Price | Call Value | 2× Puts Value | Total Value | P&L |
|-------------|------------|---------------|-------------|-----|
| $70 | $0 | $60 ($30 each) | $60 | **+$45** |
| $80 | $0 | $40 ($20 each) | $40 | **+$25** |
| $85 | $0 | $30 ($15 each) | $30 | **+$15** |
| $90 | $0 | $20 ($10 each) | $20 | **+$5** |
| $95 | $0 | $10 ($5 each) | $10 | **-$5** |
| $100 | $0 | $0 | $0 | **-$15** (max loss)|
| $105 | $5 | $0 | $5 | **-$10** |
| $110 | $10 | $0 | $10 | **-$5** |
| $115 | $15 | $0 | $15 | **$0** (breakeven) |
| $120 | $20 | $0 | $20 | **+$5** |
| $130 | $30 | $0 | $30 | **+$15** |

**Key characteristics:**

- **Downside profit:** 2× puts create 2:1 leverage below $100
- **Upside profit:** Single call creates 1:1 exposure above $115
- **Asymmetric breakevens:** Closer breakeven on downside ($85) vs. upside ($115)
- **Max loss at strike:** If stock exactly at $100, all options expire worthless

### Strap (Bullish Volatility Strategy)

**Definition:** Buy 2 ATM calls + 1 ATM put at the same strike.

**Structure:**

- **Buy 2×** ATM calls at strike $K$ (e.g., 2× $100 calls)
- **Buy 1×** ATM put at strike $K$ (e.g., $100 put)
- Same expiration
- Net: Debit (pay premium)

**Example:**

- Stock at $100
- Buy 2× $100 calls for $5 each = $10 total
- Buy 1× $100 put for $5
- **Total cost: $15 ($1,500 per position)**

**Payoff at expiration:**

| Stock Price | 2× Calls Value | Put Value | Total Value | P&L |
|-------------|----------------|-----------|-------------|-----|
| $70 | $0 | $30 | $30 | **+$15** |
| $80 | $0 | $20 | $20 | **+$5** |
| $85 | $0 | $15 | $15 | **$0** (breakeven) |
| $90 | $0 | $10 | $10 | **-$5** |
| $95 | $0 | $5 | $5 | **-$10** |
| $100 | $0 | $0 | $0 | **-$15** (max loss) |
| $105 | $10 ($5 each) | $0 | $10 | **-$5** |
| $110 | $20 ($10 each) | $0 | $20 | **+$5** |
| $115 | $30 ($15 each) | $0 | $30 | **+$15** |
| $120 | $40 ($20 each) | $0 | $40 | **+$25** |
| $130 | $60 ($30 each) | $0 | $60 | **+$45** |

**Key characteristics:**

- **Upside profit:** 2× calls create 2:1 leverage above $100
- **Downside profit:** Single put creates 1:1 exposure below $85
- **Asymmetric breakevens:** Closer breakeven on upside ($110) vs. downside ($85)
- **Max loss at strike:** If stock exactly at $100, all options expire worthless

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/strip_strap_payoff.png?raw=true" alt="strip_strap" width="700">
</p>
**Figure 1:** Payoff diagrams comparing straddle (symmetric), strip (bearish bias), and strap (bullish bias), showing how the 2:1 ratio creates asymmetric profit potential favoring the biased direction.

---

## Economic Interpretation: The Directional Volatility Premium

**Beyond the basic definition, understanding what strips/straps REALLY are economically:**

### The Evolution from Straddle to Strip/Strap

**Straddle (neutral volatility):**

$$
\text{Straddle} = 1 \text{ Call} + 1 \text{ Put} \quad \text{(symmetric)}
$$

- Bet: Big move either direction (no preference)
- Cost: 2× ATM options = $10
- Profit ratio: 1:1 both directions

**Strip (bearish volatility):**

$$
\text{Strip} = 1 \text{ Call} + 2 \text{ Puts} = \text{Straddle} + 1 \text{ Put}
$$

- Bet: Big move either direction, prefer down
- Cost: 3× ATM options = $15
- Profit ratio: 2:1 down vs. 1:1 up

**Strap (bullish volatility):**

$$
\text{Strap} = 2 \text{ Calls} + 1 \text{ Put} = \text{Straddle} + 1 \text{ Call}
$$

- Bet: Big move either direction, prefer up
- Cost: 3× ATM options = $15
- Profit ratio: 2:1 up vs. 1:1 down

### Why Pay 50% More for Directional Bias?

**The question:**

Straddle costs $10 (2 options), strip/strap costs $15 (3 options). You're paying 50% more. Why?

**The answer: Asymmetric expected move probabilities**

Markets exhibit **negative skewness** (crash risk > rally surprise):

$$
P(\text{10% down move}) > P(\text{10% up move}) \quad \text{(in equities)}
$$

**Strip exploits this:**

- Market HAS crash risk (10% down more likely than 10% up)
- Strip pays off 2× on downside
- **You're paying extra put premium to align with market skew**

**Strap fights this:**

- Market has LESS rally surprise risk
- Strap pays off 2× on upside
- **You're paying for unlikely scenario (rally > crash)**

**When straps make sense:**

- Individual stocks with catalysts (FDA approval, buyout, etc.)
- Positive skew situations (short squeeze, momentum)
- Commodities with supply shocks

### The Premium vs. Leverage Trade-Off

**Compare strip to just buying 2× puts:**

**Option A: Strip (1 call + 2 puts)**
- Cost: $15
- Downside leverage: 2:1
- Upside protection: 1:1 (if wrong direction)

**Option B: Just buy 2× puts**
- Cost: $10
- Downside leverage: 2:1
- Upside protection: NONE (if wrong, lose 100%)

**Strip advantage:**

$$
\text{Strip Cost} = 1.5 \times \text{Puts Cost}, \quad \text{but gets upside protection}
$$

For 50% more capital, you get:
- Same downside leverage (2× puts)
- **Plus:** Unlimited upside protection (the call)
- **Insurance value:** $5 (the call premium)

**This is "directional insurance" - you pay extra for peace of mind if wrong.**

---

## Key Terminology

**Strip:**

- 1 call + 2 puts (bearish volatility)
- "Stripped" down puts emphasize bearish
- Also called: "2-1 strip," "bearish volatility combo"

**Strap:**

- 2 calls + 1 put (bullish volatility)
- "Strapped" on extra calls for bullish
- Also called: "1-2 strap," "bullish volatility combo"

**ATM (At-the-Money):**

- Strips/straps typically use ATM strike
- All options at same strike = max gamma
- Alternative: Slightly OTM for cheaper entry

**Ratio:**

- 2:1 is standard (strip = 2 puts:1 call, strap = 2 calls:1 put)
- Can use 3:1, 4:1 for more directional bias
- Higher ratio = cheaper on average but more directional

**Volatility Skew:**

- Put IV > Call IV (typical in equities)
- Affects strip/strap pricing
- Strip more expensive (buying rich puts)
- Strap cheaper (buying cheap calls)

**Breakeven Points:**

For strip:

$$
\text{Lower BE} = K - \frac{\text{Total Cost}}{2} \quad \text{(divide by 2 puts)}
$$

$$
\text{Upper BE} = K + \text{Total Cost} \quad \text{(divide by 1 call)}
$$

For strap:

$$
\text{Lower BE} = K - \text{Total Cost} \quad \text{(divide by 1 put)}
$$

$$
\text{Upper BE} = K + \frac{\text{Total Cost}}{2} \quad \text{(divide by 2 calls)}
$$

---

## Why Trade Strips and Straps?

**Use cases:**

### 1. Earnings with Directional Lean

**Scenario:** Company reporting earnings, expecting big move, slight bearish bias

**Setup:**
- Stock at $100
- Earnings tomorrow
- IV at 60% (expensive, but expecting move)
- Thesis: Beat/miss both possible, but miss more likely (management guided conservatively)

**Trade:** Strip (bearish bias)

- Buy 1× $100 call for $6 (60% IV)
- Buy 2× $100 puts for $6 each = $12
- **Total cost: $18**

**Outcome Scenario A (bearish correct):**
- Earnings miss, stock drops to $85
- Call worthless: $0
- Each put worth $15 × 2 = $30
- **P&L: $30 - $18 = +$12 (67% return)**

**Outcome Scenario B (wrong, but protected):**
- Earnings beat, stock rallies to $115
- Call worth $15
- Puts worthless: $0
- **P&L: $15 - $18 = -$3 (17% loss, not 100%!)**

**Why this works:**
- Express directional bias (bearish) while maintaining upside protection
- If wrong, only lose partial premium (not all)
- If right, get 2× leverage

### 2. FDA Approval Event (Biotech)

**Scenario:** Biotech awaiting FDA approval decision

**Market expectations:**
- 60% approval → Stock $150 (+50%)
- 40% rejection → Stock $70 (-30%)
- **Skew favors upside** (rare situation)

**Trade:** Strap (bullish bias, aligns with positive skew)

- Stock at $100
- Buy 2× $100 calls for $8 each = $16
- Buy 1× $100 put for $6
- **Total cost: $22**

**Outcome A (approval):**
- Stock → $150
- Calls: 2× $50 = $100
- Put: $0
- **P&L: $100 - $22 = +$78 (355% return!)**

**Outcome B (rejection):**
- Stock → $70
- Calls: $0
- Put: $30
- **P&L: $30 - $22 = +$8 (36% return, still profit!)**

**Why this works:**
- Positive skew (upside > downside magnitude)
- Strap aligns with skew (2× upside exposure)
- Even if rejected, downside protected by put

### 3. Commodity Supply Shock

**Scenario:** Oil at $80, geopolitical tensions rising

**Thesis:**
- If tensions escalate → Oil $95 (supply shock)
- If resolved → Oil $75 (normalization)
- **Upside has more magnitude** ($95 vs $75 = $15 up vs $5 down)

**Trade:** Strap (bullish commodity volatility)

- Buy 2× $80 calls for $5 each = $10
- Buy 1× $80 put for $4
- **Total cost: $14**

**Outcome A (tensions escalate):**
- Oil → $95
- Calls: 2× $15 = $30
- **P&L: $30 - $14 = +$16 (114% return)**

**Outcome B (resolved):**
- Oil → $75
- Put: $5
- **P&L: $5 - $14 = -$9 (64% loss, partial)**

**Why this works:**
- Asymmetric move expectations (bigger upside)
- Strap captures 2× upside leverage
- Put limits downside to 64% vs. 100% if just calls

### 4. Post-Crash Recovery Play

**Scenario:** Market just crashed 15%, expecting bounce or further drop

**Setup:**
- SPY at $400 (down from $470)
- Expecting: Either recovery rally to $430 OR another leg down to $370
- **Bias:** Slightly bullish (oversold bounce more likely)

**Trade:** Strap

- Buy 2× $400 calls for $12 each = $24
- Buy 1× $400 put for $10
- **Total cost: $34**

**Outcome A (bounce):**
- SPY → $430
- Calls: 2× $30 = $60
- **P&L: $60 - $34 = +$26 (76% return)**

**Outcome B (further drop):**
- SPY → $370
- Put: $30
- **P&L: $30 - $34 = -$4 (12% loss)**

**Why this works:**
- Crash recovery has historical precedent
- 2× calls capitalize on bounce
- Put hedges renewed selloff

### 5. Neutral to Slight Directional (vs. Straddle)

**Comparison question:** Why strip instead of straddle?

**Scenario:**
- Stock at $100, volatility expected
- **Slight bearish bias** (55% down, 45% up)

**Option A: Straddle**
- Cost: $10 (1 call + 1 put)
- Symmetric payoff

**Option B: Strip**
- Cost: $15 (1 call + 2 puts)
- Asymmetric payoff (favor down)

**Analysis:**

If stock → $85:
- Straddle profit: $15 - $10 = $5
- Strip profit: $30 - $15 = $15 (**3× better!**)

If stock → $115:
- Straddle profit: $15 - $10 = $5
- Strip profit: $15 - $15 = $0 (breakeven)

**Expected value (55% down, 45% up):**
- Straddle: (0.55 × $5) + (0.45 × $5) = $5
- Strip: (0.55 × $15) + (0.45 × $0) = $8.25

**Strip has 65% higher EV if directional bias correct!**

---

## Greeks Behavior

### Delta: Asymmetric Directional Exposure

**Strip delta:**

$$
\Delta_{\text{Strip}} = \Delta_{\text{call}} + 2 \times \Delta_{\text{put}} \approx +0.50 + 2(-0.50) = -0.50
$$

**Initial delta (ATM):**
- Strip: Delta ≈ -0.50 (bearish)
- Strap: Delta ≈ +0.50 (bullish)

**Delta evolution:**

**Strip (stock drops to $90):**
- Call delta: +0.20 (OTM)
- Put delta: -0.75 each × 2 = -1.50
- **Net delta: -1.30** (very bearish!)

**Strip (stock rises to $110):**
- Call delta: +0.80 (ITM)
- Put delta: -0.25 each × 2 = -0.50
- **Net delta: +0.30** (slightly bullish)

**Key insight:** Delta becomes increasingly directional as stock moves toward your bias.

### Gamma: Positive (Long Volatility)

**Gamma:**

$$
\Gamma_{\text{Strip}} = \Gamma_{\text{call}} + 2 \times \Gamma_{\text{put}} > 0 \quad \text{(positive)}
$$

**Why positive gamma?**

You OWN all options (long gamma position). Every option you buy contributes positive gamma.

**Example:**
- Call gamma: +0.05
- Put gamma: +0.05 each × 2 = +0.10
- **Net gamma: +0.15** (excellent!)

**Practical impact:**

- Stock whipsaws → You profit from gamma
- Large moves accelerate profits (gamma convexity)
- Unlike short premium, movement HELPS you

**This is critical:** Strips/straps are LONG volatility plays (benefit from movement).

### Theta: Negative (Pay for Time)

**Theta:**

$$
\Theta_{\text{Strip}} = \Theta_{\text{call}} + 2 \times \Theta_{\text{put}} < 0 \quad \text{(negative)}
$$

**Why negative theta?**

You bought 3 options. Time decay works AGAINST you.

**Example:**
- Call theta: -$0.15/day
- Put theta: -$0.15/day × 2 = -$0.30/day
- **Net theta: -$0.45/day**

**Practical impact:**

- Lose $0.45 per day if stock doesn't move
- **Need move within ~33 days** ($15 cost / $0.45 theta = 33 days to decay to zero)
- Time is enemy (must have catalyst soon)

**Theta evolution:**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/strip_theta_decay.png?raw=true" alt="strip_theta" width="700">
</p>
**Figure 2:** Theta decay for strip showing accelerating time decay as expiration approaches, with 50% of value lost in final 2 weeks if stock unmoved.

### Vega: Positive (Long Volatility)

**Vega:**

$$
\text{Vega}_{\text{Strip}} = \text{Vega}_{\text{call}} + 2 \times \text{Vega}_{\text{put}} > 0
$$

**Example:**
- Call vega: +0.20
- Put vega: +0.20 × 2 = +0.40
- **Net vega: +0.60**

**Practical impact:**

- IV increases → Position gains value
- IV decreases → Position loses value
- **Critical:** Don't buy strips/straps at HIGH IV (you're buying expensive)

**Example:**

**Buy strip at IV = 40%:**
- Cost: $15

**Next day, IV drops to 30% (IV crush):**
- Vega loss: -0.60 × 10 = -$600
- **New value: $9** (lost 40% overnight!)

**Lesson:** Only buy strips/straps when expecting BOTH move AND IV increase (or at least stable IV).

---

## When Greeks Hurt You

### The No-Move Theta Bleed

**Scenario:** Bought strap expecting big move, stock stays flat

**Setup:**
- Stock at $100
- Strap cost: $15 (2 calls + 1 put)
- Theta: -$0.45/day

**Week 1:** Stock at $100 (no move)
- Theta loss: $0.45 × 7 = -$3.15
- **New value: $11.85**

**Week 2:** Stock at $101 (tiny move)
- Theta loss: Another -$3.15
- **New value: $8.70**

**Week 3:** Stock at $99 (oscillating, but not moving)
- Theta loss: Another -$3.15
- **New value: $5.55** (down 63%!)

**Week 4:** Stock at $100 (ended where it started)
- Theta loss: Another -$3.15
- **New value: $2.40**

**Total loss: -$12.60 (84%) despite being "right" that stock near $100**

**Lesson:** Strips/straps are NOT for range-bound markets. Theta will destroy you if no movement.

### The IV Crush Disaster

**Scenario:** Bought strip before earnings at high IV

**Setup:**
- Stock at $100, earnings tonight
- IV at 70% (very high)
- Strip cost: $22 (expensive due to high IV)
- Vega: +0.65

**Post-earnings:**
- Stock drops to $92 (good for strip, 2× puts!)
- But IV crushes: 70% → 35% (-35%)
- **Vega loss:** -0.65 × 35 = -$2,275 (!!)

**P&L breakdown:**
- Puts gained from move: 2× $8 = $16
- Vega loss from IV crush: -$22.75
- **Net P&L: $16 - $22.75 = -$6.75 loss**

**Despite being RIGHT on direction (bearish), lost money due to IV crush!**

**Lesson:** Don't buy strips/straps at elevated IV if expecting IV crush. Use alternative structures (like selling straddle + directional spread).

### The Wrong Direction Disaster

**Scenario:** Bought strip (bearish), stock rallied

**Setup:**
- Strip cost: $15
- Expecting drop to $85
- Stock rallied to $110 instead

**P&L:**
- Call gained: $10
- Puts lost: $0 (worthless)
- **Net: $10 - $15 = -$5 loss (33%)**

**Compare to straddle:**
- Straddle cost: $10
- Stock at $110: $10 gain
- **Net: $10 - $10 = $0 breakeven**

**Lesson:** If direction is WRONG, strip/strap underperforms straddle. The extra directional option doesn't help (it's OTM).

---

## Common Pitfalls

### 1. Buying at High IV

**The mistake:**

"Earnings tomorrow, I'll buy a strip to capture the move."

**What you missed:**

High IV = expensive options. You're paying top dollar and vulnerable to IV crush.

**Example:**

**IV at 70% (pre-earnings):**
- Strip cost: $22

**IV at 35% (post-earnings):**
- Strip value: $12 (even if stock moved favorably)
- **IV crush cost you $10 (45% of position!)**

**The fix:**

- **Only buy strips/straps at NORMAL IV** (<50th percentile)
- If IV high, consider selling strategies instead
- Or wait for IV to normalize post-event

### 2. Wrong Time Frame Selection

**The mistake:**

"I'll buy 3-month strip for flexibility."

**What you missed:**

Longer time = more theta to pay. Strips/straps need short-term catalysts.

**Example:**

**3-month strip:**
- Cost: $20
- Theta: -$0.30/day
- **Total theta to expiration:** $0.30 × 90 = $27 (more than you paid!)

**1-month strip:**
- Cost: $15
- Theta: -$0.50/day
- **Total theta to expiration:** $0.50 × 30 = $15 (equal to cost)

**The fix:**

- **Use 2-4 week expiration** (short-term catalyst)
- Match expiration to expected event (earnings, FDA, etc.)
- Don't use strips/straps for vague "eventually" thesis

### 3. Confusing Strip/Strap with Ratio Spreads

**The mistake:**

"Strip is like a put ratio spread, right?"

**What you missed:**

Ratio spreads SELL options (collect premium), strips/straps BUY options (pay premium).

**Comparison:**

| Feature | Strip | Put Ratio Spread |
|---------|-------|------------------|
| **Structure** | Buy 1 call + 2 puts | Buy 1 put, sell 2 puts |
| **Cost** | Debit (pay $15) | Credit or small debit |
| **Risk** | Limited (premium) | Unlimited (short puts) |
| **Theta** | Negative (pay) | Positive (collect) |
| **Gamma** | Positive (long) | Negative (short) |

**The fix:**

- **Strip:** Directional volatility BET (long premium)
- **Ratio spread:** Directional range TRADE (short premium)
- Completely different risk profiles

### 4. No Clear Catalyst

**The mistake:**

"I think the stock will move eventually, I'll buy a strap."

**What you missed:**

"Eventually" gets destroyed by theta. Need SPECIFIC, NEAR-TERM catalyst.

**Example:**

- Bought strap with vague "bullish long-term" thesis
- No specific event
- Stock drifts +5% over 2 months
- **Theta ate all gains** (and more)

**The fix:**

- **Only use strips/straps for SPECIFIC EVENTS:**
  - Earnings (< 1 week away)
  - FDA decisions (< 2 weeks)
  - Fed announcements (< 1 week)
  - Merger votes (< 1 week)
- If no catalyst, use LEAPS or stock instead

### 5. Wrong Ratio Selection

**The mistake:**

"I'll use 4:1 ratio for more directional bias!"

**What you missed:**

Higher ratio = more capital, more theta, less hedging.

**Comparison:**

**2:1 strip (standard):**
- 1 call + 2 puts
- Cost: $15
- Hedging: Call provides reasonable upside protection

**4:1 strip (aggressive):**
- 1 call + 4 puts
- Cost: $25
- Hedging: Call provides WEAK upside protection (4× puts overwhelm)

**Analysis:**

If stock rallies to $115 (wrong direction):
- **2:1 strip:** $15 call - $15 cost = $0 (breakeven)
- **4:1 strip:** $15 call - $25 cost = -$10 (still loss!)

**The fix:**

- **Standard ratio: 2:1** (balanced bias + hedging)
- Only use 3:1 or 4:1 if VERY confident in direction
- Higher ratio approaches outright directional bet (loses hedging benefit)

---

## Risk Management Rules

**Essential guidelines:**

### Position Sizing

**Rule of thumb:**

$$
\text{Position Size} = \frac{\text{Risk Capital} \times 0.05}{\text{Strip/Strap Cost}}
$$

**Example:**

- $50,000 account
- 5% risk = $2,500
- Strip cost = $15 ($1,500)
- **Max size: 1-2 contracts**

**Note:** Higher risk allocation than regular options because:
1. Limited risk (can only lose premium)
2. Asymmetric payoff (high profit potential)

### IV Entry Guidelines

**Check IV percentile before entering:**

$$
\text{IV Percentile} = \frac{\text{Current IV} - \text{Min IV (1yr)}}{\text{Max IV (1yr)} - \text{Min IV (1yr)}}
$$

**Entry rules:**

- **<40th percentile:** Good entry (options relatively cheap)
- **40-60th percentile:** Acceptable (normal range)
- **>60th percentile:** AVOID (expensive, IV crush risk)

**Exception:** Can enter at high IV if expecting IV to INCREASE further (rare).

### Time Frame Selection

**Optimal expiration:**

- **2-4 weeks:** Best balance of theta vs. time for catalyst
- **Avoid <1 week:** Gamma too high, theta too destructive
- **Avoid >6 weeks:** Too much theta to overcome

**Match to catalyst:**

- Earnings in 1 week → Use 2-week expiration
- FDA decision in 2 weeks → Use 3-week expiration
- Fed meeting in 3 days → Use 1-week expiration (exception)

### Exit Rules

**Set upfront:**

- **Profit target:** 50-100% gain (don't be greedy)
- **Stop loss:** -50% of premium paid (preserve capital)
- **Time stop:** Exit if 50% of time passed with no move
- **IV stop:** Exit if IV drops >20% (vega risk)

**Example:**

- Strip cost: $15
- Profit target: $23 (+50%)
- Stop loss: $7.50 (-50%)
- Time stop: Day 10 of 20 DTE if no movement
- IV stop: If IV drops from 40% → 32%

### Avoid These

- Never buy strips/straps at high IV (>60th percentile)
- Never use without specific catalyst (<4 weeks away)
- Never hold to expiration (theta accelerates in final week)
- Never use 3:1 or higher ratios (too directional)
- Never confuse with ratio spreads (opposite strategies)
- Never use in range-bound markets (theta destroys)

---

## Real-World Examples

### Example 1: TSLA Earnings Strip (Success)

**Setup (October 2024):**

- TSLA at $240, earnings in 5 days
- IV at 45th percentile (55% IV, normal for TSLA)
- Analyst estimates mixed, slight bearish bias (deliveries weak)

**Trade (5 DTE):**

- Buy 1× $240 call for $10
- Buy 2× $240 puts for $10 each = $20
- **Total cost: $30 ($3,000)**

**Position Greeks:**
- Delta: -0.48 (bearish bias)
- Gamma: +0.18 (long volatility)
- Theta: -$125/day (high, but short time frame)
- Vega: +$0.88 (benefit from IV expansion)

**Earnings result:**

- Miss on deliveries, weak guidance
- Stock drops $240 → $215 (-10.4%)
- IV expanded slightly: 55% → 60% (vega helped)

**Exit (next day):**

- Calls worthless: $0
- Each put worth $25 × 2 = $50
- **Total value: $50**
- **Profit: $50 - $30 = $20 (67% return)**

**Lesson:** Directional bias correct + volatility expansion = perfect strip setup. The call was "insurance" (lost $10) but 2× puts more than made up for it.

### Example 2: Biotech FDA Strap (Massive Win)

**Setup (June 2024):**

- Small cap biotech at $12
- FDA decision expected in 2 weeks
- Approval odds: ~65% (positive bias)
- IV at 38th percentile (relatively cheap)

**Trade (3 weeks DTE):**

- Buy 2× $12 calls for $1.50 each = $3.00
- Buy 1× $12 put for $1.20
- **Total cost: $4.20 ($420 per position)**

**FDA outcome:**

- **Approved!** (surprise unanimous panel vote)
- Stock gaps: $12 → $32 overnight (+167%!)

**Exit (morning after):**

- Each call worth $20 × 2 = $40
- Put worthless: $0
- **Total value: $40**
- **Profit: $40 - $4.20 = $35.80 (852% return!)**

**Lesson:** Positive skew events (FDA approval) are PERFECT for straps. Even with lower probability (65%), the magnitude of upside movement creates exceptional returns. The put was "insurance" that wasn't needed.

### Example 3: No-Move Theta Disaster

**Setup (March 2024):**

- Tech stock at $100
- Trader expects "volatility soon" (no specific catalyst)
- IV at 50th percentile

**Trade (45 DTE - too long!):**

- Buy 1× $100 call for $6
- Buy 2× $100 puts for $6 each = $12
- **Total cost: $18**

**Week 1-2:** Stock drifts $98-$102 (no real move)
- Theta: -$0.40/day × 14 = -$5.60
- **Value: $12.40**

**Week 3-4:** Stock at $101 (still no move)
- Theta: -$0.40/day × 14 = -$5.60
- **Value: $6.80**

**Week 5-6:** Stock at $99 (range-bound)
- Theta accelerating: -$0.55/day × 14 = -$7.70
- **Value: $0** (essentially worthless)

**Final outcome:**

- **Total loss: -$18 (100%)**
- Stock ended at $99 (close to start)
- No specific catalyst ever materialized

**Lesson:** "Eventually" is not a catalyst. Strips/straps need SPECIFIC, NEAR-TERM events. Theta destroyed this position despite neutral view being "correct."

### Example 4: IV Crush Despite Correct Direction

**Setup (January 2024):**

- Stock at $150, earnings tomorrow
- IV at 85th percentile (95% IV - extremely high)
- Bearish bias on fundamentals

**Trade (1 week DTE):**

- Buy 1× $150 call for $12 (expensive!)
- Buy 2× $150 puts for $12 each = $24
- **Total cost: $36**

**Earnings result:**

- Miss as expected
- Stock drops: $150 → $135 (-10%)
- **BUT IV crushes:** 95% → 50% (-45%!)

**Exit (next day):**

- Calls worthless: $0
- Puts worth $15 each × 2 = $30
- **Intrinsic gained: $30**
- **But vega loss:** -$0.80 × 45 = -$36 per contract

**P&L breakdown:**

- Directional gain: $30 (from stock drop)
- Vega loss: -$36 (from IV crush)
- Theta loss: -$3 (overnight)
- **Total: $30 - $36 - $3 = -$9 loss**
- **Final: Paid $36, value $27, loss -$9 (25%)**

**Lesson:** NEVER buy strips/straps at elevated IV before earnings. Even when DIRECTIONALLY CORRECT, IV crush destroyed the trade. Should have waited for post-earnings IV normalization OR used different structure.

---

## What to Remember

### Core Concept

**Strips and straps combine directional bias with volatility exposure:**

$$
\text{Strip} = \text{Straddle} + 1 \text{ Put} \quad \text{(bearish volatility)}
$$

$$
\text{Strap} = \text{Straddle} + 1 \text{ Call} \quad \text{(bullish volatility)}
$$

- Pay 50% more than straddle for directional bias
- Get 2:1 leverage in favored direction
- Maintain protection if wrong direction
- Defined risk (premium paid)
- Need BIG move AND correct direction for max profit

### The Setup

**Strip (Bearish Volatility):**

- Buy 1 ATM call
- Buy 2 ATM puts
- Debit paid: ~$15 (1.5× straddle cost)
- Favor: Downside moves (2× leverage)

**Strap (Bullish Volatility):**

- Buy 2 ATM calls
- Buy 1 ATM put
- Debit paid: ~$15 (1.5× straddle cost)
- Favor: Upside moves (2× leverage)

### The Greeks

**Critical to understand:**

- **Delta:** ±0.50 initially (directional bias)
- **Gamma:** Positive (long volatility, profit from movement)
- **Theta:** Negative (time decay enemy, need quick move)
- **Vega:** Positive (benefit from IV increase, hurt by IV crush)

### Maximum Profit/Loss

**Max loss (stock at strike):**

$$
\text{Max Loss} = \text{Total Premium Paid} \quad \text{(if stock exactly at } K \text{)}
$$

**Max profit:**

- Strip: Unlimited downside (2× puts), limited upside (1 call)
- Strap: Unlimited upside (2× calls), limited downside (1 put)

**Breakevens:**

Strip:
- Lower: $K - \frac{\text{Cost}}{2}$ (closer to strike)
- Upper: $K + \text{Cost}$ (farther from strike)

Strap:
- Lower: $K - \text{Cost}$ (farther from strike)
- Upper: $K + \frac{\text{Cost}}{2}$ (closer to strike)

### When to Use

**Use strips/straps when:**

- Specific catalyst coming (<4 weeks)
- Directional bias but want volatility hedge
- Normal IV (<50th percentile)
- Expecting large move (>10%)
- Asymmetric move probabilities (match to strip/strap)

**Don't use when:**

- High IV (>60th percentile, IV crush risk)
- No specific catalyst ("eventually")
- Range-bound expected
- Long time frame (theta too destructive)
- Very confident in direction (use directional spread instead)

### Common Mistakes to Avoid

1. Buying at high IV (IV crush destroys)
2. No specific catalyst (theta bleeds)
3. Wrong time frame (>6 weeks, too much theta)
4. Confusing with ratio spreads (opposite structures)
5. Using extreme ratios (3:1 or 4:1, lose hedging)
6. Holding to expiration (theta accelerates)
7. Not taking profits at 50-100% gain

### Risk Management

**Essential rules:**

- Size for 5% of account per trade (higher than normal)
- Enter only at <50th percentile IV
- Use 2-4 week expiration (short-term catalyst)
- Profit target: 50-100% gain
- Stop loss: -50% of premium
- Time stop: Exit if 50% time elapsed with no move
- IV stop: Exit if IV drops >20%

### Comparison to Straddles

**Advantages over straddles:**

- 2× leverage in favored direction
- Higher profit if direction correct
- Same unlimited profit potential (one side)

**Disadvantages vs. straddles:**

- 50% more expensive (3 options vs. 2)
- Lower profit if direction wrong
- More complex to manage
- Asymmetric breakevens (harder to calculate)

### Your Learning Path

**Progression:**

1. Master long calls/puts (directional)
2. Master straddles/strangles (neutral volatility)
3. Learn strips/straps (this chapter - directional volatility)
4. Progress to ratio spreads (sell volatility)
5. Eventually: Complex multi-leg structures

**Strips/straps bridge directional and volatility trading!**

### Final Wisdom

> "Strips and straps are for traders who have an opinion but respect uncertainty. You think the stock goes down (strip) or up (strap), but you're humble enough to pay insurance in case you're wrong. The 2:1 ratio is the sweet spot - enough bias to matter, enough hedge to sleep. But remember: these are sprints, not marathons. If you don't have a catalyst within 2-4 weeks, you're just lighting theta on fire. Use strips and straps for high-conviction, near-term events where you have directional edge but want volatility exposure. Otherwise, you're better off with straddles (if neutral) or directional spreads (if very confident)."

**Key to success:**

- Specific catalyst within 2-4 weeks (earnings, FDA, Fed)
- Enter at normal IV (<50th percentile)
- Match structure to bias (strip = bearish, strap = bullish)
- Take profits at 50-100% (don't wait for max)
- Exit if no movement by 50% time elapsed
- Never buy at elevated IV (IV crush destroys even if directionally correct)

**Most important:** Strips and straps are directional volatility bets - you need BOTH the move AND the direction. If unsure on direction, use straddles. If sure on direction, use vertical spreads. Strips/straps occupy the middle ground! 🎯📊
