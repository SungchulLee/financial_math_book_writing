# Optimal Hedging Criteria

In incomplete markets, hedging strategies depend on the **optimality criterion** chosen. Different criteria lead to different hedges, reflecting trade-offs between risk, cost, and robustness.

---

## 1. Mean–variance hedging

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

## 2. Utility-based hedging

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

## 3. Robust hedging criteria

Robust approaches aim to:
- perform reasonably well across models,
- limit worst-case losses,
- avoid overfitting to a single calibration.

Examples include:
- min–max hedging,
- stress-based hedging rules,
- conservative Greeks.

---

## 4. Practical considerations

In practice, desks choose criteria based on:
- product type (vanilla vs exotic),
- liquidity of hedging instruments,
- regulatory and capital constraints.

Often, hybrid or heuristic approaches are used.

---

## 5. Key takeaways

- Optimal hedging depends on the chosen risk criterion.
- No single hedging strategy is universally optimal.
- Robustness is often more valuable than theoretical optimality.

---

## Further reading

- Föllmer & Schweizer, hedging in incomplete markets.
- Carmona, utility-based pricing and hedging.
- Taleb, practical perspectives on hedging robustness.
