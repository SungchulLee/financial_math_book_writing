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


### 1. Portfolio Structure


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

### 2. Target Payoff


**Exotic Derivative**: Consider payoff $\Phi(S_T)$ or more generally $\Phi((S_t)_{0 \leq t \leq T})$.

**Replication Goal**: Construct portfolio such that:


$$
V_T \approx \Phi \quad \text{or} \quad V_T \geq \Phi \text{ (super-replication)}
$$



with minimal adjustments to $\theta_t$.

### 3. Trading Times


**Scheduled Times**: Predetermined rebalancing dates $\{t_1, \ldots, t_M\}$.

**Event-Driven**: Rebalance when specific events occur:
- Asset price crosses threshold: $S_t \in \mathcal{S}$
- Implied volatility changes significantly: $|\sigma_t - \sigma_{t-1}| > \delta$
- Time to maturity reaches checkpoint: $T - t \in \mathcal{T}$

**Optimality**: Choose trading times to balance hedging accuracy vs. transaction costs.

## Static Replication Techniques


### 1. Carr-Madan Decomposition


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

### 2. Breeden-Litzenberger Construction


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


### 1. Static Replication (Black-Scholes World)


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

### 2. Semi-Static Adjustment for Model Uncertainty


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

### 3. Carr-Lee Semi-Static Formula


**General Framework** (Carr-Lee 2010): For barrier options under local volatility:


$$
C^{\text{UO}}(S_0, K, H) = C(S_0, K) - \int_0^T \mathbb{E}\left[ \mathbb{1}_{\{S_t = H\}} \cdot \text{Correction}(t, S_t) \right] dt
$$



**Semi-Static Implementation**:
1. Hold static portfolio: Long call at $K$, short options as per formula
2. Monitor time spent near barrier: $L_T(H) = \lim_{\epsilon \to 0} \frac{1}{2\epsilon} \int_0^T \mathbb{1}_{\{|S_t - H| < \epsilon\}} dt$ (local time)
3. Adjust when local time accumulates significantly

## Lookback Options


### 1. Fixed Strike Lookback Call


**Payoff**: $\Phi = M_T - K$ where $M_T = \max_{0 \leq t \leq T} S_t$.

**Decomposition**: Write as sum of:
- Standard call: $(S_T - K)^+$
- Plus: $(M_T - S_T)^+$ (gain from maximum exceeding terminal value)

### 2. Goldman-Sosin-Gatto Static Replication


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

### 3. Floating Strike Lookback


**Payoff**: $S_T - m_T$ where $m_T = \min_{0 \leq t \leq T} S_t$.

**Semi-Static Strategy**:
- Monitor running minimum $m_t$
- Hold portfolio that pays $S_T - m_t$ at maturity
- Adjust when $m_t$ decreases: shift put strikes downward

**Transaction Frequency**: Typically $O(\sqrt{T/\Delta t})$ adjustments for time steps $\Delta t$.

## Asian Options


### 1. Arithmetic Average


**Payoff**: 


$$
\Phi = \left(\frac{1}{n} \sum_{i=1}^n S_{t_i} - K\right)^+
$$



for discrete monitoring dates $\{t_1, \ldots, t_n\}$.

### 2. Static Lower Bound


**Convexity**: By Jensen's inequality:


$$
\left(\frac{1}{n} \sum_{i=1}^n S_{t_i}\right)^+ \geq \frac{1}{n} \sum_{i=1}^n (S_{t_i} - nK)^+
$$



**Static Portfolio**: 
- Long $1/n$ calls at each averaging date with strike $nK$
- This portfolio sub-replicates the Asian option

### 3. Semi-Static Upper Bound


**Carr-Madan Moment-Matching**: Use static portfolio that matches first few moments of the average.

**Adjustment**: At times $t_i$:
- Observe $S_{t_i}$
- Update running average: $A_i = \frac{1}{i} \sum_{j=1}^i S_{t_j}$
- Rebalance option portfolio to match updated distribution of final average

**Frequency**: Rebalance at each averaging date (typically 12-252 times per year for monthly/daily averaging).

### 4. Rogers-Shi Static Bounds


**Theorem** (Rogers-Shi 1995): For arithmetic Asian options, tight static bounds can be constructed using:


$$
\underline{V} \leq V^{\text{Asian}} \leq \overline{V}
$$



where bounds involve portfolios of standard calls.

**Semi-Static Enhancement**: Use static bounds as initial portfolio, with adjustments when:
- Realized average deviates significantly from expected
- Volatility changes materially

## Discrete Monitoring


### 1. Bermudan Options


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

### 2. Discrete Barrier


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


### 1. Variance Swaps


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

### 2. VIX Options


**VIX Definition**: Model-free implied volatility from S&P 500 options.

**Challenge**: VIX is not directly tradable; must hedge using S&P 500 options or VIX futures.

**Semi-Static Strategy**:
1. **Static Component**: Portfolio of S&P 500 options replicating VIX (approximately)
2. **Dynamic Adjustments**: 
   - When VIX changes significantly (e.g., $\Delta \text{VIX} > 2\%$), rebalance S&P options
   - Adjust weights to maintain constant vega exposure

**Frequency**: Typically weekly or when VIX moves by threshold amount.

### 3. Volatility Swaps


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


### 1. Cost Model


**Proportional Costs**: Each trade incurs cost $\lambda |$quantity$| \times$ price.

**Objective**: Minimize total cost:


$$
\min_{\theta, \{t_i\}} \left\{ \mathbb{E}[(V_T - \Phi)^2] + \lambda \sum_{i=1}^M |\theta_{t_i} - \theta_{t_{i-1}}| S_{t_i} \right\}
$$



**Trade-off**: Hedging accuracy vs. transaction costs.

### 2. Optimal Rebalancing Times


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



### 3. Option Rebalancing


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


### 1. Model Uncertainty


**Setup**: Uncertain about true dynamics; consider set of models $\mathcal{M}$.

**Robust Objective**: Maximize worst-case performance:


$$
\max_{\{\theta_t, n_i, n_j\}} \min_{P \in \mathcal{M}} \mathbb{E}_P[V_T - \Phi]
$$



subject to transaction cost constraints.

### 2. Volatility Bounds


**Assumption**: Volatility lies in range $[\underline{\sigma}, \overline{\sigma}]$.

**Robust Semi-Static Hedge**:
1. **Static Component**: Use midpoint volatility $\bar{\sigma} = (\underline{\sigma} + \overline{\sigma})/2$ for initial replication
2. **Dynamic Adjustments**: 
   - Monitor realized variance
   - If RV suggests $\sigma \approx \underline{\sigma}$, add protective options
   - If RV suggests $\sigma \approx \overline{\sigma}$, reduce expensive hedges

**Adaptation**: Strategy adapts to observed path characteristics without assuming specific model.

### 3. Uncertain Jump Risk


**Setup**: Underlying may jump, but jump intensity and size are uncertain.

**Strategy**:
1. **Base Case**: Static replication assuming no jumps
2. **Jump Protection**: 
   - Long out-of-the-money puts (downside jump protection)
   - Long out-of-the-money calls (upside jump protection)
3. **Adjustment**: If jump occurs, rebalance entire portfolio using post-jump price

**Cost-Benefit**: Jump protection is expensive; trade-off depends on risk tolerance.

## Practical Implementation


### 1. Step 1: Initial Portfolio Design


**Identify Static Component**: Determine which options to include:
- Strikes: Choose based on payoff structure and liquidity
- Maturities: Match or slightly exceed target maturity
- Quantities: Solve for weights using Carr-Madan or similar

**Example** (Digital Option):
- Static portfolio: Tight call spread around strike $K$
- Spread width $\Delta K$ chosen based on liquidity and cost

### 2. Step 2: Define Adjustment Triggers


**Specify Rules**: Clear conditions for rebalancing:
- **Time triggers**: "Rebalance every month"
- **Price triggers**: "Rebalance if $S_t$ crosses $K \pm 10\%$"
- **Greeks triggers**: "Rebalance if $|\Delta - \Delta^*| > 0.2$"

**Backtest**: Validate trigger rules on historical data to ensure they balance cost and accuracy.

### 3. Step 3: Implement Monitoring System


**Real-Time Tracking**:
- Portfolio value $V_t$
- Target value (mark-to-market of exotic)
- Tracking error: $|V_t - \text{Target}_t|$
- Greeks: $\Delta, \Gamma, \mathcal{V}$

**Alerts**: Automated notifications when triggers are met.

### 4. Step 4: Execute Adjustments


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

### 5. Step 5: Performance Analysis


**Metrics**:
- **Hedging Error**: $|V_T - \Phi|$ at maturity
- **Transaction Costs**: $\sum_{i=1}^M \text{Cost}_i$
- **Number of Adjustments**: $M$
- **Sharpe Ratio**: Risk-adjusted performance

**Continuous Improvement**: Refine trigger rules based on observed performance.

## Case Studies


### 1. Case 1: Down-and-Out Put on Equity Index


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

### 2. Case 2: Asian Call on FX Rate


**Setup**:
- Underlying: EUR/USD
- Averaging: Daily over 6 months
- Strike: $K = 1.10$

**Semi-Static Strategy**:
1. **Static Bounds**: Rogers-Shi bounds using vanilla options
2. **Adjustments**: Monthly, update portfolio based on accumulated average
3. **Greeks Management**: Rebalance if delta drifts by > 0.3

**Result**: 6 adjustments; hedging error < 1% with transaction costs 0.3% of notional.

### 3. Case 3: Variance Swap on Commodity


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


### 1. Multi-Asset Semi-Static Hedging


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

### 2. American Options


**Optimal Exercise**: Holder can exercise at any time before maturity.

**Semi-Static Hedge**:
1. **Static Component**: Portfolio of Europeans approximating exercise boundary
2. **Adjustments**: At each potential exercise time, check if early exercise is optimal
3. **Dynamic Overlay**: Small delta-hedge to correct for approximation errors

**Challenge**: Exercise boundary is model-dependent; semi-static hedge must be robust to boundary misspecification.

### 3. Stochastic Volatility


**Model**: Volatility follows its own stochastic process:


$$
dS_t = \mu S_t dt + \sqrt{V_t} S_t dW_t^S, \quad dV_t = \kappa(\theta - V_t) dt + \xi \sqrt{V_t} dW_t^V
$$



**Semi-Static Approach**:
1. **Vega Hedging**: Hold options at multiple strikes to hedge volatility risk
2. **Adjustment**: When implied volatility changes significantly, rebalance option portfolio
3. **Frequency**: Based on vol-of-vol (typically more frequent than delta adjustments)

**Greeks to Monitor**: Delta, gamma, vega, and volga ($\frac{\partial^2 V}{\partial \sigma^2}$).

### 4. Path-Dependent Interest Rates


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


### 1. Machine Learning for Trigger Optimization


**Objective**: Use ML to learn optimal adjustment triggers from data.

**Approach**:
1. Simulate many paths under various models
2. For each path, compute optimal adjustment times (via DP)
3. Train classifier/regressor to predict adjustments from observed state variables

**Features**: $S_t$, $V_t$, Greeks, time to maturity, realized variance, etc.

**Output**: Probability of rebalancing or optimal adjustment size.

### 2. Robust Optimization


**Formulation**: 


$$
\min_{\theta, \{t_i\}} \max_{P \in \mathcal{P}} \mathbb{E}_P\left[(V_T - \Phi)^2 + \lambda \sum_{i=1}^M |\Delta \theta_i|\right]
$$



where $\mathcal{P}$ is a set of probability measures.

**Solution Methods**:
- Duality theory
- Scenario optimization
- Distributionally robust optimization

### 3. Neural Networks for Semi-Static Strategies


**Deep Hedging**: Train neural networks to output:
- Option quantities $\{n_i^C, n_j^P\}$
- Adjustment times $\{t_i\}$
- Stock positions $\theta_t$

**Training**: Minimize expected hedging error plus transaction costs over simulated paths.

**Advantage**: Can discover complex, non-linear adjustment rules that outperform hand-crafted strategies.

## Summary and Key Insights


### 1. Fundamental Principles


1. **Balance**: Semi-static hedging balances accuracy, cost, and simplicity.

2. **Static Core**: Use robust static replication as foundation; adjust only when necessary.

3. **Discrete Adjustments**: Rebalance at strategic times or events, not continuously.

4. **Model-Light**: Less dependent on specific model assumptions than fully dynamic hedging.

5. **Transaction Efficiency**: Significantly reduces trading costs compared to continuous hedging.

### 2. Practical Guidelines


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

### 3. Theoretical Contributions


- **Carr-Madan**: Static replication formulas for European payoffs
- **Rogers-Shi**: Static bounds for Asian options
- **Carr-Lee**: Semi-static hedging for barrier options under local volatility
- **Derman-Ergener-Kani**: Static hedging of exotic options in general

### 4. Future Directions


Semi-static hedging continues to evolve with:
- **Machine learning**: Automated discovery of optimal adjustment rules
- **Robustness theory**: Strategies that work across model classes
- **High-frequency data**: Using intraday information to improve timing
- **Multiple sources of risk**: Extending to multi-asset, multi-factor settings

The semi-static framework provides a practical, cost-effective approach to derivative hedging that bridges theory and practice, combining the elegance of static replication with the flexibility of dynamic adjustments.

---

## Exercises

**Exercise 1.** Using the Carr-Madan static replication formula, express the payoff of a variance swap $g(S_T) = -2\log(S_T/F)$ as a portfolio of European puts and calls. Write out the explicit weights $g''(K) = 2/K^2$ and explain why the replication uses out-of-the-money puts for $K < F$ and out-of-the-money calls for $K > F$.

??? success "Solution to Exercise 1"

    **The payoff**: A variance swap pays the realized variance minus a fixed strike. The log-contract payoff $g(S_T) = -2\log(S_T/F)$ is the key building block, where $F = S_0 e^{rT}$ is the forward price.

    **Step 1: Apply the Carr-Madan decomposition.**

    For any twice-differentiable $g$:

    $$
    g(S_T) = g(F) + g'(F)(S_T - F) + \int_0^F g''(K)(K - S_T)^+\, dK + \int_F^\infty g''(K)(S_T - K)^+\, dK
    $$

    Compute the derivatives of $g(x) = -2\log(x/F)$:

    $$
    g'(x) = -\frac{2}{x}, \qquad g''(x) = \frac{2}{x^2}
    $$

    Evaluate at $x = F$:

    $$
    g(F) = -2\log(F/F) = 0, \qquad g'(F) = -\frac{2}{F}
    $$

    Substituting:

    $$
    -2\log\frac{S_T}{F} = 0 - \frac{2}{F}(S_T - F) + \int_0^F \frac{2}{K^2}(K - S_T)^+\, dK + \int_F^\infty \frac{2}{K^2}(S_T - K)^+\, dK
    $$

    **Step 2: Identify the portfolio.**

    The decomposition gives the following **static portfolio**:

    | Component | Instrument | Quantity |
    |-----------|-----------|----------|
    | Cash | Zero-coupon bond | $g(F) = 0$ |
    | Linear | Forward contract | $g'(F) = -2/F$ units |
    | Puts ($K < F$) | Put at strike $K$ | $g''(K)\, dK = \frac{2}{K^2}\, dK$ |
    | Calls ($K > F$) | Call at strike $K$ | $g''(K)\, dK = \frac{2}{K^2}\, dK$ |

    **Step 3: Why OTM options are used.**

    For $K < F$: The put $(K - S_T)^+$ is out-of-the-money (OTM) since the forward is $F > K$. These puts are cheaper than ITM calls at the same strike and have the same payoff structure.

    For $K > F$: The call $(S_T - K)^+$ is out-of-the-money. These calls are cheaper than ITM puts at the same strike.

    Using OTM options is preferred because:

    1. **Liquidity**: OTM options are more liquid than ITM options in most markets.
    2. **Bid-ask spreads**: OTM options typically have tighter relative spreads.
    3. **Model sensitivity**: OTM option prices are more directly informative about tail risk.
    4. **No duplication**: By put-call parity, $P(K) = C(K) - (F-K)e^{-rT}$ for $K < F$, so using puts below $F$ and calls above $F$ avoids redundancy with the linear (forward) component.

    The weights $2/K^2$ decrease with strike, meaning deep OTM options receive the most weight per unit strike width, reflecting the logarithmic nature of the variance payoff.

---

**Exercise 2.** Consider an up-and-out call with strike $K = 100$ and barrier $H = 120$. Under the Black-Scholes model with constant volatility, describe the semi-static hedging strategy that uses a static portfolio of vanilla calls plus a dynamic adjustment at the barrier. Specifically, show that at the moment the barrier is first hit, the static portfolio should be liquidated and its proceeds invested in bonds.

??? success "Solution to Exercise 2"

    **Setup**: Up-and-out call with $K = 100$, barrier $H = 120$, under Black-Scholes with constant $\sigma$.

    **Step 1: Static replication using put-call symmetry.**

    Under Black-Scholes, the reflection principle gives the up-and-out call price:

    $$
    C^{\text{UO}}(S_0, K, H) = C(S_0, K) - \left(\frac{H}{S_0}\right)^{2\mu} C\left(\frac{H^2}{S_0}, K\right)
    $$

    where $\mu = (r - \frac{1}{2}\sigma^2)/\sigma^2$. This means the initial static portfolio is:

    - **Long** 1 vanilla call with strike $K = 100$
    - **Short** $(H/S_0)^{2\mu}$ vanilla calls with strike $K = 100$ evaluated at spot $H^2/S_0$

    **Step 2: Semi-static hedging strategy.**

    The semi-static approach works as follows:

    **Before barrier is hit** ($S_t < H$ for all $t$):

    - Hold the static portfolio established at time 0.
    - The portfolio value tracks the up-and-out call value as long as $S_t$ remains below $H$.

    **At the moment the barrier is first hit** ($\tau = \inf\{t : S_t \geq H\}$):

    - The up-and-out call becomes worthless: $C^{\text{UO}} = 0$.
    - The static portfolio at $S_\tau = H$ has value:

    $$
    V_\tau = C(H, K) - \left(\frac{H}{S_0}\right)^{2\mu} C\left(\frac{H^2}{S_0}, K\right)\bigg|_{S=H}
    $$

    Under the Black-Scholes reflection principle, these two terms are equal when $S = H$, so $V_\tau = 0$ exactly at the barrier.

    **Action at barrier hit**: Liquidate the entire option portfolio. Since $V_\tau = 0$ (under the model), the liquidation produces zero proceeds. Invest any small residual in the risk-free bond.

    **After barrier hit**: The exotic option is dead (knocked out), so no further hedging is needed. The bond position generates risk-free returns until maturity.

    **At maturity** ($t = T$):

    - If barrier was never hit: the static portfolio pays $(S_T - K)^+ - (H/S_0)^{2\mu}(S_T - K)^+ \cdot \text{adjustment}$, which equals the up-and-out call payoff.
    - If barrier was hit at time $\tau$: the portfolio was liquidated at zero cost, matching the zero payoff of the knocked-out option.

    **Key insight**: This is a **semi-static** strategy because it requires only one dynamic action (liquidation at the barrier), with the rest being a static hold. Under the Black-Scholes model with constant volatility, this replication is exact.

---

**Exercise 3.** Compare the total hedging cost (including transaction costs) of three strategies for a barrier option: (a) continuous delta hedging, (b) semi-static hedging with adjustment at the barrier only, and (c) purely static replication using vanilla options. If proportional transaction costs are $\varepsilon = 0.1\%$ and the option has 1 year to maturity with daily rebalancing for strategy (a), estimate which strategy is cheapest.

??? success "Solution to Exercise 3"

    **Setup**: Barrier option, $T = 1$ year, $\varepsilon = 0.1\%$ proportional transaction costs.

    **Strategy (a): Continuous delta hedging (daily rebalancing).**

    With $N = 252$ daily rebalances:

    - **Transaction costs**: Each rebalance trades $|\Delta\theta_i|$ shares. For a barrier option, delta changes rapidly near the barrier, leading to large turnover. Estimated:

    $$
    \text{TC}_a \approx \varepsilon \cdot \sigma S_0 \sqrt{N/T} = 0.001 \times 0.20 \times 100 \times \sqrt{252} = 0.02 \times 15.87 = 0.317
    $$

    However, barrier options have higher gamma near the barrier, so the actual cost is typically 2-3 times higher than for vanilla options:

    $$
    \text{TC}_a \approx 0.6 \text{ to } 0.9
    $$

    - **Hedging error**: Small for daily rebalancing, approximately $O(1/\sqrt{N}) \approx 0.06$.
    - **Total cost**: $\approx 0.7 - 1.0$.

    **Strategy (b): Semi-static hedging with adjustment at barrier only.**

    - **Transaction costs**: Initial setup (buying the static portfolio) costs $\varepsilon$ times the notional of the options purchased. For a portfolio of 2-3 vanilla options, this is approximately:

    $$
    \text{TC}_b \approx \varepsilon \times (\text{total option notional}) \approx 0.001 \times 2 \times C_{\text{BS}} \approx 0.001 \times 2 \times 8 = 0.016
    $$

    Plus one potential adjustment at the barrier:

    $$
    \text{TC}_{\text{barrier}} \approx 0.001 \times C(H, K) \approx 0.001 \times 20 = 0.02
    $$

    Total: $\text{TC}_b \approx 0.04$.

    - **Hedging error**: Under the Black-Scholes model, the semi-static hedge is exact. Under model misspecification (stochastic volatility, jumps), the error is model-dependent, typically:

    $$
    \text{HE}_b \approx 0.5 \text{ to } 1.5 \text{ (percent of option value)}
    $$

    - **Total cost**: $\approx 0.04 + 0.5 = 0.54$ (optimistic) to $0.04 + 1.5 = 1.54$ (pessimistic).

    **Strategy (c): Purely static replication.**

    - **Transaction costs**: Only the initial setup:

    $$
    \text{TC}_c \approx 0.001 \times 2 \times 8 = 0.016
    $$

    - **Hedging error**: No adjustment at the barrier, so if the static portfolio does not perfectly offset at $S = H$, there is a persistent error. For barrier options, static replication without model-specific adjustments can have significant error:

    $$
    \text{HE}_c \approx 1.0 \text{ to } 3.0
    $$

    - **Total cost**: $\approx 0.016 + 2.0 = 2.02$ (typical).

    **Comparison**:

    | Strategy | Transaction Costs | Hedging Error | Total |
    |----------|------------------|---------------|-------|
    | (a) Continuous delta | $\approx 0.8$ | $\approx 0.06$ | $\approx 0.86$ |
    | (b) Semi-static | $\approx 0.04$ | $\approx 0.5-1.5$ | $\approx 0.5-1.5$ |
    | (c) Purely static | $\approx 0.02$ | $\approx 2.0$ | $\approx 2.0$ |

    **Conclusion**: Strategy (b) (semi-static) is likely the cheapest, with total cost in the range \$0.5--\$1.5, compared to \$0.86 for continuous delta hedging. The semi-static approach dramatically reduces transaction costs while maintaining reasonable hedging accuracy through the single adjustment at the barrier. The purely static approach is cheapest in terms of transaction costs but suffers from large hedging errors.

---

**Exercise 4.** For a forward start option with payoff $(S_T / S_{T_1} - 1)^+$, design a semi-static hedging strategy. The static component should be established at time $0$ and the dynamic adjustment should occur at time $T_1$ when the strike becomes known. What vanilla instruments are needed at each time, and how do the required positions depend on $S_{T_1}$?

??? success "Solution to Exercise 4"

    **Forward start option payoff**: $(S_T / S_{T_1} - 1)^+ = \frac{1}{S_{T_1}}(S_T - S_{T_1})^+$.

    This is a call option whose strike $K = S_{T_1}$ is set at the future time $T_1$.

    **Semi-static hedging strategy.**

    **Phase 1: Time 0 to $T_1$ (before strike is known).**

    At time 0, we do not know the strike, but we know the payoff structure. The forward start call has the property that under the Black-Scholes model, its value at time 0 is:

    $$
    V_0 = \mathbb{E}\left[e^{-rT}\frac{1}{S_{T_1}}(S_T - S_{T_1})^+\right]
    $$

    By the scaling property of GBM, $S_T/S_{T_1}$ conditional on $\mathcal{F}_{T_1}$ is independent of $S_{T_1}$, so:

    $$
    V_0 = e^{-rT} \mathbb{E}\left[\frac{(S_T - S_{T_1})^+}{S_{T_1}}\right] = e^{-rT_1} C_{\text{BS}}(1, 1, T-T_1, \sigma, r)
    $$

    where $C_{\text{BS}}(1, 1, \tau, \sigma, r)$ is the Black-Scholes price of a unit-strike call on a unit-spot asset with time to maturity $\tau = T - T_1$.

    **Static component at time 0**: Since the value depends on the **ratio** $S_T/S_{T_1}$, the initial hedge should be proportional to the current spot. Hold:

    - Cash: $V_0$ in the risk-free bond
    - No stock position needed initially (delta is approximately zero for the ratio payoff)

    Alternatively, if ATM options maturing at $T_1$ and $T$ are available, establish positions that capture the forward volatility.

    **Phase 2: At time $T_1$ (strike becomes known).**

    When $S_{T_1}$ is observed, the forward start option becomes a standard call with:

    - Strike: $K = S_{T_1}$
    - Remaining maturity: $T - T_1$
    - Current spot: $S_{T_1}$

    **Dynamic adjustment at $T_1$**: Liquidate any positions from Phase 1 and establish:

    - **Vanilla call**: Buy $1/S_{T_1}$ units of a call with strike $K = S_{T_1}$ and maturity $T$. This has payoff $\frac{1}{S_{T_1}}(S_T - S_{T_1})^+$, which is exactly the forward start payoff.
    - **Delta hedge**: Optionally, set up a delta hedge $\theta_{T_1} = \frac{1}{S_{T_1}}\Delta_{\text{BS}}(S_{T_1}, S_{T_1}, T-T_1)$ shares.

    **Phase 3: Time $T_1$ to $T$ (after strike is known).**

    The position is a standard vanilla call, which can be held statically until maturity (if exact strike options are available) or delta-hedged dynamically.

    **Dependence on $S_{T_1}$**: The number of calls to purchase, $1/S_{T_1}$, depends inversely on the realized spot at $T_1$. If $S_{T_1}$ is high, fewer calls are needed (each worth more); if $S_{T_1}$ is low, more calls are needed. The total cost of the calls at time $T_1$ is:

    $$
    \text{Cost} = \frac{1}{S_{T_1}} \times C_{\text{BS}}(S_{T_1}, S_{T_1}, T-T_1) = C_{\text{BS}}(1, 1, T-T_1)
    $$

    which is independent of $S_{T_1}$ (by homogeneity of the Black-Scholes formula). This confirms the strategy is self-financing if $V_0$ is set correctly.

---

**Exercise 5.** Formalize the semi-static hedging problem as an optimization. Given a target exotic payoff $\Phi$, static positions $\alpha_i$ in vanilla options $\{V_i\}_{i=1}^N$, and a dynamic strategy $\theta_t$, minimize the expected squared hedging error:

$$
\min_{\alpha, \theta} \mathbb{E}\left[\left(\Phi - \sum_{i=1}^N \alpha_i V_i(S_T) - \int_0^T \theta_t \, dS_t\right)^2\right]
$$

Explain why separating the problem into static and dynamic components simplifies the optimization.

??? success "Solution to Exercise 5"

    **Formulation**: Given target payoff $\Phi$, static positions $\alpha_i$ in vanillas $\{V_i\}_{i=1}^N$, and dynamic strategy $\theta_t$:

    $$
    \min_{\alpha, \theta}\; \mathbb{E}\left[\left(\Phi - \sum_{i=1}^N \alpha_i V_i(S_T) - \int_0^T \theta_t\, dS_t\right)^2\right]
    $$

    **Step 1: Orthogonal decomposition.**

    Define the residual payoff after the static component:

    $$
    R \equiv \Phi - \sum_{i=1}^N \alpha_i V_i(S_T)
    $$

    The objective becomes:

    $$
    \min_{\alpha, \theta}\; \mathbb{E}\left[\left(R - \int_0^T \theta_t\, dS_t\right)^2\right]
    $$

    The stochastic integral $\int_0^T \theta_t\, dS_t$ lies in the space of martingale gains (assuming $S$ is a martingale under the pricing measure, i.e., $r = 0$). This space is orthogonal to any constant, so:

    $$
    \mathbb{E}\left[\left(R - \int_0^T \theta_t\, dS_t\right)^2\right] = (\mathbb{E}[R])^2 + \text{Var}\left(R - \int_0^T \theta_t\, dS_t\right)
    $$

    **Step 2: Separation principle.**

    The optimization separates into two independent problems:

    **(a) Static optimization**: Choose $\alpha$ to minimize the "unhedgeable" component of $R$. Specifically, the optimal $\alpha$ should make $R$ as close as possible to the span of martingale gains:

    $$
    \min_\alpha\; \min_\theta\; \mathbb{E}\left[\left(\Phi - \sum_i \alpha_i V_i - \int_0^T \theta_t\, dS_t\right)^2\right]
    $$

    **(b) Dynamic optimization**: Given $\alpha$, choose $\theta$ to minimize the variance of the residual $R - \int_0^T \theta_t\, dS_t$. This is the **mean-variance hedging** problem, whose solution is the Galtchouk-Kunita-Watanabe (GKW) projection:

    $$
    \theta_t^* = \frac{d\langle M^R, S\rangle_t}{d\langle S, S\rangle_t}
    $$

    where $M^R$ is the martingale part of $\mathbb{E}[R | \mathcal{F}_t]$.

    **Why the separation simplifies the optimization.**

    1. **Dimensionality reduction**: The static component is a finite-dimensional optimization over $\alpha \in \mathbb{R}^N$ (just $N$ parameters), while the dynamic component is an infinite-dimensional optimization over the process $\theta$. The GKW projection has a closed-form solution given $R$, so the dynamic part is solved analytically once $\alpha$ is fixed.

    2. **Convexity**: The full problem is jointly convex in $(\alpha, \theta)$, and the separation exploits the block structure. The static problem can be solved via linear regression of $\Phi$ on $\{V_i(S_T)\}$, and the dynamic problem reduces to computing conditional expectations.

    3. **Practical implementation**: The static positions $\alpha_i$ are set at time 0 and held to maturity (no rebalancing needed), while the dynamic component $\theta_t$ is updated over time. This clean separation makes the strategy operationally feasible: the expensive part (options trading) is done once, and only stock trading is done dynamically.

    4. **Robustness**: The static component provides a model-free payoff at maturity (since $\sum_i \alpha_i V_i(S_T)$ depends only on $S_T$), while the dynamic component absorbs path-dependent risk. Errors in the dynamic component affect only the residual, not the static base.

---

**Exercise 6.** A semi-static hedge for a double barrier option $\mathbb{1}\{L \leq S_t \leq H, \forall t\}$ involves adjustments at each barrier touch. In a discrete monitoring setting (daily), describe the adjustment protocol: what positions are modified when $S_t$ crosses $L$ or $H$, and how does the strategy differ from continuous monitoring? Discuss the model risk arising from the discrete vs. continuous monitoring discrepancy.

??? success "Solution to Exercise 6"

    **Setup**: Double barrier option with payoff $\mathbb{1}\{L \leq S_t \leq H, \forall t\}$, discrete daily monitoring.

    **Adjustment protocol.**

    **Initial static portfolio**: Establish positions in vanilla options that approximate the double-no-touch payoff. A common approach uses a portfolio of calls and puts at strikes near $L$ and $H$:

    - Long a tight put spread near $L$ (approximates digital put at $L$)
    - Long a tight call spread near $H$ (approximates digital call at $H$)
    - Cash position to fund the payoff if neither barrier is hit

    **Daily monitoring protocol**:

    At each monitoring time $t_i$ ($i = 1, \ldots, N$):

    **Case 1: $S_{t_i}$ crosses the upper barrier ($S_{t_i} \geq H$).**

    - The option is knocked out: payoff becomes 0.
    - **Action**: Liquidate all static option positions and the dynamic stock hedge.
    - Invest proceeds in risk-free bonds.
    - No further hedging required.

    **Case 2: $S_{t_i}$ crosses the lower barrier ($S_{t_i} \leq L$).**

    - The option is knocked out: payoff becomes 0.
    - **Action**: Same as Case 1 --- liquidate all positions.

    **Case 3: $S_{t_i}$ is near the upper barrier ($H - \epsilon < S_{t_i} < H$).**

    - The option is at risk of knockout.
    - **Action**: Increase the short delta position (the option delta becomes very negative near $H$). Adjust the static put spread to provide more protection. Tighten the rebalancing threshold.

    **Case 4: $S_{t_i}$ is near the lower barrier ($L < S_{t_i} < L + \epsilon$).**

    - Similar to Case 3 but mirrored.
    - **Action**: Increase the long delta position. Adjust the static call spread.

    **Case 5: $S_{t_i}$ is well between barriers ($L + \epsilon \leq S_{t_i} \leq H - \epsilon$).**

    - The option is far from knockout; low urgency.
    - **Action**: Minimal or no adjustment. Maintain existing positions.

    **Discrete vs. continuous monitoring: key differences.**

    1. **Barrier breach detection**: Under continuous monitoring, the barrier is hit as soon as $S_t$ touches $L$ or $H$. Under discrete monitoring, $S_t$ could cross the barrier and return between observation times. The discrete barrier option is therefore **more valuable** (less likely to knock out) than the continuous version.

    2. **Continuity correction**: The discrete barrier option price can be approximated by the continuous barrier price with a shifted barrier (Broadie-Glasserman-Kou, 1997):

        $$
        H_{\text{eff}} = H \cdot e^{\beta \sigma \sqrt{\delta t}}, \qquad L_{\text{eff}} = L \cdot e^{-\beta \sigma \sqrt{\delta t}}
        $$

        where $\beta \approx 0.5826$ and $\delta t = T/N$ is the monitoring interval. The effective barriers are shifted outward, reflecting the reduced knockout probability.

    3. **Hedging gap risk**: Between monitoring dates, the stock may breach the barrier without triggering knockout. The hedger faces "gap risk" --- the possibility that $S$ jumps through the barrier between observations. This is unhedgeable with discrete monitoring.

    **Model risk from the discrepancy.**

    The primary model risks are:

    - **Overshoot risk**: If the static hedge is calibrated to continuous barriers but the contract has discrete barriers, the hedge systematically over-protects (too conservative), wasting hedging capital.
    - **Undershoot risk**: If the hedge is calibrated to discrete barriers but realized dynamics include jumps or fast moves, the stock may breach the true continuous path barrier between monitoring times, creating unhedged losses.
    - **Gamma spike timing**: The sharp gamma increase near barriers occurs at slightly different spot levels for discrete vs. continuous monitoring, causing systematic hedging error if the wrong barrier specification is used.

---

**Exercise 7.** Prove that for any European payoff $g(S_T)$ that is twice differentiable, the Carr-Madan static replication is exact and model-free. Then explain why path-dependent payoffs generally cannot be perfectly replicated statically and require the dynamic component. Give an example of a path-dependent payoff for which the semi-static hedge achieves exact replication under specific model assumptions but not model-free.

??? success "Solution to Exercise 7"

    **Part 1: Proof that Carr-Madan static replication is exact and model-free for European payoffs.**

    **Theorem**: For any twice-differentiable function $g: \mathbb{R}_+ \to \mathbb{R}$ and any fixed point $F > 0$:

    $$
    g(x) = g(F) + g'(F)(x - F) + \int_0^F g''(K)(K - x)^+\, dK + \int_F^\infty g''(K)(x - K)^+\, dK
    $$

    for all $x > 0$.

    **Proof**: Define the right-hand side as $h(x)$ and show $h(x) = g(x)$ for all $x > 0$.

    **Case 1: $x \geq F$.** Then $(K - x)^+ = 0$ for $K \leq x$ (in particular for $K \leq F$), and $(x - K)^+ = x - K$ for $K \leq x$. So:

    $$
    h(x) = g(F) + g'(F)(x - F) + 0 + \int_F^x g''(K)(x - K)\, dK + 0
    $$

    (The integral from $x$ to $\infty$ vanishes because $(x-K)^+ = 0$ for $K > x$.)

    Integrate by parts: Let $u = g''(K)$, $dv = (x-K)\, dK$. Actually, it is easier to use the fundamental theorem of calculus directly. Note:

    $$
    \int_F^x g''(K)(x - K)\, dK = \int_F^x g''(K) \int_K^x d\ell\, dK = \int_F^x \int_F^\ell g''(K)\, dK\, d\ell
    $$

    by Fubini's theorem (switching order of integration). The inner integral is:

    $$
    \int_F^\ell g''(K)\, dK = g'(\ell) - g'(F)
    $$

    So:

    $$
    \int_F^x g''(K)(x-K)\, dK = \int_F^x [g'(\ell) - g'(F)]\, d\ell = [g(x) - g(F)] - g'(F)(x - F)
    $$

    Therefore:

    $$
    h(x) = g(F) + g'(F)(x-F) + g(x) - g(F) - g'(F)(x-F) = g(x)
    $$

    **Case 2: $x < F$.** By symmetric argument using $(K - x)^+ = K - x$ for $K \geq x$ and $(x - K)^+ = 0$ for $K \geq x$:

    $$
    h(x) = g(F) + g'(F)(x - F) + \int_x^F g''(K)(K - x)\, dK
    $$

    By the same Fubini argument:

    $$
    \int_x^F g''(K)(K-x)\, dK = [g(F) - g(x)] - g'(x)(F - x)
    $$

    Wait, let us redo this carefully:

    $$
    \int_x^F g''(K)(K-x)\, dK = \int_x^F \int_x^K d\ell\, g''(K)\, dK = \int_x^F \int_\ell^F g''(K)\, dK\, d\ell = \int_x^F [g'(F) - g'(\ell)]\, d\ell
    $$

    $$
    = g'(F)(F - x) - [g(F) - g(x)] = g'(F)(F-x) - g(F) + g(x)
    $$

    So:

    $$
    h(x) = g(F) + g'(F)(x - F) + g'(F)(F - x) - g(F) + g(x) = g(x)
    $$

    This proves the identity for all $x > 0$. Setting $x = S_T$ and taking expectations under any pricing measure:

    $$
    \mathbb{E}[g(S_T)] = g(F)\cdot 1 + g'(F)\cdot \mathbb{E}[S_T - F] + \int_0^F g''(K) P(K)\, dK + \int_F^\infty g''(K) C(K)\, dK
    $$

    where $P(K)$ and $C(K)$ are put and call prices. This holds for **any** model (any probability measure on $S_T$), making the replication **model-free**. $\square$

    **Part 2: Why path-dependent payoffs cannot be statically replicated.**

    A static portfolio of European options pays $\sum_i \alpha_i V_i(S_T)$ at maturity --- a function of $S_T$ only. A path-dependent payoff $\Phi((S_t)_{0 \leq t \leq T})$ depends on the entire trajectory, not just the terminal value. Two paths with the same $S_T$ but different histories (e.g., one that hit a barrier and one that did not) produce different payoffs from $\Phi$ but identical payoffs from any static portfolio.

    Formally, if $\omega_1$ and $\omega_2$ are two paths with $S_T(\omega_1) = S_T(\omega_2)$ but $\Phi(\omega_1) \neq \Phi(\omega_2)$, then no function $f(S_T)$ can satisfy $f(S_T) = \Phi$ for both paths simultaneously. Therefore, $\Phi$ cannot be replicated by any static portfolio of European instruments.

    The dynamic component $\int_0^T \theta_t\, dS_t$ is needed precisely because it depends on the **entire path** through the integrand $\theta_t$ (which can be adapted to the filtration), allowing it to distinguish between paths with the same terminal value but different histories.

    **Part 3: Example of semi-static exact replication under model assumptions.**

    **Up-and-out call**: $\Phi = (S_T - K)^+ \mathbb{1}\{M_T < H\}$ where $M_T = \max_{t \leq T} S_t$.

    Under **Black-Scholes with constant volatility**, the reflection principle gives an exact semi-static replication:

    - **Static portfolio**: Long call at $K$, short $(H/S_0)^{2\mu}$ calls at strike $K$ (evaluated at reflected spot $H^2/S_0$).
    - **Dynamic action**: Liquidate at the barrier hit time $\tau$ (if it occurs).

    This is **exact under Black-Scholes** because the reflection principle holds perfectly with constant volatility, ensuring the static portfolio value is zero at $S = H$.

    However, this replication is **not model-free** because:

    1. Under **stochastic volatility**, the reflection principle fails (the symmetry between the original and reflected process breaks down), and the static portfolio has nonzero value at the barrier.
    2. Under **jump diffusion**, the stock can jump through the barrier, and the static hedge at barrier touch has the wrong value.
    3. Under **local volatility** $\sigma(S,t)$, the reflection symmetry requires a specific relationship between $\sigma(S,t)$ and $\sigma(H^2/S, t)$ that is generally not satisfied.

    Thus, the up-and-out call is a canonical example of a path-dependent payoff admitting exact semi-static replication under a specific model but requiring model-dependent corrections (additional dynamic adjustments) in general.
