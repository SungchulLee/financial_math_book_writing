# Robust Delta–Gamma Hedging

## Introduction

Robust delta-gamma hedging extends classical delta-hedging by incorporating second-order (gamma) risk management while maintaining robustness to model misspecification. This approach recognizes that:

1. **Delta-hedging alone is insufficient**: First-order hedging eliminates linear risk but leaves exposure to convexity
2. **Gamma matters**: Large price moves or high volatility make gamma exposure significant
3. **Model uncertainty**: True volatility dynamics are unknown; hedging must work across multiple scenarios
4. **Practical constraints**: Perfect continuous hedging is impossible; robust strategies handle discrete rebalancing

The mathematical framework draws from stochastic optimal control, robust optimization, and PDE theory, providing both theoretical foundations and implementable algorithms for managing higher-order risks under model uncertainty.

## Mathematical Framework

### Greeks

**Delta**: First-order price sensitivity:

$$
\Delta = \frac{\partial V}{\partial S}
$$

**Gamma**: Second-order price sensitivity (curvature):

$$
\Gamma = \frac{\partial^2 V}{\partial S^2}
$$

**Vega**: Sensitivity to volatility:

$$
\mathcal{V} = \frac{\partial V}{\partial \sigma}
$$

**Relationship**: Under Black-Scholes:

$$
\mathcal{V} = S^2 \Gamma \sqrt{T - t}
$$

connecting gamma and vega.

### Portfolio Dynamics

**Position**: Hold $\theta_t$ shares of stock and $\phi_t$ options (for gamma hedging).

**Portfolio Value**:

$$
V_t = V(S_t, t) + \theta_t S_t + \phi_t O(S_t, t)
$$

where $O(S_t, t)$ is the option value.

**Delta-Gamma Neutral**: 

$$
\frac{\partial V}{\partial S} + \theta_t + \phi_t \frac{\partial O}{\partial S} = 0 \quad \text{(delta neutral)}
$$

$$
\frac{\partial^2 V}{\partial S^2} + \phi_t \frac{\partial^2 O}{\partial S^2} = 0 \quad \text{(gamma neutral)}
$$

**Solution**: 

$$
\phi_t = -\frac{\Gamma_V}{\Gamma_O}, \quad \theta_t = -\Delta_V + \phi_t \Delta_O
$$

where subscripts denote the derivative or hedging instrument.

## Classical Delta-Gamma Hedging

### Black-Scholes Framework

**Option PDE**: Under Black-Scholes with constant volatility $\sigma$:

$$
\frac{\partial V}{\partial t} + rS \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0
$$

**Perfect Hedge**: With continuous delta-gamma hedging:

$$
dV - \Delta \, dS - \Theta \, dt = 0
$$

where $\Theta = \frac{\partial V}{\partial t}$ is theta.

**Replication**: Portfolio value exactly replicates option value at all times.

### Discrete Hedging

**Time Grid**: Rebalance at times $\{t_0, t_1, \ldots, t_N\}$ with spacing $\Delta t = t_{i+1} - t_i$.

**Portfolio Dynamics**: Between rebalancing:

$$
dV_t = \theta_{t_i} \, dS_t + \phi_{t_i} \, dO_t
$$

for $t \in [t_i, t_{i+1})$.

**Taylor Expansion**: Option value change:

$$
\Delta V \approx \Delta \cdot \Delta S + \frac{1}{2} \Gamma \cdot (\Delta S)^2 + \Theta \cdot \Delta t + \frac{1}{2} \mathcal{V} \cdot (\Delta \sigma)^2 + \ldots
$$

**Hedging Error**: With delta-gamma hedging:

$$
\text{Error} \approx \frac{1}{6} \frac{\partial^3 V}{\partial S^3} (\Delta S)^3 + \frac{1}{2} \frac{\partial^2 V}{\partial S \partial t} \Delta S \, \Delta t + \ldots
$$

Third and higher-order terms, which vanish as $\Delta t \to 0$.

## Robust Hedging Under Volatility Uncertainty

### Uncertain Volatility Model

**Setup**: True volatility $\sigma_t$ is unknown but bounded:

$$
\underline{\sigma} \leq \sigma_t \leq \overline{\sigma}
$$

**Stock Dynamics**:

$$
dS_t = \mu S_t \, dt + \sigma_t S_t \, dW_t
$$

where $\sigma_t \in [\underline{\sigma}, \overline{\sigma}]$ is adversarially chosen.

**Objective**: Find hedging strategy that minimizes worst-case loss.

### Hamilton-Jacobi-Bellman Equation

**Value Function**: The minimal super-replication cost $V(S, t)$ satisfies:

$$
\frac{\partial V}{\partial t} + \sup_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} \left\{ \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right\} + rS \frac{\partial V}{\partial S} - rV = 0
$$

**Supremum**: Nature chooses volatility to maximize instantaneous risk.

**Solution**: 

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \bar{\sigma}^2(S, t) S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0
$$

where:

$$
\bar{\sigma}^2(S, t) = \begin{cases}
\overline{\sigma}^2 & \text{if } \frac{\partial^2 V}{\partial S^2} > 0 \\
\underline{\sigma}^2 & \text{if } \frac{\partial^2 V}{\partial S^2} < 0
\end{cases}
$$

**Interpretation**: 
- Positive gamma → Use maximum volatility (worst case)
- Negative gamma → Use minimum volatility (worst case)

### Hedging Strategy

**Delta Position**: 

$$
\theta_t = -\frac{\partial V}{\partial S}(S_t, t)
$$

**Gamma Position**: Adjust using options to target gamma:

$$
\Gamma_{\text{target}}(S, t) = \begin{cases}
0 & \text{if gamma is costly to hedge} \\
-\Gamma_V(S, t) & \text{if neutralizing gamma is beneficial}
\end{cases}
$$

**Adaptive**: Strategy adapts to whether position is long or short gamma.

## Multi-Factor Robust Hedging

### Stochastic Volatility

**Model**: Volatility follows its own process:

$$
dS_t = \mu S_t \, dt + \sqrt{V_t} S_t \, dW_t^S
$$

$$
dV_t = \kappa(\theta - V_t) \, dt + \xi \sqrt{V_t} \, dW_t^V
$$

with correlation $\rho = \mathbb{E}[dW_t^S dW_t^V]$.

**Greeks**:
- $\Delta = \frac{\partial V}{\partial S}$
- $\Gamma = \frac{\partial^2 V}{\partial S^2}$
- $\mathcal{V} = \frac{\partial V}{\partial v}$ (vega)
- $\mathcal{V}_{\Gamma} = \frac{\partial^2 V}{\partial v^2}$ (volga/vomma)

**Hedging Instruments**: 
- Stock (for delta)
- Options at strike $K_1$ (for gamma)
- Options at strike $K_2$ (for vega)

**Portfolio**:

$$
\Pi_t = V_t + \theta_t^S S_t + \theta_t^{O_1} O_1(S_t, v_t; K_1) + \theta_t^{O_2} O_2(S_t, v_t; K_2)
$$

**Neutral Conditions**:

$$
\frac{\partial \Pi}{\partial S} = 0, \quad \frac{\partial^2 \Pi}{\partial S^2} = 0, \quad \frac{\partial \Pi}{\partial v} = 0
$$

This is a **system of 3 equations** in 3 unknowns: $(\theta^S, \theta^{O_1}, \theta^{O_2})$.

### Cross-Gamma

**Definition**: 

$$
\Gamma_{Sv} = \frac{\partial^2 V}{\partial S \partial v}
$$

measures interaction between price and volatility changes.

**Hedging**: Cannot fully hedge cross-gamma with stock and single-maturity options alone. Requires:
- Multiple option maturities
- Exotic options sensitive to correlation

**Practical Approach**: Accept some residual cross-gamma risk as unavoidable.

## Robust Optimization Framework

### Worst-Case Hedging

**Objective**: Minimize maximum loss over uncertainty set:

$$
\min_{\theta, \phi} \max_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} \mathbb{E}_{\sigma}\left[(V_T - \Pi_T)^2\right]
$$

where $\Pi_T$ is the hedged portfolio value.

**Solution Approach**:
1. Discretize uncertainty set: $\{\sigma_1, \ldots, \sigma_n\}$
2. Solve for each scenario
3. Choose strategy that performs best in worst scenario

### Robust PDE

**General Form**: For uncertainty in drift $\mu$ and volatility $\sigma$:

$$
\frac{\partial V}{\partial t} + \sup_{(\mu, \sigma) \in \mathcal{U}} \left\{ \mu S \frac{\partial V}{\partial S} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right\} = 0
$$

where $\mathcal{U}$ is the uncertainty set.

**Viscosity Solution**: The value function is characterized as the unique viscosity solution to this PDE.

**Numerical Methods**: 
- Finite differences with supremum at each grid point
- Semi-Lagrangian schemes
- Policy iteration

### Penalty Function Approach

**Regularization**: Instead of hard constraints on $\sigma$, penalize deviations from reference:

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma_0^2 S^2 \frac{\partial^2 V}{\partial S^2} + \sup_{\sigma} \left\{ \frac{1}{2}(\sigma^2 - \sigma_0^2) S^2 \frac{\partial^2 V}{\partial S^2} - \theta \cdot \frac{(\sigma - \sigma_0)^2}{2} \right\} = 0
$$

**Solution**: 

$$
\sigma^* = \sigma_0 + \frac{1}{\theta} S^2 \frac{\partial^2 V}{\partial S^2}
$$

clamped to $[\underline{\sigma}, \overline{\sigma}]$.

**Interpretation**: $\theta$ measures aversion to model deviation; large $\theta$ keeps $\sigma^*$ close to $\sigma_0$.

## Transaction Costs

### Discrete Rebalancing

**Cost Model**: Proportional costs $\lambda$ per unit traded:

$$
\text{Cost} = \lambda |\Delta \theta| S + \lambda |\Delta \phi| O
$$

**Optimal Rebalancing**: Trade-off between hedging error and transaction costs:

$$
\min_{\{\Delta \theta_i, \Delta \phi_i\}} \mathbb{E}\left[(V_T - \Pi_T)^2 + \sum_{i=1}^N \lambda_i (|\Delta \theta_i| S_i + |\Delta \phi_i| O_i)\right]
$$

**No-Transaction Region**: Optimal to rebalance only when Greeks drift outside a band:

$$
|\Delta(S_t) - \Delta_{\text{portfolio}}| > \epsilon_{\Delta}, \quad |\Gamma(S_t) - \Gamma_{\text{portfolio}}| > \epsilon_{\Gamma}
$$

where $\epsilon_{\Delta}, \epsilon_{\Gamma}$ depend on $\lambda$ and $\sigma$.

### Asymptotic Analysis

**Small Transaction Costs**: As $\lambda \to 0$:

$$
\epsilon_{\Delta} \sim \lambda^{1/3}, \quad \epsilon_{\Gamma} \sim \lambda^{1/3}
$$

**Hedging Error**: Expected squared error:

$$
\mathbb{E}[(V_T - \Pi_T)^2] \sim \lambda^{2/3}
$$

**Implication**: Even small transaction costs significantly impact optimal hedging strategy.

### Leland's Approach

**Modified Volatility**: To account for transaction costs in delta-hedging, use:

$$
\tilde{\sigma}^2 = \sigma^2 + \sqrt{\frac{2}{\pi}} \lambda \frac{\sigma}{\sqrt{\Delta t}}
$$

**Interpretation**: Transaction costs effectively increase volatility used in Black-Scholes formula.

**Gamma Adjustment**: With gamma hedging, modification is more complex, involving both delta and gamma adjustments.

## Correlation Risk

### Multi-Asset Portfolios

**Assets**: $\mathbf{S}_t = (S_t^{(1)}, \ldots, S_t^{(n)})$ with correlation matrix $\rho$.

**Greeks Matrix**:

$$
\boldsymbol{\Gamma} = \begin{pmatrix}
\Gamma_{11} & \Gamma_{12} & \cdots & \Gamma_{1n} \\
\Gamma_{21} & \Gamma_{22} & \cdots & \Gamma_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
\Gamma_{n1} & \Gamma_{n2} & \cdots & \Gamma_{nn}
\end{pmatrix}
$$

where $\Gamma_{ij} = \frac{\partial^2 V}{\partial S_i \partial S_j}$.

**Hedging**: Requires $\frac{n(n+1)}{2}$ instruments to neutralize all second-order sensitivities.

**Robust Correlation**: Assume correlation $\rho_{ij} \in [\underline{\rho}_{ij}, \overline{\rho}_{ij}]$.

**Worst-Case Scenario**:

$$
\max_{\rho \in \mathcal{R}} \sum_{i,j} \Gamma_{ij} \rho_{ij}
$$

where $\mathcal{R}$ is the set of valid correlation matrices in the uncertainty range.

### Basket Options

**Payoff**: 

$$
\Phi = \left(\sum_{i=1}^n w_i S_T^{(i)} - K\right)^+
$$

**Challenge**: Cross-gammas $\Gamma_{ij}$ for $i \neq j$ are sensitive to correlation.

**Hedging Strategy**:
1. Delta-hedge each component
2. Gamma-hedge using options on individual assets
3. Accept residual cross-gamma risk or hedge using basket options if available

**Robust Approach**: Compute worst-case correlation matrix:

$$
\rho^* = \arg\max_{\rho \in \mathcal{R}} \text{Hedging Error}(\rho)
$$

and hedge for this scenario.

## Numerical Methods

### Finite Difference Schemes

**Grid**: Discretize $(S, t)$ space:
- Space: $S \in \{S_{\min}, S_{\min} + \Delta S, \ldots, S_{\max}\}$
- Time: $t \in \{0, \Delta t, 2\Delta t, \ldots, T\}$

**Approximation**: 

$$
\frac{\partial V}{\partial t} \approx \frac{V_i^{n+1} - V_i^n}{\Delta t}
$$

$$
\frac{\partial^2 V}{\partial S^2} \approx \frac{V_{i+1}^n - 2V_i^n + V_{i-1}^n}{(\Delta S)^2}
$$

**Robust PDE Discretization**:

$$
\frac{V_i^{n+1} - V_i^n}{\Delta t} + \max_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} \left\{ \frac{1}{2} \sigma^2 S_i^2 \frac{V_{i+1}^n - 2V_i^n + V_{i-1}^n}{(\Delta S)^2} \right\} + \ldots = 0
$$

**Algorithm**:
1. For each grid point $(S_i, t_n)$
2. Compute $\Gamma_i^n = \frac{V_{i+1}^n - 2V_i^n + V_{i-1}^n}{(\Delta S)^2}$
3. Choose $\sigma^* = \overline{\sigma}$ if $\Gamma_i^n > 0$, else $\sigma^* = \underline{\sigma}$
4. Update $V_i^{n+1}$ using explicit or implicit scheme

### Monte Carlo with Stochastic Control

**Scenario Generation**: Simulate paths under various volatility scenarios.

**Regression**: At each rebalancing time $t_i$, estimate conditional expectations:

$$
\mathbb{E}[V_{t_{i+1}} | S_{t_i}] \approx \sum_j \beta_j \phi_j(S_{t_i})
$$

using basis functions $\{\phi_j\}$ (polynomials, radial basis functions, etc.).

**Optimal Hedge**: Choose $\theta_{t_i}, \phi_{t_i}$ to minimize:

$$
\text{Var}(V_{t_{i+1}} - \theta_{t_i} S_{t_{i+1}} - \phi_{t_i} O_{t_{i+1}} | S_{t_i})
$$

**Iteration**: Work backwards from maturity to initial time.

### Policy Iteration

**Value Function**: Guess initial $V^{(0)}(S, t)$.

**Policy Update**: Given $V^{(k)}$, compute optimal control:

$$
\sigma^{(k+1)}(S, t) = \arg\max_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} \left\{ \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V^{(k)}}{\partial S^2} \right\}
$$

**Value Update**: Solve:

$$
\frac{\partial V^{(k+1)}}{\partial t} + \frac{1}{2} (\sigma^{(k+1)})^2 S^2 \frac{\partial^2 V^{(k+1)}}{\partial S^2} + \ldots = 0
$$

**Convergence**: Iterate until $\|V^{(k+1)} - V^{(k)}\| < \epsilon$.

## Greeks Monitoring and Adjustment

### Delta-Gamma Dashboard

**Real-Time Display**:
- Current spot price $S_t$
- Portfolio delta: $\Delta_{\text{portfolio}} = \sum_i \Delta_i n_i$
- Portfolio gamma: $\Gamma_{\text{portfolio}} = \sum_i \Gamma_i n_i$
- Target delta: $\Delta_{\text{target}}(S_t)$ (usually 0)
- Target gamma: $\Gamma_{\text{target}}(S_t)$ (model-dependent)
- Deviation metrics: $|\Delta_{\text{portfolio}} - \Delta_{\text{target}}|$, $|\Gamma_{\text{portfolio}} - \Gamma_{\text{target}}|$

**Alert Thresholds**: 
- **Yellow**: Deviation exceeds 10% of target
- **Red**: Deviation exceeds 25% of target

### Adjustment Algorithm

**Trigger**: If $|\Delta_{\text{portfolio}} - \Delta_{\text{target}}| > \epsilon_{\Delta}$ or $|\Gamma_{\text{portfolio}} - \Gamma_{\text{target}}| > \epsilon_{\Gamma}$:

**Step 1**: Compute required adjustments:

$$
\Delta \phi = -\frac{\Gamma_{\text{portfolio}} - \Gamma_{\text{target}}}{\Gamma_O}
$$

$$
\Delta \theta = -(\Delta_{\text{portfolio}} - \Delta_{\text{target}}) + \Delta \phi \cdot \Delta_O
$$

**Step 2**: Estimate transaction costs:

$$
\text{Cost} = \lambda (|\Delta \theta| S_t + |\Delta \phi| O_t)
$$

**Step 3**: If Cost < Expected benefit, execute trades. Otherwise, wait.

**Step 4**: Update portfolio records and reset targets.

### Stress Testing

**Scenarios**: Test portfolio performance under extreme scenarios:
1. **Large price move**: $S_t \to S_t \pm 10\%$
2. **Vol spike**: $\sigma \to \sigma + 20\%$
3. **Combined**: Simultaneous price drop and vol spike
4. **Flash crash**: $S_t \to S_t - 20\%$ instantaneously

**Metrics**:
- Change in portfolio value: $\Delta V$
- Change in delta: $\Delta \Delta$
- Change in gamma: $\Delta \Gamma$
- Worst-case loss: $\min_{\text{scenario}} \Delta V$

**Action**: If worst-case loss exceeds risk limits, adjust hedging strategy preemptively.

## Practical Applications

### Example 1: At-the-Money Call Option

**Setup**:
- $S_0 = 100$, $K = 100$, $T = 1$ month, $r = 5\%$
- Volatility uncertainty: $\sigma \in [15\%, 25\%]$

**Classical Hedge** (assume $\sigma = 20\%$):
- Delta: $\Delta = 0.52$
- Gamma: $\Gamma = 0.040$

**Robust Hedge**:
1. Compute robust value $V(S_0, 0)$ using HJB with $\sigma \in [15\%, 25\%]$
2. Robust delta and gamma:
   - If $\Gamma > 0$: Use $\sigma = 25\%$ for worst-case
   - Robust $\Delta = 0.53$, $\Gamma = 0.042$

**Hedging Portfolio**:
- Short 0.53 shares (delta-neutral)
- Long options to offset gamma if available, or accept gamma exposure

**Rebalancing**: Daily, with thresholds $\epsilon_{\Delta} = 0.05$, $\epsilon_{\Gamma} = 0.01$.

### Example 2: Short Straddle

**Position**:
- Short 1 call at strike $K = 100$
- Short 1 put at strike $K = 100$
- Initial spot: $S_0 = 100$

**Greeks**:
- Delta: $\Delta_{\text{call}} - \Delta_{\text{put}} = 0.52 - (-0.48) = 1.00 \approx 0$ (near ATM)
- Gamma: $\Gamma_{\text{call}} + \Gamma_{\text{put}} = 0.040 + 0.040 = 0.080$ (negative, since we're short)

**Gamma Risk**: Large negative gamma → profits if $S$ stays near $K$, losses if $S$ moves significantly.

**Hedging**:
1. **Delta-neutral**: Hold 0 shares initially
2. **Gamma-hedging**: 
   - **Option 1**: Long ATM options to neutralize gamma (expensive)
   - **Option 2**: Accept gamma risk, hedge delta dynamically and frequently
   - **Option 3**: Partial gamma hedge with OTM options (cheaper)

**Robust Approach**: Use robust PDE with $\sigma \in [\underline{\sigma}, \overline{\sigma}]$ to price cost of gamma hedging. Trade-off expected profit vs. worst-case loss.

### Example 3: Exotic Barrier Option

**Product**: Down-and-out call, $K = 100$, barrier $H = 90$, $T = 3$ months.

**Greeks Near Barrier**:
- Delta discontinuous at $S = H$
- Gamma spikes as $S \to H$
- Vega also large near barrier

**Hedging Strategy**:
1. **Away from barrier** ($S > 95$): Standard delta-gamma hedge
2. **Near barrier** ($90 < S < 95$):
   - Increase gamma hedge (more options)
   - Tighten rebalancing frequency
   - Monitor continuously
3. **At barrier** ($S \approx 90$):
   - Expect large P&L swing
   - Liquidate position if knocked out

**Robustness**: Use uncertain volatility model to compute worst-case scenarios near barrier. Over-hedge gamma near $H$ to protect against spike risk.

## Advanced Topics

### Smile Risk

**Implied Volatility Surface**: $\sigma(K, T)$ varies with strike and maturity.

**Sticky Delta vs. Sticky Strike**: Models for how smile evolves as $S$ changes:
- **Sticky delta**: $\sigma$ depends on $\Delta$, not absolute $K$
- **Sticky strike**: $\sigma$ remains at fixed strike $K$

**Hedging Implications**:
- Under sticky strike: Standard delta-gamma hedge is adequate
- Under sticky delta: Need to adjust for smile movement as $S$ changes

**Robust Approach**: Assume worst-case smile dynamics among plausible models.

### Rough Volatility

**Model**: Volatility has Hölder regularity $H < 1/2$:

$$
\sigma_t = f\left(\int_0^t (t-s)^{H-1/2} dW_s\right)
$$

**Gamma Hedging**: Classical quadratic variation arguments don't apply directly.

**Rough Path Hedging**: Use rough path theory to define gamma properly:

$$
\text{Gamma Cost} = \int_0^T \Gamma_t \, d[S]_t
$$

where $[S]_t$ is understood in rough path sense.

**Practical Impact**: Need finer rebalancing frequency for rough volatility than smooth models suggest.

### Jump Diffusion

**Dynamics**: 

$$
dS_t = \mu S_t \, dt + \sigma S_t \, dW_t + S_{t-} dJ_t
$$

where $J_t$ is a jump process.

**Gamma Hedging Failure**: Gamma hedging protects against continuous moves, not jumps.

**Jump Protection**: 
- Long OTM puts (downside jump protection)
- Long OTM calls (upside jump protection)
- Cost: Premium for tail options

**Robust Approach**: Assume worst-case jump intensity and size within uncertainty set.

## Model Comparison

### Model-Specific Hedging

**Black-Scholes**: Constant volatility → Simple delta hedge sufficient asymptotically.

**Stochastic Volatility (Heston)**: Need to hedge vega exposure using options at different strikes/maturities.

**Local Volatility**: $\sigma(S, t)$ deterministic function → Delta hedge sufficient, but gamma varies with $(S, t)$.

**Jump Diffusion**: Delta-gamma hedge insufficient → Need tail options.

### Robust Hedging

**Model-Free**: Works for **all models** within uncertainty class.

**Conservative**: Hedges against worst-case scenario, which may be overly pessimistic.

**Cost**: Higher hedging cost due to conservatism, but provides insurance against model risk.

**Trade-Off**: Balance robustness (protection) vs. cost (hedging expense).

## Performance Metrics

### Hedging Error

**Definition**: 

$$
\text{Error} = V_T - \Pi_T
$$

where $\Pi_T$ is hedged portfolio value.

**Mean Squared Error**:

$$
\text{MSE} = \mathbb{E}[(\text{Error})^2]
$$

**Root Mean Squared Error**:

$$
\text{RMSE} = \sqrt{\text{MSE}}
$$

### Sharpe Ratio of Hedged Portfolio

**Return**: 

$$
R = \frac{\Pi_T - \Pi_0}{\Pi_0}
$$

**Sharpe Ratio**:

$$
\text{SR} = \frac{\mathbb{E}[R] - r_f}{\text{Std}(R)}
$$

where $r_f$ is the risk-free rate.

**Interpretation**: Higher SR indicates better risk-adjusted performance.

### Maximum Drawdown

**Drawdown**: Largest peak-to-trough decline:

$$
\text{DD}_t = \max_{0 \leq s \leq t} \Pi_s - \Pi_t
$$

**Maximum Drawdown**:

$$
\text{MDD} = \max_{0 \leq t \leq T} \text{DD}_t
$$

**Risk Management**: Set limits on MDD to control tail risk.

### Cost-Benefit Analysis

**Total Cost**: Transaction costs + option premiums:

$$
\text{Total Cost} = \sum_{i=1}^N \lambda |\Delta \theta_i| S_i + \sum_{j=1}^M \text{Premium}_j
$$

**Benefit**: Reduction in hedging error variance:

$$
\text{Benefit} = \text{Var}(\text{Error}_{\text{unhedged}}) - \text{Var}(\text{Error}_{\text{hedged}})
$$

**Ratio**:

$$
\text{Cost-Benefit Ratio} = \frac{\text{Total Cost}}{\text{Benefit}}
$$

Aim for CBR < 1 (benefits exceed costs).

## Case Studies

### Case 1: Market Maker in Equity Options

**Position**: Long/short various calls and puts on S&P 500 across strikes and maturities.

**Challenges**:
- Need to maintain delta-gamma neutrality across entire book
- Manage vega exposure to volatility changes
- Transaction costs for frequent rebalancing

**Strategy**:
1. **Aggregate Greeks**: Sum delta, gamma, vega across all positions
2. **Delta-Gamma Neutral**: Use S&P futures for delta, ATM options for gamma
3. **Vega Hedging**: Use VIX futures or variance swaps
4. **Robust PDE**: Price inventory using uncertain volatility model with $\sigma \in [12\%, 30\%]$
5. **Rebalancing**: Intraday for delta (< 1% threshold), daily for gamma (< 5% threshold)

**Results**: 
- Hedging error RMSE: 0.5% of notional
- Transaction costs: 0.2% of notional per month
- Sharpe ratio of hedged book: 1.8

### Case 2: Exotic Derivatives Desk

**Portfolio**: Short Asian, lookback, and barrier options on FX pairs.

**Complexity**: Path-dependent payoffs, multiple underlyings, correlation risk.

**Hedging**:
1. **Pathwise Hedging**: Use functional derivatives for exotic Greeks
2. **Delta-Gamma Framework**: Extend to path-dependent state variables
3. **Correlation Hedging**: Use quanto options and multi-asset options
4. **Robust Optimization**: Assume worst-case volatility and correlation scenarios

**Risk Management**:
- Daily stress tests under extreme scenarios
- VaR limit: $5M at 95% confidence
- CVaR limit: $10M at 99% confidence

**Performance**: 
- P&L volatility reduced by 70% with hedging
- Cost of hedging: 1% of notional per year

### Case 3: Volatility Arbitrage Fund

**Strategy**: Long-short positions exploiting implied vs. realized volatility mispricing.

**Core Position**:
- Long straddles when implied vol < expected realized vol
- Short straddles when implied vol > expected realized vol

**Delta-Gamma Management**:
1. **Delta-Neutral**: Maintain zero delta across portfolio
2. **Gamma Exposure**: Intentionally long or short gamma depending on volatility view
3. **Dynamic Hedging**: Rebalance delta frequently (every 15 minutes during market hours)
4. **Vega Limits**: Cap aggregate vega to manage exposure to volatility changes

**Robust Approach**: Use robust PDE to value positions assuming volatility in range informed by historical data and vol-of-vol estimates.

**Results**:
- Annualized return: 12%
- Volatility: 8%
- Sharpe ratio: 1.5
- Maximum drawdown: 5%

## Summary and Key Insights

### Fundamental Principles

1. **Second-Order Risk**: Gamma captures curvature risk that delta-hedging alone cannot eliminate.

2. **Robustness**: Uncertain volatility framework provides hedging strategies that work across multiple scenarios.

3. **Trade-Offs**: Balancing hedging accuracy, transaction costs, and model risk is central to practical implementation.

4. **Higher-Order Greeks**: In reality, vega, volga, vanna, and other Greeks matter; comprehensive hedging requires multiple instruments.

5. **Discretization**: Continuous theory provides intuition, but discrete rebalancing is the reality; asymptotic analysis guides optimal frequencies.

### Practical Guidelines

**When to Gamma-Hedge**:
- Short optionality (sold options)
- Large price moves expected
- Near barrier or strike boundaries
- High gamma exposure relative to portfolio size

**When Delta-Hedging Suffices**:
- Long optionality (bought options)
- Small moves expected
- Transaction costs prohibitive
- Far from strikes and barriers

**Robustness Design**:
- Estimate realistic volatility ranges from historical data and market implied vols
- Use robust PDE for pricing and Greeks computation
- Stress test under extreme scenarios
- Dynamically adjust uncertainty ranges as new information arrives

### Theoretical Foundations

- **Avellaneda-Paras**: Robust pricing under volatility uncertainty
- **Lyons**: Rough path theory for finance
- **El Karoui et al.**: Backward SDEs and hedging under constraints
- **Cont-Tankov**: Jump models and incomplete market hedging
- **Wilmott et al.**: Practical aspects of gamma hedging

### Future Directions

Robust delta-gamma hedging continues to evolve with:
- **Machine learning**: Learning optimal hedging policies from data
- **High-frequency data**: Using tick-by-tick information for better gamma estimation
- **Multi-asset frameworks**: Extending to portfolios with complex correlation structures
- **Market microstructure**: Incorporating liquidity and market impact into hedging models

The robust delta-gamma framework provides a practical, theoretically sound approach to managing second-order risk while acknowledging and protecting against model uncertainty, bridging academic theory and trading practice in quantitative finance.
