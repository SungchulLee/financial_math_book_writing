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

**Proof sketch.** Define $f_\varepsilon(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{-iux}\phi(u)e^{-\varepsilon u^2/2}\,du$ as a regularized inversion. The Gaussian factor ensures absolute convergence. Substituting $\phi(u) = \int e^{iuy}f(y)\,dy$ and exchanging integrals (justified by Fubini's theorem since the Gaussian damping makes the double integral absolutely convergent):

$$
f_\varepsilon(x) = \int_{-\infty}^{\infty} f(y)\left[\frac{1}{2\pi}\int_{-\infty}^{\infty} e^{iu(y-x)}e^{-\varepsilon u^2/2}\,du\right]dy
$$

The inner integral is a Gaussian in $u$, evaluating to $\frac{1}{\sqrt{2\pi\varepsilon}}e^{-(y-x)^2/(2\varepsilon)}$. Therefore $f_\varepsilon$ is the convolution of $f$ with a Gaussian kernel of variance $\varepsilon$, and $f_\varepsilon \to f$ pointwise at continuity points of $f$ as $\varepsilon \to 0$. When $\phi \in L^1$, the Gaussian regularization can be removed by dominated convergence. $\square$

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

This result is the central identity of the COS method. It says: **to compute the cosine coefficients of the density, evaluate the characteristic function at the discrete frequencies $k\pi/(b-a)$ and apply a phase rotation**. No numerical integration, no density evaluation, no inversion integral---just function evaluations of $\phi$.

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
    For $X \sim N(0, 1)$, the characteristic function is $\phi(u) = e^{-u^2/2}$. On $[a, b] = [-10, 10]$:

    $$
    A_k = \frac{2}{20}\,\text{Re}\!\left[\phi\!\left(\frac{k\pi}{20}\right)e^{-ik\pi(-10)/20}\right] = \frac{1}{10}\,\text{Re}\!\left[e^{-k^2\pi^2/800}\cdot e^{ik\pi/2}\right]
    $$

    Since $e^{ik\pi/2} = i^k$:

    - For $k = 0$: $A_0 = \frac{1}{10}\,\text{Re}[1] = 0.1$
    - For $k = 1$: $A_1 = \frac{1}{10}\,\text{Re}[e^{-\pi^2/800}\cdot i] = 0$ (purely imaginary)
    - For $k = 2$: $A_2 = \frac{1}{10}\,\text{Re}[e^{-4\pi^2/800}\cdot(-1)] = -\frac{1}{10}e^{-\pi^2/200}$

    The coefficients with odd $k$ vanish (reflecting the symmetry of the standard normal about $x = 0$ and the symmetric placement of $[a, b]$), and the even coefficients decay as $e^{-ck^2}$---faster than exponential, consistent with the entire analyticity of the Gaussian.

---

## Example: Log-Normal Density

The log-normal density has no elementary Fourier series, but its characteristic function allows coefficient computation.

!!! example "Log-Normal CF and Cosine Coefficients"
    If $\ln S_T \sim N(\mu, \sigma^2)$, the characteristic function of the log-price $X = \ln S_T$ is

    $$
    \phi(u) = e^{i\mu u - \sigma^2 u^2/2}
    $$

    The cosine coefficients on any interval $[a, b]$ are computed by:

    $$
    A_k = \frac{2}{b-a}\,\text{Re}\!\left[e^{i\mu k\pi/(b-a) - \sigma^2 k^2\pi^2/(2(b-a)^2)}\cdot e^{-ik\pi a/(b-a)}\right]
    $$

    The Gaussian decay $e^{-\sigma^2 k^2 \pi^2/(2(b-a)^2)}$ ensures exponential convergence. For typical Black--Scholes parameters ($\sigma = 0.2$, $T = 1$), $N = 64$ terms yield option prices accurate to $10^{-10}$.

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
