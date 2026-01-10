# Dupire Equation as an Inverse Problem

Local volatility models provide an *exact* fit (in principle) to a continuum of vanilla option prices. This exactness comes at a cost: constructing the local volatility surface is a **highly ill-posed inverse problem** because it requires differentiating noisy market data.

---

## 1. The local volatility model

In the (risk-neutral) local volatility model, the underlying \(S_t\) follows

\[
dS_t = (r-q)S_t\,dt + \sigma_{\text{loc}}(t,S_t)\,S_t\,dW_t,
\]


where \(r\) is the risk-free rate, \(q\) is the dividend yield (or convenience yield), and
\(\sigma_{\text{loc}}(t,S)\) is the **local volatility** function to be calibrated.

Given \(\sigma_{\text{loc}}\), the model implies a unique surface of European option prices \(C(K,T)\).

---

## 2. Dupire’s forward equation

Let \(C(K,T)\) denote the time-0 price of a European call with strike \(K\) and maturity \(T\).
Under standard smoothness assumptions, Dupire derived a forward PDE relating \(C\) and \(\sigma_{\text{loc}}\).

A common (simplified) form is:

\[
\partial_T C(K,T)
= \frac12\,\sigma_{\text{loc}}^2(T,K)\,K^2\,\partial_{KK} C(K,T)
- (r-q)K\,\partial_K C(K,T)
+ q\,C(K,T),
\]


where derivatives are with respect to strike.

Solving this equation *forward* is the pricing problem.

---

## 3. Inverting Dupire: extracting local volatility

Rearranging the forward equation yields an expression for local variance

\[
\sigma_{\text{loc}}^2(T,K)
= \frac{2\left(\partial_T C + (r-q)K\partial_K C - q C\right)}
{K^2\,\partial_{KK} C}.
\]



This reveals why calibration is an inverse problem:

- it requires \(\partial_T C\) and \(\partial_{KK} C\),
- these are *derivatives* of market prices, which are observed only at discrete points and contaminated by noise.

Thus, the mapping

\[
C(\cdot,\cdot) \longmapsto \sigma_{\text{loc}}(\cdot,\cdot)
\]


is an unstable inversion involving differentiation and division by curvature.

---

## 4. Relationship to implied volatility

Market data are often given as implied vol \(\sigma_{\text{impl}}(K,T)\), not prices.
One may:

1. convert implied vol to prices via Black–Scholes,
2. interpolate to a smooth surface,
3. apply Dupire to the smoothed price surface.

Alternatively, Dupire can be written directly in terms of implied vol or total variance, but the same inverse-problem issues remain: derivatives are needed.

---

## 5. Key takeaways

- Dupire provides a *theoretical* route from a smooth call price surface to \(\sigma_{\text{loc}}(T,K)\).
- Calibration is an inverse problem because it requires **differentiating noisy, discrete data**.
- Practical implementation requires smoothing, arbitrage filtering, and careful numerics.

---

## Further reading

- Dupire (1994), “Pricing with a Smile”.
- Gatheral, *The Volatility Surface* (local vol and implied vol geometry).
- Fengler, *Semiparametric Modeling of Implied Volatility* (surface construction).
