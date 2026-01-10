# Discrete-Time Hedging Error

Continuous-time delta hedging is an idealization. Discrete rebalancing introduces a random hedging error influenced by gamma.

---

## Heuristic structure

For hedge times \(t_k\), with \(\theta_k=\Delta(t_k,S_{t_k})\), the hedging error can be related to the replacement of quadratic variation by realized squared increments:

\[
\mathrm{HE} \approx
\frac{1}{2}\sum_k \Gamma(t_k,S_{t_k})(\Delta S_k)^2
-\frac{1}{2}\int_0^T \Gamma(t,S_t)\,\mathrm{d}\langle S\rangle_t.
\]



---

## What to remember

- Discrete hedging creates variance-like error terms.
- Near-expiry gamma blow-up magnifies the error.
