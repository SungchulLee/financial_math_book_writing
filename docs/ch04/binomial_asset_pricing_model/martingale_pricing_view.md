# Martingale Pricing View

A powerful way to organize asset pricing is:

> **Discounted prices are martingales under a risk-neutral measure.**

In the binomial model, this statement is not abstract—it is a direct consequence of no-arbitrage.

---

## 1. Discounted Processes

Define discounted values:


\[
\tilde S_t := \frac{S_t}{B_t},\qquad
\tilde V_t := \frac{V_t}{B_t}.
\]





In the one-period model:


\[
\tilde S_0=S_0,\qquad
\tilde S_1=\frac{S_1}{1+r}.
\]





---

## 2. Pricing as Expectation

If a claim payoff is \(H\) at time 1, then its time-0 price is


\[
V_0 = \frac{1}{1+r}\,\mathbb{E}^{\mathbb{Q}}[H].
\]





In a multi-period model,


\[
V_n = B_n\,\mathbb{E}^{\mathbb{Q}}\left[\frac{H}{B_N}\mid \mathcal{F}_n\right].
\]





---

## 3. Replication vs Martingale Pricing

In a complete market:
- replication gives the price by portfolio construction,
- martingale pricing gives the price by expectation.

In continuous time, the Martingale Representation Theorem is the statement that these perspectives match.
