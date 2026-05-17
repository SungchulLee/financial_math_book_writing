# Model-Free Bounds


## Introduction


Model-free bounds represent a fundamental approach to derivative pricing that does not rely on specific assumptions about the underlying asset's dynamics. Instead, these bounds are derived purely from no-arbitrage principles and observable market prices, making them robust to model misspecification.

The theory of model-free bounds addresses the question: **What can we say about derivative prices using only no-arbitrage and observed option prices, without specifying a stochastic process?**

This approach is particularly valuable because:

1. It provides rigorous bounds that must hold regardless of the true underlying model
2. It identifies which information is truly necessary for pricing
3. It reveals when the market provides sufficient constraints to pin down unique prices
4. It offers model-independent hedging strategies

## Mathematical Framework


### 1. Market Setup


**Traded Assets**: Consider a frictionless market with:

- A riskless asset (bond) with price $B_t = e^{rt}$
- A risky asset (stock) with price process $S_t$
- European options with various strikes and maturities

**No-Arbitrage Assumption**: There exists no trading strategy that requires no initial investment, has non-negative payoff with probability 1, and has positive payoff with positive probability.

**Recall** (see [§ Fundamental Theorem of Asset Pricing](../../ch01/fundamental_theorem_of_asset_pricing/fundamental_theorem_of_asset_pricing.md)): under no-arbitrage there exists an equivalent measure $\mathbb{Q}$ such that the discounted price $\tilde{S}_t = S_t/B_t$ is a $\mathbb{Q}$-martingale,


$$
\frac{S_t}{B_t} = \mathbb{E}_{\mathbb{Q}}\left[ \frac{S_T}{B_T} \,\bigg|\, \mathcal{F}_t \right]
$$



### 2. Model-Free Setting


**Given Information**:

- Current stock price $S_0$
- Risk-free rate $r$
- Maturity $T$
- Prices of European calls $C(K)$ for various strikes $K$

**Unknown**: The specific dynamics of $S_t$ or equivalently, the probability measure $\mathbb{Q}$.

**Goal**: Derive bounds on prices of exotic derivatives using only no-arbitrage and observed vanilla option prices.

## Static Arbitrage Bounds


### 1. Call Option Bounds


**Intrinsic Value Bound** (Lower Bound):


$$
C(K, T) \geq (S_0 - Ke^{-rT})^+
$$



**Proof**: Consider the portfolio:

- Long one call with strike $K$
- Short one stock
- Long $Ke^{-rT}$ in bonds

At maturity:

- If $S_T > K$: Portfolio value = $(S_T - K) - S_T + K = 0$
- If $S_T \leq K$: Portfolio value = $0 - S_T + K \geq 0$

The portfolio has non-negative payoff, so by no-arbitrage, its initial value must be non-negative:


$$
C(K, T) - S_0 + Ke^{-rT} \geq 0
$$



**Upper Bound**:


$$
C(K, T) \leq S_0
$$



**Proof**: A call option cannot be worth more than the underlying stock itself. If $C(K, T) > S_0$, sell the call and buy the stock for arbitrage.

### 2. Put Option Bounds


**Lower Bound**:


$$
P(K, T) \geq (Ke^{-rT} - S_0)^+
$$



**Upper Bound**:


$$
P(K, T) \leq Ke^{-rT}
$$



**Proof**: A put option cannot be worth more than the present value of the strike. If $P(K, T) > Ke^{-rT}$, sell the put and invest the proceeds for arbitrage.

### 3. Put-Call Parity


**Exact Relationship**:


$$
C(K, T) - P(K, T) = S_0 - Ke^{-rT}
$$



**Proof**: Consider two portfolios:

- Portfolio A: One call + $Ke^{-rT}$ in bonds
- Portfolio B: One put + One stock

At maturity $T$:

- If $S_T > K$: Portfolio A = $(S_T - K) + K = S_T$, Portfolio B = $0 + S_T = S_T$
- If $S_T \leq K$: Portfolio A = $0 + K = K$, Portfolio B = $(K - S_T) + S_T = K$

Since both portfolios have identical payoffs, by no-arbitrage, they must have identical prices today.

## Convexity and Monotonicity Constraints


### 1. Convexity in Strike


**Theorem** (Convexity): The call price $C(K)$ is a convex function of the strike $K$:


$$
C(\lambda K_1 + (1-\lambda) K_2) \leq \lambda C(K_1) + (1-\lambda) C(K_2)
$$



for all $K_1 < K_2$ and $\lambda \in [0, 1]$.

**Proof**: For any $K_1 < K_2 < K_3$ with $K_2 = \alpha K_1 + (1-\alpha) K_3$, consider the butterfly spread:

- Long 1 call at $K_1$
- Long 1 call at $K_3$
- Short $\frac{K_3 - K_1}{K_2 - K_1} = \frac{1}{\alpha}$ calls at $K_2$

This portfolio has non-negative payoff everywhere, hence:


$$
C(K_1) + C(K_3) - \frac{1}{\alpha} C(K_2) \geq 0
$$



which establishes convexity.

**Consequence**: The call price function must satisfy:


$$
\frac{C(K_2) - C(K_1)}{K_2 - K_1} \leq \frac{C(K_3) - C(K_2)}{K_3 - K_2}
$$



for any $K_1 < K_2 < K_3$.

### 2. Monotonicity


**Theorem** (Decreasing in Strike): Call prices are decreasing in strike:


$$
K_1 < K_2 \implies C(K_1) \geq C(K_2)
$$



**Proof**: The payoff $(S_T - K_1)^+ \geq (S_T - K_2)^+$ for all $S_T$ when $K_1 < K_2$. By no-arbitrage, $C(K_1) \geq C(K_2)$.

**Call Spread Bound**: For $K_1 < K_2$:


$$
0 \leq C(K_1) - C(K_2) \leq e^{-rT}(K_2 - K_1)
$$



**Proof**: 

- Lower bound: From monotonicity
- Upper bound: The maximum payoff of a call spread is $K_2 - K_1$, so its present value is at most $e^{-rT}(K_2 - K_1)$

### 3. Slope Constraints


**Theorem**: The call price function satisfies:


$$
-e^{-rT} \leq \frac{\partial C}{\partial K} \leq 0
$$



**Proof**: 

- Upper bound: Monotonicity (decreasing function)
- Lower bound: From call spread bound, taking limits:

  $$
  \frac{C(K) - C(K + h)}{h} \leq e^{-rT}
  $$


  
As $h \to 0$:

  $$
  -\frac{\partial C}{\partial K} \leq e^{-rT}
  $$



**Digital Option Connection**: Define the **digital call**:


$$
\mathcal{D}(K) = e^{rT} \frac{\partial C}{\partial K}(K)
$$



Then:

$$
\mathcal{D}(K) = -\mathbb{Q}(S_T > K)
$$



and the constraint becomes:

$$
0 \leq \mathbb{Q}(S_T > K) \leq 1
$$



## Breeden-Litzenberger Formula

**Recall** (see [§ Model-Free Results](../../ch12/model_free_results/breeden_litzenberger_formula.md)): the risk-neutral density satisfies $q(K) = e^{rT} \partial^2 C / \partial K^2 (K)$, with discrete approximation $q(K_i) \approx e^{rT}[C(K_{i-1}) - 2C(K_i) + C(K_{i+1})]/(\Delta K)^2$. Convexity of $C(K)$ ensures $q \geq 0$, and the forward $F_0 = \int K q(K) dK = S_0 e^{rT}$.

## Carr-Madan Formula


### 1. Derivative Payoff Decomposition


**Theorem** (Carr-Madan, 1998): Any twice-differentiable payoff $g(S_T)$ can be decomposed as:


$$
g(S_T) = g(F) + g'(F)(S_T - F) + \int_0^F g''(K) (K - S_T)^+ \, dK + \int_F^{\infty} g''(K) (S_T - K)^+ \, dK
$$



where $F = S_0 e^{rT}$ is the forward price.

**Proof**: Integration by parts applied twice. Start with:


$$
g(S_T) - g(F) = \int_F^{S_T} g'(K) \, dK
$$



Apply integration by parts:


$$
\int_F^{S_T} g'(K) \, dK = g'(K)(K - F)\bigg|_F^{S_T} - \int_F^{S_T} (K - F) g''(K) \, dK
$$



Continuing and rearranging terms yields the result.

**Pricing Formula**: Taking expectations under $\mathbb{Q}$:


$$
\begin{aligned}
V_0 &= e^{-rT} \mathbb{E}_{\mathbb{Q}}[g(S_T)] \\
&= e^{-rT} g(F) + e^{-rT} \int_0^F g''(K) P(K) \, dK + e^{-rT} \int_F^{\infty} g''(K) C(K) \, dK
\end{aligned}
$$



**Interpretation**: 

- Any derivative can be priced using puts below the forward and calls above the forward
- The weights are given by the second derivative of the payoff function
- This is a **static replication strategy**

### 2. Applications


**Variance Swap**: For the log-contract $g(S_T) = \log(S_T/F)$:


$$
g''(K) = \frac{1}{K^2}
$$



Hence:


$$
\mathbb{E}_{\mathbb{Q}}[\log(S_T/F)] = \int_0^F \frac{P(K)}{K^2} \, dK + \int_F^{\infty} \frac{C(K)}{K^2} \, dK
$$



**Realized Variance**: Under certain conditions:


$$
\text{Var}(S_T) \approx 2e^{rT} \left( \int_0^F \frac{P(K)}{K^2} \, dK + \int_F^{\infty} \frac{C(K)}{K^2} \, dK \right)
$$



**VIX Construction**: The CBOE VIX index uses this formula to compute model-free implied variance.

## Model-Free Bounds on Path-Dependent Options


### 1. Forward Start Options


**Definition**: A forward start call option struck at-the-money at time $t_1$ with maturity $t_2$:


$$
\text{Payoff} = (S_{t_2} - S_{t_1})^+
$$



**Model-Free Bound**: Using only vanilla options:


$$
\begin{aligned}
V_0^{\text{forward}} &\leq C_0(S_0, t_2) \\
V_0^{\text{forward}} &\geq (1 - e^{-r t_1}) C_0(S_0, t_2)
\end{aligned}
$$



**Proof** (Upper Bound): The forward start option is dominated by a standard call option with the same maturity.

**Proof** (Lower Bound): More subtle, requires constructing sub-replicating portfolio using European options.

### 2. Lookback Options


**Fixed Strike Lookback Call**: Payoff is:


$$
\left(\max_{0 \leq t \leq T} S_t - K\right)^+
$$



**Model-Free Bound**: 


$$
C_{\text{lookback}}(K) \geq C_{\text{European}}(K)
$$



with equality only if volatility is zero.

**Tighter Bound**: Using convexity:


$$
C_{\text{lookback}}(K) \geq \int_K^{\infty} \frac{C(L)}{L^2} \, dL
$$



This bound can be computed from the market prices of vanilla calls.

### 3. Barrier Options


**Up-and-Out Call**: Payoff is:


$$
(S_T - K)^+ \mathbb{1}_{\{\max_{0 \leq t \leq T} S_t < H\}}
$$



where $H > S_0$ is the barrier level.

**Model-Free Bounds**: Let $C_{\text{UO}}$ denote the up-and-out call price.

**Lower Bound**:


$$
C_{\text{UO}}(K, H) \geq 0
$$



**Upper Bound**:


$$
C_{\text{UO}}(K, H) \leq C(K) - C(H)
$$



**Proof**: The up-and-out call pays $(S_T - K)^+$ only when $S_T < H$. This is less valuable than a call spread $(S_T - K)^+ - (S_T - H)^+$.

**Static Replication** (Under Specific Models): For certain models (e.g., Black-Scholes with constant volatility), exact static replication is possible using vanilla options. However, **model-free** exact replication is generally not possible for barrier options.

## Fundamental Duality

**Recall** (see [§ Superhedging Duality](superhedging_duality.md)): the super-replication cost $\pi^{\text{sup}}(g) = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} g(S_T)]$ and the sub-replication cost $\pi^{\text{sub}}(g) = \inf_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} g(S_T)]$, with strict inequality $\pi^{\text{sub}} < \pi^{\text{sup}}$ in incomplete markets and equality in complete markets.

## Advanced Model-Free Results


### 1. Variance Bounds


**Model-Free Implied Variance**: Define:


$$
\sigma_{\text{MF}}^2 = \frac{2e^{rT}}{T} \left( \int_0^{S_0} \frac{P(K)}{K^2} \, dK + \int_{S_0}^{\infty} \frac{C(K)}{K^2} \, dK \right)
$$



**Theorem** (Carr-Madan): This quantity satisfies:


$$
\sigma_{\text{MF}}^2 = \frac{1}{T} \mathbb{E}_{\mathbb{Q}}\left[ \int_0^T \frac{\sigma_t^2}{1} \, dt \right] - \frac{1}{T} \left[ \log\left(\frac{S_T}{S_0}\right) \right]^2
$$



where $\sigma_t$ is the instantaneous volatility.

**Implication**: $\sigma_{\text{MF}}^2$ provides a lower bound on the expected realized variance:


$$
\sigma_{\text{MF}}^2 \leq \frac{1}{T} \mathbb{E}_{\mathbb{Q}}\left[ \int_0^T \sigma_t^2 \, dt \right]
$$



### 2. Moment Constraints


**European Option Prices** constrain the moments of the risk-neutral distribution.

**Theorem**: Given call prices $\{C(K_i)\}_{i=1}^n$, the risk-neutral distribution $q(S)$ must satisfy:


$$
\int_0^{\infty} S^k q(S) \, dS = m_k
$$



for $k = 0, 1, 2, \ldots$, where:


$$
m_0 = 1, \quad m_1 = S_0 e^{rT}
$$



and higher moments can be computed from option prices using:


$$
m_k = e^{rT} \left[ k(k-1) \int_0^{\infty} K^{k-2} C(K) \, dK + \text{boundary terms} \right]
$$



**Application**: These moment constraints can be used to derive bounds on exotic options by optimization over distributions satisfying the constraints.

## Robust Pricing with Traded Options


### 1. Constrained Martingale Measures


**Setup**: Suppose European calls $\{C(K_i)\}_{i=1}^n$ are traded with observed prices.

**Martingale Constraint Set**: Define:


$$
\mathcal{M}_{\text{market}} = \left\{ \mathbb{Q} \in \mathcal{M}: \mathbb{E}_{\mathbb{Q}}[e^{-rT}(S_T - K_i)^+] = C(K_i), \, i = 1, \ldots, n \right\}
$$



**Robust Pricing**: For an exotic derivative with payoff $g(S_T)$:


$$
[\underline{V}, \overline{V}] = \left[ \inf_{\mathbb{Q} \in \mathcal{M}_{\text{market}}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} g(S_T)], \, \sup_{\mathbb{Q} \in \mathcal{M}_{\text{market}}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} g(S_T)] \right]
$$



**Interpretation**: The robust price interval $[\underline{V}, \overline{V}]$ contains all prices consistent with no-arbitrage and observed vanilla option prices.

### 2. Optimization Formulation


**Dual Problem**: The robust bounds can be computed by solving:


$$
\overline{V} = \sup_q \left\{ \int_0^{\infty} g(S) q(S) \, dS \right\}
$$



subject to:

1. $q(S) \geq 0$ for all $S$
2. $\int_0^{\infty} q(S) \, dS = e^{-rT}$
3. $\int_0^{\infty} S q(S) \, dS = S_0$
4. $\int_0^{\infty} (S - K_i)^+ q(S) \, dS = C(K_i)$ for $i = 1, \ldots, n$

This is a **linear programming** problem in infinite dimensions.

**Discretization**: Approximate by discretizing the state space:


$$
S \in \{S_1, S_2, \ldots, S_M\}
$$



Then solve a finite-dimensional LP with variables $q_j = q(S_j)$.

### 3. Extremal Measures


**Theorem**: The extremal measures (achieving the supremum or infimum) are typically **discrete** with support on at most $n+2$ points, where $n$ is the number of traded strikes.

**Proof Sketch**: By linear programming duality, the optimal solution has at most as many support points as constraints.

**Implication**: The worst-case or best-case scenario for pricing corresponds to a discrete probability distribution, concentrating mass on a few states.

## Applications and Examples


### 1. Example 1: Digital Option Bounds


**Payoff**: Binary option that pays $1$ if $S_T > K$, zero otherwise.

**Given**: Prices of European calls $C(K_1)$ and $C(K_2)$ with $K_1 < K < K_2$.

**Model-Free Bound**: By convexity:


$$
\frac{C(K_1) - C(K)}{K - K_1} \geq \frac{C(K) - C(K_2)}{K_2 - K}
$$



Rearranging:


$$
C(K) \leq \frac{(K_2 - K) C(K_1) + (K - K_1) C(K_2)}{K_2 - K_1}
$$



For the digital option:


$$
\mathcal{D}(K) = \lim_{h \to 0} \frac{C(K) - C(K+h)}{h}
$$



Bounds can be derived using finite differences of observed call prices.

### 2. Example 2: Variance Swap Replication


**Variance Swap Payoff**: Pays the realized variance:


$$
\text{Payoff} = \frac{1}{T} \sum_{i=1}^N \left( \log \frac{S_{t_i}}{S_{t_{i-1}}} \right)^2
$$



**Model-Free Replication**: Using the log-contract:


$$
\mathbb{E}_{\mathbb{Q}}\left[ \log \frac{S_T}{S_0} \right] = e^{-rT} \left( \int_0^{S_0} \frac{P(K)}{K^2} \, dK + \int_{S_0}^{\infty} \frac{C(K)}{K^2} \, dK \right)
$$



The variance can be replicated (approximately) by a portfolio of puts and calls.

### 3. Example 3: Asian Option Bounds


**Arithmetic Asian Call**: Payoff is:


$$
\left( \frac{1}{N} \sum_{i=1}^N S_{t_i} - K \right)^+
$$



**Model-Free Bound** (Using Jensen's Inequality):


$$
C_{\text{Asian}}(K) \leq C_{\text{European}}(K)
$$



since:


$$
\left( \frac{1}{N} \sum_{i=1}^N S_{t_i} - K \right)^+ \leq \frac{1}{N} \sum_{i=1}^N (S_{t_i} - K)^+
$$



**Tighter Bounds**: Can be derived using moment constraints and optimization over distributions.

## Computational Methods


### 1. Linear Programming Approach


**Discretization**: Choose a grid $\{S_j\}_{j=1}^M$ and discretize the density:


$$
q_j = q(S_j) \Delta S_j
$$



**LP Formulation**:


$$
\begin{aligned}
\text{maximize} \quad & \sum_{j=1}^M g(S_j) q_j \\
\text{subject to} \quad & \sum_{j=1}^M q_j = e^{-rT} \\
& \sum_{j=1}^M S_j q_j = S_0 \\
& \sum_{j=1}^M (S_j - K_i)^+ q_j = C(K_i), \quad i = 1, \ldots, n \\
& q_j \geq 0, \quad j = 1, \ldots, M
\end{aligned}
$$



**Sensitivity**: Solutions are sensitive to grid choice and number of points $M$. Use adaptive grids for better accuracy.

### 2. Semidefinite Programming


**Moment-Based Approach**: Instead of discretizing states, work directly with moments.

**Variables**: Moments $\mu_k = \mathbb{E}_{\mathbb{Q}}[S_T^k]$ for $k = 0, 1, 2, \ldots, K$.

**Constraints**:

1. Moment sequence corresponds to a valid probability measure (positive semi-definiteness)
2. Martingale constraint: $\mu_1 = S_0 e^{rT}$
3. Option pricing constraints from Breeden-Litzenberger

**SDP Formulation**: The positivity constraint can be expressed as:


$$
M = \begin{pmatrix}
\mu_0 & \mu_1 & \cdots & \mu_K \\
\mu_1 & \mu_2 & \cdots & \mu_{K+1} \\
\vdots & \vdots & \ddots & \vdots \\
\mu_K & \mu_{K+1} & \cdots & \mu_{2K}
\end{pmatrix} \succeq 0
$$



**Objective**: Compute expectation $\mathbb{E}_{\mathbb{Q}}[g(S_T)]$ as a function of moments.

### 3. Monte Carlo Methods


**Scenario Generation**: Generate scenarios $\{S_T^{(i)}\}_{i=1}^N$ from a reference distribution.

**Importance Weights**: Assign weights $\{w_i\}_{i=1}^N$ to match market prices:


$$
\sum_{i=1}^N w_i (S_T^{(i)} - K_j)^+ = C(K_j), \quad j = 1, \ldots, n
$$



**Entropy Minimization**: Choose weights to minimize relative entropy:


$$
\min_w \sum_{i=1}^N w_i \log w_i
$$



subject to pricing constraints.

**Solution**: Exponential tilting:


$$
w_i^* = \frac{\exp(-\lambda^\top g(S_T^{(i)}))}{\sum_{j=1}^N \exp(-\lambda^\top g(S_T^{(j)}))}
$$



where $\lambda$ is chosen to match constraints.

## Limitations and Extensions


### 1. Model-Free Bound Limitations


**Width of Bounds**: For many exotic derivatives, model-free bounds are **wide** – the interval $[\underline{V}, \overline{V}]$ can be large.

**Information Insufficiency**: Vanilla option prices alone may not provide tight bounds for:

- Strongly path-dependent options (e.g., lookbacks, barriers)
- Multi-asset derivatives
- Options sensitive to volatility dynamics

**Example**: For an up-and-out call, the bounds can be:


$$
0 \leq C_{\text{UO}} \leq C(K)
$$



which is not very informative.

### 2. Additional Market Information


**Volatility Surface**: Incorporating options at multiple maturities:


$$
\{C(K, T_i): i = 1, \ldots, M\}
$$



tightens bounds significantly for path-dependent options.

**Co-monotonicity**: Assuming monotonicity relationships between prices at different times can further tighten bounds.

**Dividend Information**: Knowledge of dividend payments $\{d_i, t_i\}$ modifies the martingale constraint.

### 3. Extensions to Multiple Assets


**Basket Options**: Payoff depends on multiple underlyings:


$$
g(S_T^{(1)}, S_T^{(2)}, \ldots, S_T^{(n)})
$$



**Marginal Constraints**: Given marginal option prices for each asset:


$$
\{C_i(K): K \geq 0, i = 1, \ldots, n\}
$$



**Robust Pricing**: Optimize over joint distributions with specified marginals:


$$
\sup_{\mathbb{Q}} \mathbb{E}_{\mathbb{Q}}[g(S_T^{(1)}, \ldots, S_T^{(n)})]
$$



subject to marginal constraints.

**Fréchet-Hoeffding Bounds**: Provide bounds based solely on marginals without correlation information.

## Summary and Key Insights


### 1. Fundamental Principles


1. **No-Arbitrage Foundation**: Model-free bounds rely purely on the absence of arbitrage, not on specific dynamical assumptions.

2. **Static Replication**: Many derivatives can be replicated using portfolios of vanilla options, enabling model-independent pricing.

3. **Duality**: Super-replication costs equal supremum over martingale measures; sub-replication costs equal infimum.

4. **Convexity**: The call price function's convexity in strike ensures non-negative risk-neutral densities and provides structural constraints.

5. **Information Content**: Vanilla option prices encode the risk-neutral distribution, accessible via the Breeden-Litzenberger formula.

### 2. Practical Implications


**For Traders**:

- Model-free bounds provide arbitrage-free price ranges
- Observed market prices outside these bounds indicate arbitrage opportunities (after transaction costs)

**For Risk Managers**:

- Robust bounds quantify model uncertainty
- Worst-case scenarios guide capital allocation

**For Researchers**:

- Model-free results identify which features are truly necessary for pricing
- Gaps between model-free bounds and model-specific prices reveal model-dependent risk premiums

### 3. Open Questions


1. **Tightness**: How to tighten bounds for exotic derivatives using limited additional information?

2. **Dynamic Bounds**: Extending model-free theory to multi-period settings with intermediate hedging.

3. **Computational Efficiency**: Faster algorithms for high-dimensional robust pricing problems.

4. **Market Microstructure**: Incorporating realistic frictions (bid-ask spreads, discrete strikes) into model-free theory.

Model-free bounds represent a cornerstone of robust derivative pricing, providing rigorous constraints that must hold regardless of modeling assumptions. This theory bridges classical arbitrage pricing with modern robust optimization, offering both theoretical insights and practical tools for quantitative finance.

---

## Exercises

**Exercise 1.** Consider a stock with current price $S_0 = 100$, risk-free rate $r = 0$, and maturity $T = 1$. European call prices are observed at strikes $K = 90, 100, 110$ with prices $C(90) = 14$, $C(100) = 8$, and $C(110) = 4$. Verify that these prices satisfy the convexity constraint, and compute the discrete approximation to the risk-neutral density $q(K)$ at $K = 100$ using the Breeden-Litzenberger formula.

??? success "Solution to Exercise 1"

    **Convexity check.** For strikes $K_1 = 90 < K_2 = 100 < K_3 = 110$ with prices $C(90) = 14$, $C(100) = 8$, $C(110) = 4$, the convexity (butterfly) condition requires:

    $$
    C(K_2) \leq \frac{K_3 - K_2}{K_3 - K_1} C(K_1) + \frac{K_2 - K_1}{K_3 - K_1} C(K_3)
    $$

    With $K_2 - K_1 = K_3 - K_2 = 10$, so $\lambda = \frac{K_3 - K_2}{K_3 - K_1} = \frac{1}{2}$:

    $$
    \frac{1}{2}C(90) + \frac{1}{2}C(110) = \frac{1}{2}(14) + \frac{1}{2}(4) = 9
    $$

    Since $C(100) = 8 \leq 9$, the convexity constraint is satisfied. $\checkmark$

    We can also check monotonicity: $C(90) = 14 > C(100) = 8 > C(110) = 4$. $\checkmark$

    And the slope bounds: $\frac{C(90) - C(100)}{100 - 90} = \frac{6}{10} = 0.6 \leq e^{-rT} = 1$. $\checkmark$

    **Breeden-Litzenberger density.** With $r = 0$, the discrete approximation is:

    $$
    q(K_i) \approx e^{rT} \frac{C(K_{i-1}) - 2C(K_i) + C(K_{i+1})}{(\Delta K)^2}
    $$

    At $K = 100$ with $\Delta K = 10$:

    $$
    q(100) \approx 1 \cdot \frac{C(90) - 2C(100) + C(110)}{(10)^2} = \frac{14 - 16 + 4}{100} = \frac{2}{100} = 0.02
    $$

    This means the risk-neutral density at $S_T = 100$ is approximately $q(100) = 0.02$ per unit of $S_T$. For an interval of width $\Delta K = 10$ centered at 100, the probability mass is approximately $0.02 \times 10 = 0.20$, meaning there is roughly a 20% risk-neutral probability of the stock being near 100 at maturity.

---

**Exercise 2.** Prove that put option prices $P(K)$ are convex in the strike $K$. That is, for $K_1 < K_2 < K_3$ with $K_2 = \lambda K_1 + (1 - \lambda) K_3$, show that

$$
P(K_2) \leq \lambda P(K_1) + (1 - \lambda) P(K_3)
$$

using a no-arbitrage argument based on butterfly spreads with puts.

??? success "Solution to Exercise 2"

    **Proof of put convexity via butterfly spreads.**

    Let $K_1 < K_2 < K_3$ with $K_2 = \lambda K_1 + (1 - \lambda) K_3$ where $\lambda = \frac{K_3 - K_2}{K_3 - K_1}$.

    Consider the **put butterfly spread**: long $\lambda$ puts at $K_1$, short 1 put at $K_2$, long $(1 - \lambda)$ puts at $K_3$. The terminal payoff is:

    $$
    \Pi(S_T) = \lambda(K_1 - S_T)^+ - (K_2 - S_T)^+ + (1 - \lambda)(K_3 - S_T)^+
    $$

    We verify this is non-negative in each region:

    *Case 1: $S_T \geq K_3$.* All puts expire worthless: $\Pi = 0 \geq 0$.

    *Case 2: $K_2 \leq S_T < K_3$.* Only the $K_3$ put is in the money:

    $$
    \Pi = 0 - 0 + (1 - \lambda)(K_3 - S_T) = (1 - \lambda)(K_3 - S_T) \geq 0
    $$

    *Case 3: $K_1 \leq S_T < K_2$.* The $K_2$ and $K_3$ puts are in the money:

    $$
    \Pi = 0 - (K_2 - S_T) + (1 - \lambda)(K_3 - S_T)
    $$

    $$
    = -K_2 + S_T + (1 - \lambda)K_3 - (1 - \lambda)S_T = -K_2 + \lambda S_T + (1 - \lambda)K_3
    $$

    Since $K_2 = \lambda K_1 + (1 - \lambda)K_3$:

    $$
    \Pi = -\lambda K_1 - (1 - \lambda)K_3 + \lambda S_T + (1 - \lambda)K_3 = \lambda(S_T - K_1) \geq 0
    $$

    because $S_T \geq K_1$.

    *Case 4: $S_T < K_1$.* All puts are in the money:

    $$
    \Pi = \lambda(K_1 - S_T) - (K_2 - S_T) + (1 - \lambda)(K_3 - S_T)
    $$

    $$
    = \lambda K_1 - K_2 + (1 - \lambda)K_3 + S_T(-\lambda + 1 - 1 + \lambda) = \lambda K_1 - K_2 + (1 - \lambda)K_3 = 0
    $$

    Since the butterfly has non-negative payoff everywhere, by no-arbitrage its initial cost must be non-negative:

    $$
    \lambda P(K_1) - P(K_2) + (1 - \lambda) P(K_3) \geq 0
    $$

    This gives $P(K_2) \leq \lambda P(K_1) + (1 - \lambda) P(K_3)$, establishing convexity. $\square$

---

**Exercise 3.** Using the Carr-Madan decomposition, express the price of a power payoff $g(S_T) = S_T^2$ in terms of European call and put prices. Compute $g''(K)$ and write out the resulting integral formula explicitly.

??? success "Solution to Exercise 3"

    **Carr-Madan decomposition for $g(S_T) = S_T^2$.**

    The general Carr-Madan formula with pivot $F = S_0 e^{rT}$ is:

    $$
    g(S_T) = g(F) + g'(F)(S_T - F) + \int_0^F g''(K)(K - S_T)^+ \, dK + \int_F^\infty g''(K)(S_T - K)^+ \, dK
    $$

    For $g(S_T) = S_T^2$, we compute:

    $$
    g'(S_T) = 2S_T, \quad g''(S_T) = 2
    $$

    Substituting:

    $$
    S_T^2 = F^2 + 2F(S_T - F) + \int_0^F 2(K - S_T)^+ \, dK + \int_F^\infty 2(S_T - K)^+ \, dK
    $$

    $$
    = F^2 + 2F(S_T - F) + 2\int_0^F (K - S_T)^+ \, dK + 2\int_F^\infty (S_T - K)^+ \, dK
    $$

    Taking expectations under $\mathbb{Q}$ and discounting (noting $\mathbb{E}_\mathbb{Q}[S_T - F] = 0$ by the martingale property):

    $$
    \mathbb{E}_\mathbb{Q}[e^{-rT} S_T^2] = e^{-rT} F^2 + 2\int_0^F P(K) \, dK + 2\int_F^\infty C(K) \, dK
    $$

    where $P(K) = e^{-rT}\mathbb{E}_\mathbb{Q}[(K - S_T)^+]$ and $C(K) = e^{-rT}\mathbb{E}_\mathbb{Q}[(S_T - K)^+]$ are put and call prices.

    Therefore the price of the power payoff is:

    $$
    V_0 = e^{-rT} S_0^2 e^{2rT} + 2\int_0^F P(K) \, dK + 2\int_F^\infty C(K) \, dK
    $$

    $$
    = S_0^2 e^{rT} + 2\int_0^F P(K) \, dK + 2\int_F^\infty C(K) \, dK
    $$

    The weight $g''(K) = 2$ is constant, so the power payoff is replicated by a constant portfolio density of puts (below the forward) and calls (above the forward), plus a position in the forward contract.

---

**Exercise 4.** Suppose the risk-neutral distribution of $S_T$ is supported on three points $\{80, 100, 120\}$ with probabilities $\{q_1, q_2, q_3\}$. Given that $S_0 = 100$ and $r = 0$, write down the constraints that $q_1, q_2, q_3$ must satisfy (martingale, normalization, non-negativity). Then formulate and solve the linear program that gives the model-free upper bound for the price of a digital option paying $1$ if $S_T > 100$.

??? success "Solution to Exercise 4"

    **Constraints.** With $S_T \in \{80, 100, 120\}$, probabilities $(q_1, q_2, q_3)$, $S_0 = 100$, and $r = 0$:

    - Non-negativity: $q_1, q_2, q_3 \geq 0$
    - Normalization: $q_1 + q_2 + q_3 = 1$
    - Martingale: $80q_1 + 100q_2 + 120q_3 = 100$

    From normalization and martingale constraints:

    $$
    80q_1 + 100(1 - q_1 - q_3) + 120q_3 = 100
    $$

    $$
    -20q_1 + 20q_3 = 0 \implies q_1 = q_3
    $$

    So $q_1 = q_3 = p$ and $q_2 = 1 - 2p$ with $p \in [0, 1/2]$.

    **Digital option payoff.** The digital call pays 1 if $S_T > 100$, zero otherwise:

    $$
    \xi = \begin{cases} 0 & \text{if } S_T = 80 \\ 0 & \text{if } S_T = 100 \\ 1 & \text{if } S_T = 120 \end{cases}
    $$

    **Expected payoff:**

    $$
    \mathbb{E}_\mathbb{Q}[\xi] = q_3 = p
    $$

    **LP for upper bound:**

    $$
    \overline{V} = \max_{p \in [0, 1/2]} p = \frac{1}{2}
    $$

    achieved at $p = 1/2$, giving $(q_1, q_2, q_3) = (1/2, 0, 1/2)$.

    **LP for lower bound:**

    $$
    \underline{V} = \min_{p \in [0, 1/2]} p = 0
    $$

    achieved at $p = 0$, giving $(q_1, q_2, q_3) = (0, 1, 0)$.

    Therefore the model-free bounds for the digital call are $[0, 1/2]$.

    The extremal measures are:

    - **Upper bound**: $S_T \in \{80, 120\}$ with equal probability. This is the maximum-entropy binary distribution consistent with the martingale constraint, which assigns the largest possible probability to the event $\{S_T > 100\}$.
    - **Lower bound**: $S_T = 100$ with certainty. Under this degenerate model, the stock never exceeds 100 at maturity, so the digital call is worthless.

---

**Exercise 5.** For an arithmetic Asian call with payoff $\left(\frac{1}{2}(S_{T/2} + S_T) - K\right)^+$, explain why the model-free upper bound satisfies

$$
C_{\text{Asian}}(K) \leq \frac{1}{2}\bigl(C(K, T/2) + C(K, T)\bigr)
$$

where $C(K, T/2)$ and $C(K, T)$ are European call prices at the respective maturities. Under what conditions is this bound tight?

??? success "Solution to Exercise 5"

    **Upper bound derivation.** By the convexity of $(\cdot)^+$ and the sub-additivity property:

    $$
    \left(\frac{1}{2}(S_{T/2} + S_T) - K\right)^+ \leq \frac{1}{2}(S_{T/2} - K)^+ + \frac{1}{2}(S_T - K)^+
    $$

    This follows because for any $a, b, K$:

    $$
    \left(\frac{a + b}{2} - K\right)^+ = \left(\frac{(a - K) + (b - K)}{2}\right)^+ \leq \frac{(a - K)^+ + (b - K)^+}{2}
    $$

    where the inequality uses the convexity of $x \mapsto x^+$ and the fact that $\frac{1}{2}(a - K) + \frac{1}{2}(b - K) = \frac{1}{2}(a - K)^+ + \frac{1}{2}(b - K)^+ - \frac{1}{2}(a - K)^- - \frac{1}{2}(b - K)^-$, but more directly: since $x^+$ is convex, $\left(\frac{x_1 + x_2}{2}\right)^+ \leq \frac{x_1^+ + x_2^+}{2}$.

    Taking expectations under any risk-neutral measure $\mathbb{Q}$ and discounting:

    $$
    C_{\text{Asian}}(K) \leq \frac{1}{2}C(K, T/2) + \frac{1}{2}C(K, T)
    $$

    This is a model-free upper bound, valid under any martingale model.

    **When is this bound tight?** The bound is tight (equality holds) when:

    $$
    \left(\frac{S_{T/2} + S_T}{2} - K\right)^+ = \frac{1}{2}(S_{T/2} - K)^+ + \frac{1}{2}(S_T - K)^+
    $$

    almost surely. By the condition for equality in Jensen's inequality, this requires that $(S_{T/2} - K)$ and $(S_T - K)$ have the **same sign** almost surely, meaning either both $S_{T/2} > K$ and $S_T > K$, or both $S_{T/2} \leq K$ and $S_T \leq K$.

    This happens in degenerate cases:

    1. If $K = 0$: both terms are always positive (for positive stock prices), so equality holds trivially.
    2. If $S_{T/2} = S_T$ almost surely (zero volatility between $T/2$ and $T$): both observations are the same, so both terms have the same sign.
    3. If the stock price is almost surely above or below $K$ at both times (e.g., $K$ is very far out of the money or very deep in the money).

    In general, for finite positive volatility and moderate strikes, the bound is strict.

---

**Exercise 6.** Show that the model-free implied variance $\sigma_{\text{MF}}^2$ can be computed from put options alone when $S_0 = F$ (the forward price equals the current price). Specifically, derive

$$
\sigma_{\text{MF}}^2 = \frac{2}{T} \int_0^{S_0} \frac{P(K)}{K^2} \, dK + \frac{2}{T} \int_{S_0}^{\infty} \frac{C(K)}{K^2} \, dK
$$

and explain why in practice this formula uses out-of-the-money options for both puts ($K < S_0$) and calls ($K > S_0$).

??? success "Solution to Exercise 6"

    **Derivation of the model-free implied variance formula.**

    Starting from the Carr-Madan decomposition for $g(S_T) = -\log(S_T/S_0)$ with $F = S_0 e^{rT}$ and $r = 0$ (so $F = S_0$):

    $$
    -\log\frac{S_T}{S_0} = -\log 1 + \left(-\frac{1}{S_0}\right)(S_T - S_0) + \int_0^{S_0} \frac{1}{K^2}(K - S_T)^+ \, dK + \int_{S_0}^\infty \frac{1}{K^2}(S_T - K)^+ \, dK
    $$

    since $g'(K) = -1/K$ and $g''(K) = 1/K^2$. Taking expectations:

    $$
    -\mathbb{E}_\mathbb{Q}\left[\log\frac{S_T}{S_0}\right] = 0 + \int_0^{S_0} \frac{P(K)}{K^2} \cdot e^{rT} \, dK + \int_{S_0}^\infty \frac{C(K)}{K^2} \cdot e^{rT} \, dK
    $$

    With $r = 0$ (so $e^{rT} = 1$):

    $$
    -\mathbb{E}_\mathbb{Q}\left[\log\frac{S_T}{S_0}\right] = \int_0^{S_0} \frac{P(K)}{K^2}\,dK + \int_{S_0}^\infty \frac{C(K)}{K^2}\,dK
    $$

    The model-free implied variance is defined as:

    $$
    \sigma_{\text{MF}}^2 = \frac{2}{T}\left(-\mathbb{E}_\mathbb{Q}\left[\log\frac{S_T}{S_0}\right]\right) = \frac{2}{T}\int_0^{S_0} \frac{P(K)}{K^2}\,dK + \frac{2}{T}\int_{S_0}^\infty \frac{C(K)}{K^2}\,dK
    $$

    When $S_0 = F$ (i.e., $r = 0$ or equivalently working with forward prices), this is exactly the formula stated in the exercise. $\checkmark$

    **Why out-of-the-money options are used in practice.**

    The formula splits into puts below $S_0$ and calls above $S_0$:

    - For $K < S_0$: use put prices $P(K)$. These are **out-of-the-money puts**.
    - For $K > S_0$: use call prices $C(K)$. These are **out-of-the-money calls**.

    There are two reasons for this choice:

    1. **Liquidity**: Out-of-the-money options are more actively traded than in-the-money options. Using OTM puts for $K < S_0$ and OTM calls for $K > S_0$ relies on the most liquid instruments, yielding more reliable price data.

    2. **Equivalence via put-call parity**: By put-call parity ($C(K) - P(K) = S_0 - Ke^{-rT}$), one can convert between puts and calls. For $K < S_0$:

        $$
        \frac{P(K)}{K^2} = \frac{C(K) - (S_0 - K)}{K^2}
        $$

        Using OTM puts directly avoids the subtraction of two large numbers (ITM call price minus intrinsic value), which would amplify measurement errors. Similarly for $K > S_0$, using OTM calls avoids subtracting intrinsic value from ITM put prices.

    This is precisely the methodology used by the CBOE in computing the VIX index.

---

**Exercise 7.** Consider a market with two risky assets $S^{(1)}$ and $S^{(2)}$ and suppose the marginal distributions of $S_T^{(1)}$ and $S_T^{(2)}$ are both uniform on $[80, 120]$ with $S_0^{(1)} = S_0^{(2)} = 100$. Using Frechet-Hoeffding bounds, derive model-free upper and lower bounds on the price of a spread option with payoff $(S_T^{(1)} - S_T^{(2)})^+$. Explain why the upper bound corresponds to the case of maximal negative correlation between the two assets.

??? success "Solution to Exercise 7"

    **Setup.** Both marginals are $\mu_1 = \mu_2 = \text{Uniform}[80, 120]$ with mean 100. The spread option payoff is $(S_T^{(1)} - S_T^{(2)})^+$.

    **Frechet-Hoeffding bounds.** For any joint distribution $\pi$ with given marginals $\mu_1$ and $\mu_2$, the Frechet-Hoeffding bounds on the joint CDF are:

    $$
    \max(F_1(x) + F_2(y) - 1, 0) \leq \pi(S_T^{(1)} \leq x, S_T^{(2)} \leq y) \leq \min(F_1(x), F_2(y))
    $$

    The upper Frechet bound (comonotonic coupling) corresponds to $S_T^{(2)} = F_2^{-1}(F_1(S_T^{(1)}))$. Since both marginals are identical, comonotonicity means $S_T^{(1)} = S_T^{(2)}$ a.s.

    The lower Frechet bound (countermonotonic coupling) corresponds to $S_T^{(2)} = F_2^{-1}(1 - F_1(S_T^{(1)}))$. For identical uniform marginals, this gives $S_T^{(2)} = 200 - S_T^{(1)}$.

    **Lower bound on spread option price.** Under the comonotonic coupling ($S_T^{(1)} = S_T^{(2)}$):

    $$
    (S_T^{(1)} - S_T^{(2)})^+ = 0 \quad \text{a.s.}
    $$

    So $\underline{V} = 0$. (This is also trivially a lower bound since $(x)^+ \geq 0$.)

    **Upper bound on spread option price.** Under the countermonotonic coupling ($S_T^{(2)} = 200 - S_T^{(1)}$), with $U = S_T^{(1)} \sim \text{Uniform}[80, 120]$:

    $$
    (S_T^{(1)} - S_T^{(2)})^+ = (U - (200 - U))^+ = (2U - 200)^+
    $$

    This is positive when $U > 100$, i.e., $S_T^{(1)} > 100$:

    $$
    \overline{V} = \mathbb{E}[(2U - 200)^+] = \int_{100}^{120} (2u - 200) \cdot \frac{1}{40} \, du
    $$

    $$
    = \frac{1}{40}\left[(u^2 - 200u)\right]_{100}^{120} = \frac{1}{40}\left[(14400 - 24000) - (10000 - 20000)\right]
    $$

    $$
    = \frac{1}{40}[{-9600} - ({-10000})] = \frac{1}{40}(400) = 10
    $$

    So $\overline{V} = 10$.

    **Why the upper bound corresponds to maximal negative correlation.**

    The countermonotonic coupling has correlation $\rho = -1$. Under this coupling, when $S_T^{(1)}$ is high, $S_T^{(2)}$ is low, maximizing the spread $S_T^{(1)} - S_T^{(2)}$ and hence the payoff $(S_T^{(1)} - S_T^{(2)})^+$.

    More precisely, for the payoff $(S_T^{(1)} - S_T^{(2)})^+$:

    - The payoff increases with $S_T^{(1)}$ and decreases with $S_T^{(2)}$.
    - By the rearrangement inequality, $\mathbb{E}[f(X)g(Y)]$ is maximized when $f$ is increasing, $g$ is decreasing, and $X, Y$ are countermonotonic.
    - Since we want to maximize a function that benefits from $S_T^{(1)}$ being large when $S_T^{(2)}$ is small, maximal negative dependence (countermonotonicity) is optimal.

    Therefore the model-free bounds on the spread option are $[0, 10]$.
