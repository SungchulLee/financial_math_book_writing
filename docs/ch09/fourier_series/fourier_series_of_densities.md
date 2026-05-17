# Fourier Series of Probability Densities

A probability density $f(x)$ and its characteristic function $\phi(u) = \mathbb{E}[e^{iuX}]$ are Fourier duals: each determines the other uniquely. The previous sections developed the Fourier cosine series on a finite interval $[a, b]$ and showed that smooth functions have rapidly decaying coefficients. This section combines these ideas by showing that the cosine coefficients of a density can be expressed directly in terms of the characteristic function. This relationship is the bridge between the analytic world (where characteristic functions are known in closed form for many financial models) and the computational world (where densities and option prices must be evaluated numerically).

!!! info "Prerequisites"

    - [Fourier Series on Finite Intervals](fourier_series_finite_intervals.md) (Fourier coefficients)
    - [Cosine Expansion on $[0, \pi]$](cosine_expansion.md) (cosine series on $[a, b]$)
    - Probability: characteristic functions, moment-generating functions

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Express the Fourier cosine coefficients of a density in terms of its characteristic function
    2. State the Fourier inversion theorem for recovering a density from its characteristic function
    3. Explain the duality between time-domain (density) and frequency-domain (CF) representations
    4. Identify the approximation introduced by restricting a density from $\mathbb{R}$ to $[a, b]$
    5. Compute cosine coefficients for the normal and log-normal densities via their characteristic functions

---

## Characteristic Functions as Fourier Transforms

The characteristic function of a random variable $X$ with density $f$ is defined as

$$
\phi(u) = \mathbb{E}[e^{iuX}] = \int_{-\infty}^{\infty} e^{iux} f(x)\,dx
$$

This is exactly the Fourier transform of $f$ (with the convention used in probability, which differs from the analysis convention by a sign in the exponent). The characteristic function always exists for any random variable, is uniformly continuous, satisfies $\phi(0) = 1$ and $|\phi(u)| \leq 1$, and uniquely determines the distribution.

The key properties for our purposes are:

1. **Uniqueness.** Two distributions with the same characteristic function are identical.
2. **Inversion.** Under suitable conditions, $f$ can be recovered from $\phi$ via the inverse Fourier transform.
3. **Closed-form availability.** For affine models (Black--Scholes, Heston, Bates, Variance Gamma, etc.), $\phi$ is known in closed form even when $f$ has no elementary expression.

---

## Fourier Inversion Theorem

The fundamental result linking the characteristic function back to the density is the Fourier inversion theorem.

!!! note "Theorem: Fourier Inversion"
    If $\phi \in L^1(\mathbb{R})$ (i.e., $\int_{-\infty}^{\infty}|\phi(u)|\,du < \infty$), then $X$ has a bounded continuous density given by

    $$
    f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{-iux}\phi(u)\,du
    $$

**Proof sketch.** Introduce the Gaussian regularization $f_\varepsilon(x) = \frac{1}{2\pi}\int e^{-iux}\phi(u)e^{-\varepsilon u^2/2}\,du$ and exchange integrals via Fubini. The inner integral is the Fourier transform of a Gaussian (Recall, see [§ Fundamental solution of the heat equation](../../ch05/heat_equation/fundamental_solution.md)), so $f_\varepsilon$ is the convolution of $f$ with a heat kernel of variance $\varepsilon$ and converges to $f$ at continuity points. Dominated convergence then removes the regularization when $\phi \in L^1$. $\square$

!!! warning "Integrability Condition"
    The condition $\phi \in L^1(\mathbb{R})$ is not always satisfied. For example, the Cauchy distribution has $\phi(u) = e^{-|u|}$, which is $L^1$, so inversion works. But for distributions with atoms (point masses), $\phi$ does not decay to zero and inversion in the pointwise sense fails. For most financial models (where the log-price has a continuous density), $\phi \in L^1$ holds.

---

## Cosine Coefficients via the Characteristic Function

Now we connect the Fourier cosine series on $[a, b]$ to the characteristic function. Recall that the cosine coefficients of $f$ on $[a, b]$ are

$$
A_k = \frac{2}{b-a}\int_a^b f(x)\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx
$$

We can relate this to $\phi$ by writing the cosine in terms of complex exponentials:

$$
\cos\!\left(\frac{k\pi(x-a)}{b-a}\right) = \text{Re}\!\left[e^{ik\pi(x-a)/(b-a)}\right]
$$

Substituting into the coefficient formula:

$$
A_k = \frac{2}{b-a}\,\text{Re}\!\left[\int_a^b f(x)\,e^{ik\pi(x-a)/(b-a)}\,dx\right]
$$

Factoring out $e^{-ik\pi a/(b-a)}$:

$$
A_k = \frac{2}{b-a}\,\text{Re}\!\left[e^{-ik\pi a/(b-a)}\int_a^b f(x)\,e^{ik\pi x/(b-a)}\,dx\right]
$$

!!! note "Theorem: CF-Based Cosine Coefficients"
    If $f$ is a probability density supported on $[a, b]$ (or approximately supported, with negligible mass outside $[a, b]$), then the cosine coefficients satisfy

    $$
    A_k \approx \frac{2}{b-a}\,\text{Re}\!\left[\phi\!\left(\frac{k\pi}{b-a}\right) e^{-ik\pi a/(b-a)}\right]
    $$

    where $\phi(u) = \int_{-\infty}^{\infty} e^{iux}f(x)\,dx$ is the characteristic function. The approximation becomes exact when $f$ is supported entirely on $[a, b]$.

**Proof.** When $f$ is supported on $[a, b]$:

$$
\int_a^b f(x)\,e^{ik\pi x/(b-a)}\,dx = \int_{-\infty}^{\infty} f(x)\,e^{ik\pi x/(b-a)}\,dx = \phi\!\left(\frac{k\pi}{b-a}\right)
$$

The first equality holds because $f(x) = 0$ outside $[a, b]$. Substituting into the cosine coefficient formula gives the result. When $f$ has mass outside $[a, b]$, the integral over $[a, b]$ differs from the full characteristic function by $\int_{\mathbb{R}\setminus[a,b]} f(x)e^{ik\pi x/(b-a)}\,dx$, which is the truncation error. $\square$

This result is the central identity of the COS method (Recall, see [§ COS method](../cos_method/characteristic_function_to_density.md)): to compute cosine coefficients of the density, evaluate $\phi$ at the discrete frequencies $k\pi/(b-a)$ and apply a phase rotation---no numerical integration or density evaluation is required.

---

## The Approximation Chain

The full COS approximation involves two levels of approximation, each with a controllable error:

**Step 1: Truncation to $[a, b]$.** Replace the density on $\mathbb{R}$ by its restriction to $[a, b]$:

$$
f(x) \approx f(x)\,\mathbf{1}_{[a,b]}(x)
$$

This introduces a **truncation error** equal to $\int_{\mathbb{R}\setminus[a,b]} f(x)\,dx$, the probability mass outside $[a, b]$. For the normal density with $[a, b] = [\mu - L\sigma, \mu + L\sigma]$, this error is $\text{erfc}(L/\sqrt{2}) \approx 10^{-23}$ for $L = 10$.

**Step 2: Series truncation to $N$ terms.** Replace the infinite cosine series by its $N$-term partial sum:

$$
f(x) \approx \sum_{k=0}^{N-1}{}' A_k \cos\!\left(\frac{k\pi(x-a)}{b-a}\right)
$$

The **series truncation error** is $\sum_{k=N}^{\infty} A_k \cos(\cdots)$, which decays at the rate determined by the smoothness of $f$ (exponentially for analytic densities).

---

## Example: Normal Density

The standard normal distribution provides a clean verification of the CF-based coefficient formula.

!!! example "Cosine Coefficients of the Normal Density"
    Recall (see [§ Fundamental solution of the heat equation](../../ch05/heat_equation/fundamental_solution.md)) that for $X \sim N(0,1)$ the characteristic function is $\phi(u) = e^{-u^2/2}$. On $[a,b]=[-10,10]$ the CF-based formula gives

    $$
    A_k = \frac{1}{10}\,\text{Re}\!\left[e^{-k^2\pi^2/800}\cdot i^k\right]
    $$

    Odd-$k$ coefficients vanish (by symmetry of $f$ and of $[a,b]$ about $0$), and even-$k$ coefficients decay as $e^{-ck^2}$, matching the entire analyticity of the Gaussian.

---

## Example: Log-Normal Density

Recall (see [§ GBM SDE](../../ch03/sde/index.md) and [§ Feynman--Kac](../../ch06/bs_pde_analytic_solution/feynman_kac.md)) that under Black--Scholes the log-price $X = \ln S_T$ has $\phi(u) = e^{i\mu u - \sigma^2 u^2/2}$. Substituting into the CF-based coefficient identity produces Gaussian decay $e^{-\sigma^2 k^2 \pi^2/(2(b-a)^2)}$ in $k$, so $N = 64$ terms yield option-pricing accuracy of order $10^{-10}$ for typical parameters ($\sigma = 0.2$, $T = 1$).

---

## Density on the Real Line vs Finite Interval

A subtle but important point: probability densities in finance are typically supported on $\mathbb{R}$ (or $\mathbb{R}^+$), not on a finite interval. The Fourier cosine series requires a finite interval, so we must truncate.

The key observation is that for densities with exponential or Gaussian tails, the truncation error is negligible when $[a, b]$ is chosen wide enough. Specifically:

!!! note "Proposition: Truncation Error Bound"
    If $f$ is a density with characteristic function $\phi$ and cumulants $c_1$ (mean), $c_2$ (variance), $c_3$ (third cumulant), $c_4$ (fourth cumulant), then with the truncation interval

    $$
    [a, b] = \left[c_1 - L\sqrt{c_2 + \sqrt{c_4 + 2c_2^2}},\;\; c_1 + L\sqrt{c_2 + \sqrt{c_4 + 2c_2^2}}\right]
    $$

    the truncation error satisfies $\int_{\mathbb{R}\setminus[a,b]}f(x)\,dx \leq C\,e^{-\alpha L^2}$ for constants $C, \alpha > 0$ depending on the tail behavior of $f$. The parameter $L$ is typically chosen as $L = 10$ or $L = 12$.

This cumulant-based truncation rule, introduced by Fang and Oosterlee (2008), ensures that the truncation interval adapts to the shape of the distribution: wider for heavy-tailed distributions and narrower for concentrated ones.

---

## The Duality Perspective

The relationship between densities and characteristic functions is a perfect duality:

| Time domain (density $f$) | Frequency domain (CF $\phi$) |
|---|---|
| Density values $f(x)$ | CF values $\phi(u)$ |
| Convolution of densities | Multiplication of CFs |
| Differentiation of $f$ | Multiplication by $iu$ |
| Moments $\mathbb{E}[X^n]$ | Derivatives $\phi^{(n)}(0)/i^n$ |
| Cosine coefficients $A_k$ | CF at discrete frequencies $\phi(k\pi/(b-a))$ |

The last row is the COS method's contribution: it discretizes the duality. Instead of the full Fourier transform pair $f \leftrightarrow \phi$, the COS method uses the finite set of CF evaluations $\{\phi(k\pi/(b-a))\}_{k=0}^{N-1}$ to reconstruct $f$ via a truncated cosine series.

---

## Summary

The Fourier series representation of probability densities connects the characteristic function (computable in closed form for most financial models) to the cosine coefficients (needed for density reconstruction and option pricing):

| Concept | Formula |
|---|---|
| Cosine coefficients from CF | $A_k \approx \frac{2}{b-a}\,\text{Re}\!\left[\phi\!\left(\frac{k\pi}{b-a}\right)e^{-ik\pi a/(b-a)}\right]$ |
| Truncation error | $\int_{\mathbb{R}\setminus[a,b]}f(x)\,dx$, exponentially small for light-tailed densities |
| Series truncation error | $\sum_{k \geq N}A_k\cos(\cdots)$, decays at rate governed by smoothness of $f$ |
| Fourier inversion | $f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-iux}\phi(u)\,du$ |

**The characteristic function provides a closed-form frequency-domain representation of the density, and the cosine coefficient identity $A_k \approx \frac{2}{b-a}\,\text{Re}[\phi(k\pi/(b-a))e^{-ik\pi a/(b-a)}]$ is the fundamental formula that enables the COS method to price options without ever computing the density explicitly.**

---

## Exercises

**Exercise 1.** For a random variable $X \sim N(\mu, \sigma^2)$, the characteristic function is $\phi(u) = e^{i\mu u - \sigma^2 u^2/2}$. Verify the Fourier inversion theorem by computing $f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-iux}\phi(u)\,du$ and showing that the result is $\frac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^2/(2\sigma^2)}$. (Hint: complete the square in the exponent.)

??? success "Solution to Exercise 1"
    We verify the Fourier inversion theorem for $X \sim N(\mu, \sigma^2)$ with $\phi(u) = e^{i\mu u - \sigma^2 u^2/2}$.

    Compute:

    $$
    f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-iux}\phi(u)\,du = \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{-iux}\cdot e^{i\mu u - \sigma^2 u^2/2}\,du
    $$

    Combine the exponents:

    $$
    -iux + i\mu u - \frac{\sigma^2 u^2}{2} = -\frac{\sigma^2}{2}\left(u^2 - \frac{2i(\mu - x)}{\sigma^2}u\right)
    $$

    Complete the square in $u$:

    $$
    u^2 - \frac{2i(\mu - x)}{\sigma^2}u = \left(u - \frac{i(\mu - x)}{\sigma^2}\right)^2 + \frac{(\mu - x)^2}{\sigma^4}
    $$

    Substituting back:

    $$
    f(x) = \frac{1}{2\pi}\exp\!\left(-\frac{(\mu - x)^2}{2\sigma^2}\right)\int_{-\infty}^{\infty}\exp\!\left(-\frac{\sigma^2}{2}\left(u - \frac{i(\mu-x)}{\sigma^2}\right)^2\right)du
    $$

    The integral is a Gaussian integral along a shifted contour $u - i(\mu-x)/\sigma^2$. By Cauchy's theorem (the integrand is entire and decays in the appropriate directions), the contour can be shifted back to the real line:

    $$
    \int_{-\infty}^{\infty}\exp\!\left(-\frac{\sigma^2}{2}w^2\right)dw = \sqrt{\frac{2\pi}{\sigma^2}}
    $$

    Therefore:

    $$
    f(x) = \frac{1}{2\pi}\cdot\sqrt{\frac{2\pi}{\sigma^2}}\cdot\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right) = \frac{1}{\sigma\sqrt{2\pi}}\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
    $$

    This is indeed the $N(\mu, \sigma^2)$ density. $\square$

---

**Exercise 2.** Derive the cosine coefficient formula $A_k = \frac{2}{b-a}\,\text{Re}[\phi(k\pi/(b-a))\,e^{-ik\pi a/(b-a)}]$ starting from the definition $A_k = \frac{2}{b-a}\int_a^b f(x)\cos(k\pi(x-a)/(b-a))\,dx$. Identify the step where the assumption that $f$ is supported on $[a, b]$ is used, and write the expression for the error when $f$ has mass outside $[a, b]$.

??? success "Solution to Exercise 2"
    Starting from the definition:

    $$
    A_k = \frac{2}{b-a}\int_a^b f(x)\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx
    $$

    **Step 1:** Write the cosine as the real part of a complex exponential:

    $$
    \cos\!\left(\frac{k\pi(x-a)}{b-a}\right) = \text{Re}\!\left[e^{ik\pi(x-a)/(b-a)}\right]
    $$

    **Step 2:** Substitute and use linearity of $\text{Re}$:

    $$
    A_k = \frac{2}{b-a}\,\text{Re}\!\left[\int_a^b f(x)\,e^{ik\pi(x-a)/(b-a)}\,dx\right]
    $$

    **Step 3:** Factor out the phase:

    $$
    e^{ik\pi(x-a)/(b-a)} = e^{ik\pi x/(b-a)}\cdot e^{-ik\pi a/(b-a)}
    $$

    So:

    $$
    A_k = \frac{2}{b-a}\,\text{Re}\!\left[e^{-ik\pi a/(b-a)}\int_a^b f(x)\,e^{ik\pi x/(b-a)}\,dx\right]
    $$

    **Step 4 (key step using the support assumption):** If $f$ is supported on $[a, b]$, then $f(x) = 0$ for $x \notin [a, b]$, so:

    $$
    \int_a^b f(x)\,e^{ik\pi x/(b-a)}\,dx = \int_{-\infty}^{\infty} f(x)\,e^{ik\pi x/(b-a)}\,dx = \phi\!\left(\frac{k\pi}{b-a}\right)
    $$

    where $\phi(u) = \int_{-\infty}^{\infty}e^{iux}f(x)\,dx$ is the characteristic function. This substitution yields:

    $$
    A_k = \frac{2}{b-a}\,\text{Re}\!\left[\phi\!\left(\frac{k\pi}{b-a}\right)e^{-ik\pi a/(b-a)}\right]
    $$

    **Error when $f$ has mass outside $[a, b]$:** The integral over $[a, b]$ differs from $\phi(k\pi/(b-a))$ by the missing tails:

    $$
    \varepsilon_k = \frac{2}{b-a}\,\text{Re}\!\left[e^{-ik\pi a/(b-a)}\int_{\mathbb{R}\setminus[a,b]}f(x)\,e^{ik\pi x/(b-a)}\,dx\right]
    $$

    This truncation error satisfies:

    $$
    |\varepsilon_k| \leq \frac{2}{b-a}\int_{\mathbb{R}\setminus[a,b]}f(x)\,dx = \frac{2}{b-a}\,P(X \notin [a, b])
    $$

---

**Exercise 3.** For $X \sim N(0, 1)$ on $[a, b] = [-10, 10]$, compute $A_0$, $A_1$, $A_2$, and $A_3$ using the CF-based formula. Verify that odd-indexed coefficients vanish (i.e., $A_1 = A_3 = 0$) and explain this in terms of the symmetry of the standard normal density and the symmetric placement of the interval.

??? success "Solution to Exercise 3"
    For $X \sim N(0,1)$, $\phi(u) = e^{-u^2/2}$, on $[a, b] = [-10, 10]$ (so $b - a = 20$).

    The formula is:

    $$
    A_k = \frac{2}{20}\,\text{Re}\!\left[\phi\!\left(\frac{k\pi}{20}\right)e^{-ik\pi(-10)/20}\right] = \frac{1}{10}\,\text{Re}\!\left[e^{-k^2\pi^2/800}\cdot e^{ik\pi/2}\right]
    $$

    Note that $e^{ik\pi/2} = i^k$, so:

    - $k = 0$: $i^0 = 1$, so $A_0 = \frac{1}{10}\,\text{Re}[e^0 \cdot 1] = \frac{1}{10} = 0.1$
    - $k = 1$: $i^1 = i$, so $A_1 = \frac{1}{10}e^{-\pi^2/800}\,\text{Re}[i] = 0$
    - $k = 2$: $i^2 = -1$, so $A_2 = \frac{1}{10}e^{-4\pi^2/800}\,\text{Re}[-1] = -\frac{1}{10}e^{-\pi^2/200} \approx -0.0952$
    - $k = 3$: $i^3 = -i$, so $A_3 = \frac{1}{10}e^{-9\pi^2/800}\,\text{Re}[-i] = 0$

    **Odd-indexed coefficients vanish.** For odd $k$, $i^k$ is purely imaginary ($\pm i$), so $\text{Re}[i^k] = 0$, making $A_k = 0$.

    **Symmetry explanation:** The standard normal density is symmetric about $x = 0$: $f(x) = f(-x)$. The interval $[-10, 10]$ is symmetrically placed. The cosine basis functions $\cos(k\pi(x + 10)/20)$ with odd $k$ are antisymmetric about $x = 0$ (since $\cos(k\pi(x+10)/20) = \cos(k\pi/2 + k\pi x/20)$, and for odd $k$, $\cos(k\pi/2) = 0$ and the function is odd in $x$). Therefore, the integral of a symmetric density times an antisymmetric cosine function vanishes for odd $k$.

---

**Exercise 4.** The truncation error for the cosine coefficients is $\varepsilon_k = \frac{2}{b-a}\,\text{Re}[e^{-ik\pi a/(b-a)}\int_{\mathbb{R}\setminus[a,b]}f(x)e^{ik\pi x/(b-a)}\,dx]$. For the standard normal with $[a, b] = [-5, 5]$, bound $|\varepsilon_k|$ using $P(|X| > 5) \approx 5.7 \times 10^{-7}$. Is this bound tight enough for practical pricing applications? What happens if you use $[a, b] = [-3, 3]$ instead?

??? success "Solution to Exercise 4"
    The truncation error for coefficient $A_k$ is:

    $$
    |\varepsilon_k| \leq \frac{2}{b-a}\int_{\mathbb{R}\setminus[a,b]}f(x)\,dx = \frac{2}{b-a}\,P(|X| > 5)
    $$

    **For $[a, b] = [-5, 5]$:** With $P(|X| > 5) \approx 5.7 \times 10^{-7}$ and $b - a = 10$:

    $$
    |\varepsilon_k| \leq \frac{2}{10}\cdot 5.7 \times 10^{-7} = 1.14 \times 10^{-7}
    $$

    This is an error of order $10^{-7}$ per coefficient. For pricing applications requiring $10^{-6}$ to $10^{-8}$ accuracy, this is marginally acceptable. The bound may not be tight---the actual error could be smaller since the integral involves an oscillatory integrand $f(x)e^{ik\pi x/(b-a)}$ over the tails, which may partially cancel.

    **For $[a, b] = [-3, 3]$:** Now $P(|X| > 3) \approx 2.7 \times 10^{-3}$ and $b - a = 6$:

    $$
    |\varepsilon_k| \leq \frac{2}{6}\cdot 2.7 \times 10^{-3} = 9.0 \times 10^{-4}
    $$

    This is only $10^{-3}$ accuracy per coefficient---far too large for practical pricing. With $N$ terms, the cumulative truncation error can be even larger.

    **Conclusion:** The interval $[-5, 5]$ is adequate for moderate accuracy but the interval $[-10, 10]$ (with $P(|X| > 10) \approx 10^{-23}$) is preferred for high-precision work. The cumulant-based rule with $L = 10$ standard deviations ensures the truncation error is negligible compared to the series truncation error.

---

**Exercise 5.** The duality table states that convolution of densities corresponds to multiplication of characteristic functions. If $X_1$ and $X_2$ are independent with CFs $\phi_1$ and $\phi_2$, and $Y = X_1 + X_2$ has CF $\phi_Y = \phi_1 \cdot \phi_2$, explain how the cosine coefficients of the density of $Y$ relate to those of $X_1$ and $X_2$. Why is it generally easier to work in the frequency domain for sums of independent random variables?

??? success "Solution to Exercise 5"
    If $Y = X_1 + X_2$ with $X_1, X_2$ independent, then $\phi_Y(u) = \phi_1(u)\cdot\phi_2(u)$.

    The cosine coefficients of the density of $Y$ on $[a, b]$ are:

    $$
    A_k^Y = \frac{2}{b-a}\,\text{Re}\!\left[\phi_Y\!\left(\frac{k\pi}{b-a}\right)e^{-ik\pi a/(b-a)}\right] = \frac{2}{b-a}\,\text{Re}\!\left[\phi_1\!\left(\frac{k\pi}{b-a}\right)\phi_2\!\left(\frac{k\pi}{b-a}\right)e^{-ik\pi a/(b-a)}\right]
    $$

    The relationship is **not** a simple product $A_k^Y = A_k^{X_1}\cdot A_k^{X_2}$ because the cosine coefficients involve taking the real part and a phase factor. However, in the complex exponential form, the relationship is cleaner: if $c_n^Y$, $c_n^{X_1}$, $c_n^{X_2}$ denote the complex Fourier coefficients relative to the same interval, then:

    $$
    c_n^Y \approx \frac{1}{L}\phi_Y(2\pi n/L) = \frac{1}{L}\phi_1(2\pi n/L)\cdot\phi_2(2\pi n/L)
    $$

    This is proportional to the product of characteristic function values, but not simply $c_n^{X_1}\cdot c_n^{X_2}$ (the latter would require a convolution theorem for the discretized coefficients).

    **Why the frequency domain is easier:** In the time domain, computing the density of $Y = X_1 + X_2$ requires the convolution integral $f_Y(x) = \int f_1(y)f_2(x - y)\,dy$, which is an $O(N^2)$ computation when discretized. In the frequency domain, $\phi_Y = \phi_1 \cdot \phi_2$ is a pointwise multiplication---$O(N)$ operations. This is the fundamental computational advantage: convolution in the time domain becomes multiplication in the frequency domain. For sums of multiple independent variables ($Y = X_1 + \cdots + X_m$), the time-domain approach requires $m - 1$ nested convolutions, while the frequency domain requires only $m$ pointwise multiplications of characteristic functions.

---

**Exercise 6.** For the log-normal density (Black-Scholes model with $\sigma = 0.2$, $T = 1$, $r = 0.05$), compute the first four cumulants of the log-price $X = \ln S_T$. Use these to determine the truncation interval $[a, b] = [c_1 - L\sqrt{c_2}, c_1 + L\sqrt{c_2}]$ with $L = 10$. Estimate the truncation error $P(X \notin [a, b])$ and verify it is negligible.

---

??? success "Solution to Exercise 6"
    Under Black--Scholes, the log-price is $X = \ln S_T = \ln S_0 + (r - \sigma^2/2)T + \sigma\sqrt{T}\,Z$ where $Z \sim N(0,1)$.

    With $\sigma = 0.2$, $T = 1$, $r = 0.05$, and taking $S_0 = 1$ (so $\ln S_0 = 0$):

    $$
    X \sim N\!\left(\mu_X,\; \sigma_X^2\right)
    $$

    where $\mu_X = (r - \sigma^2/2)T = 0.05 - 0.02 = 0.03$ and $\sigma_X^2 = \sigma^2 T = 0.04$.

    **Cumulants of the normal distribution $N(\mu_X, \sigma_X^2)$:**

    - $c_1 = \mu_X = 0.03$ (mean)
    - $c_2 = \sigma_X^2 = 0.04$ (variance)
    - $c_3 = 0$ (the normal distribution has zero skewness, so the third cumulant vanishes)
    - $c_4 = 0$ (the normal distribution has zero excess kurtosis, so the fourth cumulant vanishes)

    **Truncation interval:** Using the simplified formula $[a, b] = [c_1 - L\sqrt{c_2},\; c_1 + L\sqrt{c_2}]$ with $L = 10$:

    $$
    \sqrt{c_2} = \sqrt{0.04} = 0.2
    $$

    $$
    a = 0.03 - 10 \times 0.2 = 0.03 - 2.0 = -1.97
    $$

    $$
    b = 0.03 + 10 \times 0.2 = 0.03 + 2.0 = 2.03
    $$

    So $[a, b] = [-1.97, 2.03]$.

    **Truncation error:** We need $P(X \notin [-1.97, 2.03])$. Standardizing:

    $$
    P(X < -1.97) = P\!\left(Z < \frac{-1.97 - 0.03}{0.2}\right) = P(Z < -10) \approx 7.6 \times 10^{-24}
    $$

    $$
    P(X > 2.03) = P\!\left(Z > \frac{2.03 - 0.03}{0.2}\right) = P(Z > 10) \approx 7.6 \times 10^{-24}
    $$

    Total truncation error:

    $$
    P(X \notin [-1.97, 2.03]) \approx 1.5 \times 10^{-23}
    $$

    This is far below machine precision ($\approx 10^{-16}$), confirming that the truncation error is completely negligible for any practical pricing computation. The COS method's error is entirely dominated by the series truncation, not the interval truncation.
