# Identifiability Issues


Calibration of stochastic volatility models is fundamentally limited by **identifiability**. Even with rich option surfaces, some parameters are only weakly constrained, leading to instability and ambiguity.

---

## Structural vs practical identifiability


A model is **structurally identifiable** if distinct parameter sets imply distinct option prices in theory.
In practice, calibration suffers from:

- finite and noisy data,
- limited maturity coverage,
- redundancy in parameter effects.

Thus, many parameters are only *practically* identifiable within wide confidence bands.

---

## Typical weakly identifiable parameters


Across stochastic volatility models, common weak points include:

- long-run variance vs initial variance,
- mean reversion speed,
- volatility-of-volatility at long maturities.

These parameters often affect prices in similar ways over limited horizons.

---

## Manifestations in calibration


Poor identifiability appears as:

- flat loss surfaces,
- multiple local minima,
- large day-to-day parameter swings,
- good in-sample fit but poor out-of-sample behavior.

These are inverse-problem symptoms, not optimizer failures.

---

## Diagnostic tools


Useful diagnostics include:

- Jacobian and singular-value analysis,
- fixing subsets of parameters and re-fitting,
- sensitivity analysis across maturities,
- stability checks under quote perturbations.

---

## Key takeaways


- Not all parameters are equally identifiable.
- Weak identifiability is intrinsic to stochastic volatility models.
- Calibration should prioritize stable directions.

---

## Further reading


- Engl, Hanke & Neubauer, *Regularization of Inverse Problems*.
- Gatheral, *The Volatility Surface*.

---

## Exercises

**Exercise 1.** In the Heston model, both $V_0$ and $\theta$ affect the ATM implied volatility level. Explain why these parameters are weakly identifiable when only short-maturity options are available. How does adding long-maturity options improve the situation? (Hint: consider the ATM variance formula $\sigma^2_{\text{impl}}(T) \approx V_0 \cdot \frac{1-e^{-\kappa T}}{\kappa T} + \theta(1 - \frac{1-e^{-\kappa T}}{\kappa T})$.)

---

**Exercise 2.** A practitioner observes that two Heston parameter sets give nearly identical option prices across all observed strikes and maturities:

| Parameter | Set A | Set B |
|-----------|-------|-------|
| $\kappa$  | 1.5   | 4.0   |
| $\theta$  | 0.06  | 0.035 |
| $\xi$     | 0.45  | 0.52  |
| $\rho$    | $-0.68$ | $-0.71$ |
| $V_0$     | 0.04  | 0.04  |

Compute $\kappa\theta$ for each set. Calculate the Feller ratio $\nu = 2\kappa\theta/\xi^2$ for each. Even though prices are similar, do the two parameter sets have different implications for simulation and risk management?

---

**Exercise 3.** Describe how to perform a Jacobian-based identifiability analysis. For a Heston model with parameter vector $\theta = (\kappa, \bar{\theta}, \xi, \rho, V_0)$ and $M$ observed implied volatilities $\sigma_i^{\text{mkt}}$, define the Jacobian matrix $J_{ij} = \partial\sigma_i^{\text{model}}/\partial\theta_j$. Explain how the singular values of $J$ reveal which parameter combinations are well-identified and which are not.

---

**Exercise 4.** Fixing $V_0$ from ATM short-maturity implied volatility reduces the Heston model to four free parameters. Explain why this improves practical identifiability. What potential issue arises if ATM implied vol is measured with noise? Propose an alternative approach that avoids fixing $V_0$ while still improving identifiability.

---

**Exercise 5.** A calibration produces a loss surface that is very flat in the $(\kappa, \theta)$ direction but steep in $(\rho, \xi)$. Sketch what this loss surface might look like in 2D cross-sections. What does the flatness imply about confidence intervals for $\kappa$ and $\theta$? Propose a reparameterization that might improve the conditioning of the optimization (e.g., calibrating $\kappa\theta$ and $\theta$ instead of $\kappa$ and $\theta$).

---

**Exercise 6.** An options surface has quotes only at maturities $T = 0.25$ and $T = 0.5$ years. Explain why the mean-reversion speed $\kappa$ is especially poorly identified in this case. What is the minimum set of maturities you would need to reliably identify $\kappa$? How does the half-life $t_{1/2} = \ln 2/\kappa$ relate to the required maturity range?
