# Risk-Sensitive Control


## Introduction


**Risk-sensitive control** provides a framework for optimal decision-making that explicitly accounts for the variability of outcomes, not just their expected values. Unlike standard stochastic optimal control, which optimizes expected cumulative cost, risk-sensitive control incorporates an **exponential transformation** that penalizes variance and higher moments.

This approach, pioneered by Jacobson (1973) and Howard and Matheson (1972), has deep connections to:
1. **Robust control**: Worst-case optimization under model uncertainty
2. **Large deviations theory**: Rare event probabilities
3. **Information theory**: Entropy and relative entropy
4. **Financial economics**: Portfolio optimization and asset pricing

## Mathematical Framework


### 1. Standard Stochastic Control


**Setup**: Consider a controlled Markov process $\{X_t\}$ with dynamics:

$$
X_{t+1} = f(X_t, u_t, W_t)
$$

where $X_t \in \mathbb{R}^n$ is the state, $u_t \in \mathcal{U}$ is the control action, and $W_t$ is i.i.d. noise.

**Standard Objective** (Risk-Neutral):

$$
J^{\text{neutral}}(x, \pi) = \mathbb{E}\left[\sum_{t=0}^{T-1} c(X_t, u_t) + c_T(X_T) \,\bigg|\, X_0 = x\right]
$$

### 2. Risk-Sensitive Objective


**Exponential Criterion**: The risk-sensitive objective is:

$$
J^{\text{RS}}(x, \pi; \gamma) = \frac{1}{\gamma} \log \mathbb{E}\left[\exp\left(\gamma \sum_{t=0}^{T-1} c(X_t, u_t) + \gamma c_T(X_T)\right) \,\bigg|\, X_0 = x\right]
$$

where $\gamma \neq 0$ is the **risk-sensitivity parameter**.

**Interpretation**:
- $\gamma > 0$: Risk-averse (penalizes variability)
- $\gamma < 0$: Risk-seeking (rewards variability)
- $\gamma \to 0$: Recovers risk-neutral case

**Taylor Expansion**: For small $\gamma$:

$$
J^{\text{RS}} \approx \mathbb{E}[C] + \frac{\gamma}{2} \text{Var}(C) + O(\gamma^2)
$$

### 3. Risk-Sensitive Bellman Equation


**Theorem**: Define value function $V_t^{\gamma}(x)$. Then:

$$
V_t^{\gamma}(x) = \min_u \left\{c(x, u) + \frac{1}{\gamma} \log \mathbb{E}\left[e^{\gamma V_{t+1}^{\gamma}(f(x, u, W))}\right]\right\}
$$

with terminal condition $V_T^{\gamma}(x) = c_T(x)$.

## Linear-Quadratic-Gaussian Case


### 1. Setup


**Linear Dynamics**:

$$
X_{t+1} = A X_t + B u_t + C W_t, \quad W_t \sim N(0, I)
$$

**Quadratic Cost**:

$$
c(x, u) = \frac{1}{2}(x^\top Q x + u^\top R u), \quad c_T(x) = \frac{1}{2} x^\top Q_T x
$$

### 2. Risk-Sensitive LQG Solution


**Theorem** (Jacobson, 1973): The value function is:

$$
V_t^{\gamma}(x) = \frac{1}{2} x^\top P_t x + \frac{1}{2} \sum_{s=t}^{T-1} \rho_s
$$

where $P_t$ satisfies the **risk-sensitive Riccati equation**:

$$
P_t = Q + A^\top \left(P_{t+1}^{-1} - \gamma C C^\top\right)^{-1} A - A^\top P_{t+1} B (R + B^\top P_{t+1} B)^{-1} B^\top P_{t+1} A
$$

**Existence Condition**: Requires $P_{t+1}^{-1} - \gamma C C^\top \succ 0$.

**Optimal Control**:

$$
u_t^* = -K_t X_t, \quad K_t = (R + B^\top P_{t+1} B)^{-1} B^\top P_{t+1} A
$$

**Remarkable Property**: The optimal control formula is identical to risk-neutral LQG.

## Connection to Robust Control


### 1. Hansen-Sargent Duality


**Theorem**: Risk-sensitive control is equivalent to:

$$
V^{\gamma}(x) = \max_{h} \min_u \left\{c(x, u) + \mathbb{E}[V^{\gamma}(f(x, u, W + h))] - \frac{\|h\|^2}{2\gamma}\right\}
$$

**Interpretation**: Controller minimizes cost while nature maximizes via disturbance $h$, penalized by $\|h\|^2/(2\gamma)$.

### 2. Worst-Case Distribution


The worst-case distribution tilts the noise toward adverse outcomes:

$$
\frac{dP^*}{dP_0} \propto \exp\left(\gamma V^{\gamma}(f(x, u, W))\right)
$$

## Whittle's Risk-Sensitive Control


### 1. Average Cost Criterion


**Infinite Horizon**: For ergodic systems, consider:

$$
\Lambda(\gamma) = \lim_{T \to \infty} \frac{1}{\gamma T} \log \mathbb{E}\left[\exp\left(\gamma \sum_{t=0}^{T-1} c(X_t, u_t)\right)\right]
$$

**Whittle's Formula**: Under ergodicity, there exists a function $h(x)$ such that:

$$
\Lambda(\gamma) + h(x) = \min_u \left\{c(x, u) + \frac{1}{\gamma} \log \mathbb{E}\left[e^{\gamma h(f(x, u, W))}\right]\right\}
$$

### 2. Large Deviations Connection


**Legendre Transform**: The risk-sensitive cost relates to rare events:

$$
\Lambda(\gamma) = \sup_{\lambda} \{\gamma \lambda - I(\lambda)\}
$$

where $I(\lambda)$ is the rate function for the empirical average cost.

## Financial Applications


### 1. Portfolio Optimization


**Risk-Sensitive Portfolio**: With wealth dynamics $W_{t+1} = W_t(1 + r_t^\top \pi_t)$:

$$
\max_\pi \frac{1}{\gamma T} \log \mathbb{E}\left[\exp\left(\gamma \sum_{t=0}^{T-1} \log(1 + r_t^\top \pi_t)\right)\right]
$$

**Solution**: For i.i.d. returns with $r \sim N(\mu, \Sigma)$:

$$
\pi^* = \frac{1}{1 - \gamma \sigma_p^2} \Sigma^{-1} \mu
$$

where $\sigma_p^2 = \mu^\top \Sigma^{-1} \mu$ is squared Sharpe ratio.

**Effect**: Risk-sensitivity ($\gamma > 0$) reduces position size.

### 2. Asset-Liability Management


**ALM Objective**: Minimize risk-sensitive tracking error:

$$
\min_u \frac{1}{\gamma} \log \mathbb{E}\left[\exp\left(\gamma (A_T - L_T)^2\right)\right]
$$

where $A_T$ is asset value and $L_T$ is liability.

### 3. Option Pricing


**Risk-Sensitive Pricing**: Indifference price $p$ satisfies:

$$
\frac{1}{\gamma} \log \mathbb{E}\left[e^{\gamma U(W_T - \Phi)}\right] = \frac{1}{\gamma} \log \mathbb{E}\left[e^{\gamma U(W_T + p)}\right]
$$

This yields prices between sub/super-replication bounds.

## Continuous-Time Formulation


### 1. Diffusion Dynamics


**State Equation**:

$$
dX_t = b(X_t, u_t) dt + \sigma(X_t, u_t) dW_t
$$

**Risk-Sensitive Value**: Define:

$$
V(t, x) = \sup_u \frac{1}{\gamma} \log \mathbb{E}\left[\exp\left(\gamma \int_t^T c(X_s, u_s) ds + \gamma g(X_T)\right) \bigg| X_t = x\right]
$$

### 2. Risk-Sensitive HJB


**PDE**: The value function satisfies:

$$
V_t + \sup_u \left\{b \cdot \nabla V + \frac{1}{2}\text{tr}(\sigma \sigma^\top D^2 V) + \frac{\gamma}{2}|\sigma^\top \nabla V|^2 + c\right\} = 0
$$

**Key Feature**: The term $\frac{\gamma}{2}|\sigma^\top \nabla V|^2$ couples value gradient with diffusion.

### 3. Connection to Nonlinear Expectations


**g-Expectation**: Risk-sensitive control relates to BSDEs with driver:

$$
g(z) = c + \frac{\gamma}{2}|z|^2
$$

The quadratic driver corresponds to exponential utility.

## Computational Methods


### 1. Value Iteration


**Algorithm**: For discrete state/action:

$$
V^{(k+1)}(x) = \min_u \left\{c(x, u) + \frac{1}{\gamma} \log \sum_{x'} P(x'|x, u) e^{\gamma V^{(k)}(x')}\right\}
$$

**Convergence**: Contracts under appropriate conditions.

### 2. Policy Gradient


**Gradient**: For parameterized policy $\pi_\theta$:

$$
\nabla_\theta J^{\text{RS}} = \frac{\mathbb{E}\left[e^{\gamma C} \nabla_\theta \log \pi_\theta\right]}{\mathbb{E}\left[e^{\gamma C}\right]}
$$

**Challenge**: High variance due to exponential weighting.

### 3. Monte Carlo


**Importance Sampling**: Use twisted distribution:

$$
\hat{J}^{\text{RS}} = \frac{1}{\gamma} \log \frac{1}{N} \sum_{i=1}^N w_i e^{\gamma C_i}
$$

with appropriate weights $w_i$.

## Relationship to Other Frameworks


### 1. Entropy-Penalized Control


**Equivalence**: Risk-sensitive control with parameter $\gamma$ is equivalent to:

$$
\min_P \left\{\mathbb{E}_P[C] + \frac{1}{\gamma} D_{\text{KL}}(P \| P_0)\right\}
$$

where $P$ is an alternative probability measure.

### 2. Exponential Utility


**Connection**: For terminal wealth $W_T$:

$$
\max_u \mathbb{E}[-e^{-\gamma W_T}] \iff \max_u \left\{-\frac{1}{\gamma} \log \mathbb{E}[e^{-\gamma W_T}]\right\}
$$

Risk-sensitive control generalizes exponential utility to multi-period settings.

### 3. CVaR Optimization


**Comparison**:
- CVaR: Focus on tail quantile
- Risk-sensitive: Exponential weighting of all outcomes
- Risk-sensitive is smoother but less interpretable for tail risk

## Summary


### Key Results


1. **Exponential Transformation**: Risk-sensitive criterion $\frac{1}{\gamma}\log\mathbb{E}[e^{\gamma C}]$ penalizes variance and higher moments

2. **LQG Solution**: Optimal control formula unchanged; value function incorporates risk through modified Riccati equation

3. **Robust Duality**: Risk-sensitive $\Leftrightarrow$ Robust control with entropy penalty

4. **Financial Applications**: Portfolio optimization, ALM, option pricing with explicit risk consideration

### Practical Implications


- **Calibration**: $\gamma$ can be set via detection error probability or risk tolerance
- **Computation**: Value iteration and policy gradient methods available
- **Interpretation**: Balances expected cost against variability

Risk-sensitive control provides a principled framework for incorporating risk preferences into dynamic optimization, with deep connections to robust control, information theory, and financial economics.
