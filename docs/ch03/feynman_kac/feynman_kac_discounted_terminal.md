# Feynman Kac


Let \(X_t\) solve

\[
dX_t = \mu(X_t,t)\,dt + \sigma(X_t,t)\,dW_t,
\]


with generator

\[
(Lu)(x,t)=\mu(x,t)u_x(x,t)+\frac12\sigma^2(x,t)u_{xx}(x,t).
\]



Let \(r(x,t)\) be a discount (or killing) rate and let \(f\) be a terminal payoff.

---

## Statement Discounted


Define

\[
u(x,t)=\mathbb E\!\left[\exp\!\Big(-\int_t^T r(X_s,s)\,ds\Big)\,f(X_T)\,\middle|\,X_t=x\right].
\]


Then \(u\) solves the PDE

\[
u_t + Lu - r\,u = 0,
\qquad
u(x,T)=f(x).
\]



---

## Proof discount


Define the discount factor

\[
Z_s := \exp\!\Big(-\int_t^s r(X_u,u)\,du\Big),
\qquad Z_t=1,
\qquad dZ_s = -r(X_s,s)Z_s\,ds.
\]



Assume \(u\in C^{1,2}\) and satisfies the PDE

\[
u_t + Lu - r\,u = 0.
\]



Consider

\[
Y_s := Z_s\,u(X_s,s).
\]



Using Itô’s formula and the product rule,

\[
dY_s
=
Z_s\Big(u_t + Lu - r\,u\Big)(X_s,s)\,ds
+
Z_s\sigma(X_s,s)u_x(X_s,s)\,dW_s.
\]



By the PDE, the drift term vanishes, so \(Y_s\) is a local martingale:

\[
dY_s = Z_s\sigma u_x\,dW_s.
\]



Taking expectations from \(t\) to \(T\),

\[
u(x,t)=Y_t=\mathbb E^{x,t}[Y_T]
=\mathbb E^{x,t}\!\left[Z_T\,u(X_T,T)\right]
=\mathbb E^{x,t}\!\left[\exp\!\Big(-\int_t^T r(X_s,s)\,ds\Big)\,f(X_T)\right].
\]



This is the discounted Feynman–Kac representation.

---

## Special case


If \(r\equiv 0\), then

\[
u(x,t)=\mathbb E[f(X_T)\mid X_t=x]
\quad\Longleftrightarrow\quad
u_t + Lu = 0,\ \ u(x,T)=f(x).
\]
