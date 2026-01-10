# Discounting and Killing Term

## 1. Discounting in Continuous Time
Future cash flows must be discounted to reflect the time value of money.
In continuous time, discounting enters pricing equations structurally.

---

## 2. Pricing PDE with Interest Rates
For a diffusion \(X_t\), the pricing PDE takes the form:
\[
\partial_t u + \mathcal{L}u - r u = 0.
\]

The term \(-ru\) is called the **killing term**.

---

## 3. Probabilistic Interpretation
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

## 4. Killed Processes
Mathematically, discounting corresponds to a process that is:
- terminated at rate \(r\)
- weighted by survival probability

---

## 5. Financial Interpretation
- Higher interest rates reduce present values
- Discounting modifies the generator
- Credit risk and default introduce additional killing terms

---

## 6. Connection Forward
This structure extends naturally to running payoffs and defaultable claims.