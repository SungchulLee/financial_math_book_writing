# Feynman Kac


This page has two goals:

1. practice solving PDEs using the probabilistic representation
2. make explicit where the **forward equation** sits inside Feynman–Kac

---

## Application Heat


Solve

\[
V_t + \frac12\sigma^2 V_{xx}=0,\qquad V(T,x)=x^2.
\]



Take the process \(dX_s=\sigma\,dW_s\). By Feynman–Kac (no discount, no running payoff),

\[
V(t,x)=\mathbb E_{t,x}[X_T^2].
\]


Since \(X_T=x+\sigma(W_T-W_t)\),

\[
V(t,x)=x^2+\sigma^2(T-t).
\]



**Exercise:** verify directly that this satisfies the PDE and terminal condition.

---

## Application heat


Solve

\[
V_t + \mu V_x + \frac12\sigma^2 V_{xx}=0,\qquad V(T,x)=x^2.
\]



Take \(dX_s=\mu\,ds+\sigma\,dW_s\). Then \(X_T=x+\mu(T-t)+\sigma(W_T-W_t)\), so

\[
V(t,x)=\mathbb E[X_T^2]=\big(x+\mu(T-t)\big)^2+\sigma^2(T-t).
\]



---

## Where forward


Let \(p(x,t;y,T)\) be the transition density of \(X\). Then (in the simplest case)

\[
u(x,t)=\mathbb E[f(X_T)\mid X_t=x]=\int f(y)\,p(x,t;y,T)\,dy.
\]



- For fixed \((x,t)\), as a function of \((y,T)\), the density \(p\) satisfies the **Kolmogorov forward** equation.
- For fixed \((y,T)\), as a function of \((x,t)\), the same \(p\) satisfies the **Kolmogorov backward** equation.

So even when you “solve the backward PDE for \(u\),” the representation

\[
u(x,t)=\int f(y)\,p(x,t;y,T)\,dy
\]


quietly contains the forward evolution through \(p\).

---

## Summary


- Backward PDE: differential law for \(u\)
- Forward PDE: differential law for \(p\)
- Feynman–Kac: the bridge \(u = \int f\,p\)
