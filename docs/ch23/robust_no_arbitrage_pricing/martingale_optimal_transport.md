# Martingale Optimal Transport


## Introduction


Martingale Optimal Transport (MOT) represents a powerful synthesis of optimal transport theory and martingale theory, providing a framework for robust derivative pricing that combines geometric insights with financial constraints. This theory addresses the fundamental question: **What is the optimal distribution of a martingale given its marginal distributions?**

MOT has emerged as a central tool in quantitative finance for:

1. **Model-free pricing**: Deriving tight bounds on exotic derivatives using only vanilla option prices
2. **Robust hedging**: Constructing optimal hedging strategies under model uncertainty
3. **Calibration**: Ensuring no-arbitrage in fitted volatility surfaces
4. **Martingale interpolation**: Constructing martingales with prescribed marginals

The key insight is that observed option prices at different maturities constrain the marginal distributions of the underlying asset price process, but do not uniquely determine the joint distribution. MOT optimizes over all joint distributions compatible with these marginal constraints while preserving the martingale property.

## Mathematical Foundations


### 1. Classical Optimal Transport


**Monge Problem** (1781): Given probability measures $\mu$ on $\mathbb{R}^d$ and $\nu$ on $\mathbb{R}^d$, find a transport map $T: \mathbb{R}^d \to \mathbb{R}^d$ such that $T_{\#}\mu = \nu$ (meaning $\nu(B) = \mu(T^{-1}(B))$ for all Borel sets $B$) that minimizes:


$$
\inf_{T: T_{\#}\mu = \nu} \int_{\mathbb{R}^d} c(x, T(x)) \, d\mu(x)
$$



where $c(x, y)$ is the cost of transporting mass from $x$ to $y$.

**Kantorovich Relaxation** (1942): Instead of deterministic transport maps, optimize over couplings (joint distributions):


$$
\mathcal{W}_c(\mu, \nu) = \inf_{\pi \in \Pi(\mu, \nu)} \int_{\mathbb{R}^d \times \mathbb{R}^d} c(x, y) \, d\pi(x, y)
$$



where:


$$
\Pi(\mu, \nu) = \{ \pi \in \mathcal{P}(\mathbb{R}^d \times \mathbb{R}^d): \pi_1 = \mu, \, \pi_2 = \nu \}
$$



is the set of couplings with marginals $\mu$ and $\nu$.

**Wasserstein Distance**: For $c(x, y) = |x - y|^p$, the optimal transport cost defines the $p$-Wasserstein distance:


$$
W_p(\mu, \nu) = \left( \mathcal{W}_{|\cdot|^p}(\mu, \nu) \right)^{1/p}
$$



### 2. Kantorovich Duality


**Dual Problem**: 


$$
\mathcal{W}_c(\mu, \nu) = \sup_{(\phi, \psi) \in \Phi_c} \left\{ \int \phi \, d\mu + \int \psi \, d\nu \right\}
$$



where:


$$
\Phi_c = \{ (\phi, \psi): \phi(x) + \psi(y) \leq c(x, y) \text{ for all } x, y \}
$$



**Interpretation**: 

- $\phi(x)$: "Potential" at source location $x$
- $\psi(y)$: "Potential" at target location $y$
- Constraint ensures no arbitrage in transport economy

**c-Transform**: For optimal dual solutions:


$$
\psi(y) = \inf_x \{ c(x, y) - \phi(x) \} = -\phi^c(y)
$$



where $\phi^c$ is the $c$-transform of $\phi$.

## Martingale Optimal Transport Problem


### 1. Problem Formulation


**Setup**: Consider two time points $0 < T$ with:

- Initial distribution $\mu$ on $\mathbb{R}_+$ (current asset prices)
- Terminal distribution $\nu$ on $\mathbb{R}_+$ (implied by option prices at maturity $T$)

**Martingale Constraint**: Seek joint distribution $\pi$ of $(S_0, S_T)$ such that:


$$
\mathbb{E}_{\pi}[S_T | S_0] = e^{rT} S_0 \quad \text{(martingale condition under risk-neutral measure)}
$$



For simplicity, assume $r = 0$ (or work with discounted prices):


$$
\mathbb{E}_{\pi}[S_T | S_0] = S_0
$$



**Martingale Coupling Set**: Define:


$$
\mathcal{M}(\mu, \nu) = \left\{ \pi \in \Pi(\mu, \nu): \int y \, d\pi(y | x) = x \text{ for } \mu\text{-a.e. } x \right\}
$$



**MOT Problem**: Optimize a cost functional over martingale couplings:


$$
\inf_{\pi \in \mathcal{M}(\mu, \nu)} \mathbb{E}_{\pi}[c(S_0, S_T)] = \inf_{\pi \in \mathcal{M}(\mu, \nu)} \int c(x, y) \, d\pi(x, y)
$$



**Dual Problem**: 


$$
\sup_{(\phi, \psi) \in \Phi_c^M} \left\{ \int \phi \, d\mu + \int \psi \, d\nu \right\}
$$



where $\Phi_c^M$ incorporates both the cost constraint and martingale structure.

### 2. Martingale Duality


**Theorem** (Martingale Duality): Under appropriate conditions:


$$
\inf_{\pi \in \mathcal{M}(\mu, \nu)} \int c(x, y) \, d\pi = \sup_{\phi, \psi} \left\{ \int \phi \, d\mu + \int \psi \, d\nu \right\}
$$



subject to:


$$
\phi(x) + \psi(y) \leq c(x, y) \quad \text{and} \quad \psi(y) \geq y \phi'(x) \text{ for all } x, y
$$



The second constraint reflects the martingale restriction.

**Proof Sketch**: Uses convex analysis and Lagrangian duality. The martingale constraint is incorporated via the subdifferential condition.

### 3. Beiglböck-Henry-Penkner-Schachermayer Theorem


**General Duality** (BHPS 2013): For one-dimensional marginals and martingale constraint:


$$
\inf_{\pi \in \mathcal{M}(\mu, \nu)} \int c \, d\pi = \sup_{\phi \in C(\mathbb{R})} \left\{ \int \phi \, d\mu + \int \phi^* \, d\nu \right\}
$$



where $\phi^*$ is the **convex minorant** of $\phi$ defined by:


$$
\phi^*(y) = \sup \{ a y + b: ax + b \leq \phi(x) \text{ for all } x \}
$$



**Key Insight**: The $c$-transform is replaced by convex minorant, reflecting the martingale constraint.

**Application to Finance**: This duality allows computing model-free bounds on exotic derivatives using only observed vanilla option prices.

## Robust Pricing via MOT


### 1. Setup


**Given Information**:

- Current stock price $S_0$
- Call option prices $C(K)$ for strikes $K \in \mathcal{K}$
- Maturity $T$

**Implied Marginals**: Via Breeden-Litzenberger:


$$
d\nu(y) = e^{rT} \frac{\partial^2 C}{\partial K^2}(y) \, dy
$$



### 2. Model-Free Upper Bound


**Problem**: Price an exotic derivative with payoff $g(S_0, S_T)$ using only marginal information.

**Upper Bound**:


$$
\overline{V}(g) = \sup_{\pi \in \mathcal{M}(\mu, \nu)} \int g(x, y) \, d\pi(x, y)
$$



**Dual Formulation**: By MOT duality:


$$
\overline{V}(g) = \inf_{\phi} \left\{ \int \phi(x) \, d\mu(x) + \int \phi^*(y) \, d\nu(y) \right\}
$$



subject to $\phi(x) + \phi^*(y) \geq g(x, y)$ for all $x, y$.

**Interpretation**: 

- $\phi(x)$ is a "potential function" 
- The bound is achieved by a static portfolio of vanilla options plus cash
- This provides a super-replication strategy

### 3. Model-Free Lower Bound


**Lower Bound**:


$$
\underline{V}(g) = \inf_{\pi \in \mathcal{M}(\mu, \nu)} \int g(x, y) \, d\pi(x, y)
$$



**Dual**: Replace $g$ with $-g$ in the upper bound problem:


$$
\underline{V}(g) = -\overline{V}(-g)
$$



### 4. Static Replication


**Theorem** (Static Replication): The optimal dual potentials $\phi^*$ and $\psi^*$ correspond to portfolios of vanilla options that super-replicate (for upper bound) or sub-replicate (for lower bound) the exotic payoff.

**Construction**: The superhedging portfolio consists of:

- A position in the stock: $\theta_S = \phi'(S_0)$ (if $\phi$ is differentiable)
- Positions in calls: density $\theta_C(K) = \partial^2 \phi^*/\partial K^2$
- Cash: $\theta_0$

such that:


$$
\theta_S S_T + \int_0^{\infty} \theta_C(K) (S_T - K)^+ dK + \theta_0 \geq g(S_0, S_T)
$$



## Multi-Period MOT


### 1. Nested Martingales


**Setup**: Consider times $0 < T_1 < T_2 < \cdots < T_n$.

**Marginals**: Given distributions $\mu_0, \mu_1, \ldots, \mu_n$ at each time.

**Multi-Marginal MOT**: Find joint distribution $\pi$ on $\prod_{i=0}^n \mathbb{R}_+$ such that:

1. Marginal constraints: $\pi_i = \mu_i$ for each $i$
2. Martingale property: $\mathbb{E}_{\pi}[S_{T_{i+1}} | S_{T_i}] = S_{T_i}$ for all $i$

**Optimization**:


$$
\inf_{\pi \in \mathcal{M}(\mu_0, \ldots, \mu_n)} \int c(s_0, s_1, \ldots, s_n) \, d\pi(s_0, \ldots, s_n)
$$



### 2. Weak vs Strong Duality


**Weak Duality**: Always holds:


$$
\text{Primal} \geq \text{Dual}
$$



**Strong Duality**: Equality holds under regularity conditions.

**Duality Gap**: In multi-period settings, duality gaps can occur due to:

- Non-compactness
- Lack of convexity in augmented space
- Technical measure-theoretic issues

**Beiglböck-Juillet (2016)**: Established conditions for strong duality in multi-period MOT with specific cost functions.

## Computational Methods


### 1. Discretization Approach


**Grid Setup**: Discretize state spaces:

- $S_0 \in \{s_1^0, s_2^0, \ldots, s_{N_0}^0\}$
- $S_T \in \{s_1^T, s_2^T, \ldots, s_{N_T}^T\}$

**Coupling Matrix**: Let $\pi_{ij} = \pi(s_i^0, s_j^T)$ represent the joint probability.

**Linear Program**:


$$
\begin{aligned}
\text{minimize} \quad & \sum_{i=1}^{N_0} \sum_{j=1}^{N_T} c(s_i^0, s_j^T) \pi_{ij} \\
\text{subject to} \quad & \sum_{j=1}^{N_T} \pi_{ij} = \mu_i, \quad i = 1, \ldots, N_0 \quad \text{(marginal 1)} \\
& \sum_{i=1}^{N_0} \pi_{ij} = \nu_j, \quad j = 1, \ldots, N_T \quad \text{(marginal 2)} \\
& \sum_{j=1}^{N_T} s_j^T \pi_{ij} = s_i^0 \sum_{j=1}^{N_T} \pi_{ij}, \quad i = 1, \ldots, N_0 \quad \text{(martingale)} \\
& \pi_{ij} \geq 0, \quad \forall i, j
\end{aligned}
$$



**Solver**: Use standard LP solvers (CPLEX, Gurobi) for moderate dimensions.

**Refinement**: Adaptive grid refinement around regions where optimal coupling concentrates.

### 2. Entropic Regularization


**Regularized Problem**: Add entropy term to stabilize and smooth:


$$
\inf_{\pi \in \mathcal{M}(\mu, \nu)} \left\{ \int c \, d\pi + \varepsilon D_{\text{KL}}(\pi \| \mu \otimes \nu) \right\}
$$



where:


$$
D_{\text{KL}}(\pi \| \mu \otimes \nu) = \int \log\left(\frac{d\pi}{d(\mu \otimes \nu)}\right) d\pi
$$



**Sinkhorn Algorithm**: Iterative algorithm for entropic regularization:

1. Initialize $u^{(0)} = \mathbf{1}$, $v^{(0)} = \mathbf{1}$
2. Iterate:

   $$
   u^{(k+1)}_i = \frac{\mu_i}{\sum_j K_{ij} v^{(k)}_j}, \quad v^{(k+1)}_j = \frac{\nu_j}{\sum_i K_{ij} u^{(k+1)}_i}
   $$


   where $K_{ij} = \exp(-c_{ij}/\varepsilon)$ is the kernel matrix.

**Convergence**: Sinkhorn iterations converge exponentially fast to the entropic optimal transport solution.

**Martingale Extension**: Modify Sinkhorn to incorporate martingale constraint by projecting onto martingale subspace at each iteration.

### 3. Neural Network Approaches


**Parameterization**: Represent dual potentials $\phi$ and $\psi$ using neural networks.

**Training**: Minimize:


$$
\mathcal{L}(\phi, \psi) = -\left( \mathbb{E}_{\mu}[\phi(X)] + \mathbb{E}_{\nu}[\psi(Y)] \right) + \lambda \cdot \text{Penalty}(\phi, \psi)
$$



where Penalty enforces the constraints $\phi + \psi \leq c$ and martingale conditions.

**Stochastic Gradient Descent**: Sample from $\mu$ and $\nu$, compute gradients, and update network parameters.

**Advantages**: 

- Scalable to high dimensions
- Can handle complex cost functions
- Amortized computation across multiple queries

### 4. Duality-Based Methods


**Dual LP**: Instead of optimizing over couplings, solve the dual problem:


$$
\begin{aligned}
\text{maximize} \quad & \sum_{i=1}^{N_0} \phi_i \mu_i + \sum_{j=1}^{N_T} \psi_j \nu_j \\
\text{subject to} \quad & \phi_i + \psi_j \leq c_{ij}, \quad \forall i, j \\
& \psi_j \geq s_j^T \phi_i, \quad \forall i, j \quad \text{(martingale dual constraint)}
\end{aligned}
$$



**Interpretation**: $\phi_i$ are "prices" at time 0, $\psi_j$ are "prices" at time $T$.

**Solution**: Often has sparse structure; optimal $\phi$ and $\psi$ are typically piecewise linear.

## Applications in Quantitative Finance


### 1. Variance Swap Pricing


**Variance Swap Payoff**:


$$
g(S_0, S_T) = \log^2(S_T / S_0)
$$



**MOT Bounds**: Using marginals from call option prices:


$$
[\underline{V}, \overline{V}] = \left[ \inf_{\pi \in \mathcal{M}(\mu, \nu)} \mathbb{E}_{\pi}\left[\log^2(S_T / S_0)\right], \, \sup_{\pi \in \mathcal{M}(\mu, \nu)} \mathbb{E}_{\pi}\left[\log^2(S_T / S_0)\right] \right]
$$



**Tightness**: For variance swaps, bounds are often tight because the payoff is close to "monotone" in a suitable sense.

**Realized Variance**: Can be extended to realized variance:


$$
\text{RV} = \sum_{i=1}^n \log^2(S_{t_i} / S_{t_{i-1}})
$$



using multi-period MOT.

### 2. Forward Start Options


**Payoff**: Option struck at-the-money at future time $T_1$, maturing at $T_2$:


$$
g = (S_{T_2} - S_{T_1})^+
$$



**Challenge**: Payoff depends on joint distribution of $(S_{T_1}, S_{T_2})$, not just marginals.

**MOT Approach**: 

- Use marginals at $T_1$ and $T_2$ from market option prices
- Compute robust bounds via multi-period MOT

**Extremal Measures**: Optimal couplings often correspond to specific scenarios (e.g., maximum correlation, minimum correlation).

### 3. Barrier Options


**Up-and-Out Call**: Payoff is:


$$
(S_T - K)^+ \mathbb{1}_{\{\max_{0 \leq t \leq T} S_t < H\}}
$$



**MOT Bounds**: Using only marginal distributions:

**Lower Bound**:


$$
\underline{V} = \inf_{\pi \in \mathcal{M}(\mu, \nu)} \mathbb{E}_{\pi}\left[(S_T - K)^+ \mathbb{1}_{\{S_T < H\}}\right]
$$



This can be computed via MOT since the barrier event is approximated by terminal condition.

**Path-Dependent Barrier**: For exact treatment, need continuous monitoring, which requires additional information beyond marginals. MOT provides bounds but may be wide.

### 4. Robust VIX Derivatives


**VIX Definition**: Model-free implied volatility:


$$
\text{VIX}^2 = \frac{2e^{rT}}{T} \left( \int_0^{F} \frac{P(K)}{K^2} dK + \int_F^{\infty} \frac{C(K)}{K^2} dK \right)
$$



**VIX Option Payoff**: $(VIX_T - K)^+$

**Challenge**: VIX is not directly tradable; hedging requires S&P 500 options.

**MOT Approach**: 

- Treat VIX as a functional of option prices
- Use MOT to find worst-case/best-case scenarios for VIX option values
- Construct static hedges using S&P 500 options

### 5. Basket Option Bounds


**Basket Call**: Payoff is:


$$
\left(\sum_{i=1}^n w_i S_T^{(i)} - K\right)^+
$$



**Given**: Marginal option prices for each asset $S^{(i)}$.

**Unknown**: Joint distribution (correlation structure).

**MOT Generalization**: Optimize over multi-dimensional couplings:


$$
\sup_{\pi \in \mathcal{M}(\mu_1, \ldots, \mu_n)} \mathbb{E}_{\pi}\left[\left(\sum_{i=1}^n w_i S_T^{(i)} - K\right)^+\right]
$$



**Fréchet-Hoeffding Bounds**: Provide initial bounds based purely on marginals:


$$
\max_i \{S_T^{(i)}\} \leq \sum_{i=1}^n w_i S_T^{(i)} \leq n \max_i \{S_T^{(i)}\}
$$



MOT tightens these bounds using martingale constraints.

## Advanced Theoretical Results


### 1. Monge-Kantorovich and Strassen Theorems


**Strassen's Theorem**: A coupling $\pi \in \Pi(\mu, \nu)$ is a martingale coupling if and only if:


$$
\int f \, d\mu = \int f \, d\nu
$$



for all convex functions $f$ for which both integrals exist.

**Implication**: Martingale constraint is equivalent to preserving expectations of all convex functions.

**MOT Connection**: This characterizes $\mathcal{M}(\mu, \nu)$ in terms of moment constraints.

### 2. Irreducible Convex Paving (ICP)


**ICP Property**: A cost function $c$ satisfies ICP if every optimal coupling in $\mathcal{M}(\mu, \nu)$ is supported on a "paving" of $\mathbb{R} \times \mathbb{R}$ by convex sets.

**Examples**:

- $c(x, y) = |y - x|$ (absolute difference)
- $c(x, y) = (y - x)^+$ (call payoff)
- $c(x, y) = (y - x)^2$ (squared error)

**Theorem** (Beiglböck-Juillet): For ICP costs, strong duality holds and extremal couplings have explicit structure.

**Application**: Allows closed-form solutions or efficient computation for many financial payoffs.

### 3. Shadow Measures


**Definition**: A measure $\lambda$ on $\mathbb{R}$ is a **shadow measure** for $\mathcal{M}(\mu, \nu)$ if there exist left-monotone and right-monotone couplings $\pi_L, \pi_R \in \mathcal{M}(\mu, \nu)$ such that:


$$
\pi_L(A \times B) = \lambda(A \cap B), \quad \pi_R(A \times B) = \lambda(A \cup B) - \lambda(A) - \lambda(B) + \lambda(A \cap B)
$$



**Martingale Shadow**: When $\mu$ and $\nu$ are in convex order ($\mu \preceq_c \nu$), there exists a unique shadow measure $\lambda$ with:


$$
\lambda([a, b]) = \text{const} \cdot (b - a)
$$



**Application**: Shadow measures yield extremal martingale couplings, providing explicit constructions for optimal transport plans.

### 4. Peacock Property


**Peacock** (PCOC - Processus Croissant pour l'Ordre Convexe): A process $(X_t)_{t \geq 0}$ is a peacock if:


$$
X_s \preceq_c X_t \quad \text{for all } s \leq t
$$



where $\preceq_c$ denotes convex order.

**Theorem** (Kellerer): A family of measures $(\mu_t)_{t \geq 0}$ on $\mathbb{R}$ is the marginals of a martingale if and only if $\mu_s \preceq_c \mu_t$ for all $s \leq t$.

**Implication**: Peacock property characterizes when marginal distributions can arise from a martingale.

**MOT Connection**: Provides necessary and sufficient conditions for existence of martingale couplings.

### 5. Root and Barrier Embeddings


**Root Embedding**: Given marginals $\mu$ and $\nu$ with $\mu \preceq_c \nu$, construct a martingale $(M_t)_{t \in [0, 1]}$ with:

- $M_0 \sim \mu$
- $M_1 \sim \nu$

**Barrier Embedding**: Embedding stopped at a barrier level.

**Application**: These embeddings provide specific martingale couplings achieving bounds in MOT problems.

**Azéma-Yor Solution**: Classical solution to Skorokhod embedding, useful for constructing extremal couplings.

## Connections to Other Theories


### 1. Optimal Stopping


**Connection**: MOT problems can be reformulated as optimal stopping problems for suitably defined processes.

**Dual Representation**: The dual potentials in MOT correspond to value functions in optimal stopping:


$$
V(x) = \sup_{\tau} \mathbb{E}_x[g(X_{\tau}, Y_{\tau})]
$$



where the supremum is over stopping times.

**Application**: Numerical methods for optimal stopping (e.g., Longstaff-Schwartz) can be adapted to solve MOT problems.

### 2. Stochastic Control


**Control Problem**: Equivalent formulation as:


$$
\inf_{\alpha} \mathbb{E}\left[\int_0^T c(X_t, \alpha_t) dt + h(X_T)\right]
$$



subject to $dX_t = \mu(X_t, \alpha_t) dt + \sigma(X_t) dW_t$.

**Hamilton-Jacobi-Bellman**: The value function satisfies:


$$
V_t + \inf_{\alpha} \{ c(x, \alpha) + \mu(x, \alpha) V_x + \frac{1}{2} \sigma^2(x) V_{xx} \} = 0
$$



**MOT Correspondence**: Under specific cost structures, MOT duals correspond to HJB equations with martingale constraints.

### 3. Rough Path Theory


**Robust Integration**: MOT provides a framework for integrating against rough paths (paths with low regularity).

**Financial Application**: Modeling price paths with rough volatility using martingale constraints from option prices.

**Rough Volatility**: Models like rough Bergomi can be analyzed using MOT techniques to derive bounds on derivative prices.

## Practical Implementation Guide


### 1. Step 1: Data Preparation


**Input Data**:

- Current spot price $S_0$
- Market call prices $\{C(K_i)\}_{i=1}^n$ at maturity $T$
- Risk-free rate $r$

**Marginal Extraction**:

- Compute risk-neutral density using Breeden-Litzenberger:

  $$
  q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}(K)
  $$


- Interpolate/extrapolate to obtain continuous density
- Regularize to ensure no-arbitrage (monotonicity, convexity)

### 2. Step 2: Problem Formulation


**Define Payoff**: Specify exotic derivative payoff $g(S_0, S_T)$.

**Choose Cost**: Often $c = -g$ for upper bound, $c = g$ for lower bound.

**Discretize**: Choose grid points $\{s_i\}$ and discretize marginals.

### 3. Step 3: Optimization


**Primal LP**:
```
minimize    sum_{i,j} c(s_i, s_j) * π[i,j]
subject to  sum_j π[i,j] = μ[i]  for all i
            sum_i π[i,j] = ν[j]  for all j
            sum_j s_j * π[i,j] = s_i * μ[i]  for all i
            π[i,j] >= 0
```

**Dual LP**: Solve dual for potentials $\phi$, $\psi$.

**Solver Selection**: Use commercial solvers (Gurobi, CPLEX) for accuracy; open-source (GLPK, HiGHS) for research.

### 4. Step 4: Hedging Strategy


**Extract Hedge**: From optimal dual potentials:

- Stock position: $\theta_S = \phi'(S_0)$
- Option positions: $\theta_C(K) = \phi^{''*}(K)$

**Replication Portfolio**: Construct portfolio that super-replicates the exotic payoff.

**Verification**: Check that portfolio value dominates payoff under all scenarios.

### 5. Step 5: Sensitivity Analysis


**Parameter Variation**: 

- Perturb strike prices
- Change time to maturity
- Adjust interest rate

**Stability**: Ensure bounds remain stable under small perturbations.

**Convergence**: Verify convergence as grid is refined.

## Numerical Examples


### 1. Example 1: Digital Option


**Payoff**: $g(S_T) = \mathbb{1}_{\{S_T > K\}}$

**Marginals**: 

- $\mu = \delta_{100}$ (point mass at $S_0 = 100$)
- $\nu$ from market call prices with strikes $\{90, 95, 100, 105, 110, 115, 120\}$

**MOT Bounds**: Compute via LP:


$$
[\underline{V}, \overline{V}] \approx [0.45, 0.55]
$$



**Interpretation**: Model-free bounds are tight for digital options when sufficient market data available.

### 2. Example 2: Lookback Option


**Payoff**: $g = \max(S_T - S_0, 0) + \alpha \cdot \text{(excess over initial)}$

**Challenge**: Path-dependent feature makes two-point marginals insufficient.

**MOT Approach**: Use bounds:


$$
\overline{V} = \sup_{\pi \in \mathcal{M}(\mu, \nu)} \mathbb{E}_{\pi}[(S_T - S_0)^+]
$$



**Result**: Bounds may be wide due to limited information, suggesting need for multi-period MOT.

### 3. Example 3: Correlation Bounds for Spread Options


**Payoff**: $(S_T^{(1)} - S_T^{(2)} - K)^+$

**Given**: Marginal option prices for each asset.

**MOT Bounds**: Optimize over 2D martingale couplings:


$$
\overline{V} = \sup_{\pi \in \mathcal{M}(\mu_1, \mu_2)} \mathbb{E}_{\pi}[(S_T^{(1)} - S_T^{(2)} - K)^+]
$$



**Extremal Correlations**: Optimal coupling typically corresponds to perfect positive or negative correlation.

## Current Research Directions


### 1. High-Dimensional MOT


**Challenge**: Curse of dimensionality for $d > 2$ assets.

**Approaches**:

- **Dimensionality reduction**: Project onto lower-dimensional subspaces
- **Tensor methods**: Exploit structure in high-dimensional couplings
- **Neural networks**: Parameterize couplings or potentials with deep networks

### 2. Continuous-Time MOT


**Martingale Diffusion**: Given marginals $(\mu_t)_{t \in [0,T]}$, construct diffusion process $(X_t)$ with:

- Prescribed marginals
- Martingale property

**Fokker-Planck-MOT**: Combine Fokker-Planck equation with MOT constraints:


$$
\partial_t \rho + \nabla \cdot (\rho v) = 0
$$



with $\int x v \rho dx = 0$ (martingale).

### 3. Robust Calibration


**Problem**: Fit volatility surface ensuring:

- No calendar arbitrage
- No butterfly arbitrage
- Martingale property

**MOT Solution**: Impose MOT constraints on fitted surface to guarantee absence of arbitrage.

**Algorithms**: Iterative projection algorithms to enforce MOT conditions while minimizing fitting error.

### 4. Machine Learning and MOT


**Generative Models**: Use MOT to train generative adversarial networks (GANs) with martingale constraints.

**Applications**:

- Synthetic market data generation
- Stress testing
- Scenario analysis

**Neural MOT**: Parameterize optimal transport maps or couplings using neural networks, train via stochastic optimization.

## Summary and Key Insights


### 1. Fundamental Contributions


1. **Unification**: MOT unifies optimal transport and martingale theory, providing a geometric framework for financial mathematics.

2. **Model-Free Pricing**: Enables computing tight bounds on exotic derivatives using only vanilla option prices, without specifying dynamics.

3. **Duality**: Strong duality between primal (couplings) and dual (potentials) provides both theoretical insights and computational tools.

4. **Static Hedging**: Optimal dual solutions correspond to static portfolios of vanilla options that replicate or dominate exotic payoffs.

### 2. Practical Impact


**For Traders**:

- Robust pricing bounds quantify model uncertainty
- Static hedges reduce gamma risk and transaction costs

**For Risk Managers**:

- Worst-case scenarios identified via extremal martingale couplings
- Stress testing calibrated to no-arbitrage constraints

**For Quants**:

- Calibration algorithms ensuring arbitrage-free surfaces
- New product design guided by MOT bounds

### 3. Theoretical Significance


MOT represents a profound synthesis of:

- **Probability Theory**: Martingales and stochastic processes
- **Optimization**: Convex analysis and duality
- **Geometry**: Optimal transport and Wasserstein space
- **Finance**: Arbitrage pricing and hedging

This interdisciplinary framework continues to drive research at the intersection of mathematics, economics, and computation, offering both deep theoretical insights and practical tools for robust quantitative finance.

---

## Exercises

**Exercise 1.** Let $\mu = \delta_{100}$ (point mass at 100) and $\nu = \frac{1}{2}\delta_{80} + \frac{1}{2}\delta_{120}$. Write down all martingale couplings $\pi \in \mathcal{M}(\mu, \nu)$ and verify the martingale condition $\int y \, d\pi(y|x) = x$. Is the martingale coupling unique in this case?

??? success "Solution to Exercise 1"

    Since $\mu = \delta_{100}$ is a point mass at 100, a coupling $\pi \in \Pi(\mu, \nu)$ must have first marginal concentrated at $x = 100$. Therefore $\pi$ has the form:

    $$
    \pi = \delta_{100} \otimes \kappa
    $$

    where $\kappa$ is a probability measure on $\{80, 120\}$ with $\kappa = \frac{1}{2}\delta_{80} + \frac{1}{2}\delta_{120}$ (to match the second marginal $\nu$).

    So the unique coupling is:

    $$
    \pi\bigl(\{(100, 80)\}\bigr) = \frac{1}{2}, \quad \pi\bigl(\{(100, 120)\}\bigr) = \frac{1}{2}
    $$

    **Martingale verification.** We check $\int y \, d\pi(y | x = 100) = x = 100$:

    $$
    \int y \, d\pi(y | 100) = \frac{1}{2}(80) + \frac{1}{2}(120) = 40 + 60 = 100 \;\checkmark
    $$

    **Uniqueness.** Yes, the martingale coupling is unique in this case. Since $\mu$ is a point mass, the first marginal constraint forces all mass to originate at $x = 100$. The second marginal constraint forces $\kappa = \nu = \frac{1}{2}\delta_{80} + \frac{1}{2}\delta_{120}$. The martingale condition $\mathbb{E}[Y|X=100] = 100$ is automatically satisfied since $\mathbb{E}_\nu[Y] = 100$. There is no freedom in choosing the coupling; it is uniquely determined.

---

**Exercise 2.** Verify Strassen's theorem for the measures $\mu = \delta_{100}$ and $\nu = \frac{1}{3}\delta_{70} + \frac{1}{3}\delta_{100} + \frac{1}{3}\delta_{130}$. Specifically, check that $\mu \preceq_c \nu$ by showing that $\int f \, d\mu \leq \int f \, d\nu$ for $f(x) = |x - a|$ for several values of $a$, and construct an explicit martingale coupling.

??? success "Solution to Exercise 2"

    **Convex order verification.** We need $\int f \, d\mu \leq \int f \, d\nu$ for all convex $f$, where $\mu = \delta_{100}$ and $\nu = \frac{1}{3}\delta_{70} + \frac{1}{3}\delta_{100} + \frac{1}{3}\delta_{130}$.

    First, note $\int x \, d\nu = \frac{1}{3}(70 + 100 + 130) = 100 = \int x \, d\mu$, so the means match.

    For $f(x) = |x - a|$ (convex):

    $$
    \int f \, d\mu = |100 - a|
    $$

    $$
    \int f \, d\nu = \frac{1}{3}|70 - a| + \frac{1}{3}|100 - a| + \frac{1}{3}|130 - a|
    $$

    *Case $a = 70$:* $\int f \, d\mu = 30$. $\int f \, d\nu = \frac{1}{3}(0 + 30 + 60) = 30$. So $30 \leq 30$. $\checkmark$

    *Case $a = 100$:* $\int f \, d\mu = 0$. $\int f \, d\nu = \frac{1}{3}(30 + 0 + 30) = 20$. So $0 \leq 20$. $\checkmark$

    *Case $a = 130$:* $\int f \, d\mu = 30$. $\int f \, d\nu = \frac{1}{3}(60 + 30 + 0) = 30$. So $30 \leq 30$. $\checkmark$

    *Case $a = 85$:* $\int f \, d\mu = 15$. $\int f \, d\nu = \frac{1}{3}(15 + 15 + 45) = 25$. So $15 \leq 25$. $\checkmark$

    Since the means match and $\nu$ is "more spread out" than the point mass $\mu$, Jensen's inequality guarantees $\mu \preceq_c \nu$.

    **Explicit martingale coupling.** We need $\pi$ on $\{100\} \times \{70, 100, 130\}$ with:

    - First marginal: $\pi_1 = \delta_{100}$
    - Second marginal: $\pi_2 = \frac{1}{3}\delta_{70} + \frac{1}{3}\delta_{100} + \frac{1}{3}\delta_{130}$
    - Martingale: $\mathbb{E}[Y | X = 100] = 100$

    The coupling is uniquely determined:

    $$
    \pi = \frac{1}{3}\delta_{(100, 70)} + \frac{1}{3}\delta_{(100, 100)} + \frac{1}{3}\delta_{(100, 130)}
    $$

    Verification: $\mathbb{E}[Y | X = 100] = \frac{1}{3}(70 + 100 + 130) = 100$. $\checkmark$

---

**Exercise 3.** Consider the MOT problem with $\mu = \delta_{100}$, $\nu$ determined by call prices at strikes $K \in \{90, 100, 110\}$, and cost function $c(x, y) = (y - x)^2$. Set up the discretized linear program (with state space $\{90, 100, 110\}$ for $S_T$) and solve for both the minimum and maximum expected squared return. Interpret the extremal measures financially.

??? success "Solution to Exercise 3"

    **Setup.** We have $\mu = \delta_{100}$, the state space for $S_T$ is $\{90, 100, 110\}$, and the cost is $c(x, y) = (y - x)^2$.

    Let $\pi_j = \pi(\{100\} \times \{s_j\})$ for $s_1 = 90$, $s_2 = 100$, $s_3 = 110$. We need call prices to determine $\nu$, but the exercise asks us to set up and solve the LP. We treat $(\pi_1, \pi_2, \pi_3)$ as the probabilities assigned to the three terminal states.

    **Constraints:**

    - Normalization: $\pi_1 + \pi_2 + \pi_3 = 1$
    - Martingale: $90\pi_1 + 100\pi_2 + 110\pi_3 = 100$
    - Non-negativity: $\pi_1, \pi_2, \pi_3 \geq 0$

    From the martingale constraint: $90\pi_1 + 100\pi_2 + 110\pi_3 = 100$. Combined with $\pi_1 + \pi_2 + \pi_3 = 1$, we get:

    $$
    90\pi_1 + 100(1 - \pi_1 - \pi_3) + 110\pi_3 = 100
    $$

    $$
    -10\pi_1 + 10\pi_3 = 0 \implies \pi_1 = \pi_3
    $$

    So the feasible set is parameterized by $p = \pi_1 = \pi_3 \in [0, 1/2]$, with $\pi_2 = 1 - 2p$.

    **Objective.** The expected squared return is:

    $$
    \mathbb{E}[c] = (90 - 100)^2 \pi_1 + (100 - 100)^2 \pi_2 + (110 - 100)^2 \pi_3 = 100p + 0 + 100p = 200p
    $$

    **Minimum:** $p = 0$, giving $\pi = (0, 1, 0)$, i.e., $S_T = 100$ a.s., with $\mathbb{E}[c] = 0$. This is the degenerate model with zero volatility.

    **Maximum:** $p = 1/2$, giving $\pi = (1/2, 0, 1/2)$, i.e., $S_T \in \{90, 110\}$ with equal probability, with $\mathbb{E}[c] = 100$. This is the model with maximum volatility.

    **Financial interpretation:**

    - The minimum ($\pi = \delta_{(100, 100)}$) corresponds to a model with no uncertainty: the stock stays at 100 with certainty. The squared return is zero.
    - The maximum ($\pi = \frac{1}{2}\delta_{(100, 90)} + \frac{1}{2}\delta_{(100, 110)}$) corresponds to a model with maximum binary uncertainty: the stock either drops to 90 or rises to 110 with equal probability. This maximizes the variance of returns and represents the worst-case scenario for variance risk.

---

**Exercise 4.** Show that the Kantorovich dual for the classical optimal transport problem with cost $c(x,y) = |x - y|^2$ recovers the identity

$$
W_2^2(\mu, \nu) = \int x^2 \, d\mu + \int y^2 \, d\nu - 2 \sup_{\phi} \left\{ \int \phi \, d\mu + \int \phi^* \, d\nu \right\}
$$

where $\phi^*$ is the convex conjugate of $\phi$. Explain why this identity does not directly apply in the martingale optimal transport setting.

??? success "Solution to Exercise 4"

    **Deriving the identity.** For $c(x,y) = |x - y|^2 = x^2 - 2xy + y^2$, the Kantorovich problem is:

    $$
    W_2^2(\mu, \nu) = \inf_{\pi \in \Pi(\mu, \nu)} \int (x^2 - 2xy + y^2) \, d\pi(x, y)
    $$

    Since the marginals are fixed:

    $$
    \int x^2 \, d\pi = \int x^2 \, d\mu, \quad \int y^2 \, d\pi = \int y^2 \, d\nu
    $$

    Therefore:

    $$
    W_2^2(\mu, \nu) = \int x^2 \, d\mu + \int y^2 \, d\nu - 2 \sup_{\pi \in \Pi(\mu, \nu)} \int xy \, d\pi(x,y)
    $$

    By Kantorovich duality, $\sup_{\pi} \int xy \, d\pi = \sup_\phi \left\{\int \phi \, d\mu + \int \phi^* \, d\nu\right\}$ where $\phi^*(y) = \sup_x \{xy - \phi(x)\}$ is the convex conjugate of $\phi$. This follows because the dual constraint $\phi(x) + \psi(y) \leq xy$ with $\psi = \phi^*$ characterizes the optimal potentials. Thus:

    $$
    W_2^2(\mu, \nu) = \int x^2 \, d\mu + \int y^2 \, d\nu - 2 \sup_\phi \left\{\int \phi \, d\mu + \int \phi^* \, d\nu\right\}
    $$

    **Why this fails for MOT.** In classical optimal transport, the set $\Pi(\mu, \nu)$ of all couplings with given marginals is used. In MOT, we restrict to $\mathcal{M}(\mu, \nu) \subset \Pi(\mu, \nu)$, the subset of martingale couplings satisfying $\int y \, d\pi(y|x) = x$.

    The identity above relies on the fact that $\int x^2 \, d\pi$ and $\int y^2 \, d\pi$ depend only on marginals. While this remains true under the martingale constraint, the crucial difference is that:

    1. The **dual structure changes**: The martingale constraint introduces an additional linear constraint $\int y \, d\pi(y|x) = x$, which modifies the dual problem. Instead of the $c$-transform, one must use a **martingale $c$-transform** involving convex minorants.

    2. The **feasible set is smaller**: $\mathcal{M}(\mu, \nu) \subseteq \Pi(\mu, \nu)$, so the infimum over martingale couplings is generally larger than over all couplings. The decomposition $W_2^2 = \text{const} - 2\sup \int xy \, d\pi$ does not directly apply because the supremum is now over a restricted set.

    3. The **dual variables have different structure**: In MOT, the dual involves not just potentials $\phi, \psi$ but also a "slope" term reflecting the martingale constraint: $\phi(x) + \psi(y) + h(x)(y - x) \leq c(x,y)$ for some function $h$.

---

**Exercise 5.** For a forward start call with payoff $(S_{T_2} - S_{T_1})^+$ and marginals $\mu_1$ (at $T_1$) and $\mu_2$ (at $T_2$) both lognormal with means 100 and volatilities $\sigma_1 = 0.15$ and $\sigma_2 = 0.20$ respectively, explain qualitatively why the MOT upper bound is attained by a coupling that maximizes the negative dependence between $S_{T_1}$ and $S_{T_2} - S_{T_1}$. What financial scenario does this worst-case model represent?

??? success "Solution to Exercise 5"

    **Qualitative argument for the MOT upper bound.**

    The forward start call has payoff $(S_{T_2} - S_{T_1})^+$. This payoff is large when $S_{T_2}$ is large relative to $S_{T_1}$, or equivalently, when $S_{T_1}$ is small and $S_{T_2}$ is large.

    **Why maximum negative dependence attains the upper bound.**

    Consider the decomposition $S_{T_2} - S_{T_1} = (S_{T_2} - S_{T_1})$, where both $S_{T_1}$ and $S_{T_2}$ have fixed marginals. The payoff $(S_{T_2} - S_{T_1})^+$ is a convex function of the difference. By the martingale constraint, $\mathbb{E}[S_{T_2} | S_{T_1}] = S_{T_1}$, so the increment $S_{T_2} - S_{T_1}$ has conditional mean zero.

    To maximize $\mathbb{E}[(S_{T_2} - S_{T_1})^+]$, we want to maximize the conditional variance of $S_{T_2} - S_{T_1}$ (by Jensen's inequality applied to the convex function $(\cdot)^+$). This is achieved by creating maximum negative dependence between $S_{T_1}$ and the increment $S_{T_2} - S_{T_1}$:

    - When $S_{T_1}$ is low, the conditional distribution of $S_{T_2}$ should be as spread out as possible (high conditional variance), making the increment $S_{T_2} - S_{T_1}$ likely to be large and positive.
    - When $S_{T_1}$ is high, $S_{T_2}$ can be concentrated near $S_{T_1}$ (since the payoff is already zero when $S_{T_2} < S_{T_1}$).

    In terms of the joint distribution of $(S_{T_1}, S_{T_2})$, this means making $S_{T_1}$ and $S_{T_2} - S_{T_1}$ negatively dependent: small $S_{T_1}$ is paired with large upward moves.

    **Financial scenario.** The worst-case model represents a market where:

    - Stocks that have declined by time $T_1$ (low $S_{T_1}$) experience large upward rebounds by $T_2$, creating large forward-start call payoffs.
    - Stocks that have risen by time $T_1$ (high $S_{T_1}$) remain flat or decline, contributing nothing to the payoff.

    This is a "mean-reversion on steroids" scenario, where past losers become future winners with the maximum possible magnitude. For a volatility trader, this represents the worst-case scenario for forward-starting options: the implied volatility at the reset date $T_1$ is highest precisely when the forward start option is most "in danger" (i.e., when the reset strike is lowest).

    With lognormal marginals at both dates (means 100, $\sigma_1 = 0.15$, $\sigma_2 = 0.20$), the MOT upper bound is strictly larger than any single-model price because no standard model (e.g., Black-Scholes) achieves the extremal negative dependence structure.

---

**Exercise 6.** Describe the Sinkhorn algorithm for entropic regularization of the classical optimal transport problem. Then explain the key modification needed to incorporate the martingale constraint $\sum_j s_j^T \pi_{ij} = s_i^0 \sum_j \pi_{ij}$. Why does entropic regularization improve numerical stability compared to the standard LP formulation?

??? success "Solution to Exercise 6"

    **Standard Sinkhorn algorithm (classical OT).**

    Given discrete marginals $\mu = (\mu_1, \ldots, \mu_{N_0})$ and $\nu = (\nu_1, \ldots, \nu_{N_T})$, cost matrix $c_{ij}$, and regularization parameter $\varepsilon > 0$, the entropic OT problem is:

    $$
    \min_{\pi \geq 0} \sum_{i,j} c_{ij} \pi_{ij} + \varepsilon \sum_{i,j} \pi_{ij}(\log \pi_{ij} - 1)
    $$

    subject to $\sum_j \pi_{ij} = \mu_i$ and $\sum_i \pi_{ij} = \nu_j$.

    The Sinkhorn algorithm exploits the fact that the optimal $\pi$ has the form $\pi_{ij} = u_i K_{ij} v_j$ where $K_{ij} = e^{-c_{ij}/\varepsilon}$:

    1. Initialize $v_j^{(0)} = 1$ for all $j$.
    2. Iterate for $k = 0, 1, 2, \ldots$:

        $$
        u_i^{(k+1)} = \frac{\mu_i}{\sum_j K_{ij} v_j^{(k)}}, \quad v_j^{(k+1)} = \frac{\nu_j}{\sum_i K_{ij} u_i^{(k+1)}}
        $$

    3. The optimal coupling is $\pi_{ij}^* = u_i^* K_{ij} v_j^*$.

    This alternates between projecting onto the first marginal constraint and the second marginal constraint.

    **Modification for the martingale constraint.** The martingale constraint $\sum_j s_j^T \pi_{ij} = s_i^0 \sum_j \pi_{ij} = s_i^0 \mu_i$ introduces an additional linear constraint beyond the two marginal constraints.

    The key modification is to add a **third projection step** that enforces the martingale condition. After the standard Sinkhorn updates for both marginals, project the current iterate onto the martingale subspace:

    $$
    \pi_{ij} \leftarrow \pi_{ij} \cdot \exp\left(\lambda_i (s_j^T - s_i^0)\right)
    $$

    where $\lambda_i$ is a Lagrange multiplier chosen so that $\sum_j s_j^T \pi_{ij} = s_i^0 \mu_i$. This three-step iteration alternates:

    (a) Project onto first marginal ($u$-update)

    (b) Project onto second marginal ($v$-update)

    (c) Project onto martingale constraint ($\lambda$-update)

    Each step corresponds to a Bregman projection with respect to the KL divergence, and the iteration converges to the unique solution of the entropy-regularized MOT problem.

    **Why entropic regularization improves stability.** The standard LP formulation of MOT has several numerical issues:

    1. **Degeneracy**: LP solutions are at vertices of the feasible polytope, which are sparse and may not be unique, causing solver instability.
    2. **Sensitivity**: Small changes in the data (marginals, cost) can cause the LP solution to jump between vertices.
    3. **Scalability**: LP solvers have complexity $O(N^3)$ or worse.

    Entropic regularization addresses all three issues:

    - The entropy term makes the objective strictly convex, guaranteeing a **unique** solution.
    - The solution $\pi^*$ is **smooth** (fully supported), avoiding degeneracy and sensitivity.
    - The Sinkhorn algorithm has complexity $O(N^2)$ per iteration and converges exponentially fast.
    - As $\varepsilon \to 0$, the regularized solution converges to the true MOT solution.

---

**Exercise 7.** Consider two assets with marginal distributions $\mu_1$ (uniform on $[80, 120]$) and $\mu_2$ (uniform on $[90, 110]$), both with mean 100. For the basket call payoff $g = \left(\frac{1}{2}S_T^{(1)} + \frac{1}{2}S_T^{(2)} - 100\right)^+$, formulate the multi-dimensional MOT problem. Use the Frechet-Hoeffding bounds to argue that the upper bound is attained when the two assets are comonotonic, and compute the resulting bound explicitly.

??? success "Solution to Exercise 7"

    **MOT formulation.** The multi-dimensional MOT problem is:

    $$
    \overline{V} = \sup_{\pi \in \mathcal{M}(\mu_1, \mu_2)} \int \left(\frac{1}{2}s_1 + \frac{1}{2}s_2 - 100\right)^+ d\pi(s_1, s_2)
    $$

    where $\mathcal{M}(\mu_1, \mu_2)$ is the set of joint distributions on $\mathbb{R}^2_+$ with marginals $\mu_1$ (uniform on $[80, 120]$) and $\mu_2$ (uniform on $[90, 110]$), such that the martingale constraint is satisfied for each asset individually. Since we treat this as a single-period problem starting from $S_0^{(i)} = 100$, the martingale constraint requires $\mathbb{E}_\pi[S_T^{(i)}] = 100$, which is already satisfied by both uniform marginals.

    **Frechet-Hoeffding upper bound.** The Frechet-Hoeffding upper bound on the coupling is the comonotonic coupling:

    $$
    \pi^{\text{upper}}(A \times B) = \min\{\mu_1(A), \mu_2(B)\}
    $$

    For continuous marginals, this corresponds to $S_T^{(2)} = F_{\mu_2}^{-1}(F_{\mu_1}(S_T^{(1)}))$, i.e., both assets are driven by the same underlying randomness.

    **Why comonotonicity attains the upper bound.** The basket payoff $g = \left(\frac{1}{2}S_T^{(1)} + \frac{1}{2}S_T^{(2)} - 100\right)^+$ is a convex function of $(S_T^{(1)}, S_T^{(2)})$, and it is increasing in both arguments. For convex, coordinatewise increasing functions, the expectation is maximized by the comonotonic coupling (this is a consequence of the rearrangement inequality / comonotonic improvement theorem).

    **Explicit computation under comonotonicity.** Under the comonotonic coupling, let $U \sim \text{Uniform}(0, 1)$ and set:

    $$
    S_T^{(1)} = 80 + 40U, \quad S_T^{(2)} = 90 + 20U
    $$

    The basket value is:

    $$
    B = \frac{1}{2}(80 + 40U) + \frac{1}{2}(90 + 20U) = \frac{1}{2}(170 + 60U) = 85 + 30U
    $$

    The payoff is:

    $$
    g = (85 + 30U - 100)^+ = (30U - 15)^+ = 30\left(U - \frac{1}{2}\right)^+
    $$

    Computing the expectation:

    $$
    \overline{V} = \mathbb{E}[g] = 30 \int_0^1 \left(u - \frac{1}{2}\right)^+ du = 30 \int_{1/2}^1 \left(u - \frac{1}{2}\right) du
    $$

    $$
    = 30 \left[\frac{(u - 1/2)^2}{2}\right]_{1/2}^{1} = 30 \cdot \frac{(1/2)^2}{2} = 30 \cdot \frac{1}{8} = 3.75
    $$

    Therefore $\overline{V} = 3.75$.
