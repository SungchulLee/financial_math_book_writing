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
