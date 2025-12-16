# CDS Spreads and Hazard Rates

CDS spreads encode market-implied default risk and can be mapped to **hazard rates** within reduced-form credit models.

---

## 1. Relationship between spreads and default risk

Intuitively:
- higher CDS spreads imply higher default intensity,
- spreads compensate for expected default losses.

Under simplifying assumptions, spreads are approximately:

\[
s \approx (1 - R) \times \text{average hazard rate}.
\]



---

## 2. Formal link under intensity models

Under recovery of face value and deterministic intensity \(\lambda\),

\[
s
= \frac{(1-R) \int_0^T e^{-\int_0^t (r+\lambda) ds} \lambda \, dt}
{\int_0^T e^{-\int_0^t (r+\lambda) ds} \, dt}.
\]



This equation is inverted to infer \(\lambda\) from market spreads.

---

## 3. CDS bootstrapping

In practice:
- CDS spreads across maturities are given,
- piecewise-constant hazard rates are assumed,
- hazard rates are bootstrapped sequentially.

This is analogous to yield curve construction.

---

## 4. Limitations

- Recovery assumptions affect inferred hazard rates.
- Liquidity and counterparty risk affect CDS spreads.
- The hazard-rate interpretation is model-dependent.

---

## 5. Key takeaways

- CDS spreads imply default intensities.
- Bootstrapping extracts hazard rate curves.
- Interpretation depends on recovery and model choices.

---

## Further reading

- Brigo et al., CDS bootstrapping.
- O'Kane, CDS term structures.
