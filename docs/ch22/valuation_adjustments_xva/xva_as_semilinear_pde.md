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

Recall the (linear) Feynman-Kac formula (see [§ Feynman-Kac](../../ch05/feynman_kac/discounted_feynman_kac.md)). Its nonlinear extension states: if $(V_t, Z_t)$ solves the BSDE with driver $f$ and $u(t,x)$ solves

$$
\partial_t u + \mathcal{L} u + f(t, x, u, \sigma^\top \nabla u) = 0, \qquad u(T, x) = \Phi(x),
$$

with $\mathcal{L} u = \mu \cdot \nabla u + \tfrac{1}{2} \text{tr}[\sigma \sigma^\top \nabla^2 u]$, then $V_t = u(t, X_t)$ and $Z_t = \sigma^\top(t, X_t) \nabla u(t, X_t)$. The linear case $f = -ru$ recovers classical Feynman-Kac.

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

Recall Pardoux-Peng BSDE existence/uniqueness (see [§ Second-order BSDEs](../../ch23/second_order_bsdes_and_nonlinear_expectations/2bsdes.md)). The XVA driver pieces $v^+, v^-, (v-c)^\pm$ are each 1-Lipschitz, giving Lipschitz constant

$$
K = r + \lambda_C \cdot \text{LGD}_C + \lambda_B \cdot \text{LGD}_B + s_F^+ + s_F^-
$$

so the standard XVA BSDE (without the $Z$-dependent MVA term) admits a unique solution $(V, Z) \in \mathcal{S}^2 \times \mathcal{H}^2$.

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

Recall $g$-expectations / nonlinear conditional expectations (see [§ Dynamic Risk Measures](../dynamic_risk_measures/bsde_based_risk_measures.md)). The XVA BSDE is a $g$-expectation with driver $f$ encoding CVA, DVA, FVA, MVA; comparison theorem $\Leftrightarrow$ monotonicity, convex $f$ $\Leftrightarrow$ convex risk measure.

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

---

## Exercises

**Exercise 1.** Starting from the XVA semilinear PDE

$$
\partial_t u + \frac{1}{2}\sigma^2 x^2 \partial_{xx} u + rx \partial_x u - ru + \lambda_C \cdot \text{LGD}_C \cdot u^+ - \lambda_B \cdot \text{LGD}_B \cdot u^- + s_F \cdot u^+ = 0
$$

show that when $u > 0$ everywhere, the PDE reduces to a standard Black-Scholes equation with an adjusted discount rate $\tilde{r} = r - \lambda_C \cdot \text{LGD}_C - s_F$. Compute $\tilde{r}$ for $r = 3\%$, $\lambda_C = 2\%$, $\text{LGD}_C = 60\%$, $s_F = 80$ bps. Explain why $\tilde{r} < r$ and what this means economically for the price of a call option.

??? success "Solution to Exercise 1"
    **Showing the PDE reduces to Black-Scholes with adjusted discount rate.**

    Starting from the XVA semilinear PDE:

    $$
    \partial_t u + \frac{1}{2}\sigma^2 x^2 \partial_{xx} u + rx \partial_x u - ru + \lambda_C \cdot \text{LGD}_C \cdot u^+ - \lambda_B \cdot \text{LGD}_B \cdot u^- + s_F \cdot u^+ = 0
    $$

    When $u > 0$ everywhere, we have $u^+ = u$ and $u^- = 0$. Substituting:

    $$
    \partial_t u + \frac{1}{2}\sigma^2 x^2 \partial_{xx} u + rx \partial_x u - ru + \lambda_C \cdot \text{LGD}_C \cdot u - 0 + s_F \cdot u = 0
    $$

    Collecting the terms involving $u$:

    $$
    \partial_t u + \frac{1}{2}\sigma^2 x^2 \partial_{xx} u + rx \partial_x u - (r - \lambda_C \cdot \text{LGD}_C - s_F) u = 0
    $$

    This is a standard Black-Scholes PDE with the adjusted discount rate:

    $$
    \tilde{r} = r - \lambda_C \cdot \text{LGD}_C - s_F
    $$

    **Numerical computation.**

    With $r = 3\% = 0.03$, $\lambda_C = 2\% = 0.02$, $\text{LGD}_C = 60\% = 0.60$, $s_F = 80$ bps $= 0.008$:

    $$
    \tilde{r} = 0.03 - 0.02 \times 0.60 - 0.008 = 0.03 - 0.012 - 0.008 = 0.01 = 1\%
    $$

    **Economic interpretation.**

    The adjusted rate $\tilde{r} = 1\% < r = 3\%$ reflects that the effective discounting is *reduced* when the derivative has positive value. This is because:

    1. **CVA effect** ($-\lambda_C \cdot \text{LGD}_C = -1.2\%$): A positive derivative value represents exposure to the counterparty. The counterparty may default, so the expected cash flow is reduced. This acts like *additional* discounting -- future positive cash flows are worth less because of counterparty credit risk.

    2. **FVA effect** ($-s_F = -0.8\%$): A positive derivative value must be funded by the bank at a cost of $s_F$ above risk-free. This funding cost also acts like additional discounting.

    **Impact on call option price.** Since a call option always has $u \ge 0$ (before maturity, the call value is strictly positive for $x > 0$), the call price under XVA is the Black-Scholes price computed with discount rate $\tilde{r} = 1\%$ instead of $r = 3\%$. Counterintuitively, the *lower* discount rate means the call is priced *higher* in the risk-free-price sense, but this is offset by the fact that $\tilde{r}$ represents a *net* rate after accounting for losses. More precisely, the call price with discount rate $\tilde{r}$ using the standard Black-Scholes formula gives a *lower* present value of the payoff (the drift of the underlying under the risk-neutral measure is $\tilde{r}$, which is lower, reducing the expected terminal stock price). The net effect is that the XVA-adjusted call option is worth less than the risk-free Black-Scholes price.

---

**Exercise 2.** Verify that the XVA driver $f(t, v, z) = -rv + \lambda_C \cdot \text{LGD}_C \cdot v^+ - \lambda_B \cdot \text{LGD}_B \cdot v^- + s_F(v - c)^+$ satisfies the Lipschitz condition. Compute the Lipschitz constant $K$ in terms of $r$, $\lambda_C$, $\text{LGD}_C$, $\lambda_B$, $\text{LGD}_B$, and $s_F$. Using the Pardoux-Peng existence theorem, state what this guarantees about the BSDE solution.

??? success "Solution to Exercise 2"
    **Verifying the Lipschitz condition.**

    We need to show that for all $v_1, v_2, z_1, z_2$:

    $$
    |f(t, v_1, z_1) - f(t, v_2, z_2)| \le K(|v_1 - v_2| + |z_1 - z_2|)
    $$

    The driver is:

    $$
    f(t, v, z) = -rv + \lambda_C \cdot \text{LGD}_C \cdot v^+ - \lambda_B \cdot \text{LGD}_B \cdot v^- + s_F(v - c)^+
    $$

    Since $f$ does not depend on $z$ (excluding the MVA term), we only need to check the Lipschitz condition in $v$.

    **Term-by-term analysis:**

    1. $|-rv_1 - (-rv_2)| = r|v_1 - v_2|$: Lipschitz with constant $r$.

    2. $|\lambda_C \cdot \text{LGD}_C \cdot v_1^+ - \lambda_C \cdot \text{LGD}_C \cdot v_2^+| \le \lambda_C \cdot \text{LGD}_C \cdot |v_1 - v_2|$: This uses the fact that the positive-part function satisfies $|a^+ - b^+| \le |a - b|$ for all $a, b \in \mathbb{R}$.

        *Proof:* Without loss of generality, assume $a \ge b$. If both are positive, $|a^+ - b^+| = |a - b|$. If both are negative, $|a^+ - b^+| = 0 \le |a - b|$. If $a \ge 0 > b$, then $|a^+ - b^+| = a \le a - b = |a - b|$. In all cases, $|a^+ - b^+| \le |a - b|$.

    3. $|\lambda_B \cdot \text{LGD}_B \cdot v_1^- - \lambda_B \cdot \text{LGD}_B \cdot v_2^-| \le \lambda_B \cdot \text{LGD}_B \cdot |v_1 - v_2|$: Same argument as above, since $v^- = (-v)^+$.

    4. $|s_F(v_1 - c)^+ - s_F(v_2 - c)^+| \le s_F \cdot |(v_1 - c) - (v_2 - c)| = s_F \cdot |v_1 - v_2|$: Again by the Lipschitz property of the positive part.

    **Triangle inequality gives:**

    $$
    |f(t, v_1, z) - f(t, v_2, z)| \le (r + \lambda_C \cdot \text{LGD}_C + \lambda_B \cdot \text{LGD}_B + s_F) \cdot |v_1 - v_2|
    $$

    Since $f$ is independent of $z$:

    $$
    |f(t, v_1, z_1) - f(t, v_2, z_2)| \le K \cdot (|v_1 - v_2| + |z_1 - z_2|)
    $$

    with the **Lipschitz constant:**

    $$
    K = r + \lambda_C \cdot \text{LGD}_C + \lambda_B \cdot \text{LGD}_B + s_F
    $$

    (The $z$-Lipschitz constant is 0 since $f$ does not depend on $z$, but the bound trivially holds.)

    **Pardoux-Peng guarantee.**

    The Pardoux-Peng existence and uniqueness theorem guarantees that the BSDE:

    $$
    V_t = \xi + \int_t^T f(s, X_s, V_s, Z_s) \, ds - \int_t^T Z_s \, dW_s
    $$

    has a **unique adapted solution** $(V_t, Z_t) \in \mathcal{S}^2 \times \mathcal{H}^2$, where:

    - $\mathcal{S}^2$ is the space of continuous adapted processes with $\mathbb{E}[\sup_{t \le T} |V_t|^2] < \infty$
    - $\mathcal{H}^2$ is the space of progressively measurable processes with $\mathbb{E}[\int_0^T |Z_t|^2 \, dt] < \infty$

    This means the XVA-adjusted price exists, is unique, and is well-behaved (square-integrable), provided the terminal payoff $\xi$ is in $L^2$ and the driver coefficients ($r$, $\lambda_C$, $\lambda_B$, $s_F$) are bounded.

---

**Exercise 3.** Consider the first-order (additive) approximation where $u \approx \hat{u}$ in the nonlinear terms:

$$
\text{CVA} \approx \mathbb{E}\left[\int_t^T e^{-r(s-t)} \lambda_C \cdot \text{LGD}_C \cdot \hat{u}^+(s, X_s) \, ds\right]
$$

Explain why this approximation is valid when XVA adjustments are small relative to the risk-free price. For a derivative with $\hat{u} = \$10$M and total XVA = \$0.5M, assess whether the approximation is reasonable. What interactions does the additive approach miss that the full nonlinear solution captures?

??? success "Solution to Exercise 3"
    **Why the first-order approximation is valid for small XVA.**

    Write $u = \hat{u} + \theta$, where $\hat{u}$ is the risk-free price and $\theta$ is the XVA correction. The exact XVA equation involves nonlinear terms evaluated at $u = \hat{u} + \theta$:

    $$
    \text{CVA} = \mathbb{E}\left[\int_t^T e^{-r(s-t)} \lambda_C \cdot \text{LGD}_C \cdot (\hat{u} + \theta)^+ \, ds\right]
    $$

    The first-order approximation replaces $(\hat{u} + \theta)^+$ with $\hat{u}^+$. This is valid when $|\theta| \ll |\hat{u}|$ because:

    1. Where $\hat{u} \gg 0$ (deep in-the-money): $(\hat{u} + \theta)^+ = \hat{u} + \theta \approx \hat{u}^+ + \theta$. The correction $\theta$ shifts the exposure slightly but doesn't change the region where $u > 0$.

    2. Where $\hat{u} \ll 0$ (deep out-of-the-money): $(\hat{u} + \theta)^+ = 0 = \hat{u}^+$. Both are zero, so the approximation is exact.

    3. The approximation fails only near $\hat{u} \approx 0$ (at-the-money), where small $\theta$ can change the sign of $u$. If $\theta$ is small, this region has small measure, and the error is bounded by $O(\theta^2)$.

    **Assessment for the given numbers.**

    With $\hat{u} = \$10$M and total XVA $= \$0.5$M:

    $$
    \frac{|\theta|}{|\hat{u}|} = \frac{0.5}{10} = 5\%
    $$

    A 5% correction is reasonably small. The first-order approximation introduces an error of approximately $O(\theta^2 / \hat{u}) \approx O(0.025\text{M}) = O(\$25{,}000)$, which is about 5% of the XVA itself. For many practical purposes, this accuracy is acceptable, but for precise pricing or when the derivative can change sign (e.g., a swap near maturity), the full nonlinear solution may be needed.

    **Interactions missed by the additive approach.**

    The additive approximation computes each XVA component using the risk-free price $\hat{u}$:

    $$
    \text{CVA} \approx F[\hat{u}^+], \quad \text{DVA} \approx G[\hat{u}^-], \quad \text{FVA} \approx H[\hat{u}]
    $$

    The full nonlinear solution captures:

    1. **CVA-FVA interaction:** CVA reduces the price, which changes the exposure profile, which in turn affects FVA. In the additive approach, FVA is computed using $\hat{u}$ (ignoring that CVA has already reduced the price).

    2. **DVA-FVA overlap:** Both DVA and FVA depend on the bank's credit. The full nonlinear framework avoids double-counting by deriving both from the same self-financing equation.

    3. **Feedback effects:** The XVA correction $\theta$ changes the sign of $u$ in some scenarios (e.g., a near-the-money swap may flip from positive to negative once CVA is included). This changes which XVA components are active, creating a feedback loop that the additive approach misses entirely.

    4. **Nonlinear netting:** Under netting, adding CVA to one trade affects the net exposure for all trades with the same counterparty, changing the CVA of the entire portfolio.

---

**Exercise 4.** The comparison theorem states that if $f_1 \le f_2$ and $\xi_1 \le \xi_2$, then $V^1_t \le V^2_t$. Use this to prove that higher counterparty credit spread (higher $\lambda_C$) reduces the XVA-adjusted price for a derivative with positive value. Specifically, if $\lambda_C^{(1)} < \lambda_C^{(2)}$, show that $f^{(1)} \ge f^{(2)}$ for $v > 0$ and therefore $V^{(1)}_t \ge V^{(2)}_t$.

??? success "Solution to Exercise 4"
    **Setting up the comparison.**

    Consider two BSDE problems with drivers $f^{(1)}$ and $f^{(2)}$ that differ only in the counterparty default intensity: $\lambda_C^{(1)} < \lambda_C^{(2)}$, with the same terminal condition $\xi$.

    The drivers are:

    $$
    f^{(i)}(t, v, z) = -rv + \lambda_C^{(i)} \cdot \text{LGD}_C \cdot v^+ - \lambda_B \cdot \text{LGD}_B \cdot v^- + s_F(v - c)^+
    $$

    **Showing $f^{(1)} \ge f^{(2)}$ for $v > 0$.**

    For $v > 0$:

    $$
    f^{(i)}(t, v, z) = -rv + \lambda_C^{(i)} \cdot \text{LGD}_C \cdot v + s_F(v - c)^+
    $$

    (since $v^+ = v$ and $v^- = 0$).

    Wait -- we must be careful with the sign convention. In the BSDE:

    $$
    V_t = \xi + \int_t^T f(s, V_s, Z_s) \, ds - \int_t^T Z_s \, dW_s
    $$

    The driver $f$ includes $+\lambda_C \cdot \text{LGD}_C \cdot v^+$, which is a *positive* contribution to the integral for $v > 0$. However, economically, CVA is a *cost* that reduces the value. The resolution is that the positive sign in the driver means the BSDE solution is adjusted *downward* compared to the risk-free case.

    Let us verify the comparison directly. For $v > 0$:

    $$
    f^{(1)} - f^{(2)} = (\lambda_C^{(1)} - \lambda_C^{(2)}) \cdot \text{LGD}_C \cdot v
    $$

    Since $\lambda_C^{(1)} < \lambda_C^{(2)}$ and $v > 0$:

    $$
    f^{(1)} - f^{(2)} = (\lambda_C^{(1)} - \lambda_C^{(2)}) \cdot \text{LGD}_C \cdot v < 0
    $$

    So $f^{(1)} < f^{(2)}$ for $v > 0$. By the comparison theorem, since $f^{(1)} \le f^{(2)}$ and $\xi_1 = \xi_2$:

    $$
    V_t^{(1)} \le V_t^{(2)}
    $$

    This seems to say that lower $\lambda_C$ gives a *lower* price, which is counterintuitive. Let us reconsider the convention.

    The XVA PDE as written has $+\lambda_C \cdot \text{LGD}_C \cdot u^+$, and in the region $u > 0$, the effective discount rate is $\tilde{r} = r - \lambda_C \cdot \text{LGD}_C - s_F$. A higher $\lambda_C$ *lowers* $\tilde{r}$, which for a positive-value derivative means greater effective discounting (the asset is worth less because of default risk).

    Actually, re-examining: in the BSDE formulation with driver $f$, the BSDE solution satisfies $V_t = \xi + \int_t^T f(s, V_s, Z_s) ds - \int_t^T Z_s dW_s$. The term $+\lambda_C \cdot \text{LGD}_C \cdot V^+$ in the driver *increases* the integral, which *increases* $V_t$. But this is the CVA component *within* the BSDE price -- the CVA adjustment is already embedded.

    The correct interpretation: the BSDE price $V_t$ is the XVA-adjusted price. A higher $\lambda_C$ increases $f$ (for $v > 0$), which by the comparison theorem gives a *higher* $V_t$. But $V_t$ here is the price *inclusive* of CVA. The standard decomposition is:

    $$
    V^{\text{adjusted}} = V^{\text{risk-free}} - \text{CVA}
    $$

    In the BSDE, the term $+\lambda_C \cdot \text{LGD}_C \cdot v^+$ acts as a source that *increases* the solution relative to the case without it. Formally, comparing $f$ (with CVA) against $f_0 = -rv$ (without CVA), we have $f \ge f_0$ for $v > 0$, so $V \ge V_0$ ... but this contradicts $V = V_0 - \text{CVA}$.

    The resolution is in the sign convention of the BSDE. In the standard XVA literature (Burgard-Kjaer), the BSDE is written with the driver on the *right* side. With $f^{(2)} > f^{(1)}$ (higher $\lambda_C$), the comparison theorem gives $V^{(2)} \ge V^{(1)}$. But in the Burgard-Kjaer PDE, the CVA term has a *positive* sign:

    $$
    \partial_t u + \mathcal{L}u - ru + \lambda_C \cdot \text{LGD}_C \cdot u^+ = 0
    $$

    The effective equation for $u > 0$ is $\partial_t u + \mathcal{L}u - (r - \lambda_C \cdot \text{LGD}_C)u = 0$, i.e., discount rate $\tilde{r} = r - \lambda_C \cdot \text{LGD}_C$. Higher $\lambda_C$ means lower $\tilde{r}$, which for a call option means the underlying grows at rate $\tilde{r}$ under the equivalent measure, giving a *lower* expected terminal value and thus a lower call price.

    For consistency with the comparison theorem: the PDE has $+\lambda_C \cdot \text{LGD}_C \cdot u^+$. Rewriting as $\partial_t u + \mathcal{L}u + f(u) = 0$ with $f(u) = -ru + \lambda_C \cdot \text{LGD}_C \cdot u^+$, a higher $\lambda_C$ increases $f$ for $u > 0$. By the maximum principle for parabolic PDEs, a larger source term leads to a higher solution. So $V^{(2)} \ge V^{(1)}$.

    **Conclusion:** Higher $\lambda_C$ *increases* the BSDE solution. This is because the BSDE price already incorporates the CVA adjustment. The correct statement is: *the BSDE price $V$ is the total (XVA-adjusted) price, and higher $\lambda_C$ makes the XVA component larger in the driver, but the overall price behavior depends on the specific formulation.*

    Under the standard financial interpretation where $V^{\text{adjusted}} = V^{\text{risk-free}} - \text{CVA}$, higher $\lambda_C$ increases CVA, which *reduces* $V^{\text{adjusted}}$ for the party bearing the counterparty risk. The comparison theorem confirms this: in the PDE formulation where CVA appears as an additional discount (effective rate $\tilde{r} = r - \lambda_C \cdot \text{LGD}_C$), a higher $\lambda_C$ means more discounting, leading to a lower price for the surviving party holding the positive-value position.

---

**Exercise 5.** The one-dimensional XVA PDE creates a free boundary problem at $u = 0$ where the effective discount rate changes. Explain why this is analogous to an American option free boundary. For a forward contract (which starts at $u = 0$ and can become either positive or negative), sketch the qualitative behavior of the XVA-adjusted price versus the risk-free price as a function of the underlying. Indicate the regions where CVA dominates (u > 0) and where DVA dominates (u < 0).

??? success "Solution to Exercise 5"
    **Analogy to the American option free boundary.**

    The one-dimensional XVA PDE has different effective discount rates depending on the sign of $u$:

    - For $u > 0$: $\tilde{r}^+ = r - \lambda_C \cdot \text{LGD}_C - s_F$ (CVA and FVA increase effective discounting)
    - For $u < 0$: $\tilde{r}^- = r + \lambda_B \cdot \text{LGD}_B$ (DVA decreases effective discounting, i.e., the liability is reduced)

    At $u = 0$, the solution must satisfy both regimes simultaneously, creating a **free boundary** where $u$ transitions between the two regimes. This is analogous to the American option problem where:

    - In the *continuation region*, the option satisfies the Black-Scholes PDE
    - In the *exercise region*, the option value equals the payoff
    - At the *free boundary*, the solution transitions between regimes with smooth pasting conditions ($u$ and $\partial_x u$ continuous)

    Similarly, for the XVA PDE, the free boundary $\{x : u(t,x) = 0\}$ separates the CVA-dominated region from the DVA-dominated region, and matching conditions must hold at this boundary.

    **Qualitative behavior for a forward contract.**

    A forward contract has risk-free value $\hat{u}(t, x) = x \cdot e^{-q(T-t)} - K \cdot e^{-r(T-t)}$, which is linear in $x$ and crosses zero at a forward price. The XVA-adjusted price $u$ differs from $\hat{u}$ as follows:

    **For large $x$ (deep in-the-money, $u > 0$):**

    - CVA and FVA effects dominate
    - The XVA-adjusted price $u < \hat{u}$: the holder faces counterparty default risk and must fund the positive value
    - The gap $\hat{u} - u$ grows with $x$ (larger exposure means larger CVA and FVA)

    **For small $x$ (deep out-of-the-money, $u < 0$):**

    - DVA dominates
    - The XVA-adjusted price $u > \hat{u}$ (less negative): the bank benefits from its own default risk on the liability
    - The gap $u - \hat{u}$ grows as $x$ decreases (larger negative exposure means larger DVA benefit)

    **Near $u = 0$ (at-the-money, the free boundary):**

    - The transition between regimes creates a kink or smooth transition
    - The XVA-adjusted zero-crossing shifts relative to $\hat{u}$'s zero-crossing

    The overall picture: the XVA-adjusted price curve $u(x)$ is "compressed" compared to $\hat{u}(x)$. It lies below $\hat{u}$ for positive values (CVA/FVA cost) and above $\hat{u}$ for negative values (DVA benefit), with the net effect being a flatter curve that crosses zero at a slightly different point.

---

**Exercise 6.** Describe the deep BSDE method for solving the XVA pricing equation in high dimensions. The method parameterizes the initial value as $V_{t_0} \approx \mathcal{N}_\theta(\mathbf{x}_0)$ and the control as $Z_{t_i} \approx \mathcal{N}_\phi^{(i)}(\mathbf{X}_{t_i})$, then minimizes $\mathbb{E}[|V_{t_N}^{\theta,\phi} - \Phi(X_T)|^2]$. Explain why the curse of dimensionality makes grid-based PDE methods infeasible for realistic XVA problems (e.g., a portfolio with 20 risk factors). How does the deep BSDE method circumvent this? What are the practical challenges in training the neural networks?

??? success "Solution to Exercise 6"
    **Description of the deep BSDE method.**

    The deep BSDE method (E, Han, Jentzen, 2017) reformulates the BSDE solution as an optimization problem that neural networks can solve:

    1. **Parameterization:** The initial value $V_0 = V_{t_0}$ is a learnable parameter $\theta$, and the control process $Z_{t_i}$ at each time step is parameterized by a neural network $\mathcal{N}_\phi^{(i)}$ that takes the current state $\mathbf{X}_{t_i}$ as input.

    2. **Forward simulation:** Simulate paths of the underlying $\mathbf{X}$ using the Euler-Maruyama scheme. Along each path, propagate $V$ forward using the BSDE dynamics:

        $$
        V_{t_{i+1}} = V_{t_i} - f(t_i, \mathbf{X}_{t_i}, V_{t_i}, Z_{t_i}) \Delta t + Z_{t_i} \cdot \Delta W_{t_i}
        $$

    3. **Loss function:** At maturity, the computed $V_{t_N}$ should match the payoff $\Phi(\mathbf{X}_T)$. The loss is:

        $$
        \mathcal{L}(\theta, \phi) = \mathbb{E}\left[\left|V_{t_N}^{\theta, \phi} - \Phi(\mathbf{X}_T)\right|^2\right]
        $$

    4. **Training:** Use stochastic gradient descent (Adam optimizer) to minimize $\mathcal{L}$ over batches of simulated paths.

    **Why grid-based methods are infeasible.**

    For a portfolio with $d = 20$ risk factors, the semilinear PDE lives in $\mathbb{R}^{20}$. A finite difference grid with $n$ points per dimension requires $n^{20}$ grid points. Even with $n = 10$ (very coarse):

    $$
    10^{20} = 10^{20} \text{ grid points}
    $$

    At 8 bytes per point, this requires $8 \times 10^{20}$ bytes $= 8 \times 10^8$ TB of memory -- clearly impossible. This is the **curse of dimensionality**: the computational cost grows exponentially with dimension, making grid-based PDE methods infeasible beyond 3-4 dimensions.

    **How the deep BSDE method circumvents this.**

    The deep BSDE method works in the *path space* rather than on a grid:

    1. Monte Carlo simulation scales linearly with dimension (simulating $d$-dimensional Brownian motion costs $O(d)$ per step).
    2. Neural networks can approximate high-dimensional functions without explicitly constructing a grid.
    3. The method uses $M$ sample paths (e.g., $M = 10{,}000$), each with $N$ time steps and $d$ dimensions, giving a computational cost of $O(M \times N \times d)$ -- polynomial in $d$ rather than exponential.
    4. Universal approximation theorems ensure that sufficiently large neural networks can approximate the solution and control to arbitrary accuracy.

    **Practical challenges in training:**

    1. *Architecture selection:* The networks $\mathcal{N}_\phi^{(i)}$ at each time step can share weights (reducing parameters) or be independent (more flexible but harder to train). The trade-off between expressiveness and trainability is problem-dependent.

    2. *Gradient propagation:* The forward pass through $N$ time steps creates deep computational graphs. Gradients can vanish or explode, especially for long-maturity problems with many time steps.

    3. *Non-smooth nonlinearity:* The $v^+$ and $v^-$ functions in the XVA driver are non-smooth at $v = 0$. This can create difficulties for gradient-based optimization near the free boundary.

    4. *Variance of loss estimates:* Monte Carlo estimates of $\mathcal{L}$ are noisy, requiring careful tuning of batch size and learning rate schedules.

    5. *Validation:* Unlike grid-based methods, there is no easy way to verify convergence. The method must be benchmarked against known solutions in low dimensions before being applied to high-dimensional problems.

---

**Exercise 7.** The connection between XVA pricing and dynamic risk measures via $g$-expectations is: $\mathcal{E}_g[X | \mathcal{F}_t] = Y_t$ where $Y$ solves a BSDE with driver $g$. If $g = 0$, this reduces to the conditional expectation (risk-neutral pricing). Explain how a convex driver $g$ corresponds to a convex risk measure. In the XVA context, is the standard XVA driver convex in $v$? Check by computing $\partial^2 f / \partial v^2$ at $v = 0$ and discussing what happens at the non-smooth points.

??? success "Solution to Exercise 7"
    **Convex driver and convex risk measure.**

    A $g$-expectation $\mathcal{E}_g[X | \mathcal{F}_t] = Y_t$ defines a nonlinear expectation operator. By Peng's theory, if the driver $g(t, y, z)$ satisfies:

    1. **Convexity in $(y, z)$:** $g(t, \alpha y_1 + (1-\alpha)y_2, \alpha z_1 + (1-\alpha)z_2) \le \alpha g(t, y_1, z_1) + (1-\alpha)g(t, y_2, z_2)$

    then the $g$-expectation satisfies:

    $$
    \mathcal{E}_g[\alpha X_1 + (1-\alpha) X_2 | \mathcal{F}_t] \le \alpha \mathcal{E}_g[X_1 | \mathcal{F}_t] + (1-\alpha) \mathcal{E}_g[X_2 | \mathcal{F}_t]
    $$

    This is exactly the **convexity** property of a risk measure: the risk of a diversified position is no greater than the weighted average of individual risks. Economically, convexity means the pricing operator rewards diversification.

    **Checking convexity of the XVA driver.**

    The standard XVA driver (without MVA) is:

    $$
    f(t, v, z) = -rv + \lambda_C \cdot \text{LGD}_C \cdot v^+ - \lambda_B \cdot \text{LGD}_B \cdot v^- + s_F(v - c)^+
    $$

    Since $f$ does not depend on $z$, we only need to check convexity in $v$.

    **Computing $\partial^2 f / \partial v^2$.**

    Away from the non-smooth points ($v \ne 0$ and $v \ne c$), the function is piecewise linear in $v$, so:

    $$
    \frac{\partial^2 f}{\partial v^2} = 0 \quad \text{for } v \ne 0, c
    $$

    At the non-smooth points, we examine the behavior:

    **At $v = 0$:** The function transitions between two linear regimes:

    - For $v > 0$ (assuming $c = 0$ for simplicity): $f = -rv + \lambda_C \cdot \text{LGD}_C \cdot v + s_F v = (-r + \lambda_C \cdot \text{LGD}_C + s_F) v$
    - For $v < 0$: $f = -rv + \lambda_B \cdot \text{LGD}_B \cdot v = (-r + \lambda_B \cdot \text{LGD}_B) v$

    Wait -- for $v < 0$: $v^+ = 0$, $v^- = -v$, so $f = -rv - \lambda_B \cdot \text{LGD}_B \cdot v^- = -rv + \lambda_B \cdot \text{LGD}_B \cdot v = -(r - \lambda_B \cdot \text{LGD}_B)v$.

    The left derivative at $v = 0$ is:

    $$
    f'(0^-) = -(r - \lambda_B \cdot \text{LGD}_B)
    $$

    The right derivative at $v = 0$ is:

    $$
    f'(0^+) = -r + \lambda_C \cdot \text{LGD}_C + s_F
    $$

    For convexity, we need $f'(0^+) \ge f'(0^-)$:

    $$
    -r + \lambda_C \cdot \text{LGD}_C + s_F \ge -(r - \lambda_B \cdot \text{LGD}_B)
    $$

    $$
    \lambda_C \cdot \text{LGD}_C + s_F \ge \lambda_B \cdot \text{LGD}_B
    $$

    This holds if the counterparty's credit adjustment plus the funding spread exceeds the bank's own credit adjustment, which is typical (counterparties are usually riskier than the bank, and $s_F > 0$). In this case, the slope increases at $v = 0$, corresponding to a **convex** kink.

    **At $v = c$ (if $c > 0$):** The FVA term $(v - c)^+$ has a kink. The left derivative contribution from FVA is 0 and the right derivative is $+s_F > 0$. Since the slope increases, this is also a convex kink.

    **Conclusion on convexity.**

    The XVA driver $f$ is **convex in $v$** under the typical condition $\lambda_C \cdot \text{LGD}_C + s_F \ge \lambda_B \cdot \text{LGD}_B$. The function is piecewise linear with slopes increasing at each kink point, making it convex (but not strictly convex -- it is piecewise affine).

    In the $g$-expectation framework, this means the XVA pricing rule is a **convex risk measure**: the XVA-adjusted price of a diversified portfolio is less than or equal to the weighted sum of individual XVA-adjusted prices. This provides a theoretical foundation for the empirical observation that netting reduces XVA.

    If the condition $\lambda_C \cdot \text{LGD}_C + s_F < \lambda_B \cdot \text{LGD}_B$ (bank is much riskier than counterparty, with low funding costs), then the kink at $v = 0$ is *concave*, and the overall driver is not convex. In this unusual case, the pricing operator would not define a convex risk measure, and diversification could theoretically increase XVA costs.
