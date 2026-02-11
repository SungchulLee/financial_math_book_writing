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
\Delta\theta_t = \hat{\theta}_t - \hat{\theta}_{t-1}.
$$

Unstable calibration exhibits:

- Large $\|\Delta\theta_t\|$ on quiet market days.
- High variance of $\Delta\theta_t$ relative to market moves.
- Sign changes in $\Delta\theta_t$ components (oscillation).

### Parameter volatility

Compute rolling standard deviation of each parameter:

$$
\text{Vol}_T(\theta_i) = \sqrt{\frac{1}{T} \sum_{t=1}^{T} (\theta_{i,t} - \bar{\theta}_i)^2}.
$$

Compare to economically plausible variation. If $\text{Vol}(\rho)$ implies correlation swinging from $-0.9$ to $-0.5$ weekly, something is wrong.

### Explained versus unexplained P&L

Decompose daily P&L:

$$
\text{P\&L} = \underbrace{\Delta \cdot \Delta S + \frac{1}{2}\Gamma \cdot (\Delta S)^2 + \text{Vega} \cdot \Delta\sigma + \Theta \cdot \Delta t}_{\text{explained}} + \underbrace{\text{residual}}_{\text{unexplained}}.
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
\text{Vega}(\hat{\theta}_t) \ne \text{Vega}(\hat{\theta}_{t-1}).
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
\theta_t^{\text{smooth}} = \lambda \hat{\theta}_t + (1 - \lambda) \theta_{t-1}^{\text{smooth}}.
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
\min_\theta \; \mathcal{L}(\theta) + \lambda \|\theta - \hat{\theta}_{t-1}\|^2.
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
