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


### 1. Path Space


**Definition**: Let $\mathcal{C}([0,T], \mathbb{R})$ denote the space of continuous functions from $[0,T]$ to $\mathbb{R}$, equipped with the supremum norm:


$$
\|x\|_{\infty} = \sup_{t \in [0,T]} |x(t)|
$$



**Price Path**: A stock price trajectory is an element $S \in \mathcal{C}([0,T], \mathbb{R}_+)$.

**Filtration**: The natural filtration $(\mathcal{F}_t)_{t \in [0,T]}$ where $\mathcal{F}_t = \sigma(S_s: s \leq t)$ represents the information available up to time $t$.

### 2. Pathwise Derivative


**Functional Derivative**: For a functional $F: \mathcal{C}([0,T], \mathbb{R}_+) \to \mathbb{R}$, the **pathwise derivative** at time $t$ along path $S$ is:


$$
\frac{\delta F}{\delta S_t}(S) = \lim_{\varepsilon \to 0} \frac{F(S + \varepsilon \delta_t) - F(S)}{\varepsilon}
$$



where $\delta_t$ is a perturbation concentrated at time $t$.

**Existence**: For sufficiently regular functionals, this limit exists and defines a measure on $[0,T]$.

### 3. Trading Strategy


**Portfolio Process**: A trading strategy is a predictable process $\theta_t$ representing the number of shares held at time $t$.

**Self-Financing**: The portfolio value $V_t$ satisfies:


$$
V_t = V_0 + \int_0^t \theta_s \, dS_s
$$



where the integral is understood pathwise (e.g., Riemann-Stieltjes or Young integral).

**Key Requirement**: The hedge must work **for all paths** $S \in \mathcal{C}([0,T], \mathbb{R}_+)$, not just those satisfying a particular stochastic differential equation.

## Classical Pathwise Results


### 1. Föllmer's Pathwise Itô Formula


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

### 2. Vovk's Outer Measure


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


### 1. Dupire's Local Volatility (Probabilistic View)


**Classical Dupire Equation**: Under a diffusion model:


$$
\frac{\partial C}{\partial T} = \frac{1}{2} \sigma^2(K, T) K^2 \frac{\partial^2 C}{\partial K^2} - r K \frac{\partial C}{\partial K} + rC
$$



where $C(K, T)$ is the call price as a function of strike and maturity.

### 2. Pathwise Interpretation


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


### 1. Tangent Process Construction


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



### 2. Upper and Lower Hedging


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

### 3. Volatility-Robust Hedging


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


### 1. Rough Paths and Integration


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

### 2. Controlled Rough Paths


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

### 3. Pathwise Hedging with Rough Volatility


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


### 1. Setup


**Observed Data**: Market prices of European calls $C(K, T)$ for various strikes $K$ and maturities $T$.

**Goal**: Construct local volatility function $\sigma(S, t)$ that is consistent with market prices and provides pathwise hedging.

### 2. Dupire's Formula (Pathwise)


**Forward Equation**: The local volatility surface satisfies:


$$
\sigma^2(K, T) = \frac{\frac{\partial C}{\partial T}(K, T) + rK \frac{\partial C}{\partial K}(K, T)}{\frac{1}{2} K^2 \frac{\partial^2 C}{\partial K^2}(K, T)}
$$



**Pathwise Interpretation**: 

- This formula is **model-free** in the sense that it directly relates market observables
- The resulting $\sigma(K, T)$ can be used to hedge pathwise, without assuming a specific SDE

### 3. Robust Calibration


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


### 1. Path-Dependent Derivatives


**Definition**: A derivative with payoff depending on entire path:


$$
\Phi = F((S_t)_{0 \leq t \leq T})
$$



**Examples**:

- Asian options: $F(S) = \left(\frac{1}{T} \int_0^T S_t \, dt - K\right)^+$
- Lookback options: $F(S) = \max_{0 \leq t \leq T} S_t - K$
- Barrier options: $F(S) = (S_T - K)^+ \mathbb{1}_{\{\sup_{t \leq T} S_t < H\}}$

### 2. Functional Derivatives


**Definition** (Vertical Derivative): For a functional $F: \mathcal{C}([0,T], \mathbb{R}) \to \mathbb{R}$, the vertical derivative at time $t$ is:


$$
\partial_x F_t(S) = \lim_{\varepsilon \to 0} \frac{F(S + \varepsilon \mathbb{1}_{[t,T]}) - F(S)}{\varepsilon}
$$



**Horizontal Derivative**:


$$
\partial_t F_t(S) = \lim_{h \to 0} \frac{F(S^{t+h}) - F(S^t)}{h}
$$



where $S^t$ is the path stopped at time $t$.

### 3. Functional Itô Formula


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


### 1. Causality Constraint


**Definition**: A functional $F: \mathcal{C}([0,T], \mathbb{R}) \to \mathbb{R}$ is **causal** (or **non-anticipating**) if:


$$
S_t = \tilde{S}_t \text{ for all } t \leq \tau \implies F(S)_{\tau} = F(\tilde{S})_{\tau}
$$



**Financial Interpretation**: The value at time $\tau$ depends only on the path up to $\tau$, not on future values.

### 2. Vertical Derivative (Causal)


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



### 3. Martingale Property (Pathwise)


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


### 1. Asian Options


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

### 2. Lookback Options


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



### 3. Barrier Options


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


### 1. Volatility Exposure


**Vega**: Sensitivity of option price to volatility:


$$
\mathcal{V} = \frac{\partial V}{\partial \sigma}
$$



**Pathwise Challenge**: Volatility is not a traded asset, so traditional delta-hedging logic doesn't apply.

### 2. Realized Variance Hedge


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

### 3. Gamma-Vega Relationship


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


### 1. Discrete-Time Pathwise Hedge


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



### 2. Quadratic Variation Estimation


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



### 3. Pathwise Simulation


**Algorithm**:

1. Generate sample path $S_t$ (any model or historical data)
2. Compute functional derivative $\partial_x F_t(S)$ at each time
3. Implement delta-hedge: $\theta_t = \partial_x F_t(S)$
4. Track cumulative P&L: $\text{P&L}_t = V_t - V_0 - \theta_0 S_0$
5. Compare terminal P&L to target payoff $F(S)$

**Model-Free Validation**: Repeat for multiple paths from different models; pathwise hedge should work consistently.

## Connections to Model-Free Finance


### 1. Game-Theoretic Probability


**Shafer-Vovk Framework**: Replace probability spaces with game-theoretic protocols.

**Betting Strategy**: A strategy is a rule for placing bets on future outcomes based on observed history.

**Pathwise Martingale**: A process is a game-theoretic martingale if no betting strategy yields guaranteed profit.

**Connection to Hedging**: Pathwise hedging strategies correspond to defensive betting strategies in the game-theoretic framework.

### 2. Obloj's Robust Framework


**Robust Pricing**: Given marginal distributions (from market option prices), compute bounds:


$$
[\underline{P}, \overline{P}] = \text{arbitrage-free price range}
$$



**Pathwise Hedging**: The bounds are attained by pathwise super- and sub-replicating strategies.

**Theorem** (Obloj et al.): Model-free bounds from martingale optimal transport correspond to pathwise hedging strategies using vanilla options.

## Advanced Topics


### 1. Non-Markovian Strategies


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

### 2. Transaction Costs


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

### 3. Rough Bergomi Model


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


### 1. Case 1: S&P 500 Options


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

### 2. Case 2: FX Barrier Option


**Setup**: Hedge EUR/USD knock-out call with barrier at 1.20.

**Challenge**: Delta jumps discontinuously at barrier.

**Pathwise Approach**:

- Monitor proximity to barrier continuously
- Adjust hedge aggressively near barrier
- Accept larger gamma cost near barrier to maintain robustness

**Outcome**: Pathwise strategy provides protection across wide range of volatility scenarios without assuming specific model.

### 3. Case 3: Asian Option on Commodity


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


### 1. When to Use Pathwise Hedging


**Advantages**:

- Model-free: Robust to misspecification
- Transparent: Clear connection to underlying path properties
- Constructive: Provides explicit trading rules

**Best Suited For**:

- Environments with model uncertainty
- Derivatives with functional payoffs (Asian, lookback)
- Situations where continuous monitoring is feasible

### 2. Implementation Checklist


1. **Compute Functional Derivative**: Determine $\partial_x F_t(S)$ for the specific payoff
2. **Choose Rebalancing Frequency**: Balance accuracy vs. transaction costs
3. **Monitor Quadratic Variation**: Track $[S]_t$ to estimate gamma costs
4. **Set Stop-Loss Limits**: Define thresholds for intervention if hedging error exceeds bounds
5. **Backtest**: Validate strategy on historical paths before deployment

### 3. Limitations


**Continuous Monitoring**: Many pathwise results assume continuous trading, which is impossible in practice.

**Discrete Approximation**: Convergence to continuous limit depends on path regularity and rebalancing frequency.

**Transaction Costs**: Frequent rebalancing can be expensive, especially for rough paths.

**Market Impact**: Large positions may move the market, violating pathwise assumptions.

## Summary and Key Insights


### 1. Fundamental Principles


1. **Path-by-Path**: Pathwise hedging works for **every path**, not just on average under a specific model.

2. **Functional Calculus**: Extends classical Itô calculus to path-dependent derivatives using functional derivatives.

3. **Robustness**: Provides model-free hedging strategies robust to specification errors.

4. **Rough Paths**: Generalizes to rough volatility using rough path integration theory.

5. **Quadratic Variation**: Hedging error controlled by accumulated quadratic variation, which is pathwise observable.

### 2. Theoretical Contributions


- **Föllmer**: Pathwise Itô formula without probability
- **Dupire**: Functional Itô calculus for path-dependent options
- **Cont-Fournié**: Rigorous functional calculus framework
- **Bayer-Friz-Gatheral**: Rough path techniques for financial mathematics
- **Vovk**: Game-theoretic probability and outer measure

### 3. Practical Impact


Pathwise hedging transforms derivative pricing from probabilistic to deterministic framework, providing:

- **Robustness**: Works under model uncertainty
- **Transparency**: Clear hedging rules
- **Validation**: Testable on historical data without assuming model

The pathwise perspective reveals that many classical results in stochastic finance have deterministic analogs, deepening our understanding of hedging and replication in quantitative finance.

---

## Exercises

**Exercise 1.** State Follmer's pathwise Ito formula for a twice continuously differentiable function $F(t, x)$ and a continuous path $x(t)$ with finite quadratic variation $[x]_t$. Apply it to $F(t, x) = x^2$ and verify that $x(T)^2 = x(0)^2 + 2\int_0^T x(t) \, dx(t) + [x]_T$ holds for any continuous path, without any probabilistic assumptions.

??? success "Solution to Exercise 1"

    **Statement of Follmer's pathwise Ito formula.**

    Let $F: \mathbb{R} \to \mathbb{R}$ be twice continuously differentiable ($F \in C^2$), and let $x: [0,T] \to \mathbb{R}$ be a continuous path possessing finite quadratic variation along a sequence of partitions $\Pi_n = \{0 = t_0^n < t_1^n < \cdots < t_{N_n}^n = T\}$ with $|\Pi_n| \to 0$. That is, the limit

    $$
    [x]_T = \lim_{n \to \infty} \sum_{i=0}^{N_n - 1} (x(t_{i+1}^n) - x(t_i^n))^2
    $$

    exists. Then:

    $$
    F(x(T)) = F(x(0)) + \int_0^T F'(x(t))\, dx(t) + \frac{1}{2}\int_0^T F''(x(t))\, d[x]_t
    $$

    where the first integral is a pathwise limit of Riemann-Stieltjes sums:

    $$
    \int_0^T F'(x(t))\, dx(t) = \lim_{n \to \infty} \sum_i F'(x(t_i^n))(x(t_{i+1}^n) - x(t_i^n))
    $$

    and the second integral is similarly defined via $d[x]_t$. No probability measure is involved.

    **Application to $F(x) = x^2$.**

    We have $F'(x) = 2x$ and $F''(x) = 2$. Applying the pathwise Ito formula:

    $$
    x(T)^2 = x(0)^2 + \int_0^T 2x(t)\, dx(t) + \frac{1}{2}\int_0^T 2\, d[x]_t
    $$

    $$
    x(T)^2 = x(0)^2 + 2\int_0^T x(t)\, dx(t) + [x]_T
    $$

    **Verification**: We can verify this directly. By the telescoping identity applied to each partition:

    $$
    x(T)^2 - x(0)^2 = \sum_i \left[x(t_{i+1})^2 - x(t_i)^2\right] = \sum_i \left[2x(t_i)(x(t_{i+1}) - x(t_i)) + (x(t_{i+1}) - x(t_i))^2\right]
    $$

    As the mesh $|\Pi_n| \to 0$:

    - $\sum_i 2x(t_i)(x(t_{i+1}) - x(t_i)) \to 2\int_0^T x(t)\, dx(t)$ (Riemann-Stieltjes sum)
    - $\sum_i (x(t_{i+1}) - x(t_i))^2 \to [x]_T$ (definition of quadratic variation)

    Therefore $x(T)^2 = x(0)^2 + 2\int_0^T x(t)\, dx(t) + [x]_T$, which holds for **any** continuous path with finite quadratic variation, without any probabilistic assumptions.

    Note that for Brownian motion $x = W$, $[W]_T = T$ almost surely, recovering the stochastic calculus identity $W_T^2 = 2\int_0^T W_t\, dW_t + T$.

---

**Exercise 2.** Consider a European call option with payoff $(S_T - K)^+$ and a pathwise hedging strategy that holds $\Delta_t = \partial C / \partial S (t, S_t)$ shares at each time $t$, where $C$ is the Black-Scholes price function with some reference volatility $\sigma$. Using the pathwise Ito formula, show that the hedging error is

$$
\text{Error} = \frac{1}{2}\int_0^T \Gamma(t, S_t) S_t^2 \left(d[S]_t - \sigma^2 S_t^2 \, dt\right)
$$

and explain why this error depends on the realized quadratic variation versus the assumed variance.

??? success "Solution to Exercise 2"

    **Setup**: Hedge a European call $(S_T - K)^+$ using Black-Scholes delta $\Delta_t = \frac{\partial C}{\partial S}(t, S_t)$ with reference volatility $\sigma$.

    The Black-Scholes price $C(t, S)$ satisfies the PDE:

    $$
    \frac{\partial C}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} + rS\frac{\partial C}{\partial S} - rC = 0
    $$

    **Apply Follmer's pathwise Ito formula** to $C(t, S_t)$ along the realized path:

    $$
    C(T, S_T) - C(0, S_0) = \int_0^T \frac{\partial C}{\partial t}\, dt + \int_0^T \frac{\partial C}{\partial S}\, dS_t + \frac{1}{2}\int_0^T \frac{\partial^2 C}{\partial S^2}\, d[S]_t
    $$

    Since $C(T, S_T) = (S_T - K)^+$ and the hedging portfolio has value:

    $$
    V_T = C(0, S_0) + \int_0^T \Delta_t\, dS_t = C(0, S_0) + \int_0^T \frac{\partial C}{\partial S}(t, S_t)\, dS_t
    $$

    The hedging error is:

    $$
    \text{Error} = V_T - (S_T - K)^+ = C(0, S_0) + \int_0^T \frac{\partial C}{\partial S}\, dS_t - C(T, S_T)
    $$

    Substituting the Ito expansion of $C(T, S_T)$:

    $$
    \text{Error} = -\int_0^T \frac{\partial C}{\partial t}\, dt - \frac{1}{2}\int_0^T \frac{\partial^2 C}{\partial S^2}\, d[S]_t
    $$

    Using the Black-Scholes PDE to substitute $\frac{\partial C}{\partial t} = -\frac{1}{2}\sigma^2 S_t^2 \Gamma_t - rS_t \Delta_t + rC$ (with $r = 0$ for simplicity):

    $$
    \text{Error} = \int_0^T \frac{1}{2}\sigma^2 S_t^2 \Gamma_t\, dt - \frac{1}{2}\int_0^T S_t^2 \Gamma_t \frac{d[S]_t}{S_t^2} \cdot S_t^2
    $$

    More carefully, writing $d[S]_t$ for the realized quadratic variation increment:

    $$
    \text{Error} = \frac{1}{2}\int_0^T \Gamma(t, S_t) \left(\sigma^2 S_t^2\, dt - d[S]_t\right)
    $$

    or equivalently:

    $$
    \text{Error} = \frac{1}{2}\int_0^T \Gamma(t, S_t) S_t^2 \left(\sigma^2\, dt - d[\log S]_t\right)
    $$

    **Interpretation**: The hedging error depends on the difference between the **assumed variance** $\sigma^2\, dt$ used in the Black-Scholes model and the **realized quadratic variation** $d[S]_t$ of the actual path. If the realized quadratic variation equals the assumed variance ($d[S]_t = \sigma^2 S_t^2\, dt$), the error is zero. The error is weighted by gamma $\Gamma_t$, so it is largest when the option has high convexity (near the money, near expiry).

    This is a purely pathwise result: it holds for **any** continuous path with finite quadratic variation, not just for Brownian motion paths. The hedger is long gamma (since $\Gamma > 0$ for a call), so the error is positive when realized variance exceeds assumed variance, and negative otherwise.

---

**Exercise 3.** In the game-theoretic probability framework of Vovk, a hedger and nature play a game. The hedger chooses a portfolio at each step, and nature chooses the next price move. Formalize the superhedging problem in this setting: define the outer measure of a set of paths $A$ as the minimal initial capital needed to ensure non-negative wealth on all paths in $A^c$. Explain why this approach requires no probability measure.

??? success "Solution to Exercise 3"

    **Game-theoretic setup (Vovk's framework).**

    The game has two players:

    1. **Hedger (Skeptic)**: At each time step $i$, observes the history $(S_0, S_1, \ldots, S_i)$ and chooses a portfolio $\theta_i$ (number of shares to hold).
    2. **Nature (Reality)**: After the hedger's choice, reveals the next price $S_{i+1}$.

    The hedger's wealth evolves as:

    $$
    W_{i+1} = W_i + \theta_i (S_{i+1} - S_i)
    $$

    starting from initial capital $W_0$.

    **Superhedging problem**: For a set of paths $A \subseteq \mathcal{C}([0,T], \mathbb{R}_+)$, the hedger wants to ensure non-negative wealth on all paths **not** in $A$ (i.e., on $A^c$).

    **Definition of outer measure**: The outer measure of $A$ is:

    $$
    \bar{P}(A) = \inf\left\{W_0 \geq 0 : \exists \text{ strategy } \theta \text{ such that } W_T(\omega) \geq 0 \text{ for all } \omega \in A^c, \text{ and } W_t(\omega) \geq 0 \text{ for all } t, \omega\right\}
    $$

    Equivalently, $\bar{P}(A)$ is the minimal initial capital needed by the hedger to guarantee non-negative terminal wealth on every path outside $A$. If the hedger starts with capital $\bar{P}(A)$ and follows the optimal strategy, then either:

    - The path $\omega \in A^c$, and the hedger ends with $W_T \geq 0$, or
    - The path $\omega \in A$, and the hedger may have negative wealth (but this is acceptable since $A$ is the "null set").

    **Why no probability measure is needed.**

    The definition of $\bar{P}(A)$ involves only:

    - Deterministic strategies $\theta$ (functions of observed price history)
    - Deterministic constraints ($W_T \geq 0$ for each specific path $\omega$)
    - An infimum over initial capitals

    At no point does the definition reference a probability measure, expectation, or stochastic integral. The "integral" $\int_0^T \theta_t\, dS_t$ is computed pathwise as a Riemann-Stieltjes limit. The outer measure $\bar{P}$ is an intrinsic property of the **path space** and the **available trading strategies**, not of any probabilistic model.

    This approach is philosophically different from measure-theoretic probability: rather than postulating a probability space and deriving consequences, it asks "what can be achieved by trading, path by path?" Events with $\bar{P}(A) = 0$ are those that can be "hedged away" at zero cost, analogous to probability-zero events but defined without probability.

    Remarkably, Vovk showed that under this framework, many classical results of stochastic calculus (quadratic variation of Brownian motion, law of large numbers, etc.) hold for "typical" paths --- those outside a set of outer measure zero.

---

**Exercise 4.** For a discrete-time pathwise hedging strategy with rebalancing at times $0 = t_0 < t_1 < \cdots < t_N = T$, show that the hedging error for a smooth payoff $g(S_T)$ is bounded by

$$
|\text{Error}| \leq \frac{1}{2} \sup_{t, S} |\Gamma(t, S)| \cdot S^2 \cdot \sum_{i=0}^{N-1} \left(\frac{S_{t_{i+1}} - S_{t_i}}{S_{t_i}}\right)^2
$$

How does this relate to the realized variance of the path?

??? success "Solution to Exercise 4"

    **Setup**: Discrete pathwise hedging at times $0 = t_0 < t_1 < \cdots < t_N = T$, payoff $g(S_T)$ with $g \in C^2$.

    The hedging strategy holds $\theta_{t_i} = g'(S_{t_i})$ shares during $[t_i, t_{i+1})$, and the portfolio value evolves:

    $$
    V_{t_{i+1}} = V_{t_i} + g'(S_{t_i})(S_{t_{i+1}} - S_{t_i})
    $$

    The terminal error is:

    $$
    \text{Error} = V_{t_N} - g(S_T) = V_0 + \sum_{i=0}^{N-1} g'(S_{t_i})(S_{t_{i+1}} - S_{t_i}) - g(S_T)
    $$

    With $V_0 = g(S_0)$ and using the telescoping sum:

    $$
    g(S_T) - g(S_0) = \sum_{i=0}^{N-1} [g(S_{t_{i+1}}) - g(S_{t_i})]
    $$

    Apply Taylor expansion to each term:

    $$
    g(S_{t_{i+1}}) - g(S_{t_i}) = g'(S_{t_i})(S_{t_{i+1}} - S_{t_i}) + \frac{1}{2}g''(\xi_i)(S_{t_{i+1}} - S_{t_i})^2
    $$

    where $\xi_i$ is between $S_{t_i}$ and $S_{t_{i+1}}$ (by the mean value theorem). Substituting:

    $$
    g(S_T) - g(S_0) = \sum_{i=0}^{N-1} g'(S_{t_i})(S_{t_{i+1}} - S_{t_i}) + \frac{1}{2}\sum_{i=0}^{N-1} g''(\xi_i)(S_{t_{i+1}} - S_{t_i})^2
    $$

    Therefore:

    $$
    \text{Error} = g(S_0) + \sum_{i=0}^{N-1} g'(S_{t_i})\Delta S_i - g(S_T) = -\frac{1}{2}\sum_{i=0}^{N-1} g''(\xi_i)(\Delta S_i)^2
    $$

    **Bounding the error**: Since $\Gamma(t, S) = g''(S)$ for a European payoff (or more generally, $g''$ plays the role of gamma):

    $$
    |\text{Error}| = \frac{1}{2}\left|\sum_{i=0}^{N-1} g''(\xi_i)(\Delta S_i)^2\right| \leq \frac{1}{2}\sup_{t,S}|g''(S)| \sum_{i=0}^{N-1} (\Delta S_i)^2
    $$

    Writing in terms of returns $r_i = \Delta S_i / S_{t_i}$:

    $$
    |\text{Error}| \leq \frac{1}{2}\sup_{t,S}|g''(S)| \cdot \sup_i S_{t_i}^2 \cdot \sum_{i=0}^{N-1} r_i^2
    $$

    or more precisely, using the original form:

    $$
    |\text{Error}| \leq \frac{1}{2}\sup_{t,S}|\Gamma(t,S)| \cdot S^2 \cdot \sum_{i=0}^{N-1}\left(\frac{S_{t_{i+1}} - S_{t_i}}{S_{t_i}}\right)^2
    $$

    **Relation to realized variance**: The sum $\sum_{i=0}^{N-1} r_i^2 = \sum_{i=0}^{N-1} \left(\frac{\Delta S_i}{S_{t_i}}\right)^2$ is precisely the **realized variance** of the path over $[0,T]$. As $N \to \infty$ (partition refines), this converges to the quadratic variation $[\log S]_T$. The hedging error is therefore controlled by the product of the maximum gamma exposure and the realized variance, confirming the fundamental link between hedging performance and realized path roughness.

---

**Exercise 5.** Dupire's functional Ito calculus extends the pathwise approach to path-dependent derivatives. For a lookback option with payoff $\max_{0 \leq t \leq T} S_t - S_T$, explain why the classical (non-path-dependent) delta hedge is insufficient and describe what additional pathwise information the functional delta $\nabla_\omega V$ captures that the standard delta $\partial V / \partial S$ does not.

??? success "Solution to Exercise 5"

    **Why classical delta is insufficient for lookback options.**

    The lookback payoff $\Phi = \max_{0 \leq t \leq T} S_t - S_T$ depends on the entire path history through the running maximum $M_T = \max_{0 \leq t \leq T} S_t$. The standard (Markovian) delta $\partial V / \partial S$ treats the option value as a function of the current spot $S_t$ only, ignoring the dependence on $M_t$.

    Consider two scenarios at time $t$ with the same spot $S_t = 100$:

    - **Scenario A**: Running maximum $M_t = 100$ (currently at the max)
    - **Scenario B**: Running maximum $M_t = 120$ (well below the max)

    The option values and sensitivities are very different:

    - In **A**, any upward move increases $M_t$, so the option is highly sensitive to $S_t$.
    - In **B**, upward moves below 120 do not change $M_t$, so the lookback feature is insensitive to $S_t$ for moderate moves.

    A hedge based only on $\partial V / \partial S$ ignores the state variable $M_t$ and would assign the same delta to both scenarios if $V$ were treated as a function of $S_t$ alone.

    **What the functional delta $\nabla_\omega V$ captures.**

    Dupire's functional Ito calculus introduces the **vertical derivative**:

    $$
    \partial_x F_t(S) = \lim_{\varepsilon \to 0} \frac{F(S + \varepsilon \mathbb{1}_{[t,T]}) - F(S)}{\varepsilon}
    $$

    This derivative perturbs the **entire future path** from time $t$ onward by $\varepsilon$. For the lookback payoff:

    - If $S_t < M_t$: A small upward bump $\varepsilon$ to the future path does not change $M_T$ (as long as $S_t + \varepsilon < M_t$), but does change $S_T$ to $S_T + \varepsilon$. So $\partial_x F_t = -1$ (the $-S_T$ part).
    - If $S_t = M_t$: A bump increases both $M_T$ and $S_T$, so the net effect depends on whether the maximum is subsequently exceeded. The functional delta reflects this through the path-dependent state.

    The functional delta captures:

    1. **Path dependence**: The delta depends on the entire history $(S_s)_{s \leq t}$, not just $S_t$.
    2. **Running maximum as state**: The hedge ratio naturally incorporates $M_t$ as an additional state variable.
    3. **Discontinuity at $S_t = M_t$**: The delta changes character when the stock is at its running maximum vs. below it.
    4. **Local time correction**: The functional Ito formula includes a term involving the local time at the running maximum, which accounts for the singular behavior of $M_t$.

    In summary, the standard delta misses the path-dependent nature of the lookback payoff, while the functional delta from Dupire's calculus naturally incorporates the running maximum as a state variable and provides the correct hedging strategy for each path configuration.

---

**Exercise 6.** Construct a pathwise superhedging strategy for a variance swap with payoff $\sum_{i=1}^N (\log S_{t_i} / S_{t_{i-1}})^2 - K_{\text{var}}$ using the Carr-Madan log-contract replication. Show that the strategy involves holding $-2/S_t$ shares of the underlying plus a static portfolio of options, and that this hedge works for every price path without any distributional assumptions.

??? success "Solution to Exercise 6"

    **Variance swap payoff**: $\sum_{i=1}^N \left(\log \frac{S_{t_i}}{S_{t_{i-1}}}\right)^2 - K_{\text{var}}$.

    **Step 1: Carr-Madan log-contract replication.**

    The key identity from Carr-Madan is that the log contract $-\log(S_T/S_0)$ can be replicated statically. Start with the payoff $g(S_T) = -2\log(S_T/S_0)$. By the Carr-Madan decomposition:

    $$
    g(S_T) = g(F) + g'(F)(S_T - F) + \int_0^F g''(K)(K - S_T)^+ dK + \int_F^\infty g''(K)(S_T - K)^+ dK
    $$

    where $F = S_0 e^{rT}$. Computing derivatives: $g'(x) = -2/x$ and $g''(x) = 2/x^2$. So:

    $$
    -2\log\frac{S_T}{S_0} = -2\log\frac{F}{S_0} - \frac{2}{F}(S_T - F) + \int_0^F \frac{2}{K^2}(K - S_T)^+ dK + \int_F^\infty \frac{2}{K^2}(S_T - K)^+ dK
    $$

    This is a **static portfolio** of puts (weight $2/K^2$ for $K < F$) and calls (weight $2/K^2$ for $K > F$).

    **Step 2: Connect to realized variance.**

    By pathwise Ito's formula applied to $f(x) = -2\log x$:

    $$
    -2\log S_T + 2\log S_0 = -2\int_0^T \frac{1}{S_t}\, dS_t + \frac{1}{2}\int_0^T \frac{2}{S_t^2}\, d[S]_t
    $$

    $$
    = -2\int_0^T \frac{dS_t}{S_t} + \int_0^T \frac{d[S]_t}{S_t^2}
    $$

    The term $\int_0^T d[S]_t / S_t^2$ is the continuous realized variance $\int_0^T d[\log S]_t$. Therefore:

    $$
    \text{RV} = \int_0^T \frac{d[S]_t}{S_t^2} = -2\log\frac{S_T}{S_0} + 2\int_0^T \frac{dS_t}{S_t}
    $$

    **Step 3: Hedging strategy.**

    The realized variance is replicated by:

    1. **Static portfolio**: Hold $2/K^2$ puts for each strike $K < F$ and $2/K^2$ calls for each strike $K > F$, plus cash and forward positions. This replicates $-2\log(S_T/S_0)$.
    2. **Dynamic position**: Hold $-2/S_t$ shares of stock at each time $t$, and continuously rebalance. The integral $2\int_0^T dS_t/S_t$ is the P&L from this dynamic position.

    Combining: the variance swap payoff is:

    $$
    \text{RV} = \underbrace{\left(-2\log\frac{S_T}{S_0}\right)}_{\text{static portfolio payoff}} + \underbrace{2\int_0^T \frac{dS_t}{S_t}}_{\text{dynamic trading P\&L}}
    $$

    **Step 4: Why this works pathwise.**

    The identity above is a consequence of Follmer's pathwise Ito formula, which holds for **every** continuous path with finite quadratic variation. No distributional assumptions are needed. The dynamic component ($-2/S_t$ shares) is determined entirely by the current price, and the static component is determined at time 0 from observed option prices.

    In discrete time, the approximation $\sum_{i=1}^N (\log S_{t_i}/S_{t_{i-1}})^2 \approx \int_0^T d[\log S]_t$ holds with error that vanishes as the partition refines, and the discrete delta $-2/S_{t_i}$ approximates the continuous strategy. The strategy is model-free because the pathwise Ito formula requires no probability measure.

---

**Exercise 7.** Rough path theory extends pathwise calculus to paths of low regularity (Holder exponent $H < 1/2$). Explain qualitatively why financial applications with rough volatility (where $H \approx 0.1$) require the rough path framework rather than the classical Follmer pathwise calculus. What is the "iterated integral" or "signature" of a path, and why is it needed for pathwise integration against rough paths?

??? success "Solution to Exercise 7"

    **Why rough paths are needed for $H < 1/2$.**

    Follmer's pathwise Ito formula requires the path to have finite **quadratic variation**, i.e., the sum $\sum_i (x(t_{i+1}) - x(t_i))^2$ must converge. For a path with Holder regularity $\alpha$:

    $$
    |x(t_{i+1}) - x(t_i)| \leq C|t_{i+1} - t_i|^\alpha
    $$

    The quadratic variation sum satisfies:

    $$
    \sum_i (x(t_{i+1}) - x(t_i))^2 \leq C^2 \sum_i |t_{i+1} - t_i|^{2\alpha} \leq C^2 N^{1-2\alpha} |\Pi|^{2\alpha}
    $$

    For a uniform partition with $N$ points, $|\Pi| = T/N$:

    - If $\alpha > 1/2$: $\sum \to 0$ as $N \to \infty$ (trivial quadratic variation)
    - If $\alpha = 1/2$: $\sum$ converges to a finite, nonzero limit (Brownian motion case)
    - If $\alpha < 1/2$: $\sum \to \infty$ (infinite quadratic variation)

    For rough volatility with $H \approx 0.1$, the volatility path has Holder exponent $\alpha \approx 0.1 < 1/2$. The quadratic variation of such a path is **infinite**, so Follmer's formula does not apply directly.

    Moreover, the classical Riemann-Stieltjes integral $\int Y\, dX$ requires the integrand $Y$ and integrator $X$ to have combined regularity exceeding 1 (i.e., $\alpha_Y + \alpha_X > 1$, the Young condition). For $\alpha_X = H = 0.1$, we would need $\alpha_Y > 0.9$, which is unrealistically smooth for financial applications.

    **The iterated integral and signature.**

    Rough path theory overcomes this by encoding higher-order information about the path. The **iterated integral** (or second-order process) for a path $X: [0,T] \to \mathbb{R}^d$ is:

    $$
    \mathbb{X}_{s,t}^{ij} = \int_s^t \int_s^u dX_r^i\, dX_u^j
    $$

    This is an element of $\mathbb{R}^{d \times d}$ capturing how different coordinates of the path interact. For a one-dimensional path, it reduces to the area:

    $$
    \mathbb{X}_{s,t} = \int_s^t (X_u - X_s)\, dX_u
    $$

    The **signature** of a path is the collection of all iterated integrals up to any order:

    $$
    \text{Sig}(X)_{s,t} = \left(1, \int_s^t dX_u, \int_s^t \int_s^u dX_r \otimes dX_u, \ldots\right)
    $$

    **Why the signature is needed.**

    For $\alpha \in (1/3, 1/2]$, the classical Riemann-Stieltjes approach fails, but knowledge of the **first-order increments** $X_t - X_s$ and the **second-order iterated integrals** $\mathbb{X}_{s,t}$ suffices to define the integral $\int Y\, dX$ via the rough path integral:

    $$
    \int_s^t Y_u\, dX_u \approx Y_s(X_t - X_s) + Y'_s \mathbb{X}_{s,t}
    $$

    where $Y'$ is the Gubinelli derivative. The key insight is that $\mathbb{X}_{s,t}$ provides the "missing information" that the first-order increments alone cannot supply for rough paths. Without $\mathbb{X}$, different approximation schemes (left-point, midpoint, etc.) give different limits for $\int Y\, dX$, so the integral is not well-defined. The iterated integral pins down which limit is the "correct" one.

    For financial applications with rough volatility ($H \approx 0.1 < 1/3$), even higher-order iterated integrals (third order and beyond) are needed, making the rough path framework essential. The signature provides a complete, model-free description of the path's behavior at all scales, enabling pathwise integration and hedging without probabilistic assumptions.
