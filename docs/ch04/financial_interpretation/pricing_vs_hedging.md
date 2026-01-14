# Pricing vs Hedging


Although pricing and hedging are closely related, they represent **distinct
economic problems**. Measure change clarifies the difference between them.

---

## Pricing: A Valuation Problem


Pricing asks the question:

> *What is the fair value of a contingent claim today?*

Under no-arbitrage, the price of a payoff \(X_T\) at time \(T\) is given by

\[
V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[ e^{-\int_0^T r_s ds} X_T \right]
\]

where \(\mathbb{Q}\) is a risk-neutral measure.

Pricing depends only on:

- the payoff structure,
- the risk-free rate,
- the risk-neutral dynamics.

---

## Hedging: A Replication Problem


Hedging asks a different question:

> *How can the payoff be replicated or risk-managed through trading?*

Hedging strategies are constructed in the **physical market**, using observable
asset prices and trading rules. They depend on:

- market completeness,
- available instruments,
- trading constraints.

---

## Why Pricing Uses \(\mathbb{Q}\)


Pricing is measure-dependent because it is a valuation exercise.
The risk-neutral measure incorporates risk preferences implicitly through the
change of measure.

Hedging, however, is **measure-invariant**:

- A self-financing strategy remains self-financing under any equivalent measure.
- Replication arguments do not depend on \(\mathbb{P}\) or \(\mathbb{Q}\).

---

## Complete vs Incomplete Markets


- In **complete markets**, pricing and hedging coincide:
  the price is the cost of the unique replicating strategy.
- In **incomplete markets**, pricing is not unique, and hedging is imperfect.

This distinction will reappear in later chapters on model risk and robust pricing.

---

## Summary


- Pricing is a valuation problem → use \(\mathbb{Q}\).
- Hedging is a trading problem → measure-independent.
- Confusing the two leads to conceptual errors.

Understanding this distinction is essential for interpreting risk-neutral pricing
correctly.
