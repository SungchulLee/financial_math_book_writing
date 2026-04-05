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

---

## Exercises

**Exercise 1.** The European call price $C(k)$ as a function of log-strike $k = \ln K$ is not square-integrable because $C(k) \to S_0 e^{-qT}$ as $k \to -\infty$. Verify this by showing that $\int_{-\infty}^{0}|C(k)|^2\,dk = \infty$ for $C(k) \approx S_0 e^{-qT}$ (constant) on $(-\infty, 0]$. Explain why the damping factor $e^{\alpha k}$ resolves this issue.

??? success "Solution to Exercise 1"
    For $C(k) \approx S_0 e^{-qT}$ (a positive constant) on $(-\infty, 0]$, consider the integral:

    $$
    \int_{-\infty}^{0} |C(k)|^2\,dk \approx (S_0 e^{-qT})^2 \int_{-\infty}^{0} dk = \infty
    $$

    The integrand is a positive constant, and we integrate over a semi-infinite interval, so the integral diverges. Therefore $C(k) \notin L^2(\mathbb{R})$ and the Fourier transform of $C(k)$ does not exist in the $L^2$ sense.

    The damping factor $e^{\alpha k}$ with $\alpha > 0$ resolves this because the modified function $c_T(k) = e^{\alpha k} C(k)$ satisfies:

    $$
    \int_{-\infty}^{0} |c_T(k)|^2\,dk \approx (S_0 e^{-qT})^2 \int_{-\infty}^{0} e^{2\alpha k}\,dk = (S_0 e^{-qT})^2 \cdot \frac{1}{2\alpha} < \infty
    $$

    For $k \to +\infty$, the call value $C(k) \to 0$ faster than any exponential for reasonable models, so $e^{\alpha k} C(k) \to 0$ as well. Thus $c_T \in L^2(\mathbb{R})$ and its Fourier transform exists.

---

**Exercise 2.** Derive the Carr-Madan formula $\psi_T(u) = \frac{e^{-rT}\phi_T(u - (\alpha+1)i)}{(\alpha + iu)(\alpha + 1 + iu)}$ by evaluating the inner integral $\int_{-\infty}^{x}e^{(\alpha + iu)k}(e^x - e^k)\,dk$. Show each step of the integration and verify the denominator simplification.

??? success "Solution to Exercise 2"
    We evaluate the inner integral by splitting it into two parts:

    $$
    I = \int_{-\infty}^{x} e^{(\alpha + iu)k}(e^x - e^k)\,dk = e^x \int_{-\infty}^{x} e^{(\alpha + iu)k}\,dk - \int_{-\infty}^{x} e^{(\alpha + 1 + iu)k}\,dk
    $$

    For the first integral, since $\text{Re}(\alpha + iu) = \alpha > 0$, the exponential vanishes as $k \to -\infty$:

    $$
    e^x \int_{-\infty}^{x} e^{(\alpha + iu)k}\,dk = e^x \cdot \frac{e^{(\alpha + iu)x}}{\alpha + iu} = \frac{e^{(\alpha + 1 + iu)x}}{\alpha + iu}
    $$

    For the second integral, since $\text{Re}(\alpha + 1 + iu) = \alpha + 1 > 0$:

    $$
    \int_{-\infty}^{x} e^{(\alpha + 1 + iu)k}\,dk = \frac{e^{(\alpha + 1 + iu)x}}{\alpha + 1 + iu}
    $$

    Subtracting:

    $$
    I = e^{(\alpha + 1 + iu)x}\left(\frac{1}{\alpha + iu} - \frac{1}{\alpha + 1 + iu}\right) = e^{(\alpha + 1 + iu)x} \cdot \frac{(\alpha + 1 + iu) - (\alpha + iu)}{(\alpha + iu)(\alpha + 1 + iu)}
    $$

    $$
    = \frac{e^{(\alpha + 1 + iu)x}}{(\alpha + iu)(\alpha + 1 + iu)}
    $$

    Substituting back into the outer integral:

    $$
    \psi_T(u) = \frac{e^{-rT}}{(\alpha + iu)(\alpha + 1 + iu)} \int_{-\infty}^{\infty} e^{(\alpha + 1 + iu)x} f(x)\,dx = \frac{e^{-rT}\,\phi_T(u - (\alpha + 1)i)}{(\alpha + iu)(\alpha + 1 + iu)}
    $$

    The last step uses $\phi_T(u - (\alpha+1)i) = \mathbb{E}[e^{i(u - (\alpha+1)i)\ln S_T}] = \mathbb{E}[e^{iu\ln S_T + (\alpha+1)\ln S_T}] = \int e^{(\alpha+1+iu)x} f(x)\,dx$.

    For the denominator simplification:

    $$
    (\alpha + iu)(\alpha + 1 + iu) = \alpha(\alpha + 1) + i\alpha u + iu\alpha + iu + i^2 u^2
    $$

    $$
    = \alpha^2 + \alpha + 2i\alpha u + iu - u^2 = \alpha^2 + \alpha - u^2 + iu(2\alpha + 1)
    $$

---

**Exercise 3.** The integrability condition requires $\mathbb{E}[S_T^{\alpha+1}] < \infty$. For the Black-Scholes model with $\ln S_T \sim N(\mu, \sigma^2 T)$, show that $\mathbb{E}[S_T^p] = \exp(p\mu + p^2\sigma^2 T/2)$, which is finite for all $p$. For the Heston model, explain why there exists a finite upper bound $u^*$ such that $\mathbb{E}[S_T^p] = \infty$ for $p > u^*$, and what this implies for the choice of $\alpha$.

??? success "Solution to Exercise 3"
    **Black--Scholes model.** Here $\ln S_T \sim N(\mu_T, \sigma^2 T)$ where $\mu_T = \ln S_0 + (r - \sigma^2/2)T$. The $p$-th moment is:

    $$
    \mathbb{E}[S_T^p] = \mathbb{E}[e^{p \ln S_T}] = \int_{-\infty}^{\infty} e^{px} \frac{1}{\sqrt{2\pi\sigma^2 T}} \exp\!\left(-\frac{(x - \mu_T)^2}{2\sigma^2 T}\right) dx
    $$

    Completing the square in the exponent: $px - \frac{(x-\mu_T)^2}{2\sigma^2 T} = -\frac{(x - \mu_T - p\sigma^2 T)^2}{2\sigma^2 T} + p\mu_T + \frac{p^2 \sigma^2 T}{2}$.

    The remaining integral is a Gaussian integral equal to 1, so:

    $$
    \mathbb{E}[S_T^p] = \exp\!\left(p\mu_T + \frac{p^2 \sigma^2 T}{2}\right)
    $$

    This is finite for all $p \in \mathbb{R}$ because the exponential of any finite number is finite. Therefore all $\alpha > 0$ are valid for the Carr--Madan damping parameter.

    **Heston model.** The characteristic function $\phi_T(u) = \exp(C(u,T) + D(u,T) v_0 + iu\ln S_0)$ involves the Riccati solution $D(u,T)$ which satisfies an ODE. For complex arguments $u - (\alpha+1)i$, the function $D$ contains a discriminant $d = \sqrt{(\rho\sigma_v iu - \kappa)^2 + \sigma_v^2(iu + u^2)}$ that becomes singular at a critical value $u^*$. When $p = \alpha + 1$ exceeds $u^*$, the Riccati ODE explodes in finite time, meaning $D(-ip, T) \to \infty$ and $\mathbb{E}[S_T^p] = \infty$.

    The explosion point $u^*$ depends on the Heston parameters $(\kappa, \theta, \sigma_v, \rho)$ and the maturity $T$. For the damping parameter, we need $\alpha + 1 < u^*$, so $\alpha < u^* - 1$. Typical values of $u^*$ are in the range 3--10, which is why $\alpha \in (0.5, 2)$ is commonly recommended.

---

**Exercise 4.** The FFT grid relation $\Delta k = 2\pi/(N\eta)$ links the log-strike spacing to the frequency spacing $\eta$ and the grid size $N$. For $N = 4096$ and $\eta = 0.25$, compute $\Delta k$ and the total log-strike range $N\Delta k$. Convert the log-strike range to a strike range centered at $K = 100$ and determine the minimum and maximum strikes on the grid.

??? success "Solution to Exercise 4"
    With $N = 4096$ and $\eta = 0.25$:

    $$
    \Delta k = \frac{2\pi}{N\eta} = \frac{2\pi}{4096 \times 0.25} = \frac{2\pi}{1024} \approx 0.006136
    $$

    The total log-strike range is:

    $$
    N \cdot \Delta k = 4096 \times 0.006136 \approx 25.13
    $$

    The log-strike grid is centered around $k = 0$ (corresponding to $K = S_0$), ranging from $k_{\min} = -N\Delta k / 2 \approx -12.57$ to $k_{\max} = N\Delta k / 2 \approx 12.57$.

    Converting to strikes with $K = S_0 e^k$ where $S_0 = 100$:

    $$
    K_{\min} = 100 \cdot e^{-12.57} \approx 100 \times 3.47 \times 10^{-6} \approx 0.000347
    $$

    $$
    K_{\max} = 100 \cdot e^{12.57} \approx 100 \times 288{,}325 \approx 28{,}832{,}500
    $$

    The practical range of meaningful option prices is much narrower. Near $K = 100$ (i.e., $k \approx 0$), the strike spacing is approximately:

    $$
    \Delta K \approx K \cdot \Delta k = 100 \times 0.006136 \approx 0.614
    $$

    So near ATM, strikes are spaced roughly $\$0.61$ apart, which is sufficiently fine for calibration purposes.

---

**Exercise 5.** Simpson's rule weights $w_j = \frac{\eta}{3}(3 + (-1)^{j+1} - \delta_j)$ improve the discretization from $O(\eta^2)$ to $O(\eta^4)$. Write out the first six weights $w_0, w_1, \ldots, w_5$ explicitly and verify they match the standard Simpson's $1/3$ rule pattern $\{1, 4, 2, 4, 2, 4, \ldots\}/3 \cdot \eta$.

??? success "Solution to Exercise 5"
    The Simpson weights formula is $w_j = \frac{\eta}{3}(3 + (-1)^{j+1} - \delta_j)$ where $\delta_j = 1$ if $j = 0$ and $0$ otherwise.

    For $j = 0$: $w_0 = \frac{\eta}{3}(3 + (-1)^{1} - 1) = \frac{\eta}{3}(3 - 1 - 1) = \frac{\eta}{3}$

    For $j = 1$: $w_1 = \frac{\eta}{3}(3 + (-1)^{2} - 0) = \frac{\eta}{3}(3 + 1) = \frac{4\eta}{3}$

    For $j = 2$: $w_2 = \frac{\eta}{3}(3 + (-1)^{3} - 0) = \frac{\eta}{3}(3 - 1) = \frac{2\eta}{3}$

    For $j = 3$: $w_3 = \frac{\eta}{3}(3 + (-1)^{4} - 0) = \frac{\eta}{3}(3 + 1) = \frac{4\eta}{3}$

    For $j = 4$: $w_4 = \frac{\eta}{3}(3 + (-1)^{5} - 0) = \frac{\eta}{3}(3 - 1) = \frac{2\eta}{3}$

    For $j = 5$: $w_5 = \frac{\eta}{3}(3 + (-1)^{6} - 0) = \frac{\eta}{3}(3 + 1) = \frac{4\eta}{3}$

    Collecting the weights:

    $$
    (w_0, w_1, w_2, w_3, w_4, w_5) = \frac{\eta}{3}(1, 4, 2, 4, 2, 4)
    $$

    This matches the standard Simpson's $1/3$ rule pattern $\{1, 4, 2, 4, 2, 4, \ldots\} \cdot \eta/3$. The pattern is: weight 1 at the first endpoint, then alternating 4 and 2 for interior points. (The last point in a full Simpson rule would have weight 1, but in the FFT context the grid is treated as open-ended.)

---

**Exercise 6.** Compare the Carr-Madan FFT and COS methods for a calibration problem with 50 market-observed strikes and 1000 optimizer iterations. For each method, estimate the total number of characteristic function evaluations and total arithmetic operations. Under what circumstances would COS (with shared $F_k$) be competitive with Carr-Madan for calibration?

---

??? success "Solution to Exercise 6"
    **Setup:** 50 market strikes, 1000 optimizer iterations.

    **Carr--Madan FFT:** Each iteration requires one FFT with $N = 4096$ CF evaluations, plus $O(N \log N) = O(4096 \times 12) \approx 49{,}152$ arithmetic operations for the FFT, plus interpolation to the 50 market strikes ($O(50)$ operations). Total over 1000 iterations:

    - CF evaluations: $1000 \times 4096 = 4{,}096{,}000$
    - FFT operations: $1000 \times 49{,}152 \approx 49{,}152{,}000$

    **COS method:** The density coefficients $F_k$ are shared across strikes (each requires $N$ CF evaluations). For each iteration: $N = 128$ CF evaluations (shared) plus $50 \times 128 = 6{,}400$ multiply-add operations to assemble prices at 50 strikes. Total over 1000 iterations:

    - CF evaluations: $1000 \times 128 = 128{,}000$
    - Arithmetic operations: $1000 \times 6{,}400 = 6{,}400{,}000$

    **Lewis formula:** Each strike requires an independent integral with $M = 200$ CF evaluations. Total per iteration: $50 \times 200 = 10{,}000$ CF evaluations. Over 1000 iterations:

    - CF evaluations: $1000 \times 10{,}000 = 10{,}000{,}000$

    **Comparison:**

    | Method | Total CF evaluations | Total arithmetic operations |
    |---|---|---|
    | Carr--Madan FFT | 4,096,000 | $\approx 49{,}000{,}000$ |
    | COS ($N = 128$) | 128,000 | $\approx 6{,}400{,}000$ |
    | Lewis ($M = 200$) | 10,000,000 | $\approx 10{,}000{,}000$ |

    COS with shared $F_k$ is competitive with---and in fact superior to---Carr--Madan for calibration when the number of market strikes is moderate (50 here). The COS method uses 32 times fewer CF evaluations. COS becomes competitive whenever $M_{\text{strikes}} \times N_{\text{cos}} < N_{\text{fft}}$, i.e., $50 \times 128 = 6{,}400 < 4{,}096$. Since $6{,}400 > 4{,}096$, the CF evaluation count per iteration for COS is actually higher for the arithmetic, but the CF evaluations are far fewer (128 vs 4096). The crossover occurs when $M_{\text{strikes}} > N_{\text{fft}} / N_{\text{cos}} = 4096 / 128 = 32$ for arithmetic operations. For fewer than 32 strikes, COS is superior even in arithmetic; for more strikes, the COS arithmetic cost grows but the CF evaluation savings remain substantial since CF evaluations are typically the computational bottleneck.
