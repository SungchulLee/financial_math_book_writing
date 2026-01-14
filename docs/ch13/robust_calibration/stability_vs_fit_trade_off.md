# Stability vs Fit Trade-Off


Robust calibration highlights a fundamental **trade-off between stability and fit**, analogous to the bias–variance trade-off in statistics.

---

## The trade-off


- Tight fit to data reduces in-sample error.
- Excessive fit amplifies noise and instability.

Robust calibration deliberately sacrifices fit for stability.

---

## Overfitting in calibration


Overfitting leads to:
- unstable parameter estimates,
- poor out-of-sample pricing,
- exaggerated hedging errors.

This is especially severe with ill-posed inverse problems.

---

## Robustness as regularization


Robust calibration acts as:
- implicit regularization,
- constraint on parameter variability,
- control of sensitivity to data perturbations.

It complements classical regularization methods.

---

## Choosing the balance


The stability–fit balance depends on:
- intended model use (pricing vs hedging),
- market liquidity,
- risk tolerance and governance.

There is no universally optimal choice.

---

## Key takeaways


- Stability and fit cannot both be maximized.
- Robust calibration favors reliability.
- The trade-off must be explicitly managed.

---

## Further reading


- Tikhonov regularization.
- Glasserman, calibration stability.
