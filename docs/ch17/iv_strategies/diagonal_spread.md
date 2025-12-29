# Diagonal Spreads

**Diagonal spreads** are option strategies where you **buy and sell options of the same type** (calls or puts) with **different strike prices AND different expiration dates**. They combine the ideas of **vertical spreads (different strikes)** and **calendar spreads (different expirations)** to create positions that can profit from **time decay, direction, and/or volatility changes** with **defined (or mostly-defined) risk**.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/diagonal_spread_bullish.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/diagonal_spread_greeks.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/diagonal_spread_rolling.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/diagonal_spread_vs_calendar.png?raw=true" alt="long_call_vs_put" width="700">
</p>

---

## The Core Insight

**The fundamental idea:**

- Options closer to expiration decay faster (higher theta)
- Options farther out decay slower (lower theta)
- So you can **own a longer-dated option** and **sell a shorter-dated option** against it
- Repeatedly “rent out” the short-term option premium
- Keep some directional exposure via strike choices
- Often reduces cost vs. buying a long option outright

**The key equation (intuition):**

\[
\text{Edge} \approx \text{Theta collected on short} - \text{Theta paid on long}
\]

You’re essentially betting:
> “Time decay will work for me, and the underlying won’t move too far against my structure before I can manage it.”

---

## What Is a Diagonal Spread?

### The Structure

A diagonal spread uses:

- **Same option type**: call/call or put/put
- **Different strikes**: \(K_1 \neq K_2\)
- **Different expirations**: \(T_1 \neq T_2\)

**Typical construction (most common):**

- **BUY** a longer-dated option (back month)
- **SELL** a shorter-dated option (front month)

This is often called a **diagonal calendar**.

---

## Why Diagonals Exist

### 1. Turn Time Decay into an Asset
Long options pay theta.
But diagonals can be structured so the **short option’s theta** helps offset (or exceed) what you pay on the long option.

### 2. Flexible Directional Bias
By choosing strikes:

- **Bullish diagonal (calls)**: long call is ITM/ATM, short call is OTM
- **Bearish diagonal (puts)**: long put is ITM/ATM, short put is OTM

### 3. Capital Efficiency (Key Use Case)
A major practical diagonal is the **Poor Man’s Covered Call (PMCC)**:

- A long-dated ITM call replaces owning 100 shares
- You sell short-dated calls against it for income

---

## Types of Diagonal Spreads

### 1) Call Diagonal (Bullish / Income)

**Structure:**

- Buy a longer-dated call (often ITM)
- Sell a shorter-dated call (often OTM)

**Goal:** collect short-call premium while keeping bullish upside.

### 2) Put Diagonal (Bearish / Income)

**Structure:**

- Buy a longer-dated put (often ITM)
- Sell a shorter-dated put (often OTM)

**Goal:** collect short-put premium while keeping bearish exposure.

### 3) Neutral / Range Diagonal
Strikes chosen closer to spot, aiming to profit primarily from **time decay** and **mean reversion**, but this is more sensitive and requires tighter management.

---

## The Portfolio

### Call Diagonal (generic)

\[
\Pi = C(S, K_{\text{long}}, T_{\text{long}}) - C(S, K_{\text{short}}, T_{\text{short}})
\]

where \(T_{\text{long}} > T_{\text{short}}\).

### Put Diagonal (generic)

\[
\Pi = P(S, K_{\text{long}}, T_{\text{long}}) - P(S, K_{\text{short}}, T_{\text{short}})
\]

where \(T_{\text{long}} > T_{\text{short}}\).

**Greeks (typical):**

- **Delta:** depends on strikes; usually directional
- **Theta:** can be **positive** (if short theta dominates)
- **Vega:** often **positive-ish** (because you’re net long longer-dated vol)
- **Gamma:** usually small vs. pure short-term positions, but short leg can create assignment/pin risk near expiry

---


---

## Economic Interpretation

**Understanding what this strategy REALLY represents economically:**

### The Core Economic Trade-Off

This IV strategy involves specific economic trade-offs around volatility exposure. The key is understanding what you're giving up versus what you're gaining in terms of implied volatility positioning.

**Economic equivalence:**

$$
\text{Strategy P\&L} = \text{IV Change Component} + \text{Term Structure Component} + \text{Skew Component}
$$

### Why This IV Structure Exists Economically

Markets create these IV structures because different participants have different:
- Volatility expectations (near-term vs. long-term)
- Risk preferences (convexity vs. theta)
- Event views (known catalysts vs. unknown volatility)
- Hedging needs (portfolio protection vs. income generation)

### The Volatility Risk Premium

Most IV strategies exploit the **volatility risk premium** - the empirical observation that:

$$
\text{Implied Volatility} > \text{Realized Volatility} \quad \text{(on average)}
$$

**Why this exists:**
1. **Insurance value:** Investors pay premium for protection
2. **Crash insurance:** Fear of tail events inflates IV
3. **Supply/demand:** More vol buyers than sellers
4. **Behavioral biases:** Overestimation of future volatility

### Professional Institutional Perspective

Institutional traders view IV strategies as tools for:
1. **Volatility arbitrage:** Extracting the vol risk premium
2. **Term structure trading:** Exploiting mispricings across time
3. **Skew trading:** Capturing mispricing across strikes
4. **Surface arbitrage:** Finding no-arbitrage violations

Understanding the economic foundations helps you recognize when IV offers genuine edge versus when market pricing is fair.


## Concrete Example 1: Bullish Call Diagonal (PMCC Style)

**Setup:**

- Stock at \(S = 100\)
- You’re moderately bullish, but want income

**Trade:**

- Buy 90-day **$90 call** (ITM) for **$14**
- Sell 30-day **$105 call** (OTM) for **$2**

**Net debit:** \(14 - 2 = 12\) (=$1,200 per spread)

**Intuition:**

- The long ITM call behaves like stock (high delta)
- The short OTM call brings in premium and decays quickly
- If the short expires worthless, you can sell another one next month

**Key outcomes at the short expiration (30 days):**

- If stock is below $105: short expires worthless → keep premium, continue
- If stock rises above $105: short may be assigned → you manage by rolling/closing

---

## Concrete Example 2: Bearish Put Diagonal

**Setup:**

- Stock at \(S = 100\)
- You expect mild decline or sideways, want bearish tilt

**Trade:**

- Buy 90-day **$110 put** (ITM) for **$13**
- Sell 30-day **$95 put** (OTM) for **$2**

**Net debit:** \(13 - 2 = 11\)

**Goal:**

- If stock stays above $95: short put decays → keep premium
- If stock drops toward $95: position gains delta, but manage assignment risk

---

## Strike Selection Strategy

### Long Leg (Back Month)

**Common approach:**

- Choose **ITM** (especially for PMCC)
  - Higher delta (more stock-like)
  - Less theta decay per day (relative)
  - More intrinsic value, less “wasting” time value

**Rule of thumb (practitioner-style):**

- Long call delta ~ **0.70–0.85** for PMCC-style diagonals
- Long put delta ~ **-0.70 to -0.85** for bearish diagonals

### Short Leg (Front Month)

**Common approach:**

- Choose **OTM** at a strike where you’re “willing” to cap near-term move
- You want meaningful premium but not too close to the money

**Rule of thumb:**

- Short call delta ~ **0.20–0.35**
- Short put delta ~ **-0.20 to -0.35**

---

## Time Frame Selection

### Typical expirations

- Long leg: **60–180 days**
- Short leg: **20–45 days**

**Why this works:**

- The short leg has relatively high theta decay
- The long leg is more stable, giving you time to adjust

**PMCC preference:**

- Long leg often **90–180 days** (or LEAPS 1–2 years for more stability)
- Short leg often **~30–45 days** and rolled repeatedly

---

## Position Management

### 1) Close or Roll the Short Leg

If the short option is:

- **Profitable early** (e.g., you’ve captured 50–80% of its premium), consider buying it back and reselling a new one.
- **Threatened** (stock approaching short strike), you can:
  - **Roll up and out** (calls) / **roll down and out** (puts)
  - Convert the position into a different structure (e.g., vertical)
  - Close the entire diagonal

### 2) Avoid Holding the Short Leg into Expiration (Often)

Near expiration:

- gamma risk increases
- pin risk increases
- assignment becomes more likely

Many traders close/roll with **~7–14 days** left, especially if the short is near the money.

### 3) Assignment Handling (Important)

If a short call gets assigned, you may end up short shares.
If a short put gets assigned, you may end up long shares.

**Practical approach:**

- manage by rolling before assignment becomes likely
- avoid short options that are deep ITM near expiry unless you intend assignment

---

## Pros and Cons

### Diagonals — Advantages ✓
**1. Flexible design**

- Can be bullish, bearish, or neutral-ish

**2. Can generate income**

- Short leg premium can offset long leg cost

**3. Better capital efficiency**

- Especially PMCC: stock-like exposure with less capital than buying shares

**4. Often improved “cost basis” over time**

- Repeated short premium can reduce effective cost of the long option

### Diagonals — Disadvantages ✗
**1. More moving parts**

- Strike + expiration choices matter a lot

**2. Assignment and pin risk on the short leg**

- Especially near expiration

**3. Not fully defined risk in practice (sometimes)**

- If assignment happens unexpectedly, you can temporarily hold stock exposure
- Still manageable, but requires comfort with mechanics

**4. Directional whipsaws**

- Sudden moves can hurt if short leg gets challenged and long leg loses value (or IV shifts)

---


---

## Real-World Examples

[Concrete IV strategy examples]



---

## Practical Guidance

**Step-by-step implementation framework:**

### Step 1: Volatility Environment Assessment

**Before entering, evaluate:**

1. **IV level analysis:**
   - Current IV percentile (IVP) or IV rank (IVR)
   - Is IV historically high or low?
   - IV vs. realized volatility spread

2. **Term structure analysis:**
   - Shape of vol term structure (contango/backwardation)
   - Front month vs. back month IV relationship
   - Event-driven distortions in term structure

3. **Skew analysis:**
   - Put vs. call IV differential
   - Shape of vol smile/smirk
   - Unusual skew steepness

4. **Upcoming events:**
   - Earnings announcements
   - Fed meetings, economic data
   - Product launches, regulatory decisions

### Step 2: Strategy Selection Criteria

**Enter this strategy when:**
- [Specific IV conditions]
- [Term structure requirements]
- [Skew positioning]
- [Time to event/expiration]

**Avoid this strategy when:**
- [Unfavorable IV environment]
- [Wrong term structure shape]
- [Insufficient IV edge]
- [Event risk too high]

### Step 3: Position Sizing

**Calculate maximum position size:**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Loss Per Contract}}
$$

**For IV strategies, consider:**
- Vega exposure limits ($ per 1% IV move)
- Theta collection goals ($ per day target)
- Gamma risk near expiration
- Capital at risk for defined-risk strategies

**Conservative sizing:**
- Max vega: $100-200 per 1% IV move per $10k capital
- Max theta: $20-50 per day per $10k capital
- Risk 1-2% on undefined risk strategies
- Risk 2-5% on defined risk strategies

### Step 4: Entry Execution

**Best practices:**

1. **IV analysis first:** Check IV percentile before entry
2. **Liquidity check:** Ensure tight bid-ask spreads
3. **Multi-leg orders:** Enter complete structure as one order
4. **Timing considerations:** 
   - Sell vol when IV elevated (IVR > 50)
   - Buy vol when IV depressed (IVR < 30)
   - Avoid entering right before events (IV usually elevated)

**Entry checklist:**
- [ ] IV percentile checked
- [ ] Term structure analyzed
- [ ] Liquidity verified (bid-ask < 10%)
- [ ] Position sized appropriately
- [ ] Greeks calculated (delta, vega, theta, gamma)
- [ ] Max loss understood
- [ ] Exit plan defined

### Step 5: Position Management

**Active management rules:**

**IV monitoring:**
- Track IV daily (minimum)
- Monitor IV percentile changes
- Watch term structure shifts
- Alert on IV expansion/contraction

**Profit targets:**
- **For short vol:** Close at 50-75% of max profit
- **For long vol:** Take profit at 100-200% gain
- **For term structure:** Close when term structure normalizes

**Loss limits:**
- **For short vol:** Close at 2-3x credit received
- **For long vol:** Cut at 50% loss
- **Time stop:** Exit if 50% of time passed with no favorable IV move

**Adjustment triggers:**
- IV percentile moves 20+ points
- Term structure inverts unexpectedly
- Underlying makes large move (>2 SD)
- Event announced/cancelled

### Step 6: Adjustment Protocols

**When to adjust:**

**For short vol strategies:**
- Stock moves significantly against position
- IV expanding beyond entry level
- Risk of max loss approaching

**How to adjust:**
- Roll out in time (collect more theta)
- Roll strikes (move to new delta)
- Convert to different structure (spread to iron condor)
- Close and reenter at better strikes

**For long vol strategies:**
- IV not expanding as expected
- Theta burn exceeding plan
- Realized vol lower than expected

**How to adjust:**
- Scale into more contracts if IV crashes
- Roll to longer dated (reduce theta)
- Take partial profits on IV spikes
- Convert to calendar (neutralize theta)

### Step 7: Record Keeping

**Track every trade:**
- Entry IV level and percentile
- Term structure shape at entry
- Vega, theta, gamma at entry
- Days to expiration
- P&L by component (vega, theta, gamma)
- Actual IV vs. entry IV
- Lessons learned

**Quarterly review:**
- Win rate by IV percentile
- P&L by term structure shape
- Best entry IV conditions
- Common mistakes

### Common Execution Mistakes to Avoid

1. **Selling vol at low IV** - IVR < 30 usually poor for short vol
2. **Buying vol at high IV** - IVR > 70 often too expensive for long vol
3. **Ignoring term structure** - Don't sell front month if in backwardation
4. **Over-leveraging vega** - Too much vega exposure can blow up account
5. **Holding through earnings** - IV crush destroys long vol positions
6. **Not taking profits** - Greed kills short vol profits
7. **Fighting IV trends** - IV regimes can persist
8. **Ignoring skew** - Put skew can make bearish trades expensive

### Professional Implementation Tips

**For volatility selling (short vega):**
- Enter when IVR > 50, ideally > 70
- Target 60-70% probability of profit
- Close at 50% of max profit
- Use mechanical stops (2x credit)

**For volatility buying (long vega):**
- Enter when IVR < 30
- Need catalyst for IV expansion
- Take profits quickly on IV spikes
- Cut losses at 50% if IV doesn't cooperate

**For term structure trades:**
- Understand event calendar
- Check historical term structure patterns
- Monitor roll dynamics
- Scale positions gradually

**For skew trades:**
- Understand why skew exists in that stock
- Check historical skew patterns
- Combine with directional view
- Monitor skew changes daily


## Common Mistakes

### 1) Buying a Long Leg with Too Little Time
If the long option expires soon, theta decay can overwhelm the strategy.

**Fix:** use a longer-dated long leg (60–180 days or more).

### 2) Selling the Short Leg Too Close to the Money
You collect more premium but increase assignment risk and cap upside too aggressively.

**Fix:** start with OTM short strikes and adjust gradually.

### 3) Holding the Short Leg Too Close to Expiration
Pin risk and gamma explode.

**Fix:** roll/close earlier (commonly 7–14 days remaining).

### 4) Ignoring Implied Volatility
If IV collapses, long leg can lose value.

**Fix:** avoid overpaying for the long leg; consider entering after volatility spikes when appropriate.

### 5) Over-sizing Because It “Feels Covered”
PMCC is not identical to a covered call.
Your long call can lose value sharply.

**Fix:** size conservatively and treat it as an options position with real risk.

---

## When to Use Diagonals

### Best conditions

- You have a **directional bias** (mild/moderate)
- You want to **benefit from theta** (short leg decay)
- You’re comfortable managing rolls and avoiding assignment surprises

### Avoid when

- Big binary event risk inside the short leg (earnings, FDA, etc.)
- You cannot monitor or manage assignment/rolls
- Liquidity is poor (wide bid-ask spreads)

---


---

## Worst Case Scenario

**What happens when everything goes wrong:**

### The Nightmare Setup

**How it starts:**
- [IV moves against position]
- [Term structure inverts unexpectedly]
- [Unexpected catalyst emerges]
- [Position deteriorating rapidly]

**The deterioration:**

**Week 1:**
- [Early warning signs in IV]
- [Position losing value]
- [IV percentile moving adversely]
- [Critical decision point: hold or fold?]

**Through expiration:**
- [Continued adverse IV dynamics]
- [Maximum loss approached/realized]
- [Final devastating outcome]

### Maximum Loss Calculation

**Worst case mathematics:**

For defined risk IV strategies:

$$
\text{Max Loss} = \text{Debit Paid} \quad \text{(for debit strategies)}
$$

$$
\text{Max Loss} = \text{Spread Width} - \text{Credit} \quad \text{(for credit strategies)}
$$

For undefined risk IV strategies:

$$
\text{Max Loss} = \text{Unlimited} \quad \text{(naked short positions)}
$$

**Example calculation:**
- Position: [Specific IV structure]
- Entry IV: [Level and percentile]
- Adverse scenario: [What went wrong]
- **Loss: [Calculation]**
- **Impact: [% of portfolio]**

### What Goes Wrong

The worst case occurs when:

**For short volatility strategies:**
1. **Wrong IV direction:** IV explodes instead of contracting
2. **Wrong timing:** IV spike happens immediately
3. **Wrong magnitude:** IV move much larger than expected
4. **Black swan:** Unpredicted major event (crash, war, etc.)

**For long volatility strategies:**
1. **Wrong IV direction:** IV crushes instead of expanding
2. **Wrong timing:** Theta decay faster than IV gain
3. **Wrong catalyst:** Expected catalyst doesn't materialize
4. **IV collapse:** Sudden IV crush (post-earnings, resolution of uncertainty)

**For term structure strategies:**
1. **Term structure inversion:** Front month IV explodes relative to back
2. **Event surprise:** Unexpected event distorts normal term structure
3. **Roll dynamics:** Unfavorable roll yield
4. **Gamma explosion:** Front month gamma blows up

### The Cascade Effect

**Multiple compounding failures:**

**Trade 1: Initial short vol loss**
- Sold premium at IVR 60 (thought it was high enough)
- Market crashes, IV explodes to IVR 100
- Loss: $2,000 (max loss on position)

**Trade 2: Panic adjustment**
- Roll position out and down
- Pay $500 to roll
- Market continues lower
- Loss: Another $1,500

**Trade 3: Desperation**
- Double position size to "average down"
- IV continues high
- Assignment risk at expiration
- Loss: $3,000

**Total damage:**
- Cumulative loss: $7,000
- Portfolio impact: 14% of $50k account
- Emotional damage: Severe
- Time to recover: Months

### Real Disaster Scenarios

**Short volatility blow-up (February 2018 Volmageddon):**
- VIX inverse products imploded
- XIV (short vol ETN) lost 90%+ in one day
- Selling vol when VIX at 10-12
- VIX spiked to 50+
- Traders who sold naked vol destroyed
- **Many accounts wiped out entirely**

**Long volatility decay (2017):**
- Bought VIX calls expecting volatility
- VIX stayed suppressed entire year (8-12 range)
- Theta decay relentless month after month
- Traders lost 50-80% waiting for vol spike
- **Death by a thousand theta cuts**

**Term structure inversion (COVID March 2020):**
- Calendar spreads assumed normal term structure
- Front month IV exploded relative to back month
- Term structure inverted violently
- Calendar spreads lost 200-300%
- **"Safe" calendar spreads destroyed**

**Earnings IV crush disaster:**
- Bought straddle into earnings at IVR 90
- IV was 80% before earnings
- Earnings came, stock moved 5% (decent move)
- But IV crushed to 30%
- Straddle lost 40% despite stock moving
- **Directionally right, still lost big**

### The Gamma Blow-Up

**Worst case for short vol at expiration:**

**Friday 3:00pm:**
- Stock at $100.00
- Short $100 straddle (naked)
- Thought it would expire worthless
- **Net delta: 0, everything looks safe**

**Friday 3:59pm:**
- Stock drops to $99.50
- Puts now ITM
- **Net delta: -10,000 shares (100 contracts)**

**Monday morning:**
- Gap down to $95
- Must cover 10,000 shares at market
- Slippage on assignment
- **Loss: $45,000 on what was $2,000 credit**

**This is pin risk + gamma explosion at expiration**

### IV Regime Persistence

**The long grind:**

**Month 1:** Sold vol at IVR 50, expecting mean reversion
- IV stays elevated, position down 30%

**Month 2:** Rolled position, paid debit
- IV still elevated, position down 50%

**Month 3:** Rolled again, more debit
- IV finally normalizing but already lost 60%

**Month 4:** Position finally profitable
- Net result: -40% over 4 months

**The lesson:** IV regimes can persist much longer than you can stay solvent. Mean reversion is real but timing is impossible.

### Psychology of IV Losses

**Emotional stages:**
1. **Confidence:** "IV is too high, easy short"
2. **Concern:** "IV going up but it'll revert"
3. **Denial:** "This is temporary, just need to wait"
4. **Panic:** "Close everything NOW!"
5. **Capitulation:** "I'll never trade vol again"
6. **Learning:** "What did I miss about IV regimes?"

**Winning trader mindset:**
- Respect IV percentile religiously
- Accept that IV can stay irrational
- Cut losses mechanically
- Don't fight IV regime changes
- Learn and adapt

### Preventing Worst Case

**Risk management strategies:**

**1. Position sizing by vega exposure:**
```
Max vega = $100-200 per 1% IV move per $10k capital
If position has $500 vega → 2.5-5% of $50k account max
```

**2. IV percentile discipline:**
```
Only sell vol when IVR > 50 (preferably > 70)
Only buy vol when IVR < 30
No exceptions
```

**3. Mechanical stops:**
```
Short vol: Close at 2-3x credit received
Long vol: Close at 50% loss
Calendar: Close at 50% loss
```

**4. Diversification:**
```
Multiple underlyings
Different expiration cycles
Mix of IV strategies
Never all-in on one IV bet
```

**5. Defined risk structures:**
```
Prefer spreads to naked options
Iron condors > short strangles
Butterflies > naked shorts
Accept lower profit for capped risk
```

**6. Event awareness:**
```
Know earnings dates
Monitor VIX levels
Track macro events
Avoid vol selling before major events
```

### The Ultimate Protection

**Hard rules for IV trading:**

$$
\text{Position Vega} < \frac{\text{Portfolio} \times 0.02}{\text{1\% IV Move}}
$$

$$
\text{If IVR} < 30: \text{No short vol positions}
$$

$$
\text{If IVR} > 70: \text{Be cautious with long vol}
$$

$$
\text{Max Loss} < 5\% \text{ of portfolio}
$$

**Remember:** The market can remain irrational (high/low IV) longer than you can remain solvent. One bad IV trade can wipe out months of profits. Proper position sizing and discipline determine survival.

**The iron law of volatility trading:** You will experience worst case. It's not "if" but "when." Your survival depends on position sizing and mechanical risk management, not on being right about IV direction.



---

## Best Case Scenario

**What happens when everything goes right:**

### The Perfect Setup

**Ideal entry conditions:**
- [IV at optimal level for strategy]
- [Term structure favorably positioned]
- [Skew supporting the trade]
- [Timing aligned with catalyst/events]

**The optimal sequence:**

**Week 1:**
- [IV moves as anticipated]
- [Term structure behaves favorably]
- [Position accumulating profit]
- [Greeks performing as expected]

**Through expiration:**
- [Continued favorable IV dynamics]
- [Optimal IV/RV relationship]
- [Maximum profit zone reached]
- [Exit at optimal timing]

### Maximum Profit Achievement

**Best case mathematics:**

$$
\text{Max Profit} = \text{Vega P\&L} + \text{Theta P\&L} - \text{Gamma Loss}
$$

**Example calculation:**
- Position: [Specific IV structure]
- Entry IV: [Level and percentile]
- Vega exposure: [$ per 1% IV]
- Theta collection: [$ per day]
- **Scenario:**
  - IV moves from [X]% to [Y]%
  - Time passes: [N] days
  - Stock movement: [Favorable/minimal]
- **Profit: [Calculation]**
- **ROI: [Percentage]**

### What Makes It Perfect

The best case requires:
1. **Right IV direction:** IV moves as anticipated (up for long vol, down for short vol)
2. **Right timing:** IV move happens in time frame expected
3. **Right term structure:** Front/back relationship evolves favorably
4. **Right underlying movement:** Stock moves (or doesn't move) as needed
5. **Right skew:** Put/call differential behaves as expected

### IV Component Breakdown

**Vega P&L:**
- Entry IV: [Level]
- Exit IV: [Level]
- Vega position: [$ per 1%]
- **Vega profit: [Calculation]**

**Theta P&L:**
- Days passed: [N]
- Daily theta: [$ per day]
- **Theta profit/cost: [Calculation]**

**Gamma P&L:**
- Stock moves: [Minimal/favorable]
- Rebalancing: [Minimal/profitable]
- **Gamma impact: [Calculation]**

**Net P&L:** Sum of all components

### Comparison to Alternatives

**This strategy vs. [Alternative IV approach]:**
- [IV exposure comparison]
- [Risk-reward analysis]
- [When this strategy wins]
- [Capital efficiency]

### Professional Profit-Taking

**For short volatility:**
- Close at 50-75% of max profit
- Don't wait for 100% (last 20% most risky)
- Free up capital for next trade
- Example: $3 credit → close at $1.50 debit (50%)

**For long volatility:**
- Take profits on IV spikes (100-200% gains)
- Don't wait for perfect scenario
- IV mean-reverts quickly
- Example: Paid $5, worth $10 → sell

**The compounding advantage:**

Short vol example:
- Strategy 1: Hold to expiration (30 days, $300 profit)
- Strategy 2: Close at 50% (15 days, $150), redeploy for another 15 days ($150)
- **Same profit, half the time, quarter the risk**

### The Dream Scenario

**Extreme best case:**

**For short volatility:**
- Enter at IVR 80 (IV very high)
- IV immediately crushes to IVR 20
- Capture 80% of max profit in first week
- **100%+ annualized return with minimal risk**

**For long volatility:**
- Enter at IVR 10 (IV very low)
- Unexpected catalyst hits
- IV spikes to IVR 90
- **300-500% return in days**

**For term structure:**
- Perfect term structure reversion
- Front month IV collapses relative to back month
- Calendar spread worth max value
- **200-300% return on capital**

**Probability:** Rare but illustrates potential when timing perfect

**Key insight:** Best case demonstrates the asymmetric payoff potential of IV strategies. However, realistic expectations should assume median outcomes. Position sizing must account for frequent small wins (short vol) or rare large wins (long vol).


## Summary

Diagonal spreads are a powerful “hybrid” strategy:

- **Directional exposure** from strike selection
- **Income** from selling short-term options
- **Time-structure advantage** from faster decay in the front month

They’re especially useful as a next step after:

- long calls/puts,
- covered calls/cash-secured puts,
- and vertical spreads.
