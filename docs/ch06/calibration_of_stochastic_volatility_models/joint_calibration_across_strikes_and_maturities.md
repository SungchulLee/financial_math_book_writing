# Joint Calibration Across Strikes and Maturities

Stochastic volatility parameters influence the **entire implied volatility surface**. Reliable calibration therefore requires fitting **jointly across strikes and maturities**, rather than focusing on individual slices.

---

## 1. Why joint calibration is necessary

Single-maturity calibration can:
- fit the smile locally,
- but produce inconsistent parameters across maturities.

Joint calibration enforces:
- parameter consistency,
- coherent term-structure behavior,
- improved identifiability.

---

## 2. Objective function across the surface

A typical joint objective is
\[
\mathcal{L}(\theta)
= \frac12\sum_{i,j} w_{ij}
\big(\sigma^{\text{model}}_{\text{impl}}(k_i,T_j;\theta)
- \sigma^{\text{mkt}}_{\text{impl}}(k_i,T_j)\big)^2.
\]

Key design choices:
- maturity balancing (avoid one tenor dominating),
- liquidity-based weights,
- exclusion of unreliable wings.

---

## 3. Surface-wide sensitivities

Parameters affect different regions:

- \(\rho\): skew across strikes,
- \(\xi\): smile curvature and term-structure interaction,
- \(\kappa, \theta\): long-maturity variance level.

Joint calibration ensures these effects are reconciled globally.

---

## 4. Numerical considerations

- pricing speed is critical (FFT, closed forms),
- gradients/Jacobians improve optimizer robustness,
- good initial guesses reduce convergence to spurious minima.

---

## 5. Validation

After calibration, validate by:
- checking per-maturity residual patterns,
- ensuring smooth parameter evolution over time,
- testing sensitivity to weight changes.

---

## 6. Key takeaways

- Joint calibration improves identifiability and consistency.
- Weighting and maturity balance are as important as the model.
- Global surface fit is more meaningful than local perfection.

---

## Further reading

- Gatheral, *The Volatility Surface*.
- Lord & Kahl, efficient Heston calibration.
- Andersen & Piterbarg, multi-maturity calibration practice.
