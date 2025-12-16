# Second-Order BSDEs (2BSDEs)

## Introduction

**Second-order backward stochastic differential equations (2BSDEs)** represent a fundamental generalization of classical BSDEs that naturally arise when considering **model uncertainty** or **volatility uncertainty** in financial mathematics. Introduced by Soner, Touzi, and Zhang (2012), 2BSDEs provide a rigorous framework for:

1. **Robust pricing and hedging**: Derivative valuation under volatility uncertainty
2. **Viscosity solutions**: Probabilistic representation for fully nonlinear second-order PDEs
3. **Stochastic target problems**: Reachability under model ambiguity
4. **G-expectations**: Generalized nonlinear expectations under volatility uncertainty

The key innovation is that 2BSDEs account for uncertainty in the **quadratic variation** of the driving process, not just its drift, leading to fully nonlinear equations and connections to second-order PDEs.

## Mathematical Framework

### Classical BSDEs (Review)

**Standard BSDE**: A pair $(Y_t, Z_t)$ satisfying:


$$
Y_t = \xi + \int_t^T g(s, Y_s, Z_s) \, ds - \int_t^T Z_s \, dW_s
$$



where $g$ is the generator (first-order in $z$).

**Limitation**: Assumes fixed quadratic variation of the Brownian motion:


$$
d\langle W \rangle_t = dt
$$



### Volatility Uncertainty

**Setup**: Uncertain volatility matrix $\sigma_t$ with:


$$
\underline{a} \leq \sigma_t \sigma_t^\top \leq \overline{a}
$$



in the positive semidefinite ordering.

**Canonical Space**: Consider all semimartingales with quadratic variation in the specified range.

**Question**: How to define expectations and valuations that are robust to this uncertainty?

## Definition of 2BSDEs

### Informal Definition

A **second-order BSDE** is an equation of the form:


$$
Y_t = \xi + \int_t^T F(s, Y_s, Z_s, \Gamma_s) \, ds - \int_t^T Z_s \, dW_s - \int_t^T \text{tr}[\Gamma_s d\langle W \rangle_s]
$$



where:
- $F$: Generator (nonlinear, second-order)
- $\Gamma_t$: Second-order process (matrix-valued)
- $\langle W \rangle_t$: Quadratic variation of $W$

**Key Feature**: The generator $F$ depends on $\Gamma$, which interacts with uncertain quadratic variation.

### Formal Framework

**Probability Space**: Work on canonical space $\Omega = C([0,T], \mathbb{R}^d)$ of continuous paths.

**Reference Measure**: Fix a reference probability $P^0$ (often Wiener measure).

**Set of Priors**: Consider family $\mathcal{P}$ of probability measures on $\Omega$ such that:


$$
\mathcal{P} = \left\{ P: \frac{dP}{dP^0}\bigg|_{\mathcal{F}_t} = \mathcal{E}\left(\int_0^t \theta_s \, dW_s^0\right), \, \theta \in \Theta \right\}
$$



where $\Theta$ represents admissible drifts and volatilities.

**2BSDE**: A triple $(Y, Z, \Gamma)$ of adapted processes satisfying:


$$
Y_t = \sup_{P \in \mathcal{P}} E_P\left[\xi + \int_t^T f(s, Y_s, Z_s) \, ds \bigg| \mathcal{F}_t\right]
$$



for appropriate generator $f$.

### Soner-Touzi-Zhang Formulation

**Viscosity Formulation**: The 2BSDE is defined through:


$$
Y_t = \sup_{\alpha \in \mathcal{A}} E^{\alpha}\left[\xi + \int_t^T f(s, Y_s, Z_s) \, ds \bigg| \mathcal{F}_t\right]
$$



where the supremum is over admissible controls $\alpha$ affecting the quadratic variation.

**Generator**: Nonlinear in second-order term:


$$
F(t, y, z, \gamma) = f(t, y, z) + G(t, y, z, \gamma)
$$



where $G$ captures the second-order nonlinearity.

## Well-Posedness

### Existence and Uniqueness

**Theorem** (Soner-Touzi-Zhang, 2012): Under appropriate conditions on $F$ and $\xi$:
1. **Monotonicity**: $F$ is decreasing in $\gamma$
2. **Lipschitz**: $F$ is Lipschitz in $(y, z)$ uniformly in $\gamma$
3. **Boundedness**: $|F(t, 0, 0, \gamma)| \leq C$ uniformly

There exists a unique solution $(Y, Z, \Gamma)$ to the 2BSDE.

**Proof Sketch**: 
1. Define value function through dynamic programming principle
2. Show it is a viscosity solution to associated PDE
3. Use comparison principle to establish uniqueness
4. Extract $(Z, \Gamma)$ as derivatives

### Comparison Principle

**Theorem**: Let $(Y_1, Z_1, \Gamma_1)$ and $(Y_2, Z_2, \Gamma_2)$ be solutions with terminal conditions $\xi_1 \leq \xi_2$ and generators $F_1 \geq F_2$.

Then:


$$
Y_1^t \leq Y_2^t \quad P\text{-a.s. for all } t
$$



**Proof**: Uses viscosity solution theory and the comparison principle for fully nonlinear PDEs.

## Connection to Fully Nonlinear PDEs

### PDE Representation

**Theorem** (Feynman-Kac for 2BSDEs): If $Y_t = u(t, X_t)$ where $X_t$ is a state process, then $u$ satisfies the **fully nonlinear PDE**:


$$
\frac{\partial u}{\partial t} + \sup_{\sigma \in \Sigma} \left\{ \frac{1}{2} \text{tr}[\sigma \sigma^\top D^2 u] + \mu \cdot \nabla u \right\} + f(t, u, \sigma^\top \nabla u) = 0
$$



with terminal condition $u(T, x) = \Phi(x)$.

**Key Feature**: The supremum over $\sigma$ makes this a **fully nonlinear** second-order PDE, unlike standard BSDEs which give semilinear PDEs.

### Viscosity Solutions

**Definition**: A function $u$ is a viscosity solution if it satisfies:
- **Subsolution**: For any smooth test function $\phi$ with $u - \phi$ attaining a local maximum at $(t_0, x_0)$:

  $$
  \frac{\partial \phi}{\partial t} + F(t, u, D\phi, D^2\phi) \leq 0
  $$



- **Supersolution**: For any smooth test function $\phi$ with $u - \phi$ attaining a local minimum at $(t_0, x_0)$:

  $$
  \frac{\partial \phi}{\partial t} + F(t, u, D\phi, D^2\phi) \geq 0
  $$



**Theorem**: The value function $Y_t = u(t, X_t)$ from the 2BSDE is the unique viscosity solution to the associated fully nonlinear PDE.

### Examples of PDEs

**Example 1** (Uncertain Volatility): For volatility $\sigma \in [\underline{\sigma}, \overline{\sigma}]$:


$$
\frac{\partial u}{\partial t} + \sup_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} \left\{ \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} \right\} + rS \frac{\partial u}{\partial S} - ru = 0
$$



**Solution**: Use $\sigma = \overline{\sigma}$ where $u_{SS} > 0$, and $\sigma = \underline{\sigma}$ where $u_{SS} < 0$.

**Example 2** (G-Expectation): For G-Brownian motion with $\langle W \rangle_t \in [\underline{\sigma}^2 t, \overline{\sigma}^2 t]$:


$$
\frac{\partial u}{\partial t} + G\left(\frac{\partial^2 u}{\partial x^2}\right) = 0
$$



where:


$$
G(a) = \frac{1}{2}\overline{\sigma}^2 a^+ - \frac{1}{2}\underline{\sigma}^2 a^-
$$



## G-Brownian Motion and G-Expectations

### G-Brownian Motion

**Definition**: A process $B_t$ is a **G-Brownian motion** if:
1. $B_0 = 0$
2. Independent increments (in a generalized sense)
3. $B_t - B_s \sim N(\{0\} \times [\underline{\sigma}^2(t-s), \overline{\sigma}^2(t-s)])$ (G-normal distribution)

**Quadratic Variation**: For G-Brownian motion:


$$
\langle B \rangle_t \in [\underline{\sigma}^2 t, \overline{\sigma}^2 t]
$$



with exact value unknown (uncertain).

**G-Function**: The mapping:


$$
G: \mathbb{R}^{d \times d} \to \mathbb{R}
$$



defined by:


$$
G(A) = \frac{1}{2} \sup_{\sigma \in \Sigma} \text{tr}[\sigma \sigma^\top A]
$$



characterizes the quadratic variation uncertainty.

### G-Expectation

**Definition**: The **G-expectation** is defined as:


$$
\mathbb{E}^G[\xi] = Y_0
$$



where $Y_t$ solves the 2BSDE:


$$
Y_t = \sup_{P \in \mathcal{P}_G} E_P[\xi | \mathcal{F}_t]
$$



and $\mathcal{P}_G$ is the set of measures compatible with the G-Brownian motion.

**Properties**:
1. **Sublinearity**: $\mathbb{E}^G[\xi + \eta] \leq \mathbb{E}^G[\xi] + \mathbb{E}^G[\eta]$
2. **Positive homogeneity**: $\mathbb{E}^G[\lambda \xi] = \lambda \mathbb{E}^G[\xi]$ for $\lambda \geq 0$
3. **Monotonicity**: $\xi \geq \eta \implies \mathbb{E}^G[\xi] \geq \mathbb{E}^G[\eta]$
4. **Constant preserving**: $\mathbb{E}^G[c] = c$

**Representation**: Via the 2BSDE with generator:


$$
F(t, y, z, \gamma) = G(\gamma)
$$



### Peng's G-Framework

**G-Itô Formula**: For $f \in C^{1,2}$ and G-Brownian motion $B_t$:


$$
df(t, B_t) = \frac{\partial f}{\partial t} dt + \frac{\partial f}{\partial x} dB_t + G\left(\frac{\partial^2 f}{\partial x^2}\right) d\langle B \rangle_t
$$



where $\langle B \rangle_t$ is the G-quadratic variation.

**G-Martingale**: A process $M_t$ is a G-martingale if:


$$
\mathbb{E}^G[M_t | \mathcal{F}_s] = M_s \quad \text{for } s \leq t
$$



**Theorem**: Every G-martingale can be represented as:


$$
M_t = M_0 + \int_0^t Z_s \, dB_s
$$



for some adapted process $Z_t$.

## Robust Pricing and Hedging

### Super-Replication Under Volatility Uncertainty

**Problem**: Find minimal initial capital $V_0$ such that there exists a hedging strategy with:


$$
V_T \geq \Phi(S_T) \quad P\text{-a.s. for all } P \in \mathcal{P}
$$



**Solution**: The super-replication price is:


$$
V_0 = Y_0
$$



where $Y_t$ solves the 2BSDE:


$$
Y_t = \sup_{P \in \mathcal{P}} E_P[\Phi(S_T) | \mathcal{F}_t]
$$



**Hedging Strategy**: The optimal hedge is:


$$
\Delta_t = Z_t / S_t
$$



where $Z_t$ comes from the 2BSDE solution.

### Duality

**Primal Problem**: 


$$
\inf_{(Y, Z): Y_T \geq \Phi} Y_0
$$



**Dual Problem**:


$$
\sup_{P \in \mathcal{P}} E_P[\Phi(S_T)]
$$



**Theorem** (Strong Duality): Under appropriate conditions:


$$
\inf_{(Y, Z): Y_T \geq \Phi} Y_0 = \sup_{P \in \mathcal{P}} E_P[\Phi(S_T)]
$$



**Proof**: Uses 2BSDE theory and viscosity solutions.

### Incomplete Markets

**Market Structure**: When markets are incomplete due to:
- Volatility uncertainty
- Non-tradeable risk factors
- Transaction costs

2BSDEs provide natural framework for pricing and hedging.

**Pricing Interval**: The arbitrage-free price range is:


$$
[\underline{V}, \overline{V}] = \left[\inf_{P \in \mathcal{P}} E_P[\Phi], \, \sup_{P \in \mathcal{P}} E_P[\Phi]\right]
$$



Both bounds obtained via 2BSDEs.

## Stochastic Target Problems

### Target Formulation

**Problem**: Given terminal constraint $\Phi$, find initial value $y$ such that there exists a strategy making:


$$
Y_T^{y, \theta} \geq \Phi \quad P\text{-a.s. for all } P \in \mathcal{P}
$$



**Stochastic Target**: The set:


$$
\mathcal{V}_t = \{y: \exists \theta \text{ s.t. } Y_T^{y, \theta} \geq \Phi\}
$$



**Value Function**: Define:


$$
u(t, x) = \inf\{y: y \in \mathcal{V}_t(x)\}
$$



**Theorem**: The value function $u$ is a viscosity solution to a fully nonlinear PDE and can be characterized via 2BSDEs.

### Geometric Target

**Target Set**: Instead of terminal payoff, consider reaching a set $\mathcal{T} \subseteq \mathbb{R}^n$:


$$
\text{Find } y \text{ such that } (Y_T, X_T) \in \mathcal{T}
$$



**Characterization**: The reachable set is characterized by:


$$
Y_t = \sup_{P \in \mathcal{P}} \text{ess inf}\left\{\int_t^{\tau} f(s, Y_s, Z_s) \, ds + h(Y_{\tau}, X_{\tau}) \right\}
$$



where $\tau$ is a stopping time and $h$ is the target function.

## Quadratic 2BSDEs

### Definition

**Quadratic Growth**: A 2BSDE where the generator has quadratic growth in $z$:


$$
|F(t, y, z, \gamma)| \leq C(1 + |y| + |z|^2 + |\gamma|)
$$



**Example**: Exponential utility under volatility uncertainty:


$$
F(t, y, z, \gamma) = -\frac{\alpha}{2} |z|^2 + G(\gamma)
$$



### Well-Posedness

**Theorem**: Quadratic 2BSDEs have unique solutions under:
1. Small time horizon $T$
2. Bounded terminal condition
3. Monotonicity in $\gamma$

**Challenge**: Standard Lipschitz arguments fail; requires refined estimates.

**Applications**:
- Large investor models
- Portfolio optimization with ambiguity
- Risk-sensitive control

## Mean-Field 2BSDEs

### Definition

**Mean-Field Interaction**: The generator depends on the law of the solution:


$$
Y_t = \sup_{P \in \mathcal{P}} E_P\left[\xi + \int_t^T F(s, Y_s, Z_s, \mathcal{L}(Y_s)) \, ds \bigg| \mathcal{F}_t\right]
$$



where $\mathcal{L}(Y_s)$ denotes the law of $Y_s$.

**Interpretation**: Large population with model uncertainty and mean-field interactions.

### McKean-Vlasov 2BSDEs

**Coupling**: Forward-backward system:


$$
dX_t = b(t, X_t, \mathcal{L}(X_t)) \, dt + \sigma_t \, dW_t
$$




$$
Y_t = \sup_{P \in \mathcal{P}} E_P\left[\Phi(X_T) + \int_t^T f(s, X_s, Y_s, \mathcal{L}(X_s, Y_s)) \, ds \bigg| \mathcal{F}_t\right]
$$



**Applications**:
- Systemic risk under model uncertainty
- Mean-field games with ambiguity
- Large portfolio optimization

## Numerical Methods

### Finite Difference Schemes

**PDE Discretization**: For the associated fully nonlinear PDE:


$$
\frac{\partial u}{\partial t} + F(t, u, Du, D^2u) = 0
$$



**Scheme**: At each grid point $(t_i, x_j)$:


$$
\frac{u_j^{i+1} - u_j^i}{\Delta t} + F\left(t_i, u_j^i, \frac{u_{j+1}^i - u_{j-1}^i}{2\Delta x}, \frac{u_{j+1}^i - 2u_j^i + u_{j-1}^i}{(\Delta x)^2}\right) = 0
$$



**Monotone Schemes**: Ensure convergence to viscosity solution:
- Use upwind discretization for first derivatives
- Ensure monotonicity in all arguments

### Monte Carlo Methods

**Challenge**: Direct simulation difficult due to supremum over measures.

**Approach 1** (Scenario Sampling): 
1. Discretize $\mathcal{P}$ into finite set $\{P_1, \ldots, P_N\}$
2. Simulate under each $P_i$
3. Take pointwise supremum

**Approach 2** (Least-Squares Monte Carlo):
1. Backward iteration with conditional expectations
2. At each step, optimize over measures in $\mathcal{P}$
3. Use regression to approximate value function

**Complexity**: $O(M \cdot N \cdot K)$ where $M$ is paths, $N$ is measures, $K$ is time steps.

### Deep Learning Approaches

**Neural Network Parameterization**: Represent solution as:


$$
Y_t = f_{\theta_Y}(t, X_t), \quad Z_t = f_{\theta_Z}(t, X_t), \quad \Gamma_t = f_{\theta_{\Gamma}}(t, X_t)
$$



**Training**: Minimize loss:


$$
\mathcal{L}(\theta) = E\left[\left|Y_T - \xi\right|^2 + \int_0^T \left|\frac{dY_t}{dt} + F(t, Y_t, Z_t, \Gamma_t)\right|^2 dt\right]
$$



**Optimization**: Use stochastic gradient descent with mini-batches of simulated paths.

**Advantages**:
- Handles high dimensions
- Bypasses curse of dimensionality
- Scales with complexity

## Advanced Theoretical Results

### Comparison with Classical BSDEs

| **Feature** | **Classical BSDEs** | **2BSDEs** |
|-------------|---------------------|-----------|
| **Generator Order** | First-order in $z$ | Second-order in $\gamma$ |
| **PDE Type** | Semilinear | Fully nonlinear |
| **Uncertainty** | Drift only | Drift + Volatility |
| **Expectations** | Linear (g-expectation) | Sublinear (G-expectation) |
| **Uniqueness** | Standard Lipschitz | Requires monotonicity + viscosity |

### Representation Theorems

**Theorem**: The 2BSDE solution admits representation:


$$
Y_t = \sup_{P \in \mathcal{P}} E_P\left[\xi + \int_t^T f(s, Y_s, Z_s) \, ds \bigg| \mathcal{F}_t\right]
$$



where $\mathcal{P}$ is characterized by the generator $F$.

**Proof**: Uses duality arguments and the minimax theorem.

### Optimal Control Interpretation

**Control Problem**: The 2BSDE can be seen as:


$$
Y_t = \sup_{\alpha \in \mathcal{A}} \inf_{\beta \in \mathcal{B}} E^{\alpha, \beta}\left[\xi + \int_t^T f(s, Y_s, Z_s) \, ds \bigg| \mathcal{F}_t\right]
$$



where:
- $\alpha$: Player 1's control (optimizer)
- $\beta$: Player 2's control (adversary, nature)

**Interpretation**: Two-player zero-sum game under stochastic dynamics.

### Large Deviations

**Connection**: 2BSDEs arise naturally in large deviations theory.

**Rate Function**: The generator $G$ in G-expectation corresponds to rate function in Freidlin-Wentzell theory.

**Application**: Asymptotic analysis of rare events under model uncertainty.

## Applications in Finance

### Uncertain Volatility Models

**Problem**: Price and hedge options when volatility $\sigma_t \in [\underline{\sigma}, \overline{\sigma}]$.

**2BSDE Solution**: Option price $V_t$ satisfies:


$$
V_t = \sup_{P \in \mathcal{P}_{\sigma}} E_P[\Phi(S_T) | \mathcal{F}_t]
$$



**Hedging**: Optimal delta is:


$$
\Delta_t = \frac{Z_t}{S_t}
$$



**Gamma Exposure**: Second-order term $\Gamma_t$ captures residual gamma risk.

### Portfolio Optimization with Ambiguity

**Problem**: Maximize worst-case expected utility:


$$
\sup_{\pi} \inf_{P \in \mathcal{P}} E_P[U(X_T^{\pi})]
$$



**2BSDE Formulation**: Value function:


$$
V(t, x) = \sup_{\pi} \inf_{P \in \mathcal{P}} E_P[U(X_T^{\pi}) | X_t = x]
$$



satisfies a 2BSDE.

**Optimal Policy**: Extracted from $(Z_t, \Gamma_t)$ in the solution.

### Robust CVA

**Credit Valuation Adjustment**: Accounting for counterparty default risk under model uncertainty.

**2BSDE Framework**: CVA satisfies:


$$
\text{CVA}_t = \sup_{P \in \mathcal{P}} E_P\left[\int_t^T e^{-\int_t^s r_u du} dL_s \bigg| \mathcal{F}_t\right]
$$



where $L_t$ is the loss process.

**Uncertainty**: In default intensity, recovery rate, and correlation.

### Dynamic Risk Measures

**Time-Consistent Risk**: For dynamic coherent risk measure $\rho_t$:


$$
\rho_t(X) = Y_t
$$



where $Y_t$ solves a 2BSDE with appropriate generator.

**Regulatory Capital**: Basel III and Solvency II requirements can be formulated using 2BSDEs with volatility uncertainty.

## Connections to Other Theories

### Optimal Transport

**2BSDEs and Martingale Optimal Transport**: When the constraint set $\mathcal{P}$ consists of martingale measures, 2BSDEs connect to martingale optimal transport problems.

**Duality**: The dual of the 2BSDE provides bounds similar to MOT bounds.

### Game Theory

**Stochastic Differential Games**: 2BSDEs arise in zero-sum stochastic differential games with incomplete information.

**Isaacs Equation**: The associated PDE is the Isaacs equation from game theory.

### Robust Control

**H-infinity Control**: 2BSDEs provide probabilistic formulation of H-infinity robust control problems.

**Disturbance Attenuation**: The supremum over measures corresponds to worst-case disturbance.

## Open Problems and Research Directions

### Theoretical Challenges

1. **Quadratic Growth**: General well-posedness theory for quadratic 2BSDEs remains incomplete.

2. **Non-Markovian Settings**: Extending 2BSDEs beyond Markovian frameworks.

3. **Infinite Dimensions**: 2BSDEs in infinite-dimensional spaces (SPDEs, measure-valued processes).

4. **Mean-Field Limits**: Rigorous convergence results for large-population limits.

### Computational Challenges

1. **High Dimensions**: Efficient algorithms for high-dimensional 2BSDEs.

2. **Measure Optimization**: Tractable methods for optimizing over infinite-dimensional measure spaces.

3. **Neural Network Training**: Theoretical guarantees for deep learning approaches.

### Applications

1. **Market Microstructure**: Incorporating model uncertainty into high-frequency trading models.

2. **Climate Finance**: Pricing climate derivatives under model uncertainty.

3. **Insurance**: Robust reserving and pricing under longevity uncertainty.

4. **Systemic Risk**: Mean-field 2BSDEs for large financial networks.

## Summary and Key Insights

### Fundamental Contributions

1. **Volatility Uncertainty**: 2BSDEs provide rigorous framework for pricing and hedging when quadratic variation is uncertain.

2. **Fully Nonlinear PDEs**: Offer probabilistic representation for fully nonlinear second-order PDEs through viscosity solutions.

3. **G-Expectations**: Generalize nonlinear expectations to sublinear framework capturing fundamental uncertainty.

4. **Robust Valuation**: Connect to minimax optimization, providing worst-case valuations under model uncertainty.

5. **Stochastic Target**: Unify reachability problems with BSDE theory.

### Practical Implications

**For Traders**:
- Robust pricing bounds under volatility uncertainty
- Model-free hedging strategies
- Quantification of model risk

**For Risk Managers**:
- Worst-case risk measures
- Stress testing under fundamental uncertainty
- Regulatory capital with model risk

**For Researchers**:
- Rigorous mathematical foundations for robust finance
- Bridge between probability, PDEs, and control theory
- Framework for handling irreducible uncertainty

### Theoretical Significance

2BSDEs represent a major advance in stochastic analysis, unifying:
- **Backward SDEs**: Extending to fully nonlinear settings
- **Viscosity Solutions**: Providing probabilistic counterpart
- **Robust Optimization**: Connecting to minimax problems
- **Stochastic Control**: Generalizing classical optimal control

The theory continues to develop rapidly, with ongoing research addressing computational challenges, extending to new application domains, and deepening theoretical understanding of nonlinear expectations and robust valuation under fundamental uncertainty.
