# Stability and Identifiability


Calibration of interest-rate models faces challenges of **stability** and **identifiability**, especially in multi-factor and infinite-dimensional frameworks.

---

## Identifiability issues


Some parameters are weakly identifiable due to:
- limited option maturity coverage,
- correlations between factors,
- flat sensitivity of prices to certain directions.

This leads to multiple parameter sets fitting the same data.

---

## Stability across time


A stable calibration should exhibit:
- smooth parameter evolution,
- robustness to small quote changes,
- consistent dynamics across market regimes.

Large day-to-day parameter swings indicate overfitting.

---

## Diagnostic tools


Useful diagnostics include:
- sensitivity and Jacobian analysis,
- perturbation of market quotes,
- rolling-window calibration tests.

These help separate structural issues from numerical ones.

---

## Practical mitigation strategies


Stability is improved by:
- reducing model dimensionality,
- imposing economically motivated constraints,
- penalizing parameter variability,
- focusing calibration on the most liquid instruments.

Practitioners often prefer stability over perfect fit.

---

## Key takeaways


- Calibration stability is as important as fit quality.
- Identifiability problems are intrinsic, not technical.
- Regularization and parsimony are essential.

---

## Further reading


- Engl et al., inverse problems.
- Andersen & Piterbarg, calibration practice.

---

## Exercises

**Exercise 1.** Consider a two-factor Hull--White model with parameters $(a_1, \sigma_1, a_2, \sigma_2, \rho)$, where $a_i$ are mean-reversion speeds, $\sigma_i$ are volatilities, and $\rho$ is the factor correlation. Suppose you calibrate to a set of 10 co-terminal swaption volatilities. Explain why the pair $(a_2, \sigma_2)$ may be weakly identifiable when $\rho$ is close to $\pm 1$, and describe how you would detect this from the Jacobian matrix of the calibration.

---

**Exercise 2.** A calibration routine produces the following parameter values on three consecutive business days:

| Day | $a$ | $\sigma$ | $\rho$ |
|---|---|---|---|
| Mon | 0.05 | 0.012 | 0.75 |
| Tue | 0.18 | 0.009 | 0.42 |
| Wed | 0.06 | 0.011 | 0.72 |

The market quotes changed by less than 0.5 bps between days. Diagnose the likely cause of the Tuesday parameter jump and propose a regularization strategy that would prevent it while preserving the quality of fit.

---

**Exercise 3.** Let $\theta \in \mathbb{R}^p$ be the parameter vector and $V(\theta) \in \mathbb{R}^n$ be the vector of model prices. The Jacobian is $J = \partial V / \partial \theta$. Show that if $J$ has a singular value $\sigma_k \approx 0$, then the corresponding parameter direction $u_k$ (the right singular vector) is poorly identified. Explain how the condition number $\kappa(J) = \sigma_1 / \sigma_p$ relates to calibration stability.

---

**Exercise 4.** A practitioner adds a Tikhonov regularization penalty to the calibration objective:

$$
\min_\theta \sum_{i=1}^n w_i \bigl(V_i^{\text{model}}(\theta) - V_i^{\text{mkt}}\bigr)^2 + \lambda \|\theta - \theta_{\text{prior}}\|^2
$$

where $\theta_{\text{prior}}$ is a reference parameter vector (e.g., yesterday's calibrated values). Discuss how the regularization parameter $\lambda$ trades off goodness of fit against stability. Derive the first-order optimality condition and show how it relates to ridge regression.

---

**Exercise 5.** You are calibrating a LIBOR Market Model to a $10 \times 10$ swaption volatility matrix using an exponential correlation structure $\rho_{ij} = \rho_\infty + (1-\rho_\infty)e^{-\beta|T_i - T_j|}$. After calibration, you perturb the $5\text{Y} \times 5\text{Y}$ swaption volatility by $+1$ bp and re-calibrate. The parameters shift by $\Delta \rho_\infty = 0.08$ and $\Delta \beta = 0.15$. Is this level of sensitivity acceptable? Explain how you would use perturbation analysis systematically to assess whether the two-parameter correlation model provides a stable calibration.

---

**Exercise 6.** Explain the difference between **structural non-identifiability** (where distinct parameter values produce identical model outputs for all possible observations) and **practical non-identifiability** (where parameters are theoretically identifiable but cannot be distinguished given finite, noisy data). Give one example of each in the context of interest-rate model calibration.
