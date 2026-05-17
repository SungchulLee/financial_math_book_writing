# Grid Convergence and Error Analysis

Run a finite-difference solver on a coarse grid, then halve the mesh and run it again. If the scheme is consistent and stable, the error shrinks by a predictable factor -- $1/2^p$ for order $p$. Plot $\log\|\text{error}\|$ against $\log h$ and the slope reads off $p$ directly. This is the working diagnostic of **grid convergence**: the way we verify, from numerical output alone, that the FDM solution actually approaches the true Black-Scholes price as the mesh is refined.

---

### What is Grid Convergence?

**Grid convergence** refers to the behavior of the numerical solution as the mesh becomes finer. As $\Delta S \to 0$ and $\Delta t \to 0$, the finite difference solution $V_{\text{FD}}(S,t)$ should approach the exact (analytical) solution $V_{\text{BS}}(S,t)$:

$$
\| V_{\text{FD}} - V_{\text{BS}} \| \to 0
$$

as $M \to \infty$ and $N \to \infty$.

---

### Measuring Error

The **maximum absolute error** is often used:

$$
\text{Max Error} = \max_i |V_{\text{FD}}(S_i, t=0) - V_{\text{BS}}(S_i, t=0)|
$$

Other common norms include the $\ell_2$ norm (root mean square error) and relative error (useful for options deep in- or out-of-the-money).

---

### Convergence Rate (Order of Accuracy)

For a second-order method, the error should behave like:

$$
\text{Error} \propto (\Delta S)^2 + (\Delta t)^2
$$

A **log-log plot** of error vs. $1/M$ should show a **slope of 2** for second-order schemes like Crank-Nicolson.

---

### Python Example: Error vs. Time Grid Size

**`visualize_error_vs_time_grid_size_of_cn_scheme_for_european_call.py`**

```python
import matplotlib.pyplot as plt
import numpy as np
from black_scholes import BlackScholesNumericalSolver, BlackScholesFormula

# === Parameters ===
S = 100
K = 100
T = 1.0
r = 0.05
sigma = 0.2
q = 0
S_min = 0.1
S_max = 300
option_type = "call"

errors = []
grid_sizes = []
for M in range(100, 150, 10):
    S_cn, V_cn = BlackScholesNumericalSolver(S, K, T, r, sigma, q).solve(
        method="cn", option_type=option_type, Smin=S_min, Smax=S_max, NT=M+1)
    V_exact, _ = BlackScholesFormula(S_cn, K, T, r, sigma, q).price()
    max_error = np.max(np.abs(V_cn - V_exact))
    errors.append(max_error)
    grid_sizes.append(1 / M)

plt.figure(figsize=(8, 5))
plt.plot(np.log(grid_sizes), errors, marker='o')
plt.xlabel('log(grid_size)')
plt.ylabel('Max Absolute Error')
plt.title('Grid Convergence of Crank-Nicolson FDM')
plt.grid(True, which='both')
plt.tight_layout()
plt.show()
```

---

### Python Example: Error vs. Space Grid Size

**`visualize_error_vs_space_grid_size_of_cn_scheme_for_european_call.py`**

```python
import matplotlib.pyplot as plt
import numpy as np
from black_scholes import BlackScholesNumericalSolver, BlackScholesFormula

# === Parameters ===
S = 100
K = 100
T = 1.0
r = 0.05
sigma = 0.2
q = 0
S_min = 0.1
S_max = 300
option_type = "call"

errors = []
grid_sizes = []
for M in range(15, 100, 5):
    S_cn, V_cn = BlackScholesNumericalSolver(S, K, T, r, sigma, q).solve(
        method="cn", option_type=option_type, Smin=S_min, Smax=S_max, NS=M+1)
    V_exact, _ = BlackScholesFormula(S_cn, K, T, r, sigma, q).price()
    max_error = np.max(np.abs(V_cn - V_exact))
    errors.append(max_error)
    grid_sizes.append(1 / M)

plt.figure(figsize=(8, 5))
plt.plot(np.log(grid_sizes), errors, marker='o')
plt.xlabel('log(grid_size)')
plt.ylabel('Max Absolute Error')
plt.title('Grid Convergence of Crank-Nicolson FDM')
plt.grid(True, which='both')
plt.tight_layout()
plt.show()
```

---

### Interpreting Results

- A **steeper slope** indicates faster convergence.
- Deviation from expected slope may suggest stability issues, inadequate boundary conditions, or non-smooth initial data (e.g., options with discontinuous payoffs).

---

### Summary

- Grid convergence analysis validates both **accuracy** and **implementation correctness**.
- Finite difference methods like **Crank-Nicolson** exhibit second-order convergence in both time and space.
- Always pair convergence studies with **visual plots** and **error metrics** to verify performance.

---

## Exercises

**Exercise 1.** A Crank-Nicolson solver produces the following maximum errors for a European call as the spatial grid is refined:

| $M$ | Max Error |
|-----|-----------|
| 50  | 0.0400    |
| 100 | 0.0100    |
| 200 | 0.0025    |

Compute the error ratios and confirm second-order convergence. Estimate the error for $M = 400$.

??? success "Solution to Exercise 1"
    The error ratios between successive grids are:

    $$
    \frac{0.0400}{0.0100} = 4.0, \quad \frac{0.0100}{0.0025} = 4.0
    $$

    Both ratios are exactly 4. Since doubling $M$ halves $\Delta S$, a ratio of 4 means Error $\propto (\Delta S)^2 \propto M^{-2}$, confirming second-order convergence.

    For $M = 400$ (doubling from $M = 200$), we expect the error to decrease by another factor of 4:

    $$
    \text{Error}(M=400) \approx \frac{0.0025}{4} = 0.000625
    $$

---

**Exercise 2.** Explain the difference between the maximum absolute error $\max_i |V_{\text{FD}}(S_i) - V_{\text{BS}}(S_i)|$ and the root mean square error $\sqrt{\frac{1}{M}\sum_i (V_{\text{FD}}(S_i) - V_{\text{BS}}(S_i))^2}$. Under what circumstances might the two give different impressions of the solution quality?

??? success "Solution to Exercise 2"
    The **maximum absolute error** $\max_i |V_{\text{FD}}(S_i) - V_{\text{BS}}(S_i)|$ captures the worst-case pointwise deviation anywhere on the grid. It is sensitive to localized errors and reports the single largest discrepancy.

    The **root mean square (RMS) error** $\sqrt{\frac{1}{M}\sum_i (V_{\text{FD}}(S_i) - V_{\text{BS}}(S_i))^2}$ measures the average error magnitude across all grid points. It is less sensitive to isolated large errors.

    The two metrics can give different impressions when:

    - **Localized errors dominate**: Near a payoff kink at $S = K$, the error may be large over a few grid points but small elsewhere. The max error will be large, while the RMS error remains moderate.
    - **Deep out-of-the-money regions**: Both the numerical and exact solutions are near zero, so absolute errors are small. But the max error may be dominated by errors near the strike, giving a pessimistic view of the overall solution quality.
    - **Relative vs. absolute significance**: An error of 0.01 matters much more for an option worth 0.05 than for one worth 50. Max absolute error treats both equally, while neither metric captures relative accuracy. In such cases, a weighted or relative error norm may be more informative.

---

**Exercise 3.** A convergence study shows the following behavior on a log-log plot of error vs $\Delta S$: the slope is approximately 2 for $S$ far from the strike, but drops to approximately 1 near $S = K$. Explain this observation in terms of the non-smoothness of the payoff $(S - K)^+$ and the effect on the local truncation error.

??? success "Solution to Exercise 3"
    The payoff $(S - K)^+$ has a discontinuous first derivative at $S = K$: the slope jumps from 0 (for $S < K$) to 1 (for $S > K$). The second derivative $\partial^2 V / \partial S^2$ contains a Dirac delta at $S = K$.

    The local truncation error of a second-order central difference scheme is:

    $$
    \text{LTE} = \frac{(\Delta S)^2}{12}\frac{\partial^4 V}{\partial S^4} + O((\Delta S)^4)
    $$

    This derivation requires the solution to have at least four continuous derivatives. Near $S = K$, where the payoff (and at early times, the solution) lacks even two continuous derivatives, the Taylor expansion is invalid. The actual LTE at nodes near the kink is much larger — effectively $O(1)$ rather than $O((\Delta S)^2)$.

    Far from the strike, the solution is smooth ($C^\infty$), and the full second-order accuracy is realized. This explains the observed slope of approximately 2 away from $K$ and the degraded slope of approximately 1 near $K$.

    The global error is a weighted average of local contributions. Since the non-smooth region has width $O(\Delta S)$ containing $O(1)$ grid points, the global error degrades but not catastrophically — typically to $O(\Delta S)$ or $O((\Delta S)^{3/2})$ depending on the norm and the time elapsed.

---

**Exercise 4.** Using Richardson extrapolation with two Crank-Nicolson solutions at $M = 100$ (price $V_1 = 10.430$) and $M = 200$ (price $V_2 = 10.445$), compute the extrapolated estimate $V_{\text{ext}} = (4V_2 - V_1)/3$. If the exact price is $V^* = 10.4506$, what is the extrapolation error and how does it compare to $|V_2 - V^*|$?

??? success "Solution to Exercise 4"
    Using the Richardson extrapolation formula for a second-order method ($p = 2$, $r = 2$):

    $$
    V_{\text{ext}} = \frac{4V_2 - V_1}{3} = \frac{4 \times 10.445 - 10.430}{3} = \frac{41.780 - 10.430}{3} = \frac{31.350}{3} = 10.4500
    $$

    The errors are:

    - Fine-grid error: $|V_2 - V^*| = |10.445 - 10.4506| = 0.0056$
    - Extrapolation error: $|V_{\text{ext}} - V^*| = |10.4500 - 10.4506| = 0.0006$

    The extrapolation error is approximately 9.3 times smaller than the fine-grid error, demonstrating the power of Richardson extrapolation in improving accuracy without additional grid refinement.

---

**Exercise 5.** A solver produces identical results at $M = 200$ and $M = 400$ to 6 decimal places. What are two possible explanations for this plateau in the convergence study? How would you distinguish between "the solver has reached machine precision" and "the solver has a bug that produces an incorrect but converged answer"?

??? success "Solution to Exercise 5"
    **Explanation 1: Machine precision reached.** If the solver has converged to the exact solution within floating-point arithmetic precision (roughly $10^{-15}$ for double precision), further grid refinement cannot reduce the error. The solution is as accurate as the hardware allows.

    **Explanation 2: A bug producing a converged but incorrect answer.** The solver might have an error (e.g., wrong boundary condition, sign error in a coefficient) that produces a stable, converged solution to the wrong problem.

    To distinguish between these cases:

    1. **Compare to an analytical solution**: If one exists (e.g., Black-Scholes formula for European options), compute $|V_{\text{FD}} - V_{\text{exact}}|$. If this difference is $O(10^{-12})$ or smaller, machine precision is the explanation. If the difference is $O(10^{-2})$ or larger, the solver has a bug.

    2. **Check the convergence rate at coarser grids**: If the solution showed the expected convergence rate (e.g., ratio of 4 for second-order) at coarser grids before plateauing, this is consistent with reaching machine precision. If the rate was anomalous throughout, a bug is more likely.

    3. **Test with a different method or independent implementation**: Compare against an alternative solver (e.g., Monte Carlo, binomial tree). Agreement confirms correctness; disagreement points to a bug.

---

**Exercise 6.** Design a convergence study that independently tests temporal and spatial convergence. Describe how you would fix $N$ (time steps) while varying $M$ (spatial points) to isolate the spatial error, and vice versa. Why is it important to ensure one error component is much smaller than the other in such a study?

??? success "Solution to Exercise 6"
    **Isolating spatial convergence**: Fix the number of time steps $N$ at a very large value (so that the temporal error $O((\Delta\tau)^p)$ is negligible compared to the spatial error). Then run the solver for $M = 50, 100, 200, 400, \ldots$ spatial points. Plot the error vs. $\Delta S$ on a log-log scale. The slope gives the spatial convergence order.

    **Isolating temporal convergence**: Fix the number of spatial points $M$ at a very large value (so that the spatial error $O((\Delta S)^q)$ is negligible). Then run the solver for $N = 25, 50, 100, 200, \ldots$ time steps. Plot the error vs. $\Delta\tau$ on a log-log scale. The slope gives the temporal convergence order.

    **Why one component must dominate**: The total error is approximately $c_1 (\Delta S)^q + c_2 (\Delta\tau)^p$. When varying $M$ to measure spatial convergence, if the temporal error $c_2 (\Delta\tau)^p$ is comparable to the spatial error, the observed convergence rate reflects the sum of both components, not the spatial rate alone. Once the spatial error decreases below the (fixed) temporal error, further spatial refinement shows no improvement — the error plateaus at $c_2 (\Delta\tau)^p$. This contamination makes it impossible to measure the true spatial order. By making the non-varying component much smaller, we ensure the measured rate reflects only the component being tested.
