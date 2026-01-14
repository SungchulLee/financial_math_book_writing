# Survival Probability


Survival probabilities are central objects in reduced-form credit models. They describe the likelihood that default has not occurred by a given time.

---

## Definition


The **survival probability** up to time \(T\) is

\[
S(t,T) := \mathbb{Q}(\tau > T \mid \mathcal{F}_t).
\]



It is the complement of the cumulative default probability.

---

## Relation to intensity


Under standard regularity assumptions,

\[
S(t,T)
= \mathbb{E}^{\mathbb{Q}}\left[
\exp\left(-\int_t^T \lambda_s ds\right)
\middle| \mathcal{F}_t
\right].
\]



If \(\lambda_t\) is deterministic,

\[
S(t,T) = \exp\left(-\int_t^T \lambda_s ds\right).
\]



---

## Term structure of default probabilities


Survival probabilities define a **credit term structure**:
- short maturities reflect near-term credit risk,
- long maturities embed long-run solvency expectations.

Market instruments (CDS, bonds) reveal this structure.

---

## Calibration implications


In practice:
- piecewise-constant intensities are often calibrated to CDS spreads,
- survival curves are bootstrapped analogously to yield curves,
- smoothness constraints improve stability.

---

## Key takeaways


- Survival probability is the key state variable in reduced-form models.
- It is determined by the integrated intensity.
- Market credit curves encode survival information.

---

## Further reading


- O'Kane, *Modelling Single-name and Multi-name Credit Derivatives*.
- Brigo et al., credit curve construction.
