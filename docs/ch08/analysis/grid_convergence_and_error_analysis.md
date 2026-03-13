# Grid Convergence and Error Analysis

Numerical methods must not only be stable and accurate on a single grid — they should also **converge** to the correct solution as the grid is refined. This section analyzes how finite difference solutions for the Black-Scholes equation improve as we reduce the time and space step sizes.

---

## What is Grid Convergence?

**Grid convergence** refers to the behavior of the numerical solution as the mesh becomes finer. As $\Delta S \to 0$ and $\Delta t \to 0$, the finite difference solution $V_{\text{FD}}(S,t)$ should approach the exact (analytical) solution $V_{\text{BS}}(S,t)$:

$$
\| V_{\text{FD}} - V_{\text{BS}} \| \to 0
$$

as $M \to \infty$ and $N \to \infty$.

---

## Measuring Error

The **maximum absolute error** is often used:

$$
\text{Max Error} = \max_i |V_{\text{FD}}(S_i, t=0) - V_{\text{BS}}(S_i, t=0)|
$$

Other common norms include the $\ell_2$ norm (root mean square error) and relative error (useful for options deep in- or out-of-the-money).

---

## Convergence Rate (Order of Accuracy)

For a second-order method, the error should behave like:

$$
\text{Error} \propto (\Delta S)^2 + (\Delta t)^2
$$

A **log-log plot** of error vs. $1/M$ should show a **slope of 2** for second-order schemes like Crank-Nicolson.

---

## Python Example: Error vs. Time Grid Size

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

## Python Example: Error vs. Space Grid Size

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

## Interpreting Results

- A **steeper slope** indicates faster convergence.
- Deviation from expected slope may suggest stability issues, inadequate boundary conditions, or non-smooth initial data (e.g., options with discontinuous payoffs).

---

## Summary

- Grid convergence analysis validates both **accuracy** and **implementation correctness**.
- Finite difference methods like **Crank-Nicolson** exhibit second-order convergence in both time and space.
- Always pair convergence studies with **visual plots** and **error metrics** to verify performance.
