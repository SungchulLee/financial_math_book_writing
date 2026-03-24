# CDS Spreads and Hazard Rates


CDS spreads encode market-implied default risk and can be mapped to **hazard rates** within reduced-form credit models.

---

## Relationship between spreads and default risk


Intuitively:
- higher CDS spreads imply higher default intensity,
- spreads compensate for expected default losses.

Under simplifying assumptions, spreads are approximately:

\[
s \approx (1 - R) \times \text{average hazard rate}.
\]



---

## Formal link under intensity models


Under recovery of face value and deterministic intensity \(\lambda\),

\[
s
= \frac{(1-R) \int_0^T e^{-\int_0^t (r+\lambda) ds} \lambda \, dt}
{\int_0^T e^{-\int_0^t (r+\lambda) ds} \, dt}.
\]



This equation is inverted to infer \(\lambda\) from market spreads.

---

## CDS bootstrapping


In practice:
- CDS spreads across maturities are given,
- piecewise-constant hazard rates are assumed,
- hazard rates are bootstrapped sequentially.

This is analogous to yield curve construction.

---

## Limitations


- Recovery assumptions affect inferred hazard rates.
- Liquidity and counterparty risk affect CDS spreads.
- The hazard-rate interpretation is model-dependent.

---

## Key takeaways


- CDS spreads imply default intensities.
- Bootstrapping extracts hazard rate curves.
- Interpretation depends on recovery and model choices.

---

## Further reading


- Brigo et al., CDS bootstrapping.
- O'Kane, CDS term structures.

---

## Exercises

**Exercise 1.** A 5-year CDS has a par spread of $s = 120$ bp and the assumed recovery rate is $R = 40\%$. Using the approximation $s \approx (1-R)\lambda$, compute the implied constant hazard rate $\lambda$. What is the corresponding 5-year survival probability $S(0,5) = e^{-\lambda \cdot 5}$?

---

**Exercise 2.** Under deterministic intensity $\lambda$ and constant risk-free rate $r$, the par CDS spread satisfies

$$
s = \frac{(1-R)\int_0^T e^{-(r+\lambda)t}\,\lambda\,dt}{\int_0^T e^{-(r+\lambda)t}\,dt}
$$

Show that this simplifies to $s = (1-R)\lambda$ regardless of $r$ and $T$. Explain why the risk-free rate cancels in this expression.

---

**Exercise 3.** Suppose CDS spreads for maturities 1Y, 3Y, and 5Y are 50 bp, 80 bp, and 120 bp, respectively. Assuming $R = 40\%$ and piecewise-constant hazard rates, bootstrap the hazard rates $\lambda_1$ (for $[0,1]$), $\lambda_2$ (for $(1,3]$), and $\lambda_3$ (for $(3,5]$). Use a flat risk-free rate $r = 3\%$ and the simplified formula for each maturity.

---

**Exercise 4.** A trader observes that the 5-year CDS spread for a reference entity is 200 bp. With $R = 40\%$, the implied hazard rate is $\lambda = 333$ bp. If the recovery assumption is changed to $R = 30\%$, what is the new implied hazard rate? Discuss why the assumed recovery rate materially affects the calibrated hazard rate curve.

---

**Exercise 5.** Explain why CDS bootstrapping is analogous to yield curve construction from swap rates. In particular, identify the analogues of: (a) the discount factors, (b) the forward rates, and (c) the par instruments used for calibration.

---

**Exercise 6.** A corporate bond with 5-year maturity has a yield spread of 150 bp over the risk-free rate. The 5-year CDS spread for the same reference entity is 130 bp. Compute the CDS-bond basis. List three market frictions that could explain a persistent negative basis.
