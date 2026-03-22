# Convergence and Accuracy Benchmarks

The COS method's appeal lies in its exponential convergence rate for smooth densities, but actual performance depends on the payoff smoothness, the choice of truncation interval, the number of expansion terms $N$, and the specific Heston parameter regime. This section establishes theoretical convergence rates, compares COS accuracy against FFT and Monte Carlo benchmarks, and provides practical guidelines for selecting $N$ across different use cases.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State and prove the exponential convergence rate of the COS method for analytic densities
    2. Compare COS accuracy and speed against FFT and Monte Carlo for Heston pricing
    3. Identify parameter regimes where COS convergence degrades
    4. Select appropriate $N$ for a target accuracy level

---

## Intuition

Fourier cosine series converge at a rate determined by the smoothness of the function being approximated. For an analytic function (infinitely differentiable with convergent Taylor series), the Fourier coefficients decay exponentially, and the truncation error after $N$ terms vanishes exponentially fast. The Heston log-return density is analytic on the interior of its support (being the density of a diffusion process), so the COS density approximation converges exponentially. However, the total pricing error also includes a truncation error from restricting the density to $[a, b]$ and a payoff approximation error that depends on the smoothness of the payoff function.

---

## Error Decomposition

The COS pricing error has three components.

!!! info "Theorem (COS Error Decomposition)"
    Let $V$ be the exact option price and $V_N^{[a,b]}$ the COS approximation with $N$ terms on $[a, b]$. Then

    $$
    |V - V_N^{[a,b]}| \leq \underbrace{\epsilon_{\text{trunc}}(a,b)}_{\text{domain truncation}} + \underbrace{\epsilon_{\text{series}}(N)}_{\text{series truncation}} + \underbrace{\epsilon_{\text{payoff}}(N)}_{\text{payoff approximation}}
    $$

**Domain truncation error $\epsilon_{\text{trunc}}$.** This is the mass of the density outside $[a, b]$:

$$
\epsilon_{\text{trunc}} = e^{-r\tau} \int_{\mathbb{R} \setminus [a,b]} |v(y)| f(y) \, dy
$$

For the Heston density with truncation parameter $L$, this decays as $O(e^{-cL^2})$ where $c$ depends on the tail behavior. With $L = 10$, $\epsilon_{\text{trunc}} < 10^{-15}$ for all practical Heston parameters.

**Series truncation error $\epsilon_{\text{series}}$.** This is the contribution of the omitted cosine terms:

$$
\epsilon_{\text{series}} = e^{-r\tau} \left|\sum_{k=N}^{\infty}{}' A_k V_k\right|
$$

For an analytic density, $|A_k| \leq M e^{-\alpha k}$ for some $M, \alpha > 0$, giving $\epsilon_{\text{series}} = O(e^{-\alpha N})$.

**Payoff approximation error $\epsilon_{\text{payoff}}$.** For smooth payoffs (calls, puts), $|V_k| = O(1/k^2)$, so this error is dominated by $\epsilon_{\text{series}}$. For discontinuous payoffs (digitals), $|V_k| = O(1/k)$, and $\epsilon_{\text{payoff}}$ decays only algebraically.

---

## Exponential Convergence for Smooth Payoffs

The key theoretical result underpinning the COS method is the exponential decay of Fourier cosine coefficients for analytic functions.

!!! info "Theorem (Exponential Convergence)"
    Let $f$ be the conditional density of $\log S_T$ under the Heston model. If $f$ admits an analytic continuation to a strip $|\text{Im}(y)| < \beta$ in the complex plane, then the Fourier cosine coefficients satisfy

    $$
    |A_k| \leq C e^{-\beta k\pi / (b-a)}
    $$

    for a constant $C > 0$. Consequently, for a European call or put with $N$ COS terms:

    $$
    |V - V_N| = O\!\left(e^{-\beta N\pi/(b-a)}\right)
    $$

**Proof sketch.** The Fourier cosine coefficients are $A_k = \frac{2}{b-a}\text{Re}[\hat{f}(k\pi/(b-a))]$ where $\hat{f}$ is the characteristic function. The analyticity of $f$ in a strip of width $\beta$ implies $|\hat{f}(u)| \leq C e^{-\beta|u|}$ by the Paley-Wiener theorem. Setting $u = k\pi/(b-a)$ gives the exponential bound. The pricing error then follows from $|V_k| = O(1/k^2)$ for smooth payoffs. $\square$

The strip width $\beta$ is related to the **moment explosion** boundary of the Heston model: $\beta = p_+ - 1$ where $p_+$ is the critical moment exponent. For typical Heston parameters, $\beta > 1$, ensuring rapid convergence.

---

## Algebraic Convergence for Discontinuous Payoffs

For digital options with a discontinuity at $y = \log K$, the convergence rate drops significantly.

!!! info "Proposition (Algebraic Convergence for Digitals)"
    For a cash-or-nothing option priced by the COS method with $N$ terms:

    $$
    |V - V_N| = O(1/N^2)
    $$

    This is two orders slower in $N$ than the exponential rate achieved for vanilla options.

The $1/N^2$ rate arises because the discontinuity in the payoff produces $|V_k| = O(1/k)$, and the series $\sum_{k=N}^{\infty} |A_k V_k| \approx \sum_{k=N}^{\infty} e^{-\alpha k}/k \approx e^{-\alpha N}/N$, which is dominated by the boundary terms that converge as $O(1/N^2)$ after accounting for the density weighting.

---

## Benchmark Comparison: COS vs FFT vs Monte Carlo

The following benchmarks use the standard Heston test case: $S_0 = 100$, $K = 100$, $r = 0.05$, $q = 0$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $\tau = 1$.

### Single-Strike Pricing Accuracy

| Method | Parameters | Price | Abs Error | Time |
|--------|-----------|-------|-----------|------|
| COS $N=32$ | $L=10$ | 7.9618 | $5 \times 10^{-4}$ | 0.02 ms |
| COS $N=64$ | $L=10$ | 7.96234 | $1 \times 10^{-6}$ | 0.03 ms |
| COS $N=128$ | $L=10$ | 7.962344 | $3 \times 10^{-9}$ | 0.05 ms |
| FFT $N=2^{10}$ | $\Delta_u = 0.25$ | 7.9621 | $2 \times 10^{-4}$ | 0.5 ms |
| FFT $N=2^{12}$ | $\Delta_u = 0.25$ | 7.96233 | $1 \times 10^{-5}$ | 1.5 ms |
| FFT $N=2^{14}$ | $\Delta_u = 0.25$ | 7.962344 | $5 \times 10^{-8}$ | 5 ms |
| MC $10^5$ paths | QE scheme | 7.97 | $8 \times 10^{-3}$ | 50 ms |
| MC $10^6$ paths | QE scheme | 7.963 | $1 \times 10^{-3}$ | 500 ms |
| MC $10^7$ paths | QE scheme | 7.9624 | $1 \times 10^{-4}$ | 5 s |

The COS method achieves nine-digit accuracy 100,000 times faster than Monte Carlo with $10^7$ paths.

### Multi-Strike Pricing

For pricing across 50 strikes simultaneously:

| Method | Time for 50 Strikes | Accuracy |
|--------|--------------------:|----------|
| COS $N=128$ | 0.1 ms | $10^{-9}$ |
| FFT $N=2^{12}$ | 1.5 ms | $10^{-5}$ |
| Gil-Pelaez (adaptive) | 25 ms | $10^{-10}$ |
| Monte Carlo $10^6$ | 500 ms | $10^{-3}$ |

The FFT computes all 50 strikes in a single pass (interpolating from the FFT grid), while COS evaluates each strike separately but with very fast per-strike cost.

---

## Parameter Sensitivity of Convergence

The COS convergence rate depends on Heston parameters through two mechanisms: the density smoothness (affecting $\alpha$) and the density spread (affecting $b - a$).

### Effect of Vol-of-Vol $\xi$

Higher $\xi$ produces heavier tails and a wider density, requiring more COS terms.

| $\xi$ | $N$ for $10^{-6}$ accuracy | $N$ for $10^{-9}$ accuracy |
|-------|---------------------------|---------------------------|
| 0.1 | 32 | 64 |
| 0.3 | 64 | 128 |
| 0.5 | 96 | 192 |
| 1.0 | 128 | 256 |

### Effect of Maturity $\tau$

Longer maturities produce wider densities, increasing the required $N$.

| $\tau$ | $N$ for $10^{-6}$ accuracy |
|--------|---------------------------|
| 0.1 | 32 |
| 0.5 | 48 |
| 1.0 | 64 |
| 5.0 | 96 |
| 10.0 | 128 |

### Effect of Correlation $\rho$

Extreme negative correlation produces strongly skewed densities but does not significantly affect the convergence rate (the density remains smooth).

| $\rho$ | $N$ for $10^{-6}$ accuracy |
|--------|---------------------------|
| $-0.9$ | 64 |
| $-0.5$ | 64 |
| $0.0$ | 64 |
| $0.5$ | 64 |

!!! tip "Rule of Thumb"
    For the vast majority of practical Heston parameter sets:

    - **$N = 64$**: sufficient for 5--6 digits of accuracy (calibration)
    - **$N = 128$**: sufficient for 8--9 digits of accuracy (benchmark pricing)
    - **$N = 256$**: sufficient for machine precision (validation and testing)

    Only extreme parameters ($\xi > 0.8$ or $\tau > 10$) require $N > 128$.

---

## Truncation Range Sensitivity

The choice of $L$ in the cumulant-based truncation $[a, b]$ affects both the domain truncation error and the series convergence (wider intervals need more terms).

| $L$ | Domain Error | $N$ for $10^{-8}$ | Total Time |
|-----|-------------|-------------------|------------|
| 5 | $10^{-4}$ | 48 | Fast but inaccurate |
| 8 | $10^{-10}$ | 80 | Good balance |
| 10 | $10^{-15}$ | 96 | Recommended default |
| 15 | $10^{-30}$ | 144 | Overkill |

!!! warning "Overly Narrow Truncation"
    Setting $L < 6$ risks significant pricing errors for out-of-the-money options whose value depends on the density tails. This is the most common implementation error: the COS price appears to converge in $N$ (because the series error vanishes) but converges to the wrong value (because the domain error dominates).

---

## Comparison with Semi-Analytical Benchmarks

For validation, the COS method should be compared against independent semi-analytical methods.

**Benchmark 1: Lewis (2001) formula.** The call price can be written as a single contour integral in the complex strip. This provides an independent check using different numerical integration.

**Benchmark 2: High-order Gauss-Laguerre quadrature.** Applied to the Gil-Pelaez formula with 64 or 128 nodes, this gives 12--15 digit accuracy and serves as the reference for all COS benchmarks.

**Benchmark 3: Carr-Madan FFT with Richardson extrapolation.** Two FFT runs with $N$ and $2N$ points, extrapolated, provide 8--10 digit accuracy.

??? example "Cross-Validation Table"
    For $S_0 = 100$, $K = 100$, $r = 0.05$, $q = 0$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $\tau = 1$:

    | Method | Call Price | Digits Agreed |
    |--------|-----------|---------------|
    | COS $N=256$ | 7.96234412... | 12 |
    | Gauss-Laguerre 128 | 7.96234412... | 15 |
    | FFT $2^{14}$ extrapolated | 7.96234412... | 10 |
    | Lewis contour | 7.96234412... | 12 |

    All four methods agree to 10+ significant digits, providing strong confidence in the COS implementation.

---

## Summary

The COS method converges exponentially fast for European calls and puts under the Heston model, achieving six-digit accuracy with $N = 64$ terms and machine precision with $N = 256$. The convergence rate depends primarily on the vol-of-vol $\xi$ (heavier tails require more terms) and maturity $\tau$ (wider densities need wider truncation intervals). For discontinuous payoffs such as digitals, convergence drops to algebraic $O(1/N^2)$, requiring smoothing techniques for competitive accuracy. In direct benchmarks, the COS method is 10--50 times faster than Carr-Madan FFT for single-strike pricing and 100,000 times faster than Monte Carlo, while maintaining comparable or superior accuracy. The recommended defaults of $N = 64$ for calibration and $N = 128$ for pricing cover virtually all practical Heston parameter regimes.
