# Model Drift vs Market Regimes


Adaptive calibration must distinguish between **model drift** and genuine **market regime changes**, a key challenge in online learning.

---

## Model drift


Model drift refers to:
- gradual parameter changes,
- slow evolution of market dynamics,
- continuous adaptation being appropriate.

Sequential estimators handle drift naturally.

---

## Market regimes


Market regimes involve:
- abrupt structural changes,
- shifts in volatility, correlations, or liquidity,
- breakdown of historical relationships.

Regimes require discrete model adjustments.

---

## Detection challenges


Distinguishing drift from regime change is difficult because:
- both affect parameter estimates,
- noise obscures signals,
- delayed detection is common.

Statistical tests and filters provide partial solutions.

---

## Practical approaches


Common approaches include:
- regime-switching models,
- forgetting factors and adaptive gains,
- model ensembles and resets.

Human oversight remains essential.

---

## Key takeaways


- Drift and regimes require different responses.
- Online learning must balance adaptation and stability.
- Governance complements automation.

---

## Further reading


- Hamilton, regime-switching models.
- Cont, model instability in finance.

---

## Exercises

**Exercise 1.** A linear factor model $r_t = \alpha + \beta f_t + \varepsilon_t$ is estimated with an exponentially weighted RLS using forgetting factor $\lambda = 0.98$. The estimated beta drifts from 1.2 to 1.5 over 6 months. (a) Is this consistent with model drift or a regime change? What additional evidence would help distinguish them? (b) Compute the effective window length $T_{\text{eff}} = 1/(1-\lambda)$. If the true beta changed abruptly at a single point, how many observations would it take for the RLS estimate to reflect 90% of the change? (c) Propose a CUSUM test on the prediction errors $e_t = r_t - \hat{\alpha}_t - \hat{\beta}_t f_t$ to detect whether the change is abrupt or gradual.

---

**Exercise 2.** A Hamilton regime-switching model for returns has two states: $r_t \sim \mathcal{N}(\mu_1, \sigma_1^2)$ in regime 1 (bull market) and $r_t \sim \mathcal{N}(\mu_2, \sigma_2^2)$ in regime 2 (bear market), with transition matrix $P = \begin{pmatrix} p_{11} & 1-p_{11} \\ 1-p_{22} & p_{22} \end{pmatrix}$. (a) For $\mu_1 = 0.08/252$, $\sigma_1 = 0.15/\sqrt{252}$, $\mu_2 = -0.05/252$, $\sigma_2 = 0.30/\sqrt{252}$, $p_{11} = 0.98$, and $p_{22} = 0.95$, compute the expected duration of each regime. (b) Describe the Hamilton filter that computes $P(\text{regime}_t = k \mid r_1, \ldots, r_t)$ recursively. (c) Explain why regime-switching models capture abrupt structural changes that RLS with a forgetting factor handles poorly.

---

**Exercise 3.** An adaptive volatility model uses EWMA: $\hat{\sigma}_t^2 = \lambda \hat{\sigma}_{t-1}^2 + (1-\lambda) r_t^2$ with $\lambda = 0.94$ (RiskMetrics). During a calm period followed by a sudden crisis: (a) If the calm-period daily return standard deviation is 1% and then a single day has a 5% loss, compute $\hat{\sigma}_t$ on the crisis day and for each of the next 5 days (assuming returns revert to 1% moves). (b) The EWMA responds gradually to the crisis. Propose an adaptive $\lambda_t$ that decreases when large prediction errors are observed, enabling faster adaptation during regime changes. (c) Discuss the tradeoff: lower $\lambda$ during crises improves tracking but increases noise sensitivity. How would you design a regime-dependent $\lambda$?

---

**Exercise 4.** A model ensemble approach maintains three models calibrated on different lookback windows: 1 month, 6 months, and 2 years. Each model produces a VaR forecast. (a) During stable periods, which window produces the most accurate VaR? During regime transitions? (b) Propose a weighting scheme that combines the three forecasts using recent predictive performance (e.g., Bayesian model averaging with likelihood weights). (c) Alternatively, propose a "model reset" trigger: when the 1-month model diverges significantly from the 2-year model, flag a potential regime change and increase the weight on the short-window model. What statistical test would you use for the divergence threshold?

---

**Exercise 5.** Distinguish between the following types of non-stationarity in financial data: (a) slow parameter drift (e.g., gradually increasing correlations), (b) abrupt regime change (e.g., onset of a financial crisis), (c) structural break (e.g., a regulatory change that permanently alters market dynamics). For each type, describe the most appropriate estimation approach: forgetting factor RLS, regime-switching model, or batch re-estimation with a change-point detection algorithm. Provide a concrete financial example of each.

---

**Exercise 6.** A risk manager must decide whether to retrain a credit risk model after observing elevated default rates. The model was trained on 2015-2019 data; it is now 2023 and default rates have risen from 2% to 4%. (a) Is this model drift (gradual macroeconomic change) or a regime shift (structural change in credit markets)? What data would help distinguish them? (b) If the model is retrained on 2020-2023 data only, what risks arise from the short training window? If retrained on 2015-2023, the model may underweight recent dynamics. Propose a compromise. (c) Discuss regulatory considerations: under Basel guidelines, how frequently should credit risk models be recalibrated, and what validation tests (e.g., backtesting, benchmarking) are required?

---

**Exercise 7.** Consider an online Bayesian approach that maintains a posterior distribution over both the model parameters and the regime: $p(\theta, s_t \mid y_{1:t})$ where $s_t \in \{1, \ldots, K\}$ is the regime indicator. (a) Write the prediction step that marginalizes over the previous regime and transitions according to the Markov chain. (b) Write the update step using Bayes' theorem with the likelihood $p(y_t \mid \theta, s_t)$. (c) Explain why this joint inference automatically adapts to regime changes: when a regime switch occurs, the posterior shifts to a different parameter region. (d) Discuss computational challenges: for continuous $\theta$ and $K$ regimes, the posterior is a mixture of $K^t$ Gaussians after $t$ steps. How do particle filters address this exponential growth?
