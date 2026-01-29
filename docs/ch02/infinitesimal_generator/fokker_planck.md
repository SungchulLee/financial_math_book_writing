# The Fokker–Planck Equation

The **Fokker–Planck equation** (also called the **Kolmogorov forward equation**) describes the time evolution of the probability density of a diffusion process. While the backward equation acts on initial conditions $(x_0, t_0)$, the forward equation acts on current state $(x, t)$—tracking how probability mass spreads over time.

!!! tip "Related Content"
    - [Kolmogorov Forward (PDE Methods)](../../ch03/kolmogorov_equation/kolmogorov_forward_equation.md) — analytical solution techniques
    - [Kolmogorov Backward Equation](kolmogorov_backward.md) — the dual equation
    - [Infinitesimal Generator](infinitesimal_generator.md) — probabilistic foundations
    - [Invariant Measures](../diffusion_process/invariant_measures_and_stationarity.md) — stationary distributions

---

## Setting

Consider the Itô diffusion:

$$
dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t
$$

Let $p(x, t \mid x_0, t_0)$ denote the **transition density**:

$$
\mathbb{P}(X_t \in dx \mid X_{t_0} = x_0) = p(x, t \mid x_0, t_0)\,dx
$$

**Notation convention:**

- $(x_0, t_0)$: initial state and time (fixed parameters)
- $(x, t)$: current state and time (variables the PDE acts on)

---

## The Fokker–Planck Equation

!!! abstract "Theorem (Fokker–Planck Equation)"
    The transition density satisfies:

    $$
    \boxed{
    \frac{\partial p}{\partial t}(x, t \mid x_0, t_0) = \mathcal{L}_x^* p(x, t \mid x_0, t_0)
    }
    $$

    where $\mathcal{L}^*$ is the **adjoint** of the infinitesimal generator, acting on $x$:

    $$
    \boxed{
    \mathcal{L}^* p = -\frac{\partial}{\partial x}[\mu(x) p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x) p]
    }
    $$

    **Initial condition**: $p(x, t_0 \mid x_0, t_0) = \delta(x - x_0)$

**Regularity conditions**: The theorem requires:

- $\mu(x)$ and $\sigma(x)$ are sufficiently smooth (typically $C^1$)
- $\sigma(x) > 0$ (uniform ellipticity)
- Appropriate boundary conditions (natural, reflecting, or absorbing)

---

## Derivation

The Fokker–Planck equation arises from the adjoint relationship between the generator and density evolution.

??? abstract "Derivation via Integration by Parts"

    **Step 1**: Start with the expectation form. For any smooth test function $f$ with compact support:

    $$
    \frac{d}{dt}\mathbb{E}[f(X_t) \mid X_{t_0} = x_0] = \mathbb{E}[(\mathcal{L}f)(X_t)]
    $$

    **Step 2**: Write expectations as integrals against the density:

    $$
    \frac{d}{dt}\int_{-\infty}^{\infty} f(x) p(x,t \mid x_0, t_0)\,dx = \int_{-\infty}^{\infty} (\mathcal{L}f)(x) p(x,t \mid x_0, t_0)\,dx
    $$

    **Step 3**: The left side equals:

    $$
    \int_{-\infty}^{\infty} f(x) \frac{\partial p}{\partial t}(x,t \mid x_0, t_0)\,dx
    $$

    **Step 4**: Integrate by parts on the right side. For the drift term:

    $$
    \int \mu(x) f'(x) p\,dx = -\int f(x) \frac{\partial}{\partial x}[\mu(x) p]\,dx
    $$

    For the diffusion term:

    $$
    \int \frac{\sigma^2(x)}{2} f''(x) p\,dx = \int f(x) \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x) p]\,dx
    $$

    **Step 5**: Since this holds for all test functions $f$:

    $$
    \frac{\partial p}{\partial t} = -\frac{\partial}{\partial x}[\mu(x) p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x) p]
    $$

---

## Expanded Form

Expanding the derivatives explicitly using the product rule:

**Drift term:**

$$
-\frac{\partial}{\partial x}[\mu(x) p] = -\mu(x)\frac{\partial p}{\partial x} - \mu'(x)p
$$

**Diffusion term:** Let $D(x) = \sigma^2(x)$. Then:

$$
\frac{1}{2}\frac{\partial^2}{\partial x^2}[D(x) p] = \frac{1}{2}D(x)\frac{\partial^2 p}{\partial x^2} + D'(x)\frac{\partial p}{\partial x} + \frac{1}{2}D''(x)p
$$

Since $D' = 2\sigma\sigma'$ and $D'' = 2(\sigma')^2 + 2\sigma\sigma''$:

$$
\frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x) p] = \frac{\sigma^2(x)}{2}\frac{\partial^2 p}{\partial x^2} + \sigma(x)\sigma'(x)\frac{\partial p}{\partial x} + \left[(\sigma'(x))^2 + \sigma(x)\sigma''(x)\right]p
$$

**Combined:**

$$
\frac{\partial p}{\partial t} = \left[-\mu(x) + \sigma(x)\sigma'(x)\right]\frac{\partial p}{\partial x} + \frac{\sigma^2(x)}{2}\frac{\partial^2 p}{\partial x^2} + \left[-\mu'(x) + (\sigma'(x))^2 + \sigma(x)\sigma''(x)\right]p
$$

For **constant coefficients** ($\mu, \sigma = \text{const}$), this simplifies to:

$$
\frac{\partial p}{\partial t} = -\mu\frac{\partial p}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x^2}
$$

This is the **advection–diffusion equation**: probability advects with velocity $\mu$ and diffuses with coefficient $\sigma^2/2$.

---

## Continuity Form

The Fokker–Planck equation can be written as a **continuity equation**:

$$
\frac{\partial p}{\partial t} + \frac{\partial J}{\partial x} = 0
$$

where the **probability current** is:

$$
J(x, t) = \mu(x)p - \frac{1}{2}\frac{\partial}{\partial x}[\sigma^2(x)p]
$$

!!! info "Physical Interpretation"
    Probability is conserved—it flows according to current $J$. The current has two components:

    - **Drift current**: $\mu(x) p$ — deterministic flow
    - **Diffusive current**: $-\frac{1}{2}\frac{\partial}{\partial x}[\sigma^2(x)p]$ — spreading due to noise

---

## Weak (Expectation) Form

For smooth test functions $f$ with suitable decay:

$$
\frac{d}{dt}\mathbb{E}[f(X_t) \mid X_{t_0} = x_0] = \mathbb{E}[(\mathcal{L}f)(X_t)]
$$

Equivalently:

$$
\frac{d}{dt}\int_{-\infty}^{\infty} f(x)p(x, t \mid x_0, t_0)\,dx = \int_{-\infty}^{\infty} (\mathcal{L}f)(x)p(x, t \mid x_0, t_0)\,dx
$$

This formulation is **dual** to the density PDE: the generator $\mathcal{L}$ acts on test functions, while its adjoint $\mathcal{L}^*$ acts on densities.

---

## The Adjoint Relationship

The generator $\mathcal{L}$ and its adjoint $\mathcal{L}^*$ satisfy:

$$
\int_{-\infty}^{\infty} f(x)(\mathcal{L}g)(x)\,dx = \int_{-\infty}^{\infty} (\mathcal{L}^* f)(x)g(x)\,dx
$$

for suitable test functions $f, g$ with vanishing boundary terms.

| Operator | Acts on | Formula |
|----------|---------|---------|
| $\mathcal{L}$ | Test functions | $\mu(x) f'(x) + \frac{1}{2}\sigma^2(x) f''(x)$ |
| $\mathcal{L}^*$ | Densities | $-[\mu(x) f]' + \frac{1}{2}[\sigma^2(x) f]''$ |

---

## Examples

### Example 1: Brownian Motion

For $dX_t = dW_t$ (i.e., $\mu = 0$, $\sigma = 1$):

$$
\frac{\partial p}{\partial t} = \frac{1}{2}\frac{\partial^2 p}{\partial x^2}
$$

This is the **heat equation**. See [Heat Equation and Brownian Motion](../../ch03/heat_equation/heat_equation_and_brownian_motion.md).

**Solution** (heat kernel):

$$
p(x, t \mid x_0, t_0) = \frac{1}{\sqrt{2\pi (t - t_0)}}\exp\left(-\frac{(x - x_0)^2}{2(t - t_0)}\right)
$$

### Example 2: Brownian Motion with Drift

For $dX_t = \mu\,dt + \sigma\,dW_t$:

$$
\frac{\partial p}{\partial t} = -\mu\frac{\partial p}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x^2}
$$

**Solution**:

$$
p(x, t \mid x_0, t_0) = \frac{1}{\sigma\sqrt{2\pi (t-t_0)}}\exp\left(-\frac{(x - x_0 - \mu(t-t_0))^2}{2\sigma^2 (t-t_0)}\right)
$$

### Example 3: Ornstein–Uhlenbeck Process

For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ (mean-reverting to zero):

$$
\frac{\partial p}{\partial t} = \kappa\frac{\partial}{\partial x}(x \cdot p) + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x^2}
$$

**Transient solution** (starting from $X_{t_0} = x_0$):

$$
p(x, t \mid x_0, t_0) = \frac{1}{\sqrt{2\pi v(\tau)}}\exp\left(-\frac{(x - m(\tau))^2}{2v(\tau)}\right)
$$

where $\tau = t - t_0$ and:

- Mean: $m(\tau) = x_0 e^{-\kappa \tau}$
- Variance: $v(\tau) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa \tau})$

**Stationary solution** (as $\tau \to \infty$): The variance converges to $v_\infty = \frac{\sigma^2}{2\kappa}$, giving:

$$
p_\infty(x) = \frac{1}{\sqrt{2\pi v_\infty}}\exp\left(-\frac{x^2}{2v_\infty}\right) = \sqrt{\frac{\kappa}{\pi\sigma^2}}\exp\left(-\frac{\kappa x^2}{\sigma^2}\right)
$$

### Example 4: Geometric Brownian Motion

For $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ on $S > 0$:

$$
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial S}(\mu S \cdot p) + \frac{\sigma^2}{2}\frac{\partial^2}{\partial S^2}(S^2 \cdot p)
$$

!!! warning "Boundary Condition"
    GBM is defined on $S > 0$. The boundary at $S = 0$ is natural (inaccessible) for GBM, but this should be verified for modified models.

**Solution** (log-normal density):

$$
p(S, t \mid S_0, t_0) = \frac{1}{S\sigma\sqrt{2\pi (t-t_0)}}\exp\left(-\frac{(\log S - \log S_0 - (\mu - \sigma^2/2)(t-t_0))^2}{2\sigma^2 (t-t_0)}\right)
$$

---

## Stationary (Invariant) Distributions

A density $p_\infty(x)$ is **stationary** if $\mathcal{L}^* p_\infty = 0$:

$$
-\frac{d}{dx}[\mu(x)p_\infty] + \frac{1}{2}\frac{d^2}{dx^2}[\sigma^2(x)p_\infty] = 0
$$

See [Invariant Measures and Stationarity](../diffusion_process/invariant_measures_and_stationarity.md) for detailed treatment.

### Zero-Current Condition

At stationarity with zero probability current ($J = 0$):

$$
\mu(x)p_\infty = \frac{1}{2}\frac{d}{dx}[\sigma^2(x)p_\infty]
$$

### Solution (One Dimension)

$$
p_\infty(x) \propto \frac{1}{\sigma^2(x)}\exp\left(\int^x \frac{2\mu(z)}{\sigma^2(z)}\,dz\right)
$$

!!! warning "Existence Conditions"
    This formula only yields a valid density if:

    1. $\sigma(x) > 0$ for all $x$ in the domain
    2. The integral converges (normalizability)
    3. Boundary conditions are compatible (reflecting or natural)
    
    For example, standard Brownian motion on $\mathbb{R}$ has **no** stationary distribution.

---

## Comparison: Backward vs Forward

| Aspect | Backward (Kolmogorov) | Forward (Fokker–Planck) |
|--------|----------------------|------------------------|
| **Equation** | $\partial_{t_0} p + \mathcal{L}_{x_0} p = 0$ | $\partial_t p = \mathcal{L}_x^* p$ |
| **Acts on** | Initial point $(x_0, t_0)$ | Current point $(x, t)$ |
| **Question answered** | "What's the expected payoff starting from here?" | "Where will the process be?" |
| **Time direction** | Backward from terminal | Forward from initial |
| **Used for** | Option pricing, expected values | Density evolution, long-time behavior |

---

## Multidimensional Fokker–Planck

For $X_t \in \mathbb{R}^d$ with $dX_t^i = \mu^i(X_t)\,dt + \sigma^{i\alpha}(X_t)\,dW_t^\alpha$:

$$
\frac{\partial p}{\partial t} = -\sum_{i=1}^{d}\frac{\partial}{\partial x_i}(\mu^i p) + \frac{1}{2}\sum_{i,j=1}^{d}\frac{\partial^2}{\partial x_i \partial x_j}(a^{ij} p)
$$

where the diffusion matrix is $a^{ij} = \sum_{\alpha}\sigma^{i\alpha}\sigma^{j\alpha}$.

---

## Connection to Score Functions

!!! tip "Relevance to Generative Models"
    Given a **marginal density** $p(x, t)$ (obtained by integrating the transition density against a data distribution), the **score function** is:

    $$
    s(x, t) = \nabla_x \log p(x, t)
    $$

    This gradient of the log-density is fundamental to:

    - **Score matching** in machine learning
    - **Reverse-time SDEs** for diffusion models
    - **Denoising score matching** in modern generative AI

    The Fokker–Planck equation governs the evolution of $p(x, t)$, which determines the score. For time-reversal of diffusions, one needs:

    $$
    dX_t = \left[\mu(X_t) - \sigma^2(X_t) \nabla_x \log p(X_t, t)\right] dt + \sigma(X_t)\,d\bar{W}_t
    $$

    where $\bar{W}_t$ is a backward Brownian motion. See [Time Reversal of Diffusions](../diffusion_process/time_reversal_of_diffusions.md).

---

## Historical Note

- **Adriaan Fokker** (1914): Derived in the context of Brownian motion
- **Max Planck** (1917): Independent derivation for radiation problems  
- **Andrey Kolmogorov** (1931): Rigorous mathematical foundation, establishing the connection to diffusion processes

---

## Summary

$$
\boxed{
\frac{\partial p}{\partial t}(x, t \mid x_0, t_0) = -\frac{\partial}{\partial x}[\mu(x)p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x)p]
}
$$

The Fokker–Planck equation describes how probability density evolves forward in time, dual to the backward equation which describes how expectations depend on initial conditions.

---

## See Also

- [Kolmogorov Forward (PDE Methods)](../../ch03/kolmogorov_equation/kolmogorov_forward_equation.md) — analytical and numerical solutions
- [Kolmogorov Backward Equation](kolmogorov_backward.md) — the dual equation for expectations
- [Heat Equation](../../ch03/heat_equation/heat_equation_overview.md) — Fokker–Planck for standard Brownian motion
- [Infinitesimal Generator](infinitesimal_generator.md) — the operator $\mathcal{L}$
- [Invariant Measures](../diffusion_process/invariant_measures_and_stationarity.md) — stationary distributions
- [Time Reversal of Diffusions](../diffusion_process/time_reversal_of_diffusions.md) — connection to score functions
