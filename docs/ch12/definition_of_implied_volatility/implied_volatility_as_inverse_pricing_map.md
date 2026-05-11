# Implied Volatility as Inverse Pricing Map


## Introduction


Implied volatility represents one of the most fundamental concepts in modern option pricing theory. Rather than viewing volatility as a model parameter, we invert the pricing relationship to extract the market's "implied" volatility from observable option prices. This perspective transforms the Black-Scholes formula from a pricing mechanism into a coordinate transformation on the space of option prices.

## The Black-Scholes Pricing Map


### 1. Forward Direction: Price as Function of Volatility


Consider the Black-Scholes pricing functional for a European call option:


$$
\mathcal{C}: \mathbb{R}_+ \to \mathbb{R}_+, \quad \sigma \mapsto C_{\text{BS}}(S, K, T, r, \sigma)
$$



where the Black-Scholes price is given explicitly by:


$$
C_{\text{BS}}(S, K, T, r, \sigma) = S \mathcal{N}(d_1) - K e^{-rT} \mathcal{N}(d_2)
$$



with


$$
\begin{align}
d_1 &= \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} \\
d_2 &= d_1 - \sigma\sqrt{T} = \frac{\ln(S/K) + (r - \sigma^2/2)T}{\sigma\sqrt{T}}
\end{align}
$$



and $\Phi(\cdot)$ denoting the standard normal cumulative distribution function.

### 2. Mathematical Properties of the Pricing Map


**Proposition 4.1.1** (Monotonicity in Volatility)  
The Black-Scholes call price $C_{\text{BS}}$ is strictly increasing in $\sigma$ for all $(S, K, T, r)$ with $S > 0$, $K > 0$, $T > 0$.

*Proof.* Computing the derivative with respect to volatility (vega):


$$
\frac{\partial C_{\text{BS}}}{\partial \sigma} = S \phi(d_1) \sqrt{T} > 0
$$



where $\phi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$ is the standard normal density. Since $\phi(d_1) > 0$ for all $d_1 \in \mathbb{R}$, we have strict positivity. □

**Proposition 4.1.2** (Range of the Pricing Map)  
For fixed $(S, K, T, r)$, the pricing map $\sigma \mapsto C_{\text{BS}}(S, K, T, r, \sigma)$ satisfies:


$$
\lim_{\sigma \to 0^+} C_{\text{BS}} = \max(S - Ke^{-rT}, 0) = C_{\text{intrinsic}}
$$




$$
\lim_{\sigma \to \infty} C_{\text{BS}} = S
$$



*Proof.* For the lower limit, as $\sigma \to 0^+$:

- If $S > Ke^{-rT}$: $d_1, d_2 \to +\infty$, so $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 1$
- If $S < Ke^{-rT}$: $d_1, d_2 \to -\infty$, so $\mathcal{N}(d_1), \mathcal{N}(d_2) \to 0$
- If $S = Ke^{-rT}$: continuous limit gives zero

For the upper limit, as $\sigma \to \infty$:

- $d_1 \to +\infty$ (dominated by $\sigma^2 T / (2\sigma\sqrt{T}) = \sigma\sqrt{T}/2$)
- $d_2 = d_1 - \sigma\sqrt{T} \to -\infty$
- Thus $\mathcal{N}(d_1) \to 1$ and $\mathcal{N}(d_2) \to 0$, giving $C_{\text{BS}} \to S$ □

### 3. Domain and Codomain Characterization


The pricing map operates between specific spaces:


$$
\mathcal{C}: (0, \infty) \to (C_{\text{intrinsic}}, S)
$$



This characterizes the **image** of the Black-Scholes formula: any observable call price must satisfy the strict bounds:


$$
\max(S - Ke^{-rT}, 0) < C_{\text{market}} < S
$$



The strict inequalities reflect the time value of optionality.

## The Inverse Map: Definition of Implied Volatility


### 1. Formal Definition


Given an observed market price $C_{\text{market}}$ satisfying the no-arbitrage bounds, the **implied volatility** $\sigma_{\text{IV}}$ is defined as the unique solution to:


$$
C_{\text{market}} = C_{\text{BS}}(S, K, T, r, \sigma_{\text{IV}})
$$



Equivalently, we define the inverse pricing map:


$$
\sigma_{\text{IV}} = \mathcal{C}^{-1}(C_{\text{market}})
$$



where $\mathcal{C}^{-1}: (C_{\text{intrinsic}}, S) \to (0, \infty)$ is the functional inverse.

### 2. Well-Posedness of the Inverse Problem


The existence and uniqueness of the inverse map follows from:

**Theorem 4.1.1** (Invertibility of Black-Scholes Pricing)  
For any market price $C_{\text{market}} \in (C_{\text{intrinsic}}, S)$, there exists a unique $\sigma_{\text{IV}} \in (0, \infty)$ such that:


$$
C_{\text{BS}}(S, K, T, r, \sigma_{\text{IV}}) = C_{\text{market}}
$$



*Proof.* This follows immediately from:

1. **Monotonicity** (Proposition 4.1.1): $\partial C_{\text{BS}}/\partial \sigma > 0$ ensures injectivity
2. **Range characterization** (Proposition 4.1.2): The image of $(0, \infty)$ under $\mathcal{C}$ is precisely $(C_{\text{intrinsic}}, S)$, ensuring surjectivity onto the admissible price domain
3. **Continuity**: $C_{\text{BS}}$ is continuous in $\sigma$, so by the Intermediate Value Theorem, the inverse exists

Uniqueness follows from strict monotonicity. □

### 3. Regularity of the Inverse Map


**Theorem 4.1.2** (Smoothness of Implied Volatility)  
The implied volatility map $\mathcal{C}^{-1}$ is $C^\infty$ smooth on its domain $(C_{\text{intrinsic}}, S)$.

*Proof.* By the Inverse Function Theorem, since:


$$
\frac{\partial C_{\text{BS}}}{\partial \sigma} = S \phi(d_1) \sqrt{T} > 0
$$



is strictly positive and smooth in $\sigma$, the inverse function is $C^\infty$ with derivative:


$$
\frac{d\sigma_{\text{IV}}}{dC} = \frac{1}{\partial C_{\text{BS}}/\partial \sigma\big|_{\sigma=\sigma_{\text{IV}}}} = \frac{1}{S \phi(d_1(\sigma_{\text{IV}})) \sqrt{T}}
$$



Higher derivatives exist by repeated application. □

## Interpretation as Change of Coordinates


### 1. From Price Space to Volatility Space


The Black-Scholes formula establishes a diffeomorphism:


$$
\Psi: (0, \infty) \to (C_{\text{intrinsic}}, S), \quad \sigma \mapsto C_{\text{BS}}(\sigma)
$$



with smooth inverse:


$$
\Psi^{-1}: (C_{\text{intrinsic}}, S) \to (0, \infty), \quad C \mapsto \sigma_{\text{IV}}
$$



This perspective reveals implied volatility as a **coordinate transformation**: rather than quoting option prices in dollars, we quote them in units of volatility.

### 2. Advantages of Volatility Coordinates


**Normalization across strikes and maturities:**  
Option prices vary wildly with $(S, K, T)$ parameters, making comparison difficult. Implied volatility provides a normalized measure that:

- Factors out the intrinsic value
- Accounts for time to maturity
- Enables comparison across different strikes

**Market convention:**  
Traders quote and trade options in terms of implied volatility, not prices. The transformation $C \leftrightarrow \sigma_{\text{IV}}$ is the fundamental market convention.

**Stability:**  
Small errors in option prices can correspond to small errors in implied volatility due to the smoothness of $\mathcal{C}^{-1}$.

## Connection to the Model-Free Perspective


### 1. Implied Volatility Without the Black-Scholes Model


While we defined $\sigma_{\text{IV}}$ using the Black-Scholes formula, it's crucial to note:

**The market need not follow a Black-Scholes model for implied volatility to be well-defined.**

Implied volatility is simply a **quoting convention**: given any price $C \in (C_{\text{intrinsic}}, S)$, we can solve for $\sigma_{\text{IV}}$ without asserting that the underlying asset follows geometric Brownian motion with constant volatility.

This leads to the empirical phenomenon of **volatility smile**: if the market truly followed Black-Scholes, all options on the same underlying with the same maturity would have identical implied volatilities. The observation that $\sigma_{\text{IV}}(K, T)$ varies with strike $K$ and maturity $T$ indicates model misspecification.

### 2. Implied Volatility as Market Observable


From this perspective:

- **Price** $C_{\text{market}}$ is the primitive observable
- **Implied volatility** $\sigma_{\text{IV}}$ is a derived coordinate
- The **volatility surface** $\sigma_{\text{IV}}(K, T)$ encodes all information in option prices through the lens of Black-Scholes

## Mathematical Formalism: Pricing Functional in General


### 1. Extension to General Payoffs


The inversion concept extends beyond vanilla calls. For any path-independent payoff $\Psi(S_T)$, under Black-Scholes we have:


$$
V_{\text{BS}}(S, T, r, \sigma) = e^{-rT} \mathbb{E}^{\mathbb{Q}}[\Psi(S_T)]
$$



where $S_T = S e^{(r - \sigma^2/2)T + \sigma W_T}$ under the risk-neutral measure $\mathbb{Q}$.

If $V_{\text{BS}}$ is strictly monotone in $\sigma$ (which requires $\Psi$ to be non-constant), we can define:


$$
\sigma_{\text{IV}}^{\Psi} = \text{solution to } V_{\text{market}} = V_{\text{BS}}(S, T, r, \sigma)
$$



### 2. Monotonicity Conditions for General Payoffs


**Proposition 4.1.3**  
The Black-Scholes price $V_{\text{BS}}$ is strictly increasing in $\sigma$ if and only if $\Psi$ is not a linear function.

*Proof sketch.* The vega is:


$$
\frac{\partial V_{\text{BS}}}{\partial \sigma} = e^{-rT} \mathbb{E}^{\mathbb{Q}}\left[\Psi(S_T) \frac{\partial \ln S_T}{\partial \sigma}\right]
$$



Using $\partial \ln S_T / \partial \sigma = -\sigma T + W_T$, this becomes a covariance term. Non-linearity of $\Psi$ ensures non-degeneracy. □

## Numerical Considerations


### 1. Root-Finding for Implied Volatility


In practice, $\sigma_{\text{IV}}$ is computed by solving:


$$
C_{\text{BS}}(\sigma) - C_{\text{market}} = 0
$$



Equivalently, we seek:

$$
\sigma_{\text{imp}} = \arg\min_\sigma \left| C_{\text{BS}}(S, K, T, r, \sigma) - C^{\text{mkt}} \right|
$$



Standard methods include:

- **Newton-Raphson:** Fast quadratic convergence using vega as the Jacobian
- **Brent's method:** Combines bisection, secant, and inverse quadratic interpolation; robust without requiring derivatives
- **Bisection:** Simple and robust but slower (linear convergence)
- **Rational approximations:** Explicit closed-form approximations for rapid initial guesses (e.g., Brenner-Subrahmanyam, Corrado-Miller)

### 2. Practical Computation Workflow


The practical procedure for computing implied volatility proceeds as follows:

**Given inputs:**

- Current underlying price $S$
- Strike price $K$
- Time to maturity $T$
- Risk-free rate $r$
- Observed market option price $C^{\text{mkt}}$

**Algorithm:**

**Step 1.** Select an initial guess $\sigma_0$ (a common choice is $\sigma_0 = 0.20$ or the previous day's IV).

**Step 2.** Compute the Black-Scholes model price $C_{\text{BS}}(S, K, T, r, \sigma_0)$.

**Step 3.** Adjust $\sigma$ iteratively until convergence:

$$
C_{\text{BS}}(S, K, T, r, \sigma_{\text{imp}}) \approx C^{\text{mkt}}
$$



The result gives the **market-implied expectation of volatility** over the remaining life of the option. This is distinct from historical or realized volatility, which is computed from past returns.

### 3. Newton-Raphson Iteration


Given current iterate $\sigma_n$:


$$
\sigma_{n+1} = \sigma_n - \frac{C_{\text{BS}}(\sigma_n) - C_{\text{market}}}{\partial C_{\text{BS}}/\partial \sigma\big|_{\sigma=\sigma_n}} = \sigma_n - \frac{C_{\text{BS}}(\sigma_n) - C_{\text{market}}}{S \phi(d_1) \sqrt{T}}
$$



**Convergence:** Quadratic convergence is guaranteed due to $C_{\text{BS}}$ being strictly convex in $\sigma$ (positive vega derivative, i.e., vomma $> 0$).

### 4. Brent's Method


Brent's method is often preferred in production systems because it:

- Does not require derivative (vega) evaluation
- Guarantees convergence within a bracketing interval $[\sigma_{\text{lo}}, \sigma_{\text{hi}}]$
- Achieves superlinear convergence in practice

The bracketing interval is typically initialized as $\sigma \in [0.001, 5.0]$, which is guaranteed to contain the solution for any admissible market price.

### 5. Implied Volatility vs. Realized Volatility


A critical distinction:

| Concept | Definition | Source |
|---------|-----------|--------|
| Implied volatility $\sigma_{\text{IV}}$ | Volatility that equates BS price to market price | Option prices (forward-looking) |
| Historical volatility $\hat{\sigma}$ | Standard deviation of past log-returns | Price history (backward-looking) |
| Realized volatility $\sigma_{\text{RV}}$ | Actual volatility over option's life | Future prices (known ex-post) |

Comparing $\sigma_{\text{IV}}$ vs. $\hat{\sigma}$ informs relative value trades: if $\sigma_{\text{IV}} > \hat{\sigma}$, options may be "expensive" (volatility risk premium).

## Summary


The implied volatility establishes a fundamental coordinate transformation:


$$
\text{Option Price Space} \xrightarrow{\mathcal{C}^{-1}} \text{Volatility Space}
$$



This transformation:

- Is **well-defined** via monotonicity and continuity of Black-Scholes pricing
- Provides a **normalized quoting convention** independent of intrinsic value
- Enables **model-free analysis** of option markets through the volatility surface
- Admits **smooth inversion** with explicit derivatives (vega-based)

The existence of the implied volatility smile—variation of $\sigma_{\text{IV}}$ with strike and maturity—reveals the limitations of the constant-volatility Black-Scholes model while simultaneously providing a powerful descriptive framework for option market dynamics.

---

## Exercises

**Exercise 1.** For a European call with $S = 100$, $K = 105$, $T = 0.5$, and $r = 3\%$, compute the admissible price interval $(C_{\text{intrinsic}}, S)$. Explain why a market price of $C_{\text{market}} = 101$ would not admit an implied volatility.

??? success "Solution to Exercise 1"
    With $S = 100$, $K = 105$, $T = 0.5$, and $r = 0.03$:

    $$
    C_{\text{intrinsic}} = \max(S - K e^{-rT}, 0) = \max(100 - 105 e^{-0.015}, 0)
    $$

    Computing $K e^{-rT} = 105 \times e^{-0.015} \approx 105 \times 0.98511 = 103.437$.

    Since $100 - 103.437 = -3.437 < 0$, the intrinsic value is zero and the admissible interval is:

    $$
    (C_{\text{intrinsic}}, S) = (0, 100)
    $$

    A market price of $C_{\text{market}} = 101$ exceeds the upper bound $S = 100$. This violates the static no-arbitrage bound because one could sell the call for $\$101$ and buy the stock for $\$100$, pocketing $\$1$ immediately. At maturity, the obligation from the short call is $\max(S_T - 105, 0)$, which is always less than or equal to $S_T$ (the value of the long stock). Since $\min(S_T, 105) \geq 0$, the net payoff at maturity is non-negative. This is a riskless arbitrage, so no implied volatility can rationalize such a price. Formally, $C_{\text{BS}}(\sigma) < S = 100$ for all finite $\sigma$, and $\lim_{\sigma \to \infty} C_{\text{BS}} = 100 < 101$, so the equation $C_{\text{BS}}(\sigma) = 101$ has no solution.

---

**Exercise 2.** Starting from the Black-Scholes formula $C_{\text{BS}} = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$, verify analytically that $\lim_{\sigma \to \infty} C_{\text{BS}} = S$ by showing $d_1 \to +\infty$ and $d_2 \to -\infty$. Which term in $d_1$ dominates as $\sigma \to \infty$?

??? success "Solution to Exercise 2"
    Starting from the Black-Scholes formula, examine $d_1$ and $d_2$ as $\sigma \to \infty$:

    $$
    d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} = \frac{\ln(S/K) + rT}{\sigma\sqrt{T}} + \frac{\sigma\sqrt{T}}{2}
    $$

    The first term $\frac{\ln(S/K) + rT}{\sigma\sqrt{T}} \to 0$ as $\sigma \to \infty$ (numerator is constant, denominator diverges). The second term $\frac{\sigma\sqrt{T}}{2} \to +\infty$. Therefore $d_1 \to +\infty$, and the **dominant term** is $\frac{\sigma\sqrt{T}}{2}$.

    For $d_2$:

    $$
    d_2 = d_1 - \sigma\sqrt{T} = \frac{\ln(S/K) + rT}{\sigma\sqrt{T}} - \frac{\sigma\sqrt{T}}{2}
    $$

    The dominant term is $-\frac{\sigma\sqrt{T}}{2} \to -\infty$, so $d_2 \to -\infty$.

    Taking the limits of the CDF values:

    $$
    \mathcal{N}(d_1) \to \Phi(+\infty) = 1, \qquad \mathcal{N}(d_2) \to \Phi(-\infty) = 0
    $$

    Substituting into Black-Scholes:

    $$
    \lim_{\sigma \to \infty} C_{\text{BS}} = S \cdot 1 - K e^{-rT} \cdot 0 = S
    $$

    Economically, at infinite volatility the probability that $S_T > K$ approaches 1 (via $\mathcal{N}(d_2) \to 0$ for the exercise probability seems contradictory, but the effect is that the expected value of $S_T$ conditional on the option being ITM grows without bound). The option becomes equivalent to holding the stock.

---

**Exercise 3.** The derivative of implied volatility with respect to price is given by

$$
\frac{d\sigma_{\text{IV}}}{dC} = \frac{1}{S\phi(d_1(\sigma_{\text{IV}}))\sqrt{T}}
$$

For an ATM option ($S = K = 100$) with $T = 1$, $r = 0$, and $\sigma_{\text{IV}} = 0.25$, compute $d_1$, evaluate $\phi(d_1)$, and find $d\sigma_{\text{IV}}/dC$. Interpret the result: how much does implied volatility change per \$1 change in the option price?

??? success "Solution to Exercise 3"
    With $S = K = 100$, $T = 1$, $r = 0$, and $\sigma_{\text{IV}} = 0.25$:

    $$
    d_1 = \frac{\ln(100/100) + (0 + 0.25^2/2) \cdot 1}{0.25 \cdot 1} = \frac{0 + 0.03125}{0.25} = 0.125
    $$

    Evaluating the standard normal density:

    $$
    \phi(d_1) = \phi(0.125) = \frac{1}{\sqrt{2\pi}} e^{-0.125^2/2} = \frac{1}{\sqrt{2\pi}} e^{-0.0078125}
    $$

    $$
    \approx 0.39894 \times 0.99221 = 0.39584
    $$

    The derivative of implied volatility with respect to price:

    $$
    \frac{d\sigma_{\text{IV}}}{dC} = \frac{1}{S \phi(d_1) \sqrt{T}} = \frac{1}{100 \times 0.39584 \times 1} = \frac{1}{39.584} \approx 0.02526
    $$

    **Interpretation:** For each $\$1$ increase in the call option price, the implied volatility increases by approximately $0.0253$, or about $2.53$ volatility points. Equivalently, vega is approximately $\$39.58$ per volatility point, meaning a 1 percentage point increase in implied volatility raises the option price by about $\$0.3958$.

---

**Exercise 4.** Explain conceptually why the Black-Scholes pricing map $\mathcal{C}: \sigma \mapsto C_{\text{BS}}(\sigma)$ is a diffeomorphism from $(0, \infty)$ to $(C_{\text{intrinsic}}, S)$. State the three properties (monotonicity, continuity, range) required for this, and identify where each is used in the proof of Theorem 4.1.1.

??? success "Solution to Exercise 4"
    The Black-Scholes pricing map $\mathcal{C}: (0, \infty) \to (C_{\text{intrinsic}}, S)$ is a diffeomorphism because it satisfies three properties:

    **1. Continuity:** $C_{\text{BS}}(\sigma)$ is a composition of smooth functions (exponentials, the normal CDF, logarithms), so it is continuous (in fact $C^\infty$) on $(0, \infty)$. This is used in the proof of Theorem 4.1.1 to invoke the **Intermediate Value Theorem**: for any target price in the image, there exists a $\sigma$ mapping to it.

    **2. Strict monotonicity:** Proposition 4.1.1 shows $\partial C_{\text{BS}}/\partial \sigma = S\phi(d_1)\sqrt{T} > 0$ for all $\sigma > 0$. This ensures **injectivity** (one-to-one): distinct volatilities produce distinct prices, so the inverse is well-defined. In the proof, this guarantees **uniqueness** of the solution.

    **3. Range characterization:** Proposition 4.1.2 establishes $\lim_{\sigma \to 0^+} C_{\text{BS}} = C_{\text{intrinsic}}$ and $\lim_{\sigma \to \infty} C_{\text{BS}} = S$. Combined with continuity and monotonicity, the image of $(0, \infty)$ is exactly $(C_{\text{intrinsic}}, S)$. This ensures **surjectivity** (onto): every admissible price has a preimage. In the proof, this guarantees **existence** of the solution.

    Together, these properties establish that $\mathcal{C}$ is a smooth bijection with smooth inverse (since vega is everywhere nonzero, the Inverse Function Theorem gives smoothness of $\mathcal{C}^{-1}$), making it a diffeomorphism.

---

**Exercise 5.** A trader observes two call options on the same stock with the same maturity $T = 0.25$ but different strikes: $K_1 = 95$ with $C_1 = 9.50$ and $K_2 = 105$ with $C_2 = 3.20$. Both options have $S = 100$ and $r = 2\%$. (a) Verify that both prices lie in their respective admissible intervals. (b) Which option do you expect to have higher implied volatility if the smile has negative skew? Explain without computing.

??? success "Solution to Exercise 5"
    **(a)** Check that both prices lie in their admissible intervals.

    For $K_1 = 95$: $C_{\text{intrinsic}} = \max(100 - 95 e^{-0.005}, 0) = \max(100 - 94.526, 0) = 5.474$ and $S = 100$. Since $5.474 < 9.50 < 100$, the price is admissible.

    For $K_2 = 105$: $C_{\text{intrinsic}} = \max(100 - 105 e^{-0.005}, 0) = \max(100 - 104.476, 0) = 0$ and $S = 100$. Since $0 < 3.20 < 100$, the price is admissible.

    Both implied volatilities exist.

    **(b)** With negative skew (also called the volatility skew), implied volatility decreases as strike increases. This is the typical pattern observed in equity markets, where lower-strike (OTM put) options command higher implied volatilities than higher-strike (OTM call) options.

    Under negative skew, the $K_1 = 95$ option (lower strike, ITM call / OTM put equivalent) would have **higher implied volatility** than the $K_2 = 105$ option (higher strike, OTM call).

    Intuitively, the negative skew reflects the market pricing in a higher probability of large downward moves relative to the log-normal model. The lower-strike option is more sensitive to this left-tail risk, so the market "charges" a higher implied volatility to compensate. This is consistent with the empirical observation that equity returns exhibit negative skewness and excess kurtosis, features not captured by the symmetric log-normal distribution.

---

**Exercise 6.** Compare and contrast three numerical methods for computing implied volatility: Newton-Raphson, Brent's method, and bisection. For each method, state (a) the convergence rate, (b) whether it requires vega evaluation, and (c) under what conditions it might fail or be preferred. Why is Brent's method often used in production systems?

??? success "Solution to Exercise 6"
    **Newton-Raphson:**

    (a) Convergence rate: **Quadratic** — the number of correct digits roughly doubles per iteration.
    (b) Requires vega: **Yes** — the iteration formula is $\sigma_{n+1} = \sigma_n - (C_{\text{BS}}(\sigma_n) - C_{\text{market}}) / \mathcal{V}(\sigma_n)$.
    (c) Can fail if the initial guess is poor (vega near zero for deep OTM/ITM options near expiry), causing large overshoots or division by near-zero. Preferred when a good initial guess is available and speed is critical.

    **Brent's method:**

    (a) Convergence rate: **Superlinear** (between linear and quadratic in practice), combining inverse quadratic interpolation with bisection fallback.
    (b) Requires vega: **No** — it is a derivative-free method using only function evaluations.
    (c) Requires a valid bracketing interval $[\sigma_{\text{lo}}, \sigma_{\text{hi}}]$ where the function changes sign. Essentially never fails given a proper bracket. Preferred in **production systems** because it is robust, guaranteed to converge, and avoids the cost and potential numerical issues of computing vega. It handles edge cases (deep OTM, near-expiry) gracefully without special-case logic.

    **Bisection:**

    (a) Convergence rate: **Linear** — gains approximately one binary digit per iteration (halves the interval each step).
    (b) Requires vega: **No** — only function evaluations needed.
    (c) Never fails given a valid bracket, but converges slowly (about 50 iterations for machine precision from a typical starting bracket). Preferred only as a fallback or for verification, not for high-throughput computation.

    Brent's method is often used in production because it combines the robustness guarantee of bisection (always converges within the bracket) with the speed of interpolation methods, all without requiring derivative computation.

---

**Exercise 7.** If the underlying truly followed geometric Brownian motion with constant volatility $\sigma = 0.20$, what would the implied volatility surface $\sigma_{\text{IV}}(K, T)$ look like? In practice, $\sigma_{\text{IV}}$ varies with $K$ and $T$. List three market phenomena that cause deviations from the flat surface, and for each, describe qualitatively how it affects the shape of $\sigma_{\text{IV}}(K)$ at a fixed maturity.

??? success "Solution to Exercise 7"
    If the underlying truly followed GBM with constant volatility $\sigma = 0.20$, then for every strike $K$ and maturity $T$, the Black-Scholes price with $\sigma = 0.20$ would exactly match the market price. Inverting would recover $\sigma_{\text{IV}}(K, T) = 0.20$ everywhere. The implied volatility surface would be **perfectly flat** at $0.20$ across all strikes and maturities.

    Three market phenomena causing deviations from the flat surface:

    **1. Leverage effect and crash risk (causes negative skew):** Equity markets exhibit an asymmetric response to large moves: crashes are more sudden and severe than rallies. Investors demand higher premiums for downside protection (OTM puts), inflating implied volatility at low strikes relative to high strikes. At fixed maturity, $\sigma_{\text{IV}}(K)$ is **decreasing** in $K$, producing the characteristic downward-sloping "skew" seen in equity index options.

    **2. Fat tails / excess kurtosis (causes the smile):** Real asset returns have heavier tails than the normal distribution assumed by Black-Scholes. Both deep ITM and deep OTM options are more likely to finish in-the-money than the log-normal model predicts. This raises implied volatilities at both extreme strikes relative to ATM, producing a **U-shaped "smile"** in $\sigma_{\text{IV}}(K)$. This is especially prominent in currency options and short-dated equity options.

    **3. Stochastic volatility and mean reversion (causes term structure):** Realized volatility is not constant but varies over time, with periods of high and low volatility. Stochastic volatility models (e.g., Heston) predict that the smile flattens as maturity increases due to the mean-reversion of variance. At fixed maturity, the effect on $\sigma_{\text{IV}}(K)$ is to produce a **more pronounced smile for short maturities** (high curvature) that gradually flattens for longer maturities. The vol-of-vol parameter controls the overall curvature, while the correlation between the asset and its volatility process controls the skew direction.
