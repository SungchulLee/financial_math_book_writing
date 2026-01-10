# Condors (Call and Put Condors)

**Condors** are four-legged spreads combining two vertical spreads with a gap between them, creating a flat-top profit zone that's wider than a butterfly but with lower maximum profit, offering higher probability of success at the cost of reduced profit potential.









---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_body_width_comparison.png?raw=true" alt="long_call_vs_put" width="700">
</p>

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

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_decomposition.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Before trading condors, understand the structure:**

### 1. Call Condor (Bullish to Neutral)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_greeks.png?raw=true" alt="long_call_vs_put" width="700">
</p>

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

### 2. Put Condor (Bearish to Neutral)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_iv_impact.png?raw=true" alt="long_call_vs_put" width="700">
</p>

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

**Figure 1:** Comparison of butterfly (peaked payoff) vs. condor (flat-top payoff), showing how the condor sacrifices maximum profit for a wider profit zone and higher probability of success.

---

## Economic

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_time_decay.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Beyond the basic definition, understanding what condors REALLY are economically:**

### 1. From Butterfly to Condor

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_vs_butterfly.png?raw=true" alt="long_call_vs_put" width="700">
</p>

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

### 2. Condor as Two Vertical Spreads

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_whipsaw.png?raw=true" alt="long_call_vs_put" width="700">
</p>

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

### 3. The Gaussian Distribution Bet

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/long_call_condor.png?raw=true" alt="long_call_vs_put" width="700">
</p>

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

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_vs_butterfly.png?raw=true" alt="condor_butterfly" width="700">
</p>

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

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_delta_profile.png?raw=true" alt="condor_delta" width="700">
</p>

**Use cases for condors:**


### 1. Why This Structure Exists Economically

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/condor_theta_decay.png?raw=true" alt="condor_theta" width="700">
</p>

Markets create these structures because different participants have different:
- Risk preferences
- Time horizons
- Capital constraints
- View on volatility vs. direction

### 2. Professional Institutional Perspective

Institutional traders view this strategy as a tool for:
1. **Risk management:** Precise control over exposure
2. **Capital efficiency:** Optimal use of buying power
3. **Probability engineering:** Trading win rate for win size
4. **Volatility positioning:** Specific exposure to implied volatility changes

Understanding the economic foundations helps you recognize when the strategy offers genuine edge versus when market pricing is fair.


### 3. Moderate Directional Bias with Range

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

### 4. Earnings Consolidation Play

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

### 5. Low-Volatility Income Strategy

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

### 6. Low-Volatility Mean Reversion

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

### 7. Volatility Crush Post-Event

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

### 1. Delta

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

**Figure 2:** Delta profile of long condor showing near-zero delta within the body (profit zone) and small positive delta in the wings, demonstrating the range-neutral characteristic.

**Practical implication:**

- Stock moving WITHIN body ($100-$105) → Minimal P&L change (low delta)
- Stock moving IN wings ($95-$100, $105-$110) → Moderate P&L change
- Stock OUTSIDE wings → No further P&L change (max loss locked)

### 2. Gamma

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

### 3. Theta

**Theta (time decay):**

$$
\Theta_{\text{Condor}} \approx +$0.05 \text{ to } +$0.15/\text{day} \quad \text{(positive, collect time)}
$$

**Why positive theta?**

You sold 2 options (short $100 and $105 calls) and bought 2 options (long $95 and $110 calls). The short options closer to ATM decay faster than long OTM options.

**Theta evolution:**

**Figure 3:** Theta decay acceleration for condor over time, showing how time decay benefits the position as expiration approaches, with maximum theta in final two weeks.

**Pattern:**

- 45 days out: Θ ≈ +$0.03/day (slow)
- 30 days out: Θ ≈ +$0.08/day (moderate)
- 14 days out: Θ ≈ +$0.18/day (accelerating)
- 7 days out: Θ ≈ +$0.30/day (fast)

**Strategic timing:**

- **Entry:** 30-45 days out (capture most theta)
- **Exit:** 7-14 days remaining (captured majority, avoid gamma risk)

### 4. Vega

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

### 1. The Whipsaw at Body Edges

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

### 2. The IV Spike Disaster

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

### 3. The Early Exit Regret

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


## Common Mistakes

**Detailed analysis of specific errors and how to avoid them:**

### 1. Mistake #1

**The error:** "They're basically the same thing, right?"

**Why it's wrong:**

| Feature | Condor | Iron Condor |
|---------|--------|-------------|
| Structure | All calls OR all puts | Both calls AND puts |
| Entry | Pay debit | Collect credit |
| Max profit | Wing - Debit | Credit collected |
| Use case | Vega crush | Income generation |
| Capital | Lower | Higher |

**How to avoid:** Master condors BEFORE iron condors!

---

### 2. Mistake #2

**The error:** Stock at $100, IV at 15% (10th percentile)

**Why it's deadly:**
- Minimal premium → Poor ROI
- ANY IV spike = instant loss
- No volatility crush to benefit from

**Example:**

**Low IV (BAD):** IV 15% → Debit $1.20 → Any IV spike kills you

**High IV (GOOD):** IV 35% → Debit $2.50 → IV crush helps you

**How to avoid:** Only enter when IV > 40th percentile (ideally > 60th)

---

### 3. Mistake #3

**The sweet spot:**
$$
\text{Body Width} = (0.8 \text{ to } 1.2) \times \text{ATR(14)}
$$

**For $100 stock with ATR = $4:**
- Body: $4-5 wide
- Probability: 55-65%
- ROI: 100-200%

---

### 4. Mistake #4

**The error:** "Stock is in the body. Earnings tomorrow. I'll hold."

**Why it's DEADLY:**
- Stock can gap 10%+ overnight
- Turns profit into max loss instantly

**Rule:** ALWAYS close 2-3 days before earnings. No exceptions!

---

### 5. Mistake #5

**Exit rules:**
- Stock exits body by 25% of wing → Watch
- Stock exits body by 50% of wing → **EXIT OR ADJUST**
- Stock exits body by 75% of wing → **CLOSE NOW**

**Example:** Wing = $5, body top = $105
- $106.25: Monitor
- $107.50: **Take action**
- $108.75: **Close immediately**

---

### 6. Mistake #6

**Too early (25%):** Leave 75% of profits on table

**Too late (95%+):** Risk everything for last 5%

**Optimal:** Take 70-80% of max profit

**Exit formula:**
$$
\text{Exit when: Profit\%} > \left(1 - \frac{\text{DTE}}{45}\right) \times 100\%
$$

---

### 7. Mistake #7

**The cost:** Can lose 20-30% to slippage alone

**Rules:**
- Bid-ask < 10% of mid-price
- Open interest > 500
- Volume > 50 contracts/day

---

### 8. Mistake #8

**Too short (< 21 DTE):** Gamma risk explodes

**Too long (> 60 DTE):** Capital tied up, lower returns

**Sweet spot:** Enter 30-45 DTE, exit 7-14 DTE

---

### 9. Mistake #9

**The error:** Entering four legs separately

**Cost:** $40+ slippage per contract

**Rule:** ALWAYS use spread orders (all 4 legs simultaneously)

---

### 10. Mistake #10

**The error:** Holding calls through ex-dividend date

**Risk:** Early assignment, unexpected capital requirements

**Rule:** Check calendar before entering. Close ITM short calls 3 days before ex-div.

---

## Risk Management Rules

**Essential guidelines:**

### 1. Position Sizing

**Rule of thumb:**

$$
\text{Position Size} = \frac{\text{Risk Capital} \times 0.03}{\text{Max Loss per Condor}}
$$

**Example:**

- $50,000 account
- 3% risk = $1,500
- Condor max loss = $250
- **Max size: 6 contracts**

### 2. Body Width Selection

**Guidelines:**

- **Narrow ($5):** High ROI (80-100%), Lower probability (~50-60%)
- **Medium ($10):** Balanced ROI (100-150%), Medium probability (~60-70%)
- **Wide ($15+):** Lower ROI (<100%), Higher probability (~70-80%)

**Match to conviction:**

- High conviction on range: Narrow body
- Moderate conviction: Medium body  
- Low conviction: Consider iron condor instead

### 3. Time Frame Selection

**Optimal entry:**

- **30-45 DTE:** Capture most theta, avoid early gamma risk
- **Avoid <21 DTE:** Gamma risk too high
- **Avoid >60 DTE:** Slow theta, capital tied up

**Exit timing:**

- **Target:** 50-70% of max profit OR 7-14 DTE
- **Example:** Max profit $3, exit when position worth $4.50-$5 (50-70% captured)

### 4. Adjustment Triggers

**When to adjust:**

1. **Stock exits body:** Close or roll if stock >50% through wing
2. **IV spike:** Consider closing if IV jumps >30%
3. **Event risk:** Close before earnings/Fed if inside body
4. **Time decay slowing:** If theta not working after 2 weeks, reconsider

**How to adjust:**

- **Stock moved up:** Roll upper wing higher (convert to modified condor)
- **Stock moved down:** Roll lower wing lower
- **Both sides threatened:** Close for loss, redeploy

### 5. Avoid These

- Never enter condor in LOW IV (<30th percentile)
- Never hold through earnings if in body
- Never let winners turn to losers (take profit at 50-70%)
- Never use market orders (spreads too wide)
- Never ignore ex-dividend dates (assignment risk)
- Never trade illiquid strikes (bid-ask >$0.15)

---

## Real-World Examples

### 1. Pension Duration Cut via Futures

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

### 2. Transition Risk Hedge

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

### 3. Portable Alpha with Futures

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

### 4. Tactical Duration Extension

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




## Final Wisdom

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

### 1. Step 1

**Before entering, evaluate:**

1. **Market environment:**
   - Is overall trend up, down, or sideways?
   - What's the VIX level? (Want elevated volatility)
   - Any major events next 45 days? (earnings, Fed, geopolitics)

2. **Technical analysis:**
   - Support/resistance levels (strike selection)
   - Volume profile (liquidity assessment)
   - Recent price action (trending vs. consolidating)

3. **Volatility assessment:**
   - Current IV rank/percentile
   - Historical IV levels for this stock
   - IV expansion/contraction cycle

---

### 2. Step 2

**Enter condors when:**
- IV > 50th percentile (ideally > 60th)
- Stock consolidating or range-bound
- Post-earnings (IV elevated, expecting crush)
- 30-45 days to expiration available
- No binary events in window

**Avoid condors when:**
- IV < 30th percentile (too low)
- Before major catalyst (earnings, FDA decision)
- Stock in strong trend (use directional instead)
- < 21 DTE (gamma risk too high)
- Stock daily moves > 50% of body width

---

### 3. Step 3

**Body width calculation:**
$$
\text{Body Width} = (0.8 \text{ to } 1.2) \times \text{ATR(14)}
$$

**Example:**
- Stock at $100, ATR = $4
- Body width: $4-$5
- Strikes: 96/100/105/109

**Wing width:**
- Standard: Equal to body width
- Conservative: 1.5× body width (higher probability)
- Aggressive: 0.75× body width (higher ROI)

---

### 4. Step 4

**Calculate maximum position size:**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Loss Per Contract}}
$$

**Example:**
- Portfolio: $100,000
- Risk tolerance: 2%
- Risk capital: $2,000
- Max loss per contract: $250
- **Max contracts: 8**

**Conservative guidelines:**
- Risk 1-2% per trade when learning
- Max 5 uncorrelated positions
- Never more than 20% of portfolio in options

---

### 5. Step 5

**Best practices:**

1. **Use limit orders** (NEVER market orders)
   - Start at mid-price
   - Adjust by $0.05 every 2 minutes if no fill

2. **Check liquidity:**
   - Bid-ask spread < 10% of mid-price
   - Open interest > 500
   - Volume > 50 contracts/day

3. **Time entry:**
   - Avoid first 30 minutes (volatility)
   - Avoid last 30 minutes (liquidity)
   - Best: 10:30 AM - 3:30 PM EST

4. **Single order:**
   - Enter as complete spread
   - Don't leg in
   - All 4 legs simultaneously

---

### 6. Step 6

**Daily monitoring:**
- Check stock price (in body?)
- Monitor Greeks (Delta, Theta, Vega)
- Watch IV (crushing as expected?)
- Note any news/events

**Profit targets:**
- **Take profit at 70-80% of max profit**
- Don't chase last 20%
- Exit by 14 DTE regardless

**Loss limits:**
- Cut losses at 50% of max loss
- Don't hope for recovery
- Preserve capital for next trade

**Time-based exits:**
- Monitor theta decay acceleration
- Exit 7-14 DTE (before gamma risk)
- Never hold through expiration week

---

### 7. Step 7

**When to adjust:**
- Stock exits body by 50% of wing
- Major unexpected news
- IV behavior contrary to expectation

**How to adjust:**

**Option 1: Close tested side**
- Stock rallied above body
- Close upper wing ($105/$110)
- Keep lower portion as bull spread

**Option 2: Roll the body**
- Close current short calls
- Open new short calls recentered on stock
- Adds debit but recenters profit zone

**Option 3: Exit completely**
- Stock moved >75% through wing
- Better to take loss and redeploy

**Rule:** Have adjustment plan BEFORE entering!

---

### 8. Step 8

**Track every trade in spreadsheet:**

| Date | Symbol | Strikes | Entry | Exit | DTE In | DTE Out | P&L | % | IV In | IV Out | Notes |
|------|--------|---------|-------|------|---------|---------|-----|---|-------|--------|-------|

**Monthly review:**
- Win rate
- Average winner vs. average loser
- Common mistakes
- What's working?

---

### 9. Common Execution Mistakes to Avoid

1. **Entering at wrong volatility level** → Use IV rank tool
2. **Ignoring liquidity** → Check bid-ask spread
3. **Over-sizing positions** → Stick to 1-2% risk
4. **Failing to set exit rules upfront** → Write them down before entry
5. **Emotional decision-making** → Follow the plan, not feelings

---

### 10. Your Pre-Trade Checklist

**Before every condor entry:**

☐ IV > 50th percentile?  
☐ No earnings/events in window?  
☐ Body width = 1× ATR?  
☐ Bid-ask < 10% of mid?  
☐ Position sized for 1-2% risk?  
☐ Exit rules written down?  
☐ Using spread order (not legging)?  
☐ Checked ex-dividend calendar?  

**If all checked → ENTER TRADE**  
**If any unchecked → SKIP TRADE**

---


**Step-by-step implementation framework:**

### 11. Step 1

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

### 12. Step 2

**Enter this strategy when:**
- [Specific market conditions]
- [Volatility requirements]
- [Time horizon matches]
- [Risk tolerance appropriate]

**Avoid this strategy when:**
- [Unfavorable conditions]
- [Wrong volatility environment]
- [Insufficient time or liquidity]

### 13. Step 3

**Calculate maximum position size:**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Loss Per Contract}}
$$

**Conservative guidelines:**
- Risk 1-2% per trade when learning
- Max 5 uncorrelated positions
- Never more than 20% of portfolio in options

### 14. Step 4

**Best practices:**

1. **Use limit orders:** Never use market orders
2. **Check liquidity:** Bid-ask spread < 10% of mid-price
3. **Time entry:** Avoid first/last 30 minutes of trading day
4. **Single order:** Enter as complete strategy, don't leg in

### 15. Step 5

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

### 16. Step 6

**When to adjust:**
- Position threatened
- Market environment changes  
- New information emerges

**How to adjust:**
- [Adjustment technique 1]
- [Adjustment technique 2]
- [When to take loss instead]

### 17. Step 7

Track every trade:
- Entry/exit dates and prices
- Rationale for trade
- Market conditions (IV, trend, etc.)
- P&L and lessons learned

### 18. Common Execution Mistakes to Avoid

1. **Entering at wrong volatility level**
2. **Ignoring liquidity**
3. **Over-sizing positions**
4. **Failing to set exit rules upfront**
5. **Emotional decision-making**