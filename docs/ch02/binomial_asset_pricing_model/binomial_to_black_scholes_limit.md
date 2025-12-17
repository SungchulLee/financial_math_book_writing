# Binomial to Black–Scholes Limit

Black–Scholes pricing can be obtained as a scaling limit of a binomial tree.  
This section explains the idea at a high level.

---

## 1. Matching Variance

To match a continuous-time diffusion with volatility \(\sigma\), a common choice is:

\[
u = e^{\sigma\sqrt{\Delta t}},\qquad
d = e^{-\sigma\sqrt{\Delta t}}.
\]



---

## 2. Risk-Neutral Drift

Under the risk-neutral measure, the expected growth must match the risk-free rate:

\[
\mathbb{E}^{\mathbb{Q}}[S_{n+1}\mid\mathcal{F}_n] \approx (1+r\Delta t)S_n.
\]



This produces a stepwise risk-neutral probability \(q\) depending on \(u,d,r\).

---

## 3. Discrete Recursion vs PDE

Binomial recursion:

\[
V_n = \frac{1}{1+r}\Big(q V_{n+1}^{(u)} + (1-q)V_{n+1}^{(d)}\Big).
\]



In the limit \(\Delta t\to 0\), this leads to the Black–Scholes PDE:

\[
V_t + \frac12\sigma^2 S^2 V_{SS} + r S V_S - rV = 0.
\]



---

## 4. Practical Takeaway

The binomial tree remains useful even after learning the closed-form BS formula:
- intuitive,
- easy to implement,
- extends well to American options.
