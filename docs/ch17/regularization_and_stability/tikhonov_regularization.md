# Tikhonov Regularization


Ill-posed calibration problems are often stabilized by **regularization**, which introduces additional structure or prior information. The most classical approach is **Tikhonov regularization**, widely used in inverse problems and numerical analysis.

---

## Motivation


Recall a typical least-squares calibration problem:

$$
\min_{\theta \in \Theta} \; \frac12\|F(\theta) - y\|_W^2
$$


where $F$ is the forward pricing map and $y$ denotes market data.

If the Jacobian of $F$ is ill-conditioned, small data noise can lead to large parameter fluctuations. Tikhonov regularization addresses this by penalizing undesirable parameter behavior.

---

## Basic Tikhonov formulation


The Tikhonov-regularized problem is

$$
\min_{\theta \in \Theta} \;
\frac12\|F(\theta) - y\|_W^2

+ \frac{\lambda}{2}\|L(\theta - \theta_0)\|^2
$$



Components:

- $\lambda > 0$: regularization strength,
- $L$: regularization operator (often identity),
- $\theta_0$: reference or prior parameter vector.

Special cases:

- **Zero-order Tikhonov:** $L = I$, penalizes large parameter magnitudes.
- **Shifted Tikhonov:** pulls parameters toward a prior guess $\theta_0$.

---

## Linearized analysis


For a linear forward map $F(\theta) = A\theta$, the solution satisfies

$$
(A^\top W A + \lambda L^\top L)\theta
= A^\top W y + \lambda L^\top L \theta_0
$$



Key consequences:

- the matrix becomes invertible even if $A^\top W A$ is singular,
- small singular values are damped,
- variance is reduced at the cost of bias.

This bias–variance trade-off is central to regularization.

---

## Interpretation as Bayesian prior


Tikhonov regularization admits a Bayesian interpretation:

- likelihood: $y \mid \theta \sim \mathcal{N}(F(\theta), W^{-1})$,
- prior: $\theta \sim \mathcal{N}(\theta_0, (\lambda L^\top L)^{-1})$.

Then the regularized solution is the **maximum a posteriori (MAP)** estimator.

---

## Choosing the regularization parameter


Selecting $\lambda$ is critical. Common approaches:

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

??? success "Solution to Exercise 1"
    We minimize the objective

    $$
    J(\theta) = \frac{1}{2}(A\theta - y)^\top W (A\theta - y) + \frac{\lambda}{2}(\theta - \theta_0)^\top(\theta - \theta_0)
    $$

    Taking the gradient and setting it to zero:

    $$
    \nabla_\theta J = A^\top W(A\theta - y) + \lambda(\theta - \theta_0) = 0
    $$

    Expanding:

    $$
    (A^\top W A + \lambda I)\theta = A^\top W y + \lambda \theta_0
    $$

    Since $A^\top W A$ is positive semidefinite and $\lambda I$ is positive definite (for $\lambda > 0$), the sum $A^\top W A + \lambda I$ is positive definite, hence invertible. Solving:

    $$
    \hat{\theta}_\lambda = (A^\top W A + \lambda I)^{-1}(A^\top W y + \lambda \theta_0)
    $$

    **Limit $\lambda \to 0$:** The term $\lambda I$ becomes negligible and $\lambda \theta_0 \to 0$, so

    $$
    \hat{\theta}_\lambda \to (A^\top W A)^{-1} A^\top W y = \hat{\theta}_{\text{WLS}}
    $$

    which is the weighted least-squares solution (assuming $A^\top W A$ is invertible).

    **Limit $\lambda \to \infty$:** Factor out $\lambda$ from the system:

    $$
    \hat{\theta}_\lambda = \left(\frac{1}{\lambda}A^\top W A + I\right)^{-1}\left(\frac{1}{\lambda}A^\top W y + \theta_0\right)
    $$

    As $\lambda \to \infty$, $\frac{1}{\lambda}A^\top W A \to 0$ and $\frac{1}{\lambda}A^\top W y \to 0$, so

    $$
    \hat{\theta}_\lambda \to I^{-1}\theta_0 = \theta_0
    $$

    The regularized estimator thus interpolates continuously between the data-driven least-squares solution and the prior $\theta_0$ as $\lambda$ increases from 0 to $\infty$.

---

**Exercise 2.** Let $A$ have singular value decomposition $A = U\Sigma V^\top$ with singular values $\sigma_1 \ge \cdots \ge \sigma_d > 0$. Show that the Tikhonov solution with $L = I$ and $\theta_0 = 0$ can be written in the SVD basis as

$$
\hat{\theta}_\lambda = \sum_{i=1}^d \frac{\sigma_i^2}{\sigma_i^2 + \lambda} \frac{u_i^\top y}{\sigma_i} v_i
$$

Interpret the filter factors $\sigma_i^2/(\sigma_i^2 + \lambda)$ and explain how they suppress components with small singular values.

??? success "Solution to Exercise 2"
    Let $A = U\Sigma V^\top$ where $U = (u_1, \ldots, u_m)$, $V = (v_1, \ldots, v_d)$, and $\Sigma = \operatorname{diag}(\sigma_1, \ldots, \sigma_d)$. With $L = I$, $\theta_0 = 0$, and $W = I$, the Tikhonov solution is

    $$
    \hat{\theta}_\lambda = (A^\top A + \lambda I)^{-1} A^\top y
    $$

    Using the SVD:

    $$
    A^\top A = V\Sigma^\top U^\top U\Sigma V^\top = V\Sigma^2 V^\top
    $$

    so

    $$
    A^\top A + \lambda I = V(\Sigma^2 + \lambda I)V^\top
    $$

    and

    $$
    (A^\top A + \lambda I)^{-1} = V(\Sigma^2 + \lambda I)^{-1}V^\top
    $$

    Also, $A^\top y = V\Sigma U^\top y$. Combining:

    $$
    \hat{\theta}_\lambda = V(\Sigma^2 + \lambda I)^{-1}\Sigma U^\top y = \sum_{i=1}^d \frac{\sigma_i}{\sigma_i^2 + \lambda}(u_i^\top y)\,v_i = \sum_{i=1}^d \frac{\sigma_i^2}{\sigma_i^2 + \lambda}\frac{u_i^\top y}{\sigma_i}\,v_i
    $$

    The **filter factors** are $f_i = \sigma_i^2/(\sigma_i^2 + \lambda)$, satisfying $0 < f_i \le 1$.

    **Interpretation:**

    - For components with large singular values ($\sigma_i^2 \gg \lambda$): $f_i \approx 1$, so these components pass through essentially unmodified. These correspond to well-determined parameter directions.

    - For components with small singular values ($\sigma_i^2 \ll \lambda$): $f_i \approx \sigma_i^2/\lambda \approx 0$, so these components are heavily suppressed. These correspond to directions in parameter space that are poorly constrained by the data.

    - The unregularized solution ($\lambda = 0$) has coefficients $u_i^\top y / \sigma_i$, where division by small $\sigma_i$ amplifies noise. The filter factors prevent this amplification by damping precisely those components where noise dominance is most severe.

    The regularization parameter $\lambda$ sets the threshold: singular values below $\sqrt{\lambda}$ are effectively filtered out.

---

**Exercise 3.** Derive the Bayesian interpretation of Tikhonov regularization. Starting from the prior $\theta \sim \mathcal{N}(\theta_0, (\lambda L^\top L)^{-1})$ and likelihood $y|\theta \sim \mathcal{N}(A\theta, W^{-1})$, show that the MAP estimator coincides with the Tikhonov solution. What does the regularization parameter $\lambda$ correspond to in Bayesian terms?

??? success "Solution to Exercise 3"
    **Bayesian setup.** We have:

    - Prior: $\theta \sim \mathcal{N}(\theta_0, \Sigma_{\text{prior}})$ with $\Sigma_{\text{prior}} = (\lambda L^\top L)^{-1}$
    - Likelihood: $y|\theta \sim \mathcal{N}(A\theta, W^{-1})$

    The log-posterior is (up to constants):

    $$
    \log p(\theta | y) = \log p(y|\theta) + \log p(\theta) + \text{const}
    $$

    Computing each term:

    $$
    \log p(y|\theta) = -\frac{1}{2}(y - A\theta)^\top W(y - A\theta) + \text{const}
    $$

    $$
    \log p(\theta) = -\frac{1}{2}(\theta - \theta_0)^\top (\lambda L^\top L)(\theta - \theta_0) + \text{const}
    $$

    Therefore

    $$
    \log p(\theta|y) = -\frac{1}{2}\bigl[(y - A\theta)^\top W(y - A\theta) + \lambda(\theta - \theta_0)^\top L^\top L(\theta - \theta_0)\bigr] + \text{const}
    $$

    The MAP estimator maximizes $\log p(\theta|y)$, which is equivalent to minimizing

    $$
    \frac{1}{2}\|A\theta - y\|_W^2 + \frac{\lambda}{2}\|L(\theta - \theta_0)\|^2
    $$

    This is precisely the Tikhonov objective, confirming the equivalence.

    **Bayesian interpretation of $\lambda$:** The regularization parameter $\lambda$ controls the ratio of the prior precision to the likelihood precision. Specifically, the prior covariance is $(\lambda L^\top L)^{-1}$, so:

    - Large $\lambda$ means a tight prior (small prior variance) — strong belief that $\theta$ is close to $\theta_0$.
    - Small $\lambda$ means a diffuse prior (large prior variance) — letting the data speak.

    If the noise covariance is $\sigma^2 W^{-1}$ (with $\sigma^2$ explicit), then $\lambda$ is proportional to $\sigma^2 / \tau^2$, the ratio of observation noise variance to prior variance. This is the **signal-to-noise ratio** of the prior relative to the data.

---

**Exercise 4.** The L-curve method plots $\log\|F(\hat{\theta}_\lambda) - y\|$ versus $\log\|L(\hat{\theta}_\lambda - \theta_0)\|$ for varying $\lambda$. The optimal $\lambda$ is chosen at the "corner" of the L-shaped curve. Explain geometrically why the corner represents the best compromise between fit and regularity. What happens if the L-curve has no clear corner?

??? success "Solution to Exercise 4"
    The L-curve plots the residual norm $\rho(\lambda) = \|F(\hat{\theta}_\lambda) - y\|$ against the regularization norm $\eta(\lambda) = \|L(\hat{\theta}_\lambda - \theta_0)\|$ on a log-log scale for varying $\lambda$.

    **Geometric interpretation of the corner:**

    - For very small $\lambda$ (bottom-right of the L): the residual $\rho$ is minimized, but $\eta$ is large and highly sensitive to $\lambda$. The curve is nearly vertical, meaning small decreases in residual come at enormous cost in regularity.

    - For very large $\lambda$ (top-left of the L): the regularization norm $\eta$ is small, but $\rho$ is large and insensitive to further increases in $\lambda$. The curve is nearly horizontal, meaning the fit is already so poor that additional regularization gains little stability.

    - At the **corner**: there is a transition between these two regimes. This point represents the best compromise because:

        1. Reducing $\lambda$ below the corner value would sharply increase $\eta$ (instability) with only marginal improvement in $\rho$.
        2. Increasing $\lambda$ above the corner value would sharply increase $\rho$ (misfit) with only marginal improvement in $\eta$.

    The corner maximizes the curvature of the L-curve in log-log space. Formally, the optimal $\lambda^*$ can be found as

    $$
    \lambda^* = \arg\max_\lambda \kappa(\lambda)
    $$

    where $\kappa(\lambda)$ is the curvature of the parametric curve $(\log\rho(\lambda), \log\eta(\lambda))$.

    **When there is no clear corner:** This can occur when:

    - The problem is mildly ill-posed (the singular values decay slowly), so the transition between the two regimes is gradual.
    - The noise level is very low or very high relative to the signal.
    - The regularization operator $L$ does not match the true solution structure.

    In such cases, the L-curve method is unreliable, and alternative methods such as the discrepancy principle, generalized cross-validation (GCV), or information criteria should be used instead.

---

**Exercise 5.** The discrepancy principle selects $\lambda$ such that $\|F(\hat{\theta}_\lambda) - y\| \approx \delta$, where $\delta$ is the estimated noise level. If market quotes have bid-ask half-widths $\sigma_i$, propose how to estimate $\delta$ from these half-widths. What are the limitations of this approach when the model is misspecified (so that the residual has a systematic component in addition to noise)?

??? success "Solution to Exercise 5"
    If market quotes have bid-ask half-widths $\sigma_i$ for $i = 1, \ldots, n$, the noise in each observation can be modeled as $\epsilon_i$ with $|\epsilon_i| \lesssim \sigma_i$. Under the assumption that the noise is uniformly distributed over $[-\sigma_i, \sigma_i]$, the variance is $\sigma_i^2/3$, or if normally distributed with the half-width as one standard deviation, $\operatorname{Var}(\epsilon_i) = \sigma_i^2$.

    The discrepancy principle requires estimating $\delta = \mathbb{E}[\|F(\theta^*) - y\|^2]^{1/2}$, where $\theta^*$ is the true parameter. Assuming independent noise:

    $$
    \delta^2 = \sum_{i=1}^n \sigma_i^2
    $$

    so $\delta = \sqrt{\sum_{i=1}^n \sigma_i^2}$, or equivalently $\delta = \sqrt{n}\,\bar{\sigma}$ where $\bar{\sigma}$ is the root-mean-square half-width.

    If using a weighted norm $\|\cdot\|_W$ with $W = \operatorname{diag}(1/\sigma_1^2, \ldots, 1/\sigma_n^2)$, then the expected weighted residual norm is

    $$
    \mathbb{E}\left[\sum_{i=1}^n \frac{\epsilon_i^2}{\sigma_i^2}\right] = n
    $$

    so one selects $\lambda$ such that $\|F(\hat{\theta}_\lambda) - y\|_W^2 \approx n$.

    **Limitations under model misspecification:**

    When the model is misspecified, the residual decomposes as

    $$
    F(\hat{\theta}_\lambda) - y = \underbrace{(F(\hat{\theta}_\lambda) - F(\theta^*))}_{\text{regularization bias}} + \underbrace{(F(\theta^*) - F(\theta_{\text{true}}))}_{\text{model bias}} + \underbrace{(F(\theta_{\text{true}}) - y)}_{\text{noise } \epsilon}
    $$

    where $\theta_{\text{true}}$ denotes the data-generating parameters (which may not lie in the model class) and $\theta^*$ is the best-fit within the model. The discrepancy principle targets $\|F(\hat{\theta}_\lambda) - y\| \approx \delta$, but:

    - The systematic model bias $F(\theta^*) - F(\theta_{\text{true}})$ inflates the residual beyond the noise level.
    - Setting $\delta$ based only on bid-ask noise will select $\lambda$ too small, because the method tries to fit the systematic error as well.
    - In practice, one should estimate the total residual floor (noise + irreducible model error) from historical calibration residuals, not just from bid-ask widths.

    A more robust approach is to set $\delta^2 = \sum_i \sigma_i^2 + \delta_{\text{model}}^2$, where $\delta_{\text{model}}$ is estimated from the typical best-fit residual of the model on clean data.

---

**Exercise 6.** A Heston model is calibrated to 30 option prices using Tikhonov regularization with $\theta_0$ equal to yesterday's parameters. The regularization parameter is $\lambda = 0.1$. Today, a sudden market crash occurs, and the unregularized calibration yields $v_0 = 0.12$ (compared to yesterday's $v_0 = 0.04$). Compute the regularized estimate. Is the regularization appropriate in this scenario? How would you design an adaptive $\lambda$ that allows large parameter changes during genuine market events?

??? success "Solution to Exercise 6"
    The Tikhonov-regularized estimate with $L = I$ and $\theta_0$ from yesterday is

    $$
    \hat{\theta}_\lambda = (A^\top W A + \lambda I)^{-1}(A^\top W y + \lambda \theta_0)
    $$

    For the scalar parameter $v_0$ in isolation (assuming independence from other parameters for simplicity), the regularized estimate is

    $$
    \hat{v}_{0,\lambda} = \frac{\hat{v}_{0,\text{unreg}} + \lambda \cdot v_{0,\text{yesterday}}}{1 + \lambda}
    $$

    where $\hat{v}_{0,\text{unreg}}$ is the unregularized estimate, and the formula follows from the scalar version of the Tikhonov update (with the data-fitting Hessian contribution normalized to 1 for the parameter of interest).

    Substituting $\hat{v}_{0,\text{unreg}} = 0.12$, $v_{0,\text{yesterday}} = 0.04$, and $\lambda = 0.1$:

    $$
    \hat{v}_{0,\lambda} = \frac{0.12 + 0.1 \times 0.04}{1 + 0.1} = \frac{0.12 + 0.004}{1.1} = \frac{0.124}{1.1} \approx 0.1127
    $$

    The regularized estimate is approximately $v_0 \approx 0.113$, only slightly pulled toward yesterday's value.

    **Is the regularization appropriate?** In this crash scenario, the regularization with $\lambda = 0.1$ is relatively mild — it only modestly shrinks the estimate. This is acceptable because the market genuinely moved, and the large change in $v_0$ is economically justified. However, a larger $\lambda$ would dangerously suppress the legitimate signal, causing the model to underestimate current volatility.

    **Adaptive $\lambda$ design:** An adaptive scheme should reduce regularization when genuine market events occur. Several approaches:

    1. **Residual-based adaptation.** If $\|F(\hat{\theta}_\lambda) - y\|$ exceeds a threshold (e.g., 3 times the typical calibration residual), this signals model strain, and $\lambda$ should be reduced.

    2. **Market-regime switching.** Monitor indicators such as VIX level, realized volatility, or bid-ask spread widths. In stressed regimes:

        $$
        \lambda_{\text{adaptive}} = \lambda_{\text{base}} \cdot \frac{\sigma_{\text{normal}}}{\sigma_{\text{current}}}
        $$

        where $\sigma$ denotes a market noise or spread measure. Wider spreads (stressed markets) naturally reduce $\lambda$.

    3. **Innovation-based scaling.** Compute the "innovation" $\Delta\theta_{\text{unreg}} = \hat{\theta}_{\text{unreg}} - \theta_0$. If $\|\Delta\theta_{\text{unreg}}\|$ exceeds $k$ standard deviations of historical daily changes, reduce $\lambda$ proportionally:

        $$
        \lambda_{\text{adaptive}} = \lambda_{\text{base}} \cdot \min\!\left(1, \frac{k\,\sigma_{\Delta\theta}}{\|\Delta\theta_{\text{unreg}}\|}\right)
        $$

        This allows large parameter moves when they are statistically unusual but genuine.

---

**Exercise 7.** Compare zero-order Tikhonov ($L = I$) with first-order Tikhonov ($L = D_1$, the first-difference operator) for calibrating a piecewise-constant local volatility surface on a grid of 10 maturities. What structural property does each penalty enforce? Which is more appropriate for this problem and why?

??? success "Solution to Exercise 7"
    Consider a piecewise-constant local volatility $\sigma_{\text{loc}}(T)$ on maturities $T_1 < \cdots < T_{10}$, parameterized by $\theta = (\sigma_1, \ldots, \sigma_{10})^\top$.

    **Zero-order Tikhonov ($L = I$):** The penalty is

    $$
    \mathcal{R}_0(\theta) = \|\theta - \theta_0\|^2 = \sum_{i=1}^{10} (\sigma_i - \sigma_{i,0})^2
    $$

    This penalizes the magnitude of the deviation from a reference $\theta_0$. It enforces that each parameter individually stays close to its prior value. The structural property is **parameter shrinkage toward the prior** — it constrains the overall level but says nothing about the relationship between neighboring parameters.

    **First-order Tikhonov ($L = D_1$):** The penalty is

    $$
    \mathcal{R}_1(\theta) = \|D_1\theta\|^2 = \sum_{i=1}^{9} (\sigma_{i+1} - \sigma_i)^2
    $$

    This penalizes differences between consecutive parameters. The structural property is **smoothness** (small variation across maturities). The null space of $D_1$ consists of constant vectors, so only deviations from flatness are penalized.

    **Which is more appropriate?**

    First-order Tikhonov ($L = D_1$) is more appropriate for this problem, for several reasons:

    1. **Economic rationale.** Local volatility should vary smoothly across maturities. There is no reason to expect the volatility term structure to be anchored to any particular absolute level (as zero-order would enforce), but we do expect neighboring maturities to have similar local volatilities.

    2. **Prior-free smoothness.** With $D_1$, no reference parameter $\theta_0$ is needed. This avoids the problem of choosing a prior that may not be appropriate for current market conditions. The penalty is purely relational — it constrains the shape, not the level.

    3. **Avoiding artificial bias.** Zero-order Tikhonov biases all parameters toward $\theta_0$. If market conditions have shifted (e.g., a persistent increase in the volatility term structure), this bias suppresses the genuine signal. First-order Tikhonov allows the overall level to adapt freely while penalizing only roughness.

    4. **Consistency with the problem structure.** Since the local volatility is piecewise constant, the first-difference penalty directly regularizes the jumps at maturity boundaries, which is precisely the source of instability in the calibration.

    In practice, one might combine both: $\mathcal{R}(\theta) = \alpha\|D_1\theta\|^2 + \beta\|\theta - \theta_0\|^2$, using a strong $D_1$ penalty and a mild zero-order penalty to provide weak anchoring.
