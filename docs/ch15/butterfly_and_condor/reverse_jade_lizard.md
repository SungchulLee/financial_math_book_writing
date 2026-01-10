# Reverse Jade Lizard

**Reverse Jade Lizard** is a bullish debit strategy combining a long call for unlimited upside profit with a long put spread for limited downside protection, creating a defined-risk position with strong directional bias and strategic profit characteristics.









---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/reverse_jade_lizard_greeks.png?raw=true" alt="reverse_jade_lizard_greeks" width="700">
</p>

**The fundamental idea:**

- Jade Lizard: Short put + short call spread (bearish tilt, credit, undefined upside risk)
- **Reverse Jade Lizard: Long call + long put spread** (bullish tilt, debit, defined risk)
- Unlimited upside profit potential
- Limited downside protection from put spread
- Defined maximum loss
- Bullish strategy with asymmetric risk-reward
- Opposite structure of jade lizard

**The key equations:**

$$
\text{Reverse Jade Lizard} = \text{Long Call} + \text{Long Put Spread}
$$

$$
= \text{Buy Call at } K_3 + \text{Buy Put at } K_2 + \text{Sell Put at } K_1
$$

where $K_1 < K_2 < K_3$ (typically $K_2$ near current price, $K_3$ OTM, $K_1$ farther OTM)

**You're essentially betting: "The market will rally significantly (unlimited profit), but if it drops I want LIMITED protection (put spread limits downside loss), and I'm willing to pay a net debit for this asymmetric profile."**

---

## What Is Reverse Jade Lizard?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/reverse_jade_lizard_components.png?raw=true" alt="reverse_jade_lizard_components" width="700">
</p>

**Before trading reverse jade lizard, understand the structure:**

### 1. Core Structure

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/reverse_jade_lizard_scenarios.png?raw=true" alt="reverse_jade_lizard_scenarios" width="700">
</p>

**Definition:** Long call at higher strike + long put spread (buy higher strike put, sell lower strike put).

**Three-legged structure:**

- **Leg 1 (Long Call):** Buy 1× call at strike $K_3$ (OTM) → Unlimited upside
- **Leg 2 (Long Put):** Buy 1× put at strike $K_2$ (ATM/slightly OTM) → Downside protection
- **Leg 3 (Short Put):** Sell 1× put at strike $K_1$ (farther OTM) → Reduce cost
- Same expiration
- Net: **Debit paid** (you pay for the position)

**Example setup:**

- Stock at $100
- **Buy 1× $105 call** for $3.00
- **Buy 1× $95 put** for $2.50
- **Sell 1× $90 put** for $1.00
- **Net cost: $3.00 + $2.50 - $1.00 = $4.50**

**Payoff at expiration:**

| Stock Price | Long $105 Call | Long $95 Put | Short $90 Put | Total P&L | Net P&L |
|-------------|----------------|--------------|---------------|-----------|---------|
| $80 | $0 | $15 | -$10 | $5 | **+$0.50** |
| $85 | $0 | $10 | -$5 | $5 | **+$0.50** |
| $90 | $0 | $5 | $0 | $5 | **+$0.50** |
| $95 | $0 | $0 | $0 | $0 | **-$4.50** (max loss) |
| $100 | $0 | $0 | $0 | $0 | **-$4.50** |
| $105 | $0 | $0 | $0 | $0 | **-$4.50** |
| $109.50 | $4.50 | $0 | $0 | $4.50 | **$0** (breakeven) |
| $110 | $5 | $0 | $0 | $5 | **+$0.50** |
| $115 | $10 | $0 | $0 | $10 | **+$5.50** |
| $120 | $15 | $0 | $0 | $15 | **+$10.50** |
| $130 | $25 | $0 | $0 | $25 | **+$20.50** |

**Key characteristics:**

- **Upside profit:** Unlimited (long call dominates above breakeven)
- **Downside protection:** Limited (put spread provides $K_2 - K_1 = $5 protection)
- **Max loss:** Net debit - put spread width = $4.50 - $5 = -$4.50 (occurs between $K_1$ and $K_2$)
- **Max profit (downside):** Put spread width - net debit = $5 - $4.50 = $0.50 (below $K_1$)
- **Breakeven (upper):** Long call strike + net debit = $105 + $4.50 = $109.50

### 2. Why "Reverse" Jade Lizard?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/reverse_jade_lizard_vs_long_call.png?raw=true" alt="reverse_jade_lizard_vs_long_call" width="700">
</p>

**Compare to regular Jade Lizard:**

**Jade Lizard (bearish credit strategy):**
$$
\text{Jade Lizard} = \text{Short Put} + \text{Short Call Spread}
$$

- Collect credit
- Profit if stock drops or stays flat
- Undefined upside risk (short call spread caps at some point but can lose more than credit)
- Limited downside profit (capped at short put strike)

**Reverse Jade Lizard (bullish debit strategy):**
$$
\text{Reverse Jade Lizard} = \text{Long Call} + \text{Long Put Spread}
$$

- Pay debit
- Profit if stock rallies significantly
- **Defined risk** (max loss = net debit - put spread width)
- Unlimited upside profit (long call)

**Key insight:** The "reverse" means:
1. Direction reversed: Bearish → Bullish
2. Credit/debit reversed: Credit → Debit
3. Risk profile reversed: Undefined upside risk → Defined downside risk

**Figure 1:** Payoff diagram of reverse jade lizard showing unlimited upside profit (long call), limited downside protection (put spread), defined max loss zone between put strikes, and asymmetric risk-reward profile favoring bulls.

---

## Economic

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/reverse_jade_lizard_risk_profile.png?raw=true" alt="reverse_jade_lizard_risk_profile" width="700">
</p>

**Beyond the basic definition, understanding what reverse jade lizard REALLY is economically:**

### 1. Decomposition 1

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/iv_impact_reverse_jade_lizard.png?raw=true" alt="iv_impact_reverse_jade_lizard" width="700">
</p>

**Alternative view:**

$$
\text{Reverse Jade Lizard} = \text{Long Call} + \text{Partial Downside Insurance}
$$

**Think of it as:**
- **Core position:** Long $105 call (bullish, unlimited upside)
- **Insurance:** Long $95 put (protects from big drops)
- **Insurance funding:** Sell $90 put (reduces cost by $1, accepts risk below $90)

**Net effect:**
- If stock rallies: Long call profits (unlimited)
- If stock drops moderately ($95-$100): Put protects (limits loss)
- If stock crashes (<$90): Protection capped (you're on the hook for difference $90-$95)

**Why do this instead of just buying call?**
- **Cost reduction:** Put spread reduces net debit
- **Crash protection:** Unlike naked long call, you have downside floor
- **Trade-off:** Accept defined max loss for cheaper entry

### 2. Decomposition 2

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/theta_decay_reverse_jade_lizard.png?raw=true" alt="theta_decay_reverse_jade_lizard" width="700">
</p>

**Alternative decomposition:**

$$
\text{Reverse Jade Lizard} \approx \text{Synthetic Long Stock} + \text{Long Put Spread}
$$

**How to see this:**

Recall synthetic long stock:
$$
\text{Synthetic Long} = \text{Long Call} + \text{Short Put (same strike)}
$$

But in reverse jade lizard:
- Long $105 call
- Long $95 put (not same strike, so not exactly synthetic)

**Near-approximation when $K_2 \approx K_3$:**
- If you choose $K_2 = K_3$ (both ATM), then:
$$
\text{Long } K \text{ call} + \text{Long } K \text{ put} + \text{Short } K_1 \text{ put} \approx \text{Straddle} + \text{Short Put}
$$

This becomes a **modified bullish straddle** with downside risk capped by short put.

**Key insight:** The strategy has multiple interpretations depending on strike selection, but always maintains:
1. Bullish directional bias (long call)
2. Defined risk profile (put spread limits downside)
3. Asymmetric reward (unlimited upside, limited downside protection)

### 3. Decomposition 3

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/strike_selection_reverse_jade_lizard.png?raw=true" alt="strike_selection_reverse_jade_lizard" width="700">
</p>

**Most intuitive view:**

$$
\text{Reverse Jade Lizard} = \text{Long Call} - \text{Cost} + \text{Put Credit Spread}
$$

**Example:**
- Want to buy $105 call ($3 cost)
- Too expensive? Sell put credit spread to reduce cost
- Sell $95/$90 put spread: +$2.50 - $1.00 = +$1.50 credit
- **Net cost: $3 - $1.50 = $1.50** (66% cost reduction!)

**Trade-off:**
- **Benefit:** Much cheaper to enter position
- **Risk:** If stock crashes below $90, you lose on put spread
- **Max loss:** $1.50 + ($95 - $90) = $6.50... wait, let me recalculate.

Actually, let me recalculate max loss correctly:
- Net debit paid: $1.50
- If stock below $90: Long $95 put = $5 profit, short $90 put = -$5 loss
- Put spread net: $0
- Long call: $0
- **Total: -$1.50** (the net debit paid)

No wait, that's wrong too. Let me think more carefully:

At stock = $85 (below both puts):
- Long $105 call: Expires worthless, -$3 loss
- Long $95 put: ITM by $10, worth $10
- Short $90 put: ITM by $5, lose $5
- Net: -$3 + $10 - $5 = $2 profit

**Total P&L: $2 profit - $1.50 debit = $0.50 profit**

Ah! So the max loss is NOT at the crash zone. Let me find where max loss occurs.

At stock = $95 (at long put strike):
- Long $105 call: Worthless, -$3
- Long $95 put: ATM, worth $0
- Short $90 put: OTM, worth $0
- Net: -$3 + $0 - $0 = -$3

At stock = $100 (original price):
- Long $105 call: OTM, worth $0, lose $3
- Long $95 put: OTM, worth $0, lose $2.50
- Short $90 put: OTM, collect $1.00
- Net: -$3 - $2.50 + $1.00 = -$4.50

**Max loss = $4.50** occurs between $K_1$ and $K_2$ (between $90 and $95).

So the interpretation is:
- **Long call** costs $3 (loses this if not ITM)
- **Put spread** costs net $1.50 ($2.50 - $1.00)
- **Total debit: $4.50**
- If stock between $90-$105: Lose full debit
- If stock below $90: Put spread gains $5, offsetting some of the $4.50 loss
- **Net max loss: $4.50 - $5 = -$4.50** (no wait, that's still wrong)

Let me recalculate once more at $85:
- Paid $4.50 total
- Long call: $0
- Long put: $10
- Short put: -$5
- Net at expiration: $10 - $5 = $5
- **P&L: $5 - $4.50 = $0.50 profit**

At $95:
- Paid $4.50 total
- Long call: $0
- Long put: $0
- Short put: $0
- Net at expiration: $0
- **P&L: $0 - $4.50 = -$4.50 loss** ← This is max loss!

At $90:
- Paid $4.50
- Long call: $0
- Long put: $5
- Short put: $0
- Net: $5
- **P&L: $5 - $4.50 = $0.50 profit**

So **max loss occurs at $K_2$ (the long put strike) = -$4.50**.

### 4. Comparison to Other Bullish Strategies

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/reverse_jade_lizard_payoff.png?raw=true" alt="reverse_jade_lizard_payoff" width="700">
</p>

**Reverse Jade Lizard vs. Long Call:**

| Metric | Long Call | Reverse Jade Lizard |
|--------|-----------|---------------------|
| **Cost** | $3.00 | $4.50 (50% more) |
| **Max loss** | -$3.00 | -$4.50 (50% more) |
| **Upside** | Unlimited | Unlimited |
| **Downside protection** | None | Limited ($5 via put spread) |
| **Breakeven** | $108 | $109.50 |
| **Best for** | Strong bull, no crash fear | Bull with crash hedge |

**Reverse Jade Lizard vs. Bull Call Spread:**

| Metric | Bull Call Spread | Reverse Jade Lizard |
|--------|------------------|---------------------|
| **Cost** | $2.00 | $4.50 (2.25× more) |
| **Max profit** | $3.00 (capped) | Unlimited |
| **Max loss** | -$2.00 | -$4.50 |
| **Downside protection** | None | Limited ($5) |
| **Best for** | Moderate bull, defined risk | Strong bull, wants protection |

**Key insight:** Reverse jade lizard is for traders who:
1. Are strongly bullish (want unlimited upside)
2. Want some crash protection (put spread)
3. Willing to pay higher debit (vs. plain call)
4. Accept higher breakeven (vs. plain call)

### 5. Advanced Professional Perspectives

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/reverse_jade_lizard_risk_reward.png?raw=true" alt="reverse_jade_lizard_risk_reward" width="700">
</p>

**Understanding the deeper economics of reverse jade lizards:**

**1. Directional conviction with hedged theta:**

**The fundamental problem:**
- Long calls: Unlimited upside BUT negative theta kills position if stock stalls
- **Solution:** Reverse jade lizard adds protection that partially offsets theta

**Economic breakdown:**
- Long call: -$0.15 theta/day
- Long put: -$0.12 theta/day  
- Short put: +$0.08 theta/day
- **Net theta:** -$0.19/day (vs. -$0.15 for plain call)

**Theta is STILL negative** (time decay enemy), but:
- Put spread reduces net debit
- Protection valuable if wrong
- **Trade-off:** Pay more theta for insurance

**2. Volatility positioning with limited downside:**

Unlike jade lizards (bearish on IV), reverse jade lizards are **bullish on IV**:

$$
\text{Net Vega} = \text{Long Call Vega} + \text{Long Put Vega} - \text{Short Put Vega} > 0
$$

**Example:**
- Long $105 call: +0.15 vega
- Long $95 put: +0.12 vega
- Short $90 put: -0.08 vega
- **Net: +0.19 vega** (benefits from IV expansion)

**Why this matters:**
- Enter at low IV (<30th percentile)
- **If IV expands:** Position gains value from vega
- **Plus:** Stock rally gains (delta)
- **Double benefit:** Delta + vega working together

**Professional insight:** Reverse jade lizards profit from **low IV → high IV transitions** + directional move.

**3. Capital efficiency vs. stock ownership:**

**Comparing exposure:**

**Own 100 shares at $100:**
- Capital: $10,000
- Upside: Unlimited
- Downside: -$10,000 (to zero)
- No protection

**Reverse jade lizard:**
- Net debit: $4.50 ($450)
- Upside: Unlimited (above $104.50)
- Downside: -$4.50 max loss ($450)
- **Capital: $450 vs $10,000** (22× more efficient!)

**ROI comparison:**
- Stock rallies to $120 (+20%): $2,000 profit / $10,000 = **20% ROI**
- Reverse jade lizard at $120: $15.50 gain / $4.50 cost = **344% ROI** (17× better!)

**But downside:**
- Stock drops to $80 (-20%): -$2,000 / $10,000 = -20% loss
- Reverse jade lizard: -$4.50 / $4.50 = -100% loss (but only $450 nominal)

**Key: Defined risk + leverage = explosive upside with capped downside**

**4. Professional institutional uses:**

**Hedge fund overlay strategies:**
- Core position: Long equity portfolio
- **Want:** Additional upside leverage without adding directional risk
- **Solution:** Reverse jade lizards as overlay

**Example:**
- Portfolio: $100M long equities
- Add: 500 reverse jade lizards on SPY
- Cost: $225k (0.225% of portfolio)
- **If market rallies 15%:** 
  - Portfolio: +$15M
  - Reverse jade lizards: +$3.75M (assuming $7.50 gain each)
  - **Total: +$18.75M** (25% boost from 0.225% cost!)

**Pre-catalyst positioning:**
- Institutions know catalysts before retail
- Enter reverse jade lizards 30-40 days before event
- **Low IV entry + catalyst = optimal setup**

**Earnings volatility capture:**
- Stock at $100, IV at 20th percentile
- Earnings in 35 days
- **Enter reverse jade lizard for $4 debit**
- After earnings:
  - Stock rallies to $115 (+15%)
  - IV expands 20th → 65th percentile
  - **Position:** $15 intrinsic + $3 IV expansion = $18 value
  - **Profit:** $18 - $4 = $14 (350% ROI!)

**5. Behavioral finance advantages:**

**Exploiting retail biases:**
- Retail overbuys puts before events (fear)
- **Selling puts to them** (short put leg)
- Use proceeds to fund long call (leverage)

**Example of premium harvesting:**
- 30 days before earnings, puts expensive (fear)
- Sell $90 put for $2.50 (overpriced by $0.50)
- Use to reduce long call cost
- **After earnings:** Fear subsides, put decays faster
- **Net:** Got cheap long call exposure

**Conviction signaling:**
- Reverse jade lizard = "I'm willing to pay premium for upside"
- NOT like selling premium (jade lizard)
- **Signal:** Strong directional conviction
- Professional marker of quality setups

**6. Volatility term structure exploitation:**

**Front-month vs. back-month spread:**
- Near-term IV (30 DTE): 22% (cheap)
- Far-term IV (90 DTE): 28% (normal)
- **Opportunity:** Buy cheap near-term volatility

**Reverse jade lizard at 30 DTE:**
- Paying low IV for strikes
- If catalyst hits before expiration:
  - IV spikes
  - Front-month gains disproportionately
  - **Vega gain maximized**

**Term structure play:**
- Enter when IV term structure inverted or flat
- Signals: Market complacent short-term
- **Reverse jade lizard captures expansion**

**7. The mathematics of defined risk leverage:**

**Break-even probability calculation:**

For reverse jade lizard to profit:

$$
P(\text{Stock} > \text{Call Strike} + \text{Net Debit}) > 50\%
$$

**Example:**
- Current: $100
- Call strike: $105
- Debit: $4.50
- **Breakeven:** $109.50 (+9.5%)
- Historical volatility: 25% annually
- 30-day expected move: 25% × √(30/365) = 7.2%
- **Probability > $109.50:** ~25-30%

**Expected value:**
- Win (30%): Average profit $8 (if rallies to $115)
- Loss (70%): -$4.50 (max loss)
- **EV:** 0.30 × $8 - 0.70 × $4.50 = $2.40 - $3.15 = **-$0.75** (negative!)

**This example is NOT a good trade!** Need better setup:
- Lower debit (enter at lower IV)
- Stronger catalyst (higher probability)
- Closer strike (lower breakeven)

**8. Understanding the economic foundations:**

**Key insights:**

**Risk asymmetry favors bulls:**
- Downside: -$4.50 max (defined)
- Upside: Unlimited (could be +$50 if huge rally)
- **Ratio:** 11:1 upside/downside

**But probability asymmetry favors bears:**
- Probability of profit: 25-35% (low)
- Probability of loss: 65-75% (high)
- **Need:** Catalyst to shift probability

**Success formula:**

$$
\text{Edge} = (\text{Probability} \times \text{Reward}) - (1 - \text{Probability}) \times \text{Risk}
$$

**Winning setup:**
- Probability: 40% (strong catalyst)
- Reward: $10 average (if hits)
- Risk: $4.50
- **Edge:** 0.40 × $10 - 0.60 × $4.50 = $4 - $2.70 = **+$1.30** (positive!)

**Losing setup:**
- Probability: 25% (weak catalyst)
- Reward: $8
- Risk: $4.50
- **Edge:** 0.25 × $8 - 0.75 × $4.50 = $2 - $3.38 = **-$1.38** (negative!)

**The economic truth:**
- Reverse jade lizards aren't "better" than plain calls
- They're **different:** Trade higher cost for protection
- **Edge exists in:** Low IV entry + strong catalyst
- **Requires:** Catalyst expertise (not just technical analysis)

Understanding these foundations helps recognize:
- When reverse jade lizards offer edge (low IV + strong catalyst)
- When to avoid (high IV, weak catalyst, stagnant market)
- How to size (accounting for low win probability)
- Why institutions use them (leverage + defined risk + catalyst timing)

---

## Key Terminology

**Reverse Jade Lizard:**
- Bullish debit strategy
- Three-legged: Long call + long put spread
- Defined risk, unlimited reward
- Also called: "Reverse lizard," "bullish jade lizard"

**Long Call (Leg 1):**
- Provides unlimited upside profit
- Typically OTM strike
- Most expensive component
- Delta: +0.30 to +0.50

**Long Put (Leg 2):**
- Provides downside protection
- Typically ATM or slightly OTM strike
- Second most expensive component
- Delta: -0.40 to -0.50

**Short Put (Leg 3):**
- Reduces net cost of position
- Typically farther OTM strike
- Cheapest component (provides credit)
- Delta: -0.15 to -0.25

**Strike selection notation:**
- $K_1$ < $K_2$ < $K_3$
- $K_1$: Short put (lowest strike)
- $K_2$: Long put (middle strike)
- $K_3$: Long call (highest strike)
- Width: $K_2 - K_1$ (put spread width)

**Net debit:**
- Total cost = Long call + Long put - Short put
- Always positive (you pay to enter)
- Typical range: $3-$8 per spread

**Max loss:**
- Occurs between $K_1$ and $K_2$
- Formula: Net debit - Put spread width
- But actual max loss = Net debit (occurs at $K_2$)

**Max profit (downside):**
- Occurs below $K_1$
- Formula: Put spread width - Net debit
- Capped, but softens losses

**Max profit (upside):**
- Occurs above breakeven
- Unlimited (long call)

**Breakeven:**
- Upper: $K_3$ + Net debit
- Lower: None (can't break even going down if put spread width < net debit)

---

## Greeks Analysis

### 1. Delta

**Position delta:**

$$
\Delta_{\text{position}} = \Delta_{\text{long call}} + \Delta_{\text{long put}} - \Delta_{\text{short put}}
$$

**Example deltas (stock at $100):**
- Long $105 call: $\Delta_{\text{call}} = +0.35$
- Long $95 put: $\Delta_{\text{put}} = -0.45$
- Short $90 put: $\Delta_{\text{put}} = -0.20$
- **Net delta: $+0.35 - 0.45 + 0.20 = +0.10$**

**Delta characteristics:**

**Positive net delta (bullish):**
- Position profits from upside moves
- But delta is small initially (typically +0.05 to +0.15)
- Not as bullish as naked long call (delta ~0.35-0.50)

**Delta changes with price:**

As stock rallies toward $105:
- Long call delta increases: $+0.35 \to +0.50 \to +0.70$
- Long put delta decreases: $-0.45 \to -0.30 \to -0.10$
- Short put delta decreases: $-0.20 \to -0.10 \to -0.05$
- **Net delta increases** (becomes more bullish)

As stock drops toward $90:
- Long call delta decreases: $+0.35 \to +0.20 \to +0.10$
- Long put delta increases: $-0.45 \to -0.70 \to -0.90$
- Short put delta increases: $-0.20 \to -0.40 \to -0.60$
- Long put and short put partially offset
- **Net delta becomes negative** (bearish exposure)

**Delta interpretation:**

**Near current price ($95-$105):**
- Small positive delta (+0.05 to +0.15)
- **Not very directional** initially
- Need BIG move to profit

**Above $110 (rally):**
- Delta becomes strongly positive (+0.40 to +0.70)
- **Long call dominates**
- Position acts like long stock

**Below $90 (crash):**
- Delta becomes negative (-0.20 to -0.40)
- **Put spread dominates**
- But limited by short put

### 2. Gamma

**Gamma measures how delta changes as stock moves:**

$$
\Gamma_{\text{position}} = \Gamma_{\text{long call}} + \Gamma_{\text{long put}} - \Gamma_{\text{short put}}
$$

**Gamma characteristics:**

**All options have positive gamma when you're long:**
- Long call: $+\Gamma$ (increases delta as stock rises)
- Long put: $+\Gamma$ (increases absolute delta as stock falls)
- Short put: $-\Gamma$ (decreases absolute delta as stock falls)

**Net gamma by zone:**

**Far above current price (> $115):**
- Long call: High $+\Gamma$ (near strike)
- Long put: Low $+\Gamma$ (far OTM)
- Short put: Low $-\Gamma$ (deep OTM)
- **Net: Positive** (delta accelerates upward)

**Near current price ($95-$105):**
- Long call: Medium $+\Gamma$
- Long put: High $+\Gamma$ (near strike)
- Short put: Medium $-\Gamma$
- **Net: Could be positive or negative** (depends on strikes)

**Far below current price (< $85):**
- Long call: Low $+\Gamma$ (deep OTM)
- Long put: High $+\Gamma$ (ITM but near other strike)
- Short put: High $-\Gamma$ (near strike)
- **Net: Could be negative** (long put and short put offset)

**Gamma interpretation:**

**Positive net gamma (good for rallies):**
- Position accelerates gains as stock moves
- Delta increases with upside moves
- **Want this in trending markets**

**Negative net gamma (bad for whipsaws):**
- Position decelerates or reverses
- Delta decreases with moves
- **Avoid in choppy markets**

**Key insight:** Gamma is most favorable above current price (where long call dominates), making the position well-suited for strong bullish moves but less favorable for oscillation near entry.

### 3. Theta

**Theta measures daily time decay:**

$$
\Theta_{\text{position}} = \Theta_{\text{long call}} + \Theta_{\text{long put}} - \Theta_{\text{short put}}
$$

**All long options lose value to time decay:**
- Long call: $\Theta_{\text{call}} < 0$ (negative theta)
- Long put: $\Theta_{\text{put}} < 0$ (negative theta)
- Short put: $\Theta_{\text{put}} > 0$ (positive theta, you gain)

**Example theta values (30 DTE):**
- Long $105 call: $\Theta = -0.03$ per day
- Long $95 put: $\Theta = -0.04$ per day
- Short $90 put: $\Theta = +0.02$ per day
- **Net theta: $-0.03 - 0.04 + 0.02 = -0.05$ per day**

**Total theta decay (30 days):**
- Daily loss: $-0.05 \times 30 = -\$1.50$
- **This is 33% of initial $4.50 debit!**

**Theta acceleration:**

Theta is not linear - it accelerates as expiration approaches:

| DTE | Daily Theta | 10-Day Loss |
|-----|-------------|-------------|
| 60 | -$0.02 | -$0.20 |
| 30 | -$0.05 | -$0.50 |
| 15 | -$0.10 | -$1.00 |
| 7 | -$0.20 | -$1.40 |
| 3 | -$0.40 | -$1.20 |

**Theta implications:**

**Need quick moves:**
- Can't wait around - theta bleeding
- Best entered 30-60 DTE
- **Must profit within 2-3 weeks** or exit

**Breakeven moves up over time:**
- Initially: Need stock at $109.50 to break even
- After 15 days (-$0.75 theta loss): Need stock at $110.25
- After 25 days (-$1.25 loss): Need stock at $110.75
- **Time works against you** even if directionally correct

**Exit timing critical:**
- Don't hold past 14 DTE unless very profitable
- Theta accelerates in final 2 weeks
- **Better to roll position** than suffer late theta

### 4. Vega

**Vega measures sensitivity to implied volatility changes:**

$$
\text{Vega}_{\text{position}} = \text{Vega}_{\text{long call}} + \text{Vega}_{\text{long put}} - \text{Vega}_{\text{short put}}
$$

**All options have positive vega when you're long:**
- Long call: $+\text{Vega}$ (gains if IV rises)
- Long put: $+\text{Vega}$ (gains if IV rises)
- Short put: $-\text{Vega}$ (loses if IV rises)

**Example vega values:**
- Long $105 call: $\text{Vega} = +0.15$ per 1% IV change
- Long $95 put: $\text{Vega} = +0.18$ per 1% IV change
- Short $90 put: $\text{Vega} = -0.12$ per 1% IV change
- **Net vega: $+0.15 + 0.18 - 0.12 = +0.21$ per 1% IV**

**IV impact examples:**

**Scenario 1: VIX spike (+10 points, roughly +5% IV)**
- Position vega: +0.21
- Gain from vega: $+0.21 \times 5 = +$1.05$
- **Initial $4.50 position now worth $5.55** (+23% from IV alone!)

**Scenario 2: VIX crush (-5 points, roughly -2.5% IV)**
- Position vega: +0.21
- Loss from vega: $-0.21 \times 2.5 = -$0.525$
- **Initial $4.50 position now worth $3.975** (-12% from IV alone)

**Vega characteristics:**

**Positive net vega is GOOD:**
- Profit if market gets more volatile
- Protective: If stock drops, IV usually rises (offsets some delta loss)
- **Want to enter in LOW IV** (cheap options, room for expansion)

**When vega helps most:**

**Market crash:**
- Stock drops hard
- VIX spikes
- Long put gains from both delta AND vega
- **Double benefit** on downside

**Market uncertainty:**
- Earnings upcoming
- Fed meeting
- Geopolitical event
- IV rises, position gains even if stock flat

**When vega hurts:**

**Post-event IV crush:**
- After earnings announcement
- After Fed decision
- IV collapses 30-50%
- **Can lose money even if direction correct**

**Trending rally:**
- Stock grinding higher
- VIX falling (complacency)
- Lose vega value despite correct direction
- **Delta gains offset by vega losses**

**Vega strategy:**

**Best entry: Low IV environment**
- VIX below 20th percentile
- Market calm, complacent
- Options cheap
- **Maximum vega expansion potential**

**Best exit: High IV environment**
- VIX above 60th percentile
- Market fearful
- Options expensive
- **Sell before IV crush**

### 5. Greeks Summary

**Net Greeks (typical values):**

| Greek | Value | Interpretation |
|-------|-------|----------------|
| **Delta** | +0.10 | Small bullish bias initially |
| **Gamma** | Mixed | Positive far from strikes, negative near |
| **Theta** | -0.05/day | Loses $1.50 per month to decay |
| **Vega** | +0.21 | Gains $1.05 per 5% IV increase |

**Greek interactions:**

**Bullish scenario (stock rallies):**
- Delta increases (gamma positive zone)
- Theta still negative (but profits overwhelm)
- Vega may decrease (lower IV in rally)
- **Net: Strong profit** if move is large

**Bearish scenario (stock drops):**
- Delta decreases or negative (gamma mixed)
- Theta still negative (adding to losses)
- Vega likely increases (IV spike helps)
- **Net: Limited loss** due to put spread floor

**Flat scenario (stock unchanged):**
- Delta ~0 (no directional profit)
- Theta negative (losing money daily)
- Vega neutral or negative (IV may decline)
- **Net: Slow bleed** from theta

**Key takeaway:** Reverse jade lizard needs a BIG rally to overcome negative theta. Positive vega helps cushion downside but not enough to profit from crashes. Best for strong bullish conviction in low IV environments.

---

## Risk Profile and Profit Zones

### 1. Maximum Loss

**Where max loss occurs:**

Max loss happens when **all options expire worthless except those between put strikes**.

**Formula:**
$$
\text{Max Loss} = \text{Net Debit Paid}
$$

**This occurs when:** $K_1 < S_T < K_3$ (stock between short put and long call strikes)

**In our example:**
- Net debit: $4.50
- **Max loss: $4.50**
- Occurs when: $90 < S_T < $105
- **Most likely at $K_2 = $95** (long put strike)

**Why this is max loss:**
- Long call: Worthless (stock below $105)
- Long put: Worthless (stock above $95) or small value
- Short put: Worthless (stock above $90)
- **You lose entire net debit**

**Loss zone details:**

At $S_T = $100$ (initial price):
- All options OTM, expire worthless
- Loss = Net debit = $4.50

At $S_T = $95$ (long put strike):
- Long call: $0
- Long put: $0 (ATM)
- Short put: $0
- **Loss = $4.50** (worst case)

At $S_T = $92$ (between puts):
- Long call: $0
- Long put: $3
- Short put: $0
- **Loss = $4.50 - $3 = $1.50**

**Max loss probability:**

If you enter with stock at $100:
- Max loss zone: $90-$105 (15-point range)
- This is ±7.5% from entry
- **For SPY: ~35-40% probability** stock ends here (assumes ~15% annual vol, 30 DTE)

**Risk management:**
- Know max loss before entering ($4.50)
- Position size: Risk only 1-2% of account
- Example: $50,000 account → Risk $500-$1000 → 1-2 contracts
- **Never risk more than 5% on single trade**

### 2. Maximum Profit (Downside)

**Downside profit is LIMITED:**

When stock crashes below $K_1$ (short put strike), the put spread reaches max value:

$$
\text{Max Downside Profit} = (K_2 - K_1) - \text{Net Debit}
$$

**In our example:**
- Put spread width: $K_2 - K_1 = $95 - $90 = $5
- Net debit: $4.50
- **Max downside profit: $5 - $4.50 = $0.50**

**At stock = $85 (below both puts):**
- Long call: $0 (lose $3)
- Long put: $10 (gain $10 from $2.50 cost)
- Short put: -$5 (lose $5 from $1 credit)
- Put spread net: $10 - $5 = $5 gain
- **Total: $5 - $4.50 debit = $0.50 profit**

**Downside profit zone:**
- Profit: $0.50 (capped!)
- Occurs: Any stock price below $90
- **Not a great crash hedge** - only covers part of debit

**Why limited downside profit?**
- Long put gains dollar-for-dollar below $95
- But short put loses dollar-for-dollar below $90
- **Net: Only $5 spread width**, minus debit paid

**Interpretation:**
- This is NOT a bearish strategy
- Downside "profit" just softens the blow
- **Real goal: Unlimited upside**

### 3. Maximum Profit (Upside)

**Upside profit is UNLIMITED:**

As stock rallies above breakeven, the long call dominates:

$$
\text{Upside Profit} = (S_T - K_3) - \text{Net Debit} \quad \text{for } S_T > K_3 + \text{Net Debit}
$$

**In our example:**
- Long call strike: $K_3 = $105
- Net debit: $4.50
- Breakeven: $105 + $4.50 = $109.50

**At various stock prices:**

At $110 (above breakeven):
- Long call: $5 (intrinsic value)
- Long put: $0
- Short put: $0
- **Net: $5 - $4.50 = $0.50 profit**

At $115:
- Long call: $10
- **Net: $10 - $4.50 = $5.50 profit** (122% ROI)

At $120:
- Long call: $15
- **Net: $15 - $4.50 = $10.50 profit** (233% ROI)

At $130:
- Long call: $25
- **Net: $25 - $4.50 = $20.50 profit** (456% ROI)

**Profit characteristics:**

**Unlimited upside:**
- No cap on gains
- Every $1 move above $109.50 = $1 profit
- **Delta approaches +1.0** as stock rises

**Leverage:**
- Control 100 shares for $450 (vs. $10,000 for shares)
- If stock moves 10% ($100 → $110): +$0.50 profit = +11% on capital
- If stock moves 20% ($100 → $120): +$10.50 profit = +233% on capital
- **Leverage ratio: 10-20×** depending on move size

**Comparison to long call:**
- Long $105 call alone: Costs $3, breakeven $108, profit at $110 = $2
- Reverse jade lizard: Costs $4.50, breakeven $109.50, profit at $110 = $0.50
- **Trade-off:** Pay 50% more, get crash protection, but lower profits initially

### 4. Breakeven Analysis

**Upper breakeven:**

$$
\text{BE}_{\text{upper}} = K_3 + \text{Net Debit} = $105 + $4.50 = $109.50
$$

**This means:**
- Need stock to rally 9.5% (from $100 to $109.50)
- To just break even!
- **Hurdle is higher** than simple long call ($108)

**Lower breakeven:**

Typically, there is NO lower breakeven because:
- Max downside profit ($0.50) < Net debit ($4.50)
- Can't break even on downside unless put spread width > net debit

**Exception:** If you structure with very wide put spread:
- Example: $95/$80 put spread ($15 width), net debit $10
- Then max downside profit: $15 - $10 = $5 profit
- Lower breakeven: Some price between $80-$95

**But typically:** Reverse jade lizard has only ONE breakeven (upside).

**Breakeven probability:**

Assuming 30 DTE, 15% annual volatility:
- Stock at $100, need $109.50
- Move required: +9.5% in 30 days
- **Probability: ~20-25%** (roughly 1 std dev move)

**Implication:**
- 75-80% chance you DON'T reach breakeven
- **Need strong conviction** to justify trade
- Best with specific catalyst (earnings, FDA approval, etc.)

### 5. Risk-Reward Ratios

**Upside risk-reward:**

$$
\text{Risk-Reward (Upside)} = \frac{\text{Max Loss}}{\text{Typical Target Profit}}
$$

**Example targets:**

**Conservative target (+$10 move to $120):**
- Profit: $10.50
- Risk: $4.50
- **Risk-reward: 1:2.3** (lose $1 to make $2.33)

**Aggressive target (+$20 move to $130):**
- Profit: $20.50
- Risk: $4.50
- **Risk-reward: 1:4.6** (lose $1 to make $4.56)

**Very aggressive (+$30 move to $140):**
- Profit: $30.50
- Risk: $4.50
- **Risk-reward: 1:6.8** (excellent!)

**Downside risk-reward:**
- Profit: $0.50
- Risk: $4.50
- **Risk-reward: 9:1** (terrible! Lose $9 to make $1)

**Key insight:** This is a BULLISH strategy. The asymmetry favors upside. Don't enter expecting downside profit.

**Win rate vs. payoff:**

Given probabilities:
- Win (rally): 20-25% chance → Payoff: 2-5× risk
- Max loss: 35-40% chance → Payoff: -1× risk
- Small downside profit: 20% chance → Payoff: +0.1× risk
- **Expected value:** Slightly positive if you pick right stocks

**To be profitable:**
- Need 30-40% win rate (reach target)
- With 2-4× payoffs per win
- **OR** Enter in extremely low IV (improves odds)

**Figure 2:** Risk-reward profile showing unlimited upside potential with defined downside risk, breakeven points, max loss zone, and asymmetric payoff structure favoring bulls.

---

## Optimal Market Conditions

### 1. Volatility Environment

**Best entry: LOW IMPLIED VOLATILITY**

**Why low IV is crucial:**

**Lower cost:**
- When VIX is low (e.g., 12-15), options are cheap
- Long call: Might cost $2.50 instead of $3.50
- Long put: Might cost $2.00 instead of $3.00
- **Net debit: $3.00 instead of $5.00** (40% cheaper!)

**Vega expansion potential:**
- Entered at low IV → Room for IV to rise
- Positive vega → Gains when IV increases
- **IV mean reversion:** Low IV tends to rise toward average

**Probability of profit:**
- Lower breakeven: $105 + $3 = $108 (vs. $109.50 with higher cost)
- **Better odds** of reaching breakeven

**Historical IV percentile:**

**Use IV rank or IV percentile to time entry:**

| IV Percentile | Interpretation | Action |
|---------------|----------------|--------|
| < 20% | Very low, options cheap | **EXCELLENT entry** |
| 20-40% | Below average | Good entry |
| 40-60% | Average | Neutral |
| 60-80% | Above average | Poor entry |
| > 80% | Very high, options expensive | **AVOID** |

**Example: AAPL reverse jade lizard:**
- IV percentile: 15% (very low)
- Current IV: 22%
- Historical average: 28%
- **Rationale:** IV has room to expand (mean reversion), options cheap

**Why avoid high IV:**

**Expensive entry:**
- High IV → Options overpriced
- Net debit might be $6-$8 (too expensive)
- Breakeven too far: $105 + $7 = $112 (12% move required!)

**Vega crush risk:**
- After event (earnings), IV collapses
- Lose vega value even if direction correct
- **Can lose 20-30% from IV crush alone**

**Lower probability:**
- Higher breakeven = Lower win rate
- Need extreme moves to profit

**Optimal entry window:**

**Ideal: 30-60 days before catalyst**
- Enough time for theta not to hurt too much (>30 DTE)
- Not so far that you pay for excess time value (>60 DTE)
- **Sweet spot: 40-45 DTE**

**IV below 30th percentile:**
- Options cheap, room for expansion
- If IV rises, you gain from positive vega
- Even if stock flat, vega can offset theta

### 2. Price Action Setup

**Best technical setup: Bullish consolidation**

**Pattern 1: Bull flag/pennant**
```
Price action:
         /|   
        / |   ← Consolidation (building energy)
       /  |___
      /        ← Previous rally
     /          
    /
```

**Characteristics:**
- Strong rally (pole)
- Tight consolidation (flag)
- Decreasing volume
- **Breakout imminent**

**Why this is ideal:**
- Stock has momentum
- Pullback allows cheaper entry
- Consolidation = spring being compressed
- **High probability of continuation**

**Pattern 2: Ascending triangle**
```
Price:
    _______ ← Resistance
   /   /  
  /   /   ← Higher lows
 /   /    
/   /
```

**Characteristics:**
- Flat resistance (sellers at same price)
- Higher lows (buyers getting more aggressive)
- Volume declining into apex
- **Breakout usually explosive**

**Pattern 3: Cup and handle**
```
Price:
     /‾\     ← Cup
    /   \    
   |     ‾\  ← Handle
   |
```

**Characteristics:**
- Rounded bottom (cup)
- Small pullback (handle)
- Duration: 4-8 weeks typical
- **Powerful breakout pattern**

**Avoid these setups:**

**Parabolic rally (exhaustion):**
```
         |
        /|  ← Vertical (unsustainable)
       / |
      /  |
     /
```
- Too extended, likely to pull back
- High IV (options expensive)
- **Wait for consolidation**

**Downtrend:**
```
\  
 \  /\  
  \/  \   ← Lower highs, lower lows
   \/
```
- Fighting the trend (low win rate)
- **Never enter reverse jade lizard in downtrend**

### 3. Catalysts

**Best catalysts: Binary events with upside surprise potential**

**Earnings (specific types):**

**High-growth companies:**
- Companies with strong revenue growth (>20% YoY)
- Recent quarters: Beat estimates
- Guidance: Conservative (room to raise)
- **Example: Tech stocks in growth phase**

**Product launches:**
- New iPhone release
- New drug approval (FDA)
- Major contract announced
- **Binary outcome: Stock jumps or doesn't**

**M&A rumors:**
- Target company
- Industry consolidation
- Strategic buyer interest
- **Takeover premium: 20-40% typical**

**Guidance raise:**
- Company pre-announces strong quarter
- Raises full-year guidance
- **Stock often gaps 5-10% on news**

**Avoid these catalysts:**

**Earnings (high expectations):**
- Stock already rallied 20% pre-earnings
- Analysts very bullish (little upside left)
- IV extremely high (>80th percentile)
- **Priced in → Risky**

**Fed meetings (macro):**
- Hard to predict
- Can go either way
- Affects broad market, not individual stock
- **Use for index trades, not single stocks**

**Geopolitical events:**
- Elections, wars, policy changes
- Too uncertain
- Can drag on for months
- **Avoid unless very specific thesis**

### 4. Time Horizon

**Optimal holding period: 2-4 weeks**

**Why this range:**

**Less than 2 weeks:**
- Theta too strong (accelerating decay)
- Less time for move to develop
- Pin risk increases
- **Too aggressive**

**More than 6 weeks:**
- Paying for excess time value
- Theta accumulates ($1.50+ per month)
- Uncertainty increases
- **Too conservative**

**Sweet spot: 30 DTE entry, hold 2-3 weeks**
- Enter with 30 DTE
- Hold 2-3 weeks (exit at 7-14 DTE)
- If not profitable by 14 DTE → **Close position**
- If very profitable (>+100%) → **Take profit early**

**Exit timing rules:**

**By 14 DTE:**
- Theta accelerating
- If not up +50%, close
- Unlikely to recover

**By 7 DTE:**
- Absolutely exit
- Gamma and theta explode
- Pin risk maximum
- **No exceptions**

**Example timeline:**

**Day 0:** Enter reverse jade lizard (30 DTE)
- Stock at $100
- Net debit: $4.50
- Target: $120 (+20% move)

**Day 10:** Stock at $105
- Position: -$2 loss (theta + small delta gain)
- Action: Hold (need more time)

**Day 16:** Stock at $110
- Position: +$1 profit (breakeven)
- Action: Hold (still 14 DTE, let it run)

**Day 21:** Stock at $115
- Position: +$5.50 profit (+122% ROI)
- Action: **Consider taking profit** (9 DTE, theta accelerating)

**Day 23:** Stock at $112
- Position: +$3 profit
- Action: **Close immediately** (7 DTE, don't risk reversal)

### 5. Market Regime

**Best in: Bullish trending market**

**Bull market characteristics:**
- Higher highs, higher lows
- VIX declining (complacency rising)
- Breadth strong (many stocks participating)
- **Dips get bought quickly**

**Why bullish regime is ideal:**
- Strategy is directionally bullish (long call)
- Trending market → Momentum continues
- Pullbacks shallow → Limited downside risk
- **Win rate higher** in bull markets

**Neutral/choppy market:**
- Stock oscillates in range
- No clear direction
- **Worst case:** Theta bleeds, delta minimal
- **Avoid** reverse jade lizard here

**Bear market:**
- Downtrends, volatility spikes
- Put spread helps, but not enough
- Max loss -$4.50, max downside profit +$0.50
- **Net risk to downside** (lose 9× what you gain)

**Bear market rally (exception):**
- Sharp counter-trend rally
- Sentiment extremely bearish
- **Can work** if you time the bounce
- But risky - rallies often fail

### 6. Combining Indicators

**Ideal confluence for entry:**

**Technical:**
- Bull flag pattern
- Stock above 50-day MA
- RSI 40-60 (not overbought)
- Volume declining into consolidation

**Fundamental:**
- Earnings in 3-4 weeks
- Recent quarters: All beats
- Guidance conservative (room to raise)

**Volatility:**
- IV percentile < 20%
- Current IV: 24%
- Earnings IV: Historically 35%
- **Vega expansion potential: +10-15%**

**Sentiment:**
- Analyst upgrades recent
- Short interest declining
- Options skew bullish (calls expensive vs. puts)

**Example: NVDA reverse jade lizard (hypothetical)**

**Setup:**
- Stock: $480 (bull flag forming)
- Pattern: 6-week consolidation after rally from $420
- Catalyst: Earnings in 28 days
- IV: 31% (20th percentile, low vs. history)
- Thesis: AI demand strong, likely to beat + raise guidance

**Position:**
- Buy $500 call (slightly OTM)
- Buy $460 put (ATM)
- Sell $440 put (OTM)
- Net debit: $15
- Breakeven: $515 (+7.3% move)

**Risk-reward:**
- Max loss: -$15 (if stock ends $440-$500)
- Target: $550 (+$35 profit = 233% ROI)
- Probability of target: ~30% (based on historical earnings moves)
- **Reward/Risk: 2.3:1** (good!)

**Exit plan:**
- Take 50% off at +100% ROI ($30 profit)
- Let rest run to $550 target
- Stop loss: Exit at 14 DTE if not profitable
- Hard exit: 7 DTE regardless

---

## Comparison with Related Strategies

### 1. Reverse Jade Lizard vs. Jade Lizard

**Jade Lizard (Bearish credit):**

$$
\text{Jade Lizard} = \text{Short Put} + \text{Short Call Spread}
$$

**Structure:**
- Sell OTM put
- Sell call spread (sell lower, buy higher)
- Collect credit (typically $2-$4)

**Example:**
- Stock at $100
- Sell $95 put: +$2.50
- Sell $105/$110 call spread: +$1.50 ($3 - $1.50)
- **Net credit: $4.00**

**Characteristics:**
- Bearish/neutral bias
- Profit if stock drops or stays flat
- Undefined risk if stock drops hard
- Capped upside risk (protected by long $110 call)
- **Max profit: $4 credit** (if stock above $105)

**Reverse Jade Lizard (Bullish debit):**

$$
\text{Reverse Jade Lizard} = \text{Long Call} + \text{Long Put Spread}
$$

**Structure:**
- Buy OTM call
- Buy put spread (buy higher, sell lower)
- Pay debit (typically $3-$6)

**Example:**
- Stock at $100
- Buy $105 call: -$3.00
- Buy $95/$90 put spread: -$1.50 ($2.50 - $1)
- **Net debit: $4.50**

**Characteristics:**
- Bullish bias
- Profit if stock rallies significantly
- **Defined risk** (max loss = debit - put spread width)
- Unlimited upside
- **Max profit: Unlimited**

**Comparison table:**

| Metric | Jade Lizard | Reverse Jade Lizard |
|--------|-------------|---------------------|
| **Direction** | Bearish/Neutral | Bullish |
| **Entry** | Credit | Debit |
| **Upside** | Capped | Unlimited |
| **Downside** | Undefined risk | Defined risk |
| **Best for** | High IV | Low IV |
| **Theta** | Positive (earn) | Negative (lose) |
| **Vega** | Negative | Positive |
| **Win rate** | 60-70% | 30-40% |
| **Payoff** | Small ($2-$4) | Large ($10-$50+) |

**Key insight:** They are opposites:
- Jade lizard = Sell volatility, bearish tilt
- Reverse jade lizard = Buy volatility, bullish tilt

### 2. Reverse Jade Lizard vs. Long Call

**Long Call (Simple bullish):**

$$
\text{Long Call} = \text{Buy Call}
$$

**Example:**
- Stock at $100
- Buy $105 call: -$3.00
- **Net cost: $3.00**

**Payoff:**
- Below $105: -$3 max loss
- At $108: Break even
- Above $108: Unlimited profit

**Reverse Jade Lizard (Bullish with protection):**

**Example:**
- Stock at $100
- Buy $105 call: -$3.00
- Buy $95/$90 put spread: -$1.50
- **Net cost: $4.50**

**Comparison:**

| Metric | Long Call | Reverse Jade Lizard |
|--------|-----------|---------------------|
| **Cost** | $3.00 | $4.50 (50% more) |
| **Max loss** | -$3.00 | -$4.50 |
| **Max downside profit** | -$3.00 | +$0.50 |
| **Breakeven** | $108 | $109.50 |
| **Upside** | Unlimited | Unlimited |
| **Delta** | +0.35 | +0.10 |
| **Vega** | +0.15 | +0.21 (40% more) |
| **Best for** | Pure bull | Bull + crash fear |

**When to choose long call:**
- Strongly bullish, no crash concerns
- Want simplicity (one leg)
- Lower capital required
- Accept full loss if wrong

**When to choose reverse jade lizard:**
- Bullish but want crash protection
- Willing to pay 50% more for hedge
- Positive on vega (want IV expansion)
- Accept higher breakeven for peace of mind

### 3. Reverse Jade Lizard vs. Bull Call Spread

**Bull Call Spread (Defined risk and reward):**

$$
\text{Bull Call Spread} = \text{Buy Call} + \text{Sell Call (higher strike)}
$$

**Example:**
- Stock at $100
- Buy $100 call: -$5.00
- Sell $110 call: +$2.00
- **Net cost: $3.00**

**Payoff:**
- Below $100: -$3 max loss
- At $103: Break even
- At $110+: **Max profit $7** (capped!)

**Reverse Jade Lizard:**

**Example:**
- Buy $105 call: -$3.00
- Buy $95/$90 put spread: -$1.50
- **Net cost: $4.50**

**Comparison:**

| Metric | Bull Call Spread | Reverse Jade Lizard |
|--------|------------------|---------------------|
| **Cost** | $3.00 | $4.50 |
| **Max loss** | -$3.00 | -$4.50 |
| **Max profit** | $7.00 (capped at $110) | Unlimited |
| **Breakeven** | $103 | $109.50 |
| **Best for** | Moderate bull | Strong bull |
| **Theta** | -$0.03/day | -$0.05/day |
| **Win rate** | 45-50% | 30-35% |

**When to choose bull call spread:**
- Moderate bullish view (10-15% move expected)
- Want defined risk AND defined reward
- Lower capital outlay
- Higher breakeven (easier to reach)
- **Conservative traders**

**When to choose reverse jade lizard:**
- Very bullish (20%+ move expected)
- Want unlimited upside
- Willing to pay more and wait longer
- Want crash protection
- **Aggressive traders with strong conviction**

### 4. Reverse Jade Lizard vs. Collar

**Collar (Protective structure for stock owners):**

$$
\text{Collar} = \text{Long Stock} + \text{Long Put} + \text{Short Call}
$$

**Example (owns 100 shares at $100):**
- Long stock: Already own (cost $10,000)
- Buy $95 put: -$2.50 (protection)
- Sell $110 call: +$2.50 (income)
- **Net cost: $0** (zero-cost collar)

**Characteristics:**
- Downside protected (below $95 → put protects)
- Upside capped (above $110 → call assigned)
- For stock owners who want protection

**Reverse Jade Lizard (No stock required):**

**Example:**
- Buy $105 call: -$3.00
- Buy $95/$90 put spread: -$1.50
- **Net cost: $4.50**

**Comparison:**

| Metric | Collar | Reverse Jade Lizard |
|--------|--------|---------------------|
| **Capital** | $10,000 | $450 |
| **Stock required** | Yes | No |
| **Upside** | Capped at $110 | Unlimited |
| **Downside** | Protected below $95 | Limited protection |
| **Best for** | Stock owners | Option traders |
| **Leverage** | 1× | 20-30× |

**Key difference:** Collar is for stock owners who want protection. Reverse jade lizard is for option traders who want bullish leverage.

### 5. Reverse Jade Lizard vs. Risk Reversal

**Risk Reversal (Pure directional bet):**

$$
\text{Risk Reversal} = \text{Long Call} + \text{Short Put}
$$

**Example:**
- Stock at $100
- Buy $105 call: -$3.00
- Sell $95 put: +$2.50
- **Net cost: $0.50** (cheap!)

**Characteristics:**
- Very cheap (or even credit)
- Unlimited upside
- **Unlimited downside** (short naked put)
- Mimics long stock (delta ~+0.50)

**Reverse Jade Lizard:**

**Example:**
- Buy $105 call: -$3.00
- Buy $95/$90 put spread: -$1.50
- **Net cost: $4.50**

**Comparison:**

| Metric | Risk Reversal | Reverse Jade Lizard |
|--------|---------------|---------------------|
| **Cost** | $0.50 | $4.50 (9× more!) |
| **Upside** | Unlimited | Unlimited |
| **Downside risk** | Unlimited | Defined (-$4.50 max) |
| **Delta** | +0.50 | +0.10 |
| **Margin** | Required | Not required |
| **Risk level** | Very high | Moderate |

**When to choose risk reversal:**
- Very strong bullish conviction
- Comfortable with downside risk
- Have margin for short put
- Want cheap/free entry

**When to choose reverse jade lizard:**
- Bullish but want defined risk
- No margin account or want limited risk
- Willing to pay more for protection
- **Most retail traders should choose this**

---

## Practical Trading Guide

### 1. Entry Checklist

**Before entering any reverse jade lizard, verify:**

**Market conditions (must satisfy ALL):**

✓ **IV environment:**
- IV percentile < 30% (preferably < 20%)
- Current IV below historical average
- Room for IV expansion

✓ **Price action:**
- Bullish pattern (bull flag, ascending triangle, or cup-and-handle)
- Stock above 50-day moving average
- Recent consolidation after rally

✓ **Catalyst:**
- Clear catalyst 2-4 weeks away (earnings, FDA approval, product launch)
- Historical pattern: Positive surprises
- Expectations: Conservative (room to beat)

✓ **Technical:**
- RSI 40-60 (not overbought)
- Support nearby (for put spread protection)
- Volume: Declining into consolidation (coiling)

**Position specifications:**

✓ **Strike selection:**
- Long call: 1-2 strikes OTM (delta ~0.35-0.45)
- Long put: ATM or 1 strike OTM (delta ~-0.40 to -0.50)
- Short put: 5-10% below current price (delta ~-0.15 to -0.25)
- Put spread width: 5-10% of stock price

✓ **Expiration:**
- **30-45 DTE** (sweet spot)
- Not less than 21 DTE (too little time)
- Not more than 60 DTE (too much time value)

✓ **Cost:**
- Net debit: 3-6% of stock price
- Example: $100 stock → $3-$6 debit
- **If debit > $6, position too expensive** (wait for lower IV)

**Liquidity requirements:**

✓ **Options liquidity:**
- Bid-ask spread: < 10% of option price
- Open interest: > 500 per strike
- Volume: > 1000 contracts daily
- **Avoid illiquid options** (slippage kills profit)

✓ **Stock liquidity:**
- Average daily volume: > 1 million shares
- Market cap: > $5 billion (for stocks), any size for ETFs
- Spread: < $0.05 for stocks > $100

**Risk management:**

✓ **Position sizing:**
- Risk: 1-2% of account per trade (0.5% when learning)
- Max loss known: -$4.50 per spread
- Example: $50k account, risk $500 → 1 contract (risk $450)
- **Never risk more than 5% on single trade**

✓ **Exit plan:**
- Profit target: +100% to +200% of risk (50% off at +100%, let rest run)
- Stop loss: Exit by 14 DTE if not profitable
- Hard stop: Exit by 7 DTE regardless of P&L
- **Write down rules before entering!**

### 2. Step-by-Step Execution

**Step 1: Identify candidate**

**Screening criteria:**

Use options scanner to find:
- IV percentile < 30%
- Upcoming catalyst (earnings in 20-35 days)
- Stock up 5-15% last 3 months (bullish trend)
- Pullback last 2 weeks (consolidation)

**Example screen results:**
- MSFT: IV 18%, earnings in 28 days ✓
- AAPL: IV 35%, earnings in 28 days ✗ (IV too high)
- NVDA: IV 22%, no catalyst near ✗ (no catalyst)
- **Pick MSFT**

**Step 2: Analyze setup**

**Technical review:**
- Chart: Bull flag forming (rally from $380 to $420, now at $410 consolidating)
- Moving averages: Above 50-day ($395), above 200-day ($370)
- RSI: 55 (neutral, room to run)
- Volume: Declining during consolidation ✓

**Fundamental review:**
- Last 4 quarters: All earnings beats
- Guidance: Conservative (typical for MSFT)
- Analyst estimates: $2.85 EPS (achievable)
- Revenue growth: +12% YoY
- **Thesis: Likely to beat & raise guidance** → Stock targets $440-$450

**Step 3: Structure position**

**Strike selection:**

Current price: MSFT at $410

**Long call:**
- Choose: $420 call (delta ~0.40)
- Premium: $6.50
- Why: 2.4% OTM, good balance of cost vs. delta

**Long put:**
- Choose: $400 put (delta ~-0.45)
- Premium: $5.20
- Why: 2.4% OTM, provides meaningful protection

**Short put:**
- Choose: $380 put (delta ~-0.18)
- Premium: $2.00
- Why: 7.3% OTM, low probability of ITM, reduces cost

**Net debit:**
$$
\text{Net Debit} = $6.50 + $5.20 - $2.00 = $9.70
$$

**Verify:**
- Debit as % of stock: $9.70 / $410 = 2.37% ✓ (within 3-6% range)
- Put spread width: $400 - $380 = $20
- Max loss: $9.70 (at prices $380-$420)
- Max downside profit: $20 - $9.70 = $10.30 (below $380)
- Breakeven: $420 + $9.70 = $429.70 (+4.8% from current)

**Step 4: Enter position**

**Order type:**

**Always use limit orders:**
- Calculate mid-price for full spread
- Long $420 call: Bid $6.40 / Ask $6.60 → Mid $6.50
- Long $400 put: Bid $5.10 / Ask $5.30 → Mid $5.20
- Short $380 put: Bid $1.90 / Ask $2.10 → Mid $2.00
- **Net mid: $6.50 + $5.20 - $2.00 = $9.70**

**Enter order:**
- **Buy 1 MSFT $420 call** 
- **Buy 1 MSFT $400 put**
- **Sell 1 MSFT $380 put**
- All same expiration (28 DTE)
- Limit: $9.70 debit
- **Or slightly better: $9.60** (try to save $0.10)

**Execution tips:**

**During market hours:**
- First 30 minutes: Avoid (wide spreads)
- Mid-day: Best (tightest spreads)
- Last 30 minutes: Avoid (manipulation risk)

**Patience:**
- Place limit at $9.60
- If not filled in 10 minutes, increase to $9.70
- If still not filled, increase to $9.80 (max)
- **Don't chase** - if spreads too wide, wait or skip

**Verify fill:**
- Check confirmation: 1 contract filled
- Debit: $970 (including fees ~$5-$10)
- Greeks visible: Delta ~+0.05, Theta ~-$0.08/day, Vega ~+0.24

**Step 5: Monitor position**

**Daily monitoring (first week):**

**Check stock price:**
- MSFT now at $415 (up from $410)
- Your position: +$100 profit (+10%)
- **Action: Hold** (thesis still valid, earnings coming)

**Check IV:**
- IV now 20% (up from 18%)
- Vega gain: $0.24 × 2% = +$48
- **Good:** IV expanding as expected

**Check theta:**
- Days passed: 4
- Theta loss: -$0.08 × 4 = -$32
- **Acceptable:** Small loss, delta gains more than offset

**Weekly monitoring (week 2-3):**

**Scenario A: Stock rallying**
- Week 2: MSFT at $425
- Your position: +$250 profit (+26%)
- Long call: $10 (was $6.50)
- Long put: $2 (was $5.20, decayed)
- Short put: $0.50 (was $2, decayed)
- **Net: $11.50 value** (from $9.70 debit)

**Action:**
- Take 50% off (close half position)
- Lock in $125 profit
- Let rest run with house money

**Scenario B: Stock flat**
- Week 2: MSFT at $410 (unchanged)
- Your position: -$180 loss (-19%)
- Theta ate -$0.08 × 10 days = -$80
- No delta gain (flat)
- **Net: $7.90 value** (from $9.70 debit)

**Action:**
- Check earnings date: 11 days away
- Thesis: Still valid (no news to change view)
- **Hold** but prepare to exit if not profitable by earnings - 3 days

**Scenario C: Stock dropping**
- Week 2: MSFT at $390
- Your position: -$150 loss (-15%)
- Long call: $2 (was $6.50, lost value)
- Long put: $12 (was $5.20, gained)
- Short put: $0 (was $2, gained)
- Put spread: $12 - $0 = $12 (partially offsetting)
- **Net: $14 value** (from $9.70 debit)
- **Wait, let me recalculate:**

Actually at $390:
- Long $420 call: OTM by $30, worth ~$0.50
- Long $400 put: ITM by $10, worth ~$11
- Short $380 put: OTM by $10, worth ~$1
- Net: $0.50 + $11 - $1 = $10.50
- **P&L: $10.50 - $9.70 = +$0.80 profit**

Hmm, this is actually a small profit! The put spread did its job.

**Action:**
- Thesis invalidated (stock dropped, no longer bullish)
- **Close position immediately** (take small profit, be happy with hedge)

### 3. Step 6

**Exit scenario 1: Hit profit target**

**Day 18 (10 DTE remaining):**
- MSFT at $445 (up from $410 entry)
- Long $420 call: $26 (ITM by $25)
- Long $400 put: $0.10 (far OTM)
- Short $380 put: $0.05 (far OTM)
- **Position value: $26 + $0.10 - $0.05 = $26.05**
- P&L: $26.05 - $9.70 = **+$16.35 profit** (+169% ROI!)

**Action:**
- **Close entire position** immediately
- Don't wait for expiration (pin risk, theta, gap risk)
- Take the win!

**Exit execution:**
- Sell $420 call: Market order (very liquid)
- Sell $400 put: Limit order (less liquid, might get $0.05-$0.10)
- Buy $380 put: Limit order (might pay $0.00-$0.05)
- **Total proceeds: ~$26**

**Exit scenario 2: Approaching expiration, not profitable**

**Day 23 (7 DTE remaining):**
- MSFT at $418 (up slightly from $410)
- Long $420 call: $2.50 (slightly OTM)
- Long $400 put: $0.20 (far OTM)
- Short $380 put: $0.05 (far OTM)
- **Position value: $2.50 + $0.20 - $0.05 = $2.65**
- P&L: $2.65 - $9.70 = **-$7.05 loss** (-73%)

**Action:**
- **Close immediately** (7 DTE = hard stop)
- Accept the loss
- Don't hope for miracle in last week

**Rationale:**
- Theta accelerating (-$0.30/day now)
- 7 more days = -$2.10 additional decay
- Would need stock to rally to $440+ just to recover theta
- **Probability low** → Cut loss now

**Exit scenario 3: Thesis invalidated mid-trade**

**Day 8 (20 DTE remaining):**
- **News:** Microsoft announces product delay, lowers guidance
- Stock gaps down to $390
- Your position: From -$7.05 loss to +$0.80 profit (put spread helped!)

**Action:**
- **Close immediately** despite small profit
- Thesis broken (product delay = bearish)
- No reason to hold (earnings likely to disappoint)
- Take the $0.80 profit and move on

**Exit scenario 4: Take partial profit**

**Day 12 (16 DTE):**
- MSFT at $430 (up from $410)
- Long $420 call: $13 (ITM)
- Position value: $13.50
- P&L: $13.50 - $9.70 = +$3.80 (+39%)

**Action:**
- **Take 50% off** (close half the position)
- Sell 1 contract (out of 2 total)
- Lock in +$1.90 per spread
- Let other half run to target ($445+)

**Rationale:**
- Secured profit (can't lose now)
- Still have upside exposure
- **Reduces stress** (playing with house money)

### 4. Step 7

**Record keeping (mandatory for improvement):**

**Trade log entry:**

```
Date: 2024-03-15
Ticker: MSFT
Strategy: Reverse Jade Lizard
Strikes: +$420C / +$400P / -$380P (28 DTE)
Entry: $9.70 debit
Stock at entry: $410
IV at entry: 18% (15th percentile)

Thesis:
- Bull flag pattern after rally from $380
- Earnings in 28 days, history of beats
- Low IV, options cheap
- Target: $440-$450 post-earnings

Exit: 2024-04-02 (18 days held)
Stock at exit: $445
Exit price: $26.00
P&L: +$16.30 (+168% ROI)

What worked:
✓ Entered at very low IV (great timing)
✓ Bull flag played out perfectly
✓ Earnings beat, stock gapped to $430 next day
✓ Took profit at target (didn't get greedy)

What could improve:
- Could have sized larger (only risked 1.5% of account)
- Exited a bit early ($445 vs. stock went to $455 later)

Lessons:
- Low IV entry is KEY (saved $2-$3 on debit)
- Technical patterns work (bull flag very reliable)
- Taking profit at target = good discipline

Grade: A (excellent execution)
```

### 5. Common Mistakes to Avoid

**1. Entering at high IV**

**Mistake:** Trading reverse jade lizard when IV > 60th percentile

**Why bad:**
- Options expensive (debit might be $12+ instead of $6)
- IV likely to decrease (vega loss)
- Lower probability of profit (higher breakeven)

**Fix:**
- Wait for IV < 30th percentile
- Use IV rank tool to check
- **Patience pays** (wait weeks/months if needed)

**2. Ignoring liquidity**

**Mistake:** Trading options with open interest < 100

**Example:**
- You enter at mid-price $9.70
- Try to exit at $26
- Bid: $23, Ask: $29 (wide spread!)
- **You lose $3 to slippage** (11% of profit!)

**Fix:**
- Only trade strikes with OI > 500
- Check bid-ask spread < 10% of price
- **Liquid options = Lower costs**

**3. Oversizing position**

**Mistake:** Risking 10% of account on one trade

**Why disastrous:**
- One bad trade = -10% account
- Three bad trades = -30% (hard to recover)
- Emotional trading (fear, revenge trading)

**Fix:**
- Risk 1-2% max per trade
- For $50k account: Risk $500-$1000 = 1 contract
- **Small losses OK, big losses fatal**

**4. No exit plan**

**Mistake:** "I'll figure it out when I get there"

**Result:**
- Stock at $445, +168% profit
- You think: "Maybe it goes to $460!"
- Hold through earnings
- Stock drops to $420 post-earnings
- **Now only +20% profit** (gave back 148%!)

**Fix:**
- Write exit rules BEFORE entering
- Profit target: +100% → Take 50% off
- Stop loss: 14 DTE if not profitable
- **Follow rules, don't improvise**

**5. Holding too long**

**Mistake:** Holding position to expiration (0 DTE)

**Why terrible:**
- Pin risk (stock exactly at strike = chaos)
- Gamma explosion (small moves = huge P&L swings)
- Assignment risk (if ITM, you get assigned)
- Weekend risk (if Friday, can't react to news)

**Fix:**
- **Exit by 7 DTE** (no exceptions!)
- Earlier if profitable (+100%) or unprofitable (14 DTE)
- Don't hope for miracles in final week

**6. Ignoring assignment risk**

**Mistake:** Holding short $380 put when stock at $375 (ITM)

**What happens:**
- You get assigned: Forced to buy 100 shares at $380
- Stock actually at $375
- **You lose $5 per share = $500!**
- Plus, now stuck with 100 shares (need $37,500 capital)

**Fix:**
- Close position BEFORE short put goes deep ITM
- If short put delta > -0.70, close
- **Don't risk assignment** (especially if no capital for shares)

**7. Fighting the trend**

**Mistake:** Entering reverse jade lizard in downtrend

**Example:**
- Stock in clear downtrend (lower highs, lower lows)
- You think: "It's oversold, must bounce!"
- Enter reverse jade lizard
- Stock continues down
- **You lose -$9.70** (full debit)

**Fix:**
- Only enter in uptrends or after consolidation
- Wait for reversal confirmation
- **Trend is your friend** (don't fight it)

**8. Ignoring earnings IV crush**

**Mistake:** Holding through earnings when entered for $9.70 at 18% IV

**What happens:**
- Before earnings: Position worth $12 (small profit)
- After earnings: Stock flat at $410
- **IV drops 18% → 12%** (crush!)
- Vega loss: -$0.24 × 6% × 100 = -$144
- **Position now worth $9.80** (profit gone!)

**Fix:**
- If entered for low IV and IV spikes pre-earnings, **consider exiting**
- Don't hold through earnings unless thesis requires it
- **Vega crush can wipe out 20-30% of value**

### 6. Real-World Example

**Trade: AAPL Reverse Jade Lizard (Hypothetical)**

**Setup:**

**Date:** August 15, 2024
**Stock:** AAPL at $175
**Thesis:** iPhone 15 launch expected in September, historically bullish
**Technical:** Bull flag pattern, consolidating after rally from $165
**IV:** 20% (10th percentile, very low)
**Catalyst:** Apple event September 12 (28 days away)

**Analysis:**

**Fundamental:**
- New iPhone always boosts stock
- Services revenue growing 10% YoY
- China weakness priced in (already dropped from $195 to $175)
- Analyst targets: $190-$195 post-event

**Technical:**
- Broke above $170 resistance
- Consolidating $173-$177 (tight range)
- Volume declining (coiling for breakout)
- RSI: 58 (room to run)

**Options:**
- IV: 20% (vs. historical 28%)
- Earnings IV: Typically 32% (room for expansion)
- Options very cheap

**Position structure:**

**Strikes:**
- Buy $180 call (2.9% OTM, delta +0.38)
- Buy $170 put (2.9% OTM, delta -0.42)
- Sell $160 put (8.6% OTM, delta -0.16)

**Pricing:**
- $180 call: $5.20
- $170 put: $4.10
- $160 put: $1.50
- **Net debit: $5.20 + $4.10 - $1.50 = $7.80**

**Risk-reward:**
- Max loss: $7.80 (between $160-$180)
- Max downside profit: $10 - $7.80 = $2.20 (below $160)
- Breakeven: $180 + $7.80 = $187.80 (+7.3%)
- Debit as % of stock: 4.46% ✓

**Position sizing:**
- Account size: $50,000
- Risk target: 1.5% = $750
- Contracts: $750 / $780 = 0.96 → **1 contract**
- Total capital at risk: $780

**Trade execution:**

**Day 1 (August 15):** Entered position
- Order: Limit $7.70 (trying to save $0.10)
- Filled at $7.75 (saved $0.05, good enough)
- Actual debit including fees: $781

**Day 5 (August 20):** Stock at $178
- Position value: $8.50
- P&L: +$0.75 (+9.6%)
- IV: 21% (slight increase)
- **Action: Hold** (event still 3 weeks away)

**Day 10 (August 25):** Stock at $176
- Position value: $7.20
- P&L: -$0.55 (-7.1%)
- IV: 22% (continuing to rise)
- Theta loss: -$0.10 × 10 = -$1.00
- **Action: Hold** (event in 2 weeks, IV rising = good)

**Day 16 (September 1):** Stock at $180
- Position value: $10.50
- P&L: +$2.75 (+35%)
- IV: 26% (rising into event)
- Long call: ITM, delta now +0.55
- **Action: Hold** (approaching breakout)

**Day 22 (September 7):** Stock at $185 (breakout!)
- Position value: $14.20
- P&L: +$6.45 (+83%)
- IV: 30% (peaked)
- **Action: Take 50% off** (lock in profit)
- Closed 0.5 contracts at $14.20
- Profit: $3.23 (per half contract)
- Let other half run to event

**Day 28 (September 12):** Apple Event
- **Announcement:** iPhone 15 looks great, new features
- Stock gaps to $188 pre-market
- Before opening: Position worth $17.50
- **Action: Close remaining half before market open**
- Sold at $17.50

**Final results:**

**Position 1 (50%):**
- Entry: $7.75
- Exit: $14.20 (day 22)
- Profit: $6.45 per spread
- ROI: +83%

**Position 2 (50%):**
- Entry: $7.75
- Exit: $17.50 (day 28)
- Profit: $9.75 per spread
- ROI: +126%

**Combined:**
- Average exit: ($14.20 + $17.50) / 2 = $15.85
- Average profit: ($6.45 + $9.75) / 2 = **$8.10**
- **Average ROI: +104.5%**
- Total P&L: $810 (on $781 risk)

**What worked:**
✓ Entered at very low IV (10th percentile)
✓ Clear catalyst (iPhone event)
✓ Took partial profits (50% at +83%)
✓ Let rest run to event (captured gap)
✓ Exited before IV crush (post-event)

**What could improve:**
- Could have waited for better entry (stock dipped to $173 on Day 7)
- Could have sized slightly larger (only risked 1.5% of account)

**Key lessons:**
1. **Low IV entry is critical** - Saved $2-$3 on debit
2. **Taking partial profits works** - Locked in gains, still had upside
3. **Exiting before IV crush** - Stock opened at $188 but quickly dropped to $183 as IV crushed from 30% → 20%
4. **Catalysts work** - iPhone events historically bullish

**Grade: A** (excellent execution, strong profit, good risk management)

---

## Advanced Concepts

### 1. Strike Selection Strategies

**Strategy 1: Aggressive structure (higher risk-reward)**

**Goal:** Maximize leverage, accept higher breakeven

**Strike selection:**
- Long call: 5-7% OTM (delta ~0.25-0.30)
- Long put: ATM (delta ~-0.50)
- Short put: 10-15% OTM (delta ~-0.10 to -0.15)

**Example (stock at $100):**
- Buy $107 call: $2.00
- Buy $100 put: $3.00
- Sell $88 put: $0.80
- **Net: $4.20**
- Breakeven: $111.20 (+11.2%)
- Max loss: $4.20
- **Risk-reward: Need big move, but 3:1 to 5:1 payoff if works**

**When to use:**
- Very strong catalyst (FDA approval, major product launch)
- Stock has history of gapping 10-15% on news
- You have high conviction
- **Not for beginners** (low win rate)

**Strategy 2: Conservative structure (higher win rate)**

**Goal:** Lower breakeven, accept lower leverage

**Strike selection:**
- Long call: 2-3% OTM (delta ~0.40-0.45)
- Long put: 2-3% OTM (delta ~-0.40)
- Short put: 7-10% OTM (delta ~-0.20)

**Example (stock at $100):**
- Buy $103 call: $4.00
- Buy $97 put: $3.50
- Sell $92 put: $1.30
- **Net: $6.20**
- Breakeven: $109.20 (+9.2%)
- Max loss: $6.20
- **Risk-reward: Need moderate move, 1.5:1 to 3:1 payoff**

**When to use:**
- Moderate catalyst (earnings, guidance raise)
- Stock less volatile (blue chip)
- You want higher probability
- **Good for beginners**

**Strategy 3: Balanced structure (standard approach)**

**Goal:** Balance risk-reward and win rate

**Strike selection (used in most examples):**
- Long call: 3-5% OTM (delta ~0.35-0.40)
- Long put: ATM to 2% OTM (delta ~-0.45 to -0.50)
- Short put: 8-10% OTM (delta ~-0.15 to -0.20)

**Example (stock at $100):**
- Buy $105 call: $3.00
- Buy $98 put: $3.00
- Sell $90 put: $1.00
- **Net: $5.00**
- Breakeven: $110 (+10%)
- Max loss: $5.00
- **Risk-reward: 2:1 to 4:1 typical**

**Strategy 4: Vega-focused structure**

**Goal:** Maximize vega exposure (profit from IV expansion)

**Strike selection:**
- All strikes ATM or near-ATM (max vega)
- Long call: ATM (delta ~0.50, vega ~0.20)
- Long put: ATM (delta ~-0.50, vega ~0.20)
- Short put: 5% OTM (delta ~-0.25, vega ~0.15)

**Example (stock at $100):**
- Buy $100 call: $5.00
- Buy $100 put: $5.00
- Sell $95 put: $2.00
- **Net: $8.00** (expensive!)
- **Net vega: +0.25** (high vega exposure)

**When to use:**
- Expect volatility spike (VIX very low, market calm)
- Event approaching (earnings, FOMC) where IV will rise
- Stock at inflection point (could break either way)
- **Risk:** High cost, need IV expansion to profit

### 2. Adjustments and Management

**Adjustment 1: Roll up (stock rallying)**

**Scenario:**
- Entered: $100 stock, +$105C / +$95P / -$90P for $4.50
- Now: $115 stock (10 days later), position at $8 (+$3.50 profit)
- Long call: Deep ITM, delta ~0.90 (not much more upside leverage)
- **Problem:** Limited upside left (diminishing returns)

**Adjustment:**
- **Close current position** at $8 (take profit)
- **Open new position** at current price:
  - +$120C / +$110P / -$105P for $4.50
  - Reset strikes to current level
  - Regain upside leverage

**Result:**
- Profit from first position: $3.50
- New position: $4.50 cost, fresh leverage
- **Total exposure:** Still in trade but with better risk-reward

**When to roll:**
- Original position >+100% ROI
- Stock still has momentum (trend continuing)
- 14+ DTE remaining (enough time)
- **Don't roll if <10 DTE** (time running out)

**Adjustment 2: Roll down (stock dropping but thesis intact)**

**Scenario:**
- Entered: $100 stock, +$105C / +$95P / -$90P for $4.50
- Now: $93 stock (10 days later), position at $3 (-$1.50 loss)
- Near put strikes, losing to theta daily
- **Thesis:** Still bullish long-term, stock just pulled back

**Adjustment:**
- **Close current position** at $3 (accept $1.50 loss)
- **Open new position** at current price:
  - +$98C / +$88P / -$83P for $4.00
  - Adjust all strikes down by $7
  - Regain bullish exposure at new level

**Result:**
- Loss from first position: -$1.50
- New position: $4.00 cost, fresh setup
- Total capital: $7.50 at risk
- **Breakeven now:** $98 + $4 = $102 (vs. original $109.50)

**When to roll down:**
- Thesis still valid (no fundamental change)
- Stock pulled back to support
- 14+ DTE remaining
- **Cost of adjustment < 50% of original debit**

**Adjustment 3: Add calendar spread (need more time)**

**Scenario:**
- Entered: 30 DTE position for $4.50
- Now: 15 DTE, stock flat at $100, position at $3.50 (-$1 loss)
- Theta accelerating, need more time for thesis to play out
- **Problem:** Don't want to close (thesis still valid) but running out of time

**Adjustment:**
- **Keep current position** (30 DTE → now 15 DTE)
- **Add farther-dated position** (45 DTE):
  - +$105C / +$95P / -$90P (45 DTE) for $5.50
  - Same strikes, longer expiration
- Now have TWO positions at different dates

**Result:**
- Combined theta: Slower decay (averaging 15 DTE and 45 DTE)
- Total capital: $4.50 + $5.50 = $10
- **More time** for thesis to develop

**When to add calendar:**
- Strong conviction in thesis
- Willing to commit more capital
- Near-term position not yet profitable
- Far-term position reasonably priced (IV still low)

**Caution:** This is adding to a loser. Only do if:
- Thesis unchanged
- No more than 1× original capital
- **Not out of desperation** (accept loss if thesis broken)

**Adjustment 4: Convert to spread (take risk off)**

**Scenario:**
- Entered: +$105C / +$95P / -$90P for $4.50
- Now: Stock at $118, position at $12 (+$7.50 profit, +167%)
- You've made good profit but worried about pullback
- **Want:** Lock in some profit, keep some upside

**Adjustment:**
- **Sell higher call** to create call spread:
  - Current: +$105C / +$95P / -$90P
  - Add: -$125C (sell call 7 points above current price)
  - **New: +$105C/-$125C call spread** + put spread

**Result:**
- Collect premium for $125 call (e.g., $2.00)
- Now have defined max profit at $125
- **Protected against pullback** (locked in some gains)
- But cap upside at $125

**When to use:**
- Already up 100-200%
- Concerned about reversal
- Want to stay in trade but reduce risk
- **Good compromise** vs. full exit

### 3. Volatility Skew Exploitation

**Understanding put skew:**

In equity markets, puts trade at higher IV than calls:
- ATM call IV: 25%
- ATM put IV: 27%
- 10% OTM put IV: 30%
- **Put skew = +5% IV** (puts more expensive)

**How reverse jade lizard exploits this:**

**Long call (low IV):**
- OTM call at 23% IV (cheaper)
- Buy cheap volatility

**Long put (high IV):**
- ATM put at 27% IV (expensive)
- But you're buying protection, so willing to pay

**Short put (highest IV):**
- OTM put at 30% IV (most expensive!)
- **Sell expensive volatility** to reduce cost

**Net effect:**
- Selling the most expensive option (OTM put)
- Buying cheap call + expensive put
- **Skew reduces net debit by 10-20%**

**Example with skew:**

**Stock at $100, with skew:**
- Buy $105 call (23% IV): $2.80 (cheaper due to low IV)
- Buy $95 put (27% IV): $2.60
- Sell $90 put (30% IV): $1.40 (higher credit due to high IV)
- **Net: $2.80 + $2.60 - $1.40 = $4.00**

**Stock at $100, without skew (all 25% IV):**
- Buy $105 call: $3.00
- Buy $95 put: $2.40
- Sell $90 put: $1.00
- **Net: $3.00 + $2.40 - $1.00 = $4.40**

**Savings from skew: $0.40 (10% cheaper!)**

**When skew is most pronounced:**

**Post-crash:**
- Market just dropped 10-20%
- Fear high, put demand surges
- Put skew steepens to 40-50% IV for OTM puts
- **Best time to sell OTM puts** (collect huge premium)

**Pre-earnings:**
- Downside protection demand (scared of miss)
- OTM puts bid up
- Skew increases
- **Good for reducing debit**

**Avoid when skew is flat:**
- Calm markets
- VIX very low
- Skew collapses
- **Less advantageous** (can't exploit skew)

### 4. Rolling Strategies

**When to roll (vs. close):**

**Roll if:**
- Thesis still valid
- Willing to commit more capital (if needed)
- 14+ DTE remaining
- **Want to stay in trade** with better strikes

**Close if:**
- Thesis invalidated
- <10 DTE remaining
- Position deep underwater (can't recover)
- **Better opportunities elsewhere**

**Rolling up (profitable position, want more leverage):**

**Original:**
- +$105C / +$95P / -$90P
- Stock now $115, position worth $12 (up from $5)
- Profit: $7 (+140%)

**Roll to:**
- Close original: Sell at $12
- Open new: +$120C / +$110P / -$105P for $5.50
- **Net effect:** Took $6.50 profit ($12 - $5.50), still in trade

**Why roll up:**
- Original call now deep ITM (delta ~0.90, little leverage left)
- New call OTM (delta ~0.40, better leverage)
- **Free roll** (extracted profit, still in trade)

**Rolling down (losing position, want better breakeven):**

**Original:**
- +$105C / +$95P / -$90P for $5
- Stock now $93, position worth $3.50
- Loss: -$1.50

**Roll to:**
- Close original: Buy back at $3.50
- Open new: +$98C / +$88P / -$83P for $4.50
- **Net effect:** Lost $1.50, committed new $4.50, total $6 at risk

**Why roll down:**
- Original breakeven too far ($110 → now need 18% rally)
- New breakeven closer ($98 + $4.50 = $102.50 → only 10% rally)
- **Better odds** of recovery

**Caution:**
- You're adding to loser (risky)
- Only if thesis unchanged
- **Not out of hope** (must have reason to believe in recovery)

**Rolling for time (extend duration):**

**Original:**
- 30 DTE position, now 10 DTE
- Stock flat, position underwater
- Need more time

**Roll to:**
- Close 10 DTE position
- Open 40 DTE position (same strikes or adjust)
- **Pay additional debit** (buying more time)

**Why roll for time:**
- Thesis needs more time to develop
- No need to adjust strikes (just time)
- **Accept higher cost** for extra duration

**Cost:**
- Typically pay 30-50% more than original debit
- Example: Original $5, roll costs $2.50 additional → Total $7.50

### 5. Tax Considerations

**Holding period:**

**Short-term capital gains (<1 year):**
- Options held <365 days
- Taxed at ordinary income rate (up to 37%)
- **Most reverse jade lizards are short-term** (held 2-4 weeks)

**Long-term capital gains (>1 year):**
- Options held >365 days
- Taxed at lower rate (0%, 15%, or 20%)
- **Rare for this strategy** (don't hold options 1 year)

**Wash sale rule:**

**What is it:**
- Can't claim loss if you rebuy "substantially identical" position within 30 days
- **Example:**
  - Lose $1000 on AAPL reverse jade lizard
  - Buy another AAPL reverse jade lizard within 30 days
  - **Can't deduct the $1000 loss!**

**How to avoid:**
- Wait 31 days before re-entering same stock
- Or trade different stock/index
- **Don't let taxes drive trades** (but be aware)

**Tax loss harvesting:**

**Strategy:**
- If you have losing positions in December
- Close them before year-end
- **Realize losses** to offset gains from other trades

**Example:**
- Year-to-date: +$10,000 in gains (other trades)
- Losing reverse jade lizard: -$2,000 (unrealized)
- **Close in December** → Realize -$2,000 loss
- Net taxable income: $10,000 - $2,000 = $8,000
- **Save $740 in taxes** (at 37% rate)

**Caution:**
- Don't close profitable trades just for taxes
- **Let profits run**, don't let tax tail wag dog
- Losses can offset gains, but not worth taking bad loss to save taxes

### 6. Position Sizing Across Portfolio

**Kelly Criterion (advanced):**

$$
f^* = \frac{p \cdot b - q}{b}
$$

where:
- $f^*$ = Fraction of capital to risk
- $p$ = Probability of winning
- $q$ = Probability of losing (= $1 - p$)
- $b$ = Payoff ratio (reward/risk)

**Example:**
- Win probability: $p = 35\%$ (based on historical data)
- Lose probability: $q = 65\%$
- Payoff: If win, gain $8 on $5 risk → $b = 1.6$

$$
f^* = \frac{0.35 \times 1.6 - 0.65}{1.6} = \frac{0.56 - 0.65}{1.6} = \frac{-0.09}{1.6} = -5.6\%
$$

**Wait, negative?** This means don't take the trade! (Expected value is negative.)

Let me recalculate with more realistic numbers:
- Win probability: $p = 35\%$
- Payoff: Win $10 on $5 risk → $b = 2.0$

$$
f^* = \frac{0.35 \times 2.0 - 0.65}{2.0} = \frac{0.70 - 0.65}{2.0} = \frac{0.05}{2.0} = 2.5\%
$$

**Interpretation:** Risk 2.5% of capital per trade (max).

**But use fractional Kelly:**
- Full Kelly is too aggressive (large drawdowns)
- Use **1/4 Kelly** or **1/2 Kelly**
- Example: 1/4 × 2.5% = **0.625%** (risk per trade)

**For most traders:**
- Ignore Kelly (too complex)
- Simple rule: **Risk 1-2% per trade**
- This is close to 1/4 or 1/2 Kelly in most cases

**Diversification across time:**

**Don't enter all positions at once:**

**Bad:**
- Enter 5 reverse jade lizards on same day
- All expire same date
- **If macro event hurts, all lose together**

**Good:**
- Enter 1 per week over 5 weeks
- Different expirations (stagger by 7-10 days)
- **Spreads risk over time**

**Diversification across underlyings:**

**Avoid concentration:**
- Don't put 3 trades on tech stocks
- If tech sector crashes, **all lose**

**Better:**
- 1 tech (AAPL)
- 1 consumer (NKE)
- 1 healthcare (JNJ)
- 1 financial (JPM)
- **Sector diversification** reduces correlation

**Correlation management:**

**High correlation pairs (avoid):**
- AAPL + MSFT (both tech)
- XOM + CVX (both energy)
- **Move together** → No diversification benefit

**Low correlation pairs (good):**
- AAPL + JNJ (tech vs. healthcare)
- SPY + GLD (equity vs. gold)
- **Move independently** → True diversification

**Portfolio Greeks management:**

**Track aggregate Greeks:**

If you have 3 positions:
- Position 1: Delta +$100, Vega +$50
- Position 2: Delta +$80, Vega +$40
- Position 3: Delta +$120, Vega +$60
- **Net: Delta +$300, Vega +$150**

**Watch for:**
- Delta too high (>$500): Too much directional risk
- Vega too high (>$200): Too much volatility risk
- **Diversify Greeks** across positions

**Example hedge:**
- If net delta too high (+$400)
- Add negative delta position (short call spread)
- Or take profit on some winning trades
- **Bring net delta** to +$200 (more balanced)

---

---



## Summary and Key Takeaways

**Reverse jade lizard is a bullish debit strategy combining:**
- Long call (unlimited upside)
- Long put spread (limited downside protection)
- Defined maximum risk
- Best for strong bullish conviction with crash hedging

**Optimal conditions:**
- **Low IV** (<30th percentile) - Critical for low cost
- **Bullish technical setup** (bull flag, consolidation)
- **Clear catalyst** (earnings, FDA approval) in 20-40 days
- **30-45 DTE** (sweet spot for theta vs. time)

**Risk-reward profile:**
- Max loss: Net debit (typically 3-6% of stock price)
- Max downside profit: Put spread width - debit (small, e.g., +$0.50)
- Max upside profit: **Unlimited** (long call)
- Breakeven: Long call strike + net debit
- **Need 8-12% rally** to break even typically

**Greeks:**
- Delta: +0.05 to +0.15 initially (small bullish bias)
- Gamma: Mixed (positive far from strikes, best above current price)
- Theta: -$0.05 to -$0.10 per day (time decay hurts, need quick moves)
- Vega: +0.20 to +0.30 (benefits from IV expansion)

**When to use:**
- Strong bullish thesis (need >10% move)
- Want crash protection (put spread softens blow)
- Low IV environment (options cheap)
- Specific catalyst upcoming (not just hope)
- **Willing to pay debit** for defined risk

**When to avoid:**
- High IV (>60th percentile) - too expensive
- Downtrend or flat market - needs strong rally
- <21 DTE - insufficient time
- No clear catalyst - low probability

**Management rules:**
- Take 50% off at +100% ROI (lock in profit)
- Exit by 14 DTE if not profitable (theta too strong)
- **Hard exit by 7 DTE** (no exceptions!)
- Roll if thesis intact and 14+ DTE remaining
- Close immediately if thesis invalidated

**Position sizing:**
- Risk 1-2% of account per trade
- For $50k account: Risk $500-$1000 → 1 contract typically
- **Never risk >5% on single trade**
- Diversify across sectors and time

**Success factors:**
- **Low IV entry** (single most important factor)
- Strong catalyst within 20-40 days
- Disciplined exits (take profit at target, cut losses at 14 DTE)
- Proper position sizing (survive to win)
- Record keeping (learn from each trade)

**This strategy is for:**
- Traders with strong bullish conviction
- Those wanting defined risk (vs. risk reversal)
- Low IV environments (patient entry)
- Catalyst-driven trades (earnings, events)
- **Not for beginners** (complex, needs experience with Greeks)

**Bottom line:** Reverse jade lizard is a sophisticated bullish strategy that offers unlimited upside with limited downside protection, best suited for experienced options traders who can time entries at low IV, identify strong catalysts, and execute disciplined trade management. The asymmetric risk-reward favors bulls, but requires patience for proper setup and conviction to weather theta decay while waiting for the big move.