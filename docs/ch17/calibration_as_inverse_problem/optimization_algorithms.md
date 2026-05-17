# Optimization Algorithms for Calibration

Calibration reduces to solving an optimization problem. The choice of algorithm profoundly affects computational cost, robustness, and the quality of the solution. This section surveys the main algorithmic approaches used in quantitative finance.

---

## The calibration optimization problem

Recall that calibration seeks

$$
\hat\theta \in \arg\min_{\theta \in \Theta} \; \mathcal{L}(\theta)
$$

where $\mathcal{L}(\theta)$ measures misfit between model prices and market data. In the weighted least-squares case,

$$
\mathcal{L}(\theta) = \frac{1}{2} \sum_{j=1}^m w_j \left( f_j(\theta) - y_j \right)^2 = \frac{1}{2} \|r(\theta)\|_W^2
$$

with residual vector $r(\theta) = (f_1(\theta) - y_1, \ldots, f_m(\theta) - y_m)^\top$.

The problem may include constraints:

$$
\min_{\theta} \; \mathcal{L}(\theta) \quad \text{subject to} \quad g_i(\theta) \le 0, \; h_j(\theta) = 0
$$

Typical constraints in finance include positivity (variances, intensities), the Feller condition, and bounds on correlation.

---

## Local optimization methods

Local methods find a minimum near a given starting point. They are fast but may converge to local minima.

### Gradient descent

The simplest approach updates parameters along the negative gradient:

$$
\theta^{(k+1)} = \theta^{(k)} - \alpha_k \nabla \mathcal{L}(\theta^{(k)})
$$

where $\alpha_k > 0$ is the step size (learning rate).

**Advantages:** Simple, low memory.

**Disadvantages:** Slow convergence, sensitive to step size, poor performance on ill-conditioned problems.

In calibration, pure gradient descent is rarely used due to the ill-conditioning inherent in inverse problems.

### Newton's method

Newton's method uses second-order information:

$$
\theta^{(k+1)} = \theta^{(k)} - H^{-1}(\theta^{(k)}) \nabla \mathcal{L}(\theta^{(k)})
$$

where $H = \nabla^2 \mathcal{L}$ is the Hessian.

**Advantages:** Quadratic convergence near a minimum.

**Disadvantages:** Requires Hessian computation and inversion; Hessian may be indefinite far from the solution.

### Gauss–Newton method

For least-squares problems, the Hessian can be approximated. Let $J(\theta) = \nabla_\theta r(\theta) \in \mathbb{R}^{m \times d}$ be the Jacobian of the residual. Then

$$
\nabla \mathcal{L} = J^\top W r, \qquad H \approx J^\top W J
$$

ignoring second-order terms in $r$. The Gauss–Newton update solves

$$
(J^\top W J) \Delta\theta = -J^\top W r
$$

and sets $\theta^{(k+1)} = \theta^{(k)} + \Delta\theta$.

**Advantages:** No Hessian computation; often effective for mildly nonlinear problems.

**Disadvantages:** May fail when $J^\top W J$ is singular or when the problem is highly nonlinear.

### Levenberg–Marquardt algorithm

The Levenberg–Marquardt (LM) algorithm interpolates between Gauss–Newton and gradient descent:

$$
(J^\top W J + \lambda I) \Delta\theta = -J^\top W r
$$

The damping parameter $\lambda \ge 0$ is adjusted adaptively (note: the LM damping $\lambda I$ is algebraically identical to Tikhonov regularization of the linearized step; see [§ Tikhonov regularization](../regularization_and_stability/tikhonov_regularization.md)):

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
\min_{\|\Delta\theta\| \le \Delta_k} \; q(\Delta\theta)
$$

where $q$ is a local quadratic model of $\mathcal{L}$ and $\Delta_k$ is the trust-region radius.

The radius is adjusted based on the ratio of actual to predicted reduction:

$$
\rho_k = \frac{\mathcal{L}(\theta^{(k)}) - \mathcal{L}(\theta^{(k)} + \Delta\theta)}{q(0) - q(\Delta\theta)}
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
   v_i = \theta_{r_1} + F(\theta_{r_2} - \theta_{r_3})
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
v_i \leftarrow \omega v_i + c_1 r_1 (p_i - \theta_i) + c_2 r_2 (g - \theta_i)
$$

$$
\theta_i \leftarrow \theta_i + v_i
$$

where $p_i$ is the particle's best position, $g$ is the global best, $\omega$ is inertia, and $c_1, c_2$ are cognitive/social parameters.

**Advantages:** Simple, parallelizable, derivative-free.

**Disadvantages:** Can be slow to converge; parameter tuning needed.

### Simulated annealing

Simulated annealing accepts worse solutions with probability

$$
P(\text{accept}) = \exp\left( -\frac{\Delta \mathcal{L}}{T} \right)
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
\|\nabla \mathcal{L}(\theta^{(k)})\| < \epsilon_g
$$

### Relative parameter change

$$
\frac{\|\theta^{(k+1)} - \theta^{(k)}\|}{\|\theta^{(k)}\| + 1} < \epsilon_\theta
$$

### Relative objective change

$$
\frac{|\mathcal{L}(\theta^{(k+1)}) - \mathcal{L}(\theta^{(k)})|}{|\mathcal{L}(\theta^{(k)})| + 1} < \epsilon_{\mathcal{L}}
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

---

## Exercises

**Exercise 1.** Starting from the weighted least-squares objective $\mathcal{L}(\theta) = \tfrac{1}{2}\|r(\theta)\|_W^2$, derive the Gauss--Newton update formula $(J^\top W J)\Delta\theta = -J^\top W r$ by expanding $\mathcal{L}(\theta + \Delta\theta)$ to second order and dropping the term involving second derivatives of $r$.

??? success "Solution to Exercise 1"
    We start with the weighted least-squares objective

    $$
    \mathcal{L}(\theta) = \frac{1}{2} r(\theta)^\top W \, r(\theta) = \frac{1}{2} \sum_{j=1}^m w_j \, r_j(\theta)^2
    $$

    where $r(\theta) = (f_1(\theta) - y_1, \ldots, f_m(\theta) - y_m)^\top$ is the residual vector and $W = \text{diag}(w_1, \ldots, w_m)$.

    Expand $r(\theta + \Delta\theta)$ to first order:

    $$
    r(\theta + \Delta\theta) \approx r(\theta) + J(\theta)\Delta\theta
    $$

    where $J(\theta) = \nabla_\theta r(\theta) \in \mathbb{R}^{m \times d}$ is the Jacobian of the residual.

    Substituting into the objective:

    $$
    \mathcal{L}(\theta + \Delta\theta) \approx \frac{1}{2}(r + J\Delta\theta)^\top W (r + J\Delta\theta)
    $$

    Expanding (suppressing the $\theta$ argument for brevity):

    $$
    \mathcal{L}(\theta + \Delta\theta) \approx \frac{1}{2} r^\top W r + r^\top W J \Delta\theta + \frac{1}{2} \Delta\theta^\top J^\top W J \Delta\theta
    $$

    This is a quadratic in $\Delta\theta$. Note that the full second-order expansion of $\mathcal{L}$ would include an additional term involving second derivatives of $r$:

    $$
    \nabla^2 \mathcal{L} = J^\top W J + \sum_{j=1}^m w_j \, r_j \, \nabla^2 r_j
    $$

    The Gauss--Newton approximation **drops** the second term $\sum_j w_j r_j \nabla^2 r_j$, which is valid when the residuals $r_j$ are small (good fit) or the functions $f_j$ are nearly linear. Under this approximation, we minimize the quadratic model:

    $$
    q(\Delta\theta) = \frac{1}{2} r^\top W r + (J^\top W r)^\top \Delta\theta + \frac{1}{2} \Delta\theta^\top (J^\top W J) \Delta\theta
    $$

    Setting the gradient to zero:

    $$
    \nabla_{\Delta\theta} \, q = J^\top W r + J^\top W J \,\Delta\theta = 0
    $$

    Solving for $\Delta\theta$:

    $$
    (J^\top W J)\Delta\theta = -J^\top W r
    $$

    This is the Gauss--Newton update formula.

---

**Exercise 2.** In the Levenberg--Marquardt algorithm, the update solves $(J^\top W J + \lambda I)\Delta\theta = -J^\top W r$. Show that as $\lambda \to \infty$, the direction $\Delta\theta$ approaches a scaled negative gradient direction $-\nabla\mathcal{L}/\lambda$, and as $\lambda \to 0$, it reduces to the Gauss--Newton step.

??? success "Solution to Exercise 2"
    The LM update solves

    $$
    (J^\top W J + \lambda I)\Delta\theta = -J^\top W r
    $$

    **Limit $\lambda \to \infty$:**

    Dividing both sides by $\lambda$:

    $$
    \left(\frac{1}{\lambda}J^\top W J + I\right)\Delta\theta = -\frac{1}{\lambda}J^\top W r
    $$

    As $\lambda \to \infty$, the term $\frac{1}{\lambda}J^\top W J \to 0$, so

    $$
    \Delta\theta \approx -\frac{1}{\lambda}J^\top W r
    $$

    Recalling that the gradient of the least-squares objective is $\nabla\mathcal{L} = J^\top W r$, we obtain

    $$
    \Delta\theta \approx -\frac{1}{\lambda}\nabla\mathcal{L}
    $$

    This is a gradient descent step with step size $1/\lambda$. As $\lambda$ increases, the step becomes smaller and more aligned with the steepest descent direction -- safe but slow.

    **Limit $\lambda \to 0$:**

    As $\lambda \to 0$, the equation becomes

    $$
    J^\top W J \,\Delta\theta = -J^\top W r
    $$

    which is precisely the Gauss--Newton update.

    **Interpolation:** For intermediate $\lambda$, the LM step smoothly interpolates between these extremes. Geometrically, the matrix $J^\top W J + \lambda I$ has eigenvalues $\sigma_k^2 + \lambda$ (where $\sigma_k$ are the singular values of $\sqrt{W}J$). The damping $\lambda$ ensures that even if some $\sigma_k$ are very small (ill-conditioned directions), the effective eigenvalues are bounded below by $\lambda$, preventing the catastrophic amplification that would occur in pure Gauss--Newton with a near-singular $J^\top W J$.

---

**Exercise 3.** Consider a calibration problem with $d = 3$ parameters and $m = 5$ market instruments. Suppose the Jacobian at the current iterate has singular values $\sigma_1 = 10$, $\sigma_2 = 0.5$, $\sigma_3 = 0.001$. Compute the condition number of $J^\top J$. If the data perturbation $\|\delta y\| = 0.01$, estimate an upper bound on the parameter perturbation $\|\delta\theta\|$ using the pseudoinverse. Explain why Levenberg--Marquardt with $\lambda > 0$ improves the situation.

??? success "Solution to Exercise 3"
    **Condition number of $J^\top J$:**

    $$
    \kappa(J^\top J) = \left(\frac{\sigma_1}{\sigma_3}\right)^2 = \left(\frac{10}{0.001}\right)^2 = (10^4)^2 = 10^8
    $$

    **Upper bound on parameter perturbation:**

    The pseudoinverse satisfies $\|J^\dagger\|_2 = 1/\sigma_3 = 1/0.001 = 1000$. For a data perturbation $\|\delta y\| = 0.01$:

    $$
    \|\delta\theta\| \le \|J^\dagger\|_2 \cdot \|\delta y\| = 1000 \times 0.01 = 10
    $$

    A data perturbation of magnitude 0.01 can induce a parameter shift of up to 10 -- an amplification factor of 1000. The amplification is entirely due to the near-zero singular value $\sigma_3 = 0.001$.

    **Why Levenberg--Marquardt improves the situation:**

    With damping parameter $\lambda > 0$, the LM update solves

    $$
    (J^\top J + \lambda I)\Delta\theta = -J^\top r
    $$

    The eigenvalues of $J^\top J + \lambda I$ are $\sigma_k^2 + \lambda$ for $k = 1, 2, 3$. The condition number becomes

    $$
    \kappa(J^\top J + \lambda I) = \frac{\sigma_1^2 + \lambda}{\sigma_3^2 + \lambda} = \frac{100 + \lambda}{10^{-6} + \lambda}
    $$

    For example, with $\lambda = 0.01$:

    $$
    \kappa = \frac{100.01}{0.01 + 10^{-6}} \approx \frac{100}{0.01} = 10^4
    $$

    compared to $10^8$ without damping. The effective inverse norm $\|(J^\top J + \lambda I)^{-1}\|_2 = 1/(\sigma_3^2 + \lambda) = 1/(10^{-6} + 0.01) \approx 100$, compared to $1/\sigma_3^2 = 10^6$ without damping. The price is a bias: the LM solution is pulled away from the Gauss--Newton direction, but this bias is small and vastly preferable to the numerical instability of the undamped problem.

---

**Exercise 4.** In differential evolution, the mutant vector is constructed as $v_i = \theta_{r_1} + F(\theta_{r_2} - \theta_{r_3})$. Explain geometrically what the mutation operator does. If the population has converged so that all members are close together, what happens to the mutation step size? How does this relate to the algorithm's ability to explore versus exploit?

??? success "Solution to Exercise 4"
    **Geometric interpretation of the mutation operator:**

    The mutant vector $v_i = \theta_{r_1} + F(\theta_{r_2} - \theta_{r_3})$ is constructed by:

    1. Computing the **difference vector** $\theta_{r_2} - \theta_{r_3}$, which points from $\theta_{r_3}$ to $\theta_{r_2}$ in parameter space.
    2. Scaling this difference by the mutation factor $F \in (0, 2]$.
    3. Adding the scaled difference to the **base vector** $\theta_{r_1}$.

    Geometrically, this creates a new candidate by taking one member of the population ($\theta_{r_1}$) and perturbing it in a direction and magnitude determined by the spread between two other members ($\theta_{r_2}$ and $\theta_{r_3}$). The mutation operator thus uses the population's own spatial distribution as a source of perturbation directions and scales.

    **When the population has converged (all members close together):**

    If $\theta_{r_2} \approx \theta_{r_3}$ for most pairs, then

    $$
    \|\theta_{r_2} - \theta_{r_3}\| \approx 0
    $$

    and the mutation step $F(\theta_{r_2} - \theta_{r_3}) \approx 0$. The mutant $v_i \approx \theta_{r_1}$, meaning almost no exploration occurs. The algorithm loses its ability to escape the current region and stalls.

    **Exploration vs. exploitation:** This is the fundamental exploration-exploitation trade-off:

    - **Early iterations** (diverse population): Large difference vectors produce large mutations, enabling exploration of distant regions of the parameter space. The algorithm can discover multiple basins of attraction.
    - **Late iterations** (converged population): Small difference vectors produce small mutations, enabling fine-tuning (exploitation) near the current best solution. However, if the population converges prematurely to a local minimum, there is no mechanism to escape.

    This self-adaptive step-size property is both a strength (no manual tuning of step sizes) and a weakness (premature convergence). Remedies include increasing the population size, restarting with fresh random members, or using variants like DE/rand-to-best that maintain diversity.

---

**Exercise 5.** A practitioner calibrates a Heston model using two approaches: (a) Levenberg--Marquardt from a single initial guess, and (b) multi-start with 50 random initializations followed by LM. Method (a) takes 0.2 seconds and achieves loss $\mathcal{L} = 0.0035$; method (b) takes 8 seconds and achieves loss $\mathcal{L} = 0.0008$. Discuss the trade-off. Under what circumstances would you prefer (a) over (b) in a production environment?

??? success "Solution to Exercise 5"
    **Quantitative comparison:**

    - **Method (a):** Single LM run, 0.2 seconds, loss = 0.0035.
    - **Method (b):** 50-start LM, 8 seconds, loss = 0.0008. Per-run average: $8/50 = 0.16$ seconds (slightly faster per run due to different convergence behavior from different starting points).

    The multi-start approach achieves a 77% reduction in loss at a 40x increase in wall-clock time.

    **Trade-off discussion:**

    The key question is whether the loss improvement matters. In implied volatility terms, the RMSE for (a) is approximately $\sqrt{2 \times 0.0035 / m}$ and for (b) approximately $\sqrt{2 \times 0.0008 / m}$. For $m = 20$ options, this is roughly 0.019 vs. 0.009, i.e., about 2 vol points vs. 1 vol point. The 1 vol point improvement from method (b) may or may not be within bid-ask spreads.

    **Circumstances favoring method (a):**

    1. **Real-time pricing / intraday recalibration:** If the model must be recalibrated hundreds of times per day (e.g., for each quote update in an automated market-making system), 0.2 seconds is acceptable but 8 seconds is prohibitive. Latency matters more than marginal fit quality.

    2. **Good initial guess available:** If yesterday's parameters or an interpolated guess is close to the true minimum, method (a) will reliably find a good local minimum. The 50-start approach adds cost without much benefit when the starting point is already in the basin of the global minimum.

    3. **Fit quality is "good enough":** If both losses are within the bid-ask noise (i.e., the model fits all options within market spreads), the additional accuracy of method (b) has no practical value.

    4. **Warm-starting:** In a streaming calibration setting, the previous calibration result serves as the initial guess, and method (a) converges quickly. Multi-start is mainly needed for the initial calibration or after regime changes.

    **Circumstances favoring method (b):**

    1. **End-of-day risk reporting:** Time is not critical; accuracy and robustness matter. The 8-second cost is negligible.
    2. **Complex loss landscape (many local minima):** If the Heston model with the given instrument set has multiple well-separated local minima, method (a) may converge to a poor one depending on initialization.
    3. **Parameter stability concerns:** The global search is more likely to find a robust, stable minimum.

---

**Exercise 6.** For the trust-region method, the ratio

$$
\rho_k = \frac{\mathcal{L}(\theta^{(k)}) - \mathcal{L}(\theta^{(k)} + \Delta\theta)}{q(0) - q(\Delta\theta)}
$$

governs the trust-region radius adjustment. Show that if the quadratic model $q$ is exact (i.e., $\mathcal{L}$ is exactly quadratic), then $\rho_k = 1$. Give an example objective function where $\rho_k < 0$ and explain what this means geometrically.

??? success "Solution to Exercise 6"
    **Showing $\rho_k = 1$ when $\mathcal{L}$ is exactly quadratic:**

    If $\mathcal{L}$ is exactly quadratic, then

    $$
    \mathcal{L}(\theta) = \frac{1}{2}\theta^\top A \theta + b^\top \theta + c
    $$

    for some positive definite matrix $A$, vector $b$, and constant $c$. The quadratic model $q(\Delta\theta)$ used in the trust-region method is the second-order Taylor expansion of $\mathcal{L}$ around $\theta^{(k)}$:

    $$
    q(\Delta\theta) = \mathcal{L}(\theta^{(k)}) + \nabla\mathcal{L}(\theta^{(k)})^\top \Delta\theta + \frac{1}{2}\Delta\theta^\top \nabla^2\mathcal{L}(\theta^{(k)}) \Delta\theta
    $$

    When $\mathcal{L}$ is exactly quadratic, the Taylor expansion is exact with no remainder:

    $$
    \mathcal{L}(\theta^{(k)} + \Delta\theta) = q(\Delta\theta)
    $$

    Therefore:

    $$
    \rho_k = \frac{\mathcal{L}(\theta^{(k)}) - \mathcal{L}(\theta^{(k)} + \Delta\theta)}{q(0) - q(\Delta\theta)} = \frac{\mathcal{L}(\theta^{(k)}) - q(\Delta\theta)}{\mathcal{L}(\theta^{(k)}) - q(\Delta\theta)} = 1
    $$

    since $q(0) = \mathcal{L}(\theta^{(k)})$.

    **Example where $\rho_k < 0$:**

    Consider the one-dimensional objective

    $$
    \mathcal{L}(\theta) = \theta^2 + 10\sin^2(\theta)
    $$

    At $\theta^{(k)} = \pi$, we have $\mathcal{L}(\pi) = \pi^2 + 0 \approx 9.87$. The gradient and Hessian at $\pi$ are:

    $$
    \nabla\mathcal{L}(\pi) = 2\pi + 10\sin(2\pi) = 2\pi
    $$

    $$
    \nabla^2\mathcal{L}(\pi) = 2 + 20\cos(2\pi) = 22
    $$

    The quadratic model predicts a decrease for a step in the direction of the negative gradient. Taking $\Delta\theta = -1$, the model predicts:

    $$
    q(-1) = \mathcal{L}(\pi) - 2\pi + \frac{22}{2} = 9.87 - 6.28 + 11 = 14.59
    $$

    So the predicted reduction is $q(0) - q(-1) = 9.87 - 14.59 < 0$; the model actually predicts an increase for this step direction. Instead, take $\Delta\theta = -0.5$ (toward the minimum of $q$):

    $$
    q(-0.5) = 9.87 - \pi + 2.75 \approx 9.48
    $$

    The model predicts a reduction of $\approx 0.39$. But the actual value is $\mathcal{L}(\pi - 0.5) = (\pi - 0.5)^2 + 10\sin^2(\pi - 0.5) = 6.97 + 10(0.2298) = 9.27$, giving an actual reduction of $0.60$. Here $\rho_k > 0$.

    For $\rho_k < 0$ more directly, consider a large step $\Delta\theta = -1.8$. The quadratic model predicts:

    $$
    q(-1.8) = 9.87 - 2\pi(1.8) + \frac{22(1.8)^2}{2} \approx 9.87 - 11.31 + 35.64 = 34.20
    $$

    The model predicts an increase (since the step exceeds the model's minimizer), so this is not a step the trust-region would take. The key insight is that $\rho_k < 0$ occurs when the trust region is too large and the step overshoots into a region where the actual objective increases but the quadratic model predicted a decrease. A concrete scenario: at a point where the local curvature is small but positive, the quadratic model predicts a gentle decrease over a large step, but the actual function has a bump (local maximum) in that direction, causing the objective to increase.

    **Geometric meaning of $\rho_k < 0$:** The actual objective **increased** despite the quadratic model predicting a decrease. The model is so poor that the step goes "uphill." The trust-region algorithm responds by **shrinking** the trust radius $\Delta_k$ significantly and rejecting the step, forcing a smaller step where the quadratic approximation is more reliable.

---

**Exercise 7.** You need to calibrate a model where each function evaluation requires a Monte Carlo simulation costing 2 seconds. The parameter space has $d = 5$ dimensions. Compare the expected wall-clock time for: (a) Nelder--Mead with at most 500 evaluations, (b) differential evolution with population size 30 and 100 generations, and (c) Bayesian optimization with 200 evaluations. Which method would you choose and why? How would access to 16 parallel cores change your answer?

??? success "Solution to Exercise 7"
    **Wall-clock time comparison (serial execution):**

    Each function evaluation costs 2 seconds.

    **(a) Nelder--Mead:** At most 500 evaluations, and Nelder--Mead is inherently sequential (each new simplex vertex depends on the previous evaluation).

    $$
    T_a = 500 \times 2 = 1000 \text{ seconds} \approx 16.7 \text{ minutes}
    $$

    **(b) Differential evolution:** Population size $N_p = 30$, 100 generations. Each generation evaluates up to $N_p$ trial vectors, so the total evaluations are at most $30 \times 100 = 3000$.

    $$
    T_b = 3000 \times 2 = 6000 \text{ seconds} = 100 \text{ minutes}
    $$

    **(c) Bayesian optimization:** 200 evaluations. Each evaluation is sequential (the acquisition function must be updated after each observation), plus there is overhead for fitting the Gaussian process (typically $O(n^3)$ where $n$ is the number of observations so far).

    $$
    T_c = 200 \times 2 + \text{GP overhead} \approx 400 + \text{overhead} \approx 450 \text{ seconds} \approx 7.5 \text{ minutes}
    $$

    The GP overhead is modest for 200 points in 5 dimensions (a few seconds per iteration).

    **Serial ranking:** Bayesian optimization (7.5 min) < Nelder--Mead (17 min) < Differential evolution (100 min).

    **Which method to choose (serial):** Bayesian optimization is the clear winner: fewest evaluations, best sample efficiency for expensive black-box functions, and the GP surrogate provides uncertainty estimates. The 200 evaluations in $d = 5$ dimensions give roughly $200/5 = 40$ evaluations per dimension, which is adequate for a smooth landscape.

    **With 16 parallel cores:**

    Parallelization changes the calculus dramatically:

    **(a) Nelder--Mead:** Inherently sequential. At best, one can parallelize the function evaluations within a single reflection/expansion step, but this gives limited speedup (at most a few evaluations in parallel per step). Effective speedup: $\sim 2$--$3\times$.

    $$
    T_a^{\text{parallel}} \approx 500 \text{ seconds} \approx 8 \text{ minutes}
    $$

    **(b) Differential evolution:** Embarrassingly parallel within each generation -- all 30 trial evaluations can run simultaneously. With 16 cores, each generation takes $\lceil 30/16 \rceil \times 2 = 4$ seconds (2 batches of 16 and 14).

    $$
    T_b^{\text{parallel}} = 100 \times 4 = 400 \text{ seconds} \approx 6.7 \text{ minutes}
    $$

    **(c) Bayesian optimization:** Standard BO is sequential by nature (evaluate one point, update GP, select next). Batch BO variants (e.g., q-EI, Thompson sampling) can propose multiple points per iteration. With batch size 16, we need $\lceil 200/16 \rceil = 13$ rounds:

    $$
    T_c^{\text{parallel}} = 13 \times 2 + \text{GP overhead} \approx 30 + \text{overhead} \approx 60 \text{ seconds} \approx 1 \text{ minute}
    $$

    However, batch BO is less sample-efficient than sequential BO, so more total evaluations may be needed. A realistic estimate is $\sim$2--3 minutes.

    **Parallel ranking:** Bayesian optimization (1--3 min) $\approx$ Differential evolution (6.7 min) < Nelder--Mead (8 min).

    **Recommendation with parallelism:** Differential evolution becomes very competitive because it naturally exploits parallelism with no algorithmic compromise, and its global search capability addresses the multi-modality concern. For $d = 5$ with 16 cores, DE at 6.7 minutes provides a thorough global search. Batch Bayesian optimization is fastest but requires more sophisticated implementation. A practical hybrid strategy is: run DE (or multi-start local) to identify the basin of the global minimum, then refine with a local method.
