# Itô’s Lemma

Itô’s lemma is the stochastic analogue of the classical chain rule. Conceptually, it arises from a second-order Taylor expansion in which quadratic variation forces certain second-order terms to survive.

---

## 1. Quadratic Approximation and Box Calculus

For a smooth function \(f(t,b)\), the second-order Taylor expansion is

\[
df
= f_t\,dt + f_b\,db
+ \frac12 f_{tt}(dt)^2
+ \frac12 f_{bb}(db)^2
+ f_{tb}(dt)(db).
\]

For Brownian motion \(b = B_t\), the differentials satisfy the Itô rules

\[
(dt)^2 = 0, \qquad dt\,dB = 0, \qquad (dB)^2 = dt.
\]

These rules may be summarized by the box calculus:

\[
\begin{array}{|c|c|c|}
\hline
 & dt & dB \\
\hline
dt & 0 & 0 \\
\hline
dB & 0 & dt \\
\hline
\end{array}
\]

---

## 2. Differential Form of Itô’s Lemma

Applying the box rules yields

\[
df
= f_t\,dt + f_b\,dB + \frac12 f_{bb}\,dt.
\]

---

## 3. Integrated Form (Itô’s Lemma)

Let \(B_t\) be Brownian motion and \(f \in C^{1,2}\). Then

\[
\boxed{
f(t,B_t) - f(0,B_0)
=
\int_0^t f_t(s,B_s)\,ds
+ \int_0^t f_b(s,B_s)\,dB_s
+ \frac12 \int_0^t f_{bb}(s,B_s)\,ds
}
\]

---

## 4. Interpretation

- The first and third terms are ordinary (Lebesgue) integrals.
- The middle term is an Itô integral.
- The extra drift term arises from quadratic variation.

Itô’s lemma is thus the honest Taylor expansion for Brownian motion.
