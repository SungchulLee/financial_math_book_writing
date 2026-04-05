# Robust Delta–Gamma Hedging


## Introduction


Robust delta-gamma hedging extends classical delta-hedging by incorporating second-order (gamma) risk management while maintaining robustness to model misspecification. This approach recognizes that:

1. **Delta-hedging alone is insufficient**: First-order hedging eliminates linear risk but leaves exposure to convexity
2. **Gamma matters**: Large price moves or high volatility make gamma exposure significant
3. **Model uncertainty**: True volatility dynamics are unknown; hedging must work across multiple scenarios
4. **Practical constraints**: Perfect continuous hedging is impossible; robust strategies handle discrete rebalancing

The mathematical framework draws from stochastic optimal control, robust optimization, and PDE theory, providing both theoretical foundations and implementable algorithms for managing higher-order risks under model uncertainty.

## Mathematical Framework


### 1. Greeks


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

### 2. Portfolio Dynamics


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


### 1. Black-Scholes Framework


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

### 2. Discrete Hedging


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


### 1. Uncertain Volatility Model


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

### 2. Hamilton-Jacobi-Bellman Equation


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

### 3. Hedging Strategy


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


### 1. Stochastic Volatility


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

### 2. Cross-Gamma


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


### 1. Worst-Case Hedging


**Objective**: Minimize maximum loss over uncertainty set:


$$
\min_{\theta, \phi} \max_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} \mathbb{E}_{\sigma}\left[(V_T - \Pi_T)^2\right]
$$



where $\Pi_T$ is the hedged portfolio value.

**Solution Approach**:
1. Discretize uncertainty set: $\{\sigma_1, \ldots, \sigma_n\}$
2. Solve for each scenario
3. Choose strategy that performs best in worst scenario

### 2. Robust PDE


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

### 3. Penalty Function Approach


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


### 1. Discrete Rebalancing


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

### 2. Asymptotic Analysis


**Small Transaction Costs**: As $\lambda \to 0$:


$$
\epsilon_{\Delta} \sim \lambda^{1/3}, \quad \epsilon_{\Gamma} \sim \lambda^{1/3}
$$



**Hedging Error**: Expected squared error:


$$
\mathbb{E}[(V_T - \Pi_T)^2] \sim \lambda^{2/3}
$$



**Implication**: Even small transaction costs significantly impact optimal hedging strategy.

### 3. Leland's Approach


**Modified Volatility**: To account for transaction costs in delta-hedging, use:


$$
\tilde{\sigma}^2 = \sigma^2 + \sqrt{\frac{2}{\pi}} \lambda \frac{\sigma}{\sqrt{\Delta t}}
$$



**Interpretation**: Transaction costs effectively increase volatility used in Black-Scholes formula.

**Gamma Adjustment**: With gamma hedging, modification is more complex, involving both delta and gamma adjustments.

## Correlation Risk


### 1. Multi-Asset Portfolios


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

### 2. Basket Options


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


### 1. Finite Difference Schemes


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

### 2. Monte Carlo with Stochastic Control


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

### 3. Policy Iteration


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


### 1. Delta-Gamma Dashboard


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

### 2. Adjustment Algorithm


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

### 3. Stress Testing


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


### 1. Example 1: At-the-Money Call Option


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

### 2. Example 2: Short Straddle


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

### 3. Example 3: Exotic Barrier Option


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


### 1. Smile Risk


**Implied Volatility Surface**: $\sigma(K, T)$ varies with strike and maturity.

**Sticky Delta vs. Sticky Strike**: Models for how smile evolves as $S$ changes:
- **Sticky delta**: $\sigma$ depends on $\Delta$, not absolute $K$
- **Sticky strike**: $\sigma$ remains at fixed strike $K$

**Hedging Implications**:
- Under sticky strike: Standard delta-gamma hedge is adequate
- Under sticky delta: Need to adjust for smile movement as $S$ changes

**Robust Approach**: Assume worst-case smile dynamics among plausible models.

### 2. Rough Volatility


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

### 3. Jump Diffusion


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


### 1. Model-Specific Hedging


**Black-Scholes**: Constant volatility → Simple delta hedge sufficient asymptotically.

**Stochastic Volatility (Heston)**: Need to hedge vega exposure using options at different strikes/maturities.

**Local Volatility**: $\sigma(S, t)$ deterministic function → Delta hedge sufficient, but gamma varies with $(S, t)$.

**Jump Diffusion**: Delta-gamma hedge insufficient → Need tail options.

### 2. Robust Hedging


**Model-Free**: Works for **all models** within uncertainty class.

**Conservative**: Hedges against worst-case scenario, which may be overly pessimistic.

**Cost**: Higher hedging cost due to conservatism, but provides insurance against model risk.

**Trade-Off**: Balance robustness (protection) vs. cost (hedging expense).

## Performance Metrics


### 1. Hedging Error


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



### 2. Sharpe Ratio of Hedged Portfolio


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

### 3. Maximum Drawdown


**Drawdown**: Largest peak-to-trough decline:


$$
\text{DD}_t = \max_{0 \leq s \leq t} \Pi_s - \Pi_t
$$



**Maximum Drawdown**:


$$
\text{MDD} = \max_{0 \leq t \leq T} \text{DD}_t
$$



**Risk Management**: Set limits on MDD to control tail risk.

### 4. Cost-Benefit Analysis


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


### 1. Case 1: Market Maker in Equity Options


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

### 2. Case 2: Exotic Derivatives Desk


**Portfolio**: Short Asian, lookback, and barrier options on FX pairs.

**Complexity**: Path-dependent payoffs, multiple underlyings, correlation risk.

**Hedging**:
1. **Pathwise Hedging**: Use functional derivatives for exotic Greeks
2. **Delta-Gamma Framework**: Extend to path-dependent state variables
3. **Correlation Hedging**: Use quanto options and multi-asset options
4. **Robust Optimization**: Assume worst-case volatility and correlation scenarios

**Risk Management**:
- Daily stress tests under extreme scenarios
- VaR limit: \$5M at 95% confidence
- CVaR limit: \$10M at 99% confidence

**Performance**: 
- P&L volatility reduced by 70% with hedging
- Cost of hedging: 1% of notional per year

### 3. Case 3: Volatility Arbitrage Fund


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


### 1. Fundamental Principles


1. **Second-Order Risk**: Gamma captures curvature risk that delta-hedging alone cannot eliminate.

2. **Robustness**: Uncertain volatility framework provides hedging strategies that work across multiple scenarios.

3. **Trade-Offs**: Balancing hedging accuracy, transaction costs, and model risk is central to practical implementation.

4. **Higher-Order Greeks**: In reality, vega, volga, vanna, and other Greeks matter; comprehensive hedging requires multiple instruments.

5. **Discretization**: Continuous theory provides intuition, but discrete rebalancing is the reality; asymptotic analysis guides optimal frequencies.

### 2. Practical Guidelines


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

### 3. Theoretical Foundations


- **Avellaneda-Paras**: Robust pricing under volatility uncertainty
- **Lyons**: Rough path theory for finance
- **El Karoui et al.**: Backward SDEs and hedging under constraints
- **Cont-Tankov**: Jump models and incomplete market hedging
- **Wilmott et al.**: Practical aspects of gamma hedging

### 4. Future Directions


Robust delta-gamma hedging continues to evolve with:
- **Machine learning**: Learning optimal hedging policies from data
- **High-frequency data**: Using tick-by-tick information for better gamma estimation
- **Multi-asset frameworks**: Extending to portfolios with complex correlation structures
- **Market microstructure**: Incorporating liquidity and market impact into hedging models

The robust delta-gamma framework provides a practical, theoretically sound approach to managing second-order risk while acknowledging and protecting against model uncertainty, bridging academic theory and trading practice in quantitative finance.

---

## Exercises

**Exercise 1.** For a European call option with $S_0 = 100$, $K = 100$, $T = 0.25$, $r = 0$, and $\sigma = 0.20$, compute the Black-Scholes delta $\Delta$ and gamma $\Gamma$. If the stock price moves by $\Delta S = 5$, compute the hedging error from a pure delta hedge and show that the gamma correction $\frac{1}{2}\Gamma (\Delta S)^2$ accounts for most of this error.

??? success "Solution to Exercise 1"

    **Given**: $S_0 = 100$, $K = 100$, $T = 0.25$, $r = 0$, $\sigma = 0.20$.

    **Step 1: Compute the Black-Scholes delta and gamma.**

    With $r = 0$ and ATM ($S_0 = K$):

    $$
    d_1 = \frac{\ln(S_0/K) + \frac{1}{2}\sigma^2 T}{\sigma\sqrt{T}} = \frac{0 + \frac{1}{2}(0.04)(0.25)}{0.20 \times 0.50} = \frac{0.005}{0.10} = 0.05
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T} = 0.05 - 0.10 = -0.05
    $$

    Delta:

    $$
    \Delta = \Phi(d_1) = \Phi(0.05) \approx 0.5199
    $$

    Gamma:

    $$
    \Gamma = \frac{\phi(d_1)}{S_0 \sigma \sqrt{T}} = \frac{\phi(0.05)}{100 \times 0.20 \times 0.50}
    $$

    where $\phi(0.05) = \frac{1}{\sqrt{2\pi}}e^{-0.05^2/2} = 0.3989 \times e^{-0.00125} \approx 0.3984$.

    $$
    \Gamma = \frac{0.3984}{10.0} = 0.03984
    $$

    **Step 2: Hedging error from a pure delta hedge when $\Delta S = 5$.**

    The exact option values:

    - At $S = 100$: $C(100) = S_0[2\Phi(d_1) - 1] = 100 \times [2(0.5199) - 1] = 100 \times 0.0399 = 3.99$ (approximately, using ATM formula with $r=0$).
    - At $S = 105$: Recompute $d_1 = \frac{\ln(105/100) + 0.005}{0.10} = \frac{0.04879 + 0.005}{0.10} = 0.5379$, so $C(105) \approx 105\Phi(0.5379) - 100\Phi(0.4379)$.

    Using $\Phi(0.5379) \approx 0.7047$ and $\Phi(0.4379) \approx 0.6693$:

    $$
    C(105) \approx 105 \times 0.7047 - 100 \times 0.6693 = 73.99 - 66.93 = 7.06
    $$

    The delta hedge P&L when $S$ moves from 100 to 105:

    $$
    \text{Hedge P\&L} = \Delta \times \Delta S = 0.5199 \times 5 = 2.60
    $$

    Actual option value change:

    $$
    \Delta C = C(105) - C(100) = 7.06 - 3.99 = 3.07
    $$

    Hedging error from pure delta hedge:

    $$
    \text{Error} = \Delta C - \Delta \times \Delta S = 3.07 - 2.60 = 0.47
    $$

    **Step 3: Gamma correction.**

    The gamma correction is:

    $$
    \frac{1}{2}\Gamma(\Delta S)^2 = \frac{1}{2} \times 0.03984 \times 25 = 0.498
    $$

    **Comparison**: The hedging error of $0.47$ is very close to the gamma correction of $0.498$. The small discrepancy arises from higher-order terms (speed, i.e., $\frac{1}{6}\frac{\partial^3 C}{\partial S^3}(\Delta S)^3$ and beyond). This confirms that gamma accounts for the dominant source of hedging error under a pure delta hedge, and delta-gamma hedging would reduce this error to $O((\Delta S)^3)$.

---

**Exercise 2.** In the uncertain volatility model with $\sigma_t \in [\sigma_{\min}, \sigma_{\max}] = [0.15, 0.30]$, the robust price of a European call satisfies the Black-Scholes-Barenblatt PDE. Write down this PDE explicitly and explain why the worst-case volatility is $\sigma_{\max}$ when $\Gamma > 0$ and $\sigma_{\min}$ when $\Gamma < 0$. What is the financial intuition behind this "volatility switching" rule?

??? success "Solution to Exercise 2"

    **The Black-Scholes-Barenblatt (BSB) PDE.**

    Under uncertain volatility $\sigma_t \in [\sigma_{\min}, \sigma_{\max}] = [0.15, 0.30]$, the robust super-replication price $V(S,t)$ satisfies:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\Sigma(\Gamma)^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
    $$

    where the effective (worst-case) volatility $\Sigma(\Gamma)$ is:

    $$
    \Sigma(\Gamma) = \begin{cases} \sigma_{\max} = 0.30 & \text{if } \Gamma = \frac{\partial^2 V}{\partial S^2} > 0 \\ \sigma_{\min} = 0.15 & \text{if } \Gamma = \frac{\partial^2 V}{\partial S^2} < 0 \end{cases}
    $$

    with terminal condition $V(S,T) = (S - K)^+$.

    **Why worst-case volatility switches with the sign of gamma.**

    The super-replication problem seeks the price $V$ such that the hedging portfolio dominates the payoff under **all** volatility scenarios. The PDE arises from the HJB equation:

    $$
    \frac{\partial V}{\partial t} + \sup_{\sigma \in [\sigma_{\min}, \sigma_{\max}]} \left\{\frac{1}{2}\sigma^2 S^2 \Gamma\right\} + rSV_S - rV = 0
    $$

    The supremum selects the volatility that **maximizes** the instantaneous risk to the hedger:

    - **When $\Gamma > 0$** (long gamma, convex payoff region): The term $\frac{1}{2}\sigma^2 S^2 \Gamma$ is positive and increasing in $\sigma$. Higher volatility makes the option more expensive (convexity benefit). Nature chooses $\sigma_{\max}$ to make the option as expensive as possible, forcing the hedger to hold more reserves.

    - **When $\Gamma < 0$** (short gamma, concave payoff region): The term $\frac{1}{2}\sigma^2 S^2 \Gamma$ is negative and becomes more negative as $\sigma$ increases. But the supremum seeks to maximize, so nature chooses $\sigma_{\min}$ to make $\frac{1}{2}\sigma^2 S^2 |\Gamma|$ as small as possible (minimizing the benefit of being in a concave region). Equivalently, $\sigma_{\min}$ makes the negative gamma exposure as costly as possible.

    **Financial intuition**: The hedger faces an adversary (nature) who picks the worst-case volatility at each instant. A long-gamma position benefits from high realized volatility (gamma scalping), so the adversary sets volatility high, making the hedge expensive. A short-gamma position benefits from low realized volatility, so the adversary sets volatility low, maximizing the hedger's losses. This "volatility switching" rule embodies the minimax principle of robust control.

---

**Exercise 3.** Consider delta-gamma hedging a short position in an exotic option using the underlying stock and one vanilla option. Set up the system of equations for the hedge ratios $(\theta_S, \theta_{\text{vanilla}})$ that simultaneously neutralize delta and gamma exposure. Under what conditions is this system solvable, and what residual risks remain after delta-gamma hedging?

??? success "Solution to Exercise 3"

    **Setup**: Short an exotic option with value $V^{\text{exotic}}(S,t)$, hedging with the underlying stock and a vanilla option $O(S,t)$.

    Denote:

    - Exotic Greeks: $\Delta_E = \frac{\partial V^{\text{exotic}}}{\partial S}$, $\Gamma_E = \frac{\partial^2 V^{\text{exotic}}}{\partial S^2}$
    - Vanilla Greeks: $\Delta_O = \frac{\partial O}{\partial S}$, $\Gamma_O = \frac{\partial^2 O}{\partial S^2}$
    - Hedge positions: $\theta_S$ shares of stock, $\theta_O$ units of vanilla option

    **Delta-neutral condition** (total portfolio delta equals zero):

    $$
    -\Delta_E + \theta_S + \theta_O \Delta_O = 0
    $$

    **Gamma-neutral condition** (total portfolio gamma equals zero):

    $$
    -\Gamma_E + \theta_O \Gamma_O = 0
    $$

    Note: stock has zero gamma, so only the option contributes.

    **Solving the system.**

    From the gamma-neutral condition:

    $$
    \theta_O = \frac{\Gamma_E}{\Gamma_O}
    $$

    Substituting into the delta-neutral condition:

    $$
    \theta_S = \Delta_E - \theta_O \Delta_O = \Delta_E - \frac{\Gamma_E}{\Gamma_O}\Delta_O
    $$

    **Solvability condition**: The system is solvable if and only if $\Gamma_O \neq 0$, i.e., the hedging option has nonzero gamma. This is satisfied by any option that is not at expiry and not deeply in/out of the money. In particular:

    - A vanilla call or put with reasonable moneyness has $\Gamma_O > 0$.
    - A forward contract has $\Gamma_O = 0$ and cannot be used for gamma hedging.

    **Residual risks after delta-gamma hedging.**

    Even with perfect delta-gamma neutrality, the following risks remain:

    1. **Vega risk**: Sensitivity to volatility changes, $\mathcal{V} = \partial V / \partial \sigma$. The exotic and vanilla generally have different vegas, so the portfolio is not vega-neutral.
    2. **Third-order risk (speed)**: $\frac{\partial^3 V}{\partial S^3}(\Delta S)^3$ terms become relevant for large moves.
    3. **Cross-gamma (vanna)**: $\frac{\partial^2 V}{\partial S \partial \sigma}$ captures the interaction between spot and volatility moves.
    4. **Theta mismatch**: Different time decays of the exotic and vanilla create P&L over time.
    5. **Discrete rebalancing error**: In practice, the hedge is adjusted at discrete times, creating residual gamma exposure between rebalances.
    6. **Model risk**: The Greeks themselves depend on the assumed model; misspecification introduces systematic hedging errors.

    To also neutralize vega would require a third instrument (e.g., another option with a different strike or maturity), leading to a $3 \times 3$ system.

---

**Exercise 4.** Formulate the robust delta-gamma hedging problem as a minimax optimization:

$$
\min_{\Delta, \phi} \max_{\sigma \in [\sigma_{\min}, \sigma_{\max}]} \mathbb{E}_\sigma\left[\left(V_T - \Delta S_T - \phi \cdot C_T^{\text{hedge}} - V_0 + \Delta S_0 + \phi C_0^{\text{hedge}}\right)^2\right]
$$

where $\phi$ is the position in a hedging option. Explain the trade-off between hedging accuracy and the width of the volatility uncertainty band.

??? success "Solution to Exercise 4"

    **Formulation**: The robust delta-gamma hedging problem is the minimax optimization:

    $$
    \min_{\Delta, \phi} \max_{\sigma \in [\sigma_{\min}, \sigma_{\max}]} \mathbb{E}_\sigma\left[\left(V_T - \Delta S_T - \phi C_T^{\text{hedge}} - V_0 + \Delta S_0 + \phi C_0^{\text{hedge}}\right)^2\right]
    $$

    **Interpretation**: The hedger (minimizer) chooses the delta position $\Delta$ and the option position $\phi$ to minimize the worst-case expected squared hedging error, where nature (maximizer) chooses the volatility $\sigma$ adversarially from the uncertainty band.

    **Analysis of the trade-off.**

    The hedging error over one period can be approximated by Taylor expansion:

    $$
    V_{t+\delta t} - V_t \approx \Delta_V \Delta S + \frac{1}{2}\Gamma_V (\Delta S)^2 + \Theta_V \delta t
    $$

    After delta-gamma hedging (subtracting $\Delta \cdot \Delta S + \phi \cdot \Delta O$):

    $$
    \text{Error} \approx \frac{1}{2}(\Gamma_V - \phi \Gamma_O)(\Delta S)^2 + (\Theta_V - \phi \Theta_O)\delta t + \text{vega terms}
    $$

    With perfect gamma neutralization ($\phi = \Gamma_V / \Gamma_O$), the dominant residual error comes from:

    $$
    \text{Error} \approx (\Theta_V - \phi \Theta_O)\delta t + (\mathcal{V}_V - \phi \mathcal{V}_O)\Delta\sigma + \text{higher order}
    $$

    The worst-case $\sigma$ enters through $\mathbb{E}_\sigma[(\Delta S)^2] = \sigma^2 S^2 \delta t$ and through the vega terms. As the uncertainty band $[\sigma_{\min}, \sigma_{\max}]$ widens:

    - The worst-case $\mathbb{E}_\sigma[(\Delta S)^2]$ increases (wider range of possible moves), making gamma hedging more important.
    - The vega mismatch $(\mathcal{V}_V - \phi \mathcal{V}_O)\Delta\sigma$ can be larger, as the range of $\Delta\sigma$ is wider.
    - The optimal $\phi$ may deviate from the simple ratio $\Gamma_V/\Gamma_O$ to partially hedge vega at the cost of imperfect gamma neutralization.

    **The fundamental trade-off**: With a narrow volatility band, delta-gamma hedging is nearly sufficient. With a wide band, the hedger must either:

    (a) Accept larger residual vega risk (if only two instruments are available), or
    (b) Add more hedging instruments to neutralize additional Greeks, increasing transaction costs, or
    (c) Over-hedge gamma/vega to be robust, at the cost of efficiency when volatility is near the midpoint.

    The minimax solution represents the optimal compromise: the hedge that performs best in the worst-case volatility scenario.

---

**Exercise 5.** A trader holds a portfolio with delta $\Delta_P = 50$, gamma $\Gamma_P = -3$, and vega $\mathcal{V}_P = -200$. Available hedging instruments are the underlying stock ($\Delta = 1$, $\Gamma = 0$, $\mathcal{V} = 0$) and a vanilla call ($\Delta_C = 0.55$, $\Gamma_C = 0.025$, $\mathcal{V}_C = 18$). Compute the hedge ratios that neutralize delta and gamma. Is it possible to also neutralize vega with only two instruments? What additional instrument would be needed?

??? success "Solution to Exercise 5"

    **Given portfolio Greeks**: $\Delta_P = 50$, $\Gamma_P = -3$, $\mathcal{V}_P = -200$.

    **Hedging instruments**:

    - Stock: $\Delta_S = 1$, $\Gamma_S = 0$, $\mathcal{V}_S = 0$
    - Vanilla call: $\Delta_C = 0.55$, $\Gamma_C = 0.025$, $\mathcal{V}_C = 18$

    Let $n_S$ = number of shares of stock and $n_C$ = number of vanilla calls.

    **Step 1: Gamma neutralization.**

    The total portfolio gamma (including hedges) must be zero:

    $$
    \Gamma_P + n_C \Gamma_C = 0 \implies -3 + n_C \times 0.025 = 0 \implies n_C = \frac{3}{0.025} = 120
    $$

    We need to buy 120 vanilla calls.

    **Step 2: Delta neutralization.**

    After adding the calls, the total delta is:

    $$
    \Delta_P + n_S \Delta_S + n_C \Delta_C = 0 \implies 50 + n_S + 120 \times 0.55 = 0
    $$

    $$
    50 + n_S + 66 = 0 \implies n_S = -116
    $$

    We need to short 116 shares of stock.

    **Step 3: Check vega.**

    The remaining portfolio vega is:

    $$
    \mathcal{V}_{\text{total}} = \mathcal{V}_P + n_C \mathcal{V}_C + n_S \mathcal{V}_S = -200 + 120 \times 18 + (-116) \times 0 = -200 + 2160 = 1960
    $$

    The vega is **not** neutralized --- in fact, it has flipped from $-200$ to $+1960$.

    **Can we neutralize vega with two instruments?**

    No. With two instruments (stock and one vanilla call), we have two degrees of freedom ($n_S, n_C$) and three constraints (delta, gamma, vega). The system is overdetermined:

    $$
    \begin{pmatrix} 1 & 0.55 \\ 0 & 0.025 \\ 0 & 18 \end{pmatrix} \begin{pmatrix} n_S \\ n_C \end{pmatrix} = \begin{pmatrix} -50 \\ 3 \\ 200 \end{pmatrix}
    $$

    The gamma equation forces $n_C = 120$, but then the vega equation requires $n_C = 200/18 = 11.1$, which contradicts. There is no solution satisfying all three constraints simultaneously.

    **Additional instrument needed**: To neutralize all three Greeks, we need a third instrument --- for example, a second vanilla option $O_2$ with Greeks $(\Delta_2, \Gamma_2, \mathcal{V}_2)$ where $\Gamma_2$ and $\mathcal{V}_2$ are linearly independent of those of the first call. A natural choice would be:

    - An option at a different strike (different gamma-to-vega ratio)
    - An option at a different maturity (longer-dated options have higher vega relative to gamma)
    - A variance swap (pure vega exposure with zero delta and near-zero gamma)

    With three instruments, the system becomes $3 \times 3$ and is generically solvable.

---

**Exercise 6.** Derive the leading-order hedging error for a delta-gamma hedge that is rebalanced at discrete intervals $\delta t$. Show that the error is of order $O((\delta t)^{3/2})$ for a delta-gamma hedge, compared to $O((\delta t)^{1/2})$ for a pure delta hedge. Explain why this makes gamma hedging especially valuable when rebalancing frequency is limited.

??? success "Solution to Exercise 6"

    **Pure delta hedge: error of order $O((\delta t)^{1/2})$.**

    For a delta-hedged portfolio rebalanced at intervals $\delta t$, the hedging error over one period is dominated by the gamma term:

    $$
    \text{Error per step} = \frac{1}{2}\Gamma S^2 \left[(\Delta S)^2 - \sigma^2 S^2 \delta t\right]
    $$

    where $(\Delta S)^2 = \sigma^2 S^2 \delta t + O((\delta t)^{3/2})$ (from Brownian scaling). The variance of $(\Delta S)^2$ is:

    $$
    \text{Var}[(\Delta S)^2] = \mathbb{E}[(\Delta S)^4] - (\mathbb{E}[(\Delta S)^2])^2 = 3\sigma^4 S^4 (\delta t)^2 - \sigma^4 S^4 (\delta t)^2 = 2\sigma^4 S^4 (\delta t)^2
    $$

    The error per step has standard deviation $\sim \Gamma S^2 \sigma^2 \delta t$. Over $N = T/\delta t$ steps, the errors are approximately independent, so the total variance is:

    $$
    \text{Var}[\text{Total Error}] \approx N \times \frac{1}{4}\Gamma^2 S^4 \cdot 2\sigma^4 (\delta t)^2 = \frac{T}{\delta t} \times \frac{1}{2}\Gamma^2 S^4 \sigma^4 (\delta t)^2 = \frac{1}{2}\Gamma^2 S^4 \sigma^4 T \delta t
    $$

    Therefore $\text{RMSE} \sim (\delta t)^{1/2}$.

    **Delta-gamma hedge: error of order $O((\delta t)^{3/2})$.**

    With delta-gamma hedging, the second-order term $\frac{1}{2}\Gamma(\Delta S)^2$ is also neutralized. The residual error comes from third-order terms:

    $$
    \text{Error per step} \approx \frac{1}{6}\frac{\partial^3 V}{\partial S^3}(\Delta S)^3 + \text{cross terms involving } \Delta S \cdot \delta t
    $$

    The dominant term is $\frac{1}{6}\text{Speed} \cdot (\Delta S)^3$ where Speed $= \partial^3 V / \partial S^3$.

    Since $\Delta S \sim \sigma S \sqrt{\delta t}$, we have $(\Delta S)^3 \sim \sigma^3 S^3 (\delta t)^{3/2}$. The expected value $\mathbb{E}[(\Delta S)^3] = 0$ (odd moment of Gaussian), so the mean error per step vanishes. The variance of $(\Delta S)^3$ is:

    $$
    \text{Var}[(\Delta S)^3] = \mathbb{E}[(\Delta S)^6] - 0 = 15\sigma^6 S^6 (\delta t)^3
    $$

    Over $N = T/\delta t$ steps:

    $$
    \text{Var}[\text{Total Error}] \approx N \times \frac{1}{36}\text{Speed}^2 S^6 \cdot 15\sigma^6 (\delta t)^3 \sim (\delta t)^2
    $$

    Therefore $\text{RMSE} \sim (\delta t)^1$. More carefully accounting for the cross-term $\frac{\partial^2 V}{\partial S \partial t}\Delta S \cdot \delta t \sim (\delta t)^{3/2}$, the error per step is $O((\delta t)^{3/2})$ and the total RMSE is $O(\delta t)$.

    Actually, let us be more precise. The leading error per step after delta-gamma hedging is $O((\delta t)^{3/2})$, and over $N$ independent steps the total standard deviation is:

    $$
    \text{RMSE}_{\text{total}} \sim \sqrt{N} \times (\delta t)^{3/2} = \sqrt{T/\delta t} \times (\delta t)^{3/2} = \sqrt{T} \cdot (\delta t)
    $$

    So the total RMSE for a delta-gamma hedge scales as $O(\delta t)$, compared to $O(\sqrt{\delta t})$ for a pure delta hedge.

    **Why this matters for limited rebalancing**: The improvement from $O(\sqrt{\delta t})$ to $O(\delta t)$ is dramatic when rebalancing is infrequent. For example, with weekly rebalancing ($\delta t \approx 1/52$):

    - Delta-only RMSE $\propto \sqrt{1/52} \approx 0.139$
    - Delta-gamma RMSE $\propto 1/52 \approx 0.019$

    The delta-gamma hedge reduces the error by a factor of about 7. For monthly rebalancing ($\delta t \approx 1/12$):

    - Delta-only RMSE $\propto \sqrt{1/12} \approx 0.289$
    - Delta-gamma RMSE $\propto 1/12 \approx 0.083$

    The ratio is about 3.5. Thus gamma hedging is especially valuable when rebalancing frequency is constrained --- precisely the regime encountered in practice due to transaction costs and operational limitations.

---

**Exercise 7.** In the presence of both volatility uncertainty $\sigma \in [0.15, 0.30]$ and jump risk (Poisson jumps with intensity $\lambda \in [0, 0.5]$ and jump size $J \sim N(-0.05, 0.03^2)$), discuss how the robust delta-gamma hedging framework extends. What additional Greeks are relevant, and how does the worst-case scenario change when jumps are included?

??? success "Solution to Exercise 7"

    **Extended framework: volatility uncertainty plus jump risk.**

    The underlying dynamics under the worst-case scenario are:

    $$
    \frac{dS_t}{S_{t^-}} = \mu\, dt + \sigma_t\, dW_t + J\, dN_t
    $$

    where $\sigma_t \in [0.15, 0.30]$, $N_t$ is a Poisson process with intensity $\lambda \in [0, 0.5]$, and jump size $J \sim N(-0.05, 0.03^2)$.

    **Extended HJB equation.**

    The robust pricing PDE becomes an integro-differential equation:

    $$
    \frac{\partial V}{\partial t} + \sup_{\sigma, \lambda} \left\{\frac{1}{2}\sigma^2 S^2 V_{SS} + \lambda \mathbb{E}_J[V(S(1+J), t) - V(S,t)] \right\} + rSV_S - (r + \lambda^* \bar{J})V = 0
    $$

    where the supremum is taken over all $\sigma \in [0.15, 0.30]$ and $\lambda \in [0, 0.5]$, and $\bar{J} = \mathbb{E}[J]$.

    **Additional relevant Greeks.**

    Beyond delta, gamma, and vega, the following become important:

    1. **Jump delta** (sensitivity to jump occurrence):

        $$
        \Delta_J = V(S(1+\mathbb{E}[J]), t) - V(S, t)
        $$

        This measures the instantaneous P&L from an average-sized jump.

    2. **Jump gamma** (curvature with respect to jump size):

        $$
        \Gamma_J = \frac{\partial^2}{\partial J^2}\mathbb{E}[V(S(1+J), t)]
        $$

    3. **Lambda sensitivity** (sensitivity to jump intensity):

        $$
        \frac{\partial V}{\partial \lambda} = \mathbb{E}_J[V(S(1+J), t) - V(S, t)] \cdot \frac{\partial V}{\partial (\lambda)}
        $$

    4. **Cross-Greeks**: $\frac{\partial^2 V}{\partial S \partial \sigma}$ (vanna), $\frac{\partial^2 V}{\partial S \partial \lambda}$ (sensitivity of delta to jump intensity).

    **How worst-case changes with jumps.**

    The worst-case scenario analysis becomes more complex:

    **For a long-gamma position** (e.g., long call):

    - Worst-case diffusive volatility: $\sigma = \sigma_{\max} = 0.30$ (as before)
    - Worst-case jump intensity: Depends on the sign of the jump impact $\mathbb{E}_J[V(S(1+J)) - V(S)]$. For an ATM call with downward jumps ($\mathbb{E}[J] = -0.05$), a jump reduces the option value. The adversary maximizes loss by setting $\lambda = \lambda_{\max} = 0.5$.
    - Combined effect: The worst case may involve both high diffusive volatility and frequent downward jumps.

    **For a short-gamma position** (e.g., short straddle):

    - Worst-case diffusive volatility: $\sigma = \sigma_{\min} = 0.15$ (as before, minimizing hedging benefit)
    - Worst-case jump intensity: Jumps cause large instantaneous losses for a short-gamma position (the P&L is approximately $\frac{1}{2}\Gamma S^2 J^2$ per jump, which is negative when short gamma). So $\lambda = \lambda_{\max} = 0.5$.
    - The presence of jumps makes the worst case significantly worse than pure volatility uncertainty alone.

    **Hedging implications.**

    Delta-gamma hedging with diffusive instruments (stock and vanilla options) is insufficient because:

    1. Jumps create instantaneous P&L that cannot be offset by continuous trading.
    2. The jump component $\mathbb{E}_J[V(S(1+J)) - V(S) - JS V_S - \frac{1}{2}J^2 S^2 V_{SS}]$ involves higher-order terms that delta-gamma neutrality does not eliminate.

    **Additional hedges needed**:

    - **OTM puts**: Provide convex protection against downward jumps.
    - **OTM calls**: Protect against upward jumps (less critical given $\mathbb{E}[J] < 0$).
    - **Variance swaps**: Hedge the combined diffusive and jump variance exposure.

    The robust hedging cost increases substantially when jumps are included, because the adversary can now choose both the volatility and the jump intensity to maximize the hedger's losses. This underscores the limitations of delta-gamma hedging in jump-diffusion environments and motivates the use of options (especially tail options) as hedging instruments rather than relying solely on the stock.
