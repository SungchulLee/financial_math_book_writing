# Identifiability of Model Parameters


**Identifiability** asks whether parameters can be determined uniquely (or at least reliably) from the available data. In calibration, lack of identifiability leads to unstable estimates, poor interpretability, and fragile hedging.

---

## Definitions


### 1. Structural identifiability (noise-free, idealized)


A model is **structurally identifiable** (with respect to chosen instruments) if

$$
F(\theta_1)=F(\theta_2) \;\Rightarrow\; \theta_1=\theta_2
$$



This is a property of the model + instrument set, *not* of the optimizer.

### 2. Practical identifiability (finite, noisy data)


In practice, we only need parameters to be distinguishable within noise:

$$
\|F(\theta_1)-F(\theta_2)\| \lesssim \text{noise level}
\quad\Rightarrow\quad
\theta_1,\theta_2 \text{ are practically indistinguishable.}
$$



Practical identifiability depends on:

- quote noise / liquidity,
- weights $w_j$,
- instrument selection (strikes/maturities),
- numerical implementation.

---

## Local identifiability via the Jacobian


Recall the Jacobian $J(\theta)=\nabla_\theta F(\theta)\in\mathbb{R}^{m\times d}$ (see [§ Local linearization and sensitivity](forward_pricing_map_vs_inverse_calibration_map.md#local-linearization-and-sensitivity)). A standard local criterion: if $J(\theta)$ has **full column rank**, then the parameters are locally identifiable (in a smooth setting). Equivalently, if $J^\top W J$ is nonsingular for a positive definite weight matrix $W$, the (linearized) least-squares problem has a unique local solution.

### 1. Singular values as an identifiability score


Let $J = U \Sigma V^\top$ be the SVD with singular values $\sigma_1\ge \dots \ge \sigma_d$. Then:

- very small $\sigma_d$ indicates a nearly unidentifiable direction,
- the condition number $\kappa=\sigma_1/\sigma_d$ measures sensitivity.

---

## Examples of (non-)identifiability in option models


### 1. Redundancy between parameters


In many models, two different parameters can both change:

- overall variance level,
- skew strength,
- term-structure slope.

If the available option set does not excite both effects independently, parameters become entangled.

### 2. Maturity coverage matters


Short maturities can be informative about:

- instantaneous volatility level,
- jump intensity (if jumps exist),
- microstructure distortions (harder).

Long maturities are informative about:

- mean reversion,
- long-run variance,
- correlation effects (in stochastic vol).

Thus, identifiability is often improved by **joint calibration across maturities**.

---

## How to improve identifiability


### 1. Better instrument design


- include both OTM puts and calls (skew information),
- include a range of maturities (term structure),
- filter out illiquid points, or down-weight them.

### 2. Re-parameterization


Choose parameters that are closer to what the market “sees”, e.g.:

- parameterize by at-the-money variance and skew proxies,
- use transformed parameters enforcing constraints smoothly (log/softplus).

### 3. Regularization and priors


Recall (see [§ Tikhonov regularization](../regularization_and_stability/tikhonov_regularization.md)) that if parameters are weakly identifiable, Tikhonov penalties, smoothness penalties, and Bayesian priors stabilize estimation.

### 4. Report uncertainty, not just point estimates


When identifiability is weak, produce:

- confidence intervals (approximate via Hessian / Fisher information),
- bootstrap distributions,
- parameter-stability plots over time.

---

## Key takeaways


- Identifiability is about whether the *data* constrain the parameters.
- Local identifiability is governed by the Jacobian rank / singular values.
- Practical identifiability can be poor even if structural identifiability holds.
- Remedies: instrument selection, re-parameterization, and regularization.

---

## Further reading


- Inverse problems: Engl, Hanke & Neubauer.
- Practical calibration discussions: Gatheral; Andersen & Piterbarg (volatility and calibration practice).

---

## Exercises

**Exercise 1.** Consider a model with forward pricing map $F(\theta_1, \theta_2) = (\theta_1 + \theta_2, \, \theta_1 \theta_2)$. Is this model structurally identifiable? Prove your answer by determining whether $F(\theta) = F(\theta')$ implies $\theta = \theta'$, or find an explicit counterexample.

??? success "Solution to Exercise 1"
    The forward pricing map is $F(\theta_1, \theta_2) = (\theta_1 + \theta_2, \; \theta_1 \theta_2)$. The model is **not** structurally identifiable.

    **Counterexample:** Let $\theta = (a, b)$ and $\theta' = (b, a)$ with $a \neq b$. Then

    $$
    F(a, b) = (a + b, \; ab) = (b + a, \; ba) = F(b, a)
    $$

    So $F(\theta) = F(\theta')$ but $\theta \neq \theta'$.

    **Systematic proof:** Suppose $F(\theta_1, \theta_2) = F(\theta_1', \theta_2')$, i.e.,

    $$
    \theta_1 + \theta_2 = \theta_1' + \theta_2', \quad \theta_1 \theta_2 = \theta_1' \theta_2'
    $$

    By Vieta's formulas, $\theta_1$ and $\theta_2$ are the two roots of the quadratic

    $$
    t^2 - (\theta_1 + \theta_2)t + \theta_1\theta_2 = 0
    $$

    and $\theta_1'$, $\theta_2'$ are the roots of the same quadratic (since the sum and product coincide). Therefore $\{\theta_1', \theta_2'\} = \{\theta_1, \theta_2\}$ as a set, meaning either $(\theta_1', \theta_2') = (\theta_1, \theta_2)$ or $(\theta_1', \theta_2') = (\theta_2, \theta_1)$.

    The parameters are identifiable only **up to permutation**. If one imposes an ordering constraint such as $\theta_1 \le \theta_2$, then identifiability is restored.

---

**Exercise 2.** A stochastic volatility model has $d = 5$ parameters and is calibrated to $m = 20$ implied volatilities. The SVD of the Jacobian at the calibrated point yields singular values $\sigma_1 = 8.0$, $\sigma_2 = 5.2$, $\sigma_3 = 1.1$, $\sigma_4 = 0.03$, $\sigma_5 = 0.001$. Compute the condition number. Identify how many parameters are practically identifiable and how many are weakly identifiable. What specific remedies would you recommend?

??? success "Solution to Exercise 2"
    The condition number is

    $$
    \kappa(J) = \frac{\sigma_1}{\sigma_d} = \frac{\sigma_1}{\sigma_5} = \frac{8.0}{0.001} = 8000
    $$

    **Practically identifiable parameters:** The singular values indicate how well each orthogonal direction in parameter space is constrained by the data. A useful heuristic is to compare each singular value to the noise level (which in implied vol calibration is typically on the order of 0.1--1.0 vol points):

    - $\sigma_1 = 8.0$ and $\sigma_2 = 5.2$: well above noise level. The corresponding parameter combinations are well identified.
    - $\sigma_3 = 1.1$: moderately identifiable; borderline depending on data quality.
    - $\sigma_4 = 0.03$ and $\sigma_5 = 0.001$: far below the noise amplification threshold. These directions are **weakly identifiable**.

    Thus approximately **3 parameter directions** are practically identifiable, and **2 are weakly identifiable**. Note that these are directions in the $V$-basis (right singular vectors), not necessarily individual model parameters. A single weakly identifiable singular direction can involve a combination of several named parameters.

    **Recommended remedies:**

    1. **Regularization:** Add a Tikhonov penalty $\lambda\|\theta - \theta_{\text{prior}}\|^2$ to stabilize the weakly identifiable directions. Choose $\lambda$ via L-curve or cross-validation.
    2. **Fix or constrain weakly identifiable parameters:** Examine the right singular vectors $v_4$ and $v_5$ to identify which parameters contribute most. Fix one or two parameters to literature values or pre-calibrate them from separate data.
    3. **Augment the instrument set:** Include additional strikes, maturities, or exotic instruments that excite the weakly identified directions (e.g., long-dated options for mean reversion, deep OTM for vol-of-vol).
    4. **Re-parameterize:** Replace the original parameters with combinations that align better with the identifiable directions.

---

**Exercise 3.** Suppose you calibrate the SABR model ($\alpha, \beta, \rho, \nu$) to a single-maturity smile consisting of 7 strike-volatility pairs. The parameter $\beta$ is known to be difficult to identify jointly with $\alpha$. Explain why this redundancy arises from the structure of the SABR formula and describe two practical approaches to resolve it.

??? success "Solution to Exercise 3"
    In the SABR model, the implied volatility approximation (Hagan et al.) at leading order for ATM volatility is approximately

    $$
    \sigma_{\text{ATM}} \approx \frac{\alpha}{f^{1-\beta}}
    $$

    where $f$ is the forward rate. This shows that $\alpha$ and $\beta$ enter the ATM level through the combination $\alpha / f^{1-\beta}$. Changing $\beta$ can be compensated by adjusting $\alpha$ to maintain the same ATM volatility. More precisely, for a given smile at a single maturity, the pair $(\alpha, \beta)$ can be varied along the curve

    $$
    \alpha(\beta) = \sigma_{\text{ATM}} \cdot f^{1-\beta}
    $$

    without significantly changing the ATM level. The smile wings (skew and curvature) are primarily controlled by $\rho$ and $\nu$, and depend on $\beta$ only through higher-order terms. With only 7 strike-vol pairs at a single maturity, the data do not contain enough information to disentangle $\alpha$ from $\beta$; the loss surface has a flat valley along the $\alpha$--$\beta$ trade-off curve.

    **Two practical approaches to resolve the redundancy:**

    1. **Fix $\beta$ to a conventional value.** The most common industry practice is to set $\beta = 0$ (normal SABR), $\beta = 0.5$, or $\beta = 1$ (lognormal SABR) based on market convention or prior belief about the backbone dynamics. With $\beta$ fixed, $\alpha$ becomes well-identified from the ATM level, and $\rho$, $\nu$ are identified from the smile shape.

    2. **Calibrate across multiple maturities jointly.** If the same $\beta$ is imposed across all maturities (which is natural since $\beta$ reflects the backbone structure of the underlying), then different maturities provide additional constraints. The term structure of ATM volatility, combined with the varying smile shapes, can help separate $\alpha(T)$ from $\beta$, especially if $\alpha$ is allowed to vary with maturity while $\beta$ is held constant.

---

**Exercise 4.** Let $J \in \mathbb{R}^{m \times d}$ be the Jacobian of the forward map and $W$ a diagonal weight matrix with entries $w_j > 0$. Show that the Fisher information matrix for the linearized problem is $\mathcal{I} = J^\top W J$. Derive an expression for the asymptotic covariance of the parameter estimates in terms of $\mathcal{I}$ and explain how this relates to identifiability.

??? success "Solution to Exercise 4"
    Consider the linearized model $F(\theta) \approx F(\theta_0) + J \Delta\theta$, where we observe $y = F(\theta_0) + J\Delta\theta + \varepsilon$ with $\varepsilon \sim (0, W^{-1})$ (i.e., $W^{-1}$ is the covariance of the noise). The weighted least-squares estimator is

    $$
    \hat{\Delta\theta} = (J^\top W J)^{-1} J^\top W (y - F(\theta_0))
    $$

    **Derivation of the Fisher information matrix:**

    The log-likelihood for the linearized Gaussian model is

    $$
    \ell(\theta) = -\frac{1}{2}(y - F(\theta_0) - J\Delta\theta)^\top W (y - F(\theta_0) - J\Delta\theta) + \text{const}
    $$

    The score vector is

    $$
    \frac{\partial \ell}{\partial (\Delta\theta)} = J^\top W (y - F(\theta_0) - J\Delta\theta)
    $$

    The Fisher information matrix is

    $$
    \mathcal{I} = -\mathbb{E}\left[\frac{\partial^2 \ell}{\partial(\Delta\theta)\partial(\Delta\theta)^\top}\right] = J^\top W J
    $$

    **Asymptotic covariance:**

    By standard maximum likelihood theory, the asymptotic covariance of the parameter estimates is

    $$
    \text{Cov}(\hat\theta) = \mathcal{I}^{-1} = (J^\top W J)^{-1}
    $$

    **Relation to identifiability:** If $\mathcal{I} = J^\top W J$ has a small eigenvalue $\lambda_{\min}$, then the corresponding eigenvector direction has variance $1/\lambda_{\min}$, which is large. This means parameter combinations along that direction are poorly determined by the data -- precisely the definition of weak practical identifiability.

    If $\mathcal{I}$ is singular (rank-deficient), the corresponding parameter directions have infinite variance -- the parameters are not identifiable at all along those directions. The eigenvalues of $\mathcal{I}$ thus provide a quantitative identifiability score: large eigenvalues correspond to well-identified directions, and small or zero eigenvalues correspond to weakly or non-identified directions.

---

**Exercise 5.** A practitioner calibrates a Heston model to two sets of instruments: (A) only ATM options across 6 maturities, and (B) ATM plus 25-delta and 10-delta options across the same 6 maturities. Which set is expected to yield better identifiability for the vol-of-vol parameter $\sigma_v$ and the correlation parameter $\rho$? Justify your answer in terms of the information content of each instrument set.

??? success "Solution to Exercise 5"
    **Set (B)** is expected to yield better identifiability for both the vol-of-vol parameter $\sigma_v$ and the correlation $\rho$.

    **Information content of Set (A) -- ATM options only:**

    ATM options across maturities are primarily sensitive to:

    - The initial variance $v_0$ (through the ATM volatility level at short maturities).
    - The long-run variance $\bar{v}$ and mean-reversion speed $\kappa$ (through the ATM term structure).
    - A partial combination of $\sigma_v$ and $\rho$ (through the ATM skew and convexity, but only weakly).

    The ATM term structure constrains $v_0$, $\kappa$, and $\bar{v}$ reasonably well, but $\sigma_v$ and $\rho$ primarily affect the **shape of the smile** (skew and curvature), which is not observed when only ATM quotes are available. The ATM volatility is approximately $\sqrt{v_0}$ at short maturities and $\sqrt{\bar{v}}$ at long maturities, with limited sensitivity to $\sigma_v$ and $\rho$.

    **Information content of Set (B) -- ATM plus OTM options:**

    - The 25-delta and 10-delta options provide direct information about the smile **skew** and **wings**.
    - In the Heston model, the skew is primarily driven by $\rho$ (negative $\rho$ produces a downward-sloping skew).
    - The smile **curvature** (convexity) is primarily driven by $\sigma_v$ (higher vol-of-vol produces fatter tails and more curvature).
    - The 10-delta options, being further OTM, are especially sensitive to $\sigma_v$ because they probe the tail behavior.

    Formally, the Jacobian $J$ for Set (B) has larger singular values in the directions corresponding to $\sigma_v$ and $\rho$, because the OTM options introduce rows in $J$ with substantial partial derivatives $\partial \sigma^{\text{impl}}_j / \partial \sigma_v$ and $\partial \sigma^{\text{impl}}_j / \partial \rho$. This increases the rank and reduces the condition number of $J^\top W J$, improving both structural and practical identifiability for these parameters.

---

**Exercise 6.** Consider a re-parameterization from $(\sigma_0, \kappa) \mapsto (\sigma_0^2, \kappa / \sigma_0)$ in a mean-reverting volatility model. Compute the Jacobian of the transformation and discuss under what conditions the re-parameterization improves identifiability. When could it make identifiability worse?

??? success "Solution to Exercise 6"
    Let the original parameters be $\phi = (\sigma_0, \kappa)$ and the re-parameterized parameters be $\psi = (\sigma_0^2, \kappa/\sigma_0)$. Define the transformation $T: \phi \mapsto \psi$ by

    $$
    \psi_1 = \sigma_0^2, \quad \psi_2 = \frac{\kappa}{\sigma_0}
    $$

    The Jacobian of the transformation is

    $$
    \frac{\partial \psi}{\partial \phi} = \begin{pmatrix} \dfrac{\partial \psi_1}{\partial \sigma_0} & \dfrac{\partial \psi_1}{\partial \kappa} \\[8pt] \dfrac{\partial \psi_2}{\partial \sigma_0} & \dfrac{\partial \psi_2}{\partial \kappa} \end{pmatrix} = \begin{pmatrix} 2\sigma_0 & 0 \\[4pt] -\dfrac{\kappa}{\sigma_0^2} & \dfrac{1}{\sigma_0} \end{pmatrix}
    $$

    The determinant is

    $$
    \det\left(\frac{\partial\psi}{\partial\phi}\right) = \frac{2\sigma_0}{\sigma_0} = 2
    $$

    which is nonzero for all $\sigma_0 \neq 0$, so the transformation is locally invertible (a diffeomorphism) whenever $\sigma_0 > 0$.

    **When re-parameterization improves identifiability:**

    If the forward pricing map $F$ depends on $\sigma_0$ and $\kappa$ primarily through the combinations $\sigma_0^2$ (variance level) and $\kappa/\sigma_0$ (a dimensionless ratio controlling the speed-to-volatility balance), then the Jacobian $\tilde{J} = \partial F / \partial \psi$ will have more uniform singular values than the original $J = \partial F / \partial \phi$. This occurs when:

    - The model prices are naturally functions of variance (not volatility), making $\psi_1 = \sigma_0^2$ a more "linear" parameterization.
    - The ratio $\kappa/\sigma_0$ captures the economically meaningful quantity (e.g., related to the Feller ratio $2\kappa\bar{v}/\sigma_v^2$ in Heston-type models), so the data directly constrain $\psi_2$.

    In such cases, the condition number $\kappa(\tilde{J}^\top \tilde{J})$ is smaller than $\kappa(J^\top J)$, improving practical identifiability.

    **When it could make identifiability worse:**

    - If $\sigma_0$ is small, the entry $1/\sigma_0$ in the Jacobian becomes large, introducing numerical instability in the transformed parameterization.
    - If the model prices depend on $\sigma_0$ and $\kappa$ in a way that does not factor through $\sigma_0^2$ and $\kappa/\sigma_0$, then the re-parameterization introduces unnecessary nonlinearity, potentially creating new parameter correlations.
    - Near $\sigma_0 = 0$, the transformation is degenerate ($\psi_2 \to \infty$), so the re-parameterization is ill-defined in that region.

---

**Exercise 7.** You observe that a calibrated parameter $\hat\theta_3$ fluctuates wildly from day to day despite stable market conditions. Describe a bootstrap-based diagnostic procedure to assess whether $\theta_3$ is practically identifiable. Specifically, outline the resampling scheme, the quantity to compute for each bootstrap sample, and the criterion for declaring weak identifiability.

??? success "Solution to Exercise 7"
    **Bootstrap diagnostic procedure for assessing practical identifiability of $\theta_3$:**

    **Step 1 -- Resampling scheme.**

    Use a **parametric bootstrap** based on bid-ask uncertainty:

    1. Start with the calibrated parameter vector $\hat\theta$ and the set of $m$ market implied volatilities $\{y_j\}_{j=1}^m$.
    2. For each bootstrap replicate $b = 1, \ldots, B$ (with $B \ge 500$, ideally $B = 1000$):
        - Generate perturbed market data $y_j^{(b)} = y_j + \varepsilon_j^{(b)}$, where $\varepsilon_j^{(b)} \sim \text{Uniform}[-s_j, s_j]$ and $s_j$ is the bid-ask half-width of instrument $j$ (or $\varepsilon_j^{(b)} \sim N(0, s_j^2)$ for a Gaussian perturbation).
        - Re-calibrate the model to $y^{(b)}$ using the same optimization procedure and starting point, obtaining $\hat\theta^{(b)}$.

    **Step 2 -- Quantity to compute.**

    For each bootstrap sample $b$, record the full parameter vector $\hat\theta^{(b)}$. Then compute:

    - The bootstrap distribution of $\hat\theta_3^{(b)}$ across all $B$ replicates.
    - The bootstrap standard deviation: $\text{sd}(\hat\theta_3) = \sqrt{\frac{1}{B-1}\sum_{b=1}^B (\hat\theta_3^{(b)} - \bar\theta_3)^2}$.
    - The bootstrap 95% confidence interval: $[\hat\theta_3^{(0.025)}, \hat\theta_3^{(0.975)}]$ (empirical quantiles).
    - The coefficient of variation: $\text{CV} = \text{sd}(\hat\theta_3) / |\bar\theta_3|$.
    - Pairwise scatter plots of $(\hat\theta_3^{(b)}, \hat\theta_k^{(b)})$ for all other parameters $k$, to detect correlated instability (a sign of parameter entanglement).

    **Step 3 -- Criterion for declaring weak identifiability.**

    Declare $\theta_3$ weakly identifiable if any of the following hold:

    - The coefficient of variation exceeds a threshold: $\text{CV}(\hat\theta_3) > 0.5$ (i.e., the standard deviation is more than half the mean).
    - The 95% bootstrap confidence interval spans a range that is economically meaningless (e.g., for a correlation parameter, if the interval covers $[-0.9, 0.3]$, the parameter is essentially unconstrained).
    - The bootstrap distribution is bimodal or highly non-Gaussian, indicating multiple local minima or a flat loss landscape.
    - The scatter plots reveal strong linear correlations between $\theta_3$ and another parameter (ridge-like structure), indicating parameter degeneracy.

    If weak identifiability is confirmed, the recommended actions are: regularize $\theta_3$ toward a prior, fix it to a literature value, or re-parameterize the model to remove the redundancy.
