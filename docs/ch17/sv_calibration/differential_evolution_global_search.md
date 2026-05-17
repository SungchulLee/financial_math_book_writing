# Differential Evolution and Global Search

Calibration objective functions in stochastic volatility models frequently contain multiple local minima. In the Heston model, for instance, large mean-reversion speed $\kappa$ with large long-run variance $\theta$ can produce nearly identical option prices to small $\kappa$ with small $\theta$, creating distinct basins of attraction that trap local optimizers. Differential evolution (DE) is a population-based metaheuristic that explores the parameter space globally, avoiding premature convergence to suboptimal solutions. This section develops the DE algorithm, its key operators, and its application to calibration problems.

---

## Why global search is needed

Recall (see [§ Calibration as inverse problem](../calibration_as_inverse_problem/forward_pricing_map_vs_inverse_calibration_map.md) and [§ General SV calibration](../../ch14/calibration_of_stochastic_volatility_models/identifiability_issues.md)): SV objectives are typically non-convex, with $(\kappa,\theta)$ and $(\sigma_v,v_0)$ entanglement producing 2--5 local minima, flat valleys near the Feller boundary, and starting-point sensitivity that lets LM vary by 10--30% in objective value. Global search addresses these by maintaining a diverse population that collectively explores the parameter space.

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

??? success "Solution to Exercise 1"
    The difference vector $\Theta_{r_2} - \Theta_{r_3}$ captures the current scale and orientation of the population distribution, creating a self-adaptive perturbation mechanism.

    **When the population is spread out** (early generations), the randomly selected individuals $\Theta_{r_2}$ and $\Theta_{r_3}$ are far apart, so $\|\Theta_{r_2} - \Theta_{r_3}\|$ is large. The mutant vector $V_i = \Theta_{r_1} + F(\Theta_{r_2} - \Theta_{r_3})$ takes a large step, enabling broad exploration of the parameter space. In a 5-dimensional Heston parameter space, these large differences probe distant regions and can jump between basins of attraction.

    **When the population has converged** (late generations), most individuals cluster near the best solution. The difference $\|\Theta_{r_2} - \Theta_{r_3}\|$ becomes small, and the mutant vector stays close to the base vector $\Theta_{r_1}$. This naturally transitions DE from exploration to local refinement without any explicit schedule.

    **Directional adaptation.** Beyond magnitude, the difference vector also adapts its direction to the landscape geometry. If the population is elongated along a valley (e.g., along the $(\kappa, \theta)$ ridge in Heston calibration), then randomly sampled difference vectors preferentially point along the valley floor. This is because the population density is higher along the valley direction, making it more likely that $\Theta_{r_2} - \Theta_{r_3}$ aligns with the valley axis. The search thus naturally follows the contours of the objective landscape.

    **Comparison with fixed-step perturbation.** A fixed-step method, such as adding Gaussian noise $\mathcal{N}(0, \sigma^2 I)$ to each individual, requires the user to specify $\sigma$. If $\sigma$ is too large, the search overshoots in late stages; if too small, it fails to explore in early stages. Typical remedies (cooling schedules, adaptive step sizes) must be manually tuned. DE's difference-vector mechanism provides this adaptation for free, with the population itself serving as a sampling distribution that evolves with the search. This is the key reason DE is effective without extensive parameter tuning.

---

**Exercise 2.** For Heston calibration with $d = 5$ parameters and recommended $NP = 30$, $g_{\max} = 200$, compute the total number of objective function evaluations. If each evaluation takes 0.5 ms (using FFT-based pricing), estimate the total wall time. How does this change if evaluations can be parallelized across 8 cores?

??? success "Solution to Exercise 2"
    **Total function evaluations.** Each generation evaluates the objective for all $NP$ trial vectors. With $NP = 30$ and $g_{\max} = 200$:

    $$
    N_{\text{eval}} = NP \times g_{\max} = 30 \times 200 = 6{,}000
    $$

    Note: the initial population also requires $NP = 30$ evaluations, giving a total of $6{,}030$, but the initial evaluation is often counted within the first generation.

    **Serial wall time.** At 0.5 ms per evaluation:

    $$
    T_{\text{serial}} = 6{,}000 \times 0.5 \text{ ms} = 3{,}000 \text{ ms} = 3.0 \text{ s}
    $$

    **Parallel wall time with 8 cores.** Within each generation, the $NP = 30$ evaluations are independent (each trial vector is evaluated against the objective using only the current generation's target vectors). With 8 cores, each generation requires $\lceil 30 / 8 \rceil = 4$ batches, or $4 \times 0.5 = 2.0$ ms per generation:

    $$
    T_{\text{parallel}} = 200 \times 4 \times 0.5 \text{ ms} = 400 \text{ ms} = 0.4 \text{ s}
    $$

    This is a speedup factor of $3.0 / 0.4 = 7.5$, close to the ideal factor of 8. The slight loss is due to the uneven division $30 / 8 = 3.75$, meaning some cores idle during the last batch.

    In practice, overheads from memory allocation, communication, and synchronization reduce the speedup somewhat, but the embarrassingly parallel structure of DE makes it highly amenable to multi-core execution. For larger population sizes (e.g., $NP = 64$) that divide evenly into the core count, the parallelization efficiency approaches 100%.

---

**Exercise 3.** Compare DE/rand/1 and DE/best/1 mutation strategies. The former uses a random base vector while the latter uses the current best. Discuss the exploration-exploitation trade-off for each. For a Heston calibration landscape with 3 local minima of similar depth, which strategy is more likely to find the global minimum and why?

??? success "Solution to Exercise 3"
    **DE/rand/1** uses a random base vector: $V_i = \Theta_{r_1} + F(\Theta_{r_2} - \Theta_{r_3})$.

    - *Exploration:* High. The base vector $\Theta_{r_1}$ is chosen uniformly at random from the population, so the search is not biased toward any particular region. The mutant can be generated from any part of the population, maintaining diversity.
    - *Exploitation:* Moderate. There is no explicit mechanism to concentrate the search near promising regions. Convergence toward the best solution occurs only through the selection operator, which gradually eliminates poor individuals.

    **DE/best/1** uses the best individual as the base vector: $V_i = \Theta_{\text{best}} + F(\Theta_{r_1} - \Theta_{r_2})$.

    - *Exploration:* Low to moderate. All mutant vectors are centered around $\Theta_{\text{best}}$, heavily biasing the search toward the neighborhood of the current best solution. The difference vector provides some exploration, but the base point is fixed.
    - *Exploitation:* High. By anchoring all mutations at the best solution, the algorithm intensively searches the region near the current best, rapidly refining the solution.

    **For a landscape with 3 local minima of similar depth:**
    DE/rand/1 is more likely to find the global minimum. The reason is that DE/best/1's bias toward the current best creates a positive feedback loop: once the population begins to cluster around one local minimum (even if it is not the global one), almost all mutations explore that region, and the population collapses before other basins are explored. With 3 local minima of similar depth, the first basin found is essentially random, and there is roughly a $1/3$ probability of it being the global one.

    DE/rand/1, by contrast, maintains population diversity longer. Even if some individuals converge to one basin, others remain scattered and can explore the other basins. The random base vector means that mutations originate from all parts of the parameter space, not just the current best region.

    Quantitatively, for a population of $NP = 30$ and a 5D parameter space with 3 equidistant basins, DE/rand/1 might achieve 80--90% success rate (finding the global minimum) after 200 generations, while DE/best/1 might achieve only 40--60%. The hybrid DE/current-to-best/1 strategy, which balances both, typically achieves an intermediate success rate of 70--80%.

---

**Exercise 4.** The crossover rate $CR$ controls how many components of the trial vector come from the mutant. For a separable objective $\mathcal{L}(\Theta) = \sum_k g_k(\Theta_k)$, argue that small $CR$ (e.g., $CR = 0.1$) is appropriate. For the Heston objective where $\kappa$ and $\bar{v}$ are strongly coupled, explain why large $CR$ (e.g., $CR = 0.9$) is preferred.

??? success "Solution to Exercise 4"
    **Separable objective: small $CR$ is appropriate.**
    For a separable objective $\mathcal{L}(\Theta) = \sum_k g_k(\Theta_k)$, each parameter $\Theta_k$ can be optimized independently. With small $CR$ (e.g., $CR = 0.1$), the trial vector inherits only about 1 mutant component (the mandatory $k_{\text{rand}}$ plus roughly $0.1 \times d$ additional components). This means each trial differs from its parent in essentially one dimension, allowing the algorithm to optimize each parameter axis independently.

    If $CR$ were large for a separable objective, the trial vector would inherit many mutant components simultaneously. A simultaneous change in multiple independent dimensions is unlikely to improve all of them at once -- even if the mutation improves dimensions 1, 3, and 4, it might worsen dimensions 2 and 5. The trial would then be rejected by selection despite containing some beneficial changes, slowing convergence.

    **Heston objective: large $CR$ is preferred.**
    In the Heston model, the parameters $\kappa$ and $\theta$ are strongly coupled because the stationary variance is $\theta$ and the rate of reversion is $\kappa$. The product $\kappa\theta$ appears in the Feller condition and largely determines the long-term behavior. Similarly, $\sigma_v$ and $\rho$ jointly control the smile shape -- changing one without adjusting the other typically worsens the fit.

    With small $CR$, the algorithm changes one parameter at a time, which fails to navigate the curved ridge in the $(\kappa, \theta)$ plane. Moving along the ridge requires simultaneous, coordinated changes in both parameters. Large $CR$ (e.g., $CR = 0.9$) ensures that the trial vector inherits most components from the mutant, preserving the correlation structure of the difference vector.

    Specifically, if $\Theta_{r_2}$ and $\Theta_{r_3}$ both lie near the $(\kappa, \theta)$ ridge but at different positions, their difference $\Theta_{r_2} - \Theta_{r_3}$ naturally points along the ridge. With large $CR$, this correlated perturbation is preserved in the trial vector, enabling efficient movement along the valley. With small $CR$, only one component of this correlated perturbation would be inherited, losing the directional adaptation.

---

**Exercise 5.** In the JADE adaptive DE variant, the mutation factor $\mu_F$ is updated using the Lehmer mean of successful values: $\mu_F^{(g+1)} = (1-c)\mu_F^{(g)} + c \cdot \sum F_i^2 / \sum F_i$. Show that the Lehmer mean is always greater than or equal to the arithmetic mean. Why is this bias toward larger $F$ values beneficial for maintaining exploration?

??? success "Solution to Exercise 5"
    **Showing the Lehmer mean exceeds the arithmetic mean.**
    Let $\{F_i\}_{i \in S_g}$ be the successful mutation factors. The Lehmer mean is

    $$
    L = \frac{\sum_{i \in S_g} F_i^2}{\sum_{i \in S_g} F_i}
    $$

    and the arithmetic mean is

    $$
    A = \frac{\sum_{i \in S_g} F_i}{|S_g|}
    $$

    To show $L \geq A$, consider the Cauchy-Schwarz inequality applied to the vectors $(F_1, \ldots, F_n)$ and $(1, \ldots, 1)$ where $n = |S_g|$:

    $$
    \left( \sum_i F_i \right)^2 \leq n \sum_i F_i^2
    $$

    Dividing both sides by $n \sum_i F_i$ (positive since $F_i > 0$):

    $$
    \frac{\sum_i F_i}{n} \leq \frac{\sum_i F_i^2}{\sum_i F_i}
    $$

    which is exactly $A \leq L$. Equality holds if and only if all $F_i$ are equal.

    Alternatively, one can write

    $$
    L - A = \frac{\sum_i F_i^2}{\sum_i F_i} - \frac{\sum_i F_i}{n} = \frac{n \sum_i F_i^2 - (\sum_i F_i)^2}{n \sum_i F_i} = \frac{\sum_{i<j}(F_i - F_j)^2}{n \sum_i F_i} \geq 0
    $$

    where the last step uses the identity $n \sum F_i^2 - (\sum F_i)^2 = \sum_{i<j}(F_i - F_j)^2$.

    **Why the bias toward larger $F$ is beneficial.**
    The Lehmer mean gives more weight to larger $F$ values than the arithmetic mean. This is beneficial for maintaining exploration because:

    1. **Successful large $F$ values carry more information.** A trial that succeeds with a large $F$ made a significant improvement by taking a bold step. This suggests that the landscape still has substantial structure to exploit at that scale, and the algorithm should maintain the ability to take such steps.
    2. **Small $F$ successes may be trivial.** A trial with very small $F$ barely differs from its parent and might succeed simply because the change was negligible. Overweighting these would prematurely shrink the step size.
    3. **Preventing premature convergence.** If the arithmetic mean were used instead, $\mu_F$ would decrease more rapidly as the population converges (since converged populations tend to produce small successful $F$ values). The Lehmer mean's upward bias counteracts this tendency, maintaining a larger average step size and allowing the algorithm to escape shallow local minima even in later generations.

---

**Exercise 6.** A hybrid DE-LM strategy runs DE for 50 generations followed by Levenberg-Marquardt. On S&P 500 data, this achieves an objective of 0.0010 with 98% success rate in 12 seconds, while multi-start LM with 20 starts achieves 0.0012 with 90% success rate in 15 seconds. Analyze the cost-effectiveness of each approach. Under what conditions would you prefer multi-start LM over the hybrid?

??? success "Solution to Exercise 6"
    **Cost-effectiveness analysis.**

    *Hybrid DE-LM:*

    - Objective: 0.0010
    - Success rate: 98%
    - Time: 12 s
    - Expected objective per run: $0.98 \times 0.0010 + 0.02 \times 0.0010 \times (1.10) \approx 0.00100$ (since even "failures" are within 10%)
    - Cost per unit quality: $12 / 0.98 \approx 12.2$ s per successful run

    *Multi-start LM ($N = 20$):*

    - Objective: 0.0012 (20% worse)
    - Success rate: 90%
    - Time: 15 s
    - Cost per unit quality: $15 / 0.90 \approx 16.7$ s per successful run

    The hybrid is superior in both objective quality and cost-effectiveness. Per second of computation, the hybrid achieves a better objective more reliably.

    **Scalability analysis.** Multi-start LM scales as $N \times T_{\text{LM}}$, and each restart is independent, making it trivially parallelizable. With 20 cores, the 20 starts run in $T_{\text{LM}} \approx 0.75$ s (one LM run). The hybrid requires sequential DE generations (partially parallelizable per generation) plus one LM run, giving less parallel speedup.

    **When multi-start LM is preferable:**

    1. **Massively parallel hardware.** With $\geq 20$ cores, multi-start LM completes in the time of a single LM run ($< 1$ s), while the hybrid cannot parallelize its sequential DE generations as effectively. When wall-clock time is the binding constraint and abundant parallelism is available, multi-start LM wins.
    2. **Mildly multi-modal landscapes.** If the objective has only 2--3 well-separated local minima (common for Heston), even $N = 10$ random starts have a high probability of sampling at least one point in each basin. The advantage of DE's systematic exploration diminishes.
    3. **Warm-starting from previous calibration.** If yesterday's parameters provide a good starting point, a single LM run (or a few starts centered nearby) suffices. The global search phase of DE is unnecessary when the landscape is known from prior calibration.
    4. **Implementation simplicity.** Multi-start LM requires only an LM implementation plus a loop with random initialization. DE requires implementing mutation, crossover, selection, constraint handling, and adaptive parameter logic -- significantly more code to maintain.

---

**Exercise 7.** Design a termination criterion for DE that balances computational cost against solution quality. Specifically, define a population convergence metric $\sigma_{\text{pop}}^{(g)} = \max_i \|\Theta_i^{(g)} - \Theta_{\text{best}}^{(g)}\|$ and a stagnation counter. Propose specific thresholds for $\sigma_{\text{pop}}$ and the stagnation limit for Heston calibration with the parameter bounds given in this section. Justify your choices.

??? success "Solution to Exercise 7"
    **Proposed termination criterion.**
    The termination uses three conditions evaluated jointly at each generation:

    *Condition 1: Population convergence.*

    $$
    \sigma_{\text{pop}}^{(g)} = \max_i \|\Theta_i^{(g)} - \Theta_{\text{best}}^{(g)}\| < \varepsilon_{\text{pop}}
    $$

    *Condition 2: Stagnation.* Let $n_{\text{stag}}$ count the number of consecutive generations with no improvement in the best objective. Terminate if $n_{\text{stag}} > N_{\text{stag}}$.

    *Condition 3: Maximum generations.* Terminate if $g > g_{\max}$.

    The algorithm terminates when **any** of the three conditions is satisfied.

    **Threshold calibration for Heston.**
    The Heston parameter bounds given in the section are:

    $$
    v_0 \in [0.001, 0.5], \;\; \kappa \in [0.1, 10], \;\; \theta \in [0.001, 0.5], \;\; \sigma_v \in [0.01, 2.0], \;\; \rho \in [-0.999, -0.01]
    $$

    The diameter of the parameter space in the $\ell^\infty$ norm is $\max(0.499, 9.9, 0.499, 1.99, 0.989) = 9.9$ (dominated by $\kappa$). In the $\ell^2$ norm, the maximum distance between any two feasible points is

    $$
    \sqrt{0.499^2 + 9.9^2 + 0.499^2 + 1.99^2 + 0.989^2} \approx 10.3
    $$

    **Proposed thresholds:**

    - $\varepsilon_{\text{pop}} = 10^{-3}$. This is approximately $10^{-4}$ times the diameter of the parameter space. At this scale, all individuals agree on each parameter to within a fraction of its range (e.g., $\kappa$ to within $0.001$ out of a range of $9.9$). Since the subsequent LM phase will refine the solution, the DE phase does not need to converge to full precision -- only to within the basin of the global minimum.
    - $N_{\text{stag}} = 30$ generations. With $NP = 30$, each generation evaluates 30 trial vectors. After 30 stagnant generations ($30 \times 30 = 900$ evaluations with no improvement), it is very likely that the population has found the best accessible basin. Setting $N_{\text{stag}} = 30$ allows DE sufficient opportunity to escape a suboptimal basin through random mutations while avoiding wasted computation once convergence is genuinely achieved.
    - $g_{\max} = 200$. This is a hard safety limit ensuring the algorithm terminates in bounded time ($200 \times 30 = 6{,}000$ evaluations). On most Heston calibration problems, either the population convergence or stagnation criterion triggers well before generation 200.

    **Justification for the combined criterion.**
    Using only $\sigma_{\text{pop}}$ would miss cases where the population has collapsed to a suboptimal local minimum (all individuals are close together but not at the global best). Adding the stagnation counter catches cases where the population is spread out but not making progress (e.g., stuck on a flat plateau near the Feller boundary). The maximum generation limit ensures termination even in pathological cases. Together, the three conditions provide robust termination that balances computation time against solution quality for production Heston calibration.
