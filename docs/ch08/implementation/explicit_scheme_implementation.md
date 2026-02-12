# Explicit Finite Difference Scheme: Implementation

The **explicit finite difference scheme** computes the option price at the next time step directly using known values from the current time step. It is straightforward to implement but suffers from conditional stability.

---

## Discretizing the Black-Scholes PDE

Recall the Black-Scholes PDE:

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V = 0
$$

Replace derivatives using finite difference approximations:

- Time derivative (backward difference):
  $\frac{\partial V}{\partial t} \approx \frac{V_i^{n+1} - V_i^n}{\Delta t}$

- First derivative in space (central difference):
  $\frac{\partial V}{\partial S} \approx \frac{V_{i+1}^{n+1} - V_{i-1}^{n+1}}{2\Delta S}$

- Second derivative in space (central difference):
  $\frac{\partial^2 V}{\partial S^2} \approx \frac{V_{i+1}^{n+1} - 2V_i^{n+1} + V_{i-1}^{n+1}}{(\Delta S)^2}$

---

## The Explicit Formula

Substituting and rearranging:

$$
V_i^{n+1} = a_i V_{i-1}^n + b_i V_i^n + c_i V_{i+1}^n
$$

where the coefficients are:

$$
\begin{aligned}
a_i &= \frac{\Delta t}{2} \left[ \sigma^2 i^2 - r i \right] \\
b_i &= 1 - \Delta t \left[ \sigma^2 i^2 + r \right] \\
c_i &= \frac{\Delta t}{2} \left[ \sigma^2 i^2 + r i \right]
\end{aligned}
$$

Here $i$ is the spatial grid index and $S_i = i \Delta S$.

---

## Boundary and Initial Conditions

- **Terminal condition:** $V_i^N = \max(S_i - K, 0)$
- **Boundary at $S = 0$:** $V_0^n = 0$
- **Boundary at $S = S_{\max}$:** $V_M^n = S_{\max} - K e^{-r(T - t_n)}$

---

## Algorithm Outline

1. Initialize grid: set $S_i = i \Delta S$ and $t_n = n \Delta t$.
2. Set terminal condition at $t = T$: $V_i^N = \max(S_i - K, 0)$.
3. Apply boundary conditions at $S = 0$ and $S = S_{\max}$ for all time steps.
4. For $n = N-1$ down to $0$: use the explicit formula to compute $V_i^{n}$ for $1 \le i \le M-1$.
5. Output $V_i^0$ as the solution at $t = 0$.

---

## Stability Condition

The explicit scheme is only **conditionally stable**. A conservative stability condition is:

$$
\Delta t \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}
$$

If violated, the solution may exhibit oscillations or grow without bound.

---

## Python Implementation: European Call

We compare results of the explicit finite difference scheme in both original and log-price space against the analytical Black-Scholes formula.

**Black-Scholes Formula for a European Call:**

$$
C(S, t) = S \Phi(d_1) - K e^{-r(T - t)} \Phi(d_2)
$$

where $d_1 = \frac{\ln(S / K) + (r + \frac{1}{2} \sigma^2)(T - t)}{\sigma \sqrt{T - t}}$ and $d_2 = d_1 - \sigma \sqrt{T - t}$.

**`run_explicit_scheme_for_european_call.py`**

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

# === Instantiate Black-Scholes model ===
bs = BlackScholesNumericalSolver(S0, K, T, r, sigma, q)

# === Run Explicit FDM in Original Space ===
S_orig, V_orig = bs.solve(method="explicit", option_type=option_type,
                           Smin=S_min, Smax=S_max, NS=M+1)

# === Run Explicit FDM in Log-Price Space ===
S_log, V_log = bs.solve(method="explicit_log", option_type=option_type,
                          Smin=S_min_log, Smax=S_max, NX=M+1)

# === Analytical Black-Scholes Price (Vectorized) ===
S_all = np.union1d(S_orig, S_log)
S_all.sort()
S_all_safe = np.maximum(S_all, 1e-10)
V_exact_all, _ = BlackScholesFormula(S_all_safe, K, T, r, sigma, q).price()

# === Plot Comparison ===
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(S_orig, V_orig, label='Explicit FDM (original space)', lw=10, alpha=0.2)
ax.plot(S_log, V_log, label='Explicit FDM (log space)', lw=5, alpha=0.7)
ax.plot(S_all, V_exact_all, 'r--', label='Black-Scholes Analytical', lw=1)
ax.set_xlabel('Stock Price')
ax.set_ylabel('Option Value')
ax.set_title('European Call Option: Explicit FDM (Original vs Log-Space) vs Analytical')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()

# === Compute Max Errors ===
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

**`run_explicit_scheme_for_european_put.py`**

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
option_type = "put"

bs = BlackScholesNumericalSolver(S0, K, T, r, sigma, q)

S_orig, V_orig = bs.solve(method="explicit", option_type=option_type,
                           Smin=S_min, Smax=S_max, NS=M+1)
S_log, V_log = bs.solve(method="explicit_log", option_type=option_type,
                          Smin=S_min_log, Smax=S_max, NX=M+1)

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
ax.set_title('European Put Option: Explicit FDM (Original vs Log-Space) vs Analytical')
ax.grid(True)
ax.legend()
plt.tight_layout()
plt.show()

_, V_exact_orig = BlackScholesFormula(
    np.maximum(S_orig, 1e-10), K, T, r, sigma, q).price()
_, V_exact_log = BlackScholesFormula(
    np.maximum(S_log, 1e-10), K, T, r, sigma, q).price()

error_orig = np.max(np.abs(V_orig - V_exact_orig))
error_log = np.max(np.abs(V_log - V_exact_log))

print(f"Max absolute error (original space): {error_orig:.4f}")
print(f"Max absolute error (log space)     : {error_log:.4f}")
```

---

## Python Implementation: American Call

**`run_explicit_scheme_for_american_call.py`**

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

**`run_explicit_scheme_for_american_put.py`**

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

- The numerical result closely matches the analytical solution when grid resolution is high (e.g., $M = 100$, $N = 1000$).
- Small discrepancies may appear near the strike price due to discretization error, boundary approximation, and stability-driven timestep restrictions.
- The **maximum absolute error** gives a quantitative measure of accuracy.

---

## Summary

- The explicit FDM evolves the solution using a three-point stencil: $V_i^{n+1} = a_i V_{i-1}^n + b_i V_i^n + c_i V_{i+1}^n$.
- While simple and intuitive, the scheme requires small $\Delta t$ to remain stable, especially when $\sigma$ or $S_{\max}$ is large.
- Both original-space and log-price-space implementations are demonstrated, with error comparison against the analytical Black-Scholes formula.
