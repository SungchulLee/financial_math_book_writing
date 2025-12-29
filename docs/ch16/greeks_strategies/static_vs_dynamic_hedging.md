# Static Hedging

**Static hedging** is a risk management approach where you establish a hedge once and hold it without continuous rebalancing, as opposed to dynamic hedging which requires frequent adjustments.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/static_vs_dynamic_hedging_comparison.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 1:** Static Vs Dynamic Hedging Comparison visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/static_vs_dynamic_hedging_decision.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 2:** Static Vs Dynamic Hedging Decision visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/static_vs_dynamic_hedging_frequency.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 3:** Static Vs Dynamic Hedging Frequency visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/static_vs_dynamic_hedging_tracking.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 4:** Static Vs Dynamic Hedging Tracking visualization.

---

## The Core Insight

**The fundamental idea:**

- Most strategies we've covered require continuous delta hedging (dynamic)
- But continuous rebalancing has costs (bid-ask, commissions)
- What if you could hedge ONCE and be done?
- Static hedging: set it and forget it
- Trade off: imperfect hedge, but no transaction costs
- Works best for certain option types (barriers, digitals)

**The key equation:**

$$
\text{Static Hedge} = \text{Set once} + \text{Hold to maturity} + \text{Accept tracking error}
$$

**You're essentially betting: "The savings from avoiding transaction costs outweigh the tracking error from not rebalancing."**

---

## What Is Static Hedging?

**Before understanding why it's useful, understand what it is:**

### The Definition

**Static hedging** means:

- Establish hedge positions at inception
- Do NOT adjust or rebalance
- Hold to expiration (or to barrier event)
- Accept imperfect hedge (tracking error)

**Contrast with dynamic hedging:**

- Rebalance constantly (maintain delta-neutral)
- Perfect hedge in continuous limit
- High transaction costs
- What we've used in most strategies

### The Spectrum

```
Static                Mixed              Dynamic
  |                    |                    |
  |                    |                    |
Hedge once      Rebalance rarely    Rebalance constantly
Zero costs      Low costs           High costs
High tracking   Medium tracking     Low tracking error
  error           error
```

**Examples across spectrum:**

- **Pure static:** Barrier option hedged with portfolio of vanillas, never touch
- **Semi-static:** Rebalance monthly instead of daily
- **Pure dynamic:** Gamma scalping (continuous rebalancing)

---

## Why Static Hedging Exists

**Why would you ever accept tracking error?**

### 1. Transaction Costs Are Real

**The dynamic hedging dream vs. reality:**

**Theory (Black-Scholes world):**

- Continuous rebalancing
- No transaction costs
- Perfect hedge achieved
- P&L = 0 (fully hedged)

**Reality:**

- Discrete rebalancing (not continuous)
- Bid-ask spreads every trade
- Commissions
- Market impact
- **Costs accumulate rapidly**

**Example:**

- Dynamic hedging a 1-year option
- Rebalance daily: 252 trades
- 1¢ bid-ask spread per share
- 100 shares per rebalance
- **Cost: 252 × $1 = $252** (could be > option premium!)

### 2. Path-Dependent Options

**Some options are naturally suited to static hedging:**

**Barrier options:**

- Payoff depends on path (did it hit barrier?)
- Dynamic hedging is very difficult
- Static replication often better
- Can perfectly hedge with portfolio of vanillas

**Digital (binary) options:**

- Discontinuous payoff
- Gamma spikes near barrier
- Dynamic hedging nearly impossible
- Static hedge with spread is cleaner

### 3. Liquidity Constraints

**Can't always rebalance:**

- Illiquid underlyings
- After-hours barriers
- Gap risk (can't trade fast enough)
- Emergency hedges needed
- **Static hedge provides insurance**

### 4. Regulatory/Structural Constraints

**Some institutions can't rebalance frequently:**

- Mutual funds (daily NAV)
- Pension funds (compliance)
- Large positions (market impact)
- Prefer set-and-forget hedges

### 5. Long Time Horizons

**For very long-dated options:**

- 5-10 year options
- Cumulative transaction costs enormous
- Static hedge more economical
- Accept tracking error over time

---

## Static vs. Dynamic Hedging

**The fundamental comparison:**

| Aspect | Static Hedging | Dynamic Hedging |
|--------|---------------|-----------------|
| **Rebalancing** | None (or rare) | Continuous (or frequent) |
| **Transaction costs** | Minimal (one-time) | High (ongoing) |
| **Tracking error** | High (path dependent) | Low (rebalanced away) |
| **Complexity** | Simple (set and forget) | Complex (constant monitoring) |
| **Best for** | Barriers, digitals, long-dated | Vanillas, short-dated |
| **Greeks** | Fixed (don't adjust) | Managed (rebalanced) |
| **Capital** | One-time deployment | Requires liquidity buffer |
| **Risk** | Accept residual risk | Minimize residual risk |
| **Skill required** | Upfront structuring | Ongoing management |

### The Cost-Error Trade-off

**Fundamental relationship:**

$$
\text{Total Cost} = \text{Transaction Costs} + \text{Tracking Error Cost}
$$

**Dynamic hedging:**

- High transaction costs (many trades)
- Low tracking error (stay hedged)
- **Good when volatility high, short maturity**

**Static hedging:**

- Low transaction costs (one trade)
- High tracking error (drift from hedge)
- **Good when volatility low, long maturity**

**The decision:**

$$
\text{Choose Static if: } \frac{\text{Transaction Costs}}{\text{Delta}} > \text{Expected Tracking Error}
$$

---

## How Static Hedging Works

**The basic process:**

### Step 1: Choose Hedging Instruments

**For vanilla option, might use:**

- Underlying asset (stock)
- Other options (portfolio)
- Futures contracts
- Bonds (for rho exposure)

**For exotic option, typically use:**

- Portfolio of vanilla options
- Designed to replicate exotic's payoff
- Match at critical points (barriers, etc.)

### Step 2: Calculate Initial Hedge Ratio

**At inception:**

- Compute Greeks (delta, gamma, vega)
- Determine hedge size
- Structure portfolio to match
- **This is your ONLY adjustment**

### Step 3: Execute Hedge

**One-time trade:**

- Enter all positions
- Set and forget
- No further rebalancing

### Step 4: Hold to Maturity

**During life:**

- Greeks drift (delta changes)
- P&L accumulates
- Tracking error develops
- **Accept this drift**

### Step 5: Settle at Expiration

**At maturity:**

- Close all positions
- Realize tracking error
- Evaluate: did cost savings exceed tracking error?

---

## Static Hedging for Barrier Options

**This is THE classic application:**

### What Are Barrier Options?

**Barrier options have payoffs that depend on whether the underlying hits a barrier:**

**Up-and-Out Call:**

- Starts as regular call
- If stock hits barrier (above) → knocked out (worthless)
- Cheaper than vanilla call

**Down-and-In Put:**

- Starts as nothing
- If stock hits barrier (below) → becomes regular put
- Cheaper way to get put exposure

**Key feature:** Path-dependent (did it touch barrier?)

### Why Dynamic Hedging Fails for Barriers

**Problems with dynamic hedging:**

1. **Gamma explosion near barrier:**

   - Delta changes violently near barrier
   - Need to rebalance huge amounts
   - Impractical

2. **Gap risk:**

   - Stock can jump over barrier
   - Can't rebalance fast enough
   - Hedge breaks

3. **Monitoring:**

   - Need to watch price 24/7
   - Barriers can be hit overnight
   - After-hours risk

4. **Transaction costs:**

   - Many rebalances near barrier
   - Costs accumulate
   - Overwhelm savings from cheaper premium

### Static Hedge Solution

**Key insight:** Can replicate barrier option with portfolio of vanilla options!

**Example: Up-and-Out Call**

**Option to hedge:**

- Stock at $100
- Strike: $100
- Barrier: $120 (up-and-out)
- If hits $120 → worthless

**Static hedge portfolio:**

- Long 1 vanilla $100 call
- Short several $120 calls (quantity depends on maturity, vol)
- Ratio chosen to replicate knock-out

**How it works:**

- Below $120: portfolio behaves like knock-out call
- At $120: portfolio delta goes to zero (mimics knock-out)
- Above $120: portfolio stays delta-neutral (like knocked-out option)

**No rebalancing needed!**

### The Mathematics (Simplified)

**For up-and-out call with barrier $B$:**

$$
\text{UOC}(S, K, B) \approx C(K) - \left(\frac{B}{S}\right)^{2\mu} C\left(\frac{B^2}{S}, K\right)
$$

where $\mu$ depends on rates and volatility.

**In plain English:**

- Long vanilla call at strike $K$
- Short modified call with strike flipped around barrier
- Weights adjust for barrier reflection
- **Static replication!**

### Practical Example: Hedging Down-and-In Put

**Product:**

- Stock at $100
- Down-and-In Put: Strike $95, Barrier $85
- If stock hits $85 → becomes $95 put
- Otherwise expires worthless

**Static hedge:**

- Short vanilla $95 put
- Long certain ratio of $75 put (mirror around $85 barrier)
- Ratio: approximately $(85/100)^{2}$ ≈ 0.72

**Mechanics:**

- Stock above $85: portfolio near zero (DIP not active)
- Stock hits $85: portfolio now short $95 put, offsetting DIP
- Stock below $85: hedge tracks DIP well
- **Set once, hold to expiry**

**Tracking error:**

- Not perfect (especially far from barrier)
- But avoids massive rebalancing costs
- Trade-off accepted

---

## Static Hedging for Digital Options

**Another perfect application:**

### What Are Digital Options?

**Digital (binary) options pay fixed amount if condition met:**

**Cash-or-Nothing Call:**

- If $S_T > K$: receive $1
- Otherwise: receive $0
- Discontinuous payoff

**Problems for dynamic hedging:**

- Gamma infinite at strike at expiration
- Delta jumps from 0 to ∞ to 0
- Impossible to hedge dynamically near expiry

### Static Hedge with Call Spread

**Solution: Replicate with tight call spread**

**For $K = 100$ digital call:**

- Buy call at $99.95
- Sell call at $100.05
- Spread width: $0.10

**Payoff:**

- Stock > $100.05: spread worth $0.10
- Stock < $99.95: spread worth $0
- Near $100: approximately $0.05 (average)

**Scale up:**

- Want $10,000 digital payoff
- Use $10,000/$0.10 = 100,000 spreads
- **Static replication achieved!**

**No rebalancing:**

- Set at inception
- Hold to expiry
- Automatic settlement
- Avoids infinite gamma problem

---

## Static Hedging for Portfolio Insurance

**Protecting equity portfolios:**

### The Problem

**Investor has:**

- $1M stock portfolio
- Wants downside protection
- Doesn't want to rebalance frequently

**Options:**

1. **Dynamic hedging:** Buy puts, delta hedge, rebalance constantly
2. **Static hedging:** Buy puts, hold to maturity

### Static Solution: Protective Puts

**Strategy:**

- Own portfolio (long stock)
- Buy OTM puts (insurance)
- Hold to expiration
- **No rebalancing**

**Example:**

- Portfolio: $1M SPY
- Buy $950K puts (5% out-of-the-money)
- 3-month expiration
- Cost: $20K (2%)

**Mechanics:**

- Portfolio rises: benefit, puts expire worthless
- Portfolio falls: puts gain value, offset losses
- Protection "locked in" at inception
- **No rebalancing required**

**Tracking error:**

- Delta drifts as market moves
- Not perfectly hedged mid-way
- But protection guaranteed at expiry
- **Accept this drift**

### Why Static Here?

**Advantages over dynamic:**

1. **Simplicity:** Buy and hold (institutional compliance)
2. **Cost:** One transaction (not 60 daily rebalances)
3. **Certainty:** Know max loss upfront
4. **Psychological:** Set and forget (no daily stress)

**Trade-off:**

- Pay full put premium (could be reduced with dynamic)
- But save transaction costs and hassle
- **Often worth it for long-term investors**

---

## Semi-Static Hedging

**Middle ground: rebalance rarely**

### The Concept

**Instead of:**

- Never rebalancing (pure static)
- Or continuously (pure dynamic)

**Rebalance only when:**

- Delta drifts beyond threshold (e.g., ±20%)
- Time milestones (monthly, quarterly)
- Significant events (earnings, Fed meetings)

### Example: Monthly Rebalancing

**For 1-year option:**

- Set initial hedge
- Rebalance 12 times (monthly)
- Instead of 252 times (daily)

**Advantages:**

- Much lower transaction costs (12 vs. 252 trades)
- Reasonable tracking error (rebalance occasionally)
- Manageable complexity (monthly review)

**When it works:**

- Moderate volatility
- Long time horizons
- Reasonable risk tolerance
- **"Good enough" hedging**

---

## Static Hedging Strategies Across Your Toolkit

**How static hedging relates to strategies we've covered:**

| Strategy | Hedging Approach | Rebalancing Frequency |
|----------|-----------------|----------------------|
| **Straddles (Long)** | None | N/A (unhedged) |
| **Gamma Scalping** | Dynamic | Continuous |
| **Vega Trading** | Dynamic | Frequent |
| **Smile/Skew** | Dynamic | Frequent |
| **Calendar Spreads** | Static/Semi-Static | Rare (at roll) |
| **Dispersion** | Dynamic | Continuous (many assets) |
| **Convertible Arb** | Dynamic | Daily |
| **Variance Swaps** | **Static (internally)** | **None (by dealers)** |
| **Barrier Options** | **Static** | **None (portfolio)** |

**Key insight:**

- Most vol trading = dynamic hedging
- But some applications naturally static
- And dynamic can be approximated with semi-static

---

## Concrete Example: Static vs. Dynamic Comparison

**Let's compare both approaches for the same option:**

### Setup

**Option:**

- 6-month ATM call on SPY
- SPY at $400
- Strike: $400
- Option premium: $20
- Held by dealer (needs to hedge)

### Approach 1: Dynamic Hedging

**Day 1:**

- Sell call to customer (receive $20)
- Delta: 0.50
- Buy 50 shares at $400 (delta hedge)

**Day 30:**

- SPY now $410
- Delta now 0.60
- Buy 10 more shares at $410 (rebalance)
- Cost: $4,100

**Day 60:**

- SPY now $405
- Delta now 0.55
- Sell 5 shares at $405 (rebalance)
- Receive: $2,025

**...continue for 180 days...**

**Results:**

- Rebalanced 126 times (every other day)
- Transaction costs: 126 × $1 spread × 50 shares = $6,300
- Tracking error: Low (stayed hedged)
- **Total cost: ~$6,300**

### Approach 2: Static Hedging

**Day 1:**

- Sell call to customer (receive $20)
- Delta: 0.50
- Buy 50 shares at $400 (delta hedge)
- **Never rebalance**

**Day 30:**

- SPY now $410
- Delta now 0.60 (drifted!)
- Position now delta: -0.10 (should be 0)
- **Accept this drift**

**Day 60:**

- SPY now $405
- Delta now 0.55
- Position delta: -0.05
- **Still accept drift**

**Day 180 (Expiration):**

- SPY ends at $415
- Call exercised: pay $15 ($415 - $400)
- Stock position: profit $15 (bought at $400, sell at $415)
- **Net P&L: $0 (perfectly hedged at expiry!)**

**Results:**

- Rebalanced 0 times
- Transaction costs: $50 (initial trade only)
- Tracking error: High mid-way (delta drifted)
- But zero at expiration (stock + call offset)
- **Total cost: $50**

### The Comparison

| Metric | Dynamic | Static |
|--------|---------|--------|
| **Transaction costs** | $6,300 | $50 |
| **Tracking error (mid-life)** | Low | High |
| **Tracking error (expiry)** | Zero | Zero |
| **Complexity** | High | Low |
| **Winner** | - | **Static** (for vanilla at expiry) |

**Key insight:** For vanilla options held to expiry, static hedging works perfectly!

**Why don't dealers use it?** 

- They don't hold to expiry (customer might exercise early)
- They manage portfolios (not single options)
- They want to stay delta-neutral (risk management)
- But semi-static can work (monthly rebalancing)

---

## When Static Hedging Works Best

### Favorable Conditions

**1. Long time horizons**

- 6+ months to expiration
- Transaction costs accumulate with time
- Static saves significantly

**2. Low volatility**

- Delta drifts slowly
- Tracking error stays manageable
- Less need to rebalance

**3. Barrier options**

- Path-dependent payoffs
- Dynamic hedging impractical
- Static replication natural

**4. Digital options**

- Discontinuous payoffs
- Infinite gamma at barrier
- Static spreads work perfectly

**5. Portfolio hedging**

- Large portfolios
- Institutional constraints
- Long-term protection

**6. High transaction costs**

- Illiquid underlyings
- Wide spreads
- Large positions (market impact)
- Static saves money

**7. Held to expiration**

- Not exiting early
- Final P&L is what matters
- Mid-life drift acceptable

### Unfavorable Conditions

**1. Short time horizons**

- < 1 month
- Few rebalances needed anyway
- Dynamic not much more expensive

**2. High volatility**

- Delta drifts quickly
- Tracking error large
- Static hedge breaks down

**3. Vanilla options (dealer perspective)**

- Customers might exercise early
- Need continuous delta management
- Can't wait for expiration

**4. Need to exit early**

- Might sell position before expiry
- Tracking error matters mid-life
- Dynamic is safer

**5. Low transaction costs**

- Liquid markets (SPY, etc.)
- Tight spreads
- Dynamic becomes affordable

---

## Pros and Cons

### Advantages ✓

**1. Minimal transaction costs**

- One-time trade
- No ongoing spreads/commissions
- Significant savings over time
- **Main advantage**

**2. Simple to execute**

- Set at inception
- No monitoring needed
- No constant decisions
- Operationally easy

**3. No market impact**

- Not constantly trading
- Don't signal intentions
- Avoid information leakage
- Good for large positions

**4. Perfect for barriers/digitals**

- Natural replication
- Avoids gamma explosions
- Clean solution
- Industry standard

**5. Regulatory friendly**

- Set-and-forget acceptable
- No constant trading required
- Compliance easier
- Institutional preference

**6. Psychological ease**

- No daily stress
- No rebalancing anxiety
- Can ignore mid-life fluctuations
- Sleep well

**7. Guaranteed at expiry (for vanillas)**

- Stock + option offset perfectly
- No tracking error at maturity
- Final P&L predictable

### Disadvantages ✗

**1. Tracking error (main drawback)**

- Delta drifts over time
- Not hedged mid-life
- Path-dependent P&L
- Can be large

**2. No adjustment for market changes**

- Can't respond to volatility shifts
- Can't adjust for new information
- Stuck with initial hedge
- Less flexible

**3. Requires accurate initial setup**

- One chance to get it right
- Errors compound
- No correction opportunities
- Need sophisticated models

**4. Mark-to-market volatility**

- P&L swings mid-life
- Can look bad temporarily
- Accounting challenges
- Psychological discomfort

**5. Doesn't work for all options**

- Vanillas: maybe (if held to expiry)
- Barriers: yes
- Digitals: yes
- American options: no (early exercise)
- Exotics: depends

**6. Requires long horizon**

- Short-dated: dynamic better
- Need time for cost savings
- Not for quick trades

**7. Model risk**

- Static hedge depends on model accuracy
- If volatility or rates wrong → bad hedge
- No chance to correct
- Can be far off

**8. Liquidity risk**

- Need liquid hedging instruments
- One-time but potentially large trade
- Market impact at inception
- Slippage matters

---

## Advanced: Static Replication Theory

**The mathematical foundation:**

### Carr-Madan Formula

**Any European option can be replicated with portfolio of vanillas:**

$$
V(S_T) = V(F) + V'(F)(S_T - F) + \int_0^F V''(K) P(K) dK + \int_F^{\infty} V''(K) C(K) dK
$$

where:

- $V(S_T)$ = exotic option payoff
- $F$ = forward price
- $P(K), C(K)$ = puts and calls at strike $K$
- $V''(K)$ = second derivative of payoff

**In plain English:**

- Any payoff can be decomposed into:
  - Linear term (replicated by forwards)
  - Convex terms (replicated by options)
- Static portfolio of vanillas replicates any exotic
- **This is why static hedging works!**

### For Barriers

**Barrier options decompose into:**

1. Vanilla option
2. Plus/minus reflected option (around barrier)
3. Weights determined by barrier level

**Static portfolio replicates barrier exactly at:**

- Barrier level (key point)
- Expiration (final payoff)

**Not perfect between these points:**

- Tracking error exists mid-life
- But converges to zero at critical times
- **Trade-off accepted**

---

## Real-World Applications

### 1. Structured Products

**Investment banks selling:**

- Principal-protected notes
- Autocallables
- Range accruals
- **Use static hedges (too costly to rebalance)**

**Example:**

- Sell 3-year autocallable on S&P 500
- Static hedge with portfolio of vanilla options
- Rebalance quarterly (semi-static)
- Manage residual risk dynamically

### 2. Insurance Companies

**Life insurers with:**

- Guaranteed minimum death benefits
- Variable annuities with guarantees
- Long-dated liabilities
- **Use static or semi-static hedges**

**Why:**

- Very long horizons (20+ years)
- Transaction costs prohibitive
- Regulatory capital calculations
- Set-and-forget preferred

### 3. Pension Funds

**Hedging:**

- Liability duration
- Equity exposure
- Interest rate risk
- **Semi-static overlays common**

**Typical:**

- Rebalance annually
- Large notional
- Cannot rebalance frequently
- Static/semi-static natural fit

### 4. Exotic Option Dealers

**Market makers in:**

- Barrier options (FX, equity)
- Digital options
- Path-dependent exotics
- **Static hedges for barriers, dynamic for vanillas**

**Approach:**

- Static replicate barrier component
- Dynamic hedge vanilla component
- Hybrid strategy

---

## Practical Implementation

### Step 1: Determine Suitability

**Ask:**

- What's the time horizon? (> 6 months better)
- What's the option type? (Barriers/digitals best)
- What are transaction costs? (Higher costs favor static)
- Can I hold to expiry? (Yes needed)
- Is volatility low? (Lower vol favors static)

### Step 2: Design Static Hedge

**For vanilla option:**

- Delta hedge with underlying
- Hold to expiry
- Done

**For barrier option:**

- Calculate static replication portfolio
- Use Carr-Madan or barrier formula
- Construct vanilla option portfolio

**For digital option:**

- Create tight call/put spread
- Width determines payoff granularity
- Hold to expiry

### Step 3: Execute

**One-time trade:**

- Enter all positions simultaneously
- Use limit orders (control slippage)
- Document hedge ratio
- Set expiry management plan

### Step 4: Monitor (Passively)

**Don't rebalance, but do monitor:**

- Track P&L (mark-to-market)
- Measure tracking error
- Watch for structural changes
- **But don't trade!**

### Step 5: Exit

**At expiration:**

- Settle all positions
- Evaluate hedge effectiveness
- Calculate actual vs. expected tracking error
- Learn for next time

---

## What to Remember

### Core Concept

**Static hedging means: hedge once, hold to maturity, accept tracking error**

$$
\text{Static Hedge: Transaction Cost Savings} > \text{Tracking Error Cost}
$$

- Opposite of dynamic hedging
- Trade-off: cost vs. accuracy
- Works for certain applications

### The Key Trade-off

**Dynamic hedging:**

- High cost, low tracking error
- Continuous rebalancing
- Perfect in limit

**Static hedging:**

- Low cost, high tracking error
- No rebalancing
- Perfect at critical points only

**The decision depends on:**

- Transaction costs
- Time horizon
- Option type
- Volatility environment

### When to Use Static

**Best for:**

1. **Barrier options** (natural application)
2. **Digital options** (avoid gamma spike)
3. **Long time horizons** (cost savings compound)
4. **Portfolio insurance** (institutional preference)
5. **High transaction costs** (illiquid markets)

**Not for:**

1. Short-dated vanillas
2. Need to exit early
3. American options (early exercise)
4. High volatility (tracking error too large)

### Perfect Applications

**Barrier options:**

- Static replication with vanilla portfolio
- Industry standard
- Avoids rebalancing nightmare near barrier

**Digital options:**

- Static replication with tight spread
- Avoids infinite gamma
- Clean solution

**Long-dated puts (insurance):**

- Buy and hold protective puts
- No rebalancing
- Simple institutional hedge

### The Math

**For vanilla option held to expiry:**

$$
\text{Static Hedge: } \Delta_0 \text{ shares} + \text{Short Option} \to \text{P\&L} = 0 \text{ at } T
$$

**At expiration:**

- Stock P&L + Option P&L = 0
- Perfect hedge (regardless of path)
- **But not hedged mid-life!**

**For barrier option:**

$$
\text{Barrier} \approx \text{Vanilla}_1 \pm \text{Ratio} \times \text{Vanilla}_2
$$

- Static portfolio replicates barrier
- Weights determined by reflection principle
- Hold to expiry

### Your Complete Toolkit

**Hedging approaches across strategies:**

```
DYNAMIC (Continuous rebalancing):
├── Gamma Scalping
├── Vega Trading  
├── Dispersion Trading
└── Convertible Arb

STATIC (No rebalancing):
├── Barrier Options
├── Digital Options
└── Portfolio Insurance (buy & hold puts)

SEMI-STATIC (Rare rebalancing):
├── Calendar Spreads (rebalance at roll)
└── Long-term equity hedges (quarterly)

UNHEDGED:
└── Straddles/Strangles (accept directional risk)
```

**All have their place!**

### Practical Wisdom

**Static hedging works when:**

- Time horizon is long (> 6 months)
- Transaction costs are high
- Option type is path-dependent (barriers, digitals)
- Holding to expiration
- Simplicity valued

**Dynamic hedging better when:**

- Time horizon is short (< 3 months)
- Transaction costs are low
- Vanilla options
- Might exit early
- Want continuous delta-neutral

**Often use hybrid:**

- Static for barrier component
- Dynamic for vanilla component
- Semi-static (monthly rebalancing)
- **Practical middle ground**

### The Deep Insight

**Static vs. dynamic is a cost-accuracy trade-off:**

"In a frictionless world (no transaction costs), dynamic hedging is always better - it continuously maintains the hedge. But the real world has friction. Static hedging accepts imperfection mid-life to avoid the bleeding of continuous costs. For the right applications (barriers, long horizons), the cost savings far exceed the tracking error. It's not about being lazy - it's about being economically rational."

**Key lesson:**

- Don't blindly follow textbook (continuous hedging)
- Real-world constraints matter
- Transaction costs are real
- Static hedging is sophisticated, not crude
- **Choose the right tool for the job**

### Final Thought

**Static hedging reveals important truth:**

"The Black-Scholes world of continuous rebalancing is beautiful mathematics but impossible reality. Every hedge is discrete. Every rebalance has costs. Static hedging takes this to the extreme - rebalance zero times - and shows it can work! For barriers, digitals, and long-dated hedges, static is not just acceptable but often optimal. It's a reminder that practical finance requires balancing mathematical ideals with economic reality."

**Your hedging toolkit now includes:**

- ✓ Dynamic hedging (most strategies)
- ✓ Static hedging (barriers, digitals, insurance)
- ✓ Semi-static hedging (practical middle ground)
- ✓ Unhedged (straddles when accepting directional risk)

**Complete spectrum from pure static to pure dynamic!** 🎯📊

---

## Where This Fits in Your Curriculum

**This is another cross-cutting theme like theta/carry:**

**Placement options:**

**Option A: After Delta Hedging (Chapter 1.5)**
```
1. Delta Hedging (foundation - dynamic)
1.5. Static Hedging (alternative - static) ← Shows the contrast
2. Straddles (no hedging)
3. Gamma Scalping (dynamic applied)
...
```

**Option B: After all strategies (synthesis)**
```
...
9. Variance Swaps
10. Theta and Carry (time dimension)
11. Static Hedging (hedging approaches) ← Synthesis
```

**Option C: Standalone advanced chapter**
```
Part I: Core Strategies (1-9)
Part II: Cross-Cutting Themes
  - Theta and Carry
  - Static Hedging ← Advanced applications
  - Risk Management
```

**Recommendation: Option B or C** (after students understand dynamic hedging thoroughly, show the alternative)

**This completes your hedging dimension:**

- Dynamic: covered in 7+ strategies
- Static: covered here
- Semi-static: covered here
- Unhedged: straddles

**Students now understand the FULL SPECTRUM of hedging approaches!** 🎓
