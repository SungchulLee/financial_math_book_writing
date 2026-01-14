# Model Definition


The Heston model is one of the most widely used **stochastic volatility models** in equity and FX markets. It extends Black–Scholes by modeling variance as a stochastic process while retaining analytical tractability.

---

## Dynamics under the risk-neutral measure


Under the risk-neutral measure \(\mathbb{Q}\), the Heston model is defined by

\[
\begin{aligned}
dS_t &= (r-q)S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S,\\
dV_t &= \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V,\\
d\langle W^S, W^V \rangle_t &= \rho\,dt,
\end{aligned}
\]


where:
- \(S_t\): asset price,
- \(V_t\): instantaneous variance,
- \(r\): risk-free rate,
- \(q\): dividend yield,
- \(\kappa\): mean-reversion speed,
- \(\theta\): long-run variance,
- \(\xi\): volatility of volatility,
- \(\rho\): correlation between price and variance shocks.

---

## Interpretation of parameters


Each parameter has a clear economic meaning:

- \(\theta\): long-term average variance implied by options,
- \(\kappa\): speed at which variance reverts to \(\theta\),
- \(\xi\): controls smile curvature and volatility-of-volatility,
- \(\rho\): controls skew via leverage effect,
- \(V_0\): sets short-maturity variance level.

---

## Relation to Black–Scholes


If variance is deterministic (e.g. \(\xi=0\)), the Heston model collapses to a time-dependent Black–Scholes model.

Thus, Heston can be seen as:
- a minimal extension of Black–Scholes,
- the simplest stochastic volatility model generating smiles.

---

## Key takeaways


- Heston introduces stochastic variance with mean reversion.
- It captures skew, smile, and term-structure effects.
- Analytical tractability makes it a market standard.

---

## Further reading


- Heston (1993), *A Closed-Form Solution for Options with Stochastic Volatility*.
- Gatheral, *The Volatility Surface*.
