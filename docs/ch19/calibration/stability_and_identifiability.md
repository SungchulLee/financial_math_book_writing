# Stability and Identifiability


Calibration of interest-rate models faces challenges of **stability** and **identifiability**, especially in multi-factor and infinite-dimensional frameworks.

---

## Identifiability issues


Recall (see [§ Calibration as inverse problem](../../ch17/calibration_as_inverse_problem/forward_pricing_map_vs_inverse_calibration_map.md)) for the general identifiability framework. In rates models, weak identifiability arises from limited option maturity coverage, correlations between factors, and flat sensitivity of prices to certain parameter directions, producing multiple parameter sets that fit the same data.

---

## Stability across time


A stable calibration should exhibit smooth parameter evolution, robustness to small quote changes, and consistent dynamics across market regimes. Large day-to-day parameter swings indicate overfitting. Recall (see [§ IR model risk](../interest_rate_model_risk/multi_curve_issues.md)).

---

## Diagnostic tools


Useful diagnostics include sensitivity and Jacobian analysis, perturbation of market quotes, and rolling-window calibration tests. These help separate structural issues from numerical ones.

---

## Practical mitigation strategies


Recall (see [§ Regularization and stability](../../ch17/regularization_and_stability/penalization_and_smoothness_constraints.md)) for the general toolkit. In the rates context, stability is improved by reducing model dimensionality, imposing economically motivated constraints, penalizing parameter variability, and focusing calibration on the most liquid instruments. Practitioners often prefer stability over perfect fit.

---

## Key takeaways


- Calibration stability is as important as fit quality.
- Identifiability problems are intrinsic, not technical.
- Regularization and parsimony are essential.

---

## Further reading


- Engl et al., inverse problems.
- Andersen & Piterbarg, calibration practice.

---

## Exercises

**Exercise 1.** Consider a two-factor Hull--White model with parameters $(a_1, \sigma_1, a_2, \sigma_2, \rho)$, where $a_i$ are mean-reversion speeds, $\sigma_i$ are volatilities, and $\rho$ is the factor correlation. Suppose you calibrate to a set of 10 co-terminal swaption volatilities. Explain why the pair $(a_2, \sigma_2)$ may be weakly identifiable when $\rho$ is close to $\pm 1$, and describe how you would detect this from the Jacobian matrix of the calibration.

??? success "Solution to Exercise 1"
    **Why $(a_2, \sigma_2)$ is weakly identifiable when $\rho \approx \pm 1$:**

    In the two-factor Hull--White model, the short rate is:

    $$
    r(t) = x_1(t) + x_2(t) + \varphi(t)
    $$

    where $dx_i = -a_i x_i\,dt + \sigma_i\,dW_i$ and $\langle dW_1, dW_2\rangle = \rho\,dt$.

    The variance of the short rate is:

    $$
    \text{Var}[r(t)] = \frac{\sigma_1^2}{2a_1}(1 - e^{-2a_1 t}) + \frac{\sigma_2^2}{2a_2}(1 - e^{-2a_2 t}) + 2\rho\frac{\sigma_1\sigma_2}{a_1 + a_2}(1 - e^{-(a_1+a_2)t})
    $$

    When $\rho \to +1$, the two factors become nearly collinear: $W_2 \approx W_1$. In this limit, the model behaves approximately like:

    $$
    r(t) \approx \tilde{x}(t) + \varphi(t), \quad d\tilde{x} \approx -\bar{a}\,\tilde{x}\,dt + \bar{\sigma}\,dW_1
    $$

    where $\bar{a}$ and $\bar{\sigma}$ are effective single-factor parameters that depend on all five parameters. Different combinations of $(a_2, \sigma_2)$ can produce nearly identical effective dynamics because the second factor adds a contribution that is almost parallel to the first.

    More precisely, the swaption prices depend on the covariance structure of bond prices, which involves terms like:

    $$
    \sum_{k=1}^{2}\frac{\sigma_k^2}{a_k^2}(1-e^{-a_k \tau})^2 + 2\rho\frac{\sigma_1\sigma_2}{a_1 a_2}(1-e^{-a_1\tau})(1-e^{-a_2\tau})
    $$

    When $\rho \approx 1$, this can be closely approximated by a single-factor expression with effective parameters, meaning many $(a_2, \sigma_2)$ pairs (with compensating adjustments) yield nearly the same covariance structure.

    **Detection via the Jacobian:**

    Let $\theta = (a_1, \sigma_1, a_2, \sigma_2, \rho)$ and let $V(\theta) \in \mathbb{R}^{10}$ be the vector of 10 co-terminal swaption prices. Form the Jacobian:

    $$
    J = \frac{\partial V}{\partial \theta} \in \mathbb{R}^{10 \times 5}
    $$

    Compute the **singular value decomposition (SVD)** $J = U\Sigma V^T$. If $(a_2, \sigma_2)$ are weakly identifiable:

    - The smallest singular value $\sigma_5$ will be near zero (relative to $\sigma_1$).
    - The condition number $\kappa(J) = \sigma_1/\sigma_5$ will be very large (e.g., $> 10^3$).
    - The corresponding right singular vector $v_5$ will point primarily in the $(a_2, \sigma_2)$ directions, indicating that perturbations along this direction have negligible effect on the swaption prices.

    One can also examine the columns of $J$ corresponding to $a_2$ and $\sigma_2$: if $\partial V / \partial a_2$ is nearly proportional to $\partial V / \partial \sigma_2$ (or nearly zero), these parameters are practically indistinguishable.

---

**Exercise 2.** A calibration routine produces the following parameter values on three consecutive business days:

| Day | $a$ | $\sigma$ | $\rho$ |
|---|---|---|---|
| Mon | 0.05 | 0.012 | 0.75 |
| Tue | 0.18 | 0.009 | 0.42 |
| Wed | 0.06 | 0.011 | 0.72 |

The market quotes changed by less than 0.5 bps between days. Diagnose the likely cause of the Tuesday parameter jump and propose a regularization strategy that would prevent it while preserving the quality of fit.

??? success "Solution to Exercise 2"
    **Diagnosis:**

    Tuesday's parameters $(a = 0.18, \sigma = 0.009, \rho = 0.42)$ are dramatically different from Monday's $(0.05, 0.012, 0.75)$ and Wednesday's $(0.06, 0.011, 0.72)$, despite market quotes changing by less than 0.5 bps. Monday and Wednesday are similar, suggesting Tuesday is an outlier. This is the hallmark of **multiple local minima** combined with **weak identifiability**.

    The likely cause is that the calibration objective function has (at least) two distinct local minima:

    - **Basin A:** near $(a \approx 0.05, \sigma \approx 0.012, \rho \approx 0.75)$ --- Monday and Wednesday's solution.
    - **Basin B:** near $(a \approx 0.18, \sigma \approx 0.009, \rho \approx 0.42)$ --- Tuesday's solution.

    Both basins produce nearly identical swaption prices (within 0.5 bps of each other). On Tuesday, a tiny perturbation in market quotes shifted the relative depth of the two minima, causing the optimizer to converge to Basin B instead of Basin A. This is exacerbated by:

    - **Compensating parameters:** Higher $a$ with lower $\sigma$ can produce similar volatility levels (since long-run bond volatility scales as $\sigma/a$). A different $\rho$ then compensates for the changed factor structure.
    - **Optimizer initialization:** If the optimizer uses a fixed grid or random initialization (rather than warm-starting from yesterday's parameters), it may land in different basins on different days.

    **Regularization strategy:**

    **Tikhonov regularization with temporal anchoring:** Add a penalty that pulls today's parameters toward yesterday's calibrated values:

    $$
    \min_\theta \sum_i w_i (\sigma_i^{\text{model}}(\theta) - \sigma_i^{\text{mkt}})^2 + \lambda \|\theta - \theta_{\text{yesterday}}\|^2
    $$

    With $\theta_{\text{yesterday}} = (0.05, 0.012, 0.75)$ on Tuesday, the penalty term would strongly disfavor the far-away Basin B solution. The parameter $\lambda$ should be chosen so that the added penalty cost of deviating to Basin B exceeds the (tiny, $< 0.5$ bp) improvement in fit quality.

    Additional measures:

    - **Warm-start the optimizer** from yesterday's calibrated parameters, making it more likely to converge to the nearby Basin A.
    - **Constrain the parameter space:** Impose bounds such as $a \in [0.01, 0.10]$ based on economic reasoning, excluding the Basin B region entirely.
    - **Use a global optimizer** (differential evolution, simulated annealing) to map all basins, then select the one closest to the prior-day solution among those with acceptable fit.

---

**Exercise 3.** Let $\theta \in \mathbb{R}^p$ be the parameter vector and $V(\theta) \in \mathbb{R}^n$ be the vector of model prices. The Jacobian is $J = \partial V / \partial \theta$. Show that if $J$ has a singular value $\sigma_k \approx 0$, then the corresponding parameter direction $u_k$ (the right singular vector) is poorly identified. Explain how the condition number $\kappa(J) = \sigma_1 / \sigma_p$ relates to calibration stability.

??? success "Solution to Exercise 3"
    **Setup:** Let $\theta \in \mathbb{R}^p$ be the parameter vector and $V(\theta) \in \mathbb{R}^n$ the model price vector. The Jacobian is $J = \partial V/\partial \theta \in \mathbb{R}^{n \times p}$.

    Compute the **thin SVD**: $J = U \Sigma V^T$ where $U \in \mathbb{R}^{n \times p}$, $\Sigma = \text{diag}(\sigma_1, \ldots, \sigma_p)$ with $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_p \geq 0$, and $V = [v_1 | \cdots | v_p] \in \mathbb{R}^{p \times p}$ is orthogonal.

    **Effect of a small parameter perturbation:**

    A perturbation $\delta\theta$ in parameter space produces a price change:

    $$
    \delta V \approx J\,\delta\theta
    $$

    Expanding $\delta\theta$ in the basis of right singular vectors: $\delta\theta = \sum_{k=1}^p c_k v_k$. Then:

    $$
    \delta V = J\sum_k c_k v_k = \sum_k c_k \sigma_k u_k
    $$

    The price change along direction $v_k$ is amplified by $\sigma_k$. If $\sigma_k \approx 0$, then even a large perturbation $c_k$ along $v_k$ produces a negligible price change $\sigma_k c_k \approx 0$.

    **Implication for identifiability:**

    The parameter direction $v_k$ corresponding to a near-zero singular value $\sigma_k$ is **poorly identified**: the data cannot distinguish parameter values that differ along $v_k$ because the resulting price changes are vanishingly small compared to market noise. In the calibration, the optimizer can move freely along $v_k$ without affecting the objective function, leading to arbitrary or unstable values for the component of $\theta$ along $v_k$.

    **Condition number and stability:**

    The condition number of $J$ is:

    $$
    \kappa(J) = \frac{\sigma_1}{\sigma_p}
    $$

    This measures the **relative sensitivity** between the most and least identifiable parameter directions. In a linearized calibration (Gauss--Newton), the parameter update is:

    $$
    \delta\theta = (J^T J)^{-1} J^T (V^{\text{mkt}} - V^{\text{model}})
    $$

    The eigenvalues of $(J^T J)^{-1}$ are $1/\sigma_k^2$, so the amplification of noise along direction $v_k$ is proportional to $1/\sigma_k$. A perturbation $\epsilon$ in the market data produces a parameter shift:

    $$
    \|\delta\theta\| \leq \kappa(J) \cdot \frac{\|\epsilon\|}{\|V^{\text{mkt}}\|} \cdot \|\theta\|
    $$

    Therefore:

    - $\kappa(J) \gg 1$ implies the calibration is **ill-conditioned**: small market data perturbations cause large parameter swings. This is the mathematical signature of instability.
    - $\kappa(J) \approx 1$ implies all parameters are equally well-determined by the data, and the calibration is robust.

    In practice, $\kappa(J) > 100$ is a warning sign, and $\kappa(J) > 1000$ indicates serious identifiability problems requiring regularization.

---

**Exercise 4.** A practitioner adds a Tikhonov regularization penalty to the calibration objective:

$$
\min_\theta \sum_{i=1}^n w_i \bigl(V_i^{\text{model}}(\theta) - V_i^{\text{mkt}}\bigr)^2 + \lambda \|\theta - \theta_{\text{prior}}\|^2
$$

where $\theta_{\text{prior}}$ is a reference parameter vector (e.g., yesterday's calibrated values). Discuss how the regularization parameter $\lambda$ trades off goodness of fit against stability. Derive the first-order optimality condition and show how it relates to ridge regression.

??? success "Solution to Exercise 4"
    **Tikhonov-regularized objective:**

    $$
    \mathcal{L}(\theta) = \sum_{i=1}^n w_i (V_i^{\text{model}}(\theta) - V_i^{\text{mkt}})^2 + \lambda\|\theta - \theta_{\text{prior}}\|^2
    $$

    **First-order optimality condition:**

    Setting the gradient to zero:

    $$
    \nabla_\theta \mathcal{L} = 2\sum_{i=1}^n w_i (V_i^{\text{model}} - V_i^{\text{mkt}})\nabla_\theta V_i^{\text{model}} + 2\lambda(\theta - \theta_{\text{prior}}) = 0
    $$

    In matrix notation, let $r(\theta) = V^{\text{model}}(\theta) - V^{\text{mkt}}$ be the residual vector, $W = \text{diag}(w_1, \ldots, w_n)$, and $J = \nabla_\theta V^{\text{model}}$ the Jacobian. Then:

    $$
    J^T W\,r(\theta) + \lambda(\theta - \theta_{\text{prior}}) = 0
    $$

    **Linearized (Gauss--Newton) form:**

    Linearizing around a point $\theta_0$: $V^{\text{model}}(\theta) \approx V^{\text{model}}(\theta_0) + J(\theta - \theta_0)$. Substituting:

    $$
    J^T W [J(\theta - \theta_0) + r(\theta_0)] + \lambda(\theta - \theta_{\text{prior}}) = 0
    $$

    $$
    (J^T W J + \lambda I)\theta = J^T W J \theta_0 - J^T W r(\theta_0) + \lambda\theta_{\text{prior}}
    $$

    $$
    (J^T W J + \lambda I)(\theta - \theta_{\text{prior}}) = -J^T W [r(\theta_0) + J(\theta_{\text{prior}} - \theta_0)]
    $$

    Defining $\tilde{r} = V^{\text{model}}(\theta_{\text{prior}}) - V^{\text{mkt}}$ (the residual at the prior) in the simplified case $\theta_0 = \theta_{\text{prior}}$:

    $$
    \theta^* = \theta_{\text{prior}} - (J^T W J + \lambda I)^{-1} J^T W \tilde{r}
    $$

    **Connection to ridge regression:**

    This is exactly the **ridge regression** estimator. In standard ridge regression, one minimizes $\|y - X\beta\|^2 + \lambda\|\beta - \beta_0\|^2$, giving:

    $$
    \hat{\beta} = \beta_0 + (X^T X + \lambda I)^{-1} X^T(y - X\beta_0)
    $$

    The Tikhonov calibration is the nonlinear analog, with $J$ playing the role of $X$, the price residual playing the role of $y - X\beta_0$, and $\theta_{\text{prior}}$ playing the role of $\beta_0$.

    **Trade-off governed by $\lambda$:**

    - **$\lambda = 0$:** Pure least-squares fit. The calibration minimizes pricing errors without regard to parameter stability. If $J$ is ill-conditioned, parameters may be unstable.
    - **$\lambda \to \infty$:** The penalty dominates, forcing $\theta \to \theta_{\text{prior}}$. Parameters are maximally stable (they do not change at all) but the model may not fit the market data.
    - **Intermediate $\lambda$:** Balances fit quality and stability. The regularized normal equations $(J^T W J + \lambda I)$ replace the potentially singular $J^T W J$ with a well-conditioned matrix (all eigenvalues are at least $\lambda$), ensuring a stable solution. The condition number of the regularized problem is $(\sigma_1^2 + \lambda)/(\sigma_p^2 + \lambda)$, which is much smaller than $\sigma_1^2/\sigma_p^2$ when $\lambda \gg \sigma_p^2$.

---

**Exercise 5.** You are calibrating a LIBOR Market Model to a $10 \times 10$ swaption volatility matrix using an exponential correlation structure $\rho_{ij} = \rho_\infty + (1-\rho_\infty)e^{-\beta|T_i - T_j|}$. After calibration, you perturb the $5\text{Y} \times 5\text{Y}$ swaption volatility by $+1$ bp and re-calibrate. The parameters shift by $\Delta \rho_\infty = 0.08$ and $\Delta \beta = 0.15$. Is this level of sensitivity acceptable? Explain how you would use perturbation analysis systematically to assess whether the two-parameter correlation model provides a stable calibration.

??? success "Solution to Exercise 5"
    **Assessment: the sensitivity is too high.**

    A 1 bp perturbation in a single swaption volatility causes $\Delta\rho_\infty = 0.08$ and $\Delta\beta = 0.15$. These are very large shifts:

    - $\rho_\infty$ represents the long-run correlation floor. A shift of 0.08 means the minimum correlation between distant forward rates changes by 8 percentage points (e.g., from 0.30 to 0.38 or 0.22). This dramatically alters the pricing of long-tenor products.
    - $\beta$ controls the decay of correlation. A shift of 0.15 changes the adjacent correlation $e^{-\beta}$ by several percentage points.

    For a well-conditioned calibration, a 1 bp input perturbation should produce parameter changes of order $10^{-3}$ to $10^{-2}$ in correlation parameters, not $10^{-1}$. This level of sensitivity is **unacceptable** for production use.

    **Systematic perturbation analysis:**

    To assess stability comprehensively, perform the following:

    **Step 1: Build the sensitivity matrix.** For each swaption $(m)$ in the $10 \times 10$ grid, perturb $\sigma_m^{\text{mkt}}$ by $+1$ bp and re-calibrate. Record:

    $$
    S_{m} = \begin{pmatrix} \Delta\rho_\infty^{(m)} / \Delta\sigma_m \\ \Delta\beta^{(m)} / \Delta\sigma_m \end{pmatrix}
    $$

    This produces a $2 \times 100$ sensitivity matrix $S$.

    **Step 2: Analyze the sensitivity magnitudes.** Compute $\|S_m\|$ for each $m$. Swaptions with large sensitivity norms are the ones driving calibration instability. In the example, the $5\text{Y}\times 5\text{Y}$ swaption has $\|S_m\| \approx \sqrt{0.08^2 + 0.15^2}/0.01 \approx 17$, which is very large.

    **Step 3: Eigenvalue analysis.** The Hessian of the calibration objective at the minimum is approximately $H \approx J^T W J$ where $J$ is the Jacobian of model swaption vols with respect to $(\rho_\infty, \beta)$. The eigenvalues of $H$ indicate the curvature of the objective:

    - A small eigenvalue means the objective is flat along the corresponding parameter direction, leading to high sensitivity.
    - The ratio of eigenvalues (condition number) quantifies the asymmetry.

    **Step 4: Remedies if sensitivity is too high.**

    - **Add more correlation parameters** (e.g., upgrade to a 3-parameter model) to reduce the sensitivity by providing more degrees of freedom.
    - **Add Tikhonov regularization** to stabilize the parameters.
    - **Increase the swaption set** to include more instruments, improving the conditioning.
    - **Reduce the correlation model** to a single parameter if identifiability is the issue.

    A stable two-parameter model should show sensitivities of order $\Delta\rho_\infty, \Delta\beta \lesssim 0.005$ per bp, meaning the parameters change smoothly and proportionally with the data.

---

**Exercise 6.** Explain the difference between **structural non-identifiability** (where distinct parameter values produce identical model outputs for all possible observations) and **practical non-identifiability** (where parameters are theoretically identifiable but cannot be distinguished given finite, noisy data). Give one example of each in the context of interest-rate model calibration.

??? success "Solution to Exercise 6"
    **Structural non-identifiability** occurs when the model has an exact symmetry: distinct parameter values $\theta_1 \neq \theta_2$ produce identical model outputs $V(\theta_1) = V(\theta_2)$ for **all possible** observable data, not just for a particular dataset. This is a property of the model's mathematical structure, not of the data quality.

    **Example in interest-rate calibration:** Consider a two-factor Gaussian short-rate model:

    $$
    r(t) = x_1(t) + x_2(t) + \varphi(t)
    $$

    with $dx_i = -a_i x_i\,dt + \sigma_i\,dW_i$ and $\rho = \text{Corr}(W_1, W_2)$. If $a_1 = a_2$ (equal mean-reversion speeds), the two factors are **exchangeable**: swapping $(a_1, \sigma_1) \leftrightarrow (a_2, \sigma_2)$ produces the same joint distribution for $r(t)$ and hence the same prices for all interest-rate derivatives. This is structural non-identifiability: the parameter space has a discrete symmetry (label permutation) that no amount of data can resolve. The practical consequence is that the calibration has at least two global minima related by this symmetry.

    **Practical non-identifiability** occurs when parameters are theoretically distinguishable (the model has no exact symmetry) but the available data is insufficient to separate them reliably. The parameter directions are identifiable in principle, but the sensitivity of observables to certain parameter combinations is so small that noise drowns out the signal.

    **Example in interest-rate calibration:** In the SABR model calibrated to a single swaption smile:

    $$
    dF = \alpha F^\beta\,dW_1, \quad d\alpha = \nu\alpha\,dW_2, \quad \langle dW_1, dW_2\rangle = \rho\,dt
    $$

    The parameters $(\alpha, \beta, \nu, \rho)$ are structurally identifiable: different parameter values produce different smile shapes (at least in principle). However, in practice, the **correlation $\rho$** and **vol-of-vol $\nu$** are difficult to disentangle from a finite set of strike-vol observations. Both parameters control the skew, and with typical bid-ask uncertainty of 0.5--1 bp, many $(\rho, \nu)$ pairs fit the observed smile equally well within market noise. This is practical non-identifiability: with exact, infinite-precision smile data one could distinguish $\rho$ from $\nu$, but with realistic noisy quotes one cannot.

    **Key distinction:** Structural non-identifiability cannot be resolved by collecting more or better data --- it requires reformulating the model (e.g., imposing an ordering $a_1 < a_2$). Practical non-identifiability can, in principle, be resolved with more data, higher precision, or additional instrument types, but may also be mitigated by regularization or parameter reduction.
