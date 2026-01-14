# Valuation Adjustments


Credit derivatives pricing in practice requires **valuation adjustments** that go beyond idealized default models. These adjustments reflect counterparty risk, funding costs, and collateralization.

---

## Motivation for adjustments


Classical pricing assumes:
- default-free counterparties,
- frictionless funding,
- perfect collateralization.

Real markets violate these assumptions.

---

## Credit Valuation Adjustment (CVA)


**CVA** accounts for counterparty default risk:

\[
\text{CVA} = \mathbb{E}[\text{Exposure} \times \text{Loss Given Default}].
\]



It reduces the value of a derivative due to counterparty credit risk.

---

## Other XVA components


Common adjustments include:
- **DVA:** own default risk,
- **FVA:** funding costs,
- **MVA:** margin valuation adjustment.

Together, these are known as **XVA**.

---

## Interaction with CDS pricing


For CDS:
- counterparty risk affects premium valuation,
- collateral agreements mitigate but do not eliminate XVA,
- standardized CDS reduce some complexity.

---

## Key takeaways


- Valuation adjustments are essential for realistic pricing.
- CVA, DVA, and FVA materially affect values.
- Modern pricing integrates XVA into credit models.

---

## Further reading


- Gregory, *Counterparty Credit Risk*.
- Brigo, Morini & Pallavicini, XVA theory.
