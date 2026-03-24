# Optimal Hedging Criteria


In incomplete markets, hedging strategies depend on the **optimality criterion** chosen. Different criteria lead to different hedges, reflecting trade-offs between risk, cost, and robustness.

---

## Mean–variance hedging


A classical approach minimizes expected squared hedging error:

\[
\min_{\pi} \; \mathbb{E}\big[(H - V_T^{\pi})^2\big],
\]


where \(H\) is the payoff and \(V_T^{\pi}\) the hedged portfolio value.

Pros:
- mathematically tractable,
- leads to explicit hedging strategies.

Cons:
- penalizes large and small errors equally,
- sensitive to model assumptions.

---

## Utility-based hedging


Alternatively, one may maximize expected utility:

\[
\max_{\pi} \; \mathbb{E}[U(V_T^{\pi})].
\]



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

---

**Exercise 2.** Compare mean-variance hedging with utility-based hedging using exponential utility $U(x) = -e^{-\gamma x}$. For a risk-neutral agent ($\gamma \to 0$), both approaches coincide. For a risk-averse agent ($\gamma = 5$), the utility-based hedge is more conservative. Explain qualitatively how the utility-based hedge differs: does it tend to over-hedge or under-hedge compared to mean-variance? Why does risk aversion matter when the market is incomplete but not when it is complete?

---

**Exercise 3.** Robust (min-max) hedging aims to minimize the worst-case loss:

$$
\min_{\pi}\;\max_{\mathbb{Q} \in \mathcal{Q}}\;\mathbb{E}^{\mathbb{Q}}\bigl[(H - V_T^{\pi})^2\bigr]
$$

where $\mathcal{Q}$ is a set of plausible models. Suppose $\mathcal{Q}$ consists of two Heston calibrations: one with $\rho = -0.5$ and one with $\rho = -0.8$. Explain why the robust hedge will be different from the hedge optimal under either model alone. What is the trade-off of using the robust approach?

---

**Exercise 4.** A trading desk hedges vanilla options using delta (from the underlying) and vega (from a single ATM option). List the residual risk factors that remain after delta-vega hedging under a Heston model. For each factor, suggest a practical instrument or approach that could reduce the exposure.

---

**Exercise 5.** Explain why transaction costs make the choice of hedging criterion more important in incomplete markets. In a complete market with zero transaction costs, there is a unique replicating strategy regardless of preferences. With stochastic volatility and proportional transaction costs $\epsilon$, the trader faces a three-way trade-off between hedging frequency, transaction costs, and residual risk. Describe how each criterion (mean-variance, utility-based, robust) balances this trade-off differently.

---

**Exercise 6.** A fund manager prices a 1-year exotic option using the Heston model and chooses to delta-hedge without any volatility hedging. She earns the option premium $\Pi$ and expects to earn the volatility risk premium by being short volatility. Under what market conditions does this strategy generate large losses? Compute the worst-case scenario if realized vol is twice the implied vol: the approximate loss is $\frac{1}{2}\Gamma S^2(\sigma_r^2 - \sigma_i^2)T$, using $\Gamma = 0.015$, $S = 100$, $\sigma_i = 20\%$, $\sigma_r = 40\%$, $T = 1$.
