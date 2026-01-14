# Recalibration Problem


In practice, models are recalibrated repeatedly as new market data arrive. This creates the **recalibration problem**: parameters change over time in ways that may be inconsistent with the model’s own dynamics, leading to instability and hedging errors.

---

## Static calibration versus dynamic usage


A model calibrated at time \(t\) is typically used to:
- price instruments at time \(t\),
- hedge positions over \([t, t+\Delta t]\).

If the model is recalibrated at \(t+\Delta t\) to new data, the parameter shift

\[
\theta_t \longrightarrow \theta_{t+\Delta t}
\]


can introduce artificial P&L unrelated to market moves.

---

## Sources of recalibration instability


Parameter changes arise from:
- genuine market regime shifts,
- noise in quotes and surface construction,
- model misspecification,
- ill-posed calibration objectives.

Because calibration is an inverse problem, small data changes can produce large parameter jumps.

---

## Impact on hedging and P&L


Frequent recalibration can:
- break self-financing hedging arguments,
- generate unexplained P&L,
- invalidate Greeks computed from yesterday’s parameters.

This is particularly severe for models with many weakly identifiable parameters.

---

## Common practitioner responses


Typical (ad-hoc) responses include:
- smoothing parameters over time,
- freezing selected parameters,
- recalibrating only part of the surface,
- switching models across regimes.

While pragmatic, these approaches often lack theoretical consistency.

---

## Key takeaways


- Recalibration is unavoidable but problematic.
- Parameter jumps are not always economically meaningful.
- Addressing recalibration requires time-consistent modeling (next sections).

---

## Further reading


- Rebonato, *Volatility and Correlation*.
- Andersen & Piterbarg, practitioner discussions on recalibration risk.
