# Likelihood Ratio and Malliavin-Type Methods


Likelihood ratio methods move derivatives from the payoff to the distribution, enabling Greeks for nonsmooth payoffs.

---

## Score identity


If \(X^\theta\) has density \(p_\theta\),

\[
V(\theta)=\mathbb{E}_\theta[\Phi(X^\theta)]
=\int \Phi(x)p_\theta(x)\,\mathrm{d}x,
\]


then

\[
\boxed{
V'(\theta)=\mathbb{E}_\theta\!\left[\Phi(X^\theta)\frac{\partial}{\partial \theta}\log p_\theta(X^\theta)\right]
}
\]


This avoids \(\Phi'\). The quantity \(\frac{\partial}{\partial\theta}\log p_\theta\) is called the **score function**.

---

## Black–Scholes: Explicit LR estimators


In Black–Scholes, \(\log S_T = \log S + (r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z\) where \(Z \sim \mathcal{N}(0,1)\).

The density of \(Z\) is \(p(z) = \frac{1}{\sqrt{2\pi}}e^{-z^2/2}\), so \(\frac{\partial}{\partial z}\log p(z) = -z\).

**Delta via LR.** Treating \(S\) as a location parameter:

\[
\boxed{\Delta = \mathbb{E}\!\left[e^{-r\tau}\Phi(S_T) \cdot \frac{Z}{S\sigma\sqrt{\tau}}\right]}
\]

where \(Z = \frac{\log(S_T/S) - (r-\frac12\sigma^2)\tau}{\sigma\sqrt{\tau}}\) is the driving standard normal.

**Verification.** For a call, this yields \(\Delta = N(d_1)\) after evaluation.

**Vega via LR.** The volatility appears in both the drift and diffusion:

\[
\boxed{\nu = \mathbb{E}\!\left[e^{-r\tau}\Phi(S_T) \cdot \frac{Z^2 - 1 - Z\sigma\sqrt{\tau}}{\sigma}\right]}
\]

Alternatively:

\[
\nu = \mathbb{E}\!\left[e^{-r\tau}\Phi(S_T) \cdot \left(\frac{Zd_1}{\sigma} - \sqrt{\tau}\right)\right]
\]

**Gamma via LR.** The LR gamma estimator involves the second derivative of the log-density:

\[
\boxed{\Gamma = \mathbb{E}\!\left[e^{-r\tau}\Phi(S_T) \cdot \frac{Z^2 - Z\sigma\sqrt{\tau} - 1}{S^2\sigma^2\tau}\right]}
\]

This formula works even for digital options where pathwise gamma is undefined.

---

## Variance comparison


LR estimators often have higher variance than pathwise estimators:

| Greek | Pathwise variance | LR variance | Ratio |
|:------|:------------------|:------------|:------|
| Delta (smooth) | \(\mathcal{O}(1)\) | \(\mathcal{O}(1/\tau)\) | LR worse for short \(\tau\) |
| Vega (smooth) | \(\mathcal{O}(\tau)\) | \(\mathcal{O}(1)\) | Comparable |
| Gamma (kinked) | N/A | \(\mathcal{O}(1/\tau)\) | Only LR available |

**Variance reduction.** Control variates and antithetic sampling can significantly reduce LR variance.

---

## Malliavin calculus perspective (conceptual)


For diffusions driven by Brownian motion, Malliavin calculus provides a systematic framework for LR-type formulas.

**Key objects:**
- **Malliavin derivative** \(D_s X_T\): sensitivity of \(X_T\) to perturbations of \(W_s\)
- **Skorokhod integral** \(\delta(\cdot)\): adjoint of \(D\)
- **Malliavin covariance** \(\langle DX_T, DX_T \rangle_{L^2[0,T]}\)

**Integration by parts formula.** For \(F = \Phi(X_T)\) and suitable \(u\):

\[
\mathbb{E}[\Phi'(X_T) \cdot u] = \mathbb{E}[\Phi(X_T) \cdot H(u)]
\]

where \(H(u)\) is a **Malliavin weight** involving Skorokhod integrals and the inverse Malliavin covariance.

---

## Explicit Malliavin weights for Black–Scholes


**Delta weight:**

\[
H_\Delta = \frac{W_T - W_t}{S\sigma\tau} = \frac{\sqrt{\tau}Z}{S\sigma\tau} = \frac{Z}{S\sigma\sqrt{\tau}}
\]

This recovers the LR delta formula.

**Gamma weight:** The second-order Malliavin weight is:

\[
\boxed{H_\Gamma = \frac{1}{S^2\sigma^2\tau}\left(H_2(Z) - \frac{Z}{\sigma\sqrt{\tau}}\right)}
\]

where \(H_2(z) = z^2 - 1\) is the second Hermite polynomial. This gives:

\[
\Gamma = \mathbb{E}\!\left[e^{-r\tau}\Phi(S_T) \cdot H_\Gamma\right]
\]

**Vega weight:**

\[
H_\nu = \frac{Z^2 - 1}{\sigma} - \sqrt{\tau}Z
\]

---

## Localization and truncation


Near maturity, LR weights can have heavy tails (e.g., \(Z/\sqrt{\tau}\) blows up). Practical implementations use:

1. **Truncation**: Cap \(|Z|\) at some threshold
2. **Localization**: Use pathwise methods away from kinks, LR near kinks
3. **Smoothing**: Replace digital payoffs with smooth approximations

---

## Applications beyond vanilla options


LR/Malliavin methods are essential for:

- **Digital options**: Pathwise delta is undefined
- **Barrier options**: Delta involves hitting probabilities
- **Asian options**: Multiple sources of non-smoothness
- **Path-dependent exotics**: Complex dependence on trajectory

---

## What to remember


- LR/Malliavin methods handle kinked payoffs well by moving derivatives to the density.
- Explicit LR formulas exist for all Black–Scholes Greeks.
- The cost is potentially high variance from heavy-tailed weights, especially for short maturities.
- Malliavin calculus provides the theoretical foundation; Hermite polynomials appear in higher-order weights.
- Practical implementations combine pathwise (away from kinks) with LR (near kinks).
