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

**Recall** (see [§ Fundamental Theorem of Asset Pricing](../../ch01/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md)): no arbitrage $\Leftrightarrow \mathcal{M} \neq \emptyset$ (first FTAP), and the market is complete $\Leftrightarrow \mathcal{M}$ is a singleton (second FTAP).

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

---

## Exercises

**Exercise 1.** In a single-period binomial model with $S_0 = 100$, $S_1 \in \{80, 130\}$, and $r = 0$, compute the superhedging price and the sub-replication price for a European put with strike $K = 100$. Verify that the unique equivalent martingale measure yields a price within the interval $[\pi^{\text{sub}}, \pi^{\text{sup}}]$.

??? success "Solution to Exercise 1"

    **Setup.** $S_0 = 100$, $S_1 \in \{80, 130\}$, $r = 0$. The European put payoff with $K = 100$ is:

    $$
    \xi = (100 - S_1)^+ = \begin{cases} 20 & \text{if } S_1 = 80 \\ 0 & \text{if } S_1 = 130 \end{cases}
    $$

    **Equivalent martingale measure.** For $\mathbb{Q}$ to be an EMM with $r = 0$:

    $$
    \mathbb{E}_\mathbb{Q}[S_1] = S_0 \implies 80q + 130(1 - q) = 100 \implies 50q = 30 \implies q = \frac{3}{5}
    $$

    So $\mathbb{Q}(S_1 = 80) = 3/5$ and $\mathbb{Q}(S_1 = 130) = 2/5$.

    Since the model is a complete binomial model, the EMM is unique, and:

    $$
    \pi^{\text{sup}} = \pi^{\text{sub}} = \mathbb{E}_\mathbb{Q}[\xi] = \frac{3}{5}(20) + \frac{2}{5}(0) = 12
    $$

    **Verification via replication.** The replicating portfolio $(\theta^0, \theta^1)$ satisfies:

    $$
    \theta^0 + 80\theta^1 = 20, \quad \theta^0 + 130\theta^1 = 0
    $$

    Subtracting: $-50\theta^1 = 20$, so $\theta^1 = -2/5$. Then $\theta^0 = 130 \cdot 2/5 = 52$.

    Initial portfolio value: $V_0 = \theta^0 + 100\theta^1 = 52 - 40 = 12$. $\checkmark$

    The price $12$ lies in $[\pi^{\text{sub}}, \pi^{\text{sup}}] = [12, 12]$, consistent with the complete market. $\checkmark$

---

**Exercise 2.** Consider a trinomial model with $S_0 = 100$, $S_1 \in \{80, 100, 120\}$, and $r = 0$. Characterize the set of equivalent martingale measures $\mathcal{M}$ by parameterizing the probabilities $(q_1, q_2, q_3)$ of the three outcomes. For a digital call paying $1$ if $S_1 > 100$, compute

$$
\pi^{\text{sup}} = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[\xi] \quad \text{and} \quad \pi^{\text{sub}} = \inf_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[\xi]
$$

??? success "Solution to Exercise 2"

    **EMM characterization.** With $S_0 = 100$, $S_1 \in \{80, 100, 120\}$, and $r = 0$:

    Martingale condition: $80q_1 + 100q_2 + 120q_3 = 100$

    Normalization: $q_1 + q_2 + q_3 = 1$

    Non-negativity: $q_1, q_2, q_3 \geq 0$

    Subtracting: $-20q_1 + 20q_3 = 0$, so $q_1 = q_3$. Let $p = q_1 = q_3 \in [0, 1/2]$. Then $q_2 = 1 - 2p$.

    The set of EMMs is:

    $$
    \mathcal{M} = \left\{(p, 1 - 2p, p) : p \in [0, 1/2]\right\}
    $$

    This is a one-parameter family, confirming the market is incomplete (non-unique EMM).

    **Digital call payoff.** $\xi = \mathbb{1}\{S_1 > 100\}$:

    $$
    \xi(80) = 0, \quad \xi(100) = 0, \quad \xi(120) = 1
    $$

    **Expected payoff:** $\mathbb{E}_\mathbb{Q}[\xi] = q_3 = p$.

    **Superhedging price:**

    $$
    \pi^{\text{sup}} = \sup_{p \in [0, 1/2]} p = \frac{1}{2}
    $$

    **Sub-replication price:**

    $$
    \pi^{\text{sub}} = \inf_{p \in [0, 1/2]} p = 0
    $$

    **Verification via hedging.** For the superhedging price $\pi^{\text{sup}} = 1/2$: construct a portfolio $(v, \theta)$ with initial value $v = 1/2$ and $\theta$ shares of stock, such that:

    $$
    v + \theta(S_1 - S_0) \geq \xi(S_1) \text{ for all outcomes}
    $$

    - $S_1 = 80$: $1/2 + \theta(-20) \geq 0 \implies \theta \leq 1/40$
    - $S_1 = 100$: $1/2 + \theta(0) \geq 0$ (always true)
    - $S_1 = 120$: $1/2 + \theta(20) \geq 1 \implies \theta \geq 1/40$

    Setting $\theta = 1/40$: all constraints are satisfied (with equality in the first and third), confirming $\pi^{\text{sup}} = 1/2$. $\checkmark$

---

**Exercise 3.** Prove that for any contingent claim $\xi$ and constant $a > 0$,

$$
\pi^{\text{sup}}(a\xi) = a \cdot \pi^{\text{sup}}(\xi) \quad \text{and} \quad \pi^{\text{sup}}(\xi_1 + \xi_2) \leq \pi^{\text{sup}}(\xi_1) + \pi^{\text{sup}}(\xi_2)
$$

That is, show that the superhedging price functional is positive homogeneous and subadditive (hence a coherent risk measure on payoffs).

??? success "Solution to Exercise 3"

    **Positive homogeneity: $\pi^{\text{sup}}(a\xi) = a \cdot \pi^{\text{sup}}(\xi)$ for $a > 0$.**

    By the dual representation:

    $$
    \pi^{\text{sup}}(a\xi) = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_\mathbb{Q}[e^{-rT} a\xi] = a \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_\mathbb{Q}[e^{-rT} \xi] = a \cdot \pi^{\text{sup}}(\xi)
    $$

    Alternatively, from the primal side: if $\theta$ superhedges $\xi$ starting from capital $v$, then $a\theta$ superhedges $a\xi$ starting from capital $av$ (by linearity of the portfolio value). Conversely, any superhedge of $a\xi$ with capital $w$ yields a superhedge of $\xi$ with capital $w/a$. Taking infima: $\pi^{\text{sup}}(a\xi) = a \cdot \pi^{\text{sup}}(\xi)$. $\square$

    **Subadditivity: $\pi^{\text{sup}}(\xi_1 + \xi_2) \leq \pi^{\text{sup}}(\xi_1) + \pi^{\text{sup}}(\xi_2)$.**

    *Primal argument:* Let $\theta_1$ superhedge $\xi_1$ starting from $v_1 = \pi^{\text{sup}}(\xi_1) + \varepsilon/2$, and let $\theta_2$ superhedge $\xi_2$ starting from $v_2 = \pi^{\text{sup}}(\xi_2) + \varepsilon/2$. Then the combined strategy $\theta_1 + \theta_2$ is self-financing with initial capital $v_1 + v_2$ and satisfies:

    $$
    V_T^{\theta_1 + \theta_2} = V_T^{\theta_1} + V_T^{\theta_2} \geq \xi_1 + \xi_2
    $$

    So $\theta_1 + \theta_2$ superhedges $\xi_1 + \xi_2$ with initial capital $v_1 + v_2 = \pi^{\text{sup}}(\xi_1) + \pi^{\text{sup}}(\xi_2) + \varepsilon$. Since $\varepsilon > 0$ is arbitrary:

    $$
    \pi^{\text{sup}}(\xi_1 + \xi_2) \leq \pi^{\text{sup}}(\xi_1) + \pi^{\text{sup}}(\xi_2)
    $$

    *Dual argument:*

    $$
    \pi^{\text{sup}}(\xi_1 + \xi_2) = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_\mathbb{Q}[e^{-rT}(\xi_1 + \xi_2)] = \sup_{\mathbb{Q}} \left(\mathbb{E}_\mathbb{Q}[e^{-rT}\xi_1] + \mathbb{E}_\mathbb{Q}[e^{-rT}\xi_2]\right)
    $$

    $$
    \leq \sup_{\mathbb{Q}} \mathbb{E}_\mathbb{Q}[e^{-rT}\xi_1] + \sup_{\mathbb{Q}} \mathbb{E}_\mathbb{Q}[e^{-rT}\xi_2] = \pi^{\text{sup}}(\xi_1) + \pi^{\text{sup}}(\xi_2)
    $$

    where the inequality follows because the supremum of a sum is at most the sum of the suprema (the maximizing measures for $\xi_1$ and $\xi_2$ may differ). $\square$

    **Coherent risk measure interpretation.** Combined with the properties that $\pi^{\text{sup}}(\xi + c) = \pi^{\text{sup}}(\xi) + c \cdot e^{-rT}$ (translation invariance, since adding cash $c$ to the payoff shifts the superhedging cost by the discounted amount) and monotonicity ($\xi_1 \leq \xi_2$ a.s. $\implies \pi^{\text{sup}}(\xi_1) \leq \pi^{\text{sup}}(\xi_2)$), the superhedging price functional satisfies all axioms of a coherent risk measure (Artzner et al., 1999).

---

**Exercise 4.** In a model with uncertain volatility $\sigma_t \in [0.15, 0.30]$, current price $S_0 = 100$, strike $K = 100$, maturity $T = 1$, and $r = 0$, compute the superhedging and sub-replication prices for a European call using the Black-Scholes formula with the two extreme volatilities. Explain why the superhedging price corresponds to $\sigma_{\max}$ and the sub-replication price corresponds to $\sigma_{\min}$ for a standard call.

??? success "Solution to Exercise 4"

    **Black-Scholes call prices.** With $S_0 = K = 100$, $T = 1$, $r = 0$:

    $$
    C_{\text{BS}}(\sigma) = S_0\mathcal{N}(d_1) - K\mathcal{N}(d_2)
    $$

    where $d_1 = \sigma/2$ and $d_2 = -\sigma/2$ (since $\log(S_0/K) = 0$ and $r = 0$).

    **At $\sigma_{\max} = 0.30$:**

    $$
    d_1 = 0.15, \quad d_2 = -0.15
    $$

    $$
    C_{\text{BS}}(0.30) = 100[\Phi(0.15) - \Phi(-0.15)] = 100[0.5596 - 0.4404] = 11.92
    $$

    **At $\sigma_{\min} = 0.15$:**

    $$
    d_1 = 0.075, \quad d_2 = -0.075
    $$

    $$
    C_{\text{BS}}(0.15) = 100[\Phi(0.075) - \Phi(-0.075)] = 100[0.5299 - 0.4701] = 5.98
    $$

    **Superhedging and sub-replication prices:**

    $$
    \pi^{\text{sup}} = C_{\text{BS}}(\sigma_{\max}) = C_{\text{BS}}(0.30) \approx 11.92
    $$

    $$
    \pi^{\text{sub}} = C_{\text{BS}}(\sigma_{\min}) = C_{\text{BS}}(0.15) \approx 5.98
    $$

    **Why $\sigma_{\max}$ gives the superhedging price for a call.** The European call price in the Black-Scholes model is a strictly increasing function of $\sigma$ (since vega $> 0$ for all at-the-money options). Therefore:

    $$
    \pi^{\text{sup}} = \sup_{\sigma \in [0.15, 0.30]} C_{\text{BS}}(\sigma) = C_{\text{BS}}(0.30)
    $$

    $$
    \pi^{\text{sub}} = \inf_{\sigma \in [0.15, 0.30]} C_{\text{BS}}(\sigma) = C_{\text{BS}}(0.15)
    $$

    The economic intuition is that a call option is a convex function of the terminal stock price. Higher volatility increases the dispersion of $S_T$, and by Jensen's inequality, the expected value of the convex payoff $(S_T - K)^+$ increases with the variance of $S_T$. The worst case for a call seller (superhedging) is the highest volatility scenario, while the best case for a call buyer (sub-replication) is the lowest volatility scenario.

    More formally, the vega of a European call is:

    $$
    \frac{\partial C}{\partial \sigma} = S_0 \phi(d_1)\sqrt{T} > 0
    $$

    so $C$ is monotonically increasing in $\sigma$, confirming that $\sigma_{\max}$ maximizes and $\sigma_{\min}$ minimizes the call price.

---

**Exercise 5.** The good-deal bound restricts the set of equivalent martingale measures to those with bounded Radon–Nikodym derivative: $\mathcal{M}_{\text{GD}} = \{\mathbb{Q} \in \mathcal{M} : \|d\mathbb{Q}/d\mathbb{P}\|_\infty \leq K\}$. In the trinomial model of Exercise 2, with physical probabilities $\mathbb{P} = (0.3, 0.4, 0.3)$, compute the good-deal bounds for the digital call with $K = 3$, and compare them with the superhedging/sub-replication bounds from Exercise 2.

??? success "Solution to Exercise 5"

    **Setup.** Trinomial model from Exercise 2: $S_0 = 100$, $S_1 \in \{80, 100, 120\}$, $\mathcal{M} = \{(p, 1-2p, p) : p \in [0, 1/2]\}$. Physical measure $\mathbb{P} = (0.3, 0.4, 0.3)$. Digital call $\xi = \mathbb{1}\{S_1 > 100\}$. Good-deal bound parameter $K = 3$.

    **Radon–Nikodym derivative.** For $\mathbb{Q} = (p, 1-2p, p)$:

    $$
    \frac{d\mathbb{Q}}{d\mathbb{P}} = \left(\frac{p}{0.3}, \frac{1-2p}{0.4}, \frac{p}{0.3}\right)
    $$

    **Good-deal constraint:** $\left\|\frac{d\mathbb{Q}}{d\mathbb{P}}\right\|_\infty \leq K = 3$ requires:

    $$
    \frac{p}{0.3} \leq 3 \quad \implies \quad p \leq 0.9
    $$

    $$
    \frac{1-2p}{0.4} \leq 3 \quad \implies \quad 1 - 2p \leq 1.2 \quad \implies \quad p \geq -0.1
    $$

    Combined with $p \in [0, 1/2]$, the good-deal constraint is $p \in [0, 1/2]$ (all EMMs satisfy the bound with $K = 3$).

    Wait, let us check more carefully. We need $\frac{d\mathbb{Q}}{d\mathbb{P}}(\omega) \leq 3$ for all $\omega$:

    - $\omega_1$: $p / 0.3 \leq 3 \implies p \leq 0.9$ (satisfied for $p \leq 1/2$)
    - $\omega_2$: $(1 - 2p) / 0.4 \leq 3 \implies 1 - 2p \leq 1.2 \implies p \geq -0.1$ (always satisfied)
    - $\omega_3$: $p / 0.3 \leq 3 \implies p \leq 0.9$ (satisfied)

    So for $K = 3$, the good-deal constraint does not restrict the EMM set at all: $\mathcal{M}_{\text{GD}} = \mathcal{M}$.

    Let us also check whether the Radon–Nikodym derivative must be bounded below (some formulations require this). If we additionally require $\frac{d\mathbb{Q}}{d\mathbb{P}} \geq 1/K = 1/3$:

    - $\omega_1$: $p / 0.3 \geq 1/3 \implies p \geq 0.1$
    - $\omega_2$: $(1-2p) / 0.4 \geq 1/3 \implies 1 - 2p \geq 2/15 \implies p \leq 13/30 \approx 0.433$
    - $\omega_3$: $p / 0.3 \geq 1/3 \implies p \geq 0.1$

    Under this two-sided constraint, $\mathcal{M}_{\text{GD}} = \{(p, 1-2p, p) : p \in [0.1, 13/30]\}$.

    With the $\|\cdot\|_\infty \leq K$ constraint alone (as stated in the exercise):

    $$
    \pi^{\text{GD, sup}} = \sup_{p \in [0, 1/2]} p = \frac{1}{2}, \quad \pi^{\text{GD, sub}} = \inf_{p \in [0, 1/2]} p = 0
    $$

    These equal the superhedging/sub-replication bounds from Exercise 2, since $K = 3$ is not restrictive enough.

    With the two-sided constraint $1/3 \leq d\mathbb{Q}/d\mathbb{P} \leq 3$:

    $$
    \pi^{\text{GD, sup}} = \sup_{p \in [0.1, 13/30]} p = \frac{13}{30} \approx 0.433
    $$

    $$
    \pi^{\text{GD, sub}} = \inf_{p \in [0.1, 13/30]} p = 0.1
    $$

    **Comparison:** The good-deal bounds (with two-sided constraint) are $[0.1, 0.433]$, which is strictly tighter than the superhedging/sub-replication bounds $[0, 0.5]$ from Exercise 2. The good-deal bounds exclude extreme EMMs that would require implausibly large Radon–Nikodym derivatives, thereby narrowing the arbitrage-free price range.

---

**Exercise 6.** Consider a two-period model where at each step the stock either goes up by 20% or down by 20%, with $S_0 = 100$ and $r = 0$. Formulate the superhedging problem for a lookback payoff $\xi = \max(S_0, S_1, S_2) - S_2$ as a dynamic programming problem. Compute the superhedging price and the corresponding hedging strategy at each node.

??? success "Solution to Exercise 6"

    **Model setup.** Two-period binomial: $u = 1.2$, $d = 0.8$, $S_0 = 100$, $r = 0$.

    The tree has nodes:

    - $t = 0$: $S_0 = 100$
    - $t = 1$: $S_1^u = 120$, $S_1^d = 80$
    - $t = 2$: $S_2^{uu} = 144$, $S_2^{ud} = 96$, $S_2^{du} = 96$, $S_2^{dd} = 64$

    **Lookback payoff.** $\xi = \max(S_0, S_1, S_2) - S_2$:

    - Path $uu$: $\max(100, 120, 144) - 144 = 0$
    - Path $ud$: $\max(100, 120, 96) - 96 = 24$
    - Path $du$: $\max(100, 80, 96) - 96 = 4$
    - Path $dd$: $\max(100, 80, 64) - 64 = 36$

    **Risk-neutral probability.** At each node: $qu + (1-q)d = 1$ (since $r = 0$), so $1.2q + 0.8(1-q) = 1$, giving $q = 1/2$.

    Since the model is complete (binomial), $\pi^{\text{sup}} = \pi^{\text{sub}} = \mathbb{E}_\mathbb{Q}[\xi]$.

    **Dynamic programming (backward induction).**

    *At $t = 1$, node $u$ ($S_1 = 120$, running max $M_1 = 120$):*

    $$
    V_1^u = \frac{1}{2}(0) + \frac{1}{2}(24) = 12
    $$

    *At $t = 1$, node $d$ ($S_1 = 80$, running max $M_1 = 100$):*

    $$
    V_1^d = \frac{1}{2}(4) + \frac{1}{2}(36) = 20
    $$

    *At $t = 0$:*

    $$
    V_0 = \frac{1}{2}(12) + \frac{1}{2}(20) = 16
    $$

    So $\pi^{\text{sup}} = 16$.

    **Hedging strategy.**

    *At $t = 0$:* The hedge ratio is computed from the payoff values at $t = 1$:

    $$
    \theta_0 = \frac{V_1^u - V_1^d}{S_1^u - S_1^d} = \frac{12 - 20}{120 - 80} = \frac{-8}{40} = -0.2
    $$

    Cash position: $\theta_0^{\text{cash}} = V_0 - \theta_0 S_0 = 16 - (-0.2)(100) = 36$.

    *At $t = 1$, node $u$ ($S_1 = 120$):*

    $$
    \theta_1^u = \frac{0 - 24}{144 - 96} = \frac{-24}{48} = -0.5
    $$

    Cash: $V_1^u - \theta_1^u S_1^u = 12 - (-0.5)(120) = 72$.

    *At $t = 1$, node $d$ ($S_1 = 80$):*

    $$
    \theta_1^d = \frac{4 - 36}{96 - 64} = \frac{-32}{32} = -1
    $$

    Cash: $V_1^d - \theta_1^d S_1^d = 20 - (-1)(80) = 100$.

    **Summary of hedging strategy:**

    | Time | Node | Stock holding $\theta$ | Cash |
    |------|------|----------------------|------|
    | $t=0$ | $S_0 = 100$ | $-0.2$ | $36$ |
    | $t=1$ | $S_1 = 120$ | $-0.5$ | $72$ |
    | $t=1$ | $S_1 = 80$ | $-1.0$ | $100$ |

    The negative stock holdings reflect the lookback payoff's nature: the lookback put benefits from the stock going down (increasing the gap between the running max and the terminal value), so the hedge is short the stock.

---

**Exercise 7.** Prove that under proportional transaction costs with parameter $\lambda > 0$ (buying at $(1+\lambda)S$ and selling at $(1-\lambda)S$), the superhedging price of a European call satisfies

$$
\pi^{\text{sup}}(\xi; \lambda) \geq \pi^{\text{sup}}(\xi; 0)
$$

Provide an economic interpretation of why transaction costs increase the superhedging cost, and explain the heuristic that the leading-order correction scales as $O(\sqrt{\lambda})$.

??? success "Solution to Exercise 7"

    **Proof that $\pi^{\text{sup}}(\xi; \lambda) \geq \pi^{\text{sup}}(\xi; 0)$.**

    The frictionless superhedging price is:

    $$
    \pi^{\text{sup}}(\xi; 0) = \inf\{v : \exists \theta \in \mathcal{A}(0), V_0^\theta = v, V_T^\theta \geq \xi \text{ a.s.}\}
    $$

    where $\mathcal{A}(0)$ is the set of admissible strategies with zero transaction costs.

    With proportional transaction costs $\lambda > 0$, the set of admissible strategies $\mathcal{A}(\lambda)$ is restricted: each trade incurs a cost, so the self-financing condition becomes:

    $$
    dV_t^\theta = \theta_t \, dS_t - \lambda S_t |d\theta_t|
    $$

    where $\lambda S_t |d\theta_t|$ represents the transaction cost of rebalancing.

    The key observation is that $\mathcal{A}(\lambda) \subseteq \mathcal{A}(0)$ in the following sense: any strategy that is feasible with transaction costs is also feasible without them (since zero-cost trading is a special case of $\lambda$-cost trading where the costs happen to be zero). However, the converse is false: a frictionless strategy may not be affordable with transaction costs.

    More precisely, for any superhedging strategy $\theta$ under transaction costs with initial capital $v$:

    $$
    V_T^\theta = v + \int_0^T \theta_t \, dS_t - \lambda \int_0^T S_t |d\theta_t| \leq v + \int_0^T \theta_t \, dS_t
    $$

    If this strategy superhedges $\xi$ (i.e., $V_T^\theta \geq \xi$), then the frictionless version of the same strategy (with the same trading rule but no costs) has terminal value at least as large. This means the frictionless superhedging price is at most $v$. But the converse fails: a frictionless strategy requiring many trades may not superhedge when costs are deducted.

    Formally, since the feasible set of superhedging strategies shrinks when costs are introduced (fewer strategies can afford to superhedge), the infimum over a smaller set is at least as large:

    $$
    \pi^{\text{sup}}(\xi; \lambda) = \inf_{\theta \in \mathcal{A}(\lambda)} \{v : V_T^\theta \geq \xi\} \geq \inf_{\theta \in \mathcal{A}(0)} \{v : V_T^\theta \geq \xi\} = \pi^{\text{sup}}(\xi; 0)
    $$

    $\square$

    **Economic interpretation.** Transaction costs reduce the efficiency of hedging: every time the hedger adjusts the portfolio, a fraction $\lambda$ of the trade value is lost. To guarantee that the portfolio still dominates the claim $\xi$ at maturity despite these losses, the hedger must start with more capital. The superhedging cost increases because the hedger needs a "cushion" to absorb cumulative transaction costs along the worst-case path.

    **$O(\sqrt{\lambda})$ scaling heuristic.** The leading-order correction to the superhedging price scales as $O(\sqrt{\lambda})$, not $O(\lambda)$. The reasoning is as follows:

    In a Black-Scholes-type model with continuous rebalancing, the delta-hedging strategy has gamma $\Gamma$, and the optimal rebalancing frequency under transaction costs balances the hedging error against the cost of trading.

    - With rebalancing interval $\Delta t$, the hedging error per step is $O(\Gamma (\Delta S)^2) = O(\Gamma \sigma^2 S^2 \Delta t)$.
    - The transaction cost per step is $O(\lambda S |\Delta \theta|) = O(\lambda S |\Gamma \Delta S|) = O(\lambda \Gamma \sigma S^2 \sqrt{\Delta t})$.
    - The total cost over $[0, T]$ with $N = T/\Delta t$ steps is $O(N \cdot \lambda \Gamma \sigma S^2 \sqrt{\Delta t}) = O(\lambda \Gamma \sigma S^2 T / \sqrt{\Delta t})$.

    The optimal $\Delta t$ minimizes total cost (hedging error + transaction costs). The hedging error scales as $O(\Gamma \sigma^2 S^2 T)$ (independent of $N$ in expectation for the superhedging problem), so the dominant contribution is from transaction costs:

    $$
    \text{Total transaction cost} \sim \lambda^{1/2} \cdot (\text{terms involving } \Gamma, \sigma, S, T)
    $$

    when one optimizes over the rebalancing frequency. The $\sqrt{\lambda}$ scaling arises because the optimal strategy trades less frequently as $\lambda$ increases (with $\Delta t \propto \lambda^{2/3}$), but the net effect on the superhedging price gives a $\sqrt{\lambda}$ correction. This was established rigorously by Leland (1985) and refined by subsequent authors.
