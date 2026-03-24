# Tikhonov Regularization


Ill-posed calibration problems are often stabilized by **regularization**, which introduces additional structure or prior information. The most classical approach is **Tikhonov regularization**, widely used in inverse problems and numerical analysis.

---

## Motivation


Recall a typical least-squares calibration problem:

\[
\min_{\theta \in \Theta} \; \frac12\|F(\theta) - y\|_W^2,
\]


where \(F\) is the forward pricing map and \(y\) denotes market data.

If the Jacobian of \(F\) is ill-conditioned, small data noise can lead to large parameter fluctuations. Tikhonov regularization addresses this by penalizing undesirable parameter behavior.

---

## Basic Tikhonov formulation


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

## Linearized analysis


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

## Interpretation as Bayesian prior


Tikhonov regularization admits a Bayesian interpretation:

- likelihood: \(y \mid \theta \sim \mathcal{N}(F(\theta), W^{-1})\),
- prior: \(\theta \sim \mathcal{N}(\theta_0, (\lambda L^\top L)^{-1})\).

Then the regularized solution is the **maximum a posteriori (MAP)** estimator.

---

## Choosing the regularization parameter


Selecting \(\lambda\) is critical. Common approaches:

- **L-curve method:** plot fit vs regularization norm,
- **discrepancy principle:** match residual size to noise level,
- **cross-validation:** assess out-of-sample stability,
- **heuristics:** start large, decrease until instability appears.

In practice, calibration stability over time is often the most relevant criterion.

---

## Practical considerations in finance


- Regularization should not dominate liquid, well-identified directions.
- Over-regularization can suppress meaningful smile/skew information.
- Prior parameters should be economically interpretable.

---

## Key takeaways


- Tikhonov regularization stabilizes ill-posed calibration problems.
- It trades bias for variance reduction.
- The method has a clear Bayesian interpretation.
- Choosing the regularization strength is as important as choosing the model.

---

## Further reading


- Tikhonov & Arsenin, *Solutions of Ill-Posed Problems*.
- Engl, Hanke & Neubauer, *Regularization of Inverse Problems*.
- Tarantola, *Inverse Problem Theory*.

---

## Exercises

**Exercise 1.** For the linear forward map $F(\theta) = A\theta$, derive the Tikhonov-regularized solution

$$
\hat{\theta}_\lambda = (A^\top W A + \lambda I)^{-1}(A^\top W y + \lambda \theta_0)
$$

by setting the gradient of $\frac{1}{2}\|A\theta - y\|_W^2 + \frac{\lambda}{2}\|\theta - \theta_0\|^2$ to zero. Show that as $\lambda \to 0$, $\hat{\theta}_\lambda$ approaches the ordinary least-squares solution, and as $\lambda \to \infty$, $\hat{\theta}_\lambda \to \theta_0$.

---

**Exercise 2.** Let $A$ have singular value decomposition $A = U\Sigma V^\top$ with singular values $\sigma_1 \ge \cdots \ge \sigma_d > 0$. Show that the Tikhonov solution with $L = I$ and $\theta_0 = 0$ can be written in the SVD basis as

$$
\hat{\theta}_\lambda = \sum_{i=1}^d \frac{\sigma_i^2}{\sigma_i^2 + \lambda} \frac{u_i^\top y}{\sigma_i} v_i
$$

Interpret the filter factors $\sigma_i^2/(\sigma_i^2 + \lambda)$ and explain how they suppress components with small singular values.

---

**Exercise 3.** Derive the Bayesian interpretation of Tikhonov regularization. Starting from the prior $\theta \sim \mathcal{N}(\theta_0, (\lambda L^\top L)^{-1})$ and likelihood $y|\theta \sim \mathcal{N}(A\theta, W^{-1})$, show that the MAP estimator coincides with the Tikhonov solution. What does the regularization parameter $\lambda$ correspond to in Bayesian terms?

---

**Exercise 4.** The L-curve method plots $\log\|F(\hat{\theta}_\lambda) - y\|$ versus $\log\|L(\hat{\theta}_\lambda - \theta_0)\|$ for varying $\lambda$. The optimal $\lambda$ is chosen at the "corner" of the L-shaped curve. Explain geometrically why the corner represents the best compromise between fit and regularity. What happens if the L-curve has no clear corner?

---

**Exercise 5.** The discrepancy principle selects $\lambda$ such that $\|F(\hat{\theta}_\lambda) - y\| \approx \delta$, where $\delta$ is the estimated noise level. If market quotes have bid-ask half-widths $\sigma_i$, propose how to estimate $\delta$ from these half-widths. What are the limitations of this approach when the model is misspecified (so that the residual has a systematic component in addition to noise)?

---

**Exercise 6.** A Heston model is calibrated to 30 option prices using Tikhonov regularization with $\theta_0$ equal to yesterday's parameters. The regularization parameter is $\lambda = 0.1$. Today, a sudden market crash occurs, and the unregularized calibration yields $v_0 = 0.12$ (compared to yesterday's $v_0 = 0.04$). Compute the regularized estimate. Is the regularization appropriate in this scenario? How would you design an adaptive $\lambda$ that allows large parameter changes during genuine market events?

---

**Exercise 7.** Compare zero-order Tikhonov ($L = I$) with first-order Tikhonov ($L = D_1$, the first-difference operator) for calibrating a piecewise-constant local volatility surface on a grid of 10 maturities. What structural property does each penalty enforce? Which is more appropriate for this problem and why?
