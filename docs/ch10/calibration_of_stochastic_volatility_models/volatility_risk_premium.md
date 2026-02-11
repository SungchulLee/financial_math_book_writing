# Volatility Risk Premium


Stochastic volatility models distinguish between **risk-neutral** and **physical** volatility dynamics. The gap between them is captured by the **volatility risk premium (VRP)**, which has direct implications for calibration and interpretation.

---

## Risk-neutral calibration


Option prices identify parameters under the risk-neutral measure \(\mathbb{Q}\).
These parameters reflect:
- investor risk preferences,
- compensation for unhedgeable volatility risk.

They should not be confused with historical estimates.

---

## Physical dynamics


Historical time-series analysis estimates parameters under the physical measure \(\mathbb{P}\).
Empirically:
- realized volatility is lower than option-implied variance,
- volatility shocks earn negative premia.

---

## Implications for calibration


Mixing \(\mathbb{P}\) and \(\mathbb{Q}\) parameters without modeling VRP leads to:

- inconsistent dynamics,
- misleading economic interpretation,
- degraded calibration stability.

Calibration should be measure-consistent.

---

## Joint modeling approaches


Advanced frameworks introduce:
- explicit VRP processes,
- joint estimation using options and realized variance,
- Bayesian separation of measures.

These improve interpretability but increase complexity.

---

## Key takeaways


- Volatility risk premium explains discrepancies between historical and implied volatility.
- Option calibration recovers risk-neutral dynamics only.
- Measure consistency is essential.

---

## Further reading


- Bollerslev et al., variance risk premium.
- Carr & Wu, volatility premia.
