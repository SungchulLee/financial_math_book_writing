# Asymptotic Behavior of the Black-Scholes Formula


The Black-Scholes formula exhibits well-defined **limiting behavior** as parameters approach extreme values. Understanding these limits provides intuition for how options behave in different market conditions and serves as a check for numerical implementations.

This section systematically analyzes the asymptotic behavior of option prices.

---

## Limits in Stock Price


### 1. **As $S \to \infty$ (Deep In-the-Money Call)**


**Behavior of $d_1$ and $d_2$**:

$$
d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}} \to +\infty
$$

$$
d_2 = d_1 - \sigma\sqrt{T} \to +\infty
$$

**Cumulative probabilities**:

$$
\mathcal{N}(d_1), \mathcal{N}(d_2) \to 1
$$

**Call price**:

$$
\begin{aligned}
C &= S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2) \\
&\to S \cdot 1 - Ke^{-rT} \cdot 1 \\
&= S - Ke^{-rT}
\end{aligned}
$$

**Interpretation**: Deep ITM call behaves like **forward contract** with guaranteed exercise. The option value equals the stock price minus the present value of the strike.

**Put price** (via put-call parity):

$$
P = C - S + Ke^{-rT} \to 0
$$

Deep OTM put becomes worthless.

---

### 2. **As $S \to 0$ (Deep Out-of-the-Money Call)**


**Behavior of $d_1$ and $d_2$**:

$$
d_1, d_2 \to -\infty
$$

**Cumulative probabilities**:

$$
\mathcal{N}(d_1), \mathcal{N}(d_2) \to 0
$$

**Call price**:

$$
C \to S \cdot 0 - Ke^{-rT} \cdot 0 = 0
$$

**Put price**:

$$
\begin{aligned}
P &= Ke^{-rT}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1) \\
&\to Ke^{-rT} \cdot 1 - 0 \cdot 0 \\
&= Ke^{-rT}
\end{aligned}
$$

**Interpretation**: Deep ITM put approaches the present value of the strike minus essentially zero stock value.

---

## Limits in Time to Maturity


### 1. **As $T \to 0$ (Approaching Expiration)**


**Case 1: $S > K$ (ITM call)**

As $T \to 0$:

$$
\ln(S/K) > 0 \text{ dominates}, \quad d_1, d_2 \to +\infty
$$

$$
C \to S - K
$$

**Case 2: $S < K$ (OTM call)**

As $T \to 0$:

$$
\ln(S/K) < 0 \text{ dominates}, \quad d_1, d_2 \to -\infty
$$

$$
C \to 0
$$

**Case 3: $S = K$ (ATM call)**

This requires careful analysis. As $T \to 0$ with $S = K$:

$$
d_1 = \frac{(r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}} = \frac{(r + \frac{1}{2}\sigma^2)\sqrt{T}}{\sigma} \to 0
$$

$$
d_2 = \frac{(r - \frac{1}{2}\sigma^2)\sqrt{T}}{\sigma} \to 0
$$

$$
\mathcal{N}(d_1), \mathcal{N}(d_2) \to \mathcal{N}(0) = 0.5
$$

$$
C \to K \cdot 0.5 - K \cdot 1 \cdot 0.5 = 0
$$

**Summary**: As expiration approaches:

$$
\boxed{\lim_{T \to 0} C(S,T) = \max(S - K, 0) = (S-K)^+}
$$

This recovers the **terminal payoff condition**.

---

### 2. **As $T \to \infty$ (Very Long Maturity)**


**Behavior of $d_1$ and $d_2$**:

For fixed $S, K, r, \sigma$:

$$
d_1 = \frac{\ln(S/K)}{\sigma\sqrt{T}} + \frac{(r + \frac{1}{2}\sigma^2)\sqrt{T}}{\sigma}
$$

The second term dominates:

$$
d_1 \sim \frac{(r + \frac{1}{2}\sigma^2)\sqrt{T}}{\sigma} \to +\infty
$$

Similarly $d_2 \to +\infty$.

**Call price**:

$$
\begin{aligned}
C &= S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2) \\
&\to S \cdot 1 - K \cdot 0 \cdot 1 \\
&= S
\end{aligned}
$$

**Interpretation**: With infinite time, the call becomes equivalent to owning the stock (since there's certainty of finishing ITM and the strike payment becomes negligible after discounting).

**Put price**:

$$
P \to Ke^{-rT} - S \cdot 0 \to 0
$$

Long-dated puts become worthless (stock will almost certainly be above strike eventually).

---

## Limits in Volatility


### 1. **As $\sigma \to 0$ (Zero Volatility)**


**Deterministic evolution**: Stock grows at risk-free rate:

$$
S_T = S_0 e^{rT}
$$

**Case 1: $S_0 > Ke^{-rT}$** (Forward price above strike)

Stock will certainly finish above $K$:

$$
C \to S_0 - Ke^{-rT}
$$

**Case 2: $S_0 < Ke^{-rT}$** (Forward price below strike)

Stock will certainly finish below $K$:

$$
C \to 0
$$

**Case 3: $S_0 = Ke^{-rT}$** (Exactly ATM forward)

$$
C \to 0
$$

**Summary**:

$$
\boxed{\lim_{\sigma \to 0} C = \max(S_0 - Ke^{-rT}, 0)}
$$

This is the **forward value** with no volatility premium.

**Put limit**:

$$
\lim_{\sigma \to 0} P = \max(Ke^{-rT} - S_0, 0)
$$

---

### 2. **As $\sigma \to \infty$ (Infinite Volatility)**


**Behavior of $d_1$ and $d_2$**:

$$
d_1 = \frac{\ln(S/K)}{\sigma\sqrt{T}} + \frac{(r + \frac{1}{2}\sigma^2)\sqrt{T}}{\sigma}
$$

As $\sigma \to \infty$:

- First term: $\frac{\ln(S/K)}{\sigma\sqrt{T}} \to 0$
- Second term: $\frac{(r + \frac{1}{2}\sigma^2)\sqrt{T}}{\sigma} = \frac{r\sqrt{T}}{\sigma} + \frac{\sigma\sqrt{T}}{2} \to +\infty$

Therefore $d_1 \to +\infty$ and $\mathcal{N}(d_1) \to 1$.

For $d_2$:

$$
d_2 = d_1 - \sigma\sqrt{T} \to +\infty - \infty
$$

This is indeterminate. More carefully:

$$
d_2 = \frac{\ln(S/K)}{\sigma\sqrt{T}} + \frac{r\sqrt{T}}{\sigma} - \frac{\sigma\sqrt{T}}{2}
$$

As $\sigma \to \infty$, the last term dominates:

$$
d_2 \to -\infty, \quad \mathcal{N}(d_2) \to 0
$$

**Call price**:

$$
C \to S \cdot 1 - Ke^{-rT} \cdot 0 = S
$$

**Interpretation**: With infinite volatility, the call is worth the full stock price (no chance of finishing OTM since variance dominates everything).

**Put price**: From put-call parity:

$$
P = C - S + Ke^{-rT} \to S - S + Ke^{-rT} = Ke^{-rT}
$$

Infinite volatility gives the put its maximum possible value (present value of strike).

---

## Limits in Interest Rate


### 1. **As $r \to 0$ (Zero Interest Rate)**


**Call formula**:

$$
C \to S\mathcal{N}(d_1) - K\mathcal{N}(d_2)
$$

where:

$$
d_1 = \frac{\ln(S/K) + \frac{1}{2}\sigma^2 T}{\sigma\sqrt{T}}, \quad d_2 = d_1 - \sigma\sqrt{T}
$$

**Put-call parity** becomes:

$$
C - P = S - K
$$

(no discounting since $e^{-r \cdot 0} = 1$)

**Interpretation**: Options behave as if cash flows are not discounted.

---

### 2. **As $r \to \infty$ (Infinite Interest Rate)**


**Discounting**: $e^{-rT} \to 0$

**Behavior**: 

$$
d_1 \sim \frac{r\sqrt{T}}{\sigma} \to +\infty
$$

$$
d_2 = d_1 - \sigma\sqrt{T} \to +\infty
$$

**Call price**:

$$
C \to S \cdot 1 - 0 \cdot 1 = S
$$

**Interpretation**: With infinite interest rate, the discounted strike becomes zero, so the call is worth the full stock price.

**Put price**:

$$
P \to 0 \cdot 1 - S \cdot 0 = 0
$$

---

## Limits in Strike Price


### 1. **As $K \to 0$ (Zero Strike)**


**Call**:

$$
\ln(S/K) \to +\infty, \quad d_1, d_2 \to +\infty
$$

$$
C \to S - 0 \cdot e^{-rT} = S
$$

**Interpretation**: Call with zero strike is equivalent to owning the stock (certain to exercise for nothing).

**Put**:

$$
P \to 0
$$

(no value in selling stock for zero)

---

### 2. **As $K \to \infty$ (Infinite Strike)**


**Call**:

$$
\ln(S/K) \to -\infty, \quad d_1, d_2 \to -\infty
$$

$$
C \to 0
$$

(no chance of stock exceeding infinite strike)

**Put**:

$$
P \to Ke^{-rT} - S \to +\infty
$$

But in practice, $P < Ke^{-rT}$ (never exceeds max theoretical payoff).

---

## ATM Approximation for Small Time


For at-the-money options ($S \approx K$) with small $T$, there's a useful approximation.

### 1. **ATM Call Formula**


When $S = K$ and $T$ is small:

$$
d_1 \approx \frac{\sigma\sqrt{T}}{2}, \quad d_2 \approx -\frac{\sigma\sqrt{T}}{2}
$$

Using Taylor expansion of $\mathcal{N}(x)$ near $x = 0$:

$$
\mathcal{N}(x) \approx \frac{1}{2} + \frac{1}{\sqrt{2\pi}}x + O(x^3)
$$

After substitution and simplification:

$$
\boxed{C_{\text{ATM}} \approx S \cdot \frac{\sigma\sqrt{T}}{\sqrt{2\pi}} \approx 0.4 S \sigma \sqrt{T}}
$$

This is the **ATM volatility rule of thumb**: ATM option value is roughly 40% of $S\sigma\sqrt{T}$.

**Example**: $S = 100$, $\sigma = 20\%$, $T = 0.25$ (3 months):

$$
C \approx 0.4 \times 100 \times 0.2 \times 0.5 = 4
$$

---

## Summary Table


| Limit | Call Behavior | Put Behavior |
|-------|---------------|--------------|
| $S \to \infty$ | $C \to S - Ke^{-rT}$ | $P \to 0$ |
| $S \to 0$ | $C \to 0$ | $P \to Ke^{-rT}$ |
| $T \to 0$ | $C \to (S-K)^+$ | $P \to (K-S)^+$ |
| $T \to \infty$ | $C \to S$ | $P \to 0$ |
| $\sigma \to 0$ | $C \to (S-Ke^{-rT})^+$ | $P \to (Ke^{-rT}-S)^+$ |
| $\sigma \to \infty$ | $C \to S$ | $P \to Ke^{-rT}$ |
| $r \to 0$ | Reduces to $C = S\mathcal{N}(d_1) - K\mathcal{N}(d_2)$ | Put-call parity: $C - P = S - K$ |
| $r \to \infty$ | $C \to S$ | $P \to 0$ |
| $K \to 0$ | $C \to S$ | $P \to 0$ |
| $K \to \infty$ | $C \to 0$ | $P \to Ke^{-rT}$ |

---

## Practical Implications


### 1. **1. Sanity Checks**


These limits provide **bounds** for option prices:

- $0 \leq C \leq S$
- $0 \leq P \leq Ke^{-rT}$

Any pricing model violating these bounds is immediately suspect.

### 2. **2. Numerical Stability**


When implementing Black-Scholes:

- For $S \gg K$ or $S \ll K$: Use asymptotic approximations rather than evaluating $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$ with extreme arguments
- For $T \approx 0$: Use intrinsic value directly
- For $\sigma$ very small or large: Use limiting formulas

### 3. **3. Greeks Behavior**


Limiting behavior of prices determines Greeks:

- As $S \to \infty$: $\Delta_{\text{call}} \to 1$, $\Gamma \to 0$
- As $T \to 0$ with $S \neq K$: $\Gamma \to \infty$ (curvature spikes)
- As $\sigma \to 0$: Vega $\to 0$ (no sensitivity to volatility)

### 4. **4. Model Validation**


Real market data should respect these asymptotic behaviors. Violations suggest:

- Model misspecification
- Market frictions (transaction costs, liquidity)
- Early exercise features (American options)

---

## Summary


The Black-Scholes formula exhibits well-defined limiting behavior:

**Key insights**:

1. **Deep ITM call** → Stock minus present value of strike (forward-like)
2. **Near expiration** → Intrinsic value (payoff function)
3. **Long maturity** → Call worth stock, put worthless
4. **Zero volatility** → Forward value only
5. **Infinite volatility** → Call worth stock, put worth PV of strike

These limits provide:

- Intuitive understanding of option behavior
- Numerical stability checks
- Model validation criteria
- Bounds for arbitrage detection

Understanding asymptotic behavior is essential for both theoretical analysis and practical implementation of option pricing models.
