# Stability, Consistency, and Convergence

The reliability of a finite difference scheme depends on three fundamental properties: **consistency** (local accuracy), **stability** (bounded error growth), and **convergence** (approach to the true solution). The Lax Equivalence Theorem connects these concepts.

---

## The Fundamental Principle

For linear, well-posed problems:

$$
\boxed{
\text{Consistency} + \text{Stability} \Longrightarrow \text{Convergence}
}
$$

This is the **Lax Equivalence Theorem**: a consistent scheme converges if and only if it is stable.

---

## Consistency

### Definition

A scheme is **consistent** if the local truncation error vanishes as the mesh is refined.

For a PDE $\mathcal{L}u = 0$ and discrete approximation $\mathcal{L}_{\Delta}u_{\Delta} = 0$:

$$
\text{Local truncation error} = \mathcal{L}_{\Delta}u - \mathcal{L}u
$$

where $u$ is the exact solution.

**Consistency**: LTE $\to 0$ as $\Delta\tau, \Delta S \to 0$.

### Order of Consistency

If LTE $= O((\Delta\tau)^p + (\Delta S)^q)$, the scheme is:
- $p$-th order in time
- $q$-th order in space

### Example: Crank-Nicolson

For smooth solutions:

$$
\text{LTE} = O((\Delta\tau)^2 + (\Delta S)^2)
$$

Crank-Nicolson is **second-order consistent** in both time and space.

---

## Stability

### Definition

A scheme is **stable** if errors remain bounded as the computation proceeds.

For a linear scheme $\mathbf{u}^{n+1} = B\mathbf{u}^n$, stability requires:

$$
\boxed{
\|B^n\| \leq C \quad \text{for all } n\Delta\tau \leq T
}
$$

for some constant $C$ independent of the mesh.

### Von Neumann (Fourier) Analysis

The standard method for analyzing stability of constant-coefficient schemes.

**Idea**: Decompose errors into Fourier modes $e^{ik\xi}$ and analyze their growth.

**Amplification factor**: For mode $k$, let $G(k)$ be the ratio of amplitudes at successive time steps.

**Stability criterion**:

$$
\boxed{
|G(k)| \leq 1 \quad \text{for all } k
}
$$

### Example: Explicit Scheme for Heat Equation

For $u_\tau = \frac{1}{2}u_{xx}$ with explicit discretization:

$$
G = 1 - 2\lambda(1 - \cos(k\Delta x))
$$

where $\lambda = \frac{\Delta\tau}{(\Delta x)^2}$.

**Stability requires**: $|G| \leq 1 \Rightarrow \lambda \leq \frac{1}{2}$

$$
\boxed{
\Delta\tau \leq \frac{(\Delta x)^2}{2} \quad \text{(CFL condition)}
}
$$

### Example: Implicit Scheme

$$
G = \frac{1}{1 + 2\lambda(1 - \cos(k\Delta x))}
$$

Since the denominator $> 1$, we have $|G| < 1$ for all $\lambda > 0$.

**Unconditionally stable**: No restriction on $\Delta\tau$.

### Example: Crank-Nicolson

$$
G = \frac{1 - \lambda(1 - \cos(k\Delta x))}{1 + \lambda(1 - \cos(k\Delta x))}
$$

**Unconditionally stable**: $|G| \leq 1$ for all $\lambda$.

---

## Convergence

### Definition

A scheme **converges** if the numerical solution approaches the exact solution as the mesh is refined:

$$
\lim_{\Delta\tau, \Delta S \to 0} \max_{n,j} |u_j^n - u(\tau_n, S_j)| = 0
$$

### Convergence Rate

If the error satisfies:

$$
\|u_{\Delta} - u\| = O((\Delta\tau)^p + (\Delta S)^q)
$$

the scheme has convergence rate $(p, q)$.

### The Lax Equivalence Theorem

**Theorem**: For a well-posed linear initial value problem and a consistent finite difference scheme, **stability is equivalent to convergence**.

**Proof sketch**:
1. Let $e^n = u^n - u(\tau_n)$ be the global error
2. Error evolution: $e^{n+1} = Be^n + \text{LTE}$
3. By induction: $e^n = B^n e^0 + \sum_{k=0}^{n-1} B^{n-1-k}\text{LTE}_k$
4. If stable: $\|B^n\| \leq C$, so errors remain bounded
5. If consistent: LTE $\to 0$, so total error $\to 0$

---

## Practical Stability Analysis

### Matrix Criterion

For $\mathbf{u}^{n+1} = B\mathbf{u}^n$, stability requires:

$$
\rho(B) \leq 1 + O(\Delta\tau)
$$

where $\rho(B)$ is the spectral radius (largest eigenvalue magnitude).

### Energy Methods

For some problems, multiply by $u$ and sum to get energy estimates:

$$
\|u^{n+1}\|^2 \leq \|u^n\|^2
$$

This directly proves stability.

### Comparison Principles

**Monotone schemes** preserve the discrete maximum principle:

$$
\min_j u_j^n \leq u_j^{n+1} \leq \max_j u_j^n
$$

This implies $L^\infty$ stability.

---

## Issues with Non-Smooth Data

### The Problem

Option payoffs like $(S-K)^+$ are not smooth at $S = K$. This affects:

1. **Consistency**: Taylor expansions assume smoothness
2. **Convergence rate**: Observed order may be lower than theoretical

### Observed vs Theoretical Convergence

| Data Smoothness | Theoretical Order | Observed Order |
|-----------------|-------------------|----------------|
| $C^\infty$ | 2 (C-N) | 2 |
| $C^0$ (continuous) | 2 | 1-1.5 |
| Kink at strike | 2 | 0.5-1 |

### Remedies

1. **Rannacher smoothing**: Implicit steps near maturity
2. **Payoff smoothing**: Replace $(S-K)^+$ with smooth approximation
3. **Grid adaptation**: Fine grid near strike
4. **Richardson extrapolation**: Improve convergence from multiple grids

---

## The CFL Condition

The **Courant-Friedrichs-Lewy (CFL) condition** is a necessary condition for stability of explicit schemes.

### For Advection Equation $u_t + cu_x = 0$

$$
\boxed{
|c|\frac{\Delta t}{\Delta x} \leq 1
}
$$

**Interpretation**: The numerical domain of dependence must contain the physical domain of dependence.

### For Diffusion Equation $u_t = Du_{xx}$

$$
\boxed{
D\frac{\Delta t}{(\Delta x)^2} \leq \frac{1}{2}
}
$$

### For Black-Scholes (Variable Coefficients)

The CFL condition involves the local diffusion coefficient $\frac{1}{2}\sigma^2 S^2$:

$$
\frac{\sigma^2 S_{\max}^2 \Delta\tau}{2(\Delta S)^2} \leq \frac{1}{2}
$$

---

## Convergence Study (Practical)

To verify implementation, perform a **convergence study**:

1. Compute solutions on grids with $M, 2M, 4M, \ldots$ points
2. Compare to analytical solution (if available) or finest grid
3. Plot error vs grid size on log-log scale
4. Slope gives convergence order

### Example Results

| Grid | Error | Ratio |
|------|-------|-------|
| $M = 50$ | 0.0412 | — |
| $M = 100$ | 0.0103 | 4.0 |
| $M = 200$ | 0.0026 | 4.0 |

Ratio $\approx 4$ confirms second-order convergence (error $\sim M^{-2}$).

---

## Summary

$$
\boxed{
\text{Consistency} + \text{Stability} \Longleftrightarrow \text{Convergence}
}
$$

| Concept | Definition | Verification |
|---------|------------|--------------|
| **Consistency** | LTE $\to 0$ | Taylor expansion |
| **Stability** | $\|B^n\| \leq C$ | Von Neumann analysis |
| **Convergence** | $u_\Delta \to u$ | Lax theorem + above |

| Scheme | Stability | CFL Restriction |
|--------|-----------|-----------------|
| Explicit | Conditional | $\Delta\tau \leq C(\Delta S)^2$ |
| Implicit | Unconditional | None |
| Crank-Nicolson | Unconditional | None |

**A well-designed finite difference scheme must be both consistent and stable to guarantee convergence to the correct solution.**
