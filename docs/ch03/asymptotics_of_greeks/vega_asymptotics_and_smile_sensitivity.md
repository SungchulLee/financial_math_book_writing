# Vega Asymptotics and Smile Sensitivity

Vega concentrates near the money and vanishes as maturity shrinks.

---

## Scaling

In Black–Scholes,
\[
\nu(t,S)\approx S\sqrt{\tau}\,\varphi(d_1).
\]
So near the money,
\[
\boxed{\nu \sim \sqrt{\tau}.}
\]

---

## Smile models

With an implied volatility surface \(\Sigma(T,K)\), “vega” generalizes to sensitivities to surface deformations (bucket vegas), not a single scalar derivative.

---

## What to remember

- Short-maturity vega vanishes but localizes sharply near ATM.
- In smile models, vega is multi-dimensional (surface risk).
