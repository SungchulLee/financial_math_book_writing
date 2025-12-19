# CIR Model

The Cox–Ingersoll–Ross (CIR) model is a mean-reverting short-rate model with **square-root diffusion**, designed to keep rates non-negative under appropriate conditions.

---

## 1. Model dynamics

Under the risk-neutral measure \(\mathbb{Q}\),

\[
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}},
\]


with parameters \(\kappa,\theta,\sigma>0\).

---

## 2. Positivity and the Feller condition

The boundary behavior depends on the **Feller condition**:

\[
2\kappa\theta \ge \sigma^2.
\]



If satisfied, \(r_t\) stays strictly positive.
If violated, \(r_t\) may hit zero but remains non-negative.

---

## 3. Bond pricing (affine form)

Like Vasicek, CIR yields an exponential-affine bond price:

\[
P(t,T) = A(t,T)\,e^{-B(t,T)r_t}.
\]



Here \(A\) and \(B\) again have closed forms (more complex than Vasicek), reflecting the square-root diffusion.

---

## 4. Strengths and limitations

Strengths:
- non-negativity (under Feller),
- realistic rate distribution shape,
- analytical tractability for bonds.

Limitations:
- single-factor structure limits fit to the full term structure dynamics,
- smiles in interest-rate options require extensions or multi-factor models.

---

## 5. Key takeaways

- CIR is mean-reverting with state-dependent volatility.
- It often preserves non-negativity of rates.
- Bond prices remain affine and tractable.

---

## Further reading

- Cox, Ingersoll & Ross (1985).
- Brigo & Mercurio, CIR and affine term structures.
