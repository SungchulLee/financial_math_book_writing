# Implicit Finite Difference Scheme: Implementation

The **implicit finite difference method** is **unconditionally stable**, meaning it remains numerically stable even for relatively large time steps. The trade-off is that it requires solving a **system of linear equations** at each time step.

---

### Finite Difference Approximation

We use the grid $S_i = i \Delta S$ for $i = 0, 1, \ldots, M$ and $t_n = n \Delta t$ for $n = 0, 1, \ldots, N$.

In the implicit method, spatial derivatives are approximated at the **future time level** $t_{n+1}$:

- Time derivative (backward difference):
  $\frac{\partial V}{\partial t} \approx \frac{V_i^{n+1} - V_i^n}{\Delta t}$

- First spatial derivative (central difference):
  $\frac{\partial V}{\partial S} \approx \frac{V_{i+1}^{n} - V_{i-1}^{n}}{2\Delta S}$

- Second spatial derivative (central difference):
  $\frac{\partial^2 V}{\partial S^2} \approx \frac{V_{i+1}^{n} - 2V_i^{n} + V_{i-1}^{n}}{(\Delta S)^2}$

---

### The Discretized Equation

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

### Algorithm

1. Discretize the domain using $M$ spatial steps and $N$ time steps.
2. Initialize $V_i^N = \max(S_i - K, 0)$ (payoff at maturity).
3. Loop backward in time from $n = N-1$ to $0$:
   - Set up and solve the tridiagonal system $A \mathbf{V}^{n+1} = \mathbf{V}^n$.
   - Apply boundary conditions at each step.

The **Thomas algorithm** solves the tridiagonal system efficiently in $\mathcal{O}(M)$ operations.

---

### Python Implementation: European Call

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

### Python Implementation: European Put

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

### Python Implementation: American Call

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

### Python Implementation: American Put

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

### Interpretation

- The implicit scheme is **unconditionally stable** — it will not blow up for any $\Delta t$ or $\Delta S$.
- The match with the Black-Scholes formula is excellent, especially for reasonably fine grids.
- Some small deviation may occur near boundaries, but accuracy is good throughout the domain.

---

### Summary

- The implicit method improves numerical stability and allows for larger time steps.
- It transforms the discretized PDE into a tridiagonal system at each time step.
- Though more complex than the explicit method, it is **more robust** and **practical** for real-world applications.

---

## Exercises

**Exercise 1.** For the implicit scheme with $M = 4$ interior points, $\sigma = 0.2$, $r = 0.05$, $S_{\max} = 200$ ($\Delta S = 40$), and $\Delta t = 0.01$, compute the tridiagonal matrix coefficients $a_i$, $b_i$, $c_i$ for $i = 1, 2, 3, 4$. Verify that all diagonal entries $b_i$ are positive and all off-diagonal entries $a_i$, $c_i$ are negative, confirming the M-matrix structure.

??? success "Solution to Exercise 1"
    With $M = 4$, $S_{\max} = 200$, we have $\Delta S = 200/5 = 40$ (since there are $M+1 = 5$ intervals from $S = 0$ to $S = S_{\max}$). The grid points are $S_i = i \cdot 40$ for $i = 0, 1, 2, 3, 4$.

    Using $\sigma = 0.2$, $r = 0.05$, $\Delta t = 0.01$:

    $$
    a_i = -\frac{\Delta t}{2}(\sigma^2 i^2 - ri) = -\frac{0.01}{2}(0.04 i^2 - 0.05 i)
    $$

    $$
    b_i = 1 + \Delta t(\sigma^2 i^2 + r) = 1 + 0.01(0.04 i^2 + 0.05)
    $$

    $$
    c_i = -\frac{\Delta t}{2}(\sigma^2 i^2 + ri) = -\frac{0.01}{2}(0.04 i^2 + 0.05 i)
    $$

    Computing for each $i$:

    | $i$ | $\sigma^2 i^2$ | $ri$ | $a_i$ | $b_i$ | $c_i$ |
    |-----|-----------------|------|--------|--------|--------|
    | 1 | 0.04 | 0.05 | $-0.005(0.04 - 0.05) = 0.00005$ | $1 + 0.01(0.04 + 0.05) = 1.0009$ | $-0.005(0.04 + 0.05) = -0.00045$ |
    | 2 | 0.16 | 0.10 | $-0.005(0.16 - 0.10) = -0.0003$ | $1 + 0.01(0.16 + 0.05) = 1.0021$ | $-0.005(0.16 + 0.10) = -0.0013$ |
    | 3 | 0.36 | 0.15 | $-0.005(0.36 - 0.15) = -0.00105$ | $1 + 0.01(0.36 + 0.05) = 1.0041$ | $-0.005(0.36 + 0.15) = -0.00255$ |
    | 4 | 0.64 | 0.20 | $-0.005(0.64 - 0.20) = -0.0022$ | $1 + 0.01(0.64 + 0.05) = 1.0069$ | $-0.005(0.64 + 0.20) = -0.0042$ |

    All diagonal entries $b_i > 1 > 0$. For $i \geq 2$, both $a_i < 0$ and $c_i < 0$. For $i = 1$, $a_1 > 0$ (since $ri > \sigma^2 i^2$ at $i = 1$), while $c_1 < 0$. The diagonal dominance holds: $|b_i| > |a_i| + |c_i|$ for all $i$, confirming the M-matrix structure for $i \geq 2$. The slight positivity of $a_1$ does not affect the solvability of the tridiagonal system but shows that the strict M-matrix property requires either upwinding or a finer grid at low $i$.

---

**Exercise 2.** The Thomas algorithm solves a tridiagonal system in $O(M)$ operations. Describe what would happen if you used standard Gaussian elimination instead. What is its cost, and why is the Thomas algorithm preferred?

??? success "Solution to Exercise 2"
    The tridiagonal system has the form $A\mathbf{v} = \mathbf{d}$ where $A$ is an $(M-1) \times (M-1)$ tridiagonal matrix. The **Thomas algorithm** exploits the tridiagonal structure:

    - **Forward sweep** (elimination): $M - 1$ steps, each requiring 1 division, 1 multiplication, and 1 subtraction = $O(M)$ operations
    - **Back substitution**: $M - 1$ steps, each requiring 1 multiplication and 1 subtraction = $O(M)$ operations

    Total cost: $O(M)$ operations and $O(M)$ storage.

    **Standard Gaussian elimination** on a general $(M-1) \times (M-1)$ matrix requires:

    - Forward elimination: $\sim \frac{2}{3}(M-1)^3$ operations
    - Back substitution: $\sim (M-1)^2$ operations

    Total cost: $O(M^3)$ operations and $O(M^2)$ storage.

    For $M = 200$, the Thomas algorithm uses $\sim 400$ operations per time step, while Gaussian elimination uses $\sim 5 \times 10^6$. Over $N = 200$ time steps, this difference is $8 \times 10^4$ versus $10^9$ --- a factor of more than $10^4$.

    The Thomas algorithm is preferred because it is optimally efficient for tridiagonal systems: it achieves the theoretical minimum operation count, is simple to implement, numerically stable for diagonally dominant systems, and requires no pivoting.

---

**Exercise 3.** The implicit scheme is unconditionally stable, meaning any $\Delta t > 0$ can be used. However, choosing $\Delta t$ too large reduces accuracy. For a European call with $K = 100$, $T = 1$, $\sigma = 0.2$, $M = 200$, what is a reasonable choice of $N$ (number of time steps) if the target is $O((\Delta S)^2)$ accuracy in space and $O(\Delta t)$ accuracy in time?

??? success "Solution to Exercise 3"
    The implicit scheme has spatial accuracy $O((\Delta S)^2)$ and temporal accuracy $O(\Delta t)$. To balance these, we want:

    $$
    O(\Delta t) \sim O((\Delta S)^2)
    $$

    With $M = 200$ and $S_{\max} = 300$ (a typical choice), $\Delta S = 300/200 = 1.5$, so $(\Delta S)^2 = 2.25$.

    Setting $\Delta t \approx (\Delta S)^2$ gives $\Delta t \approx 2.25$, but since $T = 1$, we need $\Delta t \leq T$. The formal balance $\Delta t = C(\Delta S)^2$ for some constant $C$ means:

    $$
    N = \frac{T}{\Delta t} \sim \frac{T}{C(\Delta S)^2} = \frac{T \cdot M^2}{C \cdot S_{\max}^2}
    $$

    A practical choice is to take $N = M$ (or $N = M/2$), since the implicit scheme is unconditionally stable and overly small $\Delta t$ is unnecessary. With $M = 200$ and $N = 200$, we get $\Delta t = 0.005$, which is much smaller than $(\Delta S)^2 = 2.25$, meaning the temporal error is negligible compared to the spatial error. This is a reasonable and conservative choice.

    For a more balanced approach, one could use $N \approx 50$--$100$, giving $\Delta t \approx 0.01$--$0.02$, which keeps the temporal error comparable to or below the spatial error.

---

**Exercise 4.** Compare the implicit scheme solutions for a European call in original space and log-price space. The log-price formulation has constant coefficients, while the original-space formulation has $S$-dependent coefficients. Discuss how this affects the Thomas algorithm implementation and the accuracy of the solution.

??? success "Solution to Exercise 4"
    In **original space**, the coefficients $a_i, b_i, c_i$ depend on the grid index $i$ (equivalently on $S_i = i\Delta S$):

    $$
    a_i = -\frac{\Delta t}{2}(\sigma^2 i^2 - ri), \quad b_i = 1 + \Delta t(\sigma^2 i^2 + r), \quad c_i = -\frac{\Delta t}{2}(\sigma^2 i^2 + ri)
    $$

    The tridiagonal matrix entries vary from row to row. The Thomas algorithm still applies, but each forward-sweep step uses different coefficients. Moreover, the $i^2$ growth in the diffusion term means that for large $i$ (large $S$), the off-diagonal entries become large relative to the diagonal, which can degrade the conditioning of the system.

    In **log-price space** ($x = \ln S$), the transformed PDE has constant coefficients:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 \frac{\partial^2 V}{\partial x^2} + \left(r - \frac{1}{2}\sigma^2\right)\frac{\partial V}{\partial x} - rV = 0
    $$

    The discretized tridiagonal coefficients are:

    $$
    a = -\frac{\Delta t}{2}\left(\frac{\sigma^2}{(\Delta x)^2} - \frac{r - \sigma^2/2}{2\Delta x}\right), \quad b = 1 + \Delta t\left(\frac{\sigma^2}{(\Delta x)^2} + r\right), \quad c = -\frac{\Delta t}{2}\left(\frac{\sigma^2}{(\Delta x)^2} + \frac{r - \sigma^2/2}{2\Delta x}\right)
    $$

    These are the **same for every row**, making the tridiagonal matrix a Toeplitz matrix (constant along each diagonal). This simplifies implementation and improves conditioning. Additionally, the uniform grid in $x = \ln S$ concentrates more grid points near small $S$ values where the option value changes rapidly, improving accuracy for puts near $S = 0$ without requiring a nonuniform mesh.

---

**Exercise 5.** For the American put, the implicit scheme is combined with early exercise projection: after solving the tridiagonal system, set $V_i = \max(V_i, \Phi_i)$ for all $i$. Explain why this projection approach is simpler to implement with the implicit scheme than with Crank-Nicolson. What is the overall convergence order of the projection + implicit method?

??? success "Solution to Exercise 5"
    In the **implicit scheme**, each time step proceeds in two stages for American options:

    1. Solve the tridiagonal system $A\mathbf{V}^{n} = \mathbf{V}^{n+1}$ to get provisional continuation values
    2. Apply the projection: $V_i^n \leftarrow \max(V_i^n, \Phi_i)$ for each $i$

    This is simple because the tridiagonal solve and the projection are **decoupled**: we first solve a linear system, then apply a pointwise maximum.

    With **Crank-Nicolson**, the scheme reads $A\mathbf{V}^n = B\mathbf{V}^{n+1} + \mathbf{b}$, where both sides involve unknown values at level $n$. The projection $V_i^n \geq \Phi_i$ creates a **linear complementarity problem** (LCP) rather than a simple linear system followed by projection. The naive approach of solving the linear system and then projecting can introduce oscillations because the Crank-Nicolson scheme couples the solution at time level $n$ with itself through the averaging of explicit and implicit parts. The constraint $V \geq \Phi$ at the new time level conflicts with the implicit portion of the scheme, leading to spurious oscillations near the exercise boundary.

    The overall convergence order of the **projection + implicit method** is $O(\Delta t + (\Delta S)^2)$, i.e., first-order in time and second-order in space. The projection step does not degrade the spatial accuracy, but the first-order temporal accuracy of the implicit scheme is the dominant error. This is one order lower in time than Crank-Nicolson ($O((\Delta t)^2)$), but the simplicity and robustness of the implicit projection method often make it preferable in practice.

---

**Exercise 6.** The implicit scheme introduces numerical dissipation that damps high-frequency oscillations. While this makes the scheme robust, it can cause over-smoothing of sharp features. For a digital (binary) option with payoff $\Phi(S) = 1$ if $S > K$ and $0$ otherwise, explain how this dissipation affects the numerical solution near $S = K$.

??? success "Solution to Exercise 6"
    A digital (binary) call has the payoff:

    $$
    \Phi(S) = \begin{cases} 1 & \text{if } S > K \\ 0 & \text{if } S \leq K \end{cases}
    $$

    This payoff has a **discontinuity** (jump) at $S = K$. On the finite difference grid, this appears as a sharp transition: $V_i^N = 0$ for $S_i \leq K$ and $V_i^N = 1$ for $S_i > K$.

    The implicit scheme's numerical dissipation acts like artificial diffusion. After one time step backward, the tridiagonal solve effectively applies a smoothing operator to the solution vector. The sharp jump at $S = K$ is spread out over several grid points, creating a smooth transition region of width proportional to $\sqrt{\Delta t}$ (from the diffusion) plus $\Delta S$ (from the spatial discretization).

    Specifically, the implicit scheme's modified equation includes a leading truncation error term proportional to $\frac{\Delta t}{2}\frac{\partial^2 V}{\partial t^2}$, which for the diffusion-dominated regime near the discontinuity acts as additional diffusion of magnitude $O(\Delta t \cdot \sigma^2)$. This:

    - **Smears the step function**: The numerical solution near $S = K$ transitions gradually from 0 to 1 over a band of width $O(\sigma\sqrt{\Delta t} + \Delta S)$, rather than jumping sharply
    - **Reduces peak values**: The maximum slope of the numerical solution is bounded by $O(1/\Delta S)$, whereas the true solution (the delta of the digital option) approaches a Dirac delta as $t \to T$
    - **Underestimates Greeks**: The numerical delta (the discrete derivative of the solution) near $S = K$ is artificially broadened and lowered

    To mitigate this, practitioners use **grid refinement** near $S = K$, place a grid point exactly at $S = K$, or use the Crank-Nicolson scheme (which has less numerical dissipation) combined with smoothing of the initial condition.
