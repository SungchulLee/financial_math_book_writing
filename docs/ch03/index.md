# Chapter 3: Stochastic Differential Equations

This chapter introduces stochastic differential equations (SDEs), the cornerstone of modern quantitative finance. SDEs extend ordinary differential equations to include random perturbations, enabling the modeling of asset dynamics under uncertainty.

## Key Concepts

**Empirical Motivation**
Asset returns exhibit randomness and volatility that classical deterministic models cannot capture. The geometric Brownian motion model, driven by Brownian motion increments, provides a natural framework for modeling asset prices with realistic properties including continuous paths and log-normal distributions.

**Ito Integration**
Ito integration extends classical calculus to stochastic processes. Unlike Riemann integration, Ito integrals cannot be evaluated using standard calculus because the sample paths of Brownian motion are nowhere differentiable.
$$I_t = \int_0^t f(s) dB_s$$
Key properties include:
- Martingale property under appropriate integrability conditions
- Ito isometry: $E[I_t^2] = E[\int_0^t f^2(s) ds]$

**Ito's Formula**
Ito's formula is the stochastic counterpart to the chain rule of ordinary calculus:
$$df(B_t, t) = \frac{\partial f}{\partial t} dt + \frac{\partial f}{\partial x} dB_t + \frac{1}{2}\frac{\partial^2 f}{\partial x^2} dt$$
The additional $\frac{1}{2}\frac{\partial^2 f}{\partial x^2}$ term is the hallmark of stochastic calculus and arises from the quadratic variation of Brownian motion.

**Stochastic Differential Equations**
An SDE has the general form:
$$dX_t = \mu(X_t, t) dt + \sigma(X_t, t) dB_t$$
where $\mu$ is the drift and $\sigma$ is the volatility or diffusion coefficient.

**Existence and Uniqueness Theorems**
Under standard conditions (Lipschitz continuity and linear growth), SDEs have unique strong solutions. These conditions ensure well-defined and stable dynamics for numerical approximation.

**Diffusion Processes**
Solutions to SDEs are called diffusion processes, which are continuous-time Markov processes with continuous sample paths. They are completely characterized by their drift and diffusion coefficients.

**Generators**
The infinitesimal generator $\mathcal{L}$ of a diffusion process captures how the conditional mean evolves:
$$\mathcal{L}f = \mu \frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2}$$
Generators connect SDEs to PDEs and are fundamental in the connection between diffusion processes and their associated differential operators.

!!! warning "Important Distinction"
    Ito vs. Stratonovich integrals give different results. The Ito convention is standard in finance due to its martingale properties and lack of anticipating arguments. Stratonovich integrals are more natural from a physics perspective but require adjustment in financial applications.
