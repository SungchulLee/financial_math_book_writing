# Fitting Initial Yield Curves


A fundamental requirement of any interest-rate model is the **exact fit of the initial yield curve**. Since discount factors are directly observable from the market, a model must reproduce them to avoid static arbitrage.

---

## Market input and bootstrapping


The market provides quotes for liquid instruments such as:
- deposits and short-term rates,
- futures and FRAs,
- OIS and IRS swaps.

From these, a discount curve \(P(0,T)\) is constructed via **bootstrapping**, ensuring that each instrument is priced exactly.

---

## Curve fitting vs model fitting


Two conceptually distinct steps are involved:

1. **Curve construction:** build a smooth, arbitrage-free discount curve from market quotes.
2. **Model initialization:** ensure the model reproduces this curve at time 0.

Modern practice treats curve construction as a pre-model step.

---

## Exact fit techniques


Common approaches to enforce exact fit include:

- **Deterministic shifts:** add a time-dependent drift (e.g. Hull–White extension),
- **Initial term-structure fitting:** calibrate model functions to match \(P(0,T)\),
- **HJM framework:** exact fit is automatic by construction.

Exact fit is essential for pricing curve-sensitive products.

---

## Consequences of poor curve fit


Failure to match the initial curve leads to:
- immediate arbitrage,
- systematic mispricing of swaps and FRAs,
- unstable hedging behavior.

Thus, curve fitting is non-negotiable in practice.

---

## Key takeaways


- The initial yield curve must be fitted exactly.
- Curve construction and model calibration are separate tasks.
- Shifts and HJM ensure consistency with market curves.

---

## Further reading


- Brigo & Mercurio, curve construction.
- Andersen & Piterbarg, interest-rate modeling practice.
