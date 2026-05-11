# Static Arbitrage-Free Conditions


## Introduction


An **arbitrage-free implied volatility surface** must satisfy a set of structural constraints that prevent the construction of portfolios with guaranteed riskless profits. These conditions arise from the fundamental requirement that the risk-neutral probability density derived from option prices must be non-negative, integrate to one, and be consistent with the pricing of more complex derivatives. This section provides a complete mathematical characterization of static arbitrage-free conditions.

## Fundamental No-Arbitrage Principles


### 1. Static Arbitrage


A **static arbitrage** is a portfolio of options and cash that:

1. Has non-positive initial cost: $V_0 \leq 0$
2. Has non-negative payoff at all terminal states: $V_T(S_T) \geq 0$ for all $S_T$
3. Has strictly positive payoff with positive probability: $\mathbb{P}(V_T > 0) > 0$

**Absence of static arbitrage** requires that no such portfolio exists.

### 2. Call Spread Arbitrage


Consider a **call spread**:

- Long 1 call at strike $K_1$
- Short 1 call at strike $K_2 > K_1$

**Payoff at maturity:**

$$
V_T(S_T) = \max(S_T - K_1, 0) - \max(S_T - K_2, 0) = \begin{cases}
0 & S_T \leq K_1 \\
S_T - K_1 & K_1 < S_T \leq K_2 \\
K_2 - K_1 & S_T > K_2
\end{cases}
$$



This is non-negative for all $S_T$ and strictly positive when $K_1 < S_T \leq K_2$.

**No-arbitrage condition:**

$$
C(K_1) - C(K_2) \geq 0
$$



with strict inequality unless $K_1 = K_2$.

**Consequence:** Call prices are **monotonically decreasing** in strike:

$$
\frac{\partial C}{\partial K} \leq 0
$$



### 3. Butterfly Spread Arbitrage


Consider a **butterfly spread**:

- Long 1 call at strike $K_1$
- Short 2 calls at strike $K_2 = \frac{K_1 + K_3}{2}$ (midpoint)
- Long 1 call at strike $K_3$

For equal spacing $\Delta K = K_2 - K_1 = K_3 - K_2$:

**Payoff at maturity:** Piecewise linear, tent-shaped:

$$
V_T(S_T) = \begin{cases}
0 & S_T \leq K_1 \\
S_T - K_1 & K_1 < S_T \leq K_2 \\
K_3 - S_T & K_2 < S_T \leq K_3 \\
0 & S_T > K_3
\end{cases}
$$



Non-negative everywhere.

**No-arbitrage condition:**

$$
C(K_1) - 2C(K_2) + C(K_3) \geq 0
$$



**Consequence:** Call prices are **convex** in strike:

$$
\frac{\partial^2 C}{\partial K^2} \geq 0
$$



### 4. Calendar Spread Arbitrage


Consider a **calendar spread**:

- Short 1 call at strike $K$ maturing at $T_1$
- Long 1 call at same strike $K$ maturing at $T_2 > T_1$

**Payoff structure:** At $T_1$, close short position; at $T_2$, receive long position payoff.

For non-dividend-paying stock:

**No-arbitrage condition:**

$$
C(K, T_2) \geq C(K, T_1)
$$



**Consequence:** Call prices are **monotonically increasing** in maturity:

$$
\frac{\partial C}{\partial T} \geq 0
$$



## Mathematical Formulation


### 1. Breeden-Litzenberger Density Constraint


From the Breeden-Litzenberger formula:

$$
q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}
$$



where $q(K)$ is the risk-neutral probability density.

**No-arbitrage requirement:** $q(K) \geq 0$ for all $K > 0$

**Equivalent constraint:**

$$
\frac{\partial^2 C}{\partial K^2} \geq 0 \quad \text{for all } K
$$



This is the **butterfly arbitrage-free condition**.

### 2. Normalization: Probability Sums to One


The density must integrate to unity:

$$
\int_0^\infty q(K) dK = 1
$$



**Verification:** Using integration by parts:

$$
e^{rT} \int_0^\infty \frac{\partial^2 C}{\partial K^2} dK = e^{rT} \left[ \frac{\partial C}{\partial K}\bigg|_0^\infty \right]
$$



Boundary conditions:

- As $K \to 0$: $C(K) \to S_0 e^{-qT}$, so $\frac{\partial C}{\partial K} \to 0$
- As $K \to \infty$: $C(K) \to 0$, so $\frac{\partial C}{\partial K} \to -e^{-rT}$

Thus:

$$
e^{rT}(0 - (-e^{-rT})) = 1 \quad \checkmark
$$



## Constraints in Total Variance Space


### 1. Total Variance Definition


Define **total variance**:

$$
w(K, T) := \sigma_{\text{IV}}^2(K, T) \cdot T
$$



Using log-moneyness $y = \ln(K/F)$ where $F = S_0 e^{(r-q)T}$ is the forward:

$$
w(y, T)
$$



### 2. Durrleman's Complete Characterization


**Theorem 4.3.1** (Durrleman, 2010)  
An implied volatility surface $\sigma_{\text{IV}}(K, T)$ is arbitrage-free if and only if:

1. **Butterfly condition:** For each $T$,

   $$
   g(y, T) := \left(1 - \frac{y w_y(y, T)}{2w(y, T)}\right)^2 - \frac{w_y(y, T)^2}{4}\left(\frac{1}{w(y, T)} + \frac{1}{4}\right) + \frac{w_{yy}(y, T)}{2} \geq 0
   $$



2. **Calendar condition:** For each $K$ (or $y$),

   $$
   w_T(y, T) \geq 0
   $$



where subscripts denote partial derivatives: $w_y = \frac{\partial w}{\partial y}$, etc.

**Proof sketch:** 

- Butterfly condition ensures $\frac{\partial^2 C}{\partial K^2} \geq 0$
- Calendar condition ensures $\frac{\partial C}{\partial T} \geq 0$
- Together, these guarantee a valid probability measure exists

### 3. Gatheral's Simplified Condition


For **fixed maturity** $T$, a sufficient (but not necessary) condition:


$$
\frac{\partial^2 w}{\partial y^2} \geq 0
$$



i.e., total variance is convex in log-moneyness.

**Advantage:** Simpler to check than Durrleman's condition

**Disadvantage:** Overly restrictive (many arbitrage-free surfaces violate this)

## Constraints on Implied Volatility Derivatives


### 1. Bounds on Skew


The **slope of implied volatility** in log-moneyness coordinates:

$$
\mathcal{S}(y, T) := \frac{\partial \sigma_{\text{IV}}}{\partial y}
$$



For the surface to be arbitrage-free:

**Proposition 4.3.1** (Skew Bound)  
There exists a finite bound:

$$
\left| \frac{\partial \sigma_{\text{IV}}}{\partial y} \right| \leq C(T, \sigma_{\text{IV}})
$$



where the bound depends on maturity and the level of IV.

**Heuristic:** Extremely steep skew (e.g., $\frac{\partial \sigma_{\text{IV}}}{\partial y} = -100$) would imply unrealistic densities with most probability concentrated at a single point.

### 2. Bounds on Curvature


The **curvature of implied volatility**:

$$
\mathcal{C}(y, T) := \frac{\partial^2 \sigma_{\text{IV}}}{\partial y^2}
$$



**Proposition 4.3.2** (Curvature Constraint)  
For the Breeden-Litzenberger density to be non-negative:

$$
\frac{\partial^2 \sigma_{\text{IV}}}{\partial y^2} \geq -\frac{f(y, \sigma_{\text{IV}}, T)}{\sigma_{\text{IV}} T}
$$



where $f$ is a function of the current smile level.

**Interpretation:** Negative curvature (downward-bending smile) is permitted but cannot be arbitrarily large in magnitude.

## Lee's Moment Formula


### 1. Wing Behavior Constraint


**Theorem 4.3.2** (Lee, 2004)  
For the risk-neutral distribution to have finite variance:

$$
\lim_{|y| \to \infty} \sigma_{\text{IV}}^2(y, T) \cdot T \cdot \frac{1}{|y|} = 2
$$



More generally, for finite $p$-th moment ($p \geq 2$):

$$
\lim_{|y| \to \infty} \frac{\sigma_{\text{IV}}^2(y, T) T}{|y|} \geq \frac{2}{p}
$$



**Interpretation:** The wings of the implied volatility smile cannot be too flat. As strike moves away from ATM, IV must grow approximately as $\sqrt{|y|/T}$ to prevent infinite variance.

### 2. Left and Right Wing Slopes


Define the **left wing slope**:

$$
p_- = \lim_{y \to -\infty} \frac{\sigma_{\text{IV}}^2(y, T) T}{|y|}
$$



and **right wing slope**:

$$
p_+ = \lim_{y \to +\infty} \frac{\sigma_{\text{IV}}^2(y, T) T}{|y|}
$$



**Constraints:**

$$
0 < p_- \leq 2, \quad 0 < p_+ \leq 2
$$



**Symmetry:** For a symmetric density, $p_- = p_+ = 2$.

**Asymmetry:** Equity markets often have $p_- < p_+$ (left tail flatter than theory predicts due to put overpricing).

## Practical Arbitrage Detection


### 1. Discrete Grid Checks


Given option prices on a discrete grid $(K_i, T_j)$:

**Test 1: Butterfly condition**

For each maturity $T_j$ and strikes $K_{i-1} < K_i < K_{i+1}$:

$$
B_i := C(K_{i-1}) - 2C(K_i) + C(K_{i+1}) \geq -\epsilon
$$



where $\epsilon > 0$ is a small tolerance for numerical error/bid-ask spread.

If $B_i < -\epsilon$, there is **butterfly arbitrage**.

**Test 2: Calendar condition**

For each strike $K_i$ and maturities $T_j < T_{j+1}$:

$$
C(K_i, T_{j+1}) - C(K_i, T_j) \geq -\epsilon
$$



If violated, there is **calendar arbitrage**.

**Test 3: Wing behavior**

Check that for large $|y|$:

$$
\sigma_{\text{IV}}^2(y, T) T \gtrsim 2|y|
$$



If IV is too flat in the wings, the distribution has infinite variance (pathological).

### 2. Visualization Tools


**Density plot:** Compute $q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}$ and verify $q(K) \geq 0$ everywhere.

**Butterfly plot:** Plot $B_i$ vs $K_i$ for each maturity; all values should be non-negative.

**Calendar plot:** Plot $C(K, T_{j+1}) - C(K, T_j)$ vs $K$; all values should be non-negative.

## Arbitrage-Free Interpolation and Extrapolation


### 1. Interpolation Problem


**Given:** Observed option prices at discrete strikes $\{K_i\}$ for maturity $T$

**Goal:** Construct smooth call price function $C(K)$ that:

1. Passes through observed points
2. Satisfies arbitrage constraints
3. Is smooth enough for numerical differentiation

### 2. Cubic Spline with Constraints


Standard cubic splines can introduce spurious oscillations violating convexity.

**Solution:** Use **monotone and convex splines**:

- Enforce $C_K \leq 0$ (monotonicity)
- Enforce $C_{KK} \geq 0$ (convexity)

**Implementation:** Quadratic programming with inequality constraints.

### 3. Arbitrage-Free Parametrizations


**SVI (Stochastic Volatility Inspired):**


$$
w(y) = a + b\left(\rho(y - m) + \sqrt{(y - m)^2 + \sigma^2}\right)
$$



**Arbitrage-free conditions:**

$$
b \geq 0, \quad |b\rho| < 4a, \quad b(1 + |\rho|) < 4a, \quad a + b\sigma\sqrt{1 - \rho^2} \geq 0
$$



Fit parameters $(a, b, \rho, m, \sigma)$ to market data with these constraints.

**SSVI (Surface SVI):** Extends SVI across maturities with joint no-arbitrage constraints.

### 4. Extrapolation to Wings


**Problem:** Options trade only in a limited strike range; need to extrapolate to $K \to 0$ and $K \to \infty$ for density integration.

**Power law tails:**

For large $|y|$, use:

$$
\sigma_{\text{IV}}^2(y, T) T \sim 2|y| + c
$$



where $c$ is calibrated to the outermost observed strikes.

**Exponential decay (alternative):**


$$
\sigma_{\text{IV}}(y) \sim \sigma_\infty + A e^{-\lambda |y|}
$$



**Recommendation:** Use power law (Lee's formula) for consistency with finite variance.

## Higher-Order Constraints


### 1. Smoothness of Density


While $q(K) \geq 0$ is necessary, real densities are smooth (continuous derivatives). 

**Heuristic constraint:**

$$
\frac{\partial q}{\partial K} \text{ bounded}
$$



Equivalently:

$$
\frac{\partial^3 C}{\partial K^3} \text{ bounded}
$$



**Implication:** The call price surface should be $C^3$ smooth, not just $C^2$.

### 2. Higher Butterflies


Consider a **condor spread** (4 strikes):

- Long $K_1, K_4$
- Short $K_2, K_3$

**No-arbitrage:** Its price must be non-negative.

This imposes additional (weaker) constraints on higher derivatives of $C$.

## Calendar-Butterfly Joint Constraints


### 1. Cross-Derivative Constraints


Durrleman's condition involves both $w_T$ (calendar) and $w_{yy}$ (butterfly) simultaneously.

**Key insight:** Calendar and butterfly constraints are **coupled**. Satisfying each separately is necessary but not sufficient.

**Example:** A surface with:

- $w_{yy} \geq 0$ for each $T$
- $w_T \geq 0$ for each $y$

can still violate Durrleman's joint condition $g(y, T) \geq 0$.

**Practical implication:** Must check the full Durrleman constraint, not just separate conditions.

## Relationship to Model Calibration


### 1. Local Volatility Extraction


If the call price surface violates arbitrage, **Dupire's formula** can produce:

- Negative local volatility $\sigma_{\text{loc}}^2 < 0$
- Infinite local volatility $\sigma_{\text{loc}}^2 = \infty$
- Complex local volatility $\sigma_{\text{loc}} \in \mathbb{C}$

**Consequence:** Models fail to calibrate. 

**Solution:** Enforce arbitrage-free constraints before extracting local vol.

### 2. Stochastic Volatility Models


Arbitrage violations also prevent calibration of parametric models (Heston, SABR):

- Optimization may not converge
- Calibrated parameters may be unrealistic (e.g., $\rho = -1.2 > 1$)

**Best practice:** Clean data for arbitrage violations before calibration.

## Empirical Violations and Causes


### 1. Bid-Ask Spreads


Using **mid prices** can create apparent arbitrage:

**Example:**

- Bid for $K_1$ call: \$5.00
- Ask for $K_1$ call: \$5.10
- Bid for $K_2$ call: \$4.95
- Ask for $K_2$ call: \$5.05

Mid prices: $C(K_1) = 5.05$, $C(K_2) = 5.00$

Apparent call spread: $C(K_1) - C(K_2) = 0.05 > 0$ ✓

But using ask for long, bid for short: $5.10 - 4.95 = 0.15$ (costly, no arbitrage).

**Solution:** Use consistent bid/ask convention or conservative estimates.

### 2. Illiquidity and Stale Quotes


Deep OTM or far-dated options may have:

- Wide bid-ask spreads
- Stale quotes (not updated recently)
- Few or zero trades

**Consequence:** Implied volatility may appear to violate arbitrage due to data staleness.

**Solution:** Filter based on volume, open interest, bid-ask width.

### 3. Microstructure Noise


High-frequency fluctuations in prices can temporarily violate arbitrage on a tick-by-tick basis.

**Solution:** Use time-averaged or volume-weighted prices.

### 4. Discrete Dividends


Anticipated discrete dividends create discontinuities in the forward price, complicating arbitrage analysis.

**Solution:** Adjust for dividends explicitly or work in dividend-adjusted coordinates.

## Summary of Arbitrage-Free Conditions


An implied volatility surface is arbitrage-free if and only if:

### 1. **Pointwise bounds:**


$$
\max(S e^{-qT} - K e^{-rT}, 0) < C(K, T) < S e^{-qT}
$$



### 2. **Monotonicity in strike:**


$$
\frac{\partial C}{\partial K} \leq 0 \quad \text{(call spreads)}
$$



### 3. **Convexity in strike:**


$$
\frac{\partial^2 C}{\partial K^2} \geq 0 \quad \text{(butterflies, Breeden-Litzenberger)}
$$



### 4. **Monotonicity in maturity:**


$$
\frac{\partial C}{\partial T} \geq 0 \quad \text{(calendar spreads)}
$$



### 5. **Durrleman's joint condition:**


$$
g(y, T) = \left(1 - \frac{y w_y}{2w}\right)^2 - \frac{w_y^2}{4}\left(\frac{1}{w} + \frac{1}{4}\right) + \frac{w_{yy}}{2} \geq 0
$$



### 6. **Wing behavior (Lee):**


$$
\lim_{|y| \to \infty} \frac{\sigma_{\text{IV}}^2(y, T) T}{|y|} = 2 \quad \text{(finite variance)}
$$



### 7. **Practical workflow:**


1. **Collect market data:** Option prices or implied volatilities
2. **Clean data:** Remove stale quotes, filter illiquidity
3. **Interpolate:** Use arbitrage-free parametrizations (SVI, SSVI)
4. **Verify constraints:** Check butterfly, calendar, Durrleman conditions
5. **Extrapolate wings:** Use power law tails consistent with Lee's formula
6. **Extract density/local vol:** Apply Breeden-Litzenberger/Dupire

**Key principle:** Static arbitrage-free conditions are **necessary** for the existence of a valid risk-neutral measure and for meaningful model calibration. Any violation indicates mispricing, data error, or market friction that must be addressed before further analysis.

---

## Exercises

**Exercise 1.** Three call options with the same maturity have strikes and prices: $C(90) = 15.20$, $C(100) = 9.00$, $C(110) = 5.50$. (a) Verify strike monotonicity. (b) Compute the butterfly spread $B = C(90) - 2C(100) + C(110)$ and verify it is non-negative. (c) If instead $C(110) = 2.00$, would butterfly arbitrage exist? Describe the arbitrage strategy.

??? success "Solution to Exercise 1"
    **(a) Strike monotonicity:** Call prices must decrease as the strike increases:

    $$
    C(90) = 15.20 > C(100) = 9.00 > C(110) = 5.50 \quad \checkmark
    $$

    The monotonicity condition $\frac{\partial C}{\partial K} \leq 0$ is satisfied.

    **(b) Butterfly spread:**

    $$
    B = C(90) - 2C(100) + C(110) = 15.20 - 2(9.00) + 5.50 = 15.20 - 18.00 + 5.50 = 2.70
    $$

    Since $B = 2.70 > 0$, the butterfly condition (convexity of call prices in strike) is satisfied. This confirms the Breeden-Litzenberger density is non-negative in this strike region.

    **(c) If $C(110) = 2.00$:**

    $$
    B = C(90) - 2C(100) + C(110) = 15.20 - 18.00 + 2.00 = -0.80
    $$

    Since $B = -0.80 < 0$, butterfly arbitrage exists. The arbitrage strategy is:

    - Buy 1 call at $K = 90$ (cost \$15.20)
    - Sell 2 calls at $K = 100$ (receive $2 \times \$9.00 = \$18.00$)
    - Buy 1 call at $K = 110$ (cost \$2.00)

    Net initial cash inflow: $18.00 - 15.20 - 2.00 = \$0.80 > 0$. The payoff at maturity is the tent-shaped butterfly payoff, which is non-negative for all $S_T$. Therefore the trade has a strictly positive initial cash inflow and a non-negative terminal payoff, constituting a static arbitrage.

---

**Exercise 2.** Using the Breeden-Litzenberger formula $q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}$, suppose a fitted call price curve has $\frac{\partial^2 C}{\partial K^2} = -0.001$ at some strike $K^*$. (a) What does this imply about the risk-neutral density at $K^*$? (b) What type of arbitrage is present? (c) Describe a portfolio that would exploit this violation.

??? success "Solution to Exercise 2"
    **(a)** The Breeden-Litzenberger formula gives the risk-neutral density as $q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}$. If $\frac{\partial^2 C}{\partial K^2} = -0.001$ at strike $K^*$, then:

    $$
    q(K^*) = e^{rT} \times (-0.001) < 0
    $$

    This implies a **negative risk-neutral probability density** at $K^*$, which is impossible for a valid probability measure.

    **(b)** This is a **butterfly arbitrage**. The negative second derivative means call prices are locally concave at $K^*$, violating the convexity requirement. A butterfly spread centered at $K^*$ would have a negative price despite having a non-negative payoff.

    **(c)** To exploit this violation, construct a butterfly spread centered at $K^*$. Choose a small strike spacing $\Delta K$ and:

    - Buy 1 call at $K^* - \Delta K$
    - Sell 2 calls at $K^*$
    - Buy 1 call at $K^* + \Delta K$

    The cost is approximately $\frac{\partial^2 C}{\partial K^2}\big|_{K^*} (\Delta K)^2 = -0.001 (\Delta K)^2 < 0$, meaning we receive a net cash inflow at initiation. The payoff at maturity is the tent-shaped function, which is non-negative for all $S_T$. This constitutes a static arbitrage: strictly positive initial cash inflow with a non-negative terminal payoff.

---

**Exercise 3.** For the SVI parametrization $w(y) = a + b(\rho(y-m) + \sqrt{(y-m)^2 + \sigma^2})$, verify analytically that the wing behavior satisfies

$$
\lim_{y \to \pm\infty} \frac{w(y)}{|y|} = b(1 \pm \rho)
$$

Use Lee's constraint $0 < p_{\pm} \leq 2$ to derive bounds on $b$ and $\rho$ that ensure the distribution has finite variance.

??? success "Solution to Exercise 3"
    For the SVI parametrization $w(y) = a + b(\rho(y - m) + \sqrt{(y-m)^2 + \sigma^2})$, we analyze the wing behavior as $y \to \pm\infty$.

    **As $y \to +\infty$:**

    $$
    \sqrt{(y - m)^2 + \sigma^2} = |y - m|\sqrt{1 + \frac{\sigma^2}{(y-m)^2}} \approx (y - m)\left(1 + \frac{\sigma^2}{2(y-m)^2}\right) \approx y - m
    $$

    Therefore:

    $$
    w(y) \approx a + b(\rho(y - m) + (y - m)) = a + b(1 + \rho)(y - m)
    $$

    Dividing by $|y| = y$ for large positive $y$:

    $$
    \frac{w(y)}{|y|} \approx \frac{a + b(1+\rho)(y - m)}{y} \to b(1 + \rho) \quad \text{as } y \to +\infty
    $$

    **As $y \to -\infty$:**

    Now $|y - m| = -(y - m)$ for large negative $y$, so:

    $$
    \sqrt{(y-m)^2 + \sigma^2} \approx -(y - m) = m - y
    $$

    Therefore:

    $$
    w(y) \approx a + b(\rho(y - m) + (m - y)) = a + b(1 - \rho)(m - y)
    $$

    Dividing by $|y| = -y$:

    $$
    \frac{w(y)}{|y|} \approx \frac{a + b(1 - \rho)(m - y)}{-y} \to b(1 - \rho) \quad \text{as } y \to -\infty
    $$

    This confirms $\lim_{y \to \pm\infty} \frac{w(y)}{|y|} = b(1 \pm \rho)$.

    **Applying Lee's constraint:** Lee's moment formula requires $0 < p_{\pm} \leq 2$, where $p_+ = b(1 + \rho)$ and $p_- = b(1 - \rho)$. Since $\rho \in [-1, 1]$ and $b \geq 0$:

    - $p_+ = b(1 + \rho) \leq 2 \implies b \leq \frac{2}{1 + \rho}$
    - $p_- = b(1 - \rho) \leq 2 \implies b \leq \frac{2}{1 - \rho}$

    The binding constraint is the smaller of these two bounds:

    $$
    b \leq \frac{2}{1 + |\rho|}
    $$

    which can be written equivalently as $b(1 + |\rho|) \leq 2$. Since we also need the SVI no-arbitrage condition $b(1 + |\rho|) < 4a$ (which ensures non-negative density), the combined constraints are:

    $$
    b(1 + |\rho|) \leq 2 \quad \text{and} \quad b(1 + |\rho|) < 4a
    $$

    These ensure the risk-neutral distribution has finite variance and the implied volatility surface is arbitrage-free.

---

**Exercise 4.** Two call options on the same stock with strike $K = 100$ have maturities $T_1 = 0.25$ and $T_2 = 0.50$. Their total variances are $w(T_1) = 0.01$ and $w(T_2) = 0.018$. (a) Verify the calendar arbitrage-free condition $w(T_2) \geq w(T_1)$. (b) Compute the implied volatilities $\sigma(T_1)$ and $\sigma(T_2)$. (c) Is the term structure upward or downward sloping? (d) Compute the forward volatility $\sigma_{\text{fwd}}(T_1, T_2)$.

??? success "Solution to Exercise 4"
    Given: $K = 100$, $T_1 = 0.25$, $T_2 = 0.50$, $w(T_1) = 0.01$, $w(T_2) = 0.018$.

    **(a) Calendar arbitrage-free condition:**

    $$
    w(T_2) = 0.018 \geq w(T_1) = 0.01 \quad \checkmark
    $$

    The total variance is non-decreasing in maturity, so the calendar condition is satisfied.

    **(b) Implied volatilities:**

    $$
    \sigma(T_1) = \sqrt{\frac{w(T_1)}{T_1}} = \sqrt{\frac{0.01}{0.25}} = \sqrt{0.04} = 0.20 = 20\%
    $$

    $$
    \sigma(T_2) = \sqrt{\frac{w(T_2)}{T_2}} = \sqrt{\frac{0.018}{0.50}} = \sqrt{0.036} = 0.1897 \approx 19.0\%
    $$

    **(c) Term structure direction:** Since $\sigma(T_2) = 19.0\% < \sigma(T_1) = 20.0\%$, the term structure is **downward sloping** (inverted). This is consistent with a regime where current volatility is above its long-run mean and is expected to mean-revert downward.

    Note that the term structure can be downward sloping while still satisfying the no-arbitrage condition, because the calendar constraint requires $w(T)$ (not $\sigma(T)$) to be non-decreasing. Here $w$ increases from 0.01 to 0.018, but $\sigma$ decreases because $w$ does not grow fast enough relative to $T$.

    **(d) Forward volatility:**

    $$
    \sigma_{\text{fwd}}^2(T_1, T_2) = \frac{w(T_2) - w(T_1)}{T_2 - T_1} = \frac{0.018 - 0.01}{0.50 - 0.25} = \frac{0.008}{0.25} = 0.032
    $$

    $$
    \sigma_{\text{fwd}}(T_1, T_2) = \sqrt{0.032} = 0.1789 \approx 17.9\%
    $$

    The forward volatility of 17.9% is below both spot implied volatilities, confirming the market's expectation that volatility will decline over the 3-month to 6-month horizon.

---

**Exercise 5.** Explain why Gatheral's simplified sufficient condition $\frac{\partial^2 w}{\partial y^2} \geq 0$ (convexity of total variance in log-moneyness) is more restrictive than Durrleman's necessary and sufficient condition. Give an example of a total variance function $w(y)$ that violates convexity but still satisfies the full Durrleman condition.

??? success "Solution to Exercise 5"
    **Gatheral's condition** requires $\frac{\partial^2 w}{\partial y^2} \geq 0$, meaning total variance must be globally convex in log-moneyness. **Durrleman's condition** is:

    $$
    g(y, T) = \left(1 - \frac{y w_y}{2w}\right)^2 - \frac{w_y^2}{4}\left(\frac{1}{w} + \frac{1}{4}\right) + \frac{w_{yy}}{2} \geq 0
    $$

    Gatheral's condition is more restrictive because it ignores the positive contributions from the first two terms in $g(y, T)$. The term $\left(1 - \frac{y w_y}{2w}\right)^2 \geq 0$ always contributes non-negatively, and the term $-\frac{w_y^2}{4}(\frac{1}{w} + \frac{1}{4})$ is always non-positive. However, the squared term can be large enough to compensate for both the negative term and a mildly negative $w_{yy}$.

    Specifically, even if $w_{yy} < 0$ (violating Gatheral), we can have $g(y, T) \geq 0$ provided:

    $$
    \frac{w_{yy}}{2} \geq -\left(1 - \frac{y w_y}{2w}\right)^2 + \frac{w_y^2}{4}\left(\frac{1}{w} + \frac{1}{4}\right)
    $$

    **Example:** Consider the total variance function

    $$
    w(y) = 0.04 + 0.01 y - 0.005 y^2 + 0.04 y^4
    $$

    Near $y = 0$: $w_{yy}(0) = -0.01 < 0$, violating Gatheral's convexity condition. However, $w(0) = 0.04$, $w_y(0) = 0.01$. Computing Durrleman's function:

    $$
    g(0) = \left(1 - 0\right)^2 - \frac{(0.01)^2}{4}\left(\frac{1}{0.04} + \frac{1}{4}\right) + \frac{-0.01}{2}
    $$

    $$
    = 1 - 0.000025 \times 25.25 - 0.005 = 1 - 0.000631 - 0.005 = 0.994 > 0
    $$

    So the surface satisfies Durrleman's condition at $y = 0$ despite failing Gatheral's simplified test. The dominant $1^2 = 1$ term from the squared factor overwhelms the small negative curvature contribution.

---

**Exercise 6.** A market data set shows the following mid-market call prices for 3-month options: $C(95) = 10.20$, $C(100) = 7.50$, $C(105) = 5.80$, $C(110) = 3.50$. The bid-ask spread is \$0.15 for all strikes. (a) Check butterfly and call-spread conditions using mid prices. (b) Could any apparent violations be explained by bid-ask spreads? (c) Explain the distinction between violations at mid prices versus executable prices.

??? success "Solution to Exercise 6"
    Given 3-month call prices: $C(95) = 10.20$, $C(100) = 7.50$, $C(105) = 5.80$, $C(110) = 3.50$. Bid-ask spread is \$0.15 for all strikes.

    **(a) Checking conditions using mid prices:**

    **Call-spread conditions** ($C(K_1) > C(K_2)$ for $K_1 < K_2$):

    - $C(95) - C(100) = 10.20 - 7.50 = 2.70 > 0$ $\checkmark$
    - $C(100) - C(105) = 7.50 - 5.80 = 1.70 > 0$ $\checkmark$
    - $C(105) - C(110) = 5.80 - 3.50 = 2.30 > 0$ $\checkmark$

    **Butterfly conditions:**

    - $B_1 = C(95) - 2C(100) + C(105) = 10.20 - 15.00 + 5.80 = 1.00 > 0$ $\checkmark$
    - $B_2 = C(100) - 2C(105) + C(110) = 7.50 - 11.60 + 3.50 = -0.60 < 0$ $\boldsymbol{\times}$

    The butterfly centered at $K = 105$ is violated by $-0.60$.

    **(b) Bid-ask spread explanation:** With a bid-ask spread of \$0.15, mid prices have uncertainty of $\pm \$0.075$. The worst case for the butterfly $B_2$ uses ask prices for the long positions and bid prices for the short position:

    - Long $C(100)$: pay ask = $7.50 + 0.075 = 7.575$
    - Short 2 $C(105)$: receive bid = $2 \times (5.80 - 0.075) = 11.45$
    - Long $C(110)$: pay ask = $3.50 + 0.075 = 3.575$

    Net cost: $7.575 - 11.45 + 3.575 = -0.30$

    Since the executable butterfly still has negative cost ($-0.30$), the apparent arbitrage survives even after accounting for bid-ask spreads in this case. However, if the spread were wider (e.g., \$0.40), the executable cost would be:

    $7.70 - 11.20 + 3.70 = +0.20 > 0$, and the arbitrage would disappear.

    **(c) Mid-price vs. executable price distinction:** Mid prices are the average of bid and ask, representing a theoretical fair value. However, no trader can transact at mid prices. Actual trades occur at the bid (when selling) or ask (when buying). An apparent arbitrage at mid prices may not be executable at actual market prices because:

    - The cost of crossing the bid-ask spread on each leg can exceed the apparent profit
    - The spread represents the market maker's compensation for providing liquidity
    - True arbitrage must be profitable at executable prices (ask for buying, bid for selling)

    In practice, most apparent butterfly violations in market data are explained by bid-ask spreads, but the violation in this example is large enough ($\$0.60$ at mid) that it likely persists even at executable prices.

---

**Exercise 7.** When Dupire's formula is applied to an implied volatility surface that violates the butterfly condition ($\frac{\partial^2 C}{\partial K^2} < 0$), the extracted local volatility becomes imaginary ($\sigma_{\text{loc}}^2 < 0$). Explain why this happens by relating the Dupire formula to the Breeden-Litzenberger density. What preprocessing step should be applied to market data before extracting local volatility?

??? success "Solution to Exercise 7"
    **Dupire's formula** for local volatility is:

    $$
    \sigma_{\text{loc}}^2(K, T) = \frac{\frac{\partial C}{\partial T} + (r - q)K\frac{\partial C}{\partial K} + qC}{\frac{1}{2}K^2 \frac{\partial^2 C}{\partial K^2}}
    $$

    The denominator contains $\frac{\partial^2 C}{\partial K^2}$, which by the **Breeden-Litzenberger formula** is proportional to the risk-neutral density:

    $$
    q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}
    $$

    **Why $\sigma_{\text{loc}}^2 < 0$ when the butterfly condition is violated:**

    When $\frac{\partial^2 C}{\partial K^2} < 0$ at some strike $K^*$, the denominator of Dupire's formula becomes negative. The numerator $\frac{\partial C}{\partial T} + (r-q)K\frac{\partial C}{\partial K} + qC$ is typically positive (it must be positive in an arbitrage-free surface since it relates to the time value of the option). Therefore:

    $$
    \sigma_{\text{loc}}^2(K^*, T) = \frac{\text{positive}}{\text{negative}} < 0
    $$

    Since variance must be non-negative, a negative $\sigma_{\text{loc}}^2$ is meaningless and taking its square root yields an imaginary local volatility.

    The economic intuition is that $\frac{\partial^2 C}{\partial K^2} < 0$ implies a negative risk-neutral density $q(K^*) < 0$, meaning the pricing measure assigns negative probability to the underlying reaching $K^*$. No diffusion process can generate negative probabilities, so no local volatility function can replicate such prices.

    **Required preprocessing step:** Before extracting local volatility, the raw market data (option prices or implied volatilities) must be **smoothed and regularized** to enforce arbitrage-free constraints. The standard workflow is:

    1. **Fit an arbitrage-free parametrization** (such as SVI or SSVI) to the observed implied volatilities, with constraints ensuring $\frac{\partial^2 C}{\partial K^2} \geq 0$ (butterfly), $\frac{\partial C}{\partial T} \geq 0$ (calendar), and Durrleman's joint condition $g(y, T) \geq 0$.
    2. **Use the fitted (not raw) surface** as input to Dupire's formula.
    3. Optionally, apply **monotone convex interpolation** across strikes with enforced convexity constraints.

    This ensures the denominator of Dupire's formula is always non-negative, yielding a well-defined, real-valued local volatility surface.
