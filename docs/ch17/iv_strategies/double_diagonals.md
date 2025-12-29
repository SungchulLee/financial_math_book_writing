# Double Diagonals

**Double diagonals** are option strategies where you **simultaneously run diagonal spreads on both the call side and put side**, combining **different strike prices AND different expiration dates** on both wings. They create positions that can profit from **directional movement within a range, time decay on both sides, and term structure advantages** with **defined (or mostly-defined) risk**.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/double_diagonals_flexibility.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/double_diagonals_management.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/double_diagonals_structure.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/double_diagonals_vs_double_calendar.png?raw=true" alt="long_call_vs_put" width="700">
</p>

---

## The Core Insight

**The fundamental idea:**

- A single diagonal gives you directional exposure + income from one side
- But what if you want **directional flexibility** with income from **both sides**?
- **Solution:** Run TWO diagonal spreads at different strikes
- One call diagonal above current price (bullish tilt)
- One put diagonal below current price (bearish tilt)
- Creates a "directional tent" that can profit from modest moves in either direction

**The key equation (intuition):**

$$
\text{Double Diagonal} = \text{Call Diagonal at } K_{\text{upper}} + \text{Put Diagonal at } K_{\text{lower}}
$$

You're essentially betting:
> "Time decay will work for me on BOTH sides, the stock can move moderately in either direction, and I'll manage whichever side gets challenged while collecting theta continuously."

---

## What Is a Double Diagonal?

### The Structure

A double diagonal uses:

- **Same option types on each side**: call diagonal + put diagonal
- **Different strikes on BOTH sides**: upper and lower strikes different from spot
- **Different expirations**: front month and back month
- **Directional flexibility**: can profit from moves in either direction (within limits)

**Typical construction (most common):**

**Call side (upper):**

- **BUY** a longer-dated OTM/ATM call (back month)
- **SELL** a shorter-dated further OTM call (front month)

**Put side (lower):**

- **BUY** a longer-dated OTM/ATM put (back month)
- **SELL** a shorter-dated further OTM put (front month)

This creates a **"diagonal tent"** with directional bias possibilities.

---

## Why Double Diagonals Exist

### 1. Directional Flexibility + Income
Unlike single diagonals (one direction only), double diagonals allow:
- **Moderate bullish moves** to profit (call side wins)
- **Moderate bearish moves** to profit (put side wins)
- **Sideways movement** to profit (both sides collect theta)
- You don't need to be perfectly right on direction

### 2. Enhanced Theta Collection
- Two short options decaying (call and put)
- Both collect premium
- Works even if stock drifts in either direction
- **Double the income potential** vs. single diagonal

### 3. Term Structure Advantage on Both Sides
- Front month decays faster on **both** call and put
- Back month more stable on **both** sides
- You exploit time structure **twice**

### 4. Better Than Double Calendar (Key Difference)
- **Double calendar:** Strikes at the same level, pure range bet
- **Double diagonal:** **Strikes spread wider**, allows directional profit
- More flexible, more forgiving structure

---

## Types of Double Diagonals

### 1) Symmetrical Double Diagonal (Neutral)

**Structure:**

- Call diagonal: ATM or slightly OTM
- Put diagonal: ATM or slightly OTM
- Equal spacing from current price
- Neutral directional assumption

**Example:**

- Stock at $100
- Buy 90-day $105 call, Sell 30-day $110 call
- Buy 90-day $95 put, Sell 30-day $90 put

**Goal:** profit from range-bound movement with theta collection.

### 2) Bullish Double Diagonal

**Structure:**

- Call diagonal: Closer to the money, larger size
- Put diagonal: Further from money, smaller size
- Biased toward upside profit

**Example:**

- Stock at $100
- Buy 90-day $102 call, Sell 30-day $108 call (2 contracts)
- Buy 90-day $95 put, Sell 30-day $88 put (1 contract)

**Goal:** profit from moderate upward move while maintaining downside protection.

### 3) Bearish Double Diagonal

**Structure:**

- Call diagonal: Further from money, smaller size
- Put diagonal: Closer to money, larger size
- Biased toward downside profit

**Example:**

- Stock at $100
- Buy 90-day $105 call, Sell 30-day $112 call (1 contract)
- Buy 90-day $98 put, Sell 30-day $92 put (2 contracts)

**Goal:** profit from moderate downward move while maintaining upside protection.

### 4) Aggressive Double Diagonal (Wide Tent)

**Structure:**

- Very wide strike spacing
- Short strikes far OTM on both sides
- Maximum directional flexibility
- Lower theta but higher profit potential from moves

**Example:**

- Stock at $100
- Buy 90-day $100 call, Sell 30-day $115 call
- Buy 90-day $100 put, Sell 30-day $85 put

**Goal:** allow large moves while collecting some theta.

---

## The Portfolio

### Call Diagonal (upper wing)

$$
\Pi_{\text{call}} = C(S, K_{\text{long,call}}, T_{\text{long}}) - C(S, K_{\text{short,call}}, T_{\text{short}})
$$

### Put Diagonal (lower wing)

$$
\Pi_{\text{put}} = P(S, K_{\text{long,put}}, T_{\text{long}}) - P(S, K_{\text{short,put}}, T_{\text{short}})
$$

### Combined Position

$$
\Pi_{\text{total}} = \Pi_{\text{call}} + \Pi_{\text{put}}
$$

where:
- $T_{\text{long}} > T_{\text{short}}$ (typically 90 days vs. 30-45 days)
- $K_{\text{short,call}} > K_{\text{long,call}} \geq S$ (call side above stock)
- $K_{\text{short,put}} < K_{\text{long,put}} \leq S$ (put side below stock)

**Greeks (typical):**

- **Delta:** Can be neutral, bullish, or bearish depending on construction
- **Theta:** **Positive** (from both short legs)
- **Vega:** **Positive-ish** (net long from back month options)
- **Gamma:** Mixed (depends on proximity to strikes)

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


## Concrete Example 1: Symmetrical Double Diagonal (Neutral)

**Setup:**

- Stock at $S = 100$
- Moderate volatility environment
- You expect the stock to move but stay within reasonable range
- Want to collect theta while allowing some movement

**Trade:**

**Call diagonal (upper):**

- Buy 90-day **$105 call** (slightly OTM) for **$4.50**
- Sell 30-day **$110 call** (further OTM) for **$1.50**
- Net debit: $3.00 per spread

**Put diagonal (lower):**

- Buy 90-day **$95 put** (slightly OTM) for **$4.20**
- Sell 30-day **$90 put** (further OTM) for **$1.40**
- Net debit: $2.80 per spread

**Total net debit:** $3.00 + $2.80 = **$5.80** (= $580 per double diagonal)

**Greeks at entry:**

- Delta: ≈ 0 (approximately neutral)
- Theta: +$25/day (from both short options)
- Vega: +0.6 per spread (net long vol)
- Max risk: Net debit = $580

**Intuition:**

- If stock moves to $105: call side profits, put side collects theta
- If stock moves to $95: put side profits, call side collects theta
- If stock stays at $100: both sides collect theta
- Beyond $110 or below $90: one side challenged, manage accordingly

**Key outcomes at the short expiration (30 days):**

**Scenario 1: Stock at $100 (optimal sideways)**
- Short $110 call: expires worthless → keep $1.50
- Short $90 put: expires worthless → keep $1.40
- Long 90-day options retain most value
- **Profit: ≈$150-$200** (theta collection)
- Can roll: sell new 30-day options against long positions

**Scenario 2: Stock at $105 (moderate bull move)**
- Short $110 call: expires worthless → keep $1.50
- Short $90 put: expires worthless → keep $1.40
- Long $105 call: now ATM with 60 days left, increased value
- Long $95 put: decreased value but not worthless
- **Profit: ≈$200-$300** (combination of theta + call appreciation)

**Scenario 3: Stock at $95 (moderate bear move)**
- Short $110 call: expires worthless → keep $1.50
- Short $90 put: expires worthless → keep $1.40
- Long $95 put: now ATM with 60 days left, increased value
- Long $105 call: decreased value but not worthless
- **Profit: ≈$200-$300** (combination of theta + put appreciation)

**Scenario 4: Stock at $112 (beyond call wing)**
- Short $110 call: $2 ITM, needs management
- Short $90 put: worthless
- Long $105 call: $7 ITM (profits more)
- Net call diagonal still profitable but compressed
- **Action: Close or roll up the short call**

**Scenario 5: Stock at $88 (beyond put wing)**
- Short $110 call: worthless
- Short $90 put: $2 ITM, needs management
- Long $95 put: $7 ITM (profits more)
- Net put diagonal still profitable but compressed
- **Action: Close or roll down the short put**

---

## Concrete Example 2: Bullish Double Diagonal

**Setup:**

- Stock at $S = 100$
- You're **moderately bullish** but want downside protection
- Want to collect theta while benefiting from upward drift

**Trade:**

**Call diagonal (upper - emphasized):**

- Buy 90-day **$102 call** (close to money) for **$5.80**
- Sell 30-day **$108 call** (OTM) for **$1.80**
- Net debit: $4.00 per spread
- **2 contracts** = $800 debit

**Put diagonal (lower - protection):**

- Buy 90-day **$95 put** (OTM) for **$4.00**
- Sell 30-day **$88 put** (far OTM) for **$0.80**
- Net debit: $3.20 per spread
- **1 contract** = $320 debit

**Total net debit:** $800 + $320 = **$1,120**

**Position delta:** Approximately **+20 to +30** (bullish bias)

**Rationale:**

- More capital in call diagonal (expecting upward move)
- Put diagonal provides insurance + some theta
- If stock rises to $105-$108: large profit from call side
- If stock drops to $95: put diagonal limits loss and can profit

---

## Strike Selection Strategy

### Long Legs (Back Month)

**Call diagonal - long call:**

**Neutral to bullish approach:**

- **ATM to slightly OTM** ($100-$105 on $100 stock)
- Delta: 0.45-0.60
- Provides directional exposure
- Not too expensive

**Aggressive bullish:**

- **Slightly ITM** ($95-$100 on $100 stock)
- Delta: 0.60-0.75
- More expensive but more stock-like
- PMCC-style structure

**Put diagonal - long put:**

**Neutral to bearish approach:**

- **ATM to slightly OTM** ($95-$100 on $100 stock)
- Delta: -0.45 to -0.60
- Provides directional exposure
- Mirror of call side for symmetry

**Conservative approach:**

- **Further OTM** ($90-$95 on $100 stock)
- Delta: -0.30 to -0.45
- Cheaper, more protection-focused
- Less aggressive put side

### Short Legs (Front Month)

**Call diagonal - short call:**

**Standard approach:**

- **OTM** with delta 0.20-0.35
- Example: $108-$112 on $100 stock
- Meaningful premium but room to move

**Aggressive income:**

- **Closer to money** with delta 0.35-0.45
- Example: $105-$108 on $100 stock
- More premium but tighter range

**Put diagonal - short put:**

**Standard approach:**

- **OTM** with delta -0.20 to -0.35
- Example: $88-$92 on $100 stock
- Mirror of call side

**Aggressive income:**

- **Closer to money** with delta -0.35 to -0.45
- Example: $92-$95 on $100 stock
- More premium but tighter range

### Strike Width Strategy

**Narrow tent (5-8% total width):**

- Call: Buy $102, Sell $107
- Put: Buy $98, Sell $93
- Higher theta per dollar
- Requires more active management
- Less forgiving

**Medium tent (10-15% total width):**

- Call: Buy $105, Sell $112
- Put: Buy $95, Sell $88
- **Most common structure**
- Balanced theta/flexibility
- Good probability of profit

**Wide tent (18-25% total width):**

- Call: Buy $105, Sell $115
- Put: Buy $95, Sell $85
- Maximum directional room
- Lower theta collection
- Very forgiving, lower return

---

## Time Frame Selection

### Typical Expirations

**Long legs (back month):**

- **60-90 days:** Standard
- **90-120 days:** More conservative
- **120-180 days (or LEAPS):** Very stable, PMCC-style

**Short legs (front month):**

- **20-30 days:** Maximum theta
- **30-45 days:** Most common, balanced
- **45-60 days:** More conservative, lower theta

**Why these work:**

- **Time decay differential:** Front decays ~3x faster than back
- **Theta collection:** Short legs provide income
- **Adjustment time:** Long legs give you room to manage
- **Roll opportunities:** Can continuously sell new front months

### Common Time Ratios

| Long Leg | Short Leg | Ratio | Character | Use Case |
|----------|-----------|-------|-----------|----------|
| 60 days | 30 days | 2:1 | Aggressive | Active traders |
| 90 days | 30 days | 3:1 | **Standard** | Most common |
| 90 days | 45 days | 2:1 | Balanced | Less active |
| 120 days | 30 days | 4:1 | Conservative | Income focus |
| 180 days (LEAPS) | 30 days | 6:1 | Very stable | PMCC-style |

**Rule of thumb:**

- Minimum ratio: **2:1** (back:front)
- Sweet spot: **3:1** (90 days vs. 30 days)
- For PMCC-style: **4:1 or higher**

---

## Position Management

### 1) Entry Timing

**Best conditions to enter:**

**Market environment:**

- Moderate volatility (IVR 30-70%)
- Upward sloping term structure
- No major events in next 45 days
- Stock in defined range or trend

**Stock selection:**

- Liquid options (narrow bid-ask)
- Clear technical levels
- Moderate volatility (not extreme)
- No earnings in front month

**Avoid entering when:**

- Earnings announcement inside front month
- Extreme IV (very high or very low)
- Inverted term structure
- Just before known binary events

### 2) During the Life of the Trade

**Weekly monitoring:**

**Check position:**

- Where is stock vs. your strikes?
- How is theta accumulation?
- Any Greek shifts?
- Term structure still favorable?

**Watch for:**

- Stock approaching a short strike
- Significant IV changes
- Term structure flattening
- Time to adjust or roll

**Daily monitoring (last 2 weeks):**

- Gamma risk increasing
- Assignment risk if short legs ITM
- Decision point approaching

### 3) Adjustment Strategies

**When stock approaches upper short call:**

**Option A: Roll up and out**
- Buy back the $110 short call
- Sell new $115 call (next month)
- Collect additional premium
- Widen your tent upward

**Option B: Roll the entire call diagonal**
- Close both call legs
- Open new call diagonal higher
- Reposition structure
- More aggressive reset

**Option C: Close the challenged side**
- Take profit/loss on call diagonal
- Keep put diagonal running
- Reduces complexity
- Locks in one side

**When stock approaches lower short put:**

**Option A: Roll down and out**
- Buy back the $90 short put
- Sell new $85 put (next month)
- Widen tent downward

**Option B: Add to put side**
- Sell additional short puts
- Collect more premium
- Increases risk but lowers basis

**Option C: Close and reposition**
- Exit put diagonal
- Reassess structure
- Consider new strikes

### 4) Management at Front Month Expiration

**Decision tree (7-14 days before expiration):**

**If both short options OTM and stock near center:**

- **Let them expire worthless**
- Collect full premium
- Immediately sell new front month on both sides
- **This is the ideal scenario**

**If one side threatened:**

- **Roll the threatened side** only
- Keep the profitable side
- Adjust strikes as needed

**If position profitable overall:**

- **Close entire position** if target hit (25-50% profit)
- **Roll both sides** if continuing strategy
- Don't get greedy

**If position at loss:**

- **Evaluate each diagonal separately**
- Close losing side if beyond repair
- Keep winning side if it can recover losses

### 5) Rolling Mechanics

**Standard monthly roll (perpetual strategy):**

**Week before front expiration:**

**Step 1: Assess position**
- Calculate P&L on short legs
- Check long legs' remaining value
- Decide if continuing

**Step 2: Close or let expire**
- If OTM: let expire, keep premium
- If close: buy back to avoid assignment
- Net: collected theta from shorts

**Step 3: Sell new front month**
- Pick new short strikes (same or adjusted)
- Sell 30-45 day options
- Collect new premium
- **Now you have: original long legs + new short legs**

**Step 4 (optional): Adjust long legs**
- If long legs have < 30 days left, consider closing
- Or keep if you want to maintain structure
- Or roll long legs out to new back month

**Example monthly roll:**

**Original position (Day 0):**

- Long 90-day $105 call, Short 30-day $110 call
- Long 90-day $95 put, Short 30-day $90 put

**At 30 days (front expiration):**

- Short $110 call expires worthless: +$150
- Short $90 put expires worthless: +$140
- **Total collected: $290**

**New position (Day 30):**

- Same: Long 60-day $105 call (was 90-day, now 60-day left)
- **New:** Sell 30-day $110 call for $120
- Same: Long 60-day $95 put (was 90-day, now 60-day left)
- **New:** Sell 30-day $90 put for $110
- **Collected: $230 new premium**

**Position now:**

- Cost basis reduced by $290 from first month
- Collecting another $230 this month
- Total income: $520
- Can continue rolling monthly

---

## Pros and Cons

### Double Diagonals — Advantages ✓

**1. Directional flexibility**
- Can profit from moves in **either direction**
- Not locked into single directional bet
- More forgiving than single diagonal

**2. Enhanced theta collection**
- **Two short options** decaying
- Income from both call and put sides
- Can offset long option decay

**3. Term structure advantage on both sides**
- Exploit time differential twice
- Front month decays faster on both wings
- Back month stability on both wings

**4. Can convert to profitable side**
- If one side wins, can close losing side
- Flexibility to adjust as stock moves
- Dynamic risk management

**5. Lower cost than buying two diagonals separately**
- Negative correlation between call and put values
- Natural hedging reduces net cost
- Capital efficient structure

**6. Defined-ish risk**
- Maximum loss is net debit (mostly)
- Assignment creates temporary risk but manageable
- Better than naked options

### Double Diagonals — Disadvantages ✗

**1. Complex to manage**
- **Four option legs** to track
- Multiple Greeks to monitor
- Two expiration dates
- Requires experience

**2. Assignment risk on both sides**
- Short call assignment: short stock
- Short put assignment: long stock
- Need to manage carefully near expiration
- Can create unexpected positions

**3. Two-sided adjustments**
- Either side can need rolling
- Might need to adjust both sides
- More management than simpler strategies
- Time intensive

**4. Term structure dependency**
- If term structure flattens, hurts position
- Need favorable time structure to profit
- Not just about stock movement
- Additional risk factor

**5. Whipsaw risk**
- Stock moving back and forth
- Challenges both sides alternately
- Difficult to manage oscillations
- Can erode profits

**6. Not truly "set and forget"**
- Requires active monitoring
- Monthly rolls for perpetual strategy
- Adjustment decisions regularly
- Not passive income

**7. Capital efficiency illusion**
- Looks cheap but ties up buying power
- Assignment risk requires margin
- Can't deploy capital elsewhere
- Opportunity cost

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

### 1) Entering with Unbalanced Strikes

**The error:**

- Call diagonal: Buy $102, Sell $108
- Put diagonal: Buy $93, Sell $88
- Strikes not symmetrically positioned
- Creates unintended directional bias

**Fix:** 

- Keep strikes roughly equidistant from spot
- Or intentionally bias with understanding
- Don't create accidental asymmetry

### 2) Wrong Long Leg Time Frame

**The error:**

- Buying only 45-day long legs
- They decay too fast
- Not enough time to roll short legs
- Position collapses before theta collected

**Fix:**

- Use at least 60-90 days for long legs
- 90+ days is better for stability
- LEAPS (180+ days) for true PMCC-style

### 3) Holding Short Legs Too Close to Expiration

**The error:**

- "Just 3 more days of theta!"
- Gamma and pin risk explode
- Assignment becomes likely
- Last-minute management chaos

**Fix:**

- **Roll or close at 7-14 days** remaining
- Don't chase last few dollars of theta
- Avoid expiration week gamma

### 4) Ignoring One Side

**The error:**

- Focus only on threatened side
- Neglect the profitable side
- Miss opportunity to take profit on one side
- Over-manage one, under-manage other

**Fix:**

- Evaluate **each diagonal independently**
- Close profitable side early if appropriate
- Don't tie both sides together artificially

### 5) Over-Adjusting

**The error:**

- Stock moves $2, immediately adjust
- Constant rolling creates friction
- Death by a thousand adjustments
- Transaction costs pile up

**Fix:**

- Have clear adjustment rules
- Only adjust when short strike seriously threatened
- Accept some stock movement
- Don't over-manage

### 6) Wrong Position Size

**The error:**

- "It's defined risk, so 10 contracts!"
- Ties up too much capital
- Can't adjust properly
- Psychological pressure

**Fix:**

- Size so max loss = 1-2% of portfolio
- Start small (1-2 contracts)
- Scale up as you gain experience
- Keep powder dry for adjustments

### 7) Entering Before Events

**The error:**

- Earnings in 3 weeks
- "But my strikes are far OTM!"
- IV spike crushes structure
- Event volatility unpredictable

**Fix:**

- **Always check earnings calendar**
- Avoid front month events entirely
- Back month events OK if > 60 days
- No exceptions

### 8) Expecting Perfection

**The error:**

- Want stock to stay perfectly centered
- Frustrated by any movement
- Unrealistic expectations
- Give up after one adjustment

**Fix:**

- Accept that adjustments are **normal**
- Stock WILL move, that's OK
- Strategy works over many trades
- Focus on process, not single outcome

---

## When to Use Double Diagonals

### Best Conditions ✓

**Market environment:**

- **Moderate volatility** expected (not extreme low or high)
- Range-bound to **mild trending** market
- Upward sloping term structure
- No major market events pending

**Stock characteristics:**

- **Liquid options** (tight bid-ask spreads)
- Moderate beta (not ultra-volatile)
- Clear support/resistance levels
- Stable company fundamentals

**Volatility conditions:**

- IVR (IV Rank) **30-70%** (not extremes)
- Front month IV < Back month IV
- Stable or slightly increasing IV
- No extreme skew distortions

**Your situation:**

- Can **monitor position** regularly
- Comfortable with **rolling options**
- Have margin for potential assignment
- Understand directional flexibility
- Want theta income with directional room

**Your outlook:**

- **Mildly directional** or neutral
- Expect moderate stock movement
- Want to collect theta while allowing drift
- Willing to manage actively

### Avoid When ✗

**Dangerous conditions:**

**Binary events:**

- **Earnings inside front month** (avoid completely)
- FDA decisions
- Merger announcements
- Economic reports (if high beta stock)

**Market structure:**

- **Inverted term structure** (kills the strategy)
- Extreme high IV (pending collapse)
- Extreme low IV (no premium)
- Highly trending market (pick direction instead)

**Stock issues:**

- **Poor liquidity** (wide spreads, assignment nightmares)
- Highly volatile stock (breaks strikes constantly)
- Penny stocks (assignment risk too high)
- Biotech with binary catalysts

**Personal constraints:**

- Cannot monitor regularly
- Cannot handle assignment
- No margin account
- First time with options
- Don't understand diagonals yet

**Market conditions:**

- **Crisis/panic** (volatility explosions)
- **Strong trends** (just buy calls/puts instead)
- **Low volatility grind** (iron condor better)
- Extremely uncertain environment

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

Double diagonals are a sophisticated "hybrid of hybrids" strategy:

- **Directional flexibility** from having both call and put diagonals
- **Enhanced income** from selling short-term options on both sides
- **Time-structure advantage** exploited on both wings
- **Active management** required but offers control

**Key characteristics:**

- **Four option legs** (two diagonals)
- **Positive theta** from both short options
- **Net long vega** from back month options
- **Directional neutrality** possible (or bias if desired)
- **Defined-ish risk** with management requirements

**Best for:**

- Experienced option traders
- Those comfortable with rolling
- Active managers willing to monitor
- Traders wanting directional flexibility + income

**The progression:**

- Master **single calls/puts** first
- Then **covered calls / diagonals** (one side)
- Then **double calendars** (pure time, same strikes)
- Then **double diagonals** (time + directional flexibility)

They're especially useful as a next step after:
- Single diagonal spreads
- Double calendars
- Iron condors

**The ultimate insight:**
> "Double diagonals let you collect theta from both sides while maintaining directional flexibility. You don't need to be right about direction—just need the stock to stay within your expanded range while you continuously harvest time decay."
