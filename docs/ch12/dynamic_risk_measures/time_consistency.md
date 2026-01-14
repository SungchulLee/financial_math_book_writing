# Time-Consistency


Dynamic risk measures extend static risk measures to a multi-period setting. **Time-consistency** is a fundamental requirement ensuring that risk assessments remain logically coherent over time.

---

## Motivation


In a dynamic setting, risk is evaluated at multiple times \(t < T\).
A risk measure should not lead to decisions that are optimal today but suboptimal tomorrow.

Time-consistency formalizes this requirement.

---

## Definition


Let \(\rho_t(\cdot)\) be a conditional risk measure at time \(t\).
The family \((\rho_t)_{t \ge 0}\) is **time-consistent** if

\[
\rho_t(X) \le \rho_t(Y)
\quad \Rightarrow \quad
\rho_s(X) \le \rho_s(Y),
\qquad s < t.
\]



Equivalently, preferences should not reverse over time.

---

## Economic interpretation


Time-consistency implies:
- no preference reversals,
- stable capital allocation rules,
- coherent dynamic decision-making.

Without time-consistency, dynamic risk control becomes unstable.

---

## Examples and non-examples


- Dynamic Expected Shortfall can be time-consistent under suitable constructions.
- Dynamic VaR is typically **not** time-consistent.

This mirrors the static coherence distinction.

---

## Key takeaways


- Time-consistency is essential for dynamic risk management.
- It prevents preference reversals.
- Not all static measures admit time-consistent extensions.

---

## Further reading


- Artzner et al., dynamic risk measures.
- Föllmer & Schied, time-consistency.
