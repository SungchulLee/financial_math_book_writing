# Density Recovery Examples

Density recovery---reconstructing the probability density function from the characteristic function using the COS method---serves both as a validation tool and as a diagnostic for understanding the risk-neutral distributions implied by different financial models. This section presents detailed density recovery examples for the normal, log-normal, and Heston distributions, comparing the COS reconstruction against known densities and quantifying the accuracy as a function of the number of terms $N$.

!!! info "Prerequisites"

    - [COS Pricing Formula](cos_pricing_formula.md) (the COS framework)
    - [Error Analysis and Convergence](error_analysis_and_convergence.md) (convergence rates)
    - [From Characteristic Function to Density](characteristic_function_to_density.md) (inversion methods)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Implement density recovery using the COS method for standard distributions
    2. Quantify reconstruction accuracy as a function of $N$ and $[a, b]$
    3. Interpret features of the recovered Heston density (skew, kurtosis)
    4. Diagnose common artifacts in density reconstruction
    5. Use density recovery as a model validation and debugging tool

---

## The COS Density Reconstruction Formula

**Recall** (see [§ Cosine Coefficients via CF](cosine_coefficients_via_cf.md)): the COS reconstruction on $[a,b]$ is $\hat{f}_N(x) = \sum_{k=0}^{N-1}{}' F_k\cos(k\pi(x-a)/(b-a))$, requiring only $N$ characteristic function evaluations.

---

## Example 1: Standard Normal Density

The standard normal distribution is the simplest test case, with an analytic density and an elementary characteristic function.

!!! example "Normal Density Recovery"
    **Model:** $X \sim N(0, 1)$, $\phi(u) = e^{-u^2/2}$

    **Truncation:** $[a, b] = [-10, 10]$, so $b - a = 20$

    **Coefficients:**

    $$
    F_k = \frac{1}{10}\,\text{Re}\!\left[e^{-k^2\pi^2/800}\cdot e^{ik\pi/2}\right]
    $$

    **True density:** $f(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2}$

    **Accuracy at $x = 0$ (peak of density):**

    | $N$ | $\hat{f}_N(0)$ | True $f(0)$ | Absolute error |
    |---|---|---|---|
    | 16 | 0.398942 | 0.398942 | $< 10^{-6}$ |
    | 32 | 0.398942 | 0.398942 | $< 10^{-12}$ |
    | 64 | 0.398942 | 0.398942 | $< 10^{-15}$ |

    **Maximum error over $[-8, 8]$:**

    | $N$ | $\max_x |\hat{f}_N(x) - f(x)|$ |
    |---|---|
    | 16 | $\approx 10^{-5}$ |
    | 32 | $\approx 10^{-11}$ |
    | 64 | $< 10^{-15}$ |

    The super-exponential convergence reflects the entire analyticity of the Gaussian. With $N = 64$, the reconstruction is exact to machine precision over the region where the density is non-negligible.

---

## Example 2: Log-Normal Density

The log-normal density arises in the Black--Scholes model and provides a slightly more challenging test case due to its asymmetry.

!!! example "Log-Normal Density Recovery"
    **Model:** $X = \ln S_T$ where $S_T$ is log-normal with $\mu = \ln 100 + (0.05 - 0.04/2) \cdot 1 = \ln 100 + 0.03$ and $\sigma^2 = 0.04$ (corresponding to Black--Scholes with $S_0 = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$).

    **Characteristic function:** **Recall** (see [§ Fourier Transform Solution to the BS PDE](../../ch06/bs_pde_analytic_solution/fourier_transform.md)): $\phi(u) = \exp(i\mu u - \sigma^2 u^2 / 2)$.

    **Truncation:** $[a, b] = [\mu - 10\sigma, \mu + 10\sigma] = [4.635 - 2.0, 4.635 + 2.0] = [2.635, 6.635]$

    **Results:** With $N = 64$, the COS reconstruction matches the true log-normal density to $10^{-12}$ accuracy uniformly on $[3.0, 6.0]$.

    The recovered density is bell-shaped but slightly asymmetric (reflecting the log-normal skew), centered near $\mu \approx 4.635$ (corresponding to $S_T \approx 103$).

---

## Example 3: Heston Model Density

The Heston model is the primary application of COS density recovery, since its density has no closed-form expression.

!!! example "Heston Density Recovery"
    **Model parameters:** $S_0 = 100$, $r = 0.05$, $q = 0$, $T = 1$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\sigma_v = 0.3$, $\rho = -0.7$.

    **Characteristic function:** **Recall** (see [§ Heston Characteristic Function](../../ch16/heston_cf/closed_form_characteristic_function.md)): the Heston CF of $X_T = \ln S_T$ is given by the Riccati-based formula. The cumulants are:

    - $c_1 \approx 4.635$ (mean log-price)
    - $c_2 \approx 0.040$ (variance, similar to BS but with stochastic vol correction)
    - $c_3 < 0$ (negative skewness due to $\rho < 0$)
    - $c_4 > 0$ (excess kurtosis from stochastic volatility)

    **Truncation:** $[a, b]$ computed from cumulants with $L = 12$, giving approximately $[2.2, 7.0]$.

    **Qualitative features of the recovered density:**

    1. **Negative skew.** The left tail is heavier than the log-normal, reflecting the leverage effect ($\rho < 0$): when the stock drops, volatility rises, making further drops more likely.

    2. **Fat tails.** Both tails are heavier than the Gaussian, with the left tail especially prominent. This produces the volatility smile observed in option markets.

    3. **Peak slightly left of the BS peak.** The mode of the Heston density is slightly below the Black--Scholes mode, reflecting the negative drift correction from stochastic volatility.

    **Convergence:**

    | $N$ | $\max_x |\hat{f}_N(x) - f_{\text{ref}}(x)|$ |
    |---|---|
    | 32 | $\approx 10^{-3}$ |
    | 64 | $\approx 10^{-6}$ |
    | 128 | $\approx 10^{-10}$ |
    | 256 | $\approx 10^{-14}$ |

    The reference density $f_{\text{ref}}$ is computed by high-accuracy numerical Fourier inversion with $M = 10^4$ quadrature points. The COS reconstruction with $N = 128$ matches this reference to 10 digits.

---

## Example 4: Comparing Densities Across Models

Density recovery enables side-by-side comparison of risk-neutral distributions under different models, revealing how model choice affects pricing.

!!! example "BS vs Heston Density Comparison"
    With identical first two cumulants (same mean and variance of log-price), the Black--Scholes and Heston densities differ in their tails:

    | Feature | Black--Scholes | Heston ($\rho = -0.7$) |
    |---|---|---|
    | Skewness | 0 (symmetric) | Negative |
    | Excess kurtosis | 0 | Positive |
    | Left tail | Light (Gaussian) | Heavy |
    | Right tail | Light (Gaussian) | Moderately heavy |
    | OTM put prices | Lower | Higher |
    | Implied volatility | Flat | Skewed |

    The heavier left tail of the Heston density explains why out-of-the-money puts are more expensive under Heston than under Black--Scholes, producing the implied volatility skew observed in equity markets.

---

## Common Artifacts and Diagnostics

Density recovery can reveal implementation errors or parameter issues. The following artifacts are commonly encountered:

**Negative density values.** The cosine series is not guaranteed to produce non-negative values. Small negative values near the tails are truncation artifacts; large negative values indicate either insufficient $N$ or incorrect truncation.

!!! warning "Ringing at Boundaries"
    If the density is non-negligible at $x = a$ or $x = b$, the truncation creates an artificial discontinuity. The cosine series produces Gibbs-like oscillations near the boundary. The remedy is to widen the truncation interval.

**Aliasing.** If probability mass outside $[a, b]$ is significant, it folds back into the reconstruction, producing spurious features. Check by verifying that $\int_a^b \hat{f}_N(x)\,dx \approx 1$.

**Slow convergence.** If the error does not decrease exponentially with $N$, the density may have a non-smooth feature (kink, discontinuity) or the characteristic function may decay slowly along the real axis.

!!! tip "Diagnostic Checklist"

    1. Verify $\hat{f}_N(x) \geq 0$ for all evaluation points
    2. Verify $\int_a^b \hat{f}_N(x)\,dx \approx 1$ (e.g., using the trapezoidal rule)
    3. Compare $\hat{f}_{N}$ and $\hat{f}_{2N}$: the difference should decrease exponentially
    4. Check $\hat{f}_N(a)$ and $\hat{f}_N(b)$: should be near zero for proper truncation
    5. Compare against a known density (e.g., Black--Scholes) to validate the CF implementation

---

## Application: Model Validation

Density recovery is a powerful tool for model validation during implementation:

1. **CF implementation testing.** Recover the density and compare against a known result (e.g., Black--Scholes). Any discrepancy indicates a bug in the CF implementation.

2. **Parameter sensitivity.** Visualize how the density changes as parameters vary. For the Heston model, increasing $\rho$ from $-0.9$ to $0$ progressively reduces the skew, providing an intuitive check.

3. **Moment matching.** Compute moments from the recovered density (via numerical integration) and compare against the analytical moments from the CF derivatives. Discrepancies indicate truncation or series errors.

4. **Tail behavior.** Plot the density on a log scale to examine tail behavior. The Heston density should show heavier tails than the Gaussian, with the asymmetry controlled by $\rho$.

---

## Summary

Density recovery examples confirm the COS method's accuracy and provide diagnostic tools for implementation:

| Distribution | CF | $N$ for $10^{-8}$ accuracy | Key feature |
|---|---|---|---|
| Standard normal | $e^{-u^2/2}$ | $\approx 32$ | Super-exponential convergence |
| Log-normal | $e^{i\mu u - \sigma^2 u^2/2}$ | $\approx 32$ | Slight asymmetry |
| Heston | Riccati-based | $\approx 128$ | Negative skew, fat tails |
| Variance Gamma | Levy--Khintchine | $\approx 128$ | Peaked, heavy tails |

**Density recovery via the COS method serves as both a validation tool for characteristic function implementations and a diagnostic for understanding the risk-neutral distributions implied by different financial models, with the reconstructed density providing visual insight into features like skewness, kurtosis, and tail behavior that drive option prices.**

---

## Exercises

**Exercise 1.** For $X \sim N(0, 1)$ on $[-10, 10]$, the COS reconstruction achieves machine precision with $N = 64$. Compute the coefficients $F_0, F_2, F_4$ using $F_k = \frac{1}{10}\,\text{Re}[e^{-k^2\pi^2/800}\cdot e^{ik\pi/2}]$ and verify the values in the text. At what value of $k$ does $|F_k|$ first drop below $10^{-15}$?

??? success "Solution to Exercise 1"
    For $X \sim N(0,1)$ on $[a, b] = [-10, 10]$ with $b - a = 20$:

    $$
    F_k = \frac{1}{10}\,\text{Re}\!\left[e^{-k^2\pi^2/800}\cdot e^{ik\pi/2}\right]
    $$

    Since $e^{ik\pi/2} = i^k$, we have $\text{Re}[i^k] = \cos(k\pi/2)$, which cycles as $1, 0, -1, 0, 1, 0, -1, 0, \ldots$ for $k = 0, 1, 2, 3, \ldots$

    **$F_0$:** $F_0 = \frac{1}{10}\,\text{Re}[1\cdot 1] = 0.1$

    **$F_2$:** $F_2 = \frac{1}{10}\,\text{Re}[e^{-4\pi^2/800}\cdot(-1)] = -\frac{1}{10}e^{-\pi^2/200}$

    Since $\pi^2/200 \approx 0.04935$:

    $$
    F_2 = -0.1\times e^{-0.04935} \approx -0.1\times 0.9519 = -0.09519
    $$

    **$F_4$:** $F_4 = \frac{1}{10}\,\text{Re}[e^{-16\pi^2/800}\cdot 1] = \frac{1}{10}e^{-\pi^2/50}$

    Since $\pi^2/50 \approx 0.19739$:

    $$
    F_4 = 0.1\times e^{-0.19739} \approx 0.1\times 0.8209 = 0.08209
    $$

    These match the values used in the text.

    **Finding the first $k$ with $|F_k| < 10^{-15}$:** For even $k$, $|F_k| = \frac{1}{10}e^{-k^2\pi^2/800}$ (odd $k$ have $F_k = 0$). We need:

    $$
    \frac{1}{10}e^{-k^2\pi^2/800} < 10^{-15} \implies e^{-k^2\pi^2/800} < 10^{-14}
    $$

    $$
    k^2\pi^2/800 > 14\ln 10 \approx 32.24 \implies k^2 > 32.24\times 800/\pi^2 \approx 2614
    $$

    $$
    k > 51.1
    $$

    The first even $k$ satisfying this is $k = 52$. For $k = 52$: $|F_{52}| = 0.1\times e^{-52^2\pi^2/800} = 0.1\times e^{-33.40} \approx 0.1\times 3.3\times 10^{-15} = 3.3\times 10^{-16} < 10^{-15}$. So $|F_k|$ first drops below $10^{-15}$ at $k = 52$.

---

**Exercise 2.** For the log-normal density (Black-Scholes with $S_0 = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$), the truncation interval is approximately $[2.635, 6.635]$. Explain why this interval is not symmetric about $c_1 \approx 4.635$ in the original variable (it is symmetric in log-price). Compute $c_1 = (r - \sigma^2/2)T + \ln S_0$ and verify.

??? success "Solution to Exercise 2"
    The log-price is $X_T = \ln S_T$. Under Black--Scholes:

    $$
    c_1 = \mathbb{E}[\ln S_T] = \ln S_0 + (r - \sigma^2/2)T = \ln 100 + (0.05 - 0.02)\times 1 = \ln 100 + 0.03
    $$

    Since $\ln 100 \approx 4.6052$:

    $$
    c_1 \approx 4.6052 + 0.03 = 4.6352
    $$

    (The text rounds to $c_1 \approx 4.635$, which matches.)

    The truncation interval $[c_1 - 10\sigma\sqrt{T},\; c_1 + 10\sigma\sqrt{T}] = [4.635 - 2.0,\; 4.635 + 2.0] = [2.635, 6.635]$ is symmetric about $c_1$ in the log-price variable $x = \ln S_T$.

    However, this interval is **not** symmetric in the original stock price variable $S_T = e^x$. The interval $[2.635, 6.635]$ in log-price corresponds to $[e^{2.635}, e^{6.635}] = [13.94, 759.5]$ in stock price. The center in stock price space is $e^{c_1} = e^{4.635} \approx 103.0$, while the midpoint of the stock price interval is $(13.94 + 759.5)/2 \approx 386.7$. The asymmetry arises because the exponential map $x \mapsto e^x$ stretches the right half of the log-price interval much more than the left half. This is a fundamental property of log-normal distributions: symmetry in log-space produces positive skewness in level-space.

---

**Exercise 3.** The Heston density exhibits negative skew and excess kurtosis compared to the log-normal. If the Heston density has $c_3 < 0$ and $c_4 > 0$, explain how these cumulant values manifest in the shape of the density. Specifically, describe how the left tail, right tail, and peak of the Heston density differ from the log-normal density with the same $c_1$ and $c_2$.

??? success "Solution to Exercise 3"
    **Negative skewness ($c_3 < 0$):** This means the density has a longer left tail than right tail. In the recovered density:

    - The left tail extends farther from the mode and carries more mass than a symmetric (log-normal) density with the same $c_1$ and $c_2$
    - The mode is shifted slightly to the right of the mean
    - There is more probability of large downward moves than the log-normal predicts

    **Positive excess kurtosis ($c_4 > 0$):** This means the density has heavier tails than the Gaussian (or log-normal) on both sides and a sharper peak:

    - Both tails are heavier than the log-normal, meaning extreme moves (both up and down) are more likely
    - The center of the density is more peaked (more concentrated near the mode)
    - The "shoulders" of the density are thinner (probability is redistributed from the shoulders to the tails and peak)

    **Specific differences from the log-normal with the same $c_1$ and $c_2$:**

    - *Left tail:* The Heston density is significantly heavier in the left tail due to the combined effect of negative skewness and excess kurtosis. This is driven by the leverage effect ($\rho < 0$): when the stock drops, volatility increases, making further drops more likely and generating a feedback loop that fattens the left tail.
    - *Right tail:* The Heston density is moderately heavier than the log-normal in the right tail (from positive kurtosis), but less so than the left tail (since negative skew shifts mass leftward).
    - *Peak:* The Heston density peak is slightly to the left of the log-normal peak. The peak is also slightly higher because the excess kurtosis concentrates mass near the mode and in the tails at the expense of the shoulders.

---

**Exercise 4.** The diagnostic checklist includes verifying $\int_a^b\hat{f}_N(x)\,dx \approx 1$. Using the cosine expansion $\hat{f}_N(x) = \sum_{k=0}^{N-1}{}'F_k\cos(k\pi(x-a)/(b-a))$, show that $\int_a^b\hat{f}_N(x)\,dx = \frac{b-a}{2}F_0$. If $F_0 = A_0 = 2/(b-a)$ for a properly truncated density, verify that the integral equals 1.

??? success "Solution to Exercise 4"
    The COS reconstruction is $\hat{f}_N(x) = \sum_{k=0}^{N-1}{}' F_k\cos(k\pi(x-a)/(b-a))$. Integrating over $[a, b]$:

    $$
    \int_a^b \hat{f}_N(x)\,dx = \sum_{k=0}^{N-1}{}' F_k\int_a^b\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx
    $$

    For $k \geq 1$, the integral of $\cos(k\pi(x-a)/(b-a))$ over $[a, b]$ is:

    $$
    \int_a^b\cos\!\left(\frac{k\pi(x-a)}{b-a}\right)dx = \frac{b-a}{k\pi}\sin\!\left(\frac{k\pi(x-a)}{b-a}\right)\bigg|_a^b = \frac{b-a}{k\pi}[\sin(k\pi) - \sin(0)] = 0
    $$

    since $\sin(k\pi) = 0$ for integer $k$.

    For $k = 0$: $\int_a^b 1\,dx = b - a$.

    The prime notation means the $k = 0$ term is halved, so:

    $$
    \int_a^b\hat{f}_N(x)\,dx = \frac{1}{2}F_0\cdot(b-a) = \frac{b-a}{2}F_0
    $$

    **Verification:** For a properly truncated density, $A_0 = \frac{2}{b-a}\int_a^b f(x)\,dx \approx \frac{2}{b-a}$ (since $\int_a^b f(x)\,dx \approx 1$). Therefore $F_0 \approx A_0 \approx 2/(b-a)$, and:

    $$
    \int_a^b\hat{f}_N(x)\,dx = \frac{b-a}{2}\cdot\frac{2}{b-a} = 1
    $$

    This confirms the normalization.

---

**Exercise 5.** The COS density reconstruction can produce negative values near the boundaries when $N$ is too small. For $N = 8$ and a standard normal on $[-10, 10]$, explain why $\hat{f}_8(x)$ might be negative near $x = \pm 8$. How does increasing $N$ to 64 eliminate the negative values? What is the minimum $N$ for which $\hat{f}_N(x) \geq 0$ for all $x \in [-8, 8]$?

??? success "Solution to Exercise 5"
    For $N = 8$ and the standard normal on $[-10, 10]$, the reconstruction $\hat{f}_8(x) = \sum_{k=0}^{7}{}' F_k\cos(k\pi(x+10)/20)$ uses only 8 cosine terms. The true density at $x = 0$ is $f(0) \approx 0.3989$ and at $x = \pm 8$ is $f(\pm 8) \approx 5.05\times 10^{-16}$.

    **Why negative values can occur near $x = \pm 8$:** With only 8 terms, the cosine series can accurately reproduce the density's shape near its peak but cannot resolve the density at points far from the center. Near $x = \pm 8$, the true density is essentially zero ($\sim 10^{-16}$), but the truncated series has oscillations (ripples) whose amplitude is determined by the magnitude of the omitted coefficients. The maximum error of the 8-term approximation is $\sim 10^{-5}$ (from the convergence table), so the reconstruction at $x = 8$ could be anywhere in the range $[-10^{-5}, 10^{-5}]$---easily negative. These oscillations are the Gibbs-like phenomenon for truncated cosine series.

    **Why $N = 64$ eliminates negative values:** With $N = 64$, the reconstruction error drops below $10^{-15}$ everywhere on $[-8, 8]$. Since $f(x) > 0$ for all $x$ and $f(\pm 8) \approx 5\times 10^{-16}$, the reconstruction error ($< 10^{-15}$) is comparable to the density value itself at $x = \pm 8$. For all $x \in [-8, 8]$ with $f(x) \gg 10^{-15}$, the relative error is negligible and the reconstruction is positive. The super-exponential decay of the Gaussian cosine coefficients means the omitted terms contribute negligibly.

    **Minimum $N$:** The reconstruction is non-negative on $[-8, 8]$ when the maximum error is smaller than the minimum density value on that interval. Since $\min_{x\in[-8,8]}f(x) = f(\pm 8) \approx 5\times 10^{-16}$, we need $\varepsilon_{\max}(N) < 5\times 10^{-16}$. From the convergence table, $N = 32$ gives error $\approx 10^{-11}$, which is too large; $N = 64$ gives error $< 10^{-15}$, which suffices. The minimum $N$ for non-negativity on $[-8, 8]$ is approximately $N = 50$--$60$ (interpolating the super-exponential convergence).

---

**Exercise 6.** Use density recovery as a model validation tool: if you implement the Heston characteristic function and recover the density for $\sigma_v = 0$ (deterministic volatility), the result should match the Black-Scholes log-normal density. Explain what features of the recovered density would indicate a bug in the Heston CF implementation (e.g., wrong sign of skewness, incorrect peak location, density not integrating to 1).

---

??? success "Solution to Exercise 6"
    When $\sigma_v = 0$, the Heston model reduces to constant volatility $v(t) = v_0$ for all $t$. The log-price becomes:

    $$
    X_T = \ln S_0 + (r - v_0/2)T + \sqrt{v_0}\,W_T
    $$

    which is $N(\ln S_0 + (r - v_0/2)T,\; v_0 T)$---exactly the Black--Scholes log-normal density with $\sigma = \sqrt{v_0}$.

    **Bug indicators in the recovered density:**

    1. **Wrong sign of skewness.** If the recovered density shows positive skew (right tail heavier than left) when $\sigma_v = 0$, this indicates a sign error in the $\rho$ or drift terms of the CF implementation. With $\sigma_v = 0$, the density should be perfectly symmetric (in log-price) regardless of $\rho$, since $\rho$ only matters when $\sigma_v > 0$.

    2. **Incorrect peak location.** The mode of the recovered density should be at $\ln S_0 + (r - v_0/2)T - v_0 T = \ln S_0 + (r - 3v_0/2)T$... Actually, for the normal density the mode equals the mean: $\ln S_0 + (r - v_0/2)T$. If the peak is shifted, this suggests an error in the drift computation (e.g., missing the $-v_0/2$ convexity correction, or incorrect signs in the $C(u, T)$ function).

    3. **Density not integrating to 1.** If $\int_a^b\hat{f}_N(x)\,dx$ deviates significantly from 1 (detected by checking $F_0(b-a)/2$), this indicates the CF does not satisfy $\phi(0) = 1$, which would be a normalization bug.

    4. **Excess kurtosis or fat tails.** With $\sigma_v = 0$, the density should match the Gaussian exactly---no fat tails, no excess kurtosis. If the recovered density shows heavier tails than the known Gaussian, this suggests the $D(u, T)$ function in the Heston CF does not correctly reduce to zero when $\sigma_v = 0$ (since $D$ should vanish, leaving only the deterministic-volatility terms in $C$).

    5. **Dependence on $\rho$ or $\kappa$ or $\theta$.** Varying $\rho$, $\kappa$, or $\theta$ while keeping $\sigma_v = 0$ should not change the density (since all stochastic volatility effects vanish). If the density shifts or changes shape, the implementation incorrectly retains stochastic volatility terms when $\sigma_v = 0$.
