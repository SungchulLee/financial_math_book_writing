# Payoff Engineering


**Payoff engineering** is the systematic design and construction of custom financial payoffs by combining vanilla options, forwards, and other building blocks to create precisely tailored risk-return profiles that match specific investment objectives, hedging needs, or market views that cannot be achieved with standard instruments.

---

## The Core Insight


**The fundamental idea:**

- Standard securities (stocks, bonds, options) have fixed payoffs
- Investors often have specific, non-standard needs
- Options are like financial Lego blocks
- Combine them creatively to build any payoff shape you want
- Mathematics enables precise payoff construction
- The limit is imagination (and arbitrage constraints)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/payoff_building_blocks.png?raw=true" alt="payoff_building_blocks" width="700">
</p>
**Figure 1:** Fundamental building blocks of payoff engineering showing how calls, puts, forwards, and bonds can be combined linearly to create any desired piecewise-linear payoff structure at expiration.

**You're essentially asking: "What exact risk-return profile do I want, and how do I build it from available pieces?"**

---

## What Is Payoff Engineering?


### 1. Building Block Principle


**Fundamental components:**

**Definition:** Any financial payoff can be decomposed into a linear combination of elementary instruments: bonds (constant payoff), forwards (linear payoff), and options (convex/concave payoffs).

**When you engineer payoffs:**

- Start with desired final payoff graph
- Decompose into elementary shapes
- Each shape maps to specific instrument
- Sum of instruments creates target payoff
- Arbitrage ensures consistent pricing

**Elementary building blocks:**

$$
\begin{align*}
\text{Zero-coupon bond:} & \quad V(S_T) = 1 \quad \text{(constant)} \\
\text{Forward:} & \quad V(S_T) = S_T - K \quad \text{(linear)} \\
\text{Call:} & \quad V(S_T) = \max(S_T - K, 0) \quad \text{(convex)} \\
\text{Put:} & \quad V(S_T) = \max(K - S_T, 0) \quad \text{(concave)}
\end{align*}
$$

### 2. Replication Principle


**Any payoff can be replicated:**

**The deep insight:** By the fundamental theorem of asset pricing, any attainable payoff can be replicated by a portfolio of traded securities. If markets are complete (enough options at different strikes), you can replicate ANY payoff function.

**Formal statement:**

For any desired payoff function $V(S_T)$, there exists a portfolio $(\alpha, \beta, \{c_i\}, \{p_i\})$ such that:

$$
V(S_T) = \alpha \cdot 1 + \beta \cdot S_T + \sum_{i} c_i \max(S_T - K_i, 0) + \sum_{j} p_j \max(K_j - S_T, 0)
$$

**Translation:**
- $\alpha \cdot 1$ = Cash position (bonds)
- $\beta \cdot S_T$ = Stock or forward position
- $\sum c_i \max(S_T - K_i, 0)$ = Portfolio of call options
- $\sum p_j \max(K_j - S_T, 0)$ = Portfolio of put options

**The power:** You can build literally any payoff shape by adjusting $(\alpha, \beta, \{c_i\}, \{p_i\})$.

### 3. Static vs. Dynamic


**Two approaches to replication:**

**Static replication:**
- Buy-and-hold portfolio of options
- Set up once at $t=0$, hold to maturity
- No adjustments needed during life
- Simple, no transaction costs after initial setup
- Works for path-independent payoffs

**Dynamic replication:**
- Continuously adjust portfolio (delta hedging)
- Requires active trading during life
- Can replicate any payoff (even path-dependent)
- Higher transaction costs, operational complexity
- Used when static replication impossible or expensive

**Example - Replicating a call option:**

**Static:** Buy the call option (trivial)

**Dynamic:** 
- Start with $\Delta$ shares of stock
- Each period, adjust $\Delta$ based on Black-Scholes formula
- At expiration, portfolio converges to call payoff
- Requires continuous trading (in theory)

**When to use each:**
- Static: When payoff is path-independent and options available
- Dynamic: When payoff is path-dependent or options not available

### 4. Piecewise Linearity


**Key decomposition technique:**

Any piecewise-linear payoff can be written as:

$$
V(S_T) = a + b \cdot S_T + \sum_{i=1}^{n} c_i \cdot \max(S_T - K_i, 0) + \sum_{j=1}^{m} d_j \cdot \max(K_j - S_T, 0)
$$

**How to construct:**

1. **Identify kinks:** Where does payoff slope change?
2. **At each kink $K_i$:** Add option with strike $K_i$
3. **Weight option:** By the change in slope at that kink
4. **Add linear term:** For baseline slope
5. **Add constant:** For vertical shift

**Example - Triangle payoff:**

Want payoff:
- $V(S_T) = 0$ if $S_T \leq 90$
- $V(S_T) = S_T - 90$ if $90 < S_T \leq 110$ (slope = 1)
- $V(S_T) = 20$ if $S_T > 110$ (slope = 0)

**Construction:**
- Kink at $K_1 = 90$: Slope changes from 0 to 1 → **Buy call at 90**
- Kink at $K_2 = 110$: Slope changes from 1 to 0 → **Sell call at 110**
- **Portfolio: Long 90 call, Short 110 call** (this is a call spread!)

**Verification:**
$$
V(S_T) = \max(S_T - 90, 0) - \max(S_T - 110, 0)
$$

- If $S_T \leq 90$: $V = 0 - 0 = 0$ ✓
- If $90 < S_T \leq 110$: $V = (S_T - 90) - 0 = S_T - 90$ ✓
- If $S_T > 110$: $V = (S_T - 90) - (S_T - 110) = 20$ ✓

### 5. Breeden-Litzenberger


**Spanning with options:**

**The remarkable result:** Any twice-differentiable payoff can be spanned by a continuum of options.

**Breeden-Litzenberger formula:**

$$
V(S_T) = V(F) + V'(F)(S_T - F) + \int_{0}^{F} V''(K) \cdot P(K) \, dK + \int_{F}^{\infty} V''(K) \cdot C(K) \, dK
$$

Where:
- $V(S_T)$ = Desired payoff
- $F$ = Forward price
- $V'(F)$ = First derivative (slope at forward)
- $V''(K)$ = Second derivative (curvature)
- $P(K)$ = Put option at strike $K$
- $C(K)$ = Call option at strike $K$

**Intuition:**
- Start with linear payoff: $V(F) + V'(F)(S_T - F)$ (forward position)
- Add curvature using options
- $V''(K)$ tells you how much of each strike to buy
- Negative $V''$ → Sell options (concave payoff)
- Positive $V''$ → Buy options (convex payoff)

**Example - Squared payoff:**

Want: $V(S_T) = S_T^2$

$$
V''(K) = 2 \quad \text{(second derivative is constant)}
$$

**Replication:**

$$
S_T^2 = F^2 + 2F(S_T - F) + 2\int_{0}^{F} P(K) \, dK + 2\int_{F}^{\infty} C(K) \, dK
$$

**Translation:** Buy 2 units of every put below $F$ and 2 units of every call above $F$. The portfolio will exactly replicate $S_T^2$ at expiration.

### 6. Digital Options


**Sharp payoffs:**

**Definition:** Options that pay a fixed amount if condition is met, zero otherwise. Also called "binary options."

**Payoff:**

$$
\text{Digital Call: } V(S_T) = \begin{cases}
1 & \text{if } S_T > K \\
0 & \text{if } S_T \leq K
\end{cases}
$$

**Replication using vanilla options:**

A digital can be approximated by a tight call spread:

$$
\text{Digital Call} \approx \frac{1}{\epsilon} \left( C(K) - C(K + \epsilon) \right)
$$

As $\epsilon \to 0$, this converges to the digital payoff.

**Intuition:**
- Call spread pays $(S_T - K)$ if $K < S_T < K + \epsilon$
- Dividing by $\epsilon$ scales payoff to approximately 1
- As $\epsilon \to 0$, becomes vertical jump at $K$

**Example:**

Want digital that pays $10 if $S_T > 100$:

**Approximation:**
- Buy 100 calls at strike 100
- Sell 100 calls at strike 100.10 (10 cent spread)
- If $S_T > 100.10$: Payoff = $100 \times 0.10 = $10$ ✓
- Cost: Approximately $100 \times (C(100) - C(100.10))$

### 7. Risk Reversals


**Asymmetric positions:**

**Definition:** Combination of call and put, usually OTM on opposite sides, creating directional bias with limited cost.

**Structure:**
- Buy OTM call at $K_2$
- Sell OTM put at $K_1$ (where $K_1 < K_2$)
- Net cost: Often zero or small (premium from sold put funds bought call)

**Payoff:**

$$
V(S_T) = \max(S_T - K_2, 0) - \max(K_1 - S_T, 0)
$$

**Simplified:**
$$
V(S_T) = \begin{cases}
-(K_1 - S_T) & \text{if } S_T < K_1 \text{ (loss, like short put)} \\
0 & \text{if } K_1 \leq S_T \leq K_2 \text{ (neutral zone)} \\
S_T - K_2 & \text{if } S_T > K_2 \text{ (profit, like long call)}
\end{cases}
$$

**Economic interpretation:**
- Bullish bias (benefit if stock rises)
- But exposed to downside (short put risk)
- Often zero cost (synthetic forward-like position)
- Common in FX markets ("25-delta risk reversal")

---

## Key Terminology


**Strike:**
- Exercise price of an option
- Determines where payoff "kinks"
- Key parameter in payoff engineering
- More strikes = more flexibility

**Notional:**
- Amount of underlying exposure
- Can differ for each option in portfolio
- Controls magnitude of payoff at each kink
- Example: 2 calls creates 2× payoff above strike

**Payout Ratio:**
- Ratio of payoff received to premium paid
- Key metric for structured products
- Example: "200% participation" means $2 gain per $1 stock gain
- Used in marketing to investors

**Knock-In/Knock-Out:**
- Barrier options that activate/deactivate
- Knock-in: Becomes active if barrier hit
- Knock-out: Becomes void if barrier hit
- Used to reduce premium cost

**Cap and Floor:**
- Maximum and minimum payoffs
- Cap: Limits upside (like selling call above)
- Floor: Protects downside (like buying put below)
- Creates bounded payoff range

**Participation Rate:**
- Percentage of upside captured
- 100% = full participation
- 150% = leveraged participation (gains 1.5× stock)
- 50% = partial participation (gains 0.5× stock)

---

## Payoff Construction


### 1. Spread Payoffs


**Limited risk, limited reward:**

**Bull call spread:**

$$
V(S_T) = \max(S_T - K_1, 0) - \max(S_T - K_2, 0) \quad (K_1 < K_2)
$$

**Payoff structure:**
- Max profit: $K_2 - K_1$ (width of spread)
- Max loss: Premium paid (net of sold call)
- Breakeven: $K_1 + \text{Net Premium}$

**Why use:**
- Lower cost than buying call alone
- Defined risk (limited loss)
- Good for moderately bullish views
- Common in directional trades

**Variations:**
- Bear put spread: Profit from moderate decline
- Call calendar spread: Different expirations
- Diagonal spread: Different strikes AND expirations

### 2. Butterfly Payoffs


**Bet on low volatility:**

**Long butterfly:**

$$
V(S_T) = \max(S_T - K_1, 0) - 2\max(S_T - K_2, 0) + \max(S_T - K_3, 0)
$$

Where $K_1 < K_2 < K_3$ and typically $K_2 = \frac{K_1 + K_3}{2}$ (ATM)

**Payoff characteristics:**
- Max profit: At $S_T = K_2$ (middle strike)
- Max profit value: $K_2 - K_1$ (half wing width)
- Max loss: Premium paid (at $S_T < K_1$ or $S_T > K_3$)
- Breakeven: Two points (near $K_1$ and $K_3$)

**Simplified payoff:**

$$
V(S_T) = \begin{cases}
0 & \text{if } S_T \leq K_1 \\
S_T - K_1 & \text{if } K_1 < S_T \leq K_2 \\
K_3 - S_T & \text{if } K_2 < S_T \leq K_3 \\
0 & \text{if } S_T > K_3
\end{cases}
$$

**When to use:**
- Expect stock to stay near $K_2$ (low volatility)
- Selling volatility but with limited risk
- Earnings plays when expect minimal move
- Alternative to short straddle (lower risk)

### 3. Condor Payoffs


**Wider range than butterfly:**

**Iron condor:**

$$
V(S_T) = \max(S_T - K_1, 0) - \max(S_T - K_2, 0) - \max(S_T - K_3, 0) + \max(S_T - K_4, 0)
$$

Where $K_1 < K_2 < K_3 < K_4$

Or equivalently:
- Buy put at $K_1$
- Sell put at $K_2$
- Sell call at $K_3$
- Buy call at $K_4$

**Payoff:**

$$
V(S_T) = \begin{cases}
-(K_2 - K_1) & \text{if } S_T \leq K_1 \\
S_T - K_2 & \text{if } K_1 < S_T \leq K_2 \\
0 & \text{if } K_2 < S_T \leq K_3 \text{ (profit zone)} \\
-(S_T - K_3) & \text{if } K_3 < S_T \leq K_4 \\
-(K_4 - K_3) & \text{if } S_T > K_4
\end{cases}
$$

**Max profit:** Premium received (if $K_2 < S_T < K_3$)
**Max loss:** $K_2 - K_1$ or $K_4 - K_3$ (whichever is larger)

**Why use:**
- Wider profit range than butterfly
- Higher probability of profit (larger neutral zone)
- Lower max profit but higher win rate
- Income strategy in range-bound markets

### 4. Straddle/Strangle


**Volatility plays:**

**Long straddle:**

$$
V(S_T) = \max(S_T - K, 0) + \max(K - S_T, 0) = |S_T - K|
$$

**Payoff:** V-shaped, profits from large moves either direction

**Long strangle:**

$$
V(S_T) = \max(S_T - K_2, 0) + \max(K_1 - S_T, 0) \quad (K_1 < K_2)
$$

**Difference from straddle:**
- Uses different strikes (OTM on both sides)
- Lower cost (both options OTM)
- Need larger move to profit
- Wider breakeven range

**When to use:**
- Expect large move but uncertain direction
- Before binary events (earnings, FDA, elections)
- High implied volatility environment (for short positions)
- Volatility arbitrage

### 5. Ratio Spreads


**Unbalanced positions:**

**Call ratio spread:**
- Buy 1 call at $K_1$
- Sell 2 calls at $K_2$ (where $K_1 < K_2$)

**Payoff:**

$$
V(S_T) = \max(S_T - K_1, 0) - 2\max(S_T - K_2, 0)
$$

**Simplified:**

$$
V(S_T) = \begin{cases}
0 & \text{if } S_T \leq K_1 \\
S_T - K_1 & \text{if } K_1 < S_T \leq K_2 \\
2K_2 - K_1 - S_T & \text{if } S_T > K_2 \text{ (declines with higher } S_T \text{!)}
\end{cases}
$$

**Key feature:** Payoff turns negative above $2K_2 - K_1$
- Max profit: At $S_T = K_2$ (value = $K_2 - K_1$)
- **Unlimited loss** if stock rises far above $K_2$
- Often setup as zero-cost (premium received from 2 short calls funds long call)

**When to use:**
- Moderately bullish, don't expect huge rally
- Want to reduce cost of long call
- Willing to cap upside and take tail risk
- **Dangerous:** Can lose big if stock moons

### 6. Collar Payoffs


**Protected but capped:**

$$
V(S_T) = S_T + \max(K_1 - S_T, 0) - \max(S_T - K_2, 0)
$$

Where $K_1 < S_0 < K_2$ (protective put below, covered call above)

**Simplified:**

$$
V(S_T) = \begin{cases}
K_1 & \text{if } S_T \leq K_1 \text{ (floor)} \\
S_T & \text{if } K_1 < S_T \leq K_2 \text{ (tracks stock)} \\
K_2 & \text{if } S_T > K_2 \text{ (cap)}
\end{cases}
$$

**Construction:**
- Own stock (underlying position)
- Buy put at $K_1$ (downside protection)
- Sell call at $K_2$ (upside cap, funds put)
- Net cost: Often zero (zero-cost collar)

**When to use:**
- Own stock, want downside protection
- Willing to give up upside for protection
- Tax reasons (avoid selling stock)
- Regulatory/lockup reasons (can't sell)
- Executive compensation (protect stock grants)

### 7. Digital Payoffs


**All-or-nothing:**

**Digital call:**

$$
V(S_T) = \begin{cases}
0 & \text{if } S_T \leq K \\
N & \text{if } S_T > K
\end{cases}
$$

**Replication:** Tight call spread

$$
V(S_T) \approx \frac{N}{\epsilon} \left[ \max(S_T - K, 0) - \max(S_T - (K + \epsilon), 0) \right]
$$

**Practical construction:**
- Choose small $\epsilon$ (e.g., 1% of strike)
- Buy $\frac{N}{\epsilon}$ calls at $K$
- Sell $\frac{N}{\epsilon}$ calls at $K + \epsilon$
- As $\epsilon \to 0$, payoff approaches perfect digital

**When to use:**
- Binary events (FDA approval, election outcome)
- Trigger-based payments in structured products
- Insurance-like payoffs
- **Caution:** Very sensitive to slight changes in underlying near barrier

---

## Advanced Techniques


### 1. Convexity Engineering


**Curve the payoff:**

**Goal:** Create specific curvature (second derivative) at different points

**Breeden-Litzenberger application:**

For payoff $V(S_T)$:

$$
V''(K) = \frac{\partial^2 V}{\partial K^2}
$$

This tells you option density needed at each strike.

**Example - Exponential payoff:**

Want: $V(S_T) = e^{S_T}$

$$
V''(K) = e^K \quad \text{(positive everywhere, increasing)}
$$

**Replication:**

$$
e^{S_T} \approx e^F + e^F(S_T - F) + \int_0^F e^K P(K) dK + \int_F^\infty e^K C(K) dK
$$

**Interpretation:** Need exponentially increasing weights of options at higher strikes to replicate exponential payoff.

### 2. Moment Matching


**Match desired moments:**

**Goal:** Create payoff with specific mean, variance, skewness, kurtosis

**Approach:**
1. Calculate moments of desired payoff
2. Use options to adjust portfolio moments
3. Iterate until match

**Example - Target positive skewness:**

Standard stock has zero skewness (symmetric distribution). To add positive skewness:
- Buy OTM calls (capture upside)
- Sell or reduce stock position (reduce symmetric part)
- Result: Right-skewed return distribution

**Moment engineering formula:**

For $n$-th moment of return $R$:

$$
E[R^n] = \int (R_T - R_0)^n f(R_T) dR_T
$$

Options with different strikes contribute differently to each moment. Optimize weights to match target moments.

### 3. Greeks Engineering


**Control sensitivities:**

**Portfolio Greeks:**

$$
\begin{align*}
\Delta_{\text{portfolio}} &= \sum_i w_i \Delta_i \\
\Gamma_{\text{portfolio}} &= \sum_i w_i \Gamma_i \\
\text{Vega}_{\text{portfolio}} &= \sum_i w_i \text{Vega}_i \\
\Theta_{\text{portfolio}} &= \sum_i w_i \Theta_i
\end{align*}
$$

**Example - Delta-neutral with positive gamma:**

Want:
- $\Delta = 0$ (no directional exposure)
- $\Gamma > 0$ (profit from large moves)

**Construction:**
- Buy ATM straddle: $\Delta \approx 0$, $\Gamma > 0$
- Adjust with stock if needed to fine-tune delta to exactly zero
- Result: Pure volatility play

**Example - Positive theta, negative gamma:**

Want:
- $\Theta > 0$ (earn time decay)
- $\Gamma < 0$ (short volatility)

**Construction:**
- Short straddle or iron condor
- Collect premium, profit if stock stays in range
- Risk: Large moves hurt (negative gamma)

### 4. Variance Swaps


**Pure volatility exposure:**

**Payoff:**

$$
V_T = N \times (\sigma_{\text{realized}}^2 - K_{\text{var}})
$$

Where:
- $N$ = Notional (variance units)
- $\sigma_{\text{realized}}^2$ = Realized variance over period
- $K_{\text{var}}$ = Strike variance (fixed at trade inception)

**Replication using options:**

Variance swaps can be replicated by a portfolio of options at all strikes:

$$
\sigma^2 \approx \frac{2}{T} \left[ \int_0^F \frac{P(K)}{K^2} dK + \int_F^\infty \frac{C(K)}{K^2} dK \right]
$$

**Interpretation:**
- Buy all OTM puts below forward
- Buy all OTM calls above forward
- Weight each option by $\frac{1}{K^2}$
- Portfolio replicates realized variance

**When to use:**
- Pure bet on volatility (no directional exposure)
- Arbitrage between implied and realized volatility
- Portfolio hedging (hedge tail risk)
- Alternative to delta-hedged straddles

### 5. Forward Start Options


**Option on future option:**

**Payoff:** At time $T_1$, receive option with strike set at-the-money at $T_1$, expiring at $T_2$.

**Value at $T_1$:**

$$
V_{T_1} = C(S_{T_1}, K = S_{T_1}, T_2 - T_1)
$$

**Replication:**
- Forward start options can be valued using Black-Scholes
- Price depends on forward volatility $\sigma_{T_1 \to T_2}$

**Formula:**

$$
C_{\text{forward start}} = S_0 \cdot BS(1, 1, \sigma\sqrt{T_2 - T_1})
$$

**When to use:**
- Employee stock options (granted in future at-the-money)
- Structured products with cliquet features
- Hedge future volatility exposure
- Compensation plans

### 6. Chooser Options


**Decide later if call or put:**

**Payoff:** At time $T_1 < T$, choose whether option is call or put, both expire at $T$ with strike $K$.

**Value at $T_1$:**

$$
V_{T_1} = \max(C(S_{T_1}, K, T - T_1), P(S_{T_1}, K, T - T_1))
$$

**Replication:**

By put-call parity:

$$
\text{Chooser} = C(S_0, K, T) + P(S_0, K e^{-r(T - T_1)}, T_1)
$$

**Interpretation:**
- Long call expiring at $T$ with strike $K$
- Long put expiring at $T_1$ with strike $K e^{-r(T - T_1)}$

**When to use:**
- Uncertain market direction initially
- Binary event at $T_1$ determines direction
- More flexible than straddle
- Slightly cheaper than buying both call and put

### 7. Cliquet Options


**Ratchet mechanism:**

**Payoff:** Sum of returns, reset periodically, with floor/cap at each reset.

**Structure:**
- Observation dates: $T_1, T_2, ..., T_n$
- At each $T_i$: Lock in return $\min(\max(R_i, \text{floor}), \text{cap})$
- Final payoff: Sum of locked returns

**Example:**
- 3-year cliquet, annual resets, 0% floor, 15% cap

**Year 1:** Stock +20% → Locked return = 15% (capped)
**Year 2:** Stock -10% → Locked return = 0% (floored)
**Year 3:** Stock +8% → Locked return = 8%
**Total:** 15% + 0% + 8% = 23% over 3 years

**Replication:**
- Portfolio of forward-start options with caps/floors
- Computationally intensive
- Common in structured notes

---

## Common Mistakes


### 1. Ignoring Bid-Ask Spreads


**Theory vs. reality:**

- **Mistake:** Design complex payoff assuming mid-market prices
- **Why it fails:** Each leg costs bid-ask spread, costs multiply
- **Fix:** Check actual execution costs before finalizing design
- **Real cost:** 5-10% of notional for complex structures

**Example:**

**Theoretical design:**
- Buy butterfly: 95/100/105 calls
- Theoretical cost: $3.00 - 2 × $1.50 + $0.75 = $0.75

**Real execution:**
- Buy 95 call at ask: $3.10 (vs. $3.00 mid)
- Sell 2× 100 calls at bid: $1.45 each (vs. $1.50 mid)
- Buy 105 call at ask: $0.80 (vs. $0.75 mid)
- **Actual cost: $3.10 - 2 × $1.45 + $0.80 = $1.00**

**Impact:** 33% higher cost ($1.00 vs. $0.75 theoretical)

### 2. Forgetting Pin Risk


**Settlement headaches:**

- **Mistake:** Design payoff with strikes near expected final price
- **Why it fails:** Uncertainty about exercise at expiration, assignment risk
- **Fix:** Avoid strikes within 1-2% of expected final price
- **Real cost:** Unexpected positions, cash requirements, P&L uncertainty

**Example:**

Iron condor: 95/100/105/110 with stock at $102.50 at expiration

**The problem:**
- Did 100 call get exercised? (ITM by $2.50 but holder may not exercise)
- Did 105 call get exercised? (OTM but holder might think it's ITM)
- Friday 4pm: Unsure of position
- Monday morning: May find out assigned/not assigned
- Could end up long/short stock unexpectedly

**Fix:** Design strikes at 95/100/110/115 if stock near 102-103

### 3. Leverage Creep


**Unintentional amplification:**

- **Mistake:** Engineer payoff without tracking total notional exposure
- **Why it fails:** Gross notional can be 5-10× capital, amplifies losses
- **Fix:** Always calculate gross and net notional vs. capital
- **Real cost:** Margin calls, forced liquidation

**Example:**

Capital: $100K

**Payoff engineering:**
- Buy 10 calls at 95 (notional: 100 shares × 10 = 1,000 shares)
- Sell 20 calls at 100 (notional: 2,000 shares)
- Buy 10 calls at 105 (notional: 1,000 shares)

**Gross notional:** 4,000 shares = $400K (4× leverage)

If stock gaps down 20%:
- 95 calls: -100% = -$10K (premium paid)
- 100 calls: +100% = +$5K (premium collected)
- 105 calls: -100% = -$2K (premium paid)
- But margin requirements spike, may force liquidation at worst time

### 4. Path Dependence Oversight


**Static assumption failure:**

- **Mistake:** Design payoff assuming static replication works
- **Why it fails:** Payoff is actually path-dependent, requires dynamic hedging
- **Fix:** Identify path dependencies upfront, use appropriate replication
- **Real cost:** Hedge slippage, P&L bleed from rebalancing

**Example:**

Want payoff: "Average of stock price over 12 months"

**Naive approach:**
- Try to static replicate with options
- **Fails:** Average is path-dependent, not replicable statically

**Correct approach:**
- Must dynamically hedge
- Or use Asian option (if available)
- Or accept tracking error from static approximation

### 5. Correlation Assumptions


**Multi-asset errors:**

- **Mistake:** Design payoff on basket assuming independence
- **Why it fails:** Correlations change, especially in stress
- **Fix:** Stress test under correlation scenarios (0%, 50%, 100%)
- **Real cost:** Unexpected losses when correlations spike to 1

**Example:**

**Worst-of option on two stocks:**

Payoff: $\max(S_1 - K, 0) + \max(S_2 - K, 0)$

**Assumption:** $\rho = 0.3$ (low correlation)
**Pricing:** Cheap due to diversification benefit

**Crisis:** Both stocks fall together, $\rho \to 0.9$
**Result:** Both options OTM, payoff = 0
**Expected:** At least one would be ITM (diversification)

**Loss:** Paid premium for diversification that disappeared

### 6. Tail Risk Blindness


**Small probability, large impact:**

- **Mistake:** Design payoff optimizing expected value, ignoring tail losses
- **Why it fails:** Rare events occur more often than models predict (fat tails)
- **Fix:** Always cap maximum loss, even if reduces expected return
- **Real cost:** One tail event wipes out years of gains

**Example:**

**Short volatility strategy:**
- Sell OTM puts, collect premium
- Win rate: 95% (put expires OTM)
- Avg win: +2% monthly
- **Tail risk:** 5% of time, lose -30% (market crash)

**Expected return:** $0.95 \times 2\% + 0.05 \times (-30\%) = 1.9\% - 1.5\% = 0.4\%$

**Reality:** Tail events occur 10% of time (model underestimates), not 5%

**Actual return:** $0.90 \times 2\% + 0.10 \times (-30\%) = 1.8\% - 3\% = -1.2\%$ (negative!)

**Lesson:** Short volatility strategies look great until they don't. Always limit tail exposure.

---

## Best vs. Worst Case


### 1. Best Case: Success


**Structured note with target payoff:**

**Setup:**
- Investor wants: 100% principal protection + 150% participation in S&P 500 up to 20% gain
- 3-year horizon
- S&P currently at 4,000

**Payoff engineering:**

Target payoff:
- If S&P down or flat: Return 100% of principal (no loss)
- If S&P up 0-20%: Return 100% + 1.5× gain (max 30% gain)
- If S&P up >20%: Return 130% (capped at 30%)

**Construction:**

1. **Principal protection:**
   - Buy zero-coupon bond maturing at 100% in 3 years
   - Cost: ~85% of capital (assuming 5% rate)

2. **Participation:**
   - Remaining 15% of capital to buy calls
   - Buy 1.5× notional of ATM calls
   - Sell calls at 120% strike (20% above)
   - Net cost fits in 15% budget

**Scenario: S&P +15% over 3 years**

**Outcome:**
- Principal: 100% (bond matures at par)
- Participation: 15% × 1.5 = 22.5% gain
- **Total return: 122.5%**
- Investor achieves 22.5% gain vs. 15% for S&P 500
- **Success: Leverage on upside, no downside risk**

**Value added:**
- Investor: Gets downside protection + upside leverage
- Issuer: Earns structuring fee (~1-2%)
- Perfect payoff match to investor objectives

### 2. Worst Case: Failure


**Exotic option blowup:**

**Setup:**
- Sophisticated trader designs "risk-free" arbitrage
- Sells barrier options (knock-out puts)
- Thinks: "Stock won't hit barrier, collect premium"

**Structure:**
- Sell 100 knock-out puts on TSLA
- Strike: $200, Barrier: $150, Current: $250
- Premium collected: $500K
- Reasoning: "If stock drops to $150, I'm okay holding stock at $200"

**Month 1: Stock at $250 → $170**
- Barrier not hit yet
- Feeling confident, stock held support at $170

**Month 2: Flash crash to $145 (barrier breached!)**
- Puts knock out (become worthless to holder)
- **Trader thinks: "Great! Options expired worthless, I keep premium"**

**Reality check:**
- Trader was synthetically short stock via the puts
- When puts knocked out, synthetic short position disappeared
- But trader forgot to hedge by buying stock
- Now naked short stock exposure

**Month 3: Stock rebounds to $300**
- Massive unhedged loss: ($300 - $250) × 100 contracts × 100 shares = $500K loss
- Premium collected: +$500K
- **Net: $0** (broke even after massive drama)

**But wait, it gets worse:**
- Margin calls during month 2-3: Had to post $200K margin
- Psychological stress: Couldn't sleep, health suffered
- Opportunity cost: Capital tied up for 3 months
- **Reputation damage:** Labeled as "risky trader" by firm

**Lesson:**
- Barrier options have discontinuous Greeks
- Dynamic hedging near barriers is brutal
- "Free money" strategies usually aren't
- Complexity often hides risk, not eliminates it

---

## Risk Management Rules


### 1. Gross Notional Limits


**Control leverage:**

$$
\text{Gross Notional} = \sum_i |N_i \times \text{Strike}_i|
$$

**Limits:**
- Conservative: Gross notional ≤ 3× capital
- Moderate: Gross notional ≤ 5× capital
- Aggressive: Gross notional ≤ 10× capital
- **Never exceed 10× without special approval**

**Example:**

Capital: $100K

**Position:**
- Long 10 calls at 100 strike: Notional = 10 × 100 × 100 = $100K
- Short 20 calls at 110 strike: Notional = 20 × 100 × 110 = $220K
- Long 5 puts at 90 strike: Notional = 5 × 100 × 90 = $45K

**Gross notional:** $100K + $220K + $45K = $365K (3.65× leverage) ✓

### 2. Scenario Analysis


**Stress test the payoff:**

**Required scenarios:**
1. **Base case:** Expected outcome
2. **Upside:** Underlying +20%, volatility -20%
3. **Downside:** Underlying -20%, volatility +50%
4. **Extreme upside:** Underlying +50%
5. **Extreme downside:** Underlying -50%
6. **Volatility spike:** Underlying flat, volatility +100%
7. **Volatility collapse:** Underlying flat, volatility -50%

**Maximum loss cap:**
- Any single scenario: Loss ≤ 5% of capital
- Extreme scenarios: Loss ≤ 10% of capital
- If violated, redesign payoff

### 3. Greek Limits


**Control sensitivities:**

$$
\begin{align*}
|\Delta| &\leq 0.3 \times \text{Capital} / S_0 \quad \text{(directional exposure)} \\
|\Gamma| &\leq 0.01 \times \text{Capital} / S_0^2 \quad \text{(convexity risk)} \\
|\text{Vega}| &\leq 0.1 \times \text{Capital} \quad \text{(volatility exposure)} \\
|\Theta| &\leq 0.002 \times \text{Capital} \quad \text{(time decay)}
\end{align*}
$$

**Example ($100K capital, S = $100):**
- $|\Delta| \leq 300$ shares
- $|\Gamma| \leq 1$ (gamma in shares per dollar)
- $|\text{Vega}| \leq $10K$ (per 1% vol change)
- $|\Theta| \leq $200/day$ decay

### 4. Liquidity Requirements


**Ensure exit capability:**

**Minimum liquidity:**
- Daily option volume > 10× position size
- Bid-ask spread < 5% of mid price
- Can exit 50% of position in 1 day
- Can exit 100% of position in 3 days

**Example:**

Want to hold 100 call contracts

**Requirements:**
- Daily volume > 1,000 contracts ✓
- Bid-ask: $0.10 on $2.00 mid (5%) ✓
- 50 contracts tradeable in 1 day ✓
- 100 contracts tradeable in 3 days ✓

### 5. Complexity Penalty


**Simpler is better:**

**Complexity scoring:**
- Each unique strike: +1 point
- Each expiration: +1 point
- Barriers: +2 points
- Path dependence: +3 points
- Multiple underlyings: +2 points per asset

**Maximum complexity:** 10 points
**Target complexity:** ≤ 5 points

**Example:**

Butterfly: 3 strikes, 1 expiration = 4 points ✓
Cliquet: 1 strike, 3 expirations, path-dependent = 7 points (complex)
Worst-of barrier note: 2 underlyings, 1 strike, barrier = 6 points (borderline)

**Penalty:** For each point above 5, require 2× return target to justify

---

## Real-World Examples


### 1. CPPI (Constant Proportion Portfolio Insurance)


**Dynamic payoff engineering:**

**Goal:** Participate in equity upside while protecting downside

**Structure:**

$$
\text{Equity Exposure} = m \times (\text{Portfolio Value} - \text{Floor Value})
$$

Where:
- $m$ = Multiplier (typically 3-6)
- Floor = Minimum guaranteed value (e.g., 90% of initial capital)

**Example:**

Initial capital: $100K, Floor: $90K, Multiplier: 4

**Period 1:** Portfolio = $100K
- Cushion = $100K - $90K = $10K
- Equity exposure = 4 × $10K = $40K (40% in stocks)
- Remaining = $60K in bonds

**Period 2:** Stocks rally +10%, Portfolio = $104K
- New cushion = $104K - $90K = $14K
- **Increase** equity exposure = 4 × $14K = $56K (54% in stocks)
- Rebalance: Buy $16K more stocks

**Period 3:** Stocks crash -20%, Portfolio = $93.6K
- New cushion = $93.6K - $90K = $3.6K
- **Decrease** equity exposure = 4 × $3.6K = $14.4K (15% in stocks)
- Rebalance: Sell $41.6K stocks

**Payoff:** Convex upside (increase equity in rallies), protected downside (reduce equity in crashes)

**2008 Crisis lesson:** Many CPPI funds hit floor due to gap risk (markets gap down before rebalancing)

### 2. Autocallable Notes


**Popular retail structure:**

**Payoff:**
- Annual observation: If stock ≥ 100%, note "calls" (matures early), investor receives 100% + coupon
- If stock < 100% all years but ≥ 70% at maturity: Return 100%
- If stock < 70% at maturity: 1-to-1 downside (lose as much as stock lost below 100%)

**Example:**

3-year autocallable on Apple, 10% annual coupon

**Year 1:** AAPL +5% → Note calls, investor receives 110% ✓
**Best outcome:** Annual return = 10%

**Alternate scenario:**
**Year 1:** AAPL -5% (95%) → Continue
**Year 2:** AAPL flat (95%) → Continue
**Year 3:** AAPL +10% (105%) → Note matures at 130% (100% + 3 years × 10%)
**Return:** 9.1% annualized

**Worst scenario:**
**Year 3:** AAPL -35% (65%) → Barrier breached
**Investor loses:** 35% (same as stock)
**No coupons received:** 0%

**Replication:**
- Long stock position
- Short ATM calls at each annual observation (autocall feature)
- Short barrier put at 70% strike

**Why popular:**
- High coupons (10-15% annual)
- Frequent early maturity (feels like "winning")
- Downside protection (70% barrier)
- **But:** Gives up all upside above initial price

### 3. Target Redemption Note (TARN)


**Accumulated return cap:**

**Payoff:**
- Monthly observation: Receive max(Stock Return, 0)
- **Terminate** when accumulated return ≥ Target (e.g., 20%)
- If terminated: Return 100% + Target
- If never hits target: Return 100% + accumulated returns

**Example:**

12-month TARN on S&P 500, 20% target

**Month 1:** S&P +3% → Accumulated = 3%
**Month 2:** S&P +5% → Accumulated = 8%
**Month 3:** S&P -2% → Accumulated = 8% (no change, floor at 0)
**Month 4:** S&P +8% → Accumulated = 16%
**Month 5:** S&P +6% → Accumulated = 22% → **TERMINATED**

**Investor receives:** 120% after just 5 months (20% return in 5 months!)

**Replication:**
- Portfolio of monthly call options
- Knockout feature when accumulated gains hit target
- Complex to value (path-dependent, early termination)

**Why popular:**
- High apparent returns (20% in 5 months = 48% annualized!)
- But expected value usually similar to simple call option
- **Trick:** Cuts off right tail (if stock keeps rallying, you don't participate)

### 4. Range Accrual Note


**Daily observation payoff:**

**Payoff:**

$$
\text{Coupon} = \text{Base Rate} \times \frac{\text{Days in Range}}{\text{Total Days}}
$$

**Example:**

1-year note, 12% base rate, range: 95-105% of initial S&P 500

**Scenario 1: Low volatility year**
- 240 out of 252 trading days S&P 500 within 95-105%
- **Coupon: ** $12\% \times \frac{240}{252} = 11.4\%$

**Scenario 2: High volatility year**
- Only 100 out of 252 days in range
- **Coupon:** $12\% \times \frac{100}{252} = 4.8\%$

**Replication:**
- Portfolio of daily digital options
- 252 binary bets: "Is stock in range today?"
- **Very complex to hedge:** Requires daily rebalancing

**Risk:** Terrible payoff if volatility increases (which is when investors need returns most!)

---

## Practical Steps


### 1. Define Objective


**Start with the problem:**

**Questions to answer:**
1. What is the investment goal? (Income, growth, hedging?)
2. What is the risk tolerance? (Max acceptable loss?)
3. What is the time horizon? (Months, years?)
4. What market view? (Directional, volatility, correlation?)
5. What constraints? (Regulatory, tax, liquidity?)

**Example:**

- Goal: Generate income in flat market
- Risk tolerance: Max 5% loss
- Horizon: 3 months
- View: Stock stays $95-$105 (low volatility)
- Constraints: Can't use margin

**Conclusion:** Iron condor fits perfectly

### 2. Draw Target Payoff


**Visualize before building:**

**Steps:**
1. Sketch payoff diagram (Y-axis = P&L, X-axis = Stock price at expiration)
2. Mark key points: Max profit, max loss, breakevens
3. Identify kinks (where slope changes)
4. Note desired curvature (convex vs. concave regions)

**Example:**

Goal: Profit if stock $95-$105, small loss outside

**Sketch:**
- Below $90: Flat loss at -$3
- $90 to $95: Rising from -$3 to $0
- $95 to $105: Flat profit at $0 to +$2
- $105 to $110: Declining from +$2 to $0
- Above $110: Flat loss at -$3

**This is an iron condor!**

### 3. Decompose into Building Blocks


**Map to instruments:**

**For each kink at strike $K_i$:**
- Upward kink (slope increases): Long call at $K_i$
- Downward kink (slope decreases): Short call at $K_i$
- Similar logic for puts

**Iron condor construction:**
- Kink at $90$ (slope increases 0 → 1): Long put at $90$
- Kink at $95$ (slope decreases 1 → 0): Short put at $95$
- Kink at $105$ (slope decreases 0 → -1): Short call at $105$
- Kink at $110$ (slope increases -1 → 0): Long call at $110$

**Portfolio:**
- Long 90 put
- Short 95 put
- Short 105 call
- Long 110 call

### 4. Price Components


**Cost analysis:**

Get quotes for each leg:
- 90 put: $0.50 (bid/ask: $0.45/$0.55)
- 95 put: $1.50 (bid/ask: $1.45/$1.55)
- 105 call: $1.50 (bid/ask: $1.45/$1.55)
- 110 call: $0.50 (bid/ask: $0.45/$0.55)

**Execution (per contract):**
- Buy 90 put at ask: $0.55
- Sell 95 put at bid: $1.45
- Sell 105 call at bid: $1.45
- Buy 110 call at ask: $0.55

**Net credit:** $1.45 + $1.45 - $0.55 - $0.55 = $1.80$ per share = $180 per contract

**Max profit:** $180 (if stock ends $95-$105$)
**Max loss:** $5 - $1.80 = $3.20$ per share = $320$ per contract

### 5. Verify Arbitrage-Free


**No free money:**

**Checks:**
1. **Put-call parity:** $C - P = S - K e^{-rT}$ (approximately)
2. **No negative probabilities:** Option prices imply positive risk-neutral probabilities at all strikes
3. **No violations of dominance:** Higher strikes have lower call prices, higher put prices
4. **Consistency:** Butterfly spreads have non-negative values

**Example check - Butterfly value:**

$$
\text{Butterfly value} = C(K_1) - 2C(K_2) + C(K_3) \geq 0
$$

If violated, arbitrage exists!

### 6. Stress Test


**What-if analysis:**

**Scenarios:**
1. Stock at each kink point
2. Stock ±20% from current
3. Volatility ±50% from current
4. Interest rate ±100 bps
5. Time to expiration halved

**For each scenario:**
- Calculate Greeks (Delta, Gamma, Vega, Theta, Rho)
- Calculate P&L
- Check if within risk tolerance

**Example:**

Iron condor with stock at $100

**Scenario: Stock → $90 (down 10%)**
- P&L: -$280 per contract
- Within tolerance? If max loss = $320, yes (87% of max) ✓

**Scenario: Volatility +50% (20% → 30%)**
- Vega = -$50 per 1% vol
- P&L: -$50 × 10 = -$500
- **Exceeds max loss!** Need to hedge or redesign ✗

### 7. Execute and Monitor


**Implementation:**

**Day 1: Execute**
- Submit all legs as combo order (better pricing)
- Or leg in carefully: Start with least risky legs first
- Verify fills, confirm positions

**Weekly: Monitor Greeks**
- Calculate current Delta, Gamma, Vega, Theta
- Compare to limits
- Adjust if breached (hedge with stock/options)

**Monthly: P&L Review**
- Mark-to-market current value
- Calculate realized vs. expected P&L
- Attribution: How much from stock move? Vol change? Theta?

**At expiration:**
- Decide: Exercise, close, or let expire?
- Manage pin risk (avoid stocks near strikes)
- Document lessons learned

---

## Final Wisdom


> "Payoff engineering is both an art and a science. The science is decomposing desired payoffs into option portfolios using mathematics. The art is knowing which payoffs are actually worth creating—just because you CAN build a payoff doesn't mean you SHOULD. The best payoff engineering is invisible: it solves a real problem (hedging, income, leverage) using the simplest possible structure. When payoff engineering becomes exotic and complex, it often means someone is solving a problem that doesn't exist, usually to justify high fees. Build payoffs that serve your investors, not your ego."

**Key to success:**

- Start with clear investment objective (not the payoff)
- Draw target payoff before building (visualize first)
- Use simplest structure that achieves goal (Occam's Razor)
- Verify arbitrage-free pricing (no free lunch)
- Stress test under multiple scenarios (Murphy's Law applies)
- Monitor and adjust as needed (dynamic, not static)
- Document and learn from each trade (continuous improvement)
