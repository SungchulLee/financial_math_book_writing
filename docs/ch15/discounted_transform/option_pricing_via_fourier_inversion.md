# Option Pricing via Fourier Inversion

The exponential-affine characteristic function of affine processes enables a powerful approach to European option pricing: express the option price as a Fourier integral involving the characteristic function, then evaluate the integral numerically. This section presents the Carr-Madan FFT method and the COS method, both of which exploit the affine structure to price options across a grid of strikes simultaneously. We also discuss calibration---the inverse problem of fitting model parameters to observed option prices.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the Fourier representation of European call and put prices
    2. Apply the Carr-Madan FFT method to price options on a grid of strikes
    3. Apply the COS method using the affine characteristic function
    4. Understand how calibration uses Fourier pricing as a subroutine

---

## Intuition

A European call price is an integral of the payoff $(S_T - K)^+$ against the risk-neutral density. If we knew the density $f(x)$ of $\log S_T$, we could compute $C = e^{-r\tau}\int_{-\infty}^{\infty}(e^x - K)^+ f(x)\,dx$. We rarely know $f$ in closed form, but we always know the characteristic function $\Phi(v) = \int e^{ivx} f(x)\,dx$ for affine models. Fourier inversion recovers $f$ from $\Phi$, or---more efficiently---computes the price integral directly in the frequency domain without ever constructing $f$ explicitly.

The key insight is that the characteristic function of an affine process is known analytically (via the Riccati solutions), so the only numerical step is evaluating a one-dimensional integral. This makes Fourier pricing far more efficient than Monte Carlo simulation for European-style derivatives.

---

## The Fourier Representation of Option Prices

### Setup

Consider a European call with strike $K$, maturity $T$, on a stock with log-price $X_T = \log S_T$. Under the risk-neutral measure $\mathbb{Q}$:

$$
C(t, K) = e^{-r\tau}\,\mathbb{E}^{\mathbb{Q}}\!\left[(e^{X_T} - K)^+ \mid X_t = x\right]
$$

where $\tau = T - t$ and $x = \log S_t$.

### The Carr-Madan Approach

Carr and Madan (1999) observed that the call price as a function of log-strike $k = \log K$ is not square-integrable (it grows linearly for small $k$). To make it integrable, they introduce a damping factor $e^{\alpha k}$:

$$
c_\alpha(k) := e^{\alpha k}\,C(t, e^k)
$$

For $\alpha > 0$ sufficiently large (typically $\alpha > 1$ to ensure integrability), $c_\alpha$ is square-integrable and has the Fourier transform:

$$
\hat{c}_\alpha(v) = \int_{-\infty}^{\infty} e^{ivk}\,c_\alpha(k)\,dk = \frac{e^{-r\tau}\,\Phi_T(v - (\alpha+1)i)}{(\alpha + iv)(\alpha + 1 + iv)}
$$

where $\Phi_T(v) = \mathbb{E}^{\mathbb{Q}}[e^{iv X_T} \mid X_t = x]$ is the characteristic function of $X_T$.

### Inversion

Inverting the Fourier transform:

$$
C(t, K) = \frac{e^{-\alpha k}}{\pi}\int_0^{\infty} \operatorname{Re}\!\left[e^{-ivk}\,\hat{c}_\alpha(v)\right] dv
$$

where $k = \log K$. The integral is real because of the Hermitian symmetry of $\hat{c}_\alpha$.

### FFT Implementation

The integral is discretized on a grid $v_j = j\Delta v$ for $j = 0, 1, \ldots, N-1$, and evaluated simultaneously at log-strikes $k_n = -b + n\Delta k$ using the FFT, where $\Delta v \cdot \Delta k = 2\pi/N$. The cost is $O(N \log N)$ for $N$ strikes, compared to $O(N)$ per strike for direct quadrature.

!!! note "Choice of Damping Parameter"
    The parameter $\alpha$ controls the trade-off between the integrability of $c_\alpha$ and the numerical stability of the Fourier transform. A common choice is $\alpha = 1.5$. Too small $\alpha$ makes $c_\alpha$ non-integrable; too large $\alpha$ amplifies numerical errors in the tails. The optimal $\alpha$ minimizes the $L^2$ norm of the integrand.

---

## The COS Method

### Fourier-Cosine Series Expansion

The COS method (Fang and Oosterlee, 2008) expands the risk-neutral density on a truncated interval $[a, b]$ as a Fourier cosine series:

$$
f(x) \approx \sum_{k=0}^{N-1}{}'  A_k \cos\!\left(k\pi\frac{x - a}{b - a}\right)
$$

where the prime on the summation indicates that the $k = 0$ term is halved, and the coefficients $A_k$ are:

$$
A_k = \frac{2}{b-a}\int_a^b f(x)\cos\!\left(k\pi\frac{x-a}{b-a}\right) dx
$$

### Connection to the Characteristic Function

The key observation is that $A_k$ can be approximated using the characteristic function. Replacing the finite integral by an integral over $\mathbb{R}$ (which is accurate when $[a, b]$ captures the bulk of the density):

$$
A_k \approx \frac{2}{b-a}\operatorname{Re}\!\left[\Phi\!\left(\frac{k\pi}{b-a}\right) \cdot e^{-ik\pi a/(b-a)}\right]
$$

where $\Phi(v) = \mathbb{E}^{\mathbb{Q}}[e^{iv X_T} \mid X_t = x]$ is the characteristic function.

### Option Price Formula

For a European call with log-strike $k = \log K$:

$$
C(t, K) = e^{-r\tau} \sum_{k=0}^{N-1}{}' \operatorname{Re}\!\left[\Phi\!\left(\frac{k\pi}{b-a}\right) e^{-ik\pi a/(b-a)}\right] V_k
$$

where $V_k$ are the cosine series coefficients of the payoff function $(e^x - K)^+$, which have a known closed-form expression.

### Advantages of COS

1. **Exponential convergence**: For smooth densities, the COS method converges exponentially in $N$. Typically $N = 64$ or $N = 128$ suffices for machine precision.
2. **No damping parameter**: Unlike the Carr-Madan method, no auxiliary parameter $\alpha$ is needed.
3. **Greeks by differentiation**: Greeks (delta, gamma, vega) are obtained by differentiating the cosine series term by term.

---

## Using the Affine Characteristic Function

### Direct Evaluation

For an affine process, the characteristic function is:

$$
\Phi(\tau, v, x) = \exp\!\left(\phi(\tau, iv) + \langle \psi(\tau, iv), x \rangle\right)
$$

where $\phi$ and $\psi$ are obtained by solving the Riccati ODEs (analytically or numerically). Both the Carr-Madan and COS methods require evaluating $\Phi$ at multiple frequency points $v_0, v_1, \ldots, v_{N-1}$. For models with explicit Riccati solutions (Vasicek, CIR, Heston), each evaluation is $O(1)$. For models requiring numerical ODE solution, each evaluation costs $O(N_\tau)$ where $N_\tau$ is the number of time steps.

### Heston Model Example

For the Heston model with parameters $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$, $V_0 = 0.04$, $S_0 = \$100$, $r = 0.05$, $T = 1$:

The COS method with $N = 128$ and truncation interval $[a, b]$ chosen as $\pm 10$ standard deviations of the log-price distribution produces call prices accurate to $10^{-10}$ in about 0.1 milliseconds per strike---orders of magnitude faster than Monte Carlo.

---

## Calibration

### The Inverse Problem

Calibration finds model parameters $\boldsymbol{\theta} = (\kappa, \theta, \xi, \rho, V_0)$ (for Heston) that best fit observed option prices $C_i^{\text{mkt}}$ for strikes $K_i$ and maturities $T_i$:

$$
\boldsymbol{\theta}^* = \arg\min_{\boldsymbol{\theta}} \sum_{i=1}^M w_i\!\left(C_i^{\text{model}}(\boldsymbol{\theta}) - C_i^{\text{mkt}}\right)^2
$$

where $w_i$ are weights (often inverse bid-ask spreads or vega-based weights).

### Why Fourier Pricing Enables Calibration

Calibration requires evaluating $C_i^{\text{model}}(\boldsymbol{\theta})$ for many parameter guesses $\boldsymbol{\theta}$ during the optimization. Each evaluation requires computing option prices at multiple strikes and maturities. Fourier methods make this feasible:

1. **Speed**: COS/FFT computes prices at $N$ strikes simultaneously in $O(N)$ or $O(N \log N)$ time
2. **Gradients**: Analytic gradients $\partial C/\partial \boldsymbol{\theta}$ are available by differentiating the characteristic function with respect to parameters, enabling gradient-based optimization
3. **Stability**: The exponential-affine form ensures smooth dependence on parameters, avoiding the noise inherent in Monte Carlo gradients

### Calibration Workflow

1. Fix a maturity $T_j$ and observe market prices $C_1^{\text{mkt}}, \ldots, C_M^{\text{mkt}}$
2. For each parameter guess $\boldsymbol{\theta}$:
    - Solve the Riccati ODEs for the characteristic function at maturity $T_j$
    - Evaluate the COS/FFT formula at all strikes $K_1, \ldots, K_M$
    - Compute the objective function
3. Use Levenberg-Marquardt or differential evolution to minimize the objective
4. Repeat for multiple maturities (joint calibration)

!!! warning "Calibration Pitfalls"
    Common issues include: (1) multiple local minima, especially for models with many parameters; (2) the Feller condition $2\kappa\theta \geq \xi^2$ may be violated by the optimizer, causing numerical instability; (3) overfitting to a single maturity that fails out-of-sample. Regularization and parameter bounds are essential.

---

## Summary

Fourier inversion methods---the Carr-Madan FFT and the COS method---transform the European option pricing problem into a numerical integration of the characteristic function. For affine models, the characteristic function is known explicitly via the Riccati solutions, making each price evaluation extremely fast. The COS method achieves exponential convergence with $N \approx 128$ terms and requires no damping parameter. These methods are the computational backbone of calibration, which fits model parameters to observed option prices by minimizing a weighted least-squares objective with Fourier pricing as the inner loop.

---

## Further Reading

- Carr, P. & Madan, D. (1999). "Option Valuation Using the Fast Fourier Transform." *Journal of Computational Finance*, 2(4), 61-73.
- Fang, F. & Oosterlee, C. W. (2008). "A Novel Pricing Method for European Options Based on Fourier-Cosine Series Expansions." *SIAM Journal on Scientific Computing*, 31(2), 826-848.
- Heston, S. L. (1993). "A Closed-Form Solution for Options with Stochastic Volatility." *Review of Financial Studies*, 6(2), 327-343.
- Lord, R. & Kahl, C. (2007). "Optimal Fourier Inversion in Semi-Analytical Option Pricing." *Journal of Computational Finance*, 10(4), 1-30.
