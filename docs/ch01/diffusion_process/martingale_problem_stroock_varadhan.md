# Martingale Problem (Stroock–Varadhan)

The martingale problem defines a diffusion **via its generator** and is fundamental for uniqueness in law and weak convergence.

---

## Generator

Let \(b:\mathbb{R}^d\to\mathbb{R}^d\) and \(a:\mathbb{R}^d\to\mathbb{R}^{d\times d}\) (symmetric, nonnegative definite). Define
\[
\boxed{
(\mathcal{L}f)(x)
=
b^{i}(x)\,\frac{\partial f}{\partial x_i}(x)
+
\frac{1}{2}a^{ij}(x)\,\frac{\partial^2 f}{\partial x_i\partial x_j}(x),
}
\]
for \(f\in C_c^\infty(\mathbb{R}^d)\).

---

## Martingale Problem

Fix an initial law \(\mu\) on \(\mathbb{R}^d\). A probability measure \(\mathbb{P}\) on \(C([0,\infty);\mathbb{R}^d)\) solves the martingale problem for \((\mathcal{L},\mu)\) if

1. \(X_0\sim \mu\) under \(\mathbb{P}\),
2. for every \(f\in C_c^\infty(\mathbb{R}^d)\),
\[
\boxed{
M_t^{f}
:=
f(X_t)-f(X_0)-\int_0^t (\mathcal{L}f)(X_s)\,\mathrm{d}s
}
\]
is a martingale w.r.t. \(\mathcal{F}_t=\sigma(X_s:0\le s\le t)\).

---

## Relation to SDEs

If \(X_t\) solves
\[
\mathrm{d}X_t^{i}=b^{i}(X_t)\,\mathrm{d}t+\sigma^{i\alpha}(X_t)\,\mathrm{d}W_t^\alpha,
\quad a^{ij}=\sigma^{i\alpha}\sigma^{j\alpha},
\]
then Itô’s formula implies \(M_t^{f}\) is a (local) martingale, hence \(X\) solves the martingale problem (with suitable integrability).

Under regularity assumptions, well-posedness of the martingale problem is equivalent to uniqueness in law for the SDE.

---

## What to Remember

- Martingale problem: “\(f(X_t)-\int_0^t\mathcal{L}f(X_s)\,\mathrm{d}s\) is a martingale for all test \(f\)”.
- This defines the diffusion through \(\mathcal{L}\), independent of a chosen Brownian motion.
