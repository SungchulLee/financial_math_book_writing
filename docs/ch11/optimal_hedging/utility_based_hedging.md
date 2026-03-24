# Utility-Based Hedging

In incomplete markets, there is no unique price or hedge for a contingent claim. **Utility-based hedging** resolves this ambiguity by introducing the agent's risk preferences through a utility function. The agent selects the trading strategy that maximizes expected utility of terminal wealth, and prices are determined by **indifference** --- the price at which the agent is equally happy trading or not trading the claim.

---

## Expected Utility Framework

### The Agent's Problem

An agent with initial wealth $w$, utility function $U$, and access to a traded asset $S$ solves:

$$
\boxed{u(w) = \sup_{\xi \in \Theta} \mathbb{E}\!\left[U\!\left(w + \int_0^T \xi_t\,dS_t - \int_0^T r\,\xi_t S_t\,dt\right)\right]}
$$

where $u(w)$ is the **value function** (maximum expected utility achievable from initial wealth $w$), and the optimization is over admissible self-financing strategies.

### Standard Utility Functions

| Utility | $U(x)$ | Risk aversion | CARA/CRRA |
|:---|:---|:---|:---|
| Exponential | $-e^{-\gamma x}$ | Constant absolute ($\gamma$) | CARA |
| Power | $\frac{x^{1-p}}{1-p}$, $p > 0, p \neq 1$ | Constant relative ($p$) | CRRA |
| Logarithmic | $\ln(x)$ | $p = 1$ limit | CRRA |
| Quadratic | $x - \frac{\gamma}{2}x^2$ | Increasing (unrealistic tail) | Neither |

The exponential utility is especially tractable because it separates initial wealth from the optimization, as we shall see.

---

## Utility Indifference Pricing

### Definition

!!! abstract "Definition: Indifference Price"
    The **utility indifference price** $p$ of a claim $H$ is the amount the agent is willing to pay (or receive) such that expected utility is the same whether or not the trade occurs:

    $$
    \boxed{\sup_\xi \mathbb{E}\!\left[U\!\left(w - p + \int_0^T \xi_t\,d\tilde{S}_t + H\right)\right] = \sup_\xi \mathbb{E}\!\left[U\!\left(w + \int_0^T \xi_t\,d\tilde{S}_t\right)\right]}
    $$

    The left side is the maximum expected utility when holding the claim (purchased at price $p$); the right side is the maximum expected utility without the claim.

### Buyer's and Seller's Price

- **Buyer's indifference price** $p^b$: The maximum the buyer will pay for the claim.
- **Seller's indifference price** $p^s$: The minimum the seller will accept to write the claim.

In general, $p^b \leq p^s$, with equality only in complete markets (where both equal the unique arbitrage-free price).

### Properties

**Theorem (Properties of Indifference Prices).** *The indifference price $p = p(H)$ satisfies:*

1. *$p(H)$ lies within the arbitrage-free price interval $[\inf_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[H],\; \sup_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[H]]$.*
2. *$p$ is monotone: $H_1 \leq H_2$ a.s. implies $p(H_1) \leq p(H_2)$.*
3. *$p$ is translation-invariant for CARA utility: $p(H + c) = p(H) + c$ for constants $c$.*
4. *$p$ is concave in $H$ (for concave $U$), reflecting risk aversion.*

---

## The Exponential Utility Case

### Separation of Wealth

For $U(x) = -e^{-\gamma x}$ (exponential/CARA utility), the indifference price is **independent of initial wealth**:

$$
p(H) = -\frac{1}{\gamma}\ln\frac{\sup_\xi \mathbb{E}\left[-e^{-\gamma(G_T(\xi) + H)}\right]}{\sup_\xi \mathbb{E}\left[-e^{-\gamma G_T(\xi)}\right]}
$$

This remarkable simplification occurs because $U(w + x) = -e^{-\gamma w} e^{-\gamma x}$, and the $e^{-\gamma w}$ factor cancels in the indifference equation.

### Connection to Relative Entropy

**Theorem (Entropic Pricing).** *Under exponential utility, the indifference price equals:*

$$
\boxed{p(H) = \sup_{\mathbb{Q} \in \mathcal{M}} \left\{\mathbb{E}^{\mathbb{Q}}[H] - \frac{1}{\gamma}\mathcal{H}(\mathbb{Q} \mid \mathbb{P})\right\}}
$$

*where $\mathcal{H}(\mathbb{Q} \mid \mathbb{P}) = \mathbb{E}^{\mathbb{Q}}\!\left[\ln\frac{d\mathbb{Q}}{d\mathbb{P}}\right]$ is the relative entropy of $\mathbb{Q}$ with respect to $\mathbb{P}$, and $\mathcal{M}$ is the set of equivalent martingale measures.*

??? note "Proof Sketch"
    The key insight is the **duality** between expected utility maximization and minimization over martingale measures. For exponential utility:

    $$
    \sup_\xi \mathbb{E}\!\left[-e^{-\gamma(G_T(\xi) + H)}\right] = -\inf_{\mathbb{Q} \in \mathcal{M}} \exp\!\left(-\gamma\,\mathbb{E}^{\mathbb{Q}}[H] + \mathcal{H}(\mathbb{Q} \mid \mathbb{P})\right)
    $$

    This follows from the convex duality theory of Kramkov-Schachermayer. Substituting into the indifference pricing formula and simplifying the logarithm yields the entropic representation. $\square$

### The Minimal Entropy Measure

In the limit of **small claims** ($H \to 0$ or $\gamma \to 0$), the optimal measure converges to the **minimal entropy martingale measure** $\mathbb{Q}^E$:

$$
\mathbb{Q}^E = \arg\min_{\mathbb{Q} \in \mathcal{M}} \mathcal{H}(\mathbb{Q} \mid \mathbb{P})
$$

The indifference price then approximates:

$$
p(H) \approx \mathbb{E}^{\mathbb{Q}^E}[H] + \frac{\gamma}{2}\operatorname{Var}^{\mathbb{Q}^E}(H - \hat{H}) + O(\gamma^2)
$$

where $\hat{H}$ is the hedgeable part of $H$ and $\operatorname{Var}^{\mathbb{Q}^E}(H - \hat{H})$ is the residual risk. The indifference price equals the minimal entropy price plus a risk premium proportional to $\gamma$ and the unhedgeable variance.

---

## Optimal Hedging Strategy

### Hamilton-Jacobi-Bellman Approach

In a Markovian setting with state variables $(S_t, Y_t)$ (where $Y$ captures additional risk factors), the value function $u(t, w, S, Y)$ satisfies the **HJB equation**:

$$
\sup_\xi \left\{u_t + \mathcal{L}_{S,Y} u + \xi(\mu - r)S\,u_w + \frac{1}{2}\xi^2 \sigma^2 S^2\,u_{ww} + \xi\,\rho\sigma\eta S\,u_{wY}\right\} = 0
$$

where $\mathcal{L}_{S,Y}$ is the generator of the $(S, Y)$ process. The first-order condition in $\xi$ gives:

$$
\xi^* = -\frac{(\mu - r)S\,u_w + \rho\sigma\eta S\,u_{wY}}{\sigma^2 S^2\,u_{ww}}
$$

For exponential utility with the ansatz $u = -\exp(-\gamma(w - g(t, S, Y)))$, this reduces to:

$$
\xi^*(t, S, Y) = \frac{\mu - r}{\gamma\sigma^2 S} + \frac{\rho\eta}{\sigma}\,g_Y(t, S, Y)
$$

The first term is the **Merton ratio** (myopic demand); the second is the **hedging demand** driven by the claim exposure to $Y$.

---

## Risk Aversion and the Price-Hedge Spectrum

### Effect of Risk Aversion $\gamma$

| $\gamma$ | Price behavior | Hedge behavior |
|:---|:---|:---|
| $\gamma \to 0$ (risk-neutral) | $p \to \mathbb{E}^{\mathbb{Q}^E}[H]$ (minimal entropy price) | Minimal hedging demand |
| $\gamma$ moderate | $p$ between min and max EMM prices | Balanced hedging |
| $\gamma \to \infty$ (extreme aversion) | $p \to \sup_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[H]$ (seller's superreplication) | Maximal hedging (superreplication) |

!!! info "Interpretation"
    As the agent becomes more risk-averse, the indifference price approaches the **superreplication price** --- the most conservative bound. In the limit, the agent is willing to pay any price up to the worst-case expectation to avoid unhedgeable risk entirely. Conversely, a nearly risk-neutral agent prices at the entropy-minimizing expectation, taking on residual risk for a lower premium.

---

## Worked Example: Exponential Utility with Basis Risk

Consider the basis risk model:

$$
dS_t = 0.08\,S_t\,dt + 0.20\,S_t\,dW_t^1, \qquad dY_t = 0.10\,Y_t\,dt + 0.25\,Y_t(\rho\,dW_t^1 + \sqrt{1-\rho^2}\,dW_t^2)
$$

with $r = 0.03$, $T = 0.5$, $\rho = 0.7$, and claim $H = (Y_T - 100)^+$.

**Without the claim** (Merton portfolio):

$$
\xi^{\text{Merton}} = \frac{0.08 - 0.03}{\gamma \times 0.04 \times S_t} = \frac{1.25}{\gamma S_t}
$$

**With the claim** (indifference hedge):

$$
\xi^* = \frac{1.25}{\gamma S_t} + \frac{0.7 \times 0.25}{0.20}\,g_Y(t, S_t, Y_t) = \frac{1.25}{\gamma S_t} + 0.875\,g_Y
$$

The additional term $0.875\,g_Y$ is the hedging demand. Near the money ($Y \approx 100$), $g_Y \approx \Delta_Y$ (the delta of the claim with respect to $Y$), so the hedge behaves like:

$$
\xi^{\text{hedge}} \approx 0.875 \times \Delta_Y(t, Y_t) \times \frac{Y_t}{S_t}
$$

This is close to the minimum-variance hedge ratio $\rho \sigma_Y / \sigma_S \times (Y/S) \times \Delta_Y = 0.7 \times 1.25 \times (Y/S) \times \Delta_Y = 0.875 \times (Y/S) \times \Delta_Y$.

**Indifference price** (for $\gamma = 1$): approximately \$7.20, compared to the Black-Scholes price of \$7.50 under the minimal entropy measure. The \$0.30 discount reflects the unhedgeable risk that the buyer absorbs.

---

## Comparison with Other Approaches

| Method | Criterion | Pricing measure | Wealth-dependent |
|:---|:---|:---|:---|
| **Utility indifference** | Max $\mathbb{E}[U(W_T)]$ | Depends on $U$ and $\gamma$ | Yes (except CARA) |
| **Mean-variance** | Min $\mathbb{E}[(H - c - G_T)^2]$ | Variance-optimal $\mathbb{Q}^*$ | No |
| **Local risk min** | Min conditional variance of cost | Minimal martingale $\hat{\mathbb{P}}$ | No |
| **Superreplication** | Worst-case replication | Supremum over $\mathcal{M}$ | No |

Utility-based hedging is the most general framework: it nests the others as special cases or limiting regimes. Mean-variance hedging corresponds to quadratic utility (with caveats about the domain), and superreplication emerges in the infinite risk-aversion limit.

---

## Summary

| Concept | Key result |
|:---|:---|
| Indifference price | Price at which $\mathbb{E}[U]$ is equal with and without the claim |
| Exponential utility | Price is wealth-independent; $p = \sup_{\mathbb{Q}} \{\mathbb{E}^{\mathbb{Q}}[H] - \frac{1}{\gamma}\mathcal{H}(\mathbb{Q} \mid \mathbb{P})\}$ |
| Optimal hedge | Merton demand + hedging demand from claim exposure |
| Small $\gamma$ limit | Price converges to minimal entropy expectation |
| Large $\gamma$ limit | Price converges to superreplication price |
| Residual risk premium | $\approx \frac{\gamma}{2}\operatorname{Var}^{\mathbb{Q}^E}(\text{unhedgeable part})$ |
| Advantage | Economically founded; handles preferences and incompleteness |
| Limitation | Requires specifying utility function and risk aversion parameter |

---

## Exercises

**Exercise 1.** The entropic pricing formula is $p(H) = \sup_{\mathbb{Q} \in \mathcal{M}}\{\mathbb{E}^{\mathbb{Q}}[H] - \frac{1}{\gamma}\mathcal{H}(\mathbb{Q} \mid \mathbb{P})\}$. For $\gamma = 2$, and two candidate martingale measures with $\mathbb{E}^{\mathbb{Q}_1}[H] = 10.0$, $\mathcal{H}(\mathbb{Q}_1 \mid \mathbb{P}) = 0.5$, and $\mathbb{E}^{\mathbb{Q}_2}[H] = 11.0$, $\mathcal{H}(\mathbb{Q}_2 \mid \mathbb{P}) = 2.0$, compute $p(H)$ under each measure. Which measure achieves the supremum? How does the answer change for $\gamma = 0.5$?

---

**Exercise 2.** The small-$\gamma$ expansion gives $p(H) \approx \mathbb{E}^{\mathbb{Q}^E}[H] + \frac{\gamma}{2}\operatorname{Var}^{\mathbb{Q}^E}(H - \hat{H})$. If $\mathbb{E}^{\mathbb{Q}^E}[H] = 8.00$ and the unhedgeable variance is $\operatorname{Var}^{\mathbb{Q}^E}(H - \hat{H}) = 4.0$, compute the indifference price for $\gamma = 0.5, 1.0, 2.0, 5.0$. Plot the price as a function of $\gamma$ and verify it is increasing. At what $\gamma$ does the risk premium exceed 10% of the base price?

---

**Exercise 3.** For exponential utility $U(x) = -e^{-\gamma x}$, the optimal hedge combines the Merton demand $(\mu - r)/(\gamma\sigma^2 S)$ with the hedging demand $(\rho\eta/\sigma)g_Y$. In the worked example ($\mu = 0.08$, $r = 0.03$, $\sigma = 0.20$, $\gamma = 1$, $S = 100$), compute the Merton component. For the hedging demand with $\rho = 0.7$, $\eta = 0.25$, and $g_Y = \Delta_Y = 0.55$, $Y = 100$, compute the total hedge position. What fraction of the total position is the speculative Merton demand versus the hedging demand?

---

**Exercise 4.** As $\gamma \to \infty$, the indifference price converges to the superreplication price $\sup_{\mathbb{Q}}\mathbb{E}^{\mathbb{Q}}[H]$. In a model with $\sigma \in [0.15, 0.30]$ and an ATM call with $S = K = 100$, $T = 0.5$, $r = 0.03$, compute the superreplication price $\text{BS}(\sigma = 0.30)$ and the minimal entropy price $\text{BS}(\sigma_{\text{mid}})$ where $\sigma_{\text{mid}}$ is some intermediate value. What is the gap between these two limiting prices?

---

**Exercise 5.** The buyer's indifference price $p^b$ and seller's indifference price $p^s$ satisfy $p^b \leq p^s$ in incomplete markets. For the basis risk example with $\rho = 0.7$, $\gamma_{\text{buyer}} = 2$, $\gamma_{\text{seller}} = 1$, and unhedgeable variance $= 4.0$, compute both prices using the approximation $p \approx \mathbb{E}^{\mathbb{Q}^E}[H] \pm \frac{\gamma}{2}\operatorname{Var}(H - \hat{H})$ (with $+$ for seller and $-$ for buyer). What is the bid-ask spread $p^s - p^b$? Under what conditions does the spread vanish?

---

**Exercise 6.** Compare three pricing approaches for a call on an illiquid asset $Y$ with the parameters from the worked example ($\rho = 0.7$, $\sigma_Y = 0.25$). Compute: (a) the Black-Scholes price (ignoring incompleteness); (b) the mean-variance hedging price $\mathbb{E}^{\mathbb{Q}^*}[H]$; (c) the exponential utility indifference price for $\gamma = 1$. Which price is highest, and why? If a risk manager must choose a single price for reserving, which approach is most appropriate?
