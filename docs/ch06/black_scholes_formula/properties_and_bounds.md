# Properties and Bounds of Option Prices


Option prices satisfy fundamental mathematical properties that follow from no-arbitrage principles. These properties—monotonicity, convexity, and bounds—provide constraints that any valid pricing model must respect and enable arbitrage detection in practice.

This section rigorously establishes these properties for European options under the Black-Scholes framework.

---

## Fundamental Bounds


### 1. **Call Option Bounds**


For a European call option on a non-dividend-paying stock:

$$
\boxed{\max(S - Ke^{-r(T-t)}, 0) \leq C(S,t) \leq S}
$$

**Lower bound**: The call cannot be worth less than its discounted intrinsic value (otherwise arbitrage exists)

**Upper bound**: The call cannot exceed the stock price (option gives right to buy stock, not worth more than owning it)

**Tighter lower bound**: 

$$
C(S,t) \geq \max(S - Ke^{-r(T-t)}, 0)
$$

This is the **no-arbitrage lower bound**.

### 2. **Put Option Bounds**


For a European put:

$$
\boxed{\max(Ke^{-r(T-t)} - S, 0) \leq P(S,t) \leq Ke^{-r(T-t)}}
$$

**Lower bound**: Put worth at least discounted intrinsic value

**Upper bound**: Put cannot exceed present value of strike (max possible payoff)

### 3. **Verification for Black-Scholes**


**Lower bound for call**:

Since $\mathcal{N}(d_1), \mathcal{N}(d_2) \in [0,1]$:

When $S > Ke^{-rT}$:

$$
C = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2) \geq S \cdot 0 - Ke^{-rT} \cdot 1
$$

But more carefully, when deeply ITM, $\mathcal{N}(d_1), \mathcal{N}(d_2) \approx 1$:

$$
C \approx S - Ke^{-rT}
$$

**Upper bound**:

$$
C = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2) \leq S \cdot 1 - Ke^{-rT} \cdot 0 = S
$$

Both bounds satisfied. ✓

---

## Monotonicity in Stock Price


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

The cross-terms cancel (due to Black-Scholes PDE), leaving:

$$
\frac{\partial C}{\partial S} = \mathcal{N}(d_1)
$$

Since $\mathcal{N}(d_1) \in (0,1)$ for all finite $d_1$, the call is strictly increasing in $S$. ✓

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

---

## Monotonicity in Time


### 1. **Time Decay (Theta)**


For European calls on non-dividend-paying stocks:

$$
\frac{\partial C}{\partial t} = -\Theta < 0
$$

**Interpretation**: Call price **decreases** as time passes (all else equal), a phenomenon called **time decay**.

**Theta formula**:

$$
\Theta_{\text{call}} = -\frac{S\mathcal{N}'(d_1)\sigma}{2\sqrt{T-t}} - rKe^{-r(T-t)}\mathcal{N}(d_2)
$$

Since both terms are negative, $\Theta < 0$ (time decay).

**Exception**: Deep ITM European calls can have slightly positive theta near expiration due to interest earned on deferred strike payment.

### 2. **Increasing with Time to Maturity**


$$
\boxed{\frac{\partial C}{\partial T} > 0}
$$

**Interpretation**: Longer-dated options are more valuable (more time for favorable price movement).

**Proof**: Options with more time have:

1. Greater probability of finishing ITM
2. Higher optionality value
3. More uncertainty (higher variance $\sigma^2 T$)

From the formula, as $T$ increases, $d_1$ and $d_2$ shift, and the net effect is positive:

$$
C(S, T_2) > C(S, T_1) \quad \text{for } T_2 > T_1
$$

---

## Monotonicity in Volatility


### 1. **Vega (Volatility Sensitivity)**


$$
\boxed{\frac{\partial C}{\partial \sigma} = S\sqrt{T-t}\,\mathcal{N}'(d_1) > 0}
$$

**Interpretation**: Call (and put) prices are **strictly increasing** in volatility.

**Vega formula**:

$$
\nu = S\sqrt{T}\,\mathcal{N}'(d_1) = S\sqrt{T}\frac{1}{\sqrt{2\pi}}e^{-d_1^2/2} > 0
$$

**Economic intuition**: Higher volatility increases the probability of large moves. For options (with capped downside but unlimited upside), this increases value.

**Key property**: Vega is the same for calls and puts with identical strike and maturity:

$$
\nu_{\text{call}} = \nu_{\text{put}}
$$

This follows from put-call parity (volatility affects both equally).

---

## Monotonicity in Strike


### 1. **Call Options**


$$
\boxed{\frac{\partial C}{\partial K} = -e^{-r(T-t)}\mathcal{N}(d_2) < 0}
$$

**Interpretation**: Call price is **strictly decreasing** in strike.

**Proof**: Higher strike means:
- Lower intrinsic value
- Lower probability of exercise
- Less favorable payoff structure

From the formula:

$$
\frac{\partial C}{\partial K} = -e^{-rT}\mathcal{N}(d_2) - \text{(other terms that sum to zero)}
$$

### 2. **Put Options**


$$
\boxed{\frac{\partial P}{\partial K} = e^{-r(T-t)}\mathcal{N}(-d_2) > 0}
$$

**Interpretation**: Put price is **strictly increasing** in strike (higher strike = more valuable right to sell).

---

## Convexity in Stock Price


### 1. **Second Derivative (Gamma)**


$$
\boxed{\Gamma = \frac{\partial^2 C}{\partial S^2} = \frac{\mathcal{N}'(d_1)}{S\sigma\sqrt{T-t}} > 0}
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

---

## Convexity in Strike (Butterfly Spread)


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
