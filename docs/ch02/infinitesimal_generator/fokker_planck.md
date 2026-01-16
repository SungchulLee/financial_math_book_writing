# The Fokker–Planck Equation

The **Fokker–Planck equation** (also called the **Kolmogorov forward equation**) describes the time evolution of the probability density of a diffusion process. While the backward equation acts on initial conditions, the forward equation acts on final positions—tracking how probability mass spreads over time.

---

## Setting

Consider the diffusion:

$$
dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t
$$

Let $p(t, x, y)$ denote the transition density:

$$
\mathbb{P}(X_t \in dy \mid X_0 = x) = p(t, x, y)\,dy
$$

---

## The Fokker–Planck Equation

**Theorem**: The transition density satisfies:

$$
\boxed{
\frac{\partial p}{\partial t}(t, x, y) = \mathcal{L}_y^* p(t, x, y)
}
$$

where $\mathcal{L}^*$ is the **adjoint** of the generator:

$$
\boxed{
\mathcal{L}^* p = -\frac{\partial}{\partial y}[\mu(y) p] + \frac{1}{2}\frac{\partial^2}{\partial y^2}[\sigma^2(y) p]
}
$$

**Initial condition**: $p(0, x, y) = \delta(y - x)$.

---

## Expanded Form

Expanding the derivatives:

$$
\frac{\partial p}{\partial t} = -\mu(y)\frac{\partial p}{\partial y} - \mu'(y)p + \frac{\sigma^2(y)}{2}\frac{\partial^2 p}{\partial y^2} + \sigma(y)\sigma'(y)\frac{\partial p}{\partial y} + \frac{[\sigma'(y)]^2 + \sigma(y)\sigma''(y)}{2}p
$$

For **constant coefficients** $(\mu, \sigma = \text{const})$:

$$
\frac{\partial p}{\partial t} = -\mu\frac{\partial p}{\partial y} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial y^2}
$$

---

## Continuity Form

The Fokker–Planck equation can be written as a **continuity equation**:

$$
\frac{\partial p}{\partial t} + \frac{\partial J}{\partial y} = 0
$$

where the **probability current** is:

$$
J = \mu(y)p - \frac{1}{2}\frac{\partial}{\partial y}[\sigma^2(y)p]
$$

**Interpretation**: Probability is conserved; it flows according to current $J$.

---

## The Adjoint Relationship

The generator $\mathcal{L}$ and its adjoint $\mathcal{L}^*$ satisfy:

$$
\int_{-\infty}^{\infty} f(y)(\mathcal{L}g)(y)\,dy = \int_{-\infty}^{\infty} (\mathcal{L}^* f)(y)g(y)\,dy
$$

for suitable test functions with vanishing boundary terms.

| Operator | Acts on | Formula |
|----------|---------|---------|
| $\mathcal{L}$ | Test functions | $\mu f' + \frac{1}{2}\sigma^2 f''$ |
| $\mathcal{L}^*$ | Densities | $-(\mu f)' + \frac{1}{2}(\sigma^2 f)''$ |

---

## Examples

### Example 1: Brownian Motion

For $dX_t = dW_t$:

$$
\frac{\partial p}{\partial t} = \frac{1}{2}\frac{\partial^2 p}{\partial y^2}
$$

**Solution** (heat kernel):

$$
p(t, x, y) = \frac{1}{\sqrt{2\pi t}}\exp\left(-\frac{(y-x)^2}{2t}\right)
$$

### Example 2: Brownian Motion with Drift

For $dX_t = \mu\,dt + \sigma\,dW_t$:

$$
\frac{\partial p}{\partial t} = -\mu\frac{\partial p}{\partial y} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial y^2}
$$

**Solution**:

$$
p(t, x, y) = \frac{1}{\sigma\sqrt{2\pi t}}\exp\left(-\frac{(y - x - \mu t)^2}{2\sigma^2 t}\right)
$$

### Example 3: Ornstein–Uhlenbeck Process

For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$:

$$
\frac{\partial p}{\partial t} = \kappa\frac{\partial}{\partial y}(yp) + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial y^2}
$$

**Stationary solution** ($\partial_t p = 0$):

$$
p_\infty(y) = \sqrt{\frac{\kappa}{\pi\sigma^2}}\exp\left(-\frac{\kappa y^2}{\sigma^2}\right)
$$

This is Gaussian with variance $\sigma^2/(2\kappa)$.

### Example 4: Geometric Brownian Motion

For $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$:

$$
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial S}(\mu S p) + \frac{\sigma^2}{2}\frac{\partial^2}{\partial S^2}(S^2 p)
$$

**Solution**: Log-normal density

$$
p(t, S_0, S) = \frac{1}{S\sigma\sqrt{2\pi t}}\exp\left(-\frac{(\log S - \log S_0 - (\mu - \sigma^2/2)t)^2}{2\sigma^2 t}\right)
$$

---

## Stationary (Invariant) Distributions

A density $p_\infty(y)$ is **stationary** if $\mathcal{L}^* p_\infty = 0$, meaning:

$$
-\frac{d}{dy}[\mu(y)p_\infty] + \frac{1}{2}\frac{d^2}{dy^2}[\sigma^2(y)p_\infty] = 0
$$

**Zero-current condition**: At stationarity with $J = 0$:

$$
\mu(y)p_\infty = \frac{1}{2}\frac{d}{dy}[\sigma^2(y)p_\infty]
$$

**Solution** (one dimension):

$$
p_\infty(y) \propto \frac{1}{\sigma^2(y)}\exp\left(\int^y \frac{2\mu(z)}{\sigma^2(z)}\,dz\right)
$$

---

## Comparison: Backward vs Forward

| Aspect | Backward (Kolmogorov) | Forward (Fokker–Planck) |
|--------|----------------------|------------------------|
| **Equation** | $\partial_t p = \mathcal{L}_x p$ | $\partial_t p = \mathcal{L}_y^* p$ |
| **Acts on** | Initial point $x$ | Final point $y$ |
| **Question** | Where to start? | Where to end up? |
| **Physical** | Retrospective | Predictive |

---

## Multidimensional Fokker–Planck

For $X_t \in \mathbb{R}^d$ with $dX_t^i = \mu^i(X_t)\,dt + \sigma^{i\alpha}(X_t)\,dW_t^\alpha$:

$$
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial y_i}(\mu^i p) + \frac{1}{2}\frac{\partial^2}{\partial y_i \partial y_j}(a^{ij} p)
$$

where $a^{ij} = \sigma^{i\alpha}\sigma^{j\alpha}$.

---

## Physical Interpretation

The Fokker–Planck equation describes:

1. **Advection**: $-\nabla \cdot (\mu p)$ — probability flows with velocity field $\mu$
2. **Diffusion**: $\frac{1}{2}\nabla^2(Dp)$ — probability spreads due to noise

**Applications**:
- Statistical mechanics (Brownian particles)
- Plasma physics
- Chemical kinetics
- Population dynamics
- Neural networks

---

## Historical Note

- **Adriaan Fokker** (1914): Derived in the context of Brownian motion
- **Max Planck** (1917): Independent derivation for radiation problems
- **Andrey Kolmogorov** (1931): Rigorous mathematical foundation

---

## Summary

$$
\boxed{
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial y}[\mu(y)p] + \frac{1}{2}\frac{\partial^2}{\partial y^2}[\sigma^2(y)p]
}
$$

**The Fokker–Planck equation describes how probability density evolves in time, dual to the backward equation which describes how expectations depend on initial conditions.**
