# Barles-Souganidis Theorem

The Barles-Souganidis theorem is the fundamental convergence result for approximation schemes applied to viscosity solutions. It provides a complete, verifiable criterion: a scheme converges to the viscosity solution if and only if it is **monotone**, **stable**, and **consistent**, provided a comparison principle holds. This theorem is the nonlinear analog of the Lax equivalence theorem.

---

## Context and Motivation

### Beyond the Lax Equivalence Theorem

The Lax equivalence theorem states:

$$
\text{consistency} + \text{stability} \Longleftrightarrow \text{convergence}
$$

for **linear**, well-posed problems. However, option pricing problems are often **nonlinear** (American options, uncertain volatility) or involve **degenerate** PDEs (Black-Scholes at $S = 0$). For these problems, the Lax framework does not apply directly.

The Barles-Souganidis theorem adds a third condition --- **monotonicity** --- and extends convergence theory to the full class of degenerate elliptic PDEs:

$$
\boxed{
\text{monotonicity} + \text{stability} + \text{consistency} \Longrightarrow \text{convergence to viscosity solution}
}
$$

### Why Monotonicity Matters

Without monotonicity, a consistent and stable scheme can converge to the **wrong answer**. This is not merely a theoretical concern: high-order schemes that violate monotonicity (such as Crank-Nicolson near a payoff kink) can produce oscillations that persist under refinement, converging to a function that is not the viscosity solution.

---

## The Three Conditions

Consider a general approximation scheme $S_h$ indexed by a mesh parameter $h > 0$ (representing $\Delta S$, $\Delta\tau$, or both). The scheme is written abstractly as:

$$
S_h(\tau, x, u_h(\tau, x), u_h) = 0
$$

where $u_h(\tau, x)$ is the numerical solution at point $(\tau, x)$, and $u_h$ denotes the full numerical solution (at all grid points).

### Condition 1: Monotonicity

!!! abstract "Definition (Monotonicity)"
    The scheme $S_h$ is **monotone** if for any mesh functions $u_h \leq v_h$ (pointwise at all grid nodes):

    $$
    S_h(\tau, x, t, u_h) \leq S_h(\tau, x, t, v_h)
    $$

    for all $(\tau, x)$ and all $t \in \mathbb{R}$.

**Interpretation**: Increasing the input data does not decrease the scheme output. This is the discrete analog of the comparison principle.

**For explicit FDM schemes**: Monotonicity requires all stencil coefficients to be non-negative:

$$
u_j^{n+1} = \sum_k w_k u_{j+k}^n, \quad w_k \geq 0 \text{ for all } k, \quad \sum_k w_k = 1
$$

This is precisely the condition that the scheme computes a **convex combination** (or more generally, a positive linear combination) of neighboring values.

**Key consequence**: Monotone schemes are at most **first-order accurate** in general (this is the content of the Godunov theorem for conservation laws; for parabolic problems, the analogous result limits accuracy under monotonicity constraints).

### Condition 2: Stability

!!! abstract "Definition (Stability)"
    The scheme is **stable** if the numerical solutions are uniformly bounded:

    $$
    \|u_h\|_\infty \leq C \quad \text{for all } h > 0
    $$

    where $C$ is independent of $h$.

**For option pricing**: Option values are bounded by $0 \leq V \leq S$ (for calls) or $0 \leq V \leq K$ (for puts). Monotone schemes that preserve non-negativity and satisfy a discrete maximum principle automatically satisfy the stability condition.

### Condition 3: Consistency

!!! abstract "Definition (Consistency)"
    The scheme is **consistent** if for every smooth function $\varphi \in C^\infty$:

    $$
    \lim_{h \to 0,\; y \to x,\; \xi \to 0} S_h(\tau, y, \varphi(\tau, y) + \xi, \varphi + \xi) = F(\tau, x, \varphi(\tau, x), D\varphi(\tau, x), D^2\varphi(\tau, x))
    $$

    where $F = 0$ is the PDE.

**Interpretation**: When evaluated on smooth functions, the scheme recovers the PDE operator in the limit. This is the standard consistency condition, requiring the local truncation error to vanish.

Note that consistency only requires the scheme to agree with the PDE for **smooth** test functions. The solution itself need not be smooth.

---

## Statement of the Theorem

!!! abstract "Theorem (Barles and Souganidis, 1991)"
    Consider the degenerate elliptic PDE $F(\tau, x, u, Du, D^2u) = 0$ on a domain $\Omega$, with boundary conditions. Assume:

    1. A **comparison principle** holds for viscosity sub- and supersolutions
    2. The approximation scheme $S_h$ is **monotone**, **stable**, and **consistent**

    Then as $h \to 0$, the numerical solution $u_h$ converges **uniformly on compact subsets** to the unique viscosity solution $u$ of the PDE:

    $$
    \boxed{u_h \to u \quad \text{uniformly on compact sets as } h \to 0}
    $$

---

## Proof Outline

The proof uses **half-relaxed limits**, a technique from viscosity solution theory.

### Step 1: Define Half-Relaxed Limits

From the sequence of numerical solutions $\{u_h\}$ (which are uniformly bounded by stability), define:

$$
\overline{u}(\tau, x) = \limsup_{h \to 0,\; (\sigma, y) \to (\tau, x)} u_h(\sigma, y)
$$

$$
\underline{u}(\tau, x) = \liminf_{h \to 0,\; (\sigma, y) \to (\tau, x)} u_h(\sigma, y)
$$

By construction, $\underline{u} \leq \overline{u}$, and both are defined everywhere (the $\limsup$ and $\liminf$ exist because $\{u_h\}$ is bounded).

### Step 2: Show That the Limits Are Sub/Supersolutions

Using **monotonicity** and **consistency**, one proves:

- $\overline{u}$ is a viscosity **subsolution** of $F = 0$
- $\underline{u}$ is a viscosity **supersolution** of $F = 0$

The argument proceeds as follows. Let $\varphi$ be a smooth test function touching $\overline{u}$ from above at $(\tau_0, x_0)$. By the definition of $\overline{u}$ as a $\limsup$, there exist sequences $h_n \to 0$ and $(\tau_n, x_n) \to (\tau_0, x_0)$ with $u_{h_n}(\tau_n, x_n) \to \overline{u}(\tau_0, x_0)$.

Near $(\tau_n, x_n)$, the function $\varphi + \varepsilon_n$ (with a suitable small perturbation) touches $u_{h_n}$ from above. By the monotonicity of $S_h$:

$$
S_{h_n}(\tau_n, x_n, u_{h_n}(\tau_n, x_n), u_{h_n}) \leq S_{h_n}(\tau_n, x_n, \varphi(\tau_n, x_n) + \varepsilon_n, \varphi + \varepsilon_n)
$$

Since $S_{h_n}(\ldots, u_{h_n}, u_{h_n}) = 0$ (the numerical solution satisfies the scheme), the right-hand side is $\geq 0$. Taking $h_n \to 0$ and using consistency:

$$
F(\tau_0, x_0, \overline{u}(\tau_0, x_0), D\varphi(\tau_0, x_0), D^2\varphi(\tau_0, x_0)) \leq 0
$$

This is the subsolution property. The supersolution property for $\underline{u}$ is proved analogously.

### Step 3: Apply the Comparison Principle

Since $\overline{u}$ is a subsolution and $\underline{u}$ is a supersolution (both with the correct boundary data), the comparison principle gives:

$$
\overline{u} \leq \underline{u}
$$

Combined with $\underline{u} \leq \overline{u}$ (by definition):

$$
\overline{u} = \underline{u} = u
$$

where $u$ is the unique viscosity solution. Since the $\limsup$ and $\liminf$ agree, the convergence is uniform on compact sets. $\square$

---

## Verification for Black-Scholes Schemes

### Explicit Scheme (with CFL)

| Condition | Verification |
|-----------|-------------|
| **Monotonicity** | Non-negative coefficients: $a_j, b_j, c_j \geq 0$ (CFL + positivity) |
| **Stability** | Discrete maximum principle: $0 \leq u_j^n \leq C$ |
| **Consistency** | Taylor expansion: LTE $= O(\Delta\tau + (\Delta S)^2) \to 0$ |

**Conclusion**: The explicit scheme with CFL converges to the viscosity solution.

### Implicit Scheme

| Condition | Verification |
|-----------|-------------|
| **Monotonicity** | Inverse of an M-matrix has non-negative entries |
| **Stability** | Unconditional $L^\infty$ bound |
| **Consistency** | LTE $= O(\Delta\tau + (\Delta S)^2) \to 0$ |

**Conclusion**: The implicit scheme converges to the viscosity solution (unconditionally).

### Crank-Nicolson

| Condition | Verification |
|-----------|-------------|
| **Monotonicity** | **Fails** for large $\lambda$: amplification factor can be negative |
| **Stability** | $L^\infty$ stable (unconditionally) |
| **Consistency** | LTE $= O((\Delta\tau)^2 + (\Delta S)^2) \to 0$ |

**Conclusion**: Crank-Nicolson does **not** satisfy the Barles-Souganidis conditions directly. It converges for smooth problems (by Lax theory), but may produce incorrect results near non-smooth features. The Rannacher modification (implicit start) restores monotonicity where it matters.

---

## The Monotonicity-Accuracy Tradeoff

### Godunov-Type Barrier

A fundamental result in numerical PDE theory states that monotone schemes for second-order equations are limited to **first-order accuracy** in general. More precisely:

- **Monotone** $\Rightarrow$ at most $O(h)$ accuracy (in the $L^\infty$ norm, for general non-smooth solutions)
- Higher-order accuracy requires abandoning monotonicity

This creates a dilemma:

| Priority | Scheme type | Accuracy | Convergence guarantee |
|----------|------------|----------|----------------------|
| **Convergence** | Monotone (explicit/implicit) | $O(h)$ | Yes (Barles-Souganidis) |
| **Accuracy** | Non-monotone (Crank-Nicolson) | $O(h^2)$ | Only for smooth solutions |

### Practical Resolution

In practice, the tradeoff is managed by:

1. **Rannacher time-stepping**: Use monotone (implicit) steps near non-smooth data, then switch to the higher-order Crank-Nicolson
2. **Payoff smoothing**: Replace the kink with a smooth approximation, making the solution smooth enough for non-monotone schemes
3. **Richardson extrapolation**: Use a first-order monotone scheme and extrapolate to achieve higher effective order
4. **Wide-stencil monotone schemes**: Use broader stencils to maintain monotonicity with improved accuracy (at the cost of implementation complexity)

---

## Application to American Options

The American option obstacle problem:

$$
\min(-u_\tau + \mathcal{L}u,\; u - \Phi) = 0
$$

is naturally handled by the Barles-Souganidis framework. The discrete scheme becomes:

$$
u_j^{n+1} = \max\!\left(\text{time-step result},\; \Phi_j\right)
$$

The $\max$ operation preserves monotonicity (if the underlying time-step is monotone). Thus:

- Implicit scheme with projection: monotone, stable, consistent $\Rightarrow$ converges
- PSOR: equivalent to the projected implicit solve $\Rightarrow$ converges
- Penalty method: approximates the obstacle with a smooth penalty; converges as both $h \to 0$ and penalty parameter $\rho \to \infty$

!!! warning "Crank-Nicolson with Projection"
    Applying Crank-Nicolson and then projecting $u_j \leftarrow \max(u_j, \Phi_j)$ is **not** guaranteed to be monotone. For American options, the implicit scheme or Rannacher-started Crank-Nicolson is preferred to ensure reliable convergence.

---

## Connection to Other Convergence Frameworks

| Framework | Applies to | Key condition | Accuracy limit |
|-----------|-----------|---------------|---------------|
| **Lax equivalence** | Linear, well-posed | Stability | No limit |
| **Barles-Souganidis** | Nonlinear, degenerate | Monotonicity | $O(h)$ |
| **Krylov** | Bellman equations | Monotonicity + regularity | $O(h^{1/2})$ bounds |

The Barles-Souganidis theorem guarantees **qualitative convergence** ($u_h \to u$) but does not provide a **rate of convergence**. For rate estimates, additional regularity assumptions and more refined analysis (such as Krylov's methods) are needed.

---

## Summary

$$
\boxed{
\text{Monotone} + \text{Stable} + \text{Consistent} + \text{Comparison principle} \Longrightarrow u_h \to u \text{ (viscosity solution)}
}
$$

| Condition | Meaning | FDM verification |
|-----------|---------|-----------------|
| **Monotonicity** | Increasing data $\Rightarrow$ increasing output | Non-negative stencil coefficients |
| **Stability** | $\|u_h\|_\infty \leq C$ | Discrete maximum principle |
| **Consistency** | Scheme $\to$ PDE on smooth functions | Taylor expansion of LTE |
| **Comparison** | Ordering preserved from boundary | Property of the PDE |

| Scheme | Monotone | Converges (Barles-Souganidis) |
|--------|----------|-------------------------------|
| Explicit (CFL satisfied) | Yes | Yes |
| Implicit | Yes | Yes |
| Crank-Nicolson | No (in general) | Not guaranteed |
| Rannacher (implicit start + CN) | Yes (effectively) | Yes |

The Barles-Souganidis theorem provides the definitive convergence guarantee for finite difference methods applied to option pricing PDEs. Its practical message is clear: ensure your scheme is monotone (non-negative coefficients, CFL condition, or implicit time stepping) to guarantee convergence to the correct price, especially for American options and problems with non-smooth data.

---

## Exercises

**Exercise 1.** State the Barles-Souganidis theorem precisely. What are the four hypotheses, and what is the conclusion? Compare this to the Lax equivalence theorem and explain why the additional monotonicity condition is needed.

??? success "Solution to Exercise 1"
    **Barles-Souganidis Theorem** (1991): Consider the degenerate elliptic PDE $F(\tau, x, u, Du, D^2u) = 0$ on a domain $\Omega$ with boundary conditions. Assume:

    1. A **comparison principle** holds for viscosity sub- and supersolutions of $F = 0$
    2. The approximation scheme $S_h$ is **monotone**: if $u_h \leq v_h$ pointwise, then $S_h(\tau, x, t, u_h) \leq S_h(\tau, x, t, v_h)$
    3. The scheme is **stable**: $\|u_h\|_\infty \leq C$ uniformly in $h$
    4. The scheme is **consistent**: for every $\varphi \in C^\infty$, $S_h(\tau, y, \varphi + \xi, \varphi + \xi) \to F(\tau, x, \varphi, D\varphi, D^2\varphi)$ as $h \to 0$, $y \to x$, $\xi \to 0$

    **Conclusion**: The numerical solution $u_h$ converges uniformly on compact subsets to the unique viscosity solution $u$ as $h \to 0$.

    **Comparison with Lax equivalence**: The Lax equivalence theorem states that for **linear**, well-posed problems, consistency + stability $\Leftrightarrow$ convergence. The Barles-Souganidis theorem differs in two important ways:

    - It requires the additional condition of **monotonicity**, which has no analog in the Lax framework
    - The implication is one-directional ($\Rightarrow$, not $\Leftrightarrow$)

    **Why monotonicity is needed**: Without monotonicity, a consistent and stable scheme can converge to the wrong weak solution. For nonlinear or degenerate PDEs, the notion of solution is not unique without specifying a selection criterion. The viscosity solution is selected by the comparison principle, and monotonicity is the discrete property that ensures the numerical scheme respects this selection. The Crank-Nicolson scheme demonstrates the failure: it is consistent and stable, but not monotone, and near payoff kinks it can converge to a function that violates the viscosity solution conditions. Monotonicity guarantees that the half-relaxed limits $\overline{u}$ and $\underline{u}$ inherit the sub/supersolution properties from the scheme, which is the essential step in the proof.

---

**Exercise 2.** Verify each of the three Barles-Souganidis conditions for the explicit scheme with the CFL condition satisfied: (a) monotonicity from non-negative stencil coefficients, (b) stability from the discrete maximum principle, (c) consistency from Taylor expansion of the local truncation error.

??? success "Solution to Exercise 2"
    Consider the explicit scheme $u_j^{n+1} = a_j u_{j-1}^n + b_j u_j^n + c_j u_{j+1}^n$ applied to the Black-Scholes PDE with CFL condition satisfied.

    **(a) Monotonicity**: Under the CFL condition, the stencil coefficients for the Black-Scholes discretization are

    $$
    a_j = \frac{\Delta\tau}{2}\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} - \frac{rS_j}{\Delta S}\right), \quad c_j = \frac{\Delta\tau}{2}\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + \frac{rS_j}{\Delta S}\right)
    $$

    $$
    b_j = 1 - a_j - c_j = 1 - \Delta\tau\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + r\right)
    $$

    The CFL condition $\Delta\tau \leq (\Delta S)^2 / (\sigma^2 S_{\max}^2 + r(\Delta S)^2)$ ensures $b_j \geq 0$. With a sufficiently fine grid (or upwinding), $a_j \geq 0$ and $c_j \geq 0$. All coefficients are non-negative, so if $u^n \leq v^n$ pointwise, then $u^{n+1}_j = a_j u^n_{j-1} + b_j u^n_j + c_j u^n_{j+1} \leq a_j v^n_{j-1} + b_j v^n_j + c_j v^n_{j+1} = v^{n+1}_j$. The scheme is monotone.

    **(b) Stability**: Since $a_j + b_j + c_j = 1$ and all coefficients are non-negative, the discrete maximum principle holds: $\min_j u_j^n \leq u_j^{n+1} \leq \max_j u_j^n$. For option pricing with non-negative payoff bounded by $C$, we get $0 \leq u_j^n \leq C$ for all $n$ and $j$. Thus $\|u_h\|_\infty \leq C$ independently of $h$.

    **(c) Consistency**: For a smooth test function $\varphi(\tau, S)$, substitute into the scheme and Taylor-expand around $(\tau^n, S_j)$:

    $$
    \varphi_j^{n+1} = \varphi_j^n + \Delta\tau\, \varphi_\tau + O((\Delta\tau)^2)
    $$

    $$
    a_j \varphi_{j-1}^n + b_j \varphi_j^n + c_j \varphi_{j+1}^n = \varphi_j^n + \Delta\tau\left(\frac{1}{2}\sigma^2 S_j^2 \varphi_{SS} + rS_j \varphi_S - r\varphi\right) + O(\Delta\tau \cdot \Delta S^2)
    $$

    The local truncation error is $\text{LTE} = O(\Delta\tau + (\Delta S)^2) \to 0$ as $h \to 0$, confirming consistency.

---

**Exercise 3.** The Crank-Nicolson scheme fails the monotonicity condition because its amplification factor can be negative for high-frequency modes. Give a concrete example with specific parameter values where this failure produces visible oscillations in the numerical solution.

??? success "Solution to Exercise 3"
    Consider an American put option with $K = 100$, $\sigma = 0.4$, $r = 0.05$, $T = 1$. Use a uniform grid with $S_{\max} = 300$, $N_S = 100$ grid points ($\Delta S = 3$), and $N_\tau = 50$ time steps ($\Delta\tau = 0.02$).

    The mesh ratio at $S = S_{\max} = 300$ is

    $$
    \lambda = \frac{\sigma^2 S_{\max}^2 \Delta\tau}{(\Delta S)^2} = \frac{0.16 \times 90000 \times 0.02}{9} = 32
    $$

    The Crank-Nicolson amplification factor for the highest frequency mode ($\theta = \pi$) is

    $$
    g(\pi) = \frac{1 - 2\lambda}{1 + 2\lambda} = \frac{1 - 64}{1 + 64} = \frac{-63}{65} \approx -0.969
    $$

    This is negative with magnitude close to 1, meaning high-frequency components are nearly preserved in amplitude but **reversed in sign** at each time step.

    The put payoff $(K - S)^+$ has a kink at $S = K = 100$. This kink generates significant high-frequency Fourier components. Under Crank-Nicolson, these components are sign-reversed at each step, producing oscillations: the numerical solution alternates above and below the true value in a checkerboard pattern near $S = K$.

    After applying the American constraint $u_j \leftarrow \max(u_j, (K - S_j)^+)$, the oscillations interact with the early exercise boundary. The spurious undershoots (negative oscillations) are clipped by the obstacle, but the overshoots remain, producing a jagged numerical free boundary and option values that are systematically too high near $S^*(\tau)$. The computed Greeks ($\Delta$ and $\Gamma$) exhibit visible sawtooth patterns that do not diminish under mesh refinement, demonstrating that the scheme does not converge to the viscosity solution near the non-smooth features.

---

**Exercise 4.** The Godunov-type barrier states that monotone schemes are limited to first-order accuracy. Explain the practical resolution of this accuracy-monotonicity tradeoff: how does the Rannacher time-stepping strategy achieve effectively second-order accuracy while maintaining monotonicity where it matters?

??? success "Solution to Exercise 4"
    The Godunov-type barrier states that monotone linear schemes for second-order PDEs are limited to first-order accuracy ($O(h)$ in $L^\infty$). This creates a fundamental tension: monotonicity guarantees convergence but limits accuracy to $O(h)$, while higher-order schemes (like Crank-Nicolson, $O(h^2)$) sacrifice monotonicity.

    The **Rannacher time-stepping** strategy resolves this tradeoff by exploiting the fact that monotonicity is only critical near non-smooth features of the solution. The strategy has two phases:

    **Phase 1 (Implicit start)**: Perform 2--4 fully implicit (backward Euler) half-steps at the beginning of the time marching (near the terminal payoff). The fully implicit scheme is unconditionally monotone because the inverse of the resulting M-matrix has all non-negative entries. These monotone steps damp the high-frequency errors introduced by the payoff kink at $S = K$. After a few implicit steps, the numerical solution is effectively smooth.

    **Phase 2 (Crank-Nicolson continuation)**: Switch to Crank-Nicolson for all remaining time steps. Since the solution is now smooth (the initial non-smoothness has been damped), Crank-Nicolson's lack of monotonicity does not cause problems --- it converges at second order for smooth solutions by the Lax equivalence theorem.

    The combined scheme achieves effectively second-order accuracy ($O((\Delta\tau)^2 + (\Delta S)^2)$) overall because the implicit start introduces only $O(\Delta\tau)$ error over a fixed number of steps (which vanishes relative to the global $O((\Delta\tau)^2)$ error of Crank-Nicolson), while restoring the smoothness that Crank-Nicolson requires. The monotone initial phase ensures that the scheme respects the viscosity solution framework where it matters most (near the payoff kink), and the Crank-Nicolson continuation provides the desired accuracy.

---

**Exercise 5.** For the American option obstacle problem with projection $u_j^{n+1} = \max(\text{time-step result}, \Phi_j)$, explain why the $\max$ operation preserves monotonicity. Specifically, show that if the time-stepping scheme is monotone and $u \leq v$ at all nodes, then $\max(u_j, \Phi_j) \leq \max(v_j, \Phi_j)$.

??? success "Solution to Exercise 5"
    We need to show that the $\max$ operation preserves monotonicity. Let the time-stepping scheme produce $\tilde{u}_j$ from input data $\{u_k\}$ and $\tilde{v}_j$ from input data $\{v_k\}$, where $u_k \leq v_k$ for all $k$.

    **Monotonicity of time-stepping (by assumption)**: Since the underlying scheme is monotone and $u_k \leq v_k$ for all $k$:

    $$
    \tilde{u}_j \leq \tilde{v}_j \quad \text{for all } j
    $$

    **Monotonicity of $\max$**: We claim that for any fixed $\Phi_j$ and any $a \leq b$:

    $$
    \max(a, \Phi_j) \leq \max(b, \Phi_j)
    $$

    This follows by considering three cases:

    - If $a \leq b \leq \Phi_j$: both sides equal $\Phi_j$, so $\Phi_j \leq \Phi_j$
    - If $a \leq \Phi_j \leq b$: the left side is $\Phi_j$ and the right side is $b$, so $\Phi_j \leq b$
    - If $\Phi_j \leq a \leq b$: the left side is $a$ and the right side is $b$, so $a \leq b$

    In all cases, the inequality holds.

    **Composition preserves monotonicity**: Applying both results, if $u_k \leq v_k$ for all $k$, then

    $$
    u_j^{n+1} = \max(\tilde{u}_j, \Phi_j) \leq \max(\tilde{v}_j, \Phi_j) = v_j^{n+1}
    $$

    Therefore the full American option scheme (monotone time-step followed by $\max$ projection) is monotone. Combined with stability (the projection does not increase the $L^\infty$ norm beyond $\max(\|u_h\|_\infty, \|\Phi\|_\infty)$) and consistency (the projection does not affect the truncation error in the continuation region), the Barles-Souganidis theorem guarantees convergence to the viscosity solution of the obstacle problem.

---

**Exercise 6.** The Barles-Souganidis theorem guarantees convergence but does not provide a convergence rate. Why is this limitation important in practice? Describe how you would empirically determine the convergence rate of a monotone scheme for an American put option where no analytical solution is available.

??? success "Solution to Exercise 6"
    **Why the lack of a convergence rate matters**: The Barles-Souganidis theorem guarantees that $u_h \to u$ as $h \to 0$, but it does not tell us **how fast**. In practice, a financial engineer needs to know:

    - How fine a grid is needed to achieve a desired accuracy (e.g., pricing to within \$0.01)
    - How computational cost scales with accuracy requirements
    - Whether Richardson extrapolation or other acceleration techniques are applicable

    Without a theoretical rate, these questions cannot be answered a priori. The rate could be $O(h)$, $O(h^{1/2})$, or even $O(h^{1/4})$ depending on the regularity of the solution. For smooth European options, one typically observes $O(h)$ (first-order) convergence for monotone schemes, but for American options the free boundary introduces a regularity limitation that can degrade the rate.

    **Empirical convergence rate determination**: Since no closed-form solution exists for the American put, the convergence rate is determined by a **self-convergence study**:

    1. **Compute a reference solution** $u_{\text{ref}}$ on a very fine grid (e.g., $N = 8192$ spatial points and proportionally many time steps)

    2. **Compute solutions on a sequence of coarsening grids**: $N = 64, 128, 256, 512, 1024, 2048$, with time steps refined proportionally to maintain the CFL condition ($\Delta\tau \propto (\Delta S)^2$ for explicit schemes, or $\Delta\tau \propto \Delta S$ for implicit)

    3. **Measure the error** $e_N = \|u_N - u_{\text{ref}}\|_\infty$ (or at a specific point, e.g., $S = K$) for each grid

    4. **Estimate the convergence rate** $p$ from consecutive error pairs:

    $$
    p \approx \frac{\log(e_N / e_{2N})}{\log 2}
    $$

    5. **Verify consistency**: The estimated $p$ should stabilize as $N$ increases. For a monotone scheme (implicit Euler) applied to the American put, one typically observes $p \approx 1$ (first-order convergence), consistent with the Godunov barrier

    An alternative to the reference solution approach is to use the **ratio test**: compute $u_N$, $u_{2N}$, and $u_{4N}$, then estimate the rate from

    $$
    p \approx \frac{\log\bigl((u_N - u_{2N}) / (u_{2N} - u_{4N})\bigr)}{\log 2}
    $$

    This avoids the need for a reference solution and is the standard approach when no analytical benchmark is available.
