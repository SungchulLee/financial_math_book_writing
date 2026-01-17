# Open Problems in Financial Mathematics


## Introduction


Despite decades of development, financial mathematics contains numerous **open problems** — questions that remain unsolved or areas where current models are known to be inadequate. These open problems represent both intellectual challenges and practical limitations of quantitative finance.

This section surveys major open problems across several domains:
1. **Volatility modeling**: Rough volatility, market microstructure
2. **Model calibration**: Consistency, stability, joint calibration
3. **Machine learning**: Deep hedging, explainability
4. **Systemic risk**: Network effects, contagion
5. **Climate finance**: Pricing climate risk, transition modeling

## Volatility Surface Dynamics


### 1. The Volatility Surface Puzzle


**Observation**: Implied volatility varies across strikes and maturities, forming a **surface**.

**Challenge**: No single model captures:
- Smile (convexity in strike)
- Skew (asymmetry)
- Term structure
- **Dynamics** of the surface over time

**Stochastic Volatility Models**: Heston, SABR capture static smile but struggle with:

$$
\frac{\partial \sigma_{\text{impl}}}{\partial S} \neq \text{observed}
$$

### 2. Joint Calibration Problem


**Challenge**: Calibrate model simultaneously to:
- Vanilla options (all strikes, maturities)
- Variance swaps
- VIX options
- Exotic path-dependent options

**Current State**: Models calibrated to vanillas often misprice exotics; no unified model fits all instruments well.

### 3. Smile Dynamics


**Question**: How does the volatility smile move when the underlying moves?

**Sticky Strike**: Implied vol fixed for given strike.

**Sticky Delta**: Implied vol fixed for given delta.

**Reality**: Neither perfectly describes market behavior.

**Open Problem**: Model that endogenously generates realistic smile dynamics.

## Rough Volatility


### 1. Empirical Evidence


**Finding** (Gatheral et al., 2018): Log-volatility behaves like fractional Brownian motion with Hurst parameter $H \approx 0.1$:

$$
\mathbb{E}[|\log \sigma_{t+\Delta} - \log \sigma_t|^2] \sim \Delta^{2H}
$$

**Implication**: Volatility is **rougher** than standard diffusion ($H = 0.5$).

### 2. Rough Heston Model


**Dynamics**:

$$
dV_t = \kappa (\bar{V} - V_t) dt + \nu \sqrt{V_t} dW_t^H
$$

where $W_t^H$ is fractional Brownian motion with $H < 0.5$.

**Advantage**: Better fits short-term smile and ATM skew.

**Challenge**: 
- Not a Markov process; requires infinite-dimensional state
- Numerical methods computationally intensive
- Hedging strategy unclear

### 3. Open Questions


1. **Efficient Calibration**: Fast algorithms for rough volatility calibration
2. **Hedging**: Delta-hedging strategy under rough dynamics
3. **Risk Management**: VaR calculation with non-Markovian dynamics
4. **Economic Foundation**: Why is volatility rough?

## Market Microstructure


### 1. Price Formation


**Question**: How do prices emerge from order flow?

**Kyle Model**: Single informed trader; price impact proportional to order size.

**Reality**: Multiple informed traders, complex order types, high-frequency dynamics.

**Open Problem**: Tractable equilibrium model with:
- Multiple strategic traders
- Realistic order book dynamics
- Endogenous volatility

### 2. Optimal Execution


**Almgren-Chriss**: Minimize execution cost under linear price impact.

**Extensions Needed**:
- Nonlinear, non-permanent impact
- Stochastic liquidity
- Multiple assets
- Game-theoretic interaction with other traders

**Open Problem**: Optimal execution with realistic market impact function.

### 3. High-Frequency Limit


**Question**: What happens as trading frequency $\to \infty$?

**Observation**: Microstructure noise, bid-ask bounce, discrete prices.

**Open Problem**: Continuous-time limit that correctly captures:
- Price discreteness
- Market maker behavior
- Information revelation

## Deep Hedging and Machine Learning


### 1. Deep Hedging Framework


**Idea** (Buehler et al., 2019): Learn hedging strategy directly via neural networks:

$$
\Delta_t = \text{NN}(S_t, V_t, t; \theta)
$$

trained to minimize hedging loss.

**Advantages**:
- Model-free
- Handles transaction costs, constraints
- Captures complex dynamics

### 2. Open Problems


**Explainability**: Why does the neural network recommend this hedge?

**Generalization**: Does strategy work in regimes not in training data?

**Robustness**: Sensitivity to training data, architecture choices.

**Consistency**: How to ensure no-arbitrage constraints?

### 3. Theoretical Questions


1. **Convergence**: Does deep hedging converge to optimal strategy?
2. **Sample Complexity**: How much data needed for reliable hedging?
3. **Uncertainty Quantification**: Confidence intervals for neural network outputs?

## Calibration Challenges


### 1. Arbitrage-Free Interpolation


**Problem**: Given finite option prices, construct arbitrage-free surface.

**Constraints**:
- Call prices decreasing in strike
- Convexity: $\frac{\partial^2 C}{\partial K^2} \geq 0$
- Calendar spread: $C(K, T_1) \leq C(K, T_2)$ for $T_1 < T_2$

**Open Problem**: Optimal interpolation that:
- Satisfies arbitrage constraints
- Minimizes smoothness penalty
- Has closed-form or fast numerical solution

### 2. Joint SPX-VIX Calibration


**Challenge**: Calibrate single model to both S&P 500 options and VIX options.

**Difficulty**: Standard stochastic volatility models cannot match both:
- SPX smile shape
- VIX option prices

**Potential Solutions**: Path-dependent volatility, jumps in volatility, rough volatility.

**Open Problem**: Tractable model fitting both markets.

### 3. Martingale Optimal Transport


**Setup**: Find joint distribution of $(S_{T_1}, S_{T_2})$ consistent with marginals (from options) and martingale property.

**Solved**: Two marginals.

**Open Problems**:
- Multiple marginals (more than 2 dates)
- Path-dependent constraints
- Computational efficiency for high dimensions

## Systemic Risk and Contagion


### 1. Network Models


**Setup**: Financial institutions connected through obligations:

$$
\bar{p}_i = \min\left(d_i + \sum_j \pi_{ij} \bar{p}_j, c_i\right)
$$

where $\bar{p}_i$ is clearing payment, $\pi_{ij}$ is liability fraction.

**Eisenberg-Noe**: Existence and uniqueness of clearing vector.

**Open Problems**:
- Realistic network formation
- Dynamic network evolution
- Optimal intervention strategies

### 2. Contagion Mechanisms


**Direct Contagion**: Defaults propagate through obligations.

**Indirect Contagion**: Fire sales, funding liquidity, information contagion.

**Open Problem**: Unified model capturing all contagion channels.

### 3. Systemic Risk Measures


**Question**: How to measure contribution of institution to systemic risk?

**Proposals**: CoVaR, SRISK, network centrality measures.

**Open Problem**: Axiomatic foundation for systemic risk measures.

## Climate Finance


### 1. Climate Risk Pricing


**Physical Risk**: Direct impact of climate change (floods, droughts).

**Transition Risk**: Economic impact of decarbonization (stranded assets).

**Question**: How should asset prices reflect climate risk?

**Challenge**: 
- Long time horizons (decades)
- Deep uncertainty about climate outcomes
- Non-stationarity

### 2. Carbon Pricing Models


**Problem**: Model carbon permit prices for hedging and valuation.

**Features**:
- Policy-dependent dynamics
- Rare events (policy changes)
- Link to economic activity

**Open Problem**: Stochastic model for carbon prices with economic foundations.

### 3. Green Bonds and ESG


**Greenium**: Do green bonds trade at premium?

**Question**: Equilibrium model for ESG premium.

**Challenge**: Define and measure ESG consistently.

## Cryptocurrency and DeFi


### 1. Crypto Asset Pricing


**Challenge**: Traditional models assume economic fundamentals; cryptos have novel value drivers.

**Open Questions**:
- Fundamental value of cryptocurrency
- Appropriate discount rate
- Role of network effects

### 2. DeFi Protocol Risk


**Automated Market Makers**: Liquidity pools with algorithmic pricing.

**Open Problems**:
- Optimal AMM design
- Impermanent loss mitigation
- Cross-protocol contagion

### 3. Smart Contract Risk


**Question**: How to price risk of smart contract bugs or exploits?

**Challenge**: Fat-tailed, correlated risks without historical data.

## Mathematical Frontiers


### 1. Model-Free Finance


**Goal**: Price and hedge without specifying full model.

**Tools**: Martingale optimal transport, robust hedging.

**Open Problem**: Extend model-free methods to:
- Path-dependent options
- Multiple underlying assets
- Transaction costs

### 2. Infinite-Dimensional Stochastic Analysis


**Motivation**: Interest rate term structure, volatility surfaces are infinite-dimensional.

**SPDEs**: Stochastic partial differential equations for factor dynamics.

**Open Problems**:
- Well-posedness for relevant SPDEs
- Numerical methods for high-dimensional problems
- Statistical inference in function spaces

### 3. Backward Stochastic PDEs


**2BSDEs**: Second-order BSDEs for uncertain volatility.

**Open Problems**:
- Existence/uniqueness for general coefficients
- Numerical schemes that scale to high dimensions
- Connection to fully nonlinear PDEs

## Practical Open Challenges


### 1. Real-Time Calibration


**Challenge**: Calibrate complex models in real-time as markets move.

**Constraint**: Millisecond to second latency requirements.

**Open Problem**: Algorithms balancing accuracy and speed.

### 2. Model Uncertainty Quantification


**Challenge**: Quantify uncertainty in model outputs.

**Current State**: Point estimates dominate practice.

**Open Problem**: Practical methods for:
- Confidence intervals for prices
- Model risk reserves
- Parameter uncertainty propagation

### 3. Multi-Asset Modeling


**Challenge**: Model joint dynamics of many assets.

**Curse of Dimensionality**: Parameters grow as $O(n^2)$ or worse.

**Open Problem**: Parsimonious multi-asset models that:
- Capture dependence structure
- Remain tractable
- Calibrate stably

## Summary


### Classification of Open Problems


| Domain | Problem | Difficulty | Practical Impact |
|--------|---------|------------|------------------|
| Volatility | Smile dynamics | High | High |
| Rough vol | Efficient calibration | High | Medium |
| Microstructure | Optimal execution | Medium | High |
| ML/Deep hedging | Explainability | High | High |
| Calibration | SPX-VIX joint | Medium | High |
| Systemic risk | Network contagion | High | High |
| Climate | Risk pricing | Very High | Growing |

### Research Directions


1. **Rough volatility**: Develop efficient numerical methods and economic foundations
2. **Machine learning**: Establish theoretical foundations for deep hedging
3. **Systemic risk**: Integrate network models with macro-finance
4. **Climate finance**: Build models for long-horizon, deep uncertainty
5. **Model-free methods**: Extend to practical settings with frictions

Financial mathematics remains a vibrant field with fundamental open questions that have both intellectual depth and practical significance. Progress on these problems will shape the future of quantitative finance.
