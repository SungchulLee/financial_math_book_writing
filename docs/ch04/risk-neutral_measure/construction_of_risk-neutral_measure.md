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

---

## Exercises

**Exercise 1.**
A stock has physical dynamics $dS_t = 0.10\,S_t\,dt + 0.25\,S_t\,dW_t^{\mathbb{P}}$ with risk-free rate $r = 0.04$. Compute the market price of risk $\theta$, write the Radon-Nikodym derivative $Z_T$, and derive the discounted price dynamics under $\mathbb{Q}$. Verify that the discounted price is a $\mathbb{Q}$-martingale.

---

**Exercise 2.**
Starting from the discounted price $\tilde{S}_t = S_t / B_t$ and its dynamics $d\tilde{S}_t = (\mu_t - r_t)\tilde{S}_t\,dt + \sigma_t\tilde{S}_t\,dW_t^{\mathbb{P}}$, show that choosing $\theta_t = (\mu_t - r_t)/\sigma_t$ and defining $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds$ eliminates the drift term in the $\tilde{S}_t$ dynamics. Why is this drift removal equivalent to the martingale property?

---

**Exercise 3.**
Explain why the risk-neutral measure $\mathbb{Q}$ must be equivalent to $\mathbb{P}$ (i.e., both measures agree on which events have probability zero). What would go wrong financially if $\mathbb{Q}$ assigned positive probability to an event that is impossible under $\mathbb{P}$?

---

**Exercise 4.**
For time-varying coefficients $\mu_t$, $\sigma_t$, and $r_t$, the market price of risk $\theta_t = (\mu_t - r_t)/\sigma_t$ is a stochastic process. State the Novikov condition that ensures $Z_t$ is a true martingale and $\mathbb{Q}$ is well-defined. Give an example where the condition fails.

---

**Exercise 5.**
Consider a market with two risky assets and one Brownian motion. Write the system of equations that $\theta$ must satisfy for both discounted prices to be $\mathbb{Q}$-martingales. Under what condition on $\mu_1, \mu_2, \sigma_1, \sigma_2, r$ is the system consistent (i.e., no arbitrage)?

---

**Exercise 6.**
A student claims: "The risk-neutral measure is the probability measure that investors actually use to form expectations." Explain why this is incorrect and describe the correct interpretation of $\mathbb{Q}$.

---

**Exercise 7.**
Suppose the risk-free rate is stochastic: $dr_t = \alpha(r_t)\,dt + \beta(r_t)\,dW_t^{\mathbb{P}}$, and the same Brownian motion drives the stock. Write the discounted stock price dynamics and determine $\theta_t$. Explain why this market is complete (one Brownian motion, one traded asset besides the bond).
