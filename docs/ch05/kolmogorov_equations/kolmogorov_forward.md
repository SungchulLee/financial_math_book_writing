# Kolmogorov Forward Equation (Fokker–Planck)

The **Kolmogorov forward equation**, also known as the **Fokker–Planck equation**, describes the time evolution of the probability density of a diffusion process. While the backward equation acts on initial conditions $(x_0, t_0)$, the forward equation acts on the current state $(x, t)$—tracking how probability mass spreads over time.

!!! tip "Related Content"

    - [Kolmogorov Backward Equation](kolmogorov_backward.md) — the dual equation for expectations
    - [Forward–Backward Duality](forward_backward_duality.md) — the adjoint relationship
    - [Heat Equation](../heat_equation/heat_equation_overview.md) — Fokker–Planck for Brownian motion
    - [Invariant Measures](../../ch03/diffusion_process/invariant_measures_and_stationarity.md) — stationary distributions

---

### Setting

Consider the Itô diffusion:

$$
dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t
$$

Let $p(x, t \mid x_0, t_0)$ denote the **transition density**:

$$
\mathbb{P}(X_t \in dx \mid X_{t_0} = x_0) = p(x, t \mid x_0, t_0)\,dx
$$

**Convention:**

- $(x_0, t_0)$: initial state and time (fixed parameters)
- $(x, t)$: current state and time (variables the PDE acts on)

!!! note "Notation Variants"
    Different texts use different notations:
    
    - $p(x, t \mid x_0, t_0)$ — conditional notation (used here)
    - $p(t; x_0, x)$ — semicolon separating time from space
    - $p_{t_0, x_0}(x, t)$ — subscript for initial condition
    
    All describe the same object: the probability density of $X_t = x$ given $X_{t_0} = x_0$.

---

### The Fokker–Planck Equation

!!! abstract "Theorem (Fokker–Planck Equation)"
    The transition density satisfies:

    $$
    \boxed{
    \frac{\partial p}{\partial t}(x, t \mid x_0, t_0) = \mathcal{L}_x^* p(x, t \mid x_0, t_0)
    }
    $$

    where $\mathcal{L}^*$ is the **adjoint** of the infinitesimal generator:

    $$
    \boxed{
    \mathcal{L}^* p = -\frac{\partial}{\partial x}[\mu(x,t) p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x,t) p]
    }
    $$

    **Initial condition**: $p(x, t_0 \mid x_0, t_0) = \delta(x - x_0)$

**Regularity conditions**: The theorem requires:

- $\mu(x,t)$ and $\sigma(x,t)$ are sufficiently smooth (typically $C^1$)
- $\sigma(x,t) > 0$ (strict positivity; for uniform ellipticity, need $\sigma(x,t) \geq c > 0$)
- Appropriate boundary conditions (natural, reflecting, or absorbing)

---

### Two Formulations

#### Density Form (Strong)

The PDE for the transition density:

$$
\frac{\partial p}{\partial t} = \mathcal{L}^* p = -\frac{\partial}{\partial x}[\mu \cdot p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2 \cdot p]
$$

#### Expectation Form (Weak)

For any smooth test function $f$ with suitable decay:

$$
\frac{d}{dt}\mathbb{E}[f(X_t) \mid X_{t_0} = x_0] = \mathbb{E}[(\mathcal{L}f)(X_t)]
$$

where the infinitesimal generator is:

$$
\mathcal{L}f(x, t) = \mu(x, t)\frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2(x, t)\frac{\partial^2 f}{\partial x^2}
$$

Equivalently:

$$
\frac{d}{dt}\int_{-\infty}^{\infty} f(x) p(x, t \mid x_0, t_0)\,dx = \int_{-\infty}^{\infty} (\mathcal{L}f)(x) p(x, t \mid x_0, t_0)\,dx
$$

This formulation is **dual** to the density PDE: the generator $\mathcal{L}$ acts on test functions, while its adjoint $\mathcal{L}^*$ acts on densities.

---

### Derivation

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

### Expanded Forms

#### Constant Coefficients

For **constant coefficients** ($\mu, \sigma = \text{const}$), the Fokker–Planck equation simplifies to:

$$
\frac{\partial p}{\partial t} = -\mu\frac{\partial p}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x^2}
$$

This is the **advection–diffusion equation**: probability advects with velocity $\mu$ and diffuses with coefficient $\sigma^2/2$.

#### Variable Coefficients

??? note "Full Expansion for Variable Coefficients"

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

---

### Continuity Form and Probability Current

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
    - **Diffusive current**: $-\frac{1}{2}\frac{\partial}{\partial x}[\sigma^2(x)p]$ — spreading due to noise (Fick's law)

!!! note "Why the Diffusive Current Has This Form"
    The diffusive current $-\frac{1}{2}\partial_x[\sigma^2 p]$ rather than simply $-\frac{\sigma^2}{2}\partial_x p$ arises because:
    
    1. **State-dependent noise**: When $\sigma(x)$ varies, particles in high-volatility regions spread faster
    2. **Spurious drift**: The term $-\frac{1}{2}\sigma\sigma' p$ creates an effective drift toward low-volatility regions
    3. **Itô convention**: This specific form corresponds to the Itô interpretation of the SDE
    
    In the Stratonovich convention, the diffusive current would take a different form.

---

### Examples with Analytical Solutions

#### Example 1: Brownian Motion

For $dX_t = dW_t$ (i.e., $\mu = 0$, $\sigma = 1$):

$$
\frac{\partial p}{\partial t} = \frac{1}{2}\frac{\partial^2 p}{\partial x^2}
$$

This is the **heat equation**. 

**Solution** (heat kernel):

$$
p(x, t \mid x_0, t_0) = \frac{1}{\sqrt{2\pi (t - t_0)}}\exp\left(-\frac{(x - x_0)^2}{2(t - t_0)}\right)
$$

For explicit transition densities of BM with drift, OU, GBM, and CIR,
see [Transition Densities for Standard SDEs](transition_densities_standard_sdes.md).
The following table records only their forward equations.

#### Summary Table

| Process | SDE | Forward Equation | Transition Density |
|---------|-----|------------------|-------------------|
| Brownian Motion | $dX_t = dW_t$ | $\partial_t p = \frac{1}{2}\partial_{xx} p$ | Gaussian, variance $= t$ |
| BM with Drift | $dX_t = \mu\,dt + \sigma\,dW_t$ | $\partial_t p = -\mu\partial_x p + \frac{\sigma^2}{2}\partial_{xx} p$ | Gaussian, mean $= \mu t$ |
| Ornstein–Uhlenbeck | $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ | $\partial_t p = \kappa\partial_x(xp) + \frac{\sigma^2}{2}\partial_{xx} p$ | Gaussian, mean-reverting |
| GBM | $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ | $\partial_t p = -\mu\partial_S(Sp) + \frac{\sigma^2}{2}\partial_{SS}(S^2 p)$ | Log-normal |

---

### Stationary (Invariant) Distributions

A density $p_\infty(x)$ is **stationary** if $\mathcal{L}^* p_\infty = 0$:

$$
-\frac{d}{dx}[\mu(x)p_\infty] + \frac{1}{2}\frac{d^2}{dx^2}[\sigma^2(x)p_\infty] = 0
$$

#### Zero-Current Condition

At stationarity with zero probability current ($J = 0$):

$$
\mu(x)p_\infty = \frac{1}{2}\frac{d}{dx}[\sigma^2(x)p_\infty]
$$

#### General Solution (One Dimension)

$$
p_\infty(x) \propto \frac{1}{\sigma^2(x)}\exp\left(\int^x \frac{2\mu(z)}{\sigma^2(z)}\,dz\right)
$$

!!! warning "Existence Conditions"
    This formula only yields a valid density if:

    1. $\sigma(x) > 0$ for all $x$ in the domain
    2. The integral converges (normalizability)
    3. Boundary conditions are compatible (reflecting or natural)
    4. The process is **positive recurrent** (returns to compact sets in finite expected time)
    
    For example, standard Brownian motion on $\mathbb{R}$ has **no** stationary distribution (it is null recurrent).

#### Physical Interpretation of Stationarity

At equilibrium, the drift and diffusive currents balance:

$$
\underbrace{\mu(x) p_\infty}_{\text{drift current}} = \underbrace{\frac{1}{2}\frac{d}{dx}[\sigma^2(x)p_\infty]}_{\text{diffusive current}}
$$

This is analogous to detailed balance in statistical mechanics.

---

### Analytical Solution Methods

#### Fourier Transform Method

For constant coefficients on $\mathbb{R}$, apply the Fourier transform in $x$:

$$
\hat{p}(k, t) = \int_{-\infty}^{\infty} p(x, t) e^{-ikx}\,dx
$$

The PDE becomes an ODE in $t$:

$$
\frac{\partial \hat{p}}{\partial t} = \left(-ik\mu - \frac{\sigma^2 k^2}{2}\right)\hat{p}
$$

**Solution**: 

$$
\hat{p}(k, t) = \hat{p}(k, t_0) \exp\left[\left(-ik\mu - \frac{\sigma^2 k^2}{2}\right)(t - t_0)\right]
$$

For delta initial condition $p(x, t_0) = \delta(x - x_0)$, we have $\hat{p}(k, t_0) = e^{-ikx_0}$, and the inverse transform yields the Gaussian solution.

#### Similarity Solutions

For the heat equation, exploit scale invariance by seeking solutions of the form:

$$
p(x, t) = \frac{1}{\sqrt{t - t_0}} F\left(\frac{x - x_0}{\sqrt{t - t_0}}\right)
$$

Substituting into the PDE yields an ODE for $F(\eta)$:

$$
\frac{1}{2}F'' + \frac{1}{2}\eta F' + \frac{1}{2}F = 0
$$

whose normalized solution is $F(\eta) = \frac{1}{\sqrt{2\pi}}e^{-\eta^2/2}$.

#### Separation of Variables

On bounded domains $[a, b]$ with homogeneous boundary conditions, expand in eigenfunctions of $\mathcal{L}^*$:

$$
p(x, t) = \sum_n c_n \phi_n(x) e^{-\lambda_n (t - t_0)}
$$

where $\mathcal{L}^* \phi_n = -\lambda_n \phi_n$ with eigenvalues $0 = \lambda_0 < \lambda_1 < \lambda_2 < \cdots$.

The eigenfunction $\phi_0$ with $\lambda_0 = 0$ is the stationary distribution (if it exists).

---

### Numerical Methods

For general coefficients $\mu(x)$ and $\sigma(x)$, analytical solutions are often unavailable.

#### Finite Difference Methods

Discretize the PDE on a grid $(x_i, t_n)$:

| Scheme | Accuracy | Stability | Complexity |
|--------|----------|-----------|------------|
| **Explicit** | $O(\Delta t, \Delta x^2)$ | Conditional (CFL) | Simple |
| **Implicit** | $O(\Delta t, \Delta x^2)$ | Unconditional | Linear solve |
| **Crank–Nicolson** | $O(\Delta t^2, \Delta x^2)$ | Unconditional | Linear solve |

!!! warning "Stability Considerations"
    The advection term $-\mu \partial_x p$ requires care:
    
    - **Central differences** can cause oscillations for advection-dominated problems
    - **Upwind schemes** add numerical diffusion but ensure stability
    - **CFL condition** for explicit schemes: $\Delta t \leq \frac{\Delta x^2}{\sigma^2}$

#### Positivity Preservation

The exact solution satisfies $p \geq 0$ for all $t$. Numerical schemes should preserve this:

- Use **flux-limiting** schemes for advection
- Avoid **Crank–Nicolson** without modification (can produce negative values)
- Consider **operator splitting** for advection-diffusion

#### Monte Carlo Verification

Simulate paths of the SDE and compare the empirical histogram to the PDE solution:

```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_sde(x0, t0, t_final, mu, sigma, n_paths=100000, n_steps=1000):
    """Simulate SDE paths using Euler-Maruyama."""
    dt = (t_final - t0) / n_steps
    X = np.zeros((n_paths, n_steps + 1))
    X[:, 0] = x0
    
    for i in range(n_steps):
        dW = np.sqrt(dt) * np.random.randn(n_paths)
        X[:, i+1] = X[:, i] + mu(X[:, i]) * dt + sigma(X[:, i]) * dW
    
    return X

# Example: Ornstein-Uhlenbeck process
kappa, sigma_val = 1.0, 0.5
mu_func = lambda x: -kappa * x
sigma_func = lambda x: sigma_val * np.ones_like(x)

X = simulate_sde(x0=1.0, t0=0.0, t_final=2.0, mu=mu_func, sigma=sigma_func)

# Compare histogram to analytical solution
tau = 2.0
m_tau = 1.0 * np.exp(-kappa * tau)
v_tau = (sigma_val**2 / (2*kappa)) * (1 - np.exp(-2*kappa*tau))

x_grid = np.linspace(-2, 2, 200)
p_analytical = np.exp(-(x_grid - m_tau)**2 / (2*v_tau)) / np.sqrt(2*np.pi*v_tau)

plt.hist(X[:, -1], bins=100, density=True, alpha=0.7, label='Monte Carlo')
plt.plot(x_grid, p_analytical, 'r-', lw=2, label='Analytical')
plt.xlabel('x')
plt.ylabel('p(x, t)')
plt.legend()
plt.title('Fokker-Planck vs Monte Carlo')
plt.show()
```

---

### Multidimensional Fokker–Planck

For $X_t \in \mathbb{R}^d$ with $dX_t^i = \mu^i(X_t, t)\,dt + \sigma^{i\alpha}(X_t, t)\,dW_t^\alpha$:

$$
\frac{\partial p}{\partial t} = -\sum_{i=1}^{d}\frac{\partial}{\partial x_i}(\mu^i p) + \frac{1}{2}\sum_{i,j=1}^{d}\frac{\partial^2}{\partial x_i \partial x_j}(a^{ij} p)
$$

where the **diffusion matrix** is $a^{ij} = \sum_{\alpha}\sigma^{i\alpha}\sigma^{j\alpha} = (\sigma\sigma^\top)^{ij}$.

In vector notation:

$$
\frac{\partial p}{\partial t} = -\nabla \cdot (\mu p) + \frac{1}{2}\nabla \cdot (a \cdot \nabla p) + \frac{1}{2}p \, \nabla \cdot \nabla \cdot a
$$

!!! note "Ellipticity"
    For classical solutions, we require **uniform ellipticity**: there exists $c > 0$ such that
    
    $$\sum_{i,j} a^{ij}(x,t) \xi_i \xi_j \geq c |\xi|^2 \quad \text{for all } \xi \in \mathbb{R}^d$$
    
    This ensures the equation is genuinely parabolic and has smooth solutions.

---

### Connection to Score Functions and Diffusion Models

!!! tip "Relevance to Generative Models"
    This section connects classical Fokker–Planck theory to modern machine learning. It can be skipped on first reading.

Given a **marginal density** $p(x, t)$, the **score function** is:

$$
s(x, t) = \nabla_x \log p(x, t)
$$

This gradient of the log-density is fundamental to:

- **Score matching** in machine learning
- **Reverse-time SDEs** for diffusion generative models
- **Denoising score matching** in modern generative AI

#### Forward Process

In diffusion models, the forward SDE typically adds noise:

$$
dX_t = f(X_t, t)\,dt + g(t)\,dW_t
$$

The marginal density $p(x, t)$ (starting from data distribution $p_0$) satisfies the Fokker–Planck equation.

#### Reverse Process

The remarkable result (Anderson, 1982) is that the **reverse-time SDE**:

$$
dX_t = \left[f(X_t, t) - g^2(t) \nabla_x \log p(X_t, t)\right] dt + g(t)\,d\bar{W}_t
$$

generates samples from $p(x, t)$ running backward in time, where $\bar{W}_t$ is a backward Brownian motion.

This is the theoretical foundation for:

- **Denoising Diffusion Probabilistic Models (DDPM)**
- **Score-based Generative Models**
- **Stochastic Differential Equation approaches to generation**

The key insight is that the score $\nabla_x \log p$ can be learned from data via denoising score matching, enabling generation without knowing $p$ explicitly.

---

### Physical Interpretation and Applications

The forward equation describes:

1. **Conservation**: Probability mass is conserved (continuity equation form)
2. **Advection**: Probability flows with the drift field $\mu(x)$
3. **Diffusion**: Probability spreads due to the noise term

**Applications:**

| Field | Application |
|-------|-------------|
| **Statistical mechanics** | Brownian particles in a potential |
| **Plasma physics** | Particle velocity distributions |
| **Population dynamics** | Density evolution in space |
| **Chemical kinetics** | Reaction-diffusion systems |
| **Finance** | Evolution of asset price distributions |
| **Neuroscience** | Neural population dynamics |
| **Machine learning** | Diffusion generative models |

---

### Historical Note

- **Adriaan Fokker** (1914): Derived in the context of Brownian motion in a radiation field
- **Max Planck** (1917): Independent derivation for radiation equilibrium problems
- **Andrey Kolmogorov** (1931): Rigorous mathematical foundation establishing the connection to diffusion processes and proving existence/uniqueness

The equation is sometimes called the **Smoluchowski equation** in the physics literature, particularly for overdamped systems.

---

### Summary

$$
\boxed{
\frac{\partial p}{\partial t}(x, t \mid x_0, t_0) = -\frac{\partial}{\partial x}[\mu(x,t)p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x,t)p] = \mathcal{L}^* p
}
$$

The Fokker–Planck equation describes how probability density evolves **forward** in time, dual to the backward equation which describes how expectations depend on initial conditions.

| Aspect | Description |
|--------|-------------|
| **Input** | Initial point mass $\delta(x - x_0)$ |
| **Output** | Spreading probability density $p(x, t)$ |
| **Operator** | Adjoint generator $\mathcal{L}^*$ |
| **Physical meaning** | Conservation of probability with drift and diffusion |
| **Long-time behavior** | Convergence to stationary distribution (if ergodic) |

---

### See Also

- [Kolmogorov Backward Equation](kolmogorov_backward.md) — the dual equation for expectations
- [Forward–Backward Duality](forward_backward_duality.md) — the adjoint relationship in detail
- [Heat Equation Overview](../heat_equation/heat_equation_overview.md) — fundamental solutions
- [Heat Equation and Brownian Motion](../heat_equation/heat_equation_and_brownian_motion.md) — probabilistic connection
- [Invariant Measures](../../ch03/diffusion_process/invariant_measures_and_stationarity.md) — stationary distributions
- [Time Reversal of Diffusions](../../ch03/diffusion_process/time_reversal_of_diffusions.md) — connection to score functions
- [Feynman–Kac Formula](../feynman_kac/feynman_kac_formula.md) — discounted expectations

---

## Exercises

**Exercise 1.**
For Brownian motion with drift $dX_t = \mu\,dt + \sigma\,dW_t$, verify that the Gaussian density

$$
p(x, t \mid x_0, 0) = \frac{1}{\sigma\sqrt{2\pi t}}\exp\left(-\frac{(x - x_0 - \mu t)^2}{2\sigma^2 t}\right)
$$

satisfies the Fokker-Planck equation $\partial_t p = -\mu\partial_x p + \frac{\sigma^2}{2}\partial_{xx} p$ by computing both sides explicitly.

??? success "Solution to Exercise 1"
    The Fokker-Planck equation for constant coefficients is $\partial_t p = -\mu\partial_x p + \frac{\sigma^2}{2}\partial_{xx}p$. Let

    $$
    p(x, t) = \frac{1}{\sigma\sqrt{2\pi t}}\exp\left(-\frac{(x - x_0 - \mu t)^2}{2\sigma^2 t}\right)
    $$

    and define $z = x - x_0 - \mu t$ and $\tau = t$ for convenience. Compute:

    $$
    \frac{\partial p}{\partial t} = p\left(-\frac{1}{2t} + \frac{z^2}{2\sigma^2 t^2} + \frac{\mu z}{\sigma^2 t}\right)
    $$

    (the three terms come from differentiating $(2\pi\sigma^2 t)^{-1/2}$ and the exponential, noting $\partial_t z = -\mu$).

    $$
    \frac{\partial p}{\partial x} = -\frac{z}{\sigma^2 t}p, \qquad \frac{\partial^2 p}{\partial x^2} = \left(\frac{z^2}{\sigma^4 t^2} - \frac{1}{\sigma^2 t}\right)p
    $$

    Now compute the right-hand side:

    $$
    -\mu\frac{\partial p}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x^2} = \frac{\mu z}{\sigma^2 t}p + \frac{\sigma^2}{2}\left(\frac{z^2}{\sigma^4 t^2} - \frac{1}{\sigma^2 t}\right)p
    $$

    $$
    = p\left(\frac{\mu z}{\sigma^2 t} + \frac{z^2}{2\sigma^2 t^2} - \frac{1}{2t}\right) = \frac{\partial p}{\partial t}
    $$

    Both sides are equal, confirming the Gaussian density satisfies the Fokker-Planck equation. $\checkmark$

---

**Exercise 2.**
Write the Fokker-Planck equation in the continuity form $\partial_t p + \partial_x J = 0$ and identify the probability current $J$ for the Ornstein-Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$. At stationarity ($\partial_t p = 0$), show that $J = 0$ and use this to derive the stationary density.

??? success "Solution to Exercise 2"
    For the OU process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, we have $\mu(x) = -\kappa x$ and $\sigma(x) = \sigma$.

    The probability current is:

    $$
    J(x, t) = \mu(x)p - \frac{1}{2}\frac{\partial}{\partial x}[\sigma^2 p] = -\kappa x\,p - \frac{\sigma^2}{2}\frac{\partial p}{\partial x}
    $$

    The continuity form of the Fokker-Planck equation is $\partial_t p + \partial_x J = 0$.

    **At stationarity** ($\partial_t p = 0$): $\partial_x J = 0$, so $J = \text{const}$. For a density on $\mathbb{R}$ that decays at infinity, the current must vanish at $\pm\infty$, so $J = 0$ everywhere.

    Setting $J = 0$:

    $$
    -\kappa x\,p_\infty = \frac{\sigma^2}{2}\frac{dp_\infty}{dx}
    $$

    This is a separable ODE:

    $$
    \frac{dp_\infty}{p_\infty} = -\frac{2\kappa x}{\sigma^2}dx
    $$

    Integrating:

    $$
    \ln p_\infty = -\frac{\kappa x^2}{\sigma^2} + C
    $$

    $$
    p_\infty(x) = A\exp\left(-\frac{\kappa x^2}{\sigma^2}\right)
    $$

    Normalizing: this is a Gaussian with variance $\sigma^2/(2\kappa)$, so $A = \sqrt{\kappa/(\pi\sigma^2)}$ and:

    $$
    p_\infty(x) = \sqrt{\frac{\kappa}{\pi\sigma^2}}\exp\left(-\frac{\kappa x^2}{\sigma^2}\right)
    $$

    This is $N(0, \sigma^2/(2\kappa))$.

---

**Exercise 3.**
For constant coefficients, solve the Fokker-Planck equation using the Fourier transform. Starting from $\partial_t \hat{p} = (-ik\mu - \frac{\sigma^2 k^2}{2})\hat{p}$ with initial condition $\hat{p}(k, 0) = e^{-ikx_0}$, find $\hat{p}(k, t)$ and verify that the inverse transform yields the Gaussian transition density.

??? success "Solution to Exercise 3"
    For constant coefficients, the Fokker-Planck equation in Fourier space is:

    $$
    \frac{\partial\hat{p}}{\partial t} = \left(-ik\mu - \frac{\sigma^2 k^2}{2}\right)\hat{p}
    $$

    This is a first-order linear ODE in $t$ with solution:

    $$
    \hat{p}(k, t) = \hat{p}(k, 0)\exp\left[\left(-ik\mu - \frac{\sigma^2 k^2}{2}\right)t\right]
    $$

    With initial condition $p(x, 0) = \delta(x - x_0)$, the Fourier transform gives $\hat{p}(k, 0) = e^{-ikx_0}$. Therefore:

    $$
    \hat{p}(k, t) = \exp\left[-ik(x_0 + \mu t) - \frac{\sigma^2 t}{2}k^2\right]
    $$

    This is the characteristic function of $N(x_0 + \mu t, \sigma^2 t)$. The inverse Fourier transform gives:

    $$
    p(x, t) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{p}(k, t)e^{ikx}\,dk = \frac{1}{2\pi}\int_{-\infty}^{\infty}\exp\left[ik(x - x_0 - \mu t) - \frac{\sigma^2 t}{2}k^2\right]dk
    $$

    Completing the square in $k$ and evaluating the Gaussian integral:

    $$
    p(x, t) = \frac{1}{\sigma\sqrt{2\pi t}}\exp\left(-\frac{(x - x_0 - \mu t)^2}{2\sigma^2 t}\right)
    $$

    This is the Gaussian transition density. $\checkmark$

---

**Exercise 4.**
For geometric Brownian motion $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$, expand the Fokker-Planck equation

$$
\frac{\partial p}{\partial t} = -\frac{\partial}{\partial S}(\mu S\,p) + \frac{\sigma^2}{2}\frac{\partial^2}{\partial S^2}(S^2\,p)
$$

using the product rule. Identify the effective drift and the "spurious drift" terms that arise from the state-dependent diffusion coefficient.

??? success "Solution to Exercise 4"
    For GBM, $\mu(S) = \mu S$ and $\sigma^2(S) = \sigma^2 S^2$. Expanding the Fokker-Planck equation:

    **Drift term:**

    $$
    -\frac{\partial}{\partial S}(\mu S\,p) = -\mu p - \mu S\frac{\partial p}{\partial S}
    $$

    **Diffusion term** (using the product rule twice):

    $$
    \frac{\sigma^2}{2}\frac{\partial^2}{\partial S^2}(S^2 p) = \frac{\sigma^2}{2}\frac{\partial}{\partial S}\left(2Sp + S^2\frac{\partial p}{\partial S}\right) = \frac{\sigma^2}{2}\left(2p + 4S\frac{\partial p}{\partial S} + S^2\frac{\partial^2 p}{\partial S^2}\right)
    $$

    **Combined:**

    $$
    \frac{\partial p}{\partial t} = (\sigma^2 - \mu)p + (2\sigma^2 - \mu)S\frac{\partial p}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 p}{\partial S^2}
    $$

    **Identifying the terms:**

    - **Standard diffusion**: $\frac{\sigma^2 S^2}{2}\partial_{SS}p$ — this is the usual second-order diffusion term.
    - **Effective drift on $p$**: $(2\sigma^2 - \mu)S\partial_S p$ — this combines the physical drift $-\mu S$ with additional terms from differentiating $\sigma^2 S^2$.
    - **Spurious drift terms**: The $\sigma^2 p$ and $2\sigma^2 S\partial_S p$ contributions arise because $\sigma(S) = \sigma S$ depends on $S$. When the diffusion coefficient varies in space, differentiating $\sigma^2(S)p$ produces extra terms beyond $\frac{\sigma^2(S)}{2}\partial_{SS}p$. The term $\sigma^2 p$ is analogous to a zeroth-order "source" or "sink" of probability, while $2\sigma^2 S\partial_S p$ acts as an additional advective flux. These spurious drift effects cause probability mass to flow from high-volatility regions (large $S$) toward low-volatility regions.

---

**Exercise 5.**
The general formula for the stationary density of a one-dimensional diffusion is

$$
p_\infty(x) \propto \frac{1}{\sigma^2(x)}\exp\left(\int^x \frac{2\mu(z)}{\sigma^2(z)}\,dz\right)
$$

Apply this formula to the CIR process $dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t$ and show that the stationary density is a Gamma distribution. What condition on the parameters ensures the density is normalizable?

??? success "Solution to Exercise 5"
    For the CIR process, $\mu(x) = \kappa(\theta - x)$ and $\sigma^2(x) = \xi^2 x$. The general stationary density formula gives:

    $$
    p_\infty(x) \propto \frac{1}{\xi^2 x}\exp\left(\int^x\frac{2\kappa(\theta - z)}{\xi^2 z}\,dz\right)
    $$

    Evaluate the integral:

    $$
    \int^x\frac{2\kappa(\theta - z)}{\xi^2 z}\,dz = \frac{2\kappa}{\xi^2}\int^x\left(\frac{\theta}{z} - 1\right)dz = \frac{2\kappa}{\xi^2}(\theta\ln x - x)
    $$

    Therefore:

    $$
    p_\infty(x) \propto \frac{1}{\xi^2 x}\exp\left(\frac{2\kappa\theta}{\xi^2}\ln x - \frac{2\kappa x}{\xi^2}\right) = \frac{1}{\xi^2}x^{2\kappa\theta/\xi^2 - 1}\exp\left(-\frac{2\kappa x}{\xi^2}\right)
    $$

    This is the density of a **Gamma distribution** with shape parameter $\alpha = 2\kappa\theta/\xi^2$ and rate parameter $\beta = 2\kappa/\xi^2$:

    $$
    p_\infty(x) = \frac{\beta^\alpha}{\Gamma(\alpha)}x^{\alpha - 1}e^{-\beta x}, \qquad x > 0
    $$

    **Normalizability condition**: The Gamma density is normalizable if and only if $\alpha > 0$, i.e.:

    $$
    \frac{2\kappa\theta}{\xi^2} > 0
    $$

    Since $\kappa, \theta > 0$, this is always satisfied. The stronger Feller condition $2\kappa\theta \geq \xi^2$ (i.e., $\alpha \geq 1$) ensures the density is bounded at the origin.

---

**Exercise 6.**
On a bounded domain $[a, b]$ with homogeneous boundary conditions, the Fokker-Planck solution can be expanded in eigenfunctions: $p(x, t) = \sum_n c_n \phi_n(x) e^{-\lambda_n t}$. For the heat equation on $[0, L]$ with absorbing boundaries, identify the eigenvalues $\lambda_n$ and eigenfunctions $\phi_n$. What is the long-time behavior of $p(x, t)$?

??? success "Solution to Exercise 6"
    On $[0, L]$ with absorbing (Dirichlet) boundaries $p(0, t) = p(L, t) = 0$, the heat equation $\partial_t p = \frac{1}{2}\partial_{xx}p$ is solved by separation of variables.

    Write $p(x, t) = X(x)T(t)$. Then $T'/T = \frac{1}{2}X''/X = -\lambda$ (separation constant). This gives:

    $$
    X'' + 2\lambda X = 0, \qquad X(0) = X(L) = 0
    $$

    The eigenvalues and eigenfunctions are:

    $$
    \lambda_n = \frac{n^2\pi^2}{2L^2}, \qquad \phi_n(x) = \sin\left(\frac{n\pi x}{L}\right), \qquad n = 1, 2, 3, \ldots
    $$

    The time part gives $T_n(t) = e^{-\lambda_n t}$. The general solution is:

    $$
    p(x, t) = \sum_{n=1}^{\infty}c_n\sin\left(\frac{n\pi x}{L}\right)\exp\left(-\frac{n^2\pi^2 t}{2L^2}\right)
    $$

    where $c_n$ are determined by the initial condition.

    **Long-time behavior**: As $t \to \infty$, the dominant term is $n = 1$ (smallest eigenvalue):

    $$
    p(x, t) \approx c_1\sin\left(\frac{\pi x}{L}\right)\exp\left(-\frac{\pi^2 t}{2L^2}\right)
    $$

    The density decays exponentially to zero at rate $\lambda_1 = \pi^2/(2L^2)$. This makes physical sense: with absorbing boundaries, all probability is eventually absorbed, so $p \to 0$. There is no stationary distribution (the eigenvalue $\lambda_0 = 0$ does not appear because $\sin(0) = 0$ fails to satisfy the boundary conditions nontrivially).

---

**Exercise 7.**
The score function is defined as $s(x, t) = \nabla_x \log p(x, t)$. For a Gaussian density $p(x, t) = \frac{1}{\sqrt{2\pi v(t)}}\exp(-(x - m(t))^2/(2v(t)))$, compute the score function explicitly. Explain why the reverse-time SDE uses the score to denoise: the drift $-g^2(t)\nabla_x \log p$ points toward regions of higher probability density.

??? success "Solution to Exercise 7"
    For the Gaussian density $p(x, t) = \frac{1}{\sqrt{2\pi v(t)}}\exp\left(-\frac{(x - m(t))^2}{2v(t)}\right)$:

    $$
    \log p(x, t) = -\frac{1}{2}\log(2\pi v(t)) - \frac{(x - m(t))^2}{2v(t)}
    $$

    The score function is:

    $$
    s(x, t) = \frac{\partial}{\partial x}\log p(x, t) = -\frac{x - m(t)}{v(t)}
    $$

    **Interpretation**: The score points toward the mean $m(t)$:

    - If $x > m(t)$: $s(x,t) < 0$, pointing left (toward the mean)
    - If $x < m(t)$: $s(x,t) > 0$, pointing right (toward the mean)
    - The magnitude $|s| = |x - m(t)|/v(t)$ is larger when $x$ is far from the mean or when the variance is small (sharp peak)

    **Why the reverse-time SDE uses the score for denoising**: In the reverse-time SDE, the drift contains the term $-g^2(t)\nabla_x\log p$. Since the score $\nabla_x\log p$ always points in the direction of increasing probability density, the contribution $-g^2(t)\nabla_x\log p$ acts as a drift that pushes samples toward regions of higher probability density. During the forward process, noise is added, spreading the distribution. The reverse process must undo this: the score-based drift counteracts diffusion by steering samples back toward the high-density regions of the data distribution, effectively denoising the signal.
