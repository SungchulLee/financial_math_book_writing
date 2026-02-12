# Optimization Algorithms for Calibration

Calibration reduces to solving an optimization problem. The choice of algorithm profoundly affects computational cost, robustness, and the quality of the solution. This section surveys the main algorithmic approaches used in quantitative finance.

---

## The calibration optimization problem

Recall that calibration seeks

$$
\hat\theta \in \arg\min_{\theta \in \Theta} \; \mathcal{L}(\theta),
$$

where $\mathcal{L}(\theta)$ measures misfit between model prices and market data. In the weighted least-squares case,

$$
\mathcal{L}(\theta) = \frac{1}{2} \sum_{j=1}^m w_j \left( f_j(\theta) - y_j \right)^2 = \frac{1}{2} \|r(\theta)\|_W^2,
$$

with residual vector $r(\theta) = (f_1(\theta) - y_1, \ldots, f_m(\theta) - y_m)^\top$.

The problem may include constraints:

$$
\min_{\theta} \; \mathcal{L}(\theta) \quad \text{subject to} \quad g_i(\theta) \le 0, \; h_j(\theta) = 0.
$$

Typical constraints in finance include positivity (variances, intensities), the Feller condition, and bounds on correlation.

---

## Local optimization methods

Local methods find a minimum near a given starting point. They are fast but may converge to local minima.

### Gradient descent

The simplest approach updates parameters along the negative gradient:

$$
\theta^{(k+1)} = \theta^{(k)} - \alpha_k \nabla \mathcal{L}(\theta^{(k)}),
$$

where $\alpha_k > 0$ is the step size (learning rate).

**Advantages:** Simple, low memory.

**Disadvantages:** Slow convergence, sensitive to step size, poor performance on ill-conditioned problems.

In calibration, pure gradient descent is rarely used due to the ill-conditioning inherent in inverse problems.

### Newton's method

Newton's method uses second-order information:

$$
\theta^{(k+1)} = \theta^{(k)} - H^{-1}(\theta^{(k)}) \nabla \mathcal{L}(\theta^{(k)}),
$$

where $H = \nabla^2 \mathcal{L}$ is the Hessian.

**Advantages:** Quadratic convergence near a minimum.

**Disadvantages:** Requires Hessian computation and inversion; Hessian may be indefinite far from the solution.

### Gauss–Newton method

For least-squares problems, the Hessian can be approximated. Let $J(\theta) = \nabla_\theta r(\theta) \in \mathbb{R}^{m \times d}$ be the Jacobian of the residual. Then

$$
\nabla \mathcal{L} = J^\top W r, \qquad H \approx J^\top W J,
$$

ignoring second-order terms in $r$. The Gauss–Newton update solves

$$
(J^\top W J) \Delta\theta = -J^\top W r,
$$

and sets $\theta^{(k+1)} = \theta^{(k)} + \Delta\theta$.

**Advantages:** No Hessian computation; often effective for mildly nonlinear problems.

**Disadvantages:** May fail when $J^\top W J$ is singular or when the problem is highly nonlinear.

### Levenberg–Marquardt algorithm

The Levenberg–Marquardt (LM) algorithm interpolates between Gauss–Newton and gradient descent:

$$
(J^\top W J + \lambda I) \Delta\theta = -J^\top W r.
$$

The damping parameter $\lambda \ge 0$ is adjusted adaptively:

- Large $\lambda$: behaves like gradient descent (safe but slow).
- Small $\lambda$: behaves like Gauss–Newton (fast near a minimum).

**Typical update rule:**

1. Compute trial step $\Delta\theta$ with current $\lambda$.
2. If $\mathcal{L}(\theta + \Delta\theta) < \mathcal{L}(\theta)$: accept step, decrease $\lambda$.
3. Else: reject step, increase $\lambda$.

**Advantages:** Robust, widely used, good convergence properties.

**Disadvantages:** Requires Jacobian; may still converge to local minima.

Levenberg–Marquardt is the **standard workhorse** for calibration in quantitative finance.

### Trust-region methods

Trust-region methods constrain the step size rather than the direction. At each iteration, solve

$$
\min_{\|\Delta\theta\| \le \Delta_k} \; q(\Delta\theta),
$$

where $q$ is a local quadratic model of $\mathcal{L}$ and $\Delta_k$ is the trust-region radius.

The radius is adjusted based on the ratio of actual to predicted reduction:

$$
\rho_k = \frac{\mathcal{L}(\theta^{(k)}) - \mathcal{L}(\theta^{(k)} + \Delta\theta)}{q(0) - q(\Delta\theta)}.
$$

- $\rho_k \approx 1$: good model, expand trust region.
- $\rho_k$ small or negative: poor model, shrink trust region.

**Advantages:** More robust than line-search methods; handles indefinite Hessians gracefully.

**Disadvantages:** More complex implementation.

---

## Global optimization methods

Local methods can get trapped in local minima. Global methods explore the parameter space more broadly.

### Multi-start local optimization

The simplest global strategy:

1. Sample $N$ initial points from $\Theta$ (random, Latin hypercube, Sobol).
2. Run local optimization from each.
3. Return the best solution found.

**Advantages:** Simple, parallelizable, leverages efficient local solvers.

**Disadvantages:** No guarantee of finding the global minimum; cost scales with $N$.

### Differential evolution

Differential evolution (DE) is a population-based evolutionary algorithm:

1. Initialize a population of $N_p$ candidate solutions.
2. For each candidate $\theta_i$, create a mutant:
   $$
   v_i = \theta_{r_1} + F(\theta_{r_2} - \theta_{r_3}),
   $$
   where $r_1, r_2, r_3$ are distinct random indices and $F \in (0, 2]$ is the mutation factor.
3. Crossover: mix components of $v_i$ and $\theta_i$ to form trial vector $u_i$.
4. Selection: replace $\theta_i$ with $u_i$ if $\mathcal{L}(u_i) < \mathcal{L}(\theta_i)$.
5. Repeat until convergence.

**Advantages:** Derivative-free, good at escaping local minima, handles constraints naturally.

**Disadvantages:** Many function evaluations; tuning required ($F$, crossover rate, population size).

### Particle swarm optimization

Particle swarm optimization (PSO) maintains a swarm of particles, each with position $\theta_i$ and velocity $v_i$:

$$
v_i \leftarrow \omega v_i + c_1 r_1 (p_i - \theta_i) + c_2 r_2 (g - \theta_i),
$$
$$
\theta_i \leftarrow \theta_i + v_i,
$$

where $p_i$ is the particle's best position, $g$ is the global best, $\omega$ is inertia, and $c_1, c_2$ are cognitive/social parameters.

**Advantages:** Simple, parallelizable, derivative-free.

**Disadvantages:** Can be slow to converge; parameter tuning needed.

### Simulated annealing

Simulated annealing accepts worse solutions with probability

$$
P(\text{accept}) = \exp\left( -\frac{\Delta \mathcal{L}}{T} \right),
$$

where $T$ is the temperature, which decreases over time (cooling schedule).

**Advantages:** Can escape local minima; simple to implement.

**Disadvantages:** Slow; cooling schedule is problem-dependent.

### Basin hopping

Basin hopping combines local optimization with random perturbations:

1. Start at $\theta^{(0)}$; run local minimization to get $\tilde\theta^{(0)}$.
2. Perturb: $\theta' = \tilde\theta^{(k)} + \xi$, where $\xi$ is random.
3. Run local minimization from $\theta'$ to get $\tilde\theta'$.
4. Accept $\tilde\theta^{(k+1)} = \tilde\theta'$ with Metropolis criterion.
5. Repeat.

**Advantages:** Efficient exploration of multiple basins; leverages fast local solvers.

**Disadvantages:** Still requires many function evaluations.

---

## Derivative-free methods

When gradients are unavailable or unreliable (e.g., Monte Carlo pricing with noise), derivative-free methods are essential.

### Nelder–Mead simplex

Maintains a simplex of $d+1$ points and iteratively reflects, expands, contracts, or shrinks based on function values.

**Advantages:** No derivatives needed; simple.

**Disadvantages:** Can be slow; may converge to non-stationary points.

### Powell's method

Performs sequential one-dimensional optimizations along conjugate directions.

**Advantages:** Often faster than Nelder–Mead.

**Disadvantages:** Still requires many function evaluations.

### Bayesian optimization

Models $\mathcal{L}(\theta)$ with a Gaussian process and selects the next evaluation point by maximizing an acquisition function (e.g., expected improvement).

**Advantages:** Sample-efficient; good for expensive black-box functions.

**Disadvantages:** Scales poorly with dimension; overhead in GP fitting.

---

## Handling constraints

### Box constraints

Simple bounds $\theta_{\min} \le \theta \le \theta_{\max}$ are handled by:

- Projection after each step.
- Barrier methods (interior point).
- Transformation: $\theta = \theta_{\min} + (\theta_{\max} - \theta_{\min}) \sigma(\phi)$, where $\sigma$ is sigmoid.

### General constraints

For inequality constraints $g_i(\theta) \le 0$:

- **Penalty methods:** Add $\mu \sum_i \max(0, g_i(\theta))^2$ to the objective.
- **Augmented Lagrangian:** Combines penalties with Lagrange multipliers.
- **Interior point (barrier) methods:** Add $-\mu \sum_i \log(-g_i(\theta))$.
- **Sequential quadratic programming (SQP):** Solves a sequence of QP subproblems.

---

## Convergence diagnostics

Reliable stopping criteria are essential:

### Gradient norm

$$
\|\nabla \mathcal{L}(\theta^{(k)})\| < \epsilon_g.
$$

### Relative parameter change

$$
\frac{\|\theta^{(k+1)} - \theta^{(k)}\|}{\|\theta^{(k)}\| + 1} < \epsilon_\theta.
$$

### Relative objective change

$$
\frac{|\mathcal{L}(\theta^{(k+1)}) - \mathcal{L}(\theta^{(k)})|}{|\mathcal{L}(\theta^{(k)})| + 1} < \epsilon_{\mathcal{L}}.
$$

### Maximum iterations

A hard cap prevents infinite loops but should not be the primary criterion.

### Practical recommendations

- Use multiple criteria (gradient *and* parameter change).
- Monitor the objective function history for oscillation or stagnation.
- For global methods, track the best solution found and its stability.

---

## Computational cost considerations

The cost of calibration depends on:

1. **Cost per function evaluation:** This varies dramatically:
   - Closed-form (Black–Scholes): $O(1)$ per option.
   - Semi-analytic (Heston via FFT): $O(N_{\text{FFT}})$ per maturity slice.
   - Monte Carlo: $O(N_{\text{paths}} \times N_{\text{steps}})$.
   - PDE methods: $O(N_x \times N_t)$ per option.

2. **Number of evaluations:** Local methods may need $O(10^2)$ evaluations; global methods may need $O(10^4)$ or more.

3. **Parallelization:** Many global methods (DE, PSO, multi-start) are embarrassingly parallel.

**Rule of thumb:** Use local methods (LM, trust-region) when a good initial guess is available and function evaluations are cheap. Use global methods when the landscape is complex or initialization is uncertain.

---

## Algorithm selection guidelines

| Scenario | Recommended algorithm |
|----------|----------------------|
| Good initial guess, smooth objective | Levenberg–Marquardt |
| Unknown initialization, few parameters | Multi-start + LM |
| Many local minima, moderate dimension | Differential evolution |
| Expensive function (Monte Carlo) | Bayesian optimization or multi-start |
| Noisy gradients | Derivative-free (Nelder–Mead, Powell) |
| Constrained problem | SQP or interior point |

---

## Key takeaways

- Levenberg–Marquardt is the standard for smooth, unconstrained calibration.
- Global methods are necessary when the loss landscape has multiple minima.
- Derivative-free methods are required for Monte Carlo-based pricing.
- Convergence diagnostics should combine multiple criteria.
- Computational cost depends heavily on the pricing method.

---

## Further reading

- Nocedal & Wright, *Numerical Optimization*.
- Conn, Gould & Toint, *Trust-Region Methods*.
- Storn & Price, "Differential Evolution" (1997).
- Jones, Schonlau & Welch, "Efficient Global Optimization" (Bayesian optimization).
- Press et al., *Numerical Recipes* (practical implementations).
