# Finite Difference Methods for SABR

The SABR model gives rise to a **two-dimensional pricing PDE** in the forward $F$ and the stochastic volatility $\sigma$, with a mixed derivative term induced by the correlation $\rho$. Finite difference methods (FDM) solve this PDE on a discrete grid, producing option prices, implied volatilities, and Greeks simultaneously across all strikes. FDM is the method of choice for American-style swaptions, barrier options under SABR, and as a benchmark for the Hagan approximation and arbitrage-free extensions. This section formulates the 2D SABR PDE, discusses grid construction and boundary conditions, and presents the Alternating Direction Implicit (ADI) splitting scheme that makes the 2D problem computationally tractable.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the 2D pricing PDE for European options under the SABR model
    2. Specify appropriate boundary conditions on all edges of the computational domain
    3. Construct a non-uniform grid in $(F, \sigma)$ concentrated near the current forward
    4. Implement an ADI scheme to solve the 2D PDE efficiently
    5. Handle the mixed derivative term arising from correlation

---

## The SABR Pricing PDE

### Derivation

Under the forward measure, the price $V(t, F, \sigma)$ of a European option satisfies the backward Kolmogorov equation:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 F^{2\beta}\frac{\partial^2 V}{\partial F^2} + \rho\nu\sigma^2 F^{\beta}\frac{\partial^2 V}{\partial F\,\partial\sigma} + \frac{1}{2}\nu^2\sigma^2\frac{\partial^2 V}{\partial\sigma^2} = 0
$$

with terminal condition $V(T, F, \sigma) = \max(F - K, 0)$ for a call (or $\max(K - F, 0)$ for a put).

There is no drift in the forward equation (martingale under the forward measure) and no drift in the volatility equation (lognormal dynamics with no mean reversion). The PDE contains three second-order terms:

- $\frac{1}{2}\sigma^2 F^{2\beta}\partial_{FF}V$: diffusion in the forward direction
- $\rho\nu\sigma^2 F^{\beta}\partial_{F\sigma}V$: mixed derivative (from correlation)
- $\frac{1}{2}\nu^2\sigma^2\partial_{\sigma\sigma}V$: diffusion in the volatility direction

### Operator Splitting

Define the differential operators:

$$
\mathcal{L}_F = \frac{1}{2}\sigma^2 F^{2\beta}\frac{\partial^2}{\partial F^2}
$$

$$
\mathcal{L}_{\sigma} = \frac{1}{2}\nu^2\sigma^2\frac{\partial^2}{\partial\sigma^2}
$$

$$
\mathcal{L}_{\text{mix}} = \rho\nu\sigma^2 F^{\beta}\frac{\partial^2}{\partial F\,\partial\sigma}
$$

The PDE becomes $\partial_t V + (\mathcal{L}_F + \mathcal{L}_{\sigma} + \mathcal{L}_{\text{mix}})V = 0$. The ADI scheme splits these operators to reduce the 2D problem to a sequence of 1D problems.

---

## Grid Construction

### Domain

The computational domain is $[F_{\min}, F_{\max}] \times [\sigma_{\min}, \sigma_{\max}]$:

- **Forward**: $F_{\min} = 0$ (absorbing boundary for $\beta > 0$) or a small negative value (for $\beta = 0$). $F_{\max} = 3F_0$ to $5F_0$.
- **Volatility**: $\sigma_{\min} = 0.01\alpha$ (small but positive, to avoid degeneracy). $\sigma_{\max} = 3\alpha$ to $5\alpha$.
- **Time**: $[0, T]$ with $N_t$ steps.

### Non-Uniform Grid

A uniform grid is inefficient because the option price varies most rapidly near the current forward $F_0$ and the current volatility $\alpha$. A **sinh-based** non-uniform grid concentrates points near these values:

$$
F_j = F_0 + c_F\sinh\!\left(\frac{j - j_0}{d_F}\right), \qquad j = 0, 1, \ldots, N_F
$$

where $c_F$ and $d_F$ control the concentration and $j_0$ is the index closest to $F_0$. A similar construction applies for the $\sigma$ direction.

Typical grid sizes:

| Direction | Grid Points | Spacing at Center | Spacing at Boundary |
|-----------|-------------|-------------------|---------------------|
| Forward ($F$) | 100--200 | 0.5--2 bps | 10--50 bps |
| Volatility ($\sigma$) | 30--60 | $0.01\alpha$ | $0.1\alpha$ |
| Time ($t$) | 50--200 | Uniform or concentrated near $T$ |

---

## Boundary Conditions

### Forward Boundaries

**At $F = F_{\min} = 0$** (for $\beta > 0$): The diffusion coefficient $\sigma^2 F^{2\beta} \to 0$, so the PDE degenerates. The appropriate boundary condition is:

- Absorbing: $V(t, 0, \sigma) = 0$ for a call, $V(t, 0, \sigma) = K$ for a put
- This is consistent with the CEV boundary analysis

**At $F = F_{\max}$**: For a call, $V \approx F - Ke^{-r(T-t)}$ (intrinsic value). For a put, $V \approx 0$. Linear extrapolation from interior points is also common.

### Volatility Boundaries

**At $\sigma = \sigma_{\min}$**: The model reduces to a CEV process with constant volatility $\sigma_{\min}$. The boundary condition is the CEV option price (which can be computed in closed form).

**At $\sigma = \sigma_{\max}$**: For very high volatility, the option price approaches an asymptotic limit. A common choice is linear extrapolation: $\partial^2 V/\partial\sigma^2 = 0$.

!!! warning "Boundary Condition Sensitivity"
    The choice of $\sigma_{\max}$ affects accuracy. If $\sigma_{\max}$ is too small, the boundary condition contaminates the solution at the interior. A rule of thumb is $\sigma_{\max} \geq 3\alpha\exp(\nu\sqrt{T})$, which covers most of the volatility distribution.

---

## ADI Scheme

### Why ADI?

Direct implicit solution of the 2D PDE requires solving a system of $N_F \times N_{\sigma}$ equations at each time step. With $N_F = 200$ and $N_{\sigma} = 50$, this means a system of 10,000 unknowns --- too large for a direct tridiagonal solve.

The **Alternating Direction Implicit** (ADI) method splits the 2D operator into 1D sub-problems, each of which is tridiagonal and can be solved in $O(N)$ time.

### Douglas--Rachford Scheme

The Douglas--Rachford ADI scheme advances from $V^n$ to $V^{n+1}$ in two half-steps:

**Step 1** (implicit in $F$, explicit in $\sigma$ and mixed):

$$
\frac{V^* - V^n}{\Delta t} = \theta\mathcal{L}_F V^* + (1-\theta)\mathcal{L}_F V^n + \mathcal{L}_{\sigma}V^n + \mathcal{L}_{\text{mix}}V^n
$$

This is a tridiagonal system in the $F$ direction for each fixed $\sigma_k$.

**Step 2** (implicit correction in $\sigma$):

$$
\frac{V^{n+1} - V^*}{\Delta t} = \theta(\mathcal{L}_{\sigma}V^{n+1} - \mathcal{L}_{\sigma}V^n)
$$

This is a tridiagonal system in the $\sigma$ direction for each fixed $F_j$.

With $\theta = 1/2$, the scheme is second-order in time ($O(\Delta t^2)$).

### Handling the Mixed Derivative

The mixed derivative $\mathcal{L}_{\text{mix}}$ is treated **explicitly** in both steps. The finite difference stencil for the mixed derivative uses four corner points:

$$
\frac{\partial^2 V}{\partial F\,\partial\sigma}\bigg|_{j,k} \approx \frac{V_{j+1,k+1} - V_{j+1,k-1} - V_{j-1,k+1} + V_{j-1,k-1}}{4\Delta F_j\,\Delta\sigma_k}
$$

On non-uniform grids, the coefficients must be adjusted for the varying grid spacing.

!!! tip "Craig--Sneyd Modification"
    The Craig--Sneyd variant of ADI treats the mixed derivative more carefully, improving stability when $|\rho|$ is large:

    $$
    V^{**} = V^* + \theta\Delta t(\mathcal{L}_{\text{mix}}V^* - \mathcal{L}_{\text{mix}}V^n)
    $$

    This additional half-step adds negligible cost but significantly improves convergence for $|\rho| > 0.5$.

### Hundsdorfer--Verwer Scheme

The Hundsdorfer--Verwer (HV) scheme is a more sophisticated ADI variant that achieves better stability:

**Step 0**: $Y_0 = V^n + \Delta t\,(\mathcal{L}_F + \mathcal{L}_{\sigma} + \mathcal{L}_{\text{mix}})V^n$

**Step 1**: $Y_1 = Y_0 + \theta\Delta t\,(\mathcal{L}_F Y_1 - \mathcal{L}_F V^n)$

**Step 2**: $Y_2 = Y_1 + \theta\Delta t\,(\mathcal{L}_{\sigma} Y_2 - \mathcal{L}_{\sigma} V^n)$

**Step 3**: $\hat{Y}_0 = Y_0 + \frac{1}{2}\Delta t\,[(\mathcal{L}_F + \mathcal{L}_{\sigma} + \mathcal{L}_{\text{mix}})Y_2 - (\mathcal{L}_F + \mathcal{L}_{\sigma} + \mathcal{L}_{\text{mix}})V^n]$

**Step 4**: $V^{n+1}$: Repeat Steps 1--2 with $\hat{Y}_0$ replacing $Y_0$.

With $\theta = 1/2$, HV achieves second-order accuracy and good stability for all $|\rho| < 1$.

---

## Extracting Results

### Option Prices

After time-stepping from $T$ back to $t = 0$, the grid $V^0_{j,k}$ contains option prices at every $(F_j, \sigma_k)$ point. The price at the current state $(F_0, \alpha)$ is obtained by interpolation (typically bicubic) on the grid.

### Implied Volatilities

The Black implied volatility at each strike $K$ is obtained by:

1. Reading $V(0, K, \alpha)$ from the grid (interpolated)
2. Inverting the Black formula: find $\sigma_B$ such that $C_{\text{Black}}(F_0, K, T, \sigma_B) = V(0, K, \alpha)$

This produces the full implied volatility smile in a single PDE solve.

### Greeks

Greeks are computed by finite differences on the grid:

$$
\Delta = \frac{V_{j+1,k_0} - V_{j-1,k_0}}{F_{j+1} - F_{j-1}}, \qquad \Gamma = \frac{V_{j+1,k_0} - 2V_{j_0,k_0} + V_{j-1,k_0}}{(\Delta F)^2}
$$

$$
\mathcal{V} = \frac{V_{j_0,k+1} - V_{j_0,k-1}}{\sigma_{k+1} - \sigma_{k-1}}
$$

This provides all Greeks simultaneously without additional PDE solves.

---

## Comparison with Other Methods

| Feature | FDM (2D PDE) | Hagan Formula | Monte Carlo |
|---------|-------------|---------------|-------------|
| European pricing | Exact (up to grid error) | Approximate ($O(T^2)$) | Exact (statistical error) |
| All strikes at once | Yes | Yes | No (one strike per run) |
| Greeks | Grid differencing | Analytic | Bump-and-reprice |
| American/Bermudan | Yes (early exercise) | No | Yes (regression) |
| Barrier options | Yes (modify boundary) | No | Yes (with bias) |
| Speed (single option) | 0.1--1 s | < 1 ms | 1--10 s |
| Implementation | Complex | Simple | Moderate |

---

## Summary

Finite difference methods solve the 2D SABR pricing PDE on a grid in $(F, \sigma)$ space, producing option prices, implied volatilities, and Greeks across all strikes simultaneously. The computational domain requires non-uniform grids concentrated near the current forward and volatility, with appropriate boundary conditions at the domain edges. The ADI scheme (Douglas--Rachford or Hundsdorfer--Verwer) splits the 2D problem into sequences of tridiagonal 1D solves, with the mixed derivative treated explicitly or semi-implicitly. FDM is the method of choice for American-style options, barrier products, and benchmarking analytical approximations. The main trade-off is implementation complexity versus the speed and simplicity of the Hagan formula.

---

## Further Reading

- Hagan, P. & Woodward, D. (1999). *Equivalent Black volatilities*. Applied Mathematical Finance, 6(3), 147--157.
- Le Floc'h, F. & Kennedy, G. (2014). *Finite difference techniques for arbitrage-free SABR*. Journal of Computational Finance, 17(3), 41--69.
- in 't Hout, K. J. & Foulon, S. (2010). *ADI finite difference schemes for option pricing in the Heston model with correlation*. International Journal of Numerical Analysis and Modeling, 7(2), 303--320.
- Hundsdorfer, W. & Verwer, J. (2003). *Numerical Solution of Time-Dependent Advection-Diffusion-Reaction Equations*. Springer.

---

## Exercises

**Exercise 1.** Starting from the SABR SDE system under the forward measure, derive the 2D pricing PDE:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 F^{2\beta}\frac{\partial^2 V}{\partial F^2} + \rho\nu\sigma^2 F^{\beta}\frac{\partial^2 V}{\partial F\,\partial\sigma} + \frac{1}{2}\nu^2\sigma^2\frac{\partial^2 V}{\partial\sigma^2} = 0
$$

Identify which term arises from each Brownian motion and which term arises from the correlation.

??? success "Solution to Exercise 1"
    The SABR SDE system under the forward measure is:

    $$
    dF_t = \sigma_t F_t^{\beta}\,dW_t^{(1)}, \qquad d\sigma_t = \nu\sigma_t\,dW_t^{(2)}, \qquad d\langle W^{(1)}, W^{(2)}\rangle_t = \rho\,dt
    $$

    There is no drift in either equation because $F_t$ is a martingale under the forward measure and $\sigma_t$ follows driftless geometric Brownian motion.

    Consider a European option with price $V(t, F, \sigma)$. By Ito's lemma applied to the two-dimensional diffusion $(F_t, \sigma_t)$:

    $$
    dV = \frac{\partial V}{\partial t}\,dt + \frac{\partial V}{\partial F}\,dF_t + \frac{\partial V}{\partial \sigma}\,d\sigma_t + \frac{1}{2}\frac{\partial^2 V}{\partial F^2}\,d\langle F\rangle_t + \frac{\partial^2 V}{\partial F\,\partial\sigma}\,d\langle F, \sigma\rangle_t + \frac{1}{2}\frac{\partial^2 V}{\partial\sigma^2}\,d\langle\sigma\rangle_t
    $$

    Computing the quadratic variations and covariation:

    - $d\langle F\rangle_t = \sigma_t^2 F_t^{2\beta}\,dt$ (from $dF_t = \sigma_t F_t^{\beta}\,dW_t^{(1)}$)
    - $d\langle\sigma\rangle_t = \nu^2\sigma_t^2\,dt$ (from $d\sigma_t = \nu\sigma_t\,dW_t^{(2)}$)
    - $d\langle F,\sigma\rangle_t = \sigma_t F_t^{\beta}\cdot\nu\sigma_t\cdot\rho\,dt = \rho\nu\sigma_t^2 F_t^{\beta}\,dt$ (from the correlation between $W^{(1)}$ and $W^{(2)}$)

    Since $V$ must be a martingale under the forward measure (the discounted option price is a martingale), the $dt$ terms must sum to zero:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 F^{2\beta}\frac{\partial^2 V}{\partial F^2} + \rho\nu\sigma^2 F^{\beta}\frac{\partial^2 V}{\partial F\,\partial\sigma} + \frac{1}{2}\nu^2\sigma^2\frac{\partial^2 V}{\partial\sigma^2} = 0
    $$

    Identifying each term:

    - The term $\frac{1}{2}\sigma^2 F^{2\beta}\partial_{FF}V$ arises from the quadratic variation of $F_t$, driven by $W^{(1)}$
    - The term $\frac{1}{2}\nu^2\sigma^2\partial_{\sigma\sigma}V$ arises from the quadratic variation of $\sigma_t$, driven by $W^{(2)}$
    - The **mixed derivative** term $\rho\nu\sigma^2 F^{\beta}\partial_{F\sigma}V$ arises from the cross-variation $d\langle F,\sigma\rangle_t$, which exists because $\text{Corr}(dW^{(1)}, dW^{(2)}) = \rho$. If $\rho = 0$, this term vanishes

---

**Exercise 2.** For the SABR PDE with $\beta = 0.5$, $\nu = 0.4$, $\rho = -0.3$, $\sigma = 0.04$, and $F = 0.035$, compute the three diffusion coefficients: the forward diffusion $\frac{1}{2}\sigma^2 F^{2\beta}$, the mixed term $\rho\nu\sigma^2 F^{\beta}$, and the volatility diffusion $\frac{1}{2}\nu^2\sigma^2$. Which coefficient is largest?

??? success "Solution to Exercise 2"
    Given $\beta = 0.5$, $\nu = 0.4$, $\rho = -0.3$, $\sigma = 0.04$, and $F = 0.035$.

    **Forward diffusion coefficient:**

    $$
    \frac{1}{2}\sigma^2 F^{2\beta} = \frac{1}{2}(0.04)^2(0.035)^{2 \times 0.5} = \frac{1}{2}(0.0016)(0.035)^1 = \frac{1}{2}(0.0016)(0.035) = 2.80 \times 10^{-5}
    $$

    **Mixed derivative coefficient:**

    $$
    \rho\nu\sigma^2 F^{\beta} = (-0.3)(0.4)(0.04)^2(0.035)^{0.5} = (-0.12)(0.0016)(0.18708) = -3.592 \times 10^{-5}
    $$

    Taking the absolute value for comparison: $|\rho\nu\sigma^2 F^{\beta}| \approx 3.59 \times 10^{-5}$.

    **Volatility diffusion coefficient:**

    $$
    \frac{1}{2}\nu^2\sigma^2 = \frac{1}{2}(0.4)^2(0.04)^2 = \frac{1}{2}(0.16)(0.0016) = 1.28 \times 10^{-4}
    $$

    Comparing the three coefficients:

    | Coefficient | Value |
    |---|---|
    | Forward diffusion $\frac{1}{2}\sigma^2 F^{2\beta}$ | $2.80 \times 10^{-5}$ |
    | Mixed term $\lvert\rho\nu\sigma^2 F^{\beta}\rvert$ | $3.59 \times 10^{-5}$ |
    | Volatility diffusion $\frac{1}{2}\nu^2\sigma^2$ | $1.28 \times 10^{-4}$ |

    The **volatility diffusion coefficient** is the largest, by roughly a factor of 3.6 over the mixed term and 4.6 over the forward diffusion. This reflects the fact that with $\nu = 0.4$ (a substantial vol-of-vol) and a relatively small forward $F = 0.035$, the volatility dynamics dominate the forward dynamics. This has practical implications: the grid in the $\sigma$ direction must resolve this larger diffusion coefficient adequately.

---

**Exercise 3.** Explain why the mixed derivative term $\rho\nu\sigma^2 F^{\beta}\partial_{F\sigma}V$ prevents the use of a standard tridiagonal solver on the 2D system. How does the ADI scheme overcome this problem by splitting the operator into 1D sub-problems?

??? success "Solution to Exercise 3"
    A **tridiagonal** system arises when a finite difference scheme couples each grid point only to its immediate neighbors in one spatial direction. For a standard second derivative $\partial_{FF}V$, the central difference stencil at grid point $(j,k)$ involves only $V_{j-1,k}$, $V_{j,k}$, and $V_{j+1,k}$ --- three points along the $F$ direction with $k$ fixed --- producing a tridiagonal matrix when assembled for all $j$.

    The mixed derivative term $\rho\nu\sigma^2 F^{\beta}\partial_{F\sigma}V$ couples the $F$ and $\sigma$ directions simultaneously. Its four-point stencil involves $V_{j+1,k+1}$, $V_{j+1,k-1}$, $V_{j-1,k+1}$, and $V_{j-1,k-1}$. If one attempts a fully implicit discretization of the entire operator (including the mixed derivative), the resulting linear system connects point $(j,k)$ to points that differ in **both** the $j$ and $k$ indices. The bandwidth of the matrix is $O(N_F)$ (or $O(N_\sigma)$), destroying the tridiagonal structure and requiring either a full matrix solve ($O((N_F N_\sigma)^3)$) or iterative methods.

    The **ADI scheme** overcomes this by operator splitting. In Step 1 (implicit in $F$), the $\mathcal{L}_\sigma$ and $\mathcal{L}_{\text{mix}}$ operators are evaluated **explicitly** at the known time level $V^n$. For each fixed $\sigma_k$, the implicit system involves only the $F$-direction derivatives, producing a tridiagonal system of size $N_F$, solved independently for each $k = 1, \ldots, N_\sigma$. In Step 2 (implicit in $\sigma$), the correction involves only $\mathcal{L}_\sigma$, producing a tridiagonal system of size $N_\sigma$ for each fixed $F_j$. The mixed derivative appears only in the explicit terms and never enters the implicit solve, preserving tridiagonal structure at every stage.

    The total cost per time step is $O(N_\sigma \cdot N_F + N_F \cdot N_\sigma) = O(N_F N_\sigma)$, which is linear in the total number of grid points rather than cubic.

---

**Exercise 4.** Write out the four-point stencil for the mixed derivative on a uniform grid:

$$
\frac{\partial^2 V}{\partial F\,\partial\sigma}\bigg|_{j,k} \approx \frac{V_{j+1,k+1} - V_{j+1,k-1} - V_{j-1,k+1} + V_{j-1,k-1}}{4\Delta F\,\Delta\sigma}
$$

Show that this approximation is second-order accurate by expanding each $V_{j\pm1,k\pm1}$ in a Taylor series. How must the formula be modified for a non-uniform grid?

??? success "Solution to Exercise 4"
    **Taylor expansion of the four-point stencil.** Let $h = \Delta F$ and $k = \Delta\sigma$ on a uniform grid. Expand each corner value around $(F_j, \sigma_k)$:

    $$
    V_{j+1,k+1} = V + h V_F + k V_\sigma + \frac{h^2}{2}V_{FF} + hk\,V_{F\sigma} + \frac{k^2}{2}V_{\sigma\sigma} + O(h^3, k^3)
    $$

    $$
    V_{j+1,k-1} = V + h V_F - k V_\sigma + \frac{h^2}{2}V_{FF} - hk\,V_{F\sigma} + \frac{k^2}{2}V_{\sigma\sigma} + O(h^3, k^3)
    $$

    $$
    V_{j-1,k+1} = V - h V_F + k V_\sigma + \frac{h^2}{2}V_{FF} - hk\,V_{F\sigma} + \frac{k^2}{2}V_{\sigma\sigma} + O(h^3, k^3)
    $$

    $$
    V_{j-1,k-1} = V - h V_F - k V_\sigma + \frac{h^2}{2}V_{FF} + hk\,V_{F\sigma} + \frac{k^2}{2}V_{\sigma\sigma} + O(h^3, k^3)
    $$

    Computing the numerator:

    $$
    V_{j+1,k+1} - V_{j+1,k-1} - V_{j-1,k+1} + V_{j-1,k-1}
    $$

    The terms $V$, $hV_F$, $kV_\sigma$, $\frac{h^2}{2}V_{FF}$, and $\frac{k^2}{2}V_{\sigma\sigma}$ all cancel. The surviving leading term is:

    $$
    hk\,V_{F\sigma} + hk\,V_{F\sigma} + hk\,V_{F\sigma} + hk\,V_{F\sigma} = 4hk\,V_{F\sigma}
    $$

    Dividing by $4hk = 4\Delta F\,\Delta\sigma$:

    $$
    \frac{V_{j+1,k+1} - V_{j+1,k-1} - V_{j-1,k+1} + V_{j-1,k-1}}{4\Delta F\,\Delta\sigma} = V_{F\sigma} + O(h^2 + k^2)
    $$

    The error terms arise from third-order and higher contributions in the Taylor expansion (e.g., $\frac{h^2 k}{6}V_{FFF\sigma}$), confirming that the approximation is **second-order accurate** in both $\Delta F$ and $\Delta\sigma$.

    **Non-uniform grid modification.** On a non-uniform grid with spacings $h_j^+ = F_{j+1} - F_j$, $h_j^- = F_j - F_{j-1}$, $k_k^+ = \sigma_{k+1} - \sigma_k$, $k_k^- = \sigma_k - \sigma_{k-1}$, the stencil becomes:

    $$
    \frac{\partial^2 V}{\partial F\,\partial\sigma}\bigg|_{j,k} \approx \frac{1}{(h_j^+ + h_j^-)(k_k^+ + k_k^-)}\left[\frac{h_j^-}{h_j^+}\left(\frac{k_k^-}{k_k^+}V_{j+1,k+1} - \frac{k_k^+}{k_k^-}V_{j+1,k-1}\right) - \frac{h_j^+}{h_j^-}\left(\frac{k_k^-}{k_k^+}V_{j-1,k+1} - \frac{k_k^+}{k_k^-}V_{j-1,k-1}\right)\right]
    $$

    More commonly in practice, the asymmetric spacings are handled by rewriting the four-point stencil with weights that account for the local grid ratios, ensuring the leading-order term still recovers $V_{F\sigma}$ exactly.

---

**Exercise 5.** For a European call under SABR with $F = 3.5\%$, $K = 4.0\%$, $T = 5$Y, discuss the appropriate boundary conditions at (a) $F = 0$, (b) $F = F_{\max}$, (c) $\sigma = \sigma_{\min}$, and (d) $\sigma = \sigma_{\max}$. For the volatility boundaries, explain why the choice of $\sigma_{\max}$ affects the accuracy of the interior solution.

??? success "Solution to Exercise 5"
    For a European call with $F = 3.5\%$, $K = 4.0\%$, $T = 5$Y:

    **(a) At $F = 0$ (for $\beta > 0$):** The diffusion coefficient $\sigma^2 F^{2\beta} \to 0$ as $F \to 0$, so the PDE degenerates. The forward process is absorbed at zero. For a call option, $V(t, 0, \sigma) = 0$ for all $t$ and $\sigma$, since $\max(0 - K, 0) = 0$ and the forward cannot recover once absorbed. This is the **absorbing boundary condition**, consistent with the CEV boundary classification: for $\beta \in (0.5, 1)$, zero is an exit boundary; for $\beta \in (0, 0.5]$, zero is a regular boundary that can be reached and absorbed.

    **(b) At $F = F_{\max}$:** For large $F$, the call is deep in the money and its price approaches the intrinsic value. The boundary condition is:

    $$
    V(t, F_{\max}, \sigma) \approx F_{\max} - K
    $$

    since the forward is already discounted (under the forward measure, no additional discounting is needed for the forward itself). Alternatively, one can impose a **linear extrapolation** condition $\partial^2 V/\partial F^2 = 0$ at $F_{\max}$, which is less restrictive and avoids hardcoding a specific asymptotic form.

    **(c) At $\sigma = \sigma_{\min}$:** When volatility is very small, the stochastic volatility component becomes negligible and the model reduces to a **CEV process** with constant volatility $\sigma_{\min}$. The boundary condition is the CEV option price:

    $$
    V(t, F, \sigma_{\min}) = C_{\text{CEV}}(F, K, T - t, \sigma_{\min}, \beta)
    $$

    which can be computed in closed form using the non-central chi-squared distribution.

    **(d) At $\sigma = \sigma_{\max}$:** For very high volatility, the option price flattens as a function of $\sigma$ (the price approaches $F$ for a call in the extreme case). The boundary condition is typically **linear extrapolation**: $\partial^2 V/\partial\sigma^2 = 0$ at $\sigma_{\max}$.

    **Why $\sigma_{\max}$ affects interior accuracy:** The lognormal volatility process has heavy tails --- there is non-negligible probability that $\sigma_t$ reaches values far above $\alpha$. If $\sigma_{\max}$ is too small, the boundary condition at $\sigma_{\max}$ is applied to states that have significant probability, contaminating the interior solution through the backward propagation of the PDE. The rule of thumb $\sigma_{\max} \geq 3\alpha\exp(\nu\sqrt{T})$ ensures that the probability of $\sigma_t$ exceeding $\sigma_{\max}$ is less than approximately 0.1%, making the boundary condition error negligible. For the given parameters with $T = 5$Y, this can require a substantial domain if $\nu$ is large.

---

**Exercise 6.** Compare the Douglas-Rachford and Hundsdorfer-Verwer ADI schemes. Both achieve second-order accuracy with $\theta = 1/2$. What is the main advantage of the Hundsdorfer-Verwer scheme when $|\rho|$ is large? Estimate the additional computational cost per time step of HV relative to Douglas-Rachford.

??? success "Solution to Exercise 6"
    **Douglas--Rachford (DR)** proceeds in two stages per time step:

    - Step 1: Implicit in $F$, explicit in $\sigma$ and mixed derivative
    - Step 2: Implicit correction in $\sigma$

    The mixed derivative $\mathcal{L}_{\text{mix}}$ is treated entirely explicitly, evaluated at the old time level $V^n$.

    **Hundsdorfer--Verwer (HV)** proceeds in five stages:

    - Step 0: Explicit predictor using all operators at the old time level
    - Step 1: Implicit correction in $F$
    - Step 2: Implicit correction in $\sigma$
    - Step 3: Re-evaluation of the explicit predictor using the corrected solution $Y_2$
    - Step 4: Repeat implicit corrections (Steps 1--2) with the improved predictor

    Both achieve second-order accuracy in time with $\theta = 1/2$.

    **Advantage of HV when $|\rho|$ is large:** The key difference is in the treatment of the mixed derivative. In DR, $\mathcal{L}_{\text{mix}}$ is evaluated only at $V^n$. When $|\rho|$ is large, the mixed derivative coefficient $\rho\nu\sigma^2 F^{\beta}$ becomes comparable to or larger than the pure diffusion coefficients, and the purely explicit treatment introduces stability problems --- oscillations and potential instability for large $\Delta t$.

    In HV, Step 3 re-evaluates all operators (including $\mathcal{L}_{\text{mix}}$) at the corrected solution $Y_2$, and then Steps 1--2 are repeated. This effectively provides a **semi-implicit** treatment of the mixed derivative: the predictor-corrector structure means that the mixed derivative contribution is evaluated at a solution that is closer to $V^{n+1}$, dramatically improving stability. The Craig--Sneyd variant of DR adds one extra half-step for the mixed derivative, but HV's double-sweep structure provides even better stability for $|\rho| > 0.5$.

    **Additional computational cost:** DR requires 2 tridiagonal solves per time step (one of size $N_F$ for each $\sigma_k$, and one of size $N_\sigma$ for each $F_j$), plus one explicit evaluation of $\mathcal{L}_{\text{mix}}$. The total cost is approximately $O(2 N_F N_\sigma)$ plus the explicit evaluation.

    HV requires 4 tridiagonal solves (two sweeps of Steps 1--2) plus 2 explicit evaluations of all operators (Steps 0 and 3). The cost is approximately $O(4 N_F N_\sigma)$ plus the explicit evaluations.

    Therefore, HV costs roughly **twice** as much as DR per time step. However, HV's improved stability often allows larger time steps $\Delta t$, partially or fully compensating for the per-step cost increase. In practice, for $|\rho| > 0.5$, HV with fewer time steps can be more efficient than DR with many time steps needed to maintain stability.

---

**Exercise 7.** After solving the 2D SABR PDE on a grid of $N_F = 200$ forward points and $N_{\sigma} = 50$ volatility points with $N_t = 100$ time steps, describe how to extract: (a) the European call price at the current state $(F_0, \alpha)$, (b) the implied volatility smile across all strikes, and (c) the Greeks $\Delta$, $\Gamma$, and vega. How many PDE solves are required?

??? success "Solution to Exercise 7"
    After solving the PDE from $t = T$ back to $t = 0$, the grid $V^0_{j,k}$ contains the option price at every point $(F_j, \sigma_k)$ at $t = 0$.

    **(a) European call price at $(F_0, \alpha)$:** The current forward $F_0$ and current volatility $\alpha$ generally do not coincide exactly with grid points. The price is obtained by **bicubic interpolation** on the 2D grid: identify the surrounding grid cell $(j_0, k_0)$ such that $F_{j_0} \leq F_0 \leq F_{j_0+1}$ and $\sigma_{k_0} \leq \alpha \leq \sigma_{k_0+1}$, then interpolate using the $4 \times 4$ neighboring points. Since the grid is concentrated near $(F_0, \alpha)$ by the sinh construction, the interpolation error is very small.

    **(b) Implied volatility smile across all strikes:** For each strike $K_i$ in the desired range:

    1. Read $V(0, K_i, \alpha)$ from the grid by interpolation (bilinear or bicubic) at the point $(F = K_i, \sigma = \alpha)$ --- note that the "strike" corresponds to reading the price at $F = K_i$ from the terminal condition perspective, but at $t = 0$, the grid already contains $V^0_{j,k}$ as a function of $(F,\sigma)$. The call price at strike $K_i$ is $V^0(F_0, \alpha)$ computed once, but the **entire smile** comes from the fact that different strikes $K$ appear in the terminal condition. For a single PDE solve with a specific strike $K$, we get only one option price. To get prices at multiple strikes, one can either (i) solve one PDE per strike or (ii) solve the PDE for the full density and integrate. In practice, the standard approach for producing the smile is to solve the PDE once per strike, or use the **forward PDE** (Fokker--Planck) approach to compute the transition density and price all strikes from a single solve.

    2. Invert the Black formula: find $\sigma_B(K_i)$ such that $C_{\text{Black}}(F_0, K_i, T, \sigma_B) = V(0, K_i, \alpha)$, using Newton's method (the Black vega provides the derivative).

    If the **backward PDE** is used with a specific terminal condition for each strike, then one solve per strike is needed. However, the alternative **forward (Fokker--Planck) PDE** produces the transition density $p(F_T | F_0, \alpha)$ from a single solve, from which all strikes can be priced by integration.

    **(c) Greeks $\Delta$, $\Gamma$, and vega:** All are computed from the grid $V^0_{j,k}$ by finite differences at the point nearest $(F_0, \alpha)$, indexed as $(j_0, k_0)$:

    $$
    \Delta = \frac{V_{j_0+1,k_0} - V_{j_0-1,k_0}}{F_{j_0+1} - F_{j_0-1}}
    $$

    $$
    \Gamma = \frac{\frac{V_{j_0+1,k_0} - V_{j_0,k_0}}{F_{j_0+1} - F_{j_0}} - \frac{V_{j_0,k_0} - V_{j_0-1,k_0}}{F_{j_0} - F_{j_0-1}}}{\frac{1}{2}(F_{j_0+1} - F_{j_0-1})}
    $$

    $$
    \mathcal{V} = \frac{V_{j_0,k_0+1} - V_{j_0,k_0-1}}{\sigma_{k_0+1} - \sigma_{k_0-1}}
    $$

    **Number of PDE solves required:** For a single strike, exactly **one** PDE solve produces the price, $\Delta$, $\Gamma$, and vega simultaneously (all from the same grid). For the full implied volatility smile across $M$ strikes using the backward PDE, $M$ solves are needed (one per strike). Using the forward PDE approach, a single solve suffices for all strikes.
