# Model Drift vs Parameter Drift

Observed parameter changes over time can stem from two fundamentally different sources: **model drift** and **parameter drift**. Distinguishing between them is crucial for interpretation, risk management, and model governance.

---

## Defining the concepts

### Parameter drift

**Parameter drift** occurs when model parameters genuinely change over time because the underlying economic environment evolves.

Examples:

- Volatility levels shifting as market regimes change.
- Correlation between asset and volatility changing with market structure.
- Mean-reversion speed varying with monetary policy regimes.

In this case:

- The model class remains appropriate.
- Parameters are time-varying but structurally meaningful.
- Recalibration tracks genuine economic changes.

### Model drift

**Model drift** (or **model misspecification drift**) occurs when the true data-generating process lies outside the model class, and calibration compensates by shifting parameters.

In this case:

- The model is fundamentally wrong.
- Parameters absorb the misfit rather than representing economic quantities.
- Calibrated values lose structural interpretation.
- Different parameter changes would occur with a different (better) model.

---

## Why the distinction matters

### Interpretation

If parameters truly drift:

- Changes have economic meaning.
- Historical parameter paths inform future expectations.
- Scenario analysis can extrapolate parameter trends.

If model drift dominates:

- Parameter changes are artifacts.
- Historical paths reflect model failure, not economics.
- Scenario analysis based on parameter trends is misleading.

### Risk management

**Parameter drift:**

- Can be modeled explicitly (stochastic parameters).
- Parameter uncertainty translates to well-defined risk.
- Hedging adjustments follow from parameter dynamics.

**Model drift:**

- Indicates structural model failure.
- Risk is not captured by parameter uncertainty alone.
- Model should be replaced or augmented, not just recalibrated.

### Model governance

Regulators and model validators distinguish between:

- **Model uncertainty:** The model is correct but parameters are uncertain.
- **Model risk:** The model may be wrong.

Model drift is evidence of model risk. Parameter drift is (potentially) manageable model uncertainty.

---

## Diagnosing the source

### Indicators of parameter drift

- **Smooth evolution:** Parameters change gradually, aligned with market conditions.
- **Correlation with observables:** Parameter changes correlate with realized volatility, market stress indices, etc.
- **Interpretability:** Changes make economic sense (e.g., $\rho$ becomes more negative during crashes).
- **Stability under model extensions:** Adding features (jumps, stochastic vol-of-vol) does not eliminate parameter trends.

### Indicators of model drift

- **Erratic behavior:** Parameters jump without market events.
- **Boundary clustering:** Parameters repeatedly hit constraints (suggests model cannot fit data).
- **Systematic residuals:** Calibration errors show patterns (not random noise).
- **Poor out-of-sample performance:** Calibrated model fails on held-out instruments.
- **Instability under perturbation:** Small data changes produce large parameter changes.
- **Vanishing under model extension:** Parameter drift disappears when model is improved.

### Example: correlation in Heston

In the Heston model, $\rho$ (correlation between spot and variance shocks) is often observed to become more negative during market stress.

**Is this parameter drift or model drift?**

- If Heston accurately captures market dynamics, and correlation genuinely varies, it's parameter drift.
- If the negative $\rho$ compensates for missing jumps (which create similar skew), it's model drift: adding jumps would reduce the $\rho$ variation.

Empirically, both effects are present. Jumps explain part of the skew; residual $\rho$ variation reflects genuine correlation dynamics.

---

## Formal tests

### Encompassing tests

Compare nested models:

- Fit Model A (base) and Model B (extended).
- If parameter drift in Model A disappears in Model B, it was likely model drift.

**Example:** Compare Heston vs. Bates (Heston + jumps). If Heston's $\rho$ is stable but Bates' is not, jumps were absorbing misspecification.

### Out-of-sample stability

- Calibrate to time-$t$ data with parameters $\theta_t$.
- Predict prices at $t + \Delta t$ using $\theta_t$ (no recalibration).
- Compare to actual prices.

Systematic prediction errors indicate model drift. Random errors around zero suggest parameter drift that could be modeled.

### Specification tests

Test whether residuals are consistent with model assumptions:

- **Ljung–Box test:** Serial correlation in residuals.
- **Kolmogorov–Smirnov:** Distributional fit of standardized residuals.
- **RESET test:** Nonlinearity in residuals vs. fitted values.

Failures indicate model misspecification.

### Cross-sectional consistency

Calibrate separately to different subsets of data (e.g., puts vs. calls, short vs. long maturities). If parameters disagree:

- Random disagreement suggests noise (acceptable).
- Systematic disagreement suggests model drift.

---

## Quantitative decomposition

### Framework

Suppose we observe calibrated parameters $\hat{\theta}_t$ over time $t = 1, \ldots, T$. Decompose:

$$
\hat{\theta}_t = \theta^{\star} + \delta_t + \epsilon_t,
$$

where:

- $\theta^{\star}$ = true (unknown) average parameter.
- $\delta_t$ = parameter drift (genuine time variation).
- $\epsilon_t$ = estimation error (including model drift effects).

### Variance decomposition

Total variance:

$$
\text{Var}(\hat{\theta}_t) = \text{Var}(\delta_t) + \text{Var}(\epsilon_t) + 2\text{Cov}(\delta_t, \epsilon_t).
$$

If we can estimate $\text{Var}(\epsilon_t)$ (e.g., from bootstrap), we can attribute residual variance to drift.

### Signal-to-noise ratio

Define:

$$
\text{SNR} = \frac{\text{Var}(\delta_t)}{\text{Var}(\epsilon_t)}.
$$

- High SNR: Parameter changes are mostly genuine drift.
- Low SNR: Parameter changes are mostly noise/model drift.

---

## Practical implications

### When parameter drift dominates

- Model parameters as time-varying (stochastic parameters, regime-switching).
- Use filtering (Kalman, particle) to estimate current state.
- Incorporate parameter dynamics into hedging.
- Scenario analysis: project parameter paths.

### When model drift dominates

- Do not trust parameter trends.
- Consider model extension or replacement.
- Use robust pricing (price ranges, not point estimates).
- Increase model risk reserves.
- Communicate limitations to stakeholders.

### The mixed case

In practice, both effects are present. A pragmatic approach:

1. Use the best available model (minimize model drift).
2. Allow for genuine parameter variation (acknowledge parameter drift).
3. Quantify both sources of uncertainty.
4. Report prices with confidence intervals reflecting total uncertainty.

---

## Connection to model risk frameworks

### SR 11-7 (OCC/Federal Reserve)

The U.S. regulatory guidance on model risk management emphasizes:

- **Conceptual soundness:** Is the model appropriate for the purpose?
- **Ongoing monitoring:** Do calibrated parameters behave reasonably over time?
- **Outcomes analysis:** Does the model's output match reality?

Model drift is evidence against conceptual soundness. Excessive parameter drift raises monitoring concerns.

### Model reserves

Banks often hold reserves for model risk. The decomposition between parameter uncertainty (quantifiable) and model uncertainty (harder to quantify) affects reserve calculations.

---

## Case study: volatility smile dynamics

### Observation

Calibrate SVI parameters to SPX options daily. The skew parameter $\rho_{\text{SVI}}$ varies over time.

### Analysis

1. **Correlation with VIX:** $\rho_{\text{SVI}}$ is more negative when VIX is high. This is consistent with economics (leverage effect, panic-driven skew).

2. **Comparison with SABR:** Calibrate SABR to same data. If SABR's $\rho_{\text{SABR}}$ shows similar dynamics, it's parameter drift. If only SVI shows it, it may be model-specific drift.

3. **Out-of-sample test:** Use yesterday's parameters to price today's options. Compute error. If error is small and unbiased, model is adequate; parameter drift is genuine.

### Conclusion

For SPX, empirical evidence suggests genuine parameter drift in skew, partially correlated with market conditions. Model drift also exists (no single parameterization perfectly captures all regimes), but is secondary.

---

## Key takeaways

- Parameter drift reflects genuine economic variation; model drift reflects misspecification.
- Distinguishing them is essential for interpretation and risk management.
- Diagnostic tools: encompassing tests, out-of-sample analysis, specification tests.
- Model drift suggests the model should be improved, not just recalibrated.
- In practice, both effects coexist; quantify and manage each appropriately.

---

## Further reading

- Rebonato, *Volatility and Correlation* (parameter stability and model risk).
- Cont, "Model Uncertainty and Its Impact on Pricing" (2006).
- Andersen & Piterbarg, *Interest Rate Modeling* (calibration stability).
- OCC/Federal Reserve, "Supervisory Guidance on Model Risk Management" (SR 11-7).
- Gatheral, *The Volatility Surface* (smile dynamics and parameter interpretation).
