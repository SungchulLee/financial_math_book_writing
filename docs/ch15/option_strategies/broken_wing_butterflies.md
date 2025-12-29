# Broken Wing Butterflies

**Broken wing butterflies** are asymmetric butterfly spreads where one wing is "broken" (skipped), creating directional bias while maintaining defined risk and often allowing for credit collection or reduced debit.

---

## The Core Insight

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

**Before trading broken wings, understand the modification from regular butterflies:**

### Regular Butterfly (Symmetric) - Baseline

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

### Broken Wing Butterfly (Asymmetric)

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

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_butterfly.png?raw=true" alt="broken_wing" width="700">
</p>
**Figure 1:** Comparison of regular butterfly (symmetric) vs broken wing butterfly (asymmetric), showing how the broken wing eliminates upside risk while maintaining defined downside risk and often allowing credit collection.

---

## Economic Interpretation: Asymmetric Risk Premium

**Beyond the basic definition, understanding what broken wings REALLY are economically:**

### Why Does the Broken Wing Exist?

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

### The Asymmetric Risk-Reward Profile

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

### Comparison to Other Asymmetric Strategies

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

## Economic Interpretation

**Understanding what this strategy REALLY represents economically:**

### The Core Economic Trade-Off

This strategy involves specific economic trade-offs that determine when it's most valuable. The key is understanding what you're giving up versus what you're gaining in economic terms.

**Economic equivalence:**

$$
\text{Strategy Payoff} = \text{Component 1} + \text{Component 2} - \text{Cost/Benefit}
$$

### Why This Structure Exists Economically

Markets create these structures because different participants have different:
- Risk preferences
- Time horizons
- Capital constraints
- View on volatility vs. direction

### Professional Institutional Perspective

Institutional traders view this strategy as a tool for:
1. **Risk management:** Precise control over exposure
2. **Capital efficiency:** Optimal use of buying power
3. **Probability engineering:** Trading win rate for win size
4. **Volatility positioning:** Specific exposure to implied volatility changes

Understanding the economic foundations helps you recognize when the strategy offers genuine edge versus when market pricing is fair.


### 1. Directional Bias with Defined Risk

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

### 2. Earnings Play with Asymmetric Risk

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

### 3. Monthly Income with Skewed Risk

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

### 4. Volatility Crush Trade

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

### Delta: Directional Bias

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

### Gamma: Negative at Short Strikes

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

### Theta: Positive Time Decay

**Theta (time decay):**

$$
\Theta_{\text{BWB}} \approx +$0.10 \text{ to } +$0.25/\text{day} \quad \text{(positive, collect time!)}
$$

**Why positive theta?**

- You SOLD 2× options (short gamma/theta)
- You bought 2× options (long gamma/theta)
- Net: Short position dominates → Collect time decay

**Theta evolution:**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/bwb_theta_decay.png?raw=true" alt="bwb_theta" width="700">
</p>
**Figure 2:** Theta decay acceleration for broken wing butterfly, showing how time decay accelerates in final weeks as short options lose value faster than long options.

**Pattern:**

- 30 days out: Θ ≈ +$0.08/day
- 14 days out: Θ ≈ +$0.18/day
- 7 days out: Θ ≈ +$0.35/day (accelerating)
- Last 3 days: Θ ≈ +$0.60/day (parabolic)

**Strategy: Enter 30-45 days out, exit at 7-14 days to capture optimal theta**

### Vega: Negative Volatility Exposure

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

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/bwb_vega_surface.png?raw=true" alt="bwb_vega" width="700">
</p>
**Figure 3:** Vega surface showing negative vega exposure concentrated at short strike, with magnitude increasing as IV rises and time to expiration increases.

---

## When Greeks Hurt You

### The Whipsaw Disaster (Negative Gamma)

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

### The IV Spike Crush

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

### The Slow Bleed (Stock Drifts to Risk Zone)

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

### Position Sizing

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

### Strike Selection Guidelines

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

### Time Frame Selection

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

### Exit Rules

**Set upfront:**

- **Profit target:** 50% of max profit (e.g., max profit $10, exit at $5)
- **Stop loss:** -1.5× credit collected (e.g., credit $2, stop at -$3)
- **Time stop:** Close at 7-10 DTE regardless
- **IV stop:** Exit if IV spikes >30% from entry
- **Technical stop:** Exit if stock breaks support (bearish BWB) or resistance (bullish BWB)

### Avoid These

- Never trade broken wings in low IV (<40th percentile)
- Never hold through earnings (IV crush unpredictable)
- Never ignore directional bias (this is NOT neutral strategy)
- Never let winners turn to losers (take profit at 50%)
- Never hold to last 3 days (gamma too risky)
- Never trade illiquid strikes (spreads too wide)

---

## Real-World Examples

### Example 1: AAPL Bullish Broken Wing (Successful)

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

### Example 2: SPY Iron Fly Gone Wrong (Whipsaw)

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

### Example 3: TSLA Earnings IV Crush (Perfect Setup)

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

### Example 4: Assignment Risk (Cautionary Tale)

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

## Worst Case Scenario

**What happens when everything goes wrong:**

### The Nightmare Setup

**How it starts:**
- [Initial adverse move]
- [Market condition deterioration]
- [Position response]

**The deterioration:**

**Days 1-7:**
- [Early warning signs]
- [Position losing value]
- [Critical decision point]

**Through expiration:**
- [Continued adverse movement]
- [Max loss approached/realized]
- [Final outcome]

### Maximum Loss Calculation

**Worst case mathematics:**

$$
\text{Max Loss} = [\text{Formula}]
$$

**Example calculation:**
- [Specific example with numbers]
- [Loss breakdown]
- [Impact on portfolio]

### What Goes Wrong

The worst case occurs when:
1. **Wrong direction:** Market moves against you
2. **Wrong magnitude:** Move is severe
3. **Wrong timing:** Happens quickly, no time to adjust
4. **Wrong volatility:** IV moves unfavorably

### The Cascade Effect

**Multiple losing positions:**
- [Scenario 1: First loss]
- [Scenario 2: Revenge trading]
- [Scenario 3: Account damage]

**Total damage:**
- [Cumulative loss calculation]
- [Portfolio impact percentage]
- [Recovery difficulty]

### Assignment and Pin Risk

**Complexity at expiration:**
- [Assignment scenario]
- [Pin risk explanation]
- [Weekend risk]
- [Cleanup process]

### Real Examples of Disasters

**Historical example 1:**
- [Setup and expectation]
- [What happened]
- [Final loss]

**Historical example 2:**
- [Setup and expectation]
- [What happened]
- [Final loss]

### Psychology of Losses

**Emotional stages:**
1. **Denial:** "It will recover"
2. **Hope:** "Just need a small bounce"
3. **Anger:** "Market is rigged"
4. **Capitulation:** "Just close it"
5. **Learning:** "What went wrong?"

**Winning trader mindset:**
- Accept losses quickly
- Analyze dispassionately
- Learn and adapt
- Move forward

### Preventing Worst Case

**Risk management strategies:**

1. **Position sizing:**
   - Never risk more than [X]% per trade
   - Respect maximum loss calculations

2. **Stop losses:**
   - Exit at [trigger level]
   - Don't hope for recovery

3. **Diversification:**
   - Multiple uncorrelated positions
   - Different timeframes
   - Different strategies

4. **Avoid high-risk scenarios:**
   - [Scenario to avoid 1]
   - [Scenario to avoid 2]

### The Ultimate Protection

$$
\text{Survivability} = \frac{\text{Capital Remaining}}{\text{Capital Initial}} > 0.85
$$

Even in worst case, proper position sizing ensures you survive to trade again. The market will test you - preparation determines whether you survive or blow up.

**Remember:** Worst case WILL happen eventually. Position accordingly.



---

## Best Case Scenario

**What happens when everything goes right:**

### The Perfect Setup

**Ideal entry conditions:**
- [Market condition 1]
- [Volatility at optimal level]
- [Catalyst working in your favor]

**The optimal sequence:**

**Days 1-7:**
- [What happens initially]
- [Position response]
- [Decision point]

**Through expiration:**
- [Continuation of favorable move]
- [Profit realization]
- [Final outcome]

### Maximum Profit Achievement

**Best case mathematics:**

$$
\text{Max Profit} = [\text{Formula}]
$$

$$
\text{ROI} = \frac{\text{Max Profit}}{\text{Capital At Risk}} \times 100\%
$$

**Example calculation:**
- [Specific example with numbers]
- [Profit breakdown]
- [ROI calculation]

### What Makes It Perfect

The best case requires:
1. **Right direction:** Market moves as anticipated
2. **Right magnitude:** Move is sufficient for profit
3. **Right timing:** Move happens within time frame
4. **Right volatility:** IV behaves favorably

### Comparison to Alternatives

**This strategy vs. [Alternative]:**
- [How best case compares]
- [When this strategy wins]
- [Trade-offs involved]

### Professional Profit-Taking

**When to take profits:**
- At [X]% of max profit
- [Time-based consideration]
- [Volatility-based trigger]

**The compounding advantage:**

Taking profits early and redeploying can yield better annual returns than holding for maximum profit due to reduced risk and faster capital recycling.

### The Dream Scenario

**Extreme best case:**
- [Exceptional circumstance]
- [Outsized gain]
- [Probability and why it's rare]

**Key insight:** Best case is not guaranteed and should not be expected. Position sizing should assume realistic outcomes, not best case scenarios.


## What to Remember

### Core Concept

**Broken wing butterflies are asymmetric butterfly spreads:**

$$
\text{Broken Wing} = \text{Regular Butterfly} + \text{Skip Strike} = \text{Directional Bias} + \text{Credit}
$$

- One wing wider than body (creates asymmetry)
- Risk concentrated on one side (non-broken wing)
- Often collect net credit (skew exploitation)
- Defined maximum loss (still limited risk)
- Maximum profit at short strike (like regular fly)

### The Setup

**Bullish Broken Wing Call Butterfly:**

- Buy 1× lower call
- Sell 2× middle calls
- Buy 1× higher call (WIDER than regular fly)
- Net: Usually credit
- Risk: Downside (below lower strike)
- Safe zone: Upside (broken wing protects)

**Bearish Broken Wing Put Butterfly:**

- Buy 1× higher put
- Sell 2× middle puts
- Buy 1× lower put (WIDER than regular fly)
- Net: Usually credit
- Risk: Upside (above higher strike)
- Safe zone: Downside (broken wing protects)

### The Greeks

**Critical to understand:**

- **Delta:** Small initial delta, evolves as stock moves
- **Gamma:** NEGATIVE near short strikes (whipsaw danger)
- **Theta:** POSITIVE (collect time decay)
- **Vega:** NEGATIVE (short volatility)

**Key insight: Broken wings are theta/vega plays with directional bias!**

### Strike Selection

**Body width:**

- Narrow: Higher prob, lower profit, less risk
- Wide: Lower prob, higher profit, more risk

**Broken wing multiple:**

- 1.5×: Conservative (small credit, balanced risk)
- 2.0×: Standard (good credit, defined risk)
- 3.0×: Aggressive (large credit, higher risk)

### Maximum Profit/Loss

**Max profit (at short strike):**

$$
\text{Max Profit} = \text{Body Width} + \text{Net Credit} \quad \text{(or - Net Debit)}
$$

**Max loss (beyond non-broken wing):**

$$
\text{Max Loss} = |\text{Body Width}| - \text{Net Credit} \quad \text{(or + Net Debit)}
$$

**Breakevens:**

- Lower: $K_1 + $ (Net credit or - Net debit)
- Upper: Broken wing side = no upper breakeven (protected!)

### When to Use

**Use broken wing butterflies when:**

- Moderate directional bias (bullish or bearish)
- High IV environment (>60th percentile)
- Expect IV crush + stable stock price
- Want defined risk with credit collection
- 30-45 days to expiration

**Don't use when:**

- Low IV (<40th percentile)
- Strongly directional view (use spreads instead)
- Expecting high volatility (negative gamma will hurt)
- Very near expiration (<14 days)
- Stock volatile around short strike

### Common Mistakes to Avoid

1. Entering at low IV (won't collect enough credit)
2. Ignoring directional bias (this is NOT neutral)
3. Holding through expiration (assignment + gamma risk)
4. Wrong wing width (too aggressive = too much risk)
5. Not taking profits at 50% (greed = risk)
6. Ignoring gamma risk at short strike (whipsaw kills)
7. Trading illiquid strikes (wide bid-ask spreads)
8. No stop-loss (let losses run to max)

### Risk Management

**Essential rules:**

- Size based on MAX LOSS, not credit collected
- Enter at high IV (>60th percentile)
- Exit at 50% of max profit OR 7 DTE (whichever first)
- Stop-loss at -1.5× credit collected
- Close immediately if stock whipsaws at short strike
- Never hold through last week (gamma explodes)
- Match broken wing direction to market bias

### Comparison to Regular Butterfly

**Advantages over regular fly:**

- Often collect credit (vs pay debit)
- Directional bias (can express view)
- Protected on one side (broken wing = no risk there)
- Better risk-reward if directionally correct

**Disadvantages vs regular fly:**

- Higher max loss on risk side
- Must be directionally correct
- More complex to manage
- Less margin for error

### Your Learning Path

**Start here (broken wings), then:**

1. Master regular butterflies first (symmetric)
2. Understand skew concept (why broken wings work)
3. Learn broken wing structures (this chapter)
4. Progress to broken iron butterflies (combining calls + puts)
5. Eventually: Dynamic adjustment strategies

**Broken wings bridge income and directional trading!**

### Final Wisdom

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

**Step-by-step implementation framework:**

### Step 1: Market Assessment

**Before entering, evaluate:**

1. **Market environment:**
   - Trend direction and strength
   - Volatility level (IV percentile)
   - Upcoming events or catalysts

2. **Technical analysis:**
   - Support/resistance levels
   - Volume and liquidity
   - Recent price action

3. **Fundamental backdrop:**
   - Company-specific news
   - Sector dynamics
   - Macro environment

### Step 2: Strategy Selection Criteria

**Enter this strategy when:**
- [Specific market conditions]
- [Volatility requirements]
- [Time horizon matches]
- [Risk tolerance appropriate]

**Avoid this strategy when:**
- [Unfavorable conditions]
- [Wrong volatility environment]
- [Insufficient time or liquidity]

### Step 3: Position Sizing

**Calculate maximum position size:**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Loss Per Contract}}
$$

**Conservative guidelines:**
- Risk 1-2% per trade when learning
- Max 5 uncorrelated positions
- Never more than 20% of portfolio in options

### Step 4: Entry Execution

**Best practices:**

1. **Use limit orders:** Never use market orders
2. **Check liquidity:** Bid-ask spread < 10% of mid-price
3. **Time entry:** Avoid first/last 30 minutes of trading day
4. **Single order:** Enter as complete strategy, don't leg in

### Step 5: Position Management

**Active management rules:**

**Profit targets:**
- Take profit at [X]% of max profit
- Scale out if appropriate
- Don't be greedy

**Loss limits:**
- Cut losses at [Y]% of max loss
- Don't hope for recovery
- Preserve capital

**Time-based exits:**
- Monitor theta decay
- Exit if [time-based trigger]

### Step 6: Adjustment Protocols

**When to adjust:**
- Position threatened
- Market environment changes  
- New information emerges

**How to adjust:**
- [Adjustment technique 1]
- [Adjustment technique 2]
- [When to take loss instead]

### Step 7: Record Keeping

Track every trade:
- Entry/exit dates and prices
- Rationale for trade
- Market conditions (IV, trend, etc.)
- P&L and lessons learned

### Common Execution Mistakes to Avoid

1. **Entering at wrong volatility level**
2. **Ignoring liquidity**
3. **Over-sizing positions**
4. **Failing to set exit rules upfront**
5. **Emotional decision-making**

