# Ill-Posedness and Non-Uniqueness


Inverse problems are often **ill-posed** in the sense of Hadamard. Calibration inherits this ill-posedness: market data are noisy and incomplete, and multiple parameter sets can fit the same data almost equally well.

---

## Hadamard well-posedness


A problem is **well-posed** if:

1. **Existence:** a solution exists.
2. **Uniqueness:** the solution is unique.
3. **Stability:** the solution depends continuously on the data.

Calibration can violate (2) and (3) even when (1) holds.

---

## Why calibration is often ill-posed


### 1. Incomplete information


Market quotes provide a finite set of prices (\(m\) instruments), while models may have:

- many parameters (\(d\) large),
- hidden state variables,
- functional degrees of freedom (e.g., a local volatility surface \(\sigma_{\text{loc}}(t,S)\)).

Even when \(m\ge d\), the effective rank of the Jacobian may be much smaller due to redundancy and weak sensitivity.

### 2. Noisy data


Observed prices are affected by:

- bid–ask spreads,
- stale quotes,
- microstructure noise,
- interpolation/extrapolation artifacts (surface construction).

Let the true data be \(y^\star\) and observed data \(y = y^\star + \varepsilon\). If the inverse map is unstable, \(\varepsilon\) is amplified into large parameter errors.

### 3. Model misspecification


Even with perfect data, the model may be unable to fit all instruments:

\[
y \notin \mathrm{Range}(F).
\]


Then the optimization problem has a best-fit solution but no exact inverse.

---

## Non-uniqueness mechanisms


### 1. Flat directions (parameter degeneracy)


If the loss surface has valleys, many \(\theta\) yield nearly identical fit:

\[
\mathcal{L}(F(\theta),y) \approx \text{constant along a curve/manifold}.
\]



This occurs when two parameters play similar roles (e.g., both affect overall variance level).

### 2. Over-parameterization


Adding parameters can reduce in-sample error without improving explanatory power. Two common symptoms:

- extremely large/small parameter values,
- unstable calibrated parameters day-to-day.

### 3. Hidden constraints and bounds


Constraints (positivity, Feller condition, no-arbitrage filters) can create multiple local minima:
- one “good fit” region near the boundary,
- another interior region with slightly worse fit but better stability.

---

## A linearized view: conditioning and singular values


Around a reference \(\theta_0\), with \(F(\theta)\approx F(\theta_0)+J\Delta\theta\), least squares suggests

\[
\Delta\theta \approx (J^\top W J)^{-1}J^\top W (y - F(\theta_0)).
\]



If \(J^\top WJ\) is ill-conditioned (small eigenvalues), then:

- the inverse is numerically unstable,
- \(\|\Delta\theta\|\) can blow up relative to data noise.

This connects directly to **regularization** (Chapter 5.3).

---

## Practical diagnostics


- **Sensitivity / Greeks-to-parameters:** check Jacobian magnitudes.
- **Bootstrap / re-sample quotes:** re-calibrate after perturbing \(y\) within bid–ask.
- **Profile likelihood / one-parameter sweeps:** visualize flat directions.
- **Multiple initializations:** detect multi-modality / local minima.

---

## Key takeaways


- Calibration often fails **uniqueness** and **stability**.
- Non-uniqueness is not a bug in the optimizer; it is structural.
- Regularization and better parameterizations are standard remedies.

---

## Further reading


- Hadamard, *Lectures on Cauchy’s problem in linear partial differential equations*.
- Engl, Hanke & Neubauer, *Regularization of Inverse Problems*.
- Gatheral, *The Volatility Surface* (practical calibration issues).

---

## Exercises

**Exercise 1.** State the three Hadamard conditions for well-posedness. Give a concrete calibration example where condition (2) (uniqueness) fails: describe a two-parameter model and a set of market observables such that two distinct parameter vectors produce the same model prices.

---

**Exercise 2.** Consider a model with forward pricing map $F:\mathbb{R}^d \to \mathbb{R}^m$ and Jacobian $J = \partial F/\partial\theta$ evaluated at $\theta_0$. Suppose the singular value decomposition of $J$ is $J = U\Sigma V^\top$ with singular values $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_{\min(m,d)}$. Show that the condition number of the normal equations matrix $J^\top J$ is

$$
\kappa(J^\top J) = \left(\frac{\sigma_1}{\sigma_d}\right)^2
$$

and explain why a large condition number implies instability in the calibrated parameters.

---

**Exercise 3.** A practitioner calibrates a stochastic volatility model on Monday and obtains parameters $\theta_{\text{Mon}}$. On Tuesday, with nearly identical market data (perturbation $\|\varepsilon\| < 0.01$), the calibration yields $\theta_{\text{Tue}}$ with $\|\theta_{\text{Tue}} - \theta_{\text{Mon}}\| > 10$. Which of the three Hadamard conditions is violated? Propose two practical remedies from the diagnostics discussed in this section.

---

**Exercise 4.** Let $F(\alpha, \beta) = \alpha \beta$ be a simplified pricing function mapping two parameters to a single observable $y$. Show that the level set $\{(\alpha,\beta) : F(\alpha,\beta) = y\}$ is a hyperbola for $y \neq 0$. Compute the Jacobian $J$ at the point $(\alpha_0, \beta_0)$ and verify that the linearized inverse problem has a one-dimensional null space when $m = 1$ and $d = 2$.

---

**Exercise 5.** Suppose market data $y$ lies outside the range of the forward map, i.e., $y \notin \mathrm{Range}(F)$, due to model misspecification. Show that the least-squares objective

$$
\mathcal{L}(\theta) = \frac{1}{2}\|F(\theta) - y\|^2
$$

still has a minimizer under mild compactness assumptions on the parameter space, but that this minimizer need not be unique. Provide a geometric argument using the projection theorem.

---

**Exercise 6.** Consider a weighted least-squares calibration with weight matrix $W = \mathrm{diag}(w_1, \ldots, w_m)$ and the linearized update $\Delta\theta = (J^\top W J)^{-1} J^\top W \,\delta y$, where $\delta y$ is a perturbation in market data. If $w_i = 1/\sigma_i^2$ where $\sigma_i$ is the bid-ask half-width of instrument $i$, show that the parameter perturbation satisfies

$$
\|\Delta\theta\| \le \|(J^\top W J)^{-1}\|_2 \cdot \|J^\top W\|_2 \cdot \|\delta y\|
$$

and discuss how instruments with tight bid-ask spreads (small $\sigma_i$) disproportionately influence parameter stability.

---

**Exercise 7.** A calibration of the Heston model to 20 vanilla option prices yields two local minima: $\theta_A$ with loss $\mathcal{L}_A = 0.0012$ and $\theta_B$ with loss $\mathcal{L}_B = 0.0015$. However, $\theta_B$ produces more stable Greeks and day-to-day parameter estimates. Discuss the trade-off between goodness of fit and parameter stability. Under what criteria might a risk manager prefer $\theta_B$? How does this relate to the regularization approach described in Chapter 5.3?
