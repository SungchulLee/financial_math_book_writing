# Sequential Parameter Estimation

**Sequential parameter estimation** updates model parameters incrementally as new data arrives, rather than refitting models from scratch. This is essential for real-time financial applications.

---

## 1. Motivation

Financial markets evolve continuously:
- parameters change over time,
- data arrives sequentially,
- batch re-estimation is costly and unstable.

Sequential methods provide adaptability and computational efficiency.

---

## 2. Recursive estimation

A generic recursive update takes the form
\[
\theta_{t+1} = \theta_t + K_t (y_{t+1} - f(x_{t+1}; \theta_t)),
\]
where \(K_t\) is a gain or learning rate.

Examples include:
- recursive least squares,
- stochastic gradient descent,
- online EM algorithms.

---

## 3. Stability–adaptivity trade-off

- Large learning rates adapt quickly but are noisy.
- Small learning rates are stable but slow to adapt.

Choosing the update rule reflects a bias–variance trade-off over time.

---

## 4. Applications in finance

Sequential estimation is used for:
- online volatility estimation,
- adaptive calibration of pricing models,
- real-time risk metrics.

---

## 5. Key takeaways

- Sequential estimation updates parameters online.
- It balances stability and responsiveness.
- It is critical for real-time financial systems.

---

## Further reading

- Ljung, recursive identification.
- Bottou, stochastic gradient methods.
