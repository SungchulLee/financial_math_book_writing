# Kolmogorov Forward Equation (Fokker–Planck Equation)

The **Kolmogorov forward equation** describes how the **probability law** of a diffusion process evolves forward in time.
It can be formulated either:

1. As a **PDE for the transition density**
2. As an **evolution equation for expectations** (weak / dual form)

Throughout this page, we consider the Itô diffusion

\[
dX_t = \mu(X_t,t)\,dt + \sigma(X_t,t)\,dB_t.
\]



---

## 1. What the Forward Equation Evolves

- **Density viewpoint**: evolves the distribution \(p(x,t\mid x_0,t_0)\) forward in time.
- **Expectation viewpoint**: evolves expectations of test functions under the law of \(X_t\).

The forward equation acts on the **current state variable** \(x\) and time \(t\).

---

## 2. Density Form: Fokker–Planck Equation

Let \(p(x,t\mid x_0,t_0)\) denote the transition probability density.
The Kolmogorov forward equation is

\[
\frac{\partial p}{\partial t}
=
-\frac{\partial}{\partial x}\big(\mu(x,t)p\big)
+
\frac{1}{2}\frac{\partial^2}{\partial x^2}\big(\sigma^2(x,t)p\big).
\]



### Examples


\[
\begin{array}{lcc}
&\text{SDE}&\text{Forward Equation}\\
\text{Brownian Motion}&
dX_t=dB_t&
\partial_t p=\frac12\partial_{xx}p\\
\\
\text{Ornstein–Uhlenbeck}&
dX_t=-\kappa X_tdt+\sigma dB_t&
\partial_t p=\kappa\partial_x(xp)+\frac12\sigma^2\partial_{xx}p\\
\\
\text{Geometric Brownian Motion}&
dX_t=\mu X_tdt+\sigma X_tdB_t&
\partial_t p=-\mu\partial_x(xp)+\frac12\sigma^2\partial_{xx}(x^2p)
\end{array}
\]



---

## 3. Expectation Form (Weak / Dual Form)

For any smooth test function \(f\) with suitable decay,

\[
\frac{d}{dt}\mathbb E[f(X_t)\mid X_{t_0}=x_0]
=
\mathbb E[(Lf)(X_t)],
\]


where the infinitesimal generator is

\[
L f(x,t)
=
\mu(x,t)\frac{\partial f}{\partial x}
+
\frac12\sigma^2(x,t)\frac{\partial^2 f}{\partial x^2}.
\]



Equivalently,

\[
\frac{d}{dt}\int f(x)p(x,t)\,dx
=
\int (Lf)(x)p(x,t)\,dx.
\]



This formulation is **dual** to the density PDE: the generator acts on test functions, while its adjoint acts on densities.

---

## 4. Derivation (Itô + Integration by Parts)

??? details "Derivation of the Forward Equation"

    Apply Itô’s lemma to \(f(X_t)\):

    \[
    df(X_t)
    =
    \left(\mu f_x + \tfrac12\sigma^2 f_{xx}\right)dt
    +
    \sigma f_x\,dB_t.
    \]



    Taking expectations eliminates the martingale term:

    \[
    \frac{d}{dt}\mathbb E[f(X_t)]
    =
    \mathbb E\!\left[\mu f_x + \tfrac12\sigma^2 f_{xx}\right].
    \]



    Writing expectations via the density and integrating by parts transfers derivatives
    from \(f\) onto \(p\), yielding the Fokker–Planck equation.

---

## 5. Interpretation

- The forward equation conserves probability mass.
- It describes **how randomness spreads** over time.
- It is fundamental for:
  - invariant measures
  - long-time behavior
  - diffusion approximations
