# Convergence of Fourier Series

The previous section established that every $L^2$ function on a finite interval has a Fourier series and that the partial sums converge in the $L^2$ norm (Parseval's theorem). But $L^2$ convergence is an averaged statement---it says nothing about whether $S_N f(x_0)$ converges to $f(x_0)$ at a specific point $x_0$. For numerical methods like the COS pricing formula, we need to understand precisely how fast the partial sums approach $f$, and what happens near discontinuities where the convergence breaks down. This section develops the convergence theory of Fourier series: pointwise convergence under Dirichlet conditions, uniform convergence for smooth functions, the rate of coefficient decay as a function of regularity, and the Gibbs phenomenon at jump discontinuities.

!!! info "Prerequisites"
    - [Fourier Series on Finite Intervals](fourier_series_finite_intervals.md) (definition and Parseval's theorem)
    - Real analysis: uniform convergence, bounded variation, piecewise smoothness

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State and apply the Dirichlet convergence theorem for pointwise convergence
    2. Relate the smoothness of $f$ to the decay rate of its Fourier coefficients
    3. Determine when uniform convergence holds
    4. Describe the Gibbs phenomenon and its implications for numerical truncation
    5. Explain why smooth densities lead to exponentially convergent Fourier pricing methods

---

## Pointwise Convergence and Dirichlet Conditions

The most classical result in Fourier analysis gives sufficient conditions for the Fourier series to converge pointwise. The conditions are mild enough to cover virtually all functions arising in financial applications.

!!! note "Theorem: Dirichlet Convergence Theorem"
    Let $f$ be a periodic function with period $L$ that is piecewise smooth on $[a, a+L]$ (meaning $f$ and $f'$ are piecewise continuous with at most finitely many jump discontinuities). Then the Fourier series converges pointwise:

    $$
    S_N f(x) \to \begin{cases} f(x) & \text{if } f \text{ is continuous at } x \\ \frac{1}{2}\left[f(x^+) + f(x^-)\right] & \text{if } f \text{ has a jump at } x \end{cases}
    $$

    where $f(x^+) = \lim_{h \to 0^+} f(x+h)$ and $f(x^-) = \lim_{h \to 0^+} f(x-h)$.

**Proof sketch.** The $N$-th partial sum can be written as a convolution with the Dirichlet kernel:

$$
S_N f(x) = \frac{1}{L}\int_{-L/2}^{L/2} f(x - t)\, D_N(t)\, dt
$$

where

$$
D_N(t) = \sum_{n=-N}^{N} e^{2\pi i n t/L} = \frac{\sin((2N+1)\pi t/L)}{\sin(\pi t/L)}
$$

The Dirichlet kernel satisfies $\frac{1}{L}\int_{-L/2}^{L/2} D_N(t)\,dt = 1$ and concentrates near $t = 0$ as $N \to \infty$, though it does not form an approximate identity due to the slow decay of its oscillations. The proof proceeds by splitting the integral into neighborhoods of $t = 0$ where the piecewise smoothness of $f$ allows the Riemann--Lebesgue lemma to control the oscillatory contributions. The full details require the theory of summability kernels and are found in standard references (e.g., Katznelson, *An Introduction to Harmonic Analysis*). $\square$

At points of continuity, the Fourier series reconstructs $f$ exactly. At jump discontinuities, it converges to the midpoint of the jump---a natural consequence of the symmetry of the Dirichlet kernel.

---

## Coefficient Decay and Smoothness

The rate at which Fourier coefficients decay is directly controlled by the smoothness of the function. This relationship is the key to understanding why smooth densities lead to rapidly convergent Fourier pricing methods.

!!! note "Theorem: Decay Rate of Fourier Coefficients"
    Let $f$ be $L$-periodic.

    1. If $f$ is piecewise continuous with jump discontinuities, then $a_n, b_n = O(1/n)$ as $n \to \infty$.
    2. If $f$ is continuous and piecewise $C^1$, then $a_n, b_n = O(1/n^2)$.
    3. More generally, if $f \in C^k$ (the periodic extension is $k$-times continuously differentiable), then $a_n, b_n = O(1/n^{k+1})$.
    4. If $f$ is real-analytic (i.e., equals its Taylor series in a neighborhood of every point), then $|c_n| = O(e^{-\alpha |n|})$ for some $\alpha > 0$.

**Proof of item 3.** Integrate by parts $k$ times in the formula for $a_n$:

$$
a_n = \frac{2}{L}\int_a^{a+L} f(x)\cos\!\left(\frac{2\pi n x}{L}\right)dx
$$

Each integration by parts introduces a factor of $L/(2\pi n)$ and replaces $f$ by $f'$. The boundary terms vanish because $f$ and all its derivatives up to order $k-1$ are periodic. After $k$ integrations:

$$
a_n = \frac{2}{L}\left(\frac{L}{2\pi n}\right)^k \int_a^{a+L} f^{(k)}(x)\cos\!\left(\frac{2\pi n x}{L} + \frac{k\pi}{2}\right)dx
$$

The remaining integral is bounded by $L \cdot \|f^{(k)}\|_\infty$, giving $|a_n| \leq C/n^k$ where $C = \|f^{(k)}\|_\infty \cdot (L/(2\pi))^k \cdot 2/L$. The same argument applies to $b_n$, yielding $a_n, b_n = O(1/n^{k+1})$ when accounting for the additional factor from the derivative order. $\square$

!!! warning "Discontinuities Kill Convergence Speed"
    A single jump discontinuity in $f$ (or in any derivative of $f$) limits the coefficient decay to the rate corresponding to that level of regularity. For probability densities in finance, this means:

    - **Normal density** (analytic, $C^\infty$): exponential decay of coefficients, requiring only $N \approx 64$ terms
    - **Density with kink** (e.g., from a barrier): $O(1/n^2)$ decay, requiring $N \approx 10^3$ terms
    - **Density with jump** (e.g., discrete mass): $O(1/n)$ decay, very slow convergence

---

## Uniform Convergence

Pointwise convergence at each point does not guarantee that the convergence is uniform across the interval. Uniform convergence is stronger and ensures that the partial sums approximate $f$ equally well everywhere.

!!! note "Theorem: Uniform Convergence"
    If $f$ is continuous on $[a, a+L]$ with $f(a) = f(a+L)$ (the periodic extension is continuous) and $f$ has bounded variation, then $S_N f \to f$ uniformly on $[a, a+L]$.

    More generally, if $f \in C^1$ with periodic boundary conditions, then $S_N f \to f$ uniformly and the rate is:

    $$
    \|f - S_N f\|_\infty = O\!\left(\frac{\ln N}{N}\right)
    $$

The logarithmic factor arises from the unbounded $L^1$ norm of the Dirichlet kernel: $\|D_N\|_1 \sim \frac{4}{\pi^2}\ln N$. This slow growth of the kernel norm is the fundamental obstruction to uniform convergence for merely continuous functions.

!!! tip "Practical Consequence for COS Method"
    When the risk-neutral density is smooth (as in the Black--Scholes or Heston models), the COS method's truncated Fourier series converges uniformly and exponentially fast. The number of terms $N$ needed for a target accuracy $\varepsilon$ grows only as $O(\ln(1/\varepsilon))$, which is why $N = 64$ or $N = 128$ suffices for six-digit accuracy in practice.

---

## The Gibbs Phenomenon

When $f$ has a jump discontinuity, the Fourier partial sums exhibit a characteristic overshoot near the jump that does not vanish as $N \to \infty$. This is the Gibbs phenomenon, first observed by Wilbraham (1848) and later analyzed by Gibbs (1899).

!!! note "Theorem: Gibbs Phenomenon"
    Let $f$ have a jump discontinuity of magnitude $d = f(x_0^+) - f(x_0^-)$ at $x_0$. Then as $N \to \infty$, the partial sum $S_N f$ develops an overshoot near $x_0$ whose limiting magnitude is

    $$
    \frac{d}{\pi}\int_0^{\pi} \frac{\sin t}{t}\, dt - \frac{d}{2} \approx 0.0895 \cdot d
    $$

    That is, the overshoot converges to approximately **8.95%** of the jump size and does not decrease with increasing $N$. The overshoot region narrows as $O(1/N)$, but its peak height remains fixed.

**Proof sketch.** Near the jump at $x_0$, the partial sum behaves as

$$
S_N f(x_0 + \pi/(N+1/2)) \approx \frac{f(x_0^+) + f(x_0^-)}{2} + \frac{d}{\pi}\int_0^{\pi} \frac{\sin t}{t}\,dt - \frac{d}{2} + o(1)
$$

The integral $\int_0^\pi \frac{\sin t}{t}\,dt \approx 1.8519$ is the Si function evaluated at $\pi$. The excess over $d/2$ gives the overshoot. $\square$

!!! example "Gibbs Phenomenon for a Square Wave"
    The square wave $f(x) = \text{sgn}(\sin x)$ on $[0, 2\pi]$ has jumps of magnitude $d = 2$ at $x = 0$ and $x = \pi$. Its Fourier series is

    $$
    f(x) \sim \frac{4}{\pi}\sum_{k=0}^{\infty} \frac{\sin((2k+1)x)}{2k+1}
    $$

    The partial sums exhibit overshoots of approximately $2 \times 0.0895 = 0.179$ near each jump. No matter how many terms are included, the partial sums always overshoot the jump by about 9% of the jump size.

!!! warning "Implications for Density Recovery"
    The Gibbs phenomenon is relevant when recovering densities with sharp features (e.g., densities of barrier option payoffs or digital options with discrete mass). Near such features, the COS method's density reconstruction will exhibit oscillatory artifacts. Remedies include:

    - **Sigma factors** (Lanczos smoothing): multiply $c_n$ by $\text{sinc}(n/N)$ to suppress oscillations
    - **Fejer summation**: use Cesaro means $(S_0 + S_1 + \cdots + S_{N-1})/N$ instead of $S_N$
    - **Exponential filters**: multiply $c_n$ by $\exp(-\alpha(n/N)^p)$ for suitable $\alpha, p$

---

## Rate of Convergence Summary

The following table summarizes the relationship between regularity and convergence, which is the central practical message of this section:

| Regularity of $f$ | Coefficient decay | $\|f - S_N f\|_2$ | $\|f - S_N f\|_\infty$ |
|---|---|---|---|
| Piecewise continuous (jumps) | $O(1/n)$ | $O(1/\sqrt{N})$ | Does not converge uniformly (Gibbs) |
| Continuous, piecewise $C^1$ | $O(1/n^2)$ | $O(1/N^{3/2})$ | $O(\ln N / N)$ |
| $C^k$ (periodic) | $O(1/n^{k+1})$ | $O(1/N^{k+1/2})$ | $O(\ln N / N^k)$ |
| $C^\infty$ (periodic) | Faster than any polynomial | Faster than any polynomial | Faster than any polynomial |
| Real-analytic | $O(e^{-\alpha n})$ | $O(e^{-\alpha N})$ | $O(e^{-\alpha N})$ |

The exponential convergence for analytic functions explains why the COS method achieves machine precision with remarkably few terms for models like Black--Scholes (log-normal density) and Heston (density with exponential tail decay).

---

## L-Squared Convergence

For completeness, we record the $L^2$ convergence result that was already established via Parseval's theorem in the previous section.

!!! note "Theorem: $L^2$ Convergence"
    For any $f \in L^2([a, a+L])$, the Fourier partial sums converge in the $L^2$ norm:

    $$
    \|f - S_N f\|_2^2 = \sum_{|n| > N} |c_n|^2 \to 0 \quad \text{as } N \to \infty
    $$

    No additional assumptions on $f$ are needed beyond square-integrability.

$L^2$ convergence is the weakest of the three modes discussed here, but also the most general. It holds for all square-integrable functions, including those with discontinuities where pointwise convergence may fail or where the Gibbs phenomenon prevents uniform convergence. The rate of $L^2$ convergence is determined by the tail behavior of $\{|c_n|^2\}$, which in turn depends on the smoothness of $f$ as characterized above.

---

## Example: Convergence Rates in Practice

To illustrate the dramatic effect of smoothness on convergence, consider two functions on $[-\pi, \pi]$:

!!! example "Smooth vs Discontinuous Convergence"
    **Function 1:** $f(x) = e^{\cos x}$ (real-analytic, $C^\infty$)

    The Fourier coefficients decay exponentially. With $N = 16$ terms, the approximation error is below $10^{-10}$.

    **Function 2:** $g(x) = |x|$ (continuous but not $C^1$, with a kink at $x = 0$)

    The Fourier series is

    $$
    |x| = \frac{\pi}{2} - \frac{4}{\pi}\sum_{k=0}^{\infty} \frac{\cos((2k+1)x)}{(2k+1)^2}
    $$

    The coefficients decay as $O(1/n^2)$. With $N = 16$ terms, the approximation error is approximately $10^{-2}$---eight orders of magnitude worse.

    This contrast directly impacts option pricing: the log-normal density (analytic) allows $N = 64$ in the COS method, while a density with kinks may require $N = 10^3$ or more.

---

## Summary

Convergence of Fourier series is governed by the smoothness of the function being expanded:

| Convergence mode | Condition | Key feature |
|---|---|---|
| Pointwise | Piecewise smooth $f$ (Dirichlet conditions) | Converges to midpoint at jumps |
| Uniform | Continuous $f$ with bounded variation | No Gibbs overshoot |
| $L^2$ | $f \in L^2$ (no extra conditions) | Always holds; rate depends on smoothness |
| Exponential | Real-analytic $f$ | Machine precision with small $N$ |

| Phenomenon | Description | Remedy |
|---|---|---|
| Gibbs phenomenon | 9% overshoot at jump discontinuities | Fejer summation, sigma factors, filters |

**The smoothness-to-convergence correspondence is the fundamental reason why Fourier pricing methods achieve extraordinary efficiency for models with smooth densities: analytic characteristic functions produce exponentially decaying Fourier coefficients, requiring only tens of terms for machine-precision option prices.**
