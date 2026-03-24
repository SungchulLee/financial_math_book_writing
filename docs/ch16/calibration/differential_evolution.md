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

where $U_i \in [0,1]^5$ is a random vector, $\odot$ denotes element-wise multiplication, and $\Theta^{\text{lo}}, \Theta^{\text{hi}}$ are the lower and upper bounds. For Heston calibration, typical bounds are:

| Parameter | Lower | Upper | Interpretation |
|---|---|---|---|
| $v_0$ | $0.001$ | $1.0$ | Initial variance ($\sigma_0$ from 3% to 100%) |
| $\kappa$ | $0.01$ | $10.0$ | Mean-reversion speed (half-life 0.07 to 69 years) |
| $\theta$ | $0.001$ | $1.0$ | Long-run variance |
| $\xi$ | $0.01$ | $3.0$ | Vol-of-vol |
| $\rho$ | $-0.99$ | $0.99$ | Correlation |

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

Rather than strictly enforcing the Feller condition (which reduces the search space and may prevent the optimizer from finding good fits when the market data implies Feller violation), add a **soft penalty**:

$$
\mathcal{L}_{\text{pen}}(\Theta) = \mathcal{L}(\Theta) + \mu \cdot \max\bigl(0, \, \xi^2 - 2\kappa\theta\bigr)^2
$$

where $\mu > 0$ is a penalty weight. Setting $\mu$ large enough discourages Feller violation without creating a hard boundary that could cause the optimizer to miss nearby good solutions.

!!! tip "Feller Condition in Practice"
    Many market-calibrated Heston parameters violate the Feller condition ($2\kappa\theta < \xi^2$). The variance process still stays positive almost surely---it just touches zero with positive probability. Strictly enforcing Feller can produce worse fits. A soft penalty with $\mu$ between 10 and 100 is a practical compromise.

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

---

**Exercise 2.**
Given the mutant vector $\mathbf{V}_i = (0.038, 1.2, 0.035, 0.55, -0.74)$ and the target vector $\Theta_i = (0.042, 2.1, 0.040, 0.45, -0.68)$, perform binomial crossover with $CR = 0.9$. Suppose the random draws for each component are $(0.85, 0.95, 0.30, 0.72, 0.91)$ and $j_{\text{rand}} = 2$ (the second component). Write out the trial vector $\mathbf{U}_i$ and explain which components came from the mutant versus the target.

---

**Exercise 3.**
The penalized objective function is defined as:

$$
\mathcal{L}_{\text{pen}}(\Theta) = \mathcal{L}(\Theta) + \mu \cdot \max\bigl(0, \, \xi^2 - 2\kappa\theta\bigr)^2
$$

For the parameter set $(\kappa, \theta, \xi) = (1.5, 0.03, 0.5)$, compute the Feller violation $\xi^2 - 2\kappa\theta$ and the penalty term for $\mu = 50$. If the base loss is $\mathcal{L} = 3.0 \times 10^{-4}$, compute $\mathcal{L}_{\text{pen}}$. Compare with a Feller-satisfying parameter set $(\kappa, \theta, \xi) = (3.0, 0.05, 0.5)$ having the same base loss.

---

**Exercise 4.**
Explain why the DE/rand/1 strategy provides more robust global exploration than DE/best/1, while DE/best/1 typically converges faster. Consider a Heston calibration landscape with two local minima at $\Theta_A = (0.04, 2.0, 0.04, 0.5, -0.7)$ with $\mathcal{L}_A = 2.5 \times 10^{-4}$ and $\Theta_B = (0.06, 0.8, 0.06, 0.3, -0.5)$ with $\mathcal{L}_B = 2.8 \times 10^{-4}$. If the current best is $\Theta_A$, describe how DE/best/1 could miss $\Theta_B$ even if $\Theta_B$ is actually closer to the global minimum.

---

**Exercise 5.**
A Heston calibration uses $N_p = 50$, $g_{\max} = 200$, and prices $M = 45$ options per evaluation using the COS method with $N = 128$ terms. Compute the total number of characteristic function evaluations. If each characteristic function evaluation takes $0.5$ microseconds, estimate the total calibration time for the DE stage alone. How does this change if you double $N_p$ to 100? Discuss the trade-off between calibration robustness and computational cost.

---

**Exercise 6.**
The $\kappa$-$\theta$ ridge structure means that only the product $\kappa\theta$ is well-identified from short-maturity data. To see this, consider the long-run variance level $\theta$ and the mean-reversion speed $\kappa$ in the CIR variance process. Show that for short maturities $T \ll 1/\kappa$, the expected integrated variance depends on $v_0$ and $\kappa\theta$ approximately as:

$$
\mathbb{E}\!\left[\int_0^T v_t \, dt\right] \approx v_0 T + \frac{1}{2}\kappa(\theta - v_0)T^2
$$

Conclude that $\kappa$ and $\theta$ are individually identifiable only from data across multiple maturities, and explain how this creates the ridge structure in the objective function.

---

**Exercise 7.**
Design a stopping criterion for DE-based Heston calibration that combines multiple convergence indicators. Specifically, define a criterion using: (a) the spread $\Delta \mathcal{L} = \max_i \mathcal{L}(\Theta_i^{(g)}) - \min_i \mathcal{L}(\Theta_i^{(g)})$, (b) the parameter dispersion $\Delta\Theta_j = \max_i \Theta_{i,j}^{(g)} - \min_i \Theta_{i,j}^{(g)}$ for each component $j$, and (c) a minimum number of generations. Propose specific threshold values and justify them in the context of Heston calibration accuracy requirements (e.g., IVRMSE below 50 bps).
