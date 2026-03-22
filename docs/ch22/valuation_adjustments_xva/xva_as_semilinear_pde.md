# XVA as Semilinear PDE

The unified mathematical framework for XVA pricing rests on **backward stochastic differential equations (BSDEs)**, which through the nonlinear Feynman-Kac formula yield **semilinear partial differential equations**. This connection transforms the multi-component XVA problem into a single nonlinear pricing equation that consistently handles interactions among CVA, DVA, FVA, and other adjustments.

---

## From Linear to Nonlinear Pricing

### Classical Linear Case

Under standard Black-Scholes assumptions, the derivative price $V(t, x)$ satisfies the linear PDE:

$$
\partial_t V + \frac{1}{2}\sigma^2 x^2 \partial_{xx} V + r x \partial_x V - rV = 0
$$

with terminal condition $V(T, x) = \Phi(x)$. The corresponding **linear BSDE** is:

$$
V_t = \Phi(X_T) + \int_t^T r V_s \, ds - \int_t^T Z_s \, dW_s
$$

with driver $f(t, V, Z) = -rV$ (linear in $V$, independent of $Z$).

### XVA Breaks Linearity

When accounting for counterparty risk, funding costs, and collateral effects, the driver becomes **nonlinear**:

$$
f(t, V, Z) = -rV + \underbrace{\lambda_C \cdot \text{LGD}_C \cdot V^+}_{\text{CVA}} - \underbrace{\lambda_B \cdot \text{LGD}_B \cdot V^-}_{\text{DVA}} + \underbrace{s_F (V - C)^+}_{\text{FVA}} - \underbrace{s_L (V - C)^-}_{\text{FBA}}
$$

The terms $V^+ = \max(V, 0)$ and $V^- = \max(-V, 0)$ introduce nonlinearity, breaking the classical linear pricing framework.

---

## BSDE Formulation of XVA

### The XVA BSDE

Consider a derivative with payoff $\xi$ at maturity $T$, on an underlying driven by:

$$
dX_t = \mu(t, X_t) \, dt + \sigma(t, X_t) \, dW_t
$$

The XVA-adjusted price $V_t$ satisfies the BSDE:

$$
V_t = \xi + \int_t^T f(s, X_s, V_s, Z_s) \, ds - \int_t^T Z_s \, dW_s
$$

where $Z_t = \sigma(t, X_t) \partial_x V(t, X_t)$ is the hedging portfolio sensitivity.

### Full XVA Driver

The driver incorporating all adjustments is:

$$
f(t, x, v, z) = -r(t)v + f_{\text{CVA}}(v) + f_{\text{DVA}}(v) + f_{\text{FVA}}(v, c) + f_{\text{MVA}}(t, v, z)
$$

with components:

**CVA component:** $f_{\text{CVA}}(v) = \lambda_C(t) \cdot \text{LGD}_C \cdot v^+$

**DVA component:** $f_{\text{DVA}}(v) = -\lambda_B(t) \cdot \text{LGD}_B \cdot v^-$

**FVA component (asymmetric):** $f_{\text{FVA}}(v, c) = s_F^+(t)(v - c)^+ - s_F^-(t)(v - c)^-$

**MVA component:** $f_{\text{MVA}}(t, v, z) = s_F(t) \cdot \text{IM}(t, v, z)$

where $\lambda_C, \lambda_B$ are default intensities, $c$ is collateral, and IM depends on sensitivities (related to $z$).

---

## The Nonlinear Feynman-Kac Formula

### Statement

!!! info "Theorem (Nonlinear Feynman-Kac)"
    If $(V_t, Z_t)$ solves the BSDE with driver $f$, and if $u(t, x)$ is a smooth solution to the semilinear PDE:

    $$
    \partial_t u + \mathcal{L} u + f(t, x, u, \sigma^\top \nabla u) = 0
    $$

    with terminal condition $u(T, x) = \Phi(x)$, where $\mathcal{L}$ is the generator of $X_t$:

    $$
    \mathcal{L} u = \mu(t, x) \cdot \nabla u + \frac{1}{2} \text{tr}[\sigma \sigma^\top(t, x) \nabla^2 u]
    $$

    then $V_t = u(t, X_t)$ and $Z_t = \sigma^\top(t, X_t) \nabla u(t, X_t)$.

This is the nonlinear extension of the classical Feynman-Kac formula. In the linear case ($f = -ru$), it reduces to the standard connection between the heat equation and conditional expectations.

### The XVA Semilinear PDE

Substituting the XVA driver, the pricing PDE becomes:

$$
\partial_t u + \mathcal{L} u - r u + \lambda_C \cdot \text{LGD}_C \cdot u^+ - \lambda_B \cdot \text{LGD}_B \cdot u^- + s_F^+(u - c)^+ - s_F^-(u - c)^- = 0
$$

with $u(T, x) = \Phi(x)$.

**Structure:** This is a **semilinear PDE** -- linear in the highest-order derivatives (through $\mathcal{L}u$) but nonlinear in $u$ (through the $u^+$, $u^-$, $(u-c)^+$, $(u-c)^-$ terms).

---

## Decomposition into Risk-Free Price and XVA

### Additive Decomposition

Write $u = \hat{u} + \theta$, where $\hat{u}$ solves the risk-free PDE:

$$
\partial_t \hat{u} + \mathcal{L}\hat{u} - r\hat{u} = 0, \quad \hat{u}(T, x) = \Phi(x)
$$

Then the XVA correction $\theta$ satisfies:

$$
\partial_t \theta + \mathcal{L}\theta - r\theta + g(t, x, \hat{u} + \theta) = 0, \quad \theta(T, x) = 0
$$

where $g$ contains all the nonlinear XVA terms evaluated at $u = \hat{u} + \theta$.

### First-Order Approximation

For small XVA corrections ($|\theta| \ll |\hat{u}|$), approximate $u \approx \hat{u}$ in the nonlinear terms:

$$
\partial_t \theta + \mathcal{L}\theta - r\theta + g(t, x, \hat{u}) \approx 0
$$

This yields a **linear PDE for $\theta$** with a source term $g(t, x, \hat{u})$ that depends on the known risk-free price. The corresponding integral representation is:

$$
\theta(t, x) = \mathbb{E}\left[\int_t^T e^{-r(s-t)} g(s, X_s, \hat{u}(s, X_s)) \, ds \,\middle|\, X_t = x\right]
$$

This recovers the standard additive XVA formulas:

$$
\text{CVA} \approx \mathbb{E}\left[\int_t^T e^{-r(s-t)} \lambda_C \cdot \text{LGD}_C \cdot \hat{u}^+(s, X_s) \, ds\right]
$$

The full nonlinear solution captures XVA interactions that the additive approximation misses.

---

## Existence and Uniqueness

### Pardoux-Peng Theory

The foundational result of Pardoux and Peng (1990) establishes:

!!! info "Theorem (Existence and Uniqueness)"
    If the driver $f(t, x, v, z)$ satisfies:

    1. **Lipschitz condition in $(v, z)$:** There exists $K > 0$ such that

    $$
    |f(t, x, v_1, z_1) - f(t, x, v_2, z_2)| \le K(|v_1 - v_2| + |z_1 - z_2|)
    $$

    2. **Square integrability:** $\mathbb{E}\left[\int_0^T |f(t, X_t, 0, 0)|^2 \, dt\right] < \infty$

    3. **Terminal condition:** $\xi \in L^2(\mathcal{F}_T)$

    then the BSDE has a unique adapted solution $(V_t, Z_t) \in \mathcal{S}^2 \times \mathcal{H}^2$.

### Verification for XVA Driver

The XVA driver components are Lipschitz:

- $v \mapsto v^+$ and $v \mapsto v^-$ are Lipschitz with constant 1
- $v \mapsto (v - c)^+$ and $v \mapsto (v - c)^-$ are Lipschitz with constant 1
- Linear terms ($-rv$) are Lipschitz with constant $|r|$

Therefore the XVA BSDE (without MVA's $z$-dependence) satisfies the Pardoux-Peng conditions with:

$$
K = r + \lambda_C \cdot \text{LGD}_C + \lambda_B \cdot \text{LGD}_B + s_F^+ + s_F^-
$$

The MVA term introduces $z$-dependence through $\text{IM}(t, v, z)$, which can violate standard Lipschitz conditions and may require regularization.

---

## Comparison Theorem and Monotonicity

### Comparison Theorem

!!! info "Theorem (Comparison)"
    If $f_1(t, v, z) \le f_2(t, v, z)$ for all $(t, v, z)$, and $\xi_1 \le \xi_2$ a.s., then the BSDE solutions satisfy:

    $$
    V_t^1 \le V_t^2 \quad \text{a.s. for all } t \in [0, T]
    $$

**Application to XVA:** The comparison theorem implies:

- **Monotonicity in credit spreads:** Higher counterparty default intensity $\lambda_C$ increases the CVA component, reducing the adjusted price for the surviving party
- **Monotonicity in funding costs:** Higher funding spread $s_F$ increases FVA, reducing the price
- **Bounds:** The risk-free price $\hat{u}$ provides an upper bound for the XVA-adjusted price when all adjustment terms are non-negative costs

---

## Recursive XVA Computation

### Time-Stepping Scheme

The BSDE is solved backward in time. Discretize $[0, T]$ into steps $0 = t_0 < t_1 < \cdots < t_N = T$ with $\Delta t = T/N$:

$$
V_{t_i} = \mathbb{E}\left[V_{t_{i+1}} \,|\, \mathcal{F}_{t_i}\right] + f(t_i, X_{t_i}, V_{t_i}, Z_{t_i}) \cdot \Delta t
$$

$$
Z_{t_i} = \frac{1}{\Delta t} \mathbb{E}\left[V_{t_{i+1}} \cdot \Delta W_{t_i} \,|\, \mathcal{F}_{t_i}\right]
$$

### Branching Diffusion Method

The branching diffusion approach (Henry-Labordere, 2012) avoids nested Monte Carlo by representing the nonlinear PDE solution as an expectation over branching particle systems:

$$
u(t, x) = \mathbb{E}\left[\prod_{k \in \text{leaves}} \Phi(X_T^{(k)}) \cdot \prod_{j \in \text{branch points}} w_j\right]
$$

where particles branch at random times corresponding to the nonlinear terms in the driver.

### Deep BSDE Method

Neural networks approximate the solution and control processes:

1. Parameterize $V_{t_0} \approx \mathcal{N}_\theta(\mathbf{x}_0)$ and $Z_{t_i} \approx \mathcal{N}_\phi^{(i)}(\mathbf{X}_{t_i})$
2. Forward simulate using the Euler scheme
3. Minimize the terminal loss:

$$
\min_{\theta, \phi} \mathbb{E}\left[\left|V_{t_N}^{\theta, \phi} - \Phi(X_T)\right|^2\right]
$$

This approach scales to high dimensions, making it feasible for realistic multi-asset XVA problems.

---

## Connection to Dynamic Risk Measures

The XVA BSDE is a special case of the $g$-expectation framework (Peng, 1997):

$$
\mathcal{E}_g[X \mid \mathcal{F}_t] := Y_t
$$

where $Y_t$ solves $Y_t = X + \int_t^T g(s, Y_s, Z_s) \, ds - \int_t^T Z_s \, dW_s$.

**Correspondence:**

| XVA pricing | Dynamic risk measures |
|-------------|----------------------|
| Driver $f$ includes CVA, FVA | Driver $g$ encodes risk preferences |
| Nonlinear pricing rule | Nonlinear expectation |
| Comparison theorem | Monotonicity axiom |
| $f = 0$: risk-free pricing | $g = 0$: conditional expectation |
| Convex $f$: convex pricing | Convex $g$: convex risk measure |

The XVA pricing rule is therefore a **nonlinear conditional expectation** that incorporates credit, funding, and capital costs as "risk preferences."

---

## Numerical Challenges

### Curse of Dimensionality

Realistic XVA problems involve many risk factors (interest rates across currencies, credit spreads, FX rates, equity prices). The semilinear PDE lives in high-dimensional space, making grid-based methods infeasible beyond 3--4 dimensions.

### Nonlinearity and Iterations

The terms $u^+$ and $(u - c)^+$ are non-smooth at $u = 0$ and $u = c$, requiring:

- **Regularization:** Replace $u^+ \approx u \cdot \Phi(u/\epsilon)$ for small $\epsilon$
- **Policy iteration:** Solve a sequence of linear PDEs, updating the nonlinear region at each step
- **Picard iteration:** Iterate the BSDE solution, using the previous iterate in the nonlinear terms

### Nested Simulation

Computing $\text{EE}(t) = \mathbb{E}[V_t^+]$ at each future time point on each Monte Carlo path requires pricing the portfolio conditional on the simulated state -- a **simulation within simulation** problem that is prohibitively expensive without regression-based approximations (Longstaff-Schwartz, kernel methods, or neural networks).

---

## Example: One-Dimensional XVA PDE

Consider a single-asset derivative with GBM dynamics $dX_t = rX_t \, dt + \sigma X_t \, dW_t$, constant default intensities $\lambda_C, \lambda_B$, and symmetric funding spread $s_F$.

The XVA PDE is:

$$
\partial_t u + \frac{1}{2}\sigma^2 x^2 \partial_{xx} u + rx \partial_x u - ru + \lambda_C \cdot \text{LGD}_C \cdot u^+ - \lambda_B \cdot \text{LGD}_B \cdot u^- + s_F \cdot u^+ = 0
$$

**Simplification for positive derivative ($u > 0$):**

$$
\partial_t u + \frac{1}{2}\sigma^2 x^2 \partial_{xx} u + rx \partial_x u - (r - \lambda_C \cdot \text{LGD}_C - s_F)u = 0
$$

This is a linear PDE with an **adjusted discount rate** $\tilde{r} = r - \lambda_C \cdot \text{LGD}_C - s_F$, showing that CVA and FVA effectively increase the discounting when the derivative has positive value.

**For negative derivative ($u < 0$):**

$$
\partial_t u + \frac{1}{2}\sigma^2 x^2 \partial_{xx} u + rx \partial_x u - (r + \lambda_B \cdot \text{LGD}_B)u = 0
$$

The DVA term reduces discounting (a benefit from own credit risk).

The full solution requires matching these two regimes at $u = 0$, creating a **free boundary** problem.

---

## Key Takeaways

- XVA pricing is naturally formulated as a BSDE with a nonlinear driver incorporating credit, funding, and capital costs
- The nonlinear Feynman-Kac formula connects the BSDE to a semilinear PDE, extending the classical Black-Scholes PDE
- Existence and uniqueness follow from Pardoux-Peng theory under Lipschitz conditions on the driver
- The comparison theorem ensures monotonicity of XVA-adjusted prices in credit spreads and funding costs
- For small adjustments, the first-order approximation recovers standard additive XVA formulas
- The full nonlinear solution captures XVA interactions missed by the additive approach
- Numerical methods (deep BSDE, branching diffusion, regression-based) address the curse of dimensionality

---

## Further Reading

- Burgard, C. & Kjaer, M. (2011), "Partial Differential Equation Representations of Derivatives with Bilateral Counterparty Risk and Funding Costs"
- Crépey, S. (2015), "Bilateral Counterparty Risk Under Funding Constraints," *Mathematical Finance*
- Pardoux, E. & Peng, S. (1990), "Adapted Solution of a Backward Stochastic Differential Equation"
- Henry-Labordere, P. (2012), "Counterparty Risk Valuation: A Marked Branching Diffusion Approach"
- E, W., Han, J., & Jentzen, A. (2017), "Deep Learning-Based Numerical Methods for High-Dimensional Parabolic PDEs and BSDEs"
- Peng, S. (1997), "Backward SDE and Related $g$-Expectations"
