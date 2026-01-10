# Vega Trading

**Vega trading** is a strategy where you profit from changes in implied volatility by holding options positions while hedging away directional risk.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/vega_trading_by_maturity.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 1:** Vega Trading By Maturity visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/vega_trading_calendar_spread.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 2:** Vega Trading Calendar Spread visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/vega_trading_pnl_evolution.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 3:** Vega Trading Pnl Evolution visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/vega_trading_term_structure.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 4:** Vega Trading Term Structure visualization.

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

## The Two Types of

**This distinction is CRUCIAL:**

### 1. Realized

- **What it is:** How much the stock ACTUALLY moves

- **Measured by:** $\sigma_{\text{realized}} = \sqrt{\frac{252}{T}\sum (\text{daily returns})^2}$

- **Example:** Stock bounces between $90 and $110 → high realized volatility

- **Who trades it:** Gamma scalpers

### 2. Implied

- **What it is:** The market's EXPECTATION of future volatility, embedded in option prices

- **Derived from:** Option prices via Black-Scholes (solving for $\sigma$)

- **Example:** Options are expensive → market expects high volatility → high IV

- **Who trades it:** Vega traders

**The key insight:** These two can diverge!

- Market might expect 40% volatility (IV = 40%)

- But stock might actually realize only 25% volatility

- Or vice versa!

---

## Vega Trading

**Vega trading is NOT about realized volatility—it's about IMPLIED volatility changes!**

### 1. What Is Vega?

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


---

## Economic

**Understanding what this strategy REALLY represents economically:**

### 1. The Core Economic

This strategy involves specific economic trade-offs that determine when it's most valuable. The key is understanding what you're giving up versus what you're gaining in economic terms.

**Economic equivalence:**

$$
\text{Strategy P\&L} = \text{Greeks Exposure} + \text{Rebalancing} - \text{Costs}
$$

### 2. Why This

Markets create these strategies because different participants have different:

- Risk preferences (directional vs. convexity)

- Time horizons (short-term vs. long-term)

- Capital constraints (leverage limitations)

- View on volatility vs. direction

### 3. Professional

Institutional traders view this strategy as a tool for:

1. **Greeks arbitrage:** Extracting value from Greeks mispricing

2. **Risk transformation:** Converting one type of risk into another

3. **Capital efficiency:** Optimal use of buying power for Greeks exposure

4. **Market making:** Providing liquidity while managing Greeks

Understanding the economic foundations helps you recognize when the strategy offers genuine edge versus when market pricing is fair.


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

## Understanding the

$$\boxed{\delta \Pi \approx \underbrace{\text{Vega} \cdot \delta\sigma}_{\text{primary profit source}} + \underbrace{\frac{1}{2}\Gamma(\delta S)^2}_{\text{rebalancing side effect}} - \underbrace{\theta\,\delta t}_{\text{time decay}}}$$

### 1. The Three

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

## Concrete Example

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

## Long Vega vs. Short

**Understanding the two directions:**

### 1. Long Vega (Buy

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

### 2. Short Vega (Sell

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

## Vega Trading vs.

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

## Can You Combine

**YES! And this is common in practice:**

### 1. Volatility

**The strategy:**

- Believe IV is too low (vega view)

- AND believe realized vol will be high (gamma view)

- **Trade:** Buy options (long vega + long gamma), delta hedge

**You profit from:**

- IV increasing (vega profit)

- Stock moving around (gamma profit)

- **This is the "full package" volatility trade**

**Risk:** You're paying theta twice, so you need BOTH views to be right

### 2. Pure Vega (Vega

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

### 1. Market is too

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

### 2. Earnings

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

### 3. Front-month IV =

**Scenario:** Front-month IV = 25%, back-month IV = 35%

**Your view:** "This term structure is wrong"

**Trade:**

- Sell back-month options (short high IV)

- Buy front-month options (long low IV)

- Delta hedge both

- Profit when term structure normalizes

### 4. Volatility tends

**Scenario:** Volatility tends to revert to long-term average

**When IV > historical average:**

- Short vega (sell options)

- Bet on mean reversion downward

**When IV < historical average:**

- Long vega (buy options)

- Bet on mean reversion upward

---

## How Vega Trading

**Step-by-step process:**

### 1. Identify

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

### 2. Establish

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

### 4. Manage the

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

## Vega Trading vs.

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

### 1. Visual Summary

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

### 1. Advantages ✓

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

### 2. Disadvantages ✗

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

## When Vega Trading

**Favorable conditions:**

### 1. For Long Vega

- **IV historically low** (VIX < 15, IV percentile < 20%)

- **Market complacency** (low fear, extended bull market)

- **Before known events** (earnings, Fed meetings)

- **Term structure inverted** (front > back, suggests stress)

- **Your catalyst:** Something that will increase fear/uncertainty

### 2. For Short Vega

- **IV historically high** (VIX > 30, IV percentile > 80%)

- **Market panic** (after crashes, during crises)

- **After volatility spikes** (mean reversion opportunity)

- **Steep term structure** (front << back, suggests elevated fear)

- **Your catalyst:** Time for fear to subside

### 3. General Favorable

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

## Vega Trading

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

### 2. Calendar Spread

**Setup:**

- Sell front-month option

- Buy back-month option

- Exploits term structure

**Vega profile:**

- Slightly long vega overall

- Profits if back-month IV rises relative to front

- Collects theta from front month

### 3. Volatility

**Setup:**

- Buy options when IV low

- Sell options when IV high

- Delta hedge both

- Profit from mean reversion

### 4. Dispersion

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

## Position Sizing and

**Key considerations:**

### 1. Vega Exposure

**Rule of thumb:**

- Don't risk more than you can afford to lose on 5% IV move

- If vega = $1,000 per 1% IV, a 5% move = $5,000 P&L

- Size position so this fits your risk tolerance

### 2. Theta Management

**For long vega:**

- Calculate daily theta bleed

- Ensure IV can realistically move enough to offset

- Time horizon: typically days to weeks, not months

### 3. Delta Rebalancing

**Balance:**

- Rebalance enough to stay roughly delta-neutral

- Don't over-rebalance (costs money)

- Not trying to harvest gamma (that's a different strategy)

**Thresholds:**

- Rebalance when delta > 10-20% of position

- Or time-based (daily or twice daily)

### 4. Exit Discipline

**Have clear rules:**

- Target IV level (take profit)

- Stop loss (IV moves against you)

- Time stop (if thesis not playing out)

- Theta limit (if decay becomes too much)

---


---




## Practical Guidance

**Step-by-step implementation framework:**

### 1. Before entering,

**Before entering, evaluate:**

1. **Volatility environment:**

   - Current IV level and percentile

   - Implied vs. realized volatility spread

   - Term structure of volatility

2. **Greeks landscape:**

   - Which Greeks are mispriced

   - Expected Greeks P&L

   - Rebalancing frequency required

3. **Market conditions:**

   - Liquidity in options and underlying

   - Bid-ask spreads

   - Transaction cost environment

### 2. Enter this

**Enter this strategy when:**

- [Specific Greeks conditions]

- [Volatility requirements]

- [Liquidity sufficient for rebalancing]

- [Expected Greeks P&L > costs]

### 3. Enter LONG vega

**Enter LONG vega when:**

- **IV percentile < 40%** (room to rise)

- **Binary event coming** (earnings, FDA, FOMC) in 5-15 days

- **Historical pattern:** IV typically spikes before this event

- **Current IV < Historical pre-event IV** (underpriced)

- **Theta cost acceptable:** Daily theta < (Vega × 1 point)

**Example long vega entry:**

- AAPL 12 days before earnings

- Current IV: 28% (40th percentile)

- Historical pre-earnings IV: 40-45%

- Expected spike: 12-17 points

- Theta: -$60/day, Vega: +80 → Need 0.75 points/day

- **ENTER ✅**

---

**Enter SHORT vega when:**

- **IV percentile > 70%** (likely to fall)

- **Post-event** (after earnings, after FOMC)

- **No upcoming catalysts** (uncertainty removed)

- **IV elevated vs. realized vol** (overpriced)

- **Stock NOT unpredictable** (not TSLA, not biotech)

**Example short vega entry:**

- SPY day after FOMC

- Current IV: 24% (75th percentile)

- Historical post-FOMC: Drops to 16-18%

- Expected drop: 6-8 points

- **ENTER ✅**

---

**AVOID vega trading when:**

- **IV percentile 40-60%** (mid-range, no edge)

- **No clear event catalyst** (why would IV move?)

- **Unpredictable underlying** (TSLA, meme stocks - random IV spikes)

- **Low liquidity** (wide spreads eat profits)

- **Already moved** (IV already spiked, late to party)

- **Around major unknowns** (war, pandemic - black swans)

---


**Avoid this strategy when:**

- [Unfavorable Greeks environment]

- [High transaction costs]

- [Insufficient liquidity]

- [Wrong volatility regime]

### 4. Calculate maximum

**Calculate maximum position size:**

$$
\text{Max Size} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Greeks Loss}}
$$

**For Greeks strategies, consider:**

- Greeks exposure limits

- Rebalancing capacity

- Capital for hedge adjustments

- Margin requirements

### 5. Best practices: 1

**Best practices:**

1. **Greeks analysis:** Calculate all relevant Greeks before entry

2. **Liquidity check:** Ensure sufficient volume for rebalancing

3. **Spread analysis:** Check bid-ask spreads on all legs

4. **Hedge execution:** Enter hedges simultaneously with options

**Rebalancing framework:**

- Delta rebalance when: |Δ| > threshold

- Vega adjustment when: IV moves X%

- Gamma management when: Position size changes

- Transaction cost consideration: Balance frequency vs. cost

### 6. Active management

**Active management rules:**

**Greeks monitoring:**

- Track delta daily (minimum)

- Monitor gamma exposure

- Watch vega for IV changes

- Calculate P&L attribution by Greek

**Rebalancing triggers:**

- Delta: Rebalance when exceeds threshold

- Vega: Adjust on IV regime changes

- Gamma: Scale position with proximity to strikes

- Theta: Monitor daily decay

**Profit/loss targets:**

- Take profit at: [Greeks P&L target]

- Cut losses at: [Max acceptable Greeks loss]

- Time-based exit: [Time decay considerations]

### 7. Greeks risk

**Greeks risk limits:**

- Max delta exposure: [Limit]

- Max gamma concentration: [Limit]

- Max vega exposure: [Limit]

- Theta bleed tolerance: [Limit]

**Portfolio-level controls:**

- Correlation of Greeks across positions

- Aggregate exposure monitoring

- Stress testing for market moves

- Worst-case scenario planning

### 8. Track for every

**Track for every trade:**

- Entry Greeks (delta, gamma, vega, theta)

- Rebalancing frequency and costs

- P&L by Greek component

- Actual vs. expected volatility

- Transaction costs vs. Greeks P&L

- Lessons learned

### 9. Common Execution

1. **Ignoring transaction costs** - Frequent rebalancing eats profits

2. **Wrong rebalancing frequency** - Too often or too infrequent

3. **Insufficient liquidity** - Cannot execute rebalances efficiently

4. **Over-leveraging Greeks** - Excessive exposure to single Greek

5. **Neglecting other Greeks** - Focus on one Greek, ignore others

6. **Poor hedge timing** - Waiting too long or reacting too quickly

### 10. Professional

**For delta hedging:**

- Use delta bands (don't chase every move)

- Consider transaction costs

- Rebalance at consistent intervals

**For gamma scalping:**

- Need sufficient realized vol

- Monitor gamma P&L vs. theta cost

- Scale position size with gamma exposure

**For vega trading:**

- Understand vol term structure

- Watch for regime changes

- Consider vega cross-effects (vanna, volga)


## Common Mistakes

**Critical errors that destroy vega trading profits:**

### 1. The error: "I'll

**The error:**
"I'll buy a straddle and make money from volatility!"

**Trader thinks:**

- Vega trading = Gamma scalping

- "I'll profit from stock movement AND IV changes"

- Enters long straddle expecting both

**Reality:**

**Vega trading:** Bet on **IV changes** (market's volatility expectations)

**Gamma scalping:** Bet on **realized vol** (actual stock movement)

**Example:**

- Buy AAPL straddle @ IV 30%

- Stock chops around (realized vol 25%) → Gamma scalping LOSES (theta > gamma profits)

- But IV spikes to 40% → **Vega trading WINS** (+$800 vega profit)

**They're DIFFERENT bets:**

- Vega: Will IV change?

- Gamma: Will stock move enough?

**The fix:**

**Know what you're trading:**

- If betting on IV changes → Delta hedge perfectly, ignore stock moves

- If betting on realized vol → Let IV be (accept vega risk)

- **Don't try both** (conflicting goals)

---

### 2. The error: "IV is

**The error:**
"IV is at 65%! So much premium! I'll buy straddles and profit from volatility!"

**Example:**

- Stock IV: 60% (75th percentile - VERY high)

- Trader: "Volatility is high, perfect for vega trading!"

- Buys straddle

**Week 1-2:**

- IV mean-reverts: 60% → 50%

- **Vega loss: -$1,000**

- Stock doesn't move much

- Theta bleeding: -$600

- **Total: -$1,600** (-25% in 2 weeks)

**Why it's wrong:**

**High IV percentile = Likely to FALL** (mean reversion)

**Historical analysis:**

- IV at 70th+ percentile → 65% chance drops next 30 days

- IV at 30th- percentile → 65% chance rises next 30 days

**The fix:**

**Check IV percentile BEFORE entering:**

**For LONG vega:**

- Only enter: IV < 40th percentile

- Sweet spot: 20th-30th percentile

- Reason: Room to rise

**For SHORT vega:**

- Only enter: IV > 70th percentile  

- Sweet spot: 75th-85th percentile

- Reason: Likely to fall

**Tool:**
$$
\text{IV Percentile} = \frac{\text{Current IV} - \text{52-week Low IV}}{\text{52-week High IV} - \text{52-week Low IV}} \times 100\%
$$

---

### 3. The error: "IV

**The error:**
"IV will spike 10 points. Vega is 100. I'll make $1,000!"

**Example:**

- Position: Vega +100, Theta -$80/day

- Expected: 10-point IV spike in 20 days

- Trader: "10 × 100 = $1,000 profit!"

**Reality:**

- Days 1-19: IV slowly rising

- Theta cost: 19 × -$80 = -$1,520

- Day 20: IV finally spikes 10 points

- Vega profit: +$1,000

- **Net: -$520** (LOSS!)

**Why it's wrong:**

**Forgot theta was eating profits while waiting!**

**The fix:**

**Calculate theta-adjusted breakeven:**

$$
\text{IV Points Needed} = \frac{\text{Days Held} \times \text{Daily Theta}}{\text{Vega}}
$$

**Example:**

- Hold 20 days

- Theta: -$80/day

- Vega: +100

$$
\text{Need:} \frac{20 \times 80}{100} = 16 \text{ points!}
$$

Not 10 points - need 16 points to overcome theta!

**Rule:** For long vega, need IV to move FAST. Slow moves = theta wins.

---

### 4. The error:

**The error:**
"Earnings in 45 days. IV will spike. I'll enter now!"

**Example:**

- Stock earnings: 45 days away

- Current IV: 30%

- Historical: IV spikes to 45% in last 5 days before earnings

- Trader enters: 45 days early

**Reality:**

- Days 1-35: IV barely moves (30% → 32%)

- Theta cost: 35 × -$50 = -$1,750

- Days 36-45: IV spikes 30% → 45%

- Vega profit: +$1,500

- **Net: -$250** (theta ate the gains!)

**Why it's wrong:**

**IV spike happens LAST WEEK, not early!**

**Historical pattern (pre-earnings):**

- 30+ days out: IV flat

- 14-21 days: IV slowly rises

- 7 days: IV accelerates

- 1-3 days: **IV SPIKES** (most movement here!)

- After earnings: **IV CRUSHES** (massive drop)

**The fix:**

**Timing rules:**

**For long vega (pre-event):**

- **Too early:** >20 days before event (theta kills you)

- **Sweet spot:** 7-14 days before event

- **Optimal:** 10 days before event

- **Too late:** <3 days (already spiked)

**For short vega (post-event):**

- **Optimal:** Day after event (IV crush maximum)

- **Still OK:** 2-3 days after

- **Too late:** 1 week+ after (already dropped)

---

### 5. The error: "I'm

**The error:**
"I'm vega trading. Stock direction doesn't matter!"

**Example:**

- Trader: Long vega (bought straddle)

- Doesn't delta hedge

- IV spikes 10 points: **+$1,000 vega profit** ✅

- BUT: Stock gaps down $10 overnight

- Delta exposure (unhedged): **-$1,500 loss**

- **Net: -$500** (despite being RIGHT on vega!)

**Why it's wrong:**

**Vega trading is about IV, not stock moves:**

- Want: Pure IV exposure

- Don't want: Delta exposure contaminating P&L

**Without delta hedge:**

- Stock moves create noise

- Can't isolate vega P&L

- "Right" vega bet can still lose!

**The fix:**

**Delta hedge religiously:**

**For long straddle (vega +100):**

- Initial delta: ~0

- Stock moves $5 up → Delta now +0.40

- **Hedge:** Short 40 shares

- Rebalance when |Delta| > 0.20

**Daily routine:**

1. Check delta

2. Calculate hedge: Shares needed = -Delta × 100

3. Execute hedge

4. Record cost

**Cost:** $20-50/day in commissions  

**Benefit:** Pure vega P&L (worth it!)

---

### 6. The error: "IV

**The error:**
"IV will spike AT earnings. I'll hold through for maximum profit!"

**Example - Pre-earnings:**

- Day before earnings: IV 45%, straddle worth $30

- Profit so far: +$800

- Trader: "If I hold through earnings, IV might go even higher!"

**Earnings night:**

- AAPL reports (beat expectations)

- Stock gaps $5 up

**Next morning:**

- **IV crushes: 45% → 22%** (-23 points!)

- Straddle now: $15

- **Loss: -$1,500** (from +$800 to -$700!)

**Why it's DEADLY:**

**Post-event IV crush is BRUTAL:**

- Pre-event: IV 40-60% (elevated)

- Post-event: IV 15-25% (normalizes)

- Typical drop: 20-30 points IN ONE DAY!

**Vega losses:**

- 20-point drop × vega 100 = **-$2,000**

- Overwhelms any stock movement gains!

**The fix:**

**For long vega:**

- **Exit 1 day BEFORE event**

- Lock in IV spike profits

- Avoid IV crush

**For short vega:**

- **Enter 1 day AFTER event**

- Capture IV crush

- Avoid surprise spikes

**NEVER hold through the event itself!**

---

### 7. The error: "TSLA

**The error:**
"TSLA IV is at 70%. I'll sell straddles and collect as it drops to 50%."

**Example:**

- TSLA IV: 70% → Short vega -200

- Week 1: IV drops 70% → 65% (**+$1,000 profit**)

- Trader: "Easy money!"

**Week 2, Tuesday:**

- **Elon tweets:** "Major announcement Thursday"

- **IV SPIKES: 65% → 90%** (+25 points!)

- Vega loss: -200 × 25 = **-$5,000**

- From +$1,000 to -$4,000 in ONE DAY

**Why it's wrong:**

**Unpredictable stocks = Random IV spikes:**

**TSLA:**

- Elon can tweet anytime

- Surprise announcements

- Unpredictable

**Biotech:**

- FDA decisions

- Trial results

- Binary events

**Meme stocks:**

- Reddit can pump anytime

- Short squeeze risk

- Unpredictable

**The fix:**

**Never short vega on:**

- ❌ TSLA (Elon tweets)

- ❌ Any biotech (FDA binary)

- ❌ Meme stocks (GME, AMC)

- ❌ Small caps (low liquidity)

- ❌ Stocks with pending news

**Only short vega on:**

- ✅ SPY, QQQ (indices - predictable)

- ✅ AAPL, MSFT post-earnings (uncertainty gone)

- ✅ Large stable stocks (JNJ, KO, PG)

**Rule:** If you can't predict when IV might spike, don't short vega!

---

### 8. The error: "Vega

**The error:**
"Vega trading is 'low risk' since I'm hedged. I'll use 30% of my account!"

**Example:**

- Account: $50,000

- Position: Vega +500 (30% of capital)

- "I'm delta-hedged, what could go wrong?"

**Reality:**

- IV drops 10 points in one week

- **Vega loss: 500 × -10 = -$5,000** (-10% of account!)

- Plus theta: -$1,400

- **Total: -$6,400** (-12.8% of account)

- Psychological pressure: Exits at bottom

**Why it's wrong:**

**Vega can move 10-20 points in DAYS:**

- One week: -10 points common

- Black swan: -30 points possible

- With vega +500: **-$15,000 loss!** (30% of account)

**The fix:**

**Position sizing for vega:**

$$
\text{Max Vega} = \frac{\text{Account} \times 2\%}{10 \text{ points}}
$$

**Example:**

- $50,000 account

- Max risk: $1,000 (2%)

- **Max vega:** $1,000 / 10 = **100 vega**

Not 500 vega!

**Conservative limits:**

- Single trade: Vega < 100

- Total portfolio: Vega < 300

- Max 3 vega trades simultaneously

---

### 9. The error: "IV

**The error:**
"IV just spiked from 20% to 40%! It's going higher! I'll buy now!"

**Example:**

- Monday: IV 20%

- Tuesday: News hits, IV spikes to 40%

- Trader sees: "Volatility exploding! Buy straddle!"

- Buys Wednesday: IV 40%

**Reality:**

- Wednesday-Friday: IV peaks at 42%, then drops back to 30%

- **Vega loss:** -10 points × vega = -$1,000

- Theta: -$300

- **Total: -$1,300** (entered too late!)

**Why it's wrong:**

**IV spike already happened!**

**Typical pattern:**

- Day 1: News → IV spikes 20 points

- Day 2-3: IV stays elevated

- Day 4-7: **IV mean-reverts down**

**By entering on Day 2:**

- Missed: 20-point spike

- Caught: 10-point drop (LOSS!)

**The fix:**

**For long vega:**

- Enter BEFORE the spike (7-14 days before event)

- Exit DURING the spike (1 day before event)

- Never chase after it's moved!

**If you missed it:**

- Wait for next opportunity

- Don't chase

- FOMO kills vega traders

---

### 10. The error: "I

**The error:**
"I entered long vega, I'll check it next week."

**Example:**

- Day 1: Enter long vega (IV 30%)

- Days 2-5: Doesn't check

- Day 6: Checks position

- IV now: 25% (-5 points)

- **Loss: -$500** (could have exited Day 2 at -$100!)

**Why it's wrong:**

**IV can move FAST:**

- Day 1: Perfect

- Day 2: Still OK (+1 point)

- Day 3: **Drops -3 points** (should exit!)

- Day 4-6: Continues dropping

- By the time you check: Too late!

**The fix:**

**Daily IV tracking (non-negotiable):**

**Every morning:**

1. Check current IV

2. Compare to entry IV

3. Calculate P&L: (Current IV - Entry IV) × Vega

4. Check theta cost

5. Decide: Hold, exit, or adjust

**Spreadsheet:**

| Date | IV | ΔIV | Vega P&L | Theta | Net | Action |
|------|----|----|----------|-------|-----|---------|
| Day 1 | 30% | 0 | $0 | $0 | $0 | Entry |
| Day 2 | 31% | +1 | +$100 | -$60 | +$40 | Hold |
| Day 3 | 29% | -1 | -$100 | -$120 | -$220 | **Exit?** |

**Exit trigger:**

- IV moves -5 points against position → **EXIT**

- Don't wait for it to get worse!

---

### 11. | | Mistake |

| # | Mistake | Fix |
|---|---------|-----|
| 1 | Confusing with gamma scalping | Know the difference - pure IV bet |
| 2 | Entering at high IV percentile | Long vega <40th, short vega >70th |
| 3 | Ignoring theta cost | Calculate theta-adjusted breakeven |
| 4 | Wrong timing (too early) | 7-14 days before event, not 30+ |
| 5 | Not delta hedging | Hedge daily, isolate vega P&L |
| 6 | Holding through event | Exit 1 day before (long) or enter after (short) |
| 7 | Shorting vega on TSLA, biotech | Only short predictable stocks |
| 8 | Over-sizing | Max vega = Account × 2% / 10 points |
| 9 | Chasing IV after spike | Enter before spike, not after |
| 10 | Not tracking IV daily | Daily checks non-negotiable |

**Remember:** Vega trading is precise. One mistake = 30-50% loss. Follow the rules or don't play!

---

## Real-World Examples

**Concrete scenarios showing vega trading in practice:**

### 1. Pension Duration

**Setup:**

- Date: October 15

- Stock: AAPL $175

- Earnings: October 26 (11 days away)

- Current IV: 28% (45th percentile - normal)

- Pattern: AAPL typically spikes to 40-45% pre-earnings

**Trade:**

- Buy 2× $175 straddles @ $14 = $2,800

- Vega: +80

- Theta: -$60/day

**Day-by-day:**

**Day 1-3:** IV 28% → 29%, P&L -$100 (theta winning)  

**Day 4-6:** IV 29% → 33%, P&L +$140 (vega winning!)  

**Day 7-9:** IV 33% → 41%, P&L +$445 (acceleration!)  

**Day 10:** IV 41% → 43%, Exit at +$1,420

**Result:**

- Entry: $2,800

- Exit: $4,220

- **Profit: +$1,420 (50.7% in 10 days)**

**Why it worked:**
✅ Low IV entry (45th percentile)  
✅ Historical pattern held  
✅ Perfect timing (11 days before)  
✅ Exited 1 day before earnings (avoided IV crush)

**Next day (earnings):**

- IV crushed 43% → 22%

- If held: Profit would've been only +$340 (not $1,420)

- **Smart exit saved $1,080!**

---

### 2. Transition Risk

**Setup:**

- NFLX $450, earnings in 30 days

- Current IV: 55% (68th percentile - elevated!)

- Trader: "IV will spike to 65%+, I'll buy now"

**Trade:**

- Buy 5× $450 straddles @ $35 = $17,500

- Vega: +250

- Theta: -$350/day

**Week 1:**

- IV: 55% → 56%

- Vega: +$250

- Theta: -$1,750

- **Net: -$1,500** (-8.6%)

**Week 2:**

- **Surprise:** NFLX announces major content deal

- **IV DROPS: 56% → 52%** (uncertainty reduced!)

- Vega loss: -$1,000

- **Week P&L: -$3,250**

**Week 3:**

- More good news: Subscriber numbers strong

- **IV continues falling: 52% → 47%**

- Vega: -$750

- Theta: -$1,050

- **Week P&L: -$1,800**

**Week 3 Thursday:**

- NFLX pre-announces subscriber beat!

- **IV collapses: 47% → 40%** (-7 in one day!)

- Vega loss: -$1,750

- **From start: -$10,450** (-59.7%!)

**Exit Day 21:**

- Final loss: **-$10,450**

- Account: -13.9%

**What went wrong:**
❌ Entered at HIGH IV (68th percentile) - mean reversion down!  
❌ Too early (30 days vs. optimal 10 days)  
❌ Oversized (23% of account)  
❌ No stop loss  
❌ Didn't understand: High IV → Falls!

---

### 3. Portable Alpha

**Setup:**

- Date: FOMC decision day

- SPY: $450

- IV spiked pre-FOMC: 24% (75th percentile)

- Fed announces: No surprise (rate hold as expected)

**Trade (Day after FOMC):**

- Short 3× $450 straddles @ $18 = $5,400 credit collected

- Vega: -150

- Theta: +$120/day (collecting theta!)

**Week 1:**

- IV: 24% → 20% (-4 points, IV crush!)

- Vega profit: 150 × 4 = **+$600**

- Theta profit: +$840

- **Net: +$1,440** (26.7% in 1 week!)

**Week 2:**

- IV: 20% → 18%

- Vega: +$300

- Theta: +$840

- **Net: +$1,140**

**Exit Day 12:**

- Total profit: +$2,580

- Close position (buy back at $23.40)

- **ROI: 47.8% in 12 days**

**Why it worked:**
✅ Entered at HIGH IV (75th percentile)  
✅ Post-event (uncertainty gone)  
✅ Predictable underlying (SPY not TSLA)  
✅ IV crushed as expected  
✅ Exited early (didn't wait for full decay)

---

### 4. Tactical Duration

**Setup:**

- TSLA: $240

- IV: 70% (78th percentile - very high)

- Trader: "IV too high, will drop to 50%. Short vega!"

**Trade:**

- Short 4× $240 straddles @ $40 = $16,000 credit

- Vega: -200

- Account: $75,000

**Week 1:**

- IV: 70% → 65%

- **Vega profit: +$1,000**

- Theta: +$800

- **Net: +$1,800** (11.3%)

Trader: "Easy money! IV falling as expected!"

**Week 2, Tuesday morning:**

- **Elon tweets:** "Major announcement Thursday"

- **IV SPIKES: 65% → 90%** (+25 points in minutes!)

- **Vega loss: 200 × -25 = -$5,000**

**Wednesday:**

- Speculation continues

- IV: 90% → 95%

- **Additional vega loss: -$1,000**

**Thursday (announcement):**

- Elon announces: Stock split + new product

- TSLA rallies $15

- IV continues high: 95%

- **Total position loss: -$8,500**

**Forced exit Friday:**

- Buy back straddles @ $58

- **Final loss: -$7,200**

- Account: -9.6%

**What went wrong:**
❌ Shorted vega on UNPREDICTABLE stock (TSLA)  
❌ Elon can tweet anytime (random IV spikes)  
❌ No stop loss  
❌ Didn't exit when IV spiked 5 points

**Lesson:** Never short vega on TSLA, biotech, or meme stocks!

---

### 5. Duration Hedge

**Setup:**

- Date: Late February 2020

- VIX: 15 (calm market)

- SPY: $340

- Whispers: Virus spreading in Italy

**Trade (lucky timing):**

- Buy 10× SPY $340 straddles @ $12 = $12,000

- Vega: +500

- Trader: "If virus spreads, volatility will explode"

**Week 1 (Feb 24-28):**

- COVID panic begins!

- **VIX: 15 → 25** (+10 points)

- **SPY IV: 18% → 35%** (+17 points!)

- Vega profit: 500 × 17 = **+$8,500**

- **Position value: $12,000 → $30,500**

**Week 2 (March 2-6):**

- **Full panic:** WHO declares pandemic

- **VIX: 25 → 40** (+15 more!)

- **SPY IV: 35% → 60%** (+25 more!)

- Vega profit: 500 × 25 = **+$12,500** more

- **Position value: $30,500 → $55,000**

**Week 3 (March 9 - VIX peak):**

- **VIX hits 80!**

- **SPY IV: 60% → 85%** (+25 more!)

- **Position value: $55,000 → $95,000**

**Exit (wise move):**

- Trader exits at $95,000

**Result:**

- Entry: $12,000

- Exit: $95,000

- **Profit: +$83,000 (+692%!)**

- **In 3 weeks!**

**Why this was incredible:**
✅ Black swan timing (lucky)  
✅ Long vega BEFORE spike  
✅ Massive IV explosion (18% → 85%)  
✅ Exited near peak (didn't hold for 100%)

**Note:** This is RARE (1-2 times per decade). Don't expect this!

**Others who held:**

- VIX dropped 80 → 40 over next 2 weeks

- Gave back 50% of gains!

---

### 6. Setup: Retail

**Setup:**

- Retail trader using Robinhood

- Trade: Long vega on AMZN pre-earnings

**Trade:**

- Buy 3× AMZN $140 straddles @ $12 = $3,600

- Vega: +150

**The problem: Poor delta hedging execution**

**Day 1:**

- Delta: 0.30, need to sell 90 shares AMZN

- Uses MARKET order

- AMZN at $140.00, fills at $139.75

- **Slippage: $22.50**

**Day 3:**

- Delta: -0.25, need to buy 75 shares

- Market order: AMZN at $142, fills at $142.30

- **Slippage: $22.50**

**Day 5:**

- Delta: 0.35, need to sell 105 shares

- Market order: Slippage $30

**Week 1 totals:**

- Delta rebalances: 8 times

- Total slippage: **$180**

- Vega profit: $240

- Theta cost: -$300

- **Net: -$240** (slippage + theta killed it!)

**If using LIMIT orders:**

- Slippage: $40 (vs $180)

- **Net P&L: +$100** (profitable!)

**Lesson:** Execution matters! Use limit orders, not market orders.

---

### 7. Setup: Trader:

**Setup:**

- Trader: More sophisticated

- Strategy: Calendar spread (long vega structure)

- Stock: GOOGL $140, earnings in 2 weeks

**Trade:**

- Buy 5× GOOGL $140 calls (30 DTE) @ $8 = $4,000

- Sell 5× GOOGL $140 calls (14 DTE) @ $5 = $2,500 credit

- **Net debit: $1,500**

- **Net vega: +60** (back month more vega than front)

**Week 1:**

- IV: 30% → 35% (approaching earnings)

- Back month gains more than front month

- Position: $1,500 → $2,100 (+$600)

**Week 2 (day before earnings):**

- IV: 35% → 42%

- Front month expires (at $140, worthless if ATM)

- Back month: $8 → $13

- **Exit back month at $13**

**Result:**

- Entry: $1,500 net

- Front month: Expires worthless (as planned)

- Back month exit: 5 × $13 = $6,500

- **Profit: $6,500 - $1,500 = +$5,000** (+333%!)

**Why this worked:**

- Calendar spreads = pure vega play

- Theta on back month less than front (back month gains)

- Front month expires, left with pure long vega

- Perfect for pre-event IV spike

**Advanced but profitable!**

---

### 8. Winners share:

**Winners share:**

- Entered at low IV percentile (<40th) for long vega

- Perfect timing (7-14 days before event)

- Exited before event (avoided IV crush)

- Proper sizing (2-3% of account)

- Delta hedged correctly

- Tracked IV daily

**Losers share:**

- Entered at high IV (>60th) expecting more spike

- Wrong timing (too early = theta killed)

- Held through event (IV crush destroyed)

- Oversized positions

- Ignored IV daily moves

- Shorted vega on unpredictable stocks

**The pattern:**
$$
\text{Success} = \text{Right IV Direction} + \text{Perfect Timing} + \text{Discipline}
$$

Miss any one → Disaster!

---

## Real-World Examples

[Concrete examples]

