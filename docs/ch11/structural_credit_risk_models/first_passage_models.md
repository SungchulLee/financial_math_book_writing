# First-Passage Models

First-passage models extend Merton by allowing default to occur **at any time**, when firm value hits a default barrier.

---

## 1. Default as barrier crossing

Default time is defined as

\[
\tau = \inf\{t \ge 0 : V_t \le B_t\},
\]


where:
- \(V_t\) is firm value,
- \(B_t\) is a default barrier.

This captures early default due to distress.

---

## 2. Barrier specifications

Common choices include:
- constant barriers,
- exponentially growing barriers,
- coupon-linked barriers reflecting liabilities.

Barrier choice strongly affects default probabilities.

---

## 3. Analytical properties

In simple cases (constant barrier, GBM assets):
- default probabilities have closed forms,
- survival probabilities involve hitting-time distributions.

However, pricing becomes more complex than in Merton.

---

## 4. Advantages and limitations

Advantages:
- economically intuitive,
- allows early default,
- richer term structure of credit spreads.

Limitations:
- barrier is not observable,
- calibration is difficult,
- sensitive to modeling assumptions.

---

## 5. Key takeaways

- Default occurs at first passage below a barrier.
- Models generalize Merton’s framework.
- Calibration complexity increases significantly.

---

## Further reading

- Black & Cox (1976).
- Leland & Toft, endogenous barriers.
