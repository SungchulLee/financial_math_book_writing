# Cosine Expansion on [0, pi]

The full Fourier series uses both sine and cosine terms, but for probability densities on a bounded interval, a pure cosine expansion offers significant advantages. The sine coefficients vanish for even functions, and the cosine series avoids the boundary discontinuities that arise when a function on $[a, b]$ is periodically extended. Since probability densities are non-negative and typically smooth in the interior of their support, the cosine expansion converges faster and more uniformly than the full Fourier series. This property is the mathematical reason behind the COS method's choice of cosine basis functions rather than the full trigonometric system.

!!! info "Prerequisites"

    - [Fourier Series on Finite Intervals](fourier_series_finite_intervals.md) (definition and coefficients)
    - [Convergence of Fourier Series](convergence_of_fourier_series.md) (smoothness and decay rates)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Construct the even extension of a function and derive the cosine-only expansion
    2. Compute Fourier cosine coefficients on a general interval $[a, b]$
    3. Explain why cosine expansions have better boundary behavior than full Fourier series
    4. Relate the smoothness of the even extension to the convergence rate
    5. Recognize the cosine expansion as the foundation of the COS pricing method

---

## Even Extensions and the Cosine Series

Given a function $f$ defined on $[0, \pi]$, the **even extension** to $[-\pi, \pi]$ is

$$
f_{\text{even}}(x) = \begin{cases} f(x) & \text{if } x \in [0, \pi] \\ f(-x) & \text{if } x \in [-\pi, 0] \end{cases}
$$

Since $f_{\text{even}}$ is an even function, all its sine coefficients vanish:

$$
b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} f_{\text{even}}(x)\sin(nx)\,dx = 0
$$

because the integrand is odd. Only the cosine coefficients survive, and the Fourier series of the even extension becomes a pure **cosine series** for $f$ on $[0, \pi]$:

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos(nx), \quad x \in [0, \pi]
$$

with coefficients

$$
a_n = \frac{2}{\pi}\int_0^{\pi} f(x)\cos(nx)\,dx, \quad n = 0, 1, 2, \dots
$$

!!! tip "Why Even Extension Is Natural for Densities"
    When $f$ is a probability density on $[0, \pi]$ with $f(0) = f(\pi) = 0$ (or at least small values at the boundaries), the even extension is smooth at $x = 0$. The odd extension, by contrast, would force $f_{\text{odd}}(0) = 0$ regardless of $f(0)$, potentially creating a discontinuity. The even extension preserves the function values at the boundary, leading to a smoother periodic function and faster convergence.

---

## Cosine Expansion on a General Interval [a, b]

The COS method works on a general interval $[a, b]$, not just $[0, \pi]$. The change of variables $x \mapsto \pi(x - a)/(b - a)$ maps $[a, b]$ to $[0, \pi]$, yielding the cosine expansion on $[a, b]$.

!!! note "Definition: Fourier Cosine Series on $[a, b]$"
    Let $f \in L^1([a, b])$. The **Fourier cosine series** of $f$ on $[a, b]$ is

    $$
    f(x) \sim \sum_{k=0}^{\infty}{}' A_k \cos\!\left(\frac{k\pi(x-a)}{b-a}\right)
    $$

    where the prime on the summation denotes that the $k = 0$ term is halved, and the **cosine coefficients** are

    $$
    A_k = \frac{2}{b-a}\int_a^b f(x)\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx, \quad k = 0, 1, 2, \dots
    $$

The prime notation $\sum'$ is a standard convention meaning $A_0/2 + \sum_{k=1}^{\infty} A_k \cos(\cdots)$. This is equivalent to the $a_0/2$ convention in the full Fourier series and ensures that the zeroth coefficient formula is uniform.

**Verification of the zeroth coefficient.** Setting $k = 0$:

$$
A_0 = \frac{2}{b-a}\int_a^b f(x)\,dx
$$

For a probability density, $\int_a^b f(x)\,dx = 1$ (assuming the density is supported on $[a, b]$), so $A_0 = 2/(b-a)$ and the halved zeroth term is $A_0/2 = 1/(b-a)$, which is the uniform density on $[a, b]$.

---

## Boundary Behavior and Convergence Advantage

The crucial advantage of the cosine expansion over the full Fourier series lies in boundary behavior. Consider $f$ on $[a, b]$ and its periodic extensions:

**Full Fourier series.** The function is periodically extended with period $b - a$. If $f(a) \neq f(b)$, this creates a jump discontinuity at the boundary, introducing Gibbs oscillations and limiting coefficient decay to $O(1/k)$.

**Cosine series.** The function is first reflected (even extension) about $x = a$ and $x = b$, then periodically extended with period $2(b-a)$. The resulting function is automatically continuous at $x = a$ and $x = b$ (the reflection ensures matching values), so even if $f(a) \neq f(b)$, the even extension is continuous.

!!! note "Theorem: Convergence Improvement from Cosine Expansion"
    Let $f \in C^k([a, b])$ (not necessarily periodic). Then:

    - The full Fourier series has coefficients decaying as $O(1/n)$ in general (due to boundary jumps in the periodic extension).
    - The cosine series has coefficients decaying as $O(1/n^2)$ if $f$ is merely continuous, and as $O(1/n^{k+1})$ if $f \in C^k([a, b])$ and the even extension is also $C^k$.

    In particular, if $f'(a) = f'(b) = 0$ (Neumann boundary conditions), the even extension is $C^1$ and the cosine coefficients decay as $O(1/k^2)$ even if $f$ itself is only $C^1$.

**Proof.** The even extension $f_e$ satisfies $f_e(x) = f_e(-x)$ when centered at $a$, so $f_e$ is continuous at the reflection point. If $f'(a) = 0$, then the left and right derivatives of $f_e$ at $x = a$ also match, giving $C^1$ regularity. Each additional matching derivative at the boundary adds one order to the coefficient decay rate, following the integration-by-parts argument from the convergence theory. $\square$

!!! warning "When the Advantage Disappears"
    If $f$ has a discontinuity in the interior of $[a, b]$, the cosine expansion offers no improvement over the full Fourier series---both exhibit $O(1/k)$ decay and Gibbs oscillations at the discontinuity. The advantage is purely at the boundaries.

---

## Orthogonality of the Cosine System

The cosine functions on $[a, b]$ form an orthogonal system:

$$
\int_a^b \cos\!\left(\frac{k\pi(x-a)}{b-a}\right)\cos\!\left(\frac{j\pi(x-a)}{b-a}\right)dx = \begin{cases} b - a & \text{if } k = j = 0 \\ \frac{b-a}{2} & \text{if } k = j \neq 0 \\ 0 & \text{if } k \neq j \end{cases}
$$

This orthogonality gives the cosine coefficients the same projection interpretation as in the full Fourier case: $A_k$ is the coordinate of $f$ along the $k$-th cosine basis function, normalized by the squared norm of that basis function.

The **best $L^2$ approximation** property carries over: the truncated cosine series

$$
S_N^c f(x) = \sum_{k=0}^{N-1}{}' A_k \cos\!\left(\frac{k\pi(x-a)}{b-a}\right)
$$

minimizes $\|f - T\|_2$ over all linear combinations of the first $N$ cosine basis functions. Parseval's theorem for the cosine system reads:

$$
\frac{2}{b-a}\int_a^b |f(x)|^2\,dx = \frac{A_0^2}{2} + \sum_{k=1}^{\infty} A_k^2
$$

---

## Example: Cosine Expansion of a Gaussian Density

To illustrate the rapid convergence of cosine expansions for smooth densities, consider a standard normal density truncated to $[a, b] = [-10, 10]$.

!!! example "Cosine Coefficients of the Normal Density"
    Recall (see [§ Fundamental solution of the heat equation](../../ch05/heat_equation/fundamental_solution.md)) that the standard normal density is real-analytic with Gaussian characteristic function, so its cosine coefficients on $[-10, 10]$,

    $$
    A_k = \frac{1}{10}\int_{-10}^{10} \frac{1}{\sqrt{2\pi}}e^{-x^2/2}\cos\!\left(\frac{k\pi(x+10)}{20}\right)dx,
    $$

    decay (super-)exponentially in $k$:

    | $k$ | $A_k$ (approximate) |
    |---|---|
    | 0 | $\approx 0.1000$ |
    | 1 | $\approx 0.0999$ |
    | 2 | $\approx 0.0996$ |
    | 5 | $\approx 0.0970$ |
    | 10 | $\approx 0.0881$ |
    | 20 | $\approx 0.0615$ |
    | 50 | $\approx 0.0030$ |
    | 100 | $\approx 10^{-8}$ |

    With $N = 64$ terms, the cosine series reproduces the density to better than $10^{-6}$ accuracy uniformly on $[-10, 10]$. This is the convergence behavior exploited by the COS pricing method.

---

## Example: Cosine Expansion of a Non-Smooth Function

For contrast, consider a function with a kink.

!!! example "Cosine Expansion of $f(x) = |x|$ on $[-1, 1]$"
    The function $f(x) = |x|$ on $[-1, 1]$ is continuous but not differentiable at $x = 0$. Its cosine expansion on $[-1, 1]$ (with $a = -1$, $b = 1$) is

    $$
    |x| = \frac{1}{2} + \sum_{k=1}^{\infty} A_k\cos(k\pi(x+1)/2)
    $$

    The even extension about the boundary is smooth at $x = \pm 1$ (since $|x|$ approaches 1 from both sides), but the kink at $x = 0$ persists. The coefficients decay as $O(1/k^2)$, and with $N = 64$ terms the maximum error is approximately $10^{-3}$---far worse than the Gaussian case.

    This example illustrates that the cosine expansion's boundary advantage does not overcome interior singularities.

---

## Role in the COS Method

Recall (see [§ COS method](../cos_method/characteristic_function_to_density.md)) for the algorithmic details. The cosine basis is chosen because (i) the even extension absorbs boundary mismatches that would otherwise cause $O(1/n)$ Gibbs decay; (ii) smooth densities give exponentially decaying coefficients; (iii) the coefficients $A_k$ admit a closed-form CF expression (see [§ Cosine coefficients via CF](../cos_method/cosine_coefficients_via_cf.md)); and (iv) the series is real-valued.

---

## Summary

The Fourier cosine expansion on $[a, b]$ provides a more efficient representation than the full Fourier series for functions that are not naturally periodic:

| Feature | Full Fourier series | Cosine expansion |
|---|---|---|
| Basis functions | $\cos, \sin$ | $\cos$ only |
| Periodic extension | Period $b - a$; jumps at boundary if $f(a) \neq f(b)$ | Period $2(b-a)$; even extension avoids boundary jumps |
| Coefficient decay (non-periodic $f \in C^k$) | $O(1/n)$ in general | $O(1/n^{k+1})$ |
| Gibbs at boundary | Present if $f(a) \neq f(b)$ | Absent (even extension is continuous) |
| Suitable for densities | Suboptimal | Natural choice |

**The cosine expansion's superior boundary behavior and faster convergence for non-periodic smooth functions make it the natural choice for representing probability densities on truncated intervals, which is why it forms the basis of the COS pricing method.**

---

## Exercises

**Exercise 1.** Construct the even extension of $f(x) = x$ on $[0, \pi]$ and write out the resulting cosine series. Compute the coefficients $a_n = \frac{2}{\pi}\int_0^{\pi}x\cos(nx)\,dx$ for $n = 0, 1, 2, 3$ and verify that all sine coefficients vanish.

??? success "Solution to Exercise 1"
    The even extension of $f(x) = x$ on $[0, \pi]$ to $[-\pi, \pi]$ is:

    $$
    f_{\text{even}}(x) = |x|, \quad x \in [-\pi, \pi]
    $$

    **Cosine coefficients.** Using $a_n = \frac{2}{\pi}\int_0^{\pi}x\cos(nx)\,dx$:

    **$n = 0$:**

    $$
    a_0 = \frac{2}{\pi}\int_0^{\pi}x\,dx = \frac{2}{\pi}\cdot\frac{\pi^2}{2} = \pi
    $$

    **$n = 1$:** Integration by parts with $u = x$, $dv = \cos(x)\,dx$:

    $$
    a_1 = \frac{2}{\pi}\left[\frac{x\sin(x)}{1}\bigg|_0^{\pi} - \int_0^{\pi}\sin(x)\,dx\right] = \frac{2}{\pi}\left[0 + \cos(x)\big|_0^{\pi}\right] = \frac{2}{\pi}(-1 - 1) = -\frac{4}{\pi}
    $$

    **$n = 2$:** Integration by parts:

    $$
    a_2 = \frac{2}{\pi}\left[\frac{x\sin(2x)}{2}\bigg|_0^{\pi} - \frac{1}{2}\int_0^{\pi}\sin(2x)\,dx\right] = \frac{2}{\pi}\left[0 + \frac{\cos(2x)}{4}\bigg|_0^{\pi}\right] = \frac{2}{\pi}\cdot\frac{1-1}{4} = 0
    $$

    **$n = 3$:**

    $$
    a_3 = \frac{2}{\pi}\left[\frac{x\sin(3x)}{3}\bigg|_0^{\pi} - \frac{1}{3}\int_0^{\pi}\sin(3x)\,dx\right] = \frac{2}{\pi}\left[0 + \frac{\cos(3x)}{9}\bigg|_0^{\pi}\right] = \frac{2}{\pi}\cdot\frac{-1-1}{9} = -\frac{4}{9\pi}
    $$

    In general, for $n \geq 1$: $a_n = \frac{2}{\pi}\cdot\frac{\cos(n\pi) - 1}{n^2} = \frac{2(\,(-1)^n - 1\,)}{\pi n^2}$.

    So $a_n = 0$ for even $n \geq 2$, and $a_n = -4/(\pi n^2)$ for odd $n$.

    **Sine coefficients vanish:** All sine coefficients of the even extension are zero because $f_{\text{even}}(x)\sin(nx)$ is an odd function on $[-\pi, \pi]$:

    $$
    b_n = \frac{1}{\pi}\int_{-\pi}^{\pi}|x|\sin(nx)\,dx = 0
    $$

    The cosine series is therefore:

    $$
    x = \frac{\pi}{2} - \frac{4}{\pi}\sum_{k=0}^{\infty}\frac{\cos((2k+1)x)}{(2k+1)^2}, \quad x \in [0, \pi]
    $$

---

**Exercise 2.** Explain why the cosine expansion of a non-periodic function $f$ on $[a, b]$ converges faster than the full Fourier series. Specifically, if $f(a) \neq f(b)$, show that the periodic extension of $f$ has a jump discontinuity at the boundary (producing $O(1/n)$ coefficient decay), while the even extension used by the cosine series is continuous at the boundary (producing at least $O(1/n^2)$ decay).

??? success "Solution to Exercise 2"
    **Full Fourier series with $f(a) \neq f(b)$:** The periodic extension with period $L = b - a$ creates a function $\tilde{f}$ where $\tilde{f}(b^-) = f(b)$ but $\tilde{f}(b^+) = f(a)$. If $f(a) \neq f(b)$, there is a jump discontinuity of magnitude $|f(b) - f(a)|$ at every integer translate of $b$ (equivalently, of $a$). By the coefficient decay theorem, jump discontinuities limit the Fourier coefficients to $O(1/n)$ decay.

    **Cosine expansion:** The even extension reflects $f$ about the endpoints. Centering at $a$, the even extension on $[a - (b-a), b]$ is defined by $f_e(x) = f(2a - x)$ for $x \in [a - (b-a), a]$. At the reflection point $x = a$:

    $$
    \lim_{x \to a^+} f_e(x) = f(a), \quad \lim_{x \to a^-} f_e(x) = f(a)
    $$

    Both limits equal $f(a)$, so $f_e$ is continuous at $x = a$. Similarly, the reflection about $x = b$ yields continuity at $x = b$. When this even extension is periodically extended with period $2(b - a)$, the period-doubled function is continuous everywhere (even if $f(a) \neq f(b)$).

    Since the even extension is continuous, its Fourier coefficients (which are exactly the cosine coefficients of $f$) decay at least as $O(1/n^2)$ by the decay rate theorem. If $f$ is additionally $C^k$ on $[a, b]$ and the even extension inherits this smoothness, the decay improves to $O(1/n^{k+1})$.

    This is the convergence advantage: the cosine expansion avoids the artificial boundary discontinuity entirely, gaining at least one order of coefficient decay.

---

**Exercise 3.** Verify the orthogonality of the cosine system on $[a, b]$: show that $\int_a^b \cos(k\pi(x-a)/(b-a))\cos(j\pi(x-a)/(b-a))\,dx = 0$ when $k \neq j$. Use the substitution $y = (x - a)/(b - a)$ to reduce to a standard integral on $[0, 1]$.

??? success "Solution to Exercise 3"
    We verify $\int_a^b \cos(k\pi(x-a)/(b-a))\cos(j\pi(x-a)/(b-a))\,dx = 0$ for $k \neq j$.

    **Substitution.** Let $y = (x - a)/(b - a)$, so $x = a + (b-a)y$, $dx = (b-a)\,dy$, and as $x$ ranges over $[a, b]$, $y$ ranges over $[0, 1]$:

    $$
    \int_a^b \cos\!\left(\frac{k\pi(x-a)}{b-a}\right)\cos\!\left(\frac{j\pi(x-a)}{b-a}\right)dx = (b-a)\int_0^1 \cos(k\pi y)\cos(j\pi y)\,dy
    $$

    **Product-to-sum formula:** $\cos(k\pi y)\cos(j\pi y) = \frac{1}{2}[\cos((k-j)\pi y) + \cos((k+j)\pi y)]$.

    For $k \neq j$, both $k - j \neq 0$ and $k + j \neq 0$ (since $k, j \geq 0$). Each term integrates to:

    $$
    \int_0^1 \cos(m\pi y)\,dy = \frac{\sin(m\pi y)}{m\pi}\bigg|_0^1 = \frac{\sin(m\pi)}{m\pi} = 0
    $$

    for any nonzero integer $m$, since $\sin(m\pi) = 0$.

    Therefore the full integral equals $(b-a) \cdot \frac{1}{2}(0 + 0) = 0$. $\square$

---

**Exercise 4.** For the standard normal density $f(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ truncated to $[-10, 10]$, the cosine coefficients $A_k$ decay exponentially. Using the table of approximate values in the text ($A_0 \approx 0.1000$, $A_{50} \approx 0.0030$, $A_{100} \approx 10^{-8}$), estimate the exponential decay rate by fitting $|A_k| \approx Ce^{-\alpha k^2}$ and determine $C$ and $\alpha$.

??? success "Solution to Exercise 4"
    We fit the model $|A_k| \approx Ce^{-\alpha k^2}$ using the data points:

    - $A_0 \approx 0.1000$
    - $A_{50} \approx 0.0030$
    - $A_{100} \approx 10^{-8}$

    Taking logarithms: $\ln|A_k| \approx \ln C - \alpha k^2$.

    **From $k = 0$:** $\ln(0.1) = \ln C$, so $C \approx 0.1$.

    **From $k = 50$:** $\ln(0.003) \approx \ln(0.1) - \alpha(50)^2$

    $$
    -5.81 \approx -2.30 - 2500\alpha \implies \alpha \approx \frac{3.51}{2500} \approx 0.00140
    $$

    **Verification with $k = 100$:** $\ln C - \alpha(100)^2 = \ln(0.1) - 0.00140 \times 10000 = -2.30 - 14.0 = -16.3$.

    This predicts $|A_{100}| \approx e^{-16.3} \approx 8.3 \times 10^{-8}$.

    The actual value is $\approx 10^{-8}$, suggesting the Gaussian decay model $e^{-\alpha k^2}$ is approximately correct but the decay may accelerate slightly for larger $k$.

    **Refined fit using $k = 0$ and $k = 100$:**

    $$
    \alpha = \frac{\ln(0.1) - \ln(10^{-8})}{100^2} = \frac{-2.30 - (-18.42)}{10000} = \frac{16.12}{10000} \approx 0.00161
    $$

    So $C \approx 0.1$ and $\alpha \approx 0.0016$. This Gaussian-in-$k$ decay is consistent with the analytic formula $A_k \propto e^{-k^2\pi^2/(2L^2)}$ where $L = 20$, giving $\alpha = \pi^2/800 \approx 0.01234$. The discrepancy arises because the cosine coefficients involve phase factors $\text{Re}[e^{ik\pi/2}]$ that cause alternating vanishing of odd-indexed coefficients; the table values represent the envelope of the nonzero coefficients, not the raw exponential.

---

**Exercise 5.** The function $f(x) = |x|$ on $[-1, 1]$ has a kink at $x = 0$. Compute the first four cosine coefficients on $[-1, 1]$ using $A_k = \int_{-1}^{1}|x|\cos(k\pi(x+1)/2)\,dx$. Verify that $A_k = O(1/k^2)$ and explain why the interior kink limits the convergence rate despite the good boundary behavior.

??? success "Solution to Exercise 5"
    We compute the cosine coefficients of $f(x) = |x|$ on $[-1, 1]$ using:

    $$
    A_k = \int_{-1}^{1}|x|\cos\!\left(\frac{k\pi(x+1)}{2}\right)dx
    $$

    Let $y = (x+1)/2$ so $x = 2y - 1$, $dx = 2\,dy$, and $|x| = |2y - 1|$. As $x$ ranges over $[-1, 1]$, $y$ ranges over $[0, 1]$:

    $$
    A_k = 2\int_0^1 |2y - 1|\cos(k\pi y)\,dy
    $$

    Split at $y = 1/2$: $|2y - 1| = 1 - 2y$ for $y \in [0, 1/2]$ and $|2y - 1| = 2y - 1$ for $y \in [1/2, 1]$.

    **$k = 0$:**

    $$
    A_0 = 2\int_0^1|2y-1|\,dy = 2\cdot\frac{1}{2} = 1
    $$

    (since $\int_0^1|2y-1|\,dy = 1/2$).

    **$k \geq 1$:** By the symmetry $|2y - 1| = |2(1-y) - 1|$ and the substitution $y \to 1 - y$:

    $$
    A_k = 4\int_0^{1/2}(1-2y)\cos(k\pi y)\,dy
    $$

    Integrating by parts twice:

    $$
    \int_0^{1/2}(1-2y)\cos(k\pi y)\,dy = \left[\frac{(1-2y)\sin(k\pi y)}{k\pi}\right]_0^{1/2} + \frac{2}{k\pi}\int_0^{1/2}\sin(k\pi y)\,dy
    $$

    The boundary term gives $0$ (since $1 - 2(1/2) = 0$ and $\sin(0) = 0$). The integral evaluates to:

    $$
    \frac{2}{k\pi}\cdot\frac{1-\cos(k\pi/2)}{k\pi} = \frac{2(1-\cos(k\pi/2))}{k^2\pi^2}
    $$

    So $A_k = 4\cdot\frac{2(1-\cos(k\pi/2))}{k^2\pi^2} = \frac{8(1-\cos(k\pi/2))}{k^2\pi^2}$.

    **First four coefficients:**

    - $A_0 = 1$
    - $A_1 = \frac{8(1-\cos(\pi/2))}{\pi^2} = \frac{8}{\pi^2} \approx 0.811$
    - $A_2 = \frac{8(1-\cos(\pi))}{4\pi^2} = \frac{8 \cdot 2}{4\pi^2} = \frac{4}{\pi^2} \approx 0.405$
    - $A_3 = \frac{8(1-\cos(3\pi/2))}{9\pi^2} = \frac{8}{9\pi^2} \approx 0.090$

    **Verification of $O(1/k^2)$ decay:** The factor $1 - \cos(k\pi/2)$ is bounded between 0 and 2, so $|A_k| \leq 16/(k^2\pi^2) = O(1/k^2)$.

    **Why the interior kink limits convergence:** The even extension about the boundaries $x = \pm 1$ produces a continuous periodic function (the reflection matches function values). However, the kink at $x = 0$ is an interior non-differentiability point that persists in any extension. The derivative $f'(x) = \text{sgn}(x)$ has a jump at $x = 0$ of magnitude 2, limiting the derivative's Fourier coefficients to $O(1/k)$ and hence $f$'s coefficients to $O(1/k^2)$. The cosine expansion eliminates boundary artifacts but cannot smooth interior singularities.

---

**Exercise 6.** Parseval's theorem for the cosine system states $\frac{2}{b-a}\int_a^b|f(x)|^2\,dx = \frac{A_0^2}{2} + \sum_{k=1}^{\infty}A_k^2$. For a probability density $f$ on $[a,b]$ with $\int_a^b f(x)\,dx = 1$, show that $A_0 = 2/(b-a)$ and use Parseval's theorem to derive a bound on $\sum_{k=1}^{\infty}A_k^2$ in terms of $\int_a^b f(x)^2\,dx$. What does this bound tell you about the number of terms needed in the cosine series?

---

??? success "Solution to Exercise 6"
    **Computing $A_0$:** By definition:

    $$
    A_0 = \frac{2}{b-a}\int_a^b f(x)\,dx = \frac{2}{b-a}\cdot 1 = \frac{2}{b-a}
    $$

    since $\int_a^b f(x)\,dx = 1$ for a probability density supported on $[a, b]$.

    **Parseval's theorem applied:** The cosine Parseval identity is:

    $$
    \frac{2}{b-a}\int_a^b |f(x)|^2\,dx = \frac{A_0^2}{2} + \sum_{k=1}^{\infty}A_k^2
    $$

    Substituting $A_0 = 2/(b-a)$:

    $$
    \sum_{k=1}^{\infty}A_k^2 = \frac{2}{b-a}\int_a^b f(x)^2\,dx - \frac{1}{2}\cdot\frac{4}{(b-a)^2} = \frac{2}{b-a}\int_a^b f(x)^2\,dx - \frac{2}{(b-a)^2}
    $$

    **Interpretation:** The total energy in the non-constant cosine coefficients equals the "excess energy" of $f$ beyond the uniform density $1/(b-a)$. We can write this as:

    $$
    \sum_{k=1}^{\infty}A_k^2 = \frac{2}{b-a}\left[\int_a^b f(x)^2\,dx - \frac{1}{b-a}\right]
    $$

    By Jensen's inequality, $\int_a^b f(x)^2\,dx \geq \frac{1}{b-a}\left(\int_a^b f(x)\,dx\right)^2 = \frac{1}{b-a}$, with equality only for the uniform density $f(x) = 1/(b-a)$.

    **Implication for the number of terms:** The truncation error of the $N$-term cosine series satisfies $\|f - S_N^c f\|_2^2 = \frac{b-a}{2}\sum_{k=N}^{\infty}A_k^2$. A density that is "close to uniform" (small $\int f^2\,dx$) has small total coefficient energy, meaning fewer terms are needed. A highly concentrated density (large $\int f^2\,dx$, e.g., a narrow spike) has large coefficient energy spread over many harmonics, requiring more terms. In practice, the decay rate of individual $A_k$ (governed by smoothness) is more important than the total energy, but the Parseval bound gives a useful a priori estimate of the overall approximation quality.
