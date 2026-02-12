# Pathwise Differentiation


Pathwise differentiation computes Greeks by differentiating sample paths with respect to parameters or initial data.

---

## Mathematical framework


The key idea is to interchange differentiation and expectation:

\[
\frac{\partial}{\partial \theta} \mathbb{E}[\Phi(S_T^\theta)] = \mathbb{E}\left[\Phi'(S_T^\theta) \frac{\partial S_T^\theta}{\partial \theta}\right]
\]

**Justification.** This interchange is valid under dominated convergence if:

1. \(\Phi\) is Lipschitz continuous (hence a.e. differentiable)
2. \(\frac{\partial S_T^\theta}{\partial \theta}\) exists a.s. and is integrable
3. There exists an integrable dominating function: \(|\Phi'(S_T^\theta) \frac{\partial S_T^\theta}{\partial \theta}| \leq g(S_T)\) with \(\mathbb{E}[g(S_T)] < \infty\)

For smooth payoffs with polynomial growth, condition (3) follows from moment bounds on \(S_T\) and its Jacobian.

---

## Delta (Black–Scholes)


Since \(\partial S_T/\partial S = S_T/S\),

\[
\Delta(t,S)=\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\frac{S_T}{S}\right]
\]


for smooth \(\Phi\).

**Explicit verification.** For the log-normal model:

\[
S_T = S \exp\!\left((r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z\right), \quad Z \sim \mathcal{N}(0,1)
\]

The Jacobian \(\frac{\partial S_T}{\partial S} = \frac{S_T}{S}\) satisfies \(\mathbb{E}[(\frac{S_T}{S})^2] = e^{\sigma^2\tau} < \infty\).

For a call with \(\Phi(x) = (x-K)^+\) (which is Lipschitz but not smooth), the formula still yields:

\[
\Delta = \mathbb{E}^{t,S}\!\left[e^{-r\tau}\mathbf{1}_{S_T > K}\frac{S_T}{S}\right] = e^{-r\tau}\mathbb{E}\!\left[\mathbf{1}_{S_T > K}\frac{S_T}{S}\right]
\]

This equals \(N(d_1)\) after evaluation.

---

## Vega (Black–Scholes)


Differentiate \(S_T\) with respect to \(\sigma\):

\[
S_T = S \exp\!\left((r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z\right)
\]

\[
\frac{\partial S_T}{\partial \sigma}
=
S_T\left(\sqrt{\tau}Z - \sigma\tau\right)
\]

Thus, for smooth \(\Phi\),

\[
\boxed{
\nu(t,S)=
\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\,S_T\left(\sqrt{\tau}Z - \sigma\tau\right)\right]
}
\]

**Integrability condition.** Since \(|Z|e^{aZ}\) has finite moments for Gaussian \(Z\), the pathwise vega estimator is well-defined.

---

## Rho (Black–Scholes)


Differentiate with respect to \(r\):

\[
\frac{\partial S_T}{\partial r} = S_T \cdot \tau
\]

and the discount factor contributes \(-\tau e^{-r\tau}\). Thus:

\[
\rho = \mathbb{E}^{t,S}\!\left[-\tau e^{-r\tau}\Phi(S_T) + e^{-r\tau}\Phi'(S_T) \cdot S_T \tau\right]
\]

For a call, this simplifies to \(\rho = K\tau e^{-r\tau}N(d_2)\).

---

## Limitation: non-smooth payoffs


If \(\Phi\) has kinks, \(\Phi'\) is discontinuous and pathwise differentiation faces issues:

1. **Delta for calls/puts**: \(\Phi'(x) = \mathbf{1}_{x > K}\) is well-defined a.e., so delta works
2. **Gamma**: \(\Phi''(x) = \delta(S-K)\) is distributional, so naive pathwise differentiation fails
3. **Digital options**: \(\Phi(x) = \mathbf{1}_{x > K}\), so \(\Phi' = \delta(S-K)\) and pathwise delta fails

For these cases, likelihood ratio methods avoid derivatives of \(\Phi\) entirely.

---

## Comparison: pathwise vs likelihood ratio


| Method | Requires smooth \(\Phi\)? | Variance | Implementation |
|:-------|:-------------------------|:---------|:---------------|
| Pathwise | Yes (or Lipschitz) | Lower | Differentiate paths |
| Likelihood ratio | No | Higher | Differentiate density |

**Rule of thumb**: Use pathwise when possible (smooth payoffs), switch to LR for digital/barrier options.

---

## What to remember


- Pathwise methods are natural for smooth payoffs.
- Interchange of \(\partial/\partial\theta\) and \(\mathbb{E}\) requires dominated convergence conditions.
- For Lipschitz payoffs, pathwise delta and vega are well-defined.
- For kinked payoffs (gamma) or digital options (delta), likelihood ratio/Malliavin weights are preferable.
