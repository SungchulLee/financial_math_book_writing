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

Recall (see [§ Heston model](../../ch16/index.md)) that $\rho$ governs the spot--variance correlation; empirically it becomes more negative during market stress.

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
\hat{\theta}_t = \theta^{\star} + \delta_t + \epsilon_t
$$

where:

- $\theta^{\star}$ = true (unknown) average parameter.
- $\delta_t$ = parameter drift (genuine time variation).
- $\epsilon_t$ = estimation error (including model drift effects).

### Variance decomposition

Total variance:

$$
\text{Var}(\hat{\theta}_t) = \text{Var}(\delta_t) + \text{Var}(\epsilon_t) + 2\text{Cov}(\delta_t, \epsilon_t)
$$

If we can estimate $\text{Var}(\epsilon_t)$ (e.g., from bootstrap), we can attribute residual variance to drift.

### Signal-to-noise ratio

Define:

$$
\text{SNR} = \frac{\text{Var}(\delta_t)}{\text{Var}(\epsilon_t)}
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

2. **Comparison with SABR:** Recall (see [§ SABR model](../../ch14/sabr_model/arbitrage_free_sabr.md)). If SABR's $\rho_{\text{SABR}}$ shows similar dynamics, it's parameter drift; if only SVI shows it, it may be model-specific drift.

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

---

## Exercises

**Exercise 1.** Define parameter drift and model drift in your own words. For the Heston model calibrated daily to SPX options, give one concrete example of each: a scenario where observed changes in $\rho$ are primarily parameter drift, and a scenario where they are primarily model drift.

??? success "Solution to Exercise 1"
    **Parameter drift** is the genuine time variation of model parameters driven by changes in the underlying economic environment, while the model itself remains an appropriate description of the data-generating process. **Model drift** occurs when observed parameter changes are artifacts of model misspecification: the model class does not contain the true process, and calibration compensates by shifting parameters to absorb the misfit.

    **Example of parameter drift in $\rho$.** During a gradual transition from a low-volatility regime to a high-volatility regime (e.g., the onset of the 2020 COVID crisis), the Heston correlation $\rho$ may genuinely become more negative because the leverage effect intensifies: large downward spot moves coincide with variance spikes. If we add jumps or other extensions to the model and $\rho$ still shows the same trend, the variation is genuine parameter drift reflecting a real change in the spot-variance correlation structure.

    **Example of model drift in $\rho$.** Suppose the market exhibits sudden, large downward jumps in spot prices (crash risk) that the Heston model (a pure diffusion model) cannot generate. To fit the observed steep short-maturity skew produced by jump risk, the calibration pushes $\rho$ to extreme negative values (e.g., $\rho = -0.95$). On days without significant jump risk, $\rho$ reverts to moderate values (e.g., $\rho = -0.65$). This oscillation of $\rho$ does not reflect a genuine change in spot-variance correlation; rather, $\rho$ is compensating for missing jump dynamics. Evidence: switching to the Bates model (Heston + jumps), the jump component absorbs the skew, and $\rho$ stabilizes around $-0.70$ with much lower variation. The original $\rho$ variation in Heston was model drift.

---

**Exercise 2.** Consider the decomposition $\hat{\theta}_t = \theta^\star + \delta_t + \epsilon_t$. A bootstrap analysis (perturbing quotes within bid-ask 200 times) estimates $\text{Var}(\epsilon_t) = 0.002$ for the parameter $\bar{v}$ (long-run variance). The observed time-series variance of $\hat{\bar{v}}_t$ over 250 trading days is $\text{Var}(\hat{\bar{v}}_t) = 0.008$. Compute the signal-to-noise ratio. What fraction of the observed parameter variation is attributable to genuine drift versus estimation noise?

??? success "Solution to Exercise 2"
    **Given information.** The decomposition is $\hat{\theta}_t = \theta^\star + \delta_t + \epsilon_t$, where $\text{Var}(\epsilon_t) = 0.002$ (estimation noise from bootstrap) and $\text{Var}(\hat{\bar{v}}_t) = 0.008$ (total observed variance over 250 days).

    **Signal-to-noise ratio.** Assuming $\text{Cov}(\delta_t, \epsilon_t) \approx 0$ (genuine drift and estimation noise are independent), we have

    $$
    \text{Var}(\hat{\bar{v}}_t) = \text{Var}(\delta_t) + \text{Var}(\epsilon_t)
    $$

    Therefore

    $$
    \text{Var}(\delta_t) = \text{Var}(\hat{\bar{v}}_t) - \text{Var}(\epsilon_t) = 0.008 - 0.002 = 0.006
    $$

    The signal-to-noise ratio is

    $$
    \text{SNR} = \frac{\text{Var}(\delta_t)}{\text{Var}(\epsilon_t)} = \frac{0.006}{0.002} = 3.0
    $$

    **Fraction attributable to genuine drift.** The fraction of total observed variance due to genuine drift is

    $$
    \frac{\text{Var}(\delta_t)}{\text{Var}(\hat{\bar{v}}_t)} = \frac{0.006}{0.008} = 0.75 = 75\%
    $$

    The fraction due to estimation noise is

    $$
    \frac{\text{Var}(\epsilon_t)}{\text{Var}(\hat{\bar{v}}_t)} = \frac{0.002}{0.008} = 0.25 = 25\%
    $$

    **Interpretation.** With SNR = 3.0, the majority (75%) of the observed parameter variation in $\bar{v}$ is attributable to genuine economic drift rather than calibration noise. This suggests that modeling $\bar{v}$ as time-varying (e.g., via filtering) is justified. However, 25% of the variation is still noise, so smoothing or filtering is beneficial to separate signal from noise.

---

**Exercise 3.** An encompassing test compares the Heston model (Model A) with the Bates model (Model B = Heston + jumps). After calibrating both daily for one year, the standard deviation of $\hat{\rho}_t$ in Model A is $0.12$, while in Model B it is $0.04$. Interpret this result. Does it suggest that the $\rho$ variation in Model A is primarily parameter drift or model drift? Explain your reasoning.

??? success "Solution to Exercise 3"
    **Interpretation.** In Model A (Heston), $\hat{\rho}_t$ has standard deviation 0.12, meaning $\rho$ fluctuates over a wide range (e.g., from $-0.85$ to $-0.61$ within two standard deviations of the mean). In Model B (Bates = Heston + jumps), $\hat{\rho}_t$ has standard deviation 0.04, a reduction by a factor of 3.

    **Diagnosis: primarily model drift.** The dramatic reduction in $\rho$ variation when jumps are added strongly suggests that most of the $\rho$ variation in Model A is **model drift**, not parameter drift. The reasoning is:

    1. If $\rho$ variation were genuine parameter drift (reflecting real changes in spot-variance correlation), it would persist regardless of the model used. Adding jumps to the model should not affect a genuinely time-varying correlation.

    2. The fact that $\rho$ stabilizes in Model B indicates that Model A's $\rho$ was absorbing the skew effect of jumps. When the implied vol surface steepens due to increased jump risk, Model A can only match this by making $\rho$ more negative. Model B matches it through the jump parameters instead, allowing $\rho$ to capture only the residual diffusive correlation.

    3. The residual variation of 0.04 in Model B likely reflects a mix of genuine (smaller) parameter drift in correlation and remaining estimation noise. This level is more plausible as genuine economic variation.

    **Conclusion.** This is a textbook example of an **encompassing test**: the encompassing model (Bates) explains away most of the parameter instability in the nested model (Heston). Approximately $(0.12^2 - 0.04^2)/0.12^2 = (0.0144 - 0.0016)/0.0144 \approx 89\%$ of the variance in Heston's $\rho$ was model drift absorbed from the missing jump component.

---

**Exercise 4.** A model validator observes that the calibrated vol-of-vol parameter $\sigma_v$ in a Heston model repeatedly hits its upper constraint bound of $\sigma_v = 2.0$ during market stress. Is this more consistent with parameter drift or model drift? Propose a diagnostic test to confirm your hypothesis, and suggest a model extension that might resolve the issue.

??? success "Solution to Exercise 4"
    **Diagnosis: model drift.** When a parameter repeatedly hits its constraint boundary, this is a strong indicator of **model drift** rather than parameter drift:

    - If $\sigma_v$ truly needed to be above 2.0 during stress, the constraint is artificially limiting the calibration, and the model cannot fit the data.
    - Boundary clustering means the optimizer is being "stopped" by the constraint, suggesting the calibration loss function would continue to decrease if the parameter were allowed to go further. This is the hallmark of model misspecification: the model cannot generate enough vol-of-vol to match the observed surface, and the parameter absorbs as much of the misfit as the constraint allows.
    - During market stress, implied volatility surfaces exhibit features (extreme skew, steep term structure, convexity) that may exceed what the Heston model can produce with any parameter values, let alone constrained ones.

    **Diagnostic test.** Compute the calibration residuals (model implied vols minus market implied vols) on days when $\sigma_v$ hits the boundary versus days when it does not. If boundary days show:

    - Systematically larger residuals (particularly in the wings and short maturities),
    - Structured residual patterns (e.g., model consistently underestimates OTM put implied vols),

    then the model is misspecified, confirming model drift. Additionally, one can compute the Lagrange multiplier (shadow price) of the constraint: if it is large and persistent, the constraint is binding because the model needs more flexibility, not because the true $\sigma_v$ is near 2.0.

    **Model extension.** Several extensions could resolve this:

    - **Jumps in the spot process** (Bates model): Jumps generate steep short-maturity skew without requiring extreme $\sigma_v$, reducing the pressure on the vol-of-vol parameter.
    - **Jumps in variance** (SVJJ model): Variance jumps during stress produce the extreme vol-of-vol behavior that the diffusive CIR process cannot match, directly addressing the boundary issue.
    - **Stochastic vol-of-vol:** Allowing $\sigma_v$ itself to follow a stochastic process captures the time variation in realized vol-of-vol without requiring a constant parameter to accommodate both calm and stressed markets.

---

**Exercise 5.** Consider an out-of-sample stability test: calibrate at time $t$ with parameters $\hat{\theta}_t$, then predict prices at $t+1$ using $\hat{\theta}_t$ without recalibration. The prediction errors $e_{t+1}^{(j)} = \hat{C}_j(\hat{\theta}_t) - C_j^{\text{mkt}}(t+1)$ are computed for $m = 30$ options. If the errors are serially correlated (positive Ljung--Box test), what does this indicate about the model? Is the issue more likely parameter drift or model drift?

??? success "Solution to Exercise 5"
    **Interpretation of serial correlation.** If the prediction errors $e_{t+1}^{(j)}$ are serially correlated (positive Ljung--Box test rejects the null of no autocorrelation), this means that knowing today's prediction error provides information about tomorrow's prediction error. Specifically, if $\text{Corr}(e_t^{(j)}, e_{t+1}^{(j)}) > 0$, the model systematically under-predicts or over-predicts prices in a persistent manner.

    **Model drift is more likely.** Serial correlation in prediction errors indicates a systematic, persistent component in the errors that is not captured by the model. This is more consistent with model drift than parameter drift:

    - **Under pure parameter drift**, if the parameters change in a random-walk fashion, the prediction errors $e_{t+1}$ would reflect one-step-ahead surprises in parameter values. These surprises would be approximately uncorrelated across time (a random walk has uncorrelated increments), so prediction errors would not be serially correlated.
    - **Under model drift**, the model systematically fails to capture certain features of the data (e.g., term-structure effects, jump dynamics). These structural deficiencies persist across days, creating correlated errors. For example, if the model consistently underestimates OTM put implied vols, the prediction errors for those options will be persistently positive.

    The serial correlation pattern can reveal the nature of misspecification:

    - Positive autocorrelation at lag 1 suggests a slowly evolving structural bias.
    - Autocorrelation that decays slowly suggests a persistent mispricing pattern.
    - Autocorrelation at specific seasonal lags (e.g., weekly) could indicate market microstructure effects not captured by the model.

    The appropriate response is not merely to recalibrate more frequently (which would address parameter drift) but to investigate and potentially extend the model to eliminate the systematic component of the errors.

---

**Exercise 6.** Suppose calibrating a stochastic volatility model separately to short-maturity options ($T < 0.5$ years) and long-maturity options ($T > 1$ year) yields systematically different values for $\kappa$ (mean reversion): $\hat{\kappa}_{\text{short}} \approx 5$ and $\hat{\kappa}_{\text{long}} \approx 1.5$. Is this evidence of parameter drift, model drift, or a term-structure effect? Propose a model modification that could resolve this discrepancy.

??? success "Solution to Exercise 6"
    **Diagnosis: term-structure effect (a form of model drift).** The systematic disagreement $\hat{\kappa}_{\text{short}} \approx 5$ versus $\hat{\kappa}_{\text{long}} \approx 1.5$ is not parameter drift (which would show temporal variation, not cross-sectional disagreement at a single point in time). It is evidence of **model drift** manifesting as a term-structure effect.

    In the Heston model, $\kappa$ is a scalar constant that governs mean reversion at all time horizons. However, the true variance process may exhibit different mean-reversion behavior at different horizons:

    - **Short maturities** are sensitive to the near-term dynamics of variance, which may revert quickly (high effective $\kappa$) because intraday and weekly volatility clustering dissipates rapidly.
    - **Long maturities** are sensitive to the long-run persistence of variance, which may revert slowly (low effective $\kappa$) because structural volatility regimes persist for months or years.

    A single $\kappa$ cannot capture both behaviors simultaneously, so subsample calibration yields systematically different values. This is a cross-sectional inconsistency that indicates the model is misspecified: the true variance dynamics are not a simple CIR process with constant parameters.

    **Model modifications:**

    - **Multi-factor stochastic volatility.** Replace the single variance factor with two factors: a fast-reverting component $v_t^{(1)}$ (with high $\kappa_1$) and a slow-reverting component $v_t^{(2)}$ (with low $\kappa_2$). The total variance is $v_t = v_t^{(1)} + v_t^{(2)}$. Short-maturity options are primarily sensitive to $v_t^{(1)}$, while long-maturity options depend on both, resolving the term-structure effect.
    - **Maturity-dependent mean reversion.** Allow $\kappa(T)$ to be a function of maturity. While this breaks the strict SDE interpretation (a single process cannot have maturity-dependent parameters), it is used in practice as a calibration device and is theoretically justified in certain limiting regimes.
    - **Rough volatility models.** Models based on fractional Brownian motion (e.g., the rough Bergomi model) naturally generate different effective mean-reversion rates at different time scales through the Hurst parameter $H < 1/2$, unifying short-term clustering and long-term persistence in a single framework.

---

**Exercise 7.** Within the SR 11-7 framework for model risk management, explain how the distinction between parameter drift and model drift affects: (a) the frequency of model revalidation, (b) the size of model risk reserves, and (c) the decision to retire a model in favor of a more complex alternative. Give a concrete decision rule for when model drift is severe enough to warrant model replacement.

??? success "Solution to Exercise 7"
    **(a) Frequency of model revalidation.**

    - **Parameter drift:** If parameter changes are genuine and the model remains appropriate, revalidation can follow a standard schedule (e.g., annual). The focus is on confirming that parameter dynamics remain within expected bounds and that the model's structural assumptions still hold. Monitoring consists of tracking parameter paths and verifying they correlate with economic drivers.
    - **Model drift:** If parameter changes are driven by misspecification, more frequent revalidation is warranted because the model's adequacy is in question. The validator should revalidate whenever diagnostic indicators (boundary clustering, systematic residuals, cross-sectional inconsistency) breach thresholds. Quarterly or even monthly revalidation may be necessary in stressed markets.

    **(b) Size of model risk reserves.**

    - **Parameter drift:** Reserves cover the range of plausible parameter values weighted by their likelihood. This is quantifiable from historical parameter distributions and can be computed as the difference between prices at extreme parameter quantiles (e.g., 1st and 99th percentiles). Reserves are typically moderate because the model is trusted and parameter uncertainty is bounded.
    - **Model drift:** Reserves must be larger because they cover not only parameter uncertainty but also the unknown magnitude of model misspecification. A common approach is to compute the price difference between the current model and one or more alternative models (e.g., Heston vs. Bates vs. rough volatility), and reserve the maximum discrepancy. Model drift implies that the model's error bounds are themselves uncertain, requiring a more conservative reserve.

    **(c) Decision to retire a model.**

    - **Parameter drift:** Does not motivate model retirement. The model is appropriate; only the estimation procedure or parameter dynamics need attention. Retirement would be premature and wasteful.
    - **Model drift:** If severe and persistent, motivates retirement. The model's structural assumptions are violated, and no amount of recalibration can fix a fundamental misfit.

    **Concrete decision rule for model replacement.** A model should be flagged for replacement when all of the following hold simultaneously for three or more consecutive quarters:

    1. The encompassing test shows that an alternative model reduces parameter volatility by more than 50% (indicating the current model's parameter instability is largely model drift).
    2. Out-of-sample prediction errors exhibit serial correlation with Ljung--Box $p$-value below 0.01.
    3. Calibration residuals exceed 2 bid-ask spreads for more than 20% of observed instruments on more than 50% of trading days.
    4. The model risk reserve attributable to model uncertainty (as opposed to parameter uncertainty) exceeds a material threshold (e.g., 10% of the book's total vega P&L over the quarter).

    If these conditions are met, the model validation team should initiate a formal model change process, including parallel running of the replacement model, impact analysis on the trading book, and regulatory notification.
