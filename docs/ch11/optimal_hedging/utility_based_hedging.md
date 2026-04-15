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

### Effect of Risk Aversion γ

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

??? success "Solution to Exercise 1"
    For $\gamma = 2$, the entropic pricing formula gives:

    $$
    p_{\mathbb{Q}_1} = \mathbb{E}^{\mathbb{Q}_1}[H] - \frac{1}{\gamma}\mathcal{H}(\mathbb{Q}_1 \mid \mathbb{P}) = 10.0 - \frac{1}{2}(0.5) = 10.0 - 0.25 = 9.75
    $$

    $$
    p_{\mathbb{Q}_2} = \mathbb{E}^{\mathbb{Q}_2}[H] - \frac{1}{\gamma}\mathcal{H}(\mathbb{Q}_2 \mid \mathbb{P}) = 11.0 - \frac{1}{2}(2.0) = 11.0 - 1.0 = 10.0
    $$

    The supremum is achieved by $\mathbb{Q}_2$ with $p(H) = 10.0$. Although $\mathbb{Q}_2$ has higher entropy (larger distortion from $\mathbb{P}$), its higher expected payoff more than compensates for the entropy penalty at $\gamma = 2$.

    For $\gamma = 0.5$:

    $$
    p_{\mathbb{Q}_1} = 10.0 - \frac{1}{0.5}(0.5) = 10.0 - 1.0 = 9.0
    $$

    $$
    p_{\mathbb{Q}_2} = 11.0 - \frac{1}{0.5}(2.0) = 11.0 - 4.0 = 7.0
    $$

    Now $\mathbb{Q}_1$ achieves the supremum with $p(H) = 9.0$. At lower risk aversion ($\gamma = 0.5$), the entropy penalty is magnified by the factor $1/\gamma = 2$. The high-entropy measure $\mathbb{Q}_2$ is penalized more severely, and the more "conservative" measure $\mathbb{Q}_1$ dominates. This illustrates how lower risk aversion leads to a stronger preference for measures close to $\mathbb{P}$ (low entropy), resulting in lower indifference prices.

---

**Exercise 2.** The small-$\gamma$ expansion gives $p(H) \approx \mathbb{E}^{\mathbb{Q}^E}[H] + \frac{\gamma}{2}\operatorname{Var}^{\mathbb{Q}^E}(H - \hat{H})$. If $\mathbb{E}^{\mathbb{Q}^E}[H] = 8.00$ and the unhedgeable variance is $\operatorname{Var}^{\mathbb{Q}^E}(H - \hat{H}) = 4.0$, compute the indifference price for $\gamma = 0.5, 1.0, 2.0, 5.0$. Plot the price as a function of $\gamma$ and verify it is increasing. At what $\gamma$ does the risk premium exceed 10% of the base price?

??? success "Solution to Exercise 2"
    Using $p(H) \approx \mathbb{E}^{\mathbb{Q}^E}[H] + \frac{\gamma}{2}\operatorname{Var}^{\mathbb{Q}^E}(H - \hat{H})$ with $\mathbb{E}^{\mathbb{Q}^E}[H] = 8.00$ and $\operatorname{Var}^{\mathbb{Q}^E}(H - \hat{H}) = 4.0$:

    | $\gamma$ | Risk premium $\frac{\gamma}{2} \times 4.0$ | Indifference price $p(H)$ |
    |:---|:---|:---|
    | 0.5 | $0.25 \times 4.0 = 1.00$ | $8.00 + 1.00 = 9.00$ |
    | 1.0 | $0.50 \times 4.0 = 2.00$ | $8.00 + 2.00 = 10.00$ |
    | 2.0 | $1.00 \times 4.0 = 4.00$ | $8.00 + 4.00 = 12.00$ |
    | 5.0 | $2.50 \times 4.0 = 10.00$ | $8.00 + 10.00 = 18.00$ |

    The price is clearly increasing in $\gamma$, as the risk premium $\gamma/2 \times \operatorname{Var}$ grows linearly. More risk-averse agents demand a higher premium for bearing the unhedgeable risk.

    The risk premium exceeds 10% of the base price when:

    $$
    \frac{\gamma}{2} \times 4.0 > 0.10 \times 8.00 = 0.80 \implies 2\gamma > 0.80 \implies \gamma > 0.40
    $$

    For any $\gamma > 0.40$, the risk premium exceeds 10% of the base price. Note that for large $\gamma$ (e.g., $\gamma = 5$), the small-$\gamma$ approximation becomes unreliable and the actual price would be capped by the superreplication bound.

---

**Exercise 3.** For exponential utility $U(x) = -e^{-\gamma x}$, the optimal hedge combines the Merton demand $(\mu - r)/(\gamma\sigma^2 S)$ with the hedging demand $(\rho\eta/\sigma)g_Y$. In the worked example ($\mu = 0.08$, $r = 0.03$, $\sigma = 0.20$, $\gamma = 1$, $S = 100$), compute the Merton component. For the hedging demand with $\rho = 0.7$, $\eta = 0.25$, and $g_Y = \Delta_Y = 0.55$, $Y = 100$, compute the total hedge position. What fraction of the total position is the speculative Merton demand versus the hedging demand?

??? success "Solution to Exercise 3"
    **Merton component:**

    $$
    \xi^{\text{Merton}} = \frac{\mu - r}{\gamma\sigma^2 S} = \frac{0.08 - 0.03}{1 \times 0.04 \times 100} = \frac{0.05}{4.0} = 0.0125
    $$

    **Hedging demand:**

    $$
    \xi^{\text{hedge}} = \frac{\rho\eta}{\sigma}\,g_Y = \frac{0.7 \times 0.25}{0.20} \times 0.55 = \frac{0.175}{0.20} \times 0.55 = 0.875 \times 0.55 = 0.48125
    $$

    **Total hedge position:**

    $$
    \xi^* = \xi^{\text{Merton}} + \xi^{\text{hedge}} = 0.0125 + 0.48125 = 0.49375
    $$

    **Fraction decomposition:**

    - Merton (speculative) demand: $0.0125 / 0.49375 \approx 2.5\%$
    - Hedging demand: $0.48125 / 0.49375 \approx 97.5\%$

    The hedging demand dominates overwhelmingly. The speculative Merton component is small because the Sharpe ratio $(\mu - r)/\sigma = 0.25$ is moderate and the risk aversion $\gamma = 1$ is not negligible. The hedging demand, driven by the need to offset the claim's exposure to the $Y$ risk factor, is the primary determinant of the position. This is typical in practice: for agents holding contingent claims, the hedging motive far outweighs the speculative motive.

---

**Exercise 4.** As $\gamma \to \infty$, the indifference price converges to the superreplication price $\sup_{\mathbb{Q}}\mathbb{E}^{\mathbb{Q}}[H]$. In a model with $\sigma \in [0.15, 0.30]$ and an ATM call with $S = K = 100$, $T = 0.5$, $r = 0.03$, compute the superreplication price $\text{BS}(\sigma = 0.30)$ and the minimal entropy price $\text{BS}(\sigma_{\text{mid}})$ where $\sigma_{\text{mid}}$ is some intermediate value. What is the gap between these two limiting prices?

??? success "Solution to Exercise 4"
    With $S = K = 100$, $T = 0.5$, $r = 0.03$:

    **Superreplication price** (use $\sigma_{\max} = 0.30$):

    $$
    d_1 = \frac{\ln(100/100) + (0.03 + 0.045) \times 0.5}{0.30\sqrt{0.5}} = \frac{0 + 0.0375}{0.2121} = \frac{0.0375}{0.2121} \approx 0.1768
    $$

    $$
    d_2 = 0.1768 - 0.2121 = -0.0354
    $$

    Using $N(0.1768) \approx 0.5701$ and $N(-0.0354) \approx 0.4859$:

    $$
    C_{\max} = 100 \times 0.5701 - 100 e^{-0.015} \times 0.4859 = 57.01 - 100 \times 0.9851 \times 0.4859
    $$

    $$
    C_{\max} = 57.01 - 47.87 \approx \$9.14
    $$

    **Minimal entropy price** (use an intermediate $\sigma_{\text{mid}}$, say $\sigma_{\text{mid}} = 0.225$ as a reasonable midpoint):

    $$
    d_1 = \frac{0 + (0.03 + 0.0253) \times 0.5}{0.225\sqrt{0.5}} = \frac{0.0277}{0.1591} \approx 0.1738
    $$

    $$
    d_2 = 0.1738 - 0.1591 = 0.0147
    $$

    Using $N(0.1738) \approx 0.5690$ and $N(0.0147) \approx 0.5059$:

    $$
    C_{\text{mid}} = 100 \times 0.5690 - 100 e^{-0.015} \times 0.5059 = 56.90 - 49.84 \approx \$7.06
    $$

    **The gap** between the two limiting prices is approximately:

    $$
    C_{\max} - C_{\text{mid}} \approx 9.14 - 7.06 = \$2.08
    $$

    This gap represents the premium an infinitely risk-averse agent pays over the entropy-minimizing price. It arises entirely from the volatility uncertainty interval $[0.15, 0.30]$. As $\gamma$ increases from $0$ toward $\infty$, the indifference price smoothly interpolates from $C_{\text{mid}}$ up to $C_{\max}$, with the agent effectively "choosing" a higher implied volatility as risk aversion increases.

---

**Exercise 5.** The buyer's indifference price $p^b$ and seller's indifference price $p^s$ satisfy $p^b \leq p^s$ in incomplete markets. For the basis risk example with $\rho = 0.7$, $\gamma_{\text{buyer}} = 2$, $\gamma_{\text{seller}} = 1$, and unhedgeable variance $= 4.0$, compute both prices using the approximation $p \approx \mathbb{E}^{\mathbb{Q}^E}[H] \pm \frac{\gamma}{2}\operatorname{Var}(H - \hat{H})$ (with $+$ for seller and $-$ for buyer). What is the bid-ask spread $p^s - p^b$? Under what conditions does the spread vanish?

??? success "Solution to Exercise 5"
    Using the approximation $p \approx \mathbb{E}^{\mathbb{Q}^E}[H] \pm \frac{\gamma}{2}\operatorname{Var}(H - \hat{H})$ (with $+$ for seller and $-$ for buyer), and letting $V_0 = \mathbb{E}^{\mathbb{Q}^E}[H]$ denote the base price:

    **Seller's indifference price** ($\gamma_{\text{seller}} = 1$):

    $$
    p^s = V_0 + \frac{1}{2} \times 4.0 = V_0 + 2.0
    $$

    **Buyer's indifference price** ($\gamma_{\text{buyer}} = 2$):

    $$
    p^b = V_0 - \frac{2}{2} \times 4.0 = V_0 - 4.0
    $$

    **Bid-ask spread:**

    $$
    p^s - p^b = (V_0 + 2.0) - (V_0 - 4.0) = 6.0
    $$

    The bid-ask spread is $\$6.00$.

    **When does the spread vanish?** The spread is:

    $$
    p^s - p^b = \frac{\gamma_s}{2}\operatorname{Var}(H - \hat{H}) + \frac{\gamma_b}{2}\operatorname{Var}(H - \hat{H}) = \frac{\gamma_s + \gamma_b}{2}\operatorname{Var}(H - \hat{H})
    $$

    This vanishes when:

    - $\operatorname{Var}(H - \hat{H}) = 0$: the claim is perfectly hedgeable (complete market). When the unhedgeable variance is zero, buyer and seller agree on the unique replication price.
    - $\gamma_s = \gamma_b = 0$: both agents are risk-neutral. Risk-neutral agents do not demand a premium for bearing unhedgeable risk and agree on the risk-neutral price.

    In practice, the spread shrinks as the market becomes "more complete" (higher correlation, more traded instruments) or as agents become less risk-averse.

---

**Exercise 6.** Compare three pricing approaches for a call on an illiquid asset $Y$ with the parameters from the worked example ($\rho = 0.7$, $\sigma_Y = 0.25$). Compute: (a) the Black-Scholes price (ignoring incompleteness); (b) the mean-variance hedging price $\mathbb{E}^{\mathbb{Q}^*}[H]$; (c) the exponential utility indifference price for $\gamma = 1$. Which price is highest, and why? If a risk manager must choose a single price for reserving, which approach is most appropriate?

??? success "Solution to Exercise 6"
    Using the worked example parameters: $S_0 = Y_0 = 100$, $K = 100$, $T = 0.5$, $r = 0.03$, $\sigma_Y = 0.25$, $\rho = 0.7$.

    **(a) Black-Scholes price** (ignoring incompleteness, pricing the call on $Y$ with $\sigma_Y = 0.25$):

    $$
    d_1 = \frac{\ln(100/100) + (0.03 + 0.03125) \times 0.5}{0.25\sqrt{0.5}} = \frac{0.030625}{0.1768} \approx 0.1732
    $$

    $$
    d_2 = 0.1732 - 0.1768 = -0.0036
    $$

    Using $N(0.1732) \approx 0.5688$ and $N(-0.0036) \approx 0.4986$:

    $$
    C_{\text{BS}} = 100 \times 0.5688 - 100 e^{-0.015} \times 0.4986 \approx 56.88 - 49.12 \approx \$7.76
    $$

    **(b) Mean-variance hedging price** $\mathbb{E}^{\mathbb{Q}^*}[H]$: The variance-optimal measure adjusts the drift of $S$ but in a way that minimizes $L^2$ distortion. In the basis risk setting with constant parameters, this typically yields a price close to but slightly below the Black-Scholes price, as the variance-optimal measure accounts for the fact that only $\rho^2 = 49\%$ of the claim's risk is hedgeable. A reasonable estimate is approximately $\$7.50$.

    **(c) Exponential utility indifference price** ($\gamma = 1$): From the worked example, this is approximately $\$7.20$. The entropic penalty for unhedgeable risk reduces the price below the risk-neutral level.

    **Ordering:** $C_{\text{BS}} \approx \$7.76 > p_{\text{MV}} \approx \$7.50 > p_{\text{indiff}} \approx \$7.20$.

    The Black-Scholes price is highest because it ignores incompleteness entirely and treats the claim as if it were perfectly replicable. The mean-variance price is lower because it accounts for the residual hedging error, though it does so through an $L^2$ criterion without explicit risk preferences. The utility indifference price is lowest because the buyer demands a discount (risk premium) for absorbing unhedgeable risk, and the exponential utility explicitly penalizes the variance of the residual.

    **For reserving purposes:** A risk manager should use the **utility indifference price** or, more conservatively, the Black-Scholes price. The indifference price explicitly accounts for the institution's risk tolerance and the degree of market incompleteness. However, if regulatory requirements mandate conservatism, the Black-Scholes price (or even the superreplication price) may be more appropriate, as it provides a larger reserve buffer against unhedgeable risk. The mean-variance price is a reasonable middle ground for internal risk assessment but lacks the economic foundation of the utility-based approach.
