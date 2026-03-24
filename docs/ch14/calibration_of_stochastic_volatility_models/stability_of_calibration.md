# Stability of Calibration


Beyond fit quality, a calibration must be **stable**: small changes in market data should not cause large parameter shifts. Stability is a central criterion for production models.

---

## Sources of instability


Calibration instability arises from:

- ill-posed inverse problems,
- weakly identifiable parameters,
- noisy or illiquid quotes,
- overly flexible objectives.

These factors interact nonlinearly.

---

## Measuring stability


Common stability checks include:

- re-calibration under perturbed quotes,
- rolling-window calibration,
- monitoring parameter time series,
- comparing alternative weighting schemes.

Stability should be assessed across market regimes.

---

## Regularization and constraints


Stability is improved by:

- regularization (penalties, priors),
- economically motivated bounds,
- reduced parameterization,
- maturity-balanced objectives.

These reduce variance at the cost of bias.

---

## Practical acceptance criteria


In practice, desks often require:

- smooth parameter evolution over time,
- limited sensitivity to individual quotes,
- consistent pricing of benchmark instruments.

A slightly worse fit is often acceptable if stability improves.

---

## Key takeaways


- Stability is as important as in-sample accuracy.
- Regularization is essential in stochastic volatility calibration.
- Calibration quality must be judged dynamically, not pointwise.

---

## Further reading


- Rebonato, *Volatility and Correlation*.
- Andersen & Piterbarg, calibration stability discussions.

---

## Exercises

**Exercise 1.** A Heston model is calibrated to S&P 500 options on Monday, yielding $\kappa = 2.1$, $\theta = 0.042$, $\xi = 0.51$. On Tuesday, with ATM vol shifting by 0.5 vol points, the recalibration gives $\kappa = 3.8$, $\theta = 0.031$, $\xi = 0.62$. Compute the percentage change in each parameter. Is this calibration stable? What specific feature of the parameter space might cause such large shifts?

---

**Exercise 2.** A regularized calibration objective is

$$
\mathcal{L}_{\text{reg}}(\theta) = \mathcal{L}(\theta) + \lambda \|\theta - \theta_{\text{prior}}\|^2
$$

where $\mathcal{L}(\theta)$ is the standard fit error and $\theta_{\text{prior}}$ is yesterday's calibrated parameter. For $\lambda = 0$, the calibration changes parameters by 40% day-over-day. For $\lambda = 10$, the change is 5% but the fit error increases by 0.3 vol points. Discuss the bias-variance trade-off. How would you choose $\lambda$ in practice?

---

**Exercise 3.** Describe a rolling-window stability test for Heston calibration. Specifically, outline a procedure that: (a) calibrates to options on each of 20 consecutive trading days; (b) records the five Heston parameters daily; (c) computes a stability metric. Propose a specific metric (e.g., average daily parameter change normalized by parameter value) and explain what threshold would indicate acceptable stability.

---

**Exercise 4.** Two calibrations of the Heston model to the same data yield nearly identical fit errors ($RMSE_1 = 0.32\%$ vs. $RMSE_2 = 0.34\%$ in implied vol) but very different parameters: $(\kappa_1, \theta_1) = (1.5, 0.06)$ and $(\kappa_2, \theta_2) = (4.0, 0.035)$. Compute $\kappa\theta$ for each and explain why the product $\kappa\theta$ may be better identified than $\kappa$ and $\theta$ individually. What does this imply for practical calibration?

---

**Exercise 5.** A desk requires that no single quote perturbation of 0.2 vol points should change any Heston parameter by more than 10%. Design a sensitivity test to check this requirement. Specifically, describe: (a) how many perturbation scenarios to test; (b) how to perturb each quote; (c) how to aggregate the results into a pass/fail criterion.

---

**Exercise 6.** Explain why reducing the number of free parameters improves stability but potentially worsens fit quality. Consider the following calibration approaches for the Heston model: (a) all five parameters free; (b) fix $V_0$ from ATM implied vol, calibrate four parameters; (c) fix both $V_0$ and $\kappa$, calibrate three parameters. For each approach, discuss the expected trade-off between stability and fit quality.
