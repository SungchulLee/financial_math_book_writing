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
