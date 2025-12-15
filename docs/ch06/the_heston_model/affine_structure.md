# Affine Structure

A key advantage of the Heston model is its **affine structure**, which enables semi-closed-form pricing of European options via characteristic functions.

---

## 1. Affine processes

A process is affine if its characteristic function has exponential-affine form:
\[
\mathbb{E}\left[e^{iuX_T} \mid X_t\right]
= \exp\left(A(T-t,u) + B(T-t,u)X_t\right).
\]

The Heston model belongs to this class.

---

## 2. Characteristic function of log-price

Let \(X_t = \log S_t\). Under Heston,
\[
\mathbb{E}^{\mathbb{Q}}\left[e^{iuX_T}\mid \mathcal{F}_t\right]
= \exp\big(A(T-t,u) + B(T-t,u)V_t + iuX_t\big),
\]
where \(A,B\) solve Riccati-type ODEs.

---

## 3. Option pricing via Fourier methods

European option prices can be computed by:
- Fourier inversion,
- FFT methods,
- Carr–Madan-type formulas.

This makes Heston calibration fast and robust.

---

## 4. Implications for calibration

Affine structure implies:
- rapid evaluation of prices and gradients,
- feasibility of global surface calibration,
- wide adoption in practice.

---

## 5. Key takeaways

- Affine structure is the main strength of Heston.
- It enables efficient pricing and calibration.
- Many extensions preserve this property.

---

## Further reading

- Duffie, Pan & Singleton, affine jump diffusions.
- Carr & Madan, option valuation using FFT.
