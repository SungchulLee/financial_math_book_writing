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


Financial research often involves:
- testing many strategies,
- selecting the best-performing ones,
- ignoring failed experiments.

This leads to false discoveries.

---

## Consequences


False discoveries result in:
- spurious trading strategies,
- inflated backtest performance,
- real-world losses when deployed.

They undermine confidence in models.

---

## Mitigation techniques


Common defenses include:
- out-of-sample validation,
- cross-validation adapted to time series,
- statistical corrections for multiple testing,
- economic plausibility checks.

Discipline is crucial.

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

---

**Exercise 2.** Describe the difference between in-sample and out-of-sample validation for a trading strategy. A strategy achieves an annualized Sharpe ratio of 2.5 in-sample but 0.3 out-of-sample. Estimate the degree of overfitting using the deflated Sharpe ratio framework and explain what factors contribute to the gap.

---

**Exercise 3.** The Bonferroni correction adjusts the significance level from $\alpha$ to $\alpha / m$ when $m$ tests are conducted. For $m = 200$ strategy backtests and $\alpha = 0.05$, compute the adjusted threshold. Explain why the Bonferroni correction is conservative and describe the Benjamini-Hochberg procedure as a less conservative alternative that controls the false discovery rate.

---

**Exercise 4.** Cross-validation for time series data must respect temporal ordering (no future information leakage). Describe a walk-forward validation scheme for evaluating a trading strategy: define the training window, the gap period, and the test period. Why is a gap period between training and testing important in financial applications?

---

**Exercise 5.** Harvey, Liu, and Zhu (2016) argue that a $t$-statistic of at least 3.0 (rather than the traditional 2.0) should be required for new factor discoveries due to data snooping across decades of finance research. Explain the reasoning behind this higher threshold and compute the implied $p$-value for $t = 3.0$. How many independent tests would justify this threshold under a Bonferroni-type correction?

---

**Exercise 6.** A machine learning model with 50 features is trained on 500 daily observations to predict next-day returns. Compute the ratio of parameters to observations and discuss whether overfitting is likely. Propose three specific regularization techniques (e.g., L1 penalty, dropout, early stopping) and explain how each reduces overfitting in this context.
