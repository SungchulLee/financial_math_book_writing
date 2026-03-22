# American Options via PSOR

European options under Heston have semi-analytical prices through Fourier inversion, but **American options** require numerical methods because the early exercise boundary depends on both the stock price $S$ and the variance $v$. The early exercise feature transforms the PDE into a **linear complementarity problem (LCP)**: the option value must satisfy the PDE inequality while remaining above the intrinsic value at every point. **Projected successive over-relaxation (PSOR)** solves this LCP efficiently by combining iterative linear system solving with a projection onto the exercise constraint, integrating naturally with the ADI framework for the two-dimensional Heston PDE.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Formulate the American option pricing problem as a linear complementarity problem in two dimensions
    2. Derive the PSOR algorithm from projected Gauss-Seidel iteration
    3. Integrate PSOR with ADI time stepping for the Heston PDE
    4. Select the relaxation parameter and convergence tolerance

!!! tip "Prerequisites"
    This section builds on the [2D PDE formulation](two_dimensional_pde_formulation.md), [ADI schemes](adi_schemes.md), and [boundary conditions](boundary_conditions_for_variance.md).

---

## The Early Exercise Problem

An American option with payoff $g(S)$ can be exercised at any time $t \leq T$. The holder's optimal strategy creates a **free boundary** $S^*(t, v)$ separating the exercise region (where $V = g(S)$) from the continuation region (where $V > g(S)$).

In the Heston model, the free boundary is a **surface** in $(t, S, v)$ space---not just a curve as in the one-dimensional Black-Scholes setting. For an American put with $g(S) = (K - S)^+$:

- When $v$ is **small**, volatility is low and the put is less likely to move further in-the-money, so early exercise is more attractive and $S^*(t, v)$ is **higher**
- When $v$ is **large**, high volatility increases the option's time value, delaying exercise and pushing $S^*(t, v)$ **lower**

---

## Linear Complementarity Formulation

The American option price $V(t, x, v)$ satisfies three conditions simultaneously:

**Condition 1** (Value above intrinsic):

$$
V(t, x, v) \geq g(e^x)
$$

**Condition 2** (PDE inequality):

$$
\frac{\partial V}{\partial t} + \mathcal{L}V - rV \leq 0
$$

**Condition 3** (Complementarity):

$$
\left(V - g(e^x)\right) \cdot \left(\frac{\partial V}{\partial t} + \mathcal{L}V - rV\right) = 0
$$

where $\mathcal{L} = \mathcal{L}_x + \mathcal{L}_v + \mathcal{L}_{xv}$ is the full spatial operator.

These three conditions state that at every point $(t, x, v)$:

- Either $V = g$ (exercise region) and the PDE inequality is strict
- Or $V > g$ (continuation region) and the PDE equality holds

After time discretization, the LCP at each time step becomes a **matrix** complementarity problem:

$$
\mathbf{V}^{n+1} \geq \mathbf{g}, \qquad A \mathbf{V}^{n+1} \geq \mathbf{b}, \qquad (\mathbf{V}^{n+1} - \mathbf{g})^T (A \mathbf{V}^{n+1} - \mathbf{b}) = 0
$$

where $A$ is the implicit time-stepping matrix and $\mathbf{b}$ depends on $\mathbf{V}^n$.

---

## The PSOR Algorithm

### From Gauss-Seidel to PSOR

The standard **Gauss-Seidel** iteration for solving $A\mathbf{V} = \mathbf{b}$ updates each component sequentially using the latest available values:

$$
V_k^{(\ell+1)} = \frac{1}{a_{kk}}\left(b_k - \sum_{j < k} a_{kj} V_j^{(\ell+1)} - \sum_{j > k} a_{kj} V_j^{(\ell)}\right)
$$

**Successive over-relaxation (SOR)** accelerates convergence by introducing a relaxation parameter $\omega \in (1, 2)$:

$$
\tilde{V}_k^{(\ell+1)} = (1 - \omega) V_k^{(\ell)} + \frac{\omega}{a_{kk}}\left(b_k - \sum_{j < k} a_{kj} V_j^{(\ell+1)} - \sum_{j > k} a_{kj} V_j^{(\ell)}\right)
$$

**Projected SOR (PSOR)** adds the exercise constraint by projecting onto the feasible set after each SOR update:

$$
V_k^{(\ell+1)} = \max\!\left(\tilde{V}_k^{(\ell+1)}, \, g_k\right)
$$

where $g_k = g(e^{x_k})$ is the intrinsic value at grid point $k$.

### Algorithm

For each time step, given $\mathbf{V}^n$ from the previous step:

1. **Form** the linear system $A\mathbf{V}^{n+1} = \mathbf{b}(\mathbf{V}^n)$
2. **Initialize** $\mathbf{V}^{(0)} = \mathbf{V}^n$ (warm start)
3. **Iterate** for $\ell = 0, 1, 2, \ldots$:
    - For $k = 1, 2, \ldots, N_x N_v$:
        - Compute $\tilde{V}_k^{(\ell+1)}$ using SOR
        - Project: $V_k^{(\ell+1)} = \max(\tilde{V}_k^{(\ell+1)}, g_k)$
4. **Stop** when $\|\mathbf{V}^{(\ell+1)} - \mathbf{V}^{(\ell)}\|_\infty < \epsilon$

!!! note "Convergence of PSOR"
    PSOR converges for any $\omega \in (0, 2)$ when the matrix $A$ is an M-matrix (diagonally dominant with non-positive off-diagonal entries), which is satisfied by standard finite difference discretizations on sufficiently fine grids. The convergence rate depends on $\omega$; the optimal choice is typically $\omega \in [1.2, 1.8]$.

---

## Integration with ADI

The PSOR algorithm can be combined with ADI time stepping in two ways:

### Approach 1: PSOR After Each ADI Step (Operator Splitting Approach)

The simplest approach applies the ADI scheme to advance the PDE solution one time step (ignoring the exercise constraint), then projects:

1. Compute $\hat{\mathbf{V}}^{n+1}$ using the ADI scheme (e.g., Hundsdorfer-Verwer)
2. Project: $V_{i,j}^{n+1} = \max(\hat{V}_{i,j}^{n+1}, g_{i,j})$ for all $(i, j)$

This is sometimes called the **penalty method** or **operator splitting** approach. It is simple but introduces a splitting error: the projection is applied only once per time step, not iteratively.

### Approach 2: PSOR Within Each ADI Sweep

A more accurate approach applies PSOR within each implicit directional sweep of the ADI scheme:

1. In the $x$-direction sweep, solve the tridiagonal system for each $v_j$ line using PSOR (project after each row update)
2. In the $v$-direction sweep, solve the tridiagonal system for each $x_i$ line using PSOR

This produces better results near the exercise boundary but requires more iterations per sweep.

### Practical Recommendation

Approach 1 (projection after each full ADI step) is the standard choice in practice. The splitting error is $\mathcal{O}(\Delta\tau)$, which is compatible with the ADI temporal accuracy. Approach 2 is used when higher accuracy near the free boundary is needed.

---

## Relaxation Parameter Selection

The convergence rate of PSOR depends on the relaxation parameter $\omega$:

| $\omega$ | Behavior |
|-----------|----------|
| $\omega = 1$ | Gauss-Seidel (no over-relaxation) |
| $1 < \omega < \omega^*$ | Under-relaxed, slow but stable |
| $\omega = \omega^*$ | Optimal, fastest convergence |
| $\omega^* < \omega < 2$ | Over-relaxed, may oscillate |
| $\omega \geq 2$ | Divergent |

For the Heston PDE discretization, the **optimal** $\omega^*$ depends on the spectral radius of the Jacobi iteration matrix, which changes with the grid size and the PDE coefficients. In practice:

- Start with $\omega = 1.5$ as a robust default
- For fine grids ($N_x > 200$), increase toward $\omega = 1.7$--$1.8$
- The sensitivity to $\omega$ is modest: any $\omega \in [1.2, 1.8]$ gives acceptable performance

The stopping tolerance $\epsilon$ should be set to $10^{-6}$ to $10^{-8}$ times the notional, ensuring the iteration error is well below the spatial discretization error.

---

## Early Exercise Boundary Extraction

After solving the American option on the grid, the early exercise boundary $S^*(t, v)$ can be extracted by scanning each time slice for the transition from the exercise region to the continuation region:

For each $v_j$ and time $t_n$, find the largest $x_i$ (for a put) such that:

$$
V_{i,j}^n = g(e^{x_i})
$$

The boundary in $S$-space is $S^*_j(t_n) = e^{x_i}$. This produces a surface $S^*(t, v)$ that shows how the exercise boundary varies with both time and variance.

---

## Worked Example

Consider an American put with:

| Parameter | Value |
|-----------|-------|
| $S_0$ | $\$100$ |
| $K$ | $\$100$ |
| $r$ | $0.05$ |
| $q$ | $0$ |
| $v_0$ | $0.04$ |
| $\kappa$ | $1.5$ |
| $\theta$ | $0.04$ |
| $\xi$ | $0.3$ |
| $\rho$ | $-0.7$ |
| $T$ | $1.0$ |

**Grid**: $N_x = 150$, $N_v = 75$, $N_t = 200$, $\omega = 1.5$, $\epsilon = 10^{-7}$.

??? example "American Put Pricing Results"
    | Method | Price | Early Exercise Premium |
    |--------|:-----:|:---------------------:|
    | European put (Fourier) | $\$5.52$ | --- |
    | American put (PSOR + HV ADI) | $\$5.94$ | $\$0.42$ |

    The early exercise premium of $\$0.42$ (approximately 7.6% of the European value) reflects the value of being able to exercise when the stock drops significantly.

    The exercise boundary at $v = v_0 = 0.04$: $S^*(0, 0.04) \approx \$82$ (exercise immediately if $S < \$82$ at $t=0$).

    At $v = 0.01$ (low vol): $S^*(0, 0.01) \approx \$88$ --- higher boundary because low vol reduces time value.

    At $v = 0.10$ (high vol): $S^*(0, 0.10) \approx \$72$ --- lower boundary because high vol increases time value.

    The PSOR iteration converges in 5--15 iterations per time step with $\omega = 1.5$.

---

## Summary

American options under the Heston model are priced by solving a two-dimensional linear complementarity problem that couples the Heston PDE with the early exercise constraint. The PSOR algorithm efficiently solves this LCP by combining SOR iteration with projection onto the intrinsic value bound. Integration with ADI schemes---either through post-step projection (operator splitting) or intra-sweep PSOR---produces accurate American option prices and the two-dimensional free boundary $S^*(t, v)$. The relaxation parameter $\omega \approx 1.5$ and tolerance $\epsilon \approx 10^{-7}$ are robust defaults. The resulting exercise boundary reveals how optimal exercise depends on both moneyness and the current variance level.
