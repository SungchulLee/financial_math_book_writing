# Stability and Identifiability


Calibration of interest-rate models faces challenges of **stability** and **identifiability**, especially in multi-factor and infinite-dimensional frameworks.

---

## Identifiability issues


Some parameters are weakly identifiable due to:
- limited option maturity coverage,
- correlations between factors,
- flat sensitivity of prices to certain directions.

This leads to multiple parameter sets fitting the same data.

---

## Stability across time


A stable calibration should exhibit:
- smooth parameter evolution,
- robustness to small quote changes,
- consistent dynamics across market regimes.

Large day-to-day parameter swings indicate overfitting.

---

## Diagnostic tools


Useful diagnostics include:
- sensitivity and Jacobian analysis,
- perturbation of market quotes,
- rolling-window calibration tests.

These help separate structural issues from numerical ones.

---

## Practical mitigation strategies


Stability is improved by:
- reducing model dimensionality,
- imposing economically motivated constraints,
- penalizing parameter variability,
- focusing calibration on the most liquid instruments.

Practitioners often prefer stability over perfect fit.

---

## Key takeaways


- Calibration stability is as important as fit quality.
- Identifiability problems are intrinsic, not technical.
- Regularization and parsimony are essential.

---

## Further reading


- Engl et al., inverse problems.
- Andersen & Piterbarg, calibration practice.
