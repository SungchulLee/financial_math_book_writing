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

**Evolution:** Recall (see [§ Local Volatility Dynamics](../../ch13/index.md)). The forward smile **flattens** over time.

**Recalibration:** Tomorrow's market will likely show persistent skew, requiring a new local vol surface.

**Inconsistency:** The model predicts flat forward smiles, but recalibration shows persistent skew.

**Quantitative measure:**

$$
\text{Inconsistency} = \|\sigma_{\text{fwd}}^{\text{model}} - \sigma_{\text{IV}}^{\text{recalibrated}}\|
$$


For local vol, this can be several vol points for long-dated options.

### 3. Stochastic Volatility Models


**Status:** Better but still imperfect. Recall (see [§ Stochastic Volatility Dynamics](../../ch14/index.md)) for Heston and SABR specifics. Key dynamic-consistency facts:

- Heston: forward skew persists (via $\rho$), level evolves with $v_t$; wings and vol-of-vol may still drift on recalibration.
- SABR: with stochastic $\alpha_t$, ATM level evolves stochastically; consistency hinges on stability of $\rho$, $\nu$, $\beta$.

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


Recall (see [§ Model-Free Results](../model_free_results/breeden_litzenberger_formula.md)) for the forward variance swap strike formula. Dynamically consistent models should match these observables.

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

---

## Exercises

**Exercise 1.** Define dynamic consistency for a volatility model in your own words. Give a concrete example of how dynamic inconsistency would manifest: a model is calibrated today, evolved forward by one month, and the forward-implied surface differs systematically from the recalibrated surface.

??? success "Solution to Exercise 1"
    **Dynamic consistency** means that a volatility model, once calibrated at time $t = 0$ and evolved forward under its own dynamics to a future time $t$, produces a forward-implied volatility surface that agrees (in distribution) with the surface one would obtain by recalibrating the model to fresh market data at time $t$.

    **Concrete example:** Suppose a local volatility model is calibrated today to the SPX implied volatility surface. The model is then evolved forward by one month. Under local vol dynamics, the forward-implied smile for options expiring in, say, two months flattens significantly compared to today's smile. However, when the practitioner recalibrates to market data one month later, the market still exhibits a pronounced skew. The systematic discrepancy between the model-predicted flat forward smile and the recalibrated skewed smile is a manifestation of dynamic inconsistency. This gap means that any exotic option priced using the forward-implied smile from the original calibration will be mispriced.

---

**Exercise 2.** Explain why local volatility models are dynamically inconsistent. Specifically, if the model is calibrated today and the spot moves by 5%, describe how the model's predicted forward smile differs from what the market would actually show upon recalibration.

??? success "Solution to Exercise 2"
    Local volatility models are dynamically inconsistent because the local volatility function $\sigma_{\text{loc}}(S, t)$ is a deterministic function of spot and time. Once calibrated, the model's future smile is fully determined by the local vol surface, and it predicts that forward smiles **flatten** over time.

    **Mechanism when spot moves by 5%:** Suppose the spot drops by 5%. In the local vol framework, the model simply evaluates $\sigma_{\text{loc}}(S_{\text{new}}, t)$ at the new spot level. The smile predicted by the model at the new spot level is derived from the original local vol surface, which was designed to match today's smile. As a result:

    - The model predicts that ATM vol increases (because the local vol surface typically has higher values at lower spot levels, reflecting today's skew).
    - However, the model's predicted smile **shape** at the new spot level tends to be flatter than what the market actually exhibits.

    In practice, the market typically shows a persistent steep skew even after the spot move, while the local vol model's forward smile has lost much of its curvature. Upon recalibration, the new local vol surface differs substantially from the old one, confirming the dynamic inconsistency. The model systematically underpredicts the persistence of skew.

---

**Exercise 3.** The Heston stochastic volatility model has parameters $(\kappa, \theta, \xi, \rho, v_0)$. When recalibrating the Heston model daily, the parameter $v_0$ changes with market conditions but $\theta$ may drift as well. (a) Why does this represent dynamic inconsistency? (b) Which Heston parameters are most stable across recalibrations? (c) What modifications to the model could improve dynamic consistency?

??? success "Solution to Exercise 3"
    **(a) Why daily recalibration represents dynamic inconsistency:**

    If the Heston model were dynamically consistent, the only parameter that should change upon recalibration is $v_0$ (which tracks the current instantaneous variance). The long-run variance $\theta$, mean-reversion speed $\kappa$, vol-of-vol $\xi$, and correlation $\rho$ should remain stable because they describe structural features of the volatility dynamics. When $\theta$ drifts over successive recalibrations, it means the model's predicted evolution of the variance term structure does not match reality. The model evolves $v_t$ toward the calibrated $\theta$, but the market's actual long-run level shifts, forcing a recalibration that changes $\theta$.

    **(b) Most stable parameters across recalibrations:**

    Empirically, $\rho$ (spot-vol correlation) is the most stable Heston parameter, followed by $\xi$ (vol-of-vol). These parameters capture structural features of the joint spot-vol dynamics and the shape of the smile. The least stable parameters are $v_0$ (which must track current conditions) and $\theta$ (which drifts with market regimes). The mean-reversion speed $\kappa$ shows moderate stability.

    **(c) Modifications to improve dynamic consistency:**

    - **Time-dependent parameters:** Allow $\theta(t)$ and $\kappa(t)$ to be piecewise constant functions of time, calibrated to the term structure. This improves the static fit but sacrifices some predictive power for dynamics.
    - **Multi-factor extensions:** Add a second variance factor (double Heston) so that short-term and long-term variance dynamics decouple, reducing the need for $\theta$ to drift.
    - **Regime-switching:** Allow parameters to switch between distinct regimes, capturing structural shifts in volatility dynamics without continuous recalibration.

---

**Exercise 4.** Compare local volatility and stochastic volatility models in terms of dynamic consistency for: (a) ATM volatility dynamics, (b) skew dynamics, and (c) forward smile behavior. Summarize your comparison in a table.

??? success "Solution to Exercise 4"
    | Feature | Local Volatility | Stochastic Volatility |
    |---------|------------------|-----------------------|
    | **ATM vol dynamics** | ATM vol changes deterministically with spot via $\sigma_{\text{loc}}(S,t)$; response is immediate and fully determined by today's calibration | ATM vol evolves stochastically via the variance process $v_t$; response depends on realized vol path |
    | **Skew dynamics** | Forward skew flattens over time; model predicts skew will disappear for long forward-start periods | Forward skew persists due to non-zero $\rho$; skew decays slowly, controlled by vol-of-vol and correlation |
    | **Forward smile** | Flattens rapidly as the forward-start date increases; unrealistic for pricing cliquets and forward-start options | Maintains non-trivial shape; forward smile has persistent curvature and skew, closer to market behavior |

    **Summary:** Local vol wins on static fit (exact calibration to today's smile) but fails on dynamics. Stochastic vol provides more realistic dynamics, especially for forward-looking products, at the cost of a potentially imperfect static fit.

---

**Exercise 5.** A cliquet option depends critically on the forward smile because its payoffs are determined by periodic returns. Explain why pricing a cliquet with a dynamically inconsistent model can lead to systematic errors. Would the model overprice or underprice if the forward smile flattens faster than the market expects?

??? success "Solution to Exercise 5"
    A cliquet option's payoff depends on periodic returns $R_i = S_{t_i}/S_{t_{i-1}} - 1$ over each reset period $[t_{i-1}, t_i]$. Each period's contribution is effectively a forward-start option, and its price depends on the **forward smile** for that period. The forward smile determines the risk-neutral distribution of $S_{t_i}/S_{t_{i-1}}$, which controls the probability of triggering caps and floors on each periodic return.

    **Why dynamic inconsistency causes systematic errors:** A dynamically inconsistent model predicts the wrong forward smile for future periods. If the model's forward smile is too flat (as with local vol), it underestimates the probability of large periodic returns (both positive and negative). This directly affects:

    - The probability of hitting the cap (underestimated if skew is too flat)
    - The probability of hitting the floor (underestimated if tails are too thin)
    - The correlation structure between successive returns

    **Overpricing or underpricing:** If the forward smile flattens faster than the market expects, the model **underprices** the cliquet. The reasoning is that a flat forward smile implies thinner tails and lower variance for periodic returns, which reduces the expected value of the capped/floored return payoffs. In particular, the reduced skew undervalues the downside protection embedded in the floor feature. A stochastic volatility model with persistent forward skew would produce a higher cliquet price because it assigns more probability mass to extreme periodic returns.

---

**Exercise 6.** Bergomi's variance curve model specifies dynamics for the forward variance curve $\xi_t^T = \mathbb{E}_t[\sigma_T^2]$. Explain why directly modeling the forward variance curve leads to better dynamic consistency than calibrating a parametric model. What tradeoff does this approach introduce?

??? success "Solution to Exercise 6"
    Bergomi's variance curve model specifies the dynamics of the forward variance curve $\xi_t^T = \mathbb{E}_t[\sigma_T^2]$ directly:

    $$
    d\xi_t^T = \xi_t^T \omega(T-t) \, dZ_t
    $$

    **Why this leads to better dynamic consistency:** In parametric models (Heston, SABR), the forward variance curve is an output derived from the model parameters. The model's dynamics determine how the curve evolves, and if the dynamics are not rich enough, the evolved curve will not match market observations. By contrast, Bergomi's approach models the entire forward variance curve as the primary object. This means:

    - The initial forward variance curve is directly calibrated to the market term structure.
    - The evolution of the curve is specified by the volatility function $\omega(T-t)$, which controls how shocks propagate across maturities.
    - There is no mismatch between the model's predicted evolution and the shape of the curve, because the curve itself is the state variable.

    **Tradeoff:** The main cost is **complexity and tractability**. The variance curve model is infinite-dimensional (it tracks a function, not a finite set of parameters), making calibration and simulation more demanding. Additionally, ensuring no-arbitrage constraints (e.g., forward variances remain positive) requires careful specification of $\omega$. The model also introduces the question of how to parameterize $\omega(T-t)$ itself, trading one calibration problem for another, albeit one with more direct control over dynamics.

---

**Exercise 7.** A practitioner recalibrates a local volatility model to the SPX surface every day and uses it to price barrier options. Over one month, the model's delta hedge underperforms consistently. Diagnose this as a dynamic consistency problem and propose two potential solutions: one using a different model class, and one using the same local volatility framework with adjustments.

??? success "Solution to Exercise 7"
    **Diagnosis:** The consistent underperformance of the delta hedge is a classic symptom of dynamic inconsistency in local volatility models. The local vol model is recalibrated daily, and each recalibration changes the local volatility surface $\sigma_{\text{loc}}(S, t)$. The barrier option's delta depends on the model's prediction of how the smile will evolve as the spot approaches the barrier. Because local vol predicts forward smile flattening while the market maintains persistent skew, the model's deltas are systematically biased:

    - Near the barrier, the model underestimates the probability of barrier breaching (wrong tail behavior)
    - The delta hedge ratio is computed under incorrect forward smile assumptions
    - Daily recalibration introduces parameter instability, generating spurious P&L

    **Solution 1 (Different model class):** Switch to a stochastic volatility model such as Heston or a stochastic local volatility (SLV) model. The SLV model combines a stochastic volatility component for realistic dynamics with a local volatility component (the "leverage function") for exact calibration:

    $$
    dS_t = (r-q) S_t \, dt + L(S_t, t) \sqrt{v_t} \, S_t \, dW_t^S
    $$

    This provides both exact smile fit and more realistic forward smile dynamics, reducing the hedging error from dynamic inconsistency.

    **Solution 2 (Within local vol framework):** Apply a "mixing" or "transition" adjustment to the local vol model. Specifically:

    - Use a **weighted average** of the local vol delta and the sticky-delta (or sticky-strike) delta, with weights chosen to match the empirical skew stickiness ratio (SSR $\approx 0.5$).
    - Alternatively, apply a **minimum variance hedge** that adjusts the model delta by the empirical spot-vol beta, effectively correcting for the model's incorrect smile dynamics without changing the pricing model itself. This approach accepts that the model is dynamically inconsistent but corrects the hedge ratios using empirical information.
