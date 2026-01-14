# Delta Behavior Near the Money


As \(\tau\downarrow 0\), delta approaches a step function across the strike.

---

## Boundary layer


For a call, \(\Delta\approx \Phi_{\mathrm{N}}(d_1)\). As \(\tau\to 0\):
- \(S>K\Rightarrow \Delta\to 1\),
- \(S<K\Rightarrow \Delta\to 0\).

The transition occurs when \(\log(S/K)=\mathcal{O}(\sqrt{\tau})\).

---

## Width of transition


In log-moneyness \(x=\log(S/K)\),

\[
d_1\approx \frac{x}{\sigma\sqrt{\tau}}+\mathcal{O}(\sqrt{\tau}),
\]


so the transition width scales like \(\sigma\sqrt{\tau}\).

---

## What to remember


- Delta becomes step-like near maturity.
- The transition layer shrinks like \(\sqrt{\tau}\) in log-moneyness.
