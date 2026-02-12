# Risk-Neutral vs Physical Intensities


In credit risk modeling, default intensities differ under the **risk-neutral measure** \(\mathbb{Q}\) and the **physical measure** \(\mathbb{P}\). Understanding this distinction is essential for interpreting calibrated parameters.

---

## Two measures, two roles


- **Physical measure \(\mathbb{P}\):**
  governs real-world default frequencies and risk management.
- **Risk-neutral measure \(\mathbb{Q}\):**
  governs pricing and is inferred from market instruments (e.g. CDS).

The two intensities generally differ due to risk premia.

---

## Intensity decomposition


A common representation is

\[
\lambda_t^{\mathbb{Q}} = \lambda_t^{\mathbb{P}} + \text{credit risk premium}.
\]



The premium compensates investors for bearing default risk.

---

## Empirical implications


Empirically:
- \(\lambda^{\mathbb{Q}}\) implied from CDS is typically higher,
- historical default frequencies underestimate market-implied risk,
- stress periods amplify the gap.

Thus, CDS-implied intensities should not be interpreted as real default probabilities.

---

## Modeling approaches


Common approaches include:
- specifying \(\lambda^{\mathbb{P}}\) and adding a market price of risk,
- directly modeling \(\lambda^{\mathbb{Q}}\) for pricing,
- joint estimation using market and historical data.

---

## Key takeaways


- Risk-neutral and physical intensities differ.
- The gap reflects default risk premia.
- Measure consistency is crucial for interpretation.

---

## Further reading


- Duffie & Singleton, risk premia in credit.
- Bielecki & Rutkowski, measure changes in credit models.
