# Stability of Calibration


Recall (see [§ Ill-Posedness and Non-Uniqueness](../../ch17/calibration_as_inverse_problem/ill_posedness_and_non_uniqueness.md), [§ Tikhonov Regularization](../../ch17/regularization_and_stability/tikhonov_regularization.md), [§ Trade-off Between Fit and Robustness](../../ch17/regularization_and_stability/trade_off_between_fit_and_robustness.md)) the general regularization framework. This page applies these ideas to *stochastic volatility* calibration.

Beyond fit quality, a calibration must be **stable**: small changes in market data should not cause large parameter shifts. Stability is a central criterion for production models.

---

## Sources of instability


Calibration instability arises from:

- ill-posed inverse problems,
- weakly identifiable parameters (see [§ Identifiability Issues](identifiability_issues.md)),
- noisy or illiquid quotes,
- overly flexible objectives.

These factors interact nonlinearly.

---

## Measuring stability


Common stability checks include:

- re-calibration under perturbed quotes,
- rolling-window calibration,
- monitoring parameter time series,
- comparing alternative weighting schemes.

Stability should be assessed across market regimes.

---

## Regularization and constraints


Stability is improved by:

- regularization (penalties, priors),
- economically motivated bounds,
- reduced parameterization,
- maturity-balanced objectives.

These reduce variance at the cost of bias.

---

## Practical acceptance criteria


In practice, desks often require:

- smooth parameter evolution over time,
- limited sensitivity to individual quotes,
- consistent pricing of benchmark instruments.

A slightly worse fit is often acceptable if stability improves.

---

## Key takeaways


- Stability is as important as in-sample accuracy.
- Regularization is essential in stochastic volatility calibration.
- Calibration quality must be judged dynamically, not pointwise.

---

## Further reading


- Rebonato, *Volatility and Correlation*.
- Andersen & Piterbarg, calibration stability discussions.

---

## Exercises

**Exercise 1.** A Heston model is calibrated to S&P 500 options on Monday, yielding $\kappa = 2.1$, $\theta = 0.042$, $\xi = 0.51$. On Tuesday, with ATM vol shifting by 0.5 vol points, the recalibration gives $\kappa = 3.8$, $\theta = 0.031$, $\xi = 0.62$. Compute the percentage change in each parameter. Is this calibration stable? What specific feature of the parameter space might cause such large shifts?

??? success "Solution to Exercise 1"
    The percentage changes are computed as

    $$
    \Delta\kappa = \frac{3.8 - 2.1}{2.1} \times 100\% \approx 80.95\%
    $$

    $$
    \Delta\theta = \frac{0.031 - 0.042}{0.042} \times 100\% \approx -26.19\%
    $$

    $$
    \Delta\xi = \frac{0.62 - 0.51}{0.51} \times 100\% \approx 21.57\%
    $$

    This calibration is clearly **unstable**: a 0.5 vol point shift in ATM implied volatility should not cause parameters to move by 20--80%. A well-behaved calibration would show parameter shifts of a few percent at most for such a small market perturbation.

    The specific feature of the parameter space causing this is the **near-degeneracy between $\kappa$ and $\theta$**. In the Heston model, the long-run variance level is largely determined by the product $\kappa\theta$. Note that $\kappa_1 \theta_1 = 2.1 \times 0.042 = 0.0882$ and $\kappa_2 \theta_2 = 3.8 \times 0.031 = 0.1178$, so even the well-identified combination shifted. The loss surface is flat along the curve $\kappa\theta \approx \text{const}$, creating a ridge that the optimizer traverses dramatically in response to small data changes. This is a classic symptom of weak identifiability in the $(\kappa, \theta)$ plane.

---

**Exercise 2.** A regularized calibration objective is

$$
\mathcal{L}_{\text{reg}}(\theta) = \mathcal{L}(\theta) + \lambda \|\theta - \theta_{\text{prior}}\|^2
$$

where $\mathcal{L}(\theta)$ is the standard fit error and $\theta_{\text{prior}}$ is yesterday's calibrated parameter. For $\lambda = 0$, the calibration changes parameters by 40% day-over-day. For $\lambda = 10$, the change is 5% but the fit error increases by 0.3 vol points. Discuss the bias-variance trade-off. How would you choose $\lambda$ in practice?

??? success "Solution to Exercise 2"
    The regularized objective penalizes deviation from yesterday's parameters:

    $$
    \mathcal{L}_{\text{reg}}(\theta) = \mathcal{L}(\theta) + \lambda \|\theta - \theta_{\text{prior}}\|^2
    $$

    **Bias-variance trade-off:**

    - At $\lambda = 0$: the calibration is purely data-driven. The 40% day-over-day parameter swings indicate high **variance** — the parameters are tracking noise in the data rather than genuine market dynamics. This makes hedging unstable and Greeks unreliable.
    - At $\lambda = 10$: the 5% day-over-day change is much more stable, but the 0.3 vol point increase in fit error represents **bias** — the model is anchored to yesterday's parameters and cannot fully adapt to genuine changes in market conditions.

    **Choosing $\lambda$ in practice:** One approach is **cross-validation**: calibrate on day $t$ with various $\lambda$ values, then evaluate the fit quality on day $t+1$ without recalibration. The $\lambda$ that minimizes the out-of-sample fit error provides the best predictive stability. Alternatively, practitioners often set $\lambda$ so that (i) day-over-day parameter changes remain below 10--15% under normal market conditions, and (ii) the fit error stays within the bid-ask spread of the calibration instruments. A fit error of 0.3 vol points is typically within bid-ask bounds, so $\lambda = 10$ would likely be acceptable in production.

---

**Exercise 3.** Describe a rolling-window stability test for Heston calibration. Specifically, outline a procedure that: (a) calibrates to options on each of 20 consecutive trading days; (b) records the five Heston parameters daily; (c) computes a stability metric. Propose a specific metric (e.g., average daily parameter change normalized by parameter value) and explain what threshold would indicate acceptable stability.

??? success "Solution to Exercise 3"
    **Rolling-window stability test procedure:**

    **(a) Calibration step:** On each of the 20 consecutive trading days $t = 1, \ldots, 20$, calibrate the Heston model to the available option surface using the same objective function, weighting scheme, and optimizer settings. Record the parameter vector

    $$
    \theta_t = (\kappa_t, \bar{\theta}_t, \xi_t, \rho_t, V_{0,t})
    $$

    **(b) Record parameters:** Store the five parameters in a $20 \times 5$ matrix. Optionally also record the fit error (RMSE in implied vol) for each day to ensure the calibration succeeded.

    **(c) Stability metric:** A natural metric is the **mean absolute relative daily change (MARDC)**:

    $$
    \text{MARDC}_j = \frac{1}{19}\sum_{t=2}^{20}\frac{|\theta_{j,t} - \theta_{j,t-1}|}{|\theta_{j,t-1}|}
    $$

    for each parameter $j$. The overall stability metric is

    $$
    S = \max_j \text{MARDC}_j
    $$

    **Threshold:** A calibration is acceptably stable if $S < 0.10$ (no parameter changes by more than 10% on average per day). More stringent desks might require $S < 0.05$. If $S > 0.20$, the calibration is likely suffering from identifiability issues and regularization or parameter reduction should be applied.

    Additionally, one should inspect the parameter time series visually for jumps, oscillations, or trends. Even if $S$ is acceptable on average, isolated days with 50%+ parameter shifts would be flagged.

---

**Exercise 4.** Two calibrations of the Heston model to the same data yield nearly identical fit errors ($RMSE_1 = 0.32\%$ vs. $RMSE_2 = 0.34\%$ in implied vol) but very different parameters: $(\kappa_1, \theta_1) = (1.5, 0.06)$ and $(\kappa_2, \theta_2) = (4.0, 0.035)$. Compute $\kappa\theta$ for each and explain why the product $\kappa\theta$ may be better identified than $\kappa$ and $\theta$ individually. What does this imply for practical calibration?

??? success "Solution to Exercise 4"
    Computing $\kappa\theta$ for each parameter set:

    $$
    \kappa_1\theta_1 = 1.5 \times 0.06 = 0.09
    $$

    $$
    \kappa_2\theta_2 = 4.0 \times 0.035 = 0.14
    $$

    Although the individual parameters differ dramatically ($\kappa$ differs by a factor of 2.7, $\theta$ differs by 71%), the products $\kappa\theta$ are closer in relative terms than the individual parameters.

    The product $\kappa\theta$ is better identified because it controls the **long-run mean of the variance process**: in the Heston model under risk-neutral dynamics, the drift of $V_t$ is $\kappa(\theta - V_t)$, and the stationary mean is $\theta$. However, option prices at moderate maturities depend on the *rate of convergence* to $\theta$ weighted by the level $\theta$ itself. For a given maturity $T$, the expected average variance is approximately

    $$
    \frac{1}{T}\int_0^T \mathbb{E}[V_t]\,dt \approx V_0 \cdot \frac{1-e^{-\kappa T}}{\kappa T} + \theta\Bigl(1 - \frac{1-e^{-\kappa T}}{\kappa T}\Bigr)
    $$

    When $T$ is moderate relative to $1/\kappa$, different $(\kappa, \theta)$ pairs can produce nearly the same expected average variance, making the loss surface flat along a curve in $(\kappa, \theta)$ space.

    **Practical implication:** Calibration should either (i) reparameterize in terms of $\kappa\theta$ and one of $\kappa$ or $\theta$, or (ii) fix one of the two parameters (e.g., fix $\kappa$ from a prior or from time-series estimation) and calibrate the other. This avoids chasing along the flat direction of the loss surface and produces more stable day-to-day results.

---

**Exercise 5.** A desk requires that no single quote perturbation of 0.2 vol points should change any Heston parameter by more than 10%. Design a sensitivity test to check this requirement. Specifically, describe: (a) how many perturbation scenarios to test; (b) how to perturb each quote; (c) how to aggregate the results into a pass/fail criterion.

??? success "Solution to Exercise 5"
    **Sensitivity test design:**

    **(a) Number of perturbation scenarios:** If the calibration uses $M$ market quotes, test $2M$ scenarios (perturbing each quote up and down). For a typical surface with 20--30 quotes, this means 40--60 perturbation scenarios.

    **(b) Perturbation method:** For each quote $i$, create two perturbed surfaces:

    - $\sigma_i^+ = \sigma_i^{\text{mkt}} + 0.002$ (adding 0.2 vol points)
    - $\sigma_i^- = \sigma_i^{\text{mkt}} - 0.002$ (subtracting 0.2 vol points)

    All other quotes remain unchanged. Recalibrate the Heston model on each perturbed surface using the same objective and optimizer settings. Record the parameter vector $\theta^{(i,\pm)}$.

    **(c) Pass/fail criterion:** For each perturbation scenario $(i, \pm)$ and each parameter $j$, compute the relative change:

    $$
    r_{ij}^{\pm} = \frac{|\theta_j^{(i,\pm)} - \theta_j^{\text{base}}|}{|\theta_j^{\text{base}}|}
    $$

    The **pass criterion** is

    $$
    \max_{i,j,\pm} r_{ij}^{\pm} < 0.10
    $$

    That is, no single quote perturbation of 0.2 vol points changes any parameter by more than 10%. If the test fails, identify which quote-parameter pairs violate the threshold. Often, wing quotes (deep OTM) or short-maturity quotes are the culprits, suggesting that those quotes should receive lower weight or be excluded.

---

**Exercise 6.** Explain why reducing the number of free parameters improves stability but potentially worsens fit quality. Consider the following calibration approaches for the Heston model: (a) all five parameters free; (b) fix $V_0$ from ATM implied vol, calibrate four parameters; (c) fix both $V_0$ and $\kappa$, calibrate three parameters. For each approach, discuss the expected trade-off between stability and fit quality.

??? success "Solution to Exercise 6"
    Reducing the number of free parameters improves stability because it **constrains the optimization landscape**: fewer parameters mean fewer directions in which the loss surface can be flat, reducing the effective dimension of near-degenerate regions. However, with fewer degrees of freedom, the model has less flexibility to match the observed surface, potentially increasing the fit error.

    **(a) All five parameters free ($\kappa, \theta, \xi, \rho, V_0$):**

    - **Stability:** Poorest. The $(\kappa, \theta)$ near-degeneracy and the interaction between $V_0$ and $\theta$ at short maturities create a high-dimensional region of near-equivalent solutions. Day-to-day parameter variation can be large.
    - **Fit quality:** Best possible within the Heston model. The optimizer has maximum flexibility to match the surface.

    **(b) Fix $V_0$ from ATM implied vol, calibrate four parameters ($\kappa, \theta, \xi, \rho$):**

    - **Stability:** Significantly improved. Fixing $V_0$ removes the $V_0$-$\theta$ ambiguity at short maturities, sharpening the loss landscape. The remaining $(\kappa, \theta)$ near-degeneracy persists but is less severe.
    - **Fit quality:** Slightly reduced. If the ATM implied vol is a noisy estimate of $V_0$, the fixed value may not be optimal, but the loss in fit is typically small (within bid-ask noise).

    **(c) Fix both $V_0$ and $\kappa$, calibrate three parameters ($\theta, \xi, \rho$):**

    - **Stability:** Best of the three approaches. With $\kappa$ fixed, the $(\kappa, \theta)$ degeneracy is completely eliminated. The remaining three parameters ($\theta, \xi, \rho$) each control distinct features of the surface (level, curvature, skew) and are typically well-identified.
    - **Fit quality:** Noticeably reduced. Fixing $\kappa$ at the wrong value can cause systematic mismatch in the term structure of implied volatility. The model may not be able to reconcile short and long maturities simultaneously.

    The optimal choice depends on the use case: desks requiring stable Greeks for hedging often prefer approach (b) or (c), while desks focused on pricing exotic derivatives may need (a) with regularization to maintain flexibility.
