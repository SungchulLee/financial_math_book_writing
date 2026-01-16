# Risk-Neutral Valuation Principle

The **risk-neutral valuation principle** is the central pricing formula of mathematical finance. It states that the price of any derivative equals the discounted expected payoff under the risk-neutral measure, not the physical measure.

---

## The Fundamental Pricing Formula

In an arbitrage-free market, the time-$t$ price of a contingent claim with payoff $\Phi(X_T)$ at maturity $T$ is:

$$
\boxed{
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds}\Phi(X_T) \;\middle|\; \mathcal{F}_t\right]
}
$$

where:
- $\mathbb{Q}$ is the risk-neutral (equivalent martingale) measure
- $r_s$ is the instantaneous risk-free rate
- $\mathcal{F}_t$ is the information available at time $t$

For constant interest rate $r$:

$$
V_t = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(X_T) \mid \mathcal{F}_t]
$$

---

## Why Risk-Neutral, Not Physical?

Under the **physical measure** $\mathbb{P}$:
- Expected returns reflect risk preferences
- Different investors may assign different values
- No unique price emerges

Under the **risk-neutral measure** $\mathbb{Q}$:
- All assets earn the risk-free rate in expectation
- Prices are determined by no-arbitrage alone
- Unique prices emerge (in complete markets)

**Key insight**: Risk-neutral pricing is not about beliefs—it's about the price required to prevent arbitrage.

---

## Derivation from No-Arbitrage

### Step 1: Discounted Prices are Martingales

Under $\mathbb{Q}$, the discounted price process:

$$
\tilde{V}_t = e^{-\int_0^t r_s\,ds}V_t
$$

must be a martingale (by definition of $\mathbb{Q}$).

### Step 2: Apply Martingale Property

$$
\tilde{V}_t = \mathbb{E}^{\mathbb{Q}}[\tilde{V}_T \mid \mathcal{F}_t]
$$

### Step 3: Use Terminal Condition

At maturity, $V_T = \Phi(X_T)$, so:

$$
e^{-\int_0^t r_s\,ds}V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r_s\,ds}\Phi(X_T) \;\middle|\; \mathcal{F}_t\right]
$$

### Step 4: Rearrange

$$
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds}\Phi(X_T) \;\middle|\; \mathcal{F}_t\right]
$$

---

## The Meaning of Risk Neutrality

Under $\mathbb{Q}$, investors behave **as if** they are indifferent to risk:

| Physical World ($\mathbb{P}$) | Risk-Neutral World ($\mathbb{Q}$) |
|------------------------------|-----------------------------------|
| $\mathbb{E}^{\mathbb{P}}[dS/S] = \mu\,dt$ | $\mathbb{E}^{\mathbb{Q}}[dS/S] = r\,dt$ |
| Risk premium $\mu - r > 0$ | Risk premium = 0 |
| Prices reflect preferences | Prices reflect no-arbitrage |

**Important**: Risk-neutral pricing does not assume investors are actually risk-neutral. It's a mathematical transformation that simplifies pricing.

---

## Connection to PDE Pricing

Risk-neutral valuation is equivalent to solving the pricing PDE.

**Feynman-Kac**: If $V(t,x)$ satisfies:

$$
\frac{\partial V}{\partial t} + \mathcal{L}^{\mathbb{Q}}V - rV = 0, \quad V(T,x) = \Phi(x)
$$

where $\mathcal{L}^{\mathbb{Q}}$ is the generator under $\mathbb{Q}$, then:

$$
V(t,x) = \mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}\Phi(X_T) \mid X_t = x]
$$

**Two equivalent approaches**:
1. Solve the PDE (analytical/numerical)
2. Compute the expectation (Monte Carlo)

---

## Examples

### Example 1: European Call Option

Under $\mathbb{Q}$, the stock follows:

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

The call price is:

$$
C_t = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ \mid S_t]
$$

Since $S_T = S_t e^{(r-\sigma^2/2)(T-t) + \sigma\sqrt{T-t}Z}$ where $Z \sim N(0,1)$:

$$
C_t = S_t\Phi(d_1) - Ke^{-r(T-t)}\Phi(d_2)
$$

This is the **Black-Scholes formula**.

### Example 2: Zero-Coupon Bond

A bond paying $1$ at time $T$ has price:

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds} \;\middle|\; \mathcal{F}_t\right]
$$

For constant $r$: $P(t,T) = e^{-r(T-t)}$.

### Example 3: Digital Option

A digital call paying $1$ if $S_T > K$:

$$
V_t = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\mathbf{1}_{S_T > K}] = e^{-r(T-t)}\mathbb{Q}(S_T > K)
$$

Under Black-Scholes: $V_t = e^{-r(T-t)}\Phi(d_2)$.

---

## What Changes Under $\mathbb{Q}$?

| Quantity | Under $\mathbb{P}$ | Under $\mathbb{Q}$ |
|----------|-------------------|-------------------|
| Drift of $S$ | $\mu$ | $r$ |
| Volatility | $\sigma$ | $\sigma$ (unchanged) |
| Brownian motion | $W^{\mathbb{P}}$ | $W^{\mathbb{Q}} = W^{\mathbb{P}} + \int \theta\,ds$ |
| Probabilities | Reflect beliefs | Reflect prices |

**Volatility is invariant** under equivalent measure changes—only drift changes.

---

## Limitations and Extensions

### Incomplete Markets

When markets are incomplete:
- Multiple risk-neutral measures exist
- Pricing is not unique
- Additional criteria needed (utility, superhedging)

### Model Dependence

Risk-neutral pricing requires:
- A model for the underlying dynamics
- Calibration to market prices
- The price is only as good as the model

### Beyond European Payoffs

For path-dependent options:

$$
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds}\Phi(\{X_s\}_{t \leq s \leq T}) \;\middle|\; \mathcal{F}_t\right]
$$

The expectation may require Monte Carlo simulation.

---

## Summary

$$
\boxed{
V_t = \mathbb{E}^{\mathbb{Q}}\left[e^{-r(T-t)}\Phi(X_T) \mid \mathcal{F}_t\right]
}
$$

| Aspect | Description |
|--------|-------------|
| **What it says** | Price = discounted expected payoff under $\mathbb{Q}$ |
| **Why $\mathbb{Q}$** | Ensures no-arbitrage, unique prices |
| **What changes** | Drift becomes $r$; volatility unchanged |
| **Equivalence** | Same as solving pricing PDE |

**The risk-neutral valuation principle transforms the economic problem of pricing into a mathematical problem of computing expectations.**
