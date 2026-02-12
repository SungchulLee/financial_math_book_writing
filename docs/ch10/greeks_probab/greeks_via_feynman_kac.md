# Greeks via Feynman–Kac


Feynman–Kac represents prices as expectations and can yield expectation representations for Greeks. This probabilistic approach is foundational for Monte Carlo methods and extends naturally beyond Black–Scholes.

---

## Price as expectation


Under the risk-neutral measure \(\mathbb{Q}\),

\[
\mathrm{d}S_t = rS_t\,\mathrm{d}t + \sigma S_t\,\mathrm{d}W_t
\]

and the Feynman–Kac theorem gives

\[
V(t,S) = \mathbb{E}^{t,S}\!\left[e^{-r(T-t)}\Phi(S_T)\right]
\]

where \(\mathbb{E}^{t,S}\) denotes expectation conditional on \(S_t = S\). This is the probabilistic counterpart of the Black–Scholes PDE: \(V\) solves the PDE if and only if it equals this conditional expectation.

---

## The stochastic flow


In Black–Scholes, the terminal value has the explicit form

\[
S_T = S\exp\!\left((r - \tfrac{1}{2}\sigma^2)\tau + \sigma(W_T - W_t)\right), \quad \tau = T - t
\]

This is \(C^\infty\) in the initial condition \(S\), and the **stochastic flow derivative** (Jacobian) is

\[
\boxed{\frac{\partial S_T}{\partial S} = \frac{S_T}{S}}
\]

This ratio is key: it converts differentiation with respect to the initial condition into a multiplicative weight involving the terminal value. The identity holds because geometric Brownian motion is log-linear in its initial condition.

---

## Delta via pathwise differentiation


For sufficiently smooth payoff \(\Phi\), we can interchange differentiation and expectation:

\[
\Delta(t,S) = \frac{\partial}{\partial S}\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi(S_T)\right]
= \mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\frac{\partial S_T}{\partial S}\right]
\]

Using the stochastic flow:

\[
\boxed{
\Delta(t,S) = \mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\frac{S_T}{S}\right]
}
\]

**Verification for the European call.** With \(\Phi(x) = (x - K)^+\), we have \(\Phi'(x) = \mathbf{1}_{x > K}\) (a.e.), so

\[
\Delta = \frac{e^{-r\tau}}{S}\mathbb{E}^{t,S}\!\left[S_T \mathbf{1}_{S_T > K}\right]
\]

Computing this expectation under the log-normal distribution recovers \(\Delta = N(d_1)\).

---

## Vega via Feynman–Kac


The sensitivity to volatility requires differentiating through the distribution of \(S_T\). Writing \(S_T = S\exp((r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}\,Z)\) where \(Z \sim N(0,1)\):

\[
\frac{\partial S_T}{\partial \sigma} = S_T\left(-\sigma\tau + \sqrt{\tau}\,Z\right)
\]

For smooth \(\Phi\):

\[
\nu(t,S) = \mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\cdot S_T(-\sigma\tau + \sqrt{\tau}\,Z)\right]
\]

This is the **pathwise vega estimator**, valid when \(\Phi\) is differentiable. It provides an unbiased Monte Carlo estimator for vega.

---

## Rho via Feynman–Kac


Differentiating with respect to \(r\) affects both the discount factor and the drift:

\[
\rho = \frac{\partial}{\partial r}\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi(S_T)\right]
\]

This gives two terms:

\[
\rho = -\tau\,V(t,S) + e^{-r\tau}\mathbb{E}^{t,S}\!\left[\Phi'(S_T)\frac{\partial S_T}{\partial r}\right]
\]

Since \(\frac{\partial S_T}{\partial r} = \tau S_T\):

\[
\rho = -\tau V + e^{-r\tau}\tau\,\mathbb{E}^{t,S}\!\left[\Phi'(S_T)S_T\right]
\]

For a call, this simplifies to \(\rho = K\tau e^{-r\tau}N(d_2)\).

---

## Gamma is delicate


The second derivative with respect to \(S\) requires

\[
\Gamma = \mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi''(S_T)\left(\frac{S_T}{S}\right)^2\right] + \mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\frac{\partial^2 S_T}{\partial S^2}\right]
\]

For geometric Brownian motion, \(\frac{\partial^2 S_T}{\partial S^2} = 0\) (the flow is linear in \(S\)), so

\[
\Gamma = \frac{1}{S^2}\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi''(S_T)S_T^2\right]
\]

**Problem.** For the standard call payoff \(\Phi(x) = (x-K)^+\), we have \(\Phi''(x) = \delta(x-K)\) (Dirac delta), which is distributional. The pathwise approach breaks down because the payoff has a kink at \(K\).

**Resolutions:**

- **Smoothing**: replace \(\Phi\) by a smooth approximation \(\Phi_\epsilon\) and take \(\epsilon \to 0\).
- **Likelihood ratio method**: move the derivative from the payoff to the density (see *Likelihood Ratio and Malliavin Methods*).
- **PDE-based gamma**: compute from the closed-form \(\Gamma = N'(d_1)/(S\sigma\sqrt{\tau})\) directly.
- **Finite differences**: estimate \(\Gamma \approx (V(S+h) - 2V(S) + V(S-h))/h^2\) via re-simulation.

---

## General diffusion models


For a general SDE \(dS_t = \mu(t,S_t)\,dt + \sigma(t,S_t)\,dW_t\), the stochastic flow \(Y_t := \partial S_t/\partial S_0\) satisfies the **variational equation**:

\[
dY_t = \mu'(t,S_t)Y_t\,dt + \sigma'(t,S_t)Y_t\,dW_t, \quad Y_0 = 1
\]

where primes denote derivatives with respect to \(S\). The delta is then

\[
\Delta = \mathbb{E}\!\left[e^{-r\tau}\Phi'(S_T)Y_T\right]
\]

This extends the Feynman–Kac approach to local volatility models, CEV models, and beyond — wherever the flow \(Y_T\) can be simulated alongside the forward path.

---

## Practical Monte Carlo implementation


The Feynman–Kac representations lead to the following Monte Carlo workflow for Greeks:

1. **Simulate paths**: generate \(N\) independent paths of \(S_T^{(i)}\).
2. **Delta**: compute \(\hat{\Delta} = \frac{1}{N}\sum_{i=1}^N e^{-r\tau}\Phi'(S_T^{(i)})\frac{S_T^{(i)}}{S}\).
3. **Vega**: compute \(\hat{\nu} = \frac{1}{N}\sum_{i=1}^N e^{-r\tau}\Phi'(S_T^{(i)})S_T^{(i)}(-\sigma\tau + \sqrt{\tau}\,Z^{(i)})\).
4. **Gamma**: use likelihood ratio weights or finite differences (not pathwise).

Variance reduction techniques (antithetic variates, control variates, importance sampling) can dramatically improve the efficiency of these estimators.

---

## What to remember


- Delta can be written as an expectation involving the Jacobian \(\partial S_T/\partial S\), enabling pathwise Monte Carlo estimation.
- Vega and rho have analogous pathwise representations.
- Gamma requires more care when payoffs are nonsmooth; the pathwise method fails for kinked payoffs like vanilla calls and puts.
- The stochastic flow approach generalizes to arbitrary diffusion models through the variational equation.
