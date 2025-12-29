# Earnings IV Crush Strategies

**Earnings IV Crush strategies** are options approaches designed to exploit the predictable phenomenon where implied volatility spikes before earnings announcements and then collapses immediately afterward, regardless of the actual stock move, creating systematic profit opportunities from volatility mean reversion rather than directional bets.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/earnings_iv_crush_strategies_comparison.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/earnings_iv_crush_strategies_iv_pattern.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/earnings_iv_crush_strategies_payoff.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/earnings_iv_crush_strategies_scenarios.png?raw=true" alt="long_call_vs_put" width="700">
</p>

---

## The Core Insight

**The fundamental idea:**

- Earnings announcements are **binary events** with significant uncertainty
- Implied volatility **spikes** in the days/weeks before earnings
- After earnings are released, uncertainty resolves
- IV **collapses rapidly** (the "crush") regardless of which direction the stock moves
- **Solution:** Trade the IV crush, not the direction
- Sell premium before earnings, buy back after for profit
- Or avoid being crushed if long premium

**The key equation:**

$$
\text{IV Crush} = \text{IV}_{\text{pre-earnings}} - \text{IV}_{\text{post-earnings}}
$$

**Typical crush magnitude:**

$$
\text{IV Crush} \approx 30\% \text{ to } 70\% \text{ decline in IV level}
$$

**You're essentially betting: "The market is overpricing the earnings uncertainty, and I can profit from the inevitable volatility collapse after the announcement."**

---

## What Is Earnings IV Crush?

**Before understanding earnings strategies, we need to understand the earnings cycle:**

### The Earnings IV Cycle

**What is it?**

Implied volatility follows a **predictable pattern** around earnings announcements:

**Visual representation:**

```
    IV Level
     ↑
  50%|           ___/‾‾‾\___ 
  40%|        __/           \___
  30%|      _/                  \___
  20%|  ___/                        \___
  10%|_________________________________
     |
     -30  -20  -10   0   +10  +20  +30
     Days to Earnings    ↑    Days After
                      Earnings
```

**The four phases:**

**1. Base Period (30-45 days before):**

- IV at normal levels (20-30% typical)
- No earnings premium yet
- Regular trading

**2. Build-up Period (20-10 days before):**

- IV starts rising gradually
- Market pricing in uncertainty
- Premium accumulating

**3. Peak Period (5-1 days before):**

- IV at maximum (40-60%+ typical)
- Peak uncertainty
- **This is when to sell premium**

**4. Crush Period (Day after earnings):**

- IV collapses rapidly (50-70% drop in IV)
- Uncertainty resolved
- **This is the "crush"**

**5. Recovery Period (2-30 days after):**

- IV gradually normalizes
- Returns to base level
- Next cycle begins

### Why Does IV Crush Happen?

**The fundamental reason:**

**Before earnings:**

- Unknown information
- Stock could move ±10-20% (large uncertainty)
- Option buyers willing to pay premium
- **IV reflects this uncertainty**

**After earnings:**

- Information released
- Move has occurred (or not)
- Uncertainty resolved
- **Option buyers won't pay that premium anymore**

**Mathematical explanation:**

Before earnings, option prices reflect:

$$
C_{\text{pre}} = f(S, K, T, \sigma_{\text{high}}, \text{earnings uncertainty})
$$

After earnings:

$$
C_{\text{post}} = f(S', K, T', \sigma_{\text{low}}, \text{no earnings uncertainty})
$$

Even if $S' > S$ (stock moved favorably), the crush in $\sigma$ can dominate!

### The Cruel Reality of Long Options into Earnings

**Example scenario:**

**Before earnings:**

- Stock at $100
- Buy $100 call for $5 (IV = 60%)
- Expecting 8-10% move

**After earnings:**

- Stock moves to $108 (+8%, favorable!)
- IV crushes: 60% → 25%
- Call worth: $8.50 (not $13 as you'd expect)

**P&L:**

- Paid: $5.00
- Worth: $8.50
- **Profit: $3.50** (70% profit)

**But if just owned stock:**

- Bought at $100
- Now at $108
- **Profit: $8.00** (8% profit)

**The call "should" have made more, but IV crush limited gains!**

**Worse scenario:**

**If stock moved to $104 (+4%, still up):**

- IV crushes: 60% → 25%
- Call worth: $4.20
- **LOSS: -$0.80** despite stock going up!

**This is the IV crush trap!**

---

## The Structure

### Types of Earnings Strategies

**Based on your timing and position:**

**1. Pre-Earnings Strategies (Sell the IV Spike):**

```
Sell Premium Before → Hold Through → Buy Back After

Strategies:
├── Short Strangles (aggressive)
├── Iron Condors (defined risk)
├── Credit Spreads (directional + crush)
├── Naked Puts/Calls (very aggressive)
└── Covered Calls (income on holdings)
```

**2. Post-Earnings Strategies (Avoid the Crush):**

```
Buy Premium After → Cheaper Options → Normal Trading

Strategies:
├── Long Calls/Puts (directional)
├── Debit Spreads (defined risk)
└── Calendars (time structure)
```

**3. Hybrid Strategies (Play Both Sides):**

```
Combination Structures

Strategies:
├── Reverse Iron Condor (long before, short after)
├── Earnings Calendar (sell front, buy back)
└── Diagonal Earnings Plays
```

### The Decision Tree

**Visual framework:**

```
                Earnings Approaching
                        ↓
              ┌─────────┴─────────┐
              ↓                   ↓
         Before Earnings     After Earnings
         (High IV)          (Crushed IV)
              ↓                   ↓
         SELL Premium       BUY Premium
              ↓                   ↓
      Iron Condors         Long Options
      Short Strangles      Debit Spreads
      Credit Spreads       Calendars
              ↓                   ↓
      Hold Through         Normal Strategies
         Earnings          (IV normalized)
              ↓
         Close Next Day
      (Capture Crush)
```

### The IV Crush Math

**Quantifying the crush:**

**Historical average crush (across thousands of earnings):**

$$
\text{IV}_{\text{post}} \approx 0.3 \times \text{IV}_{\text{pre}} \text{ to } 0.5 \times \text{IV}_{\text{pre}}
$$

**Example:**

- Pre-earnings IV: 60%
- Post-earnings IV: 25%
- **Crush: 58% decline** in IV level

**This means:**

For a short option position:

$$
\text{Profit} \approx \text{Vega} \times (\text{IV}_{\text{pre}} - \text{IV}_{\text{post}})
$$

**Example:**

- Short strangle vega: -$80 per 1% IV
- IV drops 35 points (60% → 25%)
- **Profit: -80 × (-35) = $2,800** from IV crush alone!

---

## The Portfolio

### Pre-Earnings Short Premium Portfolio

**Example: Iron Condor**

$$
\Pi_{\text{IC}} = \underbrace{-P(K_1)}_{\text{Short Put}} + \underbrace{P(K_2)}_{\text{Long Put}} + \underbrace{-C(K_3)}_{\text{Short Call}} + \underbrace{C(K_4)}_{\text{Long Call}}
$$

Entered **before earnings** at high IV, closed **after earnings** at low IV.

**Greeks (before earnings):**

$$
\begin{align}
\Delta &\approx 0 \text{ (neutral)} \\
\text{Vega} &< 0 \text{ (SHORT vega - this is the edge)} \\
\Theta &> 0 \text{ (positive but secondary)} \\
\Gamma &< 0 \text{ (SHORT gamma - accept risk of move)}
\end{align}
$$

**The bet:**

- IV crush dominates price movement
- Even if stock moves against you, IV crush helps
- Close immediately after earnings

### Pre-Earnings Short Strangle Portfolio

$$
\Pi_{\text{Strangle}} = -C(K_{\text{call}}) - P(K_{\text{put}})
$$

**Greeks:**

$$
\begin{align}
\Delta &\approx 0 \\
\text{Vega} &< 0 \text{ (very short - main exposure)} \\
\Theta &> 0 \\
\Gamma &< 0 \text{ (naked risk)}
\end{align}
$$

**The bet:**

- Aggressive IV crush play
- Undefined risk but historically profitable
- Requires active management

### Post-Earnings Long Premium Portfolio

**Example: Debit Spread**

$$
\Pi_{\text{Debit}} = C(K_1) - C(K_2)
$$

Entered **after earnings** at crushed IV.

**Greeks (after earnings):**

$$
\begin{align}
\Delta &> 0 \text{ (directional)} \\
\text{Vega} &> 0 \text{ (long vega - cheap entry)} \\
\Theta &< 0 \text{ (negative but options cheap)} \\
\Gamma &> 0 \text{ (positive)}
\end{align}
$$

**The bet:**

- Options very cheap post-crush
- Directional play with cheap premium
- Normal theta decay applies

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


## The P&L Formula

### For Pre-Earnings Short Premium

$$
\delta \Pi_{\text{Pre}} \approx \underbrace{\text{Vega}_{\text{net}} \cdot \delta\sigma}_{\text{IV CRUSH (dominant)}} + \underbrace{\Delta_{\text{net}} \cdot \delta S}_{\text{Stock move}} + \underbrace{\frac{1}{2}\Gamma (\delta S)^2}_{\text{Gamma}}
$$

**Breaking it down:**

**1. IV Crush P&L (PRIMARY EDGE - 60-80% of total):**

$$
\text{P\&L}_{\text{IV}} = \text{Vega}_{\text{net}} \times (\text{IV}_{\text{post}} - \text{IV}_{\text{pre}})
$$

**For short vega positions:**

$$
\text{P\&L}_{\text{IV}} = (-\text{Vega}) \times (-\Delta \text{IV}) = \text{POSITIVE}
$$

**Example:**

- Short strangle vega: -$100 per 1% IV
- IV crushes: 60% → 25% = -35 points
- **P&L from IV: $3,500 profit**

**This is WHY the strategy works!**

**2. Directional P&L (SECONDARY - 20-40%):**

$$
\text{P\&L}_{\text{Direction}} = \Delta_{\text{net}} \times \Delta S
$$

**For delta-neutral positions:**

- Initial delta ≈ 0
- But stock move creates delta
- Usually small compared to IV effect

**Example:**

- Stock moves $8 (8%)
- Delta shifts to +20
- **P&L from direction: +$160**

**3. Gamma P&L (RISK FACTOR):**

$$
\text{P\&L}_{\text{Gamma}} = \frac{1}{2} \Gamma \times (\Delta S)^2
$$

**For short gamma:**

- Large moves hurt
- But IV crush often overwhelms this

**Example:**

- Short gamma: -30
- Stock moves $8
- **P&L from gamma: -$960 loss**

**TOTAL P&L:**

- IV crush: +$3,500
- Direction: +$160
- Gamma: -$960
- **Net: +$2,700 profit**

**IV crush dominated!**

### For Post-Earnings Long Premium

$$
\delta \Pi_{\text{Post}} \approx \underbrace{\Delta \cdot \delta S}_{\text{Directional (primary)}} + \underbrace{\text{Vega} \cdot \delta\sigma}_{\text{IV normalization}} + \underbrace{\Theta \, \delta t}_{\text{Theta decay}}
$$

**Different focus:**

- Not relying on IV crush
- Playing directional with cheap entry
- Normal option mechanics

---

## Types of Earnings IV Crush Strategies

### 1. Pre-Earnings Premium Selling (The Main Approach)

**Philosophy:**

- IV spike before earnings is predictable
- Crush is nearly guaranteed (historically)
- Sell expensive premium, buy back cheap
- Accept stock movement risk

#### A. Iron Condor (Earnings)

**Structure:**

- Sell OTM put spread
- Sell OTM call spread
- **Before earnings**, close **after**

**When to use:**

- Want defined risk
- Accept capped profit
- Conservative approach
- Systematic income

**Sizing:**

- Width includes expected move + buffer
- Typical: 1.5× expected move width

**Example:**

- Stock at $100, expected move: $10
- Sell $85/$80 put spread
- Sell $115/$120 call spread
- **Width: $15, move + $5 buffer**

**Entry timing:** 5-10 days before earnings
**Exit timing:** Day after earnings (immediately)

#### B. Short Strangle (Earnings)

**Structure:**

- Sell OTM put
- Sell OTM call
- Undefined risk
- **Higher profit potential**

**When to use:**

- Aggressive approach
- Confident in IV crush > move
- Can accept assignment
- Higher capital accounts

**Strike selection:**

- 1 SD from expected move
- Or 16-20 delta options
- Want meaningful premium

**Example:**

- Stock at $100, expected move: $8
- Sell $92 put (1 SD below move)
- Sell $108 call (1 SD above move)
- **Credit: $6-8** typically

**Management critical:**

- Close immediately after earnings
- Don't hold if stock breaks strike
- May need to roll

#### C. Credit Spreads (Earnings + Direction)

**Structure:**

- Sell closer strike
- Buy further strike
- **Directional bias + IV crush**

**When to use:**

- Have directional view
- Want defined risk
- Combine crush + direction
- Two edges

**Example (Bullish):**

- Expect stock up + IV crush
- Stock at $100
- Sell $95 put / Buy $90 put
- **Credit: $1.50**
- Benefits from up move + crush

**Key insight:**

- Can profit even if wrong on direction
- IV crush helps even if stock drops some
- Requires less precision

#### D. Covered Calls (Earnings)

**Structure:**

- Own 100 shares
- Sell call before earnings
- Collect elevated premium

**When to use:**

- Already own stock
- Willing to cap upside
- Generate income
- Conservative

**Strike selection:**

- OTM at price willing to sell
- Typical: +10-15% from current

**Example:**

- Own 100 shares @ $100
- Sell $110 call @ $5 (high IV!)
- **Income: $500**
- Keep if stock < $110

**Risk:**

- Stock gaps up >$110, shares called away
- But kept premium + gains to $110
- Usually acceptable

### 2. Post-Earnings Premium Buying

**Philosophy:**

- After crush, options are cheap
- IV at lows, will normalize
- Buy premium for directional plays
- Better risk/reward than pre-earnings

#### A. Debit Spreads (Post-Earnings)

**Structure:**

- Buy ITM or ATM
- Sell OTM
- **After earnings** at crushed IV

**When to use:**

- Have directional view
- Want cheap leverage
- Don't want naked long options
- Defined risk

**Example:**

- Earnings passed, IV crushed
- Stock at $105 (moved up)
- Buy $105 call @ $4 (IV crushed to 25%)
- Sell $115 call @ $1.50
- **Debit: $2.50** (much cheaper than pre-earnings)

#### B. Long Options (Post-Earnings)

**Structure:**

- Buy calls or puts
- After IV crush
- Simple directional

**When to use:**

- Very cheap entry
- Strong directional conviction
- Willing to accept theta
- Want unlimited upside

**Timing:**

- Day after earnings
- Or 2-3 days after (IV stabilized)
- Before IV starts building for next earnings

### 3. Hybrid Strategies (Before AND After)

#### A. Earnings Calendar Spread

**Structure:**

- Sell front month (through earnings)
- Buy back month (after earnings)
- **Profit from crush in front month**

**Example:**

- 2 weeks before earnings
- Sell 1-month $100 call (includes earnings)
- Buy 2-month $100 call (after earnings)
- **Debit: $3.00**

**What happens:**

- Front month IV spikes (good for short)
- Front month expires/crushes
- Back month unaffected
- **Profit from differential**

**Timing critical:**

- Enter 2-3 weeks before
- Front month expires just after earnings
- Back month far enough out

#### B. Reverse Iron Condor (Earnings)

**Structure:**

- Buy strangle (before earnings)
- Sell wider strangle (after earnings)
- Play the spike AND crush

**Advanced strategy:**

- Expensive and complex
- Needs big move + crush
- Not recommended for beginners

### 4. Avoiding Earnings (Defensive)

**Not a "strategy" but important:**

**If long options approaching earnings:**

**Option A: Close before earnings**
- Sell 3-5 days before
- Avoid the crush
- Take profit/loss

**Option B: Roll to later expiration**
- Close current position
- Buy later expiration (after earnings)
- Avoid crush, maintain position

**Option C: Convert to spread**
- Sell option at higher strike
- Creates defined risk spread
- Reduces crush impact

---

## Concrete Example 1: Iron Condor Earnings Play

**Setup:**

**Company:** AAPL (tech giant)
**Stock price:** $180
**Earnings:** 10 days away
**Current IV:** 45% (elevated already)
**Expected move:** $10 (5.6%)

**Analysis:**

**Historical data:**

- Average IV pre-earnings: 50-60%
- Average IV post-earnings: 20-25%
- Average crush: 50-60%
- Expected move vs actual move: 85% accuracy

**IV will likely:**

- Spike to 55-60% in next week
- Crush to 22-25% day after
- **Crush: ~35 points (58% decline)**

**The Trade (5 days before earnings):**

**Iron Condor Entry:**

**Put side:**

- Sell $170 put @ $4.20 (IV = 52%)
- Buy $165 put @ $2.30 (IV = 50%)
- **Credit: $1.90**

**Call side:**

- Sell $190 call @ $4.00 (IV = 53%)
- Buy $195 call @ $2.20 (IV = 51%)
- **Credit: $1.80**

**Total credit: $3.70 per IC**

**Position size:** 10 contracts
**Total credit received:** $3,700
**Max risk:** ($5 width - $3.70 credit) × 10 × 100 = $1,300

**Greeks (at entry):**

- Delta: -5 (nearly neutral)
- Vega: -$95 per 1% IV (short vega)
- Theta: +$55/day
- Gamma: -20

**Profit zone:** $170 to $190 (5.6% range each side)

**Management plan:**

- Close day after earnings
- Don't wait for expiration
- Stop: Stock breaks $168 or $192

### Outcome Scenario 1: Stock Stays in Range (Most Common - 60-70%)

**Day after earnings:**

**Stock:** $184 (+2.2% move, well within range)

**IV changes:**

- Pre-earnings: 52-53% average
- Post-earnings: 24%
- **Crush: 28-29 points (55% decline)**

**Position value:**

**Put spread:**

- $170 put: Was $4.20, now $0.60 (far OTM + crushed IV)
- $165 put: Was $2.30, now $0.25
- Spread worth: $0.35

**Call spread:**

- $190 call: Was $4.00, now $1.40 (OTM but closer + crushed IV)
- $195 call: Was $2.20, now $0.65
- Spread worth: $0.75

**Total position value: $1.10** (to buy back)

**P&L:**

- Received: $3.70
- Buy back: $1.10
- **Profit: $2.60 per IC**
- **Total: 10 × $260 = $2,600** (70% of max profit)

**Attribution:**

- IV crush: +$2,100 (81%)
- Theta (5 days): +$275 (11%)
- Stock move: +$225 (8%)

**CLOSE IMMEDIATELY - Don't be greedy!**

### Outcome Scenario 2: Stock Moves to Edge (20-25% of time)

**Day after earnings:**

**Stock:** $190 (exactly at short call strike!)

**IV crushed:** 53% → 24%

**Position value:**

**Put spread:** Nearly worthless ($0.10)

**Call spread:**

- $190 call: $4.50 (ATM at crushed IV)
- $195 call: $1.20
- Spread worth: $3.30

**Total: $3.40**

**P&L:**

- Received: $3.70
- Buy back: $3.40
- **Profit: $0.30 per IC** (small profit)
- **Total: $300**

**Still profitable despite hitting short strike!** (IV crush saved it)

### Outcome Scenario 3: Stock Gaps Beyond Wing (10-15% of time)

**Day after earnings:**

**Stock:** $196 (+8.9% gap - larger than expected)

**IV crushed:** 53% → 25%

**Position value:**

**Put spread:** Worthless

**Call spread:**

- $190 call: $6.50 ITM
- $195 call: $2.50 ITM
- Spread worth: $4.00 (near max width)

**Total: $4.00**

**P&L:**

- Received: $3.70
- Buy back: $4.00
- **Loss: -$0.30 per IC**
- **Total loss: -$300** (23% loss on capital at risk)

**Close and move on.**

**Even with loss, IV crush helped:**

- Without IV crush, spread would be worth $5.00 (full width)
- IV crush saved $1.00 × 10 = $1,000 in losses
- Could have been -$1,300 loss instead of -$300

### Outcome Scenario 4: Catastrophic Gap (Rare - 5%)

**Day after earnings:**

**Stock:** $210 (+16.7% gap - guidance raised dramatically)

**Position:**

- Both call options deep ITM
- Spread at full width ($5)
- Put spread worthless

**P&L:**

- Received: $3.70
- Spread worth: $5.00
- **Loss: -$1.30 per IC**
- **Total: -$1,300** (max loss, 100% of risk capital)

**This is the risk!**

**But historically:**

- Happens ~5% of the time
- Win rate 65-70% × avg profit covers this
- Positive expectancy over many trades

---

## Concrete Example 2: Short Strangle Earnings

**Setup:**

**Company:** TSLA (volatile stock)
**Stock:** $250
**Earnings:** 7 days away
**Current IV:** 60% (very elevated)
**Expected move:** $20 (8%)

**Analysis:**

**TSLA characteristics:**

- Very volatile
- Big earnings moves
- But IV crush always happens
- Risk/reward favorable historically

**The Trade (3 days before earnings):**

**Short Strangle:**

- Sell $230 put @ $9.50 (IV = 65%, 16-delta)
- Sell $270 call @ $9.00 (IV = 66%, 16-delta)
- **Total credit: $18.50 per strangle**

**Position size:** 3 contracts (conservative)
**Total credit:** $5,550

**Greeks:**

- Delta: +3 (neutral)
- Vega: -$145 per 1% IV
- Theta: +$90/day
- Gamma: -35

**Breakevens:** 

- Downside: $230 - $18.50 = $211.50
- Upside: $270 + $18.50 = $288.50

**Risk:** Undefined (but manage actively)

**Management:**

- Close day after earnings
- Stop: Stock breaks $225 or $275 (warning)
- Emergency: Stock at breakeven, close immediately

### Outcome: Stock Moves Big But IV Crush Saves It

**Day after earnings:**

**Stock:** $270 (+8% move, exactly at short call)

**IV changes:**

- Pre: 65-66%
- Post: 28%
- **Crush: 38 points (58%)**

**Position value:**

- $230 put: Was $9.50, now $0.40 (far OTM + crushed)
- $270 call: Was $9.00, now $5.20 (ATM + crushed)
- **Total: $5.60**

**P&L:**

- Received: $18.50
- Buy back: $5.60
- **Profit: $12.90 per strangle**
- **Total: 3 × $1,290 = $3,870** (70% profit)

**IV crush overcame the directional move!**

**Without IV crush:**

- $270 call would be worth $15+ at original IV
- Would be a $6,000+ loss
- **IV crush saved $10,000+**

**This is the power of the strategy!**

---

## Concrete Example 3: Avoiding IV Crush (Defensive)

**Setup:**

**Position:** Long 10 contracts $100 calls
**Cost basis:** $5.00 per call (entered 30 days ago)
**Current:** $7.50 (up 50%, nice profit)
**Issue:** Earnings in 5 days
**IV:** 50% (spiked from 25%)

**Decision point:**

**Option A: Hold through earnings (BAD)**

**Scenario if stock moves to $108:**

- Without IV crush: Call worth $12 (would be great!)
- With IV crush (50% → 22%): Call worth $8.50
- **Profit limited by crush**

**Scenario if stock stays at $100:**

- IV crushes to 22%
- Call worth $2.50
- **From $7.50 to $2.50 = -67% loss in one day!**

**Option B: Close before earnings (SMART)**

**Action:** Sell all 10 calls @ $7.50

**P&L:**

- Cost: $5.00
- Sell: $7.50
- **Profit: $2.50 per call = $2,500 (50% gain)**

**Lock in profit, avoid crush risk!**

**Option C: Roll to later expiration**

**Action:**

- Sell current $100 calls @ $7.50
- Buy 60-day $100 calls @ $6.20 (later expiration, lower IV)
- **Net credit: $1.30**

**Result:**

- Maintained position
- Collected $1,300
- After earnings, IV normalizes
- Continue holding for upside

**This is smart management!**

---

## Strike Selection Strategy

### For Pre-Earnings Short Premium

**Goal:** Capture IV crush while giving stock room to move

**Expected move calculation:**

**Method 1: ATM Straddle Price**

$$
\text{Expected Move} \approx \text{ATM Straddle Price} \times 0.85
$$

**Example:**

- ATM straddle costs $15
- Expected move: $15 × 0.85 = $12.75 (one direction)

**Method 2: IV-based (more accurate)**

$$
\text{Expected Move} = S \times \text{IV} \times \sqrt{\frac{T}{365}}
$$

**Example:**

- Stock $100, IV 60%, days to earnings 7
- Expected move = $100 × 0.60 × √(7/365) = $8.30

**Strike selection rules:**

**Conservative (Iron Condor):**

- **Strikes at 1.5× expected move**
- Example: Expected $8, use $88/$112 strikes
- Lower profit, higher win rate (75-80%)

**Standard (Iron Condor):**

- **Strikes at 1.0-1.2× expected move**
- Example: Expected $8, use $92/$108 strikes
- Balanced
- Win rate: 65-70%

**Aggressive (Short Strangle):**

- **Strikes at 0.8-1.0× expected move**
- Example: Expected $8, use $92/$108 naked
- Higher profit, more risk
- Win rate: 60-65%

### For Post-Earnings Long Premium

**Goal:** Buy cheap, directional exposure

**Strike selection:**

**ATM or slightly ITM:**

- Maximum leverage
- Cheap after crush
- Delta 45-55

**Example:**

- Stock at $105 post-earnings
- Buy $100 call (ITM) cheap
- Or buy $105 call (ATM) cheapest

**Avoid deep OTM:**

- Still expensive relative to probability
- Theta painful
- Better to use spreads

---

## Time Frame Selection

### For Pre-Earnings Selling

**Front month containing earnings:**

**Optimal entry:** 5-15 days before earnings

**Why:**

- IV building but not peaked
- Enough time to collect theta
- Not too early (IV hasn't spiked)

**Entry timing sweet spots:**

```
Days Before | IV Level | Entry Quality
------------|----------|---------------
20-30       | Normal   | Too early
15-20       | Building | Good
10-15       | Elevated | Ideal
5-10        | High     | Good
1-5         | Peak     | Risky (late)
0-1         | Maximum  | Don't enter!
```

**Exit timing:**

**Immediately after earnings release:**

- Morning after if earnings after hours
- Same day if earnings pre-market
- Don't wait!

**Why close immediately:**

- Crush happens instantly
- Capture full IV drop
- Avoid gamma risk continuing

### For Post-Earnings Buying

**Entry timing:**

**Day after earnings:**

- IV fully crushed
- Cheapest entry
- Direction clarifying

**Or 2-3 days after:**

- IV stabilized
- Can assess direction better
- Still cheap

**Expiration:**

**30-60 days out:**

- Enough time for thesis
- Lower daily theta
- Not too expensive

---

## Position Management

### Managing Pre-Earnings Positions

**Entry checklist:**

✓ Earnings date confirmed (check company IR)
✓ Expected move calculated
✓ Strikes selected (1-1.5× expected move)
✓ IV already elevated (>40% typically)
✓ Historical crush pattern confirmed
✓ Position sized (5-10% max of portfolio)
✓ Exit plan defined

**During the trade (pre-earnings):**

**Daily monitoring:**

1. **IV level:** Continuing to spike?
2. **Stock price:** Still in expected range?
3. **Days to earnings:** On schedule?
4. **News:** Any early release risk?

**If IV spikes more:**

- Good! More crush potential
- Consider adding if very early (15+ days)

**If stock moves toward short strike (5+ days before):**

- May need to roll strike out
- Or close early
- Don't let winner become loser

**Critical day before earnings:**

**Review position:**

- In profit zone still?
- Expected move reasonable?
- Comfortable holding through?

**If stock outside strikes:**

- Close position (take small loss)
- Don't gamble on reversal

**The earnings day:**

**After hours earnings (most common):**

- Stock moves after close
- Options adjust pre-market next day
- **Close at open next morning**

**Pre-market earnings:**

- Stock moves before open
- Options adjust at open
- **Close at open**

**Intraday earnings (rare):**

- Close immediately after release
- Don't wait

**CRITICAL: Close day after earnings, no exceptions!**

**Why:**

- IV crush captured ✓
- Gamma risk eliminated ✓
- Redeploy capital ✓
- Don't get greedy ✗

### Managing Post-Earnings Positions

**Entry checklist:**

✓ Earnings passed
✓ IV crushed (check it's actually low)
✓ Direction identified
✓ Normal strategy applies
✓ Next earnings >60 days away

**Management:**

- Normal option management rules
- Not earnings-specific anymore
- Focus on directional thesis

---

## Greeks Analysis

### Pre-Earnings Short Premium Greeks

**Vega (THE CRITICAL GREEK):**

**For Iron Condor:**

$$
\text{Vega}_{\text{IC}} = \text{Vega}_{\text{short puts}} + \text{Vega}_{\text{short calls}} - \text{Vega}_{\text{long wings}}
$$

**Typically:**

- Net vega: -$80 to -$120 per 1% IV
- **This is your edge!**
- IV drop = profit

**Example P&L from IV:**

- Vega: -$100 per 1% IV
- IV drop: 35 points (60% → 25%)
- **Profit: $3,500 from IV alone**

**Theta (Secondary):**

**For short premium:**

- Positive theta (+$40-80/day typical)
- But only 5-7 days to collect
- Total theta: $200-$560

**Much smaller than vega impact!**

**Gamma (The Risk):**

**For short premium:**

- Negative gamma (-20 to -40 typical)
- Large moves hurt
- **This is the main risk**

**Break-even on gamma vs vega:**

$$
\text{Vega Profit} > \text{Gamma Loss} \Rightarrow \text{Win}
$$

**Historical:** Vega wins 65-70% of the time

### Post-Earnings Long Premium Greeks

**Vega (Reduced Importance):**

- Net long vega
- But IV already crushed
- Not expecting more expansion
- Just cheap entry point

**Delta (Primary):**

- Directional bet
- Normal option mechanics
- This is the edge now

**Theta (The Cost):**

- Negative theta
- But options cheap, so tolerable
- Time horizon important

---

## When to Use Earnings IV Crush Strategies

### Use Pre-Earnings Short Premium When:

**Market conditions ✓**

- **Earnings date confirmed**
- IV already elevated (>40% minimum)
- Historical crush pattern exists (check past earnings)
- Expected move reasonable (not binary biotech)
- 5-15 days before earnings

**Stock characteristics ✓**

- **Established company** (predictable patterns)
- Good liquidity (tight spreads)
- Historical data available (3+ earnings)
- Not extreme volatility (avoid $5 biotech)

**Examples of good candidates:**

- Large cap tech (AAPL, MSFT, GOOGL)
- Mega caps (SPY, QQQ)
- Established stocks (DIS, NKE, SBUX)

**Your situation ✓**

- Can hold through earnings
- Accept undefined risk (strangle) or defined (IC)
- Will close day after (discipline)
- Understand the mechanics

**Avoid pre-earnings selling when ✗**

- **Binary event** (biotech FDA decision)
- Uncertain timing (no confirmed date)
- IV not elevated yet (<30%)
- Poor liquidity
- Very small stock (<$20)
- Can't monitor through earnings
- First time (practice first!)

### Use Post-Earnings Buying When:

**Market conditions ✓**

- **Earnings just passed**
- IV crushed (verify it's low)
- Have directional view
- Next earnings >60 days away

**Avoid post-earnings buying when ✗**

- IV didn't actually crush (check!)
- No directional conviction
- Next earnings soon (<45 days)
- Options still expensive (rare but happens)

---


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

### 1) Entering Too Late (Peak IV)

**The error:**

- Entering 1-2 days before earnings
- "IV is at 70%, huge crush coming!"
- But already priced in
- Stock gaps beyond strikes
- **No time to adjust**

**Fix:**

- **Enter 5-15 days before**
- IV still building
- Time to collect theta
- Room to adjust if needed

### 2) Holding Too Long After Earnings

**The error:**

- Entered short strangle
- Earnings passed, big profit
- "I'll wait for more theta decay"
- Stock moves next day
- **Give back all gains**

**Fix:**

- **Close day after earnings**
- Crush captured ✓
- Don't be greedy
- Redeploy capital

### 3) Strikes Too Tight

**The error:**

- Expected move: $10
- Sell strikes at $8 (inside expected)
- "Want more premium!"
- Stock moves $12
- **Loss**

**Fix:**

- **1.0-1.5× expected move** minimum
- Rather get less premium and win
- Consistent small wins > occasional big losses

### 4) Ignoring Expected Move

**The error:**

- Not calculating expected move
- Using arbitrary strikes
- "I think $95/$105 looks good"
- **No mathematical basis**

**Fix:**

- **Always calculate expected move**
- Use ATM straddle × 0.85
- Or IV × price × √(days/365)
- Base strikes on this

### 5) Position Too Large

**The error:**

- "IV crush is guaranteed!"
- 50% of portfolio in earnings trades
- One bad gap = catastrophic
- **Concentration risk**

**Fix:**

- **Max 5-10% per earnings trade**
- Diversify across multiple earnings
- Never more than 30% total in earnings
- Protect capital

### 6) Ignoring Earnings Quality

**The error:**

- Trading biotech FDA decision
- Or penny stock earnings
- **Binary outcome, not normal distribution**
- IV crush doesn't help if stock goes to $0

**Fix:**

- **Stick to established stocks**
- $50+ price minimum
- Normal businesses (tech, retail, etc.)
- Avoid binary biotech/clinical trials

### 7) Long Options Through Earnings

**The error:**

- Bought calls 30 days ago
- Up 50%, earnings in 3 days
- "I'll hold for the big move!"
- Stock moves favorably but IV crushes
- **Profit evaporates**

**Fix:**

- **Close 3-5 days before earnings**
- Or roll to post-earnings expiration
- Never hold long options through earnings
- The crush will hurt you

---

## Advanced Concepts

### 1. Quantifying Historical Crush Patterns

**Backtesting framework:**

For each stock, calculate:

$$
\text{Crush Ratio} = \frac{\text{IV}_{\text{post}}}{\text{IV}_{\text{pre}}}
$$

**Example data (AAPL, last 20 earnings):**

```
Earnings Date | IV Pre | IV Post | Crush Ratio | Stock Move
--------------|--------|---------|-------------|------------
2024 Q1       | 55%    | 22%     | 0.40        | +5.2%
2023 Q4       | 60%    | 25%     | 0.42        | -3.1%
2023 Q3       | 48%    | 20%     | 0.42        | +7.8%
...

Average Crush Ratio: 0.41
Std Dev: 0.08
Min: 0.30
Max: 0.55
```

**Use this data:**

- Predict post-earnings IV
- Size positions based on consistency
- Avoid stocks with erratic patterns

### 2. Expected Move Accuracy

**Compare expected vs actual:**

$$
\text{Accuracy} = \frac{\text{Actual Move}}{\text{Expected Move}}
$$

**Historical analysis:**

```
Stock | Expected Move Accuracy | Conclusion
------|------------------------|------------
AAPL  | 0.85 (moves 15% less) | Conservative estimate
TSLA  | 1.20 (moves 20% more) | Aggressive estimate
SPY   | 0.90 (moves 10% less) | Good estimate
```

**Adjust strike selection:**

- If accuracy > 1.0: Use wider strikes
- If accuracy < 0.9: Can use tighter strikes
- Improves win rate

### 3. Optimal Entry Timing

**Backtest different entry timings:**

```
Days Before | Avg Profit | Win Rate | Sharpe
------------|------------|----------|--------
1-3 days    | 2.1%      | 58%      | 0.9
3-7 days    | 2.8%      | 65%      | 1.3
7-10 days   | 3.2%      | 68%      | 1.5
10-15 days  | 2.9%      | 67%      | 1.4
15-20 days  | 2.3%      | 63%      | 1.1
```

**Finding:** 7-10 days before earnings optimal

**Why:**

- IV building but not peaked
- Enough theta collection time
- Can still adjust
- Not too early (IV may not spike yet)

### 4. Multi-Earnings Portfolio Theory

**Diversification across earnings:**

**Instead of 1 large position:**

- 10 small earnings positions
- Spread across different weeks
- Different sectors
- Different expected moves

**Result:**

- Lower volatility
- More consistent returns
- Survival of losing streaks
- Professional approach

**Example portfolio:**

```
Week  | Stocks          | Allocation | Expected Return
------|-----------------|------------|----------------
Week 1| AAPL, MSFT     | 10%        | +2.5%
Week 2| GOOGL, AMZN    | 10%        | +3.1%
Week 3| TSLA, NVDA     | 10%        | +2.8%
Week 4| DIS, NKE       | 10%        | +2.2%

Monthly Expected: +10.6% on 40% of capital
```

### 5. Volatility Surface Changes

**The surface transforms around earnings:**

**Pre-earnings surface:**
```
        IV
         ↑
    65% |      /‾‾‾\     ← Elevated everywhere
    55% |    /       \
    45% |  /           \
         |_______________ Strike
         OTM  ATM  OTM
```

**Post-earnings surface:**
```
        IV
         ↑
    30% |      /‾\       ← Crushed everywhere
    25% |    /     \
    20% |  /         \
         |_______________ Strike
         OTM  ATM  OTM
```

**The whole surface shifts down!**

**Implication:**

- Not just ATM that crushes
- All strikes crush (wings too)
- Can trade any strike
- But ATM has most vega

### 6. Earnings Announcement Timing Matters

**After-hours vs Pre-market:**

**After-hours (most common):**

- Announce after 4pm ET
- Stock moves after close
- Options react next morning
- **Best for overnight holding**

**Pre-market (less common):**

- Announce before 9:30am ET
- Stock gaps at open
- More slippage on close
- **Harder to manage**

**Intraday (rare):**

- Announce during market hours
- Immediate reaction
- **Can close instantly (best)**

**Check timing before entry!**

---

## Real-World Examples

### Example 1: AAPL Earnings (Q1 2024)

**Setup:**

- Date: February 1, 2024
- Stock: $185
- 10 days before earnings

**IV Analysis:**

- Current IV: 42%
- Expected to spike to: 55-60%
- Historical post-earnings IV: 20-25%
- Expected crush: 30-35 points

**Expected move:** $10 (5.4%)

**The Trade (Jan 22, 2024):**

**Iron Condor:**

- Sell $175/$170 put spread @ $1.85
- Sell $195/$200 call spread @ $1.75
- **Total credit: $3.60**
- **Position: 20 contracts**
- **Credit: $7,200**

**What happened:**

**Feb 1 (earnings day):**

- After hours, AAPL reports beats
- Stock jumps to $191 (+3.2%)
- Within range ✓

**Feb 2 (next morning):**

**IV crushed:**

- Pre: 58% (had spiked further)
- Post: 23%
- **Crush: 35 points (60%)**

**Position value:**

- Put spread: $0.15 (far OTM + crushed)
- Call spread: $0.95 (close to short strike + crushed)
- **Total: $1.10**

**Close immediately:**

**P&L:**

- Credit received: $3.60
- Buy back: $1.10
- **Profit: $2.50 per IC**
- **Total: 20 × $250 = $5,000 (69% profit)**

**Holding period:** 11 days
**Return:** 69% (annualized: 2,290%!)

**Why it worked:**

- IV crush as predicted ✓
- Stock stayed in range ✓
- Closed immediately ✓
- Proper strike selection ✓

### Example 2: TSLA Earnings - The Gap

**Setup:**

- Date: April 2024
- Stock: $170
- Earnings in 5 days

**Trade:**

**Short Strangle (aggressive):**

- Sell $150 put @ $7.50
- Sell $190 call @ $7.00
- **Credit: $14.50**
- **Position: 5 contracts**

**Expected move:** $18 (10.6%)

**Strikes at 1.18× expected move**

**What happened:**

**Earnings disaster:**

- TSLA misses badly
- Stock gaps down to $145 (-14.7%)
- **Beyond short put!**

**Next morning:**

**IV crushed but stock below put:**

- IV: 75% → 35% (crushed)
- Stock at $145
- $150 put: $5.50 ITM + crushed IV = worth $6.50
- $190 call: Worthless

**Close position:**

**P&L:**

- Credit: $14.50
- Close put: -$6.50
- Close call: -$0.10
- **Profit: $7.90 per strangle**
- **Total: 5 × $790 = $3,950 (54% profit)**

**Even with gap beyond strike, still profitable!**

**Why:**

- Massive IV crush (40 points)
- Put didn't go full ITM value due to crush
- Shows power of strategy

**If IV hadn't crushed:**

- $150 put would be worth $12+ at original IV
- Would be a $2,500 loss
- **IV crush saved the trade**

### Example 3: The Losing Trade (Reality Check)

**Setup:**

- Small cap stock
- Stock: $45
- Earnings in 3 days

**Trade:**

**Iron Condor (too aggressive):**

- Sell $40/$38 put spread
- Sell $50/$52 call spread
- Credit: $1.80
- Position: 10 contracts

**Expected move:** $5 (11%)
**Actual strikes:** Only $5 wide (at expected move, not beyond!)

**Mistake:** Strikes too tight

**What happened:**

**Earnings shock:**

- FDA approval announced with earnings
- Stock gaps to $58 (+28.9%)
- **Way beyond calls**

**Next morning:**

**Position:**

- Put spread: Worthless
- Call spread: Full width ($2.00)

**P&L:**

- Credit: $1.80
- Loss: -$2.00
- **Loss: -$0.20 per IC**
- **Total: -$200**

**But wait:**

- Max loss on IC: Width - Credit = $2.00 - $1.80 = $0.20 ✓
- Defined risk worked ✓
- Lost 100% of capital at risk

**Lessons:**

1. **Can't win them all** (even with IV crush)
2. **Strikes too tight** was the mistake
3. **Defined risk** prevented catastrophic loss
4. **Position sizing** kept loss to 1% of portfolio
5. **Move on to next trade**

**Historical edge still positive:**

- If 7/10 trades make $300
- And 3/10 lose $200
- Net: +$1,500 per 10 trades
- Positive expectancy ✓

---

## Practical Implementation

### 1. Earnings Calendar Tracking

**Weekly workflow:**

**Sunday evening:**

```
1. Get next week's earnings calendar
   - Use: earnings.com, nasdaq.com, broker
   - Note: Company, date, time (AM/PM)

2. Filter for candidates:
   - Market cap > $5B
   - Price > $50
   - Liquid options (>1000 volume)
   - Established (3+ years public)

3. Analyze each:
   - Current IV
   - Historical IV pattern
   - Expected move
   - Days until earnings

4. Plan entries:
   - Which to trade
   - When to enter (5-10 days before)
   - Strike selection
   - Position size
```

**Example watchlist:**

```
Next Week's Earnings (Feb 5-9):

Mon 2/5:
- GOOGL: $140, IV 45%, Expected $8, Enter 1/29
- DIS: $95, IV 38%, Expected $6, Enter 1/30

Wed 2/7:
- AAPL: $185, IV 42%, Expected $10, Enter 1/31
- MSFT: $415, IV 35%, Expected $25, Enter 2/1

Fri 2/9:
- AMZN: $175, IV 48%, Expected $12, Enter 2/2
```

### 2. Entry Checklist Template

```
=== EARNINGS TRADE CHECKLIST ===

Company: _______
Ticker: _______
Earnings Date: _______
Time: AM / PM (circle)

ANALYSIS:
Stock Price: $_______
Current IV: _______% 
Expected Move: $_______
Historical Crush: _______% → _______% 

STRATEGY:
Type: IC / Strangle / Credit Spread
Entry Date: _______ (5-10 days before)

STRIKES:
Put: $_____ / $_____
Call: $_____ / $_____
Width: Within 1-1.5× expected move? Y / N

POSITION:
Contracts: _______
Credit: $_______
Max Risk: $_______
% of Portfolio: _______% (< 10%? Y / N)

EXIT PLAN:
Close: Day after earnings
Stop: Stock breaks $_____ or $_____

APPROVAL:
☐ Earnings date confirmed
☐ IV elevated (>40%)
☐ Historical pattern checked
☐ Strikes calculated properly
☐ Position sized appropriately
☐ Exit plan defined

Ready to enter: Y / N
```

### 3. Live Position Tracker

**Spreadsheet format:**

```
| Ticker | Entry | DTE | IV Now | Stock | P&L | Status | Action |
|--------|-------|-----|--------|-------|-----|--------|--------|
| AAPL   | 1/22  | 5   | 58%    | $187  | +$45| Hold   | Close 2/2 |
| GOOGL  | 1/25  | 8   | 52%    | $142  | +$32| Hold   | Close 2/5 |
| TSLA   | 1/28  | 4   | 73%    | $172  | +$28| Hold   | Close 2/3 |
```

**Day of earnings:**

```
Set calendar reminder:
- "AAPL Earnings Tonight - Close Tomorrow AM"
- "GOOGL Earnings Tomorrow AM - Close at Open"
```

### 4. Post-Trade Analysis

**After each earnings trade:**

```
=== EARNINGS TRADE REVIEW ===

Ticker: AAPL
Date: Feb 1, 2024

PLANNED:
Entry IV: 42%
Exit IV: Expected 22%
Expected Move: $10
Strikes: $175 / $195

ACTUAL:
Entry IV: 42% ✓
Peak IV: 58% (good!)
Exit IV: 23% ✓
Actual Move: $6 ✓
Stock: $191 (in range ✓)

P&L:
Planned: $2.50
Actual: $2.50
Hit target: YES

LESSONS:
✓ Entered at right time (10 days)
✓ IV spiked more than expected (bonus)
✓ Closed immediately (discipline)
✓ Strike selection good

GRADE: A
```

**Monthly summary:**

```
February 2024 Earnings Trades:

Total Trades: 12
Wins: 9 (75%)
Losses: 3 (25%)
Avg Win: +$285
Avg Loss: -$155
Net P&L: +$2,100
Capital Used: $8,500
ROI: 24.7%

Best Trade: AAPL (+$500)
Worst Trade: Small cap gap (-$300)

Lessons:
- 7-10 day entry optimal
- Small caps riskier (avoid <$5B)
- Iron Condors better than strangles (defined risk)
```

### 5. Automation Tools

**Python earnings screener:**

```python
import yfinance as yf
from datetime import datetime, timedelta

def screen_earnings_opportunities():
    # Get earnings calendar
    earnings_this_week = get_earnings_calendar()
    
    opportunities = []
    
    for ticker in earnings_this_week:
        # Get data
        stock = yf.Ticker(ticker)
        current_price = stock.info['currentPrice']
        market_cap = stock.info['marketCap']
        
        # Filter criteria
        if current_price < 50 or market_cap < 5e9:
            continue
        
        # Get IV
        current_iv = get_current_iv(ticker)
        historical_iv = get_average_iv(ticker)
        
        # Check IV elevated
        if current_iv > historical_iv * 1.5:
            
            # Calculate expected move
            expected_move = calculate_expected_move(ticker)
            
            # Days to earnings
            days_to_earnings = get_days_to_earnings(ticker)
            
            # Entry recommendation
            if 5 <= days_to_earnings <= 15:
                entry_signal = "ENTER NOW"
            elif days_to_earnings > 15:
                entry_signal = f"Wait {days_to_earnings - 10} days"
            else:
                entry_signal = "TOO LATE"
            
            opportunities.append({
                'Ticker': ticker,
                'Price': current_price,
                'IV': current_iv,
                'IV vs Avg': f"{current_iv/historical_iv:.1%}",
                'Expected Move': expected_move,
                'Days to Earnings': days_to_earnings,
                'Signal': entry_signal
            })
    
    return sorted(opportunities, 
                  key=lambda x: x['IV vs Avg'], 
                  reverse=True)

# Run weekly
results = screen_earnings_opportunities()
print_formatted_table(results)
```

---

## Earnings IV Crush in Your Toolkit

### How Earnings Strategies Fit Overall

**The complete options framework:**

```
Options Trading Approaches:

1. DIRECTIONAL
   ├── Long Calls/Puts
   └── Spreads

2. VOLATILITY LEVEL
   ├── IV Rank strategies
   └── Vega trading

3. EVENT-DRIVEN ← Earnings IV Crush!
   ├── Pre-earnings (sell premium)
   ├── Post-earnings (buy premium)
   └── Defensive (avoid crush)

4. STRUCTURAL
   ├── Calendars
   ├── Diagonals
   └── Butterflies

5. SURFACE
   └── Arbitrage
```

**Earnings strategies uniquely provide:**

- **Predictable catalyst** (dates known in advance)
- **High-probability edge** (crush is nearly guaranteed)
- **Short holding period** (5-15 days)
- **Repeatable** (every quarter, multiple stocks)
- **Independent of market direction**

### Comparison with Other IV Strategies

| Strategy | Edge | Holding Period | Win Rate | Complexity |
|----------|------|----------------|----------|------------|
| **IV Rank** | Mean reversion | 20-45 days | 65-70% | Medium |
| **Calendars** | Term structure | 15-30 days | 60-65% | Medium |
| **Earnings Crush** | **Event-driven** | **5-15 days** | **65-75%** | **Medium** |
| **Surface Arb** | Mispricing | Varies | 60-65% | High |

**Earnings advantages:**

- **Known timing** (exact date)
- **Predictable pattern** (crush is reliable)
- **High frequency** (weekly opportunities)
- **Fast capital turnover** (2-week holds)
- **Can specialize** (become earnings expert)

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


## What to Remember

### Core Concept

**Earnings IV Crush is the predictable phenomenon where:**

$$
\text{IV}_{\text{pre-earnings}} > \text{IV}_{\text{post-earnings}}
$$

**Typical crush magnitude:**

- Pre-earnings IV: 50-70%
- Post-earnings IV: 20-30%
- **Decline: 30-40 points (50-70% drop)**

**This happens REGARDLESS of stock direction!**

### The Pattern

**The Earnings IV Cycle:**

```
Base → Build-up → Peak → CRUSH → Recovery
20%     30%       60%     25%      20%
              ↑           ↓
          Sell Here   Buy Back
```

**Timeline:**

- 30 days before: Base IV
- 10-20 days: Building
- 5-1 days: Peak (enter here!)
- Day after: Crush (exit here!)
- 2-30 days: Normalize

### The Strategies

**Pre-Earnings (Sell Premium):**

**When:** 5-15 days before earnings
**Why:** Capture IV crush
**How:** Iron Condors, Short Strangles, Credit Spreads
**Exit:** Day after earnings (immediately!)

**Post-Earnings (Buy Premium):**

**When:** Day after earnings
**Why:** Options are cheap
**How:** Debit Spreads, Long Options
**Exit:** Normal timeframe (30-60 days)

**Defensive (Avoid Crush):**

**When:** Have long options, earnings approaching
**How:** Close 3-5 days before, OR roll to post-earnings
**Why:** Don't get crushed!

### Strike Selection

**Expected move calculation:**

$$
\text{Expected Move} \approx \text{ATM Straddle Price} \times 0.85
$$

**Or:**

$$
\text{Expected Move} = S \times \text{IV} \times \sqrt{\frac{T}{365}}
$$

**Strike placement:**

- **Conservative:** 1.5× expected move
- **Standard:** 1.0-1.2× expected move  
- **Aggressive:** 0.8-1.0× expected move

**Example:**

- Stock $100, expected move $10
- Conservative: $85/$115 strikes
- Standard: $90/$110 strikes
- Aggressive: $92/$108 strikes

### Time Frames

**Entry:** 5-15 days before earnings
- Sweet spot: 7-10 days
- Not too early, not too late

**Exit:** Day after earnings
- After hours earnings → Close next morning
- Pre-market earnings → Close at open
- **No exceptions!**

### Why It Works

**The edge comes from:**

1. **Uncertainty resolution:** Binary event creates, then eliminates uncertainty
2. **Predictability:** Crush happens nearly 100% of the time
3. **Magnitude:** 50-70% IV decline is massive
4. **Vega dominance:** IV effect > stock movement effect (usually)
5. **Frequency:** Hundreds of opportunities per quarter

**Historical success rate:** 65-75% wins

### Greeks

**Pre-Earnings Short Premium:**

- **Vega:** -$80 to -$150 per 1% IV ← **THE EDGE**
- **Theta:** +$40-80/day (secondary)
- **Gamma:** -20 to -40 (the risk)
- **Delta:** ≈ 0 (neutral)

**The math:**

- Vega × IV crush = $3,000-5,000 profit (typical)
- Gamma × move = $500-1,500 loss (typical)
- **Net: +$1,500-3,500 profit**

### Success Factors

**What you need:**

1. **Discipline:** Enter 7-10 days before, exit day after
2. **Calculation:** Always compute expected move
3. **Risk management:** Max 5-10% per trade
4. **Patience:** Wait for good setups (established stocks)
5. **Execution:** Close immediately, no greed

### The Deep Insight

**Earnings IV Crush reveals:**

> "Option prices before earnings embed uncertainty about an unknown future event. When that event occurs, uncertainty collapses instantly, and so must option prices—regardless of which direction the stock moved. This creates a nearly guaranteed reduction in implied volatility that can be systematically harvested by selling premium before earnings and buying it back after."

**The pattern:**

- **Amateur:** Buys calls before earnings, gets crushed
- **Novice:** Recognizes IV spike, still buys options
- **Intermediate:** Sells premium but wrong timing
- **Advanced:** Systematic earnings strategy (7-10 days before, close day after)
- **Expert:** Diversified earnings portfolio, statistical tracking

### Common Pitfalls

1. ❌ Entering too late (1-2 days before)
2. ❌ Strikes too tight (inside expected move)
3. ❌ Holding after earnings (giving back gains)
4. ❌ Over-sizing (>10% per trade)
5. ❌ Trading small/biotech stocks (binary risk)
6. ❌ Long options through earnings (crush victim)
7. ❌ Ignoring expected move calculation

### When to Use

**Perfect for earnings strategies ✓:**

- Large cap stocks ($50+ price, $5B+ market cap)
- Established companies (3+ years public)
- Normal businesses (not binary biotech)
- Confirmed earnings date
- IV already elevated (>40%)
- 5-15 days before earnings
- Good liquidity (tight spreads)

**Avoid earnings strategies ✗:**

- Binary events (FDA decisions)
- Penny stocks (<$20)
- Poor liquidity
- Uncertain timing
- IV not elevated
- Too close to earnings (<5 days)
- Can't monitor through earnings

### Performance Expectations

**Realistic targets (systematic):**

**Per trade:**

- Win rate: 65-75%
- Average win: +50-70% of capital at risk
- Average loss: -50-100% of capital at risk
- Holding period: 7-15 days

**Portfolio (10 trades/month):**

- Monthly return: +8-15% on deployed capital
- Annualized: +96-180%
- Max drawdown: -15% to -25%
- Sharpe ratio: 1.5-2.0

**Key:** Consistency over time through diversification

### Final Thought

**Earnings IV Crush strategies teach:**

> "The most predictable pattern in options trading is the IV spike before earnings and collapse after. By systematically selling expensive premium before earnings and closing the day after, traders exploit one of the few truly reliable inefficiencies in options markets. Success requires discipline (timing), calculation (expected move), and risk management (position sizing), but the edge is real and repeatable."

**The strategic value:**

- **High frequency** (weekly opportunities)
- **Fast turnover** (2-week holds)
- **Predictable** (crush is nearly guaranteed)
- **Independent** (market direction doesn't matter)
- **Systematic** (rules-based, repeatable)
- **Specialization** (can become earnings expert)

**This completes your understanding of how to systematically profit from the most predictable volatility pattern in options: the earnings IV crush!** 🎯📊📈

**You now understand: the earnings IV cycle, optimal timing (7-10 days before), strike selection (1-1.5× expected move), management (close day after), and why it works—the complete earnings IV crush framework!**
