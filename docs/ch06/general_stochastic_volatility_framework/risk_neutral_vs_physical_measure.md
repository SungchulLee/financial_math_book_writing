# Risk-Neutral vs Physical Measure

Stochastic volatility models distinguish between **physical (real-world)** dynamics and **risk-neutral** dynamics used for pricing. Understanding this distinction is essential for calibration and interpretation.

---

## 1. Two probability measures

- **Physical measure (\(\mathbb{P}\))**: governs actual asset evolution.
- **Risk-neutral measure (\(\mathbb{Q}\))**: used for pricing via discounted expectations.

Option prices identify \(\mathbb{Q}\)-dynamics only.

---

## 2. Measure change and drifts

A change of measure modifies drifts but not diffusion terms:

\[
dV_t^{\mathbb{Q}} = a^{\mathbb{Q}}(V_t)dt + b(V_t)dW_t^{V,\mathbb{Q}}.
\]



The difference between \(a^{\mathbb{P}}\) and \(a^{\mathbb{Q}}\) encodes **risk premia**.

---

## 3. Volatility risk premium

Because volatility risk is unhedgeable:
- investors demand compensation,
- volatility risk premium emerges naturally,
- \(\mathbb{P}\) and \(\mathbb{Q}\) parameters differ.

This explains discrepancies between historical and implied volatility behavior.

---

## 4. Calibration implications

- option calibration recovers \(\mathbb{Q}\)-parameters,
- time-series estimation recovers \(\mathbb{P}\)-parameters,
- mixing them without a model for the risk premium leads to inconsistency.

---

## 5. Key takeaways

- Pricing and historical dynamics live under different measures.
- Risk premia are central in stochastic volatility models.
- Calibration must respect the measure distinction.

---

## Further reading

- Duffie, *Dynamic Asset Pricing Theory*.
- Fouque et al., stochastic volatility and asymptotics.
- Andersen & Piterbarg, volatility modeling practice.
