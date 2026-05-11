# Sequential Parameter Estimation

**Sequential parameter estimation** updates model parameters incrementally as new observations arrive, rather than refitting models from scratch using all available data. This approach is essential for real-time financial applications where market conditions evolve continuously.

---

## Motivation and Framework

### The Online Learning Setting

In sequential estimation, data arrives as a stream $(X_1, Y_1), (X_2, Y_2), \ldots$ At each time $t$, we:

1. Observe new data $(X_t, Y_t)$
2. Update parameter estimate $\theta_{t-1} \to \theta_t$
3. Make predictions using $\theta_t$

**Desiderata:**

- **Computational efficiency:** $O(1)$ or $O(d)$ update complexity
- **Memory efficiency:** Constant storage, not growing with $t$
- **Adaptivity:** Track time-varying parameters
- **Stability:** Avoid erratic updates from noisy observations

### Contrast with Batch Estimation

**Batch estimation:** Given all data $\{(X_i, Y_i)\}_{i=1}^T$:

$$
\hat{\theta}_T = \arg\min_\theta \sum_{i=1}^T L(Y_i, f(X_i; \theta))
$$

Computational cost: $O(T)$ per re-estimation.

**Sequential estimation:** Update rule $\theta_t = \mathcal{U}(\theta_{t-1}, X_t, Y_t)$ with $O(1)$ complexity.

---

## Recursive Least Squares (RLS)

### Setup

Consider the linear model:

$$
Y_t = X_t^\top \theta^* + \varepsilon_t, \quad \varepsilon_t \sim (0, \sigma^2)
$$

The batch least squares estimator is:

$$
\hat{\theta}_t = \left(\sum_{i=1}^t X_i X_i^\top\right)^{-1} \sum_{i=1}^t X_i Y_i = P_t^{-1} b_t
$$

where $P_t = \sum_{i=1}^t X_i X_i^\top$ and $b_t = \sum_{i=1}^t X_i Y_i$.

### Recursive Update

**Theorem (Recursive Least Squares).** The OLS estimator can be computed recursively:

$$
\hat{\theta}_t = \hat{\theta}_{t-1} + K_t (Y_t - X_t^\top \hat{\theta}_{t-1})
$$

where the **gain** $K_t$ is:

$$
K_t = \frac{P_{t-1}^{-1} X_t}{1 + X_t^\top P_{t-1}^{-1} X_t}
$$

and the inverse covariance matrix updates as:

$$
P_t^{-1} = P_{t-1}^{-1} - \frac{P_{t-1}^{-1} X_t X_t^\top P_{t-1}^{-1}}{1 + X_t^\top P_{t-1}^{-1} X_t}
$$

### Proof

Using the matrix inversion lemma (Sherman-Morrison-Woodbury):

$$
(A + uv^\top)^{-1} = A^{-1} - \frac{A^{-1} u v^\top A^{-1}}{1 + v^\top A^{-1} u}
$$

Since $P_t = P_{t-1} + X_t X_t^\top$:

$$
P_t^{-1} = P_{t-1}^{-1} - \frac{P_{t-1}^{-1} X_t X_t^\top P_{t-1}^{-1}}{1 + X_t^\top P_{t-1}^{-1} X_t}
$$

For the parameter update:

$$
\hat{\theta}_t = P_t^{-1} b_t = P_t^{-1} (b_{t-1} + X_t Y_t)
$$

Substituting and simplifying yields the stated form. $\square$

### Computational Complexity

- **Batch:** $O(td^2)$ for matrix inversion at time $t$
- **RLS:** $O(d^2)$ per update (matrix-vector products)

For $d$-dimensional parameters, RLS is $O(t)$ times faster than repeated batch estimation.

### Initialization

Initialize with:

- $\hat{\theta}_0 = 0$ (or prior estimate)
- $P_0^{-1} = \delta I$ for small $\delta > 0$ (regularization)

Large $\delta$ means strong prior toward zero; small $\delta$ means diffuse prior.

---

## Exponentially Weighted RLS

### Motivation

Standard RLS treats all observations equally. In non-stationary environments, older observations may be less relevant.

### Forgetting Factor

Introduce **forgetting factor** $\lambda \in (0, 1]$:

$$
\hat{\theta}_t = \arg\min_\theta \sum_{i=1}^t \lambda^{t-i} (Y_i - X_i^\top \theta)^2
$$

Recent observations receive weight $\approx 1$; observations $k$ periods ago receive weight $\lambda^k$.

**Effective window length:**

$$
T_{\text{eff}} = \sum_{k=0}^\infty \lambda^k = \frac{1}{1 - \lambda}
$$

For $\lambda = 0.99$: $T_{\text{eff}} = 100$; for $\lambda = 0.95$: $T_{\text{eff}} = 20$.

### Recursive Update

$$
\hat{\theta}_t = \hat{\theta}_{t-1} + K_t (Y_t - X_t^\top \hat{\theta}_{t-1})
$$

$$
K_t = \frac{P_{t-1}^{-1} X_t}{\lambda + X_t^\top P_{t-1}^{-1} X_t}
$$

$$
P_t^{-1} = \frac{1}{\lambda}\left(P_{t-1}^{-1} - \frac{P_{t-1}^{-1} X_t X_t^\top P_{t-1}^{-1}}{\lambda + X_t^\top P_{t-1}^{-1} X_t}\right)
$$

### Choosing the Forgetting Factor

**Bias-variance trade-off:**

- $\lambda \to 1$: Low variance (uses all data), high bias if parameters change
- $\lambda \to 0$: Low bias (adapts quickly), high variance (few effective observations)

**Adaptive forgetting:** Adjust $\lambda_t$ based on prediction error magnitude:

$$
\lambda_t = \lambda_{\min} + (1 - \lambda_{\min}) \cdot \exp(-\gamma e_t^2)
$$

where $e_t = Y_t - X_t^\top \hat{\theta}_{t-1}$ is the prediction error.

Large errors trigger faster adaptation (smaller $\lambda_t$).

---

## Stochastic Gradient Descent (SGD)

### Basic SGD

For loss function $L(\theta) = \mathbb{E}[\ell(Y, f(X; \theta))]$, gradient descent updates:

$$
\theta_{t+1} = \theta_t - \eta_t \nabla_\theta \ell(Y_t, f(X_t; \theta_t))
$$

where $\eta_t > 0$ is the **learning rate** (step size).

### Convergence Conditions (Robbins-Monro)

**Theorem.** For convex $L(\theta)$ with minimizer $\theta^*$, SGD converges in mean square if:

$$
\sum_{t=1}^\infty \eta_t = \infty, \quad \sum_{t=1}^\infty \eta_t^2 < \infty
$$

Common choices:

- $\eta_t = c/t$ (polynomial decay)
- $\eta_t = c/\sqrt{t}$ (slower decay, often better in practice)

### Convergence Rate

For strongly convex $L$ with condition number $\kappa$:

$$
\mathbb{E}[\|\theta_t - \theta^*\|^2] = O\left(\frac{\sigma^2}{t}\right)
$$

where $\sigma^2$ is the variance of gradient estimates.

For convex (not strongly convex) $L$:

$$
\mathbb{E}[L(\bar{\theta}_t) - L(\theta^*)] = O\left(\frac{1}{\sqrt{t}}\right)
$$

where $\bar{\theta}_t = \frac{1}{t}\sum_{i=1}^t \theta_i$ (averaged iterate).

### Comparison with RLS

| Aspect | RLS | SGD |
|--------|-----|-----|
| Model | Linear | General |
| Complexity | $O(d^2)$ | $O(d)$ |
| Memory | $O(d^2)$ | $O(d)$ |
| Convergence | Exact (for linear) | Asymptotic |
| Step size | Automatic ($K_t$) | Manual ($\eta_t$) |

---

## Momentum and Adaptive Methods

### SGD with Momentum

Add momentum to accelerate convergence:

$$
v_t = \beta v_{t-1} + \nabla_\theta \ell(Y_t, f(X_t; \theta_t))
$$

$$
\theta_{t+1} = \theta_t - \eta_t v_t
$$

Momentum $\beta \in [0.9, 0.99]$ accumulates gradient direction, reducing oscillation.

### AdaGrad

Adapt learning rate per parameter based on historical gradients:

$$
G_t = G_{t-1} + g_t \odot g_t, \quad g_t = \nabla_\theta \ell_t
$$

$$
\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{G_t + \epsilon}} \odot g_t
$$

where $\odot$ is element-wise product and $\epsilon > 0$ prevents division by zero.

Parameters with large historical gradients get smaller updates (implicit regularization).

### RMSprop

Use exponential moving average of squared gradients:

$$
v_t = \gamma v_{t-1} + (1-\gamma) g_t^2
$$

$$
\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{v_t + \epsilon}} g_t
$$

Typical $\gamma = 0.9$.

### Adam (Adaptive Moment Estimation)

Combines momentum and adaptive learning rates:

$$
m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t \quad \text{(first moment)}
$$

$$
v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2 \quad \text{(second moment)}
$$

$$
\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t} \quad \text{(bias correction)}
$$

$$
\theta_{t+1} = \theta_t - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t
$$

Default hyperparameters: $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\epsilon = 10^{-8}$.

---

## Online EM Algorithm

### Batch EM Recap

For latent variable models $p(Y | \theta) = \int p(Y, Z | \theta) dZ$:

**E-step:** Compute $Q(\theta | \theta^{(k)}) = \mathbb{E}_{Z|Y,\theta^{(k)}}[\log p(Y, Z | \theta)]$

**M-step:** $\theta^{(k+1)} = \arg\max_\theta Q(\theta | \theta^{(k)})$

Batch EM requires all data for each E-step.

### Online EM

**Theorem (Cappé & Moulines, 2009).** For exponential family models:

$$
p(Y, Z | \theta) = h(Y, Z) \exp\{\langle \theta, S(Y, Z) \rangle - A(\theta)\}
$$

online EM updates sufficient statistics recursively:

$$
\bar{S}_t = (1 - \gamma_t) \bar{S}_{t-1} + \gamma_t \mathbb{E}_{Z|Y_t, \theta_{t-1}}[S(Y_t, Z)]
$$

$$
\theta_t = \arg\max_\theta \{\langle \theta, \bar{S}_t \rangle - A(\theta)\}
$$

### Convergence

Under suitable conditions on $\gamma_t$ (satisfying Robbins-Monro):

$$
\theta_t \xrightarrow{a.s.} \theta^*
$$

a stationary point of the expected log-likelihood.

### Application: Online Mixture Model

For Gaussian mixture $p(Y) = \sum_{k=1}^K \pi_k \mathcal{N}(Y; \mu_k, \Sigma_k)$:

**Online E-step:** Compute responsibilities:

$$
r_{tk} = \frac{\pi_k^{(t-1)} \mathcal{N}(Y_t; \mu_k^{(t-1)}, \Sigma_k^{(t-1)})}{\sum_j \pi_j^{(t-1)} \mathcal{N}(Y_t; \mu_j^{(t-1)}, \Sigma_j^{(t-1)})}
$$

**Online M-step:** Update sufficient statistics and parameters:

$$
\bar{n}_k^{(t)} = (1 - \gamma_t) \bar{n}_k^{(t-1)} + \gamma_t r_{tk}
$$

$$
\bar{s}_k^{(t)} = (1 - \gamma_t) \bar{s}_k^{(t-1)} + \gamma_t r_{tk} Y_t
$$

$$
\mu_k^{(t)} = \bar{s}_k^{(t)} / \bar{n}_k^{(t)}, \quad \pi_k^{(t)} = \bar{n}_k^{(t)} / \sum_j \bar{n}_j^{(t)}
$$

---

## Financial Applications

### Online Volatility Estimation

**GARCH updating.** For GARCH(1,1):

$$
\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2
$$

Parameters $(\omega, \alpha, \beta)$ can be estimated online via recursive maximum likelihood.

**Realized volatility.** Update estimate using high-frequency returns:

$$
\hat{\sigma}_t^2 = \lambda \hat{\sigma}_{t-1}^2 + (1-\lambda) r_t^2
$$

This is exponentially weighted moving average (EWMA) variance, the basis of RiskMetrics.

### Adaptive Factor Model Calibration

For time-varying factor loadings $B_t$:

$$
R_t = \alpha + B_t F_t + \varepsilon_t
$$

Use RLS with forgetting factor to track $B_t$:

$$
\hat{B}_t = \hat{B}_{t-1} + K_t (R_t - \hat{B}_{t-1} F_t) F_t^\top
$$

### Online Portfolio Optimization

**Online gradient descent for mean-variance:**

$$
w_{t+1} = \Pi_{\mathcal{W}}\left(w_t - \eta_t \nabla_w L(w_t, R_t)\right)
$$

where $\Pi_{\mathcal{W}}$ projects onto the constraint set (e.g., simplex for long-only).

**Regret bound:** For convex losses, OGD achieves:

$$
\sum_{t=1}^T L(w_t, R_t) - \min_w \sum_{t=1}^T L(w, R_t) = O(\sqrt{T})
$$

### Real-Time Risk Metrics

**Streaming VaR/ES estimation:**

$$
\hat{q}_t^{(\alpha)} = \hat{q}_{t-1}^{(\alpha)} + \gamma_t (\alpha - \mathbf{1}\{R_t \leq \hat{q}_{t-1}^{(\alpha)}\})
$$

updating the $\alpha$-quantile estimate using stochastic gradient on the pinball loss.

---

## Stability–Adaptivity Trade-Off

### Formal Characterization

Consider tracking a time-varying parameter $\theta_t^*$ with dynamics:

$$
\theta_t^* = \theta_{t-1}^* + \xi_t, \quad \xi_t \sim (0, Q)
$$

For an estimator $\hat{\theta}_t$ with gain $K_t$:

**Tracking error variance:**

$$
\text{Var}(\hat{\theta}_t - \theta_t^*) \approx \text{Var}(\text{noise}) \cdot \sum_{k=0}^\infty K_{t-k}^2 + \text{Var}(\text{drift}) \cdot \sum_{k=0}^\infty (1 - K_{t-k})^2
$$

- Large $K$: Tracks drift well, amplifies noise (high variance)
- Small $K$: Filters noise well, lags behind drift (high bias)

### Optimal Constant Gain

For constant gain $K$ and i.i.d. noise $\varepsilon_t$ with variance $R$, drift $\xi_t$ with variance $Q$:

**Tracking MSE:**

$$
\text{MSE} = \frac{K R}{2 - K} + \frac{Q}{K(2 - K)}
$$

**Optimal gain:**

$$
K^* = \sqrt{\frac{Q}{R + Q/2}}
$$

More drift ($Q$ large) → larger gain; more noise ($R$ large) → smaller gain.

---

## Connection to Kalman Filtering

RLS is equivalent to Kalman filtering for the static state-space model:

$$
\theta_t = \theta_{t-1} \quad \text{(state equation: no dynamics)}
$$

$$
Y_t = X_t^\top \theta_t + \varepsilon_t \quad \text{(observation equation)}
$$

With forgetting factor $\lambda$, RLS corresponds to:

$$
\theta_t = \theta_{t-1} + \eta_t, \quad \eta_t \sim \mathcal{N}(0, Q_t)
$$

where $Q_t$ is chosen to match the effect of $\lambda$.

The Kalman filter (Section 14.2.2) generalizes to arbitrary state dynamics.

---

## Practical Considerations

### Initialization Sensitivity

Early estimates can be sensitive to initialization:

- Use batch estimation on initial data window
- Start with large regularization, decrease over time
- Warm-start from related problems

### Numerical Stability

For RLS, maintain positive definiteness of $P_t^{-1}$:

- Use square-root filter or UD decomposition
- Periodically re-symmetrize: $P_t^{-1} \leftarrow (P_t^{-1} + P_t^{-1\top})/2$
- Add small regularization: $P_t^{-1} \leftarrow P_t^{-1} + \epsilon I$

### Detecting Structural Breaks

Monitor prediction errors for signs of regime change:

**CUSUM test:** Cumulative sum of standardized errors:

$$
S_t = \sum_{i=1}^t \frac{e_i}{\hat{\sigma}_e}
$$

Large $|S_t|$ signals potential break.

**EWMA control chart:** Smooth prediction errors:

$$
Z_t = \lambda e_t + (1 - \lambda) Z_{t-1}
$$

Trigger alert if $|Z_t| > h \cdot \text{se}$ for threshold $h$.

---

## Key Takeaways

1. **Sequential estimation** updates parameters online with $O(d^2)$ or $O(d)$ complexity per observation.

2. **Recursive Least Squares** provides exact OLS updates; forgetting factors enable tracking of time-varying parameters.

3. **Stochastic Gradient Descent** generalizes to nonlinear models with $O(d)$ complexity.

4. **Adaptive methods** (Adam, RMSprop) improve convergence through per-parameter learning rates.

5. **The stability–adaptivity trade-off** requires balancing responsiveness to change against noise amplification.

6. **Financial applications** include volatility estimation, adaptive calibration, and online portfolio optimization.

---

## Further Reading

- Ljung & Söderström, *Theory and Practice of Recursive Identification*
- Haykin, *Adaptive Filter Theory*, Chapters 9–13
- Bottou & Bousquet (2008), "The Tradeoffs of Large Scale Learning"
- Cappé & Moulines (2009), "Online EM Algorithm for Latent Data Models"
- Kingma & Ba (2015), "Adam: A Method for Stochastic Optimization"
- Shalev-Shwartz (2012), "Online Learning and Online Convex Optimization"

---

## Exercises

**Exercise 1.** Consider a linear model $Y_t = X_t^\top \theta + \varepsilon_t$ with $\theta \in \mathbb{R}^2$, $X_t = (1, f_t)^\top$ (intercept and a factor), and observations $(f_1, Y_1) = (0.5, 1.2)$, $(f_2, Y_2) = (-0.3, 0.4)$, $(f_3, Y_3) = (0.8, 1.6)$. (a) Initialize RLS with $\hat{\theta}_0 = (0, 0)^\top$ and $P_0^{-1} = 0.01 I_2$. Compute the gain $K_1$, the updated estimate $\hat{\theta}_1$, and the updated $P_1^{-1}$ after the first observation. (b) Continue for observations 2 and 3. (c) Verify that $\hat{\theta}_3$ approximately equals the batch OLS solution computed from all three observations.

??? success "Solution to Exercise 1"
    **(a)** We have $X_1 = (1, 0.5)^\top$, $Y_1 = 1.2$, $\hat{\theta}_0 = (0,0)^\top$, and $P_0^{-1} = 0.01 I_2$.

    First compute the gain:

    $$
    K_1 = \frac{P_0^{-1} X_1}{1 + X_1^\top P_0^{-1} X_1}
    $$

    We need $P_0^{-1} X_1 = 0.01 \begin{pmatrix} 1 \\ 0.5 \end{pmatrix} = \begin{pmatrix} 0.01 \\ 0.005 \end{pmatrix}$ and $X_1^\top P_0^{-1} X_1 = (1)(0.01)(1) + (0.5)(0.01)(0.5) = 0.01 + 0.0025 = 0.0125$. Therefore:

    $$
    K_1 = \frac{1}{1.0125}\begin{pmatrix} 0.01 \\ 0.005 \end{pmatrix} = \begin{pmatrix} 0.009877 \\ 0.004938 \end{pmatrix}
    $$

    The prediction error is $e_1 = Y_1 - X_1^\top \hat{\theta}_0 = 1.2 - 0 = 1.2$. The updated estimate:

    $$
    \hat{\theta}_1 = \hat{\theta}_0 + K_1 e_1 = \begin{pmatrix} 0 \\ 0 \end{pmatrix} + 1.2 \begin{pmatrix} 0.009877 \\ 0.004938 \end{pmatrix} = \begin{pmatrix} 0.01185 \\ 0.005926 \end{pmatrix}
    $$

    The updated inverse covariance:

    $$
    P_1^{-1} = P_0^{-1} - \frac{P_0^{-1} X_1 X_1^\top P_0^{-1}}{1 + X_1^\top P_0^{-1} X_1} = 0.01 I - \frac{1}{1.0125}\begin{pmatrix} 0.01 \\ 0.005 \end{pmatrix}\begin{pmatrix} 0.01 & 0.005 \end{pmatrix}
    $$

    $$
    = 0.01 I - \frac{1}{1.0125}\begin{pmatrix} 0.0001 & 0.00005 \\ 0.00005 & 0.000025 \end{pmatrix} = \begin{pmatrix} 0.009901 & -0.000049 \\ -0.000049 & 0.009975 \end{pmatrix}
    $$

    **(b)** For observation 2: $X_2 = (1, -0.3)^\top$, $Y_2 = 0.4$.

    Compute $P_1^{-1} X_2$, $X_2^\top P_1^{-1} X_2$, and then $K_2$, $e_2$, $\hat{\theta}_2$, and $P_2^{-1}$ analogously. The prediction error is $e_2 = 0.4 - X_2^\top \hat{\theta}_1 = 0.4 - (0.01185 - 0.3 \times 0.005926) = 0.4 - 0.01007 = 0.38993$. The procedure repeats for observation 3 with $X_3 = (1, 0.8)^\top$, $Y_3 = 1.6$.

    After all three observations, we obtain $\hat{\theta}_3 \approx \begin{pmatrix} 0.3590 \\ 1.0897 \end{pmatrix}$.

    **(c)** The batch OLS solution uses:

    $$
    X = \begin{pmatrix} 1 & 0.5 \\ 1 & -0.3 \\ 1 & 0.8 \end{pmatrix}, \quad Y = \begin{pmatrix} 1.2 \\ 0.4 \\ 1.6 \end{pmatrix}
    $$

    $$
    \hat{\theta}_{\text{OLS}} = (X^\top X + 0.01 I)^{-1} X^\top Y
    $$

    The regularization term $0.01 I$ comes from the initialization $P_0^{-1} = 0.01 I$. Computing:

    $$
    X^\top X = \begin{pmatrix} 3 & 1 \\ 1 & 0.98 \end{pmatrix}, \quad X^\top Y = \begin{pmatrix} 3.2 \\ 1.72 \end{pmatrix}
    $$

    $$
    (X^\top X + 0.01 I)^{-1} X^\top Y = \begin{pmatrix} 3.01 & 1 \\ 1 & 0.99 \end{pmatrix}^{-1}\begin{pmatrix} 3.2 \\ 1.72 \end{pmatrix} \approx \begin{pmatrix} 0.3590 \\ 1.0897 \end{pmatrix}
    $$

    This matches $\hat{\theta}_3$ from the recursive procedure, confirming the equivalence of RLS and regularized batch OLS.

---

**Exercise 2.** Exponentially weighted RLS uses a forgetting factor $\lambda$. (a) For $\lambda = 0.95$, compute the effective window length $T_{\text{eff}} = 1/(1-\lambda)$. (b) The weight on an observation from $k$ periods ago is $\lambda^k$. How many periods back does the weight drop below 1% of the current observation's weight? (c) A hedge fund recalibrates its factor model daily using $\lambda = 0.99$ in calm markets and $\lambda = 0.95$ during crises. Explain the rationale: crises require faster adaptation (shorter memory). (d) Propose an adaptive forgetting factor $\lambda_t = \lambda_{\min} + (1-\lambda_{\min})\exp(-\gamma e_t^2)$ and explain how large prediction errors $e_t$ automatically reduce $\lambda_t$.

??? success "Solution to Exercise 2"
    **(a)** For $\lambda = 0.95$:

    $$
    T_{\text{eff}} = \frac{1}{1 - 0.95} = 20 \text{ observations}
    $$

    **(b)** The weight on an observation $k$ periods ago is $\lambda^k$. We need $\lambda^k < 0.01$:

    $$
    0.95^k < 0.01 \implies k \ln(0.95) < \ln(0.01) \implies k > \frac{\ln(0.01)}{\ln(0.95)} = \frac{-4.6052}{-0.05129} \approx 89.8
    $$

    So after approximately $k = 90$ periods, the weight drops below 1%.

    **(c)** During crises, market parameters (volatilities, correlations, factor loadings) change rapidly. Using $\lambda = 0.99$ in calm markets gives $T_{\text{eff}} = 100$ observations, providing low-variance estimates from a large effective sample. Switching to $\lambda = 0.95$ during crises reduces $T_{\text{eff}}$ to 20, allowing the estimator to adapt within roughly 20 trading days. The rationale is that the bias from stale data (using a long window during rapid change) exceeds the variance cost of using fewer effective observations.

    **(d)** The adaptive forgetting factor $\lambda_t = \lambda_{\min} + (1 - \lambda_{\min})\exp(-\gamma e_t^2)$ works as follows:

    - When $e_t \approx 0$ (small prediction errors): $\exp(-\gamma e_t^2) \approx 1$, so $\lambda_t \approx 1$. The estimator uses a long memory, as the current model fits well.
    - When $|e_t|$ is large (model mismatch): $\exp(-\gamma e_t^2) \to 0$, so $\lambda_t \to \lambda_{\min}$. The effective window shrinks dramatically, forcing rapid adaptation.

    The parameter $\gamma$ controls sensitivity: larger $\gamma$ makes the forgetting factor react to smaller errors. The floor $\lambda_{\min}$ prevents the effective window from becoming too short (e.g., $\lambda_{\min} = 0.9$ ensures $T_{\text{eff}} \geq 10$).

---

**Exercise 3.** Compare RLS and SGD for online estimation of a linear regression with $d = 100$ features. (a) What is the per-update computational complexity of RLS ($O(d^2)$) versus SGD ($O(d)$)? For $d = 100$, how much faster is SGD per iteration? (b) RLS converges in one pass over the data (for stationary linear problems), while SGD requires multiple passes. Explain why this is due to the second-order information captured in $P_t^{-1}$. (c) For a nonlinear model (e.g., a neural network with $d = 10{,}000$ parameters), why is SGD the only practical choice?

??? success "Solution to Exercise 3"
    **(a)** Per-update complexity:

    - **RLS:** $O(d^2)$ because the key operation is updating the $d \times d$ matrix $P_t^{-1}$ via the Sherman-Morrison formula, involving outer products and matrix-vector multiplications.
    - **SGD:** $O(d)$ because the update $\theta_{t+1} = \theta_t - \eta_t g_t$ requires only a vector addition scaled by the gradient, which is a $d$-dimensional vector.

    For $d = 100$: RLS costs $O(10{,}000)$ operations per step, while SGD costs $O(100)$. SGD is roughly **100 times faster** per iteration.

    **(b)** RLS converges in one pass because it maintains and updates the full $d \times d$ inverse covariance matrix $P_t^{-1} = (\sum_{i=1}^t X_i X_i^\top)^{-1}$, which captures the second-order curvature of the least squares loss. This is equivalent to performing Newton's method at each step: the gain $K_t = P_t^{-1} X_t / (1 + X_t^\top P_t^{-1} X_t)$ automatically scales the update by the inverse Hessian, giving optimal step sizes in all directions.

    SGD, by contrast, uses only first-order (gradient) information with a scalar learning rate $\eta_t$. It cannot distinguish between directions of high and low curvature, leading to oscillation in high-curvature directions and slow progress in low-curvature directions. Multiple passes are needed to converge, especially when the design matrix is ill-conditioned.

    **(c)** For a neural network with $d = 10{,}000$ parameters:

    - RLS would require storing and updating a $10{,}000 \times 10{,}000$ matrix ($10^8$ entries), needing roughly 800 MB of memory and $O(10^8)$ operations per update. This is completely impractical.
    - SGD requires only $O(d) = O(10{,}000)$ storage and operations per update.
    - Furthermore, the neural network loss is non-convex, so the second-order "exactness" guarantee of RLS does not apply. SGD's stochastic nature actually helps escape local minima.
    - Adaptive methods like Adam provide a practical middle ground, maintaining per-parameter learning rates with $O(d)$ memory.

---

**Exercise 4.** The stability-adaptivity tradeoff for a constant-gain estimator tracking a drifting parameter gives MSE $= KR/(2-K) + Q/(K(2-K))$ where $R$ is observation noise variance and $Q$ is drift variance. (a) For $R = 0.04$ and $Q = 0.001$, compute the optimal gain $K^* = \sqrt{Q/(R + Q/2)}$ and the resulting MSE. (b) Plot or sketch the MSE as a function of $K$ for these parameter values, showing the two components (noise amplification increasing with $K$, drift lag decreasing with $K$). (c) In financial terms, $R$ corresponds to daily return noise and $Q$ to the rate of parameter change. During a crisis, $Q$ increases tenfold. Compute the new optimal $K^*$ and explain why the estimator should adapt faster.

??? success "Solution to Exercise 4"
    **(a)** With $R = 0.04$ and $Q = 0.001$:

    $$
    K^* = \sqrt{\frac{Q}{R + Q/2}} = \sqrt{\frac{0.001}{0.04 + 0.0005}} = \sqrt{\frac{0.001}{0.0405}} = \sqrt{0.024691} \approx 0.1571
    $$

    The resulting MSE:

    $$
    \text{MSE} = \frac{K^* R}{2 - K^*} + \frac{Q}{K^*(2 - K^*)}
    $$

    With $2 - K^* \approx 1.8429$ and $K^*(2 - K^*) \approx 0.2896$:

    $$
    \text{MSE} = \frac{0.1571 \times 0.04}{1.8429} + \frac{0.001}{0.2896} = \frac{0.006284}{1.8429} + 0.003453 = 0.003410 + 0.003453 \approx 0.006863
    $$

    **(b)** The MSE as a function of $K$ has two components:

    - **Noise amplification:** $KR/(2-K)$, which is increasing and convex in $K$. At $K=0$ this equals 0; as $K \to 2$ it diverges.
    - **Drift lag:** $Q/(K(2-K))$, which is decreasing in $K$ for $K < 1$. At $K \to 0$ it diverges; it has a minimum contribution as $K$ increases.

    The total MSE is U-shaped: very large for $K$ near 0 (dominated by drift lag), decreasing to the minimum at $K^* \approx 0.157$, then increasing for large $K$ (dominated by noise). The two curves cross near the optimum, illustrating the bias-variance trade-off.

    **(c)** During a crisis, $Q$ increases tenfold: $Q_{\text{crisis}} = 0.01$. The new optimal gain:

    $$
    K^*_{\text{crisis}} = \sqrt{\frac{0.01}{0.04 + 0.005}} = \sqrt{\frac{0.01}{0.045}} = \sqrt{0.2222} \approx 0.4714
    $$

    This is three times larger than the calm-period gain ($0.157$). The estimator should adapt much faster because the parameter is now drifting more rapidly. The cost of lagging behind the drift (bias) has increased, so it is worth accepting more noise amplification (variance) to track the changes. In financial terms, the model must respond quickly when market dynamics shift during a crisis, even if this means noisier short-term estimates.

---

**Exercise 5.** The Adam optimizer updates parameters using bias-corrected first and second moment estimates. For a single parameter with gradient sequence $g_1 = 0.5$, $g_2 = -0.3$, $g_3 = 0.2$, and hyperparameters $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\eta = 0.01$, $\epsilon = 10^{-8}$: (a) Compute $m_t$, $v_t$, $\hat{m}_t$, $\hat{v}_t$, and the parameter update $\Delta\theta_t$ for $t = 1, 2, 3$. (b) Why is the bias correction $\hat{m}_t = m_t / (1-\beta_1^t)$ necessary in the early steps? (c) Compare the effective learning rate $\eta / \sqrt{\hat{v}_t}$ at each step with the fixed learning rate used in standard SGD. How does Adam automatically adjust the step size?

??? success "Solution to Exercise 5"
    **(a)** Starting from $m_0 = 0$, $v_0 = 0$:

    **Step $t = 1$** ($g_1 = 0.5$):

    $$
    m_1 = 0.9 \times 0 + 0.1 \times 0.5 = 0.05
    $$

    $$
    v_1 = 0.999 \times 0 + 0.001 \times 0.25 = 0.00025
    $$

    $$
    \hat{m}_1 = \frac{0.05}{1 - 0.9} = 0.5, \quad \hat{v}_1 = \frac{0.00025}{1 - 0.999} = 0.25
    $$

    $$
    \Delta\theta_1 = -\frac{0.01}{\sqrt{0.25} + 10^{-8}} \times 0.5 = -\frac{0.01}{0.5} \times 0.5 = -0.01
    $$

    **Step $t = 2$** ($g_2 = -0.3$):

    $$
    m_2 = 0.9 \times 0.05 + 0.1 \times (-0.3) = 0.045 - 0.03 = 0.015
    $$

    $$
    v_2 = 0.999 \times 0.00025 + 0.001 \times 0.09 = 0.00024975 + 0.00009 = 0.00033975
    $$

    $$
    \hat{m}_2 = \frac{0.015}{1 - 0.81} = \frac{0.015}{0.19} \approx 0.07895
    $$

    $$
    \hat{v}_2 = \frac{0.00033975}{1 - 0.998001} = \frac{0.00033975}{0.001999} \approx 0.16996
    $$

    $$
    \Delta\theta_2 = -\frac{0.01}{\sqrt{0.16996} + 10^{-8}} \times 0.07895 = -\frac{0.01}{0.4123} \times 0.07895 \approx -0.001915
    $$

    **Step $t = 3$** ($g_3 = 0.2$):

    $$
    m_3 = 0.9 \times 0.015 + 0.1 \times 0.2 = 0.0135 + 0.02 = 0.0335
    $$

    $$
    v_3 = 0.999 \times 0.00033975 + 0.001 \times 0.04 = 0.000339411 + 0.00004 = 0.000379411
    $$

    $$
    \hat{m}_3 = \frac{0.0335}{1 - 0.729} = \frac{0.0335}{0.271} \approx 0.12362
    $$

    $$
    \hat{v}_3 = \frac{0.000379411}{1 - 0.997003} = \frac{0.000379411}{0.002997} \approx 0.12659
    $$

    $$
    \Delta\theta_3 = -\frac{0.01}{\sqrt{0.12659} + 10^{-8}} \times 0.12362 = -\frac{0.01}{0.3558} \times 0.12362 \approx -0.003474
    $$

    **(b)** The bias correction is necessary because $m_t$ and $v_t$ are initialized at zero and are exponential moving averages. In early steps, they are biased toward zero. For example, $m_1 = 0.1 g_1 = 0.05$, but the true gradient mean is $g_1 = 0.5$. The correction $\hat{m}_1 = m_1/(1 - \beta_1^1) = 0.05/0.1 = 0.5$ recovers the unbiased estimate. Without correction, the early updates would be much smaller than they should be, effectively wasting the first several iterations. As $t \to \infty$, $\beta_1^t \to 0$ and the correction becomes negligible.

    **(c)** The effective learning rate at each step is $\eta/\sqrt{\hat{v}_t}$:

    - $t = 1$: $0.01/\sqrt{0.25} = 0.02$
    - $t = 2$: $0.01/\sqrt{0.16996} \approx 0.02426$
    - $t = 3$: $0.01/\sqrt{0.12659} \approx 0.02811$

    With standard SGD using $\eta = 0.01$, the effective learning rate is always $0.01$. Adam automatically scales the step size inversely with the root-mean-square of recent gradients. When gradients are large (volatile loss landscape), $\hat{v}_t$ is large and the effective rate decreases, preventing overshooting. When gradients are small (flat region), $\hat{v}_t$ is small and the effective rate increases, speeding convergence. This per-parameter adaptation is especially valuable when different parameters have different curvatures.

---

**Exercise 6.** A streaming VaR estimator updates the $\alpha$-quantile using $\hat{q}_t^{(\alpha)} = \hat{q}_{t-1}^{(\alpha)} + \gamma_t(\alpha - \mathbf{1}\{R_t \le \hat{q}_{t-1}^{(\alpha)}\})$. (a) Explain why this is an SGD update on the pinball (quantile) loss $\rho_\alpha(u) = u(\alpha - \mathbf{1}\{u \le 0\})$. (b) For $\alpha = 0.01$ (1% VaR), if the current estimate is $\hat{q}_t = -2.5\%$ and the new return is $R_{t+1} = -3.2\%$ (a loss exceeding VaR), compute the update direction. What is the update direction when $R_{t+1} = -1.5\%$ (no VaR breach)? (c) The step size $\gamma_t$ must satisfy the Robbins-Monro conditions. What happens if $\gamma_t$ is too large (erratic estimates) or too small (slow adaptation)?

??? success "Solution to Exercise 6"
    **(a)** The quantile loss (pinball loss) at level $\alpha$ is:

    $$
    \rho_\alpha(u) = u(\alpha - \mathbf{1}\{u \leq 0\}) = \begin{cases} \alpha u & \text{if } u > 0 \\ (\alpha - 1) u & \text{if } u \leq 0 \end{cases}
    $$

    where $u = R_t - q$ for quantile estimate $q$. The subgradient with respect to $q$ is:

    $$
    \frac{\partial}{\partial q}\rho_\alpha(R_t - q) = -(\alpha - \mathbf{1}\{R_t \leq q\}) = \mathbf{1}\{R_t \leq q\} - \alpha
    $$

    SGD on this loss gives the update $q_{t+1} = q_t - \gamma_t(\mathbf{1}\{R_t \leq q_t\} - \alpha)$, which rearranges to:

    $$
    q_{t+1} = q_t + \gamma_t(\alpha - \mathbf{1}\{R_t \leq q_t\})
    $$

    This is exactly the stated update rule. The algorithm seeks the fixed point where $\mathbb{E}[\mathbf{1}\{R_t \leq q\}] = \alpha$, i.e., $q$ is the $\alpha$-quantile.

    **(b)** With $\alpha = 0.01$, $\hat{q}_t = -2.5\%$, and $R_{t+1} = -3.2\%$:

    Since $R_{t+1} = -3.2\% < -2.5\% = \hat{q}_t$, we have $\mathbf{1}\{R_{t+1} \leq \hat{q}_t\} = 1$. The update direction is:

    $$
    \alpha - 1 = 0.01 - 1 = -0.99
    $$

    So $\hat{q}_{t+1} = -2.5\% + \gamma_t(-0.99)$. The estimate moves downward (more negative), making the VaR estimate more conservative after a loss that exceeded it. This makes sense: a VaR breach should push the threshold further into the tail.

    When $R_{t+1} = -1.5\% > -2.5\% = \hat{q}_t$ (no breach), $\mathbf{1}\{R_{t+1} \leq \hat{q}_t\} = 0$. The update direction is:

    $$
    \alpha - 0 = 0.01
    $$

    So $\hat{q}_{t+1} = -2.5\% + \gamma_t(0.01)$. The estimate nudges upward (less negative) by a small amount. The asymmetry is crucial: breaches push the estimate down by a factor of $(1 - \alpha)/\alpha = 99$ times more than non-breaches push it up. At the true quantile, breaches occur with probability $\alpha$, and the expected update is zero.

    **(c)** If $\gamma_t$ is **too large**, the quantile estimate jumps significantly with each observation. After a VaR breach, the estimate might overshoot far into the tail, and then slowly creep back. This creates erratic, unreliable VaR forecasts that oscillate wildly.

    If $\gamma_t$ is **too small**, the estimate barely moves. After a regime shift that increases tail risk, it could take hundreds of observations before the VaR estimate reflects the new reality, leading to systematic underestimation of risk.

    The Robbins-Monro conditions $\sum \gamma_t = \infty$ and $\sum \gamma_t^2 < \infty$ ensure (i) the estimator can eventually reach any quantile value (infinite total movement) and (ii) the fluctuations around the true quantile diminish (finite accumulated variance). Common choices like $\gamma_t = c/t$ or $\gamma_t = c/\sqrt{t}$ satisfy these conditions.

---

**Exercise 7.** The online EM algorithm for a two-component Gaussian mixture model $p(Y) = \pi \mathcal{N}(Y; \mu_1, \sigma_1^2) + (1-\pi)\mathcal{N}(Y; \mu_2, \sigma_2^2)$ updates sufficient statistics incrementally. (a) For a financial application, interpret the two components as "normal" and "crisis" return distributions with $\mu_1 = 0.03\%$, $\sigma_1 = 1\%$, $\mu_2 = -0.1\%$, $\sigma_2 = 3\%$, and $\pi = 0.9$. (b) When a new return observation $Y_t = -4\%$ arrives, compute the responsibilities $r_{t1}$ and $r_{t2}$. Which component claims this observation? (c) Describe how the online EM updates $\bar{n}_k$, $\bar{s}_k$, and hence $\hat{\mu}_k$ and $\hat{\pi}$. With step size $\gamma_t = 1/t$, how does the influence of old observations decay over time?

??? success "Solution to Exercise 7"
    **(a)** In the financial interpretation:

    - **Component 1 ("normal" regime):** $\mu_1 = 0.03\%$ daily return (positive drift), $\sigma_1 = 1\%$ daily volatility. This represents typical market conditions with modest positive returns and moderate volatility.
    - **Component 2 ("crisis" regime):** $\mu_2 = -0.1\%$ daily return (negative drift), $\sigma_2 = 3\%$ daily volatility. This captures stress periods with negative returns and elevated volatility.
    - **Mixing weight** $\pi = 0.9$ means the market is in the normal regime 90% of the time.

    This mixture produces a return distribution with heavier tails than a single Gaussian (excess kurtosis) and negative skewness (because the crisis component has a negative mean and high variance), matching empirical stylized facts of financial returns.

    **(b)** For $Y_t = -4\% = -0.04$, we compute the density under each component:

    $$
    \mathcal{N}(Y_t; \mu_1, \sigma_1^2) = \frac{1}{\sqrt{2\pi}(0.01)} \exp\left(-\frac{(-0.04 - 0.0003)^2}{2(0.01)^2}\right)
    $$

    $$
    = \frac{1}{0.02507} \exp\left(-\frac{(0.0403)^2}{0.0002}\right) = 39.89 \exp(-8.1205) \approx 39.89 \times 2.97 \times 10^{-4} \approx 0.01185
    $$

    $$
    \mathcal{N}(Y_t; \mu_2, \sigma_2^2) = \frac{1}{\sqrt{2\pi}(0.03)} \exp\left(-\frac{(-0.04 - (-0.001))^2}{2(0.03)^2}\right)
    $$

    $$
    = \frac{1}{0.07522} \exp\left(-\frac{(0.039)^2}{0.0018}\right) = 13.30 \exp(-0.845) \approx 13.30 \times 0.4296 \approx 5.714
    $$

    The responsibilities:

    $$
    r_{t1} = \frac{\pi \cdot \mathcal{N}(Y_t; \mu_1, \sigma_1^2)}{\pi \cdot \mathcal{N}(Y_t; \mu_1, \sigma_1^2) + (1-\pi) \cdot \mathcal{N}(Y_t; \mu_2, \sigma_2^2)}
    $$

    $$
    = \frac{0.9 \times 0.01185}{0.9 \times 0.01185 + 0.1 \times 5.714} = \frac{0.01067}{0.01067 + 0.5714} = \frac{0.01067}{0.5821} \approx 0.0183
    $$

    $$
    r_{t2} = 1 - r_{t1} \approx 0.9817
    $$

    Component 2 (crisis) overwhelmingly claims this observation with responsibility $\approx 98.2\%$. A $-4\%$ return is $4$ standard deviations below the mean of the normal component but only about $1.3$ standard deviations below the mean of the crisis component.

    **(c)** The online EM updates with step size $\gamma_t$:

    $$
    \bar{n}_k^{(t)} = (1 - \gamma_t) \bar{n}_k^{(t-1)} + \gamma_t r_{tk}
    $$

    $$
    \bar{s}_k^{(t)} = (1 - \gamma_t) \bar{s}_k^{(t-1)} + \gamma_t r_{tk} Y_t
    $$

    Then the parameters update as:

    $$
    \hat{\mu}_k^{(t)} = \frac{\bar{s}_k^{(t)}}{\bar{n}_k^{(t)}}, \quad \hat{\pi}^{(t)} = \frac{\bar{n}_1^{(t)}}{\bar{n}_1^{(t)} + \bar{n}_2^{(t)}}
    $$

    With $\gamma_t = 1/t$, after $t$ observations, each sufficient statistic is a weighted average where observation $i$ has weight proportional to $\prod_{j=i+1}^t (1 - 1/j) = i/t$. This means observation $i$ receives weight $i/t$ at time $t$, so old observations are progressively downweighted (but not exponentially -- they decay as $i/t$, which is polynomial). The effective memory grows with $t$: the estimator averages over all past data with increasing weights on recent observations. For a constant $\gamma$ (e.g., $\gamma_t = \gamma$ for all $t$), the decay would be exponential with effective window $1/\gamma$, making the algorithm more adaptive to non-stationarity.
