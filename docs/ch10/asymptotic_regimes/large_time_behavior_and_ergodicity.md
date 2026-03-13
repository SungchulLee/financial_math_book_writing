# Large-Time Behavior and Ergodicity


Large-time limits depend on whether the model admits a stationary distribution. The behavior of option prices and Greeks as \(T \to \infty\) differs fundamentally between ergodic and non-ergodic models.

---

## Non-ergodic Black–Scholes


Geometric Brownian motion has no stationary distribution in \(S\). Under the risk-neutral measure,

\[
S_T = S_0 \exp\!\left[\left(r - \frac{\sigma^2}{2}\right)T + \sigma W_T\right]
\]

As \(T \to \infty\):

- \(\log S_T\) has variance \(\sigma^2 T \to \infty\), so the distribution of \(S_T\) spreads without bound.
- The call price grows like \(S_0\) (bounded below by intrinsic value) while the put price converges to \(Ke^{-rT} \to 0\).

More precisely, for a European call:

\[
C(S_0, K, T) \to S_0 \quad \text{as } T \to \infty
\]

since \(N(d_1) \to 1\) and \(Ke^{-rT}N(d_2) \to 0\).

---

## Large-time behavior of Greeks in Black–Scholes


As \(T \to \infty\) (equivalently \(\tau \to \infty\)):

\[
\Delta_{\text{call}} = N(d_1) \to 1, \quad \Gamma \to 0, \quad \nu \to 0
\]

The option behaves increasingly like the underlying itself. This is intuitive: with enough time, any OTM call becomes ATM in expectation, and the option's optionality premium vanishes relative to the forward price.

For theta:

\[
\Theta_{\text{call}} \to rKe^{-rT}N(d_2) \to 0
\]

So time decay vanishes for very long-dated options — they are dominated by their delta exposure.

---

## Ergodic factors in multi-factor models


In multi-factor models, mean-reverting factors (e.g., variance in Heston-type models) may be ergodic with invariant measure \(\pi\). For a CIR-type variance process \(v_t\) satisfying

\[
dv_t = \kappa(\bar{v} - v_t)\,dt + \xi\sqrt{v_t}\,dW_t
\]

the process is ergodic when the Feller condition \(2\kappa\bar{v} > \xi^2\) holds, and for suitable functions \(f\):

\[
\frac{1}{T}\int_0^T f(v_s)\,\mathrm{d}s \xrightarrow{a.s.} \int f\,\mathrm{d}\pi
\]

where \(\pi\) is the Gamma distribution with shape \(\alpha = 2\kappa\bar{v}/\xi^2\) and rate \(\beta = 2\kappa/\xi^2\).

---

## Implications for long-dated option pricing


In stochastic volatility models with ergodic variance:

**Effective volatility convergence.** The time-averaged variance converges to the long-run mean:

\[
\frac{1}{T}\int_0^T v_s\,ds \xrightarrow{a.s.} \bar{v} \quad \text{as } T \to \infty
\]

This suggests that long-dated options are approximately priced by Black–Scholes with \(\sigma = \sqrt{\bar{v}}\), plus corrections that decay with maturity.

**Implied volatility term structure.** As \(T \to \infty\), implied volatility for ATM options converges to

\[
\sigma_{\text{implied}}(T) \to \sqrt{\bar{v}} + \mathcal{O}(T^{-1})
\]

The rate of convergence depends on the speed of mean reversion \(\kappa\).

---

## Large deviations and tail behavior


For non-ergodic components (like \(\log S\) itself), large-time behavior is governed by **large deviations theory**. The probability that the log-return deviates from its drift satisfies

\[
\mathbb{P}\!\left(\frac{\log(S_T/S_0)}{T} \notin [a,b]\right) \sim e^{-T \cdot I}
\]

where \(I\) is a rate function determined by the model. In Black–Scholes:

\[
I(x) = \frac{(x - \mu)^2}{2\sigma^2}
\]

with \(\mu = r - \sigma^2/2\) under the risk-neutral measure. This connects to the exponential decay of deep OTM option prices at long maturities.

---

## Practical relevance


Long-time asymptotics matter for:

- **LEAPS and long-dated warrants**: pricing and hedging options with maturities of several years.
- **Insurance-linked products**: equity-indexed annuities and variable annuity guarantees often have 10–30 year horizons.
- **Model calibration**: the long end of the implied volatility term structure constrains the ergodic properties of the variance process.
- **Risk management**: long-horizon VaR and expected shortfall calculations depend on whether variance factors are mean-reverting.

---

## What to remember


- Black–Scholes is not ergodic in \(S\); long-horizon option prices are dominated by drift and the option degenerates toward the underlying.
- Mean-reverting factors (e.g., stochastic variance) can be ergodic, and their long-run averages determine the effective volatility for long-dated options.
- Long-time asymptotics are model-dependent and linked to large deviations or ergodicity of latent factors.
- The rate of convergence to ergodic limits is governed by the mean-reversion speed.
