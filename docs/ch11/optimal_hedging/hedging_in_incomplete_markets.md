# Hedging in Incomplete Markets

When markets are incomplete --- due to unhedgeable risk factors, transaction costs, or trading constraints --- perfect replication is impossible. This section surveys the principal approaches to hedging under incompleteness: **superreplication** (eliminate all risk at maximum cost), **quantile hedging** (replicate with high probability), and **shortfall risk minimization** (control the severity of hedging failures). These methods span a spectrum from conservative to risk-tolerant, each offering a different resolution of the price-risk tradeoff.

---

## Sources of Market Incompleteness

Before developing the hedging strategies, it is useful to catalog the common sources of incompleteness:

| Source | Example | Unhedgeable risk |
|:---|:---|:---|
| Untraded risk factors | Stochastic volatility, jump intensity | Volatility, jump risk |
| Basis risk | Hedging oil with gasoline futures | Residual correlation gap |
| Transaction costs | Bid-ask spreads, market impact | Rebalancing friction |
| Trading constraints | Short-selling restrictions, margin | Constrained strategies |
| Discrete trading | Finite rebalancing dates | Discretization error |

Each source creates a gap between the set of attainable payoffs and the full space $L^2$, leading to non-unique prices and imperfect hedges.

---

## Superreplication

### Definition and Theorem

Superreplication is the most conservative approach: find the cheapest self-financing strategy that dominates the claim in every scenario.

!!! abstract "Definition: Superreplication Price"
    The **superreplication price** of a claim $H$ is:

    $$
    \boxed{\pi^{\sup}(H) = \inf\!\left\{c \in \mathbb{R} : \exists\, \xi \in \Theta \text{ such that } c + G_T(\xi) \geq H \;\; \mathbb{P}\text{-a.s.}\right\}}
    $$

**Theorem (Superreplication Duality).** *Under standard no-arbitrage conditions:*

$$
\pi^{\sup}(H) = \sup_{\mathbb{Q} \in \mathcal{M}} \mathbb{E}^{\mathbb{Q}}[\tilde{H}]
$$

*where $\mathcal{M}$ is the set of equivalent martingale measures and $\tilde{H} = e^{-rT}H$ is the discounted claim.*

??? note "Proof Sketch"
    The inequality $\pi^{\sup} \geq \sup_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[\tilde{H}]$ follows because any superreplicating strategy satisfies $c + G_T(\xi) \geq H$, so $c \geq \mathbb{E}^{\mathbb{Q}}[\tilde{H}]$ for every $\mathbb{Q} \in \mathcal{M}$ (since $\mathbb{E}^{\mathbb{Q}}[G_T(\xi)] = 0$ under any martingale measure). The reverse inequality uses Hahn-Banach separation: if $c < \sup_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[\tilde{H}]$, then no superreplicating strategy exists at cost $c$, which can be shown by constructing a separating martingale measure. $\square$

### The Superreplication Problem

In practice, the superreplication price is often **too expensive**. For example, in a stochastic volatility model:

- A European call's superreplication price equals the price under the volatility that maximizes the option value (the worst-case vol).
- If $\sigma \in [\sigma_{\min}, \sigma_{\max}]$, the superreplication price of a call is $\text{BS}(S, K, T, \sigma_{\max})$.

This can be significantly higher than any reasonable market price, making superreplication impractical for most applications.

!!! warning "Cost of Safety"
    Superreplication eliminates all risk but at the cost of a potentially large premium above the "fair" price. For claims with high sensitivity to unhedgeable factors, the superreplication price may exceed the claim's intrinsic value, making it economically unviable.

---

## Quantile Hedging

### Motivation

Instead of replicating in all scenarios, **quantile hedging** (Follmer and Leukert, 1999) seeks the cheapest strategy that replicates with a specified probability $1 - \varepsilon$.

### Formal Problem

!!! abstract "Definition: Quantile Hedging"
    Given a budget $c < \pi^{\sup}(H)$ and a confidence level $1 - \varepsilon$, the **quantile hedging problem** is:

    $$
    \boxed{\max_{\xi \in \Theta} \mathbb{P}\!\left(c + G_T(\xi) \geq H\right) \quad \text{subject to initial cost } c}
    $$

    Equivalently: find the cheapest strategy that succeeds with probability at least $1 - \varepsilon$:

    $$
    \min_{c, \xi} c \quad \text{subject to } \mathbb{P}(c + G_T(\xi) \geq H) \geq 1 - \varepsilon
    $$

### Solution Structure

**Theorem (Follmer-Leukert).** *The quantile hedging problem reduces to superreplicating a modified claim $H \cdot \mathbf{1}_A$ where $A \subset \Omega$ is a suitably chosen "success set":*

$$
\pi_\varepsilon(H) = \pi^{\sup}(H \cdot \mathbf{1}_{A^*})
$$

*The optimal success set $A^*$ is determined by the Neyman-Pearson lemma applied to the likelihood ratios $d\mathbb{Q}^*/d\mathbb{P}$ of the least favorable martingale measure.*

### Interpretation

Quantile hedging sacrifices replication on a set of "bad" scenarios with total probability $\varepsilon$. On the success set $A^*$, the hedge perfectly replicates the claim. On the failure set $A^{*c}$, the hedge may produce a loss.

The Neyman-Pearson structure implies that the scenarios sacrificed are those where the cost of hedging is highest relative to their probability --- the hedge "gives up" on the most expensive-to-hedge paths first.

### Example

Consider a European call in a stochastic volatility model with budget equal to 90% of the superreplication price. Quantile hedging:

- Perfectly replicates the call on paths where volatility stays moderate.
- Fails to replicate on paths where volatility reaches extreme levels (the most expensive scenarios).
- Achieves, say, $\mathbb{P}(\text{success}) = 0.97$ --- the hedge works in 97% of scenarios.

---

## Shortfall Risk Minimization

### Beyond Success Probability

Quantile hedging controls the **probability** of failure but ignores the **severity** of failure. A strategy that fails with probability 3% but loses \$1 million when it fails is very different from one that fails with probability 3% but loses only \$100.

**Shortfall risk minimization** addresses this by incorporating a **loss function** that penalizes the magnitude of the shortfall.

### Formal Problem

!!! abstract "Definition: Shortfall Risk Minimization"
    Given a loss function $\ell : [0, \infty) \to [0, \infty)$ (convex, increasing, $\ell(0) = 0$), the **shortfall risk** of a strategy $(c, \xi)$ is:

    $$
    \mathcal{R}(c, \xi) = \mathbb{E}\!\left[\ell\!\left((H - c - G_T(\xi))^+\right)\right]
    $$

    The shortfall risk minimization problem is:

    $$
    \boxed{\min_{\xi \in \Theta} \mathbb{E}\!\left[\ell\!\left((H - c - G_T(\xi))^+\right)\right] \quad \text{for given initial capital } c}
    $$

### Common Loss Functions

| Loss function | $\ell(x)$ | Interpretation |
|:---|:---|:---|
| Indicator | $\mathbf{1}_{\{x > 0\}}$ | Quantile hedging (probability of loss) |
| Linear | $x$ | Expected shortfall |
| Quadratic | $x^2$ | Mean-squared shortfall |
| Power | $x^p$, $p > 1$ | Penalizes large shortfalls more heavily |

### Solution Structure

**Theorem (Follmer-Leukert, 2000).** *For convex loss functions, the optimal shortfall-minimizing strategy superreplicates a modified claim:*

$$
H^* = H \cdot \varphi^*(d\mathbb{Q}^*/d\mathbb{P})
$$

*where $\varphi^* \in [0, 1]$ is a "randomized test" determined by the Neyman-Pearson lemma applied to the modified problem. The function $\varphi^*$ assigns weights to scenarios based on the likelihood ratio and the loss function.*

For the linear loss $\ell(x) = x$ (expected shortfall):

$$
\min_\xi \mathbb{E}\!\left[(H - c - G_T(\xi))^+\right]
$$

The optimal strategy minimizes the expected amount by which the hedge falls short. This is a natural criterion for risk management, as it directly controls the average loss in failure scenarios.

---

## Comparison of Approaches

### The Hedging Spectrum

The various approaches can be ordered by their conservatism:

$$
\text{Superreplication} \;\geq\; \text{Quantile hedging} \;\geq\; \text{Shortfall minimization} \;\geq\; \text{Mean-variance} \;\geq\; \text{No hedging}
$$

| Approach | Cost | Risk tolerance | Loss control |
|:---|:---|:---|:---|
| **Superreplication** | Highest | None (zero risk) | Perfect |
| **Quantile hedging** | High | Small probability of total failure | Probability only |
| **Expected shortfall min** | Moderate | Accepts some loss | Average loss |
| **Mean-variance** | Moderate | Symmetric $L^2$ loss | Variance |
| **Utility-based** | Depends on $\gamma$ | Preference-based | Utility-weighted |

### Price Ordering

For a given claim $H$:

$$
\pi^{\sup}(H) \geq \pi_\varepsilon(H) \geq p_{\text{indiff}}(H) \geq \inf_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[\tilde{H}]
$$

The superreplication price is the upper bound; the infimum over martingale measures is the lower bound. All other prices lie in between, depending on the risk criterion.

---

## Practical Considerations

### Choosing an Approach

The choice depends on the context:

- **Regulatory capital**: Superreplication or quantile hedging at high confidence ($\varepsilon = 0.01$) may be required.
- **Trading desk P&L**: Mean-variance or shortfall minimization balances cost and risk.
- **Insurance/pension**: Utility-based approaches with appropriate risk aversion.
- **Market making**: Delta hedging with transaction cost optimization (practical rebalancing).

### Computational Methods

| Approach | Computation | Difficulty |
|:---|:---|:---|
| Superreplication | Solve worst-case PDE or linear program | Moderate |
| Quantile hedging | Neyman-Pearson + superreplication of modified claim | Hard |
| Shortfall minimization | Modified Neyman-Pearson + optimal transport | Hard |
| Mean-variance | Regression / backward induction | Moderate |
| Utility-based | HJB PDE or Monte Carlo | Moderate to hard |

---

## Worked Example: Stochastic Volatility

Consider a European call ($K = 100$, $T = 1$) under a model where volatility can take values $\sigma \in [0.15, 0.35]$.

**Prices under different criteria** (with $S_0 = 100$, $r = 0.03$):

| Approach | Price | Comment |
|:---|:---|:---|
| Superreplication | \$14.80 | $\text{BS}(\sigma = 0.35)$ |
| Sub-replication | \$6.20 | $\text{BS}(\sigma = 0.15)$ |
| Quantile hedge ($\varepsilon = 0.05$) | \$12.50 | Gives up 5% worst paths |
| Expected shortfall min | \$11.00 | Controls average loss |
| Mean-variance | \$10.30 | Under variance-optimal $\mathbb{Q}^*$ |
| Utility indifference ($\gamma = 1$) | \$10.80 | Exponential utility |

The \$8.60 gap between superreplication and sub-replication reflects the degree of incompleteness. All hedging approaches produce prices within this interval, with more conservative approaches closer to the upper bound.

**Hedging strategies:**

- **Superreplication**: Hedge with $\Delta(\sigma_{\max}) = \Delta(0.35)$, always over-hedging.
- **Mean-variance**: Hedge with $\Delta(\hat{\sigma})$ where $\hat{\sigma}$ is an intermediate volatility, accepting residual risk.
- **Quantile hedging**: Hedge with the superreplicating delta on "normal" paths; no hedge on extreme paths.

---

## The Risk-Cost Frontier

The fundamental message of hedging in incomplete markets is that there exists a **risk-cost frontier**: one cannot simultaneously minimize both cost and risk. Each approach represents a different point on this frontier:

- Moving toward zero risk (superreplication) increases cost.
- Reducing cost below the superreplication price necessarily introduces some form of residual risk.
- The optimal point depends on the agent's risk tolerance, regulatory requirements, and market conditions.

The various approaches studied --- mean-variance, local risk minimization, utility-based, quantile, and shortfall --- provide a rich toolkit for navigating this frontier.

---

## Summary

| Approach | Criterion | Key result |
|:---|:---|:---|
| Superreplication | $c + G_T(\xi) \geq H$ a.s. | $\pi^{\sup} = \sup_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[\tilde{H}]$ |
| Quantile hedging | $\max \mathbb{P}(\text{success})$ for given budget | Neyman-Pearson on modified claim |
| Shortfall risk min | $\min \mathbb{E}[\ell((H - c - G_T)^+)]$ | Generalized Neyman-Pearson |
| Mean-variance | $\min \mathbb{E}[(H - c - G_T)^2]$ | $L^2$ projection / FS decomposition |
| Utility-based | $\max \mathbb{E}[U(W_T)]$ | Entropy / HJB duality |
| Price ordering | $\pi^{\sup} \geq \pi_\varepsilon \geq p_{\text{indiff}} \geq \inf \mathbb{E}^{\mathbb{Q}}[\tilde{H}]$ | |
| Key insight | Incompleteness creates a risk-cost frontier; no approach eliminates the tradeoff | |

---

## Exercises

**Exercise 1.** The superreplication price of a European call under volatility uncertainty $\sigma \in [0.15, 0.35]$ is $\text{BS}(S, K, T, \sigma_{\max})$. For $S = K = 100$, $T = 1$, $r = 0.03$, compute the superreplication price and the sub-replication price $\text{BS}(\sigma_{\min})$. What is the width of the no-arbitrage price interval? Express this width as a fraction of the midpoint price.

---

**Exercise 2.** Quantile hedging with budget $c = 0.90 \times \pi^{\sup}(H)$ replicates the claim on a success set $A^*$ chosen by Neyman-Pearson. If the superreplication price from Exercise 1 is $\pi^{\sup}$, compute the budget $c$. The claim fails to replicate on paths where realized volatility exceeds some threshold $\sigma^*$. Assuming that $\mathbb{P}(\sigma > \sigma^*)$ can be made as small as 5%, explain qualitatively which paths are "sacrificed" and why the Neyman-Pearson structure selects the most expensive-to-hedge scenarios first.

---

**Exercise 3.** The shortfall risk with linear loss is $\mathcal{R}(c, \xi) = \mathbb{E}[(H - c - G_T(\xi))^+]$. For a simple two-state model where the hedge falls short by $\$5$ with probability 0.10 and short by $\$0$ otherwise, compute the expected shortfall. Compare this to a strategy that falls short by $\$2$ with probability 0.20. Which strategy has lower shortfall risk? Which has lower failure probability (quantile hedging criterion)?

---

**Exercise 4.** The price ordering states $\pi^{\sup}(H) \geq \pi_\varepsilon(H) \geq p_{\text{indiff}}(H) \geq \inf_{\mathbb{Q}}\mathbb{E}^{\mathbb{Q}}[\tilde{H}]$. Using the worked example values ($\pi^{\sup} = \$14.80$, $\pi_\varepsilon = \$12.50$, $p_{\text{MV}} = \$10.30$, sub-rep $= \$6.20$), verify the ordering. Compute the "conservatism premium" $\pi^{\sup} - p_{\text{MV}}$ and express it as a percentage of $p_{\text{MV}}$. For what type of institution would the superreplication price be appropriate?

---

**Exercise 5.** A trader sells a European call for $\$11.00$ (the expected shortfall minimization price from the worked example) and delta-hedges using mean-variance optimal deltas. Under the worst-case volatility scenario ($\sigma = 0.35$), the Black-Scholes price is $\$14.80$. Compute the maximum shortfall $\$14.80 - \$11.00$. Under the best-case scenario ($\sigma = 0.15$), the price is $\$6.20$. Compute the best-case profit. What is the expected P&L if the trader believes $\sigma$ is uniformly distributed on $[0.15, 0.35]$?

---

**Exercise 6.** The risk-cost frontier illustrates the fundamental tradeoff in incomplete markets. For the stochastic volatility example, plot the following five points on a risk-cost diagram: (a) superreplication: cost $= \$14.80$, residual risk $= 0$; (b) quantile hedging: cost $= \$12.50$, failure probability $= 5\%$; (c) expected shortfall min: cost $= \$11.00$; (d) mean-variance: cost $= \$10.30$, residual std $\approx \$2.50$; (e) sub-replication: cost $= \$6.20$, maximum risk. Is the frontier convex or concave? Explain why no strategy can achieve simultaneously lower cost and lower risk than any point on the frontier.
