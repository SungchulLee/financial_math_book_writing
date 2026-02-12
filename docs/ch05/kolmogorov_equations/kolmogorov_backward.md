# Kolmogorov Backward Equation

The **Kolmogorov backward equation** describes how expected values of functions of a diffusion process depend on the initial condition. It is the PDE satisfied by $u(t,x) = \mathbb{E}_x[g(X_t)]$, with the generator acting on the **initial point**.

!!! tip "Related Content"
    - [Kolmogorov Forward Equation](kolmogorov_forward.md) — the dual equation for densities
    - [Forward–Backward Duality](forward_backward_duality.md) — the adjoint relationship
    - [Feynman–Kac Formula](../feynman_kac/feynman_kac_formula.md) — extension with discounting
    - [Infinitesimal Generator](../../ch02/infinitesimal_generator/infinitesimal_generator.md) — defines $\mathcal{L}$

---

## Setting

### Time-Homogeneous Case

Consider the diffusion:

$$dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$$

with generator:

$$\mathcal{L} = \mu(x)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2}{\partial x^2}$$

### Time-Inhomogeneous Case

For time-dependent coefficients:

$$dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t$$

the generator becomes time-dependent:

$$\mathcal{L}_t = \mu(x,t)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x,t)\frac{\partial^2}{\partial x^2}$$

---

## The Two Forms of the Backward Equation

The backward equation appears in two equivalent forms depending on the time convention. Understanding both is essential because different fields prefer different formulations.

### Form 1: Initial Value Problem (Forward in Time)

**Question**: Given initial condition $g$, how does $\mathbb{E}_x[g(X_t)]$ evolve as $t$ increases?

$$\boxed{\frac{\partial u}{\partial t} = \mathcal{L} u, \quad u(0, x) = g(x)}$$

Here $u(t, x) = \mathbb{E}[g(X_t) \mid X_0 = x]$.

**Time runs forward**: $t = 0 \to t = T$.

**Interpretation**: Start with a "snapshot" $g$ of some quantity at $t=0$. As time progresses, the expectation of this quantity (evaluated at where the process ends up) evolves according to $\mathcal{L}$.

### Form 2: Terminal Value Problem (Backward in Time)

**Question**: Given terminal payoff $g$ at time $T$, what is the expected value at earlier time $t$?

$$\boxed{\frac{\partial v}{\partial t} + \mathcal{L} v = 0, \quad v(T, x) = g(x)}$$

Here $v(t, x) = \mathbb{E}[g(X_T) \mid X_t = x]$.

**Time runs backward**: $t = T \to t = 0$.

**Interpretation**: We know the payoff at maturity $T$ and want to find its present value at earlier times.

### Relationship Between the Forms

| Aspect | Form 1 (IVP) | Form 2 (TVP) |
|--------|--------------|--------------|
| PDE | $\partial_t u = \mathcal{L}u$ | $\partial_t v + \mathcal{L}v = 0$ |
| Condition | $u(0,x) = g(x)$ | $v(T,x) = g(x)$ |
| Interpretation | Evolve from initial data | Propagate from terminal data |
| Time direction | Forward | Backward |

**They are the same equation**: If $u$ solves Form 1, then $v(t,x) = u(T-t, x)$ solves Form 2.

!!! info "Which Form to Use?"
    - **Form 1**: Natural for transition densities, heat equation perspective, physics
    - **Form 2**: Natural for finance (option pricing), optimal control, dynamic programming
    
    Finance typically uses Form 2 because we know the terminal payoff and want present value.

!!! note "The Sign Convention Mystery"
    The sign difference ($\partial_t u = \mathcal{L}u$ vs $\partial_t v + \mathcal{L}v = 0$) often confuses newcomers. The key insight:
    
    - In Form 1, increasing $t$ means *more time for evolution* → expectation changes
    - In Form 2, increasing $t$ means *less time until maturity* → opposite effect
    
    The time-reversal $v(t,x) = u(T-t, x)$ relates them: $\partial_t v = -\partial_t u |_{T-t}$.

---

## Transition Density Form

Let $p(t; x, y)$ be the transition density:

$$\mathbb{P}(X_t \in dy \mid X_0 = x) = p(t; x, y)\,dy$$

!!! note "Notation"
    We write $p(t; x, y)$ with semicolon to emphasize:
    
    - $(t, x)$: **backward variables** (time elapsed, starting point)
    - $y$: **terminal state** (where the process ends up)

**Backward equation** (acting on initial point $x$):

$$\boxed{\frac{\partial p}{\partial t}(t; x, y) = \mathcal{L}_x p(t; x, y)}$$

where $\mathcal{L}_x$ differentiates with respect to $x$:

$$\mathcal{L}_x p = \mu(x)\frac{\partial p}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2 p}{\partial x^2}$$

**Initial condition**: $p(0; x, y) = \delta(x - y)$.

This is a remarkable fact: the transition density satisfies *two different PDEs*:

| Equation | Variables | Operator |
|----------|-----------|----------|
| Backward | $(t, x)$ with $y$ fixed | $\mathcal{L}_x$ |
| Forward | $(t, y)$ with $x$ fixed | $\mathcal{L}_y^*$ |

---

## Expected Value Form

For any (nice) function $g$:

$$u(t, x) = \mathbb{E}[g(X_t) \mid X_0 = x] = \int g(y)\, p(t; x, y)\,dy$$

**Theorem**: $u$ satisfies the backward equation:

$$\boxed{\frac{\partial u}{\partial t} = \mathcal{L} u, \quad u(0, x) = g(x)}$$

This is the most common form encountered in applications.

---

## Derivation

### Method 1: From the Generator Definition

By definition of the infinitesimal generator:

$$(\mathcal{L}g)(x) = \lim_{t \downarrow 0} \frac{\mathbb{E}_x[g(X_t)] - g(x)}{t} = \lim_{t \downarrow 0} \frac{u(t,x) - u(0,x)}{t} = \frac{\partial u}{\partial t}(0, x)$$

This shows $\partial_t u = \mathcal{L}u$ at $t = 0$.

By the **Markov property**, the same argument applies at any time $t$:

$$
\frac{\partial u}{\partial t}(t, x) = \lim_{h \downarrow 0} \frac{u(t+h, x) - u(t, x)}{h} = \lim_{h \downarrow 0} \frac{\mathbb{E}_x[\mathbb{E}_{X_t}[g(X_h)]] - \mathbb{E}_x[g(X_t)]}{h}
$$

$$
= \mathbb{E}_x\left[\lim_{h \downarrow 0} \frac{\mathbb{E}_{X_t}[g(X_h)] - g(X_t)}{h}\right] = \mathbb{E}_x[(\mathcal{L}g)(X_t)]
$$

For the function $u(t, \cdot)$, this gives $\frac{\partial u}{\partial t}(t, x) = (\mathcal{L}_x u)(t, x)$.

### Method 2: Verification via Itô's Lemma

!!! warning "This is Verification, Not Derivation"
    This method assumes $u$ solves the PDE and verifies consistency. It does not derive the PDE from first principles.

Suppose $u$ solves $\partial_t u = \mathcal{L}u$. Define $v(t,x) = u(T-t, x)$, so $\partial_t v + \mathcal{L}v = 0$.

Apply Itô's lemma to $v(t, X_t)$:

$$dv(t, X_t) = \left(\frac{\partial v}{\partial t} + \mathcal{L}v\right)dt + \frac{\partial v}{\partial x}\sigma(X_t)\,dW_t = 0 \cdot dt + \frac{\partial v}{\partial x}\sigma(X_t)\,dW_t$$

So $v(t, X_t)$ is a **local martingale**.

Under integrability conditions, taking expectations:

$$v(0, x) = \mathbb{E}_x[v(T, X_T)] = \mathbb{E}_x[u(0, X_T)] = \mathbb{E}_x[g(X_T)]$$

This confirms $v(0,x) = u(T, x) = \mathbb{E}_x[g(X_T)]$. ✓

!!! note "The Martingale Insight"
    The verification reveals a deep connection: **$v(t, X_t)$ is a martingale precisely because $v$ solves the PDE**. This is the essence of the Feynman–Kac formula and explains why PDEs arise naturally in stochastic analysis.

### Method 3: Chapman–Kolmogorov Approach

??? abstract "Derivation via Chapman–Kolmogorov"
    The transition density satisfies the Chapman–Kolmogorov equation:
    
    $$p(t+h; x, y) = \int p(h; x, z) p(t; z, y) \, dz$$
    
    Differentiating with respect to $t$ at $t=0$:
    
    $$\frac{\partial p}{\partial t}(h; x, y)\Big|_{h=0^+} = \lim_{h \downarrow 0} \frac{p(h; x, y) - \delta(x-y)}{h}$$
    
    Using the local expansion of the transition density (moment conditions):
    
    - $\int (z-x) p(h; x, z) dz = \mu(x) h + o(h)$
    - $\int (z-x)^2 p(h; x, z) dz = \sigma^2(x) h + o(h)$
    
    A Taylor expansion argument yields the backward equation.

---

## Connection to Forward Equation (Fokker–Planck)

The backward and forward equations are **adjoints** of each other.

| Equation | Acts on | Variable | PDE |
|----------|---------|----------|-----|
| Backward | Initial point | $x$ | $\partial_t p = \mathcal{L}_x p$ |
| Forward | Terminal point | $y$ | $\partial_t p = \mathcal{L}_y^* p$ |

where the **adjoint generator** is:

$$\mathcal{L}^* p = -\frac{\partial}{\partial y}[\mu(y) p] + \frac{1}{2}\frac{\partial^2}{\partial y^2}[\sigma^2(y) p]$$

**Duality**: For test functions $f, g$:

$$\int f(x) (\mathcal{L}g)(x)\,dx = \int (\mathcal{L}^* f)(x) g(x)\,dx$$

(plus boundary terms)

!!! info "Physical Interpretation"
    - **Backward**: "From which starting points do we reach a given target?" (Value function perspective)
    - **Forward**: "Where does the probability mass flow over time?" (Distribution perspective)

See [Forward–Backward Duality](forward_backward_duality.md) for the detailed adjoint relationship.

---

## Examples

### Example 1: Brownian Motion

**SDE**: $dX_t = dW_t$ (so $\mu = 0$, $\sigma = 1$)

**Backward equation**:

$$\frac{\partial u}{\partial t} = \frac{1}{2}\frac{\partial^2 u}{\partial x^2}$$

This is the **heat equation**.

**Solution** with $u(0,x) = g(x)$:

$$u(t, x) = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi t}} e^{-(y-x)^2/2t} g(y)\,dy$$

The kernel $\frac{1}{\sqrt{2\pi t}} e^{-(y-x)^2/2t}$ is the **heat kernel** = transition density of Brownian motion.

**Explicit example**: For $g(x) = x^2$:

$$u(t, x) = \mathbb{E}_x[X_t^2] = \mathbb{E}_x[(x + W_t)^2] = x^2 + t$$

Verification: $\partial_t u = 1$, $\partial_{xx} u = 2$, so $\partial_t u = \frac{1}{2}\partial_{xx} u$. ✓

---

### Example 2: Brownian Motion with Drift

**SDE**: $dX_t = \mu\,dt + \sigma\,dW_t$

**Backward equation**:

$$\frac{\partial u}{\partial t} = \mu\frac{\partial u}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2}$$

This is the **advection-diffusion equation**.

**Solution** with $u(0,x) = g(x)$:

$$u(t, x) = \int_{-\infty}^{\infty} \frac{1}{\sigma\sqrt{2\pi t}} \exp\left(-\frac{(y - x - \mu t)^2}{2\sigma^2 t}\right) g(y)\,dy$$

---

### Example 3: Ornstein–Uhlenbeck

**SDE**: $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$

**Backward equation**:

$$\frac{\partial u}{\partial t} = -\kappa x\frac{\partial u}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2}$$

**Explicit example**: For $g(x) = x$ (expected position):

$$u(t, x) = \mathbb{E}_x[X_t] = x e^{-\kappa t}$$

Verification: $\partial_t u = -\kappa x e^{-\kappa t}$, $\partial_x u = e^{-\kappa t}$, $\partial_{xx} u = 0$

$-\kappa x \cdot e^{-\kappa t} + 0 = -\kappa x e^{-\kappa t}$. ✓

---

### Example 4: Geometric Brownian Motion

**SDE**: $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$

**Generator**: $\mathcal{L} = \mu s\frac{\partial}{\partial s} + \frac{\sigma^2 s^2}{2}\frac{\partial^2}{\partial s^2}$

**Backward equation**:

$$\frac{\partial u}{\partial t} = \mu s\frac{\partial u}{\partial s} + \frac{\sigma^2 s^2}{2}\frac{\partial^2 u}{\partial s^2}$$

### Connection to Black–Scholes

Under the **risk-neutral measure** ($\mu \to r$), the terminal value form with discounting:

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} = rV$$

is the **Black–Scholes PDE**.

This follows from Feynman–Kac: the discounted price $e^{-r(T-t)}V(t,S)$ should be a martingale.

---

## Connection to Feynman–Kac

The backward equation is a **special case** of the Feynman–Kac formula with zero potential.

| Problem | PDE | Probabilistic Solution |
|---------|-----|----------------------|
| Backward equation | $\partial_t u = \mathcal{L}u$ | $u(t,x) = \mathbb{E}_x[g(X_t)]$ |
| Feynman–Kac | $\partial_t u = \mathcal{L}u - V(x)u$ | $u(t,x) = \mathbb{E}_x\left[e^{-\int_0^t V(X_s)ds} g(X_t)\right]$ |

The potential $V(x)$ introduces **discounting** or **killing**:

- **Finance**: $V = r$ (constant risk-free rate) gives discounted expectations
- **Physics**: $V(x)$ represents a potential field that "kills" particles
- **Probability**: $V(x)$ is the rate of an independent exponential killing time

See [Feynman–Kac Formula](../feynman_kac/feynman_kac_formula.md).

---

## Connection to Dynkin's Formula

Dynkin's formula is the **integrated form** of the backward equation.

**Backward equation** (differential):
$$\frac{\partial}{\partial t}\mathbb{E}_x[g(X_t)] = \mathcal{L}_x \mathbb{E}_x[g(X_t)]$$

**Dynkin's formula** (integral):
$$\mathbb{E}_x[g(X_t)] = g(x) + \mathbb{E}_x\left[\int_0^t (\mathcal{L}g)(X_s)\,ds\right]$$

Differentiating Dynkin at $t = 0$:
$$\frac{\partial}{\partial t}\mathbb{E}_x[g(X_t)]\Big|_{t=0} = (\mathcal{L}g)(x)$$

recovers the backward equation at $t = 0$.

!!! info "Dynkin = E[Itô]"
    Dynkin's formula is simply Itô's formula with the martingale part averaged out:
    
    $$g(X_t) = g(X_0) + \int_0^t (\mathcal{L}g)(X_s)\,ds + \int_0^t g'(X_s)\sigma(X_s)\,dW_s$$
    
    Taking expectations eliminates the stochastic integral (which is a martingale).

---

## Boundary Conditions

For diffusions on **bounded domains** $D$, boundary conditions are needed.

| Type | Condition | Interpretation | Example |
|------|-----------|----------------|---------|
| **Dirichlet** | $u = g$ on $\partial D$ | Absorbing boundary (process killed) | Barrier options |
| **Neumann** | $\frac{\partial u}{\partial n} = 0$ on $\partial D$ | Reflecting boundary | Particles in a box |
| **Robin** | $\alpha u + \beta \frac{\partial u}{\partial n} = g$ | Partial absorption/reflection | Sticky boundaries |

The choice depends on the physical/financial problem.

### First Passage Problems

For the first exit time $\tau = \inf\{t \geq 0 : X_t \notin D\}$:

$$u(x) = \mathbb{E}_x[g(X_\tau)]$$

solves the **Dirichlet problem**:

$$\mathcal{L}u = 0 \text{ in } D, \quad u = g \text{ on } \partial D$$

This connects to harmonic functions and potential theory.

---

## Well-Posedness

!!! note "Scope"
    Full PDE theory is beyond this document. We state key facts.

Under standard conditions (Lipschitz $\mu$, $\sigma$; bounded or with growth control):

| Property | Condition |
|----------|-----------|
| **Existence** | Smooth $g$ → classical solution |
| **Uniqueness** | In appropriate function spaces (e.g., bounded, polynomial growth) |
| **Regularity** | Solution inherits smoothness from coefficients and data |

### Maximum Principle

If $u$ solves the backward equation on $[0,T] \times D$:

$$\max_{[0,T] \times \bar{D}} u = \max\left(\max_{\bar{D}} u(0, \cdot), \max_{[0,T] \times \partial D} u\right)$$

The maximum is attained either at the initial time or on the boundary—never in the interior.

### Viscosity Solutions

For irregular data or degenerate diffusions (where $\sigma$ can vanish), **viscosity solutions** provide the right framework:

- Weaker notion that doesn't require differentiability
- Comparison principle ensures uniqueness
- Connects to optimal control (Hamilton–Jacobi–Bellman equations)

---

## Numerical Methods

### Finite Differences (Explicit Scheme)

For Form 1 ($\partial_t u = \mathcal{L}u$), discretize on grid $(x_i, t_n)$:

$$\frac{u_i^{n+1} - u_i^n}{\Delta t} = \mu(x_i)\frac{u_{i+1}^n - u_{i-1}^n}{2\Delta x} + \frac{\sigma^2(x_i)}{2}\frac{u_{i+1}^n - 2u_i^n + u_{i-1}^n}{\Delta x^2}$$

**Stability** (CFL condition): $\Delta t \leq \frac{\Delta x^2}{\sigma^2}$

### Finite Differences (Terminal Value Problem)

For Form 2 ($\partial_t v + \mathcal{L}v = 0$), march **backward** from $v(T, \cdot) = g$:

$$v_i^{n} = v_i^{n+1} + \Delta t \cdot (\mathcal{L}v)_i^{n+1}$$

This is the standard approach for option pricing.

### Monte Carlo

The probabilistic representation provides a natural Monte Carlo method:

$$u(t, x) = \mathbb{E}_x[g(X_t)] \approx \frac{1}{N}\sum_{j=1}^N g(X_t^{(j)})$$

where $X_t^{(j)}$ are simulated paths starting from $x$.

**Advantages**: Works in high dimensions, handles complex payoffs

**Disadvantages**: Slow convergence ($O(1/\sqrt{N})$), gives answer at one point only

---

## Summary

| Form | PDE | Condition | Solution |
|------|-----|-----------|----------|
| IVP | $\partial_t u = \mathcal{L}u$ | $u(0,x) = g(x)$ | $u(t,x) = \mathbb{E}_x[g(X_t)]$ |
| TVP | $\partial_t v + \mathcal{L}v = 0$ | $v(T,x) = g(x)$ | $v(t,x) = \mathbb{E}[g(X_T) \mid X_t = x]$ |

$$\boxed{\frac{\partial u}{\partial t} = \mathcal{L}_x u = \mu(x)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2 u}{\partial x^2}}$$

**The Kolmogorov backward equation is the PDE for expected values, with the generator acting on the initial condition.**

| Aspect | Description |
|--------|-------------|
| **Input** | Initial position $x$, test function $g$ |
| **Output** | Expected value $\mathbb{E}_x[g(X_t)]$ |
| **Operator** | Generator $\mathcal{L}$ (not adjoint) |
| **Key insight** | Expectations satisfy deterministic PDEs |
| **Applications** | Option pricing, optimal stopping, filtering |

---

## See Also

- [Kolmogorov Forward Equation](kolmogorov_forward.md) — the dual equation for densities
- [Forward–Backward Duality](forward_backward_duality.md) — the adjoint relationship
- [Infinitesimal Generator](../../ch02/infinitesimal_generator/infinitesimal_generator.md) — defines $\mathcal{L}$
- [Dynkin's Formula](../../ch02/infinitesimal_generator/dynkin_formula.md) — integral form
- [Feynman–Kac Formula](../feynman_kac/feynman_kac_formula.md) — extension with potential/discounting
- [Heat Equation](../heat_equation/heat_equation_overview.md) — backward equation for Brownian motion
