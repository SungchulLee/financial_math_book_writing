# Volatility Risk Premium

Option prices are quoted under the **risk-neutral measure**, while volatility dynamics observed in time series reflect the **physical measure**. The difference is captured by the **volatility risk premium (VRP)**, which plays a central role in stochastic volatility calibration and interpretation.

---

## 1. Physical vs risk-neutral dynamics

Under the physical measure \(\mathbb{P}\), variance may follow
\[
dV_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - V_t)dt + \xi\sqrt{V_t}\,dW_t^{V,\mathbb{P}}.
\]

Under the risk-neutral measure \(\mathbb{Q}\), used for pricing,
\[
dV_t = \kappa^{\mathbb{Q}}(\theta^{\mathbb{Q}} - V_t)dt + \xi\sqrt{V_t}\,dW_t^{V,\mathbb{Q}}.
\]

The parameters generally differ.

---

## 2. Definition of the volatility risk premium

The VRP can be expressed as a change of drift:
\[
\lambda_V(V_t) = \kappa^{\mathbb{Q}}(\theta^{\mathbb{Q}} - V_t)
- \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - V_t).
\]

Economically, it compensates investors for bearing volatility risk.

---

## 3. Implications for calibration

Calibration to option prices identifies **risk-neutral parameters** only:
- \(\kappa^{\mathbb{Q}}, \theta^{\mathbb{Q}}\),
- not the physical dynamics observed in realized variance.

This explains why:
- option-implied mean reversion differs from historical estimates,
- naive mixing of historical and option calibration leads to inconsistencies.

---

## 4. Joint use of historical data

Some workflows combine:
- option calibration (risk-neutral),
- time-series calibration of variance (physical).

This requires:
- an explicit VRP model,
- consistency constraints between measures,
- careful statistical treatment.

Without this, identifiability can worsen rather than improve.

---

## 5. Market evidence

Empirically:
- variance risk premia are typically negative (investors pay for crash protection),
- option-implied variance exceeds realized variance on average.

These stylized facts justify allowing significant separation between
\(\mathbb{P}\) and \(\mathbb{Q}\) parameters.

---

## 6. Key takeaways

- Option calibration identifies risk-neutral dynamics.
- The volatility risk premium explains discrepancies with historical estimates.
- Mixing measures without a VRP model leads to misinterpretation.

---

## Further reading

- Bollerslev et al., “Expected Stock Returns and Variance Risk Premia”.
- Carr & Wu, variance risk premium studies.
- Andersen & Piterbarg, volatility modeling practice.
