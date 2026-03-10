# Chapter 9: Fourier Pricing Methods


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

This chapter develops Fourier-based techniques for pricing European options, exploiting the fact that many financial models---particularly affine processes---admit closed-form characteristic functions even when the density or option price has no explicit formula. Starting from Fourier series representations of probability densities on finite intervals, we construct the COS method via cosine expansions and characteristic function recovery of coefficients, derive the Carr-Madan FFT approach for simultaneous pricing across strike grids, present the Lewis contour integral formula for single-strike pricing, analyze convergence and error bounds for each method, compare their relative strengths, and extend these methods beyond standard equity models to interest rate derivatives, multi-factor affine models, and Bermudan options.

## Key Concepts

### **Fourier Series and Density Representations**
A probability density $f(x)$ on a finite interval $[a, b]$ admits a Fourier cosine expansion 

$$f(x) = \sum_{k=0}^{\infty}{}' A_k \cos(k\pi(x-a)/(b-a))$$ 

where the prime denotes halving the $k=0$ term and the coefficients are 

$$A_k = \frac{2}{b-a}\int_a^b f(x)\cos(k\pi(x-a)/(b-a))\,dx$$ 

On a general finite interval, the full Fourier series uses both sine and cosine terms with coefficients determined by inner products against the orthogonal basis. Convergence properties depend on the smoothness of $f$: the Dirichlet conditions guarantee pointwise convergence at continuity points, $L^2$ convergence (Parseval's theorem) holds for square-integrable densities, and for $C^k$ functions the coefficients decay as $O(1/k^{k+1})$ yielding rapid convergence. The **Gibbs phenomenon** at discontinuities produces overshoots of approximately 9% that do not vanish as the number of terms increases, motivating truncation strategies and smoothing techniques. The **cosine expansion** on $[0, \pi]$ (or any symmetric-about-endpoint interval) is particularly well-suited for probability densities because it naturally handles the boundary behavior without introducing artificial discontinuities. For densities supported on the entire real line $\mathbb{R}$, **truncation to a finite interval** $[a, b]$ introduces an exponentially small error when $f$ has exponential or Gaussian tails, as is the case for most financial models. The truncation range is typically chosen using cumulants: $[a,b] = [\mu \pm L\sqrt{\sigma^2}]$ for a suitable multiplier $L$ (often $L = 10$--$12$).

### **The COS Method**
The COS method (Fang and Oosterlee, 2008) prices European options by combining the cosine expansion of the risk-neutral density with analytic integration against the payoff. The key insight is that the Fourier cosine coefficients $A_k$ of the density can be recovered from the **characteristic function** $\phi(u) = \mathbb{E}[e^{iuX}]$ via the approximation:

$$A_k \approx \frac{2}{b-a}\,\text{Re}\!\left[\phi\!\left(\frac{k\pi}{b-a}\right) e^{-ik\pi a/(b-a)}\right]$$

This connection between the characteristic function and cosine coefficients eliminates the need to know the density explicitly---only the characteristic function is required. The **COS pricing formula** for a European option becomes a truncated series:

$$V \approx e^{-rT}\sum_{k=0}^{N-1}{}' \text{Re}\!\left[\phi\!\left(\frac{k\pi}{b-a}\right) e^{-ik\pi a/(b-a)}\right] V_k$$

where the **payoff coefficients** 

$$V_k = \frac{2}{b-a}\int_a^b \Phi(x)\cos(k\pi(x-a)/(b-a))\,dx$$ 

are computed analytically for standard payoffs (calls, puts, digitals). The method achieves **exponential convergence** in $N$ when the density is smooth, typically requiring only $N = 64$--$128$ terms for six-digit accuracy under the Heston model. **Density recovery** from the characteristic function provides a powerful diagnostic: the reconstructed density 

$$\hat{f}(x) = \sum_{k=0}^{N-1}{}' A_k \cos(k\pi(x-a)/(b-a))$$ 

can be compared against known densities (e.g., normal, chi-squared) to validate implementations and visualize the risk-neutral distribution implied by a model.

### **Error Analysis and Convergence**
The total error of the COS method decomposes into two components: (i) the **truncation error** from restricting the density support to $[a, b]$, which is exponentially small when $f$ has sufficiently light tails and the interval is chosen using cumulants; and (ii) the **series truncation error** from using $N$ terms instead of infinitely many, which decays exponentially for smooth densities (at a rate governed by the analyticity of $f$) or algebraically for less regular densities. Explicit error bounds involve the cumulants $c_n$ of the log-price: the first cumulant $c_1$ (mean) determines the center of the interval, the second cumulant $c_2$ (variance) determines the width, and higher cumulants (skewness $c_3$, kurtosis $c_4$) refine the bound. For the Heston model, where the characteristic function decays exponentially along the real axis, the COS method converges exponentially and achieves machine precision with moderate $N$.

### **Carr-Madan FFT Method**
The Carr-Madan (1999) approach prices options across a grid of strikes simultaneously using the **Fast Fourier Transform**. Starting from the Fourier representation of the modified call price $c_T(k) = e^{\alpha k}C(K)$ with $k = \ln K$ and damping parameter $\alpha > 0$:

$$c_T(k) = \frac{e^{-\alpha k}}{\pi}\int_0^{\infty} e^{-iuk}\,\psi_T(u)\,du$$

where 

$$\psi_T(u) = \frac{e^{-rT}\phi_T(u - (\alpha+1)i)}{\alpha^2 + \alpha - u^2 + iu(2\alpha+1)}$$ 

and $\phi_T$ is the characteristic function of the log-price. The damping parameter $\alpha$ must satisfy the **integrability condition** $\mathbb{E}[S_T^{\alpha+1}] < \infty$, linking to the moment structure of the model. The integral is discretized on a uniform grid with $N$ points and spacing $\eta$, then evaluated via FFT in $\mathcal{O}(N\log N)$ operations, yielding option prices at $N$ log-strike points simultaneously with spacing $\Delta k = 2\pi/(N\eta)$. Simpson's rule weights improve the discretization accuracy from first to second order. The method is optimal for **calibration** where prices are needed across a dense strike grid, but requires tuning of $\alpha$, $\eta$, and $N$.

### **Lewis Integration Formula**
The Lewis (2001) formula provides a direct contour integral representation that avoids the damping parameter entirely:

$$C = S_0 - \frac{\sqrt{S_0 K}\,e^{-rT/2}}{\pi}\int_0^{\infty} \text{Re}\!\left[\frac{e^{-iu\ln(K/S_0)}\phi_T(u - i/2)}{u^2 + 1/4}\right]du$$

This integrates along the critical line $\text{Im}(u) = 1/2$ in the complex plane, where the integrand decays as $|u|^{-2}$, ensuring rapid convergence of numerical quadrature. Gauss-Laguerre or adaptive quadrature rules typically achieve machine precision with $\mathcal{O}(100)$ function evaluations. The Lewis formula is the simplest and most elegant Fourier method for pricing a single option at a given strike.

### **Comparison and Method Selection**
The COS method excels for pricing individual options or small grids with its exponential convergence and minimal parameter tuning (only $N$ and the truncation interval). The Carr-Madan FFT method is optimal when prices are needed across a dense strike grid (e.g., for calibration), leveraging the $\mathcal{O}(N\log N)$ FFT to price all strikes simultaneously. The Lewis formula offers simplicity, high accuracy, and no tuning parameters for single-strike pricing. All three methods require the characteristic function as input, making them natural companions to affine models. In terms of accuracy per computational cost, the COS method generally provides the best ratio for individual option pricing, while the FFT is unmatched for whole-surface pricing.

### **Beyond Equity Models: Extensions and Limitations**
The COS method and other Fourier techniques extend naturally to any model with a known or computable characteristic function. For **other affine models** (Bates/SVJ, variance gamma, CGMY/tempered stable, Kou double-exponential), the characteristic function takes a Levy-Khintchine or exponential-affine form, and the COS method applies directly with appropriate truncation ranges. For **interest rate models** where the short rate or forward rate follows an affine process (Vasicek, CIR, Hull-White), the COS method prices zero-coupon bond options and swaptions using the bond price characteristic function. For **multi-factor affine models**, the Riccati system becomes vector-valued but the pricing formula retains the same structure. **Bermudan options** can be priced by combining COS pricing with backward induction, computing continuation values as Fourier-reconstructed conditional expectations at each exercise date. **Limitations and failure cases** arise when: (i) the characteristic function has heavy tails or slow decay, requiring very large $N$; (ii) the characteristic function has branch cuts in the complex plane requiring careful navigation (e.g., the Heston model's Riccati solution needs the rotation count method for path continuity); (iii) very short maturities cause the density to concentrate sharply, demanding wider truncation intervals or larger $N$; and (iv) models without closed-form $\phi$ require numerical ODE solutions for the Riccati system, adding computational overhead.

!!! note "Role in the Book"
    Fourier methods connect the characteristic function theory of affine processes (Chapter 15) to practical option pricing. They serve as the primary pricing engine for the Heston model (Chapter 16), provide the benchmark against which finite difference (Chapter 8) and Monte Carlo methods are validated, and underpin calibration routines (Chapter 17) that require fast, repeated option price evaluation across strike-maturity grids. The density recovery capability also provides diagnostic tools for understanding the risk-neutral distributions implied by different models.

---
