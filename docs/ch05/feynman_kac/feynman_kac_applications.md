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

---

## Exercises

**Exercise 1.**
Solve the PDE $V_t + \frac{1}{2}\sigma^2 V_{xx} = 0$ with terminal condition $V(T, x) = x^3$ using the Feynman-Kac representation. (Hint: if $X_T = x + \sigma(W_T - W_t)$, compute $\mathbb{E}[X_T^3]$ using the moments of the normal distribution.)

---

**Exercise 2.**
Solve $V_t + \mu V_x + \frac{1}{2}\sigma^2 V_{xx} - rV = 0$ with $V(T, x) = x$ using the discounted Feynman-Kac formula. Verify your answer satisfies the PDE by direct substitution.

---

**Exercise 3.**
Consider the PDE $V_t + \frac{1}{2}\sigma^2 V_{xx} = 0$ with $V(T, x) = e^{ax}$ for constant $a$. Use Feynman-Kac to compute $V(t, x) = \mathbb{E}[e^{aX_T} | X_t = x]$ where $dX_s = \sigma\,dW_s$. Verify that your answer satisfies the PDE.

---

**Exercise 4.**
Explain the relationship between the backward and forward Kolmogorov equations in the context of the Feynman-Kac formula. If $u(x,t) = \int f(y)\,p(x,t;y,T)\,dy$, identify which equation governs $u$ as a function of $(x,t)$ and which governs $p$ as a function of $(y,T)$.

---

**Exercise 5.**
Solve $V_t + \mu V_x + \frac{1}{2}\sigma^2 V_{xx} = 0$ with $V(T, x) = \max(x, 0)$ using Feynman-Kac. Write $V(t, x) = \mathbb{E}[\max(X_T, 0) | X_t = x]$ and express the answer in terms of the standard normal CDF $\Phi$.

---

**Exercise 6.**
Consider $V_t + \frac{1}{2}\sigma^2 V_{xx} + f(x) = 0$ with $V(T, x) = 0$ where $f(x) = 1$. Use the Feynman-Kac formula with running payoff to show that $V(t, x) = T - t$. Verify by substitution into the PDE.

---

**Exercise 7.**
Explain why the Feynman-Kac formula provides two equivalent computational methods: solving the PDE (finite differences) and computing the expectation (Monte Carlo). For a one-dimensional problem on a fine grid, which method is typically more efficient? For a five-dimensional problem, which method is preferred and why?
