# Calibration to the Implied Volatility Surface


In practice, *static* calibration to vanilla options is often performed not directly on prices, but on the **implied volatility surface**. The surface representation improves interpretability, makes quotes comparable across strikes/maturities, and helps expose arbitrage issues.

---

## From prices to implied volatility


For a given maturity \(T\) and strike \(K\), a market quote is typically a bid/ask or mid option price

\[
C^{\text{mkt}}(K,T).
\]



The **Black–Scholes implied volatility** \(\sigma_{\text{impl}}(K,T)\) is defined as the unique \(\sigma\ge 0\) such that

\[
C^{\text{BS}}(K,T;\sigma) = C^{\text{mkt}}(K,T),
\]


where \(C^{\text{BS}}\) is the Black–Scholes call price (with the appropriate forward/discounting conventions).

### 1. Why implied vols?


- **Scale normalization:** prices vary strongly with level, discounting, and maturity; implied vol is closer to a normalized “shape”.
- **Market quoting conventions:** many markets quote vol (or delta-vol) directly.
- **Diagnostics:** skew/smile and term structure become visually clear.

---

## Parameterizing the surface


A volatility “surface” is really a function of strike and maturity. Common coordinates include:

- \((K,T)\) (strike, maturity),
- \((k,T)\) where \(k=\log(K/F_T)\) is **log-moneyness**,
- \((\Delta,T)\) where \(\Delta\) is option delta (FX-style quoting).

A robust workflow typically:

1. converts raw quotes into a consistent coordinate system (often log-moneyness),
2. performs filtering (liquidity, stale quotes, outliers),
3. fits an interpolant or parametric form.

### 1. Common surface representations


- **Parametric smiles per maturity** (e.g., SVI, polynomial in \(k\))
- **Spline / kernel smoothing** across \((k,T)\)
- **Local volatility / total variance surface** \(w(k,T)=T\sigma_{\text{impl}}^2(k,T)\)

---

## No-arbitrage considerations (static)


A “good” implied vol surface should not generate static arbitrage.

Typical constraints (informally):

- **Calendar arbitrage:** total variance should be non-decreasing in \(T\) for fixed moneyness.
- **Butterfly arbitrage:** call prices convex in strike; in implied vol coordinates this imposes shape constraints.

In practice, calibration is often done after (or together with) an **arbitrage-cleaning** step: remove obvious violations, widen bid/ask, or fit a surface constrained to be arbitrage-free.

---

## Calibrating a model to the surface


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

## Practical pitfalls


- **Implied vol inversion noise:** deep OTM options or short maturities can make the implied-vol map ill-conditioned.
- **Data sparsity:** some maturities/strikes are illiquid; interpolation can dominate true information.
- **Smile parameterization bias:** a flexible surface can overfit noise; a rigid surface can distort the fit.
- **Numerical cost:** if model pricing is expensive, calibrating at many grid points may be slow.

---

## Key takeaways


- Calibrating to the implied vol surface aligns with market conventions and improves interpretability.
- Surface construction and arbitrage filtering are part of the calibration pipeline.
- The choice of **objective function** and **weights** largely determines calibration stability (next files).

---

## Further reading


- Gatheral, *The Volatility Surface* (implied vol geometry and SVI).
- Fengler, *Semiparametric Modeling of Implied Volatility*.
- Andersen & Piterbarg, *Interest Rate Modeling* (practitioner calibration details).

---

## Exercises

**Exercise 1.** Define the Black--Scholes implied volatility $\sigma_{\text{impl}}(K,T)$ precisely. For a call option with $S_0 = 100$, $K = 100$, $T = 0.25$, $r = 0.02$, $q = 0$, and market price $C^{\text{mkt}} = 5.50$, describe how you would numerically solve for $\sigma_{\text{impl}}$ using Newton's method. Write down the iteration formula and explain why Vega appears in the denominator.

---

**Exercise 2.** Explain why implied volatility is more convenient than raw prices for visualizing the volatility surface. Given the following data: $\sigma_{\text{impl}}(90, 0.25) = 0.28$, $\sigma_{\text{impl}}(100, 0.25) = 0.22$, $\sigma_{\text{impl}}(110, 0.25) = 0.20$, sketch the smile at $T = 0.25$ and identify the skew. What market phenomenon typically produces this pattern for equity index options?

---

**Exercise 3.** Define the total variance surface $w(k,T) = T\sigma_{\text{impl}}^2(k,T)$ where $k = \ln(K/F_T)$. State the calendar arbitrage condition in terms of $w$ and explain why it is easier to check in total variance coordinates than in implied volatility coordinates.

---

**Exercise 4.** A practitioner constructs an implied volatility surface from 50 market quotes using cubic spline interpolation in log-moneyness for each of 5 maturities. After interpolation, they discover that the butterfly spread $C(K-h) - 2C(K) + C(K+h) < 0$ at a specific point. What type of arbitrage does this violate? Propose two methods to repair the surface.

---

**Exercise 5.** When computing model implied volatilities $\sigma_{\text{impl}}^{\text{model}}(K_i, T_i; \theta)$ for calibration, one must numerically invert the Black--Scholes formula for each model price. Discuss the computational cost of this nested inversion when calibrating a Heston model to 200 vanilla options. How does this compare to calibrating directly in price space?

---

**Exercise 6.** Compare calibrating in log-moneyness coordinates $k = \ln(K/F_T)$ versus delta-parameterized coordinates $\Delta$. For which market (equity vs. FX) is each convention more natural? How does the choice of coordinates affect the interpolation quality in the wings?

---

**Exercise 7.** Data sparsity can make surface construction unreliable. Suppose you have 3 strikes at $T = 0.1$, 8 strikes at $T = 0.5$, and 5 strikes at $T = 2.0$. Describe how you would handle this uneven data density when constructing a smooth surface. What risks arise from over-interpolating in sparse regions, and how do these propagate to calibrated model parameters?
