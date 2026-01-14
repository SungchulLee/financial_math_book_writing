# Large-Strike and Small-Strike Asymptotics


Extreme strikes probe the tail behavior of the risk-neutral distribution.

---

## Tail control


For a call,


\[
C(t,S;K)=e^{-r\tau}\mathbb{E}[(S_T-K)^+],
\]



and for large \(K\) the main contribution is the tail \(\mathbb{P}(S_T>K)\). Similarly, deep OTM puts are controlled by \(\mathbb{P}(S_T<K)\).

---

## Black–Scholes tails


Since \(\log S_T\) is normal, tail probabilities have Gaussian asymptotics in log-strike.

---

## What to remember


- Extreme strikes encode tail probabilities.
- Implied volatility at extreme strikes reflects tail behavior and moment conditions.
