# Arbitrage Constraints on Implied Volatility


## Introduction


The existence of implied volatility requires that market prices satisfy fundamental no-arbitrage bounds. These constraints arise from static replication arguments and ensure that the pricing map $\sigma \mapsto C_{\text{BS}}(\sigma)$ has the correct domain and range for inversion. Beyond simple bounds, arbitrage-free conditions impose structural requirements on the implied volatility surface across strikes and maturities.

## Static No-Arbitrage Bounds


### 1. Point-Wise Bounds for Call Options


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

### 2. Implications for Implied Volatility Domain


**Corollary 4.3.1** (Admissible Price Domain)  
The domain of the implied volatility inverse map is:


$$
\mathcal{D}_C = (C_{\text{intrinsic}}, S e^{-qT})
$$



where $C_{\text{intrinsic}} = \max(S e^{-qT} - K e^{-rT}, 0)$.

Any price outside this interval either:

1. Admits arbitrage (economically infeasible)
2. Corresponds to $\sigma_{\text{IV}} \in \{0, \infty\}$ (boundary cases)

### 3. Put Option Bounds


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


### 1. Call Prices Decreasing in Strike


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

### 2. Implications for Implied Volatility


**Proposition 4.3.1**  
Monotonicity of call prices in strike does **not** imply monotonicity of implied volatility in strike.

The volatility smile/skew empirically exhibits:

- $\sigma_{\text{IV}}(K)$ often decreasing for $K < K_{\text{ATM}}$ (skew)
- $\sigma_{\text{IV}}(K)$ often increasing for $K > K_{\text{ATM}}$ (smile)

This is consistent with arbitrage-free pricing because the transformation $C \leftrightarrow \sigma_{\text{IV}}$ is non-linear.

### 3. Convexity: Butterfly Spread Constraint


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

### 4. Implications for Implied Volatility Surface


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


### 1. Monotonicity in Maturity


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

### 2. Implications for Total Variance


**Proposition 4.3.2**  
Monotonicity $C(T_1) \leq C(T_2)$ does **not** immediately imply $\sigma_{\text{IV}}(T_1) \leq \sigma_{\text{IV}}(T_2)$.

However, for **total variance** $w(K, T) = \sigma_{\text{IV}}^2(K, T) \cdot T$:

**Corollary 4.3.3** (Total Variance Non-Decreasing)  
Under certain technical conditions, the total variance $w(K, T)$ is non-decreasing in $T$ for fixed $K$.

This is a weaker statement than monotonicity of implied volatility itself, which can decrease with maturity (volatility term structure inversion).

## Durrleman's Necessary and Sufficient Conditions


### 1. General Arbitrage-Free Conditions


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

### 2. Conversion to Total Variance Space


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


### 1. Bounds on Skew


**Proposition 4.3.3** (Skew Bounds)  
For the surface to be arbitrage-free, the **skew** (derivative of IV with respect to log-strike) satisfies:


$$
\left| \frac{\partial \sigma_{\text{IV}}}{\partial (\ln K)} \right| \leq \frac{C_{\max}}{\sigma_{\text{IV}} \sqrt{T}}
$$



for some constant $C_{\max}$ depending on the specific no-arbitrage formulation.

### 2. Bounds on Curvature


**Proposition 4.3.4** (Convexity of Total Variance)  
A sufficient (but not necessary) condition for no butterfly arbitrage is:


$$
\frac{\partial^2 w}{\partial y^2} \geq 0
$$



i.e., total variance is convex in log-strike.

This is **stronger** than the Gatheral constraint but easier to verify.

## Connection to Risk-Neutral Density


### 1. Breeden-Litzenberger Formula


Recall (see [§ Breeden-Litzenberger Formula](../model_free_results/breeden_litzenberger_formula.md) and [§ Digital Option Pricing](../../ch06/black_scholes_formula/digital_option_pricing.md)): the convexity condition $\partial^2 C / \partial K^2 \geq 0$ is equivalent to non-negativity of the risk-neutral density $q(K) = e^{rT}\partial^2 C/\partial K^2$, which must integrate to one.

### 2. Moment Explosion Constraints


Recall (see [§ Wing Asymptotics and Moment Constraints](../asymptotics_of_implied_volatility/wing_asymptotics_and_moment_constraints.md)): **Lee's moment formula** relates the wing growth rate of total variance to the maximum finite moment of the risk-neutral density. For finite variance, $\sigma_{\text{IV}}^2(y, T) |y| \to \infty$ as $|y| \to \infty$, and the linear lower bound $\sigma_{\text{IV}}^2(y, T) \geq C |y|/T$ holds for some $C > 0$.

## Practical Arbitrage Detection


### 1. Discrete Strike Grid


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



### 2. Arbitrage-Free Interpolation


To construct an arbitrage-free surface from discrete data:

**Method 1:** Fit parametric form (e.g., SVI) with arbitrage constraints built in

**Method 2:** Use convex interpolation schemes:

- Piecewise linear in total variance $w(y, T)$
- Ensure $w_T \geq 0$ and $w_{yy} \geq 0$ (sufficient conditions)

**Method 3:** Project onto arbitrage-free space:

- Minimize distance to observed prices
- Subject to Gatheral/Durrleman constraints

## High-Order Constraints


### 1. Higher-Derivative Bounds


Beyond second-order convexity, market data suggests:

**Empirical Observation:**  
The fourth derivative $\partial^4 C / \partial K^4$ is typically small and changes sign, indicating that:

- Butterfly spreads are concave in strike spacing (approximate quadratic behavior)
- Risk-neutral density has bounded derivatives

### 2. Smoothness and Regularity


**Conjecture (Phenomenological):**  
Real implied volatility surfaces are $C^2$ in both $(K, T)$ with occasional jumps (e.g., earnings announcements, dividends).

Mathematical models (local vol, stochastic vol) typically generate $C^\infty$ smooth surfaces, suggesting microstructure noise accounts for observed roughness.

## Summary of Arbitrage Constraints


The implied volatility surface must satisfy:

### 1. **Point-wise bounds:**


$$
\max(S e^{-qT} - K e^{-rT}, 0) < C < S e^{-qT}
$$



### 2. **Strike monotonicity:**


$$
\frac{\partial C}{\partial K} \leq 0
$$



### 3. **Strike convexity (Butterfly):**


$$
\frac{\partial^2 C}{\partial K^2} \geq 0
$$



### 4. **Maturity monotonicity (Calendar):**


$$
\frac{\partial C}{\partial T} \geq 0
$$



### 5. **Total variance monotonicity:**


$$
\frac{\partial w}{\partial T} \geq 0
$$



### 6. **Wing behavior (Lee's constraint):**


$$
\lim_{|y| \to \infty} \sigma_{\text{IV}}^2(y, T) |y| = \infty
$$



These conditions ensure:

1. Existence of a valid probability measure (risk-neutral density $\geq 0$, integrates to 1)
2. No static arbitrage via butterfly or calendar spreads
3. Finite moments for the underlying distribution

Violation of any constraint allows construction of a riskless profit strategy, invalidating the surface for pricing and hedging.

---

## Exercises

**Exercise 1.** A European call option has spot $S = 100$, strike $K = 95$, risk-free rate $r = 5\%$, dividend yield $q = 2\%$, and maturity $T = 0.5$ years. Compute the no-arbitrage bounds $C_{\text{intrinsic}} < C < S e^{-qT}$. If a broker quotes $C = 6.50$, does implied volatility exist?

??? success "Solution to Exercise 1"
    We need to compute the no-arbitrage bounds with $S = 100$, $K = 95$, $r = 0.05$, $q = 0.02$, and $T = 0.5$.

    First compute the discounted quantities:

    $$
    S e^{-qT} = 100 \cdot e^{-0.02 \times 0.5} = 100 \cdot e^{-0.01} \approx 99.005
    $$

    $$
    K e^{-rT} = 95 \cdot e^{-0.05 \times 0.5} = 95 \cdot e^{-0.025} \approx 92.653
    $$

    The intrinsic value (lower bound) is:

    $$
    C_{\text{intrinsic}} = \max(S e^{-qT} - K e^{-rT}, 0) = \max(99.005 - 92.653, 0) = 6.352
    $$

    The upper bound is:

    $$
    S e^{-qT} = 99.005
    $$

    Therefore the no-arbitrage bounds are $6.352 < C < 99.005$.

    Since the quoted price $C = 6.50$ satisfies $6.352 < 6.50 < 99.005$, it lies in the admissible interval and implied volatility exists. However, note that $C = 6.50$ is very close to the intrinsic value, implying a low implied volatility.

---

**Exercise 2.** Suppose three call options with the same maturity have strikes $K_1 = 90$, $K_2 = 100$, $K_3 = 110$ and prices $C(90) = 14.20$, $C(100) = 8.50$, $C(110) = 4.80$. (a) Verify that strike monotonicity $C(K_1) \geq C(K_2) \geq C(K_3)$ holds. (b) Check whether the butterfly spread constraint $C(K_1) - 2C(K_2) + C(K_3) \geq 0$ is satisfied. (c) What would it mean economically if this constraint were violated?

??? success "Solution to Exercise 2"
    **(a)** Check strike monotonicity:

    - $C(90) = 14.20 \geq C(100) = 8.50$ ✓
    - $C(100) = 8.50 \geq C(110) = 4.80$ ✓

    Strike monotonicity is satisfied.

    **(b)** Check the butterfly spread constraint:

    $$
    C(K_1) - 2C(K_2) + C(K_3) = 14.20 - 2(8.50) + 4.80 = 14.20 - 17.00 + 4.80 = 2.00
    $$

    Since $2.00 \geq 0$, the butterfly spread constraint is satisfied.

    **(c)** If the butterfly constraint were violated (i.e., $C(K_1) - 2C(K_2) + C(K_3) < 0$), it would mean the butterfly spread has a negative initial cost but a non-negative payoff at maturity. This constitutes a static arbitrage: one could buy the butterfly spread (long calls at $K_1$ and $K_3$, short two calls at $K_2$), receive cash up front, and have a guaranteed non-negative payoff. Economically, the violation implies the risk-neutral density is negative somewhere between $K_1$ and $K_3$, which is impossible for a valid probability measure. This would indicate mispricing in the options market.

---

**Exercise 3.** Consider the Gatheral constraint for an arbitrage-free implied volatility surface in terms of total variance $w(y, T) = \sigma_{\text{IV}}^2(y, T) \cdot T$. If $w(y) = 0.04 + 0.02 y + 0.01 y^2$ for a fixed maturity, compute $\frac{\partial w}{\partial y}$ and $\frac{\partial^2 w}{\partial y^2}$. Is the sufficient condition $\frac{\partial^2 w}{\partial y^2} \geq 0$ satisfied?

??? success "Solution to Exercise 3"
    Given $w(y) = 0.04 + 0.02y + 0.01y^2$, compute the partial derivatives:

    $$
    \frac{\partial w}{\partial y} = 0.02 + 0.02y
    $$

    $$
    \frac{\partial^2 w}{\partial y^2} = 0.02
    $$

    The sufficient condition for no butterfly arbitrage is $\frac{\partial^2 w}{\partial y^2} \geq 0$. Since $0.02 > 0$, the condition is satisfied.

    This means that total variance is strictly convex in log-moneyness, which is stronger than the Gatheral constraint. The positive second derivative ensures that the risk-neutral density implied by this total variance parameterization is non-negative, consistent with an arbitrage-free surface.

---

**Exercise 4.** Using the Breeden-Litzenberger formula $\frac{\partial^2 C}{\partial K^2} = e^{-rT} q(K)$, explain why butterfly spread convexity is equivalent to non-negativity of the risk-neutral density. If a parametric model produces $q(K) < 0$ for some strike range, what type of arbitrage strategy could be constructed?

??? success "Solution to Exercise 4"
    The Breeden-Litzenberger formula states:

    $$
    \frac{\partial^2 C}{\partial K^2} = e^{-rT} q(K)
    $$

    where $q(K)$ is the risk-neutral probability density of $S_T$ evaluated at $K$.

    The butterfly spread constraint requires $C(K_1) - 2C(K_2) + C(K_3) \geq 0$ for equally spaced strikes. In the continuous limit with spacing $\Delta K$:

    $$
    C(K - \Delta K) - 2C(K) + C(K + \Delta K) \approx \frac{\partial^2 C}{\partial K^2} (\Delta K)^2
    $$

    This approximation is the finite-difference second derivative. For this to be non-negative, we need $\frac{\partial^2 C}{\partial K^2} \geq 0$, which by Breeden-Litzenberger is equivalent to $e^{-rT} q(K) \geq 0$, i.e., $q(K) \geq 0$. Since $e^{-rT} > 0$, the non-negativity of the second derivative is exactly equivalent to the non-negativity of the risk-neutral density.

    If a parametric model produces $q(K) < 0$ for some strike range $[K_a, K_b]$, one can construct an arbitrage by selling a butterfly spread centered in that region. Specifically, buy calls at $K_a$ and $K_b$ and sell calls at the midpoint $K_m = (K_a + K_b)/2$ in the appropriate ratio. The negative density region means the butterfly has negative cost (you receive premium) but non-negative payoff, yielding a riskless profit.

---

**Exercise 5.** Two European call options with the same strike $K = 100$ have maturities $T_1 = 0.25$ and $T_2 = 0.50$. The observed prices are $C(T_1) = 5.80$ and $C(T_2) = 5.60$, violating calendar monotonicity. (a) Describe a calendar spread arbitrage strategy. (b) Under what market conditions (e.g., discrete dividends) could this apparent violation be consistent with no-arbitrage?

??? success "Solution to Exercise 5"
    **(a)** Calendar spread arbitrage strategy: Since $C(T_2) = 5.60 < C(T_1) = 5.80$ violates the monotonicity $C(T_1) \leq C(T_2)$, we can construct the following arbitrage:

    - Buy the longer-dated call ($T_2 = 0.50$) for $\$5.60$
    - Sell the shorter-dated call ($T_1 = 0.25$) for $\$5.80$

    Net cash inflow at inception: $5.80 - 5.60 = \$0.20$.

    At $T_1 = 0.25$:

    - If $S_{T_1} \leq 100$: the short call expires worthless. We still hold the long $T_2$ call, which has non-negative value. Total P&L $\geq 0.20$
    - If $S_{T_1} > 100$: the short call is exercised, costing $S_{T_1} - 100$. The long call is worth at least its intrinsic value $\max(S_{T_1} - 100, 0) = S_{T_1} - 100$ (and more due to remaining time value). So the long call's value $\geq$ the short call's obligation, and we keep the initial $\$0.20$

    In either case, the strategy generates a riskless profit.

    **(b)** With discrete dividends, this apparent violation can be consistent with no-arbitrage. If a discrete dividend is paid between $T_1$ and $T_2$, the stock price drops by the dividend amount at the ex-date. This reduces the value of the longer-dated call relative to the shorter-dated one, since the longer-dated option "sees" the dividend-induced drop while the shorter-dated one expires before it. In such cases, $C(T_2) < C(T_1)$ does not constitute true arbitrage because early exercise of American calls may be optimal just before the dividend, and the replication argument above breaks down for European calls in the presence of discrete dividends.

---

**Exercise 6.** Lee's moment formula implies that for a finite-variance risk-neutral density, the wing behavior of total variance must satisfy

$$
\sigma_{\text{IV}}^2(y, T) \geq C \frac{|y|}{T}
$$

for large $|y|$. Consider a parametric model with $\sigma_{\text{IV}}(y) = 0.20$ (constant). Does this satisfy Lee's constraint? What does it imply about the moments of the risk-neutral distribution?

??? success "Solution to Exercise 6"
    Lee's constraint requires $\sigma_{\text{IV}}^2(y, T) \geq C |y| / T$ for large $|y|$. With a constant implied volatility model $\sigma_{\text{IV}}(y) = 0.20$:

    $$
    \sigma_{\text{IV}}^2(y, T) = 0.04 \quad \text{for all } y
    $$

    As $|y| \to \infty$, the right-hand side $C |y| / T \to \infty$, while the left-hand side remains constant at $0.04$. Therefore, for any fixed $C > 0$ and $T > 0$, there exists a sufficiently large $|y|$ such that:

    $$
    0.04 < C \frac{|y|}{T}
    $$

    This means the constant volatility model **violates** Lee's constraint in the wings.

    However, this does not mean the Black-Scholes model itself is arbitrage-free-inconsistent. The log-normal distribution under Black-Scholes has all moments finite. Lee's formula relates the wing behavior of implied volatility to the **maximum finite moment** of the risk-neutral distribution. For the log-normal distribution, all moments $\mathbb{E}[S_T^p]$ are finite for every $p > 0$, corresponding to the fact that the implied volatility grows sublinearly (in fact, stays constant) in the wings. The constraint $\sigma_{\text{IV}}^2 \geq C|y|/T$ is a necessary condition for the density to have finite variance, which the log-normal satisfies. The apparent contradiction resolves because the constant $C$ in Lee's formula depends on the maximum moment order, and for log-normal it can be taken arbitrarily small.

---

**Exercise 7.** In Durrleman's framework, the two conditions for an arbitrage-free surface are butterfly arbitrage-free ($\partial^2 C / \partial K^2 \geq 0$) and calendar arbitrage-free ($\partial C / \partial T \geq 0$). Given a surface where total variance is $w(y, T) = 0.01 T + 0.005 |y|$, verify whether both conditions are met. Discuss the implications of the non-differentiability at $y = 0$ for the risk-neutral density.

??? success "Solution to Exercise 7"
    Given $w(y, T) = 0.01T + 0.005|y|$, check the two Durrleman conditions.

    **Calendar arbitrage-free:** We need $\frac{\partial w}{\partial T} \geq 0$:

    $$
    \frac{\partial w}{\partial T} = 0.01 > 0
    $$

    This condition is satisfied for all $(y, T)$.

    **Butterfly arbitrage-free:** We need $\frac{\partial^2 C}{\partial K^2} \geq 0$, which relates to the second derivative of $w$ with respect to $y$. For $y \neq 0$:

    $$
    \frac{\partial w}{\partial y} = \begin{cases} 0.005 & y > 0 \\ -0.005 & y < 0 \end{cases}
    $$

    $$
    \frac{\partial^2 w}{\partial y^2} = 0 \quad \text{for } y \neq 0
    $$

    The sufficient condition $\frac{\partial^2 w}{\partial y^2} \geq 0$ is satisfied (with equality) away from $y = 0$. One would need to verify the full Gatheral constraint at each point, but the zero curvature makes the butterfly condition marginal rather than strictly satisfied.

    **Non-differentiability at $y = 0$:** The function $|y|$ has a kink at $y = 0$, where the left derivative is $-0.005$ and the right derivative is $+0.005$. In the distributional sense:

    $$
    \frac{\partial^2 |y|}{\partial y^2} = 2\delta(y)
    $$

    where $\delta(y)$ is the Dirac delta function. This means:

    $$
    \frac{\partial^2 w}{\partial y^2} = 0.01 \cdot \delta(y)
    $$

    Via Breeden-Litzenberger, the risk-neutral density is proportional to $\frac{\partial^2 C}{\partial K^2}$. The delta function contribution implies a point mass (atom) in the risk-neutral distribution at $y = 0$ (i.e., at the forward price $K = F$). This means the model assigns a discrete positive probability to $S_T$ landing exactly at the forward price, which is economically unrealistic for a continuous underlying. While not technically an arbitrage violation, the non-smooth surface produces a singular risk-neutral distribution that is problematic for practical hedging and pricing.
