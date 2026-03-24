# Differential Evolution and Global Search

Calibration objective functions in stochastic volatility models frequently contain multiple local minima. In the Heston model, for instance, large mean-reversion speed $\kappa$ with large long-run variance $\theta$ can produce nearly identical option prices to small $\kappa$ with small $\theta$, creating distinct basins of attraction that trap local optimizers. Differential evolution (DE) is a population-based metaheuristic that explores the parameter space globally, avoiding premature convergence to suboptimal solutions. This section develops the DE algorithm, its key operators, and its application to calibration problems.

---

## Why global search is needed

Before detailing the algorithm, consider why local methods alone are insufficient. The Heston calibration landscape $\mathcal{L}(\Theta)$ exhibits several features that challenge local optimizers:

1. **Multiple local minima.** The entanglement between $(\kappa, \theta)$ and between $(\sigma_v, v_0)$ creates 2--5 distinct local minima in typical equity index calibrations.
2. **Flat valleys.** Near the Feller boundary $2\kappa\theta = \sigma_v^2$, the objective changes slowly in certain directions, causing slow convergence.
3. **Parameter boundaries.** Constraints such as $\rho \in (-1, 1)$ create boundary effects where the gradient points outside the feasible set.
4. **Initialization sensitivity.** Levenberg-Marquardt results can vary by 10--30% in objective value depending on the starting point.

Global search methods address these challenges by maintaining a diverse population of candidate solutions that collectively explore the parameter space.

---

## The differential evolution algorithm

Differential evolution, introduced by Storn and Price (1997), evolves a population of $NP$ candidate solutions through mutation, crossover, and selection operations. The algorithm operates directly on continuous parameter vectors without encoding or decoding steps.

### Initialization

Generate an initial population $\{\Theta_1^{(0)}, \ldots, \Theta_{NP}^{(0)}\}$ by sampling uniformly within the parameter bounds:

$$
\Theta_{i,k}^{(0)} = \Theta_k^{\min} + U_i \cdot (\Theta_k^{\max} - \Theta_k^{\min}), \qquad U_i \sim \mathrm{Uniform}(0,1)
$$

for each parameter dimension $k = 1, \ldots, d$ and each individual $i = 1, \ldots, NP$. The population size $NP$ is typically chosen as $5d$ to $10d$, giving $NP = 25$--$50$ for Heston ($d = 5$) and $NP = 15$--$30$ for SABR ($d = 3$).

### Mutation

For each target vector $\Theta_i^{(g)}$ in generation $g$, a **mutant vector** $V_i^{(g)}$ is created by combining distinct population members. Several mutation strategies are available.

**DE/rand/1** (the classic strategy): Select three distinct individuals $r_1, r_2, r_3 \in \{1, \ldots, NP\} \setminus \{i\}$ uniformly at random and form

$$
V_i^{(g)} = \Theta_{r_1}^{(g)} + F \cdot \left( \Theta_{r_2}^{(g)} - \Theta_{r_3}^{(g)} \right)
$$

where $F \in (0, 2]$ is the **mutation factor** (also called the differential weight or scaling factor).

**DE/best/1**: Replace the random base vector with the current best individual:

$$
V_i^{(g)} = \Theta_{\mathrm{best}}^{(g)} + F \cdot \left( \Theta_{r_1}^{(g)} - \Theta_{r_2}^{(g)} \right)
$$

This variant converges faster but is more prone to premature convergence because the population is biased toward the current best.

**DE/rand/2**: Uses two difference vectors for greater exploration:

$$
V_i^{(g)} = \Theta_{r_1}^{(g)} + F \cdot \left( \Theta_{r_2}^{(g)} - \Theta_{r_3}^{(g)} \right) + F \cdot \left( \Theta_{r_4}^{(g)} - \Theta_{r_5}^{(g)} \right)
$$

**DE/current-to-best/1**: Blends the target and best vectors:

$$
V_i^{(g)} = \Theta_i^{(g)} + F \cdot \left( \Theta_{\mathrm{best}}^{(g)} - \Theta_i^{(g)} \right) + F \cdot \left( \Theta_{r_1}^{(g)} - \Theta_{r_2}^{(g)} \right)
$$

This strategy balances greediness (moving toward the best) with diversity (random perturbation).

!!! note "Geometric interpretation of mutation"
    The difference vector $\Theta_{r_2} - \Theta_{r_3}$ captures the local scale and orientation of the population distribution. When the population is spread across a valley, difference vectors point along the valley floor, naturally adapting the search direction to the landscape geometry. This self-adaptive property distinguishes DE from methods that use fixed perturbation distributions.

### Crossover

The crossover operator combines the mutant vector $V_i^{(g)}$ with the target vector $\Theta_i^{(g)}$ to form a **trial vector** $U_i^{(g)}$. The standard approach is **binomial crossover**:

$$
U_{i,k}^{(g)} = \begin{cases} V_{i,k}^{(g)} & \text{if } \mathrm{rand}_k \leq CR \text{ or } k = k_{\mathrm{rand}} \\ \Theta_{i,k}^{(g)} & \text{otherwise} \end{cases}
$$

where $CR \in [0, 1]$ is the **crossover rate**, $\mathrm{rand}_k \sim \mathrm{Uniform}(0,1)$ are independent for each dimension, and $k_{\mathrm{rand}} \in \{1, \ldots, d\}$ is a randomly chosen index that ensures the trial vector inherits at least one component from the mutant.

- **$CR = 0$:** The trial vector inherits only one mutant component (the mandatory $k_{\mathrm{rand}}$). Highly conservative; useful for separable objectives.
- **$CR = 1$:** The trial vector equals the mutant vector. Maximally exploratory; useful for non-separable objectives.

An alternative is **exponential crossover**, which copies a contiguous block of components from the mutant. This is more appropriate when adjacent parameter components are correlated (rare in calibration).

### Selection

The selection operator implements a greedy criterion: the trial vector replaces the target only if it achieves a lower (or equal) objective value:

$$
\Theta_i^{(g+1)} = \begin{cases} U_i^{(g)} & \text{if } \mathcal{L}(U_i^{(g)}) \leq \mathcal{L}(\Theta_i^{(g)}) \\ \Theta_i^{(g)} & \text{otherwise} \end{cases}
$$

This one-to-one greedy selection ensures that the best objective value in the population is non-increasing across generations:

$$
\min_i \mathcal{L}(\Theta_i^{(g+1)}) \leq \min_i \mathcal{L}(\Theta_i^{(g)})
$$

!!! tip "Constraint handling"
    When the mutant or trial vector violates parameter bounds, the standard remedy is to project back into the feasible region: $U_{i,k} \leftarrow \max(\Theta_k^{\min}, \min(\Theta_k^{\max}, U_{i,k}))$. Alternatively, a bounce-back rule $U_{i,k} \leftarrow \Theta_k^{\min} + \mathrm{rand} \cdot (\Theta_k^{\max} - \Theta_k^{\min})$ re-randomizes the infeasible component, maintaining population diversity.

---

## Control parameters

The performance of DE is governed by three control parameters: population size $NP$, mutation factor $F$, and crossover rate $CR$.

### Population size NP

The population must be large enough to explore the parameter space but small enough to keep the per-generation cost manageable. Guidelines:

$$
NP \geq 4d, \qquad \text{recommended } NP = 5d \text{ to } 10d
$$

For Heston calibration ($d = 5$), $NP = 25$--$50$ is typical. Each generation requires $NP$ objective function evaluations, which can be parallelized.

### Mutation factor F

The mutation factor controls the step size:

- **Small $F$** ($F < 0.4$): Short steps, fine-grained search, risk of premature convergence.
- **Moderate $F$** ($F \in [0.4, 0.9]$): Good balance between exploration and convergence.
- **Large $F$** ($F > 1.0$): Long steps, strong exploration, slow convergence.

A common default is $F = 0.8$. Dithering---drawing $F$ uniformly from $[0.5, 1.0]$ at each mutation---improves robustness.

### Crossover rate CR

The crossover rate controls the fraction of components inherited from the mutant:

- **$CR \in [0.0, 0.2]$:** Appropriate for separable or nearly separable objectives.
- **$CR \in [0.8, 1.0]$:** Appropriate for non-separable objectives (most calibration problems).

For Heston calibration, where parameters interact strongly, $CR = 0.9$ is recommended.

---

## Convergence analysis

### Theoretical results

Rigorous convergence proofs for DE are limited. The strongest results apply to simplified variants:

**Stochastic convergence.** Under standard assumptions (continuous $\mathcal{L}$, compact $\mathcal{D}$, $F > 0$, $CR > 0$), DE visits every point in $\mathcal{D}$ with positive probability. This implies that the best-so-far solution converges in probability to a global minimum:

$$
\Pr\!\left( \lim_{g \to \infty} \mathcal{L}(\Theta_{\mathrm{best}}^{(g)}) = \mathcal{L}^* \right) = 1
$$

However, the convergence rate is not specified---it could be arbitrarily slow.

**Empirical convergence rates.** On standard benchmark functions, DE typically converges as

$$
\mathcal{L}(\Theta_{\mathrm{best}}^{(g)}) - \mathcal{L}^* = \mathcal{O}(e^{-c \cdot g})
$$

for some problem-dependent constant $c > 0$, suggesting linear convergence in the generation count after the global basin is identified.

### Termination criteria

DE terminates when any of the following conditions are met:

1. **Maximum generations.** $g > g_{\max}$ (typical: $g_{\max} = 100$--$500$).
2. **Objective tolerance.** $\mathcal{L}(\Theta_{\mathrm{best}}^{(g)}) < \varepsilon_f$.
3. **Population convergence.** $\max_i \| \Theta_i^{(g)} - \Theta_{\mathrm{best}}^{(g)} \| < \varepsilon_\Theta$, indicating that the population has collapsed to a single point.
4. **Stagnation.** No improvement in the best objective for $g_{\mathrm{stag}}$ consecutive generations (typical: $g_{\mathrm{stag}} = 20$--$50$).

---

## Application to Heston calibration

### Setup

For Heston calibration with characteristic-function pricing, each objective evaluation requires $\mathcal{O}(N_{\mathrm{FFT}} \cdot n_T)$ operations (one FFT per maturity). With $NP = 30$ and $g_{\max} = 200$, the total budget is $30 \times 200 = 6000$ evaluations, which takes approximately 10--30 seconds on a modern workstation.

### Parameter bounds

$$
v_0 \in [0.001, 0.5], \quad \kappa \in [0.1, 10], \quad \theta \in [0.001, 0.5], \quad \sigma_v \in [0.01, 2.0], \quad \rho \in [-0.999, -0.01]
$$

### Recommended DE settings for Heston

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Strategy | DE/best/1 | Fast convergence for mildly multi-modal |
| $NP$ | 30 | $6d = 30$ |
| $F$ | Dithered $[0.5, 0.9]$ | Robust step size |
| $CR$ | 0.9 | Non-separable objective |
| $g_{\max}$ | 200 | Sufficient for convergence |
| Stagnation limit | 30 | Early termination |

### Hybrid DE-LM strategy

The most effective approach combines DE's global exploration with LM's local convergence:

1. **Phase 1 (DE).** Run DE for $g_1 = 50$--$100$ generations with the settings above.
2. **Phase 2 (LM).** Take the best DE individual as the starting point for Levenberg-Marquardt. Run LM to convergence with tight tolerances ($\varepsilon_g = 10^{-8}$).

This hybrid achieves objective values within 1--5% of the global optimum in 95%+ of trials, compared to 60--80% for multi-start LM alone.

!!! example "Comparison on S&P 500 data"
    On a typical S&P 500 option surface (50 options, 5 maturities), the three approaches yield:

    | Method | Objective | Success rate | Time |
    |--------|-----------|-------------|------|
    | Single LM | 0.0035 | 65% | 1 s |
    | Multi-start LM ($N = 20$) | 0.0012 | 90% | 15 s |
    | Hybrid DE-LM | 0.0010 | 98% | 12 s |

    Here "success rate" is the fraction of runs achieving objective within 10% of the best known.

---

## Adaptive DE variants

Several self-adaptive variants eliminate the need for manual parameter tuning.

### JADE (Adaptive DE)

JADE (Zhang and Sanderson, 2009) adapts $F$ and $CR$ based on successful values from previous generations. Each individual draws $F_i \sim \mathrm{Cauchy}(\mu_F, 0.1)$ and $CR_i \sim \mathcal{N}(\mu_{CR}, 0.1)$, where $\mu_F$ and $\mu_{CR}$ are updated using the Lehmer mean of successful values:

$$
\mu_F^{(g+1)} = (1 - c) \mu_F^{(g)} + c \cdot \frac{\sum_{i \in S_g} F_i^2}{\sum_{i \in S_g} F_i}
$$

$$
\mu_{CR}^{(g+1)} = (1 - c) \mu_{CR}^{(g)} + c \cdot \overline{CR}_{\mathrm{succ}}
$$

where $S_g$ is the set of individuals that successfully replaced their parents and $c = 0.1$ is a learning rate. JADE also incorporates a **current-to-pbest** mutation strategy using the top $p$-fraction of the population as base vectors.

### SHADE and L-SHADE

SHADE (Success-History-Based Adaptive DE) extends JADE by maintaining a historical memory of successful parameter settings. L-SHADE adds linear population size reduction: $NP^{(g)} = \mathrm{round}(NP_0 - g \cdot (NP_0 - NP_{\min}) / g_{\max})$, reducing the population from $NP_0$ to $NP_{\min}$ over the run. This concentrates resources as the search narrows.

These adaptive variants typically outperform standard DE with fixed control parameters, particularly when the optimal $F$ and $CR$ vary across the landscape.

---

## Other global search methods

Differential evolution is one of several global optimization methods applicable to calibration. Brief comparisons with the main alternatives follow.

### Particle swarm optimization

PSO maintains a swarm of particles, each with position $\Theta_i$ and velocity $v_i$:

$$
v_i^{(g+1)} = \omega \, v_i^{(g)} + c_1 \, r_1 \cdot (p_i - \Theta_i^{(g)}) + c_2 \, r_2 \cdot (p_g - \Theta_i^{(g)})
$$

$$
\Theta_i^{(g+1)} = \Theta_i^{(g)} + v_i^{(g+1)}
$$

where $p_i$ is the personal best, $p_g$ is the global best, $\omega$ is the inertia weight, and $c_1, c_2$ are cognitive and social acceleration coefficients. PSO converges faster than DE on some problems but is more susceptible to premature convergence due to the global best attractor.

### Simulated annealing

Simulated annealing accepts worse solutions with probability $\exp(-\Delta \mathcal{L} / T_k)$ under a cooling schedule $T_k \to 0$. It provides asymptotic convergence guarantees under logarithmic cooling ($T_k = C / \ln k$) but is slow in practice and typically outperformed by population-based methods on calibration problems.

### Basin hopping

Basin hopping combines local optimization with random perturbations and Metropolis acceptance. At each step: (1) perturb the current solution, (2) run a local optimizer to convergence, and (3) accept the new local minimum with probability $\min(1, \exp(-\Delta \mathcal{L} / T))$. This is effective when local minima are well-separated and the local optimizer is fast---precisely the situation in Heston calibration with FFT pricing.

---

## Exercises

**Exercise 1.** In DE/rand/1, the mutant vector is $V_i = \Theta_{r_1} + F(\Theta_{r_2} - \Theta_{r_3})$. Explain geometrically why the difference vector $\Theta_{r_2} - \Theta_{r_3}$ provides a self-adaptive step size: when the population is spread out, the differences are large, and when it has converged, the differences are small. How does this compare to a fixed-step random perturbation?

---

**Exercise 2.** For Heston calibration with $d = 5$ parameters and recommended $NP = 30$, $g_{\max} = 200$, compute the total number of objective function evaluations. If each evaluation takes 0.5 ms (using FFT-based pricing), estimate the total wall time. How does this change if evaluations can be parallelized across 8 cores?

---

**Exercise 3.** Compare DE/rand/1 and DE/best/1 mutation strategies. The former uses a random base vector while the latter uses the current best. Discuss the exploration-exploitation trade-off for each. For a Heston calibration landscape with 3 local minima of similar depth, which strategy is more likely to find the global minimum and why?

---

**Exercise 4.** The crossover rate $CR$ controls how many components of the trial vector come from the mutant. For a separable objective $\mathcal{L}(\Theta) = \sum_k g_k(\Theta_k)$, argue that small $CR$ (e.g., $CR = 0.1$) is appropriate. For the Heston objective where $\kappa$ and $\bar{v}$ are strongly coupled, explain why large $CR$ (e.g., $CR = 0.9$) is preferred.

---

**Exercise 5.** In the JADE adaptive DE variant, the mutation factor $\mu_F$ is updated using the Lehmer mean of successful values: $\mu_F^{(g+1)} = (1-c)\mu_F^{(g)} + c \cdot \sum F_i^2 / \sum F_i$. Show that the Lehmer mean is always greater than or equal to the arithmetic mean. Why is this bias toward larger $F$ values beneficial for maintaining exploration?

---

**Exercise 6.** A hybrid DE-LM strategy runs DE for 50 generations followed by Levenberg-Marquardt. On S&P 500 data, this achieves an objective of 0.0010 with 98% success rate in 12 seconds, while multi-start LM with 20 starts achieves 0.0012 with 90% success rate in 15 seconds. Analyze the cost-effectiveness of each approach. Under what conditions would you prefer multi-start LM over the hybrid?

---

**Exercise 7.** Design a termination criterion for DE that balances computational cost against solution quality. Specifically, define a population convergence metric $\sigma_{\text{pop}}^{(g)} = \max_i \|\Theta_i^{(g)} - \Theta_{\text{best}}^{(g)}\|$ and a stagnation counter. Propose specific thresholds for $\sigma_{\text{pop}}$ and the stagnation limit for Heston calibration with the parameter bounds given in this section. Justify your choices.
