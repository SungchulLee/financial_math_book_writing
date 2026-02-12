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
