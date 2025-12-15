# Robust Calibration Criteria

Given the inevitability of model and calibration uncertainty, one should not aim for a single “best fit” but for **robust calibration**: parameter estimates that perform reasonably well across scenarios and over time.

---

## 1. What does robustness mean?

A robust calibration:
- is stable under small data perturbations,
- avoids extreme or implausible parameters,
- delivers reasonable prices and Greeks out of sample,
- does not rely on finely tuned weights or quotes.

---

## 2. Robust objectives

Robust calibration criteria include:
- regularized objectives (see Chapter 5.3),
- robust loss functions (Huber, \(\ell_1\)),
- worst-case or min–max formulations,
- ensemble calibration (multiple fits).

---

## 3. Stability-based validation

Rather than minimizing residuals alone, validate by:
- day-to-day parameter stability,
- sensitivity to quote perturbations,
- stability of Greeks and hedge P&L,
- consistency across maturities and products.

---

## 4. Model risk governance

In institutional settings, robust calibration supports:
- model risk limits,
- valuation adjustment (MVA),
- transparent communication of uncertainty.

Robustness is therefore both a technical and governance requirement.

---

## 5. Key takeaways

- Perfect fit is neither achievable nor desirable.
- Robust calibration prioritizes stability and interpretability.
- Model risk must be assessed jointly with calibration.

---

## Further reading

- Cont, *Model Uncertainty and Its Impact on Pricing*.
- Glasserman & Xu, robust risk measurement.
- Andersen & Piterbarg, practitioner model risk frameworks.
