# Examples: Constructing Risk-Neutral Measures

This section provides detailed worked examples of constructing the risk-neutral measure in various market models, from the basic Black-Scholes setting to multi-asset and interest rate models.

!!! abstract "Taxonomy: completeness and uniqueness"

    The relationship between the number of traded assets $n$ and the number of independent
    Brownian motions $d$ determines the market structure:

    - **Complete market** ($n = d$): the volatility matrix $\Sigma$ is square and invertible,
      so $\boldsymbol{\theta}$ is **unique** and $\mathbb{Q}$ is the **unique** risk-neutral measure.
    - **Incomplete market** ($n < d$): $\Sigma$ is underdetermined, leaving $d - n$ free
      parameters in $\boldsymbol{\theta}$ and a **family** of risk-neutral measures.
    - **Overdetermined** ($n > d$): the system is consistent only if no-arbitrage
      constraints are satisfied; otherwise arbitrage exists.

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

### Step 2: Define the Radon–Nikodym Derivative

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

The no-arbitrage condition implies that the Girsanov kernel is $\theta = 0$, so the domestic risk-neutral measure already produces the correct drift.

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
| Interest rate | Many (bonds) | 1 | Often incomplete (state not directly spanned) | No |

---

## Key Takeaways

Across all examples, the same structural pattern emerges: the number of traded assets
relative to the number of independent Brownian motions determines whether the
risk-neutral measure is unique.

1. **Complete markets** ($n = d$): $\boldsymbol{\theta}$ is uniquely determined, one risk-neutral measure.
2. **Incomplete markets** ($n < d$): multiple valid $\boldsymbol{\theta}$, multiple risk-neutral measures; the extra degrees of freedom correspond to unhedgeable risk factors.
3. **Calibration**: In practice, $\mathbb{Q}$ is inferred from market prices, not derived from $\mathbb{P}$.
4. **Volatility unchanged**: Only drift changes under measure transformation.

**The construction of $\mathbb{Q}$ is the mathematical foundation of derivative pricing.**

---

## Exercises

**Exercise 1.**
In the Black-Scholes model with $\mu = 0.15$, $r = 0.03$, and $\sigma = 0.30$, compute the market price of risk $\theta$ and the Radon–Nikodym derivative $Z_1$ for a specific path where $W_1^{\mathbb{P}} = -0.5$. Is this path upweighted or downweighted under $\mathbb{Q}$?

??? success "Solution to Exercise 1"
    With $\mu = 0.15$, $r = 0.03$, and $\sigma = 0.30$:

    $$
    \theta = \frac{\mu - r}{\sigma} = \frac{0.15 - 0.03}{0.30} = 0.40
    $$

    For the specific path with $W_1^{\mathbb{P}} = -0.5$ and $T = 1$:

    $$
    Z_1 = \exp\!\left(-\theta W_1^{\mathbb{P}} - \frac{1}{2}\theta^2 \cdot 1\right) = \exp\!\left(-0.40 \cdot (-0.5) - \frac{1}{2}(0.16)\right)
    $$

    $$
    = \exp(0.20 - 0.08) = \exp(0.12) \approx 1.1275
    $$

    Since $Z_1 > 1$, this path is **upweighted** under $\mathbb{Q}$. Intuitively, $W_1^{\mathbb{P}} = -0.5$ corresponds to a below-average stock return. The risk-neutral measure overweights adverse outcomes (and underweights favorable ones), reflecting the risk adjustment embedded in $\mathbb{Q}$.

---

**Exercise 2.**
A stock pays a continuous dividend yield $q = 0.02$ with $\mu = 0.08$, $\sigma = 0.20$, and $r = 0.05$. Verify that the market price of risk is the same as in the no-dividend case. Write the risk-neutral dynamics and check that the discounted reinvested-dividend process is a $\mathbb{Q}$-martingale.

??? success "Solution to Exercise 2"
    With dividends, the stock dynamics are $dS_t = (\mu - q)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}$. The discounted price for a dividend-paying stock must account for the reinvested dividends. Consider $\tilde{S}_t = e^{-rt}e^{qt}S_t \cdot e^{-qt} = e^{-rt}S_t$. More carefully, the total return from holding the stock includes dividends, so the relevant discounted process is $e^{-(r-q)t}S_t$ (or equivalently $e^{-rt}$ times the dividend-reinvested portfolio).

    The market price of risk is computed from the excess return of the total return process. Since the stock pays dividends at rate $q$, the total instantaneous return is $\mu\,dt + \sigma\,dW_t^{\mathbb{P}}$. The excess over $r$ divided by $\sigma$ gives:

    $$
    \theta = \frac{\mu - r}{\sigma} = \frac{0.08 - 0.05}{0.20} = 0.15
    $$

    This is the same as without dividends (where $\mu$ would be the total return). Under $\mathbb{Q}$:

    $$
    dS_t = (r - q)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
    $$

    The discounted reinvested-dividend process $\tilde{S}_t = e^{-(r-q)t}S_t$ satisfies:

    $$
    d\tilde{S}_t = \sigma\tilde{S}_t\,dW_t^{\mathbb{Q}}
    $$

    The drift vanishes, confirming $\tilde{S}_t$ is a $\mathbb{Q}$-martingale.

---

**Exercise 3.**
For the two correlated stocks model, take $\mu_1 = 0.12$, $\mu_2 = 0.08$, $r = 0.03$, $\sigma_1 = 0.25$, $\sigma_2 = 0.30$, and $\rho = 0.4$. Solve for $\theta_1$ and $\theta_2$. Verify your answer by checking that both excess returns $\mu_i - r$ are reproduced by $\Sigma\boldsymbol{\theta}$.

??? success "Solution to Exercise 3"
    Given $\mu_1 = 0.12$, $\mu_2 = 0.08$, $r = 0.03$, $\sigma_1 = 0.25$, $\sigma_2 = 0.30$, $\rho = 0.4$:

    From $\theta_1 = (\mu_1 - r)/\sigma_1$:

    $$
    \theta_1 = \frac{0.12 - 0.03}{0.25} = 0.36
    $$

    From $\theta_2 = [(\mu_2 - r) - \sigma_2\rho\theta_1]/(\sigma_2\sqrt{1 - \rho^2})$:

    $$
    \theta_2 = \frac{(0.08 - 0.03) - 0.30 \cdot 0.4 \cdot 0.36}{0.30\sqrt{1 - 0.16}} = \frac{0.05 - 0.0432}{0.30 \cdot \sqrt{0.84}}
    $$

    $$
    = \frac{0.0068}{0.30 \cdot 0.9165} = \frac{0.0068}{0.2750} \approx 0.0247
    $$

    **Verification:** The volatility matrix is $\Sigma = \begin{pmatrix} 0.25 & 0 \\ 0.30 \cdot 0.4 & 0.30\sqrt{0.84} \end{pmatrix} = \begin{pmatrix} 0.25 & 0 \\ 0.12 & 0.2750 \end{pmatrix}$.

    $$
    \Sigma\boldsymbol{\theta} = \begin{pmatrix} 0.25 \cdot 0.36 + 0 \cdot 0.0247 \\ 0.12 \cdot 0.36 + 0.2750 \cdot 0.0247 \end{pmatrix} = \begin{pmatrix} 0.09 \\ 0.0432 + 0.0068 \end{pmatrix} = \begin{pmatrix} 0.09 \\ 0.05 \end{pmatrix}
    $$

    This matches $\boldsymbol{\mu} - r\mathbf{1} = (0.09, 0.05)^{\top}$.

---

**Exercise 4.**
In the Heston stochastic volatility model, explain why the volatility risk premium $\theta_2$ cannot be determined by no-arbitrage. If one practitioner sets $\theta_2 = 0$ and another sets $\theta_2 = -0.5\sqrt{V_t}$, write the risk-neutral variance dynamics under each choice. Which choice produces a lower long-run mean of variance under $\mathbb{Q}$?

??? success "Solution to Exercise 4"
    In the Heston model, $dS_t = \mu S_t\,dt + \sqrt{V_t}S_t\,dW_t^{1,\mathbb{P}}$ and $dV_t = \kappa(\bar{V} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{P}}$. There are two Brownian motions but only one traded risky asset $S$. The no-arbitrage condition for $S$ determines $\theta_1 = (\mu - r)/\sqrt{V_t}$, but $\theta_2$ (associated with $W^2$) is unconstrained because no traded asset's return depends solely on $W^2$ in a way that pins down $\theta_2$. This is the hallmark of an incomplete market.

    Under $\mathbb{Q}$ with a general $\theta_2$, the variance dynamics become:

    $$
    dV_t = \kappa(\bar{V} - V_t)\,dt + \xi\sqrt{V_t}(dW_t^{2,\mathbb{Q}} - \theta_2\,dt)
    $$

    **Choice 1:** $\theta_2 = 0$:

    $$
    dV_t = \kappa(\bar{V} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{Q}}
    $$

    Long-run mean: $\bar{V}$.

    **Choice 2:** $\theta_2 = -0.5\sqrt{V_t}$:

    $$
    dV_t = [\kappa(\bar{V} - V_t) + 0.5\xi V_t]\,dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{Q}}
    $$

    $$
    = [(\kappa\bar{V}) - (\kappa - 0.5\xi)V_t]\,dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{Q}}
    $$

    This has the form $\kappa^*(\bar{V}^* - V_t)\,dt$ with $\kappa^* = \kappa - 0.5\xi$ and $\bar{V}^* = \kappa\bar{V}/(\kappa - 0.5\xi)$.

    Assuming $\kappa > 0.5\xi$ (so mean reversion is maintained), $\bar{V}^* = \kappa\bar{V}/(\kappa - 0.5\xi) > \bar{V}$. Therefore, **Choice 2 produces a higher long-run mean** of variance under $\mathbb{Q}$, and Choice 1 produces the lower long-run mean $\bar{V}$.

---

**Exercise 5.**
In the FX example, the no-arbitrage condition implies $\mu_X = r_d - r_f$. Derive this condition by requiring the domestic-currency value of a foreign money market investment to grow at rate $r_d$ under $\mathbb{Q}$. What happens to the market price of risk if $\mu_X \neq r_d - r_f$?

??? success "Solution to Exercise 5"
    The domestic-currency value of investing 1 unit of foreign currency in the foreign money market is $V_t = X_t e^{r_f t}$. By Itô's formula:

    $$
    dV_t = e^{r_f t}dX_t + r_f X_t e^{r_f t}\,dt = V_t\!\left(\frac{dX_t}{X_t} + r_f\,dt\right)
    $$

    Under $\mathbb{Q}$, this discounted process $\tilde{V}_t = e^{-r_d t}V_t$ must be a martingale:

    $$
    d\tilde{V}_t = \tilde{V}_t\!\left(\frac{dX_t}{X_t} + r_f\,dt - r_d\,dt\right)
    $$

    For the drift of $\tilde{V}_t$ to vanish, the drift of $dX_t/X_t$ must equal $r_d - r_f$:

    $$
    \mu_X = r_d - r_f
    $$

    If $\mu_X \neq r_d - r_f$, the market price of risk becomes

    $$
    \theta = \frac{\mu_X - (r_d - r_f)}{\sigma_X} \neq 0
    $$

    A Girsanov change of measure with this $\theta$ is required to construct $\mathbb{Q}$, and $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$ absorbs the deviation. Under $\mathbb{Q}$, the FX dynamics always become $dX_t = (r_d - r_f)X_t\,dt + \sigma_X X_t\,dW_t^{\mathbb{Q}}$.

---

**Exercise 6.**
In the Vasicek model with $\kappa = 0.5$, $\bar{r} = 0.04$, $\sigma = 0.01$, and constant market price of risk $\theta = 0.2$, compute $\bar{r}^* = \bar{r} - \sigma\theta/\kappa$. Using the risk-neutral dynamics, compute the zero-coupon bond price $P(0, T)$ for $T = 5$ with $r_0 = 0.03$.

??? success "Solution to Exercise 6"
    Given $\kappa = 0.5$, $\bar{r} = 0.04$, $\sigma = 0.01$, $\theta = 0.2$:

    $$
    \bar{r}^* = \bar{r} - \frac{\sigma\theta}{\kappa} = 0.04 - \frac{0.01 \cdot 0.2}{0.5} = 0.04 - 0.004 = 0.036
    $$

    Under $\mathbb{Q}$, the dynamics are $dr_t = \kappa(\bar{r}^* - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}}$ with $\kappa^* = \kappa = 0.5$ and $\bar{r}^* = 0.036$.

    For the Vasicek model, the bond price is $P(0,T) = A(0,T)e^{-B(0,T)r_0}$ where

    $$
    B(0,T) = \frac{1 - e^{-\kappa T}}{\kappa} = \frac{1 - e^{-0.5 \cdot 5}}{0.5} = \frac{1 - e^{-2.5}}{0.5} = \frac{1 - 0.08209}{0.5} = \frac{0.91791}{0.5} = 1.83583
    $$

    $$
    A(0,T) = \exp\!\left[\left(\bar{r}^* - \frac{\sigma^2}{2\kappa^2}\right)(B(0,T) - T) - \frac{\sigma^2}{4\kappa}B(0,T)^2\right]
    $$

    Computing: $\sigma^2/(2\kappa^2) = 0.0001/0.5 = 0.0002$ and $\sigma^2/(4\kappa) = 0.0001/2 = 0.00005$.

    $$
    A(0,5) = \exp\!\left[(0.036 - 0.0002)(1.83583 - 5) - 0.00005 \cdot (1.83583)^2\right]
    $$

    $$
    = \exp\!\left[0.0358 \cdot (-3.16417) - 0.00005 \cdot 3.37028\right]
    $$

    $$
    = \exp(-0.11328 - 0.00017) = \exp(-0.11345) \approx 0.89280
    $$

    Therefore:

    $$
    P(0,5) = 0.89280 \cdot e^{-1.83583 \cdot 0.03} = 0.89280 \cdot e^{-0.05507} = 0.89280 \cdot 0.94645 \approx 0.84498
    $$

---

**Exercise 7.**
Consider a market with 3 stocks and 2 Brownian motions. Write the system $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$ where $\Sigma$ is $3 \times 2$. This is an overdetermined system. State the condition for a solution to exist and interpret it as a no-arbitrage condition. If the condition is violated, construct a specific arbitrage strategy.

??? success "Solution to Exercise 7"
    With 3 stocks and 2 Brownian motions, each stock has dynamics $dS_t^i = \mu_i S_t^i\,dt + \sum_{j=1}^{2}\Sigma_{ij}S_t^i\,dW_t^{j,\mathbb{P}}$. The system is:

    $$
    \begin{pmatrix} \mu_1 - r \\ \mu_2 - r \\ \mu_3 - r \end{pmatrix} = \begin{pmatrix} \Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22} \\ \Sigma_{31} & \Sigma_{32} \end{pmatrix} \begin{pmatrix} \theta_1 \\ \theta_2 \end{pmatrix}
    $$

    This is an **overdetermined** system: 3 equations, 2 unknowns. A solution exists if and only if the vector $\boldsymbol{\mu} - r\mathbf{1}$ lies in the column space of $\Sigma$. Equivalently, $\boldsymbol{\mu} - r\mathbf{1}$ must be orthogonal to the left null space of $\Sigma$. If $\mathbf{n}$ spans the left null space (so $\mathbf{n}^{\top}\Sigma = 0$), the condition is:

    $$
    \mathbf{n}^{\top}(\boldsymbol{\mu} - r\mathbf{1}) = 0
    $$

    **No-arbitrage interpretation:** The vector $\mathbf{n}$ represents portfolio weights. The condition $\mathbf{n}^{\top}\Sigma = 0$ means this portfolio has zero exposure to both Brownian motions (zero volatility, hence risk-free). No-arbitrage then requires its expected return to equal $r$, i.e., $\mathbf{n}^{\top}\boldsymbol{\mu} = r(\mathbf{n}^{\top}\mathbf{1})$, which is $\mathbf{n}^{\top}(\boldsymbol{\mu} - r\mathbf{1}) = 0$.

    **Constructing arbitrage when violated:** If $\mathbf{n}^{\top}(\boldsymbol{\mu} - r\mathbf{1}) > 0$, hold the portfolio $\mathbf{n}$ (long/short the three stocks in proportions $n_1, n_2, n_3$) and finance it at rate $r$. The portfolio has zero volatility (deterministic returns) but earns more than $r$, producing a risk-free arbitrage profit.
