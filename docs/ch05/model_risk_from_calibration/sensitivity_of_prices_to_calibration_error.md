# Sensitivity of Prices to Calibration Error

Calibration error translates directly into **model risk**: even small mis-estimation of parameters can lead to non-negligible pricing errors, especially for nonlinear or path-dependent payoffs.

---

## 1. From parameter error to price error

Let \(\hat\theta\) be the calibrated parameter vector and \(\theta^\star\) the (unknown) true parameter.
A first-order expansion yields
\[
\Delta P \approx \nabla_\theta P(\hat\theta)^{\top}(\hat\theta-\theta^\star).
\]

Thus, price sensitivity depends on:
- the magnitude of parameter uncertainty,
- the gradient of prices with respect to parameters.

---

## 2. Linear versus nonlinear effects

For vanilla options near calibration points, first-order effects may dominate.
For exotics:
- nonlinearities amplify parameter errors,
- sensitivities can be highly state-dependent.

This explains why exotics often exhibit much larger model risk than vanillas.

---

## 3. Concentration of sensitivity

Price sensitivity is typically concentrated in:
- long maturities (term-structure uncertainty),
- deep OTM regions (tail sensitivity),
- products sensitive to volatility-of-volatility or correlation.

Calibration error in weakly identified parameters can therefore dominate pricing error.

---

## 4. Practical measurement

Common approaches include:
- bump-and-reprice in parameter space,
- scenario analysis using alternative calibrations,
- computing price dispersion across plausible parameter sets.

These approaches provide *ranges* rather than point estimates.

---

## 5. Key takeaways

- Calibration error propagates directly into price uncertainty.
- Linear approximations may understate risk for nonlinear payoffs.
- Model risk assessment requires exploring parameter uncertainty.

---

## Further reading

- Cont, *Model Uncertainty and Its Impact on Pricing*.
- Glasserman, *Monte Carlo Methods in Financial Engineering*.
