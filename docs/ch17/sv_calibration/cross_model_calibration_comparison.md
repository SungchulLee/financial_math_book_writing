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

??? success "Solution to Exercise 1"
    **(a) Ability to fit the implied volatility surface.**
    The Heston model's 5 parameters $(v_0, \kappa, \theta, \sigma_v, \rho)$ provide more degrees of freedom to match features of the implied volatility surface across both strikes and maturities. The additional parameters $\kappa$ and $\theta$ allow the model to capture the term structure of implied volatility (how the smile evolves with maturity), while $\sigma_v$ and $\rho$ jointly control the smile shape and skew. SABR with fixed $\beta$ has only 3 parameters $(\alpha_0, \rho, \nu)$, which suffice for fitting a single maturity smile but cannot simultaneously constrain the term structure across maturities. Consequently, Heston generally achieves a more globally consistent fit when calibrated to the full surface, while SABR excels at per-slice fitting.

    **(b) Stability of calibrated parameters over time.**
    With 5 parameters, the Heston model faces greater risk of parameter instability. The $(\kappa, \theta)$ pair is notoriously ill-conditioned: a large $\kappa$ with large $\theta$ produces nearly identical option prices to a small $\kappa$ with small $\theta$, creating a ridge in the objective landscape. Day-over-day jumps of 50--100% in $\kappa$ are common even when the underlying surface changes minimally. SABR's 3 parameters are generally more stable because the ATM formula provides a direct constraint on $\alpha_0$, and $\rho$ and $\nu$ are identified by distinct features (skew and curvature respectively). Fewer parameters mean each is better identified by the data.

    **(c) Risk of overfitting.**
    The bias-variance tradeoff is central here. With 5 parameters fitting (say) 50 market quotes, Heston has ample data relative to parameters, so classical overfitting is not the primary concern. However, parameter overfitting in a different sense is relevant: the optimizer may exploit parameter combinations that fit today's surface well but represent unstable, non-physical configurations. This manifests as poor out-of-sample performance (e.g., unreliable Greeks or exotic prices). SABR's 3 parameters are less prone to this because the reduced flexibility limits the model's ability to "chase" noise in the market data.

    **When fewer parameters are an advantage.** Fewer parameters are preferable when: (i) the calibration target is a single maturity slice (SABR's natural domain), (ii) parameter stability is critical for hedging (stable parameters produce stable Greeks), (iii) the calibration must be performed very frequently (speed), or (iv) the data is sparse (few quoted strikes), where a richer model would overfit the limited information.

---

**Exercise 2.** Local volatility is extracted from the Dupire formula and provides an exact fit to all quoted vanilla options. Despite this, it is widely acknowledged to have poor extrapolation properties. Explain why an exact fit to vanillas does not guarantee accurate pricing of barrier options. What specific dynamic property does local vol get wrong compared to stochastic volatility models?

??? success "Solution to Exercise 2"
    Local volatility provides an exact fit to all quoted vanilla European options because the Dupire formula

    $$
    \sigma_{\text{LV}}(K, T)^2 = \frac{\partial C/\partial T + (r - q)K \, \partial C/\partial K + qC}{\frac{1}{2}K^2 \, \partial^2 C/\partial K^2}
    $$

    is constructed to reproduce the market's marginal distributions of $S_T$ at every maturity $T$. By Breeden-Litzenberger, European option prices determine the risk-neutral density $p(S_T)$ for each $T$, and local volatility is the unique diffusion model consistent with these densities.

    However, barrier options and other path-dependent derivatives depend not only on the marginal distributions but on the **joint distribution** of $(S_{t_1}, S_{t_2}, \ldots)$ at multiple times -- that is, on the full transition dynamics of the process. Two models can agree on all marginal distributions yet produce different barrier prices because the conditional distributions $p(S_{t_2} | S_{t_1})$ differ.

    The specific dynamic property that local volatility gets wrong is the **forward smile dynamics**. In local volatility models, the conditional (forward-starting) implied volatility smile flattens as time progresses. This means local vol predicts that if the spot moves to a new level, the smile will flatten out -- the model effectively predicts decreasing smile amplitude over time.

    In contrast, stochastic volatility models (like Heston) predict that the smile persists or even steepens as spot moves, because the stochastic variance process maintains randomness in future volatility regardless of the spot level. Empirically, market smiles are roughly "sticky" -- they do not flatten as rapidly as local vol predicts.

    For a down-and-out barrier option, this distinction is critical. The barrier payoff depends heavily on the probability of the spot reaching the barrier before expiry, which is determined by the transition dynamics. Local volatility, by incorrectly flattening the forward smile, typically overestimates the probability of large moves toward the barrier (for certain configurations), leading to systematically biased barrier prices. This is why traders use stochastic local volatility (SLV) models that combine both features to achieve correct marginals and more realistic dynamics.

---

**Exercise 3.** A practitioner calibrates Heston, SABR, and local vol to the same set of 50 SPX options. The Heston model has RMSE of 0.35 vol points, SABR has 0.15 vol points, and local vol has 0.00 (exact). A down-and-out put is then priced under each model, yielding prices of 2.15, 1.98, and 2.72 respectively. Discuss the dispersion of exotic prices in light of the vanilla fit quality. Why does better vanilla fit not imply more reliable exotic pricing?

??? success "Solution to Exercise 3"
    The dispersion of exotic prices (2.15, 1.98, 2.72) despite similar vanilla fit quality illustrates a fundamental principle: **vanilla options constrain marginal distributions, not path dynamics**. The three models agree (approximately) on the risk-neutral density of $S_T$ at each expiry, but disagree on the joint dynamics that determine barrier crossing probabilities.

    Consider the down-and-out put. Its price depends on:

    1. The terminal payoff $\max(K - S_T, 0)$, which is constrained by vanilla prices.
    2. The probability of the spot hitting the barrier before expiry, which depends on the full path dynamics.

    **Heston** (price = 2.15): Incorporates stochastic volatility with mean-reversion, producing specific conditional dynamics. The stochastic variance process generates fatter tails in the transition density, which affects barrier crossing probabilities.

    **SABR** (price = 1.98): Has different dynamics due to its CEV-type local volatility and log-normal stochastic volatility. The lack of mean-reversion in $\alpha_t$ gives different conditional behavior, particularly for longer-dated options.

    **Local vol** (price = 2.72): Despite perfect vanilla fit, local vol's deterministic volatility function produces systematically different transition dynamics. The "smile flattening" effect typically leads to overestimated probabilities of large moves toward the barrier, inflating the knock-out probability for certain barrier configurations or underestimating it for others. The extreme price (2.72) likely reflects local vol's poor forward dynamics.

    The key insight is that better vanilla fit does not imply more reliable exotic pricing because:

    - Vanilla options provide $m$ constraints (one per option), but the space of models consistent with these vanillas is infinite-dimensional.
    - Different models "fill in" the unconstrained degrees of freedom (transition dynamics, conditional distributions) differently.
    - Exotic prices depend on precisely those unconstrained features.
    - A model with exact vanilla fit (local vol) may have worse dynamics than a model with approximate fit (Heston) but more realistic stochastic structure.

    This is why practitioners treat the spread across model prices as a measure of **model risk** and often hedge exotics using multiple models simultaneously.

---

**Exercise 4.** Describe how to approximately map Heston parameters $(\kappa, \bar{v}, \sigma_v, \rho, v_0)$ to SABR parameters $(\alpha, \beta, \rho_{\text{SABR}}, \nu)$ at a single maturity. What quantities (ATM vol, skew, curvature) constrain this mapping? Why is the mapping only approximate and maturity-dependent?

??? success "Solution to Exercise 4"
    The approximate mapping from Heston parameters $(\kappa, \theta, \sigma_v, \rho, v_0)$ to SABR parameters $(\alpha, \beta, \rho_{\text{SABR}}, \nu)$ at a single maturity $T$ proceeds by matching observable features of the implied volatility smile.

    **Step 1: ATM volatility.** Both models must produce the same ATM implied volatility $\sigma_{\text{ATM}}$. In Heston, ATM vol is approximately

    $$
    \sigma_{\text{ATM}} \approx \sqrt{v_0 + \theta \kappa T \cdot h(\kappa, T)}
    $$

    where $h$ captures the mean-reversion dynamics. In SABR (with fixed $\beta$), ATM vol is $\sigma_{\text{ATM}} \approx \alpha_0 / F_0^{1-\beta}$ to leading order. Matching these determines $\alpha_0$.

    **Step 2: Skew (first derivative of the smile at ATM).** The ATM skew $\partial \sigma / \partial k |_{k=0}$ (where $k = \ln(K/F)$) is controlled by $\rho$ in both models. In Heston, the leading-order skew contribution is

    $$
    \text{Heston skew} \approx \frac{\rho \sigma_v}{2\sqrt{v_0}}
    $$

    In SABR, the skew is primarily controlled by $\rho_{\text{SABR}}$. Matching skews gives

    $$
    \rho_{\text{SABR}} \approx \rho_{\text{Heston}} \cdot f(\sigma_v, v_0, \nu, \alpha_0)
    $$

    where $f$ is a correction factor depending on the parameterizations.

    **Step 3: Curvature (second derivative of the smile at ATM).** The smile curvature (convexity or "butterfly") constrains $\nu$ in SABR and $\sigma_v$ in Heston. In Heston, the curvature depends on both $\sigma_v$ and $\rho^2$. In SABR, it is primarily controlled by $\nu$. Matching curvatures determines

    $$
    \nu \approx \sigma_v \cdot g(\kappa, \theta, v_0, T)
    $$

    for some function $g$ that encapsulates the mean-reversion effects.

    **Why the mapping is only approximate.** The mapping fails to be exact for several reasons:

    1. **Term structure dynamics.** Heston's mean-reversion parameter $\kappa$ governs how the smile evolves across maturities, but SABR has no analogous mechanism. At any single maturity, the effect of $\kappa$ is partially absorbed into the other parameters, but this absorption is maturity-dependent.
    2. **Higher-order smile features.** The two models produce different fourth and higher moments of the log-price distribution, leading to differences in the far wings of the smile that cannot be reconciled by matching only ATM vol, skew, and curvature.
    3. **Maturity dependence.** Heston's smile shape changes with maturity due to mean-reversion (the smile flattens for long maturities as $v_t \to \theta$), while SABR's smile shape at each maturity is independently parameterized. The Heston-to-SABR mapping therefore produces different $(\alpha, \rho_{\text{SABR}}, \nu)$ values at different maturities.
    4. **Backbone dynamics.** SABR's $\beta$ parameter has no direct Heston counterpart; it introduces a local volatility structure absent in the pure Heston model.

---

**Exercise 5.** The practical calibration pipeline suggests: "Start with SABR for speed, validate with Heston for dynamics, use local vol for exotic pricing." Critique this pipeline. In what market regime might this ordering be suboptimal? Propose an alternative pipeline for pricing long-dated autocallable notes.

??? success "Solution to Exercise 5"
    **Critique of the standard pipeline.**
    The pipeline "SABR $\to$ Heston $\to$ local vol" is reasonable for short- to medium-dated equity options where:

    - SABR provides fast initial calibration for quoting and delta hedging.
    - Heston validates the dynamics for path-dependent products.
    - Local vol enables Monte Carlo pricing of exotics with exact vanilla fit.

    However, this pipeline has several weaknesses:

    1. **SABR is not the natural choice for equities.** SABR was designed for interest rate markets. For equity options, the skew structure is dominated by the leverage effect (negative correlation), which Heston captures more naturally through $\rho$.
    2. **Local vol for exotic pricing is questionable.** As discussed in Exercise 2, local vol produces unreliable forward dynamics. Using it as the final pricing step for exotics introduces systematic bias that the pipeline was designed to avoid.
    3. **Sequential rather than integrated.** The three models are calibrated independently rather than as a unified framework. Inconsistencies between them are identified but not resolved.

    **Market regime where this ordering is suboptimal.** In a high-volatility, crisis regime (e.g., March 2020), the standard pipeline breaks down because:

    - SABR's Hagan approximation becomes inaccurate when $\nu$ is large, producing negative implied volatilities at far OTM strikes.
    - The implied volatility surface develops steep term structure features that SABR (calibrated per-slice) cannot enforce consistency across.
    - Local vol extrapolation becomes extremely unreliable with volatile market data.

    **Alternative pipeline for long-dated autocallable notes.**
    Autocallable notes have maturities of 5--10 years with periodic barrier observations, making them sensitive to both the term structure dynamics and conditional barrier crossing probabilities.

    1. **Start with Heston (or a multi-factor extension).** Heston's mean-reversion provides the term structure dynamics essential for long-dated products. Calibrate to the full surface across all maturities simultaneously. For autocallables, the inter-maturity consistency is far more important than per-slice precision.
    2. **Validate with stochastic local volatility (SLV).** Instead of pure local vol, use an SLV model that blends local volatility (exact vanilla fit) with stochastic volatility (realistic dynamics). The mixing parameter controls the trade-off.
    3. **Use SLV for exotic pricing.** Price the autocallable under SLV via Monte Carlo with barrier monitoring at each observation date. The SLV model provides both accurate vanilla calibration and more realistic barrier crossing probabilities.
    4. **Cross-check with Heston Monte Carlo.** Compare the SLV price with the Heston Monte Carlo price as a model risk diagnostic.
    5. **Skip SABR entirely.** For long-dated equity exotics, SABR adds no value over Heston and introduces an unnecessary model inconsistency.

---

**Exercise 6.** An ensemble approach averages prices across models: $\hat{P} = w_1 P_{\text{Heston}} + w_2 P_{\text{SABR}} + w_3 P_{\text{LV}}$. Discuss how to choose the weights $w_i$. Should they depend on the product being priced? On the calibration fit quality? On historical backtesting performance? Propose a specific weighting scheme and justify it.

??? success "Solution to Exercise 6"
    **Dependence on product type.** Yes, weights should absolutely depend on the product being priced. Different models have different strengths:

    - For vanilla-like payoffs, local vol (with its exact vanilla fit) should receive high weight.
    - For path-dependent payoffs (barriers, lookbacks), stochastic volatility models should be preferred because they capture forward dynamics more realistically.
    - For short-dated products, SABR may be adequate; for long-dated products, Heston's mean-reversion is essential.

    **Dependence on calibration fit quality.** Calibration fit quality is necessary but not sufficient for determining weights. Local vol always has RMSE = 0 for vanillas, but this does not make it the best model for exotics. For vanilla pricing, fit quality is directly relevant. For exotic pricing, fit quality on vanillas provides only indirect evidence of model adequacy.

    **Dependence on historical backtesting performance.** This is the most principled basis for weight selection. By backtesting each model's exotic pricing against realized payoffs (or against subsequent market prices), one can estimate the out-of-sample accuracy of each model for specific product types.

    **Proposed weighting scheme.** A two-layer scheme:

    *Layer 1 -- Product-dependent base weights.* Assign base weights based on the product category:

    - Vanillas: $w_{\text{LV}}^{(0)} = 0.6$, $w_{\text{Heston}}^{(0)} = 0.3$, $w_{\text{SABR}}^{(0)} = 0.1$
    - Barriers/path-dependent: $w_{\text{Heston}}^{(0)} = 0.5$, $w_{\text{LV}}^{(0)} = 0.2$, $w_{\text{SABR}}^{(0)} = 0.3$
    - Long-dated exotics: $w_{\text{Heston}}^{(0)} = 0.6$, $w_{\text{LV}}^{(0)} = 0.3$, $w_{\text{SABR}}^{(0)} = 0.1$

    *Layer 2 -- Performance-adjusted weights.* Adjust using exponentially weighted historical P\&L attribution. Define the model-specific hedging error over a rolling window of $N$ days:

    $$
    e_i = \frac{1}{N} \sum_{t=1}^{N} \left| P_i^{(t)} - P_{\text{realized}}^{(t)} \right|
    $$

    Then set final weights proportional to the inverse error, modulated by the base weights:

    $$
    w_i = \frac{w_i^{(0)} / e_i}{\sum_k w_k^{(0)} / e_k}
    $$

    This scheme ensures that: (i) models suited to the product type receive higher base weight, (ii) models with better recent performance are upweighted, and (iii) weights are normalized to sum to 1. The base weights provide a sensible prior when backtesting data is limited, while the performance adjustment allows the scheme to adapt to changing market regimes.
