# Dynamic Consistency


## Introduction


**Dynamic consistency** refers to whether a model's implied volatility dynamics are coherent over time. A dynamically consistent model should not contradict itself when re-evaluated at future dates. This is a stringent requirement that most practical models fail to satisfy perfectly, with important consequences for pricing and hedging.

## Definition and Framework


### 1. Formal Definition


A volatility model is **dynamically consistent** if:

1. The model is calibrated to today's implied volatility surface $\sigma_{\text{IV}}^{(0)}(K, T)$
2. The model is evolved forward to time $t$ under its own dynamics
3. The resulting implied surface $\sigma_{\text{IV}}^{(t)}(K, T-t)$ is consistent with what recalibration would produce

**Mathematical formulation:**

Let $\Theta_0$ be the model parameters calibrated at $t=0$. Evolve the model to $t$ to get state $X_t$. The forward-implied surface is:

$$
\sigma_{\text{fwd}}(K, T; X_t, \Theta_0)
$$


Dynamic consistency requires:

$$
\sigma_{\text{fwd}}(K, T; X_t, \Theta_0) \stackrel{d}{=} \sigma_{\text{IV}}(K, T; \text{recalibrated at } t)
$$


### 2. Why Dynamic Consistency Matters


**Pricing:** Exotic options depend on future smile dynamics. Inconsistent models misprice path-dependent products.

**Hedging:** Hedge ratios assume the model's dynamics. Inconsistency leads to hedging errors.

**Recalibration:** Dynamically inconsistent models require frequent recalibration, introducing P&L noise.

## Inconsistencies in Common Models


### 1. Black-Scholes Model


**Status:** Dynamically consistent but unrealistic.

Under Black-Scholes:
- Volatility is constant: $\sigma(t) = \sigma_0$
- The forward smile is flat
- Evolving forward gives the same flat smile

**Problem:** Real smiles are not flat, so Black-Scholes is consistent but wrong.

### 2. Local Volatility Models


**Status:** Dynamically inconsistent.

**Calibration:** Local vol is calibrated to match today's smile exactly.

**Evolution:** Under local vol dynamics:

$$
dS_t = (r-q) S_t dt + \sigma_{\text{loc}}(S_t, t) S_t dW_t
$$


The forward smile **flattens** over time.

**Recalibration:** Tomorrow's market will likely show persistent skew, requiring a new local vol surface.

**Inconsistency:** The model predicts flat forward smiles, but recalibration shows persistent skew.

**Quantitative measure:**

$$
\text{Inconsistency} = \|\sigma_{\text{fwd}}^{\text{model}} - \sigma_{\text{IV}}^{\text{recalibrated}}\|
$$


For local vol, this can be several vol points for long-dated options.

### 3. Stochastic Volatility Models


**Status:** Better but still imperfect.

**Heston model:**
- Forward smile has persistent skew (due to $\rho$)
- Level evolves with $v_t$
- But specific shape may not match recalibrated surface

**Improvement over local vol:**
- Forward skew persists
- Term structure evolves more realistically

**Remaining issues:**
- Smile wings may not match
- Vol-of-vol may need adjustment
- Parameter stability over time

### 4. SABR Model


**Status:** Partially consistent.

SABR with stochastic $\alpha_t$:
- ATM level evolves stochastically
- Skew determined by $\rho$, $\nu$

**Consistency depends on:**
- Whether $\alpha_t$ dynamics match implied vol dynamics
- Parameter stability ($\rho$, $\nu$, $\beta$)

## Consequences for Pricing and Hedging


### 1. Mispricing of Forward-Start Products


**Cliquets:**

$$
\text{Cliquet Price} = \mathbb{E}\left[\sum_i f\left(\frac{S_{t_i}}{S_{t_{i-1}}}\right)\right]
$$


Depends critically on forward smile. Dynamically inconsistent models give:
- Local vol: Underprices cliquets (forward smile too flat)
- Wrong volatility for future periods

**Autocallables:**

Path-dependent barriers interact with forward smile dynamics. Inconsistent models miscalculate:
- Probability of early knockout
- Value of continuation

### 2. Hedging Strategy Failures


**Delta hedging:**

If the model predicts wrong forward smile dynamics:
- Delta hedge ratio is incorrect
- Systematic hedging P&L leakage

**Vega hedging:**

Forward vega exposure depends on forward smile:
- Inconsistent models give wrong forward vega
- Term structure hedges fail

### 3. Recalibration-Induced P&L


**Daily recalibration:**

Recalibrating each day changes model parameters:

$$
\Theta_0 \to \Theta_1 \to \Theta_2 \to \cdots
$$


**P&L impact:**

$$
\text{P\&L}_{\text{recalib}} = P(\Theta_1) - P(\Theta_0)
$$


This is "model P&L" unrelated to market moves.

**Example:** A long-dated exotic may show:
- Market unchanged
- Recalibration changes parameters
- Book shows P&L from parameter change

## Model Design Trade-offs


### 1. Static Fit vs. Dynamic Realism


**Perfect static fit:**
- Local vol matches today's smile exactly
- But forward smile dynamics are unrealistic

**Realistic dynamics:**
- Stochastic vol has better dynamics
- But may not fit today's smile perfectly

**Trade-off:** Cannot have both perfect fit and perfect dynamics.

### 2. Approaches to Improve Consistency


**Additional state variables:**

Adding factors improves dynamics:
- Two-factor stochastic vol
- Stochastic vol-of-vol
- Regime switching

**Cost:** More parameters, harder calibration.

**Time-dependent parameters:**

Allow parameters to vary with time:

$$
\kappa(t), \theta(t), \xi(t)
$$


**Cost:** Loses predictive power for future dynamics.

**Bergomi framework:**

Model forward variance curve directly:

$$
d\xi_t^T = \xi_t^T \omega(T-t) dZ_t
$$


**Advantage:** Direct control over forward smile dynamics.

### 3. Practical Recommendations


| Objective | Recommended Model |
|-----------|-------------------|
| Vanilla pricing | Local vol (exact fit) |
| Simple exotics | Heston (reasonable dynamics) |
| Cliquets | Bergomi (forward smile control) |
| Forward-start | Stochastic vol with calibrated forward smile |

## Testing Dynamic Consistency


### 1. Forward Smile Comparison


**Test procedure:**

1. Calibrate model at $t=0$
2. Evolve model forward to $t$ under simulated paths
3. Compute model-implied forward smile at $t$
4. Compare to recalibrated surface from market data at $t$

**Metric:**

$$
\text{RMSE} = \sqrt{\frac{1}{N}\sum_{i=1}^N \left(\sigma_{\text{fwd},i}^{\text{model}} - \sigma_{\text{IV},i}^{\text{market}}\right)^2}
$$


### 2. Cliquet Price Stability


**Test procedure:**

1. Price a cliquet today
2. Advance one period, observe $S_{t_1}$
3. Reprice remaining periods
4. Compare to original expected continuation value

**Dynamically consistent model:** Revaluation matches expectation.

**Inconsistent model:** Systematic deviation.

### 3. Hedging P&L Analysis


**Test procedure:**

1. Hedge exotic option using model deltas
2. Track hedging P&L over time
3. Decompose into:
   - Market moves (delta, gamma)
   - Vol moves (vega)
   - Recalibration (model inconsistency)

**Dynamically consistent model:** Recalibration P&L is small/zero.

## Advanced Topics


### 1. Market Models for Forward Smile


**Forward smile market model:**

Model the forward smile surface directly:

$$
d\sigma_{\text{fwd}}(m, T_1, T_2; t) = \mu(\cdot) dt + \nu(\cdot) dW_t
$$


**Advantage:** Dynamics specified directly.
**Challenge:** Ensuring no-arbitrage constraints.

### 2. Arbitrage Constraints on Forward Smile


The forward smile must satisfy:
- Calendar spread constraint: forward variance > 0
- Butterfly constraint: forward density > 0
- Consistency with spot smile

**No-arbitrage condition:**

$$
\sigma_{\text{fwd}}^2(T_1, T_2) > 0 \quad \text{for all } T_2 > T_1
$$


### 3. Connection to Variance Swaps


Forward variance swaps provide model-free information about forward volatility:

$$
K_{\text{var}}^{\text{fwd}}(T_1, T_2) = \frac{K_{\text{var}}(T_2) T_2 - K_{\text{var}}(T_1) T_1}{T_2 - T_1}
$$


Dynamically consistent models should match these observables.

## Summary


### Key Concepts

- **Dynamic consistency:** Model dynamics coherent over time
- **Static fit:** Matching today's smile exactly
- **Trade-off:** Cannot optimize both simultaneously

### Model Comparison

| Model | Static Fit | Dynamic Consistency |
|-------|-----------|-------------------|
| Black-Scholes | Poor | Perfect (but trivial) |
| Local Vol | Perfect | Poor |
| Heston | Good | Moderate |
| SABR | Good | Moderate |
| Bergomi | Calibrated | Good |

### Practical Implications

1. **Use appropriate models for the product:**
   - Vanillas: Local vol is fine
   - Forward-start: Need dynamically consistent model

2. **Monitor recalibration P&L:**
   - Large recalibration P&L indicates inconsistency
   - Consider model change if persistent

3. **Forward smile diagnostics:**
   - Compare model-implied to market-implied
   - Adjust model or parameters if needed

### Key Takeaways

- Dynamic consistency is a stringent requirement
- Perfect static fit does not guarantee realistic dynamics
- Forward smiles are the key diagnostic tool
- Model choice depends on product being priced

---

## Further Reading


- Bergomi, L. *Stochastic Volatility Modeling*. Chapters on dynamic consistency.
- Gatheral, J. *The Volatility Surface*. Forward smile and model comparison.
- Rebonato, R. *Volatility and Correlation*. Practical implications.
- Piterbarg, V. *Smiling Hybrids*. Multi-factor models and consistency.
