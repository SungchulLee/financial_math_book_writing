# Kolmogorov Backward Equation

The **Kolmogorov backward equation** describes how quantities evolve **backward in time**.
It appears naturally in two forms:

1. As a **PDE for the transition density** in the initial variables
2. As a **PDE for expectations / value functions**

We again consider the diffusion

\[
dX_t = \mu(X_t,t)\,dt + \sigma(X_t,t)\,dB_t.
\]



---

## 1. What the Backward Equation Evolves

- **Density viewpoint**: evolution of \(p(x,t\mid x_0,t_0)\) in \((x_0,t_0)\)
- **Expectation viewpoint**: evolution of conditional expectations backward from terminal data

The backward equation acts on the **initial state** and **initial time**.

---

## 2. Density Form: Backward Equation for Transition Probabilities

The backward equation for the transition density is

\[
-\frac{\partial p}{\partial t_0}
=
\mu(x_0,t_0)\frac{\partial p}{\partial x_0}
+
\frac12\sigma^2(x_0,t_0)\frac{\partial^2 p}{\partial x_0^2}.
\]



Equivalently,

\[
\frac{\partial p}{\partial t_0}
+
\mu(x_0,t_0)\frac{\partial p}{\partial x_0}
+
\frac12\sigma^2(x_0,t_0)\frac{\partial^2 p}{\partial x_0^2}
=0.
\]



### Examples


\[
\begin{array}{lcc}
&\text{SDE}&\text{Backward Equation}\\
\text{Brownian Motion}&
dX_t=dB_t&
-\partial_{t_0}p=\tfrac12\partial_{x_0x_0}p\\
\\
\text{Ornstein–Uhlenbeck}&
dX_t=-\kappa X_tdt+\sigma dB_t&
-\partial_{t_0}p=-\kappa x_0\partial_{x_0}p+\tfrac12\sigma^2\partial_{x_0x_0}p
\end{array}
\]



---

## 3. Expectation Form: Value Function PDE

Let

\[
u(t,x)=\mathbb E[g(X_T)\mid X_t=x],
\]


where \(g\) is a terminal payoff.

Then \(u\) satisfies the **backward PDE**

\[
\partial_t u + Lu = 0,
\qquad
u(T,x)=g(x),
\]


where

\[
L=\mu(x,t)\partial_x+\tfrac12\sigma^2(x,t)\partial_{xx}.
\]



This formulation is the basis for:
- optimal stopping
- stochastic control
- derivative pricing
- the Feynman–Kac formula

---

## 4. Derivation via Chapman–Kolmogorov

??? details "Derivation of the Backward Equation"

    Using the Chapman–Kolmogorov equation,
    expand

    \[
    p(x,t\mid x_0,t_0-h)
    =
    \int p(x,t\mid y,t_0)p(y,t_0\mid x_0,t_0-h)\,dy.
    \]



    A Taylor expansion in \(y-x_0\), followed by taking the limit \(h\to0\),
    yields the backward PDE in \((x_0,t_0)\).

---

## 5. Relation to the Forward Equation

- Forward equation: evolves **distributions**
- Backward equation: evolves **values / expectations**
- They are adjoint under integration:

  \[
  \int f(x)(\partial_t p)\,dx
  =
  \int (Lf)(x)p(x)\,dx
  \]



Together, they form the analytical backbone of diffusion theory.

---

## 6. Outlook

- Adding a potential term leads to the **Feynman–Kac formula**
- Control terms lead to **Hamilton–Jacobi–Bellman equations**
- Martingale methods provide an alternative probabilistic viewpoint
