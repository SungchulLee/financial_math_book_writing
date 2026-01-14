# Sticky Strike vs Sticky Delta


When the underlying price moves, the implied volatility surface changes. Two stylized assumptions—**sticky strike** and **sticky delta**—describe how implied volatility responds to spot movements and have major implications for hedging.

---

## Sticky strike assumption


Under **sticky strike**:
- implied volatility is assumed constant at a fixed strike,
- when spot moves, the same strike retains the same implied vol.

Formally:

\[
\sigma_{\text{impl}}(K, S) \approx \sigma_{\text{impl}}(K).
\]



This assumption is simple but often unrealistic for equities.

---

## Sticky delta assumption


Under **sticky delta**:
- implied volatility is constant at a fixed delta,
- when spot moves, the strike associated with a given delta shifts.

Formally:

\[
\sigma_{\text{impl}}(\Delta, S) \approx \sigma_{\text{impl}}(\Delta).
\]



This behavior is commonly observed in FX markets.

---

## Impact on Greeks


The choice between sticky strike and sticky delta affects:
- delta hedging,
- vanna and volga,
- P&L attribution during spot moves.

In particular, delta under sticky delta is typically smaller than under sticky strike.

---

## Empirical considerations


Empirical smile dynamics often lie **between** the two extremes:
- short-term equity smiles are closer to sticky strike,
- FX smiles are closer to sticky delta,
- stressed markets can deviate from both.

Thus, these assumptions should be viewed as benchmarks, not truths.

---

## Key takeaways


- Sticky strike and sticky delta describe smile response to spot moves.
- They imply different Greeks and hedging behavior.
- Real markets interpolate between these idealizations.

---

## Further reading


- Derman, *The Volatility Smile*.
- Bergomi, *Stochastic Volatility Modeling*.
