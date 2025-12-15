# Tikhonov Regularization

Ill-posed calibration problems are often stabilized by **regularization**, which introduces additional structure or prior information. The most classical approach is **Tikhonov regularization**, widely used in inverse problems and numerical analysis.

---

## 1. Motivation

Recall a typical least-squares calibration problem:
\[
\min_{\theta \in \Theta} \; \frac12\|F(\theta) - y\|_W^2,
\]
where \(F\) is the forward pricing map and \(y\) denotes market data.

If the Jacobian of \(F\) is ill-conditioned, small data noise can lead to large parameter fluctuations. Tikhonov regularization addresses this by penalizing undesirable parameter behavior.

---

## 2. Basic Tikhonov formulation

The Tikhonov-regularized problem is
\[
\min_{\theta \in \Theta} \;
\frac12\|F(\theta) - y\|_W^2
+ \frac{\lambda}{2}\|L(\theta - \theta_0)\|^2.
\]

Components:
- \(\lambda > 0\): regularization strength,
- \(L\): regularization operator (often identity),
- \(\theta_0\): reference or prior parameter vector.

Special cases:
- **Zero-order Tikhonov:** \(L = I\), penalizes large parameter magnitudes.
- **Shifted Tikhonov:** pulls parameters toward a prior guess \(\theta_0\).

---

## 3. Linearized analysis

For a linear forward map \(F(\theta) = A\theta\), the solution satisfies
\[
(A^\top W A + \lambda L^\top L)\theta
= A^\top W y + \lambda L^\top L \theta_0.
\]

Key consequences:
- the matrix becomes invertible even if \(A^\top W A\) is singular,
- small singular values are damped,
- variance is reduced at the cost of bias.

This bias–variance trade-off is central to regularization.

---

## 4. Interpretation as Bayesian prior

Tikhonov regularization admits a Bayesian interpretation:

- likelihood: \(y \mid \theta \sim \mathcal{N}(F(\theta), W^{-1})\),
- prior: \(\theta \sim \mathcal{N}(\theta_0, (\lambda L^\top L)^{-1})\).

Then the regularized solution is the **maximum a posteriori (MAP)** estimator.

---

## 5. Choosing the regularization parameter

Selecting \(\lambda\) is critical. Common approaches:

- **L-curve method:** plot fit vs regularization norm,
- **discrepancy principle:** match residual size to noise level,
- **cross-validation:** assess out-of-sample stability,
- **heuristics:** start large, decrease until instability appears.

In practice, calibration stability over time is often the most relevant criterion.

---

## 6. Practical considerations in finance

- Regularization should not dominate liquid, well-identified directions.
- Over-regularization can suppress meaningful smile/skew information.
- Prior parameters should be economically interpretable.

---

## 7. Key takeaways

- Tikhonov regularization stabilizes ill-posed calibration problems.
- It trades bias for variance reduction.
- The method has a clear Bayesian interpretation.
- Choosing the regularization strength is as important as choosing the model.

---

## Further reading

- Tikhonov & Arsenin, *Solutions of Ill-Posed Problems*.
- Engl, Hanke & Neubauer, *Regularization of Inverse Problems*.
- Tarantola, *Inverse Problem Theory*.
