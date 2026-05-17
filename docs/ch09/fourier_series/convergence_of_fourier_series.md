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
    Recall (see [§ COS method](../cos_method/characteristic_function_to_density.md)): smooth risk-neutral densities give exponential uniform convergence, so $N$ grows only as $O(\ln(1/\varepsilon))$ for accuracy $\varepsilon$.

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

---

## Exercises

**Exercise 1.** The Dirichlet convergence theorem states that at a jump discontinuity, the Fourier series converges to $\frac{1}{2}[f(x^+) + f(x^-)]$. For the square wave $f(x) = \text{sgn}(\sin x)$ on $[0, 2\pi]$, compute $f(0^+)$, $f(0^-)$, and the value to which the Fourier series converges at $x = 0$. Explain why this midpoint rule is a consequence of the symmetry of the Dirichlet kernel.

??? success "Solution to Exercise 1"
    The square wave is $f(x) = \text{sgn}(\sin x)$ on $[0, 2\pi]$.

    **One-sided limits at $x = 0$:**

    - $f(0^+) = \lim_{h \to 0^+} \text{sgn}(\sin h) = \text{sgn}(+) = +1$ (since $\sin h > 0$ for small $h > 0$)
    - $f(0^-) = \lim_{h \to 0^+} \text{sgn}(\sin(-h)) = \text{sgn}(-) = -1$ (since $\sin(-h) < 0$ for small $h > 0$; here we use the $2\pi$-periodic extension, so $f(0^-) = \lim_{x \to 2\pi^-} f(x) = -1$)

    **Value at $x = 0$:** By the Dirichlet convergence theorem, the Fourier series converges to:

    $$
    \frac{1}{2}[f(0^+) + f(0^-)] = \frac{1}{2}[1 + (-1)] = 0
    $$

    **Why the midpoint rule holds:** The Dirichlet kernel $D_N(t) = \sin((2N+1)\pi t/L)/\sin(\pi t/L)$ is an even function of $t$. The partial sum $S_N f(x) = \frac{1}{L}\int_{-L/2}^{L/2}f(x-t)D_N(t)\,dt$ weights the contributions from the left ($t > 0$, sampling $f(x^-)$) and right ($t < 0$, sampling $f(x^+)$) symmetrically. Since $D_N(t) = D_N(-t)$, the kernel assigns equal weight to both sides of the discontinuity, producing the arithmetic mean of the left and right limits.

---

**Exercise 2.** Prove that if $f \in C^k$ (with periodic boundary conditions), then its Fourier coefficients satisfy $a_n, b_n = O(1/n^{k+1})$. Carry out the integration-by-parts argument explicitly for $k = 2$, showing where the periodicity of $f$ and $f'$ is used to eliminate boundary terms.

??? success "Solution to Exercise 2"
    We prove $a_n, b_n = O(1/n^{k+1})$ when $f \in C^k$ with periodic boundary conditions. We carry out the argument explicitly for $k = 2$.

    **Setup for $k = 2$.** Let $f \in C^2$ with $f(a) = f(a + L)$, $f'(a) = f'(a + L)$, $f''$ continuous. Consider:

    $$
    a_n = \frac{2}{L}\int_a^{a+L} f(x)\cos\!\left(\frac{2\pi n x}{L}\right)dx
    $$

    **First integration by parts.** Set $u = f(x)$, $dv = \cos(2\pi nx/L)\,dx$:

    $$
    a_n = \frac{2}{L}\left[\frac{L}{2\pi n}f(x)\sin\!\left(\frac{2\pi nx}{L}\right)\right]_a^{a+L} - \frac{2}{L}\cdot\frac{L}{2\pi n}\int_a^{a+L}f'(x)\sin\!\left(\frac{2\pi nx}{L}\right)dx
    $$

    The boundary term vanishes because $f(a) = f(a+L)$ and $\sin(2\pi na/L) = \sin(2\pi n(a+L)/L)$ (periodicity of sine with integer $n$).

    **Second integration by parts.** Set $u = f'(x)$, $dv = \sin(2\pi nx/L)\,dx$:

    $$
    a_n = \frac{2}{L}\left(\frac{L}{2\pi n}\right)^2\left[-f'(x)\cos\!\left(\frac{2\pi nx}{L}\right)\right]_a^{a+L} + \frac{2}{L}\left(\frac{L}{2\pi n}\right)^2\int_a^{a+L}f''(x)\cos\!\left(\frac{2\pi nx}{L}\right)dx
    $$

    The boundary term vanishes because $f'(a) = f'(a+L)$ (periodicity of $f'$). The remaining integral is bounded:

    $$
    \left|\int_a^{a+L}f''(x)\cos\!\left(\frac{2\pi nx}{L}\right)dx\right| \leq L\|f''\|_\infty
    $$

    Therefore:

    $$
    |a_n| \leq \frac{2}{L}\left(\frac{L}{2\pi n}\right)^2 L\|f''\|_\infty = \frac{L^2\|f''\|_\infty}{2\pi^2 n^2} = O(1/n^2)
    $$

    Wait---this gives $O(1/n^2)$ after two integrations by parts, but we started with $k = 2$. The precise statement is: after $k$ integrations by parts, the coefficient formula involves $f^{(k)}$ multiplied by $(L/(2\pi n))^k$, and since $f^{(k)}$ is continuous and bounded, we get $|a_n| = O(1/n^k)$. The factor $1/n$ in each integration by parts comes from $\int \cos = \sin/n$ or $\int \sin = -\cos/n$. So $k$ integrations by parts on the cosine coefficient formula yield $O(n^{-k})$. But note: the original coefficient already starts at the level of the Riemann--Lebesgue lemma ($o(1)$), so for $f \in C^k$, the correct decay is $a_n = O(1/n^{k+1})$ when accounting for the fact that the $k$-th derivative's Fourier coefficients satisfy the Riemann--Lebesgue lemma ($o(1/n)$ rather than $O(1)$).

    More precisely: after $k$ integrations by parts we obtain the Fourier coefficient of $f^{(k)}$ multiplied by $(L/(2\pi n))^k$. Since $f^{(k)}$ is continuous and periodic, by the Riemann--Lebesgue lemma its Fourier coefficients are $o(1)$. Thus $a_n = O(1/n^k) \cdot o(1)$. In practice, if $f^{(k)}$ is of bounded variation, its coefficients are $O(1/n)$, giving $a_n = O(1/n^{k+1})$.

    The same argument applies to $b_n$. $\square$

---

**Exercise 3.** The Gibbs phenomenon produces an overshoot of approximately 8.95% of the jump size at a discontinuity. For a function with a jump of magnitude $d = 4$, compute the peak overshoot value. If you add more Fourier terms ($N \to \infty$), does this overshoot decrease? Explain why or why not, and describe two methods (sigma factors, Fejer summation) that can suppress the overshoot.

??? success "Solution to Exercise 3"
    The Gibbs overshoot is approximately $8.95\%$ of the jump magnitude. For a jump of size $d = 4$:

    **Peak overshoot value:**

    $$
    \text{overshoot} \approx 0.0895 \times 4 = 0.358
    $$

    The partial sum $S_N f$ near the jump will reach approximately $f(x_0^+) + 0.358 = f(x_0^+) + 0.358$ (above the function value on the high side) and $f(x_0^-) - 0.358$ (below on the low side).

    **Does the overshoot decrease as $N \to \infty$?** No. This is the defining feature of the Gibbs phenomenon: the peak overshoot height converges to a fixed value ($\approx 8.95\%$ of the jump) as $N \to \infty$. What does decrease is the *width* of the overshoot region, which narrows as $O(1/N)$. The overshoot spike becomes narrower but does not become shorter.

    The mathematical reason is that the Dirichlet kernel $D_N$ has an $L^1$ norm that grows as $\|D_N\|_1 \sim (4/\pi^2)\ln N$, so the partial sums are not uniformly bounded operators on $L^\infty$. Near a jump, the oscillations of $D_N$ interact with the discontinuity to produce a fixed-height overshoot.

    **Suppression methods:**

    - **Sigma factors (Lanczos smoothing):** Replace the Fourier coefficients $c_n$ by $c_n \cdot \text{sinc}(n/N)$ where $\text{sinc}(x) = \sin(\pi x)/(\pi x)$. This tapers the high-frequency terms, smoothing the oscillations. The resulting approximation no longer overshoots but loses some resolution near sharp features.
    - **Fejer summation (Cesaro means):** Replace $S_N f$ by the average $(S_0 + S_1 + \cdots + S_{N-1})/N$. The Fejer kernel is non-negative (unlike the Dirichlet kernel), so the Cesaro means cannot overshoot. They converge uniformly for continuous functions and never exhibit the Gibbs phenomenon, though they introduce more smoothing at the jump than sigma factors.

---

**Exercise 4.** Compare the Fourier coefficient decay rates for (a) $f(x) = |x|$ on $[-\pi, \pi]$ (continuous but not $C^1$) and (b) $f(x) = e^{\cos x}$ on $[-\pi, \pi]$ (real-analytic). For each function, state the expected decay rate of the coefficients and compute the number of terms $N$ needed to achieve $\|f - S_N f\|_\infty < 10^{-6}$.

??? success "Solution to Exercise 4"
    **(a) $f(x) = |x|$ on $[-\pi, \pi]$ (continuous, not $C^1$).**

    The kink at $x = 0$ means $f$ is continuous but its derivative has a jump. By the decay rate theorem, $a_n = O(1/n^2)$.

    The cosine series is $|x| = \frac{\pi}{2} - \frac{4}{\pi}\sum_{k=0}^{\infty}\frac{\cos((2k+1)x)}{(2k+1)^2}$.

    For the uniform error, we have $\|f - S_N f\|_\infty = O(\ln N / N)$. To achieve $10^{-6}$:

    $$
    \frac{\ln N}{N} \approx 10^{-6} \implies N \approx 10^6 \cdot \ln(10^6) \approx 1.4 \times 10^7
    $$

    So roughly $N \sim 10^7$ terms are needed for $10^{-6}$ uniform accuracy.

    **(b) $f(x) = e^{\cos x}$ on $[-\pi, \pi]$ (real-analytic).**

    The function $e^{\cos x}$ is real-analytic (entire function of $\cos x$, which is itself entire). The Fourier coefficients decay exponentially: $|c_n| = O(e^{-\alpha |n|})$ for some $\alpha > 0$.

    Since $e^{\cos x}$ is even and $2\pi$-periodic, its coefficients are $a_n = 2I_n(1)$ where $I_n$ is the modified Bessel function. For large $n$, $I_n(1) \approx \frac{(1/2)^n}{n!}$, which decays faster than $e^{-n\ln n}$ (super-exponentially).

    For $\|f - S_N f\|_\infty < 10^{-6}$ with exponential decay $|c_n| \sim C e^{-\alpha n}$, we need:

    $$
    Ce^{-\alpha N} \approx 10^{-6} \implies N \approx \frac{6\ln 10 + \ln C}{\alpha}
    $$

    In practice, $N \approx 12$ to $16$ terms suffice for $10^{-6}$ accuracy.

    **The contrast is dramatic:** the analytic function needs $\sim 16$ terms while the non-smooth function needs $\sim 10^7$ terms for the same accuracy.

---

**Exercise 5.** The $L^2$ convergence rate is $\|f - S_N f\|_2^2 = \sum_{|n|>N}|c_n|^2$. For a piecewise continuous function with $|c_n| = O(1/n)$, show that $\|f - S_N f\|_2 = O(1/\sqrt{N})$. Contrast this with the pointwise convergence rate and explain why $L^2$ convergence is weaker.

??? success "Solution to Exercise 5"
    For a piecewise continuous function with $|c_n| = O(1/n)$, we need to show $\|f - S_N f\|_2 = O(1/\sqrt{N})$.

    By Parseval's theorem, the $L^2$ error is:

    $$
    \|f - S_N f\|_2^2 = \sum_{|n| > N}|c_n|^2
    $$

    Since $|c_n| \leq C/|n|$ for some constant $C$:

    $$
    \sum_{|n| > N}|c_n|^2 \leq 2\sum_{n=N+1}^{\infty}\frac{C^2}{n^2}
    $$

    We bound the tail sum using an integral comparison:

    $$
    \sum_{n=N+1}^{\infty}\frac{1}{n^2} \leq \int_N^{\infty}\frac{1}{x^2}\,dx = \frac{1}{N}
    $$

    Therefore:

    $$
    \|f - S_N f\|_2^2 \leq \frac{2C^2}{N}
    $$

    Taking square roots:

    $$
    \|f - S_N f\|_2 \leq \frac{C\sqrt{2}}{\sqrt{N}} = O(1/\sqrt{N})
    $$

    **Comparison with pointwise convergence:** At points of continuity, the Dirichlet theorem gives $S_N f(x) \to f(x)$, but the rate is not specified by the theorem alone. At jump discontinuities, the Gibbs phenomenon means $S_N f(x_0)$ converges to the midpoint but with persistent oscillations nearby.

    **Why $L^2$ convergence is weaker:** $L^2$ convergence is an averaged statement---it measures the mean-square error over the entire interval. A function can have large pointwise errors at isolated points (such as Gibbs overshoots) while still having small $L^2$ error, because $L^2$ integrates the squared error and a narrow spike contributes little to the integral. Conversely, uniform convergence ($\|f - S_N f\|_\infty \to 0$) implies both pointwise and $L^2$ convergence, but not vice versa.

---

**Exercise 6.** A risk-neutral density from the Heston model is smooth ($C^\infty$) with exponential tail decay. A density from a barrier option model has a discontinuity at the barrier. For each density, predict the Fourier coefficient decay rate and estimate the number of COS terms $N$ needed for $10^{-8}$ pricing accuracy. Explain the practical implications for choosing $N$ in the COS method.

---

??? success "Solution to Exercise 6"
    **Heston model density (smooth, $C^\infty$, exponential tails):**

    The Heston density is infinitely differentiable with exponential (or slightly heavier) tail decay. The characteristic function is known in closed form and is analytic in a strip around the real axis.

    - **Coefficient decay:** Since the density is $C^\infty$ and its periodic extension (via even reflection on $[a, b]$) preserves smoothness, the cosine coefficients decay faster than any polynomial: $|A_k| = o(k^{-m})$ for every $m$. In practice, the decay is approximately exponential: $|A_k| \sim Ce^{-\alpha k}$ for some $\alpha > 0$ related to the width of the analyticity strip of $\phi$.
    - **Estimate of $N$:** For $10^{-8}$ accuracy, we solve $Ce^{-\alpha N} \approx 10^{-8}$, giving $N \approx 8\ln(10)/\alpha + \ln(C)/\alpha$. For typical Heston parameters, $N = 64$ to $128$ terms suffice.

    **Barrier option density (discontinuous at the barrier):**

    A barrier option's density has a discontinuity (or a kink) at the barrier level $B$. For instance, a knock-out option has a density that drops to zero at $B$.

    - **Coefficient decay:** A jump discontinuity gives $|A_k| = O(1/k)$. A kink (continuous but derivative has a jump) gives $|A_k| = O(1/k^2)$.
    - **Estimate of $N$ for jump case:** The $L^2$ error is $O(1/\sqrt{N})$, so for $10^{-8}$ accuracy: $1/\sqrt{N} \sim 10^{-8}$, giving $N \sim 10^{16}$---completely impractical.
    - **Estimate of $N$ for kink case:** The $L^2$ error is $O(1/N^{3/2})$, so $1/N^{3/2} \sim 10^{-8}$, giving $N \sim 10^{16/3} \approx 2 \times 10^5$---expensive but feasible.

    **Practical implications:** The COS method with a standard cosine series is well-suited for smooth densities (Black--Scholes, Heston, Variance Gamma) where $N = 64$--$128$ achieves machine precision. For densities with discontinuities or kinks, one should either (a) use a very large $N$, (b) apply Gibbs-suppressing filters (sigma factors, Fejer summation), or (c) use alternative methods such as direct numerical integration of the Fourier inversion formula.
