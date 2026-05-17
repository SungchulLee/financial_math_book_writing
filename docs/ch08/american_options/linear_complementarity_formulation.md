# Linear Complementarity Formulation

At every grid node, exactly one of two things is true: either the option is held ($V>\Phi$ and the Black-Scholes operator vanishes), or the option is exercised ($V=\Phi$ and the operator is non-negative). Their *product* therefore vanishes everywhere -- the algebraic fingerprint of complementarity. After discretization this becomes a **linear complementarity problem (LCP)**: a tridiagonal matrix system plus the constraint that each $V_i-\Phi_i$ and each residual entry have opposite signs and zero product. This LCP structure is what PSOR, penalty methods, and projection all aim to solve.

---

## From Variational Inequality to Complementarity

Recall (see [§ American Options](../../ch07/american_options/american_option_definition.md)): the American price satisfies the variational inequality

$$
\min\!\left(-\partial_t V - \mathcal{L}V + rV,\; V - \Phi\right) = 0,\qquad \mathcal{L}V = \tfrac12\sigma^2 S^2 V_{SS} + rSV_S,
$$

equivalent to the three-line **complementarity form** $(-\partial_t V-\mathcal{L}V+rV)\ge0$, $V-\Phi\ge0$, with product zero. This is a parabolic obstacle problem with obstacle $\Phi$.

---

## Finite Difference Discretization

### Setting Up the Grid

Consider a uniform grid in the transformed variables. After applying an implicit (backward Euler) or Crank-Nicolson discretization to the Black-Scholes PDE on the spatial grid $\{S_0, S_1, \ldots, S_M\}$ with time steps $\{t^0, t^1, \ldots, t^N\}$, each time step requires solving a system involving a tridiagonal matrix.

Let $\mathbf{u}^n = (u_1^n, \ldots, u_{M-1}^n)^T$ denote the vector of option values at interior grid points at time level $n$. The implicit Euler discretization yields:

$$
(I + \Delta\tau\, A)\,\mathbf{u}^{n+1} = \mathbf{u}^n
$$

where $\tau = T - t$ is time-to-maturity (so we march forward in $\tau$), $\Delta\tau$ is the time step, and $A$ is the tridiagonal matrix arising from the spatial discretization of $-\mathcal{L} + rI$.

### The Discrete LCP

Imposing the early exercise constraint $\mathbf{u}^{n+1} \geq \boldsymbol{\Phi}$ at each time step transforms the linear system into a **linear complementarity problem**.

!!! abstract "Definition: Discrete LCP"
    Given a matrix $L \in \mathbb{R}^{m \times m}$, and vectors $\mathbf{q}, \boldsymbol{\Phi} \in \mathbb{R}^m$, the **linear complementarity problem** $\mathrm{LCP}(L, \mathbf{q}, \boldsymbol{\Phi})$ is: find $\mathbf{u} \in \mathbb{R}^m$ such that

    $$
    \begin{aligned}
    L\mathbf{u} - \mathbf{q} &\geq \mathbf{0} \\[4pt]
    \mathbf{u} - \boldsymbol{\Phi} &\geq \mathbf{0} \\[4pt]
    (L\mathbf{u} - \mathbf{q})^T(\mathbf{u} - \boldsymbol{\Phi}) &= 0
    \end{aligned}
    $$

For the American option, the identification is:

| LCP quantity | American option meaning |
|:---|:---|
| $L$ | $I + \Delta\tau\, A$ (discrete time-stepping operator) |
| $\mathbf{q}$ | $\mathbf{u}^n$ (solution at previous time level) |
| $\boldsymbol{\Phi}$ | Payoff vector $(\Phi(S_1), \ldots, \Phi(S_{M-1}))^T$ |
| $\mathbf{u}$ | $\mathbf{u}^{n+1}$ (solution at current time level) |

### Componentwise Interpretation

The complementarity condition $(L\mathbf{u} - \mathbf{q})^T(\mathbf{u} - \boldsymbol{\Phi}) = 0$ is equivalent to requiring, for each grid point $j$:

$$
(L\mathbf{u} - \mathbf{q})_j \geq 0, \quad u_j \geq \Phi_j, \quad (L\mathbf{u} - \mathbf{q})_j(u_j - \Phi_j) = 0
$$

This means at each grid point, exactly one of the following holds:

- $u_j > \Phi_j$ and $(L\mathbf{u})_j = q_j$ --- the option is in the **continuation region** and the discrete PDE is satisfied.
- $u_j = \Phi_j$ and $(L\mathbf{u})_j \geq q_j$ --- the option is in the **exercise region** and the constraint binds.

---

## Existence and Uniqueness

The theory of LCPs guarantees existence and uniqueness under a condition on the matrix $L$.

!!! abstract "Definition: M-matrix"
    A matrix $L \in \mathbb{R}^{m \times m}$ is an **M-matrix** if:

    1. $l_{jj} > 0$ for all $j$ (positive diagonal),
    2. $l_{jk} \leq 0$ for all $j \neq k$ (non-positive off-diagonal),
    3. $L$ is non-singular with $L^{-1} \geq 0$ (inverse has non-negative entries).

**Theorem (Existence and Uniqueness for LCP).** *If $L$ is an M-matrix, then $\mathrm{LCP}(L, \mathbf{q}, \boldsymbol{\Phi})$ has a unique solution for any $\mathbf{q}$ and $\boldsymbol{\Phi}$.*

??? note "Proof Sketch"
    The proof proceeds by showing the LCP is equivalent to a monotone variational inequality on the convex set $\mathcal{K} = \{\mathbf{u} : \mathbf{u} \geq \boldsymbol{\Phi}\}$. Since $L$ is an M-matrix, it is positive definite on $\mathcal{K}$ (the symmetric part $\frac{1}{2}(L + L^T)$ is positive definite). By the Stampacchia theorem, the variational inequality

    $$
    \langle L\mathbf{u} - \mathbf{q},\, \mathbf{v} - \mathbf{u}\rangle \geq 0 \quad \text{for all } \mathbf{v} \in \mathcal{K}
    $$

    has a unique solution in $\mathcal{K}$. The equivalence between this variational inequality and the LCP follows from the characterization of the normal cone to $\mathcal{K}$ at $\mathbf{u}$. $\square$

### Verification for American Options

For implicit Euler, $L = I + \Delta\tau\, A$ inherits positive diagonal, non-positive off-diagonals and diagonal dominance from $A$ (recall [§ FDM stencils](../fdm/boundary_and_terminal_conditions.md) and [§ Monotone schemes](../monotone/barles_souganidis_theorem.md)), so $L$ is an M-matrix. Crank-Nicolson uses $L=I+\tfrac{\Delta\tau}{2}A$ — still an M-matrix, but the RHS may introduce kinks; Rannacher start-up (see [§ Implementation](../implementation/crank_nicolson_implementation.md)) restores smoothness.

---

## The Free Boundary as a Complementarity Constraint

### Locating the Free Boundary

The LCP solution implicitly determines the **exercise boundary**. Define the **active set** (exercise region) and **inactive set** (continuation region):

$$
\mathcal{A}^{n+1} = \{j : u_j^{n+1} = \Phi_j\}, \qquad \mathcal{I}^{n+1} = \{j : u_j^{n+1} > \Phi_j\}
$$

The free boundary at time level $n+1$ lies between the rightmost point in $\mathcal{A}^{n+1}$ and the leftmost point in $\mathcal{I}^{n+1}$ (for an American put).

### Smooth Pasting from the LCP Perspective

The smooth pasting condition --- continuity of $V_S$ across the free boundary --- is not explicitly imposed in the LCP formulation. Instead, it emerges as a **consequence** of the regularity of the solution. The LCP enforces both the constraint and the PDE, and the smooth pasting follows from the fact that the solution to the obstacle problem has $C^1$ regularity across the free boundary (a classical result in the theory of variational inequalities).

---

## Connection to Optimization

### Quadratic Programming Formulation

The LCP can be reformulated as a **quadratic program**. If $L$ is symmetric positive definite (or can be symmetrized), the LCP is equivalent to:

$$
\min_{\mathbf{u} \geq \boldsymbol{\Phi}} \;\frac{1}{2}\mathbf{u}^T L\,\mathbf{u} - \mathbf{q}^T\mathbf{u}
$$

The KKT conditions of this quadratic program are precisely the LCP conditions. This connection is useful because:

1. It guarantees the LCP has a unique minimizer (convex objective over a convex set).
2. It motivates iterative solvers (projected gradient methods, active set methods).
3. It connects American option pricing to the broader theory of constrained optimization.

### Active Set Method

An alternative to iterative solvers is the **active set method**:

1. Guess the active set $\mathcal{A}$ (indices where $u_j = \Phi_j$).
2. Solve the reduced linear system on the inactive set $\mathcal{I}$.
3. Check the complementarity conditions; update $\mathcal{A}$ if violated.
4. Repeat until convergence.

This method converges in finitely many steps (since there are finitely many possible active sets) and is often efficient when the active set changes by only a few indices between time steps.

---

## Worked Example: American Put LCP

Consider an American put option with strike $K = 100$, risk-free rate $r = 0.05$, volatility $\sigma = 0.20$, and maturity $T = 1$. We discretize with $M = 4$ interior grid points on $[0, S_{\max}]$ with $S_{\max} = 200$.

The grid points are $S_j = j \cdot 50$ for $j = 0, 1, 2, 3, 4, 5$ (including boundaries), so the interior points are $S_1 = 50$, $S_2 = 100$, $S_3 = 150$, $S_4 = 200$ --- but we use $j = 1, \ldots, 4$ as interior. The payoff vector is:

$$
\boldsymbol{\Phi} = \begin{pmatrix} \max(100 - 50, 0) \\ \max(100 - 100, 0) \\ \max(100 - 150, 0) \\ \max(100 - 200, 0) \end{pmatrix} = \begin{pmatrix} 50 \\ 0 \\ 0 \\ 0 \end{pmatrix}
$$

Suppose after one implicit Euler step, the unconstrained solution is $\tilde{\mathbf{u}} = (45, 8, 1, 0)^T$. Since $\tilde{u}_1 = 45 < 50 = \Phi_1$, the constraint is violated at $j = 1$. The LCP solution sets:

- $u_1 = \Phi_1 = 50$ (exercise region: constraint active)
- $u_2 = 8$, $u_3 = 1$, $u_4 = 0$ (continuation region: PDE satisfied)

The free boundary lies between $S_1 = 50$ and $S_2 = 100$, consistent with the early exercise boundary for a put being below the strike.

!!! tip "Verification"
    To verify the LCP solution, check:

    1. $\mathbf{u} \geq \boldsymbol{\Phi}$ componentwise. Here $50 \geq 50$, $8 \geq 0$, $1 \geq 0$, $0 \geq 0$. Satisfied.
    2. $L\mathbf{u} - \mathbf{q} \geq \mathbf{0}$ componentwise. This must be verified with the actual matrix $L$.
    3. $(L\mathbf{u} - \mathbf{q})_j(u_j - \Phi_j) = 0$ for each $j$. At $j = 1$: $u_1 - \Phi_1 = 0$, so the product is zero regardless of the residual. At $j = 2, 3, 4$: the PDE residual $(L\mathbf{u} - \mathbf{q})_j = 0$.

---

## Comparison with Direct Projection

The simplest approach to enforcing the early exercise constraint is the **projection method**: solve the unconstrained linear system and then set $u_j \leftarrow \max(u_j, \Phi_j)$. While intuitive, this approach has a subtle deficiency.

| Aspect | LCP formulation | Direct projection |
|:---|:---|:---|
| Constraint enforcement | Simultaneous with PDE solve | Sequential (solve then project) |
| Accuracy near boundary | Higher (coupled system) | Lower (splitting error) |
| Time convergence order | Preserves scheme order | Can reduce to first-order |
| Smooth pasting | Naturally recovered | Not guaranteed |
| Implementation | Requires LCP solver (PSOR, active set) | Trivial |

The LCP formulation is the mathematically rigorous approach. The projection method can be viewed as a single iteration of a splitting scheme for the LCP and converges to the same solution in the limit of grid refinement, but with potentially lower accuracy on coarse grids.

---

## Summary

The linear complementarity formulation provides the natural mathematical framework for American option pricing on finite difference grids.

| Concept | Key point |
|:---|:---|
| Continuous LCP | Variational inequality: PDE in continuation, constraint in exercise |
| Discrete LCP | $L\mathbf{u} \geq \mathbf{q}$, $\mathbf{u} \geq \boldsymbol{\Phi}$, complementarity |
| Existence/uniqueness | Guaranteed when $L$ is an M-matrix |
| Free boundary | Determined implicitly by the active set |
| Smooth pasting | Consequence of $C^1$ regularity, not imposed |
| Solvers | PSOR, penalty method, active set (covered in subsequent sections) |

---

## Exercises

**Exercise 1.** Write the American put variational inequality in complementarity form. At a point $(t, S)$ with $S = 80$, $K = 100$, explain which of the two conditions (PDE equality or constraint binding) holds, and why.

??? success "Solution to Exercise 1"
    The American put variational inequality in complementarity form is:

    $$
    -\frac{\partial V}{\partial t} - \mathcal{L}V + rV \geq 0
    $$

    $$
    V - \Phi \geq 0
    $$

    $$
    \left(-\frac{\partial V}{\partial t} - \mathcal{L}V + rV\right)(V - \Phi) = 0
    $$

    where $\mathcal{L}V = \frac{1}{2}\sigma^2 S^2 V_{SS} + rS V_S$ and $\Phi(S) = (K - S)^+$.

    **At $S = 80$ with $K = 100$:**

    Since $S = 80 < K = 100$, the put is in the money with intrinsic value $\Phi(80) = 100 - 80 = 20$. Whether the constraint binds or the PDE holds depends on whether $S = 80$ is in the exercise or continuation region, i.e., whether $S = 80$ is below or above the exercise boundary $S^*(t)$.

    For typical parameters ($r = 0.05$, $\sigma = 0.20$, $T = 1$), the exercise boundary at intermediate times satisfies $S^*(t) \approx 75$-$85$. Since $S = 80$ is close to the boundary:

    - **If $S = 80 > S^*(t)$ (continuation region):** The PDE holds with equality, $-V_t - \mathcal{L}V + rV = 0$, and $V(t, 80) > 20 = \Phi(80)$. The option is worth more alive than exercised.

    - **If $S = 80 \leq S^*(t)$ (exercise region):** The constraint binds, $V(t, 80) = \Phi(80) = 20$, and the PDE residual is non-negative: $-V_t - \mathcal{L}V + rV \geq 0$. Immediate exercise is optimal because the interest earned on $K = 100$ exceeds the expected gain from holding.

    For a moderately deep in-the-money put with these parameters, $S = 80$ is likely near or inside the exercise region, so the constraint binding condition $V = \Phi = 20$ is the more likely scenario.

---

**Exercise 2.** For the discrete LCP with $L = I + \Delta\tau A$, verify that $L$ is an M-matrix for the implicit Euler discretization of the Black-Scholes operator. Specifically, show that $L$ has positive diagonal, non-positive off-diagonal entries, and is diagonally dominant.

??? success "Solution to Exercise 2"
    For the implicit Euler discretization of the Black-Scholes operator, the spatial discretization of $-\mathcal{L} + rI$ on a uniform grid with spacing $\Delta S$ produces a tridiagonal matrix $A$ with entries at grid point $j$ (where $S_j = j\Delta S$):

    $$
    a_j = -\frac{1}{2}\sigma^2 S_j^2 \frac{1}{\Delta S^2} + \frac{1}{2}rS_j \frac{1}{\Delta S}
    $$

    $$
    b_j = \sigma^2 S_j^2 \frac{1}{\Delta S^2} + r
    $$

    $$
    c_j = -\frac{1}{2}\sigma^2 S_j^2 \frac{1}{\Delta S^2} - \frac{1}{2}rS_j \frac{1}{\Delta S}
    $$

    where $a_j$, $b_j$, $c_j$ are the lower diagonal, diagonal, and upper diagonal entries of $A$.

    The matrix $L = I + \Delta\tau A$ has entries:

    **Positive diagonal:** $L_{jj} = 1 + \Delta\tau\, b_j = 1 + \Delta\tau(\sigma^2 S_j^2/\Delta S^2 + r) > 0$ since all terms are positive.

    **Non-positive off-diagonal:** For the sub-diagonal:

    $$
    L_{j,j-1} = \Delta\tau\, a_j = \Delta\tau\left(-\frac{\sigma^2 S_j^2}{2\Delta S^2} + \frac{rS_j}{2\Delta S}\right)
    $$

    This is non-positive provided $\frac{\sigma^2 S_j^2}{2\Delta S^2} \geq \frac{rS_j}{2\Delta S}$, i.e., $\sigma^2 S_j \geq r\Delta S$, which holds on a sufficiently fine grid. Similarly for the super-diagonal $L_{j,j+1} = \Delta\tau\, c_j \leq 0$.

    **Diagonal dominance:** The row sum satisfies:

    $$
    L_{jj} + L_{j,j-1} + L_{j,j+1} = 1 + \Delta\tau\, r > 1 > 0
    $$

    Since $L_{jj} > 0$, $L_{j,j-1} \leq 0$, $L_{j,j+1} \leq 0$, and the row sum is positive, $L$ is strictly diagonally dominant with positive diagonal. Therefore $L$ is an M-matrix.

---

**Exercise 3.** Consider the worked example with $\boldsymbol{\Phi} = (50, 0, 0, 0)^T$ and unconstrained solution $\tilde{\mathbf{u}} = (45, 8, 1, 0)^T$. Verify that the LCP solution $\mathbf{u} = (50, 8, 1, 0)^T$ satisfies all three LCP conditions: $L\mathbf{u} \geq \mathbf{q}$, $\mathbf{u} \geq \boldsymbol{\Phi}$, and $(L\mathbf{u} - \mathbf{q})_j(u_j - \Phi_j) = 0$ for each $j$.

??? success "Solution to Exercise 3"
    We verify the three LCP conditions for $\mathbf{u} = (50, 8, 1, 0)^T$ with $\boldsymbol{\Phi} = (50, 0, 0, 0)^T$ and right-hand side $\mathbf{q} = \tilde{\mathbf{u}} = (45, 8, 1, 0)^T$ (the unconstrained solution satisfies $L\tilde{\mathbf{u}} = \mathbf{q}_{\text{original}}$).

    **Condition 2: $\mathbf{u} \geq \boldsymbol{\Phi}$**

    - $u_1 = 50 \geq 50 = \Phi_1$ (equality)
    - $u_2 = 8 \geq 0 = \Phi_2$ (strict)
    - $u_3 = 1 \geq 0 = \Phi_3$ (strict)
    - $u_4 = 0 \geq 0 = \Phi_4$ (equality)

    All satisfied.

    **Condition 1: $L\mathbf{u} - \mathbf{q} \geq \mathbf{0}$**

    At $j = 1$: Since $u_1 = 50 > 45 = \tilde{u}_1$, and $L$ has positive diagonal, replacing $\tilde{u}_1 = 45$ with $u_1 = 50$ increases $(L\mathbf{u})_1$ compared to $(L\tilde{\mathbf{u}})_1 = q_1$. The off-diagonal entries of $L$ are non-positive, and $u_j \geq \tilde{u}_j$ for all $j$ (since we only increased components via projection). Therefore $(L\mathbf{u})_1 \geq (L\tilde{\mathbf{u}})_1 = q_1$. The residual $(L\mathbf{u} - \mathbf{q})_1 \geq 0$.

    At $j = 2, 3, 4$: These components were not modified by projection ($u_j = \tilde{u}_j$), but $u_1$ was increased, which affects $(L\mathbf{u})_2$ through the off-diagonal term $l_{21}$. Since $l_{21} \leq 0$ and $u_1 > \tilde{u}_1$, we have $(L\mathbf{u})_2 \leq (L\tilde{\mathbf{u}})_2 = q_2$. This could potentially violate the first condition at $j = 2$.

    In general, the simple projection does not exactly solve the LCP --- the residual condition may be violated at points adjacent to the exercise boundary. The LCP would require re-solving the coupled system to ensure all three conditions hold simultaneously. The verification above shows that the projection gives an *approximate* but not exact LCP solution.

---

**Exercise 4.** The smooth pasting condition (continuity of $V_S$ across the free boundary) is not explicitly imposed in the LCP formulation. Explain why it emerges automatically from the $C^1$ regularity of the obstacle problem solution. What numerical evidence could you check to verify that smooth pasting holds in your FDM solution?

??? success "Solution to Exercise 4"
    **Why smooth pasting emerges from $C^1$ regularity:**

    The American option problem is an obstacle problem: $V$ is the smallest supersolution of the Black-Scholes PDE that lies above the obstacle $\Phi$. Classical regularity theory for parabolic obstacle problems (due to Friedman, Kinderlehrer-Stampacchia) establishes that the solution has $C^1$ regularity across the free boundary, i.e., both $V$ and $V_S$ are continuous everywhere.

    In the continuation region, $V$ satisfies the smooth PDE $V_t + \mathcal{L}V - rV = 0$, so $V$ is smooth ($C^\infty$). In the exercise region, $V = \Phi$, and for the put $\Phi(S) = K - S$, which is also smooth (linear). At the free boundary $S = S^*(t)$:

    - Value matching $V(t, S^*) = \Phi(S^*)$ holds by continuity of $V$.
    - Slope matching $V_S(t, S^*) = \Phi'(S^*)$ holds by $C^1$ regularity.

    If $V_S$ were discontinuous at $S^*$, then $V_{SS}$ would contain a Dirac delta at $S^*$, and the PDE $V_t + \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV = 0$ would not hold in a distributional sense. The $C^1$ regularity theorem rules this out.

    **Numerical evidence for smooth pasting:**

    To verify smooth pasting in an FDM solution:

    1. Compute the discrete derivative $V_S \approx (V_{j+1} - V_{j-1})/(2\Delta S)$ at grid points near the exercise boundary.
    2. Check that the derivative transitions smoothly from $-1$ (in the exercise region for a put) to a value greater than $-1$ (in the continuation region).
    3. Plot $V_S$ as a function of $S$ --- it should be continuous and smooth, with no visible kink at the estimated free boundary.
    4. Refine the grid and verify that the derivative profile converges, with the transition becoming sharper but remaining smooth.

---

**Exercise 5.** The LCP can be reformulated as a quadratic program: $\min_{\mathbf{u} \geq \boldsymbol{\Phi}} \frac{1}{2}\mathbf{u}^T L\mathbf{u} - \mathbf{q}^T\mathbf{u}$. Show that the KKT conditions of this optimization problem are equivalent to the LCP conditions. What is the role of the Lagrange multipliers?

??? success "Solution to Exercise 5"
    The LCP conditions are:

    $$
    L\mathbf{u} - \mathbf{q} \geq \mathbf{0}, \quad \mathbf{u} \geq \boldsymbol{\Phi}, \quad (L\mathbf{u} - \mathbf{q})^T(\mathbf{u} - \boldsymbol{\Phi}) = 0
    $$

    The quadratic program is:

    $$
    \min_{\mathbf{u} \geq \boldsymbol{\Phi}} \; \frac{1}{2}\mathbf{u}^T L\mathbf{u} - \mathbf{q}^T\mathbf{u}
    $$

    **KKT conditions:** Introduce Lagrange multipliers $\boldsymbol{\lambda} \geq \mathbf{0}$ for the constraint $\mathbf{u} \geq \boldsymbol{\Phi}$. The KKT conditions are:

    1. **Stationarity:** $L\mathbf{u} - \mathbf{q} - \boldsymbol{\lambda} = \mathbf{0}$, i.e., $\boldsymbol{\lambda} = L\mathbf{u} - \mathbf{q}$
    2. **Primal feasibility:** $\mathbf{u} \geq \boldsymbol{\Phi}$
    3. **Dual feasibility:** $\boldsymbol{\lambda} \geq \mathbf{0}$, i.e., $L\mathbf{u} - \mathbf{q} \geq \mathbf{0}$
    4. **Complementary slackness:** $\boldsymbol{\lambda}^T(\mathbf{u} - \boldsymbol{\Phi}) = 0$, i.e., $(L\mathbf{u} - \mathbf{q})^T(\mathbf{u} - \boldsymbol{\Phi}) = 0$

    Conditions 2, 3, and 4 are exactly the LCP conditions. Therefore the KKT conditions are equivalent to the LCP.

    **Role of the Lagrange multipliers:** $\lambda_j = (L\mathbf{u} - \mathbf{q})_j$ represents the **early exercise premium** at grid point $j$. In the continuation region ($u_j > \Phi_j$), complementary slackness forces $\lambda_j = 0$: there is no premium since the PDE holds with equality. In the exercise region ($u_j = \Phi_j$), $\lambda_j \geq 0$ measures the degree to which the PDE residual is positive --- it quantifies how much "extra value" the early exercise right provides at that point.

---

**Exercise 6.** Compare the LCP formulation with direct projection for a coarse grid ($M = 10$) and a fine grid ($M = 1000$). On the coarse grid, the two methods may give noticeably different results near the free boundary. Explain the source of this difference and why the LCP solution is more accurate.

??? success "Solution to Exercise 6"
    **Source of difference on coarse grids:**

    The projection method solves the unconstrained PDE system first, obtaining $\tilde{\mathbf{u}}$, and then projects: $u_j = \max(\tilde{u}_j, \Phi_j)$. The LCP solves the PDE and constraint simultaneously.

    On a coarse grid ($M = 10$), the grid spacing is large and the free boundary falls between two widely-spaced grid points. The key differences are:

    1. **Splitting error:** In the projection method, the PDE solve at grid point $j$ uses the unconstrained values at neighbors $j \pm 1$, even if those neighbors should be in the exercise region with $u = \Phi$. After projection, the value at $j \pm 1$ changes to $\Phi_{j\pm1}$, but this information is not propagated back. The LCP solver iterates until the PDE and constraint are mutually consistent.

    2. **Boundary smearing:** With only 10 grid points, the transition from exercise to continuation is spread over 1-2 grid cells. The projection introduces an $O(\Delta S)$ error in the boundary location, while the LCP determines the optimal boundary within the discrete system.

    3. **Conservation:** The LCP preserves the complementarity structure exactly, so the discrete option value satisfies a discrete maximum principle. Projection may violate this principle on coarse grids.

    **On a fine grid ($M = 1000$):** Both methods converge to the same solution. The splitting error from projection is $O(\Delta\tau)$, which becomes small as the grid is refined. The LCP and projection agree to high precision, and the free boundary is resolved within a single grid cell.

    **Why the LCP is more accurate:** The LCP treats the PDE and constraint as a coupled system, correctly accounting for the interaction between the two at every grid point. It does not suffer from the operator-splitting error of the projection method. On coarse grids, this coupling is essential for accurate pricing near the boundary.
