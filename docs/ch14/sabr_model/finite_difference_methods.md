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

---

**Exercise 2.** For the SABR PDE with $\beta = 0.5$, $\nu = 0.4$, $\rho = -0.3$, $\sigma = 0.04$, and $F = 0.035$, compute the three diffusion coefficients: the forward diffusion $\frac{1}{2}\sigma^2 F^{2\beta}$, the mixed term $\rho\nu\sigma^2 F^{\beta}$, and the volatility diffusion $\frac{1}{2}\nu^2\sigma^2$. Which coefficient is largest?

---

**Exercise 3.** Explain why the mixed derivative term $\rho\nu\sigma^2 F^{\beta}\partial_{F\sigma}V$ prevents the use of a standard tridiagonal solver on the 2D system. How does the ADI scheme overcome this problem by splitting the operator into 1D sub-problems?

---

**Exercise 4.** Write out the four-point stencil for the mixed derivative on a uniform grid:

$$
\frac{\partial^2 V}{\partial F\,\partial\sigma}\bigg|_{j,k} \approx \frac{V_{j+1,k+1} - V_{j+1,k-1} - V_{j-1,k+1} + V_{j-1,k-1}}{4\Delta F\,\Delta\sigma}
$$

Show that this approximation is second-order accurate by expanding each $V_{j\pm1,k\pm1}$ in a Taylor series. How must the formula be modified for a non-uniform grid?

---

**Exercise 5.** For a European call under SABR with $F = 3.5\%$, $K = 4.0\%$, $T = 5$Y, discuss the appropriate boundary conditions at (a) $F = 0$, (b) $F = F_{\max}$, (c) $\sigma = \sigma_{\min}$, and (d) $\sigma = \sigma_{\max}$. For the volatility boundaries, explain why the choice of $\sigma_{\max}$ affects the accuracy of the interior solution.

---

**Exercise 6.** Compare the Douglas-Rachford and Hundsdorfer-Verwer ADI schemes. Both achieve second-order accuracy with $\theta = 1/2$. What is the main advantage of the Hundsdorfer-Verwer scheme when $|\rho|$ is large? Estimate the additional computational cost per time step of HV relative to Douglas-Rachford.

---

**Exercise 7.** After solving the 2D SABR PDE on a grid of $N_F = 200$ forward points and $N_{\sigma} = 50$ volatility points with $N_t = 100$ time steps, describe how to extract: (a) the European call price at the current state $(F_0, \alpha)$, (b) the implied volatility smile across all strikes, and (c) the Greeks $\Delta$, $\Gamma$, and vega. How many PDE solves are required?
