# Chapter 9: Fourier Pricing Methods

This chapter develops Fourier-based techniques for pricing European options, exploiting the fact that many financial models—particularly affine processes—admit closed-form characteristic functions even when the density or option price has no explicit formula. Starting from Fourier series representations of probability densities, we construct the COS method via cosine expansions, derive the Carr-Madan FFT approach and the Lewis contour integral formula, analyze convergence and error bounds, and extend these methods beyond standard equity models to interest rate and multi-factor settings.

## Key Concepts

**Fourier Series and Density Representations**
A probability density $f(x)$ on a finite interval $[a, b]$ admits a Fourier cosine expansion $f(x) = \sum_{k=0}^{\infty}{}' A_k \cos(k\pi(x-a)/(b-a))$ where the prime denotes halving the $k=0$ term and the coefficients are $A_k = \frac{2}{b-a}\int_a^b f(x)\cos(k\pi(x-a)/(b-a))\,dx$. Convergence properties depend on the smoothness of $f$: Dirichlet conditions guarantee pointwise convergence at continuity points, while $L^2$ convergence (Parseval's theorem) holds for square-integrable densities. The Gibbs phenomenon at discontinuities—overshoots of approximately 9%—motivates truncation strategies and smoothing techniques. For densities supported on $\mathbb{R}$, truncation to a finite interval $[a, b]$ introduces an exponentially small error when $f$ has exponential or Gaussian tails, as is the case for most financial models.

**The COS Method**
The COS method (Fang and Oosterlee, 2008) prices European options by combining the cosine expansion of the risk-neutral density with analytic integration against the payoff. The key insight is that the Fourier cosine coefficients $A_k$ can be recovered from the **characteristic function** $\phi(u) = \mathbb{E}[e^{iuX}]$ via

$$A_k \approx \frac{2}{b-a}\,\text{Re}\!\left[\phi\!\left(\frac{k\pi}{b-a}\right) e^{-ik\pi a/(b-a)}\right]$$

The option price becomes a truncated series $V \approx e^{-rT}\sum_{k=0}^{N-1}{}' \text{Re}[\phi(k\pi/(b-a))\,e^{-ik\pi a/(b-a)}]\,V_k$ where the **payoff coefficients** $V_k = \int_a^b \Phi(x)\cos(k\pi(x-a)/(b-a))\,dx$ are computed analytically for standard payoffs (calls, puts, digitals). The method achieves **exponential convergence** in $N$ when the density is smooth, typically requiring only $N = 64$–$128$ terms for six-digit accuracy under the Heston model. Error analysis decomposes into truncation error (from restricting to $[a, b]$) and series truncation error (from using $N$ terms), both controlled by explicit bounds involving the cumulants of $X$.

**Carr-Madan FFT Method**
The Carr-Madan (1999) approach prices options across a grid of strikes simultaneously using the **Fast Fourier Transform**. Starting from the Fourier representation of the modified call price $c_T(k) = e^{\alpha k}C(K)$ with $k = \ln K$ and damping parameter $\alpha > 0$:

$$c_T(k) = \frac{e^{-\alpha k}}{\pi}\int_0^{\infty} e^{-iuk}\,\psi_T(u)\,du$$

where $\psi_T(u) = e^{-rT}\phi_T(u - (\alpha+1)i)/(\alpha^2 + \alpha - u^2 + iu(2\alpha+1))$ and $\phi_T$ is the characteristic function of the log-price. The integral is discretized on a uniform grid and evaluated via FFT in $\mathcal{O}(N\log N)$ operations, yielding option prices at $N$ log-strike points simultaneously. The damping parameter $\alpha$ must satisfy the integrability condition $\mathbb{E}[S_T^{\alpha+1}] < \infty$, linking to the moment structure of the model. Simpson's rule or the trapezoidal rule with appropriate weights controls discretization error.

**Lewis Integration Formula**
The Lewis (2001) formula provides a direct contour integral representation:

$$C = S_0 - \frac{\sqrt{S_0 K}\,e^{-rT/2}}{\pi}\int_0^{\infty} \text{Re}\!\left[\frac{e^{-iu\ln(K/S_0)}\phi_T(u - i/2)}{u^2 + 1/4}\right]du$$

This avoids the damping parameter entirely by integrating along the critical line $\text{Im}(u) = 1/2$ in the complex plane. The integrand decays as $|u|^{-2}$, ensuring rapid convergence of numerical quadrature. Gauss-Laguerre or adaptive quadrature rules typically achieve machine precision with $\mathcal{O}(100)$ function evaluations.

**Comparison and Method Selection**
The COS method excels for pricing individual options or small grids with its exponential convergence and minimal parameter tuning. The FFT method is optimal when prices are needed across a dense strike grid (e.g., for calibration), leveraging the $\mathcal{O}(N\log N)$ FFT. The Lewis formula offers simplicity and high accuracy for single-strike pricing. All three methods require the characteristic function as input, making them natural companions to affine models (Chapter 15) and the Heston model (Chapter 16). Failure cases include models with heavy tails where the characteristic function decays slowly, models without closed-form $\phi$ (requiring numerical ODE solutions for the Riccati system), and very short maturities where the density concentrates sharply and requires large $N$ or wide truncation intervals.

**Beyond Equity Models**
Fourier methods extend to **interest rate models** where the short rate or forward rate follows an affine process—the COS method prices zero-coupon bond options and swaptions using the bond price characteristic function. For **multi-factor affine models**, the Riccati system becomes vector-valued but the pricing formula retains the same structure. **Bermudan options** can be priced by combining COS pricing with backward induction, computing continuation values as Fourier-reconstructed conditional expectations at each exercise date. Limitations arise when the characteristic function has branch cuts requiring careful complex-plane navigation, or when the Riccati ODEs must be solved numerically with attention to the rotation count for path continuity.

!!! note "Role in the Book"
    Fourier methods connect the characteristic function theory of affine processes (Chapter 15) to practical option pricing. They serve as the primary pricing engine for the Heston model (Chapter 16), provide the benchmark against which finite difference (Chapter 8) and Monte Carlo methods are validated, and underpin calibration routines (Chapter 17) that require fast, repeated option price evaluation across strike-maturity grids.

---
