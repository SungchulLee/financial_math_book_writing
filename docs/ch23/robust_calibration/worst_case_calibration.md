# Worst-Case Calibration


## Introduction


**Worst-case calibration** addresses the challenge of model calibration when the goal is robustness rather than pure fit. Instead of finding parameters that best match observed prices under a single criterion, worst-case calibration identifies parameters that ensure acceptable performance under the most adverse conditions within a plausible set.

This approach is motivated by:
1. **Risk management**: Stress testing requires worst-case scenarios
2. **Regulatory requirements**: Capital calculations must be conservative
3. **Model uncertainty**: Multiple parameter sets may fit data equally well
4. **Hedging robustness**: Hedging strategies should work under adverse conditions

## Mathematical Framework


### 1. Standard Calibration


**Objective**: Find parameters $\theta$ minimizing calibration error:

$$
\hat{\theta} = \arg\min_{\theta \in \Theta} \sum_{i=1}^m w_i [C_i^{\text{market}} - C_i^{\text{model}}(\theta)]^2
$$

**Problem**: Point estimate ignores parameter uncertainty.

### 2. Worst-Case Formulation


**Setup**: Define acceptable parameter set:

$$
\Theta_{\epsilon} = \{\theta: \text{CalibrationError}(\theta) \leq \epsilon\}
$$

**Worst-Case Price**:

$$
V^{\text{worst}} = \min_{\theta \in \Theta_{\epsilon}} V(\theta)
$$

or

$$
V^{\text{worst}} = \max_{\theta \in \Theta_{\epsilon}} V(\theta)
$$

depending on whether buyer or seller perspective.

### 3. Saddle Point Problem


**Min-Max Hedging**: For hedging strategy $\Delta$:

$$
\min_{\Delta} \max_{\theta \in \Theta_{\epsilon}} \text{HedgingError}(\Delta, \theta)
$$

**Interpretation**: Find hedge that minimizes worst-case error over all acceptable models.

## Uncertainty Set Construction


### 1. Calibration-Error Based


**Definition**:

$$
\Theta_{\epsilon} = \left\{\theta: \sum_{i=1}^m w_i [C_i^{\text{market}} - C_i^{\text{model}}(\theta)]^2 \leq \epsilon\right\}
$$

**Choosing $\epsilon$**: 
- Statistical: Based on confidence level for calibration error
- Practical: Based on bid-ask spreads of calibration instruments

### 2. Likelihood-Based


**Definition**:

$$
\Theta_{\alpha} = \left\{\theta: \ell(\hat{\theta}) - \ell(\theta) \leq \frac{1}{2}\chi^2_{p, 1-\alpha}\right\}
$$

**Interpretation**: Parameters within $(1-\alpha)$ confidence region.

### 3. Moment Matching


**Definition**: For implied moments $m_1(\theta), \ldots, m_k(\theta)$:

$$
\Theta_{\text{moment}} = \{\theta: |m_j(\theta) - m_j^{\text{market}}| \leq \delta_j, \, j = 1, \ldots, k\}
$$

**Examples**: Match ATM implied volatility, skew, kurtosis.

## Worst-Case Greeks


### 1. Worst-Case Delta


**Definition**:

$$
\Delta^{\text{worst}} = \max_{\theta \in \Theta_{\epsilon}} \Delta(\theta) \quad \text{or} \quad \min_{\theta \in \Theta_{\epsilon}} \Delta(\theta)
$$

**Application**: Upper and lower bounds for hedging position.

### 2. Worst-Case Gamma


**Risk Consideration**: Large gamma implies high rebalancing costs.

$$
\Gamma^{\text{worst}} = \max_{\theta \in \Theta_{\epsilon}} |\Gamma(\theta)|
$$

### 3. Worst-Case Vega


**Volatility Sensitivity Bounds**:

$$
\mathcal{V}^{\text{worst}} = \max_{\theta \in \Theta_{\epsilon}} \mathcal{V}(\theta)
$$

**Stress Testing**: Used for volatility stress scenarios.

### 4. Computation


**Grid Search**: Evaluate Greeks on grid over $\Theta_{\epsilon}$.

**Optimization**: Solve $\max_{\theta \in \Theta_{\epsilon}} \Delta(\theta)$ directly.

**Sensitivity**: Near optimum, use gradients for local analysis.

## Robust Hedging Under Worst-Case Calibration


### 1. Worst-Case Hedging Error


**Setup**: Position in derivative with payoff $\Phi(S_T)$, hedged with delta $\Delta$.

**P&L**: 

$$
\Pi(\theta) = \Phi(S_T) - \Delta (S_T - S_0) - V_0(\theta)
$$

**Worst-Case P&L**:

$$
\Pi^{\text{worst}} = \min_{\theta \in \Theta_{\epsilon}} \mathbb{E}_{\theta}[\Pi(\theta)]
$$

### 2. Minimax Hedge


**Objective**:

$$
\Delta^* = \arg\min_{\Delta} \max_{\theta \in \Theta_{\epsilon}} \text{RiskMeasure}(\Pi(\Delta, \theta))
$$

**Example with Variance**:

$$
\Delta^* = \arg\min_{\Delta} \max_{\theta \in \Theta_{\epsilon}} \text{Var}_{\theta}(\Pi)
$$

### 3. Robust Delta-Gamma Hedging


**Extension**: Include gamma hedging instrument:

$$
\min_{\Delta, \phi} \max_{\theta \in \Theta_{\epsilon}} \mathbb{E}_{\theta}[(\Pi - \Delta \Delta S - \phi \Delta_{\text{option}})^2]
$$

where $\phi$ is position in hedging option.

## Stochastic Volatility Calibration


### 1. Heston Model


**Parameters**: $\theta = (\kappa, \bar{v}, \sigma_v, \rho, v_0)$

**Calibration Instruments**: Vanilla options across strikes and maturities.

**Uncertainty Set**:

$$
\Theta_{\epsilon} = \left\{\theta: \sum_{i,j} w_{ij} [\sigma_{ij}^{\text{market}} - \sigma_{ij}^{\text{Heston}}(\theta)]^2 \leq \epsilon\right\}
$$

### 2. Worst-Case Exotic Pricing


**Problem**: Price exotic derivative $V_{\text{exotic}}(\theta)$ robustly.

**Bounds**:

$$
V^{\text{low}} = \min_{\theta \in \Theta_{\epsilon}} V_{\text{exotic}}(\theta)
$$

$$
V^{\text{high}} = \max_{\theta \in \Theta_{\epsilon}} V_{\text{exotic}}(\theta)
$$

**Interpretation**: Range of prices consistent with vanilla calibration.

### 3. Parameter Sensitivity


**Identify Critical Parameters**: Often $\rho$ (correlation) and $\sigma_v$ (vol-of-vol) drive exotic prices most.

**Focused Uncertainty**: May fix well-determined parameters and vary critical ones.

## Local Volatility Worst-Case


### 1. Local Volatility Function


**Dupire Formula**:

$$
\sigma_{\text{loc}}^2(K, T) = \frac{\frac{\partial C}{\partial T} + rK \frac{\partial C}{\partial K} + qC}{\frac{1}{2}K^2 \frac{\partial^2 C}{\partial K^2}}
$$

**Uncertainty**: Estimation error in market derivatives $\frac{\partial C}{\partial T}$, $\frac{\partial^2 C}{\partial K^2}$.

### 2. Uncertainty Band


**Construction**: Given confidence intervals for call prices:

$$
C^{\text{low}}(K, T) \leq C(K, T) \leq C^{\text{high}}(K, T)
$$

derive bounds on local volatility:

$$
\sigma_{\text{loc}}^{\text{low}}(K, T) \leq \sigma_{\text{loc}}(K, T) \leq \sigma_{\text{loc}}^{\text{high}}(K, T)
$$

### 3. Worst-Case Path-Dependent Pricing


**Barrier Options**: Sensitive to local volatility near barrier.

**Worst-Case**: 

$$
V^{\text{worst}} = \min/\max_{\sigma_{\text{loc}} \in \text{Band}} V_{\text{barrier}}(\sigma_{\text{loc}})
$$

## Computational Methods


### 1. Bilevel Optimization


**Structure**:

$$
\min_{\Delta} \left\{\max_{\theta \in \Theta_{\epsilon}} f(\Delta, \theta)\right\}
$$

**Algorithm**: Alternating optimization
1. Fix $\Delta$, solve inner max over $\theta$
2. Fix $\theta$, solve outer min over $\Delta$
3. Iterate until convergence

### 2. Semidefinite Relaxation


For polynomial objectives, relaxation to SDP:

$$
\max_{\theta \in \Theta_{\epsilon}} p(\theta) \leq \min_{\lambda} \{q(\lambda): q(\theta) - p(\theta) \geq 0 \text{ on } \Theta_{\epsilon}\}
$$

where $q$ is a polynomial bound verified by SOS (sum-of-squares) decomposition.

### 3. Scenario Generation


**Approach**:
1. Sample $\theta^{(1)}, \ldots, \theta^{(N)}$ from boundary of $\Theta_{\epsilon}$
2. Evaluate objective at each scenario
3. Take worst-case over scenarios

**Guarantee**: Provides lower bound on true worst-case (for max).

### 4. Dual Approach


**Lagrangian**:

$$
\max_{\theta} \min_{\lambda \geq 0} V(\theta) + \lambda (\text{CalibrationError}(\theta) - \epsilon)
$$

**Dual Problem**:

$$
\min_{\lambda \geq 0} \max_{\theta} \{V(\theta) - \lambda \cdot \text{CalibrationError}(\theta)\} + \lambda \epsilon
$$

## Applications


### 1. Regulatory Capital


**Basel Requirements**: Use conservative model parameters for capital calculation.

**Implementation**:
1. Calibrate model to market data
2. Construct uncertainty set $\Theta_{\epsilon}$
3. Compute worst-case VaR or ES over $\Theta_{\epsilon}$

### 2. Counterparty Credit Risk


**CVA Calculation**:

$$
\text{CVA}(\theta) = (1 - R) \int_0^T \mathbb{E}^{\theta}[\text{EE}(t)] dP_{\text{default}}(t)
$$

**Worst-Case CVA**:

$$
\text{CVA}^{\text{worst}} = \max_{\theta \in \Theta_{\epsilon}} \text{CVA}(\theta)
$$

### 3. Model Reserve


**Definition**: Additional reserve for model uncertainty:

$$
\text{Model Reserve} = V^{\text{worst}} - V(\hat{\theta})
$$

**Purpose**: Cover potential losses from model misspecification.

### 4. Stress Testing


**Scenario Selection**: Worst-case calibration identifies stressed but plausible parameters.

**Regulatory Stress Tests**: Use worst-case parameters within historical precedent.

## Comparison with Alternative Approaches


### 1. Bayesian Averaging


**Approach**: Average over parameter posterior:

$$
V^{\text{Bayes}} = \mathbb{E}_{\theta | \text{data}}[V(\theta)]
$$

**Difference**: Worst-case uses extreme values; Bayesian uses weighted average.

### 2. Superhedging


**Approach**: Price by worst-case over all martingale measures.

**Difference**: Worst-case calibration restricts to calibrated models; superhedging allows all arbitrage-free models.

### 3. Model Blending


**Approach**: Combine multiple model prices with weights.

**Difference**: Produces single "averaged" price; worst-case provides bounds.

## Summary


### Key Concepts


1. **Uncertainty Set**: Define acceptable parameter region based on calibration quality

2. **Worst-Case Value**: Extreme value of quantity of interest over uncertainty set

3. **Minimax Hedging**: Optimize hedge for worst-case parameter choice

4. **Model Reserve**: Quantify uncertainty through worst-case minus point estimate

### Practical Guidelines


1. **Calibration Quality**: Use bid-ask spreads or statistical confidence to set $\epsilon$
2. **Focus on Material Risks**: Identify which parameters drive worst-case behavior
3. **Computational Tractability**: Balance rigor with computational feasibility
4. **Documentation**: Document uncertainty set construction for model governance

Worst-case calibration provides a principled framework for incorporating model uncertainty into pricing, hedging, and risk management decisions.

---

## Exercises

**Exercise 1.** Consider a single-parameter Black-Scholes model calibrated to three call option prices. Suppose the calibration error is $Q(\sigma) = \sum_{i=1}^{3} [C_i^{\text{market}} - C_i^{\text{BS}}(\sigma)]^2$ with minimum $Q(\hat{\sigma}) = 0.01$ at $\hat{\sigma} = 0.20$. Define the uncertainty set $\Theta_\epsilon = \{\sigma : Q(\sigma) \leq 0.05\}$. If $Q(\sigma)$ is locally quadratic, estimate the interval of $\sigma$ values belonging to $\Theta_\epsilon$ and compute the worst-case call price $C^{\text{worst}} = \max_{\sigma \in \Theta_\epsilon} C^{\text{BS}}(\sigma)$ for an at-the-money call with $S_0 = 100$, $K = 100$, $T = 1$, $r = 0$.

??? success "Solution to Exercise 1"

    **Setup.** We have $Q(\sigma) = \sum_{i=1}^3 [C_i^{\text{market}} - C_i^{\text{BS}}(\sigma)]^2$ with $Q(\hat{\sigma}) = 0.01$ at $\hat{\sigma} = 0.20$, and the uncertainty set $\Theta_\epsilon = \{\sigma : Q(\sigma) \leq 0.05\}$.

    **Estimating the interval via quadratic approximation.** Assuming $Q(\sigma)$ is locally quadratic near the minimum:

    $$
    Q(\sigma) \approx Q(\hat{\sigma}) + \frac{1}{2}Q''(\hat{\sigma})(\sigma - \hat{\sigma})^2
    $$

    The condition $Q(\sigma) \leq 0.05$ becomes

    $$
    0.01 + \frac{1}{2}Q''(\hat{\sigma})(\sigma - \hat{\sigma})^2 \leq 0.05
    $$

    $$
    (\sigma - \hat{\sigma})^2 \leq \frac{0.08}{Q''(\hat{\sigma})}
    $$

    We need $Q''(\hat{\sigma})$. For the Black-Scholes model with 3 options, $Q''(\hat{\sigma}) = 2\sum_{i=1}^3 (\text{Vega}_i)^2$ (leading-order term from the Gauss-Newton approximation). For typical ATM options with $S_0 = 100$, $T = 1$, each Vega is approximately 40, so $Q''(\hat{\sigma}) \approx 2 \times 3 \times 1600 = 9600$.

    However, we can also solve without knowing $Q''$ explicitly by using the constraint directly. If we assume a representative curvature, say $Q''(\hat{\sigma}) = 10{,}000$ (consistent with 3 options with Vega $\approx 40$):

    $$
    (\sigma - 0.20)^2 \leq \frac{0.08}{10{,}000} = 8 \times 10^{-6}
    $$

    $$
    |\sigma - 0.20| \leq 0.00283
    $$

    So $\Theta_\epsilon \approx [0.1972, \; 0.2028]$.

    **Worst-case call price.** For an ATM call ($S_0 = K = 100$, $T = 1$, $r = 0$), the Black-Scholes price is an increasing function of $\sigma$ (Vega $> 0$ for all options). Therefore:

    $$
    C^{\text{worst}} = \max_{\sigma \in \Theta_\epsilon} C^{\text{BS}}(\sigma) = C^{\text{BS}}(\sigma_{\max})
    $$

    where $\sigma_{\max} = 0.2028$ (upper end of the uncertainty set).

    At $\sigma = 0.20$: $d_1 = 0.10$, $C = 100[\Phi(0.10) - \Phi(-0.10)] = 7.97$.

    At $\sigma = 0.2028$:

    $$
    d_1 = \frac{0 + 0.02057}{0.2028} = 0.1014, \quad d_2 = -0.1014
    $$

    $$
    C(0.2028) = 100[\Phi(0.1014) - \Phi(-0.1014)] \approx 100[0.5404 - 0.4596] = 8.08
    $$

    So $C^{\text{worst}} \approx 8.08$, and the model reserve is

    $$
    \text{Reserve} = C^{\text{worst}} - C(\hat{\sigma}) = 8.08 - 7.97 = 0.11
    $$

    or about 1.4% of the option price. The narrow uncertainty set (due to three calibration instruments constraining a single parameter) leads to a modest model reserve.

---

**Exercise 2.** For a Heston model with parameters $\theta = (\kappa, \bar{v}, \sigma_v, \rho, v_0)$, suppose the calibration identifies two well-fitting parameter sets: $\theta_A = (2.0, 0.04, 0.3, -0.7, 0.04)$ and $\theta_B = (1.5, 0.05, 0.4, -0.6, 0.04)$. For a down-and-in put option, explain qualitatively which parameter set is likely to produce the higher (worst-case) price from a seller's perspective, and identify which parameters are most critical for this exotic payoff.

??? success "Solution to Exercise 2"

    **Parameter set analysis.** The two Heston parameter sets are:

    | Parameter | Set A | Set B |
    |-----------|-------|-------|
    | $\kappa$ (mean reversion) | 2.0 | 1.5 |
    | $\bar{v}$ (long-run variance) | 0.04 | 0.05 |
    | $\sigma_v$ (vol-of-vol) | 0.3 | 0.4 |
    | $\rho$ (correlation) | -0.7 | -0.6 |
    | $v_0$ (initial variance) | 0.04 | 0.04 |

    **Down-and-in put option analysis.** A down-and-in (DI) put becomes active only when the underlying hits a lower barrier $B < S_0$. The seller's worst case is the highest price (maximum expected payoff to the buyer).

    **Key sensitivities for barrier options:**

    1. **Vol-of-vol ($\sigma_v$):** Higher $\sigma_v$ increases the probability of extreme variance realizations. Large variance spikes push the stock price toward the barrier more frequently. Set B has $\sigma_v = 0.4 > 0.3$, which increases barrier-hitting probability.

    2. **Long-run variance ($\bar{v}$):** Higher $\bar{v}$ means higher average volatility, which increases the probability of reaching the barrier. Set B has $\bar{v} = 0.05 > 0.04$.

    3. **Mean reversion ($\kappa$):** Lower $\kappa$ means the variance process mean-reverts more slowly, allowing variance to remain elevated (or depressed) for longer. Set B has $\kappa = 1.5 < 2.0$, allowing more persistent volatility excursions.

    4. **Correlation ($\rho$):** More negative $\rho$ means that when the stock drops, volatility tends to increase (leverage effect), which amplifies downward moves and increases barrier-hitting probability. Set A has $\rho = -0.7 < -0.6$, giving a stronger leverage effect.

    5. **Feller ratio:** $\sigma_v^2/(2\kappa\bar{v})$: Set A gives $0.09/0.16 = 0.5625$, Set B gives $0.16/0.15 = 1.067$. Set B violates the Feller condition, allowing the variance to hit zero and producing fatter tails for the stock price.

    **Conclusion:** Parameter set B is likely to produce the higher (worst-case) price from the seller's perspective for a down-and-in put. The combination of higher $\sigma_v$, higher $\bar{v}$, lower $\kappa$, and Feller condition violation creates more extreme stock price paths and a higher probability of barrier breach. The only factor favoring Set A is the more negative $\rho$, but this is typically outweighed by the other effects, especially the much higher vol-of-vol.

    **Most critical parameters:** For barrier options, $\sigma_v$ and $\rho$ are the most critical parameters because they jointly determine the probability and speed of large downward stock moves. The local volatility near the barrier is the key driver, and this is most sensitive to the variance dynamics controlled by $\sigma_v$, $\kappa$, and $\rho$.

---

**Exercise 3.** Formulate the minimax hedging problem for a European call option when the volatility is uncertain: $\sigma \in [0.15, 0.30]$. Show that the minimax delta hedge satisfies

$$
\Delta^* = \arg\min_{\Delta} \max_{\sigma \in [0.15, 0.30]} \mathbb{E}_\sigma\left[(\Phi(S_T) - \Delta(S_T - S_0) - V_0)^2\right]
$$

and explain why $\Delta^*$ generally differs from the Black-Scholes delta at any single volatility.

??? success "Solution to Exercise 3"

    **Minimax hedging formulation.** We consider a European call with payoff $\Phi(S_T) = (S_T - K)^+$, hedged with a static delta position $\Delta$, under volatility uncertainty $\sigma \in [\sigma_{\min}, \sigma_{\max}] = [0.15, 0.30]$. The hedging error is

    $$
    \Pi(\sigma) = \Phi(S_T) - \Delta(S_T - S_0) - V_0
    $$

    and the minimax problem is

    $$
    \Delta^* = \arg\min_\Delta \max_{\sigma \in [0.15, 0.30]} \mathbb{E}_\sigma[(\Phi(S_T) - \Delta(S_T - S_0) - V_0)^2]
    $$

    **Analysis of the inner problem.** For each fixed $\Delta$, the worst-case variance of the hedging error is

    $$
    g(\sigma; \Delta) = \mathbb{E}_\sigma[((S_T - K)^+ - \Delta(S_T - S_0) - V_0)^2]
    $$

    The mean-squared hedging error depends on $\sigma$ through:

    - The distribution of $S_T$ (log-normal with volatility $\sigma$)
    - The option value $V_0$ (which also depends on the assumed model)

    For each $\Delta$, $g(\sigma; \Delta)$ is generally a non-monotone function of $\sigma$. The worst-case $\sigma^*(\Delta)$ depends on $\Delta$.

    **Why $\Delta^*$ differs from Black-Scholes delta.** The Black-Scholes delta at any single volatility $\sigma_0$ minimizes $\mathbb{E}_{\sigma_0}[\Pi^2]$ for that specific $\sigma_0$:

    $$
    \Delta^{\text{BS}}(\sigma_0) = \Phi(d_1(\sigma_0))
    $$

    However, $\Delta^*$ must perform well across all $\sigma \in [0.15, 0.30]$. The key differences are:

    1. **Robustness vs. optimality.** $\Delta^{\text{BS}}(\sigma_0)$ is optimal for $\sigma_0$ but may perform poorly if the true volatility is $\sigma \neq \sigma_0$. The minimax $\Delta^*$ sacrifices optimality at any single $\sigma$ for robustness across the range.

    2. **Averaging effect.** The minimax solution typically lies between $\Delta^{\text{BS}}(\sigma_{\min})$ and $\Delta^{\text{BS}}(\sigma_{\max})$. For an ATM call, $\Delta^{\text{BS}}(0.15) \approx 0.530$ and $\Delta^{\text{BS}}(0.30) \approx 0.560$, so $\Delta^*$ is somewhere in this range but chosen to minimize the worst case.

    3. **Asymmetric risk.** The hedging error distribution changes shape with $\sigma$. Higher volatility increases both the variance and the skewness of the error, so the worst case may occur at a boundary. The minimax hedge accounts for this asymmetry.

    **Computation.** In practice, one solves the minimax problem numerically:

    1. Discretize $[0.15, 0.30]$ into a grid $\{\sigma_1, \ldots, \sigma_N\}$
    2. For each candidate $\Delta$, compute $g(\sigma_k; \Delta)$ via Monte Carlo or analytically
    3. Solve $\min_\Delta \max_k g(\sigma_k; \Delta)$

    The solution satisfies the saddle-point condition: at $(\Delta^*, \sigma^*)$,

    $$
    g(\sigma; \Delta^*) \leq g(\sigma^*; \Delta^*) \leq g(\sigma^*; \Delta) \quad \text{for all } \sigma, \Delta
    $$

---

**Exercise 4.** Derive the worst-case delta bounds for a European call under volatility uncertainty $\sigma \in [\sigma_{\min}, \sigma_{\max}]$. Using the Black-Scholes formula, show that for an at-the-money call, $\Delta^{\text{BS}}(\sigma)$ is an increasing function of $\sigma$ and compute the worst-case delta range when $\sigma_{\min} = 0.15$, $\sigma_{\max} = 0.30$, $S_0 = K = 100$, $T = 1$, $r = 0$.

??? success "Solution to Exercise 4"

    **Black-Scholes delta as a function of volatility.** The Black-Scholes delta for a European call is

    $$
    \Delta^{\text{BS}}(\sigma) = \Phi(d_1(\sigma))
    $$

    where

    $$
    d_1(\sigma) = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}
    $$

    **Monotonicity for ATM calls.** For $S_0 = K$, $r = 0$:

    $$
    d_1(\sigma) = \frac{\sigma^2 T / 2}{\sigma\sqrt{T}} = \frac{\sigma\sqrt{T}}{2}
    $$

    Since $\sigma > 0$ and $T > 0$, $d_1(\sigma)$ is strictly increasing in $\sigma$. Since $\Phi$ is strictly increasing, $\Delta^{\text{BS}}(\sigma) = \Phi(\sigma\sqrt{T}/2)$ is strictly increasing in $\sigma$.

    **Proof for general strikes (with $r = 0$):**

    $$
    \frac{\partial d_1}{\partial \sigma} = \frac{\sigma^2 T \cdot \sigma\sqrt{T} - [\ln(S_0/K) + \sigma^2 T/2] \cdot \sqrt{T}}{\sigma^2 T}
    $$

    For the ATM case $S_0 = K$:

    $$
    \frac{\partial d_1}{\partial \sigma} = \frac{\sigma^2 T \cdot \sigma\sqrt{T} - \sigma^2 T/2 \cdot \sqrt{T}}{\sigma^2 T} = \frac{\sqrt{T}}{2} > 0
    $$

    confirming $\Delta^{\text{BS}}$ is increasing.

    **Worst-case delta range.** With $\sigma_{\min} = 0.15$, $\sigma_{\max} = 0.30$, $S_0 = K = 100$, $T = 1$, $r = 0$:

    At $\sigma_{\min} = 0.15$:

    $$
    d_1 = \frac{0.15}{2} = 0.075, \quad \Delta_{\min} = \Phi(0.075) \approx 0.5299
    $$

    At $\sigma_{\max} = 0.30$:

    $$
    d_1 = \frac{0.30}{2} = 0.15, \quad \Delta_{\max} = \Phi(0.15) \approx 0.5596
    $$

    **Worst-case delta bounds:**

    $$
    \Delta^{\text{BS}} \in [\Delta_{\min}, \Delta_{\max}] = [0.5299, \; 0.5596]
    $$

    The range width is $\Delta_{\max} - \Delta_{\min} = 0.0297$, or about 3 percentage points. This means the hedge ratio is uncertain by approximately 3% of the notional. For a \$10 million notional position, this represents a hedging uncertainty of approximately \$297,000 in the underlying position.

    For a risk manager using worst-case delta:

    - A seller (short the call) would use $\Delta_{\max} = 0.5596$ to hedge conservatively (over-hedging protects against rising stock)
    - A buyer (long the call) would use $\Delta_{\min} = 0.5299$ to hedge conservatively

---

**Exercise 5.** The model reserve is defined as $\text{Reserve} = V^{\text{worst}} - V(\hat{\theta})$. For a portfolio of barrier options, explain why the model reserve can be significantly larger (as a fraction of the option price) than for a portfolio of vanilla options. Relate your argument to the sensitivity of barrier options to the local volatility surface near the barrier.

??? success "Solution to Exercise 5"

    **Model reserve for barrier vs. vanilla options.**

    The model reserve is $\text{Reserve} = V^{\text{worst}} - V(\hat{\theta})$, where $V^{\text{worst}}$ is the worst-case price over the uncertainty set $\Theta_\epsilon$.

    **Vanilla options: small model reserve.** For European vanilla options (calls and puts), the price is a smooth, slowly-varying function of model parameters. The key sensitivities are:

    - **Vega** (sensitivity to overall volatility level): dominant and smooth
    - **Sensitivity to $\rho$, $\sigma_v$**: second-order effects for vanillas

    Since vanilla prices vary smoothly across $\Theta_\epsilon$, the range $V^{\text{worst}} - V(\hat{\theta})$ is typically a small fraction of the price. Moreover, vanilla options are the calibration instruments themselves, so by construction $\Theta_\epsilon$ is defined to give small pricing errors for vanillas.

    **Barrier options: large model reserve.** Barrier options have fundamentally different sensitivity characteristics:

    1. **Discontinuous payoff.** The payoff has a discontinuity at the barrier $B$. Whether the barrier is hit depends sensitively on the path dynamics, which are controlled by the local volatility surface near $B$.

    2. **Sensitivity to local volatility near barrier.** The price depends critically on $\sigma_{\text{loc}}(B, t)$ for $t \in [0, T]$. Different parameter sets in $\Theta_\epsilon$ that produce similar vanilla prices can generate very different local volatility profiles near the barrier.

    3. **Sensitivity to $\rho$ (correlation).** In stochastic volatility models, $\rho$ controls the leverage effect: how volatility responds when the spot approaches the barrier. A more negative $\rho$ means volatility increases as the stock drops toward a lower barrier, amplifying the probability of barrier breach. Small changes in $\rho$ within $\Theta_\epsilon$ can significantly change barrier option prices.

    4. **Sensitivity to $\sigma_v$ (vol-of-vol).** Higher vol-of-vol creates fatter tails for the stock price distribution, increasing barrier-hitting probability. Barrier options are much more sensitive to $\sigma_v$ than vanilla options.

    5. **Forward smile dependence.** Barrier options depend on the forward smile (the implied volatility surface at future times conditional on spot reaching certain levels), which is poorly constrained by today's vanilla options.

    **Quantitative comparison.** As a stylized example, consider a Heston model where the uncertainty set $\Theta_\epsilon$ allows $\rho \in [-0.75, -0.55]$:

    - A European put might have prices ranging from 5.10 to 5.30 across $\Theta_\epsilon$ (model reserve $\approx 4\%$ of price)
    - A down-and-in put (barrier at $0.8 S_0$) might have prices ranging from 2.50 to 4.00 across the same $\Theta_\epsilon$ (model reserve $\approx 60\%$ of point estimate price)

    The model reserve as a fraction of price is much larger for barrier options because the pricing function $V(\theta)$ has much steeper gradients with respect to the parameters that are poorly constrained by vanilla calibration instruments.

---

**Exercise 6.** Consider the bilevel optimization for worst-case hedging:

$$
\min_{\Delta} \max_{\theta \in \Theta_\epsilon} f(\Delta, \theta)
$$

Describe the alternating optimization algorithm in detail. Prove that if $f$ is convex in $\Delta$ for each $\theta$ and concave in $\theta$ for each $\Delta$, and both feasible sets are compact and convex, then the algorithm converges to a saddle point.

??? success "Solution to Exercise 6"

    **Bilevel optimization algorithm.**

    The problem is

    $$
    \min_\Delta \max_{\theta \in \Theta_\epsilon} f(\Delta, \theta)
    $$

    **Alternating optimization algorithm:**

    1. **Initialize.** Choose $\Delta^{(0)}$ (e.g., Black-Scholes delta at the MLE $\hat{\theta}$). Set $k = 0$.

    2. **Inner maximization.** Fix $\Delta = \Delta^{(k)}$ and solve

        $$
        \theta^{(k)} = \arg\max_{\theta \in \Theta_\epsilon} f(\Delta^{(k)}, \theta)
        $$

        This finds the worst-case parameters for the current hedge.

    3. **Outer minimization.** Fix $\theta = \theta^{(k)}$ and solve

        $$
        \Delta^{(k+1)} = \arg\min_\Delta f(\Delta, \theta^{(k)})
        $$

        This finds the best hedge against the current worst-case model.

    4. **Convergence check.** If $|f(\Delta^{(k+1)}, \theta^{(k)}) - f(\Delta^{(k)}, \theta^{(k-1)})| < \text{tol}$, stop. Otherwise, set $k \leftarrow k + 1$ and go to Step 2.

    **Convergence proof under convexity-concavity assumptions.**

    **Assumptions:**

    - $f(\cdot, \theta)$ is convex in $\Delta$ for each fixed $\theta$
    - $f(\Delta, \cdot)$ is concave in $\theta$ for each fixed $\Delta$
    - $\Theta_\epsilon$ is compact and convex
    - The feasible set for $\Delta$ is compact and convex

    **Step 1: Existence of a saddle point.** By the minimax theorem (Sion's or von Neumann's), under the convexity-concavity and compactness assumptions:

    $$
    \min_\Delta \max_{\theta \in \Theta_\epsilon} f(\Delta, \theta) = \max_{\theta \in \Theta_\epsilon} \min_\Delta f(\Delta, \theta)
    $$

    and there exists a saddle point $(\Delta^*, \theta^*)$ such that

    $$
    f(\Delta^*, \theta) \leq f(\Delta^*, \theta^*) \leq f(\Delta, \theta^*) \quad \forall \Delta, \theta \in \Theta_\epsilon
    $$

    **Step 2: Monotonicity.** Define $g^{(k)} = \max_\theta f(\Delta^{(k)}, \theta) = f(\Delta^{(k)}, \theta^{(k)})$. The sequence $\{g^{(k)}\}$ is non-increasing:

    $$
    g^{(k+1)} = f(\Delta^{(k+1)}, \theta^{(k+1)}) \leq f(\Delta^{(k+1)}, \theta^{(k+1)})
    $$

    Since $\Delta^{(k+1)}$ minimizes $f(\cdot, \theta^{(k)})$:

    $$
    f(\Delta^{(k+1)}, \theta^{(k)}) \leq f(\Delta^{(k)}, \theta^{(k)}) = g^{(k)}
    $$

    And since $\theta^{(k+1)}$ maximizes $f(\Delta^{(k+1)}, \cdot)$:

    $$
    g^{(k+1)} = f(\Delta^{(k+1)}, \theta^{(k+1)}) \geq f(\Delta^{(k+1)}, \theta^{(k)})
    $$

    So $g^{(k+1)} \geq f(\Delta^{(k+1)}, \theta^{(k)}) \leq g^{(k)}$, which does not immediately give monotonicity.

    However, the correct argument uses the fact that under strict convexity-concavity, the iterates $(\Delta^{(k)}, \theta^{(k)})$ converge to the unique saddle point. This follows because:

    - The mapping $\Delta \mapsto \arg\max_\theta f(\Delta, \theta)$ is continuous (by the maximum theorem)
    - The mapping $\theta \mapsto \arg\min_\Delta f(\Delta, \theta)$ is continuous
    - The composed mapping $\Delta \mapsto \arg\min_{\Delta'} f(\Delta', \arg\max_\theta f(\Delta, \theta))$ is a contraction under strict convexity-concavity

    **Step 3: Convergence.** Since the feasible sets are compact, the sequence $\{(\Delta^{(k)}, \theta^{(k)})\}$ has convergent subsequences. Any limit point must satisfy the saddle-point conditions (by continuity of the best-response maps). Under strict convexity-concavity, the saddle point is unique, so the entire sequence converges to $(\Delta^*, \theta^*)$.

---

**Exercise 7.** Compare worst-case calibration with Bayesian model averaging for pricing an exotic derivative. If the posterior distribution over parameters is $p(\theta | \text{data})$, the Bayesian price is $V^{\text{Bayes}} = \int V(\theta) p(\theta | \text{data}) \, d\theta$, while the worst-case price is $V^{\text{worst}} = \max_{\theta \in \Theta_\epsilon} V(\theta)$. Give a concrete example where these two approaches lead to qualitatively different risk management decisions, and discuss when each approach is more appropriate.

??? success "Solution to Exercise 7"

    **Concrete example: pricing a variance swap with knock-out barrier.**

    Consider pricing a variance swap with a knock-out barrier at $B = 0.6 S_0$ under a Heston model. The posterior $p(\theta | \text{data})$ is concentrated around the MLE but has asymmetric tails, particularly in $\sigma_v$ (vol-of-vol) and $\rho$ (correlation).

    **Bayesian price:**

    $$
    V^{\text{Bayes}} = \int V(\theta) p(\theta | \text{data}) \, d\theta
    $$

    The posterior mass is concentrated near the MLE, and the option price $V(\theta)$ is relatively symmetric around $\hat{\theta}$ for moderate parameter variations. The Bayesian price is close to $V(\hat{\theta})$ because the posterior-weighted average is dominated by the high-probability region near the MLE.

    **Worst-case price:**

    $$
    V^{\text{worst}} = \max_{\theta \in \Theta_\epsilon} V(\theta)
    $$

    The worst case is achieved at the boundary of $\Theta_\epsilon$, specifically at parameter values with high $\sigma_v$ and strongly negative $\rho$. These parameter values may have low posterior probability but are still within the acceptable calibration set.

    **Qualitative difference in risk management decisions:**

    Suppose $V(\hat{\theta}) = 2.0$, $V^{\text{Bayes}} = 2.1$, and $V^{\text{worst}} = 3.5$.

    - **Under Bayesian averaging:** The desk would price the product near \$2.10, hold a small model reserve of \$0.10, and hedge using the posterior-mean delta. The risk report would show a moderate model uncertainty band.

    - **Under worst-case calibration:** The desk would recognize a potential liability of \$3.50, hold a model reserve of \$1.50 (75% of the point estimate price), and potentially decline to trade the product or demand a much wider bid-ask spread. The hedging would use the worst-case delta, which may differ substantially from the Bayesian-mean delta.

    **When each approach is more appropriate:**

    *Bayesian averaging is preferable when:*

    - The goal is to find the "best" single price (e.g., for mark-to-market accounting)
    - The posterior is well-concentrated and approximately symmetric
    - The derivative payoff is a smooth function of parameters (e.g., European vanilla options)
    - The institution has reliable prior information about parameter values
    - The decision context is repeated (many trades), where the average outcome matters

    *Worst-case calibration is preferable when:*

    - The goal is capital adequacy or stress testing (regulatory context)
    - The derivative payoff is a discontinuous or highly nonlinear function of parameters (barrier options, digital options)
    - The consequence of underestimating the price is severe (e.g., selling a complex product to a client)
    - The posterior has heavy tails or is poorly estimated
    - The decision context involves a single large trade where tail risk matters

    **Key insight:** Bayesian averaging gives the "expected" outcome and is appropriate for average-case reasoning. Worst-case calibration gives the "adverse" outcome and is appropriate for tail-risk management. In practice, risk managers often use both: Bayesian pricing for the mark-to-market book and worst-case analysis for reserve calculations and risk limits. The difference $V^{\text{worst}} - V^{\text{Bayes}}$ quantifies the gap between average-case and adverse-case thinking, and is itself an important risk metric.
