# Feynman Kac Running


Let \(X_t\) be a diffusion with generator \(L\). Let

- \(f(x)\): terminal payoff
- \(r(x,t)\): discount/killing rate
- \(g(x,t)\): running payoff (source term)

---

## Statement General


Define

\[
u(x,t)=\mathbb E\!\left[
\exp\!\Big(-\int_t^T r(X_s,s)\,ds\Big)f(X_T)
+
\int_t^T \exp\!\Big(-\int_t^s r(X_\tau,\tau)\,d\tau\Big)g(X_s,s)\,ds
\,\middle|\,X_t=x
\right].
\]



Then \(u\) solves

\[
u_t + Lu - r\,u + g = 0,
\qquad
u(x,T)=f(x).
\]



---

## Proof augmented


Let

\[
Z_s=\exp\!\Big(-\int_t^s r(X_u,u)\,du\Big),\qquad dZ_s=-r(X_s,s)Z_s\,ds.
\]



Assume \(u\in C^{1,2}\) solves the PDE. Define

\[
Y_s := Z_s u(X_s,s) + \int_t^s Z_\tau\,g(X_\tau,\tau)\,d\tau.
\]



Compute \(dY_s\). Using Itô + product rule:

\[
d(Z_su(X_s,s))
=
Z_s(u_t+Lu-r\,u)(X_s,s)\,ds
+
Z_s\sigma u_x\,dW_s.
\]


Adding \(d\left(\int_t^s Z_\tau g(X_\tau,\tau)\,d\tau\right)=Z_sg(X_s,s)\,ds\), we get

\[
dY_s
=
Z_s\big(u_t+Lu-r\,u+g\big)(X_s,s)\,ds
+
Z_s\sigma u_x\,dW_s.
\]


By the PDE the drift is zero, hence \(Y_s\) is a local martingale.

Taking expectations from \(t\) to \(T\) yields

\[
u(x,t)=\mathbb E^{x,t}\!\left[
Z_T f(X_T) + \int_t^T Z_s g(X_s,s)\,ds
\right],
\]


which is exactly the stated representation.

---

## Interpretation


- \(g\) acts as a **source term** (like heat generation).
- \(r\) acts as **discounting** (finance) or **killing** (probability/physics).
