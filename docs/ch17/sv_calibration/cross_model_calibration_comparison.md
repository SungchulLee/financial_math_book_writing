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

---

## Exercises

**Exercise 1.** The Heston model has 5 parameters while SABR (with fixed $\beta$) has 3. Discuss how the difference in parameter count affects: (a) the ability to fit the implied volatility surface, (b) the stability of calibrated parameters over time, and (c) the risk of overfitting. Under what conditions might fewer parameters be an advantage?

---

**Exercise 2.** Local volatility is extracted from the Dupire formula and provides an exact fit to all quoted vanilla options. Despite this, it is widely acknowledged to have poor extrapolation properties. Explain why an exact fit to vanillas does not guarantee accurate pricing of barrier options. What specific dynamic property does local vol get wrong compared to stochastic volatility models?

---

**Exercise 3.** A practitioner calibrates Heston, SABR, and local vol to the same set of 50 SPX options. The Heston model has RMSE of 0.35 vol points, SABR has 0.15 vol points, and local vol has 0.00 (exact). A down-and-out put is then priced under each model, yielding prices of 2.15, 1.98, and 2.72 respectively. Discuss the dispersion of exotic prices in light of the vanilla fit quality. Why does better vanilla fit not imply more reliable exotic pricing?

---

**Exercise 4.** Describe how to approximately map Heston parameters $(\kappa, \bar{v}, \sigma_v, \rho, v_0)$ to SABR parameters $(\alpha, \beta, \rho_{\text{SABR}}, \nu)$ at a single maturity. What quantities (ATM vol, skew, curvature) constrain this mapping? Why is the mapping only approximate and maturity-dependent?

---

**Exercise 5.** The practical calibration pipeline suggests: "Start with SABR for speed, validate with Heston for dynamics, use local vol for exotic pricing." Critique this pipeline. In what market regime might this ordering be suboptimal? Propose an alternative pipeline for pricing long-dated autocallable notes.

---

**Exercise 6.** An ensemble approach averages prices across models: $\hat{P} = w_1 P_{\text{Heston}} + w_2 P_{\text{SABR}} + w_3 P_{\text{LV}}$. Discuss how to choose the weights $w_i$. Should they depend on the product being priced? On the calibration fit quality? On historical backtesting performance? Propose a specific weighting scheme and justify it.
