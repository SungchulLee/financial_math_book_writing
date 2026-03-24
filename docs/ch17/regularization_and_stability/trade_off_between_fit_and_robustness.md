# Trade-Off Between Fit and Robustness


Regularization introduces an unavoidable **trade-off**: improving robustness and stability typically worsens in-sample fit. Understanding and managing this trade-off is central to practical calibration.

---

## Bias–variance trade-off


Regularization reduces variance at the cost of bias:

- **Low regularization:** excellent fit, poor stability.
- **High regularization:** stable parameters, biased fit.

The optimal point depends on data quality, model purpose, and downstream use (pricing vs hedging).

---

## Diagnostics for the trade-off


Useful diagnostics include:

- **Residual plots:** detect systematic misfit patterns.
- **Parameter paths:** track parameters as regularization increases.
- **Stability tests:** re-calibrate under perturbed data.
- **Out-of-sample instruments:** test predictive power.

---

## Economic versus statistical fit


A statistically optimal fit may be economically undesirable:

- parameters may imply implausible dynamics,
- hedging Greeks may be unstable,
- scenario sensitivities may explode.

Robust calibration prioritizes *economic behavior* over minimal residuals.

---

## Time stability as a criterion


In practice, many desks judge calibration quality by:

- day-to-day parameter stability,
- smooth evolution over time,
- absence of large jumps without market justification.

This implicitly favors stronger regularization than pure in-sample metrics.

---

## Choosing robustness deliberately


Guiding principles:
- start with strong regularization,
- relax only when justified by stable, liquid data,
- prefer bias you understand to variance you cannot hedge.

---

## Key takeaways


- Perfect fit is not the goal; *robust behavior* is.
- Regularization controls the fit–robustness balance.
- Stability across time and scenarios is often the decisive metric.

---

## Further reading


- Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*.
- Tarantola, *Inverse Problem Theory*.
- Andersen & Piterbarg, practitioner discussions on calibration stability.

---

## Exercises

**Exercise 1.** Define the bias-variance trade-off for a regularized calibration estimator $\hat{\theta}_\lambda$. Write down the mean squared error decomposition

$$
\text{MSE}(\hat{\theta}_\lambda) = \text{Bias}^2(\hat{\theta}_\lambda) + \text{Var}(\hat{\theta}_\lambda)
$$

and explain qualitatively how each term depends on $\lambda$. Sketch the bias, variance, and MSE as functions of $\lambda$.

---

**Exercise 2.** A practitioner calibrates a Heston model with $\lambda = 0$ (no regularization) and $\lambda = 1.0$ (strong regularization toward yesterday's parameters). The in-sample RMSE is 0.15 vol points and 0.45 vol points respectively. The out-of-sample RMSE (next-day prediction) is 0.85 vol points and 0.52 vol points respectively. Interpret these results in terms of the bias-variance trade-off. Which $\lambda$ would you recommend for hedging purposes?

---

**Exercise 3.** Design a cross-validation procedure to select $\lambda$ for Tikhonov-regularized Heston calibration. Describe: (a) how to partition the 40 available vanilla option quotes into training and validation sets, (b) the metric to optimize on the validation set, and (c) how to handle the fact that different partitions may yield different optimal $\lambda$ values.

---

**Exercise 4.** Economic versus statistical fit: a calibration with $\lambda = 0$ yields $\kappa = 12.5$ and $\bar{v} = 0.001$, which implies a variance half-life of $\ln 2/12.5 \approx 0.055$ years (about 2 weeks) and long-run volatility of $\sqrt{0.001} \approx 3.2\%$. Argue that these values are economically implausible for an equity index. What range of $\kappa$ and $\bar{v}$ would you consider plausible? How would you encode these beliefs as a regularization penalty?

---

**Exercise 5.** A trading desk judges calibration quality by day-to-day parameter stability. They compute the ratio $R = \text{Var}(\Delta\theta)/\text{Var}(\Delta\text{market})$ where $\Delta\theta$ is the daily parameter change and $\Delta\text{market}$ is a market move indicator (e.g., VIX change). If $R \gg 1$, parameters are too noisy; if $R \ll 1$, they may be too sticky. Propose a target range for $R$ and describe how to adjust $\lambda$ to achieve it.

---

**Exercise 6.** Consider two calibration regimes: normal markets (low VIX, tight bid-ask spreads) and stressed markets (high VIX, wide spreads). Argue that the optimal regularization strength $\lambda$ should differ between these regimes. Should $\lambda$ be larger or smaller during stress? Justify your answer from both the data quality and economic perspectives.
