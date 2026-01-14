# Dynamic Consistency


**Dynamic consistency** refers to whether a model’s implied volatility dynamics are coherent over time. A dynamically consistent model should not contradict itself when re-evaluated at future dates.

---

## Definition


A volatility model is dynamically consistent if:
- today’s implied dynamics,
- when evolved forward under the model,
- produce implied surfaces consistent with future recalibration.

This is closely related to forward-consistency ideas.

---

## Inconsistencies in common models


- **Black–Scholes:** dynamically consistent but unrealistic.
- **Local volatility:** fits today’s surface but implies unrealistic future smiles.
- **Stochastic volatility:** better dynamic behavior but still imperfect.

Dynamic inconsistency manifests as implausible forward smiles.

---

## Consequences for pricing and hedging


Dynamic inconsistency leads to:
- mispricing of forward-start products,
- hedging strategies that fail over time,
- recalibration-induced P&L noise.

---

## Model design trade-offs


Improving dynamic consistency often requires:
- additional state variables,
- stochastic volatility factors,
- sacrificing exact fit to today’s surface.

This highlights the trade-off between static fit and dynamic realism.

---

## Key takeaways


- Dynamic consistency is a stringent requirement.
- Perfect static fit does not guarantee realistic dynamics.
- Forward smiles are a key diagnostic tool.

---

## Further reading


- Bergomi, *Stochastic Volatility Modeling*.
- Björk, forward-consistent volatility modeling.
