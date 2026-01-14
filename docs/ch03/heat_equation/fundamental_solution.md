# Fundamental Solution


The heat equation admits an explicit fundamental solution, also called the **heat kernel**.

---

## Heat Kernel


The fundamental solution is
\[
G(t,x) = \frac{1}{\sqrt{2\pi t}}
\exp\!\left( -\frac{x^2}{2t} \right),
\quad t > 0.
\]

This function satisfies:
- \( \partial_t G = \tfrac12 \partial_{xx} G \)
- \( \lim_{t \downarrow 0} G(t,\cdot) = \delta_0 \) (in the distributional sense)

---

## Solution via


For an initial condition \(u(0,x) = f(x)\), the solution is given by
\[
u(t,x) = \int_{\mathbb{R}} G(t, x-y)\,f(y)\,dy.
\]

This representation shows explicitly:
- Smoothing of \(f\)
- Averaging with Gaussian weights
- Diffusion over time

---

## Regularity


If \(f\) is bounded or integrable, then:
- \(u(t,\cdot)\) is infinitely differentiable for all \(t>0\)
- If \(f \ge 0\), then \(u(t,\cdot) \ge 0\)

These properties will later justify probabilistic representations of solutions.
