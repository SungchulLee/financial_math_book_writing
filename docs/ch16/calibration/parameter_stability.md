# Parameter Stability and Identifiability

A calibration procedure that produces excellent fits today but wildly different parameters tomorrow is useless for hedging. If $\kappa$ jumps from 2.0 to 5.0 overnight despite stable market conditions, the model-implied Greeks change discontinuously and the hedge P&L suffers large, unexplained swings. **Parameter stability**---the requirement that calibrated parameters evolve smoothly through time---is therefore as important as fit quality. This section analyzes the sources of instability, develops regularization techniques to control it, and examines the deeper issue of **identifiability**: which parameters can the market data actually determine?

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Identify the sources of day-to-day parameter instability in Heston calibration
    2. Formulate Tikhonov regularization with temporal penalties and choose the regularization strength
    3. Analyze parameter identifiability through the Hessian eigenvalue structure
    4. Explain the $\kappa$-$\theta$ and $\xi$-$\rho$ degeneracies and their practical consequences

!!! tip "Prerequisites"
    This section builds on the [objective function design](objective_function_design.md), the [differential evolution](differential_evolution.md) optimizer, and the [Heston SDE and parameters](../model_definition/heston_sde_and_parameters.md).

---

## Sources of Parameter Instability

Even when the market-implied volatility surface changes by only a few basis points overnight, the calibrated Heston parameters can shift significantly. Three mechanisms drive this instability.

### Objective Function Flatness

The calibration objective $\mathcal{L}(\Theta)$ has regions where the gradient is small and the Hessian has near-zero eigenvalues. In these flat regions, many parameter combinations produce nearly identical objective values. Small changes in market data shift the minimum along the flat direction, causing large parameter movements with negligible improvement in fit quality.

### Parameter Degeneracies

The Heston model has two well-known degeneracies:

**1. The $\kappa$-$\theta$ degeneracy.** Short-maturity options primarily constrain the initial variance $v_0$ and the correlation $\rho$. The mean-reversion speed $\kappa$ and long-run variance $\theta$ enter the short-maturity smile mainly through the product $\kappa\theta$. Given short-maturity data alone, the contour $\kappa\theta = c$ forms a **hyperbolic ridge** in the $(\kappa, \theta)$ plane where the objective function is nearly constant. Adding long-maturity data breaks this degeneracy, since $\kappa$ separately controls the time scale of variance mean-reversion.

**2. The $\xi$-$\rho$ interaction.** Both the vol-of-vol $\xi$ and the correlation $\rho$ affect the implied volatility skew. Increasing $|\rho|$ steepens the skew, and increasing $\xi$ adds curvature (smile convexity). These effects partially compensate: a model with $(\xi = 0.3, \rho = -0.8)$ can produce a similar skew to one with $(\xi = 0.5, \rho = -0.6)$. The near-degeneracy creates an elongated valley in the $(\xi, \rho)$ subspace.

### Noise Amplification

Market option prices contain noise from bid-ask spreads, stale quotes, and microstructure effects. When the objective function has flat directions, the optimizer responds to this noise by moving along the flat direction---producing parameter changes that reflect noise rather than genuine market movements.

---

## Quantifying Identifiability via the Hessian

The local curvature of the objective function at the minimum determines how precisely each parameter can be identified.

### Hessian and Fisher Information

At the calibrated minimum $\Theta^*$, the Hessian matrix $H$ has entries:

$$
H_{jk} = \frac{\partial^2 \mathcal{L}}{\partial \Theta_j \, \partial \Theta_k} \bigg|_{\Theta = \Theta^*}
$$

For a least-squares objective $\mathcal{L} = \sum_i w_i e_i^2$ with residuals $e_i(\Theta) = \sigma_i^{\text{mod}}(\Theta) - \sigma_i^{\text{mkt}}$, the Gauss-Newton approximation gives:

$$
H \approx 2 \, J^\top W J
$$

where $J$ is the $M \times 5$ Jacobian matrix with entries $J_{ij} = \partial e_i / \partial \Theta_j$ and $W = \text{diag}(w_1, \ldots, w_M)$.

### Eigenvalue Analysis

The eigenvalues $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_5 > 0$ of $H$ quantify the curvature along the principal directions. The **condition number** $\kappa(H) = \lambda_1 / \lambda_5$ measures the ratio of the steepest to flattest direction.

- **Well-identified parameter combinations** correspond to eigenvectors with large eigenvalues: the objective changes rapidly when moving in these directions, so the minimum is sharply defined.
- **Poorly-identified combinations** correspond to small eigenvalues: the objective is flat, and the minimum is determined more by regularization or noise than by market data.

For typical Heston calibrations, $\kappa(H)$ ranges from $10^3$ to $10^6$, indicating severe ill-conditioning. The smallest eigenvalue direction is typically aligned with the $\kappa$-$\theta$ ridge.

### Approximate Confidence Intervals

Under a Gaussian approximation to the objective function near the minimum, the parameter covariance matrix is:

$$
\text{Cov}(\Theta^*) \approx \frac{\mathcal{L}(\Theta^*)}{M - 5} \, H^{-1}
$$

The approximate $95\%$ confidence interval for parameter $\Theta_j$ is:

$$
\Theta_j^* \pm 1.96 \sqrt{[\text{Cov}(\Theta^*)]_{jj}}
$$

Large confidence intervals signal poor identifiability. In practice, $\kappa$ often has a confidence interval spanning $\pm 50\%$ or more of its calibrated value, confirming the $\kappa$-$\theta$ degeneracy.

---

## Tikhonov Regularization

Regularization adds a penalty term to the objective function that discourages large deviations from a reference parameter set, effectively smoothing the calibration over time.

### Standard Formulation

The **Tikhonov-regularized objective** is:

$$
\mathcal{L}_{\text{reg}}(\Theta) = \mathcal{L}(\Theta) + \lambda \| \Theta - \Theta_{\text{ref}} \|_{\Lambda}^2
$$

where $\Theta_{\text{ref}}$ is the reference parameter vector, $\Lambda$ is a positive-definite weighting matrix, and $\| x \|_{\Lambda}^2 = x^\top \Lambda \, x$. In the simplest case $\Lambda = I$:

$$
\mathcal{L}_{\text{reg}}(\Theta) = \mathcal{L}(\Theta) + \lambda \sum_{j=1}^{5} (\Theta_j - \Theta_{\text{ref},j})^2
$$

### Choice of Reference

The most common choices for $\Theta_{\text{ref}}$ are:

1. **Yesterday's calibration**: $\Theta_{\text{ref}} = \Theta_{t-1}^*$. This enforces temporal smoothness, preventing large day-to-day jumps.
2. **Historical average**: $\Theta_{\text{ref}} = \bar{\Theta}$, the average of calibrated parameters over a lookback window. This anchors parameters to their typical values.
3. **Expert prior**: $\Theta_{\text{ref}}$ set to economically reasonable values (e.g., $\kappa = 2$, $\theta = 0.04$, $\rho = -0.7$).

### Parameter-Specific Penalties

Different parameters have different scales and different degrees of identifiability. A diagonal weighting matrix $\Lambda = \text{diag}(\lambda_1, \ldots, \lambda_5)$ allows parameter-specific regularization:

$$
\mathcal{L}_{\text{reg}}(\Theta) = \mathcal{L}(\Theta) + \sum_{j=1}^{5} \lambda_j (\Theta_j - \Theta_{\text{ref},j})^2
$$

Guidelines:

- **Large $\lambda_j$** for poorly identified parameters ($\kappa$, $\theta$): anchors them to the reference, preventing wild swings along the degeneracy ridge
- **Small $\lambda_j$** for well-identified parameters ($v_0$, $\rho$): allows the optimizer to follow market data closely
- **Moderate $\lambda_j$** for $\xi$: balances stability with responsiveness to smile shape changes

### Choosing the Regularization Strength

The regularization strength $\lambda$ trades off fit quality against stability. Too large: the calibrated parameters stay near the reference regardless of market data, and the fit deteriorates. Too small: no regularization effect, and instability returns.

A practical procedure is the **L-curve method**: plot $\| \Theta^*(\lambda) - \Theta_{\text{ref}} \|$ (parameter change) against $\mathcal{L}(\Theta^*(\lambda))$ (fit quality) for a range of $\lambda$ values. The curve is typically L-shaped, and the corner of the L identifies the $\lambda$ that achieves the best trade-off.

!!! note "Effect on the Hessian"
    Regularization shifts the Hessian eigenvalues: $H_{\text{reg}} = H + 2\lambda\Lambda$. This increases the smallest eigenvalue from $\lambda_5$ to $\lambda_5 + 2\lambda\lambda_{\min}(\Lambda)$, improving the condition number. The regularized problem is strictly convex when $\lambda$ is large enough, guaranteeing a unique minimum.

---

## Temporal Stability Metrics

To monitor parameter stability in production, track the following metrics daily.

### Parameter Variation Norms

The **daily parameter change** (in a suitable norm) is:

$$
\Delta_t = \| \Theta_t^* - \Theta_{t-1}^* \|_{\Lambda}
$$

A well-regularized calibration produces $\Delta_t$ values that are small relative to the parameter magnitudes. Spikes in $\Delta_t$ indicate either a genuine regime change or a calibration instability that requires investigation.

### Explained vs Unexplained Variation

Decompose the parameter change into a component explained by changes in market data and an unexplained residual:

$$
\Delta \Theta_t \approx -H^{-1} \nabla_{\Theta} \mathcal{L}_t \bigg|_{\Theta = \Theta_{t-1}^*}
$$

The explained change reflects the optimizer's response to genuine market movements. The residual $\Theta_t^* - \Theta_{t-1}^* - \Delta\Theta_t$ reveals instability from noise or degeneracy.

---

## Worked Example

Consider two consecutive days of Heston calibration to SPX options.

**Day 1**: The unregularized calibration (using DE + Nelder-Mead) produces $\Theta_1^* = (v_0, \kappa, \theta, \xi, \rho) = (0.040, 2.10, 0.039, 0.40, -0.70)$ with IVRMSE = 0.28 vol points.

**Day 2**: Market IV shifts by approximately 0.3 vol points across the surface. The unregularized calibration gives $\Theta_2^* = (0.041, 4.50, 0.020, 0.45, -0.68)$ with IVRMSE = 0.26 vol points.

The fit improved marginally (0.28 to 0.26 vol points), but $\kappa$ jumped from 2.10 to 4.50 and $\theta$ fell from 0.039 to 0.020. The product $\kappa\theta$ changed only from 0.082 to 0.090---confirming the $\kappa$-$\theta$ ridge.

**Day 2 (regularized)**: With $\Theta_{\text{ref}} = \Theta_1^*$, $\lambda_{\kappa} = 0.5$, $\lambda_{\theta} = 0.5$, $\lambda_{\xi} = 0.1$, $\lambda_{v_0} = \lambda_{\rho} = 0.01$, the regularized calibration gives $\Theta_2^{\text{reg}} = (0.041, 2.25, 0.037, 0.42, -0.69)$ with IVRMSE = 0.29 vol points.

The fit is 0.03 vol points worse (imperceptible for hedging), but the parameters moved smoothly. The daily parameter change norm dropped from 2.43 (unregularized) to 0.18 (regularized).

---

## Summary

Parameter stability is not a luxury---it is a requirement for consistent hedging and risk management. The Heston model's $\kappa$-$\theta$ and $\xi$-$\rho$ degeneracies create flat directions in the calibration objective where the optimizer is free to wander. Tikhonov regularization with parameter-specific weights $\lambda_j$ penalizes deviations from a temporal reference, effectively lifting the flat directions and producing smooth parameter trajectories. The Hessian eigenvalue analysis provides a quantitative diagnostic: large condition numbers signal identifiability problems that regularization should address, and approximate confidence intervals indicate which parameters are genuinely constrained by market data.
