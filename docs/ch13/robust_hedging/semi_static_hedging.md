# Semi-Static Hedging

## Introduction

Semi-static hedging represents a middle ground between fully dynamic hedging (continuous rebalancing) and purely static hedging (buy-and-hold). This approach constructs hedging portfolios that require:
1. **Initial setup**: A static portfolio of vanilla options and underlying asset
2. **Discrete adjustments**: Rebalancing only at specific times or when certain conditions are met
3. **Minimal transactions**: Significantly fewer trades than continuous delta-hedging

Semi-static hedging is particularly valuable because it:
- **Reduces transaction costs**: Fewer trades mean lower frictional expenses
- **Simplifies implementation**: Discrete rebalancing is operationally easier
- **Provides robustness**: Less sensitive to model misspecification than continuous strategies
- **Handles path-dependence**: Can replicate exotic options using vanilla instruments

The mathematical foundations draw from optimal control, PDE theory, and functional analysis, combining static replication techniques with strategic dynamic adjustments.

## Mathematical Framework

### Portfolio Structure

**Components**: A semi-static hedging portfolio consists of:

1. **Static Portfolio**: Positions in vanilla instruments held until maturity:
   - Calls: $\{C_i(K_i, T_i)\}_{i=1}^{N_C}$
   - Puts: $\{P_j(K_j, T_j)\}_{j=1}^{N_P}$
   - Zero-coupon bonds: $B(T)$

2. **Dynamic Component**: Position $\theta_t$ in the underlying asset, adjusted at discrete times $\{t_1, t_2, \ldots, t_M\}$ or contingently.

**Portfolio Value**:


$$
V_t = \theta_t S_t + \sum_{i=1}^{N_C} n_i^C C_i(S_t, K_i, T_i-t) + \sum_{j=1}^{N_P} n_j^P P_j(S_t, K_j, T_j-t) + B_t
$$



where $n_i^C, n_j^P$ are (typically) fixed quantities of options.

### Target Payoff

**Exotic Derivative**: Consider payoff $\Phi(S_T)$ or more generally $\Phi((S_t)_{0 \leq t \leq T})$.

**Replication Goal**: Construct portfolio such that:


$$
V_T \approx \Phi \quad \text{or} \quad V_T \geq \Phi \text{ (super-replication)}
$$



with minimal adjustments to $\theta_t$.

### Trading Times

**Scheduled Times**: Predetermined rebalancing dates $\{t_1, \ldots, t_M\}$.

**Event-Driven**: Rebalance when specific events occur:
- Asset price crosses threshold: $S_t \in \mathcal{S}$
- Implied volatility changes significantly: $|\sigma_t - \sigma_{t-1}| > \delta$
- Time to maturity reaches checkpoint: $T - t \in \mathcal{T}$

**Optimality**: Choose trading times to balance hedging accuracy vs. transaction costs.

## Static Replication Techniques

### Carr-Madan Decomposition

**Theorem** (Carr-Madan): Any twice-differentiable payoff $g(S_T)$ can be decomposed as:


$$
g(S_T) = g(F) + g'(F)(S_T - F) + \int_0^F g''(K) (K - S_T)^+ dK + \int_F^{\infty} g''(K) (S_T - K)^+ dK
$$



where $F = S_0 e^{rT}$ is the forward price.

**Static Portfolio**: 
- Linear position: $g'(F)$ units of forward
- Puts: Density $g''(K)$ for $K < F$
- Calls: Density $g''(K)$ for $K > F$
- Cash: $g(F) - g'(F) F$

**Purely Static**: No rebalancing needed; hold until maturity.

**Limitations**: 
- Only works for European-style payoffs
- Requires complete options market (continuum of strikes)
- Sensitive to bid-ask spreads for far-out-of-money options

### Breeden-Litzenberger Construction

**Risk-Neutral Density**: From call prices:


$$
q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}(K, T)
$$



**Static Replication**: To replicate any European payoff $g(S_T)$:


$$
V_0 = e^{-rT} \int_0^{\infty} g(K) q(K) dK = \int_0^{\infty} g(K) \frac{\partial^2 C}{\partial K^2}(K, T) dK
$$



**Implementation**: Discretize with available strikes:


$$
V_0 \approx \sum_{i=1}^n g(K_i) \frac{C(K_{i-1}) - 2C(K_i) + C(K_{i+1})}{(K_{i+1} - K_i)(K_i - K_{i-1})}
$$



## Barrier Options

### Static Replication (Black-Scholes World)

**Up-and-Out Call**: Payoff $(S_T - K)^+ \mathbb{1}_{\{M_T < H\}}$ where $M_T = \max_{0 \leq t \leq T} S_t$.

**Put-Call Symmetry**: Under Black-Scholes with constant volatility, there exists a static replication using:


$$
C^{\text{UO}}(S_0, K, H) = C(S_0, K) - \left(\frac{H}{S_0}\right)^{2\mu} C\left(\frac{H^2}{S_0}, K\right)
$$



where $\mu = \frac{r - \frac{1}{2}\sigma^2}{\sigma^2}$.

**Static Portfolio**:
- Long 1 standard call with strike $K$
- Short $\left(\frac{H}{S_0}\right)^{2\mu}$ calls with strike $K$ on "reflected" stock $\frac{H^2}{S}$

**Model Dependence**: This replication is exact only under specific model assumptions (constant volatility, no jumps).

### Semi-Static Adjustment for Model Uncertainty

**Challenge**: Static replication fails when:
- Volatility is stochastic
- Jumps are present
- Volatility surface changes shape

**Semi-Static Solution**: 
1. **Initial Setup**: Use approximate static replication
2. **Monitoring**: Track asset price relative to barrier
3. **Adjustment Rule**: If $S_t$ approaches barrier (e.g., $|S_t - H| < \epsilon$), rebalance the option portfolio

**Adjustment Strategy**: Near barrier, switch from static portfolio to:
- Pure delta-hedge if far from barrier
- Increased option coverage if near barrier

**Frequency**: Typically 1-5 adjustments over the life of the option, triggered by proximity to barrier.

### Carr-Lee Semi-Static Formula

**General Framework** (Carr-Lee 2010): For barrier options under local volatility:


$$
C^{\text{UO}}(S_0, K, H) = C(S_0, K) - \int_0^T \mathbb{E}\left[ \mathbb{1}_{\{S_t = H\}} \cdot \text{Correction}(t, S_t) \right] dt
$$



**Semi-Static Implementation**:
1. Hold static portfolio: Long call at $K$, short options as per formula
2. Monitor time spent near barrier: $L_T(H) = \lim_{\epsilon \to 0} \frac{1}{2\epsilon} \int_0^T \mathbb{1}_{\{|S_t - H| < \epsilon\}} dt$ (local time)
3. Adjust when local time accumulates significantly

## Lookback Options

### Fixed Strike Lookback Call

**Payoff**: $\Phi = M_T - K$ where $M_T = \max_{0 \leq t \leq T} S_t$.

**Decomposition**: Write as sum of:
- Standard call: $(S_T - K)^+$
- Plus: $(M_T - S_T)^+$ (gain from maximum exceeding terminal value)

### Goldman-Sosin-Gatto Static Replication

**Theorem** (GSG 1979): Under geometric Brownian motion, the lookback can be replicated using:


$$
\text{Lookback}(S_0, K) = \int_{K}^{\infty} \frac{C(S_0, L)}{L} \frac{\partial C}{\partial L}(S_0, L) dL + \text{additional terms}
$$



involving a continuum of vanilla calls.

**Semi-Static Approximation**: 
1. Discretize the integral over strikes
2. Hold portfolio of calls with strikes $\{K, K + \Delta, K + 2\Delta, \ldots\}$
3. Rebalance only if maximum increases significantly (e.g., by $\Delta$ or more)

**Adjustment Rule**: When $M_t$ increases from $M_{t^-}$ to $M_t > M_{t^-} + \Delta$:
- Add calls with strikes in $[M_{t^-}, M_t]$
- Adjust position sizes to match continuous limit

### Floating Strike Lookback

**Payoff**: $S_T - m_T$ where $m_T = \min_{0 \leq t \leq T} S_t$.

**Semi-Static Strategy**:
- Monitor running minimum $m_t$
- Hold portfolio that pays $S_T - m_t$ at maturity
- Adjust when $m_t$ decreases: shift put strikes downward

**Transaction Frequency**: Typically $O(\sqrt{T/\Delta t})$ adjustments for time steps $\Delta t$.

## Asian Options

### Arithmetic Average

**Payoff**: 


$$
\Phi = \left(\frac{1}{n} \sum_{i=1}^n S_{t_i} - K\right)^+
$$



for discrete monitoring dates $\{t_1, \ldots, t_n\}$.

### Static Lower Bound

**Convexity**: By Jensen's inequality:


$$
\left(\frac{1}{n} \sum_{i=1}^n S_{t_i}\right)^+ \geq \frac{1}{n} \sum_{i=1}^n (S_{t_i} - nK)^+
$$



**Static Portfolio**: 
- Long $1/n$ calls at each averaging date with strike $nK$
- This portfolio sub-replicates the Asian option

### Semi-Static Upper Bound

**Carr-Madan Moment-Matching**: Use static portfolio that matches first few moments of the average.

**Adjustment**: At times $t_i$:
- Observe $S_{t_i}$
- Update running average: $A_i = \frac{1}{i} \sum_{j=1}^i S_{t_j}$
- Rebalance option portfolio to match updated distribution of final average

**Frequency**: Rebalance at each averaging date (typically 12-252 times per year for monthly/daily averaging).

### Rogers-Shi Static Bounds

**Theorem** (Rogers-Shi 1995): For arithmetic Asian options, tight static bounds can be constructed using:


$$
\underline{V} \leq V^{\text{Asian}} \leq \overline{V}
$$



where bounds involve portfolios of standard calls.

**Semi-Static Enhancement**: Use static bounds as initial portfolio, with adjustments when:
- Realized average deviates significantly from expected
- Volatility changes materially

## Discrete Monitoring

### Bermudan Options

**Structure**: Option exercisable at discrete times $\{t_1, \ldots, t_n\}$ with payoff $g(S_{t_i})$ if exercised at $t_i$.

**Static Component**: Portfolio of European options maturing at each exercise date.

**Dynamic Component**: Recursive hedging starting from final exercise date:


$$
V_{t_{i}} = \max\{g(S_{t_i}), \mathbb{E}[V_{t_{i+1}} | \mathcal{F}_{t_i}]\}
$$



**Semi-Static Implementation**:
1. **Static Setup**: Hold options maturing at $\{t_1, \ldots, t_n\}$ approximating continuation values
2. **Adjustment at $t_i$**: 
   - Check if $g(S_{t_i})$ exceeds continuation value
   - If optimal to exercise: liquidate remaining portfolio
   - If not: rebalance for next period

**Frequency**: Exactly $n$ potential rebalancing times (at exercise opportunities).

### Discrete Barrier

**Knock-Out**: Option knocks out if $S_{t_i} \geq H$ for any $i \in \{1, \ldots, n\}$.

**Continuous vs. Discrete**: Discrete monitoring is **easier to hedge** than continuous because:
- Barrier breaches only checked at specific times
- Static replication more feasible

**Semi-Static Strategy**:
1. **Initial Portfolio**: Static replication for continuous barrier (approximate)
2. **Adjustments**: 
   - Just before each monitoring time $t_i$: Check if $S_{t_i^-} \approx H$
   - If close to barrier: Adjust portfolio to reflect discrete nature
   - If knocked out at $t_i$: Liquidate entire position

**Model**: Use trinomial tree or finite difference methods to price discrete barrier and determine adjustment triggers.

## Volatility Derivatives

### Variance Swaps

**Payoff**: 


$$
\text{Payoff} = \text{Realized Variance} - K_{\text{var}}
$$



where:


$$
\text{RV} = \frac{252}{n} \sum_{i=1}^n \log^2\left(\frac{S_{t_i}}{S_{t_{i-1}}}\right)
$$



**Static Replication** (Carr-Madan): Using log-contract:


$$
\text{RV} \approx \frac{2}{T} \left[\int_0^{S_0} \frac{P(K)}{K^2} dK + \int_{S_0}^{\infty} \frac{C(K)}{K^2} dK\right] - \frac{1}{T}\log^2\left(\frac{S_T}{S_0}\right)
$$



**Purely Static**: Hold portfolio of puts and calls with weights $1/K^2$ across all strikes.

**Implementation**: 
- Discretize integral using available strikes
- Hold portfolio until maturity
- No rebalancing required

**Jump Correction**: If jumps occur, the replication error is:


$$
\text{Error} = \sum_{\text{jumps}} \left[\log\left(\frac{S_t}{S_{t-}}\right)\right]^2
$$



which is typically small.

### VIX Options

**VIX Definition**: Model-free implied volatility from S&P 500 options.

**Challenge**: VIX is not directly tradable; must hedge using S&P 500 options or VIX futures.

**Semi-Static Strategy**:
1. **Static Component**: Portfolio of S&P 500 options replicating VIX (approximately)
2. **Dynamic Adjustments**: 
   - When VIX changes significantly (e.g., $\Delta \text{VIX} > 2\%$), rebalance S&P options
   - Adjust weights to maintain constant vega exposure

**Frequency**: Typically weekly or when VIX moves by threshold amount.

### Volatility Swaps

**Payoff**: 


$$
\text{Payoff} = \text{Realized Vol} - K_{\text{vol}}
$$



where $\text{Realized Vol} = \sqrt{\text{RV}}$.

**Challenge**: Square root makes static replication impossible with standard options.

**Semi-Static Approximation**:
1. **Static Component**: Variance swap (which can be replicated)
2. **Adjustment**: Use convexity correction:

   $$
   \text{Vol} \approx \sqrt{\text{Var}} - \frac{1}{8} \frac{\text{Var}^{3/2}}{\sqrt{\mathbb{E}[\text{Var}]}} + \ldots
   $$


3. **Rebalancing**: Adjust based on realized variance to date

## Transaction Cost Optimization

### Cost Model

**Proportional Costs**: Each trade incurs cost $\lambda |$quantity$| \times$ price.

**Objective**: Minimize total cost:


$$
\min_{\theta, \{t_i\}} \left\{ \mathbb{E}[(V_T - \Phi)^2] + \lambda \sum_{i=1}^M |\theta_{t_i} - \theta_{t_{i-1}}| S_{t_i} \right\}
$$



**Trade-off**: Hedging accuracy vs. transaction costs.

### Optimal Rebalancing Times

**Problem**: Choose trading times $\{t_1, \ldots, t_M\}$ optimally.

**Dynamic Programming**: Value function:


$$
J(t, S, V) = \inf_{\tau > t} \mathbb{E}\left[\text{Cost}(\tau, S_{\tau}, V_{\tau}) + J(\tau, S_{\tau}, V_{\tau})\right]
$$



where $\tau$ is the next trading time.

**Threshold Policy**: Rebalance when:


$$
|\theta_{\text{optimal}}(S_t) - \theta_t| > \Delta^*
$$



for optimal threshold $\Delta^*$ balancing cost and risk.

**Volatility Dependence**: Threshold typically increases with volatility:


$$
\Delta^*(t) = c \cdot \sigma(t) \cdot \sqrt{T - t}
$$



### Option Rebalancing

**Question**: When to adjust the static option portfolio?

**Criteria**:
1. **Time-based**: At regular intervals (monthly, quarterly)
2. **Price-based**: When $S_t$ moves beyond certain levels
3. **Greeks-based**: When delta, gamma, or vega deviate from targets
4. **Volatility-based**: When implied volatility shifts significantly

**Optimal Policy**: Typically combines multiple criteria:


$$
\text{Rebalance if } \max\{|\Delta_t - \Delta^*|, |\Gamma_t - \Gamma^*|, |\mathcal{V}_t - \mathcal{V}^*|\} > \epsilon
$$



## Robust Semi-Static Strategies

### Model Uncertainty

**Setup**: Uncertain about true dynamics; consider set of models $\mathcal{M}$.

**Robust Objective**: Maximize worst-case performance:


$$
\max_{\{\theta_t, n_i, n_j\}} \min_{P \in \mathcal{M}} \mathbb{E}_P[V_T - \Phi]
$$



subject to transaction cost constraints.

### Volatility Bounds

**Assumption**: Volatility lies in range $[\underline{\sigma}, \overline{\sigma}]$.

**Robust Semi-Static Hedge**:
1. **Static Component**: Use midpoint volatility $\bar{\sigma} = (\underline{\sigma} + \overline{\sigma})/2$ for initial replication
2. **Dynamic Adjustments**: 
   - Monitor realized variance
   - If RV suggests $\sigma \approx \underline{\sigma}$, add protective options
   - If RV suggests $\sigma \approx \overline{\sigma}$, reduce expensive hedges

**Adaptation**: Strategy adapts to observed path characteristics without assuming specific model.

### Uncertain Jump Risk

**Setup**: Underlying may jump, but jump intensity and size are uncertain.

**Strategy**:
1. **Base Case**: Static replication assuming no jumps
2. **Jump Protection**: 
   - Long out-of-the-money puts (downside jump protection)
   - Long out-of-the-money calls (upside jump protection)
3. **Adjustment**: If jump occurs, rebalance entire portfolio using post-jump price

**Cost-Benefit**: Jump protection is expensive; trade-off depends on risk tolerance.

## Practical Implementation

### Step 1: Initial Portfolio Design

**Identify Static Component**: Determine which options to include:
- Strikes: Choose based on payoff structure and liquidity
- Maturities: Match or slightly exceed target maturity
- Quantities: Solve for weights using Carr-Madan or similar

**Example** (Digital Option):
- Static portfolio: Tight call spread around strike $K$
- Spread width $\Delta K$ chosen based on liquidity and cost

### Step 2: Define Adjustment Triggers

**Specify Rules**: Clear conditions for rebalancing:
- **Time triggers**: "Rebalance every month"
- **Price triggers**: "Rebalance if $S_t$ crosses $K \pm 10\%$"
- **Greeks triggers**: "Rebalance if $|\Delta - \Delta^*| > 0.2$"

**Backtest**: Validate trigger rules on historical data to ensure they balance cost and accuracy.

### Step 3: Implement Monitoring System

**Real-Time Tracking**:
- Portfolio value $V_t$
- Target value (mark-to-market of exotic)
- Tracking error: $|V_t - \text{Target}_t|$
- Greeks: $\Delta, \Gamma, \mathcal{V}$

**Alerts**: Automated notifications when triggers are met.

### Step 4: Execute Adjustments

**Pre-Adjustment Check**:
- Verify trigger condition
- Calculate optimal adjustment (solve for new $\theta_t$, $n_i^C$, $n_j^P$)
- Estimate transaction costs

**Execution**:
- Place orders for required adjustments
- Monitor fill prices
- Update portfolio records

**Post-Adjustment Review**:
- Verify new portfolio matches target
- Document rationale and costs
- Update tracking error statistics

### Step 5: Performance Analysis

**Metrics**:
- **Hedging Error**: $|V_T - \Phi|$ at maturity
- **Transaction Costs**: $\sum_{i=1}^M \text{Cost}_i$
- **Number of Adjustments**: $M$
- **Sharpe Ratio**: Risk-adjusted performance

**Continuous Improvement**: Refine trigger rules based on observed performance.

## Case Studies

### Case 1: Down-and-Out Put on Equity Index

**Setup**:
- Underlying: S&P 500
- Strike: $K = 4000$
- Barrier: $H = 3800$
- Maturity: 3 months

**Semi-Static Strategy**:
1. **Initial**: Static portfolio using put-call symmetry relation
2. **Monitoring**: Daily check if $S_t \in [3800, 3850]$ (near barrier)
3. **Adjustments**: If near barrier, shift from static portfolio to dynamic delta-hedge
4. **Exit**: If barrier hit, liquidate all positions

**Result**: 3 adjustments over 3 months; total hedging error < 0.5% of notional.

### Case 2: Asian Call on FX Rate

**Setup**:
- Underlying: EUR/USD
- Averaging: Daily over 6 months
- Strike: $K = 1.10$

**Semi-Static Strategy**:
1. **Static Bounds**: Rogers-Shi bounds using vanilla options
2. **Adjustments**: Monthly, update portfolio based on accumulated average
3. **Greeks Management**: Rebalance if delta drifts by > 0.3

**Result**: 6 adjustments; hedging error < 1% with transaction costs 0.3% of notional.

### Case 3: Variance Swap on Commodity

**Setup**:
- Underlying: Crude oil (WTI)
- Tenor: 12 months
- Strike: $K_{\text{var}} = 400$ (vol$^2$ in percentage points)

**Semi-Static Strategy**:
1. **Static Replication**: Portfolio of calls and puts with weights $1/K^2$
2. **Adjustments**: None (purely static)
3. **Monitoring**: Track realized variance daily

**Result**: 
- Final realized variance: 425
- Replication error: < 2% (due to discrete strikes and jumps)
- No transaction costs beyond initial setup

## Advanced Topics

### Multi-Asset Semi-Static Hedging

**Basket Options**: Payoff depends on multiple underlyings:


$$
\Phi = \left(\sum_{i=1}^n w_i S_T^{(i)} - K\right)^+
$$



**Challenge**: Correlation uncertainty.

**Semi-Static Strategy**:
1. **Static Component**: Vanilla options on each underlying
2. **Correlation Adjustment**: Rebalance when observed correlation deviates from initial estimate
3. **Frequency**: Quarterly or when cross-asset moves are large

**Greeks**: Manage delta, gamma, and cross-gammas ($\Gamma_{ij} = \frac{\partial^2 V}{\partial S_i \partial S_j}$).

### American Options

**Optimal Exercise**: Holder can exercise at any time before maturity.

**Semi-Static Hedge**:
1. **Static Component**: Portfolio of Europeans approximating exercise boundary
2. **Adjustments**: At each potential exercise time, check if early exercise is optimal
3. **Dynamic Overlay**: Small delta-hedge to correct for approximation errors

**Challenge**: Exercise boundary is model-dependent; semi-static hedge must be robust to boundary misspecification.

### Stochastic Volatility

**Model**: Volatility follows its own stochastic process:


$$
dS_t = \mu S_t dt + \sqrt{V_t} S_t dW_t^S, \quad dV_t = \kappa(\theta - V_t) dt + \xi \sqrt{V_t} dW_t^V
$$



**Semi-Static Approach**:
1. **Vega Hedging**: Hold options at multiple strikes to hedge volatility risk
2. **Adjustment**: When implied volatility changes significantly, rebalance option portfolio
3. **Frequency**: Based on vol-of-vol (typically more frequent than delta adjustments)

**Greeks to Monitor**: Delta, gamma, vega, and volga ($\frac{\partial^2 V}{\partial \sigma^2}$).

### Path-Dependent Interest Rates

**Floaters and Path-Dependent Coupons**: Options on bonds where payoff depends on interest rate path.

**Semi-Static Strategy**:
1. **Static Component**: Portfolio of caplets and floorlets
2. **Adjustments**: At coupon reset dates, rebalance based on realized rates
3. **Curve Risk**: Manage exposure to different points on yield curve

## Comparison with Other Hedging Approaches

| **Approach** | **Adjustments** | **Transaction Costs** | **Model Dependence** | **Hedging Error** |
|--------------|-----------------|----------------------|---------------------|-------------------|
| **Continuous Delta** | Infinite | High | High | Low (in theory) |
| **Discrete Delta** | Frequent | Medium | High | Medium |
| **Semi-Static** | Few | Low | Medium | Medium |
| **Purely Static** | None | Very Low | Low | Can be high |

**Semi-Static Niche**: Optimal for situations where:
- Transaction costs are moderate to high
- Path-dependence is manageable
- Some model uncertainty exists
- Operational complexity must be limited

## Current Research Directions

### Machine Learning for Trigger Optimization

**Objective**: Use ML to learn optimal adjustment triggers from data.

**Approach**:
1. Simulate many paths under various models
2. For each path, compute optimal adjustment times (via DP)
3. Train classifier/regressor to predict adjustments from observed state variables

**Features**: $S_t$, $V_t$, Greeks, time to maturity, realized variance, etc.

**Output**: Probability of rebalancing or optimal adjustment size.

### Robust Optimization

**Formulation**: 


$$
\min_{\theta, \{t_i\}} \max_{P \in \mathcal{P}} \mathbb{E}_P\left[(V_T - \Phi)^2 + \lambda \sum_{i=1}^M |\Delta \theta_i|\right]
$$



where $\mathcal{P}$ is a set of probability measures.

**Solution Methods**:
- Duality theory
- Scenario optimization
- Distributionally robust optimization

### Neural Networks for Semi-Static Strategies

**Deep Hedging**: Train neural networks to output:
- Option quantities $\{n_i^C, n_j^P\}$
- Adjustment times $\{t_i\}$
- Stock positions $\theta_t$

**Training**: Minimize expected hedging error plus transaction costs over simulated paths.

**Advantage**: Can discover complex, non-linear adjustment rules that outperform hand-crafted strategies.

## Summary and Key Insights

### Fundamental Principles

1. **Balance**: Semi-static hedging balances accuracy, cost, and simplicity.

2. **Static Core**: Use robust static replication as foundation; adjust only when necessary.

3. **Discrete Adjustments**: Rebalance at strategic times or events, not continuously.

4. **Model-Light**: Less dependent on specific model assumptions than fully dynamic hedging.

5. **Transaction Efficiency**: Significantly reduces trading costs compared to continuous hedging.

### Practical Guidelines

**When to Use Semi-Static**:
- Transaction costs are non-negligible
- Continuous monitoring is operationally challenging
- Model uncertainty is significant
- Derivative has some path-dependence but not extreme

**Design Principles**:
- **Robust static base**: Choose static portfolio that works across multiple scenarios
- **Clear triggers**: Define objective, testable adjustment conditions
- **Cost-aware**: Explicitly account for transaction costs in optimization
- **Adaptive**: Monitor performance and refine strategy over time

### Theoretical Contributions

- **Carr-Madan**: Static replication formulas for European payoffs
- **Rogers-Shi**: Static bounds for Asian options
- **Carr-Lee**: Semi-static hedging for barrier options under local volatility
- **Derman-Ergener-Kani**: Static hedging of exotic options in general

### Future Directions

Semi-static hedging continues to evolve with:
- **Machine learning**: Automated discovery of optimal adjustment rules
- **Robustness theory**: Strategies that work across model classes
- **High-frequency data**: Using intraday information to improve timing
- **Multiple sources of risk**: Extending to multi-asset, multi-factor settings

The semi-static framework provides a practical, cost-effective approach to derivative hedging that bridges theory and practice, combining the elegance of static replication with the flexibility of dynamic adjustments.
