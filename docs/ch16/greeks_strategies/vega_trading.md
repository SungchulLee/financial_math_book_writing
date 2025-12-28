# Vega Trading

**Vega trading** is a strategy where you profit from changes in implied volatility by holding options positions while hedging away directional risk.

---

## The Core Insight

**The fundamental idea:**
- Options have two types of volatility exposure:
  - **Realized volatility** (actual stock movement)
  - **Implied volatility** (market's expectation, embedded in option prices)
- You can bet that implied volatility is wrong without betting on stock direction
- Delta hedge to remove directional exposure
- Profit when implied volatility moves toward your expectation

**You're essentially betting: "The market's fear/expectation of volatility is mispriced."**

---

## The Two Types of Volatility

**This distinction is CRUCIAL:**

### Realized Volatility (Historical/Future Actual)
- **What it is:** How much the stock ACTUALLY moves
- **Measured by:** $\sigma_{\text{realized}} = \sqrt{\frac{252}{T}\sum (\text{daily returns})^2}$
- **Example:** Stock bounces between $90 and $110 → high realized volatility
- **Who trades it:** Gamma scalpers

### Implied Volatility (Market's Expectation)
- **What it is:** The market's EXPECTATION of future volatility, embedded in option prices
- **Derived from:** Option prices via Black-Scholes (solving for $\sigma$)
- **Example:** Options are expensive → market expects high volatility → high IV
- **Who trades it:** Vega traders

**The key insight:** These two can diverge!
- Market might expect 40% volatility (IV = 40%)
- But stock might actually realize only 25% volatility
- Or vice versa!

---

## Vega Trading: Betting on Implied Volatility Changes

**Vega trading is NOT about realized volatility—it's about IMPLIED volatility changes!**

### What Is Vega?

**Vega** ($\mathcal{V}$ or $\nu$) measures how much an option's value changes when implied volatility changes:

$$
\text{Vega} = \frac{\partial V}{\partial \sigma}
$$

**In plain English:**
- If vega = 0.20, then a 1% increase in IV → option value increases by $0.20
- Long options have positive vega (benefit from IV increase)
- Short options have negative vega (hurt by IV increase)

---

## The Basic Idea

**What you do:**
1. Identify mispriced implied volatility
   - Too high? Sell options (short vega)
   - Too low? Buy options (long vega)
2. Delta hedge to remove directional exposure
3. Hold the position as IV changes
4. Profit when IV moves toward your expectation
5. Exit when IV reaches fair value (or your target)

**The goal:** Profit from implied volatility changes, not from stock direction or realized volatility.

**Key distinction from gamma scalping:**
- Gamma scalping: profit from stock MOVING (realized vol)
- Vega trading: profit from IV CHANGING (implied vol)

---

## The Portfolio

Your vega trading portfolio consists of:

$$
\Pi = \text{Option Position} + \text{Delta Hedge}
$$

More precisely:
$$
\Pi = V(S, t, \sigma) - \Delta \cdot S
$$

where $V(S,t,\sigma)$ is the option value (function of stock price, time, AND volatility), and you hedge with $\Delta$ shares.

**Why this structure?**
- The option gives you vega exposure (sensitivity to IV changes)
- The delta hedge removes directional exposure
- You're now exposed primarily to changes in implied volatility
- You've isolated the volatility risk

---

## The P&L Formula

For a vega-hedged portfolio, over a short time interval $\delta t$:

$$
\delta \Pi \approx \text{Vega} \cdot \delta\sigma + \frac{1}{2}\Gamma(\delta S)^2 - \theta\,\delta t
$$

**What this means:**

1. **$\text{Vega} \cdot \delta\sigma$**: P&L from implied volatility changes
   - This is your PRIMARY profit source in vega trading
   - If long vega and IV increases → profit
   - If short vega and IV decreases → profit
   
2. **$\frac{1}{2}\Gamma(\delta S)^2$**: P&L from delta rebalancing
   - This is a SIDE EFFECT (like in delta hedging)
   - You're not trying to maximize this (unlike gamma scalping)
   - It's tracking error that you tolerate
   
3. **$-\theta\,\delta t$**: Time decay
   - For long vega (long options): you pay theta
   - For short vega (short options): you collect theta
   - This is the "carry" of your position

**Bottom line:** You profit when IV moves in your favor faster than theta erodes your position.

---

## Understanding the P&L: Betting on Volatility Expectations

$$\boxed{\delta \Pi \approx \underbrace{\text{Vega} \cdot \delta\sigma}_{\text{primary profit source}} + \underbrace{\frac{1}{2}\Gamma(\delta S)^2}_{\text{rebalancing side effect}} - \underbrace{\theta\,\delta t}_{\text{time decay}}}$$

### The Three Components

**$\text{Vega} \cdot \delta\sigma$:** Your main bet - profit from IV changes
- **Long vega (long options):** 
  - Vega > 0
  - You want IV to INCREASE
  - Betting: "Market is too complacent, volatility will spike"
  
- **Short vega (short options):**
  - Vega < 0  
  - You want IV to DECREASE
  - Betting: "Market is too fearful, volatility will calm down"

**$\frac{1}{2}\Gamma(\delta S)^2$:** Rebalancing P&L (not your focus)
- Comes from delta hedging rebalancing
- Not intentional profit (unlike gamma scalping)
- Just accept it as side effect
- Can be positive or negative depending on position

**$-\theta\,\delta t$:** The cost or benefit of holding
- Long options: pay theta (this is your cost)
- Short options: collect theta (this is your revenue)
- Trade-off with vega exposure

---

## Concrete Example: Long Vega Trade

**Setup: You think IV is too low**

**Market conditions:**
- Stock at $S = \$100$
- ATM call trading at implied volatility IV = 20%
- Call price: $V = \$5.00$
- Call delta: $\Delta = 0.5$
- Call vega: $\mathcal{V} = 0.25$ (per 1% IV change)
- Call theta: $\theta = -\$0.05$ per day

**Your view:**
- "IV of 20% is too low—I expect it to rise to 25%"

**Your trade:**
- Buy 100 call contracts (10,000 shares worth)
- Delta hedge: short $0.5 \times 10,000 = 5,000$ shares
- **Initial cost:** $(100 \times \$5 \times 100) - (5,000 \times \$100) = \$50,000 - \$500,000 = -\$450,000$

**Scenario 1: IV increases to 25% (you're right!)**

After 5 days:
- Stock still at $\$100$ (delta-hedged, so stock movement doesn't matter much)
- IV increases from 20% to 25% (5% increase)
- New call price: approximately $\$6.25$ (increased due to higher IV)

**Your P&L breakdown:**
- **Vega profit:** $100 \text{ contracts} \times \$0.25 \times 5\% = +\$1,250$
- **Theta loss:** $100 \text{ contracts} \times (-\$0.05) \times 5 \text{ days} = -\$250$
- **Gamma P&L:** Small (stock didn't move much, well-hedged) ≈ $0
- **Net P&L:** $+\$1,250 - \$250 = +\$1,000$

**You profited because IV moved in your favor!**

**Scenario 2: IV stays at 20% (you're wrong)**

After 5 days:
- Stock still at $\$100$
- IV unchanged at 20%
- Call price: approximately $\$4.75$ (decreased only due to theta)

**Your P&L breakdown:**
- **Vega profit:** $0$ (IV didn't change)
- **Theta loss:** $100 \times (-\$0.05) \times 5 = -\$250$
- **Gamma P&L:** ≈ $0$
- **Net P&L:** $-\$250$

**You lost money because IV didn't move and you paid theta!**

---

## Long Vega vs. Short Vega

**Understanding the two directions:**

### Long Vega (Buy Options)

**Position:** Long calls and/or long puts (delta-hedged)

**Characteristics:**
- Vega > 0 (benefit from IV increases)
- Theta < 0 (pay time decay every day)
- Gamma > 0 (delta-hedged long option)

**When you use it:**
- You believe IV is too LOW
- You expect IV to INCREASE
- Examples:
  - Before earnings (expect vol spike)
  - During calm markets (expect fear to return)
  - When VIX is historically low

**The bet:**
- "Market is too complacent"
- "Volatility will surprise to the upside"
- "Options are too cheap"

**Risk:** IV stays low or decreases → you pay theta and lose money

### Short Vega (Sell Options)

**Position:** Short calls and/or short puts (delta-hedged)

**Characteristics:**
- Vega < 0 (hurt by IV increases)
- Theta > 0 (collect time decay every day)
- Gamma < 0 (delta-hedged short option)

**When you use it:**
- You believe IV is too HIGH
- You expect IV to DECREASE
- Examples:
  - After earnings (vol crush)
  - During panic (expect calm to return)
  - When VIX is historically high

**The bet:**
- "Market is too fearful"
- "Volatility will calm down"
- "Options are too expensive"

**Risk:** IV stays high or increases → you lose on vega, though you collect theta

---

## Vega Trading vs. Gamma Scalping: Critical Comparison

**These are both volatility strategies, but fundamentally different:**

| Aspect | Vega Trading | Gamma Scalping |
|--------|-------------|----------------|
| **What you trade** | IMPLIED volatility changes | REALIZED volatility (actual movement) |
| **Primary profit source** | Vega · δσ (IV changes) | ½Γ(δS)² (rebalancing) |
| **How you profit** | IV moves toward your expectation | Stock bounces around (buy low/sell high) |
| **Delta hedging role** | Isolate vega exposure | Create rebalancing opportunities |
| **Rebalancing** | Not your goal (side effect) | Your primary profit source |
| **Theta** | Cost (long) or revenue (short) | Cost paid for gamma exposure |
| **View required** | "IV is wrong relative to true risk" | "Realized vol > implied vol" |
| **Time horizon** | Can be quick (days to weeks) | Needs time for vol to realize (weeks to months) |
| **Stock movement** | Don't need it! | NEED it (more is better) |
| **What you need to be right about** | Where IV will go | How much stock will actually move |

**Key insight:**
- **Gamma scalping:** "I don't care what the market EXPECTS—I know what will ACTUALLY happen (high realized vol)"
- **Vega trading:** "I know the market's EXPECTATION is wrong—IV is mispriced"

**Example to illustrate:**
- Stock at $100, IV = 30%
- **Vega trader thinks:** "30% IV is too high—it will drop to 20% when fear subsides" → short vega
- **Gamma scalper thinks:** "30% IV is perfect—stock will actually move 35%" → long gamma

They can both be right! Or both wrong! They're betting on different things.

---

## Can You Combine Them?

**YES! And this is common in practice:**

### Volatility Arbitrage (Vega + Gamma)

**The strategy:**
- Believe IV is too low (vega view)
- AND believe realized vol will be high (gamma view)
- **Trade:** Buy options (long vega + long gamma), delta hedge

**You profit from:**
- IV increasing (vega profit)
- Stock moving around (gamma profit)
- **This is the "full package" volatility trade**

**Risk:** You're paying theta twice, so you need BOTH views to be right

### Pure Vega (Vega Only)

**The strategy:**
- Have a view on IV changes only
- Don't care about realized vol
- **Trade:** Options position based on IV view, delta hedge
- Try to minimize gamma exposure (use shorter-dated options with lower gamma)

**Example:**
- Believe IV will drop after earnings → short options right before announcement
- Exit immediately after earnings (capture vol crush)
- Don't wait for realized vol to play out

---

## Why You Vega Trade

### Use Case 1: Volatility Is Mispriced

**Scenario:** Market is too fearful or too complacent

**Example (Long Vega):**
- VIX at 12 (historically very low)
- Market is complacent
- You believe volatility will spike
- **Trade:** Buy ATM straddles, delta hedge

**Example (Short Vega):**
- After a crash, VIX at 40
- Market is panicking
- You believe volatility will calm down
- **Trade:** Sell ATM straddles, delta hedge

### Use Case 2: Event-Based Vol Trading

**Scenario:** Earnings announcement in 2 days

**Pre-earnings (Long Vega):**
- IV typically rises before earnings
- Buy options 1 week before earnings
- Sell them 1 day before (capture IV rise)
- Don't hold through earnings

**Post-earnings (Short Vega):**
- "Vol crush" - IV drops after announcement
- Sell options right before earnings
- Buy them back after (capture IV drop)

### Use Case 3: Term Structure Arbitrage

**Scenario:** Front-month IV = 25%, back-month IV = 35%

**Your view:** "This term structure is wrong"

**Trade:**
- Sell back-month options (short high IV)
- Buy front-month options (long low IV)
- Delta hedge both
- Profit when term structure normalizes

### Use Case 4: Volatility Mean Reversion

**Scenario:** Volatility tends to revert to long-term average

**When IV > historical average:**
- Short vega (sell options)
- Bet on mean reversion downward

**When IV < historical average:**
- Long vega (buy options)
- Bet on mean reversion upward

---

## How Vega Trading Works

**Step-by-step process:**

### 1. Identify Mispriced IV

**Analysis methods:**
- Compare current IV to historical IV
- Compare IV to realized volatility
- Look at IV percentile (where IV ranks historically)
- Examine term structure (front vs. back month IV)
- Check volatility smile/skew

**Tools:**
- VIX index (market volatility expectation)
- Historical volatility charts
- IV rank and IV percentile
- Volatility surfaces

### 2. Establish Position

**If IV too low (Long Vega):**
- Buy ATM options (highest vega per dollar)
- Consider straddles or strangles
- Longer-dated options have more vega

**If IV too high (Short Vega):**
- Sell ATM options
- Consider iron condors (defined risk)
- Shorter-dated options have higher theta/vega ratio

### 3. Delta Hedge

**Immediately hedge directional risk:**
- Calculate position delta
- Trade underlying to neutralize
- This isolates your vega exposure

### 4. Manage the Position

**Monitor:**
- IV changes (your main exposure)
- Delta drift (rebalance as needed)
- Time decay (your cost or revenue)
- Gamma P&L (side effect)

**Rebalancing:**
- Rebalance delta periodically (don't over-optimize like gamma scalping)
- Focus on maintaining vega exposure, not harvesting gamma

### 5. Exit Strategy

**Exit when:**
- IV reaches your target
- Your thesis is invalidated
- Theta decay overwhelms expected IV movement
- Risk/reward no longer attractive

---

## Vega Trading vs. Delta Hedging vs. Gamma Scalping

**Let's see how all three relate:**

| Strategy | Primary Exposure | What You Want | Delta Hedging Role |
|----------|------------------|---------------|-------------------|
| **Delta Hedging** | None (hedged) | Stability (no movement) | The entire strategy |
| **Gamma Scalping** | Gamma (realized vol) | Stock to move a lot | Creates rebalancing profit |
| **Vega Trading** | Vega (implied vol) | IV to change | Isolates vega exposure |

**Position structure (all similar):**
- Delta hedging: Option + stock hedge (for risk management)
- Gamma scalping: Option + stock hedge (to harvest gamma)
- Vega trading: Option + stock hedge (to isolate vega)

**Same technique, three different purposes!**

### Visual Summary

```
Option + Delta Hedge
         ↓
   Three Strategies
         ↓
    ┌────┴─────────┐
    ↓         ↓         ↓
Delta     Gamma      Vega
Hedging   Scalping   Trading
    ↓         ↓         ↓
Avoid     Profit     Profit
directional from      from IV
risk      realized   changes
          vol
    ↓         ↓         ↓
"Stay     "Move      "IV is
 neutral"  around!"   mispriced!"
```

---

## Pros and Cons

### Advantages ✓

**1. Directionally neutral**
- Don't need to predict stock direction
- Only need view on volatility expectations
- Can profit in any market direction

**2. Can profit quickly**
- Don't need to wait for volatility to realize
- IV can change in hours or days
- Faster than gamma scalping (which needs time for vol to play out)

**3. Clear analytical framework**
- IV is observable and measurable
- Can compare to historical levels
- Can use statistical tools (percentiles, z-scores, mean reversion)

**4. Event-driven opportunities**
- Earnings announcements
- Fed meetings
- Political events
- Predictable IV patterns

**5. Volatility risk premium**
- Historical tendency: IV > realized vol
- Short vega strategies can harvest this premium
- Systematic edge over time

**6. Multiple strategies**
- Can go long or short vega
- Can trade term structure
- Can trade volatility smile/skew
- Many ways to express views

**7. Combines well with gamma scalping**
- Can profit from both IV changes AND realized vol
- Complementary strategies

### Disadvantages ✗

**1. Theta decay is relentless**
- Long vega: pay theta every day
- Need IV to move fast enough to overcome theta
- Time is your enemy (for long vega)

**2. IV can stay "wrong" for a long time**
- "The market can remain irrational longer than you can remain solvent"
- IV might be mispriced but not correct quickly
- Theta bleeds while you wait

**3. Two-way risk**
- Long vega: IV can drop, you pay theta
- Short vega: IV can spike, unlimited risk
- Need to be right on both direction AND timing

**4. Transaction costs**
- Must delta hedge (incurs costs)
- Rebalancing adds up
- Bid-ask spreads on options

**5. Gamma side effects**
- Still exposed to gamma P&L
- Can work for or against you
- Adds noise to pure vega bet

**6. Requires active management**
- Need to monitor IV constantly
- Delta rebalancing needed
- Position management
- Not passive

**7. Correlation with market stress**
- Long vega profits in crises (when you don't need money)
- Short vega loses in crises (when it hurts most)
- Timing is crucial

**8. IV can be manipulated**
- Market makers can widen spreads
- Thin markets → unreliable IV
- Earnings IV can be "pinned"

**9. Model risk**
- IV derived from models (Black-Scholes, etc.)
- Different models → different IV
- What is "fair" IV?

---

## When Vega Trading Works Best

**Favorable conditions:**

### For Long Vega

- **IV historically low** (VIX < 15, IV percentile < 20%)
- **Market complacency** (low fear, extended bull market)
- **Before known events** (earnings, Fed meetings)
- **Term structure inverted** (front > back, suggests stress)
- **Your catalyst:** Something that will increase fear/uncertainty

### For Short Vega

- **IV historically high** (VIX > 30, IV percentile > 80%)
- **Market panic** (after crashes, during crises)
- **After volatility spikes** (mean reversion opportunity)
- **Steep term structure** (front << back, suggests elevated fear)
- **Your catalyst:** Time for fear to subside

### General Favorable Conditions

- Liquid options markets (tight spreads)
- Stable delta (easier to hedge)
- Low transaction costs
- Your view differs from market consensus
- Statistical edge (IV mean reversion, term structure anomalies)

**Unfavorable conditions:**

- Illiquid options (wide spreads, difficult to execute)
- Events with unpredictable impact (binary events)
- Structural regime changes (IV might not revert)
- High transaction costs
- Extreme gamma (difficult to manage delta)
- Near expiration (high theta relative to vega)

---

## Vega Trading Strategies

**Common approaches:**

### 1. Straddle/Strangle

**Long Straddle (Long Vega):**
- Buy ATM call + ATM put
- Maximum vega per dollar
- Delta-neutral naturally
- Bet: IV will increase

**Short Straddle (Short Vega):**
- Sell ATM call + ATM put
- Collect theta, short vega
- Bet: IV will decrease

### 2. Calendar Spread (Time Vega)

**Setup:**
- Sell front-month option
- Buy back-month option
- Exploits term structure

**Vega profile:**
- Slightly long vega overall
- Profits if back-month IV rises relative to front
- Collects theta from front month

### 3. Volatility Arbitrage

**Setup:**
- Buy options when IV low
- Sell options when IV high
- Delta hedge both
- Profit from mean reversion

### 4. Dispersion Trading (Advanced)

**Setup:**
- Trade index vol vs. individual stock vol
- Exploits correlation structure
- Delta hedge all components

### 5. Event Trading

**Vol Spike Trading:**
- Buy options before events
- Sell before announcement
- Capture IV rise, avoid realized vol

**Vol Crush Trading:**
- Sell options before events
- Buy back after announcement
- Capture IV drop

---

## Position Sizing and Risk Management

**Key considerations:**

### Vega Exposure

**Rule of thumb:**
- Don't risk more than you can afford to lose on 5% IV move
- If vega = $1,000 per 1% IV, a 5% move = $5,000 P&L
- Size position so this fits your risk tolerance

### Theta Management

**For long vega:**
- Calculate daily theta bleed
- Ensure IV can realistically move enough to offset
- Time horizon: typically days to weeks, not months

### Delta Rebalancing

**Balance:**
- Rebalance enough to stay roughly delta-neutral
- Don't over-rebalance (costs money)
- Not trying to harvest gamma (that's a different strategy)

**Thresholds:**
- Rebalance when delta > 10-20% of position
- Or time-based (daily or twice daily)

### Exit Discipline

**Have clear rules:**
- Target IV level (take profit)
- Stop loss (IV moves against you)
- Time stop (if thesis not playing out)
- Theta limit (if decay becomes too much)

---

## What to Remember

### Core Concepts

- **Vega trading profits from IMPLIED volatility changes, not realized volatility**
- Your portfolio: Option + Delta hedge = Vega exposure (isolated)
- P&L formula: $\text{Vega} \cdot \delta\sigma + \frac{1}{2}\Gamma(\delta S)^2 - \theta\,\delta t$
- Primary profit source: Vega · δσ (the first term)
- Delta hedging role: isolates vega exposure (removes directional risk)

### Two Directions

- **Long vega (buy options):** 
  - Bet IV will INCREASE
  - Pay theta (your cost)
  - Want: market complacency to turn into fear
  
- **Short vega (sell options):**
  - Bet IV will DECREASE  
  - Collect theta (your revenue)
  - Want: market panic to calm down

### Key Distinctions

**Vega Trading vs. Gamma Scalping:**
- Vega: Trade IMPLIED vol changes (market expectations)
- Gamma: Trade REALIZED vol (actual movement)
- Vega: Don't need stock to move
- Gamma: NEED stock to move
- Can combine both strategies!

**Vega Trading vs. Delta Hedging:**
- Same technique (option + delta hedge)
- Different purpose (profit vs. risk management)
- Vega trader WANTS vega exposure
- Delta hedger tolerates vega exposure

### Success Factors

- **Be right about IV direction:** Will it rise or fall?
- **Be right about timing:** Will it happen fast enough to beat theta?
- **Statistical edge:** IV mean reversion, term structure anomalies, vol risk premium
- **Risk management:** Position sizing, stop losses, exit discipline
- **Lower transaction costs:** Rebalancing adds up

### Advanced Insight

**The fundamental bet in vega trading:**
- "The market's EXPECTATION of volatility (IV) is wrong"
- Not about what WILL happen (realized vol)
- About what market THINKS will happen (implied vol)
- You're trading psychology and expectations, not reality

This makes vega trading more of a "meta" bet—you're betting on how other market participants will re-price risk, not on actual risk itself.

### Practical Wisdom

- **IV tends to mean-revert** → systematic edge
- **IV > realized vol historically** → short vega bias can work
- **Events create IV spikes** → trade the pattern
- **Time is crucial:** Long vega needs fast IV moves to beat theta
- **Combine with gamma scalping** for full volatility exposure

**Final insight:** Vega trading is betting on the market's MIND (what it fears/expects), while gamma scalping is betting on the market's BODY (what it actually does). Both are powerful, both are different, and both can be combined!
