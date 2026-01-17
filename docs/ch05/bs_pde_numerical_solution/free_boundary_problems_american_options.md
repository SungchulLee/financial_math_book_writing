# Free Boundary Problems and American Options

American options can be exercised at any time before expiration, leading to an **optimal stopping problem**. Numerically, this becomes a **free boundary problem** or equivalently a **variational inequality** (obstacle problem).

---

## The American Option Problem

### Optimal Stopping Formulation

Under risk-neutral dynamics $dS_t = rS_t\,dt + \sigma S_t\,dW_t$:

$$
\boxed{
V(t,S) = \sup_{\tau \in \mathcal{T}_{t,T}} \mathbb{E}^{\mathbb{Q}}\left[e^{-r(\tau-t)}\Phi(S_\tau) \mid S_t = S\right]
}
$$

where $\mathcal{T}_{t,T}$ is the set of stopping times in $[t,T]$.

### The Variational Inequality

The American option price satisfies:

$$
\boxed{
\min\left(-\frac{\partial V}{\partial t} - \mathcal{L}V + rV, \; V - \Phi\right) = 0
}
$$

where $\mathcal{L}V = \frac{1}{2}\sigma^2 S^2 V_{SS} + rS V_S$ is the Black-Scholes generator.

### Two Regions

1. **Continuation region** $\mathcal{C}$: $V > \Phi$, and the PDE holds:
   $$\frac{\partial V}{\partial t} + \mathcal{L}V - rV = 0$$

2. **Exercise region** $\mathcal{E}$: $V = \Phi$ (immediate exercise is optimal)

---

## The Free Boundary

### Definition

The **exercise boundary** $S^*(t)$ separates the two regions:

- **American put**: $\mathcal{E} = \{S < S^*(t)\}$
- **American call (no dividends)**: Never optimal to exercise early ($S^* = \infty$)
- **American call (with dividends)**: $\mathcal{E} = \{S > S^*(t)\}$

### Smooth Pasting Conditions

At the free boundary $S = S^*(t)$:

$$
\boxed{
V(t, S^*(t)) = \Phi(S^*(t)), \quad \frac{\partial V}{\partial S}(t, S^*(t)) = \Phi'(S^*(t))
}
$$

For an American put with $\Phi(S) = (K-S)^+$:

$$
V(t, S^*) = K - S^*, \quad V_S(t, S^*) = -1
$$

### Early Exercise Premium

$$
V_{\text{American}} = V_{\text{European}} + \text{Early Exercise Premium}
$$

The premium is always non-negative and reflects the value of the exercise option.

---

## Numerical Methods: Projection

### Simple Projection Method

After each time step, **project** onto the constraint:

$$
\boxed{
u_j^{n+1} \leftarrow \max(u_j^{n+1}, \Phi_j)
}
$$

### Algorithm (Implicit + Projection)

```
1. Solve (I - Δτ A)ũ^{n+1} = u^n  (unconstrained)
2. Project: u_j^{n+1} = max(ũ_j^{n+1}, Φ_j) for all j
3. Repeat for next time step
```

### Issues

- Simple but may lose accuracy near the free boundary
- First-order in time (even with Crank-Nicolson base scheme)
- Smooth pasting not explicitly enforced

---

## Linear Complementarity Problem (LCP)

### Formulation

The discrete problem at each time step is:

$$
\boxed{
\begin{aligned}
& L\mathbf{u} \geq \mathbf{f} \\
& \mathbf{u} \geq \boldsymbol{\Phi} \\
& (L\mathbf{u} - \mathbf{f})^T(\mathbf{u} - \boldsymbol{\Phi}) = 0
\end{aligned}
}
$$

where $L = I - \Delta\tau A$ and $\mathbf{f} = \mathbf{u}^n$.

### Interpretation

- Either $u_j > \Phi_j$ (continuation) and the PDE holds: $(L\mathbf{u})_j = f_j$
- Or $u_j = \Phi_j$ (exercise) and the constraint binds

---

## PSOR Algorithm

The **Projected Successive Over-Relaxation (PSOR)** method solves the LCP efficiently.

### Algorithm

For iteration $k+1$:

$$
\tilde{u}_j^{(k+1)} = (1-\omega)u_j^{(k)} + \frac{\omega}{l_{jj}}\left(f_j - \sum_{i<j} l_{ji}u_i^{(k+1)} - \sum_{i>j} l_{ji}u_i^{(k)}\right)
$$

$$
u_j^{(k+1)} = \max(\tilde{u}_j^{(k+1)}, \Phi_j)
$$

### Parameters

- $\omega \in (1, 2)$: over-relaxation parameter (typically $\omega \approx 1.2$)
- Converges when $\|\mathbf{u}^{(k+1)} - \mathbf{u}^{(k)}\| < \epsilon$

### Convergence

- Linear convergence rate
- Typically 5-20 iterations per time step
- Total cost: $O(MN \cdot \text{iterations})$

---

## Penalty Method

### Idea

Replace the hard constraint with a soft penalty:

$$
\frac{\partial V}{\partial t} + \mathcal{L}V - rV + \rho(V - \Phi)^- = 0
$$

where $(x)^- = \min(x, 0)$ and $\rho \gg 1$ is the penalty parameter.

### Discrete Form

$$
(I - \Delta\tau A + \Delta\tau \rho P)\mathbf{u}^{n+1} = \mathbf{u}^n + \Delta\tau \rho P\boldsymbol{\Phi}
$$

where $P$ is a diagonal matrix with $P_{jj} = 1$ if $u_j < \Phi_j$, else $0$.

### Properties

- Smooth formulation (no explicit constraint)
- Easy to implement with existing solvers
- Error $\sim O(1/\rho)$ from penalty approximation
- Typically $\rho = 10^6$ to $10^8$

---

## Brennan-Schwartz Algorithm

For American puts specifically, there's an elegant direct method.

### Key Observation

The exercise boundary $S^*(t)$ increases as $t \to T$ (from below).

### Algorithm

Work backward from maturity:
1. Find the grid point where exercise first becomes optimal
2. Set $u_j = \Phi_j$ for $j \leq j^*$
3. Solve PDE only for $j > j^*$

### Advantage

No iteration required—direct solve at each time step.

---

## Front-Fixing Methods

Transform coordinates to fix the free boundary.

### Coordinate Transform

Let $\xi = S/S^*(t)$ so that the boundary is always at $\xi = 1$.

### Transformed PDE

Additional terms appear involving $\dot{S}^*$, which must be determined as part of the solution.

### Advantage

High accuracy near the free boundary.

### Disadvantage

More complex implementation; boundary must be tracked.

---

## Convergence and Accuracy

### Order of Convergence

| Method | Time Order | Space Order |
|--------|------------|-------------|
| Projection + Implicit | 1 | 2 |
| PSOR + C-N | 1-1.5 | 2 |
| Penalty | 1 | 2 |
| Front-fixing | 2 | 2 |

**Note**: The free boundary introduces non-smoothness that typically limits time accuracy to first-order.

### Grid Considerations

- Place grid points near expected $S^*$
- Adaptive grids can improve efficiency
- Smoothing at maturity helps (Rannacher)

---

## Comparison of Methods

| Method | Ease | Accuracy | Speed |
|--------|------|----------|-------|
| Projection | Easy | Low | Fast |
| PSOR | Moderate | Good | Moderate |
| Penalty | Easy | Good | Fast |
| Front-fixing | Hard | High | Moderate |

---

## Summary

$$
\boxed{
\min\left(-\frac{\partial V}{\partial t} - \mathcal{L}V + rV, \; V - \Phi\right) = 0
}
$$

| Aspect | Description |
|--------|-------------|
| Problem type | Free boundary / obstacle problem |
| Constraint | $V \geq \Phi$ (can exercise anytime) |
| Free boundary | $S^*(t)$ separates exercise/continuation |
| Smooth pasting | $V$ and $V_S$ continuous at boundary |

| Method | Key Idea |
|--------|----------|
| Projection | Enforce $u \geq \Phi$ after each step |
| PSOR | Iteratively solve LCP |
| Penalty | Soft constraint via large $\rho$ |
| Front-fixing | Track boundary explicitly |

**American option pricing requires specialized numerical techniques to handle the free boundary between continuation and exercise regions.**
