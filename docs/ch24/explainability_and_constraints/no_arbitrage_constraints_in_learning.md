# No-Arbitrage Constraints in Learning


Learning-based financial models must respect **no-arbitrage constraints** to ensure economic consistency and prevent pathological behavior.

---

## Why constraints matter


Unconstrained learning may produce:
- negative option prices,
- arbitrage opportunities,
- violations of monotonicity or convexity.

Such outputs are unacceptable in pricing applications.

---

## Types of no-arbitrage constraints


Common constraints include:
- monotonicity in strike and maturity,
- convexity of option prices,
- absence of calendar and butterfly arbitrage.

These constraints encode fundamental financial laws.

---

## Enforcing constraints in learning


Approaches include:
- constrained optimization,
- penalty and regularization terms,
- architecture design (e.g., monotone networks).

Constraints improve robustness and generalization.

---

## Trade-offs


Imposing constraints:
- reduces hypothesis space,
- may slightly reduce in-sample fit,
- greatly improves out-of-sample stability.

This mirrors regularization effects.

---

## Key takeaways


- No-arbitrage constraints are essential.
- Learning must respect financial structure.
- Constraints improve robustness and trust.

---

## Further reading


- Ackerer et al., arbitrage-free learning.
- Buehler et al., deep hedging constraints.
