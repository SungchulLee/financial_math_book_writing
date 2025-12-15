# Conditional Risk Measures

**Conditional risk measures** quantify risk given the information available at a specific time. They form the building blocks of dynamic risk frameworks.

---

## 1. Conditional setting

Let \(\mathcal{F}_t\) denote the information available at time \(t\).
A conditional risk measure maps a future loss \(X\) to an \(\mathcal{F}_t\)-measurable random variable.

---

## 2. Definition

A conditional risk measure \(\rho_t(X)\) satisfies:
\[
Key properties analogous to static measures,
\]
but holds almost surely with respect to \(\mathcal{F}_t\).

For example, conditional Expected Shortfall is defined via conditional expectations.

---

## 3. Interpretation

Conditional risk measures:
- adapt risk assessments to evolving information,
- reflect updated market conditions,
- allow scenario-dependent capital requirements.

They are essential for real-time risk management.

---

## 4. Relation to static measures

Static risk measures are special cases with trivial information.
Dynamic measures are sequences of conditional risk measures linked by consistency conditions.

---

## 5. Key takeaways

- Conditional risk measures depend on available information.
- They generalize static risk concepts.
- They enable adaptive, forward-looking risk control.

---

## Further reading

- Föllmer & Penner, conditional risk measures.
- McNeil et al., conditional ES.
