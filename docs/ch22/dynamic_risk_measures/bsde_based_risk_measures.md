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

---

## Exercises

**Exercise 1.** A standard BSDE takes the form $-dY_t = f(t, Y_t, Z_t)\,dt - Z_t\,dW_t$ with terminal condition $Y_T = \xi$. Explain why the driver (generator) $f$ determines the risk measure. For the linear driver $f(t,y,z) = \mu\,|z|$, what type of risk measure does the BSDE define?

??? success "Solution to Exercise 1"

    **Why the driver determines the risk measure.** In the standard BSDE:

    $$
    -dY_t = f(t, Y_t, Z_t)\,dt - Z_t\,dW_t, \quad Y_T = \xi
    $$

    the terminal condition $\xi$ specifies the loss being assessed, while the driver $f$ determines *how* risk is propagated backward through time. Setting $\rho_t(\xi) = Y_t$, the driver controls the "nonlinearity" of the risk assessment:

    - If $f = 0$, the BSDE reduces to a martingale representation, and $Y_t = \mathbb{E}[\xi \mid \mathcal{F}_t]$ (risk-neutral expectation).
    - If $f > 0$ (for nonzero $z$), the driver adds a "risk premium" that makes $Y_t > \mathbb{E}[\xi \mid \mathcal{F}_t]$, reflecting risk aversion.
    - The specific functional form of $f(t,y,z)$ determines the nature of the risk measure: whether it is coherent, convex, or merely monetary, and what type of risk is penalized.

    The $Z_t$ component represents the sensitivity of the risk assessment to the underlying Brownian motion (hedging exposure). The driver $f$ converts this exposure into an additional risk charge.

    **The linear driver $f(t,y,z) = \mu|z|$.** This driver is:

    - Independent of $y$ (so translation invariance holds)
    - Positively homogeneous in $z$: $f(t, y, \lambda z) = \mu|\lambda z| = |\lambda| \cdot \mu|z|$ for $\lambda > 0$
    - Convex in $z$ (since $|\cdot|$ is convex)

    A driver that is positively homogeneous in $(y, z)$ (here it is independent of $y$ and homogeneous degree 1 in $z$) generates a **coherent** risk measure. The resulting BSDE risk measure is:

    $$
    \rho_t(\xi) = \operatorname{ess\,sup}_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[\xi \mid \mathcal{F}_t]
    $$

    where the set $\mathcal{Q}$ consists of measures whose Girsanov kernel $\theta_t$ satisfies $|\theta_t| \le \mu$. The parameter $\mu$ controls the degree of model uncertainty: the larger $\mu$, the wider the set of stress scenarios and the more conservative the risk assessment. This can be interpreted as a **worst-case expected loss** where the adversary can shift the drift of the Brownian motion by at most $\mu$.

---

**Exercise 2.** Show that the entropic risk measure $\rho(X) = \frac{1}{\theta}\ln\mathbb{E}[e^{-\theta X}]$ can be represented as a BSDE with quadratic driver $f(t,y,z) = \frac{\theta}{2}|z|^2$. Verify that for $\theta \to 0$, the risk measure converges to the negative expectation $\rho(X) \to -\mathbb{E}[X]$.

??? success "Solution to Exercise 2"

    **BSDE representation of the entropic risk measure.** Consider the BSDE with quadratic driver:

    $$
    -dY_t = \frac{\theta}{2}|Z_t|^2\,dt - Z_t\,dW_t, \quad Y_T = \xi
    $$

    We claim the solution is $Y_t = \frac{1}{\theta}\ln\mathbb{E}[e^{\theta\xi} \mid \mathcal{F}_t]$, which is the conditional entropic risk measure (using the loss convention where $\xi$ represents losses and $\rho_t(\xi) = \frac{1}{\theta}\ln\mathbb{E}[e^{\theta\xi} \mid \mathcal{F}_t]$; the exercise uses a gain convention with $e^{-\theta X}$ but the BSDE analysis is equivalent).

    **Verification.** Define $M_t = \mathbb{E}[e^{\theta\xi} \mid \mathcal{F}_t]$. Since $M_t$ is a martingale, by the martingale representation theorem:

    $$
    dM_t = \psi_t\,dW_t
    $$

    for some adapted process $\psi_t$. Now let $Y_t = \frac{1}{\theta}\ln M_t$. By Ito's formula:

    $$
    dY_t = \frac{1}{\theta}\frac{dM_t}{M_t} - \frac{1}{2\theta}\frac{|\psi_t|^2}{M_t^2}\,dt = \frac{\psi_t}{\theta M_t}\,dW_t - \frac{|\psi_t|^2}{2\theta M_t^2}\,dt
    $$

    Setting $Z_t = \frac{\psi_t}{\theta M_t}$, we get $|Z_t|^2 = \frac{|\psi_t|^2}{\theta^2 M_t^2}$ and:

    $$
    dY_t = Z_t\,dW_t - \frac{\theta}{2}|Z_t|^2\,dt
    $$

    Rearranging: $-dY_t = \frac{\theta}{2}|Z_t|^2\,dt - Z_t\,dW_t$, which is exactly the BSDE with driver $f(t,y,z) = \frac{\theta}{2}|z|^2$.

    The terminal condition is $Y_T = \frac{1}{\theta}\ln M_T = \frac{1}{\theta}\ln e^{\theta\xi} = \xi$. So the BSDE is satisfied.

    **Limit as $\theta \to 0$.** Using the expansion $e^{\theta\xi} \approx 1 + \theta\xi + \frac{\theta^2\xi^2}{2} + \cdots$:

    $$
    \mathbb{E}[e^{\theta\xi} \mid \mathcal{F}_t] \approx 1 + \theta\mathbb{E}[\xi \mid \mathcal{F}_t] + \frac{\theta^2}{2}\mathbb{E}[\xi^2 \mid \mathcal{F}_t] + \cdots
    $$

    Taking logarithm and dividing by $\theta$:

    $$
    Y_t = \frac{1}{\theta}\ln\mathbb{E}[e^{\theta\xi} \mid \mathcal{F}_t] \approx \frac{1}{\theta}\left(\theta\mathbb{E}[\xi \mid \mathcal{F}_t] + \frac{\theta^2}{2}\text{Var}(\xi \mid \mathcal{F}_t) + \cdots\right)
    $$

    $$
    = \mathbb{E}[\xi \mid \mathcal{F}_t] + \frac{\theta}{2}\text{Var}(\xi \mid \mathcal{F}_t) + O(\theta^2)
    $$

    As $\theta \to 0$:

    $$
    Y_t \to \mathbb{E}[\xi \mid \mathcal{F}_t]
    $$

    In the exercise's gain convention with $\rho(X) = \frac{1}{\theta}\ln\mathbb{E}[e^{-\theta X}]$, as $\theta \to 0$:

    $$
    \rho(X) \to -\mathbb{E}[X]
    $$

    which is the risk-neutral assessment (negative expected gain = expected loss). This confirms that zero risk aversion ($\theta = 0$) recovers the linear expectation, and the BSDE driver $f = \frac{\theta}{2}|z|^2 \to 0$, consistent with the conditional expectation case.

---

**Exercise 3.** Explain why BSDEs naturally produce time-consistent risk measures. Use the recursive structure: $\rho_t(X) = Y_t$ where $Y$ solves the BSDE backward from $T$ to $t$. Why does this recursion ensure that if $\rho_s(X) \le \rho_s(Y)$ at some time $s > t$, then $\rho_t(X) \le \rho_t(Y)$?

??? success "Solution to Exercise 3"

    **Why BSDEs naturally produce time-consistent risk measures.** Define $\rho_t(X) = Y_t$ where $(Y, Z)$ solves:

    $$
    Y_t = X + \int_t^T f(s, Y_s, Z_s)\,ds - \int_t^T Z_s\,dW_s
    $$

    **Step 1: The flow property.** Consider two time points $t < s < T$. The BSDE can be decomposed:

    $$
    Y_t = Y_s + \int_t^s f(u, Y_u, Z_u)\,du - \int_t^s Z_u\,dW_u
    $$

    This means $Y_t$ is obtained by solving the BSDE from $t$ to $s$ with "terminal condition" $Y_s$ at time $s$.

    **Step 2: Recursive identification.** Now consider a separate BSDE starting at time $t$ with terminal condition $\hat{\xi} = Y_s = \rho_s(X)$ at time $s$:

    $$
    \hat{Y}_t = Y_s + \int_t^s f(u, \hat{Y}_u, \hat{Z}_u)\,du - \int_t^s \hat{Z}_u\,dW_u
    $$

    By uniqueness of BSDE solutions, $\hat{Y}_u = Y_u$ for all $u \in [t, s]$. Therefore:

    $$
    \rho_t(X) = Y_t = \hat{Y}_t = \rho_t(-\rho_s(X))
    $$

    (where we identify $\rho_t(-\rho_s(X))$ as solving the BSDE on $[t,s]$ with terminal condition $\rho_s(X)$). This is precisely the recursive/tower property that defines time-consistency.

    **Step 3: Comparison theorem ensures monotonicity preservation.** If $\rho_s(X) \le \rho_s(Y)$ a.s. (the time-$s$ risk of $X$ is less than that of $Y$), then by the comparison theorem for BSDEs (which requires $f$ to be Lipschitz and increasing in $y$ under appropriate conditions):

    $$
    \rho_t(X) = Y_t^X \le Y_t^Y = \rho_t(Y) \quad \text{a.s.}
    $$

    because $Y^X$ and $Y^Y$ solve the same BSDE with ordered terminal conditions $Y_s^X \le Y_s^Y$ at time $s$, and the comparison theorem propagates this ordering backward to time $t$.

    The key insight is that BSDEs encode time-consistency through the **uniqueness of solutions and the flow property**: the solution on $[t, T]$ is uniquely determined by the terminal condition and the driver, and it can be decomposed at any intermediate time $s$ without loss of consistency.

---

**Exercise 4.** In the context of XVA (valuation adjustments), BSDEs are used to model the recursive dependence of derivative values on their own CVA. Explain why this creates a nonlinear pricing problem and how the BSDE framework handles this circularity.

??? success "Solution to Exercise 4"

    **The XVA circularity problem.** In XVA (valuation adjustments), the value $V_t$ of a derivative depends on counterparty credit risk through CVA (Credit Valuation Adjustment), DVA (Debit Valuation Adjustment), and FVA (Funding Valuation Adjustment). The key challenge is that these adjustments themselves depend on $V_t$:

    - **CVA** depends on the exposure, which depends on $V_t$
    - **FVA** depends on the funding cost, which depends on the collateral requirement, which depends on $V_t$
    - **DVA** depends on the bank's own default probability and the negative exposure, which depends on $V_t$

    This creates a **circular dependence**: $V_t$ depends on the XVA adjustments, which themselves depend on $V_t$. Mathematically:

    $$
    V_t = V_t^{\text{clean}} - \text{CVA}_t(V) + \text{DVA}_t(V) - \text{FVA}_t(V)
    $$

    where each adjustment is a functional of the value process $V$.

    **Why this is nonlinear.** In the classical (linear) pricing framework, the pricing operator is linear: the value of a portfolio is the sum of the values of its components. XVA breaks this linearity because the adjustments introduce feedback: the price depends on itself. The pricing equation becomes:

    $$
    V_t = \mathbb{E}^{\mathbb{Q}}\left[\text{Payoff}_T + \int_t^T g(s, V_s, \nabla V_s)\,ds \;\bigg|\; \mathcal{F}_t\right]
    $$

    where $g$ encodes the XVA effects and depends nonlinearly on $V_s$ (through default intensities and funding spreads).

    **How BSDEs handle the circularity.** The BSDE framework naturally accommodates this self-referential structure:

    $$
    -dV_t = g(t, V_t, Z_t)\,dt - Z_t\,dW_t, \quad V_T = \text{Payoff}
    $$

    The driver $g(t, V_t, Z_t)$ can include:

    - $-\lambda_C(t)(V_t)^+$: CVA effect (counterparty default on positive exposure)
    - $\lambda_B(t)(V_t)^-$: DVA effect (own default on negative exposure)
    - $(r_f - r)(V_t)^+$: FVA on uncollateralized positive exposure

    The BSDE framework resolves the circularity because:

    1. **Existence and uniqueness theorems** (Pardoux-Peng) guarantee that the fixed-point problem has a unique solution under Lipschitz conditions on $g$.
    2. **The backward propagation** simultaneously determines $V_t$ and the XVA adjustments at each time step, without needing to iterate to convergence.
    3. **The comparison theorem** ensures monotonicity: increasing counterparty risk (larger $\lambda_C$) increases CVA and decreases $V_t$.
    4. **Numerical schemes** (regression-based Monte Carlo, deep BSDE solvers) solve the BSDE directly, handling the nonlinearity through the conditional expectation computation at each time step.

    In essence, the BSDE turns the circular algebraic problem into a well-posed backward-in-time differential equation that can be solved systematically.

---

**Exercise 5.** The driver $f(t,y,z) = -\gamma y + \frac{\beta}{2}|z|^2$ generates a risk measure with both discounting and risk aversion. Interpret the parameters $\gamma$ (discount rate) and $\beta$ (risk aversion). What happens to the risk measure as $\beta$ increases?

??? success "Solution to Exercise 5"

    **The driver** $f(t, y, z) = -\gamma y + \frac{\beta}{2}|z|^2$ **generates the BSDE:**

    $$
    -dY_t = \left(-\gamma Y_t + \frac{\beta}{2}|Z_t|^2\right)dt - Z_t\,dW_t, \quad Y_T = \xi
    $$

    **Interpretation of $\gamma$ (discount rate).** The term $-\gamma y$ in the driver acts as a **discounting mechanism**. To see this, consider the case $\beta = 0$:

    $$
    -dY_t = -\gamma Y_t\,dt - Z_t\,dW_t
    $$

    This has the solution $Y_t = e^{-\gamma(T-t)}\mathbb{E}[\xi \mid \mathcal{F}_t]$. The risk assessment at time $t$ is the conditional expectation of the terminal loss, discounted at rate $\gamma$. Future losses are "discounted" -- they matter less the further away they are. This reflects the economic reality that a loss occurring far in the future is less concerning than one occurring soon (due to the time value of money or impatience).

    **Interpretation of $\beta$ (risk aversion).** The term $\frac{\beta}{2}|z|^2$ is a **quadratic penalty on volatility exposure**. When $\beta > 0$:

    - $Z_t$ represents the sensitivity of the risk assessment to the Brownian motion (the "hedging" component)
    - $\frac{\beta}{2}|Z_t|^2$ adds a risk premium proportional to the squared volatility exposure
    - Higher $Z_t$ (more exposure to randomness) leads to a larger risk charge

    This is analogous to the entropic risk measure, where the quadratic driver generates an exponential tilting of probabilities. The parameter $\beta$ controls how much the risk measure penalizes uncertainty:

    - $\beta = 0$: Risk-neutral (with discounting), $Y_t = e^{-\gamma(T-t)}\mathbb{E}[\xi \mid \mathcal{F}_t]$
    - Small $\beta > 0$: Mild risk aversion, approximately $Y_t \approx e^{-\gamma(T-t)}\left(\mathbb{E}[\xi \mid \mathcal{F}_t] + \frac{\beta}{2}\text{Var}(\xi \mid \mathcal{F}_t)\right)$
    - Large $\beta$: Strong risk aversion, heavy penalization of tail outcomes

    **Effect of increasing $\beta$.** As $\beta$ increases:

    1. The risk measure $\rho_t(\xi) = Y_t$ becomes more conservative (larger values for the same $\xi$).
    2. The dual representation shifts: the penalty function $\alpha(\mathbb{Q})$ in $\rho_t = \sup_{\mathbb{Q}}\{\mathbb{E}^{\mathbb{Q}}[\xi \mid \mathcal{F}_t] - \alpha_t(\mathbb{Q})\}$ decreases, allowing more extreme probability measures to contribute to the supremum.
    3. In the limit $\beta \to \infty$, the risk measure approaches the worst-case assessment (essential supremum), which penalizes volatility exposure infinitely.
    4. The connection to exponential utility: $\beta$ plays the role of the Arrow-Pratt absolute risk aversion coefficient, and $Y_t$ relates to the certainty equivalent under the utility $U(w) = -e^{-\beta w}$ (with additional discounting at rate $\gamma$).

    The combined effect of $\gamma$ and $\beta$ is: future uncertain losses are first penalized for their randomness (via $\beta$) and then discounted for their time distance (via $\gamma$).

---

**Exercise 6.** Compare BSDE-based risk measures with the backward recursion approach using conditional risk measures $\rho_t(X) = \rho_t(\rho_{t+1}(X))$. Explain how BSDEs provide the continuous-time limit of this discrete recursion. What regularity conditions on the driver $f$ ensure existence and uniqueness of the BSDE solution?

??? success "Solution to Exercise 6"

    **Discrete backward recursion.** In discrete time with periods $t = 0, 1, \ldots, N$ (where $t_k = kh$ with $h = T/N$), a time-consistent dynamic risk measure is defined by:

    $$
    \rho_N(X) = X, \quad \rho_k(X) = \rho_{k,k+1}(-\rho_{k+1}(X))
    $$

    where $\rho_{k,k+1}$ is a one-step conditional risk measure from period $k$ to $k+1$.

    **BSDE as continuous-time limit.** The time-discretized BSDE is:

    $$
    Y_{t_k} = \mathbb{E}[Y_{t_{k+1}} + f(t_k, Y_{t_{k+1}}, Z_{t_k})\,h \mid \mathcal{F}_{t_k}]
    $$

    where $Z_{t_k} \approx \frac{1}{h}\mathbb{E}[Y_{t_{k+1}} \Delta W_k \mid \mathcal{F}_{t_k}]$ and $\Delta W_k = W_{t_{k+1}} - W_{t_k}$.

    This is a backward recursion: given $Y_{t_{k+1}}$ (the risk assessment at the next period), compute $Y_{t_k}$ by:

    1. Adding the driver term $f \cdot h$ (the one-period risk charge)
    2. Taking the conditional expectation (propagating backward)

    The one-step risk measure is implicitly:

    $$
    \rho_{k,k+1}(L) = \mathbb{E}[L + f(t_k, L, Z_{t_k})\,h \mid \mathcal{F}_{t_k}]
    $$

    As $h \to 0$ (i.e., $N \to \infty$), the discrete recursion converges to the continuous BSDE:

    $$
    Y_t = \xi + \int_t^T f(s, Y_s, Z_s)\,ds - \int_t^T Z_s\,dW_s
    $$

    **Comparison of the two approaches:**

    | Aspect | Discrete recursion | BSDE |
    |--------|-------------------|------|
    | Time structure | Finite periods $0, 1, \ldots, N$ | Continuous $[0, T]$ |
    | Risk assessment | $\rho_k \in L^\infty(\mathcal{F}_{t_k})$ | $Y_t$ adapted process |
    | One-step operator | $\rho_{k,k+1}$ (explicit choice) | Driver $f(t,y,z)$ |
    | Time-consistency | By recursive construction | Automatic from BSDE structure |
    | Hedging information | Not directly available | $Z_t$ gives hedging strategy |
    | Analytical tractability | Depends on $\rho_{k,k+1}$ | PDE connection via Feynman-Kac |

    A key advantage of the BSDE formulation is that the process $Z_t$ provides the **hedging (control) strategy** as a byproduct of solving the BSDE, which is not directly available in the discrete setting.

    **Regularity conditions for existence and uniqueness.** The Pardoux-Peng (1990) theorem guarantees existence and uniqueness of adapted solutions $(Y, Z) \in \mathcal{S}^2 \times \mathcal{H}^2$ under the following conditions on the driver $f: [0,T] \times \Omega \times \mathbb{R} \times \mathbb{R}^d \to \mathbb{R}$:

    1. **Lipschitz continuity in $(y, z)$:** There exists $K > 0$ such that for all $t, \omega, y_1, y_2, z_1, z_2$:

    $$
    |f(t, y_1, z_1) - f(t, y_2, z_2)| \le K(|y_1 - y_2| + |z_1 - z_2|)
    $$

    2. **Square-integrability:** $\mathbb{E}\left[\int_0^T |f(t, 0, 0)|^2\,dt\right] < \infty$.

    3. **Terminal condition:** $\xi \in L^2(\mathcal{F}_T)$.

    4. **Progressively measurable:** $f(t, y, z)$ is progressively measurable for each $(y, z)$.

    Under these conditions, the BSDE has a unique adapted solution $(Y, Z)$ with $Y \in \mathcal{S}^2$ (continuous, square-integrable supremum) and $Z \in \mathcal{H}^2$ (square-integrable).

    **Beyond Lipschitz:** For quadratic BSDEs (where $f$ has quadratic growth in $z$, as in the entropic risk measure), the standard theory breaks down. Existence and uniqueness require:

    - Bounded terminal condition: $\xi \in L^\infty$
    - Quadratic growth: $|f(t,y,z)| \le C(1 + |y| + |z|^2)$
    - Additional structural conditions (convexity/concavity of $f$ in $z$)

    The theory of quadratic BSDEs (Kobylanski 2000, Briand-Hu 2006) provides existence and uniqueness under these modified conditions, using BMO martingale techniques.
