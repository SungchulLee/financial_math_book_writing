# Trade-Off Between Fit and Robustness


Regularization introduces an unavoidable **trade-off**: improving robustness and stability typically worsens in-sample fit. Understanding and managing this trade-off is central to practical calibration.

---

## Bias–variance trade-off


Recall (see [§ Statistical Learning in Financial Models](../../ch24/statistical_learning_in_financial_models/bias_variance_trade_off.md)) the bias–variance decomposition. In a calibration context, regularization reduces variance at the cost of bias: low $\lambda$ gives an excellent fit with poor stability, while high $\lambda$ gives stable but biased parameters. The optimal point depends on data quality, model purpose, and downstream use (pricing vs hedging).

---

## Diagnostics for the trade-off


Useful diagnostics include:

- **Residual plots:** detect systematic misfit patterns.
- **Parameter paths:** track parameters as regularization increases.
- **Stability tests:** re-calibrate under perturbed data.
- **Out-of-sample instruments:** test predictive power.

---

## Economic versus statistical fit


A statistically optimal fit may be economically undesirable — parameters may imply implausible dynamics, hedging Greeks may be unstable, and scenario sensitivities may explode (see [§ Model Risk from Calibration](../model_risk_from_calibration/impact_on_greeks_and_hedging.md)). Robust calibration prioritizes *economic behavior* over minimal residuals.

---

## Time stability as a criterion


In practice, many desks judge calibration quality by:

- day-to-day parameter stability,
- smooth evolution over time,
- absence of large jumps without market justification.

This implicitly favors stronger regularization than pure in-sample metrics.

---

## Choosing robustness deliberately


Guiding principles:

- start with strong regularization,
- relax only when justified by stable, liquid data,
- prefer bias you understand to variance you cannot hedge.

For a worst-case formulation of "bias you understand," see [§ Distributionally Robust Optimization](../../ch24/learning_under_model_uncertainty/distributionally_robust_optimization.md).

---

## Key takeaways


- Perfect fit is not the goal; *robust behavior* is.
- Regularization controls the fit–robustness balance.
- Stability across time and scenarios is often the decisive metric.

---

## Further reading


- Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*.
- Tarantola, *Inverse Problem Theory*.
- Andersen & Piterbarg, practitioner discussions on calibration stability.

---

## Exercises

**Exercise 1.** Define the bias-variance trade-off for a regularized calibration estimator $\hat{\theta}_\lambda$. Write down the mean squared error decomposition

$$
\text{MSE}(\hat{\theta}_\lambda) = \text{Bias}^2(\hat{\theta}_\lambda) + \text{Var}(\hat{\theta}_\lambda)
$$

and explain qualitatively how each term depends on $\lambda$. Sketch the bias, variance, and MSE as functions of $\lambda$.

??? success "Solution to Exercise 1"
    Let $\theta^*$ denote the true parameter and $\hat{\theta}_\lambda$ the regularized estimator based on noisy data $y = F(\theta^*) + \epsilon$. The **mean squared error** decomposes as

    $$
    \text{MSE}(\hat{\theta}_\lambda) = \mathbb{E}\bigl[\|\hat{\theta}_\lambda - \theta^*\|^2\bigr] = \|\text{Bias}(\hat{\theta}_\lambda)\|^2 + \operatorname{tr}\bigl(\text{Var}(\hat{\theta}_\lambda)\bigr)
    $$

    where

    $$
    \text{Bias}(\hat{\theta}_\lambda) = \mathbb{E}[\hat{\theta}_\lambda] - \theta^*
    $$

    $$
    \text{Var}(\hat{\theta}_\lambda) = \mathbb{E}\bigl[(\hat{\theta}_\lambda - \mathbb{E}[\hat{\theta}_\lambda])(\hat{\theta}_\lambda - \mathbb{E}[\hat{\theta}_\lambda])^\top\bigr]
    $$

    **Dependence on $\lambda$:**

    - **Bias** is an increasing function of $\lambda$. At $\lambda = 0$, the estimator is unbiased (assuming the model is correctly specified). As $\lambda$ grows, the estimator is pulled toward the prior $\theta_0$, introducing bias $\mathbb{E}[\hat{\theta}_\lambda] - \theta^* \approx \lambda B(\theta_0 - \theta^*)$ for some matrix $B$.

    - **Variance** is a decreasing function of $\lambda$. At $\lambda = 0$, the unregularized estimator has maximum variance (especially along directions with small singular values). As $\lambda$ increases, the filter factors $\sigma_i^2/(\sigma_i^2 + \lambda)$ shrink, damping the noisy components and reducing variance.

    - **MSE** is the sum of the two. It starts at the unregularized variance (high), initially decreases as the variance reduction outweighs the bias increase, reaches a minimum at some optimal $\lambda^*$, and then increases as the bias dominates.

    Qualitative sketch (as functions of $\lambda$):

    - $\text{Bias}^2$: starts at 0, increases monotonically, concave up.
    - $\text{Var}$: starts high, decreases monotonically, convex up, approaches 0.
    - $\text{MSE}$: U-shaped curve with minimum at $\lambda^*$.

    The optimal $\lambda^*$ that minimizes MSE is the one that achieves the best trade-off, and it generally depends on the unknown $\theta^*$, which is why practical methods (cross-validation, L-curve) are needed.

---

**Exercise 2.** A practitioner calibrates a Heston model with $\lambda = 0$ (no regularization) and $\lambda = 1.0$ (strong regularization toward yesterday's parameters). The in-sample RMSE is 0.15 vol points and 0.45 vol points respectively. The out-of-sample RMSE (next-day prediction) is 0.85 vol points and 0.52 vol points respectively. Interpret these results in terms of the bias-variance trade-off. Which $\lambda$ would you recommend for hedging purposes?

??? success "Solution to Exercise 2"
    **Results summary:**

    | | $\lambda = 0$ | $\lambda = 1.0$ |
    |---|---|---|
    | In-sample RMSE | 0.15 vol pts | 0.45 vol pts |
    | Out-of-sample RMSE | 0.85 vol pts | 0.52 vol pts |

    **Interpretation:**

    - $\lambda = 0$ achieves excellent in-sample fit (0.15 vol points) but poor out-of-sample prediction (0.85 vol points). The large gap of 0.70 vol points between in-sample and out-of-sample is a classic sign of **overfitting**: the model fits noise in today's data that is not present tomorrow. This is the high-variance regime.

    - $\lambda = 1.0$ has worse in-sample fit (0.45 vol points), reflecting the **bias** introduced by pulling parameters toward yesterday's values. However, the out-of-sample RMSE (0.52 vol points) is substantially better than the unregularized case, and the gap between in-sample and out-of-sample is only 0.07 vol points, indicating much more **stable** and generalizable parameters.

    **Recommendation for hedging:** $\lambda = 1.0$ is clearly preferable for hedging purposes, for several reasons:

    1. **Hedging requires prediction.** Greeks and hedge ratios depend on the model's ability to predict option value changes, which is an out-of-sample task. The 0.52 RMSE out-of-sample is far superior to 0.85.

    2. **Stability of Greeks.** Overfitted parameters fluctuate wildly day-to-day, causing hedging P&L noise from frequent rebalancing. The regularized calibration produces more stable parameters and hence smoother Greeks.

    3. **The in-sample cost is acceptable.** The 0.45 vol point in-sample residual is well within typical bid-ask spreads (often 0.5--1.0 vol points for equity index options), so the model still fits within market uncertainty.

    One might also consider intermediate values of $\lambda$ to find the minimum out-of-sample RMSE, which could be even lower.

---

**Exercise 3.** Design a cross-validation procedure to select $\lambda$ for Tikhonov-regularized Heston calibration. Describe: (a) how to partition the 40 available vanilla option quotes into training and validation sets, (b) the metric to optimize on the validation set, and (c) how to handle the fact that different partitions may yield different optimal $\lambda$ values.

??? success "Solution to Exercise 3"
    **(a) Partitioning the option quotes:**

    With 40 vanilla option quotes, a suitable cross-validation scheme is **leave-one-out** (LOO) or **$k$-fold** cross-validation.

    - **Leave-one-out:** For each $i = 1, \ldots, 40$, calibrate on the remaining 39 quotes and predict the held-out quote $i$. This gives 40 validation residuals.

    - **5-fold:** Randomly partition the 40 quotes into 5 groups of 8. For each fold, calibrate on 32 quotes and evaluate on 8.

    An important practical consideration: the partition should be **stratified** to ensure each fold contains quotes from different strikes and maturities. Removing all quotes at one maturity creates an extrapolation problem rather than an interpolation test.

    **(b) Metric to optimize:**

    The validation metric should be the **root mean squared prediction error** on the held-out set:

    $$
    \text{RMSPE}(\lambda) = \sqrt{\frac{1}{|V|}\sum_{i \in V} \bigl(C_{\text{model}}(\hat{\theta}_\lambda^{(-V)}; K_i, T_i) - C_i^{\text{obs}}\bigr)^2}
    $$

    where $\hat{\theta}_\lambda^{(-V)}$ is the Tikhonov estimate calibrated without the validation set $V$. Alternatively, one can use vega-weighted or implied-volatility-space errors for better interpretability.

    The optimal $\lambda$ minimizes this metric:

    $$
    \lambda^* = \arg\min_\lambda \text{RMSPE}(\lambda)
    $$

    **(c) Handling variability across partitions:**

    Different $k$-fold partitions may yield different optimal $\lambda$ values. To address this:

    1. **Repeat and average.** Perform $k$-fold CV multiple times with different random partitions (e.g., 10 repetitions of 5-fold CV). Average the RMSPE curves across all repetitions before selecting $\lambda^*$.

    2. **One-standard-error rule.** Compute the standard error of the CV estimate at each $\lambda$. Select the largest $\lambda$ whose CV error is within one standard error of the minimum. This favors more regularization (simpler model) when the evidence for a specific $\lambda$ is noisy, embodying the principle of parsimony.

    3. **Practical considerations for Heston.** Each CV fold requires a full Heston calibration, which is computationally expensive. To make this feasible: use a coarse grid of $\lambda$ values (e.g., $\lambda \in \{0.001, 0.01, 0.1, 0.5, 1.0, 5.0\}$), use warm-starting from the full-sample calibration, and consider LOO approximations using the influence function rather than exact re-calibration.

---

**Exercise 4.** Economic versus statistical fit: a calibration with $\lambda = 0$ yields $\kappa = 12.5$ and $\bar{v} = 0.001$, which implies a variance half-life of $\ln 2/12.5 \approx 0.055$ years (about 2 weeks) and long-run volatility of $\sqrt{0.001} \approx 3.2\%$. Argue that these values are economically implausible for an equity index. What range of $\kappa$ and $\bar{v}$ would you consider plausible? How would you encode these beliefs as a regularization penalty?

??? success "Solution to Exercise 4"
    The calibrated values $\kappa = 12.5$ and $\bar{v} = 0.001$ are economically implausible for an equity index:

    **Mean-reversion speed $\kappa = 12.5$:** The variance half-life is $t_{1/2} = \ln 2 / \kappa \approx 0.055$ years $\approx$ 14 trading days. This implies that any variance shock is halved within two weeks, which is far too fast. Empirically, equity index volatility exhibits persistent clustering, with half-lives on the order of months to years. The VIX, for example, can remain elevated for extended periods after market shocks.

    **Long-run variance $\bar{v} = 0.001$:** This corresponds to a long-run volatility of $\sqrt{\bar{v}} \approx 3.2\%$, which is unrealistically low. Historical equity index volatility rarely drops below 10%, and the long-run average is typically 15--25%.

    **Plausible ranges:**

    - $\kappa \in [0.5, 5.0]$, corresponding to half-lives of $0.14$ to $1.4$ years (roughly 1 month to 1.5 years).
    - $\bar{v} \in [0.01, 0.09]$, corresponding to long-run volatility of 10% to 30%.

    **Encoding as regularization penalty:** Define box-like penalties for each parameter:

    $$
    \mathcal{R}_{\text{econ}}(\theta) = \mu_1 \bigl(\kappa - \kappa_{\text{ref}}\bigr)^2 + \mu_2 \bigl(\bar{v} - \bar{v}_{\text{ref}}\bigr)^2
    $$

    with $\kappa_{\text{ref}} = 2.0$ (half-life $\approx$ 4 months) and $\bar{v}_{\text{ref}} = 0.04$ (long-run vol $\approx$ 20%). The weights $\mu_1, \mu_2$ should reflect the confidence in these priors.

    Alternatively, use a barrier penalty that becomes infinite outside the plausible range:

    $$
    \mathcal{R}_{\text{barrier}}(\theta) = -\frac{1}{t}\bigl[\log(\kappa - \kappa_{\min}) + \log(\kappa_{\max} - \kappa) + \log(\bar{v} - \bar{v}_{\min}) + \log(\bar{v}_{\max} - \bar{v})\bigr]
    $$

    This provides hard bounds while remaining differentiable, making it compatible with gradient-based optimization. A combined approach — quadratic shrinkage toward sensible defaults plus barrier constraints at economic boundaries — is often used in practice.

---

**Exercise 5.** A trading desk judges calibration quality by day-to-day parameter stability. They compute the ratio $R = \text{Var}(\Delta\theta)/\text{Var}(\Delta\text{market})$ where $\Delta\theta$ is the daily parameter change and $\Delta\text{market}$ is a market move indicator (e.g., VIX change). If $R \gg 1$, parameters are too noisy; if $R \ll 1$, they may be too sticky. Propose a target range for $R$ and describe how to adjust $\lambda$ to achieve it.

??? success "Solution to Exercise 5"
    The ratio $R = \text{Var}(\Delta\theta)/\text{Var}(\Delta\text{market})$ measures the **parameter responsiveness** relative to market moves.

    **Interpreting $R$:**

    - $R \gg 1$: Parameters fluctuate much more than justified by market moves. This indicates overfitting — the calibration is fitting noise, and day-to-day parameter changes are driven by bid-ask randomness rather than genuine market dynamics. Hedging with such parameters incurs unnecessary rebalancing costs.

    - $R \ll 1$: Parameters are too sticky and fail to track genuine market evolution. The regularization is so strong that meaningful signals are suppressed. The model becomes stale and potentially misprices during trending markets.

    - $R \approx 1$: Parameters respond proportionally to market changes — neither over-reacting to noise nor under-reacting to genuine moves.

    **Target range:** A reasonable target is $R \in [0.5, 2.0]$. The exact range depends on the parameter and market context:

    - For $v_0$ (spot variance), $R$ close to 1 is natural since $v_0$ should track VIX closely.
    - For $\kappa$ or $\bar{v}$ (structural parameters), $R$ well below 1 is acceptable since these parameters should be more stable than daily market fluctuations.

    **Adjusting $\lambda$ to achieve target $R$:**

    From the Tikhonov framework, the regularized parameter update satisfies approximately

    $$
    \Delta\hat{\theta}_\lambda \approx (H + \lambda I)^{-1} H \,\Delta\hat{\theta}_0
    $$

    where $H = A^\top W A$ is the data Hessian and $\Delta\hat{\theta}_0$ is the unregularized change. The variance ratio scales as

    $$
    R(\lambda) \approx \left\|\left(\frac{H}{H + \lambda I}\right)\right\|^2 R(0)
    $$

    To achieve a target $R^*$:

    1. Compute $R$ for the current $\lambda$ over a rolling window (e.g., 60 business days).
    2. If $R > R_{\max}$: increase $\lambda$ by a multiplicative factor, e.g., $\lambda \leftarrow \lambda \cdot (R / R^*)^{1/2}$.
    3. If $R < R_{\min}$: decrease $\lambda$ similarly.
    4. Smooth the adjustment over time to avoid abrupt changes in calibration behavior.

    This creates an adaptive feedback loop where the regularization strength self-adjusts to maintain the desired parameter responsiveness.

---

**Exercise 6.** Consider two calibration regimes: normal markets (low VIX, tight bid-ask spreads) and stressed markets (high VIX, wide spreads). Argue that the optimal regularization strength $\lambda$ should differ between these regimes. Should $\lambda$ be larger or smaller during stress? Justify your answer from both the data quality and economic perspectives.

??? success "Solution to Exercise 6"
    The optimal $\lambda$ should indeed differ between normal and stressed markets. The argument proceeds from two complementary perspectives.

    **Data quality perspective (larger $\lambda$ during stress):**

    - During stress, bid-ask spreads widen significantly (often 2--5x normal levels). This means the observation noise $\sigma_i$ is larger, so the signal-to-noise ratio in the data is lower.
    - With noisier data, the unregularized estimator has higher variance. The bias-variance trade-off shifts: more regularization is needed to compensate for the increased noise.
    - In the Bayesian interpretation, larger observation noise $\sigma^2$ implies a larger optimal $\lambda \propto \sigma^2 / \tau^2$.
    - Liquidity may also drop, meaning fewer reliable quotes are available, further increasing parameter uncertainty.

    **Economic perspective (smaller $\lambda$ during stress):**

    - During a market crash, genuine economic dynamics change rapidly. Volatility levels, skew shapes, and term structures shift substantially. The model parameters *should* move significantly to reflect the new reality.
    - Strong regularization toward yesterday's parameters would anchor the model to a pre-crisis regime, producing dangerous mispricing precisely when accurate pricing matters most.
    - Risk management during stress requires rapid adaptation — understating volatility in a crash has far more severe consequences than having noisy parameters.

    **Resolution of the tension:**

    These two perspectives create a genuine dilemma. The recommended resolution is a **component-wise adaptive strategy**:

    - **Increase $\lambda$ for structural parameters** ($\kappa$, $\rho$, $\xi$ in Heston): these should remain stable even during stress, as they reflect long-term dynamics that do not change overnight. Higher noise makes their estimation less reliable, so more regularization is warranted.

    - **Decrease $\lambda$ for level parameters** ($v_0$, $\bar{v}$, overall volatility level): these must adapt quickly to the new market environment. The economic cost of suppressing a legitimate level shift outweighs the statistical benefit of noise reduction.

    Formally, use a diagonal $\lambda$ matrix:

    $$
    \Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_p)
    $$

    with different strengths for different parameter groups. During stress, increase $\lambda_i$ for shape/mean-reversion parameters and decrease $\lambda_i$ for level parameters.

    Additionally, one can switch the prior $\theta_0$ from yesterday's parameters to a **stress-calibrated prior** (e.g., historical crash parameters), which allows regularization without anchoring to a stale calm-market regime.
