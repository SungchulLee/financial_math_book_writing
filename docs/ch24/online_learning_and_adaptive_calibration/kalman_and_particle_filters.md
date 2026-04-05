# Kalman and Particle Filters

**Bayesian filtering** provides a principled framework for sequential state estimation: given noisy observations arriving over time, maintain a posterior distribution over the hidden state. The **Kalman filter** gives the exact solution for linear-Gaussian systems, while **particle filters** (sequential Monte Carlo) extend to arbitrary nonlinear, non-Gaussian models. In finance, these methods track latent variables---stochastic volatility, hidden regimes, time-varying parameters---that drive observable prices and returns.

---

## State-Space Models

### General Formulation

**Definition (State-Space Model).** A discrete-time state-space model consists of:

**State equation** (hidden dynamics):

$$
x_t = f(x_{t-1}, u_t), \quad u_t \sim p_u
$$

**Observation equation** (measurement process):

$$
y_t = h(x_t, v_t), \quad v_t \sim p_v
$$

where $x_t \in \mathbb{R}^{n_x}$ is the hidden state, $y_t \in \mathbb{R}^{n_y}$ is the observation, and $u_t, v_t$ are independent noise processes.

### Linear-Gaussian Special Case

When both equations are linear with Gaussian noise:

$$
x_t = A_t x_{t-1} + B_t u_t, \quad u_t \sim \mathcal{N}(0, Q_t)
$$

$$
y_t = C_t x_t + v_t, \quad v_t \sim \mathcal{N}(0, R_t)
$$

the filtering problem admits an exact closed-form solution: the Kalman filter.

### Financial State-Space Models

**Stochastic volatility:**

$$
\log \sigma_t^2 = \alpha + \beta \log \sigma_{t-1}^2 + \eta_t, \quad \eta_t \sim \mathcal{N}(0, \sigma_\eta^2)
$$

$$
r_t = \sigma_t \varepsilon_t, \quad \varepsilon_t \sim \mathcal{N}(0, 1)
$$

Here $x_t = \log \sigma_t^2$ is hidden and $y_t = r_t$ is observed. The observation equation is nonlinear and non-Gaussian, requiring extended or particle filter methods.

**Dynamic factor model:**

$$
f_t = \Phi f_{t-1} + u_t, \quad u_t \sim \mathcal{N}(0, Q)
$$

$$
r_t = \Lambda f_t + \varepsilon_t, \quad \varepsilon_t \sim \mathcal{N}(0, \Sigma)
$$

where $f_t \in \mathbb{R}^k$ are latent factors and $r_t \in \mathbb{R}^n$ are observed returns. This is linear-Gaussian, so the Kalman filter applies directly.

---

## The Kalman Filter

### Bayesian Derivation

The filtering problem seeks the posterior $p(x_t \mid y_{1:t})$ recursively. By Bayes' theorem:

**Prediction step:**

$$
p(x_t \mid y_{1:t-1}) = \int p(x_t \mid x_{t-1}) \, p(x_{t-1} \mid y_{1:t-1}) \, dx_{t-1}
$$

**Update step:**

$$
p(x_t \mid y_{1:t}) = \frac{p(y_t \mid x_t) \, p(x_t \mid y_{1:t-1})}{p(y_t \mid y_{1:t-1})}
$$

For the linear-Gaussian model, both steps preserve Gaussianity, so the posterior is fully characterized by its mean and covariance.

### The Kalman Filter Algorithm

**Theorem (Kalman Filter).** For the linear-Gaussian state-space model with prior $x_0 \sim \mathcal{N}(\hat{x}_{0|0}, P_{0|0})$, the posterior $p(x_t \mid y_{1:t}) = \mathcal{N}(\hat{x}_{t|t}, P_{t|t})$ is computed recursively:

**Prediction:**

$$
\hat{x}_{t|t-1} = A_t \hat{x}_{t-1|t-1}
$$

$$
P_{t|t-1} = A_t P_{t-1|t-1} A_t^\top + B_t Q_t B_t^\top
$$

**Innovation:**

$$
e_t = y_t - C_t \hat{x}_{t|t-1}
$$

$$
S_t = C_t P_{t|t-1} C_t^\top + R_t
$$

**Update:**

$$
K_t = P_{t|t-1} C_t^\top S_t^{-1}
$$

$$
\hat{x}_{t|t} = \hat{x}_{t|t-1} + K_t e_t
$$

$$
P_{t|t} = (I - K_t C_t) P_{t|t-1}
$$

The matrix $K_t$ is the **Kalman gain**, $e_t$ is the **innovation** (prediction error), and $S_t$ is the innovation covariance.

### Proof of Optimality

The Kalman filter is the minimum mean squared error (MMSE) estimator. For the update step, we need the conditional distribution $p(x_t \mid y_{1:t})$. Since $(x_t, y_t)$ are jointly Gaussian given $y_{1:t-1}$:

$$
\begin{pmatrix} x_t \\ y_t \end{pmatrix} \bigg| y_{1:t-1} \sim \mathcal{N}\!\left(\begin{pmatrix} \hat{x}_{t|t-1} \\ C_t \hat{x}_{t|t-1} \end{pmatrix}, \begin{pmatrix} P_{t|t-1} & P_{t|t-1} C_t^\top \\ C_t P_{t|t-1} & S_t \end{pmatrix}\right)
$$

The conditional distribution $x_t \mid y_t, y_{1:t-1}$ is Gaussian with:

$$
\hat{x}_{t|t} = \hat{x}_{t|t-1} + P_{t|t-1}C_t^\top S_t^{-1}(y_t - C_t \hat{x}_{t|t-1}) = \hat{x}_{t|t-1} + K_t e_t
$$

$$
P_{t|t} = P_{t|t-1} - P_{t|t-1}C_t^\top S_t^{-1}C_t P_{t|t-1} = (I - K_t C_t)P_{t|t-1}
$$

$\square$

### Computational Complexity

Each update requires $O(n_x^2 n_y + n_y^3)$ operations (dominated by the matrix inversion $S_t^{-1}$). For large observation dimensions, the Woodbury identity or square-root filters improve efficiency.

---

## Extended and Unscented Kalman Filters

### Extended Kalman Filter (EKF)

For nonlinear state-space models:

$$
x_t = f(x_{t-1}) + u_t, \quad y_t = h(x_t) + v_t
$$

the EKF linearizes around the current estimate:

$$
F_t = \frac{\partial f}{\partial x}\bigg|_{x = \hat{x}_{t-1|t-1}}, \quad H_t = \frac{\partial h}{\partial x}\bigg|_{x = \hat{x}_{t|t-1}}
$$

and applies the standard Kalman filter using $F_t$ in place of $A_t$ and $H_t$ in place of $C_t$.

**Limitations:** The EKF can diverge for highly nonlinear systems because the linearization introduces systematic errors. It also requires computing Jacobians, which may be complex.

### Unscented Kalman Filter (UKF)

The UKF avoids linearization by propagating **sigma points** through the nonlinear functions.

**Algorithm (UKF):**

1. Choose $2n_x + 1$ sigma points:

$$
\chi_0 = \hat{x}, \quad \chi_i = \hat{x} + \sqrt{(n_x + \kappa)P} \big|_i, \quad \chi_{n_x+i} = \hat{x} - \sqrt{(n_x + \kappa)P}\big|_i
$$

where $\sqrt{(n_x + \kappa)P}\big|_i$ denotes the $i$-th column of the matrix square root.

2. Propagate through the nonlinear function: $\chi_i^* = f(\chi_i)$

3. Compute predicted mean and covariance from the propagated sigma points using weights $w_i$

The UKF captures the mean and covariance to third-order accuracy for Gaussian inputs (versus first-order for EKF).

---

## Particle Filters

### Motivation

For general nonlinear, non-Gaussian state-space models, no closed-form filtering solution exists. Particle filters approximate the posterior distribution using a weighted set of samples (particles).

### Sequential Monte Carlo

**Definition (Particle Approximation).** The filtering distribution is approximated by:

$$
\hat{p}(x_t \mid y_{1:t}) = \sum_{i=1}^N w_t^{(i)} \, \delta_{x_t^{(i)}}(x_t)
$$

where $\{x_t^{(i)}, w_t^{(i)}\}_{i=1}^N$ are $N$ particles and their normalized weights.

**Algorithm (Bootstrap Particle Filter -- Gordon, Salmond & Smith 1993):**

1. **Initialize:** Draw $x_0^{(i)} \sim p(x_0)$ for $i = 1, \ldots, N$, set $w_0^{(i)} = 1/N$
2. **For** $t = 1, 2, \ldots$:
    - **Propagate:** Draw $\tilde{x}_t^{(i)} \sim p(x_t \mid x_{t-1}^{(i)})$ (sample from state transition)
    - **Weight:** Compute unnormalized weights $\tilde{w}_t^{(i)} = p(y_t \mid \tilde{x}_t^{(i)})$
    - **Normalize:** $w_t^{(i)} = \tilde{w}_t^{(i)} / \sum_j \tilde{w}_t^{(j)}$
    - **Resample:** If effective sample size $N_{\text{eff}} = 1/\sum_i (w_t^{(i)})^2 < N/2$, resample $N$ particles from $\{(\tilde{x}_t^{(i)}, w_t^{(i)})\}$ with replacement and reset weights to $1/N$

### Convergence

**Theorem (Particle Filter Convergence -- Crisan & Doucet 2002).** For bounded likelihood functions, the particle filter approximation satisfies:

$$
\left|\int g(x) \, \hat{p}(x_t \mid y_{1:t}) \, dx - \int g(x) \, p(x_t \mid y_{1:t}) \, dx\right| = O_p(N^{-1/2})
$$

for any bounded measurable function $g$. The convergence rate $N^{-1/2}$ is independent of the state dimension $n_x$.

### Resampling Methods

- **Multinomial resampling:** Draw from the discrete distribution $\{w_t^{(i)}\}$. Simple but high variance.
- **Systematic resampling:** Use a single uniform draw and equally spaced thresholds. Lower variance.
- **Stratified resampling:** Divide $[0,1]$ into $N$ strata, draw one uniform per stratum. Optimal among unbiased schemes.

!!! warning "Particle Degeneracy"
    Without resampling, weights concentrate on a single particle after a few time steps. With resampling, particle diversity decreases over time (sample impoverishment). Mitigation strategies include:

    - Increasing the number of particles
    - Using optimal proposal distributions
    - Adding MCMC rejuvenation steps (resample-move)

---

## Financial Application: Stochastic Volatility Filtering

### The SV Model

Consider the log-volatility model:

$$
h_t = \mu + \phi(h_{t-1} - \mu) + \sigma_\eta \eta_t, \quad \eta_t \sim \mathcal{N}(0,1)
$$

$$
r_t = \exp(h_t/2) \varepsilon_t, \quad \varepsilon_t \sim \mathcal{N}(0,1)
$$

where $h_t = \log \sigma_t^2$ is the log-variance. The state equation is linear-Gaussian, but the observation equation is multiplicatively nonlinear ($r_t = e^{h_t/2}\varepsilon_t$), so the Kalman filter does not apply directly.

### Particle Filter Implementation

1. **Propagate:** $h_t^{(i)} = \mu + \phi(h_{t-1}^{(i)} - \mu) + \sigma_\eta \eta_t^{(i)}$ with $\eta_t^{(i)} \sim \mathcal{N}(0,1)$
2. **Weight:** $w_t^{(i)} \propto p(r_t \mid h_t^{(i)}) = \frac{1}{\sqrt{2\pi}} \exp\!\left(-\frac{h_t^{(i)}}{2} - \frac{r_t^2}{2e^{h_t^{(i)}}}\right)$
3. **Resample** when $N_{\text{eff}} < N/2$
4. **Estimate:** $\hat{\sigma}_t^2 = \sum_i w_t^{(i)} \exp(h_t^{(i)})$

The particle filter provides a full posterior distribution over $\sigma_t^2$, not just a point estimate. Credible intervals quantify uncertainty in the volatility estimate.

### Comparison with GARCH

| Feature | GARCH | Particle Filter (SV) |
|---|---|---|
| Model | Observation-driven | State-driven |
| Likelihood | Exact, closed-form | Approximate (particle) |
| Uncertainty | Point estimate only | Full posterior distribution |
| Non-Gaussian | Extensions needed | Natural |
| Computational cost | $O(T)$ | $O(TN)$ |
| Multi-dimensional | Difficult | Straightforward |

---

## Application: Pairs Trading with Kalman Filter

### Spread Modeling

For a pairs trading strategy between assets $A$ and $B$, model the spread:

$$
y_t = p_t^A - \beta_t p_t^B
$$

where the hedge ratio $\beta_t$ is time-varying. The state-space formulation:

$$
\beta_t = \beta_{t-1} + w_t, \quad w_t \sim \mathcal{N}(0, Q)
$$

$$
p_t^A = \beta_t p_t^B + \alpha + v_t, \quad v_t \sim \mathcal{N}(0, R)
$$

The Kalman filter tracks $\beta_t$ in real time, with the Kalman gain $K_t$ controlling how quickly the hedge ratio adapts to new observations.

### Trading Signal

The innovation $e_t = p_t^A - \hat{\beta}_{t|t-1} p_t^B - \hat{\alpha}$ is the unexpected component of the spread. Trading rules:

- Enter long spread when $e_t / \sqrt{S_t} < -z_{\text{entry}}$
- Enter short spread when $e_t / \sqrt{S_t} > z_{\text{entry}}$
- Exit when $|e_t / \sqrt{S_t}| < z_{\text{exit}}$

The standardized innovation $e_t / \sqrt{S_t}$ is approximately $\mathcal{N}(0,1)$ under the model, providing natural threshold calibration.

---

## Key Takeaways

1. **State-space models** decompose financial time series into latent dynamics and observation noise, providing a natural framework for tracking hidden variables.

2. The **Kalman filter** is optimal for linear-Gaussian systems and widely used for dynamic factor models, yield curve estimation, and pairs trading.

3. The **EKF** and **UKF** extend to mildly nonlinear systems, with the UKF providing better accuracy without requiring Jacobian computation.

4. **Particle filters** handle arbitrary nonlinear, non-Gaussian models, making them essential for stochastic volatility filtering and regime estimation.

5. **Financial applications** include real-time volatility tracking, adaptive hedge ratio estimation, factor model calibration, and regime detection.

---

## Further Reading

- Durbin & Koopman (2012), *Time Series Analysis by State Space Methods*
- Gordon, Salmond & Smith (1993), "Novel Approach to Nonlinear/Non-Gaussian Bayesian State Estimation"
- Doucet, de Freitas & Gordon (2001), *Sequential Monte Carlo Methods in Practice*
- Harvey (1989), *Forecasting, Structural Time Series Models and the Kalman Filter*
- Javaheri, Lautier & Galli (2003), "Filtering in Finance"

---

## Exercises

**Exercise 1.** Consider a scalar Kalman filter with state equation $x_t = x_{t-1} + u_t$, $u_t \sim \mathcal{N}(0, Q)$ and observation equation $y_t = x_t + v_t$, $v_t \sim \mathcal{N}(0, R)$. Initialize with $\hat{x}_{0|0} = 0$ and $P_{0|0} = 1$. For $Q = 0.01$ and $R = 0.25$: (a) Compute the prediction $\hat{x}_{1|0}$, $P_{1|0}$, and the Kalman gain $K_1$ when the first observation is $y_1 = 0.5$. (b) Compute the updated estimate $\hat{x}_{1|1}$ and $P_{1|1}$. (c) Show that the steady-state Kalman gain satisfies $K_\infty = (-R + \sqrt{R^2 + 4QR}) / (2R)$ and compute its numerical value.

??? success "Solution to Exercise 1"
    We have the scalar state-space model: $x_t = x_{t-1} + u_t$ with $u_t \sim N(0, Q)$, $y_t = x_t + v_t$ with $v_t \sim N(0, R)$, $Q = 0.01$, $R = 0.25$, $\hat{x}_{0|0} = 0$, $P_{0|0} = 1$.

    In standard notation: $A = 1$, $C = 1$, so the Kalman filter simplifies to scalar operations.

    **(a) Prediction:**

    $$
    \hat{x}_{1|0} = A\,\hat{x}_{0|0} = 1 \times 0 = 0
    $$

    $$
    P_{1|0} = A^2 P_{0|0} + Q = 1 + 0.01 = 1.01
    $$

    Innovation covariance and Kalman gain:

    $$
    S_1 = C^2 P_{1|0} + R = 1.01 + 0.25 = 1.26
    $$

    $$
    K_1 = \frac{P_{1|0} \cdot C}{S_1} = \frac{1.01}{1.26} \approx 0.8016
    $$

    **(b) Update with $y_1 = 0.5$:**

    $$
    e_1 = y_1 - C\,\hat{x}_{1|0} = 0.5 - 0 = 0.5
    $$

    $$
    \hat{x}_{1|1} = \hat{x}_{1|0} + K_1 e_1 = 0 + 0.8016 \times 0.5 = 0.4008
    $$

    $$
    P_{1|1} = (1 - K_1 C) P_{1|0} = (1 - 0.8016) \times 1.01 = 0.1984 \times 1.01 \approx 0.2004
    $$

    **(c) Steady-state Kalman gain:** In steady state, $P_{t|t} = P_\infty$ satisfies the algebraic Riccati equation. For the scalar random walk model:

    $$
    P_{t|t-1} = P_{t-1|t-1} + Q
    $$

    $$
    P_{t|t} = (1 - K_t) P_{t|t-1} = \frac{R}{P_{t|t-1} + R} \cdot P_{t|t-1} = \frac{R\, P_{t|t-1}}{P_{t|t-1} + R}
    $$

    In steady state, $P_{t|t} = P_{t-1|t-1} = P_\infty$, so $P_{t|t-1} = P_\infty + Q$. The fixed-point equation is:

    $$
    P_\infty = \frac{R(P_\infty + Q)}{P_\infty + Q + R}
    $$

    Cross-multiplying: $P_\infty(P_\infty + Q + R) = R(P_\infty + Q)$, which gives:

    $$
    P_\infty^2 + Q P_\infty + R P_\infty = R P_\infty + RQ
    $$

    $$
    P_\infty^2 + Q P_\infty - RQ = 0
    $$

    Using the quadratic formula:

    $$
    P_\infty = \frac{-Q + \sqrt{Q^2 + 4RQ}}{2}
    $$

    The steady-state Kalman gain is:

    $$
    K_\infty = \frac{P_\infty + Q}{P_\infty + Q + R}
    $$

    Alternatively, substituting $P_{\infty|t-1} = P_\infty + Q$ and noting $K_\infty = (P_\infty + Q)/(P_\infty + Q + R)$, we can derive directly. From $P_\infty = (1 - K_\infty)(P_\infty + Q)$ and $K_\infty = (P_\infty + Q)/(P_\infty + Q + R)$, let $p = P_\infty + Q$. Then $K_\infty = p/(p + R)$ and:

    $$
    P_\infty = \frac{Rp}{p + R} = p - Q \implies \frac{Rp}{p+R} = p - Q
    $$

    $$
    Rp = (p-Q)(p+R) = p^2 + Rp - Qp - QR
    $$

    $$
    p^2 - Qp - QR = 0 \implies p = \frac{Q + \sqrt{Q^2 + 4QR}}{2}
    $$

    Therefore:

    $$
    K_\infty = \frac{p}{p + R} = \frac{Q + \sqrt{Q^2 + 4QR}}{Q + \sqrt{Q^2 + 4QR} + 2R}
    $$

    This can be rewritten as:

    $$
    K_\infty = \frac{-R + \sqrt{R^2 + 4QR}}{2R}
    $$

    To verify: multiply numerator and denominator differently. Actually, note $K_\infty = p/(p+R)$, so $1 - K_\infty = R/(p+R)$, meaning $K_\infty = 1 - R/(p+R)$. With $p = (Q + \sqrt{Q^2 + 4QR})/2$:

    Numerically: $Q^2 + 4QR = 0.0001 + 4(0.01)(0.25) = 0.0001 + 0.01 = 0.0101$. So $\sqrt{0.0101} \approx 0.10050$.

    $$
    p = \frac{0.01 + 0.10050}{2} = 0.05525
    $$

    $$
    K_\infty = \frac{0.05525}{0.05525 + 0.25} = \frac{0.05525}{0.30525} \approx 0.1810
    $$

    Using the alternative formula: $(-0.25 + \sqrt{0.0625 + 0.01})/(0.5) = (-0.25 + \sqrt{0.0725})/0.5 = (-0.25 + 0.2693)/0.5 = 0.0193/0.5 = 0.0386$. This does not match, so the correct form of $K_\infty$ from our derivation is $K_\infty = p/(p+R) \approx 0.181$.

    Let us verify the stated formula. Setting $K = K_\infty$ in the steady-state relation $P_\infty = (1-K)(P_\infty + Q)$ and $K = (P_\infty + Q)/(P_\infty + Q + R)$ leads to $P_\infty^2 + QP_\infty - QR = 0$, giving $P_\infty = (-Q + \sqrt{Q^2 + 4QR})/2 \approx (-0.01 + 0.10050)/2 = 0.04525$. Then $K_\infty = (0.04525 + 0.01)/(0.04525 + 0.01 + 0.25) = 0.05525/0.30525 \approx 0.1810$.

    The formula $K_\infty = (-R + \sqrt{R^2 + 4QR})/(2R)$ gives $(-0.25 + \sqrt{0.0625 + 0.01})/0.5 = (-0.25 + 0.26926)/0.5 = 0.01926/0.5 = 0.03852$. This does not match $0.181$. The stated formula applies to a different parameterization. The correct steady-state gain for our model is:

    $$
    K_\infty \approx 0.181
    $$

---

**Exercise 2.** In a pairs trading application, the state-space model is $\beta_t = \beta_{t-1} + w_t$ with $w_t \sim \mathcal{N}(0, Q)$ and $p_t^A = \beta_t p_t^B + v_t$ with $v_t \sim \mathcal{N}(0, R)$. Suppose $Q = 10^{-5}$, $R = 0.01$, and $p_t^B = 50$. (a) Write the observation equation in standard form $y_t = C_t x_t + v_t$ identifying $C_t$, $y_t$, and $x_t$. (b) If the current Kalman gain is $K_t = 0.02$, the current estimate is $\hat{\beta}_{t-1|t-1} = 1.05$, and we observe $p_t^A = 53.5$, compute the innovation $e_t$ and the updated estimate $\hat{\beta}_{t|t}$. (c) The standardized innovation $e_t / \sqrt{S_t}$ is used as a trading signal. Explain why a large positive value suggests the spread is too wide (go short spread) and a large negative value suggests it is too narrow (go long spread).

??? success "Solution to Exercise 2"
    **(a)** The observation equation $p_t^A = \beta_t p_t^B + v_t$ can be written in standard form:

    $$
    y_t = C_t\, x_t + v_t
    $$

    where $y_t = p_t^A$, $x_t = \beta_t$, and $C_t = p_t^B = 50$. The state equation is $x_t = x_{t-1} + w_t$ (random walk for the hedge ratio).

    **(b)** The predicted observation is:

    $$
    \hat{y}_t = C_t\, \hat{\beta}_{t|t-1} = 50 \times 1.05 = 52.5
    $$

    (Since the state is a random walk, $\hat{\beta}_{t|t-1} = \hat{\beta}_{t-1|t-1} = 1.05$.)

    The innovation:

    $$
    e_t = p_t^A - C_t\,\hat{\beta}_{t|t-1} = 53.5 - 52.5 = 1.0
    $$

    The updated hedge ratio estimate:

    $$
    \hat{\beta}_{t|t} = \hat{\beta}_{t|t-1} + K_t\, e_t = 1.05 + 0.02 \times 1.0 = 1.07
    $$

    The positive innovation (asset A is trading higher than the model predicts) causes the estimated hedge ratio to increase from 1.05 to 1.07. This means more of asset B is needed to hedge each unit of asset A.

    **(c)** The standardized innovation $z_t = e_t / \sqrt{S_t}$ measures how unexpected the observed price of A is, given the model and the price of B. Under the model, $z_t \sim N(0, 1)$.

    - A **large positive $z_t$** means $p_t^A$ is much higher than predicted by $\hat{\beta}_{t|t-1} p_t^B$: asset A is "expensive" relative to B. The spread $p_t^A - \beta_t p_t^B$ is unusually wide. If the spread is mean-reverting (which the model assumes), we expect it to narrow. The trading signal: **go short the spread** (short A, long $\beta$ units of B).

    - A **large negative $z_t$** means $p_t^A$ is much lower than predicted: asset A is "cheap" relative to B. The spread is unusually narrow. We expect it to widen. The trading signal: **go long the spread** (long A, short $\beta$ units of B).

    The standardization by $\sqrt{S_t}$ is crucial: it adjusts the signal threshold for the current level of uncertainty. When $S_t$ is large (uncertain hedge ratio, volatile market), the same raw innovation $e_t$ produces a smaller $z_t$, reducing false signals.

---

**Exercise 3.** The Extended Kalman Filter linearizes nonlinear dynamics around the current estimate. For the stochastic volatility model $h_t = \mu + \phi(h_{t-1} - \mu) + \sigma_\eta \eta_t$ and $r_t = \exp(h_t / 2) \varepsilon_t$: (a) Identify the state equation $f(x) = \mu + \phi(x - \mu)$ and observation function $h(x) = \exp(x/2) \varepsilon$. (b) Compute the Jacobians $F_t = \partial f / \partial x = \phi$ and $H_t = \partial h / \partial x|_{x = \hat{h}_{t|t-1}}$. (c) Explain why the EKF is unreliable for this model: the observation equation $r_t = e^{h_t/2}\varepsilon_t$ is highly nonlinear and the linearization error can be large when volatility changes rapidly.

??? success "Solution to Exercise 3"
    **(a)** The state equation is $f(x) = \mu + \phi(x - \mu)$, which is linear in $x$ (affine, strictly speaking). The observation function relates the return to the log-variance: given $h_t = x_t$, $r_t = \exp(x_t/2)\,\varepsilon_t$. However, the "observation function" in the traditional sense is not simply $h(x) = \exp(x/2)\varepsilon$ because $\varepsilon_t$ is the noise itself, not an additive perturbation. More precisely, $y_t = r_t$ with conditional density $p(r_t \mid h_t) = \mathcal{N}(0, e^{h_t})$, so the observation is nonlinearly related to the state.

    **(b)** The Jacobians:

    State Jacobian: $F_t = \partial f/\partial x = \phi$ (constant, since the state equation is linear).

    For the EKF, we need to linearize the observation equation. If we (informally) write $r_t \approx \exp(\hat{h}_{t|t-1}/2)\varepsilon_t$ and treat the "observation function" as $h(x) = 0$ (the mean of $r_t$ given $h_t$ is zero for all $h_t$), the linearization is trivially $H_t = 0$, which provides no information. This is one reason the EKF fails.

    A common workaround is to transform the observation. Taking $y_t = \log r_t^2 = h_t + \log \varepsilon_t^2$. Now $\log \varepsilon_t^2$ has a $\log\chi^2(1)$ distribution, which is non-Gaussian but additive. We can write $y_t = h_t + \xi_t$ where $\xi_t = \log \varepsilon_t^2$ has mean $-1.27$ and variance $\pi^2/2 \approx 4.93$. This makes the observation equation linear: $H_t = 1$.

    **(c)** The EKF is unreliable for this model because:

    1. The original observation equation is multiplicatively nonlinear: $r_t = e^{h_t/2}\varepsilon_t$. The conditional mean $\mathbb{E}[r_t \mid h_t] = 0$ for all $h_t$, so first-order linearization around the predicted state carries zero information about $h_t$ from the observation $r_t$.
    2. Even with the $\log r_t^2$ transformation, the noise $\log\varepsilon_t^2$ is highly non-Gaussian (it is a shifted log-chi-squared distribution with heavy left tail and substantial skewness). The Kalman framework assumes Gaussian errors, so the posterior approximation can be poor.
    3. During rapid volatility changes, the linearization error compounds across time steps, potentially causing filter divergence.

    This is why particle filters (or quasi-likelihood methods that approximate $\log\varepsilon_t^2$ as Gaussian) are preferred for stochastic volatility models.

---

**Exercise 4.** A bootstrap particle filter for the stochastic volatility model uses $N = 1000$ particles. At time $t$, after propagation and weighting, the effective sample size is $N_{\text{eff}} = 1/\sum_i (w_t^{(i)})^2 = 150$. (a) Since $N_{\text{eff}} < N/2 = 500$, resampling is triggered. Describe the systematic resampling algorithm and explain why it has lower variance than multinomial resampling. (b) After resampling, all weights are reset to $1/N$. Explain the particle degeneracy problem: after many resampling steps, most particles may descend from the same ancestor. (c) Propose a resample-move step using an MCMC kernel to rejuvenate diversity. What is the target distribution for the MCMC step?

??? success "Solution to Exercise 4"
    **(a) Systematic resampling algorithm:** Given $N$ particles with normalized weights $\{w_t^{(i)}\}_{i=1}^N$:

    1. Compute the cumulative distribution $c_i = \sum_{j=1}^i w_t^{(j)}$ for $i = 1, \ldots, N$.
    2. Draw a single uniform random number $u_1 \sim \text{Uniform}(0, 1/N)$.
    3. Set the resampling points $u_i = u_1 + (i-1)/N$ for $i = 1, \ldots, N$.
    4. For each $i$, find the smallest $j$ such that $c_j \geq u_i$, and set the resampled particle $x_t^{(i)} = \tilde{x}_t^{(j)}$.

    **Why lower variance than multinomial:** Multinomial resampling draws $N$ independent samples from the categorical distribution, so each particle's replication count has variance $Nw^{(i)}(1 - w^{(i)})$. Systematic resampling uses a single random number and equally spaced thresholds, which enforces that particle $i$ is replicated approximately $Nw^{(i)}$ times (the count is either $\lfloor Nw^{(i)} \rfloor$ or $\lceil Nw^{(i)} \rceil$). The variance of the replication counts is much lower, leading to a better approximation of the target distribution.

    **(b) Particle degeneracy:** After resampling, particles with high weights are duplicated while those with low weights are eliminated. Over many time steps, the genealogy of the particles collapses: tracing any particle back through its ancestor chain, one finds that after $\tau$ resampling steps, all current particles typically descend from a single ancestor at time $t - \tau$. This means the particle approximation of the joint smoothing distribution $p(x_{1:t} \mid y_{1:t})$ deteriorates rapidly -- there is essentially only one distinct path history.

    For filtering (estimating $p(x_t \mid y_{1:t})$ at the current time), degeneracy is less severe because the propagation step introduces fresh randomness. But for smoothing or estimating functionals of the full path, degeneracy is a fundamental problem.

    **(c) Resample-move step:** After resampling, apply one or more MCMC (Markov chain Monte Carlo) steps to each particle. Specifically, for each resampled particle $x_t^{(i)}$, run a Metropolis-Hastings kernel with target distribution:

    $$
    \pi(x_t) = p(x_t \mid y_{1:t}) \propto p(y_t \mid x_t)\, p(x_t \mid y_{1:t-1})
    $$

    In practice, propose $x_t' \sim q(x_t' \mid x_t^{(i)})$ and accept with probability:

    $$
    \alpha = \min\!\left(1, \frac{p(y_t \mid x_t')\, p(x_t' \mid x_{t-1}^{(i)})}{p(y_t \mid x_t^{(i)})\, p(x_t^{(i)} \mid x_{t-1}^{(i)})} \cdot \frac{q(x_t^{(i)} \mid x_t')}{q(x_t' \mid x_t^{(i)})}\right)
    $$

    This moves duplicate particles to different locations in the state space (rejuvenation), restoring diversity while preserving the correct target distribution. The cost is additional likelihood evaluations per MCMC step.

---

**Exercise 5.** Compare the Kalman filter and particle filter for a dynamic factor model with two latent factors and 10 observed asset returns. (a) For the linear-Gaussian factor model, the Kalman filter gives exact posterior inference. What are the computational costs per time step in terms of the state dimension $n_x = 2$ and observation dimension $n_y = 10$? (b) A particle filter with $N = 500$ particles is applied to the same model. Compute the cost per time step and compare with the Kalman filter. (c) When would you prefer the particle filter despite its higher cost? Describe a modification to the factor model (e.g., regime-switching factor dynamics, Student-$t$ errors) that requires particle methods.

??? success "Solution to Exercise 5"
    **(a) Kalman filter cost for the linear-Gaussian factor model:**

    With $n_x = 2$ latent factors and $n_y = 10$ observed returns, the Kalman filter operations per time step are:

    - Prediction: $O(n_x^2) = O(4)$ for state covariance update
    - Innovation covariance: $S_t = C P_{t|t-1} C^\top + R$ requires $O(n_y^2 n_x) = O(200)$ to form $CP_{t|t-1}C^\top$ and $O(n_y^2) = O(100)$ for the addition
    - Kalman gain: $K_t = P_{t|t-1}C^\top S_t^{-1}$ requires $O(n_y^3) = O(1000)$ for inverting $S_t$ (or solving the linear system) and $O(n_x n_y^2) = O(200)$ for the product
    - State update: $O(n_x n_y) = O(20)$
    - Covariance update: $O(n_x^2 n_y) = O(40)$

    Total: $O(n_x^2 n_y + n_y^3) = O(40 + 1000) = O(1000)$ per step, dominated by the $O(n_y^3)$ matrix inversion.

    **(b) Particle filter cost:**

    With $N = 500$ particles, at each time step:

    - Propagate: $N$ draws from a 2-dimensional Gaussian: $O(N n_x^2) = O(2000)$
    - Weight: $N$ evaluations of a 10-dimensional Gaussian density: $O(N n_y^2) = O(50{,}000)$
    - Normalize: $O(N) = O(500)$
    - Resample (when needed): $O(N) = O(500)$

    Total: $O(N n_y^2) = O(50{,}000)$ per step.

    Comparison: the particle filter is about 50 times more expensive than the Kalman filter for this model, and it only provides an approximate solution where the Kalman filter gives the exact answer.

    **(c) When the particle filter is preferred:**

    The particle filter becomes necessary when the model departs from the linear-Gaussian framework. Examples:

    - **Regime-switching factor dynamics:** $f_t = \Phi_{s_t} f_{t-1} + u_t$ where $s_t$ is a latent Markov regime indicator. The posterior is a mixture of Gaussians with exponentially growing components, making exact inference intractable.
    - **Student-$t$ errors:** $\varepsilon_t \sim t_\nu$ instead of Gaussian. The posterior is no longer Gaussian, so the Kalman filter's sufficient statistics (mean and covariance) do not fully describe it.
    - **Nonlinear factor dynamics:** $f_t = g(f_{t-1}) + u_t$ for nonlinear $g$ (e.g., a threshold model or stochastic volatility on the factors).
    - **Non-Gaussian state noise:** Jump-diffusion factor dynamics where $u_t$ includes rare large jumps.

    In all these cases, the particle filter's ability to represent arbitrary distributions via weighted samples makes it the method of choice, despite its higher computational cost.

---

**Exercise 6.** The Unscented Kalman Filter propagates $2n_x + 1$ sigma points through the nonlinear functions. For a 3-dimensional state ($n_x = 3$): (a) How many sigma points are needed? (b) Describe how the sigma points are constructed from the mean $\hat{x}$ and covariance $P$ of the current estimate. (c) After propagation through $f$, the predicted mean and covariance are computed as weighted averages of the propagated sigma points. Explain why this captures the mean and covariance to third-order accuracy for Gaussian inputs, while the EKF linearization is only first-order accurate. (d) For the stochastic volatility model, would the UKF perform significantly better than the EKF?

??? success "Solution to Exercise 6"
    **(a)** For $n_x = 3$, the UKF requires $2n_x + 1 = 2(3) + 1 = 7$ sigma points.

    **(b)** Construction of sigma points from mean $\hat{x} \in \mathbb{R}^3$ and covariance $P \in \mathbb{R}^{3 \times 3}$:

    First compute the matrix square root $L$ such that $(n_x + \kappa)P = LL^\top$ (e.g., via Cholesky decomposition). Let $L_i$ denote the $i$-th column of $L$.

    The $7$ sigma points are:

    $$
    \chi_0 = \hat{x}
    $$

    $$
    \chi_i = \hat{x} + L_i, \quad i = 1, 2, 3
    $$

    $$
    \chi_{i+3} = \hat{x} - L_i, \quad i = 1, 2, 3
    $$

    The weights are: $w_0 = \kappa/(n_x + \kappa)$ for the center point, and $w_i = 1/(2(n_x + \kappa))$ for $i = 1, \ldots, 6$. With $\kappa = 0$ (a common choice for $n_x = 3$): $w_0 = 0$, $w_i = 1/6$ for $i = 1, \ldots, 6$.

    **(c)** The UKF captures mean and covariance to third-order accuracy because the sigma points are chosen to exactly match the first two moments (mean and covariance) of the prior Gaussian distribution. When these sigma points are propagated through a nonlinear function $f$, the resulting weighted mean and covariance capture:

    - The correct mean $\mathbb{E}[f(x)]$ up to third order in the Taylor expansion (the first and second derivative terms are captured exactly for polynomial nonlinearities up to degree 3).
    - The correct covariance up to second order.

    The EKF linearization $f(x) \approx f(\hat{x}) + F(x - \hat{x})$ only captures the first-order Taylor term. It misses the contribution of the Hessian and higher-order terms to the mean (e.g., $\mathbb{E}[f(x)] \neq f(\mathbb{E}[x])$ for nonlinear $f$). For a quadratic function $f(x) = x^2$, the EKF predicts $\mathbb{E}[f(x)] = \hat{x}^2$ while the truth is $\hat{x}^2 + P$. The UKF captures this exactly.

    **(d)** For the stochastic volatility model, the improvement of UKF over EKF depends on the specific formulation:

    - For the original observation $r_t = e^{h_t/2}\varepsilon_t$: both EKF and UKF struggle because the conditional mean of $r_t$ given $h_t$ is zero regardless of $h_t$. The information about $h_t$ is in the conditional variance, not the mean, and the standard EKF/UKF framework targets the mean.
    - For the transformed observation $y_t = \log r_t^2 = h_t + \log\varepsilon_t^2$: the observation equation is actually **linear** in $h_t$, so EKF and UKF produce identical results. The main issue is the non-Gaussianity of $\log\varepsilon_t^2$, which neither method handles well.

    Therefore, the UKF does **not** provide a significant improvement over the EKF for this particular model. The fundamental challenge is non-Gaussian noise, not nonlinearity, and particle filters remain the preferred approach.

---

**Exercise 7.** A risk manager uses a particle filter to track the latent volatility of an asset. The posterior at time $t$ is represented by 1000 weighted particles $\{(\sigma_t^{2,(i)}, w_t^{(i)})\}$. (a) Compute the posterior mean $\hat{\sigma}_t^2 = \sum_i w_t^{(i)} \sigma_t^{2,(i)}$ and a 95% credible interval for $\sigma_t^2$. (b) Compare this with a GARCH(1,1) model that provides only a point estimate. Why is the full posterior distribution valuable for risk management? (c) Use the posterior distribution of $\sigma_t^2$ to compute a model-uncertainty-adjusted VaR: $\text{VaR}_\alpha = \mathbb{E}_{\sigma^2 \sim p(\sigma_t^2 | y_{1:t})}[\Phi^{-1}(\alpha) \cdot \sigma]$. Explain why this is wider than the VaR computed using only the point estimate $\hat{\sigma}_t^2$.

??? success "Solution to Exercise 7"
    **(a)** The posterior mean of the variance is:

    $$
    \hat{\sigma}_t^2 = \sum_{i=1}^{1000} w_t^{(i)}\, \sigma_t^{2,(i)}
    $$

    This is a weighted average of the 1000 particle values of $\sigma_t^2$.

    For the 95% credible interval, sort the particles by $\sigma_t^{2,(i)}$ and find the 2.5th and 97.5th weighted percentiles. Concretely:

    1. Sort the particles: $\sigma_t^{2,(\pi(1))} \leq \sigma_t^{2,(\pi(2))} \leq \cdots \leq \sigma_t^{2,(\pi(1000))}$ (where $\pi$ is the sorting permutation).
    2. Compute cumulative weights: $W_k = \sum_{j=1}^k w_t^{(\pi(j))}$.
    3. The lower bound $\sigma_L^2$ is the particle value where $W_k$ first exceeds $0.025$.
    4. The upper bound $\sigma_U^2$ is the particle value where $W_k$ first exceeds $0.975$.

    The 95% credible interval is $[\sigma_L^2, \sigma_U^2]$.

    **(b)** GARCH(1,1) produces a single deterministic estimate $\hat{\sigma}_t^2 = \omega + \alpha r_{t-1}^2 + \beta \hat{\sigma}_{t-1}^2$ with no associated uncertainty. The full posterior distribution from the particle filter is valuable for risk management because:

    - **Uncertainty quantification:** The width of the credible interval tells the risk manager how confident the volatility estimate is. A wide interval during turbulent markets signals that risk estimates themselves are uncertain.
    - **Tail risk:** The right tail of the posterior on $\sigma_t^2$ directly feeds into worst-case risk assessments. A GARCH point estimate might suggest moderate volatility, but the posterior might assign non-trivial probability to much higher volatility.
    - **Decision-making under ambiguity:** A risk manager can make conservative decisions by considering the upper end of the credible interval, providing a buffer against model uncertainty.
    - **Model diagnostics:** Multimodal posteriors suggest regime ambiguity; very wide posteriors signal insufficient information.

    **(c)** The model-uncertainty-adjusted VaR integrates over the posterior distribution of volatility:

    $$
    \text{VaR}_\alpha = \mathbb{E}_{\sigma^2 \sim p(\sigma_t^2 | y_{1:t})}[\Phi^{-1}(\alpha) \cdot \sigma] = \sum_{i=1}^{1000} w_t^{(i)}\, \Phi^{-1}(\alpha) \cdot \sqrt{\sigma_t^{2,(i)}}
    $$

    Since $\Phi^{-1}(\alpha) < 0$ for $\alpha < 0.5$ (e.g., $\Phi^{-1}(0.01) = -2.326$), this is:

    $$
    \text{VaR}_\alpha = \Phi^{-1}(\alpha) \cdot \mathbb{E}[\sigma_t \mid y_{1:t}]
    $$

    The point-estimate VaR uses $\hat{\sigma}_t = \sqrt{\hat{\sigma}_t^2}$:

    $$
    \text{VaR}_\alpha^{\text{point}} = \Phi^{-1}(\alpha) \cdot \sqrt{\hat{\sigma}_t^2}
    $$

    By Jensen's inequality, since $\sigma \mapsto \sqrt{\sigma^2}$ is concave:

    $$
    \mathbb{E}[\sigma_t \mid y_{1:t}] = \mathbb{E}[\sqrt{\sigma_t^2} \mid y_{1:t}] \geq \sqrt{\mathbb{E}[\sigma_t^2 \mid y_{1:t}]} = \sqrt{\hat{\sigma}_t^2}
    $$

    Wait -- actually $\sqrt{\cdot}$ is concave, so Jensen gives $\mathbb{E}[\sqrt{\sigma_t^2}] \leq \sqrt{\mathbb{E}[\sigma_t^2]}$, which would make the adjusted VaR *less* extreme. However, the correct interpretation requires care with the sign.

    The more relevant argument is that the model-uncertainty-adjusted VaR should be computed as:

    $$
    \text{VaR}_\alpha = \mathbb{E}_{\sigma^2}\left[\Phi^{-1}(\alpha) \cdot \sigma\right] = \Phi^{-1}(\alpha) \cdot \mathbb{E}[\sigma]
    $$

    But a better formulation integrates over the full return distribution:

    $$
    P(r_t \leq -\text{VaR}) = \mathbb{E}_{\sigma^2}\left[\Phi\!\left(\frac{-\text{VaR}}{\sigma}\right)\right] = \alpha
    $$

    This is the predictive probability. By the convexity of $\Phi(-\text{VaR}/\sigma)$ in $\sigma$ (for $\text{VaR} > 0$), Jensen's inequality gives:

    $$
    \mathbb{E}\left[\Phi\!\left(\frac{-\text{VaR}}{\sigma}\right)\right] \geq \Phi\!\left(\frac{-\text{VaR}}{\mathbb{E}[\sigma]}\right)
    $$

    This means the tail probability under the mixture is larger than under the point estimate, so the VaR threshold must be more extreme (larger in absolute value) to achieve the same $\alpha$ level. The model-uncertainty-adjusted VaR is therefore wider (more conservative) than the point-estimate VaR. Intuitively, the posterior uncertainty about $\sigma_t^2$ creates a mixture of normals with different scales, which has heavier tails than a single normal at the mean volatility.
