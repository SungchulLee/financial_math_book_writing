Let (X_t) and (Y_t) be real-valued Itô processes
[
\mathrm{d}X_t = a_t,\mathrm{d}t + b_t^{\alpha},\mathrm{d}W_t^{\alpha},
\qquad
\mathrm{d}Y_t = c_t,\mathrm{d}t + d_t^{\alpha},\mathrm{d}W_t^{\alpha},
]
with Einstein summation over (\alpha=1,\dots,m). Assume (Y_t \neq 0) (almost surely for all (t) on the interval of interest) and the usual integrability.

Define
[
Z_t := \frac{X_t}{Y_t}.
]

---

# Two Equivalent Forms of the Itô Quotient Rule


## Form A (product rule + inverse rule)


Use (Z_t = X_t \cdot (Y_t^{-1})). Then
[
\mathrm{d}Z_t
=============

\frac{1}{Y_t},\mathrm{d}X_t
+
X_t,\mathrm{d}(Y_t^{-1})
+
\mathrm{d}\langle X, Y^{-1}\rangle_t.
]
So we need (\mathrm{d}(Y_t^{-1})) and (\mathrm{d}\langle X, Y^{-1}\rangle_t).

### 1. Inverse rule


Apply Itô to (g(y)=y^{-1}):
[
g'(y) = -y^{-2},\qquad g''(y)=2y^{-3}.
]
Since (\mathrm{d}\langle Y\rangle_t = d_t^{\alpha}d_t^{\alpha},\mathrm{d}t),
[
\boxed{
\mathrm{d}(Y_t^{-1})
====================

-\frac{1}{Y_t^{2}},\mathrm{d}Y_t
+
\frac{1}{Y_t^{3}},\mathrm{d}\langle Y\rangle_t
==============================================

-\frac{c_t}{Y_t^{2}},\mathrm{d}t
-\frac{d_t^{\alpha}}{Y_t^{2}},\mathrm{d}W_t^{\alpha}
+\frac{d_t^{\alpha}d_t^{\alpha}}{Y_t^{3}},\mathrm{d}t
}
]

### 2. Cross-variation term


The diffusion coefficient of (Y_t^{-1}) is (-d_t^{\alpha}/Y_t^{2}). Hence
[
\boxed{
\mathrm{d}\langle X, Y^{-1}\rangle_t
====================================

# b_t^{\alpha}\left(-\frac{d_t^{\alpha}}{Y_t^{2}}\right)\mathrm{d}t


-\frac{b_t^{\alpha}d_t^{\alpha}}{Y_t^{2}},\mathrm{d}t
}
]

Putting it together gives the quotient rule below.

---

## Form B (final quotient rule, expanded)


Substituting (\mathrm{d}X_t), (\mathrm{d}Y_t) and collecting terms:

[
\boxed{
\mathrm{d}!\left(\frac{X_t}{Y_t}\right)
=======================================

\left(
\frac{a_t}{Y_t}
---------------

## \frac{X_t c_t}{Y_t^{2}}


\frac{b_t^{\alpha} d_t^{\alpha}}{Y_t^{2}}
+
\frac{X_t, d_t^{\alpha} d_t^{\alpha}}{Y_t^{3}}
\right)\mathrm{d}t
+
\left(
\frac{b_t^{\alpha}}{Y_t}
------------------------

\frac{X_t d_t^{\alpha}}{Y_t^{2}}
\right)\mathrm{d}W_t^{\alpha}
}
]

That is the **Itô quotient rule** in index notation.

---

# A Compact “Differential Algebra” Version


Using the Itô multiplication table
[
\mathrm{d}W_t^{\alpha},\mathrm{d}W_t^{\beta}=\delta^{\alpha\beta},\mathrm{d}t,\qquad
\mathrm{d}t,\mathrm{d}W_t^{\alpha}=0,\qquad
(\mathrm{d}t)^2=0,
]
one may remember the quotient rule as:
[
\boxed{
\mathrm{d}!\left(\frac{X}{Y}\right)
===================================

## \frac{1}{Y},\mathrm{d}X


\frac{X}{Y^{2}},\mathrm{d}Y
+
\frac{X}{Y^{3}},\mathrm{d}\langle Y\rangle
------------------------------------------

\frac{1}{Y^{2}},\mathrm{d}\langle X,Y\rangle
}
]
and then substitute
[
\mathrm{d}\langle Y\rangle_t = d_t^{\alpha}d_t^{\alpha},\mathrm{d}t,
\qquad
\mathrm{d}\langle X,Y\rangle_t = b_t^{\alpha}d_t^{\alpha},\mathrm{d}t.
]

---

# Quick Consistency Check (Simple Case)


If (Y_t) has **no Brownian part**, i.e. (d_t^{\alpha}=0), then the rule reduces to the classical-looking one:
[
\mathrm{d}!\left(\frac{X_t}{Y_t}\right)
=======================================

\left(\frac{a_t}{Y_t}-\frac{X_t c_t}{Y_t^2}\right)\mathrm{d}t
+
\frac{b_t^{\alpha}}{Y_t},\mathrm{d}W_t^{\alpha},
]
which matches what you’d expect since there is no quadratic-variation correction from (Y_t).

---

If you want, next we can do the **integration by parts** identity for semimartingales (the most general form of product/quotient logic), or apply the quotient rule to derive classic martingales like (\exp(\lambda W_t - \tfrac{1}{2}\lambda^2 t)) or to derive Girsanov-type likelihood ratios.
