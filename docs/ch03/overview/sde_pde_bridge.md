# The SDE–PDE Bridge

This chapter explores the profound connection between **stochastic differential equations** (SDEs) and **partial differential equations** (PDEs). The infinitesimal generator serves as the bridge, transforming questions about random processes into deterministic equations.

!!! quote "The Central Theme"
    **Expected values of diffusion processes satisfy partial differential equations.**

This single insight underlies option pricing, filtering theory, quantum mechanics, and much of modern applied mathematics.

---

## Why Do PDEs Arise from SDEs?

Consider a diffusion process $X_t$ and ask: "What is the expected value of some quantity $g(X_T)$, given that the process starts at $X_0 = x$?"

$$u(x) = \mathbb{E}[g(X_T) \mid X_0 = x]$$

This is a **function of the starting point** $x$. The remarkable fact is that this function satisfies a PDE—even though the underlying process is random.

### The Intuition

Think of $u(x)$ as a "value function" that tells you the expected outcome starting from position $x$. As you vary $x$:

- **Nearby points** should have similar values (continuity)
- The **local dynamics** of the SDE determine how values propagate (the generator)
- **Time evolution** follows from the Markov property

These constraints force $u$ to satisfy a specific PDE.

### A Simple Example

For Brownian motion $X_t = W_t$ with $g(x) = x^2$:

$$u(t, x) = \mathbb{E}[(x + W_t)^2] = x^2 + t$$

This function satisfies the heat equation:

$$\frac{\partial u}{\partial t} = \frac{1}{2}\frac{\partial^2 u}{\partial x^2}$$

The connection is not coincidental—it's structural.

---

## The Generator: Foundation of Everything

For the diffusion $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$, the **infinitesimal generator** is:

$$\boxed{\mathcal{L} = \mu(x)\frac{\partial}{\partial x} + \frac{\sigma^2(x)}{2}\frac{\partial^2}{\partial x^2}}$$

The generator captures:

- **First-order term** $\mu(x)\partial_x$: the deterministic drift
- **Second-order term** $\frac{\sigma^2(x)}{2}\partial_{xx}$: the random fluctuations

It **uniquely characterizes** the process in law (via the martingale problem).

### What the Generator Tells Us

For any smooth function $f$:

$$(\mathcal{L}f)(x) = \lim_{t \downarrow 0} \frac{\mathbb{E}_x[f(X_t)] - f(x)}{t}$$

This is the **instantaneous expected rate of change** of $f(X_t)$ when starting from $x$.

---

## The Hierarchy of Descriptions

The SDE–PDE connection unfolds through a hierarchy:

```
┌─────────────────────────────────────┐
│         INFINITESIMAL GENERATOR     │
│    (local dynamics, t → 0 limit)    │
└─────────────────┬───────────────────┘
                  │ Markov property extends to finite time
                  ▼
┌─────────────────────────────────────┐
│      KOLMOGOROV BACKWARD EQUATION   │
│   ∂ₜu = Lu   (expected values)      │
└─────────────────┬───────────────────┘
                  │ integration by parts (duality)
                  ▼
┌─────────────────────────────────────┐
│      KOLMOGOROV FORWARD EQUATION    │
│   ∂ₜp = L*p   (probability density) │
└─────────────────┬───────────────────┘
                  │ add discounting/killing
                  ▼
┌─────────────────────────────────────┐
│         FEYNMAN–KAC FORMULA         │
│   ∂ₜu + Lu - ru = 0  (pricing)      │
└─────────────────────────────────────┘
```

Each level answers a different question:

| Level | Object | Equation | Question Answered |
|-------|--------|----------|-------------------|
| **Generator** | $\mathcal{L}$ | $(\mathcal{L}f)(x) = \lim_{t\downarrow 0}\frac{\mathbb{E}_x[f(X_t)] - f(x)}{t}$ | What happens infinitesimally? |
| **Backward** | $u(t,x) = \mathbb{E}_x[g(X_t)]$ | $\partial_t u = \mathcal{L}u$ | Expected value starting from $x$? |
| **Forward** | $p(x,t)$ density | $\partial_t p = \mathcal{L}^* p$ | Where does probability mass go? |
| **Feynman–Kac** | $u(t,x) = \mathbb{E}_x[e^{-\int r \, ds} g(X_T)]$ | $\partial_t u + \mathcal{L}u - ru = 0$ | Discounted expected value? |

---

## The Three Fundamental PDEs

### 1. Kolmogorov Backward Equation

$$\frac{\partial u}{\partial t} = \mathcal{L} u, \quad u(0, x) = g(x)$$

**Solution**: $u(t, x) = \mathbb{E}[g(X_t) \mid X_0 = x]$

**Interpretation**: How expected values evolve forward in time.

**Applications**: 

- Transition probabilities
- Heat equation (for Brownian motion)
- Expected hitting times

See [Kolmogorov Backward Equation](../kolmogorov_equations/kolmogorov_backward.md).

### 2. Kolmogorov Forward Equation (Fokker–Planck)

$$\frac{\partial p}{\partial t} = \mathcal{L}^* p, \quad p(x, 0) = \delta(x - x_0)$$

**Solution**: $p(x, t)$ is the probability density of $X_t$ given $X_0 = x_0$.

**Interpretation**: How probability density spreads over time.

**Applications**:

- Evolution of distributions
- Stationary distributions ($\mathcal{L}^* p_\infty = 0$)
- Score functions in diffusion models

See [Kolmogorov Forward Equation](../kolmogorov_equations/kolmogorov_forward.md).

### 3. Feynman–Kac Formula

$$\frac{\partial u}{\partial t} + \mathcal{L} u - r(x)u = 0, \quad u(T, x) = g(x)$$

**Solution**: $u(t, x) = \mathbb{E}\left[e^{-\int_t^T r(X_s) ds} g(X_T) \mid X_t = x\right]$

**Interpretation**: Discounted expected values (present value of future payoff).

**Applications**:

- Option pricing (Black–Scholes PDE)
- Bond pricing with stochastic rates
- Optimal stopping problems

See [Feynman–Kac Formula](../feynman_kac/feynman_kac_formula.md).

---

## Forward vs Backward: The Duality

The backward and forward equations are **adjoints** of each other, connected by integration by parts.

| Aspect | Backward | Forward |
|--------|----------|---------|
| **Equation** | $\partial_t u = \mathcal{L} u$ | $\partial_t p = \mathcal{L}^* p$ |
| **Operator** | $\mathcal{L}$ (generator) | $\mathcal{L}^*$ (adjoint) |
| **Acts on** | Test functions / payoffs | Probability densities |
| **Initial/terminal** | Initial condition $g$ | Initial point mass $\delta$ |
| **Question** | "Expected value of $g$?" | "Where is the mass?" |
| **Time direction** | Information flows backward | Density flows forward |

**The duality relation**:

$$\int_{\mathbb{R}} f(x) (\mathcal{L}g)(x) \, dx = \int_{\mathbb{R}} (\mathcal{L}^* f)(x) g(x) \, dx$$

This connects the two perspectives:

$$\mathbb{E}[g(X_T)] = \int g(x) p(x, T) \, dx$$

The backward equation gives $\mathbb{E}[g(X_T)]$ directly; the forward equation gives the density $p$ which you integrate against $g$.

See [Forward–Backward Duality](../kolmogorov_equations/forward_backward_duality.md).

---

## The Transition Density: Where Both Meet

The transition density $p(x, t \mid x_0, t_0)$ satisfies **both** equations simultaneously:

- **Backward** in $(x_0, t_0)$: $\partial_{t_0} p + \mathcal{L}_{x_0} p = 0$
- **Forward** in $(x, t)$: $\partial_t p = \mathcal{L}_x^* p$

This is a deep fact: the same object satisfies two different PDEs in different variables.

**Physical interpretation**:

- Fix the **destination** $(x, t)$, vary the **origin** $(x_0, t_0)$ → backward equation
- Fix the **origin** $(x_0, t_0)$, vary the **destination** $(x, t)$ → forward equation

---

## Applications Overview

### Finance: Option Pricing

The Black–Scholes PDE:

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} = rV$$

is exactly the Feynman–Kac equation for geometric Brownian motion with constant discounting.

**Key insight**: Pricing = solving a PDE = computing an expectation under the risk-neutral measure.

### Physics: Heat Conduction and Diffusion

The heat equation:

$$\frac{\partial T}{\partial t} = \kappa \frac{\partial^2 T}{\partial x^2}$$

is the Fokker–Planck equation for Brownian motion. Temperature evolution = probability density evolution.

### Machine Learning: Diffusion Models

Score-based generative models use:

- **Forward process**: Add noise via SDE, density evolves by Fokker–Planck
- **Reverse process**: Remove noise using learned score $\nabla \log p$
- **Training**: Match the score function

The entire framework rests on the SDE–PDE connection.

### Filtering: Kalman and Beyond

The Zakai equation for nonlinear filtering:

$$d\rho_t = \mathcal{L}^* \rho_t \, dt + \rho_t h(x) \, dY_t$$

combines Fokker–Planck evolution with measurement updates.

---

## Chapter Roadmap

This chapter develops the SDE–PDE connection systematically:

### Heat Equation (Section 3.2)

The simplest case: Brownian motion and the heat equation.

- [Heat Equation Overview](../heat_equation/heat_equation_overview.md)
- [Fundamental Solution](../heat_equation/fundamental_solution.md)
- [Scaling and Invariance](../heat_equation/scaling_and_invariance.md)
- [Maximum Principle](../heat_equation/maximum_principle.md)
- [Heat Equation and Brownian Motion](../heat_equation/heat_equation_and_brownian_motion.md)

### Kolmogorov Equations (Section 3.3)

The general theory for diffusion processes.

- [Kolmogorov Forward (Fokker–Planck)](../kolmogorov_equations/kolmogorov_forward.md)
- [Kolmogorov Backward](../kolmogorov_equations/kolmogorov_backward.md)
- [Forward–Backward Duality](../kolmogorov_equations/forward_backward_duality.md)

### Feynman–Kac Formula (Section 3.4)

Discounting, killing, and the connection to finance.

- [Feynman–Kac Formula](../feynman_kac/feynman_kac_formula.md)
- [Running Payoff Extension](../feynman_kac/feynman_kac_running_payoff.md)
- [Applications](../feynman_kac/feynman_kac_applications.md)

### Pricing PDEs (Section 3.5)

Applications to derivative pricing.

- [Discounting and Killing](../bs_pde_structure/discounting_and_killing_term.md)
- [Greeks from PDE](../bs_pde_structure/greeks_from_pde.md)
- [Boundary Conditions](../bs_pde_structure/terminal_and_boundary_conditions.md)

---

## Key Formulas at a Glance

| Object | Formula |
|--------|---------|
| **Generator** | $\mathcal{L} = \mu(x)\partial_x + \frac{\sigma^2(x)}{2}\partial_{xx}$ |
| **Adjoint** | $\mathcal{L}^* f = -\partial_x[\mu f] + \frac{1}{2}\partial_{xx}[\sigma^2 f]$ |
| **Backward PDE** | $\partial_t u = \mathcal{L} u$ |
| **Forward PDE** | $\partial_t p = \mathcal{L}^* p$ |
| **Feynman–Kac** | $\partial_t u + \mathcal{L} u - ru = 0$ |
| **Probabilistic solution** | $u(t,x) = \mathbb{E}_x[e^{-\int r \, ds} g(X_T)]$ |

---

## Historical Perspective

The SDE–PDE connection has deep historical roots:

- **1900s**: Bachelier's thesis on option pricing (before Black–Scholes!)
- **1905**: Einstein's theory of Brownian motion
- **1931**: Kolmogorov's rigorous foundation of diffusion theory
- **1947**: Feynman's path integral formulation of quantum mechanics
- **1948**: Kac's rigorous proof connecting path integrals to PDEs
- **1973**: Black–Scholes formula, applying Feynman–Kac to finance
- **2020s**: Diffusion models in generative AI, using the forward/backward connection

The mathematics developed for physics became the foundation of quantitative finance, and now powers modern machine learning.

---

## See Also

- [Infinitesimal Generator](../../ch02/infinitesimal_generator/infinitesimal_generator.md) — the operator that starts it all
- [Dynkin's Formula](../../ch02/infinitesimal_generator/dynkin_formula.md) — integral form of the backward equation
- [Generator and Martingales](../../ch02/infinitesimal_generator/generator_and_martingales.md) — martingale characterization
- [Invariant Measures](../../ch02/diffusion_process/invariant_measures_and_stationarity.md) — long-time behavior from Fokker–Planck
