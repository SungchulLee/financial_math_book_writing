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

### Market Setup

**Traded Assets**: Consider a frictionless market with:
- A riskless asset (bond) with price $B_t = e^{rt}$
- A risky asset (stock) with price process $S_t$
- European options with various strikes and maturities

**No-Arbitrage Assumption**: There exists no trading strategy that:
1. Requires no initial investment
2. Has non-negative payoff with probability 1
3. Has positive payoff with positive probability

**Fundamental Theorem of Asset Pricing**: Under no-arbitrage, there exists a probability measure $\mathbb{Q}$ equivalent to the physical measure $\mathbb{P}$ such that discounted asset prices are $\mathbb{Q}$-martingales:

$$
\frac{S_t}{B_t} = \mathbb{E}_{\mathbb{Q}}\left[ \frac{S_T}{B_T} \,\bigg|\, \mathcal{F}_t \right]
$$

### Model-Free Setting

**Given Information**:
- Current stock price $S_0$
- Risk-free rate $r$
- Maturity $T$
- Prices of European calls $C(K)$ for various strikes $K$

**Unknown**: The specific dynamics of $S_t$ or equivalently, the probability measure $\mathbb{Q}$.

**Goal**: Derive bounds on prices of exotic derivatives using only no-arbitrage and observed vanilla option prices.

## Static Arbitrage Bounds

### Call Option Bounds

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

### Put Option Bounds

**Lower Bound**:

$$
P(K, T) \geq (Ke^{-rT} - S_0)^+
$$

**Upper Bound**:

$$
P(K, T) \leq Ke^{-rT}
$$

**Proof**: A put option cannot be worth more than the present value of the strike. If $P(K, T) > Ke^{-rT}$, sell the put and invest the proceeds for arbitrage.

### Put-Call Parity

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

### Convexity in Strike

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

### Monotonicity

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

### Slope Constraints

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

### Risk-Neutral Density Recovery

**Theorem** (Breeden-Litzenberger, 1978): The risk-neutral density is given by:

$$
q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}(K)
$$

**Proof**: Starting from the call option formula:

$$
C(K) = e^{-rT} \int_K^{\infty} (S - K) q(S) \, dS
$$

Differentiate once with respect to $K$:

$$
\frac{\partial C}{\partial K} = e^{-rT} \int_K^{\infty} (-1) q(S) \, dS = -e^{-rT} \int_K^{\infty} q(S) \, dS
$$

Differentiate again:

$$
\frac{\partial^2 C}{\partial K^2} = e^{-rT} q(K)
$$

**Implications**:
1. Convexity of $C(K)$ ensures $q(K) \geq 0$ (probability density)
2. The integral $\int_0^{\infty} q(K) \, dK = 1$ (normalization)
3. The forward price:
   $$
   F_0 = \int_0^{\infty} K q(K) \, dK = S_0 e^{rT}
   $$

### Practical Implementation

**Discrete Approximation**: With observed call prices $\{C(K_i)\}_{i=1}^n$:

$$
q(K_i) \approx e^{rT} \frac{C(K_{i-1}) - 2C(K_i) + C(K_{i+1})}{(K_{i+1} - K_i)(K_i - K_{i-1})}
$$

**Interpolation**: Use splines or other smooth interpolation methods to obtain a continuous function $C(K)$, then differentiate numerically.

**Regularization**: In practice, raw market prices may violate no-arbitrage constraints due to:
- Bid-ask spreads
- Discrete strikes
- Market microstructure noise

Regularized approaches project observed prices onto the space of arbitrage-free prices.

## Carr-Madan Formula

### Derivative Payoff Decomposition

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

### Applications

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

### Forward Start Options

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

### Lookback Options

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

### Barrier Options

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

### Primal and Dual Problems

**Primal Problem** (Buyer's Perspective): Minimize the super-replication cost:

$$
\pi^{\text{sup}}(g) = \inf \left\{ V_0: \exists \text{ trading strategy with } V_T \geq g(S_T) \text{ a.s.} \right\}
$$

**Dual Problem**: Maximize over all equivalent martingale measures:

$$
\pi^{\text{dual}}(g) = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} g(S_T)]
$$

where $\mathcal{M}$ is the set of equivalent martingale measures.

**Fundamental Duality Theorem**: Under appropriate technical conditions:

$$
\pi^{\text{sup}}(g) = \pi^{\text{dual}}(g)
$$

**Interpretation**: 
- The minimum cost to super-replicate equals the maximum expected discounted payoff over all martingale measures
- This provides a dual characterization of derivative prices
- Strong duality holds in frictionless markets

### Sub-Replication

**Sub-Replication Cost**:

$$
\pi^{\text{sub}}(g) = \sup \left\{ V_0: \exists \text{ trading strategy with } V_T \leq g(S_T) \text{ a.s.} \right\}
$$

**Dual Characterization**:

$$
\pi^{\text{sub}}(g) = \inf_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}_{\mathbb{Q}}[e^{-rT} g(S_T)]
$$

**Complete Markets**: When the market is complete (unique martingale measure):

$$
\pi^{\text{sup}}(g) = \pi^{\text{sub}}(g) = \mathbb{E}_{\mathbb{Q}}[e^{-rT} g(S_T)]
$$

**Incomplete Markets**: 

$$
\pi^{\text{sub}}(g) \leq \pi^{\text{sup}}(g)
$$

with strict inequality reflecting model uncertainty.

## Advanced Model-Free Results

### Variance Bounds

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

### Moment Constraints

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

### Constrained Martingale Measures

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

### Optimization Formulation

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

### Extremal Measures

**Theorem**: The extremal measures (achieving the supremum or infimum) are typically **discrete** with support on at most $n+2$ points, where $n$ is the number of traded strikes.

**Proof Sketch**: By linear programming duality, the optimal solution has at most as many support points as constraints.

**Implication**: The worst-case or best-case scenario for pricing corresponds to a discrete probability distribution, concentrating mass on a few states.

## Applications and Examples

### Example 1: Digital Option Bounds

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

### Example 2: Variance Swap Replication

**Variance Swap Payoff**: Pays the realized variance:

$$
\text{Payoff} = \frac{1}{T} \sum_{i=1}^N \left( \log \frac{S_{t_i}}{S_{t_{i-1}}} \right)^2
$$

**Model-Free Replication**: Using the log-contract:

$$
\mathbb{E}_{\mathbb{Q}}\left[ \log \frac{S_T}{S_0} \right] = e^{-rT} \left( \int_0^{S_0} \frac{P(K)}{K^2} \, dK + \int_{S_0}^{\infty} \frac{C(K)}{K^2} \, dK \right)
$$

The variance can be replicated (approximately) by a portfolio of puts and calls.

### Example 3: Asian Option Bounds

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

### Linear Programming Approach

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

### Semidefinite Programming

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

### Monte Carlo Methods

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

### Model-Free Bound Limitations

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

### Additional Market Information

**Volatility Surface**: Incorporating options at multiple maturities:

$$
\{C(K, T_i): i = 1, \ldots, M\}
$$

tightens bounds significantly for path-dependent options.

**Co-monotonicity**: Assuming monotonicity relationships between prices at different times can further tighten bounds.

**Dividend Information**: Knowledge of dividend payments $\{d_i, t_i\}$ modifies the martingale constraint.

### Extensions to Multiple Assets

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

### Fundamental Principles

1. **No-Arbitrage Foundation**: Model-free bounds rely purely on the absence of arbitrage, not on specific dynamical assumptions.

2. **Static Replication**: Many derivatives can be replicated using portfolios of vanilla options, enabling model-independent pricing.

3. **Duality**: Super-replication costs equal supremum over martingale measures; sub-replication costs equal infimum.

4. **Convexity**: The call price function's convexity in strike ensures non-negative risk-neutral densities and provides structural constraints.

5. **Information Content**: Vanilla option prices encode the risk-neutral distribution, accessible via the Breeden-Litzenberger formula.

### Practical Implications

**For Traders**:
- Model-free bounds provide arbitrage-free price ranges
- Observed market prices outside these bounds indicate arbitrage opportunities (after transaction costs)

**For Risk Managers**:
- Robust bounds quantify model uncertainty
- Worst-case scenarios guide capital allocation

**For Researchers**:
- Model-free results identify which features are truly necessary for pricing
- Gaps between model-free bounds and model-specific prices reveal model-dependent risk premiums

### Open Questions

1. **Tightness**: How to tighten bounds for exotic derivatives using limited additional information?

2. **Dynamic Bounds**: Extending model-free theory to multi-period settings with intermediate hedging.

3. **Computational Efficiency**: Faster algorithms for high-dimensional robust pricing problems.

4. **Market Microstructure**: Incorporating realistic frictions (bid-ask spreads, discrete strikes) into model-free theory.

Model-free bounds represent a cornerstone of robust derivative pricing, providing rigorous constraints that must hold regardless of modeling assumptions. This theory bridges classical arbitrage pricing with modern robust optimization, offering both theoretical insights and practical tools for quantitative finance.
