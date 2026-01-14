# Superhedging Duality


## Introduction


Superhedging duality establishes a fundamental connection between dynamic hedging strategies and equivalent martingale measures in derivative pricing. This duality provides both theoretical foundations and computational methods for pricing under model uncertainty.

The **superhedging price** is the minimum initial capital required to construct a portfolio that replicates or dominates a derivative's payoff with certainty. Through duality theory, this dynamic optimization problem can be reformulated as a static optimization over probability measures, yielding powerful insights and computational advantages.

## Mathematical Framework


### 1. Market Model


**Filtered Probability Space**: Consider $(\Omega, \mathcal{F}, \{\mathcal{F}_t\}_{t \in [0,T]}, \mathbb{P})$ where:
- $\Omega$ is the sample space
- $\mathcal{F}$ is the $\sigma$-algebra of events
- $\{\mathcal{F}_t\}$ is a filtration representing information flow
- $\mathbb{P}$ is the physical probability measure

**Traded Assets**: 
- Riskless asset (numéraire): $S_t^0 = e^{rt}$
- $d$ risky assets: $S_t = (S_t^1, \ldots, S_t^d)$

**Price Process**: The discounted price process is:


$$
\tilde{S}_t = e^{-rt} S_t
$$



**Trading Strategy**: A predictable process $\theta_t = (\theta_t^0, \theta_t^1, \ldots, \theta_t^d)$ representing portfolio holdings.

**Value Process**: The portfolio value is:


$$
V_t^{\theta} = \theta_t^0 S_t^0 + \sum_{i=1}^d \theta_t^i S_t^i
$$



**Self-Financing**: The strategy $\theta$ is self-financing if:


$$
dV_t^{\theta} = \theta_t^0 dS_t^0 + \sum_{i=1}^d \theta_t^i dS_t^i
$$



or equivalently:


$$
d\tilde{V}_t^{\theta} = \sum_{i=1}^d \theta_t^i d\tilde{S}_t^i
$$



### 2. Admissible Strategies


**Definition**: A trading strategy $\theta$ is **admissible** if:
1. It is self-financing
2. It is predictable with respect to $\{\mathcal{F}_t\}$
3. It satisfies a lower bound: $V_t^{\theta} \geq -M$ for some constant $M$ (no unbounded borrowing)

Denote the set of admissible strategies by $\mathcal{A}$.

**Economically Reasonable Constraint**: Often we require $V_t^{\theta} \geq 0$ for all $t$ (non-negative wealth constraint).

## Superhedging Problem


### 1. Definition


**Contingent Claim**: A random variable $\xi$ measurable with respect to $\mathcal{F}_T$ representing the derivative's payoff at maturity.

**Superhedging Strategy**: A strategy $\theta \in \mathcal{A}$ **superhedges** $\xi$ if:


$$
V_T^{\theta} \geq \xi \quad \mathbb{P}\text{-almost surely}
$$



**Superhedging Price** (Seller's Price): The minimum initial capital needed to superhedge:


$$
\pi^{\text{sup}}(\xi) = \inf \left\{ v \in \mathbb{R}: \exists \theta \in \mathcal{A} \text{ with } V_0^{\theta} = v \text{ and } V_T^{\theta} \geq \xi \, \mathbb{P}\text{-a.s.} \right\}
$$



**Interpretation**: 
- $\pi^{\text{sup}}(\xi)$ is the minimum amount a seller needs to hedge the obligation to deliver $\xi$ at time $T$
- Any price above $\pi^{\text{sup}}(\xi)$ allows the seller to lock in arbitrage profit
- Any price below $\pi^{\text{sup}}(\xi)$ exposes the seller to unbounded loss

### 2. Sub-Replication


**Sub-Replicating Strategy**: A strategy $\theta$ **sub-replicates** $\xi$ if:


$$
V_T^{\theta} \leq \xi \quad \mathbb{P}\text{-almost surely}
$$



**Sub-Replication Price** (Buyer's Price):


$$
\pi^{\text{sub}}(\xi) = \sup \left\{ v \in \mathbb{R}: \exists \theta \in \mathcal{A} \text{ with } V_0^{\theta} = v \text{ and } V_T^{\theta} \leq \xi \, \mathbb{P}\text{-a.s.} \right\}
$$



**Interpretation**:
- $\pi^{\text{sub}}(\xi)$ is the maximum amount a buyer can guarantee from selling a portfolio that is dominated by $\xi$
- Any price below $\pi^{\text{sub}}(\xi)$ allows the buyer to lock in arbitrage profit

### 3. No-Arbitrage and Price Bounds


**Proposition**: Under no-arbitrage:


$$
\pi^{\text{sub}}(\xi) \leq \pi^{\text{sup}}(\xi)
$$



**Proof**: Suppose $\pi^{\text{sub}}(\xi) > \pi^{\text{sup}}(\xi)$. Then:
- Sell the sub-replicating portfolio for $\pi^{\text{sub}}(\xi)$
- Buy the superhedging portfolio for $\pi^{\text{sup}}(\xi)$
- Initial profit: $\pi^{\text{sub}}(\xi) - \pi^{\text{sup}}(\xi) > 0$
- At time $T$: receive at most $\xi$ from sub-replication, deliver at least $\xi$ from superhedging
- Net payoff $\geq 0$, yielding arbitrage

**Complete Markets**: When the market is complete:


$$
\pi^{\text{sub}}(\xi) = \pi^{\text{sup}}(\xi)
$$



and this common value is the unique arbitrage-free price.

**Incomplete Markets**: The interval $[\pi^{\text{sub}}(\xi), \pi^{\text{sup}}(\xi)]$ represents the range of arbitrage-free prices, reflecting model uncertainty.

## Equivalent Martingale Measures


### 1. Definition


**Equivalent Martingale Measure** (EMM): A probability measure $\mathbb{Q}$ on $(\Omega, \mathcal{F}_T)$ is an EMM if:
1. $\mathbb{Q} \sim \mathbb{P}$ (equivalent to the physical measure)
2. The discounted price process $\tilde{S}_t$ is a $\mathbb{Q}$-martingale:

   $$
   \tilde{S}_t = \mathbb{E}_{\mathbb{Q}}[\tilde{S}_T | \mathcal{F}_t]
   $$



**Set of EMMs**: Denote:


$$
\mathcal{M} = \{ \mathbb{Q}: \mathbb{Q} \text{ is an EMM} \}
$$



### 2. Fundamental Theorem of Asset Pricing


**First Fundamental Theorem**: The market admits no arbitrage if and only if $\mathcal{M} \neq \emptyset$.

**Second Fundamental Theorem**: The market is complete if and only if $\mathcal{M}$ is a singleton (unique EMM).

**Implications**:
- Existence of EMM $\Leftrightarrow$ No arbitrage
- Uniqueness of EMM $\Leftrightarrow$ Market completeness

## Dual Representation of Superhedging Price


### 1. Main Duality Theorem


**Theorem** (Superhedging Duality): Under appropriate technical conditions:


$$
\pi^{\text{sup}}(\xi) = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi]
$$



**Interpretation**: 
- The minimum cost to superhedge equals the maximum expected discounted payoff over all martingale measures
- This transforms a dynamic programming problem (finding optimal trading strategy) into a static optimization problem (maximizing over measures)

**Proof Outline**:

1. **Lower Bound** ($\pi^{\text{sup}}(\xi) \geq \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi]$):
   
   For any superhedging strategy $\theta$ with $V_0^{\theta} = v$ and $V_T^{\theta} \geq \xi$:
   

   $$
   e^{-rT} V_T^{\theta} = \tilde{V}_T^{\theta} \geq e^{-rT} \xi
   $$


   
   For any $\mathbb{Q} \in \mathcal{M}$, since $\tilde{V}_t^{\theta}$ is a $\mathbb{Q}$-supermartingale (under self-financing):
   

   $$
   v = V_0^{\theta} = \tilde{V}_0^{\theta} \geq \mathbb{E}_{\mathbb{Q}}[\tilde{V}_T^{\theta}] \geq \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi]
   $$


   
   Taking infimum over all superhedging strategies yields the result.

2. **Upper Bound** ($\pi^{\text{sup}}(\xi) \leq \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi]$):
   
   This direction requires showing that for $v = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi]$, there exists a superhedging strategy starting with capital $v$. This typically requires separation theorems and the Hahn-Banach theorem in functional analysis.

### 2. Technical Conditions


For the duality to hold, we typically require:

1. **No Arbitrage**: $\mathcal{M} \neq \emptyset$

2. **Closure Properties**: The set of terminal values of admissible strategies is closed in an appropriate topology

3. **Integrability**: $\xi$ is integrable under all $\mathbb{Q} \in \mathcal{M}$

4. **Bounded from Below**: Either $\xi$ or the trading strategies satisfy suitable lower bounds

**Delbaen-Schachermayer Theory**: Provides rigorous conditions for duality in general semimartingale models.

## Sub-Replication Duality


### 1. Dual Representation


**Theorem**: Under similar conditions:


$$
\pi^{\text{sub}}(\xi) = \inf_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi]
$$



**Proof**: Similar to superhedging case, with inequalities reversed.

### 2. Bid-Ask Spread


**Arbitrage-Free Price Interval**:


$$
[\pi^{\text{sub}}(\xi), \pi^{\text{sup}}(\xi)] = \left[ \inf_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi], \, \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi] \right]
$$



**Width of Spread**: The spread reflects model uncertainty:


$$
\text{Spread}(\xi) = \pi^{\text{sup}}(\xi) - \pi^{\text{sub}}(\xi) = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi] - \inf_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi]
$$



**Complete Markets**: Spread = 0 (unique price)

**Incomplete Markets**: Spread > 0 reflects uncertainty in hedging

## Applications and Examples


### 1. Example 1: Binary Option in Binomial Model


**Model**: Single-period binomial tree:
- $S_0 = 100$
- $S_1 = 120$ (up) or $S_1 = 90$ (down)
- $r = 0$

**Claim**: Digital call paying $1$ if $S_1 > 110$.

**EMM Characterization**: For $\mathbb{Q}$ to be a martingale measure:


$$
S_0 = \mathbb{E}_{\mathbb{Q}}[S_1] = 120 q + 90(1-q) = 100
$$



Solving: $q = 1/3$.

Since the EMM is unique, the market is complete:


$$
\pi^{\text{sup}}(\xi) = \pi^{\text{sub}}(\xi) = \mathbb{E}_{\mathbb{Q}}[\xi] = \frac{1}{3} \cdot 1 + \frac{2}{3} \cdot 0 = \frac{1}{3}
$$



### 2. Example 2: Incomplete Market with Volatility Uncertainty


**Model**: Stock follows:


$$
dS_t = \mu S_t \, dt + \sigma_t S_t \, dW_t
$$



where $\sigma_t \in [\sigma_{\min}, \sigma_{\max}]$ is uncertain.

**EMM Set**: For each choice of $(\sigma_t)_{t \in [0,T]}$, there is a corresponding EMM $\mathbb{Q}^{\sigma}$.

**Digital Call**: Payoff $\mathbb{1}_{\{S_T > K\}}$.

**Superhedging Price**: 


$$
\pi^{\text{sup}} = \sup_{\sigma \in [\sigma_{\min}, \sigma_{\max}]} \text{BS-Digital}(S_0, K, \sigma, T)
$$



where BS-Digital is the Black-Scholes digital call price.

**Maximizing Volatility**: Since digital option value typically increases with volatility:


$$
\pi^{\text{sup}} = \text{BS-Digital}(S_0, K, \sigma_{\max}, T)
$$



**Sub-Replication Price**:


$$
\pi^{\text{sub}} = \text{BS-Digital}(S_0, K, \sigma_{\min}, T)
$$



### 3. Example 3: Barrier Option


**Claim**: Up-and-out call with barrier $H > S_0$ and strike $K < H$:


$$
\xi = (S_T - K)^+ \mathbb{1}_{\{\max_{0 \leq t \leq T} S_t < H\}}
$$



**Challenge**: Barrier options are strongly path-dependent; hedging requires continuous monitoring.

**Superhedging Strategy**: 
- Hold a replicating portfolio for a vanilla call
- At time $\tau = \inf\{t: S_t \geq H\}$, liquidate and invest in bonds

**Superhedging Price**: Can be computed using PDE methods:


$$
\pi^{\text{sup}}(\xi) = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi]
$$



In Black-Scholes model, this reduces to the standard barrier option formula.

**Model Uncertainty**: With volatility uncertainty $\sigma \in [\sigma_{\min}, \sigma_{\max}]$:


$$
\pi^{\text{sup}}(\xi) = \sup_{\sigma \in [\sigma_{\min}, \sigma_{\max}]} C^{\text{UO}}(S_0, K, H, \sigma, T)
$$



where $C^{\text{UO}}$ is the up-and-out call price under constant volatility $\sigma$.

## Computational Methods


### 1. Linear Programming Formulation


**Discrete State Space**: Approximate $\Omega$ by a finite set $\{\omega_1, \ldots, \omega_N\}$.

**Martingale Constraints**: For each time step and state:


$$
\tilde{S}_t(\omega) = \sum_{j: \omega_j \succ \omega} \mathbb{Q}(\omega_j | \omega) \tilde{S}_{t+1}(\omega_j)
$$



**LP Formulation**:


$$
\begin{aligned}
\text{maximize} \quad & \sum_{i=1}^N e^{-rT} \xi(\omega_i) \mathbb{Q}(\omega_i) \\
\text{subject to} \quad & \text{Martingale constraints} \\
& \sum_{i=1}^N \mathbb{Q}(\omega_i) = 1 \\
& \mathbb{Q}(\omega_i) \geq 0, \quad i = 1, \ldots, N
\end{aligned}
$$



**Dual Problem**: Corresponds to finding the superhedging strategy (portfolio weights).

### 2. Monte Carlo with Linear Programming


**Scenario Generation**: Generate $N$ paths $\{S^{(i)}(t_j)\}_{j=0}^M$ for $i = 1, \ldots, N$.

**Martingale Constraints**: For each path $i$ and time $t_j$:


$$
S^{(i)}(t_j) = \sum_{k=1}^N p_{ik}(j) S^{(k)}(t_{j+1})
$$



where $p_{ik}(j)$ represents transition probabilities.

**Optimization**: Solve LP to find probabilities that maximize expected payoff while satisfying martingale constraints.

### 3. Dynamic Programming


**Bellman Equation**: For Markovian models, the superhedging price satisfies:


$$
V(t, S) = \sup_{\theta} \inf_{\sigma \in [\sigma_{\min}, \sigma_{\max}]} \left[ V(t+dt, S+dS) \right]
$$



where the supremum is over trading strategies and infimum over model parameters.

**HJB Equation**: In continuous time:


$$
\frac{\partial V}{\partial t} + \sup_{\theta} \left\{ \theta \sigma S \frac{\partial^2 V}{\partial S^2} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} \right\} = 0
$$



with terminal condition $V(T, S) = \xi(S)$.

**Numerical Solution**: Use finite difference methods or policy iteration.

## Advanced Topics


### 1. Gamma Hedging and Viscosity Solutions


**Gamma Constraint**: In models with volatility uncertainty, the superhedging strategy involves controlling the portfolio's gamma exposure.

**Viscosity Solutions**: The value function $V(t, S)$ satisfying the HJB equation is characterized as a **viscosity solution**, a generalized notion of solution for non-smooth Hamilton-Jacobi equations.

**Theorem** (Uniqueness): Under appropriate conditions, the viscosity solution to the HJB equation is unique and equals the superhedging price.

### 2. Quadratic Hedging


**Alternative Objective**: Instead of perfect replication, minimize expected squared hedging error:


$$
\min_{\theta} \mathbb{E}_{\mathbb{P}}\left[ (V_T^{\theta} - \xi)^2 \right]
$$



**Solution**: Involves projecting $\xi$ onto the space of attainable claims, leading to the **variance-optimal** hedging strategy.

**Relationship to Superhedging**: Quadratic hedging provides an approximation when perfect hedging is too expensive.

### 3. Convex Duality


**Fenchel-Rockafellar Duality**: The superhedging problem can be formulated as:


$$
\inf \{ c: (c, -\xi) \in \mathcal{C} \}
$$



where $\mathcal{C}$ is the cone of claims attainable with non-negative cost.

**Dual Problem**: Maximize over dual variables (equivalent to EMMs).

**Duality Gap**: In general settings, there may be a duality gap. Conditions ensuring zero duality gap are studied in convex analysis.

## Comparison with Other Pricing Approaches


### 1. Black-Scholes Pricing


**Assumption**: Unique EMM under geometric Brownian motion with constant volatility.

**Price**: 


$$
\pi^{\text{BS}}(\xi) = \mathbb{E}_{\mathbb{Q}^{\text{BS}}}[e^{-rT} \xi]
$$



**Relationship to Superhedging**: When $\mathcal{M} = \{\mathbb{Q}^{\text{BS}}\}$:


$$
\pi^{\text{sup}}(\xi) = \pi^{\text{sub}}(\xi) = \pi^{\text{BS}}(\xi)
$$



**Model Uncertainty**: With volatility uncertainty:


$$
\pi^{\text{BS}}(\xi; \sigma) \in [\pi^{\text{sub}}(\xi), \pi^{\text{sup}}(\xi)]
$$



for $\sigma \in [\sigma_{\min}, \sigma_{\max}]$.

### 2. Utility-Based Pricing


**Indifference Price**: The price $p$ at which an agent is indifferent between trading and not trading:


$$
U(W) = \mathbb{E}[u(W_T^{p, \theta})]
$$



**Comparison**: 
- Superhedging: Model-free, robust, but often conservative
- Utility-based: Incorporates preferences, but model-dependent

**Asymptotic Equivalence**: For small claims, utility indifference prices converge to martingale prices, which lie in $[\pi^{\text{sub}}(\xi), \pi^{\text{sup}}(\xi)]$.

### 3. Good-Deal Bounds


**Setup**: Restrict EMMs to those satisfying additional constraints, e.g., Sharpe ratio bounds:


$$
\mathcal{M}_{\text{GD}} = \left\{ \mathbb{Q} \in \mathcal{M}: \left\| \frac{d\mathbb{Q}}{d\mathbb{P}} \right\| \leq K \right\}
$$



**Good-Deal Bounds**:


$$
\pi^{\text{GD, sub}}(\xi) = \inf_{\mathbb{Q} \in \mathcal{M}_{\text{GD}}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi] \geq \pi^{\text{sub}}(\xi)
$$




$$
\pi^{\text{GD, sup}}(\xi) = \sup_{\mathbb{Q} \in \mathcal{M}_{\text{GD}}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi] \leq \pi^{\text{sup}}(\xi)
$$



**Interpretation**: Good-deal bounds tighten arbitrage-free bounds by excluding measures corresponding to "too good" investment opportunities.

## Extensions and Generalizations


### 1. Transaction Costs


**Proportional Transaction Costs**: Buying costs $(1+\lambda)S$, selling receives $(1-\mu)S$.

**Shadow Price**: The superhedging price becomes:


$$
\pi^{\text{sup}}(\xi; \lambda, \mu) \geq \pi^{\text{sup}}(\xi; 0, 0)
$$



with strict inequality reflecting the cost of trading.

**Asymptotics**: As $\lambda, \mu \to 0$:


$$
\pi^{\text{sup}}(\xi; \lambda, \mu) \approx \pi^{\text{sup}}(\xi; 0, 0) + O(\sqrt{\lambda + \mu})
$$



under regular conditions.

### 2. Discrete-Time Models


**Discrete Trading**: Trade only at times $0 = t_0 < t_1 < \cdots < t_N = T$.

**Superhedging Price**: 


$$
\pi^{\text{sup}}_{t_0, \ldots, t_N}(\xi) \geq \pi^{\text{sup}}_{\text{continuous}}(\xi)
$$



**Convergence**: As the mesh size $\max_i (t_{i+1} - t_i) \to 0$:


$$
\pi^{\text{sup}}_{t_0, \ldots, t_N}(\xi) \to \pi^{\text{sup}}_{\text{continuous}}(\xi)
$$



### 3. Multiple Assets


**Multi-Dimensional Model**: $S_t = (S_t^1, \ldots, S_t^d) \in \mathbb{R}^d$.

**Superhedging Price**: 


$$
\pi^{\text{sup}}(\xi) = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi]
$$



remains valid.

**Correlation Uncertainty**: When correlation structure is uncertain, $\mathcal{M}$ contains measures with different correlation matrices, widening the bid-ask spread.

### 4. Path-Dependent Claims


**General Path-Dependent Payoff**: 


$$
\xi = g((S_t)_{0 \leq t \leq T})
$$



**Superhedging**: Requires strategies adapted to the entire path, not just terminal value.

**Example**: Lookback option:


$$
\xi = \max_{0 \leq t \leq T} S_t - K
$$



**Superhedging PDE**: For Markovian path functionals, solve HJB equation in augmented state space $(t, S, M)$ where $M = \max_{0 \leq s \leq t} S_s$.

## Case Studies


### 1. Case Study 1: VIX Options


**VIX**: Volatility index measuring implied volatility of S&P 500 options.

**VIX Derivative**: Payoff depends on $\text{VIX}_T$.

**Challenge**: VIX is not directly tradable; only VIX futures and options are available.

**Superhedging**: Use traded VIX futures to construct super-replicating portfolio.

**Model Uncertainty**: Multiple models for VIX dynamics (mean-reverting, Heston, etc.) lead to a set $\mathcal{M}$ of martingale measures.

**Robust Price**:


$$
[\pi^{\text{sub}}, \pi^{\text{sup}}] = \text{arbitrage-free price range}
$$



### 2. Case Study 2: Credit Default Swaps (CDS)


**CDS Payoff**: Pays $1-R$ if default occurs before $T$, where $R$ is the recovery rate.

**Superhedging**: Use corporate bonds or other CDS contracts.

**Default Intensity Uncertainty**: Intensity $\lambda_t$ is uncertain, leading to multiple martingale measures.

**Robust Pricing**:


$$
\pi^{\text{sup}} = \sup_{\lambda \in \Lambda} \mathbb{E}_{\mathbb{Q}^{\lambda}}\left[ e^{-rT} (1-R) \mathbb{1}_{\{\tau < T\}} \right]
$$



where $\tau$ is the default time.

### 3. Case Study 3: Energy Derivatives


**Power Swing Options**: Allow buyer to exercise multiple times, subject to constraints.

**Superhedging**: Complex due to:
- Limited tradability of electricity
- High volatility
- Storage constraints
- Path-dependent exercise rights

**Robust Approach**: Model uncertainty in price dynamics and demand patterns. Compute superhedging price using stochastic dynamic programming.

## Practical Implementation


### 1. Step 1: Model Specification


Define the set of martingale measures $\mathcal{M}$:
- Identify sources of uncertainty (volatility, correlation, jumps, etc.)
- Specify ranges or sets for uncertain parameters

### 2. Step 2: Discretization


Discretize state space and time:
- Choose grid points for asset prices
- Select time steps for rebalancing
- Ensure sufficient granularity for accurate approximation

### 3. Step 3: Optimization


Solve the optimization problem:
- Formulate as LP, QP, or SDP depending on structure
- Use specialized solvers (CPLEX, Gurobi, MOSEK)
- Verify convergence and numerical stability

### 4. Step 4: Validation


Check results against:
- Known analytical solutions (when available)
- Monte Carlo simulations
- Market prices (for calibration and reality check)

### 5. Step 5: Hedging Strategy


Extract optimal hedging strategy from dual solution:
- Identify portfolio weights $\theta_t$
- Implement dynamic hedging algorithm
- Monitor and rebalance periodically

## Summary and Key Insights


### 1. Fundamental Results


1. **Duality Principle**: Dynamic superhedging price equals static optimization over martingale measures:

   $$
   \pi^{\text{sup}}(\xi) = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi]
   $$



2. **No-Arbitrage Bounds**: The arbitrage-free price range is:

   $$
   [\pi^{\text{sub}}(\xi), \pi^{\text{sup}}(\xi)] = \left[ \inf_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi], \, \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} \xi] \right]
   $$



3. **Completeness**: Market completeness $\Leftrightarrow$ Unique EMM $\Leftrightarrow$ Zero bid-ask spread

4. **Robustness**: Superhedging provides model-independent pricing, robust to misspecification within the set $\mathcal{M}$

### 2. Practical Implications


**For Pricing**:
- Superhedging gives upper bound on fair price
- Sub-replication gives lower bound
- Actual trading price typically lies in between

**For Hedging**:
- Superhedging strategy provides complete protection
- May be expensive for exotic derivatives
- Trade-off between hedging cost and residual risk

**For Risk Management**:
- Worst-case scenarios correspond to extremal measures in $\mathcal{M}$
- Robust pricing quantifies model risk
- Sensitivity analysis identifies key model parameters

### 3. Theoretical Significance


Superhedging duality bridges:
- Dynamic portfolio optimization (primal problem)
- Static measure optimization (dual problem)
- Functional analysis (Hahn-Banach theorem, separation)
- Convex optimization (duality theory)

This connection provides both deep theoretical insights and practical computational tools for robust derivative pricing under model uncertainty.
