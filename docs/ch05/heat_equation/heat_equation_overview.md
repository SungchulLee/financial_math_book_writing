# The Heat Equation

The heat equation is the canonical partial differential equation describing diffusion. It plays a central role in probability theory, stochastic processes, and mathematical finance, serving as the prototype for all parabolic PDEs.

---

## The Equation

In one spatial dimension, the heat equation is:

$$
\boxed{
\frac{\partial u}{\partial t}(t,x) = \frac{1}{2}\frac{\partial^2 u}{\partial x^2}(t,x), \quad (t,x) \in (0,\infty) \times \mathbb{R}
}
$$

with initial condition:

$$
u(0,x) = f(x)
$$

Here $u(t,x)$ represents:
- **Physics**: Temperature at position $x$ and time $t$
- **Probability**: Density of particles diffusing from initial distribution $f$
- **Finance**: Value function for certain derivative contracts

---

## Why the Factor $\frac{1}{2}$?

The coefficient $\frac{1}{2}$ is chosen to align with **standard Brownian motion**, whose variance satisfies:

$$
\text{Var}(B_t) = \mathbb{E}[B_t^2] = t
$$

With this normalization:
- The heat kernel equals the density of $B_t$
- The generator of Brownian motion is $\mathcal{L} = \frac{1}{2}\frac{\partial^2}{\partial x^2}$
- Feynman-Kac formulas take their simplest form

**Alternative convention**: Physics texts often write $u_t = \kappa u_{xx}$ where $\kappa$ is the thermal diffusivity. Setting $\kappa = \frac{1}{2}$ gives our normalization.

---

## Physical Derivation

The heat equation arises from two physical principles:

**1. Conservation of energy**: 
$$
\frac{\partial u}{\partial t} = -\frac{\partial q}{\partial x}
$$
where $q$ is the heat flux.

**2. Fourier's law**: Heat flows from hot to cold proportionally to the temperature gradient:
$$
q = -\kappa \frac{\partial u}{\partial x}
$$

Combining these:
$$
\frac{\partial u}{\partial t} = \kappa \frac{\partial^2 u}{\partial x^2}
$$

---

## Classification: Parabolic PDEs

The heat equation is the prototype of **parabolic** PDEs.

**General second-order linear PDE**:
$$
Au_{xx} + 2Bu_{xy} + Cu_{yy} + \text{lower order} = 0
$$

**Classification** (by discriminant $B^2 - AC$):

| Type | Condition | Example | Behavior |
|------|-----------|---------|----------|
| Elliptic | $B^2 - AC < 0$ | Laplace: $u_{xx} + u_{yy} = 0$ | Equilibrium |
| Parabolic | $B^2 - AC = 0$ | Heat: $u_t = u_{xx}$ | Diffusion |
| Hyperbolic | $B^2 - AC > 0$ | Wave: $u_{tt} = u_{xx}$ | Propagation |

---

## Key Qualitative Properties

### 1. Smoothing (Regularization)

Even if the initial data $f$ is rough (e.g., discontinuous), the solution $u(t,\cdot)$ becomes **infinitely differentiable** for any $t > 0$.

**Intuition**: Diffusion averages out irregularities.

### 2. Infinite Speed of Propagation

If $f$ has compact support, $u(t,x) > 0$ for all $x \in \mathbb{R}$ and $t > 0$.

**Contrast with wave equation**: Information travels at finite speed for hyperbolic equations.

### 3. Conservation of Mass

If $\int_{\mathbb{R}} f(x)\,dx = M$, then:
$$
\int_{\mathbb{R}} u(t,x)\,dx = M \quad \text{for all } t > 0
$$

Total "heat" (or probability mass) is conserved.

### 4. Positivity Preservation

If $f(x) \geq 0$ for all $x$, then $u(t,x) \geq 0$ for all $t > 0$ and $x \in \mathbb{R}$.

**Probabilistic meaning**: Densities remain non-negative.

### 5. Decay of Maximum

$$
\max_x u(t,x) \leq \max_x f(x)
$$

The maximum temperature decreases over time (in the absence of sources).

---

## The Heat Equation in Higher Dimensions

In $\mathbb{R}^d$:

$$
\frac{\partial u}{\partial t} = \frac{1}{2}\Delta u = \frac{1}{2}\sum_{i=1}^d \frac{\partial^2 u}{\partial x_i^2}
$$

The fundamental solution becomes:
$$
G(t,x) = \frac{1}{(2\pi t)^{d/2}} \exp\left(-\frac{|x|^2}{2t}\right)
$$

This is the density of $d$-dimensional Brownian motion $B_t \in \mathbb{R}^d$.

---

## Boundary Value Problems

On a bounded domain $\Omega \subset \mathbb{R}^d$:

$$
\begin{cases}
u_t = \frac{1}{2}\Delta u & \text{in } (0,T) \times \Omega \\
u(0,x) = f(x) & \text{initial condition} \\
u(t,x) = g(t,x) & \text{on } (0,T) \times \partial\Omega \text{ (Dirichlet)}
\end{cases}
$$

**Neumann conditions**: Specify $\frac{\partial u}{\partial n}$ on the boundary (insulated boundary).

---

## Connection to Brownian Motion

The heat equation is the **analytical counterpart** of Brownian motion:

| Probabilistic | Analytical |
|---------------|------------|
| $B_t \sim N(0,t)$ | $G(t,x) = \frac{1}{\sqrt{2\pi t}}e^{-x^2/2t}$ |
| $\mathbb{E}[f(B_t)]$ | $u(t,0) = \int f(x)G(t,x)\,dx$ |
| Generator $\mathcal{L} = \frac{1}{2}\frac{d^2}{dx^2}$ | Heat operator $\partial_t - \frac{1}{2}\partial_{xx}$ |
| Martingale $f(B_t) - \int_0^t \mathcal{L}f(B_s)\,ds$ | $u_t = \frac{1}{2}u_{xx}$ |

This connection, formalized by the **Feynman-Kac theorem**, is the foundation for probabilistic methods in PDE theory.

---

## Historical Note

- **Joseph Fourier** (1822): Derived the heat equation and introduced Fourier series to solve it
- **Norbert Wiener** (1923): Constructed Brownian motion rigorously
- **Andrey Kolmogorov** (1931): Connected diffusions to parabolic PDEs
- **Mark Kac** (1949): Probabilistic interpretation of PDE solutions

---

## Summary

$$
\boxed{
u_t = \frac{1}{2}u_{xx} \quad \longleftrightarrow \quad \text{Brownian motion}
}
$$

The heat equation describes:
- Diffusion of heat, particles, or probability
- Smoothing of initial irregularities  
- Conservation of total mass
- The analytical side of Brownian motion

**The heat equation is the simplest parabolic PDE and the gateway to understanding diffusion processes.**
