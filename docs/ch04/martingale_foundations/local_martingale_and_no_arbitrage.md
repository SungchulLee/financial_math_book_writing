# Local Martingale and No-Arbitrage

## 1. Economic Principle
A fundamental principle of mathematical finance is:
> *In an arbitrage-free market, discounted asset prices behave like martingales.*

This section explains how this principle appears both probabilistically and through PDEs.

---

## 2. Discounted Portfolios
Let \(V_t\) be the value of a self-financing portfolio and assume a constant interest rate \(r\).
Define the discounted value:
\[
\tilde V_t = e^{-rt} V_t.
\]

**No-arbitrage condition**:
\[
\tilde V_t \text{ is a local martingale}.
\]

---

## 3. Itô Decomposition
Suppose \(V_t = u(t,X_t)\).
Applying Itô's formula:
\[
d(e^{-rt}u(t,X_t)) =
e^{-rt}\big(
\partial_t u + \mathcal{L}u - r u
\big)dt
+ e^{-rt}\sigma u_x dW_t.
\]

The discounted price is a local martingale **if and only if**
\[
\boxed{
\partial_t u + \mathcal{L}u - r u = 0.
}
\]

---

## 4. PDE Interpretation
The pricing PDE is precisely the condition that removes deterministic drift.
Any non-zero drift would imply predictable profit opportunities.

---

## 5. Financial Meaning
- Martingales represent *fair games*
- Local martingales are sufficient in continuous time
- Arbitrage corresponds to positive drift after discounting

---

## 6. Connection Forward
To enforce the martingale property, we often change probability measures.
This leads directly to **risk-neutral valuation** and **Girsanov’s theorem**.