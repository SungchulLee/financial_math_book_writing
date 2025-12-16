# Greeks and Martingale Representation

In complete diffusion models, martingale representation yields a conceptual foundation for delta hedging: delta is the integrand in the stochastic integral representation of the discounted price.

---

## Discounted asset and wealth

In Black–Scholes under \(\mathbb{Q}\),


\[
\mathrm{d}S_t = rS_t\,\mathrm{d}t + \sigma S_t\,\mathrm{d}W_t,
\qquad
B_t = e^{rt}.
\]



Define the discounted asset \(\widetilde{S}_t := B_t^{-1}S_t\). Then


\[
\mathrm{d}\widetilde{S}_t = \sigma \widetilde{S}_t\,\mathrm{d}W_t,
\]



so \(\widetilde{S}\) is a \(\mathbb{Q}\)-martingale.

---

## Discounted option price is a martingale

Let \(V(t,S_t)\) be the price process and define \(\widetilde{V}_t := B_t^{-1}V(t,S_t)\). Under \(\mathbb{Q}\),


\[
\widetilde{V}_t
=
\mathbb{E}^{\mathbb{Q}}[\widetilde{V}_T\mid \mathcal{F}_t],
\]



so \(\widetilde{V}\) is a martingale.

---

## Martingale representation

In a Brownian filtration, any square-integrable martingale can be represented as


\[
\boxed{
\widetilde{V}_t = \widetilde{V}_0 + \int_0^t Z_s\,\mathrm{d}W_s
}
\]



for some predictable \(Z\) with \(\mathbb{E}\int_0^T Z_s^2\,\mathrm{d}s<\infty\).

---

## Identification of delta

By Itô’s formula and the PDE cancellation of drift,


\[
\mathrm{d}\widetilde{V}_t
=
B_t^{-1}\sigma S_t V_S(t,S_t)\,\mathrm{d}W_t.
\]



Thus


\[
\boxed{
Z_t = B_t^{-1}\sigma S_t\,\Delta(t,S_t),
\qquad \Delta=V_S.
}
\]



---

## What to remember

- Discounted option prices are martingales under \(\mathbb{Q}\).
- Martingale representation gives the stochastic integrand.
- Delta is the hedge ratio in complete diffusion models.
