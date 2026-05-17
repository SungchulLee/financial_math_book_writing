# Differential Evolution and Global Optimization

The Heston calibration objective function is **non-convex** with multiple local minima, parameter ridges, and flat regions. Gradient-based optimizers such as Levenberg-Marquardt or BFGS can converge rapidly near a minimum, but they require a good starting point and frequently get trapped in suboptimal basins. **Differential evolution** (DE), a population-based stochastic optimizer introduced by Storn and Price (1997), explores the parameter space globally without requiring gradient information. This makes DE the standard first-stage optimizer for Heston calibration, often followed by a local refinement step.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Describe the mutation, crossover, and selection operators of the DE algorithm and explain their roles
    2. Map the five Heston parameters to bounded search intervals with appropriate constraint handling
    3. Implement DE for Heston calibration with the Feller condition enforced as a penalty or constraint
    4. Design a hybrid global-local optimization strategy that combines DE with gradient-based refinement

!!! tip "Prerequisites"
    This section builds on the [objective function design](objective_function_design.md) for the calibration loss function and the [Heston SDE and parameters](../model_definition/heston_sde_and_parameters.md) for parameter interpretations and constraints.

---

## Why Global Optimization Is Necessary

The five-dimensional Heston parameter space $\Theta = (v_0, \kappa, \theta, \xi, \rho)$ produces a calibration landscape with several pathological features:

1. **Multiple local minima**: Different parameter combinations can fit the ATM volatility equally well while disagreeing on the smile wings. A gradient-based search starting from a poor initial guess converges to the nearest local minimum, which may produce large IV errors on OTM options.

2. **Ridge structure**: The $\kappa$-$\theta$ degeneracy (only the product $\kappa\theta$ is well-identified from short-maturity data) creates an elongated valley where the objective function varies slowly. Gradient methods take many small steps along such ridges.

3. **Flat regions**: When the Feller condition $2\kappa\theta \geq \xi^2$ is violated, the variance process touches zero frequently, and the model prices become insensitive to small parameter changes. The gradient nearly vanishes, stalling local optimizers.

These features motivate a global search that samples diverse regions of the parameter space before refining.

---

## The Differential Evolution Algorithm

DE maintains a **population** of $N_p$ candidate solutions (parameter vectors) and evolves them over generations using three operators: mutation, crossover, and selection. Unlike gradient descent, DE uses only objective function values---no derivatives are needed.

### Initialization

Generate $N_p$ vectors uniformly in the bounded search space:

$$
\Theta_i^{(0)} = \Theta^{\text{lo}} + U_i \odot (\Theta^{\text{hi}} - \Theta^{\text{lo}}), \qquad i = 1, \ldots, N_p
$$

where $U_i \in [0,1]^5$ is a random vector, $\odot$ denotes element-wise multiplication, and $\Theta^{\text{lo}}, \Theta^{\text{hi}}$ are the lower and upper bounds. Recall (see [§ Heston SDE and Parameters](../model_definition/heston_sde_and_parameters.md)) for parameter interpretations; typical calibration bounds are $v_0 \in [0.001, 1]$, $\kappa \in [0.01, 10]$, $\theta \in [0.001, 1]$, $\xi \in [0.01, 3]$, $\rho \in [-0.99, 0.99]$.

A population size of $N_p = 10 \times d = 50$ (where $d = 5$ is the dimension) provides a reasonable trade-off between exploration and computational cost.

### Mutation

For each target vector $\Theta_i^{(g)}$ in generation $g$, DE constructs a **mutant vector** $\mathbf{V}_i^{(g)}$ by combining other population members. The most common variant, **DE/rand/1**, selects three distinct random indices $r_1, r_2, r_3 \neq i$ and computes:

$$
\mathbf{V}_i^{(g)} = \Theta_{r_1}^{(g)} + F \cdot \left( \Theta_{r_2}^{(g)} - \Theta_{r_3}^{(g)} \right)
$$

where $F \in (0, 2]$ is the **mutation scale factor** (also called the differential weight). The difference vector $\Theta_{r_2} - \Theta_{r_3}$ provides a self-adaptive step size: when the population is spread out, mutations are large; as the population converges, mutations shrink automatically.

Other common variants include:

- **DE/best/1**: $\mathbf{V}_i = \Theta_{\text{best}}^{(g)} + F(\Theta_{r_1}^{(g)} - \Theta_{r_2}^{(g)})$, which biases search toward the current best solution
- **DE/rand/2**: adds a second difference vector for stronger perturbation
- **DE/current-to-best/1**: $\mathbf{V}_i = \Theta_i^{(g)} + F(\Theta_{\text{best}}^{(g)} - \Theta_i^{(g)}) + F(\Theta_{r_1}^{(g)} - \Theta_{r_2}^{(g)})$

For Heston calibration, **DE/best/1** often converges faster because it exploits the current best fit, while **DE/rand/1** provides more robust global exploration.

### Crossover

The mutant vector $\mathbf{V}_i$ is combined with the target vector $\Theta_i^{(g)}$ via **binomial crossover** to produce a trial vector $\mathbf{U}_i^{(g)}$. For each component $j = 1, \ldots, d$:

$$
U_{i,j}^{(g)} = \begin{cases} V_{i,j}^{(g)} & \text{if } \text{rand}_j \leq CR \text{ or } j = j_{\text{rand}} \\ \Theta_{i,j}^{(g)} & \text{otherwise} \end{cases}
$$

where $CR \in [0, 1]$ is the **crossover probability** and $j_{\text{rand}}$ is a randomly chosen index that ensures at least one component comes from the mutant. Higher $CR$ means more components are inherited from the mutant (more exploration); lower $CR$ preserves more of the current solution (more exploitation).

Typical settings for Heston calibration: $F = 0.8$, $CR = 0.9$.

### Selection

The trial vector replaces the target only if it achieves a lower objective value:

$$
\Theta_i^{(g+1)} = \begin{cases} \mathbf{U}_i^{(g)} & \text{if } \mathcal{L}(\mathbf{U}_i^{(g)}) \leq \mathcal{L}(\Theta_i^{(g)}) \\ \Theta_i^{(g)} & \text{otherwise} \end{cases}
$$

This **greedy selection** ensures the objective function value of each population member never increases, guaranteeing monotonic improvement of the best solution across generations.

---

## Constraint Handling for Heston Parameters

The Heston parameter space has both **box constraints** (each parameter within its bounds) and the **Feller condition** $2\kappa\theta \geq \xi^2$ as a nonlinear inequality constraint.

### Box Constraints

If a mutant or trial vector component falls outside its bounds, apply **bounce-back**:

$$
V_{i,j} = \begin{cases} \Theta_j^{\text{lo}} + \text{rand} \cdot (\Theta_{i,j}^{(g)} - \Theta_j^{\text{lo}}) & \text{if } V_{i,j} < \Theta_j^{\text{lo}} \\[4pt] \Theta_j^{\text{hi}} - \text{rand} \cdot (\Theta_j^{\text{hi}} - \Theta_{i,j}^{(g)}) & \text{if } V_{i,j} > \Theta_j^{\text{hi}} \end{cases}
$$

This places the repaired component between the violated bound and the current target, preserving the direction of the mutation.

### Feller Condition as Penalty

Recall (see [§ Variance Dynamics (CIR/Feller)](../variance_dynamics/cir_variance_process_solution.md)): the Feller condition $2\kappa\theta \geq \xi^2$ ensures the variance process stays strictly positive. Rather than enforcing it strictly (which can produce worse fits, since many market-calibrated parameters violate Feller), add a **soft penalty**:

$$
\mathcal{L}_{\text{pen}}(\Theta) = \mathcal{L}(\Theta) + \mu \cdot \max\bigl(0, \, \xi^2 - 2\kappa\theta\bigr)^2
$$

with $\mu$ typically in $[10, 100]$.

---

## Convergence and Stopping Criteria

DE converges when the population contracts to a small region around the global minimum. Common stopping criteria include:

1. **Maximum generations**: $g_{\max} = 200$--$500$ is typical for Heston calibration
2. **Objective tolerance**: stop when $\max_i \mathcal{L}(\Theta_i^{(g)}) - \min_i \mathcal{L}(\Theta_i^{(g)}) < \epsilon_{\text{tol}}$
3. **Parameter tolerance**: stop when $\max_{i,j}|\Theta_{i,j}^{(g)} - \Theta_{\text{best},j}^{(g)}| < \delta_{\text{tol}}$

### Convergence Rate

DE does not have a provable convergence rate in the classical optimization sense. Empirically, for Heston calibration with $N_p = 50$, DE typically reaches a neighborhood of the global minimum within 100--200 generations, requiring $N_p \times g_{\max} = 5{,}000$--$10{,}000$ objective function evaluations. Each evaluation requires $M$ Fourier inversions (one per option), so the total cost is $\mathcal{O}(M \cdot N_p \cdot g_{\max})$.

---

## Hybrid DE + Local Search

The standard practice is a **two-stage** optimization:

1. **Stage 1 (global)**: Run DE for 100--300 generations to locate the basin of the global minimum. The result $\Theta_{\text{DE}}$ is accurate to perhaps 2--3 significant digits.

2. **Stage 2 (local)**: Starting from $\Theta_{\text{DE}}$, run a gradient-based optimizer (Levenberg-Marquardt, L-BFGS-B, or Nelder-Mead) to refine the solution to machine precision.

The local stage converges quadratically (for Levenberg-Marquardt) or superlinearly (for L-BFGS-B), typically requiring only 20--50 additional evaluations to reduce the objective by several more orders of magnitude.

!!! note "Jacobian for Local Refinement"
    Levenberg-Marquardt requires the Jacobian $J_{ij} = \partial e_i / \partial \Theta_j$ where $e_i = C_i^{\text{mod}} - C_i^{\text{mkt}}$ (or the IV analog). This can be computed by finite differences (bumping each parameter and repricing) or by differentiating the characteristic function analytically with respect to each parameter.

---

## Worked Example

Consider calibrating to $M = 20$ options with the vega-weighted objective from the [previous section](objective_function_design.md).

**Setup**: $N_p = 50$, $F = 0.8$, $CR = 0.9$, DE/best/1 strategy, $g_{\max} = 200$.

**Generation 0**: Initialize 50 random parameter vectors in the Heston bounds. Evaluate all 50 objective values. The best initial vector has $\mathcal{L} = 3.2 \times 10^{-2}$ (poor fit, corresponding to IVRMSE $\approx$ 4 vol points).

**Generation 50**: The population has clustered around two basins. The best member has $\mathcal{L} = 8.7 \times 10^{-4}$ (IVRMSE $\approx$ 0.7 vol points). Parameters: $v_0 = 0.042$, $\kappa = 1.8$, $\theta = 0.038$, $\xi = 0.42$, $\rho = -0.71$.

**Generation 150**: The population has converged to a single basin. Best: $\mathcal{L} = 2.1 \times 10^{-4}$ (IVRMSE $\approx$ 0.3 vol points). Parameters: $v_0 = 0.0401$, $\kappa = 2.05$, $\theta = 0.0395$, $\xi = 0.38$, $\rho = -0.68$.

**Local refinement**: Starting from the DE solution, Nelder-Mead converges in 35 iterations to $\mathcal{L} = 1.8 \times 10^{-4}$. The parameters change only in the third or fourth significant digit.

**Total cost**: $50 \times 200 + 35 = 10{,}035$ objective evaluations, each requiring 20 Fourier inversions. On modern hardware, this completes in under 10 seconds using vectorized COS or FFT pricing.

---

## Practical Recommendations

!!! tip "Tuning Guidelines for Heston DE Calibration"

    1. **Population size**: Use $N_p = 10d$ to $15d$ where $d = 5$. Larger populations improve robustness but increase cost linearly.
    2. **Mutation factor**: $F \in [0.5, 1.0]$. Lower $F$ favors exploitation; higher $F$ favors exploration.
    3. **Crossover rate**: $CR \in [0.7, 0.95]$. High $CR$ works well when all parameters interact strongly (as in Heston).
    4. **Strategy**: DE/best/1 for speed; DE/rand/1 for robustness. Start with DE/best/1 and switch to DE/rand/1 if results are inconsistent across runs.
    5. **Seeding**: Include yesterday's calibrated parameters in the initial population to warm-start the search.
    6. **Parallelism**: Objective evaluations within a generation are independent and can be parallelized across cores.

---

## Summary

Differential evolution provides a robust, derivative-free global search for the non-convex Heston calibration problem. The algorithm's three operators---mutation (exploration via difference vectors), crossover (mixing of parent and mutant components), and greedy selection (monotonic improvement)---enable it to escape local minima that trap gradient-based methods. For Heston calibration, typical settings of $N_p = 50$, $F = 0.8$, $CR = 0.9$ with a DE/best/1 strategy converge in 100--200 generations. A hybrid approach using DE for global search followed by Levenberg-Marquardt or Nelder-Mead for local polishing achieves both robustness and precision at acceptable computational cost.

---

## Exercises

**Exercise 1.**
Consider a DE population of $N_p = 50$ in the five-dimensional Heston parameter space. At generation $g$, the best member is $\Theta_{\text{best}} = (0.04, 2.0, 0.04, 0.5, -0.7)$ and two randomly selected members are $\Theta_{r_1} = (0.03, 1.5, 0.03, 0.4, -0.6)$ and $\Theta_{r_2} = (0.05, 2.5, 0.05, 0.6, -0.8)$. Compute the mutant vector $\mathbf{V}_i$ using the DE/best/1 strategy with mutation factor $F = 0.8$. Verify that all components lie within the standard Heston bounds, and apply the bounce-back rule to any that do not.

??? success "Solution to Exercise 1"
    The DE/best/1 mutation formula is:

    $$
    \mathbf{V}_i = \Theta_{\text{best}}^{(g)} + F \cdot (\Theta_{r_1}^{(g)} - \Theta_{r_2}^{(g)})
    $$

    With $\Theta_{\text{best}} = (0.04, 2.0, 0.04, 0.5, -0.7)$, $\Theta_{r_1} = (0.03, 1.5, 0.03, 0.4, -0.6)$, $\Theta_{r_2} = (0.05, 2.5, 0.05, 0.6, -0.8)$, and $F = 0.8$:

    First, compute the difference vector:

    $$
    \Theta_{r_1} - \Theta_{r_2} = (0.03 - 0.05,\; 1.5 - 2.5,\; 0.03 - 0.05,\; 0.4 - 0.6,\; -0.6 - (-0.8))
    $$

    $$
    = (-0.02,\; -1.0,\; -0.02,\; -0.2,\; +0.2)
    $$

    Multiply by $F = 0.8$:

    $$
    F \cdot (\Theta_{r_1} - \Theta_{r_2}) = (-0.016,\; -0.8,\; -0.016,\; -0.16,\; +0.16)
    $$

    Add to $\Theta_{\text{best}}$:

    $$
    \mathbf{V}_i = (0.04 - 0.016,\; 2.0 - 0.8,\; 0.04 - 0.016,\; 0.5 - 0.16,\; -0.7 + 0.16)
    $$

    $$
    = (0.024,\; 1.2,\; 0.024,\; 0.34,\; -0.54)
    $$

    **Bounds check** using the standard Heston bounds:

    | Component | Value | Lower | Upper | In bounds? |
    |---|---|---|---|---|
    | $v_0 = 0.024$ | 0.024 | 0.001 | 1.0 | Yes |
    | $\kappa = 1.2$ | 1.2 | 0.01 | 10.0 | Yes |
    | $\theta = 0.024$ | 0.024 | 0.001 | 1.0 | Yes |
    | $\xi = 0.34$ | 0.34 | 0.01 | 3.0 | Yes |
    | $\rho = -0.54$ | $-0.54$ | $-0.99$ | 0.99 | Yes |

    All components lie within the standard bounds, so no bounce-back is needed. The mutant vector is $\mathbf{V}_i = (0.024, 1.2, 0.024, 0.34, -0.54)$.

---

**Exercise 2.**
Given the mutant vector $\mathbf{V}_i = (0.038, 1.2, 0.035, 0.55, -0.74)$ and the target vector $\Theta_i = (0.042, 2.1, 0.040, 0.45, -0.68)$, perform binomial crossover with $CR = 0.9$. Suppose the random draws for each component are $(0.85, 0.95, 0.30, 0.72, 0.91)$ and $j_{\text{rand}} = 2$ (the second component). Write out the trial vector $\mathbf{U}_i$ and explain which components came from the mutant versus the target.

??? success "Solution to Exercise 2"
    The binomial crossover rule is: for each component $j$, set $U_{i,j} = V_{i,j}$ if $\text{rand}_j \leq CR$ or $j = j_{\text{rand}}$; otherwise $U_{i,j} = \Theta_{i,j}$.

    Given: $\mathbf{V}_i = (0.038, 1.2, 0.035, 0.55, -0.74)$, $\Theta_i = (0.042, 2.1, 0.040, 0.45, -0.68)$, $CR = 0.9$, random draws $(0.85, 0.95, 0.30, 0.72, 0.91)$, $j_{\text{rand}} = 2$.

    Applying the rule component by component:

    | $j$ | $\text{rand}_j$ | $\text{rand}_j \leq CR$? | $j = j_{\text{rand}}$? | Source | $U_{i,j}$ |
    |---|---|---|---|---|---|
    | 1 ($v_0$) | 0.85 | $0.85 \leq 0.9$ : Yes | No | Mutant | 0.038 |
    | 2 ($\kappa$) | 0.95 | $0.95 \leq 0.9$ : No | Yes ($j_{\text{rand}} = 2$) | Mutant | 1.2 |
    | 3 ($\theta$) | 0.30 | $0.30 \leq 0.9$ : Yes | No | Mutant | 0.035 |
    | 4 ($\xi$) | 0.72 | $0.72 \leq 0.9$ : Yes | No | Mutant | 0.55 |
    | 5 ($\rho$) | 0.91 | $0.91 \leq 0.9$ : No | No | Target | $-0.68$ |

    The trial vector is:

    $$
    \mathbf{U}_i = (0.038,\; 1.2,\; 0.035,\; 0.55,\; -0.68)
    $$

    Components 1, 3, and 4 came from the mutant because their random draws were below $CR = 0.9$. Component 2 came from the mutant because it is the guaranteed index $j_{\text{rand}} = 2$ (even though its random draw 0.95 exceeded $CR$). Component 5 came from the target because its random draw 0.91 exceeded $CR$ and it was not $j_{\text{rand}}$. In total, 4 out of 5 components came from the mutant, consistent with the high crossover rate $CR = 0.9$.

---

**Exercise 3.**
The penalized objective function is defined as:

$$
\mathcal{L}_{\text{pen}}(\Theta) = \mathcal{L}(\Theta) + \mu \cdot \max\bigl(0, \, \xi^2 - 2\kappa\theta\bigr)^2
$$

For the parameter set $(\kappa, \theta, \xi) = (1.5, 0.03, 0.5)$, compute the Feller violation $\xi^2 - 2\kappa\theta$ and the penalty term for $\mu = 50$. If the base loss is $\mathcal{L} = 3.0 \times 10^{-4}$, compute $\mathcal{L}_{\text{pen}}$. Compare with a Feller-satisfying parameter set $(\kappa, \theta, \xi) = (3.0, 0.05, 0.5)$ having the same base loss.

??? success "Solution to Exercise 3"
    **Feller violation for $(\kappa, \theta, \xi) = (1.5, 0.03, 0.5)$:**

    $$
    \xi^2 - 2\kappa\theta = 0.5^2 - 2(1.5)(0.03) = 0.25 - 0.09 = 0.16
    $$

    The Feller condition is violated (this quantity is positive). The penalty term is:

    $$
    \mu \cdot \max(0, 0.16)^2 = 50 \times 0.16^2 = 50 \times 0.0256 = 1.28
    $$

    The penalized objective is:

    $$
    \mathcal{L}_{\text{pen}} = 3.0 \times 10^{-4} + 1.28 = 1.2803
    $$

    The penalty ($1.28$) completely dominates the base loss ($3.0 \times 10^{-4}$), making this parameter set extremely unattractive to the optimizer.

    **Feller-satisfying set $(\kappa, \theta, \xi) = (3.0, 0.05, 0.5)$:**

    $$
    \xi^2 - 2\kappa\theta = 0.25 - 2(3.0)(0.05) = 0.25 - 0.30 = -0.05
    $$

    Since $\xi^2 - 2\kappa\theta = -0.05 < 0$, the Feller condition is satisfied. The penalty term is:

    $$
    \mu \cdot \max(0, -0.05)^2 = 50 \times 0 = 0
    $$

    The penalized objective equals the base loss:

    $$
    \mathcal{L}_{\text{pen}} = 3.0 \times 10^{-4}
    $$

    **Comparison:** The Feller-violating set has $\mathcal{L}_{\text{pen}} = 1.2803$, while the Feller-satisfying set has $\mathcal{L}_{\text{pen}} = 3.0 \times 10^{-4}$. The penalty is over 4,000 times larger than the base loss, so the optimizer will strongly prefer Feller-satisfying parameters. With $\mu = 50$, the penalty is aggressive --- in practice, one might use a smaller $\mu$ (e.g., $\mu = 10$) if the market data genuinely favor a Feller-violating calibration, as is common for equity surfaces.

---

**Exercise 4.**
Explain why the DE/rand/1 strategy provides more robust global exploration than DE/best/1, while DE/best/1 typically converges faster. Consider a Heston calibration landscape with two local minima at $\Theta_A = (0.04, 2.0, 0.04, 0.5, -0.7)$ with $\mathcal{L}_A = 2.5 \times 10^{-4}$ and $\Theta_B = (0.06, 0.8, 0.06, 0.3, -0.5)$ with $\mathcal{L}_B = 2.8 \times 10^{-4}$. If the current best is $\Theta_A$, describe how DE/best/1 could miss $\Theta_B$ even if $\Theta_B$ is actually closer to the global minimum.

??? success "Solution to Exercise 4"
    **DE/rand/1** constructs the mutant as $\mathbf{V}_i = \Theta_{r_1} + F(\Theta_{r_2} - \Theta_{r_3})$, where $r_1, r_2, r_3$ are all randomly chosen from the population. Since none of these indices are tied to the current best, the mutation direction is random and the search explores the parameter space uniformly. Different population members generate mutants that point in diverse directions, maintaining population diversity.

    **DE/best/1** constructs the mutant as $\mathbf{V}_i = \Theta_{\text{best}} + F(\Theta_{r_1} - \Theta_{r_2})$. Every mutant is anchored at the current best solution, so the search is concentrated in the neighborhood of $\Theta_{\text{best}}$. This exploits the current best aggressively, leading to faster convergence when $\Theta_{\text{best}}$ is near the global minimum.

    **Why DE/best/1 could miss $\Theta_B$:** Suppose the initial population converges early so that $\Theta_A$ becomes $\Theta_{\text{best}}$. Under DE/best/1, all mutants are of the form $\Theta_A + F(\Theta_{r_1} - \Theta_{r_2})$. As the population contracts around $\Theta_A$, the difference vectors $\Theta_{r_1} - \Theta_{r_2}$ become small, and all mutants remain close to $\Theta_A$. The basin around $\Theta_B$ is never explored.

    Even though $\Theta_B$ has $\mathcal{L}_B = 2.8 \times 10^{-4}$ (close to $\mathcal{L}_A = 2.5 \times 10^{-4}$), the greedy selection mechanism means $\Theta_B$ can only enter the population if a trial vector happens to land near it and achieve a lower objective than its target. But with $\Theta_A$ as the anchor, trial vectors are unlikely to reach the distant $\Theta_B$.

    Under DE/rand/1, even when most of the population is near $\Theta_A$, random members could still generate difference vectors that point toward the region containing $\Theta_B$. Moreover, if any population member is still near $\Theta_B$ (having been initialized there), it serves as a base for mutations that explore that basin further. The diversity-preserving nature of DE/rand/1 maintains exploration of multiple basins for longer, increasing the chance of finding the true global minimum --- even if it means slower convergence to any single basin.

---

**Exercise 5.**
A Heston calibration uses $N_p = 50$, $g_{\max} = 200$, and prices $M = 45$ options per evaluation using the COS method with $N = 128$ terms. Compute the total number of characteristic function evaluations. If each characteristic function evaluation takes $0.5$ microseconds, estimate the total calibration time for the DE stage alone. How does this change if you double $N_p$ to 100? Discuss the trade-off between calibration robustness and computational cost.

??? success "Solution to Exercise 5"
    **Total objective function evaluations:** The initial population requires $N_p = 50$ evaluations. Each of the $g_{\max} = 200$ generations requires $N_p = 50$ evaluations (one per trial vector). Total:

    $$
    N_{\text{eval}} = N_p + N_p \times g_{\max} = 50 + 50 \times 200 = 10{,}050
    $$

    **Characteristic function evaluations per objective evaluation:** Each objective evaluation prices $M = 45$ options using the COS method with $N = 128$ cosine terms. With 5 maturities (assuming the 45 options are spread across 5 maturities with 9 strikes each), the COS method evaluates the characteristic function at $N = 128$ points per maturity. Thanks to strike vectorization (the same characteristic function values serve all strikes at a given maturity), the total per evaluation is:

    $$
    5 \times 128 = 640 \text{ characteristic function evaluations}
    $$

    **Total characteristic function evaluations:**

    $$
    10{,}050 \times 640 = 6{,}432{,}000
    $$

    **Time estimate:** At $0.5$ microseconds per evaluation:

    $$
    6{,}432{,}000 \times 0.5 \times 10^{-6} \text{ s} = 3.216 \text{ seconds}
    $$

    Adding overhead for the COS series summation and selection operations, the DE stage takes approximately 4--5 seconds.

    **Doubling $N_p$ to 100:** The total evaluations become $100 + 100 \times 200 = 20{,}100$, and the characteristic function evaluations double to $12{,}864{,}000$, taking approximately 6--7 seconds. The wall-clock time doubles (linear in $N_p$).

    **Trade-off discussion:** Doubling $N_p$ improves robustness by sampling the parameter space more densely, reducing the probability of missing the global basin. However, it doubles the computational cost. For Heston calibration with 5 parameters, $N_p = 50$ ($= 10d$) is usually sufficient because the parameter space is low-dimensional. The benefit of $N_p = 100$ ($= 20d$) is marginal unless the objective landscape has many closely spaced local minima. In a production setting where calibration runs daily and results are warm-started, $N_p = 50$ with warm-starting is typically more cost-effective than $N_p = 100$ without warm-starting.

---

**Exercise 6.**
The $\kappa$-$\theta$ ridge structure means that only the product $\kappa\theta$ is well-identified from short-maturity data. To see this, consider the long-run variance level $\theta$ and the mean-reversion speed $\kappa$ in the CIR variance process. Show that for short maturities $T \ll 1/\kappa$, the expected integrated variance depends on $v_0$ and $\kappa\theta$ approximately as:

$$
\mathbb{E}\!\left[\int_0^T v_t \, dt\right] \approx v_0 T + \frac{1}{2}\kappa(\theta - v_0)T^2
$$

Conclude that $\kappa$ and $\theta$ are individually identifiable only from data across multiple maturities, and explain how this creates the ridge structure in the objective function.

??? success "Solution to Exercise 6"
    **The $\kappa$-$\theta$ ridge from the short-maturity expansion:** The CIR variance process satisfies $dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t$, with conditional expectation $\mathbb{E}[v_t] = \theta + (v_0 - \theta)e^{-\kappa t}$.

    The expected integrated variance is:

    $$
    \mathbb{E}\!\left[\int_0^T v_t \, dt\right] = \int_0^T \mathbb{E}[v_t] \, dt = \int_0^T \left[\theta + (v_0 - \theta)e^{-\kappa t}\right] dt
    $$

    $$
    = \theta T + (v_0 - \theta) \cdot \frac{1 - e^{-\kappa T}}{\kappa}
    $$

    For $\kappa T \ll 1$, expand $e^{-\kappa T} \approx 1 - \kappa T + \frac{1}{2}\kappa^2 T^2 - \cdots$:

    $$
    \frac{1 - e^{-\kappa T}}{\kappa} \approx \frac{\kappa T - \frac{1}{2}\kappa^2 T^2}{\kappa} = T - \frac{1}{2}\kappa T^2
    $$

    Substituting:

    $$
    \mathbb{E}\!\left[\int_0^T v_t \, dt\right] \approx \theta T + (v_0 - \theta)\left(T - \frac{1}{2}\kappa T^2\right)
    $$

    $$
    = \theta T + v_0 T - \theta T - \frac{1}{2}\kappa(v_0 - \theta) T^2
    $$

    $$
    = v_0 T + \frac{1}{2}\kappa(\theta - v_0)T^2
    $$

    This confirms the stated approximation.

    **Why $\kappa$ and $\theta$ are not separately identifiable from short-maturity data:** The leading term $v_0 T$ depends only on $v_0$ (determined by the ATM level). The first correction term $\frac{1}{2}\kappa(\theta - v_0)T^2$ depends on the product $\kappa(\theta - v_0)$, which is equivalent to $\kappa\theta - \kappa v_0$. Since $v_0$ is pinned down by the ATM volatility, the correction depends essentially on $\kappa\theta$. The individual values of $\kappa$ and $\theta$ do not appear separately until higher-order terms in $T$ become significant.

    **The ridge structure:** In the $(\kappa, \theta)$ plane, the constraint $\kappa\theta = c$ defines a hyperbola. Along this hyperbola, the short-maturity expected integrated variance (and hence the short-maturity smile shape) is approximately constant. The objective function is therefore nearly flat along the hyperbolic ridge, creating an elongated valley. Only when long-maturity data are included does the separate effect of $\kappa$ (controlling the time scale of mean-reversion) become visible, breaking the degeneracy. Specifically, the term $e^{-\kappa T}$ for large $T$ distinguishes $\kappa = 1$ from $\kappa = 5$ even if their $\kappa\theta$ products are identical.

---

**Exercise 7.**
Design a stopping criterion for DE-based Heston calibration that combines multiple convergence indicators. Specifically, define a criterion using: (a) the spread $\Delta \mathcal{L} = \max_i \mathcal{L}(\Theta_i^{(g)}) - \min_i \mathcal{L}(\Theta_i^{(g)})$, (b) the parameter dispersion $\Delta\Theta_j = \max_i \Theta_{i,j}^{(g)} - \min_i \Theta_{i,j}^{(g)}$ for each component $j$, and (c) a minimum number of generations. Propose specific threshold values and justify them in the context of Heston calibration accuracy requirements (e.g., IVRMSE below 50 bps).

??? success "Solution to Exercise 7"
    **Proposed composite stopping criterion:** Stop the DE at generation $g$ if all three conditions are satisfied:

    **(a) Objective spread criterion:** $\Delta \mathcal{L}^{(g)} = \max_i \mathcal{L}(\Theta_i^{(g)}) - \min_i \mathcal{L}(\Theta_i^{(g)}) < \epsilon_{\mathcal{L}}$

    **(b) Parameter dispersion criterion:** $\max_j \frac{\Delta\Theta_j^{(g)}}{\Theta_j^{\text{hi}} - \Theta_j^{\text{lo}}} < \epsilon_{\Theta}$ for all components $j$

    **(c) Minimum generation criterion:** $g \geq g_{\min}$

    **Proposed threshold values:**

    - $\epsilon_{\mathcal{L}} = 10^{-5}$: For a vega-weighted objective on $M = 45$ options, IVRMSE below 50 bps corresponds to $\mathcal{L} \approx M \times (50 \times 10^{-4})^2 \approx 45 \times 2.5 \times 10^{-5} \approx 10^{-3}$. A spread of $10^{-5}$ means the best and worst population members differ by only 1% of this total loss, indicating convergence to a single basin.

    - $\epsilon_{\Theta} = 0.01$ (i.e., 1% of the parameter range): This ensures all population members agree on each parameter to within 1% of its feasible range. For $\kappa \in [0.01, 10]$, this means $\Delta\kappa < 0.1$; for $\rho \in [-0.99, 0.99]$, this means $\Delta\rho < 0.02$. These dispersions are small enough that the local refinement stage will converge quickly from any population member.

    - $g_{\min} = 50$: This prevents premature stopping due to a population that happens to be initialized in a small region. Fifty generations ensure that the mutation and crossover operators have had sufficient opportunity to explore the parameter space and that apparent convergence reflects genuine basin identification rather than insufficient mixing.

    **Justification in the context of Heston calibration:** The three conditions address different failure modes:

    1. Criterion (a) alone can be satisfied if the population converges prematurely to a local minimum. The objective spread may be small, but the parameters may not be near the global minimum.
    2. Criterion (b) alone can be satisfied if all parameters happen to be in a narrow range while the objective values still vary significantly (e.g., when the population lies on a narrow ridge in parameter space).
    3. Criterion (c) provides a safety net against both premature convergence scenarios.

    Together, the three conditions ensure that the population has contracted to a small ball in parameter space ($b$), that this ball corresponds to a well-defined objective value ($a$), and that sufficient exploration has occurred ($c$). The local refinement stage (Nelder-Mead or Levenberg-Marquardt) then takes over to achieve the final precision needed for sub-50 bps IVRMSE.
