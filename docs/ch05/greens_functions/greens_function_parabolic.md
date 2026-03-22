# Green's Function for Parabolic PDEs

A **Green's function** is the response of a linear PDE to a point source -- a delta function impulse at a single point in space and time. For parabolic equations, the Green's function encodes the complete solution operator: once you know how the system responds to a point source, you can build the solution for arbitrary data by superposition. In finance, the Green's function is the **transition density** of the underlying stochastic process.

---

## Intuition

Imagine injecting a unit of heat at a single point $y$ at time $s$. The Green's function $G(t, x; s, y)$ describes how this heat spreads to point $x$ at a later time $t > s$.

- At the injection moment: $G$ is a delta function concentrated at $y$
- For $t > s$: the heat diffuses outward, forming a bell curve that flattens and broadens
- As $t \to \infty$: the heat dissipates (on unbounded domains) or reaches equilibrium (on bounded domains)

The solution for arbitrary initial data $f(x)$ is obtained by superposition:

$$
u(t, x) = \int G(t, x; 0, y)\,f(y)\,dy
$$

Each point $y$ contributes its share $f(y)$ of heat, weighted by the Green's function.

---

## Definition

### The Parabolic Operator

Consider a general parabolic operator:

$$
\mathcal{P}u = \frac{\partial u}{\partial t} - \mathcal{L}u
$$

where $\mathcal{L}$ is a second-order elliptic operator:

$$
\mathcal{L} = \mu(x)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2}{\partial x^2}
$$

### Green's Function

The **Green's function** $G(t, x; s, y)$ is the fundamental solution of $\mathcal{P}$:

$$
\boxed{
\mathcal{P}_x G(t, x; s, y) = \frac{\partial G}{\partial t} - \mathcal{L}_x G = 0, \quad t > s
}
$$

with the **initial condition**:

$$
\lim_{t \downarrow s} G(t, x; s, y) = \delta(x - y)
$$

Here $\mathcal{L}_x$ denotes differentiation with respect to $x$.

**Interpretation**: $G(t, x; s, y)$ is the solution at $(t, x)$ due to a unit impulse at $(s, y)$.

---

## Construction for the Heat Equation

### Free-Space Green's Function

For the standard heat equation $u_t = \frac{1}{2}u_{xx}$ on $\mathbb{R}$, the Green's function is the **heat kernel**:

$$
\boxed{
G(t, x; s, y) = \frac{1}{\sqrt{2\pi(t-s)}} \exp\left(-\frac{(x-y)^2}{2(t-s)}\right), \quad t > s
}
$$

**Verification:**

1. **Satisfies the heat equation** in $(t, x)$ for $t > s$ -- direct computation (see [Fundamental Solution](../heat_equation/fundamental_solution.md))
2. **Initial condition**: As $t \downarrow s$, $G(t, x; s, y) \to \delta(x - y)$ (the Gaussian concentrates at $y$)

### Translation Invariance

For constant-coefficient equations, the Green's function depends only on differences:

$$
G(t, x; s, y) = G(t - s, x - y; 0, 0) = \Gamma(t - s, x - y)
$$

where $\Gamma(\tau, z) = \frac{1}{\sqrt{2\pi\tau}}\,e^{-z^2/2\tau}$ is the fundamental solution.

---

## Solution by Superposition

### Initial Value Problem

For $u_t = \frac{1}{2}u_{xx}$ with $u(0, x) = f(x)$:

$$
\boxed{
u(t, x) = \int_{-\infty}^{\infty} G(t, x; 0, y)\,f(y)\,dy
}
$$

This is a convolution: $u(t, \cdot) = G(t, \cdot; 0, 0) * f$.

### Source Problem

For $u_t - \frac{1}{2}u_{xx} = h(t, x)$ with $u(0, x) = 0$:

$$
u(t, x) = \int_0^t \int_{-\infty}^{\infty} G(t, x; s, y)\,h(s, y)\,dy\,ds
$$

This is the **Duhamel principle**: the response to a distributed source is the integral of responses to point sources.

### Combined Problem

For $u_t - \frac{1}{2}u_{xx} = h(t,x)$ with $u(0,x) = f(x)$:

$$
u(t, x) = \int G(t, x; 0, y)\,f(y)\,dy + \int_0^t\!\int G(t, x; s, y)\,h(s, y)\,dy\,ds
$$

---

## Properties of the Parabolic Green's Function

### 1. Positivity

$$
G(t, x; s, y) > 0 \quad \text{for all } t > s
$$

Heat always flows from source to surroundings -- the Green's function is everywhere positive. This is the PDE manifestation of the fact that transition densities are non-negative.

### 2. Normalization

$$
\int_{-\infty}^{\infty} G(t, x; s, y)\,dx = 1 \quad \text{for all } t > s
$$

The total amount of "heat" (or probability) is conserved. The Green's function is a probability density in $x$.

### 3. Semigroup Property (Chapman-Kolmogorov)

For $s < r < t$:

$$
\boxed{
G(t, x; s, y) = \int_{-\infty}^{\infty} G(t, x; r, z)\,G(r, z; s, y)\,dz
}
$$

**Interpretation**: The transition from $y$ at time $s$ to $x$ at time $t$ can be decomposed into a transition from $y$ to some intermediate point $z$ at time $r$, followed by a transition from $z$ to $x$. Summing over all possible intermediate states gives the direct transition.

**Probabilistic meaning**: This is the **Chapman-Kolmogorov equation** for the transition density of a Markov process.

### 4. Symmetry (for Self-Adjoint Operators)

When $\mathcal{L}$ is self-adjoint ($\mathcal{L} = \mathcal{L}^*$, which holds for the heat equation but not in general), the Green's function satisfies:

$$
G(t, x; s, y) = G(t, y; s, x)
$$

For non-self-adjoint operators (e.g., with drift), this symmetry fails, but a modified symmetry relates $G$ to the Green's function of the adjoint operator.

### 5. Smoothing

For $t > s$, the map $f \mapsto \int G(t, x; s, y)\,f(y)\,dy$ sends bounded measurable functions to $C^\infty$ functions. This is the **instantaneous regularization** property of parabolic equations.

---

## Construction for Variable Coefficients

### Parametrix Method

For the general operator $\mathcal{L} = \mu(x)\partial_x + \frac{1}{2}\sigma^2(x)\partial_{xx}$, the Green's function is constructed by the **parametrix method**:

1. **Freeze coefficients** at the source point $y$: define $\mathcal{L}_y = \mu(y)\partial_x + \frac{1}{2}\sigma^2(y)\partial_{xx}$, which has the explicit Gaussian Green's function:

$$
G_0(t, x; s, y) = \frac{1}{\sigma(y)\sqrt{2\pi(t-s)}} \exp\left(-\frac{(x - y - \mu(y)(t-s))^2}{2\sigma^2(y)(t-s)}\right)
$$

2. **Correct iteratively**: Write $G = G_0 + G_1 + G_2 + \cdots$ where each correction $G_n$ accounts for the error from the frozen-coefficient approximation.

3. **Convergence**: Under Holder continuity of the coefficients, the series converges and yields a smooth Green's function.

!!! note "Levi's Method"
    This iterative construction is called **Levi's parametrix method**. It is the standard technique for proving existence and deriving short-time asymptotics of the Green's function for variable-coefficient parabolic operators.

### Short-Time Asymptotics

For small $t - s$, the Green's function is approximately Gaussian:

$$
G(t, x; s, y) \approx \frac{1}{\sigma(y)\sqrt{2\pi(t-s)}} \exp\left(-\frac{(x - y - \mu(y)(t-s))^2}{2\sigma^2(y)(t-s)}\right)
$$

The corrections are of order $O((t-s)^{1/2})$ relative to the leading term.

---

## Green's Function and the Adjoint Equation

The Green's function satisfies two PDEs:

| Equation | Variables | PDE |
|---|---|---|
| **Forward** (in $t, x$) | Source $(s, y)$ fixed | $\partial_t G = \mathcal{L}_x G$ |
| **Backward** (in $s, y$) | Observation $(t, x)$ fixed | $-\partial_s G = \mathcal{L}_y^* G$ |

where $\mathcal{L}^*$ is the formal adjoint:

$$
\mathcal{L}^* p = -\frac{\partial}{\partial y}[\mu(y)p] + \frac{1}{2}\frac{\partial^2}{\partial y^2}[\sigma^2(y)p]
$$

!!! info "Financial Interpretation"
    - **Forward equation**: Fix where the process starts; the Green's function (transition density) evolves via Fokker-Planck as you vary the destination
    - **Backward equation**: Fix where you observe; the Green's function solves Kolmogorov backward as you vary the origin

---

## Example: Brownian Motion with Drift

For $dX_t = \mu\,dt + \sigma\,dW_t$ (constant coefficients), the Green's function is:

$$
G(t, x; s, y) = \frac{1}{\sigma\sqrt{2\pi(t-s)}} \exp\left(-\frac{(x - y - \mu(t-s))^2}{2\sigma^2(t-s)}\right)
$$

This is the density of $X_t \mid X_s = y$, i.e., a normal distribution with:

- Mean: $y + \mu(t-s)$
- Variance: $\sigma^2(t-s)$

**Verification of the semigroup property**: The convolution of two Gaussians is Gaussian with added means and variances -- consistent with the independent increments of Brownian motion with drift.

---

## Example: Ornstein-Uhlenbeck Process

For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, the Green's function is:

$$
G(t, x; s, y) = \frac{1}{\sqrt{2\pi\,v(t-s)}} \exp\left(-\frac{(x - ye^{-\kappa(t-s)})^2}{2\,v(t-s)}\right)
$$

where the conditional variance is:

$$
v(\tau) = \frac{\sigma^2}{2\kappa}\left(1 - e^{-2\kappa\tau}\right)
$$

**Key features:**

- The conditional mean $ye^{-\kappa\tau}$ reverts toward zero at rate $\kappa$
- The conditional variance $v(\tau) \to \frac{\sigma^2}{2\kappa}$ as $\tau \to \infty$ -- the stationary variance
- The Green's function converges to the stationary density $N(0, \sigma^2/2\kappa)$ regardless of the starting point

---

## Summary

$$
\boxed{
u(t, x) = \int G(t, x; s, y)\,f(y)\,dy \quad \text{(superposition principle)}
}
$$

| Property | Statement |
|---|---|
| **Definition** | $\partial_t G = \mathcal{L}_x G$ with $G(s^+, x; s, y) = \delta(x-y)$ |
| **Positivity** | $G > 0$ for $t > s$ |
| **Normalization** | $\int G\,dx = 1$ |
| **Semigroup** | $G(t,x;s,y) = \int G(t,x;r,z)\,G(r,z;s,y)\,dz$ |
| **Smoothing** | Maps $L^\infty$ to $C^\infty$ |

**The Green's function is the fundamental building block for parabolic PDEs: it solves the equation for a point source, and arbitrary solutions are obtained by superposition. In probability, it is the transition density; in finance, it is the state-price density.**

---

## See Also

- [Fundamental Solution](../heat_equation/fundamental_solution.md) -- the heat kernel as the simplest Green's function
- [Transition Density as Green's Function](transition_density_as_greens_function.md) -- the probabilistic interpretation
- [Spectral Decomposition](spectral_decomposition.md) -- eigenfunction expansion of the Green's function
- [Free vs Bounded Domains](free_vs_bounded_domains.md) -- how boundaries modify the Green's function
- [Kolmogorov Forward Equation](../kolmogorov_equations/kolmogorov_forward.md) -- the PDE that the Green's function satisfies
