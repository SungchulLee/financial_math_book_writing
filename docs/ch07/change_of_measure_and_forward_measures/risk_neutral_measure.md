# Risk-Neutral Measure

The **risk-neutral measure** is the cornerstone of arbitrage-free pricing. Under this measure, discounted asset prices are martingales, allowing derivative prices to be expressed as discounted expectations.

---

## 1. Numéraire and probability measure

Let \(B_t\) denote the money-market account:
\[
dB_t = r_t B_t\,dt, \qquad B_0=1.
\]

A probability measure \(\mathbb{Q}\) is **risk-neutral** if, for any tradable asset with price \(S_t\),
\[
\frac{S_t}{B_t} \text{ is a martingale under } \mathbb{Q}.
\]

---

## 2. Fundamental pricing formula

Under the risk-neutral measure,
\[
V_t = \mathbb{E}^{\mathbb{Q}}\left[
e^{-\int_t^T r_s ds} \, V_T
\middle| \mathcal{F}_t
\right],
\]
where \(V_T\) is the payoff at maturity.

This formula applies to bonds, options, and general derivatives.

---

## 3. Change of measure intuition

The risk-neutral measure:
- absorbs risk premia into the drift,
- leaves diffusion terms unchanged,
- simplifies pricing to expectation of discounted cashflows.

It is not the physical (real-world) probability measure.

---

## 4. Interest-rate context

In interest-rate models:
- the short rate \(r_t\) determines discounting,
- \(\mathbb{Q}\)-dynamics are calibrated to prices,
- physical dynamics are relevant for risk management, not pricing.

---

## 5. Key takeaways

- Risk-neutral measure enforces arbitrage-free pricing.
- Discounted prices are martingales under \(\mathbb{Q}\).
- Pricing reduces to discounted expectation.

---

## Further reading

- Harrison & Pliska, martingale pricing.
- Björk, *Arbitrage Theory in Continuous Time*.
