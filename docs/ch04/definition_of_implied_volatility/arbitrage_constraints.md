# Arbitrage Constraints on Implied Volatility

## Introduction

The existence of implied volatility requires that market prices satisfy fundamental no-arbitrage bounds. These constraints arise from static replication arguments and ensure that the pricing map $\sigma \mapsto C_{\text{BS}}(\sigma)$ has the correct domain and range for inversion. Beyond simple bounds, arbitrage-free conditions impose structural requirements on the implied volatility surface across strikes and maturities.

## Static No-Arbitrage Bounds

### Point-Wise Bounds for Call Options

For a European call option with spot $S$, strike $K$, maturity $T$, risk-free rate $r$, and dividend yield $q$:

**Theorem 4.3.1** (Fundamental Call Price Bounds)  
Any arbitrage-free call price $C$ must satisfy:


$$
\max(S e^{-qT} - K e^{-rT}, 0) \leq C \leq S e^{-qT}
$$



with strict inequalities for implied volatility to exist:


$$
\max(S e^{-qT} - K e^{-rT}, 0) < C < S e^{-qT}
$$



*Proof of lower bound.* Construct the portfolio:
- Long 1 call option
- Short $e^{-qT}$ units of stock (to account for dividends)
- Long $K e^{-rT}$ units of cash bond

At maturity $T$:
- Stock position: $-S_T e^{-qT} \cdot e^{qT} = -S_T$
- Bond position: $K e^{-rT} \cdot e^{rT} = K$
- Call payoff: $\max(S_T - K, 0)$

Total value:
- If $S_T > K$: $(S_T - K) - S_T + K = 0$
- If $S_T \leq K$: $0 - S_T + K = K - S_T \geq 0$

At time 0, portfolio value:


$$
C - S e^{-qT} + K e^{-rT}
$$



If $C < S e^{-qT} - K e^{-rT}$, portfolio has negative initial cost and non-negative terminal value—arbitrage. □

*Proof of upper bound.* Consider the strategy:
- Short 1 call option
- Long $e^{-qT}$ units of stock

At maturity:
- Stock value: $S_T$
- Call obligation: $-\max(S_T - K, 0)$

Net payoff: $S_T - \max(S_T - K, 0) = \min(S_T, K) \geq 0$

If $C > S e^{-qT}$, initial wealth is $C - S e^{-qT} > 0$ with non-negative terminal payoff—arbitrage. □

### Implications for Implied Volatility Domain

**Corollary 4.3.1** (Admissible Price Domain)  
The domain of the implied volatility inverse map is:


$$
\mathcal{D}_C = (C_{\text{intrinsic}}, S e^{-qT})
$$



where $C_{\text{intrinsic}} = \max(S e^{-qT} - K e^{-rT}, 0)$.

Any price outside this interval either:
1. Admits arbitrage (economically infeasible)
2. Corresponds to $\sigma_{\text{IV}} \in \{0, \infty\}$ (boundary cases)

### Put Option Bounds

For European puts, by symmetry and put-call parity:


$$
\max(K e^{-rT} - S e^{-qT}, 0) < P < K e^{-rT}
$$



Since:


$$
C - P = S e^{-qT} - K e^{-rT}
$$



the implied volatilities satisfy:


$$
\sigma_{\text{IV}}^{\text{call}}(K, T) = \sigma_{\text{IV}}^{\text{put}}(K, T)
$$



## Monotonicity Constraints Across Strikes

### Call Prices Decreasing in Strike

**Theorem 4.3.2** (Monotonicity in Strike)  
For fixed maturity $T$, the call price function $C(K)$ is non-increasing in strike $K$:


$$
K_1 < K_2 \implies C(K_1) \geq C(K_2)
$$



*Proof.* Consider the payoffs at maturity:


$$
\max(S_T - K_1, 0) \geq \max(S_T - K_2, 0) \quad \text{for all } S_T
$$



By the risk-neutral pricing formula:


$$
C(K_1) = e^{-rT} \mathbb{E}^{\mathbb{Q}}[\max(S_T - K_1, 0)] \geq e^{-rT} \mathbb{E}^{\mathbb{Q}}[\max(S_T - K_2, 0)] = C(K_2)
$$



If $C(K_1) < C(K_2)$, buy call at $K_1$, sell call at $K_2$—guaranteed non-negative payoff with negative initial cost. □

### Implications for Implied Volatility

**Proposition 4.3.1**  
Monotonicity of call prices in strike does **not** imply monotonicity of implied volatility in strike.

The volatility smile/skew empirically exhibits:
- $\sigma_{\text{IV}}(K)$ often decreasing for $K < K_{\text{ATM}}$ (skew)
- $\sigma_{\text{IV}}(K)$ often increasing for $K > K_{\text{ATM}}$ (smile)

This is consistent with arbitrage-free pricing because the transformation $C \leftrightarrow \sigma_{\text{IV}}$ is non-linear.

### Convexity: Butterfly Spread Constraint

**Theorem 4.3.3** (Convexity in Strike)  
The call price function $C(K)$ is convex in $K$:


$$
C(K_2) \leq \lambda C(K_1) + (1 - \lambda) C(K_3)
$$



for any $K_1 < K_2 < K_3$ with $\lambda = \frac{K_3 - K_2}{K_3 - K_1}$.

*Proof.* Consider the butterfly spread:
- Long 1 call at $K_1$
- Short $\frac{K_3 - K_1}{K_2 - K_1}$ calls at $K_2$
- Long $\frac{K_2 - K_1}{K_3 - K_1}$ calls at $K_3$

For equally spaced strikes ($K_2 - K_1 = K_3 - K_2 = \Delta K$), the payoff is:


$$
\Psi(S_T) = \begin{cases}
0 & S_T \leq K_1 \\
S_T - K_1 & K_1 < S_T \leq K_2 \\
K_3 - S_T & K_2 < S_T \leq K_3 \\
0 & S_T > K_3
\end{cases}
$$



This is a non-negative piecewise linear function (tent function). Therefore, the initial cost must be non-negative:


$$
C(K_1) - 2C(K_2) + C(K_3) \geq 0
$$



Rearranging:


$$
C(K_2) \leq \frac{C(K_1) + C(K_3)}{2}
$$



for equally spaced strikes, which extends to general convexity via density of dyadic rationals. □

**Corollary 4.3.2** (Second Derivative Bound)  
The second derivative (in the distributional sense):


$$
\frac{\partial^2 C}{\partial K^2} \geq 0
$$



This is the **Breeden-Litzenberger** density constraint: the second derivative of call price with respect to strike equals the discounted risk-neutral density, which must be non-negative.

### Implications for Implied Volatility Surface

Convexity of $C(K)$ imposes constraints on $\sigma_{\text{IV}}(K)$. Define the **total variance**:


$$
w(K, T) = \sigma_{\text{IV}}^2(K, T) \cdot T
$$



**Theorem 4.3.4** (Gatheral's Constraint)  
For the surface to be arbitrage-free:


$$
\left(1 - \frac{y}{w} \frac{\partial w}{\partial y}\right)^2 - \frac{1}{4} \left(\frac{1}{w} + \frac{1}{4}\right) \left(\frac{\partial w}{\partial y}\right)^2 + \frac{1}{2} \frac{\partial^2 w}{\partial y^2} \geq 0
$$



where $y = \ln(K/F)$ is log-moneyness ($F$ is the forward price).

*This constraint is equivalent to convexity of call prices in strike.*

## Calendar Spread Constraints

### Monotonicity in Maturity

**Theorem 4.3.5** (Call Prices Increasing in Maturity)  
For fixed strike $K$, the call price function $C(T)$ is non-decreasing in maturity $T$ (assuming zero dividends):


$$
T_1 < T_2 \implies C(T_1) \leq C(T_2)
$$



*Proof.* The American call option on a non-dividend-paying stock is never optimally exercised early. Therefore:


$$
C(T_2) = \sup_{\tau \leq T_2} \mathbb{E}[\text{Payoff at } \tau] \geq \sup_{\tau \leq T_1} \mathbb{E}[\text{Payoff at } \tau] = C(T_1)
$$



Alternatively, note that the $T_2$ option dominates the $T_1$ option (same payoff if exercised at $T_1$, plus additional optionality). □

**Remark:** With dividends, the monotonicity can be violated for sufficiently high dividend yield.

### Implications for Total Variance

**Proposition 4.3.2**  
Monotonicity $C(T_1) \leq C(T_2)$ does **not** immediately imply $\sigma_{\text{IV}}(T_1) \leq \sigma_{\text{IV}}(T_2)$.

However, for **total variance** $w(K, T) = \sigma_{\text{IV}}^2(K, T) \cdot T$:

**Corollary 4.3.3** (Total Variance Non-Decreasing)  
Under certain technical conditions, the total variance $w(K, T)$ is non-decreasing in $T$ for fixed $K$.

This is a weaker statement than monotonicity of implied volatility itself, which can decrease with maturity (volatility term structure inversion).

## Durrleman's Necessary and Sufficient Conditions

### General Arbitrage-Free Conditions

Durrleman (2010) established the complete characterization of arbitrage-free implied volatility surfaces.

**Theorem 4.3.6** (Durrleman's Conditions)  
An implied volatility surface $\sigma_{\text{IV}}(K, T)$ is arbitrage-free if and only if:

1. **Butterfly arbitrage-free:** For each $T$,

   $$
   \frac{\partial^2 C_{\text{BS}}}{\partial K^2} \geq 0
   $$



2. **Calendar arbitrage-free:** For each $K$,

   $$
   \frac{\partial C_{\text{BS}}}{\partial T} \geq 0
   $$



where the partial derivatives are computed while $\sigma_{\text{IV}}(K, T)$ may vary with $T$ or $K$.

### Conversion to Total Variance Space

In terms of total variance $w(K, T) = \sigma_{\text{IV}}^2 T$:

**Corollary 4.3.4** (Arbitrage-Free in $(w, y)$ Coordinates)  
Let $y = \ln(K/F)$. The surface is arbitrage-free if:


$$
w_T(1 - \frac{y w_y}{2w})^2 \geq \frac{w_y^2}{4}\left(\frac{1}{w} + \frac{1}{4}\right) - \frac{w_{yy}}{2}
$$



and


$$
w_T \geq 0
$$



where subscripts denote partial derivatives.

## Constraints on Implied Volatility Derivatives

### Bounds on Skew

**Proposition 4.3.3** (Skew Bounds)  
For the surface to be arbitrage-free, the **skew** (derivative of IV with respect to log-strike) satisfies:


$$
\left| \frac{\partial \sigma_{\text{IV}}}{\partial (\ln K)} \right| \leq \frac{C_{\max}}{\sigma_{\text{IV}} \sqrt{T}}
$$



for some constant $C_{\max}$ depending on the specific no-arbitrage formulation.

### Bounds on Curvature

**Proposition 4.3.4** (Convexity of Total Variance)  
A sufficient (but not necessary) condition for no butterfly arbitrage is:


$$
\frac{\partial^2 w}{\partial y^2} \geq 0
$$



i.e., total variance is convex in log-strike.

This is **stronger** than the Gatheral constraint but easier to verify.

## Connection to Risk-Neutral Density

### Breeden-Litzenberger Formula

The arbitrage-free condition $\partial^2 C / \partial K^2 \geq 0$ arises from:


$$
\frac{\partial^2 C}{\partial K^2} = e^{-rT} q(K)
$$



where $q(K)$ is the risk-neutral probability density of $S_T$.

Non-negativity of $q(K)$ is necessary and sufficient for:


$$
\int_0^\infty q(K) dK = 1 \quad \text{(probability measure)}
$$



### Moment Explosion Constraints

**Theorem 4.3.7** (Lee's Moment Formula)  
For the implied volatility surface to admit a finite-variance risk-neutral density:


$$
\lim_{|y| \to \infty} \sigma_{\text{IV}}^2(y, T) |y| = \infty
$$



where $y = \ln(K/F)$ is log-moneyness.

*This prevents probability mass from accumulating in the tails too heavily.*

**Corollary 4.3.5** (Wing Slope Bounds)  
As $y \to \pm \infty$:


$$
\sigma_{\text{IV}}^2(y, T) \geq C \frac{|y|}{T}
$$



for some constant $C > 0$, ensuring finite variance.

## Practical Arbitrage Detection

### Discrete Strike Grid

In practice, option prices are observed on a discrete grid $(K_i, T_j)$. Arbitrage violations manifest as:

1. **Butterfly violations:**

   $$
   C(K_i) - 2C(K_{i+1}) + C(K_{i+2}) < -\epsilon
   $$


   for small tolerance $\epsilon > 0$

2. **Calendar violations:**

   $$
   C(K_i, T_j) > C(K_i, T_{j+1}) + \epsilon
   $$



### Arbitrage-Free Interpolation

To construct an arbitrage-free surface from discrete data:

**Method 1:** Fit parametric form (e.g., SVI) with arbitrage constraints built in

**Method 2:** Use convex interpolation schemes:
- Piecewise linear in total variance $w(y, T)$
- Ensure $w_T \geq 0$ and $w_{yy} \geq 0$ (sufficient conditions)

**Method 3:** Project onto arbitrage-free space:
- Minimize distance to observed prices
- Subject to Gatheral/Durrleman constraints

## High-Order Constraints

### Higher-Derivative Bounds

Beyond second-order convexity, market data suggests:

**Empirical Observation:**  
The fourth derivative $\partial^4 C / \partial K^4$ is typically small and changes sign, indicating that:
- Butterfly spreads are concave in strike spacing (approximate quadratic behavior)
- Risk-neutral density has bounded derivatives

### Smoothness and Regularity

**Conjecture (Phenomenological):**  
Real implied volatility surfaces are $C^2$ in both $(K, T)$ with occasional jumps (e.g., earnings announcements, dividends).

Mathematical models (local vol, stochastic vol) typically generate $C^\infty$ smooth surfaces, suggesting microstructure noise accounts for observed roughness.

## Summary of Arbitrage Constraints

The implied volatility surface must satisfy:

### **Point-wise bounds:**

$$
\max(S e^{-qT} - K e^{-rT}, 0) < C < S e^{-qT}
$$



### **Strike monotonicity:**

$$
\frac{\partial C}{\partial K} \leq 0
$$



### **Strike convexity (Butterfly):**

$$
\frac{\partial^2 C}{\partial K^2} \geq 0
$$



### **Maturity monotonicity (Calendar):**

$$
\frac{\partial C}{\partial T} \geq 0
$$



### **Total variance monotonicity:**

$$
\frac{\partial w}{\partial T} \geq 0
$$



### **Wing behavior (Lee's constraint):**

$$
\lim_{|y| \to \infty} \sigma_{\text{IV}}^2(y, T) |y| = \infty
$$



These conditions ensure:
1. Existence of a valid probability measure (risk-neutral density $\geq 0$, integrates to 1)
2. No static arbitrage via butterfly or calendar spreads
3. Finite moments for the underlying distribution

Violation of any constraint allows construction of a riskless profit strategy, invalidating the surface for pricing and hedging.
