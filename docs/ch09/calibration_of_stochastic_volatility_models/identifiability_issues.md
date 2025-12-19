# Identifiability Issues

Calibration of stochastic volatility models is fundamentally limited by **identifiability**. Even with rich option surfaces, some parameters are only weakly constrained, leading to instability and ambiguity.

---

## 1. Structural vs practical identifiability

A model is **structurally identifiable** if distinct parameter sets imply distinct option prices in theory.
In practice, calibration suffers from:

- finite and noisy data,
- limited maturity coverage,
- redundancy in parameter effects.

Thus, many parameters are only *practically* identifiable within wide confidence bands.

---

## 2. Typical weakly identifiable parameters

Across stochastic volatility models, common weak points include:

- long-run variance vs initial variance,
- mean reversion speed,
- volatility-of-volatility at long maturities.

These parameters often affect prices in similar ways over limited horizons.

---

## 3. Manifestations in calibration

Poor identifiability appears as:

- flat loss surfaces,
- multiple local minima,
- large day-to-day parameter swings,
- good in-sample fit but poor out-of-sample behavior.

These are inverse-problem symptoms, not optimizer failures.

---

## 4. Diagnostic tools

Useful diagnostics include:

- Jacobian and singular-value analysis,
- fixing subsets of parameters and re-fitting,
- sensitivity analysis across maturities,
- stability checks under quote perturbations.

---

## 5. Key takeaways

- Not all parameters are equally identifiable.
- Weak identifiability is intrinsic to stochastic volatility models.
- Calibration should prioritize stable directions.

---

## Further reading

- Engl, Hanke & Neubauer, *Regularization of Inverse Problems*.
- Gatheral, *The Volatility Surface*.
