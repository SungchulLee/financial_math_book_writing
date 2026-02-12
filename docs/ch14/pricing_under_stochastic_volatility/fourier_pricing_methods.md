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

### Choosing $\alpha$

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
