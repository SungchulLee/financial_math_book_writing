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

??? success "Solution to Exercise 1"
    The total error for the central difference approximation of delta is:

    $$
    E(h) = \underbrace{\frac{h^2}{6}\left|C'''(S_0)\right|}_{\text{truncation error}} + \underbrace{\frac{\epsilon}{h}}_{\text{noise amplification}}
    $$

    To find the optimal $h^*$, differentiate with respect to $h$ and set equal to zero:

    $$
    \frac{dE}{dh} = \frac{h}{3}\left|C'''\right| - \frac{\epsilon}{h^2} = 0
    $$

    Solving:

    $$
    \frac{h^3}{3}\left|C'''\right| = \epsilon \quad \implies \quad h^* = \left(\frac{3\epsilon}{|C'''|}\right)^{1/3}
    $$

    This confirms $h^* \propto \epsilon^{1/3}$.

    **COS engine with $\epsilon \approx 10^{-10}$.** We need an estimate of $|C'''(S_0)|$. For a typical European call under Heston, the third derivative of the price with respect to $S_0$ (related to the "speed" Greek) is of order $|C'''| \sim 10^{-3}$ to $10^{-4}$ for ATM options. Taking $|C'''| \approx 5 \times 10^{-4}$ as a representative value:

    $$
    h^* = \left(\frac{3 \times 10^{-10}}{5 \times 10^{-4}}\right)^{1/3} = \left(6 \times 10^{-7}\right)^{1/3} \approx 8.4 \times 10^{-3}
    $$

    So the optimal bump for a COS engine is approximately $h^* \approx 0.01$ (about 1 cent for a \$100 stock). At this optimal bump, the total error is:

    $$
    E(h^*) \approx \frac{(h^*)^2}{6}|C'''| + \frac{\epsilon}{h^*} \approx \frac{(8.4 \times 10^{-3})^2 \times 5 \times 10^{-4}}{6} + \frac{10^{-10}}{8.4 \times 10^{-3}} \approx 6 \times 10^{-9} + 1.2 \times 10^{-8} \approx 2 \times 10^{-8}
    $$

    This is about 8 digits of accuracy for delta, which is more than adequate for practical purposes but substantially less than the 10--12 digit accuracy achievable via CF differentiation.

---

**Exercise 2.**
The gamma via central differences is $\Gamma \approx [C(S_0 + h) - 2C(S_0) + C(S_0 - h)]/h^2$. The noise amplification is $\epsilon/h^2$, worse than for delta ($\epsilon/h$). Compute the optimal bump size for gamma and compare with the delta optimal bump. Why must gamma bumps be larger?

??? success "Solution to Exercise 2"
    For the gamma approximation $\Gamma \approx [C(S_0 + h) - 2C(S_0) + C(S_0 - h)] / h^2$, the total error is:

    $$
    E_\Gamma(h) = \frac{h^2}{12}\left|C^{(4)}(S_0)\right| + \frac{2\epsilon}{h^2}
    $$

    The truncation error comes from the Taylor expansion (the leading error term for the second-derivative central difference involves $C^{(4)}$), while the noise amplification has $\epsilon/h^2$ scaling because three noisy evaluations are combined and divided by $h^2$.

    Setting $dE_\Gamma / dh = 0$:

    $$
    \frac{h}{6}|C^{(4)}| - \frac{4\epsilon}{h^3} = 0 \quad \implies \quad h^4 = \frac{24\epsilon}{|C^{(4)}|} \quad \implies \quad h^*_\Gamma = \left(\frac{24\epsilon}{|C^{(4)}|}\right)^{1/4}
    $$

    So $h^*_\Gamma \propto \epsilon^{1/4}$, compared to $h^*_\Delta \propto \epsilon^{1/3}$ for delta.

    **Comparison.** For the same noise level $\epsilon$:

    $$
    \frac{h^*_\Gamma}{h^*_\Delta} \propto \frac{\epsilon^{1/4}}{\epsilon^{1/3}} = \epsilon^{-1/12}
    $$

    Since $\epsilon < 1$, we have $\epsilon^{-1/12} > 1$, meaning **the gamma bump must be larger than the delta bump**. For a Monte Carlo engine with $\epsilon \sim 10^{-2}$ (100,000 paths):

    $$
    h^*_\Delta \propto (10^{-2})^{1/3} \approx 0.22, \qquad h^*_\Gamma \propto (10^{-2})^{1/4} \approx 0.32
    $$

    The gamma bump is about 50% larger. For a COS engine with $\epsilon \sim 10^{-10}$:

    $$
    h^*_\Delta \propto (10^{-10})^{1/3} \approx 2 \times 10^{-4}, \qquad h^*_\Gamma \propto (10^{-10})^{1/4} \approx 3 \times 10^{-3}
    $$

    The gamma bump is about 15 times larger. The gamma bump must be larger because the $h^2$ denominator amplifies noise more aggressively, so one must use a larger $h$ to keep the noise contribution manageable. The trade-off is accepting more truncation error to reduce the much worse noise amplification.

---

**Exercise 3.**
A Monte Carlo engine with 100,000 paths has standard error \$0.03. Using central differences with $h = 1.0$ to compute delta, the noise in $\Delta$ is approximately $2 \times 0.03/(2 \times 1.0) = 0.03$. With common random numbers (same paths for both bumped prices), the noise drops to approximately $0.001$. Explain why common random numbers are so effective: the pricing noise cancels in the difference because both evaluations use the same random draws.

??? success "Solution to Exercise 3"
    **Without common random numbers (CRN).** Let $\hat{V}^+$ and $\hat{V}^-$ denote the Monte Carlo price estimates at $S_0 + h$ and $S_0 - h$ respectively. These are independent random variables (different random draws), each with variance $\sigma^2_{\text{MC}} / M$ where $\sigma^2_{\text{MC}}$ is the single-path variance and $M$ is the number of paths. The finite difference delta estimator is:

    $$
    \hat{\Delta} = \frac{\hat{V}^+ - \hat{V}^-}{2h}
    $$

    Since $\hat{V}^+$ and $\hat{V}^-$ are independent:

    $$
    \operatorname{Var}(\hat{\Delta}) = \frac{\operatorname{Var}(\hat{V}^+) + \operatorname{Var}(\hat{V}^-)}{4h^2} = \frac{2\sigma^2_{\text{MC}}}{4Mh^2} = \frac{\sigma^2_{\text{MC}}}{2Mh^2}
    $$

    For the given numbers: $\sigma_{\text{MC}} / \sqrt{M} \approx \$0.03$, so $\sigma^2_{\text{MC}} / M \approx 9 \times 10^{-4}$. With $h = 1.0$:

    $$
    \operatorname{Std}(\hat{\Delta}) \approx \frac{\sqrt{2} \times 0.03}{2 \times 1.0} \approx 0.021
    $$

    **With CRN.** The same random number sequence $\omega_1, \ldots, \omega_M$ is used for both $\hat{V}^+$ and $\hat{V}^-$. Now the estimator is:

    $$
    \hat{\Delta} = \frac{1}{2hM}\sum_{i=1}^{M}\bigl[V^+(\omega_i) - V^-(\omega_i)\bigr]
    $$

    For a small bump $h$, the payoff at $S_0 + h$ and $S_0 - h$ using the same path $\omega_i$ produces nearly identical intermediate values (stock paths, variance paths) that differ only slightly due to the initial condition shift. The difference $V^+(\omega_i) - V^-(\omega_i)$ is approximately:

    $$
    V^+(\omega_i) - V^-(\omega_i) \approx 2h \cdot \frac{\partial V}{\partial S_0}(\omega_i) + \mathcal{O}(h^3)
    $$

    The variance of this difference is:

    $$
    \operatorname{Var}\bigl(V^+(\omega_i) - V^-(\omega_i)\bigr) = \operatorname{Var}(V^+) + \operatorname{Var}(V^-) - 2\operatorname{Cov}(V^+, V^-)
    $$

    Since the same random draws are used, $\operatorname{Corr}(V^+, V^-) \to 1$ as $h \to 0$. The variance of the difference is proportional to $h^2$ times the variance of the pathwise derivative, which is typically much smaller than $\sigma^2_{\text{MC}}$. The noise in the delta estimate becomes:

    $$
    \operatorname{Std}(\hat{\Delta}_{\text{CRN}}) \approx \frac{\operatorname{Std}(V^+ - V^-)}{2h\sqrt{M}} \propto \frac{h \cdot \sigma_{\partial V/\partial S}}{2h\sqrt{M}} = \frac{\sigma_{\partial V/\partial S}}{2\sqrt{M}}
    $$

    This is **independent of $h$** (for small $h$) and much smaller than the no-CRN noise. The cancellation occurs because the bulk of the Monte Carlo noise (which is common to both $V^+$ and $V^-$ since they share the same random draws) subtracts out in the difference, leaving only the signal (the sensitivity to the parameter change).

    In the given example, the noise drops from $\approx 0.03$ to $\approx 0.001$, a factor of 30 reduction, corresponding to a correlation $\rho_{\text{CRN}} \approx 1 - (0.001/0.03)^2 \approx 0.999$.

---

**Exercise 4.**
Compute the Heston vega via finite differences: $\mathcal{V} \approx [C(v_0 + h_v) - C(v_0 - h_v)]/(2h_v)$. For $v_0 = 0.04$ and a COS engine, suggest an appropriate bump size $h_v$. Compare the result with the CF-differentiation vega and discuss the accuracy trade-off.

??? success "Solution to Exercise 4"
    The Heston vega via finite differences is:

    $$
    \mathcal{V} \approx \frac{C(v_0 + h_v) - C(v_0 - h_v)}{2h_v}
    $$

    **Choosing $h_v$ for a COS engine.** The COS method typically achieves pricing accuracy of $\epsilon \approx 10^{-10}$ to $10^{-12}$. Using the optimal bump formula $h^* = (3\epsilon / |V'''_{v_0}|)^{1/3}$, we need an estimate of the third derivative of $V$ with respect to $v_0$.

    For a typical ATM call with $v_0 = 0.04$, the vega is $\mathcal{V} \approx 21.4$ and the volga (second derivative) is $\mathcal{G} = \partial^2 V / \partial v_0^2 \approx 60$--$100$. The third derivative is harder to estimate but is typically $|V'''_{v_0}| \sim 10^3$ to $10^4$. Taking $|V'''_{v_0}| \approx 5000$:

    $$
    h^*_v = \left(\frac{3 \times 10^{-10}}{5000}\right)^{1/3} = \left(6 \times 10^{-14}\right)^{1/3} \approx 4 \times 10^{-5}
    $$

    A practical choice is $h_v = 10^{-4}$ to $10^{-3}$. For $v_0 = 0.04$, this corresponds to bumping from $0.0399$ to $0.0401$ (for $h_v = 10^{-4}$) or from $0.039$ to $0.041$ (for $h_v = 10^{-3}$).

    **Comparison with CF differentiation.** The CF-differentiation vega is computed via:

    $$
    \mathcal{V}_{\text{CF}} = S_0 e^{-qT}\frac{\partial P_1}{\partial v_0} - Ke^{-rT}\frac{\partial P_2}{\partial v_0}
    $$

    with $\partial P_j / \partial v_0$ involving $D(u, \tau)\,\varphi(u)$ in a single integration pass. This is exact up to quadrature error ($\sim 10^{-12}$ with 128-point Gauss-Kronrod).

    The finite difference result agrees with the CF result to within the total error $E(h^*) \approx 2 \times 10^{-8}$. The accuracy trade-off:

    - **CF differentiation**: $\sim 10^{-12}$ accuracy, one integration pass, no bump-size tuning
    - **Finite differences with COS**: $\sim 10^{-8}$ accuracy at best, two repricing evaluations, requires bump-size optimization

    CF differentiation is clearly superior when available. Finite differences are the fallback for pricing engines (Monte Carlo, American PDE solvers) where the characteristic function is not accessible.

---

**Exercise 5.**
Cross-Greeks like vanna ($\partial^2 C / \partial S_0 \partial v_0$) require a 2D finite difference stencil with four evaluations. Write the formula and estimate the noise amplification. For a Monte Carlo engine, how many paths are needed to achieve a vanna standard error of 0.001?

??? success "Solution to Exercise 5"
    **Vanna formula.** The cross-Greek vanna is $\partial^2 C / \partial S_0 \, \partial v_0$. Using a 2D central difference stencil:

    $$
    \text{Vanna} \approx \frac{C(S_0 + h_S,\, v_0 + h_v) - C(S_0 + h_S,\, v_0 - h_v) - C(S_0 - h_S,\, v_0 + h_v) + C(S_0 - h_S,\, v_0 - h_v)}{4\,h_S\,h_v}
    $$

    This requires four function evaluations at the corners of the rectangle $[S_0 - h_S, S_0 + h_S] \times [v_0 - h_v, v_0 + h_v]$.

    **Noise amplification.** Each evaluation has noise $\epsilon$. The numerator involves four noisy quantities combined with alternating signs, so the noise in the numerator is at most $4\epsilon$ in the worst case (independent noise) or $\sqrt{4}\,\epsilon = 2\epsilon$ in standard deviation. The noise in the vanna estimate is:

    $$
    \operatorname{Std}(\widehat{\text{Vanna}}) \approx \frac{2\epsilon}{4\,h_S\,h_v} = \frac{\epsilon}{2\,h_S\,h_v}
    $$

    With CRN, the noise is substantially reduced because the four evaluations share the same random draws. The effective noise becomes:

    $$
    \operatorname{Std}(\widehat{\text{Vanna}}_{\text{CRN}}) \approx \frac{\sigma_{\text{cross}}}{4\,h_S\,h_v\,\sqrt{M}}
    $$

    where $\sigma_{\text{cross}}$ is the standard deviation of the single-path cross-difference (typically much smaller than $4\epsilon$).

    **Path count for 0.001 accuracy.** For a Monte Carlo engine without CRN, $\epsilon = \sigma_{\text{MC}} / \sqrt{M}$. The vanna standard error requirement is:

    $$
    \frac{\sigma_{\text{MC}}}{2\,h_S\,h_v\,\sqrt{M}} \leq 0.001
    $$

    With typical values $\sigma_{\text{MC}} \approx 10$ (standard deviation of call payoff), $h_S = 1.0$, $h_v = 0.001$:

    $$
    \sqrt{M} \geq \frac{10}{2 \times 1.0 \times 0.001 \times 0.001} = 5 \times 10^6 \quad \implies \quad M \geq 2.5 \times 10^{13}
    $$

    This is clearly infeasible without CRN. With CRN (reducing the effective noise by a factor of $\sim 100$):

    $$
    M_{\text{CRN}} \geq \frac{2.5 \times 10^{13}}{100^2} = 2.5 \times 10^9
    $$

    Still very large. In practice, vanna is one of the most difficult Greeks to compute via Monte Carlo finite differences. Common approaches to make it feasible include:

    - Using larger bumps (e.g., $h_S = 2.0$, $h_v = 0.005$), reducing $M$ to $\sim 10^7$ with CRN
    - Pathwise differentiation (avoiding finite differences entirely)
    - Computing vanna from the PDE grid when available

---

**Exercise 6.**
Design a validation test: compute delta, gamma, and vega using both CF differentiation and finite differences for a European call under Heston. The CF method serves as the reference. Vary the bump size $h$ logarithmically from $10^{-8}$ to $10^{-1}$ and plot the finite-difference error. Describe the expected V-shaped error curve and identify the optimal bump region.

??? success "Solution to Exercise 6"
    **Validation test design.**

    1. Fix Heston parameters: $S_0 = 100$, $K = 100$, $T = 1$, $r = 0.05$, $q = 0$, $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$.
    2. Compute reference values using CF differentiation: $\Delta_{\text{ref}}$, $\Gamma_{\text{ref}}$, $\mathcal{V}_{\text{ref}}$.
    3. For each bump size $h \in \{10^{-8}, 10^{-7.5}, 10^{-7}, \ldots, 10^{-1}\}$ (about 15 points on a logarithmic scale):
        - Compute $\Delta(h)$ using central differences on the COS pricer
        - Compute $\Gamma(h)$ using the second-derivative central difference
        - Compute $\mathcal{V}(h)$ by bumping $v_0$ with $h_v = h \times v_0 / S_0$ (scaling to keep the relative perturbation comparable)
    4. Plot $|\Delta(h) - \Delta_{\text{ref}}|$, $|\Gamma(h) - \Gamma_{\text{ref}}|$, $|\mathcal{V}(h) - \mathcal{V}_{\text{ref}}|$ versus $h$ on a log-log scale.

    **Expected V-shaped error curve.** The error plot for each Greek exhibits a characteristic V-shape (or U-shape on log-log axes):

    - **Right side (large $h$):** Truncation error dominates. The error decreases as $h$ shrinks. For central differences:
        - Delta: slope $= 2$ on the log-log plot (error $\propto h^2$)
        - Gamma: slope $= 2$ (error $\propto h^2$)
    - **Left side (small $h$):** Numerical noise dominates. The error increases as $h$ shrinks because the signal-to-noise ratio deteriorates:
        - Delta: slope $= -1$ (error $\propto \epsilon / h$)
        - Gamma: slope $= -2$ (error $\propto \epsilon / h^2$)
    - **Bottom of the V (optimal $h^*$):** The two error sources are balanced. This is the optimal bump region.

    For a COS engine with $\epsilon \approx 10^{-10}$:

    - **Delta optimal region:** $h^* \approx 10^{-3}$ to $10^{-2}$, with minimum error $\approx 10^{-7}$ to $10^{-8}$
    - **Gamma optimal region:** $h^* \approx 10^{-2.5}$ to $10^{-1.5}$, with minimum error $\approx 10^{-5}$ to $10^{-6}$
    - **Vega optimal region:** Similar to delta, $h^*_v \approx 10^{-4}$ to $10^{-3}$ in variance units

    The gamma V-curve has its minimum shifted to the right (larger $h$) and its minimum error is higher, consistent with the $\epsilon / h^2$ noise amplification being more severe. The validation test passes if the minimum finite-difference error for each Greek is small (e.g., $< 10^{-5}$ for delta and vega, $< 10^{-4}$ for gamma) and the V-shape slopes match the theoretical predictions ($h^2$ on the right, $1/h$ or $1/h^2$ on the left).
