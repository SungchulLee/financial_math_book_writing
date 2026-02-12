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
