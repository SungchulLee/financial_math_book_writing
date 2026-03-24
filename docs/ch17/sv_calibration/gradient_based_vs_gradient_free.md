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

### Gauss-Newton method

For nonlinear least-squares problems, the Gauss-Newton method approximates the Hessian using only first-order information. The update solves

$$
(J^\top W J) \, \Delta\Theta = -J^\top W r
$$

The approximation $H \approx J^\top W J$ ignores second-order terms $\sum_j w_j r_j \nabla^2 f_j$, which are small when residuals are small (i.e., the model fits the data well).

**Convergence.** Near a solution $\Theta^*$ with small residuals, Gauss-Newton converges quadratically:

$$
\| \Theta^{(k+1)} - \Theta^* \| \leq C \| r(\Theta^*) \| \cdot \| \Theta^{(k)} - \Theta^* \| + \mathcal{O}(\| \Theta^{(k)} - \Theta^* \|^2)
$$

When residuals are exactly zero (perfect fit), convergence is genuinely quadratic. For calibration problems with nonzero residuals, convergence degrades to linear with rate proportional to $\| r(\Theta^*) \|$.

**Limitation.** The Gauss-Newton method can fail when $J^\top W J$ is singular or nearly so. This occurs when parameters are poorly identified by the data---a common situation in stochastic volatility calibration where $\kappa$ and $\theta$ are entangled.

### Levenberg-Marquardt algorithm

The Levenberg-Marquardt (LM) algorithm regularizes the Gauss-Newton system by adding a damping term:

$$
(J^\top W J + \lambda I) \, \Delta\Theta = -J^\top W r
$$

The damping parameter $\lambda > 0$ interpolates between two regimes:

- **Small $\lambda$** ($\lambda \to 0$): Gauss-Newton step, fast convergence near the solution.
- **Large $\lambda$** ($\lambda \to \infty$): $\Delta\Theta \approx -(\lambda)^{-1} J^\top W r$, a short gradient descent step, ensuring progress when far from the solution.

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

---

**Exercise 2.** The Levenberg-Marquardt system is $(J^\top W J + \lambda I)\Delta\Theta = -J^\top W r$. Show that for $\lambda \to \infty$, the update direction approaches $-J^\top W r / \lambda$, which is a scaled gradient descent step. Compute the LM step explicitly for the scalar case ($d = 1$, $m = 3$) with $J = (1, 2, 3)^\top$, $W = I$, $r = (0.1, -0.05, 0.2)^\top$, and $\lambda = 1$.

---

**Exercise 3.** The optimal finite-difference step size for computing $\partial r_j / \partial \Theta_k$ is $h^\star \sim \sqrt{\varepsilon_{\text{mach}}} \cdot |\Theta_k|$. For double precision ($\varepsilon_{\text{mach}} \approx 10^{-16}$) and $\Theta_k = 0.04$ (typical for $v_0$), compute $h^\star$. Compare the cost of computing the full Jacobian via forward finite differences ($d+1$ evaluations) versus adjoint AD ($\le 5$ evaluations) for Heston with $d = 5$ and $m = 50$.

---

**Exercise 4.** The Nelder-Mead simplex method uses reflection, expansion, contraction, and shrink operations. For a 2D problem, sketch a simplex (triangle) and illustrate each operation geometrically. Why does the lack of convergence guarantees for $d \ge 2$ not prevent practitioners from using Nelder-Mead for SABR calibration ($d = 3$)?

---

**Exercise 5.** Bayesian optimization with expected improvement (EI) balances exploitation and exploration. For a GP surrogate with current best $\mathcal{L}_{\min} = 0.002$, posterior mean $\mu(\Theta) = 0.0018$ and posterior standard deviation $\sigma(\Theta) = 0.001$ at a candidate point $\Theta$, compute the expected improvement. Would this point be evaluated next if an alternative point has $\mu = 0.0025$, $\sigma = 0.005$?

---

**Exercise 6.** Compare the following calibration strategies for a rough volatility model where each Monte Carlo pricing evaluation takes 5 seconds: (a) Levenberg-Marquardt with finite-difference Jacobians, (b) Nelder-Mead, and (c) Bayesian optimization with 150 evaluation budget. Estimate the total wall time for each and discuss which is most suitable.

---

**Exercise 7.** In the global-then-local hybrid strategy, DE runs for 50 generations with $NP = 30$ to locate the global basin, then LM refines. Suppose DE terminates with best objective 0.0025 and LM converges to 0.0008 in 20 iterations. Could LM alone have reached 0.0008 from a random starting point? Design an experiment using multi-start LM to estimate the probability of reaching the same basin without DE's guidance.
