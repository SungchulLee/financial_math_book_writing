# Joint Calibration Across Maturities

Calibrating the Heston model to a single maturity is straightforward but incomplete: the five parameters are under-determined by one expiry's smile alone, and the resulting model may produce nonsensical prices for other maturities. **Joint calibration** fits the model to the entire implied volatility surface simultaneously, using options across multiple strikes and maturities. Different parts of the surface constrain different parameters: short maturities pin down $v_0$ and $\rho$, while long maturities identify the mean-reversion speed $\kappa$ and long-run variance $\theta$. Achieving a balanced fit across all maturities requires careful weighting and an understanding of the Heston model's term-structure constraints.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Formulate the joint calibration objective over a grid of strikes and maturities
    2. Explain which Heston parameters are identified by short-maturity versus long-maturity options
    3. Design maturity weighting schemes that balance the fit across the term structure
    4. Diagnose term-structure misfit as a signal of model inadequacy

!!! tip "Prerequisites"
    This section builds on the [objective function design](objective_function_design.md), the [differential evolution](differential_evolution.md) optimizer, and the [Heston SDE and parameters](../model_definition/heston_sde_and_parameters.md).

---

## The Joint Objective Function

Suppose the market provides options at $N_T$ maturities $\{T_1, \ldots, T_{N_T}\}$, with $N_j$ strikes $\{K_{j,1}, \ldots, K_{j,N_j}\}$ at maturity $T_j$. The total number of calibration instruments is $M = \sum_{j=1}^{N_T} N_j$. The joint objective function aggregates errors across all instruments:

$$
\mathcal{L}(\Theta) = \sum_{j=1}^{N_T} \sum_{k=1}^{N_j} w_{jk} \left( \sigma_{jk}^{\text{mod}}(\Theta) - \sigma_{jk}^{\text{mkt}} \right)^2
$$

where $\sigma_{jk}^{\text{mod}}(\Theta)$ and $\sigma_{jk}^{\text{mkt}}$ are the model and market implied volatilities for the option with strike $K_{j,k}$ and maturity $T_j$, and $w_{jk} > 0$ are weights.

This is the same vega-weighted IV-space formulation from the [objective function design](objective_function_design.md) section, now written to emphasize the maturity structure.

---

## What Different Maturities Identify

The Heston model's five parameters have different sensitivities to different parts of the term structure. Understanding these sensitivities is essential for designing a calibration that uses market data efficiently.

### Short Maturities (T ≤ 3 months)

Recall (see [§ Heston SDE and Parameters](../model_definition/heston_sde_and_parameters.md)) for parameter roles. For small $T$, the variance process has not yet mean-reverted significantly. The short-maturity smile is controlled by:

- **$v_0$**: pins the ATM level via $\sigma_{\text{ATM}}^2 T \approx v_0 T$.
- **$\rho$**: controls the **skew** with $\partial\sigma_{\text{imp}}/\partial\ln K|_{\text{ATM}} \approx \rho\xi / (4\sqrt{v_0})$, making $\rho$ well-identified from short-maturity skew.
- **$\xi$**: controls **convexity** with $\partial^2\sigma_{\text{imp}}/\partial(\ln K)^2|_{\text{ATM}} \approx \xi^2(1-\rho^2)/(8 v_0)$.

### Long Maturities (T ≥ 1 year)

For large $T$, the variance process has time to mean-revert:

- **$\theta$**: as $T \to \infty$, $\sigma_{\text{ATM}}^2 \to \theta$. Options with $T > 1/\kappa$ are primarily sensitive to $\theta$.
- **$\kappa$**: controls the rate of transition. Recall (see [§ Variance Dynamics](../variance_dynamics/cir_variance_process_solution.md)) the expected average variance:

$$
\bar{v}(T) = \frac{1}{T} \int_0^T \mathbb{E}[v_t] \, dt = \theta + (v_0 - \theta) \frac{1 - e^{-\kappa T}}{\kappa T}
$$

The shape of $\bar{v}(T)$ identifies $\kappa$ separately from $\theta$.

!!! note "The Role of Medium Maturities"
    Options with $T \approx 1/\kappa$ (typically 3--12 months) are critical for separating $\kappa$ from $\theta$. The transition region of the variance term structure provides the strongest signal for $\kappa$. Without medium-maturity data, the $\kappa$-$\theta$ degeneracy remains.

---

## Maturity Weighting Schemes

With uniform weights $w_{jk} = 1/M$, maturities with many strikes dominate the objective. A maturity with 50 listed strikes contributes 50 terms while one with 10 strikes contributes only 10, biasing the calibration toward the densely-quoted maturity.

### Equal Weight per Maturity

Assign total weight $1/N_T$ to each maturity, distributed uniformly across its strikes:

$$
w_{jk} = \frac{1}{N_T \cdot N_j}
$$

This ensures each maturity contributes equally to the objective regardless of how many strikes are available.

### Inverse-Variance Weighting

Weight each maturity by the inverse of the squared bid-ask spread, averaged across its strikes:

$$
W_j = \frac{1}{N_j} \sum_{k=1}^{N_j} \frac{1}{(\sigma_{jk}^{\text{ask}} - \sigma_{jk}^{\text{bid}})^2}
$$

$$
w_{jk} = \frac{W_j^{-1}}{\sum_{j'} W_{j'}^{-1}} \cdot \frac{1}{N_j}
$$

This downweights illiquid maturities (wide spreads) and upweights liquid ones.

### Term-Structure-Aware Weighting

To emphasize the term-structure shape (and thus improve identification of $\kappa$), assign extra weight to the ATM options across all maturities. Define the ATM option at maturity $T_j$ as the strike closest to $S_0 e^{rT_j}$, and set:

$$
w_{jk} = \begin{cases} \alpha / N_T & \text{if } K_{j,k} \text{ is the ATM strike at } T_j \\ (1 - \alpha) / (M - N_T) & \text{otherwise} \end{cases}
$$

where $\alpha \in [0.3, 0.5]$ places 30--50% of the total weight on ATM options. The resulting calibration prioritizes matching the ATM term structure, which contains the clearest signal for $\kappa$ and $\theta$.

---

## Term-Structure Consistency

The Heston model imposes structural constraints on how the implied volatility surface evolves across maturities. Violations of these constraints indicate model inadequacy rather than calibration failure.

### ATM Variance Term Structure

The expected average variance $\bar{v}(T)$ is monotone: if $v_0 < \theta$, then $\bar{v}(T)$ increases from $v_0$ toward $\theta$; if $v_0 > \theta$, it decreases. This means the Heston model **cannot produce** an ATM term structure that is humped (increasing then decreasing) or U-shaped. If the market ATM term structure has a hump, the Heston model will always misfit one region.

### Skew Decay

The Heston model predicts that the smile skew decays as $1/\sqrt{T}$ for large $T$:

$$
\text{skew}(T) \sim \frac{\rho \xi}{2\sqrt{\theta}} \cdot \frac{1}{\sqrt{T}} \qquad \text{as } T \to \infty
$$

Market skews often decay **faster** than $1/\sqrt{T}$ at medium maturities (the "term structure of skew" is steeper than the model allows), producing systematic misfit. This is a structural limitation of the single-factor Heston model, partially resolved by the [double Heston model](../extensions/double_heston_model.md).

!!! warning "Diagnosing Model Inadequacy"
    After joint calibration, plot the residuals $\sigma_{jk}^{\text{mod}} - \sigma_{jk}^{\text{mkt}}$ as a function of $T_j$ for fixed moneyness levels. Systematic patterns in the residuals (e.g., all short-maturity smiles are too flat, all long-maturity skews are too steep) signal model limitations, not calibration problems. Increasing the number of DE generations or changing weights will not fix structural misfit.

---

## Sequential vs Simultaneous Calibration

Two strategies exist for multi-maturity calibration.

### Sequential (Maturity-by-Maturity)

Calibrate independently to each maturity $T_j$, producing $N_T$ parameter sets $\{\Theta^{*(j)}\}$. This gives perfect per-maturity fits but typically produces **inconsistent parameters**: different $\kappa$ and $\theta$ for different maturities, which is impossible under the Heston model (parameters are time-homogeneous).

Sequential calibration is useful as a diagnostic: the spread of parameter values across maturities reveals which parameters are maturity-dependent and where the model's constant-parameter assumption breaks down.

### Simultaneous (Joint)

Fit a single parameter set $\Theta^*$ to all maturities simultaneously. The resulting parameters are consistent by construction, but the fit at each individual maturity is typically worse than the sequential fit.

The gap between sequential and simultaneous fit quality quantifies the **model risk**: it measures how well the constant-parameter Heston model approximates the true (time-varying) dynamics of the implied volatility surface.

---

## Worked Example

Consider SPX options at five maturities: $T \in \{1\text{M}, 3\text{M}, 6\text{M}, 1\text{Y}, 2\text{Y}\}$ with $S_0 = 4500$, $r = 0.04$, $q = 0.015$.

**Market data summary** (ATM implied volatilities):

| Maturity | ATM IV | Number of strikes |
|---|---|---|
| 1M | 16.2% | 40 |
| 3M | 17.5% | 35 |
| 6M | 18.8% | 25 |
| 1Y | 20.1% | 20 |
| 2Y | 21.0% | 15 |

The increasing ATM term structure suggests $v_0 < \theta$ (variance is currently below its long-run level).

**Step 1: Sequential calibration.**

| Parameter | 1M | 3M | 6M | 1Y | 2Y |
|---|---|---|---|---|---|
| $v_0$ | 0.0263 | 0.0262 | 0.0265 | 0.0260 | 0.0258 |
| $\kappa$ | 1.20 | 2.50 | 3.10 | 2.80 | 2.40 |
| $\theta$ | 0.0800 | 0.0410 | 0.0380 | 0.0420 | 0.0450 |
| $\xi$ | 0.45 | 0.38 | 0.35 | 0.33 | 0.30 |
| $\rho$ | $-0.75$ | $-0.72$ | $-0.70$ | $-0.68$ | $-0.65$ |

Notice: $v_0$ and $\rho$ are stable across maturities (well-identified), while $\kappa$ and $\theta$ vary significantly (the $\kappa$-$\theta$ degeneracy). The product $\kappa\theta$ ranges from 0.096 to 0.118, more stable than either parameter alone.

**Step 2: Joint calibration** with equal-weight-per-maturity, producing $\Theta^* = (0.0262, 2.45, 0.0425, 0.36, -0.71)$.

**Step 3: Fit quality comparison.**

| Maturity | Sequential IVRMSE (bps) | Joint IVRMSE (bps) |
|---|---|---|
| 1M | 12 | 35 |
| 3M | 15 | 22 |
| 6M | 18 | 20 |
| 1Y | 14 | 25 |
| 2Y | 20 | 38 |

The joint fit is 15--25 basis points worse at individual maturities, with the largest deterioration at 1M and 2Y. This is acceptable for most hedging applications (bid-ask spreads are typically 50--100 bps for OTM options).

---

## Summary

Joint calibration across maturities is essential for producing a self-consistent Heston model. Short maturities identify $v_0$ and $\rho$; long maturities identify $\theta$; medium maturities separate $\kappa$ from $\theta$ by constraining the transition time scale. Maturity weighting schemes---equal weight per maturity, inverse-variance weighting, or ATM-focused weighting---prevent dense strike sets from dominating the objective. Systematic residual patterns across maturities signal structural model limitations (non-monotone ATM term structure, over-steep skew decay) that no amount of parameter tuning can fix, motivating extensions such as the double Heston model or time-dependent parameters.

---

## Exercises

**Exercise 1.**
Consider the expected average variance formula:

$$
\bar{v}(T) = \theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}
$$

For a Heston model with $v_0 = 0.0262$, $\kappa = 2.45$, and $\theta = 0.0425$, compute $\bar{v}(T)$ and the corresponding ATM implied volatility $\sigma_{\text{ATM}} \approx \sqrt{\bar{v}(T)}$ for $T = 1/12, 1/4, 1/2, 1, 2$. Verify that the resulting term structure is monotonically increasing and explain why.

??? success "Solution to Exercise 1"
    Given $v_0 = 0.0262$, $\kappa = 2.45$, $\theta = 0.0425$. The formula is:

    $$
    \bar{v}(T) = \theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}
    $$

    Note that $v_0 - \theta = 0.0262 - 0.0425 = -0.0163$.

    **$T = 1/12$ (1 month):**

    $$
    \kappa T = 2.45 / 12 = 0.2042
    $$

    $$
    \frac{1 - e^{-0.2042}}{0.2042} = \frac{1 - 0.8153}{0.2042} = \frac{0.1847}{0.2042} = 0.9045
    $$

    $$
    \bar{v}(1/12) = 0.0425 + (-0.0163)(0.9045) = 0.0425 - 0.01474 = 0.02776
    $$

    $$
    \sigma_{\text{ATM}} \approx \sqrt{0.02776} = 16.66\%
    $$

    **$T = 1/4$ (3 months):**

    $$
    \kappa T = 2.45 \times 0.25 = 0.6125
    $$

    $$
    \frac{1 - e^{-0.6125}}{0.6125} = \frac{1 - 0.5419}{0.6125} = \frac{0.4581}{0.6125} = 0.7480
    $$

    $$
    \bar{v}(1/4) = 0.0425 + (-0.0163)(0.7480) = 0.0425 - 0.01219 = 0.03031
    $$

    $$
    \sigma_{\text{ATM}} \approx \sqrt{0.03031} = 17.41\%
    $$

    **$T = 1/2$ (6 months):**

    $$
    \kappa T = 2.45 \times 0.5 = 1.225
    $$

    $$
    \frac{1 - e^{-1.225}}{1.225} = \frac{1 - 0.2940}{1.225} = \frac{0.7060}{1.225} = 0.5763
    $$

    $$
    \bar{v}(1/2) = 0.0425 + (-0.0163)(0.5763) = 0.0425 - 0.00939 = 0.03311
    $$

    $$
    \sigma_{\text{ATM}} \approx \sqrt{0.03311} = 18.20\%
    $$

    **$T = 1$ (1 year):**

    $$
    \kappa T = 2.45
    $$

    $$
    \frac{1 - e^{-2.45}}{2.45} = \frac{1 - 0.08652}{2.45} = \frac{0.9135}{2.45} = 0.3728
    $$

    $$
    \bar{v}(1) = 0.0425 + (-0.0163)(0.3728) = 0.0425 - 0.00608 = 0.03642
    $$

    $$
    \sigma_{\text{ATM}} \approx \sqrt{0.03642} = 19.08\%
    $$

    **$T = 2$ (2 years):**

    $$
    \kappa T = 4.90
    $$

    $$
    \frac{1 - e^{-4.90}}{4.90} = \frac{1 - 0.00745}{4.90} = \frac{0.9926}{4.90} = 0.2026
    $$

    $$
    \bar{v}(2) = 0.0425 + (-0.0163)(0.2026) = 0.0425 - 0.00330 = 0.03920
    $$

    $$
    \sigma_{\text{ATM}} \approx \sqrt{0.03920} = 19.80\%
    $$

    **Summary:**

    | $T$ | $\bar{v}(T)$ | $\sigma_{\text{ATM}}$ |
    |---|---|---|
    | 1/12 | 0.02776 | 16.66% |
    | 1/4 | 0.03031 | 17.41% |
    | 1/2 | 0.03311 | 18.20% |
    | 1 | 0.03642 | 19.08% |
    | 2 | 0.03920 | 19.80% |

    The term structure is monotonically increasing because $v_0 = 0.0262 < \theta = 0.0425$. Since the current variance is below the long-run level, the expected average variance increases with $T$ as the process mean-reverts upward toward $\theta$. Mathematically, the factor $(1 - e^{-\kappa T})/(\kappa T)$ is a decreasing function of $T$ (starting near 1 for small $T$ and decaying to 0 for large $T$), so the negative term $(v_0 - \theta) \times (1 - e^{-\kappa T})/(\kappa T)$ becomes less negative as $T$ increases, causing $\bar{v}(T)$ to rise monotonically from $v_0$ toward $\theta$.

---

**Exercise 2.**
Using the short-maturity skew approximation:

$$
\left. \frac{\partial \sigma_{\text{imp}}}{\partial \ln K} \right|_{K = S_0 e^{rT}} \approx \frac{\rho \xi}{4 \sqrt{v_0}}
$$

compute the ATM skew for $v_0 = 0.04$, $\xi = 0.5$, and $\rho = -0.7$. If the market skew at $T = 1$ month is $-2.8$ per unit log-strike, estimate $\rho$ assuming $v_0$ and $\xi$ are known. Discuss why $\rho$ is well-identified from short-maturity skew data.

??? success "Solution to Exercise 2"
    The short-maturity skew approximation gives:

    $$
    \left. \frac{\partial \sigma_{\text{imp}}}{\partial \ln K} \right|_{K = S_0 e^{rT}} \approx \frac{\rho \xi}{4 \sqrt{v_0}}
    $$

    With $v_0 = 0.04$, $\xi = 0.5$, $\rho = -0.7$:

    $$
    \text{skew} \approx \frac{(-0.7)(0.5)}{4\sqrt{0.04}} = \frac{-0.35}{4 \times 0.2} = \frac{-0.35}{0.8} = -0.4375
    $$

    This means the implied volatility decreases by approximately 0.4375 percentage points (43.75 bps) per unit increase in log-strike.

    **Estimating $\rho$ from market data:** If the observed market skew at $T = 1$ month is $-2.8$ per unit log-strike, we solve:

    $$
    -2.8 = \frac{\rho \times 0.5}{4 \times 0.2} = \frac{0.5\rho}{0.8} = 0.625\rho
    $$

    $$
    \rho = \frac{-2.8}{0.625} = -4.48
    $$

    This value $|\rho| = 4.48 > 1$ is outside the admissible range $|\rho| < 1$, which indicates that the short-maturity approximation has broken down. The leading-order formula is accurate only for small perturbations around ATM and may not capture the full skew observed in the market, especially at very short maturities where higher-order terms and jump contributions become important. In practice, one would use the full calibration machinery rather than this approximation to extract $\rho$.

    If instead the market skew were a more moderate $-0.50$, we would get $\rho = -0.50 / 0.625 = -0.80$, which is in the admissible range and consistent with typical equity calibrations.

    **Why $\rho$ is well-identified:** The skew approximation is linear in $\rho$ with a known coefficient $\xi/(4\sqrt{v_0})$. Once $v_0$ is pinned down by the ATM level and $\xi$ is constrained by the smile curvature, the skew uniquely determines $\rho$. The linear dependence means small changes in the market skew translate directly into proportional changes in $\rho$, with no degeneracy or ambiguity.

---

**Exercise 3.**
A calibration uses five maturities with strike counts $N_1 = 40$, $N_2 = 35$, $N_3 = 25$, $N_4 = 20$, $N_5 = 15$ for a total of $M = 135$ options. Compare the effective per-maturity weight under: (a) uniform weights $w_{jk} = 1/M$, and (b) equal-weight-per-maturity $w_{jk} = 1/(N_T \cdot N_j)$. Show that under uniform weights, the 1M maturity receives $40/135 \approx 29.6\%$ of the total weight, while under equal-weight-per-maturity each receives exactly 20%.

??? success "Solution to Exercise 3"
    **(a) Uniform weights $w_{jk} = 1/M = 1/135$:**

    The total weight assigned to maturity $j$ is $N_j / M$:

    | Maturity $j$ | $N_j$ | Weight $= N_j / 135$ |
    |---|---|---|
    | 1 (1M) | 40 | $40/135 = 29.6\%$ |
    | 2 (3M) | 35 | $35/135 = 25.9\%$ |
    | 3 (6M) | 25 | $25/135 = 18.5\%$ |
    | 4 (1Y) | 20 | $20/135 = 14.8\%$ |
    | 5 (2Y) | 15 | $15/135 = 11.1\%$ |

    The 1M maturity receives nearly 30% of the total weight, while the 2Y maturity receives only 11%. The calibration is biased toward fitting the 1M smile, which has the most strikes.

    **(b) Equal-weight-per-maturity $w_{jk} = 1/(N_T \cdot N_j)$:**

    The total weight for maturity $j$ is:

    $$
    \sum_{k=1}^{N_j} w_{jk} = N_j \times \frac{1}{N_T \cdot N_j} = \frac{1}{N_T} = \frac{1}{5} = 20\%
    $$

    Each maturity contributes exactly 20% of the total weight, regardless of the number of strikes. The per-option weights differ across maturities:

    | Maturity $j$ | $N_j$ | $w_{jk} = 1/(5 N_j)$ | Total weight |
    |---|---|---|---|
    | 1 (1M) | 40 | $1/200 = 0.005$ | 20% |
    | 2 (3M) | 35 | $1/175 = 0.00571$ | 20% |
    | 3 (6M) | 25 | $1/125 = 0.008$ | 20% |
    | 4 (1Y) | 20 | $1/100 = 0.01$ | 20% |
    | 5 (2Y) | 15 | $1/75 = 0.01333$ | 20% |

    Individual options at sparsely-quoted maturities (2Y) receive higher individual weights to compensate for there being fewer of them. This ensures the 2Y term structure information is not drowned out by the densely-quoted 1M maturity.

---

**Exercise 4.**
The sequential calibration in the worked example yields parameter sets that vary across maturities. Compute the product $\kappa\theta$ for each maturity and verify that it is more stable than $\kappa$ or $\theta$ individually. Explain the $\kappa$-$\theta$ degeneracy: why does short-maturity data constrain $\kappa\theta$ but not $\kappa$ and $\theta$ separately? Hint: consider the expansion of $\bar{v}(T)$ for $\kappa T \ll 1$.

??? success "Solution to Exercise 4"
    **Computing $\kappa\theta$ for each maturity:**

    | Maturity | $\kappa$ | $\theta$ | $\kappa\theta$ |
    |---|---|---|---|
    | 1M | 1.20 | 0.0800 | 0.0960 |
    | 3M | 2.50 | 0.0410 | 0.1025 |
    | 6M | 3.10 | 0.0380 | 0.1178 |
    | 1Y | 2.80 | 0.0420 | 0.1176 |
    | 2Y | 2.40 | 0.0450 | 0.1080 |

    **Stability comparison:**

    - $\kappa$ ranges from 1.20 to 3.10: a factor of 2.58, or relative spread of $(3.10 - 1.20)/2.10 = 90\%$ around the mean
    - $\theta$ ranges from 0.038 to 0.080: a factor of 2.11, or relative spread of $(0.080 - 0.038)/0.050 = 84\%$ around the mean
    - $\kappa\theta$ ranges from 0.096 to 0.118: a factor of 1.23, or relative spread of $(0.118 - 0.096)/0.107 = 20\%$ around the mean

    The product $\kappa\theta$ is approximately four times more stable than either parameter individually.

    **Explaining the degeneracy:** For short maturities $\kappa T \ll 1$, the expected integrated variance is:

    $$
    \mathbb{E}\!\left[\int_0^T v_t \, dt\right] \approx v_0 T + \frac{1}{2}\kappa(\theta - v_0) T^2
    $$

    The first-order correction to the base level $v_0 T$ depends on $\kappa(\theta - v_0) = \kappa\theta - \kappa v_0$. Since $v_0$ is fixed by the ATM level, this correction depends on $\kappa\theta$ as a single quantity. Doubling $\kappa$ while halving $\theta$ (keeping $\kappa\theta$ fixed) leaves the short-maturity expected variance unchanged to second order in $T$. The individual effects of $\kappa$ (controlling the rate of mean-reversion) and $\theta$ (controlling the target level) only become distinguishable when $\kappa T$ is no longer small, i.e., when the mean-reversion has had time to act. This requires $T \gtrsim 1/\kappa$, which for $\kappa \approx 2$--$3$ means maturities of 4--6 months or longer.

---

**Exercise 5.**
The Heston model predicts skew decay as:

$$
\text{skew}(T) \sim \frac{\rho \xi}{2\sqrt{\theta}} \cdot \frac{1}{\sqrt{T}} \qquad \text{as } T \to \infty
$$

Given $\rho = -0.71$, $\xi = 0.36$, and $\theta = 0.0425$, compute the predicted skew at $T = 0.25, 0.5, 1, 2, 5$ years. If the market skew at $T = 5$ years is $-0.35$ (per unit log-strike), but the model predicts $-0.28$, discuss whether this discrepancy can be eliminated by adjusting $\rho$, $\xi$, or $\theta$ without degrading the fit at shorter maturities.

??? success "Solution to Exercise 5"
    The Heston skew decay formula is:

    $$
    \text{skew}(T) \approx \frac{\rho \xi}{2\sqrt{\theta}} \cdot \frac{1}{\sqrt{T}}
    $$

    With $\rho = -0.71$, $\xi = 0.36$, $\theta = 0.0425$:

    $$
    \frac{\rho\xi}{2\sqrt{\theta}} = \frac{(-0.71)(0.36)}{2\sqrt{0.0425}} = \frac{-0.2556}{2 \times 0.2062} = \frac{-0.2556}{0.4124} = -0.6200
    $$

    Computing the predicted skew at each maturity:

    | $T$ | $1/\sqrt{T}$ | Predicted skew |
    |---|---|---|
    | 0.25 | 2.000 | $-0.620 \times 2.000 = -1.240$ |
    | 0.5 | 1.414 | $-0.620 \times 1.414 = -0.877$ |
    | 1 | 1.000 | $-0.620 \times 1.000 = -0.620$ |
    | 2 | 0.707 | $-0.620 \times 0.707 = -0.438$ |
    | 5 | 0.447 | $-0.620 \times 0.447 = -0.277$ |

    **Discrepancy at $T = 5$:** The model predicts a skew of $-0.277$ (approximately $-0.28$), but the market skew is $-0.35$. The market skew is steeper (more negative) than the model.

    **Can adjusting parameters fix this?** To match $-0.35$ at $T = 5$, we would need:

    $$
    -0.35 = \frac{\rho\xi}{2\sqrt{\theta}} \times \frac{1}{\sqrt{5}}
    $$

    $$
    \frac{\rho\xi}{2\sqrt{\theta}} = -0.35 \times \sqrt{5} = -0.783
    $$

    This requires increasing $|\rho\xi / \sqrt{\theta}|$ from $0.620$ to $0.783$ (a 26% increase). Options include:

    - Making $\rho$ more negative (e.g., $\rho = -0.90$): This would also steepen the short-maturity skew, overshooting the market at $T = 0.25$.
    - Increasing $\xi$ (e.g., $\xi = 0.45$): This also increases smile curvature at all maturities, potentially degrading the fit at short maturities.
    - Decreasing $\theta$: This changes the ATM term structure level, degrading the long-maturity ATM fit.

    The fundamental problem is that the Heston model's skew decays as $1/\sqrt{T}$ at all maturities --- this is a structural property. If the market skew decays faster than $1/\sqrt{T}$ at medium maturities but remains relatively steep at long maturities, no single set of $(\rho, \xi, \theta)$ can simultaneously match both regimes. The discrepancy signals a structural limitation of the single-factor Heston model. A double Heston model, with two variance factors having different mean-reversion speeds, can produce richer skew term structure behavior by combining a fast-decaying component (from a rapidly mean-reverting factor) with a persistent component (from a slowly mean-reverting factor).

---

**Exercise 6.**
Define the model risk metric as the difference between sequential and joint IVRMSE at each maturity. Using the worked example data, compute this metric for all five maturities. Which maturity shows the largest model risk? Propose a weighting scheme that would reduce the joint IVRMSE at the worst-fitting maturity at the expense of the best-fitting ones. Write the modified objective function explicitly.

??? success "Solution to Exercise 6"
    **Computing the model risk metric** (joint IVRMSE $-$ sequential IVRMSE):

    | Maturity | Sequential IVRMSE (bps) | Joint IVRMSE (bps) | Model risk (bps) |
    |---|---|---|---|
    | 1M | 12 | 35 | 23 |
    | 3M | 15 | 22 | 7 |
    | 6M | 18 | 20 | 2 |
    | 1Y | 14 | 25 | 11 |
    | 2Y | 20 | 38 | 18 |

    The largest model risk is at 1M (23 bps), followed by 2Y (18 bps). The 6M maturity has the smallest model risk (2 bps), suggesting that the jointly calibrated parameters are closest to the sequentially calibrated parameters at this maturity --- consistent with 6M being a "middle ground" that the joint optimizer can fit well.

    **Proposed weighting scheme:** To reduce the joint IVRMSE at the worst-fitting maturities (1M and 2Y), increase their weight at the expense of the best-fitting maturities (6M and 3M). Define maturity-specific weights $\alpha_j$ and the modified objective:

    $$
    \mathcal{L}_{\text{modified}}(\Theta) = \sum_{j=1}^{5} \alpha_j \sum_{k=1}^{N_j} \frac{1}{N_j} \left(\sigma_{jk}^{\text{mod}}(\Theta) - \sigma_{jk}^{\text{mkt}}\right)^2
    $$

    A reasonable choice based on the model risk analysis:

    | Maturity | Model risk (bps) | Proposed $\alpha_j$ |
    |---|---|---|
    | 1M | 23 | 0.30 |
    | 3M | 7 | 0.15 |
    | 6M | 2 | 0.10 |
    | 1Y | 11 | 0.15 |
    | 2Y | 18 | 0.30 |

    with $\sum_j \alpha_j = 1$. The weights are roughly proportional to the model risk, so maturities where the joint fit suffers most receive the highest weight. This forces the optimizer to prioritize the 1M and 2Y maturities, redistributing the fit error toward the 6M and 3M maturities where the current fit has headroom.

    Note that this approach cannot eliminate the model risk entirely --- the Heston model's structural constraints (monotone ATM term structure, $1/\sqrt{T}$ skew decay) impose a floor on the achievable joint fit quality. The weighting merely redistributes the misfit across maturities in a way that better serves the user's priorities.

---

**Exercise 7.**
Consider designing an ATM-focused weighting scheme with parameter $\alpha = 0.4$. Given $N_T = 5$ maturities, $M = 135$ total options, and one ATM option per maturity, compute the weight $w_{jk}$ assigned to each ATM option and each non-ATM option. If the ATM bid-ask spread is typically 20 bps and the OTM wing bid-ask spread is 80 bps, argue that the ATM-focused scheme is consistent with inverse-variance weighting in spirit. Discuss when you might prefer $\alpha = 0.5$ over $\alpha = 0.3$.

??? success "Solution to Exercise 7"
    **Computing the weights:** With $\alpha = 0.4$, $N_T = 5$ maturities, $M = 135$ total options, and 5 ATM options (one per maturity):

    The total weight assigned to ATM options is $\alpha = 0.4$, distributed equally among the $N_T = 5$ ATM options:

    $$
    w_{\text{ATM}} = \frac{\alpha}{N_T} = \frac{0.4}{5} = 0.08
    $$

    The total weight assigned to non-ATM options is $1 - \alpha = 0.6$, distributed among $M - N_T = 135 - 5 = 130$ non-ATM options:

    $$
    w_{\text{non-ATM}} = \frac{1 - \alpha}{M - N_T} = \frac{0.6}{130} = 0.004615
    $$

    The ratio of ATM to non-ATM weight is:

    $$
    \frac{w_{\text{ATM}}}{w_{\text{non-ATM}}} = \frac{0.08}{0.004615} = 17.3
    $$

    Each ATM option receives about 17 times more weight than each non-ATM option.

    **Consistency with inverse-variance weighting:** Under inverse-variance weighting, the weight is proportional to $1/(\text{bid-ask spread})^2$. With ATM spread of 20 bps and OTM spread of 80 bps:

    $$
    \frac{w_{\text{ATM}}^{\text{inv-var}}}{w_{\text{OTM}}^{\text{inv-var}}} = \frac{1/20^2}{1/80^2} = \frac{80^2}{20^2} = 16
    $$

    The inverse-variance ratio is $16$, which is close to the ATM-focused ratio of $17.3$. This confirms that the ATM-focused scheme with $\alpha = 0.4$ is consistent in spirit with inverse-variance weighting: both assign roughly 16--17 times more weight to tightly-quoted ATM options than to wide-spread OTM options.

    **When to prefer $\alpha = 0.5$ over $\alpha = 0.3$:**

    - **$\alpha = 0.5$ (more ATM focus):** Prefer this when the primary goal is to calibrate the ATM term structure accurately, e.g., for pricing variance swaps or for extracting the mean-reversion parameters $\kappa$ and $\theta$ reliably. This is also appropriate when wing data is noisy or illiquid (wide spreads), making the wing IV unreliable.

    - **$\alpha = 0.3$ (less ATM focus):** Prefer this when wing fit quality matters, e.g., for pricing exotic options with payoffs sensitive to the tails (barrier options, digital options) or for risk management of portfolios with significant OTM exposure. This is appropriate when wing data is liquid and reliable, so the additional information content from wing options should influence the calibration.
