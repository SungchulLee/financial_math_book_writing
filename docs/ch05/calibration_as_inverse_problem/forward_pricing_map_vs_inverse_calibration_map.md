# Forward Pricing Map vs Inverse Calibration Map

Calibration is best understood as an **inverse problem**: we observe market prices (or implied volatilities) and seek model parameters that reproduce them. This section formalizes the *forward* and *inverse* maps and highlights why the inverse map is delicate.

---

## 1. The forward pricing map

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

### Practical choices of data space

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

## 2. The inverse calibration map

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

## 3. Local linearization and sensitivity

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

## 4. Typical “inverse” workflow (static)

1. **Choose instruments** (smile slices, maturities, liquidity filters)
2. **Choose data representation** (prices vs implied vols)
3. **Choose objective** \(\mathcal{L}\) and weights \(w_j\)
4. **Solve optimization** (local/global methods)
5. **Validate** (out-of-sample instruments, stability checks, hedging impact)

---

## 5. Key takeaways

- Pricing is the **forward** map \(F(\theta)\); calibration seeks the **inverse**.
- The inverse is usually posed as **optimization**, not explicit inversion.
- The Jacobian/singular values of \(J\) govern **sensitivity** and motivate **regularization** (next sections).

---

## Further reading

- Inverse problems and regularization: Tikhonov & Arsenin; Engl, Hanke & Neubauer.
- Calibration in quantitative finance: Gatheral (*The Volatility Surface*); Cont & Tankov (*Financial Modelling with Jump Processes*).
