# Calibration Instability

Model calibration to market data is essential for practical implementation, but instability in calibration results poses a fundamental challenge. Sensitivity to input data, parameter coupling, and local minima in optimization create risks of model parameter uncertainty that propagate to pricing and hedging errors.

## Key Concepts

**Sources of Instability**

1. **Non-uniqueness**: Multiple parameter sets fit equally well
2. **Sensitivity to inputs**: Small changes in option prices cause large parameter shifts
3. **Correlation between parameters**: Some parameters compensate for others
4. **Optimization landscape**: Multiple local minima complicate finding global optimum

**Local Volatility Calibration Instability**
Local volatility models $\sigma_{\text{LV}}(S, t)$ are calibrated to match all observed option prices:

$$C^{\text{LV}}(S_0, K, T; \sigma_{\text{LV}}) = C^{\text{Market}}(K, T)$$

Instability arises from:

- **Ill-posed inverse problem**: High-frequency oscillations in $\sigma_{\text{LV}}(S, t)$ can match prices equally well
- **Sensitivity to boundaries**: Extrapolation beyond quoted strikes exhibits explosive behavior
- **Input noise**: Small bid-ask bounce in option prices causes large volatility surface jumps
- **Sparse data**: Few quotes at extreme strikes/maturities force extrapolation

**Heston Model Calibration Issues**
The Heston model has 5 parameters: $v_0, \kappa, \theta, \sigma_v, \rho$

Common instabilities:

- **Flat boundaries**: Parameters at $\rho = -1$ or $\rho = 1$ cause numerical problems
- **Parameter swapping**: Similar fits possible with different $(\kappa, \theta)$ combinations
- **Unrealistic long-run variance**: Calibration to short-dated smiles extrapolates poorly
- **Jump-diffusion ambiguity**: Stochastic vol vs. jumps both produce smiles

**Sensitivity Analysis Approaches**
Quantify stability through:

1. **Hessian condition number**: measures parameter coupling strength
2. **Bootstrap resampling**: calibrate to perturbed option prices
3. **Cross-validation**: calibrate to subset, test on holdout data
4. **Parameter confidence intervals**: via optimization landscape perturbation

**Practical Mitigation Strategies**

- **Regularization**: penalize oscillatory $\sigma_{\text{LV}}$ surfaces via smoothness priors
- **Multi-stage calibration**: fit liquid instruments first (ATM volatility), then less liquid
- **Parameter anchoring**: constrain parameters to realistic ranges from historical data
- **Ensemble methods**: average across multiple stable solutions
- **Daily recalibration with incremental adjustment**: use previous day's parameters as initialization

!!! warning "Risk Management Implication"
    Unstable calibration implies:

    - Parameter uncertainty creates model risk beyond what pricing accuracy suggests
    - Hedge ratios (Greeks) are sensitive to which local minimum is selected
    - P&L attributed to calibration drift (not data/market moves) can be significant
    - Validate models out-of-sample before deploying in production

---

## Exercises

**Exercise 1.** Explain why the local volatility calibration problem is ill-posed. Specifically, why can high-frequency oscillations in $\sigma_{\text{loc}}(S, t)$ produce call prices that are nearly identical to those of a smooth local volatility surface?

??? success "Solution to Exercise 1"
    The local volatility calibration problem is ill-posed because the mapping from the local volatility surface $\sigma_{\text{loc}}(S, t)$ to European call prices $C(K, T)$ involves integration (via the Fokker-Planck or Dupire PDE). Integration is a smoothing operation: it averages the local volatility function over paths, so high-frequency oscillations in $\sigma_{\text{loc}}(S, t)$ are damped when computing option prices. Two surfaces that differ by high-frequency oscillations can produce call prices that are nearly identical within the bid-ask spread. Formally, the inverse problem of recovering $\sigma_{\text{loc}}$ from $C$ requires differentiation (Dupire's formula involves $\partial_T C$ and $\partial_{KK} C$), and differentiation amplifies noise. This is a hallmark of ill-posedness: small perturbations in the data (option prices) map to large perturbations in the solution (local volatility), and the solution is not unique unless a regularization condition is imposed.

---

**Exercise 2.** A Tikhonov regularization penalty adds a term $\lambda \int |\nabla \sigma_{\text{loc}}|^2 \, dS \, dt$ to the calibration objective. (a) What is the effect of increasing $\lambda$? (b) What happens if $\lambda = 0$? (c) How should $\lambda$ be chosen in practice?

??? success "Solution to Exercise 2"
    **(a)** Increasing $\lambda$ strengthens the smoothness penalty, forcing the calibrated local volatility surface to be smoother. High-frequency oscillations are suppressed because they contribute a large gradient term $|\nabla \sigma_{\text{loc}}|^2$. The trade-off is that a very large $\lambda$ over-smoothes the surface, degrading the fit to observed option prices.

    **(b)** If $\lambda = 0$, there is no regularization. The calibration problem is purely ill-posed: the optimizer is free to produce wildly oscillatory surfaces that fit option prices within numerical tolerance but are economically meaningless and unstable from day to day.

    **(c)** In practice, $\lambda$ is chosen by cross-validation or the L-curve method. Cross-validation holds out a subset of option prices during calibration and selects $\lambda$ to minimize the out-of-sample pricing error. The L-curve method plots the calibration residual versus the regularization norm and picks the $\lambda$ at the "elbow" where increasing smoothness no longer significantly worsens the fit. The goal is to find the $\lambda$ that balances fidelity to market data against surface stability.

---

**Exercise 3.** Two calibrations of a local volatility model on consecutive days produce very different surfaces even though option prices changed by less than 0.5%. Identify three possible sources of this instability and propose a mitigation strategy for each.

??? success "Solution to Exercise 3"
    Three possible sources:

    1. **Bid-ask noise in inputs.** Even though mid-market option prices changed by less than 0.5%, the individual quotes used for calibration may have shifted within their bid-ask spreads. Because the inverse problem is ill-posed, small changes in input prices are amplified into large local volatility surface movements. **Mitigation**: Use Tikhonov regularization to penalize surface roughness, and smooth input option prices before calibration.

    2. **Different local minimum selected.** The optimization landscape has multiple local minima. On consecutive days, the optimizer may converge to different minima due to different starting points or small changes in the objective. **Mitigation**: Use the previous day's calibrated surface as the initial guess (warm-start), so the optimizer remains in the same basin of attraction, and add a penalty term $\lambda_2 \|\sigma_{\text{loc}}^{\text{new}} - \sigma_{\text{loc}}^{\text{prev}}\|^2$ to discourage large day-to-day jumps.

    3. **Boundary/extrapolation instability.** At extreme strikes or long maturities where data is sparse, the surface is driven by extrapolation assumptions that can shift unpredictably. **Mitigation**: Anchor boundary conditions using structural constraints (e.g., asymptotic SVI parameterization of the wings) and restrict the calibration domain to the region covered by liquid quotes.

---

**Exercise 4.** In the Heston model, the parameters $\xi$ (vol-of-vol) and $\rho$ (correlation) are highly correlated in the sense that increasing $\xi$ while adjusting $\rho$ can produce nearly the same implied volatility surface. Explain why this parameter degeneracy causes calibration instability. How can the calibration be made more robust?

??? success "Solution to Exercise 4"
    The parameter degeneracy between $\xi$ (vol-of-vol) and $\rho$ (spot-vol correlation) arises because both parameters affect the implied volatility skew in similar ways. Increasing $\xi$ steepens the smile wings, but adjusting $\rho$ more negatively also steepens the skew. A higher $\xi$ with a less negative $\rho$ can produce nearly the same smile shape as a lower $\xi$ with a more negative $\rho$. This creates a ridge in the objective function: the minimum is not a well-isolated point but rather an elongated valley, so small perturbations in input data shift the optimizer along the ridge, producing large parameter jumps with minimal change in the objective value.

    To make calibration more robust, practitioners can: (1) add a regularization penalty that constrains parameters to remain near historically estimated values, (2) calibrate to instruments with different sensitivities to $\xi$ and $\rho$ (e.g., variance swaps are sensitive to $\xi$ but not $\rho$, while risk reversals are sensitive to $\rho$), and (3) fix one parameter (e.g., $\rho$ from historical spot-vol regression) and calibrate only the remaining parameters, breaking the degeneracy.

---

**Exercise 5.** A calibration procedure uses 50 option prices spanning 5 maturities and 10 strikes. The local volatility surface is represented on a 100 x 50 grid. Why does the dimensionality mismatch (5000 unknowns vs. 50 constraints) lead to non-uniqueness? How does regularization address this?

??? success "Solution to Exercise 5"
    The local volatility surface on a 100 x 50 grid has 5000 unknowns, but there are only 50 option price constraints. This is a severely underdetermined system with infinitely many solutions: any surface that satisfies the 50 price equations at the observed strikes and maturities is a valid calibration, regardless of its behavior at non-observed grid points. The 4950-dimensional null space of the problem allows high-frequency oscillations, spikes, and other artifacts that satisfy the constraints but are economically meaningless.

    Regularization addresses this by adding additional constraints that reduce the effective dimensionality of the solution space. A smoothness penalty $\lambda \int |\nabla \sigma_{\text{loc}}|^2 \, dS \, dt$ effectively eliminates high-frequency components, collapsing the null space and selecting the smoothest surface consistent with the data. This converts the underdetermined problem into a well-posed one with a unique solution (for each $\lambda$), at the cost of introducing a bias toward smooth surfaces.

---

**Exercise 6.** Compare the calibration stability of local volatility, Heston, and SABR models. For each, identify the main source of instability (ill-posedness, parameter coupling, or optimization landscape) and describe how practitioners typically handle it.

??? success "Solution to Exercise 6"
    **Local volatility.** The main source of instability is *ill-posedness*: the inverse problem from option prices to the local volatility surface is inherently ill-conditioned. Practitioners handle this with Tikhonov regularization (smoothness penalties), careful interpolation of the implied volatility surface before applying Dupire's formula, and restricting the calibration to the domain of liquid quotes.

    **Heston.** The main source is *parameter coupling*: the five parameters ($v_0$, $\kappa$, $\theta$, $\xi$, $\rho$) are correlated in their effect on the smile, creating ridges and near-flat directions in the objective function. Practitioners handle this with multi-stage calibration (fit $v_0$ and $\rho$ from short-dated ATM vol and skew, then fit $\kappa$ and $\theta$ from the term structure, and finally $\xi$ from smile curvature), parameter bounds from historical estimation, and global optimization methods (differential evolution, simulated annealing).

    **SABR.** The main source is *optimization landscape* complexity, particularly the sensitivity of the backbone parameter $\beta$ and the difficulty in separating $\alpha$ (initial vol) from $\nu$ (vol-of-vol) in short-dated smiles. Practitioners typically fix $\beta$ (e.g., $\beta = 0.5$ for rates), use the Hagan asymptotic formula for fast calibration of the remaining parameters, and impose consistency across maturities via a parameterized term structure of $\alpha(T)$, $\rho(T)$, $\nu(T)$.

---

**Exercise 7.** A desk recalibrates its local volatility model daily and observes that hedging P&L has a component that correlates with calibration changes rather than market moves. This is called "calibration noise." (a) Explain the mechanism. (b) How does this affect the realized P&L distribution? (c) Propose a filtering approach to reduce calibration noise.

??? success "Solution to Exercise 7"
    **(a) Mechanism.** Each day's recalibration produces a slightly different local volatility surface due to input noise, different local minima, or extrapolation changes. The new surface implies different Greeks (especially delta and vega), so the desk's hedge ratios change. The P&L from rebalancing includes a component driven not by actual market moves but by the change in model parameters. For example, if the local volatility surface shifts at a barrier level, the model-implied delta changes, triggering a hedge rebalance whose P&L reflects the calibration change rather than a genuine market risk factor.

    **(b) Effect on P&L distribution.** Calibration noise adds a zero-mean (approximately) but positive-variance component to the daily P&L. This inflates the realized P&L volatility beyond what genuine market risk explains, worsening the Sharpe ratio of the hedged book. It can also create spurious autocorrelation in P&L (since calibration drifts can persist over several days) and fatten the tails of the P&L distribution.

    **(c) Filtering approach.** Apply an exponential moving average or Kalman filter to the calibrated local volatility surface: instead of using each day's raw calibration $\sigma_{\text{loc}}^{\text{raw}}(S, t)$, use the filtered surface

    $$
    \sigma_{\text{loc}}^{\text{filtered}}(S, t) = \lambda \, \sigma_{\text{loc}}^{\text{raw}}(S, t) + (1 - \lambda) \, \sigma_{\text{loc}}^{\text{prev}}(S, t)
    $$

    with $\lambda \in (0, 1)$ controlling the responsiveness. A small $\lambda$ (e.g., 0.2--0.4) heavily smooths calibration noise at the cost of slower adaptation to genuine market regime changes. Alternatively, use a penalty term in the calibration objective that penalizes deviations from the previous day's surface, achieving a similar effect within the optimization itself.
