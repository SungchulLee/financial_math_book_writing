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

---

**Exercise 2.** In a pairs trading application, the state-space model is $\beta_t = \beta_{t-1} + w_t$ with $w_t \sim \mathcal{N}(0, Q)$ and $p_t^A = \beta_t p_t^B + v_t$ with $v_t \sim \mathcal{N}(0, R)$. Suppose $Q = 10^{-5}$, $R = 0.01$, and $p_t^B = 50$. (a) Write the observation equation in standard form $y_t = C_t x_t + v_t$ identifying $C_t$, $y_t$, and $x_t$. (b) If the current Kalman gain is $K_t = 0.02$, the current estimate is $\hat{\beta}_{t-1|t-1} = 1.05$, and we observe $p_t^A = 53.5$, compute the innovation $e_t$ and the updated estimate $\hat{\beta}_{t|t}$. (c) The standardized innovation $e_t / \sqrt{S_t}$ is used as a trading signal. Explain why a large positive value suggests the spread is too wide (go short spread) and a large negative value suggests it is too narrow (go long spread).

---

**Exercise 3.** The Extended Kalman Filter linearizes nonlinear dynamics around the current estimate. For the stochastic volatility model $h_t = \mu + \phi(h_{t-1} - \mu) + \sigma_\eta \eta_t$ and $r_t = \exp(h_t / 2) \varepsilon_t$: (a) Identify the state equation $f(x) = \mu + \phi(x - \mu)$ and observation function $h(x) = \exp(x/2) \varepsilon$. (b) Compute the Jacobians $F_t = \partial f / \partial x = \phi$ and $H_t = \partial h / \partial x|_{x = \hat{h}_{t|t-1}}$. (c) Explain why the EKF is unreliable for this model: the observation equation $r_t = e^{h_t/2}\varepsilon_t$ is highly nonlinear and the linearization error can be large when volatility changes rapidly.

---

**Exercise 4.** A bootstrap particle filter for the stochastic volatility model uses $N = 1000$ particles. At time $t$, after propagation and weighting, the effective sample size is $N_{\text{eff}} = 1/\sum_i (w_t^{(i)})^2 = 150$. (a) Since $N_{\text{eff}} < N/2 = 500$, resampling is triggered. Describe the systematic resampling algorithm and explain why it has lower variance than multinomial resampling. (b) After resampling, all weights are reset to $1/N$. Explain the particle degeneracy problem: after many resampling steps, most particles may descend from the same ancestor. (c) Propose a resample-move step using an MCMC kernel to rejuvenate diversity. What is the target distribution for the MCMC step?

---

**Exercise 5.** Compare the Kalman filter and particle filter for a dynamic factor model with two latent factors and 10 observed asset returns. (a) For the linear-Gaussian factor model, the Kalman filter gives exact posterior inference. What are the computational costs per time step in terms of the state dimension $n_x = 2$ and observation dimension $n_y = 10$? (b) A particle filter with $N = 500$ particles is applied to the same model. Compute the cost per time step and compare with the Kalman filter. (c) When would you prefer the particle filter despite its higher cost? Describe a modification to the factor model (e.g., regime-switching factor dynamics, Student-$t$ errors) that requires particle methods.

---

**Exercise 6.** The Unscented Kalman Filter propagates $2n_x + 1$ sigma points through the nonlinear functions. For a 3-dimensional state ($n_x = 3$): (a) How many sigma points are needed? (b) Describe how the sigma points are constructed from the mean $\hat{x}$ and covariance $P$ of the current estimate. (c) After propagation through $f$, the predicted mean and covariance are computed as weighted averages of the propagated sigma points. Explain why this captures the mean and covariance to third-order accuracy for Gaussian inputs, while the EKF linearization is only first-order accurate. (d) For the stochastic volatility model, would the UKF perform significantly better than the EKF?

---

**Exercise 7.** A risk manager uses a particle filter to track the latent volatility of an asset. The posterior at time $t$ is represented by 1000 weighted particles $\{(\sigma_t^{2,(i)}, w_t^{(i)})\}$. (a) Compute the posterior mean $\hat{\sigma}_t^2 = \sum_i w_t^{(i)} \sigma_t^{2,(i)}$ and a 95% credible interval for $\sigma_t^2$. (b) Compare this with a GARCH(1,1) model that provides only a point estimate. Why is the full posterior distribution valuable for risk management? (c) Use the posterior distribution of $\sigma_t^2$ to compute a model-uncertainty-adjusted VaR: $\text{VaR}_\alpha = \mathbb{E}_{\sigma^2 \sim p(\sigma_t^2 | y_{1:t})}[\Phi^{-1}(\alpha) \cdot \sigma]$. Explain why this is wider than the VaR computed using only the point estimate $\hat{\sigma}_t^2$.
