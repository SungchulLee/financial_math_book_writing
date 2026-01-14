# Small Noise and Large Deviations


Consider the small-noise diffusion on \([0,T]\):

\[
\boxed{
\mathrm{d}X_t^\varepsilon
=
b(X_t^\varepsilon)\,\mathrm{d}t
+
\sqrt{\varepsilon}\,\sigma(X_t^\varepsilon)\,\mathrm{d}W_t,
\qquad X_0^\varepsilon=x_0.
}
\]


As \(\varepsilon\downarrow 0\), \(X^\varepsilon\) concentrates near the ODE solution

\[
\boxed{
\dot{\bar{x}}(t)=b(\bar{x}(t)),\qquad \bar{x}(0)=x_0.
}
\]



Large deviations quantify exponentially small probabilities of atypical paths.

---

## Path-Space Rate Function (Freidlin–Wentzell)


Let \(\phi\in C([0,T];\mathbb{R}^d)\). If \(\phi\) is absolutely continuous and \(\sigma(\phi(t))\) is invertible, define

\[
\boxed{
I_{0,T}(\phi)
=
\frac{1}{2}\int_0^T
\left\|
\sigma(\phi(t))^{-1}\bigl(\dot{\phi}(t)-b(\phi(t))\bigr)
\right\|^2\,\mathrm{d}t,
}
\]


and set \(I_{0,T}(\phi)=+\infty\) otherwise.

Equivalently, using a control \(u\in L^2([0,T];\mathbb{R}^m)\) with

\[
\dot{\phi}(t)=b(\phi(t))+\sigma(\phi(t))u(t),
\]


we have

\[
\boxed{
I_{0,T}(\phi)=\frac{1}{2}\int_0^T \|u(t)\|^2\,\mathrm{d}t.
}
\]



---

## LDP Heuristic


For a set \(A\) of paths,

\[
\boxed{
\mathbb{P}(X^\varepsilon \in A)
\approx
\exp\!\left(
-\frac{1}{\varepsilon}\inf_{\phi\in A} I_{0,T}(\phi)
\right)
\quad (\varepsilon\downarrow 0).
}
\]


Thus, rare events occur along paths minimizing \(I_{0,T}\) under constraints (“most likely path”).

---

## Hamilton–Jacobi Orientation


With \(a(x)=\sigma(x)\sigma(x)^\top\), define the Hamiltonian

\[
H(x,p)=b(x)\cdot p+\frac{1}{2}p^\top a(x)p.
\]


Large deviations are closely tied to Hamilton–Jacobi equations of the form

\[
\frac{\partial V}{\partial t}+H(x,\nabla V)=0,
\]


in contrast to diffusion expectations, which satisfy linear Kolmogorov equations.

---

## What to Remember


- Small-noise diffusions satisfy a path-space LDP with speed \(\varepsilon\).
- The rate function is an action measuring the energy needed to force a path.
- Large deviations connect stochastic dynamics to nonlinear PDE (Hamilton–Jacobi).
