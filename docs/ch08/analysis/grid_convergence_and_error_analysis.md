# Grid Convergence and Error Analysis

Numerical methods must not only be stable and accurate on a single grid — they should also **converge** to the correct solution as the grid is refined. This section analyzes how finite difference solutions for the Black-Scholes equation improve as we reduce the time and space step sizes.

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

---

**Exercise 2.** Explain the difference between the maximum absolute error $\max_i |V_{\text{FD}}(S_i) - V_{\text{BS}}(S_i)|$ and the root mean square error $\sqrt{\frac{1}{M}\sum_i (V_{\text{FD}}(S_i) - V_{\text{BS}}(S_i))^2}$. Under what circumstances might the two give different impressions of the solution quality?

---

**Exercise 3.** A convergence study shows the following behavior on a log-log plot of error vs $\Delta S$: the slope is approximately 2 for $S$ far from the strike, but drops to approximately 1 near $S = K$. Explain this observation in terms of the non-smoothness of the payoff $(S - K)^+$ and the effect on the local truncation error.

---

**Exercise 4.** Using Richardson extrapolation with two Crank-Nicolson solutions at $M = 100$ (price $V_1 = 10.430$) and $M = 200$ (price $V_2 = 10.445$), compute the extrapolated estimate $V_{\text{ext}} = (4V_2 - V_1)/3$. If the exact price is $V^* = 10.4506$, what is the extrapolation error and how does it compare to $|V_2 - V^*|$?

---

**Exercise 5.** A solver produces identical results at $M = 200$ and $M = 400$ to 6 decimal places. What are two possible explanations for this plateau in the convergence study? How would you distinguish between "the solver has reached machine precision" and "the solver has a bug that produces an incorrect but converged answer"?

---

**Exercise 6.** Design a convergence study that independently tests temporal and spatial convergence. Describe how you would fix $N$ (time steps) while varying $M$ (spatial points) to isolate the spatial error, and vice versa. Why is it important to ensure one error component is much smaller than the other in such a study?
