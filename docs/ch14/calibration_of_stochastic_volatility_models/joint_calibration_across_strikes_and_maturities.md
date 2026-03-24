# Joint Calibration Across Strikes and Maturities


Stochastic volatility parameters influence the **entire implied volatility surface**. Reliable calibration therefore requires fitting **jointly across strikes and maturities**, rather than focusing on individual slices.

---

## Why joint calibration is necessary


Single-maturity calibration can:
- fit the smile locally,
- but produce inconsistent parameters across maturities.

Joint calibration enforces:
- parameter consistency,
- coherent term-structure behavior,
- improved identifiability.

---

## Objective function across the surface


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

## Surface-wide sensitivities


Parameters affect different regions:

- \(\rho\): skew across strikes,
- \(\xi\): smile curvature and term-structure interaction,
- \(\kappa, \theta\): long-maturity variance level.

Joint calibration ensures these effects are reconciled globally.

---

## Numerical considerations


- pricing speed is critical (FFT, closed forms),
- gradients/Jacobians improve optimizer robustness,
- good initial guesses reduce convergence to spurious minima.

---

## Validation


After calibration, validate by:
- checking per-maturity residual patterns,
- ensuring smooth parameter evolution over time,
- testing sensitivity to weight changes.

---

## Key takeaways


- Joint calibration improves identifiability and consistency.
- Weighting and maturity balance are as important as the model.
- Global surface fit is more meaningful than local perfection.

---

## Further reading


- Gatheral, *The Volatility Surface*.
- Lord & Kahl, efficient Heston calibration.
- Andersen & Piterbarg, multi-maturity calibration practice.

---

## Exercises

**Exercise 1.** A joint calibration objective is

$$
\mathcal{L}(\theta) = \frac{1}{2}\sum_{i,j} w_{ij}\bigl(\sigma^{\text{model}}_{\text{impl}}(k_i, T_j; \theta) - \sigma^{\text{mkt}}_{\text{impl}}(k_i, T_j)\bigr)^2
$$

Suppose the surface has 5 strikes and 4 maturities (20 data points). If the Heston model has 5 free parameters, what is the degrees-of-freedom count? Is the system over-determined, under-determined, or exactly determined? What would happen if the model had 20 free parameters instead?

---

**Exercise 2.** Explain why equal weighting across maturities can lead to the short-maturity smile dominating the calibration. If the surface has 5 strikes at each of $T = 0.08, 0.25, 0.5, 1.0$ years, and ATM implied vols are $25\%, 20\%, 18\%, 17\%$, propose a weighting scheme that balances maturities. One common choice is $w_{ij} = 1/\sigma^{\text{mkt}}(k_i, T_j)^2$. Explain the rationale.

---

**Exercise 3.** The Heston parameter $\rho$ primarily controls the skew across strikes, while $\kappa$ and $\theta$ primarily control the term structure. Design a two-stage calibration: (a) first fix $\kappa$ and $\theta$ using ATM implied volatilities across maturities; (b) then calibrate $\rho$, $\xi$, and $V_0$ to the full smile at each maturity. What advantages does this staged approach have over simultaneous optimization? What are its drawbacks?

---

**Exercise 4.** After calibrating the Heston model to the full surface, the residuals $\sigma^{\text{model}} - \sigma^{\text{mkt}}$ show a systematic pattern: the model overprices short-maturity OTM puts and underprices long-maturity ATM options. What does this pattern suggest about the model's limitations? Which additional model feature (jumps, time-dependent parameters, multi-factor volatility) would most likely address this pattern?

---

**Exercise 5.** A calibration uses 30 market quotes (6 strikes $\times$ 5 maturities) with weights proportional to open interest. The resulting RMSE in implied vol is 0.45%. If the weights are changed to be uniform, the RMSE drops to 0.38% but the longest-maturity fit deteriorates significantly. Discuss the trade-off. In a production setting for hedging vanilla options, which weighting would you prefer and why?

---

**Exercise 6.** Compare single-maturity calibration with joint calibration by considering the following experiment: calibrate the Heston model separately to each of $T = 0.25, 0.5, 1.0$ (yielding three separate parameter sets $\theta_1, \theta_2, \theta_3$) and jointly to all three maturities (yielding one parameter set $\theta_{\text{joint}}$). If the separate calibrations give $\kappa_1 = 5.0$, $\kappa_2 = 2.5$, $\kappa_3 = 1.8$, what does this variation reveal about the Heston model? Would you expect $\kappa_{\text{joint}}$ to be close to any of the individual values?
