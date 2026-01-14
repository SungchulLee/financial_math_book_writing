Good — now we can **formally define diffusion processes** in the language we have built
(Brownian motion → stochastic integration → Itô calculus).

I will proceed **axiomatically and cleanly**, with **full LaTeX**, **index notation**, and **no code**.

---

# Probability–Filtration Setup


Let
[
(\Omega,\mathcal{F},(\mathcal{F}*t)*{t\ge 0},\mathbb{P})
]
be a filtered probability space satisfying the **usual conditions**:

* ((\mathcal{F}_t)) is right-continuous
* (\mathcal{F}_0) contains all (\mathbb{P})-null sets

Let
[
W_t = (W_t^{1},\dots,W_t^{m})
]
be an (m)-dimensional Brownian motion adapted to ((\mathcal{F}_t)).

---

# Definition of an Itô Diffusion (Core Definition)


An (\mathbb{R}^d)-valued stochastic process
[
X_t = (X_t^{1},\dots,X_t^{d})
]
is called a **diffusion process** (or **Itô diffusion**) if it satisfies the stochastic differential equation

[
\boxed{
\mathrm{d}X_t^{i}
=================

b^{i}(t,X_t),\mathrm{d}t
+
\sigma^{i\alpha}(t,X_t),\mathrm{d}W_t^{\alpha},
\qquad
i=1,\dots,d,\ \alpha=1,\dots,m.
}
]

Here:

* (b^{i} : [0,\infty)\times\mathbb{R}^d \to \mathbb{R}) is the **drift field**
* (\sigma^{i\alpha} : [0,\infty)\times\mathbb{R}^d \to \mathbb{R}) is the **diffusion matrix**

---

# Integral (Weak) Form of the Definition


The SDE above is shorthand for the **integral equation**

[
\boxed{
X_t^{i}
=======

X_0^{i}
+
\int_0^t b^{i}(s,X_s),\mathrm{d}s
+
\int_0^t \sigma^{i\alpha}(s,X_s),\mathrm{d}W_s^{\alpha}
}
]

This is the **actual mathematical definition**; the differential form is symbolic.

---

# Structural Properties (Built into the Definition)


From the definition:

### 1. (i) Continuity of paths


[
t \mapsto X_t(\omega) \quad \text{is continuous almost surely}
]

because both integrals produce continuous processes.

### 2. (ii) Semimartingale structure


[
X_t^{i}
=======

\underbrace{X_0^{i}+\int_0^t b^{i}(s,X_s),\mathrm{d}s}*{\text{finite variation}}
+
\underbrace{\int_0^t \sigma^{i\alpha}(s,X_s),\mathrm{d}W_s^{\alpha}}*{\text{local martingale}}
]

---

# Diffusion Matrix and Covariation


Define the **diffusion (covariance) matrix**
[
\boxed{
a^{ij}(t,x)
:=
\sigma^{i\alpha}(t,x)\sigma^{j\alpha}(t,x)
}
]

Then the quadratic covariation of the components satisfies
[
\boxed{
\mathrm{d}\langle X^{i},X^{j}\rangle_t
======================================

a^{ij}(t,X_t),\mathrm{d}t
}
]

This identity is **defining** for diffusions.

---

# Generator of a Diffusion


For (f \in C^{2}(\mathbb{R}^d)), define the **infinitesimal generator**
[
\boxed{
(\mathcal{L}f)(x,t)
===================

b^{i}(t,x)\frac{\partial f}{\partial x_i}(x)
+
\frac{1}{2}a^{ij}(t,x)\frac{\partial^2 f}{\partial x_i\partial x_j}(x)
}
]

Itô’s lemma implies:
[
\boxed{
f(X_t)
------

## f(X_0)


\int_0^t (\mathcal{L}f)(X_s,s),\mathrm{d}s
\quad \text{is a martingale}
}
]

This characterizes diffusions among Markov processes.

---

# Markov Property (Under Mild Conditions)


If (b,\sigma) satisfy standard Lipschitz and growth assumptions, then (X_t) is a **strong Markov process**, and

[
\mathbb{E}[f(X_t)\mid\mathcal{F}_s]
===================================

\mathbb{E}[f(X_t)\mid X_s]
\quad \text{for } s\le t.
]

---

# Kolmogorov Equations


Let (p(t,x)) be the probability density of (X_t).

### 1. Forward (Fokker–Planck):


[
\boxed{
\frac{\partial p}{\partial t}
=============================

-\frac{\partial}{\partial x_i}!\left(b^{i}p\right)
+
\frac{1}{2}
\frac{\partial^2}{\partial x_i\partial x_j}!\left(a^{ij}p\right)
}
]

### 2. Backward:


[
\boxed{
\frac{\partial u}{\partial t}
+
\mathcal{L}u
============

0
}
]

---

# Special Cases


### 1. (i) Pure Brownian motion


[
\mathrm{d}X_t^{i} = \mathrm{d}W_t^{i}
]

### 2. (ii) Drifted Brownian motion


[
\mathrm{d}X_t^{i} = b^{i}(X_t),\mathrm{d}t + \mathrm{d}W_t^{i}
]

### 3. (iii) Gradient diffusion


[
\mathrm{d}X_t = -\nabla V(X_t),\mathrm{d}t + \sqrt{2},\mathrm{d}W_t
]

with invariant density
[
\pi(x) \propto e^{-V(x)}.
]

---

# Conceptual Summary


A **diffusion process** is:

> A continuous-path Markov semimartingale whose quadratic variation grows linearly in time and is locally determined by the state.

Symbolically:
[
\boxed{
\text{Diffusion}
================

\text{Brownian noise}
+
\text{state-dependent drift}
}
]

---

## Natural Next Steps


We are now ready for deep theory. The most natural continuations are:

1. **Existence and uniqueness of diffusions**
2. **Martingale problem formulation**
3. **Time reversal of diffusions**
4. **Invariant measures and ergodicity**
5. **Diffusion bridges**
6. **Large deviations**

Tell me which direction you want next, and we continue at the same mathematical level.
