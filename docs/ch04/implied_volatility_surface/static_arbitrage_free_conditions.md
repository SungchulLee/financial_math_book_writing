# Static Arbitrage-Free Conditions

## Introduction

An **arbitrage-free implied volatility surface** must satisfy a set of structural constraints that prevent the construction of portfolios with guaranteed riskless profits. These conditions arise from the fundamental requirement that the risk-neutral probability density derived from option prices must be non-negative, integrate to one, and be consistent with the pricing of more complex derivatives. This section provides a complete mathematical characterization of static arbitrage-free conditions.

## Fundamental No-Arbitrage Principles

### Static Arbitrage

A **static arbitrage** is a portfolio of options and cash that:
1. Has non-positive initial cost: $V_0 \leq 0$
2. Has non-negative payoff at all terminal states: $V_T(S_T) \geq 0$ for all $S_T$
3. Has strictly positive payoff with positive probability: $\mathbb{P}(V_T > 0) > 0$

**Absence of static arbitrage** requires that no such portfolio exists.

### Call Spread Arbitrage

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

### Butterfly Spread Arbitrage

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

### Calendar Spread Arbitrage

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

### Breeden-Litzenberger Density Constraint

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

### Normalization: Probability Sums to One

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

### Total Variance Definition

Define **total variance**:
$$
w(K, T) := \sigma_{\text{IV}}^2(K, T) \cdot T
$$

Using log-moneyness $y = \ln(K/F)$ where $F = S_0 e^{(r-q)T}$ is the forward:
$$
w(y, T)
$$

### Durrleman's Complete Characterization

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

### Gatheral's Simplified Condition

For **fixed maturity** $T$, a sufficient (but not necessary) condition:

$$
\frac{\partial^2 w}{\partial y^2} \geq 0
$$

i.e., total variance is convex in log-moneyness.

**Advantage:** Simpler to check than Durrleman's condition

**Disadvantage:** Overly restrictive (many arbitrage-free surfaces violate this)

## Constraints on Implied Volatility Derivatives

### Bounds on Skew

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

### Bounds on Curvature

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

### Wing Behavior Constraint

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

### Left and Right Wing Slopes

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

### Discrete Grid Checks

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

### Visualization Tools

**Density plot:** Compute $q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}$ and verify $q(K) \geq 0$ everywhere.

**Butterfly plot:** Plot $B_i$ vs $K_i$ for each maturity; all values should be non-negative.

**Calendar plot:** Plot $C(K, T_{j+1}) - C(K, T_j)$ vs $K$; all values should be non-negative.

## Arbitrage-Free Interpolation and Extrapolation

### Interpolation Problem

**Given:** Observed option prices at discrete strikes $\{K_i\}$ for maturity $T$

**Goal:** Construct smooth call price function $C(K)$ that:
1. Passes through observed points
2. Satisfies arbitrage constraints
3. Is smooth enough for numerical differentiation

### Cubic Spline with Constraints

Standard cubic splines can introduce spurious oscillations violating convexity.

**Solution:** Use **monotone and convex splines**:
- Enforce $C_K \leq 0$ (monotonicity)
- Enforce $C_{KK} \geq 0$ (convexity)

**Implementation:** Quadratic programming with inequality constraints.

### Arbitrage-Free Parametrizations

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

### Extrapolation to Wings

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

### Smoothness of Density

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

### Higher Butterflies

Consider a **condor spread** (4 strikes):
- Long $K_1, K_4$
- Short $K_2, K_3$

**No-arbitrage:** Its price must be non-negative.

This imposes additional (weaker) constraints on higher derivatives of $C$.

## Calendar-Butterfly Joint Constraints

### Cross-Derivative Constraints

Durrleman's condition involves both $w_T$ (calendar) and $w_{yy}$ (butterfly) simultaneously.

**Key insight:** Calendar and butterfly constraints are **coupled**. Satisfying each separately is necessary but not sufficient.

**Example:** A surface with:
- $w_{yy} \geq 0$ for each $T$
- $w_T \geq 0$ for each $y$

can still violate Durrleman's joint condition $g(y, T) \geq 0$.

**Practical implication:** Must check the full Durrleman constraint, not just separate conditions.

## Relationship to Model Calibration

### Local Volatility Extraction

If the call price surface violates arbitrage, **Dupire's formula** can produce:
- Negative local volatility $\sigma_{\text{loc}}^2 < 0$
- Infinite local volatility $\sigma_{\text{loc}}^2 = \infty$
- Complex local volatility $\sigma_{\text{loc}} \in \mathbb{C}$

**Consequence:** Models fail to calibrate. 

**Solution:** Enforce arbitrage-free constraints before extracting local vol.

### Stochastic Volatility Models

Arbitrage violations also prevent calibration of parametric models (Heston, SABR):
- Optimization may not converge
- Calibrated parameters may be unrealistic (e.g., $\rho = -1.2 > 1$)

**Best practice:** Clean data for arbitrage violations before calibration.

## Empirical Violations and Causes

### Bid-Ask Spreads

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

### Illiquidity and Stale Quotes

Deep OTM or far-dated options may have:
- Wide bid-ask spreads
- Stale quotes (not updated recently)
- Few or zero trades

**Consequence:** Implied volatility may appear to violate arbitrage due to data staleness.

**Solution:** Filter based on volume, open interest, bid-ask width.

### Microstructure Noise

High-frequency fluctuations in prices can temporarily violate arbitrage on a tick-by-tick basis.

**Solution:** Use time-averaged or volume-weighted prices.

### Discrete Dividends

Anticipated discrete dividends create discontinuities in the forward price, complicating arbitrage analysis.

**Solution:** Adjust for dividends explicitly or work in dividend-adjusted coordinates.

## Summary of Arbitrage-Free Conditions

An implied volatility surface is arbitrage-free if and only if:

### **Pointwise bounds:**
$$
\max(S e^{-qT} - K e^{-rT}, 0) < C(K, T) < S e^{-qT}
$$

### **Monotonicity in strike:**
$$
\frac{\partial C}{\partial K} \leq 0 \quad \text{(call spreads)}
$$

### **Convexity in strike:**
$$
\frac{\partial^2 C}{\partial K^2} \geq 0 \quad \text{(butterflies, Breeden-Litzenberger)}
$$

### **Monotonicity in maturity:**
$$
\frac{\partial C}{\partial T} \geq 0 \quad \text{(calendar spreads)}
$$

### **Durrleman's joint condition:**
$$
g(y, T) = \left(1 - \frac{y w_y}{2w}\right)^2 - \frac{w_y^2}{4}\left(\frac{1}{w} + \frac{1}{4}\right) + \frac{w_{yy}}{2} \geq 0
$$

### **Wing behavior (Lee):**
$$
\lim_{|y| \to \infty} \frac{\sigma_{\text{IV}}^2(y, T) T}{|y|} = 2 \quad \text{(finite variance)}
$$

### **Practical workflow:**

1. **Collect market data:** Option prices or implied volatilities
2. **Clean data:** Remove stale quotes, filter illiquidity
3. **Interpolate:** Use arbitrage-free parametrizations (SVI, SSVI)
4. **Verify constraints:** Check butterfly, calendar, Durrleman conditions
5. **Extrapolate wings:** Use power law tails consistent with Lee's formula
6. **Extract density/local vol:** Apply Breeden-Litzenberger/Dupire

**Key principle:** Static arbitrage-free conditions are **necessary** for the existence of a valid risk-neutral measure and for meaningful model calibration. Any violation indicates mispricing, data error, or market friction that must be addressed before further analysis.
