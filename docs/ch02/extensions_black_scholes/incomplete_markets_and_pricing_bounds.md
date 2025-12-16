# Incomplete Markets and Pricing Bounds

In incomplete markets, equivalent martingale measures are not unique, so arbitrage-free prices form an interval.

---

## 1. Bounds via Martingale Measures

Let \(\mathcal{Q}\) be the set of equivalent martingale measures. For a claim \(H\),

\[
\boxed{
\underline{\pi}(H)=\inf_{\mathbb{Q}\in\mathcal{Q}}\mathbb{E}^{\mathbb{Q}}[e^{-rT}H],
\qquad
\overline{\pi}(H)=\sup_{\mathbb{Q}\in\mathcal{Q}}\mathbb{E}^{\mathbb{Q}}[e^{-rT}H].
}
\]



---

## 2. Superhedging Interpretation

The upper bound often matches the superhedging price:

\[
\boxed{
\overline{\pi}(H)=
\inf\left\{x:\exists\theta\text{ s.t. }x+\int_0^T\theta_t\,\mathrm{d}S_t\ge H\ \text{a.s.}\right\}.
}
\]



---

## 3. Selecting a Price

A specific price requires an additional criterion (e.g. minimal martingale measure, variance-optimal, utility-indifference, entropy minimization).

---

## 4. What to Remember

- Incompleteness yields bounds, not a single price.
- Choosing a price needs extra structure beyond no-arbitrage.
