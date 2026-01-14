# Instability of Higher-Order Greeks


Higher-order Greeks can be unstable to estimate, especially near maturity and near payoff kinks.

---

## Noise amplification


Second derivatives amplify noise:

\[
V_{SS}(S)\approx \frac{V(S+h)-2V(S)+V(S-h)}{h^2}.
\]



---

## What to remember


- Gamma estimation is numerically ill-conditioned near expiry.
- Robust systems often smooth or bucket sensitivities.
