# Greeks via Finite Differences

When option prices come from Monte Carlo simulation or finite difference PDE solvers rather than closed-form Fourier inversion, the characteristic function is not directly available for analytic differentiation. In this setting, the most general approach to computing Greeks is **bump-and-revalue**: perturb an input parameter by a small amount $h$, reprice the option, and approximate the derivative using finite differences. The method applies universally---to any pricing engine, any payoff, any model---but introduces an inherent trade-off between the **truncation error** of the finite difference approximation (which shrinks with $h$) and the **numerical noise** from the pricing engine (which grows relative to the signal as $h$ shrinks).

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Apply central, forward, and backward difference formulas to compute Heston Greeks
    2. Analyze the trade-off between truncation error and Monte Carlo noise
    3. Select optimal bump sizes for each Heston parameter
    4. Compute cross-Greeks and second-order sensitivities

!!! tip "Prerequisites"
    This section complements [Greeks via CF differentiation](greeks_via_cf_differentiation.md) and applies to the [Monte Carlo](../monte_carlo/quadratic_exponential_scheme.md) and [FDM](../fdm/adi_schemes.md) pricing engines.

---

## Finite Difference Formulas

### Forward Difference

The simplest approximation uses two function evaluations:

$$
\frac{\partial V}{\partial \theta_k} \approx \frac{V(\theta_k + h) - V(\theta_k)}{h}
$$

This has **first-order** truncation error $\mathcal{O}(h)$.

### Central Difference

The standard choice uses three evaluations:

$$
\frac{\partial V}{\partial \theta_k} \approx \frac{V(\theta_k + h) - V(\theta_k - h)}{2h}
$$

This has **second-order** truncation error $\mathcal{O}(h^2)$ and is preferred because the leading error term cancels by symmetry.

### Second Derivative (Gamma-Type)

For second-order Greeks:

$$
\frac{\partial^2 V}{\partial \theta_k^2} \approx \frac{V(\theta_k + h) - 2V(\theta_k) + V(\theta_k - h)}{h^2}
$$

This also has second-order truncation error $\mathcal{O}(h^2)$, but the denominator $h^2$ amplifies noise.

### Cross-Derivative

For mixed second-order sensitivities:

$$
\frac{\partial^2 V}{\partial \theta_j \partial \theta_k} \approx \frac{V(\theta_j + h_j, \theta_k + h_k) - V(\theta_j + h_j, \theta_k - h_k) - V(\theta_j - h_j, \theta_k + h_k) + V(\theta_j - h_j, \theta_k - h_k)}{4 h_j h_k}
$$

This requires four repricing evaluations and has truncation error $\mathcal{O}(h_j^2 + h_k^2)$.

---

## Optimal Bump Size

### The Bias-Variance Trade-Off

For a central difference with pricing noise $\epsilon$ (standard error of the Monte Carlo estimator or rounding error of the PDE solver):

$$
\text{Total error} \approx \underbrace{\frac{V^{(3)} h^2}{6}}_{\text{truncation}} + \underbrace{\frac{\epsilon}{h}}_{\text{noise amplification}}
$$

Minimizing over $h$:

$$
h^* = \left(\frac{3\epsilon}{V^{(3)}}\right)^{1/3}
$$

For Monte Carlo with $M$ paths and variance $\sigma^2$, $\epsilon \sim \sigma / \sqrt{M}$, giving:

$$
h^* \propto M^{-1/6}
$$

!!! warning "Second Derivatives Are Noisier"
    For gamma-type second derivatives, the noise amplification is $\epsilon / h^2$, and the optimal bump is $h^* \propto \epsilon^{1/4} \propto M^{-1/8}$. This means gamma requires significantly more paths (or a larger bump) than delta for the same accuracy. With $M = 100{,}000$ paths, the optimal bump for gamma is roughly $5$--$10\times$ larger than for delta.

---

## Heston Greeks and Bump Conventions

The Heston model has seven parameters that give rise to distinct Greeks:

| Greek | Parameter | Bump Convention | Typical $h$ |
|-------|-----------|:---------------:|:-----------:|
| Delta ($\Delta$) | $S_0$ | Absolute: $S_0 \pm h$ | $\$0.01$--$\$1.00$ |
| Gamma ($\Gamma$) | $S_0$ | Absolute: $S_0 \pm h$ | $\$0.50$--$\$2.00$ |
| Vega ($\mathcal{V}$) | $v_0$ | Absolute: $v_0 \pm h$ | $0.0001$--$0.001$ |
| Theta ($\Theta$) | $T$ | Absolute: $T - h$ | $1/365$ |
| Rho ($\varrho$) | $r$ | Absolute: $r \pm h$ | $0.0001$ |
| Vol-of-vol sens. | $\xi$ | Relative: $\xi(1 \pm h)$ | $1\%$--$5\%$ |
| Correlation sens. | $\rho$ | Absolute: $\rho \pm h$ | $0.01$--$0.05$ |

### Delta and Gamma

Delta and gamma in the Heston context are defined identically to Black-Scholes:

$$
\Delta = \frac{V(S_0 + h) - V(S_0 - h)}{2h}
$$

$$
\Gamma = \frac{V(S_0 + h) - 2V(S_0) + V(S_0 - h)}{h^2}
$$

When using Monte Carlo, ensure that **the same random number seeds** are used for all three evaluations. This is critical: without common random numbers, the noise in each evaluation is independent, and the difference quotient is dominated by noise.

### Vega

In Heston, vega is the sensitivity to the initial variance $v_0$:

$$
\mathcal{V} = \frac{V(v_0 + h) - V(v_0 - h)}{2h}
$$

A bump of $h = 0.001$ (i.e., moving $v_0$ from 0.04 to 0.041 and 0.039) is typical. The bump should be small enough that the CIR dynamics change negligibly but large enough to produce a measurable price difference.

### Parameter Sensitivities

For calibration and risk management, sensitivities to $\kappa$, $\theta$, $\xi$, $\rho$ are needed. These are computed by bumping each parameter and repricing:

$$
\frac{\partial V}{\partial \xi} \approx \frac{V(\xi + h) - V(\xi - h)}{2h}
$$

!!! note "Relative vs Absolute Bumps"
    For parameters that are strictly positive (like $\xi$), relative bumps ($\xi \to \xi(1 \pm \epsilon)$) prevent the bumped parameter from becoming negative. For parameters with a finite range (like $\rho \in [-1, 1]$), absolute bumps must be chosen to keep the bumped value within the valid range.

---

## Common Random Numbers

When computing Greeks via Monte Carlo finite differences, **common random numbers (CRN)** are essential. The idea is to use the identical sequence of random draws for the base case and all bumped cases.

Without CRN:

$$
\text{Var}\!\left(\frac{\hat{V}(S_0 + h) - \hat{V}(S_0 - h)}{2h}\right) = \frac{\text{Var}(\hat{V}(S_0+h)) + \text{Var}(\hat{V}(S_0-h))}{4h^2} \approx \frac{\sigma^2}{2Mh^2}
$$

With CRN:

$$
\text{Var}\!\left(\frac{\hat{V}(S_0 + h) - \hat{V}(S_0 - h)}{2h}\right) = \frac{\text{Var}(\hat{V}(S_0+h) - \hat{V}(S_0-h))}{4h^2} \approx \frac{(1 - \rho_{\text{CRN}})\sigma^2}{2Mh^2}
$$

When $\rho_{\text{CRN}} \approx 1$ (which it is for small bumps), the variance reduction from CRN is enormous---often by a factor of $10^3$ or more.

---

## FDM Grid Greeks

When the option price comes from a PDE solver on a $(x, v)$ grid, Greeks are available directly from the grid without repricing:

- **Delta**: $\Delta = e^{-x_0} \partial V / \partial x$ evaluated at the grid point closest to $(x_0, v_0)$ using the finite difference stencil already in place
- **Gamma**: $\Gamma = e^{-2x_0}(\partial^2 V / \partial x^2 - \partial V / \partial x)$ from the grid second derivative
- **Vega**: $\mathcal{V} = \partial V / \partial v$ from the $v$-direction stencil

These "grid Greeks" are free (no additional PDE solves) and have the same accuracy as the price. For parameter sensitivities ($\xi$, $\rho$, etc.), a full reprice is needed since these enter the PDE coefficients.

---

## Worked Example

Consider a European call under Heston with $S_0 = \$100$, $K = \$100$, $T = 1$, $r = 0.05$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$.

??? example "Bump Size Sensitivity for Delta (Monte Carlo, 100,000 QE paths)"
    | Bump $h$ | $\hat{\Delta}$ (no CRN) | Std Error | $\hat{\Delta}$ (CRN) | Std Error |
    |----------|:-----------------------:|:---------:|:---------------------:|:---------:|
    | $\$0.01$ | $0.58$ | $0.42$ | $0.617$ | $0.003$ |
    | $\$0.10$ | $0.61$ | $0.045$ | $0.617$ | $0.0003$ |
    | $\$1.00$ | $0.615$ | $0.005$ | $0.617$ | $0.0001$ |
    | $\$5.00$ | $0.612$ | $0.001$ | $0.613$ | $0.0001$ |

    Without CRN, small bumps are useless (noise dominates). With CRN, even $h = \$0.10$ gives 4-digit accuracy. The optimal bump with CRN is around $h = \$0.50$--$\$1.00$, where truncation error and MC noise are balanced.

??? example "Gamma with Varying Path Count"
    Using CRN and $h = \$1.00$:

    | Paths $M$ | $\hat{\Gamma}$ | Std Error | Relative Error |
    |-----------|:--------------:|:---------:|:--------------:|
    | 10,000 | $0.0191$ | $0.0012$ | 6.3% |
    | 100,000 | $0.0189$ | $0.0004$ | 2.1% |
    | 1,000,000 | $0.0189$ | $0.0001$ | 0.7% |

    Gamma requires roughly $10\times$ more paths than delta for the same relative accuracy due to the $h^2$ denominator.

---

## Summary

Finite difference Greeks via bump-and-revalue provide a universal method for computing sensitivities under the Heston model, applicable to any pricing engine (Monte Carlo, PDE, or numerical Fourier). The central difference formula with optimal bump size balances truncation error against pricing noise. Common random numbers are essential for Monte Carlo Greeks, reducing noise by orders of magnitude. Second-order Greeks (gamma, cross-sensitivities) require larger bumps or more paths due to the $h^2$ denominator. For Fourier-priced Europeans, [CF differentiation](greeks_via_cf_differentiation.md) is preferred; for path-dependent exotics or American options, finite differences remain the primary tool.

---

## Exercises

**Exercise 1.**
The central difference formula for delta is $\Delta \approx [C(S_0 + h) - C(S_0 - h)]/(2h)$ with truncation error $\mathcal{O}(h^2)$. If the pricing engine has noise of order $\epsilon$, the total error is approximately $h^2/6 \cdot |C'''| + \epsilon/h$. Minimize this with respect to $h$ to find the optimal bump size $h^* \propto \epsilon^{1/3}$. For a COS engine with $\epsilon \approx 10^{-10}$, compute $h^*$.

---

**Exercise 2.**
The gamma via central differences is $\Gamma \approx [C(S_0 + h) - 2C(S_0) + C(S_0 - h)]/h^2$. The noise amplification is $\epsilon/h^2$, worse than for delta ($\epsilon/h$). Compute the optimal bump size for gamma and compare with the delta optimal bump. Why must gamma bumps be larger?

---

**Exercise 3.**
A Monte Carlo engine with 100,000 paths has standard error \$0.03. Using central differences with $h = 1.0$ to compute delta, the noise in $\Delta$ is approximately $2 \times 0.03/(2 \times 1.0) = 0.03$. With common random numbers (same paths for both bumped prices), the noise drops to approximately $0.001$. Explain why common random numbers are so effective: the pricing noise cancels in the difference because both evaluations use the same random draws.

---

**Exercise 4.**
Compute the Heston vega via finite differences: $\mathcal{V} \approx [C(v_0 + h_v) - C(v_0 - h_v)]/(2h_v)$. For $v_0 = 0.04$ and a COS engine, suggest an appropriate bump size $h_v$. Compare the result with the CF-differentiation vega and discuss the accuracy trade-off.

---

**Exercise 5.**
Cross-Greeks like vanna ($\partial^2 C / \partial S_0 \partial v_0$) require a 2D finite difference stencil with four evaluations. Write the formula and estimate the noise amplification. For a Monte Carlo engine, how many paths are needed to achieve a vanna standard error of 0.001?

---

**Exercise 6.**
Design a validation test: compute delta, gamma, and vega using both CF differentiation and finite differences for a European call under Heston. The CF method serves as the reference. Vary the bump size $h$ logarithmically from $10^{-8}$ to $10^{-1}$ and plot the finite-difference error. Describe the expected V-shaped error curve and identify the optimal bump region.
