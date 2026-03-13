# COS Method Applied to Heston

The Fourier Cosine (COS) method extends the Fourier inversion principle to construct an extremely fast pricing algorithm. It combines Fourier series expansions with characteristic functions to achieve rapid convergence and exceptional computational efficiency.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Understand Fourier cosine series expansions of densities
    2. Derive closed-form payoff coefficients for European options
    3. Apply the COS method to Heston option pricing

---

## Fourier Cosine Series Representation

Assume the density \(f(x)\) is supported on the interval \([a, b]\). The Fourier cosine series expansion is:

\[
f(x) \approx \sum_{k=0}^{n-1} \mathop{'} A_k \cos\left(k\pi \frac{x - a}{b - a}\right)
\]

where the prime notation \(\sum \mathop{'}\) indicates the first term is weighted by \(1/2\), and the coefficients are:

\[
A_k = \frac{2}{b-a} \mathbb{Re}\left[\varphi\left(\frac{k\pi}{b-a}\right) e^{-i\frac{k\pi a}{b-a}}\right]
\]

Here \(\varphi(u)\) is the characteristic function. The key advantage is that \(A_k\) is trivial to compute if \(\varphi\) is available.

---

## COS Method for Option Pricing

The option price under risk-neutral valuation is:

\[
V(t, S) = e^{-r\tau} \mathbb{E}^{\mathbb{Q}}[V(T, x) | \mathcal{F}(t)]
\]

where \(x = \log S(T)\). Substituting the cosine expansion of the density:

\[
V(t, S) \approx e^{-r\tau} \frac{b-a}{2} \sum_{k=0}^{n-1} \mathop{'} A_k H_k
\]

Here:
- \(A_k\) are the density Fourier coefficients (computed from the characteristic function)
- \(H_k\) are the payoff coefficients, defined as:

\[
H_k = \frac{2}{b-a} \int_a^b V(T, x) \cos\left(k\pi \frac{x - a}{b - a}\right) dx
\]

---

## Closed-Form Payoff Coefficients

For European calls and puts, the payoff integrals have closed-form solutions using auxiliary functions:

**Chi function:**
\[
\chi_k(c, d) := \int_c^d e^x \cos\left(k\pi \frac{x - a}{b - a}\right) dx
\]

\[
= \frac{1}{1 + \left(\frac{k\pi}{b-a}\right)^2} \left[
\cos\left(k\pi \frac{d-a}{b-a}\right)e^d - \cos\left(k\pi \frac{c-a}{b-a}\right)e^c
\right.
\]

\[
\left. + \frac{k\pi}{b-a}\sin\left(k\pi \frac{d-a}{b-a}\right)e^d - \frac{k\pi}{b-a}\sin\left(k\pi \frac{c-a}{b-a}\right)e^c
\right]
\]

**Psi function:**
\[
\psi_k(c, d) := \int_c^d \cos\left(k\pi \frac{x - a}{b - a}\right) dx
\]

\[
= \begin{cases}
\frac{b-a}{k\pi}\left[\sin\left(k\pi \frac{d-a}{b-a}\right) - \sin\left(k\pi \frac{c-a}{b-a}\right)\right] & k \neq 0\\
d - c & k = 0
\end{cases}
\]

**Call payoff coefficients:**
\[
H_k^{\text{call}} = \frac{2}{b-a} \chi_k(\log K, b) - \frac{2K}{b-a} \psi_k(\log K, b)
\]

**Put payoff coefficients:**
\[
H_k^{\text{put}} = \frac{2K}{b-a} \psi_k(a, \log K) - \frac{2}{b-a} \chi_k(a, \log K)
\]

---

## COS Method vs FFT Method

| Aspect | COS | FFT |
|--------|-----|-----|
| Density grid | Cosine series (adaptive) | Equidistant FFT grid |
| Convergence | Exponentially fast | Algebraic |
| # of terms needed | 32-128 typically | 512-4096 typically |
| Payoff formulas | Closed-form for vanilla | Numerical integration |
| Speed for single strike | Very fast | Slower |
| Speed for many strikes | Moderate | Very fast |

The COS method converges **exponentially** fast, making it one of the most efficient Fourier methods for vanilla European options.

---

## Implementation Steps for Heston

1. **Set bounds:** Choose \([a, b]\) to contain the significant mass of the log-return density (typically \(\pm 3 \times \text{standard deviation}\))

2. **Compute characteristic function:** For Heston, evaluate the closed-form CF at frequency points \(u_k = \frac{k\pi}{b-a}\)

3. **Compute \(A_k\):** Use the formula:
   \[
   A_k = \frac{2}{b-a} \mathbb{Re}\left[\varphi\left(\frac{k\pi}{b-a}\right) e^{-i\frac{k\pi a}{b-a}}\right]
   \]

4. **Compute \(H_k\):** For each strike \(K\), use the closed-form payoff coefficients

5. **Sum the series:**
   \[
   V = e^{-r\tau} \frac{b-a}{2} \sum_{k=0}^{n-1} \mathop{'} A_k H_k
   \]
   with typically \(n = 64\) to \(128\)

---

## Advantages of COS Method

1. **Extreme speed:** Pricing hundreds of strikes in milliseconds
2. **Exponential convergence:** Exponentially fast in the number of terms \(n\)
3. **Simplicity:** No FFT algorithm needed, just a direct sum
4. **Flexibility:** Easy to extend to exotic options with integrable payoffs
5. **Stability:** More stable numerically than FFT for moderate accuracy requirements

---

## Limitations and Extensions

**Limitations:**
- Payoff must be integrable (rules out barrier/digital options without modification)
- Choice of bounds \([a, b]\) affects convergence
- Difficult to apply to path-dependent options

**Extensions:**
- Digital options: piecewise polynomial approximation
- Barrier options: combination with finite-difference solver
- American options: backward induction with COS method at each step

---

## Summary

The COS method represents a significant advancement in computational finance, combining the analytical power of Fourier analysis with the practical efficiency of series summation. For European options under the Heston model, it typically achieves 5-8 significant digits of accuracy with only 32-64 terms, making it the preferred choice in many production systems. The exponentially fast convergence and closed-form payoff coefficients make it an exemplary application of Fourier methods in quantitative finance.
