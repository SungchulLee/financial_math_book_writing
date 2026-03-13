# Crank-Nicolson Scheme: Implementation

The **Crank-Nicolson method** combines the accuracy of the explicit method with the stability of the implicit method. It is **second-order accurate** in both time and space, making it the preferred method in many financial engineering applications.

---

## The Idea

The Crank-Nicolson method uses the **average of the explicit and implicit finite difference approximations**:

$$
\frac{V_i^{n+1} - V_i^n}{\Delta t} = \frac{1}{2} \left( L V_i^n + L V_i^{n+1} \right)
$$

where $L$ is the spatial differential operator in the Black-Scholes PDE. This leads to a **tridiagonal linear system** at each time step with improved accuracy.

---

## Finite Difference Formulation

Writing the Black-Scholes PDE as:

$$
\frac{\partial V}{\partial t} = -\frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - r S \frac{\partial V}{\partial S} + r V
$$

and applying the Crank-Nicolson approach, we derive a linear system:

$$
A \mathbf{V}^{n+1} = B \mathbf{V}^n + \mathbf{b}_{\text{boundary}}
$$

where $A$ and $B$ are tridiagonal matrices and $\mathbf{b}_{\text{boundary}}$ incorporates boundary adjustments.

---

## Properties

| Feature            | Crank-Nicolson         |
|--------------------|------------------------|
| Stability          | Unconditionally stable |
| Time Accuracy      | Second-order           |
| Space Accuracy     | Second-order           |
| Cost per time step | Moderate               |
| Overall performance| Excellent              |

---

## Python Implementation: European Call

**`run_cn_scheme_for_european_call.py`**

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

S_orig, V_orig = bs.solve(method="cn", option_type=option_type,
                           Smin=S_min, Smax=S_max, NS=M+1)
S_log, V_log = bs.solve(method="cn_log", option_type=option_type,
                          Smin=S_min_log, Smax=S_max, NX=M+1)

S_all = np.union1d(S_orig, S_log)
S_all.sort()
S_all_safe = np.maximum(S_all, 1e-10)
V_exact_all, _ = BlackScholesFormula(S_all_safe, K, T, r, sigma, q).price()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(S_orig, V_orig, label='CN FDM (original space)', lw=10, alpha=0.2)
ax.plot(S_log, V_log, label='CN FDM (log space)', lw=5, alpha=0.7)
ax.plot(S_all, V_exact_all, 'r--', label='Black-Scholes Analytical', lw=1)
ax.set_xlabel('Stock Price')
ax.set_ylabel('Option Value')
ax.set_title('European Call Option: CN FDM (Original vs Log-Space) vs Analytical')
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

**`run_cn_scheme_for_european_put.py`**

```python
import matplotlib.pyplot as plt
import numpy as np
from black_scholes import BlackScholesNumericalSolver, BlackScholesFormula

S0, K, T, r, sigma, q = 100, 100, 1.0, 0.05, 0.2, 0
S_min, S_min_log, S_max, M = 0, 1e-3, 300, 100
option_type = "put"

bs = BlackScholesNumericalSolver(S0, K, T, r, sigma, q)

S_orig, V_orig = bs.solve(method="cn", option_type=option_type,
                           Smin=S_min, Smax=S_max, NS=M+1)
S_log, V_log = bs.solve(method="cn_log", option_type=option_type,
                          Smin=S_min_log, Smax=S_max, NX=M+1)

S_all = np.union1d(S_orig, S_log)
S_all.sort()
S_all_safe = np.maximum(S_all, 1e-10)
_, V_exact_all = BlackScholesFormula(S_all_safe, K, T, r, sigma, q).price()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(S_orig, V_orig, label='CN FDM (original space)', lw=10, alpha=0.2)
ax.plot(S_log, V_log, label='CN FDM (log space)', lw=5, alpha=0.7)
ax.plot(S_all, V_exact_all, 'r--', label='Black-Scholes Analytical', lw=1)
ax.set_xlabel('Stock Price')
ax.set_ylabel('Option Value')
ax.set_title('European Put Option: CN FDM (Original vs Log-Space) vs Analytical')
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

Note: The Colab uses explicit scheme for American CN examples. The `early_exercise=True` flag enables the projection method.

**`run_cn_scheme_for_american_call.py`**

```python
import matplotlib.pyplot as plt
import numpy as np
from black_scholes import BlackScholesNumericalSolver, BlackScholesFormula

S0, K, T, r, sigma, q = 100, 100, 1.0, 0.05, 0.2, 0
S_min, S_min_log, S_max, M = 0, 1e-3, 300, 100
option_type = "call"

bs = BlackScholesNumericalSolver(S0, K, T, r, sigma, q)

S_orig, V_orig = bs.solve(method="explicit", option_type=option_type,
                           Smin=S_min, Smax=S_max, NS=M+1, early_exercise=True)
S_log, V_log = bs.solve(method="explicit_log", option_type=option_type,
                          Smin=S_min_log, Smax=S_max, NX=M+1, early_exercise=True)

S_all = np.union1d(S_orig, S_log)
S_all.sort()
S_all_safe = np.maximum(S_all, 1e-10)
V_exact_all, _ = BlackScholesFormula(S_all_safe, K, T, r, sigma, q).price()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(S_orig, V_orig, label='Explicit FDM (original space)', lw=10, alpha=0.2)
ax.plot(S_log, V_log, label='Explicit FDM (log space)', lw=5, alpha=0.7)
ax.plot(S_all, V_exact_all, 'r--', label='Black-Scholes Analytical', lw=1)
ax.set_xlabel('Stock Price')
ax.set_ylabel('Option Value')
ax.set_title('American Call Option: Explicit FDM (Original vs Log-Space) vs Analytical')
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

**`run_cn_scheme_for_american_put.py`**

```python
import matplotlib.pyplot as plt
import numpy as np
from black_scholes import BlackScholesNumericalSolver, BlackScholesFormula

S0, K, T, r, sigma, q = 100, 100, 1.0, 0.05, 0.2, 0
S_min, S_min_log, S_max, M = 0, 1e-3, 300, 100
option_type = "put"

bs = BlackScholesNumericalSolver(S0, K, T, r, sigma, q)

S_orig, V_orig = bs.solve(method="explicit", option_type=option_type,
                           Smin=S_min, Smax=S_max, NS=M+1, early_exercise=True)
S_log, V_log = bs.solve(method="explicit_log", option_type=option_type,
                          Smin=S_min_log, Smax=S_max, NX=M+1, early_exercise=True)

S_all = np.union1d(S_orig, S_log)
S_all.sort()
S_all_safe = np.maximum(S_all, 1e-10)
_, V_exact_all = BlackScholesFormula(S_all_safe, K, T, r, sigma, q).price()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(S_orig, V_orig, label='Explicit FDM (original space)', lw=10, alpha=0.2)
ax.plot(S_log, V_log, label='Explicit FDM (log space)', lw=5, alpha=0.7)
ax.plot(S_all, V_exact_all, 'r--', label='Black-Scholes Analytical', lw=1)
ax.set_xlabel('Stock Price')
ax.set_ylabel('Option Value')
ax.set_title('American Put Option: Explicit FDM (Original vs Log-Space) vs Analytical')
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

- The **Crank-Nicolson method** gives a nearly perfect match to the analytical solution.
- It achieves this with **fewer time steps** compared to the explicit method, thanks to its higher-order accuracy.
- It is stable and efficient even with relatively large time steps.

---

## Summary

- The Crank-Nicolson scheme offers a **balance between accuracy and stability**.
- It requires solving a tridiagonal system at each time step, like the implicit method.
- It is **ideal for production-quality option pricing engines**, especially for European-style derivatives.
