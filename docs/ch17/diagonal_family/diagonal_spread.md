# Diagonal Spreads


**Diagonal spreads** are option strategies where you **buy and sell options of the same type** (calls or puts) with **different strike prices AND different expiration dates**. They combine the ideas of **vertical spreads (different strikes)** and **calendar spreads (different expirations)** to create positions that can profit from **time decay, direction, and/or volatility changes** with **defined (or mostly-defined) risk**.





---

## The Core Insight


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/diagonal_spread_bullish.png?raw=true" alt="long_call_vs_put" width="700">
</p>

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

## What Is a Diagonal


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/diagonal_spread_greeks.png?raw=true" alt="long_call_vs_put" width="700">
</p>

### 1. The Structure


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/diagonal_spread_rolling.png?raw=true" alt="long_call_vs_put" width="700">
</p>

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


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/diagonal_spread_vs_calendar.png?raw=true" alt="long_call_vs_put" width="700">
</p>

### 1. Turn Time Decay

Long options pay theta.
But diagonals can be structured so the **short option’s theta** helps offset (or exceed) what you pay on the long option.

### 2. Flexible

By choosing strikes:

- **Bullish diagonal (calls)**: long call is ITM/ATM, short call is OTM
- **Bearish diagonal (puts)**: long put is ITM/ATM, short put is OTM

### 3. Capital

A major practical diagonal is the **Poor Man’s Covered Call (PMCC)**:

- A long-dated ITM call replaces owning 100 shares
- You sell short-dated calls against it for income

---

## Types of Diagonal


### 1. Call Diagonal


**Structure:**

- Buy a longer-dated call (often ITM)
- Sell a shorter-dated call (often OTM)

**Goal:** collect short-call premium while keeping bullish upside.

### 2. Put Diagonal


**Structure:**

- Buy a longer-dated put (often ITM)
- Sell a shorter-dated put (often OTM)

**Goal:** collect short-put premium while keeping bearish exposure.

### 3. Neutral / Range

Strikes chosen closer to spot, aiming to profit primarily from **time decay** and **mean reversion**, but this is more sensitive and requires tighter management.

---

## The Portfolio


### 1. Call Diagonal


\[
\Pi = C(S, K_{\text{long}}, T_{\text{long}}) - C(S, K_{\text{short}}, T_{\text{short}})
\]

where \(T_{\text{long}} > T_{\text{short}}\).

### 2. Put Diagonal


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

## Economic


**Understanding what this strategy REALLY represents economically:**

### 1. The Core Economic


This IV strategy involves specific economic trade-offs around volatility exposure. The key is understanding what you're giving up versus what you're gaining in terms of implied volatility positioning.

**Economic equivalence:**

$$
\text{Strategy P\&L} = \text{IV Change Component} + \text{Term Structure Component} + \text{Skew Component}
$$

### 2. Why This IV


Markets create these IV structures because different participants have different:
- Volatility expectations (near-term vs. long-term)
- Risk preferences (convexity vs. theta)
- Event views (known catalysts vs. unknown volatility)
- Hedging needs (portfolio protection vs. income generation)

### 3. The Volatility


Most IV strategies exploit the **volatility risk premium** - the empirical observation that:

$$
\text{Implied Volatility} > \text{Realized Volatility} \quad \text{(on average)}
$$

**Why this exists:**
1. **Insurance value:** Investors pay premium for protection
2. **Crash insurance:** Fear of tail events inflates IV
3. **Supply/demand:** More vol buyers than sellers
4. **Behavioral biases:** Overestimation of future volatility

### 4. Professional


Institutional traders view IV strategies as tools for:
1. **Volatility arbitrage:** Extracting the vol risk premium
2. **Term structure trading:** Exploiting mispricings across time
3. **Skew trading:** Capturing mispricing across strikes
4. **Surface arbitrage:** Finding no-arbitrage violations

Understanding the economic foundations helps you recognize when IV offers genuine edge versus when market pricing is fair.


## Concrete Example 1


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

## Concrete Example 2


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

## Strike Selection


### 1. Long Leg (Back


**Common approach:**

- Choose **ITM** (especially for PMCC)
  - Higher delta (more stock-like)
  - Less theta decay per day (relative)
  - More intrinsic value, less “wasting” time value

**Rule of thumb (practitioner-style):**

- Long call delta ~ **0.70–0.85** for PMCC-style diagonals
- Long put delta ~ **-0.70 to -0.85** for bearish diagonals

### 2. Short Leg (Front


**Common approach:**

- Choose **OTM** at a strike where you’re “willing” to cap near-term move
- You want meaningful premium but not too close to the money

**Rule of thumb:**

- Short call delta ~ **0.20–0.35**
- Short put delta ~ **-0.20 to -0.35**

---

## Time Frame Selection


### 1. Typical


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


### 1. Close or Roll the


If the short option is:

- **Profitable early** (e.g., you’ve captured 50–80% of its premium), consider buying it back and reselling a new one.
- **Threatened** (stock approaching short strike), you can:
  - **Roll up and out** (calls) / **roll down and out** (puts)
  - Convert the position into a different structure (e.g., vertical)
  - Close the entire diagonal

### 2. Avoid Holding the


Near expiration:

- gamma risk increases
- pin risk increases
- assignment becomes more likely

Many traders close/roll with **~7–14 days** left, especially if the short is near the money.

### 3. Assignment


If a short call gets assigned, you may end up short shares.
If a short put gets assigned, you may end up long shares.

**Practical approach:**

- manage by rolling before assignment becomes likely
- avoid short options that are deep ITM near expiry unless you intend assignment

---

## Pros and Cons


### 1. Diagonals —

**1. Flexible design**

- Can be bullish, bearish, or neutral-ish

**2. Can generate income**

- Short leg premium can offset long leg cost

**3. Better capital efficiency**

- Especially PMCC: stock-like exposure with less capital than buying shares

**4. Often improved “cost basis” over time**

- Repeated short premium can reduce effective cost of the long option

### 2. Diagonals —

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


**Detailed scenarios showing diagonal spreads in practice:**

### 1. Pension Duration


**Setup:**

**Trader profile:**
- Account: $25,000
- Goal: Generate income like covered calls without tying up $17,500 in stock
- Stock: XYZ trading at $175
- Bullish bias, wants upside participation + income

**Traditional covered call requires:**
- Buy 100 shares at $175 = $17,500
- Sell monthly calls against it = collect premium
- Problem: $17,500 capital tied up (70% of account!)

**PMCC alternative:**

```
Strategy: Diagonal call spread (PMCC)

Long leg (back month):
- Buy 1× XYZ $160 call, 180 DTE
- Deep ITM (delta ~0.80)
- Cost: $19.50 per contract = $1,950
- Acts as stock substitute

Short leg (front month):
- Sell 1× XYZ $185 call, 30 DTE
- OTM (delta ~0.25)
- Credit: $2.50 = $250

Net cost: $1,950 - $250 = $1,700
Capital saved: $17,500 - $1,700 = $15,800 (9.3× more efficient!)
```

**Initial Greeks:**
```
Long $160 call (180 DTE):
- Delta: +0.80
- Theta: -$0.02/day = -$2/day
- Vega: +0.15

Short $185 call (30 DTE):
- Delta: -0.25
- Theta: +$0.08/day = +$8/day
- Vega: -0.05

Combined position:
- Net delta: +0.55 (bullish exposure)
- Net theta: +$6/day (collecting decay!)
- Net vega: +0.10 (slightly long vol)
```

**Month 1: Perfect execution**

**Week 1-2: Stock consolidates $173-$178**
```
Action: None, let theta work
Short call: $2.50 → $1.75 (30% decay)
Long call: $19.50 → $19.80 (stock up slightly)
Net position: $1,700 → $1,550 (profit $150)
```

**Week 3: Stock rallies to $182**
```
Short call getting tested:
- Now worth $1.00 (down 60%)
- Delta: 0.25 → 0.40
Long call benefiting:
- Now worth $22.50 (up $3.00)
- Delta: 0.80 → 0.85

Net position:
- Entry: -$1,700
- Current: -$1,050 (short call $1.00, long call $22.50)
- Profit: $650
```

**Week 4 (expiration week): Stock at $183**
```
Decision: Let short call expire worthless, roll new one

Short $185 call expires:
- Worth $0 (OTM by $2)
- Collected full $250 credit!

Immediately roll:
- Sell new $190 call, 30 DTE for $2.00
- Collect another $200

Position update:
- Long call: Still holding $160 call (150 DTE remaining)
- Short call: Now $190 strike (new 30 DTE cycle)
- Month 1 income: $250
- Long call appreciation: $3.00 per share = $300
- Total month gain: $550
```

**Month 2-6: Continuation (rinse and repeat)**

```
Month 2: Stock $178-$185 range
- Collect $240 on new short call
- Long call stable
- Profit: $240

Month 3: Stock pulls back to $172
- Short call expires worthless: $225
- Long call down slightly: -$150
- Net: +$75

Month 4: Stock at $180
- Collect $260 on short call
- Long call up: +$200
- Profit: $460

Month 5: Stock at $182
- Collect $245
- Long call up: +$100
- Profit: $345

Month 6: Stock rallies to $188
- Short call tested, close early at $90 loss
- Roll to higher strike, collect $200 net
- Long call up: +$500
- Profit: $410
```

**Final outcome after 6 months:**

```
Total income from short calls:
Month 1: $250
Month 2: $240
Month 3: $225
Month 4: $260
Month 5: $245
Month 6: $110 ($200 - $90 adjustment)
Total: $1,330

Long call P&L:
Entry: $1,950 (180 DTE)
Current: $2,900 (30 DTE remaining)
Appreciation: +$950

Combined profit: $1,330 + $950 = $2,280
Initial investment: $1,700
ROI: 134% in 6 months
Annualized: ~268%

Compare to covered call:
- Would need $17,500
- Generated ~$1,500 income
- Stock appreciation: $1,300
- Total: $2,800
- ROI: 16% in 6 months
- Annualized: ~32%

PMCC advantage:
- 8× higher ROI (134% vs 16%)
- 10× less capital ($1,700 vs $17,500)
- Similar income ($1,330 vs $1,500)
- Similar risk profile
```

**What made it work:**

1. **Deep ITM long call:**
   - Delta 0.80 acts like owning 80 shares
   - Lower theta decay on back month
   - Good stock substitute

2. **OTM short calls:**
   - High probability of expiring worthless
   - Collected premium month after month
   - Rolled when threatened

3. **Time decay advantage:**
   - Short call theta > long call theta
   - Net positive $6/day
   - Compounded over 6 months

4. **Disciplined rolling:**
   - Closed short calls at 21 DTE
   - Immediately rolled to next month
   - Never held through expiration risk

5. **Stock cooperation:**
   - Mostly stayed in favorable range
   - Rallies captured by long call
   - Pullbacks didn't break structure

**Lessons:**
- PMCC provides leverage without margin
- Monthly income machine when managed
- Requires active management (monthly rolls)
- Capital efficiency enables diversification
- Works best in sideways to moderately bullish markets

### 2. Transition Risk


**Setup:**

**Trader thesis:**
- Account: $50,000
- Bearish on tech sector
- Stock: High-flying tech at $250
- Thinks consolidation/pullback coming
- Want to profit from time + direction

**The position:**

```
Diagonal put spread (bearish)

Long leg (back month):
- Buy 2× $250 puts, 90 DTE
- ATM (delta -0.50)
- Cost: $15.00 each × 2 = $3,000

Short leg (front month):
- Sell 2× $240 puts, 30 DTE
- OTM (delta -0.30)
- Credit: $4.50 each × 2 = $900

Net cost: $3,000 - $900 = $2,100
Max risk: $2,100 (if both expire worthless)

Greeks:
- Net delta: -0.40 (bearish)
- Net theta: +$15/day (collecting decay)
- Net vega: +0.30 (long volatility)
```

**Week 1-2: Thesis NOT working (stock rallies)**

```
Stock moves: $250 → $260 (+4%)

Impact:
- Long $250 puts: $15.00 → $10.00 (down $5)
- Short $240 puts: $4.50 → $2.00 (down $2.50)

Position P&L:
- Long puts loss: -$500 × 2 = -$1,000
- Short puts gain: +$250 × 2 = +$500
- Net: -$500 (24% of capital at risk)

Decision point:
- Thesis invalidated? Or temporary?
- Stock broke above resistance
- Should cut loss or hold?

Mistake: Held hoping for reversal
```

**Week 3: Continued rally ($260 → $265)**

```
Position deteriorating:
- Long $250 puts: $10.00 → $7.50
- Short $240 puts: $2.00 → $1.00

Additional loss:
- Long: -$250 × 2 = -$500
- Short: +$100 × 2 = +$200
- Net additional: -$300

Cumulative loss: -$800 (38% of capital)

Emotional state: Frustrated, hoping for reversal
Critical error: Not cutting loss at -25%
```

**Week 4 (expiration): Short puts expire worthless**

```
Stock at $265 (still up)

Short $240 puts:
- Expire OTM (worthless)
- Kept full $900 credit ✓

Long $250 puts:
- Now worth $5.50 (60 DTE)
- Down from $15 entry

Decision: Roll short puts to next month
- Sell $235 puts, 30 DTE for $3.00
- Collect $300 more

Position now:
- Long 2× $250 puts (60 DTE) at effective cost $10.50
  (paid $15, collected $4.50 first month, $1.50 second month)
- Short 2× $235 puts (30 DTE)
- Down $500 cumulative
- Still need stock to drop
```

**Month 2: Finally, the reversal**

```
Catalyst: Tech sector selloff on Fed comments

Week 1-2: Stock drops $265 → $245 (-7.5%)

Position response:
- Long $250 puts: $5.50 → $12.00 (+$6.50)
- Short $235 puts: $3.00 → $8.00 (-$5.00)

Net change:
- Long gain: +$650 × 2 = +$1,300
- Short loss: -$500 × 2 = -$1,000
- Net: +$300

This offsets previous -$500, now down only -$200
```

**Week 3-4: Continued weakness ($245 → $238)**

```
Position accelerating:
- Long $250 puts: $12.00 → $16.50
- Short $235 puts: $8.00 → $5.00 (at risk!)

Decision: Close short puts early (getting deep ITM)
- Buy back $235 puts at $5.00
- Loss on short leg: -$200 × 2 = -$400
- But protect against assignment

Long puts continue:
- Worth $16.50
- Up from $15 entry
- Profit on long: +$150 × 2 = +$300

Month 2 net: Roughly breakeven after adjustment costs
```

**Month 3: Exit strategy**

```
Stock stabilizes $235-$240

Long puts (30 DTE now):
- Worth $14.00
- Theta accelerating (burning faster now)

Decision: Take profits
- Sell long $250 puts at $14.00
- Loss: -$100 × 2 = -$200 (from $15 entry)

Total P&L across entire trade:
Month 1: -$500 (wrong direction)
Month 2: +$200 (reversal)
Month 3: -$200 (exit)
Credits collected: +$900 + $300 = +$1,200
Net profit: $700

ROI: $700 / $2,100 = 33% in 3 months
But: High stress, nearly failed
```

**What went wrong (then right):**

**Mistakes made:**
1. **Wrong initial timing:**
   - Entered too early
   - Stock had more upside
   - Should have waited for reversal confirmation

2. **No stop loss:**
   - Let position go -38%
   - Should have cut at -25%
   - Hope kept position alive

3. **Over-confidence in thesis:**
   - "Tech must pull back"
   - Market can stay irrational
   - Confirmation bias

**What saved the trade:**
1. **Time decay helped:**
   - Collected $1,200 in credits
   - Offset some losses
   - Theta was friend, not enemy

2. **Thesis eventually right:**
   - Stock did pull back (finally!)
   - Long puts gained value
   - Directional bet paid off

3. **Active management:**
   - Closed short puts when threatened
   - Didn't get assigned
   - Took profits on long puts

**Lessons:**
- Don't fight the trend (even if you "know" better)
- Use stop losses on diagonals (not unlimited time)
- Theta helps but doesn't replace good timing
- Being right eventually doesn't mean being right early
- Consider directional trades vs. income trades differently

### 3. Portable Alpha


**Setup:**

**Trader strategy:**
- Neutral strategy: Start with ATM calendar
- Plan: Adjust to diagonal if stock moves
- Goal: Manage risk while staying in trade

**Initial position (calendar spread):**

```
Stock at $100

Calendar spread (neutral):
- Buy 1× $100 call, 60 DTE for $6.00
- Sell 1× $100 call, 30 DTE for $3.50
- Net cost: $2.50

Greeks:
- Delta: ~0 (neutral)
- Theta: +$5/day
- Vega: +0.15
- Max profit: ~$4.50 (if stock at $100 at front expiration)
```

**Week 1-2: Stock rallies to $105**

```
Calendar in trouble:
- Long $100 call: $6.00 → $9.50
- Short $100 call: $3.50 → $7.00

Position:
- Net: $2.50 → $0.00 (breakeven)
- Short call now ITM (delta -0.70)
- Risk: Assignment if continues higher

Traditional response: Close at breakeven, accept defeat

Advanced response: Convert to diagonal!
```

**Adjustment: Calendar → Diagonal**

```
Action:
Step 1: Close short $100 call
- Buy back at $7.00
- Cost: $700

Step 2: Sell higher strike
- Sell $110 call, 30 DTE for $2.00
- Credit: $200

Net adjustment cost: $700 - $200 = $500

New position (diagonal):
- Long $100 call, 45 DTE (now ITM)
- Short $110 call, 30 DTE (OTM)
- Total invested: $2.50 + $5.00 = $7.50
- Structure: Now directional (bullish diagonal)
```

**Week 3-4: Stock consolidates $104-$107**

```
Perfect range for new diagonal:

Short $110 call:
- Expires worthless (stock stayed below)
- Kept $200 credit

Long $100 call:
- Stock at $106, worth $10.00 (15 DTE)
- Up from $9.50 after adjustment

Month result:
- Long call gain: +$50
- Short call credit: +$200
- Total: +$250
```

**Roll #2: New diagonal cycle**

```
Position:
- Long $100 call now 15 DTE, worth $10.00
- Sell new $110 call, 30 DTE for $2.50

But: Long call theta accelerating (risky)

Better decision: Roll long call too
- Sell $100 call at $10.00
- Buy $105 call, 45 DTE at $7.00
- Net: Pocket $3.00

New structure:
- Long $105 call, 45 DTE
- Short $110 call, 30 DTE
- Locked in: $3.00 profit
- New cost basis: $4.50
```

**Month 2-3: Continued management**

```
Repeated pattern:
- Stock stays $104-$108 range
- Short calls expire worthless monthly
- Collect $200-$250/month
- Roll long call when theta risk too high

Final outcome after 3 months:
- Collected short call credits: $650
- Long call rolled profitably: 3 times
- Total profit: $850
- Initial investment: $250 (original calendar)
- ROI: 340% in 3 months
```

**What made it exceptional:**

1. **Flexible adjustment:**
   - Didn't panic when calendar failed
   - Converted to structure that fits new market
   - Adaptation saved the trade

2. **Rolling discipline:**
   - Rolled short calls monthly
   - Rolled long call when theta accelerated
   - Never held into dangerous zones

3. **Taking profits:**
   - Locked in gains on long call rolls
   - Didn't try for "maximum profit"
   - Banked money along the way

4. **Market cooperation:**
   - Stock found range after rally
   - Perfect for diagonal structure
   - Consistent theta collection

**Advanced lessons:**
- Structures can be adjusted (not static)
- Calendar → diagonal conversion valuable
- Active management creates opportunities
- Multiple rolls compound profits
- Flexibility > rigid adherence to original plan

### 4. Tactical Duration


**Setup:**

**Trader mistake:**
- Bullish on stock into earnings
- Thinks: "Diagonal will benefit from both move + IV"
- Doesn't understand IV crush risk

**The position:**

```
2 weeks before earnings:

Diagonal call spread:
- Buy 1× $150 call, 60 DTE (after earnings)
- Sell 1× $155 call, 14 DTE (expires day after earnings)
- Cost: $7.50 - $2.50 = $5.00

IV environment:
- Long call IV: 45% (moderate)
- Short call IV: 85% (elevated pre-earnings)
- Collected high premium on short call ✓

Expectation:
- Stock rallies on earnings
- Short call profits from time decay
- Long call profits from stock move
- "Can't lose!" mindset
```

**The disaster (earnings night):**

```
Earnings released: Beat on revenue, miss on guidance

Stock reaction:
- Initial after-hours: Up to $153
- Think: "Great! Profitable!"

Next morning:
- Open: Stock gaps to $148 (down)
- Market didn't like guidance
- IV crushes 85% → 30% (massive)

Position carnage:
- Long $150 call: Was $7.50
  - Stock down to $148
  - IV crushed 45% → 30%
  - Now worth: $2.50 (down $5.00!)

- Short $155 call: Was $2.50
  - Stock at $148, far OTM
  - IV crushed, almost worthless
  - Now worth: $0.30 (gain $2.20)

Net P&L:
- Long loss: -$500
- Short gain: +$220
- Net: -$280 (56% loss in one day!)
```

**Why it was SO bad:**

```
Multiple disasters combined:

1. Wrong direction:
   - Thought bullish, stock dropped
   - Directional bet failed

2. IV crush on long call:
   - Bought at 45% IV
   - Now at 30% IV
   - Vega loss: 0.15 × -15 = -$2.25
   - This ALONE killed the position

3. Wasted elevated short premium:
   - Collected at 85% IV thinking it was edge
   - But it was pricing in THIS EXACT RISK
   - Market was right, trader was wrong

4. No protective stops:
   - Held through binary event
   - All-or-nothing bet
   - Lost the "all" side
```

**What should have been done:**

```
Correct approach:

Option 1: Avoid entirely
- Don't trade diagonals through earnings
- Binary events = bad for complex structures
- Wait until after earnings

Option 2: Close before earnings
- If already in position
- Exit 2-3 days before
- Accept small loss/gain
- Avoid the risk

Option 3: Different structure
- If must play earnings:
- Use debit spreads (both legs short-dated)
- Or long calls only (one decision)
- Not diagonals (too complex for binary event)

What would have saved $280:
- Exit 3 days before earnings at -$50 loss
- Saved: $230
- Lesson cost: $50 vs $280
```

**Lessons from disaster:**
- Never hold complex structures through earnings
- IV crush destroys long options even if right on direction
- Elevated short call premium is pricing in risk (not "free money")
- Binary events require simple structures or avoidance
- Sometimes not trading is best trade

---

## Practical Guidance


**Step-by-step implementation framework:**

### 1. Before entering,


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

### 2. Enter this


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

### 3. Calculate maximum


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

### 4. Best practices: 1


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

### 5. Active management


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

### 6. When to adjust:


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

### 7. Track every


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

### 8. Common Execution


1. **Selling vol at low IV** - IVR < 30 usually poor for short vol
2. **Buying vol at high IV** - IVR > 70 often too expensive for long vol
3. **Ignoring term structure** - Don't sell front month if in backwardation
4. **Over-leveraging vega** - Too much vega exposure can blow up account
5. **Holding through earnings** - IV crush destroys long vol positions
6. **Not taking profits** - Greed kills short vol profits
7. **Fighting IV trends** - IV regimes can persist
8. **Ignoring skew** - Put skew can make bearish trades expensive

### 9. Professional


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


### 1. Buying a Long Leg

If the long option expires soon, theta decay can overwhelm the strategy.

**Fix:** use a longer-dated long leg (60–180 days or more).

### 2. Selling the Short

You collect more premium but increase assignment risk and cap upside too aggressively.

**Fix:** start with OTM short strikes and adjust gradually.

### 3. Holding the Short

Pin risk and gamma explode.

**Fix:** roll/close earlier (commonly 7–14 days remaining).

### 4. Ignoring Implied

If IV collapses, long leg can lose value.

**Fix:** avoid overpaying for the long leg; consider entering after volatility spikes when appropriate.

### 5. Over-sizing

PMCC is not identical to a covered call.
Your long call can lose value sharply.

**Fix:** size conservatively and treat it as an options position with real risk.

---

## When to Use


### 1. Best conditions


- You have a **directional bias** (mild/moderate)
- You want to **benefit from theta** (short leg decay)
- You’re comfortable managing rolls and avoiding assignment surprises

### 2. Avoid when


- Big binary event risk inside the short leg (earnings, FDA, etc.)
- You cannot monitor or manage assignment/rolls
- Liquidity is poor (wide bid-ask spreads)

---


---



## Diagonal spreads are


Diagonal spreads are a powerful “hybrid” strategy:

- **Directional exposure** from strike selection
- **Income** from selling short-term options
- **Time-structure advantage** from faster decay in the front month

They’re especially useful as a next step after:

- long calls/puts,
- covered calls/cash-secured puts,
- and vertical spreads.