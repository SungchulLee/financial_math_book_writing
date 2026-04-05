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

??? success "Solution to Exercise 1"
    If $R_\lambda = 5$, this means that the relative variation in $\lambda$ is 5 times larger than the relative variation in market volatilities. In practical terms, $\lambda$ amplifies market noise by a factor of 5: market volatilities might fluctuate by a small amount, but $\lambda$ fluctuates proportionally 5 times as much.

    Concretely, if market volatilities move by 1% on a given day (i.e., $\Delta\sigma_{\text{market}}/\bar{\sigma}_{\text{market}} = 0.01$), then the expected relative change in $\lambda$ is:

    $$
    \frac{\Delta\lambda}{\bar{\lambda}} \approx R_\lambda \times \frac{\Delta\sigma_{\text{market}}}{\bar{\sigma}_{\text{market}}} = 5 \times 0.01 = 0.05 = 5\%
    $$

    So if $\bar{\lambda} = 0.05$, a 1% market move could cause $\lambda$ to change by approximately $0.05 \times 5\% = 0.0025$, moving from 0.05 to 0.0475 or 0.0525. This is a substantial day-to-day variation that creates problems for hedging (because Greeks depend on $\lambda$, changing $\lambda$ changes hedge ratios), P&L attribution (parameter changes produce unexplained P&L), and risk management (VaR and other risk measures become noisy).

    A value of $R_\lambda = 5$ strongly suggests that $\lambda$ is poorly identified and regularization is needed to stabilize it.

---

**Exercise 2.** The Fisher information matrix is $I = J^{\top}WJ$ where $J$ is the Jacobian of model volatilities with respect to parameters. For a two-parameter model, $I$ is $2 \times 2$. Describe what a large condition number $\kappa(I)$ implies geometrically about the shape of the objective function near the optimum. Draw a contour plot that illustrates this.

??? success "Solution to Exercise 2"
    The Fisher information matrix $I = J^\top W J$ is a $2 \times 2$ positive semi-definite matrix. Its eigenvalues $\lambda_{\max}$ and $\lambda_{\min}$ (not to be confused with the Hull-White parameter $\lambda$) and corresponding eigenvectors describe the curvature of the objective function near the optimum.

    **Geometric interpretation of large $\kappa(I)$**: The contours of the objective function $f(\lambda, \sigma) = \text{const}$ near the optimum are approximately ellipses. The eigenvalues of $I$ determine the curvature along the principal axes:

    - The eigenvector corresponding to $\lambda_{\max}$ points in the direction of greatest curvature --- the objective function increases rapidly in this direction. The parameters are tightly constrained along this axis.
    - The eigenvector corresponding to $\lambda_{\min}$ points in the direction of least curvature --- the objective function increases slowly. The parameters are poorly constrained along this axis.

    When $\kappa = \lambda_{\max}/\lambda_{\min} \gg 1$, the elliptical contours are highly elongated: very narrow in the $\lambda_{\max}$ direction and very wide in the $\lambda_{\min}$ direction. This produces a long, narrow valley in the objective function landscape.

    The contour plot would show: at the center, the minimum; surrounding it, thin elongated ellipses with the long axis oriented along the poorly-identified parameter direction (typically close to the $\lambda$ axis). Moving along the long axis barely changes the objective value, meaning the optimizer can wander significantly in that direction without increasing the error. This is the geometric manifestation of poor identifiability: many parameter values along the valley floor produce nearly identical model prices.

    For the Hull-White calibration, the long axis of the valley typically aligns with the $\lambda$ direction (or a $\lambda$-dominated linear combination of $\lambda$ and $\sigma$), reflecting the fact that $\lambda$ is less well-identified than $\sigma$.

---

**Exercise 3.** Explain why $\lambda$ is less well-identified than $\sigma$ from cap data. In particular, show that for short-dated caplets ($\lambda\delta_k \ll 1$), the bond price volatility $\sigma_P$ is approximately independent of $\lambda$, making those instruments uninformative about $\lambda$.

??? success "Solution to Exercise 3"
    The bond price volatility for a caplet is

    $$
    \sigma_P(T_{k-1}, T_k) = \frac{\sigma}{\lambda}(1 - e^{-\lambda\delta_k})\sqrt{\frac{1 - e^{-2\lambda T_{k-1}}}{2\lambda}}
    $$

    For short-dated caplets where $\lambda\delta_k \ll 1$, we expand the first factor:

    $$
    \frac{1 - e^{-\lambda\delta_k}}{\lambda} = \delta_k - \frac{\lambda\delta_k^2}{2} + \frac{\lambda^2\delta_k^3}{6} - \cdots \approx \delta_k\left(1 - \frac{\lambda\delta_k}{2} + \cdots\right)
    $$

    The leading term $\delta_k$ is independent of $\lambda$, and the correction is of order $\lambda\delta_k/2$. For typical values ($\lambda = 0.05$, $\delta_k = 0.5$), the correction is only $0.05 \times 0.5/2 = 1.25\%$ of the leading term.

    Similarly, if $\lambda T_{k-1}$ is also small (short-maturity caplets):

    $$
    \frac{1 - e^{-2\lambda T_{k-1}}}{2\lambda} \approx T_{k-1}\left(1 - \lambda T_{k-1} + \cdots\right)
    $$

    Combining, for short-dated caplets:

    $$
    \sigma_P \approx \sigma \cdot \delta_k \cdot \sqrt{T_{k-1}}
    $$

    which is independent of $\lambda$. The implied caplet volatility $\sigma_k^{\text{HW}} \propto \sigma_P$ is therefore also approximately independent of $\lambda$.

    Since $\partial \sigma_k^{\text{HW}}/\partial \lambda \approx 0$ for short-dated caplets, these instruments provide essentially no information about $\lambda$. The Jacobian row for a short-dated caplet has the form $({\approx}0, \;\partial\sigma_k/\partial\sigma)$, pointing almost entirely in the $\sigma$-direction. Only long-dated caplets, where $(1-e^{-\lambda\delta_k})/\lambda$ deviates significantly from $\delta_k$, provide meaningful sensitivity to $\lambda$.

    In contrast, $\sigma$ is well-identified because $\sigma_P$ is exactly proportional to $\sigma$ (for any fixed $\lambda$), so $\partial \sigma_k^{\text{HW}}/\partial \sigma > 0$ for all maturities. The overall level of the caplet volatility curve immediately determines $\sigma$.

---

**Exercise 4.** Tikhonov regularization adds the penalty $\mu_\lambda(\lambda - \lambda_{\text{prior}})^2 + \mu_\sigma(\sigma - \sigma_{\text{prior}})^2$ to the objective. Derive the regularized first-order conditions and show that the regularized solution is a weighted average of the unconstrained optimum and the prior, with weights determined by $\mu$.

??? success "Solution to Exercise 4"
    The regularized objective is

    $$
    F(\lambda, \sigma) = f(\lambda, \sigma) + \mu_\lambda(\lambda - \lambda_{\text{prior}})^2 + \mu_\sigma(\sigma - \sigma_{\text{prior}})^2
    $$

    The first-order conditions are:

    $$
    \frac{\partial F}{\partial \lambda} = \frac{\partial f}{\partial \lambda} + 2\mu_\lambda(\lambda - \lambda_{\text{prior}}) = 0
    $$

    $$
    \frac{\partial F}{\partial \sigma} = \frac{\partial f}{\partial \sigma} + 2\mu_\sigma(\sigma - \sigma_{\text{prior}}) = 0
    $$

    Let $(\lambda_{\text{unc}}, \sigma_{\text{unc}})$ denote the unconstrained optimum where $\partial f/\partial \lambda = \partial f/\partial \sigma = 0$. Locally approximating $f$ as quadratic near $(\lambda_{\text{unc}}, \sigma_{\text{unc}})$:

    $$
    f(\lambda, \sigma) \approx f_0 + \frac{1}{2}H_{\lambda\lambda}(\lambda - \lambda_{\text{unc}})^2 + \frac{1}{2}H_{\sigma\sigma}(\sigma - \sigma_{\text{unc}})^2 + H_{\lambda\sigma}(\lambda - \lambda_{\text{unc}})(\sigma - \sigma_{\text{unc}})
    $$

    where $H$ is the Hessian of $f$. Ignoring the cross term for simplicity ($H_{\lambda\sigma} = 0$), the first-order conditions become:

    $$
    H_{\lambda\lambda}(\lambda^* - \lambda_{\text{unc}}) + 2\mu_\lambda(\lambda^* - \lambda_{\text{prior}}) = 0
    $$

    Solving:

    $$
    \lambda^* = \frac{H_{\lambda\lambda}\,\lambda_{\text{unc}} + 2\mu_\lambda\,\lambda_{\text{prior}}}{H_{\lambda\lambda} + 2\mu_\lambda}
    $$

    This is a weighted average of the unconstrained optimum $\lambda_{\text{unc}}$ and the prior $\lambda_{\text{prior}}$:

    $$
    \lambda^* = \underbrace{\frac{H_{\lambda\lambda}}{H_{\lambda\lambda} + 2\mu_\lambda}}_{w_{\text{data}}}\,\lambda_{\text{unc}} + \underbrace{\frac{2\mu_\lambda}{H_{\lambda\lambda} + 2\mu_\lambda}}_{w_{\text{prior}}}\,\lambda_{\text{prior}}
    $$

    The weights $w_{\text{data}} + w_{\text{prior}} = 1$ are determined by the ratio of the data curvature $H_{\lambda\lambda}$ to the regularization strength $2\mu_\lambda$:

    - When $\mu_\lambda \to 0$: $w_{\text{data}} \to 1$, and $\lambda^* \to \lambda_{\text{unc}}$ (no regularization effect)
    - When $\mu_\lambda \to \infty$: $w_{\text{prior}} \to 1$, and $\lambda^* \to \lambda_{\text{prior}}$ (parameter frozen at prior)
    - When $\mu_\lambda = H_{\lambda\lambda}/2$: equal weight to data and prior

    The same analysis applies to $\sigma^*$ with $H_{\sigma\sigma}$ and $\mu_\sigma$. The regularized solution shrinks each parameter toward its prior value, with the amount of shrinkage determined by the ratio of regularization strength to data informativeness (Hessian curvature).

---

**Exercise 5.** Describe the L-curve method for choosing the regularization strength $\mu$. Plot schematically the regularization penalty versus the data-fit residual as $\mu$ varies from $0$ to $\infty$. Where is the optimal $\mu$ located on this curve, and why?

??? success "Solution to Exercise 5"
    **The L-curve method** plots two quantities as the regularization strength $\mu$ varies:

    - Horizontal axis: the data-fit residual $\|f(\lambda^*(\mu), \sigma^*(\mu))\|$ (how well the model fits the market data)
    - Vertical axis: the regularization penalty $\|(\lambda^*(\mu) - \lambda_{\text{prior}}, \sigma^*(\mu) - \sigma_{\text{prior}})\|$ (how far the parameters deviate from the prior)

    **Schematic behavior:**

    - At $\mu = 0$ (no regularization): The data-fit residual is minimized (bottom of the horizontal axis), but the regularization penalty is large because the parameters are free to move far from the prior.
    - At $\mu \to \infty$ (infinite regularization): The parameters are frozen at the prior, so the regularization penalty is zero (bottom of the vertical axis), but the data-fit residual is large because the model cannot adapt to the current market.
    - For intermediate $\mu$: The curve traces an L-shape (when plotted on log-log scale), with the vertical part (large $\mu$, penalty decreasing rapidly) connecting to the horizontal part (small $\mu$, residual decreasing rapidly).

    **Optimal $\mu$**: Located at the "elbow" of the L-curve, where the curve has maximum curvature. At this point:

    - Reducing $\mu$ further (moving right along the curve) would decrease the data-fit residual only slightly but increase the penalty substantially (parameters start to become noisy)
    - Increasing $\mu$ further (moving up along the curve) would decrease the penalty only slightly but increase the residual substantially (parameters become too rigid)

    The elbow represents the optimal bias-variance trade-off: the parameters are as close to the prior as possible (stable) while still fitting the market data adequately. Numerically, the elbow can be found by maximizing the curvature of the L-curve, or by locating the point where the second derivative of the curve (parameterized by $\mu$) changes sign.

---

**Exercise 6.** In the two-factor model, swapping $(\lambda_1, \sigma_1) \leftrightarrow (\lambda_2, \sigma_2)$ gives the same model. Explain why this label symmetry creates identifiability problems. How does the convention $\lambda_1 < \lambda_2$ resolve the issue, and what constraint would you impose in the optimizer?

??? success "Solution to Exercise 6"
    In the two-factor Hull-White model, the short rate is $r(t) = x_1(t) + x_2(t) + \varphi(t)$ where each factor satisfies $dx_i = -\lambda_i x_i\,dt + \sigma_i\,dW_i$ with $\langle dW_1, dW_2\rangle = \rho\,dt$. The model is parameterized by $(\lambda_1, \sigma_1, \lambda_2, \sigma_2, \rho)$.

    **Label symmetry**: Swapping $(\lambda_1, \sigma_1) \leftrightarrow (\lambda_2, \sigma_2)$ (and swapping $W_1 \leftrightarrow W_2$) produces the exact same model. The sum $r(t) = x_1(t) + x_2(t) + \varphi(t)$ is symmetric in the two factors. All observable quantities (bond prices, option prices, yield curve dynamics) are invariant under this swap.

    **Identifiability problem**: This symmetry means that for every parameter set $(\lambda_1, \sigma_1, \lambda_2, \sigma_2, \rho)$, there exists a second parameter set $(\lambda_2, \sigma_2, \lambda_1, \sigma_1, \rho)$ that produces identical model outputs. The mapping from parameters to observables is 2-to-1, violating injectivity. The optimizer may oscillate between these two equivalent solutions, or converge to one arbitrarily, creating apparent instability when comparing calibrations across different days or starting points.

    **Resolution via the convention $\lambda_1 < \lambda_2$**: This breaks the symmetry by assigning a label to each factor:

    - Factor 1 (slow-reverting, $\lambda_1$ small): Drives long-term yield curve movements
    - Factor 2 (fast-reverting, $\lambda_2$ large): Drives short-term, transient rate dynamics

    **Implementation in the optimizer**: Impose the constraint $\lambda_1 < \lambda_2$ (or equivalently $\lambda_1 \leq \lambda_2$) directly in the optimization. Using L-BFGS-B or a similar bounded optimizer, set the constraint as:

    $$
    0 < \lambda_1 \leq \lambda_2
    $$

    Alternatively, reparameterize as $\lambda_1 = \ell_1$ and $\lambda_2 = \ell_1 + \exp(\ell_2)$ where $\ell_1, \ell_2$ are unconstrained, which automatically enforces $\lambda_2 > \lambda_1$. This eliminates the symmetry and ensures the optimizer converges to a unique, consistently-labeled solution.

---

**Exercise 7.** Temporal smoothing jointly optimizes parameters across multiple days with the penalty $\mu\sum_{t=2}^T[(\lambda_t - \lambda_{t-1})^2 + (\sigma_t - \sigma_{t-1})^2]$. Discuss the trade-offs of this approach: what happens when $\mu$ is too large? Too small? How does the computational cost scale with the number of days $T$?

??? success "Solution to Exercise 7"
    **Temporal smoothing** jointly optimizes $(\lambda_1, \sigma_1, \ldots, \lambda_T, \sigma_T)$ by minimizing

    $$
    \sum_{t=1}^{T} f_t(\lambda_t, \sigma_t) + \mu \sum_{t=2}^{T}\left[(\lambda_t - \lambda_{t-1})^2 + (\sigma_t - \sigma_{t-1})^2\right]
    $$

    **When $\mu$ is too large**: The penalty term dominates, forcing $\lambda_t \approx \lambda_{t-1}$ and $\sigma_t \approx \sigma_{t-1}$ for all $t$. In the extreme, all parameters are nearly identical: $\lambda_1 \approx \lambda_2 \approx \cdots \approx \lambda_T$. The model becomes unresponsive to genuine market regime changes. If the market experiences a structural shift (e.g., a central bank policy change that alters the mean-reversion of rates), the smoothed parameters adapt too slowly, leading to persistent mispricing. The parameter path has low variance (stable) but high bias (lagging the market).

    **When $\mu$ is too small**: The smoothing penalty is negligible, and each day's parameters are determined independently by $f_t$ alone (equivalent to daily recalibration without regularization). The parameter path is noisy, with $\lambda_t$ jumping from day to day due to amplification of small market data perturbations. The path has low bias (tracks the market closely) but high variance (noisy, causing hedging instability).

    **Optimal $\mu$**: Balances the bias-variance trade-off. The parameters respond to sustained market trends but filter out day-to-day noise.

    **Computational cost**: The optimization has $2T$ decision variables ($\lambda_t$ and $\sigma_t$ for each day). The objective function requires $T$ separate calibration evaluations (one per day), each involving pricing multiple instruments. The smoothing penalty adds $O(T)$ quadratic terms, which are cheap to evaluate.

    - **Evaluation cost**: $O(T \times n)$ where $n$ is the number of instruments per day
    - **Gradient cost**: The smoothing penalty couples adjacent days, creating a banded structure in the Hessian (each $(\lambda_t, \sigma_t)$ interacts only with $(\lambda_{t-1}, \sigma_{t-1})$ and $(\lambda_{t+1}, \sigma_{t+1})$). Exploiting this banded structure, gradient computation is $O(T)$.
    - **Total optimization cost**: Scales linearly in $T$ per iteration if the banded structure is exploited, but the number of iterations may increase with $T$. For large $T$ (e.g., 250 trading days per year, multi-year histories), the problem can become expensive, motivating sliding-window approaches where only the most recent $T_{\text{window}}$ days are jointly optimized.

    In practice, the sliding-window variant with $T_{\text{window}} = 20$--60 trading days is common, providing sufficient smoothing without the full computational burden of the global problem.
