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
