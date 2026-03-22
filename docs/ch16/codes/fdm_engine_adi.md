# FDM Engine (ADI)

Fourier methods price European options efficiently, but they cannot handle American exercise, general barrier structures, or complex boundary conditions. Finite difference methods (FDM) solve the Heston PDE directly on a two-dimensional grid in $(S, v)$ space, providing a flexible framework for any payoff. The main challenge is that the 2D implicit solve is computationally expensive---a naive Crank-Nicolson scheme requires solving a large sparse linear system at each time step. **Alternating direction implicit (ADI)** schemes split the 2D problem into sequences of 1D tridiagonal solves, reducing the cost from $\mathcal{O}(N_S^2 N_v^2)$ to $\mathcal{O}(N_S N_v)$ per time step while maintaining stability and second-order accuracy. This guide develops the Heston PDE, the grid construction, boundary conditions, and the Craig-Sneyd ADI scheme, with implementation notes referencing [`fdm_engine_adi.py`](fdm_engine_adi.py).

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

### Non-Uniform Grid in $x$

The log-price grid concentrates points near $x_0 = \ln S_0$ (the ATM region). A sinh-based stretching is standard:

$$
x_i = x_0 + c_1 \sinh\!\left(c_2 \left(\frac{i}{N_x} - \frac{1}{2}\right)\right), \qquad i = 0, 1, \ldots, N_x
$$

where $c_1$ controls the grid range and $c_2$ controls the concentration near $x_0$. Typical values: $c_1 = 4$, $c_2 = 4$, $N_x = 100$--$200$.

### Non-Uniform Grid in $v$

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

### At $v = 0$ (Degenerate Boundary)

When $v = 0$, the diffusion coefficients in $x$ and $v$ both vanish. The PDE reduces to the ODE:

$$
\frac{\partial V}{\partial t} + (r - q)\frac{\partial V}{\partial x} + \kappa\theta\frac{\partial V}{\partial v} - rV = 0
$$

This boundary condition is applied by discretizing this reduced PDE on the $v = 0$ row. Note that $\kappa\theta > 0$ (under the Feller condition), so information flows **into** the domain from $v = 0$---the boundary is not a sink.

### At $v = v_{\max}$

For large $v$, apply a **linear extrapolation** (Neumann-type) condition:

$$
\frac{\partial^2 V}{\partial v^2}\bigg|_{v = v_{\max}} = 0
$$

This assumes the option value varies linearly in $v$ for large variance, which is approximately true when $v_{\max}$ is chosen sufficiently large.

### At $x = x_{\min}$ (Deep OTM for Calls)

For calls: $V(x_{\min}, v, t) = 0$ (the call is worthless when $S$ is very small).

For puts: $V(x_{\min}, v, t) = K e^{-r(T-t)} - S_{\min}$ (intrinsic value approximation).

### At $x = x_{\max}$ (Deep ITM for Calls)

For calls: $V(x_{\max}, v, t) = S_{\max} - K e^{-r(T-t)}$ (intrinsic value approximation).

For puts: $V(x_{\max}, v, t) = 0$.

---

## The Craig-Sneyd ADI Scheme

The Craig-Sneyd scheme treats $\mathcal{A}_1$ and $\mathcal{A}_2$ implicitly (for stability) and $\mathcal{A}_0$ explicitly (to avoid non-tridiagonal systems). With time-step size $\Delta t$ and the parameter $\vartheta \in [1/2, 1]$ (typically $\vartheta = 1/2$ for second-order accuracy), the scheme proceeds in four stages at each time step from $V^n$ to $V^{n+1}$.

### Stage 1: Explicit Predictor

$$
\hat{V} = V^n + \Delta t \left(\mathcal{A}_0 V^n + \mathcal{A}_1 V^n + \mathcal{A}_2 V^n\right)
$$

### Stage 2: Implicit $x$-Direction

$$
(I - \vartheta \Delta t \, \mathcal{A}_1) V^* = \hat{V} - \vartheta \Delta t \, \mathcal{A}_1 V^n
$$

This is a tridiagonal system in the $x$-direction for each fixed $v_j$, solved via Thomas's algorithm.

### Stage 3: Implicit $v$-Direction

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
