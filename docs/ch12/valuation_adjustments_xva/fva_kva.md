# FVA and KVA

Beyond credit risk, valuation must account for **funding** and **capital** costs through Funding Valuation Adjustment (FVA) and Capital Valuation Adjustment (KVA).

---

## 1. Funding Valuation Adjustment (FVA)

FVA accounts for the cost of funding uncollateralized positions:

\[
\text{FVA} = \mathbb{E}[ \text{Funding Spread} \times \text{Funding Exposure} ].
\]



It reflects asymmetry between borrowing and lending rates.

---

## 2. Capital Valuation Adjustment (KVA)

KVA reflects the cost of holding regulatory capital:

\[
\text{KVA} = \mathbb{E}[ \text{Cost of Capital} \times \text{Required Capital} ].
\]



KVA is forward-looking and institution-specific.

---

## 3. Interactions with other XVAs

- FVA interacts with CVA/DVA through collateralization.
- KVA depends on portfolio composition and regulation.
- XVAs are not additive in general.

---

## 4. Practical implementation

Institutions must:
- model funding and capital consistently,
- avoid double counting,
- ensure governance and transparency.

---

## 5. Key takeaways

- FVA captures funding costs.
- KVA captures capital costs.
- Both extend pricing beyond pure arbitrage theory.

---

## Further reading

- Burgard & Kjaer, funding valuation.
- Green et al., XVA frameworks.
