# Chapter 4: Measure Change

This chapter develops the framework for **changing probability measures in continuous time**, which underlies modern derivative pricing and connects stochastic calculus to financial economics.

The central idea is:

> **Pricing is achieved by changing the probability measure so that discounted asset prices become martingales.**

Rather than introducing new pricing principles, this chapter shows how the **measure-change mechanism implements the no-arbitrage framework developed earlier**.

---

## Conceptual Roadmap

The chapter follows a strict progression:

```mermaid
flowchart LR
A[Martingale Machinery]
--> B[Girsanov Theorem]
--> C[Risk-Neutral Measure]
--> D[Financial Insights]
```

---

## Structure of the Chapter

### 4.1 Martingale Machinery

We build the **mathematical foundation** required for measure change.

- Local martingales and why they matter
- Integrability conditions (Novikov, Kazamaki)
- Stochastic exponential as the Radon–Nikodym density
- Martingale representation theorem
- A unifying principle: controlling when local martingales are true martingales

This section answers: *when does a candidate density actually define a valid probability measure?*

---

### 4.2 Girsanov's Theorem

We introduce the **mechanism of measure change**.

- Intuition: drift lives in the measure, not the paths
- Financial meaning of drift adjustment
- Formal statement of Girsanov's theorem
- Proof via stochastic exponentials

The key result: changing the measure removes drift while preserving volatility and sample paths.

---

### 4.3 Risk-Neutral Measure

We apply Girsanov's theorem to construct pricing measures.

**I. Financial Meaning**

- Martingales and no-arbitrage
- Risk-neutral valuation principle

**II. Construction**

- Building the risk-neutral measure
- Market price of risk
- Concrete examples

**III. Extensions**

- Numéraire and measure change
- Forward measures

This section answers: *how does measure change produce the pricing measure used in finance?*

---

### 4.4 Financial Insights

We interpret the framework from an economic and practical perspective.

**I. Economic Foundation (WHY)**

- Stochastic discount factor (SDF)
- Connection to CAPM and factor models

**II. Measure Change Interpretation (HOW)**

- Physical vs risk-neutral probabilities
- Risk premium decomposition

**III. Pricing vs Hedging (WHAT)**

- Relationship between expectations and replication

**IV. Practice (REALITY)**

- How practitioners actually use the framework

**V. Limits (BOUNDARIES)**

- When measure change fails (incompleteness, bubbles, strict local martingales)

---

## What This Chapter Achieves

By the end of this chapter, the reader understands that:

- measure change is the **mechanism** behind risk-neutral pricing
- Girsanov's theorem explains how drift is removed
- pricing depends on volatility and payoff, not physical drift
- martingale representation underpins hedging
- different measures reflect **different economic viewpoints**, not different prices

---

## Role in the Book

This chapter provides the bridge between **stochastic calculus** (Chapters 2–3) and **pricing and PDE methods** (Chapters 5–6). It supplies the machinery used for:

- Black–Scholes derivation
- Feynman–Kac representation
- Interest-rate modeling via forward measures
