# Filtering for Time-Varying Parameters

When parameters are treated as time-varying state variables, **filtering** provides a principled framework for sequential estimation. Rather than recalibrating from scratch each day, filtering updates beliefs about parameters as new data arrive, respecting both model dynamics and observation uncertainty.

---

## The filtering framework

### State-space formulation

Consider a model where parameters $\theta_t$ evolve over time:

**State equation:**

$$
\theta_{t+1} = f(\theta_t) + \eta_t, \qquad \eta_t \sim \mathcal{N}(0, Q)
$$

**Observation equation:**

$$
y_t = h(\theta_t) + \varepsilon_t, \qquad \varepsilon_t \sim \mathcal{N}(0, R)
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
p(\theta_t \mid y_{1:t})
$$

This provides:

- A point estimate: $\hat{\theta}_t = \mathbb{E}[\theta_t \mid y_{1:t}]$.
- Uncertainty quantification: $\text{Cov}(\theta_t \mid y_{1:t})$.
- A principled update rule as new data $y_{t+1}$ arrives.

---

## Filter families: Kalman, EKF, UKF, particle

Recall (see [§ Online learning and adaptive calibration](../../ch24/online_learning_and_adaptive_calibration/filtering_and_bayesian_updating.md)) the standard filter families and their recursions. For calibration the salient features are:

- **Kalman filter** (linear $f$, $h$; Gaussian noise): exact closed-form updates via the Kalman gain $K_t = P_{t|t-1} H^\top (H P_{t|t-1} H^\top + R)^{-1}$. Inapplicable directly here because the option-pricing map $h(\theta)$ is nonlinear and parameters are constrained.
- **Extended Kalman filter (EKF):** linearizes $h$ via the Jacobian $H_t = \nabla_\theta h(\hat{\theta}_{t|t-1})$. Cheap and provides automatic uncertainty, but first-order accurate and sensitive to strong nonlinearity.
- **Unscented Kalman filter (UKF):** propagates $2d + 1$ sigma points through $h$, capturing second-order effects without Jacobians. Comparable cost to EKF for moderate $d$; still Gaussian.
- **Particle filter (SMC):** represents the posterior by $N$ weighted samples; handles arbitrary nonlinearity, non-Gaussianity, and hard constraints. Cost is $O(N \cdot C_h)$ per step (each particle requires a full pricing pass), so typically feasible only for $d \le 5$--$10$.

---

## Application to Heston model

### State vector

For Heston with time-varying parameters:

$$
\theta_t = (v_t, \kappa_t, \bar{v}_t, \sigma_{v,t}, \rho_t)^\top
$$

Often, only $v_t$ (spot variance) is treated as rapidly varying; others are slowly varying or fixed.

### Observation model

Observe implied volatilities at strikes $K_j$ and maturities $T_j$:

$$
y_t = (\sigma_{\text{impl}}(K_1, T_1; \theta_t), \ldots, \sigma_{\text{impl}}(K_m, T_m; \theta_t))^\top + \varepsilon_t
$$

The function $h(\theta) = (\sigma_{\text{impl}}(K_j, T_j; \theta))_j$ requires Heston pricing and implied vol inversion.

### State dynamics

A simple random walk model:

$$
\theta_{t+1} = \theta_t + \eta_t, \qquad \eta_t \sim \mathcal{N}(0, Q)
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

### State noise covariance Q

$Q$ controls how much parameters are allowed to change between observations:

- Too small: filter ignores genuine parameter changes (under-reactive).
- Too large: filter tracks noise (over-reactive).

**Estimation approaches:**

- Maximum likelihood on historical data.
- Cross-validation: choose $Q$ minimizing out-of-sample prediction error.
- Expert judgment based on expected parameter stability.

### Observation noise covariance R

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
x_t = (v_t, \kappa, \bar{v}, \sigma_v, \rho)^\top
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

---

## Exercises

**Exercise 1.** Write down the Kalman filter predict and update equations for the linear state-space model $\theta_{t+1} = A\theta_t + \eta_t$, $y_t = H\theta_t + \varepsilon_t$ with $A = I$ (random walk), $H \in \mathbb{R}^{m \times d}$. Show that the Kalman gain $K_t$ converges to a steady-state value $K_\infty$ when $Q$ and $R$ are constant. Derive $K_\infty$ for the scalar case ($d = m = 1$) in terms of $Q$ and $R$.

??? success "Solution to Exercise 1"
    **Kalman filter equations for the random walk model.** With $A = I$, the state-space model is

    $$
    \theta_{t+1} = \theta_t + \eta_t, \qquad y_t = H\theta_t + \varepsilon_t
    $$

    **Predict step:**

    $$
    \hat{\theta}_{t|t-1} = \hat{\theta}_{t-1|t-1}, \qquad P_{t|t-1} = P_{t-1|t-1} + Q
    $$

    **Update step:**

    $$
    K_t = P_{t|t-1} H^\top (H P_{t|t-1} H^\top + R)^{-1}
    $$

    $$
    \hat{\theta}_{t|t} = \hat{\theta}_{t|t-1} + K_t(y_t - H\hat{\theta}_{t|t-1})
    $$

    $$
    P_{t|t} = (I - K_t H) P_{t|t-1}
    $$

    **Steady-state convergence.** When $Q$ and $R$ are constant, the predicted covariance satisfies the recursion $P_{t|t-1} = P_{t-1|t-1} + Q = (I - K_{t-1}H)P_{t-1|t-2} + Q$. At steady state, let $P = P_{t|t-1} = P_{t-1|t-2}$ (the predicted covariance converges). Then $P$ satisfies the discrete algebraic Riccati equation

    $$
    P = P - PH^\top(HPH^\top + R)^{-1}HP + Q
    $$

    which simplifies to

    $$
    PH^\top(HPH^\top + R)^{-1}HP = Q
    $$

    The steady-state gain is $K_\infty = PH^\top(HPH^\top + R)^{-1}$.

    **Scalar case ($d = m = 1$).** Write $H = h$ (scalar), $Q = q$, $R = r$, and $P = p$ (steady-state predicted variance). The Riccati equation becomes

    $$
    \frac{p^2 h^2}{h^2 p + r} = q
    $$

    This gives $p^2 h^2 = q(h^2 p + r)$, i.e., $h^2 p^2 - qh^2 p - qr = 0$. Solving the quadratic in $p$:

    $$
    p = \frac{qh^2 + \sqrt{q^2 h^4 + 4h^2 qr}}{2h^2} = \frac{q + \sqrt{q^2 + 4qr/h^2}}{2}
    $$

    (taking the positive root). The steady-state Kalman gain is

    $$
    K_\infty = \frac{ph}{h^2 p + r} = \frac{p}{hp + r/h}
    $$

    For $h = 1$ this simplifies to $K_\infty = p/(p + r)$ where $p = (q + \sqrt{q^2 + 4qr})/2$. Observe that as $q/r \to \infty$ (fast-varying state relative to noise), $K_\infty \to 1$ (trust the observation), and as $q/r \to 0$, $K_\infty \to 0$ (trust the prediction).

---

**Exercise 2.** In the extended Kalman filter, the observation function $h(\theta)$ is linearized as $h(\theta) \approx h(\hat{\theta}_{t|t-1}) + H_t(\theta - \hat{\theta}_{t|t-1})$ where $H_t$ is the Jacobian. For the Heston model with $\theta = (v_0, \kappa, \bar{v}, \sigma_v, \rho)$ and observation $h(\theta) = \sigma_{\text{impl}}(K, T; \theta)$, explain how you would compute the Jacobian $H_t$ numerically. What are the relative merits of finite differences versus adjoint methods for this computation?

??? success "Solution to Exercise 2"
    **Numerical computation of the Jacobian.** The Jacobian $H_t \in \mathbb{R}^{m \times 5}$ has entries

    $$
    (H_t)_{jk} = \frac{\partial \sigma_{\text{impl}}(K_j, T_j; \theta)}{\partial \theta_k}\bigg|_{\theta = \hat{\theta}_{t|t-1}}
    $$

    where $\theta = (v_0, \kappa, \bar{v}, \sigma_v, \rho)$ and $j = 1, \ldots, m$ indexes observed options.

    **Finite differences.** The most straightforward approach uses central differences:

    $$
    (H_t)_{jk} \approx \frac{\sigma_{\text{impl}}(K_j, T_j; \theta + \delta_k e_k) - \sigma_{\text{impl}}(K_j, T_j; \theta - \delta_k e_k)}{2\delta_k}
    $$

    where $e_k$ is the $k$-th standard basis vector and $\delta_k$ is a small perturbation (typically $10^{-4}$ to $10^{-6}$ times $|\theta_k|$). This requires $2d = 10$ additional full pricings (each pricing all $m$ options), plus the baseline evaluation, giving $2d + 1 = 11$ total evaluations.

    **Adjoint (automatic differentiation) methods.** These compute the gradient of a scalar output with respect to all inputs in a single backward pass through the computational graph. For Heston pricing via Fourier methods (e.g., the Carr--Madan formula), the adjoint computes $\nabla_\theta C(K_j, T_j; \theta)$ at a cost of roughly 2--5 times a single forward evaluation, independent of the number of parameters $d$.

    **Relative merits:**

    - **Finite differences** are simple to implement, require no modification of the pricing code, and work with any black-box pricer. However, the cost scales as $O(d \cdot m)$ pricings and the accuracy depends on the step size $\delta_k$ (too small causes numerical cancellation; too large introduces truncation error).
    - **Adjoint methods** scale as $O(m)$ regardless of $d$, making them more efficient when $d$ is large. They provide machine-precision derivatives. However, they require differentiable pricing code (or an automatic differentiation framework), and implementing the adjoint for complex pricers (e.g., involving implied vol inversion, which itself requires Newton iteration) is nontrivial.

    For the Heston model with $d = 5$, finite differences are commonly used because the parameter dimension is small and Heston semi-analytic pricing is fast. For higher-dimensional models or real-time applications, adjoint methods are preferred.

---

**Exercise 3.** The unscented Kalman filter uses $2d + 1$ sigma points. For $d = 5$ (Heston parameters), how many sigma points are generated? If each function evaluation (pricing all observed options) takes 0.1 seconds, estimate the cost per filter update. Compare this to the EKF cost with finite-difference Jacobians using $2d$ additional evaluations.

??? success "Solution to Exercise 3"
    **Number of sigma points.** For $d = 5$, the UKF generates $2d + 1 = 11$ sigma points.

    **Cost per UKF update.** Each sigma point requires evaluating $h(\theta)$, which prices all observed options. At 0.1 seconds per evaluation:

    $$
    \text{UKF cost} = 11 \times 0.1 = 1.1 \text{ seconds per update}
    $$

    **EKF cost with finite-difference Jacobians.** The EKF requires the Jacobian $H_t$, computed via central finite differences with $2d = 10$ additional evaluations (plus one baseline), giving $2d + 1 = 11$ evaluations:

    $$
    \text{EKF cost} = 11 \times 0.1 = 1.1 \text{ seconds per update}
    $$

    **Comparison.** For $d = 5$, the UKF and EKF with finite-difference Jacobians have nearly identical computational cost (both require 11 function evaluations). However:

    - The UKF captures second-order nonlinearity effects (it is accurate to second order in the Taylor expansion), while the EKF is only first-order accurate.
    - The EKF with forward differences instead of central differences would require only $d + 1 = 6$ evaluations (0.6 seconds), at the cost of lower accuracy.
    - For larger $d$, the UKF cost ($2d + 1$ evaluations) and EKF finite-difference cost ($2d + 1$ for central, $d + 1$ for forward) scale similarly.
    - The UKF avoids potential issues with Jacobian singularity or poor linearization in highly nonlinear regions.

    In practice, for the Heston model with $d = 5$, both methods are fast enough for daily calibration (about 1 second), so the UKF is often preferred for its better nonlinear approximation.

---

**Exercise 4.** Consider a particle filter with $N$ particles for the Heston spot variance $v_t$. After the update step, suppose the effective sample size is $N_{\text{eff}} = 1/\sum_i (w_i)^2 = 15$ out of $N = 1000$ particles. Explain what this means about weight degeneracy. Describe the systematic resampling algorithm and explain how it addresses this issue.

??? success "Solution to Exercise 4"
    **Interpreting $N_{\text{eff}} = 15$ out of $N = 1000$.** The effective sample size (ESS) measures how many equally weighted particles would provide the same quality of approximation. With $N_{\text{eff}} = 15$, only about 1.5% of the particles carry meaningful weight. This indicates severe **weight degeneracy**: the posterior is concentrated in a small region of parameter space, and most particles have negligible weights. The weighted sample poorly represents the posterior distribution, leading to high variance in any estimates derived from the particle approximation.

    Quantitatively, if all weights were equal, $N_{\text{eff}} = N = 1000$. The ratio $N_{\text{eff}}/N = 15/1000 = 0.015$ is far below typical thresholds (commonly $0.5$ or $0.25$), indicating resampling is urgently needed.

    **Systematic resampling algorithm.** The algorithm proceeds as follows:

    1. Compute the cumulative weight distribution: $C_i = \sum_{j=1}^i w_j$ for $i = 1, \ldots, N$, with $C_0 = 0$.
    2. Draw a single uniform random number $u_1 \sim \text{Uniform}(0, 1/N)$.
    3. Set the sampling points $u_i = u_1 + (i-1)/N$ for $i = 1, \ldots, N$.
    4. For each $i$, find the index $j$ such that $C_{j-1} < u_i \le C_j$, and set the resampled particle $\theta_t^{(i)} = \tilde{\theta}_t^{(j)}$.

    **How systematic resampling addresses degeneracy.** After resampling, all particles have equal weight $1/N$. Particles with large weights are duplicated (proportional to their weight), while particles with negligible weights are eliminated. This restores diversity in the effective sample. A particle with weight $w_j$ is replicated approximately $N \cdot w_j$ times.

    Systematic resampling has lower variance than multinomial resampling because the evenly spaced $u_i$ values ensure a more uniform coverage of the cumulative distribution. It is also $O(N)$ in computational cost.

    The drawback is **sample impoverishment**: after resampling, many particles are identical copies, reducing diversity. To mitigate this, one can add a small jittering step (MCMC move) after resampling, or use regularized particle filters.

---

**Exercise 5.** A practitioner chooses the state noise covariance $Q = \text{diag}(q_1, \ldots, q_5)$ for the Heston parameter filter. Argue that $q_1$ (corresponding to $v_0$) should be much larger than $q_2$ (corresponding to $\kappa$). If $v_0$ is expected to change by about 0.005 per day and $\kappa$ by about 0.05 per month, estimate appropriate values for $q_1$ and $q_2$ (assuming daily observations and Gaussian transitions).

??? success "Solution to Exercise 5"
    **Argument for $q_1 \gg q_2$.** The diagonal entry $q_k$ of $Q$ represents the variance of the daily innovation in parameter $\theta_k$. Since $v_0$ (spot variance) reflects current market conditions and changes rapidly with realized volatility, while $\kappa$ (mean-reversion speed) is a structural parameter that changes only with shifts in market microstructure or monetary policy, $q_1$ should be much larger than $q_2$.

    Economically, $v_0$ responds to daily market events (earnings, macro announcements), whereas $\kappa$ reflects the speed at which variance reverts to its long-run mean, a feature of market structure that evolves on a monthly or quarterly time scale.

    **Estimating $q_1$.** If $v_0$ is expected to change by about $\Delta v_0 \approx 0.005$ per day, and we model this as a zero-mean Gaussian increment, then the standard deviation of the daily change is approximately $0.005$. Thus

    $$
    q_1 \approx (0.005)^2 = 2.5 \times 10^{-5}
    $$

    **Estimating $q_2$.** If $\kappa$ changes by about $0.05$ per month (approximately 21 trading days), the daily standard deviation is

    $$
    \sigma_{\kappa, \text{daily}} = \frac{0.05}{\sqrt{21}} \approx 0.0109
    $$

    Thus

    $$
    q_2 \approx (0.0109)^2 \approx 1.19 \times 10^{-4}
    $$

    **Ratio.** The ratio is

    $$
    \frac{q_1}{q_2} \approx \frac{2.5 \times 10^{-5}}{1.19 \times 10^{-4}} \approx 0.21
    $$

    Interestingly, this shows $q_2 > q_1$ in absolute terms. However, the parameters have very different scales: $v_0 \approx 0.04$ while $\kappa \approx 2.0$. In relative terms, the daily coefficient of variation for $v_0$ is $0.005/0.04 = 12.5\%$, while for $\kappa$ it is $0.0109/2.0 = 0.55\%$. Thus $v_0$ is far more variable in relative terms, which is the economically relevant comparison.

    If one instead works with normalized or log-transformed parameters, or if the problem specifies changes on an absolute scale for comparably scaled parameters, then $q_1 \gg q_2$ holds directly. The key practical point is that the filter's state noise covariance should reflect the actual time scale of each parameter's variation.

---

**Exercise 6.** Compare the Kalman filter, extended Kalman filter, and particle filter in terms of: (a) assumptions on linearity, (b) assumptions on noise distribution, (c) computational cost per update step, and (d) quality of uncertainty quantification. For each filter type, give one calibration scenario where it would be the preferred choice.

??? success "Solution to Exercise 6"
    **(a) Assumptions on linearity.**

    - **Kalman filter:** Requires both state transition $f$ and observation function $h$ to be linear.
    - **EKF:** Handles nonlinear $f$ and $h$ via first-order Taylor linearization around the current estimate.
    - **Particle filter:** No linearity assumptions; handles arbitrary nonlinear $f$ and $h$.

    **(b) Assumptions on noise distribution.**

    - **Kalman filter:** Requires Gaussian state and observation noise. Under these assumptions, the posterior is exactly Gaussian.
    - **EKF:** Assumes Gaussian noise; the posterior is approximated as Gaussian (which may be poor if the true posterior is multimodal or skewed).
    - **Particle filter:** No distributional assumptions. Can handle non-Gaussian, multimodal, and heavy-tailed distributions.

    **(c) Computational cost per update step.**

    - **Kalman filter:** $O(d^3 + d^2 m + m^3)$ for matrix operations (inversions, multiplications). Very fast for moderate dimensions.
    - **EKF:** Same as Kalman filter, plus the cost of computing the Jacobian $H_t$ (either analytically or via $O(d)$ finite differences, each requiring a full pricing evaluation).
    - **Particle filter:** $O(N \cdot C_h)$ where $N$ is the number of particles and $C_h$ is the cost of one function evaluation. For $N = 1000$ and expensive pricing, this can be orders of magnitude more costly.

    **(d) Quality of uncertainty quantification.**

    - **Kalman filter:** Exact posterior covariance under the linear-Gaussian assumption.
    - **EKF:** Approximate covariance; can be unreliable when nonlinearity is strong (may underestimate uncertainty in tails).
    - **Particle filter:** Converges to the true posterior as $N \to \infty$. For finite $N$, provides the most faithful uncertainty representation, including non-Gaussian features.

    **Preferred scenarios:**

    - **Kalman filter:** Filtering latent factors in an affine term-structure model where bond prices are linear in factors and noise is Gaussian. The linear-Gaussian structure is exact.
    - **EKF:** Filtering Heston spot variance $v_t$ using implied volatility observations, where the pricing function is nonlinear but smooth, and the posterior is approximately unimodal. The EKF provides a good balance of accuracy and speed.
    - **Particle filter:** Filtering parameters in a jump-diffusion model where the posterior can be multimodal (e.g., uncertainty about whether a jump has occurred), or when parameters have hard constraints (positivity, Feller condition) that make the Gaussian approximation poor.

---

**Exercise 7.** In Rao--Blackwellized particle filtering, certain state components are filtered analytically (via Kalman filter) conditional on particles for the remaining components. For the Heston model, suppose $v_t$ is filtered with particles and $(\kappa, \bar{v})$ are filtered with a Kalman filter conditional on $v_t$. Write down the conditional linear-Gaussian observation model for $(\kappa, \bar{v})$ given $v_t$, and explain why this decomposition reduces the variance of the Monte Carlo estimate compared to a full particle filter.

??? success "Solution to Exercise 7"
    **Conditional observation model for $(\kappa, \bar{v})$ given $v_t$.** In the Heston model, the CIR dynamics for variance are

    $$
    dv_t = \kappa(\bar{v} - v_t)\,dt + \sigma_v \sqrt{v_t}\,dW_t^v
    $$

    In discrete time, the conditional mean of the next variance observation (or an implied volatility that depends on variance) involves the term $\kappa(\bar{v} - v_t)\Delta t$. This expression is linear in $(\kappa, \bar{v})$ when $v_t$ is known.

    Specifically, suppose we observe quantities $y_t$ that, conditional on $v_t$ and other nonlinear parameters, depend linearly on $(\kappa, \bar{v})$. Define the parameter vector $\phi = (\kappa, \bar{v})^\top$. The conditional observation model takes the form

    $$
    y_t = G_t(v_t)\,\phi + g_t(v_t) + \varepsilon_t
    $$

    where $G_t(v_t)$ is a matrix whose entries depend on $v_t$ (known given the particle), and $g_t(v_t)$ captures the nonlinear dependence on $v_t$ and other fixed parameters. For instance, if the observation is the change in implied variance proxy, we might have

    $$
    \Delta v_t \approx \kappa \bar{v}\,\Delta t - \kappa v_t\,\Delta t + \sigma_v \sqrt{v_t}\,\Delta W_t
    $$

    This can be written as $\Delta v_t = \begin{pmatrix} (\bar{v} - v_t)\Delta t \end{pmatrix}\kappa + \varepsilon_t$, or in the two-parameter formulation

    $$
    \Delta v_t = \begin{pmatrix} -v_t \Delta t & \Delta t \end{pmatrix} \begin{pmatrix} \kappa \\ \kappa\bar{v} \end{pmatrix} + \sigma_v\sqrt{v_t}\,\Delta W_t
    $$

    After reparameterizing $\phi_1 = \kappa$ and $\phi_2 = \kappa\bar{v}$, this is exactly a linear-Gaussian model in $\phi$ conditional on $v_t$. A Kalman filter can track $\phi$ exactly within each particle.

    **Why Rao--Blackwellization reduces variance.** The key result is the **Rao--Blackwell theorem**: for any estimator $g(\theta)$, we have

    $$
    \text{Var}(g(\theta)) = \text{Var}(\mathbb{E}[g(\theta) \mid v_t]) + \mathbb{E}[\text{Var}(g(\theta) \mid v_t)]
    $$

    In a full particle filter, both $v_t$ and $(\kappa, \bar{v})$ are sampled with particles, contributing Monte Carlo variance in all dimensions. In the Rao--Blackwellized version, $(\kappa, \bar{v})$ is integrated out analytically (via the Kalman filter) conditional on each particle for $v_t$. This eliminates the Monte Carlo variance in the $(\kappa, \bar{v})$ dimensions entirely, leaving only the variance from the particle approximation of $v_t$.

    Formally, the Rao--Blackwellized estimate has variance equal to $\text{Var}(\mathbb{E}[g(\theta) \mid v_t])$, which is always less than or equal to $\text{Var}(g(\theta))$ by the law of total variance. The reduction is most significant when the conditional variance $\text{Var}(g(\theta) \mid v_t)$ is large, meaning that the analytically integrated components contribute substantially to overall uncertainty. In practice, this allows the Rao--Blackwellized particle filter to achieve the same accuracy as a full particle filter with far fewer particles.
