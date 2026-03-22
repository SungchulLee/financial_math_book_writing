# Optimal Execution

**Optimal execution** addresses the fundamental problem of liquidating (or acquiring) a large position while minimizing execution costs. The **Almgren-Chriss framework** balances the trade-off between **market impact** (trading too fast) and **timing risk** (trading too slow), yielding closed-form optimal trajectories that interpolate between aggressive and passive execution.

---

## The Execution Problem

### Setup

An investor holds $X$ shares of a stock and must liquidate the position over a time horizon $[0, T]$. Let:

- $x(t)$ = shares remaining at time $t$, with $x(0) = X$ and $x(T) = 0$
- $v(t) = -\dot{x}(t)$ = trading rate (shares sold per unit time)
- $S_t$ = unaffected stock price (without the trader's impact)

The execution generates cash, but trading moves the price against the investor. The goal is to choose the trajectory $x(\cdot)$ to minimize a risk-adjusted cost criterion.

---

## Market Impact Model

### Permanent Impact

Each trade permanently shifts the equilibrium price:

$$
S_t^{\text{permanent}} = S_0 - \gamma \int_0^t v(s) \, ds = S_0 + \gamma (x(t) - X)
$$

where $\gamma > 0$ is the permanent impact coefficient (price change per share traded). Permanent impact reflects the **information content** of trading.

### Temporary Impact

Execution also incurs a **temporary** price concession that affects only the current trade:

$$
S_t^{\text{execution}} = S_t^{\text{permanent}} - \eta \, v(t)
$$

where $\eta > 0$ is the temporary impact coefficient. Temporary impact reflects the **liquidity cost** of demanding immediacy.

### Unaffected Price Dynamics

The unaffected price follows arithmetic Brownian motion:

$$
dS_t = \sigma \, dW_t
$$

where $\sigma$ is the stock's volatility. (The drift is omitted as it does not affect the optimal strategy over short horizons.)

---

## Execution Cost

### Implementation Shortfall

The **implementation shortfall** is the difference between the theoretical (paper) value and the actual cash received:

$$
C = X \cdot S_0 - \int_0^T v(t) \cdot S_t^{\text{execution}} \, dt
$$

Substituting the impact model:

$$
C = \underbrace{\gamma X^2 / 2}_{\text{permanent impact}} + \underbrace{\eta \int_0^T v(t)^2 \, dt}_{\text{temporary impact}} + \underbrace{\sigma \int_0^T x(t) \, dW_t}_{\text{timing risk}}
$$

**Decomposition:**

- **Permanent impact cost** $\gamma X^2 / 2$: Independent of execution strategy (unavoidable)
- **Temporary impact cost** $\eta \int_0^T v(t)^2 \, dt$: Depends on the trading rate schedule
- **Timing risk**: Random component from price movements during execution

---

## Mean-Variance Optimization

### Objective

The Almgren-Chriss objective minimizes a **mean-variance criterion**:

$$
\min_{x(\cdot)} \left\{\mathbb{E}[C] + \lambda \, \text{Var}[C]\right\}
$$

subject to $x(0) = X$ and $x(T) = 0$, where $\lambda \ge 0$ is the risk aversion parameter.

### Expected Cost and Variance

$$
\mathbb{E}[C] = \frac{\gamma X^2}{2} + \eta \int_0^T v(t)^2 \, dt
$$

$$
\text{Var}[C] = \sigma^2 \int_0^T x(t)^2 \, dt
$$

The objective becomes:

$$
\min_{x(\cdot)} \left\{\eta \int_0^T \dot{x}(t)^2 \, dt + \lambda \sigma^2 \int_0^T x(t)^2 \, dt\right\}
$$

(dropping the constant $\gamma X^2 / 2$).

---

## Optimal Trading Trajectory

### Euler-Lagrange Equation

The variational problem yields the Euler-Lagrange equation:

$$
\eta \, \ddot{x}(t) = \lambda \sigma^2 x(t)
$$

with boundary conditions $x(0) = X$ and $x(T) = 0$.

### Solution

!!! info "Theorem (Almgren-Chriss Optimal Trajectory)"
    The optimal liquidation trajectory is:

    $$
    x^*(t) = X \cdot \frac{\sinh(\kappa(T - t))}{\sinh(\kappa T)}
    $$

    where the **urgency parameter** is:

    $$
    \kappa = \sqrt{\frac{\lambda \sigma^2}{\eta}}
    $$

The optimal trading rate is:

$$
v^*(t) = -\dot{x}^*(t) = X \kappa \cdot \frac{\cosh(\kappa(T - t))}{\sinh(\kappa T)}
$$

### Interpretation of the Urgency Parameter

The parameter $\kappa$ controls the **aggressiveness** of execution:

- $\kappa$ is large when risk aversion $\lambda$ is high or volatility $\sigma$ is high (relative to temporary impact $\eta$)
- $\kappa$ is small when temporary impact $\eta$ is high (relative to risk costs)

---

## Limiting Cases

### Risk-Neutral Limit (TWAP)

As $\lambda \to 0$ (or equivalently $\kappa \to 0$), the urgency vanishes and the optimal trajectory becomes **linear**:

$$
x^*(t) \to X \cdot \frac{T - t}{T}, \quad v^*(t) \to \frac{X}{T}
$$

This is the **Time-Weighted Average Price (TWAP)** strategy: sell at a constant rate.

### Highly Risk-Averse Limit

As $\lambda \to \infty$ (or $\kappa \to \infty$), the trajectory concentrates execution at $t = 0$:

$$
x^*(t) \to X \cdot e^{-\kappa t} \quad (\text{approximately})
$$

The investor liquidates as fast as possible to eliminate timing risk, accepting high temporary impact costs.

### VWAP Strategy

The **Volume-Weighted Average Price (VWAP)** strategy trades proportionally to expected market volume:

$$
v^{\text{VWAP}}(t) = \frac{X \cdot \text{Vol}(t)}{\int_0^T \text{Vol}(s) \, ds}
$$

where $\text{Vol}(t)$ is the expected market volume at time $t$. VWAP is not generally optimal in the Almgren-Chriss sense but minimizes participation rate and market visibility.

---

## Optimal Expected Cost

The minimum expected cost (excluding the unavoidable permanent impact) is:

$$
\mathbb{E}[C^*] = \frac{\gamma X^2}{2} + \eta X^2 \frac{\kappa}{\tanh(\kappa T)}
$$

The variance of the optimal cost is:

$$
\text{Var}[C^*] = \frac{\sigma^2 X^2}{2\kappa} \left(\frac{1}{\tanh(\kappa T)} - \frac{\kappa T}{\sinh^2(\kappa T)}\right)
$$

The **efficient frontier** traces the trade-off between $\mathbb{E}[C^*]$ and $\sqrt{\text{Var}[C^*]}$ as $\lambda$ varies:

- At $\lambda = 0$: minimum expected cost (TWAP), maximum variance
- At $\lambda = \infty$: minimum variance (immediate execution), maximum expected cost

---

## The Square-Root Impact Law

### Empirical Evidence

Extensive empirical studies show that aggregate market impact follows the **square-root law**:

$$
\Delta P \approx \sigma \cdot \sqrt{\frac{Q}{V}}
$$

where $Q$ is the total order size, $V$ is the daily volume, and $\sigma$ is daily volatility.

This implies:

- Impact is **concave** in order size (doubling the order does not double the impact)
- Impact scales with volatility
- Impact is inversely related to liquidity (volume)

### Decomposition

The total market impact decomposes as:

$$
\text{Total Impact} = \underbrace{\gamma \cdot Q}_{\text{permanent}} + \underbrace{\eta \cdot Q / T}_{\text{temporary (amortized)}}
$$

Empirical estimates typically find $\gamma \approx 0.1 \sigma / V$ and $\eta \approx 0.01 \sigma \sqrt{V}$ for liquid equities.

---

## Discrete-Time Formulation

### Setup

Divide $[0, T]$ into $N$ periods. Let $n_k$ be shares sold in period $k$, with $\sum_{k=1}^N n_k = X$.

**Execution cost:**

$$
C = \gamma \sum_{k=1}^N n_k \left(X - \sum_{j=1}^k n_j + \frac{n_k}{2}\right) + \eta \sum_{k=1}^N \frac{n_k^2}{\tau} + \sigma \sqrt{\tau} \sum_{k=1}^N x_k \epsilon_k
$$

where $\tau = T/N$, $x_k = X - \sum_{j=1}^k n_j$ is the remaining position, and $\epsilon_k \sim N(0,1)$.

### Optimal Discrete Strategy

The optimal sell quantities satisfy the recurrence:

$$
n_k^* = x_{k-1} \cdot \frac{\sinh(\kappa \tau)}{\sinh(\kappa(N-k+1)\tau)}
$$

which discretizes the continuous solution.

---

## Extensions

### Stochastic Liquidity

If temporary impact varies stochastically, $\eta_t = \eta(t, \omega)$, the optimal strategy adapts:

$$
v^*(t) \propto \frac{1}{\eta_t} \cdot x^*(t)
$$

Trade faster when liquidity is good (low $\eta_t$) and slower when liquidity is poor.

### Predictive Signals (Alpha)

If the trader has a predictive signal $\alpha_t$ for future returns:

$$
\min_{x(\cdot)} \left\{\mathbb{E}[C] - \int_0^T \alpha_t \cdot x(t) \, dt + \lambda \, \text{Var}[C]\right\}
$$

The optimal trajectory tilts execution toward times when the signal is favorable, accelerating or delaying trades to capture alpha.

### Multi-Asset Execution

For a portfolio of $d$ assets with cross-impact matrix $\boldsymbol{\eta}$:

$$
\min_{\mathbf{x}(\cdot)} \left\{\int_0^T \dot{\mathbf{x}}^\top \boldsymbol{\eta} \, \dot{\mathbf{x}} \, dt + \lambda \int_0^T \mathbf{x}^\top \boldsymbol{\Sigma} \, \mathbf{x} \, dt\right\}
$$

The solution involves matrix exponentials and eigendecomposition of $\boldsymbol{\eta}^{-1} \boldsymbol{\Sigma}$.

---

## Example: Liquidating 100,000 Shares

**Parameters:**

- $X = 100{,}000$ shares, $S_0 = \$50$
- $T = 1$ day (6.5 hours = 390 minutes)
- $\sigma = \$0.50$ (daily volatility)
- $\eta = 0.001$ \$/share/share (temporary impact)
- $\gamma = 0.0001$ \$/share (permanent impact)
- $\lambda = 10^{-6}$ (risk aversion)

**Urgency parameter:**

$$
\kappa = \sqrt{\frac{10^{-6} \times 0.25}{0.001}} = \sqrt{0.00025} \approx 0.0158 \text{ min}^{-1}
$$

$$
\kappa T = 0.0158 \times 390 \approx 6.16
$$

Since $\kappa T \gg 1$, the strategy is moderately front-loaded.

**Expected cost:**

$$
\mathbb{E}[C^*] \approx \frac{0.0001 \times 10^{10}}{2} + 0.001 \times 10^{10} \times \frac{0.0158}{1.0} \approx \$500{,}000 + \$158{,}000 = \$658{,}000
$$

representing about 13 bps of the \$5M position value.

---

## Key Takeaways

- The Almgren-Chriss framework optimizes the mean-variance trade-off between market impact (temporary + permanent) and timing risk
- The optimal trajectory $x^*(t) = X \cdot \sinh(\kappa(T-t)) / \sinh(\kappa T)$ interpolates between TWAP ($\kappa \to 0$) and immediate execution ($\kappa \to \infty$)
- The urgency parameter $\kappa = \sqrt{\lambda \sigma^2 / \eta}$ increases with risk aversion and volatility, decreases with temporary impact
- Implementation shortfall decomposes into unavoidable permanent impact plus strategy-dependent temporary impact and timing risk
- The square-root law $\Delta P \sim \sigma \sqrt{Q/V}$ governs empirical market impact
- Extensions to stochastic liquidity, alpha signals, and multi-asset portfolios enrich the framework for practical use

---

## Further Reading

- Almgren, R. & Chriss, N. (2001), "Optimal Execution of Portfolio Transactions," *Journal of Risk*
- Almgren, R. (2003), "Optimal Execution with Nonlinear Impact Functions and Trading-Enhanced Risk"
- Gatheral, J., Schied, A., & Slynko, A. (2012), "Transient Linear Price Impact and Fredholm Integral Equations"
- Cartea, A., Jaimungal, S., & Penalva, J. (2015), *Algorithmic and High-Frequency Trading*
- Bouchaud, J.-P., Farmer, J.D., & Lillo, F. (2009), "How Markets Slowly Digest Changes in Supply and Demand"
