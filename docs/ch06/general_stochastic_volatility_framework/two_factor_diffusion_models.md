# Two-Factor Diffusion Models

Stochastic volatility models extend Black–Scholes by introducing **additional sources of randomness**. The most common framework is a **two-factor diffusion**, where asset price and volatility evolve jointly.

---

## 1. General structure

A generic two-factor stochastic volatility model is written as

\[
\begin{aligned}
dS_t &= \mu(S_t, V_t, t)\,dt + \sigma(S_t, V_t, t)\,dW_t^S,\\
dV_t &= a(V_t, t)\,dt + b(V_t, t)\,dW_t^V,
\end{aligned}
\]


where:
- \(S_t\) is the asset price,
- \(V_t\) is the variance or volatility factor,
- \(W^S, W^V\) are Brownian motions (possibly correlated).

The second factor captures **randomness in volatility itself**.

---

## 2. Examples of two-factor models

Prominent examples include:

- **Heston model:** square-root variance process,
- **Hull–White stochastic volatility:** lognormal variance,
- **SABR model:** stochastic volatility with elasticity,
- **Stein–Stein model:** Ornstein–Uhlenbeck volatility.

Despite differences, all share the same two-factor diffusion structure.

---

## 3. Economic interpretation

The volatility factor represents:
- changing market uncertainty,
- latent risk perception,
- aggregation of unhedgeable risks.

Because volatility is not directly traded, this factor introduces **market incompleteness**.

---

## 4. Implications for pricing

Two-factor diffusions imply:
- non-Gaussian return distributions,
- volatility clustering,
- implied volatility smiles and term structures.

Option prices depend on the joint law of \((S_T, V_T)\), not just marginal variance.

---

## 5. Key takeaways

- Two-factor diffusions are the canonical stochastic volatility framework.
- They generalize Black–Scholes while remaining Markovian.
- Market incompleteness is intrinsic to these models.

---

## Further reading

- Heston (1993).
- Hull & White (1987).
- Fouque et al., *Multiscale Stochastic Volatility Models*.
