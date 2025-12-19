# Sensitivities as Conditional Expectations

Many Greeks can be expressed as conditional expectations, clarifying their hedging interpretation.

---

## Discounted martingale

For \(H=\Phi(S_T)\),

\[
\widetilde{V}_t
=
\mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}H\mid \mathcal{F}_t]
\]


is a \(\mathbb{Q}\)-martingale.

Martingale representation yields

\[
\widetilde{V}_t=\widetilde{V}_0+\int_0^t Z_s\,\mathrm{d}W_s.
\]


In Black–Scholes,

\[
Z_t=e^{-rt}\sigma S_t \Delta(t,S_t).
\]



---

## Interpretation

Delta is the predictable coefficient multiplying the tradable Brownian risk factor in a complete market. This is the precise foundation for “delta is the hedge ratio.”

---

## What to remember

- Delta arises as a predictable coefficient in the martingale representation.
- In incomplete markets, not every sensitivity corresponds to a tradable hedge.
