# Sensitivity of Prices to Calibration Error

Calibration error translates directly into **model risk**: even small mis-estimation of parameters can lead to non-negligible pricing errors, especially for nonlinear or path-dependent payoffs. This section develops the framework for quantifying this sensitivity.

---

## From parameter error to price error

### First-order approximation

Let $\hat{\theta}$ be the calibrated parameter vector and $\theta^{\star}$ the (unknown) true parameter. For a derivative price $P(\theta)$, a Taylor expansion gives:

$$
P(\theta^{\star}) - P(\hat{\theta}) \approx \nabla_\theta P(\hat{\theta})^\top (\theta^{\star} - \hat{\theta})
$$

Rearranging:

$$
\Delta P := P(\hat{\theta}) - P(\theta^{\star}) \approx -\nabla_\theta P(\hat{\theta})^\top \Delta\theta
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
\Delta P \approx \nabla_\theta P^\top \Delta\theta + \frac{1}{2} \Delta\theta^\top H_P \Delta\theta
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
\theta \sim \mathcal{N}(\hat{\theta}, \Sigma_\theta)
$$

where $\Sigma_\theta$ is the parameter covariance matrix (e.g., from Hessian of calibration objective, bootstrap, or Bayesian posterior).

### Price distribution (linear approximation)

Under first-order approximation:

$$
P(\theta) \approx P(\hat{\theta}) + \nabla_\theta P^\top (\theta - \hat{\theta})
$$

Then:

$$
P \sim \mathcal{N}(P(\hat{\theta}), \nabla_\theta P^\top \Sigma_\theta \nabla_\theta P)
$$

**Price variance:**

$$
\text{Var}(P) \approx \nabla_\theta P^\top \Sigma_\theta \nabla_\theta P
$$

**Price standard deviation (model risk):**

$$
\sigma_P = \sqrt{\nabla_\theta P^\top \Sigma_\theta \nabla_\theta P}
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
\text{Var}(P) = \sum_{i,j} \frac{\partial P}{\partial \theta_i} \frac{\partial P}{\partial \theta_j} \Sigma_{\theta,ij}
$$

If parameters are approximately independent ($\Sigma_\theta$ diagonal):

$$
\text{Var}(P) \approx \sum_i \left( \frac{\partial P}{\partial \theta_i} \right)^2 \sigma_{\theta_i}^2
$$

The contribution of parameter $i$ is:

$$
\text{Contribution}_i = \left( \frac{\partial P}{\partial \theta_i} \right)^2 \sigma_{\theta_i}^2
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
\text{VaR}_\alpha^{\text{param}} = \sup_{\theta \in C_\alpha} |P(\theta) - P(\hat{\theta})|
$$

where $C_\alpha$ is the $(1-\alpha)$ confidence region for $\theta$.

For Gaussian $\theta$ and linear $P$:

$$
\text{VaR}_\alpha^{\text{param}} = z_\alpha \cdot \sigma_P
$$

where $z_\alpha$ is the standard normal quantile.

### Price intervals

Report prices as intervals:

$$
P \in [P(\hat{\theta}) - \text{VaR}_\alpha^{\text{param}}, \, P(\hat{\theta}) + \text{VaR}_\alpha^{\text{param}}]
$$

For asymmetric or nonlinear cases, use Monte Carlo quantiles.

### Model reserve

Banks often hold reserves for model risk:

$$
\text{Model Reserve} = \lambda \cdot \text{VaR}_\alpha^{\text{param}}
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
\hat{\theta} = (v_0, \kappa, \bar{v}, \sigma_v, \rho) = (0.04, 2.0, 0.04, 0.5, -0.7)
$$

Bootstrap analysis yields approximate standard errors:

$$
\sigma_\theta = (0.002, 0.3, 0.005, 0.05, 0.05)
$$

### Vanilla option

For an ATM 3-month call, sensitivities are approximately:

$$
\nabla_\theta P \approx (0.5, 0.01, 0.1, 0.02, 0.05)
$$

Price standard deviation:

$$
\sigma_P \approx \sqrt{(0.5)^2(0.002)^2 + (0.01)^2(0.3)^2 + \cdots} \approx 0.001
$$

This is small relative to the option price (~$5$), so model risk is modest.

### Barrier option

For a down-and-out call (barrier 10% below spot), sensitivities are larger:

$$
\nabla_\theta P \approx (2.0, 0.05, 0.3, 0.2, 0.8)
$$

Price standard deviation:

$$
\sigma_P \approx 0.05
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

---

## Exercises

**Exercise 1.** Given the parameter covariance $\Sigma_\theta = \text{diag}(\sigma_{v_0}^2, \sigma_\kappa^2, \sigma_{\bar{v}}^2, \sigma_{\sigma_v}^2, \sigma_\rho^2)$ and price gradient $\nabla_\theta P$, derive the formula for price standard deviation $\sigma_P = \sqrt{\nabla_\theta P^\top \Sigma_\theta \nabla_\theta P}$. Using the Heston example values $\hat{\theta} = (0.04, 2.0, 0.04, 0.5, -0.7)$, $\sigma_\theta = (0.002, 0.3, 0.005, 0.05, 0.05)$, and $\nabla_\theta P = (0.5, 0.01, 0.1, 0.02, 0.05)$ for a vanilla option, compute $\sigma_P$ and the contribution of each parameter.

??? success "Solution to Exercise 1"
    **Derivation of the price standard deviation formula.**

    Starting from the first-order Taylor expansion:

    $$
    P(\theta) \approx P(\hat{\theta}) + \nabla_\theta P(\hat{\theta})^\top (\theta - \hat{\theta})
    $$

    The price error is $P(\theta) - P(\hat{\theta}) \approx \nabla_\theta P^\top (\theta - \hat{\theta})$. Under the probabilistic model $\theta \sim \mathcal{N}(\hat{\theta}, \Sigma_\theta)$, we compute:

    $$
    \text{Var}(P) = \text{Var}\!\left(\nabla_\theta P^\top (\theta - \hat{\theta})\right) = \nabla_\theta P^\top \text{Cov}(\theta - \hat{\theta}) \nabla_\theta P = \nabla_\theta P^\top \Sigma_\theta \nabla_\theta P
    $$

    using the standard result $\text{Var}(a^\top X) = a^\top \Sigma_X a$ for constant $a$. Therefore:

    $$
    \sigma_P = \sqrt{\nabla_\theta P^\top \Sigma_\theta \nabla_\theta P}
    $$

    **Numerical computation for the vanilla option.**

    With $\Sigma_\theta = \text{diag}(0.002^2, 0.3^2, 0.005^2, 0.05^2, 0.05^2)$ and $\nabla_\theta P = (0.5, 0.01, 0.1, 0.02, 0.05)$:

    $$
    \text{Var}(P) = \sum_{i=1}^{5} \left(\frac{\partial P}{\partial \theta_i}\right)^2 \sigma_{\theta_i}^2
    $$

    Computing each term:

    | Parameter | $\partial P / \partial \theta_i$ | $\sigma_{\theta_i}$ | Contribution $= (\partial P/\partial \theta_i)^2 \sigma_{\theta_i}^2$ |
    |-----------|------|------|------|
    | $v_0$ | 0.5 | 0.002 | $(0.5)^2(0.002)^2 = 1.000 \times 10^{-6}$ |
    | $\kappa$ | 0.01 | 0.3 | $(0.01)^2(0.3)^2 = 9.000 \times 10^{-6}$ |
    | $\bar{v}$ | 0.1 | 0.005 | $(0.1)^2(0.005)^2 = 2.500 \times 10^{-7}$ |
    | $\sigma_v$ | 0.02 | 0.05 | $(0.02)^2(0.05)^2 = 1.000 \times 10^{-6}$ |
    | $\rho$ | 0.05 | 0.05 | $(0.05)^2(0.05)^2 = 6.250 \times 10^{-6}$ |

    Summing: $\text{Var}(P) = 1.000 + 9.000 + 0.250 + 1.000 + 6.250 = 17.500 \times 10^{-6}$

    $$
    \sigma_P = \sqrt{1.750 \times 10^{-5}} \approx 0.00418
    $$

    **Contribution analysis (percentage of total variance):**

    - $v_0$: $1.000 / 17.500 = 5.7\%$
    - $\kappa$: $9.000 / 17.500 = 51.4\%$
    - $\bar{v}$: $0.250 / 17.500 = 1.4\%$
    - $\sigma_v$: $1.000 / 17.500 = 5.7\%$
    - $\rho$: $6.250 / 17.500 = 35.7\%$

    The dominant sources of model risk for the vanilla option are $\kappa$ (mean reversion) and $\rho$ (correlation), despite $\kappa$ having a small price sensitivity, because its parameter uncertainty ($\sigma_\kappa = 0.3$) is large. The price standard deviation of $\approx 0.004$ is small relative to a typical ATM option price ($\sim 5$), confirming that vanilla model risk is modest.

---

**Exercise 2.** For a down-and-out call with barrier 10% below spot, the price gradient is $\nabla_\theta P = (2.0, 0.05, 0.3, 0.2, 0.8)$ with the same $\sigma_\theta$ as Exercise 1. Compute $\sigma_P$ and identify the dominant source of model risk. Compare to the vanilla case and explain why barriers amplify calibration sensitivity.

??? success "Solution to Exercise 2"
    **Computation for the barrier option.**

    With $\nabla_\theta P = (2.0, 0.05, 0.3, 0.2, 0.8)$ and the same $\sigma_\theta$:

    | Parameter | $\partial P / \partial \theta_i$ | $\sigma_{\theta_i}$ | Contribution |
    |-----------|------|------|------|
    | $v_0$ | 2.0 | 0.002 | $(2.0)^2(0.002)^2 = 1.600 \times 10^{-5}$ |
    | $\kappa$ | 0.05 | 0.3 | $(0.05)^2(0.3)^2 = 2.250 \times 10^{-4}$ |
    | $\bar{v}$ | 0.3 | 0.005 | $(0.3)^2(0.005)^2 = 2.250 \times 10^{-6}$ |
    | $\sigma_v$ | 0.2 | 0.05 | $(0.2)^2(0.05)^2 = 1.000 \times 10^{-4}$ |
    | $\rho$ | 0.8 | 0.05 | $(0.8)^2(0.05)^2 = 1.600 \times 10^{-3}$ |

    Summing: $\text{Var}(P) = 0.0160 + 0.2250 + 0.0023 + 0.1000 + 1.6000 = 1.9433 \times 10^{-3}$

    $$
    \sigma_P = \sqrt{1.9433 \times 10^{-3}} \approx 0.0441
    $$

    **Dominant source of model risk:** Correlation $\rho$ contributes $1.600 \times 10^{-3}$ out of $1.943 \times 10^{-3}$, which is **82.3%** of total variance. The next largest is $\kappa$ at 11.6%, followed by $\sigma_v$ at 5.1%.

    **Comparison to vanilla case:**

    - Barrier $\sigma_P \approx 0.044$ vs. vanilla $\sigma_P \approx 0.004$: the barrier option has roughly **10 times** the price standard deviation.
    - The dominant risk factor shifts from $\kappa$ (vanilla) to $\rho$ (barrier).

    **Why barriers amplify calibration sensitivity:**

    1. **Discontinuous payoff:** The barrier condition creates a discontinuity in the payoff function. Small changes in the probability distribution near the barrier (driven by $\rho$, $\sigma_v$) lead to large price changes.

    2. **Path dependence:** The barrier option price depends on the entire distribution of the spot process over $[0, T]$, not just the terminal distribution. Parameters like $\rho$ and $\sigma_v$ control the dynamics of the joint spot-vol process, which determines how likely the spot is to breach the barrier during its path.

    3. **Sensitivity to skew and tails:** Correlation $\rho$ controls the skew of the implied volatility surface. For a down-and-out call, the probability mass near the lower barrier is highly sensitive to skew: more negative $\rho$ means more probability in the left tail, increasing the knock-out probability and reducing the option price. This effect is much stronger than for vanilla options, which depend primarily on the volatility at the strike.

    4. **Nonlinear parameter dependence:** Barrier option prices are typically convex or concave in parameters near the barrier, so second-order effects (ignored in the linear approximation) further amplify the sensitivity.

---

**Exercise 3.** Using the second-order Taylor expansion $\Delta P \approx \nabla_\theta P^\top \Delta\theta + \frac{1}{2}\Delta\theta^\top H_P \Delta\theta$, explain when the second-order term is important. For a product where $H_P$ is positive definite, show that $\mathbb{E}[\Delta P] \ne 0$ even when $\mathbb{E}[\Delta\theta] = 0$. Compute the bias $\mathbb{E}[\Delta P] = \frac{1}{2}\text{tr}(H_P \Sigma_\theta)$ and discuss its implications for mark-to-model pricing.

??? success "Solution to Exercise 3"
    **When the second-order term matters.**

    The second-order Taylor expansion is:

    $$
    \Delta P \approx \nabla_\theta P^\top \Delta\theta + \frac{1}{2}\Delta\theta^\top H_P \Delta\theta
    $$

    The second-order term $\frac{1}{2}\Delta\theta^\top H_P \Delta\theta$ is important when:

    - The parameter error $\|\Delta\theta\|$ is large relative to the scale over which $P(\theta)$ is approximately linear.
    - The Hessian $H_P$ has large eigenvalues (strong curvature in parameter space).
    - The product is an exotic with non-monotonic or discontinuous parameter dependence (barriers, digitals, cliquets).

    Quantitatively, the second-order term matters when $\frac{1}{2}|\Delta\theta^\top H_P \Delta\theta|$ is comparable to $|\nabla_\theta P^\top \Delta\theta|$.

    **Bias when $H_P$ is positive definite.**

    Taking expectations with $\mathbb{E}[\Delta\theta] = 0$ (unbiased estimation):

    $$
    \mathbb{E}[\Delta P] = \nabla_\theta P^\top \underbrace{\mathbb{E}[\Delta\theta]}_{=0} + \frac{1}{2}\mathbb{E}[\Delta\theta^\top H_P \Delta\theta]
    $$

    The second term is:

    $$
    \mathbb{E}[\Delta\theta^\top H_P \Delta\theta] = \mathbb{E}\!\left[\sum_{i,j} (H_P)_{ij} \Delta\theta_i \Delta\theta_j\right] = \sum_{i,j} (H_P)_{ij} \mathbb{E}[\Delta\theta_i \Delta\theta_j] = \sum_{i,j} (H_P)_{ij} (\Sigma_\theta)_{ij}
    $$

    $$
    = \text{tr}(H_P \Sigma_\theta)
    $$

    Therefore:

    $$
    \mathbb{E}[\Delta P] = \frac{1}{2}\text{tr}(H_P \Sigma_\theta)
    $$

    When $H_P$ is positive definite, all eigenvalues of $H_P$ are positive, and since $\Sigma_\theta$ is positive semi-definite, $\text{tr}(H_P \Sigma_\theta) > 0$. This means:

    $$
    \mathbb{E}[\Delta P] > 0
    $$

    **Implications for mark-to-model pricing:**

    - Even with an unbiased parameter estimator, the **price estimate is biased upward** when the price is convex in parameters. This is a consequence of Jensen's inequality: $\mathbb{E}[P(\theta)] > P(\mathbb{E}[\theta])$.

    - The bias $\frac{1}{2}\text{tr}(H_P \Sigma_\theta)$ is always positive for convex products, meaning the expected model price **overestimates** the true price (evaluated at the true parameters). This creates a systematic mark-to-model error.

    - For concave products ($H_P$ negative definite), the bias is negative: the model systematically **underestimates** the price.

    - This bias is sometimes called the **convexity adjustment** for parameter uncertainty. It should be accounted for in valuation adjustments (model reserve or XVA-like corrections), particularly for exotic products where $H_P$ is large.

    - The magnitude of the bias depends on the product of two factors: the curvature of the price ($H_P$) and the magnitude of parameter uncertainty ($\Sigma_\theta$). Reducing either (through better models or more precise calibration) reduces the bias.

---

**Exercise 4.** Describe the bump-and-reprice method for estimating $\partial P / \partial \theta_i$. Why should the bump size $\delta$ be chosen on the order of $\sigma_{\theta_i}$? For a Monte Carlo pricer with numerical noise $\sigma_{\text{MC}} = 0.01$, derive the minimum bump size needed for the signal $|P(\theta + \delta e_i) - P(\theta - \delta e_i)|$ to exceed the noise level $2\sigma_{\text{MC}}$, given $\partial P / \partial \theta_i = 0.5$.

??? success "Solution to Exercise 4"
    **Bump-and-reprice method.**

    The procedure estimates the price sensitivity $\partial P / \partial \theta_i$ by central differencing:

    1. Start with calibrated parameters $\hat{\theta}$.
    2. For parameter $i$, create perturbed vectors $\hat{\theta}^+ = \hat{\theta} + \delta e_i$ and $\hat{\theta}^- = \hat{\theta} - \delta e_i$.
    3. Price the derivative under both: $P^+ = P(\hat{\theta}^+)$ and $P^- = P(\hat{\theta}^-)$.
    4. Estimate: $\frac{\partial P}{\partial \theta_i} \approx \frac{P^+ - P^-}{2\delta}$.

    **Why $\delta \sim \sigma_{\theta_i}$:**

    - If $\delta \ll \sigma_{\theta_i}$: the bump is much smaller than the actual parameter uncertainty. The price change $P^+ - P^-$ becomes dominated by numerical noise (Monte Carlo variance, finite-difference truncation error). The signal-to-noise ratio is poor.

    - If $\delta \gg \sigma_{\theta_i}$: the bump overshoots the relevant region of parameter space. The finite difference captures the average slope over a range much wider than the uncertainty region, potentially including nonlinear effects that distort the local sensitivity estimate.

    - $\delta \sim \sigma_{\theta_i}$ matches the bump to the actual scale of parameter uncertainty, providing the best trade-off: the sensitivity is measured over the relevant range while maintaining adequate signal-to-noise.

    **Minimum bump size given Monte Carlo noise.**

    The signal from the central difference is:

    $$
    |P^+ - P^-| \approx 2\delta \left|\frac{\partial P}{\partial \theta_i}\right|
    $$

    Each of $P^+$ and $P^-$ has Monte Carlo noise $\sigma_{\text{MC}} = 0.01$, so the noise in their difference is:

    $$
    \sigma_{\text{diff}} = \sqrt{\sigma_{\text{MC}}^2 + \sigma_{\text{MC}}^2} = \sigma_{\text{MC}}\sqrt{2} = 0.01\sqrt{2} \approx 0.01414
    $$

    For the signal to exceed the noise at, say, a $2\sigma$ significance level:

    $$
    2\delta \left|\frac{\partial P}{\partial \theta_i}\right| > 2\sigma_{\text{diff}}
    $$

    $$
    2\delta \times 0.5 > 2 \times 0.01414
    $$

    $$
    \delta > \frac{2 \times 0.01414}{2 \times 0.5} = \frac{0.02828}{1.0} = 0.02828
    $$

    So the minimum bump size is $\delta_{\min} \approx 0.028$. If this exceeds $\sigma_{\theta_i}$ for some parameter, then either the Monte Carlo sample size must be increased (to reduce $\sigma_{\text{MC}}$) or variance reduction techniques (common random numbers, antithetic variates) must be employed. Using the same random number seeds for $P^+$ and $P^-$ (common random numbers) dramatically reduces $\sigma_{\text{diff}}$, allowing smaller $\delta$.

---

**Exercise 5.** A principal component analysis of $\Sigma_\theta$ reveals that 90% of parameter variance is captured by the first two eigenvectors. Describe how to use these principal components to efficiently estimate the price standard deviation $\sigma_P$. If the first eigenvector points in the $(\kappa, \bar{v})$ direction, what does this suggest about the structure of parameter uncertainty?

??? success "Solution to Exercise 5"
    **PCA-based efficient estimation.**

    Let the eigendecomposition of $\Sigma_\theta$ be:

    $$
    \Sigma_\theta = \sum_{k=1}^{d} \lambda_k u_k u_k^\top
    $$

    where $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_d$ are eigenvalues and $u_k$ are orthonormal eigenvectors. The price variance is:

    $$
    \sigma_P^2 = \nabla_\theta P^\top \Sigma_\theta \nabla_\theta P = \sum_{k=1}^{d} \lambda_k (\nabla_\theta P^\top u_k)^2
    $$

    If 90% of parameter variance is captured by the first two eigenvectors ($\lambda_1 + \lambda_2 \ge 0.9 \cdot \text{tr}(\Sigma_\theta)$), we can approximate:

    $$
    \sigma_P^2 \approx \lambda_1 (\nabla_\theta P^\top u_1)^2 + \lambda_2 (\nabla_\theta P^\top u_2)^2
    $$

    **Efficient estimation procedure:**

    1. Compute $\Sigma_\theta$ from perturbation analysis or bootstrap.
    2. Find the top two eigenvectors $u_1, u_2$ and eigenvalues $\lambda_1, \lambda_2$.
    3. Compute the price sensitivity along each principal direction: $g_k = \nabla_\theta P^\top u_k$ for $k = 1, 2$. This can be done with just two bump-and-reprice evaluations (bump along $u_1$ and $u_2$) instead of $d$ evaluations (one per parameter).
    4. Estimate $\sigma_P \approx \sqrt{\lambda_1 g_1^2 + \lambda_2 g_2^2}$.

    This reduces the computational cost from $2d$ pricings (for $d$ parameters) to just 4 pricings (two bumps, each requiring up and down), while capturing 90% of the model risk.

    **Interpretation of the first eigenvector pointing in the $(\kappa, \bar{v})$ direction.**

    If $u_1$ has large components in the $\kappa$ and $\bar{v}$ directions, this means:

    - The dominant source of parameter uncertainty is in the **joint $(\kappa, \bar{v})$ space**. The mean-reversion speed and long-run variance are the most uncertain parameters.

    - These two parameters are likely **highly correlated** in the posterior: many different $(\kappa, \bar{v})$ pairs produce similar model fits. This is a well-known identification problem in Heston: the long-run mean of variance under the risk-neutral measure is $\bar{v}$, but the speed at which variance reverts to $\bar{v}$ is $\kappa$. The product $\kappa \bar{v}$ (the drift of variance when $v$ is small) is better identified than either parameter individually.

    - This suggests a **reparametrization**: instead of calibrating $(\kappa, \bar{v})$ independently, one could calibrate $(\kappa \bar{v}, \kappa)$ or $(\bar{v}, \kappa / \bar{v})$, which may reduce the dominant eigenvalue and improve calibration stability.

    - For model risk, the practical implication is that the price uncertainty is dominated by uncertainty about the **long-term volatility dynamics** rather than the short-term spot volatility or skew parameters.

---

**Exercise 6.** Define Parameter VaR as $\text{VaR}_\alpha^{\text{param}} = z_\alpha \cdot \sigma_P$. For a portfolio of 10 exotic options, each with $\sigma_{P_i}$ computed independently, the total model risk is not simply $\sum_i \sigma_{P_i}$ due to correlation. Derive the correct formula for portfolio-level $\sigma_P^{\text{portfolio}}$ accounting for the fact that all options depend on the same parameters $\theta$. Show that diversification of model risk is limited when sensitivities have the same sign.

??? success "Solution to Exercise 6"
    **Portfolio-level model risk.**

    Consider a portfolio of $n = 10$ exotic options with prices $P_1(\theta), \ldots, P_{10}(\theta)$, all depending on the same parameter vector $\theta$. The portfolio value is:

    $$
    V(\theta) = \sum_{i=1}^{10} P_i(\theta)
    $$

    Using the first-order approximation:

    $$
    V(\theta) \approx V(\hat{\theta}) + \left(\sum_{i=1}^{10} \nabla_\theta P_i\right)^\top (\theta - \hat{\theta})
    $$

    The portfolio price variance is:

    $$
    \sigma_V^2 = \left(\sum_{i=1}^{10} \nabla_\theta P_i\right)^\top \Sigma_\theta \left(\sum_{i=1}^{10} \nabla_\theta P_i\right)
    $$

    Expanding:

    $$
    \sigma_V^2 = \sum_{i=1}^{10} \sum_{j=1}^{10} \nabla_\theta P_i^\top \Sigma_\theta \nabla_\theta P_j = \sum_{i=1}^{10} \sigma_{P_i}^2 + 2\sum_{i < j} \nabla_\theta P_i^\top \Sigma_\theta \nabla_\theta P_j
    $$

    The cross-term $\nabla_\theta P_i^\top \Sigma_\theta \nabla_\theta P_j$ is the **model risk covariance** between options $i$ and $j$.

    **Why diversification is limited when sensitivities have the same sign.**

    The model risk correlation between two options is:

    $$
    \rho_{ij}^{\text{model}} = \frac{\nabla_\theta P_i^\top \Sigma_\theta \nabla_\theta P_j}{\sigma_{P_i} \sigma_{P_j}}
    $$

    If all options have price gradients $\nabla_\theta P_i$ pointing in similar directions (same sign for the dominant parameters), then $\rho_{ij}^{\text{model}} \approx 1$ for all pairs. In the extreme case where all gradients are proportional ($\nabla_\theta P_i = c_i g$ for some common direction $g$):

    $$
    \sigma_V^2 = \left(\sum_i c_i\right)^2 g^\top \Sigma_\theta g = \left(\sum_i c_i\right)^2 \sigma_g^2
    $$

    $$
    \sigma_V = \left|\sum_i c_i\right| \sigma_g = \sum_i |c_i| \sigma_g = \sum_i \sigma_{P_i}
    $$

    There is **no diversification**: portfolio model risk equals the sum of individual model risks.

    This contrasts with market risk, where positions in different underlyings may have low or negative correlations. Model risk from calibration is fundamentally different: all options in the portfolio are exposed to the **same** parameter uncertainty. Diversification of model risk requires positions with **opposing** parameter sensitivities (e.g., one option that increases in value when $\rho$ increases and another that decreases), which is difficult to achieve unless the portfolio is deliberately constructed to hedge model risk.

    **Portfolio Parameter VaR:**

    $$
    \text{VaR}_\alpha^{\text{portfolio}} = z_\alpha \cdot \sigma_V = z_\alpha \sqrt{\sum_{i,j} \nabla_\theta P_i^\top \Sigma_\theta \nabla_\theta P_j}
    $$

    This is generally much larger than $z_\alpha \sqrt{\sum_i \sigma_{P_i}^2}$ (which would be the VaR if model risks were independent) and can approach $z_\alpha \sum_i \sigma_{P_i}$ (the VaR if model risks are perfectly correlated).

---

**Exercise 7.** A trader prices a 1-year cliquet option under the Heston, SABR, and local volatility models, obtaining prices of 4.2, 3.8, and 5.1 respectively, all calibrated to the same vanilla surface. Discuss how this price range reflects model risk beyond parameter uncertainty. How would you combine the within-model parameter uncertainty (from calibration error) with the across-model uncertainty to produce a single confidence interval for the fair price?

??? success "Solution to Exercise 7"
    **Model risk beyond parameter uncertainty.**

    The three prices (Heston: 4.2, SABR: 3.8, Local vol: 5.1) span a range of 1.3, despite all models being calibrated to the same vanilla surface. This price dispersion reflects **structural model risk**: the models agree on vanilla prices (by construction of the calibration) but disagree on the cliquet because:

    1. **Different dynamics:** The models imply different dynamics for the forward smile. Heston generates stochastic volatility with mean reversion; SABR generates a correlated spot-vol diffusion without mean reversion; local volatility generates deterministic, state-dependent volatility. A cliquet option depends critically on the **forward-starting implied volatility surface**, which is not pinned down by today's vanilla surface.

    2. **Forward smile effect:** Local volatility models are known to flatten forward smiles relative to stochastic volatility models. This explains why the local vol price (5.1) is highest: it overestimates future smile convexity for cliquet-type products (or equivalently, it prices forward-starting options as if future smiles are flatter, which can increase or decrease prices depending on the payoff structure; in this case, the cliquet benefits from the local vol dynamics).

    3. **Structural incompleteness:** The vanilla surface constrains only the marginal distributions of the underlying at each maturity. It does not constrain the joint distribution across maturities or the path properties, which cliquets depend on.

    **Combining within-model and across-model uncertainty.**

    Suppose each model $m \in \{\text{Heston}, \text{SABR}, \text{LV}\}$ gives a price $P_m(\hat{\theta}_m)$ with within-model parameter standard deviation $\sigma_{P_m}$.

    **Step 1: Within-model intervals.** For each model, construct a confidence interval:

    $$
    I_m = [P_m - z_\alpha \sigma_{P_m}, \; P_m + z_\alpha \sigma_{P_m}]
    $$

    **Step 2: Across-model uncertainty.** Treat the model choice as an additional source of uncertainty. A simple approach is to compute the mean and standard deviation across model prices:

    $$
    \bar{P} = \frac{1}{3}(4.2 + 3.8 + 5.1) = 4.367
    $$

    $$
    \sigma_{\text{model}} = \sqrt{\frac{1}{3}\sum_m (P_m - \bar{P})^2} = \sqrt{\frac{(4.2 - 4.367)^2 + (3.8 - 4.367)^2 + (5.1 - 4.367)^2}{3}}
    $$

    $$
    = \sqrt{\frac{0.028 + 0.322 + 0.537}{3}} = \sqrt{0.296} \approx 0.544
    $$

    **Step 3: Combined confidence interval.** Assuming within-model and across-model uncertainties are independent:

    $$
    \sigma_{\text{total}} = \sqrt{\sigma_{\text{model}}^2 + \bar{\sigma}_P^2}
    $$

    where $\bar{\sigma}_P^2 = \frac{1}{3}\sum_m \sigma_{P_m}^2$ is the average within-model variance. The combined interval is:

    $$
    P \in [\bar{P} - z_\alpha \sigma_{\text{total}}, \; \bar{P} + z_\alpha \sigma_{\text{total}}]
    $$

    **Alternative approaches:**

    - **Union of intervals:** Take $I = \bigcup_m I_m$, which gives the most conservative estimate. This is simple but may be overly wide.

    - **Bayesian model averaging:** Assign prior probabilities $w_m$ to each model (based on out-of-sample performance, economic plausibility, etc.) and compute the mixture distribution $P \sim \sum_m w_m \mathcal{N}(P_m, \sigma_{P_m}^2)$. The resulting distribution is multimodal, and the confidence interval is taken from its quantiles.

    - **Worst-case approach:** For risk management, use $P_{\min} = \min_m (P_m - z_\alpha \sigma_{P_m})$ and $P_{\max} = \max_m (P_m + z_\alpha \sigma_{P_m})$ to bound the fair price from below and above.

    In practice, the across-model uncertainty ($\sigma_{\text{model}} \approx 0.54$) typically dominates within-model parameter uncertainty for exotics. The range of $1.3$ (from 3.8 to 5.1) represents roughly 30% of the average price, underscoring that for cliquet options, **choosing the model matters more than calibrating it precisely**.
