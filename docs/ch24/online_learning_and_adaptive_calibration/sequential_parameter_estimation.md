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

---

**Exercise 2.** Exponentially weighted RLS uses a forgetting factor $\lambda$. (a) For $\lambda = 0.95$, compute the effective window length $T_{\text{eff}} = 1/(1-\lambda)$. (b) The weight on an observation from $k$ periods ago is $\lambda^k$. How many periods back does the weight drop below 1% of the current observation's weight? (c) A hedge fund recalibrates its factor model daily using $\lambda = 0.99$ in calm markets and $\lambda = 0.95$ during crises. Explain the rationale: crises require faster adaptation (shorter memory). (d) Propose an adaptive forgetting factor $\lambda_t = \lambda_{\min} + (1-\lambda_{\min})\exp(-\gamma e_t^2)$ and explain how large prediction errors $e_t$ automatically reduce $\lambda_t$.

---

**Exercise 3.** Compare RLS and SGD for online estimation of a linear regression with $d = 100$ features. (a) What is the per-update computational complexity of RLS ($O(d^2)$) versus SGD ($O(d)$)? For $d = 100$, how much faster is SGD per iteration? (b) RLS converges in one pass over the data (for stationary linear problems), while SGD requires multiple passes. Explain why this is due to the second-order information captured in $P_t^{-1}$. (c) For a nonlinear model (e.g., a neural network with $d = 10{,}000$ parameters), why is SGD the only practical choice?

---

**Exercise 4.** The stability-adaptivity tradeoff for a constant-gain estimator tracking a drifting parameter gives MSE $= KR/(2-K) + Q/(K(2-K))$ where $R$ is observation noise variance and $Q$ is drift variance. (a) For $R = 0.04$ and $Q = 0.001$, compute the optimal gain $K^* = \sqrt{Q/(R + Q/2)}$ and the resulting MSE. (b) Plot or sketch the MSE as a function of $K$ for these parameter values, showing the two components (noise amplification increasing with $K$, drift lag decreasing with $K$). (c) In financial terms, $R$ corresponds to daily return noise and $Q$ to the rate of parameter change. During a crisis, $Q$ increases tenfold. Compute the new optimal $K^*$ and explain why the estimator should adapt faster.

---

**Exercise 5.** The Adam optimizer updates parameters using bias-corrected first and second moment estimates. For a single parameter with gradient sequence $g_1 = 0.5$, $g_2 = -0.3$, $g_3 = 0.2$, and hyperparameters $\beta_1 = 0.9$, $\beta_2 = 0.999$, $\eta = 0.01$, $\epsilon = 10^{-8}$: (a) Compute $m_t$, $v_t$, $\hat{m}_t$, $\hat{v}_t$, and the parameter update $\Delta\theta_t$ for $t = 1, 2, 3$. (b) Why is the bias correction $\hat{m}_t = m_t / (1-\beta_1^t)$ necessary in the early steps? (c) Compare the effective learning rate $\eta / \sqrt{\hat{v}_t}$ at each step with the fixed learning rate used in standard SGD. How does Adam automatically adjust the step size?

---

**Exercise 6.** A streaming VaR estimator updates the $\alpha$-quantile using $\hat{q}_t^{(\alpha)} = \hat{q}_{t-1}^{(\alpha)} + \gamma_t(\alpha - \mathbf{1}\{R_t \le \hat{q}_{t-1}^{(\alpha)}\})$. (a) Explain why this is an SGD update on the pinball (quantile) loss $\rho_\alpha(u) = u(\alpha - \mathbf{1}\{u \le 0\})$. (b) For $\alpha = 0.01$ (1% VaR), if the current estimate is $\hat{q}_t = -2.5\%$ and the new return is $R_{t+1} = -3.2\%$ (a loss exceeding VaR), compute the update direction. What is the update direction when $R_{t+1} = -1.5\%$ (no VaR breach)? (c) The step size $\gamma_t$ must satisfy the Robbins-Monro conditions. What happens if $\gamma_t$ is too large (erratic estimates) or too small (slow adaptation)?

---

**Exercise 7.** The online EM algorithm for a two-component Gaussian mixture model $p(Y) = \pi \mathcal{N}(Y; \mu_1, \sigma_1^2) + (1-\pi)\mathcal{N}(Y; \mu_2, \sigma_2^2)$ updates sufficient statistics incrementally. (a) For a financial application, interpret the two components as "normal" and "crisis" return distributions with $\mu_1 = 0.03\%$, $\sigma_1 = 1\%$, $\mu_2 = -0.1\%$, $\sigma_2 = 3\%$, and $\pi = 0.9$. (b) When a new return observation $Y_t = -4\%$ arrives, compute the responsibilities $r_{t1}$ and $r_{t2}$. Which component claims this observation? (c) Describe how the online EM updates $\bar{n}_k$, $\bar{s}_k$, and hence $\hat{\mu}_k$ and $\hat{\pi}$. With step size $\gamma_t = 1/t$, how does the influence of old observations decay over time?
