# Mean-Variance Hedging

In incomplete markets, perfect replication is generally impossible. **Mean-variance hedging** seeks the self-financing trading strategy that minimizes the expected squared hedging error at maturity. This criterion leads to elegant solutions via $L^2$ projection theory and the **Follmer-Schweizer decomposition**, connecting hedging to fundamental concepts in functional analysis.

!!! tip "Toy mechanism: orthogonal projection in $L^2$"
    The whole machinery is one geometric picture. Let $\mathcal{A}$ be the linear space of all attainable terminal wealths $\int_0^T\xi_t\,dS_t$ under self-financing strategies. Then minimising $\mathbb{E}[(H - V_T)^2]$ is exactly the question: *what is the closest point in $\mathcal{A}$ to $H$ in $L^2$?* That is orthogonal projection — the same operation as projecting a vector onto a subspace in finite-dimensional geometry. The Föllmer–Schweizer decomposition $H = H_0 + \int_0^T\xi^H\,dS + L_T$ is the projection theorem with $\int\xi^H\,dS$ being the projection onto $\mathcal{A}$ and $L_T$ the orthogonal residual. The "optimal hedge" is just "drop a perpendicular." Everything below — the minimal martingale measure, BSDE characterisations, the connection to risk-neutral pricing — is bookkeeping on this single projection.

---

## The Mean-Variance Hedging Problem

### Setup

Let $(\Omega, \mathcal{F}, \mathbb{P})$ be a probability space with filtration $(\mathcal{F}_t)_{t \in [0,T]}$. Consider a market with:

- A risk-free asset (money market account) $B_t = e^{rt}$.
- A risky asset with discounted price process $\tilde{S}_t = S_t / B_t$.
- A contingent claim $H$ (an $\mathcal{F}_T$-measurable random variable representing the discounted payoff).

A **self-financing strategy** is a pair $(c, \xi)$ where $c \in \mathbb{R}$ is the initial capital and $\xi = (\xi_t)_{t \in [0,T]}$ is a predictable process representing the number of shares held. The terminal wealth of such a strategy is:

$$
c + \int_0^T \xi_t\,d\tilde{S}_t =: c + G_T(\xi)
$$

where $G_T(\xi) = \int_0^T \xi_t\,d\tilde{S}_t$ is the **gains process**.

### The Optimization Problem

!!! abstract "Definition: Mean-Variance Hedging Problem"
    The mean-variance hedging problem is to find $(c^*, \xi^*)$ that minimizes the expected squared hedging error:

    $$
    \boxed{\min_{c \in \mathbb{R},\; \xi \in \Theta} \mathbb{E}\!\left[\left(H - c - G_T(\xi)\right)^2\right]}
    $$

    where $\Theta$ is the space of admissible (predictable, square-integrable) trading strategies.

This is a **least-squares problem** in the Hilbert space $L^2(\Omega, \mathcal{F}_T, \mathbb{P})$: we seek the best approximation of the claim $H$ by elements of the form $c + G_T(\xi)$.

---

## The L-Squared Projection Interpretation

### Hilbert Space Structure

The space $L^2(\mathbb{P}) = L^2(\Omega, \mathcal{F}_T, \mathbb{P})$ is a Hilbert space with inner product:

$$
\langle X, Y \rangle = \mathbb{E}[XY]
$$

The set of attainable terminal wealths forms a **closed linear subspace**:

$$
\mathcal{G} = \left\{c + G_T(\xi) : c \in \mathbb{R},\; \xi \in \Theta\right\} \subset L^2(\mathbb{P})
$$

The mean-variance hedging problem is the **orthogonal projection** of $H$ onto $\mathcal{G}$:

$$
\boxed{c^* + G_T(\xi^*) = \operatorname{proj}_{\mathcal{G}}(H)}
$$

**Theorem (Projection Characterization).** *The pair $(c^*, \xi^*)$ is the mean-variance optimal hedge if and only if the hedging error is orthogonal to $\mathcal{G}$:*

$$
\mathbb{E}\!\left[\left(H - c^* - G_T(\xi^*)\right) \cdot \left(c + G_T(\xi)\right)\right] = 0 \quad \text{for all } c \in \mathbb{R},\; \xi \in \Theta
$$

??? note "Proof"
    This is a direct consequence of the projection theorem in Hilbert spaces. The space $\mathcal{G}$ is a closed subspace of $L^2(\mathbb{P})$ (closedness requires a technical argument involving the structure of stochastic integrals). For any $H \in L^2(\mathbb{P})$, there exists a unique $\hat{H} \in \mathcal{G}$ such that $\|H - \hat{H}\|_2 \leq \|H - G\|_2$ for all $G \in \mathcal{G}$, and the minimizer is characterized by the orthogonality condition $H - \hat{H} \perp \mathcal{G}$. $\square$

### Consequences of Orthogonality

Setting $\xi = 0$ in the orthogonality condition gives:

$$
\mathbb{E}[H - c^* - G_T(\xi^*)] \cdot c = 0 \quad \text{for all } c
$$

which implies $c^* = \mathbb{E}[H] - \mathbb{E}[G_T(\xi^*)]$. If $\tilde{S}$ is a martingale under $\mathbb{P}$ (i.e., $\mathbb{E}[G_T(\xi)] = 0$ for all $\xi$), then:

$$
c^* = \mathbb{E}[H]
$$

The optimal initial capital equals the expected discounted payoff under the physical measure.

---

## The Follmer-Schweizer Decomposition

### Statement

The Follmer-Schweizer (FS) decomposition provides the key structural result for mean-variance hedging in a semimartingale framework.

**Theorem (Follmer-Schweizer Decomposition).** *Under suitable integrability conditions, any $H \in L^2(\mathbb{P})$ admits a unique decomposition:*

$$
\boxed{H = H_0 + \int_0^T \xi_t^H\,d\tilde{S}_t + L_T^H}
$$

*where:*

- *$H_0 \in \mathbb{R}$ is a constant (the initial value).*
- *$\xi^H$ is a predictable process (the hedging strategy).*
- *$L^H$ is a martingale orthogonal to $\tilde{S}$ (i.e., $\langle L^H, \tilde{S} \rangle = 0$), representing the unhedgeable risk.*

### Connection to Mean-Variance Hedging

Under additional conditions (notably that $\tilde{S}$ satisfies the **structure condition** --- see below), the FS decomposition yields the mean-variance optimal hedge:

$$
c^* = H_0, \qquad \xi^* = \xi^H
$$

The minimum hedging error is:

$$
\min_{c, \xi} \mathbb{E}\!\left[(H - c - G_T(\xi))^2\right] = \mathbb{E}\!\left[(L_T^H)^2\right]
$$

This is the variance of the unhedgeable component --- an intrinsic measure of the claim's "distance from attainability."

### The Structure Condition

The FS decomposition and its optimality require that $\tilde{S}$ satisfies the **structure condition**: $\tilde{S}$ is a semimartingale that can be decomposed as:

$$
\tilde{S}_t = \tilde{S}_0 + M_t + \int_0^t \alpha_s\,d\langle M \rangle_s
$$

where $M$ is the martingale part and $\alpha$ is a predictable process (the **mean-variance tradeoff process**). The quantity:

$$
\hat{K}_T = \int_0^T \alpha_t^2\,d\langle M \rangle_t
$$

is the **mean-variance tradeoff** of $\tilde{S}$. For the FS decomposition to yield the mean-variance optimal hedge, one needs $\hat{K}_T$ to be deterministic or, more generally, the **Kunita-Watanabe condition** to hold.

---

## The Variance-Optimal Measure

### Definition

An alternative characterization of mean-variance hedging uses the **variance-optimal martingale measure**.

!!! abstract "Definition: Variance-Optimal Measure"
    The variance-optimal martingale measure $\mathbb{Q}^*$ is the equivalent martingale measure that minimizes the $L^2(\mathbb{P})$ norm of its Radon–Nikodym derivative:

    $$
    \mathbb{Q}^* = \arg\min_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}\!\left[\left(\frac{d\mathbb{Q}}{d\mathbb{P}}\right)^2\right]
    $$

    where $\mathcal{M}$ is the set of equivalent martingale measures.

**Theorem.** *Under the structure condition with deterministic mean-variance tradeoff $\hat{K}_T$, the mean-variance optimal initial capital is:*

$$
c^* = \mathbb{E}^{\mathbb{Q}^*}[H]
$$

*and the variance-optimal measure has the density:*

$$
\frac{d\mathbb{Q}^*}{d\mathbb{P}} = \frac{\mathcal{E}(-\alpha \cdot M)_T}{\mathbb{E}[\mathcal{E}(-\alpha \cdot M)_T]}
$$

*where $\mathcal{E}$ denotes the stochastic exponential.*

---

## Explicit Solution in the Black-Scholes Framework

### Complete Market Case

In the standard Black-Scholes model ($dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$), the market is complete and every $H \in L^2$ is attainable. The mean-variance optimal hedge coincides with the perfect replicating strategy:

$$
c^* = e^{-rT}\mathbb{E}^{\mathbb{Q}}[H], \qquad \xi_t^* = \frac{\partial V}{\partial S}(t, S_t)
$$

where $V$ solves the Black-Scholes PDE. The hedging error is zero: $L_T^H = 0$.

### Incomplete Market: Stochastic Volatility

Consider the Heston model:

$$
dS_t = \mu S_t\,dt + \sqrt{v_t}\,S_t\,dW_t^1, \qquad dv_t = \kappa(\theta - v_t)\,dt + \eta\sqrt{v_t}\,dW_t^2
$$

with $\operatorname{Corr}(dW^1, dW^2) = \rho$. The market is incomplete (volatility risk cannot be hedged with the stock alone). The FS decomposition of a European claim $H = h(S_T)$ has:

- $\xi_t^H$ involves both $\partial V / \partial S$ and an additional term correcting for the drift of $v_t$.
- $L_T^H \neq 0$ captures the unhedgeable volatility risk.
- $\mathbb{E}[(L_T^H)^2]$ measures the residual hedging variance, which depends on $\eta$ and $|\rho|$.

!!! info "Role of Correlation"
    When $|\rho| = 1$ (perfect stock-volatility correlation), the model is effectively complete and $L_T^H = 0$. As $|\rho|$ decreases, the unhedgeable component grows. At $\rho = 0$, the volatility risk is entirely orthogonal to the stock and cannot be reduced by trading the stock.

---

## Worked Example: Incomplete Market with Basis Risk

Consider hedging a claim on an illiquid asset $Y$ using a correlated liquid asset $S$:

$$
dS_t = \mu_S S_t\,dt + \sigma_S S_t\,dW_t^1, \qquad dY_t = \mu_Y Y_t\,dt + \sigma_Y Y_t\left(\rho\,dW_t^1 + \sqrt{1-\rho^2}\,dW_t^2\right)
$$

The claim is $H = (Y_T - K)^+$ (call on $Y$), but only $S$ is tradeable.

**Mean-variance optimal hedge:**

The optimal number of shares of $S$ held at time $t$ is:

$$
\xi_t^* = \rho \cdot \frac{\sigma_Y}{\sigma_S} \cdot \frac{Y_t}{S_t} \cdot \frac{\partial C}{\partial Y}(t, Y_t)
$$

where $C(t, Y)$ is the Black-Scholes price of the call on $Y$. This is the **minimum-variance hedge ratio**, a classical result in cross-hedging.

**Minimum hedging error:**

$$
\mathbb{E}[(H - c^* - G_T(\xi^*))^2] = (1 - \rho^2) \cdot \operatorname{Var}(H)
$$

The fraction $\rho^2$ of the claim's variance is hedgeable; the remaining $1 - \rho^2$ is unhedgeable basis risk.

| Correlation $\rho$ | Hedgeable fraction | Residual variance |
|:---|:---|:---|
| 1.0 | 100% | 0% |
| 0.9 | 81% | 19% |
| 0.7 | 49% | 51% |
| 0.5 | 25% | 75% |
| 0.0 | 0% | 100% |

---

## Relationship to Other Approaches

### Mean-Variance vs. Risk-Neutral Hedging

| Aspect | Mean-variance hedging | Risk-neutral (delta) hedging |
|:---|:---|:---|
| Measure | Physical measure $\mathbb{P}$ | Risk-neutral measure $\mathbb{Q}$ |
| Criterion | Minimize $\mathbb{E}^{\mathbb{P}}[(H - c - G_T)^2]$ | Replicate under $\mathbb{Q}$ |
| Complete markets | Coincides with replication | Perfect hedge |
| Incomplete markets | Optimal $L^2$ approximation | Depends on choice of $\mathbb{Q}$ |
| Initial capital | $\mathbb{E}^{\mathbb{Q}^*}[H]$ | $\mathbb{E}^{\mathbb{Q}}[H]$ (model-dependent) |

### Mean-Variance vs. Quadratic Hedging

Mean-variance hedging is a **global** criterion: it minimizes the total hedging error at maturity. **Local risk minimization** (covered in the next section) minimizes the risk incrementally at each time step. The two approaches coincide in complete markets but differ in incomplete markets.

---

## Summary

| Concept | Key result |
|:---|:---|
| Problem | $\min_{c, \xi} \mathbb{E}[(H - c - G_T(\xi))^2]$ |
| Solution method | $L^2$ projection onto the space of attainable payoffs |
| FS decomposition | $H = H_0 + \int \xi^H\,d\tilde{S} + L_T^H$ (hedgeable + unhedgeable) |
| Optimal initial capital | $c^* = H_0 = \mathbb{E}^{\mathbb{Q}^*}[H]$ (under structure condition) |
| Minimum error | $\mathbb{E}[(L_T^H)^2]$ = variance of unhedgeable component |
| Variance-optimal measure | $\mathbb{Q}^*$ minimizes $\mathbb{E}[(d\mathbb{Q}/d\mathbb{P})^2]$ |
| Complete markets | Reduces to perfect replication |
| Basis risk | Hedgeable fraction = $\rho^2$ when using correlated proxy |

---

## Exercises

**Exercise 1.** In the basis risk model with $dS_t = 0.08 S_t\,dt + 0.20 S_t\,dW_t^1$ and $dY_t = 0.10 Y_t\,dt + 0.30 Y_t(\rho\,dW_t^1 + \sqrt{1-\rho^2}\,dW_t^2)$, the minimum-variance hedge ratio for a call on $Y$ is $\xi_t^* = \rho(\sigma_Y/\sigma_S)(Y_t/S_t)(\partial C/\partial Y)$. For $\rho = 0.8$, $S_0 = Y_0 = 100$, and $\Delta_Y = \partial C/\partial Y = 0.55$, compute the optimal number of shares of $S$ to hold. What happens to $\xi^*$ as $\rho \to 0$?

??? success "Solution to Exercise 1"
    We are given $\rho = 0.8$, $\sigma_Y = 0.30$, $\sigma_S = 0.20$, $S_0 = Y_0 = 100$, and $\Delta_Y = 0.55$. The minimum-variance hedge ratio is:

    $$
    \xi^* = \rho \cdot \frac{\sigma_Y}{\sigma_S} \cdot \frac{Y_0}{S_0} \cdot \Delta_Y
    $$

    Substituting:

    $$
    \xi^* = 0.8 \times \frac{0.30}{0.20} \times \frac{100}{100} \times 0.55 = 0.8 \times 1.5 \times 1.0 \times 0.55 = 0.66
    $$

    The agent should hold **0.66 shares** of $S$ per unit of the claim on $Y$.

    As $\rho \to 0$, the hedge ratio $\xi^* \to 0$. This is intuitive: when the correlation between $S$ and $Y$ vanishes, trading $S$ provides no information about or exposure to $Y$, so the optimal hedge involves no position in $S$ at all. The assets become independent, and hedging with $S$ is futile.

---

**Exercise 2.** The hedgeable fraction of a claim's variance in the basis risk model is $\rho^2$. For correlations $\rho = 0.5, 0.7, 0.8, 0.9, 0.95$, compute both the hedgeable fraction and the residual variance $(1-\rho^2)\operatorname{Var}(H)$. If $\operatorname{Var}(H) = 100$, at what correlation level does the residual standard deviation fall below $\$3$?

??? success "Solution to Exercise 2"
    The hedgeable fraction is $\rho^2$ and the residual variance is $(1 - \rho^2)\operatorname{Var}(H)$. With $\operatorname{Var}(H) = 100$:

    | $\rho$ | $\rho^2$ (hedgeable) | $1 - \rho^2$ (residual fraction) | Residual variance | Residual std dev |
    |:---|:---|:---|:---|:---|
    | 0.50 | 0.250 | 0.750 | 75.0 | 8.66 |
    | 0.70 | 0.490 | 0.510 | 51.0 | 7.14 |
    | 0.80 | 0.640 | 0.360 | 36.0 | 6.00 |
    | 0.90 | 0.810 | 0.190 | 19.0 | 4.36 |
    | 0.95 | 0.9025 | 0.0975 | 9.75 | 3.12 |

    We need the residual standard deviation to fall below $\$3$, so:

    $$
    \sqrt{(1 - \rho^2) \times 100} < 3 \implies (1 - \rho^2) \times 100 < 9 \implies \rho^2 > 0.91 \implies \rho > \sqrt{0.91} \approx 0.954
    $$

    The correlation must exceed approximately **0.954** for the residual standard deviation to fall below $\$3$.

---

**Exercise 3.** The orthogonality condition for the mean-variance optimal hedge states $\mathbb{E}[(H - c^* - G_T(\xi^*))(c + G_T(\xi))] = 0$ for all $c, \xi$. Explain why setting $\xi = 0$ gives $c^* = \mathbb{E}[H]$ when $\tilde{S}$ is a $\mathbb{P}$-martingale. What is the economic interpretation of this condition --- why must the hedging error be uncorrelated with every tradeable payoff?

??? success "Solution to Exercise 3"
    Setting $\xi = 0$ in the orthogonality condition:

    $$
    \mathbb{E}\!\left[(H - c^* - G_T(\xi^*)) \cdot c\right] = 0 \quad \text{for all } c \in \mathbb{R}
    $$

    Since $c$ is an arbitrary constant, this requires:

    $$
    \mathbb{E}[H - c^* - G_T(\xi^*)] = 0
    $$

    When $\tilde{S}$ is a $\mathbb{P}$-martingale, the stochastic integral $G_T(\xi) = \int_0^T \xi_t\,d\tilde{S}_t$ is also a martingale (under integrability conditions), so $\mathbb{E}[G_T(\xi^*)] = 0$. Therefore:

    $$
    \mathbb{E}[H] - c^* = 0 \implies c^* = \mathbb{E}[H]
    $$

    **Economic interpretation:** The orthogonality condition states that the hedging error $\varepsilon = H - c^* - G_T(\xi^*)$ must be uncorrelated with every tradeable payoff $c + G_T(\xi)$. If it were correlated, one could construct a modified strategy that exploits this correlation to reduce the mean-squared error further, contradicting the optimality of $(c^*, \xi^*)$.

    In financial terms, this means the residual risk after optimal hedging is **purely idiosyncratic** relative to the traded instruments. No linear combination of traded assets can explain any remaining variation in the hedging error. This is the financial analogue of the residual in an OLS regression being orthogonal to the regressors.

---

**Exercise 4.** In the Heston model with $|\rho| = 0.7$, the unhedgeable component $L_T^H$ captures volatility risk. If $\mathbb{E}[(L_T^H)^2] = (1 - \rho^2) \cdot \operatorname{Var}(H)$ approximately, and $\operatorname{Var}(H) = 64$ for an ATM call, compute the minimum hedging error standard deviation achievable by trading the stock alone. How much additional variance reduction would a variance swap (adding a second traded instrument) provide if it has correlation $0.95$ with the volatility factor?

??? success "Solution to Exercise 4"
    With $|\rho| = 0.7$ and $\operatorname{Var}(H) = 64$:

    $$
    \mathbb{E}[(L_T^H)^2] = (1 - \rho^2)\operatorname{Var}(H) = (1 - 0.49) \times 64 = 0.51 \times 64 = 32.64
    $$

    The minimum hedging error standard deviation from trading the stock alone is:

    $$
    \sqrt{32.64} \approx 5.71
    $$

    Now suppose we add a variance swap with correlation $0.95$ with the volatility factor. The volatility factor corresponds to $W^2$ (the orthogonal Brownian motion). The stock hedges the $W^1$ component (with effectiveness $\rho^2 = 0.49$), leaving $1 - \rho^2 = 0.51$ of the variance unhedged.

    The unhedged variance is $(1 - \rho^2)\operatorname{Var}(H) = 32.64$. The variance swap, correlated at $0.95$ with the volatility factor, can hedge a fraction $0.95^2 = 0.9025$ of this remaining unhedged variance. Therefore the additional variance reduction is:

    $$
    0.9025 \times 32.64 \approx 29.46
    $$

    The new residual variance is:

    $$
    32.64 - 29.46 = 3.18
    $$

    The new residual standard deviation is $\sqrt{3.18} \approx 1.78$. The variance swap reduces the residual standard deviation from approximately $\$5.71$ to approximately $\$1.78$, a dramatic improvement. The total hedgeable fraction of variance rises from $49\%$ to approximately $95\%$.

---

**Exercise 5.** The Follmer-Schweizer decomposition writes $H = H_0 + \int_0^T \xi_t^H\,d\tilde{S}_t + L_T^H$. In a complete market ($L_T^H = 0$), this reduces to the replicating strategy. For a European call in the Black-Scholes model with $S_0 = 100$, $K = 100$, $\sigma = 0.20$, $r = 0.05$, $T = 1$, identify $H_0$ (the optimal initial capital) and $\xi_t^*$ (the hedging strategy). Verify that $H_0$ equals the Black-Scholes price.

??? success "Solution to Exercise 5"
    In the Black-Scholes model with $S_0 = 100$, $K = 100$, $\sigma = 0.20$, $r = 0.05$, $T = 1$, the market is complete, so $L_T^H = 0$ and the FS decomposition reduces to:

    $$
    H = H_0 + \int_0^T \xi_t^H\,d\tilde{S}_t
    $$

    **Identifying $H_0$:** The optimal initial capital is the Black-Scholes price of the call:

    $$
    H_0 = e^{-rT}\,\text{BS}(S_0, K, T, \sigma, r)
    $$

    Computing the Black-Scholes price:

    $$
    d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} = \frac{0 + (0.05 + 0.02) \times 1}{0.20} = \frac{0.07}{0.20} = 0.35
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T} = 0.35 - 0.20 = 0.15
    $$

    Using standard normal values: $N(0.35) \approx 0.6368$ and $N(0.15) \approx 0.5596$.

    $$
    C = S_0\,N(d_1) - K e^{-rT}N(d_2) = 100 \times 0.6368 - 100 \times e^{-0.05} \times 0.5596
    $$

    $$
    C = 63.68 - 100 \times 0.9512 \times 0.5596 = 63.68 - 53.23 = 10.45
    $$

    So $H_0 \approx \$10.45$ (the discounted Black-Scholes price of the call).

    **Identifying $\xi_t^*$:** The hedging strategy is the Black-Scholes delta:

    $$
    \xi_t^* = \frac{\partial C}{\partial S}(t, S_t) = N(d_1(t, S_t))
    $$

    where $d_1(t, S_t) = \frac{\ln(S_t/K) + (r + \sigma^2/2)(T - t)}{\sigma\sqrt{T - t}}$.

    **Verification:** In a complete market, the FS decomposition initial value $H_0$ equals $\mathbb{E}^{\mathbb{Q}}[\tilde{H}]$, which is precisely the discounted risk-neutral expectation --- the Black-Scholes price. The hedging error is zero ($L_T^H = 0$) because the claim is perfectly replicable.

---

**Exercise 6.** The variance-optimal measure $\mathbb{Q}^*$ minimizes $\mathbb{E}[(d\mathbb{Q}/d\mathbb{P})^2]$ over all equivalent martingale measures. In a model where $d\tilde{S}_t = \sigma\tilde{S}_t\,dW_t + \alpha\sigma^2\tilde{S}_t\,dt$ (with $\alpha = (\mu - r)/\sigma^2$), the density of $\mathbb{Q}^*$ involves the stochastic exponential $\mathcal{E}(-\alpha\sigma\,W)_T$. For $\mu = 0.08$, $r = 0.03$, $\sigma = 0.25$, $T = 1$, compute the Sharpe ratio $\lambda = (\mu - r)/\sigma$ and the mean-variance tradeoff $\hat{K}_T = \lambda^2 T$. What is the economic interpretation of $\hat{K}_T$?

??? success "Solution to Exercise 6"
    The Sharpe ratio is:

    $$
    \lambda = \frac{\mu - r}{\sigma} = \frac{0.08 - 0.03}{0.25} = \frac{0.05}{0.25} = 0.20
    $$

    The mean-variance tradeoff is:

    $$
    \hat{K}_T = \lambda^2 T = 0.20^2 \times 1 = 0.04
    $$

    **Economic interpretation:** The mean-variance tradeoff $\hat{K}_T$ measures the **maximum Sharpe ratio squared** accumulated over the trading horizon. It quantifies the reward-to-risk ratio available from optimally investing in the risky asset.

    Specifically, $\hat{K}_T = \lambda^2 T$ represents:

    - The squared Sharpe ratio multiplied by the time horizon, reflecting the cumulative opportunity cost of risk.
    - In the Merton portfolio problem, the maximum expected log-return per unit variance achievable by continuous trading over $[0, T]$.
    - It appears in the density of the variance-optimal measure: $d\mathbb{Q}^*/d\mathbb{P} \propto \mathcal{E}(-\lambda W)_T$, and $\hat{K}_T$ determines how far $\mathbb{Q}^*$ deviates from $\mathbb{P}$. A larger $\hat{K}_T$ means a larger Girsanov drift removal, and the variance-optimal measure differs more from the physical measure.

    When $\hat{K}_T$ is deterministic (as here, since all parameters are constant), the local risk minimization and variance-optimal hedging strategies coincide. The value $\hat{K}_T = 0.04$ indicates a relatively modest reward-to-risk ratio, consistent with the moderate Sharpe ratio of $0.20$.
