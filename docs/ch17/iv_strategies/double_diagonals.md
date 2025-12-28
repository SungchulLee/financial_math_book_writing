# Double Diagonals

**Double diagonals** are option strategies where you **simultaneously run diagonal spreads on both the call side and put side**, combining **different strike prices AND different expiration dates** on both wings. They create positions that can profit from **directional movement within a range, time decay on both sides, and term structure advantages** with **defined (or mostly-defined) risk**.

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
