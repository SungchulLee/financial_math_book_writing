# Carr--Madan Fast Fourier Transform Method

While the COS method prices a single option at a given strike with exponential convergence, many practical applications---particularly model calibration---require option prices across a dense grid of strikes simultaneously. The Carr--Madan (1999) method addresses this by expressing the option price as a Fourier transform that can be evaluated at all grid points in a single FFT pass, with total cost $O(N\log N)$ instead of $O(N)$ per strike. The method introduces a damping parameter $\alpha$ that ensures integrability of the modified call transform, and the FFT produces prices at $N$ log-strike values simultaneously. This section derives the Carr--Madan formula, discusses the choice of damping parameter, and explains the FFT discretization.

!!! info "Prerequisites"
    - [From Characteristic Function to Density](../cos_method/characteristic_function_to_density.md) (Fourier inversion)
    - [Fourier Series of Probability Densities](../fourier_series/fourier_series_of_densities.md) (CF as Fourier transform)
    - Numerical methods: discrete Fourier transform, FFT algorithm

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the Carr--Madan formula for the damped call transform
    2. Explain the role of the damping parameter $\alpha$ and its integrability condition
    3. Discretize the Fourier integral for FFT evaluation
    4. Implement the Carr--Madan FFT pricing for a grid of strikes
    5. Apply Simpson's rule weights for improved accuracy

---

## Motivation: Why Transform the Call Price?

The European call price as a function of log-strike $k = \ln K$ is

$$
C(k) = e^{-rT}\int_{-\infty}^{\infty}(e^x - e^k)^+ f(x)\,dx
$$

where $x = \ln S_T$ and $f$ is the risk-neutral density of $\ln S_T$. The function $C(k)$ is not square-integrable over $k \in \mathbb{R}$ because $C(k) \to S_0 e^{-qT}$ as $k \to -\infty$ (deep in-the-money calls approach the forward price). This means the Fourier transform of $C(k)$ does not exist in the classical sense. Carr and Madan's insight was to introduce an exponential damping factor that makes the modified call price square-integrable.

---

## The Damped Call Transform

Define the **damped call price**:

$$
c_T(k) = e^{\alpha k}C(k)
$$

where $\alpha > 0$ is the damping parameter. Since $C(k) \to S_0 e^{-qT}$ as $k \to -\infty$, the factor $e^{\alpha k} \to 0$ ensures $c_T(k) \to 0$ as $k \to -\infty$. For $k \to +\infty$, $C(k) \to 0$ faster than any exponential (for reasonable models), so $c_T(k) \to 0$ as well. Under suitable conditions on $\alpha$, $c_T \in L^1(\mathbb{R}) \cap L^2(\mathbb{R})$.

The Fourier transform of $c_T$ is:

$$
\psi_T(u) = \int_{-\infty}^{\infty} e^{iuk}c_T(k)\,dk = \int_{-\infty}^{\infty} e^{iuk}e^{\alpha k}C(k)\,dk
$$

!!! note "Theorem: Carr--Madan Formula"
    The Fourier transform of the damped call price is

    $$
    \psi_T(u) = \frac{e^{-rT}\phi_T(u - (\alpha + 1)i)}{\alpha^2 + \alpha - u^2 + iu(2\alpha + 1)}
    $$

    where $\phi_T(u) = \mathbb{E}[e^{iu\ln S_T}]$ is the characteristic function of the log-price.

**Proof.** Substituting $C(k) = e^{-rT}\int_k^{\infty}(e^x - e^k)f(x)\,dx$:

$$
\psi_T(u) = e^{-rT}\int_{-\infty}^{\infty}\int_k^{\infty} e^{iuk + \alpha k}(e^x - e^k)f(x)\,dx\,dk
$$

Exchanging the order of integration (valid when $\mathbb{E}[S_T^{\alpha+1}] < \infty$):

$$
\psi_T(u) = e^{-rT}\int_{-\infty}^{\infty}f(x)\left[\int_{-\infty}^{x}e^{(\alpha + iu)k}(e^x - e^k)\,dk\right]dx
$$

The inner integral evaluates to:

$$
\int_{-\infty}^{x}e^{(\alpha + iu)k}(e^x - e^k)\,dk = \frac{e^{(\alpha + 1 + iu)x}}{\alpha + iu} - \frac{e^{(\alpha + 1 + iu)x}}{\alpha + 1 + iu}
$$

$$
= e^{(\alpha + 1 + iu)x}\left(\frac{1}{\alpha + iu} - \frac{1}{\alpha + 1 + iu}\right) = \frac{e^{(\alpha + 1 + iu)x}}{(\alpha + iu)(\alpha + 1 + iu)}
$$

Therefore:

$$
\psi_T(u) = \frac{e^{-rT}}{(\alpha + iu)(\alpha + 1 + iu)}\int_{-\infty}^{\infty}e^{(\alpha + 1 + iu)x}f(x)\,dx = \frac{e^{-rT}\phi_T(u - (\alpha+1)i)}{(\alpha + iu)(\alpha + 1 + iu)}
$$

Expanding the denominator: $(\alpha + iu)(\alpha + 1 + iu) = \alpha^2 + \alpha + i u(2\alpha + 1) - u^2$. $\square$

---

## Integrability Condition for the Damping Parameter

The damping parameter $\alpha$ must satisfy the condition that the characteristic function $\phi_T(u - (\alpha+1)i)$ exists, which requires:

$$
\mathbb{E}[S_T^{\alpha+1}] = \phi_T(-(\alpha+1)i) < \infty
$$

!!! warning "Choosing $\alpha$"
    The damping parameter $\alpha$ must lie in the strip where the moment $\mathbb{E}[S_T^{\alpha+1}]$ is finite:

    - **Black--Scholes:** All $\alpha > 0$ work (Gaussian tails ensure all moments exist)
    - **Heston:** $\alpha$ must satisfy $\alpha + 1 < u^*$ where $u^*$ is the explosion point of the Riccati ODE for $D(u, T)$. Typically $\alpha \in (0.5, 2)$
    - **Variance Gamma:** $\alpha + 1 < M/\sigma$ where $M$ is the right exponential parameter
    - **CGMY:** $\alpha + 1 < M$

    A common practical choice is $\alpha = 1.5$, which works for most models.

!!! tip "Sensitivity to $\alpha$"
    The choice of $\alpha$ affects the accuracy of the FFT discretization. Too small an $\alpha$ makes the integrand slowly decaying; too large an $\alpha$ pushes the CF evaluation closer to the explosion point. The optimal $\alpha$ minimizes the discretization error and can be chosen by the saddle-point method of Lord and Kahl (2007).

---

## FFT Discretization

To evaluate the call price $C(k) = e^{-\alpha k}\frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-iuk}\psi_T(u)\,du$ using the FFT, discretize the integral on a uniform grid.

Let $\eta$ be the spacing in the frequency domain, with $N$ points $u_j = j\eta$ for $j = 0, 1, \ldots, N-1$. The trapezoidal rule approximation is:

$$
C(k_m) \approx \frac{e^{-\alpha k_m}}{\pi}\sum_{j=0}^{N-1} e^{-ij\eta k_m}\psi_T(u_j)\frac{\eta}{2}\left(2 - \delta_j\right)
$$

where $\delta_j = 1$ if $j = 0$ and 0 otherwise (trapezoidal endpoint correction).

The log-strike grid is determined by the FFT relation:

$$
k_m = -\frac{N\eta\Delta k}{2} + m\Delta k, \quad \Delta k = \frac{2\pi}{N\eta}, \quad m = 0, 1, \ldots, N-1
$$

!!! note "Proposition: FFT Evaluation"
    The $N$ call prices $\{C(k_m)\}_{m=0}^{N-1}$ can be computed simultaneously as:

    $$
    C(k_m) = \frac{e^{-\alpha k_m}}{\pi}\,\text{Re}\!\left[\text{FFT}\!\left\{e^{-i u_j k_0}\psi_T(u_j)\frac{\eta}{2}(2-\delta_j)\right\}\right]_m
    $$

    where the FFT is the standard $N$-point discrete Fourier transform, costing $O(N\log N)$ operations.

The FFT simultaneously produces option prices at $N$ log-strikes with spacing $\Delta k = 2\pi/(N\eta)$.

---

## Simpson's Rule Enhancement

The trapezoidal rule introduces an $O(\eta^2)$ discretization error. Simpson's rule improves this to $O(\eta^4)$ by using alternating weights $\{1, 4, 2, 4, 2, \ldots, 4, 1\}$ scaled by $\eta/3$:

$$
w_j = \frac{\eta}{3}\left(3 + (-1)^{j+1} - \delta_j\right)
$$

The call prices become:

$$
C(k_m) = \frac{e^{-\alpha k_m}}{\pi}\,\text{Re}\!\left[\text{FFT}\!\left\{e^{-iu_j k_0}\psi_T(u_j) w_j\right\}\right]_m
$$

Simpson's rule is the standard choice in Carr--Madan implementations, providing two extra orders of accuracy at no additional computational cost.

---

## Parameter Selection

The FFT parameters $N$, $\eta$, and $\alpha$ must be chosen to balance accuracy against resolution:

| Parameter | Role | Typical value | Tradeoff |
|---|---|---|---|
| $N$ | Grid size | $2^{12} = 4096$ | Larger $N$ = finer grids in both domains |
| $\eta$ | Frequency spacing | $0.25$ | Smaller $\eta$ = more accurate quadrature |
| $\Delta k = 2\pi/(N\eta)$ | Log-strike spacing | $\approx 0.006$ | Determined by $N$ and $\eta$ |
| $\alpha$ | Damping | $1.5$ | Must satisfy moment condition |

!!! tip "Resolution Constraint"
    The product $N\eta$ determines the total frequency range, while $\Delta k = 2\pi/(N\eta)$ determines the strike resolution. For calibration requiring prices at many strikes, increasing $N$ improves both quadrature accuracy and strike resolution simultaneously.

---

## Example: Black--Scholes FFT Pricing

!!! example "Carr--Madan FFT vs Black--Scholes"
    Parameters: $S_0 = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$, $\alpha = 1.5$.

    With $N = 4096$ and $\eta = 0.25$, the FFT produces 4096 call prices at log-strikes spaced by $\Delta k \approx 0.006$ (corresponding to strikes roughly from $\$50$ to $\$200$ with spacing $\approx \$0.60$).

    At-the-money ($K = 100$): $C_{\text{FFT}} = 10.4506$, $C_{\text{BS}} = 10.4506$. Error $< 10^{-4}$.

    The error is dominated by the discretization of the Fourier integral, not by the FFT itself. Simpson's rule weights reduce the error to $< 10^{-6}$.

---

## Example: Heston FFT Calibration Grid

!!! example "Simultaneous Pricing Under Heston"
    With Heston parameters and $N = 4096$, a single FFT call produces option prices at all 4096 strikes in approximately 10 milliseconds. This makes the Carr--Madan method ideal for calibration, where the objective function requires evaluation at hundreds of market-observed strikes.

    For a fixed maturity, the calibration loop evaluates:

    1. Propose parameters $(\kappa, \theta, \sigma_v, \rho, v_0)$
    2. One FFT call: $O(N\log N) \approx 50{,}000$ operations
    3. Interpolate to market strikes: $O(M)$ where $M$ is the number of market quotes
    4. Compute objective (e.g., sum of squared implied vol errors)
    5. Repeat with optimizer

    The FFT step (2) is the bottleneck, but at 10 ms per evaluation, even 1000 optimizer iterations complete in 10 seconds.

---

## Comparison with COS Method

| Feature | Carr--Madan FFT | COS Method |
|---|---|---|
| Output | Prices at $N$ strikes simultaneously | Price at a single strike |
| Complexity | $O(N\log N)$ for all strikes | $O(N)$ per strike |
| Parameters to tune | $\alpha, \eta, N$ | $N, [a,b]$ |
| Accuracy per cost | Good for dense grids | Superior for individual options |
| Convergence order | $O(\eta^2)$ or $O(\eta^4)$ (Simpson) | Exponential for smooth $f$ |
| Best use | Calibration | Pricing, Greeks |

The two methods are complementary: Carr--Madan for calibration over strike grids, COS for precise single-option pricing and sensitivity computation.

---

## Summary

The Carr--Madan FFT method provides simultaneous option pricing across a grid of strikes:

| Component | Formula / Value |
|---|---|
| Damped call transform | $\psi_T(u) = \frac{e^{-rT}\phi_T(u - (\alpha+1)i)}{\alpha^2 + \alpha - u^2 + iu(2\alpha+1)}$ |
| Integrability condition | $\mathbb{E}[S_T^{\alpha+1}] < \infty$ |
| FFT grid relation | $\Delta k = 2\pi/(N\eta)$ |
| Complexity | $O(N\log N)$ for $N$ strikes simultaneously |
| Simpson's rule | Improves discretization from $O(\eta^2)$ to $O(\eta^4)$ |

**The Carr--Madan FFT method exploits the Fourier structure of option prices to produce an entire strike-grid of prices in a single $O(N\log N)$ pass, making it the method of choice for calibration problems that require evaluating hundreds of option prices per iteration.**
