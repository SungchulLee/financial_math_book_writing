# Second-Order BSDEs (2BSDEs)


## Introduction


**Second-order backward stochastic differential equations (2BSDEs)** represent a fundamental generalization of classical BSDEs that naturally arise when considering **model uncertainty** or **volatility uncertainty** in financial mathematics. Introduced by Soner, Touzi, and Zhang (2012), 2BSDEs provide a rigorous framework for:

1. **Robust pricing and hedging**: Derivative valuation under volatility uncertainty
2. **Viscosity solutions**: Probabilistic representation for fully nonlinear second-order PDEs
3. **Stochastic target problems**: Reachability under model ambiguity
4. **G-expectations**: Generalized nonlinear expectations under volatility uncertainty

The key innovation is that 2BSDEs account for uncertainty in the **quadratic variation** of the driving process, not just its drift, leading to fully nonlinear equations and connections to second-order PDEs.

## Mathematical Framework


### 1. Classical BSDEs (Review)


**Standard BSDE**: A pair $(Y_t, Z_t)$ satisfying:


$$
Y_t = \xi + \int_t^T g(s, Y_s, Z_s) \, ds - \int_t^T Z_s \, dW_s
$$



where $g$ is the generator (first-order in $z$).

**Limitation**: Assumes fixed quadratic variation of the Brownian motion:


$$
d\langle W \rangle_t = dt
$$



### 2. Volatility Uncertainty


**Setup**: Uncertain volatility matrix $\sigma_t$ with:


$$
\underline{a} \leq \sigma_t \sigma_t^\top \leq \overline{a}
$$



in the positive semidefinite ordering.

**Canonical Space**: Consider all semimartingales with quadratic variation in the specified range.

**Question**: How to define expectations and valuations that are robust to this uncertainty?

## Definition of 2BSDEs


### 1. Informal Definition


A **second-order BSDE** is an equation of the form:


$$
Y_t = \xi + \int_t^T F(s, Y_s, Z_s, \Gamma_s) \, ds - \int_t^T Z_s \, dW_s - \int_t^T \text{tr}[\Gamma_s d\langle W \rangle_s]
$$



where:
- $F$: Generator (nonlinear, second-order)
- $\Gamma_t$: Second-order process (matrix-valued)
- $\langle W \rangle_t$: Quadratic variation of $W$

**Key Feature**: The generator $F$ depends on $\Gamma$, which interacts with uncertain quadratic variation.

### 2. Formal Framework


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

### 3. Soner-Touzi-Zhang Formulation


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


### 1. Existence and Uniqueness


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

### 2. Comparison Principle


**Theorem**: Let $(Y_1, Z_1, \Gamma_1)$ and $(Y_2, Z_2, \Gamma_2)$ be solutions with terminal conditions $\xi_1 \leq \xi_2$ and generators $F_1 \geq F_2$.

Then:


$$
Y_1^t \leq Y_2^t \quad P\text{-a.s. for all } t
$$



**Proof**: Uses viscosity solution theory and the comparison principle for fully nonlinear PDEs.

## Connection to Fully Nonlinear PDEs


### 1. PDE Representation


**Theorem** (Feynman-Kac for 2BSDEs): If $Y_t = u(t, X_t)$ where $X_t$ is a state process, then $u$ satisfies the **fully nonlinear PDE**:


$$
\frac{\partial u}{\partial t} + \sup_{\sigma \in \Sigma} \left\{ \frac{1}{2} \text{tr}[\sigma \sigma^\top D^2 u] + \mu \cdot \nabla u \right\} + f(t, u, \sigma^\top \nabla u) = 0
$$



with terminal condition $u(T, x) = \Phi(x)$.

**Key Feature**: The supremum over $\sigma$ makes this a **fully nonlinear** second-order PDE, unlike standard BSDEs which give semilinear PDEs.

### 2. Viscosity Solutions


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

### 3. Examples of PDEs


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


### 1. G-Brownian Motion


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

### 2. G-Expectation


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



### 3. Peng's G-Framework


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


### 1. Super-Replication Under Volatility Uncertainty


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

### 2. Duality


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

### 3. Incomplete Markets


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


### 1. Target Formulation


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

### 2. Geometric Target


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


### 1. Definition


**Quadratic Growth**: A 2BSDE where the generator has quadratic growth in $z$:


$$
|F(t, y, z, \gamma)| \leq C(1 + |y| + |z|^2 + |\gamma|)
$$



**Example**: Exponential utility under volatility uncertainty:


$$
F(t, y, z, \gamma) = -\frac{\alpha}{2} |z|^2 + G(\gamma)
$$



### 2. Well-Posedness


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


### 1. Definition


**Mean-Field Interaction**: The generator depends on the law of the solution:


$$
Y_t = \sup_{P \in \mathcal{P}} E_P\left[\xi + \int_t^T F(s, Y_s, Z_s, \mathcal{L}(Y_s)) \, ds \bigg| \mathcal{F}_t\right]
$$



where $\mathcal{L}(Y_s)$ denotes the law of $Y_s$.

**Interpretation**: Large population with model uncertainty and mean-field interactions.

### 2. McKean-Vlasov 2BSDEs


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


### 1. Finite Difference Schemes


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

### 2. Monte Carlo Methods


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

### 3. Deep Learning Approaches


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


### 1. Comparison with Classical BSDEs


| **Feature** | **Classical BSDEs** | **2BSDEs** |
|-------------|---------------------|-----------|
| **Generator Order** | First-order in $z$ | Second-order in $\gamma$ |
| **PDE Type** | Semilinear | Fully nonlinear |
| **Uncertainty** | Drift only | Drift + Volatility |
| **Expectations** | Linear (g-expectation) | Sublinear (G-expectation) |
| **Uniqueness** | Standard Lipschitz | Requires monotonicity + viscosity |

### 2. Representation Theorems


**Theorem**: The 2BSDE solution admits representation:


$$
Y_t = \sup_{P \in \mathcal{P}} E_P\left[\xi + \int_t^T f(s, Y_s, Z_s) \, ds \bigg| \mathcal{F}_t\right]
$$



where $\mathcal{P}$ is characterized by the generator $F$.

**Proof**: Uses duality arguments and the minimax theorem.

### 3. Optimal Control Interpretation


**Control Problem**: The 2BSDE can be seen as:


$$
Y_t = \sup_{\alpha \in \mathcal{A}} \inf_{\beta \in \mathcal{B}} E^{\alpha, \beta}\left[\xi + \int_t^T f(s, Y_s, Z_s) \, ds \bigg| \mathcal{F}_t\right]
$$



where:
- $\alpha$: Player 1's control (optimizer)
- $\beta$: Player 2's control (adversary, nature)

**Interpretation**: Two-player zero-sum game under stochastic dynamics.

### 4. Large Deviations


**Connection**: 2BSDEs arise naturally in large deviations theory.

**Rate Function**: The generator $G$ in G-expectation corresponds to rate function in Freidlin-Wentzell theory.

**Application**: Asymptotic analysis of rare events under model uncertainty.

## Applications in Finance


### 1. Uncertain Volatility Models


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

### 2. Portfolio Optimization with Ambiguity


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

### 3. Robust CVA


**Credit Valuation Adjustment**: Accounting for counterparty default risk under model uncertainty.

**2BSDE Framework**: CVA satisfies:


$$
\text{CVA}_t = \sup_{P \in \mathcal{P}} E_P\left[\int_t^T e^{-\int_t^s r_u du} dL_s \bigg| \mathcal{F}_t\right]
$$



where $L_t$ is the loss process.

**Uncertainty**: In default intensity, recovery rate, and correlation.

### 4. Dynamic Risk Measures


**Time-Consistent Risk**: For dynamic coherent risk measure $\rho_t$:


$$
\rho_t(X) = Y_t
$$



where $Y_t$ solves a 2BSDE with appropriate generator.

**Regulatory Capital**: Basel III and Solvency II requirements can be formulated using 2BSDEs with volatility uncertainty.

## Connections to Other Theories


### 1. Optimal Transport


**2BSDEs and Martingale Optimal Transport**: When the constraint set $\mathcal{P}$ consists of martingale measures, 2BSDEs connect to martingale optimal transport problems.

**Duality**: The dual of the 2BSDE provides bounds similar to MOT bounds.

### 2. Game Theory


**Stochastic Differential Games**: 2BSDEs arise in zero-sum stochastic differential games with incomplete information.

**Isaacs Equation**: The associated PDE is the Isaacs equation from game theory.

### 3. Robust Control


**H-infinity Control**: 2BSDEs provide probabilistic formulation of H-infinity robust control problems.

**Disturbance Attenuation**: The supremum over measures corresponds to worst-case disturbance.

## Open Problems and Research Directions


### 1. Theoretical Challenges


1. **Quadratic Growth**: General well-posedness theory for quadratic 2BSDEs remains incomplete.

2. **Non-Markovian Settings**: Extending 2BSDEs beyond Markovian frameworks.

3. **Infinite Dimensions**: 2BSDEs in infinite-dimensional spaces (SPDEs, measure-valued processes).

4. **Mean-Field Limits**: Rigorous convergence results for large-population limits.

### 2. Computational Challenges


1. **High Dimensions**: Efficient algorithms for high-dimensional 2BSDEs.

2. **Measure Optimization**: Tractable methods for optimizing over infinite-dimensional measure spaces.

3. **Neural Network Training**: Theoretical guarantees for deep learning approaches.

### 3. Applications


1. **Market Microstructure**: Incorporating model uncertainty into high-frequency trading models.

2. **Climate Finance**: Pricing climate derivatives under model uncertainty.

3. **Insurance**: Robust reserving and pricing under longevity uncertainty.

4. **Systemic Risk**: Mean-field 2BSDEs for large financial networks.

## Summary and Key Insights


### 1. Fundamental Contributions


1. **Volatility Uncertainty**: 2BSDEs provide rigorous framework for pricing and hedging when quadratic variation is uncertain.

2. **Fully Nonlinear PDEs**: Offer probabilistic representation for fully nonlinear second-order PDEs through viscosity solutions.

3. **G-Expectations**: Generalize nonlinear expectations to sublinear framework capturing fundamental uncertainty.

4. **Robust Valuation**: Connect to minimax optimization, providing worst-case valuations under model uncertainty.

5. **Stochastic Target**: Unify reachability problems with BSDE theory.

### 2. Practical Implications


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

### 3. Theoretical Significance


2BSDEs represent a major advance in stochastic analysis, unifying:
- **Backward SDEs**: Extending to fully nonlinear settings
- **Viscosity Solutions**: Providing probabilistic counterpart
- **Robust Optimization**: Connecting to minimax problems
- **Stochastic Control**: Generalizing classical optimal control

The theory continues to develop rapidly, with ongoing research addressing computational challenges, extending to new application domains, and deepening theoretical understanding of nonlinear expectations and robust valuation under fundamental uncertainty.

---

## Exercises

**Exercise 1.** A standard BSDE has the form $-dY_t = f(t, Y_t, Z_t) \, dt - Z_t \, dW_t$ with terminal condition $Y_T = \xi$. Explain the key difference between a BSDE and a 2BSDE, which has the form $-dY_t = f(t, Y_t, Z_t, \hat{a}_t) \, dt - Z_t \, dW_t$ where $\hat{a}_t$ represents the uncertain quadratic variation. Why does the 2BSDE require a family of probability measures rather than a single one?

??? success "Solution to Exercise 1"

    **Key difference between BSDEs and 2BSDEs.**

    In a standard BSDE, the driving noise is a Brownian motion $W_t$ on a fixed probability space $(\Omega, \mathcal{F}, P)$, and the quadratic variation is deterministic: $d\langle W \rangle_t = dt$. The generator $f(t, Y_t, Z_t)$ depends only on the value process $Y_t$ and the control process $Z_t$. The solution $(Y_t, Z_t)$ is computed under the single measure $P$.

    In a 2BSDE, the generator $f(t, Y_t, Z_t, \hat{a}_t)$ depends additionally on $\hat{a}_t$, which represents the (uncertain) quadratic variation of the canonical process. The equation takes the form:

    $$
    -dY_t = f(t, Y_t, Z_t, \hat{a}_t) \, dt - Z_t \, dW_t
    $$

    where $\hat{a}_t = d\langle W \rangle_t / dt$ is no longer fixed at 1 but can vary within bounds $[\underline{a}, \overline{a}]$.

    **Why a family of probability measures is required.** Under a single probability measure $P$, the quadratic variation of the canonical process is determined. To capture uncertainty in the quadratic variation (i.e., volatility uncertainty), one must consider a family $\mathcal{P}$ of probability measures, each corresponding to a different volatility scenario. Under measure $P^\alpha \in \mathcal{P}$, the canonical process has quadratic variation $\hat{a}^\alpha_t \, dt$ with $\hat{a}^\alpha_t \in [\underline{a}, \overline{a}]$.

    The 2BSDE solution is then defined as:

    $$
    Y_t = \sup_{P \in \mathcal{P}} E_P\left[\xi + \int_t^T f(s, Y_s, Z_s, \hat{a}_s) \, ds \bigg| \mathcal{F}_t\right]
    $$

    The supremum over $\mathcal{P}$ encodes the worst-case evaluation over all admissible volatility scenarios. This is fundamentally different from a standard BSDE, where only a single measure is used, and it is precisely this feature that connects 2BSDEs to fully nonlinear (rather than semilinear) PDEs.

---

**Exercise 2.** For the linear BSDE $-dY_t = (\alpha Y_t + \beta Z_t) \, dt - Z_t \, dW_t$ with $Y_T = \xi$, show that the solution is $Y_t = \mathbb{E}_t^{\mathbb{Q}}[e^{-\alpha(T-t)}\xi]$ where $\mathbb{Q}$ is the measure under which $\tilde{W}_t = W_t - \beta t$ is a Brownian motion. Then explain why no such simple representation exists for the nonlinear generator in a 2BSDE.

??? success "Solution to Exercise 2"

    **Solving the linear BSDE.**

    Consider the BSDE:

    $$
    -dY_t = (\alpha Y_t + \beta Z_t) \, dt - Z_t \, dW_t, \quad Y_T = \xi
    $$

    Define $\tilde{W}_t = W_t - \beta t$ and let $\mathbb{Q}$ be the measure under which $\tilde{W}_t$ is a Brownian motion, given by Girsanov's theorem with Radon-Nikodym derivative:

    $$
    \frac{d\mathbb{Q}}{dP}\bigg|_{\mathcal{F}_t} = \mathcal{E}\left(\int_0^t \beta \, dW_s\right) = \exp\left(\beta W_t - \frac{\beta^2}{2}t\right)
    $$

    Under $\mathbb{Q}$, the BSDE becomes:

    $$
    -dY_t = \alpha Y_t \, dt - Z_t \, d\tilde{W}_t
    $$

    since $Z_t \, dW_t = Z_t \, d\tilde{W}_t + \beta Z_t \, dt$. Now define $\hat{Y}_t = e^{\alpha t} Y_t$. By the product rule:

    $$
    d\hat{Y}_t = \alpha e^{\alpha t} Y_t \, dt + e^{\alpha t} \, dY_t = \alpha e^{\alpha t} Y_t \, dt + e^{\alpha t}(-\alpha Y_t \, dt + Z_t \, d\tilde{W}_t) = e^{\alpha t} Z_t \, d\tilde{W}_t
    $$

    So $\hat{Y}_t$ is a $\mathbb{Q}$-martingale. Taking conditional expectations:

    $$
    e^{\alpha t} Y_t = E_\mathbb{Q}[e^{\alpha T} Y_T | \mathcal{F}_t] = E_\mathbb{Q}[e^{\alpha T} \xi | \mathcal{F}_t]
    $$

    Therefore:

    $$
    Y_t = E_\mathbb{Q}\left[e^{-\alpha(T-t)} \xi \bigg| \mathcal{F}_t\right]
    $$

    At $t = 0$, this gives $\mathcal{E}_g[\xi] = Y_0 = E_\mathbb{Q}[e^{-\alpha T} \xi]$.

    **Why no such representation exists for 2BSDEs.** The linear BSDE admits this closed-form representation because the generator $g(t, y, z) = \alpha y + \beta z$ is linear in $(y, z)$. Linearity allows a single measure change (Girsanov) to absorb the generator entirely, reducing the problem to a classical expectation.

    In a 2BSDE, the generator $F(t, y, z, \gamma)$ depends nonlinearly on the second-order term $\gamma$, which interacts with the uncertain quadratic variation. The nonlinearity means:

    1. No single measure change can absorb $F$ --- one would need different measures for different values of $\gamma$.
    2. The supremum over measures $\mathcal{P}$ is intrinsic to the problem and cannot be reduced to evaluation under a single measure.
    3. The associated PDE is fully nonlinear, not semilinear, so the classical Feynman-Kac representation (which works for linear and semilinear PDEs) does not apply directly.

---

**Exercise 3.** The Soner-Touzi-Zhang wellposedness result for 2BSDEs requires the generator to satisfy certain regularity conditions. State these conditions and explain their financial interpretation. In particular, why is the Lipschitz condition on the generator important for ensuring the uniqueness of the robust derivative price?

??? success "Solution to Exercise 3"

    **Soner-Touzi-Zhang well-posedness conditions.**

    The well-posedness result for 2BSDEs requires the generator $F(t, y, z, \gamma)$ to satisfy:

    **(C1) Monotonicity in $\gamma$**: $F$ is decreasing in $\gamma$ in the sense that for $\gamma_1 \leq \gamma_2$ (in the positive semidefinite ordering):

    $$
    F(t, y, z, \gamma_1) \geq F(t, y, z, \gamma_2)
    $$

    **(C2) Lipschitz continuity in $(y, z)$**: There exists a constant $K > 0$ such that for all $(t, \gamma)$:

    $$
    |F(t, y_1, z_1, \gamma) - F(t, y_2, z_2, \gamma)| \leq K(|y_1 - y_2| + |z_1 - z_2|)
    $$

    **(C3) Uniform boundedness**: $|F(t, 0, 0, \gamma)| \leq C$ for some constant $C$, uniformly in $(t, \gamma)$.

    **Financial interpretation of each condition:**

    - **Monotonicity in $\gamma$ (C1)**: In the context of uncertain volatility, higher gamma exposure (larger $\gamma$) means the portfolio is more exposed to volatility moves. The monotonicity condition says that increasing gamma exposure decreases the generator, which corresponds to the fact that the worst-case cost of volatility uncertainty is higher when gamma is larger. This ensures that the optimization over volatility scenarios has a well-defined structure --- nature's choice of volatility is adversarial and consistent.

    - **Lipschitz condition (C2)**: This ensures that small perturbations in the portfolio value $y$ or hedging strategy $z$ lead to small changes in the generator. Financially, this means that the pricing rule is stable: nearby portfolios or hedging strategies produce nearby prices. Without this condition, two nearly identical derivative positions could have vastly different robust prices, which would be economically unreasonable. For uniqueness, the Lipschitz condition provides the contraction property needed for the Picard iteration to converge to a unique fixed point, ensuring that the robust derivative price is unique.

    - **Boundedness (C3)**: This ensures that the generator does not explode when the position is zero, preventing degenerate solutions. Financially, it means the cost of model uncertainty for a zero position is finite.

    The **Lipschitz condition is particularly important for uniqueness** because it ensures that the mapping from terminal conditions to initial values (the pricing operator) is a contraction. Without it, multiple solutions to the 2BSDE could exist, meaning the robust derivative price would be ambiguous --- there would be multiple values that are self-consistently "robust," undermining the usefulness of the framework.

---

**Exercise 4.** Show that the superhedging price under uncertain volatility $\sigma_t \in [\underline{\sigma}, \overline{\sigma}]$ can be characterized as the solution of a 2BSDE with generator $f(t, y, z, a) = -rz + \frac{1}{2}\overline{\sigma}^2 |z|^2 \mathbb{1}_{z \geq 0} + \frac{1}{2}\underline{\sigma}^2 |z|^2 \mathbb{1}_{z < 0}$. Verify that this reduces to the BSB equation in the Markovian case.

??? success "Solution to Exercise 4"

    **Characterization of the superhedging price via 2BSDE.**

    Consider a stock $S_t$ with uncertain volatility $\sigma_t \in [\underline{\sigma}, \overline{\sigma}]$. Under risk-neutral pricing, the stock dynamics are $dS_t = rS_t \, dt + \sigma_t S_t \, dW_t$. The superhedging price is:

    $$
    V_t = \sup_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} E^\sigma\left[e^{-r(T-t)} \Phi(S_T) \bigg| \mathcal{F}_t\right]
    $$

    The 2BSDE formulation is: find $(Y_t, Z_t)$ such that

    $$
    Y_t = e^{-rT}\Phi(S_T) + \int_t^T f(s, Y_s, Z_s, \hat{a}_s) \, ds - \int_t^T Z_s \, dW_s
    $$

    where $\hat{a}_t = \sigma_t^2$ is the uncertain quadratic variation rate and the generator is:

    $$
    f(t, y, z, a) = -ry + \frac{1}{2}a|z|^2 \cdot \text{(sign-dependent term)}
    $$

    More precisely, let us work in log-stock coordinates. The superhedging price $V(t, S)$ satisfies the BSB equation:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^{*2} S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0
    $$

    where $\sigma^{*2} = \overline{\sigma}^2$ when $\Gamma = \partial^2 V / \partial S^2 > 0$ and $\sigma^{*2} = \underline{\sigma}^2$ when $\Gamma < 0$.

    In the 2BSDE framework with $Y_t = V(t, S_t)$ and $Z_t = S_t \frac{\partial V}{\partial S}(t, S_t)$, the generator can be written as:

    $$
    f(t, y, z, a) = -ry + \frac{1}{2}a \cdot \Gamma_t S_t^2
    $$

    where nature chooses $a = \overline{\sigma}^2$ if $\Gamma_t > 0$ and $a = \underline{\sigma}^2$ if $\Gamma_t < 0$. This is equivalently:

    $$
    f(t, y, z, \Gamma) = -ry + \frac{1}{2}\overline{\sigma}^2 S^2 \Gamma^+ - \frac{1}{2}\underline{\sigma}^2 S^2 \Gamma^-
    $$

    where $\Gamma^+ = \max(\Gamma, 0)$ and $\Gamma^- = \max(-\Gamma, 0)$.

    **Reduction to BSB equation in the Markovian case.** If $Y_t = u(t, S_t)$ for a smooth function $u$, then by Ito's formula:

    $$
    dY_t = \left(\frac{\partial u}{\partial t} + rS\frac{\partial u}{\partial S} + \frac{1}{2}\sigma_t^2 S^2 \frac{\partial^2 u}{\partial S^2}\right) dt + \sigma_t S \frac{\partial u}{\partial S} \, dW_t
    $$

    Matching with the 2BSDE dynamics and optimizing over $\sigma_t$ yields:

    $$
    \frac{\partial u}{\partial t} + rS\frac{\partial u}{\partial S} + \sup_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} - ru = 0
    $$

    The supremum selects $\overline{\sigma}$ when $\frac{\partial^2 u}{\partial S^2} > 0$ and $\underline{\sigma}$ when $\frac{\partial^2 u}{\partial S^2} < 0$, which is precisely the Black-Scholes-Barenblatt equation with terminal condition $u(T, S) = \Phi(S)$.

---

**Exercise 5.** Describe a numerical scheme for solving 2BSDEs based on the branching diffusion method or the deep learning approach. For the deep learning approach, explain how the neural network parameterizes the control $Z_t$ and how the loss function enforces the terminal condition $Y_T = \xi$ and the dynamics. What are the main computational challenges compared to standard BSDEs?

??? success "Solution to Exercise 5"

    **Deep learning approach for solving 2BSDEs.**

    The deep learning method for 2BSDEs, extending the approach of Han, Jentzen, and E (2018) for standard BSDEs, parameterizes the solution using neural networks and trains by minimizing a loss that enforces the 2BSDE dynamics and terminal condition.

    **Neural network parameterization.** Discretize $[0, T]$ into $N$ time steps $0 = t_0 < t_1 < \cdots < t_N = T$ with $\Delta t = T/N$. The unknowns are:

    - $Y_0 \in \mathbb{R}$: the initial value (a trainable scalar)
    - $Z_{t_i} = f_{\theta_Z^i}(t_i, X_{t_i})$: neural networks approximating the control process at each time step
    - $\Gamma_{t_i} = f_{\theta_\Gamma^i}(t_i, X_{t_i})$: neural networks approximating the second-order process

    **Forward simulation.** Simulate the state process $X_t$ forward:

    $$
    X_{t_{i+1}} = X_{t_i} + b(t_i, X_{t_i})\Delta t + \sigma_{t_i} \Delta W_i
    $$

    where $\sigma_{t_i}$ is chosen adversarially based on $\Gamma_{t_i}$:

    $$
    \sigma_{t_i}^* = \arg\sup_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} \frac{1}{2}\sigma^2 \Gamma_{t_i}
    $$

    **Backward iteration.** Update $Y$ using the Euler discretization of the 2BSDE:

    $$
    Y_{t_{i+1}} = Y_{t_i} - F(t_i, Y_{t_i}, Z_{t_i}, \Gamma_{t_i})\Delta t + Z_{t_i} \Delta W_i
    $$

    **Loss function.** The loss enforces the terminal condition:

    $$
    \mathcal{L}(\theta) = E\left[\left|Y_{t_N} - \xi(X_{t_N})\right|^2\right]
    $$

    where $Y_{t_N}$ is obtained by iterating the discrete dynamics forward from $Y_0$ using the neural network approximations.

    An alternative, more robust loss includes both terminal mismatch and dynamics residual:

    $$
    \mathcal{L}(\theta) = E\left[\left|Y_{t_N} - \xi\right|^2 + \lambda \sum_{i=0}^{N-1} \left|Y_{t_{i+1}} - Y_{t_i} + F(t_i, Y_{t_i}, Z_{t_i}, \Gamma_{t_i})\Delta t - Z_{t_i}\Delta W_i\right|^2\right]
    $$

    **Optimization.** Use stochastic gradient descent (Adam optimizer) with mini-batches of simulated paths. At each training iteration:

    1. Sample a batch of $M$ Brownian paths $\{\Delta W_i^{(m)}\}$
    2. Forward propagate to compute $\{Y_{t_N}^{(m)}\}$
    3. Compute loss and backpropagate
    4. Update parameters $\theta$

    **Main computational challenges compared to standard BSDEs:**

    1. **Optimization over measures**: At each time step, the worst-case volatility must be determined based on $\Gamma_{t_i}$. This inner optimization adds computational cost and can introduce instability.

    2. **Second-order process $\Gamma_t$**: Approximating $\Gamma_t$ requires either an additional neural network (increasing the parameter space) or computing second derivatives of $Y$ with respect to $X$ (requiring higher-order automatic differentiation).

    3. **Non-convexity**: The loss landscape for 2BSDEs is more complex due to the interplay between the adversarial volatility choice and the neural network parameters, making convergence slower and less reliable.

    4. **Stability**: The supremum over measures can amplify numerical errors. Small errors in $\Gamma_t$ can lead to incorrect volatility selection, which propagates and accumulates over time steps.

    5. **Curse of dimensionality for the measure space**: While neural networks handle high-dimensional state spaces well, the optimization over the measure space $\mathcal{P}$ adds an additional layer of complexity absent in standard BSDEs.

---

**Exercise 6.** The connection between 2BSDEs and fully nonlinear PDEs is established through the nonlinear Feynman-Kac formula. State this formula and explain how the solution $u(t, x)$ of the fully nonlinear PDE $\partial_t u + G(D^2 u) = 0$ with $G(A) = \sup_{\sigma \in [\underline{\sigma}, \overline{\sigma}]}\frac{1}{2}\sigma^2 A$ is related to the 2BSDE solution. Why is the viscosity solution concept necessary here?

??? success "Solution to Exercise 6"

    **Nonlinear Feynman-Kac formula for 2BSDEs.**

    **Statement.** Let $(Y_t, Z_t, \Gamma_t)$ be the solution of a 2BSDE with generator $F(t, y, z, \gamma)$ and terminal condition $\xi = \Phi(X_T)$, where $X_t$ is a state process. If $Y_t = u(t, X_t)$ for a function $u: [0,T] \times \mathbb{R}^d \to \mathbb{R}$, then $u$ is the unique viscosity solution of the fully nonlinear PDE:

    $$
    \frac{\partial u}{\partial t}(t, x) + \sup_{\sigma \in \Sigma}\left\{\frac{1}{2}\text{tr}[\sigma\sigma^\top D^2 u(t,x)] + \mu(t,x) \cdot \nabla u(t,x)\right\} + f(t, u, \sigma^\top \nabla u) = 0
    $$

    with terminal condition $u(T, x) = \Phi(x)$.

    **Application to the G-heat equation.** For the specific case where $F(t, y, z, \gamma) = G(\gamma)$ with:

    $$
    G(A) = \sup_{\sigma \in [\underline{\sigma}, \overline{\sigma}]} \frac{1}{2}\sigma^2 A = \frac{1}{2}\overline{\sigma}^2 A^+ - \frac{1}{2}\underline{\sigma}^2 A^-
    $$

    the associated PDE is:

    $$
    \frac{\partial u}{\partial t} + G\left(\frac{\partial^2 u}{\partial x^2}\right) = 0
    $$

    The 2BSDE solution $Y_t = u(t, B_t)$ where $B_t$ is the G-Brownian motion satisfies:

    $$
    Y_t = \sup_{P \in \mathcal{P}_G} E_P[\Phi(B_T) | \mathcal{F}_t]
    $$

    The connection is established as follows. Apply the G-Ito formula to $u(t, B_t)$:

    $$
    du(t, B_t) = \frac{\partial u}{\partial t} \, dt + \frac{\partial u}{\partial x} \, dB_t + \frac{1}{2}\frac{\partial^2 u}{\partial x^2} \, d\langle B \rangle_t
    $$

    Since $d\langle B \rangle_t = \hat{a}_t \, dt$ with $\hat{a}_t \in [\underline{\sigma}^2, \overline{\sigma}^2]$, the PDE condition $\partial_t u + G(\partial_{xx} u) = 0$ ensures that:

    $$
    \frac{\partial u}{\partial t} + \frac{1}{2}\hat{a}_t \frac{\partial^2 u}{\partial x^2} \leq 0
    $$

    for all admissible $\hat{a}_t$, with equality attained by the worst-case choice. This makes $u(t, B_t)$ a G-supermartingale that achieves its supremum, connecting the PDE solution to the 2BSDE value process.

    Identifying $Z_t = \frac{\partial u}{\partial x}(t, B_t)$ and $\Gamma_t = \frac{\partial^2 u}{\partial x^2}(t, B_t)$ completes the correspondence: $(Y_t, Z_t, \Gamma_t)$ solves the 2BSDE if and only if $u$ solves the fully nonlinear PDE.

    **Why the viscosity solution concept is necessary.** The viscosity solution framework is essential for several reasons:

    1. **Lack of classical regularity**: The PDE $\partial_t u + G(D^2 u) = 0$ is fully nonlinear. Unlike semilinear PDEs arising from standard BSDEs, classical (smooth) solutions may not exist. For example, when the payoff $\Phi$ is not smooth (e.g., a call option payoff $(x - K)^+$), the solution $u$ inherits this lack of smoothness.

    2. **Discontinuous coefficients**: The function $G(A) = \frac{1}{2}\overline{\sigma}^2 A^+ - \frac{1}{2}\underline{\sigma}^2 A^-$ has a kink at $A = 0$. When $D^2 u$ changes sign, the PDE effectively switches between two different equations, and the solution may not be $C^2$ at the switching boundary.

    3. **Comparison principle and uniqueness**: Viscosity solution theory provides a comparison principle for fully nonlinear PDEs: if $u$ is a viscosity subsolution and $v$ is a viscosity supersolution with $u(T, \cdot) \leq v(T, \cdot)$, then $u \leq v$ on $[0, T] \times \mathbb{R}^d$. This is the key tool for establishing uniqueness of the 2BSDE solution.

    4. **Stability under approximation**: Viscosity solutions are stable under uniform convergence of approximating equations, which is crucial for the convergence of numerical schemes (finite differences, Monte Carlo) to the true solution.

    Without the viscosity solution concept, one could neither guarantee existence of a solution to the PDE in general nor prove uniqueness, and the Feynman-Kac connection between the 2BSDE and the PDE would break down.
