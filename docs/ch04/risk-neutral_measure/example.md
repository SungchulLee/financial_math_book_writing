# Examples: Constructing Risk-Neutral Measures

This section provides detailed worked examples of constructing the risk-neutral measure in various market models, from the basic Black-Scholes setting to multi-asset and interest rate models.

---

## Example 1: Black-Scholes Model (Single Stock)

### Physical Dynamics

Under $\mathbb{P}$, the stock price follows:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
$$

with constant parameters $\mu$ (expected return) and $\sigma$ (volatility).

### Step 1: Identify the Market Price of Risk

The market price of risk is:

$$
\theta = \frac{\mu - r}{\sigma}
$$

**Example**: If $\mu = 0.12$, $r = 0.05$, $\sigma = 0.20$:

$$
\theta = \frac{0.12 - 0.05}{0.20} = 0.35
$$

### Step 2: Define the Radon-Nikodym Derivative

$$
Z_T = \exp\left(-\theta W_T^{\mathbb{P}} - \frac{1}{2}\theta^2 T\right)
$$

$$
\frac{d\mathbb{Q}}{d\mathbb{P}} = Z_T
$$

### Step 3: Apply Girsanov

Under $\mathbb{Q}$:

$$
W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t
$$

is a Brownian motion.

### Step 4: Risk-Neutral Dynamics

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
$$

$$
= \mu S_t\,dt + \sigma S_t\,(dW_t^{\mathbb{Q}} - \theta\,dt)
$$

$$
= (\mu - \sigma\theta)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

$$
= rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

### Verification

The discounted price $\tilde{S}_t = e^{-rt}S_t$ satisfies:

$$
d\tilde{S}_t = \sigma\tilde{S}_t\,dW_t^{\mathbb{Q}}
$$

No drift term—$\tilde{S}_t$ is a $\mathbb{Q}$-martingale. ✓

---

## Example 2: Stock with Dividends

### Physical Dynamics

$$
dS_t = (\mu - q)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
$$

where $q$ is the continuous dividend yield.

### Market Price of Risk

$$
\theta = \frac{(\mu - q) - (r - q)}{\sigma} = \frac{\mu - r}{\sigma}
$$

Same as before—dividends don't affect $\theta$.

### Risk-Neutral Dynamics

$$
dS_t = (r - q)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

### Discounted Process

The appropriate discounted process is $e^{-rt}S_t e^{qt} = e^{-(r-q)t}S_t$:

$$
d(e^{-(r-q)t}S_t) = \sigma e^{-(r-q)t}S_t\,dW_t^{\mathbb{Q}}
$$

This is a martingale. ✓

---

## Example 3: Two Correlated Stocks

### Physical Dynamics

$$
\begin{cases}
dS_t^1 = \mu_1 S_t^1\,dt + \sigma_1 S_t^1\,dW_t^{1,\mathbb{P}} \\
dS_t^2 = \mu_2 S_t^2\,dt + \sigma_2 S_t^2\,(\rho\,dW_t^{1,\mathbb{P}} + \sqrt{1-\rho^2}\,dW_t^{2,\mathbb{P}})
\end{cases}
$$

where $W^1, W^2$ are independent and $\rho$ is the correlation.

### Market Price of Risk Vector

We need $\boldsymbol{\theta} = (\theta_1, \theta_2)$ such that:

$$
\begin{pmatrix} \mu_1 - r \\ \mu_2 - r \end{pmatrix} = \begin{pmatrix} \sigma_1 & 0 \\ \sigma_2\rho & \sigma_2\sqrt{1-\rho^2} \end{pmatrix} \begin{pmatrix} \theta_1 \\ \theta_2 \end{pmatrix}
$$

### Solution

$$
\theta_1 = \frac{\mu_1 - r}{\sigma_1}
$$

$$
\theta_2 = \frac{(\mu_2 - r) - \sigma_2\rho\theta_1}{\sigma_2\sqrt{1-\rho^2}}
$$

### Uniqueness

If the volatility matrix has full rank (2 assets, 2 Brownian motions), $\boldsymbol{\theta}$ is **unique** and the market is **complete**.

---

## Example 4: Incomplete Market (Stochastic Volatility)

### Heston Model Dynamics

$$
\begin{cases}
dS_t = \mu S_t\,dt + \sqrt{V_t}S_t\,dW_t^{1,\mathbb{P}} \\
dV_t = \kappa(\bar{V} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{P}}
\end{cases}
$$

with $\text{Corr}(dW^1, dW^2) = \rho$.

### The Problem

Two sources of randomness ($W^1, W^2$) but only one traded asset ($S$).

The market price of risk for $W^1$ is determined:

$$
\theta_1 = \frac{\mu - r}{\sqrt{V_t}}
$$

But $\theta_2$ (the **volatility risk premium**) is **not determined** by no-arbitrage alone.

### Multiple Risk-Neutral Measures

Any choice of $\theta_2(t, V_t)$ satisfying integrability conditions gives a valid risk-neutral measure.

**Common choices**:
- $\theta_2 = 0$ (no volatility risk premium)
- $\theta_2 = \lambda\sqrt{V_t}$ (proportional to volatility)

### Implication

Different choices of $\theta_2$ give different option prices. The market is **incomplete**.

---

## Example 5: Foreign Exchange

### Domestic Perspective

Under $\mathbb{P}$:

$$
dX_t = (\mu_X)X_t\,dt + \sigma_X X_t\,dW_t^{\mathbb{P}}
$$

where $X_t$ is the exchange rate (domestic per foreign).

### No-Arbitrage Condition

To prevent FX arbitrage:

$$
\mu_X = r_d - r_f
$$

where $r_d$ is domestic rate, $r_f$ is foreign rate.

### Market Price of Risk

$$
\theta = \frac{\mu_X - (r_d - r_f)}{\sigma_X} = 0
$$

No measure change needed! The FX market is already "risk-neutral" with respect to interest rate differentials.

### Risk-Neutral Dynamics

$$
dX_t = (r_d - r_f)X_t\,dt + \sigma_X X_t\,dW_t^{\mathbb{Q}}
$$

---

## Example 6: Vasicek Interest Rate Model

### Physical Dynamics

$$
dr_t = \kappa(\bar{r} - r_t)\,dt + \sigma\,dW_t^{\mathbb{P}}
$$

### Market Price of Risk

For interest rate models, $\theta$ is typically specified exogenously:

$$
\theta_t = \lambda \quad \text{(constant)}
$$

or

$$
\theta_t = \frac{\lambda}{\sigma}r_t \quad \text{(proportional to rate)}
$$

### Risk-Neutral Dynamics

$$
dr_t = \kappa(\bar{r} - r_t)\,dt + \sigma(dW_t^{\mathbb{Q}} - \theta\,dt)
$$

$$
= [\kappa(\bar{r} - r_t) - \sigma\theta]\,dt + \sigma\,dW_t^{\mathbb{Q}}
$$

$$
= \kappa^*(\bar{r}^* - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}
$$

where $\kappa^* = \kappa$ and $\bar{r}^* = \bar{r} - \sigma\theta/\kappa$.

### Bond Pricing

Under $\mathbb{Q}$:

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_t^T r_s\,ds} \;\middle|\; r_t\right]
$$

For Vasicek, this has closed form:

$$
P(t,T) = A(t,T)e^{-B(t,T)r_t}
$$

---

## Summary Table

| Model | # Assets | # BMs | Complete? | $\theta$ Unique? |
|-------|----------|-------|-----------|------------------|
| Black-Scholes | 1 | 1 | Yes | Yes |
| Multi-stock | $n$ | $n$ | Yes | Yes |
| Stoch. vol. | 1 | 2 | No | No |
| FX | 1 | 1 | Yes | Yes |
| Interest rate | 0 (bond) | 1 | No | No |

---

## Key Takeaways

1. **Complete markets**: $\theta$ is uniquely determined, one risk-neutral measure
2. **Incomplete markets**: Multiple valid $\theta$, multiple risk-neutral measures
3. **Calibration**: In practice, $\mathbb{Q}$ is inferred from market prices, not derived from $\mathbb{P}$
4. **Volatility unchanged**: Only drift changes under measure transformation

**The construction of $\mathbb{Q}$ is the mathematical foundation of derivative pricing.**
