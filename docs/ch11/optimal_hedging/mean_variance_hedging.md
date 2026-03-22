# Mean-Variance Hedging

In incomplete markets, perfect replication is generally impossible. **Mean-variance hedging** seeks the self-financing trading strategy that minimizes the expected squared hedging error at maturity. This criterion leads to elegant solutions via $L^2$ projection theory and the **Follmer-Schweizer decomposition**, connecting hedging to fundamental concepts in functional analysis.

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
    The variance-optimal martingale measure $\mathbb{Q}^*$ is the equivalent martingale measure that minimizes the $L^2(\mathbb{P})$ norm of its Radon-Nikodym derivative:

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
