# CVA and DVA


**Credit Valuation Adjustment (CVA)** and **Debit Valuation Adjustment (DVA)** account for counterparty and own default risk in derivative pricing.

---

## Credit Valuation Adjustment (CVA)


CVA reflects the expected loss due to counterparty default:

\[
\text{CVA}
= \mathbb{E}[ \text{Exposure} \times \text{LGD} \times \mathbf{1}_{\{\text{counterparty defaults}\}} ].
\]



It reduces the value of a derivative from the bank’s perspective.

---

## Debit Valuation Adjustment (DVA)


DVA reflects the benefit arising from the bank’s own default risk:

\[
\text{DVA}
= \mathbb{E}[ \text{Negative Exposure} \times \text{LGD}_{\text{own}} ].
\]



Economically controversial, DVA can increase reported profits as credit quality worsens.

---

## Net valuation adjustment


In practice:

\[
V_{\text{adjusted}} = V_{\text{risk-free}} - \text{CVA} + \text{DVA}.
\]



Accounting and regulatory treatments differ across jurisdictions.

---

## Modeling considerations


Key drivers include:
- exposure profiles,
- default intensities,
- recovery assumptions,
- netting and collateral.

---

## Key takeaways


- CVA reflects counterparty credit risk.
- DVA reflects own default risk.
- Both materially affect derivative values.

---

## Further reading


- Gregory, *Counterparty Credit Risk*.
- Brigo et al., CVA/DVA theory.
