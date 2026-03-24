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

- Check in-sample fit (residuals, patterns).
- Perform perturbation analysis.
- Compute out-of-sample error (hold-out or next-day).
- Examine parameter stability over time.

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

---

**Exercise 2.** The Huber loss function is $\ell_H(r) = \frac{1}{2}r^2$ for $|r| \le \delta$ and $\delta|r| - \frac{1}{2}\delta^2$ for $|r| > \delta$. Show that $\ell_H$ is continuously differentiable but not twice differentiable at $|r| = \delta$. Compare the influence function of Huber loss to that of squared loss, and explain why Huber loss is more robust to outlier quotes.

---

**Exercise 3.** A perturbation analysis is performed: market quotes are perturbed 500 times within bid-ask spreads, and the model is recalibrated each time. The resulting parameter distributions for $\rho$ have mean $-0.71$ and standard deviation $0.08$. For $\sigma_v$, the mean is $0.45$ and standard deviation is $0.15$. Which parameter is more robustly identified? How would you use these distributions to compute a confidence interval for the price of a barrier option?

---

**Exercise 4.** Design a cross-validation experiment for a Heston calibration. You have 40 vanilla options across 8 strikes and 5 maturities. Describe the hold-out strategy (which instruments to hold out), the metric for out-of-sample performance, and how to interpret a scenario where in-sample RMSE is 0.2 vol points but out-of-sample RMSE is 1.5 vol points.

---

**Exercise 5.** Consider the regularized objective $\mathcal{L}_{\text{robust}}(\theta) = \mathcal{L}_{\text{fit}}(\theta) + \lambda\|\theta - \hat{\theta}_{t-1}\|^2$. Show that the first-order condition implies the optimal $\hat{\theta}_t$ lies on the line segment between the unconstrained MLE $\hat{\theta}_t^{\text{MLE}}$ and the prior $\hat{\theta}_{t-1}$, assuming $\mathcal{L}_{\text{fit}}$ is quadratic near its minimum. Express the optimal $\hat{\theta}_t$ as a weighted average and derive the weights in terms of $\lambda$ and the Fisher information matrix.

---

**Exercise 6.** The worst-case objective $\min_\theta \max_{y \in \mathcal{Y}} \mathcal{L}(\theta, y)$ provides a minimax calibration. For a simplified setting with one parameter $\theta$ and two market quotes $y_1, y_2$ each within a band $[y_i - \delta_i, y_i + \delta_i]$, solve the minimax problem graphically. How does the minimax solution differ from the standard least-squares solution?

---

**Exercise 7.** A model validation team observes that calibrated parameters for a SABR model exhibit the following over 120 trading days: mean $\alpha = 0.35$, std $0.08$; mean $\rho = -0.45$, std $0.12$; mean $\nu = 0.80$, std $0.25$. Using the robust calibration checklist from this section, assess whether each parameter meets the temporal stability criterion. Propose specific adjustments to the calibration procedure to improve stability for the most problematic parameter.
