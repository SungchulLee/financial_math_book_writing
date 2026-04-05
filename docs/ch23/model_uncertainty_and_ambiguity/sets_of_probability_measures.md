# Sets of Probability Measures


## Introduction


When facing model uncertainty, decision makers and financial analysts work with **sets of probability measures** rather than a single canonical measure. This mathematical framework provides the foundation for robust optimization, ambiguity-averse preferences, and stress testing in quantitative finance.

This chapter develops the mathematical theory of sets of probability measures, their topological properties, and applications to robust valuation and risk management.

## Mathematical Foundations


### 1. Probability Spaces and Measures


**Setup**: Let $(\Omega, \mathcal{F})$ be a measurable space where:
- $\Omega$ is the state space
- $\mathcal{F}$ is a $\sigma$-algebra of events

**Probability Measure**: A function $P: \mathcal{F} \to [0,1]$ satisfying:
1. $P(\emptyset) = 0$, $P(\Omega) = 1$
2. Countable additivity: For disjoint $\{A_i\}_{i=1}^{\infty}$,

   $$
   P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)
   $$



**Space of Probability Measures**: Denote:


$$
\mathcal{M}_1(\Omega) = \{ P: P \text{ is a probability measure on } (\Omega, \mathcal{F}) \}
$$



### 2. Weak Topology


The space $\mathcal{M}_1(\Omega)$ is endowed with the **weak topology** (or weak-* topology).

**Definition** (Weak Convergence): A sequence $\{P_n\}$ converges weakly to $P$ (written $P_n \xrightarrow{w} P$) if:


$$
\int_{\Omega} f \, dP_n \to \int_{\Omega} f \, dP
$$



for all bounded continuous functions $f: \Omega \to \mathbb{R}$.

**Portmanteau Theorem**: The following are equivalent for $P_n \xrightarrow{w} P$:

1. $\int f \, dP_n \to \int f \, dP$ for all bounded continuous $f$
2. $\limsup_n P_n(F) \leq P(F)$ for all closed sets $F$
3. $\liminf_n P_n(G) \geq P(G)$ for all open sets $G$
4. $P_n(A) \to P(A)$ for all $P$-continuity sets $A$ (i.e., $P(\partial A) = 0$)

**Prokhorov's Theorem**: If $\Omega$ is a complete separable metric space (Polish space), then:
- $\mathcal{M}_1(\Omega)$ is complete and separable in the weak topology
- A subset $\mathcal{P} \subseteq \mathcal{M}_1(\Omega)$ is relatively compact iff it is tight

### 3. Total Variation Distance


**Definition** (Total Variation): The total variation distance between probability measures $P$ and $Q$ is:


$$
\|P - Q\|_{\text{TV}} = \sup_{A \in \mathcal{F}} |P(A) - Q(A)| = \frac{1}{2} \int_{\Omega} \left| \frac{dP}{d\mu} - \frac{dQ}{d\mu} \right| d\mu
$$



where $\mu = P + Q$.

**Properties**:
1. Metric: $\|P - Q\|_{\text{TV}}$ defines a metric on $\mathcal{M}_1(\Omega)$
2. Range: $\|P - Q\|_{\text{TV}} \in [0, 1]$
3. Triangle inequality: $\|P - R\|_{\text{TV}} \leq \|P - Q\|_{\text{TV}} + \|Q - R\|_{\text{TV}}$

**Relationship to Weak Topology**: Total variation is stronger than weak convergence:


$$
\|P_n - P\|_{\text{TV}} \to 0 \implies P_n \xrightarrow{w} P
$$



but the converse is generally false.

## Specification of Sets of Probability Measures


### 1. Parametric Uncertainty Sets


**$\varepsilon$-Contamination**: Given a reference measure $P_0$ and contamination level $\varepsilon \in [0,1]$:


$$
\mathcal{P}_{\varepsilon} = \{ (1-\varepsilon) P_0 + \varepsilon Q: Q \in \mathcal{M}_1(\Omega) \}
$$



**Interpretation**: At most $\varepsilon$ fraction of the probability mass can come from an arbitrary measure $Q$.

**Total Variation Ball**:


$$
\mathcal{P}_{\text{TV}}(\delta) = \{ P: \|P - P_0\|_{\text{TV}} \leq \delta \}
$$



**KL Divergence Ball** (Relative Entropy Ball):


$$
\mathcal{P}_{\text{KL}}(\theta) = \left\{ P \ll P_0: D_{\text{KL}}(P \| P_0) \leq \theta \right\}
$$



where the KL divergence is:


$$
D_{\text{KL}}(P \| P_0) = \begin{cases}
\displaystyle\int_{\Omega} \log\left(\frac{dP}{dP_0}\right) dP & \text{if } P \ll P_0 \\
+\infty & \text{otherwise}
\end{cases}
$$



### 2. Density-Based Sets


**Density Ratio Bounds**: For a reference measure $P_0$:


$$
\mathcal{P}_{\text{density}} = \left\{ P: \frac{dP}{dP_0}(\omega) \in [\ell(\omega), u(\omega)] \text{ for } P_0\text{-a.e. } \omega \right\}
$$



where $0 \leq \ell(\omega) \leq u(\omega)$ are given density bounds.

**Example**: In continuous time, specify bounds on the market price of risk:


$$
\mathcal{Q} = \left\{ \mathbb{Q}: \left\| \frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_t} \right\|_{L^{\infty}} \leq K \right\}
$$



### 3. Moment-Based Sets


**Mean-Variance Uncertainty**: For a random vector $X$:


$$
\mathcal{P}_{\text{moment}} = \left\{ P: \mathbb{E}_P[X] \in \mathcal{M}, \, \text{Cov}_P(X) \in \Sigma \right\}
$$



where $\mathcal{M} \subseteq \mathbb{R}^n$ and $\Sigma$ is a set of positive semidefinite matrices.

**General Moment Constraints**:


$$
\mathcal{P} = \left\{ P: \mathbb{E}_P[g_i(X)] \in \mathcal{C}_i, \, i = 1, \ldots, k \right\}
$$



for constraint sets $\mathcal{C}_i \subseteq \mathbb{R}$.

### 4. Rectangularity


A fundamental concept for dynamic consistency in multi-period models.

**Definition** (Rectangular Set): A set $\mathcal{P}$ of probability measures on $(\Omega, \mathcal{F}_T)$ is **rectangular** with respect to a filtration $\{\mathcal{F}_t\}_{t \leq T}$ if for any $P, Q \in \mathcal{P}$, the "pasted" measure:


$$
R(A) = \mathbb{E}_P[\mathbb{1}_A \cdot \mathbb{1}_B + \mathbb{1}_A \cdot \mathbb{1}_{B^c} \cdot P(A|\mathcal{F}_t) / Q(B|\mathcal{F}_t) \cdot Q(A|\mathcal{F}_t)]
$$



also belongs to $\mathcal{P}$ for all $B \in \mathcal{F}_t$ and $A \in \mathcal{F}_T$.

**Intuitive Characterization**: $\mathcal{P}$ is rectangular if:


$$
\mathcal{P} = \left\{ P: P(\cdot | \mathcal{F}_t) \in \mathcal{P}_t \text{ for all } t \leq T \right\}
$$



where $\mathcal{P}_t$ are measurable families of conditional distributions.

**Importance**: Rectangularity ensures that optimal decisions under maxmin preferences remain optimal when reconsidered at intermediate times (dynamic consistency).

## Convexity and Compactness Properties


### 1. Convex Sets of Measures


**Convex Combination**: For $P, Q \in \mathcal{M}_1(\Omega)$ and $\lambda \in [0,1]$:


$$
\lambda P + (1-\lambda) Q \in \mathcal{M}_1(\Omega)
$$



**Convex Hull**: For a family $\{\mathcal{P}_i\}_{i \in I}$:


$$
\text{conv}(\mathcal{P}) = \left\{ \sum_{i=1}^n \lambda_i P_i: P_i \in \mathcal{P}, \sum_{i=1}^n \lambda_i = 1, \lambda_i \geq 0 \right\}
$$



**Theorem**: Many natural uncertainty sets are convex:
1. KL balls: $\mathcal{P}_{\text{KL}}(\theta)$ is convex
2. Total variation balls: $\mathcal{P}_{\text{TV}}(\delta)$ is convex
3. Moment-constrained sets: $\mathcal{P}_{\text{moment}}$ is convex (under convex constraints)

### 2. Compactness


**Theorem** (Compact Sets): Under weak topology, $\mathcal{P} \subseteq \mathcal{M}_1(\Omega)$ is compact if:
1. $\mathcal{P}$ is closed
2. $\mathcal{P}$ is tight (for Polish spaces)

**Tightness**: A family $\mathcal{P}$ is **tight** if for every $\varepsilon > 0$, there exists a compact set $K \subseteq \Omega$ such that:


$$
P(K) > 1 - \varepsilon \quad \text{for all } P \in \mathcal{P}
$$



**Implications**: Compactness ensures that:
- $\min_{P \in \mathcal{P}} \mathbb{E}_P[f]$ is attained for continuous $f$
- Sequential minimizing procedures converge

### 3. Extreme Points and Choquet's Theorem


**Extreme Point**: $P \in \mathcal{P}$ is an **extreme point** if it cannot be written as a strict convex combination:


$$
P = \lambda P_1 + (1-\lambda) P_2 \quad \text{with } P_1, P_2 \in \mathcal{P}, P_1 \neq P_2, \lambda \in (0,1)
$$



implies $P = P_1 = P_2$.

**Choquet's Theorem**: If $\mathcal{P}$ is a compact convex set in a locally convex topological vector space, then every $P \in \mathcal{P}$ can be represented as:


$$
P = \int_{\text{ext}(\mathcal{P})} Q \, d\mu(Q)
$$



for some probability measure $\mu$ on the set of extreme points $\text{ext}(\mathcal{P})$.

**Application**: For maxmin expected utility:


$$
\min_{P \in \mathcal{P}} \mathbb{E}_P[u(X)] = \min_{P \in \text{ext}(\mathcal{P})} \mathbb{E}_P[u(X)]
$$



reducing the optimization to extreme points.

## Robust Optimization Framework


### 1. General Robust Problem


Consider the robust optimization problem:


$$
\inf_{x \in \mathcal{X}} \sup_{P \in \mathcal{P}} \mathbb{E}_P[f(x, \omega)]
$$



where:
- $\mathcal{X}$ is the decision space
- $\mathcal{P}$ is the uncertainty set of probability measures
- $f(x, \omega)$ is the loss function

**Minimax Theorem**: Under appropriate conditions (compactness, convexity, continuity):


$$
\inf_{x \in \mathcal{X}} \sup_{P \in \mathcal{P}} \mathbb{E}_P[f(x, \omega)] = \sup_{P \in \mathcal{P}} \inf_{x \in \mathcal{X}} \mathbb{E}_P[f(x, \omega)]
$$



### 2. Duality and Conjugate Functions


**Conjugate Function**: For a convex function $\phi: \mathbb{R}^n \to \mathbb{R}$:


$$
\phi^*(y) = \sup_{x \in \mathbb{R}^n} \left\{ x^\top y - \phi(x) \right\}
$$



**Fenchel-Rockafellar Duality**: For convex $f, g$:


$$
\inf_x \{ f(x) + g(x) \} = \sup_{y} \{ -f^*(y) - g^*(-y) \}
$$



**Application to Robust Optimization**: The robust problem:


$$
\min_{x} \max_{P \in \mathcal{P}} \mathbb{E}_P[f(x, \cdot)]
$$



can be reformulated using the conjugate of the indicator function of $\mathcal{P}$.

### 3. Specific Examples


### 4. Robust Mean-Variance Portfolio


**Problem**: 


$$
\max_{w} \min_{P \in \mathcal{P}} \left\{ w^\top \mathbb{E}_P[R] - \frac{\lambda}{2} w^\top \text{Cov}_P(R) w \right\}
$$



**KL Uncertainty**: For $\mathcal{P} = \mathcal{P}_{\text{KL}}(\theta)$:


$$
\min_{P \in \mathcal{P}} \mathbb{E}_P[w^\top R] = \mathbb{E}_{P_0}[w^\top R] - \sqrt{2\theta \cdot w^\top \Sigma_0 w}
$$



where $\Sigma_0 = \text{Cov}_{P_0}(R)$.

**Robust Portfolio**:


$$
w^* = \frac{1}{\lambda + \sqrt{2\theta/\mu^\top \Sigma_0^{-1} \mu}} \Sigma_0^{-1} \mu_0
$$



where $\mu_0 = \mathbb{E}_{P_0}[R]$.

### 5. Robust Option Pricing


**Problem**: Price a European option with payoff $\Phi(S_T)$ under model uncertainty.

**Setup**: Consider equivalent martingale measures $\mathbb{Q}$ with bounded market price of risk:


$$
\mathcal{Q} = \left\{ \mathbb{Q}: \left\| \frac{d\mathbb{Q}}{d\mathbb{P}} \right\|_{\infty} \leq K \right\}
$$



**Robust Price**:


$$
V_0 = \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}_{\mathbb{Q}}\left[ e^{-rT} \Phi(S_T) \right]
$$



**PDE Formulation**: The value function $V(t, S)$ satisfies the Hamilton-Jacobi-Bellman equation:


$$
\frac{\partial V}{\partial t} + \sup_{\sigma \in [\sigma_{\min}, \sigma_{\max}]} \mathcal{L}^{\sigma} V = 0
$$



where $\mathcal{L}^{\sigma}$ is the Black-Scholes operator with volatility $\sigma$.

## Contraction and Expansion of Uncertainty Sets


### 1. Conditional Updating


**Question**: How should $\mathcal{P}$ be updated upon observing information $\mathcal{F}_t$?

**Naive Update** (Full Bayesian):


$$
\mathcal{P}_t = \{ P(\cdot | \mathcal{F}_t): P \in \mathcal{P} \}
$$



**Problem**: This may not preserve rectangularity or lead to time-consistent preferences.

**Maximum Likelihood Update**: Choose the measure in $\mathcal{P}$ most consistent with observed data:


$$
P_t = \arg\max_{P \in \mathcal{P}} \text{likelihood}(P | \text{data up to } t)
$$



**Robust Bayesian Update**: Update using worst-case likelihood:


$$
\mathcal{P}_t = \left\{ P \in \mathcal{P}: \frac{dP}{dP_0}\bigg|_{\mathcal{F}_t} \geq \ell_t \right\}
$$



for appropriately chosen threshold $\ell_t$.

### 2. Learning and Contraction


As more data is observed, uncertainty should decrease.

**Frequentist Consistency**: If the true measure $P^* \in \mathcal{P}$, then with probability one:


$$
\mathcal{P}_n \to \{P^*\} \quad \text{as } n \to \infty
$$



where $\mathcal{P}_n$ is the posterior uncertainty set after $n$ observations.

**Theorem** (Contraction Rate): Under regularity conditions, the diameter of $\mathcal{P}_n$ contracts at rate:


$$
\text{diam}(\mathcal{P}_n) = O_P(n^{-1/2})
$$



in appropriate metrics.

## Entropic Penalty and Relative Entropy


### 1. Relative Entropy


**Definition**: For $P \ll Q$:


$$
D_{\text{KL}}(P \| Q) = \int_{\Omega} \log\left(\frac{dP}{dQ}\right) dP
$$



**Properties**:
1. **Non-negativity**: $D_{\text{KL}}(P \| Q) \geq 0$ with equality iff $P = Q$ (Gibbs' inequality)
2. **Joint convexity**: $D_{\text{KL}}(\cdot \| \cdot)$ is jointly convex
3. **Data processing inequality**: For measurable $f$:

   $$
   D_{\text{KL}}(P \circ f^{-1} \| Q \circ f^{-1}) \leq D_{\text{KL}}(P \| Q)
   $$



### 2. Entropic Constraint


The KL divergence naturally penalizes deviation from a reference measure.

**Optimization Problem**:


$$
\min_{P} \mathbb{E}_P[X] \quad \text{subject to} \quad D_{\text{KL}}(P \| P_0) \leq \theta
$$



**Solution** (Exponential Tilting):


$$
\frac{dP^*}{dP_0} = \frac{e^{-\lambda^* X}}{Z(\lambda^*)}
$$



where:
- $\lambda^*$ is chosen so that $D_{\text{KL}}(P^* \| P_0) = \theta$
- $Z(\lambda) = \mathbb{E}_{P_0}[e^{-\lambda X}]$ is the moment generating function

### 3. Connection to Exponential Utility


**Entropic Risk Measure**:


$$
\rho_{\beta}(X) = \frac{1}{\beta} \log \mathbb{E}_{P_0}\left[ e^{\beta X} \right]
$$



**Dual Representation**:


$$
\rho_{\beta}(X) = \sup_{P \ll P_0} \left\{ \mathbb{E}_P[X] - \frac{1}{\beta} D_{\text{KL}}(P \| P_0) \right\}
$$



**Interpretation**: The supremum is over all measures $P$ in the entropic ball, trading off expected value against model distance.

**Exponential Utility**: For utility $u(x) = -e^{-\beta x}$:


$$
-\frac{1}{\beta} \log(-\mathbb{E}[u(X)]) = \rho_{\beta}(X)
$$



linking risk-sensitive preferences to model uncertainty.

## Applications in Continuous Time


### 1. Drift Uncertainty in Brownian Motion


**Setup**: Observed process:


$$
dX_t = \mu_t \, dt + \sigma \, dW_t
$$



with uncertain drift $\mu_t \in \mathcal{M}$.

**Set of Measures**: Define:


$$
\mathcal{P} = \left\{ P^{\mu}: \mu \in \mathcal{M} \right\}
$$



where under $P^{\mu}$, $X$ has drift $\mu$.

**Girsanov Theorem**: Measures $P^{\mu}$ are related by:


$$
\frac{dP^{\mu}}{dP^0}\bigg|_{\mathcal{F}_t} = \exp\left( \int_0^t \frac{\mu_s}{\sigma} dW_s - \frac{1}{2} \int_0^t \left(\frac{\mu_s}{\sigma}\right)^2 ds \right)
$$



### 2. Volatility Uncertainty


**Setup**: Stock price:


$$
dS_t = \mu S_t \, dt + \sigma_t S_t \, dW_t
$$



with $\sigma_t \in [\sigma_{\min}, \sigma_{\max}]$.

**Set of Equivalent Martingale Measures**: For each admissible $\sigma_t$:


$$
d\mathbb{Q}^{\sigma} = \exp\left( -\int_0^T \theta_s \, dW_s - \frac{1}{2} \int_0^T \theta_s^2 \, ds \right) d\mathbb{P}
$$



where $\theta_t = (\mu - r)/\sigma_t$ is the market price of risk.

**Robust Derivative Pricing**:


$$
V_t = \inf_{\sigma \in [\sigma_{\min}, \sigma_{\max}]} \mathbb{E}_{\mathbb{Q}^{\sigma}}\left[ e^{-r(T-t)} \Phi(S_T) \, \big| \, \mathcal{F}_t \right]
$$



### 3. Stochastic Control with Model Uncertainty


**Controlled SDE**:


$$
dX_t = b(X_t, u_t) \, dt + \sigma(X_t) \, dW_t + \gamma(X_t) \, dB_t
$$



where $B_t$ represents model misspecification.

**Robust Control Problem**:


$$
\inf_{u} \sup_{B} \mathbb{E}\left[ \int_0^T e^{-\rho t} \left( c(X_t, u_t) + \frac{\theta}{2} \left(\frac{dB_t}{dt}\right)^2 \right) dt \right]
$$



**Worst-Case Process**: The optimal misspecification $B^*$ satisfies:


$$
\frac{dB_t^*}{dt} = \frac{1}{\theta} \gamma(X_t)^\top \nabla V(t, X_t)
$$



where $V$ is the value function.

## Comparison of Uncertainty Specifications


### 1. Trade-offs Between Uncertainty Sets


| **Type** | **Advantages** | **Disadvantages** |
|----------|---------------|-------------------|
| **KL Ball** | Information-theoretic interpretation; tractable computations | Requires absolute continuity $P \ll P_0$ |
| **Total Variation** | Metric structure; easy to visualize | May be too restrictive in high dimensions |
| **Density Bounds** | Flexible; can incorporate expert judgment | Difficult to specify bounds a priori |
| **Moment-Based** | Uses observable quantities (mean, variance) | May include unrealistic measures |
| **$\varepsilon$-Contamination** | Simple parametrization | Limited modeling flexibility |

### 2. Computational Complexity


**KL Divergence**: Often leads to closed-form solutions via exponential tilting.

**Total Variation**: Generally requires numerical optimization but has finite-dimensional reformulation for discrete spaces.

**Moment Constraints**: Can be solved via semidefinite programming for polynomial moments.

**Density Bounds**: Typically requires Monte Carlo methods or grid-based approaches.

## Extreme Scenarios and Stress Testing


### 1. Worst-Case Measure


**Definition**: The **worst-case measure** for a loss function $\ell$ is:


$$
P^* = \arg\max_{P \in \mathcal{P}} \mathbb{E}_P[\ell]
$$



**Characterization**: For convex $\mathcal{P}$ and convex $\ell$, $P^*$ often lies on the boundary of $\mathcal{P}$.

### 2. Stress Testing Framework


**Objective**: Identify extreme but plausible scenarios.

**Reverse Stress Test**: Find the smallest perturbation $P^*$ such that:


$$
\mathbb{E}_{P^*}[\ell] \geq \ell_{\text{threshold}}
$$



subject to:


$$
D_{\text{KL}}(P^* \| P_0) \text{ is minimized}
$$



**Solution**: Use Lagrangian:


$$
\mathcal{L}(P, \lambda) = \mathbb{E}_P[\ell] + \lambda D_{\text{KL}}(P \| P_0)
$$



yielding:


$$
\frac{dP^*}{dP_0} \propto e^{-\lambda^* \ell}
$$



### 3. Scenario Generation


**Monte Carlo from Worst-Case Measure**: Sample paths from $P^*$ to generate stress scenarios.

**Importance Sampling**: Use $P^*$ as the importance distribution:


$$
\mathbb{E}_P[\ell] = \mathbb{E}_{P^*}\left[ \ell \cdot \frac{dP}{dP^*} \right]
$$



with reduced variance for rare events.

## Connections to Information Theory


### 1. Mutual Information Under Uncertainty


**Mutual Information**: For joint measure $P_{XY}$:


$$
I(X; Y) = D_{\text{KL}}(P_{XY} \| P_X \otimes P_Y)
$$



**Under Model Uncertainty**: Consider:


$$
I_{\min}(X; Y) = \inf_{P \in \mathcal{P}} I_P(X; Y)
$$



and:


$$
I_{\max}(X; Y) = \sup_{P \in \mathcal{P}} I_P(X; Y)
$$



**Application**: Robust portfolio diversification seeks to minimize $I_{\max}$ between asset returns.

### 2. Channel Capacity


**Definition**: Maximum information transmission rate:


$$
C = \sup_{P_X} \inf_{P_{Y|X}} I(X; Y)
$$



**Financial Interpretation**: Limits on information extraction from noisy market data under model uncertainty.

## Advanced Topics


### 1. Wasserstein Distance and Optimal Transport


**Wasserstein Distance**: For $p \geq 1$:


$$
W_p(P, Q) = \left( \inf_{\pi \in \Pi(P, Q)} \int_{\Omega \times \Omega} d(x, y)^p \, d\pi(x, y) \right)^{1/p}
$$



where $\Pi(P, Q)$ is the set of couplings with marginals $P$ and $Q$.

**Wasserstein Ball**:


$$
\mathcal{P}_W(\delta) = \{ P: W_p(P, P_0) \leq \delta \}
$$



**Advantages**: 
- Metrizes weak convergence
- Respects the geometry of $\Omega$
- Leads to smooth optimization problems

**Robust Optimization with Wasserstein**:


$$
\inf_x \sup_{P \in \mathcal{P}_W(\delta)} \mathbb{E}_P[f(x, \cdot)]
$$



### 2. φ-Divergences


**General Family**: For convex $\phi: [0, \infty) \to \mathbb{R}$ with $\phi(1) = 0$:


$$
D_{\phi}(P \| Q) = \int_{\Omega} \phi\left(\frac{dP}{dQ}\right) dQ
$$



**Examples**:
1. **KL Divergence**: $\phi(t) = t \log t$
2. **Total Variation**: $\phi(t) = |t - 1|$
3. **$\chi^2$ Divergence**: $\phi(t) = (t - 1)^2$
4. **Hellinger Distance**: $\phi(t) = (\sqrt{t} - 1)^2$

**Properties**: All $\phi$-divergences satisfy:
- Non-negativity
- Joint convexity
- Data processing inequality

### 3. Robustness and Minimax Theorems


**Sion's Minimax Theorem**: If $\mathcal{X}$ is compact convex, $\mathcal{P}$ is convex, and $f(x, P)$ is:
- Convex-continuous in $x$ for fixed $P$
- Concave-continuous in $P$ for fixed $x$

then:


$$
\inf_{x \in \mathcal{X}} \sup_{P \in \mathcal{P}} f(x, P) = \sup_{P \in \mathcal{P}} \inf_{x \in \mathcal{X}} f(x, P)
$$



**Application**: Ensures existence of saddle points in robust optimization.

### 4. Capacities and Non-Additive Measures


**Capacity** (Non-additive measure): $\nu: \mathcal{F} \to [0,1]$ satisfying:
1. $\nu(\emptyset) = 0$, $\nu(\Omega) = 1$
2. Monotonicity: $A \subseteq B \implies \nu(A) \leq \nu(B)$

**Core of Capacity**:


$$
\text{core}(\nu) = \{ P \in \mathcal{M}_1(\Omega): P(A) \geq \nu(A) \text{ for all } A \in \mathcal{F} \}
$$



**Theorem**: For convex capacities:


$$
\int f \, d\nu = \min_{P \in \text{core}(\nu)} \mathbb{E}_P[f]
$$



establishing connection between non-additive integration and maxmin preferences.

## Summary and Practical Guidelines


### 1. Key Theoretical Results


1. **Topological Structure**: $\mathcal{M}_1(\Omega)$ with weak topology is a complete separable metric space (for Polish $\Omega$)

2. **Compactness**: Tightness + closedness $\implies$ compactness, ensuring existence of extremal measures

3. **Rectangularity**: Necessary and sufficient for dynamic consistency with maxmin preferences

4. **Duality**: Robust optimization problems often admit dual formulations using conjugate functions

5. **Entropic Penalty**: KL divergence provides tractable penalty function with exponential tilting solutions

### 2. Practical Recommendations


**Specifying $\mathcal{P}$**:
1. Start with moment-based sets using observable statistics
2. Refine with KL or Wasserstein balls centered at empirical measure
3. Validate using stress tests and expert judgment

**Computational Approaches**:
1. Exploit extreme points for maxmin problems
2. Use duality for convex formulations
3. Apply importance sampling for rare events

**Model Selection**:
1. KL divergence: When absolute continuity is reasonable
2. Wasserstein distance: When geometry of outcomes matters
3. Total variation: For conservative worst-case analysis
4. Moment constraints: When statistical data is primary input

### 3. Open Research Questions


1. **High-Dimensional Uncertainty**: How to specify and compute with $\mathcal{P}$ in high dimensions without curse of dimensionality?

2. **Adaptive Learning**: Optimal procedures for updating $\mathcal{P}$ as data accumulates while maintaining rectangularity?

3. **Robust Deep Learning**: Incorporating model uncertainty into neural network training and deployment?

4. **Market Microstructure**: How does ambiguity aversion affect bid-ask spreads and liquidity in models with sets of measures?

The framework of sets of probability measures provides mathematically rigorous foundations for robust decision-making under model uncertainty, with far-reaching applications in quantitative finance, risk management, and machine learning.

---

## Exercises

**Exercise 1.** Let $P_0 = N(0, 1)$ be the standard normal distribution. Compute the KL divergence $D_{\text{KL}}(P \| P_0)$ when $P = N(\mu, 1)$ (shifted mean) and when $P = N(0, \sigma^2)$ (changed variance). For the KL ball $\mathcal{P}_{\text{KL}}(0.5) = \{P \ll P_0 : D_{\text{KL}}(P \| P_0) \leq 0.5\}$, determine the range of means $\mu$ allowed when the variance is fixed at 1.

??? success "Solution to Exercise 1"

    **Case 1: Shifted mean.** Let $P = N(\mu, 1)$ and $P_0 = N(0, 1)$. Using the KL divergence formula for Gaussians:

    $$
    D_{\text{KL}}(P \| P_0) = \frac{1}{2}\left[\frac{\sigma_P^2}{\sigma_0^2} + \frac{(\mu_P - \mu_0)^2}{\sigma_0^2} - 1 + \log\frac{\sigma_0^2}{\sigma_P^2}\right]
    $$

    With $\sigma_P^2 = \sigma_0^2 = 1$, $\mu_P = \mu$, $\mu_0 = 0$:

    $$
    D_{\text{KL}}(N(\mu, 1) \| N(0, 1)) = \frac{1}{2}\left[1 + \mu^2 - 1 + 0\right] = \frac{\mu^2}{2}
    $$

    **Case 2: Changed variance.** Let $P = N(0, \sigma^2)$ and $P_0 = N(0, 1)$:

    $$
    D_{\text{KL}}(N(0, \sigma^2) \| N(0, 1)) = \frac{1}{2}\left[\sigma^2 + 0 - 1 + \log\frac{1}{\sigma^2}\right] = \frac{1}{2}\left[\sigma^2 - 1 - \log \sigma^2\right]
    $$

    **Range of means in $\mathcal{P}_{\text{KL}}(0.5)$ with fixed variance 1:** We need $D_{\text{KL}}(N(\mu, 1) \| N(0,1)) \leq 0.5$, which gives:

    $$
    \frac{\mu^2}{2} \leq 0.5 \implies \mu^2 \leq 1 \implies \mu \in [-1, 1]
    $$

    Therefore, the KL ball of radius 0.5 centered at $N(0,1)$, restricted to distributions with unit variance, allows means in the range $[-1, 1]$.

---

**Exercise 2.** For the $\varepsilon$-contamination set $\mathcal{P}_\varepsilon = \{(1 - \varepsilon) P_0 + \varepsilon Q : Q \in \mathcal{M}_1(\mathbb{R})\}$ with $P_0 = N(0,1)$ and $\varepsilon = 0.1$, compute $\sup_{P \in \mathcal{P}_\varepsilon} \mathbb{E}_P[X]$ and $\inf_{P \in \mathcal{P}_\varepsilon} \mathbb{E}_P[X]$ for a bounded loss function $X$ with $X \in [-10, 10]$. Show that the worst-case measure places its contaminating mass at the extreme point.

??? success "Solution to Exercise 2"

    With $P_0 = N(0,1)$, $\varepsilon = 0.1$, and $X \in [-10, 10]$ bounded.

    For any $P = (1-\varepsilon)P_0 + \varepsilon Q$ in $\mathcal{P}_\varepsilon$:

    $$
    \mathbb{E}_P[X] = (1-\varepsilon)\mathbb{E}_{P_0}[X] + \varepsilon \mathbb{E}_Q[X]
    $$

    **Supremum**: To maximize $\mathbb{E}_P[X]$, we maximize $\mathbb{E}_Q[X]$. Since $X \in [-10, 10]$, the maximum of $\mathbb{E}_Q[X]$ over all probability measures $Q$ is achieved by $Q = \delta_{x^*}$ where $x^*$ is chosen to maximize $X$. Since $X$ is the identity function on $\mathbb{R}$ (restricted to $[-10, 10]$ as a bound on the loss), but more precisely, $X$ itself is a random variable with values in $[-10, 10]$. The contaminating measure $Q$ can place all mass at the point maximizing $X$, which is $x^* = 10$:

    $$
    \sup_{Q} \mathbb{E}_Q[X] = 10 \quad \text{(achieved by } Q = \delta_{10}\text{)}
    $$

    Therefore:

    $$
    \sup_{P \in \mathcal{P}_\varepsilon} \mathbb{E}_P[X] = (1-0.1) \times 0 + 0.1 \times 10 = 1.0
    $$

    **Infimum**: To minimize $\mathbb{E}_P[X]$, we minimize $\mathbb{E}_Q[X]$. The minimum is achieved by $Q = \delta_{-10}$:

    $$
    \inf_{P \in \mathcal{P}_\varepsilon} \mathbb{E}_P[X] = 0.9 \times 0 + 0.1 \times (-10) = -1.0
    $$

    **Worst-case at extremes**: In both cases, the optimal contaminating measure places all its mass at the extreme point of the support of $X$. This is a general property: the worst-case $Q$ in an $\varepsilon$-contamination model is always a point mass (Dirac delta) at the value that maximizes (or minimizes) the objective. This follows because $\mathbb{E}_Q[X]$ is linear in $Q$, and the maximum of a linear functional over all probability measures is attained at an extreme point, which is a Dirac mass.

---

**Exercise 3.** Prove that the total variation ball $\mathcal{P}_{\text{TV}}(\delta) = \{P : \|P - P_0\|_{\text{TV}} \leq \delta\}$ is convex and closed in the weak topology. Then show that for a bounded measurable function $f$ with $\|f\|_\infty \leq M$:

$$
\sup_{P \in \mathcal{P}_{\text{TV}}(\delta)} \mathbb{E}_P[f] = \mathbb{E}_{P_0}[f] + \delta M
$$

??? success "Solution to Exercise 3"

    **Convexity**: Let $P_1, P_2 \in \mathcal{P}_{\text{TV}}(\delta)$ and $\alpha \in [0,1]$. For any $A \in \mathcal{F}$:

    $$
    |(\alpha P_1 + (1-\alpha)P_2)(A) - P_0(A)| = |\alpha(P_1(A) - P_0(A)) + (1-\alpha)(P_2(A) - P_0(A))|
    $$

    $$
    \leq \alpha |P_1(A) - P_0(A)| + (1-\alpha)|P_2(A) - P_0(A)|
    $$

    Taking the supremum over $A$:

    $$
    \|\alpha P_1 + (1-\alpha)P_2 - P_0\|_{\text{TV}} \leq \alpha \|P_1 - P_0\|_{\text{TV}} + (1-\alpha)\|P_2 - P_0\|_{\text{TV}} \leq \alpha \delta + (1-\alpha)\delta = \delta
    $$

    So $\alpha P_1 + (1-\alpha)P_2 \in \mathcal{P}_{\text{TV}}(\delta)$, proving convexity.

    **Closedness in weak topology**: Let $\{P_n\}$ be a sequence in $\mathcal{P}_{\text{TV}}(\delta)$ with $P_n \xrightarrow{w} P$. We need to show $\|P - P_0\|_{\text{TV}} \leq \delta$. By the Portmanteau theorem, for any closed set $F$: $\limsup_n P_n(F) \leq P(F)$. For the TV characterization, note that $\|P - P_0\|_{\text{TV}} = \sup_A |P(A) - P_0(A)|$. The total variation norm is lower semicontinuous with respect to weak convergence:

    $$
    \|P - P_0\|_{\text{TV}} \leq \liminf_n \|P_n - P_0\|_{\text{TV}} \leq \delta
    $$

    (This uses the fact that the TV ball is weakly closed.) Hence $P \in \mathcal{P}_{\text{TV}}(\delta)$.

    **Worst-case expectation**: For bounded $f$ with $\|f\|_\infty \leq M$, we want to show:

    $$
    \sup_{P: \|P - P_0\|_{\text{TV}} \leq \delta} \mathbb{E}_P[f] = \mathbb{E}_{P_0}[f] + \delta M
    $$

    **Upper bound**: For any $P$ with $\|P - P_0\|_{\text{TV}} \leq \delta$:

    $$
    \mathbb{E}_P[f] - \mathbb{E}_{P_0}[f] = \int f \, d(P - P_0) \leq \|f\|_\infty \|P - P_0\|_{\text{TV}} \leq M \delta
    $$

    using the definition of TV distance as the operator norm for bounded functions.

    **Attainment**: We exhibit a measure $P^*$ achieving equality. Write the signed measure $P - P_0 = \delta \cdot \nu$ where $\|\nu\|_{\text{TV}} = 1$. To maximize $\int f \, d\nu$, we need $\nu$ concentrated on $\{f = M\}$ (positive part) and $\{f = -M\}$ (negative part). Specifically, let $A^+ = \arg\max f$ and choose:

    $$
    P^* = P_0 + \delta(\delta_{x^+} - \delta_{x^-})
    $$

    where $x^+ \in \arg\max f$ (with $f(x^+) = M$) and $x^-$ is chosen so that $P^*$ remains a valid probability measure with $\|P^* - P_0\|_{\text{TV}} = \delta$. This construction gives $\mathbb{E}_{P^*}[f] = \mathbb{E}_{P_0}[f] + \delta(M - f(x^-))$, which achieves $\mathbb{E}_{P_0}[f] + \delta M$ when $f(x^-) = -M + M = 0$, or more precisely, the supremum is achieved in the limit by concentrating the positive perturbation where $f$ is maximal.

    More rigorously, $\sup_{\|P - P_0\|_{\text{TV}} \leq \delta} \mathbb{E}_P[f] = \mathbb{E}_{P_0}[f] + \delta \cdot \text{ess sup}_{P_0}(f)$ when $P_0$ has full support, and equals $\mathbb{E}_{P_0}[f] + \delta M$ for $\|f\|_\infty = M$ when the supremum of $f$ is $M$.

---

**Exercise 4.** Consider the robust portfolio optimization problem

$$
\max_w \min_{P \in \mathcal{P}_{\text{KL}}(\theta)} \left\{ w^\top \mathbb{E}_P[R] - \frac{\lambda}{2} w^\top \Sigma_0 w \right\}
$$

with two assets having $\mu_0 = (0.08, 0.12)^\top$ and $\Sigma_0 = \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{pmatrix}$. For $\lambda = 2$ and $\theta = 0.1$, compute the robust optimal portfolio and compare it with the classical Markowitz portfolio (obtained at $\theta = 0$).

??? success "Solution to Exercise 4"

    **Parameters**: $\mu_0 = (0.08, 0.12)^\top$, $\Sigma_0 = \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{pmatrix}$, $\lambda = 2$, $\theta = 0.1$.

    **Classical Markowitz**: With $\theta = 0$ (no ambiguity):

    $$
    w_{\text{MV}} = \frac{1}{\lambda} \Sigma_0^{-1} \mu_0
    $$

    Compute $\Sigma_0^{-1}$: $\det(\Sigma_0) = 0.04 \times 0.09 - 0.01^2 = 0.0036 - 0.0001 = 0.0035$

    $$
    \Sigma_0^{-1} = \frac{1}{0.0035} \begin{pmatrix} 0.09 & -0.01 \\ -0.01 & 0.04 \end{pmatrix} = \begin{pmatrix} 25.714 & -2.857 \\ -2.857 & 11.429 \end{pmatrix}
    $$

    $$
    \Sigma_0^{-1} \mu_0 = \begin{pmatrix} 25.714 \times 0.08 + (-2.857) \times 0.12 \\ (-2.857) \times 0.08 + 11.429 \times 0.12 \end{pmatrix} = \begin{pmatrix} 2.057 - 0.343 \\ -0.229 + 1.371 \end{pmatrix} = \begin{pmatrix} 1.714 \\ 1.143 \end{pmatrix}
    $$

    $$
    w_{\text{MV}} = \frac{1}{2} \begin{pmatrix} 1.714 \\ 1.143 \end{pmatrix} = \begin{pmatrix} 0.857 \\ 0.571 \end{pmatrix}
    $$

    **Robust portfolio**: For the KL uncertainty set, the worst-case mean adjustment for direction $w$ reduces the expected return by $\sqrt{2\theta \cdot w^\top \Sigma_0 w}$. The robust portfolio takes the form:

    $$
    w^* = \frac{1}{\lambda + \kappa} \Sigma_0^{-1} \mu_0
    $$

    where $\kappa = \sqrt{2\theta / (\mu_0^\top \Sigma_0^{-1} \mu_0)}$. Compute:

    $$
    \mu_0^\top \Sigma_0^{-1} \mu_0 = 0.08 \times 1.714 + 0.12 \times 1.143 = 0.1371 + 0.1371 = 0.2743
    $$

    $$
    \kappa = \sqrt{\frac{2 \times 0.1}{0.2743}} = \sqrt{0.7293} = 0.854
    $$

    $$
    w^* = \frac{1}{2 + 0.854} \begin{pmatrix} 1.714 \\ 1.143 \end{pmatrix} = \frac{1}{2.854} \begin{pmatrix} 1.714 \\ 1.143 \end{pmatrix} = \begin{pmatrix} 0.601 \\ 0.400 \end{pmatrix}
    $$

    **Comparison**: The robust portfolio is:

    $$
    w^* = \frac{\lambda}{\lambda + \kappa} w_{\text{MV}} = \frac{2}{2.854} w_{\text{MV}} \approx 0.701 \times w_{\text{MV}}
    $$

    Positions are shrunk by about 30%. Asset 1 drops from $0.857$ to $0.601$, and asset 2 from $0.571$ to $0.400$. The ambiguity parameter $\theta = 0.1$ effectively increases risk aversion from $\lambda = 2$ to $\lambda + \kappa \approx 2.854$, reflecting the decision maker's caution about the estimated mean returns.

---

**Exercise 5.** Derive the exponential tilting solution for the problem $\min_{P} \mathbb{E}_P[X]$ subject to $D_{\text{KL}}(P \| P_0) \leq \theta$. Starting from the Lagrangian $\mathcal{L}(P, \lambda) = \mathbb{E}_P[X] + \lambda(D_{\text{KL}}(P \| P_0) - \theta)$, show that the optimal density ratio is $dP^*/dP_0 \propto e^{-X/\lambda^*}$ and explain how $\lambda^*$ is determined by the constraint $D_{\text{KL}}(P^* \| P_0) = \theta$.

??? success "Solution to Exercise 5"

    **Lagrangian formulation**: We want to solve:

    $$
    \min_P \mathbb{E}_P[X] \quad \text{subject to} \quad D_{\text{KL}}(P \| P_0) \leq \theta, \quad \mathbb{E}_{P_0}\left[\frac{dP}{dP_0}\right] = 1
    $$

    The Lagrangian is (with multiplier $\lambda \geq 0$ for the KL constraint):

    $$
    \mathcal{L}(P, \lambda) = \mathbb{E}_P[X] + \lambda(D_{\text{KL}}(P \| P_0) - \theta)
    $$

    Writing $Z = dP/dP_0$ and expanding:

    $$
    \mathcal{L}(Z, \lambda) = \mathbb{E}_{P_0}[ZX] + \lambda\left(\mathbb{E}_{P_0}[Z\log Z] - \theta\right)
    $$

    subject to $\mathbb{E}_{P_0}[Z] = 1$, $Z \geq 0$.

    **Variational derivative**: Introduce Lagrange multiplier $\nu$ for the normalization constraint. The augmented Lagrangian is:

    $$
    \tilde{\mathcal{L}} = \mathbb{E}_{P_0}[ZX + \lambda Z \log Z + \nu Z] - \lambda\theta - \nu
    $$

    Setting the functional derivative with respect to $Z(\omega)$ to zero:

    $$
    X(\omega) + \lambda(\log Z(\omega) + 1) + \nu = 0
    $$

    Solving for $Z$:

    $$
    Z(\omega) = \exp\left(-\frac{X(\omega)}{\lambda} - 1 - \frac{\nu}{\lambda}\right)
    $$

    **Normalization**: The constraint $\mathbb{E}_{P_0}[Z] = 1$ determines the constant:

    $$
    e^{-1 - \nu/\lambda} \cdot \mathbb{E}_{P_0}\left[e^{-X/\lambda}\right] = 1 \implies e^{-1-\nu/\lambda} = \frac{1}{\mathbb{E}_{P_0}[e^{-X/\lambda}]}
    $$

    Therefore the optimal density ratio is:

    $$
    \frac{dP^*}{dP_0} = \frac{e^{-X/\lambda^*}}{\mathbb{E}_{P_0}[e^{-X/\lambda^*}]}
    $$

    **Determining $\lambda^*$**: By complementary slackness, either $\lambda^* = 0$ (and the constraint is not active) or $D_{\text{KL}}(P^* \| P_0) = \theta$ (constraint is binding). When the constraint binds:

    $$
    D_{\text{KL}}(P^* \| P_0) = \mathbb{E}_{P^*}\left[\log\frac{dP^*}{dP_0}\right] = \mathbb{E}_{P^*}\left[-\frac{X}{\lambda^*} - \log \mathbb{E}_{P_0}[e^{-X/\lambda^*}]\right]
    $$

    $$
    = -\frac{\mathbb{E}_{P^*}[X]}{\lambda^*} - \log \mathbb{E}_{P_0}[e^{-X/\lambda^*}] = \theta
    $$

    This is a single equation in $\lambda^*$ that can be solved numerically. As $\lambda^* \to 0^+$, the KL divergence grows to infinity (the tilting becomes extreme). As $\lambda^* \to \infty$, the KL divergence goes to 0 (the tilting vanishes). By continuity and monotonicity, there exists a unique $\lambda^*$ satisfying $D_{\text{KL}}(P^* \| P_0) = \theta$.

    The solution is an **exponential tilting** (also called Esscher transform) that reweights the reference measure $P_0$ by exponentially penalizing high values of $X$ (since we are minimizing $\mathbb{E}_P[X]$). States where $X$ is large get downweighted, and states where $X$ is small get upweighted, consistent with a pessimistic worst-case measure.

---

**Exercise 6.** Explain why rectangularity of $\mathcal{P}$ is necessary for dynamic consistency with maxmin preferences. Construct a simple two-period example with $\Omega = \{uu, ud, du, dd\}$ where the set $\mathcal{P} = \{P_1, P_2\}$ is not rectangular, and demonstrate that the optimal strategy chosen at $t = 0$ differs from the strategy the agent would choose at $t = 1$ upon reaching a particular node.

??? success "Solution to Exercise 6"

    **Why rectangularity is necessary**: Consider maxmin preferences $V_t(f) = \min_{P \in \mathcal{P}} \mathbb{E}_P[u(f) | \mathcal{F}_t]$. Dynamic consistency requires that if a plan is optimal at $t = 0$, the agent does not want to deviate at $t = 1$.

    Suppose $\mathcal{P}$ is not rectangular. Then there exist measures $P_1, P_2 \in \mathcal{P}$ and a node at $t=1$ such that one cannot freely combine $P_1$'s conditional at one node with $P_2$'s conditional at another node. This means the worst-case measure at $t=0$ (which jointly optimizes over both periods) may differ from the measure that is worst case conditional on reaching a particular node at $t=1$.

    **Two-period example**: Let $\Omega = \{uu, ud, du, dd\}$, with $\mathcal{F}_1 = \sigma(\{uu,ud\}, \{du,dd\})$.

    Define $P_1$ and $P_2$ as:

    | State | $P_1$ | $P_2$ |
    |-------|-------|-------|
    | $uu$ | $0.3 \times 0.5 = 0.15$ | $0.7 \times 0.8 = 0.56$ |
    | $ud$ | $0.3 \times 0.5 = 0.15$ | $0.7 \times 0.2 = 0.14$ |
    | $du$ | $0.7 \times 0.6 = 0.42$ | $0.3 \times 0.4 = 0.12$ |
    | $dd$ | $0.7 \times 0.4 = 0.28$ | $0.3 \times 0.6 = 0.18$ |

    So $P_1(u_1) = 0.3$, $P_1(u_2|u_1) = 0.5$, $P_1(u_2|d_1) = 0.6$; and $P_2(u_1) = 0.7$, $P_2(u_2|u_1) = 0.8$, $P_2(u_2|d_1) = 0.4$.

    **Non-rectangularity**: To check, try to paste $P_1$'s conditional at node $u_1$ with $P_2$'s conditional at node $d_1$ and $P_1$'s marginal. This would give $R(u_1) = 0.3$, $R(u_2|u_1) = 0.5$, $R(u_2|d_1) = 0.4$. But $R \notin \{P_1, P_2\}$ since $P_1$ has $P_1(u_2|d_1) = 0.6 \neq 0.4$ and $P_2$ has $P_2(u_1) = 0.7 \neq 0.3$. So $\mathcal{P}$ is not rectangular.

    **Dynamic inconsistency**: Consider the act $f(uu) = 10$, $f(ud) = 0$, $f(du) = 0$, $f(dd) = 10$ with $u(x) = x$.

    At $t = 0$:

    $$
    \mathbb{E}_{P_1}[f] = 0.15 \times 10 + 0.28 \times 10 = 4.3
    $$

    $$
    \mathbb{E}_{P_2}[f] = 0.56 \times 10 + 0.18 \times 10 = 7.4
    $$

    $\min = 4.3$ (worst case is $P_1$).

    Now at $t = 1$, suppose we reach node $u_1$. Under $P_1$: $\mathbb{E}_{P_1}[f|u_1] = 0.5 \times 10 + 0.5 \times 0 = 5$. Under $P_2$: $\mathbb{E}_{P_2}[f|u_1] = 0.8 \times 10 + 0.2 \times 0 = 8$. The worst case at node $u_1$ is $P_1$ with value 5.

    But if the agent could use $P_2$'s conditional at $d_1$ (which gives $\mathbb{E}_{P_2}[f|d_1] = 0.4 \times 0 + 0.6 \times 10 = 6$) and $P_1$'s conditional at $u_1$ (value 5), the overall worst case would combine different conditionals at different nodes, which is impossible with a non-rectangular set. The worst-case measure at $t=0$ ($P_1$) imposes conditionals at both nodes simultaneously, but the agent at node $u_1$ might prefer to evaluate robustness differently than what $P_1$'s conditional prescribes.

    This creates a tension: the continuation strategy embedded in the $t=0$ plan (based on $P_1$ being worst case globally) may not match the strategy the agent would choose at $t=1$ (where the worst-case conditional measure might differ). This is the failure of dynamic consistency.

---

**Exercise 7.** Compare Wasserstein balls and KL divergence balls as uncertainty sets. For the discrete distribution $P_0 = \frac{1}{3}\delta_1 + \frac{1}{3}\delta_2 + \frac{1}{3}\delta_3$ on $\{1, 2, 3\}$, describe the sets $\mathcal{P}_W(0.5) = \{P : W_1(P, P_0) \leq 0.5\}$ and $\mathcal{P}_{\text{KL}}(0.5) = \{P : D_{\text{KL}}(P \| P_0) \leq 0.5\}$. Which set is larger? Which leads to more conservative worst-case expectations for $f(x) = x^2$?

??? success "Solution to Exercise 7"

    **Setup**: $P_0 = \frac{1}{3}\delta_1 + \frac{1}{3}\delta_2 + \frac{1}{3}\delta_3$ on $\{1, 2, 3\}$ with $d(x,y) = |x-y|$.

    **KL ball**: $\mathcal{P}_{\text{KL}}(0.5) = \{P : D_{\text{KL}}(P \| P_0) \leq 0.5\}$. Since $P_0$ is supported on $\{1,2,3\}$, any $P \ll P_0$ must also be supported on $\{1,2,3\}$. Write $P = (p_1, p_2, p_3)$ with $p_i \geq 0$, $\sum p_i = 1$.

    $$
    D_{\text{KL}}(P \| P_0) = \sum_{i=1}^3 p_i \log\frac{p_i}{1/3} = \sum_{i=1}^3 p_i \log(3p_i) = \log 3 + \sum_{i=1}^3 p_i \log p_i
    $$

    The constraint $D_{\text{KL}}(P \| P_0) \leq 0.5$ defines a convex subset of the probability simplex in $\mathbb{R}^3$. The set is bounded within $\{1,2,3\}$ and cannot include any mass outside these three points.

    **Wasserstein ball**: $\mathcal{P}_W(0.5) = \{P : W_1(P, P_0) \leq 0.5\}$. Unlike the KL ball, the Wasserstein ball allows $P$ to place mass on points other than $\{1,2,3\}$. For instance, $P$ could place mass at $x = 0.5$ or $x = 3.5$, as long as the total transport cost is at most 0.5.

    A measure $P$ in the Wasserstein ball can move each atom of $P_0$ by at most a total average distance of 0.5. For example, $P = \frac{1}{3}\delta_{0.5} + \frac{1}{3}\delta_2 + \frac{1}{3}\delta_3$ has $W_1(P, P_0) = \frac{1}{3} \times 0.5 = 0.167 \leq 0.5$, so this is in the Wasserstein ball. Similarly, $P = \frac{1}{3}\delta_1 + \frac{1}{3}\delta_2 + \frac{1}{3}\delta_{4.5}$ has $W_1 = \frac{1}{3} \times 1.5 = 0.5$, which is exactly on the boundary.

    **Which set is larger?** The Wasserstein ball is larger in the sense that it contains distributions not supported on $\{1,2,3\}$, whereas the KL ball is restricted to this support. Within the simplex over $\{1,2,3\}$, the comparison depends on the specific radii, but the key structural difference is that the Wasserstein ball explores a much richer set of distributions.

    **Worst-case $\mathbb{E}_P[f]$ for $f(x) = x^2$**:

    *KL ball*: Restricted to $\{1,2,3\}$, we maximize $p_1 \cdot 1 + p_2 \cdot 4 + p_3 \cdot 9$ subject to $D_{\text{KL}}(P \| P_0) \leq 0.5$. The maximum is achieved by shifting mass toward $x = 3$ (highest $f$ value). Using exponential tilting, the worst case is $p_i^* \propto \frac{1}{3} e^{\lambda x_i^2}$, where $\lambda$ is chosen to saturate the KL constraint. The reference expectation is $\mathbb{E}_{P_0}[f] = \frac{1}{3}(1 + 4 + 9) = \frac{14}{3} \approx 4.667$.

    Numerically, with the KL constraint at 0.5, the worst-case $P^*$ shifts mass toward $x = 3$, giving approximately $p_3^* \approx 0.56$, $p_2^* \approx 0.29$, $p_1^* \approx 0.15$, and $\mathbb{E}_{P^*}[x^2] \approx 0.15 + 1.16 + 5.04 = 6.35$.

    *Wasserstein ball*: The worst case can move mass to points beyond $\{1,2,3\}$. For instance, moving the atom at $x = 3$ to $x = 4.5$ (distance 1.5, transport cost $\frac{1}{3} \times 1.5 = 0.5$) gives $f(4.5) = 20.25$. This yields $\mathbb{E}[f] = \frac{1}{3}(1 + 4 + 20.25) = 8.42$.

    Even better, we could move all three atoms rightward: move $x=1$ to $x=2.5$, $x=2$ to $x=3.5$, $x=3$ to $x=4.5$, each by 1.5, but average transport $= 1.5 > 0.5$, so this exceeds the budget. Optimally, concentrate the transport on the atom where $f$ has the highest marginal return. Since $f(x) = x^2$ is convex and increasing for $x > 0$, moving the rightmost atom yields the greatest increase. Moving atom at $x = 3$ rightward by $\Delta$ costs $\frac{1}{3}\Delta$ in transport and gains $\frac{1}{3}((3+\Delta)^2 - 9)$ in expectation. Setting $\frac{1}{3}\Delta = 0.5$ gives $\Delta = 1.5$, and the gain is $\frac{1}{3}(20.25 - 9) = 3.75$.

    So the Wasserstein worst-case $\mathbb{E}[x^2] \approx 4.667 + 3.75 = 8.42$.

    **Conclusion**: The Wasserstein ball leads to a more conservative (higher) worst-case expectation ($\approx 8.42$) compared to the KL ball ($\approx 6.35$) for the convex function $f(x) = x^2$. This is because the Wasserstein ball can move mass to locations with arbitrarily high values of $f$, while the KL ball can only reweight existing atoms. For convex loss functions, this support extension property makes Wasserstein-based ambiguity fundamentally more conservative.
