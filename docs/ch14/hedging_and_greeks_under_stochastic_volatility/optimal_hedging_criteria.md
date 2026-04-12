# Optimal Hedging Criteria


In incomplete markets, hedging strategies depend on the **optimality criterion** chosen. Different criteria lead to different hedges, reflecting trade-offs between risk, cost, and robustness.

---

## Mean–variance hedging


A classical approach minimizes expected squared hedging error:

$$
\min_{\pi} \; \mathbb{E}\big[(H - V_T^{\pi})^2\big]
$$


where $H$ is the payoff and $V_T^{\pi}$ the hedged portfolio value.

Pros:
- mathematically tractable,
- leads to explicit hedging strategies.

Cons:
- penalizes large and small errors equally,
- sensitive to model assumptions.

---

## Utility-based hedging


Alternatively, one may maximize expected utility:

$$
\max_{\pi} \; \mathbb{E}[U(V_T^{\pi})]
$$



This framework:
- incorporates risk aversion,
- links pricing and hedging,
- is economically coherent.

However, it is often computationally demanding.

---

## Robust hedging criteria


Robust approaches aim to:
- perform reasonably well across models,
- limit worst-case losses,
- avoid overfitting to a single calibration.

Examples include:
- min–max hedging,
- stress-based hedging rules,
- conservative Greeks.

---

## Practical considerations


In practice, desks choose criteria based on:
- product type (vanilla vs exotic),
- liquidity of hedging instruments,
- regulatory and capital constraints.

Often, hybrid or heuristic approaches are used.

---

## Key takeaways


- Optimal hedging depends on the chosen risk criterion.
- No single hedging strategy is universally optimal.
- Robustness is often more valuable than theoretical optimality.

---

## Further reading


- Föllmer & Schweizer, hedging in incomplete markets.
- Carmona, utility-based pricing and hedging.
- Taleb, practical perspectives on hedging robustness.

---

## Exercises

**Exercise 1.** The mean-variance optimal hedge minimizes

$$
\min_{\pi}\;\mathbb{E}\bigl[(H - V_T^{\pi})^2\bigr]
$$

For a payoff $H$ with $\mathbb{E}[H] = 10$ and $\text{Var}[H] = 25$, and a hedging portfolio that can replicate a fraction $R^2 = 0.80$ of the variance, compute the residual variance $\text{Var}[H - V_T^{\pi}] = (1 - R^2)\text{Var}[H]$. What is the standard deviation of the hedging error? In what units should this be compared to the option premium?

??? success "Solution to Exercise 1"
    The residual variance is

    $$
    \text{Var}[H - V_T^{\pi}] = (1 - R^2)\,\text{Var}[H] = (1 - 0.80) \times 25 = 5
    $$

    The standard deviation of the hedging error is

    $$
    \sigma_{\text{hedge error}} = \sqrt{5} \approx 2.236
    $$

    This means that even with an optimal hedge that captures 80% of the payoff variance, the residual hedging error has a standard deviation of approximately $2.24$.

    This should be compared to the option premium in the **same currency units**. If the premium is, say, $\Pi = 10$ (the expected payoff), then the hedging error standard deviation is about 22% of the premium. The ratio $\sigma_{\text{hedge error}} / \Pi$ gives the coefficient of variation of the hedging error relative to the price charged, which is a measure of how much risk the hedger retains per unit of premium earned. A high ratio indicates that the residual risk is large relative to the compensation received.

---

**Exercise 2.** Compare mean-variance hedging with utility-based hedging using exponential utility $U(x) = -e^{-\gamma x}$. For a risk-neutral agent ($\gamma \to 0$), both approaches coincide. For a risk-averse agent ($\gamma = 5$), the utility-based hedge is more conservative. Explain qualitatively how the utility-based hedge differs: does it tend to over-hedge or under-hedge compared to mean-variance? Why does risk aversion matter when the market is incomplete but not when it is complete?

??? success "Solution to Exercise 2"
    For a risk-neutral agent ($\gamma \to 0$), exponential utility becomes linear: $U(x) \approx -1 + \gamma x$. Maximizing $\mathbb{E}[U(V_T^\pi)]$ reduces to maximizing $\mathbb{E}[V_T^\pi]$, and the variance of the hedging error does not matter. In this limit, utility-based hedging coincides with mean-variance hedging (both seek the best expected outcome).

    For a risk-averse agent ($\gamma = 5$), the exponential utility $U(x) = -e^{-\gamma x}$ penalizes downside outcomes much more heavily than it rewards upside outcomes. The certainty equivalent of a random payoff $X$ is

    $$
    \text{CE} = -\frac{1}{\gamma}\ln\mathbb{E}[e^{-\gamma X}] \approx \mathbb{E}[X] - \frac{\gamma}{2}\text{Var}[X]
    $$

    for approximately normal $X$. The penalty $\frac{\gamma}{2}\text{Var}[X]$ grows with $\gamma$, so the risk-averse agent is willing to sacrifice expected return to reduce variance.

    The utility-based hedge tends to **over-hedge** compared to mean-variance: it takes larger hedging positions to reduce the probability of large losses, even if this increases expected hedging cost. In particular, the utility-based hedge may buy additional protective options (e.g., put protection or extra vega hedging) that the mean-variance hedge would not justify.

    In a complete market, risk aversion does not matter because perfect replication eliminates all risk — there is nothing to be averse to. The unique replicating strategy is optimal for every utility function. In an incomplete market, residual risk remains, and how the agent values that risk (via $\gamma$) directly affects the choice of hedge.

---

**Exercise 3.** Robust (min-max) hedging aims to minimize the worst-case loss:

$$
\min_{\pi}\;\max_{\mathbb{Q} \in \mathcal{Q}}\;\mathbb{E}^{\mathbb{Q}}\bigl[(H - V_T^{\pi})^2\bigr]
$$

where $\mathcal{Q}$ is a set of plausible models. Suppose $\mathcal{Q}$ consists of two Heston calibrations: one with $\rho = -0.5$ and one with $\rho = -0.8$. Explain why the robust hedge will be different from the hedge optimal under either model alone. What is the trade-off of using the robust approach?

??? success "Solution to Exercise 3"
    The robust hedge solves

    $$
    \min_{\pi}\;\max_{\mathbb{Q} \in \mathcal{Q}}\;\mathbb{E}^{\mathbb{Q}}\bigl[(H - V_T^{\pi})^2\bigr]
    $$

    With $\mathcal{Q} = \{\mathbb{Q}_1(\rho = -0.5),\;\mathbb{Q}_2(\rho = -0.8)\}$, the optimal hedge under $\mathbb{Q}_1$ alone differs from the optimal hedge under $\mathbb{Q}_2$ alone because the correlation parameter $\rho$ affects the joint dynamics of spot and volatility, and hence the hedge ratios (particularly vanna-related adjustments).

    Under $\rho = -0.5$, the leverage effect is moderate, so the hedge has smaller vanna corrections. Under $\rho = -0.8$, the leverage effect is strong, requiring larger adjustments for the correlation between spot and vol moves.

    The robust hedge must perform reasonably under **both** scenarios simultaneously. It chooses the strategy that minimizes the worst-case (maximum) expected squared error across the two models. This typically results in a hedge that is **intermediate** between the two model-specific optima — not optimal under either model, but acceptable under both.

    The trade-off is suboptimality versus robustness. If the true model is $\mathbb{Q}_1$, the robust hedge underperforms compared to the $\mathbb{Q}_1$-optimal hedge. The same holds for $\mathbb{Q}_2$. However, the robust hedge avoids the catastrophic performance that would occur if the wrong model-specific hedge were used. In practice, this insurance against model misspecification is often worth the cost.

---

**Exercise 4.** A trading desk hedges vanilla options using delta (from the underlying) and vega (from a single ATM option). List the residual risk factors that remain after delta-vega hedging under a Heston model. For each factor, suggest a practical instrument or approach that could reduce the exposure.

??? success "Solution to Exercise 4"
    After delta-vega hedging under the Heston model, the following residual risk factors remain:

    1. **Vanna risk** (cross-sensitivity $\partial^2 C / \partial S\,\partial\sigma$): The delta changes when volatility moves and vice versa. This is especially important when $\rho \neq 0$. *Instrument:* Risk reversals (long OTM call, short OTM put, or vice versa) have significant vanna exposure.

    2. **Volga risk** (sensitivity $\partial^2 C / \partial\sigma^2$): The vega itself changes when volatility moves, creating convexity in volatility. *Instrument:* Butterfly spreads or strangles, which have high volga, can be used to hedge this exposure.

    3. **Vol-of-vol risk** (sensitivity to $\xi$): The parameter governing the magnitude of variance fluctuations affects smile curvature. *Instrument:* Options on variance (e.g., VIX options) or variance swap options provide exposure to $\xi$.

    4. **Correlation risk** (sensitivity to $\rho$): Changes in the spot-vol correlation affect the skew of the implied volatility surface. *Instrument:* This is difficult to hedge directly; proxy hedges include skew-sensitive portfolios such as risk reversals with specific strike selection.

    5. **Term-structure risk**: The vega hedge uses a single ATM option at one maturity, but the portfolio may have exposure across multiple maturities. *Instrument:* Calendar spreads or options at different maturities can address maturity mismatch.

    6. **Theta/time decay mismatch**: The hedging option decays at a different rate than the hedged position. *Instrument:* Regular rebalancing of the vega hedge or using options with matching maturity profiles.

---

**Exercise 5.** Explain why transaction costs make the choice of hedging criterion more important in incomplete markets. In a complete market with zero transaction costs, there is a unique replicating strategy regardless of preferences. With stochastic volatility and proportional transaction costs $\epsilon$, the trader faces a three-way trade-off between hedging frequency, transaction costs, and residual risk. Describe how each criterion (mean-variance, utility-based, robust) balances this trade-off differently.

??? success "Solution to Exercise 5"
    With proportional transaction costs $\epsilon$ per unit traded, the trader faces a three-way trade-off:

    - **More frequent hedging** reduces tracking error (residual risk) but increases cumulative transaction costs.
    - **Less frequent hedging** saves on costs but allows larger deviations from the target hedge ratio.
    - **Incomplete markets** compound this because even continuous hedging leaves residual risk from the unhedged volatility factor.

    Each criterion balances this trade-off differently:

    **Mean-variance hedging** minimizes $\mathbb{E}[(H - V_T^\pi)^2]$ including costs. The optimal rebalancing frequency is determined by equating the marginal reduction in tracking-error variance with the marginal increase in expected transaction costs. This leads to a "bandwidth" approach: rebalance when the hedge ratio drifts beyond a threshold. The threshold depends on $\epsilon$, $\Gamma$, and the volatility of the hedge ratio. Mean-variance hedging treats all deviations symmetrically (upside and downside).

    **Utility-based hedging** with a concave utility function penalizes large losses more than it values large gains. A risk-averse agent rebalances more aggressively on the downside (when the portfolio is short gamma and exposed to losses) and less aggressively on the upside. This creates an asymmetric rebalancing rule. Transaction costs are tolerated more readily when the alternative is a large unhedged loss.

    **Robust hedging** assumes the worst-case model within a set $\mathcal{Q}$. Under the worst-case model, volatility may be higher or the correlation more adverse, leading to wider hedge-ratio fluctuations. The robust hedger tends to hedge more conservatively (wider positions, more frequent rebalancing) to protect against model uncertainty, accepting higher transaction costs as insurance. The rebalancing rule is designed for the worst-case scenario, not the expected scenario.

    In a complete market with zero transaction costs, all three criteria yield the same strategy (the unique replicating portfolio), making the choice irrelevant. Incompleteness and frictions together create meaningful distinctions between criteria.

---

**Exercise 6.** A fund manager prices a 1-year exotic option using the Heston model and chooses to delta-hedge without any volatility hedging. She earns the option premium $\Pi$ and expects to earn the volatility risk premium by being short volatility. Under what market conditions does this strategy generate large losses? Compute the worst-case scenario if realized vol is twice the implied vol: the approximate loss is $\frac{1}{2}\Gamma S^2(\sigma_r^2 - \sigma_i^2)T$, using $\Gamma = 0.015$, $S = 100$, $\sigma_i = 20\%$, $\sigma_r = 40\%$, $T = 1$.

??? success "Solution to Exercise 6"
    The strategy generates large losses when **realized volatility significantly exceeds implied volatility** — that is, when the volatility risk premium turns negative or when a volatility spike occurs (e.g., financial crisis, pandemic shock, geopolitical event).

    The approximate gamma P&L for a delta-hedged option position over the holding period is

    $$
    \text{Gamma P\&L} \approx \frac{1}{2}\,\Gamma\,S^2\,(\sigma_r^2 - \sigma_i^2)\,T
    $$

    Since the fund manager is short the option and delta-hedging, she loses money when realized vol exceeds implied vol. Substituting the given values:

    $$
    \text{Loss} = \frac{1}{2} \times 0.015 \times 100^2 \times (0.40^2 - 0.20^2) \times 1
    $$

    $$
    = \frac{1}{2} \times 0.015 \times 10{,}000 \times (0.16 - 0.04) \times 1
    $$

    $$
    = \frac{1}{2} \times 0.015 \times 10{,}000 \times 0.12
    $$

    $$
    = \frac{1}{2} \times 18 = 9.0
    $$

    The approximate loss is $\$9.0$ per option. If the option premium $\Pi$ collected is smaller than $9.0$, the strategy is net negative. For context, the Black-Scholes price of an ATM call with $\sigma = 0.20$, $S = 100$, $T = 1$, $r = 0.03$ is approximately $\$8.9$. So a doubling of realized vol would wipe out essentially the entire premium.

    The conditions for large losses include: sudden volatility regime changes, sustained high realized vol without a corresponding increase in implied vol (if the position is marked to market using implied vol), and jump events that cause realized vol to spike far above the level priced into the option.
