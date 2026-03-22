# Finite Difference Methods for the PIDE

Under jump-diffusion dynamics, the standard Black-Scholes PDE acquires an **integral term** that accounts for the nonlocal effect of jumps. The resulting equation is a **partial integro-differential equation** (PIDE). Numerical solution of the PIDE extends finite difference methods from classical PDEs by discretizing this integral term, typically using an **implicit-explicit (IMEX) splitting** that treats the differential part implicitly (for stability) and the integral part explicitly (for efficiency).

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the PIDE for European option pricing under Merton jump-diffusion
    2. Discretize the integral term using quadrature on a finite grid
    3. Implement the implicit-explicit (IMEX) time-stepping scheme
    4. Analyze stability and convergence of the resulting numerical method

---

## Derivation of the PIDE

### From Hedging to the Pricing Equation

Consider a portfolio consisting of an option $V(t, S)$ and $-\Delta$ shares of stock. Between jumps, the standard delta-hedging argument yields the Black-Scholes PDE terms. At a jump time, the stock price changes from $S$ to $SY$, and the option value changes from $V(t, S)$ to $V(t, SY)$. The expected change in option value from jumps, per unit time, is:

$$
\lambda\int_0^{\infty}[V(t, Sy) - V(t, S)]g(y)\,dy
$$

where $g(y)$ is the density of the jump multiplier $Y$ and $\lambda$ is the jump intensity.

### The PIDE

!!! info "Theorem: Merton PIDE"
    Under the risk-neutral measure, the price $V(t, S)$ of a European option satisfies

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} + (r - \lambda\bar{k})S\frac{\partial V}{\partial S} - (r + \lambda)V + \lambda\int_0^{\infty}V(t, Sy)g(y)\,dy = 0
    $$

    with terminal condition $V(T, S) = \Phi(S)$ (the payoff).

The equation can be rewritten by separating the $-\lambda V$ term:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 V_{SS} + (r - \lambda\bar{k})SV_S - rV + \lambda\!\int_0^{\infty}\!\bigl[V(t, Sy) - V(t, S)\bigr]g(y)\,dy = 0
$$

This form shows the structure: the first four terms are the Black-Scholes PDE (with modified drift), and the integral term is the **jump correction**.

### Change to Log-Price Variable

For numerical implementation, the change of variable $x = \ln S$ simplifies the equation. Setting $v(t, x) = V(t, e^x)$:

$$
\frac{\partial v}{\partial t} + \frac{1}{2}\sigma^2\frac{\partial^2 v}{\partial x^2} + \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)\frac{\partial v}{\partial x} - (r + \lambda)v + \lambda\!\int_{-\infty}^{\infty}\!v(t, x + y)f(y)\,dy = 0
$$

where $f(y)$ is the density of $\ln Y \sim N(\mu_J, \sigma_J^2)$.

!!! tip "Convolution Structure"
    The integral term $\int v(t, x+y)f(y)\,dy$ is a convolution $v * f$ evaluated at $x$. This structure can be exploited using the FFT for efficient computation: $(v * f)(x) = \mathcal{F}^{-1}[\mathcal{F}(v) \cdot \mathcal{F}(f)]$.

---

## Spatial Discretization

### The Grid

Choose a computational domain $[x_{\min}, x_{\max}]$ with $x_{\min} = \ln S_0 - L$ and $x_{\max} = \ln S_0 + L$ for some $L > 0$ (typically $L = 5\sigma\sqrt{T}$ to $10\sigma\sqrt{T}$). Introduce a uniform grid:

$$
x_j = x_{\min} + j\,\Delta x, \quad j = 0, 1, \ldots, J, \quad \Delta x = \frac{x_{\max} - x_{\min}}{J}
$$

Let $v_j^k \approx v(t_k, x_j)$ denote the numerical approximation at grid point $(t_k, x_j)$.

### Differential Part

The second derivative and first derivative are discretized using standard central differences:

$$
\frac{\partial^2 v}{\partial x^2}\bigg|_{x_j} \approx \frac{v_{j+1} - 2v_j + v_{j-1}}{\Delta x^2}
$$

$$
\frac{\partial v}{\partial x}\bigg|_{x_j} \approx \frac{v_{j+1} - v_{j-1}}{2\Delta x}
$$

This yields a tridiagonal matrix for the differential operator.

### Integral Part

The integral $I_j = \lambda\int_{-\infty}^{\infty}v(t, x_j + y)f(y)\,dy$ is approximated by quadrature. Since $f(y)$ is the $N(\mu_J, \sigma_J^2)$ density, the integrand decays rapidly and can be truncated to $[y_{\min}, y_{\max}]$ with $y_{\min} = \mu_J - 5\sigma_J$ and $y_{\max} = \mu_J + 5\sigma_J$.

**Trapezoidal rule:**

$$
I_j \approx \lambda\sum_{l=0}^{L_q}\omega_l\,v(t, x_j + y_l)\,f(y_l)
$$

where $\{y_l, \omega_l\}$ are the quadrature nodes and weights. The values $v(t, x_j + y_l)$ at non-grid points are obtained by **linear interpolation** from the grid values $\{v_j\}$.

**FFT-based approach:** Alternatively, evaluate the convolution on the full grid using:

$$
I_j \approx \lambda\Delta x\sum_{l}v_{j+l}\,f(x_l)
$$

computed via FFT in $O(J\log J)$ operations.

---

## Time Discretization: IMEX Splitting

### Motivation for Splitting

The differential part of the PIDE produces a tridiagonal linear system when treated implicitly, which is solved in $O(J)$ operations. The integral part couples all grid points, producing a dense matrix. Treating it implicitly would require solving a dense $J \times J$ system at each time step, which is prohibitively expensive.

The IMEX strategy resolves this: treat the **differential part implicitly** (Crank-Nicolson or backward Euler) for unconditional stability, and the **integral part explicitly** (forward Euler) for efficiency.

### The IMEX Scheme

Define the operators:

- $\mathcal{D}$: differential part (tridiagonal)
- $\mathcal{I}$: integral part (dense)

The backward-in-time stepping from $t_{k+1}$ to $t_k$ (with $\Delta t = T/N_t$):

!!! info "Algorithm: IMEX Scheme"
    $$
    \frac{v^k - v^{k+1}}{\Delta t} + \theta\mathcal{D}v^k + (1-\theta)\mathcal{D}v^{k+1} + \mathcal{I}v^{k+1} = 0
    $$

    Rearranging:

    $$
    (I - \theta\Delta t\,\mathcal{D})v^k = (I + (1-\theta)\Delta t\,\mathcal{D})v^{k+1} + \Delta t\,\mathcal{I}v^{k+1}
    $$

    For $\theta = 1$ (backward Euler) or $\theta = 1/2$ (Crank-Nicolson).

At each time step:

1. Compute $\mathcal{I}v^{k+1}$ explicitly using the known solution at $t_{k+1}$ (cost: $O(J\log J)$ via FFT or $O(J \cdot L_q)$ via direct quadrature)
2. Form the right-hand side $b = (I + (1-\theta)\Delta t\,\mathcal{D})v^{k+1} + \Delta t\,\mathcal{I}v^{k+1}$
3. Solve the tridiagonal system $(I - \theta\Delta t\,\mathcal{D})v^k = b$ (cost: $O(J)$)

### Boundary Conditions

At the boundaries of the log-price grid:

- **Far below** ($x \to x_{\min}$): For a call, $V \to 0$, so $v(t, x_{\min}) = 0$
- **Far above** ($x \to x_{\max}$): For a call, $V \approx Se^{-\lambda\bar{k}T} - Ke^{-rT}$, approximated by the intrinsic value or a linear extrapolation

For put options, the roles are reversed.

---

## Stability and Convergence

### Stability of the IMEX Scheme

!!! info "Proposition: Stability Condition"
    The IMEX scheme with implicit differential and explicit integral is stable provided:

    $$
    \Delta t \leq \frac{C}{\lambda}
    $$

    for a constant $C$ that depends on the quadrature weights. In practice, this is a mild restriction since $\lambda$ is typically $O(1)$, allowing $\Delta t$ on the order of $1/\lambda$.

The implicit treatment of the diffusion term removes the parabolic CFL condition $\Delta t \leq \Delta x^2/(2\sigma^2)$ that would otherwise restrict the time step severely.

### Convergence

For smooth payoffs, the IMEX scheme with Crank-Nicolson achieves:

- $O(\Delta x^2)$ spatial convergence (from central differences)
- $O(\Delta t^2)$ temporal convergence (from Crank-Nicolson)
- $O(\Delta y^2)$ quadrature convergence (from trapezoidal rule with smooth integrand)

For non-smooth payoffs (e.g., calls and puts with a kink at $K$), the convergence degrades to $O(\Delta x)$ near the strike unless the grid is aligned with the kink or a smoothing technique is applied.

---

## Comparison with Other Methods

| Method | European | Path-dependent | American | Complexity per price |
|--------|----------|----------------|----------|---------------------|
| Merton series | Exact | No | No | $O(n_{\max})$ |
| FFT/Fourier | Fast | No | No | $O(N\log N)$ |
| Monte Carlo | $O(1/\sqrt{M})$ | Yes | Via LSM | $O(MN)$ |
| PIDE (IMEX) | $O(\Delta x^2, \Delta t^2)$ | Limited | Yes | $O(N_t J\log J)$ |

The PIDE approach is particularly valuable for:

- **American options**: The free boundary condition is naturally incorporated through the penalty method or PSOR
- **Barrier options**: Grid-based methods handle barriers more naturally than Monte Carlo
- **Moderate dimensions**: Efficient for one-asset problems; multi-asset PIDEs face the curse of dimensionality

---

## Worked Example

!!! example "PIDE Setup for European Put"
    **Parameters:** $S_0 = \$100$, $K = \$100$, $T = 0.5$, $r = 0.05$, $\sigma = 0.20$, $\lambda = 1.0$, $\mu_J = -0.08$, $\sigma_J = 0.25$.

    **Grid specification:**

    - Log-price domain: $x \in [\ln 100 - 3, \ln 100 + 3] = [1.605, 7.605]$ (covers $S \in [\$5, \$2{,}000]$)
    - Grid points: $J = 200$, so $\Delta x = 0.03$
    - Time steps: $N_t = 100$, so $\Delta t = 0.005$
    - Quadrature: 50 points on $[\mu_J - 5\sigma_J, \mu_J + 5\sigma_J] = [-1.33, 1.17]$

    **Terminal condition:**

    $$
    v^{N_t}_j = \max(K - e^{x_j}, 0)
    $$

    **Stability check:** $\Delta t \cdot \lambda = 0.005 \times 1.0 = 0.005 \ll 1$ (well within stability bounds).

    **Result:** The PIDE solution converges to the Merton series price \$4.91 as the grid is refined, with a Richardson-extrapolated error below $10^{-4}$ at the specified resolution.

---

## Summary

The partial integro-differential equation for Merton jump-diffusion pricing combines the standard Black-Scholes PDE with an integral term representing the expected option value change from jumps. The change to log-price coordinates reveals the convolution structure of the integral, enabling FFT-based evaluation. The IMEX splitting treats the tridiagonal differential part implicitly and the dense integral part explicitly, achieving unconditional stability for the diffusion component with only a mild CFL-like restriction from the jump intensity. The resulting scheme has $O(\Delta x^2, \Delta t^2)$ convergence for smooth payoffs and extends naturally to American options and barrier options through penalty methods and grid alignment.
