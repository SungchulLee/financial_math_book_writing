# Gamma Risk and Convexity Effects

For a small move \(\delta S\),
\[
\delta V \approx \Delta\,\delta S + \frac{1}{2}\Gamma(\delta S)^2.
\]
Delta-hedging removes the linear term, leaving
\[
\boxed{\delta V_{\text{delta-hedged}}\approx \frac{1}{2}\Gamma(\delta S)^2.}
\]
Thus gamma exposure links delta-hedged P\&L to realized variance.

---

## What to remember

- Long gamma benefits from volatility (large squared moves).
- Short gamma earns carry but is exposed to large moves.
