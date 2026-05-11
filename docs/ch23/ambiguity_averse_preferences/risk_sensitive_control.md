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

---

## Exercises

**Exercise 1.** For the risk-sensitive criterion $J_\gamma = \frac{1}{\gamma}\log \mathbb{E}[e^{\gamma \sum_{t=0}^T c_t}]$ with a quadratic stage cost $c_t = x_t^2 + u_t^2$, show that as $\gamma \to 0$, $J_\gamma \to \mathbb{E}[\sum_t c_t]$ (risk-neutral case). Then compute the second-order expansion $J_\gamma \approx \mathbb{E}[C] + \frac{\gamma}{2}\text{Var}(C)$ where $C = \sum_t c_t$, demonstrating that risk sensitivity penalizes variance.

??? success "Solution to Exercise 1"
    Let $C = \sum_{t=0}^T c_t$ denote the total cost. The risk-sensitive criterion is:

    $$
    J_\gamma = \frac{1}{\gamma}\log\mathbb{E}[e^{\gamma C}]
    $$

    **Limit as $\gamma \to 0$:** We use the Taylor expansion $e^{\gamma C} = 1 + \gamma C + \frac{\gamma^2 C^2}{2} + O(\gamma^3)$.

    Taking expectations: $\mathbb{E}[e^{\gamma C}] = 1 + \gamma\mathbb{E}[C] + \frac{\gamma^2\mathbb{E}[C^2]}{2} + O(\gamma^3)$.

    Then:

    $$
    \log\mathbb{E}[e^{\gamma C}] = \log\left(1 + \gamma\mathbb{E}[C] + \frac{\gamma^2\mathbb{E}[C^2]}{2} + O(\gamma^3)\right)
    $$

    Using $\log(1 + x) = x - x^2/2 + O(x^3)$ with $x = \gamma\mathbb{E}[C] + \frac{\gamma^2\mathbb{E}[C^2]}{2} + \cdots$:

    $$
    \log\mathbb{E}[e^{\gamma C}] = \gamma\mathbb{E}[C] + \frac{\gamma^2\mathbb{E}[C^2]}{2} - \frac{\gamma^2(\mathbb{E}[C])^2}{2} + O(\gamma^3)
    $$

    $$
    = \gamma\mathbb{E}[C] + \frac{\gamma^2}{2}\left(\mathbb{E}[C^2] - (\mathbb{E}[C])^2\right) + O(\gamma^3) = \gamma\mathbb{E}[C] + \frac{\gamma^2}{2}\text{Var}(C) + O(\gamma^3)
    $$

    Dividing by $\gamma$:

    $$
    J_\gamma = \mathbb{E}[C] + \frac{\gamma}{2}\text{Var}(C) + O(\gamma^2)
    $$

    As $\gamma \to 0$, $J_\gamma \to \mathbb{E}[C]$, recovering the risk-neutral criterion. ✓

    **Interpretation of the second-order term:** The expansion $J_\gamma \approx \mathbb{E}[C] + \frac{\gamma}{2}\text{Var}(C)$ shows that for small $\gamma > 0$, the risk-sensitive criterion approximates a mean-variance objective where:

    - The first term $\mathbb{E}[C]$ is the expected total cost (same as risk-neutral)
    - The second term $\frac{\gamma}{2}\text{Var}(C)$ penalizes the variability of the total cost

    Thus, risk sensitivity introduces a penalty for variance, with $\gamma$ controlling the trade-off. Higher $\gamma$ means greater penalty for cost variability, encouraging the controller to choose actions that reduce not just the expected cost but also its dispersion. The exponential criterion naturally encodes this mean-variance trade-off without requiring separate specification of a variance constraint. $\square$

---

**Exercise 2.** Prove the duality between risk-sensitive control and robust control: show that $\frac{1}{\gamma}\log \mathbb{E}_{P_0}[e^{\gamma C}] = \sup_{P \ll P_0}\{\mathbb{E}_P[C] - \frac{1}{\gamma}D_{\text{KL}}(P \| P_0)\}$. Interpret the worst-case measure $P^*$ and explain how the parameter $\gamma$ trades off expected cost against model uncertainty.

??? success "Solution to Exercise 2"
    **To prove:** $\frac{1}{\gamma}\log\mathbb{E}_{P_0}[e^{\gamma C}] = \sup_{P \ll P_0}\left\{\mathbb{E}_P[C] - \frac{1}{\gamma}D_{\text{KL}}(P \| P_0)\right\}$

    **Step 1: Upper bound.** For any $P \ll P_0$ with $M = dP/dP_0$:

    $$
    \mathbb{E}_P[C] - \frac{1}{\gamma}D_{\text{KL}}(P \| P_0) = \mathbb{E}_{P_0}[MC] - \frac{1}{\gamma}\mathbb{E}_{P_0}[M\log M]
    $$

    $$
    = \mathbb{E}_{P_0}\left[M\left(C - \frac{1}{\gamma}\log M\right)\right] = \frac{1}{\gamma}\mathbb{E}_{P_0}\left[M\log\frac{e^{\gamma C}}{M}\right]
    $$

    By Jensen's inequality ($\mathbb{E}_P[\log Y] \leq \log\mathbb{E}_P[Y]$ with $Y = e^{\gamma C}/M$ under $P$):

    $$
    \mathbb{E}_{P_0}\left[M\log\frac{e^{\gamma C}}{M}\right] \leq \log\mathbb{E}_{P_0}\left[M \cdot \frac{e^{\gamma C}}{M}\right] = \log\mathbb{E}_{P_0}[e^{\gamma C}]
    $$

    Therefore: $\mathbb{E}_P[C] - \frac{1}{\gamma}D_{\text{KL}}(P \| P_0) \leq \frac{1}{\gamma}\log\mathbb{E}_{P_0}[e^{\gamma C}]$.

    **Step 2: Attainment.** Define:

    $$
    M^* = \frac{dP^*}{dP_0} = \frac{e^{\gamma C}}{\mathbb{E}_{P_0}[e^{\gamma C}]}
    $$

    Verify $M^* \geq 0$ and $\mathbb{E}_{P_0}[M^*] = 1$. ✓

    Compute the KL divergence:

    $$
    D_{\text{KL}}(P^* \| P_0) = \mathbb{E}_{P^*}[\log M^*] = \mathbb{E}_{P^*}[\gamma C - \log\mathbb{E}_{P_0}[e^{\gamma C}]]
    $$

    $$
    = \gamma\mathbb{E}_{P^*}[C] - \log\mathbb{E}_{P_0}[e^{\gamma C}]
    $$

    Therefore:

    $$
    \mathbb{E}_{P^*}[C] - \frac{1}{\gamma}D_{\text{KL}}(P^* \| P_0) = \mathbb{E}_{P^*}[C] - \frac{1}{\gamma}\left(\gamma\mathbb{E}_{P^*}[C] - \log\mathbb{E}_{P_0}[e^{\gamma C}]\right)
    $$

    $$
    = \mathbb{E}_{P^*}[C] - \mathbb{E}_{P^*}[C] + \frac{1}{\gamma}\log\mathbb{E}_{P_0}[e^{\gamma C}] = \frac{1}{\gamma}\log\mathbb{E}_{P_0}[e^{\gamma C}]
    $$

    The supremum is achieved, completing the proof. $\square$

    **Interpretation of $P^*$:** The worst-case measure $P^*$ exponentially tilts probabilities toward high-cost outcomes. The Radon–Nikodym derivative $dP^*/dP_0 \propto e^{\gamma C}$ assigns more weight to states where $C$ is large. This is the adversarial distribution that maximizes expected cost net of the entropy penalty.

    **Role of $\gamma$:** The parameter $\gamma$ controls the trade-off:

    - Large $\gamma$: weak entropy penalty, allowing $P^*$ to deviate far from $P_0$ and focus on extreme outcomes
    - Small $\gamma$: strong entropy penalty, keeping $P^*$ close to $P_0$
    - $\gamma \to 0$: $P^* \to P_0$, recovering the risk-neutral criterion

---

**Exercise 3.** In the linear-quadratic-Gaussian setting with dynamics $x_{t+1} = Ax_t + Bu_t + w_t$, $w_t \sim N(0, \Sigma_w)$, the risk-sensitive optimal control satisfies a modified Riccati equation. Compare the risk-sensitive gain matrix with the standard LQG gain for $A = 0.9$, $B = 1$, $Q = 1$, $R = 0.1$, $\Sigma_w = 0.25$, and $\gamma = 0.5$. How does risk sensitivity change the optimal control law?

??? success "Solution to Exercise 3"
    **Setup:** $A = 0.9$, $B = 1$, $Q = 1$, $R = 0.1$, $\Sigma_w = 0.25$ (so $C = \sqrt{0.25} = 0.5$ with $CC^\top = 0.25$), $\gamma = 0.5$.

    **Standard LQG Riccati equation (scalar):**

    $$
    P = Q + A^2 P - \frac{A^2 P^2 B^2}{R + B^2 P} = 1 + 0.81P - \frac{0.81P^2}{0.1 + P}
    $$

    Multiplying by $(0.1 + P)$:

    $$
    P(0.1 + P) = (0.1 + P) + 0.81P(0.1 + P) - 0.81P^2
    $$

    $$
    0.1P + P^2 = 0.1 + P + 0.081P + 0.81P^2 - 0.81P^2
    $$

    $$
    P^2 + 0.1P - P - 0.081P - 0.1 = 0
    $$

    $$
    P^2 - 0.981P - 0.1 = 0
    $$

    $$
    P = \frac{0.981 + \sqrt{0.981^2 + 0.4}}{2} = \frac{0.981 + \sqrt{0.9624 + 0.4}}{2} = \frac{0.981 + \sqrt{1.3624}}{2} = \frac{0.981 + 1.1673}{2} = 1.0742
    $$

    Standard gain: $K_{\text{std}} = \frac{A P B}{R + B^2 P} = \frac{0.9 \times 1.0742}{0.1 + 1.0742} = \frac{0.9668}{1.1742} = 0.8234$.

    **Risk-sensitive Riccati equation:** The risk-sensitive Riccati in the scalar case is:

    $$
    P = Q + A^2\left(\frac{1}{P^{-1} - \gamma\Sigma_w}\right) - \frac{A^2 P_{\text{eff}}^2 B^2}{R + B^2 P_{\text{eff}}}
    $$

    where $P_{\text{eff}} = (P^{-1} - \gamma\Sigma_w)^{-1} = \frac{P}{1 - \gamma\Sigma_w P}$.

    With $\gamma\Sigma_w = 0.5 \times 0.25 = 0.125$:

    $$
    P_{\text{eff}} = \frac{P}{1 - 0.125P}
    $$

    Existence requires $1 - 0.125P > 0$, i.e., $P < 8$.

    The Riccati equation becomes:

    $$
    P = 1 + \frac{0.81P}{1 - 0.125P} - \frac{0.81P^2/(1-0.125P)^2}{0.1 + P/(1-0.125P)}
    $$

    Simplifying the second term: $\frac{0.81P}{1 - 0.125P}$.

    For the third term, let $\tilde{P} = P/(1-0.125P)$:

    $$
    \frac{0.81\tilde{P}^2}{0.1 + \tilde{P}} = \frac{0.81P^2/(1-0.125P)^2}{0.1 + P/(1-0.125P)} = \frac{0.81P^2}{(1-0.125P)^2 \cdot \frac{0.1(1-0.125P) + P}{1-0.125P}} = \frac{0.81P^2}{(1-0.125P)(0.1 + 0.875P)}
    $$

    Wait — let me simplify. Actually, the standard form of the risk-sensitive Riccati in the scalar LQG case (with $C = I$ for simplicity, i.e., $\Sigma_w$ directly enters) is most cleanly written as:

    $$
    P = Q + A^2 P_{\text{eff}} - \frac{A^2 P_{\text{eff}}^2}{R + P_{\text{eff}}}, \quad P_{\text{eff}} = \frac{P}{1 - \gamma\Sigma_w P}
    $$

    Let me iterate numerically. Start with $P^{(0)} = 1.0742$ (the standard LQG value).

    $P_{\text{eff}}^{(0)} = \frac{1.0742}{1 - 0.125 \times 1.0742} = \frac{1.0742}{0.8657} = 1.2407$.

    $P^{(1)} = 1 + 0.81(1.2407) - \frac{0.81(1.2407)^2}{0.1 + 1.2407} = 1 + 1.005 - \frac{1.2472}{1.3407} = 1 + 1.005 - 0.9303 = 1.0747$.

    Iterate: $P_{\text{eff}} = 1.0747/(1 - 0.125 \times 1.0747) = 1.0747/0.8657 = 1.2413$.

    $P^{(2)} = 1 + 0.81(1.2413) - 0.81(1.2413)^2/(0.1 + 1.2413) = 1 + 1.0055 - 1.2485/1.3413 = 1 + 1.0055 - 0.9309 = 1.0746$.

    Converged: $P_\gamma \approx 1.0747$.

    Risk-sensitive gain: $K_\gamma = \frac{A \cdot P_{\text{eff}}}{R + P_{\text{eff}}} = \frac{0.9 \times 1.2413}{0.1 + 1.2413} = \frac{1.1172}{1.3413} = 0.8329$.

    **Comparison:**

    | Criterion | $P$ | $K$ (gain) | $u^* = -Kx$ |
    |-----------|-----|------------|-------------|
    | Standard LQG ($\gamma = 0$) | 1.074 | 0.823 | Less aggressive |
    | Risk-sensitive ($\gamma = 0.5$) | 1.075 | 0.833 | More aggressive |

    The risk-sensitive controller has a slightly higher gain (0.833 vs 0.823), meaning it applies slightly stronger feedback. This is because the risk-sensitive criterion penalizes cost variability: by controlling more aggressively, the controller reduces the variance of future states (and hence future costs), at the expense of higher control effort. The effective Riccati matrix $P_{\text{eff}} > P$ amplifies the state cost, leading to the more aggressive response.

    The difference is modest for $\gamma = 0.5$ because $\gamma\Sigma_w P \approx 0.134$ is relatively small. For larger $\gamma$ (approaching the breakdown point at $\gamma = 1/(\Sigma_w P) \approx 3.72$), the differences would be much more dramatic. $\square$

---

**Exercise 4.** Calibrate the risk sensitivity parameter $\gamma$ using the detection error probability method. Given a reference model $P_0$ and a worst-case model $P^*$, the detection error probability is $p_e = \frac{1}{2}(P_0(\text{reject } P_0) + P^*(\text{reject } P^*))$. For a Gaussian reference model, show that $p_e$ depends on the KL divergence between $P_0$ and $P^*$, and determine $\gamma$ such that $p_e = 0.10$.

??? success "Solution to Exercise 4"
    **Setup:** Reference model $P_0 = N(\mu_0, \sigma^2)$, worst-case model $P^* = N(\mu^*, \sigma^2)$ (same variance, shifted mean — the typical worst-case perturbation in LQG settings).

    **KL divergence between Gaussians with equal variance:**

    $$
    D_{\text{KL}}(P^* \| P_0) = \frac{(\mu^* - \mu_0)^2}{2\sigma^2}
    $$

    **Detection error probability:** For the likelihood ratio test with $n$ i.i.d. observations, the log-likelihood ratio is:

    $$
    \log\Lambda_n = \sum_{i=1}^n \left[\frac{(X_i - \mu_0)^2}{2\sigma^2} - \frac{(X_i - \mu^*)^2}{2\sigma^2}\right] = \frac{\mu^* - \mu_0}{\sigma^2}\sum_{i=1}^n X_i - \frac{n(\mu^{*2} - \mu_0^2)}{2\sigma^2}
    $$

    Under $P_0$: $\log\Lambda_n \sim N\left(-\frac{n(\mu^* - \mu_0)^2}{2\sigma^2}, \frac{n(\mu^* - \mu_0)^2}{\sigma^2}\right)$

    Under $P^*$: $\log\Lambda_n \sim N\left(\frac{n(\mu^* - \mu_0)^2}{2\sigma^2}, \frac{n(\mu^* - \mu_0)^2}{\sigma^2}\right)$

    For the symmetric test (threshold at $\log\Lambda = 0$):

    - Type I error: $\alpha = P_0(\log\Lambda_n > 0) = \Phi\left(-\frac{\sqrt{n}|\mu^* - \mu_0|}{2\sigma}\right)$
    - Type II error: $\beta = P^*(\log\Lambda_n \leq 0) = \Phi\left(-\frac{\sqrt{n}|\mu^* - \mu_0|}{2\sigma}\right)$

    So $\alpha = \beta$ and the detection error probability is:

    $$
    p_e = \frac{1}{2}(\alpha + \beta) = \Phi\left(-\frac{\sqrt{n}\,\delta}{2}\right)
    $$

    where $\delta = |\mu^* - \mu_0|/\sigma$ is the signal-to-noise ratio.

    **Connection to KL divergence:** Note that $D_{\text{KL}} = \delta^2/2$, so $\delta = \sqrt{2D_{\text{KL}}}$ and:

    $$
    p_e = \Phi\left(-\frac{\sqrt{n}\sqrt{2D_{\text{KL}}}}{2}\right) = \Phi\left(-\sqrt{\frac{nD_{\text{KL}}}{2}}\right)
    $$

    This confirms that $p_e$ depends on $D_{\text{KL}}$ (and sample size $n$).

    **Calibrating $\gamma$:** From the duality, risk sensitivity with parameter $\gamma$ corresponds to an entropy penalty of $1/\gamma$, and the worst-case model satisfies:

    $$
    D_{\text{KL}}(P^* \| P_0) = \text{function of } \gamma \text{ and the problem parameters}
    $$

    Setting $p_e = 0.10$:

    $$
    0.10 = \Phi\left(-\sqrt{\frac{nD_{\text{KL}}}{2}}\right) \implies \sqrt{\frac{nD_{\text{KL}}}{2}} = \Phi^{-1}(0.90) = 1.2816
    $$

    $$
    D_{\text{KL}} = \frac{2(1.2816)^2}{n} = \frac{3.285}{n}
    $$

    For example, with $n = 100$ quarterly observations: $D_{\text{KL}} = 0.03285$.

    Since the risk-sensitive parameter relates to entropy via $D_{\text{KL}}(P^* \| P_0) = \gamma \cdot \text{Var}_{P^*}(C)/2$ (in the LQG case), one can numerically solve for $\gamma$ given the model parameters and the target $D_{\text{KL}}$. The key insight is that $\gamma$ is not chosen arbitrarily but is pinned down by the requirement that the worst-case model be statistically difficult to distinguish from the reference model at the specified detection error level. $\square$

---

**Exercise 5.** Apply risk-sensitive control to a Merton portfolio problem. An investor with risk-sensitive criterion $\frac{1}{\gamma}\log \mathbb{E}[e^{\gamma W_T}]$ chooses the fraction of wealth in a risky asset with return $\mu = 0.08$ and volatility $\sigma = 0.20$. Derive the optimal portfolio weight and show that it is smaller than the Merton ratio $\mu/(\sigma^2)$ for $\gamma > 0$.

??? success "Solution to Exercise 5"
    **Setup:** Wealth dynamics $dW_t = W_t[\pi(\mu\,dt + \sigma\,dB_t) + (1-\pi)r\,dt]$ with constant fraction $\pi$ in the risky asset. Log-wealth at time $T$:

    $$
    \log W_T = \log W_0 + \left[\pi\mu + (1-\pi)r - \frac{\pi^2\sigma^2}{2}\right]T + \pi\sigma B_T
    $$

    The risk-sensitive criterion (maximizing):

    $$
    J(\pi) = \frac{1}{\gamma}\log\mathbb{E}\left[e^{\gamma\log W_T}\right] = \frac{1}{\gamma}\log\mathbb{E}[W_T^\gamma]
    $$

    Since $\log W_T \sim N(m, s^2)$ with $m = \log W_0 + [\pi\mu + (1-\pi)r - \pi^2\sigma^2/2]T$ and $s^2 = \pi^2\sigma^2 T$:

    $$
    \mathbb{E}[W_T^\gamma] = \mathbb{E}[e^{\gamma\log W_T}] = e^{\gamma m + \gamma^2 s^2/2}
    $$

    Therefore:

    $$
    J(\pi) = \frac{1}{\gamma}\left(\gamma m + \frac{\gamma^2 s^2}{2}\right) = m + \frac{\gamma s^2}{2}
    $$

    $$
    = \log W_0 + \left[\pi\mu + (1-\pi)r - \frac{\pi^2\sigma^2}{2}\right]T + \frac{\gamma\pi^2\sigma^2 T}{2}
    $$

    $$
    = \log W_0 + \left[\pi(\mu - r) + r - \frac{\pi^2\sigma^2(1-\gamma)}{2}\right]T
    $$

    **Optimize over $\pi$:** Taking the derivative and setting to zero:

    $$
    \frac{\partial J}{\partial \pi} = (\mu - r)T - \pi\sigma^2(1-\gamma)T = 0
    $$

    $$
    \pi^* = \frac{\mu - r}{\sigma^2(1-\gamma)}
    $$

    **Note:** This requires $\gamma < 1$ for the second-order condition to hold ($\partial^2 J/\partial\pi^2 = -\sigma^2(1-\gamma)T < 0$ iff $\gamma < 1$).

    **Comparison with the Merton ratio:** The standard Merton ratio (risk-neutral, or equivalently CRRA with $\gamma_{\text{CRRA}} = 1$) for log utility is:

    $$
    \pi_{\text{Merton}} = \frac{\mu - r}{\sigma^2}
    $$

    With numerical values $\mu = 0.08$, $\sigma = 0.20$, $r = 0$ (for simplicity):

    $$
    \pi_{\text{Merton}} = \frac{0.08}{0.04} = 2.0
    $$

    $$
    \pi^*_{\text{RS}} = \frac{0.08}{0.04(1 - \gamma)}
    $$

    Wait — for $\gamma > 0$, $1 - \gamma < 1$, so $\pi^* > \pi_{\text{Merton}}$. This seems counterintuitive. The issue is the sign convention: when $\gamma > 0$ in the criterion $\frac{1}{\gamma}\log\mathbb{E}[e^{\gamma\log W_T}]$, the agent is actually risk-seeking (maximizing a convex functional of log-wealth).

    For **risk-averse** risk-sensitive control, we use $\gamma < 0$ (or equivalently, minimize the criterion with $\gamma > 0$). With $\gamma < 0$:

    $$
    \pi^* = \frac{\mu - r}{\sigma^2(1 - \gamma)} = \frac{\mu - r}{\sigma^2(1 + |\gamma|)}
    $$

    Since $1 + |\gamma| > 1$, we have $\pi^* < \pi_{\text{Merton}}$.

    With $|\gamma| = 0.5$ (i.e., $\gamma = -0.5$ for risk aversion):

    $$
    \pi^* = \frac{0.08}{0.04 \times 1.5} = \frac{0.08}{0.06} = 1.333
    $$

    compared to $\pi_{\text{Merton}} = 2.0$.

    **Alternatively**, using the convention where we maximize $-\frac{1}{\gamma}\log\mathbb{E}[e^{-\gamma\log W_T}]$ with $\gamma > 0$:

    $$
    \pi^* = \frac{\mu - r}{\sigma^2(1 + \gamma)}
    $$

    With $\gamma = 0.5$: $\pi^* = 0.08/(0.04 \times 1.5) = 1.333 < 2.0 = \pi_{\text{Merton}}$.

    **Conclusion:** Risk-sensitive control with $\gamma > 0$ (risk-averse convention) reduces the optimal portfolio weight from the Merton ratio. The effective risk aversion increases from 1 (log utility) to $1 + \gamma$, shrinking the position in the risky asset. This reflects the agent's concern about tail outcomes: the exponential criterion penalizes large losses more heavily than a log-utility agent would. $\square$

---

**Exercise 6.** In an asset-liability management context, a pension fund must match liabilities $L_T$ at time $T$. Formulate the risk-sensitive ALM problem as $\min_u \frac{1}{\gamma}\log \mathbb{E}[e^{\gamma(L_T - A_T)^2}]$ where $A_T$ is the asset value. Explain how $\gamma$ controls the fund's aversion to shortfall risk, and why the risk-sensitive formulation is more appropriate than the standard mean-variance approach for pension funds.

??? success "Solution to Exercise 6"
    **Formulation of the risk-sensitive ALM problem:**

    Let $A_t$ denote the asset portfolio value at time $t$ and $L_T$ the liability at maturity $T$. The fund manager chooses an investment strategy $u = \{u_t\}$ (portfolio weights) to minimize the risk-sensitive tracking error:

    $$
    \min_u J_\gamma(u) = \min_u \frac{1}{\gamma}\log\mathbb{E}\left[e^{\gamma(L_T - A_T)^2}\right]
    $$

    where $\gamma > 0$ controls the degree of shortfall aversion.

    **How $\gamma$ controls shortfall risk aversion:**

    Using the Taylor expansion for small $\gamma$:

    $$
    J_\gamma \approx \mathbb{E}[(L_T - A_T)^2] + \frac{\gamma}{2}\text{Var}[(L_T - A_T)^2] + O(\gamma^2)
    $$

    - **$\gamma = 0$ (risk-neutral):** $J_0 = \mathbb{E}[(L_T - A_T)^2]$, which is the mean squared tracking error. This penalizes overfunding and underfunding symmetrically.

    - **Small $\gamma > 0$:** Adds a variance penalty, discouraging outcomes where the squared shortfall is highly variable. Since $(L_T - A_T)^2$ has high variance precisely when large shortfalls occur with non-trivial probability, this indirectly penalizes shortfall risk.

    - **Large $\gamma$:** The exponential weighting $e^{\gamma(L_T - A_T)^2}$ is dominated by the largest values of $(L_T - A_T)^2$, i.e., the worst-case shortfalls. In the limit:

    $$
    \lim_{\gamma \to \infty} J_\gamma = \text{ess sup}(L_T - A_T)^2
    $$

    The fund becomes infinitely averse to shortfalls and targets worst-case minimization.

    **Why risk-sensitive is more appropriate than mean-variance for pension funds:**

    1. **Asymmetric consequences:** For pension funds, underfunding ($L_T > A_T$) has severe consequences (regulatory penalties, benefit cuts, sponsor contributions), while overfunding has mild consequences. The exponential weighting in the risk-sensitive criterion naturally amplifies the impact of large shortfalls relative to small ones, even though $(L_T - A_T)^2$ is symmetric. The exponential tilts toward extreme scenarios asymmetrically through the probability weighting.

    2. **Tail risk focus:** Mean-variance minimizes $\mathbb{E}[(L_T - A_T)^2]$, treating all deviations equally. Risk-sensitive control places exponentially more weight on extreme shortfalls. For a pension fund with a long tail of liability risks (longevity, inflation, market crashes), this tail focus is essential.

    3. **Robustness interpretation:** Via the duality $J_\gamma = \sup_P\{\mathbb{E}_P[(L_T-A_T)^2] - \frac{1}{\gamma}D_{\text{KL}}(P\|P_0)\}$, the risk-sensitive criterion evaluates the tracking error under a worst-case probability model. This is appropriate because pension funds face significant model uncertainty about:
        - Future investment returns
        - Liability discount rates
        - Longevity and mortality trends
        - Inflation dynamics

    4. **Dynamic consistency:** The risk-sensitive Bellman equation provides a dynamically consistent framework for multi-period ALM, whereas mean-variance optimization is notoriously time-inconsistent (the optimal policy at $t=1$ generally differs from the $t=0$ plan).

    5. **Regulatory alignment:** Pension regulators increasingly focus on stress testing and worst-case scenarios (e.g., solvency capital requirements). The risk-sensitive framework naturally incorporates these concerns through the parameter $\gamma$, which can be calibrated to regulatory stress test levels. $\square$
