# Free Boundary Problems (American Options)

American options lead to **optimal stopping** and to a **variational inequality** (obstacle problem), not a classical PDE.

We focus on the American put payoff \(\Phi(S)=(K-S)^+\).

---

## 1. Optimal Stopping Representation

Under risk-neutral dynamics
\[
\mathrm{d}S_t=rS_t\,\mathrm{d}t+\sigma S_t\,\mathrm{d}W_t,
\]
the American price is
\[
\boxed{
V(t,S)=\sup_{\tau\in\mathcal{T}_{t,T}}\mathbb{E}^{t,S}\!\left[e^{-r(\tau-t)}\Phi(S_\tau)\right].
}
\]

---

## 2. Variational Inequality

Let \(\mathcal{L}\) be the Black–Scholes generator:
\[
\mathcal{L}f=\frac12\sigma^2S^2 f_{SS}+rS f_S.
\]
Then \(V\) satisfies
\[
\boxed{
\min\!\left(
-\frac{\partial V}{\partial t}-\mathcal{L}V+rV,\;
V-\Phi
\right)=0.
}
\]

Continuation region: \(V>\Phi\) and the PDE holds.  
Exercise region: \(V=\Phi\).

---

## 3. Free Boundary and Smooth Pasting (Formal)

Let \(S^\ast(t)\) be the exercise boundary. Then
\[
\boxed{V(t,S^\ast(t))=K-S^\ast(t),\qquad V_S(t,S^\ast(t))=-1.}
\]

---

## 4. Numerical Enforcement

Common discrete formulations:
- projection: \(V^{n+1}\leftarrow\max\{V^{n+1},\Phi\}\),
- linear complementarity problem (LCP) enforcing complementarity between PDE residual and obstacle gap.

---

## 5. What to Remember

- American pricing is optimal stopping.
- The PDE becomes an obstacle problem with an unknown free boundary.
- Numerics must enforce \(V\ge\Phi\) plus the dynamics.
