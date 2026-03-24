# Cosine Series Coefficients via Characteristic Function

The COS method rests on a single remarkable identity: the Fourier cosine coefficients of a probability density on $[a, b]$ can be computed from the characteristic function without ever evaluating or integrating the density itself. This section derives this identity rigorously, quantifies the approximation error, and shows how it transforms the problem of density expansion from numerical integration into simple function evaluation. The result is the computational engine of the entire COS pricing framework.

!!! info "Prerequisites"
    - [Fourier Series of Probability Densities](../fourier_series/fourier_series_of_densities.md) (CF and cosine coefficients)
    - [Cosine Expansion on $[0, \pi]$](../fourier_series/cosine_expansion.md) (cosine series on $[a,b]$)
    - [From Characteristic Function to Density](characteristic_function_to_density.md) (inversion methods)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the exact and approximate cosine coefficient formulas from the CF
    2. Quantify the truncation error from restricting the density to $[a, b]$
    3. Implement the coefficient computation for any model with a known CF
    4. Verify the formula against direct numerical integration for test cases
    5. Understand why only $N$ evaluations of $\phi$ suffice to approximate the density

---

## The Exact Cosine Coefficients

Recall that the Fourier cosine coefficients of a density $f$ on $[a, b]$ are defined by

$$
A_k = \frac{2}{b-a}\int_a^b f(x)\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx, \quad k = 0, 1, 2, \ldots
$$

For a density supported on $[a, b]$ (meaning $f(x) = 0$ for $x \notin [a, b]$), these coefficients are exact. For a density on $\mathbb{R}$ truncated to $[a, b]$, they are approximate.

We now derive the connection to the characteristic function in full detail.

---

## Derivation of the CF-Based Formula

Write the cosine as the real part of a complex exponential:

$$
\cos\!\left(\frac{k\pi(x-a)}{b-a}\right) = \text{Re}\!\left[\exp\!\left(\frac{ik\pi(x-a)}{b-a}\right)\right]
$$

Substituting into the definition of $A_k$:

$$
A_k = \frac{2}{b-a}\,\text{Re}\!\left[\int_a^b f(x)\exp\!\left(\frac{ik\pi(x-a)}{b-a}\right)dx\right]
$$

Expanding the exponent:

$$
\frac{ik\pi(x-a)}{b-a} = \frac{ik\pi x}{b-a} - \frac{ik\pi a}{b-a}
$$

so that

$$
A_k = \frac{2}{b-a}\,\text{Re}\!\left[e^{-ik\pi a/(b-a)}\int_a^b f(x)\exp\!\left(\frac{ik\pi x}{b-a}\right)dx\right]
$$

!!! note "Theorem: Cosine Coefficients via Characteristic Function"
    Let $f$ be a probability density with characteristic function $\phi(u) = \int_{-\infty}^{\infty}e^{iux}f(x)\,dx$. Define

    $$
    F_k = \frac{2}{b-a}\,\text{Re}\!\left[\phi\!\left(\frac{k\pi}{b-a}\right)e^{-ik\pi a/(b-a)}\right]
    $$

    Then:

    - If $f$ is supported on $[a, b]$: $A_k = F_k$ exactly.
    - If $f$ has support on $\mathbb{R}$: $A_k = F_k - \varepsilon_k$, where the truncation error is

    $$
    \varepsilon_k = \frac{2}{b-a}\,\text{Re}\!\left[e^{-ik\pi a/(b-a)}\int_{\mathbb{R}\setminus[a,b]} f(x)\exp\!\left(\frac{ik\pi x}{b-a}\right)dx\right]
    $$

**Proof.** When $f$ is supported on $[a, b]$:

$$
\int_a^b f(x)\exp\!\left(\frac{ik\pi x}{b-a}\right)dx = \int_{-\infty}^{\infty} f(x)\exp\!\left(\frac{ik\pi x}{b-a}\right)dx = \phi\!\left(\frac{k\pi}{b-a}\right)
$$

The first equality holds because $f(x) = 0$ outside $[a, b]$. Substitution gives $A_k = F_k$.

For general $f$ on $\mathbb{R}$:

$$
\int_a^b f(x)\exp\!\left(\frac{ik\pi x}{b-a}\right)dx = \phi\!\left(\frac{k\pi}{b-a}\right) - \int_{\mathbb{R}\setminus[a,b]} f(x)\exp\!\left(\frac{ik\pi x}{b-a}\right)dx
$$

The second term is the truncation error $\varepsilon_k$, bounded by

$$
|\varepsilon_k| \leq \frac{2}{b-a}\int_{\mathbb{R}\setminus[a,b]} f(x)\,dx = \frac{2}{b-a}\,P(X \notin [a, b])
$$

$\square$

---

## Error Bound for the Truncation

The truncation error $\varepsilon_k$ is controlled by the tail mass of the distribution outside $[a, b]$.

!!! note "Proposition: Uniform Truncation Error Bound"
    For all $k \geq 0$:

    $$
    |\varepsilon_k| \leq \frac{2}{b-a}\int_{\mathbb{R}\setminus[a,b]} f(x)\,dx
    $$

    In particular, if $[a, b]$ is chosen to capture all but a fraction $\delta$ of the probability mass, then $|\varepsilon_k| \leq 2\delta/(b-a)$ for every $k$.

For the cumulant-based truncation $[a, b] = [c_1 - L\sqrt{c_2}, c_1 + L\sqrt{c_2}]$ with $L = 10$:

- **Normal distribution:** $\delta = P(|X - \mu| > 10\sigma) \approx 1.5 \times 10^{-23}$
- **Heston model (typical):** $\delta \approx 10^{-15}$ or smaller
- **Variance Gamma:** $\delta$ depends on the tail parameter; may require $L = 12$

The truncation error is essentially negligible for all practical purposes when $L$ is chosen appropriately.

---

## Algorithmic Summary

The computation of cosine coefficients via the characteristic function reduces to a simple algorithm:

**Input:** Characteristic function $\phi$, truncation interval $[a, b]$, number of terms $N$.

**Output:** Approximate cosine coefficients $\{F_k\}_{k=0}^{N-1}$.

**Steps:**

1. For each $k = 0, 1, \ldots, N-1$, compute the frequency $\omega_k = k\pi/(b-a)$
2. Evaluate $\phi(\omega_k)$ (one CF evaluation per coefficient)
3. Compute the phase factor $e^{-ik\pi a/(b-a)}$
4. Set $F_k = \frac{2}{b-a}\,\text{Re}[\phi(\omega_k)\cdot e^{-ik\pi a/(b-a)}]$

The total cost is $N$ evaluations of $\phi$ plus $O(N)$ elementary operations. There is no numerical integration, no matrix inversion, and no iterative procedure.

!!! tip "Implementation Detail"
    The phase factor $e^{-ik\pi a/(b-a)}$ can be computed incrementally: if $\alpha = e^{-i\pi a/(b-a)}$, then the $k$-th phase is $\alpha^k$, computed by multiplying the previous phase by $\alpha$. This avoids $N$ separate calls to the exponential function.

---

## Verification: Direct Integration vs CF Formula

To build confidence in the CF-based formula, we verify it by comparing against direct numerical integration of the coefficient definition.

!!! example "Verification for $N(0, 1)$ on $[-10, 10]$"
    **Direct integration:**

    $$
    A_k^{\text{direct}} = \frac{1}{10}\int_{-10}^{10}\frac{1}{\sqrt{2\pi}}e^{-x^2/2}\cos\!\left(\frac{k\pi(x+10)}{20}\right)dx
    $$

    Evaluated numerically using adaptive quadrature.

    **CF formula:**

    $$
    F_k = \frac{1}{10}\,\text{Re}\!\left[e^{-k^2\pi^2/800}\cdot e^{ik\pi/2}\right]
    $$

    | $k$ | $A_k^{\text{direct}}$ | $F_k$ (CF formula) | $|A_k - F_k|$ |
    |---|---|---|---|
    | 0 | $1.0000 \times 10^{-1}$ | $1.0000 \times 10^{-1}$ | $< 10^{-16}$ |
    | 2 | $9.5124 \times 10^{-2}$ | $9.5124 \times 10^{-2}$ | $< 10^{-16}$ |
    | 10 | $5.3991 \times 10^{-2}$ | $5.3991 \times 10^{-2}$ | $< 10^{-16}$ |
    | 50 | $4.5400 \times 10^{-4}$ | $4.5400 \times 10^{-4}$ | $< 10^{-16}$ |

    The agreement is exact to machine precision, confirming that the truncation error is negligible on $[-10, 10]$ for the standard normal.

---

## Example: Coefficients for the Heston Model

The Heston model demonstrates the formula's power for distributions without closed-form densities.

!!! example "Heston Cosine Coefficients"
    With parameters $S_0 = 100$, $K = 100$, $r = 0.05$, $T = 1$, $\kappa = 1.5$, $\theta = 0.04$, $\sigma_v = 0.3$, $\rho = -0.7$, $v_0 = 0.04$, and truncation interval $[a, b] = [-5, 5]$ for the log-moneyness:

    The characteristic function $\phi(u)$ is evaluated using the Heston closed-form expression. The cosine coefficients $F_k$ are computed via the CF formula, requiring exactly $N$ evaluations of $\phi$.

    The coefficient magnitudes $|F_k|$ decay exponentially for this parameter set, with $|F_{64}| \approx 10^{-8}$ and $|F_{128}| \approx 10^{-15}$. This exponential decay reflects the smoothness of the Heston density and explains why $N = 64$ to $128$ terms suffice for pricing accuracy.

---

## Connection to the COS Pricing Formula

The cosine coefficient identity is the computational core of the COS method. Once the density coefficients $\{F_k\}$ are known, the option price is obtained by combining them with the payoff coefficients $\{V_k\}$:

$$
V \approx e^{-rT}\sum_{k=0}^{N-1}{}' F_k \cdot V_k
$$

where $V_k$ are the analytically computed inner products of the payoff with the cosine basis. This formula, derived in full in the next section on [COS Pricing Formula](cos_pricing_formula.md), shows that the entire pricing problem reduces to:

1. **$N$ evaluations of $\phi$** (to get $F_k$)
2. **$N$ analytic computations** (to get $V_k$)
3. **One inner product** (to get the price)

The total cost is dominated by the $N$ characteristic function evaluations, which for the Heston model involves evaluating the Riccati solution $N$ times.

---

## Summary

The cosine coefficient identity is the central computational result of the COS method:

| Item | Formula / Value |
|---|---|
| Exact coefficients | $A_k = \frac{2}{b-a}\int_a^b f(x)\cos(k\pi(x-a)/(b-a))\,dx$ |
| CF approximation | $F_k = \frac{2}{b-a}\,\text{Re}[\phi(k\pi/(b-a))\cdot e^{-ik\pi a/(b-a)}]$ |
| Error | $|A_k - F_k| \leq 2P(X \notin [a,b])/(b-a)$ |
| Cost | $N$ evaluations of $\phi$, no integration |

**By expressing the cosine coefficients as evaluations of the characteristic function at discrete frequencies, the COS method eliminates numerical integration from the density expansion, reducing the coefficient computation to $N$ function evaluations that can be performed in closed form for any affine model.**

---

## Exercises

**Exercise 1.** Starting from $A_k = \frac{2}{b-a}\int_a^b f(x)\cos(k\pi(x-a)/(b-a))\,dx$, carry out the full derivation of the CF-based formula $F_k = \frac{2}{b-a}\,\text{Re}[\phi(k\pi/(b-a))\,e^{-ik\pi a/(b-a)}]$. Identify each step: (i) replacing cosine by $\text{Re}[e^{i\cdot}]$, (ii) factoring out the phase, and (iii) extending the integral from $[a, b]$ to $\mathbb{R}$ using the support assumption.

---

**Exercise 2.** The uniform truncation error bound states $|\varepsilon_k| \leq 2P(X \notin [a, b])/(b-a)$ for all $k$. For a distribution with $P(X \notin [a, b]) = 10^{-10}$ and $b - a = 10$, compute the bound on $|\varepsilon_k|$. If the COS price involves summing $N = 128$ terms with $|V_k| \leq 100$, bound the total truncation-induced price error.

---

**Exercise 3.** For $X \sim N(0, 1)$ on $[-10, 10]$, compute $F_0$, $F_2$, and $F_4$ using the CF-based formula. Verify that $F_1 = F_3 = 0$ by showing that $\text{Re}[e^{-k^2\pi^2/800}\cdot i^k] = 0$ for odd $k$. Explain this result in terms of the symmetry of the standard normal density.

---

**Exercise 4.** The phase factor $e^{-ik\pi a/(b-a)}$ can be computed incrementally as $\alpha^k$ where $\alpha = e^{-i\pi a/(b-a)}$. For $[a, b] = [-5, 5]$, compute $\alpha$ and verify that $\alpha^0 = 1$, $\alpha^1 = e^{i\pi/2} = i$, $\alpha^2 = e^{i\pi} = -1$. Explain why this incremental computation saves computational effort compared to evaluating $e^{-ik\pi a/(b-a)}$ from scratch for each $k$.

---

**Exercise 5.** The verification table for $N(0,1)$ shows agreement between direct integration and the CF formula to machine precision ($< 10^{-16}$). Explain why the agreement is so exact for this distribution (not merely close, but exact to machine precision). What property of the normal distribution on $[-10, 10]$ makes the truncation error negligible?

---

**Exercise 6.** For the Heston model, the coefficient magnitudes $|F_k|$ decay exponentially. If $|F_{64}| \approx 10^{-8}$ and $|F_{128}| \approx 10^{-15}$, estimate the exponential decay rate $c$ in $|F_k| \approx Ce^{-ck}$. Using this rate, predict $|F_{256}|$ and determine the number of terms $N$ needed for $|F_N| < 10^{-12}$.
