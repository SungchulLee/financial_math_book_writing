# Confidence Sets for Models


## Introduction


**Confidence sets for models** provide a rigorous statistical framework for quantifying uncertainty about model parameters and specifications. Rather than relying on point estimates, confidence sets characterize the range of parameter values or models that are statistically consistent with observed data.

In quantitative finance, confidence sets are essential for:

1. **Robust pricing**: Determining price bounds consistent with market data
2. **Risk management**: Quantifying parameter uncertainty in VaR calculations
3. **Model validation**: Testing whether calibrated models are statistically consistent
4. **Regulatory compliance**: Demonstrating model uncertainty quantification

## Statistical Foundations


### 1. Confidence Regions


**Definition**: A $(1-\alpha)$ confidence region for parameter $\theta$ is a random set $C_n = C_n(X_1, \ldots, X_n)$ such that:

$$
P_{\theta}(\theta \in C_n) \geq 1 - \alpha \quad \text{for all } \theta \in \Theta
$$

**Interpretation**: Under repeated sampling, the confidence region contains the true parameter at least $(1-\alpha)$ of the time.

### 2. Likelihood-Based Confidence Regions


**Log-Likelihood**: For observations $X_1, \ldots, X_n$:

$$
\ell(\theta) = \sum_{i=1}^n \log f(X_i; \theta)
$$

**Likelihood Ratio Statistic**:

$$
\Lambda_n(\theta) = 2[\ell(\hat{\theta}) - \ell(\theta)]
$$

where $\hat{\theta}$ is the MLE.

**Wilks' Theorem**: Under regularity conditions:

$$
\Lambda_n(\theta_0) \xrightarrow{d} \chi^2_p
$$

where $p = \dim(\theta)$.

**Confidence Region**:

$$
C_n = \{\theta: \Lambda_n(\theta) \leq \chi^2_{p, 1-\alpha}\}
$$

### 3. Wald Confidence Regions


**Asymptotic Normality**:

$$
\sqrt{n}(\hat{\theta} - \theta_0) \xrightarrow{d} N(0, I(\theta_0)^{-1})
$$

where $I(\theta)$ is the Fisher information.

**Wald Region**:

$$
C_n^W = \{\theta: n(\hat{\theta} - \theta)^\top \hat{I}(\hat{\theta})(\hat{\theta} - \theta) \leq \chi^2_{p, 1-\alpha}\}
$$

This is an ellipsoid centered at the MLE.

### 4. Bootstrap Confidence Regions


**Percentile Bootstrap**:

1. Resample $X_1^*, \ldots, X_n^*$ from empirical distribution
2. Compute $\hat{\theta}^*$ from bootstrap sample
3. Repeat $B$ times
4. Confidence region from quantiles of $\{\hat{\theta}^{*(b)}\}$

**Bias-Corrected Bootstrap**: Adjusts for bias in bootstrap distribution.

## Confidence Sets in Option Pricing


### 1. Implied Volatility Uncertainty


**Setup**: Observe option prices $C_1, \ldots, C_m$ with strikes $K_1, \ldots, K_m$.

**Model**: Black-Scholes prices $C_i^{BS}(\sigma)$ as function of volatility $\sigma$.

**Calibration Error**:

$$
Q(\sigma) = \sum_{i=1}^m w_i [C_i - C_i^{BS}(\sigma)]^2
$$

**Confidence Set for $\sigma$**:

$$
\mathcal{C}_{\sigma} = \{\sigma: Q(\sigma) - Q(\hat{\sigma}) \leq \Delta_{\alpha}\}
$$

where $\Delta_{\alpha}$ depends on the error distribution.

### 2. Stochastic Volatility Model Calibration


**Heston Model Parameters**: $\theta = (\kappa, \bar{v}, \sigma_v, \rho, v_0)$

**Confidence Region**: 

$$
\mathcal{C}_{\theta} = \{\theta: \ell(\theta) \geq \ell(\hat{\theta}) - \frac{1}{2}\chi^2_{5, 1-\alpha}\}
$$

**Challenge**: High-dimensional confidence regions are difficult to visualize and interpret.

### 3. Profile Likelihood


**Definition**: For parameter of interest $\psi = g(\theta)$:

$$
\ell_p(\psi) = \max_{\theta: g(\theta) = \psi} \ell(\theta)
$$

**Profile Confidence Interval**:

$$
\mathcal{C}_{\psi} = \{\psi: 2[\ell(\hat{\theta}) - \ell_p(\psi)] \leq \chi^2_{1, 1-\alpha}\}
$$

**Application**: Confidence interval for a single Greek while accounting for uncertainty in other parameters.

## Model Confidence Sets


### 1. Hansen's Model Confidence Set


**Setup**: Compare $m$ models $\{M_1, \ldots, M_m\}$ based on loss function $L_{i,t}$ for model $i$ at time $t$.

**Superior Set**: $\mathcal{M}^* = \{M_i: \mathbb{E}[L_{i,t}] \leq \mathbb{E}[L_{j,t}] \text{ for some } j\}$

**MCS Algorithm** (Hansen, Lunde, Nason, 2011):

1. Start with all models: $\hat{\mathcal{M}} = \{M_1, \ldots, M_m\}$
2. Test equal predictive ability: $H_0: \mathbb{E}[d_{ij,t}] = 0$ for all $i, j \in \hat{\mathcal{M}}$
3. If $H_0$ rejected, eliminate worst model
4. Repeat until $H_0$ not rejected

**Result**: $\hat{\mathcal{M}}_{1-\alpha}$ contains $\mathcal{M}^*$ with probability $\geq 1 - \alpha$.

### 2. Test Statistics for MCS


**Range Statistic**:

$$
T_R = \max_{i,j \in \hat{\mathcal{M}}} \frac{|\bar{d}_{ij}|}{\sqrt{\hat{\text{var}}(\bar{d}_{ij})}}
$$

**Semi-Quadratic Statistic**:

$$
T_{SQ} = \sum_{i \in \hat{\mathcal{M}}} \left(\frac{\bar{d}_{i\cdot}}{\sqrt{\hat{\text{var}}(\bar{d}_{i\cdot})}}\right)^2 \mathbf{1}_{\bar{d}_{i\cdot} > 0}
$$

where $\bar{d}_{i\cdot} = \frac{1}{|\hat{\mathcal{M}}|} \sum_{j \in \hat{\mathcal{M}}} \bar{d}_{ij}$.

### 3. Application to Volatility Models


**Competing Models**: GARCH, EGARCH, GJR-GARCH, Realized Volatility, Implied Volatility

**Loss Function**: Quasi-likelihood loss or MSE for variance forecasting

**MCS Result**: Identifies which models cannot be distinguished from the best model at a given confidence level.

## Bayesian Credible Sets


### 1. Posterior Distribution


**Bayes' Theorem**:

$$
p(\theta | X) = \frac{L(X | \theta) \pi(\theta)}{\int L(X | \theta) \pi(\theta) d\theta}
$$

**Credible Set**: A $(1-\alpha)$ credible set $C$ satisfies:

$$
P(\theta \in C | X) = 1 - \alpha
$$

### 2. Highest Posterior Density Region


**Definition**: The HPD region is the smallest set with coverage $1-\alpha$:

$$
C_{\text{HPD}} = \{\theta: p(\theta | X) \geq c_{\alpha}\}
$$

where $c_{\alpha}$ is chosen so that $P(\theta \in C_{\text{HPD}} | X) = 1 - \alpha$.

**Property**: Among all $(1-\alpha)$ credible sets, HPD has minimum volume.

### 3. Comparison with Frequentist Sets


| Aspect | Confidence Set | Credible Set |
|--------|----------------|--------------|
| Interpretation | Coverage probability over repeated sampling | Posterior probability given data |
| Prior | Not required | Required |
| Parameter | Fixed unknown | Random variable |
| Small sample | May have poor coverage | Depends on prior |

### 4. Bayesian Model Uncertainty


**Posterior Model Probability**:

$$
P(M_k | X) = \frac{P(X | M_k) P(M_k)}{\sum_j P(X | M_j) P(M_j)}
$$

**Credible Model Set**: Include models until cumulative posterior probability exceeds $1 - \alpha$.

## Calibration Confidence Sets in Practice


### 1. Interest Rate Models


**Vasicek Parameters**: $\theta = (a, b, \sigma)$

**Calibration Data**: Zero-coupon bond prices or cap/floor prices

**Confidence Set Construction**:

1. Estimate $\hat{\theta}$ by minimizing pricing errors
2. Compute Hessian of objective at $\hat{\theta}$
3. Invert Hessian to get covariance estimate
4. Construct ellipsoidal confidence region

### 2. Credit Risk Models


**Merton Model**: Asset value follows GBM with parameters $(\mu, \sigma_A)$

**Challenge**: Asset value not directly observed

**Approach**: 

- Calibrate to equity price and implied volatility
- Propagate uncertainty through the structural model
- Confidence set for default probability

### 3. Numerical Methods


**Grid Search**: Evaluate likelihood on parameter grid, identify acceptable region.

**MCMC**: Sample from posterior, use samples to characterize credible region.

**Optimization-Based**: Start from MLE, trace boundary of acceptable region.

## Uncertainty Propagation


### 1. Delta Method


**Transformation**: For $g(\theta)$ smooth:

$$
\sqrt{n}(g(\hat{\theta}) - g(\theta)) \xrightarrow{d} N\left(0, \nabla g(\theta)^\top \Sigma \nabla g(\theta)\right)
$$

**Confidence Interval for $g(\theta)$**:

$$
g(\hat{\theta}) \pm z_{1-\alpha/2} \sqrt{\nabla g(\hat{\theta})^\top \hat{\Sigma} \nabla g(\hat{\theta}) / n}
$$

### 2. Monte Carlo Propagation


**Algorithm**:

1. Draw $\theta^{(1)}, \ldots, \theta^{(B)}$ from confidence region or posterior
2. Compute $y^{(b)} = g(\theta^{(b)})$ for each draw
3. Confidence interval from quantiles of $\{y^{(b)}\}$

### 3. Application to Greek Uncertainty


**Example**: Delta uncertainty given parameter uncertainty

$$
\Delta(\theta) = \frac{\partial V}{\partial S}(\theta)
$$

**Confidence Interval**: Propagate parameter confidence set through $\Delta(\cdot)$.

## Summary


### Key Methods


1. **Likelihood-Based**: Wilks' theorem provides asymptotic confidence regions via likelihood ratio

2. **Bootstrap**: Resampling-based confidence sets without distributional assumptions

3. **Model Confidence Sets**: Hansen's MCS identifies statistically indistinguishable models

4. **Bayesian Credible Sets**: Posterior-based uncertainty quantification

### Practical Guidelines


1. **Dimensionality**: Use profile likelihood for interpretable low-dimensional sets
2. **Model Comparison**: MCS provides rigorous multiple model comparison
3. **Propagation**: Combine confidence sets with sensitivity analysis for derived quantities
4. **Reporting**: Report confidence sets alongside point estimates

Confidence sets for models provide the statistical foundation for quantifying and communicating uncertainty in calibrated financial models.

---

## Exercises

**Exercise 1.** For a Black-Scholes model calibrated to $m = 5$ call options, the MLE is $\hat{\sigma} = 0.22$ with log-likelihood $\ell(\hat{\sigma}) = -12.5$. Using Wilks' theorem, construct a 95% confidence interval for $\sigma$. The critical value is $\chi^2_{1, 0.95} = 3.84$. If $\ell(\sigma)$ is approximately quadratic near the MLE with curvature $\ell''(\hat{\sigma}) = -500$, compute the confidence interval explicitly.

??? success "Solution to Exercise 1"

    We are given $\hat{\sigma} = 0.22$, $\ell(\hat{\sigma}) = -12.5$, $\chi^2_{1,0.95} = 3.84$, and $\ell''(\hat{\sigma}) = -500$.

    **Wilks' theorem confidence interval.** By Wilks' theorem, the 95% confidence region is

    $$
    \mathcal{C} = \{\sigma : 2[\ell(\hat{\sigma}) - \ell(\sigma)] \leq 3.84\}
    $$

    which is equivalent to

    $$
    \mathcal{C} = \{\sigma : \ell(\sigma) \geq \ell(\hat{\sigma}) - 1.92\} = \{\sigma : \ell(\sigma) \geq -14.42\}
    $$

    **Quadratic approximation.** Since the log-likelihood is approximately quadratic near the MLE:

    $$
    \ell(\sigma) \approx \ell(\hat{\sigma}) + \frac{1}{2}\ell''(\hat{\sigma})(\sigma - \hat{\sigma})^2 = -12.5 - 250(\sigma - 0.22)^2
    $$

    Substituting into the Wilks condition:

    $$
    2\left[-\frac{1}{2}\ell''(\hat{\sigma})(\sigma - \hat{\sigma})^2\right] \leq 3.84
    $$

    $$
    2 \cdot 250 \cdot (\sigma - 0.22)^2 \leq 3.84
    $$

    $$
    (\sigma - 0.22)^2 \leq \frac{3.84}{500} = 0.00768
    $$

    $$
    |\sigma - 0.22| \leq \sqrt{0.00768} \approx 0.0877
    $$

    Therefore the 95% confidence interval is approximately

    $$
    \sigma \in (0.22 - 0.0877, \; 0.22 + 0.0877) = (0.1323, \; 0.3077)
    $$

    Note that the observed Fisher information is $\hat{I} = -\ell''(\hat{\sigma}) = 500$, so the asymptotic standard error is $\text{se}(\hat{\sigma}) = 1/\sqrt{500} \approx 0.0447$, and the Wald interval $\hat{\sigma} \pm 1.96 \times 0.0447 = (0.1324, 0.3076)$ agrees closely.

---

**Exercise 2.** Consider a two-parameter model $\theta = (\sigma, \rho)$ calibrated from option prices. The Fisher information matrix at the MLE $\hat{\theta} = (0.25, -0.65)$ is

$$
\hat{I} = \begin{pmatrix} 400 & 50 \\ 50 & 200 \end{pmatrix}
$$

Construct the 95% Wald confidence ellipse. Compute the semi-axes of the ellipse and explain which parameter direction is most precisely estimated.

??? success "Solution to Exercise 2"

    We have $\hat{\theta} = (0.25, -0.65)$ and

    $$
    \hat{I} = \begin{pmatrix} 400 & 50 \\ 50 & 200 \end{pmatrix}
    $$

    **Wald confidence ellipse.** The 95% Wald confidence region is

    $$
    \mathcal{C}^W = \{\theta : (\hat{\theta} - \theta)^\top \hat{I} (\hat{\theta} - \theta) \leq \chi^2_{2, 0.95}\}
    $$

    With $\chi^2_{2, 0.95} = 5.991$, this defines an ellipse centered at $\hat{\theta}$.

    **Semi-axes computation.** The ellipse shape is determined by the eigenvalues of $\hat{I}$. We solve $\det(\hat{I} - \mu I) = 0$:

    $$
    (400 - \mu)(200 - \mu) - 2500 = 0
    $$

    $$
    \mu^2 - 600\mu + 77500 = 0
    $$

    $$
    \mu = \frac{600 \pm \sqrt{360000 - 310000}}{2} = \frac{600 \pm \sqrt{50000}}{2} = \frac{600 \pm 223.6}{2}
    $$

    So $\mu_1 = 411.8$ and $\mu_2 = 188.2$.

    The semi-axes of the confidence ellipse have lengths

    $$
    a_i = \sqrt{\frac{\chi^2_{2,0.95}}{\mu_i}}
    $$

    $$
    a_1 = \sqrt{\frac{5.991}{411.8}} \approx \sqrt{0.01455} \approx 0.1206
    $$

    $$
    a_2 = \sqrt{\frac{5.991}{188.2}} \approx \sqrt{0.03183} \approx 0.1784
    $$

    **Eigenvector directions.** For $\mu_1 = 411.8$:

    $$
    (400 - 411.8)x + 50y = 0 \implies y = 0.236x
    $$

    So the direction of the shorter semi-axis is approximately $(1, 0.236)/\|(1, 0.236)\| \approx (0.973, 0.230)$, which is close to the $\sigma$-axis.

    **Interpretation.** The larger eigenvalue $\mu_1 = 411.8$ corresponds to the direction most precisely estimated (shortest semi-axis $a_1 = 0.1206$). This direction is close to the $\sigma$-axis, meaning $\sigma$ is more precisely estimated than $\rho$. The direction of greatest uncertainty ($a_2 = 0.1784$) is approximately along the $\rho$-axis. The off-diagonal element $50$ introduces a tilt, indicating a mild correlation between the estimators of $\sigma$ and $\rho$.

---

**Exercise 3.** Explain the profile likelihood method for constructing a confidence interval for $\sigma$ in the Heston model while accounting for uncertainty in $(\kappa, \bar{v}, \sigma_v, \rho, v_0)$. Write the profile log-likelihood $\ell_p(\sigma) = \max_{\kappa, \bar{v}, \sigma_v, \rho, v_0} \ell(\sigma, \kappa, \bar{v}, \sigma_v, \rho, v_0)$ and explain why this interval is generally wider than the interval obtained by fixing all other parameters at their MLE values.

??? success "Solution to Exercise 3"

    **Profile likelihood definition.** In the Heston model with full parameter vector $\theta = (\sigma_v, \kappa, \bar{v}, \rho, v_0)$, suppose we want a confidence interval for $\sigma_v$ (vol-of-vol) alone. The profile log-likelihood is

    $$
    \ell_p(\sigma_v) = \max_{\kappa, \bar{v}, \rho, v_0} \ell(\sigma_v, \kappa, \bar{v}, \rho, v_0)
    $$

    For each fixed value of $\sigma_v$, we optimize the log-likelihood over the remaining four parameters. The profile confidence interval at level $1 - \alpha$ is

    $$
    \mathcal{C}_{\sigma_v} = \left\{\sigma_v : 2[\ell(\hat{\theta}) - \ell_p(\sigma_v)] \leq \chi^2_{1, 1-\alpha}\right\}
    $$

    where $\hat{\theta}$ is the full MLE.

    **Why the profile interval is wider.** Consider the alternative "plug-in" interval obtained by fixing all other parameters at their MLE values $(\hat{\kappa}, \hat{\bar{v}}, \hat{\rho}, \hat{v}_0)$ and varying only $\sigma_v$:

    $$
    \ell_{\text{plug-in}}(\sigma_v) = \ell(\sigma_v, \hat{\kappa}, \hat{\bar{v}}, \hat{\rho}, \hat{v}_0)
    $$

    Since the profile likelihood maximizes over the nuisance parameters, by definition

    $$
    \ell_p(\sigma_v) \geq \ell_{\text{plug-in}}(\sigma_v)
    $$

    for every $\sigma_v$. This means the profile likelihood decreases more slowly as $\sigma_v$ moves away from its MLE, because the other parameters can adjust to partially compensate. Consequently:

    $$
    2[\ell(\hat{\theta}) - \ell_p(\sigma_v)] \leq 2[\ell(\hat{\theta}) - \ell_{\text{plug-in}}(\sigma_v)]
    $$

    The set where the left side is below $\chi^2_{1,1-\alpha}$ is therefore larger than the set where the right side is below the same threshold. In other words, the profile interval is wider because it honestly accounts for uncertainty in the nuisance parameters. The plug-in interval is artificially narrow because it ignores correlations between $\sigma_v$ and $(\kappa, \bar{v}, \rho, v_0)$.

    **Practical implications.** In the Heston model, parameters are often highly correlated (e.g., $\kappa$ and $\bar{v}$ are nearly unidentifiable individually). The profile likelihood captures this by allowing compensating parameter shifts, resulting in a confidence interval that more accurately reflects the true uncertainty about $\sigma_v$.

---

**Exercise 4.** Hansen's Model Confidence Set (MCS) procedure compares $m = 4$ volatility models: GARCH, EGARCH, GJR-GARCH, and Realized Volatility. Suppose the average loss differences are $\bar{d}_{12} = 0.5$, $\bar{d}_{13} = 1.2$, $\bar{d}_{14} = -0.3$, with standard errors all approximately 0.4. Walk through one iteration of the MCS algorithm at the 10% significance level, identifying which model (if any) is eliminated first and why.

??? success "Solution to Exercise 4"

    **MCS algorithm setup.** We have $m = 4$ models: (1) GARCH, (2) EGARCH, (3) GJR-GARCH, (4) Realized Volatility, with average loss differences $\bar{d}_{12} = 0.5$, $\bar{d}_{13} = 1.2$, $\bar{d}_{14} = -0.3$, and standard errors $\approx 0.4$ for all pairs.

    **Step 1: Test equal predictive ability.** Recall $\bar{d}_{ij} = \bar{L}_i - \bar{L}_j$ where $\bar{L}_i$ is the average loss for model $i$. From the given data:

    - $\bar{d}_{12} = 0.5 > 0$: Model 1 has higher average loss than Model 2
    - $\bar{d}_{13} = 1.2 > 0$: Model 1 has higher average loss than Model 3
    - $\bar{d}_{14} = -0.3 < 0$: Model 1 has lower average loss than Model 4

    To find all pairwise differences, we use transitivity:

    - $\bar{d}_{23} = \bar{d}_{13} - \bar{d}_{12} = 1.2 - 0.5 = 0.7$
    - $\bar{d}_{24} = \bar{d}_{14} - \bar{d}_{12} = -0.3 - 0.5 = -0.8$
    - $\bar{d}_{34} = \bar{d}_{14} - \bar{d}_{13} = -0.3 - 1.2 = -1.5$

    **Step 2: Compute the range statistic.**

    $$
    T_R = \max_{i,j} \frac{|\bar{d}_{ij}|}{\text{se}(\bar{d}_{ij})}
    $$

    The standardized differences are:

    | Pair | $|\bar{d}_{ij}|/0.4$ |
    |------|----------------------|
    | (1,2) | 1.25 |
    | (1,3) | 3.00 |
    | (1,4) | 0.75 |
    | (2,3) | 1.75 |
    | (2,4) | 2.00 |
    | (3,4) | 3.75 |

    So $T_R = 3.75$, achieved by the pair $(3, 4)$.

    **Step 3: Test at 10% level.** Compare $T_R = 3.75$ against the bootstrap critical value for $T_R$ at the 10% significance level. For $m = 4$ models, the critical value under the null of equal predictive ability (obtained by bootstrap) is typically around 2.5--3.0 at the 10% level. Since $T_R = 3.75$ exceeds this, we reject $H_0$.

    **Step 4: Eliminate the worst model.** To identify the worst model, compute the average relative loss:

    $$
    \bar{d}_{i\cdot} = \frac{1}{m} \sum_{j} \bar{d}_{ij}
    $$

    - $\bar{d}_{1\cdot} = \frac{1}{4}(0 + 0.5 + 1.2 - 0.3) = 0.35$
    - $\bar{d}_{2\cdot} = \frac{1}{4}(-0.5 + 0 + 0.7 - 0.8) = -0.15$
    - $\bar{d}_{3\cdot} = \frac{1}{4}(-1.2 - 0.7 + 0 - 1.5) = -0.85$
    - $\bar{d}_{4\cdot} = \frac{1}{4}(0.3 + 0.8 + 1.5 + 0) = 0.65$

    Model 4 (Realized Volatility) has the highest $\bar{d}_{4\cdot} = 0.65$, meaning it has the worst average performance. **Model 4 is eliminated** in this iteration.

    The algorithm continues with models $\{1, 2, 3\}$ and repeats the test. If the null cannot be rejected for the remaining set, the MCS is $\hat{\mathcal{M}}_{0.90} = \{$GARCH, EGARCH, GJR-GARCH$\}$.

---

**Exercise 5.** Compare a 95% frequentist confidence interval with a 95% Bayesian highest posterior density (HPD) interval for volatility $\sigma$. If the prior is $\sigma \sim \text{Uniform}(0.1, 0.5)$ and the likelihood is concentrated around $\hat{\sigma} = 0.22$, explain qualitatively how the HPD interval differs from the likelihood-based confidence interval. Under what conditions do the two intervals approximately coincide?

??? success "Solution to Exercise 5"

    **Frequentist 95% confidence interval.** Using the likelihood-based approach, the confidence interval is

    $$
    \mathcal{C}_{\text{freq}} = \{\sigma : 2[\ell(\hat{\sigma}) - \ell(\sigma)] \leq 3.84\}
    $$

    This depends only on the likelihood function and is centered (approximately) at the MLE $\hat{\sigma} = 0.22$. It makes no reference to prior information about $\sigma$.

    **Bayesian 95% HPD interval.** The posterior is

    $$
    p(\sigma | X) \propto L(X | \sigma) \cdot \pi(\sigma) = L(X | \sigma) \cdot \mathbf{1}_{[0.1, 0.5]}(\sigma) \cdot \frac{1}{0.4}
    $$

    The HPD region is the shortest interval $C$ such that $P(\sigma \in C | X) = 0.95$.

    **Qualitative comparison:**

    1. **Truncation effect.** The uniform prior $\sigma \sim \text{Uniform}(0.1, 0.5)$ truncates the posterior at $\sigma = 0.1$ and $\sigma = 0.5$. If the likelihood-based interval extends below $0.1$ or above $0.5$, the HPD interval will be narrower because the prior excludes those values. With the likelihood concentrated around $0.22$ and the prior support $[0.1, 0.5]$, this truncation is most likely to affect the lower tail if the confidence interval extends below $0.1$.

    2. **Shape near boundaries.** Near the boundaries $0.1$ and $0.5$, the posterior drops abruptly to zero, while the likelihood-based interval transitions smoothly. The HPD, by selecting the highest-density region, efficiently avoids low-prior regions.

    3. **With concentrated likelihood.** Since the likelihood is concentrated around $\hat{\sigma} = 0.22$, which is well within the prior support $[0.1, 0.5]$, the prior is nearly flat over the high-likelihood region. In this regime, the posterior is approximately proportional to the likelihood alone.

    **Conditions for approximate coincidence.** The frequentist confidence interval and the Bayesian HPD interval approximately coincide when:

    - The prior is approximately flat (uninformative) over the high-likelihood region
    - The sample size is large enough that the likelihood dominates the prior (Bernstein-von Mises theorem)
    - The MLE is well-separated from the boundaries of the prior support

    Under these conditions, the posterior is approximately $N(\hat{\sigma}, I(\hat{\sigma})^{-1})$, which yields the same interval as the Wald confidence interval. In our example, with $\hat{\sigma} = 0.22$ well inside $[0.1, 0.5]$ and concentrated likelihood, the two intervals will be nearly identical.

---

**Exercise 6.** Using the delta method, derive the approximate variance of the Black-Scholes call price $C(\sigma)$ induced by parameter uncertainty $\hat{\sigma} \sim N(\sigma_0, s^2)$. Show that

$$
\text{Var}(C(\hat{\sigma})) \approx \left(\frac{\partial C}{\partial \sigma}\right)^2 s^2 = \text{Vega}^2 \cdot s^2
$$

For $S_0 = K = 100$, $T = 1$, $r = 0$, $\sigma_0 = 0.20$, and $s = 0.02$, compute the 95% confidence interval for the call price.

??? success "Solution to Exercise 6"

    **Delta method derivation.** The Black-Scholes call price is $C = C(\sigma)$. If $\hat{\sigma} \sim N(\sigma_0, s^2)$, then by the delta method:

    $$
    C(\hat{\sigma}) \approx C(\sigma_0) + C'(\sigma_0)(\hat{\sigma} - \sigma_0)
    $$

    Taking variances:

    $$
    \text{Var}(C(\hat{\sigma})) \approx [C'(\sigma_0)]^2 \cdot \text{Var}(\hat{\sigma}) = [C'(\sigma_0)]^2 \cdot s^2
    $$

    Since $C'(\sigma) = \frac{\partial C}{\partial \sigma} = \text{Vega}$, we have

    $$
    \text{Var}(C(\hat{\sigma})) \approx \text{Vega}^2 \cdot s^2
    $$

    **Numerical computation.** For $S_0 = K = 100$, $T = 1$, $r = 0$, $\sigma_0 = 0.20$:

    First, compute $d_1$ and $d_2$:

    $$
    d_1 = \frac{\ln(S_0/K) + (r + \sigma_0^2/2)T}{\sigma_0 \sqrt{T}} = \frac{0 + 0.02}{0.20} = 0.10
    $$

    $$
    d_2 = d_1 - \sigma_0 \sqrt{T} = 0.10 - 0.20 = -0.10
    $$

    The Black-Scholes call price:

    $$
    C = S_0 \mathcal{N}(d_1) - K e^{-rT} \mathcal{N}(d_2) = 100[\Phi(0.10) - \Phi(-0.10)]
    $$

    $$
    = 100[0.5398 - 0.4602] = 100 \times 0.0796 = 7.966
    $$

    The Vega:

    $$
    \text{Vega} = S_0 \sqrt{T} \phi(d_1) = 100 \cdot 1 \cdot \phi(0.10)
    $$

    where $\phi(0.10) = \frac{1}{\sqrt{2\pi}} e^{-0.005} = 0.3970$. So

    $$
    \text{Vega} = 100 \times 0.3970 = 39.70
    $$

    **Standard deviation of the call price:**

    $$
    \text{sd}(C(\hat{\sigma})) = \text{Vega} \cdot s = 39.70 \times 0.02 = 0.794
    $$

    **95% confidence interval for the call price:**

    $$
    C(\sigma_0) \pm 1.96 \times \text{Vega} \cdot s = 7.966 \pm 1.96 \times 0.794
    $$

    $$
    = 7.966 \pm 1.556 = (6.41, \; 9.52)
    $$

    The 95% confidence interval for the call price is approximately $(6.41, 9.52)$. This represents a relative uncertainty of about $\pm 19.5\%$, showing that even modest parameter uncertainty ($s = 0.02$ on $\sigma_0 = 0.20$, or 10% relative) translates into substantial pricing uncertainty for at-the-money options with high Vega.

---

**Exercise 7.** Design a bootstrap procedure to construct a confidence set for the Heston model parameters. Given $n = 100$ daily option price observations, describe the resampling scheme (parametric vs. nonparametric), the computation of bootstrap replicates $\hat{\theta}^{*(1)}, \ldots, \hat{\theta}^{*(B)}$, and the construction of the confidence region from these replicates. Discuss the computational challenges when each bootstrap replicate requires a full Heston calibration.

??? success "Solution to Exercise 7"

    **Bootstrap procedure design for Heston model parameters.**

    **Setup.** We observe $n = 100$ daily option price snapshots, each containing prices of $m$ options (across strikes and maturities). Denote the data as $\{C_{t,i}\}$ for $t = 1, \ldots, 100$ and $i = 1, \ldots, m$.

    **Step 1: Point estimate.** Calibrate the Heston model to the full dataset (or to each day separately and average) to obtain $\hat{\theta} = (\hat{\kappa}, \hat{\bar{v}}, \hat{\sigma}_v, \hat{\rho}, \hat{v}_0)$.

    **Step 2: Choose resampling scheme.**

    *Nonparametric bootstrap:* Resample the $n$ daily observation vectors $(C_{t,1}, \ldots, C_{t,m})$ with replacement to create a bootstrap dataset $\{C_{t^*,i}\}_{t^*=1}^n$. This preserves the cross-sectional dependence within each day but requires that daily snapshots are approximately independent (or weakly dependent).

    *Parametric bootstrap:* Simulate option prices from the fitted Heston model. For each day $t$:

    - Simulate $S_T$ paths under the Heston model with parameters $\hat{\theta}$
    - Compute model option prices and add noise: $C_{t,i}^* = C_i^{\text{Heston}}(\hat{\theta}) + \varepsilon_{t,i}^*$ where $\varepsilon_{t,i}^*$ are drawn from the estimated residual distribution

    The parametric approach is preferable when the model is well-specified, as it respects the pricing structure.

    **Step 3: Compute bootstrap replicates.** For each bootstrap sample $b = 1, \ldots, B$:

    1. Generate bootstrap data $\{C^{*(b)}_{t,i}\}$
    2. Calibrate the Heston model to the bootstrap data by minimizing

        $$
        \hat{\theta}^{*(b)} = \arg\min_\theta \sum_{t,i} w_{t,i} [C^{*(b)}_{t,i} - C_i^{\text{Heston}}(\theta)]^2
        $$

    3. Store $\hat{\theta}^{*(b)}$

    **Step 4: Construct confidence region.** From the $B$ bootstrap replicates $\{\hat{\theta}^{*(1)}, \ldots, \hat{\theta}^{*(B)}\}$:

    *Marginal intervals:* For each parameter $\theta_j$, take the $(\alpha/2, 1-\alpha/2)$ quantiles of $\{\hat{\theta}_j^{*(b)}\}$ to form a 95% marginal confidence interval.

    *Joint ellipsoidal region:* Compute the bootstrap covariance $\hat{\Sigma}^* = \frac{1}{B-1}\sum_{b=1}^B (\hat{\theta}^{*(b)} - \bar{\theta}^*)(\hat{\theta}^{*(b)} - \bar{\theta}^*)^\top$ and form

    $$
    \mathcal{C} = \{\theta : (\theta - \hat{\theta})^\top (\hat{\Sigma}^*)^{-1} (\theta - \hat{\theta}) \leq c_\alpha\}
    $$

    where $c_\alpha$ is the $(1-\alpha)$ quantile of $\{(\hat{\theta}^{*(b)} - \hat{\theta})^\top (\hat{\Sigma}^*)^{-1} (\hat{\theta}^{*(b)} - \hat{\theta})\}_{b=1}^B$.

    *Convex hull:* The convex hull of the inner 95% of bootstrap replicates (after removing the 5% most extreme) provides a nonparametric joint region.

    **Computational challenges:**

    1. **Cost per replicate.** Each Heston calibration requires evaluating the characteristic function and performing nonlinear optimization, typically taking seconds to minutes. With $B = 1000$ replicates, total computation is $10^3$--$10^5$ seconds.

    2. **Convergence issues.** Some bootstrap samples may lead to calibration failure (non-convergence, Feller condition violations). A robust implementation must handle these gracefully.

    3. **Mitigation strategies:**
        - Use warm-starting: initialize bootstrap calibration at $\hat{\theta}$
        - Reduce $B$ and use bias-corrected accelerated (BCa) bootstrap for better small-$B$ performance
        - Parallelize: bootstrap replicates are independent and embarrassingly parallel
        - Use fast pricing methods (COS method, FFT) to reduce per-calibration cost
        - Consider the "cheap bootstrap" approximation: $\hat{\theta}^{*(b)} \approx \hat{\theta} - H^{-1} J^\top \delta C^{(b)}$ using a one-step Newton update, avoiding full re-optimization
