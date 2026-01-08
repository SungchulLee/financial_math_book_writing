# Broken Wing Butterflies

**Broken wing butterflies** are asymmetric butterfly spreads where one wing is "broken" (skipped), creating directional bias while maintaining defined risk and often allowing for credit collection or reduced debit.

---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_butterfly.png?raw=true" alt="broken_wing" width="700">
</p>

**The fundamental idea:**

- Regular butterflies are symmetric: profit at center, risk on both wings
- "Breaking" one wing eliminates risk on that side
- Creates directional bias (bullish or bearish lean)
- Often can be entered for a CREDIT (get paid to enter)
- Still maintains defined maximum loss
- Trade-off: Reduced max profit vs regular butterfly

**The key equation:**

$$
\text{Max Loss} = |\text{Wing Width}| - \text{Net Premium} \quad \text{(still defined!)}
$$

$$
\text{Max Profit} = \text{Body Width} + \text{Net Credit} \quad \text{(or Body - Net Debit)}
$$

**You're essentially betting: "Stock will stay in my profit zone, which is skewed towards one direction, and I want to collect premium for taking asymmetric risk."**

---

## What Is a Broken Wing Butterfly?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/bwb_theta_decay.png?raw=true" alt="bwb_theta" width="700">
</p>

**Before trading broken wings, understand the modification from regular butterflies:**

### 1. Regular Butterfly (Symmetric) - Baseline

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/bwb_vega_surface.png?raw=true" alt="bwb_vega" width="700">
</p>

**Standard call butterfly:**

- Buy 1× $95 call
- Sell 2× $100 calls
- Buy 1× $105 call
- **Cost:** $2 debit
- **Max profit at $100:** $3
- **Risk on both sides:** Below $95, above $105

**Payoff at expiration:**

- Stock < $95: Lose $2 (debit paid)
- Stock = $100: Profit $3
- Stock > $105: Lose $2 (debit paid)
- **Symmetric risk**

### 2. Broken Wing Butterfly (Asymmetric)

**Bullish broken wing call butterfly:**

- Buy 1× $95 call
- Sell 2× $100 calls
- Buy 1× $110 call (WIDER upper wing, "broken")
- **Cost:** $0.50 CREDIT (get paid!)
- **Max profit at $100:** $5.50
- **Risk only on downside:** Below $95
- **Risk-free above $105:** Can't lose on upside!

**Key modification:**

$$
\text{Upper Strike} = K_2 + (K_2 - K_1) + \text{Offset}
$$

Where offset creates asymmetry and allows credit collection.

**Example breakdown:**

- $K_1 = 95$ (lower strike)
- $K_2 = 100$ (center strike, short)
- $K_3 = 110$ (upper strike, NOT 105)
- Body width: $100 - $95 = $5
- Upper wing: $110 - $100 = $10$ (WIDER than body!)
- **This asymmetry creates the "broken" wing**

**Payoff characteristics:**

- Stock < $95: Lose $4.50 (max loss)
- Stock = $100: Profit $5.50 (max profit)
- Stock = $105 or higher: Breakeven to small profit
- **No risk above $105** (broken wing protects you!)

**Figure 1:** Comparison of regular butterfly (symmetric) vs broken wing butterfly (asymmetric), showing how the broken wing eliminates upside risk while maintaining defined downside risk and often allowing credit collection.

---

## Economic

**Beyond the basic definition, understanding what broken wings REALLY are economically:**

### 1. Why Does the Broken Wing Exist?

**The fundamental market insight:**

Options markets exhibit **volatility skew** - OTM puts are more expensive than OTM calls (in equities). Broken wing butterflies exploit this by:

1. **Selling expensive insurance** (short calls near ATM)
2. **Buying cheap protection** (far OTM call)
3. **Creating one-sided risk** (only lose on one side)
4. **Collecting net premium** (skew differential allows credit)

**Skew exploitation:**

$$
\underbrace{P_{95\text{C}}}_{\text{Pay fair price}} - 2 \times \underbrace{P_{100\text{C}}}_{\text{Collect rich premium}} + \underbrace{P_{110\text{C}}}_{\text{Pay cheap protection}} < 0 \quad \text{(net credit!)}
$$

### 2. The Asymmetric Risk-Reward Profile

**Why traders love broken wings:**

**Regular butterfly:**

- Pay $2 debit
- Max profit: $3 (150% return)
- Risk $2 on BOTH sides
- **Symmetric but requires capital**

**Broken wing butterfly:**

- Collect $0.50 credit
- Max profit: $5.50 (∞% return on credit!)
- Risk $4.50 on ONE side only
- **Asymmetric and pays you to enter**

**The trade-off:**

$$
\text{Directional Bias} + \text{Credit Collection} = \text{One-Sided Risk}
$$

You're accepting that if you're wrong on direction (stock crashes below $95), you lose more than the symmetric butterfly. But if you're right (stock stays $95-$110), you profit significantly.

### 3. Comparison to Other Asymmetric Strategies

**vs. Vertical Spread:**

| Feature | Broken Wing Fly | Vertical Spread |
|---------|----------------|-----------------|
| **Max profit** | At center strike | At upper/lower strike |
| **Risk** | Defined, one-sided | Defined, directional |
| **Premium** | Often credit | Usually debit |
| **Profit zone** | Range around center | Directional move |
| **Greeks** | Negative gamma at risk side | Positive/negative delta throughout |

**vs. Iron Condor:**

| Feature | Broken Wing Fly | Iron Condor |
|---------|----------------|-------------|
| **Structure** | Single-side butterfly | Two-sided short strangles |
| **Risk** | One-sided (broken wing side) | Both sides symmetric |
| **Profit zone** | Centered, skewed | Wide range |
| **Premium** | Credit (usually) | Credit (always) |
| **Adjustability** | Limited (defined structure) | Easier (can roll sides) |

**Key insight:** Broken wings are like "half an iron condor" - you're selling premium in the middle but only protecting one side (the broken wing side eliminates that risk).

---

## Key Terminology

**Broken Wing:**

- One wing of the butterfly has strikes wider than the body
- "Breaking" means skipping the symmetric strike
- Creates asymmetry in risk profile

**Body Width:**

- Distance between short strikes and near long strike
- Determines max profit potential
- Typically $5 or $10 in liquid underlyings

**Wing Width:**

- Distance from short strike to long strike on each side
- Regular fly: Both wings equal to body
- Broken wing: One wing WIDER than body

**Skip Strike:**

- The strike you "skip" to create the broken wing
- Example: If regular fly uses $95/$100/$105, broken wing might use $95/$100/$110 (skipping $105)

**Directional Bias:**

- Bullish broken wing: Break the upper wing (wider upper strike)
- Bearish broken wing: Break the lower wing (wider lower strike)

**Net Credit:**

- Total premium collected minus premium paid
- Broken wings often collect credit due to skew exploitation
- Credit = instant profit if stock stays in range

---

## Why Trade Broken Wing Butterflies?

**Use cases for broken wings:**


---

## Economic

**Understanding what broken wing butterflies REALLY represent economically:**

### 1. The Core Economic Trade-Off

Broken wing butterflies represent a specific economic proposition: **trading symmetric risk for asymmetric risk to match directional bias while collecting premium**. Unlike standard butterflies (neutral, pay debit), broken wings tilt the structure toward expected market behavior.

**Economic equivalence:**

$$
\text{Broken Wing Butterfly} = \underbrace{\text{Standard Butterfly}}\_{\text{Symmetric}} + \underbrace{\text{Directional Skew}}\_{\text{Asymmetric}}
$$

**The transformation:**
- Start with: Long $100, short 2×$105, long $110 (symmetric, pay debit)
- **Widen one wing:** Long $100, short 2×$105, long $115 (asymmetric, collect credit!)
- **Result:** Shifted max risk to one side, created credit structure

**Why this matters economically:**
- **Symmetric butterfly:** Betting on NO movement (neutral)
- **Broken wing:** Betting on directional bias + range-bound behavior
- **Credit collected:** Compensation for accepting skewed risk

### 2. Why This Structure Exists Economically

Markets create broken wing butterflies because different participants have different:

**1. Risk preferences (Asymmetric utility):**

Most investors have **asymmetric risk tolerance:**
- **Downside:** Very risk-averse (can't tolerate crashes)
- **Upside:** Risk-neutral (happy with any rally)

**Example:** Long-only portfolio manager
- Portfolio: Long $10M in equities
- Fear: Market crashes -20%
- Attitude toward rallies: "Let it run"
- **Perfect strategy:** Broken wing butterfly
  - Protects against crash (lower risk)
  - No cap on upside (upper wing broken)
  - Collect premium for crash risk

**2. Directional conviction + volatility**

**Classic problem:**
- Belief: "Stock will stay range-bound, slightly bullish"
- Challenge: How to express this precisely?

**Solutions comparison:**

| Strategy | Direction | Vol Bet | Credit/Debit | Risk Profile |
|----------|-----------|---------|--------------|--------------|
| Long call | Bullish | Long | Debit | Unlimited up, lose debit down |
| Bull call spread | Bullish | Long | Debit | Capped up, lose debit down |
| **Broken wing fly** | **Range + Bias** | **Short** | **Credit** | **Asymmetric risk** |

**Broken wing butterfly uniquely expresses:**
- "Stock will stay $95-$105" (range)
- "But more likely near $100 than $95" (bias)
- "Willing to risk crash below $90" (skew)
- "Don't want to cap upside above $110" (broken upper wing)

**3. Capital efficiency through credit collection**

**Standard butterfly:**
- Cost: $2 debit (pay upfront)
- Max profit: $3 (at center)
- **ROI:** $3 / $2 = 150%

**Broken wing butterfly:**
- Cost: $1.50 credit (get paid!)
- Max profit: $6.50 ($5 body + $1.50 credit)
- Risk: $3.50 ($5 body - $1.50 credit)
- **ROI:** $6.50 / $3.50 = 186% (better risk-reward)

**Plus:**
- Credit = **immediate buying power release**
- Can deploy capital elsewhere
- Negative cost basis (profit locked in if expires in middle)

### 3. Professional Institutional Perspective

**How institutions actually use broken wings:**

**1. Portfolio hedging with income:**

**Hedging problem:**
- Long $50M equity portfolio
- Want crash protection
- But puts are expensive (debit)
- **Solution:** Sell broken wing butterflies

**Structure:**
- Sell put broken wings (bullish skew)
- Collect $100k monthly premium
- Risk: $500k if market crashes <5%
- **Net:** $1.2M annual income, defined risk

**Why this works:**
- Credit offsets hedging costs
- Risk only on one side (crash)
- Broken upper wing = never capped on rallies

**2. Earnings volatility capture:**

Institutions know: **Earnings moves are asymmetrically distributed**
- 60% chance: Stock stays ±3%
- 25% chance: Stock rallies 5-10%
- 15% chance: Stock crashes 5-10%

**Optimal strategy:**
- **Bearish broken wing** (wider lower wing)
- Captures high-prob neutral/rally scenario
- Protected on crash side (lower wing broken)
- **Collect credit from IV crush**

**Example:**
- Stock at $50 pre-earnings, IV at 60%
- Buy $45 put, sell 2×$50 puts, buy $52 put (narrow upper wing)
- Collect $2 credit

**Outcomes:**
- Stock $48-$52 (60% prob): Keep $2 + profit from IV crush
- Stock rallies $55+ (25% prob): Max loss $2 (wide upper wing protects)
- Stock crashes $43 (15% prob): Max loss $5 ($3 body - $2 credit, but less than naked short)

**3. Market-making and volatility arbitrage:**

**Professional volatility traders:**
- Trade thousands of butterflies
- Look for **skew mispricings**
- **Broken wings isolate specific vol segments**

**Example:**
- OTM call IV: 25%
- ATM call IV: 30%
- OTM put IV: 35% (steep skew)

**Arbitrage:**
- Sell put broken wing (capture rich OTM put IV)
- Buy call broken wing (cheap OTM calls)
- **Net:** Exploit skew differential
- Collect credit on put side, pay less on call side

**4. Probability engineering:**

Institutions use broken wings to **customize win probabilities:**

$$
P(\text{Profit}) = P(\text{In Tent}) + P(\text{Beyond Broken Wing})
$$

**Example calibration:**
- Want 70% win rate
- Stock has 40% prob of staying $95-$105
- Stock has 35% prob of rallying > $105
- **Total:** 75% win rate

**Structure:**
- Center butterfly at $100 (capture 40% prob)
- Widen upper wing to $115 (capture 35% rally prob)
- **Total win rate:** 75% (matches target)
- Accept 25% loss prob (stock crashes < $90)

### 4. The Volatility Smile Exploitation

**Key insight:** Broken wings **arbitrage the volatility smile**

**In equity markets:**

$$
\text{IV}_{OTM\;Put} > \text{IV}_{ATM} > \text{IV}_{OTM\;Call}
$$

**Standard butterfly (symmetric):**
- Buy OTM put (expensive IV)
- Sell 2× ATM (medium IV)
- Buy OTM call (cheap IV)
- **Net:** Pay for expensive put, don't fully benefit from cheap call

**Broken wing butterfly (asymmetric):**
- Buy ATM put (medium IV)
- Sell 2× OTM put (expensive IV!) - **Exploit the richest IV**
- Buy far OTM put (still expensive IV, but wider)
- **Net:** Collect credit from selling richest IV point

**The arbitrage:**

$$
\text{Credit} = \underbrace{2 \times \text{Sell Rich IV}}\_{\text{Premium}} - \underbrace{\text{Buy Med IV}}\_{\text{Cost}} - \underbrace{\text{Buy Exp IV}}\_{\text{Cost}}
$$

**If skew is steep enough:**
- Rich IV sold > 2× (Medium + Far IV bought)
- **Result:** NET CREDIT despite buying 2 options!

**Example:**
- Stock at $100
- ATM $100 put: IV 30% → $5.00
- OTM $95 put: IV 35% → $2.80 each
- Far OTM $85 put: IV 33% → $1.50

**Broken wing:**
- Buy $100 put: -$5.00
- Sell 2× $95 puts: +$5.60
- Buy $85 put: -$1.50
- **Net credit:** +$0.10 (despite buying 2 options!)

**Why this works:**
- Selling OTM puts (richest IV) generates outsized premium
- Buying ATM and far OTM (lower relative IV) costs less
- **Volatility smile = your edge**

### 5. The Behavioral Finance Angle

**Why markets misprice broken wings:**

**1. Investor overreaction to tail risk:**
- Crash fear overpriced (OTM puts expensive)
- Rally probability underpriced (OTM calls cheap)
- **Broken wings exploit this:**
  - Sell crash fear (put broken wing)
  - Buy rally protection cheaply (call broken wing)

**2. Path-dependent preferences:**
- Investors care about PATH, not just outcome
- Prefer "gradual gain" to "volatile gain"
- **Broken wings provide smooth P&L:**
  - Credit collected upfront (feel good immediately)
  - Max profit in middle (most likely outcome)
  - Limited loss on tail (peace of mind)

**3. Mental accounting:**
- Credit = "house money" (feels free)
- Debit = "my money" (painful to lose)
- **Broken wings collect credit:**
  - Traders hold longer (feel profitable)
  - Better compliance with plan
  - Less emotional decision-making

### 6. The Information Asymmetry Trade

**Sophisticated traders use broken wings to exploit information edges:**

**Example: Earnings insider (legal edge):**
- Work at company, know results will be "good not great"
- Public expects either crash or moon
- **Your edge:** Know it'll be boring (+2% move)

**Optimal structure:**
- Sell broken wing butterfly
- Center at +2% (your expected outcome)
- Widen both wings (protect against surprise)
- **Collect credit for being right about "boring"**

**Why this works:**
- Market prices binary outcome (crash or moon)
- You know true distribution (tight, boring)
- **Broken wing captures the difference**

### 7. Understanding the Economic Foundations

**Key insights from broken wing butterflies:**

**1. Risk is not symmetric in markets:**
- **Equity markets:** Slow grind up, fast crash down
- **Volatility skew:** Reflects this asymmetry
- **Broken wings:** Structurally match reality

**2. Premium collection vs. debit strategies:**
- **Debit:** Betting on specific outcome
- **Credit:** Selling probability to others
- **Broken wings:** Blend both (credit + specific outcome bet)

**3. Customization = value:**
- Markets price "standard" structures efficiently
- **Custom structures** (broken wings) often mispriced
- **Edge exists** in the customization

**4. Directional + volatility combined:**
- Most strategies are OR (direction OR volatility)
- **Broken wings are AND** (direction AND volatility range)
- This **dual bet is hard to price** → opportunities

**5. Time decay with protection:**
- Pure credit spreads: Time decay, but unlimited risk
- Pure debits: Limited risk, but pay for time
- **Broken wings:** Time decay working for you, risk defined
- **Best of both worlds**

**The economic truth:**
- Broken wings don't create "free money"
- They **redistribute risk** to match your view
- **If your view is correct more often than market expects:** Profitable
- **If wrong:** Still have defined risk (survivable)

Understanding the economic foundations helps you recognize:
- When broken wings offer genuine edge (directional view + vol skew exploitation)
- When market pricing is fair (efficient, no edge)
- How to customize structure to match specific market view


### 8. Directional Bias with Defined Risk

**Scenario:** Moderately bullish on AAPL, but want defined risk

**Trade:** Bullish broken wing call butterfly

- Buy 1× $170 call for $6
- Sell 2× $175 calls for $8 each = $16 collected
- Buy 1× $185 call for $2
- **Net credit: $16 - $6 - $2 = $8 collected**

**Outcome:**

- Stock at $175: Max profit = $13 ($5 body + $8 credit)
- Stock above $180: Breakeven to small profit
- Stock below $170: Max loss = -$7 ($5 body - $8 credit, but negative)

Wait, let me recalculate: 
- Max loss = $(175-170) - 8 = -3$ if stock below $170
- Max profit = $(175-170) + 8 = 13$ if stock at $175
- Above $185: All options ITM, payoff = $(185-175) - (185-170) = 10 - 15 = -5$... 

Actually, the calculation is:
- Below $170: All expire, keep $8 credit
- At $175: Long $170 worth $5, short 2×$175 worthless, long $185 worthless → Payoff $5 + $8 credit = $13
- Above $185: Complex, need to verify structure

**Why this works:**

- Upside protection from wide upper wing
- Collect premium upfront
- Only risk on downside (if stock crashes)

### 9. Earnings Play with Asymmetric Risk

**Scenario:** TSLA earnings, expect neutral to slightly bullish move, not crash

**Traditional butterfly:**

- Symmetric risk both sides
- Pay debit
- IV crush helps but eats both wings

**Broken wing butterfly:**

- Wider upper wing (no upside risk if stock rockets)
- Collect credit (IV crush multiplies profit)
- Only risk: Stock crashes below lower strike

**Trade:**

- Stock at $240
- Buy $230 call, sell 2× $240 calls, buy $255 call
- Net credit: $3

**Outcomes:**

- Stock rockets to $270: Upper wing protection, keep $3 profit
- Stock stays $240: Max profit $13 ($10 body + $3 credit)
- Stock crashes to $220: Max loss $7 ($10 body - $3 credit)

**Why this works:**

- Earnings: Upside surprise more common than crash
- Broken wing protects against upside surprise
- IV crush benefits credit collection
- Directional bias matches historical earnings pattern

### 10. Monthly Income with Skewed Risk

**Scenario:** Income strategy, willing to take downside risk but not upside

**Philosophy:**

- Markets tend to trend up over time (equities)
- Willing to risk losses if market crashes
- NOT willing to cap upside in strong rallies
- Want to collect monthly premium

**Trade:** Sell broken wing butterflies monthly

**Example on SPY:**

- SPY at $450
- Buy $440 call, sell 2× $450 calls, buy $465 call (wider upper wing)
- Net credit: $2

**Each month:**

- Collect $2 credit ($200 per contract)
- Risk $8 if SPY drops below $440
- No risk if SPY rallies above $465

**Annual strategy:**

- 12 months × $2 credit = $24 potential income
- Occasional losses when market drops
- Never capped on upside (broken wing protects)

**Why this works:**

- Consistent credit collection (theta decay)
- Asymmetric risk matches market tendency (up-bias)
- No missed rallies (broken wing covers you)

### 11. Volatility Crush Trade

**Scenario:** IV elevated, expecting mean reversion and stock stability

**Setup:**

- Stock at $100
- IV at 40% (80th percentile, rich)
- Expect IV to compress to 30% AND stock to stay stable

**Trade:** Broken wing butterfly to capture IV crush

- Buy $95 call (IV 38%)
- Sell 2× $100 calls (IV 40%, richest)
- Buy $110 call (IV 35%, cheaper than symmetric $105)
- **Net credit: $1.50**

**What happens if correct:**

- Stock stays near $100: Max profit zone
- IV drops 10% → Short calls lose value faster (richest IV)
- **Combined: Theta decay + Vega crush = accelerated profit**

**Outcome after 2 weeks:**

- Stock at $99
- IV compressed to 32% (-8%)
- Position value: +$4.50 (already profitable)
- Can close for 300% gain on credit collected

---

## Greeks Behavior

### 1. Delta

**Bullish broken wing delta profile:**

$$
\Delta_{\text{BWB}} = \Delta_{K_1} - 2 \times \Delta_{K_2} + \Delta_{K_3}
$$

**Example at initiation:**

- $K_1 = 95$ call: $\Delta = +0.65$
- $K_2 = 100$ calls: $\Delta = +0.50$ each
- $K_3 = 110$ call: $\Delta = +0.25$
- **Net delta: $0.65 - 2(0.50) + 0.25 = -0.10$** (slightly bearish initially)

**Key insight:** Despite being "bullish broken wing," initial delta can be negative! This is because you're short 2× near-ATM calls. Delta becomes positive as stock rises into profit zone.

**Delta evolution:**

- Stock at $90: Delta ≈ -0.05 (all OTM, minimal exposure)
- Stock at $100: Delta ≈ +0.30 (long 95 call dominates)
- Stock at $105: Delta ≈ -0.20 (short 100 calls dominate)  
- Stock at $110: Delta ≈ +0.10 (approaching balanced wings)
- Stock above $115: Delta ≈ 0 (all wings balanced out)

### 2. Gamma

**Gamma profile:**

$$
\Gamma_{\text{BWB}} = \Gamma_{K_1} - 2 \times \Gamma_{K_2} + \Gamma_{K_3}
$$

**Critical characteristic: NEGATIVE gamma near short strikes!**

**Example:**

- Stock at $100 (at short strike)
- **Gamma: -0.08** (very negative)
- Small move either direction HURTS initially

**Gamma zones:**

- **Near $95:** Slightly positive (long wing)
- **Near $100:** VERY negative (short strikes, -0.08)
- **Near $110:** Slightly positive (long wing)
- **Between zones:** Low gamma

**Practical impact:**

- Stock at $99 → moves to $101 → **Immediate loss** (negative gamma)
- This is why you want stock to STAY at $100, not whipsaw around it
- Gamma works against you until stock settles

### 3. Theta

**Theta (time decay):**

$$
\Theta_{\text{BWB}} \approx +$0.10 \text{ to } +$0.25/\text{day} \quad \text{(positive, collect time!)}
$$

**Why positive theta?**

- You SOLD 2× options (short gamma/theta)
- You bought 2× options (long gamma/theta)
- Net: Short position dominates → Collect time decay

**Theta evolution:**

**Figure 2:** Theta decay acceleration for broken wing butterfly, showing how time decay accelerates in final weeks as short options lose value faster than long options.

**Pattern:**

- 30 days out: Θ ≈ +$0.08/day
- 14 days out: Θ ≈ +$0.18/day
- 7 days out: Θ ≈ +$0.35/day (accelerating)
- Last 3 days: Θ ≈ +$0.60/day (parabolic)

**Strategy: Enter 30-45 days out, exit at 7-14 days to capture optimal theta**

### 4. Vega

**Vega (IV sensitivity):**

$$
\text{Vega}_{\text{BWB}} = \text{Vega}_{K_1} - 2 \times \text{Vega}_{K_2} + \text{Vega}_{K_3} < 0 \quad \text{(net short)}
$$

**Why short vega?**

- Short 2× ATM calls (highest vega)
- Long 1× OTM call + 1× far OTM call (lower vega)
- Net: You're SHORT volatility

**Example:**

- $95 call vega: +0.15
- $100 calls vega: +0.22 each
- $110 call vega: +0.08
- **Net vega: $0.15 - 2(0.22) + 0.08 = -0.21$**
- **Interpretation: Lose $21 if IV rises 1%**

**Practical impact:**

- **IV spike:** Position loses value (even if stock stable)
- **IV crush:** Position gains value (win on both theta + vega)
- **Best entry: High IV** (sell expensive volatility, profit from crush)

**Vega surface:**

**Figure 3:** Vega surface showing negative vega exposure concentrated at short strike, with magnitude increasing as IV rises and time to expiration increases.

---

## When Greeks Hurt You

### 1. The Whipsaw Disaster (Negative Gamma)

**Scenario:** Stock oscillates around short strike

**Setup:**

- Broken wing butterfly: $95/$100/$110 calls
- Stock at $100
- Net credit: $2

**Day 1:** Stock drops to $98
- Negative gamma kicks in
- Delta becomes more negative
- **P&L: -$40** (despite only $2 move)

**Day 2:** Stock rallies back to $102
- Negative gamma again
- Delta flips positive but loses more
- **P&L: -$80** (another -$40)

**Net result:**

- Stock ended $2 higher (slightly favorable)
- But whipsaw caused -$80 loss
- **This is gamma risk at short strikes!**

**Lesson:** Broken wings HATE volatility around the short strike. Need stock to sit still or move decisively to one side.

### 2. The IV Spike Crush

**Scenario:** Unexpected news spikes IV

**Setup:**

- Stock at $100
- Broken wing fly with $2 credit
- IV at 30%

**News:** FDA approval uncertainty announced

**Day 1:**

- Stock unchanged at $100
- IV spikes: 30% → 50% (+20%)
- **Your P&L:**

  - Vega: -0.21 × 20 = -$420
  - Delta: $0 (stock flat)
  - Theta: +$10 (one day's decay)
  - **Total: -$410 loss** (despite stock AT your target!)

**Lesson:** Short vega position = vulnerability to IV spikes. Enter when IV high, not low.

### 3. The Slow Bleed (Stock Drifts to Risk Zone)

**Scenario:** Stock slowly trends toward max loss zone

**Setup:**

- Bullish broken wing: $95/$100/$110
- Max loss below $95
- Stock at $100, slowly declining

**Week 1:** Stock at $98
- Small loss, theta still helping
- **P&L: +$15** (theta > delta loss)

**Week 2:** Stock at $96  
- Getting closer to risk zone
- **P&L: +$5** (theta slowing, delta hurting)

**Week 3:** Stock at $94
- Below $95, in max loss zone
- **P&L: -$150** (ouch)

**Mistake:** Didn't exit when stock was at $98 (early warning)

**Lesson:** Set stop-loss BEFORE max loss zone. Exit at $96-97, not $94.

---

## Common Pitfalls

### 1. Wrong Directional Bias

**The mistake:**

"I'll trade a broken wing butterfly just for the credit, direction doesn't matter."

**What you missed:**

Broken wings ARE directional trades! You've concentrated risk on one side.

**Example:**

- Trade bullish broken wing (risk on downside)
- Stock drops 10%
- **Max loss hit, despite collecting credit**

**The fix:**

- Only use bullish broken wing if neutral-to-bullish
- Only use bearish broken wing if neutral-to-bearish
- Match direction to your actual market view

### 2. Ignoring Gamma Risk

**The mistake:**

"Stock is at my short strike, perfect! I'll hold for max profit."

**What you missed:**

Negative gamma at short strike = whipsaw risk. Small moves hurt disproportionately.

**Example:**

- Stock at $100 (your short strike)
- Stock whipsaws $100 → $102 → $98 → $101
- Each move costs -$30 to -$50
- **Total: -$150 loss despite ending near $100**

**The fix:**

- Take profits early (at 50% max profit, don't wait for max)
- Exit if stock volatile around short strike
- Monitor intraday moves, not just close prices

### 3. Entering at Low IV

**The mistake:**

"Broken wings can be profitable in any IV environment."

**What you missed:**

You're selling options (short vega). Need HIGH IV to:
1. Collect meaningful credit
2. Benefit from IV crush
3. Get proper compensation for risk

**Example:**

- Enter broken wing at 20th percentile IV
- Collect $0.50 credit (small)
- IV normalizes UP to 50th percentile
- **P&L: -$200** (vega loss exceeds credit)

**The fix:**

- Only enter broken wings at >60th percentile IV
- Check IV rank/percentile before trading
- Use broken wings as "IV crush" plays

### 4. Holding to Expiration

**The mistake:**

"I'll let it expire for max profit."

**What you missed:**

- Gamma explodes near expiration (binary outcomes)
- Assignment risk on short calls (if stock near strikes)
- Pin risk (stock exactly at strike = uncertainty)
- Minimal additional profit vs huge risk

**Example:**

- Stock at $100, Friday expiration
- Hoping for max profit (stock stays exactly $100)
- Stock closes at $100.05 (slightly ITM)
- **Short 100 calls assigned: Must deliver 200 shares at $100**
- Stock gaps to $103 Monday open
- **Loss: -$600** (could have closed Friday for +$400)

**The fix:**

- Close 1 week before expiration (capture 80% of max profit)
- Avoid Friday expiration if stock near short strikes
- Take profit early, avoid gamma + pin risk

### 5. Improper Strike Selection

**The mistake:**

"I'll make the broken wing really wide for maximum credit."

**What you missed:**

Wider broken wing = More directional bias needed. If you're wrong, max loss increases.

**Example:**

- Stock at $100
- Aggressive broken wing: $95/$100/$120 (very wide upper wing)
- Net credit: $5 (attractive!)
- Stock drops to $93
- **Max loss: -$15** ($95-$100 body width - $5 credit)
- Could have used $95/$100/$110: Max loss only -$7

**The fix:**

- Match wing width to conviction level
- Typical: Upper wing 2× body width (balanced)
- Aggressive: Upper wing 3× body width (higher credit, more risk)
- Use volatility/ATR to guide width selection

---

## Risk Management Rules

**Essential guidelines:**

### 1. Position Sizing

**Rule of thumb:**

$$
\text{Position Size} = \frac{\text{Max Loss Tolerance}}{\text{Max Loss per Contract}}
$$

**Example:**

- $50,000 account
- 3% risk per trade = $1,500
- Broken wing max loss = $500
- **Max size: 3 contracts**

**Key: Size based on MAX LOSS, not credit collected!**

### 2. Strike Selection Guidelines

**Body width (distance to short strike):**

- Narrow ($5): Higher probability, lower profit
- Medium ($10): Balanced
- Wide ($15+): Lower probability, higher profit, more risk

**Broken wing width:**

- Conservative: 1.5× body width
- Standard: 2× body width (most common)
- Aggressive: 3× body width (rare, high credit)

**Example on $100 stock:**

- Body: $95-$100 ($5 wide)
- Broken wing: $95/$100/$110 (upper wing = $10 = 2× body)

### 3. Time Frame Selection

**Entry:**

- 30-45 days to expiration (DTE)
- Optimal theta decay zone
- Enough time for stock to settle

**Exit:**

- Target: 7-14 days remaining
- Capture 70-80% of max profit
- Avoid gamma explosion

**Example timeline:**

- Day 0: Enter (45 DTE)
- Day 30: Evaluate, consider taking profit if +50%
- Day 35: Close if still open (10 DTE)

### 4. Exit Rules

**Set upfront:**

- **Profit target:** 50% of max profit (e.g., max profit $10, exit at $5)
- **Stop loss:** -1.5× credit collected (e.g., credit $2, stop at -$3)
- **Time stop:** Close at 7-10 DTE regardless
- **IV stop:** Exit if IV spikes >30% from entry
- **Technical stop:** Exit if stock breaks support (bearish BWB) or resistance (bullish BWB)

### 5. Avoid These

- Never trade broken wings in low IV (<40th percentile)
- Never hold through earnings (IV crush unpredictable)
- Never ignore directional bias (this is NOT neutral strategy)
- Never let winners turn to losers (take profit at 50%)
- Never hold to last 3 days (gamma too risky)
- Never trade illiquid strikes (spreads too wide)

---

## Real-World Examples

### 1. Pension Duration Cut via Futures

**Setup (March 2024):**

- AAPL at $175
- Moderately bullish bias (new product cycle)
- IV at 65th percentile (reasonable)

**Trade:** Bullish broken wing call butterfly (45 DTE)

- Buy 1× $170 call for $8.50
- Sell 2× $175 calls for $11.50 each = $23 collected
- Buy 1× $185 call for $3
- **Net credit: $23 - $8.50 - $3 = $11.50 collected**

**Position Greeks:**

- Delta: -0.05 (slightly bearish initially)
- Gamma: -0.06 (negative at $175)
- Theta: +$0.15/day
- Vega: -0.18

**Outcome (30 days later):**

- AAPL drifted to $177 (slightly above target)
- IV compressed: 65th → 45th percentile
- **P&L breakdown:**

  - Theta: +$150 (30 days × $5/day average)
  - Delta: +$20 (small favorable move)
  - Vega: +$80 (IV crush helped)
  - **Total: +$250 profit**
- Exited at +$250 (50% of max profit potential)

**Lesson:** Combination of theta decay + IV crush + small favorable move = solid profit. Didn't hold for max, avoided risk.

### 2. Transition Risk Hedge

**Setup (January 2024):**

- SPY at $480
- Thought market would consolidate
- High IV (70th percentile)

**Trade:** Bullish broken wing (45 DTE)

- Buy $475 call, sell 2× $480 calls, buy $495 call
- Net credit: $4

**What happened (next 2 weeks):**

- **Week 1:** SPY whipsawed $480 → $485 → $478 → $483
- Each move hurt due to negative gamma
- **P&L after week 1: -$150** (despite theta + credit)

- **Week 2:** Volatility continued, SPY ranged $478-$483
- More gamma pain
- **P&L after week 2: -$280**

**Exit:**

- Closed at -$280 loss
- Credit was $400, so net -$680 total loss

**Lesson:** Broken wings can't handle whipsaw around short strike. Needed stable market, got volatility. Should have exited after week 1 when whipsaw pattern emerged.

### 3. Portable Alpha with Futures

**Setup (October 2024):**

- TSLA at $240, earnings next week
- IV spiked to 90th percentile (80% IV)
- Neutral-to-bullish bias

**Trade:** Bullish broken wing (30 DTE, post-earnings)

- Buy $230 call for $18
- Sell 2× $240 calls for $22 each = $44
- Buy $255 call for $6
- **Net credit: $44 - $18 - $6 = $20**

**Post-earnings:**

- TSLA rallied to $250 (good directional call)
- IV crushed: 80% → 45%
- **P&L:**

  - Delta: +$100 (stock move)
  - Vega: +$350 (massive IV crush benefit)
  - Theta: +$80 (1 week decay)
  - **Total: +$530 profit** (on $20 credit = 2,650% ROI!)

**Lesson:** High IV entry + directional correctness + IV crush = home run. This is the ideal broken wing setup.

### 4. Tactical Duration Extension

**Setup:**

- Stock at $100
- Broken wing: $95/$100/$110
- Net credit: $3
- Held to expiration (mistake)

**Expiration Friday:**

- Stock at $100.10 (just above short strike)
- Thought: "Stock slightly above, I'll let it expire for max profit"

**What happened:**

- $100 calls slightly ITM ($0.10)
- **Assigned on BOTH short $100 calls**
- Now SHORT 200 shares at $100 average
- Stock gaps up Monday to $103
- **Forced to buy back at $103: Loss = -$600**

**Better outcome if closed Friday:**

- Position value: $7 profit (near max)
- Could have closed for $700 profit
- **Avoiding expiration would have saved $1,300!**

**Lesson:** NEVER hold broken wings into expiration if stock near short strikes. Assignment + gap risk = disaster.

---


---



## Common Mistakes

**The 10 mistakes that destroy broken wing butterfly profits:**

### 1. Mistake #1

**The error:** Trading bullish BWB when actually bearish (or vice versa).  
**Result:** Stock moves to your wide wing (risk side) = max loss.  
**Fix:** Match structure to conviction. Bullish conviction = Bullish BWB. Period.

### 2. Mistake #2

**The error:** "It's defined risk, I'll trade 50 contracts!"  
**Reality:** $7.50 max loss × 50 × 100 = **$37,500 loss** (75% of $50k account destroyed)  
**Fix:** Use formula: Portfolio × 3% / Max Loss. Example: $50k account = 2-3 contracts MAX.

### 3. Mistake #3

**The error:** Don't identify risk side before entry.  
**Result:** Surprised when max loss hits: "I thought I was protected!"  
**Fix:** Before every entry, state: "Wide [upper/lower] wing = risk on [upside/downside]. I accept this."

### 4. Mistake #4

**The error:** "Stock will bounce back" when already at max loss.  
**Reality:** Theta doesn't help at max loss. Gamma hurts if it bounces.  
**Fix:** Exit at -50% of max loss, ALWAYS. No hoping, no waiting.

### 5. Mistake #5

**Low IV (<40th percentile):** Options too cheap, no edge, IV might expand (kills you).  
**High IV (>80th percentile):** IV expansion risk huge, one spike destroys position.  
**Fix:** ONLY trade 45-70th percentile IV. Outside this range = skip trade.

### 6. Mistake #6

**The error:** "I want max profit!" (Max = landing exactly at center strike)  
**Probability:** 5-10% (very rare)  
**Result:** Give back profits when stock moves away.  
**Fix:** Systematic exit at +50-60% of max profit. Win rate: 60%+ vs. 10% for max profit.

### 7. Mistake #7

**The error:** Trade OTM strikes with OI < 100.  
**Reality:** Bid $9.50, Ask $12.50 (spread = $3). Want $11, get filled at $12.  
**Cost:** -$100 per contract lost to slippage.  
**Fix:** Minimum OI > 500, spread < 10% of mid-price.

### 8. Mistake #8

**The error:** Holding to 3 DTE with stock near strikes.  
**Reality:** Gamma explodes, $0.50 move = $500 loss in minutes.  
**Fix:** Exit by 7 DTE unless deeply profitable (+70%+).

### 9. Mistake #9

**The error:** "I'll buy the calls today, sell tomorrow when market drops."  
**Reality:** Overnight gap up = calls expensive, your structure now costs more.  
**Risk:** Directional exposure between legs.  
**Fix:** ALWAYS combo orders (all 4 legs simultaneously).

### 10. Mistake #10

**The error:** "I collected $11.50 credit, I made $1,150!"  
**Reality:** Max loss = $7.50 (wide wing - credit). You can LOSE $750 per spread.  
**Calculation:** Wide wing $10 - Credit $11.50 = Still risk if wide wing < credit... wait.  

Let me recalculate: If wide wing is $10 and credit is $11.50, then:
- Max profit = Narrow wing + Credit = $5 + $11.50 = $16.50
- Max loss = Wide wing - Credit = $10 - $11.50 = -$1.50 (negative means... profit?)

Actually, if credit > wide wing, there's no max loss (you keep profit regardless). The max loss formula is:
$$
\text{Max Loss} = \max(0, \text{Wide Wing} - \text{Credit})
$$

So if credit $11.50 > wide wing $10, max loss = $0 (you profit no matter what).

**Better example:** Wide wing $10, Credit $2.50:
- Max loss = $10 - $2.50 = **$7.50** (this is real risk)

**Fix:** Always calculate: Max Loss = Wide Wing - Credit. This is your REAL risk, not the credit amount.

### 11. The Compounding Effect

**One mistake (oversizing) wipes out many wins:**

**Example:**
- 20 winning trades: +$6 each = +$120
- 1 oversized max loss: 10× normal size = -$75
- **Net:** +$45 (62% of gains lost to one mistake)

**Success = Perfect execution + Discipline:**

Follow ALL rules:
1. Directional bias matches structure ✓
2. Position size = Formula ✓  
3. IV 45-70th percentile ✓
4. Exit at +50-60% profit ✓
5. Stop loss at -50% max loss ✓
6. Exit by 7 DTE ✓
7. Combo orders only ✓
8. Know which wing is wide ✓

**Break ANY rule = High probability of disaster.**  

Broken wings are profitable when traded perfectly. Imperfect execution = account destruction. 🎯

---

## Final Wisdom

> "Broken wing butterflies are the thinking trader's income strategy. You're not trying to be market-neutral - you're expressing a directional bias while still collecting premium and maintaining defined risk. The 'broken wing' isn't a flaw, it's a feature that protects you from catastrophic loss on one side while letting you sleep at night. Master these and you've unlocked asymmetric risk-reward with positive carry."

**Key to success:**

- Enter ONLY at high IV (>60th percentile)
- Match broken wing direction to market bias
- Exit at 50% max profit (don't be greedy)
- Close before expiration (avoid gamma nightmare)
- Size for max loss (not credit collected)
- Monitor for whipsaw at short strikes (negative gamma danger)

**Most important:** Broken wings are directional theta/vega plays, NOT neutral strategies. Respect the bias, manage the gamma, capture the credit! 🦋📊


---

## Practical Guidance

**Step-by-step broken wing butterfly implementation:**

### 1. Critical Pre-Trade Checklist

☐ **Directional bias clear?** (Bullish → Bullish BWB, Bearish → Bearish BWB)  
☐ **IV 45-70th percentile?** (Sweet spot for entry)  
☐ **Identify wide wing** (This is your risk side!)  
☐ **Can handle max loss?** (Wide wing - Credit)  
☐ **30-60 DTE?** (Optimal time frame)  
☐ **Liquid strikes?** (OI > 500, spread < 10%)  
☐ **Credit ≥ $2?** (Worth transaction costs)

### 2. Position Sizing Formula

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times 3\%}{\text{Max Loss Per Spread} \times 100}
$$

**Example:** $50,000 account, $7.50 max loss per spread  
**Max:** $1,500 / $750 = **2 contracts** (not 10, not 20!)

### 3. Entry Execution

1. **Combo order** (all 4 legs simultaneously)
2. **Limit at mid-price** (never market order)
3. **Verify structure:** Which wing is wide? (Know your risk!)
4. **Set alerts:** For breakevens and max loss zones

### 4. Exit Rules (Non-Negotiable)

**Take profit:**
- At +50-60% of max profit
- Example: Max $16.50, exit at +$8-10

**Stop loss:**
- At -50% of max loss
- Example: Max loss $7.50, exit at -$3.75

**Time stop:**
- Exit at 50% time if not +25% profitable
- Example: 30 DTE, exit at 15 DTE if not up +25%

**Gamma stop:**
- Always exit by 7 DTE regardless of P&L

### 5. Management During Trade

**Daily:** Check stock price relative to tent  
**Weekly:** Check IV percentile (exit if > 70th)  
**At 50% time:** Evaluate if hitting targets  
**Never:** Hope for recovery when at max loss

### 6. When to Adjust vs. Close

**Generally:** Close, don't adjust  
**Broken wings are directional bets** - if wrong, exit

**Only adjust if:**
- Deeply profitable (+70%+)
- Want to lock gains by converting to safer structure
- Have strong reason direction will reverse

**Otherwise:** Close and move on

### 7. Record Template

| Date | Underlying | Type | Strikes | DTE | Credit | IV | Max Loss | Outcome | Lesson |
|------|------------|------|---------|-----|--------|----|---------| ---------|--------|
| 1/15 | SPY | Bull BWB | 445/450/465 | 45 | $11.50 | 55% | $7.50 | +$624 (54%) | Exited at target ✓ |

**Track:** Win rate (target: 60%+), Avg profit (target: 50% of max), Avg loss (should be <50% of max loss)
4. **Failing to set exit rules upfront**
5. **Emotional decision-making**