# Path Dependence Basics


**Path-dependent options** are derivatives whose payoff depends not just on the final price of the underlying asset at expiration, but on the entire path the asset price took to get there, including features like maximum, minimum, average prices, or whether certain barriers were crossed during the option's life.

---

## The Core Insight


**The fundamental idea:**

- Standard options care only about final price
- Path-dependent options care about the journey
- The "how you got there" matters, not just "where you ended"
- Can create cheaper hedging and better-targeted exposures
- Require more sophisticated pricing and hedging
- History of the price path becomes a state variable

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/path_dependent_vs_vanilla.png?raw=true" alt="path_dependent_vs_vanilla" width="700">
</p>
**Figure 1:** Comparison of vanilla vs. path-dependent option payoffs showing how two price paths ending at the same final price can yield different payoffs for Asian options (average matters) and barrier options (whether barrier crossed matters).

**You're essentially asking: "What matters more—the destination or the journey?"**

---

## What Is Path Dependence?


### 1. Strong vs. Weak


**Two types of path dependence:**

**Weak path dependence:**
- Payoff depends on discrete events during option life
- Example: Barrier options (did price cross barrier?)
- Example: Lookback options (what was the max/min?)
- Can be tracked with finite state variables
- Computationally manageable

**Strong path dependence:**
- Payoff depends on continuous history
- Example: Asian options (what was average price?)
- Example: Timer options (accumulated variance)
- Requires tracking continuous path information
- Computationally intensive (Monte Carlo often needed)

**Mathematical distinction:**

**Weak:** Payoff $V(S_T, M)$ where $M = \max_{0 \leq t \leq T} S_t$ (single number)

**Strong:** Payoff $V(S_T, \bar{S})$ where $\bar{S} = \frac{1}{T}\int_0^T S_t dt$ (continuous integral)

### 2. Static vs. Dynamic Replication


**Can we replicate without trading?**

**Static replication (rare for path-dependent):**
- Buy-and-hold portfolio of vanilla options
- Works for some digital/barrier combinations
- Generally not possible for path-dependent options
- Exception: Some barrier options can be statically replicated

**Dynamic replication (standard for path-dependent):**
- Continuously adjust hedge portfolio
- Track evolving state variables (average, max, etc.)
- Requires frequent rebalancing
- Transaction costs matter a lot

**Why static replication usually fails:**

Path-dependent payoff at expiration depends on $S_t$ for all $t \in [0,T]$. A static portfolio of vanilla options only depends on $S_T$. Mathematically, the space of functions $V(S_0, S_1, ..., S_T)$ is much larger than $V(S_T)$, so vanilla options can't span path-dependent payoffs.

### 3. Memory in Pricing


**State variables beyond current price:**

Standard option pricing: $V = V(S, t)$ (current price, current time)

Path-dependent pricing: $V = V(S, t, X)$ where $X$ is memory:
- $X = \bar{S}$ (running average for Asian)
- $X = M$ (maximum so far for lookback)
- $X = \sigma^2_{\text{realized}}$ (variance for timer options)
- $X = \mathbb{1}_{\text{barrier crossed}}$ (indicator for barriers)

**Example - Asian option:**

At $t = T/2$:
- Current stock price: $S = 100$
- Running average: $\bar{S}_{0 \to T/2} = 95$

**Two traders with same stock price but different memory:**
- Trader A: Average so far = $95$ → Needs bigger rally to profit
- Trader B: Average so far = $90$ → Already closer to profit
- **Same $S$, different values!**

This is why path-dependent options are multidimensional in nature.

### 4. Volatility Smile Impact


**Path dependence affects implied volatility:**

**Observation:** Path-dependent options have different sensitivity to volatility skew than vanilla options.

**Asian options:**
- Averaging reduces effective volatility
- Less sensitive to volatility smile
- Implied vol is lower than ATM vanilla vol
- **Cheaper than vanilla** (averaging dampens volatility)

**Lookback options:**
- Max/min extremely sensitive to tail events
- More sensitive to volatility skew (cares about extremes)
- Implied vol higher than ATM vanilla vol
- **More expensive than vanilla** (extreme sensitivity)

**Barrier options:**
- Sensitivity depends on barrier location
- Near-the-money barriers: Very sensitive to smile
- Far OTM barriers: Less sensitive
- Can be cheaper OR more expensive than vanilla

### 5. Computation Methods


**How to price path-dependent options:**

**Monte Carlo simulation:**
- Simulate many price paths
- Calculate payoff for each path
- Average discounted payoffs
- **Pros:** Flexible, handles any path dependence
- **Cons:** Slow, convergence rate $O(1/\sqrt{N})$

**PDE methods (finite difference):**
- Solve partial differential equation numerically
- State space includes price AND memory variable
- Grid in $(S, X, t)$ space
- **Pros:** Fast for low-dimensional problems
- **Cons:** Curse of dimensionality (slow for many state variables)

**Closed-form approximations:**
- Analytical bounds or approximations
- Control variates (use vanilla option + correction)
- Moment matching
- **Pros:** Very fast
- **Cons:** Less accurate, limited applicability

**Tree methods:**
- Binomial/trinomial trees with path memory
- Recombining where possible
- **Pros:** Intuitive, American exercise easily handled
- **Cons:** Exponential growth in nodes for true path dependence

### 6. Transaction Costs


**Path dependence amplifies trading costs:**

**Why:**
- Dynamic hedging requires frequent rebalancing
- More state variables → More complex hedge ratios
- Memory changes continuously → Hedge changes continuously
- Higher gamma/vanna → Larger rehedging amounts

**Example - Asian option hedging:**

**Vanilla option hedging:**
- Rehedge when $\Delta$ changes significantly
- Maybe 10-20 trades over option life

**Asian option hedging:**
- Must rehedge as BOTH $S$ and $\bar{S}$ change
- Average changes every instant (even if $S$ constant!)
- Maybe 50-100 trades over option life
- **2-5× more transaction costs**

**Impact on profitability:**
- Market makers charge wider bid-ask for path-dependent options
- Retail investors pay this premium
- Academic "fair value" ≠ market price due to transaction costs

### 7. Early Exercise Considerations


**American path-dependent options:**

**Complexity multiplier:** Early exercise adds another dimension

**Example - American Asian call:**

Decision at time $t$:
- Current stock price: $S_t$
- Average so far: $\bar{S}_{0 \to t}$
- Time remaining: $T - t$

**Should you exercise?**

**If $S_t > \bar{S}_{0 \to t}$:**
- Exercising now: Payoff = $S_t - \bar{S}_{0 \to t}$
- Waiting: Might increase average (if stock stays high)
- But time value of money favors early exercise
- **Complex optimal stopping problem**

**Pricing method:** Longstaff-Schwartz (least-squares Monte Carlo) or finite difference with free boundary

---

## Key Terminology


**Monitoring Frequency:**
- Continuous: Path observed continuously (theoretical)
- Discrete: Path observed at fixed dates (realistic)
- Daily, weekly, monthly observations
- Affects payoff and pricing

**Averaging Method:**
- Arithmetic average: $\frac{1}{n}\sum_{i=1}^n S_i$ (most common)
- Geometric average: $\left(\prod_{i=1}^n S_i\right)^{1/n}$ (less common)
- Weighted average: $\sum_{i=1}^n w_i S_i$ (custom weights)

**Strike Type:**
- Fixed strike: $\max(\bar{S} - K, 0)$ (predetermined)
- Floating strike: $\max(S_T - \bar{S}, 0)$ (average becomes strike)
- Both versions trade actively

**Barrier Type:**
- Up-and-in: Activates if price rises to barrier
- Up-and-out: Deactivates if price rises to barrier
- Down-and-in: Activates if price falls to barrier
- Down-and-out: Deactivates if price falls to barrier

**Rebate:**
- Payment if barrier option knocked out
- Compensates holder for losing option
- Can be paid at knockout or at maturity
- Adds complexity to pricing

**Reset Feature:**
- Lookback max/min can reset periodically
- Cliquet-style periodic locking of gains
- Reduces cost vs. full lookback
- Popular in structured products

---

## Asian Options


### 1. Definition and Payoff


**Average price options:**

**Arithmetic Asian call (fixed strike):**

$$
V_T = \max\left(\bar{S} - K, 0\right)
$$

where $\bar{S} = \frac{1}{n}\sum_{i=1}^n S_{t_i}$ (discrete observations)

**Floating strike Asian call:**

$$
V_T = \max\left(S_T - \bar{S}, 0\right)
$$

**Continuous average:**

$$
\bar{S} = \frac{1}{T}\int_0^T S_t \, dt
$$

### 2. Why Use Asian Options?


**Advantages:**

**Cheaper than vanilla:**
- Averaging reduces volatility
- Payoff smoothed by averaging process
- Typically 20-40% cheaper than equivalent vanilla option
- Good for budget-constrained hedgers

**Manipulation-resistant:**
- Payoff depends on average, not single price
- Hard to manipulate many observations
- Used for thinly-traded underlyings
- Common in commodity markets

**Natural for periodic cash flows:**
- Match payoff to business reality
- Example: Monthly revenue hedging
- Average monthly price more relevant than final price
- Reduces basis risk

**Example:**

Airlines hedging fuel costs:
- Need to hedge average monthly jet fuel price
- Not just final month price
- Asian option perfectly matches exposure
- Vanilla option has basis risk (final ≠ average)

### 3. Pricing Methods


**No closed form for arithmetic average:**

**Geometric average (closed form exists):**

For geometric Asian, Black-Scholes formula applies with adjusted volatility:

$$
\sigma_{\text{geo}} = \frac{\sigma}{\sqrt{3}}
$$

**Why $\sqrt{3}$:** Variance of geometric average is 1/3 of variance of terminal price.

**Arithmetic average (numerical methods):**

**Curran approximation:**
- Replace arithmetic average with lognormal distribution
- Match first two moments
- Use Black-Scholes with adjusted parameters
- Error typically < 1%

**Monte Carlo:**
- Simulate $N$ paths: $S_0, S_1, ..., S_n$
- Calculate average for each path: $\bar{S}^{(i)}$
- Calculate payoff for each path: $V^{(i)} = \max(\bar{S}^{(i)} - K, 0)$
- Discount and average: $V_0 = e^{-rT} \frac{1}{N}\sum_{i=1}^N V^{(i)}$

**PDE method:**
- State variables: $(S, \bar{S}, t)$
- PDE: $\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} + \frac{S - n\bar{S}}{T - t}\frac{\partial V}{\partial \bar{S}} = rV$
- Note extra term $\frac{\partial V}{\partial \bar{S}}$ (memory evolution)
- Solve backward from $T$ to $0$

### 4. Greeks for Asian Options


**Delta:**

$$
\Delta_{\text{Asian}} = \frac{\partial V}{\partial S} + \frac{\partial V}{\partial \bar{S}} \cdot \frac{\partial \bar{S}}{\partial S}
$$

**Interpretation:**
- Two effects: Direct (current price) and indirect (through average)
- Early in life: Mostly direct effect ($\bar{S}$ not yet much history)
- Late in life: Mostly indirect effect (average dominated by history)

**Example:**

**Day 1 of 100-day Asian:**
- $\frac{\partial \bar{S}}{\partial S} \approx \frac{1}{100}$ (today's price is 1/100 of average)
- $\Delta_{\text{Asian}} \approx \Delta_{\text{vanilla}}$ (small indirect effect)

**Day 99 of 100-day Asian:**
- $\frac{\partial \bar{S}}{\partial S} \approx \frac{1}{100}$ (still 1/100)
- But $\frac{\partial V}{\partial \bar{S}}$ is large (payoff almost determined)
- $\Delta_{\text{Asian}} \ll \Delta_{\text{vanilla}}$ (average already "locked in")

**Vega:**

$$
\text{Vega}_{\text{Asian}} < \text{Vega}_{\text{vanilla}}
$$

Because averaging reduces effective volatility.

**Rule of thumb:** Vega of Asian ≈ 60-70% of vanilla vega

### 5. Trading Strategies


**Buy Asian calls when:**
- Need to hedge average price exposure (natural matching)
- Want cheaper option than vanilla (budget constraint)
- Expect steady trends (averaging helps with trending markets)
- Low volatility environment (averaging less disadvantageous)

**Sell Asian calls when:**
- Expect high volatility (vanilla would be more valuable)
- Expect late spike in price (Asian benefits less from this)
- Can charge high implied volatility (implied > realized)

**Asian vs. Vanilla spread:**
- Long vanilla call + Short Asian call (same strike)
- Profit if: Large late move (vanilla benefits, Asian doesn't)
- Risk: Cost of vanilla - premium of Asian (net debit)

---

## Barrier Options


### 1. Definition and Types


**Options that activate or deactivate at barriers:**

**Up-and-out call:**

$$
V_T = \begin{cases}
\max(S_T - K, 0) & \text{if } \max_{0 \leq t \leq T} S_t < H \\
0 & \text{if } \max_{0 \leq t \leq T} S_t \geq H
\end{cases}
$$

where $H$ is the barrier (above current price)

**Down-and-out put:**

$$
V_T = \begin{cases}
\max(K - S_T, 0) & \text{if } \min_{0 \leq t \leq T} S_t > H \\
0 & \text{if } \min_{0 \leq t \leq T} S_t \leq H
\end{cases}
$$

where $H$ is the barrier (below current price)

**Eight standard types:**
- Up-and-out call / put
- Up-and-in call / put
- Down-and-out call / put
- Down-and-in call / put

**Parity relation:**

$$
\text{Vanilla} = \text{Knock-out} + \text{Knock-in}
$$

Example: $\text{Call} = \text{Down-and-out call} + \text{Down-and-in call}$

### 2. Pricing Formulas


**Closed-form solutions exist!**

**Down-and-out call (Black-Scholes framework):**

$$
C_{\text{DO}} = C_{\text{vanilla}} - \left(\frac{H}{S_0}\right)^{2\lambda} C_{\text{reflected}}
$$

where:
- $C_{\text{vanilla}}$ = Standard Black-Scholes call
- $\lambda = \frac{r + \sigma^2/2}{\sigma^2}$
- $C_{\text{reflected}}$ = Call with strike and spot reflected around barrier

**Full formula (Merton 1973, Reiner-Rubinstein 1991):**

$$
C_{\text{DO}} = S_0 N(x_1) - K e^{-rT} N(x_1 - \sigma\sqrt{T}) - S_0 \left(\frac{H}{S_0}\right)^{2\lambda} N(y_1) + K e^{-rT} \left(\frac{H}{S_0}\right)^{2\lambda - 2} N(y_1 - \sigma\sqrt{T})
$$

where:
$$
\begin{align*}
x_1 &= \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} \\
y_1 &= \frac{\ln(H^2/(S_0 K)) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}
\end{align*}
$$

**Practical:** Use software (QuantLib, Bloomberg, etc.) - formulas are complex!

### 3. Why Use Barrier Options?


**Cost reduction:**

**Example:**

Stock at $100, want call option

**Vanilla call:** Strike $100, 1 year, premium = $10

**Up-and-out call:** Strike $100, barrier $120, 1 year, premium = $6

**Savings:** 40% cheaper!

**Trade-off:** If stock hits $120, option vanishes (even if it later falls back)

**When to use barriers:**
- Strong view that barrier won't be hit
- Want cheaper hedge (willing to accept knockout risk)
- Natural barrier exists (e.g., leveraged position liquidates at price level)

**Target redemption structures:**
- Use barriers to cap maximum payout
- Reduce issuer cost
- Pass savings to investor (higher coupons)

### 4. Risk Characteristics


**Discontinuous Greeks near barrier:**

**Delta explodes near barrier:**
- Far from barrier: Delta similar to vanilla
- Near barrier: Delta → ∞ (theoretically)
- Why: Small move determines knockout (huge impact)

**Gamma singularity:**
- $\Gamma \to \infty$ as $S \to H$
- Hedging becomes impossible near barrier
- Market makers widen spreads dramatically
- **Extreme rehedging costs**

**Example:**

Down-and-out call, barrier at $95, stock at $96

**Greeks:**
- Delta: 0.8 (vs. 0.5 for vanilla)
- Gamma: 0.5 (vs. 0.05 for vanilla) - **10× higher!**
- Vega: 0.3 (vs. 0.4 for vanilla)

**Next day, stock at $95.50:**
- Delta now: 1.5 (increased from 0.8!)
- Must buy 0.7 more shares per option to hedge
- If position = 10,000 contracts, must buy 70,000 shares
- **Market impact + slippage = huge cost**

### 5. Barrier Monitoring


**Continuous vs. discrete:**

**Continuous monitoring (theoretical):**
- Barrier checked at every instant
- Higher knockout probability
- More expensive to provide
- Formula assumes this

**Discrete monitoring (reality):**
- Barrier checked at specific times (daily close, etc.)
- Lower knockout probability (price can spike intraday)
- Cheaper for buyer
- Requires adjusted pricing

**Price difference:**

Discrete-monitored barrier option ≈ 5-15% more expensive than continuous (cheaper to knock out)

**Example:**

Stock at $100, down-and-out call with barrier at $90

**Continuous monitoring:** Premium = $8
**Daily monitoring:** Premium = $9.20 (15% higher)

Why: Stock can dip to $89 intraday but close at $91 (survives under daily monitoring)

### 6. Rebates


**Compensation for knockout:**

**Rebate structure:**

If knocked out, option holder receives rebate $R$

**Payoff:**

$$
V_T = \begin{cases}
\max(S_T - K, 0) & \text{if barrier not hit} \\
R & \text{if barrier hit}
\end{cases}
$$

**Example:**

Down-and-out call: Strike $100, barrier $90, rebate $5

**Scenario 1:** Stock stays above $90, ends at $110
- Payoff: $110 - $100 = $10$ ✓

**Scenario 2:** Stock hits $90 (knocked out)
- Payoff: $5$ rebate (vs. $0 without rebate)

**Pricing with rebate:**

$$
V_{\text{barrier + rebate}} = V_{\text{barrier}} + R \times \mathbb{P}(\text{barrier hit})
$$

**Why use rebates:**
- Soften blow of knockout
- Make barrier options more attractive
- Issuer can still save money vs. vanilla (rebate < option value)

### 7. Double Barriers


**Two barriers (upper and lower):**

**Double knock-out call:**

$$
V_T = \begin{cases}
\max(S_T - K, 0) & \text{if } L < S_t < U \text{ for all } t \\
0 & \text{if } S_t \leq L \text{ or } S_t \geq U \text{ for any } t
\end{cases}
$$

**Example:**

Stock at $100, double knock-out call

- Lower barrier: $L = 90$
- Upper barrier: $U = 110$
- Strike: $K = 100$

**Payoff:** Only if stock stays in $[90, 110]$ range entire time

**Why use:**
- Much cheaper than vanilla (both sides can knock out)
- Bet on range-bound market
- Common in FX markets (corridor options)

**Pricing:** Numerical methods (Monte Carlo, PDE) - no simple closed form

---

## Lookback Options


### 1. Definition


**Payoff depends on maximum or minimum:**

**Fixed strike lookback call:**

$$
V_T = \max\left(\max_{0 \leq t \leq T} S_t - K, 0\right)
$$

You get to "look back" and buy at strike $K$, but payoff based on best price achieved.

**Floating strike lookback call:**

$$
V_T = S_T - \min_{0 \leq t \leq T} S_t
$$

You get to "look back" and buy at the LOWEST price observed (floating strike).

**Lookback put (floating strike):**

$$
V_T = \max_{0 \leq t \leq T} S_t - S_T
$$

You get to "look back" and sell at the HIGHEST price observed.

### 2. Why Lookback Options?


**Perfect hindsight:**

- Payoff as if you knew the future
- Always exercise at optimal point
- Removes timing risk
- **Very expensive** (20-50% more than vanilla)

**Example:**

Stock path: $100 → $110 → $95 → $105$

**Vanilla call** (strike $100$):
- Payoff: $\max(105 - 100, 0) = $5$

**Lookback call** (floating strike):
- Strike = min($100, $110, $95, $105$) = $95$
- Payoff: $105 - 95 = $10$
- **Double the vanilla payoff!**

### 3. Closed-Form Pricing


**Formulas exist (Goldman-Sosin-Gatto 1979):**

**Floating strike lookback call:**

$$
C_{\text{LB}} = S_0 N(a_1) - e^{-rT} S_{\min} N(a_2) + S_0 \frac{\sigma^2}{2r} \left[ N(-a_1) - e^{-rT} \left(\frac{S_0}{S_{\min}}\right)^{-2r/\sigma^2} N(-a_3) \right]
$$

where:
$$
\begin{align*}
a_1 &= \frac{\ln(S_0/S_{\min}) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} \\
a_2 &= a_1 - \sigma\sqrt{T} \\
a_3 &= \frac{\ln(S_0/S_{\min}) + (-r + \sigma^2/2)T}{\sigma\sqrt{T}}
\end{align*}
$$

**Practical:** Again, use software - formulas are complex.

### 4. Greeks


**Delta of lookback:**

$$
\Delta_{\text{LB}} > \Delta_{\text{vanilla}}
$$

**Why:** Lookback always "in-the-money" in some sense (best price guaranteed)

**Gamma:**

$$
\Gamma_{\text{LB}} > \Gamma_{\text{vanilla}}
$$

**Why:** Payoff highly sensitive to new extremes

**Vega:**

$$
\text{Vega}_{\text{LB}} \gg \text{Vega}_{\text{vanilla}}
$$

**Why:** Higher volatility → More extreme max/min → Much higher payoff

**Rule of thumb:** Vega of lookback ≈ 150-200% of vanilla vega

### 5. Partial Lookback


**Reduce cost with caps/floors:**

**Capped lookback call:**

$$
V_T = \min\left(\max_{0 \leq t \leq T} S_t - K, \, C\right)
$$

Where $C$ is the cap (maximum payoff).

**Example:**

Lookback call on stock at $100

**Full lookback:** Payoff = $S_{\max} - 100$ (unbounded)
**Capped lookback:** Payoff = $\min(S_{\max} - 100, 20)$ (max $20)

**Cost:**
- Full lookback: $25
- Capped at $20: $18 (28% cheaper)

**Trade-off:** Give up extreme upside for cost savings

### 6. Shout Options


**One-time reset:**

**Payoff:** At any point before expiration, holder can "shout" and lock in the current intrinsic value as a floor.

$$
V_T = \max\left(S_T - K, \, S_{\text{shout}} - K\right)
$$

**Example:**

Stock path: $100 → $130 → $110$

**Vanilla call** (strike $100$): Payoff = $110 - 100 = $10$

**Shout option:** Shouted at $130
- Floor locked in: $130 - 100 = $30$
- Final: $110 - 100 = $10$
- **Payoff: $\max(10, 30) = $30$**

**Cost:** Shout ≈ 10-20% more than vanilla (much cheaper than full lookback)

**When to use:**
- Want partial lookback (one chance to lock profit)
- Budget doesn't allow full lookback
- Expect one big move, then reversal

---

## Common Mistakes


### 1. Ignoring Monitoring Frequency


**Continuous vs. discrete assumption:**

- **Mistake:** Price barrier option assuming continuous monitoring
- **Why it fails:** Reality is discrete (daily close, etc.), affects probability
- **Fix:** Adjust pricing for actual monitoring frequency
- **Real cost:** Overpay by 5-15% if assuming continuous when actually discrete

**Example:**

Down-and-out call, barrier at $90, stock at $100

**Continuous monitoring price:** $8.50
**Daily monitoring price:** $9.20
**Reality:** Monitoring is daily

**Error:** If you paid $8.50 thinking continuous, you underpaid for what you got. Seller loses money. If you're the seller and priced at $8.50, **you lose $0.70 per contract**.

### 2. Barrier Option Delta Hedging


**Impossible near barriers:**

- **Mistake:** Try to delta hedge barrier option near barrier
- **Why it fails:** Delta explodes, changes faster than you can trade
- **Fix:** Exit position well before reaching barrier (e.g., 2-5% buffer)
- **Real cost:** Unhedgeable losses if barrier approached

**Example:**

Short 1000 down-and-out calls, barrier $95, stock at $96

**Day 1:** Delta = 0.7, hedge by buying 700 shares per contract = 700,000 shares
**Day 2:** Stock falls to $95.50, delta now 1.3
- Need to buy (1.3 - 0.7) × 1000 × 100 = 60,000 more shares
**Day 3:** Stock at $95.20, delta now 2.5
- Need to buy (2.5 - 1.3) × 1000 × 100 = 120,000 more shares

**Problem:** Buying huge size in falling market
- Market impact: Pushes price up 1-2%
- Slippage: $1-2 per share
- **Total cost: $120K-$240K** from gamma bleed

**Lesson:** Don't hold barrier options near barriers, especially as seller!

### 3. Asian Option Timing Error


**Early average vs. late average:**

- **Mistake:** Buy Asian option late in its life (most of average already determined)
- **Why it fails:** Option has little sensitivity to future prices (optionality lost)
- **Fix:** Buy Asian options early, when average still flexible
- **Real cost:** Pay option premium for minimal exposure

**Example:**

100-day Asian call, stock at $100, average so far = $95

**Day 10:** Average = $101 (10 days at ~$101)
- Remaining 90 days can significantly change average
- Asian call has substantial optionality

**Day 90:** Average = $99 (90 days averaging to $99)
- Remaining 10 days barely move average
- Need stock at $200+ in last 10 days to make average > $100
- **Asian call almost worthless** (average "locked in")

**Mistake:** Bought Asian call on Day 90 for $2
**Reality:** Intrinsic value ≈ $0, time value ≈ $0 (average locked)
**Loss:** Entire $2 premium wasted

### 4. Forgetting Path Can't Be Undone


**History is permanent:**

- **Mistake:** Think barrier option that knocked out can "knock back in"
- **Why it fails:** Once knocked out, it's dead forever
- **Fix:** Understand knockout is permanent (path dependence!)
- **Real cost:** Hold worthless position thinking it might revive

**Example:**

Down-and-out call, barrier $90

**Week 1:** Stock at $100 → $92 (still alive)
**Week 2:** Stock dips to $89 briefly (**knocked out!**)
**Week 3:** Stock rallies to $110

**Mistake:** Think "stock is back above barrier, option is back!"
**Reality:** Option knocked out in Week 2, stays worthless
**Loss:** Hold dead option instead of reinvesting

### 5. Lookback Vega Underestimation


**Extreme vol sensitivity:**

- **Mistake:** Sell lookback option treating vega like vanilla
- **Why it fails:** Lookback vega is 2-3× vanilla vega
- **Fix:** Hedge vega explicitly (buy vanilla options for vega)
- **Real cost:** Unhedged losses when vol spikes

**Example:**

Sell lookback call for $25

**Greeks:**
- Delta: Hedged with stock ✓
- Vega: $50 per 1% vol (ignored ✗)

**Volatility spikes from 20% to 30%:**
- Vega loss: $50 × 10% = $500 per contract
- If sold 100 contracts: **$50,000 loss** from vega

**Fix:** Buy vanilla options to hedge vega
- Buy vanilla calls worth $30 vega
- Remaining $20 vega exposure manageable

### 6. Over-Complicating Structures


**Complexity for complexity's sake:**

- **Mistake:** Combine multiple path-dependent features (barrier + lookback + Asian)
- **Why it fails:** Impossible to price accurately, model risk explodes
- **Fix:** Use simplest structure that achieves goal
- **Real cost:** Mispricing, impossible hedging, disputes at maturity

**Example:**

**"Exotic masterpiece":**
- Asian call based on arithmetic average
- With lookback feature (strike = minimum average)
- With barrier (knocks out if maximum average > $120)
- Observed weekly

**Problems:**
- How to price? Monte Carlo with huge variance (slow convergence)
- How to hedge? Greeks undefined (discontinuous everywhere)
- Settlement disputes: "Was weekly close $119.99 or $120.01?"
- Model risk: Pricing assumptions matter hugely

**Better:**
- Simple Asian call achieves 80% of desired exposure
- 90% cheaper to engineer and hedge
- Clear pricing and settlement

---

## Best vs. Worst Case


### 1. Best Case: Success


**Corporate hedging with Asian options:**

**Setup:**
- Airline needs to hedge average monthly jet fuel price for next 12 months
- Monthly consumption: 1M gallons
- Current price: $3/gallon
- Budget: $200K for hedging

**Vanilla option approach:**
- Buy 12 monthly call options (one per month)
- Each covers 1M gallons at $3 strike
- Cost per call: ~$20K
- **Total cost: $240K** (over budget!)

**Asian option approach:**
- Buy single 12-month Asian call
- Average monthly price, covers 12M gallons
- Strike: $3
- **Cost: $150K** (25% cheaper due to averaging)

**Outcome Year 1:**

**Fuel prices:**
- Months 1-6: $3.20 average (up 6.7%)
- Months 7-12: $2.80 average (down 6.7%)
- **Annual average: $3.00** (flat!)

**Vanilla option result:**
- First 6 months: Exercised calls, saved $0.20 × 6M gallons = $1.2M
- Last 6 months: Calls expired worthless (price below $3)
- **Net savings: $1.2M - $240K premium = $960K**

**Asian option result:**
- Annual average = $3.00 = strike
- Option expires at-the-money (worthless)
- **Net savings: -$150K** (lost premium)

**Wait, vanilla won?**

**But consider Year 2:**

**Fuel prices:**
- Steady increase: $2.80 → $3.50 (25% rise)
- Monthly average increases steadily

**Vanilla option result:**
- Buy 12 new calls at current price ($3.50 strike)
- Cost: $300K (much more expensive!)
- Savings: Depends on future prices

**Asian option result:**
- Average for year: $3.15
- Option pays: ($3.15 - $3.00) × 12M = $1.8M
- **Net savings: $1.8M - $150K = $1.65M**
- **Asian option won big!**

**Lesson:** Asian options perfect for hedging average exposure, especially over long periods. Cheaper AND better match to actual exposure.

### 2. Worst Case: Failure


**Barrier option disaster:**

**Setup:**
- Hedge fund selling barrier options to juice returns
- "Pick up nickels in front of steamroller"
- Sells 10,000 down-and-out puts on S&P 500

**Structure:**
- S&P at 4,000
- Strike: 3,800 (5% OTM)
- Barrier: 3,600 (10% down from current)
- Premium collected: $5 per contract = $5M total
- Reasoning: "Market won't fall 10% before expiration (3 months)"

**Month 1: Market steady at 4,000**
- Theta decay: Earning $50K/day
- Feeling like genius
- **Cumulative P&L: +$1.5M**

**Month 2: Gradual decline to 3,700**
- Still above barrier (safe!)
- But delta increasing (going ITM)
- Hedging by shorting S&P futures
- **Cumulative P&L: +$2M** (theta still winning)

**Month 3: Flash crash**

**Day 1 of Month 3: Gap down to 3,550 overnight (barrier breached!)**

**Immediate effects:**
- All 10,000 puts knocked out (become worthless to buyers)
- Hedge fund celebrates: "Barrier saved us!"
- **But wait...**

**The hedge position:**
- Had been short S&P futures to delta hedge (when stock at 3,700)
- Short position: 500,000 shares equivalent
- S&P fell from 3,700 to 3,550 (4% drop)
- **Hedge profit: 500,000 × $150 = $75M... but**

**The disaster:**
- Puts knocked out → No more short put position
- But still short 500,000 shares from hedging!
- Now naked short in crashed market

**Day 2-30: Market rebounds to 3,900**
- Naked short position: Loss = 500,000 × (3,900 - 3,550) = $175M
- Premium collected: +$5M
- Hedge profits (up to barrier): +$10M
- **Net loss: -$160M**

**How this happened:**
- Delta of barrier option is discontinuous at barrier
- When barrier hit, delta → 0 instantly
- But hedge position doesn't disappear
- Left with unhedged position at WORST time

**Post-mortem:**
- Fund down 80% (started with $200M)
- Investors redeem
- Fund liquidates
- Founder's career destroyed

**Lessons:**
1. Barrier options have discontinuous risk (not just at expiration!)
2. Hedging near barriers is impossible
3. Risk-free premium doesn't exist
4. Complexity hides risk, doesn't eliminate it

---

## Risk Management Rules


### 1. Path Variable Limits


**Track state variables:**

For Asian options:
$$
\text{Track } (\bar{S}_t, S_t, t)
$$

For lookback options:
$$
\text{Track } (S_{\min}, S_{\max}, S_t, t)
$$

For barrier options:
$$
\text{Track } (\mathbb{1}_{\text{barrier hit}}, S_t, t)
$$

**Update frequency:**
- Real-time for barriers near breach
- Daily for Asian/lookback
- Use automated systems (manual tracking error-prone)

### 2. Buffer Zones for Barriers


**Never let price reach barrier:**

$$
\text{Exit threshold} = \text{Barrier} \pm 2\sigma\sqrt{\Delta t}
$$

**Example:**

Down-and-out call, barrier $90, daily vol = 1.5%

**Buffer:** $90 × (1 + 2 × 0.015) = $92.70$

**Rule:** If stock falls below $92.70, exit all positions (don't wait for $90)

**Why:** Price can gap through $90, leaving unhedgeable exposure

### 3. Complexity Budget


**Limit path-dependent features:**

**Maximum complexity score:**
- Base option: 1 point
- + Barrier: +3 points
- + Asian: +2 points
- + Lookback: +4 points
- + American exercise: +2 points

**Hard limit:** 6 points per option

**Example:**

- Barrier + Asian = 3 + 2 = 5 points ✓
- Barrier + Lookback = 3 + 4 = 7 points ✗ (too complex)

**Rationale:** Higher complexity = higher model risk, hedging risk, settlement disputes

### 4. Monte Carlo Convergence


**Ensure sufficient samples:**

$$
\text{Standard Error} \propto \frac{1}{\sqrt{N}}
$$

**Requirements:**
- Minimum 10,000 paths for pricing
- Minimum 100,000 paths for Greeks
- Use variance reduction techniques (antithetic, control variates)

**Check convergence:**

Run pricing multiple times with different seeds:
- If prices vary by >1%, increase $N$
- Target: Standard error < 0.5% of option value

### 5. Scenario Analysis


**Stress test path-dependent features:**

**Required scenarios:**
1. **Linear path:** Steady trend up/down
2. **Spike path:** Late sudden move
3. **Oscillating path:** Up-down-up-down
4. **Gap path:** Multiple gaps (barriers!)
5. **High vol path:** Random walk with 2× volatility
6. **Low vol path:** Random walk with 0.5× volatility

**For each scenario:**
- Calculate P&L
- Calculate Greeks
- Check if within risk limits
- Maximum scenario loss ≤ 10% of capital

---

## Real-World Examples


### 1. FX Hedging with Asian Options


**Exporter hedging:**

**Setup:**
- US exporter receives €10M monthly for next 12 months
- Current EUR/USD: 1.10
- Need to hedge average annual exchange rate

**Asian option hedge:**
- Buy 12-month Asian put on EUR/USD
- Average fixings: Monthly
- Strike: 1.10
- Notional: €120M (12 months × €10M)
- Premium: 2% = $2.64M

**Outcome:**

**EUR/USD path:**
- Months 1-3: 1.12 (stable)
- Months 4-6: 1.08 (declining)
- Months 7-9: 1.05 (weak EUR)
- Months 10-12: 1.03 (weaker)
- **Average: 1.07**

**Without hedge:**
- Revenue: €120M × 1.07 = $128.4M

**With Asian put hedge:**
- Revenue: €120M × 1.07 = $128.4M
- Put payoff: (1.10 - 1.07) × €120M = $3.6M
- Premium paid: -$2.64M
- **Net: $129.36M** (vs. $132M if spot stayed 1.10)

**Benefit:** Protected downside, limited cost

### 2. Commodity Producer Using Lookback


**Gold miner:**

**Setup:**
- Mining 100,000 oz gold over next year
- Monthly production: 8,333 oz
- Want to lock in high price

**Lookback put:**
- Floating strike lookback put
- Ensures sale at highest price over year
- Premium: 8% of notional = $150M × 8% = $12M

**Gold price path:**
- Start: $1,500/oz
- Month 3: $1,700/oz (spike on geopolitical fears)
- Month 6: $1,600/oz (stabilize)
- Month 9: $1,400/oz (decline)
- End: $1,450/oz (low)

**Without lookback:**
- Revenue: 100,000 oz × average $1,533/oz = $153.3M

**With lookback put:**
- Strike = max price = $1,700/oz (Month 3)
- Payoff: (1,700 - 1,450) × 100,000 = $25M
- Premium: -$12M
- Revenue: $145M (spot sale) + $25M (put) - $12M (premium) = $158M

**Benefit:** Captured the spike at $1,700 even though ended at $1,450

### 3. Autocallable Note Disaster


**Retail structured product:**

**Setup:**
- Note linked to bank stock (Lehman Brothers)
- Autocallable: Matures early if stock up
- Barrier: Downside protection at 70%
- Issue price: Stock at $100

**Year 1:** Stock at $105 → Note calls, investors receive 110% ✓

**New issue (2007):**
- Same structure, stock at $100
- Issued just before financial crisis

**Year 1 (2008):** Stock crashes to $30 (70% barrier breached)
- Investors lose 70% (same as stock)
- No autocall (stock never rallied)
- **Many retail investors lost life savings**

**Lesson:**
- Barrier options can have catastrophic outcomes
- Autocallable structures hide tail risk
- Retail investors didn't understand barrier feature
- Mass lawsuits followed (banks paid billions in settlements)

### 4. Corporate Bond with Lookback Feature


**Reverse convertible:**

**Setup:**
- Bond linked to worst-of 3 stocks (AAPL, MSFT, GOOGL)
- Coupon: 15% annually
- Maturity: 3 years
- Lookback: Strike = 80% of lowest price in last month

**Year 1-2:** All stocks up, investors collect 15% ✓

**Year 3, Month 11:** Flash crash
- AAPL drops to $120 (was $180)
- Lookback strike: 80% × $120 = $96

**Year 3, Month 12:**
- AAPL recovers to $150
- But strike already locked at $96
- **Conversion:** Receive AAPL shares at $96 (vs. $150 market)
- **Loss:** $150 - $96 = $54 per share (36% loss)

**Investors:**
- Received 45% in coupons over 3 years
- Lost 36% on conversion
- **Net: +9%** (vs. 50% gain if held stocks directly)

**Lesson:** Lookback features can lock in worst outcomes, even if market recovers

---

## Practical Steps


### 1. Identify Path Dependence


**Before trading, ask:**

1. Does payoff depend on terminal price only?
   - Yes → Vanilla option
   - No → Path-dependent (continue)

2. What history matters?
   - Average → Asian option
   - Maximum/minimum → Lookback option
   - Barrier crossed → Barrier option
   - Multiple features → Exotic combo

3. Can I use vanilla approximation?
   - Asian with long tenor → Approximate with vanilla
   - Barrier far OTM → Approximate with vanilla
   - Otherwise → Need path-dependent pricing

### 2. Choose Monitoring Frequency


**Trade-off: Accuracy vs. cost**

**Continuous monitoring:**
- Theoretical construct
- Highest knockout probability
- Most expensive for buyer
- Use for rough estimates

**Daily monitoring:**
- Most common in practice
- Reasonable approximation
- Much cheaper than continuous
- Easy to verify (closing prices)

**Weekly/monthly monitoring:**
- Lowest knockout probability
- Cheapest for buyer
- Higher model risk
- Used for long-dated options

**Decision rule:**
- < 3 months: Daily monitoring
- 3-12 months: Weekly monitoring
- > 12 months: Monthly monitoring

### 3. Estimate Fair Value


**Pricing workflow:**

1. **Vanilla benchmark:**
   - Price equivalent vanilla option
   - This is upper bound for Asians, reference for barriers

2. **Path-dependent adjustment:**
   - Asian: Multiply vanilla price by 0.7-0.85
   - Barrier (far OTM): Multiply vanilla by 0.6-0.8
   - Lookback: Multiply vanilla by 1.3-1.6

3. **Numerical pricing:**
   - Use Monte Carlo with ≥10,000 paths
   - Or finite difference PDE
   - Or closed-form if available (rare)

4. **Bid-ask adjustment:**
   - Add 5-10% for vanilla options
   - Add 10-20% for path-dependent
   - Reflects hedging difficulty

### 4. Implement Monitoring System


**Track state variables:**

**For Asian options:**
```python
class AsianOption:
    def __init__(self):
        self.observations = []
        self.average = 0
    
    def add_observation(self, price, date):
        self.observations.append((price, date))
        self.average = np.mean([p for p, d in self.observations])
    
    def payoff(self, final_price, strike):
        return max(self.average - strike, 0)
```

**For barrier options:**
```python
class BarrierOption:
    def __init__(self, barrier, barrier_type):
        self.barrier = barrier
        self.barrier_type = barrier_type  # 'down-and-out', etc.
        self.knocked_out = False
    
    def check_barrier(self, price):
        if self.barrier_type == 'down-and-out' and price <= self.barrier:
            self.knocked_out = True
        # ... other types
    
    def payoff(self, final_price, strike):
        if self.knocked_out:
            return 0
        return max(final_price - strike, 0)
```

### 5. Hedge Dynamically


**Greeks-based hedging:**

1. **Calculate Greeks:**
   - Use numerical methods (finite difference, Monte Carlo)
   - Update daily (or more frequent near barriers)

2. **Delta hedge:**
   - Buy/sell underlying to neutralize directional risk
   - Rehedge when delta changes >10%

3. **Vega hedge:**
   - Buy/sell vanilla options to neutralize vol risk
   - Important for lookbacks (high vega)
   - Rehedge monthly or after vol moves >5%

4. **Gamma management:**
   - Monitor near barriers (gamma explodes)
   - Exit positions if approaching barrier
   - Use options to flatten gamma if needed

### 6. Settlement Process


**At expiration:**

1. **Verify all observations:**
   - Asian: Confirm all fixing dates/prices
   - Lookback: Confirm max/min prices
   - Barrier: Confirm barrier never breached

2. **Calculate payoff:**
   - Use agreed-upon formula
   - Document all intermediate values
   - Handle disputes (if any data disagreement)

3. **Deliver payment/shares:**
   - Cash settlement (most common)
   - Or physical delivery (if specified)

4. **Post-mortem analysis:**
   - Actual vs. expected P&L
   - Hedge performance
   - Lessons for next trade

---

## Final Wisdom


> "Path-dependent options are powerful tools that can reduce costs and better target exposures—but only if you truly understand the path features you're embedding. The path from here to expiration matters as much as the destination. Asian options are elegant for hedging average exposures, barriers can reduce costs dramatically, and lookbacks guarantee optimal execution—but each comes with unique risks. The moment you lose track of the path variables (average, barriers, extremes), or fail to understand how Greeks behave along different paths, you've turned sophisticated hedging into speculation. Respect the path, monitor it religiously, and never hold barrier options near barriers unless you enjoy financial Russian roulette."

**Key to success:**

- Match path dependence to actual exposure (Asian for average, etc.)
- Understand path features deeply before trading
- Monitor state variables continuously (average, max, barriers)
- Hedge early and often (don't wait for trouble)
- Keep structures simple (each path feature adds risk)
- Stress test under realistic paths (not just terminal prices)
- Exit barrier positions with buffer (don't wait for disaster)
