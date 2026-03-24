# Stress and Crisis Behavior


Credit models calibrated in normal markets often fail during **stress and crisis periods**. Understanding these breakdowns is central to credit model risk.

---

## Regime dependence


During crises:
- default intensities jump,
- correlations spike,
- liquidity evaporates.

Static models cannot capture these regime shifts.

---

## Model breakdown mechanisms


Common failure modes include:
- extrapolation beyond calibration data,
- frozen liquidity invalidating market prices,
- violated independence assumptions.

Models appear stable until stress occurs.

---

## Stress testing


Robust credit risk management relies on:
- scenario analysis,
- extreme but plausible stresses,
- reverse stress testing.

Stress tests complement, not replace, models.

---

## Lessons from crises


Historical crises show:
- tail risk dominates averages,
- diversification benefits vanish,
- conservative assumptions outperform complex models.

---

## Key takeaways


- Crisis behavior differs qualitatively from normal markets.
- Stress testing is indispensable.
- Model humility is essential in credit markets.

---

## Further reading


- BIS, stress testing frameworks.
- Cont, model uncertainty and crises.

---

## Exercises

**Exercise 1.** A credit model is calibrated to CDS spreads during a period when the average BBB spread is 120 bp. During a crisis, spreads widen to 500 bp. Explain why simply re-calibrating the model to crisis spreads may not be sufficient. What structural features of the model (e.g., constant correlation, fixed recovery) might break down?

---

**Exercise 2.** Describe three specific mechanisms through which credit models fail during stress periods. For each mechanism, provide a concrete example from the 2008 financial crisis or the 2020 COVID-19 market disruption.

---

**Exercise 3.** A risk manager conducts a stress test by shifting all default intensities up by a factor of 3 while keeping correlations constant. Explain why this "parallel shift" stress test may underestimate portfolio credit losses. What additional stressed parameters should be considered?

---

**Exercise 4.** Define reverse stress testing. For a portfolio of 50 investment-grade corporate bonds, describe how you would implement a reverse stress test to find the minimum set of conditions (e.g., default rate, correlation, recovery) that would cause a 10% portfolio loss.

---

**Exercise 5.** During the 2008 crisis, diversification benefits "vanished" for many credit portfolios. Explain this phenomenon using the concept of correlation regime switching. If pre-crisis correlation is $\rho = 15\%$ and crisis correlation is $\rho = 50\%$, describe qualitatively how the portfolio loss distribution changes.

---

**Exercise 6.** Compare the effectiveness of three stress testing approaches for credit portfolios: (a) historical simulation using past crisis data, (b) hypothetical scenario analysis, and (c) model-based stressed calibration. For each approach, discuss strengths, weaknesses, and the types of risks it can and cannot capture.
