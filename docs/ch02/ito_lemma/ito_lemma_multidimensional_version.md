Let (W_t = (W_t^{1},\dots,W_t^{m})) be an (m)-dimensional Brownian motion and (X_t=(X_t^{1},\dots,X_t^{d})) an (\mathbb{R}^d)-valued diffusion solving (Einstein summation convention throughout)

[
\boxed{
\mathrm{d}X_t^{i} = b^{i}(t,X_t),\mathrm{d}t + \sigma^{i\alpha}(t,X_t),\mathrm{d}W_t^{\alpha},
\qquad i=1,\dots,d,\ \alpha=1,\dots,m.
}
]

Let (f:[0,T]\times\mathbb{R}^d\to\mathbb{R}) be (C^{1,2}) (once in (t), twice in (x)). Define (Y_t = f(t,X_t)). Then the **multidimensional Itô formula in index notation** is

[
\boxed{
\mathrm{d}f(t,X_t)
==================

\frac{\partial f}{\partial t}(t,X_t),\mathrm{d}t
+
\frac{\partial f}{\partial x_i}(t,X_t),\mathrm{d}X_t^{i}
+
\frac{1}{2}\frac{\partial^2 f}{\partial x_i\partial x_j}(t,X_t),\mathrm{d}\langle X^{i},X^{j}\rangle_t.
}
]

Now compute the quadratic covariation term. Since

[
\mathrm{d}X_t^{i} = b^{i},\mathrm{d}t + \sigma^{i\alpha},\mathrm{d}W_t^{\alpha},
]

only the Brownian parts contribute to quadratic variation, and using

[
\mathrm{d}\langle W^{\alpha}, W^{\beta}\rangle_t = \delta^{\alpha\beta},\mathrm{d}t,
]

we get

[
\boxed{
\mathrm{d}\langle X^{i},X^{j}\rangle_t
======================================

# \sigma^{i\alpha}(t,X_t)\sigma^{j\beta}(t,X_t),\mathrm{d}\langle W^{\alpha},W^{\beta}\rangle_t


\sigma^{i\alpha}(t,X_t)\sigma^{j\alpha}(t,X_t),\mathrm{d}t.
}
]

Substitute back and also substitute (\mathrm{d}X_t^{i}) explicitly:

[
\begin{aligned}
\mathrm{d}f(t,X_t)
&=
f_t(t,X_t),\mathrm{d}t
+
f_i(t,X_t)\left(b^{i}(t,X_t),\mathrm{d}t + \sigma^{i\alpha}(t,X_t),\mathrm{d}W_t^{\alpha}\right)
\
&\quad
+
\frac{1}{2} f_{ij}(t,X_t),\sigma^{i\alpha}(t,X_t)\sigma^{j\alpha}(t,X_t),\mathrm{d}t,
\end{aligned}
]
where I use the standard shorthand
[
f_t = \frac{\partial f}{\partial t},\qquad
f_i = \frac{\partial f}{\partial x_i},\qquad
f_{ij} = \frac{\partial^2 f}{\partial x_i\partial x_j}.
]

Collecting (\mathrm{d}t) and (\mathrm{d}W) terms gives the most common index form:

[
\boxed{
\mathrm{d}f(t,X_t)
==================

\left(
f_t(t,X_t)
+
b^{i}(t,X_t),f_i(t,X_t)
+
\frac{1}{2}\sigma^{i\alpha}(t,X_t)\sigma^{j\alpha}(t,X_t),f_{ij}(t,X_t)
\right)\mathrm{d}t
+
\sigma^{i\alpha}(t,X_t),f_i(t,X_t),\mathrm{d}W_t^{\alpha}.
}
]

---

## Generator in Index Notation


Define
[
a^{ij}(t,x) := \sigma^{i\alpha}(t,x)\sigma^{j\alpha}(t,x).
]

Then the (time-dependent) generator (\mathcal{L}) acting on (f) is

[
\boxed{
(\mathcal{L}f)(t,x)
===================

b^{i}(t,x), \frac{\partial f}{\partial x_i}(t,x)
+
\frac{1}{2}a^{ij}(t,x),\frac{\partial^2 f}{\partial x_i\partial x_j}(t,x).
}
]

So Itô can be written compactly as
[
\boxed{
\mathrm{d}f(t,X_t)
==================

\left(f_t + \mathcal{L}f\right)(t,X_t),\mathrm{d}t
+
\frac{\partial f}{\partial x_i}(t,X_t)\sigma^{i\alpha}(t,X_t),\mathrm{d}W_t^{\alpha}.
}
]

---

## Vector-Valued Version (Optional but Often Used)


If (f:[0,T]\times\mathbb{R}^d\to\mathbb{R}^k) with components (f^r) ((r=1,\dots,k)), apply the scalar formula componentwise:

[
\boxed{
\mathrm{d}f^{r}(t,X_t)
======================

\left(
\frac{\partial f^{r}}{\partial t}
+
b^{i}\frac{\partial f^{r}}{\partial x_i}
+
\frac{1}{2}a^{ij}\frac{\partial^2 f^{r}}{\partial x_i\partial x_j}
\right)\mathrm{d}t
+
\sigma^{i\alpha}\frac{\partial f^{r}}{\partial x_i},\mathrm{d}W_t^{\alpha}.
}
]

---

If you want, the next very natural step is to write the **Itô product rule** and **Itô formula for (f(X_t)) with (X_t) itself a semimartingale**, still in index notation (that’s where (\mathrm{d}\langle \cdot,\cdot\rangle) bookkeeping becomes really powerful).
