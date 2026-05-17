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

Recall (see [§ Black-Scholes PDE](../../ch06/index.md)): under the risk-neutral measure with local-volatility SDE $dS_t = (r-q)S_t\,dt + \sigma_{\text{loc}}(S_t,t)S_t\,dW_t^{\mathbb{Q}}$, the Feynman-Kac theorem gives the **local volatility PDE**

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma_{\text{loc}}^2(S, t) S^2 \frac{\partial^2 V}{\partial S^2} + (r - q) S \frac{\partial V}{\partial S} - rV = 0
$$

with terminal condition $V(S, T) = \Phi(S)$. The dependence on $(S, t)$ means the coefficients of the PDE vary across the grid, requiring careful treatment in the discretization.

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

Recall (see [§ FDM](../../ch08/fdm/boundary_and_terminal_conditions.md)): the explicit scheme is conditionally stable via von Neumann analysis requiring non-negativity of all coefficients $\alpha_j, \beta_j, \gamma_j$. Specializing the CFL bound to local volatility, the binding constraint is

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

Recall (see [§ FDM](../../ch08/fdm/boundary_and_terminal_conditions.md)): the general **theta-scheme** combines explicit and implicit evaluations of the spatial operator $\mathcal{L}$, with $\theta = 0$ giving forward Euler, $\theta = 1$ backward Euler, and $\theta = 1/2$ **Crank-Nicolson** (trapezoidal rule). Under local volatility the operator $\mathcal{L}^n$ uses time-dependent coefficients $a_j^n = \tfrac{1}{2}\sigma_{\text{loc}}^2(e^{x_j}, t^n)$, $b_j^n = r - q - a_j^n$.

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

---

## Exercises

**Exercise 1.** Starting from the local volatility PDE in $S$-space, perform the log-spot transformation $x = \ln S$ and verify that the PDE coefficients are:

$$
a(x, t) = \frac{1}{2}\sigma_{\text{loc}}^2(e^x, t), \quad b(x, t) = r - q - a(x, t), \quad c = -r
$$

Show each step of the chain rule computation explicitly.

??? success "Solution to Exercise 1"
    We start with the local volatility PDE in $S$-space:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma_{\text{loc}}^2(S, t) S^2 \frac{\partial^2 V}{\partial S^2} + (r - q) S \frac{\partial V}{\partial S} - rV = 0
    $$

    Set $x = \ln S$, so $S = e^x$, and define $U(x, t) = V(e^x, t)$.

    **First derivative.** By the chain rule with $\frac{dx}{dS} = \frac{1}{S}$:

    $$
    \frac{\partial V}{\partial S} = \frac{\partial U}{\partial x}\frac{dx}{dS} = \frac{1}{S}\frac{\partial U}{\partial x}
    $$

    **Second derivative.** Differentiating again:

    $$
    \frac{\partial^2 V}{\partial S^2} = \frac{\partial}{\partial S}\left(\frac{1}{S}\frac{\partial U}{\partial x}\right) = -\frac{1}{S^2}\frac{\partial U}{\partial x} + \frac{1}{S}\frac{\partial}{\partial S}\left(\frac{\partial U}{\partial x}\right)
    $$

    For the second term, apply the chain rule again:

    $$
    \frac{\partial}{\partial S}\left(\frac{\partial U}{\partial x}\right) = \frac{1}{S}\frac{\partial^2 U}{\partial x^2}
    $$

    Therefore:

    $$
    \frac{\partial^2 V}{\partial S^2} = \frac{1}{S^2}\left(\frac{\partial^2 U}{\partial x^2} - \frac{\partial U}{\partial x}\right)
    $$

    **Time derivative.** Since the transformation is purely spatial, $\frac{\partial V}{\partial t} = \frac{\partial U}{\partial t}$.

    **Substitution.** Inserting into the PDE:

    $$
    \frac{\partial U}{\partial t} + \frac{1}{2}\sigma_{\text{loc}}^2 S^2 \cdot \frac{1}{S^2}\left(\frac{\partial^2 U}{\partial x^2} - \frac{\partial U}{\partial x}\right) + (r-q)S \cdot \frac{1}{S}\frac{\partial U}{\partial x} - rU = 0
    $$

    Simplifying:

    $$
    \frac{\partial U}{\partial t} + \frac{1}{2}\sigma_{\text{loc}}^2(e^x, t)\frac{\partial^2 U}{\partial x^2} + \left(r - q - \frac{1}{2}\sigma_{\text{loc}}^2(e^x, t)\right)\frac{\partial U}{\partial x} - rU = 0
    $$

    Reading off the coefficients:

    $$
    a(x,t) = \frac{1}{2}\sigma_{\text{loc}}^2(e^x, t), \quad b(x,t) = r - q - a(x,t), \quad c = -r
    $$

    which confirms the stated result.

---

**Exercise 2.** Consider a local volatility surface $\sigma_{\text{loc}}(S, t) = 0.3$ for $S < 100$ and $\sigma_{\text{loc}}(S, t) = 0.15$ for $S \geq 100$. Using a uniform grid in log-space with $\Delta x = 0.01$, compute the explicit scheme CFL time step constraint $\Delta t_{\max}$ at both $S = 80$ and $S = 120$. Which region dictates the global stability constraint?

??? success "Solution to Exercise 2"
    The CFL stability condition for the explicit scheme is:

    $$
    \Delta t \leq \frac{(\Delta x)^2}{\sigma_{\text{loc}}^2(e^{x_j}, t) + 2r(\Delta x)^2}
    $$

    With $\Delta x = 0.01$ and assuming a small $r$ (the term $2r(\Delta x)^2$ is negligible since $2r(0.01)^2 \ll \sigma^2$ for any reasonable $r$), the constraint simplifies to approximately:

    $$
    \Delta t_{\max} \approx \frac{(\Delta x)^2}{\sigma_{\text{loc}}^2}
    $$

    **At $S = 80$ (where $\sigma_{\text{loc}} = 0.3$):**

    $$
    \Delta t_{\max}(S=80) \approx \frac{(0.01)^2}{(0.3)^2} = \frac{10^{-4}}{0.09} \approx 1.11 \times 10^{-3}
    $$

    **At $S = 120$ (where $\sigma_{\text{loc}} = 0.15$):**

    $$
    \Delta t_{\max}(S=120) \approx \frac{(0.01)^2}{(0.15)^2} = \frac{10^{-4}}{0.0225} \approx 4.44 \times 10^{-3}
    $$

    The region $S < 100$ with $\sigma_{\text{loc}} = 0.3$ dictates the global stability constraint, since it produces the smaller $\Delta t_{\max}$. The global time step must satisfy $\Delta t \leq 1.11 \times 10^{-3}$, meaning the high-volatility region forces the entire grid to use approximately four times as many time steps as the low-volatility region would require on its own.

---

**Exercise 3.** Write out the tridiagonal matrix $\mathbf{A}^n$ for the fully implicit scheme on a grid with $M = 4$ interior points. Specify all entries in terms of $\alpha_j^n$, $\delta_j^n$, and $\gamma_j^n$. What boundary condition modifications are needed in the first and last rows for a European call?

??? success "Solution to Exercise 3"
    For $M = 4$ interior points ($j = 1, 2, 3, 4$), the fully implicit scheme at each time step requires solving:

    $$
    -\alpha_j^n U_{j-1}^n + (1 + \delta_j^n) U_j^n - \gamma_j^n U_{j+1}^n = U_j^{n+1}
    $$

    The tridiagonal matrix $\mathbf{A}^n$ is:

    $$
    \mathbf{A}^n = \begin{pmatrix} 1+\delta_1^n & -\gamma_1^n & 0 & 0 \\ -\alpha_2^n & 1+\delta_2^n & -\gamma_2^n & 0 \\ 0 & -\alpha_3^n & 1+\delta_3^n & -\gamma_3^n \\ 0 & 0 & -\alpha_4^n & 1+\delta_4^n \end{pmatrix}
    $$

    The system is $\mathbf{A}^n \mathbf{U}^n = \mathbf{U}^{n+1} + \mathbf{d}^n$, where $\mathbf{d}^n$ incorporates boundary conditions.

    **Boundary modifications for a European call:**

    - At the lower boundary ($j = 0$, where $S_{\min} \approx 0$): the Dirichlet condition $U_0^n \approx 0$ means the term $\alpha_1^n U_0^n = 0$, so no modification is needed in the first row — the boundary term vanishes.
    - At the upper boundary ($j = 5$, where $S_{\max} \gg K$): the condition $U_5^n = S_{\max}e^{-q(T-t^n)} - Ke^{-r(T-t^n)}$ is known. The term $\gamma_4^n U_5^n$ must be moved to the right-hand side, so the boundary correction vector has $d_4^n = \gamma_4^n U_5^n$ and all other entries zero.

---

**Exercise 4.** Explain why Rannacher time-stepping (2--4 initial fully implicit steps followed by Crank-Nicolson) eliminates spurious oscillations near payoff discontinuities while preserving second-order convergence. What property of the fully implicit scheme causes it to damp oscillations, and why does switching to Crank-Nicolson after the initial steps not reintroduce them?

??? success "Solution to Exercise 4"
    **Why Rannacher smoothing works:**

    The Crank-Nicolson scheme has second-order accuracy $O((\Delta t)^2 + (\Delta x)^2)$ but is only weakly $L$-stable — it does not fully damp high-frequency components in the solution. When the terminal condition has a discontinuity (digital payoff) or a kink (call/put payoff), the initial data contains high-frequency Fourier modes. Crank-Nicolson's trapezoidal time stepping assigns an amplification factor close to $-1$ for the highest-frequency modes, causing them to oscillate rather than decay. These oscillations manifest as spurious wiggles near the discontinuity.

    **The fully implicit scheme** (backward Euler) is $L$-stable: its amplification factor for high-frequency modes is close to zero. This means it aggressively damps all high-frequency components within just a few time steps. After 2--4 implicit steps, the oscillatory modes introduced by the non-smooth terminal condition have been reduced to negligible levels, and the remaining solution is smooth.

    **Switching to Crank-Nicolson does not reintroduce oscillations** because the oscillations originate from the non-smooth terminal data. Once the implicit steps have smoothed the solution, the data at subsequent time levels is smooth and does not excite new high-frequency modes. Crank-Nicolson then operates on smooth data, where it achieves its full second-order accuracy. The few initial implicit steps ($O(1)$ in number) contribute only $O(\Delta t)$ total error, which does not degrade the overall $O((\Delta t)^2)$ convergence rate.

---

**Exercise 5.** Derive the finite difference formulas for delta and gamma in the log-spot coordinate $x = \ln S$. Starting from:

$$
\Delta = \frac{\partial V}{\partial S} = \frac{1}{S}\frac{\partial U}{\partial x}
$$

show that the centered difference approximation yields:

$$
\Delta \approx \frac{U_{j+1}^0 - U_{j-1}^0}{2\Delta x \cdot e^{x_j}}
$$

Then derive the corresponding formula for $\Gamma = \partial^2 V / \partial S^2$ in terms of $U$ and $x$.

??? success "Solution to Exercise 5"
    Starting from $V(S, t) = U(\ln S, t)$, differentiate with respect to $S$:

    $$
    \frac{\partial V}{\partial S} = \frac{\partial U}{\partial x}\frac{dx}{dS} = \frac{1}{S}\frac{\partial U}{\partial x}
    $$

    So $\Delta = \frac{1}{S}\frac{\partial U}{\partial x}$. Using a centered difference for $\partial U / \partial x$ at the final time level ($n = 0$):

    $$
    \frac{\partial U}{\partial x}\bigg|_{x_j} \approx \frac{U_{j+1}^0 - U_{j-1}^0}{2\Delta x}
    $$

    Therefore:

    $$
    \Delta \approx \frac{U_{j+1}^0 - U_{j-1}^0}{2\Delta x \cdot e^{x_j}}
    $$

    since $S = e^{x_j}$.

    For gamma, differentiate delta with respect to $S$:

    $$
    \Gamma = \frac{\partial^2 V}{\partial S^2} = \frac{\partial}{\partial S}\left(\frac{1}{S}\frac{\partial U}{\partial x}\right) = -\frac{1}{S^2}\frac{\partial U}{\partial x} + \frac{1}{S^2}\frac{\partial^2 U}{\partial x^2} = \frac{1}{S^2}\left(\frac{\partial^2 U}{\partial x^2} - \frac{\partial U}{\partial x}\right)
    $$

    Substituting centered finite differences:

    $$
    \frac{\partial^2 U}{\partial x^2}\bigg|_{x_j} \approx \frac{U_{j+1}^0 - 2U_j^0 + U_{j-1}^0}{(\Delta x)^2}
    $$

    $$
    \frac{\partial U}{\partial x}\bigg|_{x_j} \approx \frac{U_{j+1}^0 - U_{j-1}^0}{2\Delta x}
    $$

    Therefore:

    $$
    \Gamma \approx \frac{1}{e^{2x_j}}\left(\frac{U_{j+1}^0 - 2U_j^0 + U_{j-1}^0}{(\Delta x)^2} - \frac{U_{j+1}^0 - U_{j-1}^0}{2\Delta x}\right)
    $$

---

**Exercise 6.** A convergence study for a European put under local volatility shows prices of 5.4321, 5.4189, 5.4156, and 5.4148 on grids of $100 \times 50$, $200 \times 100$, $400 \times 200$, and $800 \times 400$ (spatial $\times$ temporal). Compute the Richardson ratios and determine the observed order of convergence. Estimate the extrapolated exact price.

??? success "Solution to Exercise 6"
    The prices on successive grids are: $P_1 = 5.4321$, $P_2 = 5.4189$, $P_3 = 5.4156$, $P_4 = 5.4148$.

    **Successive differences:**

    $$
    P_1 - P_2 = 0.0132, \quad P_2 - P_3 = 0.0033, \quad P_3 - P_4 = 0.0008
    $$

    **Richardson ratios** (ratio of consecutive differences):

    $$
    R_1 = \frac{P_1 - P_2}{P_2 - P_3} = \frac{0.0132}{0.0033} = 4.00
    $$

    $$
    R_2 = \frac{P_2 - P_3}{P_3 - P_4} = \frac{0.0033}{0.0008} = 4.125
    $$

    Both ratios are approximately 4, which indicates **second-order convergence**. When both $\Delta x$ and $\Delta t$ are halved simultaneously, the error scales as $O((\Delta x)^2 + (\Delta t)^2)$, and the ratio of errors on successive grids is $2^2 = 4$.

    **Richardson extrapolation** using the two finest grids:

    $$
    P^* \approx P_4 + \frac{P_4 - P_3}{4 - 1} = 5.4148 + \frac{-0.0008}{3} \approx 5.4148 - 0.0003 = 5.4145
    $$

    The extrapolated exact price is approximately $5.4145$.

---

**Exercise 7.** For the sinh-based non-uniform grid $x_j = x_c + d \sinh((\xi_j - \xi_c)/\alpha)$, explain how the parameter $\alpha$ controls the grid concentration. If you need the grid spacing at the center $x_c$ to be approximately $\Delta x_{\text{center}} = 0.002$ and the grid spans $[-2, 2]$ in log-space with $M = 200$ points, estimate an appropriate value of $\alpha$.

??? success "Solution to Exercise 7"
    The sinh-based grid is $x_j = x_c + d\sinh((\xi_j - \xi_c)/\alpha)$, where $\xi_j$ is a uniform grid.

    **How $\alpha$ controls concentration:** The local grid spacing in $x$ is:

    $$
    \Delta x_j = \frac{dx}{d\xi}\Delta\xi = \frac{d}{\alpha}\cosh\left(\frac{\xi_j - \xi_c}{\alpha}\right)\Delta\xi
    $$

    At the center ($\xi_j = \xi_c$), $\cosh(0) = 1$, so $\Delta x_{\text{center}} = (d/\alpha)\Delta\xi$. Away from the center, $\cosh$ grows exponentially, so the grid spacing increases. A smaller $\alpha$ makes $\cosh$ grow faster, concentrating more points near the center and spacing them further apart in the wings. A larger $\alpha$ produces a more uniform grid.

    **Estimating $\alpha$:** The uniform grid $\xi$ spans an interval $[\xi_{\min}, \xi_{\max}]$ with $M = 200$ points, giving $\Delta\xi = (\xi_{\max} - \xi_{\min}) / 200$. The $x$-grid spans $[-2, 2]$ (total width 4). The grid boundaries satisfy $x_{\max} - x_c = d\sinh((\xi_{\max} - \xi_c)/\alpha) = 2$.

    For simplicity, let the $\xi$-grid span $[-1, 1]$ with $\xi_c = 0$, so $\Delta\xi = 2/200 = 0.01$ and $d\sinh(1/\alpha) = 2$.

    At the center: $\Delta x_{\text{center}} = (d/\alpha)(0.01) = 0.002$, giving $d/\alpha = 0.2$.

    From the boundary condition: $d\sinh(1/\alpha) = 2$, so $d = 2/\sinh(1/\alpha)$.

    Substituting into $d/\alpha = 0.2$:

    $$
    \frac{2}{\alpha\sinh(1/\alpha)} = 0.2
    $$

    $$
    \alpha\sinh(1/\alpha) = 10
    $$

    Let $u = 1/\alpha$. Then $\sinh(u)/u = 10$. Solving numerically: $\sinh(u) \approx (e^u - e^{-u})/2$. Trying $u \approx 3.5$: $\sinh(3.5)/3.5 \approx 16.54/3.5 \approx 4.73$. Trying $u \approx 4.5$: $\sinh(4.5)/4.5 \approx 45.0/4.5 = 10.0$. So $u \approx 4.5$, giving $\alpha \approx 1/4.5 \approx 0.22$.
