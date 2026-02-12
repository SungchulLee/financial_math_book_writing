# Explicit, Implicit, and Crank-Nicolson Schemes

After spatial discretization, the Black-Scholes PDE becomes an ODE system in time. The choice of **time-stepping scheme** determines stability, accuracy, and computational cost.

---

## The Semi-Discrete System

After spatial discretization:

$$
\frac{d\mathbf{u}}{d\tau} = A\mathbf{u}
$$

where $\mathbf{u} = (u_1, \ldots, u_{M-1})^T$ and $A$ is the tridiagonal spatial operator matrix.

**Goal**: Advance from $\mathbf{u}^n$ at time $\tau_n$ to $\mathbf{u}^{n+1}$ at time $\tau_{n+1} = \tau_n + \Delta\tau$.

---

## Explicit Scheme (Forward Euler)

### Formulation

Evaluate the right-hand side at the **known** time level $n$:

$$
\boxed{
\mathbf{u}^{n+1} = \mathbf{u}^n + \Delta\tau \cdot A\mathbf{u}^n = (I + \Delta\tau A)\mathbf{u}^n
}
$$

### Component Form

$$
u_j^{n+1} = a_j u_{j-1}^n + (1 + b_j)u_j^n + c_j u_{j+1}^n
$$

### Properties

| Property | Assessment |
|----------|------------|
| Implementation | Simple, no linear solve |
| Cost per step | $O(M)$ |
| Stability | **Conditional** |
| Accuracy | First-order in time |

### Stability Condition (CFL)

For the heat equation, stability requires:

$$
\boxed{
\Delta\tau \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}
}
$$

This is often **very restrictive**, requiring many time steps.

**Example**: $\sigma = 0.3$, $S_{\max} = 300$, $\Delta S = 1$:

$$
\Delta\tau \leq \frac{1}{0.09 \times 90000} \approx 0.000123
$$

For $T = 1$ year, this requires $N > 8000$ time steps!

---

## Implicit Scheme (Backward Euler)

### Formulation

Evaluate the right-hand side at the **unknown** time level $n+1$:

$$
\mathbf{u}^{n+1} = \mathbf{u}^n + \Delta\tau \cdot A\mathbf{u}^{n+1}
$$

Rearranging:

$$
\boxed{
(I - \Delta\tau A)\mathbf{u}^{n+1} = \mathbf{u}^n
}
$$

### Properties

| Property | Assessment |
|----------|------------|
| Implementation | Requires linear solve |
| Cost per step | $O(M)$ with tridiagonal solver |
| Stability | **Unconditionally stable** |
| Accuracy | First-order in time |

### Linear System

The matrix $(I - \Delta\tau A)$ is tridiagonal and can be solved efficiently using the **Thomas algorithm** (tridiagonal matrix algorithm) in $O(M)$ operations.

### Advantages

- No time step restriction for stability
- Can use large $\Delta\tau$ if accuracy permits
- Robust for stiff problems

---

## Crank-Nicolson Scheme (Trapezoidal Rule)

### Formulation

Average of explicit and implicit:

$$
\mathbf{u}^{n+1} = \mathbf{u}^n + \frac{\Delta\tau}{2}(A\mathbf{u}^n + A\mathbf{u}^{n+1})
$$

Rearranging:

$$
\boxed{
\left(I - \frac{\Delta\tau}{2}A\right)\mathbf{u}^{n+1} = \left(I + \frac{\Delta\tau}{2}A\right)\mathbf{u}^n
}
$$

### Properties

| Property | Assessment |
|----------|------------|
| Implementation | Requires linear solve |
| Cost per step | $O(M)$ with tridiagonal solver |
| Stability | **Unconditionally stable** |
| Accuracy | **Second-order** in time |

### Why Second-Order?

Crank-Nicolson is equivalent to the trapezoidal rule for ODEs, which has error $O((\Delta\tau)^2)$.

---

## The Theta-Scheme (Generalization)

The **theta-scheme** parameterizes the family:

$$
\boxed{
(I - \theta\Delta\tau A)\mathbf{u}^{n+1} = (I + (1-\theta)\Delta\tau A)\mathbf{u}^n
}
$$

| $\theta$ | Scheme | Stability | Accuracy |
|----------|--------|-----------|----------|
| 0 | Explicit | Conditional | $O(\Delta\tau)$ |
| 1/2 | Crank-Nicolson | Unconditional | $O((\Delta\tau)^2)$ |
| 1 | Implicit | Unconditional | $O(\Delta\tau)$ |

**Common choice**: $\theta = 0.5$ (Crank-Nicolson) for accuracy, or $\theta = 1$ for robustness.

---

## Oscillation Issues with Crank-Nicolson

### The Problem

For **non-smooth** initial data (e.g., option payoffs with kinks), Crank-Nicolson can produce **oscillations** near $\tau = 0$.

**Example**: European call payoff $(S-K)^+$ has a discontinuous derivative at $S = K$.

### Cause

Crank-Nicolson is not **monotone**—the discrete maximum principle can be violated.

### Solution: Rannacher Time-Stepping

Use a few **implicit** steps initially, then switch to Crank-Nicolson:

```
For n = 0, 1:  (first two steps)
    Use backward Euler (θ = 1)
For n = 2, 3, ..., N-1:
    Use Crank-Nicolson (θ = 0.5)
```

This damps high-frequency oscillations while maintaining overall second-order accuracy.

---

## Comparison of Schemes

### Accuracy vs Stability

| Scheme | Time Accuracy | Space Accuracy | Stability |
|--------|---------------|----------------|-----------|
| Explicit | $O(\Delta\tau)$ | $O((\Delta S)^2)$ | Conditional |
| Implicit | $O(\Delta\tau)$ | $O((\Delta S)^2)$ | Unconditional |
| C-N | $O((\Delta\tau)^2)$ | $O((\Delta S)^2)$ | Unconditional |

### Computational Cost

| Scheme | Cost per Step | Total Cost (fixed accuracy) |
|--------|---------------|---------------------------|
| Explicit | $O(M)$ | High (many steps needed) |
| Implicit | $O(M)$ | Moderate |
| C-N | $O(M)$ | Low (fewer steps needed) |

---

## Implementation: Thomas Algorithm

For the tridiagonal system:

$$
\alpha_j u_{j-1} + \beta_j u_j + \gamma_j u_{j+1} = d_j
$$

**Forward sweep**:
```
c'_1 = γ_1 / β_1
d'_1 = d_1 / β_1
For j = 2, ..., M-1:
    c'_j = γ_j / (β_j - α_j c'_{j-1})
    d'_j = (d_j - α_j d'_{j-1}) / (β_j - α_j c'_{j-1})
```

**Back substitution**:
```
u_{M-1} = d'_{M-1}
For j = M-2, ..., 1:
    u_j = d'_j - c'_j u_{j+1}
```

**Cost**: $O(M)$ operations.

---

## Practical Recommendations

### For European Options

1. Use **Crank-Nicolson** with **Rannacher smoothing**
2. Grid: $M \approx 200$, $N \approx 100$
3. Center grid around strike $K$

### For American Options

1. Use **implicit** scheme (easier constraint enforcement)
2. Project after each step: $u_j^{n+1} \leftarrow \max(u_j^{n+1}, \Phi_j)$

### For Barrier Options

1. Use **implicit** for stability near barriers
2. Place grid points exactly on barriers

---

## Summary

$$
\boxed{
\begin{aligned}
\text{Explicit}: & \quad \mathbf{u}^{n+1} = (I + \Delta\tau A)\mathbf{u}^n \\
\text{Implicit}: & \quad (I - \Delta\tau A)\mathbf{u}^{n+1} = \mathbf{u}^n \\
\text{Crank-Nicolson}: & \quad \left(I - \frac{\Delta\tau}{2}A\right)\mathbf{u}^{n+1} = \left(I + \frac{\Delta\tau}{2}A\right)\mathbf{u}^n
\end{aligned}
}
$$

| Recommendation | Scheme |
|----------------|--------|
| Accuracy priority | Crank-Nicolson |
| Robustness priority | Implicit |
| Simplicity priority | Explicit (with small $\Delta\tau$) |
| Non-smooth data | Rannacher (implicit start, then C-N) |

**The choice of time-stepping scheme balances accuracy, stability, and computational efficiency.**
