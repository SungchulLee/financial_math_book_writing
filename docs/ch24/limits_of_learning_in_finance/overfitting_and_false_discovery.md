# Overfitting and False Discovery


**Overfitting** and **false discovery** are pervasive risks in financial learning due to noisy data and multiple testing.

---

## Overfitting in finance


Overfitting occurs when a model:

- fits noise rather than signal,
- performs well in-sample,
- fails out-of-sample.

Limited data and heavy noise exacerbate the problem.

---

## Multiple testing and data snooping


Financial research often involves testing many strategies, selecting the best, and ignoring failed experiments — leading to false discoveries.

Recall (see [§ Multiple Testing Correction](multiple_testing_correction.md)) for the formal FWER/FDR machinery (Bonferroni, Holm, Benjamini-Hochberg) and Harvey-Liu-Zhu / deflated Sharpe / haircut adjustments.

---

## Consequences


False discoveries produce spurious strategies, inflated backtests, and real-world losses when deployed.

---

## Mitigation techniques


Common defenses: out-of-sample validation, time-series cross-validation, multiple-testing correction (see [§ Multiple Testing Correction](multiple_testing_correction.md)), and economic plausibility checks.

---

## Key takeaways


- Overfitting is endemic in finance.
- Multiple testing inflates false positives.
- Rigorous validation is essential.

---

## Further reading


- Bailey et al., backtest overfitting.
- Harvey, Liu & Zhu, false discoveries.

---

## Exercises

**Exercise 1.** A researcher tests 100 independent trading strategies on the same dataset and selects the one with the highest Sharpe ratio. If each strategy is truly unprofitable (null hypothesis true for all), what is the probability that at least one strategy appears significant at the 5% level? Compute $1 - (0.95)^{100}$ and explain why this probability is so high.

??? success "Solution to Exercise 1"
    **Probability of at least one false significant result.**

    Under the null hypothesis, each strategy is truly unprofitable. Testing at the 5% level means each test has a 5% probability of a false positive (type I error). With 100 independent tests, the probability that *all* tests correctly fail to reject is:

    $$
    \Pr(\text{no false positive}) = (1 - 0.05)^{100} = 0.95^{100}
    $$

    Computing $0.95^{100}$:

    $$
    0.95^{100} = e^{100 \ln(0.95)} = e^{100 \times (-0.05129)} = e^{-5.129} \approx 0.00592
    $$

    Therefore, the probability of **at least one** false positive is:

    $$
    \Pr(V \geq 1) = 1 - 0.95^{100} \approx 1 - 0.00592 = 0.994
    $$

    This is approximately **99.4%**. It is virtually certain that at least one strategy will appear "significant" by pure chance.

    **Why so high?** Each test has only a 5% false positive rate, but with 100 independent chances, the cumulative probability of at least one error accumulates rapidly. The expected number of false positives is $100 \times 0.05 = 5$. The researcher who selects the "best" strategy is almost certainly selecting a false discovery. This is the essence of the multiple testing problem: individual test validity does not ensure family-wise validity.

---

**Exercise 2.** Describe the difference between in-sample and out-of-sample validation for a trading strategy. A strategy achieves an annualized Sharpe ratio of 2.5 in-sample but 0.3 out-of-sample. Estimate the degree of overfitting using the deflated Sharpe ratio framework and explain what factors contribute to the gap.

??? success "Solution to Exercise 2"
    **In-sample vs. out-of-sample validation and the deflated Sharpe ratio.**

    **In-sample vs. out-of-sample:** In-sample validation evaluates a strategy on the same data used to develop and optimize it. The strategy is free to fit noise, idiosyncratic patterns, and spurious correlations in the training data. Out-of-sample validation evaluates on data that was not used during development, providing an unbiased estimate of future performance.

    **The gap:** An in-sample Sharpe of 2.5 versus an out-of-sample Sharpe of 0.3 represents a dramatic degradation. The **overfitting ratio** can be defined as:

    $$
    \text{Overfitting Ratio} = 1 - \frac{\text{SR}_{\text{OOS}}}{\text{SR}_{\text{IS}}} = 1 - \frac{0.3}{2.5} = 0.88
    $$

    This means 88% of the in-sample performance was due to overfitting.

    **Deflated Sharpe ratio framework.** The deflated Sharpe ratio (Bailey and Lopez de Prado, 2014) tests whether the observed Sharpe ratio exceeds what would be expected by chance given the number of trials. The null hypothesis is that the true Sharpe ratio is zero, and the "best-of-$N$" selection inflates the observed SR. The expected maximum Sharpe under the null for $N$ independent strategies is approximately:

    $$
    \text{SR}_0 \approx \sqrt{2 \log N} \cdot \frac{1}{\sqrt{T}}
    $$

    The DSR is the probability that the observed SR exceeds $\text{SR}_0$, adjusted for skewness ($\hat{\gamma}_3$) and kurtosis ($\hat{\gamma}_4$):

    $$
    \text{DSR} = \Phi\!\left(\frac{(\widehat{\text{SR}} - \text{SR}_0)\sqrt{T-1}}{\sqrt{1 - \hat{\gamma}_3 \cdot \widehat{\text{SR}} + \frac{\hat{\gamma}_4 - 1}{4}\widehat{\text{SR}}^2}}\right)
    $$

    **Contributing factors to the gap:**

    1. **Parameter optimization on in-sample data** allows the model to exploit noise.
    2. **Feature selection** (choosing the "best" predictors from many candidates) introduces selection bias.
    3. **Non-stationarity** means patterns in the training period may not persist.
    4. **Overfitting to specific regimes** (e.g., a bull market) that do not recur.
    5. **Transaction costs and market impact** are often underestimated in backtests.

---

**Exercise 3.** The Bonferroni correction adjusts the significance level from $\alpha$ to $\alpha / m$ when $m$ tests are conducted. For $m = 200$ strategy backtests and $\alpha = 0.05$, compute the adjusted threshold. Explain why the Bonferroni correction is conservative and describe the Benjamini-Hochberg procedure as a less conservative alternative that controls the false discovery rate.

??? success "Solution to Exercise 3"
    **Bonferroni correction and the Benjamini-Hochberg alternative.**

    **Bonferroni correction.** With $m = 200$ tests and significance level $\alpha = 0.05$, the adjusted threshold is:

    $$
    \frac{\alpha}{m} = \frac{0.05}{200} = 0.00025
    $$

    Each individual test must achieve $p \leq 0.00025$ to be declared significant. In terms of $t$-statistics (for a two-sided test with large degrees of freedom):

    $$
    t_{\text{threshold}} = \Phi^{-1}\!\left(1 - \frac{0.00025}{2}\right) = \Phi^{-1}(0.999875) \approx 3.66
    $$

    **Why Bonferroni is conservative.** The Bonferroni correction uses the union bound:

    $$
    \Pr\!\left(\bigcup_{i=1}^{m_0}\{p_i \leq \alpha/m\}\right) \leq \sum_{i=1}^{m_0} \Pr(p_i \leq \alpha/m)
    $$

    The union bound is tight only when events are mutually exclusive. In practice, strategy backtests are positively correlated (they use the same market data), so the joint probability of multiple false positives is lower than the sum of individual probabilities. Bonferroni overestimates the FWER, leading to unnecessarily stringent thresholds and reduced power (failure to detect genuinely profitable strategies).

    **Benjamini-Hochberg (BH) procedure.** Instead of controlling the family-wise error rate (probability of any false positive), BH controls the **false discovery rate** (expected proportion of false positives among rejections):

    $$
    \text{FDR} = \mathbb{E}\!\left[\frac{V}{R \vee 1}\right]
    $$

    **Steps:**

    1. Order p-values: $p_{(1)} \leq p_{(2)} \leq \cdots \leq p_{(m)}$
    2. Find $k^* = \max\!\left\{i : p_{(i)} \leq \frac{i}{m}\alpha\right\}$
    3. Reject $H_{(1)}, \ldots, H_{(k^*)}$

    The BH line is $i\alpha/m = i \cdot 0.05/200 = i \cdot 0.00025$. Each hypothesis $i$ gets its own threshold that increases linearly:

    | $i$ | BH threshold $i\alpha/m$ |
    |-----|--------------------------|
    | 1   | 0.00025                  |
    | 2   | 0.00050                  |
    | 3   | 0.00075                  |
    | 10  | 0.00250                  |
    | 50  | 0.01250                  |

    The BH procedure is less conservative because it allows a controlled fraction of false positives rather than demanding zero false positives. For large $m$, BH rejects substantially more hypotheses than Bonferroni while maintaining the FDR at $\alpha$.

---

**Exercise 4.** Cross-validation for time series data must respect temporal ordering (no future information leakage). Describe a walk-forward validation scheme for evaluating a trading strategy: define the training window, the gap period, and the test period. Why is a gap period between training and testing important in financial applications?

??? success "Solution to Exercise 4"
    **Walk-forward validation for trading strategies.**

    **Walk-forward scheme design:**

    The data is divided into sequential, non-overlapping blocks that respect temporal ordering:

    1. **Training window** (e.g., 3 years = 756 trading days): The model is estimated or optimized on this period. All parameter choices, feature selection, and hyperparameter tuning occur within this window.

    2. **Gap period** (e.g., 1 month = 21 trading days): A buffer between training and testing that is neither used for training nor evaluation. This period is deliberately excluded.

    3. **Test period** (e.g., 6 months = 126 trading days): The model, with parameters frozen from the training window, is evaluated on this data. Performance metrics (Sharpe ratio, returns, drawdown) are recorded.

    The procedure then "walks forward": the windows shift by the length of the test period, and the process repeats. Each iteration produces one out-of-sample evaluation. The final performance estimate is the aggregate across all test periods.

    **Why the gap period is important:**

    - **Autocorrelation and look-ahead.** Financial features often exhibit serial correlation over days or weeks. Without a gap, the last training observations and first test observations are highly correlated, creating information leakage. The model effectively "knows" something about the near-future test data from the tail of its training data.

    - **Lagged features.** Many strategies use lagged variables (e.g., 20-day moving average, monthly momentum). If a strategy uses a 20-day lookback feature, the first test-day prediction depends on data from the previous 20 days, which overlaps with the training period. A gap of at least 20 days ensures no feature computed on the test set depends on training-period prices.

    - **Execution delay.** In practice, signals are generated with a delay (e.g., a signal computed at close is traded at next day's open). The gap mimics this real-world latency.

    - **Regime transition.** A gap reduces the risk that the test period begins during a regime that was heavily represented at the end of the training period, which would flatter autocorrelation-based strategies.

---

**Exercise 5.** Harvey, Liu, and Zhu (2016) argue that a $t$-statistic of at least 3.0 (rather than the traditional 2.0) should be required for new factor discoveries due to data snooping across decades of finance research. Explain the reasoning behind this higher threshold and compute the implied $p$-value for $t = 3.0$. How many independent tests would justify this threshold under a Bonferroni-type correction?

??? success "Solution to Exercise 5"
    **Harvey-Liu-Zhu threshold of $t \geq 3.0$ for new factors.**

    **Reasoning behind the higher threshold.** The traditional $t$-statistic threshold of 2.0 corresponds to a significance level of $\alpha = 0.05$ for a single, pre-specified hypothesis. However, the cross-section of expected returns literature has, over several decades, tested hundreds of candidate factors. Harvey, Liu, and Zhu (2016) estimate that over 300 factors have been tested. The standard $t = 2.0$ threshold ignores this multiplicity.

    If we treat the publication of each factor as an implicit test, the effective significance level must be adjusted for the total number of tests. Using a Bonferroni-type correction:

    $$
    t_{\text{threshold}} = \Phi^{-1}\!\left(1 - \frac{\alpha}{2m}\right)
    $$

    For $m = 300$ and $\alpha = 0.05$:

    $$
    t_{\text{threshold}} = \Phi^{-1}\!\left(1 - \frac{0.05}{600}\right) = \Phi^{-1}(0.9999167) \approx 3.78
    $$

    The recommendation of $t \geq 3.0$ is actually a somewhat lenient compromise.

    **$p$-value for $t = 3.0$:** For a two-sided test under a standard normal approximation:

    $$
    p = 2(1 - \Phi(3.0)) = 2(1 - 0.99865) = 2 \times 0.00135 = 0.0027
    $$

    **Implied number of tests under Bonferroni.** If $t = 3.0$ is the threshold, this corresponds to a per-test significance level of $\alpha/m = 0.0027$. For overall $\alpha = 0.05$:

    $$
    m = \frac{\alpha}{0.0027} = \frac{0.05}{0.0027} \approx 18.5
    $$

    So a threshold of $t = 3.0$ is the Bonferroni correction for approximately 18--19 independent tests. Given that over 300 factors have been tested, even $t = 3.0$ may be insufficient (the Bonferroni correction for 300 tests gives $t \approx 3.78$). The lower threshold of 3.0 reflects the fact that many factor tests are correlated (they use overlapping data and related economic concepts), which reduces the effective number of independent tests.

    **A factor with $t = 2.5$ based on 20 years of monthly data ($T = 240$):** The $p$-value is $2(1 - \Phi(2.5)) = 2(0.00621) = 0.0124$, which would be significant at the 5% level for a single test. However, given hundreds of tested factors, this evidence is insufficient. The factor would not survive even a modest Bonferroni correction with $m \geq 5$ tests.

---

**Exercise 6.** A machine learning model with 50 features is trained on 500 daily observations to predict next-day returns. Compute the ratio of parameters to observations and discuss whether overfitting is likely. Propose three specific regularization techniques (e.g., L1 penalty, dropout, early stopping) and explain how each reduces overfitting in this context.

??? success "Solution to Exercise 6"
    **Parameter-to-observation ratio and regularization.**

    **Parameter-to-observation ratio.** A linear model with 50 features has at least 51 parameters (50 coefficients + 1 intercept). The ratio is:

    $$
    \frac{p}{n} = \frac{51}{500} \approx 0.10
    $$

    For a more complex model (e.g., a neural network), the number of parameters can be much larger. As a rule of thumb, overfitting becomes a serious concern when $p/n > 0.05$, especially in finance where the signal-to-noise ratio is extremely low (daily return SNR $\approx 0.01$--$0.05$). With $p/n = 0.10$ and low SNR, **overfitting is very likely**: the model has enough capacity to fit noise patterns that do not generalize.

    The effective sample size is further reduced by serial correlation in financial data. If daily returns have autocorrelation $\rho$, the effective sample size is approximately:

    $$
    n_{\text{eff}} \approx n \cdot \frac{1 - \rho}{1 + \rho}
    $$

    With $\rho = 0.1$, $n_{\text{eff}} \approx 500 \times 0.818 = 409$, worsening the ratio.

    **Three regularization techniques:**

    **1. L1 penalty (Lasso).** Add an $\ell_1$ penalty to the loss function:

    $$
    \hat{\beta} = \arg\min_\beta \left\{\sum_{t=1}^n (r_t - x_t^\top \beta)^2 + \lambda \sum_{j=1}^p |\beta_j|\right\}
    $$

    The L1 penalty drives many coefficients exactly to zero, performing automatic **feature selection**. With 50 features and a low-SNR target, most features are likely noise; Lasso eliminates them, reducing the effective model complexity to perhaps 5--10 features. The penalty parameter $\lambda$ is chosen by cross-validation. This directly addresses overfitting by reducing the number of active parameters.

    **2. Dropout (for neural networks).** During each training iteration, randomly set a fraction $p_{\text{drop}}$ (e.g., 0.3) of hidden unit activations to zero. This prevents the network from relying on specific neurons and forces distributed representations. Effectively, dropout trains an ensemble of $2^H$ sub-networks (where $H$ is the number of hidden units), averaging their predictions at test time. In the context of financial prediction, dropout prevents the network from memorizing specific date-return associations and forces it to learn more robust patterns.

    **3. Early stopping.** Monitor the model's performance on a held-out validation set during training. Stop training when validation performance begins to degrade, even if training loss continues to decrease. The point of divergence between training and validation loss is the onset of overfitting. Early stopping implicitly regularizes by limiting the effective number of optimization steps, which constrains the model to remain in a neighborhood of the initialization where coefficients are small (akin to an $\ell_2$ penalty for gradient descent on linear models). For financial data, where the signal is weak, the optimal stopping point typically occurs very early in training.
