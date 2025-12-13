Perfect.
We now enter the **core technical heart** of diffusion theory.

Below is a **rigorous, math-first development of stochastic integration**, starting from motivation and ending with Itô’s isometry and extensions — **no code**, **full LaTeX**, and precise logic.

---

# 1. Why Ordinary Integration Fails

Let ({W_t}_{t \ge 0}) be Brownian motion.

A naïve attempt would define
[
\int_0^T f(t),\mathrm{d}W_t
]
as a Riemann–Stieltjes integral.

❌ This fails because Brownian paths have **infinite total variation** almost surely:
[
\sup_{\Pi} \sum_k |W_{t_k}-W_{t_{k-1}}| = \infty
]

Hence, classical pathwise integration does **not** apply.

---

# 2. Philosophy of Stochastic Integration

Key idea:

> Define the integral **as a random variable**, not pathwise.

We replace pathwise limits by **limits in probability or in (L^2(\Omega))**.

---

# 3. Step Processes (Building Blocks)

Let (0 = t_0 < t_1 < \cdots < t_n = T).

A **simple (step) process** is
[
H_t(\omega)
===========

\sum_{k=0}^{n-1}
H_k(\omega),\mathbf{1}*{(t_k,t*{k+1}]}(t)
]

where:

* (H_k) is (\mathcal{F}_{t_k})-measurable
* (\mathbb{E}[H_k^2] < \infty)

---

# 4. Definition of the Itô Integral (Step Processes)

For a step process (H_t), define
[
\boxed{
\int_0^T H_t,\mathrm{d}W_t
:=
\sum_{k=0}^{n-1}
H_k
\bigl(W_{t_{k+1}} - W_{t_k}\bigr)
}
]

This is a **finite sum of random variables**, hence well-defined.

---

# 5. Linearity and Mean Zero

Linearity:
[
\int_0^T (aH_t + bG_t),\mathrm{d}W_t
====================================

a\int_0^T H_t,\mathrm{d}W_t
+
b\int_0^T G_t,\mathrm{d}W_t
]

Expectation:
[
\boxed{
\mathbb{E}\left[\int_0^T H_t,\mathrm{d}W_t\right] = 0
}
]

because increments of Brownian motion have mean zero and are independent of the past.

---

# 6. Itô Isometry (Fundamental Theorem)

For step processes:
[
\boxed{
\mathbb{E}\left[
\left(
\int_0^T H_t,\mathrm{d}W_t
\right)^2
\right]
=======

\mathbb{E}\left[
\int_0^T H_t^2,\mathrm{d}t
\right]
}
]

### Proof Sketch

[
\begin{aligned}
\mathbb{E}\left[\left(\sum_k H_k \Delta W_k\right)^2\right]
&=
\sum_k \mathbb{E}[H_k^2]\mathbb{E}[(\Delta W_k)^2]
\
&=
\sum_k \mathbb{E}[H_k^2](t_{k+1}-t_k)
\end{aligned}
]

Cross terms vanish due to independence.

---

# 7. Extension to General Integrands

Define the space
[
\boxed{
\mathcal{H}^2
=============

\left{
H_t \text{ adapted} :
\mathbb{E}\left[\int_0^T H_t^2,\mathrm{d}t\right] < \infty
\right}
}
]

Step processes are **dense** in (\mathcal{H}^2).

Hence, for (H \in \mathcal{H}^2), define
[
\int_0^T H_t,\mathrm{d}W_t
==========================

L^2\text{-}\lim_{n \to \infty}
\int_0^T H_t^{(n)},\mathrm{d}W_t
]

where (H^{(n)}) are step approximations.

---

# 8. Martingale Property

For (H \in \mathcal{H}^2),
[
\boxed{
M_t := \int_0^t H_s,\mathrm{d}W_s
}
]
is a martingale.

Moreover,
[
\langle M \rangle_t = \int_0^t H_s^2,\mathrm{d}s
]

---

# 9. Quadratic Variation Revisited

Let
[
M_t = \int_0^t H_s,\mathrm{d}W_s
]

Then:
[
\boxed{
[M]_t
=====

\int_0^t H_s^2,\mathrm{d}s
}
]

This shows stochastic integrals inherit Brownian roughness.

---

# 10. Why Left-End Points Matter (Itô vs Stratonovich)

Definition uses **left endpoints**:
[
H_k = H_{t_k}
]

This choice ensures:

* Adaptedness
* Martingale property
* Itô isometry

Other choices lead to **different integrals**.

---

# 11. Stratonovich Integral (Brief Contrast)

Define:
[
\int_0^T H_t \circ \mathrm{d}W_t
================================

\lim_{|\Pi| \to 0}
\sum_k
H_{\frac{t_k+t_{k+1}}{2}}
\bigl(W_{t_{k+1}}-W_{t_k}\bigr)
]

Relation:
[
\boxed{
\int_0^T H_t \circ \mathrm{d}W_t
================================

\int_0^T H_t,\mathrm{d}W_t
+
\frac{1}{2}
\int_0^T \frac{\mathrm{d}H_t}{\mathrm{d}W_t},\mathrm{d}t
}
]

---

# 12. Integration with Respect to Time

Contrast:
[
\int_0^T H_t,\mathrm{d}t
\quad \text{vs} \quad
\int_0^T H_t,\mathrm{d}W_t
]

Key difference:
[
\mathbb{E}\left[\int_0^T H_t,\mathrm{d}W_t\right] = 0
\quad
\text{but}
\quad
\mathbb{E}\left[\int_0^T H_t,\mathrm{d}t\right] \neq 0
]

---

# 13. Isometry as Geometry

The mapping
[
H \mapsto \int_0^T H_t,\mathrm{d}W_t
]
is an **isometry**:
[
L^2([0,T]\times\Omega)
\longrightarrow
L^2(\Omega)
]

This gives stochastic integration a **Hilbert space structure**.

---

# 14. Where This Leads

Stochastic integration enables:

1. **Itô’s formula**
2. **Stochastic differential equations**
3. **Girsanov theorem**
4. **Local time**
5. **Diffusion processes**
6. **Modern diffusion models (score-based)**

---

## Next Natural Step

We are now perfectly positioned to study:

* **Itô’s formula (full derivation)**
* **Stochastic differential equations**
* **Martingale representation theorem**
* **Local time & Tanaka formula**

Tell me which one you want next — and we continue at the same mathematical depth.
