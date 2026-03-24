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

---

## Exercises

**Exercise 1.** Let $\varepsilon_i \sim N(0, \delta^2)$ be independent noise on observed call prices at equally spaced strikes with spacing $h$. Show that the central finite-difference approximation to $\partial_{KK}C$ at a point has variance $6\delta^2/h^4$. If bid-ask noise is $\delta = 0.05$ and strike spacing is $h = 5$, compute the standard deviation of the estimated second derivative.

---

**Exercise 2.** A practitioner uses a cubic spline to smooth call prices across 15 strikes before applying the Dupire formula. The spline is fit by minimizing

$$
\sum_{j=1}^{15} w_j \bigl(\tilde{C}(K_j) - C_j^{\text{obs}}\bigr)^2 + \lambda \int_{K_{\min}}^{K_{\max}} \bigl(\tilde{C}''(K)\bigr)^2 \, dK
$$

Explain the role of the penalty parameter $\lambda$. What happens to the local volatility surface as $\lambda \to 0$? As $\lambda \to \infty$?

---

**Exercise 3.** Given three call prices at strikes $K-h$, $K$, $K+h$ for a fixed maturity, and call prices at the same strike $K$ for maturities $T$ and $T + \Delta T$, write down the finite-difference approximations for $\partial_{KK}C(K,T)$ and $\partial_T C(K,T)$. Then express the Dupire local variance estimate $\hat{\sigma}_{\text{loc}}^2(T,K)$ in terms of these five market prices, $r$, $q$, $h$, and $\Delta T$.

---

**Exercise 4.** The no-arbitrage convexity condition requires $\partial_{KK}C \ge 0$. Construct a numerical example with three call prices at strikes $K \in \{90, 100, 110\}$ where the butterfly spread is negative (i.e., $C(90) - 2C(100) + C(110) < 0$). Show that the Dupire formula yields $\sigma_{\text{loc}}^2 < 0$ at this point. Describe how you would correct this violation in practice.

---

**Exercise 5.** Explain why working in total implied variance coordinates $w(k, T) = T\sigma_{\text{impl}}^2(k, T)$ with $k = \ln(K/F_T)$ facilitates calendar-arbitrage checking. Specifically, show that the condition $\partial_T w(k, T) \ge 0$ for fixed $k$ is necessary for absence of calendar arbitrage, and relate this to the positivity of the numerator in the Dupire formula.

---

**Exercise 6.** Compare two smoothing approaches for a set of 50 option quotes across 5 maturities: (a) independent cubic spline per maturity, and (b) joint SVI parameterization across all maturities. Discuss which approach is more likely to satisfy calendar-spread arbitrage constraints and why. What additional steps are needed for approach (a) to ensure time-consistency?

---

**Exercise 7.** Consider the penalized least-squares problem with a roughness penalty in both strike and maturity directions:

$$
\min_{\tilde{C}} \sum_j w_j\bigl(\tilde{C}_j - C_j^{\text{obs}}\bigr)^2 + \lambda_K \int (\partial_{KK}\tilde{C})^2 \, dK + \lambda_T \int (\partial_T \tilde{C})^2 \, dT
$$

Discuss why $\lambda_K$ and $\lambda_T$ may need to be chosen differently. If strikes are densely sampled but maturities are sparse, which penalty should be larger and why?
