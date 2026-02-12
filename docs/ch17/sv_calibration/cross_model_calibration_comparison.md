# Cross-Model Calibration Comparison

Different stochastic volatility models—Heston, SABR, and local volatility—provide alternative parameterizations of the same market implied volatility surface. Comparing calibration results across models reveals strengths, weaknesses, and complementary insights about market structure and model assumptions.

## Key Concepts

**Heston Model Calibration**
The Heston SDE:
$$dS_t = \mu S_t dt + \sqrt{v_t} S_t dB_t^S$$
$$dv_t = \kappa(\theta - v_t) dt + \sigma_v \sqrt{v_t} dB_t^v$$

Calibration targets entire option surface with 5 parameters. Strengths:
- Analytical or semi-analytical formulas (Fourier inversion)
- Mean-reversion parameter captures volatility persistence
- Correlation parameter captures skew

Weaknesses:
- Parameter instability, especially for mean-reversion
- Limited fitting at far OTM strikes
- Assumption of constant parameters over time

**SABR Model Calibration**
The SABR SDE (for forward $F$):
$$dF_t = \alpha_t (F_t)^{\beta} dB_t^F$$
$$d\alpha_t = \nu \alpha_t dB_t^{\alpha}$$

Hagan's closed-form approximation enables rapid calibration. Strengths:
- Simple, intuitive 4 parameters
- Excellent fitting to smile/skew near ATM
- Natural for interest rate derivatives
- Avoids numerical PDE solving

Weaknesses:
- Less accurate at far OTM strikes
- Limited ability to fit volatility term structure
- Empirical nature of Hagan formula

**Local Volatility Calibration**
Dupire's local volatility:
$$\sigma_{\text{LV}}(S, t)^2 = \frac{\partial C/\partial T + rK\partial C/\partial K}{(1/2)K^2 \partial^2 C/\partial K^2}$$

Strengths:
- Exact fit to all quoted options by construction
- No parameters—deterministic volatility function
- Enables Monte Carlo pricing of exotic options

Weaknesses:
- Extreme extrapolation behavior (explosion near boundaries)
- No term structure in volatility unless separately parameterized
- Lacks mean-reversion, predicts increasing smile over time

**Comparison Results**

| Aspect | Heston | SABR | Local Vol |
|--------|--------|------|-----------|
| ATM Fit | Good | Excellent | Perfect |
| Smile Fit | Good | Excellent | Perfect |
| Term Structure | Moderate | Moderate | Limited |
| Far OTM | Fair | Fair | Unreliable |
| Computational Speed | Medium | Fast | Fast |
| Parameter Stability | Challenging | Good | N/A |
| Extrapolation | Reasonable | Moderate | Poor |

**Cross-Model Insights**
1. **Complementary strengths**: Different models excel in different regimes
2. **Parameter mapping**: Heston/SABR parameters can be approximately mapped to each other
3. **Consensus forecasts**: Ensemble methods averaging predictions reduce model-specific biases
4. **Market regime identification**: Model fit quality indicates market structure changes

**Practical Calibration Pipeline**
1. Start with SABR for speed and stability
2. Validate with Heston for dynamics and path-dependence
3. Use local vol for exotic payoff pricing
4. Compare Greeks across models for robustness
5. Select model based on product type and market regime

!!! note "Integration Strategy"
    Best practices combine models:
    - SABR for liquid, standard products
    - Heston for path-dependent exotics and long-dated instruments
    - Local vol as reality check for exotic pricing
    - Monitor cross-model P&L attribution to identify regime changes
