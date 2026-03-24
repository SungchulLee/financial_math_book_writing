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

### Bump-and-reprice for Greeks

1. Compute $\Delta(\hat{\theta})$.
2. Perturb each parameter: $\theta_i \to \theta_i + \delta_i$.
3. Recompute $\Delta(\hat{\theta} + \delta e_i)$.
4. Estimate $\partial \Delta / \partial \theta_i$.
5. Combine with parameter uncertainty.

### Monte Carlo Greek uncertainty

1. Sample $\theta^{(j)} \sim p(\theta | \text{data})$.
2. Compute $\Delta^{(j)} = \Delta(\theta^{(j)})$ for each sample.
3. Examine distribution of $\{\Delta^{(j)}\}$.

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

Regularization that stabilizes parameters also stabilizes Greeks:

$$
\min_\theta \mathcal{L}(\theta) + \lambda \|\theta - \theta_{\text{prior}}\|^2
$$

Smaller parameter jumps → smaller Greek jumps.

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

---

**Exercise 2.** A delta-hedged portfolio has hedging error $\epsilon \approx \frac{1}{2}(\Gamma(\theta^\star) - \Gamma(\hat{\theta}))(\Delta S)^2$ per period. Over 252 trading days, if the gamma error is systematic (same sign each day) with magnitude 0.001 and daily spot moves have standard deviation $\sigma_S = 1.5\%$, estimate the cumulative P&L impact. Compare this to the case where gamma errors are random with mean zero.

---

**Exercise 3.** In the numerical example, mis-estimating $\rho$ by $0.1$ changed the delta of a 95%-strike put from $-0.35$ to $-0.30$. Compute the parameter sensitivity $\partial\Delta/\partial\rho$ from these values. If $\rho$ uncertainty is $\sigma_\rho = 0.05$, what is the 95% confidence interval for the hedge ratio?

---

**Exercise 4.** Explain the concept of "cross-Greek contamination." Consider a vanna-hedged position where the hedge ratio is $\partial^2 P / \partial S \partial \sigma$. If both $\rho$ and $\sigma_v$ are mis-estimated, show how the vanna error depends on both parameter errors simultaneously. Why might this compound effect be larger than the sum of individual parameter impacts?

---

**Exercise 5.** A risk manager proposes hedging with Greek ranges: $\Delta \in [\Delta_{\min}, \Delta_{\max}]$ computed over a 95% confidence region for parameters. For a position where $\Delta_{\min} = -0.38$ and $\Delta_{\max} = -0.28$, the desk hedges at the midpoint $-0.33$. Compute the maximum residual delta exposure for a \$50M notional. Discuss when hedging at the midpoint is optimal versus hedging more conservatively.

---

**Exercise 6.** Compare the following robust hedging strategies for a book of barrier options: (a) delta-hedging with the calibrated model, (b) static hedging using vanilla options, and (c) delta-hedging but using an average delta across three different models (Heston, SABR, local vol). For each strategy, discuss model dependence, transaction costs, and residual risk.

---

**Exercise 7.** The recalibration-Greek feedback loop generates transaction costs proportional to $|\Delta_t(\hat{\theta}_t) - \Delta_{t-1}(\hat{\theta}_{t-1})|$. Using the decomposition $\Delta\Delta_t = (\partial\Delta/\partial S)\Delta S + (\partial\Delta/\partial\sigma)\Delta\sigma + \nabla_\theta\Delta^\top\Delta\hat{\theta}$, identify which term represents unnecessary turnover due to calibration noise. Propose a quantitative criterion for deciding when to skip rebalancing (i.e., when the calibration-induced component dominates the market-driven components).
