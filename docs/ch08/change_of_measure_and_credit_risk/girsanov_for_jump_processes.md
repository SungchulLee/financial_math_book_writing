# Girsanov for Jump Processes

Girsanov’s theorem extends beyond diffusions to **jump processes**, providing the mathematical foundation for changing measures in credit risk models.

---

## 1. Jumps and compensators

Default is modeled as a jump process with compensator
\[
A_t = \int_0^{t \wedge \tau} \lambda_s ds.
\]

Under a measure change, both the compensator and intensity may change.

---

## 2. Girsanov theorem for jumps

Girsanov’s theorem states that, under suitable integrability conditions:
- the compensated jump process remains a martingale,
- the intensity transforms multiplicatively or additively.

This generalizes the drift adjustment in diffusion models.

---

## 3. Application to default modeling

In credit models:
- the likelihood of default paths is reweighted,
- jump intensities reflect risk premia,
- pricing formulas remain tractable.

This formalism justifies using different intensities under \(\mathbb{P}\) and \(\mathbb{Q}\).

---

## 4. Combined diffusion–jump models

Many models include:
- diffusive market factors,
- jump-to-default components.

Girsanov’s theorem applies jointly to both parts.

---

## 5. Key takeaways

- Girsanov extends to jump processes.
- Default intensities change under measure change.
- This underpins risk-neutral credit pricing.

---

## Further reading

- Jacod & Shiryaev, jump processes.
- Cont & Tankov, financial modeling with jumps.
