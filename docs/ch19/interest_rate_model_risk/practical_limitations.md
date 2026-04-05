# Practical Limitations


Even well-designed interest-rate models face **practical limitations** when deployed in real trading and risk environments. Recognizing these limitations is a core aspect of model risk management.

---

## Calibration vs usage gap


Models calibrated to:
- liquid vanilla instruments

are often used to price:
- illiquid or exotic products.

Extrapolation beyond calibration data introduces uncertainty.

---

## Sensitivity to implementation choices


Results depend on:
- interpolation and smoothing methods,
- numerical solvers and discretization,
- day-count and market conventions.

These choices can dominate theoretical differences between models.

---

## Hedging limitations


Even with perfect calibration:
- hedging instruments may be illiquid,
- dynamic re-hedging assumptions fail,
- transaction costs and slippage matter.

Model-implied hedges are idealizations.

---

## Governance and controls


Effective model risk management requires:
- validation across scenarios,
- stress testing and benchmarking,
- conservative usage and reserves.

No model should be treated as “truth”.

---

## Key takeaways


- All IR models are approximations.
- Practical constraints limit theoretical optimality.
- Awareness of limitations is essential for safe use.

---

## Further reading


- Basel model risk guidance.
- Cont, *Model Uncertainty and Its Impact on Pricing*.

---

## Exercises

**Exercise 1.** A bank calibrates a SABR model to the ATM swaption surface and uses it to price a 30-year Bermudan swaption. The calibration instruments (European swaptions) have maturities up to 10 years. Discuss the sources of model risk that arise from using the model outside its calibration domain. What specific aspects of the Bermudan swaption are most sensitive to this extrapolation?

??? success "Solution to Exercise 1"

    **Sources of model risk from extrapolation beyond the calibration domain:**

    The SABR model calibrated to European swaptions up to 10 years is used to price a 30-year Bermudan swaption. Several sources of model risk arise:

    1. **Volatility term structure extrapolation:** The SABR parameters ($\alpha$, $\beta$, $\rho$, $\nu$) are calibrated to maturities up to 10 years. For the 30-year Bermudan, the model must generate volatilities for expiries between 10 and 30 years. The extrapolated parameters may not reflect the actual market dynamics at these longer horizons. The vol-of-vol $\nu$ and correlation $\rho$ are particularly sensitive to maturity, and their behavior beyond 10 years is essentially unconstrained by the calibration.

    2. **Exercise boundary dependence:** A Bermudan swaption involves an optimal exercise decision at each exercise date. This decision depends on the entire forward rate distribution at future dates, not just the marginal distributions captured by European swaptions. The SABR model, which is calibrated to marginals (European swaption prices), does not uniquely determine the joint dynamics of forward rates across time. Different models can agree on all European swaption prices but disagree on the Bermudan exercise boundary.

    3. **Correlation structure:** The Bermudan exercise decision depends on the correlation between swap rates at different tenors (e.g., the 10-year swap rate and the 20-year swap rate at future dates). SABR, being a single-factor model for each individual swaption, does not specify these cross-tenor correlations. The Bermudan price is sensitive to correlation, but this dimension is not calibrated.

    4. **Mean reversion at long horizons:** Over 30 years, mean reversion in interest rates is a critical feature. The SABR model, being a local volatility/stochastic volatility model for forward rates, may not adequately capture mean reversion effects that become dominant over multi-decade horizons.

    5. **Smile dynamics:** SABR calibrates to the static smile at each maturity but does not constrain how the smile evolves over time. The Bermudan's value depends on the future smile (at exercise dates), which is not pinned down by today's calibration.

    **Most sensitive aspects of the Bermudan:** The exercise boundary (which determines when it is optimal to exercise) and the continuation value (which depends on the distribution of future swap rates) are most sensitive to the extrapolation. Small changes in extrapolated volatility or correlation parameters can shift the exercise boundary, materially affecting the price.

---

**Exercise 2.** Two quant teams implement the same Hull--White model for a callable bond. Team A uses cubic spline interpolation for the yield curve, while Team B uses monotone piecewise-linear interpolation. The resulting prices differ by 3 bps. Explain why implementation choices can have this magnitude of impact and propose a protocol for quantifying implementation risk.

??? success "Solution to Exercise 2"

    **Why implementation choices can produce 3 bps differences:**

    The Hull-White model prices depend on the yield curve through the time-dependent drift $\theta(t)$, which is calibrated to match the initial term structure exactly. The function $\theta(t)$ is derived from the yield curve:

    $$
    \theta(t) = \frac{\partial f(0,t)}{\partial t} + \kappa f(0,t) + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})
    $$

    where $f(0,t)$ is the instantaneous forward rate curve. This derivative $\partial f/\partial t$ amplifies any differences in the yield curve construction:

    - **Cubic spline interpolation** (Team A) produces a smooth yield curve with continuous second derivatives, but may introduce oscillations (especially in the forward rate curve) between node points. These oscillations are amplified by differentiation.
    - **Monotone piecewise-linear interpolation** (Team B) produces a non-oscillatory curve but has discontinuous first derivatives at node points, creating jumps in the forward rate curve.

    For a callable bond, the price depends on the yield curve at many points (each call date), and the forward rate curve between nodes. A 3 bps difference in price is entirely plausible because:

    - The forward rate curve can differ by 5--10 bps between interpolation methods at points between nodes.
    - The callable bond's optionality makes it sensitive to the shape of the forward curve (exercise decisions depend on rate levels at future call dates).
    - Integration of $\theta(t)$ over 10+ years accumulates interpolation differences.

    **Protocol for quantifying implementation risk:**

    1. **Define a reference implementation set:** Select $M$ reasonable implementations (varying interpolation, solver, grid resolution, time stepping).
    2. **Common test portfolio:** Price a standardized set of instruments (vanilla bonds, caps, swaptions, callable bonds) under each implementation.
    3. **Compute the implementation risk measure:**

        $$
        \text{Implementation risk} = \max_{m} V_m - \min_{m} V_m
        $$

        for each instrument.

    4. **Convergence testing:** For numerical parameters (grid size, time steps), verify that results converge as resolution increases. If they do not, flag the instrument as implementation-sensitive.
    5. **Sensitivity analysis:** Perturb each implementation choice individually to identify which choices drive the largest price differences.
    6. **Documentation and governance:** Record the chosen implementation, justify the choices, and maintain the price range as an implementation risk reserve.

---

**Exercise 3.** A trader hedges a 10-year CMS spread option using delta and vega from a two-factor LMM. Over a 1-month period, the realized P&L deviates significantly from the model-predicted P&L. List at least four potential sources of this hedging error, distinguishing between model risk, market risk, and operational risk.

??? success "Solution to Exercise 3"

    **Potential sources of hedging error, classified by risk type:**

    **Model risk (errors in the model itself):**

    1. **Incorrect volatility dynamics:** The two-factor LMM may not capture the true volatility dynamics of the underlying rates. If realized volatility differs from the model-implied volatility (e.g., due to stochastic volatility effects not captured by a diffusion LMM), the vega hedge will be imperfect.

    2. **Correlation misspecification:** The CMS spread option depends critically on the correlation between different swap rates. The two-factor LMM imposes a specific (low-rank) correlation structure. If the realized correlation differs, the spread option's value changes but the hedge does not adjust correctly.

    3. **Skew and convexity errors:** CMS spread options are sensitive to the smile/skew of the underlying swaptions. If the LMM does not accurately reproduce the smile dynamics, the model-implied Greeks (especially gamma and vanna) will be wrong.

    **Market risk (factors not hedged):**

    4. **Unhedged higher-order Greeks:** Delta and vega hedging leaves the portfolio exposed to gamma, vanna (cross-derivative of vega and delta), and volga (second derivative with respect to volatility). Over a 1-month horizon with significant rate or volatility moves, these higher-order effects can produce material P&L.

    5. **Basis risk:** If the hedge instruments (e.g., plain vanilla swaptions) do not exactly offset the risk factors of the CMS spread option, basis risk arises. The LMM may not fully capture the basis between the hedge instruments and the exotic.

    **Operational risk:**

    6. **Discrete rebalancing:** The model assumes continuous delta hedging, but rebalancing occurs at discrete intervals (e.g., daily). Over a 1-month period with 20+ rebalancing events, the cumulative discrete hedging error can be significant, especially if gamma is large.

    7. **Execution slippage and market impact:** The model assumes frictionless trading. In practice, bid-ask spreads, market impact of large trades, and execution timing create systematic deviations from the model-predicted P&L.

---

**Exercise 4.** A model validation team proposes the following benchmark test: price the same exotic derivative under three different models (Hull--White, LMM, and SABR-LMM) and report the range of prices. If the range is less than 2 bps, the model risk is deemed acceptable. Critique this approach and suggest improvements.

??? success "Solution to Exercise 4"

    **Critique of the three-model benchmark test:**

    The proposed methodology (price under Hull-White, LMM, and SABR-LMM; accept if range < 2 bps) has several weaknesses:

    1. **Selection bias:** Three specific models may agree with each other while all being wrong in the same direction. For example, all three are continuous diffusion models---none captures jump risk. The range captures inter-model disagreement but not systematic bias.

    2. **Arbitrary threshold:** The 2 bps threshold is not grounded in any statistical or economic framework. For some products (e.g., large notional CMS spread options), 2 bps may represent millions of dollars. For others (e.g., vanilla caps), 2 bps may be within bid-ask spreads.

    3. **Model correlation:** The three models share common assumptions (no jumps, Gaussian or near-Gaussian dynamics, continuous rebalancing). Their price ranges may be artificially narrow because they occupy a small region of the space of possible models.

    4. **Parameter dependence:** Each model has calibration parameters, and the price depends on which parameters are used. The "price under model X" is not unique---it depends on the calibration methodology. Two implementations of the same LMM can produce different prices.

    5. **Ignores hedging dimension:** Model risk affects not only prices but also hedge ratios. Two models may agree on price but disagree on delta or vega, leading to different hedging P&L over time.

    **Suggested improvements:**

    1. **Include structurally different models:** Add models with fundamentally different dynamics (e.g., jump-diffusion, rough volatility, local volatility) to broaden the range of assumptions tested.

    2. **Weighted range based on calibration quality:** Weight each model's price by the quality of its calibration fit. A model that fits the vanilla surface poorly should receive less weight.

    3. **Stress-test each model:** For each model, perturb calibration parameters within their confidence intervals and report the resulting price range. The model-specific uncertainty may exceed the inter-model range.

    4. **Include hedging analysis:** Compare not just initial prices but also simulated hedging P&L under each model over a historical period or under stress scenarios.

    5. **Scale threshold to notional and product sensitivity:** Replace the fixed 2 bps threshold with a threshold proportional to the product's vega, gamma, or other relevant sensitivity, and express in dollar terms relative to the risk appetite.

    6. **Bayesian model averaging:** Rather than accepting/rejecting based on range, compute a model-averaged price with uncertainty bounds that reflect both inter-model and intra-model (parameter) uncertainty.

---

**Exercise 5.** Dynamic delta hedging of an interest rate option assumes continuous rebalancing with zero transaction costs. In practice, hedging occurs daily with bid-ask spreads of 0.25 bps on the underlying swap. For a 5-year swaption with notional \$500 million and daily delta rebalancing, estimate the cumulative transaction costs over the life of the option. How does this compare to the model-implied option price?

??? success "Solution to Exercise 5"

    **Setup:** 5-year swaption, \$500 million notional, daily delta rebalancing, bid-ask spread = 0.25 bps on the underlying swap.

    **Step 1: Estimate daily hedge rebalancing amount.**

    The delta of a swaption changes daily due to changes in rates, time decay, and volatility moves. For an ATM swaption, the daily change in delta (gamma effect) can be estimated as:

    $$
    \Delta(\text{delta}) \approx \Gamma \times \Delta r
    $$

    where $\Gamma$ is the swaption gamma and $\Delta r$ is the daily rate move. For a 5-year ATM swaption:

    - Typical gamma: $\Gamma \approx 500{,}000$ per bp (for \$500M notional, in DV01 terms)
    - Typical daily rate move: $\Delta r \approx 3$ bps (standard deviation)
    - Daily rebalancing notional: $\approx \Gamma \times \Delta r \times \text{DV01 conversion} \approx$ \$50--100 million notional equivalent per day (rough order of magnitude)

    A simpler approach: the hedge involves trading the underlying swap. The daily rebalancing amount in notional terms depends on how much delta changes. For an ATM swaption with $\delta = 0.5$, the initial hedge is approximately \$250M in swaps. Daily rebalancing trades are a fraction of this, typically 1--5% of the initial hedge, so roughly \$2.5--12.5M per day.

    **Step 2: Transaction cost per rebalancing.**

    Each rebalancing trade incurs a half-spread cost:

    $$
    \text{Cost per trade} = \text{notional traded} \times \frac{\text{bid-ask}}{2} \times \text{DV01}
    $$

    For a 5-year swap, DV01 $\approx$ 4.5 bps per 1% notional. The half-spread cost per \$1M traded is:

    $$
    \text{Cost per \$1M} = 1{,}000{,}000 \times 0.000025 \times 0.00045 \approx \$0.01
    $$

    This is very small per trade. More directly, the bid-ask spread of 0.25 bps means crossing the spread costs 0.125 bps of DV01. For \$10M rebalancing with 5-year DV01 ~\$4,500 per \$1M notional:

    $$
    \text{Daily cost} \approx 10 \times 4{,}500 \times 0.000125 = \$5.63
    $$

    **Step 3: Cumulative cost.**

    Over 5 years (approximately 1,260 trading days):

    Using a more standard approach from the literature, the cumulative hedging cost for delta hedging is approximately:

    $$
    \text{Total cost} \approx N \times \sigma_{\text{daily}} \times \Gamma \times \text{half-spread} \times \sqrt{n_{\text{days}}} \times \text{DV01}
    $$

    A practical rule of thumb: transaction costs for daily delta hedging of a swaption amount to roughly **2--10 bps** of the option premium, depending on the bid-ask spread and gamma profile. For a 5-year ATM swaption on \$500M with a premium of approximately 200--400 bps of annuity (roughly \$4--8M), the cumulative transaction cost over the life is:

    $$
    \text{Total transaction cost} \approx 5\% \times \$6M = \$300{,}000
    $$

    This represents approximately **0.6 bps** of notional, which is small relative to the option premium (200--400 bps of annuity) but not negligible. The transaction cost is a drag on hedging performance and represents a real cost that is not captured in the frictionless model price. It highlights the gap between theoretical continuous hedging and practical discrete hedging with frictions.

---

**Exercise 6.** The Basel Committee's SR 11-7 guidance on model risk management requires that models be validated independently of the development team. Describe the key elements of a model validation report for an interest rate derivatives pricing model, including (a) conceptual soundness, (b) data quality, (c) backtesting, and (d) stress testing. For each element, give a concrete example relevant to a LIBOR Market Model.

??? success "Solution to Exercise 6"

    **Key elements of a model validation report for a LIBOR Market Model:**

    **(a) Conceptual soundness:**

    This assesses whether the model's theoretical framework is appropriate for its intended use. The validation report should examine:

    - **Theoretical foundations:** Does the LMM correctly implement the no-arbitrage drift condition? Are the forward rate dynamics consistent with the chosen numeraire? Is the measure change from the spot measure to the terminal measure implemented correctly?
    - **Assumptions and limitations:** Are the key assumptions (continuous diffusion, no jumps, specific volatility parameterization, finite-rank correlation) clearly documented? Are the limitations acknowledged (e.g., difficulty capturing smile dynamics without extensions)?
    - **Example for LMM:** Verify that the drift of forward rate $L_i(t)$ under the terminal measure $\mathbb{Q}^{T_N}$ satisfies:

        $$
        \mu_i(t) = -\sigma_i(t) \sum_{j=i+1}^{N-1} \frac{\delta_j L_j(t)}{1 + \delta_j L_j(t)} \rho_{ij} \sigma_j(t)
        $$

        An independent re-derivation should confirm this drift specification. Errors in the drift (e.g., wrong sign, missing terms) would produce arbitrage in the model.

    **(b) Data quality:**

    This assesses whether the input data is accurate, complete, and appropriate:

    - **Market data:** Are swaption volatilities sourced from reliable providers? Are stale or illiquid quotes identified and handled appropriately? Is the yield curve construction robust?
    - **Calibration data selection:** Are the calibration instruments (European swaptions by expiry and tenor) sufficient to constrain the model parameters? Are highly illiquid quotes excluded or down-weighted?
    - **Example for LMM:** Verify that the swaption volatility matrix used for calibration is arbitrage-free (e.g., no calendar spread arbitrage between adjacent expiries). Check that the interpolation of missing swaption quotes (e.g., for off-grid expiry/tenor combinations) does not introduce artifacts.

    **(c) Backtesting:**

    This compares model predictions with realized outcomes:

    - **Price backtesting:** Compare model-predicted option prices with subsequent market prices over a historical period.
    - **Hedging P&L backtesting:** Simulate the hedging strategy prescribed by the model over historical data and compare the realized P&L with the model-predicted P&L. Systematic deviations indicate model misspecification.
    - **Example for LMM:** Over the past 2 years, run daily delta-vega hedging of a portfolio of Bermudan swaptions using the LMM. Compare the cumulative hedging P&L with the model-predicted zero P&L. Compute the mean, standard deviation, and skewness of daily P&L residuals. Test whether the mean is statistically different from zero (indicating systematic hedging bias).

    **(d) Stress testing:**

    This evaluates model behavior under extreme or unusual market conditions:

    - **Parameter stress:** Perturb calibrated parameters (volatilities, correlations, mean reversion) by $\pm 2$ standard deviations and report the price impact.
    - **Market scenario stress:** Reprice under historical stress scenarios (2008 crisis, 2020 COVID shock, taper tantrum) and evaluate whether the model produces sensible prices and Greeks.
    - **Boundary behavior:** Test model behavior when rates approach zero, when the yield curve inverts, or when volatility spikes.
    - **Example for LMM:** Recalibrate the LMM to the swaption surface as of September 2008 (Lehman collapse). Verify that the model calibrates without failure, produces positive prices for all instruments, and yields hedge ratios that do not exhibit extreme instability. Report the range of Bermudan swaption prices under $\pm 20\%$ shifts to the entire volatility surface and $\pm 0.3$ shifts to all pairwise correlations.
