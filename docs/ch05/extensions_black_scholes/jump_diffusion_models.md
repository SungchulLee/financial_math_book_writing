# Jump-Diffusion Models

Jump-diffusions incorporate discontinuous moves and generate heavy tails and short-maturity smiles.

---

## 1. Merton-Type Model


\[
\boxed{
\frac{\mathrm{d}S_t}{S_{t^-}}=(r-\lambda\kappa)\,\mathrm{d}t+\sigma\,\mathrm{d}W_t+\mathrm{d}J_t,
}
\]


with Poisson intensity \(\lambda\), jump multiplier \(Y\), and \(\kappa=\mathbb{E}[Y-1]\) ensuring the discounted price is a martingale.

---

## 2. Pricing PIDE


\[
\boxed{
\frac{\partial V}{\partial t}
+\frac{1}{2}\sigma^2 S^2 V_{SS}
+rS V_S
-rV
+\lambda\int_{\mathbb{R}_+}\bigl(V(t,Sy)-V(t,S)\bigr)\,\nu(\mathrm{d}y)=0.
}
\]



---

## 3. What to Remember

- Jumps lead to integro-differential pricing equations.
- Jumps naturally create implied volatility smiles, especially at short maturities.
