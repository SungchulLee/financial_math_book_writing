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

??? success "Solution to Exercise 1"
    **(a)** A gradual drift from $\beta = 1.2$ to $\beta = 1.5$ over 6 months (~125 trading days) could be either:

    - **Model drift:** A smooth, monotonic increase driven by evolving market structure (e.g., increasing leverage, sector rotation). The estimated $\beta$ would show a steady upward trend with small fluctuations.
    - **Regime change:** An abrupt jump to a new $\beta$ level, with the RLS estimate gradually catching up due to the smoothing effect of the forgetting factor.

    Additional evidence to distinguish them:

    - Plot $\hat{\beta}_t$ over time: drift shows a smooth curve; a regime change shows a rapid transition.
    - Examine prediction errors $e_t$: drift produces small, persistent errors in one direction; a regime change produces a cluster of large errors around the break point.
    - Look at external indicators: a regime change often coincides with identifiable events (policy changes, crises), while drift is associated with gradual fundamental changes.
    - Apply a formal structural break test (Chow test, Bai-Perron test) to the residual series.

    **(b)** The effective window length is:

    $$
    T_{\text{eff}} = \frac{1}{1 - 0.98} = 50 \text{ observations}
    $$

    For an abrupt change in $\beta$ from $\beta_{\text{old}}$ to $\beta_{\text{new}}$ at time $t_0$, the RLS estimate at time $t_0 + k$ is approximately:

    $$
    \hat{\beta}_{t_0+k} \approx \beta_{\text{new}} - (\beta_{\text{new}} - \beta_{\text{old}})\lambda^k
    $$

    The estimate reflects 90% of the change when $\lambda^k \leq 0.10$:

    $$
    0.98^k \leq 0.10 \implies k \geq \frac{\ln(0.10)}{\ln(0.98)} = \frac{-2.3026}{-0.02020} \approx 114
    $$

    It takes about **114 observations** (approximately 4.5 months of daily data) for the RLS estimate to reflect 90% of an abrupt change. This is very slow, highlighting the limitation of exponential smoothing for detecting regime changes.

    **(c)** A CUSUM test on the prediction errors:

    Compute the cumulative sum of standardized prediction errors:

    $$
    S_t = \sum_{i=1}^t \frac{e_i}{\hat{\sigma}_e}
    $$

    where $\hat{\sigma}_e$ is an estimate of the standard deviation of $e_t$ under the null hypothesis of no change.

    - **Gradual drift:** The errors $e_t$ have a small, persistent bias. The CUSUM $S_t$ drifts slowly and steadily in one direction, crossing alarm boundaries late. The slope of $S_t$ is approximately constant and small.
    - **Abrupt change:** At the break point, prediction errors suddenly become large and one-sided. The CUSUM $S_t$ shows a sharp kink -- flat before the break, then steeply increasing (or decreasing). The change in slope is abrupt and large.

    The V-mask or page-CUSUM variant can formally distinguish these patterns: the test statistic $\max_{1 \leq k \leq t} |S_t - S_k - (t-k)\bar{e}|$ exceeds the threshold at or near the true break point for abrupt changes, while for gradual drift it remains below the threshold longer and triggers more diffusely.

---

**Exercise 2.** A Hamilton regime-switching model for returns has two states: $r_t \sim \mathcal{N}(\mu_1, \sigma_1^2)$ in regime 1 (bull market) and $r_t \sim \mathcal{N}(\mu_2, \sigma_2^2)$ in regime 2 (bear market), with transition matrix $P = \begin{pmatrix} p_{11} & 1-p_{11} \\ 1-p_{22} & p_{22} \end{pmatrix}$. (a) For $\mu_1 = 0.08/252$, $\sigma_1 = 0.15/\sqrt{252}$, $\mu_2 = -0.05/252$, $\sigma_2 = 0.30/\sqrt{252}$, $p_{11} = 0.98$, and $p_{22} = 0.95$, compute the expected duration of each regime. (b) Describe the Hamilton filter that computes $P(\text{regime}_t = k \mid r_1, \ldots, r_t)$ recursively. (c) Explain why regime-switching models capture abrupt structural changes that RLS with a forgetting factor handles poorly.

??? success "Solution to Exercise 2"
    **(a)** The expected duration of a regime is:

    $$
    D_k = \frac{1}{1 - p_{kk}}
    $$

    For regime 1 (bull market): $D_1 = 1/(1 - 0.98) = 50$ days $\approx 2$ months.

    For regime 2 (bear market): $D_2 = 1/(1 - 0.95) = 20$ days $\approx 1$ month.

    The unconditional (ergodic) probabilities are:

    $$
    \pi_1 = \frac{1 - p_{22}}{2 - p_{11} - p_{22}} = \frac{0.05}{0.07} \approx 0.714
    $$

    $$
    \pi_2 = \frac{1 - p_{11}}{2 - p_{11} - p_{22}} = \frac{0.02}{0.07} \approx 0.286
    $$

    The market spends about 71% of the time in the bull regime and 29% in the bear regime.

    **(b)** The Hamilton filter recursively computes:

    *Prediction step:* For each regime $k$, compute the predicted regime probability:

    $$
    P(s_t = k \mid r_{1:t-1}) = \sum_{j=1}^{2} p_{jk} \cdot P(s_{t-1} = j \mid r_{1:t-1})
    $$

    *Update step:* Incorporate the new observation $r_t$:

    $$
    P(s_t = k \mid r_{1:t}) = \frac{p(r_t \mid s_t = k) \cdot P(s_t = k \mid r_{1:t-1})}{\sum_{j=1}^2 p(r_t \mid s_t = j) \cdot P(s_t = j \mid r_{1:t-1})}
    $$

    where $p(r_t \mid s_t = k) = \mathcal{N}(r_t; \mu_k, \sigma_k^2)$ is the Gaussian density evaluated at $r_t$ under regime $k$'s parameters. The denominator is the marginal likelihood of $r_t$, which normalizes the probabilities.

    **(c)** RLS with a forgetting factor treats parameter changes as continuous and smooth. When an abrupt regime change occurs (e.g., from bull to bear), RLS slowly adjusts, blending the old and new regime parameters into a single estimate that is accurate for neither regime.

    The regime-switching model explicitly models discrete structural breaks:

    - It maintains separate parameter sets $(\mu_k, \sigma_k)$ for each regime, so parameters do not need to "drift" -- they switch instantaneously.
    - The filtered probabilities $P(s_t = k \mid r_{1:t})$ can shift rapidly from near 1 for one regime to near 1 for the other, even within a few observations, if the likelihood ratio is strong enough.
    - The model captures the bimodal nature of returns (different means and volatilities in different regimes), while RLS with a forgetting factor can only represent a single evolving parameter.

    The key advantage is that regime-switching models **anticipate** that parameters will revert to previously observed values when a regime recurs, while RLS treats every change as novel.

---

**Exercise 3.** An adaptive volatility model uses EWMA: $\hat{\sigma}_t^2 = \lambda \hat{\sigma}_{t-1}^2 + (1-\lambda) r_t^2$ with $\lambda = 0.94$ (RiskMetrics). During a calm period followed by a sudden crisis: (a) If the calm-period daily return standard deviation is 1% and then a single day has a 5% loss, compute $\hat{\sigma}_t$ on the crisis day and for each of the next 5 days (assuming returns revert to 1% moves). (b) The EWMA responds gradually to the crisis. Propose an adaptive $\lambda_t$ that decreases when large prediction errors are observed, enabling faster adaptation during regime changes. (c) Discuss the tradeoff: lower $\lambda$ during crises improves tracking but increases noise sensitivity. How would you design a regime-dependent $\lambda$?

??? success "Solution to Exercise 3"
    **(a)** Calm-period: $\hat{\sigma}_{t-1} = 1\% = 0.01$, so $\hat{\sigma}_{t-1}^2 = 0.0001$. With $\lambda = 0.94$:

    **Crisis day** ($r_t = -5\% = -0.05$):

    $$
    \hat{\sigma}_t^2 = 0.94 \times 0.0001 + 0.06 \times 0.0025 = 0.000094 + 0.000150 = 0.000244
    $$

    $$
    \hat{\sigma}_t = \sqrt{0.000244} = 1.562\%
    $$

    **Next 5 days** (returns revert to $\pm 1\%$ moves; take $r^2 = 0.0001$):

    Day $t+1$: $\hat{\sigma}^2 = 0.94 \times 0.000244 + 0.06 \times 0.0001 = 0.000229 + 0.000006 = 0.000235$, $\hat{\sigma} = 1.534\%$

    Day $t+2$: $\hat{\sigma}^2 = 0.94 \times 0.000235 + 0.06 \times 0.0001 = 0.000221 + 0.000006 = 0.000227$, $\hat{\sigma} = 1.507\%$

    Day $t+3$: $\hat{\sigma}^2 = 0.94 \times 0.000227 + 0.06 \times 0.0001 = 0.000213 + 0.000006 = 0.000220$, $\hat{\sigma} = 1.482\%$

    Day $t+4$: $\hat{\sigma}^2 = 0.94 \times 0.000220 + 0.06 \times 0.0001 = 0.000207 + 0.000006 = 0.000213$, $\hat{\sigma} = 1.458\%$

    Day $t+5$: $\hat{\sigma}^2 = 0.94 \times 0.000213 + 0.06 \times 0.0001 = 0.000200 + 0.000006 = 0.000206$, $\hat{\sigma} = 1.435\%$

    The volatility estimate jumps from 1% to 1.56% on the crisis day and then decays slowly back toward 1%, taking many days to return to normal.

    **(b)** An adaptive $\lambda_t$ that responds to large prediction errors:

    $$
    \lambda_t = \lambda_{\min} + (1 - \lambda_{\min}) \exp(-\gamma e_t^2)
    $$

    where $e_t = r_t^2 - \hat{\sigma}_{t-1}^2$ is the prediction error for the variance. With $\lambda_{\min} = 0.80$ and $\gamma$ calibrated so that a $5\sigma$ event (rare) triggers near-minimal $\lambda$:

    - Normal day ($e_t \approx 0$): $\lambda_t \approx 1$, standard long-memory smoothing.
    - Crisis day ($e_t^2$ large): $\lambda_t \to \lambda_{\min} = 0.80$, so $T_{\text{eff}} = 5$. The estimator "forgets" old data almost immediately and focuses on the crisis.

    This would produce a much sharper spike in $\hat{\sigma}_t$ on the crisis day (approximately $\hat{\sigma}_t^2 = 0.80 \times 0.0001 + 0.20 \times 0.0025 = 0.00058$, giving $\hat{\sigma}_t = 2.41\%$), responding more realistically to the extreme event.

    **(c)** The tradeoff with a regime-dependent $\lambda$:

    - During crises, lower $\lambda$ (shorter memory) enables rapid tracking of elevated volatility, but each observation has outsized influence, making the estimate noisy. If a single calm day occurs during a crisis, the estimate might drop prematurely.
    - A practical design: use a regime indicator (e.g., based on the VIX level, recent realized volatility, or a Hamilton filter probability) to set $\lambda$. For instance: $\lambda = 0.97$ when $P(\text{calm}) > 0.8$ and $\lambda = 0.90$ when $P(\text{crisis}) > 0.5$. The regime probabilities smooth the transition between $\lambda$ values, preventing abrupt switching that could itself introduce instability.

---

**Exercise 4.** A model ensemble approach maintains three models calibrated on different lookback windows: 1 month, 6 months, and 2 years. Each model produces a VaR forecast. (a) During stable periods, which window produces the most accurate VaR? During regime transitions? (b) Propose a weighting scheme that combines the three forecasts using recent predictive performance (e.g., Bayesian model averaging with likelihood weights). (c) Alternatively, propose a "model reset" trigger: when the 1-month model diverges significantly from the 2-year model, flag a potential regime change and increase the weight on the short-window model. What statistical test would you use for the divergence threshold?

??? success "Solution to Exercise 4"
    **(a)** During **stable periods**, the 2-year lookback window produces the most accurate VaR because:

    - The larger sample reduces estimation error (lower variance of parameter estimates).
    - In a stationary environment, more data is always better for estimating tail quantiles.
    - The 1-month window has too few observations (about 22 trading days) for reliable tail estimation.

    During **regime transitions**, the 1-month window is most accurate because:

    - It quickly reflects the new distributional properties (higher volatility, fatter tails).
    - The 2-year window dilutes the crisis data with stale calm-period data, systematically underestimating VaR.
    - The 6-month window is a compromise but still lags during rapid transitions.

    **(b)** Bayesian model averaging with predictive likelihood weights:

    Let $M_j$ ($j \in \{1\text{-month}, 6\text{-month}, 2\text{-year}\}$) denote each model. At each time $t$, compute the predictive likelihood of the new observation under each model:

    $$
    L_t^{(j)} = p(r_t \mid r_{1:t-1}, M_j)
    $$

    Update the model weights using Bayes' rule:

    $$
    w_t^{(j)} = \frac{w_{t-1}^{(j)} L_t^{(j)}}{\sum_k w_{t-1}^{(k)} L_t^{(k)}}
    $$

    The combined VaR forecast:

    $$
    \text{VaR}_t = \sum_j w_t^{(j)} \text{VaR}_t^{(j)}
    $$

    During calm periods, the 2-year model will have the highest predictive likelihood (best density forecasts) and receive the most weight. During crises, the 1-month model will outperform and gain weight. This automatic reweighting provides a smooth adaptation mechanism.

    **(c)** A model-reset trigger based on divergence between short and long windows:

    Define the divergence statistic as the absolute difference in VaR forecasts, normalized by the long-window forecast:

    $$
    D_t = \frac{|\text{VaR}_t^{1\text{m}} - \text{VaR}_t^{2\text{y}}|}{|\text{VaR}_t^{2\text{y}}|}
    $$

    When $D_t > d^*$ (threshold), flag a potential regime change and shift weight to the short-window model.

    An appropriate statistical test: the **Kolmogorov-Smirnov (KS) test** comparing the empirical return distribution from the last month with the distribution from the last 2 years. The KS statistic $D_n = \sup_x |F_{1m}(x) - F_{2y}(x)|$ tests whether the two samples come from the same distribution. A rejection at significance level $\alpha$ triggers the regime-change flag.

    Alternatively, a **likelihood ratio test** comparing the log-likelihood of recent observations under the 1-month versus 2-year model: $\Lambda_t = 2\sum_{i=t-21}^t [\log L_i^{1m} - \log L_i^{2y}]$. Under the null (same regime), $\Lambda_t \sim \chi^2_k$ approximately, and large values trigger the alarm.

---

**Exercise 5.** Distinguish between the following types of non-stationarity in financial data: (a) slow parameter drift (e.g., gradually increasing correlations), (b) abrupt regime change (e.g., onset of a financial crisis), (c) structural break (e.g., a regulatory change that permanently alters market dynamics). For each type, describe the most appropriate estimation approach: forgetting factor RLS, regime-switching model, or batch re-estimation with a change-point detection algorithm. Provide a concrete financial example of each.

??? success "Solution to Exercise 5"
    **(a) Slow parameter drift** (e.g., gradually increasing correlations):

    - **Example:** Over 2018-2023, the correlation between US and European equity markets increases from 0.6 to 0.8 as globalization deepens and algorithmic trading creates tighter linkages.
    - **Best approach: Forgetting factor RLS.** The exponentially weighted scheme with $\lambda \approx 0.98$-$0.99$ smoothly tracks the evolving correlation without overreacting to daily noise. The effective window of 50-100 days captures the trend while averaging out short-term fluctuations.

    **(b) Abrupt regime change** (e.g., onset of a financial crisis):

    - **Example:** In March 2020, the COVID-19 pandemic caused a sudden shift: volatilities tripled, correlations spiked to near 1, and mean returns turned sharply negative -- all within a few days.
    - **Best approach: Regime-switching model.** A Hamilton-type model with "normal" and "crisis" regimes can detect the switch within 2-3 observations (if the likelihood ratio is strong) and immediately apply the crisis-regime parameters. Unlike RLS, it does not need to "forget" old data gradually -- it switches to a pre-estimated crisis parameter set.

    **(c) Structural break** (e.g., a regulatory change that permanently alters market dynamics):

    - **Example:** The implementation of MiFID II in January 2018 permanently changed European equity market microstructure: bid-ask spreads, trading volumes, and dark pool activity shifted to new levels that did not revert.
    - **Best approach: Batch re-estimation with change-point detection.** First, apply a formal change-point test (Bai-Perron, CUSUM, or binary segmentation) to identify the break date. Then re-estimate the model using only post-break data. Unlike regime-switching models (which assume regimes can recur), a structural break implies the old regime will never return, so old data is permanently discarded.

    | Non-stationarity type | Temporal pattern | Best estimation method | Key property |
    |---|---|---|---|
    | Slow drift | Continuous, smooth | Forgetting factor RLS | Tracks gradual changes |
    | Abrupt regime change | Discrete, recurring | Regime-switching model | Fast detection, reversion possible |
    | Structural break | One-time permanent shift | Change-point detection + re-estimation | Old data permanently irrelevant |

---

**Exercise 6.** A risk manager must decide whether to retrain a credit risk model after observing elevated default rates. The model was trained on 2015-2019 data; it is now 2023 and default rates have risen from 2% to 4%. (a) Is this model drift (gradual macroeconomic change) or a regime shift (structural change in credit markets)? What data would help distinguish them? (b) If the model is retrained on 2020-2023 data only, what risks arise from the short training window? If retrained on 2015-2023, the model may underweight recent dynamics. Propose a compromise. (c) Discuss regulatory considerations: under Basel guidelines, how frequently should credit risk models be recalibrated, and what validation tests (e.g., backtesting, benchmarking) are required?

??? success "Solution to Exercise 6"
    **(a)** Distinguishing model drift from regime shift:

    The increase from 2% to 4% default rate could be:

    - **Model drift:** Gradual macroeconomic deterioration (rising interest rates, inflation, supply chain disruptions) steadily increases default probabilities. The increase would appear smooth over 2020-2023 with no single break point.
    - **Regime shift:** A structural change in credit markets (e.g., pandemic-related government support ending, creating a "cliff" in defaults) or a change in the composition of borrowers (post-pandemic lending standards).

    Data to help distinguish:

    - Time series of monthly default rates: smooth upward trend (drift) vs. step function (regime shift).
    - Macroeconomic covariates: if default rates track GDP growth, unemployment, and interest rates smoothly, it is drift.
    - Sector analysis: if defaults concentrate in specific sectors affected by a structural change (e.g., commercial real estate post-COVID), it is more likely a regime shift.
    - Rating migration matrices: gradual widening of downgrade rates suggests drift; sudden spikes suggest a regime.

    **(b)** Compromise for retraining:

    - **Training on 2020-2023 only (4 years):** Risks include insufficient data for rare events, overfitting to the pandemic-recovery cycle, and poor out-of-sample performance in a different macro environment.
    - **Training on 2015-2023 (9 years):** Risks include underweighting recent dynamics, as the 2015-2019 period may no longer be representative.

    **Proposed compromise:** Use a weighted estimation that downweights older data:

    $$
    \hat{\theta} = \arg\max_\theta \sum_{t=2015}^{2023} w_t \cdot \ell_t(\theta)
    $$

    where $w_t$ increases with recency (e.g., $w_t = \lambda^{2023-t}$ with $\lambda = 0.85$, giving 2015 data about 27% of the weight of 2023 data). This preserves statistical power from the full sample while emphasizing recent dynamics.

    Alternatively, use a two-stage approach: estimate structural parameters (e.g., sensitivity of default to macro factors) on the full sample, and estimate the current macro state and level parameters on recent data.

    **(c)** Regulatory considerations under Basel:

    - **Recalibration frequency:** Basel III/IV requires that internal ratings-based (IRB) models be reviewed at least annually and recalibrated whenever there is evidence of material deterioration in predictive power (Basel Committee, BCBS 239).
    - **Backtesting:** Compare predicted default rates with realized defaults over multiple time horizons (1-year, 3-year). A systematic underprediction (actual defaults exceeding predicted) triggers mandatory recalibration.
    - **Benchmarking:** Compare the internal model's outputs against external benchmarks (rating agency default studies, regulatory benchmarks) to identify model-specific biases.
    - **Validation tests:** Discriminatory power tests (Gini coefficient, ROC/AUC), calibration tests (Hosmer-Lemeshow, binomial test for PD accuracy), and stability tests (population stability index comparing recent vs. development sample characteristics).
    - **Conservatism:** Regulators may require a margin of conservatism to be added when model performance deteriorates or data is limited, and models must be recalibrated within a regulatory timeline (typically 90 days of identifying material issues).

---

**Exercise 7.** Consider an online Bayesian approach that maintains a posterior distribution over both the model parameters and the regime: $p(\theta, s_t \mid y_{1:t})$ where $s_t \in \{1, \ldots, K\}$ is the regime indicator. (a) Write the prediction step that marginalizes over the previous regime and transitions according to the Markov chain. (b) Write the update step using Bayes' theorem with the likelihood $p(y_t \mid \theta, s_t)$. (c) Explain why this joint inference automatically adapts to regime changes: when a regime switch occurs, the posterior shifts to a different parameter region. (d) Discuss computational challenges: for continuous $\theta$ and $K$ regimes, the posterior is a mixture of $K^t$ Gaussians after $t$ steps. How do particle filters address this exponential growth?

??? success "Solution to Exercise 7"
    **(a) Prediction step:**

    The joint predictive distribution over the regime and parameters at time $t$, given observations up to $t-1$:

    $$
    p(\theta, s_t = k \mid y_{1:t-1}) = \sum_{j=1}^K p(s_t = k \mid s_{t-1} = j)\, p(\theta, s_{t-1} = j \mid y_{1:t-1})
    $$

    where $p(s_t = k \mid s_{t-1} = j) = P_{jk}$ is the $(j,k)$ entry of the transition matrix. If the parameters also evolve (e.g., $\theta_t = \theta_{t-1} + w_t$), the prediction additionally convolves with the parameter transition kernel:

    $$
    p(\theta, s_t = k \mid y_{1:t-1}) = \sum_{j=1}^K P_{jk} \int p(\theta \mid \theta')\, p(\theta', s_{t-1} = j \mid y_{1:t-1})\, d\theta'
    $$

    For static $\theta$ (parameters that differ across regimes but do not evolve within a regime), the integral simplifies.

    **(b) Update step:**

    Using Bayes' theorem:

    $$
    p(\theta, s_t = k \mid y_{1:t}) = \frac{p(y_t \mid \theta, s_t = k)\, p(\theta, s_t = k \mid y_{1:t-1})}{p(y_t \mid y_{1:t-1})}
    $$

    where the marginal likelihood is:

    $$
    p(y_t \mid y_{1:t-1}) = \sum_{k=1}^K \int p(y_t \mid \theta, s_t = k)\, p(\theta, s_t = k \mid y_{1:t-1})\, d\theta
    $$

    The likelihood $p(y_t \mid \theta, s_t = k)$ evaluates the probability of the observation under the model with parameters $\theta$ in regime $k$.

    **(c)** This joint inference adapts automatically to regime changes because:

    - Before a regime switch, the posterior concentrates on, say, $s_t = 1$ with parameters $\theta$ near $\theta_1^*$ (the optimal parameters for regime 1).
    - When a regime switch occurs, observations become inconsistent with $(s_t = 1, \theta_1^*)$: the likelihood $p(y_t \mid \theta_1^*, s_t = 1)$ becomes small.
    - The posterior rapidly shifts weight toward $s_t = 2$, and the marginal $p(\theta \mid s_t = 2, y_{1:t})$ concentrates on $\theta_2^*$ (regime 2 parameters).
    - Crucially, if the model has previously been in regime 2, the posterior for $\theta$ given $s_t = 2$ already "remembers" the regime-2 parameters from past data. There is no need to re-estimate from scratch.

    This is fundamentally different from RLS, which must slowly drift from $\theta_1^*$ toward $\theta_2^*$. The regime-switching Bayesian approach can switch instantaneously because it maintains separate parameter posteriors for each regime.

    **(d) Computational challenges:**

    At time $t$, the posterior $p(\theta, s_{1:t} \mid y_{1:t})$ involves a sum over all possible regime sequences $s_{1:t} \in \{1, \ldots, K\}^t$. Even after integrating out the path $s_{1:t-1}$, the posterior $p(\theta, s_t \mid y_{1:t})$ is a mixture of distributions: each possible sequence of past regimes contributes a different posterior component for $\theta$. After $t$ steps with $K$ regimes:

    - The exact posterior is a mixture of $K^t$ Gaussian components (for conjugate models).
    - For $K = 2$ and $t = 100$: $2^{100} \approx 10^{30}$ components -- clearly intractable.

    **Particle filters address this** by representing the joint posterior with a finite set of $N$ weighted particles $\{(\theta^{(i)}, s_t^{(i)}, w_t^{(i)})\}_{i=1}^N$. Each particle carries a parameter value and a regime assignment. The algorithm:

    1. **Propagate:** For each particle, sample $s_t^{(i)} \sim P(s_t \mid s_{t-1}^{(i)})$ from the transition matrix, and optionally perturb $\theta^{(i)}$ if parameters evolve.
    2. **Weight:** $w_t^{(i)} \propto p(y_t \mid \theta^{(i)}, s_t^{(i)})$.
    3. **Resample** when $N_{\text{eff}}$ is low.

    This avoids the exponential growth because the particle approximation implicitly prunes unlikely regime histories through resampling. The cost is $O(N)$ per time step, independent of $t$. The accuracy is controlled by $N$: with $N = 10{,}000$ particles, the filter can track complex multi-regime dynamics with time-varying parameters, maintaining a tractable representation of the posterior at all times.
