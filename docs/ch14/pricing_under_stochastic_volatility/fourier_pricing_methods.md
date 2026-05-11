# Fourier Pricing Methods

Fourier methods convert option pricing into numerical integration problems using characteristic functions. They are widely used for stochastic volatility models because they are fast, accurate, and enable efficient calibration across many strikes simultaneously.

---

## Overview of Fourier Pricing

### The Basic Idea

European option prices involve expectations of the form:

$$
C(K) = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]
$$

The density of $S_T$ (or $X_T = \log S_T$) is typically unavailable in closed form for stochastic volatility models, but the **characteristic function** $\varphi(u) = \mathbb{E}[e^{iuX_T}]$ often is.

**Key insight:** Use Fourier inversion to express prices as integrals of $\varphi$, then evaluate numerically.

### Pricing Formula Types

| Method | Integral form | Key feature |
|--------|---------------|-------------|
| Direct density inversion | $\int e^{-iux}\varphi(u)\,du$ | Recovers $f(x)$ first |
| Gil-Pelaez | $\int \text{Re}[\cdot]\,du$ | Real-valued integrand |
| Carr–Madan | $\int e^{-iuk}\psi(u)\,du$ | Damped call transform |
| Lewis | $\int \varphi(u-i/2)\cdot(\cdot)\,du$ | Symmetric formula |
| COS | $\sum_k A_k \text{Re}[\varphi(\cdot)]$ | Cosine expansion |

---

## Carr–Madan Method

### The Problem with Direct Integration

A European call price is:

$$
C(K) = e^{-rT}\int_{\log K}^{\infty}(e^x - K)f(x)\,dx
$$

where $f(x)$ is the density of $X_T = \log S_T$.

**Issue:** The call price $C(K)$ as a function of $K$ is not square-integrable (it grows as $K \to 0$), preventing direct Fourier analysis.

### Damping the Payoff

Introduce a **damping factor** $e^{\alpha k}$ where $k = \log K$:

$$
c(k) = e^{\alpha k}C(e^k)
$$

For $\alpha > 0$, the modified price $c(k) \to 0$ as $k \to -\infty$, making it integrable.

### The Carr–Madan Formula

The Fourier transform of $c(k)$ is:

$$
\hat{c}(u) = \int_{-\infty}^{\infty} e^{iuk}c(k)\,dk = \frac{e^{-rT}\varphi(u - i(\alpha+1))}{\alpha^2 + \alpha - u^2 + i(2\alpha+1)u}
$$

**Derivation:** Substitute the call payoff, interchange integrals, and evaluate.

### Inversion Formula

The call price is recovered by:

$$
C(K) = \frac{e^{-\alpha k}}{\pi}\int_0^{\infty} e^{-iuk}\hat{c}(u)\,du
$$

or equivalently:

$$
C(K) = \frac{e^{-\alpha k}}{\pi}\int_0^{\infty} \text{Re}\left[e^{-iuk}\hat{c}(u)\right]du
$$

### Choosing α

The damping parameter $\alpha$ must satisfy:

1. **Integrability:** $\alpha > 0$
2. **Moment existence:** $\mathbb{E}[S_T^{\alpha+1}] < \infty$

For Heston, this means $\alpha + 1$ must be less than the critical moment $n^*(T)$.

**Typical choices:** $\alpha = 1.5$ or $\alpha = 0.75$

**Rule of thumb:** Choose $\alpha$ such that the integrand decays smoothly without oscillating excessively.

---

## FFT Implementation

### Discretization

Discretize the integration with step $\Delta u$ and truncate at $N$ points:

$$
C(k_j) \approx \frac{e^{-\alpha k_j}}{\pi}\sum_{n=0}^{N-1} e^{-i u_n k_j}\hat{c}(u_n)\Delta u
$$

where $u_n = n\Delta u$ and $k_j$ is the log-strike grid.

### FFT Structure

For the FFT to apply, we need:

$$
k_j = -b + j\Delta k, \quad j = 0, \ldots, N-1
$$

with the relationship:

$$
\Delta u \cdot \Delta k = \frac{2\pi}{N}
$$

**Trade-off:** Fine $\Delta u$ (accurate integration) implies coarse $\Delta k$ (sparse strike grid), and vice versa.

### Simpson's Rule Enhancement

Apply Simpson's weights for improved accuracy:

$$
C(k_j) \approx \frac{e^{-\alpha k_j}}{\pi}\sum_{n=0}^{N-1} e^{-i u_n k_j}\hat{c}(u_n)\cdot w_n \cdot \Delta u
$$

where $w_n = \frac{1}{3}(3 + (-1)^n - \delta_{n,0})$.

### Implementation Summary

```python
def carr_madan_fft(S0, K_array, T, r, q, cf_func, alpha=1.5, N=4096):
    """
    Carr-Madan FFT pricing
    cf_func: characteristic function phi(u) of log(S_T)
    """
    # Grid parameters
    du = 0.01
    dk = 2 * np.pi / (N * du)
    b = N * dk / 2
    
    # u grid
    u = np.arange(N) * du
    
    # Modified characteristic function
    def psi(v):
        num = np.exp(-r * T) * cf_func(v - 1j * (alpha + 1))
        denom = alpha**2 + alpha - v**2 + 1j * (2*alpha + 1) * v
        return num / denom
    
    # Simpson weights
    w = np.ones(N)
    w[0] = 0.5
    w[1::2] = 4/3
    w[2::2] = 2/3
    
    # Integrand with adjustment
    x = np.exp(1j * b * u) * psi(u) * w * du
    
    # FFT
    y = np.fft.fft(x)
    
    # Strike grid
    k_grid = -b + np.arange(N) * dk
    K_grid = np.exp(k_grid)
    C_grid = np.exp(-alpha * k_grid) / np.pi * np.real(y)
    
    # Interpolate to desired strikes
    C = np.interp(K_array, K_grid, C_grid)
    return C
```

---

## Lewis Formula

### Alternative Representation

Lewis (2001) provides a symmetric formula:

$$
C(K) = S_0 e^{-qT} - \frac{\sqrt{S_0 K}e^{-(r+q)T/2}}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{iuk}\varphi(u - i/2)}{u^2 + 1/4}\right]du
$$

where $k = \log(K/S_0)$.

### Advantages

- No damping parameter to choose
- Symmetric in $S_0$ and $K$
- Often more stable numerically

### Disadvantage

- Requires $\mathbb{E}[\sqrt{S_T}] < \infty$ (weaker than Carr–Madan)

---

## COS Method

### Cosine Series Expansion

The **COS method** (Fang & Oosterlee, 2008) expands the density in cosine series:

$$
f(x) \approx \sum_{k=0}^{N-1} A_k \cos\left(k\pi\frac{x-a}{b-a}\right)
$$

on a truncated domain $[a, b]$.

### Fourier-Cosine Coefficients

The coefficients are related to the characteristic function:

$$
A_k = \frac{2}{b-a}\text{Re}\left[\varphi\left(\frac{k\pi}{b-a}\right)e^{-ik\pi\frac{a}{b-a}}\right]
$$

### Option Pricing

The call price becomes:

$$
C(K) = e^{-rT}\sum_{k=0}^{N-1} \text{Re}\left[\varphi\left(\frac{k\pi}{b-a}\right)e^{-ik\pi\frac{a}{b-a}}\right] \cdot V_k
$$

where $V_k$ are precomputed payoff coefficients:

$$
V_k = \frac{2}{b-a}\int_{\log K}^b (e^x - K)\cos\left(k\pi\frac{x-a}{b-a}\right)dx
$$

These have closed-form expressions.

### Advantages of COS

1. **Very fast:** $O(N)$ complexity per strike
2. **High accuracy:** Exponential convergence for smooth densities
3. **Flexible:** Works for calls, puts, digitals, etc.
4. **No damping:** Natural truncation

### Domain Selection

Choose $[a, b]$ based on cumulants:

$$
a = c_1 - L\sqrt{c_2 + \sqrt{c_4}}, \quad b = c_1 + L\sqrt{c_2 + \sqrt{c_4}}
$$

where $c_j$ are cumulants of $X_T$ and $L \approx 10$–$12$.

For Heston, cumulants can be computed from CF derivatives.

---

## Comparison of Methods

| Method | Speed | Accuracy | Ease of use | Multiple strikes |
|--------|-------|----------|-------------|-----------------|
| Carr–Madan + FFT | Fast | Good | Medium | Excellent |
| Lewis | Medium | Good | Easy | Good |
| COS | Very fast | Excellent | Medium | Excellent |
| Quadrature | Slow | High | Easy | Poor |

### Recommendations

- **Calibration (many strikes):** COS or Carr–Madan FFT
- **Single price:** Lewis or direct quadrature
- **Greeks:** COS (differentiable) or FFT with bump
- **Exotics:** Method depends on payoff structure

---

## Numerical Considerations

### Integration Truncation

For Carr–Madan:

- Truncate at $u_{\max}$ where $|\hat{c}(u)| < \epsilon$
- Typically $u_{\max} \in [100, 500]$

For COS:

- Choose domain $[a, b]$ to capture 99.99% of density
- $N = 64$–$256$ terms usually suffice

### Grid Resolution

| Parameter | Carr–Madan | COS |
|-----------|------------|-----|
| $N$ | 4096–8192 | 64–256 |
| Strike spacing | Fixed by FFT | Arbitrary |
| Computational cost | $O(N \log N)$ | $O(N \cdot N_K)$ |

### Error Sources

1. **Truncation error:** Domain too small
2. **Discretization error:** Grid too coarse
3. **Numerical precision:** Cancellation in complex arithmetic
4. **Model error:** CF evaluation issues

### Validation

Always validate against:

- Black–Scholes (set $\xi = 0$)
- Monte Carlo (independent method)
- Put-call parity

---

## Extension to Puts and Other Payoffs

### Put Options

Use put-call parity:

$$
P(K) = C(K) - S_0 e^{-qT} + K e^{-rT}
$$

Or modify the Fourier transform for put payoffs directly.

### Digital Options

Digital call: $\mathbf{1}_{S_T > K}$

$$
D_C(K) = e^{-rT}\left[\frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-iuk}\varphi(u)}{iu}\right]du\right]
$$

### Power Payoffs

For $(S_T)^p$:

$$
\mathbb{E}[(S_T)^p] = e^{rT}\varphi(-ip)
$$

(if the moment exists).

---

## Key Takeaways

- Fourier methods use characteristic functions for efficient option pricing
- Carr–Madan + FFT prices many strikes simultaneously
- The COS method offers high accuracy with exponential convergence
- Damping parameters must respect moment existence
- Numerical stability requires careful implementation
- These methods are essential for stochastic volatility calibration

---

## Further Reading

- Carr, P. & Madan, D. (1999). *Option valuation using the fast Fourier transform*. Journal of Computational Finance.
- Lewis, A. (2001). *A simple option formula for general jump-diffusion and other exponential Lévy processes*. Working paper.
- Fang, F. & Oosterlee, C.W. (2008). *A novel pricing method for European options based on Fourier-cosine series expansions*. SIAM Journal on Scientific Computing.
- Lord, R. & Kahl, C. (2007). *Optimal Fourier inversion in semi-analytical option pricing*. Journal of Computational Finance.
- Lee, R. (2004). *Option pricing by transform methods: extensions, unification, and error control*. Journal of Computational Finance.

---

## Exercises

**Exercise 1.** In the Carr-Madan formula, the damped call transform is

$$
\hat{c}(u) = \frac{e^{-rT}\varphi(u - i(\alpha+1))}{\alpha^2 + \alpha - u^2 + i(2\alpha+1)u}
$$

Verify that the denominator can be factored as $-(u - i\alpha)(u - i(\alpha + 1))$. For $\alpha = 1.5$, compute $|\hat{c}(u)|$ at $u = 0, 5, 20, 50$ given a Black-Scholes CF with $\sigma = 0.20$, $T = 1$, $r = 0.03$, $S_0 = 100$. How fast does $|\hat{c}(u)|$ decay?

??? success "Solution to Exercise 1"
    **Factoring the denominator:** Write the denominator as

    $$
    \alpha^2 + \alpha - u^2 + i(2\alpha+1)u
    $$

    We claim this equals $-(u - i\alpha)(u - i(\alpha+1))$. Expanding:

    $$
    (u - i\alpha)(u - i(\alpha+1)) = u^2 - i(\alpha+1)u - i\alpha u + i^2\alpha(\alpha+1)
    $$

    $$
    = u^2 - i(2\alpha+1)u - \alpha(\alpha+1) = u^2 - i(2\alpha+1)u - \alpha^2 - \alpha
    $$

    Negating: $-(u - i\alpha)(u - i(\alpha+1)) = -u^2 + i(2\alpha+1)u + \alpha^2 + \alpha$, which matches the denominator.

    **Computing $|\hat{c}(u)|$ for $\alpha = 1.5$:** The Black-Scholes CF is

    $$
    \varphi(u) = \exp\!\left(iu\!\left[\log 100 + (0.03 - 0.02)T\right] - \frac{0.04\,u^2\cdot 1}{2}\right)
    $$

    with $r = 0.03$, $\sigma = 0.20$, $T = 1$, $S_0 = 100$. The numerator of $\hat{c}$ evaluates $\varphi(u - 2.5i)$. The modulus of $\varphi(u - iv)$ for real $u$ is

    $$
    |\varphi(u - iv)| = \exp\!\left(v\!\left[\log S_0 + (r - \tfrac{\sigma^2}{2})T\right] - \frac{\sigma^2 T}{2}(u^2 - v^2)\right)
    $$

    For the denominator at $\alpha = 1.5$: $|{-}(u - 1.5i)(u - 2.5i)| = \sqrt{u^2 + 2.25}\cdot\sqrt{u^2 + 6.25}$.

    At $u = 0$: $|\hat{c}(0)|$ involves $|\varphi(-2.5i)|/\sqrt{2.25\cdot 6.25} = |\varphi(-2.5i)|/3.75$. Since $\varphi(-2.5i) = \mathbb{E}[S_T^{2.5}]$ which is a finite positive number, $|\hat{c}(0)|$ is moderate.

    At $u = 5$: The Gaussian decay $e^{-0.02\cdot 25} = e^{-0.5} \approx 0.607$ reduces the numerator, while the denominator grows as $\sqrt{27.25}\cdot\sqrt{31.25} \approx 29.2$.

    At $u = 20$: $e^{-0.02\cdot 400} = e^{-8} \approx 3.4 \times 10^{-4}$, and the denominator is $\approx u^2 = 400$.

    At $u = 50$: $e^{-0.02\cdot 2500} = e^{-50} \approx 1.9 \times 10^{-22}$, with denominator $\approx 2500$.

    The decay is dominated by the Gaussian factor $e^{-\sigma^2 u^2 T/2}$, so $|\hat{c}(u)|$ decays as $e^{-0.02u^2}/u^2$ for large $u$. This extremely rapid decay means the integral converges quickly and $u_{\max} = 50$--$100$ is more than sufficient.

---

**Exercise 2.** The FFT requires the log-strike spacing and frequency spacing to satisfy $\Delta u \cdot \Delta k = 2\pi/N$. For $N = 4096$ and $\Delta u = 0.01$: (a) compute $\Delta k$; (b) find the range of log-strikes $[k_{\min}, k_{\max}]$; (c) convert to actual strikes $K = e^k$ and determine the strike range for $S_0 = 100$. Are ITM and OTM options well-covered?

??? success "Solution to Exercise 2"
    **(a)** With $N = 4096$ and $\Delta u = 0.01$:

    $$
    \Delta k = \frac{2\pi}{N\cdot\Delta u} = \frac{2\pi}{4096\times 0.01} = \frac{2\pi}{40.96} \approx 0.1534
    $$

    **(b)** The log-strike grid is $k_j = -b + j\Delta k$ for $j = 0, \ldots, 4095$, where $b = N\Delta k/2 = 4096 \times 0.1534 / 2 \approx 314.16$. So

    $$
    k_{\min} = -b \approx -314.16, \qquad k_{\max} = -b + (N-1)\Delta k \approx -314.16 + 4095\times 0.1534 \approx 314.0
    $$

    **(c)** Converting to strikes $K = e^k$ with $S_0 = 100$: $K_{\min} = e^{-314} \approx 0$ (effectively zero), and $K_{\max} = e^{314}$, which is astronomically large. However, only strikes near $S_0$ are financially meaningful. The log-moneyness relative to $S_0 = 100$ is $k - \log 100 = k - 4.605$. Strikes in the range $K \in [50, 200]$ correspond to $k \in [3.91, 5.30]$, which is well within the grid.

    The grid spacing in strike space near ATM ($k \approx 4.6$) is $\Delta K \approx K\,\Delta k \approx 100 \times 0.1534 \approx 15.3$. This is relatively coarse. For finer strike resolution, either increase $N$ or decrease $\Delta u$ (at the cost of integration accuracy). Interpolation between grid points is typically used to obtain prices at specific strikes. Both ITM and OTM options are well-covered.

---

**Exercise 3.** The Lewis formula is

$$
C(K) = S_0 e^{-qT} - \frac{\sqrt{S_0 K}\,e^{-(r+q)T/2}}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{iuk}\varphi(u - i/2)}{u^2 + 1/4}\right]du
$$

Show that for the Black-Scholes CF $\varphi(u) = \exp(iu[(r-q-\sigma^2/2)T] - \sigma^2 u^2 T/2)$, the formula recovers the standard Black-Scholes call price. (Hint: the integral reduces to a known Fourier integral related to the normal distribution.)

??? success "Solution to Exercise 3"
    Substitute the BS characteristic function $\varphi(u) = \exp\!\left(iu\mu T - \frac{\sigma^2 u^2 T}{2}\right)$ with $\mu = r - q - \sigma^2/2$ into the Lewis formula. We need $\varphi(u - i/2)$:

    $$
    \varphi(u - i/2) = \exp\!\left(i(u - i/2)\mu T - \frac{\sigma^2(u-i/2)^2 T}{2}\right)
    $$

    Expanding $(u - i/2)^2 = u^2 - iu + 1/4$ (note: this is $-1/4$ for the real part shift):

    $$
    \varphi(u - i/2) = \exp\!\left(iu\mu T + \frac{\mu T}{2} - \frac{\sigma^2 T}{2}\!\left(u^2 - iu - \frac{1}{4}\right)\right)
    $$

    $$
    = \exp\!\left(\frac{\mu T}{2} + \frac{\sigma^2 T}{8}\right)\exp\!\left(iu\!\left(\mu T + \frac{\sigma^2 T}{2}\right) - \frac{\sigma^2 T u^2}{2}\right)
    $$

    Since $\mu + \sigma^2/2 = r - q$, the $u$-dependent part becomes $e^{iu(r-q)T - \sigma^2 Tu^2/2}$, which is a Gaussian Fourier factor. The Lewis integral then takes the form

    $$
    \int_0^{\infty}\text{Re}\!\left[\frac{e^{iuk}\cdot e^{iu(r-q)T - \sigma^2 Tu^2/2}}{u^2 + 1/4}\right]du
    $$

    This is a known Fourier integral of a Gaussian times a Lorentzian, whose evaluation via residue calculus or completion of the square yields terms involving the normal CDF $\Phi$. After accounting for the prefactors $S_0 e^{-qT}$ and $\sqrt{S_0 K}\,e^{-(r+q)T/2}$, the result is

    $$
    C(K) = S_0 e^{-qT}\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)
    $$

    with $d_{1,2} = \frac{\log(S_0/K) + (r - q \pm \sigma^2/2)T}{\sigma\sqrt{T}}$, which is the standard Black-Scholes formula. This confirms that the Lewis formula reduces correctly in the GBM case.

---

**Exercise 4.** The COS method approximates the density by a cosine expansion on $[a, b]$ with domain chosen using cumulants. For the Heston model with $V_0 = 0.04$, $\theta = 0.04$, $\kappa = 2$, $\xi = 0.5$, $\rho = -0.7$, $T = 1$: (a) compute the first cumulant $c_1 = (r - q)T - \frac{1}{2}\mathbb{E}[\int_0^T V_s\,ds] + \log S_0$; (b) estimate $c_2 \approx \mathbb{E}[\int_0^T V_s\,ds]$ (the approximate variance); (c) choose $[a, b]$ using $a = c_1 - 10\sqrt{c_2}$, $b = c_1 + 10\sqrt{c_2}$.

??? success "Solution to Exercise 4"
    **(a) First cumulant:** The first cumulant of $X_T = \log S_T$ under $\mathbb{Q}$ is

    $$
    c_1 = \log S_0 + (r - q)T - \frac{1}{2}\mathbb{E}\!\left[\int_0^T V_s\,ds\right]
    $$

    For the Heston model, $\mathbb{E}[V_s] = \theta + (V_0 - \theta)e^{-\kappa s}$, so

    $$
    \mathbb{E}\!\left[\int_0^T V_s\,ds\right] = \theta T + (V_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa}
    $$

    With $V_0 = 0.04$, $\theta = 0.04$, $\kappa = 2$, $T = 1$: since $V_0 = \theta$, this simplifies to $\mathbb{E}[\int_0^T V_s\,ds] = \theta T = 0.04$. Taking $r = 0.03$, $q = 0$, $S_0 = 100$:

    $$
    c_1 = \log 100 + 0.03 - 0.02 = 4.6052 + 0.01 = 4.6152
    $$

    **(b) Second cumulant (approximate variance):** The approximate variance of $X_T$ is $c_2 \approx \mathbb{E}[\int_0^T V_s\,ds] = 0.04$. (A more precise formula includes terms from the vol-of-vol, but this is the leading approximation.)

    **(c) Domain selection:** With $c_1 \approx 4.6152$ and $c_2 \approx 0.04$:

    $$
    a = c_1 - 10\sqrt{c_2} = 4.6152 - 10\times 0.2 = 4.6152 - 2.0 = 2.6152
    $$

    $$
    b = c_1 + 10\sqrt{c_2} = 4.6152 + 2.0 = 6.6152
    $$

    In terms of spot price, this corresponds to $[e^{2.615}, e^{6.615}] = [13.67, 744.0]$, which comfortably covers all financially relevant strikes around $S_0 = 100$.

---

**Exercise 5.** Compare the computational cost of pricing a single European call option using: (a) Carr-Madan FFT with $N = 4096$; (b) COS method with $N = 128$ terms; (c) direct numerical integration (trapezoidal rule) with 1000 points. Express costs in terms of the number of characteristic function evaluations. If each CF evaluation takes $1\,\mu s$, estimate wall-clock times for each method.

??? success "Solution to Exercise 5"
    **(a) Carr-Madan FFT with $N = 4096$:** The FFT itself costs $O(N\log_2 N) = O(4096\times 12) \approx 49{,}000$ operations. However, the CF is evaluated at each of the $N = 4096$ frequency points, so the number of CF evaluations is 4096. At $1\,\mu s$ per evaluation: $\approx 4.1\,\text{ms}$ for CF evaluations plus FFT overhead, total $\approx 5\,\text{ms}$.

    **(b) COS method with $N = 128$ terms:** Each term requires one CF evaluation, so 128 CF evaluations. For $N_K$ strikes, the summation is $O(N\cdot N_K)$, but for a single strike $N_K = 1$: 128 evaluations. Time: $128\,\mu s \approx 0.13\,\text{ms}$.

    **(c) Direct trapezoidal rule with 1000 points:** Each quadrature point requires one CF evaluation: 1000 evaluations. Time: $1000\,\mu s = 1\,\text{ms}$.

    **Summary:**

    | Method | CF evaluations | Estimated time |
    |--------|---------------|----------------|
    | Carr-Madan FFT | 4096 | $\approx 5$ ms |
    | COS ($N=128$) | 128 | $\approx 0.13$ ms |
    | Trapezoidal ($N=1000$) | 1000 | $\approx 1$ ms |

    For a single strike, COS is fastest. The FFT appears slowest per single strike, but it simultaneously produces prices at all $N = 4096$ log-strike grid points. For calibration across many strikes, the FFT cost is amortized: the per-strike cost is $\approx 5\,\text{ms}/4096 \approx 1.2\,\mu s$.

---

**Exercise 6.** A digital call option pays $\$1$ if $S_T > K$. Its price under a stochastic volatility model is

$$
D_C(K) = e^{-rT}\left[\frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\text{Re}\left[\frac{e^{-iu\log K}\varphi(u)}{iu}\right]du\right]
$$

Explain why this formula is simply the discounted risk-neutral probability $\mathbb{Q}(S_T > K)$ expressed via Gil-Pelaez inversion. If the underlying follows a Heston model, describe how the smile affects digital prices compared to Black-Scholes digital prices at strikes below and above ATM.

??? success "Solution to Exercise 6"
    The price of a digital call paying $\$1$ if $S_T > K$ is simply the discounted risk-neutral probability:

    $$
    D_C(K) = e^{-rT}\mathbb{Q}(S_T > K) = e^{-rT}\mathbb{Q}(X_T > \log K) = e^{-rT}[1 - F_{X_T}(\log K)]
    $$

    By the Gil-Pelaez inversion formula, the CDF is

    $$
    F_{X_T}(x) = \frac{1}{2} - \frac{1}{\pi}\int_0^{\infty}\text{Re}\!\left[\frac{e^{-iux}\varphi(u)}{iu}\right]du
    $$

    Therefore $1 - F_{X_T}(\log K) = \frac{1}{2} + \frac{1}{\pi}\int_0^{\infty}\text{Re}\!\left[\frac{e^{-iu\log K}\varphi(u)}{iu}\right]du$, and multiplying by $e^{-rT}$ gives the digital call formula. This is indeed just the Gil-Pelaez inversion applied to $\mathbb{Q}(X_T > \log K)$, discounted to present value.

    **Effect of the Heston smile on digital prices:** Under Black-Scholes, the risk-neutral density is log-normal. Under Heston, the density exhibits fatter tails and negative skew (when $\rho < 0$).

    - **Below ATM ($K < S_0 e^{(r-q)T}$):** The digital call pays when $S_T > K$, which is already likely. The Heston model with $\rho < 0$ assigns more probability to the left tail (large downward moves), which slightly reduces $\mathbb{Q}(S_T > K)$ compared to BS for moderately below-ATM strikes. However, the fatter right tail partially offsets this. The net effect depends on the specific strike.

    - **Above ATM ($K > S_0 e^{(r-q)T}$):** The digital pays only if the stock rises above $K$. With negative skew, the Heston model has a heavier left tail but also fatter right tail than BS. For moderately OTM calls, the heavier left tail reduces $\mathbb{Q}(S_T > K)$, making Heston digital call prices lower than BS. For far OTM calls, the fatter right tail of Heston can make digital prices higher than BS.

    The volatility smile encodes exactly these deviations: higher implied volatilities at low strikes reflect the heavier left tail, directly affecting digital option prices.

---

**Exercise 7.** Implement (or describe the steps to implement) a put-call parity check for the Carr-Madan FFT pricer. Specifically, for a given set of Heston parameters, compute $C(K)$ and $P(K) = C(K) - S_0 e^{-qT} + K e^{-rT}$ at several strikes. Explain why put-call parity provides a useful validation: it tests whether the martingale condition $\varphi(-i) = e^{(r-q)T}$ is satisfied, and whether the numerical integration is accurate. What is the typical magnitude of put-call parity violations in a well-implemented FFT pricer?

??? success "Solution to Exercise 7"
    **Implementation steps:**

    1. Choose Heston parameters (e.g., $V_0 = 0.04$, $\theta = 0.04$, $\kappa = 2$, $\xi = 0.5$, $\rho = -0.7$, $r = 0.03$, $q = 0.01$, $T = 1$, $S_0 = 100$).
    2. Run the Carr-Madan FFT to obtain call prices $C(K_j)$ on the log-strike grid.
    3. Compute put prices from parity: $P(K_j) = C(K_j) - S_0 e^{-qT} + K_j e^{-rT}$.
    4. Alternatively, run the FFT for puts directly (using a put-damped transform with $\alpha < 0$) and compare.
    5. The put-call parity violation is $\epsilon(K) = |C(K) - P(K) - S_0 e^{-qT} + K e^{-rT}|$.

    **Why this is a useful validation:** Put-call parity $C - P = S_0 e^{-qT} - Ke^{-rT}$ holds model-independently for European options whenever the discounted asset price is a martingale. In the Fourier framework, this identity is equivalent to the martingale condition $\varphi(-i) = e^{(r-q)T}$. If the CF implementation has a bug (wrong branch of the square root, incorrect drift term, etc.), the martingale condition will be violated, and parity will fail. Additionally, parity tests the accuracy of the numerical integration: truncation errors, discretization errors, or insufficient grid resolution will produce different errors for calls and puts, showing up as parity violations.

    **Typical magnitude:** In a well-implemented FFT pricer with $N = 4096$, $\Delta u = 0.01$, and properly chosen $\alpha$, put-call parity violations are at the level of $10^{-8}$ to $10^{-10}$ (relative to the option price), limited by machine precision and quadrature accuracy. Violations larger than $10^{-4}$ indicate a bug or poor parameter choices. Common causes of larger violations include: incorrect $\alpha$ (moment explosion), insufficient $u_{\max}$ (truncation), or branch-cut issues in the CF evaluation.
