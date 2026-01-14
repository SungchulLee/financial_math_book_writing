# Discounting Killing


## Discounting

Future cash flows must be discounted to reflect the time value of money.
In continuous time, discounting enters pricing equations structurally.

---

## Pricing PDE Interest

For a diffusion \(X_t\), the pricing PDE takes the form:
\[
\partial_t u + \mathcal{L}u - r u = 0.
\]

The term \(-ru\) is called the **killing term**.

---

## Probabilistic

Consider the discounted process:
\[
e^{-rt} u(t,X_t).
\]

The killing term compensates for the exponential decay, ensuring martingality.

Equivalent representation:
\[
u(t,x) = \mathbb{E}\left[
e^{-\int_t^T r ds} \Phi(X_T)
\mid X_t=x
\right].
\]

---

## Killed Processes

Mathematically, discounting corresponds to a process that is:
- terminated at rate \(r\)
- weighted by survival probability

---

## Financial

- Higher interest rates reduce present values
- Discounting modifies the generator
- Credit risk and default introduce additional killing terms

---

## Connection Forward

This structure extends naturally to running payoffs and defaultable claims.