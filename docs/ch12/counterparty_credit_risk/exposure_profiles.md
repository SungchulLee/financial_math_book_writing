# Exposure Profiles


Counterparty credit risk (CCR) arises from the possibility that a counterparty defaults while a derivative position has positive value. **Exposure profiles** describe how this value evolves over time.

---

## Definition of exposure


For a portfolio value process \(V_t\), the exposure at time \(t\) is

\[
E_t = \max(V_t, 0).
\]



Exposure is stochastic and depends on future market states.

---

## Expected Exposure (EE)


The **Expected Exposure** at time \(t\) is

\[
\text{EE}(t) = \mathbb{E}[E_t].
\]



It summarizes average counterparty exposure and is used in CVA calculations.

---

## Exposure profiles over time


Plotting \(\text{EE}(t)\) across maturities yields an exposure profile.
Key drivers include:
- product structure,
- optionality and convexity,
- netting and collateral agreements.

---

## Role of netting and collateral


- Netting reduces exposure by offsetting positions.
- Collateral reduces exposure dynamically but introduces margin risk.
- Exposure profiles must reflect legal agreements.

---

## Key takeaways


- Exposure is the positive portfolio value.
- Exposure profiles describe its time evolution.
- Netting and collateral materially affect CCR.

---

## Further reading


- Gregory, *Counterparty Credit Risk*.
- Brigo et al., exposure modeling.
