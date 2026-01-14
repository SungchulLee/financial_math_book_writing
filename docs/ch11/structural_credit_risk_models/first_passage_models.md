# First-Passage Models


First-passage models extend Merton by allowing default to occur **at any time**, when firm value hits a default barrier.

---

## Default as barrier crossing


Default time is defined as

\[
\tau = \inf\{t \ge 0 : V_t \le B_t\},
\]


where:
- \(V_t\) is firm value,
- \(B_t\) is a default barrier.

This captures early default due to distress.

---

## Barrier specifications


Common choices include:
- constant barriers,
- exponentially growing barriers,
- coupon-linked barriers reflecting liabilities.

Barrier choice strongly affects default probabilities.

---

## Analytical properties


In simple cases (constant barrier, GBM assets):
- default probabilities have closed forms,
- survival probabilities involve hitting-time distributions.

However, pricing becomes more complex than in Merton.

---

## Advantages and limitations


Advantages:
- economically intuitive,
- allows early default,
- richer term structure of credit spreads.

Limitations:
- barrier is not observable,
- calibration is difficult,
- sensitive to modeling assumptions.

---

## Key takeaways


- Default occurs at first passage below a barrier.
- Models generalize Merton’s framework.
- Calibration complexity increases significantly.

---

## Further reading


- Black & Cox (1976).
- Leland & Toft, endogenous barriers.
