# Gamma Scalping


**Gamma scalping** is a trading strategy that systematically profits by **buying low and selling high** through frequent rebalancing of a hedged option position.


- Own an option + hedge with stock
- When the stock moves, your hedge becomes unbalanced
- Rebalance by trading in the opposite direction
- This forces you to buy after drops and sell after rises
- Repeat this many times to accumulate profits

**You're essentially converting stock volatility into systematic "buy low, sell high" trades.**

---

## The Basic Idea


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/gamma_scalping_mechanism.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 1:** Gamma scalping mechanism illustrating how rebalancing a delta-hedged position forces systematic buying low and selling high, converting gamma exposure into realized P&L through dynamic trading.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/gamma_scalping_pnl_components.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 2:** P&L component breakdown showing the interplay between gamma scalping profits (positive convexity), theta decay (time cost), and transaction costs, demonstrating the conditions required for profitable gamma scalping.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/gamma_scalping_profile.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 3:** Profit profile of a gamma scalping strategy showing cumulative P&L over time under different realized volatility scenarios, illustrating how profitability depends on realized vol exceeding implied vol.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/gamma_scalping_realized_vs_implied.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 4:** Realized versus implied volatility comparison showing the critical relationship that determines gamma scalping profitability, with breakeven volatility levels and optimal entry/exit zones marked.

---

## The Core Insight


**The fundamental idea is simple:**

**What you do:**

1. Buy an option (typically at-the-money)
2. Hedge by shorting $\Delta$ shares of the underlying stock (making your portfolio "delta-neutral")
3. As the stock moves, your hedge becomes unbalanced
4. Rebalance frequently by buying low and selling high
5. Profit from these rebalancing trades

**The goal:** Make money from actual stock price movement (called *realized volatility*) that exceeds what you paid for the option (based on *implied volatility*).

---

## The Portfolio


Your gamma scalping portfolio consists of:

$$
\Pi = \text{Long Option} + \text{Delta Hedge (short stock)}
$$

More precisely:
$$
\Pi = V(S, t) - \Delta \cdot S
$$

where $V(S,t)$ is the option value and you short $\Delta$ shares.

**Why this structure?**

- The delta hedge neutralizes first-order price risk (you're not betting on direction)
- What remains is exposure to second-order effects—the curvature captured by gamma
- You profit from repeatedly rebalancing this hedge as prices move

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


Over a short time interval $\delta t$ with stock price move $\delta S$, your portfolio P&L is:

$$
\delta \Pi \approx \frac{1}{2}\Gamma(\delta S)^2 - \theta\,\delta t
$$

**What this means:**

1. **$\frac{1}{2}\Gamma(\delta S)^2$**: Your profit from the stock movement

      - $\Gamma$ (gamma) measures how fast your hedge becomes unbalanced
      - $(\delta S)^2$ means bigger price swings create more profit (regardless of direction!)
  
2. **$\theta\,\delta t$**: Your loss from time decay

      - $\theta$ (theta) is how much the option loses in value per day
      - $\delta t$ is the time that passes

**Bottom line:** You profit when the "gamma gains" from stock movement exceed the "theta cost" of holding the option (plus trading costs).

---

## Understanding the


$$\boxed{\delta \Pi = \underbrace{\frac{1}{2}\Gamma(\delta S)^2}_{\text{buy low, sell high profits}} - \underbrace{\theta\,\delta t}_{\text{option time decay}}}$$

### 1. The Two


**$-\theta\,\delta t$:** Loss from time decay of the option

- This is the "rent" you pay for holding the option position
- Every day that passes, the option loses value (all else equal)
- This is purely a function of time—you lose this even if the stock doesn't move
- This is a **passive loss**

**$\frac{1}{2}\Gamma(\delta S)^2$:** Gain from buying low and selling high

- This is the profit you realize by **actively rebalancing** your delta hedge
- Each rebalancing forces you to trade against the move (buy low, sell high)
- The $(\delta S)^2$ term shows that bigger moves create more profit
- This is an **active gain** from trading

### 2. How "Buy Low,


**The mechanism:**

1. Stock moves (say, drops)
2. Your delta changes due to gamma
3. To maintain your hedge, you must reduce your short position
4. **This means buying stock after it dropped** (buying low!)
5. Stock moves back up
6. Your delta changes again
7. To maintain your hedge, you must increase your short position
8. **This means selling stock after it rose** (selling high!)

**You're not trying to time the market—the rebalancing rules force you to buy low and sell high!**

### 3. Concrete Example


**Setup:**

- You own **1 call option contract** (in the US, 1 contract controls 100 shares)
- Stock price: $S = \$100$
- Option delta: $\Delta = 0.5$
- Option gamma: $\Gamma = 0.05$ (for illustration)
- **Your hedge:** Short $0.5 \times 100 = 50$ shares

**Scenario: Stock fluctuates**

**Step 1: Stock drops to $\$98$**

- Your option loses value, but your short 50 shares gains: $50 \times \$2 = \$100$
- Due to gamma, delta changed from $0.5$ to $0.45$
- New hedge needed: $0.45 \times 100 = 45$ shares
- **Action:** Buy back (cover) 5 shares at $\$98$ ← **Buying low!**

**Step 2: Stock bounces back to $\$100$**

- Delta changes from $0.45$ back to $0.5$
- New hedge needed: $0.5 \times 100 = 50$ shares
- **Action:** Short 5 additional shares at $\$100$ ← **Selling high!**

**Your rebalancing profit:**

- Bought 5 shares at $\$98$
- Sold 5 shares at $\$100$
- Profit: $5 \times (\$100 - \$98) = \$10$

**This is gamma scalping in action!** The more the stock bounces around, the more "buy low, sell high" opportunities you get.

### 4. The Trade-off


Think of it as:

- **Revenue:** "Buy low, sell high" profits from volatility = $\frac{1}{2}\Gamma(\delta S)^2$
- **Cost:** Time decay from holding the option = $\theta\,\delta t$
- **Net profit:** Revenue - Cost - Transaction costs

You win when volatility is high enough that your "buy low, sell high" profits exceed your time decay costs and transaction costs.

---

## The Sign of Gamma


**Important:** Gamma's sign depends on your position:

**Long options** (when you buy):

- Long call: $\Gamma > 0$
- Long put: $\Gamma > 0$

**Short options** (when you sell):

- Short call: $\Gamma < 0$
- Short put: $\Gamma < 0$

**For gamma scalping:**

- We specifically use **long options** where $\Gamma > 0$
- This means stock movement helps us: $\frac{1}{2}\Gamma(\delta S)^2 > 0$
- We get to buy low and sell high
- But we pay for this with time decay ($\theta < 0$ for long options)

**If you were short gamma:**

- Stock movement would hurt you (gamma term becomes negative)
- You'd be forced to buy high and sell low (the opposite!)
- But you'd collect time decay instead
- This is the opposite strategy—betting on low volatility

---

## Why You Need the


**Natural question:** "If the profit comes from buying low and selling high, why do I need the option? Can't I just trade the stock directly?"

**The answer:** Yes, the profit comes from "buy low, sell high"—but the option provides something invaluable that makes this strategy actually work.

---

### 1. The Problem


**If you just trade stock directly:**

**Critical questions arise:**

- When do you buy? When do you sell? How much?
- You need to **predict** when the stock has dropped enough to buy
- You need to **predict** when the stock has risen enough to sell  
- You need **timing skill** and **market prediction**
- You're exposed to **directional risk** (what if the stock keeps falling after you buy?)

**This is very difficult!** Most traders fail at timing the market consistently.

---

### 2. The Option's Role


**The option (via gamma) provides an automatic, mathematical rule that tells you exactly when and how much to trade—no prediction needed.**

### 3. How It Works


**With the option:**

1. **The option's delta tells you your current hedge ratio**

       - Delta = 0.5 → hedge with 50 shares
       - Delta = 0.45 → hedge with 45 shares

2. **Gamma makes delta change automatically as the stock moves**

       - Stock drops → delta decreases → you need fewer short shares → **buy signal**
       - Stock rises → delta increases → you need more short shares → **sell signal**

3. **You just follow the delta—no prediction required**

       - Delta went from 0.5 to 0.45? Buy back 5 shares
       - Delta went from 0.45 to 0.5? Sell 5 shares
       - It's purely mechanical

**The option is essentially an adaptive algorithm that generates "buy" and "sell" signals automatically based on price movements!**

---

### 4. Why This Is


### 5. Without Option


- **When to buy?** "I think the stock has dropped enough" ← subjective guess
- **How much to buy?** "I'll buy $10,000 worth" ← arbitrary decision
- **Risk:** What if you're wrong? Stock could keep falling
- **Emotion:** Fear and greed influence your decisions
- **Result:** Requires skill, prediction, discipline, and luck

### 6. With Option


- **When to buy?** "Delta changed, so I rebalance now" ← mechanical rule
- **How much to buy?** "Exactly $(\Delta_{\text{new}} - \Delta_{\text{old}}) \times 100$ shares" ← precise calculation
- **Risk:** You're always hedged (delta-neutral), no directional exposure
- **Emotion:** No emotion needed, just follow the math
- **Result:** No prediction needed, purely systematic

---

### 7. The Option's


Think of the option as providing a **mathematical framework** that:

1. **Converts unpredictable price movements into predictable trading rules**

       - Stock movement is random and hard to predict
       - But delta changes are mathematically determined by gamma
       - You trade based on delta changes, not price predictions

2. **Removes directional risk**

       - Without the option, buying stock means you're betting it will go up
       - With the option + hedge, you're delta-neutral (no directional bet)
       - You profit from movement itself, not direction

3. **Provides a convex payoff structure**

       - The $(\delta S)^2$ term means bigger moves = more profit
       - This convexity comes from the option's curvature (gamma)
       - Direct stock trading is linear, not convex

4. **Scales the trading amount automatically**

       - Gamma is highest at-the-money where small moves matter most
       - Gamma is lower far from the money where large moves matter less
       - The option automatically adjusts your trading intensity

---

### 8. Concrete


**Scenario:** Stock at $100, drops to $98, rises back to $100

### 9. Strategy A


- **Stock at $100:** "Should I wait for a dip? But what if it goes up?"
- **Stock drops to $98:** "Is this the bottom? Or will it drop to $95? Should I buy now or wait?"
- **Decision at $98:** You *guess* it's a good entry and buy 5 shares (how did you decide 5? why not 10 or 2?)
- **Stock rises to $100:** "Should I sell now? Or wait for $102? What if it drops again?"
- **Decision at $100:** You *guess* it's a good exit and sell (lucky timing!)
- **Problem:** Every decision requires prediction and judgment. High stress, lots of uncertainty.

### 10. Strategy B


- **Stock at $100:** Delta = 0.5, hedge with 50 shares short. Done. No decision needed.
- **Stock drops to $98:** Delta automatically changes to 0.45 (this is a mathematical fact from gamma)
- **Rebalancing rule:** Buy back 5 shares to maintain hedge. No judgment, no stress.
- **Stock rises to $100:** Delta automatically changes back to 0.5
- **Rebalancing rule:** Sell 5 shares to maintain hedge. No judgment, no stress.
- **Advantage:** Zero prediction required, purely mechanical, emotionless.

**The difference:** Strategy A requires you to be a fortune teller. Strategy B just requires you to follow simple math.

---

### 11. What You're


**Theta (time decay) is the price you pay for this automatic signal service:**

$$\delta \Pi = \underbrace{\frac{1}{2}\Gamma(\delta S)^2}_{\text{profit from automatic signals}} - \underbrace{\theta\,\delta t}_{\text{cost of the signal service}}$$

Think of it like:

- **Gamma profits:** Revenue from following the automatic trading signals
- **Theta cost:** Subscription fee for the signal-generating service
- **Net profit:** Revenue - Subscription fee

**The option is worth it if:** The stock moves around enough (high realized volatility) that the signal service generates more profit than its subscription cost!

---

### 12. The Key Insight


**The option doesn't just let you "buy low, sell high"—it tells you WHEN and HOW MUCH to buy and sell, without requiring any market prediction or timing skill.**

| Without the Option | With the Option (Gamma Scalping) |
|-------------------|----------------------------------|
| ❌ Must predict market turning points | ✓ Delta changes tell you when to trade |
| ❌ Must decide how much to trade | ✓ Gamma determines exactly how much |
| ❌ Exposed to directional risk | ✓ Hedged against directional moves |
| ❌ Requires discretionary judgment | ✓ Purely mechanical, rule-based |
| ❌ Emotional decisions | ✓ Emotionless execution |
| ❌ Timing skill needed | ✓ No timing needed |

**The option converts an unpredictable, stressful trading problem into a predictable, systematic process.**

**That's why you need the option!**

---

## Why It Works


The gamma term $\frac{1}{2}\Gamma(\delta S)^2$ captures the "buy low, sell high" pattern:

- When the stock drops, your delta decreases → you need fewer short shares → **buy signal**
- When the stock rises, your delta increases → you need more short shares → **sell signal**
- The squared term $(\delta S)^2$ means you profit regardless of direction
- After each rebalancing, your portfolio is delta-neutral again, ready for the next move

**The key:** You don't need to predict direction. The rebalancing rules automatically make you buy low and sell high!

---

## Pros and Cons


### 1. Advantages ✓


**1. Direction-neutral strategy**

- You don't need to predict whether the stock goes up or down
- You only need to predict that it will *move* (be volatile)

**2. Automatic "buy low, sell high" mechanism**

- The rebalancing rules force disciplined trading
- No need to time the market or make discretionary decisions
- Removes emotional bias from trading
- Delta and gamma tell you exactly when and how much to trade

**3. Mathematical edge**

- If you believe realized volatility will exceed implied volatility, you have a quantifiable edge
- The P&L formula gives you a clear framework: is $\frac{1}{2}\Gamma(\delta S)^2 > \theta\,\delta t$?

**4. Defined maximum loss**

- Your worst case is losing the option premium you paid
- Unlike naked short options, you have limited downside

**5. Profits in choppy markets**

- Sideways, volatile markets (where directional traders struggle) are ideal for gamma scalping
- Multiple back-and-forth moves generate multiple profitable rebalances

**6. Volatility is sometimes more predictable than direction**

- Certain market conditions (earnings, events, regime changes) create predictable volatility spikes
- Easier to know "something will happen" than to know which direction

**7. Systematic and emotionless**

- Follow mathematical rules, not gut feelings
- Reduces psychological stress of trading
- Can be automated or semi-automated

### 2. Disadvantages ✗


**1. Transaction costs eat into profits**

- Every rebalance costs money: commissions, bid-ask spreads, slippage
- Frequent rebalancing (necessary for high gamma) means costs add up quickly
- Real P&L: $\delta \Pi \approx \frac{1}{2}\Gamma(\delta S)^2 - \theta\,\delta t - \text{transaction costs}$

**2. Time decay is relentless**

- Theta bleeds away every day, even when the market doesn't move
- Weekends and overnight periods drain value without giving you rebalancing opportunities
- You're constantly "paying rent" to hold the position

**3. Requires active management**

- Not a set-and-forget strategy
- You need to monitor positions and rebalance frequently
- Time-intensive and requires discipline

**4. Can still lose money in volatile markets**

- Even if volatility increases, you can lose if:
  - It doesn't increase *enough* to overcome theta
  - Most movement happens in large gaps (where you can't rebalance)
  - Transaction costs are too high

**5. Near-expiration gamma explosion**

- Gamma becomes extremely large near expiration, especially at-the-money
- While this creates huge rebalancing profits, it also means:
  - Theta becomes enormous (you're paying a lot per day)
  - Small stock moves create large, rapid hedge adjustments
  - Higher operational risk and stress

**6. Path dependency**

- Not just *how much* the stock moves, but *when* and *how* it moves matters
- Example: One big move vs. many small moves (same total distance)
  - Many small moves: multiple profitable rebalances → good for you
  - One big gap move: only one rebalance → less profit
- The $(\delta S)^2$ term is realized through actual rebalancing trades

**7. Capital requirements**

- Need enough capital to maintain the delta hedge
- Stock hedge position can be substantial, especially for expensive stocks
- Margin requirements and risk management considerations

**8. Execution risk**

- In fast-moving markets, you may not rebalance at desired prices
- Slippage can be significant during volatility spikes
- "Pinned" positions near expiration can be difficult to manage

---

## When Gamma Scalping


**Favorable conditions:**

- You bought options when implied volatility was low
- Realized volatility turns out to be high (lots of back-and-forth movement)
- Sufficient time to expiration (weeks to months, not days)
- Liquid underlyings with tight bid-ask spreads
- Stable, frequent price movements (not large gaps)

**Unfavorable conditions:**

- You bought expensive options (high implied volatility)
- Stock barely moves or moves in large gaps
- Very short time to expiration (theta overwhelms gamma gains)
- High transaction costs or illiquid markets
- Large overnight/weekend gaps (can't rebalance during closed markets)

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

**Avoid this strategy when:**
- [Unfavorable Greeks environment]
- [High transaction costs]
- [Insufficient liquidity]
- [Wrong volatility regime]

### 3. Calculate maximum


**Calculate maximum position size:**

$$
\text{Max Size} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Greeks Loss}}
$$

**For Greeks strategies, consider:**
- Greeks exposure limits
- Rebalancing capacity
- Capital for hedge adjustments
- Margin requirements

### 4. Best practices: 1


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

### 5. Active management


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

### 6. Greeks risk


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

### 7. Track for every


**Track for every trade:**
- Entry Greeks (delta, gamma, vega, theta)
- Rebalancing frequency and costs
- P&L by Greek component
- Actual vs. expected volatility
- Transaction costs vs. Greeks P&L
- Lessons learned

### 8. Common Execution


1. **Ignoring transaction costs** - Frequent rebalancing eats profits
2. **Wrong rebalancing frequency** - Too often or too infrequent
3. **Insufficient liquidity** - Cannot execute rebalances efficiently
4. **Over-leveraging Greeks** - Excessive exposure to single Greek
5. **Neglecting other Greeks** - Focus on one Greek, ignore others
6. **Poor hedge timing** - Waiting too long or reacting too quickly

### 9. Professional


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


**Critical errors that destroy gamma scalping profits:**

### 1. The error: "Stock


**The error:**
"Stock is volatile lately. Perfect for gamma scalping!"

**Example:**
- AAPL moving $5/day (seems volatile)
- But IV: Only 18% (20th percentile - LOW)
- Historical realized vol: 25%
- **Gap: IV is UNDERPRICED**

**Why it's wrong:**

When IV < Realized vol:
- You're paying LESS than fair value
- Theta will be smaller
- But realized vol still costs to hedge
- **Should be SHORT gamma, not long!**

**The fix:**
- Only gamma scalp when IV > Realized vol
- Check IV percentile (need >40th percentile minimum)
- Calculate: Current IV vs. 30-day realized vol
- If IV lower → Short gamma (opposite strategy)

---

### 2. The error: "Gamma


**The error:**
"Gamma is +0.50, I'll rebalance every hour!"

**Example:**
- Straddle theta: -$50/day
- Rebalances: 8 times/day
- Commission: $0.50/share
- Shares per rebalance: 50
- **Daily commission: 8 × $0.50 × 50 = $200**

**Daily P&L:**
- Gamma profits: $120
- Theta cost: -$50
- Commission: -$200
- **Net: -$130** (LOSING despite volatility!)

**Why it's wrong:**

Transaction costs include:
- Commissions ($0.50-1.00 per share)
- Bid-ask slippage ($0.02-0.05 per share)
- Market impact (moving price against you)

**For retail trader:**
- Total cost: $0.70-1.50 per share round-trip
- 50 shares = $35-75 per rebalance
- 8 rebalances = $280-600/day!

**The fix:**
- Rebalance less frequently
- Use delta bands: Rebalance when delta >0.30 (not every move)
- Calculate: Gamma profits must exceed costs
- Typical: 1-2 rebalances/day MAX for retail

---

### 3. The error: "Set


**The error:**
"Set and forget. I'll rebalance once a day at close."

**Example:**
- Stock gaps $10 at open
- Delta now 0.80 (massive exposure!)
- Waits until close to rebalance
- Stock moves another $5 against position
- **Unhedged loss: $750**

**Why it's wrong:**

Too infrequent:
- Large delta excursions
- Misses gamma profits
- Takes on unwanted directional risk

**The error (opposite):**
"I'll rebalance every 15 minutes!"

**Why it's wrong:**

Too frequent:
- Transaction costs explode
- Overtrading
- Chasing small moves

**The fix:**

**Delta band approach:**
- Rebalance when |Delta| > 0.25-0.30
- Not on time schedule
- Based on actual exposure
- Balances costs vs. risk

**Example:**
- Delta starts: 0
- Stock moves $3 → Delta: 0.15 → Don't rebalance
- Stock moves $6 → Delta: 0.35 → **REBALANCE**
- Rebalancing back to 0
- Wait for next trigger

---

### 4. The error: "Gamma


**The error:**
"Gamma scalping is 'market neutral.' I'll use 50% of my account!"

**Example:**
- Account: $50,000
- Position: 10× straddles @ $2,500 each = $25,000
- "It's hedged, so low risk, right?"

**Wrong! **

**What happens:**
- Volatility dies
- Theta bleeding $300/day
- Position down $3,000 after 2 weeks
- **12% account drawdown**
- Psychological pressure to exit
- Exits at worst time

**Why it's wrong:**

"Market neutral" ≠ Low risk
- Vega risk (IV changes)
- Theta risk (time decay)
- Gap risk (can't hedge)
- Execution risk (slippage)

**The fix:**

**Position sizing for gamma scalping:**
$$
\text{Max Position} = \frac{\text{Account} \times 5\%}{\text{Straddle Cost}}
$$

**Example:**
- $50,000 account
- Max risk: $2,500
- Straddle cost: $2,500
- **Max: 1 contract** (not 10!)

**Professional sizing:**
- 5% per position
- Max 20% total in gamma scalping
- 50% cash for rebalancing
- Rest in other strategies

---

### 5. The error: "High


**The error:**
"High IV before earnings = perfect for gamma scalping!"

**Example:**
- AAPL earnings in 2 days
- IV: 45% (elevated!)
- Sells ATM straddle
- "I'll gamma scalp the movement"

**What happens:**
- Stock gaps $8 on earnings (from $180 to $188)
- Delta hedge (short stock): -$800 loss
- Straddle gain: Only $500
- **Net: -$300** (gap losses > straddle gain)

**Why it's DEADLY:**

Gamma scalping assumes:
- Continuous rebalancing
- No gaps

Earnings create:
- GAPS (can't rebalance)
- Binary moves
- IV crush after (long vega gets killed)

**The fix:**

**NEVER gamma scalp through:**
- Earnings (any stock)
- FOMC meetings (indices)
- Binary FDA decisions (biotech)
- Elections (market indices)
- Geopolitical events

**Rule:** Exit ALL gamma scalps 2 days before any binary event.

---

### 6. The error: "Gamma


**The error:**
"Gamma scalping is about gamma. I don't need to worry about vega."

**Example:**
- Long ATM straddle
- Vega: +100
- Gamma scalping happily
- IV drops from 30% → 25% (5 points)
- **Vega loss: -$500**
- Erases 10 days of gamma profits!

**Why it's wrong:**

Long straddle = long vega:
- If IV drops → Massive loss
- Can lose MORE from vega than gain from gamma
- Common scenario: Post-event IV crush

**Example:**
- Enter: IV 35% (post-earnings elevated)
- Week later: IV 25% (normalize)
- Vega loss: -$1,000
- Gamma profits: +$800
- **Net: -$200** (vega killed you!)

**The fix:**

**Option 1: Hedge vega**
- Sell farther OTM options (calendar spread)
- Reduces vega exposure
- Complicated for retail

**Option 2: Only enter when IV won't drop**
- Low IV environment already (15-20%)
- Unlikely to drop further
- Or: Trending higher

**Option 3: Accept the risk**
- Size appropriately
- Understand: You're long gamma AND long vega
- Both must work in your favor

---

### 7. The error: "I


**The error:**
"I understand the math. I don't need stops."

**Example:**
- Entry: Straddle @ $2,500
- Week 1: Down $300
- Week 2: Down $800
- Week 3: Down $1,400
- Week 4: Down $2,000
- Finally exits: -$2,000 (80% loss)

**Why it's wrong:**

Gamma scalping can bleed slowly:
- Low vol environment = death by thousand cuts
- Theta wins every day
- Gamma P&L not enough
- Loss accelerates

**The fix:**

**Stop loss rules:**

**Time-based:**
- Exit at 21 DTE (regardless of P&L)
- Reason: Gamma risk too high <21 DTE

**Loss-based:**
- Exit at -30% of premium
- Example: $2,500 straddle → Exit at -$750
- Reason: Preserve capital for better opportunities

**Vol-based:**
- Exit if realized vol < 50% of implied vol for 5 days
- Example: IV 30%, realized vol 12% → **EXIT**
- Reason: Vol not materializing, theta will win

---

### 8. The error: "Vol


**The error:**
"Vol died. Let me add more contracts to make up for it!"

**Example:**
- Initial: 1 straddle, down $400
- "If I add 2 more, I can average down"
- Adds 2 straddles @ $2,200 each
- Vol continues dead
- Now: 3 straddles, down $1,500
- **Disaster!**

**Why it's wrong:**

Averaging down in gamma scalping:
- Doesn't change the vol environment
- Increases exposure when conditions WORST
- Classic revenge trading

**If vol is low:**
- More position size won't create vol
- You're just losing faster

**The fix:**

**If in losing gamma scalp:**
1. Exit (take loss)
2. Wait for vol to return
3. Enter NEW position (fresh start)

**Never:**
- Average down
- Add to losers
- "Double down to recover"

---

### 9. The error: "I'm


**The error:**
"I'm up $500. Great!"

**But breakdown:**
- Gamma P&L: +$200
- Theta cost: -$400
- Vega P&L: +$700

**What this ACTUALLY means:**

You're NOT making money from gamma scalping!
- Gamma profits: Barely covering theta
- Real profit: Vega (IV increased)
- **You got lucky on vega, not skilled on gamma**

**Why it matters:**

If you don't track components:
- Don't know if strategy working
- Might continue when should exit
- False confidence

**Example continuation:**
- Week 2: Vega goes AGAINST you (-$700)
- Gamma still weak (+$200)
- Theta continues (-$400)
- **Now: -$900** (all vega gains erased + more)

**The fix:**

**Daily P&L attribution:**

$$
\text{Total P\&L} = \text{Gamma P\&L} + \text{Theta P\&L} + \text{Vega P\&L} + \text{Costs}
$$

**Track in spreadsheet:**

| Day | Gamma | Theta | Vega | Costs | Total | Notes |
|-----|-------|-------|------|-------|-------|-------|
| 1 | +$120 | -$50 | +$20 | -$30 | +$60 | Good day |
| 2 | +$90 | -$50 | -$10 | -$20 | +$10 | Gamma weak |
| 3 | +$40 | -$50 | -$30 | -$25 | -$65 | **RED FLAG** |

**When to exit:**
- Gamma < Theta for 3+ days → EXIT
- Vega driving profits (not gamma) → Risk
- Costs eating into profits → Reduce rebalancing

---

### 10. The error: "Set


**The error:**
"Set up the straddle, rebalance daily. Passive income!"

**Reality:**

**Hour 1: 9:30 AM**
- Market opens, gap down
- Need to rebalance NOW
- Can't wait

**Hour 3: 11:30 AM**
- Fed speaker surprise comments
- Vol spike, need to assess
- Should I exit?

**Hour 5: 2:00 PM**
- Stock rallying, delta at 0.35
- Rebalance needed
- Execute trades

**After hours:**
- Calculate P&L attribution
- Adjust for tomorrow
- Set alerts

**This is ACTIVE, not passive!**

**Time commitment:**
- Monitoring: 2-3 hours/day minimum
- Rebalancing: 1-2 trades/day
- Analysis: 30 min/day
- **Total: 3-4 hours/day**

**The fix:**

**If you don't have time:**
- Don't gamma scalp
- Use passive strategies
- Buy and hold, or Wheel, or index funds

**Gamma scalping requires:**
- Active monitoring
- Quick decisions
- Daily rebalancing
- Continuous analysis

**It's a job, not passive income!**

---

### 11. | | Mistake |


| # | Mistake | Fix |
|---|---------|-----|
| 1 | Entering at low IV | Only when IV > realized vol |
| 2 | Ignoring costs | Limit rebalances, calculate all costs |
| 3 | Wrong rebalance frequency | Use delta bands, not time |
| 4 | Over-sizing | Max 5% per position |
| 5 | Through earnings | Exit 2 days before ANY binary event |
| 6 | Neglecting vega | Track vega, hedge or accept risk |
| 7 | No stop loss | Exit at -30% OR 21 DTE |
| 8 | Chasing/averaging down | Exit losers, wait for new setup |
| 9 | Not tracking attribution | Daily P&L breakdown required |
| 10 | Treating as passive | Accept it's active or don't do it |

**Remember:** Gamma scalping is hard. Mistakes are common. Pros make these mistakes too. The difference: They learn and adjust. You should too!

---

## Real-World Examples


**Concrete scenarios showing gamma scalping in practice:**

### 1. Pension Duration


**Setup:**
- SPY: $440
- IV: 24% (55th percentile)
- 30-day realized vol: 18%
- Gap: IV overpriced by 6 vol points
- Trader: "This is my edge"

**Trade:**
- Buy 1× $440 straddle @ $24 (30 DTE)
- Delta: 0
- Gamma: +0.025
- Theta: -$19/day

**Week 1:**
- SPY range: $437-$445 daily
- Rebalanced 10 times
- Gamma P&L: +$720
- Theta cost: -$133
- **Net: +$587**

**Week 2:**
- Continued choppiness
- Gamma P&L: +$650
- Theta cost: -$140
- **Net: +$510**

**Exit Day 14:**
- Position value: $24 → $31.10
- **Profit: +$710 (29.6%)**
- Annualized: ~775%

**Why it worked:**
✅ IV > Realized vol (edge existed)
✅ Choppy market (not trending)
✅ Disciplined exit (14 days)
✅ Proper sizing (1 contract = 2.4% of $100k account)

---

### 2. Transition Risk


**Setup:**
- AAPL: $180 post-earnings
- IV: 42% (75th percentile - VERY high)
- Trader: "High IV = lots of premium = good for gamma scalping!"

**Trade:**
- Buy 2× $180 straddles @ $18 each = $3,600

**Week 1:**
- AAPL range: $178-$183
- Decent movement!
- Gamma P&L: +$340
- Theta cost: -$180
- Vega: $0 (IV stable)
- **Net: +$160** (good!)

**Week 2:**
- Problem: IV crush begins
- IV: 42% → 36% (-6 points)
- Vega exposure: 2 straddles × 25 vega each = 50 vega
- Vega loss: 50 × -6 = **-$300**
- Plus theta: -$180
- Plus gamma: +$280
- **Net: -$200** (now losing!)

**Week 3:**
- IV continues dropping: 36% → 32%
- Vega loss: **-$200** more
- Gamma can't keep up
- Total now: -$240

**Exit Day 18:**
- Vega damage: -$500
- Gamma profits: +$620
- Theta costs: -$360
- **Net: -$240 (-6.7% loss)**

**What went wrong:**
❌ Entered at PEAK IV (75th percentile)
❌ Ignored vega risk (long vega + IV dropping)
❌ Gamma couldn't overcome vega losses

**Lesson:** High IV can be a TRAP if it's mean-reverting downward!

---

### 3. Portable Alpha


**Setup:**
- TSLA: $240
- Earnings: Tomorrow after close
- IV: 68% (elevated pre-earnings)
- Trader: "I'll gamma scalp the pre-earnings movement!"

**Trade:**
- Buy 1× $240 straddle @ $32 (2 days to earnings)

**Day 1:**
- TSLA: $238-$245 (choppy pre-earnings)
- Gamma P&L: +$240
- Theta cost: -$60
- **P&L: +$180** (great!)

**Earnings night:**
- Trader: "Do I hold through earnings or exit?"
- Greed: "If I exit, I lock in +$180. If I hold, maybe more movement!"
- **Decides to HOLD**

**Next morning:**
- TSLA gaps to $265 (+$25!)
- **The gap destroyed everything:**
  - Delta hedge (short stock) taken on: -$1,200 loss
  - Straddle value: Only up $800
  - **Net: -$400**
  - From +$180 to -$400 overnight!

**Final:**
- Exited immediately at open
- Total loss: -$400
- Account impact: -4%

**What went wrong:**
❌ HELD THROUGH EARNINGS (cardinal sin!)
❌ Gap risk = automatic loss for gamma scalper
❌ Greed (didn't take +$180 profit)

**Lesson:** NEVER gamma scalp through binary events. The gap will destroy you.

---

### 4. Tactical Duration


**Setup:**
- SPY: $480
- VIX: 11 (very low)
- Market: Grinding higher slowly
- IV: 16% (25th percentile - LOW)
- Trader: "Market is moving, I'll gamma scalp!"

**Trade:**
- Buy 1× $480 straddle @ $18 (30 DTE)

**Week 1:**
- SPY: $479-$482 (3-point range - TINY!)
- Gamma P&L: +$80
- Theta cost: -$130
- **Net: -$50** (losing)

Trader: "Just one slow week. Vol will pick up."

**Week 2:**
- SPY: $481-$484 (still small)
- Gamma P&L: +$90
- Theta cost: -$130
- **Net: -$40**

**Week 3:**
- Same pattern
- Gamma P&L: +$75
- Theta cost: -$125
- **Net: -$50**

**Exit Day 21:**
- Total gamma: +$245
- Total theta: -$385
- **Net: -$140 (-7.8%)**

**What went wrong:**
❌ Entered in LOW volatility environment (VIX 11)
❌ IV < Realized vol (should have been SHORT gamma)
❌ No edge existed
❌ Theta always wins in low vol

**Lesson:** Don't gamma scalp just because "market is moving." Need HIGH vol, not any vol.

---

### 5. Duration Hedge


**Setup:**
- Trader: Professional, 10 years experience
- Account: $250,000
- Strategy: Multiple small gamma scalps

**Trade 1 (January):**
- SPY straddle, 30 DTE, $4,500 cost
- Conditions: IV 28%, realized vol 24% (good)
- Hold: 16 days
- **Result: +$1,240 (+27.6%)**

**Trade 2 (February):**
- QQQ straddle, 30 DTE, $4,200 cost
- Conditions: IV 32%, realized vol 28% (good)
- Hold: 14 days
- **Result: +$1,580 (+37.6%)**

**Trade 3 (March):**
- SPY straddle, 30 DTE, $4,800 cost
- Conditions: IV 22%, realized vol 26% (BAD - IV too low!)
- Exited Day 5 at -$380
- **Result: -$380 (-7.9%)**
- Note: Exited EARLY when realized vol was high but IV not keeping up

**Trade 4 (April):**
- No trade - market too quiet (VIX <12)
- Sat on hands
- **Discipline to NOT trade**

**Trade 5 (May):**
- SPY straddle, volatility returned
- Hold: 12 days
- **Result: +$920 (+20.4%)**

**Q1-Q2 Results:**
- Trades: 4 (1 skipped)
- Winners: 3 (+$3,740)
- Losers: 1 (-$380)
- **Net: +$3,360**
- Capital risked: ~$18,000 total
- **ROI: 18.7% (on capital)**
- Account: +1.3%

**Why this worked:**
✅ Selective (only traded when edge existed)
✅ Disciplined (exited loser early)
✅ Patient (skipped low vol month)
✅ Proper sizing (2% per trade)
✅ Diversified (SPY + QQQ)

**Lesson:** Gamma scalping is NOT "always be trading." It's "trade when conditions are right, sit when they're not."

---

### 6. Setup: Trader:


**Setup:**
- Trader: Retail, using Robinhood
- NVDA: $450
- Thinks: "I'll gamma scalp NVDA, it's volatile!"

**Trade:**
- Buy 1× $450 straddle @ $30

**Day 1 rebalancing nightmare:**

**10:00 AM: Rebalance #1**
- Delta: 0.40, need to sell 40 shares
- Market order: Fills at $449.75 (NVDA at $450)
- **Slippage: $10**

**11:30 AM: Rebalance #2**
- Delta: -0.35, need to buy 35 shares
- Market order: Fills at $452.25 (NVDA at $452)
- **Slippage: $7.75**

**2:00 PM: Rebalance #3**
- Delta: 0.30, need to sell 30 shares
- Market order: Fills at $454.65 (NVDA at $454.50)
- **Slippage: $4.50**

**Day 1 totals:**
- Gamma P&L (theoretical): $180
- Actual slippage: $22.25
- Commissions: $0 (Robinhood)
- **Net gamma: $157.75**
- Theta cost: -$40
- **Net: +$117.75** (OK but slippage ate 12%!)

**Week 1 (extrapolated):**
- 5 days × 3 rebalances = 15 rebalances
- Slippage: ~$330
- Gamma P&L: $900
- **Slippage = 37% of gamma profits!**

**Result after 2 weeks:**
- Gamma: +$1,800
- Slippage: -$660
- Theta: -$560
- **Net: +$580** (19% return)

**But:**
If using limit orders:
- Slippage: -$180 (much better!)
- **Net: +$1,060** (35% return)

**Difference: 16% return due to execution!**

**Lesson:** Use LIMIT orders, not market orders. Slippage is a silent killer in gamma scalping.

---

### 7. Winners share:


**Winners share:**
- Entered when IV > realized vol (edge)
- Choppy markets (not trending)
- Disciplined exits (50-80% profit)
- Proper sizing (2-5% of account)
- Good execution (limit orders)

**Losers share:**
- Wrong vol environment (low IV or IV mean-reverting)
- Binary events (earnings, gaps)
- Over-sized positions
- No stop losses
- Poor execution (market orders, slippage)

**The formula:**
$$
\text{Success} = \text{Right Vol Environment} + \text{Good Execution} + \text{Discipline}
$$

Miss any one → Disaster!

---

## Real-World Examples


[Concrete examples]

