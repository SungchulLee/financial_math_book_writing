# Forward Consistency


**Forward consistency** aims to ensure that a model calibrated today remains internally consistent when viewed from tomorrow’s perspective. It provides a theoretical framework for mitigating the recalibration problem.

---

## Definition of forward consistency


A model is forward consistent if:
- parameters calibrated at time \(t\),
- when evolved according to the model’s own dynamics,
- generate future price distributions consistent with recalibration at later times.

In other words, recalibration should not contradict the model’s implied evolution.

---

## Forward consistency in interest-rate models


In Heath–Jarrow–Morton (HJM) frameworks:
- the entire forward curve is modeled as a state variable,
- no recalibration is needed once the curve is observed.

This eliminates parameter jumps by construction.

---

## Challenges in equity and volatility models


Equity volatility models typically:
- have low-dimensional parameters,
- cannot span the full implied-vol surface dynamics.

As a result:
- recalibration becomes necessary,
- forward consistency is violated unless the model is extended.

---

## Approaches to restore consistency


Methods include:
- **state-extended models** (add latent factors),
- **stochastic parameter models**,
- **term-structure extensions** of volatility models,
- **consistent recalibration (CRC) frameworks**.

These approaches trade model simplicity for dynamic coherence.

---

## Key takeaways


- Forward consistency links calibration across time.
- Static models are generally not forward consistent.
- Achieving consistency requires richer state dynamics.

---

## Further reading


- Björk & Christensen, consistent recalibration.
- Filipović, *Term-Structure Models*.
- Carmona & Nadtochiy, stochastic volatility term structures.
