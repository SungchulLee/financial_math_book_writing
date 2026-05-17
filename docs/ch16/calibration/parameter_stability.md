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

**1. The $\kappa$-$\theta$ degeneracy.** Short-maturity options primarily constrain $v_0$ and $\rho$. The mean-reversion speed $\kappa$ and long-run variance $\theta$ enter the short-maturity smile mainly through the product $\kappa\theta$, producing a **hyperbolic ridge** $\kappa\theta = c$ in the $(\kappa, \theta)$ plane where the objective is nearly constant. Recall (see [§ Joint Calibration Across Maturities](joint_calibration_across_maturities.md)): long-maturity data breaks this degeneracy via the $e^{-\kappa T}$ term structure.

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

---

## Exercises

**Exercise 1.**
On Day 1, a Heston calibration yields $\Theta_1^* = (0.035, 1.80, 0.045, 0.50, -0.72)$. On Day 2 (with only a 0.2 vol-point market shift), the unregularized calibration yields $\Theta_2^* = (0.036, 3.60, 0.025, 0.55, -0.69)$. Compute the product $\kappa\theta$ for each day and verify that the change in $\kappa\theta$ is small compared to the individual changes in $\kappa$ and $\theta$. Quantify the daily parameter change norm $\|\Theta_2^* - \Theta_1^*\|$ using the Euclidean metric.

??? success "Solution to Exercise 1"
    **Day 1:** $\kappa\theta = 1.80 \times 0.045 = 0.0810$

    **Day 2:** $\kappa\theta = 3.60 \times 0.025 = 0.0900$

    Change in $\kappa\theta$: $|0.0900 - 0.0810| = 0.0090$, a relative change of $0.0090/0.0810 = 11.1\%$.

    Individual changes:

    - $\kappa$: $|3.60 - 1.80| = 1.80$, relative change $1.80/1.80 = 100\%$
    - $\theta$: $|0.025 - 0.045| = 0.020$, relative change $0.020/0.045 = 44.4\%$

    The product $\kappa\theta$ changed by only 11%, while $\kappa$ doubled (100% change) and $\theta$ decreased by 44%. This confirms the $\kappa$-$\theta$ ridge: the optimizer moved along the hyperbola $\kappa\theta \approx \text{const}$ in the $(\kappa, \theta)$ plane, producing large individual parameter changes with only a small change in the observable quantity $\kappa\theta$.

    **Euclidean parameter change norm:**

    $$
    \|\Theta_2^* - \Theta_1^*\| = \sqrt{(0.036 - 0.035)^2 + (3.60 - 1.80)^2 + (0.025 - 0.045)^2 + (0.55 - 0.50)^2 + (-0.69 - (-0.72))^2}
    $$

    $$
    = \sqrt{(0.001)^2 + (1.80)^2 + (-0.020)^2 + (0.05)^2 + (0.03)^2}
    $$

    $$
    = \sqrt{10^{-6} + 3.24 + 4 \times 10^{-4} + 2.5 \times 10^{-3} + 9 \times 10^{-4}}
    $$

    $$
    = \sqrt{3.2439} = 1.801
    $$

    The norm is dominated by the $\kappa$ change ($1.80^2 = 3.24$ accounts for $99.9\%$ of the squared norm). This highlights that the Euclidean norm is sensitive to parameter scale; in practice, one should use a normalized or weighted norm that accounts for the different magnitudes of the parameters.

---

**Exercise 2.**
The Gauss-Newton approximation of the Hessian is $H \approx 2 J^\top W J$, where $J$ is the $M \times 5$ Jacobian. Suppose $M = 30$ options and the Jacobian has singular values $s_1 = 12, s_2 = 8, s_3 = 5, s_4 = 0.8, s_5 = 0.05$. Compute the eigenvalues of $J^\top J$ (which are $s_j^2$), the condition number $\kappa(H)$, and the approximate 95% confidence interval half-width for the parameter corresponding to the smallest singular value, assuming $\mathcal{L}(\Theta^*) = 2.0 \times 10^{-4}$, unit weights, and $M - 5 = 25$.

??? success "Solution to Exercise 2"
    **Eigenvalues of $J^\top J$:** The eigenvalues are the squares of the singular values:

    $$
    \lambda_j(J^\top J) = s_j^2: \quad 144, \; 64, \; 25, \; 0.64, \; 0.0025
    $$

    The Hessian eigenvalues (under the Gauss-Newton approximation with unit weights) are $\lambda_j(H) = 2 s_j^2$:

    $$
    288, \; 128, \; 50, \; 1.28, \; 0.005
    $$

    **Condition number:**

    $$
    \kappa(H) = \frac{\lambda_{\max}}{\lambda_{\min}} = \frac{288}{0.005} = 57{,}600
    $$

    This is a severely ill-conditioned problem, indicating that one parameter direction is approximately 58,000 times less constrained than the best-identified direction.

    **Approximate 95% confidence interval for the worst-identified parameter:** The parameter covariance matrix is:

    $$
    \text{Cov}(\Theta^*) \approx \frac{\mathcal{L}(\Theta^*)}{M - 5} H^{-1}
    $$

    For the parameter corresponding to the smallest eigenvalue (the least-identified direction):

    $$
    [\text{Cov}(\Theta^*)]_{55} \approx \frac{\mathcal{L}(\Theta^*)}{(M-5) \cdot \lambda_5(H)} = \frac{2.0 \times 10^{-4}}{25 \times 0.005} = \frac{2.0 \times 10^{-4}}{0.125} = 1.6 \times 10^{-3}
    $$

    The 95% confidence interval half-width is:

    $$
    1.96 \sqrt{1.6 \times 10^{-3}} = 1.96 \times 0.0400 = 0.0784
    $$

    If this direction corresponds to $\kappa$ (which typically has magnitude $\sim 2$), the 95% confidence interval is $\kappa \pm 0.078$, or $\pm 3.9\%$ relative uncertainty. If it corresponds to $\theta$ (magnitude $\sim 0.04$), the interval is $\theta \pm 0.078$, meaning $\theta$ is essentially unconstrained. In practice, the smallest eigenvalue direction is typically a linear combination of $\kappa$ and $\theta$ (the $\kappa$-$\theta$ ridge direction), and the confidence interval spans a long segment of the degeneracy hyperbola.

---

**Exercise 3.**
Consider the Tikhonov-regularized objective:

$$
\mathcal{L}_{\text{reg}}(\Theta) = \mathcal{L}(\Theta) + \sum_{j=1}^{5} \lambda_j (\Theta_j - \Theta_{\text{ref},j})^2
$$

with $\Theta_{\text{ref}} = (0.040, 2.10, 0.039, 0.40, -0.70)$ and weights $\lambda = (0.01, 0.5, 0.5, 0.1, 0.01)$. If the unregularized minimum is at $\Theta^* = (0.041, 4.50, 0.020, 0.45, -0.68)$, compute the regularization penalty and compare it to a typical unregularized loss of $\mathcal{L} = 2.6 \times 10^{-4}$. Discuss whether the penalty is large enough to shift the regularized minimum away from the unregularized one.

??? success "Solution to Exercise 3"
    **Regularization penalty at the unregularized minimum $\Theta^* = (0.041, 4.50, 0.020, 0.45, -0.68)$:**

    | $j$ | $\Theta_j^*$ | $\Theta_{\text{ref},j}$ | $\Delta\Theta_j$ | $\lambda_j$ | $\lambda_j (\Delta\Theta_j)^2$ |
    |---|---|---|---|---|---|
    | $v_0$ | 0.041 | 0.040 | 0.001 | 0.01 | $10^{-8}$ |
    | $\kappa$ | 4.50 | 2.10 | 2.40 | 0.5 | $0.5 \times 5.76 = 2.88$ |
    | $\theta$ | 0.020 | 0.039 | $-0.019$ | 0.5 | $0.5 \times 3.61 \times 10^{-4} = 1.805 \times 10^{-4}$ |
    | $\xi$ | 0.45 | 0.40 | 0.05 | 0.1 | $0.1 \times 0.0025 = 2.5 \times 10^{-4}$ |
    | $\rho$ | $-0.68$ | $-0.70$ | 0.02 | 0.01 | $0.01 \times 4 \times 10^{-4} = 4 \times 10^{-6}$ |

    Total penalty: $\approx 2.88 + 1.805 \times 10^{-4} + 2.5 \times 10^{-4} + \text{negligible} \approx 2.880$

    The penalty is dominated by the $\kappa$ term ($2.88$), which is enormous compared to the base loss $\mathcal{L} = 2.6 \times 10^{-4}$. The ratio is:

    $$
    \frac{\text{penalty}}{\mathcal{L}} = \frac{2.88}{2.6 \times 10^{-4}} \approx 11{,}077
    $$

    The penalty exceeds the base loss by more than four orders of magnitude. This means the regularized optimizer will never choose $\kappa = 4.50$ --- the penalty for deviating from $\kappa_{\text{ref}} = 2.10$ far outweighs any improvement in fit quality. The regularized minimum will lie much closer to $\Theta_{\text{ref}}$, with $\kappa$ moving only slightly from 2.10 to accommodate the small change in market data.

    The regularization weights $\lambda_\kappa = \lambda_\theta = 0.5$ are effective at controlling the $\kappa$-$\theta$ instability, while $\lambda_{v_0} = \lambda_\rho = 0.01$ allows these well-identified parameters to track the market freely.

---

**Exercise 4.**
Explain the L-curve method for choosing the regularization strength $\lambda$. Sketch the expected shape of the L-curve (parameter change on one axis, fit quality on the other) for Heston calibration. What happens at the two extremes: $\lambda \to 0$ and $\lambda \to \infty$? If the L-curve corner occurs at $\lambda = 0.3$ with IVRMSE $= 0.30$ vol points and parameter change norm $= 0.20$, while $\lambda = 0.1$ gives IVRMSE $= 0.27$ and norm $= 0.95$, which would you choose for a hedging application?

??? success "Solution to Exercise 4"
    **The L-curve method:** Plot the parameter change norm $\|\Theta^*(\lambda) - \Theta_{\text{ref}}\|$ on the horizontal axis and the fit quality $\mathcal{L}(\Theta^*(\lambda))$ (or equivalently IVRMSE) on the vertical axis, for a range of $\lambda$ values.

    **Shape of the L-curve:**

    - **$\lambda \to 0$ (no regularization):** The optimizer is free to minimize $\mathcal{L}$ without constraint. The fit quality is optimal (IVRMSE is minimized), but the parameter change can be large (the point lies far to the right on the horizontal axis).
    - **$\lambda \to \infty$ (full regularization):** The optimizer is forced to stay at $\Theta_{\text{ref}}$, so the parameter change is zero (the point is at the left edge), but the fit quality can be poor since $\Theta_{\text{ref}}$ may not match today's market.
    - **Intermediate $\lambda$:** As $\lambda$ increases from 0, the parameter change decreases rapidly at first (moving left) with only a small loss in fit quality. Beyond a critical point, further increases in $\lambda$ yield diminishing reductions in parameter change while the fit quality deteriorates sharply.

    The resulting curve is L-shaped, with the corner representing the best trade-off between stability and fit quality.

    **Choosing between the two candidates:**

    - $\lambda = 0.3$: IVRMSE $= 0.30$ vol points, parameter change norm $= 0.20$
    - $\lambda = 0.1$: IVRMSE $= 0.27$ vol points, parameter change norm $= 0.95$

    For a hedging application, **$\lambda = 0.3$ is strongly preferred**. The reasoning:

    1. The fit quality difference is only 3 bps ($0.30$ vs $0.27$ vol points), which is well within typical bid-ask spreads of 5--10 bps for liquid options. This difference is imperceptible for hedging.
    2. The parameter stability improvement is dramatic: the parameter change norm drops from $0.95$ to $0.20$, a factor of nearly 5. Stable parameters produce stable Greeks, which means smoother hedge rebalancing and lower transaction costs.
    3. A parameter change norm of $0.95$ would cause noticeable jumps in model-implied Greeks, leading to erratic hedge adjustments and unpredictable P&L attribution. A norm of $0.20$ ensures smooth daily parameter evolution.

---

**Exercise 5.**
Regularization modifies the Hessian to $H_{\text{reg}} = H + 2\Lambda$ where $\Lambda = \text{diag}(\lambda_1, \ldots, \lambda_5)$. If the original Hessian has eigenvalues $(500, 120, 30, 0.8, 0.002)$ and you set $\lambda_j = 0.5$ for all $j$, compute the regularized eigenvalues and the new condition number. By what factor has the condition number improved? Discuss whether uniform regularization is appropriate given the structure of the Heston degeneracies.

??? success "Solution to Exercise 5"
    **Original eigenvalues of $H$:** $(500, 120, 30, 0.8, 0.002)$

    **Regularized eigenvalues:** $H_{\text{reg}} = H + 2\Lambda$ where $\Lambda = \text{diag}(0.5, 0.5, 0.5, 0.5, 0.5)$, so $2\Lambda = \text{diag}(1, 1, 1, 1, 1)$. The regularized eigenvalues are:

    $$
    (500 + 1, \; 120 + 1, \; 30 + 1, \; 0.8 + 1, \; 0.002 + 1) = (501, \; 121, \; 31, \; 1.8, \; 1.002)
    $$

    **Original condition number:**

    $$
    \kappa(H) = \frac{500}{0.002} = 250{,}000
    $$

    **Regularized condition number:**

    $$
    \kappa(H_{\text{reg}}) = \frac{501}{1.002} = 500.0
    $$

    **Improvement factor:**

    $$
    \frac{250{,}000}{500} = 500
    $$

    The condition number improved by a factor of 500, from a severely ill-conditioned problem to a moderately conditioned one.

    **Is uniform regularization appropriate?** Uniform regularization ($\lambda_j = 0.5$ for all $j$) is suboptimal for the Heston problem. The large eigenvalues (500, 120, 30) correspond to well-identified parameter directions that do not need regularization --- adding 1 to these eigenvalues has a negligible effect ($< 3\%$ relative change). The small eigenvalues (0.8, 0.002) correspond to poorly-identified directions (the $\kappa$-$\theta$ ridge and the $\xi$-$\rho$ valley) that need strong regularization.

    A better approach is to set $\lambda_j$ inversely proportional to the identifiability of each parameter: large $\lambda_j$ for $\kappa$ and $\theta$ (corresponding to small eigenvalues), small $\lambda_j$ for $v_0$ and $\rho$ (corresponding to large eigenvalues). For example, $\lambda = (0.01, 0.5, 0.5, 0.1, 0.01)$ would provide strong regularization where needed while minimally distorting the well-constrained parameters. This targeted approach achieves a similar condition number improvement while preserving the optimizer's ability to track market movements in the well-identified parameters.

---

**Exercise 6.**
A trading desk monitors the daily parameter change $\Delta_t = \|\Theta_t^* - \Theta_{t-1}^*\|_\Lambda$ with a 20-day rolling average. Over the past 20 days, $\Delta_t$ averages 0.15 with standard deviation 0.05. Today, $\Delta_t = 0.85$. Propose a statistical test to determine if this spike is abnormal (e.g., more than 3 standard deviations above the mean). If the spike is confirmed as abnormal, list three possible causes and the diagnostic checks you would perform for each.

??? success "Solution to Exercise 6"
    **Statistical test:** The z-score for today's observation is:

    $$
    z = \frac{\Delta_t - \bar{\Delta}}{\sigma_{\Delta}} = \frac{0.85 - 0.15}{0.05} = \frac{0.70}{0.05} = 14.0
    $$

    This is 14 standard deviations above the mean, far exceeding the 3-sigma threshold. Under a normal approximation, the probability of observing $z \geq 14$ is effectively zero ($< 10^{-44}$). Even allowing for non-normality and heavy tails in the distribution of $\Delta_t$, a 14-sigma event is unambiguously abnormal.

    **Three possible causes and diagnostic checks:**

    **Cause 1: Genuine market regime change** (e.g., a volatility event, central bank announcement, or market crash). Diagnostics:

    - Check whether the market IV surface has shifted by significantly more than the 20-day average daily shift. If the surface moved by several vol points (compared to a typical 0.2--0.5 vol-point daily move), the large parameter change may be the correct model response.
    - Verify that the IVRMSE is comparable to recent values --- if the model still fits well, the parameter shift is driven by genuine market dynamics.
    - Check VIX or realized volatility for confirmation of an elevated regime.

    **Cause 2: Calibration instability** (the optimizer found a different basin on the objective function landscape). Diagnostics:

    - Rerun the calibration multiple times with different random seeds. If the results are inconsistent across runs, the optimizer is exploring multiple basins and the result is seed-dependent.
    - Check whether $\kappa\theta$ and $\rho\xi$ products changed significantly, or only the individual parameters. If the products are stable but individual parameters shifted, the optimizer is wandering along a degeneracy ridge.
    - Increase the regularization strength $\lambda$ and rerun. If the parameters snap back to near yesterday's values with minimal loss in fit quality, the original jump was due to the flat objective landscape.

    **Cause 3: Bad market data** (stale quotes, data feed errors, missing options). Diagnostics:

    - Inspect the raw market IV surface for anomalies: missing maturities, discontinuous smiles, negative butterfly spreads, or calendar spread violations.
    - Compare today's surface to yesterday's and flag any options where the IV changed by more than 3 times the typical daily move.
    - Check the number of calibration instruments $M$ --- if options were dropped or added (e.g., due to an expiry rollover), the calibration may respond to a changed input set rather than changed prices.
    - Rerun calibration after removing the suspected bad data points and check whether the parameter spike disappears.

---

**Exercise 7.**
Consider two parameter sets that lie on the $\kappa$-$\theta$ ridge: $\Theta_A = (0.04, 2.0, 0.05, 0.45, -0.70)$ and $\Theta_B = (0.04, 5.0, 0.02, 0.45, -0.70)$. Both have $\kappa\theta = 0.10$. Compute the expected average variance $\bar{v}(T)$ for both parameter sets at $T = 0.25$ and $T = 2.0$ using:

$$
\bar{v}(T) = \theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}
$$

Show that $\bar{v}(0.25)$ is similar for both but $\bar{v}(2.0)$ differs significantly. Conclude that long-maturity options break the $\kappa$-$\theta$ degeneracy.

??? success "Solution to Exercise 7"
    **Computing $\bar{v}(T)$ for both parameter sets:**

    The formula is $\bar{v}(T) = \theta + (v_0 - \theta)\frac{1 - e^{-\kappa T}}{\kappa T}$ with $v_0 = 0.04$ for both.

    **$\Theta_A = (v_0=0.04, \kappa=2.0, \theta=0.05)$:**

    At $T = 0.25$: $\kappa T = 0.5$

    $$
    \frac{1 - e^{-0.5}}{0.5} = \frac{1 - 0.6065}{0.5} = \frac{0.3935}{0.5} = 0.7870
    $$

    $$
    \bar{v}_A(0.25) = 0.05 + (0.04 - 0.05)(0.7870) = 0.05 - 0.00787 = 0.04213
    $$

    At $T = 2.0$: $\kappa T = 4.0$

    $$
    \frac{1 - e^{-4.0}}{4.0} = \frac{1 - 0.01832}{4.0} = \frac{0.98168}{4.0} = 0.24542
    $$

    $$
    \bar{v}_A(2.0) = 0.05 + (0.04 - 0.05)(0.24542) = 0.05 - 0.002454 = 0.04755
    $$

    **$\Theta_B = (v_0=0.04, \kappa=5.0, \theta=0.02)$:**

    At $T = 0.25$: $\kappa T = 1.25$

    $$
    \frac{1 - e^{-1.25}}{1.25} = \frac{1 - 0.2865}{1.25} = \frac{0.7135}{1.25} = 0.5708
    $$

    $$
    \bar{v}_B(0.25) = 0.02 + (0.04 - 0.02)(0.5708) = 0.02 + 0.01142 = 0.03142
    $$

    At $T = 2.0$: $\kappa T = 10.0$

    $$
    \frac{1 - e^{-10.0}}{10.0} = \frac{1 - 0.0000454}{10.0} = \frac{0.99995}{10.0} = 0.09999
    $$

    $$
    \bar{v}_B(2.0) = 0.02 + (0.04 - 0.02)(0.09999) = 0.02 + 0.002000 = 0.02200
    $$

    **Summary:**

    | | $\bar{v}(0.25)$ | $\sigma_{\text{ATM}}(0.25)$ | $\bar{v}(2.0)$ | $\sigma_{\text{ATM}}(2.0)$ |
    |---|---|---|---|---|
    | $\Theta_A$ ($\kappa=2, \theta=0.05$) | 0.04213 | 20.53% | 0.04755 | 21.81% |
    | $\Theta_B$ ($\kappa=5, \theta=0.02$) | 0.03142 | 17.73% | 0.02200 | 14.83% |

    At $T = 0.25$, the two parameter sets already show a notable difference ($20.53\%$ vs $17.73\%$, about 280 bps), though both are in a plausible range. At $T = 2.0$, the difference is dramatic: $21.81\%$ vs $14.83\%$, a spread of nearly 700 bps. This is because $\Theta_A$ has $v_0 < \theta$, so $\bar{v}(T)$ increases toward $\theta = 0.05$, while $\Theta_B$ has $v_0 > \theta$, so $\bar{v}(T)$ decreases toward $\theta = 0.02$.

    **Conclusion:** Even though both parameter sets share $\kappa\theta = 0.10$ and are nearly indistinguishable from short-maturity data alone, their long-maturity predictions diverge sharply. The 2-year ATM implied volatility provides a clear discriminant between the two. Long-maturity options break the $\kappa$-$\theta$ degeneracy because $\kappa$ controls the rate of convergence to $\theta$: a fast mean-reversion ($\kappa = 5$) means the 2-year average variance is essentially $\theta$ (since $e^{-\kappa T} \approx 0$), while a slow mean-reversion ($\kappa = 2$) means the initial variance $v_0$ still has significant influence. The market's 2-year ATM volatility directly reveals which scenario is correct.
