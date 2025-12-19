# Dynkin’s Formula

Dynkin’s formula expresses expectations of functionals of a diffusion
in terms of its infinitesimal generator.

## Statement

Let \(X_t\) solve

\[
dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t,
\]


and let \(f\in C^2\).

For a stopping time \(\tau\),

\[
\boxed{
\mathbb E_x[f(X_\tau)]
=
f(x) + \mathbb E_x\!\left[\int_0^\tau Lf(X_s)\,ds\right]
}
\]



provided

\[
\mathbb E_x\!\left[\int_0^\tau |Lf(X_s)|\,ds\right] < \infty.
\]



## Proof (Itô’s Formula)

[Your full proof here, unchanged]

## Intuition

Dynkin’s formula is a **stochastic fundamental theorem of calculus**:
- \(f(x)\): initial value
- \(Lf\): instantaneous expected drift of \(f(X_t)\)
