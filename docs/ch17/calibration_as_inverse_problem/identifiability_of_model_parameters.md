# Identifiability of Model Parameters


**Identifiability** asks whether parameters can be determined uniquely (or at least reliably) from the available data. In calibration, lack of identifiability leads to unstable estimates, poor interpretability, and fragile hedging.

---

## Definitions


### 1. Structural identifiability (noise-free, idealized)


A model is **structurally identifiable** (with respect to chosen instruments) if

\[
F(\theta_1)=F(\theta_2) \;\Rightarrow\; \theta_1=\theta_2.
\]



This is a property of the model + instrument set, *not* of the optimizer.

### 2. Practical identifiability (finite, noisy data)


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

## Local identifiability via the Jacobian


A standard local criterion: if the Jacobian

\[
J(\theta)=\nabla_\theta F(\theta)\in\mathbb{R}^{m\times d}
\]


has **full column rank** at \(\theta\), then the parameters are locally identifiable (in a smooth setting).

Equivalently, if \(J^\top W J\) is nonsingular for a positive definite weight matrix \(W\), the (linearized) least-squares problem has a unique local solution.

### 1. Singular values as an identifiability score


Let \(J = U \Sigma V^\top\) be the SVD with singular values \(\sigma_1\ge \dots \ge \sigma_d\). Then:

- very small \(\sigma_d\) indicates a nearly unidentifiable direction,
- the condition number \(\kappa=\sigma_1/\sigma_d\) measures sensitivity.

---

## Examples of (non-)identifiability in option models


### 1. Redundancy between parameters


In many models, two different parameters can both change:

- overall variance level,
- skew strength,
- term-structure slope.

If the available option set does not excite both effects independently, parameters become entangled.

### 2. Maturity coverage matters


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

## How to improve identifiability


### 1. Better instrument design


- include both OTM puts and calls (skew information),
- include a range of maturities (term structure),
- filter out illiquid points, or down-weight them.

### 2. Re-parameterization


Choose parameters that are closer to what the market “sees”, e.g.:

- parameterize by at-the-money variance and skew proxies,
- use transformed parameters enforcing constraints smoothly (log/softplus).

### 3. Regularization and priors


If parameters are weakly identifiable, regularization stabilizes estimation:

- Tikhonov: penalize deviation from prior \(\theta_{\text{prior}}\),
- smoothness penalties (for functional parameters),
- Bayesian priors to express beliefs and uncertainty.

(See Chapter 5.3.)

### 4. Report uncertainty, not just point estimates


When identifiability is weak, produce:

- confidence intervals (approximate via Hessian / Fisher information),
- bootstrap distributions,
- parameter-stability plots over time.

---

## Key takeaways


- Identifiability is about whether the *data* constrain the parameters.
- Local identifiability is governed by the Jacobian rank / singular values.
- Practical identifiability can be poor even if structural identifiability holds.
- Remedies: instrument selection, re-parameterization, and regularization.

---

## Further reading


- Inverse problems: Engl, Hanke & Neubauer.
- Practical calibration discussions: Gatheral; Andersen & Piterbarg (volatility and calibration practice).

---

## Exercises

**Exercise 1.** Consider a model with forward pricing map $F(\theta_1, \theta_2) = (\theta_1 + \theta_2, \, \theta_1 \theta_2)$. Is this model structurally identifiable? Prove your answer by determining whether $F(\theta) = F(\theta')$ implies $\theta = \theta'$, or find an explicit counterexample.

---

**Exercise 2.** A stochastic volatility model has $d = 5$ parameters and is calibrated to $m = 20$ implied volatilities. The SVD of the Jacobian at the calibrated point yields singular values $\sigma_1 = 8.0$, $\sigma_2 = 5.2$, $\sigma_3 = 1.1$, $\sigma_4 = 0.03$, $\sigma_5 = 0.001$. Compute the condition number. Identify how many parameters are practically identifiable and how many are weakly identifiable. What specific remedies would you recommend?

---

**Exercise 3.** Suppose you calibrate the SABR model ($\alpha, \beta, \rho, \nu$) to a single-maturity smile consisting of 7 strike-volatility pairs. The parameter $\beta$ is known to be difficult to identify jointly with $\alpha$. Explain why this redundancy arises from the structure of the SABR formula and describe two practical approaches to resolve it.

---

**Exercise 4.** Let $J \in \mathbb{R}^{m \times d}$ be the Jacobian of the forward map and $W$ a diagonal weight matrix with entries $w_j > 0$. Show that the Fisher information matrix for the linearized problem is $\mathcal{I} = J^\top W J$. Derive an expression for the asymptotic covariance of the parameter estimates in terms of $\mathcal{I}$ and explain how this relates to identifiability.

---

**Exercise 5.** A practitioner calibrates a Heston model to two sets of instruments: (A) only ATM options across 6 maturities, and (B) ATM plus 25-delta and 10-delta options across the same 6 maturities. Which set is expected to yield better identifiability for the vol-of-vol parameter $\sigma_v$ and the correlation parameter $\rho$? Justify your answer in terms of the information content of each instrument set.

---

**Exercise 6.** Consider a re-parameterization from $(\sigma_0, \kappa) \mapsto (\sigma_0^2, \kappa / \sigma_0)$ in a mean-reverting volatility model. Compute the Jacobian of the transformation and discuss under what conditions the re-parameterization improves identifiability. When could it make identifiability worse?

---

**Exercise 7.** You observe that a calibrated parameter $\hat\theta_3$ fluctuates wildly from day to day despite stable market conditions. Describe a bootstrap-based diagnostic procedure to assess whether $\theta_3$ is practically identifiable. Specifically, outline the resampling scheme, the quantity to compute for each bootstrap sample, and the criterion for declaring weak identifiability.
