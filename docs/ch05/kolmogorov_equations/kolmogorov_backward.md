# Kolmogorov Backward Equation

The **Kolmogorov backward equation** describes how expected values of functions of a diffusion process depend on the initial condition. It is the PDE satisfied by $u(t,x) = \mathbb{E}_x[g(X_t)]$, with the generator acting on the **initial point**.

!!! tip "Related Content"
    - [Kolmogorov Forward Equation](kolmogorov_forward.md) — the dual equation for densities
    - [Forward–Backward Duality](forward_backward_duality.md) — the adjoint relationship
    - [Feynman–Kac Formula](../feynman_kac/feynman_kac_formula.md) — extension with discounting
    - [Infinitesimal Generator](../../ch03/infinitesimal_generator/infinitesimal_generator.md) — defines $\mathcal{L}$

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
- [Infinitesimal Generator](../../ch03/infinitesimal_generator/infinitesimal_generator.md) — defines $\mathcal{L}$
- [Dynkin's Formula](../../ch03/infinitesimal_generator/dynkin_formula.md) — integral form
- [Feynman–Kac Formula](../feynman_kac/feynman_kac_formula.md) — extension with potential/discounting
- [Heat Equation](../heat_equation/heat_equation_overview.md) — backward equation for Brownian motion

---

## Exercises

**Exercise 1.**
For the Ornstein-Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, write down the Kolmogorov backward equation. Verify that $u(t, x) = xe^{-\kappa t}$ solves the backward equation with initial condition $g(x) = x$. What is the probabilistic interpretation of this solution?

??? success "Solution to Exercise 1"
    For the OU process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, the generator is:

    $$
    \mathcal{L} = -\kappa x\frac{\partial}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2}{\partial x^2}
    $$

    The backward equation is:

    $$
    \frac{\partial u}{\partial t} = -\kappa x\frac{\partial u}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2}
    $$

    **Verification** that $u(t, x) = xe^{-\kappa t}$ solves it with $g(x) = x$:

    $$
    \frac{\partial u}{\partial t} = -\kappa x e^{-\kappa t}, \qquad \frac{\partial u}{\partial x} = e^{-\kappa t}, \qquad \frac{\partial^2 u}{\partial x^2} = 0
    $$

    $$
    \mathcal{L}u = -\kappa x \cdot e^{-\kappa t} + \frac{\sigma^2}{2}\cdot 0 = -\kappa x e^{-\kappa t} = \frac{\partial u}{\partial t} \;\checkmark
    $$

    Also $u(0, x) = x \cdot 1 = x = g(x)$. $\checkmark$

    **Probabilistic interpretation**: $u(t, x) = \mathbb{E}[X_t \mid X_0 = x] = xe^{-\kappa t}$. This says the expected position of the OU process at time $t$ decays exponentially toward zero (the long-run mean when $\theta = 0$). The mean-reversion parameter $\kappa$ controls how fast the expectation converges.

---

**Exercise 2.**
For Brownian motion $dX_t = dW_t$, the backward equation is the heat equation $\partial_t u = \frac{1}{2}\partial_{xx} u$. Starting from the initial condition $g(x) = e^{\alpha x}$ for a constant $\alpha$, find the solution $u(t, x) = \mathbb{E}_x[e^{\alpha X_t}]$ by guessing $u(t, x) = e^{\alpha x + \beta t}$ and determining $\beta$.

??? success "Solution to Exercise 2"
    For Brownian motion $dX_t = dW_t$, the backward equation is $\partial_t u = \frac{1}{2}\partial_{xx}u$. We guess $u(t, x) = e^{\alpha x + \beta t}$. Then:

    $$
    \frac{\partial u}{\partial t} = \beta e^{\alpha x + \beta t}, \qquad \frac{\partial^2 u}{\partial x^2} = \alpha^2 e^{\alpha x + \beta t}
    $$

    Substituting into $\partial_t u = \frac{1}{2}\partial_{xx}u$:

    $$
    \beta e^{\alpha x + \beta t} = \frac{\alpha^2}{2}e^{\alpha x + \beta t}
    $$

    Dividing by $e^{\alpha x + \beta t}$ gives $\beta = \frac{\alpha^2}{2}$.

    Therefore the solution is:

    $$
    u(t, x) = e^{\alpha x + \alpha^2 t / 2}
    $$

    **Verification**: At $t = 0$, $u(0, x) = e^{\alpha x} = g(x)$. $\checkmark$

    **Probabilistic check**: $u(t, x) = \mathbb{E}_x[e^{\alpha X_t}] = \mathbb{E}[e^{\alpha(x + W_t)}] = e^{\alpha x}\mathbb{E}[e^{\alpha W_t}]$. Since $W_t \sim N(0, t)$, the moment-generating function gives $\mathbb{E}[e^{\alpha W_t}] = e^{\alpha^2 t/2}$. Therefore $u(t, x) = e^{\alpha x + \alpha^2 t/2}$. $\checkmark$

---

**Exercise 3.**
The backward equation has two forms: the initial value problem $\partial_t u = \mathcal{L}u$ with $u(0, x) = g(x)$ and the terminal value problem $\partial_t v + \mathcal{L}v = 0$ with $v(T, x) = g(x)$. Show that these are related by the substitution $v(t, x) = u(T - t, x)$. Why is the terminal value form more natural for option pricing?

??? success "Solution to Exercise 3"
    Given $v(t, x) = u(T - t, x)$, we compute:

    $$
    \frac{\partial v}{\partial t}(t, x) = -\frac{\partial u}{\partial s}(s, x)\bigg|_{s = T - t}
    $$

    where $s = T - t$. Since $u$ satisfies $\frac{\partial u}{\partial s} = \mathcal{L}u$:

    $$
    \frac{\partial v}{\partial t} = -\mathcal{L}u(T - t, x) = -\mathcal{L}v(t, x)
    $$

    Therefore $\frac{\partial v}{\partial t} + \mathcal{L}v = 0$. $\checkmark$

    For the condition: $v(T, x) = u(T - T, x) = u(0, x) = g(x)$. $\checkmark$

    **Why Form 2 is more natural for option pricing**: In finance, the payoff $g(S_T) = (S_T - K)^+$ is known at maturity $T$. We want to find the present value at time $t < T$. The terminal value formulation $\partial_t v + \mathcal{L}v = 0$ with $v(T, x) = g(x)$ directly models this situation: we know the boundary condition at the future time $T$ and solve backward to find the value at earlier times. The time variable $t$ represents calendar time, running from now to expiry, and $v(t, S)$ gives the option price at each intermediate time.

---

**Exercise 4.**
For geometric Brownian motion $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$, write the backward equation in the variable $S$. Show that under the risk-neutral measure (replacing $\mu$ with $r$) and adding discounting $-rV$, you recover the Black-Scholes PDE:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

??? success "Solution to Exercise 4"
    For GBM $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$, the generator is $\mathcal{L} = \mu S\partial_S + \frac{\sigma^2 S^2}{2}\partial_{SS}$, so the backward equation is:

    $$
    \frac{\partial u}{\partial t} = \mu S\frac{\partial u}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 u}{\partial S^2}
    $$

    Under the risk-neutral measure, replace $\mu$ with $r$. In the terminal value form, the backward equation becomes:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} = 0
    $$

    Now, the option price involves discounting: $V(t, S) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[g(S_T) \mid S_t = S]$. To account for the discounting factor, define $\tilde{V} = e^{r(T-t)}V$, so $\tilde{V}$ satisfies the backward equation without discounting. From $V = e^{-r(T-t)}\tilde{V}$:

    $$
    \frac{\partial V}{\partial t} = re^{-r(T-t)}\tilde{V} + e^{-r(T-t)}\frac{\partial\tilde{V}}{\partial t} = rV + e^{-r(T-t)}\frac{\partial\tilde{V}}{\partial t}
    $$

    Since $\tilde{V}$ satisfies $\frac{\partial\tilde{V}}{\partial t} + rS\frac{\partial\tilde{V}}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2\tilde{V}}{\partial S^2} = 0$, and noting $\frac{\partial V}{\partial S} = e^{-r(T-t)}\frac{\partial\tilde{V}}{\partial S}$ (similarly for the second derivative), substituting gives:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} = rV
    $$

    This is the **Black-Scholes PDE**. $\checkmark$

---

**Exercise 5.**
Verify the backward equation using Ito's lemma: if $v(t, x)$ solves $\partial_t v + \mathcal{L}v = 0$, apply Ito's lemma to $v(t, X_t)$ to show that $v(t, X_t)$ is a local martingale. Taking expectations, conclude that $v(0, x) = \mathbb{E}_x[g(X_T)]$.

??? success "Solution to Exercise 5"
    Suppose $v(t, x)$ solves $\frac{\partial v}{\partial t} + \mathcal{L}v = 0$ with $v(T, x) = g(x)$. Apply Ito's lemma to $v(t, X_t)$:

    $$
    dv(t, X_t) = \frac{\partial v}{\partial t}\,dt + \frac{\partial v}{\partial x}\,dX_t + \frac{1}{2}\frac{\partial^2 v}{\partial x^2}\,(dX_t)^2
    $$

    Substituting $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$ and $(dX_t)^2 = \sigma^2(X_t)\,dt$:

    $$
    dv = \left(\frac{\partial v}{\partial t} + \mu\frac{\partial v}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 v}{\partial x^2}\right)dt + \sigma\frac{\partial v}{\partial x}\,dW_t
    $$

    $$
    = \left(\frac{\partial v}{\partial t} + \mathcal{L}v\right)dt + \sigma\frac{\partial v}{\partial x}\,dW_t = 0 \cdot dt + \sigma\frac{\partial v}{\partial x}\,dW_t
    $$

    So $v(t, X_t)$ is a local martingale (the $dt$ term vanishes because $v$ solves the PDE).

    Under suitable integrability conditions (e.g., $v$ and $\partial_x v \cdot \sigma$ are bounded), $v(t, X_t)$ is a true martingale. Therefore:

    $$
    v(0, x) = \mathbb{E}_x[v(0, X_0)] = \mathbb{E}_x[v(T, X_T)] = \mathbb{E}_x[g(X_T)]
    $$

    This confirms that the solution to the backward PDE gives the expected value of the terminal payoff. $\checkmark$

---

**Exercise 6.**
Dynkin's formula states $\mathbb{E}_x[g(X_t)] = g(x) + \mathbb{E}_x\left[\int_0^t (\mathcal{L}g)(X_s)\,ds\right]$. Differentiate both sides with respect to $t$ at $t = 0$ to recover the backward equation at $t = 0$. Why does the Markov property allow you to extend this to all $t > 0$?

??? success "Solution to Exercise 6"
    Dynkin's formula states:

    $$
    \mathbb{E}_x[g(X_t)] = g(x) + \mathbb{E}_x\left[\int_0^t(\mathcal{L}g)(X_s)\,ds\right]
    $$

    Differentiating both sides with respect to $t$:

    $$
    \frac{\partial}{\partial t}\mathbb{E}_x[g(X_t)] = \frac{\partial}{\partial t}\mathbb{E}_x\left[\int_0^t(\mathcal{L}g)(X_s)\,ds\right] = \mathbb{E}_x[(\mathcal{L}g)(X_t)]
    $$

    At $t = 0$:

    $$
    \frac{\partial}{\partial t}\mathbb{E}_x[g(X_t)]\bigg|_{t=0} = \mathbb{E}_x[(\mathcal{L}g)(X_0)] = (\mathcal{L}g)(x)
    $$

    Writing $u(t, x) = \mathbb{E}_x[g(X_t)]$, this gives $\partial_t u(0, x) = (\mathcal{L}u)(0, x)$, which is the backward equation at $t = 0$.

    **Extension to all $t > 0$ via the Markov property**: By the Markov property, $\mathbb{E}_x[g(X_{t+h}) \mid \mathcal{F}_t] = \mathbb{E}_{X_t}[g(X_h)]$. Therefore:

    $$
    u(t + h, x) = \mathbb{E}_x[g(X_{t+h})] = \mathbb{E}_x[\mathbb{E}_{X_t}[g(X_h)]] = \mathbb{E}_x[u(h, X_t)]
    $$

    This shows that $u(t + h, x)$ can be viewed as computing the expectation $\mathbb{E}_x[\tilde{g}(X_t)]$ where $\tilde{g}(\cdot) = u(h, \cdot)$. Applying the same Dynkin argument to $\tilde{g}$ and differentiating with respect to $h$ at $h = 0$ gives $\partial_t u(t, x) = (\mathcal{L}u)(t, x)$ for all $t > 0$.

---

**Exercise 7.**
Consider the first exit time $\tau = \inf\{t \geq 0 : X_t \notin (a, b)\}$ for a Brownian motion with drift $dX_t = \mu\,dt + \sigma\,dW_t$. The expected exit time $u(x) = \mathbb{E}_x[\tau]$ satisfies the boundary value problem $\mathcal{L}u = -1$ in $(a, b)$ with $u(a) = u(b) = 0$. Solve this ODE explicitly and verify that $u(x) > 0$ for $x \in (a, b)$.

??? success "Solution to Exercise 7"
    The ODE is $\mathcal{L}u = -1$ with $\mathcal{L} = \mu\frac{d}{dx} + \frac{\sigma^2}{2}\frac{d^2}{dx^2}$:

    $$
    \mu u' + \frac{\sigma^2}{2}u'' = -1, \qquad u(a) = u(b) = 0
    $$

    **Case 1: $\mu = 0$**. The ODE becomes $\frac{\sigma^2}{2}u'' = -1$, so $u'' = -2/\sigma^2$. Integrating twice:

    $$
    u(x) = -\frac{x^2}{\sigma^2} + C_1 x + C_2
    $$

    Boundary conditions: $u(a) = 0$ and $u(b) = 0$ give $C_1 = \frac{a + b}{\sigma^2}$ and $C_2 = -\frac{ab}{\sigma^2}$. Thus:

    $$
    u(x) = \frac{(x - a)(b - x)}{\sigma^2}
    $$

    Since $a < x < b$, both factors are positive, so $u(x) > 0$. $\checkmark$

    **Case 2: $\mu \neq 0$**. Let $\lambda = 2\mu/\sigma^2$. The ODE is $u'' + \lambda u' = -2/\sigma^2$. The homogeneous solution is $u_h = A + Be^{-\lambda x}$. A particular solution is $u_p = -x/\mu$ (verify: $u_p' = -1/\mu$, $u_p'' = 0$, so $\mu(-1/\mu) + 0 = -1$). The general solution:

    $$
    u(x) = A + Be^{-\lambda x} - \frac{x}{\mu}
    $$

    Applying $u(a) = 0$ and $u(b) = 0$:

    $$
    A + Be^{-\lambda a} = \frac{a}{\mu}, \qquad A + Be^{-\lambda b} = \frac{b}{\mu}
    $$

    Subtracting: $B(e^{-\lambda a} - e^{-\lambda b}) = \frac{a - b}{\mu}$, so:

    $$
    B = \frac{a - b}{\mu(e^{-\lambda a} - e^{-\lambda b})}
    $$

    and $A = \frac{a}{\mu} - Be^{-\lambda a}$.

    **Positivity**: By the maximum principle for elliptic equations, since $\mathcal{L}u = -1 < 0$ in $(a, b)$ and $u = 0$ on the boundary, the minimum of $u$ must be attained on the boundary. Since $u(a) = u(b) = 0$ and $u$ cannot have an interior minimum below zero (that would contradict $\mathcal{L}u = -1 < 0$), we conclude $u(x) \geq 0$ in $[a, b]$. The strong maximum principle sharpens this to $u(x) > 0$ for $x \in (a, b)$.
