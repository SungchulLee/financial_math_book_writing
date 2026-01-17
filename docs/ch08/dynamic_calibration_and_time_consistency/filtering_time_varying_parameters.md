# Filtering for Time-Varying Parameters

When parameters are treated as time-varying state variables, **filtering** provides a principled framework for sequential estimation. Rather than recalibrating from scratch each day, filtering updates beliefs about parameters as new data arrive, respecting both model dynamics and observation uncertainty.

---

## The filtering framework

### State-space formulation

Consider a model where parameters $\theta_t$ evolve over time:

**State equation:**
$$
\theta_{t+1} = f(\theta_t) + \eta_t, \qquad \eta_t \sim \mathcal{N}(0, Q),
$$

**Observation equation:**
$$
y_t = h(\theta_t) + \varepsilon_t, \qquad \varepsilon_t \sim \mathcal{N}(0, R),
$$

where:

- $\theta_t \in \mathbb{R}^d$ is the (unobserved) parameter state.
- $y_t \in \mathbb{R}^m$ is the observed market data (option prices, implied vols).
- $f$ describes parameter dynamics (often $f(\theta) = \theta$ for random walk).
- $h$ is the pricing function (forward map).
- $Q$ is state noise covariance (parameter uncertainty growth).
- $R$ is observation noise covariance (market data noise).

### The filtering problem

Given observations $y_1, \ldots, y_t$, estimate the posterior:

$$
p(\theta_t \mid y_{1:t}).
$$

This provides:

- A point estimate: $\hat{\theta}_t = \mathbb{E}[\theta_t \mid y_{1:t}]$.
- Uncertainty quantification: $\text{Cov}(\theta_t \mid y_{1:t})$.
- A principled update rule as new data $y_{t+1}$ arrives.

---

## The Kalman filter

When both $f$ and $h$ are linear and noise is Gaussian, the Kalman filter provides exact, closed-form updates.

### Linear state-space model

$$
\theta_{t+1} = A \theta_t + \eta_t, \qquad y_t = H \theta_t + \varepsilon_t.
$$

### Kalman filter recursion

**Predict:**
$$
\hat{\theta}_{t|t-1} = A \hat{\theta}_{t-1|t-1}, \qquad P_{t|t-1} = A P_{t-1|t-1} A^\top + Q.
$$

**Update:**
$$
K_t = P_{t|t-1} H^\top (H P_{t|t-1} H^\top + R)^{-1},
$$
$$
\hat{\theta}_{t|t} = \hat{\theta}_{t|t-1} + K_t (y_t - H \hat{\theta}_{t|t-1}),
$$
$$
P_{t|t} = (I - K_t H) P_{t|t-1}.
$$

### Interpretation

- $K_t$ is the **Kalman gain**: balances trust in prediction vs. observation.
- Large $R$ (noisy data): rely more on prediction.
- Large $Q$ (uncertain dynamics): rely more on observation.

### Limitations for calibration

In option pricing:

- $h(\theta)$ is nonlinear (Black–Scholes, Heston pricing).
- Parameters may have constraints (positivity, bounds).
- Observation dimension $m$ can be large (many options).

The standard Kalman filter does not apply directly.

---

## The extended Kalman filter (EKF)

The EKF handles nonlinearity by linearizing around the current estimate.

### Linearization

At each step, approximate:

$$
h(\theta) \approx h(\hat{\theta}_{t|t-1}) + H_t (\theta - \hat{\theta}_{t|t-1}),
$$

where $H_t = \nabla_\theta h(\hat{\theta}_{t|t-1})$ is the Jacobian (sensitivity of prices to parameters).

### EKF recursion

Same structure as Kalman filter, but with $H_t$ evaluated at the current estimate:

**Predict:**
$$
\hat{\theta}_{t|t-1} = f(\hat{\theta}_{t-1|t-1}), \qquad P_{t|t-1} = F_t P_{t-1|t-1} F_t^\top + Q,
$$

where $F_t = \nabla_\theta f(\hat{\theta}_{t-1|t-1})$.

**Update:**
$$
K_t = P_{t|t-1} H_t^\top (H_t P_{t|t-1} H_t^\top + R)^{-1},
$$
$$
\hat{\theta}_{t|t} = \hat{\theta}_{t|t-1} + K_t (y_t - h(\hat{\theta}_{t|t-1})),
$$
$$
P_{t|t} = (I - K_t H_t) P_{t|t-1}.
$$

### Advantages

- Computationally efficient (comparable to optimization-based calibration).
- Provides uncertainty estimates automatically.
- Smooth parameter evolution (no discontinuous jumps).

### Disadvantages

- Linearization can be poor for highly nonlinear $h$.
- Gaussian approximation may be inadequate.
- Requires Jacobian computation (can use finite differences).

---

## The unscented Kalman filter (UKF)

The UKF avoids explicit linearization by propagating carefully chosen "sigma points" through the nonlinear functions.

### Sigma points

For state dimension $d$, choose $2d + 1$ sigma points:

$$
\chi_0 = \hat{\theta}, \quad \chi_i = \hat{\theta} + \sqrt{(d + \lambda) P} \big|_i, \quad \chi_{i+d} = \hat{\theta} - \sqrt{(d + \lambda) P} \big|_i,
$$

where $\sqrt{(d + \lambda) P}|_i$ denotes the $i$-th column of the matrix square root, and $\lambda$ is a scaling parameter.

### Propagation

Transform sigma points through $f$ and $h$:

$$
\chi_i^{-} = f(\chi_i), \qquad \gamma_i = h(\chi_i^{-}).
$$

Compute weighted means and covariances from the transformed points.

### Advantages over EKF

- Captures nonlinearity more accurately (second-order accuracy vs. first-order for EKF).
- No Jacobian computation required.
- Often more robust for highly nonlinear problems.

### Disadvantages

- More function evaluations per step ($2d + 1$ vs. 1 for EKF).
- Still assumes Gaussian distributions.

---

## Particle filters

Particle filters (sequential Monte Carlo) handle arbitrary nonlinearity and non-Gaussianity by representing the posterior with a set of weighted samples ("particles").

### Algorithm outline

1. **Initialize:** Draw $N$ particles $\{\theta_0^{(i)}\}_{i=1}^N$ from prior.

2. **Predict:** Propagate each particle through state dynamics:
   $$
   \tilde{\theta}_t^{(i)} = f(\theta_{t-1}^{(i)}) + \eta_t^{(i)}.
   $$

3. **Update:** Compute importance weights based on likelihood:
   $$
   w_t^{(i)} \propto p(y_t \mid \tilde{\theta}_t^{(i)}).
   $$

4. **Resample:** Draw $N$ particles from $\{\tilde{\theta}_t^{(i)}\}$ with probabilities $\{w_t^{(i)}\}$.

5. **Repeat** for next time step.

### Advantages

- Handles arbitrary distributions and nonlinearities.
- Naturally accommodates constraints (reject invalid particles).
- Provides full posterior, not just mean and covariance.

### Disadvantages

- Computationally expensive (many particles needed for high-dimensional $\theta$).
- Degeneracy: weights concentrate on few particles over time.
- Requires careful tuning (number of particles, resampling strategy).

### Practical considerations

For option model calibration:

- Each particle requires pricing all observed options (expensive).
- Parallelization helps (particles are independent).
- Typically feasible for $d \le 5$–$10$ parameters.

---

## Application to Heston model

### State vector

For Heston with time-varying parameters:

$$
\theta_t = (v_t, \kappa_t, \bar{v}_t, \sigma_{v,t}, \rho_t)^\top.
$$

Often, only $v_t$ (spot variance) is treated as rapidly varying; others are slowly varying or fixed.

### Observation model

Observe implied volatilities at strikes $K_j$ and maturities $T_j$:

$$
y_t = (\sigma_{\text{impl}}(K_1, T_1; \theta_t), \ldots, \sigma_{\text{impl}}(K_m, T_m; \theta_t))^\top + \varepsilon_t.
$$

The function $h(\theta) = (\sigma_{\text{impl}}(K_j, T_j; \theta))_j$ requires Heston pricing and implied vol inversion.

### State dynamics

A simple random walk model:

$$
\theta_{t+1} = \theta_t + \eta_t, \qquad \eta_t \sim \mathcal{N}(0, Q).
$$

The covariance $Q$ encodes beliefs about parameter stability:

- Small diagonal entries for stable parameters ($\kappa$, $\bar{v}$).
- Larger entries for volatile parameters ($v_0$, $\rho$).

### Filtering results

Filtering produces:

- Daily parameter estimates $\hat{\theta}_t$ that evolve smoothly.
- Confidence intervals reflecting both data noise and parameter uncertainty.
- Automatic adaptation to market conditions without ad-hoc smoothing.

---

## Choosing filter hyperparameters

### State noise covariance $Q$

$Q$ controls how much parameters are allowed to change between observations:

- Too small: filter ignores genuine parameter changes (under-reactive).
- Too large: filter tracks noise (over-reactive).

**Estimation approaches:**

- Maximum likelihood on historical data.
- Cross-validation: choose $Q$ minimizing out-of-sample prediction error.
- Expert judgment based on expected parameter stability.

### Observation noise covariance $R$

$R$ reflects uncertainty in market data:

- Diagonal entries proportional to bid-ask spreads squared.
- Off-diagonal entries often set to zero (independent noise).

### Number of particles (for particle filters)

- More particles = better approximation but higher cost.
- Rule of thumb: start with $N = 1000$–$10000$; increase if results are noisy.

---

## Comparison: filtering vs. recalibration

| Aspect | Daily recalibration | Filtering |
|--------|---------------------|-----------|
| Parameter continuity | Discontinuous jumps | Smooth evolution |
| Uncertainty quantification | Requires bootstrap | Built-in |
| Computational cost | One optimization per day | Sequential updates |
| Theoretical foundation | Ad-hoc | Bayesian optimal |
| Handling of noise | Overfits if not regularized | Principled noise model |
| Complexity | Simple implementation | More complex setup |

### When to prefer filtering

- Parameters are genuinely time-varying.
- Smooth parameter paths are important for hedging.
- Uncertainty quantification is needed.
- Sufficient computational resources for particle methods.

### When to prefer recalibration

- Parameters are approximately constant (recalibrate infrequently).
- Simplicity is paramount.
- Filtering infrastructure is unavailable.

---

## Joint filtering of state and parameters

In models like Heston, the variance $v_t$ is a latent state with known dynamics, while $(\kappa, \bar{v}, \sigma_v, \rho)$ are parameters.

### Augmented state approach

Augment the state vector:

$$
x_t = (v_t, \kappa, \bar{v}, \sigma_v, \rho)^\top.
$$

Apply filtering to $x_t$, treating parameters as slowly evolving states.

### Rao–Blackwellization

If some components are linear-Gaussian given others, exploit this structure:

- Filter parameters with particles.
- Conditional on parameters, filter $v_t$ with Kalman filter.

This reduces variance and improves efficiency.

---

## Key takeaways

- Filtering provides a principled framework for sequential parameter estimation.
- The Kalman filter applies to linear-Gaussian cases; EKF and UKF handle nonlinearity.
- Particle filters handle arbitrary distributions but are computationally expensive.
- Filtering produces smooth parameter paths and automatic uncertainty quantification.
- Hyperparameters ($Q$, $R$, number of particles) require careful tuning.
- Filtering is complementary to, not a replacement for, good model specification.

---

## Further reading

- Durbin & Koopman, *Time Series Analysis by State Space Methods*.
- Simon, *Optimal State Estimation* (Kalman, EKF, UKF).
- Doucet, de Freitas & Gordon, *Sequential Monte Carlo Methods in Practice*.
- Johannes, Polson & Stroud, "Optimal Filtering of Jump Diffusions" (2009).
- Bates, "Maximum Likelihood Estimation of Latent Affine Processes" (2006).
