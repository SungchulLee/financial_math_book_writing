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
V'(\theta)=\mathbb{E}_\theta\!\left[\Phi(X^\theta)\frac{\partial}{\partial \theta}\log p_\theta(X^\theta)\right].
}
\]
This avoids \(\Phi'\).

---

## Black–Scholes idea

\(\log S_T\) is Gaussian, so scores can be computed explicitly for parameters such as \(\sigma\) or \(S\), producing LR estimators of vega or delta.

---

## Malliavin perspective (conceptual)

For diffusions,
\[
\frac{\partial}{\partial x}\mathbb{E}[\Phi(X_T^x)]
=
\mathbb{E}[\Phi(X_T^x)\,H],
\]
where \(H\) is a weight built using Malliavin derivatives and covariance inverses.

---

## What to remember

- LR/Malliavin methods handle kinked payoffs well.
- The cost is potentially high variance from heavy-tailed weights.
