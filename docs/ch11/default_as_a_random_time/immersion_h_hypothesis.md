# Immersion (H-Hypothesis)


The **immersion property**, also called the **H-hypothesis**, is a key assumption in credit risk models relating martingales under different filtrations.

---

## Definition of the H-hypothesis


Given filtrations \((\mathcal{F}_t)\subseteq(\mathcal{G}_t)\), immersion holds if:

\[
\text{every } (\mathcal{F}_t, \mathbb{Q})\text{-martingale is also a }(\mathcal{G}_t, \mathbb{Q})\text{-martingale}.
\]



This ensures consistency of martingale properties after enlargement.

---

## Interpretation in credit risk


If immersion holds:
- market prices remain martingales after including default information,
- no additional drift terms appear due to filtration enlargement,
- pricing formulas remain tractable.

This is a strong but convenient assumption.

---

## Relation to intensity models


In reduced-form (intensity-based) models:
- immersion often holds by construction,
- default is conditionally independent of market factors given intensity,
- hazard rates drive default probabilities.

This supports clean separation of market and credit risk.

---

## When immersion fails


If immersion does not hold:
- additional compensator terms appear,
- default may convey information about market factors,
- pricing becomes more complex.

Structural models often violate immersion.

---

## Key takeaways


- Immersion preserves martingale properties after enlargement.
- It simplifies pricing and hedging in credit models.
- It is natural in reduced-form but not structural models.

---

## Further reading


- Jeanblanc & Le Cam, immersion in credit risk.
- Elliott et al., hidden Markov default models.
