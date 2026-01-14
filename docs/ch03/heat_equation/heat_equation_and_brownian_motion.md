# Heat Equation


The heat equation provides the analytical description of Brownian motion.

---

## Transition Density


Let \((B_t)_{t \ge 0}\) be a standard Brownian motion.
Then \(B_t\) has density
\[
p(t,x) = \frac{1}{\sqrt{2\pi t}}
\exp\!\left( -\frac{x^2}{2t} \right),
\]
which is exactly the heat kernel.

Thus, the law of Brownian motion evolves according to the heat equation.

---

## Expectation


For a bounded measurable function \(f\), define
\[
u(t,x) = \mathbb{E}\!\left[ f(x + B_t) \right].
\]

Then \(u\) solves
\[
\partial_t u = \frac12 \partial_{xx} u,
\quad u(0,x) = f(x).
\]

This provides the first example of a **probabilistic representation of PDE solutions**.

---

## Conceptual Bridge


This connection establishes a fundamental principle:

> Diffusion in probability corresponds to diffusion in analysis.

Later chapters will extend this idea to:
- General diffusions (Kolmogorov equations)
- Discounted expectations (Feynman–Kac)
- Pricing PDEs in finance
