# Risk-Neutral Probability

In the binomial model, “risk-neutral probability” is **not** a belief about real outcomes.
It is a probability measure that makes **discounted asset prices martingales**.

---

## 1. Definition

Assume the no-arbitrage condition:

\[
d < 1+r < u.
\]



Define

\[
\boxed{
q := \frac{(1+r)-d}{u-d}.
}
\]



Then \(0<q<1\).

---

## 2. Martingale Property of the Discounted Stock

Compute under \(\mathbb{Q}\):

\[
\mathbb{E}^{\mathbb{Q}}[S_1]
= q(uS_0) + (1-q)(dS_0)
= (1+r)S_0.
\]



Equivalently,

\[
\boxed{
\mathbb{E}^{\mathbb{Q}}\left[\frac{S_1}{1+r}\right] = S_0.
}
\]



So the discounted stock is a martingale.

---

## 3. Risk-Neutral Pricing Formula

For a payoff \(H\) at time 1,

\[
\boxed{
V_0 = \frac{1}{1+r}\,\mathbb{E}^{\mathbb{Q}}[H]
= \frac{1}{1+r}\big(qH_u + (1-q)H_d\big).
}
\]



---

## 4. Preview of FTAP

In finite state spaces, the Fundamental Theorem of Asset Pricing says:

> No-arbitrage \(\iff\) there exists an equivalent martingale measure \(\mathbb{Q}\).

The binomial model is the simplest example where you can compute \(\mathbb{Q}\) explicitly.
