# Forward Pricing Map vs Inverse Calibration Map


Calibration is best understood as an **inverse problem**: we observe market prices (or implied volatilities) and seek model parameters that reproduce them. This section formalizes the *forward* and *inverse* maps and highlights why the inverse map is delicate.

---

## The forward pricing map


Let a parametric model be indexed by a parameter vector

\[
\theta \in \Theta \subset \mathbb{R}^d.
\]


Given a set of traded instruments \(\{I_j\}_{j=1}^m\) (e.g., vanilla options across strikes/maturities), the model produces prices

\[
P_j(\theta) := \text{ModelPrice}(I_j;\theta).
\]



Define the **forward pricing map**

\[
F:\Theta \to \mathbb{R}^m,\qquad
F(\theta) := (P_1(\theta),\dots,P_m(\theta)).
\]



### 1. Practical choices of data space


Depending on conventions and numerical stability, calibration may target:

- **Option prices** \(P^{\text{mkt}}_j\)
- **Implied volatilities** \(\sigma^{\text{impl}}_j\) (via a Black–Scholes inversion)
- **Normalized prices** (e.g., by forward/discount factor)
- **Local or total variance** (e.g., \(w=T\sigma^2\))

To unify notation, let

\[
y \in \mathbb{R}^m
\]


denote the chosen market data representation, and let \(F(\theta)\) output the matching model representation.

---

## The inverse calibration map


In an ideal world, calibration would mean “invert the map”:

\[
\theta = F^{-1}(y).
\]


But \(F\) is rarely invertible globally, and even when it is locally invertible, inversion can be unstable.

Instead, calibration is typically formulated as an **optimization problem**:

\[
\hat\theta \in \arg\min_{\theta\in\Theta} \; \mathcal{L}(F(\theta), y),
\]


where \(\mathcal{L}\) is a loss (misfit) function.

Common choices include:

- **Least squares on prices**

  \[
  \mathcal{L}(F(\theta),y)=\frac12\sum_{j=1}^m w_j\,(P_j(\theta)-P^{\text{mkt}}_j)^2
  \]


- **Least squares on implied vols**

  \[
  \mathcal{L}(F(\theta),y)=\frac12\sum_{j=1}^m w_j\,(\sigma^{\text{impl}}_j(\theta)-\sigma^{\text{impl,mkt}}_j)^2
  \]


- **Robust losses** (Huber, \(\ell_1\)) to reduce sensitivity to outliers

---

## Local linearization and sensitivity


A key lens is the Jacobian of the forward map:

\[
J(\theta) := \nabla_\theta F(\theta) \in \mathbb{R}^{m\times d}.
\]



Near a reference \(\theta_0\), we have

\[
F(\theta_0+\Delta\theta) \approx F(\theta_0) + J(\theta_0)\Delta\theta.
\]



If \(J\) has small singular values, small perturbations in data (e.g., bid/ask noise) can induce large changes in \(\Delta\theta\). This is the core mechanism behind instability of inverse calibration.

---

## Typical “inverse” workflow (static)


1. **Choose instruments** (smile slices, maturities, liquidity filters)
2. **Choose data representation** (prices vs implied vols)
3. **Choose objective** \(\mathcal{L}\) and weights \(w_j\)
4. **Solve optimization** (local/global methods)
5. **Validate** (out-of-sample instruments, stability checks, hedging impact)

---

## Key takeaways


- Pricing is the **forward** map \(F(\theta)\); calibration seeks the **inverse**.
- The inverse is usually posed as **optimization**, not explicit inversion.
- The Jacobian/singular values of \(J\) govern **sensitivity** and motivate **regularization** (next sections).

---

## Further reading


- Inverse problems and regularization: Tikhonov & Arsenin; Engl, Hanke & Neubauer.
- Calibration in quantitative finance: Gatheral (*The Volatility Surface*); Cont & Tankov (*Financial Modelling with Jump Processes*).

---

## Exercises

**Exercise 1.** Consider a model with parameter vector $\theta = (\sigma, \rho) \in \mathbb{R}^2$ and three traded instruments whose model prices are given by

$$
P_1(\theta) = \sigma^2, \quad P_2(\theta) = \sigma \rho, \quad P_3(\theta) = \rho^2
$$

Write down the forward pricing map $F:\Theta \to \mathbb{R}^3$. Compute the Jacobian $J(\theta)$ and determine for which values of $\theta$ the Jacobian fails to have full column rank. What does this imply about the invertibility of $F$ near those points?

---

**Exercise 2.** Suppose we calibrate to $m = 5$ implied volatilities using a model with $d = 3$ parameters. The singular values of the Jacobian at the calibrated point are $\sigma_1 = 12.4$, $\sigma_2 = 3.1$, $\sigma_3 = 0.002$. Compute the condition number $\kappa$ of $J$. Suppose the market data are perturbed by $\|\varepsilon\| = 0.5$ vol points. Provide an upper bound on $\|\Delta\theta\|$ using the linearized sensitivity relation and comment on the practical implication.

---

**Exercise 3.** A practitioner calibrates to option prices and obtains $\hat\theta_{\text{price}}$. She then re-calibrates using implied volatilities as the data representation and obtains $\hat\theta_{\text{vol}}$. Explain why $\hat\theta_{\text{price}}$ and $\hat\theta_{\text{vol}}$ may differ even though the underlying market data are the same. Which representation is more natural for out-of-the-money options and why?

---

**Exercise 4.** Let the forward map be $F(\theta) = A\theta + b$ for a matrix $A \in \mathbb{R}^{m \times d}$ and vector $b \in \mathbb{R}^m$. Show that the weighted least-squares calibration problem

$$
\min_\theta \frac{1}{2}(A\theta + b - y)^\top W (A\theta + b - y)
$$

has a unique solution if and only if $A^\top W A$ is invertible, and derive the closed-form expression for $\hat\theta$.

---

**Exercise 5.** Consider two loss functions for calibration: (i) least squares on prices, and (ii) least squares on implied volatilities. Let $\text{Vega}_j = \partial P_j / \partial \sigma_j^{\text{impl}}$ denote the Black-Scholes vega of the $j$-th option. Show that, to first order, calibrating on prices with equal weights $w_j = 1$ is equivalent to calibrating on implied volatilities with weights proportional to $\text{Vega}_j^2$.

---

**Exercise 6.** In the typical static calibration workflow, step 5 involves validation on out-of-sample instruments. Design a concrete validation procedure for a Heston model calibrated to S&P 500 options: specify what instruments you would hold out, what metrics you would evaluate, and what thresholds would indicate an acceptable calibration.

---

**Exercise 7.** Suppose the forward map satisfies $F(\theta_1) = F(\theta_2)$ for $\theta_1 \neq \theta_2$. Prove that the unregularized least-squares problem

$$
\min_\theta \|F(\theta) - y\|^2
$$

cannot have a unique global minimizer for any $y \in \mathrm{Range}(F)$. How does adding a Tikhonov penalty $\lambda \|\theta - \theta_{\text{prior}}\|^2$ resolve this issue?
