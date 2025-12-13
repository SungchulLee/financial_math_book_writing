# PDEs Satisfied by Greeks

A clean way to obtain PDEs for Greeks is to treat Greeks as solutions of **sensitivity PDEs**.

---

## Operator form

Define the Black–Scholes operator
\[
\mathcal{A}V
:=
\frac{\partial V}{\partial t}
+\frac{1}{2}\sigma^2 S^2 V_{SS}
+rS V_S
-rV.
\]
Then \(V\) solves \(\mathcal{A}V=0\).

---

## Vega

Let \(\nu=V_\sigma\). Differentiate \(\mathcal{A}V=0\) in \(\sigma\):
\[
\mathcal{A}\nu = -\sigma S^2 V_{SS}.
\]
With payoff independent of \(\sigma\),
\[
\boxed{\nu(T,S)=0.}
\]

---

## Rho

Let \(\rho=V_r\). Differentiating in \(r\) yields
\[
\boxed{
\frac{\partial \rho}{\partial t}
+\frac{1}{2}\sigma^2 S^2 \rho_{SS}
+rS\rho_S
-r\rho
=
V - S V_S,
\qquad \rho(T,S)=0.
}
\]

---

## Theta identity

From the PDE,
\[
\boxed{
\Theta
=
\frac{\partial V}{\partial t}
=
-\frac{1}{2}\sigma^2 S^2 V_{SS} - rS V_S + rV.
}
\]

---

## What to remember

- Vega and rho satisfy inhomogeneous parabolic PDEs with zero terminal data.
- Theta can be computed directly from \(V,\Delta,\Gamma\) using the PDE.
