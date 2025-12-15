# Smile Dynamics and Hedging

Smile dynamics describe how the implied volatility surface evolves as market conditions change. Understanding these dynamics is essential for **hedging volatility risk** beyond simple vega neutralization.

---

## 1. Static vs dynamic smiles

A **static smile** assumes the surface is fixed in time except for deterministic decay.
A **dynamic smile** evolves with:
- spot movements,
- volatility regime shifts,
- changes in market sentiment.

Dynamic effects generate additional sources of P&L.

---

## 2. Smile dynamics and P&L

When spot moves:
- implied volatility typically changes non-uniformly across strikes,
- vanna and volga effects appear,
- delta–vega hedges may break down.

Smile dynamics explain why delta-hedged options still exhibit volatility-driven P&L.

---

## 3. Hedging implications

Effective hedging requires:
- understanding how the smile moves with spot,
- hedging across multiple strikes and maturities,
- monitoring higher-order Greeks.

Single-instrument vega hedges are generally insufficient.

---

## 4. Model-based perspectives

Different models imply different smile dynamics:
- local volatility: sticky strike behavior,
- stochastic volatility: leverage-driven skew dynamics,
- SABR: interpolates between behaviors.

Model choice therefore affects hedging outcomes.

---

## 5. Key takeaways

- Smile dynamics are central to volatility hedging.
- Hedging requires managing vega, vanna, and volga jointly.
- Model assumptions materially affect risk attribution.

---

## Further reading

- Derman & Kani, local volatility and smile dynamics.
- Bergomi, *Stochastic Volatility Modeling*.
