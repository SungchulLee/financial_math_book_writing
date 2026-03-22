# Milstein Scheme for the Heston Model

The Euler-Maruyama scheme achieves strong convergence order $\frac{1}{2}$, which means halving the time step only reduces the pathwise error by a factor of $\sqrt{2}$. The **Milstein scheme** adds a correction term derived from the Ito-Taylor expansion that captures the curvature of the diffusion coefficient, boosting the strong convergence order to 1 for scalar SDEs. Applying Milstein to the Heston model, however, reveals a subtle obstacle: the two-dimensional correlated system requires simulation of the **Levy area**, which is computationally expensive and difficult to implement correctly.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the Milstein correction term from the Ito-Taylor expansion for a scalar SDE
    2. Apply the Milstein scheme to the CIR variance process with its square-root diffusion
    3. Explain the Levy area problem that arises in correlated multi-dimensional SDEs
    4. Assess when Milstein offers a practical advantage over Euler for Heston simulation

!!! tip "Prerequisites"
    This section builds on the [Euler discretization](euler_discretization_and_pitfalls.md) and the [CIR variance process](../variance_dynamics/cir_variance_process_solution.md).

---

## The Ito-Taylor Expansion

To understand the Milstein correction, consider a generic scalar SDE:

$$
dY_t = a(Y_t) \, dt + b(Y_t) \, dW_t
$$

The Euler-Maruyama scheme approximates the increment over $[t_n, t_{n+1}]$ by freezing the coefficients at $t_n$:

$$
Y_{n+1}^{\text{Euler}} = Y_n + a(Y_n) \Delta t + b(Y_n) \Delta W_n
$$

The **Ito-Taylor expansion** of $b(Y_t)$ around $Y_n$ gives the next-order correction. Applying Ito's formula to $b(Y_t)$:

$$
b(Y_t) = b(Y_n) + \int_{t_n}^{t} b'(Y_s) b(Y_s) \, dW_s + \text{higher order terms}
$$

Substituting this into the stochastic integral $\int_{t_n}^{t_{n+1}} b(Y_t) \, dW_t$ and retaining the leading correction yields the **Milstein scheme**:

$$
Y_{n+1} = Y_n + a(Y_n) \Delta t + b(Y_n) \Delta W_n + \frac{1}{2} b(Y_n) b'(Y_n) \left[ (\Delta W_n)^2 - \Delta t \right]
$$

The additional term $\frac{1}{2} b(Y_n) b'(Y_n) [(\Delta W_n)^2 - \Delta t]$ is the **Milstein correction**. It captures the leading nonlinear effect of the diffusion and improves the strong convergence order from $\frac{1}{2}$ to $1$.

---

## Milstein Applied to the CIR Variance Process

The CIR variance process in the Heston model has the form:

$$
dv_t = \kappa(\theta - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^{(2)}
$$

Here the drift is $a(v) = \kappa(\theta - v)$ and the diffusion is $b(v) = \xi\sqrt{v}$. The derivative of the diffusion coefficient is:

$$
b'(v) = \frac{\xi}{2\sqrt{v}}
$$

The Milstein correction term becomes:

$$
\frac{1}{2} b(v_n) b'(v_n) = \frac{1}{2} \cdot \xi\sqrt{v_n} \cdot \frac{\xi}{2\sqrt{v_n}} = \frac{\xi^2}{4}
$$

This is remarkably simple: the correction is a **constant** independent of $v_n$. The full Milstein update for the variance is:

$$
v_{n+1} = v_n + \kappa(\theta - v_n) \Delta t + \xi\sqrt{v_n^+} \, \Delta W_n^{(2)} + \frac{\xi^2}{4}\left[(\Delta W_n^{(2)})^2 - \Delta t\right]
$$

where $v_n^+ = \max(v_n, 0)$ applies the full truncation fix from the Euler section.

!!! note "The Constant Correction"
    The fact that $b(v)b'(v) = \xi^2/2$ is constant for the CIR process is special. For most nonlinear diffusions, the Milstein correction depends on the current state. This simplification makes Milstein particularly easy to implement for CIR-type processes.

---

## Milstein for the Log-Price Process

The log-price process $x_t = \ln S_t$ satisfies:

$$
dx_t = \left(r - q - \tfrac{1}{2} v_t\right) dt + \sqrt{v_t} \, dW_t^{(1)}
$$

Here the diffusion is $b(x, v) = \sqrt{v}$, which depends on $v$ rather than $x$. Since $\partial b / \partial x = 0$, the Milstein correction in the $x$-direction vanishes. The log-price update is:

$$
x_{n+1} = x_n + \left(r - q - \tfrac{1}{2} v_n^+\right) \Delta t + \sqrt{v_n^+} \, \Delta W_n^{(1)}
$$

This is identical to the Euler update. The Milstein improvement for the Heston model concentrates entirely in the variance equation.

---

## The Levy Area Problem

### Why Multi-Dimensional Milstein Is Hard

For a system of SDEs driven by correlated Brownian motions, the full Milstein scheme requires not only the increments $\Delta W^{(1)}$ and $\Delta W^{(2)}$ but also the **Levy area** (or iterated stochastic integral):

$$
A_{n} = \int_{t_n}^{t_{n+1}} \int_{t_n}^{s} dW_u^{(1)} \, dW_s^{(2)} - \int_{t_n}^{t_{n+1}} \int_{t_n}^{s} dW_u^{(2)} \, dW_s^{(1)}
$$

This double integral measures the "area" swept by the two-dimensional Brownian path and captures the cross-interaction between the two noise sources. When $\rho \neq 0$, the Levy area has a non-trivial distribution that cannot be expressed in closed form in terms of $\Delta W^{(1)}$ and $\Delta W^{(2)}$ alone.

### Consequences for Convergence

Without simulating the Levy area, the Milstein scheme for the correlated 2D Heston system does **not** achieve strong order 1 in general. The achievable convergence orders are:

| Component | With Levy Area | Without Levy Area |
|-----------|---------------|-------------------|
| Variance (1D Milstein) | Strong order 1 | Strong order 1 |
| Full 2D system | Strong order 1 | Strong order $\frac{1}{2}$ |

The variance equation alone benefits from the Milstein correction (strong order 1), because it is a scalar SDE in $v$ driven by a single Brownian motion $W^{(2)}$. The cross-coupling through $\rho$ only affects the joint simulation of $(x, v)$.

### Practical Implications

Simulating the Levy area accurately requires either:

1. **Truncated Fourier series** approximations (Wiktorsson, 2001), which add $\mathcal{O}(p)$ operations per step for $p$ Fourier terms
2. **Exact sampling** methods that are computationally expensive

For most practical purposes, the improvement from strong order $\frac{1}{2}$ to strong order 1 in the joint system does not justify the cost of Levy area simulation. This is a key reason why practitioners prefer the [QE scheme](quadratic_exponential_scheme.md) or [exact simulation](exact_simulation_broadie_kaya.md), which achieve near-exact accuracy without Ito-Taylor corrections.

!!! warning "When Milstein Without Levy Area Helps"
    Even without the Levy area, applying the Milstein correction to the variance process alone can reduce pricing bias compared to pure Euler. The variance is the "difficult" component (non-Lipschitz diffusion), and improving its simulation accuracy benefits the overall price estimate. The log-price equation, being linear in $x$, is already well-handled by Euler.

---

## Convergence Comparison

The following table summarizes the convergence properties of Euler and Milstein for the Heston model:

| Property | Euler (Full Truncation) | Milstein (Variance Only) | Milstein (Full 2D + Levy) |
|----------|------------------------|--------------------------|---------------------------|
| Weak order | 1 | 1 | 1 |
| Strong order (variance) | $\frac{1}{2}$ | 1 | 1 |
| Strong order (joint) | $\frac{1}{2}$ | $\frac{1}{2}$ | 1 |
| Cost per step | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(p)$ |
| Implementation | Simple | Simple | Complex |

For **weak convergence** (relevant to option pricing), both Euler and Milstein achieve order 1, so the pricing accuracy improvement from Milstein is modest. The main benefit of Milstein is in **strong convergence** for path-dependent payoffs where individual path accuracy matters.

---

## Worked Example

Consider the Heston parameters from the Euler section:

| Parameter | Value |
|-----------|-------|
| $v_0$ | $0.04$ |
| $\kappa$ | $1.5$ |
| $\theta$ | $0.04$ |
| $\xi$ | $0.3$ |
| $\Delta t$ | $1/252$ |

**Single Milstein step for variance**: Suppose $v_n = 0.04$ and draw $Z_2 = -1.5$ (a moderately negative shock). Then $\Delta W^{(2)} = \sqrt{1/252} \cdot (-1.5) \approx -0.0945$.

**Euler update:**

$$
v_{n+1}^{\text{Euler}} = 0.04 + 1.5(0.04 - 0.04)(1/252) + 0.3\sqrt{0.04}(-0.0945) \approx 0.04 - 0.00567 = 0.03433
$$

**Milstein update:**

$$
v_{n+1}^{\text{Milstein}} = 0.03433 + \frac{0.09}{4}\left[(-0.0945)^2 - \frac{1}{252}\right] \approx 0.03433 + 0.0225(0.00893 - 0.00397) \approx 0.03444
$$

The Milstein correction adds approximately $0.00011$ to the variance, partially compensating for the downward shock. Over many steps, these corrections accumulate to reduce the strong error significantly.

??? example "Convergence Rate Verification"
    To verify the convergence orders empirically, simulate $M$ paths with step sizes $\Delta t \in \{1/50, 1/100, 1/200, 1/400\}$:

    1. For each $\Delta t$, compute the variance at $T = 1$ using both Euler and Milstein
    2. Use a very fine grid ($\Delta t = 1/10000$) as the "exact" reference
    3. Compute the strong error: $\varepsilon(\Delta t) = \left(\frac{1}{M}\sum_{m=1}^{M}|v_N^{(m)} - v_{\text{ref}}^{(m)}|^2\right)^{1/2}$
    4. Plot $\log \varepsilon$ vs $\log \Delta t$: Euler gives slope $\approx 0.5$; Milstein (variance only) gives slope $\approx 1.0$

---

## Summary

The Milstein scheme improves the strong convergence order of the CIR variance discretization from $\frac{1}{2}$ to 1 by adding the correction term $\frac{\xi^2}{4}[(\Delta W)^2 - \Delta t]$, which is constant for the square-root diffusion. For the log-price equation, the Milstein correction vanishes because the diffusion does not depend on $x$. The correlated two-dimensional Heston system requires the Levy area for full strong order 1 convergence, which is expensive to simulate. In practice, applying Milstein to the variance process alone (without the Levy area) offers a modest improvement over Euler at negligible additional cost. For substantially better accuracy, the [QE scheme](quadratic_exponential_scheme.md) and [exact simulation](exact_simulation_broadie_kaya.md) are preferred.
