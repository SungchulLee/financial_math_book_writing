Let (X_t) and (Y_t) be (real-valued) **Itô processes**:
[
\mathrm{d}X_t = a_t,\mathrm{d}t + b_t^{\alpha},\mathrm{d}W_t^{\alpha},
\qquad
\mathrm{d}Y_t = c_t,\mathrm{d}t + d_t^{\alpha},\mathrm{d}W_t^{\alpha},
]
with Einstein summation over (\alpha=1,\dots,m). Assume the usual integrability so all terms make sense.

---

## Quadratic Covariation


The quadratic covariation is
[
\boxed{
\mathrm{d}\langle X, Y\rangle_t = b_t^{\alpha} d_t^{\alpha},\mathrm{d}t.
}
]
This comes from (\mathrm{d}\langle W^{\alpha},W^{\beta}\rangle_t=\delta^{\alpha\beta}\mathrm{d}t) and the fact that (\mathrm{d}t)-terms have zero quadratic variation.

---

## Itô Product Rule


The **Itô product rule** is
[
\boxed{
\mathrm{d}(X_t Y_t)
===================

X_t,\mathrm{d}Y_t
+
Y_t,\mathrm{d}X_t
+
\mathrm{d}\langle X, Y\rangle_t.
}
]

Substituting the SDEs:
[
\boxed{
\mathrm{d}(X_t Y_t)
===================

\bigl(X_t c_t + Y_t a_t + b_t^{\alpha} d_t^{\alpha}\bigr),\mathrm{d}t
+
\bigl(X_t d_t^{\alpha} + Y_t b_t^{\alpha}\bigr),\mathrm{d}W_t^{\alpha}.
}
]

---

## “Differential Multiplication Table” (Useful Heuristic)


This rule is exactly what you get if you expand
[
\mathrm{d}(XY) = (X+\mathrm{d}X)(Y+\mathrm{d}Y)-XY
]
and keep terms up to order (\mathrm{d}t), using
[
(\mathrm{d}t)^2=0,\qquad \mathrm{d}t,\mathrm{d}W_t^{\alpha}=0,\qquad
\mathrm{d}W_t^{\alpha},\mathrm{d}W_t^{\beta}=\delta^{\alpha\beta},\mathrm{d}t.
]
Then
[
\mathrm{d}X_t,\mathrm{d}Y_t
===========================

# (b_t^{\alpha},\mathrm{d}W_t^{\alpha})(d_t^{\beta},\mathrm{d}W_t^{\beta})


# b_t^{\alpha}d_t^{\beta}\delta^{\alpha\beta},\mathrm{d}t


b_t^{\alpha}d_t^{\alpha},\mathrm{d}t,
]
which matches (\mathrm{d}\langle X,Y\rangle_t).

---

## Common Special Cases


### 1. (a) Square / Itô formula for (X_t^2)


Take (Y_t=X_t):
[
\boxed{
\mathrm{d}(X_t^2) = 2X_t,\mathrm{d}X_t + \mathrm{d}\langle X\rangle_t
}
]
and since (\mathrm{d}\langle X\rangle_t = b_t^{\alpha}b_t^{\alpha},\mathrm{d}t),
[
\boxed{
\mathrm{d}(X_t^2)
=================

\left(2X_t a_t + b_t^{\alpha}b_t^{\alpha}\right)\mathrm{d}t
+
2X_t b_t^{\alpha},\mathrm{d}W_t^{\alpha}.
}
]

### 2. (b) Product of vector Itô processes (index form)


Let (X_t^{i},Y_t^{j}) satisfy
[
\mathrm{d}X_t^{i}=a_t^{i}\mathrm{d}t+b_t^{i\alpha}\mathrm{d}W_t^{\alpha},
\qquad
\mathrm{d}Y_t^{j}=c_t^{j}\mathrm{d}t+d_t^{j\alpha}\mathrm{d}W_t^{\alpha}.
]
Then
[
\boxed{
\mathrm{d}(X_t^{i}Y_t^{j})
==========================

X_t^{i},\mathrm{d}Y_t^{j}
+
Y_t^{j},\mathrm{d}X_t^{i}
+
\mathrm{d}\langle X^{i},Y^{j}\rangle_t,
\qquad
\mathrm{d}\langle X^{i},Y^{j}\rangle_t=b_t^{i\alpha}d_t^{j\alpha}\mathrm{d}t.
}
]

---

If you want the next piece that naturally follows: the **Itô quotient rule** for (\mathrm{d}!\left(\frac{X_t}{Y_t}\right)) (with conditions (Y_t\neq 0)), still in clean index notation.
