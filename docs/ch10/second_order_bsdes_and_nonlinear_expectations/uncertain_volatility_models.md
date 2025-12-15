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

### Setup

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

### Hedging Portfolio

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

### Super-Replication Price

**Definition**: The **super-replication price** $V^{\text{sup}}(S_0)$ is the minimal initial capital required to construct a hedging portfolio that dominates the option payoff under all volatility scenarios:

$$
V^{\text{sup}}(S_0) = \inf \left\{ V_0: \exists \Delta_t \text{ s.t. } V_T \geq \Phi(S_T) \text{ for all } \sigma_t \in [\underline{\sigma}, \overline{\sigma}] \right\}
$$

**Interpretation**: Conservative pricing from seller's perspective.

### Sub-Replication Price

**Definition**: The **sub-replication price** $V^{\text{sub}}(S_0)$ is the maximal initial capital from which a portfolio can be constructed that is dominated by the option payoff:

$$
V^{\text{sub}}(S_0) = \sup \left\{ V_0: \exists \Delta_t \text{ s.t. } V_T \leq \Phi(S_T) \text{ for all } \sigma_t \in [\underline{\sigma}, \overline{\sigma}] \right\}
$$

**Interpretation**: Aggressive pricing from buyer's perspective.

### Bid-Ask Spread

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

### Black-Scholes-Barenblatt Equation

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

### Viscosity Solutions

**Definition**: Since $V$ may not be $C^2$ (especially at strike for digital options), solutions are understood in the **viscosity sense**.

**Viscosity Solution**: A function $V$ satisfying:
- At smooth points: PDE holds classically
- At non-smooth points: Comparison with test functions

**Uniqueness**: The viscosity solution is unique, ensuring well-posedness.

**Comparison Principle**: If $V_1$ and $V_2$ are respectively sub- and supersolutions with $V_1(T, \cdot) \leq V_2(T, \cdot)$, then $V_1 \leq V_2$ everywhere.

### Examples

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

### Delta Hedging

**Theorem**: The optimal hedging strategy is:

$$
\Delta_t^* = \frac{\partial V}{\partial S}(t, S_t)
$$

where $V$ is the super-replication price.

**Proof**: By construction, $V(t, S_t)$ is a supermartingale under worst-case volatility. The delta position makes the portfolio self-financing.

**Interpretation**: Classic delta-hedging, but using value function from nonlinear PDE.

### Gamma Adjustment

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

### Vega Hedging

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

### Path-Dependent Options

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

### Barrier Options

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

### American Options

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

### Lookback Options

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

### Basket Options

**Assets**: $\mathbf{S}_t = (S_t^{(1)}, \ldots, S_t^{(n)})$

**Dynamics**:

$$
dS_t^{(i)} = \mu_i S_t^{(i)} \, dt + \sigma_t^{(i)} S_t^{(i)} \, dW_t^{(i)}
$$

**Correlation Uncertainty**: Cross-correlations $\rho_{ij}(t) \in [\underline{\rho}_{ij}, \overline{\rho}_{ij}]$.

### Nonlinear PDE

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

### Correlation Bounds

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

### Finite Difference Schemes

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

### Monte Carlo Simulation

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

### Policy Iteration

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

### Implied Volatility Bounds

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

### Historical Volatility

**Realized Volatility**: Compute from historical returns:

$$
\hat{\sigma} = \sqrt{\frac{252}{n} \sum_{i=1}^n \log^2\left(\frac{S_{t_i}}{S_{t_{i-1}}}\right)}
$$

**Bounds**: Use historical range:

$$
\underline{\sigma} = \hat{\sigma} - k \cdot \text{std}(\sigma_{\text{hist}}), \quad \overline{\sigma} = \hat{\sigma} + k \cdot \text{std}(\sigma_{\text{hist}})
$$

for some confidence level $k$.

### Combining Information

**Hybrid Approach**: Combine implied and historical:

$$
\underline{\sigma} = \min\{\sigma_{\text{imp}}^{\min}, \sigma_{\text{hist}}^{\min}\}, \quad \overline{\sigma} = \max\{\sigma_{\text{imp}}^{\max}, \sigma_{\text{hist}}^{\max}\}
$$

**Judgment**: Analyst judgment based on market conditions, regime shifts, etc.

## Model Risk and Stress Testing

### Model Risk Quantification

**Definition**: The difference between model price and robust price:

$$
\text{Model Risk} = V^{\text{sup}} - V^{\text{model}}
$$

**Interpretation**: Additional capital required to protect against model misspecification.

### Stress Testing

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

### Value-at-Risk (VaR)

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

### Heston Model

**Dynamics**: 

$$
dS_t = \mu S_t \, dt + \sqrt{V_t} S_t \, dW_t^S, \quad dV_t = \kappa(\theta - V_t) \, dt + \xi \sqrt{V_t} \, dW_t^V
$$

**Known Parameters**: Assumes specific mean-reversion $\kappa$, long-run mean $\theta$, vol-of-vol $\xi$.

**Comparison**: Heston is **parametric** and **specific**, while UVM is **nonparametric** and **robust**.

### Local Volatility

**Model**: $\sigma = \sigma(S, t)$ determined from market prices via Dupire's formula.

**Certainty**: Assumes specific, deterministic volatility function.

**Comparison**: Local volatility is **model-complete** but not robust to misspecification; UVM provides bounds.

### SABR Model

**Dynamics**:

$$
dF_t = \alpha_t F_t^{\beta} \, dW_t^1, \quad d\alpha_t = \nu \alpha_t \, dW_t^2
$$

**Usage**: Widely used for FX and interest rate options.

**Comparison**: SABR specifies stochastic dynamics; UVM only specifies bounds.

### Pros and Cons

| **Model** | **Pros** | **Cons** |
|-----------|----------|----------|
| **UVM** | Model-free, robust, conservative | Wide spreads, conservative pricing |
| **Heston** | Tractable, explicit formulas | Requires parameter estimation, model risk |
| **Local Vol** | Matches market prices exactly | No smile dynamics, deterministic |
| **SABR** | Captures smile dynamics, popular | Parameter instability, calibration challenges |

## Applications in Practice

### Market Making

**Two-Way Quotes**: Provide bid and ask prices:
- **Bid**: $V^{\text{sub}}$ (buying from client)
- **Ask**: $V^{\text{sup}}$ (selling to client)

**Spread**: Reflects volatility uncertainty:

$$
\text{Spread} = V^{\text{sup}} - V^{\text{sub}}
$$

**Inventory Management**: Adjust spreads based on position (long/short gamma).

### Exotic Derivatives Desk

**Structured Products**: Price complex payoffs using UVM framework.

**Example** (Worst-of Basket):

$$
\Phi = \min_{i=1, \ldots, n} S_T^{(i)} - K
$$

**Hedging**: Use UVM to compute robust hedges in each underlying and correlation.

**Risk**: Quantify model risk using spread width.

### Risk Management

**Regulatory Capital**: Basel III requires quantification of model risk:

$$
\text{Model Risk Capital} = V^{\text{sup}} - V^{\text{expected}}
$$

**Internal Models**: Banks use UVM to stress-test trading book.

**Backtesting**: Compare realized P&L against robust bounds to validate assumptions.

## Advanced Topics

### Uncertain Jump Risk

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

### Time-Dependent Bounds

**Time-Varying Uncertainty**:

$$
\underline{\sigma}(t) \leq \sigma_t \leq \overline{\sigma}(t)
$$

**PDE**: Coefficient becomes time-dependent:

$$
\frac{\partial V}{\partial t} + rS \frac{\partial V}{\partial S} + \frac{1}{2} \bar{\sigma}^2(t, V) S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0
$$

**Application**: Models regime shifts, earnings announcements, macroeconomic releases.

### Transaction Costs

**Proportional Costs**: Each trade costs $\lambda |$quantity$| \times$ price.

**Modified PDE**: Includes nonlinear terms from costs:

$$
\frac{\partial V}{\partial t} + rS \frac{\partial V}{\partial S} + \frac{1}{2} \bar{\sigma}^2(V) S^2 \frac{\partial^2 V}{\partial S^2} - \lambda S \left|\frac{\partial V}{\partial S}\right| - rV = 0
$$

**Interpretation**: Transaction costs increase super-replication price.

### Interest Rate Uncertainty

**Stochastic Rates**: Uncertain short rate $r_t \in [\underline{r}, \overline{r}]$.

**Discount Factor**: Affects pricing through:

$$
\exp\left(-\int_0^T r_s \, ds\right)
$$

**Joint Uncertainty**: Both volatility and interest rate uncertain.

**Dimension**: Increases state space dimension, making numerical solution more challenging.

## Research Directions

### Deep Learning for UVMs

**Neural Network Approximation**: Represent value function:

$$
V(t, S) \approx f_{\theta}(t, S)
$$

**Training**: Minimize PDE residual:

$$
\mathcal{L}(\theta) = \mathbb{E}\left[\left|\frac{\partial f_{\theta}}{\partial t} + rS \frac{\partial f_{\theta}}{\partial S} + \frac{1}{2} \bar{\sigma}^2(f_{\theta}) S^2 \frac{\partial^2 f_{\theta}}{\partial S^2} - rf_{\theta}\right|^2\right]
$$

**Advantages**: Handles high dimensions, bypasses curse of dimensionality.

### Data-Driven Calibration

**Machine Learning**: Learn volatility bounds from data:
- Supervised learning: Predict $[\underline{\sigma}, \overline{\sigma}]$ from market features
- Reinforcement learning: Optimal hedging strategies under UVM

**Online Learning**: Update bounds dynamically as new data arrives.

### Rough Volatility

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

### Fundamental Results

1. **Fully Nonlinear PDEs**: Robust pricing under volatility uncertainty leads to Black-Scholes-Barenblatt equation.

2. **Viscosity Solutions**: Generalized notion of solution handles non-smooth payoffs and discontinuous coefficients.

3. **Optimal Hedging**: Delta-hedging with value function from nonlinear PDE is optimal.

4. **Bid-Ask Spreads**: Market spreads can be explained by volatility uncertainty and gamma exposure.

5. **Model-Free Bounds**: Provides rigorous bounds without specifying volatility dynamics.

### Practical Implications

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

### Theoretical Significance

Uncertain volatility models bridge:
- **Stochastic Analysis**: BSDEs and martingale theory
- **PDE Theory**: Fully nonlinear equations and viscosity solutions
- **Optimization**: Robust control and minimax problems
- **Finance**: Pricing, hedging, and risk management

The UVM framework represents a cornerstone of robust quantitative finance, providing rigorous mathematical foundations for handling model uncertainty while maintaining practical applicability in derivative pricing, hedging, and risk management.
