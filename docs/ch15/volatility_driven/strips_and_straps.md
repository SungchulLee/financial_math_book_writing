# Strips and Straps

**Strips and straps** are directional volatility strategies that combine unequal ratios of puts and calls at the same strike, expressing both a directional bias and a volatility bet - strips favor downside (2 puts : 1 call) while straps favor upside (1 put : 2 calls).

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/straddle_strip_strap_comparison.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/strap_payoff.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/strip_payoff.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/strip_strap_greeks.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/strip_strap_scenarios.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/strip_time_decay.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/strip_vs_two_puts.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/strips_and_straps_breakeven_analysis.png?raw=true" alt="long_call_vs_put" width="700">
</p>

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


---

## Economic Interpretation: Advanced Perspectives

**Understanding what strips and straps REALLY represent economically:**

### The Core Economic Trade-Off

Strips and straps represent a sophisticated proposition: **Trading symmetric volatility exposure (straddles) for asymmetric volatility exposure that matches directional conviction** while maintaining protection in the opposite direction.

**Economic equivalence:**

$$
\text{Strip (Bearish)} = \text{Straddle} + \underbrace{\text{Extra Put}}\_{\text{Bearish Leverage}}
$$

$$
\text{Strap (Bullish)} = \text{Straddle} + \underbrace{\text{Extra Call}}\_{\text{Bullish Leverage}}
$$

**Why this matters economically:**

- **Straddle:** Neutral volatility play, symmetric payoff

- **Strip/Strap:** Directional volatility play, asymmetric payoff

- **Trade-off:** Pay extra premium for leveraged exposure to preferred direction

**Cost comparison:**

- Straddle: 1 call + 1 put = $10 (neutral)

- Strip: 1 call + 2 puts = $15 (50% more expensive, bearish)

- Strap: 2 calls + 1 put = $14 (40% more expensive, bullish)

**Key:** Extra premium buys 2× leverage in directional move, but lose more if wrong direction or no move.

### Why This Structure Exists Economically

Markets create strips and straps because traders need to express **"I expect volatility AND have directional bias"**:

**1. Volatility + direction combined:**

**The fundamental problem:**

- Pure directional play (long call/put): Loses if wrong direction

- Pure volatility play (straddle): No leverage to preferred direction

- **Solution:** Strip/strap combines both

**Economic breakdown:**

**Strip (bearish bias + volatility):**

- 1 call: Protects if wrong (stock rallies)

- 2 puts: 2× leverage if right (stock drops)

- **View:** "Stock will move big, more likely down"

**Strap (bullish bias + volatility):**

- 2 calls: 2× leverage if right (stock rallies)

- 1 put: Protects if wrong (stock drops)

- **View:** "Stock will move big, more likely up"

**2. Asymmetric event probabilities:**

Markets often have **asymmetric distributions**:

**Earnings example:**

- Stock beats: +8% average move

- Stock misses: -12% average move

- **Asymmetry:** Downside 50% larger than upside

**Optimal structure: Strip (bearish skew)**

- 2 puts capture larger downside

- 1 call protects smaller upside

- **Matches market asymmetry**

**FDA approval example:**

- Approval: +50% average move

- Rejection: -30% average move

- **Asymmetry:** Upside 67% larger than downside

**Optimal structure: Strap (bullish skew)**

- 2 calls capture larger upside

- 1 put protects smaller downside

- **Matches market asymmetry**

**3. Capital efficiency through leverage:**

**Comparing returns on $15 investment:**

**Scenario: Stock drops from $100 to $85 (-15%)**

**Straddle (cost $10):**

- 1 put: $15 profit

- P&L: $15 - $10 = $5

- **ROI:** 50%

**Strip (cost $15):**

- 2 puts: $30 profit

- P&L: $30 - $15 = $15

- **ROI:** 100% (2× better!)

**Difference:** Extra $5 premium buys $15 additional profit (3:1 leverage)

**4. Professional institutional uses:**

**Hedge fund earnings strategies:**

- Core position: Long/short equity

- **Overlay:** Strips/straps on positions with strong conviction

**Example:**

- Long NVDA position (bullish conviction)

- Earnings coming, expect beat

- **Add:** Strap on NVDA

  - 2 calls: Amplify gains if right

  - 1 put: Hedge if wrong

- **Result:** Enhanced returns with protection

**Market maker volatility positioning:**

- See order flow indicating direction

- **Retail buying calls:** Bullish sentiment

- **Professional response:** Sell straps (collect premium from retail, limited risk)

**Arbitrage trading:**

- Identify mispriced volatility skew

- **If put skew too steep:** Sell strips (collect rich put premium)

- **If call skew too flat:** Buy straps (cheap call leverage)

**5. Volatility smile exploitation:**

**Equity markets (put skew typical):**

$$
\text{IV}_{OTM\;Put} > \text{IV}_{ATM} > \text{IV}_{OTM\;Call}
$$

**Strip advantage (bearish):**

- Buying 2 puts at elevated IV

- **But:** If you're right about drop, realized vol > implied

- **Edge:** Put skew overpays for protection, strip captures move

**Example:**

- ATM put: IV 35%, costs $6

- **If stock drops 15%:** Realized vol was 45%

- **Profit:** $15 intrinsic × 2 = $30, paid $12

- **Net:** $18 profit (150% ROI)

**Strap advantage (bullish):**

- Buying 2 calls at lower IV (relative to puts)

- **Cheaper leverage** than buying extra puts would be

- **Edge:** Call skew underprices upside moves

**6. Behavioral finance advantages:**

**Exploiting retail biases:**

**Fear asymmetry:**

- Retail overbuys puts (fear of crashes)

- Makes puts expensive

- **Professional response:** Sell strips when put premiums inflated

- Collect overpriced premium, limited risk (protection from 1 call)

**Greed asymmetry:**

- Retail underbuys upside protection

- Makes calls relatively cheap

- **Professional response:** Buy straps when calls underpriced

- Cheap leverage on upside

**Herd behavior:**

- After crash: Everyone bearish

- **Opportunity:** Buy straps (crowd wrong, calls cheap)

- After rally: Everyone bullish

- **Opportunity:** Buy strips (crowd wrong, puts on sale)

**7. The mathematics of directional leverage:**

**Expected value calculation:**

$$
EV = P(\text{Up}) \times \text{Profit}_{\text{Up}} - P(\text{Down}) \times \text{Loss}_{\text{Down}}
$$

**Strip example (bearish bias):**

- Cost: $15

- P(Down 15%): 55%

- P(Up 15%): 45%

- Profit if down: $30 - $15 = $15

- Loss if up: $15 - $15 = $0 (breakeven)

- **EV:** 0.55 × $15 + 0.45 × $0 = $8.25 (positive!)

**Strap example (bullish bias):**

- Cost: $14

- P(Up 15%): 60%

- P(Down 15%): 40%

- Profit if up: $30 - $14 = $16

- Loss if down: $15 - $14 = $1

- **EV:** 0.60 × $16 + 0.40 × $1 = $10 (strong!)

**Key insight:** Positive EV requires **accurate directional bias** + **sufficient move magnitude**.

**8. Comparison to alternatives:**

**vs. Straddle:**
| Metric | Straddle | Strip | Strap |
|--------|----------|-------|-------|
| **Bias** | Neutral | Bearish | Bullish |
| **Cost** | $10 | $15 (+50%) | $14 (+40%) |
| **Leverage** | 1× both ways | 2× down, 1× up | 2× up, 1× down |
| **Best if** | Big move either way | Big move down | Big move up |

**vs. Long Puts/Calls:**
| Metric | Long 2 Puts | Strip | Long 2 Calls | Strap |
|--------|-------------|-------|--------------|-------|
| **Cost** | $12 | $15 (+25%) | $12 | $14 (+17%) |
| **Upside protection** | None | Full (1 call) | N/A | N/A |
| **Downside protection** | N/A | N/A | None | Full (1 put) |
| **Max loss** | -$12 (100%) | -$15 (100%) | -$12 (100%) | -$14 (100%) |

**Strip/strap advantage:** Protection in opposite direction for small extra cost.

**9. Understanding the economic foundations:**

**Key insights:**

**Directional conviction is valuable:**

- If your directional bias is correct 60%+ of time

- **Strip/strap edge:** 2× leverage captures your conviction

- **Straddle disadvantage:** Equal exposure both ways (wastes opportunity)

**Move magnitude matters more than probability:**

- 55% probability × $15 move = $8.25 EV

- 70% probability × $5 move = $3.50 EV

- **Strip/strap requires:** Both probability AND magnitude

**Cost of protection is asymmetric:**

- Strip: Pay $6 (1 call) for upside protection, gain $12 (2 puts) downside leverage

- **Cost/benefit ratio:** 1:2 (efficient!)

- Strap: Pay $6 (1 put) for downside protection, gain $12 (2 calls) upside leverage

- **Cost/benefit ratio:** 1:2 (efficient!)

**Theta is the enemy (more than straddles):**

- Straddle theta: -$0.25/day

- Strip theta: -$0.38/day (50% worse)

- Strap theta: -$0.35/day (40% worse)

- **Need:** Quick move (don't hold long)

**IV crush risk is amplified:**

- Straddle: 2 options, IV crush hurts

- Strip: 3 options, IV crush hurts 50% more

- Strap: 3 options, IV crush hurts 50% more

- **Mitigation:** Enter before IV spike, exit after move

**10. The economic truth:**

Strips and straps aren't "better" than straddles—they're **different:**

**Use strips/straps when:**

- Have directional conviction (60%+ probability)

- Event has asymmetric distribution

- Willing to pay extra for leverage

- **Edge:** Better than market at predicting direction

**Use straddles when:**

- Truly neutral (50/50 either way)

- Just want volatility exposure

- Event has symmetric distribution

- **Edge:** Volatility mispriced, no directional view

**The economic foundations reveal:**

- Strips/straps are directional + volatility bets

- **Require:** Directional skill + magnitude prediction

- **Edge exists in:** Asymmetric event prediction

- **Success requires:** Being right about BOTH direction AND magnitude more often than market expects

Understanding these helps recognize:

- When strips/straps offer edge (asymmetric events + directional conviction)

- When to avoid (symmetric events, no directional view)

- How to size (accounting for higher cost + theta)

- Why professionals use them (leverage directional skill while maintaining protection)

---

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


---

## Worst Case Scenario

**What happens when volatility fails to materialize:**

### The Nightmare Setup: The "Guaranteed Volatility" That Never Came

**How it starts (The "Perfect" Earnings Play):**

You enter a strap on NVDA before earnings:

- NVDA at $130 (consolidating before earnings)

- Thesis: "Earnings will cause big move, more likely up"

- IV at 55th percentile (premiums elevated)

- Historical moves: Average 12% post-earnings

- **Structure:** Strap (bullish bias) 7 DTE to earnings

  - Buy 2× $130 calls: -$7.00 each = -$14.00

  - Buy 1× $130 put: -$6.50

  - **Total cost: $20.50** ($2,050 per strap)

  - **Breakeven up:** $140.25 (+7.9%)

  - **Breakeven down:** $119.75 (-7.9%)

  - **Need:** >7.9% move either direction to profit

- **Win probability (estimated):** 65% (expecting big earnings beat)

You trade 5 straps (feels reasonable for "high volatility" event).

**But then reality strikes:**

**Earnings Night:**

- Earnings report: Meets expectations (not beat, not miss)

- Guidance: In-line (no surprises)

- Stock reaction: Opens at $131.50 (+1.2%, tiny move)

- **Inside your breakeven zone by huge margin**

**Your position immediately (next morning):**

- 2× $130 calls: $1.50 ITM each = $3.00 total value (paid $14)

- 1× $130 put: OTM, worth $0.10 (paid $6.50)

- **Position value:** $3.10

- **Current loss:** $20.50 - $3.10 = **-$17.40 per strap**

- **5 straps:** -$17.40 × 5 × 100 = **-$8,700 loss**

- Account: $50,000 → $41,300 (-17.4%)

**Plus IV crush:**

- IV drops: 55th → 25th percentile overnight

- **Vega loss:** -$3.00 additional per strap

- **Total loss:** -$20.40 per strap

- **5 straps:** **-$10,200 loss** (20.4% of account)

**Your emotional response:** "Just needs to move $5 more, I'll hold"

**The deterioration:**

**Days 1-3 (Theta Acceleration):**

- NVDA drifts: $131 → $132 → $131.50

- **Theta burning:** -$2.50/day per strap

- Position value: $3.10 → $2.20 → $1.50

- **Loss growing:** -$19 → -$19.80 → -$20.30

- Only 4 DTE left

**Days 4-5 (The Realization):**

- NVDA still at $131

- **Theta now:** -$4.00/day (exponential acceleration)

- Position: $1.50 → $0.40 → $0.10

- **3 DTE:** Down -$20.40 (99.5% of premium)

**Day 6-7 (The Capitulation):**

- NVDA closes at $130.80

- **All options expire near-worthless**

- Calls: $0.80 ITM × 2 = $1.60

- Put: Worthless

- **Final value:** $1.60 per strap

**Expiration:**

- NVDA settles at $130.80 (+0.6% from entry)

- **Final loss:** $20.50 - $1.60 = **-$18.90 per strap**

- **5 straps:** -$18.90 × 5 × 100 = **-$9,450 loss**

- Account: $50,000 → $40,550 (-18.9%)

- **Lost 92% of premium paid** on tiny move

**But the worst is yet to come...**

### Maximum Loss Calculation

**Worst case mathematics:**

For strips and straps, max loss is **the total premium paid**:

$$
\text{Max Loss} = \text{Total Premium Paid}
$$

**This occurs when stock doesn't move at all:**
$$
\text{At Expiration, Stock = Entry Price} \implies \text{All Options Worthless}
$$

**Example (our strap):**

- Total premium: $20.50 per strap

- **Max loss:** $20.50 per strap (100% of investment)

**With 5 straps:**
$$
\text{Total Max Loss} = \$20.50 \times 100 \times 5 = \$10,250
$$

**Impact on portfolio:**

- Started: $50,000

- After strap disaster: $39,750 (-20.5%)

- **Recovery needed:** +25.8% just to break even

**For strip (bearish bias):**

- Premium: $21 (1 call + 2 puts)

- **Max loss:** $21 per strip (also 100%)

**The deceptive "protection":**

- Traders think: "I have protection both ways!"

- **Reality:** Protection worthless if stock doesn't move

- **Dead zone:** Wide range where lose most/all premium

- Stock can move 5-7% and still lose 80-100%

### What Goes Wrong: Multiple Failure Modes

The worst case for strips/straps occurs when:

**1. No move (most common disaster - 40-50%):**

- **The trap:** Stock stays flat or tiny move

- **All options expire worthless or near-worthless**

- Lose 90-100% of premium paid

- **Example:** Stock $100, stays $98-$102, lose everything

**2. Wrong direction (brutal):**

- Enter strap (bullish bias), stock drops 10%

- **2 calls worthless** (paid $14, lost everything)

- 1 put only gains $10 (paid $6.50)

- **Net:** $10 - $20.50 = -$10.50 (51% loss)

- **If it were strip:** Even worse (2 puts would have won)

**3. Insufficient move magnitude (soul-crushing):**

- Enter strap, stock rallies 5% (good direction!)

- **But:** Need 7.9% to breakeven

- Calls only $5 ITM × 2 = $10 value

- **Loss:** $20.50 - $10 = -$10.50 (51% loss)

- **Close but no cigar:** Right direction, wrong magnitude

**4. IV crush after entry (double whammy):**

- Entered at IV 55th percentile

- Event passes, IV crushes to 20th

- **Vega loss:** -$4 to -$6 per strap

- **Plus theta:** -$2 to -$4/day

- **Total decay:** Much faster than expected

- Can lose 80% in 2-3 days even with small favorable move

**5. Theta acceleration (the silent killer):**

- **First 20 days:** -$0.50/day (tolerable)

- **Last 10 days:** -$2.00/day (painful)

- **Last 5 days:** -$4.00/day (brutal)

- **Last 2 days:** -$8.00/day (devastating)

- **Hold too long:** Extra -$20-40 loss per strap

### The Cascade Effect: Strip/Strap Death Spiral

**Month 1: First "sure thing" earnings strap**

- 5 straps, $20.50 each

- Stock moves 2% (insufficient)

- **Loss:** -$9,450 (18.9% of account)

- Account: $50,000 → $40,550

- **Emotional state:** Shock

**Month 2: "Better event this time" strip**

- 6 strips (trying to recover)

- Stock moves 8% BUT IN WRONG DIRECTION (up, not down)

- **Loss:** -$8,400 (only 1 call profits, 2 puts worthless)

- Account: $40,550 → $32,150 (-36% cumulative)

- **Emotional state:** Desperation

**Month 3: "Can't lose three times" strap**

- 10 straps (all-in recovery)

- Stock doesn't move (meets expectations)

- **Loss:** -$20,500 (100% of premium on all straps)

- Account: $32,150 → $11,650 (-77% cumulative)

- **Emotional state:** Devastation

**Total damage:**

- Started: $50,000

- After 3 strips/straps: $11,650

- **Need +329% to recover** (nearly impossible)

### The IV Crush Destruction

**The hidden killer:**

**Day 0 (Before event):**

- IV: 55th percentile

- Strap cost: $20.50

- **Vega:** +0.40 per strap (long vega)

**Day 1 (After event):**

- Stock moves 2% (tiny)

- **IV crushes:** 55th → 25th percentile (-30 IV points)

- **Vega loss:** 0.40 × -30 = **-$12 per strap!**

- Intrinsic value: $2

- **Total value:** $2 (vs $20.50 paid)

- **Loss from IV alone:** -$12 (58% of total loss)

**This is why:**

- Entering at high IV = dangerous

- IV crush can destroy position even with correct direction

- **Need:** Enter at LOW IV (< 30th percentile)

### Real Examples of Disasters

**Historical Example 1: TSLA Earnings "Beat" (Q2 2024)**

**Setup:**

- Trader: "TSLA will beat, stock will rally 15%+"

- TSLA at $245

- Strap: 2× $245 calls + 1× $245 put

- Cost: $22 per strap

- 10 straps

**Earnings night:**

- Earnings beat on EPS

- **But:** Revenue miss, margins compressed

- Stock reaction: Opens at $248 (+1.2%, underwhelming)

- Next 3 days: Drifts to $242 (-1.2%)

**Result:**

- Calls worthless (below $245)

- Put only $3 ITM

- **Final loss:** $22 - $3 = -$19 per strap

- 10 straps: **-$19,000** (86% loss)

- On $60k account: -32%

**Lesson:** "Earnings beat" doesn't guarantee big move. Expectations already priced in.

**Historical Example 2: AAPL Product Launch (Sept 2023)**

**Setup:**

- Trader: "iPhone launch will cause rally"

- AAPL at $180

- Strap: 2× $180 calls + 1× $180 put

- Cost: $18 per strap

- 15 straps

**Launch day:**

- iPhone announced (as expected)

- No surprises, no major innovations

- Stock: Opens at $181, closes at $179.50 (-0.3%)

**Result:**

- No movement, all options expire worthless

- **Final loss:** $18 × 15 × 100 = **-$27,000** (100% of premium)

- On $80k account: -34%

**Lesson:** "Obvious" catalysts often already priced in. Need surprise for volatility.

### Psychology of Losses

**Emotional stages (strips/straps specific):**

**1. Overconfidence: "Earnings always move stock!"**

- Historical average: 12% move

- **Miss:** That's AVERAGE, not guaranteed

- **Reality:** 30-40% of earnings have <5% moves

**2. Hope: "Just needs small move"**

- Stock at $132, breakeven $140

- "Only needs $8 more!" (6%)

- **Reality:** 6% move in 3 DTE = very unlikely

**3. Theta paralysis: "Already lost 80%"**

- Position at -$16 (78% loss)

- "Only $4.50 more to lose, might as well hold"

- **Result:** Lose full $20.50 (held false hope)

**4. Direction confusion: "I was right about direction!"**

- Stock moved up 5% (correct direction)

- **But:** Not enough magnitude for breakeven

- Still lose 50% even when directionally correct

**5. IV misunderstanding: "Why did I lose if stock moved?"**

- Stock moved 8% (good!)

- **But:** IV crush -40 points

- Vega loss > Delta gain

- **Net:** Still lose money

**Winning trader mindset:**

- **Accept:** 40-50% of strips/straps expire worthless (high failure rate)

- **Exit:** At -50% loss or 3 DTE (don't hold to -100%)

- **Select:** Only events with historical >10% moves

- **Size:** Risk 2-3% per trade (not 20%!)

### Preventing Worst Case

**Risk management strategies:**

**1. Position sizing (CRITICAL):**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times 2\%}{\text{Premium} \times 100}
$$

**Example:**

- Portfolio: $50,000

- Premium: $20.50 per strap

- **Max contracts:** $50,000 × 0.02 / $2,050 = **0.49 → 1 strap only!**

**NOT 5, NOT 10 - Just 1 strap for $50k account!**

**Why 2% (not 5%)?**

- High failure rate (40-50%)

- Max loss = 100% of premium

- Need survive 3-5 sequential losses

**2. Exit discipline (MANDATORY):**

**Exit triggers:**

- **-50% loss:** Exit immediately

  - Example: Paid $20.50, if drops to $10, exit (save half)

- **3 DTE:** Exit if not profitable

  - Theta acceleration too severe after this

- **IV crush:** Exit if IV drops 20+ points post-event

  - Further decay likely, lock in remaining value

**3. Event quality verification:**

**Before every entry:**

- **Historical moves:** Last 4 events averaged >10% moves?

- **Surprise potential:** Room to beat/miss expectations?

- **Catalyst strength:** Binary event or gradual adjustment?

**High-quality events only:**

- Earnings (history of big surprises)

- FDA (binary approve/reject)

- Merger announcement

- **NOT:** Product launches, conferences, CEO speeches

**4. IV percentile discipline:**

**Only trade when:**

- IV < 40th percentile (preferably <30th)

- **If IV > 50th:** Too expensive, skip trade

**Why?**

- Higher IV = higher premium = higher breakeven

- IV crush risk after event

- **Edge exists only at LOW IV**

**Example:**

- Low IV (30th): Strip costs $15, breakeven ±12%

- High IV (60th): Strip costs $22, breakeven ±17%

- **12% easier to achieve than 17%!**

**5. Magnitude requirements:**

**Calculate breakeven moves BEFORE entry:**

- Strap breakeven: (Premium / 2) / Stock price

- Strip breakeven: (Premium / 2) / Stock price

**Example:**

- Stock: $100

- Strap: $20 premium

- **Breakeven:** ($20/2) / $100 = **10% move required**

**If historical moves <10%:** DON'T TRADE!

**Only trade if:**

- Historical average move > 1.5× breakeven

- Example: Need 10% breakeven → only trade if avg move >15%

### The Ultimate Protection

$$
\text{Survivability} = \frac{\text{Capital Remaining}}{\text{Capital Initial}} > 0.92
$$

**The harsh reality:**

- 40-50% of strips/straps expire worthless

- Even with "correct" direction, need magnitude

- **Theta + vega working against you**

- **Max loss = 100% of premium** (common outcome)

**Math proving the difficulty:**

- 10 trades: $20 premium each

- 4 winners: +$15 avg = +$60

- 6 losers: -$20 each = -$120

- **Net:** +$60 - $120 = **-$60** (losing strategy!)

**To be profitable:**

- Need 55%+ win rate (hard to achieve)

- **OR:** Better magnitude (occasional $50+ wins)

- **Both require:** Excellent event selection

**The only protection: EXTREME DISCIPLINE**

- Risk 2% per trade (not 10-20%)

- Exit at -50% loss or 3 DTE (don't hold to -100%)

- Only trade LOW IV (<40th percentile)

- Only trade high-quality events (historical >10% moves)

- Track win rate (if <45%, stop trading this strategy)

**Remember:** Strips/straps are HIGH RISK despite seeming "safe" (protection both ways). 100% loss on 40-50% of trades + high cost = need perfect execution. Event selection skill is EVERYTHING!

---

## Best Case Scenario

**When volatility + direction align perfectly:**

### The Perfect Setup: Low IV + Strong Catalyst + Correct Bias

**Ideal entry conditions:**

- NVDA at $130, earnings in 7 days

- IV at 28th percentile (options cheap - critical!)

- Historical earnings moves: Average 14%, last 4 quarters all beats

- Bullish bias: AI boom continuing, strong guidance expected

- 14 DTE (1 week post-earnings)

**Strap structure (bullish bias):**

- Buy 2× $130 calls: -$5.50 each = -$11.00

- Buy 1× $130 put: -$4.50

- **Total cost: $15.50** ($1,550 per strap)

- **Breakeven up:** $137.75 (+6%)

- **Breakeven down:** $122.25 (-6%)

- **Need:** >6% move either direction to profit

- 3 straps (conservative sizing on $50k account)

**The perfect sequence:**

**Days 1-6 (The Wait):**

- NVDA drifts: $130 → $132 (small move up)

- Position response:

  - Theta: -$0.40/day × 6 = -$2.40 (manageable)

  - Delta: +$4.00 (2 calls gaining)

  - **Week 1 P&L:** +$1.60 per strap (+10%)

- **Decision:** Hold for catalyst

**Earnings Night (Day 7):**

- NVDA crushes earnings

- Raises full-year guidance significantly

- AI chip demand "unprecedented"

- Stock gaps up: $132 → $152 (+15.4% overnight!)

- **WAY above breakeven of $137.75!**

**Position response (next morning):**

- 2× $130 calls: $22 ITM each = $44 total value (paid $11)

- 1× $130 put: Far OTM, worth $0.05 (paid $4.50)

- **Position value:** $44.05

- **Profit:** $44.05 - $15.50 = **+$28.55 per strap**

- **3 straps:** +$28.55 × 3 × 100 = **+$8,565** (184% ROI!)

**Plus IV expansion bonus:**

- IV spikes: 28th → 62nd percentile (post-earnings fear of pullback)

- **Vega gain:** +$4.00 per strap

- **Position value with IV:** $48.05

- **Profit:** $48.05 - $15.50 = **+$32.55 per strap**

- **Total:** +$32.55 × 3 × 100 = **+$9,765** (210% ROI!)

**Days 8-9 (The Momentum):**

- NVDA continues: $152 → $158 (+6 more points)

- Calls now $28 ITM each

- **Position value:** $56.10

- **Profit:** $56.10 - $15.50 = **+$40.60 per strap**

- **Total:** +$40.60 × 3 × 100 = **+$12,180** (262% ROI!)

**Exit Day 9:**

- Take profit at +262% ROI

- **Realized:** $12,180 profit

- **Held:** 9 days (64% of duration)

- On $4,650 capital (3 × $1,550) = **262% return in 9 days**

- **Annualized:** 10,663% (obviously not sustainable, but shows leverage power)

### Maximum Profit Achievement

$$
\text{Max Profit (Strap/Strip)} = \text{Unlimited (from long calls/puts)}
$$

**Our strap:**

- 2 calls deep ITM

- At NVDA $158: $28 ITM each = $56

- Plus put worthless

- **Value:** $56 per strap

- Profit: $56 - $15.50 = **+$40.60 per strap**

- **3 straps:** +$12,180

**If held and NVDA rallied to $180:**

- 2 calls: $50 ITM each = $100

- **Profit:** $100 - $15.50 = $84.50 per strap

- **3 straps:** +$25,350 (**545% ROI!**)

**Key insight:** Unlimited upside from 2× call exposure, leveraged gains

### What Makes It Perfect

Best case for strips/straps requires ALL:

**1. Low IV entry (CRITICAL):**

- IV < 30th percentile

- **Our trade:** 28th percentile ✓

- Options cheap = lower cost = lower breakeven

**2. Strong catalyst delivers:**

- Historical pattern of big moves (>10%)

- **Our trade:** NVDA earnings crushed ✓

- +15.4% move

**3. Correct directional bias:**

- Strap (bullish), stock rallied

- **Our trade:** 2× calls captured full move ✓

- If wrong direction (stock dropped), only 1× put exposure

**4. Sufficient magnitude:**

- Move exceeded breakeven by 10+ points

- **Our trade:** +$20 above breakeven ✓

- Deep ITM = full profit capture

**5. IV expansion after entry:**

- Low IV → High IV transition

- **Our trade:** 28th → 62nd percentile ✓

- Vega gains +$4 per strap (13% of profit)

**6. Quick move:**

- Happened in 7 days (fast)

- **Our trade:** Minimal theta decay ✓

- Only -$2.40 from theta

**The perfect combination:**

- **Delta gains:** +$33 (81% of profit) - biggest contributor

- **Vega gains:** +$4 (10% of profit)

- Theta cost: -$2.40 (6% drag)

- **Net:** +$40.60 per strap ✓

### Comparison to Alternatives

**Strap vs. Straddle:**

**Same scenario (NVDA $130 → $158, +$28):**

**Straddle:**

- Cost: $10 (1 call + 1 put)

- 1 call: $28 profit

- **P&L:** $28 - $10 = $18 (180% ROI)

- On 5 straddles: +$9,000

**Our strap:**

- Cost: $15.50 (2 calls + 1 put, 55% more expensive)

- 2 calls: $56 profit

- **P&L:** $56 - $15.50 = $40.60 (262% ROI)

- On 3 straps: +$12,180

**Strap wins:** 35% more absolute profit despite 40% fewer contracts!

**Strap vs. Long 2 Calls:**

**Alternative: Buy 2 calls only**

- Cost: $11 (2× $5.50)

- At $158: $56 profit

- **P&L:** $56 - $11 = $45 (409% ROI!)

- On 5 sets: +$22,500

**Comparison:**

- 2 calls: Higher ROI (409% vs 262%)

- **But:** No downside protection

- **If stock dropped to $110:** 2 calls = -100% (-$11), Strap = -35% (-$5.45)

**When strap wins:**

- **Uncertain direction:** Want leverage on preferred side + protection

- **Our trade:** Knew direction (bullish), so 2 calls would have been better

- **Trade-off:** Pay for protection you didn't need

### Professional Profit-Taking

**When to take profits:**

Professionals use systematic exits:

**Exit trigger system:**

**1. Profit target (primary):**

- Exit at **+150-250% ROI**

- Our trade: +262% at $158, exit ✓

- **Take 50-75% off**, let rest run if strong momentum

**2. Time-based:**

- Exit after catalyst (within 1-3 days post-event)

- Capture move, avoid theta decay

- **Our trade:** Exited Day 9 (2 days post-earnings) ✓

**3. IV-based:**

- Exit if IV compressing back toward entry

- **Lock in vega gains before evaporation**

- Our trade: IV still elevated, good timing

**4. Technical:**

- Exit if stock hits major resistance

- Or momentum slowing (RSI >70)

- **Don't overstay**

**The compounding advantage:**

Early exits with high ROI:

**Strategy A: Hold for maximum (retail):**

- Trade 1: 14 days, +$80 (if perfect)

- Probability: 15% (massive move)

- **Expected:** 0.15 × $80 = $12 per trade

**Strategy B: Exit at +200%, redeploy (professional):**

- Trade 1: 9 days, +$31 (200% ROI, 40% probability)

- Redeploy faster

- **In 14 days:** Possible 1.5 trades

- **Expected:** 0.40 × $31 × 1.5 = $18.60 per period

**Strategy B wins:** 55% better through faster turnover + higher win rate

### The Dream Scenario

**Extreme best case (rare but possible):**

**Black swan positive event:**

- Enter 10 straps on tech stocks before major AI breakthrough

- Average cost: $15 each

- **Sector-wide rally:** 20-30% across board

**Example outcome:**

- 10 straps × $60 avg profit = **+$60,000**

- On $15,000 invested = **400% ROI**

**Why rare:**

- Sector rallies: 1-2× per decade

- Timing perfectly: Very difficult

- Having capital deployed: Requires patience

- **Probability:** <1%

### The Reality Check

**Typical strip/strap outcomes (100 trades, professional execution):**

- **45 winners** (big moves, correct direction): +$25 avg = +$1,125

- **15 partial winners** (right direction, insufficient magnitude): +$5 avg = +$75

- **40 losers** (no move or wrong direction): -$15 avg (cut at -50% with 3 DTE rule) = -$600

- **Net:** +$600 per 100 opportunities

- **On $15.50 avg cost per trade:** +$600 / $1,550 risk = **38.7% return per opportunity set**

- **Annual:** ~6 opportunities/year = **232% annual return**

**But this requires:**

- **Excellent event selection** (45% win rate on magnitude + direction)

- **Low IV discipline** (all entries <35th percentile)

- **Exit discipline** (cut losses at -50%, take profits at +150-250%)

- **Position sizing** (survive 5-10 sequential losses)

**Most traders achieve:**

- 25-35% win rate (poor event/direction selection)

- High IV entries (expensive breakevens)

- Hold to expiration (lose 100% on losers)

- **Net:** Losing strategy

**Key insights:**

- **Not get-rich-quick:** Requires skill in event + direction prediction

- **High leverage:** 200-400% gains when right

- **High loss rate:** 40-55% of trades lose

- **Catalyst + directional skill critical:** Separates pros (45%+ win rate) from amateurs (25%)

**Most important:** Best case = consistent +150-250% returns on winning trades (45% of time), not occasional +500% home runs (15% of time). Success from:

- Low IV discipline (only <35th percentile)

- Event quality (historical >10% moves)

- Directional skill (60%+ accuracy on bias)

- Exit discipline (cut losses at -50%, take profits at +200%)

- Size correctly (survive the 40-55% losers) 🎯

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


---

## Practical Guidance

**Step-by-step strips/straps implementation:**

### Critical Pre-Trade Checklist

☐ **Directional bias clear?** (Bearish → Strip, Bullish → Strap)  
☐ **IV < 35th percentile?** (Low IV critical for affordable entry)  
☐ **Historical moves >10%?** (Event must have track record of big moves)  
☐ **Specific catalyst within 14 DTE?** (Earnings, FDA, etc.)  
☐ **Calculate breakeven:** (Premium/2)/Stock price = % move needed  
☐ **Verify bias probability:** >55% confidence in direction  
☐ **Liquid strikes?** (OI > 1,000, spread < 10% per leg)  
☐ **Position size for 100% loss?** (Max loss = premium paid)

### Step 1: Event Quality Verification

**CRITICAL: Only trade high-quality volatile events**

**Qualifying events:**

- **Earnings** (history of >10% moves)

- **FDA decisions** (binary approve/reject)

- **Merger announcements** (pending close)

- **Major product launches** (iPhone-level significance)

**Historical move verification:**

- Last 4 events averaged >10% moves

- At least 2 of last 4 exceeded 12%

- **If < 10% historical avg:** DON'T TRADE

**Disqualifying events:**

- Conference speeches

- Analyst days

- Regular product updates

- "Market expectations" without binary catalyst

### Step 2: Directional Bias Determination

**Choose structure based on conviction:**

**Strip (Bearish bias):**

- Use when: 60%+ probability of downside move

- Structure: 1 call + 2 puts

- **Best for:** Overvalued stocks, negative guidance risk, sector weakness

**Strap (Bullish bias):**

- Use when: 60%+ probability of upside move

- Structure: 2 calls + 1 put

- **Best for:** Undervalued stocks, positive surprise potential, sector strength

**If bias < 55%:** Use straddle instead (not strip/strap)

### Step 3: Strike Selection and Breakeven Calculation

**ATM strikes (standard approach):**

- Long calls/puts: At-the-money

- **Advantage:** Highest gamma, most responsive to moves

- **Cost:** More expensive

**Slightly OTM strikes (cost reduction):**

- Long calls/puts: 2-3% OTM

- **Advantage:** 20-30% cheaper

- **Trade-off:** Need bigger move to profit

**Breakeven calculation:**

$$
\text{Breakeven \%} = \frac{\text{Total Premium} / 2}{\text{Stock Price}} \times 100\%
$$

**Example (Strap):**

- Stock: $130

- Premium: $15.50

- **Breakeven:** ($15.50 / 2) / $130 = **6.0%**

- **Breakeven prices:** $137.80 (up) and $122.20 (down)

**Only trade if:**

- Historical average move > 1.5× breakeven

- Example: Need 6% breakeven → only if historical avg >9%

### Step 4: IV Environment Check

**Critical rule: IV < 35th percentile**

**Check IV percentile (not absolute IV):**

- Use IV rank or IV percentile indicator

- **< 25th:** Excellent (very cheap)

- **25-35th:** Good (acceptable)

- **35-50th:** Borderline (marginal)

- **> 50th:** AVOID (too expensive)

**Why IV matters:**

- High IV = expensive premium = high breakeven

- IV crush after event = additional loss

- **Edge exists only at LOW IV**

**Example impact:**

- Low IV (25th): Strap costs $14, breakeven 5.4%

- High IV (60th): Strap costs $22, breakeven 8.5%

- **8.5% is 58% harder to achieve than 5.4%!**

### Step 5: Position Sizing

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times 2\%}{\text{Total Premium} \times 100}
$$

**Example:** $50k account, $15.50 premium  
**Max:** $1,000 / $1,550 = **0.6 → 1 contract only**

**Why only 2% (not 5%)?**

- Max loss = 100% of premium (full capital at risk)

- High failure rate (40-50% lose money)

- Need survive 5-10 sequential losses

**Diversification:**

- Max 3 strips/straps per month

- Different events (not all earnings)

- **Never put >6% in strips/straps total**

### Step 6: Entry Execution

**Order entry:**

1. **Multi-leg combo order** (all 3 legs simultaneously)

2. **Limit at mid-price** or $0.10 better for entire combo

3. **Verify structure:** Count options (2 of bias direction, 1 protection)

4. **Set alerts:** Breakevens, -50% loss, 3 DTE warning

**Timing:**

- **Best:** 7-14 days before catalyst

- **Avoid:** >14 days (too much theta), <5 days (too little time)

- **Optimal:** Enter when IV dips (typically mid-week)

### Step 7: Position Management

**Daily monitoring:**

- Stock price (is move happening?)

- Days to expiration (exit by 3 DTE)

- P&L (hit -50% loss? Exit)

**Exit triggers (ANY trigger → close immediately):**

**Profit targets:**

- **Primary:** +150-250% ROI

  - Example: Paid $15.50, exit at $23-35 value

- **Event-based:** 1-3 days post-event (captured move)

**Stop losses (CRITICAL):**

- **-50% of premium:** Exit immediately

  - Example: Paid $15.50, if drops to $7.75, exit

- **3 DTE:** Exit if not +50% profitable

  - Theta too severe after this

- **IV crush >20 points:** Exit post-event

  - Further decay likely

**Time stops:**

- **Always exit by 3 DTE** regardless of P&L

- **Exit by 7 DTE if not profitable** (don't hope)

### Step 8: What NOT to Do (Critical)

**NEVER adjust strips/straps:**

- Rolling doesn't help (different catalyst, different setup)

- **Just close** and move on

**NEVER add to losing position:**

- "Averaging down" multiplies losses

- Strip/strap that didn't work = thesis wrong

- **Accept loss, move on**

**NEVER hold through expiration:**

- Final 3 days: -$5-10/day theta

- Already lost? Lose even more

- **Exit by 3 DTE always**

### Step 9: Record Template

| Date | Type | Stock | Catalyst | Premium | IV% | BE% | Outcome | P&L | ROI | Notes |
|------|------|-------|----------|---------|-----|-----|---------|-----|-----|-------|
| 1/15 | Strap | NVDA | Earnings | $15.50 | 28% | 6.0% | +$32.55 | +$9,765 | +210% | Crushed, exited D9 |
| 2/10 | Strip | TSLA | Earnings | $21.00 | 55% | 8.1% | -$18.90 | -$9,450 | -90% | No move, held too long |

**Track quarterly:**

- **Win rate:** Target 45-50%

- **Avg winner:** +200% ROI

- **Avg loser:** -50% loss (stopped out)

- **Expectancy:** Should be positive

**Calculate expectancy:**
$$
E = (W\% \times \text{Avg Win}) - (L\% \times \text{Avg Loss})
$$

Example: 0.48 × $30 - 0.52 × $7.50 = $14.40 - $3.90 = **+$10.50 per trade**

### The Strip/Strap Trading Rules

**Never trade when:**

1. No directional bias (< 55% confidence)

2. IV > 35th percentile (too expensive)

3. Historical moves < 10% (insufficient volatility)

4. No specific catalyst within 14 days

5. > 14 DTE to event (too much theta) or < 5 DTE (too little time)

6. Event not high-quality (conferences, speeches don't count)

7. Can't calculate breakeven < 8%

**Always:**

1. Use combo orders (3 legs simultaneously)

2. Calculate breakeven before entry

3. Verify historical moves > 1.5× breakeven

4. Exit at -50% loss or 3 DTE

5. Size for 2% max risk

6. Close (don't adjust) when wrong

7. Take profits at +150-250% ROI

**The golden rule:** If historical event volatility < 10% OR IV > 35th percentile OR directional confidence < 55%, DON'T trade strips/straps. The three requirements are:

1. **High volatility event** (>10% historical moves)

2. **Low IV entry** (<35th percentile)

3. **Strong directional bias** (>55% confidence)

**All three must be met. Missing any one = skip the trade.**

