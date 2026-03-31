# Asymptotic Behavior of the Black-Scholes Formula


The Black-Scholes formula exhibits well-defined **limiting behavior** as parameters approach extreme values. Understanding these limits provides intuition for how options behave in different market conditions and serves as a check for numerical implementations.

This section systematically analyzes the asymptotic behavior of option prices.

---

## Limits in Stock Price


### 1. **As S → ∞ (Deep In-the-Money Call)**


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

### 2. **As S → 0 (Deep Out-of-the-Money Call)**


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


### 1. **As T → 0 (Approaching Expiration)**


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

### 2. **As T → ∞ (Very Long Maturity)**


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


### 1. **As σ → 0 (Zero Volatility)**


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

### 2. **As σ → ∞ (Infinite Volatility)**


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


### 1. **As r → 0 (Zero Interest Rate)**


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

### 2. **As r → ∞ (Infinite Interest Rate)**


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


### 1. **As K → 0 (Zero Strike)**


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

### 2. **As K → ∞ (Infinite Strike)**


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

---

## Exercises

**Exercise 1.** Let $C(S, K, T, r, \sigma)$ denote the Black-Scholes call price. Prove rigorously that

$$
\lim_{S \to \infty} \frac{C(S, K, T, r, \sigma)}{S} = 1
$$

by analyzing the rate at which $\mathcal{N}(d_1) \to 1$ as $S \to \infty$. What does this tell you about the delta of a deep in-the-money call?

---

**Exercise 2.** For an at-the-money call ($S = K$) with $r = 0$, use the Taylor expansion of $\mathcal{N}(x)$ around $x = 0$ to show that the call price satisfies

$$
C \approx \frac{S \sigma \sqrt{T}}{\sqrt{2\pi}}
$$

for small $T$. Compute the percentage error of this approximation relative to the exact Black-Scholes price when $S = K = 100$, $\sigma = 0.25$, $r = 0$, and $T = 0.01$.

---

**Exercise 3.** Consider the put price $P$ as $\sigma \to \infty$. Show from the Black-Scholes formula (not from put-call parity) that $P \to Ke^{-rT}$. Explain the financial intuition: why should the put attain its maximum theoretical value when volatility is infinite?

---

**Exercise 4.** Examine the behavior of the Black-Scholes call price as $r \to -\infty$ (negative interest rates). Determine $\lim_{r \to -\infty} d_1$, $\lim_{r \to -\infty} d_2$, and $\lim_{r \to -\infty} C$. Is the result consistent with the economic interpretation of a very negative interest rate?

---

**Exercise 5.** The summary table states that as $T \to \infty$, the put price satisfies $P \to 0$. However, this assumes $r > 0$. What happens to $\lim_{T \to \infty} P$ when $r = 0$? Prove your answer by carefully analyzing $d_1$ and $d_2$ in this special case.

---

**Exercise 6.** Using the ATM approximation $C_{\text{ATM}} \approx 0.4 \, S \sigma \sqrt{T}$, derive an approximate formula for the ATM implied volatility $\sigma_{\text{impl}}$ given a market price $C_{\text{mkt}}$ of an at-the-money call. Apply your formula to find the approximate implied volatility when $S = 50$, $T = 0.25$, and $C_{\text{mkt}} = 2.00$.

---

**Exercise 7.** Consider the ratio of a European put to a European call, $P/C$, for a fixed strike $K$ and maturity $T$. Determine

$$
\lim_{\sigma \to 0^+} \frac{P(S, K, T, r, \sigma)}{C(S, K, T, r, \sigma)}
$$

for the three cases $S > Ke^{-rT}$, $S < Ke^{-rT}$, and $S = Ke^{-rT}$. Discuss why the $S = Ke^{-rT}$ case requires careful treatment.

---

## Solutions

??? success "Solution to Exercise 1"
    We need to show $\lim_{S \to \infty} C/S = 1$. From the Black-Scholes formula:

    $$
    \frac{C}{S} = \mathcal{N}(d_1) - \frac{Ke^{-rT}}{S}\mathcal{N}(d_2)
    $$

    As $S \to \infty$, we have $d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}} \to +\infty$, so $\mathcal{N}(d_1) \to 1$. Similarly $d_2 \to +\infty$, so $\mathcal{N}(d_2) \to 1$.

    For the second term, $\frac{Ke^{-rT}}{S} \to 0$ while $\mathcal{N}(d_2) \to 1$, so $\frac{Ke^{-rT}}{S}\mathcal{N}(d_2) \to 0$.

    To analyze the rate, note that for large $x$, $1 - \mathcal{N}(x) \sim \frac{\phi(x)}{x}$ where $\phi$ is the standard normal density. Since $d_1 \sim \frac{\ln S}{\sigma\sqrt{T}}$ for large $S$:

    $$
    1 - \mathcal{N}(d_1) \sim \frac{\phi(d_1)}{d_1} \sim \frac{\sigma\sqrt{T}}{\ln S} \cdot \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{(\ln S)^2}{2\sigma^2 T}\right)
    $$

    This decays faster than any power of $S$, so $\mathcal{N}(d_1) \to 1$ extremely rapidly. Therefore:

    $$
    \frac{C}{S} = \mathcal{N}(d_1) - \frac{Ke^{-rT}}{S}\mathcal{N}(d_2) \to 1 - 0 = 1
    $$

    For the delta interpretation: since $\Delta = \frac{\partial C}{\partial S} = \mathcal{N}(d_1)$ and $d_1 \to +\infty$ as $S \to \infty$, we get $\Delta \to 1$. This means a deep in-the-money call behaves like holding the stock itself, with a one-to-one response to stock price changes.

??? success "Solution to Exercise 2"
    With $S = K$ and $r = 0$, we have:

    $$
    d_1 = \frac{\ln(1) + \frac{1}{2}\sigma^2 T}{\sigma\sqrt{T}} = \frac{\sigma\sqrt{T}}{2}
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T} = -\frac{\sigma\sqrt{T}}{2}
    $$

    For small $T$, let $\epsilon = \frac{\sigma\sqrt{T}}{2}$. Using the Taylor expansion $\mathcal{N}(x) \approx \frac{1}{2} + \frac{x}{\sqrt{2\pi}}$ for small $x$:

    $$
    \mathcal{N}(d_1) \approx \frac{1}{2} + \frac{\epsilon}{\sqrt{2\pi}}, \quad \mathcal{N}(d_2) \approx \frac{1}{2} - \frac{\epsilon}{\sqrt{2\pi}}
    $$

    With $r = 0$, the call price is:

    $$
    C = S\mathcal{N}(d_1) - K\mathcal{N}(d_2) = S\left(\frac{1}{2} + \frac{\epsilon}{\sqrt{2\pi}}\right) - S\left(\frac{1}{2} - \frac{\epsilon}{\sqrt{2\pi}}\right) = \frac{2S\epsilon}{\sqrt{2\pi}}
    $$

    Substituting $\epsilon = \frac{\sigma\sqrt{T}}{2}$:

    $$
    C \approx \frac{2S}{2\sqrt{2\pi}} \cdot \sigma\sqrt{T} = \frac{S\sigma\sqrt{T}}{\sqrt{2\pi}}
    $$

    **Numerical check** with $S = K = 100$, $\sigma = 0.25$, $r = 0$, $T = 0.01$:

    Approximation: $C_{\text{approx}} = \frac{100 \times 0.25 \times \sqrt{0.01}}{\sqrt{2\pi}} = \frac{100 \times 0.25 \times 0.1}{\sqrt{2\pi}} = \frac{2.5}{2.5066} \approx 0.9974$.

    Exact: $d_1 = \frac{0.25\sqrt{0.01}}{2} = 0.0125$, $d_2 = -0.0125$.

    $$
    C_{\text{exact}} = 100\,\mathcal{N}(0.0125) - 100\,\mathcal{N}(-0.0125) = 100(0.50499 - 0.49501) = 0.9974
    $$

    Percentage error: $\frac{|0.9974 - 0.9974|}{0.9974} \approx 0.003\%$, which is negligible for small $T$.

??? success "Solution to Exercise 3"
    The Black-Scholes put formula is:

    $$
    P = Ke^{-rT}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)
    $$

    As $\sigma \to \infty$, recall from the main text that $d_1 \to +\infty$ and $d_2 \to -\infty$. Therefore:

    $$
    \mathcal{N}(-d_1) = 1 - \mathcal{N}(d_1) \to 1 - 1 = 0
    $$

    $$
    \mathcal{N}(-d_2) = 1 - \mathcal{N}(d_2) \to 1 - 0 = 1
    $$

    Substituting into the put formula:

    $$
    P \to Ke^{-rT} \cdot 1 - S \cdot 0 = Ke^{-rT}
    $$

    **Financial intuition**: When volatility is infinite, the stock price at maturity is essentially unpredictable, with arbitrarily large swings in either direction. The put holder benefits from downward moves (payoff $K - S_T$ when $S_T < K$), and with infinite volatility, the probability of the stock finishing near zero becomes significant. The maximum payoff of a put is $K$ (when $S_T = 0$), and with infinite volatility, the expected discounted payoff approaches $Ke^{-rT}$. This is the theoretical maximum value for a European put: the present value of the strike, corresponding to the scenario where the stock is almost certainly worthless at expiration.

??? success "Solution to Exercise 4"
    As $r \to -\infty$:

    $$
    d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
    $$

    The term $(r + \frac{1}{2}\sigma^2)T \to -\infty$, so $d_1 \to -\infty$.

    $$
    d_2 = d_1 - \sigma\sqrt{T} \to -\infty
    $$

    Therefore $\mathcal{N}(d_1) \to 0$ and $\mathcal{N}(d_2) \to 0$.

    For the call price:

    $$
    C = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)
    $$

    The first term $S\mathcal{N}(d_1) \to 0$.

    For the second term, $e^{-rT} \to +\infty$ as $r \to -\infty$, but $\mathcal{N}(d_2) \to 0$. We need to evaluate $Ke^{-rT}\mathcal{N}(d_2)$ more carefully. Using the asymptotic $\mathcal{N}(x) \sim \frac{\phi(x)}{|x|}$ for $x \to -\infty$ and substituting $d_2 \approx \frac{rT}{\sigma\sqrt{T}} = \frac{r\sqrt{T}}{\sigma}$:

    $$
    Ke^{-rT}\mathcal{N}(d_2) \sim Ke^{-rT} \cdot \frac{1}{|d_2|\sqrt{2\pi}} \exp\left(-\frac{d_2^2}{2}\right) \sim Ke^{-rT} \cdot \frac{\sigma}{|r|\sqrt{T}\sqrt{2\pi}} \exp\left(-\frac{r^2 T}{2\sigma^2}\right)
    $$

    Since $e^{-rT} = e^{|r|T}$ grows only exponentially while $e^{-r^2 T/(2\sigma^2)}$ decays as a Gaussian in $r$, the product goes to $0$ as $r \to -\infty$.

    Therefore:

    $$
    \lim_{r \to -\infty} C = 0
    $$

    **Economic interpretation**: A very negative interest rate means cash is extremely expensive to hold, and the present value of the strike $Ke^{-rT} \to +\infty$. The forward price $Se^{rT} \to 0$, meaning the stock is expected to lose nearly all its value under the risk-neutral measure. The option to buy the stock at any positive strike is worthless because the stock itself becomes worthless in forward terms. This is consistent: no rational agent would pay for the right to buy an asset whose risk-neutral expected value vanishes.

??? success "Solution to Exercise 5"
    When $r = 0$, the stock price dynamics under $\mathbb{Q}$ are $dS_t = \sigma S_t dW_t$ (pure martingale).

    $$
    d_1 = \frac{\ln(S/K) + \frac{1}{2}\sigma^2 T}{\sigma\sqrt{T}} = \frac{\ln(S/K)}{\sigma\sqrt{T}} + \frac{\sigma\sqrt{T}}{2}
    $$

    As $T \to \infty$: the first term $\frac{\ln(S/K)}{\sigma\sqrt{T}} \to 0$, while the second term $\frac{\sigma\sqrt{T}}{2} \to +\infty$.

    So $d_1 \to +\infty$ and $\mathcal{N}(d_1) \to 1$.

    $$
    d_2 = d_1 - \sigma\sqrt{T} = \frac{\ln(S/K)}{\sigma\sqrt{T}} - \frac{\sigma\sqrt{T}}{2} \to -\infty
    $$

    So $\mathcal{N}(d_2) \to 0$.

    The put price (with $r = 0$, so $e^{-rT} = 1$):

    $$
    P = K\mathcal{N}(-d_2) - S\mathcal{N}(-d_1) \to K \cdot 1 - S \cdot 0 = K
    $$

    Therefore $\lim_{T \to \infty} P = K$ when $r = 0$.

    This contrasts with the $r > 0$ case where $P \to 0$. The difference arises because when $r = 0$, there is no discounting: $Ke^{-rT} = K$ for all $T$. The put's maximum payoff is $K$ (when $S_T = 0$), and with infinite time, the stock—being a martingale under $\mathbb{Q}$ when $r = 0$—has a positive probability of approaching zero. In fact, geometric Brownian motion with zero drift almost surely reaches arbitrarily small values over infinite time, so the put captures nearly its full payoff value $K$.

??? success "Solution to Exercise 6"
    From the ATM approximation $C_{\text{ATM}} \approx 0.4\, S \sigma \sqrt{T}$, we solve for $\sigma$:

    $$
    \sigma_{\text{impl}} \approx \frac{C_{\text{mkt}}}{0.4\, S \sqrt{T}}
    $$

    More precisely, using $C_{\text{ATM}} \approx \frac{S\sigma\sqrt{T}}{\sqrt{2\pi}}$:

    $$
    \sigma_{\text{impl}} \approx \frac{C_{\text{mkt}}\sqrt{2\pi}}{S\sqrt{T}}
    $$

    **Application** with $S = 50$, $T = 0.25$, $C_{\text{mkt}} = 2.00$:

    $$
    \sigma_{\text{impl}} \approx \frac{2.00}{0.4 \times 50 \times \sqrt{0.25}} = \frac{2.00}{0.4 \times 50 \times 0.5} = \frac{2.00}{10} = 0.20 = 20\%
    $$

    The approximate implied volatility is $20\%$.

??? success "Solution to Exercise 7"
    **Case 1: $S > Ke^{-rT}$ (forward price above strike)**

    As $\sigma \to 0^+$: $d_1, d_2 \to +\infty$, so $C \to S - Ke^{-rT} > 0$ and $P \to 0$.

    $$
    \lim_{\sigma \to 0^+} \frac{P}{C} = \frac{0}{S - Ke^{-rT}} = 0
    $$

    **Case 2: $S < Ke^{-rT}$ (forward price below strike)**

    As $\sigma \to 0^+$: $d_1, d_2 \to -\infty$, so $C \to 0$ and $P \to Ke^{-rT} - S > 0$.

    $$
    \lim_{\sigma \to 0^+} \frac{P}{C} = \frac{Ke^{-rT} - S}{0^+} = +\infty
    $$

    **Case 3: $S = Ke^{-rT}$ (ATM forward)**

    Both $C \to 0$ and $P \to 0$, giving a $0/0$ indeterminate form. Using the ATM approximations for small $\sigma$:

    $$
    d_1 = \frac{\sigma\sqrt{T}}{2}, \quad d_2 = -\frac{\sigma\sqrt{T}}{2}
    $$

    With the Taylor expansion $\mathcal{N}(x) \approx \frac{1}{2} + \frac{x}{\sqrt{2\pi}}$ for small $x$:

    $$
    C \approx S\left(\frac{1}{2} + \frac{\sigma\sqrt{T}}{2\sqrt{2\pi}}\right) - Ke^{-rT}\left(\frac{1}{2} - \frac{\sigma\sqrt{T}}{2\sqrt{2\pi}}\right)
    $$

    Since $S = Ke^{-rT}$, denote this common value by $F$:

    $$
    C \approx F\left(\frac{1}{2} + \frac{\sigma\sqrt{T}}{2\sqrt{2\pi}}\right) - F\left(\frac{1}{2} - \frac{\sigma\sqrt{T}}{2\sqrt{2\pi}}\right) = \frac{F\sigma\sqrt{T}}{\sqrt{2\pi}}
    $$

    Similarly:

    $$
    P = C - S + Ke^{-rT} = C - F + F = C
    $$

    So $P \approx C$ when $S = Ke^{-rT}$, giving:

    $$
    \lim_{\sigma \to 0^+} \frac{P}{C} = 1
    $$

    The $S = Ke^{-rT}$ case requires careful treatment because both numerator and denominator vanish simultaneously, creating an indeterminate form. L'Hopital's rule or Taylor expansion around $\sigma = 0$ is needed. The limiting ratio of $1$ reflects the symmetry of the ATM forward position: at the forward strike, calls and puts have equal value to leading order.
