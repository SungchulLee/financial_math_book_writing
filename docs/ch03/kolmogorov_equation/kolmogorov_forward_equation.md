# Kolmogorov Forward Equation

The **Kolmogorov forward equation** describes how the probability distribution of a diffusion process evolves forward in time. It is also known as the **Fokker–Planck equation**.

!!! tip "Related Content"
    For probabilistic derivation and connection to generators, see [Fokker–Planck (SDE Perspective)](../../ch02/infinitesimal_generator/fokker_planck.md).

---

## The Equation

Consider the Itô diffusion:

$$
dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t
$$

Let $p(x, t \mid x_0, t_0)$ denote the transition density:

$$
\mathbb{P}(X_t \in dx \mid X_{t_0} = x_0) = p(x, t \mid x_0, t_0)\,dx
$$

!!! abstract "Kolmogorov Forward Equation"
    The transition density satisfies:

    $$
    \frac{\partial p}{\partial t}(x, t \mid x_0, t_0) = -\frac{\partial}{\partial x}[\mu(x,t) \cdot p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x,t) \cdot p]
    $$

    **Initial condition**: $p(x, t_0 \mid x_0, t_0) = \delta(x - x_0)$

**Notation convention:**

- $(x_0, t_0)$: initial state and time (fixed)
- $(x, t)$: current state and time (the PDE variables)
- The equation evolves $p$ **forward** in $t$

---

## Two Formulations

### Density Form (Strong)

The PDE for the transition density:

$$
\frac{\partial p}{\partial t} = \mathcal{L}^* p = -\frac{\partial}{\partial x}[\mu \cdot p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2 \cdot p]
$$

### Expectation Form (Weak)

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

## Derivation

??? abstract "Derivation from Itô's Lemma"

    **Step 1**: Apply Itô's lemma to $f(X_t)$:

    $$
    df(X_t) = \left(\mu \frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2}\right)dt + \sigma \frac{\partial f}{\partial x}\,dW_t
    $$

    **Step 2**: Take expectations (the martingale term vanishes):

    $$
    \frac{d}{dt}\mathbb{E}[f(X_t)] = \mathbb{E}\left[\mu \frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2}\right]
    $$

    **Step 3**: Write expectations via the density:

    $$
    \frac{d}{dt}\int f(x) p(x,t)\,dx = \int (\mathcal{L}f)(x) p(x,t)\,dx
    $$

    **Step 4**: Integrate by parts to transfer derivatives from $f$ onto $p$:

    $$
    \int f(x) \frac{\partial p}{\partial t}\,dx = \int f(x) \left[-\frac{\partial}{\partial x}(\mu p) + \frac{1}{2}\frac{\partial^2}{\partial x^2}(\sigma^2 p)\right]dx
    $$

    **Step 5**: Since this holds for all test functions $f$, the integrands must be equal, yielding the Fokker–Planck equation.

---

## Examples with Solutions

| Process | SDE | Forward Equation | Solution $p(x, t \mid x_0, t_0)$ |
|---------|-----|------------------|----------------------------------|
| Brownian Motion | $dX_t = dW_t$ | $\partial_t p = \frac{1}{2}\partial_{xx} p$ | $\frac{1}{\sqrt{2\pi\tau}} e^{-\frac{(x-x_0)^2}{2\tau}}$ |
| BM with Drift | $dX_t = \mu\,dt + \sigma\,dW_t$ | $\partial_t p = -\mu\partial_x p + \frac{\sigma^2}{2}\partial_{xx} p$ | $\frac{1}{\sigma\sqrt{2\pi\tau}} e^{-\frac{(x-x_0-\mu\tau)^2}{2\sigma^2\tau}}$ |
| Ornstein–Uhlenbeck | $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ | $\partial_t p = \kappa\partial_x(xp) + \frac{\sigma^2}{2}\partial_{xx} p$ | Gaussian (see below) |
| GBM | $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ | $\partial_t p = -\mu\partial_S(Sp) + \frac{\sigma^2}{2}\partial_{SS}(S^2 p)$ | Log-normal |

where $\tau = t - t_0$.

### Ornstein–Uhlenbeck Details

The OU process has Gaussian transition density:

$$
p(x, t \mid x_0, t_0) = \frac{1}{\sqrt{2\pi v(\tau)}}\exp\left(-\frac{(x - m(\tau))^2}{2v(\tau)}\right)
$$

with $\tau = t - t_0$ and:

- Mean: $m(\tau) = x_0 e^{-\kappa\tau}$
- Variance: $v(\tau) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\tau})$

As $\tau \to \infty$, the distribution converges to the stationary Gaussian with variance $\frac{\sigma^2}{2\kappa}$.

---

## Connection to Heat Equation

For **standard Brownian motion** ($\mu = 0$, $\sigma = 1$), the forward equation becomes:

$$
\frac{\partial p}{\partial t} = \frac{1}{2}\frac{\partial^2 p}{\partial x^2}
$$

This is the **heat equation** (with diffusion coefficient $1/2$).

The solution is the **heat kernel** (fundamental solution):

$$
p(x, t \mid x_0, t_0) = \frac{1}{\sqrt{2\pi(t - t_0)}}\exp\left(-\frac{(x - x_0)^2}{2(t - t_0)}\right)
$$

See [Heat Equation Overview](../heat_equation/heat_equation_overview.md) and [Heat Equation and Brownian Motion](../heat_equation/heat_equation_and_brownian_motion.md) for detailed analysis.

---

## Analytical Solution Methods

### Fourier Transform

For constant coefficients on $\mathbb{R}$, apply the Fourier transform in $x$:

$$
\hat{p}(k, t) = \int_{-\infty}^{\infty} p(x, t) e^{-ikx}\,dx
$$

The PDE becomes an ODE in $t$:

$$
\frac{\partial \hat{p}}{\partial t} = \left(-ik\mu - \frac{\sigma^2 k^2}{2}\right)\hat{p}
$$

**Solution**: $\hat{p}(k, t) = \hat{p}(k, t_0) \exp\left[\left(-ik\mu - \frac{\sigma^2 k^2}{2}\right)(t - t_0)\right]$

Inverse transform yields the Gaussian solution.

### Similarity Solutions

For the heat equation, look for solutions of the form:

$$
p(x, t) = \frac{1}{\sqrt{t - t_0}} F\left(\frac{x - x_0}{\sqrt{t - t_0}}\right)
$$

Substituting into the PDE yields an ODE for $F$, whose solution is Gaussian.

### Separation of Variables

On bounded domains with homogeneous boundary conditions, expand in eigenfunctions of $\mathcal{L}^*$:

$$
p(x, t) = \sum_n c_n \phi_n(x) e^{-\lambda_n (t - t_0)}
$$

See [Heat Equation: Separation of Variables](../../ch05/bs_pde_analytic_solution/separation_of_variables.md).

---

## Numerical Methods

For general coefficients $\mu(x)$ and $\sigma(x)$, analytical solutions are often unavailable. Numerical approaches include:

### Finite Difference Methods

Discretize the PDE on a grid $(x_i, t_n)$:

- **Explicit scheme**: Simple but conditionally stable (CFL condition)
- **Implicit scheme**: Unconditionally stable, requires solving linear systems
- **Crank–Nicolson**: Second-order accurate, good balance

!!! warning "Stability Considerations"
    The advection term $-\mu \partial_x p$ requires care—pure central differences can cause oscillations. Upwind schemes or artificial diffusion may be needed for advection-dominated problems.

See [Finite Difference Methods](../../ch05/bs_pde_numerical_solution/finite_difference_methods.md) for implementation details.

### Monte Carlo Verification

Simulate many paths of the SDE and compare the empirical histogram to the PDE solution:

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

# Example: Ornstein-Uhlenbeck
kappa, sigma_val = 1.0, 0.5
mu = lambda x: -kappa * x
sigma = lambda x: sigma_val * np.ones_like(x)

X = simulate_sde(x0=1.0, t0=0.0, t_final=2.0, mu=mu, sigma=sigma)

# Compare histogram to analytical solution
plt.hist(X[:, -1], bins=100, density=True, alpha=0.7, label='Monte Carlo')
# Add analytical Gaussian for comparison
```

---

## Physical Interpretation

The forward equation describes:

1. **Conservation**: Probability mass is conserved (continuity equation form)
2. **Advection**: Probability flows with the drift field $\mu(x)$
3. **Diffusion**: Probability spreads due to the noise term

**Applications:**

- Statistical mechanics (Brownian particles in a potential)
- Plasma physics (particle distributions)
- Population dynamics (density evolution)
- Chemical kinetics (reaction-diffusion systems)
- Finance (evolution of asset price distributions)

---

## Comparison: Forward vs Backward

| Aspect | Forward (Fokker–Planck) | Backward (Kolmogorov) |
|--------|------------------------|----------------------|
| **Variables** | Current $(x, t)$ | Initial $(x_0, t_0)$ |
| **Equation** | $\partial_t p = \mathcal{L}_x^* p$ | $\partial_{t_0} p + \mathcal{L}_{x_0} p = 0$ |
| **Time direction** | Evolve forward | Evolve backward |
| **Question** | "Where will it be?" | "Where did it start?" |
| **Primary use** | Density evolution, invariant measures | Pricing, expected values |

See [Kolmogorov Backward Equation](kolmogorov_backward_equation.md) for the dual formulation.

---

## Summary

The Kolmogorov forward equation:

$$
\boxed{
\frac{\partial p}{\partial t}(x, t \mid x_0, t_0) = -\frac{\partial}{\partial x}[\mu(x) p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x) p]
}
$$

evolves the probability density **forward** in time, describing how an initial point mass $\delta(x - x_0)$ spreads into a distribution.

---

## See Also

- [Fokker–Planck (SDE Perspective)](../../ch02/infinitesimal_generator/fokker_planck.md) — probabilistic derivation, adjoint operators
- [Kolmogorov Backward Equation](kolmogorov_backward_equation.md) — the dual equation
- [Heat Equation Overview](../heat_equation/heat_equation_overview.md) — fundamental solutions
- [Heat Equation and Brownian Motion](../heat_equation/heat_equation_and_brownian_motion.md) — probabilistic connection
- [Finite Difference Methods](../../ch05/bs_pde_numerical_solution/finite_difference_methods.md) — numerical implementation
