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

---

**Exercise 2.** A Tikhonov regularization penalty adds a term $\lambda \int |\nabla \sigma_{\text{loc}}|^2 \, dS \, dt$ to the calibration objective. (a) What is the effect of increasing $\lambda$? (b) What happens if $\lambda = 0$? (c) How should $\lambda$ be chosen in practice?

---

**Exercise 3.** Two calibrations of a local volatility model on consecutive days produce very different surfaces even though option prices changed by less than 0.5%. Identify three possible sources of this instability and propose a mitigation strategy for each.

---

**Exercise 4.** In the Heston model, the parameters $\xi$ (vol-of-vol) and $\rho$ (correlation) are highly correlated in the sense that increasing $\xi$ while adjusting $\rho$ can produce nearly the same implied volatility surface. Explain why this parameter degeneracy causes calibration instability. How can the calibration be made more robust?

---

**Exercise 5.** A calibration procedure uses 50 option prices spanning 5 maturities and 10 strikes. The local volatility surface is represented on a 100 x 50 grid. Why does the dimensionality mismatch (5000 unknowns vs. 50 constraints) lead to non-uniqueness? How does regularization address this?

---

**Exercise 6.** Compare the calibration stability of local volatility, Heston, and SABR models. For each, identify the main source of instability (ill-posedness, parameter coupling, or optimization landscape) and describe how practitioners typically handle it.

---

**Exercise 7.** A desk recalibrates its local volatility model daily and observes that hedging P&L has a component that correlates with calibration changes rather than market moves. This is called "calibration noise." (a) Explain the mechanism. (b) How does this affect the realized P&L distribution? (c) Propose a filtering approach to reduce calibration noise.
