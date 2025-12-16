# Measure Changes with Default

Changing probability measures in the presence of default requires special care because default introduces **jumps** and filtration enlargement.

---

## 1. Measure change framework

Let \(\mathbb{Q}\) and \(\mathbb{P}\) be equivalent measures on the enlarged filtration \((\mathcal{G}_t)\).
The Radon–Nikodym derivative must account for:
- diffusion risks,
- jump-to-default risk.

---

## 2. Effect on intensities

Under a change of measure, the default intensity transforms as

\[
\lambda_t^{\mathbb{Q}} = \lambda_t^{\mathbb{P}} + \theta_t,
\]


where \(\theta_t\) reflects the market price of default risk.

This parallels drift changes in diffusion models.

---

## 3. Martingale preservation

For pricing, discounted asset prices must remain martingales under the chosen measure.
This imposes consistency conditions linking:
- compensators,
- measure changes,
- recovery assumptions.

---

## 4. Practical relevance

Measure changes with default are crucial for:
- linking historical default models to pricing models,
- joint equity–credit modeling,
- stress testing and scenario analysis.

---

## 5. Key takeaways

- Measure changes affect default intensities.
- Jump risk requires special treatment.
- Consistency is essential for arbitrage-free pricing.

---

## Further reading

- Jeanblanc & Rutkowski, measure changes with default.
- Elliott et al., hidden default intensity models.
