# Potential Future Exposure (PFE)


**Potential Future Exposure (PFE)** measures the worst-case exposure at a given confidence level, complementing average exposure measures.

---

## Definition


For confidence level \(\alpha\),

\[
\text{PFE}_{\alpha}(t)
= \inf\{x : \mathbb{P}(E_t \le x) \ge \alpha\}.
\]



PFE is a quantile of the exposure distribution.

---

## Interpretation


A statement such as:
> “The 95% PFE at 1 year is 20 million”
means exposure exceeds 20 million with only 5% probability.

PFE focuses on tail exposure rather than averages.

---

## Relation to EE


- EE measures average exposure.
- PFE measures extreme but plausible exposure.
- Both are required for risk limits and capital.

PFE is not additive across portfolios.

---

## Computation


PFE is typically computed via:
- Monte Carlo simulation,
- scenario generation under market dynamics,
- incorporation of netting and collateral.

Model assumptions strongly influence PFE.

---

## Key takeaways


- PFE is a high-quantile exposure measure.
- It complements Expected Exposure.
- Tail modeling accuracy is critical.

---

## Further reading


- Basel CCR capital framework.
- Glasserman, Monte Carlo exposure models.
