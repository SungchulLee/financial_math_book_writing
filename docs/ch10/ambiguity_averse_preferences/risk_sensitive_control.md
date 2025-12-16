# Risk-Sensitive Control

**Risk-sensitive control** extends stochastic control by explicitly penalizing uncertainty and variability in outcomes, closely related to ambiguity-averse preferences.

---

## 1. Classical vs risk-sensitive control

Classical control maximizes expected payoff:

\[
\max \mathbb{E}[X].
\]



Risk-sensitive control maximizes:

\[
\max \; \mathbb{E}\left[ -\exp(-\theta X) \right],
\]


or equivalent exponential criteria.

---

## 2. Interpretation

Risk-sensitive control:
- penalizes downside risk,
- amplifies tail outcomes,
- reflects aversion to uncertainty.

It is more conservative than risk-neutral control.

---

## 3. Connection to entropy penalization

Risk-sensitive control is equivalent to:
- robust control with entropy penalties,
- exponential utility maximization.

This links ambiguity aversion to control theory.

---

## 4. Financial applications

Applications include:
- portfolio optimization under uncertainty,
- robust hedging,
- dynamic risk management.

The resulting controls are smoother and more conservative.

---

## 5. Key takeaways

- Risk-sensitive control penalizes uncertainty.
- It connects utility, entropy, and robustness.
- Widely used in robust finance and engineering.

---

## Further reading

- Jacobson, risk-sensitive control.
- Fleming & McEneaney, robust control.
