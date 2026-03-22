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

The COS method recovers the density $f(x)$ on $[a, b]$ using the formula

$$
\hat{f}_N(x) = \sum_{k=0}^{N-1}{}' F_k \cos\!\left(\frac{k\pi(x-a)}{b-a}\right)
$$

where

$$
F_k = \frac{2}{b-a}\,\text{Re}\!\left[\phi\!\left(\frac{k\pi}{b-a}\right)e^{-ik\pi a/(b-a)}\right]
$$

This formula requires only $N$ evaluations of the characteristic function $\phi$. The reconstruction is evaluated at any desired set of points $\{x_j\}$ using the precomputed coefficients.

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

    **Characteristic function:** $\phi(u) = \exp(i\mu u - \sigma^2 u^2 / 2)$

    **Truncation:** $[a, b] = [\mu - 10\sigma, \mu + 10\sigma] = [4.635 - 2.0, 4.635 + 2.0] = [2.635, 6.635]$

    **Results:** With $N = 64$, the COS reconstruction matches the true log-normal density to $10^{-12}$ accuracy uniformly on $[3.0, 6.0]$.

    The recovered density is bell-shaped but slightly asymmetric (reflecting the log-normal skew), centered near $\mu \approx 4.635$ (corresponding to $S_T \approx 103$).

---

## Example 3: Heston Model Density

The Heston model is the primary application of COS density recovery, since its density has no closed-form expression.

!!! example "Heston Density Recovery"
    **Model parameters:** $S_0 = 100$, $r = 0.05$, $q = 0$, $T = 1$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\sigma_v = 0.3$, $\rho = -0.7$.

    **Characteristic function:** The Heston CF of the log-price $X_T = \ln S_T$ is given by the Riccati-based formula. The cumulants are:

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
