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

---

## Exercises

**Exercise 1.**
Given $N = 2048$ and frequency spacing $\Delta_u = 0.5$, compute the log-strike spacing $\Delta_x = 2\pi / (N \Delta_u)$ and the total log-strike range $N \Delta_x$. If the spot price is $S_0 = 100$, what are the minimum and maximum dollar strikes on the grid? Are the extreme strikes practically relevant for pricing?

---

**Exercise 2.**
The Fourier inversion formula recovers the density from the characteristic function:

$$
f(x) = \frac{1}{\pi} \operatorname{Re}\!\left(\int_0^{\infty} e^{-iux}\varphi(u) \, du\right)
$$

Explain why the integration over $(-\infty, \infty)$ reduces to an integral over $[0, \infty)$. What symmetry property of $\varphi(u)$ is used? Hint: for a real-valued random variable, $\varphi(-u) = \overline{\varphi(u)}$.

---

**Exercise 3.**
The FFT computes $N$ equally-spaced prices in $\mathcal{O}(N \log N)$ operations. If $N = 4096$, how many operations does the FFT require? Compare this to evaluating $M = 50$ individual Gil-Pelaez integrals, each requiring 64 CF evaluations. At what value of $M$ does the FFT become more efficient than individual Gil-Pelaez pricing?

---

**Exercise 4.**
Suppose the density recovered by FFT shows spurious oscillations (ringing) near the boundaries of the log-strike grid. Propose two remedies: (a) increasing $u_{\max}$ (explain why), and (b) applying a windowing function to the frequency-domain data before the inverse FFT. Describe the trade-off between reducing boundary effects and losing resolution.

---

**Exercise 5.**
The Carr-Madan method produces prices on an equally-spaced log-strike grid, but market strikes are irregularly spaced. Describe how to interpolate the FFT output to obtain prices at arbitrary strikes. Would you use linear interpolation in log-strike space or cubic spline interpolation? Discuss the accuracy implications for deep OTM options where the price function is convex.

---

**Exercise 6.**
For a Heston model with $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$, the characteristic function decays as $|\varphi(u)| \sim e^{-cu^2}$ for large $u$. Estimate the truncation error when integrating up to $u_{\max} = 50$ versus $u_{\max} = 100$. Is the improvement worth the additional CF evaluations?

---

**Exercise 7.**
The FFT prices calls for all strikes simultaneously, but a calibration requires both call prices and implied volatilities. After obtaining the FFT price vector, describe the computational pipeline to convert prices to implied volatilities. If $M = 45$ calibration strikes do not lie on the FFT grid, estimate the total number of Newton-Raphson iterations needed (assuming 4 iterations per strike) and compare this cost to the FFT itself.
