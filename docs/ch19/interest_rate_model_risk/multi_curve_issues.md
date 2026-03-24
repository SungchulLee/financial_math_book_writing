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

---

**Exercise 2.** In a multi-curve framework, consider a 2-year interest rate swap with semiannual fixed payments and quarterly floating payments referencing 3-month LIBOR. The OIS discount factors are $P^{\text{OIS}}(0, T_j)$ and the 3-month LIBOR forward rates are $L_i^{3M}(0)$. Write down the swap valuation formula, clearly distinguishing where the OIS curve is used (discounting) and where the LIBOR curve is used (projection).

---

**Exercise 3.** A collateralized swap is discounted at the OIS rate, while an uncollateralized swap includes a funding value adjustment (FVA). If the OIS rate is 2.5% and the bank's unsecured funding spread is 50 bps, estimate the impact on the present value of a 10-year, \$100 million notional swap. Should the FVA increase or decrease the value to the bank?

---

**Exercise 4.** Consider two tenor-specific LIBOR curves: 3-month and 6-month. The 6-month forward rate for a specific period can be related to two consecutive 3-month forward rates. In a single-curve world, this relationship is exact. Explain why in a multi-curve world, a basis spread arises between the two tenors and how this basis is modeled.

---

**Exercise 5.** Discuss how multi-curve modeling increases the dimensionality of interest rate models. If a single-curve LMM requires $n$ forward rates, how many additional state variables does a multi-curve extension with $k$ tenor-specific curves introduce? What are the implications for Monte Carlo simulation speed?

---

**Exercise 6.** A risk manager argues that curve construction choices (interpolation method, instrument selection, bootstrapping algorithm) can change swap valuations by 1--2 basis points. Explain why this "curve-building risk" should be classified as model risk and propose a methodology to quantify it systematically.
