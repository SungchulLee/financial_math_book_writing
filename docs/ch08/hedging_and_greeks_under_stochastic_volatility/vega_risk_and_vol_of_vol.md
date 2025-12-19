# Vega Risk and Vol-of-Vol

Under stochastic volatility, option risk is no longer captured by delta alone. **Vega risk** and, more subtly, **volatility-of-volatility (vol-of-vol) risk** become central drivers of P&L and hedging performance.

---

## 1. Vega in stochastic volatility models

In Black–Scholes, vega measures sensitivity to a single volatility parameter:

\[
\text{Vega} = \partial_{\sigma} P.
\]



In stochastic volatility models, volatility itself is random, so vega represents sensitivity to:
- the current variance level,
- the volatility state variable,
- the implied volatility surface.

Thus, vega is model- and state-dependent.

---

## 2. Vol-of-vol risk

The parameter (or process) controlling volatility fluctuations—often denoted \(\xi\)—introduces **second-order volatility risk**.

Consequences:
- option prices depend on uncertainty of future volatility,
- convexity in volatility matters,
- products sensitive to smile curvature are especially exposed.

This risk cannot be hedged by delta or vega alone.

---

## 3. Greeks beyond vega

Common higher-order sensitivities include:
- **Volga (vomma):** sensitivity of vega to volatility,
- **Vanna:** cross-sensitivity between spot and volatility,
- sensitivities to variance process parameters.

These Greeks are typically large for long-dated or exotic options.

---

## 4. Practical implications

- Vega hedging with a single option is insufficient.
- Smile dynamics cause residual P&L even for delta–vega neutral portfolios.
- Vol-of-vol risk explains persistent hedging errors in practice.

---

## 5. Key takeaways

- Vega risk is richer under stochastic volatility.
- Vol-of-vol introduces unhedgeable second-order effects.
- Understanding higher-order Greeks is essential for risk management.

---

## Further reading

- Taleb, *Dynamic Hedging*.
- Bergomi, *Stochastic Volatility Modeling*.
