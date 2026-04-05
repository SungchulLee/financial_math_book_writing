# Recalibration Problem

In practice, models are recalibrated repeatedly as new market data arrive. This creates the **recalibration problem**: parameters change over time in ways that may be inconsistent with the model's own dynamics, leading to instability, unexplained P&L, and hedging errors.

---

## Static calibration versus dynamic usage

A model calibrated at time $t$ is typically used to:

- price instruments at time $t$,
- compute Greeks for hedging,
- hedge positions over $[t, t + \Delta t]$.

If the model is recalibrated at $t + \Delta t$ to new data, the parameter shift

$$
\theta_t \longrightarrow \theta_{t+\Delta t}
$$

can introduce artificial P&L unrelated to actual market moves.

### The fundamental tension

Consider a stochastic volatility model with parameters $\theta = (\kappa, \bar{v}, \sigma_v, \rho, v_0)$. The model specifies dynamics for the variance process, yet:

- The calibrated $v_0$ at time $t$ need not equal the model-implied $v_t$ evolved from yesterday's calibration.
- Long-run mean $\bar{v}$ and mean-reversion $\kappa$ may jump without any corresponding market event.

This creates an inconsistency: the model's own dynamics are not respected by recalibration.

---

## Sources of recalibration instability

Parameter changes arise from multiple sources:

### 1. Genuine market regime shifts

Markets do change: volatility regimes shift, correlations evolve, risk premia vary. Some parameter movement reflects real economic changes.

### 2. Noise in quotes and surface construction

Bid-ask spreads, stale quotes, and interpolation artifacts introduce noise. Calibration to noisy data produces noisy parameters.

### 3. Model misspecification

If the true data-generating process lies outside the model class, calibration compensates by shifting parameters. This creates spurious parameter dynamics.

### 4. Ill-posed calibration objectives

Weakly identified parameters can jump dramatically in response to small data changes. The Jacobian's small singular values amplify noise.

### 5. Numerical instability

Different optimizer initializations or convergence criteria can yield different local minima, causing apparent parameter jumps.

---

## Quantifying recalibration instability

### Day-over-day parameter changes

Let $\hat{\theta}_t$ denote calibrated parameters on day $t$. Define:

$$
\Delta\theta_t = \hat{\theta}_t - \hat{\theta}_{t-1}
$$

Unstable calibration exhibits:

- Large $\|\Delta\theta_t\|$ on quiet market days.
- High variance of $\Delta\theta_t$ relative to market moves.
- Sign changes in $\Delta\theta_t$ components (oscillation).

### Parameter volatility

Compute rolling standard deviation of each parameter:

$$
\text{Vol}_T(\theta_i) = \sqrt{\frac{1}{T} \sum_{t=1}^{T} (\theta_{i,t} - \bar{\theta}_i)^2}
$$

Compare to economically plausible variation. If $\text{Vol}(\rho)$ implies correlation swinging from $-0.9$ to $-0.5$ weekly, something is wrong.

### Explained versus unexplained P&L

Decompose daily P&L:

$$
\text{P\&L} = \underbrace{\Delta \cdot \Delta S + \frac{1}{2}\Gamma \cdot (\Delta S)^2 + \text{Vega} \cdot \Delta\sigma + \Theta \cdot \Delta t}_{\text{explained}} + \underbrace{\text{residual}}_{\text{unexplained}}
$$

Recalibration-induced P&L shows up as unexplained residual even when market moves are modest.

---

## Impact on hedging and P&L

### Self-financing failure

In continuous-time theory, a delta-hedged portfolio is self-financing. But if parameters jump:

$$
\Delta_t \ne \Delta_{t-}
$$

discontinuously, the rebalancing cost is non-zero and unhedged.

### Greeks instability

Greeks depend on calibrated parameters:

$$
\text{Vega}(\hat{\theta}_t) \ne \text{Vega}(\hat{\theta}_{t-1})
$$

If $\hat{\theta}$ jumps, hedges based on yesterday's Greeks are stale.

### Exotic pricing inconsistency

A barrier option priced on day $t$ with $\hat{\theta}_t$ may have a materially different value than the same option repriced on day $t+1$ with $\hat{\theta}_{t+1}$, even if the spot price is unchanged.

### Example: Heston model instability

Suppose day 1 calibration yields $v_0 = 0.04$, $\kappa = 2$, $\bar{v} = 0.04$. Day 2 calibration yields $v_0 = 0.05$, $\kappa = 1.5$, $\bar{v} = 0.05$.

- The $25\%$ jump in $v_0$ implies a volatility spike not reflected in realized vol.
- The $\kappa$ change affects term structure and exotic pricing.
- Without a market event, this is pure calibration noise.

---

## Common practitioner responses

### 1. Parameter smoothing

Apply exponential smoothing:

$$
\theta_t^{\text{smooth}} = \lambda \hat{\theta}_t + (1 - \lambda) \theta_{t-1}^{\text{smooth}}
$$

**Pros:** Reduces day-to-day noise.

**Cons:** Introduces lag; may miss genuine regime changes; no theoretical justification.

### 2. Freezing parameters

Hold certain parameters (e.g., $\kappa$, $\bar{v}$) fixed over extended periods; recalibrate only $v_0$ and $\rho$ daily.

**Pros:** Reduces degrees of freedom; improves stability.

**Cons:** Arbitrary choice of which to freeze; can accumulate misfit.

### 3. Hierarchical calibration

Calibrate slowly-moving parameters (mean reversion, long-run levels) to historical data or long-dated options. Calibrate fast-moving parameters (spot vol, correlation) daily to short-dated options.

**Pros:** Aligns parameter dynamics with economic intuition.

**Cons:** Requires judgment on time scales; still ad-hoc.

### 4. Regularization toward prior

Use Tikhonov regularization pulling toward yesterday's parameters:

$$
\min_\theta \; \mathcal{L}(\theta) + \lambda \|\theta - \hat{\theta}_{t-1}\|^2
$$

**Pros:** Principled; controls jump magnitude.

**Cons:** Choice of $\lambda$; may under-react to genuine changes.

### 5. Regime-switching models

Allow discrete regimes with different parameter sets; use filtering to infer the current regime.

**Pros:** Explicitly models structural breaks.

**Cons:** Complexity; regime identification is itself noisy.

---

## The deeper problem: model inconsistency

All these approaches are patches. The fundamental issue is that:

> **A model calibrated statically at each point in time does not define a consistent stochastic process for parameters.**

If we calibrate $\theta_t$ at each $t$, the sequence $\{\theta_t\}$ is an empirical time series, not a model output. The model provides no guidance on how $\theta$ should evolve.

This motivates **forward-consistent** and **time-consistent** modeling frameworks (see next sections).

---

## Diagnostic tools

### Parameter stability plots

Plot calibrated parameters over time. Look for:

- Excessive volatility on quiet days.
- Correlation with market moves (expected) versus decorrelation (problematic).
- Boundary clustering (parameters hitting constraints).

### Bootstrap sensitivity

Perturb market quotes within bid-ask; recalibrate; examine parameter distribution. Wide distributions indicate weak identifiability.

### Objective function landscape

Plot calibration loss as a function of individual parameters. Flat regions indicate degeneracy; multiple minima indicate non-convexity.

### Out-of-sample fit

Calibrate to a subset of instruments; test fit on held-out instruments. Overfitting to noise shows up as poor out-of-sample performance.

---

## Key takeaways

- Recalibration is unavoidable: markets evolve, and models must track them.
- Parameter jumps are often noise, not signal.
- Frequent recalibration can destabilize hedging and generate unexplained P&L.
- Practitioner responses (smoothing, freezing, regularization) are ad-hoc but useful.
- The root cause is inconsistency between static calibration and dynamic model usage.
- Forward-consistent frameworks provide a principled alternative.

---

## Further reading

- Rebonato, *Volatility and Correlation* (practitioner perspective on recalibration).
- Andersen & Piterbarg, *Interest Rate Modeling* (calibration stability discussions).
- Cont, "Model Uncertainty and Its Impact on Pricing" (model risk from recalibration).
- Guyon & Henry-Labordère, *Nonlinear Option Pricing* (dynamic calibration issues).

---

## Exercises

**Exercise 1.** A Heston model is calibrated on day $t$ with $\hat{v}_0 = 0.04$ and $\kappa = 2.0$, $\bar{v} = 0.04$, $\sigma_v = 0.3$. Using the exact conditional expectation $\mathbb{E}[v_{t+\Delta t}] = \bar{v} + (v_0 - \bar{v})e^{-\kappa \Delta t}$ with $\Delta t = 1/252$, compute the model-predicted variance for day $t+1$. If recalibration on day $t+1$ yields $\hat{v}_0^{\text{new}} = 0.052$, compute the discrepancy and discuss whether this is consistent with model dynamics.

??? success "Solution to Exercise 1"
    **Model-predicted variance for day $t+1$.** Using the exact conditional expectation formula for the CIR process:

    $$
    \mathbb{E}[v_{t+\Delta t}] = \bar{v} + (v_0 - \bar{v})e^{-\kappa\,\Delta t}
    $$

    With $v_0 = 0.04$, $\bar{v} = 0.04$, $\kappa = 2.0$, and $\Delta t = 1/252$:

    $$
    \mathbb{E}[v_{t+\Delta t}] = 0.04 + (0.04 - 0.04)e^{-2/252} = 0.04
    $$

    Since $v_0 = \bar{v}$, the expected variance is unchanged at 0.04. To assess the plausibility of deviations, compute the conditional standard deviation. For the CIR process:

    $$
    \text{Var}(v_{t+\Delta t}) = \frac{v_0 \sigma_v^2}{\kappa}\left(e^{-\kappa\,\Delta t} - e^{-2\kappa\,\Delta t}\right) + \frac{\bar{v}\sigma_v^2}{2\kappa}\left(1 - e^{-\kappa\,\Delta t}\right)^2
    $$

    Substituting values:

    $$
    \text{Var}(v_{t+\Delta t}) = \frac{0.04 \times 0.09}{2}(e^{-2/252} - e^{-4/252}) + \frac{0.04 \times 0.09}{4}(1 - e^{-2/252})^2
    $$

    For small $\Delta t$, we can approximate $e^{-\kappa\Delta t} \approx 1 - \kappa\Delta t$:

    $$
    \text{Var}(v_{t+\Delta t}) \approx v_0\,\sigma_v^2\,\Delta t = 0.04 \times 0.09 \times \frac{1}{252} \approx 1.43 \times 10^{-5}
    $$

    So $\text{Std}(v_{t+\Delta t}) \approx 0.00378$.

    **Discrepancy with recalibration.** If recalibration yields $\hat{v}_0^{\text{new}} = 0.052$, the discrepancy is

    $$
    \hat{v}_0^{\text{new}} - \mathbb{E}[v_{t+\Delta t}] = 0.052 - 0.04 = 0.012
    $$

    In units of the model's conditional standard deviation:

    $$
    \frac{0.012}{0.00378} \approx 3.17 \text{ standard deviations}
    $$

    **Discussion.** A 3.2-sigma event has probability approximately 0.08% under the model's Gaussian approximation. While not impossible as a single occurrence, if such discrepancies occur regularly (e.g., on more than 1--2% of days), this is inconsistent with the model dynamics. The model predicts that $v_0$ should remain close to 0.04 on a daily basis, but recalibration says it jumped to 0.052. This discrepancy likely reflects a combination of:

    - Genuine variance change not fully captured by the diffusive CIR model (missing jumps in variance).
    - Model misspecification causing $\hat{v}_0$ to absorb errors in other parameters.
    - The recalibrated $\hat{v}_0^{\text{new}}$ representing an "effective" spot variance that differs from the CIR state variable.

---

**Exercise 2.** Define the parameter volatility metric $\text{Vol}_T(\theta_i) = \sqrt{\frac{1}{T}\sum_{t=1}^T (\theta_{i,t} - \bar{\theta}_i)^2}$. Suppose that over 60 trading days, the calibrated $\rho$ values for a Heston model have mean $\bar{\rho} = -0.72$ and standard deviation $0.09$, while the S&P 500 realized volatility changed by less than 1%. Argue that this level of $\rho$ variation is more indicative of calibration noise than genuine parameter drift.

??? success "Solution to Exercise 2"
    **Setting up the argument.** The Heston $\rho$ parameter measures the correlation between spot and variance shocks and is an economic quantity tied to the leverage effect. Over 60 trading days with the S&P 500 realized volatility changing by less than 1%, the macro environment is essentially stable.

    **Quantifying the variation.** With $\bar{\rho} = -0.72$ and standard deviation 0.09, the calibrated $\rho$ fluctuates roughly over the range $[-0.90, -0.54]$ (two-sigma band). This means:

    - The implied skew of the volatility surface oscillates significantly, even though realized market conditions are stable.
    - The range of 0.36 in $\rho$ translates to substantial changes in the implied volatility skew (roughly 1--3 vol points difference in 25-delta put-call skew, depending on maturity).

    **Why this is calibration noise.** If the variation were genuine parameter drift, we would expect:

    1. **Correlation with observables:** $\rho$ changes should correlate with realized spot-volatility correlation, VIX movements, or other market indicators. With realized vol changing less than 1%, there is no economic driver for $\rho$ to move by 12.5% of its absolute value (0.09/0.72).

    2. **Smoothness:** Genuine economic correlation shifts are gradual. If $\rho$ oscillates rapidly (e.g., flipping from $-0.65$ to $-0.80$ and back within a week) without corresponding market events, this is noise.

    3. **Magnitude relative to identification.** A bootstrap analysis would likely show that the standard error of $\hat{\rho}$ from a single calibration is of order 0.05--0.10, comparable to or larger than the observed time-series standard deviation of 0.09. This means the observed variation is within the range that estimation uncertainty alone can explain.

    **Conclusion.** The 0.09 standard deviation in $\rho$ over a quiet 60-day period is more consistent with calibration noise (sensitivity to small quote changes, optimizer variability, and weak identification in the $\rho$ direction) than with genuine parameter drift. A practitioner should consider regularization, smoothing, or fixing $\rho$ during stable periods.

---

**Exercise 3.** Write down the P&L decomposition for a delta- and vega-hedged portfolio of exotic options. Identify the term that corresponds to recalibration-induced P&L. For a book with vega exposure of \$50,000 per vol point, estimate the unexplained P&L if recalibration shifts the ATM implied volatility by 0.3 vol points without any actual market move.

??? success "Solution to Exercise 3"
    **P&L decomposition.** For a portfolio of exotic options with value $V$ that is delta- and vega-hedged, the daily P&L can be decomposed as

    $$
    \text{P\&L} = \underbrace{\frac{\partial V}{\partial S}\Delta S + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}(\Delta S)^2 + \frac{\partial V}{\partial \sigma}\Delta\sigma + \frac{\partial V}{\partial t}\Delta t}_{\text{explained by Greeks}} + \underbrace{\sum_k \frac{\partial V}{\partial \theta_k}\Delta\theta_k}_{\text{recalibration P\&L}} + \underbrace{\text{higher-order and cross terms}}_{\text{residual}}
    $$

    Since the portfolio is delta-hedged, $\frac{\partial V}{\partial S}\Delta S$ is offset by the hedge. Since it is vega-hedged, $\frac{\partial V}{\partial \sigma}\Delta\sigma$ for the primary vol exposure is also offset.

    **Recalibration-induced P&L.** The term $\sum_k \frac{\partial V}{\partial \theta_k}\Delta\theta_k$ captures the P&L from parameter changes that are not hedged. This includes changes in all calibrated parameters: $v_0$, $\kappa$, $\bar{v}$, $\sigma_v$, $\rho$. When recalibration shifts parameters without a corresponding market move, this entire term is "unexplained" P&L.

    **Numerical estimate.** With vega exposure of \$50,000 per vol point, a recalibration-induced shift of 0.3 vol points in ATM implied volatility (without any actual market move) generates

    $$
    \text{Unexplained P\&L} = \$50{,}000 \times 0.3 = \$15{,}000
    $$

    This is a single-day effect. Over a year of daily recalibration, if such shifts are random with zero mean, they contribute to P&L volatility:

    $$
    \text{Annual P\&L vol from recalibration} \approx \$15{,}000 \times \sqrt{252} \approx \$238{,}000
    $$

    This is economically significant: it represents pure noise in the P&L that cannot be attributed to any market risk factor, complicating risk management and performance measurement.

---

**Exercise 4.** Consider exponential smoothing $\theta_t^{\text{smooth}} = \lambda\hat{\theta}_t + (1-\lambda)\theta_{t-1}^{\text{smooth}}$ with $\lambda = 0.3$. Starting from $\theta_0^{\text{smooth}} = 0.04$, compute $\theta_t^{\text{smooth}}$ for $t = 1, 2, 3, 4$ given raw calibrated values $\hat{\theta}_1 = 0.05$, $\hat{\theta}_2 = 0.038$, $\hat{\theta}_3 = 0.055$, $\hat{\theta}_4 = 0.041$. Compare the smoothed path to the raw path and discuss the lag introduced by smoothing.

??? success "Solution to Exercise 4"
    **Computing the smoothed path.** The recursion is $\theta_t^{\text{smooth}} = \lambda\hat{\theta}_t + (1-\lambda)\theta_{t-1}^{\text{smooth}}$ with $\lambda = 0.3$ and $\theta_0^{\text{smooth}} = 0.04$.

    **Step $t = 1$:**

    $$
    \theta_1^{\text{smooth}} = 0.3 \times 0.05 + 0.7 \times 0.04 = 0.015 + 0.028 = 0.043
    $$

    **Step $t = 2$:**

    $$
    \theta_2^{\text{smooth}} = 0.3 \times 0.038 + 0.7 \times 0.043 = 0.0114 + 0.0301 = 0.0415
    $$

    **Step $t = 3$:**

    $$
    \theta_3^{\text{smooth}} = 0.3 \times 0.055 + 0.7 \times 0.0415 = 0.0165 + 0.02905 = 0.04555
    $$

    **Step $t = 4$:**

    $$
    \theta_4^{\text{smooth}} = 0.3 \times 0.041 + 0.7 \times 0.04555 = 0.0123 + 0.031885 = 0.044185
    $$

    **Summary table:**

    | $t$ | $\hat{\theta}_t$ (raw) | $\theta_t^{\text{smooth}}$ |
    |:---:|:---:|:---:|
    | 0 | -- | 0.0400 |
    | 1 | 0.050 | 0.0430 |
    | 2 | 0.038 | 0.0415 |
    | 3 | 0.055 | 0.0456 |
    | 4 | 0.041 | 0.0442 |

    **Comparison and lag discussion.** The raw path jumps: $0.04 \to 0.05 \to 0.038 \to 0.055 \to 0.041$ (range of 0.017). The smoothed path is much more stable: $0.04 \to 0.043 \to 0.0415 \to 0.0456 \to 0.0442$ (range of 0.0056).

    The smoothing reduces volatility by roughly a factor of 3 but introduces lag:

    - At $t = 1$, the raw value jumps to 0.050 but the smoothed value only reaches 0.043 (capturing 30% of the move).
    - At $t = 2$, the raw value drops to 0.038 but the smoothed value is still at 0.0415 (above the raw value, reflecting the lingering influence of the $t=1$ spike).
    - The smoothed path is always between the raw value and the previous smoothed value, and responds sluggishly to genuine changes.

    The lag is controlled by $\lambda$: smaller $\lambda$ means more smoothing but more lag. With $\lambda = 0.3$, the half-life of the exponential weight is $-\ln(2)/\ln(0.7) \approx 1.94$ steps, meaning it takes about 2 days for half of a genuine level shift to be reflected in the smoothed parameter.

---

**Exercise 5.** In Tikhonov-regularized recalibration, $\min_\theta \mathcal{L}(\theta) + \lambda\|\theta - \hat{\theta}_{t-1}\|^2$, derive the first-order optimality condition. Show that the solution is a weighted average between the unconstrained minimizer $\hat{\theta}_t^{\text{MLE}}$ and the prior $\hat{\theta}_{t-1}$. Express the weights in terms of $\lambda$ and the Hessian of $\mathcal{L}$ at the optimum.

??? success "Solution to Exercise 5"
    **First-order optimality condition.** The Tikhonov-regularized objective is

    $$
    J(\theta) = \mathcal{L}(\theta) + \lambda\|\theta - \hat{\theta}_{t-1}\|^2
    $$

    Setting the gradient to zero:

    $$
    \nabla_\theta J(\theta) = \nabla\mathcal{L}(\theta) + 2\lambda(\theta - \hat{\theta}_{t-1}) = 0
    $$

    **Showing the weighted-average structure.** Let $\hat{\theta}_t^{\text{MLE}}$ denote the unconstrained minimizer of $\mathcal{L}$, so $\nabla\mathcal{L}(\hat{\theta}_t^{\text{MLE}}) = 0$. Perform a second-order Taylor expansion of $\nabla\mathcal{L}$ around $\hat{\theta}_t^{\text{MLE}}$:

    $$
    \nabla\mathcal{L}(\theta) \approx \nabla^2\mathcal{L}(\hat{\theta}_t^{\text{MLE}})(\theta - \hat{\theta}_t^{\text{MLE}}) = \mathcal{H}(\theta - \hat{\theta}_t^{\text{MLE}})
    $$

    where $\mathcal{H} = \nabla^2\mathcal{L}(\hat{\theta}_t^{\text{MLE}})$ is the Hessian of the loss at the MLE. Substituting into the optimality condition:

    $$
    \mathcal{H}(\theta^\star - \hat{\theta}_t^{\text{MLE}}) + 2\lambda(\theta^\star - \hat{\theta}_{t-1}) = 0
    $$

    Solving for $\theta^\star$:

    $$
    (\mathcal{H} + 2\lambda I)\theta^\star = \mathcal{H}\hat{\theta}_t^{\text{MLE}} + 2\lambda\hat{\theta}_{t-1}
    $$

    $$
    \theta^\star = (\mathcal{H} + 2\lambda I)^{-1}(\mathcal{H}\hat{\theta}_t^{\text{MLE}} + 2\lambda\hat{\theta}_{t-1})
    $$

    This can be rewritten as a weighted average:

    $$
    \theta^\star = W\,\hat{\theta}_t^{\text{MLE}} + (I - W)\hat{\theta}_{t-1}
    $$

    where the weight matrix is

    $$
    W = (\mathcal{H} + 2\lambda I)^{-1}\mathcal{H}
    $$

    and $I - W = (\mathcal{H} + 2\lambda I)^{-1}(2\lambda I)$.

    **Interpretation.** In the eigenbasis of $\mathcal{H}$, with eigenvalues $h_k$, the weight on the MLE for the $k$-th direction is $h_k/(h_k + 2\lambda)$. For well-identified parameters (large $h_k$), the weight approaches 1 (trust the data). For weakly identified parameters (small $h_k$), the weight approaches 0 (trust the prior $\hat{\theta}_{t-1}$). This is precisely the desired behavior: regularization primarily stabilizes poorly determined parameters.

---

**Exercise 6.** A practitioner freezes $(\kappa, \bar{v}, \sigma_v)$ for one month while recalibrating $(v_0, \rho)$ daily. After one month, the frozen parameters are re-estimated. Discuss the advantages and risks of this hierarchical calibration approach. Under what market conditions might this strategy fail badly? Propose a criterion for triggering early re-estimation of the frozen parameters.

??? success "Solution to Exercise 6"
    **Advantages of hierarchical calibration:**

    - **Reduced degrees of freedom.** With only $(v_0, \rho)$ free daily (2 parameters), the calibration problem is better conditioned than the full 5-parameter problem. This reduces the risk of overfitting to noise and produces more stable daily parameter paths.
    - **Alignment with time scales.** $(\kappa, \bar{v}, \sigma_v)$ are structural parameters that reflect long-term market properties (mean-reversion speed, long-run volatility level, vol-of-vol). These change slowly and benefit from estimation over longer windows. $(v_0, \rho)$ reflect current market conditions and must track daily.
    - **Computational efficiency.** A 2-parameter optimization is faster and more reliable than a 5-parameter one, especially when the pricing function is expensive.

    **Risks:**

    - **Accumulating misfit.** If the frozen parameters drift away from their true values during the month, the daily calibration of $(v_0, \rho)$ must compensate, distorting their interpretation. For example, if $\bar{v}$ truly increases but is frozen, $v_0$ will be biased upward to absorb the misfit.
    - **Inability to respond to regime changes.** If a market event (e.g., a central bank announcement, a crash) fundamentally changes the mean-reversion structure or vol-of-vol, waiting until month-end to recalibrate $(\kappa, \bar{v}, \sigma_v)$ can lead to severely mispriced exotics and incorrect hedges.
    - **Cross-parameter contamination.** The frozen parameters affect the shape of the implied vol surface. If they are wrong, the daily-calibrated $(v_0, \rho)$ may take economically implausible values to compensate.

    **Market conditions where this strategy fails badly:**

    - Sudden regime shifts (financial crises, pandemic onset) where all parameters change simultaneously.
    - Persistent trending markets where $\bar{v}$ shifts gradually but significantly over a month.
    - Periods of extreme stress where $\sigma_v$ increases sharply and the frozen value is far too low, causing poor wing fitting and incorrect exotic prices.

    **Criterion for early re-estimation.** Trigger re-estimation of frozen parameters when any of the following holds:

    - The daily calibration residual (RMSE of implied vol fit) exceeds twice its rolling 20-day median for 3 consecutive days.
    - $(v_0, \rho)$ hit their constraint bounds or take values outside their historical 2-sigma range.
    - The VIX moves by more than 5 points in a single week (indicating a regime change).
    - The P&L attribution residual (unexplained P&L) exceeds a predefined threshold (e.g., more than 2 standard deviations of historical daily unexplained P&L) for 2 or more consecutive days.

---

**Exercise 7.** Design a diagnostic dashboard for monitoring recalibration stability. List at least five metrics or plots that should be included, explain what each one measures, and describe the warning signal that would trigger further investigation. For one of these metrics, propose a specific quantitative threshold above which the calibration should be flagged as unstable.

??? success "Solution to Exercise 7"
    **Diagnostic dashboard for recalibration stability.** The following five metrics and plots should be included:

    **1. Parameter time-series plot with rolling confidence bands.**

    - *What it measures:* The evolution of each calibrated parameter $\hat{\theta}_{i,t}$ over time, overlaid with a rolling mean and $\pm 2\sigma$ band (e.g., 20-day rolling window).
    - *Warning signal:* Parameters frequently breaching the 2-sigma band, rapid oscillations on quiet market days, or a persistent trend that diverges from the rolling mean.

    **2. Day-over-day parameter change magnitude $\|\Delta\theta_t\|$.**

    - *What it measures:* The Euclidean norm of the daily parameter change vector $\Delta\theta_t = \hat{\theta}_t - \hat{\theta}_{t-1}$, normalized by the parameter scale. This quantifies recalibration instability in a single number per day.
    - *Warning signal:* Spikes in $\|\Delta\theta_t\|$ that do not coincide with significant market moves (e.g., large $\|\Delta\theta_t\|$ on days when $|\Delta S/S| < 0.5\%$ and $|\Delta\text{VIX}| < 0.5$).
    - *Specific threshold:* Flag the calibration as unstable if $\|\Delta\theta_t\|$ exceeds its 60-day rolling 95th percentile on a day when realized market moves are below their 25th percentile. Concretely, for the Heston model, if the normalized parameter change $\sqrt{\sum_k (\Delta\theta_k / \text{scale}_k)^2}$ exceeds 3.0 on a quiet day (where scales are the rolling standard deviations of each parameter), trigger an investigation.

    **3. Calibration residual RMSE time series.**

    - *What it measures:* The root-mean-square error of the calibrated model's implied vols versus market implied vols across all instruments, plotted daily.
    - *Warning signal:* Increasing trend in RMSE (model fit is deteriorating), or RMSE consistently above the average bid-ask spread (model cannot fit within market uncertainty).

    **4. Unexplained P&L attribution plot.**

    - *What it measures:* The daily unexplained P&L (total P&L minus Greek-explained P&L) for the trading book. This captures the economic impact of recalibration jumps.
    - *Warning signal:* Unexplained P&L that is large relative to explained P&L, serially correlated (indicating systematic model issues), or consistently of one sign (indicating bias).

    **5. Bootstrap parameter distribution plot.**

    - *What it measures:* For each calibration date (or a representative sample), the distribution of parameters obtained by perturbing market quotes within bid-ask spreads and recalibrating 200+ times. Displayed as box plots or violin plots over time.
    - *Warning signal:* Wide bootstrap distributions (weak identification), bootstrap distributions that do not overlap with the previous day's distribution (genuine change vs. noise is ambiguous), or bimodal distributions (multiple local minima in the calibration objective).

    **Additional useful metrics (beyond the required five):**

    - **Parameter correlation matrix heatmap** (identifies parameters that move together, suggesting redundancy or compensation effects).
    - **Calibration residual structure plot** (residuals vs. strike/maturity, to detect systematic misfit patterns indicating model drift).
