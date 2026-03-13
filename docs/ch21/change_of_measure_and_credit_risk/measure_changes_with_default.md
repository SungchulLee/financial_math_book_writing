# Measure Changes with Default


Changing probability measures in the presence of default requires special care because default introduces **jumps** and filtration enlargement.

---

## Measure change framework


Let \(\mathbb{Q}\) and \(\mathbb{P}\) be equivalent measures on the enlarged filtration \((\mathcal{G}_t)\).
The Radon–Nikodym derivative must account for:
- diffusion risks,
- jump-to-default risk.

---

## Effect on intensities


Under a change of measure, the default intensity transforms as

\[
\lambda_t^{\mathbb{Q}} = \lambda_t^{\mathbb{P}} + \theta_t,
\]


where \(\theta_t\) reflects the market price of default risk.

This parallels drift changes in diffusion models.

---

## Martingale preservation


For pricing, discounted asset prices must remain martingales under the chosen measure.
This imposes consistency conditions linking:
- compensators,
- measure changes,
- recovery assumptions.

---

## Practical relevance


Measure changes with default are crucial for:
- linking historical default models to pricing models,
- joint equity–credit modeling,
- stress testing and scenario analysis.

---

## Key takeaways


- Measure changes affect default intensities.
- Jump risk requires special treatment.
- Consistency is essential for arbitrage-free pricing.

---

## Further reading


- Jeanblanc & Rutkowski, measure changes with default.
- Elliott et al., hidden default intensity models.
