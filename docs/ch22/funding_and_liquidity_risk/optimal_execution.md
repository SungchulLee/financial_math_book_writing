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

Recall (see [§ Market Impact](market_impact.md)) for the empirical square-root law $\Delta P \approx \sigma\sqrt{Q/V}$, its concavity in order size, the permanent/temporary decomposition $\gamma Q + \eta Q/T$, and typical empirical coefficient estimates. See also [§ Market Impact and Feedback Effects](../../ch24/market_impact_and_feedback_effects/algorithmic_trading_mean_field_games.md) for cross-asset and feedback extensions.

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

---

## Exercises

**Exercise 1.** In the Almgren-Chriss model, the trader minimizes $\mathbb{E}[\text{Cost}] + \lambda\,\text{Var}[\text{Cost}]$ over execution trajectories. Explain the trade-off: increasing the execution speed reduces timing risk (variance) but increases market impact (expected cost). What does the risk aversion parameter $\lambda$ control?

??? success "Solution to Exercise 1"
    **The mean-variance trade-off in optimal execution.**

    In the Almgren-Chriss framework, the execution cost decomposes as:

    $$
    C = \underbrace{\frac{\gamma X^2}{2}}_{\text{permanent (fixed)}} + \underbrace{\eta \int_0^T v(t)^2 \, dt}_{\text{temporary impact}} + \underbrace{\sigma \int_0^T x(t) \, dW_t}_{\text{timing risk}}
    $$

    The optimization objective is:

    $$
    \min_{x(\cdot)} \left\{\mathbb{E}[C] + \lambda \, \text{Var}[C]\right\}
    $$

    **The trade-off:**

    - **Executing faster** (higher trading rate $v(t)$, shorter effective duration):
        - **Reduces timing risk:** The variance $\text{Var}[C] = \sigma^2 \int_0^T x(t)^2 \, dt$ is smaller because the remaining position $x(t)$ drops to zero quickly, reducing exposure to random price movements.
        - **Increases expected cost:** The temporary impact cost $\eta \int_0^T v(t)^2 \, dt$ is larger because the convexity of $v^2$ penalizes high trading rates.

    - **Executing slower** (lower trading rate, spreading over the full horizon):
        - **Reduces expected cost:** The temporary impact cost is minimized by trading at a uniform rate (TWAP), which minimizes $\int v^2 \, dt$ for a given total quantity.
        - **Increases timing risk:** The position remains large for longer, so $\int x(t)^2 \, dt$ is larger, and the portfolio is exposed to more cumulative price risk.

    **What $\lambda$ controls:**

    The risk aversion parameter $\lambda \ge 0$ determines how the trader values the reduction in variance relative to the increase in expected cost:

    - **$\lambda = 0$ (risk-neutral):** The trader cares only about expected cost. The optimal strategy is TWAP -- trade at a constant rate to minimize $\int v^2 \, dt$. Timing risk is completely ignored.
    - **$\lambda$ small:** The trader is slightly risk-averse. The optimal strategy is close to TWAP but slightly front-loaded -- trading a bit faster at the beginning to reduce exposure.
    - **$\lambda$ large:** The trader strongly penalizes variance. The strategy becomes aggressive, liquidating most of the position early to eliminate timing risk, even at the cost of higher temporary impact.
    - **$\lambda \to \infty$:** The trader liquidates immediately (block trade), accepting maximum temporary impact to achieve zero timing risk.

    The urgency parameter $\kappa = \sqrt{\lambda \sigma^2 / \eta}$ encapsulates this trade-off in a single number: it increases with risk aversion $\lambda$ and volatility $\sigma$ (favoring speed) and decreases with temporary impact $\eta$ (favoring patience).

---

**Exercise 2.** A trader must sell $X_0 = 100{,}000$ shares over $T = 5$ days. Under the linear impact model with permanent impact $\gamma = 0.0002$ \$/share and temporary impact $\eta = 0.001$ \$/share, and risk aversion $\lambda = 10^{-6}$, describe the shape of the optimal trading trajectory. Is it front-loaded (aggressive) or back-loaded (passive)?

??? success "Solution to Exercise 2"
    **Shape of the optimal trading trajectory.**

    **Given parameters:**

    - $X_0 = 100{,}000$ shares
    - $T = 5$ days
    - $\gamma = 0.0002$ \$/share (permanent impact)
    - $\eta = 0.001$ \$/share (temporary impact)
    - $\lambda = 10^{-6}$ (risk aversion)

    To determine the shape, we need the urgency parameter. We also need $\sigma$. Since the problem does not specify volatility, let us use a typical value, say $\sigma = \$0.50$ per day (corresponding to about 1% daily volatility for a \$50 stock).

    **Urgency parameter:**

    $$
    \kappa = \sqrt{\frac{\lambda \sigma^2}{\eta}} = \sqrt{\frac{10^{-6} \times 0.25}{0.001}} = \sqrt{\frac{2.5 \times 10^{-7}}{10^{-3}}} = \sqrt{2.5 \times 10^{-4}} \approx 0.0158 \text{ day}^{-1}
    $$

    $$
    \kappa T = 0.0158 \times 5 = 0.079
    $$

    **Interpretation of $\kappa T$:**

    Since $\kappa T = 0.079 \ll 1$, this is close to the risk-neutral limit. The optimal trajectory is:

    $$
    x^*(t) = X \cdot \frac{\sinh(\kappa(T-t))}{\sinh(\kappa T)}
    $$

    For small $\kappa T$, $\sinh(\kappa(T-t)) \approx \kappa(T-t)$ and $\sinh(\kappa T) \approx \kappa T$, so:

    $$
    x^*(t) \approx X \cdot \frac{T - t}{T}
    $$

    This is approximately a **TWAP strategy** (linear trajectory, constant trading rate).

    **The strategy is essentially uniform, with a very slight front-loading.** Since $\kappa T$ is small, risk aversion has minimal effect. The trader should sell approximately 20,000 shares per day over the 5-day window.

    The slight front-loading can be seen by comparing the trading rate at $t = 0$ versus $t = T$:

    $$
    \frac{v^*(0)}{v^*(T)} = \frac{\cosh(\kappa T)}{\cosh(0)} = \cosh(0.079) \approx 1.003
    $$

    The initial trading rate is only 0.3% higher than the final rate -- virtually uniform.

    If the volatility were higher (say $\sigma = \$2$) or risk aversion were larger ($\lambda = 10^{-4}$), then $\kappa T$ would be larger and the strategy would become visibly front-loaded (aggressive).

---

**Exercise 3.** Show that in the risk-neutral case ($\lambda = 0$), the Almgren-Chriss optimal trajectory is a TWAP (Time-Weighted Average Price) strategy that trades at a constant rate. Derive this result from the first-order optimality conditions.

??? success "Solution to Exercise 3"
    **Derivation of the TWAP result for $\lambda = 0$.**

    When $\lambda = 0$ (risk-neutral), the trader minimizes only the expected cost:

    $$
    \min_{x(\cdot)} \mathbb{E}[C] = \min_{x(\cdot)} \left\{\frac{\gamma X^2}{2} + \eta \int_0^T v(t)^2 \, dt\right\}
    $$

    Since $\gamma X^2/2$ is constant (independent of the strategy), this reduces to:

    $$
    \min_{x(\cdot)} \int_0^T v(t)^2 \, dt \quad \text{subject to} \quad \int_0^T v(t) \, dt = X
    $$

    where $v(t) = -\dot{x}(t) \ge 0$ is the selling rate and the constraint ensures full liquidation.

    **First-order conditions via calculus of variations:**

    Form the Lagrangian:

    $$
    \mathcal{L} = \int_0^T v(t)^2 \, dt - \mu \left(\int_0^T v(t) \, dt - X\right)
    $$

    Taking the functional derivative with respect to $v(t)$:

    $$
    \frac{\delta \mathcal{L}}{\delta v(t)} = 2v(t) - \mu = 0
    $$

    This gives:

    $$
    v^*(t) = \frac{\mu}{2} = \text{constant}
    $$

    The constant trading rate is determined by the constraint:

    $$
    \int_0^T v^*(t) \, dt = v^* \cdot T = X \implies v^* = \frac{X}{T}
    $$

    Therefore:

    $$
    v^*(t) = \frac{X}{T} \quad \text{for all } t \in [0, T]
    $$

    and the remaining position is:

    $$
    x^*(t) = X - \int_0^t v^*(s) \, ds = X\left(1 - \frac{t}{T}\right)
    $$

    This is the **TWAP strategy**: sell at a constant rate $X/T$ shares per unit time.

    **Verification via the Euler-Lagrange equation:**

    Alternatively, the Euler-Lagrange equation for the Almgren-Chriss problem is:

    $$
    \eta \ddot{x}(t) = \lambda \sigma^2 x(t)
    $$

    Setting $\lambda = 0$:

    $$
    \ddot{x}(t) = 0
    $$

    The general solution is $x(t) = At + B$. Applying boundary conditions $x(0) = X$ and $x(T) = 0$:

    $$
    B = X, \quad A = -\frac{X}{T}
    $$

    $$
    x^*(t) = X\left(1 - \frac{t}{T}\right)
    $$

    This confirms the TWAP result. The optimality follows from the convexity of $v \mapsto v^2$: by Jensen's inequality, uniform trading minimizes $\int v^2 \, dt$ subject to a fixed total $\int v \, dt = X$.

---

**Exercise 4.** In the presence of only temporary impact (no permanent impact, $\gamma = 0$), the total execution cost depends on the sum of squared trading rates $\sum v_k^2$. Show that the minimum-cost strategy is uniform trading (TWAP). How does adding permanent impact change the optimal strategy?

??? success "Solution to Exercise 4"
    **Minimum-cost strategy with temporary impact only.**

    **Part 1: With only temporary impact ($\gamma = 0$).**

    The total execution cost is:

    $$
    C = \eta \sum_{k=1}^{N} v_k^2 \cdot \tau
    $$

    where $v_k = n_k / \tau$ is the trading rate in period $k$, $n_k$ is shares sold in period $k$, and $\tau = T/N$.

    Equivalently:

    $$
    C = \frac{\eta}{\tau} \sum_{k=1}^{N} n_k^2 \quad \text{subject to} \quad \sum_{k=1}^{N} n_k = X
    $$

    To minimize $\sum n_k^2$ subject to $\sum n_k = X$, we use the Lagrange multiplier method or invoke the **Cauchy-Schwarz inequality**:

    $$
    \left(\sum_{k=1}^N n_k\right)^2 \le N \sum_{k=1}^N n_k^2
    $$

    with equality if and only if $n_1 = n_2 = \cdots = n_N$.

    Therefore the minimum is achieved by uniform trading:

    $$
    n_k^* = \frac{X}{N} \quad \text{for all } k
    $$

    This is the **TWAP strategy**.

    The minimum cost is:

    $$
    C^* = \frac{\eta}{\tau} \cdot N \cdot \left(\frac{X}{N}\right)^2 = \frac{\eta X^2}{N\tau} = \frac{\eta X^2}{T}
    $$

    **Part 2: How permanent impact changes the optimal strategy.**

    When permanent impact $\gamma > 0$ is included, the cost becomes:

    $$
    C = \frac{\gamma X^2}{2} + \frac{\eta}{\tau} \sum_{k=1}^N n_k^2
    $$

    The permanent impact cost $\gamma X^2/2$ is independent of the strategy (it depends only on the total quantity $X$, not on how the liquidation is split). Therefore, adding permanent impact does **not** change the expected-cost-minimizing strategy: TWAP is still optimal for minimizing $\mathbb{E}[C]$.

    However, when we include **risk aversion** ($\lambda > 0$), permanent impact matters indirectly. The risk term is:

    $$
    \text{Var}[C] = \sigma^2 \tau \sum_{k=1}^N x_k^2
    $$

    where $x_k$ is the remaining position. Minimizing $\mathbb{E}[C] + \lambda \text{Var}[C]$ now involves a trade-off:

    - The temporary impact term $\sum n_k^2$ favors uniform trading.
    - The variance term $\sum x_k^2$ favors front-loaded trading (reducing $x_k$ quickly).

    The permanent impact term remains fixed and does not affect the optimization. The optimal strategy is the Almgren-Chriss $\sinh$ trajectory, which front-loads execution relative to TWAP. The degree of front-loading depends on $\kappa = \sqrt{\lambda \sigma^2 / \eta}$: higher $\kappa$ means more aggressive (front-loaded) execution.

---

**Exercise 5.** A VWAP (Volume-Weighted Average Price) strategy trades proportionally to historical volume patterns. Compare VWAP with the Almgren-Chriss optimal trajectory. Under what market conditions does VWAP perform well? When does it perform poorly?

??? success "Solution to Exercise 5"
    **VWAP versus Almgren-Chriss optimal trajectory.**

    **VWAP strategy:**

    The VWAP strategy trades proportionally to expected market volume:

    $$
    v^{\text{VWAP}}(t) = \frac{X \cdot \text{Vol}(t)}{\int_0^T \text{Vol}(s)\,ds}
    $$

    where $\text{Vol}(t)$ is the expected market volume at time $t$ (typically exhibiting a U-shaped intraday pattern: high volume at the open and close, lower during midday).

    **Almgren-Chriss optimal trajectory:**

    $$
    v^{\text{AC}}(t) = X\kappa \cdot \frac{\cosh(\kappa(T-t))}{\sinh(\kappa T)}
    $$

    This depends on risk aversion, volatility, and impact parameters, but not on volume patterns.

    **Comparison:**

    | Feature | VWAP | Almgren-Chriss |
    |---|---|---|
    | **Objective** | Match average market price | Minimize risk-adjusted cost |
    | **Volume adaptation** | Yes (trades with volume) | No (fixed trajectory) |
    | **Risk aversion** | Implicit (low impact) | Explicit (parameter $\lambda$) |
    | **Urgency** | None | Controlled by $\kappa$ |
    | **Information leakage** | Low (blends with market) | Potentially higher (front-loaded) |
    | **Benchmark** | VWAP price | Arrival price |

    **When VWAP performs well:**

    1. **Low urgency trades:** When there is no time pressure and the trader simply wants to achieve a fair average price with minimal market impact. VWAP's low participation rate minimizes signaling to the market.

    2. **Stable markets:** When volatility is low and predictable, timing risk is small, so the risk-aversion component of Almgren-Chriss offers little advantage.

    3. **Volume is predictable:** VWAP relies on historical volume patterns. When intraday volume is stable and predictable (typical for large-cap liquid equities), VWAP achieves low participation rates throughout the day.

    4. **Benchmark matching:** When the trader's performance is measured against the VWAP benchmark (common for asset managers executing client orders), VWAP directly minimizes tracking error against the benchmark.

    **When VWAP performs poorly:**

    1. **Urgent liquidations:** When risk aversion is high (e.g., unwinding a losing position), VWAP's lack of urgency is suboptimal. Almgren-Chriss front-loads execution to reduce risk.

    2. **Volatile markets:** When $\sigma$ is large, timing risk dominates. VWAP ignores this risk entirely, while Almgren-Chriss optimally trades it off against impact.

    3. **Volume is unpredictable:** If actual volume deviates significantly from the historical pattern (e.g., due to news events), VWAP participation rates become uneven, potentially leading to high impact during low-volume periods.

    4. **Information-driven trades:** If the trader has a directional view (alpha signal), VWAP does not exploit it. Almgren-Chriss with alpha tilts execution to capture the signal.

    5. **Large position relative to volume:** If $X/V$ is large, VWAP may result in very high participation rates during low-volume periods, creating excessive impact. Almgren-Chriss (or participation-rate-constrained variants) handles this more gracefully.

    In practice, many execution algorithms combine elements of both: they use VWAP-like volume profiling to minimize market visibility while incorporating urgency adjustments inspired by Almgren-Chriss to manage timing risk.

---

**Exercise 6.** The Almgren-Chriss model assumes that the stock price follows arithmetic Brownian motion with constant volatility. Discuss the limitations of this assumption. How would mean-reverting prices, time-varying volatility, or non-linear impact functions change the optimal execution strategy?

??? success "Solution to Exercise 6"
    **Limitations of the Almgren-Chriss assumptions and extensions.**

    The Almgren-Chriss model assumes arithmetic Brownian motion with constant volatility: $dS_t = \sigma \, dW_t$, with linear permanent and temporary impact functions. Each assumption has limitations and consequences for the optimal strategy.

    **Limitation 1: Arithmetic Brownian motion (ABM).**

    ABM allows negative prices and has constant absolute (not relative) volatility. For short execution horizons (minutes to hours), ABM is a reasonable approximation. For longer horizons (days to weeks), geometric Brownian motion (GBM) is more appropriate:

    $$
    dS_t = \mu S_t \, dt + \sigma S_t \, dW_t
    $$

    Under GBM, the optimal strategy must account for the drift $\mu$ and the multiplicative structure. If $\mu < 0$ (expected price decline), the trader should accelerate execution; if $\mu > 0$, delay may be beneficial. The ABM model with zero drift ignores this asymmetry.

    **Limitation 2: Constant volatility.**

    In reality, volatility exhibits:

    - **Intraday patterns:** Volatility is typically higher at market open and close (U-shaped pattern).
    - **Stochastic variation:** Volatility changes randomly, often clustering (GARCH effects).
    - **Regime dependence:** Stress periods have much higher volatility.

    **Effect on optimal strategy:** If volatility is time-varying but predictable, the Euler-Lagrange equation becomes:

    $$
    \eta \ddot{x}(t) = \lambda \sigma(t)^2 x(t)
    $$

    The optimal strategy trades faster during high-volatility periods (to reduce timing risk when it is greatest) and slower during low-volatility periods (when the cost of waiting is low). For stochastic volatility, the optimal strategy becomes adaptive: monitor realized volatility in real time and adjust the trading rate accordingly.

    **Limitation 3: Mean-reverting prices.**

    If prices exhibit mean reversion (temporary price dislocations that revert):

    $$
    dS_t = \theta(\bar{S} - S_t) \, dt + \sigma \, dW_t
    $$

    the optimal execution strategy changes qualitatively. If the current price is above the long-run mean ($S_t > \bar{S}$), the seller should accelerate execution to exploit the favorable price. If the price is below the mean, patience is rewarded because the price is expected to recover.

    Formally, the urgency to sell increases when the price is high and decreases when the price is low. This creates an **adaptive** strategy that conditions on the current price level, unlike the predetermined Almgren-Chriss trajectory.

    Mean reversion also reduces timing risk (prices don't wander as far), so the variance penalty is smaller, and the overall optimal strategy is closer to TWAP than in the ABM case.

    **Limitation 4: Non-linear impact functions.**

    The Almgren-Chriss model assumes linear impact: $g(v) = \gamma v$ and $h(v) = \eta v$. Empirical evidence suggests:

    - **Concave temporary impact:** $h(v) = \eta |v|^{\delta}$ with $\delta \approx 0.5$ (square-root law). This means the cost of trading fast increases less than linearly -- the marginal impact of additional speed decreases.

    - **Effect on optimal strategy:** With concave impact, the optimal strategy is **more front-loaded** than the linear case. Since the marginal cost of trading fast is lower, the optimizer exploits this by concentrating more trading early.

    - **Transient impact:** Some models (Obizhaeva-Wang 2013) allow temporary impact to decay gradually rather than instantaneously:

        $$
        S_t = S_0 - \gamma \int_0^t v(s)\,ds - \int_0^t \eta \, e^{-\rho(t-s)} v(s)\,ds + \sigma W_t
        $$

        where $\rho$ is the decay rate. When impact decays slowly, the trader should space trades further apart to allow the impact to dissipate, leading to a more spread-out trajectory.

    - **Non-linear permanent impact:** If permanent impact is concave ($g(v) = \gamma |v|^{\alpha}$ with $\alpha < 1$), this can lead to dynamic arbitrage concerns (Gatheral 2010). Ensuring no-dynamic-arbitrage places constraints on the relationship between temporary and permanent impact functions.

    **Summary of extensions:**

    | Assumption | Effect on Optimal Strategy |
    |---|---|
    | Mean-reverting prices | Adaptive: trade faster when price favorable |
    | Time-varying volatility | Trade faster in high-vol periods |
    | Stochastic volatility | Real-time adaptive adjustment |
    | Concave temporary impact | More front-loaded than linear case |
    | Transient (decaying) impact | More spread out to allow decay |
    | Positive drift | Delay execution; negative drift: accelerate |

    In practice, production-grade execution algorithms incorporate many of these extensions, using real-time data to continuously update the trading schedule.
