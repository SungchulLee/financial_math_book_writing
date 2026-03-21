# Girsanov's Theorem


Girsanov's theorem is one of the most powerful tools in mathematical finance. It describes how a change of probability measure modifies the drift of a stochastic process while preserving its Brownian structure. This is essential for pricing derivatives via risk-neutral measures.

---

## Setting and Assumptions

Let $(\Omega, \mathcal{F}, \{\mathcal{F}_t\}, \mathbb{P})$ be a filtered probability space supporting a standard Brownian motion $W_t$.

Let $\theta_t$ be an **adapted process** (the **Girsanov kernel**) satisfying the **Novikov condition**:

$$
\mathbb{E}^{\mathbb{P}}\!\left[
\exp\!\left(\frac{1}{2} \int_0^T \theta_s^2 \,ds\right)
\right] < \infty
$$

This condition ensures that the exponential martingale does not explode and is a true martingale (not just a local martingale).

---

## The Exponential Martingale

Define the **Radon-Nikodym derivative** (also called the **exponential martingale**):

$$
\boxed{
Z_t = \exp\!\left(
-\int_0^t \theta_s\, dW_s
-\frac{1}{2} \int_0^t \theta_s^2 \,ds
\right)
}
$$

**Key properties:**

1. **Strictly positive:** $Z_t > 0$ almost surely for all $t$
2. **Martingale:** Under the original measure $\mathbb{P}$, $Z_t$ is a true martingale
3. **Unit expectation:** $\mathbb{E}^{\mathbb{P}}[Z_t] = 1$ for all $t$

**Why the form?** The specific structure $-\int \theta\,dW_s - \frac{1}{2}\int \theta^2 ds$ arises from Itô's lemma applied to exponential functions, ensuring the martingale property.

---

## The Measure Change

Define a new probability measure $\mathbb{Q}$ on $\mathcal{F}_T$ via:

$$
\boxed{
\frac{d\mathbb{Q}}{d\mathbb{P}}\Big|_{\mathcal{F}_T} = Z_T
}
$$

For any random variable $X$, the relationship between expectations under the two measures is:

$$
\mathbb{E}^{\mathbb{Q}}[X] = \mathbb{E}^{\mathbb{P}}[X \cdot Z_T]
$$

For events in the σ-algebra $\mathcal{F}_t$ (where $t \leq T$), since $Z_t$ is a martingale:

$$
\mathbb{Q}(A) = \mathbb{E}^{\mathbb{P}}[Z_T \cdot \mathbf{1}_A] = \mathbb{E}^{\mathbb{P}}[Z_t \cdot \mathbf{1}_A], \quad A \in \mathcal{F}_t
$$

---

## Statement of Girsanov's Theorem

**Theorem (Girsanov, 1960):** Under the new measure $\mathbb{Q}$, the process

$$
\boxed{
\widetilde{W}_t := W_t + \int_0^t \theta_s \,ds
}
$$

is a **standard Brownian motion**.

**Equivalently:** The original Brownian motion $W_t$ can be written as

$$
W_t = \widetilde{W}_t - \int_0^t \theta_s\,ds
$$

under $\mathbb{Q}$.

---

## Interpretation: The Drift Removal Mechanism

| Perspective | Under $\mathbb{P}$ (Original Measure) | Under $\mathbb{Q}$ (New Measure) |
|-------------|--------------------------------------|--------------------------------|
| Brownian motion | $W_t$ is standard | $\widetilde{W}_t$ is standard |
| Transformed BM | $\widetilde{W}_t = W_t + \int \theta\,ds$ has drift | Driftless |
| What changed | Original measure | Probability measure and interpretation |
| Information structure | Same filtration | Same filtration |
| Volatility | Unchanged | Unchanged |

**Key insight:** The theorem shows that drift can be removed by reweighting paths via a change of measure. The drift is not a fundamental property of the process—it's an artifact of how we assign probabilities to outcomes.

---

## Connection to SDEs: Removing Drift

**Original SDE under $\mathbb{P}$:**

$$
dX_t = \mu(t)\,dt + \sigma(t)\,dW_t
$$

where $\mu(t)$ is the drift.

**Choose Girsanov kernel:** $\theta_t = \frac{\mu(t)}{\sigma(t)}$ (assuming $\sigma(t) \neq 0$)

**Under $\mathbb{Q}$:** Since $W_t = \widetilde{W}_t - \int_0^t \theta_s\,ds$:

$$
dX_t = \mu(t)\,dt + \sigma(t)\left(d\widetilde{W}_t - \theta_t\,dt\right)
$$

$$
= \mu(t)\,dt + \sigma(t)\,d\widetilde{W}_t - \sigma(t)\theta_t\,dt
$$

$$
= \left(\mu(t) - \sigma(t)\theta_t\right)dt + \sigma(t)\,d\widetilde{W}_t
$$

$$
= 0\,dt + \sigma(t)\,d\widetilde{W}_t
$$

$$
= \sigma(t)\,d\widetilde{W}_t
$$

**Result:** The drift has been completely removed under $\mathbb{Q}$!

---

## Financial Application: Risk-Neutral Pricing

**Problem:** Price a derivative given the stock price dynamics under the physical measure $\mathbb{P}$:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
$$

The risk $\mu$ and risk-free rate $r$ are different, so this is not a martingale.

**Solution via Girsanov:**

1. **Choose Girsanov kernel:** $\theta = \frac{\mu - r}{\sigma}$ (market price of risk)

2. **Define numeraire-relative measure $\mathbb{Q}$:** Use $Z_T = \exp\left(-\int_0^T \theta\,dW_s - \frac{1}{2}\int_0^T \theta^2\,ds\right)$

3. **Under $\mathbb{Q}$:** The discounted stock price becomes a martingale:

$$
d(e^{-rt}S_t) = 0\,dt + e^{-rt}\sigma S_t\,d\widetilde{W}_t
$$

4. **Option price:** Risk-neutral expectation:

$$
C(t, S_t) = e^{-r(T-t)} \mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ | \mathcal{F}_t]
$$

This is the foundation of the Black-Scholes pricing formula.

---

## Example 1: Drifted Brownian Motion

**Original process under $\mathbb{P}$:**

$$
dX_t = \mu\,dt + \sigma\,dW_t, \quad X_0 = 0
$$

where $\mu$ and $\sigma$ are constants.

**Choose Girsanov kernel:** $\theta = \frac{\mu}{\sigma}$ (constant)

**Check Novikov condition:**

$$
\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\int_0^T \left(\frac{\mu}{\sigma}\right)^2 ds\right)\right] = \exp\left(\frac{\mu^2 T}{2\sigma^2}\right) < \infty \quad \checkmark
$$

**Exponential martingale:**

$$
Z_t = \exp\left(-\frac{\mu}{\sigma}W_t - \frac{\mu^2 t}{2\sigma^2}\right)
$$

**Under $\mathbb{Q}$ with $d\mathbb{Q}/d\mathbb{P} = Z_T$:**

$$
\widetilde{W}_t := W_t + \frac{\mu}{\sigma}t \text{ is a standard Brownian motion}
$$

**Therefore:** Substituting back into the original SDE:

$$
dX_t = \mu\,dt + \sigma\left(d\widetilde{W}_t - \frac{\mu}{\sigma}dt\right) = 0\,dt + \sigma\,d\widetilde{W}_t = \sigma\,d\widetilde{W}_t
$$

The drift has been **completely removed** under $\mathbb{Q}$!

**Under $\mathbb{Q}$:**

$$
X_t = \sigma\widetilde{W}_t \sim \mathcal{N}(0, \sigma^2 t)
$$

---

## Example 2: Geometric Brownian Motion (Stock Price)

**Original process under $\mathbb{P}$ (physical measure):**

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
$$

where:
- $\mu$ = real-world drift (expected return)
- $\sigma$ = volatility
- $r$ = risk-free rate (assumed constant)

**Key observation:** The discounted stock price $e^{-rt}S_t$ is NOT a $\mathbb{P}$-martingale because:

$$
d(e^{-rt}S_t) = -re^{-rt}S_t\,dt + e^{-rt}dS_t
$$

$$
= -re^{-rt}S_t\,dt + e^{-rt}(\mu S_t\,dt + \sigma S_t\,dW_t)
$$

$$
= e^{-rt}S_t(\mu - r)\,dt + e^{-rt}\sigma S_t\,dW_t$$

The $dt$ coefficient is $(\mu - r)S_t e^{-rt} \neq 0$ (unless $\mu = r$), so this is not a martingale.

**Choose Girsanov kernel:** The market price of risk

$$
\theta = \frac{\mu - r}{\sigma}
$$

**Check Novikov condition:**

$$
\mathbb{E}^{\mathbb{P}}\left[\exp\left(\frac{1}{2}\int_0^T \left(\frac{\mu-r}{\sigma}\right)^2 ds\right)\right] = \exp\left(\frac{(\mu-r)^2 T}{2\sigma^2}\right) < \infty \quad \checkmark
$$

**Exponential martingale (Radon-Nikodym derivative):**

$$
Z_t = \exp\left(-\frac{\mu - r}{\sigma}W_t - \frac{(\mu-r)^2 t}{2\sigma^2}\right)
$$

**Under $\mathbb{Q}$ with $d\mathbb{Q}/d\mathbb{P} = Z_T$:**

$$
\widetilde{W}_t := W_t + \frac{\mu - r}{\sigma}t \text{ is a standard Brownian motion}
$$

**Transform the SDE:** Since $W_t = \widetilde{W}_t - \frac{\mu-r}{\sigma}t$:

$$
dS_t = \mu S_t\,dt + \sigma S_t\left(d\widetilde{W}_t - \frac{\mu-r}{\sigma}dt\right)
$$

$$
= \mu S_t\,dt + \sigma S_t\,d\widetilde{W}_t - (\mu - r)S_t\,dt
$$

$$
= rS_t\,dt + \sigma S_t\,d\widetilde{W}_t
$$

**Result under $\mathbb{Q}$ (risk-neutral measure):**

$$
dS_t = rS_t\,dt + \sigma S_t\,d\widetilde{W}_t
$$

Now the discounted stock price is a martingale:

$$
d(e^{-rt}S_t) = -re^{-rt}S_t\,dt + e^{-rt}dS_t
$$

$$
= -re^{-rt}S_t\,dt + e^{-rt}(rS_t\,dt + \sigma S_t\,d\widetilde{W}_t)
$$

$$
= e^{-rt}\sigma S_t\,d\widetilde{W}_t \quad \text{(martingale!)}
$$

**Option pricing:** A European call option with strike $K$ and maturity $T$ has price:

$$
C(t, S_t) = e^{-r(T-t)} \mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ | \mathcal{F}_t]
$$

where the expectation is under the **risk-neutral measure** $\mathbb{Q}$.

**Key insight:** Under $\mathbb{Q}$:
- The expected return of the stock is $r$ (risk-free rate)
- Investors are indifferent to risk
- This is why derivative prices don't depend on $\mu$!

---

## Example 3: Vasicek Model (Interest Rates)

**Original process under $\mathbb{P}$:**

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t
$$

where:
- $\theta$ = long-run mean interest rate
- $\kappa$ = mean reversion speed
- $\sigma$ = volatility

**Typical market price of risk:** $\lambda$ (constant or time-dependent)

**Choose Girsanov kernel:** $\theta = \lambda$

**Under the risk-neutral measure $\mathbb{Q}$:**

Define $\widetilde{W}_t = W_t + \lambda t$

$$
dr_t = [\kappa(\theta - r_t) - \lambda\sigma]\,dt + \sigma\,d\widetilde{W}_t
$$

The effective "long-run mean" becomes:

$$
\theta^* = \theta - \frac{\lambda}{\kappa}
$$

**Financial interpretation:** The market price of interest rate risk ($\lambda$) shifts the equilibrium level of rates from $\theta$ to $\theta^*$. The real-world view ($\mathbb{P}$) and the pricing view ($\mathbb{Q}$) differ precisely by this market price.

---

## Why Girsanov Matters in Finance

Girsanov's theorem is indispensable because:

1. **Separation of expectations from pricing:** The real-world drift $\mu$ (what market participants believe will happen) differs from the risk-neutral drift $r$ (what the market prices in)

2. **Universal pricing formula:** All derivatives can be priced via risk-neutral expectations, regardless of investors' actual beliefs

3. **Model calibration:** We can fit models to market prices using $\mathbb{Q}$ measures, then extract market prices of risk to understand investor preferences

4. **Consistent pricing across assets:** Girsanov ensures that a single choice of numeraire and measure prices all derivatives consistently

5. **Computational advantage:** Working under $\mathbb{Q}$ often simplifies calculations because many prices become martingales
