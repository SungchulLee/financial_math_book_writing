# OIS-LIBOR Spread Modeling

The overnight indexed swap (OIS) rate and LIBOR historically tracked closely but diverged significantly during financial crises, revealing credit risk and market structure effects. The multi-curve framework models these spreads to capture basis risk, funding costs, and counterparty credit risk in interest rate derivatives.

## Key Concepts

**OIS vs. LIBOR Rates**

- **OIS**: Daily overnight rate compounded, zero credit risk (central bank collateral)
- **LIBOR**: 3M/6M/12M unsecured borrowing rate, contains credit and term premium

OIS-LIBOR spread (basis) represents:

$$\text{LIBOR}(T) - \text{OIS}(T) = \text{Credit Premium} + \text{Liquidity Premium} + \text{Term Premium}$$

**Multi-Curve Framework**
Traditional approach: single curve for discounting and projection
Modern approach: separate curves for:

1. **Discount curve** (OIS): risk-free rate, used for all PV calculations
2. **Projection curves** (LIBOR): one curve per tenor (3M, 6M, 12M)
3. **Basis curves**: spread between LIBOR and OIS for each tenor

Forward LIBOR in multi-curve:

$$L_{t}(T, T+\Delta) = \text{OIS}_t(T, T+\Delta) + \text{Basis}_t(\Delta)$$

**Spread Modeling Dynamics**
Spread $X_t = L_t - \text{OIS}_t$ dynamics can follow:

1. **Mean-reverting**: $dX_t = \kappa(\bar{X} - X_t) dt + \sigma_X dB_t$
2. **Deterministic spreads** (earlier models): constant basis
3. **Stochastic spreads**: correlate with credit/liquidity conditions

**Funding Cost Modeling**
Banks have different funding rates depending on creditworthiness:

$$r_t^{\text{funding}}(T) = r_t^{\text{OIS}}(T) + \text{CDS}_t + \text{Liquidity Adjustment}$$

Swap pricing reflection:

$$\text{Par Swap Rate} = \text{OIS Forward} + \text{Funding Spread}$$

**CVA and Counterparty Risk**
Multi-curve framework enables:

- Credit valuation adjustment (CVA) using OIS as risk-free rate
- Proper valuation of collateralized transactions (discounted at OIS)
- Uncollateralized liabilities (discounted at own credit curve)

**Basis Risk in Hedging**
Hedging LIBOR exposure with OIS introduces basis risk:

$$P\&L_{\text{basis}} = N \times (\text{LIBOR} - \text{OIS}) \times dBasis \times \Delta t$$

Risk management requires:

- Separate basis risk limits
- Monitoring spread term structure
- Dynamic rehedging of basis exposure

!!! warning "Implementation Challenges"
    Multi-curve framework introduces complexity:

    - Computational cost of managing multiple curves
    - Calibration instability when spreads are tight
    - Backward compatibility with legacy systems
    - Correlation assumptions between rate and spread
    - Crisis scenarios where basis explodes (e.g., LIBOR freeze 2008)

---

## Exercises

**Exercise 1.** The OIS-LIBOR spread for 3-month USD LIBOR widened from approximately 10 bps to over 350 bps during the 2008 financial crisis. Explain the economic forces that drove this widening and why the spread did not fully revert to pre-crisis levels even after markets stabilized.

??? success "Solution to Exercise 1"

    **Economic forces driving the widening:**

    The OIS-LIBOR spread for 3-month USD LIBOR widened from ~10 bps to over 350 bps during 2008 due to several reinforcing factors:

    1. **Credit risk surge:** As major financial institutions (Bear Stearns, Lehman Brothers, AIG) failed or nearly failed, the perceived credit risk of lending unsecured to any bank increased dramatically. LIBOR, being an unsecured lending rate, absorbed this credit premium. OIS, based on overnight lending with daily rollover (and effectively central-bank-backed), was largely insulated.

    2. **Liquidity hoarding:** Banks became unwilling to lend for term periods (even 3 months), preferring to hold liquid reserves. The resulting scarcity of term lending pushed LIBOR up relative to overnight rates. This liquidity premium was distinct from credit risk.

    3. **Counterparty risk uncertainty:** The interconnectedness of the financial system meant that lending to any bank carried exposure to the entire system. Even solvent banks demanded higher rates to compensate for uncertainty about counterparty solvency.

    4. **Market dysfunction:** The interbank lending market partially froze, meaning LIBOR submissions became increasingly based on judgment rather than transactions, potentially overstating or understating actual borrowing costs.

    **Why the spread did not fully revert:**

    After the acute phase, spreads settled at 20--30 bps (2--3 times pre-crisis levels) rather than returning to ~10 bps because:

    - **Regulatory changes:** Basel III liquidity requirements (LCR, NSFR) made term unsecured lending more capital-intensive, permanently increasing its cost relative to overnight lending.
    - **Collateralization became standard:** Post-crisis, collateral posting (CSA) became the norm for derivatives, making OIS the natural discount rate and institutionalizing the OIS-LIBOR distinction.
    - **Structural shift in money markets:** Money market funds shifted from unsecured bank paper to secured instruments (repo, Treasury bills), reducing supply of unsecured term funding.
    - **Risk awareness:** Market participants permanently recalibrated their assessment of bank credit risk, recognizing that the pre-crisis spread was artificially compressed.

---

**Exercise 2.** In a multi-curve framework, a 5-year interest rate swap has quarterly floating payments at 3-month LIBOR and annual fixed payments. The OIS discount factors are given, and the 3-month LIBOR forward rates are projected from the LIBOR curve. Write down the present value of the floating leg

$$
V_{\text{float}} = \sum_{i=1}^{20} \delta_i\,L_i^{3M}(0)\,P^{\text{OIS}}(0, T_{i})
$$

and explain why $L_i^{3M}(0)$ must come from the LIBOR curve while $P^{\text{OIS}}(0, T_i)$ comes from the OIS curve.

??? success "Solution to Exercise 2"

    The present value of the floating leg is given by:

    $$
    V_{\text{float}} = \sum_{i=1}^{20} \delta_i\,L_i^{3M}(0)\,P^{\text{OIS}}(0, T_{i})
    $$

    **Why $L_i^{3M}(0)$ comes from the LIBOR curve:**

    The forward LIBOR rate $L_i^{3M}(0)$ represents the market's expectation (under the appropriate forward measure) of the 3-month LIBOR fixing at the start of period $i$. This rate reflects the credit and liquidity characteristics of unsecured interbank lending. It is extracted from the 3-month LIBOR curve, which is constructed from:

    - 3-month LIBOR fixings (short end)
    - FRAs referencing 3-month LIBOR (intermediate)
    - LIBOR swaps with quarterly floating payments (long end)

    The OIS curve cannot be used for projection because the OIS-implied forward rate $\frac{1}{\delta_i}\left(\frac{P^{\text{OIS}}(0,T_{i-1})}{P^{\text{OIS}}(0,T_i)} - 1\right)$ does not include the credit/liquidity spread embedded in LIBOR. Using OIS forwards would underestimate each floating payment by approximately the OIS-LIBOR basis spread.

    **Why $P^{\text{OIS}}(0, T_i)$ comes from the OIS curve:**

    For collateralized swaps (the standard post-crisis), the posted collateral earns the OIS rate. By no-arbitrage, the appropriate discount rate for collateralized cash flows is OIS. The reasoning is:

    - The collateral posted against the mark-to-market of the swap accrues interest at OIS.
    - The cost of funding the collateral is therefore OIS.
    - Discounting at any other rate would create an arbitrage between the swap and its collateral.

    Using LIBOR discount factors $P^{\text{LIBOR}}(0, T_i)$ for discounting would overstate the discount rate (since LIBOR > OIS), undervaluing future cash flows and producing prices inconsistent with the market for collateralized trades.

---

**Exercise 3.** The OIS-LIBOR spread $X_t$ follows a mean-reverting process $dX_t = \kappa(\bar{X} - X_t)\,dt + \sigma_X\,dB_t$ with $\bar{X} = 15$ bps, $\kappa = 0.5$, $\sigma_X = 8$ bps, and current value $X_0 = 20$ bps. Compute the expected spread $\mathbb{E}[X_1]$ in 1 year and the standard deviation of $X_1$. What is the probability that the spread exceeds 40 bps?

??? success "Solution to Exercise 3"

    The spread follows an Ornstein-Uhlenbeck process:

    $$
    dX_t = \kappa(\bar{X} - X_t)\,dt + \sigma_X\,dB_t
    $$

    with $\bar{X} = 15$ bps, $\kappa = 0.5$, $\sigma_X = 8$ bps, $X_0 = 20$ bps.

    The solution is normally distributed: $X_T \sim N(\mu_T, \sigma_T^2)$ with:

    $$
    \mu_T = \bar{X} + (X_0 - \bar{X})e^{-\kappa T}
    $$

    $$
    \sigma_T^2 = \frac{\sigma_X^2}{2\kappa}(1 - e^{-2\kappa T})
    $$

    **Expected spread at $T = 1$:**

    $$
    \mu_1 = 15 + (20 - 15)e^{-0.5} = 15 + 5 \times 0.6065 = 15 + 3.033 = 18.03 \text{ bps}
    $$

    **Standard deviation at $T = 1$:**

    $$
    \sigma_1^2 = \frac{64}{1.0}(1 - e^{-1.0}) = 64 \times (1 - 0.3679) = 64 \times 0.6321 = 40.45 \text{ bps}^2
    $$

    $$
    \sigma_1 = \sqrt{40.45} = 6.36 \text{ bps}
    $$

    **Probability that $X_1 > 40$ bps:**

    $$
    P(X_1 > 40) = 1 - N\!\left(\frac{40 - 18.03}{6.36}\right) = 1 - N(3.453)
    $$

    $$
    N(3.453) \approx 0.99972
    $$

    $$
    P(X_1 > 40) \approx 0.00028 = 0.028\%
    $$

    The probability of the spread exceeding 40 bps in one year is approximately **0.03%**, which is very small under this model. The mean-reversion pulls the spread back toward 15 bps, and starting at 20 bps, reaching 40 bps would require a move of about 3.5 standard deviations. However, this result depends heavily on the Gaussian assumption; in practice, spread dynamics exhibit fat tails and jumps (as seen in 2008), so the true probability of extreme widening is likely much higher than this model suggests.

---

**Exercise 4.** A bank has a portfolio of collateralized and uncollateralized swaps. The collateralized swaps are discounted at OIS, while the uncollateralized swaps must account for funding costs. Explain why a bank with a higher credit spread assigns a different value to the same uncollateralized swap compared to a bank with a lower credit spread. Is this a market inconsistency or a legitimate economic effect?

??? success "Solution to Exercise 4"

    **Why different banks value the same uncollateralized swap differently:**

    For a collateralized swap, both banks discount at OIS and arrive at the same value (assuming they agree on market data). For an uncollateralized swap, the absence of collateral means:

    - **Bank A** (high credit spread, e.g., CDS = 80 bps) funds its derivative exposure at $r^{\text{OIS}} + 80$ bps.
    - **Bank B** (low credit spread, e.g., CDS = 20 bps) funds at $r^{\text{OIS}} + 20$ bps.

    The funding value adjustment (FVA) for each bank is:

    $$
    \text{FVA}_A = \int_0^T \text{EE}_A(t) \cdot s_A \cdot P^{\text{OIS}}(0,t)\,dt
    $$

    $$
    \text{FVA}_B = \int_0^T \text{EE}_B(t) \cdot s_B \cdot P^{\text{OIS}}(0,t)\,dt
    $$

    where $\text{EE}(t)$ is the expected exposure and $s$ is the funding spread. Since $s_A > s_B$, Bank A has a larger FVA and thus assigns a lower value to the swap (from its perspective as the party with positive expected exposure).

    **Market inconsistency or legitimate economic effect?**

    This is a **legitimate economic effect**, not a market inconsistency. Different banks face genuinely different costs:

    - If Bank A receives a positive cash flow in the future, it must fund the negative mark-to-market today at its own (higher) borrowing cost.
    - The cost of funding is real and bank-specific---it is not an artifact of the model.
    - The difference in valuations reflects the fact that the same derivative has different economic costs for different entities, depending on their funding structure.

    However, this creates a **market microstructure challenge:** there is no single "market price" for uncollateralized derivatives. This is why the industry has moved strongly toward collateralization (which eliminates FVA and produces a unique, bank-independent valuation) and why FVA remains one of the most debated topics in quantitative finance. Some argue that FVA should not affect derivative pricing (since it conflates funding with hedging), while others argue it is a real cost that must be reflected in pricing to avoid losses.

---

**Exercise 5.** Consider a tenor basis swap that exchanges 3-month LIBOR for 6-month LIBOR. In a single-curve world, the basis spread should be zero. Explain why a non-zero basis spread exists in practice and describe how a multi-curve model captures this. If the 3M/6M basis is currently 5 bps, estimate the annual cash flow on a \$1 billion notional basis swap.

??? success "Solution to Exercise 5"

    **Tenor basis swap structure:** In a 3M/6M basis swap, one party pays 3-month LIBOR (reset quarterly) and receives 6-month LIBOR (reset semiannually) on the same notional. A basis spread $b$ is added to the 3M leg: one pays $L^{3M} + b$ quarterly and receives $L^{6M}$ semiannually.

    **Why the basis spread is non-zero:**

    In a single-curve world, the 6-month rate should exactly equal the compounded 3-month rate, making the basis swap fair with $b = 0$. In practice, $b \neq 0$ because:

    1. **Credit risk tenor mismatch:** A 6-month unsecured loan locks the lender into credit exposure for 6 months. Two consecutive 3-month loans allow reassessment after 3 months. The 6-month rate includes a premium for this additional credit commitment, making $L^{6M}$ higher than the compounded $L^{3M}$.

    2. **Liquidity differences:** The 3-month and 6-month money markets have different depths and participant bases, leading to different supply-demand dynamics.

    3. **Marginal funding preference:** Banks may prefer to fund at specific tenors (e.g., 3-month for regulatory reasons), creating demand-driven basis effects.

    **Multi-curve capture:** A multi-curve model builds separate forward curves for each tenor. The basis spread is the difference between the forward rate from the 6M curve and the compounded forward from the 3M curve:

    $$
    b(T) = L^{6M}(0; T, T+6M) - \left[\frac{(1 + \delta_{3M}L^{3M}(0; T, T+3M))(1 + \delta_{3M}L^{3M}(0; T+3M, T+6M)) - 1}{\delta_{6M}}\right]
    $$

    **Cash flow estimate:** For a \$1 billion notional basis swap with a 3M/6M basis of 5 bps:

    The annual cash flow attributable to the basis is approximately:

    $$
    \text{Annual basis cash flow} \approx N \times b = 1{,}000{,}000{,}000 \times 0.0005 = \$500{,}000
    $$

    More precisely, the cash flow depends on the payment frequency and netting of the two legs, but the order of magnitude is \$500,000 per year on \$1 billion notional for a 5 bps basis.

---

**Exercise 6.** In the transition from LIBOR to SOFR (Secured Overnight Financing Rate), the credit component of LIBOR disappears. Discuss how this transition affects the multi-curve framework. Will a multi-curve approach still be necessary in a post-LIBOR world, and if so, what curves will replace the LIBOR projection curves?

??? success "Solution to Exercise 6"

    **Impact of LIBOR-to-SOFR transition on the multi-curve framework:**

    LIBOR embedded credit and term premiums, which created spreads between the OIS discount curve and LIBOR projection curves. SOFR is a secured overnight rate with negligible credit risk, essentially equivalent to the OIS rate. The transition has several effects:

    **Simplification---return to near-single-curve:** Since SOFR is the overnight secured rate and the OIS curve is derived from SOFR-based swaps, the projection and discount curves converge:

    $$
    P^{\text{discount}}(0,T) = P^{\text{OIS}}(0,T) \approx P^{\text{SOFR projection}}(0,T)
    $$

    There is no credit spread between the "risk-free" discount curve and the projection curve, eliminating the main driver of multi-curve complexity.

    **Will multi-curve still be necessary?** Yes, but for different reasons:

    1. **Legacy LIBOR contracts:** During the transition period (and beyond, for long-dated contracts), some instruments still reference LIBOR (or LIBOR + spread adjustment). These require a separate projection curve, maintaining multi-curve needs temporarily.

    2. **Term SOFR vs. compounded SOFR:** Term SOFR (forward-looking, derived from futures) and compounded SOFR in arrears are different rate constructions. If instruments reference different SOFR variants, separate curves may be needed.

    3. **Cross-currency basis:** Multi-curve issues persist in cross-currency markets. The basis between USD SOFR and, say, EUR ESTR (or GBP SONIA) still requires separate curves for each currency.

    4. **Credit-sensitive rates:** Some market participants use credit-sensitive alternatives (BSBY, Ameribor). If these coexist with SOFR, a multi-curve framework is needed for portfolios that reference both.

    5. **Tenor basis for non-SOFR benchmarks:** In non-USD markets, the transition to RFRs (ESTR, SONIA, TONA) is at different stages, and tenor bases may persist.

    **What replaces LIBOR projection curves?**

    - The primary projection curve becomes the **SOFR OIS curve** (identical to the discount curve for collateralized trades).
    - For legacy contracts: **SOFR + fixed spread adjustment** curves (one per LIBOR tenor, using the ISDA-mandated spread adjustments).
    - For cross-currency: **FX-implied SOFR curves** or basis-adjusted curves for each currency pair.

    The net effect is a significant simplification of the multi-curve framework in single-currency USD markets, but multi-curve considerations do not disappear entirely.
