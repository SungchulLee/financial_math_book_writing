# Trade-Off Between Fit and Robustness


Regularization introduces an unavoidable **trade-off**: improving robustness and stability typically worsens in-sample fit. Understanding and managing this trade-off is central to practical calibration.

---

## Bias–variance trade-off


Regularization reduces variance at the cost of bias:

- **Low regularization:** excellent fit, poor stability.
- **High regularization:** stable parameters, biased fit.

The optimal point depends on data quality, model purpose, and downstream use (pricing vs hedging).

---

## Diagnostics for the trade-off


Useful diagnostics include:

- **Residual plots:** detect systematic misfit patterns.
- **Parameter paths:** track parameters as regularization increases.
- **Stability tests:** re-calibrate under perturbed data.
- **Out-of-sample instruments:** test predictive power.

---

## Economic versus statistical fit


A statistically optimal fit may be economically undesirable:

- parameters may imply implausible dynamics,
- hedging Greeks may be unstable,
- scenario sensitivities may explode.

Robust calibration prioritizes *economic behavior* over minimal residuals.

---

## Time stability as a criterion


In practice, many desks judge calibration quality by:

- day-to-day parameter stability,
- smooth evolution over time,
- absence of large jumps without market justification.

This implicitly favors stronger regularization than pure in-sample metrics.

---

## Choosing robustness deliberately


Guiding principles:
- start with strong regularization,
- relax only when justified by stable, liquid data,
- prefer bias you understand to variance you cannot hedge.

---

## Key takeaways


- Perfect fit is not the goal; *robust behavior* is.
- Regularization controls the fit–robustness balance.
- Stability across time and scenarios is often the decisive metric.

---

## Further reading


- Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*.
- Tarantola, *Inverse Problem Theory*.
- Andersen & Piterbarg, practitioner discussions on calibration stability.
