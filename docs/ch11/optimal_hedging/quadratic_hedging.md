# Quadratic Hedging

Quadratic hedging encompasses a family of approaches that minimize hedging error measured by a quadratic criterion. The two principal variants --- **local risk minimization** and **variance-optimal hedging** --- differ in whether the optimization is performed incrementally at each time step or globally over the entire horizon. Both rely on deep connections to martingale theory and lead to distinct pricing measures in incomplete markets.

---

## Two Quadratic Criteria

### Overview

Let $H$ be a contingent claim in an incomplete market where perfect replication is impossible. Both approaches use an $L^2$ loss function but differ in scope:

| Criterion | Optimization | Pricing measure | Strategy type |
|:---|:---|:---|:---|
| **Local risk minimization** | Minimize risk at each $t$ | Minimal martingale measure $\hat{\mathbb{P}}$ | Not necessarily self-financing |
| **Variance-optimal hedging** | Minimize terminal error | Variance-optimal measure $\mathbb{Q}^*$ | Self-financing |

The mean-variance hedging problem (covered in the previous section) is the variance-optimal approach. This section develops local risk minimization in detail and then compares the two.

---

## Local Risk Minimization

### Cost Process and Risk

Consider a trading strategy $(\xi, \eta)$ where $\xi_t$ is the number of risky shares and $\eta_t$ is the money market holding. The **value process** is:

$$
V_t(\xi, \eta) = \xi_t S_t + \eta_t B_t
$$

The **cost process** $C_t$ measures the cumulative cost of running the strategy:

$$
C_t = V_t - \int_0^t \xi_s\,dS_s - \int_0^t \eta_s\,dB_s = V_t - \int_0^t \xi_s\,d\tilde{S}_s \cdot B_t
$$

In discounted terms:

$$
\tilde{C}_t = \tilde{V}_t - \int_0^t \xi_s\,d\tilde{S}_s
$$

For a self-financing strategy, $\tilde{C}_t = \tilde{V}_0$ is constant. For non-self-financing strategies, $\tilde{C}_t$ varies over time, and changes in $\tilde{C}$ represent injections or withdrawals of capital.

!!! abstract "Definition: Local Risk"
    The **local risk** at time $t$ of a strategy $(\xi, \eta)$ is:

    $$
    R_t(\xi) = \mathbb{E}\!\left[\left(\tilde{C}_{t + dt} - \tilde{C}_t\right)^2 \mid \mathcal{F}_t\right]
    $$

    equivalently, the conditional variance of the infinitesimal cost increment $d\tilde{C}_t$.

### The Optimization Problem

!!! abstract "Definition: Locally Risk-Minimizing Strategy"
    A strategy $(\xi^*, \eta^*)$ with $V_T = H$ is **locally risk-minimizing** if, for each $t$, $\xi_t^*$ minimizes the local risk $R_t(\xi)$ among all strategies that replicate $H$ at maturity.

The requirement $V_T = H$ is essential: the strategy must deliver the claim at maturity, but it need not be self-financing along the way. The cost process $C$ captures the "leakage" --- the strategy may require intermediate capital injections.

### Solution via the Kunita-Watanabe Decomposition

The locally risk-minimizing strategy is determined by the **Kunita-Watanabe (KW) decomposition** of the claim under a specific measure.

**Theorem (Kunita-Watanabe Decomposition).** *Let $M$ be a square-integrable martingale and $N$ any square-integrable martingale. Then $N$ admits a unique decomposition:*

$$
N_t = N_0 + \int_0^t \phi_s\,dM_s + L_t
$$

*where $\phi$ is predictable and $L$ is a martingale orthogonal to $M$ ($\langle L, M \rangle = 0$).*

Applied to the claim $H$: under the **minimal martingale measure** $\hat{\mathbb{P}}$ (defined below), the discounted claim price process $\tilde{V}_t = \hat{\mathbb{E}}[e^{-rT}H \mid \mathcal{F}_t]$ decomposes as:

$$
\tilde{V}_t = \tilde{V}_0 + \int_0^t \xi_s^*\,d\tilde{S}_s + L_t
$$

The optimal hedge is $\xi^* = \phi$ (the KW integrand), and $L_t$ is the cumulative cost process of the locally risk-minimizing strategy.

---

## The Minimal Martingale Measure

### Definition

!!! abstract "Definition: Minimal Martingale Measure"
    The **minimal martingale measure** $\hat{\mathbb{P}}$ is the equivalent martingale measure under which every $\mathbb{P}$-local martingale orthogonal to $\tilde{S}$ remains a local martingale. Equivalently, $\hat{\mathbb{P}}$ changes only the drift of $\tilde{S}$ to zero, without affecting the orthogonal component.

### Construction

If $\tilde{S}$ has the decomposition $\tilde{S}_t = \tilde{S}_0 + M_t + \int_0^t \alpha_s\,d\langle M \rangle_s$ (the structure condition), then:

$$
\frac{d\hat{\mathbb{P}}}{d\mathbb{P}} = \mathcal{E}(-\alpha \cdot M)_T
$$

where $\mathcal{E}$ denotes the stochastic exponential.

### Example: Stochastic Volatility

In a model $dS_t = \mu S_t\,dt + \sigma(v_t) S_t\,dW_t^1$ with stochastic volatility $dv_t = b(v_t)\,dt + \eta(v_t)\,dW_t^2$, the minimal martingale measure adjusts only the drift of $W^1$ (to make $\tilde{S}$ a martingale) and leaves $W^2$ unchanged. This means:

- Under $\hat{\mathbb{P}}$: the volatility process $v_t$ retains its physical-measure dynamics.
- The locally risk-minimizing price is $V_t = \hat{\mathbb{E}}[e^{-r(T-t)}H \mid \mathcal{F}_t]$.

This contrasts with risk-neutral pricing under an arbitrary EMM, which would modify the volatility dynamics as well.

---

## Variance-Optimal Hedging (Global Criterion)

### Recap

The variance-optimal (mean-variance) hedge minimizes the global criterion:

$$
\min_{c, \xi} \mathbb{E}\!\left[\left(H - c - \int_0^T \xi_t\,d\tilde{S}_t\right)^2\right]
$$

over **self-financing** strategies. The solution uses the Follmer-Schweizer decomposition and the variance-optimal measure $\mathbb{Q}^*$.

### Key Differences from Local Risk Minimization

| Feature | Local risk minimization | Variance-optimal hedging |
|:---|:---|:---|
| Self-financing | No (cost process $C \neq$ const) | Yes |
| Criterion | $\min R_t(\xi)$ at each $t$ | $\min \mathbb{E}[(H - c - G_T)^2]$ |
| Pricing measure | Minimal $\hat{\mathbb{P}}$ | Variance-optimal $\mathbb{Q}^*$ |
| Strategy | KW decomposition under $\hat{\mathbb{P}}$ | FS decomposition under $\mathbb{P}$ |
| Optimal capital | $\hat{\mathbb{E}}[\tilde{H}]$ | $\mathbb{E}^{\mathbb{Q}^*}[\tilde{H}]$ |

### When They Coincide

In **complete markets**, both approaches yield the unique replicating strategy. They also coincide when $\tilde{S}$ is a $\mathbb{P}$-martingale (i.e., the physical measure is already a martingale measure, so $\alpha = 0$).

More generally, the two approaches agree when the mean-variance tradeoff process $\hat{K}_T = \int_0^T \alpha_t^2\,d\langle M \rangle_t$ is **deterministic**. When $\hat{K}_T$ is random, the variance-optimal strategy involves an additional correction term that accounts for the stochasticity of the investment opportunity set.

---

## Explicit Formulas: Geometric Brownian Motion with Basis Risk

Consider hedging a claim $H = h(Y_T)$ on an untraded asset $Y$ using a correlated traded asset $S$:

$$
dS_t = \mu_S S_t\,dt + \sigma_S S_t\,dW_t^1, \qquad dY_t = \mu_Y Y_t\,dt + \sigma_Y Y_t(\rho\,dW_t^1 + \sqrt{1-\rho^2}\,dW_t^2)
$$

**Locally risk-minimizing hedge:**

$$
\xi_t^{\text{LRM}} = \rho\,\frac{\sigma_Y}{\sigma_S}\,\frac{Y_t}{S_t}\,\frac{\partial \hat{V}}{\partial Y}(t, Y_t)
$$

where $\hat{V}(t, Y) = e^{-r(T-t)}\hat{\mathbb{E}}[h(Y_T) \mid Y_t = Y]$ uses the minimal martingale measure (which leaves $Y$'s volatility unchanged).

**Variance-optimal hedge:**

$$
\xi_t^{\text{VO}} = \rho\,\frac{\sigma_Y}{\sigma_S}\,\frac{Y_t}{S_t}\,\frac{\partial V^*}{\partial Y}(t, Y_t) + \text{correction term}
$$

where $V^*$ uses the variance-optimal measure and the correction accounts for the mean-variance tradeoff.

In this particular model (GBM with constant parameters), the mean-variance tradeoff is deterministic, so $\xi^{\text{LRM}} = \xi^{\text{VO}}$ (up to the self-financing adjustment).

---

## Residual Risk Decomposition

### Decomposition of Hedging Error

For both approaches, the minimum achievable risk can be decomposed:

$$
\text{Min hedging error}^2 = \underbrace{\operatorname{Var}(L_T^H)}_{\text{unhedgeable risk}} = \underbrace{(1 - R^2)}_{\text{hedge inefficiency}} \cdot \operatorname{Var}(H)
$$

where $R^2$ is the **coefficient of determination** measuring the fraction of the claim's variance that can be explained by trading. In the basis risk model:

$$
R^2 = \rho^2
$$

### Interpretation

The residual risk has two sources:

1. **Market incompleteness**: Risk factors not spanned by traded assets (e.g., $W^2$ above).
2. **Correlation structure**: The strength of the link between the claim and traded instruments.

No quadratic hedging strategy can reduce the error below $\sqrt{1 - R^2} \cdot \operatorname{Std}(H)$, regardless of how sophisticated the dynamic strategy is.

---

## Discrete-Time Approximation

### Implementation

In practice, both local and global quadratic hedges are implemented on a discrete time grid $0 = t_0 < t_1 < \cdots < t_N = T$:

**Local risk minimization (discrete):**

At each $t_k$, compute:

$$
\xi_{t_k}^* = \frac{\operatorname{Cov}(\Delta\tilde{V}_{t_k}, \Delta\tilde{S}_{t_k} \mid \mathcal{F}_{t_k})}{\operatorname{Var}(\Delta\tilde{S}_{t_k} \mid \mathcal{F}_{t_k})}
$$

This is the **regression coefficient** of the value change on the price change --- a conditional regression that can be estimated by Monte Carlo.

**Variance-optimal (discrete):**

Solve the global regression:

$$
\min_{c, \xi_0, \ldots, \xi_{N-1}} \mathbb{E}\!\left[\left(H - c - \sum_{k=0}^{N-1} \xi_{t_k}\,\Delta\tilde{S}_{t_k}\right)^2\right]
$$

This is a standard least-squares problem that can be solved by backward induction (dynamic programming) or by Monte Carlo regression (Longstaff-Schwartz type).

---

## Summary

| Concept | Local risk minimization | Variance-optimal hedging |
|:---|:---|:---|
| Criterion | Min conditional variance of cost | Min terminal squared error |
| Self-financing | No | Yes |
| Decomposition | Kunita-Watanabe under $\hat{\mathbb{P}}$ | Follmer-Schweizer under $\mathbb{P}$ |
| Pricing measure | Minimal martingale $\hat{\mathbb{P}}$ | Variance-optimal $\mathbb{Q}^*$ |
| Strategy | $\xi^* = $ KW integrand | $\xi^* = $ FS integrand |
| Coincide when | Market complete, or $\hat{K}_T$ deterministic | |
| Residual risk | $\operatorname{Var}(L_T^H) = (1 - R^2)\operatorname{Var}(H)$ | Same in many models |
| Practical computation | Conditional regression at each step | Global regression / backward induction |
