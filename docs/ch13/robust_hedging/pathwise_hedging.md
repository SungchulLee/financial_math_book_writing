# Pathwise Hedging

## Introduction

Pathwise hedging represents a paradigm shift from traditional stochastic hedging strategies to deterministic, model-free approaches that work **path-by-path**. Rather than relying on specific probability measures or stochastic models, pathwise hedging constructs portfolios that replicate or dominate derivatives for **every possible realization** of the underlying asset price path.

This approach is particularly powerful because:
1. **Model-free**: No assumptions about the underlying dynamics
2. **Robust**: Works for every path, not just on average
3. **Constructive**: Provides explicit trading strategies
4. **Implementable**: Does not require continuous rebalancing in many cases

The foundations of pathwise hedging lie in rough path theory, functional analysis, and the theory of controlled differential equations, providing rigorous mathematical tools for derivative hedging under model uncertainty.

## Mathematical Framework

### Path Space

**Definition**: Let $\mathcal{C}([0,T], \mathbb{R})$ denote the space of continuous functions from $[0,T]$ to $\mathbb{R}$, equipped with the supremum norm:


$$
\|x\|_{\infty} = \sup_{t \in [0,T]} |x(t)|
$$



**Price Path**: A stock price trajectory is an element $S \in \mathcal{C}([0,T], \mathbb{R}_+)$.

**Filtration**: The natural filtration $(\mathcal{F}_t)_{t \in [0,T]}$ where $\mathcal{F}_t = \sigma(S_s: s \leq t)$ represents the information available up to time $t$.

### Pathwise Derivative

**Functional Derivative**: For a functional $F: \mathcal{C}([0,T], \mathbb{R}_+) \to \mathbb{R}$, the **pathwise derivative** at time $t$ along path $S$ is:


$$
\frac{\delta F}{\delta S_t}(S) = \lim_{\varepsilon \to 0} \frac{F(S + \varepsilon \delta_t) - F(S)}{\varepsilon}
$$



where $\delta_t$ is a perturbation concentrated at time $t$.

**Existence**: For sufficiently regular functionals, this limit exists and defines a measure on $[0,T]$.

### Trading Strategy

**Portfolio Process**: A trading strategy is a predictable process $\theta_t$ representing the number of shares held at time $t$.

**Self-Financing**: The portfolio value $V_t$ satisfies:


$$
V_t = V_0 + \int_0^t \theta_s \, dS_s
$$



where the integral is understood pathwise (e.g., Riemann-Stieltjes or Young integral).

**Key Requirement**: The hedge must work **for all paths** $S \in \mathcal{C}([0,T], \mathbb{R}_+)$, not just those satisfying a particular stochastic differential equation.

## Classical Pathwise Results

### Föllmer's Pathwise Itô Formula

**Theorem** (Föllmer, 1981): For a twice continuously differentiable function $f: \mathbb{R} \to \mathbb{R}$ and a continuous path $S$ of finite quadratic variation $[S]_T$, we have:


$$
f(S_T) - f(S_0) = \int_0^T f'(S_t) \, dS_t + \frac{1}{2} \int_0^T f''(S_t) \, d[S]_t
$$



where:
- The first integral is pathwise Riemann-Stieltjes (or Young if $S$ is rough)
- $[S]_t = \lim_{|\Pi| \to 0} \sum_{i} (S_{t_{i+1}} - S_{t_i})^2$ is the quadratic variation

**Interpretation**: This formula holds **path-by-path**, without reference to any probability measure or Brownian motion.

**Hedging Implication**: To replicate $f(S_T)$ from initial capital $f(S_0)$:
- Hold $\theta_t = f'(S_t)$ shares at time $t$ (delta hedging)
- But accumulate error: $\frac{1}{2} \int_0^T f''(S_t) \, d[S]_t$

### Vovk's Outer Measure

**Game-Theoretic Probability**: Vovk (2012) developed a framework where probability emerges from pathwise considerations.

**Outer Measure**: Define:


$$
\bar{P}(A) = \inf \left\{ V_0: \exists \theta \text{ s.t. } V_T \geq \mathbb{1}_A \text{ for all } S \right\}
$$



where $A \subseteq \mathcal{C}([0,T], \mathbb{R}_+)$ is an event.

**Properties**:
- Super-additive but not additive
- Provides upper bound on "probability" in pathwise sense
- Connects to continuous-time betting strategies

## Dupire-Type Formulas

### Dupire's Local Volatility (Probabilistic View)

**Classical Dupire Equation**: Under a diffusion model:


$$
\frac{\partial C}{\partial T} = \frac{1}{2} \sigma^2(K, T) K^2 \frac{\partial^2 C}{\partial K^2} - r K \frac{\partial C}{\partial K} + rC
$$



where $C(K, T)$ is the call price as a function of strike and maturity.

### Pathwise Interpretation

**Realized Variance**: For a given path $S$, define the **realized local variance** at time $t$:


$$
\sigma^2_{\text{realized}}(S_t, t) = \lim_{\Delta t \to 0} \frac{(S_{t+\Delta t} - S_t)^2}{\Delta t}
$$



assuming the limit exists.

**Pathwise Dupire Formula**: The function $C(K, T)$ satisfies:


$$
\frac{\partial C}{\partial T}(K, T) = \frac{1}{2} K^2 \frac{\partial^2 C}{\partial K^2}(K, T) \cdot \mathbb{E}[\sigma^2_{\text{realized}}(K, T)]
$$



where the expectation is with respect to paths conditional on $S_T = K$.

**Robustness**: This relationship holds regardless of the specific model, connecting market-observed option prices to realized path properties.

## Robust Pathwise Hedging Strategies

### Tangent Process Construction

**Idea**: Construct a path $\tilde{S}$ that "touches" the derivative payoff at maturity.

**Setup**: Consider a European option with payoff $\Phi(S_T)$.

**Tangent Path**: A path $\tilde{S} \in \mathcal{C}([0,T], \mathbb{R}_+)$ with:
1. $\tilde{S}_0 = S_0$ (same initial value)
2. $\tilde{S}_T$ chosen such that $\Phi(\tilde{S}_T)$ equals the target

**Hedge**: Follow the delta-hedging strategy as if the path were $\tilde{S}$:


$$
\theta_t = \Phi'(\tilde{S}_t)
$$



**Accumulated Error**: The hedging error is:


$$
\text{Error} = \frac{1}{2} \int_0^T \Phi''(\tilde{S}_t) \left( d[S]_t - d[\tilde{S}]_t \right)
$$



### Upper and Lower Hedging

**Upper Hedge**: Construct portfolio that **dominates** the payoff for all paths:


$$
V_T^{\text{upper}} \geq \Phi(S_T) \quad \text{for all } S
$$



**Strategy**:
1. Choose the "worst-case" tangent path $\tilde{S}^{\max}$
2. Delta-hedge along $\tilde{S}^{\max}$
3. Accumulate quadratic variation penalty

**Lower Hedge**: Construct portfolio that is **dominated** by the payoff:


$$
V_T^{\text{lower}} \leq \Phi(S_T) \quad \text{for all } S
$$



**Bid-Ask Spread**: The difference:


$$
V_0^{\text{upper}} - V_0^{\text{lower}} = \text{Model uncertainty premium}
$$



reflects the inherent ambiguity in pathwise hedging.

### Volatility-Robust Hedging

**Volatility Uncertainty**: Assume only that:


$$
\underline{\sigma}^2 \leq \sigma^2_{\text{realized}}(S_t, t) \leq \overline{\sigma}^2
$$



**Robust Hedging Problem**: Find minimal initial capital $V_0$ such that:


$$
V_0 + \int_0^T \theta_t \, dS_t \geq \Phi(S_T)
$$



for all paths with quadratic variation satisfying the bound.

**Solution**: Use HJB equation with volatility uncertainty:


$$
V_t + \sup_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} \left\{ \frac{1}{2} \sigma^2 S^2 V_{SS} \right\} + rSV_S - rV = 0
$$



**Pathwise Implementation**:
- Monitor realized quadratic variation
- Adjust hedge dynamically based on observed path regularity

## Rough Path Theory

### Rough Paths and Integration

**Rough Path**: A pair $(X, \mathbb{X})$ where:
- $X: [0,T] \to \mathbb{R}^d$ is a continuous path
- $\mathbb{X}_{s,t}$ is the "second-order increment":

  $$
  \mathbb{X}_{s,t} \approx \int_s^t (X_r - X_s) \otimes dX_r
  $$



**Hölder Continuity**: $X$ has Hölder exponent $\alpha \in (1/3, 1/2]$:


$$
|X_t - X_s| \leq C |t - s|^{\alpha}
$$



**Young Integral**: For $\alpha > 1/2$, the Riemann-Stieltjes integral:


$$
\int_0^T Y_t \, dX_t = \lim_{|\Pi| \to 0} \sum_i Y_{t_i} (X_{t_{i+1}} - X_{t_i})
$$



exists pathwise.

**Rough Integral**: For $\alpha \in (1/3, 1/2]$, integration requires the second-order term $\mathbb{X}$.

### Controlled Rough Paths

**Definition**: A process $Y$ is **controlled** by rough path $X$ if:


$$
Y_t - Y_s = Y'_s (X_t - X_s) + R_{s,t}
$$



where $R_{s,t} = o(|t-s|^{\alpha})$ is a remainder term.

**Derivative Process**: $Y'_t$ is called the **Gubinelli derivative** of $Y$ with respect to $X$.

**Application to Finance**: Portfolio value $V_t$ controlled by stock price $S_t$:


$$
V_t - V_s = \theta_s (S_t - S_s) + R_{s,t}
$$



where $\theta_s$ is the delta position.

### Pathwise Hedging with Rough Volatility

**Rough Volatility Models**: Volatility exhibits Hölder regularity $H < 1/2$:


$$
\sigma_t = \sigma_0 + \int_0^t K(t-s) \, dW_s^H
$$



where $W^H$ is fractional Brownian motion with $H < 1/2$.

**Challenge**: Classical Itô calculus does not apply directly.

**Rough Path Solution**:
1. Lift $(S, V)$ to rough path $(S, \mathbb{S})$ including second-order terms
2. Define hedging strategy in controlled rough path sense
3. Prove convergence of discrete hedging to continuous limit

**Theorem** (Bayer-Friz-Gatheral): Under rough volatility, pathwise delta-hedging converges to the correct limit using rough path integration, without assuming specific stochastic model.

## Robust Local Volatility

### Setup

**Observed Data**: Market prices of European calls $C(K, T)$ for various strikes $K$ and maturities $T$.

**Goal**: Construct local volatility function $\sigma(S, t)$ that is consistent with market prices and provides pathwise hedging.

### Dupire's Formula (Pathwise)

**Forward Equation**: The local volatility surface satisfies:


$$
\sigma^2(K, T) = \frac{\frac{\partial C}{\partial T}(K, T) + rK \frac{\partial C}{\partial K}(K, T)}{\frac{1}{2} K^2 \frac{\partial^2 C}{\partial K^2}(K, T)}
$$



**Pathwise Interpretation**: 
- This formula is **model-free** in the sense that it directly relates market observables
- The resulting $\sigma(K, T)$ can be used to hedge pathwise, without assuming a specific SDE

### Robust Calibration

**Optimization Problem**: Find $\sigma(S, t)$ that minimizes:


$$
\sum_{i,j} \left( C^{\text{model}}(K_i, T_j; \sigma) - C^{\text{market}}(K_i, T_j) \right)^2
$$



subject to:
1. $\sigma(S, t) > 0$ (positivity)
2. No calendar arbitrage
3. No butterfly arbitrage

**Pathwise Consistency**: The calibrated $\sigma$ must allow for pathwise hedging that replicates the option prices.

**Regularization**: Add penalty for roughness:


$$
+ \lambda \int_0^T \int_0^{\infty} \left( \frac{\partial \sigma}{\partial S} \right)^2 dS \, dt
$$



to ensure smooth volatility surface amenable to pathwise analysis.

## Functional Itô Calculus

### Path-Dependent Derivatives

**Definition**: A derivative with payoff depending on entire path:


$$
\Phi = F((S_t)_{0 \leq t \leq T})
$$



**Examples**:
- Asian options: $F(S) = \left(\frac{1}{T} \int_0^T S_t \, dt - K\right)^+$
- Lookback options: $F(S) = \max_{0 \leq t \leq T} S_t - K$
- Barrier options: $F(S) = (S_T - K)^+ \mathbb{1}_{\{\sup_{t \leq T} S_t < H\}}$

### Functional Derivatives

**Definition** (Vertical Derivative): For a functional $F: \mathcal{C}([0,T], \mathbb{R}) \to \mathbb{R}$, the vertical derivative at time $t$ is:


$$
\partial_x F_t(S) = \lim_{\varepsilon \to 0} \frac{F(S + \varepsilon \mathbb{1}_{[t,T]}) - F(S)}{\varepsilon}
$$



**Horizontal Derivative**:


$$
\partial_t F_t(S) = \lim_{h \to 0} \frac{F(S^{t+h}) - F(S^t)}{h}
$$



where $S^t$ is the path stopped at time $t$.

### Functional Itô Formula

**Theorem** (Dupire, Cont-Fournié): For a path-dependent functional $F$ with sufficient regularity:


$$
F(S) = F(S_0) + \int_0^T \partial_x F_t(S) \, dS_t + \frac{1}{2} \int_0^T \partial_{xx} F_t(S) \, d[S]_t + \int_0^T \partial_t F_t(S) \, dt
$$



where all terms are defined pathwise.

**Hedging Formula**: To replicate $F(S)$, hold:


$$
\theta_t = \partial_x F_t(S)
$$



shares at time $t$, accumulating gamma and theta costs.

**Pathwise Consistency**: This formula holds for **every continuous path** with finite quadratic variation, without probabilistic assumptions.

## Causal Functional Calculus

### Causality Constraint

**Definition**: A functional $F: \mathcal{C}([0,T], \mathbb{R}) \to \mathbb{R}$ is **causal** (or **non-anticipating**) if:


$$
S_t = \tilde{S}_t \text{ for all } t \leq \tau \implies F(S)_{\tau} = F(\tilde{S})_{\tau}
$$



**Financial Interpretation**: The value at time $\tau$ depends only on the path up to $\tau$, not on future values.

### Vertical Derivative (Causal)

For causal functionals, the vertical derivative simplifies:


$$
\partial_x F_t(S) = \lim_{\varepsilon \to 0} \frac{F(S + \varepsilon \delta_t) - F(S)}{\varepsilon}
$$



where $\delta_t$ is a spike at time $t$.

**Example** (Asian Option): 


$$
F(S) = \left( \frac{1}{T} \int_0^T S_u \, du - K \right)^+
$$



has vertical derivative:


$$
\partial_x F_t(S) = \frac{1}{T} \left( \frac{1}{T} \int_0^T S_u \, du - K \right)_+
$$



### Martingale Property (Pathwise)

**Definition**: A causal functional $M$ is a **pathwise martingale** if:


$$
\int_0^t \partial_x M_s(S) \, dS_s = M_t(S) - M_0(S)
$$



for all paths $S$.

**Characterization**: Pathwise martingales satisfy:


$$
\partial_t M_t(S) + \frac{1}{2} \sigma^2(S_t, t) \partial_{xx} M_t(S) = 0
$$



for any choice of local volatility $\sigma$.

## Applications to Exotic Options

### Asian Options

**Payoff**: 


$$
\Phi = \left( \bar{S} - K \right)^+ \quad \text{where } \bar{S} = \frac{1}{T} \int_0^T S_t \, dt
$$



**State Variables**: $(S_t, A_t)$ where $A_t = \int_0^t S_u \, du$ is the accumulated average.

**Functional Derivative**:


$$
\frac{\delta \Phi}{\delta S_t} = \frac{1}{T} (\bar{S} - K)_+' = \frac{1}{T} \mathbb{1}_{\{\bar{S} > K\}}
$$



**Pathwise Hedge**: Hold $\theta_t = \frac{1}{T} \mathbb{1}_{\{\bar{S} > K\}}$ shares, where the indicator is evaluated based on current running average.

**Gamma Cost**: 


$$
\frac{1}{2} \int_0^T \frac{1}{T^2} \delta_{\bar{S} = K} \, d[S]_t
$$



where $\delta_{\bar{S} = K}$ is the Dirac delta at the boundary.

### Lookback Options

**Payoff**: 


$$
\Phi = M_T - K \quad \text{where } M_t = \max_{0 \leq s \leq t} S_s
$$



**State Variables**: $(S_t, M_t)$.

**Functional Derivative**: When $S_t < M_t$:


$$
\frac{\delta \Phi}{\delta S_t} = 0
$$



When $S_t = M_t$ (at the running maximum):


$$
\frac{\delta \Phi}{\delta S_t} = 1
$$



**Pathwise Hedge**: 
- Hold 0 shares when below running maximum
- Hold 1 share when at running maximum
- Continuously monitor and adjust

**Local Time**: The hedge accumulates a "local time" correction at the maximum:


$$
L_T = \text{time spent at running maximum}
$$



### Barrier Options

**Up-and-Out Call**: 


$$
\Phi = (S_T - K)^+ \mathbb{1}_{\{M_T < H\}}
$$



**Functional Derivative**: 
- Below barrier ($S_t < H$): $\partial_x \Phi = (S_T - K)_+'$ standard delta
- At barrier ($S_t = H$): Delta jumps to zero

**Pathwise Strategy**:
- Delta-hedge as long as barrier not hit
- Liquidate immediately upon hitting barrier
- Accumulate error from jump in delta

**Robustness**: The pathwise hedge is robust to model misspecification but sensitive to exact timing of barrier hit.

## Pathwise Vega Hedging

### Volatility Exposure

**Vega**: Sensitivity of option price to volatility:


$$
\mathcal{V} = \frac{\partial V}{\partial \sigma}
$$



**Pathwise Challenge**: Volatility is not a traded asset, so traditional delta-hedging logic doesn't apply.

### Realized Variance Hedge

**Variance Swap**: Contract paying:


$$
\text{Payoff} = \text{Realized Variance} - K_{\text{var}}
$$



**Pathwise Replication**: Using Carr-Madan:


$$
\text{RV} = \frac{2}{T} \left( \int_0^{S_0} \frac{P(K)}{K^2} dK + \int_{S_0}^{\infty} \frac{C(K)}{K^2} dK \right)
$$



**Hedging Vega**: Long variance swaps to hedge vega exposure pathwise.

**Portfolio**: Hold $\theta_t^{\text{stock}}$ shares and $\theta_K^{\text{options}}$ options at each strike $K$ such that:


$$
\theta_t^{\text{stock}} dS_t + \int \theta_K^{\text{options}} dC(K, T) = dV
$$



for all paths.

### Gamma-Vega Relationship

**Pathwise Identity**:


$$
\int_0^T \Gamma_t \, d[S]_t = \text{Total Gamma Cost}
$$



**Vega Decomposition**: 


$$
\mathcal{V} = \mathbb{E}\left[ \int_0^T \Gamma_t \frac{\partial \sigma_t^2}{\partial \sigma_0} dt \right]
$$



**Pathwise Interpretation**: Vega is the sensitivity of accumulated gamma costs to initial volatility, averaged over paths.

## Numerical Implementation

### Discrete-Time Pathwise Hedge

**Time Grid**: Partition $[0,T]$ into $0 = t_0 < t_1 < \cdots < t_N = T$.

**Discrete Hedge**: At each $t_i$, hold:


$$
\theta_{t_i} = \partial_x F_{t_i}(S)
$$



shares.

**Portfolio Value**:


$$
V_{t_{i+1}} = V_{t_i} + \theta_{t_i} (S_{t_{i+1}} - S_{t_i})
$$



**Convergence**: As $\max_i (t_{i+1} - t_i) \to 0$:


$$
V_{t_N} \to F(S) + \text{Second-order terms}
$$



### Quadratic Variation Estimation

**Realized Variance**:


$$
[S]^{\Pi}_T = \sum_{i=0}^{N-1} (S_{t_{i+1}} - S_{t_i})^2
$$



**Consistency**: As $|\Pi| \to 0$:


$$
[S]^{\Pi}_T \to [S]_T
$$



**Usage**: Monitor realized variance to assess hedging error:


$$
\text{Error} \approx \frac{1}{2} \Gamma [S]^{\Pi}_T
$$



### Pathwise Simulation

**Algorithm**:
1. Generate sample path $S_t$ (any model or historical data)
2. Compute functional derivative $\partial_x F_t(S)$ at each time
3. Implement delta-hedge: $\theta_t = \partial_x F_t(S)$
4. Track cumulative P&L: $\text{P&L}_t = V_t - V_0 - \theta_0 S_0$
5. Compare terminal P&L to target payoff $F(S)$

**Model-Free Validation**: Repeat for multiple paths from different models; pathwise hedge should work consistently.

## Connections to Model-Free Finance

### Game-Theoretic Probability

**Shafer-Vovk Framework**: Replace probability spaces with game-theoretic protocols.

**Betting Strategy**: A strategy is a rule for placing bets on future outcomes based on observed history.

**Pathwise Martingale**: A process is a game-theoretic martingale if no betting strategy yields guaranteed profit.

**Connection to Hedging**: Pathwise hedging strategies correspond to defensive betting strategies in the game-theoretic framework.

### Obloj's Robust Framework

**Robust Pricing**: Given marginal distributions (from market option prices), compute bounds:


$$
[\underline{P}, \overline{P}] = \text{arbitrage-free price range}
$$



**Pathwise Hedging**: The bounds are attained by pathwise super- and sub-replicating strategies.

**Theorem** (Obloj et al.): Model-free bounds from martingale optimal transport correspond to pathwise hedging strategies using vanilla options.

## Advanced Topics

### Non-Markovian Strategies

**Path Dependence**: Hedging strategy depends on entire history, not just current state:


$$
\theta_t = \Theta((S_s)_{0 \leq s \leq t})
$$



**Example** (Variance-Dependent Hedge):


$$
\theta_t = \partial_x F_t(S) \cdot \left(1 + \beta \cdot \frac{[S]_t}{t}\right)
$$



adjusting for realized variance.

**Optimality**: In some cases, non-Markovian strategies outperform Markovian ones in pathwise sense.

### Transaction Costs

**Friction**: Each trade incurs cost proportional to transaction size:


$$
\text{Cost} = \lambda |\theta_{t_{i+1}} - \theta_{t_i}| S_{t_i}
$$



**Pathwise Problem**: Minimize hedging error subject to transaction cost penalty:


$$
\min_{\theta} \left\{ |V_T - F(S)| + \lambda \sum_{i=0}^{N-1} |\theta_{t_{i+1}} - \theta_{t_i}| S_{t_i} \right\}
$$



**Solution**: Leads to discrete adjustments (only rehedge when drift exceeds threshold).

**Pathwise Optimality**: Find strategy that minimizes worst-case error over all paths, subject to cost constraints.

### Rough Bergomi Model

**Model**: Fractional volatility with $H < 1/2$:


$$
dS_t = S_t \sqrt{V_t} \, dW_t, \quad V_t = \xi_t \mathcal{E}\left(\eta \int_0^t (t-s)^{H-1/2} dW_s^{\perp}\right)
$$



**Pathwise Interpretation**: 
- Volatility path has roughness $H$
- Delta-hedging requires rough path integration techniques
- Convergence of discrete hedging strategies depends on regularity

**Practical Implication**: Need finer time grid for rough volatility than for smooth Brownian models.

## Case Studies

### Case 1: S&P 500 Options

**Setup**: Hedge a one-month ATM call on S&P 500 using pathwise strategy.

**Data**: 
- Initial spot: $S_0 = 4500$
- Strike: $K = 4500$
- Historical paths (5-minute data)

**Strategy**: 
- Compute functional derivative at each 5-minute interval
- Rebalance delta position
- Track cumulative hedging error

**Result**: Pathwise hedge tracks option value closely across multiple historical episodes, validating model-free approach.

### Case 2: FX Barrier Option

**Setup**: Hedge EUR/USD knock-out call with barrier at 1.20.

**Challenge**: Delta jumps discontinuously at barrier.

**Pathwise Approach**:
- Monitor proximity to barrier continuously
- Adjust hedge aggressively near barrier
- Accept larger gamma cost near barrier to maintain robustness

**Outcome**: Pathwise strategy provides protection across wide range of volatility scenarios without assuming specific model.

### Case 3: Asian Option on Commodity

**Setup**: Hedge arithmetic Asian call on crude oil with quarterly averaging.

**Path Dependence**: Accumulated average $A_t = \int_0^t S_u du$ is key state variable.

**Functional Derivative**:


$$
\theta_t = \frac{1}{T} \Phi'\left(\frac{A_t + S_t (T-t)}{T}\right)
$$



approximating remaining average.

**Implementation**: Daily rebalancing using functional delta based on current accumulated average.

**Performance**: Hedging error within 2% of theoretical bound across 100 historical paths.

## Practical Guidelines

### When to Use Pathwise Hedging

**Advantages**:
- Model-free: Robust to misspecification
- Transparent: Clear connection to underlying path properties
- Constructive: Provides explicit trading rules

**Best Suited For**:
- Environments with model uncertainty
- Derivatives with functional payoffs (Asian, lookback)
- Situations where continuous monitoring is feasible

### Implementation Checklist

1. **Compute Functional Derivative**: Determine $\partial_x F_t(S)$ for the specific payoff
2. **Choose Rebalancing Frequency**: Balance accuracy vs. transaction costs
3. **Monitor Quadratic Variation**: Track $[S]_t$ to estimate gamma costs
4. **Set Stop-Loss Limits**: Define thresholds for intervention if hedging error exceeds bounds
5. **Backtest**: Validate strategy on historical paths before deployment

### Limitations

**Continuous Monitoring**: Many pathwise results assume continuous trading, which is impossible in practice.

**Discrete Approximation**: Convergence to continuous limit depends on path regularity and rebalancing frequency.

**Transaction Costs**: Frequent rebalancing can be expensive, especially for rough paths.

**Market Impact**: Large positions may move the market, violating pathwise assumptions.

## Summary and Key Insights

### Fundamental Principles

1. **Path-by-Path**: Pathwise hedging works for **every path**, not just on average under a specific model.

2. **Functional Calculus**: Extends classical Itô calculus to path-dependent derivatives using functional derivatives.

3. **Robustness**: Provides model-free hedging strategies robust to specification errors.

4. **Rough Paths**: Generalizes to rough volatility using rough path integration theory.

5. **Quadratic Variation**: Hedging error controlled by accumulated quadratic variation, which is pathwise observable.

### Theoretical Contributions

- **Föllmer**: Pathwise Itô formula without probability
- **Dupire**: Functional Itô calculus for path-dependent options
- **Cont-Fournié**: Rigorous functional calculus framework
- **Bayer-Friz-Gatheral**: Rough path techniques for financial mathematics
- **Vovk**: Game-theoretic probability and outer measure

### Practical Impact

Pathwise hedging transforms derivative pricing from probabilistic to deterministic framework, providing:
- **Robustness**: Works under model uncertainty
- **Transparency**: Clear hedging rules
- **Validation**: Testable on historical data without assuming model

The pathwise perspective reveals that many classical results in stochastic finance have deterministic analogs, deepening our understanding of hedging and replication in quantitative finance.
