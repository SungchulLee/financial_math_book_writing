# Fokker-Planck for Financial Models

The Fokker-Planck equation describes the evolution of probability density functions for diffusion processes. It is the forward equation counterpart to the backward Kolmogorov equation and provides crucial insights into the probability distribution of asset prices under various financial models.

## Key Concepts

**Forward Equation (Fokker-Planck)**
For a diffusion process $dX_t = \mu(X_t, t) dt + \sigma(X_t, t) dB_t$, the Fokker-Planck equation governs the probability density $p(x, t)$:
$$\frac{\partial p}{\partial t} = -\frac{\partial}{\partial x}[\mu(x, t) p(x, t)] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x, t) p(x, t)]$$

**Geometric Brownian Motion (GBM)**
For GBM: $dS_t = \mu S_t dt + \sigma S_t dB_t$

The Fokker-Planck equation is:
$$\frac{\partial p}{\partial t} = -\mu \frac{\partial(xp)}{\partial x} + \frac{1}{2}\sigma^2 \frac{\partial^2(x^2 p)}{\partial x^2}$$

In log-space with $y = \ln(x)$, the density becomes Gaussian:
$$p(y, t) = \frac{1}{\sigma\sqrt{2\pi t}} \exp\left(-\frac{(y - \mu t)^2}{2\sigma^2 t}\right)$$

**Cox-Ingersoll-Ross (CIR) Model**
For interest rates: $dr_t = \kappa(\theta - r_t) dt + \sqrt{\gamma r_t} dB_t$

The Fokker-Planck equation yields a non-central chi-square distribution under specific parameter conditions, enabling analytical computation of transition probabilities.

**Mean-Reverting Processes**
For Ornstein-Uhlenbeck type processes, the Fokker-Planck equation has steady-state solutions that represent long-run probability distributions, independent of initial conditions.

**Conditional Distribution Properties**
The Fokker-Planck equation determines:
- Conditional transition densities $p(x, t | x_0, 0)$
- Moments and moment dynamics
- Boundary behavior and absorption probabilities

!!! note "Practical Significance"
    Fokker-Planck equations enable:
    - Analytical computation of option prices (no boundary conditions needed unlike PDEs)
    - Calibration of model parameters to observed density features
    - Risk management through understanding the distribution of future asset values
    - Construction of transition probability matrices for discrete approximations

---

## QuantPie Derivation

### Fokker-Planck Equation for Brownian Motion

For Brownian motion $dX_t = dB_t$, the probability density $p(x, t)$ satisfies:

$$
\frac{\partial p}{\partial t} = \frac{1}{2}\frac{\partial^2 p}{\partial x^2}
$$

**Derivation using Itô's Lemma:**

For any test function $f$ in $C_c^2$ (twice continuously differentiable with compact support):

$$
df(B_t) = f'(B_t)dB_t + \frac{1}{2}f''(B_t)dt
$$

Taking expectations:
$$
\frac{d}{dt}\mathbb{E}[f(B_t)] = \frac{1}{2}\mathbb{E}[f''(B_t)]
$$

Using the transition density function $p(x, t)$:

$$
\mathbb{E}[f] = \int_{-\infty}^{\infty} f(x)p(x, t)dx
$$

$$
\frac{d}{dt}\mathbb{E}[f] = \int_{-\infty}^{\infty} f(x)\frac{\partial p}{\partial t}dx
$$

**Integration by parts** (assuming boundary terms vanish):

$$
\mathbb{E}[f''(x)] = \int_{-\infty}^{\infty} f''(x)p(x, t)dx = \int_{-\infty}^{\infty} f(x)p_{xx}(x, t)dx
$$

Therefore:
$$
\int_{-\infty}^{\infty} f(x)\left[\frac{\partial p}{\partial t} - \frac{1}{2}p_{xx}\right]dx = 0
$$

Since this holds for all test functions:
$$
\boxed{\frac{\partial p}{\partial t} = \frac{1}{2}\frac{\partial^2 p}{\partial x^2}}
$$

### Fokker-Planck for General Diffusions

For a general SDE:
$$
dX_t = \mu(X_t, t)dt + \sigma(X_t, t)dB_t
$$

Applying Itô's Lemma:
$$
df = \left(\mu f_x + \frac{1}{2}\sigma^2 f_{xx}\right)dt + \sigma f_x dB_t
$$

Taking expectations and using integration by parts:

$$
\boxed{
\frac{\partial p}{\partial t} = -\frac{\partial(\mu p)}{\partial x} + \frac{1}{2}\frac{\partial^2(\sigma^2 p)}{\partial x^2}
}
$$

**Key examples:**

| Process | SDE | Fokker-Planck |
|---------|-----|---------------|
| **Brownian Motion** | $dX_t = dB_t$ | $\frac{\partial p}{\partial t} = \frac{1}{2}\frac{\partial^2 p}{\partial x^2}$ |
| **Ornstein-Uhlenbeck** | $dX_t = -\kappa X_t dt + \sigma dB_t$ | $\frac{\partial p}{\partial t} = \kappa\frac{\partial(xp)}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 p}{\partial x^2}$ |
| **Geometric Brownian Motion** | $dX_t = \mu X_t dt + \sigma X_t dB_t$ | $\frac{\partial p}{\partial t} = -\mu\frac{\partial(xp)}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2(x^2 p)}{\partial x^2}$ |

### Connection to Kolmogorov Equations

The **Fokker-Planck equation** is the **forward Kolmogorov equation** - it describes how the probability density evolves forward in time. In contrast, the backward Kolmogorov equation describes how solutions to PDE problems evolve backward in time (relevant for pricing and expected values).

**Forward vs Backward:**

| Aspect | Forward (Fokker-Planck) | Backward |
|--------|------------------------|----------|
| **Variables** | $x, t$ (forward time) | $x_0, t_0$ (backward time) |
| **Describes** | Evolution of density | PDE for expected values |
| **Application** | Probability distributions | Option pricing, exit times |
| **Boundary Conditions** | Initial condition required | Terminal condition required |
