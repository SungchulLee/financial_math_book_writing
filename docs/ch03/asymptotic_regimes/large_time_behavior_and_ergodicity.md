# Large-Time Behavior and Ergodicity

Large-time limits depend on whether the model admits a stationary distribution.

---

## Non-ergodic Black–Scholes

Geometric Brownian motion has no stationary distribution in \(S\). Long-horizon behavior is dominated by drift and accumulated volatility.

---

## Ergodic factors

In multi-factor models, mean-reverting factors (e.g. variance in Heston-type models) may be ergodic with invariant measure \(\pi\), and for suitable \(f\),

\[
\frac{1}{T}\int_0^T f(X_s)\,\mathrm{d}s \to \int f\,\mathrm{d}\pi.
\]

---

## What to remember

- Black–Scholes is not ergodic in \(S\).
- Long-time asymptotics are model-dependent and often linked to large deviations or ergodicity of factors.
