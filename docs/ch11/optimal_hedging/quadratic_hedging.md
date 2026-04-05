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

---

## Exercises

**Exercise 1.** In the discrete-time local risk minimization formula, $\xi_{t_k}^* = \operatorname{Cov}(\Delta\tilde{V}_{t_k}, \Delta\tilde{S}_{t_k} \mid \mathcal{F}_{t_k}) / \operatorname{Var}(\Delta\tilde{S}_{t_k} \mid \mathcal{F}_{t_k})$, this is a regression coefficient. For a one-period model with $\tilde{S}_0 = 100$, $\tilde{S}_1 \in \{110, 100, 90\}$ with probabilities $\{0.3, 0.4, 0.3\}$, and a claim $H$ with payoffs $\{12, 3, 0\}$, compute $\xi_0^*$ and the residual risk $\mathbb{E}[(H - c^* - \xi_0^*\Delta\tilde{S})^2]$.

??? success "Solution to Exercise 1"
    **Step 1: Compute moments of $\tilde{S}_1$ and $H$.**

    The discounted asset prices and claim payoffs with their probabilities are:

    | State | Prob | $\tilde{S}_1$ | $\Delta\tilde{S} = \tilde{S}_1 - 100$ | $H$ |
    |:---|:---|:---|:---|:---|
    | Up | 0.3 | 110 | 10 | 12 |
    | Mid | 0.4 | 100 | 0 | 3 |
    | Down | 0.3 | 90 | $-10$ | 0 |

    $$
    \mathbb{E}[\Delta\tilde{S}] = 0.3(10) + 0.4(0) + 0.3(-10) = 0
    $$

    $$
    \mathbb{E}[H] = 0.3(12) + 0.4(3) + 0.3(0) = 3.6 + 1.2 + 0 = 4.8
    $$

    **Step 2: Compute the variance and covariance.**

    $$
    \operatorname{Var}(\Delta\tilde{S}) = \mathbb{E}[(\Delta\tilde{S})^2] = 0.3(100) + 0.4(0) + 0.3(100) = 60
    $$

    $$
    \operatorname{Cov}(\Delta\tilde{S}, H) = \mathbb{E}[\Delta\tilde{S} \cdot H] - \mathbb{E}[\Delta\tilde{S}]\mathbb{E}[H]
    $$

    $$
    \mathbb{E}[\Delta\tilde{S} \cdot H] = 0.3(10)(12) + 0.4(0)(3) + 0.3(-10)(0) = 36
    $$

    $$
    \operatorname{Cov}(\Delta\tilde{S}, H) = 36 - 0 = 36
    $$

    **Step 3: Compute the optimal hedge ratio.**

    $$
    \xi_0^* = \frac{\operatorname{Cov}(\Delta\tilde{S}, H)}{\operatorname{Var}(\Delta\tilde{S})} = \frac{36}{60} = 0.6
    $$

    **Step 4: Compute the optimal initial capital.**

    Since $\mathbb{E}[\Delta\tilde{S}] = 0$ (the discounted price is a martingale under $\mathbb{P}$ here), we have:

    $$
    c^* = \mathbb{E}[H] = 4.8
    $$

    **Step 5: Compute the residual risk.**

    The hedging error in each state is $\varepsilon = H - c^* - \xi_0^*\Delta\tilde{S}$:

    | State | $H - 4.8 - 0.6\Delta\tilde{S}$ | $\varepsilon^2$ |
    |:---|:---|:---|
    | Up | $12 - 4.8 - 6.0 = 1.2$ | 1.44 |
    | Mid | $3 - 4.8 - 0 = -1.8$ | 3.24 |
    | Down | $0 - 4.8 + 6.0 = 1.2$ | 1.44 |

    $$
    \mathbb{E}[\varepsilon^2] = 0.3(1.44) + 0.4(3.24) + 0.3(1.44) = 0.432 + 1.296 + 0.432 = 2.16
    $$

    The residual risk is $\mathbb{E}[(H - c^* - \xi_0^*\Delta\tilde{S})^2] = 2.16$, with a residual standard deviation of $\sqrt{2.16} \approx 1.47$.

---

**Exercise 2.** The minimal martingale measure $\hat{\mathbb{P}}$ changes only the drift of $\tilde{S}$ and leaves orthogonal martingales unchanged. In a stochastic volatility model $dS = \mu S\,dt + \sigma(v)S\,dW^1$, $dv = b(v)\,dt + \eta(v)\,dW^2$ with $\rho = 0$, explain why the minimal martingale measure preserves the physical-measure dynamics of $v$. How does this affect the locally risk-minimizing price compared to a risk-neutral price that uses a market price of volatility risk?

??? success "Solution to Exercise 2"
    Under the minimal martingale measure $\hat{\mathbb{P}}$, the density process is $d\hat{\mathbb{P}}/d\mathbb{P} = \mathcal{E}(-\alpha \cdot M)_T$, where $\alpha$ is chosen so that the drift of $\tilde{S}$ is removed.

    In the stochastic volatility model with $\rho = 0$, the Brownian motions $W^1$ (driving $S$) and $W^2$ (driving $v$) are independent. The structure condition gives:

    $$
    \tilde{S}_t = \tilde{S}_0 + M_t + \int_0^t \alpha_s\,d\langle M\rangle_s
    $$

    where $M_t = \int_0^t \sigma(v_s)S_s\,dW_s^1$ is the martingale part, and $\alpha_s = (\mu - r)/(\sigma(v_s)^2 S_s^2) \cdot S_s^2 = (\mu - r)/\sigma(v_s)^2$. The Girsanov change affects only $W^1$:

    $$
    \hat{W}_t^1 = W_t^1 + \int_0^t \frac{\mu - r}{\sigma(v_s)}\,ds
    $$

    Since $\rho = 0$, the process $W^2$ is orthogonal to $M$ (which is driven entirely by $W^1$). By definition, the minimal martingale measure preserves every $\mathbb{P}$-local martingale orthogonal to $\tilde{S}$. Since $W^2$ is orthogonal to $M$ (and hence to $\tilde{S}$), $W^2$ remains a Brownian motion under $\hat{\mathbb{P}}$. Consequently, the dynamics of $v_t = f(W^2)$ are **unchanged** under $\hat{\mathbb{P}}$.

    **Effect on pricing:** The locally risk-minimizing price $\hat{V} = \hat{\mathbb{E}}[e^{-r(T-t)}H \mid \mathcal{F}_t]$ uses the physical-measure volatility dynamics. In contrast, a risk-neutral price under an arbitrary EMM would introduce a **market price of volatility risk** $\lambda_v$, modifying the drift of $v$ to $dv_t = [\kappa(\theta - v_t) - \lambda_v \eta(v_t)]\,dt + \eta(v_t)\,d\hat{W}_t^2$. This changes the distribution of future volatility and hence the option price.

    The minimal martingale measure is the unique EMM that does not "distort" the volatility dynamics --- it only removes the equity risk premium. This makes it the most parsimonious choice and the natural pricing measure for local risk minimization.

---

**Exercise 3.** The Kunita-Watanabe decomposition writes $N_t = N_0 + \int_0^t \phi_s\,dM_s + L_t$ with $\langle L, M\rangle = 0$. For a two-dimensional Brownian motion $(W^1, W^2)$ with $M_t = W_t^1$, decompose $N_t = \rho W_t^1 + \sqrt{1-\rho^2}W_t^2$. Identify $\phi$ and $L$, and verify $\langle L, M\rangle = 0$. What is $\mathbb{E}[L_T^2]$ and what fraction of $N$'s variance is hedgeable?

??? success "Solution to Exercise 3"
    Given $M_t = W_t^1$ and $N_t = \rho W_t^1 + \sqrt{1 - \rho^2}\,W_t^2$, the Kunita-Watanabe decomposition writes:

    $$
    N_t = N_0 + \int_0^t \phi_s\,dM_s + L_t
    $$

    Since $N_0 = 0$ and $M_t = W_t^1$, we identify:

    $$
    N_t = \rho W_t^1 + \sqrt{1 - \rho^2}\,W_t^2 = \int_0^t \rho\,dW_s^1 + \sqrt{1 - \rho^2}\,W_t^2
    $$

    Therefore:

    - $\phi_s = \rho$ (a constant predictable process)
    - $L_t = \sqrt{1 - \rho^2}\,W_t^2$

    **Verification of orthogonality:** We need $\langle L, M \rangle = 0$.

    $$
    \langle L, M \rangle_t = \left\langle \sqrt{1 - \rho^2}\,W^2,\; W^1 \right\rangle_t = \sqrt{1 - \rho^2}\,\langle W^2, W^1 \rangle_t = 0
    $$

    since $W^1$ and $W^2$ are independent Brownian motions.

    **Residual risk:**

    $$
    \mathbb{E}[L_T^2] = (1 - \rho^2)\,\mathbb{E}[(W_T^2)^2] = (1 - \rho^2) \cdot T
    $$

    The total variance of $N$ is $\mathbb{E}[N_T^2] = \rho^2 T + (1 - \rho^2)T = T$. The hedgeable fraction is:

    $$
    \frac{\mathbb{E}[N_T^2] - \mathbb{E}[L_T^2]}{\mathbb{E}[N_T^2]} = \frac{T - (1 - \rho^2)T}{T} = \rho^2
    $$

    So a fraction $\rho^2$ of $N$'s variance is hedgeable by trading $M = W^1$.

---

**Exercise 4.** Local risk minimization and variance-optimal hedging coincide when the mean-variance tradeoff $\hat{K}_T = \int_0^T \alpha_t^2\,d\langle M\rangle_t$ is deterministic. For the Black-Scholes model with $\alpha = (\mu - r)/\sigma^2$ and $d\langle M\rangle_t = \sigma^2 S_t^2\,dt$, show that $\hat{K}_T = ((\mu - r)/\sigma)^2 T$, which is deterministic. Conclude that both quadratic approaches yield the same hedge in Black-Scholes.

??? success "Solution to Exercise 4"
    In the Black-Scholes model, $\tilde{S}_t = S_t e^{-rt}$ satisfies:

    $$
    d\tilde{S}_t = (\mu - r)\tilde{S}_t\,dt + \sigma\tilde{S}_t\,dW_t
    $$

    The martingale part is $dM_t = \sigma\tilde{S}_t\,dW_t$, so $d\langle M\rangle_t = \sigma^2\tilde{S}_t^2\,dt$.

    The drift can be written as:

    $$
    (\mu - r)\tilde{S}_t\,dt = \frac{\mu - r}{\sigma^2\tilde{S}_t^2} \cdot \sigma^2\tilde{S}_t^2\,dt \cdot \tilde{S}_t
    $$

    Wait --- more carefully, from the structure condition $d\tilde{S}_t = dM_t + \alpha_t\,d\langle M\rangle_t$:

    $$
    (\mu - r)\tilde{S}_t\,dt = \alpha_t \cdot \sigma^2\tilde{S}_t^2\,dt \implies \alpha_t = \frac{\mu - r}{\sigma^2\tilde{S}_t}
    $$

    Now compute the mean-variance tradeoff:

    $$
    \hat{K}_T = \int_0^T \alpha_t^2\,d\langle M\rangle_t = \int_0^T \frac{(\mu - r)^2}{\sigma^4\tilde{S}_t^2} \cdot \sigma^2\tilde{S}_t^2\,dt = \int_0^T \frac{(\mu - r)^2}{\sigma^2}\,dt = \frac{(\mu - r)^2}{\sigma^2}\,T
    $$

    This simplifies to:

    $$
    \hat{K}_T = \left(\frac{\mu - r}{\sigma}\right)^2 T = \lambda^2 T
    $$

    where $\lambda = (\mu - r)/\sigma$ is the Sharpe ratio. Since $\mu$, $r$, and $\sigma$ are all constants, $\hat{K}_T$ is **deterministic**.

    Because $\hat{K}_T$ is deterministic, the local risk minimization and variance-optimal hedging approaches coincide. Both yield the same hedge ratio, and the minimal martingale measure equals the variance-optimal measure (which is the unique risk-neutral measure in the Black-Scholes model). Thus, in the complete Black-Scholes market, all quadratic hedging approaches reduce to the standard delta-hedging replicating strategy.

---

**Exercise 5.** In the basis risk model with $\rho = 0.6$, $\sigma_S = 0.20$, $\sigma_Y = 0.30$, and a call on $Y$ with $\Delta_Y = 0.50$, $Y_0 = S_0 = 100$: compute the locally risk-minimizing hedge $\xi^{\text{LRM}} = \rho(\sigma_Y/\sigma_S)(Y/S)\Delta_Y$. Compute the residual risk as $(1-\rho^2)\operatorname{Var}(H)$ if $\operatorname{Var}(H) = 50$. By how much does the hedge reduce the total risk compared to an unhedged position?

??? success "Solution to Exercise 5"
    Given $\rho = 0.6$, $\sigma_S = 0.20$, $\sigma_Y = 0.30$, $\Delta_Y = 0.50$, and $Y_0 = S_0 = 100$:

    $$
    \xi^{\text{LRM}} = \rho \cdot \frac{\sigma_Y}{\sigma_S} \cdot \frac{Y_0}{S_0} \cdot \Delta_Y = 0.6 \times \frac{0.30}{0.20} \times \frac{100}{100} \times 0.50 = 0.6 \times 1.5 \times 1.0 \times 0.50 = 0.45
    $$

    The locally risk-minimizing hedge is to hold **0.45 shares** of $S$ per unit of the claim.

    The residual risk with $\operatorname{Var}(H) = 50$:

    $$
    \text{Residual variance} = (1 - \rho^2)\operatorname{Var}(H) = (1 - 0.36) \times 50 = 0.64 \times 50 = 32
    $$

    The residual standard deviation is $\sqrt{32} \approx 5.66$.

    **Risk reduction compared to unhedged position:**

    - Unhedged variance: $\operatorname{Var}(H) = 50$, so unhedged std dev $= \sqrt{50} \approx 7.07$.
    - Hedged residual variance: $32$, so hedged std dev $\approx 5.66$.
    - Variance reduction: $50 - 32 = 18$, which is $18/50 = 36\%$ of total variance.
    - Standard deviation reduction: from $7.07$ to $5.66$, a decrease of $1.41$ or about $20\%$.

    The hedge removes $\rho^2 = 36\%$ of the claim's variance. While meaningful, a correlation of $0.6$ provides only moderate hedge effectiveness. Increasing $\rho$ to $0.8$ would raise the hedgeable fraction to $64\%$, nearly doubling the risk reduction.

---

**Exercise 6.** The coefficient of determination $R^2 = \rho^2$ measures hedge effectiveness. A trader hedges a basket option on three stocks using only the index. The basket's correlation with the index is $\rho = 0.85$. Compute $R^2$ and the fraction of unhedgeable variance. If the basket option has standard deviation $\$5.00$, what is the minimum achievable hedging error standard deviation? The trader considers adding a sector ETF with incremental $R^2$ improvement of $0.05$. What is the new residual standard deviation?

??? success "Solution to Exercise 6"
    The coefficient of determination is:

    $$
    R^2 = \rho^2 = 0.85^2 = 0.7225
    $$

    The fraction of unhedgeable variance is $1 - R^2 = 1 - 0.7225 = 0.2775$, or about $27.75\%$.

    With the basket option standard deviation of $\$5.00$, the variance is $25.00$. The minimum achievable hedging error standard deviation is:

    $$
    \sqrt{(1 - R^2) \cdot \operatorname{Var}(H)} = \sqrt{0.2775 \times 25} = \sqrt{6.9375} \approx \$2.63
    $$

    **Adding the sector ETF:** The new $R^2$ becomes $0.7225 + 0.05 = 0.7725$. The new residual fraction is $1 - 0.7725 = 0.2275$. The new residual standard deviation is:

    $$
    \sqrt{0.2275 \times 25} = \sqrt{5.6875} \approx \$2.39
    $$

    Adding the sector ETF reduces the hedging error standard deviation from $\$2.63$ to $\$2.39$, a reduction of about $\$0.24$ (roughly $9\%$). Each incremental instrument provides diminishing marginal improvement as $R^2$ approaches $1$.
