# BSDE-Based Risk Measures

Backward Stochastic Differential Equations (BSDEs) provide a powerful mathematical framework for defining **dynamic, time-consistent risk measures**. The recursive structure of BSDEs naturally encodes the time-consistency property.

---

## Introduction to BSDEs

A **backward stochastic differential equation** has the form:

$$
Y_t = X + \int_t^T g(s, Y_s, Z_s) \, ds - \int_t^T Z_s \, dW_s
$$

where:
- $X \in L^2(\mathcal{F}_T)$ is the **terminal condition** (e.g., a loss at maturity)
- $g: [0,T] \times \mathbb{R} \times \mathbb{R}^d \to \mathbb{R}$ is the **driver** (or generator)
- $(Y_t)_{t \in [0,T]}$ is the **solution process** (adapted)
- $(Z_t)_{t \in [0,T]}$ is the **control process** (adapted)
- $(W_t)$ is a $d$-dimensional Brownian motion

**Key insight:** Unlike forward SDEs, BSDEs specify the terminal value and work backward in time.

---

## Risk Measure Interpretation

Given a BSDE with terminal condition $X$ (the loss), define:

$$
\rho_t(X) := Y_t
$$

The solution $Y_t$ represents the **dynamic risk assessment** of the terminal loss $X$ at time $t$.

**Why this works:**
- $Y_T = X$: At maturity, risk equals the realized loss
- $Y_t$ for $t < T$: Risk assessment given information $\mathcal{F}_t$
- The BSDE propagates risk backward through time

---

## The Role of the Driver

The driver $g(t, y, z)$ encodes **risk preferences**:

| Driver $g$ | Risk Measure Type |
|------------|------------------|
| $g = 0$ | Conditional expectation |
| $g(y,z) = \gamma |z|^2 / 2$ | Entropic risk |
| $g$ convex in $z$ | Convex risk measure |
| $g$ positively homogeneous in $(y,z)$ | Coherent risk measure |

**General principle:** More "aggressive" drivers (larger $g$) correspond to more conservative (risk-averse) measures.

---

## Standard Assumptions

For existence and uniqueness of BSDE solutions, standard conditions on $g$ are:

### Lipschitz Condition
$$
|g(t, y_1, z_1) - g(t, y_2, z_2)| \le K(|y_1 - y_2| + |z_1 - z_2|)
$$

### Growth Condition
$$
|g(t, 0, 0)| \le K
$$

Under these conditions (Pardoux-Peng, 1990), the BSDE has a unique adapted solution $(Y, Z)$.

---

## g-Expectations (Peng)

**g-expectation** is a nonlinear generalization of conditional expectation:

$$
\mathcal{E}_g[X | \mathcal{F}_t] := Y_t
$$

where $Y$ solves the BSDE with terminal condition $X$ and driver $g$.

### Properties of g-Expectations

If $g$ satisfies appropriate conditions:

1. **Monotonicity:** $X \ge X' \Rightarrow \mathcal{E}_g[X | \mathcal{F}_t] \ge \mathcal{E}_g[X' | \mathcal{F}_t]$

2. **Time-Consistency:** 
   $$\mathcal{E}_g[X | \mathcal{F}_s] = \mathcal{E}_g[\mathcal{E}_g[X | \mathcal{F}_t] | \mathcal{F}_s]$$ 
   for $s < t$

3. **Translation Invariance:** If $g$ is independent of $y$:
   $$\mathcal{E}_g[X + m | \mathcal{F}_t] = \mathcal{E}_g[X | \mathcal{F}_t] + m$$
   for $\mathcal{F}_t$-measurable $m$

4. **Convexity:** If $g$ is convex in $z$:
   $$\mathcal{E}_g[\lambda X + (1-\lambda)Y | \mathcal{F}_t] \le \lambda \mathcal{E}_g[X | \mathcal{F}_t] + (1-\lambda)\mathcal{E}_g[Y | \mathcal{F}_t]$$

---

## Example: Linear Driver (Conditional Expectation)

If $g(t, y, z) = 0$, the BSDE becomes:

$$
Y_t = X - \int_t^T Z_s \, dW_s
$$

Taking conditional expectations:
$$
Y_t = \mathbb{E}[X | \mathcal{F}_t]
$$

This recovers the standard conditional expectation.

---

## Example: Entropic Risk Measure

Consider the driver:
$$
g(t, y, z) = \frac{\gamma}{2} |z|^2
$$

The solution satisfies:
$$
Y_t = \frac{1}{\gamma} \log \mathbb{E}\left[e^{\gamma X} \big| \mathcal{F}_t\right]
$$

This is the **conditional entropic risk measure** with risk aversion parameter $\gamma$.

**Properties:**
- Convex but not positively homogeneous
- More sensitive to tail losses than conditional expectation
- Connects to exponential utility maximization

---

## Example: Coherent Risk Measures

For coherent measures, the driver must be positively homogeneous:
$$
g(t, \lambda y, \lambda z) = \lambda g(t, y, z) \quad \text{for } \lambda > 0
$$

A canonical example:
$$
g(t, y, z) = \theta |z|
$$

for some $\theta \ge 0$. This generates a **penalty for volatility exposure**.

---

## Time-Consistency from BSDEs

BSDEs naturally produce time-consistent risk measures due to their recursive structure.

**Proof sketch:** Let $\rho_t(X) = Y_t$ where $Y$ solves the BSDE with terminal condition $X$. Then:

1. For $s < t$, $Y_s$ is the BSDE solution at time $s$ with "terminal condition" $Y_t$ at time $t$
2. This gives: $\rho_s(X) = \rho_s(-\rho_t(X))$
3. This is precisely the time-consistency condition

**Key insight:** The flow property of BSDE solutions encodes time-consistency automatically.

---

## Comparison Theorem

**Theorem:** If $X \le X'$ a.s. and $g \le g'$, then the corresponding BSDE solutions satisfy:
$$
Y_t \le Y'_t \quad \text{a.s. for all } t
$$

This ensures **monotonicity** of BSDE-based risk measures.

---

## Dual Representation via BSDEs

For convex risk measures defined via BSDEs, there is a dual representation:

$$
\rho_t(X) = \operatorname{ess\,sup}_{\mathbb{Q} \in \mathcal{Q}} \left\{ \mathbb{E}^\mathbb{Q}[X | \mathcal{F}_t] - \alpha_t(\mathbb{Q}) \right\}
$$

where:
- $\mathcal{Q}$ is a set of equivalent probability measures
- $\alpha_t(\mathbb{Q})$ is a penalty function related to the driver $g$

The driver $g$ and penalty $\alpha$ are connected via **convex duality**.

---

## Quadratic BSDEs

When $g$ has quadratic growth in $z$:
$$
|g(t, y, z)| \le K(1 + |y| + |z|^2)
$$

the theory becomes more delicate:
- Solutions may not exist for all terminal conditions
- Uniqueness may fail
- Special techniques (BMO martingales) are required

**Relevance:** Quadratic BSDEs arise in entropic risk and exponential utility problems.

---

## Multidimensional Extensions

For portfolios with multiple risk factors, consider BSDEs driven by multidimensional Brownian motion:

$$
Y_t = X + \int_t^T g(s, Y_s, Z_s) \, ds - \int_t^T Z_s \cdot dW_s
$$

where $Z_s \in \mathbb{R}^d$ and $W$ is $d$-dimensional.

The driver can incorporate:
- Correlation structure between risk factors
- Factor-specific risk aversion
- Cross-hedging effects

---

## Applications in Finance

### Option Pricing Under Constraints
BSDEs with suitable drivers price derivatives under portfolio constraints (no short-selling, funding costs).

### Valuation Adjustments (XVA)
XVA calculations naturally formulate as BSDEs:
$$
V_t = \text{Payoff}_T + \int_t^T g(s, V_s, \nabla V_s) \, ds - \int_t^T \nabla V_s \cdot dW_s
$$

where $g$ incorporates CVA, DVA, FVA, KVA effects.

### Dynamic Portfolio Optimization
Risk-averse portfolio optimization leads to BSDE characterizations of value functions.

### Capital Allocation
BSDE solutions enable dynamic, time-consistent capital allocation across business units.

---

## Numerical Methods for BSDEs

Since BSDEs propagate backward, numerical schemes work from $T$ to $0$:

### Time Discretization
For partition $0 = t_0 < t_1 < \cdots < t_n = T$:
$$
Y_{t_i} \approx \mathbb{E}[Y_{t_{i+1}} + g(t_i, Y_{t_{i+1}}, Z_{t_i}) \Delta t | \mathcal{F}_{t_i}]
$$

### Monte Carlo Methods
1. Simulate paths forward
2. Compute terminal values
3. Regress backward to estimate conditional expectations

### Deep Learning Approaches
Neural networks can approximate the solution $(Y_t, Z_t)$ directly.

---

## Connection to PDEs

Via the **nonlinear Feynman-Kac formula**, BSDE solutions connect to PDEs:

If $Y_t = u(t, X_t)$ where $X$ is a diffusion, then $u$ satisfies:
$$
\partial_t u + \mathcal{L}u + g(t, u, \sigma^\top \nabla u) = 0
$$

with terminal condition $u(T, x) = h(x)$.

This connects BSDE-based risk measures to **nonlinear PDEs**.

---

## Key Takeaways

- BSDEs generate dynamic, time-consistent risk measures via $\rho_t(X) = Y_t$
- The driver $g$ encodes risk preferences (linear = expectation, convex = risk-averse)
- g-expectations generalize conditional expectations to nonlinear settings
- Time-consistency follows automatically from BSDE structure
- BSDEs unify pricing, hedging, and risk measurement in a single framework
- Numerical methods propagate backward using conditional expectations

---

## Further Reading

- Peng, S. (1997), "Backward SDE and Related g-Expectation"
- El Karoui, N., Peng, S., & Quenez, M.-C. (1997), "Backward Stochastic Differential Equations in Finance"
- Delbaen, F., Peng, S., & Rosazza Gianin, E. (2010), "Representation of the Penalty Term of Dynamic Concave Utilities"
- Pardoux, E. & Peng, S. (1990), "Adapted Solution of a Backward Stochastic Differential Equation"
- Crépey, S. (2015), "Bilateral Counterparty Risk under Funding Constraints" (BSDE approach to XVA)
