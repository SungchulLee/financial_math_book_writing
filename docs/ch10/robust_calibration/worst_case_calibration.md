# Worst-Case Calibration

**Worst-case calibration** selects model parameters that perform acceptably under the most adverse plausible market scenarios.

---

## 1. Concept

Instead of minimizing average error, worst-case calibration solves:
\[
\min_{\theta} \; \max_{m \in \mathcal{M}} \text{Error}(\theta, m),
\]
where \(\mathcal{M}\) represents admissible market perturbations.

This emphasizes robustness over best fit.

---

## 2. Relation to robust optimization

Worst-case calibration:
- mirrors max–min optimization,
- aligns with ambiguity-averse preferences,
- guards against overfitting.

It is conservative by design.

---

## 3. Practical implementation

Approaches include:
- penalty methods,
- scenario-based calibration,
- adversarial perturbations of data.

Computational cost is higher than classical calibration.

---

## 4. Benefits and limitations

Benefits:
- stable parameters,
- resilience to noise.

Limitations:
- potentially lower in-sample accuracy,
- increased conservatism.

---

## 5. Key takeaways

- Worst-case calibration prioritizes stability.
- It protects against adverse data realizations.
- Conservatism is a deliberate choice.

---

## Further reading

- Ben-Tal et al., robust optimization.
- Cont, robust calibration.
