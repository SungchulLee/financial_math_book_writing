# Explicit Finite Difference Scheme: Implementation

The **explicit finite difference scheme** computes the option price at the next time step directly using known values from the current time step. It is straightforward to implement but suffers from conditional stability.

---

### Discretizing the Black-Scholes PDE

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

### The Explicit Formula

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

### Boundary and Initial Conditions

- **Terminal condition:** $V_i^N = \max(S_i - K, 0)$
- **Boundary at $S = 0$:** $V_0^n = 0$
- **Boundary at $S = S_{\max}$:** $V_M^n = S_{\max} - K e^{-r(T - t_n)}$

---

### Algorithm Outline

1. Initialize grid: set $S_i = i \Delta S$ and $t_n = n \Delta t$.
2. Set terminal condition at $t = T$: $V_i^N = \max(S_i - K, 0)$.
3. Apply boundary conditions at $S = 0$ and $S = S_{\max}$ for all time steps.
4. For $n = N-1$ down to $0$: use the explicit formula to compute $V_i^{n}$ for $1 \le i \le M-1$.
5. Output $V_i^0$ as the solution at $t = 0$.

---

### Stability Condition

The explicit scheme is only **conditionally stable**. A conservative stability condition is:

$$
\Delta t \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}
$$

If violated, the solution may exhibit oscillations or grow without bound.

---

### Python Implementation: European Call

We compare results of the explicit finite difference scheme in both original and log-price space against the analytical Black-Scholes formula.

**Black-Scholes Formula for a European Call:**

$$
C(S, t) = S \mathcal{N}(d_1) - K e^{-r(T - t)} \mathcal{N}(d_2)
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

### Python Implementation: European Put

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

### Python Implementation: American Call

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

### Python Implementation: American Put

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

### Interpretation

- The numerical result closely matches the analytical solution when grid resolution is high (e.g., $M = 100$, $N = 1000$).
- Small discrepancies may appear near the strike price due to discretization error, boundary approximation, and stability-driven timestep restrictions.
- The **maximum absolute error** gives a quantitative measure of accuracy.

---

### Summary

- The explicit FDM evolves the solution using a three-point stencil: $V_i^{n+1} = a_i V_{i-1}^n + b_i V_i^n + c_i V_{i+1}^n$.
- While simple and intuitive, the scheme requires small $\Delta t$ to remain stable, especially when $\sigma$ or $S_{\max}$ is large.
- Both original-space and log-price-space implementations are demonstrated, with error comparison against the analytical Black-Scholes formula.

---

## Exercises

**Exercise 1.** Verify the explicit scheme coefficients $a_i = \frac{\Delta t}{2}[\sigma^2 i^2 - ri]$, $b_i = 1 - \Delta t[\sigma^2 i^2 + r]$, $c_i = \frac{\Delta t}{2}[\sigma^2 i^2 + ri]$ by substituting finite difference approximations into the Black-Scholes PDE and isolating terms at nodes $i-1$, $i$, and $i+1$.

??? success "Solution to Exercise 1"
    The Black-Scholes PDE is

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
    $$

    Substitute the finite difference approximations. For the time derivative (backward in $\tau = T - t$, forward marching from maturity):

    $$
    \frac{\partial V}{\partial t} \approx \frac{V_i^{n+1} - V_i^n}{\Delta t}
    $$

    For the spatial derivatives at the **known** time level $n$:

    $$
    \frac{\partial V}{\partial S}\bigg|_i^n \approx \frac{V_{i+1}^n - V_{i-1}^n}{2\Delta S}, \quad \frac{\partial^2 V}{\partial S^2}\bigg|_i^n \approx \frac{V_{i+1}^n - 2V_i^n + V_{i-1}^n}{(\Delta S)^2}
    $$

    Substituting with $S_i = i\Delta S$:

    $$
    \frac{V_i^{n+1} - V_i^n}{\Delta t} + \frac{1}{2}\sigma^2 (i\Delta S)^2 \frac{V_{i+1}^n - 2V_i^n + V_{i-1}^n}{(\Delta S)^2} + r(i\Delta S)\frac{V_{i+1}^n - V_{i-1}^n}{2\Delta S} - rV_i^n = 0
    $$

    Simplifying $S_i^2 / (\Delta S)^2 = i^2$ and $S_i / (2\Delta S) = i/2$:

    $$
    V_i^{n+1} = V_i^n + \Delta t\left[\frac{1}{2}\sigma^2 i^2(V_{i+1}^n - 2V_i^n + V_{i-1}^n) + \frac{ri}{2}(V_{i+1}^n - V_{i-1}^n) - rV_i^n\right]
    $$

    Collecting terms by node:

    - Coefficient of $V_{i-1}^n$: $\frac{\Delta t}{2}(\sigma^2 i^2 - ri) = a_i$
    - Coefficient of $V_i^n$: $1 - \Delta t(\sigma^2 i^2 + r) = b_i$
    - Coefficient of $V_{i+1}^n$: $\frac{\Delta t}{2}(\sigma^2 i^2 + ri) = c_i$

    This confirms $V_i^{n+1} = a_i V_{i-1}^n + b_i V_i^n + c_i V_{i+1}^n$ with the stated coefficients.

---

**Exercise 2.** For $\sigma = 0.2$, $S_{\max} = 300$, $M = 100$ ($\Delta S = 3$), compute the stability bound $\Delta t \leq (\Delta S)^2 / (\sigma^2 S_{\max}^2)$. How many time steps $N$ are required for $T = 1$? What is the total number of floating-point operations (approximately)?

??? success "Solution to Exercise 2"
    Given $\sigma = 0.2$, $S_{\max} = 300$, $M = 100$, we have $\Delta S = S_{\max}/M = 3$.

    The stability bound is:

    $$
    \Delta t \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2} = \frac{9}{0.04 \times 90000} = \frac{9}{3600} = 0.0025
    $$

    For $T = 1$, the number of time steps required is:

    $$
    N \geq \frac{T}{\Delta t} = \frac{1}{0.0025} = 400
    $$

    At each time step, we compute $V_i^{n+1}$ for $i = 1, \ldots, M-1 = 99$ interior points. Each update requires 3 multiplications and 2 additions (5 floating-point operations). Over $N = 400$ time steps:

    $$
    \text{Total operations} \approx 5 \times 99 \times 400 \approx 2 \times 10^5
    $$

    Note that the stability condition based on $S_{\max}$ is conservative. A tighter analysis uses the von Neumann criterion, which may allow somewhat larger $\Delta t$ for moderate grid indices, but the $S_{\max}$-based bound guarantees stability everywhere.

---

**Exercise 3.** The coefficient $a_i = \frac{\Delta t}{2}[\sigma^2 i^2 - ri]$ is negative when $i < r/\sigma^2$. For $r = 0.05$ and $\sigma = 0.2$, compute the threshold index $i^* = r/\sigma^2$. Explain why negative coefficients violate the monotonicity of the scheme and describe the upwinding remedy.

??? success "Solution to Exercise 3"
    The threshold index is:

    $$
    i^* = \frac{r}{\sigma^2} = \frac{0.05}{0.04} = 1.25
    $$

    So for $i = 1$, we have $a_1 = \frac{\Delta t}{2}(\sigma^2 \cdot 1 - r \cdot 1) = \frac{\Delta t}{2}(0.04 - 0.05) = -0.005\Delta t < 0$.

    A negative $a_i$ means the scheme assigns a negative weight to $V_{i-1}^n$. The explicit update $V_i^{n+1} = a_i V_{i-1}^n + b_i V_i^n + c_i V_{i+1}^n$ is a weighted average of neighboring values only when all coefficients are nonnegative. When $a_i < 0$, the scheme loses its **maximum principle** (monotonicity): the numerical solution can develop spurious oscillations and may violate the constraint $V \geq 0$ even if the true solution is nonnegative.

    The **upwinding remedy** replaces the central difference for the first spatial derivative with a one-sided (upwind) difference chosen according to the sign of the convection coefficient $rS_i$. Since $rS_i > 0$, we use a backward difference:

    $$
    \frac{\partial V}{\partial S}\bigg|_i \approx \frac{V_i^n - V_{i-1}^n}{\Delta S}
    $$

    This modifies the coefficients so that $a_i$ remains nonnegative for all $i$, restoring monotonicity at the cost of reducing spatial accuracy from second order to first order in the convection term.

---

**Exercise 4.** Compare the explicit scheme in original space and log-price space for a European put with $K = 100$. In the log-price formulation, the diffusion coefficient is $\sigma^2/2$ (constant), whereas in original space it is $\sigma^2 S^2/2$ (growing with $S$). Explain why the CFL condition in log-space, $\Delta\tau \leq (\Delta x)^2/\sigma^2$, is much less restrictive than the original-space condition.

??? success "Solution to Exercise 4"
    In **original space**, the explicit scheme has the CFL condition:

    $$
    \Delta t \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}
    $$

    Because $S_{\max}^2$ appears in the denominator, for large $S_{\max}$ the allowed time step becomes extremely small.

    In **log-price space**, set $x = \ln S$. The Black-Scholes PDE transforms into:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 \frac{\partial^2 V}{\partial x^2} + \left(r - \frac{1}{2}\sigma^2\right)\frac{\partial V}{\partial x} - rV = 0
    $$

    The diffusion coefficient is now $\sigma^2/2$, a constant independent of $S$. The CFL condition becomes:

    $$
    \Delta\tau \leq \frac{(\Delta x)^2}{\sigma^2}
    $$

    where $\Delta x = (\ln S_{\max} - \ln S_{\min})/M$. Since $\ln S_{\max}$ grows much more slowly than $S_{\max}$ itself, the log-space CFL bound is far less restrictive. For example, with $S_{\max} = 300$ and $S_{\min} = 1\text{e-}3$, we have $\ln(300/0.001) \approx 12.6$, so $\Delta x \approx 0.126$ and $\Delta\tau \leq 0.126^2/0.04 \approx 0.40$, which is enormously more permissive than the original-space bound of $0.0025$.

    Additionally, the uniform grid in log-space naturally places more grid points near $S = 0$ (where the put payoff varies rapidly) and fewer near large $S$, improving resolution exactly where the put option's value changes most.

---

**Exercise 5.** The algorithm outline states that at $t = T$, we set $V_i^N = \max(S_i - K, 0)$ for a call. If we also want to price a put on the same grid, what changes are needed in the terminal condition and boundary conditions? Write them out explicitly.

??? success "Solution to Exercise 5"
    For a European **put** with strike $K$:

    - **Terminal condition:** $V_i^N = \max(K - S_i, 0)$ for all $i = 0, 1, \ldots, M$
    - **Boundary at $S = 0$:** As $S \to 0$, the put is deep in the money. The boundary condition is $V_0^n = K e^{-r(T - t_n)}$, i.e., the present value of the strike
    - **Boundary at $S = S_{\max}$:** For sufficiently large $S_{\max}$, the put is worthless: $V_M^n = 0$

    Compared to the call:

    | | Call | Put |
    |---|---|---|
    | Terminal | $\max(S_i - K, 0)$ | $\max(K - S_i, 0)$ |
    | $S = 0$ | $V_0^n = 0$ | $V_0^n = Ke^{-r(T - t_n)}$ |
    | $S = S_{\max}$ | $V_M^n = S_{\max} - Ke^{-r(T - t_n)}$ | $V_M^n = 0$ |

    The interior update formula $V_i^{n+1} = a_i V_{i-1}^n + b_i V_i^n + c_i V_{i+1}^n$ and the coefficients $a_i, b_i, c_i$ remain unchanged; only the terminal and boundary values differ.

---

**Exercise 6.** When pricing an American call with the explicit scheme and early exercise projection, explain why early exercise is never optimal for a non-dividend-paying stock (i.e., the projection step never activates). How does this change when the stock pays a continuous dividend yield $q > 0$?

??? success "Solution to Exercise 6"
    For a **non-dividend-paying** American call ($q = 0$), early exercise is never optimal. The key argument relies on the convexity bound: for any $t < T$,

    $$
    C(S, t) \geq S - Ke^{-r(T-t)} > S - K
    $$

    The first inequality follows because the European call price is bounded below by $S - Ke^{-r(T-t)}$ (by the no-arbitrage lower bound). The second inequality holds because $e^{-r(T-t)} < 1$ when $r > 0$ and $t < T$. Since the early exercise payoff is $S - K$, and the continuation value $C(S,t)$ strictly exceeds it, the projection step $V_i = \max(V_i, S_i - K)$ never activates.

    Economically, exercising early forfeits the remaining time value of the option. With no dividends, there is no competing benefit: the holder never receives less by waiting.

    When $q > 0$, the stock pays a continuous dividend yield that the option holder does not receive. The no-arbitrage lower bound weakens to:

    $$
    C(S, t) \geq Se^{-q(T-t)} - Ke^{-r(T-t)}
    $$

    When $q$ is large enough relative to $r$, this bound can fall below $S - K$, making early exercise optimal for sufficiently deep in-the-money calls. The projection step then activates at grid points where $S_i - K > V_i$ (the computed continuation value). In practice, early exercise of a dividend-paying call tends to occur just before the dividend yield causes the stock to lose value faster than the interest rate discounts the strike.
