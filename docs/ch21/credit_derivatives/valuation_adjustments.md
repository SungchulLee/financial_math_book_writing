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

---

## Exercises

**Exercise 1.** A bank enters a 5-year interest rate swap with a counterparty whose 5-year CDS spread is 200 bp and recovery rate is $R = 40\%$. The expected positive exposure (EPE) of the swap is estimated at \$5 million. Using the simplified unilateral CVA formula

$$
\text{CVA} \approx (1 - R) \times \text{Spread} \times \text{EPE} \times T
$$

compute the approximate CVA. Explain why this adjustment reduces the swap's value to the bank.

---

**Exercise 2.** Explain the economic meaning of Debit Valuation Adjustment (DVA). A bank with a 5-year CDS spread of 100 bp computes its DVA on a derivative portfolio. Why is DVA sometimes criticized as a "benefit from own deterioration"? Discuss whether DVA should be included in the bank's reported P&L.

---

**Exercise 3.** A fully collateralized CDS with daily margining has near-zero CVA. Explain why. Then describe a scenario where residual CVA remains even with collateralization (e.g., gap risk, margin period of risk). How does the margin period of risk affect the CVA calculation?

---

**Exercise 4.** Funding Valuation Adjustment (FVA) arises when a derivative's collateral requirements generate funding costs above the risk-free rate. If a bank's funding spread over the risk-free rate is 50 bp and the uncollateralized derivative has an average positive value of \$20 million over 5 years, estimate the FVA. Discuss whether FVA should be passed on to the client or absorbed by the bank's treasury.

---

**Exercise 5.** Compare and contrast CVA, DVA, FVA, and MVA. For each adjustment, state (a) what risk or cost it captures, (b) whether it increases or decreases the derivative's value to the bank, and (c) which market data is needed for its computation.

---

**Exercise 6.** Consider a CDS where both the protection buyer and the protection seller have non-trivial default risk. Explain how bilateral CVA modifies the standard CDS pricing formula. Why does counterparty risk in a CDS create "wrong-way risk" (i.e., the protection seller is more likely to default precisely when protection is needed)?
