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

We begin with a **one-period market** on the time grid \(t = 0,1\).


!!! note "Continuous Compounding Convention"
    Throughout this chapter, we use **continuous compounding** for the risk-free rate. In a one-period model, the risk-free asset grows by the factor \(e^{r dt}\), ensuring consistency with the Black–Scholes framework and simplifying the limiting arguments.


### Assets


* **Risk-free asset (bank account)**: with \(B_0 = 1\)


\[
B_{dt} = e^{r dt}
\]


* **Risky asset (stock)**: with \(S_0 > 0\) and \(0 < d < e^{r dt} < u\)

$$
S_{dt} =
\begin{cases}
u S_0 & \text{(up state)} \\
d S_0 & \text{(down state)}
\end{cases}
$$


### Portfolios

A **self-financing portfolio** is described by holdings \((\Delta, \beta)\), where:



* \(\Delta\): number of shares of stock


* \(\beta\): units of the bank account


Its value satisfies:

$$
V_0 = \Delta S_0 + \beta B_0, \qquad
V_{dt} = \Delta S_{dt} + \beta B_{dt}
$$

## 2. Contingent Claims and the Pricing Problem

A **contingent claim** (or derivative) is any payoff measurable with respect to the terminal stock price:

$$
H = H(S_{dt})
$$

The central question of asset pricing is:

> **What is the fair price \(V_0\) of the payoff \(H\) at time 0?**


We will answer this question through several equivalent perspectives:

1. **No-arbitrage** (existence of admissible prices),

2. **Replication** (uniqueness of prices),

3. **Risk-neutral pricing** (valuation by expectation).



## 3. No-Arbitrage and Its Meaning


### Definition (Arbitrage)

A portfolio \((\Delta, \beta)\) is an **arbitrage** if:


1. \(V_0 \le 0\),
2. \(V_{dt} \ge 0\) in all states,
3. \(\mathbb P(V_{dt} > 0) > 0\).

A market is **arbitrage-free** if no such portfolio exists.



### Derivation of the No-Arbitrage Condition


Consider the **discounted stock price**

$$
\tilde S_{dt} := \frac{S_{dt}}{e^{r dt}}
$$

* If \(e^{r dt} \ge u\), the bank dominates the stock even in the up state.


* If \(e^{r dt} \le d\), the stock dominates the bank even in the down state.


Therefore, absence of arbitrage requires:

$$
\boxed{d < e^{r dt} < u}
$$

## 4. Geometric Interpretation

Under the no-arbitrage condition,

$$
\frac{d S_0}{e^{r dt}} < S_0 < \frac{u S_0}{e^{r dt}}
$$

Equivalently, the current stock price lies in the **convex hull** of its discounted future values:

$$
S_0 \in \left[ \frac{d S_0}{e^{r dt}}, \frac{u S_0}{e^{r dt}} \right]
$$

This convexity property is the key to everything that follows.


## 5. Preview: Risk-Neutral Probability


When \(d < e^{r dt} < u\), there exists a unique number \(q \in (0,1)\) given by

$$
\boxed{
q := \frac{e^{r dt} - d}{u - d}
}
$$

such that

$$
S_0 = e^{-rdt}\big( q u S_0 + (1-q) d S_0 \big)
$$


### Risk-Neutral Measure


Define a probability measure \(\mathbb Q\) on the one-period state space by

$$
\mathbb Q(\text{up}) = q, 
\qquad 
\mathbb Q(\text{down}) = 1 - q
$$

This probability measure \(\mathbb Q\) is called the **risk-neutral measure**.



### Martingale Interpretation

Under \(\mathbb Q\), the stock price satisfies

$$
S_0 = e^{-rdt}\,\mathbb E^{\mathbb Q}[S_{dt}]
$$

Equivalently, the **discounted stock price**

$$
\tilde S_{dt} := e^{-rdt} S_{dt}
$$

is a martingale under \(\mathbb Q\).

This observation will form the basis of the general risk-neutral pricing formula for contingent claims.


