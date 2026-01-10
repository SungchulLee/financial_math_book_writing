# BSDE-Based Risk Measures

Backward Stochastic Differential Equations (BSDEs) provide a powerful mathematical framework for defining **dynamic risk measures**.

---

## 1. BSDE formulation

A BSDE has the form

\[
Y_t = X + \int_t^T g(s, Y_s, Z_s) ds - \int_t^T Z_s dW_s,
\]


where:
- \(X\) is the terminal loss,
- \(g\) is a driver function.

The solution \(Y_t\) defines a dynamic risk measure.

---

## 2. Risk measure interpretation

Define

\[
\rho_t(X) := Y_t.
\]



Different choices of the driver \(g\) correspond to different risk attitudes:
- linear drivers → expectation-based risk,
- convex drivers → conservative risk measures.

---

## 3. Time-consistency

BSDE-based risk measures are naturally time-consistent due to their recursive structure.
This makes them attractive for dynamic risk management.

---

## 4. Applications

BSDE risk measures are used in:
- capital allocation,
- dynamic portfolio optimization,
- valuation adjustments (XVA).

They unify pricing and risk concepts.

---

## 5. Key takeaways

- BSDEs generate dynamic, time-consistent risk measures.
- The driver encodes risk aversion.
- They provide a flexible and rigorous framework.

---

## Further reading

- Peng, nonlinear expectations.
- Delbaen et al., BSDE risk measures.
