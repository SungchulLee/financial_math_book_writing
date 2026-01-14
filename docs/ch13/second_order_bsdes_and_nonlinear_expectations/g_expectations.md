# g-Expectations


## Introduction


The theory of **g-expectations** represents a fundamental generalization of classical linear expectation to **nonlinear expectations** that arise naturally in financial mathematics under model uncertainty, transaction costs, and risk aversion. Introduced by Shige Peng in 1997, g-expectations provide a unified framework for:

1. **Nonlinear pricing**: Prices that are not simply expectations under a single probability measure
2. **Dynamic risk measures**: Time-consistent measures of risk (e.g., dynamic coherent risk measures)
3. **Robust valuation**: Pricing under model uncertainty
4. **Backward stochastic differential equations (BSDEs)**: Solutions to BSDEs define g-expectations

The mathematical foundation lies in the theory of **backward stochastic differential equations (BSDEs)** and provides a bridge between stochastic analysis, PDEs, and financial mathematics.

## Mathematical Foundations


### 1. Classical Expectation


**Linear Expectation**: Given a probability space $(\Omega, \mathcal{F}, P)$ and random variable $\xi \in L^2(\Omega, \mathcal{F}, P)$:


$$
E[\xi] = \int_{\Omega} \xi(\omega) \, dP(\omega)
$$



**Properties**:
1. **Linearity**: $E[a\xi + b\eta] = aE[\xi] + bE[\eta]$
2. **Monotonicity**: $\xi \geq \eta \implies E[\xi] \geq E[\eta]$
3. **Constant preserving**: $E[c] = c$ for constants $c$
4. **Tower property**: $E[E[\xi|\mathcal{G}]] = E[\xi]$

**Conditional Expectation**: For sub-$\sigma$-algebra $\mathcal{G} \subseteq \mathcal{F}$:


$$
E[\xi|\mathcal{G}]
$$



is the unique $\mathcal{G}$-measurable random variable satisfying:


$$
E[\xi \mathbb{1}_A] = E[E[\xi|\mathcal{G}] \mathbb{1}_A] \quad \text{for all } A \in \mathcal{G}
$$



### 2. Backward Stochastic Differential Equations


**BSDE Definition**: A pair of processes $(Y_t, Z_t)_{t \in [0,T]}$ satisfying:


$$
Y_t = \xi + \int_t^T g(s, Y_s, Z_s) \, ds - \int_t^T Z_s \, dW_s
$$



where:
- $\xi$: Terminal condition (random variable, $\mathcal{F}_T$-measurable)
- $g: [0,T] \times \mathbb{R} \times \mathbb{R}^d \to \mathbb{R}$: Generator (driver)
- $W_t$: $d$-dimensional Brownian motion
- $Y_t$: Solution process (value process)
- $Z_t$: Control process (gradient process)

**Differential Form**:


$$
dY_t = -g(t, Y_t, Z_t) \, dt + Z_t \, dW_t, \quad Y_T = \xi
$$



### 3. Well-Posedness


**Theorem** (Pardoux-Peng, 1990): Suppose:
1. $g$ is uniformly Lipschitz in $(y, z)$
2. $\mathbb{E}\left[\int_0^T |g(t, 0, 0)|^2 dt\right] < \infty$
3. $\mathbb{E}[|\xi|^2] < \infty$

Then there exists a unique adapted solution $(Y_t, Z_t)$ to the BSDE with:


$$
\mathbb{E}\left[\sup_{t \in [0,T]} |Y_t|^2 + \int_0^T |Z_t|^2 dt\right] < \infty
$$



**Proof Sketch**: Use Picard iteration with contraction mapping in appropriate Banach space of adapted processes.

## g-Expectation Definition


### 1. Conditional g-Expectation


**Definition**: Given generator $g$ and terminal condition $\xi$, the **conditional g-expectation** is:


$$
\mathcal{E}_g[\xi|\mathcal{F}_t] := Y_t
$$



where $Y_t$ is the solution to the BSDE:


$$
Y_t = \xi + \int_t^T g(s, Y_s, Z_s) \, ds - \int_t^T Z_s \, dW_s
$$



**g-Expectation**: The unconditional version is:


$$
\mathcal{E}_g[\xi] := \mathcal{E}_g[\xi|\mathcal{F}_0] = Y_0
$$



**Interpretation**: 
- Generalizes conditional expectation
- Depends on entire path through generator $g$
- Nonlinear in general

### 2. Properties


**Proposition** (Basic Properties): For g-expectation $\mathcal{E}_g$:

1. **Constant Preserving**: $\mathcal{E}_g[c] = c$ for constants $c$

2. **Monotonicity**: If $\xi \geq \eta$ a.s., then $\mathcal{E}_g[\xi] \geq \mathcal{E}_g[\eta]$

3. **Translation Invariance**: $\mathcal{E}_g[\xi + c|\mathcal{F}_t] = \mathcal{E}_g[\xi|\mathcal{F}_t] + c$

4. **Time Consistency**: 

   $$
   \mathcal{E}_g[\mathcal{E}_g[\xi|\mathcal{F}_t]|\mathcal{F}_s] = \mathcal{E}_g[\xi|\mathcal{F}_s] \quad \text{for } s \leq t
   $$



**Proof** (Time Consistency): Let $Y_t = \mathcal{E}_g[\xi|\mathcal{F}_t]$. Then:


$$
Y_s = Y_t + \int_s^t g(r, Y_r, Z_r) \, dr - \int_s^t Z_r \, dW_r
$$



This BSDE with terminal condition $Y_t$ has solution $Y_s$ at time $s$, establishing time consistency.

### 3. Examples


**Example 1** (Linear Case): If $g(t, y, z) = 0$, then:


$$
\mathcal{E}_g[\xi|\mathcal{F}_t] = E[\xi|\mathcal{F}_t]
$$



the classical conditional expectation.

**Example 2** (Exponential Utility): If $g(t, y, z) = -\frac{\gamma}{2} |z|^2$, then:


$$
\mathcal{E}_g[\xi] = -\frac{1}{\gamma} \log E[e^{-\gamma \xi}]
$$



the certainty equivalent under exponential utility with risk aversion $\gamma$.

**Example 3** (Worst-Case Expectation): If $g(t, y, z) = \alpha |z|$, then:


$$
\mathcal{E}_g[\xi] = \sup_{\mathbb{Q} \in \mathcal{P}_{\alpha}} E_{\mathbb{Q}}[\xi]
$$



where $\mathcal{P}_{\alpha}$ is a set of probability measures with bounded density.

## Generators and Their Properties


### 1. Lipschitz Generators


**Definition**: Generator $g$ is **Lipschitz** if there exists $K > 0$ such that:


$$
|g(t, y_1, z_1) - g(t, y_2, z_2)| \leq K(|y_1 - y_2| + |z_1 - z_2|)
$$



for all $(t, y_1, z_1), (t, y_2, z_2)$.

**Consequence**: Lipschitz generators ensure unique solutions to BSDEs and well-defined g-expectations.

### 2. Convexity


**Definition**: Generator $g(t, y, z)$ is **convex** in $(y, z)$ if:


$$
g(t, \lambda y_1 + (1-\lambda) y_2, \lambda z_1 + (1-\lambda) z_2) \leq \lambda g(t, y_1, z_1) + (1-\lambda) g(t, y_2, z_2)
$$



for all $\lambda \in [0, 1]$.

**Implication**: Convex generators lead to concave g-expectations:


$$
\mathcal{E}_g[\lambda \xi_1 + (1-\lambda) \xi_2] \geq \lambda \mathcal{E}_g[\xi_1] + (1-\lambda) \mathcal{E}_g[\xi_2]
$$



**Risk Aversion**: Convexity in $z$ corresponds to risk aversion in the associated valuation.

### 3. Positive Homogeneity


**Definition**: Generator $g(t, y, z)$ is **positively homogeneous** in $(y, z)$ if:


$$
g(t, \lambda y, \lambda z) = \lambda g(t, y, z)
$$



for all $\lambda > 0$.

**Consequence**: The corresponding g-expectation is positively homogeneous:


$$
\mathcal{E}_g[\lambda \xi] = \lambda \mathcal{E}_g[\xi]
$$



for $\lambda > 0$.

### 4. Subadditivity


**Definition**: Generator $g$ induces **subadditive** g-expectation if:


$$
\mathcal{E}_g[\xi_1 + \xi_2] \leq \mathcal{E}_g[\xi_1] + \mathcal{E}_g[\xi_2]
$$



**Sufficient Condition**: If $g(t, y, z)$ is convex and positively homogeneous in $(y, z)$, then $\mathcal{E}_g$ is subadditive.

## Comparison Theorems


### 1. Comparison of Terminal Conditions


**Theorem** (Comparison): Let $(Y_t, Z_t)$ and $(\bar{Y}_t, \bar{Z}_t)$ be solutions to BSDEs with the same generator $g$ but terminal conditions $\xi$ and $\bar{\xi}$ respectively.

If $\xi \leq \bar{\xi}$ a.s., then:


$$
Y_t \leq \bar{Y}_t \quad \text{a.s. for all } t \in [0, T]
$$



**Proof**: Define $\Delta Y_t = \bar{Y}_t - Y_t$ and $\Delta Z_t = \bar{Z}_t - Z_t$. Then:


$$
d(\Delta Y_t) = -[g(t, \bar{Y}_t, \bar{Z}_t) - g(t, Y_t, Z_t)] \, dt + \Delta Z_t \, dW_t
$$



Apply Itô's formula to $(\Delta Y_t)^-$ (negative part) and use Lipschitz property to show $(\Delta Y_t)^- = 0$.

### 2. Comparison of Generators


**Theorem**: Let $(Y_t, Z_t)$ and $(\bar{Y}_t, \bar{Z}_t)$ be solutions to BSDEs with generators $g$ and $\bar{g}$ respectively, both with the same terminal condition $\xi$.

If $g(t, y, z) \geq \bar{g}(t, y, z)$ for all $(t, y, z)$, then:


$$
Y_t \leq \bar{Y}_t \quad \text{a.s. for all } t \in [0, T]
$$



**Interpretation**: Larger generator → Larger "running cost" → Smaller value process.

**Application**: If $g_1 \leq g_2$, then:


$$
\mathcal{E}_{g_1}[\xi] \geq \mathcal{E}_{g_2}[\xi]
$$



### 3. Strict Comparison


**Theorem** (Strict Comparison): Under additional regularity (strict inequality on a set of positive measure), strict inequalities hold:


$$
\xi < \bar{\xi} \text{ a.s. on set } A \text{ with } P(A) > 0 \implies Y_t < \bar{Y}_t \text{ a.s.}
$$



## Representation Theorems


### 1. Minimal and Maximal Representations


**Theorem** (Peng): For convex and positively homogeneous generator $g$, the g-expectation admits representations:


$$
\mathcal{E}_g[\xi] = \sup_{\mathbb{Q} \in \mathcal{Q}} E_{\mathbb{Q}}[\xi] = \inf_{\mathbb{Q} \in \mathcal{Q}^c} E_{\mathbb{Q}}[\xi]
$$



where:
- $\mathcal{Q}$: Set of "admissible" probability measures
- $\mathcal{Q}^c$: Complement set

**Construction**: The set $\mathcal{Q}$ is characterized through the generator $g$ via Girsanov's theorem.

### 2. Entropic Representation


**Exponential Utility Case**: For $g(t, y, z) = -\frac{\gamma}{2} |z|^2$:


$$
\mathcal{E}_g[\xi] = \sup_{\mathbb{Q} \ll P} \left\{ E_{\mathbb{Q}}[\xi] - \frac{1}{\gamma} H(\mathbb{Q}|P) \right\}
$$



where:


$$
H(\mathbb{Q}|P) = E_{\mathbb{Q}}\left[\log \frac{d\mathbb{Q}}{dP}\right]
$$



is the relative entropy (Kullback-Leibler divergence).

**Proof**: The optimal measure $\mathbb{Q}^*$ has Radon-Nikodym derivative:


$$
\frac{d\mathbb{Q}^*}{dP}\bigg|_{\mathcal{F}_T} = \exp\left(-\gamma \xi + \frac{\gamma^2}{2} \int_0^T |Z_t|^2 dt - \gamma \int_0^T Z_t \, dW_t\right)
$$



where $Z_t$ comes from the BSDE solution.

### 3. Choquet Capacity Representation


**Non-Additive Measure**: For certain generators, g-expectations correspond to integration with respect to Choquet capacities.

**Capacity**: A set function $\nu: \mathcal{F} \to [0, 1]$ with:
1. $\nu(\emptyset) = 0$, $\nu(\Omega) = 1$
2. Monotonicity: $A \subseteq B \implies \nu(A) \leq \nu(B)$

**Choquet Integral**:


$$
\int_{\Omega} \xi \, d\nu = \int_0^{\infty} \nu(\{\xi \geq t\}) \, dt + \int_{-\infty}^0 [\nu(\{\xi \geq t\}) - 1] \, dt
$$



**Connection**: Certain g-expectations can be written as Choquet integrals with appropriately defined capacity.

## Dynamic Risk Measures


### 1. Coherent Risk Measures


**Definition** (Artzner et al., 1999): A functional $\rho: L^{\infty} \to \mathbb{R}$ is a **coherent risk measure** if:

1. **Monotonicity**: $X \geq Y \implies \rho(X) \leq \rho(Y)$
2. **Translation invariance**: $\rho(X + c) = \rho(X) - c$
3. **Positive homogeneity**: $\rho(\lambda X) = \lambda \rho(X)$ for $\lambda > 0$
4. **Subadditivity**: $\rho(X + Y) \leq \rho(X) + \rho(Y)$

**Example**: Average Value-at-Risk (AVaR or CVaR):


$$
\text{AVaR}_{\alpha}(X) = \frac{1}{\alpha} \int_0^{\alpha} \text{VaR}_u(X) \, du
$$



### 2. Dynamic Coherent Risk Measures


**Definition**: A family $\{\rho_t\}_{t \in [0,T]}$ is a **dynamic coherent risk measure** if each $\rho_t$ is coherent and satisfies **time consistency**:


$$
\rho_s(\rho_t(X)) = \rho_s(X) \quad \text{for } s \leq t
$$



**Theorem** (Delbaen et al., 2010): Dynamic coherent risk measures correspond to g-expectations with generators that are convex, positively homogeneous, and Lipschitz.

**Representation**: 


$$
\rho_t(X) = \mathcal{E}_g[-X|\mathcal{F}_t]
$$



for appropriate generator $g$.

### 3. Connection to BSDEs


**Theorem**: If $\rho_t$ is a dynamic coherent risk measure, then $Y_t = \rho_t(X)$ satisfies a BSDE:


$$
dY_t = g(t, Y_t, Z_t) \, dt - Z_t \, dW_t, \quad Y_T = X
$$



where $g$ is convex and positively homogeneous in $(y, z)$.

**Converse**: Given such a generator, the g-expectation defines a dynamic coherent risk measure.

## Applications to Finance


### 1. Option Pricing Under Model Uncertainty


**Setup**: Uncertain volatility $\sigma \in [\underline{\sigma}, \overline{\sigma}]$.

**Robust Price**: The seller's (super-replication) price is:


$$
V_0 = \mathcal{E}_g[\Phi(S_T)]
$$



where:


$$
g(t, y, z) = \sup_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} \left\{ -\frac{1}{2} \sigma^2 |z|^2 \right\} = -\frac{1}{2} \underline{\sigma}^2 |z|^2
$$



for positive gamma positions.

**BSDE**:


$$
dY_t = \frac{1}{2} \underline{\sigma}^2 |Z_t|^2 \, dt + Z_t \, dW_t, \quad Y_T = \Phi(S_T)
$$



**Hedging Strategy**: The optimal hedge is $\Delta_t = Z_t$.

### 2. Utility Indifference Pricing


**Setup**: Agent with exponential utility $u(x) = -e^{-\gamma x}$ and risk aversion $\gamma > 0$.

**Indifference Price**: Price $p$ such that:


$$
\sup_{\theta} E[-e^{-\gamma(X_T^{\theta, 0})}] = \sup_{\theta} E[-e^{-\gamma(X_T^{\theta, p} + \Phi)}]
$$



where $X_T^{\theta, v}$ is terminal wealth from initial capital $v$ and strategy $\theta$.

**g-Expectation**: The indifference price satisfies:


$$
p = \mathcal{E}_g[\Phi]
$$



with generator:


$$
g(t, y, z) = -\frac{\gamma}{2} |z - \sigma S_t|^2 + \frac{\gamma}{2} \sigma^2 S_t^2
$$



### 3. Optimal Investment with Ambiguity


**Problem**: Maximize worst-case expected utility:


$$
\sup_{\pi} \inf_{\mathbb{Q} \in \mathcal{Q}} E_{\mathbb{Q}}[u(X_T^{\pi})]
$$



where $\mathcal{Q}$ is a set of probability measures representing ambiguity.

**Solution**: The value function satisfies:


$$
V(t, x) = \mathcal{E}_g[u(X_T) | X_t = x]
$$



with appropriate generator encoding ambiguity aversion.

**Optimal Strategy**: Extracted from the $Z$ process in the BSDE solution:


$$
\pi_t^* = f(Z_t, X_t)
$$



### 4. Credit Risk and CVA


**Credit Valuation Adjustment (CVA)**: Adjustment for counterparty default risk.

**g-Expectation Framework**: The CVA can be computed using:


$$
\text{CVA} = \mathcal{E}_g[\text{Loss at default}]
$$



with generator reflecting uncertainty about default intensity and recovery rates.

**Advantage**: Captures model uncertainty and ambiguity in credit modeling.

## Numerical Methods


### 1. Discrete-Time Approximation


**Euler Scheme**: Partition $[0, T]$ into $N$ intervals with $\Delta t = T/N$.

**Backward Iteration**: Starting from $Y_T = \xi$:


$$
Y_{t_i} = Y_{t_{i+1}} + g(t_i, Y_{t_i}, Z_{t_i}) \Delta t - Z_{t_i} \Delta W_{t_i}
$$



**Z Estimation**: Use least-squares projection:


$$
Z_{t_i} = \arg\min_{z} E\left[\left|Y_{t_{i+1}} - Y_{t_i} - g(t_i, Y_{t_i}, z) \Delta t + z \Delta W_{t_i}\right|^2 | \mathcal{F}_{t_i}\right]
$$



**Convergence**: Under Lipschitz conditions:


$$
E[|Y_0 - Y_0^N|] = O(\Delta t^{1/2})
$$



### 2. Monte Carlo Methods


**Algorithm**:
1. Simulate $M$ paths of Brownian motion: $\{W^{(m)}_t\}_{m=1}^M$
2. At each time $t_i$, estimate conditional expectations using regression
3. Backward iterate to compute $Y_0$

**Regression**: Use basis functions $\{\phi_j\}$ to approximate:


$$
E[Y_{t_{i+1}} | \mathcal{F}_{t_i}] \approx \sum_{j=1}^K \alpha_j \phi_j(S_{t_i})
$$



**Complexity**: $O(MNK)$ where $M$ is paths, $N$ is time steps, $K$ is basis functions.

### 3. Deep Learning Approaches


**Neural Network Parameterization**: Represent $(Y_t, Z_t)$ using neural networks:


$$
Y_t = f_{\theta_Y}(t, S_t), \quad Z_t = f_{\theta_Z}(t, S_t)
$$



**Training**: Minimize loss function:


$$
\mathcal{L}(\theta_Y, \theta_Z) = E\left[\left|Y_T - \xi\right|^2 + \int_0^T \left|dY_t + g(t, Y_t, Z_t) dt - Z_t dW_t\right|^2\right]
$$



**Advantages**: 
- Handles high-dimensional problems
- Avoids curse of dimensionality
- Scales well with complexity

## Advanced Topics


### 1. Reflected BSDEs


**Definition**: A triple $(Y_t, Z_t, K_t)$ satisfying:


$$
Y_t = \xi + \int_t^T g(s, Y_s, Z_s) \, ds + K_T - K_t - \int_t^T Z_s \, dW_s
$$



with:
1. $Y_t \geq S_t$ (obstacle constraint)
2. $K_t$ is increasing, continuous, $K_0 = 0$
3. $\int_0^T (Y_t - S_t) \, dK_t = 0$ (Skorokhod condition)

**Interpretation**: $K_t$ is the minimal pushing force to keep $Y_t$ above obstacle $S_t$.

**Application**: American option pricing, optimal stopping problems.

### 2. Mean-Field BSDEs


**Setup**: Large population of agents, each influenced by others.

**Mean-Field BSDE**:


$$
Y_t^i = \xi^i + \int_t^T g(s, Y_s^i, Z_s^i, \bar{Y}_s, \bar{Z}_s) \, ds - \int_t^T Z_s^i \, dW_s^i
$$



where $\bar{Y}_t = \frac{1}{N} \sum_{i=1}^N Y_t^i$ is the empirical mean.

**Limit**: As $N \to \infty$, the system converges to a McKean-Vlasov type BSDE.

**Application**: Systemic risk, large portfolio optimization, crowd behavior in markets.

### 3. Forward-Backward SDEs


**Coupled System**: $(X_t, Y_t, Z_t)$ satisfying:


$$
dX_t = b(t, X_t, Y_t, Z_t) \, dt + \sigma(t, X_t, Y_t, Z_t) \, dW_t
$$




$$
dY_t = -g(t, X_t, Y_t, Z_t) \, dt + Z_t \, dW_t
$$



with $X_0 = x$ and $Y_T = \Phi(X_T)$.

**Application**: Stochastic control problems where control affects both forward dynamics and backward valuation.

**Well-Posedness**: Requires careful analysis; solutions exist under monotonicity or small-time conditions.

### 4. Quadratic BSDEs


**Generator**: Quadratic growth in $z$:


$$
g(t, y, z) = f(t, y) + \frac{1}{2} z^\top A(t, y) z
$$



**Challenge**: Standard Lipschitz theory doesn't apply directly.

**Existence**: Proven under specific conditions (Kobylanski, 2000).

**Application**: 
- Exponential utility maximization
- Risk-sensitive control
- Large deviations

## Connections to PDEs


### 1. Feynman-Kac Formula for BSDEs


**Theorem**: If $Y_t = v(t, X_t)$ for some function $v$ and state process $X_t$, then $v$ satisfies the PDE:


$$
\frac{\partial v}{\partial t} + \mathcal{L} v + g(t, v, \sigma^\top \nabla v) = 0
$$



with terminal condition $v(T, x) = \Phi(x)$, where $\mathcal{L}$ is the infinitesimal generator of $X_t$.

**Proof**: Apply Itô's formula to $v(t, X_t)$ and match terms with the BSDE.

**Interpretation**: BSDEs provide probabilistic representation for nonlinear PDEs.

### 2. Viscosity Solutions


**Definition**: A function $v$ is a **viscosity solution** if it satisfies the PDE in the viscosity sense (comparison with smooth test functions).

**Theorem** (Crandall-Ishii-Lions): Under appropriate conditions, the BSDE solution $Y_t = v(t, X_t)$ where $v$ is the unique viscosity solution to the associated PDE.

**Advantage**: Viscosity solutions exist even when classical solutions don't (e.g., non-smooth payoffs).

### 3. Hamilton-Jacobi-Bellman Equations


**Stochastic Control**: Consider:


$$
V(t, x) = \sup_{\alpha \in \mathcal{A}} E\left[\int_t^T f(s, X_s^{\alpha}, \alpha_s) \, ds + \Phi(X_T^{\alpha}) \bigg| X_t = x\right]
$$



**HJB Equation**:


$$
\frac{\partial V}{\partial t} + \sup_{\alpha} \{\mathcal{L}^{\alpha} V + f(t, x, \alpha)\} = 0
$$



**BSDE Connection**: The value function satisfies a BSDE with generator:


$$
g(t, y, z) = \sup_{\alpha} \{-f(t, x, \alpha) - \mu^{\alpha}(t, x) \cdot \nabla v - \frac{1}{2} \text{tr}[(\sigma^{\alpha})^2 \nabla^2 v]\}
$$



## Convergence and Stability


### 1. Continuous Dependence


**Theorem**: Let $(Y_t^n, Z_t^n)$ be solutions to BSDEs with generators $g_n$ and terminal conditions $\xi_n$.

If $g_n \to g$ and $\xi_n \to \xi$ in appropriate norms, then:


$$
Y_t^n \to Y_t, \quad Z_t^n \to Z_t
$$



in $L^2$ norm.

**Proof**: Use Lipschitz continuity and Gronwall's inequality.

**Application**: Justifies numerical approximations and perturbation analysis.

### 2. Convergence of Discretizations


**Theorem**: The discrete-time approximation converges to the continuous-time BSDE solution:


$$
\sup_{t \in [0,T]} E[|Y_t - Y_t^N|^2] = O(\Delta t)
$$



under appropriate regularity conditions.

**Higher-Order Schemes**: Milstein-type schemes achieve $O((\Delta t)^{3/2})$ or better.

### 3. Robustness to Model Perturbations


**g-Expectations Stability**: Small changes in generator lead to small changes in g-expectation:


$$
|g_1 - g_2| \leq \epsilon \implies |\mathcal{E}_{g_1}[\xi] - \mathcal{E}_{g_2}[\xi]| \leq C \epsilon
$$



for some constant $C$ depending on $T$ and Lipschitz constants.

## Summary and Key Insights


### 1. Fundamental Contributions


1. **Nonlinear Expectations**: g-expectations extend classical expectations to nonlinear frameworks, capturing risk aversion, ambiguity, and model uncertainty.

2. **BSDE Solutions**: Provide constructive method to compute g-expectations through backward stochastic differential equations.

3. **Time Consistency**: g-expectations are dynamically consistent, essential for multi-period decision-making and risk management.

4. **Representation Theorems**: Connect g-expectations to multiple probability measures, capacities, and supremum/infimum operations.

5. **Dynamic Risk Measures**: Provide mathematical foundation for coherent, time-consistent risk measures used in finance and insurance.

### 2. Practical Implications


**For Pricing**:
- Robust pricing under model uncertainty
- Utility-based valuation
- Credit valuation adjustments

**For Risk Management**:
- Dynamic coherent risk measures
- Stress testing frameworks
- Regulatory capital calculations

**For Portfolio Optimization**:
- Ambiguity-averse portfolio selection
- Robust optimal control
- Mean-field game equilibria

### 3. Theoretical Significance


g-Expectations unify:
- **Stochastic Analysis**: BSDEs and martingale theory
- **PDE Theory**: Viscosity solutions and Hamilton-Jacobi equations
- **Optimization**: Stochastic control and minimax problems
- **Finance**: Pricing, hedging, and risk management

The theory continues to evolve with extensions to:
- Mean-field limits
- Infinite-dimensional settings
- Non-Markovian frameworks
- Machine learning integration

g-Expectations represent a cornerstone of modern mathematical finance, providing rigorous foundations for robust valuation and decision-making under uncertainty.
