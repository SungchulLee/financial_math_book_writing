# Fourier Series on Finite Intervals

Fourier analysis provides the mathematical backbone of modern option pricing under models with known characteristic functions. Before developing the COS method and other Fourier pricing techniques, we must establish the classical theory of Fourier series on bounded intervals. The key insight is that any sufficiently regular function on $[a, b]$ can be decomposed into a sum of sinusoidal components, and the coefficients of this decomposition carry the same information as the original function. In the pricing context, this means we can reconstruct a probability density from its Fourier coefficients, which are directly computable from the characteristic function.

!!! info "Prerequisites"
    - Linear algebra: inner product spaces, orthogonality, projections
    - Real analysis: $L^2$ spaces, pointwise and uniform convergence
    - Basic probability: probability density functions, expectation

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define the Fourier series of a function on a general finite interval $[a, b]$
    2. Compute Fourier coefficients using orthogonality relations
    3. State and prove Parseval's theorem for $L^2$ functions
    4. Connect Fourier coefficients to the inner product structure of $L^2([a, b])$
    5. Recognize the role of Fourier series as the starting point for COS-based option pricing

---

## The Trigonometric System on a Finite Interval

The foundation of Fourier series is the orthogonality of the trigonometric system. Consider the interval $[a, b]$ with length $L = b - a$. The functions

$$
\left\{ 1,\; \cos\!\left(\frac{2\pi n x}{L}\right),\; \sin\!\left(\frac{2\pi n x}{L}\right) : n = 1, 2, 3, \dots \right\}
$$

form an orthogonal system in the Hilbert space $L^2([a, b])$ equipped with the inner product

$$
\langle f, g \rangle = \int_a^b f(x)\, g(x)\, dx
$$

The orthogonality relations are fundamental. For integers $m, n \geq 0$:

$$
\int_a^b \cos\!\left(\frac{2\pi m x}{L}\right) \cos\!\left(\frac{2\pi n x}{L}\right) dx = \begin{cases} L & \text{if } m = n = 0 \\ L/2 & \text{if } m = n \neq 0 \\ 0 & \text{if } m \neq n \end{cases}
$$

$$
\int_a^b \sin\!\left(\frac{2\pi m x}{L}\right) \sin\!\left(\frac{2\pi n x}{L}\right) dx = \begin{cases} L/2 & \text{if } m = n \neq 0 \\ 0 & \text{if } m \neq n \end{cases}
$$

$$
\int_a^b \cos\!\left(\frac{2\pi m x}{L}\right) \sin\!\left(\frac{2\pi n x}{L}\right) dx = 0 \quad \text{for all } m, n
$$

These identities follow from the product-to-sum formulas for trigonometric functions and direct integration. Orthogonality ensures that the coefficients in a Fourier expansion can be extracted individually, without coupling between different frequency components.

---

## Definition of Fourier Series

With the orthogonal system in hand, we can define the Fourier series representation of a function.

!!! note "Definition: Fourier Series on $[a, b]$"
    Let $f \in L^1([a, b])$ with $L = b - a$. The **Fourier series** of $f$ on $[a, b]$ is

    $$
    f(x) \sim \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos\!\left(\frac{2\pi n x}{L}\right) + b_n \sin\!\left(\frac{2\pi n x}{L}\right) \right]
    $$

    where the **Fourier coefficients** are

    $$
    a_n = \frac{2}{L} \int_a^b f(x)\, \cos\!\left(\frac{2\pi n x}{L}\right) dx, \quad n = 0, 1, 2, \dots
    $$

    $$
    b_n = \frac{2}{L} \int_a^b f(x)\, \sin\!\left(\frac{2\pi n x}{L}\right) dx, \quad n = 1, 2, 3, \dots
    $$

    The symbol $\sim$ indicates that the series is formally associated with $f$; equality in various senses is the subject of convergence theory.

The factor $a_0/2$ in front of the constant term is a convention that makes the formula for $a_n$ uniform across all $n \geq 0$. Setting $n = 0$ in the cosine coefficient formula yields $a_0 = \frac{2}{L}\int_a^b f(x)\,dx$, so the constant term $a_0/2$ equals the average value of $f$ on $[a, b]$.

---

## Derivation of the Coefficient Formulas

The Fourier coefficients arise naturally from the orthogonality of the trigonometric system. Suppose $f$ has the representation

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos\!\left(\frac{2\pi n x}{L}\right) + b_n \sin\!\left(\frac{2\pi n x}{L}\right) \right]
$$

To extract $a_m$ for $m \geq 1$, multiply both sides by $\cos(2\pi m x / L)$ and integrate over $[a, b]$. By orthogonality, every term on the right vanishes except the one with $n = m$:

$$
\int_a^b f(x)\, \cos\!\left(\frac{2\pi m x}{L}\right) dx = a_m \cdot \frac{L}{2}
$$

Solving for $a_m$ gives the formula above. The derivation of $b_m$ is identical, multiplying by $\sin(2\pi m x / L)$ instead. This procedure---projecting onto an orthogonal basis element---is the Fourier-analytic analogue of extracting coordinates in a finite-dimensional inner product space.

!!! tip "Projection Interpretation"
    The Fourier coefficients are the coordinates of $f$ in the orthonormal basis $\{e_n\}$ of $L^2([a, b])$. The $N$-th partial sum $S_N f$ is the orthogonal projection of $f$ onto the subspace spanned by the first $2N + 1$ basis functions. This projection minimizes the $L^2$ distance to $f$ among all trigonometric polynomials of degree at most $N$.

---

## Partial Sums and Best Approximation

The **$N$-th partial sum** of the Fourier series is the trigonometric polynomial

$$
S_N f(x) = \frac{a_0}{2} + \sum_{n=1}^{N} \left[ a_n \cos\!\left(\frac{2\pi n x}{L}\right) + b_n \sin\!\left(\frac{2\pi n x}{L}\right) \right]
$$

This partial sum enjoys a remarkable optimality property.

!!! note "Theorem: Best $L^2$ Approximation"
    Among all trigonometric polynomials $T_N(x) = \frac{\alpha_0}{2} + \sum_{n=1}^{N}[\alpha_n \cos(2\pi n x/L) + \beta_n \sin(2\pi n x/L)]$, the Fourier partial sum $S_N f$ uniquely minimizes the $L^2$ error:

    $$
    \|f - S_N f\|_2^2 \leq \|f - T_N\|_2^2
    $$

    with equality if and only if $T_N = S_N f$.

**Proof.** Write $T_N = S_N f + (T_N - S_N f)$. The difference $T_N - S_N f$ is a trigonometric polynomial whose Fourier coefficients are $\alpha_n - a_n$ and $\beta_n - b_n$. By orthogonality:

$$
\|f - T_N\|_2^2 = \|f - S_N f\|_2^2 + \|S_N f - T_N\|_2^2
$$

Since $\|S_N f - T_N\|_2^2 \geq 0$, the minimum is achieved when $T_N = S_N f$. $\square$

This result confirms that Fourier coefficients are not merely a convenient representation---they provide the provably optimal low-frequency approximation in the $L^2$ sense.

---

## Bessel's Inequality

Before proving Parseval's theorem, we establish a fundamental inequality that holds without any additional assumptions on $f$.

!!! note "Theorem: Bessel's Inequality"
    For any $f \in L^2([a, b])$:

    $$
    \frac{a_0^2}{4} + \frac{1}{2}\sum_{n=1}^{\infty} (a_n^2 + b_n^2) \leq \frac{1}{L}\int_a^b |f(x)|^2\, dx
    $$

**Proof.** The $L^2$ norm of the partial sum satisfies

$$
\|S_N f\|_2^2 = \frac{L}{2}\left(\frac{a_0^2}{2} + \sum_{n=1}^{N}(a_n^2 + b_n^2)\right)
$$

by orthogonality. Since $S_N f$ is the best $L^2$ approximation, $\|f - S_N f\|_2^2 \geq 0$ gives

$$
\|f\|_2^2 \geq \|S_N f\|_2^2 = \frac{L}{2}\left(\frac{a_0^2}{2} + \sum_{n=1}^{N}(a_n^2 + b_n^2)\right)
$$

Dividing by $L$ and letting $N \to \infty$ yields Bessel's inequality. $\square$

Bessel's inequality tells us that the sum of squared Fourier coefficients is bounded by the energy $\|f\|_2^2$ of the original function. The gap between the two sides, if any, represents the energy in $f$ that cannot be captured by the trigonometric system.

---

## Parseval's Theorem

When the trigonometric system is complete in $L^2([a, b])$---meaning no nonzero function is orthogonal to all basis elements---Bessel's inequality becomes an equality. This is Parseval's theorem, the cornerstone of $L^2$ Fourier analysis.

!!! note "Theorem: Parseval's Theorem"
    For any $f \in L^2([a, b])$:

    $$
    \frac{1}{L}\int_a^b |f(x)|^2\, dx = \frac{a_0^2}{4} + \frac{1}{2}\sum_{n=1}^{\infty}(a_n^2 + b_n^2)
    $$

    Equivalently, $\|f - S_N f\|_2 \to 0$ as $N \to \infty$.

**Proof.** The key step is showing that the trigonometric system is complete in $L^2([a, b])$. By the Stone--Weierstrass theorem, trigonometric polynomials are dense in $C([a, b])$ under the uniform norm. Since $C([a, b])$ is dense in $L^2([a, b])$ and uniform convergence implies $L^2$ convergence on bounded intervals, trigonometric polynomials are dense in $L^2([a, b])$.

Given $\varepsilon > 0$, choose a trigonometric polynomial $T_N$ with $\|f - T_N\|_2 < \varepsilon$. By the best approximation property, $\|f - S_N f\|_2 \leq \|f - T_N\|_2 < \varepsilon$. Hence $S_N f \to f$ in $L^2$.

Expanding $\|f - S_N f\|_2^2 = \|f\|_2^2 - \|S_N f\|_2^2 \to 0$ and using the orthogonality computation of $\|S_N f\|_2^2$ yields the identity. $\square$

!!! warning "Parseval's theorem is an $L^2$ statement"
    Parseval's theorem guarantees convergence in the $L^2$ norm, which is convergence in the mean-square sense. It does **not** guarantee pointwise convergence at every point. Functions that agree $L^2$-a.e. have the same Fourier coefficients, so pointwise behavior at individual points is not captured by this result. Pointwise convergence requires additional regularity assumptions, treated in the next section.

---

## Complex Exponential Form

The complex exponential form of the Fourier series is more compact and connects directly to the characteristic function in probability theory.

!!! note "Definition: Complex Fourier Series"
    Let $f \in L^1([a, b])$ with $L = b - a$. The **complex Fourier series** of $f$ is

    $$
    f(x) \sim \sum_{n=-\infty}^{\infty} c_n\, e^{2\pi i n x / L}
    $$

    where the **complex Fourier coefficients** are

    $$
    c_n = \frac{1}{L} \int_a^b f(x)\, e^{-2\pi i n x / L}\, dx, \quad n \in \mathbb{Z}
    $$

The relationship between real and complex coefficients is:

$$
c_0 = \frac{a_0}{2}, \qquad c_n = \frac{a_n - i b_n}{2}, \qquad c_{-n} = \frac{a_n + i b_n}{2} \quad (n \geq 1)
$$

When $f$ is real-valued, $c_{-n} = \overline{c_n}$, reflecting the conjugate symmetry that ensures the series sums to a real number.

Parseval's theorem in complex form becomes particularly elegant:

$$
\frac{1}{L}\int_a^b |f(x)|^2\, dx = \sum_{n=-\infty}^{\infty} |c_n|^2
$$

This is the form most directly relevant to financial applications, since the characteristic function $\phi(u) = \mathbb{E}[e^{iuX}]$ is essentially the Fourier transform (complex exponential inner product) of the density.

---

## Example: Fourier Series of a Linear Function

To build concrete intuition, we compute the Fourier series of a simple function on the standard interval $[0, 2\pi]$.

!!! example "Fourier Coefficients of $f(x) = x$ on $[0, 2\pi]$"
    For $f(x) = x$ on $[0, 2\pi]$ with $L = 2\pi$:

    **Constant term:**

    $$
    a_0 = \frac{2}{2\pi}\int_0^{2\pi} x\, dx = \frac{1}{\pi} \cdot 2\pi^2 = 2\pi
    $$

    **Cosine coefficients** ($n \geq 1$): Integration by parts gives

    $$
    a_n = \frac{1}{\pi}\int_0^{2\pi} x \cos(nx)\, dx = \frac{1}{\pi}\left[\frac{x \sin(nx)}{n} + \frac{\cos(nx)}{n^2}\right]_0^{2\pi} = 0
    $$

    **Sine coefficients** ($n \geq 1$): Integration by parts gives

    $$
    b_n = \frac{1}{\pi}\int_0^{2\pi} x \sin(nx)\, dx = \frac{1}{\pi}\left[-\frac{x \cos(nx)}{n} + \frac{\sin(nx)}{n^2}\right]_0^{2\pi} = -\frac{2}{n}
    $$

    Therefore the Fourier series is

    $$
    x \sim \pi - 2\sum_{n=1}^{\infty} \frac{\sin(nx)}{n}
    $$

    The series converges to $f(x) = x$ at every interior point $x \in (0, 2\pi)$, and to $\pi$ (the average of the left and right limits) at the endpoints where the periodic extension has a jump discontinuity.

---

## Example: Parseval's Identity Applied

Parseval's theorem can produce remarkable closed-form sums by choosing $f$ strategically.

!!! example "Basel Problem via Parseval's Theorem"
    Using $f(x) = x$ on $[0, 2\pi]$ with coefficients $a_0 = 2\pi$, $a_n = 0$, $b_n = -2/n$:

    $$
    \frac{1}{2\pi}\int_0^{2\pi} x^2\, dx = \frac{(2\pi)^2}{4} + \frac{1}{2}\sum_{n=1}^{\infty}\frac{4}{n^2}
    $$

    The left side equals $\frac{4\pi^2}{3}$. Hence

    $$
    \frac{4\pi^2}{3} = \pi^2 + 2\sum_{n=1}^{\infty}\frac{1}{n^2}
    $$

    Solving gives the celebrated Basel series:

    $$
    \sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}
    $$

    This demonstrates the power of Parseval's theorem: an energy identity for Fourier coefficients produces a number-theoretic result.

---

## Connection to Financial Applications

The Fourier series framework developed here is not merely classical analysis---it is the mathematical foundation for modern computational finance. The connection operates at three levels:

1. **Density representation.** A risk-neutral density $f(x)$ on a truncated interval $[a, b]$ admits a Fourier series whose coefficients encode the distribution. Recovering these coefficients from the characteristic function is the central idea of the COS method.

2. **Coefficient computation via characteristic function.** The complex Fourier coefficient $c_n$ involves $\int f(x) e^{-2\pi i n x / L}\, dx$, which is precisely the characteristic function $\phi$ evaluated at a specific frequency. This eliminates the need to know $f$ explicitly.

3. **Parseval's theorem and error control.** The energy identity guarantees that truncating the Fourier series to $N$ terms captures all but $\sum_{|n|>N} |c_n|^2$ of the energy. When coefficients decay rapidly (as they do for smooth densities), few terms suffice for high accuracy.

These connections are developed precisely in the sections on [Fourier Series of Probability Densities](fourier_series_of_densities.md) and [Cosine Coefficients via Characteristic Function](../cos_method/cosine_coefficients_via_cf.md).

---

## Summary

The Fourier series on a finite interval $[a, b]$ decomposes a function into sinusoidal components, with coefficients extracted via orthogonal projection. The central results are:

| Result | Statement |
|---|---|
| Fourier coefficients | $a_n = \frac{2}{L}\int_a^b f(x)\cos(2\pi n x/L)\,dx$, $b_n = \frac{2}{L}\int_a^b f(x)\sin(2\pi n x/L)\,dx$ |
| Best approximation | $S_N f$ minimizes $\|f - T_N\|_2$ over all trigonometric polynomials of degree $\leq N$ |
| Bessel's inequality | $\sum |c_n|^2 \leq \frac{1}{L}\|f\|_2^2$ |
| Parseval's theorem | $\sum |c_n|^2 = \frac{1}{L}\|f\|_2^2$ (completeness of trigonometric system) |

**The orthogonal decomposition of functions into sinusoidal components, together with Parseval's energy identity, provides the mathematical foundation for reconstructing probability densities from characteristic functions in the COS pricing method.**

---

## Exercises

**Exercise 1.** Compute the Fourier cosine and sine coefficients $a_n$ and $b_n$ for $f(x) = x^2$ on $[0, 2\pi]$. Verify the constant term $a_0/2$ equals the average value of $f$ on the interval. Use integration by parts and confirm that $a_n = O(1/n^2)$ and $b_n = O(1/n)$.

---

**Exercise 2.** Prove the orthogonality relation $\int_a^b \cos(2\pi m x / L)\sin(2\pi n x / L)\,dx = 0$ for all integers $m, n \geq 0$, where $L = b - a$. Use the product-to-sum identity $\cos\alpha\sin\beta = \frac{1}{2}[\sin(\alpha + \beta) - \sin(\alpha - \beta)]$.

---

**Exercise 3.** The best $L^2$ approximation theorem states that the Fourier partial sum $S_N f$ minimizes $\|f - T_N\|_2$ over all trigonometric polynomials of degree $\leq N$. Verify this numerically for $f(x) = e^{\cos x}$ on $[-\pi, \pi]$ by computing $\|f - S_N f\|_2$ for $N = 4, 8, 16$ and confirming that the error decreases with each increase in $N$.

---

**Exercise 4.** Using Parseval's theorem with the Fourier series of $f(x) = x$ on $[0, 2\pi]$ (which has $a_0 = 2\pi$, $a_n = 0$, and $b_n = -2/n$), derive the identity $\sum_{n=1}^{\infty}1/n^2 = \pi^2/6$. Explain each step of the derivation and identify where Parseval's equality is applied.

---

**Exercise 5.** Convert the real Fourier series of $f(x) = x$ on $[0, 2\pi]$ to complex exponential form $\sum_{n=-\infty}^{\infty} c_n e^{2\pi i n x / L}$. Verify that $c_{-n} = \overline{c_n}$ for all $n$, and confirm that Parseval's theorem in complex form $\sum_{n} |c_n|^2 = \frac{1}{L}\|f\|_2^2$ gives the same result as the real form.

---

**Exercise 6.** Bessel's inequality states $\frac{a_0^2}{4} + \frac{1}{2}\sum_{n=1}^{\infty}(a_n^2 + b_n^2) \leq \frac{1}{L}\int_a^b|f(x)|^2\,dx$. For a function $f \in L^2([a,b])$, explain under what conditions the inequality becomes an equality (Parseval's theorem). Give an example of a function space where Bessel's inequality is strict, and explain why.

---

**Exercise 7.** For the probability density $f(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$ truncated to $[-5, 5]$, compute the complex Fourier coefficient $c_n$ using $c_n = \frac{1}{L}\int_a^b f(x)e^{-2\pi i n x/L}\,dx$ and explain how this integral relates to the characteristic function $\phi(u) = e^{-u^2/2}$ evaluated at $u = 2\pi n / L$. This connection foreshadows the COS method.
