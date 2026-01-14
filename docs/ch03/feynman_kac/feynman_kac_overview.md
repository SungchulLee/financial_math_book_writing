# Feynman Kac Overview


Feynman–Kac is the key bridge between:

- **Backward PDEs** (value functions / expectations)
- **Stochastic representations** (conditional expectations under diffusions)
- **Forward PDEs** (transition densities, via an integral representation)

Throughout, let \(X_t\) be a diffusion:

\[
dX_t = \mu(X_t,t)\,dt + \sigma(X_t,t)\,dW_t,
\qquad
(L\varphi)(x,t)=\mu(x,t)\varphi_x+\frac12\sigma^2(x,t)\varphi_{xx}.
\]



---

## Three levels


### 1. Kolmogorov backwa


Define

\[
u(x,t)=\mathbb E\big[f(X_T)\mid X_t=x\big].
\]


Then \(u\) satisfies the terminal-value problem

\[
u_t + Lu = 0,
\qquad
u(x,T)=f(x).
\]



### 2. B Discounted term


Let \(r(x,t)\) be a (possibly state-dependent) discount / killing rate. Define

\[
u(x,t)=\mathbb E\!\left[\exp\!\Big(-\int_t^T r(X_s,s)\,ds\Big)\,f(X_T)\,\middle|\,X_t=x\right].
\]


Then

\[
u_t + Lu - r\,u = 0,
\qquad
u(x,T)=f(x).
\]



### 3. C Discounted term


Let \(g(x,t)\) be a running payoff/source term. Define

\[
u(x,t)=\mathbb E\!\left[
\exp\!\Big(-\int_t^T r(X_s,s)\,ds\Big)f(X_T)
+
\int_t^T \exp\!\Big(-\int_t^s r(X_\tau,\tau)\,d\tau\Big)g(X_s,s)\,ds
\,\middle|\,X_t=x
\right].
\]


Then

\[
u_t + Lu - r\,u + g = 0,
\qquad
u(x,T)=f(x).
\]



---

## How connects forward


- The **backward PDE** tells you how \(u(x,t)\) evolves backward from terminal data.
- The **forward PDE** tells you how the transition density \(p(x,t;y,T)\) evolves forward.
- Feynman–Kac lets you represent

\[
u(x,t)=\int f(y)\,p(x,t;y,T)\,dy
\]


(in the simplest case \(r\equiv0,g\equiv0\)), making the duality explicit.

Next pages: rigorous statements + proofs + examples.
