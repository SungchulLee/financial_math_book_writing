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

## Monte Carlo Implementation: Finite Difference Methods

The simplest computational approach is finite difference approximation:

\[
\frac{\partial V}{\partial \theta} \approx \frac{V(\theta + d\theta) - V(\theta)}{d\theta} \quad \text{(Forward Difference)}
\]

\[
\frac{\partial V}{\partial \theta} \approx \frac{V(\theta) - V(\theta - d\theta)}{d\theta} \quad \text{(Backward Difference)}
\]

\[
\frac{\partial V}{\partial \theta} \approx \frac{V(\theta + d\theta) - V(\theta - d\theta)}{2d\theta} \quad \text{(Central Difference, second-order)}
\]

Central differences have \(O(d\theta^2)\) error, while forward and backward differences have \(O(d\theta)\) error. The practical challenge is choosing \(d\theta\) to balance discretization error and sampling noise.

---

## Likelihood Ratio Method

The likelihood ratio method, also called the score function method, computes Greeks without differentiating the payoff function. Instead, it differentiates the probability density:

\[
\frac{\partial V}{\partial \theta} = e^{-r\tau} \int V(T,S) \frac{\partial f_\theta(s)}{\partial \theta} ds
\]

Rewriting using the density:

\[
\frac{\partial V}{\partial \theta} = e^{-r\tau} \int V(T,S) \frac{\partial \log f_\theta(s)}{\partial \theta} f_\theta(s) ds = e^{-r\tau} \mathbb{E}\left[V(T,S) \frac{\partial \log f(S_T)}{\partial \theta}\right]
\]

### Likelihood Ratio Delta

For a Black–Scholes stock process with parameter \(\theta = S_0\) (initial price):

\[
S_T = S_0 \exp\left(\left(r - \frac{1}{2}\sigma^2\right)\tau + \sigma\sqrt{\tau}Z\right), \quad Z \sim \mathcal{N}(0,1)
\]

Taking the log derivative with respect to \(S_0\):

\[
\frac{\partial \log f(S_T)}{\partial S_0} = \frac{1}{S_0}
\]

Thus:

\[
\Delta = e^{-r\tau} \mathbb{E}\left[V(T,S_T) \cdot \frac{1}{S_0}\right]
\]

For a call option, this becomes:

\[
\Delta = \frac{e^{-r\tau}}{S_0} \mathbb{E}[(S_T - K)^+ ]
\]

### Likelihood Ratio Vega

For volatility parameter \(\theta = \sigma\):

\[
S_T = S_0 \exp\left(\left(r - \frac{1}{2}\sigma^2\right)\tau + \sigma\sqrt{\tau}Z\right)
\]

The score function (log derivative of density) with respect to \(\sigma\) is:

\[
\frac{\partial \log f(S_T)}{\partial \sigma} = \frac{1}{\sigma^3\tau}\left(\log(S_T/S_0) - \left(r - \frac{1}{2}\sigma^2\right)\tau\right) \cdot \left(\sqrt{\tau}Z - \sigma\tau\right)
\]

Simplifying:

\[
\nu = \frac{e^{-r\tau}}{\sigma\tau} \mathbb{E}\left[\max(S_T - K, 0) \left(\sqrt{\tau}Z - \sigma\tau\right)\right]
\]

The advantage of likelihood ratio is that it works for non-smooth payoffs (e.g., digital options) where pathwise differentiation fails.

---

## Pathwise Delta in Heston Model

For the Heston stochastic volatility model:

\[
dS(t) = rS(t)dt + \sqrt{v(t)}S(t)dW_x^{\mathbb{Q}}(t)
\]

The pathwise delta under Heston is:

\[
\Delta = e^{-r\tau} \mathbb{E}^{\mathbb{Q}}\left[\Phi'(S_T) \frac{S_T}{S_0}\right]
\]

The key difference from Black–Scholes is that the Jacobian \(\frac{\partial S_T}{\partial S_0}\) still equals \(\frac{S_T}{S_0}\) due to linearity in the drift coefficient with respect to \(S\), but the path-dependent volatility introduces additional variance in the Monte Carlo estimator.

---

## What to remember


- Pathwise methods are natural for smooth payoffs and have lower variance.
- Interchange of \(\partial/\partial\theta\) and \(\mathbb{E}\) requires dominated convergence conditions.
- For Lipschitz payoffs, pathwise delta and vega are well-defined.
- Likelihood ratio methods work for kinked payoffs (gamma, digital options) but exhibit higher variance.
- Finite difference is simple to implement but requires careful choice of step size \(d\theta\).
- Heston model preserves pathwise delta formula but increases sampling variance due to stochastic volatility.
