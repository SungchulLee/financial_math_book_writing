# Small-Volatility Asymptotics

Consider \(\sigma\downarrow 0\). Randomness vanishes and prices approach deterministic limits.

---

## Deterministic limit

As \(\sigma\to 0\),
\[
\mathrm{d}S_t=rS_t\,\mathrm{d}t+\sigma S_t\,\mathrm{d}W_t
\to
\dot{S}_t=rS_t,
\]
so \(S_T\to S e^{r\tau}\).

---

## OTM becomes exponentially small

If \(K>S e^{r\tau}\) (OTM call in the deterministic limit),
\[
C(t,S;K)\approx \exp\!\left(-\frac{c}{\sigma^2}\right).
\]

---

## What to remember

- OTM prices shrink exponentially in \(1/\sigma^2\).
- These asymptotics connect to large deviations and Laplace principles.
