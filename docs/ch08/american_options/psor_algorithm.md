# PSOR Algorithm

The **Projected Successive Over-Relaxation (PSOR)** algorithm is the workhorse iterative method for solving the linear complementarity problems that arise in American option pricing. It combines the classical SOR iteration for linear systems with a projection step that enforces the early exercise constraint, yielding an efficient and robust solver.

---

## Motivation: From SOR to PSOR

### SOR for Linear Systems

Recall the **Successive Over-Relaxation (SOR)** method for solving $L\mathbf{u} = \mathbf{q}$. Decompose $L = D - E - F$ where $D$ is the diagonal, $-E$ is the strict lower triangle, and $-F$ is the strict upper triangle. The SOR iteration is:

$$
u_j^{(k+1)} = (1 - \omega)\,u_j^{(k)} + \frac{\omega}{l_{jj}}\left(q_j - \sum_{i < j} l_{ji}\,u_i^{(k+1)} - \sum_{i > j} l_{ji}\,u_i^{(k)}\right)
$$

where $\omega \in (0, 2)$ is the relaxation parameter. For $\omega = 1$ this reduces to Gauss-Seidel; for $\omega > 1$ it is over-relaxation (accelerated convergence for many problems).

### Adding the Projection

For the LCP, we must additionally enforce $\mathbf{u} \geq \boldsymbol{\Phi}$. The PSOR method achieves this by **projecting** after each component update:

1. Compute the SOR update $\tilde{u}_j^{(k+1)}$ as above.
2. Set $u_j^{(k+1)} = \max(\tilde{u}_j^{(k+1)}, \Phi_j)$.

This projection ensures the constraint is satisfied at every iteration, and the complementarity condition emerges naturally at convergence.

---

## The PSOR Algorithm

!!! abstract "Algorithm: PSOR for LCP"
    **Input:** Matrix $L \in \mathbb{R}^{m \times m}$, vectors $\mathbf{q}, \boldsymbol{\Phi} \in \mathbb{R}^m$, relaxation parameter $\omega \in (1, 2)$, tolerance $\varepsilon > 0$, initial guess $\mathbf{u}^{(0)}$.

    **Repeat** for $k = 0, 1, 2, \ldots$:

    &emsp; **For** $j = 1, 2, \ldots, m$:

    $$
    \tilde{u}_j^{(k+1)} = (1 - \omega)\,u_j^{(k)} + \frac{\omega}{l_{jj}}\left(q_j - \sum_{i < j} l_{ji}\,u_i^{(k+1)} - \sum_{i > j} l_{ji}\,u_i^{(k)}\right)
    $$

    $$
    u_j^{(k+1)} = \max\!\left(\tilde{u}_j^{(k+1)},\; \Phi_j\right)
    $$

    &emsp; **End For**

    **Until** $\|\mathbf{u}^{(k+1)} - \mathbf{u}^{(k)}\|_\infty < \varepsilon$

    **Output:** $\mathbf{u}^{(k+1)}$ (approximate LCP solution)

!!! info "Role of the Projection"
    The $\max$ operation acts as a **projection onto the feasible set** $\{\mathbf{u} : \mathbf{u} \geq \boldsymbol{\Phi}\}$. At convergence, grid points in the exercise region satisfy $u_j = \Phi_j$ with $(L\mathbf{u})_j > q_j$, and points in the continuation region satisfy $u_j > \Phi_j$ with $(L\mathbf{u})_j = q_j$. The complementarity condition holds automatically.

---

## Convergence Theory

### Convergence Theorem

**Theorem.** *Let $L$ be an M-matrix with positive diagonal entries $l_{jj} > 0$. Then the PSOR algorithm converges to the unique solution of $\mathrm{LCP}(L, \mathbf{q}, \boldsymbol{\Phi})$ for any relaxation parameter $\omega \in (0, 2)$ and any initial guess $\mathbf{u}^{(0)} \geq \boldsymbol{\Phi}$.*

??? note "Proof Sketch"
    The proof relies on the **monotonicity** of the PSOR iteration when $L$ is an M-matrix.

    1. **Monotone operator:** Since $L$ is an M-matrix, the mapping $T_\omega : \mathbf{u}^{(k)} \mapsto \mathbf{u}^{(k+1)}$ defined by the PSOR iteration is a monotone operator on the lattice $\{\mathbf{u} : \mathbf{u} \geq \boldsymbol{\Phi}\}$. That is, $\mathbf{u}^{(k)} \leq \mathbf{v}^{(k)}$ componentwise implies $T_\omega(\mathbf{u}^{(k)}) \leq T_\omega(\mathbf{v}^{(k)})$.

    2. **Contraction:** The spectral radius of the SOR iteration matrix $G_\omega = (D - \omega E)^{-1}[(1-\omega)D + \omega F]$ satisfies $\rho(G_\omega) < 1$ for $\omega \in (0, 2)$ when $L$ is an M-matrix. The projection does not increase the distance to the fixed point.

    3. **Fixed point:** The limit $\mathbf{u}^* = \lim_{k \to \infty} \mathbf{u}^{(k)}$ satisfies the LCP conditions by continuity of the iteration and the $\max$ operation. $\square$

### Rate of Convergence

The convergence rate depends on the spectral radius of the iteration matrix. For the tridiagonal systems arising from one-dimensional finite difference discretizations:

- **Gauss-Seidel** ($\omega = 1$): $\rho(G_1) \approx 1 - c\,h^2$ where $h$ is the grid spacing, so convergence is slow on fine grids.
- **Optimal SOR**: The optimal relaxation parameter satisfies

$$
\omega^* = \frac{2}{1 + \sqrt{1 - \rho(G_1)^2}}
$$

which yields $\rho(G_{\omega^*}) = \omega^* - 1$. For the Black-Scholes discretization, $\omega^* \approx 1.2$ to $1.5$ depending on the grid parameters.

- **Practical observation**: With near-optimal $\omega$, PSOR typically converges in 5-20 iterations per time step, compared to 50-200 for Gauss-Seidel on the same grid.

---

## Implementation Details

### Choosing the Relaxation Parameter

The optimal $\omega$ depends on the spectral radius of the Gauss-Seidel iteration matrix, which in turn depends on the grid spacing, time step, and model parameters. In practice:

| Approach | Method |
|:---|:---|
| Analytical estimate | Use $\omega^* = 2/(1 + \sqrt{1 - \rho^2})$ with estimated $\rho$ |
| Empirical tuning | Try $\omega \in \{1.0, 1.1, 1.2, \ldots, 1.8\}$ on a test problem |
| Adaptive | Update $\omega$ during iteration based on convergence rate |

For typical American option parameters with $M = 100$-$500$ grid points, $\omega \in [1.2, 1.5]$ works well.

### Stopping Criteria

Several criteria are used in practice:

1. **Absolute change**: $\|\mathbf{u}^{(k+1)} - \mathbf{u}^{(k)}\|_\infty < \varepsilon$
2. **Relative change**: $\|\mathbf{u}^{(k+1)} - \mathbf{u}^{(k)}\|_\infty / \|\mathbf{u}^{(k+1)}\|_\infty < \varepsilon$
3. **Residual**: $\max_j \min\left((L\mathbf{u}^{(k+1)} - \mathbf{q})_j,\; u_j^{(k+1)} - \Phi_j\right) < \varepsilon$

The third criterion directly measures violation of the LCP conditions and is the most reliable, though slightly more expensive to evaluate.

### Initial Guess

A good initial guess accelerates convergence:

- **First time step**: Use the payoff $\boldsymbol{\Phi}$ as the initial guess.
- **Subsequent time steps**: Use the solution from the previous time step $\mathbf{u}^n$.
- **Continuation value**: Use the unconstrained solution $(I + \Delta\tau A)^{-1}\mathbf{q}$ (one tridiagonal solve) as the initial guess, then project.

### Computational Cost

Each PSOR iteration costs $O(m)$ operations (one sweep through the grid). With $K_{\text{iter}}$ iterations per time step and $N$ time steps:

$$
\text{Total cost} = O(m \cdot K_{\text{iter}} \cdot N)
$$

For $m = 200$, $K_{\text{iter}} = 10$, $N = 100$: approximately $200{,}000$ floating-point operations --- very efficient.

---

## Pseudocode

```
function PSOR_LCP(L, q, Phi, omega, tol, max_iter)
    u = Phi  // initial guess
    for k = 1, 2, ..., max_iter:
        u_old = u.copy()
        for j = 1, 2, ..., m:
            sigma = sum(L[j,i] * u[i] for i < j)
                  + sum(L[j,i] * u_old[i] for i > j)
            u_tilde = (1 - omega) * u_old[j]
                    + omega * (q[j] - sigma) / L[j,j]
            u[j] = max(u_tilde, Phi[j])
        end for
        if max|u - u_old| < tol:
            return u
    end for
    warn("PSOR did not converge")
    return u
end function
```

---

## Worked Example

Consider the LCP from a single implicit Euler step for an American put with $K = 100$ on a coarse 3-point interior grid ($S_1 = 40$, $S_2 = 80$, $S_3 = 120$).

**Given:**

$$
L = \begin{pmatrix} 1.08 & -0.03 & 0 \\ -0.05 & 1.12 & -0.06 \\ 0 & -0.07 & 1.15 \end{pmatrix}, \quad \mathbf{q} = \begin{pmatrix} 58.0 \\ 18.0 \\ 2.0 \end{pmatrix}, \quad \boldsymbol{\Phi} = \begin{pmatrix} 60 \\ 20 \\ 0 \end{pmatrix}
$$

**Iteration with $\omega = 1.2$:**

Starting from $\mathbf{u}^{(0)} = \boldsymbol{\Phi} = (60, 20, 0)^T$:

**Iteration 1:** For $j = 1$:

$$
\tilde{u}_1 = (1 - 1.2)(60) + \frac{1.2}{1.08}(58.0 - (-0.03)(20) - 0) = -12 + \frac{1.2 \times 58.6}{1.08} = -12 + 65.11 = 53.11
$$

Since $53.11 < 60 = \Phi_1$, we project: $u_1^{(1)} = 60$.

For $j = 2$:

$$
\tilde{u}_2 = (1 - 1.2)(20) + \frac{1.2}{1.12}(18.0 - (-0.05)(60) - (-0.06)(0)) = -4 + \frac{1.2 \times 21.0}{1.12} = -4 + 22.50 = 18.50
$$

Since $18.50 < 20 = \Phi_2$, we project: $u_2^{(1)} = 20$.

For $j = 3$:

$$
\tilde{u}_3 = (1 - 1.2)(0) + \frac{1.2}{1.15}(2.0 - (-0.07)(20)) = \frac{1.2 \times 3.4}{1.15} = 3.55
$$

Since $3.55 > 0 = \Phi_3$: $u_3^{(1)} = 3.55$.

After iteration 1: $\mathbf{u}^{(1)} = (60, 20, 3.55)^T$.

The algorithm continues, and after a few more iterations the solution stabilizes with $u_1 = 60$ (exercise), $u_2 = 20$ (exercise), and $u_3 \approx 3.6$ (continuation). The free boundary lies between $S_2 = 80$ and $S_3 = 120$.

---

## Comparison with Other LCP Solvers

| Method | Cost per step | Convergence | Ease of implementation |
|:---|:---|:---|:---|
| **PSOR** | $O(m \cdot K_{\text{iter}})$ | Linear, parameter-dependent | Moderate |
| **Projected Gauss-Seidel** | $O(m \cdot K_{\text{iter}})$ | Linear, slower | Easy ($\omega = 1$) |
| **Penalty method** | $O(m)$ per Newton step | Quadratic (Newton), approx. error $O(1/\rho)$ | Easy |
| **Active set** | $O(m)$ per solve | Finite termination | Moderate |
| **Multigrid** | $O(m)$ total | Optimal | Complex |

PSOR remains popular due to its simplicity, reliability, and good performance for the moderate-sized systems typical in one-dimensional option pricing. For higher-dimensional problems or very large grids, multigrid or penalty methods may be preferable.

---

## Practical Considerations

### Handling the Boundary Conditions

The PSOR iteration applies to interior grid points. Boundary conditions (e.g., $V(0, t) = K e^{-r\tau}$ for a put, $V(S_{\max}, t) = 0$) are incorporated into the right-hand side vector $\mathbf{q}$ before iteration begins.

### Monitoring the Active Set

Tracking which grid points are in the active set $\mathcal{A} = \{j : u_j = \Phi_j\}$ provides useful diagnostics:

- The active set should be a connected interval (for standard American puts).
- If the active set "flickers" between iterations, the relaxation parameter may need adjustment.
- The active set at convergence directly gives the discrete exercise boundary.

### Extension to Crank-Nicolson

When using Crank-Nicolson time stepping, the LCP becomes:

$$
\left(I + \tfrac{\Delta\tau}{2}A\right)\mathbf{u}^{n+1} \geq \left(I - \tfrac{\Delta\tau}{2}A\right)\mathbf{u}^n, \quad \mathbf{u}^{n+1} \geq \boldsymbol{\Phi}
$$

The PSOR algorithm applies with $L = I + \frac{\Delta\tau}{2}A$ and $\mathbf{q} = (I - \frac{\Delta\tau}{2}A)\mathbf{u}^n$. The M-matrix property of $L$ is preserved, ensuring convergence.

---

## Summary

| Aspect | Detail |
|:---|:---|
| Core idea | SOR iteration with projection onto $\mathbf{u} \geq \boldsymbol{\Phi}$ |
| Convergence | Guaranteed for M-matrix $L$ and $\omega \in (0, 2)$ |
| Optimal $\omega$ | Typically $1.2$-$1.5$ for American options; reduces iterations significantly |
| Cost | $O(m \cdot K_{\text{iter}})$ per time step; $K_{\text{iter}} \approx 5$-$20$ |
| Free boundary | Determined by the active set at convergence |
| Strengths | Simple, reliable, well-understood convergence theory |
| Limitation | Linear convergence; not optimal for very large systems |
