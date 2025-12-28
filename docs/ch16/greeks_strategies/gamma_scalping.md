# Gamma Scalping

**Gamma scalping** is a trading strategy that systematically profits by **buying low and selling high** through frequent rebalancing of a hedged option position.

---

## The Core Insight

**The fundamental idea is simple:**

- Own an option + hedge with stock
- When the stock moves, your hedge becomes unbalanced
- Rebalance by trading in the opposite direction
- This forces you to buy after drops and sell after rises
- Repeat this many times to accumulate profits

**You're essentially converting stock volatility into systematic "buy low, sell high" trades.**

---

## The Basic Idea

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

## Understanding the P&L: Buy Low, Sell High

$$\boxed{\delta \Pi = \underbrace{\frac{1}{2}\Gamma(\delta S)^2}_{\text{buy low, sell high profits}} - \underbrace{\theta\,\delta t}_{\text{option time decay}}}$$

### The Two Components

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

### How "Buy Low, Sell High" Happens Automatically

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

### Concrete Example

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

### The Trade-off

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

## Why You Need the Option: The Critical Role

**Natural question:** "If the profit comes from buying low and selling high, why do I need the option? Can't I just trade the stock directly?"

**The answer:** Yes, the profit comes from "buy low, sell high"—but the option provides something invaluable that makes this strategy actually work.

---

### The Problem Without Options

**If you just trade stock directly:**

**Critical questions arise:**

- When do you buy? When do you sell? How much?
- You need to **predict** when the stock has dropped enough to buy
- You need to **predict** when the stock has risen enough to sell  
- You need **timing skill** and **market prediction**
- You're exposed to **directional risk** (what if the stock keeps falling after you buy?)

**This is very difficult!** Most traders fail at timing the market consistently.

---

### The Option's Role: Automatic Trading Signals

**The option (via gamma) provides an automatic, mathematical rule that tells you exactly when and how much to trade—no prediction needed.**

#### How It Works

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

### Why This Is Powerful

#### Without Option (Discretionary Trading)

- **When to buy?** "I think the stock has dropped enough" ← subjective guess
- **How much to buy?** "I'll buy $10,000 worth" ← arbitrary decision
- **Risk:** What if you're wrong? Stock could keep falling
- **Emotion:** Fear and greed influence your decisions
- **Result:** Requires skill, prediction, discipline, and luck

#### With Option (Gamma Scalping)

- **When to buy?** "Delta changed, so I rebalance now" ← mechanical rule
- **How much to buy?** "Exactly $(\Delta_{\text{new}} - \Delta_{\text{old}}) \times 100$ shares" ← precise calculation
- **Risk:** You're always hedged (delta-neutral), no directional exposure
- **Emotion:** No emotion needed, just follow the math
- **Result:** No prediction needed, purely systematic

---

### The Option's Mathematical Service

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

### Concrete Comparison

**Scenario:** Stock at $100, drops to $98, rises back to $100

#### Strategy A: Direct Trading (No Option)

- **Stock at $100:** "Should I wait for a dip? But what if it goes up?"
- **Stock drops to $98:** "Is this the bottom? Or will it drop to $95? Should I buy now or wait?"
- **Decision at $98:** You *guess* it's a good entry and buy 5 shares (how did you decide 5? why not 10 or 2?)
- **Stock rises to $100:** "Should I sell now? Or wait for $102? What if it drops again?"
- **Decision at $100:** You *guess* it's a good exit and sell (lucky timing!)
- **Problem:** Every decision requires prediction and judgment. High stress, lots of uncertainty.

#### Strategy B: Gamma Scalping (With Option)

- **Stock at $100:** Delta = 0.5, hedge with 50 shares short. Done. No decision needed.
- **Stock drops to $98:** Delta automatically changes to 0.45 (this is a mathematical fact from gamma)
- **Rebalancing rule:** Buy back 5 shares to maintain hedge. No judgment, no stress.
- **Stock rises to $100:** Delta automatically changes back to 0.5
- **Rebalancing rule:** Sell 5 shares to maintain hedge. No judgment, no stress.
- **Advantage:** Zero prediction required, purely mechanical, emotionless.

**The difference:** Strategy A requires you to be a fortune teller. Strategy B just requires you to follow simple math.

---

### What You're Paying For

**Theta (time decay) is the price you pay for this automatic signal service:**

$$\delta \Pi = \underbrace{\frac{1}{2}\Gamma(\delta S)^2}_{\text{profit from automatic signals}} - \underbrace{\theta\,\delta t}_{\text{cost of the signal service}}$$

Think of it like:

- **Gamma profits:** Revenue from following the automatic trading signals
- **Theta cost:** Subscription fee for the signal-generating service
- **Net profit:** Revenue - Subscription fee

**The option is worth it if:** The stock moves around enough (high realized volatility) that the signal service generates more profit than its subscription cost!

---

### The Key Insight

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

### Advantages ✓

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

### Disadvantages ✗

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

## When Gamma Scalping Works Best

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

## What to Remember

- **Gamma scalping is essentially a systematic "buy low, sell high" strategy**
- **The option provides automatic trading signals (via delta and gamma) so you don't need to predict the market**
- Your portfolio $\Pi$ combines a long option with a delta hedge (short stock)
- The rebalancing rules automatically force you to buy after drops and sell after rises
- The gamma term $\frac{1}{2}\Gamma(\delta S)^2$ represents your accumulated "buy low, sell high" profits
- The theta term represents the cost of the "automatic signal service"
- You profit when realized variance exceeds what you paid (theta decay plus transaction costs)
- "Gamma scalping" specifically refers to **long gamma** positions ($\Gamma > 0$)
- This is an active strategy requiring discipline, capital, and low transaction costs
- Success depends on the relationship: **realized volatility vs. implied volatility**
- **Key advantage:** Converts unpredictable markets into predictable, rule-based trading