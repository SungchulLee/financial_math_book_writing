# Linear Complementarity Formulation

The pricing of American options leads naturally to a **linear complementarity problem (LCP)**. The holder's right to exercise at any time imposes a constraint that the option value must lie above the payoff at all times. Combined with the Black-Scholes PDE in the continuation region, this produces a complementarity structure that is both elegant and computationally tractable.

---

## From Variational Inequality to Complementarity

### The Continuous Problem

Recall that the American option price $V(t,S)$ satisfies the **variational inequality**:

$$
\min\!\left(-\frac{\partial V}{\partial t} - \mathcal{L}V + rV,\; V - \Phi\right) = 0
$$

where $\mathcal{L}V = \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S$ is the Black-Scholes differential operator and $\Phi(S)$ is the payoff function. This can be equivalently written in **complementarity form**:

$$
\begin{aligned}
-\frac{\partial V}{\partial t} - \mathcal{L}V + rV &\geq 0 \\[4pt]
V - \Phi &\geq 0 \\[4pt]
\left(-\frac{\partial V}{\partial t} - \mathcal{L}V + rV\right)(V - \Phi) &= 0
\end{aligned}
$$

!!! info "Complementarity Interpretation"
    At every point $(t,S)$ in the domain, exactly one of two situations holds:

    - **Continuation**: $V > \Phi$ and the PDE $\frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0$ holds with equality.
    - **Exercise**: $V = \Phi$ and the PDE residual $-\frac{\partial V}{\partial t} - \mathcal{L}V + rV \geq 0$ (the option is "too cheap" to continue holding).

    The third condition enforces that at least one of the two inequalities is active --- they cannot both be strict simultaneously.

### Analogy with the Obstacle Problem

The American option problem is a **parabolic obstacle problem**. Define the "obstacle" as $\Phi(S)$. The solution $V$ must lie above the obstacle everywhere, and in regions where $V$ is strictly above $\Phi$, it satisfies the PDE. This is identical in structure to the classical obstacle problem in the theory of variational inequalities.

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

For the implicit Euler scheme, $L = I + \Delta\tau\, A$. Under standard discretization of the Black-Scholes operator with a sufficiently fine grid:

- The diagonal entries of $A$ are positive (from the $rI$ term and central differences).
- The off-diagonal entries of $A$ are non-positive (provided the mesh is fine enough to avoid oscillations).
- Adding the identity ensures $L$ has strictly positive diagonal and is diagonally dominant.

Therefore $L$ is an M-matrix, and the discrete LCP has a unique solution at each time step.

!!! warning "Crank-Nicolson Caveat"
    With the Crank-Nicolson scheme, the operator becomes $L = I + \frac{\Delta\tau}{2}A$, and the right-hand side involves $(I - \frac{\Delta\tau}{2}A)\mathbf{u}^n$. The M-matrix property still holds for $L$, but the right-hand side may introduce complications near the free boundary. Rannacher time-stepping (a few implicit Euler steps at the start) is commonly used to restore smoothness.

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
