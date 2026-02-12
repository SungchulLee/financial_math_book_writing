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



### 2. $\phi$-Divergences


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
