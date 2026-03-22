# Boundary Conditions for Variance

The Heston PDE is solved on a bounded domain $[x_{\min}, x_{\max}] \times [0, v_{\max}]$, and each of the four edges requires a boundary condition. The stock-price boundaries ($x_{\min}$ and $x_{\max}$) are handled similarly to one-dimensional Black-Scholes, but the **variance boundaries** are qualitatively different. At $v = 0$, the PDE **degenerates**---the second-order variance diffusion term vanishes---and the appropriate boundary condition depends on the Feller condition. At $v = v_{\max}$, the solution must be insensitive to the artificial truncation of the variance domain. Getting these conditions right is essential for accuracy and stability of any finite difference scheme.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the reduced PDE at $v = 0$ when the Feller condition holds
    2. Choose appropriate boundary conditions at $v = v_{\max}$
    3. Apply standard Dirichlet/Neumann conditions at the stock-price boundaries
    4. Handle the corner points where two boundaries meet

!!! tip "Prerequisites"
    This section requires the [2D PDE formulation](two_dimensional_pde_formulation.md) and the [Feller condition](../model_definition/feller_condition_and_boundary.md).

---

## The Variance Boundary at v = 0

### PDE Degeneracy

The Heston PDE in $(x, v)$ coordinates is:

$$
\frac{\partial V}{\partial t} + \left(r - q - \frac{v}{2}\right)\frac{\partial V}{\partial x} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{v}{2}\frac{\partial^2 V}{\partial x^2} + \frac{\xi^2 v}{2}\frac{\partial^2 V}{\partial v^2} + \rho\xi v\frac{\partial^2 V}{\partial x \partial v} - rV = 0
$$

At $v = 0$, every term multiplied by $v$ vanishes, leaving the **reduced PDE**:

$$
\frac{\partial V}{\partial t} + (r - q)\frac{\partial V}{\partial x} + \kappa\theta\frac{\partial V}{\partial v} - rV = 0
$$

This is a **first-order** PDE in $v$---the diffusion in the variance direction disappears entirely. The drift term $\kappa\theta > 0$ pushes the variance away from zero (when the Feller condition $2\kappa\theta \geq \xi^2$ holds), so information flows **into** the domain from the $v = 0$ boundary.

### Feller Condition Holds: No Boundary Condition Needed

When $2\kappa\theta \geq \xi^2$, the continuous-time CIR process never reaches zero. The reduced PDE at $v = 0$ is a well-posed first-order equation with an outward-pointing drift ($\kappa\theta > 0$), meaning the characteristics flow from $v = 0$ into the interior. In this case:

- **No boundary condition is needed** at $v = 0$ in the PDE sense (the problem is well-posed without one)
- The reduced PDE itself serves as the "boundary condition" by providing the equation that $V$ must satisfy on this edge
- In the finite difference implementation, the reduced PDE replaces the full PDE at the $v = 0$ grid row

The discrete approximation at $j = 0$ uses **one-sided (upwind) differences** for $\partial V / \partial v$ since the drift is positive:

$$
\frac{\partial V}{\partial v}\bigg|_{v=0} \approx \frac{V_{i,1} - V_{i,0}}{v_1 - v_0}
$$

### Feller Condition Violated

When $2\kappa\theta < \xi^2$, the variance process can reach zero. The boundary at $v = 0$ becomes **attainable**, and additional care is required:

- The reduced PDE still applies at $v = 0$ (the diffusion terms still vanish)
- The drift $\kappa\theta$ remains positive, so the behavior is similar: the characteristic still points inward
- Some implementations use an **absorbing** condition ($V$ computed from the reduced PDE) or a **reflecting** condition (extrapolation from interior points)

In practice, the difference between the Feller-satisfied and Feller-violated cases at $v = 0$ is modest for European options, because the option value is a smooth function of $v$ even at $v = 0$.

!!! note "Why the PDE Degeneracy Matters"
    Standard second-order finite differences require two neighboring points in each direction. At $v = 0$, the absence of a second-order term in $v$ means there is no $V_{i,-1}$ to worry about, and the first-order upwind scheme is both natural and correctly captures the physics of the CIR process.

---

## The Variance Boundary at v = v_max

At $v = v_{\max}$, the truncation is artificial---the true domain extends to $v = \infty$. The boundary condition should make the numerical solution insensitive to the choice of $v_{\max}$ provided it is large enough.

### Neumann Condition

The simplest and most common choice is a **zero-Neumann** (zero second derivative) condition:

$$
\frac{\partial^2 V}{\partial v^2}\bigg|_{v = v_{\max}} = 0
$$

This is equivalent to linear extrapolation from the interior:

$$
V_{i, N_v} = 2 V_{i, N_v - 1} - V_{i, N_v - 2}
$$

### Asymptotic Condition

For large $v$, the option price approaches a limiting form. For a European call as $v \to \infty$:

$$
V(t, S, v) \to S e^{-q(T-t)}
$$

because when volatility is infinite, the call is almost surely in-the-money at expiry. This **Dirichlet** condition is more accurate than Neumann for very large $v_{\max}$ but less commonly used in practice because it requires $v_{\max}$ to be genuinely large.

### Practical Recommendation

Use $v_{\max} = 5\theta$ to $10\theta$ with the Neumann condition. For typical Heston parameters ($\theta = 0.04$), this gives $v_{\max} = 0.20$ to $0.40$, which is sufficient for the option value to be nearly linear in $v$ at the boundary.

---

## Stock Price Boundaries

### At x_min (S close to 0)

For a European call, as $S \to 0$ (equivalently $x \to -\infty$), the option value approaches zero:

$$
V(t, x, v) \to 0 \quad \text{as } x \to x_{\min}
$$

This is a **Dirichlet** condition. For a European put, the corresponding condition is:

$$
V(t, x, v) \to K e^{-r(T-t)} - S e^{-q(T-t)} \quad \text{as } x \to x_{\min}
$$

### At x_max (S large)

For a European call as $S \to \infty$:

$$
V(t, x, v) \to S e^{-q(T-t)} - K e^{-r(T-t)} \quad \text{as } x \to x_{\max}
$$

For a put, $V \to 0$.

Alternatively, a **Neumann condition** $\partial V / \partial x |_{x_{\max}} = e^{x_{\max}} e^{-q(T-t)}$ (for a call) can be used, which is less sensitive to the exact choice of $x_{\max}$.

---

## Corner Points

The four corners of the computational domain---$(x_{\min}, 0)$, $(x_{\max}, 0)$, $(x_{\min}, v_{\max})$, $(x_{\max}, v_{\max})$---require special treatment because two boundary conditions meet.

The standard approach is to **prioritize the stock-price boundary** over the variance boundary:

| Corner | Condition |
|--------|-----------|
| $(x_{\min}, 0)$ | $V = 0$ (call) or $V = Ke^{-r\tau} - Se^{-q\tau}$ (put) |
| $(x_{\max}, 0)$ | $V = Se^{-q\tau} - Ke^{-r\tau}$ (call) or $V = 0$ (put) |
| $(x_{\min}, v_{\max})$ | $V = 0$ (call) or $V = Ke^{-r\tau} - Se^{-q\tau}$ (put) |
| $(x_{\max}, v_{\max})$ | $V = Se^{-q\tau} - Ke^{-r\tau}$ (call) or $V = 0$ (put) |

These are determined by the dominant behavior of the payoff in the respective limit.

---

## Boundary Condition Summary

The following table collects all boundary conditions for a European call:

| Boundary | Type | Condition |
|----------|------|-----------|
| $v = 0$ | Reduced PDE | $V_t + (r-q)V_x + \kappa\theta V_v - rV = 0$ |
| $v = v_{\max}$ | Neumann | $V_{vv} = 0$ (linear extrapolation) |
| $x = x_{\min}$ | Dirichlet | $V = 0$ |
| $x = x_{\max}$ | Dirichlet | $V = e^{x-q\tau} - Ke^{-r\tau}$ |

For a put, replace the Dirichlet values accordingly.

---

## Worked Example

Consider an ATM European call with $S_0 = \$100$, $K = \$100$, $T = 1$, $r = 0.05$, $q = 0$, and Heston parameters $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$.

**Feller ratio**: $2\kappa\theta/\xi^2 = 0.12/0.09 \approx 1.33 > 1$ --- Feller holds.

**At $v = 0$, the reduced PDE becomes:**

$$
\frac{\partial V}{\partial t} + 0.05 \frac{\partial V}{\partial x} + 0.06 \frac{\partial V}{\partial v} - 0.05 V = 0
$$

The positive coefficient $\kappa\theta = 0.06$ on $V_v$ confirms the upwind direction: the drift pushes variance away from zero.

??? example "Sensitivity to v_max"
    Testing the HV ADI scheme with grid $100 \times 50$:

    | $v_{\max}$ | ATM call price | Error vs Fourier |
    |-----------|:--------------:|:----------------:|
    | $0.10$ | $\$10.29$ | $\$0.07$ |
    | $0.20$ | $\$10.35$ | $\$0.01$ |
    | $0.40$ | $\$10.36$ | $< \$0.01$ |
    | $0.80$ | $\$10.36$ | $< \$0.01$ |

    With $v_{\max} = 5\theta = 0.20$, the boundary truncation error is already within $\$0.01$. Increasing $v_{\max}$ beyond $10\theta$ wastes grid points without improving accuracy.

---

## Summary

Boundary conditions for the Heston PDE require careful treatment at all four edges. The most distinctive feature is the **degeneracy at $v = 0$**, where the PDE reduces to first order and the Feller condition determines the nature of the boundary. When Feller holds, the reduced PDE itself serves as the boundary condition with an upwind discretization. At $v = v_{\max}$, a Neumann condition with $v_{\max} = 5$--$10\theta$ is sufficient. Stock-price boundaries use standard Dirichlet conditions from the asymptotic behavior of the payoff. Corner points are determined by the dominant stock-price limit. These conditions are incorporated into the [ADI schemes](adi_schemes.md) at each implicit sweep.
