# Parametric vs Nonparametric Learning


Statistical learning methods used in financial modeling can broadly be classified into **parametric** and **nonparametric** approaches. The distinction reflects a fundamental trade-off between structure and flexibility.

---

## Parametric learning


Parametric models assume a fixed functional form with a finite number of parameters:

\[
f(x; \theta), \quad \theta \in \mathbb{R}^d.
\]



Examples include:
- linear and generalized linear models,
- ARIMA and GARCH models,
- parametric volatility and interest-rate models.

Advantages:
- interpretability,
- data efficiency,
- stable estimation.

Limitations:
- model misspecification risk,
- limited flexibility.

---

## Nonparametric learning


Nonparametric models impose minimal structural assumptions and let data determine the functional form.

Examples include:
- kernel regression,
- splines,
- k-nearest neighbors,
- tree-based methods.

Advantages:
- high flexibility,
- ability to capture nonlinear patterns.

Limitations:
- data hungry,
- prone to overfitting,
- harder to interpret.

---

## Semi-parametric approaches


Many practical models are **semi-parametric**, combining:
- parametric structure for core dynamics,
- nonparametric components for residual effects.

This balances interpretability and flexibility.

---

## Financial modeling perspective


In finance:
- parametric models dominate risk-neutral pricing,
- nonparametric methods excel in forecasting and risk estimation,
- model choice reflects data availability and stability needs.

---

## Key takeaways


- Parametric models trade flexibility for structure.
- Nonparametric models trade structure for flexibility.
- Hybrid approaches are often most effective.

---

## Further reading


- Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*.
- McNeil et al., statistical learning in finance.
