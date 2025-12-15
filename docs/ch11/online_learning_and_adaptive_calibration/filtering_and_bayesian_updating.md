# Filtering and Bayesian Updating

**Filtering** and **Bayesian updating** provide principled frameworks for sequential inference when model parameters or states are latent.

---

## 1. State-space models

Consider a state-space model:
\[
x_{t+1} = g(x_t) + \varepsilon_t, \quad
y_t = h(x_t) + \eta_t.
\]

The latent state \(x_t\) evolves over time and must be inferred from observations.

---

## 2. Bayesian updating

Bayesian inference updates beliefs via
\[
p(x_t \mid y_{1:t}) \propto p(y_t \mid x_t) p(x_t \mid y_{1:t-1}).
\]

This recursion underlies all filtering methods.

---

## 3. Filtering techniques

Common filters include:
- Kalman filter (linear-Gaussian),
- Extended and Unscented Kalman filters,
- Particle filters for nonlinear/non-Gaussian models.

Choice depends on model complexity and accuracy needs.

---

## 4. Financial applications

Filtering is widely used for:
- stochastic volatility estimation,
- latent factor models,
- regime-switching detection.

---

## 5. Key takeaways

- Filtering performs sequential Bayesian inference.
- It handles latent states and noisy observations.
- Particle methods trade accuracy for computation.

---

## Further reading

- Kalman, linear filtering.
- Doucet et al., particle filtering.
