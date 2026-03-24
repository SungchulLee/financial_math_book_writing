# Penalty Method

The **penalty method** replaces the hard early exercise constraint of the American option problem with a smooth penalty term. Instead of solving a linear complementarity problem directly, one solves a nonlinear PDE that approximates the free boundary problem with controllable accuracy. This approach is attractive for its simplicity and compatibility with standard PDE solvers.

---

## The Penalty Approximation

### From Complementarity to Penalization

Recall the American option variational inequality in complementarity form:

$$
\left(-\frac{\partial V}{\partial t} - \mathcal{L}V + rV\right) \geq 0, \quad V \geq \Phi, \quad \left(-\frac{\partial V}{\partial t} - \mathcal{L}V + rV\right)(V - \Phi) = 0
$$

The penalty method relaxes the hard constraint $V \geq \Phi$ by adding a **penalty term** that penalizes violations:

$$
\boxed{
\frac{\partial V^\rho}{\partial t} + \mathcal{L}V^\rho - rV^\rho + \rho\,(V^\rho - \Phi)^- = 0
}
$$

where $(x)^- = \min(x, 0)$ is the negative part and $\rho > 0$ is the **penalty parameter**.

!!! info "Intuition"
    When $V^\rho > \Phi$ (continuation region), the penalty term $(V^\rho - \Phi)^- = 0$ vanishes and the standard Black-Scholes PDE holds. When $V^\rho < \Phi$ (violation of the constraint), the penalty term $\rho(V^\rho - \Phi)^-$ is a large negative number that forces $V^\rho$ back toward $\Phi$. As $\rho \to \infty$, the penalized solution $V^\rho$ converges to the true American option price $V$.

### Alternative Penalty Functions

The negative part function $(x)^-$ is the simplest choice, but other penalty functions are used in practice:

| Penalty function $p(x)$ | Formula | Smoothness |
|:---|:---|:---|
| Negative part | $(x)^- = \min(x, 0)$ | Lipschitz (not $C^1$) |
| Smoothed negative part | $-\frac{1}{2}(\sqrt{x^2 + \epsilon^2} - x)$ | $C^\infty$ |
| Exponential | $-\frac{1}{\alpha}e^{-\alpha x}$ for $x < 0$ | $C^\infty$ |
| Power penalty | $[(x)^-]^{1/k}$ with $k > 1$ | $C^0$ |

The smoothed variants avoid the non-differentiability at $x = 0$, which can improve the convergence of Newton's method.

---

## Convergence of the Penalty Approximation

### Error Bound

**Theorem (Penalty Convergence).** *Let $V$ be the solution of the American option variational inequality and $V^\rho$ the solution of the penalized PDE. Then:*

$$
\boxed{0 \leq V - V^\rho \leq \frac{C}{\rho}}
$$

*where $C > 0$ depends on the problem data but not on $\rho$.*

??? note "Proof Sketch"
    **Lower bound** ($V^\rho \leq V$): The penalized equation can be written as

    $$
    -\frac{\partial V^\rho}{\partial t} - \mathcal{L}V^\rho + rV^\rho = \rho(V^\rho - \Phi)^- \leq 0
    $$

    Since $V$ satisfies $-\frac{\partial V}{\partial t} - \mathcal{L}V + rV \geq 0$, the difference $w = V - V^\rho$ satisfies a differential inequality with non-negative boundary and terminal data. By the maximum principle, $w \geq 0$.

    **Upper bound**: In the exercise region where $V = \Phi$, the penalized solution satisfies $V^\rho \geq \Phi - C/\rho$ for some constant $C$ (since the penalty term forces $\rho|V^\rho - \Phi| \leq C$ when $V^\rho < \Phi$). In the continuation region, $V^\rho$ satisfies the same PDE as $V$. Combining these estimates via comparison principles yields the $O(1/\rho)$ bound. $\square$

!!! tip "Practical Implication"
    The $O(1/\rho)$ convergence rate means that each factor-of-10 increase in $\rho$ gains roughly one decimal digit of accuracy. Typical choices:

    - $\rho = 10^4$: error $\sim 10^{-4}$ (moderate accuracy)
    - $\rho = 10^6$: error $\sim 10^{-6}$ (sufficient for most applications)
    - $\rho = 10^8$: error $\sim 10^{-8}$ (high precision, may cause conditioning issues)

---

## Discrete Formulation

### Time Discretization

Applying implicit Euler to the penalized PDE yields the nonlinear system at each time step:

$$
\frac{\mathbf{u}^{n+1} - \mathbf{u}^n}{\Delta\tau} + A\mathbf{u}^{n+1} + \rho\,\mathbf{p}(\mathbf{u}^{n+1}) = \mathbf{0}
$$

where $\mathbf{p}(\mathbf{u})$ is the componentwise penalty: $p_j(u_j) = (u_j - \Phi_j)^- = \min(u_j - \Phi_j, 0)$.

Rearranging:

$$
(I + \Delta\tau\, A)\mathbf{u}^{n+1} + \Delta\tau\,\rho\,\mathbf{p}(\mathbf{u}^{n+1}) = \mathbf{u}^n
$$

### Matrix Formulation with Indicator

Define the diagonal indicator matrix $P(\mathbf{u})$ with entries:

$$
P_{jj}(\mathbf{u}) = \begin{cases} 1 & \text{if } u_j < \Phi_j \\ 0 & \text{if } u_j \geq \Phi_j \end{cases}
$$

Then the penalty term can be written as $\mathbf{p}(\mathbf{u}) = P(\mathbf{u})(\mathbf{u} - \boldsymbol{\Phi})$, and the system becomes:

$$
\left(I + \Delta\tau\, A + \Delta\tau\,\rho\, P(\mathbf{u}^{n+1})\right)\mathbf{u}^{n+1} = \mathbf{u}^n + \Delta\tau\,\rho\, P(\mathbf{u}^{n+1})\boldsymbol{\Phi}
$$

Since $P$ depends on $\mathbf{u}^{n+1}$, this is a **nonlinear** system that must be solved iteratively.

---

## Newton's Method for the Penalty System

### Linearization

Define the residual:

$$
F(\mathbf{u}) = (I + \Delta\tau\, A)\mathbf{u} + \Delta\tau\,\rho\,\mathbf{p}(\mathbf{u}) - \mathbf{u}^n
$$

Newton's method solves $F(\mathbf{u}) = \mathbf{0}$ iteratively:

$$
\mathbf{u}^{(k+1)} = \mathbf{u}^{(k)} - [J(\mathbf{u}^{(k)})]^{-1} F(\mathbf{u}^{(k)})
$$

The Jacobian is:

$$
J(\mathbf{u}) = I + \Delta\tau\, A + \Delta\tau\,\rho\, P(\mathbf{u})
$$

Since $P$ is diagonal, $J$ is tridiagonal (same sparsity as $I + \Delta\tau A$), so the Newton step reduces to a **tridiagonal solve** --- the same cost as an unconstrained implicit step.

### Convergence of Newton's Method

!!! warning "Non-Smoothness"
    The penalty function $p(x) = (x)^-$ has a discontinuous derivative at $x = 0$. Strictly speaking, Newton's method applies to the generalized Jacobian. In practice, this causes no difficulty: Newton's method converges in 2-4 iterations for typical $\rho$ values.

    Using a smoothed penalty function (e.g., the smoothed negative part with parameter $\epsilon = 1/\rho$) restores classical quadratic convergence of Newton's method.

### Algorithm

!!! abstract "Algorithm: Penalty Method with Newton Iteration"
    **Input:** Time-stepping matrix $I + \Delta\tau A$, previous solution $\mathbf{u}^n$, payoff $\boldsymbol{\Phi}$, penalty parameter $\rho$, tolerance $\varepsilon$.

    **For** each time step $n = 0, 1, \ldots, N-1$:

    1. Set initial guess $\mathbf{u}^{(0)} = \mathbf{u}^n$.
    2. **Repeat** for $k = 0, 1, 2, \ldots$:
        - Compute indicator: $P_{jj} = 1$ if $u_j^{(k)} < \Phi_j$, else $0$.
        - Form $J = I + \Delta\tau A + \Delta\tau\rho\, P$.
        - Compute residual: $F = (I + \Delta\tau A)\mathbf{u}^{(k)} + \Delta\tau\rho\, P(\mathbf{u}^{(k)} - \boldsymbol{\Phi}) - \mathbf{u}^n$.
        - Solve $J\,\delta\mathbf{u} = -F$ (tridiagonal solve).
        - Update: $\mathbf{u}^{(k+1)} = \mathbf{u}^{(k)} + \delta\mathbf{u}$.
        - **If** $\|\delta\mathbf{u}\|_\infty < \varepsilon$, **break**.
    3. Set $\mathbf{u}^{n+1} = \mathbf{u}^{(k+1)}$.

    **End For**

---

## Fixed-Point Iteration Alternative

For simplicity, one can use a **fixed-point (Picard) iteration** instead of Newton's method:

1. Given $\mathbf{u}^{(k)}$, compute $P = P(\mathbf{u}^{(k)})$.
2. Solve the **linear** system $(I + \Delta\tau A + \Delta\tau\rho\, P)\mathbf{u}^{(k+1)} = \mathbf{u}^n + \Delta\tau\rho\, P\boldsymbol{\Phi}$.
3. Repeat until convergence.

This is equivalent to "lagging" the indicator $P$ by one iteration. It converges for sufficiently large $\rho$ but may require more iterations than Newton's method. In practice, the fixed-point iteration also converges in 2-5 iterations for well-chosen $\rho$.

---

## Conditioning and Choice of Penalty Parameter

### The Conditioning Dilemma

Large $\rho$ improves the approximation accuracy ($O(1/\rho)$ error) but worsens the conditioning of the Jacobian $J$. The condition number scales as:

$$
\kappa(J) \sim \rho \cdot \Delta\tau
$$

in the exercise region, since the diagonal entries of $J$ in the exercise region are of order $1 + \Delta\tau\rho$.

### Practical Guidelines

| Parameter | Typical range | Notes |
|:---|:---|:---|
| $\rho$ | $10^4$ to $10^8$ | Balance accuracy vs. conditioning |
| Newton tolerance | $10^{-10}$ to $10^{-12}$ | Tighter than penalty error |
| Max Newton iterations | 5-10 | Convergence usually in 2-4 |

!!! tip "Rule of Thumb"
    Choose $\rho$ so that the penalty error $O(1/\rho)$ is smaller than the discretization error $O(\Delta\tau + h^2)$. For a grid with $h = 0.01$ (space) and $\Delta\tau = 0.01$ (time), the discretization error is $O(10^{-2})$, so $\rho = 10^4$ already suffices.

---

## Worked Example

Consider an American put with $K = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$, on a 3-point interior grid with $S_1 = 40$, $S_2 = 80$, $S_3 = 120$.

**Setup:** $\boldsymbol{\Phi} = (60, 20, 0)^T$, $\mathbf{u}^n = (58, 18, 2)^T$, $\Delta\tau = 0.01$, $\rho = 10^4$.

**Iteration 1:** Starting from $\mathbf{u}^{(0)} = \mathbf{u}^n = (58, 18, 2)^T$.

Compute the indicator: $u_1 = 58 < 60 = \Phi_1$ so $P_{11} = 1$; $u_2 = 18 < 20 = \Phi_2$ so $P_{22} = 1$; $u_3 = 2 > 0 = \Phi_3$ so $P_{33} = 0$.

The Jacobian $J$ has the same structure as $I + \Delta\tau A$ but with $\Delta\tau\rho = 100$ added to diagonal entries $j = 1, 2$. This makes $J_{11}$ and $J_{22}$ very large, effectively forcing $u_1 \approx \Phi_1 = 60$ and $u_2 \approx \Phi_2 = 20$ in the exercise region.

After the Newton step, the solution is approximately:

$$
\mathbf{u}^{(1)} \approx (60.00, 20.00, 2.05)^T
$$

The first two components are pinned to the payoff (up to $O(1/\rho)$ error), while the third satisfies the unconstrained PDE. After one more Newton step, convergence is achieved.

**Comparison with exact LCP solution:** The exact LCP gives $(60, 20, 2.05)^T$, confirming the penalty method with $\rho = 10^4$ is accurate to several decimal places on this grid.

---

## Comparison with PSOR

| Aspect | Penalty method | PSOR |
|:---|:---|:---|
| **Formulation** | Smooth nonlinear PDE | Iterative LCP solve |
| **Constraint handling** | Soft (penalty approximation) | Exact (projection) |
| **Approximation error** | $O(1/\rho)$ from penalization | None (solves LCP exactly to tolerance) |
| **Solver per time step** | Newton (2-4 iterations) | PSOR (5-20 iterations) |
| **Cost per iteration** | One tridiagonal solve | One sweep ($O(m)$) |
| **Parameter tuning** | $\rho$ (penalty) | $\omega$ (relaxation) |
| **Extension to higher dimensions** | Natural (standard PDE solver) | More complex |
| **Conditioning** | Degrades with large $\rho$ | Unaffected |

!!! tip "When to Use Which"
    - **Penalty method**: Preferred when an existing PDE solver infrastructure is available, or in higher dimensions where PSOR is less natural. The penalty term is easy to add to any implicit time-stepping code.
    - **PSOR**: Preferred when exact LCP solutions are required without approximation error, or when conditioning is a concern.

---

## Extension to Higher Dimensions

A major advantage of the penalty method is its natural extension to multi-dimensional problems (e.g., American options on multiple assets). The penalized PDE in $d$ dimensions is:

$$
\frac{\partial V^\rho}{\partial t} + \mathcal{L}_d V^\rho - rV^\rho + \rho(V^\rho - \Phi)^- = 0
$$

where $\mathcal{L}_d$ is the multi-dimensional Black-Scholes operator. The penalty term does not change the sparsity structure of the discretization matrix, so standard multi-dimensional PDE solvers (ADI, operator splitting) can be used with only minor modifications.

---

## Summary

| Concept | Key point |
|:---|:---|
| Core idea | Replace hard constraint $V \geq \Phi$ with penalty term $\rho(V - \Phi)^-$ |
| Convergence | $V^\rho \to V$ as $\rho \to \infty$ with error $O(1/\rho)$ |
| Discrete solver | Newton's method on penalized nonlinear system (2-4 iterations) |
| Cost per step | Same as unconstrained solve (tridiagonal) plus Newton iterations |
| Conditioning | Degrades with large $\rho$; balance against discretization error |
| Advantage | Simple implementation, natural multi-dimensional extension |
| Limitation | Introduces approximation error; conditioning sensitivity |

---

## Exercises

**Exercise 1.** For the penalty method with $\rho = 10^6$, estimate the penalty approximation error $O(1/\rho)$. If the discretization error is $O(h^2)$ with $h = 0.01$, is the penalty error negligible? What value of $\rho$ would balance the penalty and discretization errors?

---

**Exercise 2.** Write out one iteration of Newton's method for the penalty system at a single time step. Given $\mathbf{u}^{(0)} = \mathbf{u}^n = (58, 18, 2)^T$ with $\boldsymbol{\Phi} = (60, 20, 0)^T$ and $\rho = 10^4$, compute the indicator matrix $P$ and describe qualitatively how the Newton step adjusts the solution.

---

**Exercise 3.** The penalty function $(x)^- = \min(x, 0)$ has a discontinuous derivative at $x = 0$. Describe the smoothed penalty function $p(x) = -\frac{1}{2}(\sqrt{x^2 + \epsilon^2} - x)$ and explain how it approximates $(x)^-$. For what choice of $\epsilon$ relative to $\rho$ does the smoothing not affect the overall penalty accuracy?

---

**Exercise 4.** The condition number of the Jacobian scales as $\kappa(J) \sim \rho\Delta\tau$ in the exercise region. For $\rho = 10^8$ and $\Delta\tau = 0.01$, estimate $\kappa(J)$. At what point does the conditioning become problematic for double-precision floating-point arithmetic?

---

**Exercise 5.** Compare the penalty method and PSOR for pricing an American put. If the penalty method uses 3 Newton iterations per time step (each costing one tridiagonal solve) and PSOR uses 12 iterations per time step (each costing one sweep), which method is faster per time step? Consider that a tridiagonal solve costs approximately $5M$ operations and a PSOR sweep costs approximately $3M$ operations.

---

**Exercise 6.** The penalty method extends naturally to multi-dimensional problems. For a two-asset American option with a 2D spatial grid of size $M \times M$, the penalty term does not change the sparsity structure of the discretization matrix. Explain why this is a significant advantage over PSOR, which is less natural in higher dimensions.
