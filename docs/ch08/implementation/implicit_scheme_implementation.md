# Implicit Finite Difference Scheme: Implementation

The **implicit finite difference method** is **unconditionally stable**, meaning it remains numerically stable even for relatively large time steps. The trade-off is that it requires solving a **system of linear equations** at each time step.

---

## Finite Difference Approximation

We use the grid $S_i = i \Delta S$ for $i = 0, 1, \ldots, M$ and $t_n = n \Delta t$ for $n = 0, 1, \ldots, N$.

In the implicit method, spatial derivatives are approximated at the **future time level** $t_{n+1}$:

- Time derivative (backward difference):
  $\frac{\partial V}{\partial t} \approx \frac{V_i^{n+1} - V_i^n}{\Delta t}$

- First spatial derivative (central difference):
  $\frac{\partial V}{\partial S} \approx \frac{V_{i+1}^{n} - V_{i-1}^{n}}{2\Delta S}$

- Second spatial derivative (central difference):
  $\frac{\partial^2 V}{\partial S^2} \approx \frac{V_{i+1}^{n} - 2V_i^{n} + V_{i-1}^{n}}{(\Delta S)^2}$

---

## The Discretized Equation

Substituting into the Black-Scholes PDE and rearranging:

$$
a_i V_{i-1}^{n+1} + b_i V_i^{n+1} + c_i V_{i+1}^{n+1} = V_i^n
$$

with coefficients:

$$
\begin{aligned}
a_i &= -\frac{\Delta t}{2} \left( \sigma^2 i^2 - r i \right) \\
b_i &= 1 + \Delta t \left( \sigma^2 i^2 + r \right) \\
c_i &= -\frac{\Delta t}{2} \left( \sigma^2 i^2 + r i \right)
\end{aligned}
$$

This forms a **tridiagonal linear system** solved at each time step.

---

## Algorithm

1. Discretize the domain using $M$ spatial steps and $N$ time steps.
2. Initialize $V_i^N = \max(S_i - K, 0)$ (payoff at maturity).
3. Loop backward in time from $n = N-1$ to $0$:
   - Set up and solve the tridiagonal system $A \mathbf{V}^{n+1} = \mathbf{V}^n$.
   - Apply boundary conditions at each step.

The **Thomas algorithm** solves the tridiagonal system efficiently in $\mathcal{O}(M)$ operations.

---

## Python Implementation: European Call

**`run_implicit_scheme_for_european_call.py`**

```python
import matplotlib.pyplot as plt
import numpy as np
from black_scholes import BlackScholesNumericalSolver, BlackScholesFormula

# === Parameters ===
S0 = 100
K = 100
T = 1.0
r = 0.05
sigma = 0.2
q = 0
S_min = 0
S_min_log = 1e-3
S_max = 300
M = 100
option_type = "call"

bs = BlackScholesNumericalSolver(S0, K, T, r, sigma, q)

S_orig, V_orig = bs.solve(method="implicit", option_type=option_type,
                           Smin=S_min, Smax=S_max, NS=M+1)
S_log, V_log = bs.solve(method="implicit_log", option_type=option_type,
                          Smin=S_min_log, Smax=S_max, NX=M+1)

S_all = np.union1d(S_orig, S_log)
S_all.sort()
S_all_safe = np.maximum(S_all, 1e-10)
V_exact_all, _ = BlackScholesFormula(S_all_safe, K, T, r, sigma, q).price()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(S_orig, V_orig, label='Implicit FDM (original space)', lw=10, alpha=0.2)
ax.plot(S_log, V_log, label='Implicit FDM (log space)', lw=5, alpha=0.7)
ax.plot(S_all, V_exact_all, 'r--', label='Black-Scholes Analytical', lw=1)
ax.set_xlabel('Stock Price')
ax.set_ylabel('Option Value')
ax.set_title('European Call Option: Implicit FDM (Original vs Log-Space) vs Analytical')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()

V_exact_orig, _ = BlackScholesFormula(
    np.maximum(S_orig, 1e-10), K, T, r, sigma, q).price()
V_exact_log, _ = BlackScholesFormula(
    np.maximum(S_log, 1e-10), K, T, r, sigma, q).price()

error_orig = np.max(np.abs(V_orig - V_exact_orig))
error_log = np.max(np.abs(V_log - V_exact_log))

print(f"Max absolute error (original space): {error_orig:.4f}")
print(f"Max absolute error (log space)     : {error_log:.4f}")
```

---

## Python Implementation: European Put

**`run_implicit_scheme_for_european_put.py`**

```python
import matplotlib.pyplot as plt
import numpy as np
from black_scholes import BlackScholesNumericalSolver, BlackScholesFormula

S0, K, T, r, sigma, q = 100, 100, 1.0, 0.05, 0.2, 0
S_min, S_min_log, S_max, M = 0, 1e-3, 300, 100
option_type = "put"

bs = BlackScholesNumericalSolver(S0, K, T, r, sigma, q)

S_orig, V_orig = bs.solve(method="implicit", option_type=option_type,
                           Smin=S_min, Smax=S_max, NS=M+1)
S_log, V_log = bs.solve(method="implicit_log", option_type=option_type,
                          Smin=S_min_log, Smax=S_max, NX=M+1)

S_all = np.union1d(S_orig, S_log)
S_all.sort()
S_all_safe = np.maximum(S_all, 1e-10)
_, V_exact_all = BlackScholesFormula(S_all_safe, K, T, r, sigma, q).price()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(S_orig, V_orig, label='Implicit FDM (original space)', lw=10, alpha=0.2)
ax.plot(S_log, V_log, label='Implicit FDM (log space)', lw=5, alpha=0.7)
ax.plot(S_all, V_exact_all, 'r--', label='Black-Scholes Analytical', lw=1)
ax.set_xlabel('Stock Price')
ax.set_ylabel('Option Value')
ax.set_title('European Put Option: Implicit FDM (Original vs Log-Space) vs Analytical')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()

_, V_exact_orig = BlackScholesFormula(
    np.maximum(S_orig, 1e-10), K, T, r, sigma, q).price()
_, V_exact_log = BlackScholesFormula(
    np.maximum(S_log, 1e-10), K, T, r, sigma, q).price()

print(f"Max absolute error (original space): {np.max(np.abs(V_orig - V_exact_orig)):.4f}")
print(f"Max absolute error (log space)     : {np.max(np.abs(V_log - V_exact_log)):.4f}")
```

---

## Python Implementation: American Call

**`run_implicit_scheme_for_american_call.py`**

```python
import matplotlib.pyplot as plt
import numpy as np
from black_scholes import BlackScholesNumericalSolver, BlackScholesFormula

S0, K, T, r, sigma, q = 100, 100, 1.0, 0.05, 0.2, 0
S_min, S_min_log, S_max, M = 0, 1e-3, 300, 100
option_type = "call"

bs = BlackScholesNumericalSolver(S0, K, T, r, sigma, q)

S_orig, V_orig = bs.solve(method="implicit", option_type=option_type,
                           Smin=S_min, Smax=S_max, NS=M+1, early_exercise=True)
S_log, V_log = bs.solve(method="implicit_log", option_type=option_type,
                          Smin=S_min_log, Smax=S_max, NX=M+1, early_exercise=True)

S_all = np.union1d(S_orig, S_log)
S_all.sort()
S_all_safe = np.maximum(S_all, 1e-10)
V_exact_all, _ = BlackScholesFormula(S_all_safe, K, T, r, sigma, q).price()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(S_orig, V_orig, label='Implicit FDM (original space)', lw=10, alpha=0.2)
ax.plot(S_log, V_log, label='Implicit FDM (log space)', lw=5, alpha=0.7)
ax.plot(S_all, V_exact_all, 'r--', label='Black-Scholes Analytical', lw=1)
ax.set_xlabel('Stock Price')
ax.set_ylabel('Option Value')
ax.set_title('American Call Option: Implicit FDM (Original vs Log-Space) vs Analytical')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()

V_exact_orig, _ = BlackScholesFormula(
    np.maximum(S_orig, 1e-10), K, T, r, sigma, q).price()
V_exact_log, _ = BlackScholesFormula(
    np.maximum(S_log, 1e-10), K, T, r, sigma, q).price()

print(f"Max absolute error (original space): {np.max(np.abs(V_orig - V_exact_orig)):.4f}")
print(f"Max absolute error (log space)     : {np.max(np.abs(V_log - V_exact_log)):.4f}")
```

---

## Python Implementation: American Put

**`run_implicit_scheme_for_american_put.py`**

```python
import matplotlib.pyplot as plt
import numpy as np
from black_scholes import BlackScholesNumericalSolver, BlackScholesFormula

S0, K, T, r, sigma, q = 100, 100, 1.0, 0.05, 0.2, 0
S_min, S_min_log, S_max, M = 0, 1e-3, 300, 100
option_type = "put"

bs = BlackScholesNumericalSolver(S0, K, T, r, sigma, q)

S_orig, V_orig = bs.solve(method="implicit", option_type=option_type,
                           Smin=S_min, Smax=S_max, NS=M+1, early_exercise=True)
S_log, V_log = bs.solve(method="implicit_log", option_type=option_type,
                          Smin=S_min_log, Smax=S_max, NX=M+1, early_exercise=True)

S_all = np.union1d(S_orig, S_log)
S_all.sort()
S_all_safe = np.maximum(S_all, 1e-10)
_, V_exact_all = BlackScholesFormula(S_all_safe, K, T, r, sigma, q).price()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(S_orig, V_orig, label='Implicit FDM (original space)', lw=10, alpha=0.2)
ax.plot(S_log, V_log, label='Implicit FDM (log space)', lw=5, alpha=0.7)
ax.plot(S_all, V_exact_all, 'r--', label='Black-Scholes Analytical', lw=1)
ax.set_xlabel('Stock Price')
ax.set_ylabel('Option Value')
ax.set_title('American Put Option: Implicit FDM (Original vs Log-Space) vs Analytical')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()

_, V_exact_orig = BlackScholesFormula(
    np.maximum(S_orig, 1e-10), K, T, r, sigma, q).price()
_, V_exact_log = BlackScholesFormula(
    np.maximum(S_log, 1e-10), K, T, r, sigma, q).price()

print(f"Max absolute error (original space): {np.max(np.abs(V_orig - V_exact_orig)):.4f}")
print(f"Max absolute error (log space)     : {np.max(np.abs(V_log - V_exact_log)):.4f}")
```

---

## Interpretation

- The implicit scheme is **unconditionally stable** — it will not blow up for any $\Delta t$ or $\Delta S$.
- The match with the Black-Scholes formula is excellent, especially for reasonably fine grids.
- Some small deviation may occur near boundaries, but accuracy is good throughout the domain.

---

## Summary

- The implicit method improves numerical stability and allows for larger time steps.
- It transforms the discretized PDE into a tridiagonal system at each time step.
- Though more complex than the explicit method, it is **more robust** and **practical** for real-world applications.
