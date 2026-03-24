# Stability Issues


Even with smoothing, local volatility calibration can be unstable. Instability can appear as jagged \(\sigma_{\text{loc}}\) surfaces, extreme values near wings, or strong sensitivity to small quote changes. This section summarizes where instability comes from and how it is managed.

---

## Structural instability in the Dupire formula


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

## Boundary and extrapolation effects


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

## Short-maturity pathologies


As \(T\to 0\), option prices become very sensitive to microstructure, discrete dividends, and jump risk.
Even a small mismatch in forward/dividend handling can distort \(\partial_T C\) significantly.

Practitioner rules of thumb:
- exclude ultra-short maturities from the Dupire inversion,
- treat dividend modeling carefully (forward curve consistency),
- apply stronger smoothing in time near \(T=0\).

---

## Numerical differentiation stability


Even with a smooth fitted surface, numerical differentiation choices matter:

- finite difference step sizes,
- derivative schemes (central vs one-sided),
- interpolation grid spacing.

Stability improves when:
- derivatives are computed analytically from the fitted functional form (e.g., splines/SVI),
- differentiation is done in well-scaled coordinates (log-moneyness),
- the grid avoids extreme clustering where finite differences become tiny.

---

## Regularized local vol (post-processing)


A common practical approach is to compute a “raw” local vol estimate and then solve a *regularized reconstruction* problem:

\[
\min_{\sigma_{\text{loc}}} \; \|\text{Price}(\sigma_{\text{loc}}) - C^{\text{mkt}}\|^2
+ \lambda\,\mathcal{R}(\sigma_{\text{loc}}),
\]


where \(\mathcal{R}\) penalizes roughness in \(t\) and/or \(S\).

This shifts the problem from direct differentiation (very unstable) to a PDE-constrained optimization (more stable but computationally heavier).

---

## Validation for stability


You should validate local vol surfaces by:

- **re-calibration under perturbations** within bid/ask,
- checking for unreasonable spikes or negative local variance (should not occur),
- pricing simple exotics (barriers) and checking sensitivity,
- monitoring day-to-day surface movement.

---

## Key takeaways


- Local volatility calibration is intrinsically ill-posed; smoothing is necessary but not sufficient.
- Instability concentrates in wings, sparse maturities, and near expiry.
- Numerical differentiation and extrapolation are major sources of error.
- Regularized PDE-constrained approaches can improve stability at higher cost.

---

## Further reading


- Dupire (1994), “Pricing with a Smile”.
- Gatheral, *The Volatility Surface*.
- Rebonato, *Volatility and Correlation* (practitioner view on local vol pitfalls).

---

## Exercises

**Exercise 1.** The Dupire formula involves the ratio of a numerator $N = 2(\partial_T C + (r-q)K\partial_K C - qC)$ to a denominator $D = K^2 \partial_{KK}C$. Suppose both $N$ and $D$ are estimated with relative errors $\delta_N$ and $\delta_D$ respectively. Using first-order error propagation, show that the relative error in $\sigma_{\text{loc}}^2 = N/D$ satisfies

$$
\frac{\delta(\sigma_{\text{loc}}^2)}{\sigma_{\text{loc}}^2} \approx \sqrt{\delta_N^2 + \delta_D^2}
$$

Explain why the instability is worst when $|D|$ is small, even if $\delta_D$ is moderate.

---

**Exercise 2.** Consider a deep out-of-the-money call with $K = 150$, $S_0 = 100$, $T = 0.5$, and observed price $C^{\text{obs}} = 0.12$. The butterfly spread value $\partial_{KK}C$ estimated from neighboring strikes is $0.0003$. Estimate $\sigma_{\text{loc}}^2$ using a simplified Dupire formula with $r = q = 0$ and numerator $\partial_T C = 0.25$. Now perturb the butterfly spread by $\pm 0.0001$ and recompute. What is the relative change in $\sigma_{\text{loc}}^2$?

---

**Exercise 3.** A practitioner observes that the local volatility surface extracted on Monday and Tuesday (with very similar market data) differs by up to 30% in the short-maturity wings. List at least four specific sources of this instability, ordered from most to least impactful. For each source, propose a concrete mitigation strategy.

---

**Exercise 4.** In the regularized local volatility reconstruction

$$
\min_{\sigma_{\text{loc}}} \|\text{Price}(\sigma_{\text{loc}}) - C^{\text{mkt}}\|^2 + \lambda\,\mathcal{R}(\sigma_{\text{loc}})
$$

suppose $\mathcal{R}(\sigma_{\text{loc}}) = \int\int [(\partial_T \sigma_{\text{loc}})^2 + (\partial_K \sigma_{\text{loc}})^2]\,dK\,dT$. Explain the trade-off controlled by $\lambda$. What happens to the vanilla repricing error as $\lambda \to \infty$? How would you choose $\lambda$ in practice using an L-curve or cross-validation approach?

---

**Exercise 5.** At very short maturities ($T < 0.05$), discrete dividends introduce jumps in the forward price. Explain why ignoring discrete dividends leads to errors in $\partial_T C$ and hence in the extracted local volatility. Describe how using a proportional dividend model versus a cash dividend model affects the stability of the Dupire inversion near ex-dividend dates.

---

**Exercise 6.** As a stability check, a practitioner perturbs each market quote within its bid-ask spread (say $\pm 0.5$ vols) and re-calibrates the local volatility surface 100 times. The resulting distribution of $\sigma_{\text{loc}}(T_0, K_0)$ at a specific point has mean $0.22$ and standard deviation $0.08$. Is this level of uncertainty acceptable for hedging purposes? How would you use this bootstrap analysis to define confidence bands on the local volatility surface?

---

**Exercise 7.** Compare the stability properties of two approaches to local volatility calibration: (a) direct Dupire inversion from a smoothed implied volatility surface, and (b) PDE-constrained optimization that minimizes pricing errors subject to a smoothness penalty on $\sigma_{\text{loc}}$. Discuss computational cost, accuracy of vanilla repricing, and robustness to data noise for each approach. Under what conditions does method (b) justify its additional cost?
