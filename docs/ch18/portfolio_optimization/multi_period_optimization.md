
# Multi-Period Optimization and Dynamic Portfolio Rebalancing



The single-period portfolio optimization framework, while elegant and analytically tractable, is limited in its ability to model the dynamic nature of real-world investing. In practice, portfolios are held over multiple periods, during which asset prices evolve stochastically, investor objectives may change, and new information becomes available. This necessitates a transition from static to dynamic models of asset allocation—accounting for intertemporal preferences, transaction costs, and path-dependent constraints.

This section develops the theoretical foundation of multi-period portfolio optimization, introduces dynamic programming and model predictive control (MPC) approaches, and discusses practical methods of portfolio rebalancing under uncertainty.



## 1. Intertemporal Investment Problem



Let the investment horizon consist of $T$ discrete time periods, indexed by $t = 0, 1, \dots, T-1$. Let:

- $\mathbf{w}_t$ be the portfolio weights at time $t$,
- $\boldsymbol{r}_{t+1}$ be the (random) return vector between $t$ and $t+1$,
- $W_t$ be the portfolio value at time $t$.

The portfolio evolves as:

$$
W_{t+1} = W_t (1 + \mathbf{w}_t^T \boldsymbol{r}_{t+1})
$$

An investor maximizes expected utility over the terminal wealth or, in more general settings, over a stream of consumption and wealth:

**Terminal Utility Model**

$$
\max_{\{\mathbf{w}_t\}_{t=0}^{T-1}} \mathbb{E}[U(W_T)]
$$

**Intertemporal Consumption Model**

$$
\max_{\{\mathbf{w}_t, c_t\}} \mathbb{E} \left[ \sum_{t=0}^{T-1} \delta^t u(c_t) + \delta^T U(W_T) \right]
$$



subject to budget and feasibility constraints. Here, $u(\cdot)$ and $U(\cdot)$ are concave utility functions, and $\delta \in (0, 1]$ is a discount factor.

This formulation yields a **dynamic stochastic control problem**, often approached using **Bellman equations** or **stochastic dynamic programming**.



## 2. Dynamic Programming and the Bellman Equation



The value function at time $t$ is:

$$
V_t(W_t) = \max_{\mathbf{w}_t} \mathbb{E}_t \left[ V_{t+1}(W_{t+1}) \right]
$$

with terminal condition:

$$
V_T(W_T) = U(W_T)
$$

The optimal portfolio policy $\{\mathbf{w}_t^*\}$ is obtained by backward induction. For log utility and i.i.d. returns, the multi-period problem reduces to the static problem:

- The **myopic property** of log utility implies that the investor optimizes at each time as if it were the final period.

However, for general utility functions (e.g., power utility), the optimal policy exhibits **intertemporal hedging demand**—a desire to adjust today’s portfolio in anticipation of future changes in investment opportunities.

This leads to decomposition of the optimal policy into:

- **Myopic demand**: responds to current return and risk trade-offs.
- **Hedging demand**: responds to changes in the investment opportunity set.



## 3. Model Predictive Control (MPC) Approach



In practice, solving the dynamic programming problem exactly may be infeasible due to:

- High dimensionality,
- Non-stationarity in returns,
- Path-dependent constraints (e.g., drawdown limits, capital calls).

An alternative is the **Model Predictive Control** (MPC) or **receding horizon** approach, in which:

1. At each time step $t$, solve a finite-horizon optimization problem over $H$ future periods.
2. Implement only the first-period decision $\mathbf{w}_t^*$.
3. At $t+1$, re-estimate the model and repeat.

MPC provides a tractable and adaptive mechanism to dynamically update decisions in response to new data or regime shifts.



## 4. Transaction Costs and Rebalancing Strategies



Dynamic portfolio management must incorporate **transaction costs**, which may be:

- **Proportional**: $\tau \|\mathbf{w}_{t+1} - \mathbf{w}_t\|_1$
- **Fixed**: per-trade execution cost
- **Market impact models**: increasing with order size

The inclusion of transaction costs introduces *friction* and leads to **infrequent trading** and **no-trade regions**.

Common rebalancing strategies include:

- **Periodic rebalancing**: rebalance every $k$ periods.
- **Threshold rebalancing**: rebalance when deviation from target exceeds tolerance.
- **Cost-aware optimization**: solve for optimal tradeoff between tracking error and transaction cost.



#### Example: Transaction Cost-Aware Optimization


$$
\min_{\mathbf{w}_{t+1}} \; \lambda \|\mathbf{w}_{t+1} - \mathbf{w}_t\|_1 + (1 - \lambda) \| \mathbf{w}_{t+1} - \mathbf{w}_{\text{target}} \|_2^2
$$

where $\mathbf{w}_{\text{target}}$ is the mean-variance optimal allocation and $\lambda$ controls the cost-return trade-off.



## 5. Empirical Considerations in Multi-Period Models



In real-world implementation, dynamic portfolio strategies face several challenges:

- **Parameter uncertainty**: return forecasts and covariances evolve over time.
- **Model risk**: dependence on assumptions of stationarity, ergodicity, or return distribution.
- **Path dependence**: wealth constraints, taxation, and liquidity considerations vary over the horizon.

To address these issues:

- Use **robust estimation and regularization** within each re-optimization window.
- Apply **Bayesian updating** to parameter distributions as new data arrives.
- Incorporate **scenario-based or Monte Carlo simulation** for uncertainty modeling.



## Summary



Multi-period portfolio optimization extends the single-period framework into a dynamic setting that reflects the realities of evolving markets, transaction costs, and investment horizons. By modeling wealth evolution over time and incorporating intertemporal preferences, investors can construct adaptive policies that balance risk, return, and cost in a forward-looking manner. Approaches such as dynamic programming, model predictive control, and transaction cost-aware rebalancing provide both theoretical rigor and practical tools for dynamic asset allocation.