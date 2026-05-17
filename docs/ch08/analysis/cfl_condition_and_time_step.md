# CFL Condition and Time Step Restrictions

An explicit scheme can only see a few neighboring nodes when computing the next time level. If the true PDE propagates information faster than that stencil can reach -- a characteristic crosses more than one cell per time step, or diffusion spreads beyond the three-point window -- the scheme is computing the next value from the wrong source points, and errors compound exponentially. The **CFL condition** is the precise inequality ($c\Delta t\le\Delta x$ for advection, $\sigma^2\Delta t\le(\Delta x)^2$ for diffusion) that forbids this overshoot and fixes the maximum stable time step for any explicit scheme.

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

Recall (see [§ Von Neumann Stability Analysis — Explicit Scheme](von_neumann_stability_analysis.md#explicit-scheme-forward-euler)): for $u_\tau = D u_{xx}$ with explicit time stepping and $\lambda = D\Delta\tau/(\Delta x)^2$, the amplification factor $g = 1 - 4\lambda\sin^2(\xi/2)$ gives stability iff $\lambda \leq 1/2$.

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

---

## Exercises

**Exercise 1.** For the advection equation $u_t + cu_x = 0$ with $c = 2$, $\Delta x = 0.1$, and $\Delta t = 0.04$, compute the Courant number $\nu = |c|\Delta t/\Delta x$. Is the CFL condition satisfied? What is the maximum allowable $\Delta t$?

??? success "Solution to Exercise 1"
    The Courant number is:

    $$
    \nu = \frac{|c|\Delta t}{\Delta x} = \frac{2 \times 0.04}{0.1} = \frac{0.08}{0.1} = 0.8
    $$

    Since $\nu = 0.8 \leq 1$, the CFL condition **is satisfied**.

    The maximum allowable $\Delta t$ is obtained by setting $\nu = 1$:

    $$
    \Delta t_{\max} = \frac{\Delta x}{|c|} = \frac{0.1}{2} = 0.05
    $$

---

**Exercise 2.** For the Black-Scholes PDE in original coordinates with $\sigma = 0.25$, $S_{\max} = 400$, and $M = 200$ ($\Delta S = 2$), compute the CFL restriction on $\Delta\tau$. How many time steps are needed for $T = 1$? Repeat the calculation in log-price coordinates with the same number of spatial points and compare.

??? success "Solution to Exercise 2"
    **In original coordinates** with $\sigma = 0.25$, $S_{\max} = 400$, $M = 200$, so $\Delta S = S_{\max}/M = 400/200 = 2$:

    $$
    \Delta\tau \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2} = \frac{(2)^2}{(0.25)^2 \times (400)^2} = \frac{4}{0.0625 \times 160{,}000} = \frac{4}{10{,}000} = 4 \times 10^{-4}
    $$

    Time steps needed for $T = 1$:

    $$
    N \geq \frac{1}{4 \times 10^{-4}} = 2{,}500
    $$

    **In log-price coordinates** with the same $M = 200$ spatial points. The log-price range is $[x_{\min}, x_{\max}] = [\ln(S_{\min}), \ln(S_{\max})]$. Taking $S_{\min} \approx S_{\max}e^{-x_{\text{range}}}$ and using a comparable range, we get $\Delta x = (\ln S_{\max} - \ln S_{\min})/M$. For a typical range $\ln(400) - \ln(0.01) \approx 10.6$, we get $\Delta x \approx 10.6/200 = 0.053$. The CFL condition is:

    $$
    \Delta\tau \leq \frac{(\Delta x)^2}{\sigma^2} = \frac{(0.053)^2}{(0.25)^2} = \frac{2.81 \times 10^{-3}}{0.0625} \approx 0.045
    $$

    Time steps needed:

    $$
    N \geq \frac{1}{0.045} \approx 23
    $$

    The log-price formulation requires roughly 100 times fewer time steps (23 vs. 2,500), because the CFL bound is independent of $S_{\max}$.

---

**Exercise 3.** The explicit scheme coefficients for the Black-Scholes PDE are $a_j = \frac{\Delta\tau}{2}(\sigma^2 j^2 - rj)$, $b_j = 1 - \Delta\tau(\sigma^2 j^2 + r)$, $c_j = \frac{\Delta\tau}{2}(\sigma^2 j^2 + rj)$. Rewrite the scheme as a convex combination of neighboring values and show that non-negativity of all three coefficients is equivalent to the CFL condition plus $j \geq r/\sigma^2$.

??? success "Solution to Exercise 3"
    The explicit scheme is $u_j^{n+1} = a_j u_{j-1}^n + b_j u_j^n + c_j u_{j+1}^n$ with:

    $$
    a_j = \frac{\Delta\tau}{2}(\sigma^2 j^2 - rj), \quad b_j = 1 - \Delta\tau(\sigma^2 j^2 + r), \quad c_j = \frac{\Delta\tau}{2}(\sigma^2 j^2 + rj)
    $$

    Note that $a_j + b_j + c_j = 1 - r\Delta\tau$. After accounting for the $-ru$ term (which gives a factor $(1-r\Delta\tau)$ per step), the scheme is a convex combination if all three coefficients are non-negative.

    **Non-negativity of $c_j$**: Since $c_j = \frac{\Delta\tau}{2}(\sigma^2 j^2 + rj)$ and $j \geq 1$, $r > 0$, $\sigma > 0$, we always have $c_j > 0$.

    **Non-negativity of $a_j$**: We need $\sigma^2 j^2 - rj \geq 0$, i.e., $j(\sigma^2 j - r) \geq 0$. For $j \geq 1$, this requires $j \geq r/\sigma^2$.

    **Non-negativity of $b_j$**: We need $1 - \Delta\tau(\sigma^2 j^2 + r) \geq 0$, i.e.:

    $$
    \Delta\tau \leq \frac{1}{\sigma^2 j^2 + r}
    $$

    The most restrictive constraint occurs at $j = M$ (the largest node):

    $$
    \Delta\tau \leq \frac{1}{\sigma^2 M^2 + r}
    $$

    This is precisely the CFL condition. Thus, non-negativity of all three coefficients requires both the CFL condition ($b_j \geq 0$ for all $j$) and $j \geq r/\sigma^2$ ($a_j \geq 0$). The latter condition means that for small $j$ (near $S = 0$), the coefficient $a_j$ can be negative regardless of $\Delta\tau$. This is a convection-related issue, not a CFL issue, and is remedied by upwind differencing at affected nodes.

---

**Exercise 4.** For the accuracy-matched time step strategy with Crank-Nicolson, the error is $O((\Delta\tau)^2 + (\Delta S)^2)$. If $M = 200$ and $S_{\max} = 300$ (so $\Delta S = 1.5$), what value of $N$ balances the temporal and spatial errors? Compare this to the CFL-required $N$ for the explicit scheme.

??? success "Solution to Exercise 4"
    With $M = 200$ and $S_{\max} = 300$, the spatial step is $\Delta S = 300/200 = 1.5$.

    For Crank-Nicolson, the error is $O((\Delta\tau)^2 + (\Delta S)^2)$. Balancing temporal and spatial errors:

    $$
    (\Delta\tau)^2 \sim (\Delta S)^2 \implies \Delta\tau \sim \Delta S = 1.5
    $$

    This gives $N = T/\Delta\tau = 1/1.5 \approx 1$, which is unrealistically coarse. A more practical interpretation is that for a given target accuracy $\epsilon$, we need $(\Delta S)^2 \sim \epsilon$ and $(\Delta\tau)^2 \sim \epsilon$. With $\Delta S = 1.5$, $(\Delta S)^2 = 2.25$, so we want $(\Delta\tau)^2 \approx 2.25$, giving $\Delta\tau \approx 1.5$ and $N \approx 1$.

    In practice, one typically takes $N \sim M$, so $N \approx 200$ with $\Delta\tau = 1/200 = 0.005$. This ensures both errors are of comparable magnitude at fine resolution.

    **Comparison to explicit CFL**: The explicit scheme requires:

    $$
    \Delta\tau \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}
    $$

    With $\sigma = 0.3$: $\Delta\tau \leq (1.5)^2 / ((0.3)^2 \times (300)^2) = 2.25/8100 \approx 2.78 \times 10^{-4}$, requiring $N \geq 3{,}600$. Crank-Nicolson needs only about 200 time steps for comparable accuracy, a factor of 18 fewer.

---

**Exercise 5.** Explain the "explicit scheme trap": why does doubling the spatial resolution ($M \to 2M$) increase the total computational cost of the explicit scheme by a factor of 8, while the implicit scheme's cost only increases by a factor of 4?

??? success "Solution to Exercise 5"
    **Why work scales as $8\times$ for explicit**: Let the original grid have $M$ spatial points and $N$ time steps. The CFL condition requires $N = O(M^2)$ since $\Delta\tau \leq C(\Delta S)^2$ and $\Delta S = S_{\max}/M$. The cost per time step is $O(M)$ (one pass through the grid), so total cost is $O(M \cdot N) = O(M \cdot M^2) = O(M^3)$.

    When we double $M \to 2M$:

    - $\Delta S$ is halved, so the CFL condition forces $\Delta\tau \to \Delta\tau/4$ (since $\Delta\tau \propto (\Delta S)^2$)
    - The number of time steps becomes $4N$
    - The cost per step doubles to $O(2M)$
    - Total cost: $O(2M \cdot 4N) = 8 \cdot O(MN)$

    Hence doubling spatial resolution increases work by a factor of 8.

    **Why work scales as $4\times$ for implicit**: The implicit scheme is unconditionally stable, so $N$ is chosen for accuracy, not stability. With accuracy-matched time stepping, $N \sim M$ (or $N$ is held fixed). Cost per step is $O(M)$ (tridiagonal solve). Total cost: $O(M \cdot N) = O(M^2)$.

    When $M \to 2M$:

    - $N \to 2N$ (to maintain accuracy matching)
    - Cost per step: $O(2M)$
    - Total cost: $O(2M \cdot 2N) = 4 \cdot O(MN)$

    Hence doubling spatial resolution increases work by a factor of 4.

---

**Exercise 6.** The Rannacher start strategy uses 2-4 implicit steps followed by Crank-Nicolson. If the implicit steps use the same $\Delta\tau$ as the Crank-Nicolson steps, what fraction of the total computation time is spent on implicit steps when $N = 200$? Does this overhead significantly affect efficiency?

??? success "Solution to Exercise 6"
    With $N = 200$ total time steps and 4 implicit (Rannacher) steps at the start, followed by 196 Crank-Nicolson steps:

    The fraction of steps that are implicit is:

    $$
    \frac{4}{200} = 0.02 = 2\%
    $$

    Both the implicit and Crank-Nicolson steps require solving a tridiagonal system at each step, which has cost $O(M)$. The per-step cost is essentially the same for both methods (the only difference is the right-hand side assembly, which is trivial). Therefore, the implicit steps account for approximately 2% of the total computation time.

    This overhead is negligible and does not significantly affect efficiency. The benefit — restoring smooth second-order convergence for non-smooth payoffs — far outweighs the cost. Even with the most conservative choice of 4 implicit half-steps (where each Crank-Nicolson step is replaced by two implicit half-steps), the overhead would be $8/204 \approx 4\%$, still negligible.
