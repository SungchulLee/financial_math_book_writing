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

??? success "Solution to Exercise 1"
    We are given $N = 2048$ and $\Delta_u = 0.5$. The FFT constraint links the frequency and log-strike grids:

    $$
    \Delta_x = \frac{2\pi}{N \Delta_u} = \frac{2\pi}{2048 \times 0.5} = \frac{2\pi}{1024} \approx 0.006136
    $$

    The total log-strike range covered by the grid is:

    $$
    N \Delta_x = 2048 \times 0.006136 = \frac{2\pi}{\Delta_u} = \frac{2\pi}{0.5} = 4\pi \approx 12.566
    $$

    To center the grid around the at-the-money point $x = 0$ (where $x = \log(S_T / S_0)$), set $x_{\min} = -N\Delta_x / 2 \approx -6.283$ and $x_{\max} = N\Delta_x / 2 \approx 6.283$.

    The corresponding dollar strikes are $K = S_0 e^{x_k}$. At the extremes:

    $$
    K_{\min} = 100 \cdot e^{-6.283} \approx 100 \times 0.00187 = 0.187
    $$

    $$
    K_{\max} = 100 \cdot e^{6.283} \approx 100 \times 535.5 = 53{,}550
    $$

    These extreme strikes are not practically relevant for pricing. A call with $K = 0.19$ is essentially worth $S_0 e^{-q\tau} - K e^{-r\tau}$ (deep ITM), and a call with $K = 53{,}550$ has essentially zero value (deep OTM). The useful portion of the grid lies in the central region, typically $K \in [50, 200]$ (i.e., $x \in [\log 0.5, \log 2] \approx [-0.69, 0.69]$), which covers only about $0.69 / 6.28 \approx 11\%$ of each half of the grid. The excess grid points at the tails are a cost of the uniform spacing required by FFT.

---

**Exercise 2.**
The Fourier inversion formula recovers the density from the characteristic function:

$$
f(x) = \frac{1}{\pi} \operatorname{Re}\!\left(\int_0^{\infty} e^{-iux}\varphi(u) \, du\right)
$$

Explain why the integration over $(-\infty, \infty)$ reduces to an integral over $[0, \infty)$. What symmetry property of $\varphi(u)$ is used? Hint: for a real-valued random variable, $\varphi(-u) = \overline{\varphi(u)}$.

??? success "Solution to Exercise 2"
    For a real-valued random variable $X$, the characteristic function satisfies the conjugate symmetry property:

    $$
    \varphi(-u) = \mathbb{E}[e^{-iuX}] = \overline{\mathbb{E}[e^{iuX}]} = \overline{\varphi(u)}
    $$

    The full Fourier inversion formula is:

    $$
    f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{-iux}\varphi(u)\,du
    $$

    Split this into negative and positive parts and substitute $u \to -u$ in the negative part:

    $$
    f(x) = \frac{1}{2\pi}\int_0^{\infty} e^{-iux}\varphi(u)\,du + \frac{1}{2\pi}\int_0^{\infty} e^{iux}\varphi(-u)\,du
    $$

    Using $\varphi(-u) = \overline{\varphi(u)}$:

    $$
    f(x) = \frac{1}{2\pi}\int_0^{\infty}\left[e^{-iux}\varphi(u) + e^{iux}\overline{\varphi(u)}\right] du
    $$

    For any complex number $z$, $z + \overline{z} = 2\operatorname{Re}(z)$. Since $\overline{e^{-iux}\varphi(u)} = e^{iux}\overline{\varphi(u)}$, we have:

    $$
    f(x) = \frac{1}{2\pi}\int_0^{\infty} 2\operatorname{Re}\!\left[e^{-iux}\varphi(u)\right] du = \frac{1}{\pi}\operatorname{Re}\!\left(\int_0^{\infty} e^{-iux}\varphi(u)\,du\right)
    $$

    This halves the integration domain and works with a real-valued integrand, both of which are advantageous for numerical computation.

---

**Exercise 3.**
The FFT computes $N$ equally-spaced prices in $\mathcal{O}(N \log N)$ operations. If $N = 4096$, how many operations does the FFT require? Compare this to evaluating $M = 50$ individual Gil-Pelaez integrals, each requiring 64 CF evaluations. At what value of $M$ does the FFT become more efficient than individual Gil-Pelaez pricing?

??? success "Solution to Exercise 3"
    The FFT computes $N$ outputs in $\mathcal{O}(N \log_2 N)$ operations. For $N = 4096 = 2^{12}$:

    $$
    N \log_2 N = 4096 \times 12 = 49{,}152 \text{ operations}
    $$

    For individual Gil-Pelaez pricing of $M$ strikes, each requiring 64 CF evaluations:

    $$
    \text{Total GP cost} = 64M \text{ CF evaluations}
    $$

    Each CF evaluation in the FFT context involves roughly the same cost as a Gil-Pelaez CF evaluation. The FFT requires $N = 4096$ CF evaluations (one per frequency node) plus $N \log_2 N$ multiply-add operations for the transform. Since CF evaluations are far more expensive than multiply-adds (each involves exponentials, square roots, etc.), the dominant cost is the $N = 4096$ CF evaluations.

    The FFT becomes more efficient than individual Gil-Pelaez pricing when:

    $$
    N < 64M \quad \Longrightarrow \quad M > \frac{N}{64} = \frac{4096}{64} = 64
    $$

    So the FFT is more efficient when $M > 64$ strikes are needed. For $M = 50$, Gil-Pelaez requires $64 \times 50 = 3{,}200$ CF evaluations, which is fewer than the FFT's 4,096. At $M = 64$ the two methods are comparable, and for $M > 64$ the FFT wins decisively since it prices all $N = 4096$ strikes simultaneously.

---

**Exercise 4.**
Suppose the density recovered by FFT shows spurious oscillations (ringing) near the boundaries of the log-strike grid. Propose two remedies: (a) increasing $u_{\max}$ (explain why), and (b) applying a windowing function to the frequency-domain data before the inverse FFT. Describe the trade-off between reducing boundary effects and losing resolution.

??? success "Solution to Exercise 4"
    **(a) Increasing $u_{\max}$:** Spurious oscillations (Gibbs phenomenon) arise when the truncation at $u_{\max}$ cuts off the integral before the CF has fully decayed. The sharp truncation in frequency space is equivalent to convolving the true density with a sinc function, which produces ringing artifacts near discontinuities or rapid changes in the density.

    Increasing $u_{\max}$ allows the integral to capture higher-frequency components of the density, reducing the truncation error. If the CF has decayed to negligible values by $u_{\max}$, the truncation effect vanishes. Specifically, the truncation error is bounded by:

    $$
    \epsilon_{\text{trunc}} \leq \frac{1}{\pi}\int_{u_{\max}}^{\infty}\frac{|\varphi(u)|}{u}\,du
    $$

    For Heston with exponential CF decay $|\varphi(u)| \sim Ce^{-\alpha u}$, doubling $u_{\max}$ from 50 to 100 reduces this error from $O(e^{-50\alpha})$ to $O(e^{-100\alpha})$, an enormous improvement. However, doubling $u_{\max}$ while keeping $N$ fixed doubles $\Delta_u$ and thus halves $\Delta_x$, changing the spatial resolution, or if $\Delta_u$ is kept fixed, $N$ must be doubled.

    **(b) Windowing function:** Instead of sharply truncating at $u_{\max}$, multiply the frequency-domain data by a smooth window function $w(u)$ that tapers from 1 to 0 near $u_{\max}$. Common choices include:

    - **Hanning window:** $w(u) = \frac{1}{2}(1 + \cos(\pi u / u_{\max}))$
    - **Gaussian window:** $w(u) = e^{-\beta(u/u_{\max})^2}$
    - **Exponential damping:** $w(u) = e^{-\eta u}$

    The smooth taper eliminates the sharp cutoff that causes ringing, effectively replacing sinc-function side lobes with smoother decay.

    **Trade-off:** Windowing suppresses ringing but broadens the effective point spread function of the inverse transform, reducing the spatial resolution of the recovered density. Peaks become wider, and fine features of the density (e.g., sharp kurtosis effects) may be smoothed out. The optimal strategy balances truncation artifacts against resolution loss: use the largest feasible $u_{\max}$ with a mild window (e.g., exponential damping with small $\eta$) to achieve both sharp density recovery and clean boundaries.

---

**Exercise 5.**
The Carr-Madan method produces prices on an equally-spaced log-strike grid, but market strikes are irregularly spaced. Describe how to interpolate the FFT output to obtain prices at arbitrary strikes. Would you use linear interpolation in log-strike space or cubic spline interpolation? Discuss the accuracy implications for deep OTM options where the price function is convex.

??? success "Solution to Exercise 5"
    The FFT produces call prices $C(x_k)$ at log-strikes $x_k = x_{\min} + k \Delta_x$, $k = 0, \ldots, N-1$. To obtain prices at arbitrary market strikes $K_m$, compute $x_m = \log K_m$ and interpolate.

    **Linear interpolation in log-strike space** finds the grid interval $[x_k, x_{k+1}]$ containing $x_m$ and computes:

    $$
    C(x_m) = C(x_k) + \frac{x_m - x_k}{\Delta_x}(C(x_{k+1}) - C(x_k))
    $$

    This is simple and fast but only first-order accurate, with error $O(\Delta_x^2)$.

    **Cubic spline interpolation in log-strike space** fits a piecewise cubic polynomial through the grid prices, ensuring continuity of the function and its first two derivatives. The interpolation error is $O(\Delta_x^4)$, significantly better than linear.

    **Recommendation:** Cubic spline interpolation is strongly preferred. The reasons are:

    1. **Accuracy:** The $O(\Delta_x^4)$ error of cubic splines means that even with a moderately coarse FFT grid, the interpolation error is negligible.

    2. **Smoothness:** Cubic splines preserve the smoothness of the price function, which matters for computing Greeks (e.g., gamma involves second derivatives of the price with respect to strike).

    3. **Deep OTM convexity:** For deep OTM options, the price function $C(x)$ is highly convex in log-strike space. Linear interpolation systematically underestimates the price in convex regions (it lies below the true curve between grid points). This negative bias can be significant for OTM options where the price itself is small. Cubic splines, by fitting the curvature, largely eliminate this bias.

    However, one must ensure the spline does not produce negative prices (an artifact of oscillatory cubic fits near zero). A safeguard is to apply the spline to $\log C(x_k)$ instead of $C(x_k)$ in regions where prices are very small, or to floor interpolated values at zero.

---

**Exercise 6.**
For a Heston model with $v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$, the characteristic function decays as $|\varphi(u)| \sim e^{-cu^2}$ for large $u$. Estimate the truncation error when integrating up to $u_{\max} = 50$ versus $u_{\max} = 100$. Is the improvement worth the additional CF evaluations?

??? success "Solution to Exercise 6"
    The Heston CF decays for large $u$ approximately as $|\varphi(u)| \sim C e^{-c u^2}$ where $c$ depends on the variance parameters. For the given parameters ($v_0 = 0.04$, $\kappa = 2.0$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$), the dominant decay rate at large $u$ is governed by $v_0 \tau / 2$ in the short-time regime and by the mean-reversion-adjusted rate for longer maturities. For concreteness, assume the decay is approximately $|\varphi(u)| \sim e^{-\alpha u}$ with $\alpha \approx v_0 \tau / 2 = 0.02\tau$ (for the linear decay regime) or faster.

    The truncation error when integrating up to $u_{\max}$ is bounded by:

    $$
    \epsilon_{\text{trunc}} \leq \frac{C}{\pi u_{\max}} e^{-\alpha u_{\max}}
    $$

    **For $u_{\max} = 50$:** With conservative $\alpha \approx 0.5$ (appropriate for $\tau \sim 1$ with these parameters):

    $$
    \epsilon_{50} \sim \frac{1}{\pi \cdot 50} e^{-0.5 \times 50} = \frac{1}{157} e^{-25} \approx 6.4 \times 10^{-3} \times 1.4 \times 10^{-11} \approx 9 \times 10^{-14}
    $$

    **For $u_{\max} = 100$:**

    $$
    \epsilon_{100} \sim \frac{1}{\pi \cdot 100} e^{-0.5 \times 100} = \frac{1}{314} e^{-50} \approx 3.2 \times 10^{-3} \times 1.9 \times 10^{-22} \approx 6 \times 10^{-25}
    $$

    The improvement from $u_{\max} = 50$ to $u_{\max} = 100$ reduces the truncation error from $\sim 10^{-14}$ to $\sim 10^{-25}$, a gain of about 11 orders of magnitude. However, $10^{-14}$ is already below double-precision machine epsilon ($\approx 2.2 \times 10^{-16}$), so the truncation error at $u_{\max} = 50$ is already negligible in practice.

    The additional CF evaluations from $u = 50$ to $u = 100$ (doubling the grid or adding nodes in $[50, 100]$) increase computational cost but provide no practical benefit since other error sources (quadrature discretization, floating-point arithmetic) dominate. Therefore, $u_{\max} = 50$ is sufficient and the improvement from $u_{\max} = 100$ is **not** worth the additional cost.

---

**Exercise 7.**
The FFT prices calls for all strikes simultaneously, but a calibration requires both call prices and implied volatilities. After obtaining the FFT price vector, describe the computational pipeline to convert prices to implied volatilities. If $M = 45$ calibration strikes do not lie on the FFT grid, estimate the total number of Newton-Raphson iterations needed (assuming 4 iterations per strike) and compare this cost to the FFT itself.

??? success "Solution to Exercise 7"
    **Computational pipeline from FFT prices to implied volatilities:**

    1. **FFT computation:** Run the Carr-Madan FFT to obtain call prices $C(x_k)$ on the log-strike grid $\{x_k\}_{k=0}^{N-1}$. Cost: $N$ CF evaluations plus $O(N \log N)$ FFT operations.

    2. **Interpolation to market strikes:** The $M = 45$ calibration strikes $\{K_m\}$ generally do not coincide with the FFT grid. Compute $x_m = \log K_m$ and use cubic spline interpolation to obtain $C_m = C(x_m)$. Cost: $O(N)$ for spline setup, $O(M)$ for evaluation.

    3. **Implied volatility inversion:** For each market strike $K_m$, solve the Black-Scholes equation $C^{\text{BS}}(K_m, \sigma_m) = C_m$ for $\sigma_m$ using Newton-Raphson iteration. Each iteration requires evaluating $C^{\text{BS}}$ and its vega $\partial C^{\text{BS}} / \partial \sigma$. The update is:

        $$
        \sigma^{(n+1)} = \sigma^{(n)} - \frac{C^{\text{BS}}(\sigma^{(n)}) - C_m}{\text{vega}(\sigma^{(n)})}
        $$

    **Cost estimate:** With 4 Newton-Raphson iterations per strike and $M = 45$ strikes:

    $$
    \text{Total NR iterations} = 4 \times 45 = 180
    $$

    Each iteration involves one Black-Scholes price evaluation and one vega computation, both $O(1)$ operations (involving a few exponentials and normal CDF evaluations). The total cost of the implied volatility inversion is approximately 180 Black-Scholes evaluations.

    **Comparison with FFT cost:** For $N = 2048$, the FFT requires 2048 Heston CF evaluations. Each Heston CF evaluation involves computing $C(\tau, u)$ and $D(\tau, u)$ with complex exponentials, logarithms, and square roots --- significantly more expensive than a Black-Scholes evaluation. Roughly, one CF evaluation costs 5--10 times a BS evaluation in terms of floating-point operations.

    Therefore the FFT cost is equivalent to roughly $2048 \times 7 \approx 14{,}000$ BS-equivalent operations, while the Newton-Raphson inversion costs only $180$ BS evaluations. The implied volatility inversion adds about $180/14{,}000 \approx 1.3\%$ overhead to the total computation. The FFT dominates the cost of the calibration pipeline.
