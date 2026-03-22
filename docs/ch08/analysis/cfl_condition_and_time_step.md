# CFL Condition and Time Step Restrictions

The Courant-Friedrichs-Lewy (CFL) condition provides a necessary stability constraint for explicit finite difference schemes. For option pricing, it dictates how small the time step must be relative to the spatial grid, and understanding it is essential for efficient numerical implementation.

---

## The CFL Principle

### Domain of Dependence

The CFL condition originates from a fundamental principle: the **numerical domain of dependence** must contain the **physical domain of dependence** of the PDE.

For a hyperbolic equation $u_t + c u_x = 0$ with wave speed $c > 0$, the value $u(x, t+\Delta t)$ depends on $u(x - c\Delta t, t)$. If the explicit scheme at node $j$ uses only nodes $j-1, j, j+1$ at time level $n$, then the numerical domain of dependence extends from $x_{j-1}$ to $x_{j+1}$. The physical characteristic through $(x_j, t_{n+1})$ reaches $x_j - c\Delta t$ at time $t_n$.

The CFL condition requires:

$$
c\Delta t \leq \Delta x
$$

so that the foot of the characteristic lies within $[x_{j-1}, x_{j+1}]$.

!!! info "CFL Condition (Advection)"
    For the advection equation $u_t + cu_x = 0$ with an explicit scheme using a three-point stencil:

    $$
    \boxed{\nu = \frac{|c|\Delta t}{\Delta x} \leq 1}
    $$

    The dimensionless ratio $\nu$ is called the **Courant number**.

---

## CFL for the Diffusion Equation

For the diffusion equation $u_\tau = D u_{xx}$, the explicit (forward Euler) scheme:

$$
u_j^{n+1} = u_j^n + \lambda(u_{j+1}^n - 2u_j^n + u_{j-1}^n)
$$

with $\lambda = D\Delta\tau / (\Delta x)^2$ is stable if and only if $\lambda \leq 1/2$.

### Positivity Interpretation

Rewrite the scheme as:

$$
u_j^{n+1} = \lambda \, u_{j-1}^n + (1 - 2\lambda) \, u_j^n + \lambda \, u_{j+1}^n
$$

This is a **convex combination** of neighboring values (and hence preserves the maximum principle) if and only if all coefficients are non-negative:

$$
\lambda \geq 0 \quad \text{and} \quad 1 - 2\lambda \geq 0
$$

The second condition gives:

$$
\boxed{\lambda = \frac{D\Delta\tau}{(\Delta x)^2} \leq \frac{1}{2}}
$$

!!! tip "Positivity and the CFL Condition"
    For parabolic equations, the CFL condition is equivalent to requiring **non-negative stencil coefficients**, which in turn guarantees the **discrete maximum principle**: the numerical solution cannot create new extrema.

---

## CFL for the Black-Scholes PDE

### In Original Coordinates

The Black-Scholes PDE in time-to-maturity form:

$$
\frac{\partial u}{\partial \tau} = \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} + rS\frac{\partial u}{\partial S} - ru
$$

Discretized with central differences on a uniform grid $S_j = j\Delta S$, the explicit scheme coefficients at node $j$ are:

$$
a_j = \frac{\Delta\tau}{2}(\sigma^2 j^2 - rj), \quad
b_j = 1 - \Delta\tau(\sigma^2 j^2 + r), \quad
c_j = \frac{\Delta\tau}{2}(\sigma^2 j^2 + rj)
$$

where $u_j^{n+1} = a_j u_{j-1}^n + b_j u_j^n + c_j u_{j+1}^n$.

**Positivity of $b_j$** requires:

$$
1 - \Delta\tau(\sigma^2 j^2 + r) \geq 0 \quad \Longrightarrow \quad \Delta\tau \leq \frac{1}{\sigma^2 j^2 + r}
$$

The binding constraint occurs at $j = M$ (where $S_M = S_{\max}$):

$$
\boxed{\Delta\tau \leq \frac{1}{\sigma^2 M^2 + r} = \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2 + r(\Delta S)^2}}
$$

For $r(\Delta S)^2 \ll \sigma^2 S_{\max}^2$, this simplifies to:

$$
\Delta\tau \lesssim \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}
$$

**Positivity of $a_j$** requires $\sigma^2 j^2 - rj \geq 0$, i.e., $j \geq r/\sigma^2$. For small $j$, $a_j$ can be negative, which is a separate issue related to the convection term (remedied by upwinding if needed).

### In Log-Price Coordinates

After the transformation $x = \ln S$, the PDE has constant coefficients:

$$
\frac{\partial u}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial u}{\partial x} - ru
$$

The diffusion CFL condition becomes:

$$
\boxed{\frac{\sigma^2 \Delta\tau}{2(\Delta x)^2} \leq \frac{1}{2} \quad \Longleftrightarrow \quad \Delta\tau \leq \frac{(\Delta x)^2}{\sigma^2}}
$$

This is **independent of $S_{\max}$**, a major advantage of log-price coordinates. The time step restriction depends only on $\sigma$ and $\Delta x$.

---

## Practical Time Step Calculations

### Example: European Call Option

Consider typical parameters: $K = 100$, $T = 1$, $\sigma = 0.3$, $r = 0.05$.

**In original coordinates** with $S_{\max} = 300$, $M = 200$ ($\Delta S = 1.5$):

$$
\Delta\tau \leq \frac{(1.5)^2}{(0.3)^2 \times (300)^2} = \frac{2.25}{8100} \approx 2.78 \times 10^{-4}
$$

Minimum time steps: $N \geq T / \Delta\tau \approx 3{,}600$.

**In log-price coordinates** with $\Delta x = 0.02$:

$$
\Delta\tau \leq \frac{(0.02)^2}{(0.3)^2} = \frac{4 \times 10^{-4}}{0.09} \approx 4.44 \times 10^{-3}
$$

Minimum time steps: $N \geq T / \Delta\tau \approx 225$.

### Comparison Table

| Coordinate | $\Delta\tau$ bound | Min time steps for $T=1$ |
|-----------|-------------------|-------------------------|
| Original ($S_{\max}=300$, $M=200$) | $2.78 \times 10^{-4}$ | 3,600 |
| Log-price ($\Delta x = 0.02$) | $4.44 \times 10^{-3}$ | 225 |
| Implicit (either) | No restriction | Choose for accuracy |

The log-price formulation reduces the required number of explicit time steps by an order of magnitude.

---

## Time Step Selection Strategies

### Strategy 1: CFL-Based (Explicit Schemes)

Set $\Delta\tau$ to satisfy the CFL condition with a safety factor:

$$
\Delta\tau = \alpha \cdot \Delta\tau_{\text{CFL}}, \quad \alpha \in [0.8, 0.95]
$$

The safety factor accounts for rounding and the approximate nature of frozen-coefficient analysis for variable-coefficient problems.

### Strategy 2: Accuracy-Matched (Implicit/Crank-Nicolson)

For unconditionally stable schemes, choose $\Delta\tau$ to match spatial and temporal accuracy.

**Crank-Nicolson** has error $O((\Delta\tau)^2 + (\Delta S)^2)$. Balancing these:

$$
(\Delta\tau)^2 \sim (\Delta S)^2 \quad \Longrightarrow \quad \Delta\tau \sim \Delta S
$$

For $M = 200$ spatial points and $S_{\max} = 300$: $\Delta S = 1.5$, so take $N \approx T/\Delta S \approx 1/1.5 \approx 1$ is too coarse. A practical rule is $N \approx M/2$ to $M$, giving $N \approx 100$ to $200$.

**Implicit (backward Euler)** has error $O(\Delta\tau + (\Delta S)^2)$. Matching:

$$
\Delta\tau \sim (\Delta S)^2 \quad \Longrightarrow \quad N \sim \frac{T}{(\Delta S)^2}
$$

This requires more time steps than Crank-Nicolson for the same accuracy.

### Strategy 3: Rannacher Start

When using Crank-Nicolson with non-smooth payoffs:

1. Take 2-4 implicit steps with $\Delta\tau_{\text{impl}}$ (small, possibly CFL-like)
2. Switch to Crank-Nicolson with larger $\Delta\tau_{\text{CN}}$

The implicit steps smooth the solution, allowing Crank-Nicolson to achieve its full second-order accuracy.

---

## CFL and Scheme Selection

The CFL condition is the primary reason **explicit schemes are rarely used** for Black-Scholes problems in practice.

| Scheme | CFL restriction | Typical $N$ ($M=200$) | Cost per step | Total cost |
|--------|----------------|----------------------|---------------|------------|
| Explicit | $\Delta\tau \leq C(\Delta S)^2$ | 3,600 | $O(M)$ | $O(M \cdot M^2) = O(M^3)$ |
| Implicit | None | 100-200 | $O(M)$ | $O(M^2)$ |
| Crank-Nicolson | None | 100-200 | $O(M)$ | $O(M^2)$ |

The explicit scheme has $O(M)$ cost per step, but the CFL restriction forces $N = O(M^2)$ time steps, giving **total cost $O(M^3)$**. Implicit and Crank-Nicolson use only $O(M)$ time steps (chosen for accuracy), yielding **total cost $O(M^2)$**.

!!! warning "Explicit Scheme Trap"
    Doubling the spatial resolution ($M \to 2M$) for an explicit scheme requires quadrupling the number of time steps ($N \to 4N$), increasing total work by a factor of 8. For implicit schemes, the work only increases by a factor of 4.

---

## Non-Negativity of Coefficients

Beyond the standard CFL condition, a stronger requirement for reliable option pricing is **non-negativity of all stencil coefficients**. This ensures:

1. **Discrete maximum principle**: No spurious oscillations
2. **Monotonicity**: Essential for convergence to the viscosity solution (see Barles-Souganidis theorem)
3. **Non-negative prices**: The numerical solution preserves the non-negativity of option values

For the explicit scheme in original coordinates, all three coefficients $a_j, b_j, c_j$ must be non-negative. The coefficient $a_j = \frac{\Delta\tau}{2}(\sigma^2 j^2 - rj)$ is negative for $j < r/\sigma^2$, which occurs at small $S$. This can be resolved by:

- Using upwind differencing for the first derivative at affected nodes
- Switching to log-price coordinates where coefficients are constant
- Using the implicit scheme, which maintains monotonicity unconditionally

---

## Summary

$$
\boxed{
\text{CFL condition: } \frac{D\Delta\tau}{(\Delta x)^2} \leq \frac{1}{2}
}
$$

| Aspect | Key Point |
|--------|-----------|
| **Origin** | Numerical domain must contain physical domain |
| **For Black-Scholes** | $\Delta\tau \leq (\Delta S)^2 / (\sigma^2 S_{\max}^2)$ |
| **Log-price advantage** | CFL independent of $S_{\max}$ |
| **Positivity link** | CFL equivalent to non-negative stencil coefficients |
| **Practical impact** | Explicit schemes require $N = O(M^2)$ steps |
| **Remedy** | Use implicit or Crank-Nicolson (unconditionally stable) |

The CFL condition is a necessary evil for explicit schemes. Its severity for the Black-Scholes PDE in original coordinates is the main motivation for using either implicit time-stepping or log-price coordinates in practice.
