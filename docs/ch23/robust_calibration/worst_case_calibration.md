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
