# Named Functions Implementation Guide

The Hull-White model's analytical tractability rests on a small set of named functions --- $B(\tau)$, $A(\tau)$, $\theta(t)$, $\psi(t)$, $\sigma_r^2(t)$ --- that appear in bond pricing, simulation, and derivative pricing. This guide explains how the companion Python module `named_functions_implementation.py` translates each formula into code, discusses numerical choices (differentiation, integration, grid resolution), and maps every method to its mathematical definition in the [Named Functions](../named_functions/named_functions_definition.md) reference page.

!!! info "Prerequisites"
    - [Named Functions Definition](../named_functions/named_functions_definition.md) (mathematical formulas)
    - [Hull-White Model Class Guide](hull_white_model_class.md) (class architecture)
    - [Short Rate Solution](../short_rate/short_rate_solution.md) (OU solution for $r_t$)

!!! abstract "Learning Objectives"
    By the end of this guide, you will be able to:

    1. Map each named function formula to its Python implementation
    2. Explain the numerical differentiation scheme used for the instantaneous forward rate $f(0,t)$
    3. Describe how $A(\tau)$ is computed via numerical integration and why analytical shortcuts exist for $B(\tau)$
    4. Validate the implementation against known closed-form results
    5. Identify numerical pitfalls and their mitigations

---

## Function Catalog

The following table lists every named function, its formula, and the corresponding method in the implementation module.

| Function | Formula | Method | Notes |
|----------|---------|--------|-------|
| $B(\tau)$ | $-\frac{1-e^{-\lambda\tau}}{\lambda}$ | `compute_B(tau)` | Analytical; no numerical error |
| $\theta(t)$ | $f(0,t) + \frac{1}{\lambda}\frac{\partial f}{\partial t}(0,t) + \frac{\sigma^2}{2\lambda^2}(1-e^{-2\lambda t})$ | `compute_theta(t)` | Requires numerical differentiation of $\ln P^M$ |
| $A(\tau)$ | See below | `compute_A(tau, T)` | Requires numerical integration |
| $\psi(t)$ | $f(0,t) + \frac{\lambda\sigma^2}{2}B^2(t)$ | `compute_psi(t)` | Analytical given $f(0,t)$ |
| $\sigma_r^2(t_0,t)$ | $-\frac{1}{2}\sigma^2 B(2(t-t_0))$ | `compute_var(t0, t)` | Analytical |

---

## Implementation Details

### B-function

The function $B(\tau) = -(1 - e^{-\lambda\tau})/\lambda$ is implemented directly:

```python
def compute_B(self, tau):
    return -(1.0 - np.exp(-self.lambd * tau)) / self.lambd
```

For $\lambda\tau \ll 1$, the formula is numerically stable because $1 - e^{-x} \approx x$ for small $x$. No special handling is needed unless $\lambda = 0$, which is not a valid Hull-White parameterization.

### Instantaneous forward rate

The forward rate $f(0,t)$ is obtained by numerical differentiation of the market discount curve:

$$
f(0,t) = -\frac{\partial}{\partial t}\ln P^M(0,t)
$$

The implementation uses a central difference scheme:

```python
def compute_f(self, t, dt=1e-4):
    return -(np.log(self.P(t + dt)) - np.log(self.P(t - dt))) / (2 * dt)
```

!!! warning "Forward Rate Sensitivity"
    The forward rate involves differentiating a market curve that may itself be interpolated. The step size `dt` should be small enough for accuracy but large enough to avoid amplifying interpolation noise. A value of $10^{-4}$ works well for smooth parametric curves (Nelson-Siegel, Svensson). For piecewise-linear curves, increase to $10^{-3}$ or use the analytical derivative if available.

### Theta function

The drift function $\theta(t)$ requires both $f(0,t)$ and its derivative $\partial f/\partial t$:

$$
\theta(t) = f(0,t) + \frac{1}{\lambda}\frac{\partial f(0,t)}{\partial t} + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})
$$

The derivative $\partial f/\partial t$ is computed by a second numerical differentiation:

```python
def compute_theta(self, t, dt=1e-4):
    f = self.compute_f(t)
    df_dt = (self.compute_f(t + dt) - self.compute_f(t - dt)) / (2 * dt)
    return f + df_dt / self.lambd + (self.sigma**2 / (2 * self.lambd**2)) * (1 - np.exp(-2 * self.lambd * t))
```

This involves a second-order finite difference of $\ln P^M$. The total truncation error is $O(dt^2)$.

### A-function

The function $A(\tau)$ for bond pricing at time $T - \tau$ involves an integral of $\theta$ weighted by $B$:

$$
A(\tau) = -\frac{\sigma^2}{4\lambda^3}(3 - 2\lambda\tau - 4e^{-\lambda\tau} + e^{-2\lambda\tau}) + \lambda\int_0^{\tau}\theta(T - \tau')B(\tau')\,d\tau'
$$

The first term is analytical. The integral is evaluated by the trapezoidal rule on a uniform grid:

```python
def compute_A(self, tau, T, n_points=250):
    # Analytical part
    lt = self.lambd * tau
    analytic = -(self.sigma**2 / (4 * self.lambd**3)) * (
        3 - 2 * lt - 4 * np.exp(-lt) + np.exp(-2 * lt)
    )
    # Numerical integral
    tau_grid = np.linspace(0, tau, n_points)
    integrand = np.array([
        self.compute_theta(T - tp) * self.compute_B(tp) for tp in tau_grid
    ])
    integral = self.lambd * np.trapz(integrand, tau_grid)
    return analytic + integral
```

!!! tip "Grid Resolution"
    The default 250 points provides accuracy to approximately 6 significant figures for maturities up to 30 years. For pricing applications requiring higher precision (e.g., Greeks by finite differences), increase to 500 or use Simpson's rule.

### Variance and mean functions

The conditional variance $\sigma_r^2(t_0, t)$ and mean $\psi(t)$ are simple combinations of $B$:

```python
def compute_var(self, t0, t):
    return -0.5 * self.sigma**2 * self.compute_B(2 * (t - t0))

def compute_psi(self, t):
    return self.compute_f(t) + 0.5 * self.lambd * self.sigma**2 * self.compute_B(t)**2
```

---

## Validation

### Consistency checks

The named functions satisfy several identities that serve as unit tests:

1. **$B(0) = 0$**: The duration function vanishes at zero tenor
2. **$A(0) = 0$**: The bond price intercept is unity ($P(T,T) = 1$) when $\tau = 0$
3. **$\psi(0) = r(0)$**: The conditional mean at $t = 0$ equals the initial short rate
4. **Bond price recovery**: $P^{\text{model}}(0,T) = \exp(A(T) + B(T)\,r(0))$ should match $P^M(0,T)$ when $\theta(t)$ is calibrated correctly

### Numerical accuracy

| Function | Error source | Typical magnitude |
|----------|-------------|-------------------|
| $B(\tau)$ | Machine precision | $< 10^{-15}$ |
| $f(0,t)$ | Finite difference | $O(dt^2) \approx 10^{-8}$ |
| $\theta(t)$ | Two finite differences | $O(dt^2) \approx 10^{-8}$ |
| $A(\tau)$ | Trapezoidal rule (250 pts) | $O(N^{-2}) \approx 10^{-6}$ |

---

## Summary

| Aspect | Detail |
|--------|--------|
| **Core functions** | $B$, $\theta$, $A$, $\psi$, $\sigma_r^2$ |
| **Analytical** | $B$, $\psi$, $\sigma_r^2$ (given forward rate) |
| **Numerical** | $\theta$ (finite differences), $A$ (quadrature) |
| **Key parameter** | Market discount curve $P^M(0,T)$ drives $\theta$ and $A$ |
| **Validation** | Boundary identities + bond price recovery |

For the full class that wraps these functions into a pricing engine, see the [Hull-White Model Class Guide](hull_white_model_class.md). For the derivative pricing methods that use $A$ and $B$, see [Bond and Derivative Pricing Classes Guide](bond_derivative_pricing_classes.md).
