# Model Drift vs Parameter Drift


Observed parameter changes over time can stem from two fundamentally different sources: **model drift** and **parameter drift**. Distinguishing between them is crucial for interpretation and risk management.

---

## Parameter drift


**Parameter drift** occurs when:
- model parameters are treated as time-dependent,
- recalibration reflects evolving market conditions.

Examples:
- changing long-run variance,
- evolving skew preferences.

Parameter drift can be modeled explicitly but undermines static model interpretation.

---

## Model drift


**Model drift** arises when:
- the true market dynamics lie outside the model class,
- calibration compensates by shifting parameters.

In this case:
- parameters drift to absorb misspecification,
- calibrated values lose structural meaning.

---

## Diagnosing the difference


Indicators of model drift:
- systematic parameter trends across regimes,
- instability even with heavy regularization,
- poor out-of-sample performance.

Indicators of parameter drift:
- smooth evolution aligned with macro/market events,
- improved fit from explicit time-dependence.

---

## Risk management implications


- Parameter drift requires dynamic hedging adjustments.
- Model drift suggests the model should be replaced or extended.
- Confusing the two leads to mispriced risk and fragile hedges.

---

## Key takeaways


- Not all parameter changes mean the same thing.
- Model drift signals misspecification.
- Parameter drift can be modeled but reduces parsimony.

---

## Further reading


- Rebonato, *Volatility and Correlation*.
- Cont, *Model Uncertainty and Its Impact on Pricing*.
- Andersen & Piterbarg, dynamic calibration practice.
