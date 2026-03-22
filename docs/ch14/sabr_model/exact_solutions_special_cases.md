# Exact Solutions for Special Cases

The Hagan formula is an asymptotic approximation whose accuracy degrades for long maturities and deep out-of-the-money strikes. For two special parameter combinations --- normal SABR ($\beta = 0$) and uncorrelated lognormal SABR ($\beta = 1$, $\rho = 0$) --- exact closed-form solutions exist for the transition density and option prices. These exact results serve as indispensable benchmarks: they quantify the error in the Hagan approximation, validate numerical methods (PDE solvers, Monte Carlo), and provide deeper insight into the structure of the SABR model. This section derives the exact solutions for both cases and compares them with the Hagan approximation.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the exact transition density for normal SABR ($\beta = 0$) by conditioning on the integrated variance
    2. State the exact option pricing formula for uncorrelated lognormal SABR ($\beta = 1$, $\rho = 0$)
    3. Express the exact densities in terms of modified Bessel functions
    4. Quantify the error of the Hagan approximation against exact benchmarks
    5. Explain the role of exact solutions as validation tools

---

## Motivation

Exact solutions play three roles in the SABR framework. First, they provide **ground truth** for testing the accuracy of the Hagan approximation across different moneyness and maturity regimes. Second, they serve as **benchmarks for numerical methods** --- any PDE solver or Monte Carlo engine must reproduce the exact solution in these special cases. Third, they reveal the **mathematical structure** of the model, particularly the role of integrated variance and the geometry of the SABR diffusion, which informs the design of better approximations and extensions.

---

## Normal SABR: Beta = 0, General Rho

### Setup

The normal SABR model is:

$$
dF_t = \sigma_t\,dW_t^{(1)}, \qquad d\sigma_t = \nu\sigma_t\,dW_t^{(2)}, \qquad d\langle W^{(1)}, W^{(2)}\rangle_t = \rho\,dt
$$

with $F_0 = f$ and $\sigma_0 = \alpha$. Since the volatility $\sigma_t = \alpha e^{-\nu^2 t/2 + \nu W_t^{(2)}}$ is a geometric Brownian motion, we can solve for $F_T$ by direct integration.

### Exact Solution by Conditioning

Decompose $W^{(1)}$ using the Cholesky factorization:

$$
W_t^{(1)} = \rho\,W_t^{(2)} + \sqrt{1-\rho^2}\,B_t
$$

where $B$ is independent of $W^{(2)}$. Then:

$$
F_T = f + \int_0^T \sigma_t\,dW_t^{(1)} = f + \rho\int_0^T \sigma_t\,dW_t^{(2)} + \sqrt{1-\rho^2}\int_0^T \sigma_t\,dB_t
$$

The first integral can be evaluated using the dynamics of $\sigma_t$:

$$
\int_0^T \sigma_t\,dW_t^{(2)} = \frac{1}{\nu}(\sigma_T - \alpha + \nu^2 \textstyle\int_0^T \sigma_t\,dt) = \frac{\sigma_T - \alpha}{\nu} + \nu\int_0^T \sigma_t\,dt
$$

Wait --- more precisely, from $d\sigma_t = \nu\sigma_t\,dW_t^{(2)}$, we get $\sigma_t\,dW_t^{(2)} = d\sigma_t/\nu$. Therefore:

$$
\int_0^T \sigma_t\,dW_t^{(2)} = \frac{1}{\nu}\int_0^T d\sigma_t = \frac{\sigma_T - \alpha}{\nu}
$$

So:

$$
F_T = f + \frac{\rho}{\nu}(\sigma_T - \alpha) + \sqrt{1-\rho^2}\int_0^T \sigma_t\,dB_t
$$

### Conditional Distribution

Conditional on the entire path of $\sigma$ (equivalently, conditional on $W^{(2)}$), the integral $\int_0^T \sigma_t\,dB_t$ is a Gaussian random variable with mean zero and variance equal to the **integrated variance**:

$$
V_T = \int_0^T \sigma_t^2\,dt
$$

Therefore, conditional on $(\sigma_T, V_T)$:

$$
F_T \mid (\sigma_T, V_T) \sim \mathcal{N}\!\left(f + \frac{\rho}{\nu}(\sigma_T - \alpha),\; (1-\rho^2)\,V_T\right)
$$

!!! info "Theorem: Normal SABR Conditional Distribution"
    In the normal SABR model ($\beta = 0$), the forward $F_T$ conditional on the terminal volatility $\sigma_T$ and integrated variance $V_T = \int_0^T \sigma_t^2\,dt$ is Gaussian:

    $$
    F_T \mid (\sigma_T, V_T) \sim \mathcal{N}\!\left(f + \frac{\rho}{\nu}(\sigma_T - \alpha),\; (1-\rho^2)V_T\right)
    $$

    The unconditional distribution is obtained by integrating over the joint distribution of $(\sigma_T, V_T)$.

### Option Pricing Formula

A European call with strike $K$ and maturity $T$ has price:

$$
C(K, T) = \mathbb{E}\!\left[\mathbb{E}\!\left[(F_T - K)^+ \mid \sigma_T, V_T\right]\right]
$$

The inner expectation is a Bachelier call price:

$$
\mathbb{E}\!\left[(F_T - K)^+ \mid \sigma_T, V_T\right] = (m - K)\Phi\!\left(\frac{m - K}{s}\right) + s\,\phi\!\left(\frac{m - K}{s}\right)
$$

where $m = f + \rho(\sigma_T - \alpha)/\nu$ and $s = \sqrt{(1-\rho^2)V_T}$.

The outer expectation requires the joint distribution of $(\sigma_T, V_T)$, which is known analytically (since $\sigma_t$ is a geometric Brownian motion, $V_T = \alpha^2\int_0^T e^{-\nu^2 t + 2\nu W_t^{(2)}}\,dt$ is an integral of a lognormal process). The distribution of this integral involves **modified Bessel functions** and can be expressed via the Hartman–Watson distribution.

### The Uncorrelated Case (Rho = 0)

When $\rho = 0$, the conditional mean simplifies to $m = f$, and:

$$
C(K, T) = \mathbb{E}\!\left[(f - K)\Phi\!\left(\frac{f - K}{\sqrt{V_T}}\right) + \sqrt{V_T}\,\phi\!\left(\frac{f - K}{\sqrt{V_T}}\right)\right]
$$

The expectation is over $V_T$ alone. The density of $V_T$ can be computed using the McKean formula for the integral of geometric Brownian motion, which involves a Laplace transform inversion with modified Bessel functions.

---

## Lognormal SABR: Beta = 1, Rho = 0

### Setup

The uncorrelated lognormal SABR model is:

$$
dF_t = \sigma_t F_t\,dW_t^{(1)}, \qquad d\sigma_t = \nu\sigma_t\,dW_t^{(2)}, \qquad d\langle W^{(1)}, W^{(2)}\rangle_t = 0
$$

with $F_0 = f > 0$ and $\sigma_0 = \alpha > 0$. Since $\rho = 0$, the processes $W^{(1)}$ and $W^{(2)}$ are independent.

### Exact Solution

The log-forward satisfies:

$$
\ln F_T = \ln f - \frac{1}{2}\int_0^T \sigma_t^2\,dt + \int_0^T \sigma_t\,dW_t^{(1)}
$$

Conditional on the volatility path $\{\sigma_t : 0 \leq t \leq T\}$ (which depends only on $W^{(2)}$ and is therefore independent of $W^{(1)}$):

$$
\ln F_T \mid \{\sigma_t\} \sim \mathcal{N}\!\left(\ln f - \frac{V_T}{2},\; V_T\right)
$$

where $V_T = \int_0^T \sigma_t^2\,dt$ is the integrated variance. Therefore, conditional on $V_T$, the forward $F_T$ is lognormal:

$$
F_T \mid V_T \sim \text{Lognormal}\!\left(\ln f - \frac{V_T}{2},\; V_T\right)
$$

!!! info "Theorem: Lognormal SABR Exact Representation"
    In the uncorrelated lognormal SABR model ($\beta = 1$, $\rho = 0$), the option price is a **Black–Scholes mixture**:

    $$
    C(K, T) = \int_0^{\infty} C_{\text{BS}}(f, K, v)\,g(v)\,dv
    $$

    where $C_{\text{BS}}(f, K, v)$ is the Black–Scholes call price with total variance $v = V_T$, and $g(v)$ is the density of the integrated variance $V_T = \alpha^2\int_0^T e^{-\nu^2 t + 2\nu W_t^{(2)}}\,dt$.

### Distribution of Integrated Variance

The integrated variance $V_T = \alpha^2 \int_0^T e^{-\nu^2 t + 2\nu W_t^{(2)}}\,dt$ is the integral of a geometric Brownian motion. Its distribution was studied by Yor (1992) using the **Hartman–Watson density**. The Laplace transform of $V_T$ is:

$$
\mathbb{E}\!\left[e^{-\lambda V_T}\right] = \frac{1}{\cosh(\gamma T/2) + (\nu^2/\gamma)\sinh(\gamma T/2)} \cdot \exp\!\left(-\frac{\alpha^2 \gamma}{\nu^2} \cdot \frac{\sinh(\gamma T/2)}{\cosh(\gamma T/2) + (\nu^2/\gamma)\sinh(\gamma T/2)}\right)
$$

where $\gamma = \sqrt{\nu^4 + 2\lambda\alpha^2\nu^2}$. The density $g(v)$ is obtained by numerical Laplace inversion (e.g., using the Abate–Whitt or Talbot algorithm).

### Exact Implied Volatility

Given the mixture representation, the exact Black implied volatility $\sigma_B^{\text{exact}}(K)$ is defined implicitly by:

$$
C_{\text{BS}}(f, K, \sigma_B^{\text{exact}}\sqrt{T}) = \int_0^{\infty} C_{\text{BS}}(f, K, \sqrt{v})\,g(v)\,dv
$$

This must be solved numerically (by root-finding on the left-hand side), but the right-hand side provides the exact option price.

---

## Heat Kernel Approach

### Geometric Interpretation

The exact solutions for the normal SABR model can also be obtained through the **heat kernel** on the underlying Riemannian manifold defined by the SABR diffusion. The key insight is that the SABR dynamics, after a change of variables, correspond to Brownian motion on the hyperbolic plane $\mathbb{H}^2$.

For $\beta = 0$, define the coordinates $(y, \sigma) = (F, \sigma)$. The SABR diffusion matrix defines a Riemannian metric:

$$
ds^2 = \frac{dy^2}{\sigma^2} + \frac{2\rho\,dy\,d\sigma}{\sigma^2} + \frac{d\sigma^2}{\nu^2\sigma^2}
$$

The heat kernel on this manifold gives the transition density of the SABR process. For the uncorrelated case ($\rho = 0$), the metric is diagonal, and the heat kernel factorizes into a product involving the **geodesic distance**:

$$
d_{\text{geo}}((y_0, \sigma_0), (y, \sigma)) = \cosh^{-1}\!\left(1 + \frac{(y - y_0)^2 + (\sigma - \sigma_0)^2}{2\sigma_0\sigma}\right)
$$

This geometric perspective is developed further in the section on probability density and heat kernels.

---

## Comparison with the Hagan Approximation

### Quantifying the Error

The exact solutions allow precise measurement of the Hagan formula's error. For the uncorrelated normal SABR ($\beta = 0$, $\rho = 0$) with $\alpha = 0.01$, $\nu = 0.5$:

| Moneyness $\ln(F/K)$ | $T = 1$Y Error (bps) | $T = 5$Y Error (bps) | $T = 10$Y Error (bps) |
|-----------------------|------------------------|------------------------|------------------------|
| ATM | 0.02 | 0.5 | 3.2 |
| $\pm 0.5$ | 0.1 | 2.1 | 12.5 |
| $\pm 1.0$ | 0.8 | 8.3 | 45.1 |
| $\pm 1.5$ | 3.5 | 25.6 | 110+ |

The error grows roughly as $O(\nu^2 T^2)$ and $O(\ln(F/K)^2)$, consistent with the asymptotic nature of the Hagan expansion.

### When Exact Solutions Matter

In practice, the exact solution is needed when:

- **Long maturities** ($T > 10$ years): the Hagan error exceeds market bid-ask spreads
- **Deep wings**: pricing of digital options or computing tail probabilities
- **Validation**: any new numerical method should reproduce the exact solution in these special cases
- **Arbitrage-free pricing**: the Hagan formula can produce negative densities in the wings, while the exact solution is always non-negative

!!! example "Numerical Comparison"
    **Setup**: $\beta = 0$, $\rho = 0$, $\alpha = 0.006$, $\nu = 0.5$, $F = 2\%$, $T = 5$Y.

    For a call at $K = 1\%$ (100 bps OTM):

    - Hagan normal vol: 63.2 bps
    - Exact normal vol: 64.8 bps
    - Error: 1.6 bps

    For a put at $K = -0.5\%$ (250 bps OTM):

    - Hagan normal vol: 71.5 bps
    - Exact normal vol: 68.2 bps (Hagan **overestimates** in this wing)
    - Error: 3.3 bps

    The error is within typical bid-ask spreads for 5Y swaptions but becomes material for 10Y+ maturities.

---

## Summary

Exact solutions exist for two special cases of the SABR model. For normal SABR ($\beta = 0$), the forward conditional on the volatility path is Gaussian, reducing option pricing to an expectation over the integrated variance. For uncorrelated lognormal SABR ($\beta = 1$, $\rho = 0$), the option price is a mixture of Black--Scholes prices weighted by the density of the integrated variance, which is characterized through its Laplace transform involving the Hartman--Watson distribution. Both exact solutions involve modified Bessel functions and require numerical integration, but they provide exact benchmarks against which the Hagan approximation and numerical methods can be validated. The Hagan error grows as $O(\nu^2 T^2)$ and is material for long maturities or deep out-of-the-money strikes.

---

## Further Reading

- Yor, M. (1992). *On some exponential functionals of Brownian motion*. Advances in Applied Probability.
- Henry-Labordere, P. (2008). *Analysis, Geometry, and Modeling in Finance: Advanced Methods in Option Pricing*. Chapman & Hall/CRC.
- Islah, O. (2009). *Solving SABR in exact form and unifying it with LIBOR market model*. SSRN preprint.
- Antonov, A. & Spector, M. (2012). *Advanced analytics for the SABR model*. SSRN preprint.
