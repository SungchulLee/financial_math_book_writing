# Chapter 1: Discrete Models and the Fundamental Theorem of Asset Pricing

This chapter develops the theory of arbitrage-free pricing from first principles in
discrete-time, finite-state markets. It begins with static pricing using portfolios
and state prices, builds toward dynamic hedging and replication in the binomial model,
and culminates in the Fundamental Theorem of Asset Pricing, which provides the general
mathematical foundation for all modern pricing theory.

---

## Conceptual Roadmap

The chapter follows a single guiding idea:

> **Prices are determined by the absence of arbitrage.**

This idea unfolds in stages:

```mermaid
flowchart LR
A[Static Payoffs]
--> B[State Prices]
--> C[Replication]
--> D[Risk-Neutral Pricing]
--> E[Multi-Period Models]
--> F[Continuous Limit]
--> G[FTAP]
```

---

## Structure of the Chapter

### 1. Discrete-Time Foundations

We begin with a one-period model, where all future uncertainty is captured by a finite
set of states.

- Assets are described by a **payoff matrix**
- Portfolios generate state-dependent payoffs
- **Arbitrage** is defined as a free lunch across states
- **Arrow–Debreu securities** provide a basis for all payoffs

The key result is:

$$
V_0 = \sum_{s} \psi_s \, X(\omega_s)
$$

where $\psi_s$ are **state prices**. They exist if and only if the market is
arbitrage-free, and are unique if and only if the market is complete.

---

### 2. The Binomial Model

We introduce dynamics through the binomial model, where prices evolve over time.

Three seemingly different approaches are actually equivalent:

- **Replication**: construct a portfolio matching the payoff
- **Delta hedging**: eliminate risk dynamically
- **Risk-neutral pricing**: compute discounted expectations

All lead to:

$$
V_0 = e^{-r\Delta t} \mathbb{E}^{\mathbb{Q}}[V_1]
$$

where $\mathbb{Q}$ is the **risk-neutral measure**. This is the first appearance of
the central idea:

> pricing = expectation under a special probability measure

---

### 3. Multi-Period Models and American Options

Extending to multiple periods introduces:

- **Recombining trees**
- **Backward induction**
- **Dynamic hedging strategies**

American options introduce **optimal stopping**, where pricing becomes:

$$
V = \max(\text{exercise value},\; \text{continuation value})
$$

The trinomial model reveals an important limitation: when markets are incomplete,
prices are no longer unique.

---

### 4. Binomial to Black–Scholes Limit

As the time step shrinks:

- the binomial model converges to Brownian motion
- prices converge to the Black–Scholes model
- the discrete recursion becomes the Black–Scholes PDE

This shows that continuous-time finance is not new theory, but a **limit of discrete
models**.

---

### 5. Fundamental Theorem of Asset Pricing

The chapter culminates in the FTAP, which generalizes everything developed so far:

$$
\text{No-Arbitrage} \iff \text{Existence of a Martingale Measure}
$$

$$
\text{Completeness} \iff \text{Uniqueness of that Measure}
$$

The proof relies on convex geometry (separating hyperplanes), revealing that:

- arbitrage is a geometric inconsistency
- pricing measures arise as separating functionals

This unifies state prices, risk-neutral probabilities, and replication-based pricing
into a single framework.

---

### 6. Numéraire and Change of Measure

Finally, the theory is extended by changing the unit of account (numéraire).

> Prices are invariant under the choice of numéraire.

Different numéraires produce different martingale measures, but the same prices. This
leads to the general pricing formula:

$$
V_t = N_t \, \mathbb{E}^{\mathbb{Q}^N}\!\left[\frac{\Phi_T}{N_T} \;\middle|\; \mathcal{F}_t\right]
$$

and provides powerful tools for simplifying complex pricing problems.

---

## What This Chapter Achieves

By the end of the chapter, the reader understands that:

- arbitrage-free pricing is fundamentally a **linear pricing rule**
- dynamic hedging and risk-neutral expectation are **equivalent**
- continuous-time models arise as **limits of discrete ones**
- all pricing can be expressed as expectation under a **martingale measure**

!!! note "Role in the Book"
    This chapter provides the foundation for stochastic calculus and continuous-time
    finance in later chapters: Brownian motion and martingales (Chapter 2), Itô
    calculus (Chapter 3), change of measure and Girsanov's theorem (Chapter 4), and
    the Feynman–Kac connection (Chapter 5).
