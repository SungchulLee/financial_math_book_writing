# Local Volatility Models

Local volatility replaces constant \(\sigma\) with \(\sigma_{\mathrm{loc}}(t,S)\), allowing calibration to an implied volatility surface.

---

## 1. Model

Under \(\mathbb{Q}\),
\[
\boxed{
\mathrm{d}S_t=rS_t\,\mathrm{d}t+\sigma_{\mathrm{loc}}(t,S_t)S_t\,\mathrm{d}W_t^{\mathbb{Q}}.
}
\]

---

## 2. Pricing PDE

\[
\boxed{
\frac{\partial V}{\partial t}
+\frac{1}{2}\sigma_{\mathrm{loc}}(t,S)^2 S^2 V_{SS}
+rS V_S
-rV=0,
\qquad V(T,S)=\Phi(S).
}
\]

---

## 3. Dupire (Formal)

Given call prices \(C(T,K)\), a formal local variance is
\[
\boxed{
\sigma_{\mathrm{loc}}(T,K)^2=
\frac{\frac{\partial C}{\partial T}(T,K)}
{\frac{1}{2}K^2\frac{\partial^2 C}{\partial K^2}(T,K)}.
}
\]

---

## 4. What to Remember

- Local volatility fits the full surface (idealized).
- Dynamics of the smile may be unrealistic; hedging can be challenging.
