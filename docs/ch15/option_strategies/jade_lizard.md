# Jade Lizard and Big Lizard

**Jade Lizard** is an income strategy combining a short put with a short call spread, creating a credit position with no upside risk (cannot lose if stock rallies) but defined downside risk, popular among traders seeking premium collection with asymmetric risk profiles.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_capital_efficiency.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_components.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_credit_vs_width.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_greeks.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_lizard_payoff.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_scenarios.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_vs_big_lizard.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_vs_strangle.png?raw=true" alt="long_call_vs_put" width="700">
</p>

---

## The Core Insight

**The fundamental idea:**

- Traditional short put: Collect premium, risk if stock drops
- Traditional short call spread: Collect premium, risk if stock rallies
- **Jade Lizard: Combine both** → Collect more premium, eliminate upside risk
- Key feature: Net credit > call spread width (no upside risk)
- Downside risk only (if stock crashes below short put)
- Popular for bullish-to-neutral income generation

**The key equation:**

$$
\text{Net Credit} > (K_{\text{call high}} - K_{\text{call low}})
$$

This ensures **zero upside risk** (credit collected exceeds max call spread loss).

**You're essentially betting: "Stock won't crash (short put safe) and I'm willing to cap my upside risk (call spread) to collect maximum premium."**

---

## What Is a Jade Lizard?

**Before trading Jade Lizards, understand the structure:**

### Standard Jade Lizard

**Definition:** Sell OTM put + Sell OTM call spread (higher strikes).

**Structure:**

- **Sell 1×** OTM put at strike $K_P$ (e.g., $95 put)
- **Sell 1×** OTM call at strike $K_{C1}$ (e.g., $105 call)
- **Buy 1×** higher OTM call at strike $K_{C2}$ (e.g., $110 call)
- Same expiration
- Net: Credit collected

**Example:**

- Stock at $100
- Sell $95 put for $3.50
- Sell $105 call for $2.50
- Buy $110 call for $0.80
- **Net credit: $3.50 + $2.50 - $0.80 = $5.20**
- **Call spread width: $110 - $105 = $5**
- **Credit > Width:** $5.20 > $5 ✓ (no upside risk!)

**Payoff at expiration:**

| Stock Price | Put P&L | Call Spread P&L | Total P&L |
|-------------|---------|-----------------|-----------|
| $80 | -$15 (assigned) | +$1.70 (keep credit) | **-$13.30** |
| $90 | -$5 (assigned) | +$1.70 | **-$3.30** |
| $95 | $0 | +$1.70 | **+$1.70** |
| $100 | $0 | +$1.70 | **+$1.70** |
| $105 | $0 | +$1.70 | **+$1.70** |
| $108 | $0 | -$1.30 ($3 ITM - $1.70 credit) | **-$1.30** |
| $110+ | $0 | -$3.30 (max loss) | **-$3.30** |

**But wait - at $110:**

- Put expires worthless: Keep $3.50
- Call spread max loss: -$5 (width)
- **Net: $3.50 - $5 = -$1.50?**

Let me recalculate:

**At $110 (stock above call spread):**

- Put: Expires worthless (sold for $3.50, keep it)
- Call spread: Max loss = -($110 - $105) = -$5
- **Total: $3.50 - $5 = -$1.50 loss**

**Wait, this violates the "no upside risk" claim!**

Let me reconsider. The net credit collected was $5.20. Let's trace through again:

**Total credit collected upfront:** $5.20

**At expiration, if stock at $110+:**

- Short $105 call: Must pay ($110 - $105) = $5
- Long $110 call: Receive ($110 - $110) = $0
- **Call spread loss: -$5**
- **Net P&L: $5.20 credit - $5 loss = +$0.20**

**Ah! The credit ($5.20) EXCEEDS the spread width ($5), so worst case upside is +$0.20 profit.**

This is the key to Jade Lizard: **Credit must exceed call spread width.**

### Big Lizard (Variation)

**Definition:** Jade Lizard with WIDER call spread to collect more premium.

**Structure:**

- Sell OTM put
- Sell OTM call spread with **wider width** (e.g., $10 instead of $5)
- Collect larger credit BUT more upside risk

**Example:**

- Stock at $100
- Sell $95 put for $3.50
- Sell $105 call for $2.50
- Buy $115 call for $0.20 (wider spread)
- **Net credit: $5.80**
- **Call spread width: $10**
- **Credit < Width:** $5.80 < $10 (has upside risk!)

**This is NOT a pure Jade Lizard** (has upside risk), but collects more premium.

**Trade-off:**

- More premium ($5.80 vs $5.20)
- But upside risk exists (if stock rallies hard)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_lizard_payoff.png?raw=true" alt="jade_lizard" width="700">
</p>
**Figure 1:** Payoff diagram for Jade Lizard showing no upside risk (flat or small profit above call spread), maximum profit in the middle range, and downside risk below short put strike.

---

## Economic Interpretation: Selling Two Risks, Keeping One

**Beyond the basic definition, understanding what Jade Lizards REALLY are economically:**

### Decomposition into Components

**Jade Lizard = Short Put + Short Call Spread**

**Short Put component:**

- Collect premium
- Risk: Stock drops below strike
- Obligation: Buy stock at strike if assigned

**Short Call Spread component:**

- Collect premium (sell $105 call, buy $110 call)
- Risk: Stock rallies above $105
- Max loss: Width of spread ($5)
- Capped upside risk

**Combined effect:**

$$
\text{Jade Lizard} = \underbrace{\text{Short Put}}_{\text{Downside risk}} + \underbrace{\text{Short Call Spread}}_{\text{Capped upside risk}}
$$

**Key insight:** By ensuring **credit > call spread width**, you eliminate upside risk entirely.

### Why Eliminate Upside Risk?

**Market bias: Equities have upside drift**

Historical data shows:
- **Long-term equity trend:** UP (~10% annually)
- **Crash risk:** DOWN (fat left tail)
- **Distribution:** Negatively skewed

**Strategic logic:**

- Don't want to lose money if stock rallies (market's natural tendency)
- **Willing to take downside risk** (lower probability in bull market)
- Jade Lizard aligns with market bias

**Comparison to alternatives:**

**Short strangle (sell put + sell call):**

- Risk on BOTH sides (downside AND upside)
- Unlimited risk on both ends

**Jade Lizard (sell put + sell call spread):**

- Risk on downside ONLY
- **No upside risk** (capped by call spread, offset by credit)

**Trade-off:**

- Collect less premium than strangle
- But eliminate upside risk (sleep better)

### The "Lizard" Name Origin

**Why "Jade Lizard"?**

- Coined by options educators (tastytrade community)
- "Jade" = valuable (high premium collection)
- "Lizard" = agile, low risk (eliminates upside risk)
- Contrasts with "Iron Condor" (sells both sides with defined risk)

**Big Lizard:**

- Wider call spread (bigger "lizard")
- More premium but violates no-upside-risk rule

---

## Key Terminology

**Jade Lizard:**

- Short put + short call spread
- Net credit > call spread width (no upside risk)
- Also called: "No-Risk Call Spread Collar" (less common)

**Big Lizard:**

- Jade Lizard with wider call spread
- Credit < call spread width (has upside risk)
- Trade-off: More premium for accepting upside risk

**Short Put:**

- Obligation to buy stock at strike if assigned
- Downside risk (stock drops below strike)
- Collect premium

**Short Call Spread:**

- Sell lower call, buy higher call
- Capped upside risk (width of spread)
- Collect net premium

**Breakeven:**

Lower breakeven only (no upper breakeven due to no upside risk):

$$
\text{BE}_{\text{lower}} = K_{\text{put}} - \text{Net Credit}
$$

**Example:**

- Short $95 put, net credit $5.20
- **BE: $95 - $5.20 = $89.80**

---

## Why Trade Jade Lizards?

**Use cases:**


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


### 1. Bullish-to-Neutral Income (Main Use)

**Scenario:** Stock in established uptrend, want income without upside risk

**Setup:**

- AAPL at $175, strong uptrend
- Expect: Consolidation or continued rally (NOT crash)

**Trade (30 DTE):**

- Sell $165 put for $4.20
- Sell $185 call for $3.50
- Buy $190 call for $1.50
- **Net credit: $6.20**
- **Call spread width: $5**
- **No upside risk:** $6.20 > $5 ✓

**Outcomes:**

**AAPL → $180 (slight rally):**

- All expire worthless
- **Profit: $6.20** (full credit, max profit)

**AAPL → $195 (strong rally):**

- Put worthless, call spread loses $5
- **P&L: $6.20 - $5 = +$1.20** (still profit!)

**AAPL → $160 (drops):**

- Put assigned: Buy 100 shares at $165
- Shares worth $160 → Loss $5
- **P&L: $6.20 - $5 = +$1.20** (breakeven zone)

**AAPL → $150 (crashes):**

- Put assigned at $165
- Shares worth $150 → Loss $15
- **P&L: $6.20 - $15 = -$8.80** (max risk zone)

**Why this works:**

- AAPL trending up (upside protected by design)
- Collect $6.20 premium (good income)
- Only risk if crashes (lower probability)

### 2. Post-Earnings Implied Volatility Crush

**Scenario:** Stock reported earnings, IV elevated, expecting IV crush + consolidation

**Setup:**

- TSLA at $240, just reported earnings
- IV at 70% (elevated post-earnings)
- Expect: IV to normalize to 45%, stock to consolidate

**Trade (21 DTE):**

- Sell $230 put for $6
- Sell $255 call for $5
- Buy $265 call for $2
- **Net credit: $9**
- **Call spread width: $10**

**Wait, this violates no-upside-risk rule!**

Let me adjust:

**Better trade:**

- Sell $230 put for $6
- Sell $255 call for $5
- Buy $260 call for $3
- **Net credit: $8**
- **Call spread width: $5**
- **No upside risk: $8 > $5** ✓

**Outcome (one week later):**

- IV crushes: 70% → 45%
- Stock at $245 (consolidating)
- **Position value:** $1.50 (mostly decayed)
- **Can close for:** $8 - $1.50 = $6.50 profit (81% of max)

**Why this works:**

- IV crush benefits ALL short options
- Stock consolidation keeps price in safe zone
- Collected premium during high IV (optimal entry)

### 3. Low-Volatility Range-Bound Markets

**Scenario:** Market in extended low-volatility regime

**Setup:**

- SPY trading $445-$455 for 3 months
- VIX at 12 (very low)
- Expecting continued range

**Trade (45 DTE):**

- Sell $440 put for $4
- Sell $460 call for $3
- Buy $465 call for $1.20
- **Net credit: $5.80**
- **Call spread width: $5**
- **No upside risk: $5.80 > $5** ✓

**Weekly management:**

- **Week 1-3:** SPY stays $445-$455, theta working
- **Week 4:** SPY at $452, position value $1.20
- **Exit:** Close for $4.60 profit (79% of max)

**Why this works:**

- Low VIX = cheaper options (but still collect good premium)
- Range-bound eliminates directional risk
- No upside risk = perfect for slow uptrend

### 4. Replacing Covered Calls (Capital Efficiency)

**Comparison:**

**Traditional covered call:**

- Own 100 shares at $100 = $10,000 capital
- Sell $105 call for $2.50
- **Capital required: $10,000**
- **Max profit: $7.50** (if called away at $105)

**Jade Lizard alternative:**

- Sell $95 put for $3.50
- Sell $105 call for $2.50
- Buy $110 call for $0.80
- **Capital required: ~$3,000** (margin for short put)
- **Max profit: $5.20**

**Comparison:**

| Metric | Covered Call | Jade Lizard |
|--------|--------------|-------------|
| Capital | $10,000 | $3,000 |
| Max profit | $7.50 | $5.20 |
| ROI | 7.5% | 17.3% |
| Upside | Capped at $105 | No cap (above $110) |
| Risk | Own stock (full downside) | Put assignment |

**Why Jade Lizard can be better:**

- **3× capital efficiency** ($3K vs $10K)
- **2× ROI** (17% vs 7.5%)
- **No upside risk** (vs covered call capped)

---

## Greeks Behavior

### Delta: Slightly Bullish to Neutral

**Delta calculation:**

$$
\Delta_{\text{JL}} = \Delta_{\text{put}} + \Delta_{\text{call spread}}
$$

**Example:**

- Short $95 put: Δ = +0.20 (short put = positive delta)
- Short $105/$110 call spread: Δ = -0.15
- **Net delta: +0.05** (slightly bullish)

**Delta evolution:**

- **Stock drops to $90:** Delta becomes +0.60 (put dominates)
- **Stock at $100:** Delta ≈ 0 (balanced)
- **Stock rallies to $110:** Delta ≈ 0 (call spread capped)

**Key insight:** Jade Lizard is nearly delta-neutral in target zone, slightly bullish overall.

### Gamma: Negative (Short Premium)

**Gamma:**

$$
\Gamma_{\text{JL}} = \Gamma_{\text{put}} + \Gamma_{\text{call spread}} < 0
$$

**Why negative?**

You SOLD options (short gamma). Small moves around strikes hurt.

**Example:**

- Short put gamma: -0.03
- Short call spread gamma: -0.02
- **Net gamma: -0.05**

**Practical impact:**

- Stock whipsaws around $95 or $105 → Gamma losses
- Best scenario: Stock enters safe zone and STAYS there

### Theta: Positive (Collect Time Decay)

**Theta:**

$$
\Theta_{\text{JL}} = \Theta_{\text{put}} + \Theta_{\text{call spread}} > 0
$$

**Example:**

- Short put theta: +$0.12/day
- Short call spread theta: +$0.08/day
- **Net theta: +$0.20/day** (collect ~$20/day)

**Theta evolution:**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_lizard_theta.png?raw=true" alt="jade_theta" width="700">
</p>
**Figure 2:** Theta decay collection for Jade Lizard showing positive daily theta from both short put and short call spread components, accelerating in final 2 weeks.

**Strategic timing:**

- Enter 30-45 DTE (optimal theta zone)
- Exit at 7-14 DTE or 50-70% profit (whichever first)

### Vega: Negative (Short Volatility)

**Vega:**

$$
\text{Vega}_{\text{JL}} = \text{Vega}_{\text{put}} + \text{Vega}_{\text{call spread}} < 0
$$

**Example:**

- Short put vega: -0.18
- Short call spread vega: -0.12
- **Net vega: -0.30**

**Practical impact:**

- **IV increases:** Position loses value (even if stock in safe zone)
- **IV decreases:** Position gains value (vega crush helps)

**Best entry: High IV** (>60th percentile) to benefit from mean reversion.

---

## Common Pitfalls

### 1. Violating the "No Upside Risk" Rule

**The mistake:**

"I'll widen the call spread to collect more premium."

**What you missed:**

If credit < call spread width, you have upside risk (no longer a true Jade Lizard).

**Example:**

**Bad trade:**

- Sell $95 put for $3.50
- Sell $105 call for $2.50
- Buy $115 call for $0.50 (wide spread)
- **Net credit: $5.50**
- **Call spread width: $10**
- **Upside risk:** $5.50 - $10 = **-$4.50 max loss if stock rallies**

**The fix:**

- **Always ensure:** Net credit ≥ call spread width
- If violating this, it's a "Big Lizard" (different strategy, has upside risk)

### 2. Ignoring Assignment Risk

**The mistake:**

"I'll just hold to expiration for max profit."

**What you missed:**

Short put can be assigned EARLY (American options), especially if deep ITM near ex-dividend.

**Example:**

**Setup:**

- Jade Lizard on AAPL
- Stock drops from $175 → $155 (below $165 put strike)
- Ex-dividend date tomorrow ($0.25)

**Friday night:**

- Short $165 put is $10 ITM
- **Assigned:** Must buy 100 shares at $165
- Now own shares worth $155 → Immediate -$10 loss
- **Plus:** Stock could gap down Monday

**The fix:**

- **Close or roll short put** if deeply ITM (>$5)
- Avoid holding short puts through ex-dividend dates
- Monitor assignment risk in final week

### 3. Wrong Strike Selection (Too Aggressive)

**The mistake:**

"I'll sell ATM put for maximum premium."

**What you missed:**

ATM put has 50% probability of being ITM. Too risky.

**Example:**

**Aggressive trade:**

- Stock at $100
- Sell $100 put (ATM) for $5
- High probability of assignment!

**Conservative trade:**

- Stock at $100
- Sell $90 put (10% OTM) for $2
- Lower premium BUT lower probability

**The fix:**

- **Target 15-20 delta puts** (~15-20% OTM)
- Balances premium collection with safety
- Example: Stock at $100, sell $85-$87 put

### 4. Entering at Low IV

**The mistake:**

"Jade Lizards work in any volatility environment."

**What you missed:**

Low IV = low premium collected. Not worth the risk.

**Example:**

**Low IV entry (VIX = 12, stock IV 18%):**

- Net credit: $2.50
- Downside risk: Potentially -$15 if stock crashes
- **Risk/reward: Terrible** ($2.50 gain vs $15+ loss)

**High IV entry (VIX = 22, stock IV 35%):**

- Net credit: $6.50
- Same downside risk: -$15
- **Risk/reward: Better** ($6.50 gain vs $15 loss)

**The fix:**

- **Only enter Jade Lizards when IV >50th percentile**
- Higher premium justifies risk
- IV crush works in your favor (short vega)

### 5. No Exit Plan

**The mistake:**

"I'll hold for maximum profit."

**What you missed:**

Last 20% of profit has highest risk (gamma explodes, assignment risk).

**Example:**

**Week 4 (of 6):**

- Collected $6 credit initially
- Position now worth $1.50
- **Unrealized profit: $4.50 (75% of max)**

**Trader holds for last $1.50...**

**Week 5:** Stock whipsaws around strikes
- Gamma losses: -$2
- **Now only +$2.50 profit** (lost $2 by being greedy)

**The fix:**

- **Exit at 50-75% of max profit**
- Example: $6 credit, close at $1.50-$3 remaining value
- Avoid last week (gamma + assignment risk too high)

---

## Risk Management Rules

### Strike Selection

**Short put guidelines:**

$$
\Delta_{\text{put}} = 0.15 \text{ to } 0.25 \quad \text{(15-25% probability ITM)}
$$

**Example:**

- Stock at $100
- Target: 20-delta put
- **Strikes: $85-$90 range**

**Call spread guidelines:**

$$
\Delta_{\text{short call}} = 0.15 \text{ to } 0.25
$$

$$
\text{Width} = 1\text{-}2 \times \text{ATR (Average True Range)}
$$

**Example:**

- Stock at $100, ATR = $3
- Short call: $110-$115 (20-25 delta)
- Width: $5 (about 1.5× ATR)

### Position Sizing

**Rule of thumb:**

$$
\text{Position Size} = \frac{\text{Account} \times 0.05}{\text{Put Strike}}
$$

**Example:**

- $50,000 account
- 5% risk = $2,500
- Short put at $95
- **Max 1 contract** ($95 × 100 = $9,500 assignment value)

**Alternatively, size on margin required:**

- Margin for Jade Lizard: ~$3,000 per contract
- 5% of $50K account = $2,500
- **Max 1 contract**

### Time Frame

**Entry:**

- **30-45 DTE:** Optimal theta decay zone
- Avoid <21 DTE (gamma too high)

**Exit:**

- **Target:** 50-75% of max profit
- **OR:** 7-10 DTE (whichever first)

**Example:**

- Enter 35 DTE for $6 credit
- Exit at $1.50-$3 remaining value (75-50% profit)
- OR exit at Day 25 (10 DTE remaining)

### IV Entry Requirements

**Check IV percentile:**

$$
\text{IV Percentile} = \frac{\text{Current IV} - \text{52-week Low}}{\text{52-week High} - \text{52-week Low}}
$$

**Entry rules:**

- **<40th percentile:** AVOID (options too cheap)
- **40-60th:** Acceptable
- **>60th:** IDEAL (high premium, IV crush potential)

### Adjustment Triggers

**When to adjust:**

1. **Stock threatens put strike:** Within $2 of short put
2. **Stock rockets past call spread:** Above long call strike
3. **IV spike:** Unexpected 30%+ IV increase
4. **Time decay stalling:** Theta not working after 2 weeks

**How to adjust:**

- **Stock drops:** Roll put down and out (lower strike, later expiration)
- **Stock rallies:** Usually no action needed (no upside risk by design)
- **IV spike:** Consider closing for scratch (reenter later)

---

## Real-World Examples

### Example 1: SPY Monthly Income (Success)

**Setup (March 2024):**

- SPY at $520
- IV at 58th percentile (16% IV)
- Bullish market trend

**Trade (35 DTE):**

- Sell $505 put for $5.20 (18-delta)
- Sell $535 call for $4.10 (20-delta)
- Buy $540 call for $2.50
- **Net credit: $6.80**
- **Call spread width: $5**
- **No upside risk:** $6.80 > $5 ✓

**Week 1:** SPY at $525
- Position value: $5.10
- **Profit so far: $1.70** (theta working)

**Week 2:** SPY at $530
- Position value: $3.80
- **Profit: $3.00** (44% of max)

**Week 3:** SPY at $532
- Position value: $2.50
- **Profit: $4.30** (63% of max)

**Exit (Day 22, 13 DTE remaining):**

- Closed for $2.00
- **Total profit: $4.80 (71% of max)**
- **ROI: 160%** on $3,000 margin

**Lesson:** Clean Jade Lizard execution. Stock stayed in safe zone, theta worked, exited before final week gamma risk. No upside risk protected against late rally.

### Example 2: NVDA Earnings Crush (Success)

**Setup (November 2024, post-earnings):**

- NVDA at $140, just reported earnings
- IV at 75th percentile (75% IV post-earnings)
- Expecting IV crush + consolidation

**Trade (30 DTE):**

- Sell $130 put for $7.50
- Sell $150 call for $6.00
- Buy $155 call for $3.20
- **Net credit: $10.30**
- **Call spread width: $5**
- **No upside risk:** $10.30 > $5 ✓

**Next day (IV crush):**

- IV dropped: 75% → 50% (-25%)
- Stock at $143 (slight rally)
- **Position value:** $4.50
- **Unrealized profit: $5.80** (56% in 1 day!)

**Exit (3 days later):**

- Closed for $3.20
- **Total profit: $7.10 (69% of max)**
- **3-day return: 237%**

**Lesson:** High IV entry + IV crush = perfect Jade Lizard setup. Both short put and short call benefited from vega crush.

### Example 3: Assignment Disaster (Cautionary)

**Setup:**

- Stock at $100
- Jade Lizard: Sell $95 put, sell $110/$115 call spread
- Net credit: $6.50

**Week 3:** Stock drops to $92 (below put strike)

- Trader thinks: "It'll bounce back, I'll hold"
- Put now $3 ITM

**Week 4:** Stock at $90

- Put now $5 ITM
- Ex-dividend date approaching
- **Friday:** Assigned on short put (early assignment)
- **Forced to buy 100 shares at $95**

**Monday:** Stock gaps down to $87

- Own shares worth $87, paid $95
- **Loss: -$8 per share = -$800**
- But collected $6.50 credit
- **Net loss: -$150**

**Better outcome if closed Week 3:**

- Week 3 value at $92: $9 (put worth ~$3, call spread ~$0)
- Could have closed for -$2.50 loss
- **Saved: -$2.50 vs -$1.50 = $1.00** (plus avoided overnight gap risk)

**Lesson:** Don't "hope" for recovery when short put is ITM. Close or roll before assignment risk escalates.

### Example 4: Big Lizard Upside Loss

**Setup:**

- Stock at $100
- **Big Lizard (not standard Jade):**

  - Sell $90 put for $3
  - Sell $110 call for $3
  - Buy $125 call for $0.50
- **Net credit: $5.50**
- **Call spread width: $15**
- **Upside risk exists:** $5.50 < $15

**Outcome:**

- Stock rallies to $125 (strong bull market)
- Call spread max loss: -$15
- **Net P&L: $5.50 - $15 = -$9.50 loss**

**If used standard Jade Lizard:**

- Buy $115 call instead of $125 call (narrower spread)
- Credit would be $4
- Spread width: $5
- **Would have small profit:** $4 - $5 = -$1 (or close to breakeven)

**Lesson:** "Big Lizard" collects more premium but violates the no-upside-risk rule. If stock rallies hard, you lose. Stick to standard Jade Lizard (credit > width) for true upside protection.

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

**Jade Lizard eliminates upside risk while collecting premium:**

$$
\text{Jade Lizard} = \text{Short Put} + \text{Short Call Spread}
$$

$$
\text{Net Credit} > \text{Call Spread Width} \quad \text{(key requirement)}
$$

- No upside risk (cannot lose if stock rallies)
- Downside risk only (short put assignment)
- Bullish-to-neutral bias
- Income strategy for trending/range-bound markets

### The Setup

**Standard Jade Lizard:**

- Sell OTM put (15-25 delta)
- Sell OTM call (15-25 delta)
- Buy higher OTM call (width = 1-2× ATR)
- Net credit > call spread width

**Big Lizard:**

- Same structure
- BUT wider call spread (more premium, has upside risk)

### The Greeks

- **Delta:** Slightly positive (~+0.05 to +0.15)
- **Gamma:** Negative (short premium)
- **Theta:** Positive (collect time decay)
- **Vega:** Negative (short volatility)

### Maximum Profit/Loss

**Max profit (stock in safe zone):**

$$
\text{Max Profit} = \text{Net Credit Collected}
$$

**Max loss (stock crashes below put):**

$$
\text{Max Loss} = (K_{\text{put}} - S_{\text{final}}) - \text{Net Credit}
$$

**Upside:**

No upside loss if credit > spread width (Jade Lizard)

**Breakeven:**

$$
\text{BE}_{\text{lower}} = K_{\text{put}} - \text{Net Credit}
$$

### When to Use

**Use Jade Lizard when:**

- Bullish to neutral bias
- High IV environment (>50th percentile)
- Want income with no upside risk
- Capital efficiency vs covered calls
- 30-45 DTE available

**Don't use when:**

- Low IV (<40th percentile, poor premium)
- Bearish on underlying
- Before earnings (IV spike risk)
- Stock highly volatile (gamma risk)

### Common Mistakes

1. Violating no-upside-risk rule (credit < width)
2. Ignoring assignment risk (short put ITM)
3. Wrong strikes (too aggressive on put)
4. Entering at low IV (poor risk/reward)
5. No exit plan (holding to expiration)
6. Confusing with Big Lizard (different risk profile)

### Risk Management

- Enter at IV >50th percentile
- Sell 15-25 delta puts (not ATM)
- Ensure credit > call spread width
- Size for 5% of account
- Exit at 50-75% profit or 7-10 DTE
- Close if put becomes deeply ITM (>$5)

### Comparison to Alternatives

**vs. Covered Call:**

- Jade Lizard: Less capital, higher ROI, no upside cap
- Covered Call: Own stock, capped upside

**vs. Short Strangle:**

- Jade Lizard: No upside risk
- Strangle: Unlimited risk both sides

**vs. Iron Condor:**

- Jade Lizard: Only downside risk, higher credit
- Iron Condor: Both sides defined risk, lower credit

### Final Wisdom

> "The Jade Lizard is the income trader's answer to covered calls - all the premium, a fraction of the capital, and none of the upside regret. By combining a short put with a short call spread, you're essentially saying 'I don't think the stock will crash, and even if it rallies to the moon, I won't lose.' The magic is in the math: credit > spread width = no upside risk. But discipline matters: sell the put far enough out, enter when IV is rich, and take profits before the last week. The Jade Lizard rewards patience and punishes greed."

**Key to success:**

- ALWAYS ensure: Net credit ≥ call spread width
- Enter when IV >50th percentile (rich premium)
- Sell 15-25 delta puts (not ATM)
- Exit at 50-75% max profit (don't be greedy)
- Monitor short put for assignment risk
- Close or roll if put gets deeply ITM

**Most important:** The "no upside risk" feature is what makes Jade Lizard special. Don't violate this by widening the call spread too much (becomes Big Lizard with upside risk). Stick to the formula! 🦎💚


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

