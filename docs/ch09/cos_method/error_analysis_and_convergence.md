# Error Analysis and Convergence

Understanding the error structure of the COS method is essential for choosing parameters ($N$, $[a,b]$, $L$) that achieve a target accuracy with minimal computation. The total error decomposes into two independent components: the truncation error from restricting the density to a finite interval, and the series truncation error from using finitely many cosine terms. This section derives rigorous bounds for each component, establishes the exponential convergence rate for smooth densities, and explains why the COS method achieves machine precision with remarkably few terms for standard financial models.

!!! info "Prerequisites"
    - [COS Pricing Formula](cos_pricing_formula.md) (the formula whose error we analyze)
    - [Truncation to Finite Domain](truncation_to_finite_domain.md) (domain truncation)
    - [Convergence of Fourier Series](../fourier_series/convergence_of_fourier_series.md) (coefficient decay rates)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Decompose the total COS error into truncation and series components
    2. Bound each error component in terms of model parameters
    3. Determine the convergence rate for a given model
    4. Choose $N$ and $[a, b]$ to achieve a prescribed accuracy
    5. Explain why exponential convergence holds for affine models with smooth densities

---

## Error Decomposition

The COS pricing formula approximates the true option value $V$ by

$$
V_{\text{COS}} = e^{-rT}\sum_{k=0}^{N-1}{}' F_k\, V_k
$$

The total error $|V - V_{\text{COS}}|$ arises from two sources that we analyze separately.

!!! note "Theorem: Error Decomposition"
    The total COS error satisfies

    $$
    |V - V_{\text{COS}}| \leq \underbrace{|V - V_{[a,b]}|}_{\text{truncation error } \varepsilon_1} + \underbrace{|V_{[a,b]} - V_{\text{COS}}|}_{\text{series truncation error } \varepsilon_2}
    $$

    where $V_{[a,b]} = e^{-rT}\int_a^b \Phi(x)f(x)\,dx$ is the option value with the density restricted to $[a, b]$.

This decomposition follows from the triangle inequality. The two errors are independent: $\varepsilon_1$ depends only on the choice of $[a, b]$, while $\varepsilon_2$ depends on $N$ and the smoothness of $f$.

---

## Truncation Error Analysis

The truncation error arises from the probability mass and payoff contribution outside $[a, b]$.

!!! note "Theorem: Truncation Error Bound"
    For a European call with payoff $\Phi(x) = K(e^x - 1)^+$:

    $$
    \varepsilon_1 = e^{-rT}\left|\int_{\mathbb{R}\setminus[a,b]} \Phi(x)f(x)\,dx\right| \leq e^{-rT}K\left[\mathbb{E}[e^{X}\mathbf{1}_{X \notin [a,b]}] + P(X \notin [a,b])\right]
    $$

    If $X$ has mean $c_1$, variance $c_2$, and the truncation interval is $[c_1 - L\sqrt{c_2}, c_1 + L\sqrt{c_2}]$, then for distributions with sub-Gaussian tails:

    $$
    \varepsilon_1 \leq C\, e^{-\alpha L^2}
    $$

    for constants $C, \alpha > 0$ depending on the model parameters.

For the cumulant-based truncation with $L = 10$:

| Model | $\varepsilon_1$ (approximate) |
|---|---|
| Black--Scholes | $< 10^{-20}$ |
| Heston (typical) | $< 10^{-15}$ |
| Variance Gamma | $< 10^{-10}$ |

The truncation error is negligible for all standard models with $L \geq 10$.

---

## Series Truncation Error Analysis

The series truncation error arises from using $N$ cosine terms instead of infinitely many. This is the dominant error component and the one that determines the convergence rate.

!!! note "Theorem: Series Truncation Error"
    Assume $f$ is supported on $[a, b]$ (truncation error already handled). The series truncation error is

    $$
    \varepsilon_2 = e^{-rT}\left|\sum_{k=N}^{\infty}{}' A_k\, V_k\right|
    $$

    This satisfies the bound

    $$
    \varepsilon_2 \leq e^{-rT}\left(\sum_{k=N}^{\infty} A_k^2\right)^{1/2}\left(\sum_{k=N}^{\infty} V_k^2\right)^{1/2}
    $$

    by the Cauchy--Schwarz inequality.

The bound involves the tail sums of two coefficient sequences:

- $\{A_k\}$: the density coefficients, whose decay rate depends on the smoothness of $f$
- $\{V_k\}$: the payoff coefficients, whose decay depends on the smoothness of $\Phi$

---

## Convergence Rate for Smooth Densities

The convergence rate of the COS method is determined by the slower-decaying of the two coefficient sequences. Since payoff functions (calls, puts) have a kink at the strike, the payoff coefficients decay as $O(1/k^2)$. However, this does not limit the COS method because the density coefficients $A_k$ typically decay much faster.

!!! note "Theorem: Exponential Convergence for Analytic Densities"
    If the density $f$ extends to an analytic function in a strip $|\text{Im}(z)| < \beta$ around the real axis, then the cosine coefficients decay exponentially:

    $$
    |A_k| \leq C\, e^{-\beta k\pi/(b-a)}
    $$

    and the series truncation error satisfies

    $$
    \varepsilon_2 \leq C'\, e^{-\beta N\pi/(b-a)}
    $$

    for constants $C, C'$ depending on $f$ and $\Phi$.

**Proof sketch.** The cosine coefficient $A_k$ can be written as a contour integral in the complex plane. Shifting the contour by $\pm i\beta$ (into the strip of analyticity) introduces a factor of $e^{-\beta k\pi/(b-a)}$ from the exponential term, while the integral along the shifted contour is bounded by the supremum of $|f|$ on the shifted contour. $\square$

The exponential convergence rate $\beta\pi/(b-a)$ depends on the ratio of the analyticity strip width $\beta$ to the interval length $b-a$. This explains why narrower truncation intervals (when justified by negligible truncation error) give faster convergence.

---

## Convergence Rates for Standard Models

Different financial models have different analyticity properties, leading to different convergence rates:

| Model | Density analyticity | Coefficient decay | $N$ for 8-digit accuracy |
|---|---|---|---|
| Black--Scholes (log-normal) | Entire ($\beta = \infty$) | $O(e^{-ck^2})$ (super-exponential) | $\approx 32$ |
| Heston | Strip of finite width | $O(e^{-ck})$ (exponential) | $\approx 64$--$128$ |
| Variance Gamma | Strip of finite width | $O(e^{-ck})$ (exponential) | $\approx 128$ |
| CGMY ($Y < 1$) | Strip of finite width | $O(e^{-ck})$ (exponential) | $\approx 128$--$256$ |
| CGMY ($Y \geq 1$) | No strip / reduced width | $O(1/k^p)$ (algebraic) | $\approx 10^3$ or more |

!!! warning "Algebraic Convergence"
    When the density is not analytic (e.g., models with jumps that produce density kinks), the COS method converges only algebraically: $\varepsilon_2 = O(1/N^p)$ for some power $p$. In such cases, many more terms are needed, and alternative methods (FFT, numerical integration) may be competitive.

---

## Interaction Between Truncation and Series Error

The two error components interact through the interval length $b - a$:

- **Wider $[a, b]$** (larger $L$): reduces truncation error $\varepsilon_1$ but increases $b - a$, which slows the exponential convergence rate $e^{-\beta N\pi/(b-a)}$ and requires larger $N$.

- **Narrower $[a, b]$** (smaller $L$): improves convergence rate but risks significant truncation error.

The optimal balance is achieved when both errors are comparable. For the standard cumulant-based truncation with $L = 10$, the truncation error is $O(10^{-20})$ or smaller, while the series error with $N = 64$ is typically $O(10^{-8})$ to $O(10^{-12})$. Since the truncation error is always negligible, the series error dominates and $N$ is the primary tuning parameter.

---

## Practical Error Estimation

In implementations, the convergence can be monitored empirically:

!!! tip "Convergence Diagnostics"
    1. **Richardson extrapolation.** Compute $V_N$ and $V_{2N}$. If $|V_{2N} - V_N| < \varepsilon$, then $V_{2N}$ is accurate to approximately $\varepsilon$.

    2. **Coefficient magnitude.** If $|F_k V_k| < \varepsilon$ for $k \geq N_0$, then the remaining terms contribute less than $(N - N_0)\varepsilon$ to the sum.

    3. **Double the interval test.** Recompute with $[a', b'] = [2a, 2b]$. If the price changes by less than $\varepsilon$, the truncation is adequate.

---

## Example: Error Convergence Under Black--Scholes

To illustrate the convergence behavior, we examine the error as a function of $N$ for the Black--Scholes model.

!!! example "Convergence Study: Black--Scholes Call"
    Parameters: $S_0 = 100$, $K = 100$, $r = 0.10$, $\sigma = 0.25$, $T = 0.1$, $[a,b] = [-1, 1]$.

    | $N$ | COS price | $|V_{\text{COS}} - V_{\text{BS}}|$ | Convergence rate |
    |---|---|---|---|
    | 8 | 3.6614 | $2.1 \times 10^{-3}$ | --- |
    | 16 | 3.6593 | $3.5 \times 10^{-6}$ | super-exponential |
    | 32 | 3.6593 | $1.2 \times 10^{-11}$ | super-exponential |
    | 64 | 3.6593 | $< 10^{-15}$ | machine precision |

    The error decreases faster than any exponential, consistent with the super-exponential coefficient decay of the Gaussian density. The convergence is so rapid that $N = 32$ already provides 11-digit accuracy.

---

## Example: Error Convergence Under Heston

The Heston model provides the benchmark for exponential (but not super-exponential) convergence.

!!! example "Convergence Study: Heston Call"
    Parameters: $S_0 = 100$, $K = 100$, $r = 0$, $T = 1$, typical Heston parameters.

    | $N$ | $|V_{\text{COS}} - V_{\text{ref}}|$ | Convergence rate |
    |---|---|---|
    | 16 | $\approx 10^{-2}$ | --- |
    | 32 | $\approx 10^{-4}$ | exponential |
    | 64 | $\approx 10^{-7}$ | exponential |
    | 128 | $\approx 10^{-11}$ | exponential |
    | 256 | $\approx 10^{-15}$ | machine precision |

    Each doubling of $N$ adds approximately 3--4 digits of accuracy, consistent with exponential convergence $\varepsilon_2 \sim e^{-cN}$.

---

## Summary

The COS method's error structure is clean and well-understood:

| Error component | Source | Bound | Typical magnitude |
|---|---|---|---|
| Truncation error $\varepsilon_1$ | Restricting density to $[a, b]$ | $O(e^{-\alpha L^2})$ | $< 10^{-15}$ with $L = 10$ |
| Series error $\varepsilon_2$ | Using $N$ cosine terms | $O(e^{-\beta N\pi/(b-a)})$ for analytic $f$ | Dominant; tuned via $N$ |
| Total error | $\varepsilon_1 + \varepsilon_2$ | Dominated by $\varepsilon_2$ | Target via choice of $N$ |

**For models with analytic characteristic functions and smooth densities, the COS method achieves exponential convergence in $N$, with the convergence rate determined by the width of the analyticity strip of the density relative to the truncation interval length.**
