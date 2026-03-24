# Market Price of Risk


The market price of risk quantifies how much excess return investors demand per unit
of risk. It plays a central role in the change of measure from the physical to the
risk-neutral world.

---

## Definition


For a risky asset with dynamics
\[
dS_t = \mu_t S_t\,dt + \sigma_t S_t\,dW_t^{\mathbb{P}},
\]
the **market price of risk** is defined as
\[
\theta_t := \frac{\mu_t - r_t}{\sigma_t}.
\]

It measures excess drift relative to volatility.

---

## Interpretation


- Large \(\theta_t\): high compensation required for bearing risk
- Small \(\theta_t\): low risk premium

The market price of risk determines how probabilities are tilted when moving from
\(\mathbb{P}\) to \(\mathbb{Q}\).

---

## Role in Measure Change


The drift adjustment in Girsanov’s theorem is precisely \(\theta_t\):
\[
W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds.
\]

Thus:
- \(\theta_t\) removes excess drift,
- volatility remains unchanged.

---

## Multi-Asset Case


In a market with \(n\) risky assets driven by a \(d\)-dimensional Brownian motion,
the market price of risk becomes a vector \(\boldsymbol{\theta}_t \in \mathbb{R}^d\),
satisfying
\[
\boldsymbol{\mu}_t - r_t \mathbf{1}
= \Sigma_t \boldsymbol{\theta}_t,
\]
where \(\Sigma_t\) is the volatility matrix.

---

## Summary


The market price of risk:
- encodes risk premia,
- determines the Radon–Nikodym derivative,
- links economic intuition with probabilistic structure.

It is the key quantity connecting observed returns to risk-neutral pricing.

---

## Exercises

**Exercise 1.**
A stock has $\mu = 0.09$, $\sigma = 0.20$, and $r = 0.03$. Compute the market price of risk $\theta$. If $\mu$ increases to $0.12$ while $\sigma$ and $r$ remain unchanged, how does $\theta$ change? Interpret this economically.

---

**Exercise 2.**
Using the definition $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds$, show that under $\mathbb{Q}$ the drift of the stock price process changes from $\mu$ to $r$, while the volatility $\sigma$ is unchanged. Explain why $\theta$ is called the "price" of risk.

---

**Exercise 3.**
In a two-asset market with volatility matrix $\Sigma$ and excess return vector $\boldsymbol{\mu} - r\mathbf{1}$, the market price of risk vector satisfies $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$. Suppose $\Sigma$ is a $2 \times 3$ matrix (two assets, three Brownian motions). How many free parameters does $\boldsymbol{\theta}$ have? What does this imply about market completeness?

---

**Exercise 4.**
Show that the market price of risk $\theta = (\mu - r)/\sigma$ equals the Sharpe ratio of the asset. Explain why this means all assets in a single-factor complete market must have the same Sharpe ratio, and relate this to the absence of arbitrage.

---

**Exercise 5.**
Suppose $\theta_t$ is time-varying with $\theta_t = a + b\sin(2\pi t)$ where $a = 0.3$ and $b = 0.2$. Compute $\int_0^1 \theta_t^2\,dt$ and verify that the Novikov condition is satisfied for $T = 1$. Does the market price of risk need to be constant for the risk-neutral measure to exist?

---

**Exercise 6.**
A market has two stocks both driven by the same Brownian motion: $dS_t^i = \mu_i S_t^i\,dt + \sigma_i S_t^i\,dW_t$ for $i = 1, 2$. Show that no-arbitrage requires $(\mu_1 - r)/\sigma_1 = (\mu_2 - r)/\sigma_2$. What happens if this equality is violated?

---

**Exercise 7.**
In an interest rate model, the market price of risk is specified exogenously as $\theta_t = \lambda r_t / \sigma$ (proportional to the short rate). Write the risk-neutral dynamics of the short rate and explain how $\theta_t$ modifies the physical drift. Why can't $\theta_t$ be determined from traded asset prices alone in this setting?
