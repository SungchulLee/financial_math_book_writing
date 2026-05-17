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


Market quotes provide a finite set of prices ($m$ instruments), while models may have:

- many parameters ($d$ large),
- hidden state variables,
- functional degrees of freedom (e.g., a local volatility surface $\sigma_{\text{loc}}(t,S)$).

Even when $m\ge d$, the effective rank of the Jacobian may be much smaller due to redundancy and weak sensitivity.

### 2. Noisy data


Observed prices are affected by:

- bid–ask spreads,
- stale quotes,
- microstructure noise,
- interpolation/extrapolation artifacts (surface construction).

Let the true data be $y^\star$ and observed data $y = y^\star + \varepsilon$. If the inverse map is unstable, $\varepsilon$ is amplified into large parameter errors.

### 3. Model misspecification


Even with perfect data, the model may be unable to fit all instruments:

$$
y \notin \mathrm{Range}(F)
$$


Then the optimization problem has a best-fit solution but no exact inverse.

---

## Non-uniqueness mechanisms


### 1. Flat directions (parameter degeneracy)


If the loss surface has valleys, many $\theta$ yield nearly identical fit:

$$
\mathcal{L}(F(\theta),y) \approx \text{constant along a curve/manifold}
$$



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


Recall (see [§ Local linearization and sensitivity](forward_pricing_map_vs_inverse_calibration_map.md#local-linearization-and-sensitivity)) that around a reference $\theta_0$, $F(\theta)\approx F(\theta_0)+J\Delta\theta$. If $J^\top WJ$ is ill-conditioned (small eigenvalues), the linearized inverse $\Delta\theta \approx (J^\top W J)^{-1}J^\top W (y - F(\theta_0))$ is numerically unstable and $\|\Delta\theta\|$ blows up relative to data noise.

This connects directly to **Tikhonov regularization** (see [§ Tikhonov regularization](../regularization_and_stability/tikhonov_regularization.md)).

---

## Practical diagnostics


- **Sensitivity / Greeks-to-parameters:** check Jacobian magnitudes.
- **Bootstrap / re-sample quotes:** re-calibrate after perturbing $y$ within bid–ask.
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

??? success "Solution to Exercise 1"
    **The three Hadamard conditions for well-posedness:**

    1. **Existence:** A solution $\theta$ exists such that $F(\theta) = y$.
    2. **Uniqueness:** The solution is unique -- there is only one $\theta$ with $F(\theta) = y$.
    3. **Stability:** The solution depends continuously on the data -- small changes in $y$ produce small changes in $\theta$.

    **Concrete calibration example where uniqueness fails:**

    Consider a two-parameter model with $\theta = (a, b) \in \mathbb{R}^2$ and forward pricing map

    $$
    F(a, b) = (a^2 + b^2, \; a^2 b^2)
    $$

    mapping to $m = 2$ market observables. Then the parameter vectors $\theta_1 = (1, 2)$ and $\theta_2 = (2, 1)$ produce

    $$
    F(1, 2) = (1 + 4, \; 1 \cdot 4) = (5, 4)
    $$

    $$
    F(2, 1) = (4 + 1, \; 4 \cdot 1) = (5, 4)
    $$

    So $F(\theta_1) = F(\theta_2) = (5, 4)$ with $\theta_1 \neq \theta_2$, violating uniqueness. More generally, $F(a, b) = F(b, a)$ for all $(a, b)$, and $F(a, b) = F(-a, b) = F(a, -b) = F(-a, -b)$, so each market observation is consistent with up to 8 distinct parameter vectors (up to sign and permutation symmetries).

    This is a realistic issue: many financial models have symmetries (e.g., a two-factor model where the factors are exchangeable) that create non-uniqueness. Without imposing ordering constraints or sign conventions, the calibration inverse problem violates Hadamard's uniqueness condition.

---

**Exercise 2.** Consider a model with forward pricing map $F:\mathbb{R}^d \to \mathbb{R}^m$ and Jacobian $J = \partial F/\partial\theta$ evaluated at $\theta_0$. Suppose the singular value decomposition of $J$ is $J = U\Sigma V^\top$ with singular values $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_{\min(m,d)}$. Show that the condition number of the normal equations matrix $J^\top J$ is

$$
\kappa(J^\top J) = \left(\frac{\sigma_1}{\sigma_d}\right)^2
$$

and explain why a large condition number implies instability in the calibrated parameters.

??? success "Solution to Exercise 2"
    The SVD of $J$ gives $J = U \Sigma V^\top$, so

    $$
    J^\top J = V \Sigma^\top U^\top U \Sigma V^\top = V \Sigma^\top \Sigma V^\top = V \,\text{diag}(\sigma_1^2, \ldots, \sigma_d^2)\, V^\top
    $$

    The eigenvalues of $J^\top J$ are $\sigma_1^2, \sigma_2^2, \ldots, \sigma_d^2$, and the condition number is

    $$
    \kappa(J^\top J) = \frac{\lambda_{\max}(J^\top J)}{\lambda_{\min}(J^\top J)} = \frac{\sigma_1^2}{\sigma_d^2} = \left(\frac{\sigma_1}{\sigma_d}\right)^2
    $$

    **Why a large condition number implies instability:**

    The linearized calibration problem solves the normal equations

    $$
    J^\top J \,\Delta\theta = J^\top (y - F(\theta_0))
    $$

    If we perturb the right-hand side by $\delta$, the perturbation in the solution satisfies

    $$
    \frac{\|\delta(\Delta\theta)\|}{\|\Delta\theta\|} \le \kappa(J^\top J) \cdot \frac{\|\delta\|}{\|J^\top(y - F(\theta_0))\|}
    $$

    When $\kappa(J^\top J) = (\sigma_1/\sigma_d)^2$ is large, even small perturbations in the data (entering through the right-hand side) are amplified by this factor, producing large changes in the calibrated parameters. The squared relationship means the instability in parameters is quadratically worse than the condition number of $J$ itself. For example, if $\kappa(J) = 1000$, then $\kappa(J^\top J) = 10^6$, meaning the normal equations amplify data errors by up to a factor of one million.

---

**Exercise 3.** A practitioner calibrates a stochastic volatility model on Monday and obtains parameters $\theta_{\text{Mon}}$. On Tuesday, with nearly identical market data (perturbation $\|\varepsilon\| < 0.01$), the calibration yields $\theta_{\text{Tue}}$ with $\|\theta_{\text{Tue}} - \theta_{\text{Mon}}\| > 10$. Which of the three Hadamard conditions is violated? Propose two practical remedies from the diagnostics discussed in this section.

??? success "Solution to Exercise 3"
    **Violated condition:** This is a violation of **condition (3), stability** (continuous dependence on data). The market data changed by $\|\varepsilon\| < 0.01$, yet the parameters changed by $\|\theta_{\text{Tue}} - \theta_{\text{Mon}}\| > 10$. The ratio

    $$
    \frac{\|\Delta\theta\|}{\|\varepsilon\|} > \frac{10}{0.01} = 1000
    $$

    shows extreme amplification of data perturbations, which is the hallmark of instability (ill-conditioning), not non-existence or non-uniqueness per se.

    Note: Non-uniqueness (condition 2) may also play a role if the large parameter shift indicates that the optimizer found a different local minimum on Tuesday. However, the primary diagnosis based on the described symptoms is instability.

    **Two practical remedies:**

    1. **Tikhonov regularization / parameter anchoring:** Add a penalty $\lambda\|\theta - \theta_{\text{prior}}\|^2$ to the objective function, where $\theta_{\text{prior}}$ could be yesterday's calibrated parameters or a long-term average. This penalizes large day-to-day parameter movements and stabilizes the inversion. The regularization parameter $\lambda$ controls the trade-off between fit quality and parameter stability.

    2. **Multiple initializations with stability filtering:** Run the calibration from $N$ different starting points (e.g., $N = 20$). Among the solutions that achieve an acceptable fit (loss within, say, 10% of the best), select the one closest to yesterday's parameters. This combines global search (to avoid poor local minima) with a stability preference (to reduce day-to-day fluctuations). Alternatively, use the bootstrap diagnostic: perturb market data within bid-ask spreads, recalibrate multiple times, and report the median parameter vector rather than any single calibration result.

---

**Exercise 4.** Let $F(\alpha, \beta) = \alpha \beta$ be a simplified pricing function mapping two parameters to a single observable $y$. Show that the level set $\{(\alpha,\beta) : F(\alpha,\beta) = y\}$ is a hyperbola for $y \neq 0$. Compute the Jacobian $J$ at the point $(\alpha_0, \beta_0)$ and verify that the linearized inverse problem has a one-dimensional null space when $m = 1$ and $d = 2$.

??? success "Solution to Exercise 4"
    The forward map is $F(\alpha, \beta) = \alpha\beta$ with a single observable $y$.

    **Level set is a hyperbola:** For $y \neq 0$, the level set is

    $$
    \{(\alpha, \beta) : \alpha\beta = y\} = \left\{(\alpha, \beta) : \beta = \frac{y}{\alpha}, \; \alpha \neq 0\right\}
    $$

    This is a rectangular hyperbola in the $(\alpha, \beta)$-plane. For $y > 0$, it has branches in the first and third quadrants; for $y < 0$, in the second and fourth quadrants. For $y = 0$, the level set degenerates to the union of the two axes, $\{\alpha = 0\} \cup \{\beta = 0\}$.

    **Jacobian computation:** At the point $(\alpha_0, \beta_0)$,

    $$
    J(\alpha_0, \beta_0) = \nabla_{(\alpha,\beta)} F = \begin{pmatrix} \beta_0 & \alpha_0 \end{pmatrix} \in \mathbb{R}^{1 \times 2}
    $$

    **Null space of the linearized problem:** With $m = 1$ (one equation) and $d = 2$ (two unknowns), the rank of $J$ is at most 1 (assuming $(\alpha_0, \beta_0) \neq (0, 0)$, so $J \neq 0$). By the rank-nullity theorem:

    $$
    \dim(\ker J) = d - \text{rank}(J) = 2 - 1 = 1
    $$

    The null space is spanned by the vector orthogonal to $(\beta_0, \alpha_0)$, namely

    $$
    n = \begin{pmatrix} \alpha_0 \\ -\beta_0 \end{pmatrix}
    $$

    since $J \cdot n = \beta_0 \cdot \alpha_0 + \alpha_0 \cdot (-\beta_0) = 0$. This null vector is tangent to the hyperbola $\alpha\beta = y$ at $(\alpha_0, \beta_0)$: the linearized inverse problem cannot distinguish between parameter perturbations along this direction, reflecting the fundamental non-uniqueness of the full nonlinear problem along the level set.

---

**Exercise 5.** Suppose market data $y$ lies outside the range of the forward map, i.e., $y \notin \mathrm{Range}(F)$, due to model misspecification. Show that the least-squares objective

$$
\mathcal{L}(\theta) = \frac{1}{2}\|F(\theta) - y\|^2
$$

still has a minimizer under mild compactness assumptions on the parameter space, but that this minimizer need not be unique. Provide a geometric argument using the projection theorem.

??? success "Solution to Exercise 5"
    **Existence of a minimizer:**

    Assume the parameter space $\Theta$ is compact (closed and bounded in $\mathbb{R}^d$). The objective

    $$
    \mathcal{L}(\theta) = \frac{1}{2}\|F(\theta) - y\|^2
    $$

    is a continuous function on the compact set $\Theta$ (assuming $F$ is continuous). By the **Weierstrass extreme value theorem**, $\mathcal{L}$ attains its minimum on $\Theta$, so a minimizer exists.

    **The minimizer need not be unique:**

    Since $y \notin \mathrm{Range}(F)$, no $\theta$ achieves $\mathcal{L}(\theta) = 0$. The minimizer is the point(s) in $\mathrm{Range}(F)$ closest to $y$.

    **Geometric argument via the projection theorem:** The set $\mathcal{F} = \{F(\theta) : \theta \in \Theta\} \subset \mathbb{R}^m$ is the image of the compact set $\Theta$ under the continuous map $F$, hence $\mathcal{F}$ is compact. By the projection theorem (best approximation in a Hilbert space), there exists at least one point $\hat{z} \in \mathcal{F}$ minimizing $\|z - y\|$ over $z \in \mathcal{F}$.

    However, uniqueness of the projection requires $\mathcal{F}$ to be **convex** (in a Hilbert space, the nearest-point projection onto a closed convex set is unique). In general, $\mathcal{F} = \mathrm{Range}(F)$ is **not convex** -- it is a curved manifold or a nonlinear image of $\Theta$. Therefore:

    - There may be multiple points $\hat{z}_1, \hat{z}_2 \in \mathcal{F}$ equidistant from $y$ (think of $y$ equidistant from two "bumps" on a curved surface).
    - Even if the nearest point $\hat{z}$ in $\mathcal{F}$ is unique, the preimage $F^{-1}(\{\hat{z}\})$ may contain multiple parameter vectors (due to non-injectivity of $F$).

    Both mechanisms produce non-unique minimizers of $\mathcal{L}$.

---

**Exercise 6.** Consider a weighted least-squares calibration with weight matrix $W = \mathrm{diag}(w_1, \ldots, w_m)$ and the linearized update $\Delta\theta = (J^\top W J)^{-1} J^\top W \,\delta y$, where $\delta y$ is a perturbation in market data. If $w_i = 1/\sigma_i^2$ where $\sigma_i$ is the bid-ask half-width of instrument $i$, show that the parameter perturbation satisfies

$$
\|\Delta\theta\| \le \|(J^\top W J)^{-1}\|_2 \cdot \|J^\top W\|_2 \cdot \|\delta y\|
$$

and discuss how instruments with tight bid-ask spreads (small $\sigma_i$) disproportionately influence parameter stability.

??? success "Solution to Exercise 6"
    **Derivation of the bound:**

    The linearized parameter perturbation is

    $$
    \Delta\theta = (J^\top W J)^{-1} J^\top W \,\delta y
    $$

    Taking norms (using the operator norm induced by the Euclidean vector norm):

    $$
    \|\Delta\theta\| = \|(J^\top W J)^{-1} J^\top W \,\delta y\|
    $$

    By the submultiplicativity of operator norms:

    $$
    \|\Delta\theta\| \le \|(J^\top W J)^{-1}\|_2 \cdot \|J^\top W\|_2 \cdot \|\delta y\|
    $$

    This is the required bound.

    **Influence of instruments with tight bid-ask spreads:**

    When $w_i = 1/\sigma_i^2$ (inverse-variance weighting), instruments with small bid-ask half-widths $\sigma_i$ receive large weights $w_i$. This has several consequences:

    1. **Dominant influence on parameters:** The weighted normal equations $J^\top W J$ are dominated by the rows of $J$ corresponding to high-weight (tight-spread) instruments. These instruments effectively "steer" the parameter estimates.

    2. **Amplified sensitivity to their perturbations:** A perturbation $\delta y_i$ in a tightly-quoted instrument contributes $w_i \delta y_i = \delta y_i / \sigma_i^2$ to the weighted residual. If $\sigma_i$ is small, even a small absolute perturbation $\delta y_i$ produces a large weighted contribution, disproportionately shifting the parameters.

    3. **Risk of overfitting to microstructure noise:** Very liquid instruments may have tight quoted spreads but still contain microstructure noise (stale quotes, asynchronous updates). Inverse-variance weighting trusts these quotes heavily, potentially calibrating to noise rather than signal.

    4. **Practical recommendation:** Use bid-ask-based weights as a starting point but consider capping the maximum weight (e.g., $w_i = \min(1/\sigma_i^2, \, w_{\max})$) to prevent any single instrument from dominating the calibration. Alternatively, use $w_i = 1/\max(\sigma_i, \sigma_{\min})^2$ with a floor on the spread.

---

**Exercise 7.** A calibration of the Heston model to 20 vanilla option prices yields two local minima: $\theta_A$ with loss $\mathcal{L}_A = 0.0012$ and $\theta_B$ with loss $\mathcal{L}_B = 0.0015$. However, $\theta_B$ produces more stable Greeks and day-to-day parameter estimates. Discuss the trade-off between goodness of fit and parameter stability. Under what criteria might a risk manager prefer $\theta_B$? How does this relate to the regularization approach described in Chapter 5.3?

??? success "Solution to Exercise 7"
    **The trade-off:**

    The loss difference is $\mathcal{L}_B - \mathcal{L}_A = 0.0015 - 0.0012 = 0.0003$, which is 25% higher in relative terms but very small in absolute terms. Both solutions fit 20 options well (RMSE on the order of $\sqrt{2 \times 0.0012 / 20} \approx 0.011$ in implied vol, roughly 1 vol point). The practical question is whether this marginal improvement in fit justifies the instability of $\theta_A$.

    **Arguments for preferring $\theta_B$ (the risk manager's perspective):**

    1. **Hedging stability:** Greeks computed from $\theta_B$ are more stable, meaning that hedge ratios (delta, vega, gamma) do not jump erratically from day to day. Unstable Greeks lead to excessive rebalancing, higher transaction costs, and potentially larger hedging errors -- a direct P&L impact that far outweighs the calibration error difference.

    2. **P&L attribution:** Stable parameters allow meaningful decomposition of daily P&L into market moves versus model changes. With $\theta_A$, parameter instability contaminates P&L attribution, making it difficult to distinguish genuine market risk from calibration noise.

    3. **Risk limits and reporting:** Risk metrics (VaR, stress tests) computed from $\theta_A$ will fluctuate, potentially triggering false limit breaches or masking real risk. Regulators and internal risk committees expect parameter stability commensurate with market stability.

    4. **Model confidence:** A solution that is sensitive to small data perturbations likely sits near a ridge or saddle of the loss surface, meaning it is not a robust representation of the market. $\theta_B$, being more stable, likely sits in a broader basin, suggesting it captures the market structure more reliably.

    **Connection to regularization (Chapter 5.3):**

    Preferring $\theta_B$ over $\theta_A$ is implicitly performing regularization. The Tikhonov-regularized problem

    $$
    \min_\theta \; \mathcal{L}(\theta) + \lambda \|\theta - \theta_{\text{prior}}\|^2
    $$

    explicitly trades off fit quality ($\mathcal{L}$) against parameter stability (proximity to a prior or to yesterday's parameters). By choosing $\theta_B$, the risk manager is effectively applying a stability preference that corresponds to a positive regularization parameter $\lambda > 0$. The optimal $\lambda$ balances the 0.0003 increase in misfit against the gain in parameter and Greek stability -- exactly the bias-variance trade-off central to regularization theory. In practice, one can formalize this by sweeping $\lambda$ and selecting the value that yields acceptable fit (within bid-ask) while minimizing day-to-day parameter variation.
