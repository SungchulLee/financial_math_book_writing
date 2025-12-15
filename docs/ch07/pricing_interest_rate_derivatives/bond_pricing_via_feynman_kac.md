# Bond Pricing via Feynman–Kac

An alternative and often more intuitive approach to bond pricing uses the **Feynman–Kac formula**, which expresses prices as expectations of discounted cashflows under the risk-neutral measure.

---

## 1. Risk-neutral valuation

The fundamental pricing relation is
\[
P(t,T) = \mathbb{E}^{\mathbb{Q}}\left[
\exp\left(-\int_t^T r_s ds\right)
\middle| \mathcal{F}_t
\right].
\]

This holds for any arbitrage-free short-rate model under \(\mathbb{Q}\).

---

## 2. Feynman–Kac theorem

The Feynman–Kac theorem states that the function
\[
u(t,r) = \mathbb{E}^{\mathbb{Q}}\left[
\exp\left(-\int_t^T r_s ds\right)
\middle| r_t=r
\right]
\]
is the unique solution to the bond pricing PDE with terminal condition \(u(T,r)=1\).

Thus:
- expectation formulation and PDE formulation are equivalent,
- the choice is one of perspective and convenience.

---

## 3. Closed-form evaluation

For affine short-rate models:
- the integral \(\int_t^T r_s ds\) is Gaussian (Vasicek) or non-central chi-square (CIR),
- expectations can be computed analytically,
- results coincide with exponential-affine formulas.

---

## 4. Monte Carlo interpretation

The Feynman–Kac form enables:
- Monte Carlo pricing of bonds,
- simulation-based pricing of IR derivatives,
- easy extension to path-dependent payoffs.

However, Monte Carlo is usually inefficient for plain bonds compared to closed forms.

---

## 5. Key takeaways

- Bond prices are discounted expectations under \(\mathbb{Q}\).
- Feynman–Kac links PDEs and probabilistic pricing.
- Monte Carlo follows naturally from this view.

---

## Further reading

- Karatzas & Shreve, *Brownian Motion and Stochastic Calculus*.
- Björk, *Arbitrage Theory in Continuous Time*.
