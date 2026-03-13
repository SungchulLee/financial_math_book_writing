# Construction of the Risk-Neutral Measure


The risk-neutral measure is a probability measure under which discounted asset prices
are martingales. Its existence is the mathematical expression of the absence of arbitrage.

This section explains how the risk-neutral measure is constructed using Girsanov’s theorem.

---

## Market Model


Consider a financial market consisting of:
- a risk-free asset \(B_t\),
- a risky asset \(S_t\).

Under the physical measure \(\mathbb{P}\), assume
\[
dS_t = \mu_t S_t\,dt + \sigma_t S_t\,dW_t^{\mathbb{P}},
\qquad
dB_t = r_t B_t\,dt,
\]
where \(\mu_t\), \(\sigma_t\), and \(r_t\) are adapted processes.

---

## Discounted Asset Price


Define the discounted price process
\[
\tilde S_t := \frac{S_t}{B_t}.
\]

Applying Itô’s formula,
\[
d\tilde S_t
= (\mu_t - r_t)\tilde S_t\,dt
+ \sigma_t \tilde S_t\,dW_t^{\mathbb{P}}.
\]

The presence of the drift term \((\mu_t - r_t)\) prevents \(\tilde S_t\) from being
a martingale under \(\mathbb{P}\).

---

## Measure Change


Define the process
\[
\theta_t := \frac{\mu_t - r_t}{\sigma_t},
\]
and the stochastic exponential
\[
Z_t = \exp\!\left(
- \int_0^t \theta_s\,dW_s^{\mathbb{P}}
- \frac12 \int_0^t \theta_s^2\,ds
\right).
\]

Under suitable integrability conditions, \(Z_t\) is a martingale and defines a new
probability measure \(\mathbb{Q}\) by
\[
\frac{d\mathbb{Q}}{d\mathbb{P}} \Big|_{\mathcal{F}_t} = Z_t.
\]

---

## Risk-Neutral Dynamics


By Girsanov’s theorem, the process
\[
W_t^{\mathbb{Q}} := W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds
\]
is a Brownian motion under \(\mathbb{Q}\).

The discounted asset price then satisfies
\[
d\tilde S_t = \sigma_t \tilde S_t\,dW_t^{\mathbb{Q}},
\]
and is therefore a martingale.

---

## Definition


A **risk-neutral measure** is a probability measure \(\mathbb{Q}\) equivalent to
\(\mathbb{P}\) under which all discounted traded asset prices are martingales.

Its existence ensures arbitrage-free pricing.
