# Diffusion Process Overview

## Concept Definition

Let $(\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{P})$ be a filtered probability space satisfying the **usual conditions** (right-continuity of $(\mathcal{F}_t)$; $\mathcal{F}_0$ contains all $\mathbb{P}$-null sets). Let

$$
W_t = (W_t^{1}, \dots, W_t^{m})
$$

be an $m$-dimensional Brownian motion adapted to $(\mathcal{F}_t)$.

!!! info "Definition: Itô Diffusion"
    An $\mathbb{R}^d$-valued process $X_t = (X_t^{1}, \dots, X_t^{d})$ is an **Itô diffusion** if it satisfies the stochastic differential equation

    $$
    \mathrm{d}X_t^{i}
    = b^{i}(t, X_t)\,\mathrm{d}t
    + \sigma^{i\alpha}(t, X_t)\,\mathrm{d}W_t^{\alpha},
    \qquad i = 1, \dots, d,\quad \alpha = 1, \dots, m,
    $$

    where:

    - $b^{i} : [0,\infty) \times \mathbb{R}^d \to \mathbb{R}$ is the **drift field**,
    - $\sigma^{i\alpha} : [0,\infty) \times \mathbb{R}^d \to \mathbb{R}$ is the **diffusion matrix**.

    The Einstein summation convention is in force throughout (repeated Greek indices are summed from $1$ to $m$).

The differential form is symbolic. The **mathematically precise definition** is the integral equation

$$
X_t^{i}
= X_0^{i}
+ \int_0^t b^{i}(s, X_s)\,\mathrm{d}s
+ \int_0^t \sigma^{i\alpha}(s, X_s)\,\mathrm{d}W_s^{\alpha}.
$$

---

## Explanation

### Semimartingale Decomposition

Every Itô diffusion is a **semimartingale**: it decomposes as

$$
X_t^{i}
= \underbrace{X_0^{i} + \int_0^t b^{i}(s, X_s)\,\mathrm{d}s}_{\text{finite variation (drift)}}
+ \underbrace{\int_0^t \sigma^{i\alpha}(s, X_s)\,\mathrm{d}W_s^{\alpha}}_{\text{local martingale (noise)}}.
$$

Paths $t \mapsto X_t(\omega)$ are **continuous almost surely**, since both integrals produce continuous processes.

### Diffusion Matrix and Quadratic Covariation

Define the **covariance matrix**

$$
a^{ij}(t, x) := \sigma^{i\alpha}(t, x)\,\sigma^{j\alpha}(t, x).
$$

This matrix is symmetric and non-negative definite. A defining identity for diffusions is

$$
\mathrm{d}\langle X^{i}, X^{j} \rangle_t = a^{ij}(t, X_t)\,\mathrm{d}t.
$$

That is, **quadratic covariation grows linearly in time at a rate determined by the current state**.

### Infinitesimal Generator

For $f \in C^{1,2}([0,\infty)\times\mathbb{R}^d)$ (once differentiable in $t$, twice in $x$), the **infinitesimal generator** acting on the spatial variables is

$$
(\mathcal{L}f)(t, x)
= b^{i}(t, x)\,\frac{\partial f}{\partial x_i}(x)
+ \frac{1}{2}\,a^{ij}(t, x)\,\frac{\partial^2 f}{\partial x_i \partial x_j}(x).
$$

Here $\mathcal{L}$ acts on the *spatial* argument of $f$; the coefficients $b^i, a^{ij}$ carry the time dependence. For time-homogeneous coefficients one may restrict to $f \in C^{2}(\mathbb{R}^d)$; the full Itô formula requires $C^{1,2}$ regularity.

By Itô's formula,

$$
f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(s, X_s)\,\mathrm{d}s
= \int_0^t \frac{\partial f}{\partial x_i}(X_s)\,\sigma^{i\alpha}(s, X_s)\,\mathrm{d}W_s^{\alpha},
$$

which is a local martingale. This local martingale characterisation of diffusions is the foundation of the **martingale problem formulation** (see [Martingale Problem — Stroock–Varadhan](martingale_problem_stroock_varadhan.md)).

### Markov Property

Under standard Lipschitz and linear-growth conditions on $b$ and $\sigma$, the SDE has a unique strong solution and $X_t$ is a **strong Markov process**:

$$
\mathbb{E}[f(X_t) \mid \mathcal{F}_s] = \mathbb{E}[f(X_t) \mid X_s], \qquad s \le t.
$$

The extension to stopping times is the **strong Markov property** (see [Strong Markov Property](strong_markov_property.md)).

---

## Diagram / Example

### Special Cases

**Pure Brownian motion** ($b = 0$, $\sigma = I$):

$$
\mathrm{d}X_t^{i} = \mathrm{d}W_t^{i}.
$$

**Drifted Brownian motion:**

$$
\mathrm{d}X_t^{i} = b^{i}(X_t)\,\mathrm{d}t + \mathrm{d}W_t^{i}.
$$

**Gradient diffusion** (Langevin equation):

$$
\mathrm{d}X_t = -\nabla V(X_t)\,\mathrm{d}t + \sqrt{2}\,\mathrm{d}W_t,
$$

which has invariant density $\pi(x) \propto e^{-V(x)}$ whenever $\int e^{-V} < \infty$. This is the prototypical example for invariant measures; see [Invariant Measures and Stationarity](invariant_measures_and_stationarity.md).

### Structure at a Glance

$$
\boxed{
\text{Diffusion}
= \text{state-dependent drift} + \text{state-dependent Brownian noise}
}
$$

| Component | Symbol | Role |
|---|---|---|
| Drift | $b^i(t,x)$ | Deterministic push |
| Diffusion matrix | $\sigma^{i\alpha}(t,x)$ | Amplitude of noise |
| Covariance matrix | $a^{ij} = \sigma^{i\alpha}\sigma^{j\alpha}$ | Quadratic variation rate |
| Generator | $\mathcal{L}$ | Infinitesimal mean evolution |

---

## Proof / Derivation

The SDE integral equation is well-defined under standard conditions. We verify the semimartingale decomposition and the quadratic covariation identity.

**Quadratic covariation.** By bilinearity of quadratic covariation and $\langle W^{\alpha}, W^{\beta} \rangle_t = \delta^{\alpha\beta} t$:

$$
\langle X^i, X^j \rangle_t
= \left\langle \int_0^{\cdot} \sigma^{i\alpha}(s, X_s)\,\mathrm{d}W_s^{\alpha},\;
\int_0^{\cdot} \sigma^{j\beta}(s, X_s)\,\mathrm{d}W_s^{\beta} \right\rangle_t
= \int_0^t \sigma^{i\alpha}(s, X_s)\,\sigma^{j\beta}(s, X_s)\,\mathrm{d}\langle W^\alpha, W^\beta \rangle_s
= \int_0^t \sigma^{i\alpha}(s, X_s)\,\sigma^{j\alpha}(s, X_s)\,\mathrm{d}s
= \int_0^t a^{ij}(s, X_s)\,\mathrm{d}s.
$$

(The Itô isometry gives $\mathbb{E}[\langle M \rangle_t] = \mathbb{E}[\int_0^t h_s^2\,\mathrm{d}s]$ for an $L^2$ martingale $M = \int h\,\mathrm{d}W$; it is the bilinearity identity above that yields the pathwise quadratic covariation.)

**Itô's formula.** For $f \in C^{1,2}([0,\infty) \times \mathbb{R}^d)$, the chain rule for semimartingales gives:

$$
\mathrm{d}f(t, X_t)
= \frac{\partial f}{\partial t}\,\mathrm{d}t
+ \frac{\partial f}{\partial x_i}\,\mathrm{d}X_t^i
+ \frac{1}{2}\,\frac{\partial^2 f}{\partial x_i \partial x_j}\,\mathrm{d}\langle X^i, X^j \rangle_t.
$$

Substituting $\mathrm{d}X_t^i = b^i\,\mathrm{d}t + \sigma^{i\alpha}\,\mathrm{d}W_t^\alpha$ and $\mathrm{d}\langle X^i,X^j\rangle_t = a^{ij}\,\mathrm{d}t$, and collecting all $\mathrm{d}t$ terms:

$$
\mathrm{d}f(t, X_t)
= \underbrace{\left(\frac{\partial f}{\partial t} + b^i\frac{\partial f}{\partial x_i} + \frac{1}{2}a^{ij}\frac{\partial^2 f}{\partial x_i\partial x_j}\right)}_{= \,\partial_t f \,+\, \mathcal{L}f}\mathrm{d}t
+ \frac{\partial f}{\partial x_i}\,\sigma^{i\alpha}\,\mathrm{d}W_t^{\alpha}
= \left(\frac{\partial f}{\partial t} + \mathcal{L}f\right)\mathrm{d}t
+ \frac{\partial f}{\partial x_i}\,\sigma^{i\alpha}\,\mathrm{d}W_t^{\alpha}.
$$

The stochastic integral term is a local martingale; the remaining term is finite variation. $\square$

---

## What to Remember

- A diffusion is a continuous-path Markov semimartingale whose quadratic covariation is $\mathrm{d}\langle X^i, X^j\rangle_t = a^{ij}(t, X_t)\,\mathrm{d}t$.
- The drift $b$ and diffusion matrix $\sigma$ fully specify the dynamics; $a = \sigma\sigma^\top$ is the effective covariance.
- The generator $\mathcal{L}$ encodes the infinitesimal mean behaviour and connects SDEs to PDEs (Kolmogorov equations).
- The SDE defines the process pathwise; the martingale problem defines it in law via $\mathcal{L}$ alone.
