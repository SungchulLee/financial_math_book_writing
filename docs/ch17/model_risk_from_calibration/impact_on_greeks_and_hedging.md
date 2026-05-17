# Impact on Greeks and Hedging

Calibration error affects not only prices but also **Greeks**, which are used for hedging. Unstable or mis-specified Greeks can lead to systematic hedging losses, even when the pricing error appears small.

---

## Greeks as model-dependent objects

### Definition

Greeks are partial derivatives of the option price with respect to market variables:

$$
\Delta = \frac{\partial P}{\partial S}, \quad \Gamma = \frac{\partial^2 P}{\partial S^2}, \quad \text{Vega} = \frac{\partial P}{\partial \sigma}, \quad \Theta = \frac{\partial P}{\partial t}, \quad \text{etc.}
$$

These derivatives are computed **under the calibrated model** with parameters $\hat{\theta}$:

$$
\Delta(\hat{\theta}) = \frac{\partial P}{\partial S}\bigg|_{\theta = \hat{\theta}}
$$

### The problem

If $\hat{\theta} \ne \theta^{\star}$, the computed Greeks are wrong:

$$
\Delta(\hat{\theta}) \ne \Delta(\theta^{\star})
$$

Hedging based on $\Delta(\hat{\theta})$ leaves residual exposure to the true $\Delta(\theta^{\star})$.

---

## Sensitivity of Greeks to parameters

### First-order analysis

Expand Greeks around the true parameter:

$$
\Delta(\hat{\theta}) - \Delta(\theta^{\star}) \approx \nabla_\theta \Delta(\theta^{\star})^\top (\hat{\theta} - \theta^{\star})
$$

The term $\nabla_\theta \Delta$ is the **sensitivity of delta to parameters**, a second-order derivative of the price:

$$
\nabla_\theta \Delta = \nabla_\theta \left( \frac{\partial P}{\partial S} \right) = \frac{\partial^2 P}{\partial S \partial \theta}
$$

### Implication

Even small parameter errors can materially distort hedge ratios when $\nabla_\theta \Delta$ is large.

### Higher-order Greeks

For Gamma, Vega, etc., the analysis is similar:

$$
\Gamma(\hat{\theta}) - \Gamma(\theta^{\star}) \approx \nabla_\theta \Gamma^\top \Delta\theta
$$

Higher-order Greeks (Gamma, Vanna, Volga) are often more sensitive to parameters than Delta itself.

---

## Hedging breakdown mechanisms

### 1. Systematic hedge ratio errors

If $\Delta(\hat{\theta})$ consistently over- or under-estimates true delta:

- Portfolio accumulates directional exposure.
- P&L variance increases.
- Hedging creates rather than removes risk.

### 2. Volatility of hedge ratios

Frequent recalibration with unstable parameters causes hedge ratios to jump:

- Transaction costs increase (constant rebalancing).
- Hedges chase noise rather than signal.
- Gamma/vega hedging becomes unreliable.

### 3. Cross-Greek contamination

In multi-factor models, Greeks are interconnected:

- Mis-estimated correlation $\rho$ affects both delta and vega.
- Vol-of-vol errors distort gamma and vanna simultaneously.
- Hedging one risk may inadvertently increase another.

### 4. Model-specific Greeks

Some Greeks exist only in certain models:

- **Vanna** (cross-derivative $\partial^2 P / \partial S \partial \sigma$) depends on how spot and vol interact.
- **Volga** ($\partial^2 P / \partial \sigma^2$) depends on vol-of-vol structure.

If the model is mis-specified, these Greeks may be meaningless or misleading.

---

## Quantifying Greek sensitivity

### Parameter-delta covariance

The variance of delta due to parameter uncertainty:

$$
\text{Var}(\Delta) \approx \nabla_\theta \Delta^\top \Sigma_\theta \nabla_\theta \Delta
$$

This gives a confidence interval for the hedge ratio:

$$
\Delta \in \left[ \hat{\Delta} - z_\alpha \sigma_\Delta, \; \hat{\Delta} + z_\alpha \sigma_\Delta \right]
$$

Recall (see [bump-and-reprice and Monte Carlo propagation for prices](sensitivity_of_prices_to_calibration_error.md#practical-measurement)) — the same procedures apply to Greeks by replacing $P$ with $\Delta$, $\Gamma$, etc.

---

## Hedging error analysis

### Single-period hedging error

Consider delta-hedging a call option over $[t, t + \Delta t]$. The hedging error is:

$$
\epsilon = \Delta C - \Delta(\hat{\theta}) \cdot \Delta S
$$

where $\Delta C$ is the actual change in option value.

Under the true model:

$$
\epsilon = \frac{1}{2} \Gamma(\theta^{\star}) (\Delta S)^2 + \text{higher-order terms}
$$

Under the calibrated model:

$$
\epsilon_{\text{model}} = \frac{1}{2} \Gamma(\hat{\theta}) (\Delta S)^2 + \cdots
$$

The discrepancy:

$$
\epsilon - \epsilon_{\text{model}} \approx \frac{1}{2} (\Gamma(\theta^{\star}) - \Gamma(\hat{\theta})) (\Delta S)^2
$$

### Cumulative effect

Over $N$ hedging periods:

$$
\text{Total error} \approx \sum_{i=1}^N \epsilon_i
$$

If errors are biased (systematic), they accumulate linearly. If unbiased but noisy, they accumulate as $\sqrt{N}$.

Calibration-induced errors are often **systematic** (same direction each day), leading to P&L drift.

---

## Example: Heston delta sensitivity

### Setup

In Heston, delta depends on all parameters:

$$
\Delta = \Delta(S, v_0, \kappa, \bar{v}, \sigma_v, \rho, K, T)
$$

### Sensitivity to correlation

The correlation $\rho$ affects skew. For OTM puts:

- More negative $\rho$ → steeper skew → higher put delta (in absolute value).

If $\rho$ is mis-estimated by $-0.1$ (true $\rho = -0.8$, calibrated $\rho = -0.7$):

- Put delta is underestimated.
- Hedging leaves residual downside exposure.
- In a selloff, hedged position loses money.

### Numerical example

Consider a 3-month 95% strike put on SPX with:

- True parameters: $\rho = -0.8$, giving $\Delta_{\text{true}} = -0.35$.
- Calibrated: $\rho = -0.7$, giving $\Delta_{\text{calib}} = -0.30$.

The hedge is $5\%$ short of the correct delta. For a \$100M notional position:

- Under-hedge: \$5M delta exposure.
- In a $5\%$ SPX move: unexpected P&L of ~\$250K.

---

## Robust hedging practices

### 1. Hedge with Greek ranges

Rather than using point estimates, compute:

$$
\Delta_{\min} = \inf_{\theta \in C_\alpha} \Delta(\theta), \qquad \Delta_{\max} = \sup_{\theta \in C_\alpha} \Delta(\theta)
$$

where $C_\alpha$ is a confidence region for parameters.

Hedge to the midpoint but reserve for the range.

### 2. Model-invariant hedging

Some hedges depend less on model details:

- **Delta-neutralization:** Hedge delta using the underlying (less model-dependent than vega hedging).
- **Static hedging with vanillas:** Replicate exotic payoffs using traded options (model-free if exact).
- **Variance swaps for vega:** Direct exposure to realized variance (model-independent).

### 3. Stress testing under alternative calibrations

- Recalibrate with different objectives, weights, or data subsets.
- Compute Greeks under each calibration.
- Evaluate worst-case hedging error.

### 4. Simpler proxy models for risk

Use robust, simple models for risk management even if pricing uses complex models:

- Black–Scholes Greeks for delta/gamma limits.
- SABR or sticky-strike rules for vega.
- Reserve for model differences.

### 5. Regularization for stable Greeks

Recall (see [robust objective functions](robust_calibration_criteria.md#robust-objective-functions)) — regularization toward a prior or yesterday's parameters that stabilizes $\hat\theta$ likewise stabilizes Greeks, since smaller parameter jumps imply smaller Greek jumps.

---

## Greeks and recalibration

### The recalibration-Greek feedback loop

1. Market moves → recalibrate → parameters change.
2. Greeks change → hedge ratios change.
3. Rebalance hedges → transaction costs.
4. Repeat daily.

If parameters are unstable, this loop amplifies costs and risks.

### Breaking the loop

- Recalibrate less frequently (weekly, monthly).
- Use filtering for smooth parameter evolution.
- Hedge to lagged Greeks (reduces turnover).
- Accept wider hedge bands (tolerate small mismatches).

---

## Regulatory and governance considerations

### Model risk management (SR 11-7)

Regulators expect:

- Sensitivity analysis of models to parameter changes.
- Documentation of parameter uncertainty and its impact on hedging.
- Limits on positions with high model sensitivity.
- Reserves for hedging error from model risk.

### Best practices

- Compute and report Greek sensitivity to parameters.
- Include parameter uncertainty in risk reports.
- Stress test hedging strategies under parameter scenarios.
- Review calibration stability as part of model validation.

---

## Key takeaways

- Greeks are highly sensitive to calibration quality.
- Hedging based on unstable parameters is fragile and costly.
- Greek uncertainty should be quantified and hedged conservatively.
- Robust hedging prioritizes model-invariant strategies.
- Regularization and filtering improve Greek stability.
- Greek sensitivity is a key component of model risk.

---

## Further reading

- Taleb, *Dynamic Hedging* (practical hedging and model risk).
- Cont & Tankov, *Financial Modelling with Jump Processes* (Greeks in jump-diffusion models).
- Rebonato, *Volatility and Correlation* (model risk in hedging).
- Gatheral, *The Volatility Surface* (Greeks under stochastic volatility).
- Glasserman, *Monte Carlo Methods in Financial Engineering* (Greek estimation).

---

## Exercises

**Exercise 1.** Starting from $\Delta(\hat{\theta}) - \Delta(\theta^\star) \approx \nabla_\theta \Delta^\top (\hat{\theta} - \theta^\star)$, derive the variance of the hedge ratio due to parameter uncertainty:

$$
\text{Var}(\Delta) = \nabla_\theta \Delta^\top \Sigma_\theta \nabla_\theta \Delta
$$

For a Heston model with $\Sigma_\theta = \text{diag}(0.002^2, 0.3^2, 0.005^2, 0.05^2, 0.05^2)$ and $\nabla_\theta \Delta = (15, 0.005, 2, 0.3, 0.8)$, compute $\sigma_\Delta$ and interpret the result for a \$100M notional position.

??? success "Solution to Exercise 1"
    We start from the first-order approximation of the hedge ratio error:

    $$
    \Delta(\hat{\theta}) - \Delta(\theta^\star) \approx \nabla_\theta \Delta(\theta^\star)^\top (\hat{\theta} - \theta^\star)
    $$

    The parameter estimation error $\hat{\theta} - \theta^\star$ is a random vector with covariance $\Sigma_\theta$. Taking the variance of both sides:

    $$
    \text{Var}(\Delta(\hat{\theta})) \approx \text{Var}\!\left(\nabla_\theta \Delta^\top (\hat{\theta} - \theta^\star)\right)
    $$

    Since $\nabla_\theta \Delta$ is treated as a constant (evaluated at $\theta^\star$), and using the identity $\text{Var}(a^\top X) = a^\top \text{Cov}(X) \, a$ for any constant vector $a$:

    $$
    \text{Var}(\Delta) = \nabla_\theta \Delta^\top \Sigma_\theta \nabla_\theta \Delta
    $$

    This is a scalar quadratic form. Now substitute the given values. With $\Sigma_\theta = \text{diag}(0.002^2, 0.3^2, 0.005^2, 0.05^2, 0.05^2)$ and $\nabla_\theta \Delta = (15, 0.005, 2, 0.3, 0.8)$:

    $$
    \text{Var}(\Delta) = (15)^2(0.002)^2 + (0.005)^2(0.3)^2 + (2)^2(0.005)^2 + (0.3)^2(0.05)^2 + (0.8)^2(0.05)^2
    $$

    Computing each term:

    - $v_0$: $(15)^2(0.002)^2 = 225 \times 4 \times 10^{-6} = 9.00 \times 10^{-4}$
    - $\kappa$: $(0.005)^2(0.3)^2 = 2.5 \times 10^{-5} \times 0.09 = 2.25 \times 10^{-6}$
    - $\bar{v}$: $(2)^2(0.005)^2 = 4 \times 2.5 \times 10^{-5} = 1.00 \times 10^{-4}$
    - $\sigma_v$: $(0.3)^2(0.05)^2 = 0.09 \times 2.5 \times 10^{-3} = 2.25 \times 10^{-4}$
    - $\rho$: $(0.8)^2(0.05)^2 = 0.64 \times 2.5 \times 10^{-3} = 1.60 \times 10^{-3}$

    Summing: $\text{Var}(\Delta) \approx 9.00 \times 10^{-4} + 2.25 \times 10^{-6} + 1.00 \times 10^{-4} + 2.25 \times 10^{-4} + 1.60 \times 10^{-3} = 2.827 \times 10^{-3}$

    Therefore:

    $$
    \sigma_\Delta = \sqrt{2.827 \times 10^{-3}} \approx 0.053
    $$

    **Interpretation:** The dominant contributions come from $\rho$ (57%) and $v_0$ (32%). For a \$100M notional position, the delta uncertainty of $\pm 0.053$ translates to a notional exposure uncertainty of $0.053 \times \$100\text{M} = \$5.3\text{M}$. At the 95% confidence level ($z_{0.025} = 1.96$), the hedge ratio lies in $[\hat{\Delta} - 0.104, \hat{\Delta} + 0.104]$, meaning the unhedged exposure could be as large as \$10.4M. This is substantial and warrants robust hedging practices.

---

**Exercise 2.** A delta-hedged portfolio has hedging error $\epsilon \approx \frac{1}{2}(\Gamma(\theta^\star) - \Gamma(\hat{\theta}))(\Delta S)^2$ per period. Over 252 trading days, if the gamma error is systematic (same sign each day) with magnitude 0.001 and daily spot moves have standard deviation $\sigma_S = 1.5\%$, estimate the cumulative P&L impact. Compare this to the case where gamma errors are random with mean zero.

??? success "Solution to Exercise 2"
    The per-period hedging error from gamma mis-estimation is:

    $$
    \epsilon_i = \frac{1}{2}(\Gamma(\theta^\star) - \Gamma(\hat{\theta}))(\Delta S_i)^2
    $$

    Given: gamma error magnitude $|\Gamma(\theta^\star) - \Gamma(\hat{\theta})| = 0.001$, daily spot move standard deviation $\sigma_S = 1.5\% = 0.015$, and 252 trading days.

    The expected squared daily move is $\mathbb{E}[(\Delta S_i)^2] = \sigma_S^2 = (0.015)^2 = 2.25 \times 10^{-4}$.

    **Case 1: Systematic gamma error (same sign each day).**

    Each day's expected error is:

    $$
    \mathbb{E}[\epsilon_i] = \frac{1}{2} \times 0.001 \times 2.25 \times 10^{-4} = 1.125 \times 10^{-7}
    $$

    Over 252 days, the errors accumulate linearly since they are all the same sign:

    $$
    \text{Total error} = 252 \times 1.125 \times 10^{-7} = 2.835 \times 10^{-5}
    $$

    Per unit of spot, this is $2.835 \times 10^{-5}$. For a \$100M notional, the cumulative P&L impact is approximately $2.835 \times 10^{-5} \times \$100\text{M} = \$2{,}835$. While this seems small per unit, note that this scales with the square of notional and the true gamma error may be much larger for exotic products.

    More importantly, the error is **deterministic in sign**: it does not diversify over time. The total grows as $N$, not $\sqrt{N}$.

    **Case 2: Random gamma error (mean zero, same magnitude).**

    If the gamma error changes sign randomly each day with mean zero, then $\epsilon_i$ are independent mean-zero random variables. The expected total error is zero:

    $$
    \mathbb{E}\!\left[\sum_{i=1}^{252} \epsilon_i\right] = 0
    $$

    The standard deviation of the cumulative error is:

    $$
    \sigma_{\text{total}} = \sqrt{252} \times \frac{1}{2} \times 0.001 \times \sigma_S^2 = \sqrt{252} \times 1.125 \times 10^{-7} \approx 1.786 \times 10^{-6}
    $$

    This is about $16\times$ smaller than the systematic case. The key difference is that systematic errors accumulate linearly ($\propto N$), while random errors accumulate as $\sqrt{N}$. Calibration-induced gamma errors are typically systematic because the same biased parameters are used each day, making the systematic case the relevant one in practice.

---

**Exercise 3.** In the numerical example, mis-estimating $\rho$ by $0.1$ changed the delta of a 95%-strike put from $-0.35$ to $-0.30$. Compute the parameter sensitivity $\partial\Delta/\partial\rho$ from these values. If $\rho$ uncertainty is $\sigma_\rho = 0.05$, what is the 95% confidence interval for the hedge ratio?

??? success "Solution to Exercise 3"
    From the numerical example:

    - True: $\rho = -0.8$, $\Delta_{\text{true}} = -0.35$
    - Calibrated: $\rho = -0.7$, $\Delta_{\text{calib}} = -0.30$

    The finite-difference estimate of the parameter sensitivity is:

    $$
    \frac{\partial \Delta}{\partial \rho} \approx \frac{\Delta(\rho = -0.7) - \Delta(\rho = -0.8)}{-0.7 - (-0.8)} = \frac{-0.30 - (-0.35)}{0.1} = \frac{0.05}{0.1} = 0.5
    $$

    This means a unit increase in $\rho$ increases delta by $0.5$ (makes puts less negative in delta, consistent with less skew).

    Given $\sigma_\rho = 0.05$, the standard deviation of delta due to $\rho$-uncertainty alone is:

    $$
    \sigma_\Delta = \left|\frac{\partial \Delta}{\partial \rho}\right| \sigma_\rho = 0.5 \times 0.05 = 0.025
    $$

    The 95% confidence interval for the hedge ratio is:

    $$
    \Delta \in \left[\hat{\Delta} - 1.96 \sigma_\Delta, \; \hat{\Delta} + 1.96 \sigma_\Delta\right] = \left[-0.35 - 0.049, \; -0.35 + 0.049\right] = [-0.399, -0.301]
    $$

    This is a wide range: the true delta could be anywhere from $-0.40$ to $-0.30$ at the 95% level. For hedging purposes, this means the residual delta after hedging at $\hat{\Delta} = -0.35$ could be as large as $\pm 0.049$ in absolute value, which for a \$100M notional gives \$4.9M of unhedged delta exposure. The fact that a single parameter ($\rho$) generates such a wide confidence band underscores the importance of accurate skew calibration for OTM puts.

---

**Exercise 4.** Explain the concept of "cross-Greek contamination." Consider a vanna-hedged position where the hedge ratio is $\partial^2 P / \partial S \partial \sigma$. If both $\rho$ and $\sigma_v$ are mis-estimated, show how the vanna error depends on both parameter errors simultaneously. Why might this compound effect be larger than the sum of individual parameter impacts?

??? success "Solution to Exercise 4"
    **Cross-Greek contamination** refers to the phenomenon where mis-estimation of model parameters simultaneously distorts multiple Greeks, and these distortions interact in ways that compound hedging errors.

    Consider the vanna of an option, defined as:

    $$
    \text{Vanna} = \frac{\partial^2 P}{\partial S \partial \sigma}
    $$

    In a stochastic volatility model like Heston, vanna depends on the full parameter vector $\theta = (\rho, \sigma_v, \kappa, \bar{v}, v_0)$. Expanding vanna around the true parameters:

    $$
    \text{Vanna}(\hat{\theta}) - \text{Vanna}(\theta^\star) \approx \frac{\partial \text{Vanna}}{\partial \rho} \Delta\rho + \frac{\partial \text{Vanna}}{\partial \sigma_v} \Delta\sigma_v + \text{cross terms}
    $$

    When both $\rho$ and $\sigma_v$ are mis-estimated, the vanna error has a second-order cross term from the Taylor expansion:

    $$
    \text{Vanna error} \approx \frac{\partial \text{Vanna}}{\partial \rho}\Delta\rho + \frac{\partial \text{Vanna}}{\partial \sigma_v}\Delta\sigma_v + \frac{\partial^2 \text{Vanna}}{\partial \rho \, \partial \sigma_v}\Delta\rho \, \Delta\sigma_v + \cdots
    $$

    The cross-derivative term $\frac{\partial^2 \text{Vanna}}{\partial \rho \, \partial \sigma_v}\Delta\rho \, \Delta\sigma_v$ represents the **interaction effect**. This compound effect can be larger than the sum of individual parameter impacts for several reasons:

    1. **Correlated estimation errors:** In calibration, $\rho$ and $\sigma_v$ are often negatively correlated (both affect skew). If $\Delta\rho$ and $\Delta\sigma_v$ tend to have opposite signs, and if the cross-derivative has the appropriate sign, the interaction term reinforces the individual errors rather than canceling them.

    2. **Nonlinear parameter interactions:** In Heston, the correlation $\rho$ determines how spot and volatility co-move, while $\sigma_v$ determines the magnitude of volatility fluctuations. Vanna captures the sensitivity of delta to volatility, which depends on the *product* of these effects: how much vol moves ($\sigma_v$) and how that movement correlates with spot ($\rho$). Mis-estimating both simultaneously distorts this entire mechanism.

    3. **Higher-order Greeks are more sensitive:** Vanna is already a second-order derivative of price. Its sensitivity to parameters (a third-order derivative of price) tends to be larger in relative terms than the sensitivity of delta or vega, amplifying any parameter error.

    In practice, cross-Greek contamination means that hedging vanna risk while having incorrect $\rho$ and $\sigma_v$ can actually increase portfolio risk rather than reduce it, because the vanna hedge itself is mis-sized.

---

**Exercise 5.** A risk manager proposes hedging with Greek ranges: $\Delta \in [\Delta_{\min}, \Delta_{\max}]$ computed over a 95% confidence region for parameters. For a position where $\Delta_{\min} = -0.38$ and $\Delta_{\max} = -0.28$, the desk hedges at the midpoint $-0.33$. Compute the maximum residual delta exposure for a \$50M notional. Discuss when hedging at the midpoint is optimal versus hedging more conservatively.

??? success "Solution to Exercise 5"
    Given: $\Delta_{\min} = -0.38$, $\Delta_{\max} = -0.28$, midpoint hedge $\hat{\Delta} = -0.33$, notional = \$50M.

    The maximum residual delta exposure occurs at the extremes of the confidence region:

    $$
    \text{Max residual} = \max(|\Delta_{\max} - \hat{\Delta}|, |\Delta_{\min} - \hat{\Delta}|) = \max(|-0.28 + 0.33|, |-0.38 + 0.33|) = \max(0.05, 0.05) = 0.05
    $$

    Since the midpoint is exactly centered, both extremes give equal residual. For \$50M notional:

    $$
    \text{Max residual exposure} = 0.05 \times \$50\text{M} = \$2.5\text{M}
    $$

    **When is midpoint hedging optimal?**

    Midpoint hedging minimizes the *maximum possible residual* (minimax criterion), which is optimal when:

    - The loss function is symmetric in delta error (equal cost of being over-hedged vs. under-hedged).
    - The parameter distribution is symmetric within the confidence region.
    - Transaction costs of rebalancing are low relative to the risk.

    **When should one hedge more conservatively?**

    - **Asymmetric loss:** If the cost of being under-hedged (e.g., short gamma in a crash) exceeds the cost of being over-hedged, one should hedge closer to $\Delta_{\min} = -0.38$ (more protection). This is common for risk-averse institutions and when the portfolio has short convexity.

    - **Skewed parameter distribution:** If the parameter posterior is skewed (e.g., $\rho$ more likely to be more negative), the expected delta is not the midpoint of the range, and one should hedge at the expected value.

    - **Regulatory constraints:** Risk limits may require hedging to a worst-case scenario rather than the midpoint.

    - **Cost of carry:** If holding excess hedge is cheap (e.g., delta hedging with futures has low cost), hedging conservatively (closer to the worst case) is preferred. If hedging is expensive (exotic hedging instruments), minimizing hedge notional via the midpoint is preferable.

    A common practical compromise is to hedge at the midpoint but hold a capital reserve equal to the worst-case residual exposure (\$2.5M in this case).

---

**Exercise 6.** Compare the following robust hedging strategies for a book of barrier options: (a) delta-hedging with the calibrated model, (b) static hedging using vanilla options, and (c) delta-hedging but using an average delta across three different models (Heston, SABR, local vol). For each strategy, discuss model dependence, transaction costs, and residual risk.

??? success "Solution to Exercise 6"
    **(a) Delta-hedging with the calibrated model.**

    - **Model dependence:** High. Barrier option deltas are extremely sensitive to the model choice and parameter calibration. The delta of a down-and-out call can vary by 50% or more across models, especially when the spot is near the barrier.
    - **Transaction costs:** Moderate to high. Delta changes rapidly near the barrier (gamma explosion), requiring frequent rebalancing. Parameter recalibration adds further turnover.
    - **Residual risk:** Large. Model mis-specification leads to systematic hedging errors. The delta hedge is only as good as the model, and barrier options are precisely the products where models disagree most.

    **(b) Static hedging using vanilla options.**

    - **Model dependence:** Low to moderate. A static replication of a barrier option using a portfolio of vanilla calls and puts (following the Carr-Chou approach or put-call symmetry methods) can be nearly model-free if the barrier is continuously monitored and the replication is exact. In practice, discrete monitoring and finite strike availability introduce model dependence in the residual.
    - **Transaction costs:** Low ongoing costs. The vanilla portfolio is established once and does not require frequent rebalancing. The initial cost may be higher (bid-ask on multiple vanillas), but there is no gamma-driven turnover.
    - **Residual risk:** Moderate. Residual arises from discrete monitoring adjustments, gap risk (spot jumping through the barrier), and the approximation in the static hedge construction. However, this residual is typically smaller and more predictable than dynamic hedging errors.

    **(c) Delta-hedging with averaged delta across three models.**

    - **Model dependence:** Reduced but not eliminated. Averaging Heston, SABR, and local vol deltas diversifies model-specific biases. If models err in different directions, the average is more robust. However, if all models share a common structural deficiency (e.g., all are continuous diffusions and miss jumps), averaging does not help.
    - **Transaction costs:** Similar to (a), but potentially lower because the averaged delta is smoother (model-specific noise partially cancels), reducing turnover.
    - **Residual risk:** Lower than (a) because model-specific errors are diversified. The residual risk is dominated by the common component of model error (structural model risk) rather than parameter-specific risk.

    **Ranking:** For barrier options, (b) static hedging is generally preferred when feasible, as it minimizes model dependence and ongoing costs. Strategy (c) is a practical improvement over (a) when static hedging is not available (e.g., complex exotic structures). Strategy (a) is the least robust but simplest to implement.

---

**Exercise 7.** The recalibration-Greek feedback loop generates transaction costs proportional to $|\Delta_t(\hat{\theta}_t) - \Delta_{t-1}(\hat{\theta}_{t-1})|$. Using the decomposition $\Delta\Delta_t = (\partial\Delta/\partial S)\Delta S + (\partial\Delta/\partial\sigma)\Delta\sigma + \nabla_\theta\Delta^\top\Delta\hat{\theta}$, identify which term represents unnecessary turnover due to calibration noise. Propose a quantitative criterion for deciding when to skip rebalancing (i.e., when the calibration-induced component dominates the market-driven components).

??? success "Solution to Exercise 7"
    The total change in delta between rebalancing dates decomposes as:

    $$
    \Delta\Delta_t = \underbrace{\frac{\partial \Delta}{\partial S}\Delta S}_{\text{gamma term}} + \underbrace{\frac{\partial \Delta}{\partial \sigma}\Delta\sigma}_{\text{vanna term}} + \underbrace{\nabla_\theta \Delta^\top \Delta\hat{\theta}}_{\text{calibration term}}
    $$

    **Identifying the unnecessary turnover:**

    The first two terms ($\Gamma \cdot \Delta S$ and vanna $\cdot \Delta\sigma$) represent **market-driven** changes in delta. These reflect genuine changes in the option's risk profile due to actual market movements and are necessary for maintaining the hedge.

    The third term $\nabla_\theta \Delta^\top \Delta\hat{\theta}$ represents **calibration-driven** changes: the delta changes because the parameters changed upon recalibration, not because the market moved in a way that requires rehedging. If the parameter changes are due to calibration noise (optimizer randomness, small data perturbations, local minima), this term represents **unnecessary turnover**.

    **Quantitative criterion for skipping rebalancing:**

    Define the calibration-induced component as:

    $$
    R_{\text{calib}} = |\nabla_\theta \Delta^\top \Delta\hat{\theta}|
    $$

    and the market-driven component as:

    $$
    R_{\text{market}} = \left|\frac{\partial \Delta}{\partial S}\Delta S + \frac{\partial \Delta}{\partial \sigma}\Delta\sigma\right|
    $$

    **Proposed criterion:** Skip rebalancing when the calibration component dominates:

    $$
    \frac{R_{\text{calib}}}{R_{\text{calib}} + R_{\text{market}}} > \alpha
    $$

    for a threshold $\alpha \in (0.5, 0.8)$. Equivalently, rebalance only when:

    $$
    R_{\text{market}} > \frac{1 - \alpha}{\alpha} R_{\text{calib}}
    $$

    A practical alternative is to impose a significance test. Estimate the standard deviation of calibration noise from historical perturbation analysis: $\sigma_{\text{calib}} = \sqrt{\nabla_\theta \Delta^\top \Sigma_{\hat{\theta}} \nabla_\theta \Delta}$, where $\Sigma_{\hat{\theta}}$ is the covariance of parameter estimates across perturbations. Then skip rebalancing when:

    $$
    |\Delta\Delta_t| < k \cdot \sigma_{\text{calib}}
    $$

    for some multiplier $k$ (e.g., $k = 2$). This means: only rebalance when the total delta change is significantly larger than what calibration noise alone could explain.

    **Implementation notes:**

    - The threshold $\alpha$ or multiplier $k$ should be calibrated to balance transaction cost savings against hedging slippage.
    - One can also implement a **Kalman filter** for parameters, which naturally separates signal from noise in parameter evolution, providing filtered estimates of $\Delta\hat{\theta}$ that exclude the noise component.
    - An alternative is to hedge using yesterday's parameters (skip recalibration entirely) and only update parameters weekly or when the market-driven delta change exceeds a threshold.
