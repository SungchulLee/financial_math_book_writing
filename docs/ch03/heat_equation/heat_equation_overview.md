# Heat Equation Overview

The heat equation is the canonical partial differential equation describing diffusion.
It plays a central role in probability theory, stochastic processes, and mathematical finance.

In one spatial dimension, the heat equation is given by
\[
\partial_t u(t,x) = \frac{1}{2}\,\partial_{xx} u(t,x),
\quad (t,x) \in (0,\infty) \times \mathbb{R},
\]
together with an initial condition
\[
u(0,x) = f(x).
\]

Here, \(u(t,x)\) represents the temperature (or mass, or probability density) at time \(t\)
and position \(x\).

---

## Diffusive Nature

The heat equation is **parabolic**, reflecting irreversible spreading over time.
Unlike hyperbolic equations, information propagates instantaneously and solutions become
smooth for any positive time.

Key qualitative properties:
- Smoothing of initial data
- Conservation of total mass
- Positivity preservation

These features mirror the behavior of Brownian motion.

---

## Why the Factor \( \tfrac12 \)?

The coefficient \( \tfrac12 \) is chosen to align the equation with standard Brownian motion,
whose variance satisfies
\[
\mathbb{E}[B_t^2] = t.
\]

With this normalization, the heat equation becomes the PDE counterpart of Brownian diffusion,
which will be made precise later.
