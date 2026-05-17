# Properties and Bounds of Option Prices

Option prices satisfy fundamental mathematical properties that follow from no-arbitrage principles. These properties—monotonicity, convexity, and bounds—provide constraints that any valid pricing model must respect and enable arbitrage detection in practice.

!!! tip "Toy mechanism: dominated portfolios"
    Every result in this section is a corollary of a single mechanism: if portfolio $A$ pays at least as much as portfolio $B$ in every state of the world, then $A_0 \geq B_0$. The lower bound $C \geq (S - Ke^{-rT})^+$, the convex butterfly constraint, the calendar-spread inequality, and the parity-based Greek symmetries all come from comparing two payoff functions pathwise and reading off the price inequality. The Black–Scholes formula then *verifies* these properties — but the properties themselves are deeper than any specific model.

This section rigorously establishes these properties for European options under the Black-Scholes framework.

!!! info "Where this fits"
    - **Roadmap row(s):** Geometry (convexity / gamma) and the monotonicity of the formula in each parameter.
    - **Builds on:** [The Black-Scholes formula](bs_formula_statement.md) (the closed form being differentiated) and [Girsanov derivation](girsanov_derivation.md) (the PDE underlying the Greeks).
    - **Feeds into:** [Asymptotic behavior](asymptotic_behavior.md) (limit signs respect the monotonicity below) and [Computational examples](computational_examples.md) (numerical Greeks).

!!! note "Proposition (No-Arbitrage Properties of European Options)"
    For European options on a non-dividend-paying stock, the Black-Scholes prices satisfy:

    1. **Bounds**: $(S - Ke^{-rT})^+ \leq C \leq S$ and $(Ke^{-rT} - S)^+ \leq P \leq Ke^{-rT}$
    2. **Monotonicity**: $C$ is increasing in $S$, $T$, $\sigma$ and decreasing in $K$; reversed for $P$ in $S$ and $K$
    3. **Convexity**: $\Gamma = \partial^2 C / \partial S^2 > 0$ and $\partial^2 C / \partial K^2 > 0$

    Each property follows from the no-arbitrage principle; violations imply arbitrage opportunities. The proofs below verify these directly from the Black-Scholes formula.

---

!!! note "Lemma (Density-Strike Identity)"
    For all $S, K, T > 0$, $r \in \mathbb{R}$, and $\sigma > 0$, the Black-Scholes parameters $d_1$ and $d_2 = d_1 - \sigma\sqrt{T}$ satisfy

    $$
    S\,\phi(d_1) = K e^{-rT}\,\phi(d_2)
    $$

    where $\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ is the standard normal density.

    **Proof.** From the definitions, $d_1 - d_2 = \sigma\sqrt{T}$ and $d_1 + d_2 = \frac{2\ln(S/K) + 2rT}{\sigma\sqrt{T}}$, so

    $$
    d_1^2 - d_2^2 = (d_1 + d_2)(d_1 - d_2) = 2\ln(S/K) + 2rT
    $$

    Therefore

    $$
    \frac{\phi(d_1)}{\phi(d_2)} = \exp\!\left(\tfrac{1}{2}(d_2^2 - d_1^2)\right) = \exp\!\left(-\ln(S/K) - rT\right) = \frac{K}{S}\,e^{-rT}
    $$

    Cross-multiplying yields the stated identity. $\square$

    **Where it appears.** This identity is the algebraic engine behind several Black-Scholes Greek formulas. It causes the cross-terms in the differentiations $\partial C/\partial S$ (Monotonicity in Stock Price, below) and $\partial C/\partial K$ (Monotonicity in Strike, below) to cancel, yielding the clean expressions $\partial C/\partial S = \mathcal{N}(d_1)$ and $\partial C/\partial K = -e^{-rT}\mathcal{N}(d_2)$. The same cancellation simplifies the gamma, vega, and theta derivations.

---

## Fundamental Bounds

*Section goal: the lower and upper price bounds enforced by no-arbitrage.*

### 1. **Call Option Bounds**


For a European call option on a non-dividend-paying stock:

$$
\boxed{\max(S - Ke^{-rT}, 0) \leq C \leq S}
$$

**Lower bound**: The call cannot be worth less than its discounted intrinsic value (otherwise arbitrage exists)

**Upper bound**: The call cannot exceed the stock price (option gives right to buy stock, not worth more than owning it)

**Tighter lower bound**: 

$$
C \geq \max(S - Ke^{-rT}, 0)
$$

This is the **no-arbitrage lower bound**.

### 2. **Put Option Bounds**


For a European put:

$$
\boxed{\max(Ke^{-rT} - S, 0) \leq P \leq Ke^{-rT}}
$$

**Lower bound**: Put worth at least discounted intrinsic value

**Upper bound**: Put cannot exceed present value of strike (max possible payoff)

### 3. **Verification for Black-Scholes**


Since $\mathcal{N}(d_1), \mathcal{N}(d_2) \in [0,1]$, the upper bound follows immediately: $C = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2) \leq S \cdot 1 - Ke^{-rT} \cdot 0 = S$. ✓

For the lower bound $C \geq (S - Ke^{-rT})^+$, use **direct no-arbitrage**. Compare "long 1 call + cash $Ke^{-rT}$" (cost $C + Ke^{-rT}$, terminal value $\max(S_T - K, 0) + K = \max(S_T, K)$) with "long 1 share" (cost $S$, terminal value $S_T$). The first dominates pathwise: $\max(S_T, K) \geq S_T$, so $C + Ke^{-rT} \geq S$; combined with $C \geq 0$ this yields $C \geq (S - Ke^{-rT})^+$. The bound holds in *any* arbitrage-free model. ✓

---

## Monotonicity in Stock Price

*Section goal: $\partial C/\partial S = \mathcal{N}(d_1) > 0$ and the put analogue, derived via the Density-Strike Identity Lemma.*

### 1. **Call Options**


$$
\boxed{\frac{\partial C}{\partial S} = \mathcal{N}(d_1) > 0}
$$

**Interpretation**: Call price is **strictly increasing** in stock price.

**Proof**: Differentiating the Black-Scholes formula:

$$
\frac{\partial C}{\partial S} = \mathcal{N}(d_1) + S\frac{\partial \mathcal{N}(d_1)}{\partial S} - Ke^{-rT}\frac{\partial \mathcal{N}(d_2)}{\partial S}
$$

Using $\frac{\partial d_1}{\partial S} = \frac{1}{S\sigma\sqrt{T}}$ and $\frac{\partial d_2}{\partial S} = \frac{\partial d_1}{\partial S}$:

$$
\frac{\partial \mathcal{N}(d_1)}{\partial S} = \mathcal{N}'(d_1)\frac{1}{S\sigma\sqrt{T}}
$$

After substitution and using $\mathcal{N}'(d_1) = \frac{1}{\sqrt{2\pi}}e^{-d_1^2/2}$:

The cross-terms cancel because $S\mathcal{N}'(d_1)\frac{\partial d_1}{\partial S} = Ke^{-rT}\mathcal{N}'(d_2)\frac{\partial d_2}{\partial S}$, which is precisely the Density-Strike Identity (Lemma above). This leaves:

$$
\frac{\partial C}{\partial S} = \mathcal{N}(d_1)
$$

Since $\mathcal{N}(d_1) \in (0,1)$ for all finite $d_1$, the call is strictly increasing in $S$. ✓

**Economic intuition**: A higher stock price increases the probability that the call finishes in-the-money and raises the expected payoff conditional on exercise.

### 2. **Put Options**


$$
\boxed{\frac{\partial P}{\partial S} = -\mathcal{N}(-d_1) = \mathcal{N}(d_1) - 1 < 0}
$$

**Interpretation**: Put price is **strictly decreasing** in stock price.

**Proof**: From put-call parity:

$$
P = C - S + Ke^{-rT}
$$

Differentiate:

$$
\frac{\partial P}{\partial S} = \frac{\partial C}{\partial S} - 1 = \mathcal{N}(d_1) - 1 < 0
$$

Since $\mathcal{N}(d_1) < 1$, we have $\frac{\partial P}{\partial S} < 0$. ✓

**Economic intuition**: A higher stock price reduces the likelihood that the put finishes in-the-money and lowers the expected payoff $(K - S_T)^+$.

---

## Monotonicity in Time

*Section goal: how $\Theta < 0$ encodes time decay and the calendar-vs-maturity-time sign.*

### 1. **Time Decay (Theta)**


Recall (see [§ Greeks in Black-Scholes](../../ch10/greeks/greeks_in_black_scholes_model.md)): the closed-form theta $\Theta_{\text{call}} = -S\mathcal{N}'(d_1)\sigma/(2\sqrt{T}) - rKe^{-rT}\mathcal{N}(d_2)$ is negative when $r>0$ (non-dividend), so call value decays in calendar time, with $\Theta = -\partial C/\partial T$.

### 2. **Increasing with Time to Maturity**


For a European call on a non-dividend-paying stock with $r \geq 0$:

$$
\boxed{\frac{\partial C}{\partial T} > 0}
$$

(equivalently, $-\Theta_{\text{call}} > 0$ — the same sign convention, written in time-to-maturity instead of calendar time).

**Interpretation**: Longer-dated options are more valuable (more time for favorable price movement).

**Caveats.** Monotonicity can fail outside the standing assumptions: with continuous dividends $q > r$, deep-ITM European calls can lose value with longer $T$ (dividends accrue to the stock holder, not the option holder); with sufficiently negative $r$, discounting flips the calendar-spread inequality. No-dividends and $r \geq 0$ guarantee $\partial C/\partial T > 0$ unconditionally.

**Proof sketch**: For $T_2 > T_1$, a longer-dated call dominates the shorter-dated call by a calendar-spread no-arbitrage argument (Section "Calendar Spread Inequality" below); under non-negative rates and no dividends, the dominating portfolio has non-negative cost, so $C(S, T_2) \geq C(S, T_1)$.

---

## Monotonicity in Volatility

*Section goal: vega $\nu > 0$ as a property bound — both calls and puts gain from higher $\sigma$.*

Recall (see [§ Greeks in Black-Scholes](../../ch10/greeks/greeks_in_black_scholes_model.md)): $\nu = \partial C/\partial\sigma = S\sqrt{T}\,\mathcal{N}'(d_1) > 0$, identical for calls and puts by put-call parity, so option value is strictly increasing in $\sigma$

$$
\boxed{\frac{\partial C}{\partial \sigma} > 0, \qquad \nu_{\text{call}} = \nu_{\text{put}}}
$$

**Economic intuition**: Higher volatility increases the probability of large moves. For options (capped downside, unlimited upside) this increases value.

---

## Monotonicity in Strike

*Section goal: $\partial C/\partial K < 0$ via the same density identity, and the put analogue.*

### 1. **Call Options**


$$
\boxed{\frac{\partial C}{\partial K} = -e^{-rT}\mathcal{N}(d_2) < 0}
$$

**Interpretation**: Call price is **strictly decreasing** in strike.

**Proof**: Higher strike means:

- Lower intrinsic value
- Lower probability of exercise
- Less favorable payoff structure

Differentiating the Black-Scholes formula, the cross-terms cancel by the Density-Strike Identity (Lemma above):

$$
\frac{\partial C}{\partial K} = -e^{-rT}\mathcal{N}(d_2) < 0
$$

### 2. **Put Options**


$$
\boxed{\frac{\partial P}{\partial K} = e^{-rT}\mathcal{N}(-d_2) > 0}
$$

**Interpretation**: Put price is **strictly increasing** in strike (higher strike = more valuable right to sell).

---

## Convexity in Stock Price

*Section goal: $\Gamma > 0$ as the curvature of the price function in the underlying.*

### 1. **Second Derivative (Gamma)**


$$
\boxed{\Gamma = \frac{\partial^2 C}{\partial S^2} = \frac{\mathcal{N}'(d_1)}{S\sigma\sqrt{T}} > 0}
$$

**Interpretation**: Option value is **convex** in stock price.

**Gamma formula**:

$$
\Gamma = \frac{1}{S\sigma\sqrt{T}}\frac{1}{\sqrt{2\pi}}e^{-d_1^2/2} > 0
$$

**Implication**: 

- Options benefit from large stock price moves in either direction
- Delta increases as stock rises (accelerating gains)
- Delta decreases as stock falls (decelerating losses)

**Put gamma**: From put-call parity,

$$
\Gamma_{\text{put}} = \Gamma_{\text{call}}
$$

Both calls and puts have the same gamma.

### 2. **Graphical Interpretation**


The option value curve $C(S)$ is:

- **Concave up** (shaped like ⌣)
- Slope (delta) increases with $S$
- Tangent line always lies below the curve

This convexity property is fundamental to option hedging and risk management.

**Economic intuition**: Convexity means options benefit disproportionately from large moves—gains from favorable moves always exceed losses from unfavorable moves of the same magnitude. This asymmetry is the source of the option's time value.

---

## Convexity in Strike (Butterfly Spread)

*Section goal: $\partial^2 C/\partial K^2 > 0$ from a no-arbitrage butterfly argument.*

### 1. **Butterfly Constraint**


For strikes $K_1 < K_2 < K_3$ with $K_2 - K_1 = K_3 - K_2 = \Delta K$:

$$
\boxed{C(K_2) \leq \frac{C(K_1) + C(K_3)}{2}}
$$

**Interpretation**: Call prices are **convex** (downward) in strike.

**Proof**: Consider a **butterfly spread**:

- Buy 1 call at $K_1$
- Sell 2 calls at $K_2$
- Buy 1 call at $K_3$

**Cost**:

$$
\text{Cost} = C(K_1) - 2C(K_2) + C(K_3)
$$

**Payoff**: Non-negative in all states (can verify by cases).

**No-arbitrage**: Since payoff $\geq 0$, cost must be $\geq 0$:

$$
C(K_1) - 2C(K_2) + C(K_3) \geq 0
$$

Rearranging:

$$
C(K_2) \leq \frac{C(K_1) + C(K_3)}{2}
$$

This is the **convexity constraint** for call prices. ✓

### 2. **Continuous Version**


For infinitesimally close strikes:

$$
\frac{\partial^2 C}{\partial K^2} \geq 0
$$

From Black-Scholes:

$$
\frac{\partial^2 C}{\partial K^2} = e^{-rT}\frac{\mathcal{N}'(d_2)}{K\sigma\sqrt{T}} > 0
$$

Strict convexity holds. ✓

---

## Calendar Spread Inequality

*Section goal: the constraint $C(S, T_1) \leq C(S, T_2)$ and its no-arbitrage proof.*

### 1. **Time Spread Constraint**


For maturities $T_1 < T_2$ with identical strike $K$:

$$
\boxed{C(S, T_1) \leq C(S, T_2)}
$$

**Interpretation**: Longer-dated calls are always worth at least as much as shorter-dated calls.

**Proof**: The longer-dated option can replicate the shorter-dated option by:

1. Hold the longer option until $T_1$
2. Exercise if optimal at $T_1$
3. Or continue holding until $T_2$

This flexibility makes it at least as valuable.

**Black-Scholes verification**: From the formula, $C$ is increasing in $T$. ✓

---

## Arbitrage Bounds Summary


### 1. **Comprehensive Bounds**


For European options on non-dividend-paying stocks:

| Property | Call | Put |
|----------|------|-----|
| **Lower bound** | $\max(S - Ke^{-rT}, 0)$ | $\max(Ke^{-rT} - S, 0)$ |
| **Upper bound** | $S$ | $Ke^{-rT}$ |
| **Monotonicity in $S$** | $\frac{\partial C}{\partial S} > 0$ | $\frac{\partial P}{\partial S} < 0$ |
| **Monotonicity in $T$** | $\frac{\partial C}{\partial T} > 0$ | $\frac{\partial P}{\partial T} > 0$ |
| **Monotonicity in $\sigma$** | $\frac{\partial C}{\partial \sigma} > 0$ | $\frac{\partial P}{\partial \sigma} > 0$ |
| **Monotonicity in $K$** | $\frac{\partial C}{\partial K} < 0$ | $\frac{\partial P}{\partial K} > 0$ |
| **Convexity in $S$** | $\Gamma > 0$ | $\Gamma > 0$ |
| **Convexity in $K$** | $\frac{\partial^2 C}{\partial K^2} > 0$ | $\frac{\partial^2 P}{\partial K^2} > 0$ |

---

## Practical Implications

*Section goal: using these bounds to detect arbitrage in market quotes.*

### 1. **Arbitrage Detection**


Market prices violating these properties suggest:

1. **Arbitrage opportunity**: Execute butterfly, calendar, or conversion spreads
2. **Transaction costs**: Apparent violations within bid-ask spread
3. **Dividend effects**: Non-dividend assumptions violated
4. **Early exercise**: American features not captured

### 2. **Model Validation**


Any pricing model must satisfy:

- All monotonicity conditions
- Convexity constraints
- Upper and lower bounds

Black-Scholes satisfies all of these (as verified above).

### 3. **Greeks Consistency**


The properties imply relationships among Greeks:

- $\Delta \in (0,1)$ for calls (from monotonicity and bounds)
- $\Gamma > 0$ (from convexity)
- $\Theta < 0$ typically (from time decay)
- $\nu > 0$ (from volatility benefit)

These must be consistent for any valid pricing model.

---

## Comparison: American vs. European

*Section goal: when the early-exercise premium vanishes (calls on non-dividend stocks) and when it does not (puts).*

For American options on non-dividend-paying stocks:

### 1. **Call Options**


$$
C_{\text{American}} = C_{\text{European}}
$$

**Reason**: Never optimal to exercise early (forgo time value and interest on strike).

### 2. **Put Options**


$$
P_{\text{American}} \geq P_{\text{European}}
$$

**Reason**: Early exercise can be optimal when deep ITM (capture strike immediately rather than wait).

**Bound**:

$$
\max(K - S, 0) \leq P_{\text{American}} \leq K
$$

Note: American put lower bound is *intrinsic value*, not discounted intrinsic value.

---

## Summary


European option prices under Black-Scholes satisfy rigorous mathematical properties:

**Bounds**:

- Calls: $(S - Ke^{-rT})^+ \leq C \leq S$
- Puts: $(Ke^{-rT} - S)^+ \leq P \leq Ke^{-rT}$

**Monotonicity**:

- Increasing in $S$ (calls), $T$, $\sigma$
- Decreasing in $K$ (calls), increasing in $K$ (puts)

**Convexity**:

- Convex in $S$ (positive gamma)
- Convex in $K$ (butterfly constraint)

**Significance**:

1. **Arbitrage detection**: Violations indicate mispricing
2. **Model validation**: Any valid model must satisfy these
3. **Hedging implications**: Convexity drives dynamic hedging needs
4. **Greeks relationships**: Properties constrain sensitivities

These properties are more fundamental than the specific Black-Scholes formula—they follow from no-arbitrage alone and apply to any option pricing model.

---

## Exercises

**Exercise 1.** A European call is quoted at $C = 12$ with $S = 100$, $K = 95$, $r = 4\%$, and $T = 0.5$ years. Verify that the call price satisfies both the upper bound $C \leq S$ and the lower bound $C \geq \max(S - Ke^{-rT}, 0)$. What is the time value of the option?

??? success "Solution to Exercise 1"
    **Given**: $C = 12$, $S = 100$, $K = 95$, $r = 0.04$, $T = 0.5$.

    **Upper bound check**: $C = 12 \leq 100 = S$ ✓

    **Lower bound**: $\max(S - Ke^{-rT}, 0) = \max(100 - 95e^{-0.02}, 0) = \max(100 - 93.12, 0) = 6.88$.

    $C = 12 \geq 6.88$ ✓

    Both bounds are satisfied.

    **Time value**: The intrinsic value is $\max(S - K, 0) = \max(100 - 95, 0) = 5$.

    $$
    \text{Time value} = C - \text{Intrinsic value} = 12 - 5 = 7
    $$

    The option's time value is $\$7$, representing the value of optionality (the chance of further favorable moves and the interest savings from deferring the strike payment).

---
**Exercise 2.** Prove the butterfly spread inequality: for strikes $K_1 < K_2 < K_3$ with $K_2 = \frac{K_1 + K_3}{2}$, show that

$$
C(K_2) \leq \frac{C(K_1) + C(K_3)}{2}
$$

by constructing a butterfly spread portfolio and arguing that its payoff is non-negative in all states.

??? success "Solution to Exercise 2"
    Consider the butterfly spread portfolio: buy 1 call at $K_1$, sell 2 calls at $K_2 = \frac{K_1+K_3}{2}$, buy 1 call at $K_3$.

    The payoff at maturity is $\Pi(S_T) = (S_T - K_1)^+ - 2(S_T - K_2)^+ + (S_T - K_3)^+$.

    **Case 1: $S_T \leq K_1$**

    All calls expire worthless: $\Pi = 0 - 0 + 0 = 0 \geq 0$.

    **Case 2: $K_1 < S_T \leq K_2$**

    $$
    \Pi = (S_T - K_1) - 0 + 0 = S_T - K_1 > 0
    $$

    **Case 3: $K_2 < S_T \leq K_3$**

    $$
    \Pi = (S_T - K_1) - 2(S_T - K_2) + 0 = -S_T + 2K_2 - K_1 = K_3 - S_T
    $$

    since $2K_2 - K_1 = K_3$. Since $S_T \leq K_3$, we have $\Pi = K_3 - S_T \geq 0$.

    **Case 4: $S_T > K_3$**

    $$
    \Pi = (S_T - K_1) - 2(S_T - K_2) + (S_T - K_3) = -K_1 + 2K_2 - K_3 = 0
    $$

    In all cases $\Pi \geq 0$. By no-arbitrage, a portfolio with non-negative payoff must have non-negative cost:

    $$
    C(K_1) - 2C(K_2) + C(K_3) \geq 0
    $$

    Rearranging: $C(K_2) \leq \frac{C(K_1) + C(K_3)}{2}$.

---
**Exercise 3.** Compute the delta $\Delta = \mathcal{N}(d_1)$, gamma $\Gamma = \frac{\mathcal{N}'(d_1)}{S\sigma\sqrt{T}}$, and vega $\nu = S\sqrt{T}\,\mathcal{N}'(d_1)$ for a call with $S = 50$, $K = 50$, $r = 3\%$, $\sigma = 20\%$, $T = 1$. Verify that $\Delta \in (0, 1)$, $\Gamma > 0$, and $\nu > 0$.

??? success "Solution to Exercise 3"
    **Parameters**: $S = 50$, $K = 50$, $r = 0.03$, $\sigma = 0.20$, $T = 1$.

    $$
    d_1 = \frac{\ln(1) + (0.03 + 0.02) \times 1}{0.20} = \frac{0.05}{0.20} = 0.25
    $$

    Standard normal values: $\mathcal{N}(0.25) = 0.5987$, $\mathcal{N}'(0.25) = \phi(0.25) = \frac{1}{\sqrt{2\pi}}e^{-0.03125} = 0.3867$.

    **Delta**:

    $$
    \Delta = \mathcal{N}(d_1) = 0.5987
    $$

    Check: $\Delta \in (0, 1)$ ✓

    **Gamma**:

    $$
    \Gamma = \frac{\mathcal{N}'(d_1)}{S\sigma\sqrt{T}} = \frac{0.3867}{50 \times 0.20 \times 1} = \frac{0.3867}{10} = 0.03867
    $$

    Check: $\Gamma > 0$ ✓

    **Vega**:

    $$
    \nu = S\sqrt{T}\,\mathcal{N}'(d_1) = 50 \times 1 \times 0.3867 = 19.34
    $$

    Check: $\nu > 0$ ✓

    All three conditions are verified, consistent with the theoretical properties of European options.

---
**Exercise 4.** Show that gamma is the same for a European call and put with the same strike and maturity. Start from put-call parity $P = C - S + Ke^{-rT}$ and differentiate twice with respect to $S$.

??? success "Solution to Exercise 4"
    From put-call parity:

    $$
    P = C - S + Ke^{-rT}
    $$

    Differentiate once with respect to $S$:

    $$
    \frac{\partial P}{\partial S} = \frac{\partial C}{\partial S} - 1
    $$

    Differentiate again:

    $$
    \frac{\partial^2 P}{\partial S^2} = \frac{\partial^2 C}{\partial S^2}
    $$

    That is:

    $$
    \Gamma_{\text{put}} = \Gamma_{\text{call}}
    $$

    The second derivative of $Ke^{-rT}$ (a constant with respect to $S$) is zero, and the second derivative of $-S$ is also zero. Therefore the gamma of the put equals the gamma of the call for options with the same strike and maturity. This also follows intuitively: gamma measures the curvature of the option price with respect to $S$, and since put and call prices differ by a linear function of $S$, their curvatures are identical.

---
**Exercise 5.** A market maker observes the following call prices for three strikes with the same maturity: $C(90) = 15.20$, $C(100) = 9.50$, $C(110) = 5.80$. Check whether the convexity condition $C(100) \leq \frac{C(90) + C(110)}{2}$ holds. If violated, describe the arbitrage strategy.

??? success "Solution to Exercise 5"
    Check convexity: $\frac{C(90) + C(110)}{2} = \frac{15.20 + 5.80}{2} = 10.50$.

    Compare with $C(100) = 9.50$.

    Since $9.50 \leq 10.50$, the convexity condition $C(100) \leq \frac{C(90) + C(110)}{2}$ **holds**. ✓

    There is no arbitrage opportunity. The butterfly spread (buy $C(90)$, sell $2 \times C(100)$, buy $C(110)$) costs $15.20 - 2(9.50) + 5.80 = 2.00 > 0$, which is consistent with its non-negative payoff. If the condition had been violated (say $C(100) = 11.00 > 10.50$), one would sell the butterfly (sell $C(90)$, buy $2 \times C(100)$, sell $C(110)$) to collect a positive upfront cash flow with a non-positive future liability.

---
**Exercise 6.** Explain why an American call on a non-dividend-paying stock is never exercised early. Use the lower bound $C \geq S - Ke^{-rT} > S - K$ (for $r > 0$ and $T > 0$) to argue that the option is always worth more alive than dead.

??? success "Solution to Exercise 6"
    For a European call on a non-dividend-paying stock, the no-arbitrage lower bound is:

    $$
    C \geq \max(S - Ke^{-rT}, 0) \geq S - Ke^{-rT}
    $$

    When $r > 0$ and $T > 0$: $e^{-rT} < 1$, so $Ke^{-rT} < K$, which gives:

    $$
    C \geq S - Ke^{-rT} > S - K
    $$

    If the American call were exercised early, the holder would receive $S - K$ (the intrinsic value). But the option is worth at least $S - Ke^{-rT} > S - K$, so exercising destroys value equal to at least $K(1 - e^{-rT}) > 0$.

    This excess value has two components:

    1. **Time value of money**: By not exercising, the holder defers paying $K$, earning interest $K(1 - e^{-rT})$ on the deferred payment.
    2. **Insurance value**: The option protects against the stock falling below $K$; early exercise forfeits this downside protection.

    Since the option alive is always worth more than the exercise value $S - K$, early exercise is never optimal for an American call on a non-dividend-paying stock.

---
**Exercise 7.** The Black-Scholes theta for a call is

$$
\Theta = -\frac{S\mathcal{N}'(d_1)\sigma}{2\sqrt{T}} - rKe^{-rT}\mathcal{N}(d_2)
$$

Show that both terms are negative, so $\Theta < 0$ in general. Under what limiting conditions (deep ITM, near expiration) might the interest rate term dominate the volatility term? Can theta ever be positive for a European call on a non-dividend-paying stock?

??? success "Solution to Exercise 7"
    The theta formula is:

    $$
    \Theta = -\underbrace{\frac{S\mathcal{N}'(d_1)\sigma}{2\sqrt{T}}}_{\text{Term 1}} - \underbrace{rKe^{-rT}\mathcal{N}(d_2)}_{\text{Term 2}}
    $$

    **Term 1**: $S > 0$, $\mathcal{N}'(d_1) = \phi(d_1) > 0$, $\sigma > 0$, $\sqrt{T} > 0$, so Term 1 is strictly positive, making $-\text{Term 1} < 0$.

    **Term 2**: $r > 0$, $K > 0$, $e^{-rT} > 0$, $\mathcal{N}(d_2) > 0$, so Term 2 is strictly positive, making $-\text{Term 2} < 0$.

    Both terms are negative, so $\Theta < 0$ in general when $r > 0$.

    **When the interest rate term dominates**: For deep ITM calls ($S \gg K$), $d_1 \to +\infty$, so $\mathcal{N}'(d_1) = \phi(d_1) \to 0$ (the volatility term vanishes since the normal density decays rapidly). Meanwhile $\mathcal{N}(d_2) \to 1$, so Term 2 $\to rKe^{-rT}$, which remains bounded and positive. In this regime, theta is dominated by the interest rate term.

    **Can theta be positive?** For a European call on a non-dividend-paying stock with $r > 0$, theta is always negative (both terms have the same sign). However, if we consider the edge case $r = 0$, Term 2 vanishes and $\Theta = -\frac{S\phi(d_1)\sigma}{2\sqrt{T}} < 0$ still.

    In practice, theta can become very slightly positive for deep ITM European calls on dividend-paying stocks (or for European puts), but for calls on non-dividend-paying stocks, $\Theta \leq 0$ always holds (with equality only in degenerate limits).
