# Misspecification vs Estimation Error


## Introduction


In quantitative finance and econometrics, model uncertainty arises from two fundamentally different sources:

1. **Misspecification Error**: The true data-generating process lies outside the considered model class
2. **Estimation Error**: The true model belongs to the model class, but parameters are estimated with finite-sample error

Understanding the distinction between these error sources and their interaction is crucial for:

- Robust model selection
- Proper uncertainty quantification
- Risk management
- Statistical inference under model uncertainty

This chapter provides rigorous mathematical treatment of both error types, their decomposition, and methods for handling their combined effects.

## Mathematical Framework


### 1. Setup and Notation


**Data-Generating Process**: Let $P^*$ denote the true (unknown) probability measure governing observed data $\{X_i\}_{i=1}^n$.

**Model Class**: Consider a parametric family $\mathcal{M} = \{P_{\theta}: \theta \in \Theta\}$ where $\Theta \subseteq \mathbb{R}^d$ is the parameter space.

**Well-Specified Model**: The model is **correctly specified** if:


$$
P^* \in \mathcal{M} \quad \text{i.e., } P^* = P_{\theta^*} \text{ for some } \theta^* \in \Theta
$$



**Misspecified Model**: The model is **misspecified** if:


$$
P^* \notin \mathcal{M}
$$



### 2. Pseudo-True Parameter


Even under misspecification, we can define a best approximation within the model class.

**Definition** (Pseudo-True Parameter): The **pseudo-true parameter** $\theta_0$ is defined as:


$$
\theta_0 = \arg\min_{\theta \in \Theta} D_{\text{KL}}(P^* \| P_{\theta})
$$



where $D_{\text{KL}}(P \| Q)$ is the Kullback-Leibler divergence.

**Alternative Characterizations**:

1. **Maximum Likelihood**: 

   $$
   \theta_0 = \arg\max_{\theta \in \Theta} \mathbb{E}_{P^*}[\log p_{\theta}(X)]
   $$



2. **Minimum Hellinger Distance**:

   $$
   \theta_0 = \arg\min_{\theta \in \Theta} \int \left( \sqrt{p^*} - \sqrt{p_{\theta}} \right)^2
   $$



**Properties**:

- When well-specified: $\theta_0 = \theta^*$
- When misspecified: $\theta_0$ is the "closest" parameter in the KL sense
- $\theta_0$ is uniquely defined under identifiability conditions

### 3. Estimator and Estimation Error


**Maximum Likelihood Estimator (MLE)**:


$$
\hat{\theta}_n = \arg\max_{\theta \in \Theta} \sum_{i=1}^n \log p_{\theta}(X_i)
$$



**Estimation Error**: The deviation between estimator and pseudo-true parameter:


$$
\Delta_{\text{est}} = \hat{\theta}_n - \theta_0
$$



**Asymptotic Distribution**: Under regularity conditions:


$$
\sqrt{n}(\hat{\theta}_n - \theta_0) \xrightarrow{d} \mathcal{N}(0, \Sigma(\theta_0))
$$



where $\Sigma(\theta_0)$ is the asymptotic covariance matrix.

### 4. Misspecification Error


**Approximation Error**: The distance between the pseudo-true model and the truth:


$$
\Delta_{\text{mis}} = D_{\text{KL}}(P^* \| P_{\theta_0})
$$



**Decomposition**: For any $\theta \in \Theta$:


$$
D_{\text{KL}}(P^* \| P_{\theta}) = \underbrace{D_{\text{KL}}(P^* \| P_{\theta_0})}_{\text{Misspecification}} + \underbrace{D_{\text{KL}}(P_{\theta_0} \| P_{\theta})}_{\text{Within-Model}}
$$



This decomposition shows that any parameter $\theta \neq \theta_0$ incurs both misspecification error and within-model error.

## Asymptotic Theory


### 1. Consistency Under Misspecification


**Theorem** (Consistency): Under standard regularity conditions:


$$
\hat{\theta}_n \xrightarrow{p} \theta_0 \quad \text{as } n \to \infty
$$



even when the model is misspecified.

**Proof Sketch**: By the law of large numbers:


$$
\frac{1}{n} \sum_{i=1}^n \log p_{\theta}(X_i) \xrightarrow{p} \mathbb{E}_{P^*}[\log p_{\theta}(X)]
$$



uniformly in $\theta$. The MLE $\hat{\theta}_n$ maximizes the LHS, which converges to the RHS, which is maximized at $\theta_0$ by definition.

**Interpretation**: The MLE consistently estimates the pseudo-true parameter $\theta_0$, not necessarily the true parameter $\theta^*$ (which may not exist in $\mathcal{M}$).

### 2. Asymptotic Normality


**Theorem** (Asymptotic Distribution): Under regularity conditions:


$$
\sqrt{n}(\hat{\theta}_n - \theta_0) \xrightarrow{d} \mathcal{N}(0, H(\theta_0)^{-1} J(\theta_0) H(\theta_0)^{-1})
$$



where:

- **Hessian**: 

  $$
  H(\theta) = -\mathbb{E}_{P^*}\left[ \nabla^2 \log p_{\theta}(X) \right]
  $$


- **Outer Product of Scores** (OPG):

  $$
  J(\theta) = \mathbb{E}_{P^*}\left[ \nabla \log p_{\theta}(X) \nabla \log p_{\theta}(X)^\top \right]
  $$



**Sandwich Formula**: The asymptotic covariance is:


$$
\Sigma(\theta_0) = H(\theta_0)^{-1} J(\theta_0) H(\theta_0)^{-1}
$$



often called the **robust** or **sandwich** covariance matrix.

**Well-Specified Case**: When $P^* = P_{\theta_0}$:


$$
H(\theta_0) = J(\theta_0) = \mathcal{I}(\theta_0)
$$



the Fisher information, and:


$$
\Sigma(\theta_0) = \mathcal{I}(\theta_0)^{-1}
$$



the Cramér-Rao bound.

### 3. Rate of Convergence


**Parametric Rate**: Both estimation error and convergence rate are $O_p(n^{-1/2})$:


$$
\|\hat{\theta}_n - \theta_0\| = O_p(n^{-1/2})
$$



**Misspecification**: The misspecification error $\Delta_{\text{mis}}$ does **not** vanish as $n \to \infty$:


$$
D_{\text{KL}}(P^* \| P_{\theta_0}) = O(1)
$$



**Implication**: For large $n$:

- Estimation error becomes negligible: $O(n^{-1/2})$
- Misspecification error dominates: $O(1)$

## Decomposition of Prediction Error


### 1. Expected Loss Framework


Consider prediction error measured by a loss function $\ell(y, \hat{y})$.

**Expected Loss**: For predictor $\hat{f}_n$ based on $n$ samples:


$$
R(\hat{f}_n) = \mathbb{E}_{P^*}[\ell(Y, \hat{f}_n(X))]
$$



**Decomposition**: We can write:


$$
R(\hat{f}_n) = \underbrace{R(f^*)}_{\text{Bayes risk}} + \underbrace{[R(f_{\theta_0}) - R(f^*)]}_{\text{Approximation (Misspecification)}} + \underbrace{[R(\hat{f}_n) - R(f_{\theta_0})]}_{\text{Estimation}}
$$



where:

- $f^*$ is the Bayes-optimal predictor under $P^*$
- $f_{\theta_0}$ is the best predictor in model class $\mathcal{M}$
- $\hat{f}_n$ is the estimated predictor

### 2. Bias-Variance-Misspecification Tradeoff


For squared error loss $\ell(y, \hat{y}) = (y - \hat{y})^2$:

**Mean Squared Error**:


$$
\text{MSE}(\hat{f}_n) = \mathbb{E}_{P^*}[(Y - \hat{f}_n(X))^2]
$$



**Classical Decomposition** (Well-Specified):


$$
\text{MSE}(\hat{f}_n) = \underbrace{\mathbb{E}[(\mathbb{E}[\hat{f}_n] - f^*)^2]}_{\text{Bias}^2} + \underbrace{\mathbb{E}[(\hat{f}_n - \mathbb{E}[\hat{f}_n])^2]}_{\text{Variance}}
$$



**Extended Decomposition** (Misspecified):


$$
\text{MSE}(\hat{f}_n) = \underbrace{(f_{\theta_0} - f^*)^2}_{\text{Misspecification}^2} + \underbrace{(\mathbb{E}[\hat{f}_n] - f_{\theta_0})^2}_{\text{Bias}^2} + \underbrace{\text{Var}(\hat{f}_n)}_{\text{Variance}}
$$



**Interpretation**:

1. **Misspecification**: Cannot be reduced by collecting more data
2. **Bias**: Decreases with more flexible models
3. **Variance**: Decreases with more data but increases with model complexity

## Model Selection Under Misspecification


### 1. Information Criteria


Information criteria balance goodness-of-fit against model complexity.

### 2. Akaike Information Criterion (AIC)


**Definition**:


$$
\text{AIC} = -2 \sum_{i=1}^n \log p_{\hat{\theta}_n}(X_i) + 2d
$$



where $d = \dim(\Theta)$ is the number of parameters.

**Asymptotic Justification**: AIC estimates:


$$
-2n \cdot \mathbb{E}_{P^*}[\log p_{\hat{\theta}_n}(X)] + 2d \approx -2n \cdot \mathbb{E}_{P^*}[\log p_{\theta_0}(X)] + \text{bias correction}
$$



**Key Property**: AIC is consistent for selecting the model that minimizes KL divergence to $P^*$, even under misspecification.

### 3. Bayesian Information Criterion (BIC)


**Definition**:


$$
\text{BIC} = -2 \sum_{i=1}^n \log p_{\hat{\theta}_n}(X_i) + d \log n
$$



**Asymptotic Property**: BIC is consistent for model selection when the true model is in the candidate set (well-specified case).

**Under Misspecification**: BIC tends to select simpler models than AIC due to larger penalty ($\log n$ vs $2$).

### 4. Takeuchi Information Criterion (TIC)


**Robust Variant** accounting for misspecification:


$$
\text{TIC} = -2 \sum_{i=1}^n \log p_{\hat{\theta}_n}(X_i) + 2 \text{tr}(H^{-1} J)
$$



where $H$ and $J$ are estimates of $H(\theta_0)$ and $J(\theta_0)$.

**Interpretation**: The trace term $\text{tr}(H^{-1} J)$ reduces to $d$ when well-specified, generalizing AIC.

### 5. Cross-Validation


Cross-validation directly estimates prediction error without assuming correct specification.

**$K$-Fold Cross-Validation**:


$$
\text{CV} = \frac{1}{K} \sum_{k=1}^K \sum_{i \in \mathcal{D}_k} \ell(Y_i, \hat{f}_{-k}(X_i))
$$



where $\hat{f}_{-k}$ is trained on all data except fold $k$.

**Asymptotic Behavior**:


$$
\text{CV} \approx \mathbb{E}_{P^*}[\ell(Y, \hat{f}_n(X))] + O_p(n^{-1})
$$



**Advantages**:

- Valid under misspecification
- No assumption about model form
- Directly relevant for prediction

**Disadvantages**:

- Computationally intensive
- High variance for small $n$

### 6. Model Averaging


Instead of selecting a single model, average predictions across models.

**Weighted Average**:


$$
\hat{f}_{\text{avg}} = \sum_{m=1}^M w_m \hat{f}_m
$$



**Optimal Weights**: Minimize expected loss:


$$
w^* = \arg\min_w \mathbb{E}_{P^*}[\ell(Y, \sum_{m=1}^M w_m \hat{f}_m(X))]
$$



subject to $\sum_m w_m = 1$, $w_m \geq 0$.

**Bayesian Model Averaging (BMA)**:


$$
w_m^{\text{BMA}} = \frac{p(\mathcal{D} | \mathcal{M}_m) p(\mathcal{M}_m)}{\sum_{j=1}^M p(\mathcal{D} | \mathcal{M}_j) p(\mathcal{M}_j)}
$$



**Under Misspecification**: BMA may not be optimal; frequentist stacking often performs better.

## Inference Under Misspecification


### 1. Hypothesis Testing


**Null Hypothesis**: $H_0: \theta = \theta_0$ (pseudo-true value).

**Wald Test Statistic**:


$$
W_n = n(\hat{\theta}_n - \theta_0)^\top \hat{\Sigma}^{-1} (\hat{\theta}_n - \theta_0)
$$



**Asymptotic Distribution**:


$$
W_n \xrightarrow{d} \chi^2_d \quad \text{under } H_0
$$



using the sandwich estimator $\hat{\Sigma}$.

**Critical Issue**: Standard tests assume well-specification. Using incorrect covariance (e.g., $\mathcal{I}(\theta_0)^{-1}$ instead of sandwich) leads to:

- Incorrect size
- Invalid p-values
- Misleading inference

### 2. Confidence Intervals


**Standard CI** (assuming well-specification):


$$
\hat{\theta}_n \pm z_{\alpha/2} \sqrt{\frac{\mathcal{I}(\hat{\theta}_n)^{-1}}{n}}
$$



**Robust CI** (allowing misspecification):


$$
\hat{\theta}_n \pm z_{\alpha/2} \sqrt{\frac{\hat{\Sigma}}{n}}
$$



where $\hat{\Sigma}$ is the sandwich estimator.

**Coverage**: 

- Standard CI: May have coverage $< 1-\alpha$ under misspecification
- Robust CI: Maintains nominal coverage asymptotically

### 3. Quasi-Likelihood Methods


**Quasi-Likelihood**: Specify only first two moments:


$$
\mathbb{E}[Y|X] = \mu(X; \theta), \quad \text{Var}(Y|X) = V(\mu(X; \theta))
$$



**Estimating Equation**:


$$
\sum_{i=1}^n \frac{\partial \mu(X_i; \theta)}{\partial \theta} \frac{Y_i - \mu(X_i; \theta)}{V(\mu(X_i; \theta))} = 0
$$



**Advantage**: Robust to distributional misspecification; only requires correct specification of mean and variance functions.

**Consistency**: $\hat{\theta}_n \to \theta_0$ where:


$$
\mathbb{E}_{P^*}\left[ \frac{\partial \mu(X; \theta_0)}{\partial \theta} \frac{Y - \mu(X; \theta_0)}{V(\mu(X; \theta_0))} \right] = 0
$$



## Misspecification Tests


### 1. Moment Tests


**Idea**: Check if moments implied by the model match empirical moments.

**Test Statistic**: For moment conditions $\mathbb{E}[g(X, \theta)] = 0$:


$$
Q_n = n \cdot \bar{g}_n(\hat{\theta}_n)^\top W \bar{g}_n(\hat{\theta}_n)
$$



where $\bar{g}_n(\theta) = n^{-1} \sum_{i=1}^n g(X_i, \theta)$ and $W$ is a weight matrix.

**Asymptotic Distribution**:


$$
Q_n \xrightarrow{d} \chi^2_r \quad \text{under correct specification}
$$



where $r$ is the number of overidentifying restrictions.

**Rejection**: Large $Q_n$ provides evidence of misspecification.

### 2. Hausman Test


**Setup**: Two estimators $\hat{\theta}_1$ and $\hat{\theta}_2$ where:

- $\hat{\theta}_1$ is consistent under both $H_0$ and $H_1$ but inefficient under $H_0$
- $\hat{\theta}_2$ is consistent and efficient under $H_0$ but inconsistent under $H_1$

**Test Statistic**:


$$
H = (\hat{\theta}_1 - \hat{\theta}_2)^\top [\text{Var}(\hat{\theta}_1 - \hat{\theta}_2)]^{-1} (\hat{\theta}_1 - \hat{\theta}_2)
$$



**Asymptotic Distribution**:


$$
H \xrightarrow{d} \chi^2_d \quad \text{under } H_0
$$



**Application**: Test endogeneity, omitted variables, or other forms of misspecification.

### 3. Omnibus Tests


**Goodness-of-Fit Tests**: 

1. **Kolmogorov-Smirnov**:

   $$
   D_n = \sup_x |\hat{F}_n(x) - F_{\theta_0}(x)|
   $$



2. **Cramér-von Mises**:

   $$
   W_n^2 = n \int_{-\infty}^{\infty} [\hat{F}_n(x) - F_{\theta_0}(x)]^2 dF_{\theta_0}(x)
   $$



3. **Anderson-Darling**:

   $$
   A_n^2 = n \int_{-\infty}^{\infty} \frac{[\hat{F}_n(x) - F_{\theta_0}(x)]^2}{F_{\theta_0}(x)[1 - F_{\theta_0}(x)]} dF_{\theta_0}(x)
   $$



**Power**: These tests can detect various forms of misspecification but may have low power against specific alternatives.

## Robustness to Misspecification


### 1. Robust Estimators


**M-Estimators**: Minimize a robust loss function:


$$
\hat{\theta}_n = \arg\min_{\theta} \sum_{i=1}^n \rho(X_i, \theta)
$$



where $\rho$ is chosen to downweight outliers.

**Example** (Huber Loss): For regression:


$$
\rho_{\delta}(r) = \begin{cases}
\frac{1}{2} r^2 & |r| \leq \delta \\
\delta |r| - \frac{1}{2} \delta^2 & |r| > \delta
\end{cases}
$$



**Breakdown Point**: Fraction of contamination an estimator can handle before breaking down.

### 2. Influence Functions


**Influence Function**: Measures sensitivity to infinitesimal contamination:


$$
\text{IF}(x; T, P) = \lim_{\varepsilon \to 0} \frac{T((1-\varepsilon)P + \varepsilon \delta_x) - T(P)}{\varepsilon}
$$



where $T$ is a statistical functional and $\delta_x$ is a point mass at $x$.

**Gross Error Sensitivity**:


$$
\gamma^* = \sup_x |\text{IF}(x; T, P)|
$$



**Interpretation**: Smaller $\gamma^*$ indicates greater robustness to outliers.

**For MLE**: Influence function is unbounded, making it sensitive to outliers and misspecification.

### 3. Empirical Likelihood


**Idea**: Nonparametric approach that assigns probabilities $p_i$ to observations.

**Optimization**:


$$
\max_{p_1, \ldots, p_n} \prod_{i=1}^n p_i \quad \text{subject to} \quad \sum_{i=1}^n p_i = 1, \quad \sum_{i=1}^n p_i g(X_i, \theta) = 0
$$



**Advantage**: Does not require specifying a parametric likelihood; robust to distributional misspecification.

**Empirical Likelihood Ratio**:


$$
\text{ELR}(\theta) = \max_{p_i} \prod_{i=1}^n (n p_i)
$$



subject to moment constraints.

**Asymptotic Distribution**:


$$
-2 \log \text{ELR}(\theta_0) \xrightarrow{d} \chi^2_r
$$



## Applications to Quantitative Finance


### 1. Option Pricing Under Misspecification


**Setup**: True stock dynamics unknown; use Black-Scholes as working model.

**Black-Scholes Model**:


$$
dS_t = \mu S_t \, dt + \sigma S_t \, dW_t
$$



**True Dynamics** (e.g., with jumps):


$$
dS_t = \mu S_t \, dt + \sigma S_t \, dW_t + S_{t-} \, dJ_t
$$



where $J_t$ is a jump process.

**Pricing Error**: 


$$
\text{Error} = |V_{\text{BS}}(S_0, K, \sigma) - V_{\text{true}}(S_0, K)|
$$



**Components**:

1. **Misspecification**: Ignoring jumps creates systematic bias
2. **Estimation Error**: Volatility $\sigma$ estimated from data
3. **Interaction**: Estimated $\sigma$ may partially compensate for model misspecification

### 2. Risk Management


**Value-at-Risk (VaR)**: 


$$
\text{VaR}_{\alpha} = \inf\{v: P^*(L \leq v) \geq 1 - \alpha\}
$$



**Under Misspecified Model**: Using $P_{\theta_0}$ instead of $P^*$:


$$
\text{VaR}_{\alpha}^{\text{model}} = \inf\{v: P_{\theta_0}(L \leq v) \geq 1 - \alpha\}
$$



**Model Risk**: 


$$
\Delta_{\text{VaR}} = \text{VaR}_{\alpha}^{\text{model}} - \text{VaR}_{\alpha}
$$



**Backtesting**: Check if actual violations match predicted:


$$
\text{Violation rate} = \frac{1}{T} \sum_{t=1}^T \mathbb{1}\{L_t > \text{VaR}_{\alpha, t}^{\text{model}}\}
$$



Should be close to $\alpha$ if model is well-specified.

### 3. Portfolio Optimization


**Mean-Variance Problem**:


$$
\max_w \left\{ w^\top \mu - \frac{\lambda}{2} w^\top \Sigma w \right\}
$$



**Parameter Estimation**:

- $\hat{\mu}$ estimated from sample mean
- $\hat{\Sigma}$ estimated from sample covariance

**Estimation Error Impact**: 


$$
\text{Loss} = (w^*_{\hat{\mu}, \hat{\Sigma}} - w^*_{\mu, \Sigma})^\top \Sigma (w^*_{\hat{\mu}, \hat{\Sigma}} - w^*_{\mu, \Sigma})
$$



**Misspecification**: Returns may not be i.i.d. normal:

- Fat tails
- Time-varying moments
- Dependencies

**Robust Approach**: Use shrinkage estimators or robust covariance estimators to reduce impact of both estimation error and misspecification.

### 4. Factor Models


**Model**: Returns generated by factors:


$$
R_i = \alpha_i + \beta_i^\top F + \varepsilon_i
$$



**Misspecification**: 

- Missing factors
- Nonlinear factor loadings
- Time-varying betas

**Estimation Error**: 

- Estimated $\hat{\beta}_i$ from regression
- Standard error: $O(n^{-1/2})$

**Joint Impact**: 


$$
\mathbb{E}[(R_i - \hat{\alpha}_i - \hat{\beta}_i^\top F)^2] = \underbrace{\mathbb{E}[\varepsilon_i^2]}_{\text{Idiosyncratic}} + \underbrace{\beta_i^\top \text{Cov}(F) \beta_i}_{\text{Factor}} + \underbrace{O(n^{-1})}_{\text{Estimation}}
$$



when well-specified. Under misspecification, first term includes structural error.

## Advanced Theoretical Results


### 1. Semiparametric Efficiency


**Semiparametric Model**: Parametric component $\theta$ and infinite-dimensional nuisance component $\eta$.

**Efficient Score**: The orthogonal component to the nuisance tangent space:


$$
\tilde{\ell}(\theta, \eta) = \ell(\theta, \eta) - \Pi[\ell(\theta, \eta) | \mathcal{T}_{\eta}]
$$



**Efficient Influence Function**: 


$$
\text{IF}_{\text{eff}}(x) = \mathcal{I}(\theta)^{-1} \tilde{\ell}(\theta, \eta)(x)
$$



**Semiparametric Efficiency Bound**:


$$
\text{Var}(\hat{\theta}) \geq \frac{1}{n \cdot \mathcal{I}_{\text{semi}}(\theta)}
$$



**Under Misspecification**: Efficiency bounds still apply, but target is pseudo-true $\theta_0$ rather than true $\theta^*$.

### 2. Double Robustness


**Setup**: Two working models:

1. Outcome regression: $m(X; \alpha)$
2. Propensity score: $\pi(X; \beta)$

**Doubly Robust Estimator**:


$$
\hat{\tau} = \frac{1}{n} \sum_{i=1}^n \left[ \frac{Y_i A_i}{\pi(X_i; \hat{\beta})} - \frac{m(X_i; \hat{\alpha})(A_i - \pi(X_i; \hat{\beta}))}{\pi(X_i; \hat{\beta})} \right]
$$



**Property**: $\hat{\tau}$ is consistent if **either** (not necessarily both):

- $m(X; \alpha)$ is correctly specified, **or**
- $\pi(X; \beta)$ is correctly specified

**Interpretation**: Provides insurance against misspecification of one component.

### 3. High-Dimensional Asymptotics


**Setup**: Dimension $d = d_n \to \infty$ as $n \to \infty$.

**Regime**: $d/n \to \kappa \in (0, 1)$ (proportional asymptotics).

**Estimation Error**: In high dimensions:


$$
\|\hat{\theta}_n - \theta_0\|^2 = O_p\left(\frac{d}{n}\right)
$$



rather than $O_p(n^{-1})$ in fixed-dimensional case.

**Misspecification**: Can be exacerbated in high dimensions:

- More parameters to estimate
- Greater potential for overfitting
- Model selection more difficult

**Regularization**: Methods like LASSO add penalty to control both estimation error and effective model complexity:


$$
\hat{\theta}_{\lambda} = \arg\min_{\theta} \left\{ \sum_{i=1}^n (Y_i - X_i^\top \theta)^2 + \lambda \|\theta\|_1 \right\}
$$



## Practical Guidelines


### 1. Detection Strategy


**Step 1**: Diagnostic Checks

- Plot residuals vs. fitted values
- Q-Q plots for normality
- ACF plots for independence

**Step 2**: Formal Tests

- Run omnibus goodness-of-fit tests
- Check moment conditions
- Perform Hausman-type specification tests

**Step 3**: Cross-Validation

- Compare in-sample vs. out-of-sample performance
- Large discrepancy suggests overfitting or misspecification

### 2. Remedial Measures


**When Misspecification Detected**:

1. **Expand Model Class**: Add more flexible features
   - Interaction terms
   - Nonlinear transformations
   - Regime-switching components

2. **Use Robust Methods**: 
   - Sandwich covariance for inference
   - M-estimators for estimation
   - Empirical likelihood

3. **Model Averaging**: Combine multiple models to hedge misspecification risk

4. **Regularization**: Add penalties to prevent overfitting while allowing for misspecification

### 3. Reporting Standards


**Best Practices**:

1. **Always report sandwich standard errors** when model specification uncertain

2. **Conduct sensitivity analysis**: Report results under multiple model specifications

3. **Validate out-of-sample**: Use holdout data or cross-validation

4. **Document assumptions**: Be explicit about modeling choices and their implications

5. **Report information criteria**: AIC, BIC, or TIC to facilitate model comparison

### 4. Balancing Act


**Trade-off Triangle**:

```
         Complexity
            /\
           /  \
          /    \
         /      \
        /        \
       /          \
      /            \
     /______________\
Misspecification  Estimation
    Error          Error
```

**Optimal Model**: Minimizes total error:


$$
\text{Total Error} = \text{Misspecification Error} + \text{Estimation Error}
$$



**Guidelines**:

- **Small $n$**: Use simpler models to reduce estimation error
- **Large $n$**: Can afford more complex models; focus on reducing misspecification
- **High $d$**: Regularization crucial to control estimation error

## Summary and Key Insights


### 1. Fundamental Distinctions


1. **Nature of Error**:
   - Misspecification: Structural, does not vanish with more data
   - Estimation: Statistical, decreases at rate $O(n^{-1/2})$

2. **Asymptotic Behavior**:
   - As $n \to \infty$: Estimation error → 0, Misspecification error persists
   - Dominance switches from estimation (small $n$) to misspecification (large $n$)

3. **Inference**:
   - Misspecification requires sandwich covariance
   - Standard errors based on Fisher information are invalid under misspecification

### 2. Practical Implications


1. **Model Selection**: Use information criteria (AIC/BIC) or cross-validation that account for both error sources

2. **Uncertainty Quantification**: Sandwich estimators provide valid inference under misspecification

3. **Robustness**: M-estimators and quasi-likelihood methods offer protection

4. **High Dimensions**: Regularization helps control estimation error; model selection critical for misspecification

### 3. Research Frontiers


1. **Optimal Model Averaging**: Theory for optimal weights under joint misspecification and estimation error

2. **Adaptive Inference**: Methods that automatically adjust for detected misspecification

3. **Deep Learning**: Understanding misspecification vs. estimation error in neural networks

4. **Causal Inference**: Double robustness and related techniques for handling model uncertainty

The interplay between misspecification and estimation error is central to statistical modeling. A deep understanding of both error sources and their interaction is essential for robust quantitative finance applications, from derivative pricing to risk management to portfolio optimization.

---

## Exercises

**Exercise 1.** Consider a true data-generating process $P^*$ that is a mixture of two normals: $P^* = 0.7 \cdot N(0.05, 0.04) + 0.3 \cdot N(-0.10, 0.09)$. A practitioner fits a single Gaussian model $P_\theta = N(\mu, \sigma^2)$. Compute the pseudo-true parameter $\theta^* = \arg\min_\theta D_{\text{KL}}(P^* \| P_\theta)$ and the misspecification error. Explain why the fitted model fails to capture the left tail of $P^*$.

??? success "Solution to Exercise 1"

    The true distribution is $P^* = 0.7 \cdot N(0.05, 0.04) + 0.3 \cdot N(-0.10, 0.09)$.

    **Step 1: Compute the moments of $P^*$.** The mean is:

    $$
    \mu^* = 0.7 \times 0.05 + 0.3 \times (-0.10) = 0.035 - 0.030 = 0.005
    $$

    The second moment is:

    $$
    \mathbb{E}[X^2] = 0.7(0.04 + 0.05^2) + 0.3(0.09 + 0.10^2) = 0.7(0.0425) + 0.3(0.10) = 0.02975 + 0.03 = 0.05975
    $$

    So the variance is $\sigma^{*2} = 0.05975 - 0.005^2 = 0.059725$.

    **Step 2: Find the pseudo-true parameter.** For a Gaussian model $P_\theta = N(\mu, \sigma^2)$, the KL divergence $D_{\text{KL}}(P^* \| P_\theta)$ is minimized when $P_\theta$ matches the first two moments of $P^*$ (this is a well-known property of the Gaussian family as the maximum entropy distribution for given mean and variance).

    The pseudo-true parameters are:

    $$
    \mu_0 = \mu^* = 0.005, \quad \sigma_0^2 = \sigma^{*2} = 0.059725
    $$

    **Step 3: Compute the misspecification error.** The KL divergence is:

    $$
    D_{\text{KL}}(P^* \| P_{\theta_0}) = \int p^*(x) \log\frac{p^*(x)}{p_{\theta_0}(x)} \, dx = -H(P^*) - \int p^*(x) \log p_{\theta_0}(x) \, dx
    $$

    Since $P_{\theta_0} = N(\mu_0, \sigma_0^2)$ matches the mean and variance of $P^*$:

    $$
    \int p^*(x) \log p_{\theta_0}(x) \, dx = -\frac{1}{2}\log(2\pi\sigma_0^2) - \frac{1}{2\sigma_0^2}\mathbb{E}_{P^*}[(X - \mu_0)^2] = -\frac{1}{2}\log(2\pi\sigma_0^2) - \frac{1}{2}
    $$

    Therefore $D_{\text{KL}}(P^* \| P_{\theta_0}) = -H(P^*) + \frac{1}{2}\log(2\pi e \sigma_0^2)$, where $H(P^*)$ is the differential entropy of the mixture.

    The entropy of a Gaussian with variance $\sigma_0^2$ is $H_{\text{Gauss}} = \frac{1}{2}\log(2\pi e \sigma_0^2)$, and since a Gaussian maximizes entropy for given variance, we have $H(P^*) \leq H_{\text{Gauss}}$, so $D_{\text{KL}}(P^* \| P_{\theta_0}) \geq 0$. The misspecification error is strictly positive because $P^*$ is bimodal while $P_{\theta_0}$ is unimodal.

    **Step 4: Left tail failure.** The left tail of $P^*$ is heavier than that of $P_{\theta_0}$ because the mixture component $N(-0.10, 0.09)$ contributes significant mass in the far left. The fitted Gaussian, while matching the overall variance, distributes its tails symmetrically. In particular:

    $$
    P^*(X < -0.5) \gg P_{\theta_0}(X < -0.5)
    $$

    This is because the mixture's second component (with mean $-0.10$ and standard deviation $0.3$) places substantial probability at extreme negative values. The single Gaussian cannot capture this asymmetric, heavy-tailed structure, leading to systematic underestimation of left-tail risk.

---

**Exercise 2.** For a correctly specified model $P^* = P_{\theta_0}$ with $n = 100$ observations, the MLE $\hat{\theta}_n$ has asymptotic variance $I(\theta_0)^{-1}/n$. Compute the estimation error contribution to the total pricing error $|V(\hat{\theta}_n) - V(\theta_0)|$ using the delta method when $V(\theta) = \text{BS}(S_0, K, \sigma(\theta), T)$ is a Black-Scholes call price. Express the result in terms of the vega and the Fisher information.

??? success "Solution to Exercise 2"

    **Setup**: The model is correctly specified, so $P^* = P_{\theta_0}$, $\hat{\theta}_n$ is the MLE with $n = 100$, and $V(\theta) = \text{BS}(S_0, K, \sigma(\theta), T)$ is a Black-Scholes call price.

    **Delta method**: For a smooth function $V(\theta)$ of the parameter, the pricing error satisfies:

    $$
    V(\hat{\theta}_n) - V(\theta_0) \approx \nabla_\theta V(\theta_0)^\top (\hat{\theta}_n - \theta_0)
    $$

    The variance of this pricing error is:

    $$
    \text{Var}(V(\hat{\theta}_n) - V(\theta_0)) \approx \nabla_\theta V(\theta_0)^\top \text{Var}(\hat{\theta}_n) \nabla_\theta V(\theta_0)
    $$

    **Single-parameter case ($\theta = \sigma$)**: If the only uncertain parameter is volatility, then $\nabla_\sigma V = \mathcal{V}$ (the Black-Scholes vega), and in the well-specified case:

    $$
    \text{Var}(\hat{\sigma}_n) = \frac{1}{n \cdot I(\sigma_0)}
    $$

    where $I(\sigma_0)$ is the Fisher information for the volatility parameter.

    Therefore the estimation error contribution to the pricing error is:

    $$
    |V(\hat{\sigma}_n) - V(\sigma_0)| \approx |\mathcal{V}(\sigma_0)| \cdot |\hat{\sigma}_n - \sigma_0|
    $$

    with standard deviation:

    $$
    \text{sd}(V(\hat{\sigma}_n) - V(\sigma_0)) \approx \frac{|\mathcal{V}(\sigma_0)|}{\sqrt{n \cdot I(\sigma_0)}}
    $$

    For $n = 100$:

    $$
    \text{sd}(\text{pricing error}) = \frac{|\mathcal{V}(\sigma_0)|}{10 \sqrt{I(\sigma_0)}}
    $$

    **Interpretation**: The pricing error is proportional to the vega (sensitivity of the option price to volatility) and inversely proportional to $\sqrt{n I(\sigma_0)}$. Options with high vega (e.g., ATM options with long maturity) are most sensitive to estimation error. The Fisher information $I(\sigma_0)$ captures how informative the data is about $\sigma$: higher $I(\sigma_0)$ means more precise estimation and smaller pricing error.

    **Multi-parameter extension**: If $\theta = (\mu, \sigma)^\top$, the pricing error variance is:

    $$
    \text{Var}(V(\hat{\theta}_n) - V(\theta_0)) = \frac{1}{n} \nabla_\theta V(\theta_0)^\top I(\theta_0)^{-1} \nabla_\theta V(\theta_0)
    $$

    Since the Black-Scholes call price under the risk-neutral measure does not depend on $\mu$, we have $\partial V / \partial \mu = 0$ in the risk-neutral framework, and the result reduces to the vega-based formula above.

---

**Exercise 3.** Explain the decomposition of total model risk into misspecification and estimation components:

$$
\text{Total Error} = \underbrace{|V(\theta^*) - V^*|}_{\text{misspecification}} + \underbrace{|V(\hat{\theta}_n) - V(\theta^*)|}_{\text{estimation}}
$$

In which regime (small $n$ vs. large $n$) does each term dominate? Illustrate with a concrete example of fitting a geometric Brownian motion to data with stochastic volatility.

??? success "Solution to Exercise 3"

    **Decomposition**: The total model risk in pricing a derivative $V$ is:

    $$
    |V(\hat{\theta}_n) - V^*| \leq \underbrace{|V(\theta^*) - V^*|}_{\text{misspecification}} + \underbrace{|V(\hat{\theta}_n) - V(\theta^*)|}_{\text{estimation}}
    $$

    where $V^*$ is the true price, $\theta^*$ is the pseudo-true parameter, and $\hat{\theta}_n$ is the MLE.

    **Asymptotic behavior**:

    - **Misspecification error** $|V(\theta^*) - V^*| = O(1)$: This is a fixed bias that does not vanish with sample size. It reflects the structural inability of the model to capture the true dynamics.

    - **Estimation error** $|V(\hat{\theta}_n) - V(\theta^*)| = O_p(n^{-1/2})$: By the delta method and asymptotic normality of the MLE, this vanishes as $n \to \infty$.

    **Regime analysis**:

    - **Small $n$**: Estimation error dominates. With few observations, parameter estimates are noisy, and $|V(\hat{\theta}_n) - V(\theta^*)|$ is large. The misspecification error may be relatively small in comparison. Using a simpler model (lower misspecification within a simpler class, or equivalently, less estimation error) may be preferable.

    - **Large $n$**: Misspecification error dominates. The estimation error shrinks to zero, but the structural bias remains. Increasing sample size does not help reduce total error; only improving the model specification can help.

    **Concrete example: GBM fitted to Heston data.** Suppose the true dynamics follow the Heston model:

    $$
    dS_t = \mu S_t \, dt + \sqrt{v_t} S_t \, dW_t^1, \quad dv_t = \kappa(\bar{v} - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^2
    $$

    and we fit a GBM: $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$ (constant volatility).

    The pseudo-true $\sigma^*$ is essentially the average integrated volatility: $\sigma^{*2} \approx \bar{v}$. The misspecification error arises because:

    1. The GBM cannot produce the implied volatility smile (different strikes are mispriced systematically).
    2. For an OTM put, the GBM underestimates the true price because it misses the fat left tail generated by stochastic volatility and leverage effect ($\rho < 0$).

    With $n = 50$ daily returns, estimation error in $\hat{\sigma}$ might be $\pm 5\%$, leading to pricing errors of order $\mathcal{V} \times 0.05$. With $n = 5000$, estimation error drops to $\pm 0.5\%$, but the misspecification bias (e.g., 10-15% for deep OTM puts) persists.

---

**Exercise 4.** The sandwich (Huber-White) variance estimator provides valid standard errors under model misspecification. For a quasi-MLE $\hat{\theta}$, the sandwich variance is $\hat{V} = A^{-1} B (A^{-1})^\top$ where $A = -\frac{1}{n}\sum_{i=1}^n \nabla^2 \ell_i(\hat{\theta})$ and $B = \frac{1}{n}\sum_{i=1}^n \nabla \ell_i(\hat{\theta}) \nabla \ell_i(\hat{\theta})^\top$. Explain why $A \neq B$ indicates misspecification and how this affects confidence intervals compared to the standard MLE variance $A^{-1}/n$.

??? success "Solution to Exercise 4"

    **Sandwich estimator**: The sandwich (Huber-White) variance is:

    $$
    \hat{V} = A^{-1} B (A^{-1})^\top
    $$

    where:

    $$
    A = -\frac{1}{n}\sum_{i=1}^n \nabla^2 \ell_i(\hat{\theta}), \quad B = \frac{1}{n}\sum_{i=1}^n \nabla \ell_i(\hat{\theta}) \nabla \ell_i(\hat{\theta})^\top
    $$

    **Why $A \neq B$ indicates misspecification**: Under correct specification, the information matrix equality holds:

    $$
    -\mathbb{E}[\nabla^2 \ell(\theta_0)] = \mathbb{E}[\nabla \ell(\theta_0) \nabla \ell(\theta_0)^\top]
    $$

    This is because $\mathbb{E}[\nabla \ell] = 0$ under the true model, and differentiating this identity gives $\mathbb{E}[\nabla^2 \ell] + \mathbb{E}[\nabla \ell \nabla \ell^\top] = 0$. So $A = B$ in population when well-specified.

    When misspecified, the score $\nabla \ell(\theta_0)$ does not integrate to zero under $P^*$ in the same way, and the second Bartlett identity fails. Therefore $A \neq B$, and the discrepancy $\|A - B\|$ is a measure of the degree of misspecification.

    **Impact on confidence intervals**: The standard MLE variance uses $A^{-1}/n$ (equivalent to the inverse Fisher information). The correct asymptotic variance under misspecification is $A^{-1}BA^{-1}/n$.

    - If $B > A$ (in the matrix ordering sense), then $A^{-1}BA^{-1} > A^{-1}$, meaning the standard CI is **too narrow**. This leads to **under-coverage**: the nominal 95% CI may have actual coverage well below 95%, giving false confidence in the estimates.

    - If $B < A$, the standard CI is too wide (conservative), which is less dangerous but still inefficient.

    In practice, misspecification typically increases variance relative to the well-specified case, so standard CIs tend to be anti-conservative. The sandwich estimator corrects this by using the empirically observed score variability rather than the theoretically expected variability under the assumed model.

---

**Exercise 5.** A modeler compares Black-Scholes (1 parameter: $\sigma$) against Heston (5 parameters) for pricing a set of 20 vanilla options. Using AIC, derive the penalty for each model and explain when the simpler Black-Scholes model might be preferred despite higher in-sample calibration error. How does this relate to the bias-variance trade-off?

??? success "Solution to Exercise 5"

    **AIC for Black-Scholes (BS)**: With 1 parameter ($d_{\text{BS}} = 1$), fitting 20 options:

    $$
    \text{AIC}_{\text{BS}} = -2\sum_{i=1}^{20} \log p_{\hat{\sigma}}(V_i^{\text{obs}}) + 2 \times 1
    $$

    The penalty term is $2d = 2$.

    **AIC for Heston**: With 5 parameters ($d_H = 5$: $v_0, \kappa, \bar{v}, \xi, \rho$):

    $$
    \text{AIC}_H = -2\sum_{i=1}^{20} \log p_{\hat{\theta}_H}(V_i^{\text{obs}}) + 2 \times 5
    $$

    The penalty term is $2d = 10$.

    **When BS might be preferred**: The AIC difference is:

    $$
    \text{AIC}_{\text{BS}} - \text{AIC}_H = \underbrace{-2(\mathcal{L}_{\text{BS}} - \mathcal{L}_H)}_{\text{fit difference}} + \underbrace{(2 - 10)}_{\text{penalty difference}}
    $$

    BS is preferred (lower AIC) when $\text{AIC}_{\text{BS}} < \text{AIC}_H$, i.e.:

    $$
    -2(\mathcal{L}_{\text{BS}} - \mathcal{L}_H) < 8
    $$

    $$
    \mathcal{L}_H - \mathcal{L}_{\text{BS}} < 4
    $$

    This occurs when the Heston model's improvement in log-likelihood over BS is less than 4. With only 20 options, Heston's 4 extra parameters may not sufficiently improve the fit to justify the complexity penalty.

    **Connection to bias-variance trade-off**:

    - **Bias (misspecification)**: BS has higher bias since it cannot capture the volatility smile. Heston has lower bias as it models stochastic volatility.

    - **Variance (estimation error)**: BS has lower estimation variance since it has only 1 parameter estimated from 20 data points. Heston has higher variance since 5 parameters must be estimated from the same 20 data points, with a ratio of $d/n = 5/20 = 0.25$ (high).

    - **Total error**: $\text{MSE} = \text{Bias}^2 + \text{Variance}$. For small datasets ($n = 20$), the variance reduction from using BS may outweigh its bias increase, making the simpler model preferable. AIC formalizes this trade-off through the penalty $2d$.

    This is why, in practice, traders sometimes use Black-Scholes with a volatility smile adjustment rather than calibrating a full stochastic volatility model when the dataset is small.

---

**Exercise 6.** Consider the White (1982) information matrix test for misspecification. The null hypothesis is $H_0: A = B$ (where $A$ and $B$ are defined as in Exercise 4). Describe how to implement this test for a GARCH(1,1) model fitted to daily returns, and interpret rejection of $H_0$ in terms of what aspects of the return distribution the GARCH model fails to capture.

??? success "Solution to Exercise 6"

    **White's information matrix test**: The null hypothesis is $H_0: A(\theta_0) = B(\theta_0)$, where:

    $$
    A(\theta_0) = -\mathbb{E}_{P^*}[\nabla^2 \ell(\theta_0)], \quad B(\theta_0) = \mathbb{E}_{P^*}[\nabla \ell(\theta_0) \nabla \ell(\theta_0)^\top]
    $$

    Under correct specification, $A = B$ (the information matrix equality).

    **Implementation for GARCH(1,1)**: The GARCH(1,1) model is:

    $$
    r_t = \mu + \varepsilon_t, \quad \varepsilon_t = \sigma_t z_t, \quad \sigma_t^2 = \omega + \alpha \varepsilon_{t-1}^2 + \beta \sigma_{t-1}^2
    $$

    with parameters $\theta = (\mu, \omega, \alpha, \beta)^\top$ and $z_t \sim N(0,1)$.

    **Step 1**: Estimate $\hat{\theta}$ by MLE.

    **Step 2**: Compute for each observation $t$:

    $$
    s_t = \nabla_\theta \ell_t(\hat{\theta}), \quad H_t = \nabla^2_\theta \ell_t(\hat{\theta})
    $$

    where $\ell_t(\theta) = -\frac{1}{2}\log(2\pi) - \frac{1}{2}\log\sigma_t^2 - \frac{r_t - \mu)^2}{2\sigma_t^2}$.

    **Step 3**: Form the sample estimates:

    $$
    \hat{A} = -\frac{1}{n}\sum_{t=1}^n H_t, \quad \hat{B} = \frac{1}{n}\sum_{t=1}^n s_t s_t^\top
    $$

    **Step 4**: Vectorize $\hat{A} - \hat{B}$ (taking unique elements due to symmetry; for $d = 4$ parameters, there are $d(d+1)/2 = 10$ unique elements). Construct the test statistic:

    $$
    T = n \cdot \text{vech}(\hat{A} - \hat{B})^\top \hat{\Omega}^{-1} \text{vech}(\hat{A} - \hat{B})
    $$

    where $\hat{\Omega}$ is a consistent estimate of the asymptotic covariance of $\text{vech}(\hat{A} - \hat{B})$.

    Under $H_0$: $T \xrightarrow{d} \chi^2_{10}$.

    **Step 5**: Reject $H_0$ if $T > \chi^2_{10, \alpha}$.

    **Interpretation of rejection**: Rejection of $H_0$ (i.e., $A \neq B$) indicates that the GARCH(1,1) model with Gaussian innovations is misspecified. Common reasons include:

    - **Non-normal innovations**: Returns may have heavier tails than Gaussian (Student-$t$ or GED innovations would be more appropriate). This manifests as excess kurtosis in standardized residuals $\hat{z}_t = \hat{\varepsilon}_t / \hat{\sigma}_t$.

    - **Asymmetric volatility response**: GARCH(1,1) treats positive and negative shocks symmetrically, while empirically negative returns increase volatility more (leverage effect). This is captured by GJR-GARCH or EGARCH models.

    - **Long memory in volatility**: GARCH(1,1) has exponentially decaying autocorrelation in $\sigma_t^2$, while realized volatility often exhibits long memory (slow hyperbolic decay), suggesting FIGARCH or rough volatility models.

    - **Regime changes**: The assumption of constant parameters $(\omega, \alpha, \beta)$ may fail during structural breaks or regime switches.

---

**Exercise 7.** In a simulation study, generate $n = 500$ observations from a stochastic volatility model (Heston) and fit both a Black-Scholes model and a Heston model. For each fitted model, compute the pricing error for an out-of-the-money put option ($K = 0.9 S_0$). Decompose the Black-Scholes error into misspecification and estimation components. For the Heston model, argue that the misspecification error is zero and all error comes from estimation. Under what conditions might the misspecified Black-Scholes model produce a smaller total error?

??? success "Solution to Exercise 7"

    **Setup**: The true DGP is Heston with parameters $(\kappa, \bar{v}, v_0, \xi, \rho, \mu)$. We observe $n = 500$ returns and fit:

    - **Model A** (BS): $dS_t = \hat{\mu} S_t \, dt + \hat{\sigma} S_t \, dW_t$ (1 parameter for pricing: $\hat{\sigma}$)
    - **Model B** (Heston): All 5 parameters estimated

    **Black-Scholes error decomposition**: The total pricing error for an OTM put ($K = 0.9 S_0$) is:

    $$
    |V_{\text{BS}}(\hat{\sigma}) - V^*| \leq \underbrace{|V_{\text{BS}}(\sigma^*) - V^*|}_{\text{misspecification}} + \underbrace{|V_{\text{BS}}(\hat{\sigma}) - V_{\text{BS}}(\sigma^*)|}_{\text{estimation}}
    $$

    - **Misspecification**: $V_{\text{BS}}(\sigma^*)$ uses the pseudo-true volatility $\sigma^* = \sqrt{\bar{v}}$ (approximately). For an OTM put, BS systematically underprices because it cannot capture the left-skew in the return distribution generated by negative $\rho$ (leverage effect). The implied volatility smile means that the OTM put's market-implied volatility exceeds $\sigma^*$. This error is $O(1)$ and does not vanish with more data.

    - **Estimation**: $|V_{\text{BS}}(\hat{\sigma}) - V_{\text{BS}}(\sigma^*)| \approx |\mathcal{V}| \cdot |\hat{\sigma} - \sigma^*|$. With $n = 500$, $|\hat{\sigma} - \sigma^*| = O_p(n^{-1/2}) \approx O_p(0.045)$. This is relatively small.

    **Heston error decomposition**: Since the true DGP is Heston, the model is correctly specified:

    $$
    |V_H(\hat{\theta}) - V^*| = \underbrace{|V_H(\theta^*) - V^*|}_{= 0} + |V_H(\hat{\theta}) - V_H(\theta^*)|
    $$

    The misspecification error is exactly zero. All error comes from estimation. However, with 5 parameters and $n = 500$, the estimation error may be substantial because:

    - Parameters like $\xi$ (vol-of-vol) and $\rho$ (correlation) are hard to estimate precisely from return data alone.
    - The pricing function $V_H(\theta)$ may have high sensitivity to certain parameters (e.g., $\xi$ affects the smile shape strongly).
    - The estimation error is $O_p(n^{-1/2})$ but with a potentially large constant due to the high-dimensional Fisher information structure.

    **When BS might win**: The misspecified BS can produce smaller total error when:

    $$
    \underbrace{|V_{\text{BS}}(\sigma^*) - V^*|}_{\text{BS misspecification}} + \underbrace{O_p(n^{-1/2})}_{\text{BS estimation}} < \underbrace{O_p(\sqrt{5/n})}_{\text{Heston estimation}}
    $$

    This can happen when:

    1. **The option is near ATM**: BS misspecification error is small for near-ATM options where the smile effect is minimal.
    2. **Heston parameters are poorly identified**: When $\kappa$ and $\bar{v}$ are confounded, or when $\xi$ is difficult to estimate, the Heston estimation error is inflated.
    3. **Small $n$ or short observation period**: With limited data, the 5-parameter Heston model overfits, producing larger out-of-sample errors than the parsimonious BS model.
    4. **Low vol-of-vol regime**: When $\xi$ is small, the Heston model is close to BS, so misspecification is mild but Heston's extra parameters add unnecessary estimation noise.

    This exemplifies the bias-variance trade-off: BS has higher bias but lower variance, while Heston has zero bias but higher variance. For small to moderate $n$, the simpler model can be preferred overall.
