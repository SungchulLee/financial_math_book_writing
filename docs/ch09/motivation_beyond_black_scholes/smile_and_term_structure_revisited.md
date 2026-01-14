# Smile and Term Structure Revisited


One of the most visible failures of the Black–Scholes model is the presence of a **volatility smile** and a non-flat **term structure of implied volatility**. These phenomena summarize how markets deviate from constant-volatility assumptions.

---

## The implied volatility surface


Implied volatility \(\sigma_{\text{impl}}(K,T)\) is defined as the volatility that reproduces the market option price when plugged into Black–Scholes.

Empirically:
- implied volatility depends on strike (smile/skew),
- implied volatility depends on maturity (term structure).

---

## Smile patterns


Typical equity index smiles exhibit:
- negative skew (higher implied vol for OTM puts),
- asymmetry reflecting crash risk,
- curvature increasing in stressed markets.

Single-stock smiles may differ but still contradict flat-vol assumptions.

---

## Term structure effects


Implied volatility varies with maturity due to:
- mean reversion of volatility,
- macro uncertainty at longer horizons,
- short-term event risk (earnings, announcements).

A single constant volatility cannot fit all maturities simultaneously.

---

## Economic interpretation


The smile and term structure encode:
- market beliefs about tail risk,
- demand for downside protection,
- expectations of future volatility dynamics.

They are not artifacts, but equilibrium outcomes of risk preferences.

---

## Key takeaways


- The volatility smile is ubiquitous and persistent.
- Term structure effects are economically meaningful.
- Any realistic model must explain both jointly.

---

## Further reading


- Rubinstein, implied binomial trees.
- Gatheral, *The Volatility Surface*.
- Carr & Wu, variance and tail risk.
