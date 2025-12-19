# Negative Rates and Model Breakdown

The emergence of **negative interest rates** in several markets exposed important weaknesses in classical interest-rate models. Understanding these breakdowns is central to interest-rate model risk.

---

## 1. Classical assumptions and their failure

Many traditional models implicitly assume:
- non-negative interest rates,
- lognormal dynamics for rates or forwards,
- discount factors decreasing smoothly.

Negative rates violate these assumptions and invalidate parts of the modeling framework.

---

## 2. Impact on short-rate models

- **Vasicek:** allows negative rates naturally, but may produce unrealistic distributions.
- **CIR:** enforces non-negativity but struggles when market rates are negative.
- **Shifted models:** ad-hoc shifts restore positivity but distort dynamics.

No approach is fully satisfactory across regimes.

---

## 3. Market model issues

Lognormal LIBOR Market Models (LMM):
- break down when rates approach zero,
- require shifts or normal (Bachelier) dynamics,
- complicate calibration and interpretation.

These fixes introduce additional model risk.

---

## 4. Practical responses

Practitioners respond by:
- switching to normal-rate models,
- introducing time-dependent shifts,
- accepting regime-dependent modeling choices.

Each solution trades theoretical consistency for practicality.

---

## 5. Key takeaways

- Negative rates reveal hidden model assumptions.
- Classical lognormal frameworks are fragile.
- Regime awareness is essential in IR modeling.

---

## Further reading

- Andersen & Piterbarg, negative rates discussions.
- Mercurio, interest-rate modeling post-crisis.
