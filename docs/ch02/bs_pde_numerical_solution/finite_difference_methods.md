# Finite Difference Methods

We consider the Black–Scholes PDE for an option price \(V(t,S)\) (no dividends for simplicity):
\[
\boxed{
\frac{\partial V}{\partial t}
+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}
+rS\frac{\partial V}{\partial S}
-rV=0,
\qquad (t,S)\in [0,T)\times (0,\infty).
}
\]
For a European payoff \(V(T,S)=\Phi(S)\), this is a terminal value problem.

---

## 1. Time-to-Maturity Form

Set \(\tau:=T-t\) and \(u(\tau,S):=V(T-\tau,S)\). Then
\[
\boxed{
\frac{\partial u}{\partial \tau}
=
\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2}
+rS\frac{\partial u}{\partial S}
-ru,
\qquad u(0,S)=\Phi(S).
}
\]

---

## 2. Spatial Grid and Notation

Choose a grid \(S_i\) on \([0,S_{\max}]\). Let
\[
u_i^n \approx u(\tau_n,S_i),
\qquad \tau_n = n\Delta \tau.
\]

For uniform spacing \(S_i=i\Delta S\), central differences are:
\[
\boxed{
u_S(\tau_n,S_i)\approx \frac{u_{i+1}^n-u_{i-1}^n}{2\Delta S},
\qquad
u_{SS}(\tau_n,S_i)\approx \frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{(\Delta S)^2}.
}
\]

---

## 3. Discrete Operator View

Write the PDE as
\[
\frac{\partial u}{\partial \tau}=\mathcal{A}u,
\quad
(\mathcal{A}u)(S)=\frac{1}{2}\sigma^2 S^2 u_{SS}+rSu_S-ru.
\]
Finite differences yield a matrix \(A\) such that \(\mathcal{A}\approx A\), so the PDE becomes an ODE system:
\[
\boxed{
\frac{\mathrm{d}}{\mathrm{d}\tau}u(\tau)\approx Au(\tau).
}
\]

---

## 4. Truncation and Boundary Conditions

Truncate \(S\in(0,\infty)\) to \([0,S_{\max}]\). For a call,
\[
V(t,0)=0,
\qquad
V(t,S_{\max})\approx S_{\max}-Ke^{-r(T-t)}.
\]
For a put,
\[
V(t,0)\approx Ke^{-r(T-t)},
\qquad
V(t,S_{\max})\approx 0.
\]

---

## 5. Why Log-Price Helps

Using \(x=\log S\) often yields constant diffusion coefficient (after a gauge transform), improving numerical conditioning and enabling uniform grids in \(x\).

---

## 6. What to Remember

- Finite differences replace derivatives by local stencil formulas.
- Boundary treatment is essential and affects stability/accuracy.
- Log-price coordinates often improve behavior.
