# Parameter Stability and Identifiability

A calibrated model is only useful if its parameters are stable over time and well-identified by the calibration instruments. In practice, Hull-White parameters $(\lambda, \sigma)$ calibrated daily to market data can exhibit large day-to-day fluctuations even when the underlying market moves are small. This instability creates challenges for hedging, risk management, and P\&L attribution. This section analyzes the sources of parameter instability, discusses identifiability conditions, and presents regularization techniques that improve stability without sacrificing fit quality.

## Day-to-Day Parameter Variation

When the model is recalibrated daily to the current cap or swaption market, the parameters $(\lambda_t, \sigma_t)$ form a time series. Ideally, small market moves should produce small parameter changes, but in practice:

- $\lambda$ can jump significantly because the swaption volatility surface has a near-flat region where different $(\lambda, \sigma)$ pairs produce similar prices
- $\sigma$ is more stable because it scales the overall volatility level, which is directly observed

The parameter variation can be quantified by the daily standard deviation:

$$
\text{std}(\Delta \lambda) = \sqrt{\frac{1}{T-1}\sum_{t=1}^{T-1}(\lambda_{t+1} - \lambda_t)^2}
$$

and similarly for $\sigma$. A useful diagnostic is the ratio of parameter variation to the variation in the calibration targets:

$$
R_\lambda = \frac{\text{std}(\Delta \lambda) / \bar{\lambda}}{\text{std}(\Delta \sigma_{\text{market}}) / \bar{\sigma}_{\text{market}}}
$$

Values of $R_\lambda \gg 1$ indicate that $\lambda$ is amplifying market noise.

## Identifiability

A parameter is identifiable if the calibration data uniquely determines its value. Formally, $(\lambda, \sigma)$ are identifiable if the map

$$
(\lambda, \sigma) \mapsto \left(\sigma_1^{\text{HW}}(\lambda, \sigma), \ldots, \sigma_n^{\text{HW}}(\lambda, \sigma)\right)
$$

is injective in a neighborhood of the true parameters.

**Proposition.** In the Hull-White model, $\sigma$ is well-identified from the at-the-money cap volatility level: $\partial \sigma_k^{\text{HW}} / \partial \sigma > 0$ for all $k$. The mean-reversion $\lambda$ is identified from the slope of the volatility term structure: $\partial \sigma_k^{\text{HW}} / \partial \lambda$ changes sign or magnitude across maturities.

The **Fisher information matrix** quantifies identifiability:

$$
I(\lambda, \sigma) = J^{\top} W J
$$

where $J$ is the Jacobian of model volatilities with respect to parameters and $W$ is the weight matrix. The eigenvalues of $I$ measure how well each parameter direction is determined:

- A large eigenvalue means the corresponding parameter combination is tightly constrained
- A small eigenvalue indicates a poorly identified direction, leading to instability

!!! warning "Near-Singular Fisher Information"
    When the smallest eigenvalue of $I$ is close to zero, the parameters are nearly unidentifiable in one direction. This typically manifests as a long, narrow valley in the objective function, allowing the optimizer to wander along the valley floor without significantly increasing the error. Regularization addresses this by adding curvature to the valley.

## Condition Number

The condition number of the Fisher information matrix,

$$
\kappa = \frac{\lambda_{\max}(I)}{\lambda_{\min}(I)}
$$

measures the sensitivity of the calibrated parameters to perturbations in the market data. A large condition number ($\kappa > 100$) signals potential instability.

**Proposition.** The condition number of the Hull-White calibration problem increases with $\lambda$: when mean-reversion is strong, the caplet volatilities $\sigma_k^{\text{HW}}$ become insensitive to $\lambda$ for short maturities (because $B(T_k, T_{k+1}) \approx \delta_k$ regardless of $\lambda$ when $\lambda\delta_k \ll 1$), concentrating the $\lambda$-sensitivity in long-dated instruments and making the identification fragile.

## Tikhonov Regularization

The most common regularization approach adds a penalty for deviating from a prior parameter set $(\lambda_{\text{prior}}, \sigma_{\text{prior}})$:

$$
\min_{\lambda, \sigma}\; f(\lambda, \sigma) + \mu_\lambda\,(\lambda - \lambda_{\text{prior}})^2 + \mu_\sigma\,(\sigma - \sigma_{\text{prior}})^2
$$

where $f$ is the original calibration objective and $\mu_\lambda, \mu_\sigma \geq 0$ are regularization strengths.

The prior can be:

- **Yesterday's parameters**: $(\lambda_{\text{prior}}, \sigma_{\text{prior}}) = (\lambda_{t-1}, \sigma_{t-1})$, encouraging temporal stability
- **Historical average**: computed over a rolling window, anchoring to a long-run estimate
- **Expert judgment**: based on economic reasoning about the mean-reversion speed

The regularized solution balances data fit against parameter stability:

$$
(\lambda^*, \sigma^*) = \arg\min\; \underbrace{f(\lambda, \sigma)}_{\text{market fit}} + \underbrace{\mu\,\|(\lambda, \sigma) - (\lambda_{\text{prior}}, \sigma_{\text{prior}})\|^2}_{\text{stability}}
$$

## Choosing Regularization Strength

The regularization parameters $\mu_\lambda$ and $\mu_\sigma$ control the bias-variance trade-off:

- **Too small**: no stability improvement; parameters still noisy
- **Too large**: parameters frozen near the prior, ignoring market information
- **Just right**: parameters respond to genuine market moves but filter out noise

A practical approach is cross-validation: hold out one calibration instrument, calibrate to the rest, and check the held-out error. The optimal $\mu$ minimizes the average held-out error.

Alternatively, the L-curve method plots the regularization penalty against the data fit residual as $\mu$ varies, and selects $\mu$ at the "elbow" of the resulting curve.

## Temporal Smoothing

An extension of Tikhonov regularization penalizes the rate of parameter change over time:

$$
\min_{\lambda_1, \sigma_1, \ldots, \lambda_T, \sigma_T}\; \sum_{t=1}^{T} f_t(\lambda_t, \sigma_t) + \mu \sum_{t=2}^{T}\left[(\lambda_t - \lambda_{t-1})^2 + (\sigma_t - \sigma_{t-1})^2\right]
$$

This jointly optimizes parameters across multiple days, producing a smoother parameter path. The cost is that the optimization problem becomes larger and requires historical data.

???+ example "Regularized Calibration"
    ```python
    def main():
        hw = HullWhite(sigma=0.01, lambd=0.05, P=P_market)

        # Previous day's parameters
        lambd_prior = 0.048
        sigma_prior = 0.0098
        mu_lambd = 10.0
        mu_sigma = 1000.0

        def objective(params):
            lambd, sigma = params
            hw.lambd = lambd
            hw.sigma = sigma
            fit_error = sum((hw.implied_vol(T) - s_mkt)**2
                           for T, s_mkt in zip(maturities, market_vols))
            reg_penalty = (mu_lambd * (lambd - lambd_prior)**2
                          + mu_sigma * (sigma - sigma_prior)**2)
            return fit_error + reg_penalty

        from scipy.optimize import minimize
        result = minimize(objective, [lambd_prior, sigma_prior],
                         method='L-BFGS-B',
                         bounds=[(0.001, 1.0), (0.0001, 0.1)])
        print(f"lambda={result.x[0]:.4f}, sigma={result.x[1]:.6f}")
    ```

## Identifiability in the Two-Factor Model

The two-factor Hull-White model with five parameters $(\lambda_1, \lambda_2, \sigma_1, \sigma_2, \rho)$ has richer identifiability structure:

- $\sigma_1$ and $\sigma_2$ are identified from the overall volatility level
- $\lambda_1$ and $\lambda_2$ are identified from the decorrelation between short and long maturities
- $\rho$ is identified from the cross-maturity correlation structure

However, the model is symmetric under swapping $(\lambda_1, \sigma_1) \leftrightarrow (\lambda_2, \sigma_2)$, creating a label ambiguity. The convention $\lambda_1 < \lambda_2$ (factor 1 is the slow-reverting factor) resolves this.

## Summary

Parameter stability and identifiability are critical for the practical use of calibrated Hull-White models. Day-to-day recalibration can produce noisy parameter paths, particularly for $\lambda$, which is less well-identified than $\sigma$ from cap data. The Fisher information matrix and its condition number diagnose identifiability issues. Tikhonov regularization, penalizing deviation from a prior parameter set, stabilizes the calibration by filtering noise while preserving sensitivity to genuine market moves. Temporal smoothing extends this to multi-day parameter paths. The regularization strength is chosen via cross-validation or the L-curve method, balancing data fit against parameter stability.

---

## Exercises

**Exercise 1.** The ratio $R_\lambda = \frac{\text{std}(\Delta\lambda)/\bar{\lambda}}{\text{std}(\Delta\sigma_{\text{market}})/\bar{\sigma}_{\text{market}}}$ measures parameter amplification. If $R_\lambda = 5$, what does this mean in practical terms? If market volatilities move by 1% on a given day, how much would you expect $\lambda$ to change?

---

**Exercise 2.** The Fisher information matrix is $I = J^{\top}WJ$ where $J$ is the Jacobian of model volatilities with respect to parameters. For a two-parameter model, $I$ is $2 \times 2$. Describe what a large condition number $\kappa(I)$ implies geometrically about the shape of the objective function near the optimum. Draw a contour plot that illustrates this.

---

**Exercise 3.** Explain why $\lambda$ is less well-identified than $\sigma$ from cap data. In particular, show that for short-dated caplets ($\lambda\delta_k \ll 1$), the bond price volatility $\sigma_P$ is approximately independent of $\lambda$, making those instruments uninformative about $\lambda$.

---

**Exercise 4.** Tikhonov regularization adds the penalty $\mu_\lambda(\lambda - \lambda_{\text{prior}})^2 + \mu_\sigma(\sigma - \sigma_{\text{prior}})^2$ to the objective. Derive the regularized first-order conditions and show that the regularized solution is a weighted average of the unconstrained optimum and the prior, with weights determined by $\mu$.

---

**Exercise 5.** Describe the L-curve method for choosing the regularization strength $\mu$. Plot schematically the regularization penalty versus the data-fit residual as $\mu$ varies from $0$ to $\infty$. Where is the optimal $\mu$ located on this curve, and why?

---

**Exercise 6.** In the two-factor model, swapping $(\lambda_1, \sigma_1) \leftrightarrow (\lambda_2, \sigma_2)$ gives the same model. Explain why this label symmetry creates identifiability problems. How does the convention $\lambda_1 < \lambda_2$ resolve the issue, and what constraint would you impose in the optimizer?

---

**Exercise 7.** Temporal smoothing jointly optimizes parameters across multiple days with the penalty $\mu\sum_{t=2}^T[(\lambda_t - \lambda_{t-1})^2 + (\sigma_t - \sigma_{t-1})^2]$. Discuss the trade-offs of this approach: what happens when $\mu$ is too large? Too small? How does the computational cost scale with the number of days $T$?
