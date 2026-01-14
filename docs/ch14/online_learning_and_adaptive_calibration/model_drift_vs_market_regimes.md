# Model Drift vs Market Regimes


Adaptive calibration must distinguish between **model drift** and genuine **market regime changes**, a key challenge in online learning.

---

## Model drift


Model drift refers to:
- gradual parameter changes,
- slow evolution of market dynamics,
- continuous adaptation being appropriate.

Sequential estimators handle drift naturally.

---

## Market regimes


Market regimes involve:
- abrupt structural changes,
- shifts in volatility, correlations, or liquidity,
- breakdown of historical relationships.

Regimes require discrete model adjustments.

---

## Detection challenges


Distinguishing drift from regime change is difficult because:
- both affect parameter estimates,
- noise obscures signals,
- delayed detection is common.

Statistical tests and filters provide partial solutions.

---

## Practical approaches


Common approaches include:
- regime-switching models,
- forgetting factors and adaptive gains,
- model ensembles and resets.

Human oversight remains essential.

---

## Key takeaways


- Drift and regimes require different responses.
- Online learning must balance adaptation and stability.
- Governance complements automation.

---

## Further reading


- Hamilton, regime-switching models.
- Cont, model instability in finance.
