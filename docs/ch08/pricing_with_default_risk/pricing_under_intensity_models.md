# Pricing under Intensity Models

Intensity-based models provide tractable pricing formulas for defaultable claims by modeling default via a hazard rate process.

---

## 1. Pricing framework

Assume:
- default intensity \(\lambda_t\),
- recovery scheme specified,
- immersion and progressive enlargement hold.

Pricing reduces to computing discounted expectations involving survival probabilities.

---

## 2. Defaultable zero-coupon bond

Under recovery of treasury (RT), the price simplifies to
\[
P^d(t,T)
= \mathbb{E}^{\mathbb{Q}}\left[
\exp\left(-\int_t^T (r_s + \lambda_s) ds\right)
\middle| \mathcal{F}_t
\right].
\]

Default risk acts like an additional discount rate.

---

## 3. General recovery case

With recovery of face value or market value, pricing involves:
- integrals over default times,
- survival probabilities,
- expected recovery payments.

Closed forms exist for simple intensity models.

---

## 4. Relation to CDS pricing

The same framework prices:
- credit default swaps (premium vs protection legs),
- risky bonds and loans,
- credit-linked notes.

Consistency across products is essential.

---

## 5. Key takeaways

- Intensity models yield tractable pricing formulas.
- Default risk enters through survival probabilities.
- Recovery assumptions must be consistent across instruments.

---

## Further reading

- Duffie & Singleton, intensity-based pricing.
- Brigo et al., credit derivatives pricing.
