# Short-Maturity Asymptotics


Let \(\tau:=T-t\downarrow 0\). Short-maturity asymptotics describe how prices concentrate near the current state.

---

## Diffusive scaling


Typical diffusion increments are \(\mathcal{O}(\sqrt{\tau})\), so near-the-money regions dominate short-time pricing.

---

## Black–Scholes log return



\[
\log\frac{S_T}{S_t}
=
\left(r-\frac{1}{2}\sigma^2\right)\tau+\sigma\sqrt{\tau}\,Z,
\qquad Z\sim\mathcal{N}(0,1).
\]



---

## Far OTM is exponentially small


For strikes far from \(S\), short-time prices often scale like


\[
V(t,S;K)\approx \exp\!\left(-\frac{I(S,K)}{\tau}\right),
\]



where \(I\) is a rate function (large deviations).

---

## What to remember


- Typical moves are \(\mathcal{O}(\sqrt{\tau})\).
- ATM dominates; far OTM is exponentially small in \(1/\tau\).
