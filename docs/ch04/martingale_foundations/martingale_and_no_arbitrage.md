# Martingale and No-Arbitrage


This section explains the deep connection between **no-arbitrage**, **martingale
pricing**, and **change of probability measure**. The goal is conceptual rather
than technical: to understand *why* measure change removes arbitrage, before
learning *how* such a change of measure is constructed.

---

## Arbitrage and Discounted Asset Prices


An **arbitrage opportunity** is a trading strategy that:
- requires zero initial cost,
- has nonnegative payoff almost surely,
- has strictly positive payoff with positive probability.

In continuous-time models, arbitrage is most naturally studied using
**discounted asset prices**. Let \( B_t \) denote the money market account and
\( S_t \) the price of a risky asset. The discounted price is
\[
\tilde S_t = \frac{S_t}{B_t}.
\]

If discounted prices exhibit systematic upward drift under the physical
probability measure \( P \), arbitrage opportunities may arise.

---

## Martingales and Local Martingales


In discrete time, no-arbitrage is closely related to discounted prices being
**martingales**. In continuous time, however, the martingale condition is often
too strong.

Instead, the correct probabilistic object is a **local martingale**.

- Every martingale is a local martingale.
- Many economically meaningful price processes are local martingales but not
  true martingales.

Local martingales capture the idea that asset prices have *no systematic drift*
once properly adjusted, even if expectations are not globally well-behaved.

---

## No-Arbitrage and Martingale Property


A central insight of modern asset pricing is:

> **If discounted asset prices are local martingales under some probability
> measure equivalent to \( P \), then arbitrage opportunities are ruled out.**

Equivalently:
- Arbitrage corresponds to predictable drift in discounted prices.
- Removing drift removes arbitrage.

This motivates the search for a probability measure under which discounted
prices behave like martingales.

---

## Why Measure Change Removes Arbitrage


A **change of measure** does not alter:
- the paths of asset prices,
- the available trading strategies,
- the economic payoffs.

It only alters the **probabilities** assigned to future scenarios.

Changing the probability measure can therefore:
- eliminate artificial drift terms,
- convert discounted prices into martingales,
- neutralize arbitrage opportunities.

Importantly, the new measure must be **equivalent** to the original one, meaning
that events of zero probability remain impossible.

---

## Economic Interpretation


From an economic viewpoint:
- Under the physical measure \( P \), asset prices reflect risk preferences and
  beliefs.
- Under an equivalent martingale measure, prices reflect *fair values* relative
  to a chosen numéraire.

This distinction clarifies the difference between:
- **pricing** (measure-dependent, martingale-based),
- **hedging** (pathwise, model-based).

---

## Relation to the Fundamental Theorem of Asset Pricing


The ideas developed here lead directly to the **Fundamental Theorem of Asset
Pricing (FTAP)**:

> **No-arbitrage is equivalent to the existence of an equivalent probability
> measure under which discounted asset prices are (local) martingales.**

The precise mathematical statement and its proof are deferred to Chapter 5,
where the FTAP is studied in detail using functional-analytic tools.

---

## What Comes Next


- **Girsanov’s theorem** explains how probability measures are changed in
  continuous-time stochastic models.
- The **risk-neutral measure** provides a canonical example associated with the
  money market numéraire.
- Later, different choices of numéraire will lead to different martingale
  measures, all consistent with no-arbitrage.

---
