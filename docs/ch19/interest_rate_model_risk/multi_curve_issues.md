# Multi-Curve Issues


Modern interest-rate markets operate with **multiple yield curves**, reflecting credit and liquidity effects. This fundamentally alters pricing and hedging compared to single-curve frameworks.

---

## From single-curve to multi-curve


Pre-crisis practice used:
- one curve for discounting and forwarding.

Post-crisis markets distinguish:
- OIS curves for discounting,
- tenor-specific curves for forwarding (LIBOR, EURIBOR).

This separation is essential for arbitrage-free pricing.

---

## Implications for valuation


Multi-curve pricing affects:
- swaps and FRAs,
- caps/floors and swaptions,
- collateralized vs uncollateralized trades.

Cashflows must be discounted and projected using different curves.

---

## Model extensions


Classical models must be extended to:
- handle multiple correlated curves,
- model spreads between curves,
- incorporate collateral and funding effects.

These extensions increase dimensionality and calibration complexity.

---

## Model risk considerations


Multi-curve models introduce:
- additional parameters with weak identifiability,
- dependence on market conventions,
- sensitivity to curve construction choices.

Curve-building risk becomes part of model risk.

---

## Key takeaways


- Single-curve models are no longer sufficient.
- Multi-curve modeling is unavoidable but complex.
- Curve construction choices materially affect prices.

---

## Further reading


- Henrard, *Interest Rate Modelling in the Multi-Curve Framework*.
- Brigo et al., collateral and multi-curve modeling.

---

## Exercises

**Exercise 1.** Before the 2008 financial crisis, a single discount curve was used for both discounting and projection. Explain why the OIS-LIBOR basis widened during the crisis and why this made single-curve pricing inconsistent with market quotes. What specific market instrument first revealed the breakdown of the single-curve assumption?

??? success "Solution to Exercise 1"

    **Pre-crisis single-curve assumption:** Before 2008, the spread between LIBOR and OIS was consistently small (typically 5--10 bps), so practitioners treated them as interchangeable. A single curve (usually constructed from LIBOR swaps) served both for discounting future cash flows and for projecting forward LIBOR rates.

    **Why the basis widened during the crisis:** During the 2008 financial crisis, several forces drove the OIS-LIBOR spread from approximately 10 bps to over 350 bps:

    - **Credit risk:** LIBOR reflects the unsecured borrowing cost of panel banks. As bank credit risk surged (bank defaults, near-defaults, and credit downgrades), the credit premium embedded in LIBOR increased dramatically.
    - **Liquidity hoarding:** Banks became reluctant to lend to each other for term periods, preferring to hold reserves. This liquidity premium pushed term LIBOR rates higher relative to overnight rates.
    - **Counterparty risk:** Uncertainty about which banks might fail made banks demand higher rates for unsecured lending.
    - **OIS stability:** The OIS rate, being based on overnight lending (effectively central-bank-collateralized), remained much more stable, closely tracking the Fed Funds target rate.

    **Instrument revealing the breakdown:** The **basis swap** (exchanging, e.g., 3-month LIBOR for OIS flat, or 3-month LIBOR for 6-month LIBOR) was the instrument that first clearly revealed the breakdown. Before the crisis, basis swap spreads were negligible (near zero). When they widened significantly, it became impossible to consistently value a floating leg using one curve while discounting with the same curve---the single-curve framework produced prices inconsistent with observed basis swap quotes.

    **Why spreads did not fully revert:** Even after the acute phase of the crisis, spreads remained elevated (20--30 bps instead of the pre-crisis 5--10 bps) because:

    - Regulatory changes (Basel III) increased the cost of unsecured interbank lending.
    - Collateralization became standard practice, making OIS the natural discount rate for collateralized trades.
    - Market participants internalized the credit distinction between secured and unsecured rates.

---

**Exercise 2.** In a multi-curve framework, consider a 2-year interest rate swap with semiannual fixed payments and quarterly floating payments referencing 3-month LIBOR. The OIS discount factors are $P^{\text{OIS}}(0, T_j)$ and the 3-month LIBOR forward rates are $L_i^{3M}(0)$. Write down the swap valuation formula, clearly distinguishing where the OIS curve is used (discounting) and where the LIBOR curve is used (projection).

??? success "Solution to Exercise 2"

    **Setup:** 2-year swap, semiannual fixed payments at times $T_1^{\text{fix}} = 0.5, T_2^{\text{fix}} = 1.0, T_3^{\text{fix}} = 1.5, T_4^{\text{fix}} = 2.0$, quarterly floating payments at times $T_1^{\text{flt}} = 0.25, T_2^{\text{flt}} = 0.50, \ldots, T_8^{\text{flt}} = 2.0$.

    **Fixed leg present value:**

    $$
    V_{\text{fixed}} = R \sum_{j=1}^{4} \delta_j^{\text{fix}}\,P^{\text{OIS}}(0, T_j^{\text{fix}})
    $$

    where $R$ is the fixed swap rate and $\delta_j^{\text{fix}} = 0.5$ (semiannual accrual). The OIS discount factors $P^{\text{OIS}}(0, T_j^{\text{fix}})$ are used for discounting because this is a collateralized trade (or, in the multi-curve convention, the risk-free discount curve is OIS).

    **Floating leg present value:**

    $$
    V_{\text{float}} = \sum_{i=1}^{8} \delta_i^{\text{flt}}\,L_i^{3M}(0)\,P^{\text{OIS}}(0, T_i^{\text{flt}})
    $$

    where $\delta_i^{\text{flt}} = 0.25$ (quarterly accrual), $L_i^{3M}(0)$ is the 3-month LIBOR forward rate for period $[T_{i-1}^{\text{flt}}, T_i^{\text{flt}}]$, and $P^{\text{OIS}}(0, T_i^{\text{flt}})$ is the OIS discount factor.

    **Why the curves differ:**

    - **LIBOR curve for projection:** The forward rates $L_i^{3M}(0)$ must be extracted from the 3-month LIBOR curve because they represent the expected 3-month unsecured borrowing rate. This curve is built from 3-month LIBOR fixings, FRAs, and LIBOR swaps. In the multi-curve world, $L_i^{3M}(0) \neq \frac{1}{\delta_i}\left(\frac{P^{\text{OIS}}(0,T_{i-1})}{P^{\text{OIS}}(0,T_i)} - 1\right)$ because the LIBOR forward rate includes a credit/liquidity spread over OIS.

    - **OIS curve for discounting:** Discount factors come from the OIS curve because collateralized derivatives earn the OIS rate on posted collateral. The discount rate should reflect the funding cost of the collateral, which is OIS. Using LIBOR for discounting would overstate the discount rate by the OIS-LIBOR spread.

    The **par swap rate** $R$ is found by setting $V_{\text{fixed}} = V_{\text{float}}$:

    $$
    R = \frac{\sum_{i=1}^{8} \delta_i^{\text{flt}}\,L_i^{3M}(0)\,P^{\text{OIS}}(0, T_i^{\text{flt}})}{\sum_{j=1}^{4} \delta_j^{\text{fix}}\,P^{\text{OIS}}(0, T_j^{\text{fix}})}
    $$

---

**Exercise 3.** A collateralized swap is discounted at the OIS rate, while an uncollateralized swap includes a funding value adjustment (FVA). If the OIS rate is 2.5% and the bank's unsecured funding spread is 50 bps, estimate the impact on the present value of a 10-year, \$100 million notional swap. Should the FVA increase or decrease the value to the bank?

??? success "Solution to Exercise 3"

    **Setup:** OIS rate = 2.5%, unsecured funding spread = 50 bps, 10-year swap, \$100 million notional.

    **Collateralized valuation:** The swap is discounted at the OIS rate of 2.5%. Under standard CSA (credit support annex), the collateral earns OIS, so the discount rate is 2.5%.

    **Uncollateralized valuation:** Without collateral, the bank must fund its derivative exposure at its unsecured rate of $2.5\% + 0.50\% = 3.0\%$. The higher discount rate reduces the present value of future cash flows.

    **Estimating the FVA impact:** The FVA is approximately the difference in present values when discounting at 3.0% versus 2.5%. For a rough estimate on a 10-year at-the-money swap, the average duration of cash flows is approximately 5 years. The PV difference per dollar of cash flow is approximately:

    $$
    \Delta PV \approx \text{spread} \times \text{average duration} = 0.0050 \times 5 = 0.025 = 2.5\%
    $$

    For a \$100 million notional at-the-money swap, the net expected cash flows are small (near zero for a par swap), but the gross cash flows on each leg are significant. A more precise estimate uses the annuity:

    $$
    \text{Annuity at OIS} = \sum_{j=1}^{10} P^{\text{OIS}}(0, T_j) \approx \sum_{j=1}^{10} e^{-0.025j} \approx 8.752
    $$

    $$
    \text{Annuity at OIS + spread} = \sum_{j=1}^{10} e^{-0.030j} \approx 8.530
    $$

    The FVA on the fixed leg (assuming a fixed rate of about 2.5%) is approximately:

    $$
    \text{FVA} \approx R \times N \times (\text{Annuity}_{\text{OIS}} - \text{Annuity}_{\text{funded}}) = 0.025 \times 100{,}000{,}000 \times (8.752 - 8.530)
    $$

    $$
    = 0.025 \times 100{,}000{,}000 \times 0.222 = \$555{,}000
    $$

    This is approximately **5.55 bps** of notional.

    **Direction:** The FVA should **decrease** the value to the bank. The bank faces higher funding costs for the uncollateralized position, so the fair value of receiving the swap is lower (the bank demands a higher fixed rate to compensate) and the fair value of paying the swap is also lower (the bank receives less value from future floating payments when discounted at the higher rate). The FVA is always a cost from the perspective of the bank with the higher credit spread.

---

**Exercise 4.** Consider two tenor-specific LIBOR curves: 3-month and 6-month. The 6-month forward rate for a specific period can be related to two consecutive 3-month forward rates. In a single-curve world, this relationship is exact. Explain why in a multi-curve world, a basis spread arises between the two tenors and how this basis is modeled.

??? success "Solution to Exercise 4"

    **Single-curve relationship:** In a single-curve world with discount factors $P(0,T)$, the 6-month forward rate for $[T, T + 6M]$ can be decomposed as:

    $$
    1 + \delta_{6M} L^{6M}(T) = (1 + \delta_{3M} L^{3M}(T, T+3M))(1 + \delta_{3M} L^{3M}(T+3M, T+6M))
    $$

    This is an exact no-arbitrage relationship when all rates are derived from the same curve.

    **Multi-curve basis:** In a multi-curve world, the 3-month LIBOR curve and the 6-month LIBOR curve are constructed independently from different instruments (3M LIBOR swaps and 6M LIBOR swaps, respectively). The relationship above no longer holds exactly because:

    - **Credit risk tenor dependence:** A 6-month unsecured loan carries more credit risk than two consecutive 3-month loans (since the lender is locked in for 6 months without the ability to reassess after 3 months). This makes $L^{6M} > $ the compounded 3-month rate.
    - **Liquidity premium:** Different tenors have different liquidity characteristics. The 3-month market is typically more liquid than the 6-month market, affecting pricing.
    - **Rollover risk:** Two consecutive 3-month loans expose the lender to rollover risk (the borrower might default before the second period), while a single 6-month loan has different risk characteristics.

    The **basis spread** $b$ captures this difference:

    $$
    1 + \delta_{6M} L^{6M}(T) = (1 + \delta_{3M} L^{3M}(T, T+3M))(1 + \delta_{3M} L^{3M}(T+3M, T+6M)) + \delta_{6M}\,b
    $$

    or equivalently, $L^{6M} \approx L^{3M}_{\text{compounded}} + b$.

    **Modeling the basis:** The basis is modeled as a separate stochastic process, typically mean-reverting:

    $$
    db_t = \kappa_b(\bar{b} - b_t)\,dt + \sigma_b\,dW_t^b
    $$

    where $\bar{b}$ is the long-run average basis (historically 10--25 bps for 3M/6M), with correlations to the underlying rate dynamics. In multi-curve LMMs, the basis for each tenor is an additional state variable.

---

**Exercise 5.** Discuss how multi-curve modeling increases the dimensionality of interest rate models. If a single-curve LMM requires $n$ forward rates, how many additional state variables does a multi-curve extension with $k$ tenor-specific curves introduce? What are the implications for Monte Carlo simulation speed?

??? success "Solution to Exercise 5"

    **Single-curve LMM dimensionality:** A standard LIBOR Market Model with $n$ forward rates has $n$ state variables $L_1(t), L_2(t), \ldots, L_n(t)$, each following a diffusion process. The total number of parameters includes $n$ initial volatilities and an $n \times n$ correlation matrix (with $n(n-1)/2$ free parameters).

    **Multi-curve extension:** With $k$ tenor-specific curves (e.g., OIS, 1M LIBOR, 3M LIBOR, 6M LIBOR), the multi-curve LMM requires:

    - **Forward rates per curve:** Each of the $k$ curves has its own set of forward rates. If the OIS curve has $n$ forward rates and each additional tenor curve also has approximately $n$ forward rates, the total number of state variables is approximately $k \times n$.
    - **Additional spread variables:** Alternatively, one can model $n$ OIS forward rates and $(k-1) \times n$ basis spreads, giving the same total of $k \times n$ state variables.
    - **Correlation structure:** The correlation matrix now has dimension $kn \times kn$, with $kn(kn-1)/2$ free parameters. This includes intra-curve correlations (between forward rates on the same curve) and inter-curve correlations (between rates on different curves).

    **Example:** With $n = 40$ quarterly forward rates and $k = 3$ curves (OIS, 3M, 6M):

    - Single-curve: 40 state variables, $40 \times 39 / 2 = 780$ correlation parameters.
    - Multi-curve: $3 \times 40 = 120$ state variables, $120 \times 119 / 2 = 7{,}140$ correlation parameters.

    **Implications for Monte Carlo:**

    - **Simulation time scales linearly** with the number of state variables (each time step requires evolving $kn$ diffusions instead of $n$), so the per-path cost increases by a factor of approximately $k$.
    - **Variance of estimates** may increase due to additional stochastic dimensions, requiring more paths for the same accuracy.
    - **Memory requirements** increase proportionally.
    - **Calibration becomes much harder:** The vastly larger parameter space ($\sim k^2$ times as many correlation parameters) makes calibration unstable and potentially ill-posed. In practice, strong parametric restrictions on the correlation structure (e.g., separable or block-diagonal forms) are imposed to keep the problem tractable.

    Overall, multi-curve extensions increase Monte Carlo computational cost by a factor of roughly $k$ per path, but the calibration cost increases far more than linearly due to the explosion in the correlation parameter space.

---

**Exercise 6.** A risk manager argues that curve construction choices (interpolation method, instrument selection, bootstrapping algorithm) can change swap valuations by 1--2 basis points. Explain why this "curve-building risk" should be classified as model risk and propose a methodology to quantify it systematically.

??? success "Solution to Exercise 6"

    **Why curve-building risk is model risk:**

    Curve construction is not a purely mechanical process---it involves numerous modeling choices, each of which affects output valuations:

    - **Interpolation method:** Cubic spline, monotone convex, piecewise linear, log-linear on discount factors, etc. Different methods produce different forward rate curves, especially between node points and at the long end.
    - **Instrument selection:** Which market instruments (deposits, FRAs, futures, swaps) are used as inputs, and for which maturities. Including or excluding certain instruments changes the curve.
    - **Bootstrapping algorithm:** Sequential bootstrapping vs. global fitting (e.g., least squares). The order of instrument inclusion in sequential methods can matter.
    - **Smoothing vs. exactness:** Some methods exactly reprice all input instruments but produce oscillating forwards; others produce smooth forwards but reprice instruments only approximately.
    - **Extrapolation:** Beyond the last liquid instrument, the curve is extrapolated, and the method (flat forward, Smith-Wilson, etc.) is purely a modeling choice.

    These are not market risk factors (they do not change with market data) but rather **structural choices that affect valuations**. This is precisely the definition of model risk: uncertainty in outputs arising from uncertainty in modeling methodology.

    **Proposed methodology to quantify curve-building risk:**

    1. **Define a set of plausible curve construction methods:** Select $M$ reasonable alternatives (e.g., 4--6 combinations of interpolation methods and instrument sets).

    2. **Build each curve from the same market data:** On a given date, construct $M$ different yield curves using the same input market quotes but different methodologies.

    3. **Reprice the portfolio under each curve:** For each curve variant $m = 1, \ldots, M$, compute the total portfolio value $V_m$.

    4. **Compute the curve-building risk measure:**

        $$
        \text{Curve-building risk} = \max_m V_m - \min_m V_m
        $$

        or, for a distributional measure, compute the standard deviation $\text{std}(V_1, \ldots, V_M)$.

    5. **Decompose by instrument:** Identify which positions are most sensitive to curve construction choices (typically illiquid tenors, long-dated trades, and trades with cash flows between node points).

    6. **Maintain time series:** Repeat this analysis daily or weekly to understand how curve-building risk varies over time and market conditions.

    7. **Set reserves:** Use the range or a confidence interval to set model risk reserves (e.g., hold the average of the range as a valuation adjustment).

    This methodology is analogous to model risk quantification for pricing models, and it should be part of the model governance framework alongside pricing model validation.
