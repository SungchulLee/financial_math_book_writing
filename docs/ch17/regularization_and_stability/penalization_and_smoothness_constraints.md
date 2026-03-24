# Penalization and Smoothness Constraints


Beyond simple parameter shrinkage, regularization can encode **structural beliefs** about smoothness, monotonicity, or shape. Such penalization is especially important when calibrating *functional* objects like volatility surfaces.

---

## Penalization as constraint relaxation


Hard constraints (e.g., exact smoothness or monotonicity) are often replaced by soft penalties:

\[
\min_{\theta} \; \mathcal{L}(\theta) + \lambda \mathcal{R}(\theta),
\]


where \(\mathcal{R}\) measures deviation from desired structure.

This approach:
- improves numerical stability,
- allows controlled violations when data strongly suggest them.

---

## Smoothness penalties


### 1. Finite-difference penalties


For discretized parameters \(\theta_i\):

\[
\mathcal{R}(\theta)
= \sum_i (\theta_{i+1}-\theta_i)^2
\quad \text{or} \quad
\sum_i (\theta_{i+2}-2\theta_{i+1}+\theta_i)^2.
\]



These penalize:
- large gradients (first differences),
- curvature/roughness (second differences).

### 2. Continuous formulations


For a function \(f(x)\):

\[
\mathcal{R}(f) = \int |f'(x)|^2 dx
\quad \text{or} \quad
\int |f''(x)|^2 dx.
\]



Such penalties are common in spline-based volatility surfaces.

---

## Shape and financial constraints


Regularization can enforce economically motivated shapes:

- **monotonicity** (e.g., total variance in maturity),
- **convexity** (call price in strike),
- **positivity** (variance, intensities).

These are often implemented as:
- inequality constraints with slack variables,
- barrier or penalty terms.

---

## Penalization in stochastic and local volatility


- **Local volatility:** strong smoothing needed to prevent noise amplification.
- **Stochastic volatility:** mild penalties help stabilize weakly identified parameters.
- **Term-structure models:** smoothness across maturity improves forward consistency.

---

## Interaction with discretization


Penalization strength depends on grid resolution:

- finer grids require stronger penalties for comparable smoothness,
- penalties should scale with discretization step size.

Ignoring this can lead to misleading calibration comparisons.

---

## Key takeaways


- Penalization encodes prior beliefs about smoothness and shape.
- Smoothness constraints are essential for functional calibration problems.
- The choice of penalty must be consistent with discretization and economics.

---

## Further reading


- Wahba, *Spline Models for Observational Data*.
- Fengler, *Semiparametric Modeling of Implied Volatility*.
- Gatheral, *The Volatility Surface*.

---

## Exercises

**Exercise 1.** For a discretized local volatility surface on a grid with $n$ strike points, write down the first-difference and second-difference penalty matrices $D_1$ and $D_2$ explicitly for $n = 5$. Show that the second-difference penalty $\mathcal{R}(\theta) = \|D_2\theta\|^2$ penalizes curvature while leaving linear functions unpenalized.

---

**Exercise 2.** Consider the continuous smoothness penalty $\mathcal{R}(f) = \int_a^b (f''(x))^2\,dx$. Show that among all functions interpolating $n$ data points, the one minimizing this penalty is a natural cubic spline. What boundary conditions does the natural cubic spline satisfy?

---

**Exercise 3.** A practitioner fits an implied volatility smile at a single maturity using a penalized least-squares objective:

$$
\min_f \sum_{i=1}^m w_i(f(k_i) - \sigma_i^{\text{obs}})^2 + \lambda \int (f''(k))^2\,dk
$$

If $\lambda$ is too small, the fit interpolates the noisy data exactly. If $\lambda$ is too large, the fit becomes a straight line. For intermediate $\lambda$, how many effective degrees of freedom does the smoother have? Relate this to the trace of the smoother matrix.

---

**Exercise 4.** Monotonicity of total variance in maturity ($\partial_T w \ge 0$) is a no-arbitrage constraint. Formulate this as both a hard constraint and a soft penalty. For the soft penalty version, propose a specific penalty function $\mathcal{R}_{\text{mono}}(w)$ that is zero when the constraint is satisfied and positive otherwise. Discuss the trade-off between hard and soft enforcement.

---

**Exercise 5.** For a local volatility grid with spacing $h$ in strike, show that the first-difference penalty with coefficient $\lambda$ is equivalent to a continuous penalty with effective strength $\lambda / h$. Conclude that if the grid is refined (smaller $h$), the penalty coefficient $\lambda$ must be increased proportionally to maintain the same level of smoothing. Derive the exact scaling relationship.

---

**Exercise 6.** Combine a smoothness penalty with a convexity constraint for fitting a call price surface. Write down the full optimization problem including: (a) data-fitting term, (b) smoothness penalty in strike, (c) smoothness penalty in maturity, and (d) hard convexity constraint $\partial_{KK}C \ge 0$. Discuss how you would solve this constrained optimization problem numerically.
