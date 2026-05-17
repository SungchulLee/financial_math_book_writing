# Robust Calibration Criteria

Given the inevitability of model and calibration uncertainty, one should not aim for a single "best fit" but for **robust calibration**: parameter estimates that perform reasonably well across scenarios, over time, and under perturbations.

---

## What does robustness mean?

A robust calibration satisfies several criteria simultaneously:

### 1. Stability under data perturbations

Small changes in input data (within bid-ask spreads, across data vendors) should not produce large changes in parameters:

$$
\|\theta(\text{data} + \epsilon) - \theta(\text{data})\| \le C \|\epsilon\|
$$

for some reasonable constant $C$.

### 2. Avoidance of extreme parameters

Parameters should lie well within economically plausible bounds:

- Volatility parameters positive and bounded.
- Correlation within $[-1, 1]$, not clustering at boundaries.
- Mean-reversion speeds positive and not extreme.

### 3. Reasonable out-of-sample performance

The calibrated model should price instruments not used in calibration with acceptable accuracy:

- Hold-out validation error comparable to in-sample error.
- No systematic bias in out-of-sample pricing.

### 4. Temporal stability

Parameters should evolve smoothly over time unless market conditions genuinely change:

- Day-to-day parameter volatility should be economically interpretable.
- No oscillations or sign changes without market events.

### 5. Stable Greeks and hedging behavior

Hedge ratios derived from calibrated parameters should be reliable:

- Greeks should not jump erratically.
- Hedging P&L attribution should be stable.

---

## Robust objective functions

### Regularized objectives

Add penalties to discourage extreme or unstable parameters:

$$
\mathcal{L}_{\text{robust}}(\theta) = \mathcal{L}_{\text{fit}}(\theta) + \lambda \mathcal{R}(\theta)
$$

where $\mathcal{R}$ penalizes:

- Distance from prior or yesterday's parameters.
- Parameter magnitude (shrinkage).
- Roughness (for functional parameters).

### Robust loss functions

Replace squared loss with losses less sensitive to outliers:

**Huber loss:**

$$
\ell_H(r) = \begin{cases} \frac{1}{2} r^2 & |r| \le \delta \\ \delta |r| - \frac{1}{2}\delta^2 & |r| > \delta \end{cases}
$$

**$\ell_1$ loss:**

$$
\ell_1(r) = |r|
$$

These reduce the influence of stale quotes or outliers.

### Worst-case objectives

Minimize the maximum error across scenarios:

$$
\min_\theta \max_{y \in \mathcal{Y}} \mathcal{L}(\theta, y)
$$

where $\mathcal{Y}$ is a set of plausible market data realizations (e.g., within bid-ask).

This produces parameters that are uniformly acceptable rather than optimal for one scenario.

### Ensemble calibration

Fit multiple models or use multiple calibration runs:

1. Calibrate with different initializations, weights, or subsets.
2. Aggregate results (mean, median, or model averaging).
3. Report dispersion as uncertainty measure.

Ensemble methods reduce sensitivity to any single calibration choice.

---

## Stability-based validation

### Day-over-day parameter tracking

Monitor calibrated parameters over time:

- Compute rolling mean and standard deviation.
- Flag days with parameter changes exceeding thresholds.
- Investigate large changes: market event or calibration artifact?

### Perturbation analysis

Systematically perturb inputs:

1. Add noise within bid-ask to each quote.
2. Recalibrate $N$ times with different perturbations.
3. Examine distribution of resulting parameters.

**Metrics:**

- Standard deviation of parameters across perturbations.
- Maximum parameter deviation.
- Correlation of parameter changes with perturbations.

### Cross-validation

Hold out subsets of instruments:

1. Calibrate to $80\%$ of data.
2. Price held-out $20\%$ with calibrated parameters.
3. Compute out-of-sample error.
4. Rotate hold-out set; average results.

Models that overfit noise show poor cross-validation performance.

### Instrument subset consistency

Calibrate separately to different instrument types:

- Puts vs. calls.
- Short-dated vs. long-dated.
- ATM vs. OTM.

If parameters disagree significantly, the model may be mis-specified or data may be inconsistent.

---

## Economic versus statistical criteria

### Statistical fit

Minimizing residual sum of squares (RSS) or maximizing likelihood measures statistical fit:

$$
\text{RSS} = \sum_j w_j (P_j^{\text{model}} - P_j^{\text{mkt}})^2
$$

Lower RSS is better statistically.

### Economic plausibility

Parameters should make economic sense:

- Long-run variance $\bar{v}$ should be consistent with historical realized volatility.
- Mean-reversion $\kappa$ should imply reasonable half-lives.
- Correlation $\rho$ should align with observed spot-vol dynamics.

A statistically optimal fit may be economically implausible (and vice versa).

### The trade-off

Often, the most robust calibration:

- Sacrifices some in-sample fit for stability.
- Prioritizes economic interpretability over statistical optimality.
- Accepts small pricing residuals in exchange for reliable Greeks.

---

## Time stability as a primary criterion

### Rationale

In practice, many trading desks judge calibration quality primarily by time stability:

- Parameters that jump without market justification are problematic.
- Smooth evolution is easier to hedge and explain.
- Stability reduces transaction costs and operational complexity.

### Implementation

Regularize toward yesterday's parameters:

$$
\mathcal{L}(\theta) = \mathcal{L}_{\text{fit}}(\theta) + \lambda \|\theta - \hat{\theta}_{t-1}\|^2
$$

This penalizes large parameter changes, promoting continuity.

### Choosing λ

- Large $\lambda$: very stable parameters, potentially stale (under-reactive).
- Small $\lambda$: responsive to data, potentially noisy (over-reactive).

Optimal $\lambda$ depends on:

- Market volatility (more volatile markets may warrant smaller $\lambda$).
- Data quality (noisier data warrants larger $\lambda$).
- Hedging frequency (less frequent hedging tolerates less stability).

---

## Model risk governance

### Role in institutional settings

Robust calibration supports broader model risk management:

- **Model risk limits:** Cap positions with high sensitivity to calibration.
- **Valuation adjustments:** Reserve for calibration uncertainty.
- **Model validation:** Demonstrate stability as part of approval process.
- **Audit trail:** Document calibration choices and their rationale.

### Regulatory expectations

Regulators (OCC, Fed, PRA) expect:

- Sensitivity analysis showing impact of calibration uncertainty.
- Evidence that calibration is stable and interpretable.
- Reserves for pricing and hedging errors from model risk.
- Ongoing monitoring of calibration performance.

### Communication

Robust calibration facilitates communication:

- Parameter uncertainty can be reported alongside point estimates.
- Price ranges are more informative than point prices.
- Stability metrics provide confidence in model outputs.

---

## Practical workflow for robust calibration

### Step 1: Data preparation

- Filter illiquid/stale quotes.
- Ensure arbitrage-free surface.
- Document data sources and filters.

### Step 2: Objective function design

- Choose price vs. vol space based on use case.
- Set weights reflecting quote quality (bid-ask spreads).
- Add regularization toward prior or previous calibration.

### Step 3: Optimization

- Use robust optimizer (trust-region, Levenberg-Marquardt).
- Run multiple initializations to check for local minima.
- Enforce parameter bounds.

### Step 4: Validation

Recall (see [stability-based validation](robust_calibration_criteria.md#stability-based-validation)) — run perturbation analysis, cross-validation, day-over-day tracking, and instrument-subset consistency checks; flag fits whose residuals show systematic patterns.

### Step 5: Documentation and monitoring

- Record calibrated parameters and diagnostics.
- Flag calibrations that fail stability tests.
- Review periodically with model validation team.

---

## Summary: robust calibration checklist

| Criterion | Diagnostic | Action if failed |
|-----------|-----------|------------------|
| Stability under perturbations | Perturbation analysis | Increase regularization |
| No extreme parameters | Parameter bounds check | Tighten constraints |
| Good out-of-sample fit | Cross-validation | Reduce overfitting |
| Temporal smoothness | Day-over-day tracking | Regularize toward prior |
| Economic plausibility | Compare to historical data | Adjust priors |
| Stable Greeks | Greek sensitivity analysis | Simplify model or hedge conservatively |

---

## Key takeaways

- Perfect fit is neither achievable nor desirable.
- Robust calibration prioritizes stability and interpretability over minimal residuals.
- Regularization, robust losses, and ensemble methods improve robustness.
- Time stability is often the most important practical criterion.
- Model risk must be assessed jointly with calibration.
- Robust calibration supports risk management, governance, and communication.

---

## Further reading

- Cont, "Model Uncertainty and Its Impact on Pricing" (2006).
- Glasserman & Xu, "Robust Risk Measurement and Model Risk" (2014).
- Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning* (regularization, cross-validation).
- Tarantola, *Inverse Problem Theory* (robust estimation).
- OCC/Federal Reserve, "Supervisory Guidance on Model Risk Management" (SR 11-7).

---

## Exercises

**Exercise 1.** Define the five criteria for robust calibration listed in this section (stability, avoidance of extremes, out-of-sample performance, temporal stability, stable Greeks). For a Heston model calibrated to SPX options, design a specific quantitative test for each criterion and specify a pass/fail threshold.

??? success "Solution to Exercise 1"
    The five criteria and their quantitative tests for a Heston model calibrated to SPX options are as follows.

    **1. Stability under data perturbations.**

    *Test:* Perturb each market quote by a random amount uniformly distributed within its bid-ask spread. Recalibrate 200 times with independent perturbations. Compute the standard deviation of each parameter across runs.

    *Pass/fail:* The coefficient of variation (std/mean) for each parameter should be below 10%. For example, if $\hat{\rho} = -0.70$, the standard deviation across perturbations should satisfy $\sigma_\rho < 0.07$.

    **2. Avoidance of extreme parameters.**

    *Test:* Define economically plausible bounds: $v_0 \in [0.005, 0.25]$, $\kappa \in [0.1, 10]$, $\bar{v} \in [0.005, 0.20]$, $\sigma_v \in [0.05, 2.0]$, $\rho \in [-0.95, 0.05]$. Check that the calibrated parameters lie strictly within these bounds with a margin of at least 10% of the range from each boundary.

    *Pass/fail:* All parameters within bounds with margin. Fail if any parameter is within 10% of a boundary (e.g., $\rho < -0.90$ or $\kappa > 9$).

    **3. Reasonable out-of-sample performance.**

    *Test:* Hold out 20% of the calibration instruments (e.g., every 5th strike-maturity pair). Calibrate to the remaining 80%. Price the held-out instruments with the calibrated model.

    *Pass/fail:* Out-of-sample RMSE in implied volatility should be no more than $1.5\times$ the in-sample RMSE. If in-sample RMSE is 0.3 vol points, out-of-sample RMSE should be below 0.45 vol points.

    **4. Temporal stability.**

    *Test:* Track calibrated parameters over 60 trading days. Compute day-over-day changes $|\hat{\theta}_t - \hat{\theta}_{t-1}|$ for each parameter. Compare to the parameter's standard deviation from the perturbation test.

    *Pass/fail:* The median day-over-day change should be below $2\sigma_{\text{perturbation}}$ for each parameter. Large daily jumps (exceeding $3\sigma$) should occur on fewer than 5% of days and should coincide with significant market events.

    **5. Stable Greeks and hedging behavior.**

    *Test:* Compute the delta of a benchmark ATM 3-month call each day using the daily calibration. Decompose the daily delta change into a market-driven component ($\Gamma \Delta S + \text{vanna} \cdot \Delta\sigma$) and a calibration-driven component ($\nabla_\theta \Delta^\top \Delta\hat{\theta}$).

    *Pass/fail:* The calibration-driven component should account for less than 30% of the total daily delta change on average. If calibration noise dominates Greek changes, the calibration is too unstable for reliable hedging.

---

**Exercise 2.** The Huber loss function is $\ell_H(r) = \frac{1}{2}r^2$ for $|r| \le \delta$ and $\delta|r| - \frac{1}{2}\delta^2$ for $|r| > \delta$. Show that $\ell_H$ is continuously differentiable but not twice differentiable at $|r| = \delta$. Compare the influence function of Huber loss to that of squared loss, and explain why Huber loss is more robust to outlier quotes.

??? success "Solution to Exercise 2"
    **Continuity and differentiability of Huber loss.**

    The Huber loss is defined as:

    $$
    \ell_H(r) = \begin{cases} \frac{1}{2}r^2 & |r| \le \delta \\ \delta|r| - \frac{1}{2}\delta^2 & |r| > \delta \end{cases}
    $$

    *Continuity at $|r| = \delta$:* At $r = \delta$: from the left, $\frac{1}{2}\delta^2$; from the right, $\delta \cdot \delta - \frac{1}{2}\delta^2 = \frac{1}{2}\delta^2$. Continuous.

    *First derivative:*

    $$
    \ell_H'(r) = \begin{cases} r & |r| \le \delta \\ \delta \cdot \text{sgn}(r) & |r| > \delta \end{cases}
    $$

    At $r = \delta$: from the left, $\ell_H'(\delta^-) = \delta$; from the right, $\ell_H'(\delta^+) = \delta$. So $\ell_H$ is continuously differentiable.

    *Second derivative:*

    $$
    \ell_H''(r) = \begin{cases} 1 & |r| < \delta \\ 0 & |r| > \delta \end{cases}
    $$

    At $r = \delta$: $\ell_H''(\delta^-) = 1$ and $\ell_H''(\delta^+) = 0$. The second derivative has a jump discontinuity, so $\ell_H$ is **not** twice differentiable at $|r| = \delta$.

    **Influence function comparison.**

    The influence function measures how much a single observation affects the estimate. For M-estimators, the influence function is proportional to $\psi(r) = \ell'(r)$.

    - *Squared loss:* $\psi_{\text{sq}}(r) = r$. The influence grows linearly without bound. A single outlier with large $|r|$ can move the estimate arbitrarily far.

    - *Huber loss:* $\psi_H(r) = \min(|r|, \delta) \cdot \text{sgn}(r)$. The influence is bounded: $|\psi_H(r)| \le \delta$ for all $r$.

    **Why Huber loss is more robust:** In calibration, a stale or erroneous quote produces a large residual $r$. Under squared loss, this outlier dominates the objective and pulls parameters toward fitting the bad quote. Under Huber loss, once $|r| > \delta$, the outlier's influence is capped at $\delta$, so it cannot distort the calibration beyond a bounded amount. The threshold $\delta$ is chosen to match the typical bid-ask spread: residuals within $\delta$ are treated as informative (squared loss regime), while residuals beyond $\delta$ are treated as potential outliers (linear loss regime, bounded influence).

---

**Exercise 3.** A perturbation analysis is performed: market quotes are perturbed 500 times within bid-ask spreads, and the model is recalibrated each time. The resulting parameter distributions for $\rho$ have mean $-0.71$ and standard deviation $0.08$. For $\sigma_v$, the mean is $0.45$ and standard deviation is $0.15$. Which parameter is more robustly identified? How would you use these distributions to compute a confidence interval for the price of a barrier option?

??? success "Solution to Exercise 3"
    **Robustness of identification.**

    The coefficient of variation (CV) measures how precisely a parameter is identified relative to its magnitude:

    - $\rho$: $\text{CV} = 0.08 / 0.71 \approx 11.3\%$
    - $\sigma_v$: $\text{CV} = 0.15 / 0.45 \approx 33.3\%$

    The parameter $\rho$ is **more robustly identified** than $\sigma_v$, since its relative standard deviation is about three times smaller. This is typical: correlation $\rho$ is well-constrained by the skew of the implied volatility surface, while vol-of-vol $\sigma_v$ primarily affects the curvature (smile convexity), which is less precisely observed.

    **Confidence interval for a barrier option price.**

    To propagate parameter uncertainty to the barrier option price:

    1. **From the perturbation analysis**, we have 500 parameter vectors $\theta^{(j)} = (\ldots, \rho^{(j)}, \ldots, \sigma_v^{(j)}, \ldots)$.

    2. **For each $\theta^{(j)}$**, compute the barrier option price $P^{(j)} = P(\theta^{(j)})$ using the full pricing model.

    3. **Construct the empirical distribution** of $\{P^{(j)}\}_{j=1}^{500}$.

    4. **Report the confidence interval** as the empirical quantiles: a 95% confidence interval is $[P_{(0.025)}, P_{(0.975)}]$, where $P_{(\alpha)}$ denotes the $\alpha$-quantile of the price distribution.

    Alternatively, using the delta method for a first-order approximation:

    $$
    \sigma_P \approx \sqrt{\left(\frac{\partial P}{\partial \rho}\right)^2 (0.08)^2 + \left(\frac{\partial P}{\partial \sigma_v}\right)^2 (0.15)^2 + 2 \frac{\partial P}{\partial \rho}\frac{\partial P}{\partial \sigma_v} \text{Cov}(\rho, \sigma_v)}
    $$

    Given that $\sigma_v$ has much larger uncertainty, it is likely the dominant contributor to barrier option model risk, despite being less precisely identified. Barrier options are particularly sensitive to $\sigma_v$ because the distribution of future volatility paths determines the probability of barrier breach.

---

**Exercise 4.** Design a cross-validation experiment for a Heston calibration. You have 40 vanilla options across 8 strikes and 5 maturities. Describe the hold-out strategy (which instruments to hold out), the metric for out-of-sample performance, and how to interpret a scenario where in-sample RMSE is 0.2 vol points but out-of-sample RMSE is 1.5 vol points.

??? success "Solution to Exercise 4"
    **Cross-validation design for Heston calibration.**

    We have 40 vanilla options: 8 strikes $\times$ 5 maturities.

    **Hold-out strategy:** Use maturity-stratified $k$-fold cross-validation with $k = 5$. In each fold, hold out one complete maturity slice (all 8 strikes for that maturity). This is preferred over random hold-out because:

    - Holding out an entire maturity tests the model's ability to interpolate/extrapolate along the term structure.
    - Random hold-out risks holding out instruments that are nearly redundant with the training set, giving an overly optimistic out-of-sample score.

    For each fold $j \in \{1, \ldots, 5\}$:

    1. Remove all 8 options at maturity $T_j$ from the calibration set.
    2. Calibrate Heston to the remaining 32 options.
    3. Price the 8 held-out options at maturity $T_j$ using the calibrated parameters.
    4. Compute the out-of-sample error for fold $j$.

    **Metric:** Use root mean squared error in implied volatility space:

    $$
    \text{RMSE}_j^{\text{out}} = \sqrt{\frac{1}{8}\sum_{i=1}^{8}\left(\sigma_{\text{iv}}^{\text{model}}(K_i, T_j) - \sigma_{\text{iv}}^{\text{mkt}}(K_i, T_j)\right)^2}
    $$

    Average across folds: $\overline{\text{RMSE}}^{\text{out}} = \frac{1}{5}\sum_{j=1}^{5} \text{RMSE}_j^{\text{out}}$.

    **Interpreting in-sample RMSE = 0.2 vol points, out-of-sample RMSE = 1.5 vol points.**

    The ratio $1.5 / 0.2 = 7.5$ indicates severe **overfitting**. The model achieves a good fit to the calibration data but fails dramatically on held-out instruments. This suggests:

    - The model has too many effective degrees of freedom relative to the data, or the optimizer is finding parameter values that fit noise in the calibration quotes.
    - Parameters may be at extreme values that produce a locally good fit but poor generalization.
    - Regularization is needed: adding $\lambda\|\theta - \theta_{\text{prior}}\|^2$ to the objective will trade in-sample fit for out-of-sample robustness. The optimal $\lambda$ can be selected to minimize $\overline{\text{RMSE}}^{\text{out}}$.
    - The model itself may be mis-specified for the given maturity range (e.g., Heston may not capture the term structure adequately, suggesting the need for a time-dependent model or additional factors).

---

**Exercise 5.** Consider the regularized objective $\mathcal{L}_{\text{robust}}(\theta) = \mathcal{L}_{\text{fit}}(\theta) + \lambda\|\theta - \hat{\theta}_{t-1}\|^2$. Show that the first-order condition implies the optimal $\hat{\theta}_t$ lies on the line segment between the unconstrained MLE $\hat{\theta}_t^{\text{MLE}}$ and the prior $\hat{\theta}_{t-1}$, assuming $\mathcal{L}_{\text{fit}}$ is quadratic near its minimum. Express the optimal $\hat{\theta}_t$ as a weighted average and derive the weights in terms of $\lambda$ and the Fisher information matrix.

??? success "Solution to Exercise 5"
    Consider the regularized objective:

    $$
    \mathcal{L}_{\text{robust}}(\theta) = \mathcal{L}_{\text{fit}}(\theta) + \lambda\|\theta - \hat{\theta}_{t-1}\|^2
    $$

    **Quadratic approximation of $\mathcal{L}_{\text{fit}}$:** Near its minimum $\hat{\theta}_t^{\text{MLE}}$, approximate:

    $$
    \mathcal{L}_{\text{fit}}(\theta) \approx \mathcal{L}_{\text{fit}}(\hat{\theta}_t^{\text{MLE}}) + \frac{1}{2}(\theta - \hat{\theta}_t^{\text{MLE}})^\top \mathcal{I} (\theta - \hat{\theta}_t^{\text{MLE}})
    $$

    where $\mathcal{I} = \nabla^2 \mathcal{L}_{\text{fit}}(\hat{\theta}_t^{\text{MLE}})$ is the observed Fisher information matrix (the Hessian of the negative log-likelihood at the MLE).

    **First-order condition:** Setting $\nabla_\theta \mathcal{L}_{\text{robust}} = 0$:

    $$
    \mathcal{I}(\hat{\theta}_t - \hat{\theta}_t^{\text{MLE}}) + 2\lambda(\hat{\theta}_t - \hat{\theta}_{t-1}) = 0
    $$

    Solving for $\hat{\theta}_t$:

    $$
    (\mathcal{I} + 2\lambda I)\hat{\theta}_t = \mathcal{I}\hat{\theta}_t^{\text{MLE}} + 2\lambda\hat{\theta}_{t-1}
    $$

    $$
    \hat{\theta}_t = (\mathcal{I} + 2\lambda I)^{-1}(\mathcal{I}\hat{\theta}_t^{\text{MLE}} + 2\lambda\hat{\theta}_{t-1})
    $$

    This can be rewritten as a **weighted average**:

    $$
    \hat{\theta}_t = W \hat{\theta}_t^{\text{MLE}} + (I - W)\hat{\theta}_{t-1}
    $$

    where:

    $$
    W = (\mathcal{I} + 2\lambda I)^{-1}\mathcal{I}
    $$

    **Verification:** $I - W = (\mathcal{I} + 2\lambda I)^{-1}(2\lambda I)$, and indeed $W + (I - W) = I$.

    **Interpretation of the weights:**

    - When $\lambda \to 0$: $W \to I$, so $\hat{\theta}_t \to \hat{\theta}_t^{\text{MLE}}$ (pure maximum likelihood, no regularization).
    - When $\lambda \to \infty$: $W \to 0$, so $\hat{\theta}_t \to \hat{\theta}_{t-1}$ (parameters frozen at yesterday's values).
    - The weight matrix $W$ depends on the Fisher information $\mathcal{I}$: parameters that are well-identified by the data (large eigenvalues of $\mathcal{I}$) receive higher weight on the MLE, while poorly identified parameters (small eigenvalues) are pulled more toward the prior.

    This is precisely analogous to a **Bayesian update** with a Gaussian prior $\theta \sim \mathcal{N}(\hat{\theta}_{t-1}, (2\lambda)^{-1}I)$ and Gaussian likelihood with precision $\mathcal{I}$. The posterior mean is the weighted average above. The optimal $\hat{\theta}_t$ always lies on the line segment (in the matrix-weighted sense) between $\hat{\theta}_t^{\text{MLE}}$ and $\hat{\theta}_{t-1}$.

---

**Exercise 6.** The worst-case objective $\min_\theta \max_{y \in \mathcal{Y}} \mathcal{L}(\theta, y)$ provides a minimax calibration. For a simplified setting with one parameter $\theta$ and two market quotes $y_1, y_2$ each within a band $[y_i - \delta_i, y_i + \delta_i]$, solve the minimax problem graphically. How does the minimax solution differ from the standard least-squares solution?

??? success "Solution to Exercise 6"
    **Simplified minimax problem setup.**

    We have one parameter $\theta$, two market quotes $y_1, y_2$ in bands $[y_1 - \delta_1, y_1 + \delta_1]$ and $[y_2 - \delta_2, y_2 + \delta_2]$, and the loss:

    $$
    \mathcal{L}(\theta, y) = w_1(P_1(\theta) - y_1')^2 + w_2(P_2(\theta) - y_2')^2
    $$

    where $y_i' \in [y_i - \delta_i, y_i + \delta_i]$ are the adversarial data choices (with unit weights $w_1 = w_2 = 1$ for simplicity).

    **Standard least-squares:** Minimizes $\mathcal{L}(\theta, y)$ at $y_i' = y_i$ (mid-market):

    $$
    \hat{\theta}_{\text{LS}} = \arg\min_\theta \left[(P_1(\theta) - y_1)^2 + (P_2(\theta) - y_2)^2\right]
    $$

    **Minimax formulation:**

    $$
    \hat{\theta}_{\text{MM}} = \arg\min_\theta \max_{y_1' \in [y_1 - \delta_1, y_1 + \delta_1], \, y_2' \in [y_2 - \delta_2, y_2 + \delta_2]} \left[(P_1(\theta) - y_1')^2 + (P_2(\theta) - y_2')^2\right]
    $$

    **Inner maximization (adversary's choice):** For a fixed $\theta$, the adversary chooses $y_i'$ to maximize the squared errors. The worst case is:

    $$
    y_i' = \begin{cases} y_i - \delta_i & \text{if } P_i(\theta) > y_i \\ y_i + \delta_i & \text{if } P_i(\theta) < y_i \end{cases}
    $$

    That is, the adversary pushes each quote as far from the model price as possible within its band. This gives the worst-case loss:

    $$
    \mathcal{L}_{\text{WC}}(\theta) = (|P_1(\theta) - y_1| + \delta_1)^2 + (|P_2(\theta) - y_2| + \delta_2)^2
    $$

    **Graphical solution:** For a linear model $P_i(\theta) = a_i \theta + b_i$, the least-squares loss is a parabola centered at $\hat{\theta}_{\text{LS}}$. The worst-case loss is a wider parabola (shifted upward and broadened by $\delta_1, \delta_2$). Its minimum occurs at a $\hat{\theta}_{\text{MM}}$ that may differ from $\hat{\theta}_{\text{LS}}$.

    **Key difference from least-squares:**

    - The minimax solution is **pulled toward the instrument with the wider bid-ask spread** ($\delta_i$), because that instrument contributes more to worst-case loss. Standard least-squares treats all mid-quotes equally.
    - The minimax calibration is more **conservative**: it sacrifices mid-market fit to ensure no single adverse data realization causes a large error.
    - If $\delta_1 = \delta_2$, the minimax solution coincides with the least-squares solution at mid-market quotes. The solutions diverge when bid-ask spreads are asymmetric across instruments.
    - The minimax approach naturally handles illiquid quotes (large $\delta_i$) by down-weighting them, similar to weighted least squares with weights inversely proportional to bid-ask width.

---

**Exercise 7.** A model validation team observes that calibrated parameters for a SABR model exhibit the following over 120 trading days: mean $\alpha = 0.35$, std $0.08$; mean $\rho = -0.45$, std $0.12$; mean $\nu = 0.80$, std $0.25$. Using the robust calibration checklist from this section, assess whether each parameter meets the temporal stability criterion. Propose specific adjustments to the calibration procedure to improve stability for the most problematic parameter.

??? success "Solution to Exercise 7"
    **Temporal stability assessment.**

    A useful metric for temporal stability is the coefficient of variation (CV), which measures day-to-day variability relative to the parameter's mean. Additionally, we examine the daily standard deviation relative to the parameter's overall level.

    | Parameter | Mean | Std | CV (%) | Assessment |
    |-----------|------|-----|--------|------------|
    | $\alpha$ | 0.35 | 0.08 | 22.9% | Moderate instability |
    | $\rho$ | $-0.45$ | 0.12 | 26.7% | Moderate instability |
    | $\nu$ | 0.80 | 0.25 | 31.3% | **Most problematic** |

    For context, a well-calibrated parameter should typically have a CV below 10-15% over a stable market period. All three parameters exceed this threshold, but $\nu$ (vol-of-vol) is the most problematic with a 31.3% CV.

    To further assess, consider the implied daily parameter changes. If parameters evolve as a random walk with daily std $\sigma_{\text{daily}}$, then over 120 days, $\sigma_{\text{total}} \approx \sqrt{120} \cdot \sigma_{\text{daily}}$, so $\sigma_{\text{daily}} \approx \sigma_{\text{total}} / \sqrt{120}$:

    - $\alpha$: $\sigma_{\text{daily}} \approx 0.08/10.95 \approx 0.0073$ (2.1% of mean daily)
    - $\rho$: $\sigma_{\text{daily}} \approx 0.12/10.95 \approx 0.011$ (2.4% of mean daily)
    - $\nu$: $\sigma_{\text{daily}} \approx 0.25/10.95 \approx 0.023$ (2.9% of mean daily)

    However, if the observed std is primarily from day-to-day jumps (not a smooth random walk), the effective daily instability may be much larger.

    **Proposed adjustments for $\nu$ (most problematic parameter):**

    1. **Stronger regularization toward prior:** Use $\mathcal{L}_{\text{robust}} = \mathcal{L}_{\text{fit}} + \lambda_\nu (\nu - \hat{\nu}_{t-1})^2$ with a relatively large $\lambda_\nu$ specifically for the vol-of-vol parameter. A parameter-specific regularization allows $\alpha$ and $\rho$ (better identified) to move more freely while constraining $\nu$.

    2. **Tighter parameter bounds:** Restrict $\nu \in [0.3, 1.5]$ based on historical analysis, preventing extreme values that arise from overfitting.

    3. **Exponential smoothing:** Rather than using the raw calibrated $\hat{\nu}_t$, apply exponential smoothing: $\nu_t^{\text{smooth}} = \alpha_s \hat{\nu}_t + (1 - \alpha_s)\nu_{t-1}^{\text{smooth}}$ with $\alpha_s \approx 0.1$--$0.3$, filtering out high-frequency noise.

    4. **Fix $\nu$ over longer horizons:** Since vol-of-vol is weakly identified by vanilla options, consider recalibrating $\nu$ only weekly (or monthly) while allowing $\alpha$ and $\rho$ to update daily. This reflects the economic intuition that $\nu$ represents a structural feature of the volatility process that should not change rapidly.

    5. **Use additional instruments:** Variance swaps or VIX options are more sensitive to $\nu$ and can help pin it down more precisely, reducing calibration noise.
