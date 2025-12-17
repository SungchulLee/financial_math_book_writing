# One-Period Model and No-Arbitrage

In the one-period binomial model, no-arbitrage is equivalent to a simple inequality:

\[
d < 1+r < u.
\]


This condition has a clear financial meaning and leads to existence of a **risk-neutral probability**.

---

## 1. Setup


\[
B_0=1,\quad B_1=1+r,
\qquad
S_1 \in \{uS_0, dS_0\},\quad u>d>0.
\]



---

## 2. What Is an Arbitrage?

A portfolio \((\Delta,\beta)\) is an **arbitrage** if:

1. \(V_0 = \Delta S_0 + \beta B_0 \le 0\)
2. \(V_1 = \Delta S_1 + \beta B_1 \ge 0\) in both states
3. \(\mathbb{P}(V_1>0)>0\) (strict profit with positive probability)

No-arbitrage means **no such portfolio exists**.

---

## 3. Deriving the No-Arbitrage Condition

Consider the discounted stock:

\[
\tilde S_1 := \frac{S_1}{1+r}.
\]



If \(1+r \ge u\), then the bank dominates the stock even in the up state.
A trader could short the stock and invest in the bank to lock a profit (an arbitrage).

If \(1+r \le d\), then the stock dominates the bank even in the down state.
A trader could borrow money (short the bank) and buy the stock to lock a profit.

Therefore, to avoid arbitrage we must have:

\[
d < 1+r < u.
\]



---

## 4. Geometric Meaning: Discounted Price Lies Between States

Under no-arbitrage,

\[
\frac{dS_0}{1+r} < S_0 < \frac{uS_0}{1+r}.
\]



Equivalently,

\[
S_0 \in \text{convex hull of } \left\{\frac{uS_0}{1+r}, \frac{dS_0}{1+r}\right\}.
\]



This convex-combination viewpoint is exactly what produces the risk-neutral probability \(q\).

---

## 5. Preview: Risk-Neutral Probability

If \(d < 1+r < u\), define

\[
q := \frac{(1+r)-d}{u-d}.
\]


Then \(q\in(0,1)\), and

\[
S_0 = \frac{1}{1+r}\Big(q\,uS_0 + (1-q)\,dS_0\Big).
\]



That is, **the discounted stock is a martingale under \(\mathbb{Q}\)**.
