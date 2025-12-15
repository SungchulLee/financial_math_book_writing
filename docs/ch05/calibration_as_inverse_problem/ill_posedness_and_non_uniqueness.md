# Ill-Posedness and Non-Uniqueness

Inverse problems are often **ill-posed** in the sense of Hadamard. Calibration inherits this ill-posedness: market data are noisy and incomplete, and multiple parameter sets can fit the same data almost equally well.

---

## 1. Hadamard well-posedness

A problem is **well-posed** if:

1. **Existence:** a solution exists.
2. **Uniqueness:** the solution is unique.
3. **Stability:** the solution depends continuously on the data.

Calibration can violate (2) and (3) even when (1) holds.

---

## 2. Why calibration is often ill-posed

### 2.1 Incomplete information

Market quotes provide a finite set of prices (\(m\) instruments), while models may have:

- many parameters (\(d\) large),
- hidden state variables,
- functional degrees of freedom (e.g., a local volatility surface \(\sigma_{\text{loc}}(t,S)\)).

Even when \(m\ge d\), the effective rank of the Jacobian may be much smaller due to redundancy and weak sensitivity.

### 2.2 Noisy data

Observed prices are affected by:

- bid–ask spreads,
- stale quotes,
- microstructure noise,
- interpolation/extrapolation artifacts (surface construction).

Let the true data be \(y^\star\) and observed data \(y = y^\star + \varepsilon\). If the inverse map is unstable, \(\varepsilon\) is amplified into large parameter errors.

### 2.3 Model misspecification

Even with perfect data, the model may be unable to fit all instruments:
\[
y \notin \mathrm{Range}(F).
\]
Then the optimization problem has a best-fit solution but no exact inverse.

---

## 3. Non-uniqueness mechanisms

### 3.1 Flat directions (parameter degeneracy)

If the loss surface has valleys, many \(\theta\) yield nearly identical fit:
\[
\mathcal{L}(F(\theta),y) \approx \text{constant along a curve/manifold}.
\]

This occurs when two parameters play similar roles (e.g., both affect overall variance level).

### 3.2 Over-parameterization

Adding parameters can reduce in-sample error without improving explanatory power. Two common symptoms:

- extremely large/small parameter values,
- unstable calibrated parameters day-to-day.

### 3.3 Hidden constraints and bounds

Constraints (positivity, Feller condition, no-arbitrage filters) can create multiple local minima:
- one “good fit” region near the boundary,
- another interior region with slightly worse fit but better stability.

---

## 4. A linearized view: conditioning and singular values

Around a reference \(\theta_0\), with \(F(\theta)\approx F(\theta_0)+J\Delta\theta\), least squares suggests
\[
\Delta\theta \approx (J^\top W J)^{-1}J^\top W (y - F(\theta_0)).
\]

If \(J^\top WJ\) is ill-conditioned (small eigenvalues), then:

- the inverse is numerically unstable,
- \(\|\Delta\theta\|\) can blow up relative to data noise.

This connects directly to **regularization** (Chapter 5.3).

---

## 5. Practical diagnostics

- **Sensitivity / Greeks-to-parameters:** check Jacobian magnitudes.
- **Bootstrap / re-sample quotes:** re-calibrate after perturbing \(y\) within bid–ask.
- **Profile likelihood / one-parameter sweeps:** visualize flat directions.
- **Multiple initializations:** detect multi-modality / local minima.

---

## 6. Key takeaways

- Calibration often fails **uniqueness** and **stability**.
- Non-uniqueness is not a bug in the optimizer; it is structural.
- Regularization and better parameterizations are standard remedies.

---

## Further reading

- Hadamard, *Lectures on Cauchy’s problem in linear partial differential equations*.
- Engl, Hanke & Neubauer, *Regularization of Inverse Problems*.
- Gatheral, *The Volatility Surface* (practical calibration issues).
