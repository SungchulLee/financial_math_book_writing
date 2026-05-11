# Uncertain Volatility Models


## Introduction


**Uncertain volatility models (UVMs)** provide a rigorous framework for option pricing and hedging when the true volatility of the underlying asset is unknown or uncertain. Rather than assuming a specific volatility parameter or stochastic volatility model, UVMs consider a **range** or **set** of possible volatilities and seek prices and hedging strategies that are **robust** to this uncertainty.

The seminal work of Avellaneda, Levy, and Parás (1995) established the mathematical foundations of uncertain volatility models, showing that:

1. Robust super-replication prices satisfy **fully nonlinear PDEs**
2. Optimal hedging strategies can be characterized explicitly
3. Market bid-ask spreads can be explained by volatility uncertainty

This framework has profound implications for:

- **Model-free pricing**: Deriving bounds without specifying dynamics
- **Robust hedging**: Strategies that work across volatility scenarios
- **Risk management**: Quantifying model risk
- **Regulatory capital**: Computing capital requirements under model uncertainty

## Mathematical Framework


### 1. Setup


**Asset Price Dynamics**: The underlying asset $S_t$ follows:


$$
dS_t = \mu S_t \, dt + \sigma_t S_t \, dW_t
$$



where:

- $\mu$: Drift (unimportant for pricing under risk-neutrality)
- $\sigma_t$: Instantaneous volatility (uncertain)
- $W_t$: Brownian motion

**Volatility Uncertainty**: The true volatility is unknown but constrained:


$$
\underline{\sigma} \leq \sigma_t \leq \overline{\sigma}
$$



**Key Assumption**: No assumptions on $\sigma_t$ dynamics; could be deterministic, stochastic, path-dependent, etc.

### 2. Hedging Portfolio


**Portfolio**: At time $t$, hold $\Delta_t$ shares of stock.

**Value Process**: Starting with $V_0$, the portfolio evolves:


$$
dV_t = \Delta_t \, dS_t + (V_t - \Delta_t S_t) r \, dt
$$



where $r$ is the risk-free rate.

**Self-Financing**: The strategy is self-financing (no additional capital injections).

**Goal**: Choose $V_0$ and $\Delta_t$ such that:


$$
V_T \geq \Phi(S_T) \quad \text{for all admissible volatility paths } \{\sigma_t\}_{t \in [0,T]}
$$



## Avellaneda-Levy-Parás Model


### 1. Super-Replication Price


**Definition**: The **super-replication price** $V^{\text{sup}}(S_0)$ is the minimal initial capital required to construct a hedging portfolio that dominates the option payoff under all volatility scenarios:


$$
V^{\text{sup}}(S_0) = \inf \left\{ V_0: \exists \Delta_t \text{ s.t. } V_T \geq \Phi(S_T) \text{ for all } \sigma_t \in [\underline{\sigma}, \overline{\sigma}] \right\}
$$



**Interpretation**: Conservative pricing from seller's perspective.

### 2. Sub-Replication Price


**Definition**: The **sub-replication price** $V^{\text{sub}}(S_0)$ is the maximal initial capital from which a portfolio can be constructed that is dominated by the option payoff:


$$
V^{\text{sub}}(S_0) = \sup \left\{ V_0: \exists \Delta_t \text{ s.t. } V_T \leq \Phi(S_T) \text{ for all } \sigma_t \in [\underline{\sigma}, \overline{\sigma}] \right\}
$$



**Interpretation**: Aggressive pricing from buyer's perspective.

### 3. Bid-Ask Spread


**Arbitrage-Free Range**: The interval:


$$
[V^{\text{sub}}(S_0), V^{\text{sup}}(S_0)]
$$



represents the range of arbitrage-free prices under volatility uncertainty.

**Spread Width**: The bid-ask spread is:


$$
\text{Spread} = V^{\text{sup}}(S_0) - V^{\text{sub}}(S_0)
$$



**Factors**:

- Increases with $\overline{\sigma} - \underline{\sigma}$ (uncertainty range)
- Increases with option gamma exposure
- Increases with time to maturity

## Fully Nonlinear PDE


### 1. Black-Scholes-Barenblatt Equation


**Theorem** (Avellaneda-Parás): The super-replication price $V^{\text{sup}}(t, S)$ satisfies the **Black-Scholes-Barenblatt (BSB) equation**:


$$
\frac{\partial V}{\partial t} + rS \frac{\partial V}{\partial S} + \frac{1}{2} \bar{\sigma}^2(V) S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0
$$



with terminal condition $V(T, S) = \Phi(S)$, where:


$$
\bar{\sigma}^2(V) = \begin{cases}
\overline{\sigma}^2 & \text{if } \frac{\partial^2 V}{\partial S^2} > 0 \\
\underline{\sigma}^2 & \text{if } \frac{\partial^2 V}{\partial S^2} < 0
\end{cases}
$$



**Proof Sketch**: 

1. Dynamic programming principle: $V$ is the value function
2. Apply Itô's formula to $V(t, S_t)$
3. Choose $\sigma_t$ adversarially to maximize/minimize $\frac{\partial^2 V}{\partial S^2}$
4. Obtain nonlinear PDE

**Nonlinearity**: The coefficient $\bar{\sigma}^2(V)$ depends on the **sign of gamma**, making this fully nonlinear.

### 2. Viscosity Solutions


**Definition**: Since $V$ may not be $C^2$ (especially at strike for digital options), solutions are understood in the **viscosity sense**.

**Viscosity Solution**: A function $V$ satisfying:

- At smooth points: PDE holds classically
- At non-smooth points: Comparison with test functions

**Uniqueness**: The viscosity solution is unique, ensuring well-posedness.

**Comparison Principle**: If $V_1$ and $V_2$ are respectively sub- and supersolutions with $V_1(T, \cdot) \leq V_2(T, \cdot)$, then $V_1 \leq V_2$ everywhere.

### 3. Examples


**Example 1** (European Call): For $\Phi(S) = (S - K)^+$:

- The call has $\Gamma = \frac{\partial^2 C}{\partial S^2} > 0$ everywhere (except boundaries)
- Use $\sigma = \overline{\sigma}$ uniformly
- Super-replication price:

  $$
  V^{\text{sup}}(S_0) = \text{BS}(S_0, K, \overline{\sigma}, T)
  $$



**Example 2** (European Put): For $\Phi(S) = (K - S)^+$:

- The put has $\Gamma > 0$ everywhere (positive gamma)
- Use $\sigma = \overline{\sigma}$ uniformly
- Super-replication price:

  $$
  V^{\text{sup}}(S_0) = \text{BS-Put}(S_0, K, \overline{\sigma}, T)
  $$



**Example 3** (Digital Option): For $\Phi(S) = \mathbb{1}_{\{S > K\}}$:

- Gamma is infinite (Dirac delta) at $S = K$
- For $S < K$: $\Gamma < 0$ → Use $\underline{\sigma}$
- For $S > K$: $\Gamma > 0$ → Use $\overline{\sigma}$
- Discontinuous solution at $S = K$

**Example 4** (Butterfly Spread): For $\Phi(S) = \max(0, S - K_1) - 2\max(0, S - K_2) + \max(0, S - K_3)$:

- Piecewise linear payoff
- Gamma alternates sign in different regions
- Volatility switches at strikes

## Optimal Hedging Strategy


### 1. Delta Hedging


**Theorem**: The optimal hedging strategy is:


$$
\Delta_t^* = \frac{\partial V}{\partial S}(t, S_t)
$$



where $V$ is the super-replication price.

**Proof**: By construction, $V(t, S_t)$ is a supermartingale under worst-case volatility. The delta position makes the portfolio self-financing.

**Interpretation**: Classic delta-hedging, but using value function from nonlinear PDE.

### 2. Gamma Adjustment


**Gamma Exposure**: The residual gamma exposure is:


$$
\Gamma_t = \frac{\partial^2 V}{\partial S^2}(t, S_t)
$$



**Worst-Case Volatility**: At each instant, nature chooses:


$$
\sigma_t^* = \begin{cases}
\overline{\sigma} & \text{if } \Gamma_t > 0 \\
\underline{\sigma} & \text{if } \Gamma_t < 0
\end{cases}
$$



**Accumulated Cost**: The total gamma cost over hedging period is:


$$
\text{Cost} = \frac{1}{2} \int_0^T \Gamma_t \sigma_t^2 S_t^2 \, dt
$$



### 3. Vega Hedging


**Question**: Can we hedge against volatility uncertainty using options?

**Additional Instruments**: Hold portfolio of options $\{O_i\}_{i=1}^n$ with different strikes.

**Enhanced Hedging**: 


$$
\Pi_t = V_t + \sum_{i=1}^n \theta_i^t O_i(t, S_t)
$$



**Gamma Neutralization**: Choose $\{\theta_i\}$ to make:


$$
\frac{\partial^2 \Pi}{\partial S^2} = 0
$$



**Cost-Benefit**: Gamma hedging reduces uncertainty but requires purchasing options (expensive).

## Extensions and Generalizations


### 1. Path-Dependent Options


**Asian Options**: Payoff depends on average:


$$
\Phi = \left(\frac{1}{T} \int_0^T S_t \, dt - K\right)^+
$$



**State Variables**: $(t, S, A)$ where $A_t = \int_0^t S_u \, du$.

**PDE**: Higher-dimensional BSB equation:


$$
\frac{\partial V}{\partial t} + S \frac{\partial V}{\partial A} + rS \frac{\partial V}{\partial S} + \frac{1}{2} \bar{\sigma}^2(V) S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0
$$



**Complexity**: Increases with dimension; numerical methods required.

### 2. Barrier Options


**Knock-Out Call**: Payoff is:


$$
\Phi = (S_T - K)^+ \mathbb{1}_{\{\max_{0 \leq t \leq T} S_t < H\}}
$$



**Challenge**: Near barrier, gamma can be very large.

**BSB Equation**: With barrier at $S = H$:


$$
V(t, H) = 0 \quad \text{(boundary condition)}
$$



**Volatility Choice**: 

- Far from barrier: Use volatility based on gamma sign
- Near barrier: Critical region where hedging is difficult

### 3. American Options


**Early Exercise**: Holder can exercise at any time $\tau \leq T$:


$$
\Phi = \sup_{0 \leq \tau \leq T} e^{-r\tau} g(S_{\tau})
$$



**Variational Inequality**: The value function satisfies:


$$
\min\left\{ \frac{\partial V}{\partial t} + rS \frac{\partial V}{\partial S} + \frac{1}{2} \bar{\sigma}^2(V) S^2 \frac{\partial^2 V}{\partial S^2} - rV, \, V - g(S) \right\} = 0
$$



**Exercise Boundary**: Define free boundary $S^*(t)$ where $V(t, S^*(t)) = g(S^*(t))$.

**Optimal Exercise**: Exercise when $S_t$ hits boundary $S^*(t)$.

### 4. Lookback Options


**Payoff**: Depends on running maximum:


$$
\Phi = M_T - K \quad \text{where } M_t = \max_{0 \leq s \leq t} S_s
$$



**State Space**: $(t, S, M)$ with $M \geq S$.

**PDE**: 


$$
\frac{\partial V}{\partial t} + rS \frac{\partial V}{\partial S} + \frac{1}{2} \bar{\sigma}^2(V) S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0
$$



with boundary condition $V(t, M, M) = $ continuously updated.

## Multi-Asset Case


### 1. Basket Options


**Assets**: $\mathbf{S}_t = (S_t^{(1)}, \ldots, S_t^{(n)})$

**Dynamics**:


$$
dS_t^{(i)} = \mu_i S_t^{(i)} \, dt + \sigma_t^{(i)} S_t^{(i)} \, dW_t^{(i)}
$$



**Correlation Uncertainty**: Cross-correlations $\rho_{ij}(t) \in [\underline{\rho}_{ij}, \overline{\rho}_{ij}]$.

### 2. Nonlinear PDE


**Hessian Matrix**: Let $\mathbf{H} = D^2 V$ (Hessian of $V$ in $\mathbf{S}$).

**BSB Equation**:


$$
\frac{\partial V}{\partial t} + \mathbf{r} \cdot \mathbf{S} \odot \nabla V + \sup_{\boldsymbol{\Sigma} \in \mathcal{S}} \left\{ \frac{1}{2} \text{tr}[\boldsymbol{\Sigma} \mathbf{S} \mathbf{S}^\top \odot \mathbf{H}] \right\} - rV = 0
$$



where:

- $\boldsymbol{\Sigma} = (\sigma_{ij})$: Covariance matrix
- $\mathcal{S}$: Set of admissible covariance matrices
- $\odot$: Element-wise multiplication

**Optimal Covariance**: Chosen to maximize the quadratic form $\text{tr}[\boldsymbol{\Sigma} \mathbf{H}]$ subject to constraints.

### 3. Correlation Bounds


**Fréchet-Hoeffding Bounds**: For marginals with volatilities $\{\sigma_i\}$:


$$
\max\left\{-1, \sum_{i \neq j} \frac{\sigma_i \sigma_j}{\sigma_i^2 + \sigma_j^2} - (n-1)\right\} \leq \rho_{ij} \leq 1
$$



**Semidefinite Constraint**: The correlation matrix $\boldsymbol{\rho}$ must be positive semidefinite.

**Optimization**: Solve:


$$
\sup_{\boldsymbol{\rho} \in \mathcal{R}} \text{tr}[\boldsymbol{\rho} \odot \mathbf{H}]
$$



where $\mathcal{R}$ is the set of valid correlation matrices.

## Numerical Methods


### 1. Finite Difference Schemes


**Grid**: Discretize $(t, S)$ space:

- Time: $t \in \{0, \Delta t, 2\Delta t, \ldots, T\}$
- Space: $S \in \{S_{\min}, S_{\min} + \Delta S, \ldots, S_{\max}\}$

**Scheme**: At each grid point $(t_i, S_j)$:


$$
\frac{V_j^{i+1} - V_j^i}{\Delta t} + rS_j \frac{V_{j+1}^i - V_{j-1}^i}{2\Delta S} + \frac{1}{2} \bar{\sigma}^2(\Gamma_j^i) S_j^2 \frac{V_{j+1}^i - 2V_j^i + V_{j-1}^i}{(\Delta S)^2} - rV_j^i = 0
$$



where:


$$
\Gamma_j^i = \frac{V_{j+1}^i - 2V_j^i + V_{j-1}^i}{(\Delta S)^2}
$$



**Volatility Selection**: At each point, use:


$$
\bar{\sigma}^2(\Gamma_j^i) = \begin{cases}
\overline{\sigma}^2 & \text{if } \Gamma_j^i > 0 \\
\underline{\sigma}^2 & \text{if } \Gamma_j^i < 0
\end{cases}
$$



**Monotone Schemes**: Ensure convergence to viscosity solution by using upwind schemes.

### 2. Monte Carlo Simulation


**Challenge**: Direct Monte Carlo is difficult due to supremum over volatilities.

**Approach**: For each simulated path:

1. At each time step, observe $S_t$ and $\Gamma_t$
2. Choose $\sigma_t$ adversarially based on $\text{sign}(\Gamma_t)$
3. Continue simulation to maturity
4. Average over paths

**Least-Squares Monte Carlo**: Estimate continuation values using regression:


$$
V(t, S) \approx \sum_{k=1}^K \beta_k \phi_k(S)
$$



**Complexity**: $O(M \cdot N)$ where $M$ is number of paths, $N$ is time steps.

### 3. Policy Iteration


**Algorithm**:

1. **Initialize**: Guess volatility policy $\sigma^{(0)}(t, S)$
2. **Solve PDE**: Compute $V^{(k)}$ solving linear PDE with $\sigma = \sigma^{(k)}$
3. **Update Policy**: Set:

   $$
   \sigma^{(k+1)}(t, S) = \begin{cases}
   \overline{\sigma} & \text{if } \frac{\partial^2 V^{(k)}}{\partial S^2} > 0 \\
   \underline{\sigma} & \text{if } \frac{\partial^2 V^{(k)}}{\partial S^2} < 0
   \end{cases}
   $$


4. **Iterate**: Repeat until convergence $\|V^{(k+1)} - V^{(k)}\| < \epsilon$

**Convergence**: Monotone convergence to viscosity solution.

## Calibration and Market Data


### 1. Implied Volatility Bounds


**Market Information**: Observed call prices $\{C(K_i, T_j)\}$ at various strikes and maturities.

**Implied Volatility**: For each option, compute:


$$
\sigma_{\text{imp}}(K, T) = \text{BS}^{-1}(C(K, T), S_0, K, r, T)
$$



**Volatility Bounds**: Set:


$$
\underline{\sigma}(t) = \min_{K, T} \sigma_{\text{imp}}(K, T), \quad \overline{\sigma}(t) = \max_{K, T} \sigma_{\text{imp}}(K, T)
$$



**Refinement**: Use smile dynamics to infer time-varying bounds $\underline{\sigma}(t)$, $\overline{\sigma}(t)$.

### 2. Historical Volatility


**Realized Volatility**: Compute from historical returns:


$$
\hat{\sigma} = \sqrt{\frac{252}{n} \sum_{i=1}^n \log^2\left(\frac{S_{t_i}}{S_{t_{i-1}}}\right)}
$$



**Bounds**: Use historical range:


$$
\underline{\sigma} = \hat{\sigma} - k \cdot \text{std}(\sigma_{\text{hist}}), \quad \overline{\sigma} = \hat{\sigma} + k \cdot \text{std}(\sigma_{\text{hist}})
$$



for some confidence level $k$.

### 3. Combining Information


**Hybrid Approach**: Combine implied and historical:


$$
\underline{\sigma} = \min\{\sigma_{\text{imp}}^{\min}, \sigma_{\text{hist}}^{\min}\}, \quad \overline{\sigma} = \max\{\sigma_{\text{imp}}^{\max}, \sigma_{\text{hist}}^{\max}\}
$$



**Judgment**: Analyst judgment based on market conditions, regime shifts, etc.

## Model Risk and Stress Testing


### 1. Model Risk Quantification


**Definition**: The difference between model price and robust price:


$$
\text{Model Risk} = V^{\text{sup}} - V^{\text{model}}
$$



**Interpretation**: Additional capital required to protect against model misspecification.

### 2. Stress Testing


**Scenarios**: Test portfolio under extreme volatility scenarios:

1. **Vol Spike**: $\sigma \to \overline{\sigma}$ suddenly
2. **Vol Crash**: $\sigma \to \underline{\sigma}$ suddenly
3. **Time-Varying**: $\sigma_t$ follows worst-case path

**P&L Impact**: Compute:


$$
\text{P&L}_{\text{stress}} = V(T, S_T^{\text{stress}}) - V_0 - \int_0^T \Delta_t \, dS_t^{\text{stress}}
$$



**Worst-Case Loss**: Maximum loss over all scenarios:


$$
\text{WCL} = \sup_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} \text{Loss}(\sigma)
$$



### 3. Value-at-Risk (VaR)


**Standard VaR**: Under specific model $\mathcal{M}$:


$$
\text{VaR}_{\alpha}^{\mathcal{M}} = \inf\{v: P^{\mathcal{M}}(\text{Loss} > v) \leq \alpha\}
$$



**Robust VaR**: Over model class:


$$
\text{VaR}_{\alpha}^{\text{robust}} = \sup_{\mathcal{M} \in \text{Model Class}} \text{VaR}_{\alpha}^{\mathcal{M}}
$$



**Conservatism**: Robust VaR accounts for model uncertainty, yielding higher capital requirements.

## Comparison with Stochastic Volatility Models


### 1. Heston Model


**Dynamics**: 


$$
dS_t = \mu S_t \, dt + \sqrt{V_t} S_t \, dW_t^S, \quad dV_t = \kappa(\theta - V_t) \, dt + \xi \sqrt{V_t} \, dW_t^V
$$



**Known Parameters**: Assumes specific mean-reversion $\kappa$, long-run mean $\theta$, vol-of-vol $\xi$.

**Comparison**: Heston is **parametric** and **specific**, while UVM is **nonparametric** and **robust**.

### 2. Local Volatility


**Model**: $\sigma = \sigma(S, t)$ determined from market prices via Dupire's formula.

**Certainty**: Assumes specific, deterministic volatility function.

**Comparison**: Local volatility is **model-complete** but not robust to misspecification; UVM provides bounds.

### 3. SABR Model


**Dynamics**:


$$
dF_t = \alpha_t F_t^{\beta} \, dW_t^1, \quad d\alpha_t = \nu \alpha_t \, dW_t^2
$$



**Usage**: Widely used for FX and interest rate options.

**Comparison**: SABR specifies stochastic dynamics; UVM only specifies bounds.

### 4. Pros and Cons


| **Model** | **Pros** | **Cons** |
|-----------|----------|----------|
| **UVM** | Model-free, robust, conservative | Wide spreads, conservative pricing |
| **Heston** | Tractable, explicit formulas | Requires parameter estimation, model risk |
| **Local Vol** | Matches market prices exactly | No smile dynamics, deterministic |
| **SABR** | Captures smile dynamics, popular | Parameter instability, calibration challenges |

## Applications in Practice


### 1. Market Making


**Two-Way Quotes**: Provide bid and ask prices:

- **Bid**: $V^{\text{sub}}$ (buying from client)
- **Ask**: $V^{\text{sup}}$ (selling to client)

**Spread**: Reflects volatility uncertainty:


$$
\text{Spread} = V^{\text{sup}} - V^{\text{sub}}
$$



**Inventory Management**: Adjust spreads based on position (long/short gamma).

### 2. Exotic Derivatives Desk


**Structured Products**: Price complex payoffs using UVM framework.

**Example** (Worst-of Basket):


$$
\Phi = \min_{i=1, \ldots, n} S_T^{(i)} - K
$$



**Hedging**: Use UVM to compute robust hedges in each underlying and correlation.

**Risk**: Quantify model risk using spread width.

### 3. Risk Management


**Regulatory Capital**: Basel III requires quantification of model risk:


$$
\text{Model Risk Capital} = V^{\text{sup}} - V^{\text{expected}}
$$



**Internal Models**: Banks use UVM to stress-test trading book.

**Backtesting**: Compare realized P&L against robust bounds to validate assumptions.

## Advanced Topics


### 1. Uncertain Jump Risk


**Dynamics**: Add jump component:


$$
dS_t = \mu S_t \, dt + \sigma_t S_t \, dW_t + S_{t-} \, dJ_t
$$



where $J_t$ is a jump process with uncertain intensity $\lambda \in [\underline{\lambda}, \overline{\lambda}]$.

**PIDE**: Pricing satisfies partial integro-differential equation (PIDE):


$$
\frac{\partial V}{\partial t} + \mathcal{L}V + \sup_{\lambda \in [\underline{\lambda}, \overline{\lambda}]} \left\{ \lambda \int (V(t, Sy) - V(t, S)) \nu(dy) \right\} = 0
$$



where $\nu$ is the jump size distribution.

**Complexity**: Numerical solution requires discretization of integral term.

### 2. Time-Dependent Bounds


**Time-Varying Uncertainty**:


$$
\underline{\sigma}(t) \leq \sigma_t \leq \overline{\sigma}(t)
$$



**PDE**: Coefficient becomes time-dependent:


$$
\frac{\partial V}{\partial t} + rS \frac{\partial V}{\partial S} + \frac{1}{2} \bar{\sigma}^2(t, V) S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0
$$



**Application**: Models regime shifts, earnings announcements, macroeconomic releases.

### 3. Transaction Costs


**Proportional Costs**: Each trade costs $\lambda |$quantity$| \times$ price.

**Modified PDE**: Includes nonlinear terms from costs:


$$
\frac{\partial V}{\partial t} + rS \frac{\partial V}{\partial S} + \frac{1}{2} \bar{\sigma}^2(V) S^2 \frac{\partial^2 V}{\partial S^2} - \lambda S \left|\frac{\partial V}{\partial S}\right| - rV = 0
$$



**Interpretation**: Transaction costs increase super-replication price.

### 4. Interest Rate Uncertainty


**Stochastic Rates**: Uncertain short rate $r_t \in [\underline{r}, \overline{r}]$.

**Discount Factor**: Affects pricing through:


$$
\exp\left(-\int_0^T r_s \, ds\right)
$$



**Joint Uncertainty**: Both volatility and interest rate uncertain.

**Dimension**: Increases state space dimension, making numerical solution more challenging.

## Research Directions


### 1. Deep Learning for UVMs


**Neural Network Approximation**: Represent value function:


$$
V(t, S) \approx f_{\theta}(t, S)
$$



**Training**: Minimize PDE residual:


$$
\mathcal{L}(\theta) = \mathbb{E}\left[\left|\frac{\partial f_{\theta}}{\partial t} + rS \frac{\partial f_{\theta}}{\partial S} + \frac{1}{2} \bar{\sigma}^2(f_{\theta}) S^2 \frac{\partial^2 f_{\theta}}{\partial S^2} - rf_{\theta}\right|^2\right]
$$



**Advantages**: Handles high dimensions, bypasses curse of dimensionality.

### 2. Data-Driven Calibration


**Machine Learning**: Learn volatility bounds from data:

- Supervised learning: Predict $[\underline{\sigma}, \overline{\sigma}]$ from market features
- Reinforcement learning: Optimal hedging strategies under UVM

**Online Learning**: Update bounds dynamically as new data arrives.

### 3. Rough Volatility


**Fractional Brownian Motion**: Volatility with Hurst exponent $H < 1/2$:


$$
\sigma_t = f\left(\int_0^t (t-s)^{H-1/2} dW_s\right)
$$



**UVM Extension**: Bounds on rough volatility:


$$
\underline{H} \leq H_t \leq \overline{H}
$$



**Challenge**: Requires rough path theory for rigorous treatment.

## Summary and Key Insights


### 1. Fundamental Results


1. **Fully Nonlinear PDEs**: Robust pricing under volatility uncertainty leads to Black-Scholes-Barenblatt equation.

2. **Viscosity Solutions**: Generalized notion of solution handles non-smooth payoffs and discontinuous coefficients.

3. **Optimal Hedging**: Delta-hedging with value function from nonlinear PDE is optimal.

4. **Bid-Ask Spreads**: Market spreads can be explained by volatility uncertainty and gamma exposure.

5. **Model-Free Bounds**: Provides rigorous bounds without specifying volatility dynamics.

### 2. Practical Implications


**For Traders**:

- Robust pricing: conservative but safe
- Hedging: model-free delta strategies
- Market making: natural bid-ask spreads

**For Risk Managers**:

- Model risk quantification
- Stress testing frameworks
- Regulatory capital calculations

**For Researchers**:

- Connection to fully nonlinear PDEs
- Viscosity solution theory
- Robust optimization frameworks

### 3. Theoretical Significance


Uncertain volatility models bridge:

- **Stochastic Analysis**: BSDEs and martingale theory
- **PDE Theory**: Fully nonlinear equations and viscosity solutions
- **Optimization**: Robust control and minimax problems
- **Finance**: Pricing, hedging, and risk management

The UVM framework represents a cornerstone of robust quantitative finance, providing rigorous mathematical foundations for handling model uncertainty while maintaining practical applicability in derivative pricing, hedging, and risk management.

---

## Exercises

**Exercise 1.** Consider the Black-Scholes-Barenblatt equation for an uncertain volatility model with $\sigma \in [\underline{\sigma}, \overline{\sigma}] = [0.15, 0.30]$. For a European call with $S_0 = K = 100$ and $T = 1$, the robust price satisfies $V^{\text{sup}} = \text{BS}(S_0, K, \overline{\sigma}, T)$ since $\Gamma > 0$ for a call. Compute $V^{\text{sup}}$ and $V^{\text{sub}} = \text{BS}(S_0, K, \underline{\sigma}, T)$ and interpret the bid-ask spread.

??? success "Solution to Exercise 1"

    **Goal.** Compute the super-replication and sub-replication prices for a European call with $S_0 = K = 100$, $T = 1$, $r = 0$, $\underline{\sigma} = 0.15$, $\overline{\sigma} = 0.30$.

    **Step 1: Gamma of a European call.** The European call has payoff $\Phi(S) = (S - K)^+$. The Black-Scholes gamma is:

    $$
    \Gamma = \frac{\partial^2 C}{\partial S^2} = \frac{\phi(d_1)}{S \sigma \sqrt{T}} > 0
    $$

    where $\phi$ is the standard normal density and $d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$. Since $\phi > 0$ everywhere and $S, \sigma, T > 0$, we have $\Gamma > 0$ everywhere in the domain.

    **Step 2: Worst-case volatility.** The BSB equation selects the volatility that maximizes $\frac{1}{2}\sigma^2 S^2 \Gamma$. Since $\Gamma > 0$, this is maximized by choosing $\sigma = \overline{\sigma}$. The super-replication price uses $\overline{\sigma}$ uniformly.

    For the sub-replication (buyer's) price, the worst case from the buyer's perspective is the minimum payoff expectation, achieved with $\sigma = \underline{\sigma}$.

    **Step 3: Compute prices using Black-Scholes formula.** With $r = 0$, the Black-Scholes call price is:

    $$
    C(S_0, K, \sigma, T) = S_0 \mathcal{N}(d_1) - K\mathcal{N}(d_2)
    $$

    where $d_1 = \frac{\sigma\sqrt{T}}{2}$ and $d_2 = -\frac{\sigma\sqrt{T}}{2}$ (since $S_0 = K$ and $r = 0$).

    **Super-replication price** ($\sigma = \overline{\sigma} = 0.30$):

    $$
    d_1 = \frac{0.30}{2} = 0.15, \quad d_2 = -0.15
    $$

    $$
    V^{\text{sup}} = 100[\Phi(0.15) - \Phi(-0.15)] = 100[0.5596 - 0.4404] = 100 \times 0.1192 \approx \$11.92
    $$

    **Sub-replication price** ($\sigma = \underline{\sigma} = 0.15$):

    $$
    d_1 = \frac{0.15}{2} = 0.075, \quad d_2 = -0.075
    $$

    $$
    V^{\text{sub}} = 100[\Phi(0.075) - \Phi(-0.075)] = 100[0.5299 - 0.4701] = 100 \times 0.0598 \approx \$5.98
    $$

    **Step 4: Bid-ask spread.**

    $$
    \text{Spread} = V^{\text{sup}} - V^{\text{sub}} \approx \$11.92 - \$5.98 = \$5.94
    $$

    **Interpretation.** The spread of approximately $\$5.94$ (about 50% of the mid-price) reflects the substantial volatility uncertainty. The seller, who is short gamma, faces the worst case at $\overline{\sigma} = 0.30$ and must charge at least $\$11.92$. The buyer, who is long gamma, benefits from high volatility, so the worst case for the buyer (lowest value of the long call position) is at $\underline{\sigma} = 0.15$, giving a maximum willingness to pay of $\$5.98$.

    Any price in $[\$5.98, \$11.92]$ is arbitrage-free under the uncertain volatility model. The wide spread illustrates why volatility uncertainty is economically significant: doubling the volatility range from $[0.15, 0.30]$ roughly doubles the bid-ask spread. $\square$

---

**Exercise 2.** Write down the Black-Scholes-Barenblatt PDE for the superhedging price:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}S^2 a^*(S, t) \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

where $a^*(S,t) = \overline{\sigma}^2$ if $\Gamma > 0$ and $a^*(S,t) = \underline{\sigma}^2$ if $\Gamma < 0$. For a butterfly spread payoff $(S - K_1)^+ - 2(S - K_2)^+ + (S - K_3)^+$ with $K_1 < K_2 < K_3$, describe how the worst-case volatility switches as a function of $S$, and explain why the BSB equation becomes a free-boundary problem.

??? success "Solution to Exercise 2"

    **Goal.** Describe the worst-case volatility for a butterfly spread and explain why the BSB equation becomes a free-boundary problem.

    **Step 1: Butterfly spread payoff.** The butterfly spread has payoff:

    $$
    \Phi(S) = (S - K_1)^+ - 2(S - K_2)^+ + (S - K_3)^+
    $$

    with $K_1 < K_2 < K_3$. This payoff is piecewise linear:

    $$
    \Phi(S) = \begin{cases} 0 & S \leq K_1 \\ S - K_1 & K_1 < S \leq K_2 \\ K_3 - S & K_2 < S \leq K_3 \\ 0 & S > K_3 \end{cases}
    $$

    (assuming $K_2 = (K_1 + K_3)/2$ for a symmetric butterfly).

    **Step 2: Gamma of the butterfly.** The butterfly is the sum of three call options with different signs. The gamma of each call is positive. Therefore:

    $$
    \Gamma_{\text{butterfly}} = \Gamma_{K_1} - 2\Gamma_{K_2} + \Gamma_{K_3}
    $$

    The gamma of a call is concentrated near its strike (peaked at $S = K$). The butterfly gamma has the following structure:

    - **$S \ll K_1$ or $S \gg K_3$**: All gammas are small, $\Gamma_{\text{butterfly}} \approx 0$
    - **$S$ near $K_1$**: $\Gamma_{K_1}$ dominates, so $\Gamma_{\text{butterfly}} > 0$
    - **$S$ near $K_2$**: $-2\Gamma_{K_2}$ dominates, so $\Gamma_{\text{butterfly}} < 0$
    - **$S$ near $K_3$**: $\Gamma_{K_3}$ dominates, so $\Gamma_{\text{butterfly}} > 0$

    **Step 3: Worst-case volatility switching.** The BSB equation prescribes:

    $$
    a^*(S, t) = \begin{cases} \overline{\sigma}^2 & \text{if } \Gamma(t, S) > 0 \\ \underline{\sigma}^2 & \text{if } \Gamma(t, S) < 0 \end{cases}
    $$

    For the butterfly:

    - **Near $K_1$ and $K_3$** (wings): $\Gamma > 0$, so worst-case $\sigma = \overline{\sigma}$
    - **Near $K_2$** (body): $\Gamma < 0$, so worst-case $\sigma = \underline{\sigma}$
    - **Transition regions**: $\Gamma$ changes sign at two points $S^*(t) \in (K_1, K_2)$ and $S^{**}(t) \in (K_2, K_3)$

    **Step 4: Free-boundary problem.** The BSB equation becomes a free-boundary problem because the locations $S^*(t)$ and $S^{**}(t)$ where $\Gamma = 0$ (and thus where the volatility switches) are not known a priori --- they must be determined as part of the solution. Specifically:

    On each side of the free boundaries, $V$ satisfies a different linear PDE:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\overline{\sigma}^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0 \quad \text{where } \Gamma > 0
    $$

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\underline{\sigma}^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0 \quad \text{where } \Gamma < 0
    $$

    At the free boundaries $S = S^*(t)$ and $S = S^{**}(t)$:

    - $\Gamma(t, S^*(t)) = 0$ and $\Gamma(t, S^{**}(t)) = 0$ (continuity of gamma at the boundary)
    - $V$ and $\partial V / \partial S$ are continuous across the boundary (smooth pasting conditions)

    The free boundaries evolve in time and must be tracked numerically. This is why the BSB equation is fundamentally harder than the standard Black-Scholes PDE: it is a coupled system of two linear PDEs with moving interfaces, rather than a single linear PDE on the whole domain. $\square$

---

**Exercise 3.** Prove that the gamma of a European call is always positive: $\Gamma = \partial^2 C / \partial S^2 > 0$. Then show that for a digital call payoff $\mathbb{1}\{S_T > K\}$, the gamma changes sign near the strike (positive for $S < K$, negative for $S > K$). What is the worst-case volatility for pricing the digital call, and why does it differ from the call option case?

??? success "Solution to Exercise 3"

    **Goal.** Prove $\Gamma > 0$ for a European call, analyze the digital call gamma, and determine worst-case volatility.

    **Part 1: Gamma of a European call is always positive.**

    The Black-Scholes call price is $C(S) = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$ where:

    $$
    d_1 = \frac{\ln(S/K) + (r + \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}, \quad d_2 = d_1 - \sigma\sqrt{T-t}
    $$

    Computing the gamma:

    $$
    \Gamma = \frac{\partial^2 C}{\partial S^2} = \frac{\partial}{\partial S}\left[\mathcal{N}(d_1) + S\phi(d_1)\frac{\partial d_1}{\partial S}\right]
    $$

    Using the fact that $\frac{\partial d_1}{\partial S} = \frac{1}{S\sigma\sqrt{T-t}}$ and the identity $S\phi(d_1) = Ke^{-r(T-t)}\phi(d_2)$, the gamma simplifies to:

    $$
    \Gamma = \frac{\phi(d_1)}{S\sigma\sqrt{T-t}}
    $$

    Since $\phi(d_1) = \frac{1}{\sqrt{2\pi}}e^{-d_1^2/2} > 0$ for all $d_1 \in \mathbb{R}$, and $S, \sigma, \sqrt{T-t} > 0$, we conclude:

    $$
    \Gamma > 0 \quad \text{for all } S > 0, \; t < T
    $$

    $\square$

    **Part 2: Gamma of a digital call.**

    The digital (binary) call has payoff $\Phi(S) = \mathbb{1}_{\{S > K\}}$. Its Black-Scholes price is:

    $$
    V_{\text{dig}}(S) = e^{-r(T-t)}\mathcal{N}(d_2)
    $$

    The delta is:

    $$
    \Delta_{\text{dig}} = \frac{\partial V_{\text{dig}}}{\partial S} = e^{-r(T-t)}\phi(d_2) \cdot \frac{1}{S\sigma\sqrt{T-t}}
    $$

    The gamma is:

    $$
    \Gamma_{\text{dig}} = \frac{\partial^2 V_{\text{dig}}}{\partial S^2} = \frac{\partial \Delta_{\text{dig}}}{\partial S}
    $$

    Computing this derivative:

    $$
    \Gamma_{\text{dig}} = e^{-r(T-t)} \frac{\phi(d_2)}{S^2\sigma^2(T-t)}\left(-d_1\right)
    $$

    (using $\frac{\partial d_2}{\partial S} = \frac{1}{S\sigma\sqrt{T-t}}$ and $\phi'(d_2) = -d_2 \phi(d_2)$, combined with the product rule). The sign of $\Gamma_{\text{dig}}$ is determined by $-d_1$:

    $$
    \Gamma_{\text{dig}} \propto -d_1
    $$

    - **$S < K$ (out of the money)**: $d_1 < 0$ (approximately, for short maturities), so $\Gamma_{\text{dig}} > 0$
    - **$S > K$ (in the money)**: $d_1 > 0$, so $\Gamma_{\text{dig}} < 0$
    - **$S = K$ (at the money)**: $d_1 = \sigma\sqrt{T-t}/2 > 0$, so gamma is slightly negative at the money

    More precisely, $\Gamma_{\text{dig}} = 0$ when $d_1 = 0$, i.e., at $S^* = K\exp(-(r + \sigma^2/2)(T-t))$, which is slightly below $K$.

    **Part 3: Worst-case volatility for the digital call.**

    Since $\Gamma_{\text{dig}}$ changes sign, the worst-case volatility in the BSB equation also switches:

    - **$S < S^*$** (where $\Gamma_{\text{dig}} > 0$): worst-case $\sigma = \overline{\sigma}$
    - **$S > S^*$** (where $\Gamma_{\text{dig}} < 0$): worst-case $\sigma = \underline{\sigma}$

    This differs fundamentally from the European call, where $\Gamma > 0$ everywhere leads to a single worst-case volatility $\overline{\sigma}$. For the digital call, the super-replication price is determined by a switching volatility that depends on the current stock price relative to $S^*$. The seller of a digital call faces different risks on each side of the strike:

    - Below the strike (positive gamma region): the seller benefits from lower volatility, so the worst case is $\overline{\sigma}$
    - Above the strike (negative gamma region): the seller benefits from higher volatility, so the worst case is $\underline{\sigma}$

    The digital call's super-replication price must be computed by solving the full BSB equation with this switching volatility, and the result is strictly higher than the Black-Scholes price at any single volatility in $(\underline{\sigma}, \overline{\sigma})$. $\square$

---

**Exercise 4.** Implement a finite difference scheme for the BSB equation on a grid with $N_S = 100$ spatial points and $N_t = 250$ time steps. At each node, the scheme must select the worst-case volatility based on the sign of $\Gamma$. Describe the algorithm and discuss convergence: why is the BSB equation harder to solve numerically than the standard Black-Scholes PDE?

??? success "Solution to Exercise 4"

    **Goal.** Describe a finite difference scheme for the BSB equation and discuss convergence.

    **Step 1: Grid setup.** Define:

    - Time grid: $t_i = i\Delta t$ for $i = 0, 1, \ldots, N_t$, with $\Delta t = T/N_t$
    - Space grid: $S_j = S_{\min} + j\Delta S$ for $j = 0, 1, \ldots, N_S$, with $\Delta S = (S_{\max} - S_{\min})/N_S$
    - Denote $V_j^i \approx V(t_i, S_j)$

    **Step 2: Terminal condition.** At $i = N_t$ (time $T$):

    $$
    V_j^{N_t} = \Phi(S_j) \quad \text{for all } j
    $$

    **Step 3: Backward iteration (explicit scheme).** For $i = N_t - 1, N_t - 2, \ldots, 0$:

    First, compute the discrete gamma at each node:

    $$
    \Gamma_j^{i+1} = \frac{V_{j+1}^{i+1} - 2V_j^{i+1} + V_{j-1}^{i+1}}{(\Delta S)^2}
    $$

    Select the worst-case volatility:

    $$
    \sigma_j^{i+1} = \begin{cases} \overline{\sigma} & \text{if } \Gamma_j^{i+1} > 0 \\ \underline{\sigma} & \text{if } \Gamma_j^{i+1} < 0 \\ \frac{\overline{\sigma} + \underline{\sigma}}{2} & \text{if } \Gamma_j^{i+1} = 0 \end{cases}
    $$

    Update the value using the explicit finite difference scheme:

    $$
    V_j^i = V_j^{i+1} + \Delta t \left[rS_j \frac{V_{j+1}^{i+1} - V_{j-1}^{i+1}}{2\Delta S} + \frac{1}{2}(\sigma_j^{i+1})^2 S_j^2 \Gamma_j^{i+1} - rV_j^{i+1}\right]
    $$

    **Step 4: Boundary conditions.** At $j = 0$ ($S = S_{\min} \approx 0$): $V_0^i \approx e^{-r(T-t_i)}\Phi(0)$.

    At $j = N_S$ ($S = S_{\max}$): Apply an asymptotic condition, e.g., for a call: $V_{N_S}^i \approx S_{\max} - Ke^{-r(T-t_i)}$.

    **Step 5: Full algorithm.**

    ```
    1. Initialize: V[j, N_t] = Phi(S[j]) for all j
    2. For i = N_t-1 down to 0:
       a. Compute Gamma[j] for j = 1, ..., N_S-1
       b. Select sigma[j] based on sign(Gamma[j])
       c. Compute V[j, i] using explicit update formula
       d. Apply boundary conditions at j = 0 and j = N_S
    3. Output: V[j*, 0] where S[j*] = S_0
    ```

    **Step 6: Convergence discussion.**

    The BSB equation is harder to solve numerically than the standard Black-Scholes PDE for several reasons:

    1. **Nonlinearity and monotone schemes**: The coefficient $\sigma^2(S,t)$ depends on the solution itself (through the sign of $\Gamma$). The Barles-Souganidis theorem guarantees convergence of numerical schemes to the viscosity solution provided the scheme is (a) monotone, (b) consistent, and (c) stable. Monotonicity requires that $V_j^i$ is an increasing function of the neighboring values $V_{j\pm 1}^{i+1}$, which imposes a CFL-type condition:

    $$
    \Delta t \leq \frac{(\Delta S)^2}{\overline{\sigma}^2 S_{\max}^2 + rS_{\max}\Delta S}
    $$

    2. **Volatility switching instability**: Near the free boundary where $\Gamma = 0$, the discrete gamma $\Gamma_j^{i+1}$ may oscillate in sign due to numerical noise, causing the volatility to flip between $\overline{\sigma}$ and $\underline{\sigma}$ erratically. This can slow convergence or cause instability. Remedies include smoothing the gamma near zero or using implicit schemes.

    3. **Non-smooth solutions**: The BSB solution may have discontinuous second derivatives at the free boundary where $\Gamma = 0$. Standard finite difference convergence theory assumes smooth solutions, so the convergence rate degrades near discontinuities. Typical convergence is $O(\Delta S + \Delta t)$ for monotone schemes, versus $O((\Delta S)^2 + \Delta t)$ for the standard Black-Scholes PDE with smooth solutions.

    4. **Implicit vs explicit**: An implicit scheme avoids the CFL condition but requires solving a nonlinear system at each time step (because $\sigma$ depends on the unknown $\Gamma$). Policy iteration (solving a linear system with fixed $\sigma$, then updating $\sigma$, and repeating) is an effective approach.

    5. **Convergence to viscosity solution**: The monotone scheme converges to the unique viscosity solution of the BSB equation, but the rate may be only $O(\sqrt{\Delta t})$ due to the low regularity of the solution. $\square$

---

**Exercise 5.** The uncertain volatility model can be connected to 2BSDEs. Show that the superhedging price $V_t$ satisfies the 2BSDE $-dY_t = f(t, Y_t, Z_t, \Gamma_t) \, dt - Z_t \, dW_t$ where the generator $f$ depends on the uncertain volatility through $\Gamma_t$. What is the explicit form of the generator $f$ for the uncertain volatility model?

??? success "Solution to Exercise 5"

    **Goal.** Show that the superhedging price satisfies a 2BSDE and identify the generator.

    **Step 1: Setup.** Consider a stock $S_t$ under risk-neutral dynamics with uncertain volatility:

    $$
    dS_t = rS_t \, dt + \sigma_t S_t \, dW_t, \quad \sigma_t \in [\underline{\sigma}, \overline{\sigma}]
    $$

    The superhedging price of a claim $\Phi(S_T)$ is:

    $$
    V_t = \sup_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} E^\sigma\left[e^{-r(T-t)}\Phi(S_T) \bigg| \mathcal{F}_t\right]
    $$

    **Step 2: 2BSDE formulation.** Define $Y_t = e^{-rt}V_t$ (the discounted superhedging price). By the dynamic programming principle, $(Y_t, Z_t)$ satisfies:

    $$
    -dY_t = f(t, Y_t, Z_t, \hat{a}_t) \, dt - Z_t \, dW_t
    $$

    where $\hat{a}_t = \sigma_t^2$ is the uncertain instantaneous variance and $Z_t = e^{-rt}\sigma_t S_t \frac{\partial V}{\partial S}$.

    **Step 3: Derive the generator.** Apply Ito's formula to $Y_t = e^{-rt}V(t, S_t)$:

    $$
    dY_t = e^{-rt}\left[-rV + \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma_t^2 S^2 \frac{\partial^2 V}{\partial S^2}\right]dt + e^{-rt}\sigma_t S \frac{\partial V}{\partial S} \, dW_t
    $$

    Identifying $Z_t = e^{-rt}\sigma_t S_t \frac{\partial V}{\partial S}$ and $\Gamma_t = \frac{\partial^2 V}{\partial S^2}$, the BSDE dynamics require:

    $$
    f(t, Y_t, Z_t, \hat{a}_t) = -\left[-rV + \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\hat{a}_t S^2 \Gamma_t\right]e^{-rt}
    $$

    The BSB equation (which $V$ satisfies) states that:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\hat{a}_t^* S^2 \Gamma_t - rV = 0
    $$

    where $\hat{a}_t^* = \arg\sup_{\hat{a} \in [\underline{\sigma}^2, \overline{\sigma}^2]} \frac{1}{2}\hat{a} S^2 \Gamma_t$ is the worst-case variance.

    **Step 4: Explicit generator.** The generator of the 2BSDE for the uncertain volatility model is:

    $$
    f(t, y, z, \hat{a}) = -ry + \sup_{\hat{a} \in [\underline{\sigma}^2, \overline{\sigma}^2]} \frac{1}{2}\hat{a} \cdot \Gamma_t S_t^2 e^{-rt}
    $$

    Equivalently, working directly with the undiscounted value process $V_t$ and expressing the generator in terms of the gamma $\Gamma_t$:

    $$
    f(t, V, Z, \Gamma) = -rV + rS\frac{\partial V}{\partial S} + G(\Gamma S^2)
    $$

    where:

    $$
    G(x) = \sup_{\hat{a} \in [\underline{\sigma}^2, \overline{\sigma}^2]} \frac{1}{2}\hat{a} \cdot x = \frac{1}{2}\overline{\sigma}^2 x^+ - \frac{1}{2}\underline{\sigma}^2 x^-
    $$

    Since $\Gamma S^2$ has the same sign as $\Gamma$, the generator explicitly becomes:

    $$
    f(t, V, Z, \Gamma) = -rV + rS\frac{\partial V}{\partial S} + \frac{1}{2}\overline{\sigma}^2 S^2 \Gamma^+ - \frac{1}{2}\underline{\sigma}^2 S^2 \Gamma^-
    $$

    This is the 2BSDE generator for the uncertain volatility model. The dependence on $\Gamma$ (the second-order process) makes this a genuine 2BSDE, not a standard BSDE. The supremum over $\hat{a}$ encodes the adversarial choice of volatility by nature, selecting the worst case for the hedger at each instant. $\square$

---

**Exercise 6.** For a portfolio of vanilla options with both positive and negative gamma regions, the worst-case volatility in the UVM switches between $\underline{\sigma}$ and $\overline{\sigma}$ depending on the portfolio gamma. Consider a risk reversal (long OTM call, short OTM put). Determine which volatility is worst-case in each moneyness region and explain why the robust price of the risk reversal depends on the correlation between the volatility switching and the stock price level.

??? success "Solution to Exercise 6"

    **Goal.** Analyze the worst-case volatility for a risk reversal and explain the role of the volatility-stock price correlation.

    **Step 1: Risk reversal structure.** A risk reversal consists of:

    - Long one OTM call with strike $K_C > S_0$
    - Short one OTM put with strike $K_P < S_0$

    The combined payoff is:

    $$
    \Phi(S) = (S - K_C)^+ - (K_P - S)^+
    $$

    **Step 2: Gamma analysis of each component.**

    The **long call** has gamma:

    $$
    \Gamma_{\text{call}} = \frac{\phi(d_1^C)}{S\sigma\sqrt{T-t}} > 0
    $$

    concentrated near $S = K_C$.

    The **short put** has gamma:

    $$
    \Gamma_{\text{put}} = -\frac{\phi(d_1^P)}{S\sigma\sqrt{T-t}} < 0
    $$

    (negative because we are short the put), concentrated near $S = K_P$.

    **Step 3: Portfolio gamma by region.**

    $$
    \Gamma_{\text{RR}}(S) = \Gamma_{\text{call}}(S) + \Gamma_{\text{short put}}(S)
    $$

    - **$S \ll K_P$ (deep OTM)**: Both gammas are small, but the short put gamma dominates since $S$ is closer to $K_P$. $\Gamma_{\text{RR}} < 0$.

    - **$S \approx K_P$ (near put strike)**: The short put gamma is at its most negative. $\Gamma_{\text{RR}} < 0$ (strongly negative).

    - **$K_P < S < K_C$ (between strikes)**: Both gammas are moderate. Near the midpoint, $\Gamma_{\text{RR}}$ could be either sign depending on the relative distances. Typically $\Gamma_{\text{RR}} \approx 0$ or slightly positive/negative.

    - **$S \approx K_C$ (near call strike)**: The long call gamma dominates. $\Gamma_{\text{RR}} > 0$ (strongly positive).

    - **$S \gg K_C$ (deep ITM)**: Both gammas are small, but the long call gamma dominates. $\Gamma_{\text{RR}} > 0$ (weakly).

    **Step 4: Worst-case volatility assignment.**

    Applying the BSB rule $\sigma^* = \overline{\sigma}$ where $\Gamma > 0$ and $\sigma^* = \underline{\sigma}$ where $\Gamma < 0$:

    | Stock price region | Portfolio gamma | Worst-case $\sigma$ |
    |---|---|---|
    | $S \leq K_P$ (near/below put strike) | $\Gamma < 0$ | $\underline{\sigma}$ |
    | $K_P < S < S^*$ (between strikes, put side) | $\Gamma < 0$ | $\underline{\sigma}$ |
    | $S^* < S < K_C$ (between strikes, call side) | $\Gamma > 0$ | $\overline{\sigma}$ |
    | $S \geq K_C$ (near/above call strike) | $\Gamma > 0$ | $\overline{\sigma}$ |

    where $S^*$ is the point between $K_P$ and $K_C$ where $\Gamma_{\text{RR}} = 0$.

    **Step 5: Why the robust price depends on the correlation between volatility switching and stock price.**

    The worst-case volatility is $\underline{\sigma}$ when $S$ is low (near $K_P$) and $\overline{\sigma}$ when $S$ is high (near $K_C$). This means nature's worst-case strategy introduces a **positive correlation between volatility and stock price**: high volatility when $S$ is high, low volatility when $S$ is low.

    This matters because:

    1. **Path-dependent worst case**: The worst-case volatility depends on where $S$ is at each instant. If $S$ moves toward $K_C$, the worst-case volatility increases (to $\overline{\sigma}$), amplifying the stock's upward movements and increasing the expected call payoff. If $S$ moves toward $K_P$, the worst-case volatility decreases (to $\underline{\sigma}$), damping the stock's downward movements and reducing the put's payoff recovery for the seller.

    2. **Asymmetric risk amplification**: The positive correlation between $\sigma$ and $S$ is the worst case for the risk reversal seller because it amplifies losses on both sides: the long call becomes more expensive (high vol when $S$ is high) and the short put protection weakens (low vol when $S$ is low, so $S$ is less likely to recover from a drop).

    3. **Comparison with Black-Scholes**: In Black-Scholes with constant $\sigma$, the risk reversal price is simply $C(K_C, \sigma) - P(K_P, \sigma)$. In the UVM, the effective volatility differs by region, and the super-replication price is strictly higher than the Black-Scholes price at any single $\sigma \in (\underline{\sigma}, \overline{\sigma})$ because the switching strategy is adversarial.

    4. **Connection to skew**: The worst-case volatility pattern (low vol for low $S$, high vol for high $S$) is the opposite of the typical equity implied volatility skew (where IV increases as $S$ decreases). This means the UVM worst case for a risk reversal is particularly conservative, as it assumes a volatility regime that contradicts the empirical skew pattern. This highlights that the UVM provides model-free bounds that do not exploit empirical regularities in the smile. $\square$
