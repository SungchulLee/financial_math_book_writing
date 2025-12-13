# Smile Trading and Skew Bets

Smile trading targets relative mispricings across strikes (skew/curvature) and maturities (term structure).

A useful abstraction is a functional sensitivity:
\[
\delta V \approx \int \frac{\delta V}{\delta \Sigma(T,K)}\,\delta \Sigma(T,K)\,\mathrm{d}K.
\]

---

## What to remember

- Smile trades target surface deformations, not just the level of volatility.
- Asymptotics constrain feasible short-time and tail behaviors of the surface.
