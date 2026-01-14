# Drift Adjustment and Financial Meaning


Girsanov’s theorem is used in finance to remove risk premia from asset prices,
making arbitrage-free pricing possible.

---

## Asset Price Dynamics


Under the physical measure \(\mathbb{P}\), assume

\[
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
\]

Discounting alone does not eliminate the drift unless \(\mu = r\).

---

## Market Price of Risk


Define the market price of risk

\[
\theta := \frac{\mu - r}{\sigma}
\]

This quantity measures excess return per unit of volatility.

---

## Measure Change


Define the density process

\[
Z_t = \exp\!\left(
-\theta W_t^{\mathbb{P}}
-\frac12 \theta^2 t
\right),
\qquad
\frac{d\mathbb{Q}}{d\mathbb{P}} = Z_T
\]

Under \(\mathbb{Q}\),

\[
W_t^{\mathbb{Q}} := W_t^{\mathbb{P}} + \theta t
\]

is a Brownian motion.

---

## Risk-Neutral Dynamics


Under the risk-neutral measure \(\mathbb{Q}\),

\[
dS_t = r S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
\]

The discounted price process \(e^{-rt}S_t\) is therefore a martingale.

---

## Interpretation


- Expected returns are adjusted to the risk-free rate
- Volatility is unchanged
- Sample paths are identical; probabilities are reweighted

This drift adjustment is the mathematical foundation of risk-neutral pricing.
