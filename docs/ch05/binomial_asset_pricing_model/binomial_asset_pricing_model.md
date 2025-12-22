Perfect — here is a **clean, fully integrated combination** of your two pieces into a single, coherent opening chapter section.
Nothing is duplicated, the narrative flows, and **no-arbitrage is treated as an intrinsic part of the model**, not an add-on.

You can drop this in directly as
`binomial_asset_pricing_model.md`.

---

# Binomial Asset Pricing Model

## Introduction

The **binomial asset pricing model**, developed by **Cox, Ross, and Rubinstein (1979)**, provides a discrete-time framework for modeling stock price evolution and pricing derivative securities. At each time step, the stock price can move to one of two possible values — **up** or **down** — by predetermined factors.

Despite its apparent simplicity, the binomial model captures the *essential logic* of arbitrage-free pricing and serves as the conceptual foundation for continuous-time models, most notably the **Black–Scholes framework**.

The discrete-time setting offers several key advantages:

* **Computational tractability**: step-by-step valuation via backward induction

* **Flexibility**: natural treatment of American options, dividends, and time-varying parameters

* **Path-dependent payoffs**: compatibility with barrier, lookback, and exotic options

* **Pedagogical clarity**: finite-state algebraic setting for core pricing principles

More fundamentally, the binomial model reveals the structure underlying modern asset pricing:

* **No-arbitrage** restrictions on prices

* **Replication** and **uniqueness** of values

* Emergence of a **risk-neutral probability**

* **Martingale pricing** of discounted assets

* The **binomial-to–Black–Scholes limit**

We proceed deliberately in this discrete framework to understand arbitrage-free pricing *before* passing to continuous time.

---

## 1. Market Setup

We begin with a **one-period market** on the time grid $t = 0,1$.

!!! note "Continuous Compounding Convention"
Throughout this chapter, we use **continuous compounding** for the risk-free rate. In a one-period model, the risk-free asset grows by the factor $e^r$, ensuring consistency with the Black–Scholes framework and simplifying the limiting arguments.

### Assets

* **Risk-free asset (bank account)**:

$$
B_0 = 1, \qquad B_1 = e^r, \quad r > -1.
$$

* **Risky asset (stock)**:

$$
S_0 > 0, \qquad
  S_1 =
  \begin{cases}
  u S_0 & \text{(up state)} \
  d S_0 & \text{(down state)}
  \end{cases},
  \quad \text{with } u > d > 0.
$$

---

### Portfolios

A **self-financing portfolio** is described by holdings ( $\Delta, \beta$ ), where:

* $\Delta$: number of shares of stock

* $\beta$: units of the bank account

Its value satisfies:

$$
V_0 = \Delta S_0 + \beta B_0, \qquad
V_1 = \Delta S_1 + \beta B_1.
$$

---

## 2. Contingent Claims and the Pricing Problem

A **contingent claim** (or derivative) is any payoff measurable with respect to the terminal stock price:

$$
H = H$S_1$.
$$

The central question of asset pricing is:

> **What is the fair price $V_0$ of the payoff ( H ) at time 0?**

We will answer this question through several equivalent perspectives:

1. **No-arbitrage** (existence of admissible prices),
2. **Replication** (uniqueness of prices),
3. **Risk-neutral pricing** (valuation by expectation).

Before pricing any claim, however, we must understand when the *market itself* is free of arbitrage.

---

## 3. No-Arbitrage and Its Meaning

### Definition (Arbitrage)

A portfolio ( $\Delta, \beta$ ) is an **arbitrage** if:

1. $V_0 \le 0$,
2. $V_1 \ge 0$ in all states,
3. ( \mathbb{P}$V_1 > 0$ > 0 ).

A market is **arbitrage-free** if no such portfolio exists.

---

### Derivation of the No-Arbitrage Condition

Consider the **discounted stock price**:

$$
\tilde S_1 := \frac{S_1}{e^r}.
$$

* If $e^r \ge u$, the bank dominates the stock even in the up state.
  Shorting the stock and investing in the bank yields a sure profit.

* If $e^r \le d$, the stock dominates the bank even in the down state.
  Borrowing from the bank and buying the stock yields a sure profit.

Therefore, **absence of arbitrage** requires:

$$
\boxed{d < e^r < u.}
$$

---

## 4. Geometric Interpretation

Under the no-arbitrage condition:

$$
\frac{d S_0}{e^r} < S_0 < \frac{u S_0}{e^r}.
$$

Equivalently, the current stock price lies in the **convex hull** of its discounted future values:

$$
S_0 \in \left[
\frac{d S_0}{e^r}, \frac{u S_0}{e^r}
\right]
$$

This convexity property is the key to everything that follows.

---

## 5. Preview: Risk-Neutral Probability

When $d < e^r < u$, there exists a unique number

$$
\boxed{q := \frac{e^r - d}{u - d}}, \qquad q \in (0,1),
$$

such that

$$
S_0 = e^{-r}\big( q,u S_0 + (1-q), d S_0 \big).
$$

This means:

> **The discounted stock price is a martingale under the probability $\mathbb{Q}$.**

This probability measure is called the **risk-neutral measure**, and it will allow us to price all contingent claims by expectation.

---

## Where This Leads

With the binomial model and no-arbitrage in place, we are now prepared to develop:

* **Replicating portfolios** and price uniqueness

* **Arrow–Debreu state prices**

* **Risk-neutral pricing** and martingale valuation

* **Multi-period binomial trees**

* The **binomial-to–Black–Scholes limit**

This completes the foundational setup of the binomial asset pricing model.

---

### ✅ TOC result (what you wanted)

* **Binomial Asset Pricing Model** ✅
  (model + no-arbitrage unified, clean, canonical)

If you want next, I can:

* tighten this into theorem–proof style,

* align notation with later replication sections,

* or check global consistency across Chapter 5.

This is *exactly* how a serious finance text should begin.
