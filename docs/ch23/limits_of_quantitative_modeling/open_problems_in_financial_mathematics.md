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

---

## Exercises

**Exercise 1.** The joint calibration of SPX and VIX options remains an open problem. Explain why a model that perfectly fits the SPX implied volatility surface may fail to reproduce VIX option prices. What structural feature of the volatility dynamics (e.g., the forward variance curve) creates this tension, and why do standard stochastic volatility models struggle with it?

??? success "Solution to Exercise 1"

    **Why SPX Calibration Fails for VIX Options**

    **The VIX and Forward Variance**

    The VIX index is defined (approximately) as:

    $$
    \text{VIX}^2 = \frac{1}{T} \mathbb{E}^{\mathbb{Q}}\left[\int_0^T \sigma_s^2\, ds \,\Big|\, \mathcal{F}_0\right]
    $$

    where $T = 30/365$ and $\sigma_s$ is the instantaneous variance of the S&P 500 under the risk-neutral measure. VIX options depend on the distribution of $\text{VIX}_T$ at a future date, which requires knowledge of:

    $$
    \text{VIX}_T^2 = \frac{1}{\tau} \mathbb{E}^{\mathbb{Q}}\left[\int_T^{T+\tau} \sigma_s^2\, ds \,\Big|\, \mathcal{F}_T\right]
    $$

    This is a conditional expectation of *future* integrated variance, which depends on the dynamics of the variance process between $T$ and $T + \tau$.

    **Why SPX Calibration Is Insufficient**

    SPX options at time 0 with maturity $T$ depend on the marginal distribution of $S_T$ (or equivalently, the distribution of $\int_0^T \sigma_s^2\, ds$). These prices constrain the risk-neutral distribution of integrated variance but do **not** uniquely determine:

    1. The *path-wise dynamics* of the variance process $\sigma_t^2$.
    2. The *conditional distributions* of future variance given the state at intermediate times.
    3. The *volatility of variance* (vol-of-vol) and the *mean reversion* of variance separately --- only their combined effect on the integrated variance distribution.

    In a Heston model with parameters $(\kappa, \bar{v}, \nu, \rho, v_0)$, the SPX smile primarily constrains the combination of $\nu$ (vol-of-vol), $\rho$ (correlation), and $v_0$ (current variance). Multiple parameter sets can produce similar SPX smiles but very different VIX option prices because VIX options are sensitive to the *forward variance dynamics* --- specifically, to the conditional distribution of $v_T$ and the integrated variance path from $T$ to $T + \tau$.

    **The Structural Tension**

    Consider two models:

    - **Model A**: High vol-of-vol $\nu$, high mean reversion $\kappa$. Variance fluctuates rapidly but reverts quickly. The variance at maturity $T$ is uncertain (wide distribution), so VIX options are expensive.
    - **Model B**: Lower vol-of-vol, lower mean reversion. Variance drifts slowly. The distribution of $v_T$ may have similar marginal properties for SPX pricing, but the conditional dynamics differ, leading to different VIX option prices.

    Both models can produce similar SPX smiles because the SPX smile depends on the *marginal* of integrated variance, while VIX options depend on the *conditional* distribution of forward variance.

    **Why Standard Stochastic Volatility Models Struggle**

    In the Heston model, the forward variance curve $\mathbb{E}[v_T | \mathcal{F}_0]$ is exponentially decaying:

    $$
    \mathbb{E}^{\mathbb{Q}}[v_T | v_0] = \bar{v} + (v_0 - \bar{v}) e^{-\kappa T}
    $$

    This rigid functional form limits the model's ability to match both the SPX term structure and the VIX term structure simultaneously. The VIX smile also tends to be more symmetric and convex than what Heston generates, because the Heston model's variance distribution (non-central chi-squared) may not have the right shape for the VIX distribution.

    **Potential Solutions**

    1. **Path-dependent volatility models** (e.g., models where $\sigma_t$ depends on the path of $S$): These can decouple the SPX calibration from the forward variance dynamics.
    2. **Rough volatility models**: With $H \approx 0.1$, the forward variance curve has a different functional form that can better match both SPX and VIX simultaneously.
    3. **Models with jumps in variance**: Adding jumps to the variance process provides additional degrees of freedom to match the VIX smile shape.

---

**Exercise 2.** Rough volatility models use fractional Brownian motion with Hurst parameter $H \approx 0.1$ to capture the observed power-law behavior of implied volatility at-the-money skew. Discuss the mathematical challenges of pricing and hedging in rough volatility models: why are standard PDE methods inapplicable, and what numerical approaches (e.g., Volterra integral equations, Monte Carlo with Cholesky) are used instead?

??? success "Solution to Exercise 2"

    **Mathematical Challenges of Rough Volatility Models**

    **Why Standard PDE Methods Fail**

    In classical stochastic volatility models (e.g., Heston), the variance process $V_t$ is Markovian: its future evolution depends only on its current value. This Markov property is essential for PDE pricing, because it allows us to write the option price as a function $C(t, S, V)$ satisfying a two-dimensional PDE (the Heston PDE).

    In rough volatility models, the variance process is driven by fractional Brownian motion $W^H$ with $H < 0.5$. Fractional Brownian motion is **not** a semimartingale (for $H \neq 0.5$) and is **not** Markovian. The conditional expectation:

    $$
    \mathbb{E}[V_{t+\Delta} | \mathcal{F}_t]
    $$

    depends on the entire history of the process up to time $t$, not just on $V_t$. This means:

    1. **No finite-dimensional Markov structure**: The state space is infinite-dimensional (the entire path history). There is no PDE of the form $\partial_t C + \mathcal{L} C = 0$ in finitely many state variables.

    2. **Not a semimartingale**: The standard Ito calculus does not apply directly. The rough Heston model's variance dynamics:

        $$
        V_t = V_0 + \frac{1}{\Gamma(\alpha)} \int_0^t (t-s)^{\alpha - 1} \kappa(\bar{V} - V_s)\, ds + \frac{1}{\Gamma(\alpha)} \int_0^t (t-s)^{\alpha - 1} \nu \sqrt{V_s}\, dW_s
        $$

        where $\alpha = H + 1/2 \in (0.5, 1)$, is a Volterra-type stochastic integral equation with a singular kernel $(t - s)^{\alpha - 1}$.

    3. **No Feynman-Kac connection**: The standard Feynman-Kac theorem connects expectations of Markov diffusions to PDEs. Without the Markov property, this connection breaks down.

    **Numerical Approaches**

    *Volterra Integral Equations*:

    The characteristic function of the log-price in the rough Heston model satisfies a fractional Riccati equation:

    $$
    \psi(t) = \int_0^t K(t - s) F(\psi(s))\, ds
    $$

    where $K(t) = t^{\alpha - 1}/\Gamma(\alpha)$ is the fractional kernel and $F$ is a quadratic function derived from the Heston affine structure. This is solved numerically using Adams-type schemes for Volterra equations, which are more computationally intensive than standard ODE solvers (complexity $O(N^2)$ for $N$ time steps, versus $O(N)$ for Markov models).

    *Monte Carlo with Cholesky Decomposition*:

    Fractional Brownian motion can be simulated exactly using the Cholesky decomposition of its covariance matrix:

    $$
    \text{Cov}(W_s^H, W_t^H) = \frac{1}{2}(|s|^{2H} + |t|^{2H} - |t - s|^{2H})
    $$

    For $N$ time steps, the covariance matrix is $N \times N$, and Cholesky decomposition costs $O(N^3)$. This makes simulation expensive for fine time grids. Approximate methods include:

    - **Hybrid scheme** (Bennedsen, Lunde, Pakkanen): Decomposes the kernel into a short-memory component (simulated exactly) and a long-memory component (approximated by a sum of exponentials), reducing cost to near $O(N)$.
    - **Rough path lifts**: Using the theory of rough paths to reduce simulation complexity.

    *Markovian Approximations*:

    Approximate the rough process by a multi-factor Markov process. The fractional kernel $K(t) = t^{\alpha - 1}/\Gamma(\alpha)$ can be approximated by a sum of exponentials:

    $$
    K(t) \approx \sum_{k=1}^M c_k e^{-\lambda_k t}
    $$

    Each exponential corresponds to a Markov factor, giving an $M$-dimensional Markov system that can be priced via standard PDE methods. The approximation quality improves with $M$, but computational cost grows.

    **Hedging Challenges**

    Delta hedging under rough volatility is complicated because:

    - The delta depends on the entire volatility path, not just the current level.
    - The non-Markovian nature means the optimal hedge ratio cannot be computed from a finite-dimensional PDE.
    - Practical hedging must use approximate strategies based on Markovian projections or empirical approaches, and the hedging error from these approximations is an active area of research.

---

**Exercise 3.** The optimal execution problem asks for a trading strategy that minimizes execution cost including market impact. Formulate the Almgren-Chriss framework as a stochastic control problem and explain why the optimal strategy involves a trade-off between urgency (execution risk) and patience (market impact). What extensions are needed to handle non-linear or transient market impact?

??? success "Solution to Exercise 3"

    **Almgren-Chriss Optimal Execution Framework**

    **Problem Formulation**

    An investor must execute a trade of $X$ shares over a time horizon $[0, T]$. Let $x_t$ denote the remaining inventory at time $t$, with $x_0 = X$ and $x_T = 0$. The trading rate is $\dot{x}_t = dx_t/dt$ (continuous-time formulation; in practice, trades occur at discrete intervals).

    The stock price evolves as:

    $$
    S_t = S_0 + \sigma W_t - g(\dot{x}_t)
    $$

    where $\sigma W_t$ is the random price movement (unaffected by the trader) and $g(\dot{x}_t)$ is the **permanent price impact** from trading. Additionally, there is a **temporary impact** $h(\dot{x}_t)$ that affects only the execution price, not the fundamental price.

    **The Almgren-Chriss Objective**

    The implementation shortfall is the difference between the paper value $X \cdot S_0$ and the actual execution proceeds:

    $$
    \text{IS} = X \cdot S_0 - \int_0^T (S_t - h(\dot{x}_t)) (-\dot{x}_t)\, dt
    $$

    In the linear impact model, $g(v) = \gamma v$ (permanent impact) and $h(v) = \eta v$ (temporary impact), where $v = -\dot{x}_t > 0$ is the selling rate.

    The expected cost and variance of the implementation shortfall are:

    $$
    \mathbb{E}[\text{IS}] = \frac{1}{2}\gamma X^2 + \eta \int_0^T \dot{x}_t^2\, dt
    $$

    $$
    \text{Var}[\text{IS}] = \sigma^2 \int_0^T x_t^2\, dt
    $$

    The Almgren-Chriss problem minimizes the mean-variance objective:

    $$
    \min_{x_t} \left\{ \mathbb{E}[\text{IS}] + \lambda \cdot \text{Var}[\text{IS}] \right\} = \min_{x_t} \left\{ \eta \int_0^T \dot{x}_t^2\, dt + \lambda \sigma^2 \int_0^T x_t^2\, dt \right\}
    $$

    where $\lambda > 0$ is the risk aversion parameter and the permanent impact cost $\frac{1}{2}\gamma X^2$ is constant (independent of strategy).

    **The Urgency-Patience Trade-Off**

    The Euler-Lagrange equation for the optimization problem is:

    $$
    \eta \ddot{x}_t = \lambda \sigma^2 x_t
    $$

    with boundary conditions $x_0 = X$ and $x_T = 0$. The solution is:

    $$
    x_t = X \cdot \frac{\sinh(\kappa(T - t))}{\sinh(\kappa T)}
    $$

    where $\kappa = \sigma \sqrt{\lambda / \eta}$.

    The parameter $\kappa$ governs the trade-off:

    - **High $\lambda$ (risk-averse / urgent)**: $\kappa$ is large. The strategy front-loads execution, trading quickly at the beginning to reduce variance (execution risk). This incurs higher temporary impact cost $\eta \int \dot{x}_t^2\, dt$ because the trading rate is high.

    - **Low $\lambda$ (risk-neutral / patient)**: $\kappa$ is small. The strategy spreads execution evenly over $[0, T]$ (approaching TWAP --- time-weighted average price), minimizing temporary impact cost. But the portfolio remains exposed to price risk for longer, increasing variance.

    - In the limit $\lambda \to \infty$: Immediate execution (block trade), maximizing impact cost but eliminating price risk.
    - In the limit $\lambda \to 0$: TWAP strategy $x_t = X(1 - t/T)$, minimizing impact cost but accepting full price risk.

    **Extensions for Non-Linear and Transient Impact**

    *Non-linear permanent impact*: If $g(v) = \gamma |v|^\beta$ with $\beta \neq 1$, the Euler-Lagrange equation becomes non-linear and generally lacks closed-form solutions. Numerical methods (dynamic programming, finite differences) are needed. The qualitative trade-off persists but the optimal trajectory shape changes.

    *Transient impact*: The Almgren-Chriss model assumes permanent impact ($g$) and instantaneous temporary impact ($h$). In reality, market impact decays over time (the Obizhaeva-Wang model):

    $$
    S_t = S_0 + \sigma W_t + \int_0^t G(t - s) \, dQ_s
    $$

    where $G(t-s)$ is a decay kernel (e.g., $G(\tau) = G_0 e^{-\rho \tau}$) and $Q_t$ is the cumulative quantity traded. With transient impact, the optimal strategy can be non-monotone: it may be optimal to trade, pause (allowing impact to decay), and then trade again. This makes the problem significantly harder --- it becomes a control problem with memory (the state includes the accumulated impact, not just the current inventory).

    *Multiple assets*: Executing trades in multiple correlated assets introduces cross-impact (trading asset $i$ affects the price of asset $j$). The state space grows, and the impact matrix must be estimated, introducing additional estimation error.

    These extensions represent active research areas in market microstructure, and fully satisfactory solutions combining all realistic features remain open.

---

**Exercise 4.** Systemic risk modeling seeks to capture contagion effects through interbank networks. Describe the Eisenberg-Noe clearing model for a network of financial institutions and explain why the clearing vector is a fixed point. What makes computing the worst-case network topology an open problem?

??? success "Solution to Exercise 4"

    **Eisenberg-Noe Clearing Model and Network Topology**

    **The Clearing Model**

    Consider a network of $n$ financial institutions. Institution $i$ has:

    - External assets $e_i \geq 0$ (assets outside the network).
    - Liabilities $\bar{p}_i$ to other institutions (total obligations).
    - Relative liabilities $\pi_{ij} = L_{ij}/\bar{p}_i$, where $L_{ij}$ is the amount $i$ owes to $j$, and $\sum_j \pi_{ij} = 1$.

    The **clearing payment vector** $p^* = (p_1^*, \ldots, p_n^*)$ specifies what each institution actually pays. The key constraint is **limited liability**: institution $i$ can pay at most what it has:

    $$
    p_i^* = \min\left(\bar{p}_i, \; e_i + \sum_{j=1}^n \pi_{ji} p_j^*\right)
    $$

    The first argument $\bar{p}_i$ represents full payment of obligations. The second argument is the total available resources: external assets $e_i$ plus payments received from other institutions $\sum_j \pi_{ji} p_j^*$.

    **Why the Clearing Vector Is a Fixed Point**

    Define the map $\Phi: \mathbb{R}^n \to \mathbb{R}^n$ by:

    $$
    \Phi_i(p) = \min\left(\bar{p}_i, \; e_i + \sum_{j=1}^n \pi_{ji} p_j\right)
    $$

    The clearing vector $p^*$ satisfies $p^* = \Phi(p^*)$, i.e., it is a fixed point of $\Phi$. This is because the clearing condition is self-referential: what institution $i$ can pay depends on what it receives from others, which in turn depends on what those institutions can pay, which depends on what they receive, and so on.

    **Existence and Uniqueness (Eisenberg-Noe Theorem)**

    *Existence*: The map $\Phi$ maps the compact, convex set $[0, \bar{p}_1] \times \cdots \times [0, \bar{p}_n]$ into itself. Moreover, $\Phi$ is **monotone** (if $p \leq p'$ componentwise, then $\Phi(p) \leq \Phi(p')$) because higher payments from others mean more resources available. By Tarski's fixed-point theorem (or directly by iterating from the top $p = \bar{p}$), a greatest fixed point exists.

    *Uniqueness*: Under mild regularity conditions (the liability network is connected, or all institutions have positive external assets), the clearing vector is unique. The intuition is that the contraction-like property of $\Phi$ (each dollar received from others generates less than a dollar in payments, due to the min with $\bar{p}_i$) ensures convergence.

    *Algorithm*: The clearing vector can be computed by the "fictitious default algorithm":

    1. Start with $p^{(0)} = \bar{p}$ (everyone pays in full).
    2. Compute $p^{(k+1)} = \Phi(p^{(k)})$.
    3. Since $\Phi$ is monotone and $p^{(0)}$ is the maximum, the sequence $\{p^{(k)}\}$ is decreasing and converges to $p^*$ in at most $n$ iterations (each iteration can cause at most one new institution to default).

    **Why Worst-Case Network Topology Is an Open Problem**

    The problem of finding the network structure $(\pi_{ij})$ that maximizes systemic losses is challenging for several reasons:

    1. **Combinatorial complexity**: The space of possible network topologies is enormous. For $n$ institutions, the liability matrix has $O(n^2)$ entries, each of which can take a range of values. The optimization over this space is combinatorial and generally NP-hard.

    2. **Non-convexity**: The total systemic loss $L(\pi) = \sum_i (\bar{p}_i - p_i^*)$ is a non-convex function of the liability matrix $\pi$ because the clearing map involves min operations that create kinks and non-differentiability.

    3. **Endogeneity**: In reality, the network topology is not fixed --- it responds to institutions' strategic decisions. An institution that sees a risky counterparty will reduce its exposure, changing the network. Modeling this strategic interaction requires game-theoretic tools, and the resulting equilibrium network is hard to characterize.

    4. **Data limitations**: Real interbank networks are not fully observable. Regulators see bilateral exposures with limited granularity, and the structure of OTC derivative networks is particularly opaque. Inference of network structure from partial data is a statistical challenge.

    5. **Multiple contagion channels**: The Eisenberg-Noe model captures only direct default contagion through contractual obligations. In practice, contagion also operates through fire sales (institutions selling assets to meet obligations, depressing prices), funding liquidity (loss of confidence causing withdrawal of short-term funding), and information contagion (one institution's distress causing market-wide reassessment of risk). Incorporating all channels into a single optimization framework remains open.

---

**Exercise 5.** Deep hedging uses neural networks to learn hedging strategies directly from data. Discuss the theoretical challenges: (a) what function class does the neural network approximate, (b) how is the training loss related to a risk measure, and (c) why is explainability of the learned strategy a fundamental concern for regulators?

??? success "Solution to Exercise 5"

    **Theoretical Challenges of Deep Hedging**

    **(a) Function Class Approximated by the Neural Network**

    In the deep hedging framework, the hedge ratio at time $t$ is:

    $$
    \Delta_t = f_\theta(I_t)
    $$

    where $I_t$ is the information set (which may include the stock price $S_t$, variance $V_t$, time $t$, current portfolio value, and possibly path features) and $f_\theta$ is a neural network with parameters $\theta$.

    The neural network approximates a function from the information set to the action space (hedge ratios). By the universal approximation theorem, a sufficiently wide single-hidden-layer network can approximate any continuous function on a compact set to arbitrary accuracy. In practice, recurrent neural networks (RNNs/LSTMs) or temporal convolutional networks are used to capture path dependence, approximating functions of the form:

    $$
    \Delta_t = f_\theta(S_0, S_1, \ldots, S_t, V_0, V_1, \ldots, V_t, t)
    $$

    The theoretical function class is the set of all **adapted, caglad strategies** --- functions that depend on information available at time $t$ and are left-continuous. The neural network parameterizes a subset of this class. A key theoretical question is whether this parameterized subset is rich enough to contain or approximate the optimal strategy. For the universal approximation theorem to apply rigorously, one needs the optimal strategy to be continuous (or at least measurable) in its arguments, which may fail near option boundaries or at maturity.

    **(b) Training Loss and Risk Measures**

    The neural network is trained by minimizing:

    $$
    \min_\theta \; \rho\left(\text{P\&L}(\theta)\right)
    $$

    where $\rho$ is a risk measure applied to the hedging P&L:

    $$
    \text{P\&L}(\theta) = -H(S_T) + \sum_{t=0}^{N-1} \Delta_t(\theta) (S_{t+1} - S_t) + \text{option premium}
    $$

    Here $H(S_T)$ is the option payoff and the sum represents the gains from the hedging portfolio.

    Common choices for $\rho$:

    - **Mean-squared error**: $\rho(X) = \mathbb{E}[X^2]$. Corresponds to quadratic hedging (minimizing variance of hedging error). This has a well-developed theory (Follmer-Schweizer minimal martingale measure) and the optimal strategy is known analytically in some models.

    - **CVaR (Conditional Value at Risk)**: $\rho(X) = \text{CVaR}_\alpha(X) = \mathbb{E}[X | X \geq \text{VaR}_\alpha(X)]$. This focuses on the tail of the hedging loss distribution, penalizing catastrophic hedging failures more than variance does. It is a coherent risk measure in the sense of Artzner et al.

    - **Entropic risk measure**: $\rho(X) = \frac{1}{\gamma}\log \mathbb{E}[e^{\gamma X}]$, corresponding to exponential utility. This connects deep hedging to utility-based hedging in incomplete markets.

    The choice of risk measure determines the character of the learned strategy: variance-minimizing strategies may tolerate occasional large losses, while CVaR-minimizing strategies will sacrifice average performance to avoid tail losses.

    **(c) Explainability as a Regulatory Concern**

    Regulators require that financial institutions understand and can explain their risk management strategies. The concern with deep hedging is multifaceted:

    1. **No closed-form**: The hedge ratio is defined implicitly by the neural network weights. Unlike Black-Scholes delta $\Delta = \mathcal{N}(d_1)$, there is no formula that a human can inspect and understand.

    2. **Sensitivity to training data**: If the training data does not include crisis scenarios, the learned strategy may behave unpredictably during crises. Unlike a model-based strategy where we can analytically characterize behavior under extreme parameters, a neural network's extrapolation properties are unknown.

    3. **Regulatory validation**: Under SR 11-7, model validators must independently assess model assumptions and limitations. For a neural network, the "assumptions" are implicit in the training data and architecture, making independent assessment extremely difficult.

    4. **Accountability**: If a deep hedging strategy produces unexpected losses, it is difficult to determine *why*. Was it a data issue? An architecture issue? A fundamental limitation of the approach? This makes post-mortem analysis and corrective action challenging.

    5. **Gaming and adversarial inputs**: Neural networks can be sensitive to adversarial perturbations --- small changes in inputs that cause large changes in outputs. In a financial context, this could mean that small market movements trigger unexpectedly large changes in hedge ratios.

    Potential mitigations include using explainable AI techniques (SHAP, attention mechanisms), constraining the network architecture to enforce known properties (e.g., monotonicity of delta in the underlying price), and running the deep hedging strategy alongside a traditional model for comparison.

---

**Exercise 6.** Climate finance requires pricing assets over horizons of 30-100 years under deep uncertainty about climate scenarios. Explain why standard discounted cash flow models are inadequate and discuss the role of ambiguity-averse preferences (e.g., maxmin expected utility) in pricing climate risk. What is the "fat tail" problem in climate risk modeling, and how does it relate to Knightian uncertainty?

??? success "Solution to Exercise 6"

    **Climate Finance: Inadequacy of Standard DCF and the Role of Ambiguity Aversion**

    **Why Standard Discounted Cash Flow Is Inadequate**

    Standard DCF pricing computes the present value of future cash flows $C_t$ as:

    $$
    V_0 = \sum_{t=1}^{T} \frac{\mathbb{E}[C_t]}{(1+r)^t}
    $$

    This framework fails for climate risk pricing for several reasons:

    1. **Discount rate sensitivity over long horizons**: For a 50-year cash flow, the discount factor at $r = 5\%$ is $(1.05)^{-50} \approx 0.087$, while at $r = 2\%$ it is $(1.02)^{-50} \approx 0.372$. The present value changes by a factor of 4 depending on the discount rate. For climate-relevant horizons (50--100 years), the choice of discount rate dominates the valuation, but there is no consensus on the appropriate rate for such horizons (the Stern-Nordhaus debate centers precisely on this).

    2. **Non-stationarity**: Standard DCF assumes a stationary economic environment where the discount rate and cash flow distributions are stable. Climate change introduces fundamental non-stationarity: the probability distributions of weather events, sea levels, agricultural yields, and energy costs are all shifting over time in ways that depend on policy choices not yet made.

    3. **Deep uncertainty about probability distributions**: Standard DCF requires specifying $\mathbb{E}[C_t]$, which presupposes a known probability distribution over climate outcomes. In practice, climate models produce a wide range of scenarios (from modest warming to catastrophic tipping points), and the probabilities assigned to these scenarios are themselves highly uncertain.

    4. **Tail risk and irreversibility**: Climate outcomes include potential catastrophic scenarios (collapse of ice sheets, permafrost methane release, ecosystem collapse) that are irreversible. Standard DCF treats these as low-probability events with finite expected cost, but the expected value may be dominated by rare catastrophic outcomes whose probabilities are poorly known.

    **Ambiguity-Averse Preferences: Maxmin Expected Utility**

    When probability distributions are themselves uncertain (ambiguity or Knightian uncertainty), the standard expected utility framework is inadequate. The maxmin expected utility (MEU) framework of Gilboa and Schmeidler replaces the single probability measure $\mathbb{P}$ with a set of plausible measures $\mathcal{P}$:

    $$
    V_0 = \min_{\mathbb{P} \in \mathcal{P}} \mathbb{E}^{\mathbb{P}}\left[\sum_{t=1}^T \frac{U(C_t)}{(1+r)^t}\right]
    $$

    The agent evaluates each decision under the *worst-case* probability distribution in $\mathcal{P}$. This leads to:

    - **Higher implicit discount for climate-exposed assets**: If the set $\mathcal{P}$ includes scenarios with severe climate damage, the worst-case valuation assigns higher probability to adverse outcomes, reducing asset values.
    - **Precautionary behavior**: The agent is willing to pay more for climate mitigation or adaptation because the worst-case scenario is very bad.
    - **Dynamic consistency**: Under smooth ambiguity preferences (Klibanoff, Marinacci, Mukerji), the agent's beliefs are updated consistently over time using a second-order expected utility:

    $$
    V_0 = \int \phi\left(\mathbb{E}^{\mathbb{P}_\theta}\left[\sum_t \frac{U(C_t)}{(1+r)^t}\right]\right) d\mu(\theta)
    $$

    where $\theta$ indexes climate models, $\mu$ is a prior over models, and $\phi$ is a concave function capturing ambiguity aversion. When $\phi$ is linear, this reduces to standard Bayesian expected utility. When $\phi$ is strictly concave, the agent places extra weight on pessimistic models.

    **The Fat Tail Problem and Knightian Uncertainty**

    The "fat tail" problem in climate risk refers to the observation (Weitzman, 2009) that:

    1. Climate sensitivity (the temperature increase from doubling CO2) has a distribution with a fat right tail. There is non-negligible probability of extreme warming (e.g., 6--10 degrees Celsius).

    2. The economic damage function $D(T)$ relating temperature increase $T$ to economic loss is likely convex and possibly catastrophic at high temperatures.

    3. The combination of a fat-tailed temperature distribution and a convex damage function means that the expected damage $\mathbb{E}[D(T)]$ may be **infinite** or dominated by catastrophic scenarios:

    $$
    \mathbb{E}[D(T)] = \int_0^{\infty} D(T) f(T)\, dT
    $$

    If $D(T)$ grows faster than the tail of $f(T)$ decays, this integral diverges (Weitzman's "dismal theorem").

    This connects to **Knightian uncertainty** because:

    - The probability of extreme climate outcomes is not reliably estimable from historical data (no precedent for current CO2 levels in human history).
    - Different climate models give very different tail probabilities; there is no consensus distribution.
    - The very concept of assigning a probability to, say, "global temperature increase exceeds 6 degrees by 2100" is fraught with model uncertainty.

    In this setting, standard risk pricing (which requires a known probability distribution) breaks down. Ambiguity-averse frameworks provide a principled approach: rather than pretending to know the probability of catastrophe, acknowledge the uncertainty and price assets conservatively by considering the range of plausible scenarios. This leads to climate risk premiums that are larger than those implied by any single "best-estimate" model, reflecting the genuine uncertainty about the most consequential outcomes.
