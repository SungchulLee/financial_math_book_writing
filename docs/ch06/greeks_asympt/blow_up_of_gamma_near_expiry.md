# Blow-Up of Gamma Near Expiry


For vanilla options, gamma becomes large near expiry around the strike.

---

## Scaling


In Black–Scholes,

\[
\Gamma(t,S)\approx \frac{1}{S\sigma\sqrt{\tau}}\,\varphi(d_1),
\qquad \tau=T-t.
\]


Thus near the money,

\[
\boxed{\Gamma \sim \tau^{-1/2}.}
\]



---

## Localization


As \(\tau\downarrow 0\), \(\varphi(d_1)\) localizes near \(S\approx K\), so gamma forms a narrow peak around the strike.

---

## Interpretation


Diffusion smoothing replaces the payoff’s kink (distributional second derivative) by a bump of width \(\mathcal{O}(\sqrt{\tau})\) and height \(\mathcal{O}(\tau^{-1/2})\).

---

## What to remember


- Gamma spikes near the strike as maturity approaches.
- This amplifies discrete hedging error and makes numerical gamma unstable.
