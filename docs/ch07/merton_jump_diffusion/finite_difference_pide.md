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

---

## Exercises

**Exercise 1.** Starting from the Merton PIDE in the original price variable $S$, perform the change of variable $x = \ln S$, $v(t,x) = V(t, e^x)$ to derive the log-price PIDE. Verify that the drift coefficient becomes $r - \lambda\bar{k} - \frac{1}{2}\sigma^2$ and that the integral term becomes a convolution $\lambda\int v(t, x+y)\,f(y)\,dy$ where $f$ is the $N(\mu_J, \sigma_J^2)$ density.

??? success "Solution to Exercise 1"
    Starting from the PIDE in the original variable $S$:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} + (r - \lambda\bar{k})S\frac{\partial V}{\partial S} - (r+\lambda)V + \lambda\int_0^{\infty}V(t, Sy)g(y)\,dy = 0
    $$

    Set $x = \ln S$, so $S = e^x$ and $v(t, x) = V(t, e^x)$. Compute the derivatives using the chain rule:

    $$
    \frac{\partial V}{\partial S} = \frac{1}{S}\frac{\partial v}{\partial x}, \qquad \frac{\partial^2 V}{\partial S^2} = \frac{1}{S^2}\left(\frac{\partial^2 v}{\partial x^2} - \frac{\partial v}{\partial x}\right)
    $$

    Substituting into the PDE terms:

    $$
    \frac{1}{2}\sigma^2 S^2 \cdot \frac{1}{S^2}\left(\frac{\partial^2 v}{\partial x^2} - \frac{\partial v}{\partial x}\right) + (r - \lambda\bar{k})S \cdot \frac{1}{S}\frac{\partial v}{\partial x} = \frac{1}{2}\sigma^2\frac{\partial^2 v}{\partial x^2} + \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)\frac{\partial v}{\partial x}
    $$

    For the integral term, substitute $Sy = e^{x+\ln y}$. Setting $z = \ln y$, we have $y = e^z$, $dy = e^z\,dz$, and $g(y)\,dy = f(z)\,dz$ where $f(z)$ is the density of $\ln Y \sim N(\mu_J, \sigma_J^2)$. Therefore:

    $$
    \lambda\int_0^{\infty}V(t, Sy)g(y)\,dy = \lambda\int_{-\infty}^{\infty}v(t, x + z)f(z)\,dz
    $$

    The complete log-price PIDE is:

    $$
    \frac{\partial v}{\partial t} + \frac{1}{2}\sigma^2\frac{\partial^2 v}{\partial x^2} + \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)\frac{\partial v}{\partial x} - (r+\lambda)v + \lambda\int_{-\infty}^{\infty}v(t, x+z)f(z)\,dz = 0
    $$

    The drift coefficient is indeed $r - \lambda\bar{k} - \frac{1}{2}\sigma^2$, and the integral is a convolution $\lambda(v * f)(x)$.

---


**Exercise 2.** Consider the spatial discretization of the differential part on a uniform grid with spacing $\Delta x$. Write down the tridiagonal matrix $A$ that represents the discrete operator $\frac{1}{2}\sigma^2 \frac{v_{j+1} - 2v_j + v_{j-1}}{\Delta x^2} + \alpha\frac{v_{j+1} - v_{j-1}}{2\Delta x} - (r+\lambda)v_j$ where $\alpha = r - \lambda\bar{k} - \frac{1}{2}\sigma^2$. Express the sub-diagonal, diagonal, and super-diagonal entries in terms of $\sigma$, $\alpha$, $r$, $\lambda$, and $\Delta x$.

??? success "Solution to Exercise 2"
    Define $\alpha = r - \lambda\bar{k} - \frac{1}{2}\sigma^2$. The discrete operator at grid point $j$ is:

    $$
    \mathcal{D}v_j = \frac{\sigma^2}{2}\frac{v_{j+1} - 2v_j + v_{j-1}}{\Delta x^2} + \alpha\frac{v_{j+1} - v_{j-1}}{2\Delta x} - (r+\lambda)v_j
    $$

    Collecting coefficients of $v_{j-1}$, $v_j$, and $v_{j+1}$:

    **Sub-diagonal** (coefficient of $v_{j-1}$):

    $$
    a = \frac{\sigma^2}{2\Delta x^2} - \frac{\alpha}{2\Delta x}
    $$

    **Diagonal** (coefficient of $v_j$):

    $$
    b = -\frac{\sigma^2}{\Delta x^2} - (r + \lambda)
    $$

    **Super-diagonal** (coefficient of $v_{j+1}$):

    $$
    c = \frac{\sigma^2}{2\Delta x^2} + \frac{\alpha}{2\Delta x}
    $$

    The tridiagonal matrix $A$ has $a$ on the sub-diagonal, $b$ on the main diagonal, and $c$ on the super-diagonal:

    $$
    A = \begin{pmatrix} b & c & & \\ a & b & c & \\ & \ddots & \ddots & \ddots \\ & & a & b \end{pmatrix}
    $$

---


**Exercise 3.** For the IMEX scheme with backward Euler ($\theta = 1$), the update at each time step is $(I - \Delta t\,\mathcal{D})v^k = v^{k+1} + \Delta t\,\mathcal{I}v^{k+1}$. Explain why treating $\mathcal{I}$ explicitly introduces a stability restriction $\Delta t \leq C/\lambda$, while treating $\mathcal{D}$ implicitly removes the parabolic CFL condition. What would happen to the computational cost if $\mathcal{I}$ were also treated implicitly?

??? success "Solution to Exercise 3"
    **Why implicit $\mathcal{D}$ removes the parabolic CFL:** The differential operator $\mathcal{D}$ is a discretization of a parabolic PDE (diffusion equation). Explicit treatment would require $\Delta t \leq \Delta x^2/(2\sigma^2)$ for stability, which becomes very restrictive as $\Delta x \to 0$. Implicit treatment (backward Euler or Crank-Nicolson) is unconditionally stable for parabolic equations because the eigenvalues of $(I - \theta\Delta t\,\mathcal{D})^{-1}$ remain bounded regardless of $\Delta t/\Delta x^2$.

    **Why explicit $\mathcal{I}$ introduces a CFL-like restriction:** The integral operator $\mathcal{I}$ has operator norm approximately $\lambda$ (since $\int f(y)\,dy = 1$ and the operator evaluates $v$ at shifted points with weight $\lambda$). Explicit treatment means the scheme amplifies the solution by a factor $(I + \Delta t\,\mathcal{I})$, whose spectral radius is approximately $1 + \lambda\Delta t$. For stability, we need this factor not to grow unboundedly, requiring $\lambda\Delta t \leq C$ for a moderate constant $C$ (typically $C \approx 1$).

    **Cost of implicit $\mathcal{I}$:** If $\mathcal{I}$ were treated implicitly, the system to solve at each time step would be $(I - \theta\Delta t\,\mathcal{D} - \Delta t\,\mathcal{I})v^k = b$. The operator $\mathcal{I}$ couples all grid points (it is a dense matrix from the convolution), so the system matrix is dense $J \times J$. Direct solution would cost $O(J^3)$ per time step (LU factorization of a dense matrix), or $O(J^2)$ per time step using iterative methods. This is vastly more expensive than the $O(J)$ cost of solving the tridiagonal system from the implicit $\mathcal{D}$ alone.

---


**Exercise 4.** The convolution $I_j = \lambda\int v(t, x_j + y)\,f(y)\,dy$ can be computed via the FFT. Explain why $\mathcal{F}[v * f] = \mathcal{F}[v] \cdot \mathcal{F}[f]$ holds, and why this reduces the cost from $O(J^2)$ (direct summation) to $O(J \log J)$. What care must be taken regarding the periodic extension assumption of the discrete Fourier transform?

??? success "Solution to Exercise 4"
    The convolution theorem states that the Fourier transform of a convolution equals the product of the Fourier transforms:

    $$
    \mathcal{F}[v * f](k) = \mathcal{F}[v](k) \cdot \mathcal{F}[f](k)
    $$

    This holds because $(v * f)(x) = \int v(x-y)f(y)\,dy$, and taking the Fourier transform and exchanging the order of integration yields the product. Therefore, the convolution can be computed as:

    $$
    I_j = \lambda \cdot \mathcal{F}^{-1}[\mathcal{F}[v] \cdot \mathcal{F}[f]]_j
    $$

    Direct summation of $I_j = \lambda\sum_l v_{j+l}f_l\Delta x$ for all $j$ costs $O(J^2)$ (each of $J$ grid points requires summing over $J$ terms). Using the FFT, each transform costs $O(J\log J)$, pointwise multiplication costs $O(J)$, and the inverse FFT costs $O(J\log J)$, for a total of $O(J\log J)$.

    **Care with periodic extension:** The discrete Fourier transform assumes the input is periodic with period $J\Delta x$. If $v$ is not periodic (it generally is not, since boundary values differ), the circular convolution introduces errors at the boundaries. To avoid this, **zero-padding** is used: extend the arrays $v$ and $f$ to length $2J$ (padding with zeros), compute the circular convolution on the extended grid, and extract the central $J$ values. This converts the circular convolution into a linear convolution, at the cost of doubling the array length (still $O(J\log J)$ overall).

---


**Exercise 5.** For the worked example (European put with $S_0 = \$100$, $K = \$100$, $T = 0.5$, $\sigma = 0.20$, $\lambda = 1.0$, $\mu_J = -0.08$, $\sigma_J = 0.25$, $r = 0.05$), compute the compensator $\bar{k}$ and the adjusted drift $\alpha = r - \lambda\bar{k} - \frac{1}{2}\sigma^2$. Verify that $\Delta t \cdot \lambda = 0.005$ for $N_t = 100$ time steps, and explain why this satisfies the stability condition.

??? success "Solution to Exercise 5"
    The compensator is:

    $$
    \bar{k} = e^{\mu_J + \sigma_J^2/2} - 1 = e^{-0.08 + 0.0625/2} - 1 = e^{-0.08 + 0.03125} - 1 = e^{-0.04875} - 1 \approx -0.04758
    $$

    The adjusted drift is:

    $$
    \alpha = r - \lambda\bar{k} - \frac{1}{2}\sigma^2 = 0.05 - 1.0 \times (-0.04758) - \frac{1}{2}(0.04) = 0.05 + 0.04758 - 0.02 = 0.07758
    $$

    For $N_t = 100$ time steps over $T = 0.5$, the time step is $\Delta t = T/N_t = 0.5/100 = 0.005$.

    The stability parameter is:

    $$
    \Delta t \cdot \lambda = 0.005 \times 1.0 = 0.005
    $$

    This is much less than 1, well within the stability bound $\Delta t \leq C/\lambda$. The condition requires $\Delta t \cdot \lambda = O(1)$, so having $\Delta t \cdot \lambda = 0.005 \ll 1$ provides a large stability margin. This means the explicit treatment of the integral part will not cause numerical instabilities, and the overall IMEX scheme will be stable.

---


**Exercise 6.** A European call payoff $\max(S - K, 0) = \max(e^x - K, 0)$ has a kink at $x = \ln K$. Explain why the convergence of the finite difference scheme degrades from $O(\Delta x^2)$ to $O(\Delta x)$ near this point. Describe two techniques to restore second-order convergence: (a) aligning a grid point with $x = \ln K$, and (b) smoothing the payoff by replacing the kink with a regularized approximation.

??? success "Solution to Exercise 6"
    The European call payoff $g(x) = \max(e^x - K, 0)$ has a discontinuous first derivative (kink) at $x = \ln K$. The central difference approximation of $g''(x)$ involves a Dirac delta at the kink:

    $$
    g''(x) = e^x\mathbf{1}_{x > \ln K} + K\delta(x - \ln K)
    $$

    When the grid does not align with $\ln K$, the kink falls between grid points, and the finite difference approximation of $g''$ introduces an $O(1/\Delta x)$ error localized near the strike. This pollutes the solution in a neighborhood of the strike, degrading global convergence from $O(\Delta x^2)$ to $O(\Delta x)$.

    **(a) Grid alignment:** Place a grid point exactly at $x^* = \ln K$ by choosing $\Delta x$ and the grid offset so that $x^* = x_{\min} + j^*\Delta x$ for some integer $j^*$. This ensures the kink lies at a grid point rather than between grid points, and the finite difference stencil correctly captures the discontinuity in the derivative. With alignment, the $O(\Delta x^2)$ convergence is restored away from the strike, and the overall convergence improves significantly.

    **(b) Payoff smoothing:** Replace $g(x) = \max(e^x - K, 0)$ with a regularized version that has a continuous second derivative. For example, use the smoothed payoff:

    $$
    g_\epsilon(x) = \frac{e^x - K}{2}\left(1 + \text{erf}\!\left(\frac{x - \ln K}{\epsilon}\right)\right)
    $$

    where $\epsilon = O(\Delta x)$ is a smoothing width. Alternatively, replace the terminal condition with the exact Black-Scholes price at a small residual maturity $\Delta t$ (which is smooth), and start the backward timestepping from $T - \Delta t$. Both approaches eliminate the kink and restore second-order convergence.

---


**Exercise 7.** The PIDE framework extends to American options by adding the early exercise constraint $V(t, S) \geq \Phi(S)$ at each time step (where $\Phi$ is the intrinsic value). Describe how the penalty method modifies the IMEX scheme: at each time step, add a term $\rho\,\max(\Phi_j - v_j^k, 0)$ to the right-hand side with a large penalty parameter $\rho$. Explain why this forces $v_j^k \geq \Phi_j$ approximately, and what trade-off the choice of $\rho$ involves.

??? success "Solution to Exercise 7"
    The penalty method modifies the IMEX time step by adding a penalty term that enforces the early exercise constraint. At each time step, the update becomes:

    $$
    (I - \theta\Delta t\,\mathcal{D})v^k = (I + (1-\theta)\Delta t\,\mathcal{D})v^{k+1} + \Delta t\,\mathcal{I}v^{k+1} + \rho\Delta t\,\max(\Phi - v^k, 0)
    $$

    where $\Phi_j = \max(K - e^{x_j}, 0)$ for a put (or $\max(e^{x_j} - K, 0)$ for a call) and $\rho \gg 1$ is the penalty parameter.

    **Why it works:** If $v_j^k < \Phi_j$ at some grid point, the penalty term $\rho\,(\Phi_j - v_j^k)$ is large and positive, pushing $v_j^k$ upward toward $\Phi_j$. The larger $\rho$ is, the more strongly the constraint is enforced. In the limit $\rho \to \infty$, the solution satisfies $v_j^k \geq \Phi_j$ exactly. For finite $\rho$, the constraint is satisfied approximately, with violation of order $O(1/\rho)$.

    **Trade-off in choosing $\rho$:** A large $\rho$ enforces the constraint more accurately but stiffens the system of equations, potentially causing convergence issues in iterative solvers (the condition number of the linear system grows with $\rho$). It may also require smaller time steps for the nonlinear iteration to converge. A small $\rho$ gives a well-conditioned system but allows violations of the exercise constraint, introducing a pricing error of order $O(1/\rho)$. In practice, $\rho$ is chosen large enough that the penalty error is smaller than the discretization error (e.g., $\rho = 10^4$ to $10^8$), and the nonlinear system is solved by iteration (computing $\max(\Phi - v^k, 0)$ using the previous iterate and repeating until convergence).
