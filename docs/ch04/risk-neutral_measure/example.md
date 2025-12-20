# Examples: Black–Scholes and Multi-Asset Models

This section illustrates the construction of the risk-neutral measure in standard models.

---

## Black–Scholes Model

Under \(\mathbb{P}\),
\[
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}.
\]

The market price of risk is constant:
\[
\theta = \frac{\mu - r}{\sigma}.
\]

Define
\[
W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t.
\]

Under \(\mathbb{Q}\),
\[
dS_t = r S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}},
\]
and the discounted price is a martingale.

---

## Multi-Asset Model

Let \(S_t = (S_t^1,\dots,S_t^n)\) satisfy
\[
dS_t^i = \mu_i S_t^i\,dt + \sum_{j=1}^d \sigma_{ij} S_t^i\,dW_t^{j,\mathbb{P}}.
\]

The vector market price of risk \(\boldsymbol{\theta}\) solves
\[
\boldsymbol{\mu} - r\mathbf{1} = \Sigma \boldsymbol{\theta}.
\]

If \(\Sigma\) has full rank, the market is complete and \(\boldsymbol{\theta}\) is unique.

---

## Interpretation

- Uniqueness of \(\mathbb{Q}\) ⇔ market completeness
- Multiple solutions ⇔ incomplete markets

These distinctions will reappear in later chapters.
