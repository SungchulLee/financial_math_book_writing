# Model Uncertainty in Asset Allocation


## Introduction


**Model uncertainty in asset allocation** addresses the fundamental challenge that investors must choose among competing models of asset returns, each with different implications for optimal portfolio construction. Unlike parameter uncertainty within a fixed model, model uncertainty involves ambiguity about the correct structural specification of return dynamics.

This uncertainty manifests in several ways:

1. **Factor model selection**: Which factors explain returns?
2. **Distributional assumptions**: Normal vs. fat-tailed distributions
3. **Time series structure**: I.i.d. vs. predictable returns
4. **Regime dynamics**: Single regime vs. regime-switching models

The theoretical and practical implications connect Bayesian model averaging, robust optimization, and decision theory under ambiguity.

## Sources of Model Uncertainty


### 1. Factor Model Specification


**CAPM vs. Multi-Factor**: Should returns be modeled by:

$$
R_i - r_f = \alpha_i + \beta_i (R_m - r_f) + \epsilon_i
$$

or by Fama-French factors:

$$
R_i - r_f = \alpha_i + \beta_{i,m} (R_m - r_f) + \beta_{i,s} SMB + \beta_{i,v} HML + \epsilon_i
$$

or by alternative factors (momentum, quality, low volatility)?

**Implications**: Different factor models imply different expected returns and covariances, leading to different optimal portfolios.

### 2. Return Predictability


**Unpredictable Returns**:

$$
R_{t+1} = \mu + \epsilon_{t+1}
$$

**Predictable Returns** (with predictor $x_t$):

$$
R_{t+1} = \alpha + \beta x_t + \epsilon_{t+1}
$$

**Model Uncertainty**: Is the predictive coefficient $\beta$ zero or significantly different from zero?

### 3. Distributional Assumptions


**Gaussian**:

$$
R \sim N(\mu, \Sigma)
$$

**Student-t** (fat tails):

$$
R \sim t_{\nu}(\mu, \Sigma)
$$

**Mixture of Normals** (regimes):

$$
R \sim \sum_{k=1}^K \pi_k N(\mu_k, \Sigma_k)
$$

### 4. Parameter Stability


**Constant Parameters**:

$$
\mu_t = \mu, \quad \Sigma_t = \Sigma \quad \text{for all } t
$$

**Time-Varying Parameters**:

$$
\mu_t = f(z_t), \quad \Sigma_t = g(z_t)
$$

where $z_t$ are state variables.

## Bayesian Model Averaging


### 1. Framework


**Model Space**: Consider models $\mathcal{M} = \{M_1, M_2, \ldots, M_K\}$.

**Prior Model Probabilities**: $P(M_k)$ for $k = 1, \ldots, K$.

**Posterior Model Probabilities**:

$$
P(M_k | D) = \frac{P(D | M_k) P(M_k)}{\sum_{j=1}^K P(D | M_j) P(M_j)}
$$

where $P(D | M_k)$ is the marginal likelihood under model $k$.

### 2. Marginal Likelihood


**Definition**:

$$
P(D | M_k) = \int P(D | \theta_k, M_k) P(\theta_k | M_k) d\theta_k
$$

**Computation**: Often requires numerical integration (MCMC, importance sampling).

**BIC Approximation**:

$$
\log P(D | M_k) \approx \log P(D | \hat{\theta}_k, M_k) - \frac{d_k}{2} \log T
$$

where $d_k$ is the number of parameters in model $k$ and $T$ is the sample size.

### 3. Posterior Predictive Distribution


**BMA Predictive**:

$$
P(R_{T+1} | D) = \sum_{k=1}^K P(R_{T+1} | D, M_k) P(M_k | D)
$$

**Implication**: The predictive distribution is a mixture across models, weighted by posterior model probabilities.

### 4. Asset Allocation Under BMA


**Expected Utility**:

$$
\mathbb{E}[U(W_{T+1}) | D] = \sum_{k=1}^K P(M_k | D) \mathbb{E}[U(W_{T+1}) | D, M_k]
$$

**Optimal Portfolio**: Maximize expected utility under the BMA predictive distribution.

**Key Insight**: BMA naturally incorporates model uncertainty into portfolio choice.

## Model Uncertainty and Estimation Risk


### 1. Parameter Uncertainty Within Models


For each model $M_k$, the posterior distribution of parameters is:

$$
P(\theta_k | D, M_k) \propto P(D | \theta_k, M_k) P(\theta_k | M_k)
$$

**Total Uncertainty**: Combines within-model parameter uncertainty and across-model uncertainty:

$$
\text{Var}(R_{T+1} | D) = \underbrace{\sum_k P(M_k | D) \text{Var}(R_{T+1} | D, M_k)}_{\text{within-model}} + \underbrace{\text{Var}_k[\mathbb{E}(R_{T+1} | D, M_k)]}_{\text{across-model}}
$$

### 2. Effect on Portfolio Choice


**Conservative Allocation**: Model uncertainty typically:

- Increases perceived uncertainty about returns
- Shrinks optimal positions toward safer assets
- Reduces leverage

**Example**: If model $M_1$ predicts high equity returns and $M_2$ predicts low returns, BMA produces intermediate expectations with higher variance than either model alone.

### 3. Learning and Model Selection


**Dynamic Updating**: As data accumulates:

$$
P(M_k | D_1, \ldots, D_t) \propto P(D_t | D_1, \ldots, D_{t-1}, M_k) P(M_k | D_1, \ldots, D_{t-1})
$$

**Convergence**: Under regularity conditions, posterior concentrates on the "best" model (or model(s) closest to truth).

## Robust Approaches to Model Uncertainty


### 1. Minimax Regret


**Regret Definition**: For portfolio $w$ and true model $M$:

$$
\text{Regret}(w, M) = U(w^*(M)) - U(w)
$$

where $w^*(M)$ is optimal under model $M$.

**Minimax Regret**:

$$
w^{\text{MR}} = \arg\min_w \max_{M \in \mathcal{M}} \text{Regret}(w, M)
$$

**Properties**: Minimax regret is less conservative than maximin utility.

### 2. Multiple Priors (Ambiguity)


Recall MEU and smooth (KMM) preferences for choosing among models (see [§ Ambiguity-Averse Preferences](../ambiguity_averse_preferences/max_min_expected_utility.md)). Applied here, MEU gives $\max_w \min_{P \in \mathcal{P}} \sum_k P(M_k) \mathbb{E}[U(W) | M_k]$ (robust model weights), while KMM separates ambiguity attitude $\phi$ from second-order beliefs $\mu(M_k)$.

## Practical Applications


### 1. Strategic Asset Allocation


**Model Candidates**:

- Historical average returns
- CAPM equilibrium returns
- Black-Litterman with views
- Regime-switching models

**BMA Implementation**:

1. Estimate each model on historical data
2. Compute posterior model probabilities
3. Generate BMA predictive returns
4. Optimize portfolio under BMA distribution

### 2. Return Predictability Debate


**Key Question**: Are stock returns predictable?

**Model Comparison**:

- $M_0$: Unpredictable (random walk)
- $M_1$: Predictable by dividend yield
- $M_2$: Predictable by term spread

**Finding** (Avramov, 2002): Model uncertainty about predictability significantly affects optimal portfolios:

- Investors uncertain about predictability hold more conservative portfolios
- Effect is larger than parameter uncertainty within models

### 3. Factor Investing


**Model Selection**: Which factors to use?

$$
M_{\text{CAPM}}: \quad R = \alpha + \beta R_m + \epsilon
$$

$$
M_{\text{FF3}}: \quad R = \alpha + \beta_1 R_m + \beta_2 SMB + \beta_3 HML + \epsilon
$$

$$
M_{\text{FF5}}: \quad \text{adds RMW and CMA factors}
$$

**BMA Factor Model**: Weights factors by posterior model probabilities, naturally selecting relevant factors.

### 4. Regime-Switching Models


**Two-Regime Model**:

$$
R_t | S_t = k \sim N(\mu_k, \Sigma_k)
$$

with Markov switching for $S_t$.

**Model Uncertainty**: Uncertainty about:

- Number of regimes
- Transition probabilities
- State-dependent parameters

**Portfolio Implication**: Regime uncertainty leads to more diversified, defensive portfolios.

## Decision-Theoretic Foundations


### 1. Savage's Framework Extension


**State Space**: Extend to include model uncertainty:

$$
\Omega = \bigcup_{k=1}^K \Omega_k
$$

where $\Omega_k$ is the state space under model $M_k$.

**Acts**: A portfolio $w$ maps states to wealth outcomes.

**Preferences**: Complete ordering over acts incorporating model uncertainty.

### 2. Ellsberg Paradox in Finance


**Example**: Consider two assets:

- Asset A: Well-understood risk (stock index)
- Asset B: Novel asset with ambiguous risk (new asset class)

**Observation**: Investors may avoid Asset B even if it offers diversification benefits, due to ambiguity aversion.

**Implication**: Home bias and underdiversification may reflect model uncertainty aversion.

### 3. Dynamic Consistency


Recall rectangularity, sophisticated agents, and recursive preferences as resolutions to time-inconsistency under learning and ambiguity (see [§ Dynamic Consistency](dynamic_consistency.md)).

## Computational Methods


### 1. MCMC for BMA


**Algorithm** (Model-Space MCMC):

1. Initialize model $M^{(0)}$ and parameters $\theta^{(0)}$
2. For $i = 1, \ldots, N$:
   - Propose model move: $M' \sim q(M' | M^{(i-1)})$
   - Accept/reject based on marginal likelihood ratio
   - If accepted, draw $\theta^{(i)} \sim P(\theta | D, M')$

**Output**: Samples $(M^{(i)}, \theta^{(i)})$ approximate joint posterior.

### 2. Stochastic Programming


**Scenario-Based**:

1. Generate scenarios under each model
2. Assign probabilities based on posterior model weights
3. Solve:

$$
\max_w \sum_{k=1}^K P(M_k | D) \sum_{s=1}^{S_k} \frac{1}{S_k} U(w^\top R_s^{(k)})
$$

### 3. Numerical Integration


**Quadrature**: For low-dimensional problems, use numerical integration over parameter space within each model.

**Importance Sampling**: For high-dimensional problems:

$$
\mathbb{E}[g(R)] \approx \frac{1}{N} \sum_{i=1}^N w_i g(R^{(i)})
$$

with appropriate importance weights.

## Empirical Evidence


### 1. Out-of-Sample Performance


**Finding** (Uppal-Zaffaroni, 2013): Portfolios that account for model uncertainty:

- Lower turnover
- Better Sharpe ratios out-of-sample
- More robust to regime changes

### 2. Hedge Fund Returns


**Model Uncertainty**: Hedge fund returns exhibit:

- Non-normality
- Regime dependence
- Time-varying factor exposures

**Implication**: Traditional mean-variance ignores significant model uncertainty.

### 3. International Diversification


**Home Bias Puzzle**: Investors hold too little foreign equity.

**Model Uncertainty Explanation**: Greater ambiguity about foreign market models → ambiguity aversion → home bias.

## Summary


### Key Results


1. **BMA Framework**: Provides coherent treatment of model uncertainty in asset allocation

2. **Posterior Averaging**: Combines within-model and across-model uncertainty

3. **Conservative Portfolios**: Model uncertainty leads to more diversified, less levered positions

4. **Dynamic Learning**: Bayesian updating allows for learning about true model

### Practical Implications


1. **Model Humility**: Consider multiple models rather than committing to one
2. **Diversification Value**: Model uncertainty strengthens case for diversification
3. **Robust Portfolios**: Design portfolios that perform reasonably across models
4. **Continuous Updating**: Update model beliefs as new evidence arrives

Model uncertainty in asset allocation represents a fundamental challenge that standard optimization ignores, requiring either Bayesian or robust approaches to produce sensible investment strategies.

---

## Exercises

**Exercise 1.** An investor considers two models for equity returns: Model A (GBM with $\mu_A = 0.08$, $\sigma_A = 0.18$) and Model B (regime-switching with $\mu_B^1 = 0.12$, $\sigma_B^1 = 0.12$ in the bull regime and $\mu_B^2 = -0.05$, $\sigma_B^2 = 0.30$ in the bear regime). For a mean-variance investor with risk aversion $\lambda = 3$, compute the optimal equity allocation under each model. How does the allocation change under Bayesian model averaging with equal model weights?

??? success "Solution to Exercise 1"
    **Optimal allocation under each model.**

    For a mean-variance investor with risk aversion $\lambda$, the optimal weight in equity (with a risk-free asset) is:

    $$
    w^* = \frac{\mu - r_f}{\lambda \sigma^2}
    $$

    (assuming zero risk-free rate for simplicity, so $\mu$ is the excess return).

    **Model A (GBM):** $\mu_A = 0.08$, $\sigma_A = 0.18$, $\lambda = 3$.

    $$
    w_A^* = \frac{0.08}{3 \times 0.18^2} = \frac{0.08}{3 \times 0.0324} = \frac{0.08}{0.0972} = 0.823
    $$

    **Model B (regime-switching):** We need the unconditional moments. Let $\pi_1$ and $\pi_2 = 1 - \pi_1$ be the stationary regime probabilities. Without further information about transition probabilities, assume equal time in each regime: $\pi_1 = \pi_2 = 0.5$.

    Unconditional mean:

    $$
    \mu_B = \pi_1 \mu_B^1 + \pi_2 \mu_B^2 = 0.5 \times 0.12 + 0.5 \times (-0.05) = 0.035
    $$

    Unconditional variance (using the law of total variance):

    $$
    \sigma_B^2 = \pi_1 (\sigma_B^1)^2 + \pi_2 (\sigma_B^2)^2 + \pi_1 \pi_2 (\mu_B^1 - \mu_B^2)^2
    $$

    $$
    = 0.5 \times 0.0144 + 0.5 \times 0.09 + 0.5 \times 0.5 \times (0.17)^2
    $$

    $$
    = 0.0072 + 0.045 + 0.25 \times 0.0289 = 0.0072 + 0.045 + 0.007225 = 0.059425
    $$

    $$
    w_B^* = \frac{0.035}{3 \times 0.059425} = \frac{0.035}{0.178275} = 0.196
    $$

    **Model-averaged allocation under BMA.** With equal model weights $P(M_A) = P(M_B) = 0.5$, the BMA predictive distribution has:

    $$
    \mu_{\text{BMA}} = 0.5 \times 0.08 + 0.5 \times 0.035 = 0.0575
    $$

    For the variance, use the law of total variance across models:

    $$
    \sigma_{\text{BMA}}^2 = \underbrace{0.5 \times 0.0324 + 0.5 \times 0.059425}_{\text{within-model}} + \underbrace{0.5 \times 0.5 \times (0.08 - 0.035)^2}_{\text{across-model}}
    $$

    $$
    = 0.0162 + 0.029713 + 0.25 \times 0.002025 = 0.045913 + 0.000506 = 0.046419
    $$

    $$
    w_{\text{BMA}}^* = \frac{0.0575}{3 \times 0.046419} = \frac{0.0575}{0.139257} = 0.413
    $$

    **Summary:**

    | | Model A | Model B | BMA |
    |---|---------|---------|-----|
    | Mean return | 8.0% | 3.5% | 5.75% |
    | Variance | 0.0324 | 0.0594 | 0.0464 |
    | Optimal weight | 82.3% | 19.6% | 41.3% |

    The BMA allocation (41.3%) is between the two model-specific allocations but is not simply their average (which would be $(82.3 + 19.6)/2 = 51.0\%$). It is lower because the BMA variance exceeds the average of individual model variances due to the across-model variance component. Model uncertainty leads to a more conservative allocation.

---

**Exercise 2.** Using the Bayesian framework, derive the posterior distribution of the mean return $\mu$ given a conjugate prior $\mu \sim N(\mu_0, \sigma_0^2)$ and $n$ observed returns with sample mean $\bar{X}$ and known variance $\sigma^2$. Show that the posterior predictive variance exceeds the sample variance by a term reflecting estimation uncertainty, and explain how this additional variance affects portfolio construction.

??? success "Solution to Exercise 2"
    **Setup.** Prior: $\mu \sim N(\mu_0, \sigma_0^2)$. Data: $n$ observations with sample mean $\bar{X}$ and known variance $\sigma^2$.

    **Likelihood:** $\bar{X} \mid \mu \sim N(\mu, \sigma^2/n)$.

    **Posterior derivation.** By Bayes' theorem for conjugate Gaussian:

    $$
    p(\mu \mid \bar{X}) \propto p(\bar{X} \mid \mu) p(\mu) \propto \exp\!\left(-\frac{n(\bar{X} - \mu)^2}{2\sigma^2}\right) \exp\!\left(-\frac{(\mu - \mu_0)^2}{2\sigma_0^2}\right)
    $$

    Completing the square in $\mu$: define the posterior precision as $\tau_n = 1/\sigma_0^2 + n/\sigma^2$ and the posterior mean as:

    $$
    \mu_n = \frac{\mu_0/\sigma_0^2 + n\bar{X}/\sigma^2}{1/\sigma_0^2 + n/\sigma^2} = \frac{\tau_0 \mu_0 + \tau_{\text{data}} \bar{X}}{\tau_0 + \tau_{\text{data}}}
    $$

    where $\tau_0 = 1/\sigma_0^2$ and $\tau_{\text{data}} = n/\sigma^2$. The posterior variance is:

    $$
    \sigma_n^2 = \frac{1}{\tau_n} = \frac{1}{1/\sigma_0^2 + n/\sigma^2}
    $$

    So $\mu \mid \bar{X} \sim N(\mu_n, \sigma_n^2)$.

    **Posterior predictive distribution.** For a new return $R_{n+1} \mid \mu \sim N(\mu, \sigma^2)$:

    $$
    R_{n+1} \mid \bar{X} \sim N(\mu_n, \sigma^2 + \sigma_n^2)
    $$

    The predictive variance is:

    $$
    \text{Var}(R_{n+1} \mid \bar{X}) = \sigma^2 + \sigma_n^2 = \sigma^2 + \frac{1}{1/\sigma_0^2 + n/\sigma^2}
    $$

    **Excess variance from estimation uncertainty.** The sample variance of returns is $\sigma^2$. The posterior predictive variance exceeds this by:

    $$
    \Delta = \sigma_n^2 = \frac{1}{1/\sigma_0^2 + n/\sigma^2}
    $$

    In the noninformative prior limit ($\sigma_0^2 \to \infty$):

    $$
    \Delta = \frac{\sigma^2}{n}
    $$

    which is exactly the standard error of the mean squared.

    **Effect on portfolio construction.** For a mean-variance investor with risk aversion $\lambda$, the optimal allocation using the predictive distribution is:

    $$
    w^* = \frac{\mu_n}{\lambda(\sigma^2 + \sigma_n^2)}
    $$

    Compared to the plug-in solution $w_{\text{plug}} = \bar{X} / (\lambda \sigma^2)$, the Bayesian solution is more conservative in two ways:

    1. **Shrunk mean:** $\mu_n$ is shrunk from $\bar{X}$ toward the prior $\mu_0$ (reducing the numerator)
    2. **Inflated variance:** $\sigma^2 + \sigma_n^2 > \sigma^2$ (increasing the denominator)

    Both effects push the allocation toward zero (i.e., toward the risk-free asset), reflecting proper accounting for estimation uncertainty.

---

**Exercise 3.** Compare three approaches to handling model uncertainty in a two-asset allocation problem: (a) plug-in optimization using MLE estimates, (b) Bayesian model averaging, and (c) robust optimization with an ellipsoidal uncertainty set. For each, describe the resulting portfolio and explain which approach produces the most diversified allocation.

??? success "Solution to Exercise 3"
    Consider two assets with unknown mean $\mu = (\mu_1, \mu_2)^\top$ and known covariance $\Sigma$.

    **(a) Plug-in optimization (MLE).**

    Estimate $\hat{\mu}$ from sample means and compute:

    $$
    w_{\text{plug}} = \frac{1}{\lambda}\Sigma^{-1}\hat{\mu}
    $$

    **Properties:** This approach treats $\hat{\mu}$ as if it were the true $\mu$. It is known to be an "error maximizer" --- it overweights assets whose returns are overestimated and underweights those with underestimated returns. The resulting portfolio is often highly concentrated, unstable across samples, and performs poorly out of sample.

    **(b) Bayesian model averaging.**

    Suppose the investor considers $K$ models, each producing a posterior predictive distribution. Under BMA:

    $$
    p(R \mid D) = \sum_{k=1}^K P(M_k \mid D)\, p(R \mid D, M_k)
    $$

    The optimal BMA portfolio maximizes expected utility under this mixture:

    $$
    w_{\text{BMA}} = \arg\max_w \sum_{k=1}^K P(M_k \mid D)\,\mathbb{E}_{M_k}\!\left[U(w^\top R) \mid D\right]
    $$

    For mean-variance utility, this becomes:

    $$
    w_{\text{BMA}} = \frac{1}{\lambda}\Sigma_{\text{BMA}}^{-1}\mu_{\text{BMA}}
    $$

    where $\mu_{\text{BMA}}$ and $\Sigma_{\text{BMA}}$ are the mean and covariance of the BMA predictive distribution. Since $\Sigma_{\text{BMA}}$ includes both within-model and across-model variance, the BMA portfolio is more diversified than the plug-in.

    **Properties:** BMA naturally incorporates parameter and model uncertainty. The predictive covariance is inflated relative to any single model, and the predictive mean is a weighted average. Both effects encourage diversification.

    **(c) Robust optimization with ellipsoidal uncertainty.**

    The robust portfolio solves:

    $$
    w_{\text{robust}} = \arg\max_w \left\{w^\top \hat{\mu} - \kappa\sqrt{w^\top \Omega w} - \frac{\lambda}{2}w^\top \Sigma w\right\}
    $$

    where $\Omega$ is the estimation error covariance and $\kappa$ controls the confidence level.

    **Properties:** The penalty term $\kappa\sqrt{w^\top \Omega w}$ penalizes portfolios that are sensitive to estimation errors. This pushes the portfolio away from concentrated positions (which have high exposure to estimation error) toward more diversified allocations. The robust portfolio explicitly shrinks positions in assets with high estimation uncertainty.

    **Comparison:**

    | Feature | Plug-in | BMA | Robust |
    |---------|---------|-----|--------|
    | Estimation error | Ignored | Accounted via predictive variance | Accounted via uncertainty set |
    | Diversification | Low (concentrated) | Moderate | High |
    | Stability | Low (sensitive to sample) | Moderate | High |
    | Conservatism | Low | Moderate | High (controllable via $\kappa$) |

    The **robust optimization** approach typically produces the most diversified allocation because the worst-case penalty explicitly penalizes concentrated positions. BMA is the second most diversified, and plug-in the least. However, robust optimization may be overly conservative if $\kappa$ is set too large, while BMA provides a more natural calibration of uncertainty through the posterior.

---

**Exercise 4.** The "estimation risk premium" is the additional return required to compensate for parameter uncertainty. For a single risky asset with uncertain mean $\mu \sim N(\hat{\mu}, \sigma_\mu^2)$, derive the effective risk aversion of a Bayesian investor and show that it exceeds the nominal risk aversion $\lambda$ by a term proportional to $\sigma_\mu^2 / \sigma^2$, where $\sigma^2$ is the return variance.

??? success "Solution to Exercise 4"
    **Setup.** A single risky asset with return $R \sim N(\mu, \sigma^2)$, where $\mu$ is uncertain: $\mu \sim N(\hat{\mu}, \sigma_\mu^2)$. A mean-variance investor has nominal risk aversion $\lambda$.

    **Bayesian predictive distribution.** By the law of total expectation and variance:

    $$
    \mathbb{E}[R] = \hat{\mu}, \quad \text{Var}(R) = \sigma^2 + \sigma_\mu^2
    $$

    **Optimal portfolio.** Under mean-variance preferences, the optimal weight in the risky asset is:

    $$
    w^* = \frac{\hat{\mu}}{\lambda(\sigma^2 + \sigma_\mu^2)}
    $$

    **Rewriting as effective risk aversion.** We can write:

    $$
    w^* = \frac{\hat{\mu}}{\lambda_{\text{eff}} \cdot \sigma^2}
    $$

    where the effective risk aversion is:

    $$
    \lambda_{\text{eff}} = \lambda \cdot \frac{\sigma^2 + \sigma_\mu^2}{\sigma^2} = \lambda\!\left(1 + \frac{\sigma_\mu^2}{\sigma^2}\right)
    $$

    **The estimation risk premium.** The effective risk aversion exceeds the nominal risk aversion by:

    $$
    \Delta\lambda = \lambda \cdot \frac{\sigma_\mu^2}{\sigma^2}
    $$

    Equivalently, the investor requires an additional return of:

    $$
    \text{Estimation risk premium} = \Delta\lambda \cdot \sigma^2 \cdot w = \lambda \sigma_\mu^2 w
    $$

    to compensate for parameter uncertainty.

    **Financial interpretation.** The ratio $\sigma_\mu^2 / \sigma^2$ measures the relative importance of estimation uncertainty compared to return uncertainty. With a noninformative prior and $n$ observations, $\sigma_\mu^2 \approx \sigma^2/n$, so:

    $$
    \lambda_{\text{eff}} = \lambda\!\left(1 + \frac{1}{n}\right)
    $$

    For $n = 60$ monthly observations, $\lambda_{\text{eff}} \approx 1.017\lambda$ --- a modest increase. But for $n = 10$, $\lambda_{\text{eff}} = 1.1\lambda$, a 10% increase. With informative priors or multiple uncertain parameters, the effect can be much larger. The estimation risk premium is the additional compensation the Bayesian investor demands for bearing parameter uncertainty, and it is the mechanism through which uncertainty about $\mu$ leads to more conservative positions.

---

**Exercise 5.** Demonstrate the "1/N puzzle": for $N = 10$ assets with estimated mean returns and covariance, show numerically that the naive equal-weight portfolio $w_i = 1/N$ often outperforms the Markowitz optimal portfolio out of sample. Explain this result in terms of estimation error amplification and the condition number of the sample covariance matrix.

??? success "Solution to Exercise 5"
    **The $1/N$ puzzle.**

    **Setup.** Consider $N = 10$ assets. We generate data from a known model (e.g., multivariate normal with true $\mu$ and $\Sigma$), estimate parameters from a sample of size $T$, and compare:

    1. **Markowitz portfolio:** $w_{\text{MV}} = \frac{1}{\lambda}\hat{\Sigma}^{-1}\hat{\mu}$ (with normalization)
    2. **Equal-weight portfolio:** $w_{1/N} = (1/N, \ldots, 1/N)^\top$

    **Why $1/N$ outperforms.**

    The out-of-sample Sharpe ratio of the Markowitz portfolio depends on the **estimation error**, which has two components:

    $$
    w_{\text{MV}} - w^* = \frac{1}{\lambda}\hat{\Sigma}^{-1}(\hat{\mu} - \mu) + \frac{1}{\lambda}(\hat{\Sigma}^{-1} - \Sigma^{-1})\mu
    $$

    The variance of the estimation error is amplified by $\hat{\Sigma}^{-1}$, which amplifies noise in $\hat{\mu}$.

    **Condition number.** The condition number $\kappa(\hat{\Sigma}) = \lambda_{\max}(\hat{\Sigma}) / \lambda_{\min}(\hat{\Sigma})$ measures how much $\hat{\Sigma}^{-1}$ amplifies errors. For typical financial data with $N = 10$ and $T = 60$:

    - The sample covariance matrix has $N(N+1)/2 = 55$ free parameters but only $T = 60$ data points
    - The condition number is often $\kappa \approx 50$--$500$
    - Small errors in $\hat{\mu}$ get amplified by a factor proportional to $\kappa$

    **Bias-variance tradeoff.** Let us decompose the out-of-sample expected utility loss:

    $$
    \mathbb{E}[\text{Loss}(w)] = \underbrace{(w - w^*)^\top \Sigma (w - w^*)}_{\text{variance of error}} + \underbrace{(\mathbb{E}[w] - w^*)^\top \Sigma (\mathbb{E}[w] - w^*)}_{\text{bias}^2}
    $$

    The $1/N$ portfolio has zero variance (it does not depend on data) but potentially large bias (it ignores the true optimal weights). The Markowitz portfolio has zero bias (on average, it targets the right weights) but large variance (estimation errors make each realization far from optimal).

    **Threshold.** The $1/N$ portfolio outperforms when:

    $$
    \text{Bias}^2(1/N) < \text{Variance}(\text{MV})
    $$

    DeMiguel, Garlappi, and Uppal (2009) showed that this holds when:

    $$
    T < T^* \approx \frac{N \cdot \kappa(\Sigma)}{\text{SR}^2}
    $$

    where $\text{SR}$ is the Sharpe ratio of the true tangent portfolio. For realistic parameters ($N = 10$, $\kappa = 100$, $\text{SR} = 0.5$), $T^* \approx 4000$ months (over 300 years), explaining why $1/N$ dominates in practice.

    **Numerical illustration.** With $N = 10$, $T = 120$ (10 years monthly), typical simulations show:

    - Markowitz out-of-sample SR: $\approx 0.15$
    - $1/N$ out-of-sample SR: $\approx 0.30$

    The $1/N$ portfolio achieves roughly double the Sharpe ratio by completely avoiding estimation error, even though it ignores all information about expected returns and correlations.

---

**Exercise 6.** An investor uses Bayesian model averaging with three models: Black-Scholes, Heston, and SABR. The posterior model probabilities are $P(M_1 | \text{data}) = 0.5$, $P(M_2 | \text{data}) = 0.35$, $P(M_3 | \text{data}) = 0.15$. For a portfolio of options, compute the model-averaged price and the model uncertainty contribution to total pricing uncertainty. How should the investor update these weights as new data arrives?

??? success "Solution to Exercise 6"
    **Model-averaged price.**

    Let $C_k$ denote the option price under model $M_k$. The BMA price is:

    $$
    \bar{C} = \sum_{k=1}^3 P(M_k \mid \text{data}) \cdot C_k = 0.50 \, C_1 + 0.35 \, C_2 + 0.15 \, C_3
    $$

    For concreteness, suppose the models produce prices for a European call:

    - Black-Scholes ($M_1$): $C_1 = \$10.50$
    - Heston ($M_2$): $C_2 = \$11.20$
    - SABR ($M_3$): $C_3 = \$10.80$

    Then:

    $$
    \bar{C} = 0.50 \times 10.50 + 0.35 \times 11.20 + 0.15 \times 10.80 = 5.25 + 3.92 + 1.62 = \$10.79
    $$

    **Model uncertainty contribution to total pricing uncertainty.**

    The total pricing variance under BMA decomposes via the law of total variance:

    $$
    \text{Var}(C \mid \text{data}) = \underbrace{\sum_{k=1}^3 P(M_k \mid \text{data})\,\text{Var}(C \mid M_k, \text{data})}_{\text{within-model uncertainty}} + \underbrace{\sum_{k=1}^3 P(M_k \mid \text{data})(C_k - \bar{C})^2}_{\text{across-model uncertainty}}
    $$

    The **across-model** (model uncertainty) component:

    $$
    \text{Var}_{\text{model}} = 0.50(10.50 - 10.79)^2 + 0.35(11.20 - 10.79)^2 + 0.15(10.80 - 10.79)^2
    $$

    $$
    = 0.50 \times 0.0841 + 0.35 \times 0.1681 + 0.15 \times 0.0001
    $$

    $$
    = 0.04205 + 0.05884 + 0.000015 = 0.10090
    $$

    So $\text{Var}_{\text{model}} \approx 0.101$, giving a model uncertainty standard deviation of $\sqrt{0.101} \approx \$0.318$.

    Suppose within-model parameter uncertainty contributes $\text{Var}_{\text{param}} \approx 0.05$ (typical for well-calibrated models). Then:

    $$
    \text{Var}_{\text{total}} = 0.05 + 0.101 = 0.151
    $$

    The model uncertainty fraction is $0.101 / 0.151 \approx 67\%$ --- model uncertainty dominates parameter uncertainty. This is a common empirical finding: the choice of model matters more than the precise calibration within any given model.

    **Updating model weights with new data.**

    As new data $D_{\text{new}}$ arrives, the model weights are updated via Bayes' theorem:

    $$
    P(M_k \mid D_{\text{old}}, D_{\text{new}}) = \frac{P(D_{\text{new}} \mid D_{\text{old}}, M_k)\,P(M_k \mid D_{\text{old}})}{\sum_{j=1}^3 P(D_{\text{new}} \mid D_{\text{old}}, M_j)\,P(M_j \mid D_{\text{old}})}
    $$

    where $P(D_{\text{new}} \mid D_{\text{old}}, M_k) = \int P(D_{\text{new}} \mid \theta_k, M_k)\,P(\theta_k \mid D_{\text{old}}, M_k)\,d\theta_k$ is the **predictive likelihood** under model $k$.

    **Practical implementation:**

    1. For each model $M_k$, compute the predictive likelihood of the new data using the current posterior over parameters
    2. Multiply by the current model weight to get unnormalized posterior
    3. Normalize to obtain updated weights

    Models that better predict the new data receive increased weight. Over time, the posterior concentrates on the model (or models) that best explain the data. However, if the true data-generating process is a mixture or does not exactly match any model, the weights may not converge to a degenerate distribution, maintaining meaningful model uncertainty indefinitely.

    **For a portfolio of options**, the BMA approach should be applied to each option in the portfolio, with the model-averaged portfolio value being $\bar{V} = \sum_k P(M_k \mid \text{data}) V_k$, where $V_k$ is the portfolio value under model $k$. Correlation effects across options within the portfolio are automatically captured by the within-model covariance structure.
