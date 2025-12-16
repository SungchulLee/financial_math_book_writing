# Identifiability of Model Parameters

**Identifiability** asks whether parameters can be determined uniquely (or at least reliably) from the available data. In calibration, lack of identifiability leads to unstable estimates, poor interpretability, and fragile hedging.

---

## 1. Definitions

### 1.1 Structural identifiability (noise-free, idealized)

A model is **structurally identifiable** (with respect to chosen instruments) if

\[
F(\theta_1)=F(\theta_2) \;\Rightarrow\; \theta_1=\theta_2.
\]



This is a property of the model + instrument set, *not* of the optimizer.

### 1.2 Practical identifiability (finite, noisy data)

In practice, we only need parameters to be distinguishable within noise:

\[
\|F(\theta_1)-F(\theta_2)\| \lesssim \text{noise level}
\quad\Rightarrow\quad
\theta_1,\theta_2 \text{ are practically indistinguishable.}
\]



Practical identifiability depends on:

- quote noise / liquidity,
- weights \(w_j\),
- instrument selection (strikes/maturities),
- numerical implementation.

---

## 2. Local identifiability via the Jacobian

A standard local criterion: if the Jacobian

\[
J(\theta)=\nabla_\theta F(\theta)\in\mathbb{R}^{m\times d}
\]


has **full column rank** at \(\theta\), then the parameters are locally identifiable (in a smooth setting).

Equivalently, if \(J^\top W J\) is nonsingular for a positive definite weight matrix \(W\), the (linearized) least-squares problem has a unique local solution.

### Singular values as an identifiability score

Let \(J = U \Sigma V^\top\) be the SVD with singular values \(\sigma_1\ge \dots \ge \sigma_d\). Then:

- very small \(\sigma_d\) indicates a nearly unidentifiable direction,
- the condition number \(\kappa=\sigma_1/\sigma_d\) measures sensitivity.

---

## 3. Examples of (non-)identifiability in option models

### 3.1 Redundancy between parameters

In many models, two different parameters can both change:

- overall variance level,
- skew strength,
- term-structure slope.

If the available option set does not excite both effects independently, parameters become entangled.

### 3.2 Maturity coverage matters

Short maturities can be informative about:

- instantaneous volatility level,
- jump intensity (if jumps exist),
- microstructure distortions (harder).

Long maturities are informative about:

- mean reversion,
- long-run variance,
- correlation effects (in stochastic vol).

Thus, identifiability is often improved by **joint calibration across maturities**.

---

## 4. How to improve identifiability

### 4.1 Better instrument design

- include both OTM puts and calls (skew information),
- include a range of maturities (term structure),
- filter out illiquid points, or down-weight them.

### 4.2 Re-parameterization

Choose parameters that are closer to what the market “sees”, e.g.:

- parameterize by at-the-money variance and skew proxies,
- use transformed parameters enforcing constraints smoothly (log/softplus).

### 4.3 Regularization and priors

If parameters are weakly identifiable, regularization stabilizes estimation:

- Tikhonov: penalize deviation from prior \(\theta_{\text{prior}}\),
- smoothness penalties (for functional parameters),
- Bayesian priors to express beliefs and uncertainty.

(See Chapter 5.3.)

### 4.4 Report uncertainty, not just point estimates

When identifiability is weak, produce:

- confidence intervals (approximate via Hessian / Fisher information),
- bootstrap distributions,
- parameter-stability plots over time.

---

## 5. Key takeaways

- Identifiability is about whether the *data* constrain the parameters.
- Local identifiability is governed by the Jacobian rank / singular values.
- Practical identifiability can be poor even if structural identifiability holds.
- Remedies: instrument selection, re-parameterization, and regularization.

---

## Further reading

- Inverse problems: Engl, Hanke & Neubauer.
- Practical calibration discussions: Gatheral; Andersen & Piterbarg (volatility and calibration practice).
