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
    Let $f(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ on $[-10, 10]$. The cosine coefficients are

    $$
    A_k = \frac{2}{20}\int_{-10}^{10} \frac{1}{\sqrt{2\pi}}e^{-x^2/2}\cos\!\left(\frac{k\pi(x+10)}{20}\right)dx
    $$

    Since the Gaussian is analytic (entire), the cosine coefficients decay exponentially. Numerically:

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

The Fourier cosine series on $[a, b]$ is the expansion chosen by the COS method (Fang and Oosterlee, 2008) for representing the risk-neutral density. The reasons for this choice are now clear:

1. **Boundary compatibility.** Probability densities typically decay to zero or near-zero at the boundaries of the truncation interval $[a, b]$, so the even extension is smooth at the boundaries. This avoids the artificial discontinuities that would arise from periodic extension in the full Fourier series.

2. **Rapid convergence.** For smooth densities (as produced by affine models), the cosine coefficients decay exponentially, requiring only $N = 64$ to $128$ terms.

3. **Simple coefficient recovery.** As shown in the next section on [Cosine Coefficients via CF](../cos_method/cosine_coefficients_via_cf.md), the cosine coefficients $A_k$ can be expressed in terms of the characteristic function, enabling coefficient computation without knowing the density explicitly.

4. **Real-valued series.** The cosine series produces real-valued partial sums automatically, avoiding the need to take real parts of complex exponentials at each evaluation point.

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

---

**Exercise 2.** Explain why the cosine expansion of a non-periodic function $f$ on $[a, b]$ converges faster than the full Fourier series. Specifically, if $f(a) \neq f(b)$, show that the periodic extension of $f$ has a jump discontinuity at the boundary (producing $O(1/n)$ coefficient decay), while the even extension used by the cosine series is continuous at the boundary (producing at least $O(1/n^2)$ decay).

---

**Exercise 3.** Verify the orthogonality of the cosine system on $[a, b]$: show that $\int_a^b \cos(k\pi(x-a)/(b-a))\cos(j\pi(x-a)/(b-a))\,dx = 0$ when $k \neq j$. Use the substitution $y = (x - a)/(b - a)$ to reduce to a standard integral on $[0, 1]$.

---

**Exercise 4.** For the standard normal density $f(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ truncated to $[-10, 10]$, the cosine coefficients $A_k$ decay exponentially. Using the table of approximate values in the text ($A_0 \approx 0.1000$, $A_{50} \approx 0.0030$, $A_{100} \approx 10^{-8}$), estimate the exponential decay rate by fitting $|A_k| \approx Ce^{-\alpha k^2}$ and determine $C$ and $\alpha$.

---

**Exercise 5.** The function $f(x) = |x|$ on $[-1, 1]$ has a kink at $x = 0$. Compute the first four cosine coefficients on $[-1, 1]$ using $A_k = \int_{-1}^{1}|x|\cos(k\pi(x+1)/2)\,dx$. Verify that $A_k = O(1/k^2)$ and explain why the interior kink limits the convergence rate despite the good boundary behavior.

---

**Exercise 6.** Parseval's theorem for the cosine system states $\frac{2}{b-a}\int_a^b|f(x)|^2\,dx = \frac{A_0^2}{2} + \sum_{k=1}^{\infty}A_k^2$. For a probability density $f$ on $[a,b]$ with $\int_a^b f(x)\,dx = 1$, show that $A_0 = 2/(b-a)$ and use Parseval's theorem to derive a bound on $\sum_{k=1}^{\infty}A_k^2$ in terms of $\int_a^b f(x)^2\,dx$. What does this bound tell you about the number of terms needed in the cosine series?
