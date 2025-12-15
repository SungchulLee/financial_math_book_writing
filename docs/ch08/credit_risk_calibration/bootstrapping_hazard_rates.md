# Bootstrapping Hazard Rates

Calibration of reduced-form credit models typically starts by **bootstrapping hazard rates** from market instruments, most commonly CDS spreads.

---

## 1. Credit curve construction

Analogous to yield curve bootstrapping, the goal is to construct a **survival probability curve**
\[
S(0,T) = \mathbb{Q}(\tau > T),
\]
or equivalently a hazard rate curve \(\lambda(t)\).

Market inputs:
- CDS spreads across maturities,
- recovery assumptions,
- discount curve.

---

## 2. Piecewise-constant hazard rates

A standard approach assumes
\[
\lambda(t) = \lambda_i, \quad t \in (T_{i-1}, T_i].
\]

Hazard rates are solved sequentially so that each CDS maturity is priced exactly.

---

## 3. Numerical procedure

The bootstrapping algorithm:
1. Fix recovery rate and discount curve.
2. Solve for \(\lambda_1\) using the shortest-maturity CDS.
3. Proceed iteratively for longer maturities.

This yields a term structure of default intensities.

---

## 4. Practical considerations

- Results depend strongly on recovery assumptions.
- Market liquidity varies by maturity.
- Smoothness is often imposed post-bootstrap.

Despite limitations, this approach is industry standard.

---

## 5. Key takeaways

- Hazard rates are bootstrapped from CDS spreads.
- Piecewise-constant intensities are widely used.
- Recovery assumptions critically affect results.

---

## Further reading

- O'Kane, CDS bootstrapping.
- Brigo et al., credit curve construction.
