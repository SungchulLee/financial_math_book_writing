# Filtering and Bayesian Updating


**Filtering** and **Bayesian updating** provide principled frameworks for sequential inference when model parameters or states are latent.

---

## State-space models


Consider a state-space model:

\[
x_{t+1} = g(x_t) + \varepsilon_t, \quad
y_t = h(x_t) + \eta_t.
\]



The latent state \(x_t\) evolves over time and must be inferred from observations.

---

## Bayesian updating


Bayesian inference updates beliefs via

\[
p(x_t \mid y_{1:t}) \propto p(y_t \mid x_t) p(x_t \mid y_{1:t-1}).
\]



This recursion underlies all filtering methods.

---

## Filtering techniques


Common filters include:
- Kalman filter (linear-Gaussian),
- Extended and Unscented Kalman filters,
- Particle filters for nonlinear/non-Gaussian models.

Choice depends on model complexity and accuracy needs.

---

## Financial applications


Filtering is widely used for:
- stochastic volatility estimation,
- latent factor models,
- regime-switching detection.

---

## Key takeaways


- Filtering performs sequential Bayesian inference.
- It handles latent states and noisy observations.
- Particle methods trade accuracy for computation.

---

## Further reading


- Kalman, linear filtering.
- Doucet et al., particle filtering.

---

## Exercises

**Exercise 1.** For a linear-Gaussian state-space model $x_{t+1} = 0.95 x_t + \varepsilon_t$ with $\varepsilon_t \sim N(0, 0.01)$ and $y_t = x_t + \eta_t$ with $\eta_t \sim N(0, 0.04)$, write down the Kalman filter prediction and update equations. Starting from $\hat{x}_0 = 0$ and $P_0 = 1$, compute the first two Kalman filter updates given observations $y_1 = 0.5$ and $y_2 = 0.3$.

---

**Exercise 2.** Derive the Bayesian updating rule $p(x_t | y_{1:t}) \propto p(y_t | x_t) \, p(x_t | y_{1:t-1})$ from Bayes' theorem. Explain why the prediction step $p(x_t | y_{1:t-1}) = \int p(x_t | x_{t-1}) p(x_{t-1} | y_{1:t-1}) \, dx_{t-1}$ is computationally expensive for nonlinear models and how particle filters address this through Monte Carlo approximation.

---

**Exercise 3.** The stochastic volatility model $\log \sigma_t^2 = \phi \log \sigma_{t-1}^2 + \eta_t$ with $r_t = \sigma_t \varepsilon_t$ is a nonlinear state-space model. Explain why the Kalman filter cannot be applied directly and describe how a particle filter with $N = 1000$ particles would estimate the latent volatility path. What is the resampling step and why is it necessary?

---

**Exercise 4.** Compare the Extended Kalman Filter (EKF) and the Unscented Kalman Filter (UKF) for a nonlinear observation equation $y_t = x_t^2 + \eta_t$. The EKF linearizes via $h'(x_t) = 2x_t$, while the UKF uses sigma points. For $\hat{x}_t = 3$ and $P_t = 0.5$, compute the EKF and UKF predicted observation means and variances. Which is more accurate?

---

**Exercise 5.** In a regime-switching model, the latent state $s_t \in \{1, 2\}$ follows a Markov chain. The Bayesian filter computes $P(s_t = i | y_{1:t})$ recursively. For transition matrix $P = \begin{pmatrix} 0.95 & 0.05 \\ 0.10 & 0.90 \end{pmatrix}$ and observation densities $p(y_t | s_t = 1) = N(0.05, 0.01)$ and $p(y_t | s_t = 2) = N(-0.10, 0.04)$, compute the filtered probability of being in regime 1 after observing $y_1 = -0.08$, starting from equal prior probabilities.

---

**Exercise 6.** Describe how a Kalman filter can be used to estimate time-varying hedge ratios. If the hedge ratio $\beta_t$ follows a random walk $\beta_{t+1} = \beta_t + w_t$ and the observation is $r_t^Y = \beta_t r_t^X + \varepsilon_t$, set up the state-space model and derive the Kalman filter equations for $\hat{\beta}_t$. How does the Kalman gain adapt as the signal-to-noise ratio changes?
