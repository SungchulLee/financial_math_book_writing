# Stability Issues

Even with smoothing, local volatility calibration can be unstable. Instability can appear as jagged \(\sigma_{\text{loc}}\) surfaces, extreme values near wings, or strong sensitivity to small quote changes. This section summarizes where instability comes from and how it is managed.

---

## 1. Structural instability in the Dupire formula

The Dupire expression

\[
\sigma_{\text{loc}}^2(T,K)
= \frac{2\left(\partial_T C + (r-q)K\partial_K C - q C\right)}
{K^2\,\partial_{KK} C}
\]


has two built-in amplifiers:

1. **Differentiation amplifies noise** (numerator and denominator).
2. **Division by curvature**: if \(\partial_{KK}C\) is small, errors explode.

The curvature is typically smallest in:
- far wings (deep OTM),
- regions with sparse data,
- maturities with wide bid/ask spreads.

---

## 2. Boundary and extrapolation effects

Local vol requires a surface over a domain in \((K,T)\), but data are finite:

- strikes are available only in a range,
- maturities are discrete.

Thus extrapolation is unavoidable, and instability often concentrates near:

- smallest maturity \(T\to 0\),
- largest maturity (scarce quotes),
- extreme strikes where extrapolation dominates.

Common mitigation:
- enforce reasonable asymptotic wing behavior (e.g., SVI-inspired),
- freeze or damp local vol outside liquid regions.

---

## 3. Short-maturity pathologies

As \(T\to 0\), option prices become very sensitive to microstructure, discrete dividends, and jump risk.
Even a small mismatch in forward/dividend handling can distort \(\partial_T C\) significantly.

Practitioner rules of thumb:
- exclude ultra-short maturities from the Dupire inversion,
- treat dividend modeling carefully (forward curve consistency),
- apply stronger smoothing in time near \(T=0\).

---

## 4. Numerical differentiation stability

Even with a smooth fitted surface, numerical differentiation choices matter:

- finite difference step sizes,
- derivative schemes (central vs one-sided),
- interpolation grid spacing.

Stability improves when:
- derivatives are computed analytically from the fitted functional form (e.g., splines/SVI),
- differentiation is done in well-scaled coordinates (log-moneyness),
- the grid avoids extreme clustering where finite differences become tiny.

---

## 5. Regularized local vol (post-processing)

A common practical approach is to compute a “raw” local vol estimate and then solve a *regularized reconstruction* problem:

\[
\min_{\sigma_{\text{loc}}} \; \|\text{Price}(\sigma_{\text{loc}}) - C^{\text{mkt}}\|^2
+ \lambda\,\mathcal{R}(\sigma_{\text{loc}}),
\]


where \(\mathcal{R}\) penalizes roughness in \(t\) and/or \(S\).

This shifts the problem from direct differentiation (very unstable) to a PDE-constrained optimization (more stable but computationally heavier).

---

## 6. Validation for stability

You should validate local vol surfaces by:

- **re-calibration under perturbations** within bid/ask,
- checking for unreasonable spikes or negative local variance (should not occur),
- pricing simple exotics (barriers) and checking sensitivity,
- monitoring day-to-day surface movement.

---

## 7. Key takeaways

- Local volatility calibration is intrinsically ill-posed; smoothing is necessary but not sufficient.
- Instability concentrates in wings, sparse maturities, and near expiry.
- Numerical differentiation and extrapolation are major sources of error.
- Regularized PDE-constrained approaches can improve stability at higher cost.

---

## Further reading

- Dupire (1994), “Pricing with a Smile”.
- Gatheral, *The Volatility Surface*.
- Rebonato, *Volatility and Correlation* (practitioner view on local vol pitfalls).
