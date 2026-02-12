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
