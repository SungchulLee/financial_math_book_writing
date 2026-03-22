# Finite Difference Pricing with Local Volatility

Under the local volatility model, the Black-Scholes PDE retains its structure but the diffusion coefficient $\sigma(S, t)$ depends on both spot and time. This space-time dependence prevents closed-form solutions for most payoffs and necessitates numerical PDE methods. Finite difference methods (FDM) discretize the PDE on a grid and march backward in time from the terminal payoff to obtain present values. This section develops the FDM framework for local volatility, covering grid construction, explicit and implicit time-stepping schemes, the Crank-Nicolson method, and the practical considerations that arise when $\sigma(S, t)$ varies significantly across the computational domain.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Write the Black-Scholes PDE with a local volatility function $\sigma(S, t)$
    - Discretize the PDE using explicit, implicit, and Crank-Nicolson schemes
    - Analyze stability conditions and their dependence on the local volatility surface
    - Construct non-uniform grids adapted to the strike and volatility structure
    - Implement boundary conditions appropriate for local volatility pricing

## The Local Volatility PDE

### From SDE to PDE

Under the risk-neutral measure, the asset price follows:

$$
dS_t = (r - q) S_t \, dt + \sigma_{\text{loc}}(S_t, t) S_t \, dW_t^{\mathbb{Q}}
$$

By the Feynman-Kac theorem, the price $V(S, t)$ of a European contingent claim with payoff $\Phi(S_T)$ satisfies the **local volatility PDE**:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma_{\text{loc}}^2(S, t) S^2 \frac{\partial^2 V}{\partial S^2} + (r - q) S \frac{\partial V}{\partial S} - rV = 0
$$

with terminal condition $V(S, T) = \Phi(S)$.

This is identical to the Black-Scholes PDE except that the constant $\sigma$ is replaced by the function $\sigma_{\text{loc}}(S, t)$. The dependence on $(S, t)$ means the coefficients of the PDE vary across the grid, requiring careful treatment in the discretization.

### Log-Spot Transformation

Working directly in $S$-space produces non-constant coefficients even for Black-Scholes. The transformation $x = \ln S$ simplifies the structure. Setting $U(x, t) = V(e^x, t)$:

$$
\frac{\partial U}{\partial t} + \frac{1}{2}\sigma_{\text{loc}}^2(e^x, t) \frac{\partial^2 U}{\partial x^2} + \left(r - q - \frac{1}{2}\sigma_{\text{loc}}^2(e^x, t)\right) \frac{\partial U}{\partial x} - rU = 0
$$

Define the coefficients:

$$
a(x, t) = \frac{1}{2}\sigma_{\text{loc}}^2(e^x, t), \quad b(x, t) = r - q - a(x, t), \quad c = -r
$$

The PDE becomes:

$$
\frac{\partial U}{\partial t} + a(x, t) \frac{\partial^2 U}{\partial x^2} + b(x, t) \frac{\partial U}{\partial x} + cU = 0
$$

This form is preferred for numerical implementation because the diffusion and convection coefficients vary through $\sigma_{\text{loc}}$ but the spatial coordinate $x$ is unbounded and uniformly spaced in log-space.

## Grid Construction

### Spatial Grid

Choose a computational domain $[x_{\min}, x_{\max}]$ in log-spot space with $M + 1$ grid points:

$$
x_j = x_{\min} + j \Delta x, \quad j = 0, 1, \ldots, M, \quad \Delta x = \frac{x_{\max} - x_{\min}}{M}
$$

The domain boundaries should be far enough from the strike to avoid boundary effects. A common choice:

$$
x_{\min} = \ln S_0 - L\sigma_{\max}\sqrt{T}, \quad x_{\max} = \ln S_0 + L\sigma_{\max}\sqrt{T}
$$

where $\sigma_{\max} = \max_{S,t} \sigma_{\text{loc}}(S, t)$ and $L \geq 4$ ensures the boundaries are sufficiently far.

### Non-Uniform Grids

For accuracy near the strike $K$, a non-uniform grid concentrates points where the payoff has a kink. A common approach uses a **sinh-based** transformation:

$$
x_j = x_c + d \sinh\left(\frac{\xi_j - \xi_c}{\alpha}\right)
$$

where $x_c = \ln K$ is the center, $\xi_j$ is a uniform grid, and $\alpha$ controls the concentration. Smaller $\alpha$ packs more points near the strike.

!!! tip "Grid Sizing Rule of Thumb"
    For European options, $M = 200$--$500$ spatial points and $N = 100$--$500$ time steps typically provide four-digit accuracy. For barrier options under local volatility, grid requirements increase substantially due to the need to resolve the barrier level precisely.

### Time Grid

Divide $[0, T]$ into $N$ time steps:

$$
t^n = n \Delta t, \quad n = 0, 1, \ldots, N, \quad \Delta t = \frac{T}{N}
$$

Since the PDE is solved backward in time, we march from $t^N = T$ (where the terminal condition is known) to $t^0 = 0$.

Let $U_j^n$ denote the numerical approximation to $U(x_j, t^n)$.

## Explicit Scheme

### Discretization

The **explicit** (forward Euler in time, centered differences in space) scheme evaluates all spatial derivatives at the known time level $t^{n+1}$:

$$
\frac{U_j^n - U_j^{n+1}}{\Delta t} + a_j^{n+1} \frac{U_{j+1}^{n+1} - 2U_j^{n+1} + U_{j-1}^{n+1}}{(\Delta x)^2} + b_j^{n+1} \frac{U_{j+1}^{n+1} - U_{j-1}^{n+1}}{2\Delta x} + cU_j^{n+1} = 0
$$

where $a_j^{n+1} = a(x_j, t^{n+1})$ and $b_j^{n+1} = b(x_j, t^{n+1})$. Solving for $U_j^n$:

$$
U_j^n = \alpha_j^{n+1} U_{j-1}^{n+1} + \beta_j^{n+1} U_j^{n+1} + \gamma_j^{n+1} U_{j+1}^{n+1}
$$

where:

$$
\alpha_j = \Delta t \left(\frac{a_j}{(\Delta x)^2} - \frac{b_j}{2\Delta x}\right)
$$

$$
\beta_j = 1 - \Delta t \left(\frac{2a_j}{(\Delta x)^2} - c\right)
$$

$$
\gamma_j = \Delta t \left(\frac{a_j}{(\Delta x)^2} + \frac{b_j}{2\Delta x}\right)
$$

### Stability Condition

The explicit scheme is conditionally stable. The von Neumann stability analysis requires all coefficients $\alpha_j$, $\beta_j$, $\gamma_j$ to be non-negative. The binding constraint is typically $\beta_j \geq 0$:

$$
\Delta t \leq \frac{(\Delta x)^2}{2a_j + |c|(\Delta x)^2} = \frac{(\Delta x)^2}{\sigma_{\text{loc}}^2(e^{x_j}, t) + 2r(\Delta x)^2}
$$

For local volatility, this condition must hold at **every** grid point. The most restrictive point is where $\sigma_{\text{loc}}$ is largest:

$$
\Delta t \leq \frac{(\Delta x)^2}{\sigma_{\max}^2 + 2r(\Delta x)^2}
$$

When $\sigma_{\text{loc}}$ varies significantly (for example, from 10% to 80% across the grid), the stability constraint is dictated by the peak volatility region, making the explicit scheme expensive.

!!! warning "CFL Condition under Local Volatility"
    Unlike constant-volatility Black-Scholes where the CFL constraint is uniform, local volatility creates spatially varying stability requirements. A single high-volatility region (e.g., far OTM where $\sigma_{\text{loc}}$ can spike) forces small $\Delta t$ everywhere, even in low-volatility regions. This motivates implicit schemes.

## Implicit Scheme

### Discretization

The **fully implicit** (backward Euler) scheme evaluates spatial derivatives at the unknown time level $t^n$:

$$
\frac{U_j^n - U_j^{n+1}}{\Delta t} + a_j^n \frac{U_{j+1}^n - 2U_j^n + U_{j-1}^n}{(\Delta x)^2} + b_j^n \frac{U_{j+1}^n - U_{j-1}^n}{2\Delta x} + cU_j^n = 0
$$

Rearranging into matrix form:

$$
-\alpha_j^n U_{j-1}^n + (1 + \delta_j^n) U_j^n - \gamma_j^n U_{j+1}^n = U_j^{n+1}
$$

where:

$$
\alpha_j^n = \Delta t \left(\frac{a_j^n}{(\Delta x)^2} - \frac{b_j^n}{2\Delta x}\right)
$$

$$
\delta_j^n = \Delta t \left(\frac{2a_j^n}{(\Delta x)^2} - c\right)
$$

$$
\gamma_j^n = \Delta t \left(\frac{a_j^n}{(\Delta x)^2} + \frac{b_j^n}{2\Delta x}\right)
$$

### Tridiagonal System

The implicit scheme at each time step requires solving a tridiagonal linear system:

$$
\mathbf{A}^n \mathbf{U}^n = \mathbf{U}^{n+1} + \mathbf{d}^n
$$

where $\mathbf{A}^n$ is a tridiagonal matrix with entries depending on the local volatility at time $t^n$, and $\mathbf{d}^n$ incorporates boundary conditions. The system is solved efficiently by the **Thomas algorithm** (LU decomposition for tridiagonal matrices) in $O(M)$ operations.

**Key property:** The implicit scheme is **unconditionally stable** — no restriction on $\Delta t$ relative to $\Delta x$. However, it is only first-order accurate in time ($O(\Delta t)$).

### Coefficient Update at Each Time Step

A critical difference from constant-volatility FDM: the matrix $\mathbf{A}^n$ changes at every time step because $\sigma_{\text{loc}}(e^{x_j}, t^n)$ depends on $t$. The local volatility surface must be evaluated (or interpolated) at each grid point and time level, adding computational overhead compared to constant $\sigma$.

## Crank-Nicolson Scheme

### The Theta Method

The general **theta-scheme** combines explicit and implicit evaluations:

$$
\frac{U_j^n - U_j^{n+1}}{\Delta t} + \theta \mathcal{L}^n U_j^n + (1 - \theta)\mathcal{L}^{n+1} U_j^{n+1} = 0
$$

where $\mathcal{L}$ is the spatial differential operator:

$$
\mathcal{L}^n U_j^n = a_j^n \frac{U_{j+1}^n - 2U_j^n + U_{j-1}^n}{(\Delta x)^2} + b_j^n \frac{U_{j+1}^n - U_{j-1}^n}{2\Delta x} + c U_j^n
$$

The parameter $\theta$ controls the scheme:

- $\theta = 0$: Explicit (forward Euler)
- $\theta = 1$: Fully implicit (backward Euler)
- $\theta = 1/2$: **Crank-Nicolson** (trapezoidal rule)

### Crank-Nicolson Properties

Setting $\theta = 1/2$ gives second-order accuracy in both space and time: $O((\Delta x)^2 + (\Delta t)^2)$. The scheme is unconditionally stable but can produce **spurious oscillations** near discontinuities in the terminal condition (e.g., the digital option payoff or the kink in vanilla call/put payoffs).

The tridiagonal system for Crank-Nicolson is:

$$
-\frac{\theta}{2}\alpha_j^n U_{j-1}^n + \left(1 + \frac{\theta}{2}\delta_j^n\right) U_j^n - \frac{\theta}{2}\gamma_j^n U_{j+1}^n = \frac{1-\theta}{2}\alpha_j^{n+1} U_{j-1}^{n+1} + \left(1 - \frac{1-\theta}{2}\delta_j^{n+1}\right) U_j^{n+1} + \frac{1-\theta}{2}\gamma_j^{n+1} U_{j+1}^{n+1}
$$

with $\theta = 1/2$ for Crank-Nicolson.

!!! tip "Rannacher Time-Stepping"
    To suppress Crank-Nicolson oscillations near payoff discontinuities, apply 2--4 fully implicit (backward Euler) steps at the start, then switch to Crank-Nicolson for the remaining steps. This **Rannacher smoothing** eliminates the oscillations while preserving second-order accuracy away from the terminal condition.

## Boundary Conditions

### Far-Field Boundaries

At the domain boundaries $x_{\min}$ and $x_{\max}$ (equivalently, $S_{\min} = e^{x_{\min}}$ and $S_{\max} = e^{x_{\max}}$), boundary conditions are required.

**For a European call:**

- At $S_{\min} \approx 0$: $V(S_{\min}, t) \approx 0$ (Dirichlet)
- At $S_{\max} \gg K$: $V(S_{\max}, t) \approx S_{\max} e^{-q(T-t)} - K e^{-r(T-t)}$ (asymptotic value)

**For a European put:**

- At $S_{\min} \approx 0$: $V(S_{\min}, t) \approx K e^{-r(T-t)}$
- At $S_{\max} \gg K$: $V(S_{\max}, t) \approx 0$

**Alternative: Linearity condition.** At the far boundaries, the option value becomes nearly linear in $S$, so a Neumann-type condition $\partial^2 V / \partial S^2 = 0$ (equivalently, $\partial^2 U / \partial x^2 = 0$ in log-space) avoids specifying exact boundary values.

### Barrier Options

For barrier options, the barrier level $B$ must lie exactly on a grid line. At the barrier:

$$
V(B, t) = \text{rebate}(t) \quad \text{(knock-out)}
$$

Under local volatility, the barrier requires extra grid refinement because $\sigma_{\text{loc}}(B, t)$ may differ substantially from $\sigma_{\text{loc}}(S_0, t)$.

## Implementation Considerations

### Evaluating the Local Volatility Surface

At each grid point $(x_j, t^n)$, the FDM scheme requires $\sigma_{\text{loc}}(e^{x_j}, t^n)$. The local volatility surface is typically available on a separate grid (from Dupire's formula applied to market data). Interpolation is needed:

1. **Bilinear interpolation:** Simple but only $C^0$, which can introduce oscillations in the FDM coefficients
2. **Bicubic spline interpolation:** Smooth ($C^2$), preferred for stable FDM solutions
3. **Caching:** Pre-compute and store $\sigma_{\text{loc}}$ values on the FDM grid before the time-stepping loop

### Greeks Computation

Finite differences on the grid directly yield the Greeks:

$$
\Delta = \frac{\partial V}{\partial S} \approx \frac{U_{j+1}^0 - U_{j-1}^0}{2\Delta x \cdot e^{x_j}}
$$

$$
\Gamma = \frac{\partial^2 V}{\partial S^2} \approx \frac{1}{e^{2x_j}}\left(\frac{U_{j+1}^0 - 2U_j^0 + U_{j-1}^0}{(\Delta x)^2} - \frac{U_{j+1}^0 - U_{j-1}^0}{2\Delta x}\right)
$$

$$
\Theta = -\frac{U_j^0 - U_j^1}{\Delta t}
$$

Vega under local volatility requires a separate computation: bump the entire $\sigma_{\text{loc}}$ surface and re-solve the PDE.

### Accuracy and Convergence

**Theorem 13.5.1** (Convergence of FDM for Local Volatility PDE)
If $\sigma_{\text{loc}}(S, t)$ is bounded, Lipschitz continuous in $S$, and piecewise continuous in $t$, then:

- The explicit scheme converges at rate $O(\Delta t + (\Delta x)^2)$ under the CFL condition
- The implicit scheme converges at rate $O(\Delta t + (\Delta x)^2)$ unconditionally
- The Crank-Nicolson scheme converges at rate $O((\Delta t)^2 + (\Delta x)^2)$ unconditionally

for payoffs $\Phi \in C^0$ (Lipschitz continuous). For discontinuous payoffs (e.g., digitals), Rannacher smoothing restores second-order convergence for Crank-Nicolson.

!!! example "Convergence Study"
    Consider a European call with $K = 100$, $T = 1$, $r = 5\%$, $q = 0\%$, and a local volatility surface $\sigma_{\text{loc}}(S, t) = 0.2 + 0.1 e^{-0.01(S-100)^2}$ (a bump centered at $S = 100$). Using Crank-Nicolson with Rannacher smoothing:

    | Grid ($M \times N$) | Price | Error | Ratio |
    |---------------------|-------|-------|-------|
    | $100 \times 50$ | 10.4537 | $3.2 \times 10^{-2}$ | — |
    | $200 \times 100$ | 10.4219 | $8.1 \times 10^{-3}$ | 3.95 |
    | $400 \times 200$ | 10.4139 | $2.0 \times 10^{-3}$ | 4.05 |
    | $800 \times 400$ | 10.4119 | $5.0 \times 10^{-4}$ | 4.00 |

    The ratio approaches 4, confirming second-order convergence $O((\Delta x)^2 + (\Delta t)^2)$ when both $\Delta x$ and $\Delta t$ are halved simultaneously.

## Comparison with Constant Volatility FDM

The main differences when implementing FDM under local volatility versus constant volatility are:

| Aspect | Constant $\sigma$ | Local Volatility $\sigma(S, t)$ |
|--------|-------------------|-------------------------------|
| PDE coefficients | Fixed | Vary with $(S, t)$ |
| Matrix assembly | Once | Every time step |
| CFL condition (explicit) | Uniform | Varies across grid |
| Surface interpolation | Not needed | Required at each node |
| Vega computation | Single bump-and-reprice | Full surface perturbation |
| Grid design | Standard | Adapted to $\sigma_{\text{loc}}$ structure |

The additional cost per time step is modest (matrix reassembly and surface interpolation are $O(M)$), so the total cost remains $O(MN)$, the same asymptotic complexity as constant-volatility FDM. The practical overhead is typically a factor of 2--3 in wall-clock time.

## Summary

Finite difference methods provide a robust framework for pricing under local volatility:

1. The **local volatility PDE** is the standard Black-Scholes PDE with $\sigma$ replaced by $\sigma_{\text{loc}}(S, t)$, yielding space-time-varying coefficients
2. The **log-spot transformation** $x = \ln S$ simplifies the PDE structure and enables uniform grid spacing
3. **Explicit schemes** are straightforward but suffer from spatially varying CFL constraints dictated by peak volatility
4. **Implicit schemes** are unconditionally stable and handle volatile local volatility surfaces without time step restrictions
5. **Crank-Nicolson** achieves second-order accuracy in both space and time, with Rannacher smoothing needed near payoff discontinuities
6. **Grid design** and **surface interpolation** are the two principal implementation challenges specific to local volatility FDM
