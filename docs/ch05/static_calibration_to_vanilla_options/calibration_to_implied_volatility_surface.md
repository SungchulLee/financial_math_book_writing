# Calibration to the Implied Volatility Surface

In practice, *static* calibration to vanilla options is often performed not directly on prices, but on the **implied volatility surface**. The surface representation improves interpretability, makes quotes comparable across strikes/maturities, and helps expose arbitrage issues.

---

## 1. From prices to implied volatility

For a given maturity \(T\) and strike \(K\), a market quote is typically a bid/ask or mid option price
\[
C^{\text{mkt}}(K,T).
\]

The **Black–Scholes implied volatility** \(\sigma_{\text{impl}}(K,T)\) is defined as the unique \(\sigma\ge 0\) such that
\[
C^{\text{BS}}(K,T;\sigma) = C^{\text{mkt}}(K,T),
\]
where \(C^{\text{BS}}\) is the Black–Scholes call price (with the appropriate forward/discounting conventions).

### Why implied vols?

- **Scale normalization:** prices vary strongly with level, discounting, and maturity; implied vol is closer to a normalized “shape”.
- **Market quoting conventions:** many markets quote vol (or delta-vol) directly.
- **Diagnostics:** skew/smile and term structure become visually clear.

---

## 2. Parameterizing the surface

A volatility “surface” is really a function of strike and maturity. Common coordinates include:

- \((K,T)\) (strike, maturity),
- \((k,T)\) where \(k=\log(K/F_T)\) is **log-moneyness**,
- \((\Delta,T)\) where \(\Delta\) is option delta (FX-style quoting).

A robust workflow typically:

1. converts raw quotes into a consistent coordinate system (often log-moneyness),
2. performs filtering (liquidity, stale quotes, outliers),
3. fits an interpolant or parametric form.

### Common surface representations

- **Parametric smiles per maturity** (e.g., SVI, polynomial in \(k\))
- **Spline / kernel smoothing** across \((k,T)\)
- **Local volatility / total variance surface** \(w(k,T)=T\sigma_{\text{impl}}^2(k,T)\)

---

## 3. No-arbitrage considerations (static)

A “good” implied vol surface should not generate static arbitrage.

Typical constraints (informally):

- **Calendar arbitrage:** total variance should be non-decreasing in \(T\) for fixed moneyness.
- **Butterfly arbitrage:** call prices convex in strike; in implied vol coordinates this imposes shape constraints.

In practice, calibration is often done after (or together with) an **arbitrage-cleaning** step: remove obvious violations, widen bid/ask, or fit a surface constrained to be arbitrage-free.

---

## 4. Calibrating a model to the surface

Let the model depend on parameters \(\theta\). For each grid point \((K_i,T_i)\), we can compute model prices \(C^{\text{model}}(K_i,T_i;\theta)\) and then compute the corresponding implied vol
\[
\sigma^{\text{model}}_{\text{impl}}(K_i,T_i;\theta).
\]

Calibration “to the surface” means selecting \(\theta\) such that
\[
\sigma^{\text{model}}_{\text{impl}}(K_i,T_i;\theta)
\approx
\sigma^{\text{mkt}}_{\text{impl}}(K_i,T_i).
\]

This is usually posed as a weighted optimization problem (see next sections).

---

## 5. Practical pitfalls

- **Implied vol inversion noise:** deep OTM options or short maturities can make the implied-vol map ill-conditioned.
- **Data sparsity:** some maturities/strikes are illiquid; interpolation can dominate true information.
- **Smile parameterization bias:** a flexible surface can overfit noise; a rigid surface can distort the fit.
- **Numerical cost:** if model pricing is expensive, calibrating at many grid points may be slow.

---

## 6. Key takeaways

- Calibrating to the implied vol surface aligns with market conventions and improves interpretability.
- Surface construction and arbitrage filtering are part of the calibration pipeline.
- The choice of **objective function** and **weights** largely determines calibration stability (next files).

---

## Further reading

- Gatheral, *The Volatility Surface* (implied vol geometry and SVI).
- Fengler, *Semiparametric Modeling of Implied Volatility*.
- Andersen & Piterbarg, *Interest Rate Modeling* (practitioner calibration details).
