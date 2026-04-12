# Penalization and Smoothness Constraints


Beyond simple parameter shrinkage, regularization can encode **structural beliefs** about smoothness, monotonicity, or shape. Such penalization is especially important when calibrating *functional* objects like volatility surfaces.

---

## Penalization as constraint relaxation


Hard constraints (e.g., exact smoothness or monotonicity) are often replaced by soft penalties:

$$
\min_{\theta} \; \mathcal{L}(\theta) + \lambda \mathcal{R}(\theta)
$$


where $\mathcal{R}$ measures deviation from desired structure.

This approach:
- improves numerical stability,
- allows controlled violations when data strongly suggest them.

---

## Smoothness penalties


### 1. Finite-difference penalties


For discretized parameters $\theta_i$:

$$
\mathcal{R}(\theta)
= \sum_i (\theta_{i+1}-\theta_i)^2
\quad \text{or} \quad
\sum_i (\theta_{i+2}-2\theta_{i+1}+\theta_i)^2
$$



These penalize:
- large gradients (first differences),
- curvature/roughness (second differences).

### 2. Continuous formulations


For a function $f(x)$:

$$
\mathcal{R}(f) = \int |f'(x)|^2 dx
\quad \text{or} \quad
\int |f''(x)|^2 dx
$$



Such penalties are common in spline-based volatility surfaces.

---

## Shape and financial constraints


Regularization can enforce economically motivated shapes:

- **monotonicity** (e.g., total variance in maturity),
- **convexity** (call price in strike),
- **positivity** (variance, intensities).

These are often implemented as:
- inequality constraints with slack variables,
- barrier or penalty terms.

---

## Penalization in stochastic and local volatility


- **Local volatility:** strong smoothing needed to prevent noise amplification.
- **Stochastic volatility:** mild penalties help stabilize weakly identified parameters.
- **Term-structure models:** smoothness across maturity improves forward consistency.

---

## Interaction with discretization


Penalization strength depends on grid resolution:

- finer grids require stronger penalties for comparable smoothness,
- penalties should scale with discretization step size.

Ignoring this can lead to misleading calibration comparisons.

---

## Key takeaways


- Penalization encodes prior beliefs about smoothness and shape.
- Smoothness constraints are essential for functional calibration problems.
- The choice of penalty must be consistent with discretization and economics.

---

## Further reading


- Wahba, *Spline Models for Observational Data*.
- Fengler, *Semiparametric Modeling of Implied Volatility*.
- Gatheral, *The Volatility Surface*.

---

## Exercises

**Exercise 1.** For a discretized local volatility surface on a grid with $n$ strike points, write down the first-difference and second-difference penalty matrices $D_1$ and $D_2$ explicitly for $n = 5$. Show that the second-difference penalty $\mathcal{R}(\theta) = \|D_2\theta\|^2$ penalizes curvature while leaving linear functions unpenalized.

??? success "Solution to Exercise 1"
    Let the parameter vector be $\theta = (\theta_1, \theta_2, \theta_3, \theta_4, \theta_5)^\top$. The **first-difference matrix** $D_1 \in \mathbb{R}^{4 \times 5}$ is

    $$
    D_1 = \begin{pmatrix} -1 & 1 & 0 & 0 & 0 \\ 0 & -1 & 1 & 0 & 0 \\ 0 & 0 & -1 & 1 & 0 \\ 0 & 0 & 0 & -1 & 1 \end{pmatrix}
    $$

    so that $(D_1 \theta)_i = \theta_{i+1} - \theta_i$ for $i = 1, \ldots, 4$.

    The **second-difference matrix** $D_2 \in \mathbb{R}^{3 \times 5}$ is

    $$
    D_2 = \begin{pmatrix} 1 & -2 & 1 & 0 & 0 \\ 0 & 1 & -2 & 1 & 0 \\ 0 & 0 & 1 & -2 & 1 \end{pmatrix}
    $$

    so that $(D_2 \theta)_i = \theta_{i+2} - 2\theta_{i+1} + \theta_i$ for $i = 1, 2, 3$.

    Now consider a linear function $\theta_i = a + b\,i$ for constants $a, b$. Then

    $$
    (D_2 \theta)_i = (a + b(i+2)) - 2(a + b(i+1)) + (a + b\,i) = a + bi + 2b - 2a - 2bi - 2b + a + bi = 0
    $$

    for every $i$. Therefore $\|D_2 \theta\|^2 = 0$ for any linear $\theta$, confirming that the second-difference penalty has the **null space** consisting of all linear (affine) functions on the grid.

    Geometrically, the second-difference operator is a discrete approximation to the second derivative $f''$, which vanishes for linear functions. The penalty $\|D_2 \theta\|^2$ thus measures the total squared discrete curvature while leaving the linear trend completely unpenalized.

---

**Exercise 2.** Consider the continuous smoothness penalty $\mathcal{R}(f) = \int_a^b (f''(x))^2\,dx$. Show that among all functions interpolating $n$ data points, the one minimizing this penalty is a natural cubic spline. What boundary conditions does the natural cubic spline satisfy?

??? success "Solution to Exercise 2"
    We seek to minimize

    $$
    \mathcal{R}(f) = \int_a^b (f''(x))^2\,dx
    $$

    subject to the interpolation constraints $f(x_i) = y_i$ for $i = 1, \ldots, n$, where $a \le x_1 < \cdots < x_n \le b$.

    **Proof via calculus of variations.** Define the admissible set $\mathcal{A} = \{f \in H^2[a,b] : f(x_i) = y_i\}$. Let $f^*$ be the minimizer and let $g \in H^2[a,b]$ satisfy $g(x_i) = 0$ for all $i$. For any $\epsilon$, $f^* + \epsilon g \in \mathcal{A}$, so

    $$
    \frac{d}{d\epsilon}\bigg|_{\epsilon=0} \int_a^b (f^{*\prime\prime} + \epsilon g'')^2\,dx = 2\int_a^b f^{*\prime\prime}(x)\,g''(x)\,dx = 0
    $$

    Integrating by parts twice:

    $$
    \int_a^b f^{*\prime\prime} g''\,dx = \bigl[f^{*\prime\prime} g'\bigr]_a^b - \int_a^b f^{*\prime\prime\prime} g'\,dx = \bigl[f^{*\prime\prime} g' - f^{*\prime\prime\prime} g\bigr]_a^b + \int_a^b f^{*(4)}(x)\,g(x)\,dx
    $$

    For this to vanish for all admissible $g$:

    1. On each sub-interval $(x_i, x_{i+1})$, the fundamental lemma of the calculus of variations gives $f^{*(4)}(x) = 0$, so $f^*$ is a cubic polynomial on each sub-interval.
    2. At the interpolation points, $f^*$, $f^{*\prime}$, and $f^{*\prime\prime}$ must be continuous (otherwise the penalty integral would be infinite). This gives $C^2$ continuity.
    3. The boundary terms give $f^{*\prime\prime}(a) = 0$ and $f^{*\prime\prime}(b) = 0$.

    A function that is piecewise cubic, $C^2$ at each knot, and satisfies $f''(a) = f''(b) = 0$ is precisely a **natural cubic spline**.

    The **natural boundary conditions** are

    $$
    f''(x_1) = 0 \quad \text{and} \quad f''(x_n) = 0
    $$

    These conditions state that the spline becomes linear (zero curvature) at the endpoints, which is the variational consequence of not penalizing the function behavior beyond the data range.

---

**Exercise 3.** A practitioner fits an implied volatility smile at a single maturity using a penalized least-squares objective:

$$
\min_f \sum_{i=1}^m w_i(f(k_i) - \sigma_i^{\text{obs}})^2 + \lambda \int (f''(k))^2\,dk
$$

If $\lambda$ is too small, the fit interpolates the noisy data exactly. If $\lambda$ is too large, the fit becomes a straight line. For intermediate $\lambda$, how many effective degrees of freedom does the smoother have? Relate this to the trace of the smoother matrix.

??? success "Solution to Exercise 3"
    The penalized least-squares estimator can be written in matrix form as $\hat{f} = S_\lambda y$, where $S_\lambda$ is the **smoother matrix** (also called the hat matrix) that maps observed values to fitted values.

    The **effective degrees of freedom** (edf) of the smoother is defined as

    $$
    \text{edf}(\lambda) = \operatorname{tr}(S_\lambda)
    $$

    To understand the behavior:

    - **When $\lambda \to 0$:** The penalty vanishes, and the fit interpolates the data exactly. In the spline formulation with $m$ data points, the smoother matrix approaches the identity $S_0 = I_m$, so $\text{edf} \to m$. All $m$ degrees of freedom are used.

    - **When $\lambda \to \infty$:** The roughness penalty dominates. Since $\int (f'')^2\,dk$ is minimized by linear functions (for which $f'' = 0$), the fit converges to the (weighted) least-squares line. A linear fit has 2 parameters, so $\text{edf} \to 2$.

    - **For intermediate $\lambda$:** The effective degrees of freedom interpolates smoothly between 2 and $m$. One can show this using the representation in the Demmler-Reinsch basis. If we write the penalty in the eigenbasis of the roughness matrix with eigenvalues $\delta_j$, then

    $$
    S_\lambda = \operatorname{diag}\!\left(\frac{1}{1 + \lambda \delta_j}\right)
    $$

    and

    $$
    \text{edf}(\lambda) = \sum_{j=1}^m \frac{1}{1 + \lambda \delta_j}
    $$

    Each term lies in $(0, 1]$, with the two eigenvalues $\delta_j = 0$ (corresponding to the linear functions in the null space of the penalty) contributing exactly 1 each.

    The effective degrees of freedom provides a continuous, interpretable measure of model complexity. In practice, one can select $\lambda$ by targeting a specific edf, or by minimizing a criterion such as generalized cross-validation (GCV):

    $$
    \text{GCV}(\lambda) = \frac{\frac{1}{m}\|y - S_\lambda y\|^2}{\left(1 - \frac{\text{edf}(\lambda)}{m}\right)^2}
    $$

---

**Exercise 4.** Monotonicity of total variance in maturity ($\partial_T w \ge 0$) is a no-arbitrage constraint. Formulate this as both a hard constraint and a soft penalty. For the soft penalty version, propose a specific penalty function $\mathcal{R}_{\text{mono}}(w)$ that is zero when the constraint is satisfied and positive otherwise. Discuss the trade-off between hard and soft enforcement.

??? success "Solution to Exercise 4"
    Let $w(K, T)$ denote the total implied variance surface (total variance = implied variance $\times$ time to maturity). The no-arbitrage constraint requires

    $$
    \frac{\partial w}{\partial T}(K, T) \ge 0 \quad \text{for all } K, T
    $$

    since calendar spreads must have non-negative value.

    **Hard constraint formulation.** In the discretized setting with maturities $T_1 < \cdots < T_N$ and strikes $K_1, \ldots, K_M$:

    $$
    \min_{w} \sum_{i,j} \alpha_{ij}(w(K_j, T_i) - w^{\text{obs}}_{ij})^2 \quad \text{subject to} \quad w(K_j, T_{i+1}) \ge w(K_j, T_i) \;\;\forall\, i, j
    $$

    This is a quadratic program with linear inequality constraints.

    **Soft penalty formulation.** Define

    $$
    \mathcal{R}_{\text{mono}}(w) = \sum_{i=1}^{N-1} \sum_{j=1}^{M} \left[\max\!\left(0,\; w(K_j, T_i) - w(K_j, T_{i+1})\right)\right]^2
    $$

    This penalty is zero whenever $w(K_j, T_{i+1}) \ge w(K_j, T_i)$ (monotonicity holds) and positive when the constraint is violated. The full penalized objective becomes

    $$
    \min_{w} \sum_{i,j} \alpha_{ij}(w(K_j, T_i) - w^{\text{obs}}_{ij})^2 + \mu \,\mathcal{R}_{\text{mono}}(w)
    $$

    where $\mu > 0$ controls the enforcement strength.

    In the continuous setting, one can use

    $$
    \mathcal{R}_{\text{mono}}(w) = \int \!\!\int \left[\max\!\left(0, -\frac{\partial w}{\partial T}(K, T)\right)\right]^2 dK\,dT
    $$

    **Trade-off discussion:**

    - *Hard constraints* guarantee no arbitrage but may be infeasible if the data themselves violate the constraint (noisy quotes), leading to poor fits or numerical difficulties.
    - *Soft penalties* allow small violations, which is more robust to noisy data. The parameter $\mu$ controls the trade-off: as $\mu \to \infty$, the soft penalty approaches the hard constraint.
    - In practice, a two-stage approach is common: first fit with soft penalty, then project onto the feasible set. Alternatively, use the soft penalty with a large but finite $\mu$ and verify that residual violations are within bid-ask spreads.

---

**Exercise 5.** For a local volatility grid with spacing $h$ in strike, show that the first-difference penalty with coefficient $\lambda$ is equivalent to a continuous penalty with effective strength $\lambda / h$. Conclude that if the grid is refined (smaller $h$), the penalty coefficient $\lambda$ must be increased proportionally to maintain the same level of smoothing. Derive the exact scaling relationship.

??? success "Solution to Exercise 5"
    Consider a function $f$ sampled on a uniform grid $x_i = a + ih$ for $i = 0, 1, \ldots, n$, with spacing $h = (b-a)/n$. The first-difference penalty is

    $$
    \mathcal{R}_h(\theta) = \sum_{i=0}^{n-1} (\theta_{i+1} - \theta_i)^2
    $$

    where $\theta_i = f(x_i)$. By Taylor expansion, $\theta_{i+1} - \theta_i = f(x_{i+1}) - f(x_i) \approx h f'(x_i)$, so

    $$
    \mathcal{R}_h(\theta) \approx \sum_{i=0}^{n-1} h^2 (f'(x_i))^2 = h \sum_{i=0}^{n-1} h\,(f'(x_i))^2 \approx h \int_a^b (f'(x))^2\,dx
    $$

    The last step recognizes the sum as a Riemann approximation with step $h$. Therefore the discrete penalized problem

    $$
    \min_\theta \sum_{i=1}^m (f(x_i) - y_i)^2 + \lambda \sum_{i=0}^{n-1}(\theta_{i+1} - \theta_i)^2
    $$

    is approximately equivalent to the continuous problem

    $$
    \min_f \sum_{i=1}^m (f(x_i) - y_i)^2 + \lambda\, h \int_a^b (f'(x))^2\,dx
    $$

    The effective continuous regularization strength is therefore $\lambda_{\text{eff}} = \lambda h$.

    **Scaling relationship.** If we refine the grid from spacing $h$ to spacing $h' = h/2$ and want the same effective smoothing $\lambda_{\text{eff}}$, we need

    $$
    \lambda' h' = \lambda h \quad \implies \quad \lambda' = \lambda \frac{h}{h'} = 2\lambda
    $$

    More generally, the required scaling is

    $$
    \lambda \propto \frac{1}{h}
    $$

    That is, halving the grid spacing requires doubling the penalty coefficient. If this scaling is not applied, refining the grid will effectively weaken the regularization, producing rougher fits despite having the same nominal $\lambda$ — a common source of inconsistency in calibration comparisons across different grid resolutions.

---

**Exercise 6.** Combine a smoothness penalty with a convexity constraint for fitting a call price surface. Write down the full optimization problem including: (a) data-fitting term, (b) smoothness penalty in strike, (c) smoothness penalty in maturity, and (d) hard convexity constraint $\partial_{KK}C \ge 0$. Discuss how you would solve this constrained optimization problem numerically.

??? success "Solution to Exercise 6"
    Let $C(K_j, T_i)$ denote the call price surface on a grid of strikes $K_1 < \cdots < K_M$ and maturities $T_1 < \cdots < T_N$. The full optimization problem is:

    **(a) Data-fitting term:**

    $$
    \mathcal{L}(C) = \sum_{i=1}^{N} \sum_{j=1}^{M} w_{ij}\bigl(C(K_j, T_i) - C^{\text{obs}}_{ij}\bigr)^2
    $$

    where $w_{ij}$ are weights (e.g., inverse bid-ask spread squared or vega-weighted).

    **(b) Smoothness penalty in strike:** Using second differences along the strike direction at each maturity:

    $$
    \mathcal{R}_K(C) = \sum_{i=1}^{N} \sum_{j=1}^{M-2} \bigl(C(K_{j+2}, T_i) - 2C(K_{j+1}, T_i) + C(K_j, T_i)\bigr)^2
    $$

    **(c) Smoothness penalty in maturity:** Using first or second differences along the maturity direction at each strike:

    $$
    \mathcal{R}_T(C) = \sum_{i=1}^{N-1} \sum_{j=1}^{M} \bigl(C(K_j, T_{i+1}) - C(K_j, T_i)\bigr)^2
    $$

    **(d) Hard convexity constraint:** The call price must be convex in strike, which in the discrete setting means

    $$
    C(K_{j+2}, T_i) - 2C(K_{j+1}, T_i) + C(K_j, T_i) \ge 0 \quad \text{for all } i, j
    $$

    This is the discrete analogue of $\partial_{KK}C \ge 0$ and is equivalent to requiring that butterfly spreads have non-negative value.

    **Full problem:**

    $$
    \min_{C} \;\; \mathcal{L}(C) + \lambda_K \mathcal{R}_K(C) + \lambda_T \mathcal{R}_T(C)
    $$

    subject to

    $$
    C(K_{j+2}, T_i) - 2C(K_{j+1}, T_i) + C(K_j, T_i) \ge 0 \quad \forall\, i = 1,\ldots,N,\; j = 1,\ldots,M-2
    $$

    **Numerical solution approaches:**

    1. **Quadratic programming (QP).** The objective is quadratic in the unknowns $C(K_j, T_i)$ and the constraints are linear inequalities. This is a standard convex QP, solvable by interior-point methods or active-set methods. For moderate grid sizes (e.g., $N \times M \le 500$), off-the-shelf QP solvers (OSQP, Gurobi, CVXOPT) handle this efficiently.

    2. **Augmented Lagrangian / ADMM.** For larger problems, one can split the objective into the smooth data-fitting + penalty part and the constraint part, solving each sub-problem alternately. ADMM is particularly effective when the constraint projection (onto the convex cone) is cheap.

    3. **Interior-point methods.** Replace the hard constraint by a logarithmic barrier:

    $$
    -\frac{1}{t}\sum_{i,j} \log\bigl(C(K_{j+2}, T_i) - 2C(K_{j+1}, T_i) + C(K_j, T_i)\bigr)
    $$

    and increase $t$ iteratively. This converts the constrained problem into a sequence of unconstrained problems.

    4. **Practical considerations.** One should also enforce additional no-arbitrage constraints (monotonicity in maturity for total variance, boundary conditions as $K \to 0$ and $K \to \infty$), and choose $\lambda_K, \lambda_T$ via cross-validation or the L-curve method.
