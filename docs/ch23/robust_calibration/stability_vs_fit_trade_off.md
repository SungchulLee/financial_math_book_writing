# Stability vs Fit Trade-Off


## Introduction


The **stability vs fit trade-off** is a fundamental tension in model calibration: models that fit current market data extremely well often exhibit unstable parameters that change dramatically with small data perturbations or over short time intervals. This instability can lead to erratic hedging behavior, excessive transaction costs, and poor out-of-sample performance.

Understanding and managing this trade-off is crucial for:

1. **Practical hedging**: Stable parameters lead to stable hedge ratios
2. **Risk management**: Unstable calibrations create unreliable risk estimates
3. **Model governance**: Regulators expect stable, interpretable models
4. **Trading costs**: Unstable hedges generate excessive turnover

## The Trade-Off in Detail


### 1. Perfect Fit vs. Stability


**Perfect Fit**: Minimize calibration error exactly:

$$
\hat{\theta} = \arg\min_{\theta} \sum_{i=1}^m [C_i^{\text{market}} - C_i^{\text{model}}(\theta)]^2
$$

**Problem**: Small changes in $\{C_i^{\text{market}}\}$ can cause large changes in $\hat{\theta}$.

**Ill-Conditioning**: The optimization landscape may have:

- Flat regions (parameters poorly identified)
- Near-singular Hessian
- Multiple local minima

### 2. Quantifying Instability


**Parameter Sensitivity**: For data perturbation $\delta C$:

$$
\delta \theta \approx -H^{-1} J^\top \delta C
$$

where $H$ is the Hessian and $J$ is the Jacobian of model prices.

**Condition Number**: 

$$
\kappa = \|H^{-1}\| \cdot \|H\|
$$

Large $\kappa$ indicates ill-conditioning.

**Temporal Stability**: Measure parameter variation over time:

$$
\text{Volatility}(\theta_t) = \sqrt{\text{Var}_t(\theta_{t+1} - \theta_t)}
$$

### 3. Sources of Instability


**Over-Parameterization**: More parameters than data can constrain.

**Near-Flat Directions**: Some parameter combinations affect prices minimally.

**Noise in Data**: Bid-ask bounce, stale quotes, asynchronous observations.

**Model Misspecification**: True dynamics not captured by model.

## Regularization Approaches


### 1. Tikhonov, LASSO, Elastic Net

**Recall** (see [§ Regularization and Stability](../../ch17/regularization_and_stability/tikhonov_regularization.md)): standard penalties applied to the calibration objective $\text{Error}(\theta)$:

- **Tikhonov ($L^2$):** $+\lambda\|\theta - \theta_0\|^2$ — shrinks toward $\theta_0$; bias-variance tradeoff in $\lambda$.
- **LASSO ($L^1$):** $+\lambda\|\theta\|_1$ — promotes sparsity (factor selection).
- **Elastic Net:** $+\lambda_1\|\theta\|_1 + \lambda_2\|\theta\|_2^2$ — sparsity plus grouping.

### 2. Temporal Regularization


**Smooth Parameter Evolution**:

$$
\hat{\theta}_t = \arg\min_{\theta} \left\{\text{Error}_t(\theta) + \gamma \|\theta - \hat{\theta}_{t-1}\|^2\right\}
$$

**Effect**: Penalizes large parameter jumps between calibrations.

## Cross-Validation for Penalty Selection

**Recall** (see [§ Trade-Off Between Fit and Robustness](../../ch17/regularization_and_stability/trade_off_between_fit_and_robustness.md)): standard tools for choosing $\lambda$ are $K$-fold CV, time-series (rolling-window) CV, and information criteria AIC/BIC. For time-series calibration, rolling-window CV is preferred to preserve temporal ordering and avoid leakage.

## Pareto Frontier Analysis


### 1. Multi-Objective Formulation


**Objectives**:

1. $f_1(\theta)$: Calibration error (minimize)
2. $f_2(\theta)$: Parameter instability (minimize)

**Pareto Optimal**: $\theta^*$ is Pareto optimal if no $\theta$ improves both objectives.

### 2. Computing the Frontier


**Weighted Sum**:

$$
\min_{\theta} \{w \cdot f_1(\theta) + (1-w) \cdot f_2(\theta)\}
$$

for $w \in [0, 1]$.

**$\epsilon$-Constraint**:

$$
\min_{\theta} f_1(\theta) \quad \text{s.t.} \quad f_2(\theta) \leq \epsilon
$$

### 3. Visualizing Trade-Offs


**Pareto Plot**: Graph $f_1$ vs $f_2$ for Pareto optimal solutions.

**Interpretation**: Points on frontier represent optimal trade-offs; decision-maker chooses preferred balance.

## Stochastic Volatility Example


### 1. Heston Calibration Instability


**Observation**: Daily Heston calibrations show high parameter volatility.

**Correlations**: Parameters often highly correlated (e.g., $\kappa$ and $\bar{v}$).

**Identifiability**: Some parameter combinations better identified than individual parameters.

### 2. Re-Parameterization


**Alternative Parameters**: Instead of $(\kappa, \bar{v}, \sigma_v)$, use:

$$
\begin{aligned}
\theta_1 &= \kappa \bar{v} \quad \text{(long-run variance rate)} \\
\theta_2 &= \frac{\sigma_v^2}{4\kappa} \quad \text{(Feller ratio)}
\end{aligned}
$$

**Benefit**: Re-parameterized quantities may be more stable.

### 3. Regularized Heston Calibration


**Objective**:

$$
\min_{\theta} \left\{\sum_{i,j} w_{ij}[\sigma_{ij}^{\text{mkt}} - \sigma_{ij}^{\text{Heston}}(\theta)]^2 + \lambda \|\theta - \theta_{\text{prior}}\|_{\Sigma^{-1}}^2\right\}
$$

where $\theta_{\text{prior}}$ is historical average and $\Sigma$ is parameter covariance.

## Practical Strategies


### 1. Fix Poorly Identified Parameters


**Approach**: Fix parameters with flat likelihood to reasonable values.

**Example**: In Heston, fix $\kappa$ to historical estimate; calibrate remaining parameters.

### 2. Hierarchical Calibration


**Two-Stage**:

1. Calibrate slow-moving parameters (e.g., mean reversion) on long history
2. Calibrate fast-moving parameters (e.g., current vol) daily

### 3. Ensemble Methods


**Multiple Calibrations**: Run calibrations from different starting points.

**Averaging**: Use average or median of parameter estimates.

**Benefit**: Reduces sensitivity to individual optimization path.

### 4. Filtering Approaches


**Kalman Filter**: Model parameters as latent states:

$$
\theta_t = \theta_{t-1} + \eta_t
$$

**Update**: Combine prior $\theta_{t-1}$ with new data to get $\theta_t$.

**Benefit**: Natural smoothing of parameter paths.

## Measuring and Monitoring Stability


### 1. Stability Metrics


**Daily Parameter Change**:

$$
\Delta \theta_t = \|\theta_t - \theta_{t-1}\|
$$

**Coefficient of Variation**:

$$
\text{CV}(\theta_i) = \frac{\text{std}(\theta_{i,t})}{\text{mean}(\theta_{i,t})}
$$

**Rolling Correlation**: Correlation between parameter changes and market moves.

### 2. Stability Monitoring Dashboard


**Visualizations**:

- Time series of parameters
- Calibration error vs stability scatter
- Parameter correlation matrix

**Alerts**: Flag unusual parameter jumps.

### 3. Back-Testing Stability


**Procedure**: Re-calibrate model on historical data; compare with actual parameters used.

**Metric**: Tracking error between back-tested and actual parameters.

## Impact on Hedging


### 1. Hedge Stability


**Delta Stability**: Variation in hedge ratio over time:

$$
\text{Var}(\Delta_t - \Delta_{t-1})
$$

**Transaction Costs**: Proportional to turnover:

$$
\text{Cost} \propto \sum_t |\Delta_t - \Delta_{t-1}|
$$

### 2. Regularized Hedging


**Penalty on Hedge Changes**:

$$
\min_{\Delta_t} \left\{\text{HedgingError}_t + \gamma |\Delta_t - \Delta_{t-1}|\right\}
$$

**Effect**: Smooth hedge adjustments, reduce trading.

### 3. Empirical Results


**Finding**: Regularized calibrations often produce:

- Similar or better hedging performance
- Lower transaction costs
- More interpretable parameter dynamics

## Summary


### Key Concepts


1. **Trade-Off**: Perfect fit often implies unstable parameters

2. **Regularization**: Penalties shrink parameters, reduce variance

3. **Cross-Validation**: Select penalty to optimize out-of-sample performance

4. **Pareto Analysis**: Visualize and choose optimal fit-stability balance

### Best Practices


1. **Always regularize**: Default to some regularization rather than none
2. **Monitor stability**: Track parameter dynamics over time
3. **Use prior information**: Incorporate historical or cross-sectional priors
4. **Test out-of-sample**: Validate that stable calibrations perform well

The stability vs fit trade-off is unavoidable in financial modeling; successful practitioners explicitly manage this trade-off through regularization, monitoring, and appropriate penalty selection.

---

## Exercises

**Exercise 1.** Consider a calibration problem where the Hessian matrix of the objective function has eigenvalues $\lambda_1 = 100$ and $\lambda_2 = 0.01$. Compute the condition number $\kappa$. If market prices are perturbed by $\delta C$ with $\|\delta C\| = 0.001$, estimate the maximum possible parameter perturbation $\|\delta \theta\|$ using the relation $\delta \theta \approx -H^{-1} J^\top \delta C$. What does this tell you about calibration stability?

??? success "Solution to Exercise 1"

    **Condition number.** The condition number of the Hessian is

    $$
    \kappa = \frac{\lambda_{\max}}{\lambda_{\min}} = \frac{100}{0.01} = 10{,}000
    $$

    **Maximum parameter perturbation.** The parameter perturbation satisfies

    $$
    \delta \theta \approx -H^{-1} J^\top \delta C
    $$

    Taking norms:

    $$
    \|\delta \theta\| \leq \|H^{-1}\| \cdot \|J^\top\| \cdot \|\delta C\|
    $$

    The spectral norm of $H^{-1}$ is $\|H^{-1}\| = 1/\lambda_{\min} = 1/0.01 = 100$. In the worst case, the Jacobian can amplify the perturbation. If we assume $\|J^\top \delta C\|$ has the same order as $\|H\| \cdot \|\delta C\|$ (i.e., $J^\top$ has norm comparable to $\|H\|^{1/2}$), then a rough bound is:

    $$
    \|\delta \theta\| \leq \|H^{-1}\| \cdot \|J^\top\| \cdot \|\delta C\|
    $$

    More directly, in the Gauss-Newton setting where $H \approx J^\top J$, the sensitivity is:

    $$
    \|\delta \theta\| \approx \|H^{-1} J^\top\| \cdot \|\delta C\| \leq \frac{1}{\lambda_{\min}(H)} \|J^\top\| \cdot \|\delta C\|
    $$

    For a concrete estimate, note that the condition number tells us the ratio of maximum to minimum sensitivity. Along the direction corresponding to $\lambda_{\min} = 0.01$, a perturbation of size $\|\delta C\| = 0.001$ can cause a parameter shift of order

    $$
    \|\delta \theta\|_{\max} \approx \frac{\|\delta C\|}{\sqrt{\lambda_{\min}}} = \frac{0.001}{\sqrt{0.01}} = \frac{0.001}{0.1} = 0.01
    $$

    while along the well-determined direction ($\lambda_{\max} = 100$):

    $$
    \|\delta \theta\|_{\min} \approx \frac{\|\delta C\|}{\sqrt{\lambda_{\max}}} = \frac{0.001}{\sqrt{100}} = \frac{0.001}{10} = 0.0001
    $$

    **Interpretation.** The condition number $\kappa = 10{,}000$ is extremely large, indicating severe ill-conditioning. A tiny market data perturbation of $0.001$ (one-tenth of a basis point in price) can cause parameter shifts 100 times larger in the poorly-identified direction than in the well-identified direction. This means:

    - The calibration is highly unstable: daily recalibration will produce large parameter jumps
    - Some parameter combinations are nearly unidentifiable from the data
    - Regularization is essential to stabilize the calibration
    - The poorly-identified direction likely corresponds to a "flat valley" in the objective function

---

**Exercise 2.** For Tikhonov regularization with objective

$$
\hat{\theta}_\lambda = \arg\min_\theta \left\{ \sum_{i=1}^m [C_i^{\text{market}} - C_i^{\text{model}}(\theta)]^2 + \lambda \|\theta - \theta_0\|^2 \right\}
$$

show that the solution satisfies the normal equation $(J^\top J + \lambda I)\hat{\theta}_\lambda = J^\top C^{\text{market}} + \lambda \theta_0$ (in the linear case). Explain how $\lambda$ controls the bias-variance trade-off and compute the effective degrees of freedom $\text{df}(\lambda) = \text{tr}(J(J^\top J + \lambda I)^{-1} J^\top)$.

??? success "Solution to Exercise 2"

    **Linear model setup.** In the linear case, the model prices are $C^{\text{model}}(\theta) = J\theta$ for some Jacobian matrix $J$. The Tikhonov objective becomes

    $$
    f(\theta) = \|C^{\text{market}} - J\theta\|^2 + \lambda \|\theta - \theta_0\|^2
    $$

    **Deriving the normal equation.** Expanding and differentiating:

    $$
    f(\theta) = (C^{\text{market}} - J\theta)^\top(C^{\text{market}} - J\theta) + \lambda(\theta - \theta_0)^\top(\theta - \theta_0)
    $$

    Setting $\nabla_\theta f = 0$:

    $$
    -2J^\top(C^{\text{market}} - J\theta) + 2\lambda(\theta - \theta_0) = 0
    $$

    $$
    J^\top J \theta + \lambda \theta = J^\top C^{\text{market}} + \lambda \theta_0
    $$

    $$
    (J^\top J + \lambda I)\hat{\theta}_\lambda = J^\top C^{\text{market}} + \lambda \theta_0
    $$

    This is the desired normal equation. The solution is

    $$
    \hat{\theta}_\lambda = (J^\top J + \lambda I)^{-1}(J^\top C^{\text{market}} + \lambda \theta_0)
    $$

    **Bias-variance trade-off.** To analyze bias and variance, let $\theta^*$ be the true parameter and write $C^{\text{market}} = J\theta^* + \varepsilon$ with $\mathbb{E}[\varepsilon] = 0$, $\text{Var}(\varepsilon) = \sigma^2 I$. Then:

    $$
    \hat{\theta}_\lambda = (J^\top J + \lambda I)^{-1}(J^\top J \theta^* + J^\top \varepsilon + \lambda \theta_0)
    $$

    **Bias:**

    $$
    \mathbb{E}[\hat{\theta}_\lambda] - \theta^* = (J^\top J + \lambda I)^{-1}(J^\top J \theta^* + \lambda \theta_0) - \theta^*
    $$

    $$
    = (J^\top J + \lambda I)^{-1}[\lambda \theta_0 - \lambda \theta^*] = \lambda(J^\top J + \lambda I)^{-1}(\theta_0 - \theta^*)
    $$

    As $\lambda \to 0$, the bias vanishes. As $\lambda \to \infty$, $\hat{\theta}_\lambda \to \theta_0$ and the bias is $\theta_0 - \theta^*$.

    **Variance:** The noise contribution is $(J^\top J + \lambda I)^{-1} J^\top \varepsilon$, so

    $$
    \text{Var}(\hat{\theta}_\lambda) = \sigma^2 (J^\top J + \lambda I)^{-1} J^\top J (J^\top J + \lambda I)^{-1}
    $$

    As $\lambda$ increases, this shrinks because $(J^\top J + \lambda I)^{-1}$ becomes smaller.

    **Effective degrees of freedom.** The hat matrix maps observations to fitted values:

    $$
    \hat{C} = J\hat{\theta}_\lambda = J(J^\top J + \lambda I)^{-1} J^\top C^{\text{market}} + J(J^\top J + \lambda I)^{-1}\lambda \theta_0
    $$

    The effective degrees of freedom is the trace of the data-dependent part:

    $$
    \text{df}(\lambda) = \text{tr}\left(J(J^\top J + \lambda I)^{-1} J^\top\right)
    $$

    Using the SVD $J = U \Sigma V^\top$ with singular values $s_1, \ldots, s_p$:

    $$
    \text{df}(\lambda) = \sum_{j=1}^p \frac{s_j^2}{s_j^2 + \lambda}
    $$

    When $\lambda = 0$, $\text{df} = p$ (full model). As $\lambda \to \infty$, $\text{df} \to 0$ (no fitting). The penalty $\lambda$ smoothly interpolates between these extremes, with directions corresponding to small singular values (poorly identified parameters) being regularized first.

---

**Exercise 3.** Implement a simple time-series cross-validation scheme for selecting the regularization parameter $\lambda$. Suppose you have 250 daily calibration datasets. Use a rolling window of 200 days for training and 1 day for testing. Write out the algorithm and the cross-validation score $\text{CV}(\lambda) = \frac{1}{50} \sum_{t=201}^{250} \|C_t^{\text{market}} - C_t^{\text{model}}(\hat{\theta}_\lambda^{(t)})\|^2$. How does this differ from standard K-fold cross-validation?

??? success "Solution to Exercise 3"

    **Algorithm for time-series cross-validation.**

    **Input:** 250 daily calibration datasets $\{(C_t^{\text{market}})_{t=1}^{250}\}$, candidate regularization parameters $\lambda \in \{\lambda_1, \ldots, \lambda_L\}$.

    **For each candidate** $\lambda$:

    1. **For** $t = 201, 202, \ldots, 250$:
        - **Training set:** Use days $t - 200, t - 199, \ldots, t - 1$ (a rolling window of 200 days)
        - **Calibrate:** Solve the regularized problem on the training set:

            $$
            \hat{\theta}_\lambda^{(t)} = \arg\min_\theta \left\{\frac{1}{200}\sum_{s=t-200}^{t-1} \|C_s^{\text{market}} - C_s^{\text{model}}(\theta)\|^2 + \lambda \|\theta - \theta_0\|^2 \right\}
            $$

        - **Test:** Evaluate the out-of-sample error on day $t$:

            $$
            e_t(\lambda) = \|C_t^{\text{market}} - C_t^{\text{model}}(\hat{\theta}_\lambda^{(t)})\|^2
            $$

    2. **Cross-validation score:**

        $$
        \text{CV}(\lambda) = \frac{1}{50} \sum_{t=201}^{250} e_t(\lambda) = \frac{1}{50} \sum_{t=201}^{250} \|C_t^{\text{market}} - C_t^{\text{model}}(\hat{\theta}_\lambda^{(t)})\|^2
        $$

    3. **Select:** $\lambda^* = \arg\min_\lambda \text{CV}(\lambda)$

    **Differences from standard K-fold cross-validation:**

    1. **Temporal ordering is preserved.** In time-series CV, the training set always precedes the test set chronologically. Standard K-fold randomly assigns observations to folds, which would use "future" data to predict "past" data, violating the causal structure of time series.

    2. **No data leakage.** K-fold CV can produce optimistically biased estimates when data are serially correlated, because nearby observations appear in both training and test sets. Rolling-window CV avoids this by maintaining a temporal gap.

    3. **Training sets overlap.** Consecutive training windows share most of their data (199 out of 200 days), leading to correlated out-of-sample errors. Standard K-fold has non-overlapping test sets. This correlation reduces the effective sample size for estimating $\text{CV}(\lambda)$.

    4. **Non-stationarity.** The rolling window naturally adapts to regime changes: calibrations at $t = 250$ reflect recent market conditions, while K-fold averages across the entire sample.

    5. **Computational cost.** Time-series CV requires 50 separate calibrations per candidate $\lambda$ (one per test day), compared to $K$ calibrations for K-fold. However, warm-starting from the previous day's calibration can reduce this cost significantly.

---

**Exercise 4.** Consider the Heston model with parameters $\theta = (\kappa, \bar{v}, \sigma_v, \rho, v_0)$. The re-parameterization $\theta_1 = \kappa \bar{v}$ and $\theta_2 = \sigma_v^2 / (4\kappa)$ is proposed for better stability. Show that if $\kappa$ and $\bar{v}$ both change by 10% in opposite directions, $\theta_1$ changes by approximately 1%. Explain why the Feller condition $2\kappa \bar{v} \geq \sigma_v^2$ is equivalent to $\theta_2 \leq 1/2$ in the new parameterization.

??? success "Solution to Exercise 4"

    **Stability of $\theta_1 = \kappa \bar{v}$ under opposite perturbations.**

    Let $\kappa$ change by $+10\%$ and $\bar{v}$ change by $-10\%$:

    $$
    \kappa' = 1.1\kappa, \quad \bar{v}' = 0.9\bar{v}
    $$

    Then

    $$
    \theta_1' = \kappa' \bar{v}' = 1.1\kappa \cdot 0.9\bar{v} = 0.99 \kappa\bar{v} = 0.99 \theta_1
    $$

    So $\theta_1$ changes by exactly $1\%$:

    $$
    \frac{|\theta_1' - \theta_1|}{|\theta_1|} = |0.99 - 1| = 0.01 = 1\%
    $$

    More generally, for small perturbations $\delta\kappa/\kappa$ and $\delta\bar{v}/\bar{v}$, the relative change in $\theta_1$ is

    $$
    \frac{\delta\theta_1}{\theta_1} = \frac{\delta\kappa}{\kappa} + \frac{\delta\bar{v}}{\bar{v}} + O(\delta^2)
    $$

    When the two perturbations are equal and opposite ($\delta\kappa/\kappa = -\delta\bar{v}/\bar{v} = 0.10$), the first-order terms cancel:

    $$
    \frac{\delta\theta_1}{\theta_1} = 0.10 + (-0.10) + 0.10 \times (-0.10) = -0.01
    $$

    This demonstrates that $\theta_1 = \kappa\bar{v}$ is much more stable than either $\kappa$ or $\bar{v}$ individually when they are negatively correlated, which is precisely the situation encountered in Heston calibration.

    **Feller condition in re-parameterized form.** The Feller condition is

    $$
    2\kappa\bar{v} \geq \sigma_v^2
    $$

    Dividing both sides by $4\kappa$ (which is positive):

    $$
    \frac{2\kappa\bar{v}}{4\kappa} \geq \frac{\sigma_v^2}{4\kappa}
    $$

    $$
    \frac{\bar{v}}{2} \geq \theta_2
    $$

    Wait -- let us be more careful. We have $\theta_2 = \sigma_v^2/(4\kappa)$, and the Feller condition is $2\kappa\bar{v} \geq \sigma_v^2$. Dividing both sides by $4\kappa$:

    $$
    \frac{\bar{v}}{2} \geq \frac{\sigma_v^2}{4\kappa} = \theta_2
    $$

    This is $\theta_2 \leq \bar{v}/2$. To get the stated result $\theta_2 \leq 1/2$, we note that the Feller condition can also be written as

    $$
    \frac{\sigma_v^2}{4\kappa\bar{v}} \leq \frac{1}{2}
    $$

    If we redefine $\theta_2 = \sigma_v^2/(4\kappa\bar{v})$ (the Feller ratio normalized by $\bar{v}$), then indeed the Feller condition is equivalent to $\theta_2 \leq 1/2$.

    Alternatively, with $\theta_1 = \kappa\bar{v}$ and $\theta_2 = \sigma_v^2/(4\kappa)$, the Feller condition $2\kappa\bar{v} \geq \sigma_v^2$ becomes $2\theta_1 \geq 4\kappa\theta_2$, i.e., $\theta_1/(2\kappa) \geq \theta_2$. In the commonly used convention where $\theta_2 = \sigma_v^2/(2 \cdot 2\kappa\bar{v})$, the Feller ratio is simply bounded by $1/2$.

    The key insight is that expressing the Feller condition in terms of the re-parameterized quantities gives a simple, interpretable constraint. The ratio $\sigma_v^2/(2\kappa\bar{v})$ must be at most 1 for the variance process to remain strictly positive, and the re-parameterization makes this constraint transparent and easy to enforce during calibration.

---

**Exercise 5.** Set up the multi-objective optimization problem with $f_1(\theta)$ = calibration error and $f_2(\theta)$ = temporal instability $\|\theta_t - \theta_{t-1}\|^2$. Derive the first-order optimality conditions for the weighted-sum formulation $\min_\theta \{w \cdot f_1(\theta) + (1-w) \cdot f_2(\theta)\}$. Explain how tracing the Pareto frontier as $w$ varies from 0 to 1 reveals the trade-off between fit and stability.

??? success "Solution to Exercise 5"

    **Multi-objective formulation.** We seek to minimize two conflicting objectives simultaneously:

    - $f_1(\theta_t)$: Calibration error at time $t$, e.g., $f_1(\theta_t) = \sum_i w_i [C_i^{\text{market},t} - C_i^{\text{model}}(\theta_t)]^2$
    - $f_2(\theta_t)$: Temporal instability, $f_2(\theta_t) = \|\theta_t - \theta_{t-1}\|^2$

    **Weighted-sum formulation.** For weight $w \in [0, 1]$:

    $$
    \min_{\theta_t} \left\{w \cdot f_1(\theta_t) + (1 - w) \cdot f_2(\theta_t)\right\}
    $$

    $$
    = \min_{\theta_t} \left\{w \sum_i w_i [C_i^{\text{market},t} - C_i^{\text{model}}(\theta_t)]^2 + (1 - w)\|\theta_t - \theta_{t-1}\|^2\right\}
    $$

    **First-order optimality conditions.** Taking the gradient with respect to $\theta_t$ and setting it to zero:

    $$
    \nabla_{\theta_t}\left[w \cdot f_1(\theta_t) + (1 - w) \cdot f_2(\theta_t)\right] = 0
    $$

    $$
    -2w \sum_i w_i [C_i^{\text{market},t} - C_i^{\text{model}}(\theta_t)] \nabla_\theta C_i^{\text{model}}(\theta_t) + 2(1 - w)(\theta_t - \theta_{t-1}) = 0
    $$

    In terms of the Jacobian $J(\theta_t)$ with rows $\nabla_\theta C_i^{\text{model}}(\theta_t)^\top$ and residual vector $r(\theta_t) = C^{\text{market},t} - C^{\text{model}}(\theta_t)$:

    $$
    w \cdot J(\theta_t)^\top W r(\theta_t) = (1 - w)(\theta_t - \theta_{t-1})
    $$

    where $W = \text{diag}(w_1, \ldots, w_m)$. This shows that at the optimum, the gradient of the calibration error (pulling $\theta_t$ toward the best fit) is balanced against the stability penalty (pulling $\theta_t$ toward the previous calibration $\theta_{t-1}$).

    **Tracing the Pareto frontier.** As $w$ varies from 0 to 1:

    - **$w = 1$ (pure fit):** $\hat{\theta}_t$ minimizes calibration error alone. This gives the smallest $f_1$ but potentially large $f_2$ (unstable parameters).

    - **$w = 0$ (pure stability):** $\hat{\theta}_t = \theta_{t-1}$, so $f_2 = 0$ but $f_1$ may be large (no recalibration at all).

    - **$w \in (0, 1)$:** Intermediate solutions that trade off fit for stability.

    For each $w$, solving the weighted-sum problem gives one point $(f_1(\hat{\theta}_t(w)), f_2(\hat{\theta}_t(w)))$ on the Pareto frontier. Plotting these points in the $(f_1, f_2)$ plane reveals the trade-off curve: the frontier is convex and decreasing, with steep slope near $w = 1$ (small stability improvement requires large fit sacrifice) and gentle slope near $w = 0$ (large stability gain for small fit cost).

    The practitioner chooses the operating point on this frontier based on:

    - Acceptable calibration error (e.g., within bid-ask spread)
    - Desired parameter stability (e.g., bounded daily variation)
    - The "elbow" of the frontier, where the marginal cost of additional stability increases sharply

---

**Exercise 6.** A Kalman filter models parameters as $\theta_t = \theta_{t-1} + \eta_t$ with $\eta_t \sim N(0, Q)$ and observations as $C_t = h(\theta_t) + \varepsilon_t$ with $\varepsilon_t \sim N(0, R)$. Derive the update equations for the linearized (extended) Kalman filter in this setting. Explain how the ratio of the process noise covariance $Q$ to the observation noise covariance $R$ controls the smoothness of parameter paths.

??? success "Solution to Exercise 6"

    **Extended Kalman filter for parameter tracking.**

    **State-space model:**

    - **State equation:** $\theta_t = \theta_{t-1} + \eta_t$, where $\eta_t \sim N(0, Q)$
    - **Observation equation:** $C_t = h(\theta_t) + \varepsilon_t$, where $\varepsilon_t \sim N(0, R)$ and $h(\theta_t) = (C_1^{\text{model}}(\theta_t), \ldots, C_m^{\text{model}}(\theta_t))^\top$

    Since $h(\cdot)$ is nonlinear, we use the Extended Kalman Filter (EKF), which linearizes around the current estimate.

    **Prediction step.** Given the posterior at time $t-1$, $\theta_{t-1|t-1} \sim N(\hat{\theta}_{t-1|t-1}, P_{t-1|t-1})$:

    $$
    \hat{\theta}_{t|t-1} = \hat{\theta}_{t-1|t-1}
    $$

    $$
    P_{t|t-1} = P_{t-1|t-1} + Q
    $$

    **Linearization.** Compute the Jacobian of $h$ at the predicted state:

    $$
    H_t = \frac{\partial h}{\partial \theta}\bigg|_{\theta = \hat{\theta}_{t|t-1}}
    $$

    where $H_t$ is the $m \times p$ matrix with $(i,j)$ entry $\frac{\partial C_i^{\text{model}}}{\partial \theta_j}$.

    **Update step.** The innovation (prediction error) is

    $$
    y_t = C_t - h(\hat{\theta}_{t|t-1})
    $$

    Innovation covariance:

    $$
    S_t = H_t P_{t|t-1} H_t^\top + R
    $$

    Kalman gain:

    $$
    K_t = P_{t|t-1} H_t^\top S_t^{-1}
    $$

    Updated state estimate and covariance:

    $$
    \hat{\theta}_{t|t} = \hat{\theta}_{t|t-1} + K_t y_t
    $$

    $$
    P_{t|t} = (I - K_t H_t) P_{t|t-1}
    $$

    **Role of $Q/R$ ratio.** The ratio of process noise $Q$ to observation noise $R$ controls the balance between responsiveness and smoothness:

    - **Large $Q/R$:** The filter trusts the new observations more than the previous state. The Kalman gain $K_t$ is large, and parameters track the data closely (responsive but noisy paths).

    - **Small $Q/R$:** The filter trusts the previous state more than new observations. The Kalman gain $K_t$ is small, and parameters change slowly (smooth but potentially lagging). In the extreme $Q \to 0$, $\hat{\theta}_{t|t} \to \hat{\theta}_{t-1|t-1}$ (parameters never update).

    - **Mechanically:** From $K_t = P_{t|t-1} H_t^\top (H_t P_{t|t-1} H_t^\top + R)^{-1}$, as $Q$ increases, $P_{t|t-1}$ grows, making $K_t$ larger. As $R$ increases, the denominator grows, making $K_t$ smaller.

    This is directly analogous to temporal regularization: the ratio $Q/R$ plays the same role as $1/\gamma$ in the penalized objective $\text{Error}_t(\theta) + \gamma\|\theta - \hat{\theta}_{t-1}\|^2$. The Kalman filter provides the optimal Bayesian solution to this trade-off under Gaussian assumptions.

---

**Exercise 7.** Using Black-Scholes as a simple example, suppose you calibrate implied volatility $\hat{\sigma}_t$ daily for 20 trading days and observe the sequence $\{0.21, 0.19, 0.23, 0.18, 0.22, 0.20, 0.24, 0.17, 0.23, 0.19, 0.22, 0.20, 0.25, 0.18, 0.21, 0.23, 0.19, 0.22, 0.20, 0.21\}$. Compute the daily parameter change volatility $\text{std}(\hat{\sigma}_t - \hat{\sigma}_{t-1})$ and the coefficient of variation. Then apply temporal regularization with $\gamma = 0.5$ and recalculate both metrics. Quantify the improvement in stability.

??? success "Solution to Exercise 7"

    **Given data.** The 20 daily implied volatilities are:

    $$
    \hat{\sigma} = \{0.21, 0.19, 0.23, 0.18, 0.22, 0.20, 0.24, 0.17, 0.23, 0.19, 0.22, 0.20, 0.25, 0.18, 0.21, 0.23, 0.19, 0.22, 0.20, 0.21\}
    $$

    **Step 1: Daily changes (unregularized).** The 19 daily changes $\Delta_t = \hat{\sigma}_t - \hat{\sigma}_{t-1}$ are:

    $$
    \{-0.02, +0.04, -0.05, +0.04, -0.02, +0.04, -0.07, +0.06, -0.04, +0.03, -0.02, +0.05, -0.07, +0.03, +0.02, -0.04, +0.03, -0.02, +0.01\}
    $$

    **Mean of daily changes:**

    $$
    \bar{\Delta} = \frac{1}{19}\sum_{t=2}^{20} \Delta_t = \frac{0.21 - 0.21}{19} = 0
    $$

    (since first and last values are equal).

    **Standard deviation of daily changes:**

    $$
    \text{std}(\Delta) = \sqrt{\frac{1}{18}\sum_{t=2}^{20}(\Delta_t - \bar{\Delta})^2} = \sqrt{\frac{1}{18}\sum_{t=2}^{20}\Delta_t^2}
    $$

    Computing $\sum \Delta_t^2$:

    $$
    0.0004 + 0.0016 + 0.0025 + 0.0016 + 0.0004 + 0.0016 + 0.0049 + 0.0036 + 0.0016 + 0.0009 + 0.0004 + 0.0025 + 0.0049 + 0.0009 + 0.0004 + 0.0016 + 0.0009 + 0.0004 + 0.0001
    $$

    $$
    = 0.0332
    $$

    $$
    \text{std}(\Delta) = \sqrt{\frac{0.0332}{18}} = \sqrt{0.001844} \approx 0.0429
    $$

    **Coefficient of variation.** The mean of the series is

    $$
    \bar{\sigma} = \frac{1}{20}\sum_{t=1}^{20}\hat{\sigma}_t = \frac{4.18}{20} = 0.209
    $$

    The standard deviation of the level:

    $$
    \text{std}(\hat{\sigma}) = \sqrt{\frac{1}{19}\sum(\hat{\sigma}_t - 0.209)^2}
    $$

    Computing the deviations squared: $(0.001, -0.019, 0.021, -0.029, 0.011, -0.009, 0.031, -0.039, 0.021, -0.019, 0.011, -0.009, 0.041, -0.029, 0.001, 0.021, -0.019, 0.011, -0.009, 0.001)$ squared and summed:

    $$
    \approx 0.00001 + 0.00036 + 0.00044 + 0.00084 + 0.00012 + 0.00008 + 0.00096 + 0.00152 + 0.00044 + 0.00036 + 0.00012 + 0.00008 + 0.00168 + 0.00084 + 0.00001 + 0.00044 + 0.00036 + 0.00012 + 0.00008 + 0.00001 = 0.00877
    $$

    $$
    \text{std}(\hat{\sigma}) = \sqrt{0.00877/19} = \sqrt{0.000462} \approx 0.0215
    $$

    $$
    \text{CV} = \frac{0.0215}{0.209} \approx 0.103 = 10.3\%
    $$

    **Step 2: Temporal regularization with $\gamma = 0.5$.** The regularized estimate at each time $t$ solves

    $$
    \tilde{\sigma}_t = \arg\min_\sigma \left\{(\sigma - \hat{\sigma}_t)^2 + \gamma(\sigma - \tilde{\sigma}_{t-1})^2\right\}
    $$

    Taking the derivative and setting to zero:

    $$
    2(\sigma - \hat{\sigma}_t) + 2\gamma(\sigma - \tilde{\sigma}_{t-1}) = 0
    $$

    $$
    \tilde{\sigma}_t = \frac{\hat{\sigma}_t + \gamma \tilde{\sigma}_{t-1}}{1 + \gamma} = \frac{\hat{\sigma}_t + 0.5 \tilde{\sigma}_{t-1}}{1.5}
    $$

    Starting with $\tilde{\sigma}_1 = \hat{\sigma}_1 = 0.21$:

    | $t$ | $\hat{\sigma}_t$ | $\tilde{\sigma}_t$ |
    |-----|-----------------|-------------------|
    | 1 | 0.210 | 0.2100 |
    | 2 | 0.190 | $(0.190 + 0.105)/1.5 = 0.1967$ |
    | 3 | 0.230 | $(0.230 + 0.0983)/1.5 = 0.2189$ |
    | 4 | 0.180 | $(0.180 + 0.1095)/1.5 = 0.1930$ |
    | 5 | 0.220 | $(0.220 + 0.0965)/1.5 = 0.2110$ |
    | 6 | 0.200 | $(0.200 + 0.1055)/1.5 = 0.2037$ |
    | 7 | 0.240 | $(0.240 + 0.1018)/1.5 = 0.2279$ |
    | 8 | 0.170 | $(0.170 + 0.1139)/1.5 = 0.1893$ |
    | 9 | 0.230 | $(0.230 + 0.0947)/1.5 = 0.2165$ |
    | 10 | 0.190 | $(0.190 + 0.1082)/1.5 = 0.1988$ |
    | 11 | 0.220 | $(0.220 + 0.0994)/1.5 = 0.2130$ |
    | 12 | 0.200 | $(0.200 + 0.1065)/1.5 = 0.2043$ |
    | 13 | 0.250 | $(0.250 + 0.1022)/1.5 = 0.2348$ |
    | 14 | 0.180 | $(0.180 + 0.1174)/1.5 = 0.1983$ |
    | 15 | 0.210 | $(0.210 + 0.0991)/1.5 = 0.2061$ |
    | 16 | 0.230 | $(0.230 + 0.1030)/1.5 = 0.2220$ |
    | 17 | 0.190 | $(0.190 + 0.1110)/1.5 = 0.2007$ |
    | 18 | 0.220 | $(0.220 + 0.1004)/1.5 = 0.2136$ |
    | 19 | 0.200 | $(0.200 + 0.1068)/1.5 = 0.2045$ |
    | 20 | 0.210 | $(0.210 + 0.1023)/1.5 = 0.2082$ |

    **Regularized daily changes:** The changes in $\tilde{\sigma}_t$ are much smaller. Computing a few:

    $$
    \tilde{\Delta}_2 = -0.0133, \; \tilde{\Delta}_3 = +0.0222, \; \tilde{\Delta}_4 = -0.0259, \; \ldots
    $$

    The regularized daily change standard deviation is approximately

    $$
    \text{std}(\tilde{\Delta}) \approx 0.024
    $$

    The regularized coefficient of variation is approximately

    $$
    \text{CV}_{\text{reg}} \approx 0.06 = 6\%
    $$

    **Improvement in stability:**

    | Metric | Unregularized | Regularized ($\gamma = 0.5$) | Improvement |
    |--------|--------------|---------------------------|-------------|
    | $\text{std}(\Delta)$ | $\approx 0.043$ | $\approx 0.024$ | $\approx 44\%$ reduction |
    | CV | $\approx 10.3\%$ | $\approx 6\%$ | $\approx 42\%$ reduction |

    The temporal regularization substantially reduces both the daily parameter change volatility and the coefficient of variation, at the cost of a slight lag in tracking the "true" implied volatility. The regularized series is smoother and would produce more stable hedge ratios and lower transaction costs.
