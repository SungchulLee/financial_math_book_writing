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

### Short Maturities ($T \leq 3$ months)

For small $T$, the variance process has not yet mean-reverted significantly: $v_T \approx v_0 + \mathcal{O}(\kappa T)$. The short-maturity smile is therefore controlled primarily by:

- **$v_0$ (initial variance)**: Determines the ATM implied volatility level. The approximation $\sigma_{\text{ATM}}^2 T \approx v_0 T$ holds for short $T$, so the ATM level directly pins down $v_0$.
- **$\rho$ (correlation)**: Controls the **skew** (slope of the smile). To leading order in $T$, the ATM skew is:

$$
\left. \frac{\partial \sigma_{\text{imp}}}{\partial \ln K} \right|_{K = S_0 e^{rT}} \approx \frac{\rho \xi}{4 \sqrt{v_0}}
$$

This linear-in-$\rho$ dependence makes $\rho$ well-identified from the short-maturity skew.

- **$\xi$ (vol-of-vol)**: Controls the **convexity** (curvature) of the smile. To leading order:

$$
\left. \frac{\partial^2 \sigma_{\text{imp}}}{\partial (\ln K)^2} \right|_{K = S_0 e^{rT}} \approx \frac{\xi^2(1 - \rho^2)}{8 v_0}
$$

### Long Maturities ($T \geq 1$ year)

For large $T$, the variance process has time to mean-revert, and the smile reflects the long-run behavior:

- **$\theta$ (long-run variance)**: Determines the long-maturity ATM level. As $T \to \infty$, $\sigma_{\text{ATM}}^2 \to \theta$. Options with $T > 1/\kappa$ (the mean-reversion half-life) are primarily sensitive to $\theta$.
- **$\kappa$ (mean-reversion speed)**: Controls how quickly the term structure of ATM volatility transitions from $\sqrt{v_0}$ (short end) to $\sqrt{\theta}$ (long end). The ATM variance term structure is approximately:

$$
\bar{v}(T) = \frac{1}{T} \int_0^T \mathbb{E}[v_t] \, dt = \theta + (v_0 - \theta) \frac{1 - e^{-\kappa T}}{\kappa T}
$$

The shape of $\bar{v}(T)$ as a function of $T$ identifies $\kappa$ separately from $\theta$.

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
