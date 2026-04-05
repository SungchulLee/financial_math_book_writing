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

---

## Exercises

**Exercise 1.** Derive the Fourier representation of the European call price starting from $C = e^{-r\tau}\int_{-\infty}^\infty (e^x - K)^+ f(x)\,dx$ where $f(x)$ is the risk-neutral density of $\log S_T$. Show that the price can be written as a single integral involving the characteristic function $\Phi(v)$.

??? success "Solution to Exercise 1"
    Starting from the call price formula with $x = \log S_t$ and $f$ the risk-neutral density of $X_T = \log S_T$:

    $$
    C = e^{-r\tau}\int_{-\infty}^{\infty}(e^x - K)^+ f(x)\,dx = e^{-r\tau}\int_{\log K}^{\infty}(e^x - K)f(x)\,dx
    $$

    Split into two terms:

    $$
    C = e^{-r\tau}\int_{\log K}^{\infty} e^x f(x)\,dx - Ke^{-r\tau}\int_{\log K}^{\infty} f(x)\,dx
    $$

    The second integral is $\mathbb{Q}(X_T \geq \log K)$, which can be expressed via the inversion formula using $\Phi(v) = \int e^{ivx}f(x)\,dx$:

    $$
    \mathbb{Q}(X_T \geq k) = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\operatorname{Re}\!\left[\frac{e^{-ivk}\Phi(v)}{iv}\right]dv
    $$

    where $k = \log K$. For the first integral, define the density $\tilde{f}(x) = e^x f(x)/\mathbb{E}[e^{X_T}]$ (the Esscher-transformed density). Its characteristic function is $\tilde{\Phi}(v) = \Phi(v - i)/\Phi(-i)$. Then

    $$
    \int_k^{\infty} e^x f(x)\,dx = \Phi(-i)\left[\frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\operatorname{Re}\!\left[\frac{e^{-ivk}\tilde{\Phi}(v)}{iv}\right]dv\right]
    $$

    Combining and noting $e^{-r\tau}\Phi(-i) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[e^{X_T}] = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[S_T] = S_t$ (by the martingale property of discounted prices):

    $$
    C = S_t\Pi_1 - Ke^{-r\tau}\Pi_2
    $$

    where $\Pi_1$ and $\Pi_2$ are both expressed as single integrals involving the characteristic function $\Phi(v)$.

---

**Exercise 2.** The Carr-Madan method introduces a damping factor $e^{\alpha k}$ (where $k = \log K$) to make the Fourier transform of the call price integrable. Explain why $\alpha > 0$ is needed and derive the condition on $\alpha$ that ensures integrability in terms of the moment condition $\mathbb{E}[S_T^{\alpha+1}] < \infty$.

??? success "Solution to Exercise 2"
    The call price as a function of log-strike $k = \log K$ is $C(k) = e^{-r\tau}\mathbb{E}[(e^{X_T} - e^k)^+]$. As $k \to -\infty$ (deep in-the-money), $C(k) \to e^{-r\tau}\mathbb{E}[e^{X_T}] - e^{-r\tau}e^k \to S_t$, which is positive and bounded. However, $C(k) \geq 0$ and decays to zero only as $k \to +\infty$, while it approaches a positive constant as $k \to -\infty$. Thus $C(k) \notin L^1(\mathbb{R})$ and has no Fourier transform.

    Multiplying by the damping factor $e^{\alpha k}$ for $\alpha > 0$:

    $$
    c_\alpha(k) = e^{\alpha k}C(k)
    $$

    As $k \to -\infty$, $c_\alpha(k) \to e^{\alpha k}S_t \to 0$ exponentially. As $k \to +\infty$, $c_\alpha(k) \to 0$ (since $C(k)$ decays faster than any polynomial). So $c_\alpha$ is integrable provided it does not blow up.

    The Fourier transform of $c_\alpha$ involves evaluating $\mathbb{E}[e^{(\alpha+1)X_T}]$, which appears in the denominator of $\hat{c}_\alpha$. For this to be finite, we need

    $$
    \mathbb{E}[S_T^{\alpha+1}] = \mathbb{E}[e^{(\alpha+1)X_T}] < \infty
    $$

    This is the integrability condition on $\alpha$. For the Black-Scholes model this holds for all $\alpha > 0$ since $X_T$ is Gaussian. For models with heavy tails (e.g., jump-diffusions), the condition restricts $\alpha$ to values below a critical exponent determined by the exponential moment condition of the process.

---

**Exercise 3.** In the COS method, the option price is approximated by

$$
C \approx e^{-r\tau}\sum_{k=0}^{N-1}{}' \operatorname{Re}\!\left[\Phi\!\left(\frac{k\pi}{b-a}\right)e^{-ik\pi\frac{a}{b-a}}\right] V_k
$$

where $V_k$ are the cosine series coefficients of the payoff. For a call option, compute $V_k$ analytically by integrating $(e^x - K)^+\cos(k\pi\frac{x-a}{b-a})$ over $[a, b]$.

??? success "Solution to Exercise 3"
    We need to compute

    $$
    V_k = \frac{2}{b - a}\int_a^b (e^x - K)^+\cos\!\left(k\pi\frac{x - a}{b - a}\right)dx
    $$

    Since $(e^x - K)^+ = 0$ for $x < \log K$ and $e^x - K$ for $x \geq \log K$, with $\ell = \log K$:

    $$
    V_k = \frac{2}{b - a}\int_{\max(a, \ell)}^b (e^x - K)\cos\!\left(k\pi\frac{x - a}{b - a}\right)dx
    $$

    This splits into two integrals. Define $\omega_k = \frac{k\pi}{b - a}$ and $d = \max(a, \ell)$. The payoff coefficient integrals are:

    **First integral** (the $e^x$ part): Using integration by parts or the known formula $\int e^x \cos(\omega_k(x - a))\,dx = \frac{e^x[\cos(\omega_k(x-a)) + \omega_k\sin(\omega_k(x-a))]}{1 + \omega_k^2}$, evaluate from $d$ to $b$.

    **Second integral** (the $-K$ part): $-K\int_d^b \cos(\omega_k(x - a))\,dx = -\frac{K}{\omega_k}[\sin(\omega_k(b - a)) - \sin(\omega_k(d - a))]$ for $k \geq 1$, and $-K(b - d)$ for $k = 0$.

    For $k \geq 1$, combining and using $\omega_k(b - a) = k\pi$:

    $$
    V_k = \frac{2}{b-a}\!\left[\frac{e^b(\cos(k\pi) + \omega_k\sin(k\pi)) - e^d(\cos(\omega_k(d-a)) + \omega_k\sin(\omega_k(d-a)))}{1 + \omega_k^2} + \frac{K\sin(\omega_k(d-a))}{\omega_k}\right]
    $$

    Since $\sin(k\pi) = 0$ and $\cos(k\pi) = (-1)^k$, this simplifies to a closed-form expression in terms of $k$, $a$, $b$, $K$, and $d = \max(a, \log K)$.

---

**Exercise 4.** The truncation range $[a, b]$ in the COS method is typically set using cumulants of the log-price distribution. If $c_1$, $c_2$, $c_4$ are the first, second, and fourth cumulants, write down the standard choice $a = c_1 - L\sqrt{c_2 + \sqrt{c_4}}$ and $b = c_1 + L\sqrt{c_2 + \sqrt{c_4}}$ with $L = 10$. For the Black-Scholes model, compute $c_1$ and $c_2$ and verify the resulting range.

??? success "Solution to Exercise 4"
    For the Black-Scholes model, $X_T = \log S_T \sim N(\mu_X, \sigma_X^2)$ where $\mu_X = x + (r - \frac{1}{2}\sigma^2)\tau$ and $\sigma_X^2 = \sigma^2\tau$. The cumulants of a normal distribution are:

    - First cumulant: $c_1 = \mu_X = x + (r - \frac{1}{2}\sigma^2)\tau$
    - Second cumulant: $c_2 = \sigma_X^2 = \sigma^2\tau$
    - Fourth cumulant: $c_4 = 0$ (all cumulants of order $\geq 3$ vanish for Gaussian distributions)

    The truncation range is

    $$
    a = c_1 - L\sqrt{c_2 + \sqrt{c_4}} = c_1 - L\sqrt{\sigma^2\tau}
    $$

    $$
    b = c_1 + L\sqrt{c_2 + \sqrt{c_4}} = c_1 + L\sqrt{\sigma^2\tau}
    $$

    With $L = 10$, this gives $[a, b] = [c_1 - 10\sigma\sqrt{\tau},\; c_1 + 10\sigma\sqrt{\tau}]$. Since the normal density drops below $10^{-22}$ beyond $10$ standard deviations, this range captures essentially the entire probability mass, ensuring the truncation error is negligible.

    For typical parameters (e.g., $\sigma = 0.2$, $\tau = 1$), $\sigma\sqrt{\tau} = 0.2$, so $[a, b] = [c_1 - 2, c_1 + 2]$, a range of width $4$ centered on the expected log-price.

---

**Exercise 5.** Compare the computational complexity of the Carr-Madan FFT and the COS method. If $N$ is the number of strike points and the characteristic function evaluation costs $O(1)$ (closed-form Riccati solution), what is the total cost of pricing at $N$ strikes for each method? Which method has the advantage for calibration where prices at many strikes are needed simultaneously?

??? success "Solution to Exercise 5"
    **Carr-Madan FFT:** The method discretizes the Fourier integral at $N$ frequency points $v_j = j\Delta v$, evaluates the characteristic function at each (cost $O(1)$ per evaluation for closed-form models), then applies the FFT to obtain prices at $N$ log-strikes simultaneously. The FFT costs $O(N\log N)$, and the $N$ characteristic function evaluations cost $O(N)$, giving total cost

    $$
    \text{Carr-Madan: } O(N\log N)
    $$

    **COS method:** The method sums $N$ terms, each requiring one characteristic function evaluation at $v_k = \frac{k\pi}{b-a}$ (cost $O(1)$) and one multiplication by the precomputed payoff coefficient $V_k$. This gives $N$ prices at a single strike in $O(N)$ operations. For $M$ different strikes, the cost is $O(NM)$ since the characteristic function evaluations are shared but the summation must be repeated for each strike.

    **Comparison for calibration:** In calibration, we need prices at $M$ strikes simultaneously. The Carr-Madan FFT produces all $N = M$ prices in $O(N\log N)$ operations with a single FFT call. The COS method costs $O(NM)$. If $M = N$ (many strikes), FFT has the advantage at $O(N\log N)$ vs $O(N^2)$. However, the COS method typically needs far fewer terms ($N \approx 64$--$128$ vs $N \approx 4096$ for FFT) due to exponential convergence, so in practice the COS method is often faster despite the less favorable scaling.

    For calibration specifically, both methods are vastly superior to Monte Carlo. The COS method is generally preferred because it requires no damping parameter tuning and achieves higher accuracy with fewer terms.

---

**Exercise 6.** Describe the calibration workflow for fitting a Heston model to a panel of European option prices across multiple strikes and maturities. What is the objective function, how is the characteristic function used as a subroutine, and what optimizer is typically employed? Discuss the role of the Feller condition as a parameter constraint.

??? success "Solution to Exercise 6"
    **Objective function.** Given observed market prices $C_i^{\text{mkt}}$ for strikes $K_i$ and maturities $T_i$ ($i = 1, \ldots, M$), the Heston parameters $\boldsymbol{\theta} = (\kappa, \theta, \xi, \rho, V_0)$ are found by minimizing

    $$
    \boldsymbol{\theta}^* = \arg\min_{\boldsymbol{\theta}} \sum_{i=1}^M w_i\!\left(C_i^{\text{model}}(\boldsymbol{\theta}) - C_i^{\text{mkt}}\right)^2
    $$

    where $w_i$ are weights (commonly inverse bid-ask spread or $1/\text{vega}_i^2$ to equalize the impact of options across strikes).

    **Characteristic function as subroutine.** For each parameter guess $\boldsymbol{\theta}$, the model prices are computed as follows: (1) solve the Heston Riccati ODEs analytically for $\phi(\tau, iv)$ and $\psi(\tau, iv)$, yielding the discounted characteristic function; (2) feed the characteristic function into the COS or Carr-Madan formula to compute prices at all strikes for each maturity. This inner loop is executed hundreds or thousands of times during optimization.

    **Optimizer.** Common choices include:

    - *Levenberg-Marquardt*: A gradient-based method for nonlinear least squares, efficient when analytic gradients $\partial C/\partial \boldsymbol{\theta}$ are available (by differentiating the characteristic function)
    - *Differential evolution*: A global optimizer that avoids local minima, useful for initial parameter estimation
    - A typical workflow uses differential evolution for a coarse global search, then Levenberg-Marquardt for refinement

    **Feller condition.** The condition $2\kappa\theta \geq \xi^2$ ensures the CIR variance process $V_t$ stays strictly positive. In calibration, this should be imposed as a constraint: $2\kappa\theta \geq \xi^2$ (or with a small margin). Violating Feller causes $V_t$ to touch zero, where the square root diffusion is not Lipschitz, leading to numerical instability in the Riccati ODE solutions (branch cuts in the complex square root). In practice, many calibrated Heston parameters violate Feller, which is acceptable if the characteristic function is implemented with the correct branch of the complex logarithm (the "rotation count" or "little Heston trap" fix), but imposing Feller as a soft constraint via regularization improves robustness.
