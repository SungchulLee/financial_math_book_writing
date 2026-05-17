# Gradient-Based vs Gradient-Free Methods

Calibration algorithms fall into two broad classes depending on whether they use derivative information of the objective function. Gradient-based methods exploit first- and second-order derivatives for fast local convergence, while gradient-free methods rely only on function evaluations and offer greater robustness to noise and non-smoothness. This section compares the principal algorithms from each class, analyzes their convergence properties, and identifies the regimes where each approach excels.

---

## Problem setup

Recall that the calibration objective takes the form

$$
\min_{\Theta \in \mathcal{D}} \; \mathcal{L}(\Theta) = \frac{1}{2} \sum_{j=1}^{m} w_j \left( f_j(\Theta) - y_j \right)^2 = \frac{1}{2} \| r(\Theta) \|_W^2
$$

where $\Theta \in \mathbb{R}^d$ is the parameter vector ($d = 5$ for Heston, $d = 3$ for SABR with fixed $\beta$), $r(\Theta)$ is the residual vector, and $\mathcal{D}$ is the feasible set defined by parameter bounds. The Jacobian of the residual is $J(\Theta) = \nabla_\Theta r(\Theta) \in \mathbb{R}^{m \times d}$.

The choice of algorithm depends on three factors:

1. **Availability of derivatives.** Can $\nabla \mathcal{L}$ or $J$ be computed efficiently?
2. **Smoothness of the objective.** Is $\mathcal{L}$ smooth, or does it contain noise from Monte Carlo pricing?
3. **Number of local minima.** Is the landscape unimodal or multi-modal?

---

## Gradient-based methods

Gradient-based methods use derivative information to determine the search direction. They achieve fast convergence when the objective is smooth and a good starting point is available.

### Gauss-Newton and Levenberg-Marquardt methods

Recall (see [§ Optimization algorithms](../calibration_as_inverse_problem/optimization_algorithms.md)): the Gauss-Newton update solves $(J^\top W J)\Delta\Theta = -J^\top W r$ using the small-residual Hessian approximation; the Levenberg-Marquardt (LM) algorithm regularizes this with damping $(J^\top W J + \lambda I)\Delta\Theta = -J^\top W r$, interpolating between Gauss-Newton ($\lambda\to 0$) and gradient descent ($\lambda\to\infty$).

For SV calibration specifically, Gauss-Newton convergence degrades when $J^\top W J$ is near-singular — common when $\kappa$ and $\theta$ are entangled in Heston.

**Adaptive damping.** The gain ratio $\varrho$ measures the quality of the quadratic model:

$$
\varrho = \frac{\mathcal{L}(\Theta^{(k)}) - \mathcal{L}(\Theta^{(k)} + \Delta\Theta)}{\Delta\Theta^\top (J^\top W r + \frac{1}{2}(J^\top W J + \lambda I) \Delta\Theta)}
$$

The update rule is:

- $\varrho > 0.75$: good model, reduce $\lambda \leftarrow \lambda / \beta_{\mathrm{down}}$ (typically $\beta_{\mathrm{down}} = 3$)
- $0.25 < \varrho \leq 0.75$: adequate model, keep $\lambda$
- $\varrho \leq 0.25$: poor model, increase $\lambda \leftarrow \beta_{\mathrm{up}} \cdot \lambda$ (typically $\beta_{\mathrm{up}} = 2$)

**Convergence theorem.** Under standard regularity assumptions (Lipschitz-continuous Jacobian, bounded weights), the LM algorithm with adaptive damping satisfies:

$$
\liminf_{k \to \infty} \| \nabla \mathcal{L}(\Theta^{(k)}) \| = 0
$$

The local convergence rate near a regular minimum (where $J^\top W J$ is nonsingular) is quadratic when $\lambda^{(k)} \to 0$, matching Gauss-Newton.

!!! note "Marquardt's scaling"
    An important variant replaces $\lambda I$ with $\lambda \, \mathrm{diag}(J^\top W J)$, which accounts for different parameter scales. This is particularly useful in Heston calibration where parameters span different orders of magnitude (e.g., $v_0 \sim 0.04$ versus $\kappa \sim 3.0$).

### Trust-region methods

Trust-region methods constrain the step size rather than regularizing the Hessian. At each iteration, the subproblem is

$$
\min_{\Delta\Theta} \; q(\Delta\Theta) = \nabla \mathcal{L}^\top \Delta\Theta + \frac{1}{2} \Delta\Theta^\top B \, \Delta\Theta \quad \text{subject to} \quad \| \Delta\Theta \| \leq \Delta_k
$$

where $B = J^\top W J$ (or the full Hessian) and $\Delta_k$ is the trust-region radius. The radius is adjusted based on the actual-to-predicted reduction ratio $\varrho$:

- $\varrho > 0.75$ and $\| \Delta\Theta \| = \Delta_k$: expand, $\Delta_{k+1} = 2 \Delta_k$
- $\varrho < 0.25$: contract, $\Delta_{k+1} = \Delta_k / 4$
- Otherwise: keep $\Delta_{k+1} = \Delta_k$

Trust-region methods have strong global convergence guarantees: every limit point of the sequence $\{\Theta^{(k)}\}$ is a stationary point.

### Adjoint methods for gradient computation

The cost of gradient-based methods depends critically on how the Jacobian $J$ is computed. Three approaches are available.

**Finite differences.** The simplest method approximates

$$
\frac{\partial r_j}{\partial \Theta_k} \approx \frac{r_j(\Theta + h_k e_k) - r_j(\Theta)}{h_k}
$$

with step size $h_k$. This requires $d + 1$ evaluations of the pricing function per iteration. Central differences improve accuracy to $\mathcal{O}(h^2)$ at the cost of $2d + 1$ evaluations.

The optimal step size balances truncation error ($\mathcal{O}(h)$) against numerical cancellation ($\mathcal{O}(\varepsilon_{\mathrm{mach}} / h)$):

$$
h^* \sim \sqrt{\varepsilon_{\mathrm{mach}}} \cdot |\Theta_k| \approx 10^{-8} \cdot |\Theta_k|
$$

for double-precision arithmetic.

**Algorithmic (adjoint) differentiation.** Adjoint AD computes the full gradient $\nabla_\Theta \mathcal{L}$ in a single backward pass through the pricing code, with computational cost

$$
\text{cost}(\nabla \mathcal{L}) \leq C_{\mathrm{AD}} \cdot \text{cost}(\mathcal{L})
$$

where $C_{\mathrm{AD}} \leq 5$ is a constant independent of the parameter dimension $d$. This is a dramatic improvement over finite differences when $d$ is moderate to large.

For the Heston characteristic function, the adjoint pass differentiates through the Riccati ODE solutions $C(u, T)$ and $D(u, T)$, the FFT, and the objective function evaluation. Modern AD tools (e.g., JAX, PyTorch, or Enzyme) automate this process.

**Analytic derivatives.** For models with closed-form pricing (e.g., SABR via Hagan's formula), the Jacobian can be computed by direct differentiation of the pricing formula. This is the fastest approach but requires model-specific derivations.

---

## Gradient-free methods

Gradient-free methods use only function values $\mathcal{L}(\Theta)$. They are essential when:

- The pricing function involves Monte Carlo simulation (noisy gradients)
- The objective is non-differentiable (e.g., uses $\ell_1$ loss or max-norm)
- Implementation simplicity outweighs convergence speed

### Nelder-Mead simplex

The Nelder-Mead algorithm maintains a simplex of $d + 1$ vertices $\{\Theta_0, \ldots, \Theta_d\}$ in parameter space and iteratively replaces the worst vertex through geometric transformations.

Let the vertices be ordered so that $\mathcal{L}(\Theta_0) \leq \mathcal{L}(\Theta_1) \leq \cdots \leq \mathcal{L}(\Theta_d)$. The centroid of the best $d$ vertices is $\bar{\Theta} = \frac{1}{d} \sum_{i=0}^{d-1} \Theta_i$. The algorithm attempts the following operations in sequence:

1. **Reflection.** $\Theta_r = \bar{\Theta} + \alpha_r (\bar{\Theta} - \Theta_d)$ with $\alpha_r = 1$. If $\mathcal{L}(\Theta_0) \leq \mathcal{L}(\Theta_r) < \mathcal{L}(\Theta_{d-1})$, accept $\Theta_r$.

2. **Expansion.** If $\mathcal{L}(\Theta_r) < \mathcal{L}(\Theta_0)$, try $\Theta_e = \bar{\Theta} + \alpha_e (\Theta_r - \bar{\Theta})$ with $\alpha_e = 2$. Accept the better of $\Theta_r$ and $\Theta_e$.

3. **Contraction.** If $\mathcal{L}(\Theta_r) \geq \mathcal{L}(\Theta_{d-1})$:
    - *Outside contraction*: $\Theta_c = \bar{\Theta} + \alpha_c (\Theta_r - \bar{\Theta})$ with $\alpha_c = 0.5$.
    - *Inside contraction*: $\Theta_c = \bar{\Theta} - \alpha_c (\bar{\Theta} - \Theta_d)$ with $\alpha_c = 0.5$.

4. **Shrink.** If contraction fails, shrink all vertices toward the best: $\Theta_i \leftarrow \Theta_0 + \sigma_s (\Theta_i - \Theta_0)$ with $\sigma_s = 0.5$.

**Convergence properties.** Nelder-Mead has no general convergence guarantee in dimensions $d \geq 2$. McKinnon (1998) constructed examples where the algorithm converges to a non-stationary point. In practice, it performs well on low-dimensional problems ($d \leq 5$--$10$) and is widely used for SABR calibration ($d = 3$) and Heston calibration ($d = 5$).

The method requires $\mathcal{O}(1)$--$\mathcal{O}(2)$ function evaluations per iteration (compared to $d + 1$ for finite-difference gradients), making it attractive when each evaluation is expensive.

### Powell's conjugate direction method

Powell's method searches along a set of directions $\{d_1, \ldots, d_d\}$, performing exact line minimization along each. After one cycle of $d$ line searches, the direction of greatest improvement is replaced by the net displacement direction. The conjugate direction property emerges from the line search geometry rather than from gradient information.

**Convergence.** For a quadratic objective $\mathcal{L}(\Theta) = \frac{1}{2} \Theta^\top A \Theta + b^\top \Theta + c$, Powell's method terminates in at most $d$ cycles (each of $d$ line searches), achieving finite termination analogous to conjugate gradient methods.

For non-quadratic objectives, convergence is superlinear in favorable cases but can stall if the search directions become nearly dependent.

### Bayesian optimization

Bayesian optimization builds a probabilistic surrogate model of the objective function and selects the next evaluation point to maximize an acquisition function.

The **Gaussian process** (GP) surrogate models $\mathcal{L}(\Theta)$ as a random function with posterior mean $\mu(\Theta)$ and variance $\sigma^2(\Theta)$ conditioned on evaluations $\{(\Theta_i, \mathcal{L}_i)\}_{i=1}^n$. The **expected improvement** (EI) acquisition function

$$
\mathrm{EI}(\Theta) = \mathbb{E}\!\left[\max\!\left(\mathcal{L}_{\min} - \mathcal{L}(\Theta), 0\right)\right] = (\mathcal{L}_{\min} - \mu(\Theta)) \Phi(z) + \sigma(\Theta) \phi(z)
$$

where $z = (\mathcal{L}_{\min} - \mu(\Theta)) / \sigma(\Theta)$, balances exploitation (evaluating near the current best) against exploration (evaluating where uncertainty is high).

**Strengths.** Bayesian optimization is sample-efficient, often finding good solutions in 50--200 evaluations, making it viable when each pricing evaluation is very expensive (e.g., Monte Carlo pricing of exotics).

**Limitations.** The GP overhead scales as $\mathcal{O}(n^3)$ with the number of evaluations, limiting applicability to problems with moderate evaluation budgets. The method also struggles in dimensions above $d \approx 20$.

---

## Convergence comparison

The following table summarizes the convergence properties and computational costs of the main algorithms.

| Algorithm | Order | Cost per iteration | Gradient needed | Global convergence |
|-----------|-------|-------------------|-----------------|-------------------|
| Gauss-Newton | Quadratic (small residuals) | $\mathcal{O}(md^2)$ solve | Yes | No |
| Levenberg-Marquardt | Quadratic (local) | $\mathcal{O}(md^2)$ solve | Yes | Yes (to stationary) |
| Trust region | Quadratic (local) | $\mathcal{O}(md^2)$ solve | Yes | Yes (to stationary) |
| Nelder-Mead | Sublinear (no guarantee) | $\mathcal{O}(m)$ evaluations | No | No (heuristic) |
| Powell | Superlinear (quadratic) | $\mathcal{O}(md)$ line searches | No | No (heuristic) |
| Bayesian optimization | N/A (global) | $\mathcal{O}(n^3)$ GP update | No | Asymptotic |

The cost per iteration includes the pricing evaluations ($\mathcal{O}(m)$ for $m$ instruments) and the linear algebra. The gradient cost is dominated by the Jacobian computation: $\mathcal{O}(dm)$ for finite differences, $\mathcal{O}(m)$ for adjoint AD.

### Empirical comparison on Heston calibration

In practice, the convergence behavior on a typical Heston calibration problem (50 options, 5 maturities, 10 strikes per maturity) is approximately:

| Algorithm | Iterations to $10^{-6}$ | Function evaluations | Wall time |
|-----------|--------------------------|---------------------|-----------|
| LM (analytic Jacobian) | 15--30 | 100--200 | 0.5--2 s |
| LM (finite differences) | 15--30 | 500--1200 | 2--8 s |
| Nelder-Mead | 200--500 | 200--500 | 1--5 s |
| Powell | 100--300 | 500--1500 | 3--10 s |
| Bayesian optimization | 50--150 | 50--150 | 10--60 s |

!!! tip "Practical recommendation"
    For production Heston calibration with semi-analytic pricing, Levenberg-Marquardt with adjoint differentiation is the method of choice. For SABR calibration (only 3 parameters, closed-form pricing), Nelder-Mead or even grid search is competitive. For calibration involving Monte Carlo pricing (e.g., rough volatility models), Bayesian optimization or Nelder-Mead avoids the difficulty of noisy gradients.

---

## Hybrid strategies

The strengths of gradient-based and gradient-free methods are complementary. Two hybrid strategies are widely used in practice.

### Global-then-local

Use a global gradient-free method (differential evolution, particle swarm) for a limited number of iterations to locate the basin of the global minimum, then switch to LM for rapid local convergence:

1. Run differential evolution for 50--100 generations with a population of 20--50 individuals.
2. Take the best individual as the starting point for LM.
3. Run LM to convergence with tight tolerances.

This strategy is particularly effective for Heston calibration, where the objective has 2--3 local minima and the global minimum is well-separated.

### Multi-start local

Run $N$ independent LM optimizations from randomly sampled starting points and select the best result:

1. Sample $\Theta^{(1)}, \ldots, \Theta^{(N)}$ uniformly from the parameter bounds.
2. Run LM from each starting point to convergence.
3. Return $\hat{\Theta} = \arg\min_i \mathcal{L}(\Theta_{\mathrm{final}}^{(i)})$.

With $N = 10$--$50$ starts, this approach achieves near-global optimality with full parallelizability across starting points.

---

## Exercises

**Exercise 1.** Starting from the nonlinear least-squares objective $\mathcal{L}(\Theta) = \frac{1}{2}\|r(\Theta)\|_W^2$, derive the Gauss-Newton update equation $(J^\top W J)\Delta\Theta = -J^\top W r$. Under what conditions on the residual vector $r(\Theta^\star)$ does the Gauss-Newton method achieve quadratic convergence?

??? success "Solution to Exercise 1"
    **Derivation of the Gauss-Newton update.** Starting from the weighted nonlinear least-squares objective

    $$
    \mathcal{L}(\Theta) = \frac{1}{2} \|r(\Theta)\|_W^2 = \frac{1}{2} r(\Theta)^\top W \, r(\Theta)
    $$

    the gradient is

    $$
    \nabla \mathcal{L} = J^\top W \, r
    $$

    where $J = \nabla_\Theta r(\Theta) \in \mathbb{R}^{m \times d}$ is the Jacobian. The Hessian is

    $$
    H = J^\top W J + \sum_{j=1}^{m} w_j r_j \nabla^2 f_j
    $$

    The Gauss-Newton approximation drops the second-order term $\sum_j w_j r_j \nabla^2 f_j$, giving $H \approx J^\top W J$. Setting the Newton update $H \, \Delta\Theta = -\nabla \mathcal{L}$ yields

    $$
    (J^\top W J) \, \Delta\Theta = -J^\top W \, r
    $$

    which is the Gauss-Newton equation.

    **Conditions for quadratic convergence.** Near a solution $\Theta^*$, we can analyze the convergence rate by examining the error in the Hessian approximation. The true Newton direction uses $H = J^\top W J + S$ where $S = \sum_j w_j r_j \nabla^2 f_j$. The Gauss-Newton error is proportional to $\|S\|$, which satisfies

    $$
    \|S(\Theta^*)\| \leq C_1 \|r(\Theta^*)\| \cdot \max_j \|\nabla^2 f_j(\Theta^*)\|
    $$

    Quadratic convergence of the Gauss-Newton method occurs when $r(\Theta^*) = 0$ (zero residual at the solution). In this case $S(\Theta^*) = 0$ and the Gauss-Newton Hessian equals the true Hessian, so the method behaves identically to Newton's method, which converges quadratically under standard assumptions (Lipschitz-continuous Jacobian and nonsingular $J^\top W J$).

    When $r(\Theta^*) \neq 0$ (nonzero residuals), the dropped second-order term introduces an $\mathcal{O}(\|r(\Theta^*)\|)$ error. The convergence rate degrades to linear with rate constant proportional to $\|r(\Theta^*)\| \cdot \|J^{-1}\| \cdot \max_j \|\nabla^2 f_j\|$. For calibration problems where the model fits the data well (small residuals), the convergence is nearly quadratic. When the model is misspecified and residuals are large, convergence can be slow or the method can fail entirely -- this motivates the Levenberg-Marquardt regularization.

---

**Exercise 2.** The Levenberg-Marquardt system is $(J^\top W J + \lambda I)\Delta\Theta = -J^\top W r$. Show that for $\lambda \to \infty$, the update direction approaches $-J^\top W r / \lambda$, which is a scaled gradient descent step. Compute the LM step explicitly for the scalar case ($d = 1$, $m = 3$) with $J = (1, 2, 3)^\top$, $W = I$, $r = (0.1, -0.05, 0.2)^\top$, and $\lambda = 1$.

??? success "Solution to Exercise 2"
    **Showing the LM step approaches scaled gradient descent for large $\lambda$.**
    The LM system is

    $$
    (J^\top W J + \lambda I) \, \Delta\Theta = -J^\top W r
    $$

    For $\lambda \to \infty$, the matrix $J^\top W J + \lambda I$ is dominated by $\lambda I$:

    $$
    \Delta\Theta = -(J^\top W J + \lambda I)^{-1} J^\top W r \approx -\frac{1}{\lambda} J^\top W r
    $$

    since $(J^\top W J + \lambda I)^{-1} \to \lambda^{-1} I$ as $\lambda \to \infty$. More precisely, using the Neumann series:

    $$
    (J^\top W J + \lambda I)^{-1} = \frac{1}{\lambda}\left(I + \frac{J^\top W J}{\lambda}\right)^{-1} = \frac{1}{\lambda}\left(I - \frac{J^\top W J}{\lambda} + \mathcal{O}(\lambda^{-2})\right)
    $$

    The direction $-J^\top W r = -\nabla \mathcal{L}$ is the negative gradient of $\mathcal{L}$, so the LM step becomes a short gradient descent step with effective step size $1/\lambda$.

    **Explicit computation for the scalar case.**
    Given $d = 1$, $m = 3$, $J = (1, 2, 3)^\top$, $W = I$, $r = (0.1, -0.05, 0.2)^\top$, and $\lambda = 1$:

    $$
    J^\top W J = J^\top J = 1^2 + 2^2 + 3^2 = 14
    $$

    $$
    J^\top W r = J^\top r = 1(0.1) + 2(-0.05) + 3(0.2) = 0.1 - 0.1 + 0.6 = 0.6
    $$

    The LM equation becomes

    $$
    (14 + 1) \, \Delta\Theta = -0.6
    $$

    $$
    \Delta\Theta = -\frac{0.6}{15} = -0.04
    $$

    For comparison, the pure Gauss-Newton step ($\lambda = 0$) would be $\Delta\Theta = -0.6 / 14 \approx -0.0429$, and the pure gradient descent step ($\lambda \to \infty$) would approach $-0.6 / \lambda \to 0$. The LM step with $\lambda = 1$ is slightly smaller than the Gauss-Newton step, reflecting the regularizing effect of the damping term.

---

**Exercise 3.** The optimal finite-difference step size for computing $\partial r_j / \partial \Theta_k$ is $h^\star \sim \sqrt{\varepsilon_{\text{mach}}} \cdot |\Theta_k|$. For double precision ($\varepsilon_{\text{mach}} \approx 10^{-16}$) and $\Theta_k = 0.04$ (typical for $v_0$), compute $h^\star$. Compare the cost of computing the full Jacobian via forward finite differences ($d+1$ evaluations) versus adjoint AD ($\le 5$ evaluations) for Heston with $d = 5$ and $m = 50$.

??? success "Solution to Exercise 3"
    **Optimal finite-difference step size.**
    For $\varepsilon_{\text{mach}} \approx 10^{-16}$ and $\Theta_k = v_0 = 0.04$:

    $$
    h^* = \sqrt{\varepsilon_{\text{mach}}} \cdot |\Theta_k| = \sqrt{10^{-16}} \times 0.04 = 10^{-8} \times 0.04 = 4 \times 10^{-10}
    $$

    This is a very small perturbation. At this step size, the forward difference achieves a balance between truncation error $\mathcal{O}(h) \sim 4 \times 10^{-10}$ and round-off error $\mathcal{O}(\varepsilon_{\text{mach}} / h) \sim 10^{-16} / (4 \times 10^{-10}) = 2.5 \times 10^{-7}$, giving a total relative accuracy of approximately $\sqrt{\varepsilon_{\text{mach}}} \approx 10^{-8}$ for the derivative approximation.

    **Cost comparison for the full Jacobian ($d = 5$, $m = 50$).**

    *Forward finite differences:* Computing the full Jacobian $J \in \mathbb{R}^{50 \times 5}$ requires $d + 1 = 6$ evaluations of the pricing function (one base evaluation plus one perturbed evaluation per parameter). Each evaluation prices all $m = 50$ options via the FFT. Total cost per iteration: **6 pricing evaluations**.

    *Adjoint AD:* The adjoint (reverse-mode) differentiation computes the full gradient $\nabla_\Theta \mathcal{L}$ in a single backward pass with cost at most $C_{\text{AD}} \leq 5$ times the cost of a single forward evaluation. For least-squares, the full Jacobian can be obtained by running the adjoint once per residual component, but more efficiently, the product $J^\top W r$ (which is all LM needs) can be computed in a single backward pass. Total cost: **at most 5 equivalent pricing evaluations** for the gradient, or equivalently 1 forward + 1 backward pass.

    For Heston with $d = 5$, the cost savings from adjoint AD are modest (5 vs. 6 evaluations), because $d$ is small. The advantage of adjoint AD becomes dramatic when $d$ is larger (e.g., local volatility surface calibration with $d = 100+$, where finite differences require 101 evaluations versus $\leq 5$ for adjoint AD).

    However, even for $d = 5$, adjoint AD provides an additional benefit: **exact derivatives** (to machine precision), avoiding the step-size sensitivity of finite differences. This can improve LM convergence, particularly near the solution where the quadratic model needs to be accurate.

---

**Exercise 4.** The Nelder-Mead simplex method uses reflection, expansion, contraction, and shrink operations. For a 2D problem, sketch a simplex (triangle) and illustrate each operation geometrically. Why does the lack of convergence guarantees for $d \ge 2$ not prevent practitioners from using Nelder-Mead for SABR calibration ($d = 3$)?

??? success "Solution to Exercise 4"
    **Geometric illustration (2D case).**
    Consider a simplex (triangle) with vertices $\Theta_0$ (best), $\Theta_1$, and $\Theta_2$ (worst) in $\mathbb{R}^2$. The centroid of the best face is $\bar{\Theta} = (\Theta_0 + \Theta_1)/2$.

    - **Reflection:** $\Theta_r = \bar{\Theta} + 1 \cdot (\bar{\Theta} - \Theta_2)$ reflects the worst vertex through the centroid. Geometrically, $\Theta_r$ is the mirror image of $\Theta_2$ across the line through $\Theta_0$ and $\Theta_1$. The simplex "flips" to the other side.
    - **Expansion:** $\Theta_e = \bar{\Theta} + 2 \cdot (\Theta_r - \bar{\Theta})$ pushes $\Theta_r$ further away from the centroid. The simplex stretches in the direction of improvement, taking a larger step when the landscape is favorable.
    - **Contraction (outside):** $\Theta_c = \bar{\Theta} + 0.5 \cdot (\Theta_r - \bar{\Theta})$ is the midpoint between the centroid and the reflected point. The simplex contracts toward the centroid from the reflection side.
    - **Contraction (inside):** $\Theta_c = \bar{\Theta} - 0.5 \cdot (\bar{\Theta} - \Theta_2)$ is the midpoint between the centroid and the worst vertex. The simplex contracts inward.
    - **Shrink:** All vertices move toward the best vertex: $\Theta_i \leftarrow \Theta_0 + 0.5(\Theta_i - \Theta_0)$. The entire simplex halves in size, centered on $\Theta_0$.

    **Why lack of convergence guarantees does not prevent practical use for SABR.**
    McKinnon's counterexample shows that Nelder-Mead can converge to non-stationary points, but this pathological behavior requires carefully constructed objectives. In SABR calibration practice, the following factors mitigate the theoretical concern:

    1. **Low dimension.** SABR has only $d = 3$ parameters (with $\beta$ fixed). Nelder-Mead's simplex in 3D has 4 vertices, which is manageable and well-explored empirically. The pathological behavior is more likely in higher dimensions.
    2. **Smooth objective.** The SABR objective (sum of squared implied vol differences using Hagan's closed-form formula) is smooth and well-behaved, unlike the pathological functions in the counterexamples.
    3. **Well-conditioned problem.** With $\alpha_0$ eliminated via the ATM constraint, only 2 parameters remain. The objective is nearly quadratic near the minimum, which is the regime where Nelder-Mead performs best.
    4. **Speed.** Each Hagan formula evaluation takes microseconds. Even if Nelder-Mead takes 200--500 iterations, the total time is negligible (milliseconds). Practitioners can afford to run multiple restarts to verify the result.
    5. **Verification.** The calibrated parameters can be immediately verified by computing model implied vols and comparing to the market. Any convergence failure is immediately visible as a poor fit.

---

**Exercise 5.** Bayesian optimization with expected improvement (EI) balances exploitation and exploration. For a GP surrogate with current best $\mathcal{L}_{\min} = 0.002$, posterior mean $\mu(\Theta) = 0.0018$ and posterior standard deviation $\sigma(\Theta) = 0.001$ at a candidate point $\Theta$, compute the expected improvement. Would this point be evaluated next if an alternative point has $\mu = 0.0025$, $\sigma = 0.005$?

??? success "Solution to Exercise 5"
    **Computing the expected improvement.**
    Given $\mathcal{L}_{\min} = 0.002$, $\mu(\Theta) = 0.0018$, $\sigma(\Theta) = 0.001$:

    $$
    z = \frac{\mathcal{L}_{\min} - \mu(\Theta)}{\sigma(\Theta)} = \frac{0.002 - 0.0018}{0.001} = \frac{0.0002}{0.001} = 0.2
    $$

    The expected improvement formula gives

    $$
    \text{EI}(\Theta) = (\mathcal{L}_{\min} - \mu(\Theta)) \Phi(z) + \sigma(\Theta) \phi(z)
    $$

    where $\Phi$ is the standard normal CDF and $\phi$ is the standard normal PDF. Using standard values:

    $$
    \Phi(0.2) \approx 0.5793, \qquad \phi(0.2) = \frac{1}{\sqrt{2\pi}} e^{-0.02} \approx 0.3910
    $$

    Therefore:

    $$
    \text{EI} = 0.0002 \times 0.5793 + 0.001 \times 0.3910 = 0.0001159 + 0.0003910 = 0.0005069
    $$

    **Comparison with the alternative point.** For the alternative point with $\mu = 0.0025$, $\sigma = 0.005$:

    $$
    z' = \frac{0.002 - 0.0025}{0.005} = \frac{-0.0005}{0.005} = -0.1
    $$

    $$
    \Phi(-0.1) \approx 0.4602, \qquad \phi(-0.1) \approx 0.3970
    $$

    $$
    \text{EI}' = (-0.0005) \times 0.4602 + 0.005 \times 0.3970 = -0.0002301 + 0.001985 = 0.001755
    $$

    Since $\text{EI}' = 0.001755 > \text{EI} = 0.000507$, the alternative point would be evaluated next, not the first candidate.

    This illustrates the exploration-exploitation tradeoff: the first point has a better mean ($\mu = 0.0018 < 0.002$, already below the current best), but the second point has much higher uncertainty ($\sigma = 0.005$ vs. $0.001$). The EI acquisition function favors the uncertain point because the large $\sigma$ creates a substantial probability of a very large improvement, even though the mean prediction is worse than the current best. This is the hallmark of Bayesian optimization: it preferentially explores regions where the model is uncertain, which is essential for finding global optima.

---

**Exercise 6.** Compare the following calibration strategies for a rough volatility model where each Monte Carlo pricing evaluation takes 5 seconds: (a) Levenberg-Marquardt with finite-difference Jacobians, (b) Nelder-Mead, and (c) Bayesian optimization with 150 evaluation budget. Estimate the total wall time for each and discuss which is most suitable.

??? success "Solution to Exercise 6"
    **Cost estimates for each method with 5-second evaluations.**

    **(a) Levenberg-Marquardt with finite-difference Jacobians.**
    Each LM iteration requires $d + 1$ function evaluations for the Jacobian (where $d$ is the number of parameters in the rough volatility model; assume $d \approx 5$--$8$). With 5 seconds per evaluation:

    - Cost per iteration: $(d + 1) \times 5 = 6 \times 5 = 30$ s (for $d = 5$)
    - Typical iterations to convergence: 15--30
    - Total wall time: $30 \times 20 = 600$ s $\approx$ 10 minutes

    This is prohibitively slow for daily calibration. Moreover, finite-difference gradients are unreliable with Monte Carlo pricing because the pricing noise ($\sim 1/\sqrt{N_{\text{MC}}}$) contaminates the derivative estimate. The optimal step size analysis breaks down when the function evaluations themselves carry statistical noise of magnitude $\varepsilon_{\text{MC}} \gg \varepsilon_{\text{mach}}$.

    **(b) Nelder-Mead.**
    Nelder-Mead requires 1--2 function evaluations per iteration (reflection, possibly expansion or contraction). For $d = 5$:

    - Cost per iteration: $1 \times 5 = 5$ s (typical), occasionally $2 \times 5 = 10$ s
    - Typical iterations: 200--500
    - Total wall time: $300 \times 5 = 1{,}500$ s $\approx$ 25 minutes

    The total number of evaluations is 300--500, each taking 5 s, for a total of 25--42 minutes. Nelder-Mead is robust to noise (it uses only function values, not differences), but the convergence is slow and there are no theoretical guarantees of finding even a local minimum.

    **(c) Bayesian optimization with 150 evaluation budget.**
    Each evaluation takes 5 s, and the GP update adds overhead:

    - Evaluation cost: $150 \times 5 = 750$ s
    - GP overhead: $\mathcal{O}(n^3)$ at each step, negligible for $n = 150$ ($< 1$ s per update)
    - Total wall time: approximately $750$ s $\approx$ 12.5 minutes

    **Comparison and recommendation.**

    | Method | Evaluations | Wall time | Noise robustness |
    |--------|------------|-----------|------------------|
    | LM (FD) | 100--200 | 10 min | Poor |
    | Nelder-Mead | 300--500 | 25--42 min | Good |
    | Bayesian opt. | 150 | 12.5 min | Excellent |

    Bayesian optimization is the most suitable method for this problem. It achieves the best tradeoff between evaluation budget and solution quality because:

    1. **Sample efficiency.** BO's GP surrogate model makes optimal use of each expensive evaluation, using the full history to guide exploration. With 150 evaluations, BO typically finds solutions comparable to what Nelder-Mead finds in 300--500 evaluations.
    2. **Noise handling.** The GP naturally models observation noise through the nugget parameter, providing smoothed predictions even when individual evaluations are noisy.
    3. **Fixed budget.** The 150-evaluation budget is known in advance, making runtime predictable ($\approx$ 12.5 min), which is important for production scheduling.

    LM with finite differences should be avoided due to the noise sensitivity of the gradient estimates. If adjoint AD is available for the rough volatility model (which may be feasible through automatic differentiation frameworks like JAX), LM becomes viable again and would be the fastest option.

---

**Exercise 7.** In the global-then-local hybrid strategy, DE runs for 50 generations with $NP = 30$ to locate the global basin, then LM refines. Suppose DE terminates with best objective 0.0025 and LM converges to 0.0008 in 20 iterations. Could LM alone have reached 0.0008 from a random starting point? Design an experiment using multi-start LM to estimate the probability of reaching the same basin without DE's guidance.

??? success "Solution to Exercise 7"
    **Could LM alone have reached 0.0008 from a random starting point?**
    Possibly, but with low probability. The fact that DE converged to an objective of 0.0025 (not 0.0008) before LM refinement suggests that the global minimum lies in a narrow basin that is difficult to find without systematic exploration. LM from a random start would need to land in the correct basin by chance.

    If the objective landscape has $k$ local minima, a random starting point has probability approximately $1/k$ of landing in the global basin (assuming equal basin sizes). For Heston calibration with $k \approx 3$ basins, this gives roughly 33% probability per start. However, basins are not equally sized: the global minimum often has a smaller basin of attraction than suboptimal minima (the $(\kappa, \theta)$ ridge creates a large, flat basin that attracts many starting points).

    **Experimental design to estimate the probability.**

    *Step 1: Establish reference.*
    Run the hybrid DE-LM to convergence. Record the final parameters $\Theta^*_{\text{hybrid}}$ and objective $\mathcal{L}^*_{\text{hybrid}} = 0.0008$. This defines the "target basin."

    *Step 2: Multi-start LM experiment.*
    Sample $N = 200$ starting points uniformly from the Heston parameter bounds. For each starting point $\Theta^{(i)}_0$:

    1. Run LM to convergence with the same settings (tolerances, damping strategy) as in the hybrid.
    2. Record the final objective $\mathcal{L}^{(i)}_{\text{final}}$ and parameters $\Theta^{(i)}_{\text{final}}$.
    3. Classify the result as "same basin" if $\|\Theta^{(i)}_{\text{final}} - \Theta^*_{\text{hybrid}}\| < \delta$ and $|\mathcal{L}^{(i)}_{\text{final}} - 0.0008| < \varepsilon$, where $\delta$ and $\varepsilon$ are small tolerances (e.g., $\delta = 0.01 \cdot \|\Theta^*_{\text{hybrid}}\|$ and $\varepsilon = 0.0001$).

    *Step 3: Estimate the basin probability.*
    The fraction of the 200 starts that reach the global basin provides an estimate $\hat{p}$ of the probability. A 95% confidence interval is

    $$
    \hat{p} \pm 1.96 \sqrt{\frac{\hat{p}(1 - \hat{p})}{N}}
    $$

    *Step 4: Cluster analysis.*
    Group the 200 final parameter vectors by proximity using $k$-means or DBSCAN clustering. Each cluster represents a distinct local minimum. Record the number of clusters $k$, the objective value at each cluster center, and the fraction of starts assigned to each cluster. This provides a map of the objective landscape.

    *Step 5: Cost comparison.*
    Compute the expected number of LM starts needed to find the global basin: $N_{\text{expected}} = 1/\hat{p}$. The expected cost is $N_{\text{expected}} \times T_{\text{LM}}$. Compare with the DE-LM hybrid cost (12 s). If $\hat{p} = 0.3$ and $T_{\text{LM}} = 1$ s, then $N_{\text{expected}} \approx 3.3$ starts at 1 s each gives 3.3 s, which is less than the 12 s hybrid. But if $\hat{p} = 0.1$, then $N_{\text{expected}} = 10$ starts at 1 s each gives 10 s, comparable to the hybrid. The breakeven point is $\hat{p} = T_{\text{LM}} / T_{\text{hybrid}} = 1/12 \approx 0.08$: if the basin probability exceeds 8%, multi-start LM is cheaper on average.
