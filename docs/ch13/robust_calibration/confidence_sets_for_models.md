# Confidence Sets for Models

In robust calibration, model parameters are not treated as point estimates but as belonging to **confidence sets** reflecting statistical uncertainty.

---

## 1. Motivation

Market data is:
- noisy,
- sparse in some regions,
- subject to microstructure effects.

Point calibration often overfits noise. Confidence sets provide uncertainty awareness.

---

## 2. Construction of confidence sets

Confidence sets can be built using:
- asymptotic likelihood theory,
- bootstrap methods,
- moment-based inequalities.

They define a family of models statistically consistent with observed data.

---

## 3. Interpretation

A confidence set represents:
- plausible parameter values,
- estimation error bounds,
- regions of model ambiguity.

Robust decisions hedge against all models in the set.

---

## 4. Financial relevance

Confidence-set calibration is used in:
- option surface fitting,
- interest-rate model calibration,
- stress testing and risk management.

It improves stability under data perturbations.

---

## 5. Key takeaways

- Parameters should be treated as uncertain.
- Confidence sets formalize estimation risk.
- Robust calibration improves reliability.

---

## Further reading

- Hansen, robust inference.
- Andrews, confidence sets under misspecification.
