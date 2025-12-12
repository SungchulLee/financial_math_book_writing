Let ((\Omega,\mathcal{F},(\mathcal{F}*t)*{t\ge 0},\mathbb{P})) carry an (m)-dimensional Brownian motion (W_t=(W_t^{(1)},\dots,W_t^{(m)})). I’ll state and derive **Itô’s lemma** in the standard (rigorous) way: first for smooth functions of Brownian motion, then for general diffusions.

---

# 1. Itô’s Lemma for (f(t,W_t))

Assume
[
f \in C^{1,2}\bigl([0,T]\times \mathbb{R}^m\bigr),
]
meaning (f) is once continuously differentiable in (t) and twice continuously differentiable in (x).

Define the process
[
Y_t := f(t,W_t).
]

Then **Itô’s lemma** says:
[
\boxed{
\mathrm{d}f(t,W_t)
==================

\frac{\partial f}{\partial t}(t,W_t),\mathrm{d}t
+
\sum_{i=1}^m \frac{\partial f}{\partial x_i}(t,W_t),\mathrm{d}W_t^{(i)}
+
\frac{1}{2}\sum_{i=1}^m \frac{\partial^2 f}{\partial x_i^2}(t,W_t),\mathrm{d}t
}
]

Equivalently (integrated form):
[
\boxed{
f(t,W_t)=f(0,W_0)+\int_0^t \frac{\partial f}{\partial s}(s,W_s),\mathrm{d}s
+\sum_{i=1}^m\int_0^t \frac{\partial f}{\partial x_i}(s,W_s),\mathrm{d}W_s^{(i)}
+\frac{1}{2}\int_0^t \sum_{i=1}^m \frac{\partial^2 f}{\partial x_i^2}(s,W_s),\mathrm{d}s
}
]

For (m=1):
[
\boxed{
\mathrm{d}f(t,W_t)
==================

f_t(t,W_t),\mathrm{d}t
+
f_x(t,W_t),\mathrm{d}W_t
+
\frac{1}{2}f_{xx}(t,W_t),\mathrm{d}t
}
]

---

# 2. Why the Extra (\tfrac{1}{2}f_{xx},\mathrm{d}t) Term Appears

The entire phenomenon comes from the **quadratic variation** of Brownian motion:
[
(W_{t+\Delta}-W_t)^2 \approx \Delta
\quad \text{(in mean / probability as } \Delta\to 0\text{)}
]

Heuristically, in “differential algebra” one uses the rules:
[
(\mathrm{d}t)^2 = 0,\qquad \mathrm{d}t,\mathrm{d}W_t = 0,\qquad (\mathrm{d}W_t)^2 = \mathrm{d}t.
]

Those are not classical calculus rules; they encode quadratic variation.

---

# 3. A Clean Derivation in One Dimension

Let (m=1), (Y_t=f(t,W_t)). Consider a partition (0=t_0<\cdots<t_n=t), and define
[
\Delta t_k = t_{k+1}-t_k,\qquad \Delta W_k = W_{t_{k+1}}-W_{t_k}.
]

Write a second-order Taylor expansion:
[
\begin{aligned}
f(t_{k+1},W_{t_{k+1}})-f(t_k,W_{t_k})
&=
f_t(t_k,W_{t_k}),\Delta t_k
+
f_x(t_k,W_{t_k}),\Delta W_k
\
&\quad
+\frac{1}{2}f_{xx}(t_k,W_{t_k}),(\Delta W_k)^2
+
R_k,
\end{aligned}
]
where the remainder (R_k) contains terms of order:
[
R_k = O\bigl((\Delta t_k)^2\bigr)+O\bigl(\Delta t_k,|\Delta W_k|\bigr)+O\bigl(|\Delta W_k|^3\bigr).
]

Summing over (k) yields
[
f(t,W_t)-f(0,W_0)
=================

\sum_k f_t(\cdot)\Delta t_k
+
\sum_k f_x(\cdot)\Delta W_k
+
\frac{1}{2}\sum_k f_{xx}(\cdot)(\Delta W_k)^2
+
\sum_k R_k.
]

Now use the key limits (as mesh (|\Pi|\to 0)):

1. Riemann sum:
   [
   \sum_k f_t(t_k,W_{t_k}),\Delta t_k
   \to
   \int_0^t f_t(s,W_s),\mathrm{d}s.
   ]

2. Itô integral definition:
   [
   \sum_k f_x(t_k,W_{t_k}),\Delta W_k
   \to
   \int_0^t f_x(s,W_s),\mathrm{d}W_s.
   ]

3. Quadratic variation:
   [
   \sum_k f_{xx}(t_k,W_{t_k}),(\Delta W_k)^2
   \to
   \int_0^t f_{xx}(s,W_s),\mathrm{d}s.
   ]

4. Remainder vanishes in probability (or in (L^2)) because (|\Delta W_k|) is typically of size (\sqrt{\Delta t_k}), so (|\Delta W_k|^3) is of size ((\Delta t_k)^{3/2}), which is summable to (0) as mesh (\to 0).

This yields:
[
f(t,W_t)-f(0,W_0)
=================

\int_0^t f_t(s,W_s),\mathrm{d}s
+
\int_0^t f_x(s,W_s),\mathrm{d}W_s
+
\frac{1}{2}\int_0^t f_{xx}(s,W_s),\mathrm{d}s.
]

---

# 4. General Itô’s Lemma for Diffusions (X_t)

Let (X_t\in\mathbb{R}^d) solve the SDE
[
\boxed{
\mathrm{d}X_t = b(X_t,t),\mathrm{d}t + \sigma(X_t,t),\mathrm{d}W_t,
}
]
where (W_t\in\mathbb{R}^m), (b\in\mathbb{R}^d), (\sigma\in\mathbb{R}^{d\times m}).

Let (f\in C^{1,2}([0,T]\times\mathbb{R}^d)). Then

[
\boxed{
\begin{aligned}
\mathrm{d}f(t,X_t)
&=
\frac{\partial f}{\partial t}(t,X_t),\mathrm{d}t
+
\sum_{i=1}^d \frac{\partial f}{\partial x_i}(t,X_t),\mathrm{d}X_t^{(i)}
\
&\quad
+
\frac{1}{2}\sum_{i,j=1}^d
\frac{\partial^2 f}{\partial x_i\partial x_j}(t,X_t),
\mathrm{d}\langle X^{(i)},X^{(j)}\rangle_t.
\end{aligned}
}
]

Now compute the quadratic covariation:
[
\mathrm{d}\langle X^{(i)},X^{(j)}\rangle_t
==========================================

\bigl(\sigma(X_t,t)\sigma(X_t,t)^\top\bigr)_{ij},\mathrm{d}t.
]

Let
[
a(x,t) := \sigma(x,t)\sigma(x,t)^\top \in \mathbb{R}^{d\times d}.
]

Substitute (\mathrm{d}X_t = b,\mathrm{d}t + \sigma,\mathrm{d}W_t) to get the standard compact form:

[
\boxed{
\mathrm{d}f(t,X_t)
==================

\left(
\frac{\partial f}{\partial t}(t,X_t)
+
\nabla f(t,X_t)^\top b(X_t,t)
+
\frac{1}{2}\operatorname{Tr}!\bigl(a(X_t,t)\nabla^2 f(t,X_t)\bigr)
\right)\mathrm{d}t
+
\nabla f(t,X_t)^\top \sigma(X_t,t),\mathrm{d}W_t
}
]

---

# 5. Two Classic Examples (Quick but Deep)

### Example 1: (f(x)=x^2), (X_t=W_t)

Here (f'(x)=2x), (f''(x)=2). Itô:
[
\mathrm{d}(W_t^2) = 2W_t,\mathrm{d}W_t + \mathrm{d}t.
]
So
[
W_t^2 - t \text{ is a martingale.}
]

### Example 2: (f(x)=e^{\lambda x}), (X_t=W_t)

(f'(x)=\lambda e^{\lambda x}), (f''(x)=\lambda^2 e^{\lambda x}). Then
[
\mathrm{d}\bigl(e^{\lambda W_t}\bigr)
=====================================

\lambda e^{\lambda W_t},\mathrm{d}W_t
+
\frac{1}{2}\lambda^2 e^{\lambda W_t},\mathrm{d}t.
]
Hence
[
\exp\left(\lambda W_t - \frac{1}{2}\lambda^2 t\right)
]
is a martingale.

---

# 6. Where Itô’s Lemma Fits in the Big Picture

Itô’s lemma is exactly the statement that the **generator**
[
\mathcal{L}f(x,t)
=================

\nabla f(x,t)^\top b(x,t)
+
\frac{1}{2}\operatorname{Tr}!\bigl(a(x,t)\nabla^2 f(x,t)\bigr)
]
controls the drift of (f(t,X_t)).

That is,
[
f(t,X_t) - f(0,X_0) - \int_0^t \left(\frac{\partial f}{\partial s} + \mathcal{L}f\right)(s,X_s),\mathrm{d}s
]
is a martingale.

---

If you tell me what level you want next, we can go in a few directions immediately:

* a fully detailed proof using (L^2) convergence and localization
* Itô’s lemma for **semimartingales**
* the **multidimensional** version with index notation
* the **Stratonovich** chain rule and conversion formula
