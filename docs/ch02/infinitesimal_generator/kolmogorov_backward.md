# Kolmogorov Backward Equation

The **Kolmogorov backward equation** describes how expected values of functions of a diffusion process depend on the initial condition. It is a fundamental PDE that connects stochastic processes to analytical methods.

---

## Setting

Consider the time-homogeneous diffusion:

$$
dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t
$$

with infinitesimal generator:

$$
\mathcal{L} = \mu(x)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2}{\partial x^2}
$$

---

## The Backward Equation for Transition Densities

Let $p(t, x, y)$ be the transition density:

$$
\mathbb{P}(X_t \in dy \mid X_0 = x) = p(t, x, y)\,dy
$$

**Theorem**: The transition density satisfies the backward equation:

$$
\boxed{
\frac{\partial p}{\partial t}(t, x, y) = \mathcal{L}_x p(t, x, y)
}
$$

where $\mathcal{L}_x$ acts on the **initial point** variable $x$:

$$
\mathcal{L}_x p = \mu(x)\frac{\partial p}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2 p}{\partial x^2}
$$

**Initial condition**: As $t \to 0^+$, $p(t, x, y) \to \delta(x - y)$.

---

## The Backward Equation for Expected Values

More generally, for any function $g$, define:

$$
u(t, x) = \mathbb{E}[g(X_t) \mid X_0 = x] = \int g(y) p(t, x, y)\,dy
$$

**Theorem**: The function $u$ satisfies:

$$
\boxed{
\frac{\partial u}{\partial t} = \mathcal{L} u
}
$$

with initial condition $u(0, x) = g(x)$.

---

## Derivation

### Method 1: From the Generator Definition

By definition of the generator:

$$
\mathcal{L}u(0,x) = \lim_{t \to 0} \frac{\mathbb{E}_x[g(X_t)] - g(x)}{t} = \lim_{t \to 0} \frac{u(t,x) - u(0,x)}{t} = \frac{\partial u}{\partial t}(0, x)
$$

By the Markov property, this extends to all times:

$$
\frac{\partial u}{\partial t}(t, x) = \mathcal{L}_x u(t, x)
$$

### Method 2: Using Itô's Lemma

Apply Itô's lemma to $u(T-t, X_t)$ where $u$ solves $\partial_t u = \mathcal{L} u$:

$$
d[u(T-t, X_t)] = \left(-\frac{\partial u}{\partial t} + \mathcal{L} u\right)dt + \frac{\partial u}{\partial x}\sigma\,dW_t = \frac{\partial u}{\partial x}\sigma\,dW_t
$$

This is a martingale! Taking expectations:

$$
u(T, x) = \mathbb{E}_x[u(0, X_T)] = \mathbb{E}_x[g(X_T)]
$$

---

## Terminal Value Problem

Often the backward equation is posed as a **terminal value problem**. If we want:

$$
v(t, x) = \mathbb{E}[g(X_T) \mid X_t = x]
$$

then $v$ satisfies:

$$
\boxed{
\frac{\partial v}{\partial t} + \mathcal{L} v = 0, \quad v(T, x) = g(x)
}
$$

**Note**: The sign changes because we're going backward from terminal time $T$.

---

## Examples

### Example 1: Brownian Motion

For $dX_t = dW_t$ (so $\mu = 0$, $\sigma = 1$):

$$
\frac{\partial u}{\partial t} = \frac{1}{2}\frac{\partial^2 u}{\partial x^2}
$$

This is the **heat equation**! The solution with $u(0,x) = g(x)$ is:

$$
u(t, x) = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi t}} e^{-(y-x)^2/2t} g(y)\,dy
$$

### Example 2: Brownian Motion with Drift

For $dX_t = \mu\,dt + \sigma\,dW_t$:

$$
\frac{\partial u}{\partial t} = \mu\frac{\partial u}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2}
$$

This is the **advection-diffusion equation**.

### Example 3: Ornstein-Uhlenbeck

For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$:

$$
\frac{\partial u}{\partial t} = -\kappa x\frac{\partial u}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2}
$$

---

## Interpretation

The backward equation describes how the **probability of reaching a target** changes as we vary the **starting point**.

**Question answered**: "From where should I start to achieve a given expected outcome?"

| Variable | Role |
|----------|------|
| $t$ | Time elapsed |
| $x$ | Initial position (varied) |
| $y$ | Final position (fixed target) |

---

## Connection to Dynkin's Formula

Dynkin's formula is the integrated version of the backward equation:

$$
\mathbb{E}_x[g(X_t)] = g(x) + \mathbb{E}_x\left[\int_0^t (\mathcal{L}g)(X_s)\,ds\right]
$$

Differentiating at $t = 0$ recovers $\frac{\partial}{\partial t}\mathbb{E}_x[g(X_t)]\big|_{t=0} = \mathcal{L}g(x)$.

---

## Well-Posedness

Under standard conditions (bounded, Lipschitz coefficients):

1. **Existence**: Classical solution exists for smooth $g$
2. **Uniqueness**: Solution is unique in appropriate function spaces
3. **Regularity**: Solution inherits smoothness from coefficients and initial data

For less regular data, **viscosity solutions** provide the appropriate framework.

---

## Summary

$$
\boxed{
\frac{\partial u}{\partial t}(t, x) = \mathcal{L}_x u(t, x) = \mu(x)\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2 u}{\partial x^2}
}
$$

**The Kolmogorov backward equation is the PDE satisfied by expected values of diffusion processes, with the generator acting on the initial condition.**
