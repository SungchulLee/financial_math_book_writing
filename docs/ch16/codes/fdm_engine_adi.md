# FDM Engine (ADI)

Fourier methods price European options efficiently, but they cannot handle American exercise, general barrier structures, or complex boundary conditions. Finite difference methods (FDM) solve the Heston PDE directly on a two-dimensional grid in $(S, v)$ space, providing a flexible framework for any payoff. The main challenge is that the 2D implicit solve is computationally expensive---a naive Crank-Nicolson scheme requires solving a large sparse linear system at each time step. **Alternating direction implicit (ADI)** schemes split the 2D problem into sequences of 1D tridiagonal solves, reducing the cost from $\mathcal{O}(N_S^2 N_v^2)$ to $\mathcal{O}(N_S N_v)$ per time step while maintaining stability and second-order accuracy. This guide develops the Heston PDE, the grid construction, boundary conditions, and the Craig-Sneyd ADI scheme, with implementation notes referencing [`fdm_engine_adi.py`](fdm_engine_adi.md).

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Formulate the Heston PDE in log-price coordinates and identify its three operator components
    2. Construct a non-uniform grid that concentrates points near the at-the-money region and low variance
    3. Specify boundary conditions at all four grid edges including the degenerate $v = 0$ boundary
    4. Implement the Craig-Sneyd ADI scheme with tridiagonal solvers

!!! tip "Prerequisites"
    This section builds on the [two-dimensional PDE formulation](../fdm/two_dimensional_pde_formulation.md), the [ADI schemes](../fdm/adi_schemes.md), and the [boundary conditions for variance](../fdm/boundary_conditions_for_variance.md). The model parameters come from the [`HestonModel` class](heston_model_class.md).

---

## The Heston PDE

Under the risk-neutral measure, the price $V(S, v, t)$ of a European derivative satisfies:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}v S^2 \frac{\partial^2 V}{\partial S^2} + \rho\xi v S \frac{\partial^2 V}{\partial S \partial v} + \frac{1}{2}\xi^2 v \frac{\partial^2 V}{\partial v^2} + (r - q)S\frac{\partial V}{\partial S} + \kappa(\theta - v)\frac{\partial V}{\partial v} - rV = 0
$$

### Log-Price Transformation

Setting $x = \ln S$ eliminates the multiplicative $S$ coefficient:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}v\frac{\partial^2 V}{\partial x^2} + \rho\xi v\frac{\partial^2 V}{\partial x \partial v} + \frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2} + \left(r - q - \frac{v}{2}\right)\frac{\partial V}{\partial x} + \kappa(\theta - v)\frac{\partial V}{\partial v} - rV = 0
$$

### Operator Splitting

Write $\partial V / \partial t + \mathcal{A}V = 0$ where $\mathcal{A} = \mathcal{A}_0 + \mathcal{A}_1 + \mathcal{A}_2$ with:

- $\mathcal{A}_0 V = \rho\xi v \dfrac{\partial^2 V}{\partial x \partial v}$ (mixed derivative, the **cross term**)
- $\mathcal{A}_1 V = \dfrac{1}{2}v\dfrac{\partial^2 V}{\partial x^2} + \left(r - q - \dfrac{v}{2}\right)\dfrac{\partial V}{\partial x} - \dfrac{r}{2}V$ (the **$x$-direction** operator)
- $\mathcal{A}_2 V = \dfrac{1}{2}\xi^2 v\dfrac{\partial^2 V}{\partial v^2} + \kappa(\theta - v)\dfrac{\partial V}{\partial v} - \dfrac{r}{2}V$ (the **$v$-direction** operator)

The kill term $-rV$ is split equally between $\mathcal{A}_1$ and $\mathcal{A}_2$. Each of $\mathcal{A}_1$ and $\mathcal{A}_2$ is a one-dimensional operator (tridiagonal when discretized), while $\mathcal{A}_0$ couples the two directions.

---

## Grid Construction

### Non-Uniform Grid in x

The log-price grid concentrates points near $x_0 = \ln S_0$ (the ATM region). A sinh-based stretching is standard:

$$
x_i = x_0 + c_1 \sinh\!\left(c_2 \left(\frac{i}{N_x} - \frac{1}{2}\right)\right), \qquad i = 0, 1, \ldots, N_x
$$

where $c_1$ controls the grid range and $c_2$ controls the concentration near $x_0$. Typical values: $c_1 = 4$, $c_2 = 4$, $N_x = 100$--$200$.

### Non-Uniform Grid in v

The variance grid concentrates points near $v = 0$ (where the PDE degenerates) and near $v_0$:

$$
v_j = v_{\max} \left(\frac{j}{N_v}\right)^2, \qquad j = 0, 1, \ldots, N_v
$$

The quadratic spacing places half the grid points in $[0, v_{\max}/4]$. Typical values: $v_{\max} = 5\theta$ to $10\theta$, $N_v = 50$--$100$.

### Time Grid

Uniform spacing $\Delta t = T / N_t$ with $N_t = 100$--$500$ time steps (marching backward from $t = T$ to $t = 0$).

---

## Boundary Conditions

The Heston PDE requires boundary conditions on all four edges of the $(x, v)$ rectangle.

### At v = 0 (Degenerate Boundary)

When $v = 0$, the diffusion coefficients in $x$ and $v$ both vanish. The PDE reduces to the ODE:

$$
\frac{\partial V}{\partial t} + (r - q)\frac{\partial V}{\partial x} + \kappa\theta\frac{\partial V}{\partial v} - rV = 0
$$

This boundary condition is applied by discretizing this reduced PDE on the $v = 0$ row. Note that $\kappa\theta > 0$ (under the Feller condition), so information flows **into** the domain from $v = 0$---the boundary is not a sink.

### At v = v_max

For large $v$, apply a **linear extrapolation** (Neumann-type) condition:

$$
\frac{\partial^2 V}{\partial v^2}\bigg|_{v = v_{\max}} = 0
$$

This assumes the option value varies linearly in $v$ for large variance, which is approximately true when $v_{\max}$ is chosen sufficiently large.

### At x = x_min (Deep OTM for Calls)

For calls: $V(x_{\min}, v, t) = 0$ (the call is worthless when $S$ is very small).

For puts: $V(x_{\min}, v, t) = K e^{-r(T-t)} - S_{\min}$ (intrinsic value approximation).

### At x = x_max (Deep ITM for Calls)

For calls: $V(x_{\max}, v, t) = S_{\max} - K e^{-r(T-t)}$ (intrinsic value approximation).

For puts: $V(x_{\max}, v, t) = 0$.

---

## The Craig-Sneyd ADI Scheme

The Craig-Sneyd scheme treats $\mathcal{A}_1$ and $\mathcal{A}_2$ implicitly (for stability) and $\mathcal{A}_0$ explicitly (to avoid non-tridiagonal systems). With time-step size $\Delta t$ and the parameter $\vartheta \in [1/2, 1]$ (typically $\vartheta = 1/2$ for second-order accuracy), the scheme proceeds in four stages at each time step from $V^n$ to $V^{n+1}$.

### Stage 1: Explicit Predictor

$$
\hat{V} = V^n + \Delta t \left(\mathcal{A}_0 V^n + \mathcal{A}_1 V^n + \mathcal{A}_2 V^n\right)
$$

### Stage 2: Implicit x-Direction

$$
(I - \vartheta \Delta t \, \mathcal{A}_1) V^* = \hat{V} - \vartheta \Delta t \, \mathcal{A}_1 V^n
$$

This is a tridiagonal system in the $x$-direction for each fixed $v_j$, solved via Thomas's algorithm.

### Stage 3: Implicit v-Direction

$$
(I - \vartheta \Delta t \, \mathcal{A}_2) V^{**} = V^* - \vartheta \Delta t \, \mathcal{A}_2 V^n
$$

This is a tridiagonal system in the $v$-direction for each fixed $x_i$.

### Stage 4: Cross-Term Correction

$$
V^{n+1} = V^{**} + \frac{1}{2}\Delta t\left(\mathcal{A}_0 V^{**} - \mathcal{A}_0 V^n\right)
$$

This correction improves accuracy by incorporating an updated estimate of the cross derivative.

!!! note "Stability"
    The Craig-Sneyd scheme is unconditionally stable for $\vartheta \geq 1/2$. The choice $\vartheta = 1/2$ gives second-order accuracy in time. The Douglas scheme is a simpler variant that omits Stage 4 but has slightly larger time-discretization error.

---

## Discretizing the Mixed Derivative

The cross term $\mathcal{A}_0 V = \rho\xi v \, \partial^2 V / \partial x \partial v$ is discretized using the central difference stencil:

$$
\frac{\partial^2 V}{\partial x \partial v}\bigg|_{i,j} \approx \frac{V_{i+1,j+1} - V_{i+1,j-1} - V_{i-1,j+1} + V_{i-1,j-1}}{4 \Delta x_i \Delta v_j}
$$

On a non-uniform grid, replace $\Delta x_i$ and $\Delta v_j$ with the appropriate local spacing.

This stencil is always applied explicitly (it acts on known values from the current or predicted time level), so it never creates a non-tridiagonal matrix.

---

## Implementation Outline

```python
def heston_fdm_adi(model, K, T, N_x=150, N_v=60, N_t=200,
                   cp="call", theta_adi=0.5):
    """
    Price a European option via the Craig-Sneyd ADI scheme.

    Parameters
    ----------
    model : HestonModel
    K : float
        Strike price
    T : float
        Time to maturity
    N_x, N_v, N_t : int
        Grid sizes
    cp : str
        "call" or "put"
    theta_adi : float
        ADI scheme parameter (0.5 for 2nd order)

    Returns
    -------
    price : float
        Option price at (S0, v0, t=0)
    """
    # Build grids
    x_grid = build_log_price_grid(model, K, N_x)
    v_grid = build_variance_grid(model, N_v)
    dt = T / N_t

    # Terminal condition
    S_grid = np.exp(x_grid)
    if cp == "call":
        V = np.maximum(S_grid[:, None] - K, 0) * np.ones((1, N_v + 1))
    else:
        V = np.maximum(K - S_grid[:, None], 0) * np.ones((1, N_v + 1))

    # Time-stepping (backward from T to 0)
    for n in range(N_t):
        # Apply boundary conditions
        apply_boundary_conditions(V, x_grid, v_grid, K, T - n * dt,
                                 model, cp)

        # Stage 1: Explicit predictor
        A0_Vn = compute_cross_term(V, x_grid, v_grid, model)
        A1_Vn = compute_x_operator(V, x_grid, v_grid, model)
        A2_Vn = compute_v_operator(V, x_grid, v_grid, model)
        V_hat = V + dt * (A0_Vn + A1_Vn + A2_Vn)

        # Stage 2: Implicit x-direction (tridiagonal)
        V_star = solve_x_implicit(V_hat, V, A1_Vn, x_grid, v_grid,
                                  model, dt, theta_adi)

        # Stage 3: Implicit v-direction (tridiagonal)
        V_dstar = solve_v_implicit(V_star, V, A2_Vn, x_grid, v_grid,
                                   model, dt, theta_adi)

        # Stage 4: Cross-term correction
        A0_Vdstar = compute_cross_term(V_dstar, x_grid, v_grid, model)
        V = V_dstar + 0.5 * dt * (A0_Vdstar - A0_Vn)

    # Interpolate to (S0, v0)
    price = interpolate_to_spot(V, x_grid, v_grid,
                                np.log(model.S0), model.v0)
    return price
```

---

## Validation and Convergence

Validate the FDM engine against the COS method for European options:

| Grid ($N_x \times N_v \times N_t$) | FDM Price | COS Price | Error (bps) |
|---|---|---|---|
| $50 \times 25 \times 50$ | 10.4521 | 10.4503 | 0.17 |
| $100 \times 50 \times 100$ | 10.4506 | 10.4503 | 0.03 |
| $200 \times 100 \times 200$ | 10.4503 | 10.4503 | 0.00 |

The scheme converges as $\mathcal{O}(\Delta x^2 + \Delta v^2 + \Delta t^2)$ with the Craig-Sneyd method at $\vartheta = 1/2$.

---

## Summary

The FDM-ADI engine solves the two-dimensional Heston PDE by splitting it into three operators: the $x$-direction diffusion/convection $\mathcal{A}_1$, the $v$-direction diffusion/convection $\mathcal{A}_2$, and the mixed derivative $\mathcal{A}_0$. The Craig-Sneyd scheme treats $\mathcal{A}_1$ and $\mathcal{A}_2$ implicitly via tridiagonal solves and $\mathcal{A}_0$ explicitly with a correction step, achieving unconditional stability and second-order accuracy in all variables. Non-uniform grids in both $x$ and $v$ concentrate resolution where the solution varies most rapidly. The degenerate boundary at $v = 0$ requires special treatment via the reduced PDE. This engine is the foundation for pricing American options (via PSOR) and barrier options under the Heston model.

---

## Exercises

**Exercise 1.**
Starting from the Heston PDE in $(S, v)$ coordinates, derive the log-price PDE by substituting $x = \ln S$. Verify that the coefficient of $\partial V / \partial x$ becomes $(r - q - v/2)$ and that the $S^2$ coefficient in the second derivative is absorbed. Explain why the log-price formulation is preferred for FDM: what numerical problem does the multiplicative $S$ coefficient cause on a uniform grid?

??? success "Solution to Exercise 1"
    Starting from the Heston PDE in $(S, v)$ coordinates:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}v S^2 \frac{\partial^2 V}{\partial S^2} + \rho\xi v S \frac{\partial^2 V}{\partial S \partial v} + \frac{1}{2}\xi^2 v \frac{\partial^2 V}{\partial v^2} + (r - q)S\frac{\partial V}{\partial S} + \kappa(\theta - v)\frac{\partial V}{\partial v} - rV = 0
    $$

    Substitute $x = \ln S$, so $S = e^x$. By the chain rule:

    $$
    \frac{\partial V}{\partial S} = \frac{\partial V}{\partial x}\frac{\partial x}{\partial S} = \frac{1}{S}\frac{\partial V}{\partial x}
    $$

    $$
    \frac{\partial^2 V}{\partial S^2} = \frac{\partial}{\partial S}\left(\frac{1}{S}\frac{\partial V}{\partial x}\right) = -\frac{1}{S^2}\frac{\partial V}{\partial x} + \frac{1}{S^2}\frac{\partial^2 V}{\partial x^2}
    $$

    $$
    \frac{\partial^2 V}{\partial S \partial v} = \frac{1}{S}\frac{\partial^2 V}{\partial x \partial v}
    $$

    Substituting into the PDE:

    - **Second derivative in $S$**: $\frac{1}{2}v S^2 \cdot \frac{1}{S^2}\left(\frac{\partial^2 V}{\partial x^2} - \frac{\partial V}{\partial x}\right) = \frac{1}{2}v\frac{\partial^2 V}{\partial x^2} - \frac{1}{2}v\frac{\partial V}{\partial x}$
    - **Cross derivative**: $\rho\xi v S \cdot \frac{1}{S}\frac{\partial^2 V}{\partial x \partial v} = \rho\xi v\frac{\partial^2 V}{\partial x \partial v}$
    - **First derivative in $S$**: $(r - q)S \cdot \frac{1}{S}\frac{\partial V}{\partial x} = (r - q)\frac{\partial V}{\partial x}$

    Collecting the $\partial V/\partial x$ terms:

    $$
    -\frac{1}{2}v\frac{\partial V}{\partial x} + (r - q)\frac{\partial V}{\partial x} = \left(r - q - \frac{v}{2}\right)\frac{\partial V}{\partial x}
    $$

    This confirms the coefficient of $\partial V/\partial x$ is $(r - q - v/2)$, and the $S^2$ factor has been absorbed.

    **Why the log-price formulation is preferred for FDM:**

    In the $(S, v)$ formulation, the diffusion coefficient $\frac{1}{2}vS^2$ and convection coefficient $(r-q)S$ are both proportional to $S$. On a uniform grid in $S$, this means:

    1. The Peclet number (ratio of convection to diffusion) varies across the grid, causing numerical instability in regions of large $S$.
    2. Resolution is wasted in the large-$S$ region where the option value varies slowly, and is insufficient near $S = 0$ where the value changes rapidly.
    3. The coefficient $S^2$ in the second derivative creates a "superdiffusion" at large $S$, requiring very fine grids or extremely small time steps to maintain stability.

    In the $(x, v)$ formulation, all coefficients depend only on $v$ (not on $x$), making the PDE coefficients spatially uniform in the $x$-direction. This allows uniform or mildly non-uniform grids to resolve the solution accurately, and the CFL condition is independent of the grid location in $x$.

---

**Exercise 2.**
Consider a non-uniform variance grid $v_j = v_{\max}(j/N_v)^2$ for $j = 0, 1, \ldots, N_v$ with $v_{\max} = 0.5$ and $N_v = 100$. Compute the grid spacing $\Delta v_j = v_{j+1} - v_j$ for $j = 0, 1, 2$ and $j = 98, 99$. What fraction of the grid points lie in $[0, v_{\max}/4] = [0, 0.125]$? Explain why concentrating points near $v = 0$ is important for the accuracy of the Heston FDM.

??? success "Solution to Exercise 2"
    The grid is $v_j = v_{\max}(j/N_v)^2$ with $v_{\max} = 0.5$ and $N_v = 100$.

    The spacing is $\Delta v_j = v_{j+1} - v_j = v_{\max}\left[\left(\frac{j+1}{N_v}\right)^2 - \left(\frac{j}{N_v}\right)^2\right] = v_{\max}\frac{2j + 1}{N_v^2}$.

    **For $j = 0$:**

    $$
    \Delta v_0 = 0.5 \times \frac{1}{10000} = 0.00005
    $$

    **For $j = 1$:**

    $$
    \Delta v_1 = 0.5 \times \frac{3}{10000} = 0.00015
    $$

    **For $j = 2$:**

    $$
    \Delta v_2 = 0.5 \times \frac{5}{10000} = 0.00025
    $$

    **For $j = 98$:**

    $$
    \Delta v_{98} = 0.5 \times \frac{197}{10000} = 0.00985
    $$

    **For $j = 99$:**

    $$
    \Delta v_{99} = 0.5 \times \frac{199}{10000} = 0.00995
    $$

    The spacing near $v = 0$ is about 200 times finer than near $v = v_{\max}$.

    **Fraction of grid points in $[0, v_{\max}/4] = [0, 0.125]$:**

    The point $v_j = 0.125$ corresponds to $(j/100)^2 = 0.125/0.5 = 0.25$, so $j/100 = 0.5$, i.e., $j = 50$. Therefore, 50 out of 100 grid points (i.e., **50%**) lie in $[0, 0.125]$, which is only 25% of the total range.

    **Why concentration near $v = 0$ is important:**

    1. **PDE degeneracy**: At $v = 0$, the diffusion coefficient $\frac{1}{2}\xi^2 v$ and $\frac{1}{2}v$ both vanish, creating a degenerate boundary. The solution exhibits rapid variation near $v = 0$ (especially when the Feller condition is violated), requiring fine resolution to capture the boundary layer.

    2. **Typical calibrated parameters**: Market-calibrated Heston parameters often have $v_0 = 0.01$--$0.06$ and $\theta = 0.02$--$0.08$. With $v_{\max} = 0.5$, the economically relevant variance range $[0, 0.1]$ occupies only 20% of the domain. The quadratic grid ensures adequate resolution in this critical region.

    3. **Interpolation accuracy**: The final price is obtained by interpolating to $(x_0, v_0)$ on the grid. If $v_0 = 0.04$ falls between coarse grid points, interpolation error can dominate. The quadratic grid ensures that $v_0$ is surrounded by closely-spaced grid points.

---

**Exercise 3.**
At the degenerate boundary $v = 0$, the Heston PDE reduces to:

$$
\frac{\partial V}{\partial t} + (r - q)\frac{\partial V}{\partial x} + \kappa\theta\frac{\partial V}{\partial v} - rV = 0
$$

Explain why the diffusion terms vanish at $v = 0$. If the Feller condition $2\kappa\theta \geq \xi^2$ is satisfied, the term $\kappa\theta\frac{\partial V}{\partial v}$ pushes information into the domain. Discretize this reduced PDE using forward differences in $v$ and central differences in $x$, and write the resulting finite difference equation for $V_{i,0}^{n+1}$.

??? success "Solution to Exercise 3"
    At $v = 0$, the Heston PDE terms involving $v$ as a multiplicative factor vanish:

    - $\frac{1}{2}v\frac{\partial^2 V}{\partial x^2} \to 0$ (the $x$-diffusion vanishes)
    - $\rho\xi v\frac{\partial^2 V}{\partial x \partial v} \to 0$ (the cross term vanishes)
    - $\frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2} \to 0$ (the $v$-diffusion vanishes)
    - The convection in $v$: $\kappa(\theta - 0)\frac{\partial V}{\partial v} = \kappa\theta\frac{\partial V}{\partial v}$ survives

    The remaining PDE is:

    $$
    \frac{\partial V}{\partial t} + (r - q)\frac{\partial V}{\partial x} + \kappa\theta\frac{\partial V}{\partial v} - rV = 0
    $$

    If the Feller condition $2\kappa\theta \geq \xi^2$ holds, the drift $\kappa\theta > 0$ is sufficiently strong to push the variance away from zero. Since $\partial V/\partial v$ is typically negative for a call (higher variance means higher option value, so moving into the domain increases $V$), the term $\kappa\theta \partial V/\partial v$ acts as an inflow from the boundary.

    **Finite difference discretization:**

    Use backward Euler in time, central differences in $x$, and a **forward** difference in $v$ (since the $v$-convection at $v = 0$ has coefficient $\kappa\theta > 0$, pushing into the domain, so a forward difference is appropriate for the upwind direction):

    $$
    \frac{V_{i,0}^{n+1} - V_{i,0}^n}{\Delta t} + (r - q)\frac{V_{i+1,0}^n - V_{i-1,0}^n}{2\Delta x_i} + \kappa\theta\frac{V_{i,1}^n - V_{i,0}^n}{\Delta v_0} - rV_{i,0}^n = 0
    $$

    Solving for $V_{i,0}^{n+1}$:

    $$
    V_{i,0}^{n+1} = V_{i,0}^n + \Delta t\left[-(r-q)\frac{V_{i+1,0}^n - V_{i-1,0}^n}{2\Delta x_i} - \kappa\theta\frac{V_{i,1}^n - V_{i,0}^n}{\Delta v_0} + rV_{i,0}^n\right]
    $$

    Note: since we are marching **backward** in time (from $t = T$ to $t = 0$), the time index convention is reversed: $V^{n+1}$ is at an earlier time than $V^n$. The forward difference in $v$ uses $V_{i,1}$ (the first interior point) and $V_{i,0}$ (the boundary), which is appropriate since information flows inward from $v = 0$.

---

**Exercise 4.**
The Craig-Sneyd ADI scheme has four stages. Stages 2 and 3 each require solving a tridiagonal system. If the grid has $N_x = 150$ and $N_v = 60$, how many tridiagonal solves are performed per time step (counting both stages)? If each tridiagonal solve of size $N$ costs $\mathcal{O}(N)$ operations via Thomas's algorithm, compute the total cost per time step. Compare this with a fully implicit Crank-Nicolson scheme that requires solving a single $(N_x \cdot N_v) \times (N_x \cdot N_v)$ sparse system.

??? success "Solution to Exercise 4"
    **Stage 2 (implicit $x$-direction):** For each fixed $v_j$ ($j = 0, 1, \ldots, N_v$), solve a tridiagonal system of size $N_x + 1$ (or $N_x - 1$ interior points). This requires $N_v + 1 = 61$ tridiagonal solves, each of size approximately $N_x = 150$.

    **Stage 3 (implicit $v$-direction):** For each fixed $x_i$ ($i = 0, 1, \ldots, N_x$), solve a tridiagonal system of size $N_v + 1$ (or $N_v - 1$ interior points). This requires $N_x + 1 = 151$ tridiagonal solves, each of size approximately $N_v = 60$.

    **Total tridiagonal solves per time step:**

    $$
    N_{\text{solves}} = (N_v + 1) + (N_x + 1) = 61 + 151 = 212
    $$

    **Total cost per time step:**

    Thomas's algorithm for a tridiagonal system of size $N$ costs $\mathcal{O}(N)$ operations (specifically, $8N$ floating-point operations):

    $$
    \text{Cost}_{\text{ADI}} = 61 \times \mathcal{O}(N_x) + 151 \times \mathcal{O}(N_v) = 61 \times 150 + 151 \times 60 = 9{,}150 + 9{,}060 = 18{,}210
    $$

    This is $\mathcal{O}(N_x N_v)$.

    Including Stages 1 and 4 (explicit operations), which involve matrix-vector multiplications on the $N_x \times N_v$ grid, the total cost is $\mathcal{O}(N_x N_v)$ per time step.

    **Comparison with fully implicit Crank-Nicolson:**

    A fully implicit scheme requires solving a single sparse linear system of size $(N_x + 1)(N_v + 1) = 151 \times 61 = 9{,}211$. The matrix is banded with bandwidth approximately $N_x + 1$ (due to the $v$-coupling). Using a banded solver, the cost is $\mathcal{O}(N_x^2 N_v)$ or $\mathcal{O}(N_x N_v^2)$ (whichever is larger), which for this grid is:

    $$
    \text{Cost}_{\text{CN}} = \mathcal{O}(N_x^2 \cdot N_v) = \mathcal{O}(150^2 \times 60) = \mathcal{O}(1{,}350{,}000)
    $$

    Using a direct sparse solver (e.g., LU decomposition), the cost is roughly $\mathcal{O}(N_x N_v \cdot \min(N_x, N_v))$ with proper ordering, which is still $\mathcal{O}(N_x N_v \cdot 60) \approx 540{,}000$.

    The ADI cost ($18{,}210$) is about **30--75 times cheaper** than the fully implicit Crank-Nicolson cost ($540{,}000$--$1{,}350{,}000$). This massive speedup is the fundamental motivation for ADI splitting.

---

**Exercise 5.**
The convergence table shows that doubling the grid from $100 \times 50 \times 100$ to $200 \times 100 \times 200$ reduces the error from 0.03 bps to 0.00 bps. Verify that this is consistent with second-order convergence $\mathcal{O}(\Delta x^2 + \Delta v^2 + \Delta t^2)$: when all grid sizes are doubled, each spacing halves, so the error should decrease by a factor of approximately 4. Compute the actual error reduction factor and discuss any deviations.

??? success "Solution to Exercise 5"
    The convergence table gives:

    | Grid | Error (bps) |
    |---|---|
    | $50 \times 25 \times 50$ | 0.17 |
    | $100 \times 50 \times 100$ | 0.03 |
    | $200 \times 100 \times 200$ | 0.00 |

    From the first refinement (doubling all grid sizes):

    $$
    \text{Reduction factor}_1 = \frac{0.17}{0.03} \approx 5.67
    $$

    For perfect second-order convergence, doubling all grid sizes (halving $\Delta x$, $\Delta v$, $\Delta t$) should reduce the error by a factor of $2^2 = 4$. The observed factor of 5.67 exceeds 4.

    From the second refinement:

    $$
    \text{Reduction factor}_2 = \frac{0.03}{0.00}
    $$

    This ratio is infinite because the error rounds to 0.00 bps. If the true error at the finest grid is, say, 0.002 bps, the reduction factor would be $0.03/0.002 = 15$, which also exceeds 4.

    **Explanation of deviations from the theoretical factor of 4:**

    1. **The reported errors are rounded**: The 0.00 bps at the finest grid likely represents an error of $10^{-5}$--$10^{-4}$ bps. If the true value is 0.005 bps, the ratio is $0.03/0.005 = 6$, still above 4 but closer.

    2. **Pre-asymptotic regime**: At the coarsest grid ($50 \times 25 \times 50$), the error may include higher-order terms ($\mathcal{O}(\Delta x^4)$ etc.) that are not negligible. The observed convergence rate is closer to the theoretical value only in the asymptotic regime (sufficiently fine grids).

    3. **Non-uniform grid effects**: The sinh-based $x$-grid and quadratic $v$-grid have locally varying step sizes. When the grid is refined, the local step sizes decrease faster in the regions where points are concentrated (near ATM and near $v = 0$), which can produce super-quadratic convergence if the error is dominated by these regions.

    4. **Error cancellation**: On certain grid sizes, positive and negative local errors may partially cancel, leading to a smaller global error than the pure $\mathcal{O}(h^2)$ bound would predict.

    Overall, the convergence is consistent with (and slightly better than) the theoretical second-order rate $\mathcal{O}(\Delta x^2 + \Delta v^2 + \Delta t^2)$.

---

**Exercise 6.**
The mixed derivative stencil:

$$
\frac{\partial^2 V}{\partial x \partial v}\bigg|_{i,j} \approx \frac{V_{i+1,j+1} - V_{i+1,j-1} - V_{i-1,j+1} + V_{i-1,j-1}}{4\Delta x_i \Delta v_j}
$$

involves four corner points of the $(i, j)$ cell. Explain why this stencil cannot be made into a tridiagonal matrix in either direction. This is the fundamental reason the cross term must be treated explicitly in the ADI scheme. What is the stability implication of treating $\mathcal{A}_0$ explicitly?

??? success "Solution to Exercise 6"
    The mixed derivative stencil:

    $$
    \frac{\partial^2 V}{\partial x \partial v}\bigg|_{i,j} \approx \frac{V_{i+1,j+1} - V_{i+1,j-1} - V_{i-1,j+1} + V_{i-1,j-1}}{4\Delta x_i \Delta v_j}
    $$

    involves four points: $(i+1, j+1)$, $(i+1, j-1)$, $(i-1, j+1)$, and $(i-1, j-1)$---the four **corners** of the cell centered at $(i, j)$.

    **Why this cannot be made tridiagonal:**

    A tridiagonal matrix in the $x$-direction (for fixed $j$) involves only the points $(i-1, j)$, $(i, j)$, and $(i+1, j)$---three consecutive points in the same row. The mixed derivative stencil couples point $(i, j)$ to $(i \pm 1, j \pm 1)$, which are in **adjacent rows** $j-1$ and $j+1$. Including these off-row points destroys the tridiagonal structure.

    Similarly, a tridiagonal matrix in the $v$-direction (for fixed $i$) would only involve $(i, j-1)$, $(i, j)$, $(i, j+1)$. The stencil couples to $(i \pm 1, j \pm 1)$, which are in adjacent columns.

    In matrix form, the full implicit operator including the cross term has bandwidth $2N_x + 1$ (or $2N_v + 1$), making it a **pentadiagonal** or wider banded system. This is fundamentally why the ADI method treats $\mathcal{A}_0$ explicitly.

    **Stability implication of explicit treatment:**

    Treating $\mathcal{A}_0$ explicitly means the cross-term contribution is evaluated at the known time level $V^n$, not the unknown $V^{n+1}$. This introduces a CFL-like stability constraint:

    $$
    \Delta t \lesssim \frac{4\Delta x \Delta v}{|\rho\xi v_{\max}|}
    $$

    For the Craig-Sneyd scheme with $\vartheta = 1/2$, the implicit treatment of $\mathcal{A}_1$ and $\mathcal{A}_2$ provides unconditional stability in the respective directions, and the explicit cross-term correction in Stage 4 mitigates (but does not eliminate) the stability constraint from $\mathcal{A}_0$. In practice, for typical Heston parameters ($|\rho| \leq 0.9$, moderate $\xi$), the scheme is stable with the standard time-step sizes ($N_t = 100$--$500$), and the explicit treatment of $\mathcal{A}_0$ does not impose a binding constraint. However, for extreme parameters ($|\rho| \to 1$, large $\xi$), the user may need to increase $N_t$ to maintain stability.

---

**Exercise 7.**
Modify the FDM engine to price an American put option. The American exercise constraint requires $V(x, v, t) \geq \max(K - e^x, 0)$ at all times. Describe how to incorporate this constraint at each time step using the **projected SOR (PSOR)** method: after the ADI solve, project the solution onto the constraint set $V \geq g(x)$ where $g(x) = \max(K - e^x, 0)$. Where on the $(x, v)$ grid do you expect the early exercise boundary to lie, and how does it depend on $v$?

??? success "Solution to Exercise 7"
    **American put pricing via PSOR with the ADI scheme:**

    The American put satisfies the same Heston PDE as the European put, but with the additional **early exercise constraint**:

    $$
    V(x, v, t) \geq g(x) = \max(K - e^x, 0) \quad \text{for all } (x, v, t)
    $$

    This converts the PDE into a **free boundary problem** (or linear complementarity problem):

    $$
    \min\left(-\frac{\partial V}{\partial t} - \mathcal{A}V, \; V - g\right) = 0
    $$

    **Incorporating PSOR with ADI:**

    At each time step (marching backward from $T$ to $0$), the procedure is:

    1. **Run the ADI scheme** (Stages 1--4) as for the European put, obtaining an intermediate solution $V^{n+1,\text{Euro}}$.

    2. **Project onto the exercise boundary**: Apply the constraint pointwise:

        $$
        V_{i,j}^{n+1} = \max\left(V_{i,j}^{n+1,\text{Euro}}, \; g(x_i)\right) = \max\left(V_{i,j}^{n+1,\text{Euro}}, \; \max(K - e^{x_i}, 0)\right)
        $$

    This "penalty" or "projection" approach is the simplest implementation. For higher accuracy, PSOR (projected successive over-relaxation) replaces the implicit solves in Stages 2 and 3 with projected solves:

    In the implicit $x$-direction solve (Stage 2), instead of solving $(I - \vartheta\Delta t\mathcal{A}_1)V^* = \text{RHS}$, apply PSOR iteration:

    $$
    V_i^{(k+1)} = \max\left(V_i^{(k)} + \omega\left(\frac{\text{RHS}_i - \sum_j a_{ij}V_j^{(k)}}{a_{ii}}\right) - V_i^{(k)}, \; g(x_i)\right)
    $$

    where $\omega \in (1, 2)$ is the relaxation parameter (typically $\omega = 1.2$--$1.5$) and $a_{ij}$ are the tridiagonal matrix entries. Iterate until convergence.

    **Early exercise boundary location:**

    The early exercise boundary is the curve $S^*(v, t)$ (or equivalently $x^*(v, t) = \ln S^*(v, t)$) below which it is optimal to exercise the put immediately. For a put, exercise is optimal when $S$ is small enough (deep ITM).

    The boundary depends on $v$ as follows:

    - **High $v$**: When variance is high, the option has significant time value because there is a chance the stock price could recover above $K$. The exercise boundary $S^*(v, t)$ is **lower** (exercise is delayed to lower stock prices).

    - **Low $v$**: When variance is low, the stock price is unlikely to recover, so the time value is small. The exercise boundary $S^*(v, t)$ is **higher** (exercise happens at stock prices closer to $K$).

    - **As $v \to 0$**: If the Feller condition is satisfied and variance stays near zero, the dynamics become nearly deterministic ($S_t \approx S_0 e^{(r-q)t}$). The exercise boundary approaches the deterministic Black-Scholes American put boundary with $\sigma = 0$, which is $S^* = K$ (immediate exercise at the strike).

    - **As $t \to T$** (near expiry): The exercise boundary approaches $K$ for all $v$, since time value vanishes.

    On the $(x, v)$ grid, the early exercise region is a 2D set $\{(x, v) : x \leq x^*(v, t)\}$ that changes shape at each time step. The boundary $x^*(v, t)$ is a decreasing function of $v$ (the exercise region shrinks as variance increases) and an increasing function of time-to-maturity (the exercise region grows as expiry approaches).
