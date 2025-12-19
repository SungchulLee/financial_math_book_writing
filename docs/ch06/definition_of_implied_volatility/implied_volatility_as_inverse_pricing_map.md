# Implied Volatility as Inverse Pricing Map

## Introduction

Implied volatility represents one of the most fundamental concepts in modern option pricing theory. Rather than viewing volatility as a model parameter, we invert the pricing relationship to extract the market's "implied" volatility from observable option prices. This perspective transforms the Black-Scholes formula from a pricing mechanism into a coordinate transformation on the space of option prices.

## The Black-Scholes Pricing Map

### Forward Direction: Price as Function of Volatility

Consider the Black-Scholes pricing functional for a European call option:


$$
\mathcal{C}: \mathbb{R}_+ \to \mathbb{R}_+, \quad \sigma \mapsto C_{\text{BS}}(S, K, T, r, \sigma)
$$



where the Black-Scholes price is given explicitly by:


$$
C_{\text{BS}}(S, K, T, r, \sigma) = S \Phi(d_1) - K e^{-rT} \Phi(d_2)
$$



with


$$
\begin{align}
d_1 &= \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} \\
d_2 &= d_1 - \sigma\sqrt{T} = \frac{\ln(S/K) + (r - \sigma^2/2)T}{\sigma\sqrt{T}}
\end{align}
$$



and $\Phi(\cdot)$ denoting the standard normal cumulative distribution function.

### Mathematical Properties of the Pricing Map

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
- If $S > Ke^{-rT}$: $d_1, d_2 \to +\infty$, so $\Phi(d_1), \Phi(d_2) \to 1$
- If $S < Ke^{-rT}$: $d_1, d_2 \to -\infty$, so $\Phi(d_1), \Phi(d_2) \to 0$
- If $S = Ke^{-rT}$: continuous limit gives zero

For the upper limit, as $\sigma \to \infty$:
- $d_1 \to +\infty$ (dominated by $\sigma^2 T / (2\sigma\sqrt{T}) = \sigma\sqrt{T}/2$)
- $d_2 = d_1 - \sigma\sqrt{T} \to -\infty$
- Thus $\Phi(d_1) \to 1$ and $\Phi(d_2) \to 0$, giving $C_{\text{BS}} \to S$ □

### Domain and Codomain Characterization

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

### Formal Definition

Given an observed market price $C_{\text{market}}$ satisfying the no-arbitrage bounds, the **implied volatility** $\sigma_{\text{IV}}$ is defined as the unique solution to:


$$
C_{\text{market}} = C_{\text{BS}}(S, K, T, r, \sigma_{\text{IV}})
$$



Equivalently, we define the inverse pricing map:


$$
\sigma_{\text{IV}} = \mathcal{C}^{-1}(C_{\text{market}})
$$



where $\mathcal{C}^{-1}: (C_{\text{intrinsic}}, S) \to (0, \infty)$ is the functional inverse.

### Well-Posedness of the Inverse Problem

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

### Regularity of the Inverse Map

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

### From Price Space to Volatility Space

The Black-Scholes formula establishes a diffeomorphism:


$$
\Psi: (0, \infty) \to (C_{\text{intrinsic}}, S), \quad \sigma \mapsto C_{\text{BS}}(\sigma)
$$



with smooth inverse:


$$
\Psi^{-1}: (C_{\text{intrinsic}}, S) \to (0, \infty), \quad C \mapsto \sigma_{\text{IV}}
$$



This perspective reveals implied volatility as a **coordinate transformation**: rather than quoting option prices in dollars, we quote them in units of volatility.

### Advantages of Volatility Coordinates

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

### Implied Volatility Without the Black-Scholes Model

While we defined $\sigma_{\text{IV}}$ using the Black-Scholes formula, it's crucial to note:

**The market need not follow a Black-Scholes model for implied volatility to be well-defined.**

Implied volatility is simply a **quoting convention**: given any price $C \in (C_{\text{intrinsic}}, S)$, we can solve for $\sigma_{\text{IV}}$ without asserting that the underlying asset follows geometric Brownian motion with constant volatility.

This leads to the empirical phenomenon of **volatility smile**: if the market truly followed Black-Scholes, all options on the same underlying with the same maturity would have identical implied volatilities. The observation that $\sigma_{\text{IV}}(K, T)$ varies with strike $K$ and maturity $T$ indicates model misspecification.

### Implied Volatility as Market Observable

From this perspective:
- **Price** $C_{\text{market}}$ is the primitive observable
- **Implied volatility** $\sigma_{\text{IV}}$ is a derived coordinate
- The **volatility surface** $\sigma_{\text{IV}}(K, T)$ encodes all information in option prices through the lens of Black-Scholes

## Mathematical Formalism: Pricing Functional in General

### Extension to General Payoffs

The inversion concept extends beyond vanilla calls. For any path-independent payoff $\Psi(S_T)$, under Black-Scholes we have:


$$
V_{\text{BS}}(S, T, r, \sigma) = e^{-rT} \mathbb{E}^{\mathbb{Q}}[\Psi(S_T)]
$$



where $S_T = S e^{(r - \sigma^2/2)T + \sigma W_T}$ under the risk-neutral measure $\mathbb{Q}$.

If $V_{\text{BS}}$ is strictly monotone in $\sigma$ (which requires $\Psi$ to be non-constant), we can define:


$$
\sigma_{\text{IV}}^{\Psi} = \text{solution to } V_{\text{market}} = V_{\text{BS}}(S, T, r, \sigma)
$$



### Monotonicity Conditions for General Payoffs

**Proposition 4.1.3**  
The Black-Scholes price $V_{\text{BS}}$ is strictly increasing in $\sigma$ if and only if $\Psi$ is not a linear function.

*Proof sketch.* The vega is:


$$
\frac{\partial V_{\text{BS}}}{\partial \sigma} = e^{-rT} \mathbb{E}^{\mathbb{Q}}\left[\Psi(S_T) \frac{\partial \ln S_T}{\partial \sigma}\right]
$$



Using $\partial \ln S_T / \partial \sigma = -\sigma T + W_T$, this becomes a covariance term. Non-linearity of $\Psi$ ensures non-degeneracy. □

## Numerical Considerations

### Root-Finding for Implied Volatility

In practice, $\sigma_{\text{IV}}$ is computed by solving:


$$
C_{\text{BS}}(\sigma) - C_{\text{market}} = 0
$$



Standard methods include:
- **Newton-Raphson:** Fast convergence using vega as derivative
- **Bisection:** Robust but slower
- **Rational approximations:** Explicit formulas for rapid computation

### Newton-Raphson Iteration

Given current iterate $\sigma_n$:


$$
\sigma_{n+1} = \sigma_n - \frac{C_{\text{BS}}(\sigma_n) - C_{\text{market}}}{\partial C_{\text{BS}}/\partial \sigma\big|_{\sigma=\sigma_n}} = \sigma_n - \frac{C_{\text{BS}}(\sigma_n) - C_{\text{market}}}{S \phi(d_1) \sqrt{T}}
$$



**Convergence:** Quadratic convergence is guaranteed due to $C_{\text{BS}}$ being strictly convex in $\sigma$ (positive vega derivative, i.e., vomma $> 0$).

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
