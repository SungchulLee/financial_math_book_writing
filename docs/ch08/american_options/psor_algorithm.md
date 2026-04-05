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

---

## Exercises

**Exercise 1.** For the SOR iteration with $\omega = 1$ (Gauss-Seidel), write out one full sweep of the PSOR algorithm for the worked example with $L$, $\mathbf{q}$, and $\boldsymbol{\Phi}$ as given. Start from $\mathbf{u}^{(0)} = \boldsymbol{\Phi}$ and compute $\mathbf{u}^{(1)}$.

??? success "Solution to Exercise 1"
    With $\omega = 1$ (Gauss-Seidel), the PSOR update becomes:

    $$
    \tilde{u}_j^{(1)} = \frac{1}{l_{jj}}\left(q_j - \sum_{i < j} l_{ji}\,u_i^{(1)} - \sum_{i > j} l_{ji}\,u_i^{(0)}\right)
    $$

    Starting from $\mathbf{u}^{(0)} = \boldsymbol{\Phi} = (60, 20, 0)^T$ with the given $L$, $\mathbf{q}$:

    **For $j = 1$:**

    $$
    \tilde{u}_1^{(1)} = \frac{1}{1.08}\left(58.0 - (-0.03)(20) - 0\right) = \frac{58.0 + 0.6}{1.08} = \frac{58.6}{1.08} \approx 54.26
    $$

    Since $54.26 < 60 = \Phi_1$, project: $u_1^{(1)} = 60$.

    **For $j = 2$:**

    $$
    \tilde{u}_2^{(1)} = \frac{1}{1.12}\left(18.0 - (-0.05)(60) - (-0.06)(0)\right) = \frac{18.0 + 3.0}{1.12} = \frac{21.0}{1.12} \approx 18.75
    $$

    Since $18.75 < 20 = \Phi_2$, project: $u_2^{(1)} = 20$.

    **For $j = 3$:**

    $$
    \tilde{u}_3^{(1)} = \frac{1}{1.15}\left(2.0 - (-0.07)(20)\right) = \frac{2.0 + 1.4}{1.15} = \frac{3.4}{1.15} \approx 2.96
    $$

    Since $2.96 > 0 = \Phi_3$, no projection needed: $u_3^{(1)} = 2.96$.

    After one Gauss-Seidel sweep: $\mathbf{u}^{(1)} = (60, 20, 2.96)^T$.

    Note: Compared with the $\omega = 1.2$ case in the text (which gave $u_3^{(1)} = 3.55$), the Gauss-Seidel result $u_3^{(1)} = 2.96$ is closer to the initial guess $u_3^{(0)} = 0$. The over-relaxation accelerates convergence by taking a larger step.

---

**Exercise 2.** The optimal relaxation parameter satisfies $\omega^* = 2/(1 + \sqrt{1 - \rho(G_1)^2})$. If the spectral radius of the Gauss-Seidel iteration matrix is $\rho(G_1) = 0.98$, compute $\omega^*$. How many iterations per time step would you expect with Gauss-Seidel versus optimal SOR?

??? success "Solution to Exercise 2"
    Given $\rho(G_1) = 0.98$, the optimal relaxation parameter is:

    $$
    \omega^* = \frac{2}{1 + \sqrt{1 - \rho(G_1)^2}} = \frac{2}{1 + \sqrt{1 - 0.98^2}} = \frac{2}{1 + \sqrt{1 - 0.9604}} = \frac{2}{1 + \sqrt{0.0396}}
    $$

    $$
    \sqrt{0.0396} \approx 0.199
    $$

    $$
    \omega^* = \frac{2}{1.199} \approx 1.668
    $$

    **Iteration count estimates:**

    For Gauss-Seidel ($\omega = 1$), the error after $k$ iterations decays as $\rho(G_1)^k = 0.98^k$. To reduce the error by a factor of $10^{-6}$:

    $$
    0.98^k = 10^{-6} \implies k = \frac{-6\ln 10}{\ln 0.98} \approx \frac{-13.82}{-0.0202} \approx 684 \text{ iterations}
    $$

    For optimal SOR ($\omega = \omega^*$), the spectral radius is $\rho(G_{\omega^*}) = \omega^* - 1 \approx 0.668$. The same reduction requires:

    $$
    0.668^k = 10^{-6} \implies k = \frac{-6\ln 10}{\ln 0.668} \approx \frac{-13.82}{-0.404} \approx 34 \text{ iterations}
    $$

    Optimal SOR requires roughly 34 iterations compared to 684 for Gauss-Seidel --- a factor of 20 speedup. For the more typical tolerance requirements in option pricing (reduce error by $10^{-3}$), the counts would be approximately 342 for Gauss-Seidel and 17 for optimal SOR.

---

**Exercise 3.** Explain why the projection step $u_j^{(k+1)} = \max(\tilde{u}_j^{(k+1)}, \Phi_j)$ ensures the complementarity condition at convergence. Specifically, show that at a converged solution, each grid point satisfies either $u_j = \Phi_j$ (exercise) or $(L\mathbf{u})_j = q_j$ (PDE satisfied), but not both with strict inequality simultaneously.

??? success "Solution to Exercise 3"
    At convergence, $\mathbf{u}^{(k+1)} = \mathbf{u}^{(k)} = \mathbf{u}^*$. The PSOR iteration gives for each $j$:

    $$
    \tilde{u}_j^* = (1 - \omega)u_j^* + \frac{\omega}{l_{jj}}\left(q_j - \sum_{i \neq j} l_{ji}u_i^*\right) = u_j^* + \frac{\omega}{l_{jj}}\left(q_j - (L\mathbf{u}^*)_j\right)
    $$

    Define the residual $r_j = q_j - (L\mathbf{u}^*)_j$. Then $\tilde{u}_j^* = u_j^* + \frac{\omega}{l_{jj}} r_j$.

    The projection gives $u_j^* = \max(\tilde{u}_j^*, \Phi_j)$, so at convergence:

    $$
    u_j^* = \max\!\left(u_j^* + \frac{\omega}{l_{jj}} r_j,\; \Phi_j\right)
    $$

    **Case 1: $u_j^* > \Phi_j$ (continuation).** Since $u_j^*$ is strictly above $\Phi_j$, for the max to return $u_j^*$ we need $u_j^* + \frac{\omega}{l_{jj}} r_j = u_j^*$, which gives $r_j = 0$, i.e., $(L\mathbf{u}^*)_j = q_j$. The PDE is satisfied exactly.

    **Case 2: $u_j^* = \Phi_j$ (exercise).** The max condition gives $\Phi_j = \max(\Phi_j + \frac{\omega}{l_{jj}} r_j, \Phi_j)$, which requires $\frac{\omega}{l_{jj}} r_j \leq 0$. Since $\omega > 0$ and $l_{jj} > 0$, this means $r_j \leq 0$, i.e., $(L\mathbf{u}^*)_j \geq q_j$. The PDE residual is non-negative.

    **Complementarity:** In Case 1, $(L\mathbf{u}^* - \mathbf{q})_j = 0$ and $u_j^* - \Phi_j > 0$, so the product is $0$. In Case 2, $u_j^* - \Phi_j = 0$, so the product is $0$ regardless. Thus $(L\mathbf{u}^* - \mathbf{q})_j (u_j^* - \Phi_j) = 0$ for all $j$.

    The two cases are mutually exclusive: if $u_j^* > \Phi_j$ then $(L\mathbf{u}^*)_j = q_j$ exactly; if $u_j^* = \Phi_j$ then $(L\mathbf{u}^*)_j \geq q_j$. Both inequalities cannot be strict simultaneously, which is the complementarity condition.

---

**Exercise 4.** The stopping criterion $\|\mathbf{u}^{(k+1)} - \mathbf{u}^{(k)}\|_\infty < \varepsilon$ measures the change between iterations. An alternative is the LCP residual $\max_j \min((L\mathbf{u} - \mathbf{q})_j, u_j - \Phi_j)$. Explain why the residual criterion is more reliable and give an example where the change criterion might stop too early.

??? success "Solution to Exercise 4"
    **Why the residual criterion is more reliable:**

    The change criterion $\|\mathbf{u}^{(k+1)} - \mathbf{u}^{(k)}\|_\infty < \varepsilon$ measures how much the iterate moves, but a small change does not guarantee the LCP conditions are satisfied. The LCP residual directly measures violation of the complementarity conditions.

    The residual criterion checks:

    $$
    \max_j \min\!\left((L\mathbf{u} - \mathbf{q})_j,\; u_j - \Phi_j\right) < \varepsilon
    $$

    This is zero if and only if the LCP is satisfied: for each $j$, at least one of the two quantities is non-positive (i.e., near zero or satisfying its inequality).

    **Example where the change criterion stops too early:**

    Suppose the relaxation parameter $\omega$ is poorly chosen (e.g., close to 2), causing the iterates to oscillate slowly. The differences $\|\mathbf{u}^{(k+1)} - \mathbf{u}^{(k)}\|$ might become small while the iterates are still far from the true solution --- the iteration is "stalling" rather than converging.

    Concretely, consider a grid point near the free boundary where $u_j^{(k)}$ alternates between $\Phi_j + \delta$ and $\Phi_j + \delta + \epsilon$ for small $\delta > 0$. The change $\epsilon$ may be below the tolerance, but the residual $(L\mathbf{u} - \mathbf{q})_j$ could still be of order $\delta$, which is much larger. The change criterion would declare convergence prematurely, while the residual criterion would correctly identify that the solution is not yet accurate.

    Another scenario: if the initial guess is close to the solution in the continuation region but incorrectly classifies a point near the boundary, the change criterion may be satisfied after one iteration (small change), but the LCP residual at the misclassified point would be large.

---

**Exercise 5.** For the Crank-Nicolson variant of PSOR, the matrix becomes $L = I + \frac{\Delta\tau}{2}A$ and $\mathbf{q} = (I - \frac{\Delta\tau}{2}A)\mathbf{u}^n$. Verify that $L$ is still an M-matrix, ensuring PSOR convergence. What care must be taken with the right-hand side computation?

??? success "Solution to Exercise 5"
    For the Crank-Nicolson variant, $L = I + \frac{\Delta\tau}{2}A$ and $\mathbf{q} = (I - \frac{\Delta\tau}{2}A)\mathbf{u}^n$.

    **M-matrix verification for $L = I + \frac{\Delta\tau}{2}A$:**

    The matrix $A$ arising from the Black-Scholes discretization has:

    - Positive diagonal entries $a_{jj} > 0$
    - Non-positive off-diagonal entries $a_{jk} \leq 0$ for $j \neq k$ (on a sufficiently fine grid)

    For $L = I + \frac{\Delta\tau}{2}A$:

    - **Positive diagonal:** $L_{jj} = 1 + \frac{\Delta\tau}{2}a_{jj} > 1 > 0$ since $a_{jj} > 0$.
    - **Non-positive off-diagonal:** $L_{jk} = \frac{\Delta\tau}{2}a_{jk} \leq 0$ for $j \neq k$.
    - **Diagonal dominance:** The row sum is $L_{jj} + \sum_{k \neq j} L_{jk} = 1 + \frac{\Delta\tau}{2}(a_{jj} + \sum_{k \neq j} a_{jk}) = 1 + \frac{\Delta\tau}{2}r > 0$

    (where $r$ is the risk-free rate, since the row sums of $A$ equal $r$ for the Black-Scholes discretization). Therefore $L$ is strictly diagonally dominant with positive diagonal and non-positive off-diagonal, so $L$ is an M-matrix. PSOR convergence is guaranteed for $\omega \in (0, 2)$.

    **Care with the right-hand side:**

    The matrix $I - \frac{\Delta\tau}{2}A$ appearing in $\mathbf{q}$ is *not* an M-matrix (it has positive off-diagonal entries). This means $\mathbf{q}$ can have components that are larger or smaller than $\mathbf{u}^n$ depending on the local solution curvature. Near the free boundary, this can produce $q_j$ values that cause the unconstrained solution to dip below the payoff, requiring the projection step.

    Additionally, on coarse grids or with large $\Delta\tau$, the matrix $I - \frac{\Delta\tau}{2}A$ may not be non-negative, leading to spurious oscillations in $\mathbf{q}$ near the strike. Rannacher time-stepping (using a few implicit Euler steps at the start) mitigates this by ensuring smooth initial data before switching to Crank-Nicolson.

---

**Exercise 6.** Compare the computational cost of PSOR with $K_{\text{iter}} = 10$ iterations per time step against a single tridiagonal solve (as in the penalty method). For $m = 200$ interior points and $N = 100$ time steps, compute the total operation count for each method. Under what conditions does the penalty method become more efficient?

??? success "Solution to Exercise 6"
    **PSOR cost:**

    Each PSOR sweep through $m$ grid points costs approximately $3m$ operations (one multiply-add for the lower sum, one for the upper sum, and the update/projection). With $K_{\text{iter}} = 10$ iterations per time step:

    $$
    \text{PSOR cost per time step} = 10 \times 3m = 30m
    $$

    $$
    \text{PSOR total cost} = 30m \times N = 30 \times 200 \times 100 = 600{,}000 \text{ operations}
    $$

    **Penalty method cost:**

    The penalty method uses Newton iteration, each requiring one tridiagonal solve. A tridiagonal solve on $m$ unknowns costs approximately $5m$ operations (Thomas algorithm: forward elimination and back substitution). With 3 Newton iterations per time step (a typical count):

    $$
    \text{Penalty cost per time step} = 3 \times 5m = 15m
    $$

    $$
    \text{Penalty total cost} = 15m \times N = 15 \times 200 \times 100 = 300{,}000 \text{ operations}
    $$

    **Comparison:** The penalty method is about 2x faster than PSOR for these parameters ($300{,}000$ vs $600{,}000$).

    **When does the penalty method become more efficient?**

    The penalty method is more efficient when $N_{\text{Newton}} \times 5m < K_{\text{iter}} \times 3m$, i.e., when $5N_{\text{Newton}} < 3K_{\text{iter}}$, or $K_{\text{iter}} > \frac{5}{3}N_{\text{Newton}}$.

    With $N_{\text{Newton}} = 3$: the penalty method is faster when $K_{\text{iter}} > 5$ PSOR iterations.

    Since PSOR typically needs 5-20 iterations, the penalty method is usually competitive or faster. The penalty method becomes especially advantageous when:

    - The grid is fine (large $m$), causing PSOR to need more iterations.
    - The relaxation parameter $\omega$ is not well-tuned, increasing $K_{\text{iter}}$.
    - Higher dimensions are used, where PSOR is less natural but the penalty term adds negligible cost to existing PDE solvers.
