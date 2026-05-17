# Asymptotic Behavior of the Black-Scholes Formula

The Black-Scholes formula exhibits well-defined **limiting behavior** as parameters approach extreme values. These limits give intuition for option behavior across market regimes and serve as sanity checks for numerical implementations.

!!! info "Where this fits"
    - **Roadmap row(s):** All six perspectives examined through limits in $S, K, T, \sigma, r$.
    - **Builds on:** [The Black-Scholes formula](bs_formula_statement.md) (the component analysis of $d_1, d_2$) and [Properties and bounds](properties_and_bounds.md) (monotonicity establishes the signs of the limits).
    - **Feeds into:** [Computational examples](computational_examples.md) (numerical-stability fixes near $T \to 0$ and extreme $d_1, d_2$).

!!! note "Unifying Principle"
    Every limit in this section reduces to the same mechanism: determining the sign and rate at which $d_1$ and $d_2$ diverge to $\pm\infty$. Since $C = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$ and the Gaussian CDF satisfies $\mathcal{N}(x) \to 1$ as $x \to +\infty$ and $\mathcal{N}(x) \to 0$ as $x \to -\infty$, all asymptotics follow from the **tail behavior of the standard normal distribution**.

---

## Limits in Stock Price

*Section goal: what happens to call and put prices as the spot drifts to $0$ and to $\infty$.*

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

**Put price** (via put-call parity): $P = C - S + Ke^{-rT} \to 0$ — the deep OTM put is worthless.

---

### 2. **As S → 0 (Deep Out-of-the-Money Call)**


Now $d_1, d_2 \to -\infty$, so $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 0$ and $C \to 0$. For the put, $\mathcal{N}(-d_2) \to 1$ gives $P \to Ke^{-rT}$: the deep ITM put approaches the present value of the strike.

---

## Limits in Time to Maturity

*Section goal: option value at the expiry boundary ($T \to 0$) and in the long-dated limit ($T \to \infty$).*

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

Both $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$ tend to $\tfrac{1}{2}$, and $S\,\mathcal{N}(d_1) - Ke^{-rT}\,\mathcal{N}(d_2)$ becomes a $\tfrac{K}{2} - \tfrac{K}{2}$ near-cancellation. To see the limit cleanly, substitute the Taylor expansion $\mathcal{N}(\epsilon) = \tfrac{1}{2} + \frac{\epsilon}{\sqrt{2\pi}} + O(\epsilon^3)$ with $\epsilon_i = d_i$. With $S = K$:

$$
d_1 = \frac{(r + \tfrac{1}{2}\sigma^2)\sqrt{T}}{\sigma}, \qquad d_2 = \frac{(r - \tfrac{1}{2}\sigma^2)\sqrt{T}}{\sigma}, \qquad d_1 - d_2 = \sigma\sqrt{T}
$$

The call price becomes

$$
C = K\!\left[\mathcal{N}(d_1) - e^{-rT}\mathcal{N}(d_2)\right] = K\!\left[\tfrac{1}{2}(1 - e^{-rT}) + \tfrac{1}{\sqrt{2\pi}}\!\left(d_1 - e^{-rT}d_2\right) + O(T^{3/2})\right]
$$

Each bracketed term is $O(T^{1/2})$ as $T \to 0$ — the first via $1 - e^{-rT} = rT + O(T^2)$, the second via $d_i = O(\sqrt{T})$ — so

$$
C = O(\sqrt{T}) \;\to\; 0 \;=\; (S - K)^+
$$

The leading $K\sigma\sqrt{T}/\sqrt{2\pi}$ term is exactly the ATM approximation derived later in this section.

**Summary**: As expiration approaches:

$$
\boxed{\lim_{T \to 0} C(S,T) = \max(S - K, 0) = (S-K)^+}
$$

This recovers the **terminal payoff condition**.

---

### 2. **As T → ∞ (Very Long Maturity, r > 0)**


**Assumption**: $r > 0$ throughout this subsection. The case $r = 0$ is qualitatively different (see Exercise 5).

Decompose

$$
d_1 = \frac{\ln(S/K)}{\sigma\sqrt{T}} + \frac{(r + \tfrac{1}{2}\sigma^2)\sqrt{T}}{\sigma}, \qquad d_2 = d_1 - \sigma\sqrt{T}
$$

The first term decays as $T^{-1/2}$, the second grows as $T^{1/2}$ with positive coefficient (since $r + \tfrac{1}{2}\sigma^2 > 0$); the second term dominates strictly. So $d_1, d_2 \to +\infty$ at rate $\sqrt{T}$, and $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 1$.

**Call price**: Both terms in $C = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$ converge: $S\mathcal{N}(d_1) \to S$ and the strike term *vanishes by exponential decay* — $Ke^{-rT} \to 0$ exponentially while $\mathcal{N}(d_2)$ is bounded. Therefore

$$
C \to S
$$

The discounted strike's exponential decay always dominates any sub-exponential factor in $\mathcal{N}(d_2)$, which is why this limit is unconditional in $\sigma$ (given $r > 0$).

**Put price**: $P = C - S + Ke^{-rT} \to S - S + 0 = 0$.

---

## Limits in Volatility

*Section goal: behaviour as $\sigma \to 0$ (deterministic stock) and $\sigma \to \infty$ (extreme uncertainty).*

### 1. **As σ → 0 (Zero Volatility)**


**Deterministic evolution**: Stock grows at risk-free rate:

$$
S_T = S_0 e^{rT}
$$

**Case 1: $S_0 > Ke^{-rT}$** (Forward price above strike)

As $\sigma \to 0$, $d_1, d_2 \to +\infty$ so $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 1$. The stock finishes above $K$ with probability approaching $1$:

$$
C \to S_0 - Ke^{-rT}
$$

**Case 2: $S_0 < Ke^{-rT}$** (Forward price below strike)

Now $d_1, d_2 \to -\infty$, so $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 0$ and

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


**Behavior of $d_1$ and $d_2$**: Decompose

$$
d_1 = \frac{\ln(S/K) + rT}{\sigma\sqrt{T}} + \frac{\sigma\sqrt{T}}{2}, \qquad d_2 = \frac{\ln(S/K) + rT}{\sigma\sqrt{T}} - \frac{\sigma\sqrt{T}}{2}
$$

The first piece decays as $\sigma^{-1}$, the $\pm\sigma\sqrt{T}/2$ pieces grow linearly in $\sigma$. So linear growth dominates inverse decay, with opposite signs:

$$
d_1 = +\frac{\sigma\sqrt{T}}{2} + O(\sigma^{-1}) \to +\infty, \qquad d_2 = -\frac{\sigma\sqrt{T}}{2} + O(\sigma^{-1}) \to -\infty
$$

Therefore $\mathcal{N}(d_1) \to 1$ and $\mathcal{N}(d_2) \to 0$. (The "indeterminate $\infty - \infty$" form for $d_2 = d_1 - \sigma\sqrt{T}$ resolves as soon as one writes both $d_1$ and $d_2$ in terms of the same dominant scale $\sigma\sqrt{T}$ — they have opposite limits, not a cancellation.)

**Call price**:

$$
C \to S \cdot 1 - Ke^{-rT} \cdot 0 = S
$$

**Interpretation**: $\mathcal{N}(d_1) \to 1$ and $\mathcal{N}(d_2) \to 0$, so as in the deep-ITM case the call approaches the full stock price.

**Put price**: Put-call parity gives $P = C - S + Ke^{-rT} \to Ke^{-rT}$.

**Summary**:

$$
\boxed{\lim_{\sigma \to \infty} C = S, \qquad \lim_{\sigma \to \infty} P = Ke^{-rT}}
$$

---

## Limits in Interest Rate

*Section goal: how prices respond as $r \to 0$ and as $r \to \infty$.*

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


As $r \to \infty$, $d_1, d_2 \to +\infty$ (driven by the $r\sqrt{T}/\sigma$ term) and $e^{-rT} \to 0$. The discounted strike vanishes (cf. $T \to \infty$), giving $C \to S$ and $P \to 0$.

---

## Limits in Strike Price

*Section goal: limits as $K \to 0$ (call $\to S$) and $K \to \infty$ (call $\to 0$).*

### 1. **As K → 0 (Zero Strike)**


As $K \to 0$, $d_1, d_2 \to +\infty$, so $C \to S$ and $P \to 0$ — a zero-strike call is equivalent to owning the stock.

### 2. **As K → ∞ (Infinite Strike)**


As $K \to \infty$, $d_1, d_2 \to -\infty$, so $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 0$ and $C \to 0$ (no chance of exceeding the strike). The put price obeys $P = Ke^{-rT}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)$ with $\mathcal{N}(-d_1), \mathcal{N}(-d_2) \to 1$, so $P \sim Ke^{-rT} - S \to +\infty$. The general upper bound $P \leq Ke^{-rT}$ remains valid — both sides diverge at the same rate, so $P/(Ke^{-rT}) \to 1$, i.e., the put approaches its theoretical maximum value relative to the discounted strike.

---

## ATM Approximation for Small Time

*Section goal: the clean short-time expansion $C_{\text{ATM}} \approx 0.4\, S\sigma\sqrt{T}$ and its derivation.*

For at-the-money options ($S \approx K$) with small $T$, a useful closed-form approximation emerges.

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
| $T \to \infty$ ($r > 0$) | $C \to S$ | $P \to 0$ |
| $\sigma \to 0$ | $C \to (S-Ke^{-rT})^+$ | $P \to (Ke^{-rT}-S)^+$ |
| $\sigma \to \infty$ | $C \to S$ | $P \to Ke^{-rT}$ |
| $r \to 0$ | Reduces to $C = S\mathcal{N}(d_1) - K\mathcal{N}(d_2)$ | Put-call parity: $C - P = S - K$ |
| $r \to \infty$ | $C \to S$ | $P \to 0$ |
| $K \to 0$ | $C \to S$ | $P \to 0$ |
| $K \to \infty$ | $C \to 0$ | $P \to Ke^{-rT}$ |

---

## Practical Implications

Recall (see [§ Properties and Bounds](properties_and_bounds.md) and [§ Common Numerical Issues](computational_examples.md#common-numerical-issues)): the bounds $0 \leq C \leq S$, $0 \leq P \leq Ke^{-rT}$ provide sanity checks, and the limiting formulas above motivate the special-case branches used near $T \approx 0$, $\sigma \to 0$, or $|d_i|$ large in production implementations. For the Greek-level limits ($\Delta \to 1$ deep ITM, $\Gamma \to \infty$ as $T \to 0$ near the strike — pin risk — and $\nu \to 0$ as $\sigma \to 0$), see [§ Greeks in Black-Scholes](../../ch10/greeks/greeks_in_black_scholes_model.md). Real-market violations of these asymptotics signal model misspecification, transaction-cost frictions, or American features.

---

## Summary

The five regimes — deep ITM (forward-like), near expiration (intrinsic), long maturity (call $\to S$), zero/infinite $\sigma$ — are summarised in the table above and serve as bounds, sanity checks, and stability triggers in implementations.

---

## Exercises

**Exercise 1.** Let $C(S, K, T, r, \sigma)$ denote the Black-Scholes call price. Prove rigorously that

$$
\lim_{S \to \infty} \frac{C(S, K, T, r, \sigma)}{S} = 1
$$

by analyzing the rate at which $\mathcal{N}(d_1) \to 1$ as $S \to \infty$. What does this tell you about the delta of a deep in-the-money call?

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

---
**Exercise 2.** For an at-the-money call ($S = K$) with $r = 0$, use the Taylor expansion of $\mathcal{N}(x)$ around $x = 0$ to show that the call price satisfies

$$
C \approx \frac{S \sigma \sqrt{T}}{\sqrt{2\pi}}
$$

for small $T$. Compute the percentage error of this approximation relative to the exact Black-Scholes price when $S = K = 100$, $\sigma = 0.25$, $r = 0$, and $T = 0.01$.

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

---
**Exercise 3.** Consider the put price $P$ as $\sigma \to \infty$. Show from the Black-Scholes formula (not from put-call parity) that $P \to Ke^{-rT}$. Explain the financial intuition: why should the put attain its maximum theoretical value when volatility is infinite?

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

---
**Exercise 4.** Examine the behavior of the Black-Scholes call price as $r \to -\infty$ (negative interest rates). Determine $\lim_{r \to -\infty} d_1$, $\lim_{r \to -\infty} d_2$, and $\lim_{r \to -\infty} C$. Is the result consistent with the economic interpretation of a very negative interest rate?

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

    The second term $Ke^{-rT}\mathcal{N}(d_2)$ is the contest of interest: $e^{-rT} \to +\infty$ as $r \to -\infty$, but $\mathcal{N}(d_2) \to 0$. To resolve it, set $\rho = -r > 0$ so $\rho \to +\infty$. To leading order $d_2 \approx -\rho\sqrt{T}/\sigma$. Apply Mills' ratio: for $x \to -\infty$,

    $$
    \mathcal{N}(x) \sim \frac{\phi(x)}{|x|} = \frac{1}{|x|\sqrt{2\pi}}\,\exp\!\left(-\frac{x^2}{2}\right)
    $$

    so the second term has the form (constant)$\cdot \rho^{-1}\cdot \exp\!\left(\rho T - \rho^2 T/(2\sigma^2)\right)$ up to a polynomial-in-$\rho$ prefactor. The exponent

    $$
    \rho T - \frac{\rho^2 T}{2\sigma^2} = -\frac{T}{2\sigma^2}\bigl(\rho - \sigma^2\bigr)^2 + \frac{\sigma^2 T}{2}
    $$

    is a downward parabola in $\rho$: it goes to $-\infty$ as $\rho \to \infty$. So the *quadratic* Gaussian decay strictly beats the *linear* exponential growth, and $Ke^{-rT}\mathcal{N}(d_2) \to 0$.

    Therefore:

    $$
    \lim_{r \to -\infty} C = 0
    $$

    **Economic interpretation**: A very negative interest rate means cash is extremely expensive to hold, and the present value of the strike $Ke^{-rT} \to +\infty$. The forward price $Se^{rT} \to 0$, meaning the stock is expected to lose nearly all its value under the risk-neutral measure. The option to buy the stock at any positive strike is worthless because the stock itself becomes worthless in forward terms. This is consistent: no rational agent would pay for the right to buy an asset whose risk-neutral expected value vanishes.

---
**Exercise 5.** The summary table states that as $T \to \infty$, the put price satisfies $P \to 0$. However, this assumes $r > 0$. What happens to $\lim_{T \to \infty} P$ when $r = 0$? Prove your answer by carefully analyzing $d_1$ and $d_2$ in this special case.

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

---
**Exercise 6.** Using the ATM approximation $C_{\text{ATM}} \approx 0.4 \, S \sigma \sqrt{T}$, derive an approximate formula for the ATM implied volatility $\sigma_{\text{impl}}$ given a market price $C_{\text{mkt}}$ of an at-the-money call. Apply your formula to find the approximate implied volatility when $S = 50$, $T = 0.25$, and $C_{\text{mkt}} = 2.00$.

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

---
**Exercise 7.** Consider the ratio of a European put to a European call, $P/C$, for a fixed strike $K$ and maturity $T$. Determine

$$
\lim_{\sigma \to 0^+} \frac{P(S, K, T, r, \sigma)}{C(S, K, T, r, \sigma)}
$$

for the three cases $S > Ke^{-rT}$, $S < Ke^{-rT}$, and $S = Ke^{-rT}$. Discuss why the $S = Ke^{-rT}$ case requires careful treatment.

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
