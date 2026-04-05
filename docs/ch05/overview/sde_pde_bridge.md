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

### Why Does the Generator Lead to the Backward Equation?

The arrow labeled "Markov property extends to finite time" deserves explanation — it is the logical core of the entire hierarchy.

**Setup.** Define:

$$u(x_0, t_0) = \mathbb{E}[g(X_t) \mid X_{t_0} = x_0]$$

This is a function of the starting point $(x_0, t_0)$. We want to find what PDE it satisfies.

**The generator is purely infinitesimal.** By definition, $\mathcal{L}_{x_0}$ captures only what happens as $h \to 0$, with the time argument frozen:

$$(\mathcal{L}_{x_0} f)(x_0) = \lim_{h \downarrow 0} \frac{\mathbb{E}_{x_0}[f(X_{t_0+h})] - f(x_0)}{h}$$

This is a *local* rule — it tells you the instantaneous rate of change in the spatial variable $x_0$, but says nothing directly about finite time horizons.

**Step 1: Apply the Markov property (tower property).**

Take a small step $h > 0$ forward from $t_0$. By the Markov property, once you know where the process is at $t_0 + h$, the earlier history is irrelevant:

$$u(x_0, t_0) = \mathbb{E}\!\left[\mathbb{E}[g(X_t) \mid X_{t_0+h}] \;\Big|\; X_{t_0} = x_0\right] = \mathbb{E}_{x_0}\!\left[u(X_{t_0+h},\, t_0+h)\right]$$

**Step 2: Rewrite as a difference and take $h \to 0$.**

Since $u(x_0, t_0) = \mathbb{E}_{x_0}[u(X_{t_0+h}, t_0+h)]$, we can write:

$$\frac{\partial u}{\partial t_0} = \lim_{h \to 0} \frac{\mathbb{E}_{x_0}[u(X_{t_0+h},\, t_0+h)] - u(x_0, t_0)}{h}$$

**Step 3: Split the increment into spatial and temporal parts.**

Add and subtract $\mathbb{E}_{x_0}[u(X_{t_0+h}, t_0)]$ to separate the two effects:

$$\frac{\partial u}{\partial t_0} = \lim_{h \to 0} \frac{\mathbb{E}_{x_0}[u(X_{t_0+h},\, t_0)] - u(x_0, t_0)}{h} + \lim_{h \to 0} \frac{\mathbb{E}_{x_0}[u(X_{t_0+h},\, t_0+h) - u(X_{t_0+h},\, t_0)]}{h}$$

The **first term** is exactly the generator applied to $u(\cdot, t_0)$ as a function of $x_0$:

$$\lim_{h \to 0} \frac{\mathbb{E}_{x_0}[u(X_{t_0+h},\, t_0)] - u(x_0, t_0)}{h} = \mathcal{L}_{x_0}\, u(x_0, t_0)$$

The **second term**: expanding $u(X_{t_0+h}, t_0+h) - u(X_{t_0+h}, t_0) = \partial_{t_0} u \cdot h + O(h^2)$, so after dividing by $h$ and taking the limit this contributes $\mathbb{E}_{x_0}[\partial_{t_0} u(X_{t_0+h}, t_0)] \to \partial_{t_0} u(x_0, t_0)$.

!!! note "Why the second term cannot be ignored"
    The difference $u(X_{t_0+h}, t_0+h) - u(X_{t_0+h}, t_0)$ is $O(h)$ — it is of leading order in $h$ and does **not** vanish in the limit. This is why you cannot simply substitute $u(X_{t_0+h}, t_0)$ for $u(X_{t_0+h}, t_0+h)$ and read off the generator directly. The two-step split is necessary.

Combining both terms and rearranging:

$$\frac{\partial u}{\partial t_0} - \partial_{t_0} u(x_0, t_0) = \mathcal{L}_{x_0}\, u(x_0, t_0)$$

which gives the backward equation with the correct sign convention (since $t_0$ runs backward toward the terminal condition at $t$):

$$\boxed{-\partial_{t_0} u = \mathcal{L}_{x_0} u, \qquad u(x_0, t) = g(x_0)}$$

!!! note "Why Markov is essential"
    Without the Markov property, $\mathbb{E}[g(X_t) \mid X_{t_0+h}]$ would depend on the full history before $t_0 + h$, not just the current state $X_{t_0+h}$. The tower step in Step 1 would collapse, and you could not reduce a finite-time expectation to a single application of $\mathcal{L}_{x_0}$.

**In summary:**

| Step | Role |
|------|------|
| Generator $\mathcal{L}_{x_0}$ | Encodes local dynamics in the spatial variable $x_0$ at each instant |
| Markov property | Enables tower property: $u(x_0,t_0) = \mathbb{E}_{x_0}[u(X_{t_0+h}, t_0+h)]$ |
| Two-step split | Separates spatial increment (→ generator) from temporal increment (→ $\partial_{t_0} u$) |
| Result | $-\partial_{t_0} u = \mathcal{L}_{x_0} u$ holds for all $t_0 < t$ |

---

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

- [Discounting and Killing](../../ch06/bs_pde_structure/discounting_and_killing_term.md)
- [Greeks from PDE](../../ch06/bs_pde_structure/greeks_from_pde.md)
- [Boundary Conditions](../../ch06/bs_pde_structure/terminal_and_boundary_conditions.md)

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

- [Infinitesimal Generator](../../ch03/infinitesimal_generator/infinitesimal_generator.md) — the operator that starts it all
- [Dynkin's Formula](../../ch03/infinitesimal_generator/dynkin_formula.md) — integral form of the backward equation
- [Generator and Martingales](../../ch03/infinitesimal_generator/generator_and_martingales.md) — martingale characterization
- [Invariant Measures](../../ch03/diffusion_process/invariant_measures_and_stationarity.md) — long-time behavior from Fokker–Planck

---

## Exercises

**Exercise 1.** Consider the Ornstein-Uhlenbeck process $dX_t = -\theta X_t\,dt + \sigma\,dW_t$ with $\theta > 0$. Write down the infinitesimal generator $\mathcal{L}$ and verify that the function $u(t, x) = x\,e^{-\theta t}$ satisfies $\partial_t u = \mathcal{L} u$ (the Kolmogorov backward equation with terminal condition $u(0,x) = x$).

??? success "Solution to Exercise 1"
    The Ornstein-Uhlenbeck process $dX_t = -\theta X_t\,dt + \sigma\,dW_t$ has drift $\mu(x) = -\theta x$ and diffusion coefficient $\sigma(x) = \sigma$. The infinitesimal generator is:

    $$
    \mathcal{L} = -\theta x\frac{\partial}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2}{\partial x^2}
    $$

    Now verify that $u(t, x) = xe^{-\theta t}$ satisfies $\partial_t u = \mathcal{L} u$.

    **Left-hand side**:

    $$
    \frac{\partial u}{\partial t} = -\theta x e^{-\theta t}
    $$

    **Right-hand side**: Compute each term of $\mathcal{L} u$:

    $$
    \frac{\partial u}{\partial x} = e^{-\theta t}, \qquad \frac{\partial^2 u}{\partial x^2} = 0
    $$

    Therefore:

    $$
    \mathcal{L} u = -\theta x \cdot e^{-\theta t} + \frac{\sigma^2}{2} \cdot 0 = -\theta x e^{-\theta t}
    $$

    Since $\partial_t u = -\theta x e^{-\theta t} = \mathcal{L} u$, the function $u(t,x) = xe^{-\theta t}$ satisfies the Kolmogorov backward equation. This is consistent with the probabilistic interpretation: $\mathbb{E}[X_t \mid X_0 = x] = xe^{-\theta t}$ for the OU process, which is the conditional mean decaying exponentially toward zero.

---

**Exercise 2.** For a general one-dimensional diffusion $dX_t = \mu(x)\,dt + \sigma(x)\,dW_t$, the adjoint operator $\mathcal{L}^*$ acting on a density $p$ is

$$
\mathcal{L}^* p = -\frac{\partial}{\partial x}[\mu(x)\,p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x)\,p]
$$

Verify the duality relation $\int f(x)\,(\mathcal{L}g)(x)\,dx = \int (\mathcal{L}^* f)(x)\,g(x)\,dx$ by integration by parts, assuming $f$ and $g$ vanish at $\pm\infty$.

??? success "Solution to Exercise 2"
    We need to verify $\int f\,(\mathcal{L}g)\,dx = \int (\mathcal{L}^* f)\,g\,dx$ where:

    $$
    \mathcal{L}g = \mu g' + \frac{1}{2}\sigma^2 g'', \qquad \mathcal{L}^* f = -(\mu f)' + \frac{1}{2}(\sigma^2 f)''
    $$

    Consider the left-hand side, integrating term by term.

    **First term** (drift):

    $$
    \int_{-\infty}^{\infty} f(x)\,\mu(x)\,g'(x)\,dx
    $$

    Integrate by parts (boundary terms vanish since $f, g \to 0$ at $\pm\infty$):

    $$
    = -\int_{-\infty}^{\infty} \frac{\partial}{\partial x}[\mu(x)\,f(x)]\,g(x)\,dx = -\int_{-\infty}^{\infty} (\mu f)'(x)\,g(x)\,dx
    $$

    **Second term** (diffusion):

    $$
    \int_{-\infty}^{\infty} f(x)\,\frac{1}{2}\sigma^2(x)\,g''(x)\,dx
    $$

    Integrate by parts once:

    $$
    = -\int_{-\infty}^{\infty} \frac{\partial}{\partial x}\!\left[\frac{1}{2}\sigma^2(x)\,f(x)\right] g'(x)\,dx
    $$

    Integrate by parts again:

    $$
    = \int_{-\infty}^{\infty} \frac{\partial^2}{\partial x^2}\!\left[\frac{1}{2}\sigma^2(x)\,f(x)\right] g(x)\,dx
    $$

    Combining both terms:

    $$
    \int f\,(\mathcal{L}g)\,dx = \int \left\{-(\mu f)' + \frac{1}{2}(\sigma^2 f)''\right\} g\,dx = \int (\mathcal{L}^* f)\,g\,dx
    $$

    This confirms the duality relation. $\square$

---

**Exercise 3.** For Brownian motion ($\mu = 0$, $\sigma = 1$), the transition density is $p(x, t \mid x_0, 0) = \frac{1}{\sqrt{2\pi t}} e^{-(x - x_0)^2/(2t)}$. Verify directly that this density satisfies both the forward equation $\partial_t p = \frac{1}{2}\partial_{xx} p$ in $(x, t)$ and the backward equation $\partial_t p + \frac{1}{2}\partial_{x_0 x_0} p = 0$ in $(x_0, t)$ (with $t$ treated as the same variable in both cases).

??? success "Solution to Exercise 3"
    The Brownian motion transition density is $p(x, t \mid x_0, 0) = \frac{1}{\sqrt{2\pi t}}\exp\!\left(-\frac{(x-x_0)^2}{2t}\right)$.

    **Forward equation**: $\partial_t p = \frac{1}{2}\partial_{xx} p$ with derivatives taken in $(x, t)$, holding $x_0$ fixed.

    Compute $\partial_t p$. Let $\phi = -\frac{(x-x_0)^2}{2t}$, so $p = (2\pi t)^{-1/2}e^\phi$.

    $$
    \partial_t p = p\left(-\frac{1}{2t} + \frac{(x-x_0)^2}{2t^2}\right)
    $$

    Compute $\partial_{xx} p$:

    $$
    \partial_x p = p\cdot\frac{-(x-x_0)}{t}
    $$

    $$
    \partial_{xx} p = p\left(\frac{(x-x_0)^2}{t^2} - \frac{1}{t}\right)
    $$

    Therefore $\frac{1}{2}\partial_{xx}p = p\left(\frac{(x-x_0)^2}{2t^2} - \frac{1}{2t}\right) = \partial_t p$. The forward equation is verified.

    **Backward equation**: $\partial_t p + \frac{1}{2}\partial_{x_0 x_0} p = 0$ with derivatives in $(x_0, t)$, holding $x$ fixed. (Note: here $t$ plays the role of the time variable in both equations.)

    $$
    \partial_{x_0} p = p\cdot\frac{(x - x_0)}{t}, \qquad \partial_{x_0 x_0} p = p\left(\frac{(x-x_0)^2}{t^2} - \frac{1}{t}\right)
    $$

    Note that $\partial_{x_0 x_0}p = \partial_{xx}p$ since $(x - x_0)^2$ is symmetric and only the sign of the first derivative changes. Therefore:

    $$
    \partial_t p + \frac{1}{2}\partial_{x_0 x_0}p = p\left(-\frac{1}{2t} + \frac{(x-x_0)^2}{2t^2}\right) + \frac{1}{2}p\left(\frac{(x-x_0)^2}{t^2} - \frac{1}{t}\right)
    $$

    Wait -- this does not give zero. The issue is the sign convention. For Brownian motion with $\mu = 0$, the backward equation in the standard form is $\partial_t p = \frac{1}{2}\partial_{x_0 x_0}p$ (or equivalently $-\partial_{t_0}p = \frac{1}{2}\partial_{x_0 x_0}p$ when differentiating in the initial time $t_0$). Since $p$ depends on $t - t_0$ and we set $t_0 = 0$, we have $\partial_{t_0}p = -\partial_t p$. The backward equation in $(x_0, t_0)$ becomes:

    $$
    -\partial_t p = -\frac{1}{2}\partial_{x_0 x_0}p \quad \Longleftrightarrow \quad \partial_t p = \frac{1}{2}\partial_{x_0 x_0}p
    $$

    Since $\partial_{x_0 x_0}p = \partial_{xx}p$ (by the symmetry $(x - x_0)^2$), this is the same computation as the forward equation, and it holds. $\square$

---

**Exercise 4.** Let $X_t$ follow geometric Brownian motion $dX_t = rX_t\,dt + \sigma X_t\,dW_t$. Define the value function $u(t, x) = \mathbb{E}[e^{-r(T-t)} g(X_T) \mid X_t = x]$ for a European payoff $g$. Show that $u$ satisfies the Black-Scholes PDE

$$
\frac{\partial u}{\partial t} + rx\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2 x^2 \frac{\partial^2 u}{\partial x^2} - ru = 0
$$

by identifying the generator, applying Feynman-Kac, and matching the discounting term.

??? success "Solution to Exercise 4"
    For geometric Brownian motion under the risk-neutral measure, $dX_t = rX_t\,dt + \sigma X_t\,dW_t$, the generator is:

    $$
    \mathcal{L} = rx\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2 x^2\frac{\partial^2}{\partial x^2}
    $$

    The value function is $u(t, x) = \mathbb{E}\!\left[e^{-r(T-t)}g(X_T) \mid X_t = x\right]$.

    By the **Feynman-Kac theorem**, the function $u(t, x) = \mathbb{E}_x\!\left[e^{-\int_t^T r\,ds}\,g(X_T)\right]$ satisfies:

    $$
    \frac{\partial u}{\partial t} + \mathcal{L}u - r\,u = 0, \qquad u(T, x) = g(x)
    $$

    Substituting the generator:

    $$
    \frac{\partial u}{\partial t} + rx\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2 x^2\frac{\partial^2 u}{\partial x^2} - ru = 0
    $$

    This is exactly the **Black-Scholes PDE** with terminal condition $u(T, x) = g(x)$.

    The key steps are:

    1. **Identify the generator**: From $dX_t = rX_t\,dt + \sigma X_t\,dW_t$, we read off $\mu(x) = rx$ and $\sigma(x) = \sigma x$, giving $\mathcal{L} = rx\partial_x + \frac{1}{2}\sigma^2 x^2\partial_{xx}$
    2. **Apply Feynman-Kac**: The discounted expectation $u = \mathbb{E}[e^{-r(T-t)}g(X_T)]$ satisfies $\partial_t u + \mathcal{L}u - ru = 0$
    3. **Match the discounting term**: The constant discount rate $r$ produces the $-ru$ term in the PDE, which converts the generator equation into the pricing PDE $\square$

---

**Exercise 5.** Consider the diffusion $dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t$ (the CIR process). Write down the generator $\mathcal{L}$ and the Kolmogorov forward equation for the transition density $p(x, t)$. Then find the stationary density $p_\infty(x)$ by solving $\mathcal{L}^* p_\infty = 0$ and identify it as a Gamma distribution.

??? success "Solution to Exercise 5"
    The CIR process $dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t$ has $\mu(x) = \kappa(\theta - x)$ and $\sigma(x) = \xi\sqrt{x}$.

    **Generator**:

    $$
    \mathcal{L} = \kappa(\theta - x)\frac{\partial}{\partial x} + \frac{\xi^2 x}{2}\frac{\partial^2}{\partial x^2}
    $$

    **Kolmogorov forward equation**: $\partial_t p = \mathcal{L}^* p$ where:

    $$
    \mathcal{L}^* p = -\frac{\partial}{\partial x}[\kappa(\theta - x)\,p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\xi^2 x\,p]
    $$

    **Stationary density**: Set $\mathcal{L}^* p_\infty = 0$:

    $$
    -\frac{d}{dx}[\kappa(\theta - x)\,p_\infty] + \frac{1}{2}\frac{d^2}{dx^2}[\xi^2 x\,p_\infty] = 0
    $$

    Integrate once:

    $$
    -\kappa(\theta - x)p_\infty + \frac{1}{2}\frac{d}{dx}[\xi^2 x\,p_\infty] = C_1
    $$

    With the boundary condition that $p_\infty \to 0$ as $x \to \infty$ and the flux vanishes, we set $C_1 = 0$:

    $$
    \frac{1}{2}\xi^2\frac{d}{dx}[x\,p_\infty] = \kappa(\theta - x)p_\infty
    $$

    Expand the left side: $\frac{1}{2}\xi^2(p_\infty + xp_\infty') = \kappa(\theta - x)p_\infty$. Rearranging:

    $$
    xp_\infty' = \left(\frac{2\kappa\theta}{\xi^2} - 1\right)p_\infty - \frac{2\kappa}{\xi^2}x\,p_\infty
    $$

    Let $\alpha = \frac{2\kappa\theta}{\xi^2}$ and $\beta = \frac{2\kappa}{\xi^2}$. Then:

    $$
    xp_\infty' = (\alpha - 1)p_\infty - \beta x\,p_\infty
    $$

    This ODE has the solution $p_\infty(x) = C\,x^{\alpha - 1}e^{-\beta x}$ for $x > 0$, which is the **Gamma distribution** $\text{Gamma}(\alpha, \beta)$ with shape $\alpha = \frac{2\kappa\theta}{\xi^2}$ and rate $\beta = \frac{2\kappa}{\xi^2}$.

    The normalizing constant is $C = \frac{\beta^\alpha}{\Gamma(\alpha)}$, giving:

    $$
    p_\infty(x) = \frac{\beta^\alpha}{\Gamma(\alpha)}\,x^{\alpha-1}\,e^{-\beta x}, \quad x > 0
    $$

    The Feller condition $2\kappa\theta > \xi^2$ (i.e., $\alpha > 1$) ensures that $p_\infty(0) = 0$, so the process stays strictly positive.

---

**Exercise 6.** The Feynman-Kac formula states that $u(t,x) = \mathbb{E}_x[e^{-\int_t^T r(X_s)\,ds}\,g(X_T)]$ solves $\partial_t u + \mathcal{L}u - r(x)u = 0$ with $u(T,x) = g(x)$. For the special case $r(x) = r$ (constant) and $dX_t = \mu\,dt + \sigma\,dW_t$ (arithmetic Brownian motion), verify that $u(t, x) = e^{-r(T-t)}\,\mathbb{E}_x[g(X_T)]$ satisfies the PDE by direct substitution, using the fact that $X_T \mid X_t = x$ is $N(x + \mu(T-t),\, \sigma^2(T-t))$.

??? success "Solution to Exercise 6"
    For constant $r$ and arithmetic Brownian motion $dX_t = \mu\,dt + \sigma\,dW_t$, we have $X_T \mid X_t = x \sim N(x + \mu(T-t),\, \sigma^2(T-t))$.

    The Feynman-Kac solution is:

    $$
    u(t, x) = e^{-r(T-t)}\,\mathbb{E}_x[g(X_T)] = e^{-r(T-t)} \int_{-\infty}^{\infty} g(y)\,\frac{1}{\sigma\sqrt{2\pi(T-t)}}\exp\!\left(-\frac{(y - x - \mu(T-t))^2}{2\sigma^2(T-t)}\right)dy
    $$

    Let $\tau = T - t$, so $u(t,x) = e^{-r\tau}\,F(x, \tau)$ where $F(x, \tau) = \mathbb{E}_x[g(X_T)]$.

    **Compute $\partial_t u$**: Since $\tau = T - t$, $\partial_t = -\partial_\tau$:

    $$
    \partial_t u = re^{-r\tau}F - e^{-r\tau}\partial_\tau F
    $$

    **Compute $\partial_x u$**: The dependence on $x$ enters only through the Gaussian mean $x + \mu\tau$:

    $$
    \partial_x F = \int g(y)\,\frac{y - x - \mu\tau}{\sigma^2\tau}\,\phi\,dy, \quad \partial_{xx}F = \int g(y)\left(\frac{(y-x-\mu\tau)^2}{\sigma^4\tau^2} - \frac{1}{\sigma^2\tau}\right)\phi\,dy
    $$

    where $\phi$ is the Gaussian density. These are standard results for Gaussian convolutions.

    Now $F$ satisfies the **backward (heat-type) equation** $\partial_\tau F = \mu\partial_x F + \frac{1}{2}\sigma^2\partial_{xx}F$ (the Kolmogorov backward equation for ABM). Therefore $\partial_\tau F = \mathcal{L}F$.

    Substituting into the PDE $\partial_t u + \mathcal{L}u - ru = 0$:

    $$
    \partial_t u + \mathcal{L}u - ru = (re^{-r\tau}F - e^{-r\tau}\partial_\tau F) + e^{-r\tau}\mathcal{L}F - re^{-r\tau}F
    $$

    $$
    = e^{-r\tau}(-\partial_\tau F + \mathcal{L}F) = 0
    $$

    since $\partial_\tau F = \mathcal{L}F$. The PDE is satisfied. At $t = T$ ($\tau = 0$), the Gaussian collapses to a point mass at $x$, giving $u(T, x) = g(x)$. $\square$

---

**Exercise 7.** The transition density $p(x, t \mid x_0, t_0)$ satisfies the backward equation in $(x_0, t_0)$ and the forward equation in $(x, t)$ simultaneously. Explain why these two PDEs do not contradict each other, despite involving different differential operators ($\mathcal{L}_{x_0}$ vs. $\mathcal{L}_x^*$). In your answer, clarify the role of which variables are held fixed and which are varied in each equation.

??? success "Solution to Exercise 7"
    The transition density $p(x, t \mid x_0, t_0)$ is a function of **four variables**: $(x, t, x_0, t_0)$. The two PDEs operate on different pairs of these variables:

    **Backward equation**: Fix the destination $(x, t)$ and differentiate in the origin $(x_0, t_0)$:

    $$
    \frac{\partial p}{\partial t_0} + \mathcal{L}_{x_0}\,p = 0
    $$

    Here $\mathcal{L}_{x_0} = \mu(x_0)\partial_{x_0} + \frac{1}{2}\sigma^2(x_0)\partial_{x_0 x_0}$ acts on $p$ as a function of $x_0$, with $(x, t)$ treated as fixed parameters. This equation asks: "How does the transition probability change as we vary the starting point?"

    **Forward equation**: Fix the origin $(x_0, t_0)$ and differentiate in the destination $(x, t)$:

    $$
    \frac{\partial p}{\partial t} = \mathcal{L}_x^*\,p
    $$

    Here $\mathcal{L}_x^* = -\partial_x[\mu(x)\,\cdot\,] + \frac{1}{2}\partial_{xx}[\sigma^2(x)\,\cdot\,]$ acts on $p$ as a function of $x$, with $(x_0, t_0)$ treated as fixed parameters. This equation asks: "How does the probability density spread over time?"

    **Why there is no contradiction**: The two equations involve **differentiation with respect to different variables**. The backward equation constrains $p$ as a function of $(x_0, t_0)$ for each fixed $(x, t)$, while the forward equation constrains $p$ as a function of $(x, t)$ for each fixed $(x_0, t_0)$. These are independent sets of constraints on the same function, and a sufficiently smooth function of four variables can satisfy both simultaneously.

    An analogy: a function $f(x, y) = e^{x+y}$ satisfies $\partial_x f = f$ (an equation in $x$) and $\partial_y f = f$ (an equation in $y$) simultaneously without contradiction, because the two equations operate on different variables.

    The operators $\mathcal{L}_{x_0}$ and $\mathcal{L}_x^*$ are different ($\mathcal{L}$ vs. its adjoint) precisely because they act on different arguments and encode different physical questions. The generator $\mathcal{L}_{x_0}$ describes how expected values depend on starting position; the adjoint $\mathcal{L}_x^*$ describes how probability mass flows through space. These are dual perspectives on the same Markov process, and duality is what guarantees that a single transition density can satisfy both equations.
