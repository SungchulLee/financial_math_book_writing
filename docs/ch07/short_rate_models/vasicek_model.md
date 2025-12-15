# Vasicek Model

The Vasicek model is a classic Gaussian short-rate model with mean reversion. It is analytically tractable and leads to closed-form zero-coupon bond prices.

---

## 1. Model dynamics

Under the risk-neutral measure \(\mathbb{Q}\), Vasicek assumes
\[
dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t^{\mathbb{Q}},
\]
where:
- \(\kappa>0\): mean-reversion speed,
- \(\theta\): long-run mean level,
- \(\sigma>0\): volatility.

This is an Ornstein–Uhlenbeck (OU) process.

---

## 2. Key properties

- **Gaussian rates:** \(r_t\) is normally distributed.
- **Mean reversion:** \(\mathbb{E}[r_t]\) reverts to \(\theta\).
- **Possibility of negative rates:** because the distribution is Gaussian.

---

## 3. Bond pricing (affine form)

Vasicek implies an exponential-affine bond price:
\[
P(t,T) = A(t,T)\,e^{-B(t,T)r_t}.
\]

For \(\tau=T-t\),
\[
B(t,T)=\frac{1-e^{-\kappa\tau}}{\kappa}.
\]

The function \(A(t,T)\) has a closed form involving \(\kappa,\theta,\sigma\) (and can be derived via PDE or expectation).

---

## 4. Calibration notes

- Vasicek can be shifted (Hull–White) to fit the initial yield curve exactly.
- Pure Vasicek often cannot fit the observed term structure without such shifting.
- Option pricing is tractable but smiles/skews are limited in Gaussian models.

---

## 5. Key takeaways

- Vasicek is the simplest mean-reverting short-rate diffusion.
- It yields closed-form bond prices in affine form.
- Gaussianity implies negative rates and limited smile features.

---

## Further reading

- Vasicek (1977).
- Hull & White (1990), time-dependent extension.
