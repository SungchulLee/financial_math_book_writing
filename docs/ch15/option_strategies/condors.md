# Condors (Call and Put Condors)

**Condors** are four-legged spreads combining two vertical spreads with a gap between them, creating a flat-top profit zone that's wider than a butterfly but with lower maximum profit, offering higher probability of success at the cost of reduced profit potential.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_body_width_comparison.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_decomposition.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_greeks.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_iv_impact.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_time_decay.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_vs_butterfly.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_whipsaw.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/long_call_condor.png?raw=true" alt="long_call_vs_put" width="700">
</p>

---

## The Core Insight

**The fundamental idea:**

- Butterflies have peaked payoff (profit at one point)
- Condors have flat-top payoff (profit across a range)
- Trade-off: Lower max profit BUT wider profit zone
- Same risk as butterfly but more forgiving
- Higher probability of profit (more room for stock to move)
- Natural evolution: Vertical Spread → Butterfly → Condor → Iron Condor

**The key equation:**

$$
\text{Max Profit (Condor)} = \text{Width of Body} - \text{Net Debit Paid}
$$

$$
\text{Max Loss (Condor)} = \text{Wing Width} - \text{Max Profit}
$$

**You're essentially betting: "Stock will stay within a RANGE (not a point) and I'm willing to accept lower profit for higher probability."**

---

## What Is a Condor?

**Before trading condors, understand the structure:**

### Call Condor (Bullish to Neutral)

**Definition:** Four calls at different strikes creating flat-top payoff.

**Structure (Long Call Condor):**

- **Buy 1×** lower call at $K_1$ (e.g., $95)
- **Sell 1×** middle-low call at $K_2$ (e.g., $100)
- **Sell 1×** middle-high call at $K_3$ (e.g., $105)
- **Buy 1×** higher call at $K_4$ (e.g., $110)

**Key characteristics:**

- Body width: $K_3 - K_2$ (the flat profit zone)
- Wing width: $K_2 - K_1 = K_4 - K_3$ (equal wings)
- Net: Debit spread (pay to enter)
- All same expiration

**Example:**

- Stock at $102
- Buy $95 call for $9
- Sell $100 call for $5
- Sell $105 call for $2
- Buy $110 call for $0.50
- **Net debit: $9 - $5 - $2 + $0.50 = $2.50**

**Payoff at expiration:**

| Stock Price | $95 Call | $100 Call | $105 Call | $110 Call | Total Value | P&L |
|-------------|----------|-----------|-----------|-----------|-------------|-----|
| $90 | $0 | $0 | $0 | $0 | $0 | **-$2.50** |
| $95 | $0 | $0 | $0 | $0 | $0 | **-$2.50** |
| $100 | $5 | $0 | $0 | $0 | $5 | **+$2.50** |
| $102.50 | $7.50 | $2.50 | $0 | $0 | $5 | **+$2.50** |
| $105 | $10 | $5 | $0 | $0 | $5 | **+$2.50** |
| $110 | $15 | $10 | $5 | $0 | $0 | **-$2.50** |
| $115 | $20 | $15 | $10 | $5 | $0 | **-$2.50** |

**Key insight: Profit zone is $100-$105 (entire body width), not single point!**

### Put Condor (Bearish to Neutral)

**Definition:** Four puts at different strikes creating flat-top payoff.

**Structure (Long Put Condor):**

- **Buy 1×** higher put at $K_4$ (e.g., $110)
- **Sell 1×** middle-high put at $K_3$ (e.g., $105)
- **Sell 1×** middle-low put at $K_2$ (e.g., $100)
- **Buy 1×** lower put at $K_1$ (e.g., $95)

**Example:**

- Stock at $102
- Buy $110 put for $9
- Sell $105 put for $5
- Sell $100 put for $2
- Buy $95 put for $0.50
- **Net debit: $2.50** (same as call condor by put-call parity)

**Payoff: Identical to call condor** (by put-call parity)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_vs_butterfly.png?raw=true" alt="condor_butterfly" width="700">
</p>
**Figure 1:** Comparison of butterfly (peaked payoff) vs. condor (flat-top payoff), showing how the condor sacrifices maximum profit for a wider profit zone and higher probability of success.

---

## Economic Interpretation: The Probability Trade-Off

**Beyond the basic definition, understanding what condors REALLY are economically:**

### From Butterfly to Condor: The Evolution

**The fundamental progression:**

**Butterfly (3 strikes):**

- Buy $95 call, sell 2× $100 calls, buy $105 call
- **Profit zone:** Single point ($100)
- **Max profit:** $2.50 (at exactly $100)
- **Probability:** ~40% (stock must land near $100)

**Condor (4 strikes):**

- Buy $95 call, sell $100 call, sell $105 call, buy $110 call
- **Profit zone:** Range ($100-$105)
- **Max profit:** $2.50 (anywhere $100-$105)
- **Probability:** ~60% (stock can land anywhere in $5 range)

**The trade-off:**

$$
\text{Butterfly Max Profit} = \text{Condor Max Profit} \quad \text{(same!)}
$$

But:

$$
P(\text{Condor Profit}) > P(\text{Butterfly Profit}) \quad \text{(higher probability)}
$$

**Why same max profit?**

Both have same debit and same wing widths. The condor just "spreads out" the butterfly peak across a range.

### Condor as Two Vertical Spreads

**Alternative view: Condor = Bull Spread + Bear Spread**

**Bull call spread (lower wing):**

- Buy $95 call, sell $100 call
- Debit: $4
- Max profit: $1 (at $100+)

**Bear call spread (upper wing):**

- Sell $105 call, buy $110 call
- Credit: $1.50
- Max profit: $1.50 (at $105-)

**Combined (Condor):**

- Net debit: $4 - $1.50 = $2.50
- Max profit: $5 - $2.50 = $2.50 (when both spreads hit max value)

**Key insight:**

$$
\text{Condor} = \text{Long Vertical Spread} + \text{Short Vertical Spread (non-overlapping)}
$$

This decomposition helps with adjustment strategies (can exit one side independently).

### The Gaussian Distribution Bet

**What you're really betting on:**

Stock returns follow (approximately) normal distribution. Condor profits from stock staying within 1 standard deviation.

**Example:**

- Stock at $100, IV = 20%, 30 days to expiration
- Expected move (1σ): $100 × 0.20 × √(30/365) = $5.72

**Condor strikes:**

- $95/$100/$105/$110 (body: $100-$105)
- Body center: $102.50
- **Probability stock ends $100-$105:** ~45% (assuming normal distribution)

**Compare to butterfly:**

- $95/$102.50/$110 (peak at $102.50)
- **Probability stock ends within $2 of $102.50:** ~25%

**Condor has ~80% higher probability!** (45% vs. 25%)

---

## Key Terminology

**Body (or Plateau):**

- The flat-top profit zone
- Distance between two short strikes ($K_3 - K_2$)
- Where max profit is achieved
- Wider body = higher probability but same max profit

**Wings:**

- The outer spreads (lower and upper)
- Lower wing: $K_2 - K_1$
- Upper wing: $K_4 - K_3$
- Always equal width in standard condor

**Debit Condor:**

- Long condor (buy outer strikes, sell inner strikes)
- Pay debit to enter
- Profit if stock stays in body
- Limited risk (debit paid)

**Credit Condor:**

- Short condor (sell outer strikes, buy inner strikes)
- Collect credit to enter
- Profit if stock moves outside body
- Used when expecting breakout

**Iron Condor:**

- Combination of call condor + put condor
- Four strikes: Short put spread + short call spread
- Net credit position
- Covered separately in your curriculum

**Breakeven Points:**

$$
\text{Lower BE} = K_1 + \text{Net Debit}
$$

$$
\text{Upper BE} = K_4 - \text{Net Debit}
$$

---

## Why Trade Condors?

**Use cases for condors:**


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


### 1. Moderate Directional Bias with Range

**Scenario:** Bullish on AAPL but expect consolidation in $170-$180 range

**Trade:** Call condor

- Stock at $175
- Buy $170 call for $8
- Sell $175 call for $5
- Sell $180 call for $2
- Buy $185 call for $0.50
- **Net debit: $1.50**

**Outcome at expiration:**

- Stock at $177 (within body) → Max profit $3.50 ($5 body - $1.50 debit)
- Stock at $168 (below range) → Max loss -$1.50
- Stock at $188 (above range) → Max loss -$1.50

**Why this works:**

- Don't need to predict exact price (entire $175-$180 range works)
- Higher probability than butterfly (~60% vs. ~40%)
- Still limited risk (only risk $1.50)

### 2. Earnings Consolidation Play

**Scenario:** Stock gapped on earnings, expect rest of day/week to consolidate

**Setup:**

- TSLA reports earnings, gaps from $240 → $250 pre-market
- Expecting consolidation in $245-$255 range post-gap

**Trade (at market open):**

- Buy $240 call for $12
- Sell $245 call for $8
- Sell $255 call for $2
- Buy $260 call for $0.50
- **Net debit: $2.50**

**Thesis:**

- Big move already happened (gap up $10)
- Stock will digest move, trade range-bound
- Condor captures consolidation better than butterfly

**Outcome (3 days later):**

- Stock consolidated between $248-$252
- Condor at max profit: $7.50 ($10 body - $2.50 debit)
- **Return: 200%** (on $2.50 debit)

### 3. Low-Volatility Income Strategy

**Scenario:** Market in low-volatility regime, want income from range-bound trading

**Strategy:** Sell condors weekly

**Trade (SPY at $450):**

- SPY has been range-bound $445-$455 for weeks
- Sell call condor: Buy $440 call, sell $445 call, sell $455 call, buy $460 call
- **Collect credit?** No, this is long condor (debit)

Wait, let me reconsider. For income, you'd want SHORT condor:

**Corrected trade (SHORT condor for income):**

- Sell $440 call for $11
- Buy $445 call for $7
- Buy $455 call for $2
- Sell $460 call for $0.50
- **Net credit: $2.50**

**Income thesis:**

- SPY breaks out of $445-$455 range → Collect $2.50 credit
- SPY stays in range → Max loss $2.50 (but this is what we DON'T want)

**Actually, for income from range-bound, you want IRON CONDOR, not regular condor.**

Let me fix this example:

### 3. Low-Volatility Mean Reversion

**Scenario:** Stock has broken out, expect mean reversion back to range

**Setup:**

- Stock normally trades $95-$105
- Just broke down to $90 (oversold)
- Expect reversion back to $95-$105

**Trade:** Long call condor

- Buy $90 call for $3
- Sell $95 call for $1
- Sell $105 call for $0.10
- Buy $110 call for $0.02
- **Net debit: $2.08**

**Thesis:**

- Stock will revert to $95-$105 range (normal range)
- Don't care exactly where in range
- Condor profits from entire range

**Outcome (2 weeks later):**

- Stock at $98 (back in range)
- Max profit: $5 - $2.08 = $2.92 (140% return)

### 4. Volatility Crush Post-Event

**Scenario:** IV elevated before earnings, expect crush after

**Setup:**

- Stock at $100, earnings tomorrow
- IV at 60% (high)
- After earnings, expect IV → 35% AND stock to stay $95-$105

**Trade:** Long condor (benefit from IV crush)

- Buy $95 call for $8 (60% IV)
- Sell $100 call for $5 (60% IV)
- Sell $105 call for $2 (60% IV)
- Buy $110 call for $0.50 (60% IV)
- **Net debit: $1.50**

**Post-earnings:**

- Stock at $102 (within body)
- IV crushed to 35%
- Condor value: $4.80 (intrinsic + small time value)
- **Can close for $3.30 profit (220% gain)**

**Why this works:**

- IV crush helps (all options cheaper, net benefit to debit spread)
- Stock in profit zone (max profit approaching)
- Didn't need to predict exact landing spot

---

## Greeks Behavior

### Delta: Neutral in Body, Directional at Wings

**Delta profile:**

$$
\Delta_{\text{Condor}} = \Delta_{K_1} - \Delta_{K_2} - \Delta_{K_3} + \Delta_{K_4}
$$

**Example (stock at $102, in body):**

- $95 call: Δ = +0.95 (deep ITM)
- $100 call: Δ = +0.75 (ITM)
- $105 call: Δ = +0.30 (OTM)
- $110 call: Δ = +0.10 (OTM)
- **Net delta: 0.95 - 0.75 - 0.30 + 0.10 = 0.00**

**Delta evolution:**

- **Below $95:** Delta ≈ 0 (all wings balanced, all OTM)
- **$95-$100:** Delta increases (long $95 call activating)
- **$100-$105 (BODY):** Delta ≈ 0 (balanced, in profit zone)
- **$105-$110:** Delta decreases (short $105 call activating)
- **Above $110:** Delta ≈ 0 (all wings balanced, all ITM)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_delta_profile.png?raw=true" alt="condor_delta" width="700">
</p>
**Figure 2:** Delta profile of long condor showing near-zero delta within the body (profit zone) and small positive delta in the wings, demonstrating the range-neutral characteristic.

**Practical implication:**

- Stock moving WITHIN body ($100-$105) → Minimal P&L change (low delta)
- Stock moving IN wings ($95-$100, $105-$110) → Moderate P&L change
- Stock OUTSIDE wings → No further P&L change (max loss locked)

### Gamma: Negative at Short Strikes, Positive at Long Strikes

**Gamma profile:**

$$
\Gamma_{\text{Condor}} = \Gamma_{K_1} - \Gamma_{K_2} - \Gamma_{K_3} + \Gamma_{K_4}
$$

**Critical zones:**

- **At $100 (lower short strike):** Negative gamma (small moves hurt)
- **At $105 (upper short strike):** Negative gamma (small moves hurt)
- **In body ($100-$105):** Low gamma (P&L stable)
- **At $95, $110 (long strikes):** Positive gamma (small benefit)

**Example:**

- Stock at $100 (lower edge of body)
- **Gamma ≈ -0.04** (negative)
- Stock moves to $101 → Delta increases → Position value decreases slightly

**Why negative gamma matters:**

Unlike butterfly where you want stock to PIN at center, condor wants stock to STAY STABLE anywhere in body. Negative gamma at edges means whipsaw around edges hurts.

**Practical strategy:**

- **Best scenario:** Stock enters body and STAYS there (no whipsaw)
- **Worst scenario:** Stock whipsaws around $100 or $105 edges

### Theta: Positive Time Decay

**Theta (time decay):**

$$
\Theta_{\text{Condor}} \approx +$0.05 \text{ to } +$0.15/\text{day} \quad \text{(positive, collect time)}
$$

**Why positive theta?**

You sold 2 options (short $100 and $105 calls) and bought 2 options (long $95 and $110 calls). The short options closer to ATM decay faster than long OTM options.

**Theta evolution:**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_theta_decay.png?raw=true" alt="condor_theta" width="700">
</p>
**Figure 3:** Theta decay acceleration for condor over time, showing how time decay benefits the position as expiration approaches, with maximum theta in final two weeks.

**Pattern:**

- 45 days out: Θ ≈ +$0.03/day (slow)
- 30 days out: Θ ≈ +$0.08/day (moderate)
- 14 days out: Θ ≈ +$0.18/day (accelerating)
- 7 days out: Θ ≈ +$0.30/day (fast)

**Strategic timing:**

- **Entry:** 30-45 days out (capture most theta)
- **Exit:** 7-14 days remaining (captured majority, avoid gamma risk)

### Vega: Negative Volatility Exposure

**Vega (IV sensitivity):**

$$
\text{Vega}_{\text{Condor}} = \text{Vega}_{K_1} - \text{Vega}_{K_2} - \text{Vega}_{K_3} + \text{Vega}_{K_4} < 0
$$

**Why negative vega?**

The two short strikes (at $100 and $105) have higher vega than the two long strikes ($95 and $110).

**Example:**

- $95 call vega: +0.12 (OTM, lower vega)
- $100 call vega: +0.25 (near ATM, high vega)
- $105 call vega: +0.22 (near ATM, high vega)
- $110 call vega: +0.08 (OTM, lower vega)
- **Net vega: 0.12 - 0.25 - 0.22 + 0.08 = -0.27**

**Practical impact:**

- **IV increases:** Position loses value (even if stock in body)
- **IV decreases:** Position gains value (vega crush helps)

**Best entry:** High IV environment (sell expensive options, profit from crush)

---

## When Greeks Hurt You

### The Whipsaw at Body Edges

**Scenario:** Stock oscillates around lower body edge

**Setup:**

- Condor: $95/$100/$105/$110
- Stock at $100 (lower edge of body)
- Negative gamma at this level

**Day 1:** Stock at $100 → $99
- Position value decreases (moving out of body)
- **P&L: -$40** (negative gamma effect)

**Day 2:** Stock bounces $99 → $101
- Position value increases but not fully recovered
- **P&L: -$20** (still down from start)

**Day 3:** Stock drops $101 → $98
- More losses
- **P&L: -$80** (cumulative whipsaw damage)

**Net result:**

- Stock ended at $98 (slightly below body, but not max loss zone)
- Whipsaw around $100 edge caused -$80 loss
- Should have exited when pattern emerged

### The IV Spike Disaster

**Scenario:** Entered condor at low IV, unexpected event spikes IV

**Setup:**

- Stock at $102 (in body)
- Condor debit: $2.50
- Entered when IV = 25% (low)

**Unexpected news:** FDA delay announcement

**Result:**

- Stock stays at $102 (still in body, should be profitable)
- But IV spikes: 25% → 45%
- **Vega impact:** -0.27 × 20 = -$540 per contract
- Position value drops from $4 to -$1.40
- **P&L: -$3.90** (despite being in profit zone!)

**Lesson:** Negative vega position vulnerable to IV spikes. Enter condors when IV high, not low.

### The Early Exit Regret

**Scenario:** Took profit too early, missed bigger gains

**Setup:**

- Condor: $95/$100/$105/$110, debit $2.50
- Max profit: $2.50 (if stock in body at expiration)

**Week 1:** Stock at $103 (in body)
- Position value: $3.50
- **Profit: $1.00** (40% of max)
- Trader thinks: "I'll take profit now"

**Week 2-4:** Stock stays $101-$104 (perfectly in body)
- Theta continues to work
- By expiration: Position worth $5.00
- **Missed profit: $1.50** (another 60%)

**Trade-off:**

- Early exit secured $1.00 profit (40% return)
- But left $1.50 on table (60% additional return)

**Lesson:** Condors need time to work (theta accumulation). Don't exit too early unless stock threatens to leave body.

---

## Common Pitfalls

### 1. Confusing Condor with Iron Condor

**The mistake:**

"I'll trade a condor for income" (thinking of iron condor)

**What you missed:**

- **Long Condor:** Debit spread, profit if stock STAYS in body
- **Iron Condor:** Credit spread, profit if stock stays in WIDE range

**Example confusion:**

- Want income from range-bound market
- Enter long call condor (pay debit)
- **Wrong!** Should have used iron condor (collect credit)

**The fix:**

- **Long condor:** Use when expecting stock to enter specific range
- **Iron condor:** Use for income when expecting continued range-bound

### 2. Wrong Body Width Selection

**The mistake:**

"I'll make the body really wide for maximum probability"

**What you missed:**

Wider body = Same max profit but higher debit = Lower ROI

**Example:**

**Option A: Narrow body**
- $95/$100/$105/$110 (body = $5)
- Debit: $2.50
- Max profit: $2.50 (100% ROI)

**Option B: Wide body**
- $95/$100/$110/$115 (body = $10)
- Debit: $4.50
- Max profit: $5.50 (122% ROI)

**Analysis:**

- Option B has higher probability (wider body)
- But requires more capital ($4.50 vs $2.50)
- ROI only slightly better (122% vs 100%)
- **Risk more capital for marginal probability improvement**

**The fix:**

- **Narrow body ($5):** Higher ROI, accept lower probability
- **Medium body ($10):** Balanced probability and ROI
- **Wide body ($15+):** Use iron condor instead (better structure)

### 3. Holding Through High-Impact Events

**The mistake:**

"My condor has 30 days left, I'll hold through earnings"

**What you missed:**

Earnings cause large moves that can blow through body.

**Example:**

- Condor: $95/$100/$105/$110
- 15 days to expiration
- Stock at $103 (nicely in body)
- Earnings in 3 days

**Earnings outcome:**

- Stock beats estimates
- Gaps from $103 → $112 overnight
- Now above entire condor structure
- **Max loss realized: -$2.50**

**Better approach:**

- Close condor before earnings (take $1.50 profit at 60% of max)
- Avoid binary event risk

**The fix:**

- Check earnings calendar before entering
- Close or adjust before earnings if inside body
- Never "hope" stock won't move on earnings

### 4. Not Adjusting Losing Positions

**The mistake:**

"I'll just wait, maybe stock comes back"

**What you missed:**

Once stock exits body, probability of returning diminishes. Early adjustment saves capital.

**Example:**

**Week 1:**

- Condor: $95/$100/$105/$110, debit $2.50
- Stock at $108 (above body)
- Current loss: -$1.50
- **Thought:** "It might come back"

**Week 2:**

- Stock at $111 (even further out)
- Current loss: -$2.50 (max loss)

**Week 3:**

- Stock at $113 (no hope)
- Max loss locked in

**Better approach (Week 1):**

- Stock at $108, close for -$1.50 loss
- **Save:** -$1.50 vs. -$2.50 = $1.00 saved
- Redeploy capital to new opportunity

**The fix:**

- If stock exits body by >50% of wing width, consider closing
- Example: Body is $100-$105, wing is $5, if stock → $107.50+, close
- Don't wait for max loss

### 5. Ignoring Dividend Events

**The mistake:**

Trading condors through ex-dividend dates without adjustment

**What you missed:**

Dividends cause early assignment risk on short calls if ITM.

**Example:**

- Call condor: $95/$100/$105/$110
- Stock at $106, ex-dividend tomorrow ($1.50 dividend)
- **Your short $100 call and $105 call are ITM**

**Risk:**

- Short $100 call gets assigned early (counterparty wants dividend)
- Now you're SHORT 100 shares (forced to deliver)
- **Your condor structure is broken**

**The fix:**

- Check ex-dividend dates before entering
- Close ITM short calls before ex-dividend
- Or roll entire condor to post-dividend strikes

---

## Risk Management Rules

**Essential guidelines:**

### Position Sizing

**Rule of thumb:**

$$
\text{Position Size} = \frac{\text{Risk Capital} \times 0.03}{\text{Max Loss per Condor}}
$$

**Example:**

- $50,000 account
- 3% risk = $1,500
- Condor max loss = $250
- **Max size: 6 contracts**

### Body Width Selection

**Guidelines:**

- **Narrow ($5):** High ROI (80-100%), Lower probability (~50-60%)
- **Medium ($10):** Balanced ROI (100-150%), Medium probability (~60-70%)
- **Wide ($15+):** Lower ROI (<100%), Higher probability (~70-80%)

**Match to conviction:**

- High conviction on range: Narrow body
- Moderate conviction: Medium body  
- Low conviction: Consider iron condor instead

### Time Frame Selection

**Optimal entry:**

- **30-45 DTE:** Capture most theta, avoid early gamma risk
- **Avoid <21 DTE:** Gamma risk too high
- **Avoid >60 DTE:** Slow theta, capital tied up

**Exit timing:**

- **Target:** 50-70% of max profit OR 7-14 DTE
- **Example:** Max profit $3, exit when position worth $4.50-$5 (50-70% captured)

### Adjustment Triggers

**When to adjust:**

1. **Stock exits body:** Close or roll if stock >50% through wing
2. **IV spike:** Consider closing if IV jumps >30%
3. **Event risk:** Close before earnings/Fed if inside body
4. **Time decay slowing:** If theta not working after 2 weeks, reconsider

**How to adjust:**

- **Stock moved up:** Roll upper wing higher (convert to modified condor)
- **Stock moved down:** Roll lower wing lower
- **Both sides threatened:** Close for loss, redeploy

### Avoid These

- Never enter condor in LOW IV (<30th percentile)
- Never hold through earnings if in body
- Never let winners turn to losers (take profit at 50-70%)
- Never use market orders (spreads too wide)
- Never ignore ex-dividend dates (assignment risk)
- Never trade illiquid strikes (bid-ask >$0.15)

---

## Real-World Examples

### Example 1: AAPL Consolidation Condor (Success)

**Setup (September 2024):**

- AAPL at $175 post-iPhone launch
- Expecting consolidation in $170-$180 range
- IV at 55th percentile (reasonable)

**Trade (30 DTE):**

- Buy $170 call for $8.50
- Sell $175 call for $5.20
- Sell $180 call for $2.30
- Buy $185 call for $0.70
- **Net debit: $1.70**

**Position Greeks:**

- Delta: +0.02 (nearly neutral)
- Gamma: -0.03 (small negative)
- Theta: +$0.12/day
- Vega: -0.22

**Week 1:** AAPL drifts $173-$177
- Position value: $2.20
- **Profit: $0.50** (theta working)

**Week 2:** AAPL consolidates $175-$178
- Position value: $2.90
- **Profit: $1.20** (theta accelerating)

**Week 3:** AAPL at $177
- Position value: $3.50
- **Profit: $1.80** (60% of max)
- **Decision:** Take profit (30 DTE → 9 DTE)

**Exit (Day 21):**

- Sold condor for $3.50
- **Total profit: $1.80 (106% return on $1.70 debit)**

**Lesson:** Condor worked perfectly - stock stayed in body, theta accumulated, exited before final week gamma risk.

### Example 2: SPY Volatility Crush (Successful)

**Setup (Post-Election 2024):**

- Election creates uncertainty, IV elevated
- SPY at $450, IV at 75th percentile (28% IV)
- After election, expecting IV crush and consolidation

**Trade (45 DTE):**

- Buy $440 call for $14
- Sell $445 call for $10.50
- Sell $455 call for $4.50
- Buy $460 call for $2.50
- **Net debit: $1.50**

**Election result (next day):**

- SPY at $452 (within body)
- IV crushed: 28% → 18% (-10%)
- **Vega benefit:** -(-0.30) × 10 = +$300
- **Position value:** $3.80 (intrinsic + vega gain)

**Exit (2 days post-election):**

- **Profit: $2.30 (153% return)**
- Captured both directional and vega gains

**Lesson:** High IV entry + directional correctness + IV crush = home run. Condor ideal for post-event volatility crush.

### Example 3: TSLA Whipsaw Disaster

**Setup (November 2024):**

- TSLA at $240
- Condor: $230/$240/$250/$260, debit $3

**Week 1:** TSLA volatile

- Day 1: $240 → $248 (in body, good)
- Day 2: $248 → $238 (exited body down)
- Day 3: $238 → $246 (back in body)
- Day 4: $246 → $236 (out again)
- Day 5: $236 → $244 (back in)

**Whipsaw damage:**

Each cross of body edge (negative gamma) caused small losses:
- **Cumulative loss from whipsaw: -$280**

**Week 2:** TSLA settles at $242 (in body)

- "Should" be profitable (in body)
- **Actual P&L: -$280 + small theta = -$200**

**Lesson:** Condors HATE whipsaw around body edges. If stock volatile, exit early. Better for stocks that STAY in range, not oscillate into it.

### Example 4: Earnings Gap-Out Disaster

**Setup (October 2024):**

- Stock at $103 (in body of $95/$100/$105/$110 condor)
- Debit: $2.50
- 12 DTE, earnings in 4 days
- Current profit: +$1.20
- **Trader holds through earnings** (mistake)

**Earnings outcome:**

- Massive beat, guidance raised
- Stock gaps: $103 → $118 overnight
- Now WAY above condor structure

**Final P&L:**

- Max loss: -$2.50
- **Total loss from $1.20 profit position**

**Better outcome if closed before earnings:**

- Would have locked in $1.20 profit (48% return)
- **Cost of holding: $1.20 - (-$2.50) = $3.70 swing**

**Lesson:** ALWAYS close condors before earnings if in body. Theta gains aren't worth binary event risk.

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

**Condors are flat-top spreads offering higher probability than butterflies:**

$$
\text{Condor} = \text{Lower Vertical Spread} + \text{Upper Vertical Spread (non-overlapping)}
$$

- Four strikes, equal wing widths
- Profit zone is a range (body), not a point
- Same max profit as butterfly but wider profit zone
- Debit spread (pay to enter)
- Higher probability of profit (~60% vs. ~40% for butterfly)

### The Setup

**Long Call Condor:**

- Buy lower call ($K_1$)
- Sell middle-low call ($K_2$)
- Sell middle-high call ($K_3$)
- Buy higher call ($K_4$)
- Net: Debit paid
- Profit if: Stock ends $K_2$ to $K_3$ (body)

**Long Put Condor:**

- Same payoff as call condor (put-call parity)
- Use when: Same range expectation, prefer put mechanics

### The Greeks

**Critical to understand:**

- **Delta:** Near zero in body, small positive in wings
- **Gamma:** Negative at short strikes (edges of body), positive at long strikes
- **Theta:** Positive (collect time decay)
- **Vega:** Negative (short volatility)

**Key insight:** Condors want stock to STAY in body with low volatility.

### Strike Selection

**Body width:**

- **Narrow ($5):** Higher ROI, lower probability
- **Medium ($10):** Balanced, most common
- **Wide ($15+):** Lower ROI, higher probability

**Wing width:**

- Equal to body width or wider
- Standard: Wings = Body (symmetric condor)
- Wider wings = Higher probability but higher debit

### Maximum Profit/Loss

**Max profit (stock in body at expiration):**

$$
\text{Max Profit} = (K_2 - K_1) - \text{Net Debit} = (K_4 - K_3) - \text{Net Debit}
$$

**Max loss (stock outside wings):**

$$
\text{Max Loss} = \text{Net Debit Paid}
$$

**Breakevens:**

$$
\text{Lower BE} = K_1 + \text{Net Debit}
$$

$$
\text{Upper BE} = K_4 - \text{Net Debit}
$$

### When to Use

**Use condors when:**

- Expecting stock to consolidate in range
- Higher probability desired vs. butterfly
- Post-event volatility crush expected
- High IV environment (vega crush helps)
- 30-45 days to expiration

**Don't use when:**

- Low IV (<30th percentile)
- Before earnings/major events
- Stock highly volatile (whipsaw risk)
- Need higher max profit (use butterfly)
- Want income from range (use iron condor)

### Common Mistakes to Avoid

1. Confusing with iron condor (different structure/purpose)
2. Wrong body width (too wide = capital inefficient)
3. Holding through earnings (binary risk)
4. Not adjusting when stock exits body
5. Entering at low IV (vega spike hurts)
6. Ignoring ex-dividend dates (assignment risk)
7. Taking profits too early (<40% max)

### Risk Management

**Essential rules:**

- Size for max loss: 2-3% of account per trade
- Enter at 30-45 DTE (optimal theta zone)
- Exit at 50-70% max profit OR 7-14 DTE
- Close before earnings if in body
- Adjust if stock exits body by >50% of wing
- Use limit orders (spreads can be wide)
- Check ex-dividend calendar

### Comparison to Butterfly

**Advantages over butterfly:**

- Wider profit zone (range vs. point)
- Higher probability of profit (~60% vs ~40%)
- More forgiving (stock can move within body)

**Disadvantages vs. butterfly:**

- Same max profit (no advantage there)
- Higher debit for same max profit
- Less precise (can't target exact price)

### Your Learning Path

**Progression:**

1. Master vertical spreads first (building blocks)
2. Learn butterflies (peaked payoff)
3. Learn condors (this chapter - flat-top payoff)
4. Progress to iron condors (credit version)
5. Eventually: Dynamic adjustment strategies

**Condors bridge butterflies and iron condors!**

### Final Wisdom

> "Condors are the pragmatist's butterfly - you sacrifice the romantic notion of pinpoint accuracy for the realistic acknowledgment that markets are messy. Instead of predicting the stock lands at exactly $100, you say 'somewhere between $100 and $105 works for me.' That humility is rewarded with higher probability, but the market still demands discipline: exit before earnings, don't chase the last dollar, and respect the whipsaw risk at the edges. Condors teach you that being approximately right is more profitable than being precisely wrong."

**Key to success:**

- Enter when IV elevated (>50th percentile)
- Match body width to expected range (use ATR or IV)
- Exit at 50-70% max profit (don't be greedy)
- Close before events (earnings, Fed, etc.)
- Monitor body edges (whipsaw danger zones)
- Give theta time to work (don't exit too early)

**Most important:** Condors are about RANGES, not points. Master this mindset shift from butterflies and you've unlocked higher-probability trading! 🎯📊


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

