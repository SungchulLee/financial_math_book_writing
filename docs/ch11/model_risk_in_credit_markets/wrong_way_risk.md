# Wrong-Way Risk

**Wrong-way risk (WWR)** arises when exposure to a counterparty increases precisely when the counterparty’s credit quality deteriorates. It is a major source of model risk in credit markets.

---

## 1. Definition

Wrong-way risk occurs when:
- exposure and default risk are positively correlated,
- losses are amplified during adverse market conditions.

The opposite case is **right-way risk**, where exposure decreases as credit risk increases.

---

## 2. Examples

Typical examples include:
- interest-rate swaps with leveraged counterparties,
- FX derivatives where currency depreciation weakens the counterparty,
- CDS written on correlated reference entities.

WWR is most severe during market stress.

---

## 3. Modeling challenges

Standard intensity models often assume:
- independence between exposure and default,
- constant or exogenous intensities.

These assumptions underestimate tail losses when WWR is present.

---

## 4. Practical mitigation

Mitigation techniques include:
- conservative exposure modeling,
- stressed CVA calculations,
- explicit dependence between market factors and intensity.

Regulatory frameworks require explicit WWR consideration.

---

## 5. Key takeaways

- Wrong-way risk amplifies credit losses.
- Independence assumptions are dangerous.
- Stress-based modeling is essential.

---

## Further reading

- Gregory, *Counterparty Credit Risk*.
- Basel III CVA guidance.
