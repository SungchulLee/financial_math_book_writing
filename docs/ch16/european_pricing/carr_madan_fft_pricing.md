# Carr-Madan FFT Pricing Method

The Carr-Madan method enables fast computation of European option prices by recovering the probability density from the characteristic function using Fast Fourier Transform (FFT). This is particularly powerful for models like Heston where the characteristic function is known in closed form.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Understand density recovery from characteristic functions
    2. Apply FFT to compute option prices efficiently
    3. Handle computational issues (grid design, boundary corrections)

---

## Density Recovery from Characteristic Function

The relationship between the probability density \(f(x)\) and the characteristic function \(\varphi(u) = \mathbb{E}[e^{iuX}]\) is given by the Fourier inversion formula:

\[
f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-iux}\varphi(u) du
\]

For real-valued \(x\), using symmetry properties:

\[
f(x) = \frac{1}{\pi} \mathbb{Re}\left(\int_0^{\infty} e^{-iux}\varphi(u) du\right)
\]

---

## FFT Implementation

To apply FFT efficiently, discretize the integration domain. Let:

- \(u_n = \Delta_u \cdot n\) for \(n = 0, 1, \ldots, N-1\) (frequency grid)
- \(x_k = x_{\min} + \Delta_x \cdot k\) for \(k = 0, 1, \ldots, N-1\) (space grid)

The crucial relationship linking grid sizes is:

\[
\Delta_u \cdot \Delta_x = \frac{2\pi}{N}
\]

This ensures the discrete transform is consistent with FFT requirements (usually \(N = 2^m\)).

### Trapezoidal Rule with Boundary Correction

Approximate the integral using trapezoidal rule:

\[
f(x_k) \approx \frac{\Delta_u}{\pi} \mathbb{Re}\left(\sum_{n=0}^{N-1} e^{-iu_n x_k}\varphi(u_n) - \frac{1}{2}(\text{first} + \text{last})\right)
\]

The boundary correction terms account for the approximation of the infinite integral by \([0, u_{\max}]\).

### FFT Transformation

Factor out the phase shift:

\[
\phi(u_n) := e^{-ix_{\min}u_n}\varphi(u_n)
\]

Then:

\[
f(x_k) \approx \frac{\Delta_u}{\pi} \mathbb{Re}\left(\sum_{n=0}^{N-1} e^{-i\frac{2\pi}{N}nk} \phi(u_n) - \frac{1}{2}(\text{boundary})\right)
\]

The exponential sum is precisely an FFT (inverse Fourier transform), which can be computed in \(O(N \log N)\) time.

---

## Grid Design Considerations

1. **Choice of \(\Delta_u\):** Determines the resolution in space. Smaller \(\Delta_u\) gives finer spatial grid.

2. **Choice of \(u_{\max}\):** Controls the truncation error in density recovery. For Heston, \(u_{\max} = 20\) to \(100\) is typically sufficient depending on the required accuracy.

3. **Space bounds \([x_{\min}, x_{\max}]\):** Should encompass the region where the density is significant. For log-returns, typically \([x_{\min}, x_{\max}] \approx [\log(0.5), \log(2)]\) relative to the forward price.

4. **Number of points \(N\):** Must be a power of 2 for efficient FFT. Doubling \(N\) doubles computational cost but cuts grid spacing in half.

---

## Option Pricing via FFT

Once the density \(f(x)\) is recovered, European option prices are computed via:

\[
V(t, S) = e^{-r\tau} \int_{-\infty}^{\infty} \max(Se^x - K, 0) \cdot f(x) dx
\]

The integral is evaluated numerically on the discretized grid:

\[
V(t, S) \approx e^{-r\tau} \sum_{k} V(x_k) \cdot f(x_k) \cdot \Delta_x
\]

where \(V(x) = \max(Se^x - K, 0)\) for a call option.

---

## Advantages and Limitations

**Advantages:**
- Extremely fast once FFT is computed (multiple strikes in parallel)
- Works for any model with known characteristic function
- Automatically handles Greeks via re-evaluation on shifted grids

**Limitations:**
- FFT requires equidistant grid (adaptive grids not directly applicable)
- Boundary effects may require large \(u_{\max}\)
- Accuracy sensitive to grid design choices
- Less efficient for a single strike compared to other methods

---

## Computational Example

For Heston pricing with \(S = 100\), \(K = [80, \ldots, 120]\), \(\tau = 1/12\) year:

1. Set \(\Delta_u = 0.5\), compute \(\Delta_x = 2\pi / (N \Delta_u)\) for \(N = 2^{11} = 2048\)
2. Evaluate Heston characteristic function at \(u_n\) for \(n = 0, \ldots, N-1\)
3. Apply FFT to recover density on \([x_{\min}, x_{\max}]\)
4. Price all strikes in a single pass

Total computation time: typically milliseconds for all strikes.

---

## Summary

The Carr-Madan FFT method leverages Fourier analysis to convert characteristic function evaluation into efficient option pricing. Its speed and generality make it the gold standard for pricing under stochastic volatility models, especially when multiple strikes need to be priced simultaneously. The method highlights the practical importance of affine models that admit closed-form characteristic functions.
