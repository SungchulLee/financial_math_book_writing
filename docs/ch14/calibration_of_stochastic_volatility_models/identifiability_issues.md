# Identifiability Issues


Recall (see [§ Identifiability of Model Parameters](../../ch17/calibration_as_inverse_problem/identifiability_of_model_parameters.md)) the general inverse-problem perspective on identifiability. This page focuses on identifiability obstacles *specific to stochastic volatility models*.

Calibration of SV models is fundamentally limited by **identifiability**. Even with rich option surfaces, some parameters are only weakly constrained, leading to instability and ambiguity.

---

## Structural vs practical identifiability


A model is **structurally identifiable** if distinct parameter sets imply distinct option prices in theory.
In practice, calibration suffers from:

- finite and noisy data,
- limited maturity coverage,
- redundancy in parameter effects.

Thus, many parameters are only *practically* identifiable within wide confidence bands.

---

## Typical weakly identifiable parameters


Across SV models (Heston specifics: see [§ Heston Calibration Pipeline](../../ch17/sv_calibration/heston_calibration_pipeline.md); SABR specifics: see [§ SABR Calibration Workflow](../../ch17/sv_calibration/sabr_calibration_workflow.md)), common weak points include:

- long-run variance vs initial variance,
- mean reversion speed,
- volatility-of-volatility at long maturities.

These parameters often affect prices in similar ways over limited horizons.

---

## Manifestations in calibration


Poor identifiability appears as:

- flat loss surfaces,
- multiple local minima,
- large day-to-day parameter swings,
- good in-sample fit but poor out-of-sample behavior.

These are inverse-problem symptoms, not optimizer failures.

---

## Diagnostic tools


Useful diagnostics include:

- Jacobian and singular-value analysis,
- fixing subsets of parameters and re-fitting,
- sensitivity analysis across maturities,
- stability checks under quote perturbations.

---

## Key takeaways


- Not all parameters are equally identifiable.
- Weak identifiability is intrinsic to stochastic volatility models.
- Calibration should prioritize stable directions.

---

## Further reading


- Engl, Hanke & Neubauer, *Regularization of Inverse Problems*.
- Gatheral, *The Volatility Surface*.

---

## Exercises

**Exercise 1.** In the Heston model, both $V_0$ and $\theta$ affect the ATM implied volatility level. Explain why these parameters are weakly identifiable when only short-maturity options are available. How does adding long-maturity options improve the situation? (Hint: consider the ATM variance formula $\sigma^2_{\text{impl}}(T) \approx V_0 \cdot \frac{1-e^{-\kappa T}}{\kappa T} + \theta(1 - \frac{1-e^{-\kappa T}}{\kappa T})$.)

??? success "Solution to Exercise 1"
    The approximate ATM implied variance at maturity $T$ is

    $$
    \sigma^2_{\text{impl}}(T) \approx V_0 \cdot \frac{1 - e^{-\kappa T}}{\kappa T} + \theta\Bigl(1 - \frac{1 - e^{-\kappa T}}{\kappa T}\Bigr)
    $$

    Define the weight function $\alpha(T) = \frac{1 - e^{-\kappa T}}{\kappa T}$, so that $\sigma^2_{\text{impl}}(T) \approx \alpha(T) V_0 + (1 - \alpha(T))\theta$. This is a weighted average of $V_0$ and $\theta$, with the weight $\alpha(T)$ decreasing from $1$ (at $T = 0$) toward $0$ (as $T \to \infty$).

    **When only short-maturity options are available:** For small $T$, $\alpha(T) \approx 1 - \kappa T/2$, so $\alpha(T)$ is close to $1$ and $1 - \alpha(T) \approx \kappa T/2$ is small. The ATM implied variance is dominated by $V_0$, with only a tiny contribution from $\theta$. This means:

    - The data primarily constrains $V_0$
    - The parameter $\theta$ enters only through a small correction term proportional to $\kappa T/2$
    - The effects of $V_0$ and $\theta$ are nearly collinear: increasing $V_0$ by $\epsilon$ and decreasing $\theta$ by $\epsilon \alpha(T)/(1-\alpha(T))$ leaves the implied variance nearly unchanged

    Therefore $V_0$ and $\theta$ are weakly identifiable — many $(V_0, \theta)$ combinations fit the short-maturity data equally well.

    **Adding long-maturity options improves identifiability:** At long maturities, $\alpha(T) \to 0$, so $\sigma^2_{\text{impl}}(T) \approx \theta$. The long-maturity ATM variance pins down $\theta$ independently of $V_0$. With $\theta$ determined from long maturities and $V_0$ determined from short maturities, the two parameters become separately identifiable. The different maturity regimes break the degeneracy by providing data where the two parameters have distinct effects.

---

**Exercise 2.** A practitioner observes that two Heston parameter sets give nearly identical option prices across all observed strikes and maturities:

| Parameter | Set A | Set B |
|-----------|-------|-------|
| $\kappa$  | 1.5   | 4.0   |
| $\theta$  | 0.06  | 0.035 |
| $\xi$     | 0.45  | 0.52  |
| $\rho$    | $-0.68$ | $-0.71$ |
| $V_0$     | 0.04  | 0.04  |

Compute $\kappa\theta$ for each set. Calculate the Feller ratio $\nu = 2\kappa\theta/\xi^2$ for each. Even though prices are similar, do the two parameter sets have different implications for simulation and risk management?

??? success "Solution to Exercise 2"
    **Computing $\kappa\theta$:**

    $$
    \kappa_A\theta_A = 1.5 \times 0.06 = 0.09
    $$

    $$
    \kappa_B\theta_B = 4.0 \times 0.035 = 0.14
    $$

    **Computing the Feller ratio $\nu = 2\kappa\theta/\xi^2$:**

    $$
    \nu_A = \frac{2 \times 1.5 \times 0.06}{0.45^2} = \frac{0.18}{0.2025} \approx 0.889
    $$

    $$
    \nu_B = \frac{2 \times 4.0 \times 0.035}{0.52^2} = \frac{0.28}{0.2704} \approx 1.035
    $$

    **Implications for simulation and risk management:**

    Although both parameter sets produce nearly identical option prices, they have very different implications:

    - **Feller condition:** Set A has $\nu_A < 1$, meaning the Feller condition $2\kappa\theta \geq \xi^2$ is violated. The variance process can hit zero, requiring careful treatment in Monte Carlo simulation (e.g., absorption, reflection, or truncation schemes). Set B has $\nu_B > 1$, barely satisfying the Feller condition — the variance stays strictly positive almost surely.
    - **Simulation behavior:** Set A with its lower $\kappa = 1.5$ exhibits slower mean reversion, meaning volatility excursions are more persistent. Set B with $\kappa = 4.0$ reverts much faster. Although option prices integrate over paths and may be similar, path-level behavior differs substantially, affecting path-dependent derivative pricing (barriers, lookbacks, Asian options).
    - **Risk management:** The different mean-reversion speeds imply different variance dynamics. Set A produces longer volatility clusters and heavier-tailed return distributions over short horizons, while Set B implies quicker normalization. VaR and Expected Shortfall estimates based on simulated paths would differ between the two parameterizations.

    This demonstrates that identical calibration fit does not guarantee identical risk characteristics, highlighting the practical danger of weak identifiability.

---

**Exercise 3.** Describe how to perform a Jacobian-based identifiability analysis. For a Heston model with parameter vector $\theta = (\kappa, \bar{\theta}, \xi, \rho, V_0)$ and $M$ observed implied volatilities $\sigma_i^{\text{mkt}}$, define the Jacobian matrix $J_{ij} = \partial\sigma_i^{\text{model}}/\partial\theta_j$. Explain how the singular values of $J$ reveal which parameter combinations are well-identified and which are not.

??? success "Solution to Exercise 3"
    **Jacobian-based identifiability analysis:**

    Given the Heston parameter vector $\theta = (\kappa, \bar{\theta}, \xi, \rho, V_0) \in \mathbb{R}^5$ and $M$ observed implied volatilities $\sigma_i^{\text{mkt}}$, define the model map $F: \mathbb{R}^5 \to \mathbb{R}^M$ with $F_i(\theta) = \sigma_i^{\text{model}}(\theta)$. The Jacobian is the $M \times 5$ matrix

    $$
    J_{ij} = \frac{\partial \sigma_i^{\text{model}}}{\partial \theta_j}
    $$

    which can be computed via finite differences or adjoint methods.

    **Singular value decomposition (SVD):** Compute $J = U \Sigma V^T$ where $\Sigma = \text{diag}(s_1, s_2, s_3, s_4, s_5)$ with $s_1 \geq s_2 \geq \cdots \geq s_5 \geq 0$. The columns of $V$ define parameter-space directions (linear combinations of parameters), and the corresponding singular values $s_j$ measure how sensitively the implied vol surface responds to perturbations in each direction.

    **Interpretation:**

    - **Large singular values** correspond to well-identified parameter combinations: a small change in these directions produces a large change in implied vols, so the data strongly constrains these combinations.
    - **Small singular values** correspond to weakly identified directions: the data barely constrains these parameter combinations. The condition number $s_1/s_5$ quantifies overall ill-conditioning.
    - If $s_5 \approx 0$, there is a direction $v_5$ in parameter space along which the model response is nearly flat — this is the least identifiable combination. Typically, $v_5$ lies close to the $(\kappa, \theta)$ plane, reflecting the $\kappa$-$\theta$ degeneracy.

    The SVD thus reveals not just *which* parameters are poorly identified, but which *combinations* are problematic, guiding reparameterization and regularization strategies.

---

**Exercise 4.** Fixing $V_0$ from ATM short-maturity implied volatility reduces the Heston model to four free parameters. Explain why this improves practical identifiability. What potential issue arises if ATM implied vol is measured with noise? Propose an alternative approach that avoids fixing $V_0$ while still improving identifiability.

??? success "Solution to Exercise 4"
    **Why fixing $V_0$ improves practical identifiability:** Setting $V_0 = \sigma_{\text{ATM}}^2(T_{\min})$ (the ATM implied variance at the shortest maturity) removes one dimension from the parameter space and, more importantly, eliminates the $V_0$-$\theta$ degeneracy at short maturities. With $V_0$ fixed, the short-maturity smile constrains $(\rho, \xi)$ and the term structure constrains $(\kappa, \theta)$ with less interference. The Jacobian matrix loses one column, and the remaining singular values are typically better separated.

    **Potential issue with noisy ATM vol:** If the ATM implied vol is measured with noise (e.g., wide bid-ask spreads, illiquidity, or stale quotes), fixing $V_0$ imports this noise as a systematic bias. All other parameters will shift to compensate for the incorrect $V_0$, and the resulting calibration may be worse than a free optimization that could find a better $V_0$. This is particularly problematic in illiquid markets or for very short maturities where the ATM level can be uncertain by several vol points.

    **Alternative approach:** Instead of hard-fixing $V_0$, use a **soft constraint** (regularization penalty):

    $$
    \mathcal{L}_{\text{reg}}(\theta) = \mathcal{L}(\theta) + \lambda_0 (V_0 - \hat{V}_0)^2
    $$

    where $\hat{V}_0 = \sigma_{\text{ATM}}^2(T_{\min})$ is the estimated value and $\lambda_0$ is a penalty weight. This anchors $V_0$ near the ATM-implied value without rigidly fixing it, allowing the optimizer to adjust $V_0$ slightly if the data strongly favors a different value. The penalty weight $\lambda_0$ controls the trade-off between using the ATM prior and fitting the data.

---

**Exercise 5.** A calibration produces a loss surface that is very flat in the $(\kappa, \theta)$ direction but steep in $(\rho, \xi)$. Sketch what this loss surface might look like in 2D cross-sections. What does the flatness imply about confidence intervals for $\kappa$ and $\theta$? Propose a reparameterization that might improve the conditioning of the optimization (e.g., calibrating $\kappa\theta$ and $\theta$ instead of $\kappa$ and $\theta$).

??? success "Solution to Exercise 5"
    **Loss surface structure:** In a 2D cross-section along the $(\kappa, \theta)$ direction, the contours of the loss function $\mathcal{L}(\kappa, \theta \mid \xi, \rho, V_0 \text{ fixed})$ are highly elongated ellipses, stretching along a curve approximately defined by $\kappa\theta \approx \text{const}$. The loss barely changes as one moves along this curve but increases rapidly when moving perpendicular to it. In contrast, the $(\rho, \xi)$ cross-section shows nearly circular contours — a well-conditioned landscape with a sharp minimum.

    **Implications for confidence intervals:** The flatness in $(\kappa, \theta)$ implies that:

    - Individual confidence intervals for $\kappa$ and $\theta$ are very wide
    - The parameters are strongly negatively correlated: a higher $\kappa$ compensates for a lower $\theta$
    - Marginal standard errors from the inverse Hessian dramatically understate the true uncertainty if off-diagonal correlations are ignored

    **Reparameterization:** Replace $(\kappa, \theta)$ with $(\phi, \theta)$ where $\phi = \kappa\theta$ is the mean-reversion pull. The reparameterized loss surface $\mathcal{L}(\phi, \theta, \xi, \rho, V_0)$ will have more circular contours in the $(\phi, \theta)$ direction because $\phi$ captures the well-identified combination directly. The optimizer converges faster, the Hessian is better conditioned, and the resulting confidence intervals for $\phi$ are narrow and meaningful.

    Alternatively, one could calibrate $(\kappa\theta, \theta/\kappa)$ or use $(\log\kappa, \log\theta)$ to improve scaling. The key insight is to align the parameterization with the identifiable directions of the loss surface.

---

**Exercise 6.** An options surface has quotes only at maturities $T = 0.25$ and $T = 0.5$ years. Explain why the mean-reversion speed $\kappa$ is especially poorly identified in this case. What is the minimum set of maturities you would need to reliably identify $\kappa$? How does the half-life $t_{1/2} = \ln 2/\kappa$ relate to the required maturity range?

??? success "Solution to Exercise 6"
    **Why $\kappa$ is poorly identified with only $T = 0.25$ and $T = 0.5$:** The mean-reversion speed $\kappa$ controls how quickly the variance process converges from $V_0$ toward $\theta$. Its effect on option prices is primarily through the term structure — how ATM implied volatility varies across maturities. The expected variance at time $T$ is

    $$
    \mathbb{E}[V_T] = \theta + (V_0 - \theta)e^{-\kappa T}
    $$

    For the two available maturities, $e^{-\kappa \times 0.25}$ and $e^{-\kappa \times 0.5}$ differ by a factor of $e^{-0.25\kappa}$. When the maturity range is narrow (only 0.25 years separating the two tenors), the exponential function is nearly linear over this interval, making it difficult to distinguish between different $\kappa$ values. Specifically, for $\kappa = 2$, we get $e^{-0.5} = 0.607$ and $e^{-1.0} = 0.368$, while for $\kappa = 4$, we get $e^{-1.0} = 0.368$ and $e^{-2.0} = 0.135$. The ratio of these values carries the information about $\kappa$, but with noisy data, distinguishing these ratios requires sufficient maturity separation.

    **Minimum maturity set:** To reliably identify $\kappa$, the maturity range should span at least one half-life $t_{1/2} = \ln 2/\kappa$, and preferably two to three half-lives. A good minimum set would include:

    - A short maturity $T_1 \leq 0.25$ (to pin down $V_0$)
    - A medium maturity $T_2 \approx t_{1/2}$ (where mean reversion has had a visible effect)
    - A long maturity $T_3 \geq 2t_{1/2}$ (where the variance is close to $\theta$)

    For typical values $\kappa \in [1, 5]$, we have $t_{1/2} \in [0.14, 0.69]$ years, so maturities spanning at least $0.1$ to $1.5$ years are needed.

    **Half-life relationship:** The half-life $t_{1/2} = \ln 2/\kappa$ is the time for the expected variance to move halfway from $V_0$ to $\theta$. If the maximum available maturity $T_{\max}$ is much less than $t_{1/2}$, the variance process has barely begun to mean-revert, and $\kappa$ has almost no effect on observable prices — it is effectively unidentifiable. Conversely, if $T_{\max} \gg t_{1/2}$, the variance is essentially at $\theta$ for all long-dated options, and $\kappa$ only affects intermediate maturities. The ideal scenario is $T_{\max} \approx 2$--$3 \times t_{1/2}$, providing data in the transition region where $\kappa$ has maximum impact.
