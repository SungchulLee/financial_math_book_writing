# Forward Consistency

**Forward consistency** aims to ensure that a model calibrated today remains internally consistent when viewed from tomorrow's perspective. It provides a theoretical framework for mitigating the recalibration problem by requiring that model dynamics and calibration be mutually compatible.

---

## Definition of forward consistency

### Informal statement

A model is forward consistent if:

1. Parameters calibrated at time $t$ to market data,
2. when evolved according to the model's own dynamics to time $t + \Delta t$,
3. generate prices consistent with what recalibration at $t + \Delta t$ would produce.

In other words, **recalibration should not contradict the model's implied evolution**.

### Formal definition

Let $\theta_t$ denote calibrated parameters at time $t$, and let $\Phi_{t \to t+\Delta t}(\theta_t, \omega)$ denote the model-implied parameter evolution (possibly stochastic, depending on path $\omega$).

A model is **forward consistent** if, for typical market realizations:

$$
\hat{\theta}_{t+\Delta t}^{\text{calib}} \approx \Phi_{t \to t+\Delta t}(\hat{\theta}_t, \omega),
$$

where $\hat{\theta}_{t+\Delta t}^{\text{calib}}$ is the result of fresh calibration at $t + \Delta t$.

### Why this matters

If forward consistency fails:

- The model provides no guidance on how to evolve positions.
- Hedging becomes path-dependent in unmodeled ways.
- P&L attribution breaks down.
- Exotics with future calibration dates (e.g., cliquets) are inconsistently priced.

---

## Forward consistency in interest-rate models

The Heath–Jarrow–Morton (HJM) framework provides the canonical example of forward consistency.

### The HJM approach

In HJM, the entire forward rate curve $f(t, T)$ for $T \ge t$ is modeled as the state variable:

$$
df(t, T) = \alpha(t, T) \, dt + \sigma(t, T) \, dW_t.
$$

The no-arbitrage drift condition determines $\alpha$ in terms of $\sigma$:

$$
\alpha(t, T) = \sigma(t, T) \int_t^T \sigma(t, u) \, du.
$$

### Why HJM is forward consistent

At time $t$, the model is "calibrated" by observing the current forward curve $f(t, \cdot)$. The model then specifies exactly how this curve evolves. At time $t + \Delta t$:

- The curve $f(t + \Delta t, \cdot)$ is determined by the model dynamics.
- No recalibration is needed (or possible) for the curve shape.
- Only the volatility structure $\sigma(t, T)$ may be recalibrated.

This eliminates the inconsistency between calibration and dynamics for the primary state variable.

### Limitations

- HJM requires specifying a volatility function $\sigma(t, T)$ across all maturities.
- The infinite-dimensional state is often reduced to finite factors (Hull–White, Gaussian HJM).
- Volatility recalibration can still introduce inconsistencies.

---

## Challenges in equity and volatility models

Equity volatility models typically have different structure:

### Low-dimensional parameterization

Models like Heston use a small number of parameters ($\kappa$, $\bar{v}$, $\sigma_v$, $\rho$, $v_0$) to generate an entire implied volatility surface. This is convenient but creates a mismatch:

- The parameter space is $\mathbb{R}^5$.
- The implied vol surface is (effectively) infinite-dimensional.
- A 5-parameter model cannot capture arbitrary surface dynamics.

### The calibration-dynamics gap

In Heston, the variance process follows:

$$
dv_t = \kappa(\bar{v} - v_t) \, dt + \sigma_v \sqrt{v_t} \, dW_t^v.
$$

The model specifies how $v_t$ evolves, but not how $(\kappa, \bar{v}, \sigma_v, \rho)$ evolve. When we recalibrate:

- $\hat{v}_0^{\text{new}}$ from calibration may differ from $v_{\Delta t}$ evolved under the model.
- $\hat{\kappa}^{\text{new}}$, $\hat{\bar{v}}^{\text{new}}$ are treated as constants but are re-estimated.

This violates forward consistency.

### Result: recalibration is necessary

Unlike HJM, equity vol models cannot fit arbitrary surfaces. The model is misspecified, so recalibration compensates. Forward consistency is structurally violated.

---

## Approaches to restore consistency

Several frameworks attempt to reconcile calibration with dynamics.

### 1. State-extended models

Enlarge the state space to include variables that can track surface dynamics.

**Example: Bergomi's variance curve model**

Model the entire forward variance curve $\xi_t(T) = \mathbb{E}_t[v_T]$ as the state:

$$
d\xi_t(T) = \text{(drift)} \, dt + \eta(T - t) \xi_t(T) \, dW_t.
$$

The forward variance curve is now a state variable, analogous to forward rates in HJM. Calibration becomes observing $\xi_t(\cdot)$ from option prices.

**Advantages:** Forward consistent by construction.

**Disadvantages:** Infinite-dimensional; requires choosing $\eta(\cdot)$; computational complexity.

### 2. Stochastic parameter models

Allow parameters to follow their own stochastic processes:

$$
d\theta_t = \mu_\theta(\theta_t) \, dt + \Sigma_\theta(\theta_t) \, dZ_t.
$$

The parameter process $\theta_t$ is now part of the model. Calibration estimates the current state $\theta_t$, and the model specifies future evolution.

**Challenges:**

- What dynamics for $\theta$? Often ad-hoc.
- Identification: separating parameter uncertainty from parameter dynamics.
- Nested calibration: must calibrate both the base model and the parameter process.

### 3. Term-structure extensions

Extend scalar parameters to term structures:

- Instead of a single $\bar{v}$, use a forward long-run variance curve $\bar{v}(T)$.
- Instead of scalar $\rho$, use maturity-dependent correlation $\rho(T)$.

This increases flexibility to fit the surface and allows smoother recalibration.

### 4. Consistent recalibration (CRC) framework

The CRC framework (Björk, Landén, Svensson; Carmona, Nadtochiy) formalizes the requirement:

> **The calibration map and model dynamics must be consistent.**

Let $\mathcal{C}: \text{(market data)} \to \theta$ be the calibration map. Let $\Phi: \theta_t \to \theta_{t+\Delta t}$ be model-implied evolution. CRC requires:

$$
\mathcal{C}(\text{prices at } t + \Delta t) = \Phi(\mathcal{C}(\text{prices at } t), \omega).
$$

This is a strong constraint that typically cannot be satisfied by standard models. The CRC framework characterizes *which* models and calibration procedures are mutually consistent.

### 5. Market models for volatility

By analogy with LIBOR market models for rates, one can model tradeable volatility instruments (e.g., variance swaps, VIX futures) directly:

$$
d\text{VS}_t(T) = \text{VS}_t(T) \sigma_{\text{VS}}(t, T) \, dW_t.
$$

This ensures that calibration to variance swap prices is consistent with modeled dynamics.

---

## Practical implications

### When forward consistency matters most

- **Cliquets and forward-starting options:** Pricing depends on future calibration.
- **Long-dated exotics:** Inconsistent recalibration accumulates over time.
- **Dynamic hedging of path-dependent options:** Hedge ratios depend on how parameters evolve.
- **Risk management:** Scenario analysis requires consistent future model states.

### When it matters less

- **Short-dated vanillas:** Calibrated daily; recalibration effects are small.
- **Static hedging:** No parameter evolution needed.
- **Relative value trades:** Inconsistencies may cancel across legs.

### Practical compromise

Full forward consistency is often unattainable. A pragmatic approach:

1. Use HJM-style models where possible (rates, variance curves).
2. For low-dimensional models, recalibrate slowly-changing parameters infrequently.
3. Use regularization to penalize parameter jumps.
4. Document model limitations; report parameter uncertainty.
5. Stress test pricing under alternative parameter paths.

---

## Forward consistency and model risk

Forward inconsistency is a form of model risk:

- The model does not fully describe the system.
- Unmodeled parameter dynamics introduce uncertainty.
- P&L explanations are incomplete.

Quantifying this risk requires:

- Estimating typical recalibration magnitude.
- Propagating parameter uncertainty to prices and Greeks.
- Scenario analysis with alternative parameter paths.

---

## Key takeaways

- Forward consistency links calibration across time.
- HJM-style models achieve consistency by modeling the full term structure.
- Low-dimensional equity/vol models are typically not forward consistent.
- Achieving consistency requires richer state dynamics (variance curves, stochastic parameters).
- The CRC framework provides a theoretical criterion for consistency.
- Forward inconsistency is a source of model risk that should be acknowledged and managed.

---

## Further reading

- Heath, Jarrow & Morton, "Bond Pricing and the Term Structure of Interest Rates" (1992).
- Björk & Christensen, "Interest Rate Dynamics and Consistent Forward Rate Curves" (1999).
- Carmona & Nadtochiy, "Local Volatility Dynamic Models" (2009).
- Bergomi, *Stochastic Volatility Modeling* (forward variance models).
- Filipović, *Term-Structure Models: A Graduate Course*.
