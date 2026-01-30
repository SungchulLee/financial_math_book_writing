# Kolmogorov Backward Equation

The **Kolmogorov backward equation** describes how expected values of functions of a diffusion process depend on the initial condition. It is the PDE satisfied by $u(t,x) = \mathbb{E}_x[g(X_t)]$, with the generator acting on the **initial point**.

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

The backward equation appears in two equivalent forms depending on the time convention.

### Form 1: Initial Value Problem (Forward in Time)

**Question**: Given initial condition $g$, how does $\mathbb{E}_x[g(X_t)]$ evolve as $t$ increases?

$$\boxed{\frac{\partial u}{\partial t} = \mathcal{L} u, \quad u(0, x) = g(x)}$$

Here $u(t, x) = \mathbb{E}[g(X_t) \mid X_0 = x]$.

**Time runs forward**: $t = 0 \to t = T$.

### Form 2: Terminal Value Problem (Backward in Time)

**Question**: Given terminal payoff $g$ at time $T$, what is the expected value at earlier time $t$?

$$\boxed{\frac{\partial v}{\partial t} + \mathcal{L} v = 0, \quad v(T, x) = g(x)}$$

Here $v(t, x) = \mathbb{E}[g(X_T) \mid X_t = x]$.

**Time runs backward**: $t = T \to t = 0$.

### Relationship Between the Forms

| Aspect | Form 1 (IVP) | Form 2 (TVP) |
|--------|--------------|--------------|
| PDE | $\partial_t u = \mathcal{L}u$ | $\partial_t v + \mathcal{L}v = 0$ |
| Condition | $u(0,x) = g(x)$ | $v(T,x) = g(x)$ |
| Interpretation | Evolve from initial data | Propagate from terminal data |
| Time direction | Forward | Backward |

**They are the same equation**: If $u$ solves Form 1, then $v(t,x) = u(T-t, x)$ solves Form 2.

!!! info "Which Form to Use?"
    - **Form 1**: Natural for transition densities, heat equation perspective
    - **Form 2**: Natural for finance (option pricing), optimal control
    
    Finance typically uses Form 2 because we know the terminal payoff and want present value.

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

---

## Expected Value Form

For any (nice) function $g$:

$$u(t, x) = \mathbb{E}[g(X_t) \mid X_0 = x] = \int g(y)\, p(t; x, y)\,dy$$

**Theorem**: $u$ satisfies the backward equation:

$$\boxed{\frac{\partial u}{\partial t} = \mathcal{L} u, \quad u(0, x) = g(x)}$$

---

## Derivation

### Method 1: From the Generator Definition

By definition of the infinitesimal generator:

$$(\mathcal{L}g)(x) = \lim_{t \downarrow 0} \frac{\mathbb{E}_x[g(X_t)] - g(x)}{t} = \lim_{t \downarrow 0} \frac{u(t,x) - u(0,x)}{t} = \frac{\partial u}{\partial t}(0, x)$$

This shows $\partial_t u = \mathcal{L}u$ at $t = 0$.

By the Markov property, the same argument applies at any time $t$:

$$\frac{\partial u}{\partial t}(t, x) = \mathcal{L}_x u(t, x)$$

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
    - **Backward**: "From which starting points do we reach a given target?"
    - **Forward**: "Where does the probability mass flow over time?"

See [Fokker–Planck Equation](fokker_planck.md).

---

## Examples

### Example 1: Brownian Motion

**SDE**: $dX_t = dW_t$ (so $\mu = 0$, $\sigma = 1$)

**Backward equation**:

$$\frac{\partial u}{\partial t} = \frac{1}{2}\frac{\partial^2 u}{\partial x^2}$$

This is the **heat equation**.

**Solution** with $u(0,x) = g(x)$:

$$u(t, x) = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi t}} e^{-(y-x)^2/2t} g(y)\,dy$$

The kernel $\frac{1}{\sqrt{2\pi t}} e^{-(y-x)^2/2t}$ is the **heat kernel** = transition density of BM.

---

### Example 2: Brownian Motion with Drift

**SDE**: $dX_t = \mu\,dt + \sigma\,dW_t$

**Backward equation**:

$$\frac{\partial u}{\partial t} = \mu\frac{\partial u}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2}$$

This is the **advection-diffusion equation**.

---

### Example 3: Ornstein–Uhlenbeck

**SDE**: $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$

**Backward equation**:

$$\frac{\partial u}{\partial t} = -\kappa x\frac{\partial u}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2}$$

---

### Example 4: Geometric Brownian Motion

**SDE**: $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$

**Generator**: $\mathcal{L} = \mu s\frac{\partial}{\partial s} + \frac{\sigma^2 s^2}{2}\frac{\partial^2}{\partial s^2}$

**Backward equation**:

$$\frac{\partial u}{\partial t} = \mu s\frac{\partial u}{\partial s} + \frac{\sigma^2 s^2}{2}\frac{\partial^2 u}{\partial s^2}$$

Under the risk-neutral measure ($\mu = r$), the terminal value form:

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} = rV$$

is the **Black–Scholes PDE** (with discounting).

---

## Connection to Feynman–Kac

The backward equation is a **special case** of the Feynman–Kac formula with zero potential.

| Problem | PDE | Probabilistic Solution |
|---------|-----|----------------------|
| Backward equation | $\partial_t u = \mathcal{L}u$ | $u(t,x) = \mathbb{E}_x[g(X_t)]$ |
| Feynman–Kac | $\partial_t u = \mathcal{L}u - V(x)u$ | $u(t,x) = \mathbb{E}_x\left[e^{-\int_0^t V(X_s)ds} g(X_t)\right]$ |

The potential $V(x)$ introduces **discounting** or **killing**.

See [Feynman–Kac Formula](feynman_kac.md).

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

---

## Boundary Conditions

For diffusions on **bounded domains** $D$, boundary conditions are needed.

| Type | Condition | Interpretation |
|------|-----------|----------------|
| **Dirichlet** | $u = g$ on $\partial D$ | Absorbing boundary (process killed) |
| **Neumann** | $\frac{\partial u}{\partial n} = 0$ on $\partial D$ | Reflecting boundary |
| **Robin** | $\alpha u + \beta \frac{\partial u}{\partial n} = g$ | Partial absorption/reflection |

The choice depends on the physical/financial problem.

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

For irregular data or degenerate diffusions, **viscosity solutions** provide the right framework.

---

## Summary

| Form | PDE | Condition | Solution |
|------|-----|-----------|----------|
| IVP | $\partial_t u = \mathcal{L}u$ | $u(0,x) = g(x)$ | $u(t,x) = \mathbb{E}_x[g(X_t)]$ |
| TVP | $\partial_t v + \mathcal{L}v = 0$ | $v(T,x) = g(x)$ | $v(t,x) = \mathbb{E}[g(X_T) \mid X_t = x]$ |

$$\boxed{\frac{\partial u}{\partial t} = \mathcal{L}_x u = \mu(x)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2 u}{\partial x^2}}$$

**The Kolmogorov backward equation is the PDE for expected values, with the generator acting on the initial condition.**

---

## See Also

- [Fokker–Planck Equation](fokker_planck.md) — the forward equation (adjoint)
- [Infinitesimal Generator](infinitesimal_generator.md) — defines $\mathcal{L}$
- [Dynkin's Formula](dynkin_formula.md) — integral form
- [Feynman–Kac Formula](feynman_kac.md) — extension with potential/discounting
