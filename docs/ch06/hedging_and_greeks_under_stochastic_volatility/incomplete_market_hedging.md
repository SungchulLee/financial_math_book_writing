# Incomplete Market Hedging

Stochastic volatility models operate in **incomplete markets**: not all sources of risk can be hedged using traded assets. This fundamentally changes hedging theory and practice.

---

## 1. Why markets are incomplete

In stochastic volatility models:
- volatility is not directly tradable,
- variance shocks introduce independent risk,
- delta hedging alone cannot eliminate uncertainty.

As a result, perfect replication is impossible.

---

## 2. Consequences for hedging

In an incomplete market:
- hedging strategies are not unique,
- residual risk remains even after optimal hedging,
- hedging performance depends on chosen objective.

This contrasts sharply with Black–Scholes replication.

---

## 3. Common hedging instruments

Practitioners attempt to reduce incompleteness using:
- options of different strikes/maturities (vega hedging),
- variance swaps or volatility indices (when available),
- dynamic rebalancing across the surface.

Still, some risks remain irreducible.

---

## 4. Hedging error as a random variable

Hedging error should be viewed as:
\[
\text{P&L}_{\text{hedge}} = \text{model error} + \text{unhedgeable risk}.
\]

Risk management focuses on:
- distribution of hedging error,
- tail risk,
- robustness across scenarios.

---

## 5. Key takeaways

- Stochastic volatility implies incomplete markets.
- Hedging aims to reduce, not eliminate, risk.
- Residual risk must be measured and managed explicitly.

---

## Further reading

- Schweizer, mean–variance hedging.
- Cont, *Model Uncertainty and Its Impact on Pricing*.
