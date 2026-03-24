# Objective Function Design

Calibrating the Heston model means choosing five parameters $\Theta = (v_0, \kappa, \theta, \xi, \rho)$ so that model prices match market prices as closely as possible. The objective function translates this vague goal into a precise optimization problem---and its design has a surprisingly large effect on calibration quality, speed, and stability. Two natural choices arise: minimize errors in **price space** or in **implied-volatility space**. Each has distinct scaling properties, sensitivity to market data quality, and computational cost. This section develops both formulations rigorously, introduces vega weighting as the bridge between them, and compares RMSE and IVRMSE metrics.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Formulate the Heston calibration problem as a nonlinear least-squares optimization in both price space and implied-volatility space
    2. Derive the vega-weighting transformation that converts price-space errors into approximate IV-space errors
    3. Compare RMSE and IVRMSE metrics and explain when each is preferred
    4. Identify pathologies in objective function landscapes---flat regions, multiple minima, and parameter degeneracies

!!! tip "Prerequisites"
    This section builds on the [Heston SDE and parameters](../model_definition/heston_sde_and_parameters.md), the [closed-form characteristic function](../heston_cf/closed_form_characteristic_function.md), and the [semi-closed-form Fourier inversion](../european_pricing/semi_closed_form_fourier_inversion.md) for computing Heston option prices.

---

## The Calibration Problem

Suppose the market provides $M$ European option prices $\{C_i^{\text{mkt}}\}_{i=1}^M$ observed at strikes $K_i$ and maturities $T_i$. The Heston model produces corresponding model prices $C_i^{\text{mod}}(\Theta)$ via Fourier inversion of the characteristic function. Calibration seeks:

$$
\Theta^* = \arg\min_{\Theta \in \mathcal{A}} \; \mathcal{L}(\Theta)
$$

where $\mathcal{A}$ is the admissible parameter set (e.g., $v_0 > 0$, $\kappa > 0$, $\theta > 0$, $\xi > 0$, $|\rho| < 1$) and $\mathcal{L}$ is the objective function. The choice of $\mathcal{L}$ fundamentally shapes the optimization landscape.

---

## Price-Space Objective Function

The most direct formulation measures the squared difference between model and market prices.

### Definition

The **price-space objective** is the weighted sum of squared pricing errors:

$$
\mathcal{L}_{\text{price}}(\Theta) = \sum_{i=1}^{M} w_i \left( C_i^{\text{mod}}(\Theta) - C_i^{\text{mkt}} \right)^2
$$

where $w_i > 0$ are user-specified weights. With uniform weights $w_i = 1/M$, minimizing $\mathcal{L}_{\text{price}}$ is equivalent to minimizing the root-mean-square error:

$$
\text{RMSE} = \sqrt{\frac{1}{M} \sum_{i=1}^{M} \left( C_i^{\text{mod}}(\Theta) - C_i^{\text{mkt}} \right)^2}
$$

### Scaling Problem

Price-space calibration suffers from a fundamental scaling asymmetry. Deep in-the-money calls with strike $K = 80$ on a \$100 stock have prices of order \$20, while far out-of-the-money calls with $K = 130$ have prices of order \$0.50. A \$0.10 error on the first option is a 0.5% relative error, but the same absolute error on the second is a 20% relative error.

With uniform weights, the optimizer focuses almost entirely on fitting the high-priced (ITM) options and ignores the OTM options---precisely where the implied volatility smile carries the most information about the tails of the risk-neutral distribution.

!!! warning "Uniform Price Weights Distort Calibration"
    With $w_i = 1$ for all $i$, the objective function is dominated by ITM options. The calibrated model may fit the ATM and ITM region well but produce large implied volatility errors for OTM options. This defeats the purpose of calibrating to the volatility surface.

---

## Implied-Volatility-Space Objective Function

The alternative is to express errors in implied-volatility space, where the natural scale is more uniform across strikes and maturities.

### Definition

Let $\sigma_i^{\text{mkt}}$ denote the market implied volatility for the $i$-th option and $\sigma_i^{\text{mod}}(\Theta)$ the implied volatility backed out from the model price $C_i^{\text{mod}}(\Theta)$. The **IV-space objective** is:

$$
\mathcal{L}_{\text{IV}}(\Theta) = \sum_{i=1}^{M} w_i \left( \sigma_i^{\text{mod}}(\Theta) - \sigma_i^{\text{mkt}} \right)^2
$$

The corresponding error metric is the implied-volatility root-mean-square error:

$$
\text{IVRMSE} = \sqrt{\frac{1}{M} \sum_{i=1}^{M} \left( \sigma_i^{\text{mod}}(\Theta) - \sigma_i^{\text{mkt}} \right)^2}
$$

### Advantages

Implied volatilities for equity options typically range from 10% to 60%, regardless of moneyness or maturity. A 0.5 vol-point error has the same economic significance whether the option is ITM or OTM. This uniform scaling means uniform weights $w_i = 1$ in IV space already produce a well-balanced fit across the entire surface.

### Computational Cost

The disadvantage of IV-space calibration is computational: extracting $\sigma_i^{\text{mod}}(\Theta)$ from $C_i^{\text{mod}}(\Theta)$ requires inverting the Black-Scholes formula at every evaluation of the objective function. This inversion is typically done via Newton-Raphson on the Black-Scholes pricing formula:

$$
\sigma_{n+1} = \sigma_n - \frac{C^{\text{BS}}(K_i, T_i, \sigma_n) - C_i^{\text{mod}}(\Theta)}{\mathcal{V}_i(\sigma_n)}
$$

where $\mathcal{V}_i = \partial C^{\text{BS}} / \partial \sigma$ is the Black-Scholes vega. Each Newton iteration requires one Black-Scholes evaluation, and convergence typically takes 3--5 iterations. For $M$ options and $N_{\text{eval}}$ objective function evaluations during optimization, this adds $\mathcal{O}(M \cdot N_{\text{eval}})$ Black-Scholes calls on top of the Fourier pricing cost.

---

## Vega Weighting: Bridging the Two Spaces

Vega weighting provides a computationally cheap approximation to IV-space calibration while working entirely in price space.

### Derivation via the Inverse Function Theorem

The Black-Scholes pricing function $C^{\text{BS}}(K, T, \sigma)$ is monotonically increasing in $\sigma$ (for fixed $K, T$), so the implied volatility function $\sigma^{\text{imp}}(C)$ is well-defined. By the inverse function theorem:

$$
\frac{\partial \sigma^{\text{imp}}}{\partial C} = \frac{1}{\mathcal{V}}
$$

where $\mathcal{V} = \partial C^{\text{BS}} / \partial \sigma$ is the Black-Scholes vega. A first-order Taylor expansion of the implied volatility error around the market price gives:

$$
\sigma_i^{\text{mod}} - \sigma_i^{\text{mkt}} \approx \frac{C_i^{\text{mod}} - C_i^{\text{mkt}}}{\mathcal{V}_i}
$$

Substituting into the IV-space objective yields:

$$
\mathcal{L}_{\text{IV}}(\Theta) \approx \sum_{i=1}^{M} \frac{1}{\mathcal{V}_i^2} \left( C_i^{\text{mod}}(\Theta) - C_i^{\text{mkt}} \right)^2
$$

This is precisely the price-space objective with weights $w_i = 1/\mathcal{V}_i^2$.

### Definition

The **vega-weighted price-space objective** is:

$$
\mathcal{L}_{\text{vega}}(\Theta) = \sum_{i=1}^{M} \frac{1}{\mathcal{V}_i^2} \left( C_i^{\text{mod}}(\Theta) - C_i^{\text{mkt}} \right)^2
$$

where $\mathcal{V}_i = \mathcal{V}^{\text{BS}}(K_i, T_i, \sigma_i^{\text{mkt}})$ is the Black-Scholes vega evaluated at the market implied volatility. Since the market data are fixed, the weights $1/\mathcal{V}_i^2$ are constants computed once before optimization begins.

!!! note "Vega Weights Are Precomputed"
    The vega weights depend only on market data (strikes, maturities, market implied vols) and are computed once. They do not change during the optimization, so the per-iteration cost of $\mathcal{L}_{\text{vega}}$ is identical to that of $\mathcal{L}_{\text{price}}$.

### Why Vega Weighting Works

The Black-Scholes vega has the closed-form expression:

$$
\mathcal{V} = S_0 e^{-qT} \sqrt{T} \, \phi(d_1)
$$

where $\phi$ is the standard normal PDF and $d_1 = [\ln(S_0/K) + (r - q + \sigma^2/2)T] / (\sigma\sqrt{T})$. Key properties:

1. **ATM options** have the largest vega (since $\phi(d_1)$ is maximized near $d_1 = 0$), so their weight $1/\mathcal{V}^2$ is the smallest. The optimizer is allowed to sacrifice ATM fit slightly.
2. **Deep OTM options** have small vega, so their weight $1/\mathcal{V}^2$ is large. Small price errors on OTM options are amplified, forcing the optimizer to fit them carefully.
3. **Long-dated options** have larger vega (via the $\sqrt{T}$ factor), so they receive lower weight than short-dated options at the same moneyness.

This rebalancing naturally prioritizes the wings of the smile, where the Heston model's skew and kurtosis parameters $\rho$ and $\xi$ are most visible.

---

## Comparison of Error Metrics

The following table summarizes the three objective functions.

| Metric | Formula | Scaling | Cost per Evaluation |
|---|---|---|---|
| Price RMSE | $\sqrt{M^{-1}\sum (C_i^{\text{mod}} - C_i^{\text{mkt}})^2}$ | Dominated by ITM | Lowest: $M$ Fourier inversions |
| IVRMSE | $\sqrt{M^{-1}\sum (\sigma_i^{\text{mod}} - \sigma_i^{\text{mkt}})^2}$ | Uniform across surface | Highest: $M$ Fourier + $M$ Newton |
| Vega-weighted RMSE | $\sqrt{M^{-1}\sum \mathcal{V}_i^{-2}(C_i^{\text{mod}} - C_i^{\text{mkt}})^2}$ | Approximates IVRMSE | Same as price RMSE |

In practice, vega-weighted RMSE is the standard choice for Heston calibration. It closely approximates the IVRMSE objective while incurring no additional computational cost beyond the base pricing engine.

---

## Relative Weighting Schemes

Beyond the choice of error space, additional weighting across options can improve calibration for specific trading needs.

### Bid-Ask Spread Weighting

Options with wider bid-ask spreads carry more price uncertainty. A natural modification penalizes errors relative to the spread:

$$
w_i = \frac{1}{(\sigma_i^{\text{ask}} - \sigma_i^{\text{bid}})^2}
$$

Tight-spread options (typically ATM, liquid maturities) receive high weight, while wide-spread options (far OTM, illiquid) receive low weight.

### Maturity Weighting

For term-structure consistency, one may weight maturities to balance the number of options per expiry:

$$
w_i = \frac{1}{n_{T_i}}
$$

where $n_{T_i}$ is the number of options with maturity $T_i$. This prevents an expiry with 50 listed strikes from dominating one with only 10 strikes.

### Open Interest / Volume Weighting

Weighting by open interest or traded volume emphasizes the options that market participants actually use for hedging, focusing calibration effort on economically relevant contracts.

---

## Objective Function Landscape

The Heston calibration objective is non-convex with a complex landscape that depends on the choice of error metric.

### Multiple Local Minima

The five Heston parameters interact nonlinearly through the characteristic function. The skew depends on both $\rho$ and $\xi$; the term structure of ATM volatility depends on the combination $\kappa\theta$ rather than $\kappa$ and $\theta$ individually. This creates **ridges** and **valleys** in the objective function where different parameter combinations produce similar fits.

### Parameter Degeneracies

Two well-known degeneracies complicate calibration:

1. **$\kappa$-$\theta$ degeneracy**: Short-maturity options constrain $v_0$ and $\rho$ well, but only the product $\kappa\theta$ (not $\kappa$ and $\theta$ separately) affects the short-term smile. Separate identification requires long-maturity data.

2. **$\xi$-$\rho$ interaction**: Both parameters affect the smile curvature. Increasing $\xi$ steepens the smile, while making $\rho$ more negative increases the skew. These effects partially compensate, creating a valley of near-optimal solutions.

!!! warning "Flat Regions in the Landscape"
    Near the degeneracy manifold, the objective function gradient is small and the Hessian is ill-conditioned. Gradient-based optimizers converge slowly or stall, and the calibrated parameters may be sensitive to small changes in market data.

### Effect of Error Metric on Landscape

The vega-weighted and IVRMSE objectives typically produce a **more convex** landscape than the unweighted price objective. By normalizing errors to a common scale, vega weighting reduces the elongated valleys caused by ITM/OTM asymmetry. This makes the optimization easier for both gradient-based and global methods.

---

## Regularization

To combat parameter instability and degeneracy, a regularization term is often added to the objective function.

### Tikhonov Regularization

The penalized objective adds a quadratic penalty on the deviation from a reference parameter set $\Theta_{\text{ref}}$:

$$
\mathcal{L}_{\text{reg}}(\Theta) = \mathcal{L}(\Theta) + \lambda \| \Theta - \Theta_{\text{ref}} \|^2
$$

where $\lambda > 0$ is the regularization strength. The reference $\Theta_{\text{ref}}$ can be yesterday's calibrated parameters (for temporal stability) or a prior estimate from historical analysis.

### Weighted Regularization

Different parameters may warrant different penalty strengths:

$$
\mathcal{L}_{\text{reg}}(\Theta) = \mathcal{L}(\Theta) + \sum_{j=1}^{5} \lambda_j (\Theta_j - \Theta_{\text{ref},j})^2
$$

For example, one might penalize changes in $\kappa$ and $\theta$ strongly (since they are poorly identified from short-maturity data) while allowing $v_0$ and $\rho$ to vary freely (since they are well-constrained by market data).

---

## Worked Example

Consider calibrating to $M = 15$ European call options on a stock with $S_0 = 100$, $r = 0.02$, $q = 0$, at three maturities $T \in \{0.25, 0.5, 1.0\}$ with five strikes each $K \in \{85, 92, 100, 108, 115\}$.

**Step 1: Compute market vegas.** For each $(K_i, T_i, \sigma_i^{\text{mkt}})$, evaluate:

$$
\mathcal{V}_i = S_0 \sqrt{T_i} \, \phi(d_{1,i})
$$

For the ATM 1-year option with $\sigma^{\text{mkt}} = 0.20$: $d_1 = (0 + 0.02 + 0.02) \cdot 1 / 0.20 = 0.20$, so $\mathcal{V} = 100 \cdot 1.0 \cdot \phi(0.20) = 100 \cdot 0.3910 = 39.10$.

For the OTM ($K = 115$) 3-month option with $\sigma^{\text{mkt}} = 0.25$: $d_1 = [\ln(100/115) + (0.02 + 0.03125) \cdot 0.25] / (0.25 \cdot 0.5) = [-0.1398 + 0.01281] / 0.125 = -1.016$, so $\mathcal{V} = 100 \cdot 0.5 \cdot \phi(-1.016) = 50 \cdot 0.2396 = 11.98$.

**Step 2: Compute weights.** The vega weights are:

$$
w_{\text{ATM, 1Y}} = \frac{1}{39.10^2} = 6.54 \times 10^{-4}, \qquad w_{\text{OTM, 3M}} = \frac{1}{11.98^2} = 6.97 \times 10^{-3}
$$

The OTM short-dated option receives a weight roughly 10 times larger than the ATM long-dated option, compensating for its smaller price sensitivity.

**Step 3: Evaluate objective.** Suppose the model overprices the ATM call by \$0.50 and the OTM call by \$0.10. The contributions are:

- ATM: $6.54 \times 10^{-4} \times 0.50^2 = 1.64 \times 10^{-4}$
- OTM: $6.97 \times 10^{-3} \times 0.10^2 = 6.97 \times 10^{-5}$

Despite the ATM error being five times larger in price, the two contributions to the objective are comparable---confirming that vega weighting balances the fit across the surface.

---

## Summary

The objective function is the lens through which the optimizer views the calibration problem. Price-space RMSE is simple but biased toward ITM options. IV-space IVRMSE provides uniform scaling but adds computational overhead. Vega weighting achieves the best of both worlds: it approximates the IVRMSE objective via the first-order relationship $\Delta\sigma \approx \Delta C / \mathcal{V}$, with zero additional cost per iteration. In practice, vega-weighted least squares combined with Tikhonov regularization forms the standard objective function for Heston calibration, producing stable fits that balance accuracy across the implied volatility surface.

---

## Exercises

**Exercise 1.**
Consider three European call options on a stock with $S_0 = 100$, $r = 3\%$, $q = 0$: (i) an ITM call with $K = 85$, $T = 0.5$, $\sigma^{\text{mkt}} = 22\%$; (ii) an ATM call with $K = 100$, $T = 0.5$, $\sigma^{\text{mkt}} = 20\%$; (iii) an OTM call with $K = 120$, $T = 0.5$, $\sigma^{\text{mkt}} = 25\%$. Compute the Black-Scholes vega $\mathcal{V} = S_0\sqrt{T}\,\phi(d_1)$ for each option and the corresponding vega weight $w = 1/\mathcal{V}^2$. Verify that the OTM option receives the largest weight and explain why this is desirable for calibration.

---

**Exercise 2.**
Using the first-order approximation $\sigma_i^{\text{mod}} - \sigma_i^{\text{mkt}} \approx (C_i^{\text{mod}} - C_i^{\text{mkt}})/\mathcal{V}_i$, show that the vega-weighted price-space objective:

$$
\mathcal{L}_{\text{vega}}(\Theta) = \sum_{i=1}^{M} \frac{1}{\mathcal{V}_i^2} (C_i^{\text{mod}} - C_i^{\text{mkt}})^2
$$

is exactly equal to the IV-space objective $\mathcal{L}_{\text{IV}}(\Theta) = \sum_i (\sigma_i^{\text{mod}} - \sigma_i^{\text{mkt}})^2$ to first order. Then give a scenario where the approximation breaks down (hint: consider large price errors or options near expiry).

---

**Exercise 3.**
A calibration uses $M = 20$ options. The optimizer finds parameters that produce model prices with a price RMSE of \$0.35 and an IVRMSE of 42 bps. Suppose you switch from uniform weights to vega weights. The new calibration yields a price RMSE of \$0.52 but an IVRMSE of 28 bps. Explain why the price RMSE increased while the IVRMSE decreased. Which metric should a volatility trader use to evaluate calibration quality, and why?

---

**Exercise 4.**
The $\kappa$-$\theta$ degeneracy means the objective function has a valley along curves where $\kappa\theta \approx \text{const}$. Suppose $\kappa\theta = 0.10$ and you consider the pairs $(\kappa, \theta) = (2.0, 0.05)$ and $(\kappa, \theta) = (5.0, 0.02)$. Both yield the same $\kappa\theta$ product. Compute the mean-reversion half-life $\tau_{1/2} = \ln(2)/\kappa$ for each case and the Feller ratio $2\kappa\theta/\xi^2$ for $\xi = 0.5$. Discuss which parameter set produces more realistic variance dynamics and what data would help distinguish between them.

---

**Exercise 5.**
Consider the Tikhonov regularization term:

$$
\mathcal{L}_{\text{reg}}(\Theta) = \mathcal{L}(\Theta) + \sum_{j=1}^{5} \lambda_j (\Theta_j - \Theta_{\text{ref},j})^2
$$

with $\Theta_{\text{ref}} = (0.04, 2.0, 0.04, 0.5, -0.70)$ and penalty weights $\lambda = (0, 10, 10, 0, 0)$. Explain why $\lambda_1 = \lambda_4 = \lambda_5 = 0$ (no penalty on $v_0$, $\xi$, $\rho$) while $\lambda_2 = \lambda_3 = 10$ (strong penalty on $\kappa$ and $\theta$). If tomorrow's unregularized calibration gives $\kappa = 5.0$ and $\theta = 0.02$ with an objective value of $\mathcal{L} = 2.0 \times 10^{-4}$, compute the total regularized objective and compare it to a stable solution $\kappa = 2.1$, $\theta = 0.039$ with $\mathcal{L} = 2.5 \times 10^{-4}$.

---

**Exercise 6.**
In the worked example, the ATM 1-year option has $\mathcal{V} = 39.10$ and a \$0.50 pricing error, while the OTM 3-month option has $\mathcal{V} = 11.98$ and a \$0.10 pricing error. Convert each pricing error to an implied volatility error using the approximation $\Delta\sigma \approx \Delta C / \mathcal{V}$. Express both in basis points and compare. Which option has a larger IV error, and does this match the relative contributions to the vega-weighted objective?

---

**Exercise 7.**
Design an objective function that combines vega weighting with bid-ask spread weighting. Propose a formula of the form:

$$
w_i = \frac{1}{\mathcal{V}_i^2} \cdot f(\sigma_i^{\text{ask}} - \sigma_i^{\text{bid}})
$$

where $f$ is a function of the IV bid-ask spread. Justify your choice of $f$ (e.g., $f(s) = 1/s^2$, $f(s) = 1/s$, or a clipped version). Discuss the trade-off: if an OTM option has a small vega (large $1/\mathcal{V}_i^2$) but a wide bid-ask spread (suggesting the market quote is unreliable), should the combined weight be large or small?
