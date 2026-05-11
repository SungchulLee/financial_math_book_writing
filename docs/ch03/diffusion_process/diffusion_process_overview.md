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
    \qquad i = 1, \dots, d,\quad \alpha = 1, \dots, m
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
+ \int_0^t \sigma^{i\alpha}(s, X_s)\,\mathrm{d}W_s^{\alpha}
$$

!!! note "Three equivalent views of a diffusion"
    The same object can be understood through three lenses:

    1. **SDE** (pathwise): $\mathrm{d}X_t = b\,\mathrm{d}t + \sigma\,\mathrm{d}W_t$
    2. **Generator** (analytic): $\mathcal{L} = b \cdot \nabla + \frac{1}{2}a : \nabla^2$
    3. **Martingale problem** (law): $f(X_t) - \int_0^t \mathcal{L}f\,\mathrm{d}s$ is a martingale

    This page is the master definition; later pages (invariant measures, time reversal, large deviations) build on these objects without redefining them.

---

## Explanation

### Semimartingale Decomposition

Every Itô diffusion is a **semimartingale**: it decomposes as

$$
X_t^{i}
= \underbrace{X_0^{i} + \int_0^t b^{i}(s, X_s)\,\mathrm{d}s}_{\text{finite variation (drift)}}

+ \underbrace{\int_0^t \sigma^{i\alpha}(s, X_s)\,\mathrm{d}W_s^{\alpha}}_{\text{local martingale (noise)}}
$$

Paths $t \mapsto X_t(\omega)$ are **continuous almost surely**, since both integrals produce continuous processes.

### Diffusion Matrix and Quadratic Covariation

Define the **covariance matrix**

$$
a^{ij}(t, x) := \sigma^{i\alpha}(t, x)\,\sigma^{j\alpha}(t, x)
$$

This matrix is symmetric and non-negative definite. A defining identity for diffusions is

$$
\mathrm{d}\langle X^{i}, X^{j} \rangle_t = a^{ij}(t, X_t)\,\mathrm{d}t
$$

That is, **quadratic covariation grows linearly in time at a rate determined by the current state**.

### Infinitesimal Generator

For $f \in C^{1,2}([0,\infty)\times\mathbb{R}^d)$ (once differentiable in $t$, twice in $x$), the **infinitesimal generator** acting on the spatial variables is

$$
(\mathcal{L}f)(t, x)
= b^{i}(t, x)\,\frac{\partial f}{\partial x_i}(x)

+ \frac{1}{2}\,a^{ij}(t, x)\,\frac{\partial^2 f}{\partial x_i \partial x_j}(x)
$$

Here $\mathcal{L}$ acts on the *spatial* argument of $f$; the coefficients $b^i, a^{ij}$ carry the time dependence. For time-homogeneous coefficients one may restrict to $f \in C^{2}(\mathbb{R}^d)$; the full Itô formula requires $C^{1,2}$ regularity.

By Itô's formula,

$$
f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(s, X_s)\,\mathrm{d}s
= \int_0^t \frac{\partial f}{\partial x_i}(X_s)\,\sigma^{i\alpha}(s, X_s)\,\mathrm{d}W_s^{\alpha}
$$

which is a local martingale. This local martingale characterisation of diffusions is the foundation of the **martingale problem formulation** (see [Martingale Problem — Stroock–Varadhan](martingale_problem_stroock_varadhan.md)).

### Markov Property

Under standard Lipschitz and linear-growth conditions on $b$ and $\sigma$, the SDE has a unique strong solution and $X_t$ is a **strong Markov process**:

$$
\mathbb{E}[f(X_t) \mid \mathcal{F}_s] = \mathbb{E}[f(X_t) \mid X_s], \qquad s \le t
$$

The extension to stopping times is the **strong Markov property** (see [Strong Markov Property](strong_markov_property.md)).

---

## Diagram / Example

### Special Cases

**Pure Brownian motion** ($b = 0$, $\sigma = I$):

$$
\mathrm{d}X_t^{i} = \mathrm{d}W_t^{i}
$$

**Drifted Brownian motion:**

$$
\mathrm{d}X_t^{i} = b^{i}(X_t)\,\mathrm{d}t + \mathrm{d}W_t^{i}
$$

**Gradient diffusion** (Langevin equation):

$$
\mathrm{d}X_t = -\nabla V(X_t)\,\mathrm{d}t + \sqrt{2}\,\mathrm{d}W_t
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
= \int_0^t a^{ij}(s, X_s)\,\mathrm{d}s
$$

(The Itô isometry gives $\mathbb{E}[\langle M \rangle_t] = \mathbb{E}[\int_0^t h_s^2\,\mathrm{d}s]$ for an $L^2$ martingale $M = \int h\,\mathrm{d}W$; it is the bilinearity identity above that yields the pathwise quadratic covariation.)

**Itô's formula.** For $f \in C^{1,2}([0,\infty) \times \mathbb{R}^d)$, the chain rule for semimartingales gives:

$$
\mathrm{d}f(t, X_t)
= \frac{\partial f}{\partial t}\,\mathrm{d}t

+ \frac{\partial f}{\partial x_i}\,\mathrm{d}X_t^i
+ \frac{1}{2}\,\frac{\partial^2 f}{\partial x_i \partial x_j}\,\mathrm{d}\langle X^i, X^j \rangle_t
$$

Substituting $\mathrm{d}X_t^i = b^i\,\mathrm{d}t + \sigma^{i\alpha}\,\mathrm{d}W_t^\alpha$ and $\mathrm{d}\langle X^i,X^j\rangle_t = a^{ij}\,\mathrm{d}t$, and collecting all $\mathrm{d}t$ terms:

$$
\mathrm{d}f(t, X_t)
= \underbrace{\left(\frac{\partial f}{\partial t} + b^i\frac{\partial f}{\partial x_i} + \frac{1}{2}a^{ij}\frac{\partial^2 f}{\partial x_i\partial x_j}\right)}_{= \,\partial_t f \,+\, \mathcal{L}f}\mathrm{d}t

+ \frac{\partial f}{\partial x_i}\,\sigma^{i\alpha}\,\mathrm{d}W_t^{\alpha}
= \left(\frac{\partial f}{\partial t} + \mathcal{L}f\right)\mathrm{d}t

+ \frac{\partial f}{\partial x_i}\,\sigma^{i\alpha}\,\mathrm{d}W_t^{\alpha}
$$

The stochastic integral term is a local martingale; the remaining term is finite variation. $\square$

---

## What to Remember

- A diffusion is a continuous-path Markov semimartingale whose quadratic covariation is $\mathrm{d}\langle X^i, X^j\rangle_t = a^{ij}(t, X_t)\,\mathrm{d}t$.
- The drift $b$ and diffusion matrix $\sigma$ fully specify the dynamics; $a = \sigma\sigma^\top$ is the effective covariance.
- The generator $\mathcal{L}$ is the central object: it determines local behaviour, martingale structure, invariant measures, and PDEs. A diffusion can be understood in three equivalent ways: (1) pathwise via the SDE, (2) analytically via the generator $\mathcal{L}$, (3) probabilistically via the [martingale problem](martingale_problem_stroock_varadhan.md).
- The SDE defines the process pathwise; the martingale problem defines it in law via $\mathcal{L}$ alone.

---

## Exercises

**Exercise 1.** Let $X_t$ be a one-dimensional Itô diffusion with drift $b(x) = -\alpha x$ and diffusion coefficient $\sigma(x) = \beta$, where $\alpha, \beta > 0$ are constants. Write down the covariance matrix $a(x)$ and the infinitesimal generator $\mathcal{L}$. Apply $\mathcal{L}$ to the test function $f(x) = x^2$ and interpret the result.

??? success "Solution to Exercise 1"
    The diffusion coefficient is $\sigma(x) = \beta$, so the covariance matrix is

    $$
    a(x) = \sigma(x)^2 = \beta^2
    $$

    The infinitesimal generator for a one-dimensional diffusion with drift $b(x) = -\alpha x$ and covariance $a(x) = \beta^2$ is

    $$
    \mathcal{L}f(x) = b(x)\,f'(x) + \frac{1}{2}\,a(x)\,f''(x) = -\alpha x\,f'(x) + \frac{\beta^2}{2}\,f''(x)
    $$

    Applying $\mathcal{L}$ to $f(x) = x^2$: we have $f'(x) = 2x$ and $f''(x) = 2$, so

    $$
    \mathcal{L}(x^2) = -\alpha x \cdot 2x + \frac{\beta^2}{2} \cdot 2 = -2\alpha x^2 + \beta^2
    $$

    **Interpretation.** By Itô's formula, $f(X_t) - f(X_0) - \int_0^t \mathcal{L}f(X_s)\,\mathrm{d}s$ is a local martingale, so

    $$
    \frac{\mathrm{d}}{\mathrm{d}t}\mathbb{E}[X_t^2] = \mathbb{E}[\mathcal{L}(X_t^2)] = -2\alpha\,\mathbb{E}[X_t^2] + \beta^2
    $$

    The term $-2\alpha\,\mathbb{E}[X_t^2]$ represents mean reversion pulling the second moment toward zero, while $\beta^2$ represents the constant injection of variance by the noise. At equilibrium, $\mathbb{E}[X_t^2] = \beta^2/(2\alpha)$.

---

**Exercise 2.** Consider the two-dimensional diffusion $(X_t^1, X_t^2)$ satisfying

$$
\mathrm{d}X_t^1 = X_t^2\,\mathrm{d}t + \mathrm{d}W_t^1, \qquad \mathrm{d}X_t^2 = -X_t^1\,\mathrm{d}t + \mathrm{d}W_t^2
$$

Compute the covariance matrix $a^{ij}$ and the quadratic covariation $\langle X^1, X^2 \rangle_t$. Is $a$ degenerate or non-degenerate?

??? success "Solution to Exercise 2"
    The drift is $b(x) = (x^2, -x^1)^\top$ and the diffusion matrix is $\sigma = I_{2 \times 2}$ (the identity). Therefore

    $$
    a^{ij} = \sigma^{i\alpha}\sigma^{j\alpha} = \delta^{ij}
    $$

    so

    $$
    a = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
    $$

    The quadratic covariation is

    $$
    \langle X^1, X^2 \rangle_t = \int_0^t a^{12}(X_s)\,\mathrm{d}s = \int_0^t 0\,\mathrm{d}s = 0
    $$

    The matrix $a = I$ is strictly positive definite (all eigenvalues equal $1$), so it is **non-degenerate**. The two components of the diffusion are driven by independent Brownian motions, despite the coupling in the drift.

---

**Exercise 3.** Verify the semimartingale decomposition for the geometric Brownian motion $\mathrm{d}S_t = \mu S_t\,\mathrm{d}t + \sigma S_t\,\mathrm{d}W_t$. Identify the drift field $b(s)$, the diffusion coefficient $\sigma(s)$, and the covariance matrix $a(s)$. Write down the infinitesimal generator $\mathcal{L}$ and compute $\mathcal{L}f$ for $f(s) = \log s$.

??? success "Solution to Exercise 3"
    For geometric Brownian motion $\mathrm{d}S_t = \mu S_t\,\mathrm{d}t + \sigma S_t\,\mathrm{d}W_t$, the coefficients are:

    - **Drift field:** $b(s) = \mu s$
    - **Diffusion coefficient:** $\sigma(s) = \sigma s$ (using $\sigma$ for both the constant and the function, with the understanding that the diffusion coefficient function is $s \mapsto \sigma s$)
    - **Covariance matrix:** $a(s) = (\sigma s)^2 = \sigma^2 s^2$

    The semimartingale decomposition is

    $$
    S_t = S_0 + \underbrace{\int_0^t \mu S_s\,\mathrm{d}s}_{\text{finite variation}} + \underbrace{\int_0^t \sigma S_s\,\mathrm{d}W_s}_{\text{local martingale}}
    $$

    The infinitesimal generator is

    $$
    \mathcal{L}f(s) = \mu s\,f'(s) + \frac{1}{2}\sigma^2 s^2\,f''(s)
    $$

    For $f(s) = \log s$: we have $f'(s) = 1/s$ and $f''(s) = -1/s^2$, so

    $$
    \mathcal{L}(\log s) = \mu s \cdot \frac{1}{s} + \frac{1}{2}\sigma^2 s^2 \cdot \left(-\frac{1}{s^2}\right) = \mu - \frac{\sigma^2}{2}
    $$

    This is a constant, confirming that $\log S_t - (\mu - \sigma^2/2)t$ is a local martingale — consistent with the well-known result $\log S_t = \log S_0 + (\mu - \sigma^2/2)t + \sigma W_t$.

---

**Exercise 4.** Let $X_t$ be an Itô diffusion in $\mathbb{R}^d$ with generator $\mathcal{L}$. Using Itô's formula, show that for $f \in C^2(\mathbb{R}^d)$, the process

$$
M_t^f := f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,\mathrm{d}s
$$

is a local martingale. Under what additional condition on $f$ and $\sigma$ does $M_t^f$ become a true martingale?

??? success "Solution to Exercise 4"
    By Itô's formula applied to $f \in C^2(\mathbb{R}^d)$ (taking $f$ time-independent):

    $$
    f(X_t) = f(X_0) + \int_0^t \frac{\partial f}{\partial x_i}(X_s)\,\mathrm{d}X_s^i + \frac{1}{2}\int_0^t \frac{\partial^2 f}{\partial x_i \partial x_j}(X_s)\,\mathrm{d}\langle X^i, X^j \rangle_s
    $$

    Substituting $\mathrm{d}X_s^i = b^i(X_s)\,\mathrm{d}s + \sigma^{i\alpha}(X_s)\,\mathrm{d}W_s^\alpha$ and $\mathrm{d}\langle X^i, X^j\rangle_s = a^{ij}(X_s)\,\mathrm{d}s$:

    $$
    f(X_t) - f(X_0) = \int_0^t \left(b^i \partial_i f + \frac{1}{2}a^{ij}\partial_i\partial_j f\right)(X_s)\,\mathrm{d}s + \int_0^t \partial_i f(X_s)\,\sigma^{i\alpha}(X_s)\,\mathrm{d}W_s^\alpha
    $$

    The first integral is $\int_0^t (\mathcal{L}f)(X_s)\,\mathrm{d}s$, so

    $$
    M_t^f = f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,\mathrm{d}s = \int_0^t \partial_i f(X_s)\,\sigma^{i\alpha}(X_s)\,\mathrm{d}W_s^\alpha
    $$

    This is a stochastic integral with respect to Brownian motion, hence a **local martingale**.

    $M_t^f$ is a **true martingale** if the integrand is square-integrable:

    $$
    \mathbb{E}\!\int_0^t \sum_{i,\alpha} |\partial_i f(X_s)|^2\,|\sigma^{i\alpha}(X_s)|^2\,\mathrm{d}s < \infty
    $$

    A sufficient condition is that $\nabla f$ is bounded (e.g. $f \in C_c^2(\mathbb{R}^d)$) and $\sigma$ satisfies the linear growth condition $|\sigma(x)| \le C(1 + |x|)$, combined with finite moments $\mathbb{E}[\sup_{s \le t}|X_s|^2] < \infty$.

---

**Exercise 5.** For the gradient diffusion $\mathrm{d}X_t = -\nabla V(X_t)\,\mathrm{d}t + \sqrt{2}\,\mathrm{d}W_t$ with $V(x) = \frac{1}{2}k|x|^2$ in $\mathbb{R}^d$ (where $k > 0$), identify the drift, diffusion matrix, and generator. Verify that $\pi(x) \propto e^{-V(x)}$ is a Gaussian density and compute its mean and covariance.

??? success "Solution to Exercise 5"
    For the gradient diffusion $\mathrm{d}X_t = -\nabla V(X_t)\,\mathrm{d}t + \sqrt{2}\,\mathrm{d}W_t$ with $V(x) = \frac{1}{2}k|x|^2$:

    - **Drift:** $b^i(x) = -\partial_i V(x) = -kx^i$
    - **Diffusion matrix:** $\sigma^{i\alpha} = \sqrt{2}\,\delta^{i\alpha}$, so $a^{ij} = 2\delta^{ij}$
    - **Generator:**

    $$
    \mathcal{L}f(x) = -kx^i\,\partial_i f(x) + \frac{1}{2}\cdot 2\delta^{ij}\,\partial_i\partial_j f(x) = -kx \cdot \nabla f(x) + \Delta f(x)
    $$

    The invariant density is $\pi(x) \propto e^{-V(x)} = e^{-k|x|^2/2}$. Normalizing:

    $$
    \pi(x) = \left(\frac{k}{2\pi}\right)^{d/2} \exp\!\left(-\frac{k}{2}|x|^2\right)
    $$

    This is a $d$-dimensional Gaussian with:

    - **Mean:** $\mathbb{E}[X] = 0$
    - **Covariance:** $\mathrm{Cov}(X^i, X^j) = \frac{1}{k}\,\delta^{ij}$, i.e. $\Sigma = \frac{1}{k}I_d$

    This is verified by matching the exponent: $-\frac{k}{2}|x|^2 = -\frac{1}{2}x^\top(kI)x$, which is the exponent of $\mathcal{N}(0, k^{-1}I)$.

---

**Exercise 6.** Consider a one-dimensional diffusion with $b(x) = 0$ and $\sigma(x) = \sqrt{1 + x^2}$. Compute the covariance function $a(x)$ and write down the generator $\mathcal{L}$. Does this diffusion satisfy the standard Lipschitz condition? Does the linear growth condition hold?

??? success "Solution to Exercise 6"
    With $b(x) = 0$ and $\sigma(x) = \sqrt{1 + x^2}$, the covariance function is

    $$
    a(x) = \sigma(x)^2 = 1 + x^2
    $$

    The generator is

    $$
    \mathcal{L}f(x) = \frac{1}{2}(1 + x^2)\,f''(x)
    $$

    **Lipschitz condition.** We need $|\sigma(x) - \sigma(y)| \le L|x - y|$ for some constant $L$. Compute

    $$
    \sigma'(x) = \frac{x}{\sqrt{1 + x^2}}
    $$

    Since $|\sigma'(x)| = |x|/\sqrt{1+x^2} < 1$ for all $x$, by the mean value theorem $|\sigma(x) - \sigma(y)| \le |x - y|$. So the **Lipschitz condition holds** with $L = 1$.

    **Linear growth condition.** We need $|\sigma(x)| \le C(1 + |x|)$ for some constant $C$. Since $\sqrt{1 + x^2} \le 1 + |x|$ (squaring both sides: $1 + x^2 \le 1 + 2|x| + x^2$, which is true), the **linear growth condition holds** with $C = 1$.

    Therefore, by the standard existence and uniqueness theorem, the SDE $\mathrm{d}X_t = \sqrt{1+X_t^2}\,\mathrm{d}W_t$ has a unique strong solution.

---

**Exercise 7.** Let $X_t$ be a $d$-dimensional Itô diffusion with constant drift $b \in \mathbb{R}^d$ and constant diffusion matrix $\sigma \in \mathbb{R}^{d \times m}$. Show that $X_t$ is a Gaussian process and compute $\mathbb{E}[X_t]$ and $\mathrm{Cov}(X_s, X_t)$ for $s \le t$ in terms of $b$, $a = \sigma\sigma^\top$, and the initial condition $X_0 = x_0$.

??? success "Solution to Exercise 7"
    With constant $b$ and $\sigma$, the SDE $\mathrm{d}X_t = b\,\mathrm{d}t + \sigma\,\mathrm{d}W_t$ has the explicit solution

    $$
    X_t = x_0 + bt + \sigma W_t
    $$

    Since $W_t$ is a Gaussian process (every finite collection $(W_{t_1}, \ldots, W_{t_k})$ is jointly Gaussian), and $X_t$ is an affine transformation of $W_t$, $X_t$ is also a **Gaussian process**.

    **Mean:**

    $$
    \mathbb{E}[X_t] = x_0 + bt
    $$

    **Covariance:** For $s \le t$, using $a = \sigma\sigma^\top$:

    $$
    \mathrm{Cov}(X_s^i, X_t^j) = \mathrm{Cov}\!\left(\sigma^{i\alpha}W_s^\alpha,\, \sigma^{j\beta}W_t^\beta\right) = \sigma^{i\alpha}\sigma^{j\beta}\,\mathrm{Cov}(W_s^\alpha, W_t^\beta)
    $$

    Since $\mathrm{Cov}(W_s^\alpha, W_t^\beta) = \min(s,t)\,\delta^{\alpha\beta} = s\,\delta^{\alpha\beta}$ for $s \le t$:

    $$
    \mathrm{Cov}(X_s^i, X_t^j) = \sigma^{i\alpha}\sigma^{j\alpha}\,s = a^{ij}\,s
    $$

    In matrix form:

    $$
    \mathrm{Cov}(X_s, X_t) = a\,\min(s, t) = \sigma\sigma^\top \min(s, t)
    $$
