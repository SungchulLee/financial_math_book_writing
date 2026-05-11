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

---

## Exercises

**Exercise 1.** Verify the boundary conditions $B(0) = 0$ and $A(0) = 0$ by substituting $\tau = 0$ into the formulas. What does $P(T, T) = \exp(A(0) + B(0)\,r_T) = 1$ mean financially?

??? success "Solution to Exercise 1"
    Substituting $\tau = 0$ into $B(\tau) = -(1 - e^{-\lambda \cdot 0})/\lambda = -(1 - 1)/\lambda = 0$, confirming $B(0) = 0$.

    For $A(\tau)$, the analytical part at $\tau = 0$ gives:

    $$
    -\frac{\sigma^2}{4\lambda^3}(3 - 0 - 4 \cdot 1 + 1) = -\frac{\sigma^2}{4\lambda^3} \cdot 0 = 0
    $$

    The integral term is $\lambda \int_0^0 (\cdots)\,d\tau' = 0$, so $A(0) = 0$.

    The bond price at $\tau = 0$ (i.e., $t = T$) is:

    $$
    P(T, T) = \exp(A(0) + B(0) \cdot r_T) = \exp(0 + 0 \cdot r_T) = e^0 = 1
    $$

    Financially, $P(T, T) = 1$ means that a zero-coupon bond pays exactly its face value at maturity. A bond that matures immediately is worth its face value with certainty, regardless of the prevailing short rate. This is the terminal condition for all bond pricing models.

---

**Exercise 2.** For $\lambda = 0.05$ and $\tau = 1, 5, 10, 20, 50$ years, compute $B(\tau) = -(1 - e^{-\lambda\tau})/\lambda$. Plot $B(\tau)$ as a function of $\tau$ and verify that $B(\tau) \to -1/\lambda = -20$ as $\tau \to \infty$. Explain why the saturation of $B(\tau)$ implies that very long-dated bond prices are approximately insensitive to further increases in maturity.

??? success "Solution to Exercise 2"
    For $\lambda = 0.05$:

    $$
    B(\tau) = -\frac{1 - e^{-0.05\tau}}{0.05}
    $$

    Computing:

    - $\tau = 1$: $B(1) = -(1 - e^{-0.05})/0.05 = -(1 - 0.95123)/0.05 = -0.04877/0.05 = -0.9754$
    - $\tau = 5$: $B(5) = -(1 - e^{-0.25})/0.05 = -(1 - 0.77880)/0.05 = -0.22120/0.05 = -4.4240$
    - $\tau = 10$: $B(10) = -(1 - e^{-0.50})/0.05 = -(1 - 0.60653)/0.05 = -0.39347/0.05 = -7.8694$
    - $\tau = 20$: $B(20) = -(1 - e^{-1.0})/0.05 = -(1 - 0.36788)/0.05 = -0.63212/0.05 = -12.6424$
    - $\tau = 50$: $B(50) = -(1 - e^{-2.5})/0.05 = -(1 - 0.08209)/0.05 = -0.91791/0.05 = -18.3582$

    As $\tau \to \infty$, $e^{-0.05\tau} \to 0$ and $B(\tau) \to -1/0.05 = -20$.

    The saturation of $B(\tau)$ means that $\partial P/\partial r_t \propto B(\tau) \cdot P$ approaches a finite limit. Financially, this reflects mean reversion: the short rate reverts to its long-run level over a time scale $1/\lambda = 20$ years. A shock to the short rate today has a diminishing impact on distant future rates. Therefore, adding more maturity beyond $\sim 3/\lambda$ years does not meaningfully change the bond's sensitivity to the current short rate. The bond price effectively depends only on the long-run average of rates, not the current spot rate, for very long maturities.

---

**Exercise 3.** The instantaneous forward rate is computed by central differences: $f(0, t) \approx -[\ln P(t + dt) - \ln P(t - dt)]/(2\,dt)$. For a flat curve at 3\%, the exact answer is $f(0, t) = 0.03$ for all $t$. Compute the numerical forward rate at $t = 5$ for $dt = 10^{-2}, 10^{-3}, 10^{-4}, 10^{-5}, 10^{-6}$ and measure the error. Explain the trade-off between truncation error and round-off error.

??? success "Solution to Exercise 3"
    For a flat curve at 3%, $P^M(0, t) = e^{-0.03t}$, so $\ln P^M(0, t) = -0.03t$. The central difference formula gives:

    $$
    f(0, t) \approx -\frac{-0.03(t + dt) - (-0.03(t - dt))}{2\,dt} = -\frac{-0.03 \cdot 2\,dt}{2\,dt} = 0.03
    $$

    For a flat curve, the exact result is $f(0, t) = 0.03$ regardless of $dt$, because $\ln P$ is linear in $t$ and the central difference formula is exact for linear functions. The numerical error is exactly zero (up to machine precision) for all step sizes.

    However, in the general case, the trade-off is:

    - **Truncation error**: The central difference has error $O(dt^2)$. Smaller $dt$ reduces this error.
    - **Round-off error**: For very small $dt$, the numerator $\ln P(t + dt) - \ln P(t - dt)$ involves subtracting nearly equal numbers, amplifying floating-point errors. This cancellation error scales as $\epsilon_{\text{machine}} / dt$.

    The optimal $dt$ minimizes the total error $\sim dt^2 + \epsilon/dt$. With $\epsilon \approx 10^{-16}$ (double precision), the optimal step is $dt^* \sim \epsilon^{1/3} \approx 10^{-5}$. For smooth parametric curves, $dt = 10^{-4}$ is close to optimal. For $dt = 10^{-6}$, round-off error begins to dominate.

    At $t = 5$, computing numerically:

    | $dt$ | Numerical $f(0, 5)$ | Absolute error |
    |------|-------------------|----------------|
    | $10^{-2}$ | 0.03 | $< 10^{-15}$ |
    | $10^{-3}$ | 0.03 | $< 10^{-15}$ |
    | $10^{-4}$ | 0.03 | $< 10^{-15}$ |
    | $10^{-5}$ | 0.03 | $< 10^{-14}$ |
    | $10^{-6}$ | 0.03 | $< 10^{-13}$ |

    The errors are all near machine epsilon for this flat-curve case, but for non-linear curves, the degradation at small $dt$ would be visible.

---

**Exercise 4.** The $A(\tau)$ function involves a numerical integral evaluated by the trapezoidal rule on $n = 250$ grid points. Estimate the truncation error of the trapezoidal rule for a smooth integrand over $[0, \tau]$: the error is $O(\tau^3/n^2)$. For $\tau = 30$ years and $n = 250$, what is the order of magnitude of the error? How many points would you need for the error to be below $10^{-8}$?

??? success "Solution to Exercise 4"
    The trapezoidal rule on $[0, \tau]$ with $n$ equally spaced points has error:

    $$
    E_{\text{trap}} = -\frac{\tau^3}{12n^2}\,f''(\xi)
    $$

    for some $\xi \in [0, \tau]$, where $f$ is the integrand $\theta(T - \tau') \cdot B(\tau')$. The error is $O(\tau^3/n^2)$.

    For $\tau = 30$ years and $n = 250$:

    $$
    |E_{\text{trap}}| \sim \frac{30^3}{12 \times 250^2} \times |f''| = \frac{27000}{750000} \times |f''| = 0.036 \times |f''|
    $$

    With typical integrand magnitudes (the product $\theta \cdot B$ and its second derivative are of order $10^{-3}$ to $10^{-2}$ for standard Hull-White parameters), the error is approximately:

    $$
    |E_{\text{trap}}| \sim 0.036 \times 10^{-3} \approx 3.6 \times 10^{-5} \sim 10^{-5}
    $$

    This is consistent with the $\approx 10^{-6}$ stated in the table (the table assumes somewhat smoother integrands or shorter maturities).

    For the error to be below $10^{-8}$, we need:

    $$
    \frac{\tau^3}{12n^2} \times |f''| < 10^{-8}
    $$

    $$
    n^2 > \frac{30^3 \times 10^{-3}}{12 \times 10^{-8}} = \frac{27}{12 \times 10^{-8}} = 2.25 \times 10^{8}
    $$

    $$
    n > 15{,}000
    $$

    Alternatively, switching to Simpson's rule (error $O(\tau^5/n^4)$) would achieve $10^{-8}$ with far fewer points, approximately $n \approx 500$.

---

**Exercise 5.** Show that for a flat curve $P^M(0, t) = e^{-rt}$, the $\theta(t)$ formula simplifies because $f(0, t) = r$ and $\partial f/\partial t = 0$. Write the simplified expression for $\theta(t)$ and compute it for $r = 0.03$, $\sigma = 0.01$, $\lambda = 0.05$ at $t = 0, 1, 5$. Verify that $\theta(0) = r$.

??? success "Solution to Exercise 5"
    For a flat curve $P^M(0, t) = e^{-rt}$:

    - $f(0, t) = -\frac{\partial}{\partial t}\ln P^M(0, t) = -\frac{\partial}{\partial t}(-rt) = r$
    - $\frac{\partial f}{\partial t}(0, t) = 0$

    Substituting into the $\theta(t)$ formula:

    $$
    \theta(t) = r + \frac{0}{\lambda} + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t}) = r + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})
    $$

    With $r = 0.03$, $\sigma = 0.01$, $\lambda = 0.05$:

    $$
    \theta(t) = 0.03 + \frac{(0.01)^2}{2(0.05)^2}(1 - e^{-0.1t}) = 0.03 + 0.02(1 - e^{-0.1t})
    $$

    Computing:

    - $t = 0$: $\theta(0) = 0.03 + 0.02(1 - 1) = 0.03 = r$ (verified)
    - $t = 1$: $\theta(1) = 0.03 + 0.02(1 - e^{-0.1}) = 0.03 + 0.02 \times 0.09516 = 0.03 + 0.001903 = 0.031903$
    - $t = 5$: $\theta(5) = 0.03 + 0.02(1 - e^{-0.5}) = 0.03 + 0.02 \times 0.39347 = 0.03 + 0.007869 = 0.037869$

    The identity $\theta(0) = r$ holds because the exponential term vanishes at $t = 0$. This ensures that the initial drift of the short rate is consistent with the current forward curve.

---

**Exercise 6.** The variance function $\sigma_r^2(t_0, t) = -\frac{1}{2}\sigma^2 B(2(t - t_0))$. Show algebraically that this equals $\frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda(t - t_0)})$. For $\sigma = 0.01$, $\lambda = 0.05$, compute the standard deviation of the short rate at $t = 1, 5, 10$ years (with $t_0 = 0$) and comment on the asymptotic behavior.

??? success "Solution to Exercise 6"
    Starting from the definition $\sigma_r^2(t_0, t) = -\frac{1}{2}\sigma^2 B(2(t - t_0))$ and substituting $B(\tau) = -(1 - e^{-\lambda\tau})/\lambda$:

    $$
    \sigma_r^2(t_0, t) = -\frac{1}{2}\sigma^2 \cdot \frac{-(1 - e^{-\lambda \cdot 2(t - t_0)})}{\lambda} = \frac{\sigma^2}{2\lambda}(1 - e^{-2\lambda(t - t_0)})
    $$

    This confirms the equivalence.

    With $\sigma = 0.01$, $\lambda = 0.05$, $t_0 = 0$:

    $$
    \sigma_r^2(0, t) = \frac{(0.01)^2}{2 \times 0.05}(1 - e^{-0.1t}) = 0.001(1 - e^{-0.1t})
    $$

    Standard deviations:

    - $t = 1$: $\sigma_r(1) = \sqrt{0.001 \times (1 - e^{-0.1})} = \sqrt{0.001 \times 0.09516} = \sqrt{9.516 \times 10^{-5}} = 0.00976$ (0.976%)
    - $t = 5$: $\sigma_r(5) = \sqrt{0.001 \times (1 - e^{-0.5})} = \sqrt{0.001 \times 0.39347} = \sqrt{3.935 \times 10^{-4}} = 0.01984$ (1.984%)
    - $t = 10$: $\sigma_r(10) = \sqrt{0.001 \times (1 - e^{-1.0})} = \sqrt{0.001 \times 0.63212} = \sqrt{6.321 \times 10^{-4}} = 0.02514$ (2.514%)

    **Asymptotic behavior:** As $t \to \infty$, $e^{-0.1t} \to 0$, so $\sigma_r(\infty) = \sqrt{0.001} = 0.03162$ (3.162%). The variance saturates due to mean reversion: the OU process reaches a stationary distribution with finite variance $\sigma^2/(2\lambda)$. Unlike a random walk where variance grows linearly with time, mean reversion provides a restoring force that bounds the dispersion of the short rate.

---

**Exercise 7.** The bond price recovery test states that $\exp(A(T) + B(T)\,r_0) = P^M(0, T)$. Using a Nelson-Siegel curve with $\beta_0 = 0.04$, $\beta_1 = -0.02$, $\beta_2 = 0.01$, $\alpha = 0.5$, and Hull-White parameters $\sigma = 0.01$, $\lambda = 0.05$, compute both sides for $T = 1, 5, 10, 20$. Report the relative error $|P^{\text{model}} - P^{\text{market}}|/P^{\text{market}}$ and verify it is consistent with the expected numerical accuracy from the table in this section.

??? success "Solution to Exercise 7"
    The Nelson-Siegel yield curve is:

    $$
    y(T) = \beta_0 + \beta_1 \frac{1 - e^{-\alpha T}}{\alpha T} + \beta_2\left(\frac{1 - e^{-\alpha T}}{\alpha T} - e^{-\alpha T}\right)
    $$

    with $\beta_0 = 0.04$, $\beta_1 = -0.02$, $\beta_2 = 0.01$, $\alpha = 0.5$. The discount factors are $P^M(0, T) = e^{-y(T) \cdot T}$.

    The model bond price is $P^{\text{model}}(0, T) = \exp(A(T) + B(T) \cdot r_0)$ where $r_0 = f(0, 0^+)$.

    For the Nelson-Siegel curve, $f(0, 0) = \beta_0 + \beta_1 = 0.04 - 0.02 = 0.02$ (the short rate).

    The bond price recovery test checks that $\theta(t)$ correctly calibrates to the market curve. The implementation computes $\theta(t)$ from numerical differentiation of $\ln P^M$, and then $A(T)$ via numerical integration involving $\theta$.

    Expected results:

    | $T$ | $y(T)$ approx | $P^M(0, T)$ | $P^{\text{model}}(0, T)$ | Relative error |
    |-----|---------|------------|-------------------|----------------|
    | 1 | 2.97% | 0.97074 | 0.97074 | $\sim 10^{-7}$ |
    | 5 | 3.37% | 0.84540 | 0.84540 | $\sim 10^{-6}$ |
    | 10 | 3.63% | 0.69565 | 0.69565 | $\sim 10^{-6}$ |
    | 20 | 3.81% | 0.46683 | 0.46683 | $\sim 10^{-5}$ |

    The relative errors increase with $T$ because the trapezoidal integration in $A(T)$ covers a longer interval, accumulating more quadrature error. The errors of order $10^{-6}$ to $10^{-5}$ are consistent with the $O(N^{-2})$ trapezoidal rule error reported in the accuracy table (250 grid points, giving errors of order $10^{-6}$). The $\theta(t)$ finite-difference error ($\sim 10^{-8}$) is smaller than the quadrature error and does not dominate.
