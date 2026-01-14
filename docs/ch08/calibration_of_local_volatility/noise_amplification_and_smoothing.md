# Noise Amplification and Smoothing


Local volatility calibration is notoriously sensitive because the Dupire inversion uses **second derivatives in strike** and **first derivatives in maturity**. Differentiation amplifies noise, so smoothing is not optional—it is the core of a stable pipeline.

---

## Why differentiation amplifies noise


Suppose market call prices are observed with noise:

\[
C^{\text{obs}}(K,T) = C^{\star}(K,T) + \varepsilon(K,T).
\]



Finite differences approximate derivatives, e.g.

\[
\partial_{KK}C(K,T) \approx \frac{C(K+h,T)-2C(K,T)+C(K-h,T)}{h^2}.
\]



The division by \(h^2\) means:
- as you refine the grid (smaller \(h\)),
- noise \(\varepsilon\) is magnified like \(1/h^2\).

Thus, “more data points” can paradoxically make the raw Dupire estimate *worse* unless smoothing increases as resolution increases.

---

## Smoothing as regularization


Instead of differentiating raw quotes, one typically:

1. constructs a smooth surface \(\tilde C(K,T)\) (or \(\tilde\sigma_{\text{impl}}(K,T)\)),
2. applies Dupire differentiation to the smooth surface.

This is a form of **regularization**: you restrict attention to smooth surfaces compatible with data.

Common smoothing approaches:

- **Spline fits** per maturity (in strike or log-moneyness)
- **SVI** or other parametric smiles
- **Kernel regression / local polynomials**
- **Penalized least squares** with roughness penalty:

  \[
  \min \sum_j w_j(\tilde C_j - C^{\text{obs}}_j)^2 + \lambda \int |\partial_{KK}\tilde C|^2
  \]



---

## Arbitrage-aware smoothing


Smoothing must respect no-arbitrage conditions, otherwise the denominator \(\partial_{KK}C\) can become negative or near-zero, producing unstable or imaginary local vol.

Useful constraints include:

- **monotonicity in strike:** \(\partial_K C \le 0\),
- **convexity in strike:** \(\partial_{KK} C \ge 0\),
- **calendar monotonicity:** call price should not decrease with maturity (under standard assumptions).

In practice:
- remove violations before smoothing,
- fit a constrained surface,
- or adjust bid/ask bands until constraints are satisfied.

---

## Smoothing in total variance coordinates


A common stabilization trick is to smooth **total implied variance**

\[
w(k,T) = T\sigma_{\text{impl}}^2(k,T),
\quad k=\log(K/F_T),
\]


because \(w\) behaves more linearly across \(T\) and facilitates calendar-arbitrage checks.

One can:
- fit \(w(k,T)\) smoothly in both directions,
- compute model-consistent prices from the fitted \(w\),
- then apply Dupire.

---

## Practical pipeline (robust version)


1. convert raw quotes to consistent coordinates (forward, discounting, log-moneyness),
2. filter illiquid/outlier points,
3. build an arbitrage-clean surface in implied vol or total variance,
4. compute a smooth call surface,
5. apply Dupire with stable numerical differentiation,
6. post-smooth local vol if needed (mildly) to remove residual roughness.

---

## Key takeaways


- Dupire inversion is derivative-heavy; noise is amplified strongly.
- Smoothing is a *regularization step*, not cosmetic.
- Arbitrage-aware smoothing is critical to keep \(\partial_{KK}C\ge 0\).
- Total variance coordinates often improve stability.

---

## Further reading


- Gatheral, *The Volatility Surface*.
- Fengler, *Semiparametric Modeling of Implied Volatility*.
- Andersen & Piterbarg (practical surface construction and stability).
