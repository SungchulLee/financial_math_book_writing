# Sensitivity of Prices to Calibration Error

Calibration error translates directly into **model risk**: even small mis-estimation of parameters can lead to non-negligible pricing errors, especially for nonlinear or path-dependent payoffs. This section develops the framework for quantifying this sensitivity.

---

## From parameter error to price error

### First-order approximation

Let $\hat{\theta}$ be the calibrated parameter vector and $\theta^{\star}$ the (unknown) true parameter. For a derivative price $P(\theta)$, a Taylor expansion gives:

$$
P(\theta^{\star}) - P(\hat{\theta}) \approx \nabla_\theta P(\hat{\theta})^\top (\theta^{\star} - \hat{\theta}).
$$

Rearranging:

$$
\Delta P := P(\hat{\theta}) - P(\theta^{\star}) \approx -\nabla_\theta P(\hat{\theta})^\top \Delta\theta,
$$

where $\Delta\theta = \hat{\theta} - \theta^{\star}$ is the parameter estimation error.

### Key insight

Price sensitivity depends on two factors:

1. **Parameter uncertainty:** The magnitude and direction of $\Delta\theta$.
2. **Price gradient:** The sensitivity $\nabla_\theta P$ of the derivative to parameters.

Products with large $\|\nabla_\theta P\|$ are more exposed to calibration error.

---

## Second-order effects

For derivatives with significant curvature in parameter space, first-order approximation may understate risk.

### Taylor expansion to second order

$$
\Delta P \approx \nabla_\theta P^\top \Delta\theta + \frac{1}{2} \Delta\theta^\top H_P \Delta\theta,
$$

where $H_P = \nabla_\theta^2 P$ is the Hessian of the price with respect to parameters.

### When second-order matters

- **Exotic options:** Barrier options, cliquets, and autocallables often have non-monotonic dependence on parameters.
- **At-the-money options near expiry:** Gamma-like behavior in parameter space.
- **Correlation-sensitive products:** Basket options, dispersion trades.

### Convexity and concavity

If $H_P$ is positive definite, price is convex in parameters:

- Parameter uncertainty creates upward bias in expected price.
- Jensen's inequality: $\mathbb{E}[P(\theta)] \ge P(\mathbb{E}[\theta])$.

If $H_P$ is negative definite, the opposite holds.

---

## Propagating parameter uncertainty

### Probabilistic framework

Model parameter uncertainty as:

$$
\theta \sim \mathcal{N}(\hat{\theta}, \Sigma_\theta),
$$

where $\Sigma_\theta$ is the parameter covariance matrix (e.g., from Hessian of calibration objective, bootstrap, or Bayesian posterior).

### Price distribution (linear approximation)

Under first-order approximation:

$$
P(\theta) \approx P(\hat{\theta}) + \nabla_\theta P^\top (\theta - \hat{\theta}).
$$

Then:

$$
P \sim \mathcal{N}(P(\hat{\theta}), \nabla_\theta P^\top \Sigma_\theta \nabla_\theta P).
$$

**Price variance:**

$$
\text{Var}(P) \approx \nabla_\theta P^\top \Sigma_\theta \nabla_\theta P.
$$

**Price standard deviation (model risk):**

$$
\sigma_P = \sqrt{\nabla_\theta P^\top \Sigma_\theta \nabla_\theta P}.
$$

### Monte Carlo propagation

For nonlinear dependence or non-Gaussian parameter uncertainty:

1. Draw $N$ samples $\theta^{(i)} \sim p(\theta)$.
2. Compute $P^{(i)} = P(\theta^{(i)})$ for each sample.
3. Estimate price distribution from $\{P^{(i)}\}$.

This captures higher-order effects and non-Gaussian tails.

---

## Concentration of sensitivity

### Which parameters matter most?

Decompose price variance by parameter:

$$
\text{Var}(P) = \sum_{i,j} \frac{\partial P}{\partial \theta_i} \frac{\partial P}{\partial \theta_j} \Sigma_{\theta,ij}.
$$

If parameters are approximately independent ($\Sigma_\theta$ diagonal):

$$
\text{Var}(P) \approx \sum_i \left( \frac{\partial P}{\partial \theta_i} \right)^2 \sigma_{\theta_i}^2.
$$

The contribution of parameter $i$ is:

$$
\text{Contribution}_i = \left( \frac{\partial P}{\partial \theta_i} \right)^2 \sigma_{\theta_i}^2.
$$

### Typical patterns in option models

| Parameter | Sensitive products | Less sensitive products |
|-----------|-------------------|------------------------|
| Spot volatility $v_0$ | Short-dated options, barriers | Long-dated options |
| Mean reversion $\kappa$ | Term structure, long-dated | Short-dated ATM |
| Vol-of-vol $\sigma_v$ | Variance swaps, vol derivatives | Vanilla options (weak) |
| Correlation $\rho$ | Skew-sensitive products | ATM options |
| Long-run variance $\bar{v}$ | Long-dated options | Short-dated options |

### Dimensionality reduction

In high-dimensional parameter spaces, principal component analysis (PCA) on $\Sigma_\theta$ identifies the dominant directions of uncertainty. Price sensitivity to these principal components determines aggregate model risk.

---

## Vanilla versus exotic sensitivity

### Vanillas near calibration points

If a vanilla option is used in calibration, its price is close to market by construction. Calibration error primarily affects:

- Options **not** in the calibration set.
- The **Greeks** of calibrated options (next section).
- **Extrapolated** regions (far OTM, long maturities).

### Exotic options

Exotics depend on dynamics not fully constrained by vanilla prices:

- **Path dependence:** Barriers, lookbacks, Asians depend on the full price distribution over time.
- **Forward-starting features:** Cliquets depend on forward smiles.
- **Correlation:** Multi-asset options depend on correlation parameters often weakly identified.

**Result:** Exotics amplify calibration error.

### Example: barrier option sensitivity

A down-and-out call has price $P(\theta)$ that is highly sensitive to:

- Spot volatility (barrier proximity).
- Skew/correlation (probability mass near barrier).
- Vol-of-vol (distribution of future vol).

A $5\%$ error in $\rho$ can translate to $>10\%$ error in barrier price, far exceeding vanilla sensitivity.

---

## Quantifying model risk from calibration

### Parameter VaR

Define the $\alpha$-level parameter Value-at-Risk:

$$
\text{VaR}_\alpha^{\text{param}} = \sup_{\theta \in C_\alpha} |P(\theta) - P(\hat{\theta})|,
$$

where $C_\alpha$ is the $(1-\alpha)$ confidence region for $\theta$.

For Gaussian $\theta$ and linear $P$:

$$
\text{VaR}_\alpha^{\text{param}} = z_\alpha \cdot \sigma_P,
$$

where $z_\alpha$ is the standard normal quantile.

### Price intervals

Report prices as intervals:

$$
P \in [P(\hat{\theta}) - \text{VaR}_\alpha^{\text{param}}, \, P(\hat{\theta}) + \text{VaR}_\alpha^{\text{param}}].
$$

For asymmetric or nonlinear cases, use Monte Carlo quantiles.

### Model reserve

Banks often hold reserves for model risk:

$$
\text{Model Reserve} = \lambda \cdot \text{VaR}_\alpha^{\text{param}},
$$

where $\lambda \ge 1$ is a safety factor.

---

## Practical measurement

### Bump-and-reprice

The standard approach:

1. Calibrate to obtain $\hat{\theta}$.
2. For each parameter $\theta_i$, compute $P(\hat{\theta} + \delta e_i)$ and $P(\hat{\theta} - \delta e_i)$.
3. Estimate $\partial P / \partial \theta_i \approx (P^+ - P^-) / (2\delta)$.
4. Combine with parameter uncertainty estimates.

**Choice of bump size $\delta$:**

- Too small: numerical noise dominates.
- Too large: nonlinearity distorts estimate.
- Rule of thumb: $\delta \sim \sigma_{\theta_i}$ (one standard deviation).

### Scenario analysis

Evaluate prices under alternative calibrations:

- Calibrate to different subsets of data.
- Use different objective functions or weights.
- Perturb data within bid-ask spreads.

The dispersion of prices across scenarios quantifies model risk.

### Alternative model comparison

Price the same product under different models (Heston, SABR, local vol). The range of prices reflects model uncertainty beyond parameter uncertainty.

---

## Example: Heston model calibration error

### Setup

Suppose we calibrate Heston to SPX options and obtain:

$$
\hat{\theta} = (v_0, \kappa, \bar{v}, \sigma_v, \rho) = (0.04, 2.0, 0.04, 0.5, -0.7).
$$

Bootstrap analysis yields approximate standard errors:

$$
\sigma_\theta = (0.002, 0.3, 0.005, 0.05, 0.05).
$$

### Vanilla option

For an ATM 3-month call, sensitivities are approximately:

$$
\nabla_\theta P \approx (0.5, 0.01, 0.1, 0.02, 0.05).
$$

Price standard deviation:

$$
\sigma_P \approx \sqrt{(0.5)^2(0.002)^2 + (0.01)^2(0.3)^2 + \cdots} \approx 0.001.
$$

This is small relative to the option price (~$5$), so model risk is modest.

### Barrier option

For a down-and-out call (barrier 10% below spot), sensitivities are larger:

$$
\nabla_\theta P \approx (2.0, 0.05, 0.3, 0.2, 0.8).
$$

Price standard deviation:

$$
\sigma_P \approx 0.05,
$$

which may be $5$–$10\%$ of the option value—significant model risk.

---

## Key takeaways

- Calibration error propagates to prices via the gradient $\nabla_\theta P$.
- First-order approximation often suffices for vanillas; exotics may need higher-order analysis.
- Parameter variance $\Sigma_\theta$ can be estimated via Hessian, bootstrap, or Bayesian methods.
- Exotics amplify calibration error due to path dependence and sensitivity to weakly identified parameters.
- Model risk should be quantified and reserved against.

---

## Further reading

- Cont, "Model Uncertainty and Its Impact on Pricing" (2006).
- Glasserman, *Monte Carlo Methods in Financial Engineering* (sensitivity estimation).
- Rebonato, *Volatility and Correlation* (model risk in practice).
- Hull, *Options, Futures, and Other Derivatives* (bump-and-reprice).
