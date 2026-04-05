# Crank-Nicolson Scheme: Implementation

The **Crank-Nicolson method** combines the accuracy of the explicit method with the stability of the implicit method. It is **second-order accurate** in both time and space, making it the preferred method in many financial engineering applications.

---

### The Idea

The Crank-Nicolson method uses the **average of the explicit and implicit finite difference approximations**:

$$
\frac{V_i^{n+1} - V_i^n}{\Delta t} = \frac{1}{2} \left( L V_i^n + L V_i^{n+1} \right)
$$

where $L$ is the spatial differential operator in the Black-Scholes PDE. This leads to a **tridiagonal linear system** at each time step with improved accuracy.

---

### Finite Difference Formulation

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

### Properties

| Feature            | Crank-Nicolson         |
|--------------------|------------------------|
| Stability          | Unconditionally stable |
| Time Accuracy      | Second-order           |
| Space Accuracy     | Second-order           |
| Cost per time step | Moderate               |
| Overall performance| Excellent              |

---

### Python Implementation: European Call

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

### Python Implementation: European Put

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

### Python Implementation: American Call

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

### Python Implementation: American Put

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

### Interpretation

- The **Crank-Nicolson method** gives a nearly perfect match to the analytical solution.
- It achieves this with **fewer time steps** compared to the explicit method, thanks to its higher-order accuracy.
- It is stable and efficient even with relatively large time steps.

---

### Summary

- The Crank-Nicolson scheme offers a **balance between accuracy and stability**.
- It requires solving a tridiagonal system at each time step, like the implicit method.
- It is **ideal for production-quality option pricing engines**, especially for European-style derivatives.

---

## Exercises

**Exercise 1.** Write out the Crank-Nicolson update in component form: express $u_j^{n+1}$ as a function of $u_{j-1}^{n+1}$, $u_j^{n+1}$, $u_{j+1}^{n+1}$ and $u_{j-1}^n$, $u_j^n$, $u_{j+1}^n$. Identify the left-hand side matrix and right-hand side matrix coefficients.

??? success "Solution to Exercise 1"
    The Crank-Nicolson scheme averages the spatial operator between time levels $n$ and $n+1$. Starting from the Black-Scholes PDE written as $\partial V/\partial t = LV$ (where $L$ is the spatial operator), the CN discretization is:

    $$
    \frac{V_j^{n+1} - V_j^n}{\Delta t} = \frac{1}{2}(LV_j^n + LV_j^{n+1})
    $$

    Using central differences for the spatial operator at grid point $j$ with $S_j = j\Delta S$:

    $$
    LV_j = \frac{1}{2}\sigma^2 j^2 (V_{j+1} - 2V_j + V_{j-1}) + \frac{rj}{2}(V_{j+1} - V_{j-1}) - rV_j
    $$

    Define the coefficients:

    $$
    \alpha_j = \frac{\Delta t}{4}(\sigma^2 j^2 - rj), \quad \beta_j = \frac{\Delta t}{2}(\sigma^2 j^2 + r), \quad \gamma_j = \frac{\Delta t}{4}(\sigma^2 j^2 + rj)
    $$

    The **left-hand side** (unknowns at level $n+1$):

    $$
    -\alpha_j V_{j-1}^{n+1} + (1 + \beta_j) V_j^{n+1} - \gamma_j V_{j+1}^{n+1}
    $$

    The **right-hand side** (known values at level $n$):

    $$
    \alpha_j V_{j-1}^n + (1 - \beta_j) V_j^n + \gamma_j V_{j+1}^n
    $$

    In matrix form, the LHS matrix $A$ has entries:

    $$
    A = \begin{pmatrix} 1+\beta_1 & -\gamma_1 & & \\ -\alpha_2 & 1+\beta_2 & -\gamma_2 & \\ & \ddots & \ddots & \ddots \\ & & -\alpha_{M-1} & 1+\beta_{M-1} \end{pmatrix}
    $$

    The RHS matrix $B$ has entries:

    $$
    B = \begin{pmatrix} 1-\beta_1 & \gamma_1 & & \\ \alpha_2 & 1-\beta_2 & \gamma_2 & \\ & \ddots & \ddots & \ddots \\ & & \alpha_{M-1} & 1-\beta_{M-1} \end{pmatrix}
    $$

    The system solved at each time step is $A\mathbf{V}^{n+1} = B\mathbf{V}^n + \mathbf{b}_{\text{boundary}}$.

---

**Exercise 2.** Using the parameters $S_0 = 100$, $K = 100$, $T = 1$, $r = 0.05$, $\sigma = 0.2$, $M = 100$, compare the Crank-Nicolson solution in original space vs log-space. Which coordinate system produces a smaller maximum absolute error? Explain why log-space is expected to perform better for puts at small $S$ values.

??? success "Solution to Exercise 2"
    With $S_0 = 100$, $K = 100$, $T = 1$, $r = 0.05$, $\sigma = 0.2$, $M = 100$, both CN implementations (original and log-space) closely match the analytical Black-Scholes price. However, the **log-space** formulation typically produces a smaller maximum absolute error for the following reasons:

    1. **Uniform resolution where it matters**: In log-space, $x = \ln S$ with a uniform grid $\Delta x$ provides finer resolution near $S = 0$ (where $\Delta S$ is effectively very small) and coarser resolution at large $S$ (where the option value is nearly linear). For a put option, the payoff curvature is concentrated near $S = K$ and below, exactly where log-space provides better coverage.

    2. **Constant coefficients**: The log-space PDE has constant diffusion coefficient $\sigma^2/2$, eliminating the $S^2$-dependent diffusion that causes the original-space scheme to lose accuracy at large $S$.

    3. **Better conditioning**: The constant-coefficient tridiagonal system in log-space has a more uniform condition number, leading to smaller roundoff error amplification.

    For puts at small $S$ values, the payoff $\max(K - S, 0) \approx K$ varies slowly, but the option's **delta** changes rapidly as $S$ approaches zero. In original space with uniform $\Delta S$, these rapid changes may not be resolved. In log-space, the transformation $x = \ln S$ stretches the small-$S$ region, placing many grid points where they are most needed.

---

**Exercise 3.** The Crank-Nicolson scheme averages the spatial operator between time levels $n$ and $n+1$. Show that this averaging is equivalent to applying the trapezoidal rule to the ODE system $d\mathbf{u}/d\tau = A\mathbf{u}$, and explain why the trapezoidal rule is second-order accurate.

??? success "Solution to Exercise 3"
    The spatial semi-discretization of the Black-Scholes PDE produces an ODE system:

    $$
    \frac{d\mathbf{u}}{d\tau} = A\mathbf{u}
    $$

    where $\tau = T - t$ is the forward time variable and $A$ is the matrix from the spatial discretization. The **trapezoidal rule** applied to this ODE from $\tau_n$ to $\tau_{n+1} = \tau_n + \Delta t$ is:

    $$
    \mathbf{u}^{n+1} = \mathbf{u}^n + \frac{\Delta t}{2}\left(A\mathbf{u}^n + A\mathbf{u}^{n+1}\right)
    $$

    Rearranging:

    $$
    \left(I - \frac{\Delta t}{2}A\right)\mathbf{u}^{n+1} = \left(I + \frac{\Delta t}{2}A\right)\mathbf{u}^n
    $$

    This is exactly the Crank-Nicolson scheme, confirming the equivalence.

    The trapezoidal rule is second-order accurate because of its **symmetry**. The local truncation error is obtained by Taylor-expanding $\mathbf{u}(\tau + \Delta t)$:

    $$
    \mathbf{u}(\tau + \Delta t) = \mathbf{u}(\tau) + \Delta t\, \mathbf{u}'(\tau) + \frac{(\Delta t)^2}{2}\mathbf{u}''(\tau) + \frac{(\Delta t)^3}{6}\mathbf{u}'''(\tau) + O((\Delta t)^4)
    $$

    The trapezoidal rule approximates the integral $\int_{\tau}^{\tau+\Delta t} f(s)\, ds$ by $\frac{\Delta t}{2}(f(\tau) + f(\tau+\Delta t))$. Expanding $f(\tau + \Delta t) = f(\tau) + \Delta t f'(\tau) + \frac{(\Delta t)^2}{2}f''(\tau) + \cdots$ and substituting:

    $$
    \frac{\Delta t}{2}(f(\tau) + f(\tau + \Delta t)) = \Delta t\, f(\tau) + \frac{(\Delta t)^2}{2}f'(\tau) + \frac{(\Delta t)^3}{4}f''(\tau) + \cdots
    $$

    Comparing with the exact integral $\Delta t\, f(\tau) + \frac{(\Delta t)^2}{2}f'(\tau) + \frac{(\Delta t)^3}{6}f''(\tau) + \cdots$, the first discrepancy is at $O((\Delta t)^3)$, confirming second-order accuracy in time.

---

**Exercise 4.** For the American call implementation in the code above, the explicit scheme with early exercise is used instead of Crank-Nicolson. Explain why the Crank-Nicolson scheme with projection can produce spurious oscillations for American options, and describe the Rannacher time-stepping fix.

??? success "Solution to Exercise 4"
    The Crank-Nicolson scheme with early exercise projection for American options can produce **spurious oscillations** near the exercise boundary. The mechanism is as follows:

    1. The CN scheme treats the spatial operator as an average of explicit and implicit evaluations: $\frac{1}{2}(L^n + L^{n+1})$. This implicit-explicit coupling means the scheme "looks ahead" to the next time level.

    2. For American options, the early exercise constraint $V \geq \Phi$ (where $\Phi$ is the payoff) creates a **free boundary** separating the exercise region from the continuation region. At the free boundary, the solution has a discontinuity in its second derivative.

    3. The CN scheme applied to a solution with a kink (discontinuous second derivative) suffers from the same problem as applying the trapezoidal rule to a non-smooth function: the second-order accuracy breaks down, and the scheme generates oscillations of amplitude $O(\Delta t)$ that do not damp out. These oscillations appear as a checkerboard pattern near the exercise boundary.

    4. The naive projection (solve CN system, then apply $\max(V, \Phi)$) does not properly couple the free boundary condition with the CN time-stepping, exacerbating the oscillation problem.

    The **Rannacher time-stepping** fix replaces the first few Crank-Nicolson steps (typically 2--4 steps from maturity) with fully implicit steps. Since the implicit scheme has strong numerical dissipation, it damps out the high-frequency oscillations triggered by the non-smooth terminal condition. After these initial implicit steps, the solution is sufficiently smooth for the CN scheme to proceed without oscillations. Specifically:

    - Use $\Delta t_{\text{impl}} = \Delta t / 2$ for the first 2--4 half-steps (fully implicit)
    - Switch to standard CN for all remaining time steps

    This preserves the overall $O((\Delta t)^2 + (\Delta S)^2)$ convergence rate of CN while eliminating the spurious oscillations.

---

**Exercise 5.** The boundary condition $\mathbf{b}_{\text{boundary}}$ in the Crank-Nicolson system $A\mathbf{V}^{n+1} = B\mathbf{V}^n + \mathbf{b}_{\text{boundary}}$ depends on the boundary values at both time levels $n$ and $n+1$. Explain why both boundary values contribute and write down the explicit form of the boundary vector for a European call.

??? success "Solution to Exercise 5"
    The CN system at each time step is:

    $$
    A\mathbf{V}^{n+1} = B\mathbf{V}^n + \mathbf{b}_{\text{boundary}}
    $$

    Both boundary values at levels $n$ and $n+1$ contribute because the CN scheme evaluates the spatial operator at **both** time levels. Specifically, the equations for the first interior point ($j = 1$) and the last interior point ($j = M-1$) involve boundary values $V_0$ and $V_M$:

    At $j = 1$: the spatial stencil at level $n+1$ uses $V_0^{n+1}$ (from the LHS matrix), and the stencil at level $n$ uses $V_0^n$ (from the RHS matrix). Since $V_0$ is a known boundary value (not an unknown), these terms are moved to the right-hand side.

    Similarly at $j = M-1$: both $V_M^{n+1}$ and $V_M^n$ appear and are moved to the boundary vector.

    For a **European call** with boundary conditions $V_0^n = 0$ (at $S = 0$) and $V_M^n = S_{\max} - Ke^{-r(T - t_n)}$ (at $S = S_{\max}$), define $g^n = V_M^n = S_{\max} - Ke^{-r(T-t_n)}$. The boundary vector is:

    $$
    \mathbf{b}_{\text{boundary}} = \begin{pmatrix} \alpha_1 V_0^n + \alpha_1 V_0^{n+1} \\ 0 \\ \vdots \\ 0 \\ \gamma_{M-1} g^n + \gamma_{M-1} g^{n+1} \end{pmatrix}
    $$

    Since $V_0^n = V_0^{n+1} = 0$ for a call, the first entry vanishes. The last entry simplifies to:

    $$
    \gamma_{M-1}(g^n + g^{n+1}) = \gamma_{M-1}\left[(S_{\max} - Ke^{-r(T-t_n)}) + (S_{\max} - Ke^{-r(T-t_{n+1})})\right]
    $$

    where $\gamma_{M-1} = \frac{\Delta t}{4}(\sigma^2(M-1)^2 + r(M-1))$. Both time-level boundary values contribute because the CN averaging requires evaluating the spatial operator at both $t_n$ and $t_{n+1}$.

---

**Exercise 6.** If you double the spatial resolution from $M = 100$ to $M = 200$ while keeping $N$ fixed, what happens to the Crank-Nicolson solution accuracy? What is the optimal relationship between $M$ and $N$ for the Crank-Nicolson scheme to achieve balanced spatial and temporal accuracy?

??? success "Solution to Exercise 6"
    The Crank-Nicolson scheme has global truncation error $O((\Delta t)^2 + (\Delta S)^2)$. With $M$ spatial points and $N$ time steps, $\Delta S = S_{\max}/M$ and $\Delta t = T/N$.

    **Doubling $M$ from 100 to 200 with $N$ fixed**: $\Delta S$ is halved, so $(\Delta S)^2$ decreases by a factor of 4. However, $\Delta t$ remains unchanged. The total error becomes:

    $$
    E \sim C_1 (\Delta t)^2 + C_2 (\Delta S)^2 = C_1 (\Delta t)^2 + \frac{C_2}{4}(\Delta S_{\text{old}})^2
    $$

    If the original error was spatially dominated ($C_2(\Delta S)^2 \gg C_1(\Delta t)^2$), doubling $M$ significantly improves accuracy. But if the temporal error was already dominant, the improvement is negligible because the $(\Delta t)^2$ term is unchanged. Eventually, further spatial refinement yields no benefit --- the solution is "time-error limited."

    **Optimal relationship**: To balance spatial and temporal errors:

    $$
    (\Delta t)^2 \sim (\Delta S)^2 \implies \Delta t \sim \Delta S \implies \frac{T}{N} \sim \frac{S_{\max}}{M}
    $$

    Therefore:

    $$
    N \sim M \cdot \frac{T}{S_{\max}}
    $$

    With $T = 1$ and $S_{\max} = 300$, the balanced relationship is $N \sim M/300$. For $M = 100$, only $N \approx 1$ would suffice for balance, but in practice one uses at least $N = O(M)$ to ensure stability of the tridiagonal solver and adequate resolution of early exercise boundaries.

    In log-space where $\Delta x = (\ln S_{\max} - \ln S_{\min})/M$, the balance condition $\Delta t \sim \Delta x$ gives $N \sim M \cdot T / (\ln S_{\max} - \ln S_{\min})$, which for typical parameters yields $N \sim M$, a more natural scaling.

    The key practical takeaway: for Crank-Nicolson, always refine $M$ and $N$ together (typically $N \propto M$) to take full advantage of the second-order convergence in both dimensions.
