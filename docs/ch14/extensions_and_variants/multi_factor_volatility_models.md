# Multi-Factor Volatility Models


Single-factor stochastic volatility models often fail to capture the full richness of volatility dynamics. **Multi-factor volatility models** introduce additional latent factors to improve realism and stability.

---

## Motivation for multiple factors


Empirical volatility exhibits:
- short-term fluctuations,
- long-term persistence,
- regime-dependent behavior.

A single volatility factor cannot capture all time scales simultaneously.

---

## General structure


A generic multi-factor model may be written as

\[
V_t = \sum_{i=1}^n V_t^{(i)},
\]


where each factor satisfies its own stochastic dynamics, often with different mean-reversion speeds.

---

## Examples


- **Two-factor Heston:** fast and slow variance components,
- **Long/short memory models:** separated time scales,
- **Factor-based rough approximations:** Markovian lifts of rough volatility.

These models improve fit and stability across maturities.

---

## Calibration and identifiability


Adding factors increases flexibility but introduces:
- identifiability challenges,
- higher calibration variance,
- need for stronger regularization.

Calibration typically requires:
- wide maturity coverage,
- strong parameter constraints,
- stability-focused objectives.

---

## Key takeaways


- Multi-factor models capture multiple volatility time scales.
- They improve surface fit and dynamic consistency.
- Complexity must be balanced against stability.

---

## Further reading


- Bergomi, *Stochastic Volatility Modeling*.
- Fouque et al., multiscale volatility models.
- Abi Jaber et al., multi-factor rough volatility.
