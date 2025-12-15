# Stability of Calibration

Beyond fit quality, a calibration must be **stable**: small changes in market data should not cause large parameter shifts. Stability is a central criterion for production models.

---

## 1. Sources of instability

Calibration instability arises from:

- ill-posed inverse problems,
- weakly identifiable parameters,
- noisy or illiquid quotes,
- overly flexible objectives.

These factors interact nonlinearly.

---

## 2. Measuring stability

Common stability checks include:

- re-calibration under perturbed quotes,
- rolling-window calibration,
- monitoring parameter time series,
- comparing alternative weighting schemes.

Stability should be assessed across market regimes.

---

## 3. Regularization and constraints

Stability is improved by:

- regularization (penalties, priors),
- economically motivated bounds,
- reduced parameterization,
- maturity-balanced objectives.

These reduce variance at the cost of bias.

---

## 4. Practical acceptance criteria

In practice, desks often require:

- smooth parameter evolution over time,
- limited sensitivity to individual quotes,
- consistent pricing of benchmark instruments.

A slightly worse fit is often acceptable if stability improves.

---

## 5. Key takeaways

- Stability is as important as in-sample accuracy.
- Regularization is essential in stochastic volatility calibration.
- Calibration quality must be judged dynamically, not pointwise.

---

## Further reading

- Rebonato, *Volatility and Correlation*.
- Andersen & Piterbarg, calibration stability discussions.
