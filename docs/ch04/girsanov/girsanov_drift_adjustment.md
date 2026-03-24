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

---

## Exercises

**Exercise 1.**
A stock follows $dS_t = 0.08\,S_t\,dt + 0.30\,S_t\,dW_t^{\mathbb{P}}$ with risk-free rate $r = 0.02$. Compute the market price of risk $\theta$, write the density process $Z_t$, and derive the risk-neutral dynamics of $S_t$.

---

**Exercise 2.**
Starting from the physical dynamics $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}$ and the definition $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$, show step by step that the discounted price process $e^{-rt}S_t$ is a $\mathbb{Q}$-martingale. In particular, verify that the $dt$ term vanishes after substitution.

---

**Exercise 3.**
Consider an asset with physical drift $\mu = 0.05$ and volatility $\sigma = 0.40$ in a market with $r = 0.03$. A second asset has $\mu' = 0.10$ and $\sigma' = 0.40$. Both assets are driven by the same Brownian motion. Compute $\theta$ for each asset. Are the two values consistent? What does this tell you about arbitrage in this market?

---

**Exercise 4.**
Explain why the volatility $\sigma$ is unchanged under the Girsanov measure change, while the drift changes from $\mu$ to $r$. Relate your answer to the fact that quadratic variation is a pathwise quantity.

---

**Exercise 5.**
Under $\mathbb{P}$, a zero-coupon bond price satisfies $dP(t,T) = \mu_P P(t,T)\,dt + \sigma_P P(t,T)\,dW_t^{\mathbb{P}}$. Apply the Girsanov drift adjustment to derive the dynamics under $\mathbb{Q}$ and show that the discounted bond price $e^{-\int_0^t r_s\,ds}P(t,T)$ is a $\mathbb{Q}$-martingale.

---

**Exercise 6.**
Suppose $\theta$ is not constant but depends on the current stock price: $\theta_t = (\mu(S_t) - r) / \sigma(S_t)$. Write the Radon-Nikodym derivative $Z_T$ in integral form and state the Novikov condition that must hold. Explain why this condition may fail for certain choices of $\mu(\cdot)$ and $\sigma(\cdot)$.

---

**Exercise 7.**
For the density process $Z_t = \exp(-\theta W_t^{\mathbb{P}} - \frac{1}{2}\theta^2 t)$ with constant $\theta = 0.3$ and $T = 2$, compute $\mathbb{E}^{\mathbb{P}}[Z_T]$ and verify it equals 1. Then compute $Z_T$ for a specific path where $W_T^{\mathbb{P}} = 1.5$ and interpret the result: is this path upweighted or downweighted under $\mathbb{Q}$?
