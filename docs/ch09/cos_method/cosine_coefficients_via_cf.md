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

**Recall** (see [§ Cosine Coefficients via the Characteristic Function](../fourier_series/fourier_series_of_densities.md#cosine-coefficients-via-the-characteristic-function)): writing $\cos(\cdot) = \text{Re}[e^{i\cdot}]$ and factoring the phase reduces the cosine-coefficient integral to a characteristic function evaluation.

!!! note "Theorem: Cosine Coefficients via Characteristic Function"
    Let $f$ be a probability density with characteristic function $\phi(u) = \int_{-\infty}^{\infty}e^{iux}f(x)\,dx$. Define

    $$
    F_k = \frac{2}{b-a}\,\text{Re}\!\left[\phi\!\left(\frac{k\pi}{b-a}\right)e^{-ik\pi a/(b-a)}\right]
    $$

    Then:

    - If $f$ is supported on $[a, b]$: $A_k = F_k$ exactly.
    - If $f$ has support on $\mathbb{R}$: $A_k = F_k - \varepsilon_k$, with truncation error bounded by

    $$
    |\varepsilon_k| \leq \frac{2}{b-a}\int_{\mathbb{R}\setminus[a,b]} f(x)\,dx = \frac{2}{b-a}\,P(X \notin [a, b])
    $$

The proof and explicit form of $\varepsilon_k$ are derived in [§ Fourier Series of Probability Densities](../fourier_series/fourier_series_of_densities.md#cosine-coefficients-via-the-characteristic-function). In what follows we treat $F_k$ as the COS-method input and focus on its algorithmic and error properties.

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

??? success "Solution to Exercise 1"
    **Step (i): Replace cosine by Re[$e^{i\cdot}$].**

    Starting from the definition:

    $$
    A_k = \frac{2}{b-a}\int_a^b f(x)\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx
    $$

    Use $\cos(\theta) = \text{Re}[e^{i\theta}]$:

    $$
    A_k = \frac{2}{b-a}\,\text{Re}\!\left[\int_a^b f(x)\exp\!\left(\frac{ik\pi(x-a)}{b-a}\right)dx\right]
    $$

    **Step (ii): Factor out the phase.**

    Expand the exponent: $\frac{ik\pi(x-a)}{b-a} = \frac{ik\pi x}{b-a} - \frac{ik\pi a}{b-a}$. The second term is independent of $x$, so factor it out:

    $$
    A_k = \frac{2}{b-a}\,\text{Re}\!\left[e^{-ik\pi a/(b-a)}\int_a^b f(x)\exp\!\left(\frac{ik\pi x}{b-a}\right)dx\right]
    $$

    **Step (iii): Extend the integral to $\mathbb{R}$.**

    If $f$ is supported on $[a, b]$ (i.e., $f(x) = 0$ for $x \notin [a, b]$), then:

    $$
    \int_a^b f(x)\exp\!\left(\frac{ik\pi x}{b-a}\right)dx = \int_{-\infty}^{\infty} f(x)\exp\!\left(\frac{ik\pi x}{b-a}\right)dx = \phi\!\left(\frac{k\pi}{b-a}\right)
    $$

    The last equality follows from the definition of the characteristic function $\phi(u) = \int_{-\infty}^{\infty}e^{iux}f(x)\,dx$ evaluated at $u = k\pi/(b-a)$.

    Substituting back:

    $$
    A_k = F_k = \frac{2}{b-a}\,\text{Re}\!\left[\phi\!\left(\frac{k\pi}{b-a}\right)e^{-ik\pi a/(b-a)}\right]
    $$

---

**Exercise 2.** The uniform truncation error bound states $|\varepsilon_k| \leq 2P(X \notin [a, b])/(b-a)$ for all $k$. For a distribution with $P(X \notin [a, b]) = 10^{-10}$ and $b - a = 10$, compute the bound on $|\varepsilon_k|$. If the COS price involves summing $N = 128$ terms with $|V_k| \leq 100$, bound the total truncation-induced price error.

??? success "Solution to Exercise 2"
    The uniform truncation error bound gives:

    $$
    |\varepsilon_k| \leq \frac{2\,P(X \notin [a,b])}{b-a} = \frac{2 \times 10^{-10}}{10} = 2 \times 10^{-11}
    $$

    This bound holds for every $k \geq 0$.

    The total truncation-induced error in the COS price is:

    $$
    |\text{price error}| \leq e^{-rT}\sum_{k=0}^{N-1}|\varepsilon_k|\,|V_k| \leq e^{-rT}\cdot N \cdot \frac{2\delta}{b-a}\cdot\max_k|V_k|
    $$

    With $N = 128$, $|\varepsilon_k| \leq 2 \times 10^{-11}$, and $|V_k| \leq 100$:

    $$
    |\text{price error}| \leq e^{-rT}\cdot 128 \cdot 2\times 10^{-11}\cdot 100 = e^{-rT}\cdot 2.56 \times 10^{-7}
    $$

    For typical interest rates and maturities, $e^{-rT} \leq 1$, so the total truncation-induced price error is bounded by approximately $2.56 \times 10^{-7}$. This is small enough for virtually all practical pricing applications.

---

**Exercise 3.** For $X \sim N(0, 1)$ on $[-10, 10]$, compute $F_0$, $F_2$, and $F_4$ using the CF-based formula. Verify that $F_1 = F_3 = 0$ by showing that $\text{Re}[e^{-k^2\pi^2/800}\cdot i^k] = 0$ for odd $k$. Explain this result in terms of the symmetry of the standard normal density.

??? success "Solution to Exercise 3"
    For $X \sim N(0, 1)$ on $[a, b] = [-10, 10]$, we have $b - a = 20$ and $\phi(u) = e^{-u^2/2}$. The CF-based formula gives:

    $$
    F_k = \frac{2}{20}\,\text{Re}\!\left[e^{-(k\pi/20)^2/2}\cdot e^{-ik\pi(-10)/20}\right] = \frac{1}{10}\,\text{Re}\!\left[e^{-k^2\pi^2/800}\cdot e^{ik\pi/2}\right]
    $$

    Note that $e^{ik\pi/2} = i^k$, so $i^0 = 1$, $i^1 = i$, $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, etc.

    **$F_0$:** $F_0 = \frac{1}{10}\,\text{Re}[e^0 \cdot 1] = \frac{1}{10} = 0.1$

    **$F_2$:** $F_2 = \frac{1}{10}\,\text{Re}[e^{-4\pi^2/800}\cdot(-1)] = -\frac{1}{10}e^{-\pi^2/200}$. Since $\pi^2/200 \approx 0.04935$, we get $F_2 = -0.1 \times e^{-0.04935} \approx -0.09519$.

    **$F_4$:** $F_4 = \frac{1}{10}\,\text{Re}[e^{-16\pi^2/800}\cdot 1] = \frac{1}{10}e^{-\pi^2/50}$. Since $\pi^2/50 \approx 0.19739$, we get $F_4 = 0.1 \times e^{-0.19739} \approx 0.08209$.

    **$F_1$ and $F_3$:** For $k = 1$: $\text{Re}[e^{-\pi^2/800}\cdot i] = 0$ since $\text{Re}[i] = 0$. For $k = 3$: $\text{Re}[e^{-9\pi^2/800}\cdot(-i)] = 0$ since $\text{Re}[-i] = 0$. In general, for odd $k$, $i^k$ is purely imaginary ($\pm i$), so $\text{Re}[e^{-k^2\pi^2/800}\cdot i^k] = 0$.

    **Symmetry explanation:** The standard normal density is symmetric about zero: $f(-x) = f(x)$. On the symmetric interval $[-10, 10]$, the cosine basis functions $\cos(k\pi(x+10)/20)$ for odd $k$ are antisymmetric about $x = 0$ (this follows from the phase relationship). The integral of a symmetric function times an antisymmetric function over a symmetric interval vanishes, giving $F_k = 0$ for odd $k$.

---

**Exercise 4.** The phase factor $e^{-ik\pi a/(b-a)}$ can be computed incrementally as $\alpha^k$ where $\alpha = e^{-i\pi a/(b-a)}$. For $[a, b] = [-5, 5]$, compute $\alpha$ and verify that $\alpha^0 = 1$, $\alpha^1 = e^{i\pi/2} = i$, $\alpha^2 = e^{i\pi} = -1$. Explain why this incremental computation saves computational effort compared to evaluating $e^{-ik\pi a/(b-a)}$ from scratch for each $k$.

??? success "Solution to Exercise 4"
    For $[a, b] = [-5, 5]$, we have $a/(b-a) = -5/10 = -1/2$, so the base phase factor is:

    $$
    \alpha = e^{-i\pi a/(b-a)} = e^{-i\pi(-1/2)} = e^{i\pi/2} = i
    $$

    Verification:

    - $\alpha^0 = 1$ (correct: $e^{0} = 1$)
    - $\alpha^1 = i$ (correct: $e^{i\pi/2} = i$)
    - $\alpha^2 = i^2 = -1$ (correct: $e^{i\pi} = -1$)

    **Why incremental computation saves effort:** Computing $e^{-ik\pi a/(b-a)}$ from scratch for each $k = 0, 1, \ldots, N-1$ requires $N$ calls to the complex exponential function (each involving evaluation of $\cos$ and $\sin$). The incremental approach computes $\alpha$ once and then obtains $\alpha^k = \alpha^{k-1}\cdot \alpha$ by a single complex multiplication per step (4 real multiplications and 2 real additions). Complex multiplication is much cheaper than evaluating trigonometric functions (which typically use polynomial approximations or lookup tables internally). For $N = 128$, this replaces 128 transcendental function evaluations with 1 transcendental evaluation plus 127 complex multiplications.

---

**Exercise 5.** The verification table for $N(0,1)$ shows agreement between direct integration and the CF formula to machine precision ($< 10^{-16}$). Explain why the agreement is so exact for this distribution (not merely close, but exact to machine precision). What property of the normal distribution on $[-10, 10]$ makes the truncation error negligible?

??? success "Solution to Exercise 5"
    The agreement is exact to machine precision (not merely close) because of two factors:

    **1. Negligible truncation error.** The standard normal density on $[-10, 10]$ has truncation error $P(|X| > 10) = \text{erfc}(10/\sqrt{2}) \approx 1.5 \times 10^{-23}$, which is far below the double-precision machine epsilon of $\approx 2.2 \times 10^{-16}$. This means the CF-based coefficients $F_k$ and the true cosine coefficients $A_k$ differ by an amount ($|\varepsilon_k| \leq 2 \times 1.5 \times 10^{-23}/20 \approx 1.5 \times 10^{-24}$) that is undetectable in double-precision arithmetic.

    **2. Both formulas evaluate exactly the same mathematical expression in floating point.** The CF formula $F_k = \frac{1}{10}\text{Re}[\phi(k\pi/20)\cdot e^{ik\pi/2}]$ and the numerical quadrature of $A_k^{\text{direct}}$ both reduce to evaluating the same Gaussian integrand. With adaptive quadrature (which achieves high accuracy for smooth integrands), the numerical integral converges to the same floating-point value as the CF formula.

    The key property of the normal distribution that makes this work is the extremely rapid (super-exponential) decay of the Gaussian tails, ensuring that essentially zero probability mass lies outside $[-10, 10]$.

---

**Exercise 6.** For the Heston model, the coefficient magnitudes $|F_k|$ decay exponentially. If $|F_{64}| \approx 10^{-8}$ and $|F_{128}| \approx 10^{-15}$, estimate the exponential decay rate $c$ in $|F_k| \approx Ce^{-ck}$. Using this rate, predict $|F_{256}|$ and determine the number of terms $N$ needed for $|F_N| < 10^{-12}$.

---

??? success "Solution to Exercise 6"
    Given $|F_k| \approx Ce^{-ck}$, we use the two data points:

    $$
    Ce^{-64c} \approx 10^{-8}, \quad Ce^{-128c} \approx 10^{-15}
    $$

    Dividing the second by the first:

    $$
    e^{-64c} = \frac{10^{-15}}{10^{-8}} = 10^{-7}
    $$

    Taking logarithms:

    $$
    -64c = -7\ln 10 \implies c = \frac{7\ln 10}{64} = \frac{7 \times 2.3026}{64} \approx 0.2519
    $$

    From the first equation: $C = 10^{-8}\cdot e^{64c} = 10^{-8}\cdot e^{16.12} \approx 10^{-8}\cdot 9.97 \times 10^{6} \approx 0.0997 \approx 0.1$.

    **Prediction for $|F_{256}|$:**

    $$
    |F_{256}| \approx 0.1\cdot e^{-0.2519\times 256} = 0.1\cdot e^{-64.49} \approx 0.1\times 10^{-28} = 10^{-29}
    $$

    **Number of terms for $|F_N| < 10^{-12}$:**

    $$
    Ce^{-cN} < 10^{-12} \implies 0.1\cdot e^{-0.2519 N} < 10^{-12}
    $$

    $$
    e^{-0.2519 N} < 10^{-11} \implies -0.2519 N < -11\ln 10 \implies N > \frac{11 \times 2.3026}{0.2519} \approx 100.6
    $$

    Therefore $N = 101$ terms suffice to guarantee $|F_N| < 10^{-12}$. In practice, $N = 128$ (the next power of 2) is a safe and convenient choice.
