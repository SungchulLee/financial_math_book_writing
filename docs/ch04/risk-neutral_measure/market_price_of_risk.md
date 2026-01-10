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
