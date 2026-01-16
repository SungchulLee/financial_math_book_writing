# Kolmogorov Equations

The **Kolmogorov equations** describe the time evolution of probability distributions for diffusion processes. They come in two fundamental forms:

- **Backward equation**: Evolution of expected values as a function of initial condition
- **Forward equation** (Fokker–Planck): Evolution of the probability density over time

These equations form the analytical backbone of diffusion theory and connect stochastic processes to partial differential equations.

---

## Setting

Consider the time-homogeneous diffusion:

$$
dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t
$$

with infinitesimal generator:

$$
\mathcal{L} = \mu(x)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2}{\partial x^2}
$$

Let $p(t, x, y)$ denote the **transition density**:

$$
\mathbb{P}(X_t \in dy \mid X_0 = x) = p(t, x, y)\,dy
$$

---

## Kolmogorov Backward Equation

### Statement

The transition density $p(t, x, y)$, viewed as a function of the **initial point** $(x)$ and time $(t)$, satisfies:

$$
\boxed{
\frac{\partial p}{\partial t}(t, x, y) = \mathcal{L}_x p(t, x, y)
}
$$

where $\mathcal{L}_x$ acts on the $x$ variable:

$$
\mathcal{L}_x p = \mu(x)\frac{\partial p}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2 p}{\partial x^2}
$$

**Initial condition**: As $t \to 0^+$,

$$
p(t, x, y) \to \delta(x - y)
$$

### Interpretation

The backward equation describes how the probability of reaching $y$ changes as we vary the **starting point** $x$.

**Physical intuition**: "Where must I start to end up at $y$?"

### General Form (Expected Values)

For any function $f$, define:

$$
u(t, x) = \mathbb{E}[f(X_t) \mid X_0 = x] = \int f(y) p(t, x, y)\,dy
$$

Then $u$ satisfies the backward equation:

$$
\boxed{
\frac{\partial u}{\partial t} = \mathcal{L} u
}
$$

with initial condition $u(0, x) = f(x)$.

### Derivation

**Step 1**: Use the Chapman–Kolmogorov equation:

$$
p(t + s, x, y) = \int p(t, x, z) p(s, z, y)\,dz
$$

**Step 2**: Differentiate with respect to $s$ at $s = 0$:

$$
\frac{\partial p}{\partial t}(t, x, y) = \lim_{s \to 0} \frac{1}{s}\left[ p(t + s, x, y) - p(t, x, y) \right]
$$

$$
= \lim_{s \to 0} \frac{1}{s} \int p(t, x, z) \left[ p(s, z, y) - \delta(z - y) \right] dz
$$

**Step 3**: Recognize the generator acting on the $z$ variable in $p(s, z, y)$:

$$
\lim_{s \to 0} \frac{p(s, z, y) - \delta(z - y)}{s} = \mathcal{L}_z^* \delta(z - y)
$$

**Step 4**: After integration by parts, this yields the backward equation.

---

## Kolmogorov Forward Equation (Fokker–Planck)

### Statement

The transition density $p(t, x, y)$, viewed as a function of the **final point** $(y)$ and time $(t)$, satisfies:

$$
\boxed{
\frac{\partial p}{\partial t}(t, x, y) = \mathcal{L}_y^* p(t, x, y)
}
$$

where $\mathcal{L}^*$ is the **adjoint** (or **formal adjoint**) of $\mathcal{L}$:

$$
\mathcal{L}^* p = -\frac{\partial}{\partial y}[\mu(y) p] + \frac{1}{2}\frac{\partial^2}{\partial y^2}[\sigma^2(y) p]
$$

Expanding:

$$
\boxed{
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial y}[\mu(y) p] + \frac{1}{2}\frac{\partial^2}{\partial y^2}[\sigma^2(y) p]
}
$$

**Initial condition**: $p(0, x, y) = \delta(y - x)$.

### Alternative Form

The Fokker–Planck equation is often written as:

$$
\frac{\partial p}{\partial t} = -\frac{\partial J}{\partial y}
$$

where the **probability current** is:

$$
J = \mu(y) p - \frac{1}{2}\frac{\partial}{\partial y}[\sigma^2(y) p]
$$

This is a **continuity equation**: probability is conserved, flowing with current $J$.

### Interpretation

The forward equation describes how the **probability density evolves** over time.

**Physical intuition**: "Given I started at $x$, where am I likely to be at time $t$?"

### Derivation (Integration by Parts)

For any test function $\phi$:

$$
\int \phi(y) \frac{\partial p}{\partial t}(t, x, y)\,dy = \frac{d}{dt} \mathbb{E}[\phi(X_t) \mid X_0 = x]
$$

By the backward equation applied to $\phi$:

$$
= \int (\mathcal{L}\phi)(y) \, p(t, x, y)\,dy
$$

Integrating by parts (moving derivatives from $\phi$ to $p$):

$$
= \int \phi(y) (\mathcal{L}^* p)(t, x, y)\,dy
$$

Since this holds for all $\phi$:

$$
\frac{\partial p}{\partial t} = \mathcal{L}^* p
$$

---

## The Adjoint Operator

The generator $\mathcal{L}$ and its adjoint $\mathcal{L}^*$ are related by:

$$
\int f(x) (\mathcal{L}g)(x)\,dx = \int (\mathcal{L}^* f)(x) g(x)\,dx
$$

for suitable test functions with appropriate boundary conditions.

**Explicit formulas**:

| Operator | Formula |
|----------|---------|
| Generator $\mathcal{L}$ | $\mu(x)\partial_x + \frac{1}{2}\sigma^2(x)\partial_{xx}$ |
| Adjoint $\mathcal{L}^*$ | $-\partial_x[\mu(x) \cdot] + \frac{1}{2}\partial_{xx}[\sigma^2(x) \cdot]$ |

**Key difference**: In $\mathcal{L}$, coefficients are outside derivatives. In $\mathcal{L}^*$, they are inside.

---

## Example 1: Brownian Motion

For standard Brownian motion: $\mu = 0$, $\sigma = 1$.

**Generator**: $\mathcal{L} = \frac{1}{2}\frac{\partial^2}{\partial x^2}$

**Backward equation**:

$$
\frac{\partial p}{\partial t} = \frac{1}{2}\frac{\partial^2 p}{\partial x^2}
$$

**Forward equation** (same due to self-adjointness):

$$
\frac{\partial p}{\partial t} = \frac{1}{2}\frac{\partial^2 p}{\partial y^2}
$$

**Solution** (heat kernel):

$$
p(t, x, y) = \frac{1}{\sqrt{2\pi t}} \exp\left(-\frac{(y - x)^2}{2t}\right)
$$

This is the **fundamental solution** to the heat equation.

---

## Example 2: Brownian Motion with Drift

For $dX_t = \mu\,dt + \sigma\,dW_t$ (constant coefficients):

**Forward equation**:

$$
\frac{\partial p}{\partial t} = -\mu\frac{\partial p}{\partial y} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial y^2}
$$

**Solution**:

$$
p(t, x, y) = \frac{1}{\sigma\sqrt{2\pi t}} \exp\left(-\frac{(y - x - \mu t)^2}{2\sigma^2 t}\right)
$$

The density is Gaussian, centered at $x + \mu t$, spreading with variance $\sigma^2 t$.

---

## Example 3: Ornstein–Uhlenbeck Process

For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$:

**Forward equation**:

$$
\frac{\partial p}{\partial t} = \kappa\frac{\partial}{\partial y}(yp) + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial y^2}
$$

**Stationary solution** ($\partial p/\partial t = 0$):

$$
p_\infty(y) = \sqrt{\frac{\kappa}{\pi\sigma^2}} \exp\left(-\frac{\kappa y^2}{\sigma^2}\right)
$$

This is the **invariant measure**: $N(0, \sigma^2/2\kappa)$.

---

## Example 4: Geometric Brownian Motion

For $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$:

**Forward equation** (in $S$):

$$
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial S}(\mu S p) + \frac{\sigma^2}{2}\frac{\partial^2}{\partial S^2}(S^2 p)
$$

**Solution**: Log-normal density

$$
p(t, S_0, S) = \frac{1}{S\sigma\sqrt{2\pi t}} \exp\left(-\frac{(\log S - \log S_0 - (\mu - \sigma^2/2)t)^2}{2\sigma^2 t}\right)
$$

---

## Connection to Invariant Measures

A probability measure $\pi$ is **invariant** for the diffusion if:

$$
\mathcal{L}^* \pi = 0
$$

**Interpretation**: No net probability flow; the distribution is stationary.

**For one dimension with detailed balance**:

$$
\pi(x) \propto \frac{1}{\sigma^2(x)} \exp\left(\int^x \frac{2\mu(y)}{\sigma^2(y)}\,dy\right)
$$

provided this is normalizable.

---

## Comparison: Backward vs Forward

| Aspect | Backward Equation | Forward Equation |
|--------|-------------------|------------------|
| **Variable** | Initial point $x$ | Final point $y$ |
| **Operator** | Generator $\mathcal{L}$ | Adjoint $\mathcal{L}^*$ |
| **Question** | "Where must I start?" | "Where will I end up?" |
| **Use** | Expected values, pricing | Density evolution |
| **Initial condition** | $u(0,x) = f(x)$ | $p(0,y) = \delta(y-x)$ |

**Duality**: The backward and forward equations are **adjoint** to each other.

---

## Multidimensional Generalization

For $X_t \in \mathbb{R}^d$ with:

$$
dX_t^i = \mu^i(X_t)\,dt + \sigma^{i\alpha}(X_t)\,dW_t^\alpha
$$

**Generator**:

$$
\mathcal{L} = \mu^i \partial_i + \frac{1}{2}a^{ij}\partial_i\partial_j, \quad a^{ij} = \sigma^{i\alpha}\sigma^{j\alpha}
$$

**Forward equation**:

$$
\frac{\partial p}{\partial t} = -\partial_i(\mu^i p) + \frac{1}{2}\partial_i\partial_j(a^{ij} p)
$$

---

## Numerical Methods

### Solving the Forward Equation

1. **Finite differences**: Discretize space and time
2. **Spectral methods**: Expand in eigenfunctions
3. **Monte Carlo**: Kernel density estimation from simulated paths

### Solving the Backward Equation

1. **Finite differences**: Solve backward in time
2. **Feynman–Kac**: Monte Carlo simulation
3. **Series expansion**: For special cases

---

## Applications

1. **Finance**: Option pricing, risk management
2. **Physics**: Diffusion, heat conduction, quantum mechanics
3. **Biology**: Population dynamics, neural activity
4. **Engineering**: Filtering, control theory
5. **Statistics**: Bayesian inference, MCMC diagnostics

---

## Historical Note

**Andrey Kolmogorov** (1903–1987) derived these equations in his foundational 1931 paper "Über die analytischen Methoden in der Wahrscheinlichkeitsrechnung" (On Analytical Methods in Probability Theory).

**Adriaan Fokker** and **Max Planck** independently derived the forward equation in physics contexts (1914, 1917), hence the name "Fokker–Planck equation."

---

## Summary

$$
\boxed{
\begin{aligned}
\text{Backward:} \quad & \frac{\partial u}{\partial t} = \mathcal{L} u & \text{(acts on initial condition)} \\[1em]
\text{Forward:} \quad & \frac{\partial p}{\partial t} = \mathcal{L}^* p & \text{(acts on final position)}
\end{aligned}
}
$$

| Equation | Operator | Describes |
|----------|----------|-----------|
| Backward | $\mathcal{L} = \mu\partial_x + \frac{1}{2}\sigma^2\partial_{xx}$ | Expected values |
| Forward (Fokker–Planck) | $\mathcal{L}^* = -\partial_x(\mu\cdot) + \frac{1}{2}\partial_{xx}(\sigma^2\cdot)$ | Probability density |

**The Kolmogorov equations are the PDE formulation of diffusion theory, dual to the SDE formulation via the Feynman–Kac connection.**
