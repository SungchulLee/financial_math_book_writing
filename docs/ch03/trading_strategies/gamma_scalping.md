# Gamma Scalping

Gamma scalping combines a long-gamma option position with frequent delta hedging to monetize realized volatility relative to implied volatility.

---

## Heuristic P&L

Over small \(\delta t\) with move \(\delta S\),

\[
\delta \Pi \approx \frac{1}{2}\Gamma(\delta S)^2 - (\text{theta})\,\delta t.
\]


Profitability depends on whether realized variance (gamma term) exceeds carry cost (theta) plus transaction costs.

---

## What to remember

- Gamma scalping is essentially a realized variance trade.
- Costs and near-expiry gamma blow-up are central practical constraints.
