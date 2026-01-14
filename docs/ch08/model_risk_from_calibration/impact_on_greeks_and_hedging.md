# Impact on Greeks and Hedging


Calibration error affects not only prices but also **Greeks**, which are used for hedging. Unstable or mis-specified Greeks can lead to systematic hedging losses.

---

## Greeks as model-dependent objects


Greeks are computed under the calibrated model:

\[
\Delta = \partial_S P(\hat\theta), \quad
\text{Vega} = \partial_\sigma P(\hat\theta), \; \text{etc.}
\]



If \(\hat\theta\) is unstable, Greeks inherit this instability.

---

## Sensitivity of Greeks to parameters


A second-order effect appears:

\[
\Delta_{\text{true}} - \Delta_{\text{model}}
\approx
\nabla_\theta(\partial_S P)^{\top}(\hat\theta-\theta^\star).
\]



Thus, even small parameter errors can materially distort hedge ratios.

---

## Hedging breakdown mechanisms


Common failure modes:
- frequent recalibration changes Greeks abruptly,
- hedges are adjusted to noise rather than signal,
- offsetting risks are mis-identified.

These effects are amplified in models with many weakly identifiable parameters.

---

## Robust hedging practices


Practitioners often:
- hedge with **ranges** of Greeks,
- focus on model-invariant hedges (e.g., delta-neutralization),
- stress-test hedges under alternative calibrations,
- use simpler proxy models for risk management.

---

## Key takeaways


- Greeks are highly sensitive to calibration quality.
- Hedging based on unstable parameters is fragile.
- Robust hedging requires acknowledging model uncertainty.

---

## Further reading


- Taleb, *Dynamic Hedging*.
- Cont & Tankov, discussions on model risk and Greeks.
