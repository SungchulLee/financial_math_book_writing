# The Infinitesimal Generator

The **infinitesimal generator** is the fundamental object that characterizes a Markov process. It captures the local dynamics of the process and connects stochastic differential equations to partial differential equations. Understanding generators is essential for Dynkin's formula, Kolmogorov equations, the Feynman–Kac formula, and the martingale problem.

!!! warning "Scope of This Document"
    This document focuses on **diffusion processes**—continuous Markov processes driven by Brownian motion. The generator takes the form of a second-order differential operator.
    
    For **jump processes** (Lévy processes, compound Poisson), the generator includes an integral term and becomes an integro-differential operator.

!!! tip "Related Content"
    - [Dynkin's Formula](dynkin_formula.md) — integral form of the generator
    - [Generator and Martingales](generator_and_martingales.md) — martingale characterization
    - [Fokker–Planck Equation](../../ch03/kolmogorov_equations/kolmogorov_forward.md) — the adjoint generator and density evolution
    - [Kolmogorov Backward Equation](../../ch03/kolmogorov_equations/kolmogorov_backward.md) — PDE for expectations

---

## Motivation

Consider a diffusion process $X_t$ and a smooth function $f$. We want to understand how $\mathbb{E}[f(X_t) \mid X_{t_0} = x_0]$ changes with time, starting from position $x_0$ at time $t_0$.

**Key question**: What is the instantaneous rate of change?

$$
\lim_{h \downarrow 0} \frac{\mathbb{E}[f(X_{t_0+h}) \mid X_{t_0} = x_0] - f(x_0)}{h} = \, ?
$$

The answer is the **generator** acting on $f$.

### Why Should You Care? A Financial Example

Consider **geometric Brownian motion** $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$ modeling a stock price. Its generator is:

$$
\mathcal{L} = \mu S \frac{\partial}{\partial S} + \frac{\sigma^2 S^2}{2} \frac{\partial^2}{\partial S^2}
$$

The **Black–Scholes PDE** for option pricing is:

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

This is precisely $\partial_t V + \mathcal{L}^{(r)} V - rV = 0$, where $\mathcal{L}^{(r)}$ is the generator under the risk-neutral measure. The generator is the **bridge** connecting the stochastic model to the pricing PDE.

---

## Definition

Let $X_t$ be a time-inhomogeneous Markov process on $\mathbb{R}^d$ with dynamics that may depend on time.

!!! abstract "Definition (Infinitesimal Generator — Pointwise)"
    The **infinitesimal generator** $\mathcal{L}_t$ at time $t_0$ is the operator defined by:

    $$
    \boxed{
    (\mathcal{L}_{t_0} f)(x_0) := \lim_{h \downarrow 0} \frac{\mathbb{E}[f(X_{t_0+h}) \mid X_{t_0} = x_0] - f(x_0)}{h}
    }
    $$

    for functions $f$ in the **domain** of $\mathcal{L}$:

    $$
    \mathrm{Dom}(\mathcal{L}) = \left\{ f : \text{the limit exists for all } x_0 \right\}
    $$

**Interpretation**: $(\mathcal{L}_{t_0} f)(x_0)$ is the **instantaneous expected rate of change** of $f$ at position $x_0$, starting at time $t_0$.

---

## Generator of a Diffusion Process

For a diffusion process solving the SDE:

$$
dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t
$$

the generator is:

$$
\boxed{
(\mathcal{L}_t f)(x) = \mu(x, t)f'(x) + \frac{1}{2}\sigma^2(x, t)f''(x)
}
$$

!!! info "Meaning of the Subscript $t$"
    The subscript $t$ on $\mathcal{L}_t$ indicates that the coefficients are **evaluated at time $t$**. Specifically, when computing $(\mathcal{L}_{t_0} f)(x_0)$, we use:
    
    - Drift: $\mu(x_0, t_0)$
    - Diffusion: $\sigma(x_0, t_0)$
    
    The generator acts on the **spatial variable** $x$ while the subscript specifies the **time at which coefficients are frozen**.

!!! note "Time-Homogeneous Case"
    When coefficients are independent of time, i.e., $\mu(x,t) = \mu(x)$ and $\sigma(x,t) = \sigma(x)$, the generator simplifies to:
    
    $$(\mathcal{L}f)(x) = \mu(x)f'(x) + \frac{1}{2}\sigma^2(x)f''(x)$$
    
    and we drop the subscript $t$. The subscript notation $\mathbb{E}_{x}[\cdot]$ is also common:
    
    $$(\mathcal{L}f)(x) = \lim_{h \downarrow 0} \frac{\mathbb{E}_x[f(X_h)] - f(x)}{h}$$

### Derivation via Itô's Lemma

!!! warning "Regularity Assumptions"
    The following derivation requires:
    
    1. **Smoothness**: $f \in C^2(\mathbb{R})$ (twice continuously differentiable)
    2. **Integrability**: $\mathbb{E}\left[\int_{t_0}^{t_0+h} |f'(X_s)|^2 \sigma^2(X_s, s) \, ds\right] < \infty$ for the Itô integral to be a martingale
    3. **Coefficient regularity**: $\mu$ and $\sigma$ satisfy conditions ensuring the SDE has a strong solution

Apply Itô's lemma to $f(X_t)$:

$$
df(X_t) = f'(X_t)\,dX_t + \frac{1}{2}f''(X_t)(dX_t)^2
$$

$$
= f'(X_t)[\mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t] + \frac{1}{2}f''(X_t)\sigma^2(X_t, t)\,dt
$$

$$
= \underbrace{\left[\mu(X_t, t)f'(X_t) + \frac{1}{2}\sigma^2(X_t, t)f''(X_t)\right]}_{(\mathcal{L}_t f)(X_t)}dt + f'(X_t)\sigma(X_t, t)\,dW_t
$$

Taking expectations (the Itô integral has zero expectation under the integrability condition):

$$
\frac{d}{dh}\mathbb{E}[f(X_{t_0+h}) \mid X_{t_0} = x_0]\Big|_{h=0} = (\mathcal{L}_{t_0} f)(x_0)
$$

More generally:

$$
\frac{d}{dt}\mathbb{E}[f(X_t) \mid X_{t_0} = x_0] = \mathbb{E}[(\mathcal{L}_t f)(X_t) \mid X_{t_0} = x_0]
$$

---

## Extended Generator for Time-Dependent Functions

When working with functions $f(x, t)$ that depend explicitly on both space and time, we need the **extended generator**.

!!! abstract "Definition (Extended Generator)"
    For $f: \mathbb{R}^d \times [0, T] \to \mathbb{R}$ with $f \in C^{2,1}$ (twice differentiable in $x$, once in $t$), the **extended generator** is:

    $$
    \boxed{
    (\tilde{\mathcal{L}} f)(x, t) = \frac{\partial f}{\partial t}(x, t) + (\mathcal{L}_t f)(x, t)
    }
    $$

    Explicitly:

    $$
    (\tilde{\mathcal{L}} f)(x, t) = \frac{\partial f}{\partial t} + \mu(x, t)\frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2(x, t)\frac{\partial^2 f}{\partial x^2}
    $$

**Why this matters**: The extended generator appears naturally in:

- **Feynman–Kac formula**: The PDE $\tilde{\mathcal{L}} u - r u = 0$ connects to discounted expectations
- **Dynkin's formula for time-dependent functions**: $f(X_t, t) - f(X_{t_0}, t_0) - \int_{t_0}^t (\tilde{\mathcal{L}} f)(X_s, s) \, ds$ is a martingale
- **Kolmogorov backward equation**: Written compactly as $\tilde{\mathcal{L}} u = 0$

See [Feynman–Kac Formula](../../ch03/feynman_kac/feynman_kac_formula.md) for the primary application.

---

## Multidimensional Generator

For a $d$-dimensional diffusion driven by $m$ independent Brownian motions:

$$
dX_t^i = \mu^i(X_t, t)\,dt + \sum_{\alpha=1}^{m}\sigma^{i\alpha}(X_t, t)\,dW_t^\alpha, \quad i = 1, \ldots, d
$$

!!! info "Index Convention"
    - $i, j \in \{1, \ldots, d\}$: indices for state-space dimensions
    - $\alpha \in \{1, \ldots, m\}$: indices for independent Brownian motions
    - $\sigma$ is a $d \times m$ matrix: $\sigma^{i\alpha}$ is the sensitivity of $X^i$ to $W^\alpha$

The generator is:

$$
\boxed{
(\mathcal{L}_t f)(x) = \sum_{i=1}^d \mu^i(x, t)\frac{\partial f}{\partial x_i}(x) + \frac{1}{2}\sum_{i,j=1}^d a^{ij}(x, t)\frac{\partial^2 f}{\partial x_i \partial x_j}(x)
}
$$

where the **diffusion matrix** (or covariance matrix) is:

$$
a^{ij}(x,t) = \sum_{\alpha=1}^{m}\sigma^{i\alpha}(x,t)\sigma^{j\alpha}(x,t) = (\sigma \sigma^\top)^{ij}
$$

**In vector notation**:

$$
\mathcal{L}_t f = \mu \cdot \nabla f + \frac{1}{2} a : \nabla^2 f = \mu \cdot \nabla f + \frac{1}{2} \mathrm{tr}(a \cdot \nabla^2 f)
$$

---

## Examples (Time-Homogeneous)

The following classical examples have time-independent coefficients.

### Example 1: Brownian Motion

For $dX_t = dW_t$ (i.e., $\mu = 0$, $\sigma = 1$):

$$
\mathcal{L} = \frac{1}{2}\frac{d^2}{dx^2}
$$

This is half the **Laplacian**, explaining the connection between Brownian motion and the heat equation.

### Example 2: Brownian Motion with Drift

For $dX_t = \mu\,dt + \sigma\,dW_t$ (constant coefficients):

$$
\mathcal{L} = \mu\frac{d}{dx} + \frac{\sigma^2}{2}\frac{d^2}{dx^2}
$$

### Example 3: Ornstein–Uhlenbeck Process

For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$:

$$
\mathcal{L} = -\kappa x\frac{d}{dx} + \frac{\sigma^2}{2}\frac{d^2}{dx^2}
$$

??? example "Worked Example: Computing $\mathcal{L}f$ for $f(x) = x^2$"
    For the OU process with $f(x) = x^2$:
    
    - $f'(x) = 2x$
    - $f''(x) = 2$
    
    Therefore:
    
    $$(\mathcal{L}f)(x) = -\kappa x \cdot 2x + \frac{\sigma^2}{2} \cdot 2 = -2\kappa x^2 + \sigma^2$$
    
    **Verification**: For small $h$, Dynkin's formula gives:
    
    $$\mathbb{E}[X_h^2 \mid X_0 = x_0] \approx x_0^2 + h(-2\kappa x_0^2 + \sigma^2) = x_0^2(1 - 2\kappa h) + \sigma^2 h$$
    
    This matches the exact formula $\mathbb{E}[X_h^2 \mid X_0 = x_0] = x_0^2 e^{-2\kappa h} + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa h})$ to first order in $h$.

### Example 4: Geometric Brownian Motion

For $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$:

$$
\mathcal{L} = \mu S\frac{d}{dS} + \frac{\sigma^2 S^2}{2}\frac{d^2}{dS^2}
$$

!!! warning "Domain Restriction"
    GBM lives on the positive half-line $(0, \infty)$. The generator is only defined for $S > 0$, and functions in $\mathrm{Dom}(\mathcal{L})$ must satisfy appropriate boundary conditions as $S \to 0^+$ and $S \to \infty$. This is important for option pricing where payoffs may not be smooth at $S = 0$.

---

## Domain Considerations

The generator is only defined for functions where the limit exists. This is not just a technicality—it affects which functions can be used in Dynkin's formula and related results.

**Typical function spaces**:

| Space | Notation | Description |
|-------|----------|-------------|
| Smooth compact support | $C_c^\infty(\mathbb{R}^d)$ | Infinitely differentiable, zero outside a compact set |
| Vanishing at infinity | $C_0^2(\mathbb{R}^d)$ | Twice differentiable, $f(x) \to 0$ as $\|x\| \to \infty$ |
| Schwartz space | $\mathcal{S}(\mathbb{R}^d)$ | Rapidly decreasing with all derivatives |

For diffusions with smooth coefficients, the generator is well-defined on $C^2$ functions satisfying appropriate growth conditions.

!!! warning "Boundary and Growth Conditions"
    The precise domain depends on:
    
    - **Boundary behavior**: reflection, absorption, or killing at boundaries
    - **Coefficient degeneracy**: when $\sigma(x) \to 0$ at some points
    - **Growth conditions**: behavior of $\mu$ and $\sigma$ at infinity
    
    For example, the generator of reflecting Brownian motion on $[0, \infty)$ requires boundary conditions at $x = 0$ (Neumann condition: $f'(0) = 0$).

??? example "Functions Where the Generator Fails"
    Consider Brownian motion with $\mathcal{L} = \frac{1}{2}\frac{d^2}{dx^2}$.
    
    - $f(x) = |x|$ — $f''$ doesn't exist at $x = 0$
    - $f(x) = e^{x^2}$ — may fail growth conditions at infinity
    - $f(x) = \mathbf{1}_{[0,1]}(x)$ (indicator function) — not differentiable

---

## Transition Operators

The generator describes **local** (infinitesimal) dynamics. The **transition operator** describes **global** (finite-time) evolution.

!!! abstract "Definition (Transition Operator)"
    The **transition operator** $P_{t_0, t}$ is defined by:

    $$
    (P_{t_0, t} f)(x_0) = \mathbb{E}[f(X_t) \mid X_{t_0} = x_0]
    $$

    It maps a function $f$ to its expected value at time $t$, given the process starts at $x_0$ at time $t_0$.

The generator is the infinitesimal version:

$$
(\mathcal{L}_{t_0} f)(x_0) = \lim_{h \downarrow 0} \frac{(P_{t_0, t_0+h} f)(x_0) - f(x_0)}{h}
$$

### Chapman–Kolmogorov Equation

The transition operators satisfy the **Chapman–Kolmogorov equation**: for $t_0 < s < t$,

$$
P_{t_0, t} = P_{s, t} \circ P_{t_0, s}
$$

This is simply the **Markov property** in operator form: to compute the expectation at time $t$, we can first evolve to any intermediate time $s$, then continue from $s$ to $t$.

!!! info "Operator Composition Order"
    The composition $P_{s,t} \circ P_{t_0, s}$ means: **first** apply $P_{t_0, s}$ (evolve from $t_0$ to $s$), **then** apply $P_{s,t}$ (evolve from $s$ to $t$). In operator notation, the rightmost operator acts first:
    
    $$(P_{s,t} \circ P_{t_0, s})f = P_{s,t}(P_{t_0, s} f)$$

### Time-Homogeneous Case

When coefficients don't depend on time, the transition operator depends only on the **time difference** $h = t - t_0$:

$$
P_{t_0, t_0 + h} = P_h \quad \text{(independent of } t_0\text{)}
$$

In this case, the Chapman–Kolmogorov equation becomes:

$$
P_{h_1 + h_2} = P_{h_1} \circ P_{h_2}
$$

---

## Key Properties

### 1. Linearity

$$
\mathcal{L}(\alpha f + \beta g) = \alpha \mathcal{L}f + \beta \mathcal{L}g
$$

### 2. Maximum Principle (Diffusions Only)

For **diffusion generators** (no jumps), if $f$ attains a maximum at $x^*$ and $f \in \mathrm{Dom}(\mathcal{L})$:

$$
(\mathcal{L}f)(x^*) \leq 0
$$

??? abstract "Proof"
    At a maximum, $f'(x^*) = 0$ and $f''(x^*) \leq 0$. Therefore:

    $$(\mathcal{L}f)(x^*) = \mu(x^*) \cdot 0 + \frac{1}{2}\sigma^2(x^*) \cdot f''(x^*) \leq 0$$

    since $\sigma^2(x^*) \geq 0$.

!!! warning "Failure for Jump Processes"
    This maximum principle is **specific to diffusion generators**. For processes with jumps (e.g., Lévy processes), the generator includes an integral term:
    
    $$\mathcal{L}f(x) = \mu(x) f'(x) + \frac{\sigma^2(x)}{2}f''(x) + \int_{\mathbb{R}} \left[f(x+y) - f(x) - y f'(x) \mathbf{1}_{|y|<1}\right] \nu(dy)$$
    
    The integral term can be positive even at a maximum of $f$, violating the principle. This has important consequences for optimal stopping and free boundary problems with jumps.

### 3. Characterizes the Process

Under mild regularity conditions, the generator **uniquely determines** the law of the process. This is the basis of the **martingale problem** approach (Stroock–Varadhan).

| Direction | Statement | Condition |
|-----------|-----------|-----------|
| Process → $\mathcal{L}$ | Given SDE, compute generator | Always (by definition) |
| $\mathcal{L}$ → Process | Given generator, recover process law | Requires regularity conditions |

The Stroock–Varadhan martingale problem addresses the **inverse direction**: given $\mathcal{L}$, does there exist a unique process whose generator is $\mathcal{L}$?

!!! warning "When Uniqueness Can Fail"
    Without regularity conditions:
    
    - **Non-uniqueness**: Multiple processes may share the same generator
    - **Non-existence**: No process may realize a given generator
    
    Typical regularity conditions involve continuity and growth bounds on $\mu(x,t)$ and $\sigma(x,t)$, plus ellipticity ($\sigma > 0$).

See [Martingale Problem](../diffusion_process/martingale_problem_stroock_varadhan.md).

---

## The Generator and Martingales

!!! abstract "Theorem (Dynkin's Martingale)"
    For $f \in C^2$ with appropriate integrability conditions, the process:

    $$
    M_t^f := f(X_t) - f(X_{t_0}) - \int_{t_0}^t (\mathcal{L}_s f)(X_s)\,ds
    $$

    is a **martingale** with respect to the natural filtration.

**Proof**: This follows directly from Itô's lemma—the drift term is $(\mathcal{L}_s f)(X_s)\,ds$, and the Itô integral $\int f'(X_s)\sigma(X_s, s)\,dW_s$ is a martingale (under the square-integrability condition).

See [Generator and Martingales](generator_and_martingales.md) for details.

### Harmonic Functions

A function $f$ is **$\mathcal{L}$-harmonic** if:

$$
\mathcal{L}f = 0
$$

**Consequence**: If $\mathcal{L}f = 0$, then $f(X_t)$ is a martingale.

!!! note "Terminology"
    The term "$\mathcal{L}$-harmonic" generalizes the classical notion of harmonic functions (satisfying $\Delta f = 0$). For standard Brownian motion where $\mathcal{L} = \frac{1}{2}\Delta$, a function is $\mathcal{L}$-harmonic if and only if it is classically harmonic. However, for other processes (e.g., OU process), $\mathcal{L}$-harmonic functions differ from classically harmonic functions.

---

## Connection to PDEs

The generator connects stochastic processes to partial differential equations.

### Kolmogorov Backward Equation

The function $u(x_0, t_0) = \mathbb{E}[g(X_T) \mid X_{t_0} = x_0]$ satisfies:

$$
\frac{\partial u}{\partial t_0} + \mathcal{L}_{t_0} u = 0, \quad u(x_0, T) = g(x_0)
$$

where $\mathcal{L}_{t_0}$ acts on $x_0$ with coefficients evaluated at time $t_0$.

!!! info "Sign Convention"
    The equation is written with $t_0$ as the **initial time** variable, running backward from the terminal time $T$. As $t_0$ increases toward $T$, we have less time for the process to evolve, so $u$ approaches the terminal condition $g$.
    
    Some texts use $t$ as a forward time variable with $u(x, t) = \mathbb{E}[g(X_T) \mid X_t = x]$, yielding the same equation. The key point: the derivative is with respect to the **conditioning time**, and the generator acts on the **conditioning position**.

See [Kolmogorov Backward Equation](../../ch03/kolmogorov_equations/kolmogorov_backward.md).

### Kolmogorov Forward (Fokker–Planck) Equation

The transition density $p(x, t \mid x_0, t_0)$ satisfies:

$$
\frac{\partial p}{\partial t} = \mathcal{L}^*_t p
$$

where $\mathcal{L}^*_t$ is the **adjoint** of $\mathcal{L}_t$, acting on $x$ with coefficients evaluated at time $t$. See [Fokker–Planck Equation](../../ch03/kolmogorov_equations/kolmogorov_forward.md).

### Feynman–Kac Formula

The function:

$$
u(x_0, t_0) = \mathbb{E}\left[e^{-\int_{t_0}^T r(X_s, s)\,ds} g(X_T) \,\Big|\, X_{t_0} = x_0\right]
$$

satisfies:

$$
\frac{\partial u}{\partial t_0} + \mathcal{L}_{t_0} u - r(x_0, t_0) u = 0, \quad u(x_0, T) = g(x_0)
$$

Using the extended generator notation: $\tilde{\mathcal{L}} u - r u = 0$ where $\tilde{\mathcal{L}} = \partial_t + \mathcal{L}_t$.

See [Feynman–Kac Formula](feynman_kac.md).

---

## The Adjoint Generator

The **adjoint** $\mathcal{L}^*_t$ is defined by the duality relation:

$$
\int_{-\infty}^{\infty} f(x)(\mathcal{L}_t g)(x)\,dx = \int_{-\infty}^{\infty} (\mathcal{L}^*_t f)(x)g(x)\,dx
$$

for suitable test functions with vanishing boundary terms.

For a diffusion with coefficients $\mu(x, t)$ and $\sigma(x, t)$:

$$
\boxed{
\mathcal{L}^*_t f = -\frac{\partial}{\partial x}[\mu(x, t) f] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x, t) f]
}
$$

??? abstract "Derivation via Integration by Parts"
    Starting from the duality requirement, we compute $\int f \cdot \mathcal{L}_t g \, dx$ and integrate by parts to move derivatives onto $f$.
    
    **First-order term** (drift):
    
    $$\int_{-\infty}^{\infty} f(x) \cdot \mu(x,t) g'(x) \, dx$$
    
    Integrate by parts ($u = f \mu$, $dv = g' dx$):
    
    $$= \underbrace{[f \mu g]_{-\infty}^{\infty}}_{= 0} - \int_{-\infty}^{\infty} (f \mu)' g \, dx = -\int_{-\infty}^{\infty} \frac{\partial}{\partial x}[\mu f] \cdot g \, dx$$
    
    **Second-order term** (diffusion):
    
    $$\int_{-\infty}^{\infty} f(x) \cdot \frac{1}{2}\sigma^2(x,t) g''(x) \, dx$$
    
    Integrate by parts twice ($u = f \sigma^2/2$, $dv = g'' dx$):
    
    First integration:
    $$= \underbrace{\left[\frac{\sigma^2 f}{2} g'\right]_{-\infty}^{\infty}}_{= 0} - \int_{-\infty}^{\infty} \frac{\partial}{\partial x}\left[\frac{\sigma^2 f}{2}\right] g' \, dx$$
    
    Second integration:
    $$= -\underbrace{\left[\frac{\partial}{\partial x}\left(\frac{\sigma^2 f}{2}\right) g\right]_{-\infty}^{\infty}}_{= 0} + \int_{-\infty}^{\infty} \frac{\partial^2}{\partial x^2}\left[\frac{\sigma^2 f}{2}\right] g \, dx$$
    
    **Combining**:
    
    $$\int f \cdot \mathcal{L}_t g \, dx = \int \left( -\frac{\partial}{\partial x}[\mu f] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2 f] \right) g \, dx$$
    
    Therefore:
    
    $$\mathcal{L}^*_t f = -\frac{\partial}{\partial x}[\mu(x,t) f] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x,t) f]$$

| Operator | Acts on | Formula |
|----------|---------|---------|
| $\mathcal{L}_t$ | Test functions | $\mu(x,t) f'(x) + \frac{1}{2}\sigma^2(x,t) f''(x)$ |
| $\mathcal{L}^*_t$ | Densities | $-[\mu(x,t) f]' + \frac{1}{2}[\sigma^2(x,t) f]''$ |

The adjoint appears in:

- **Fokker–Planck equation**: $\partial_t p = \mathcal{L}^*_t p$
- **Invariant measures** (time-homogeneous case): $\mathcal{L}^* \pi = 0$

---

## Beyond Diffusions: Jump Process Generators

This document focuses on diffusion processes, but generators extend naturally to processes with jumps.

### Lévy Process Generator

For a Lévy process with drift $b$, diffusion $\sigma$, and Lévy measure $\nu$, the generator is:

$$
\mathcal{L}f(x) = b f'(x) + \frac{\sigma^2}{2}f''(x) + \int_{\mathbb{R} \setminus \{0\}} \left[f(x+y) - f(x) - y f'(x) \mathbf{1}_{|y|<1}\right] \nu(dy)
$$

The integral term captures the contribution of jumps:

- $f(x+y) - f(x)$: change in $f$ due to a jump of size $y$
- $-yf'(x)\mathbf{1}_{|y|<1}$: compensator for small jumps (ensures integrability)
- $\nu(dy)$: Lévy measure giving the intensity of jumps of size $y$

### Jump-Diffusion Generator

For a jump-diffusion $dX_t = \mu(X_t)dt + \sigma(X_t)dW_t + dJ_t$ where $J_t$ is a compound Poisson process with intensity $\lambda$ and jump size distribution $F$:

$$
\mathcal{L}f(x) = \mu(x)f'(x) + \frac{\sigma^2(x)}{2}f''(x) + \lambda \int_{\mathbb{R}} [f(x+y) - f(x)] F(dy)
$$

**Key differences for jump processes include**:
    
- The maximum principle fails (integral term can be positive at maxima)
- Domain requirements are different (smoothness conditions depend on $\nu$)
- The martingale problem requires different techniques

---

## Summary

| Object | Definition | Role |
|--------|------------|------|
| Generator $\mathcal{L}_t$ | $\lim_{h \downarrow 0} \frac{\mathbb{E}[f(X_{t_0+h}) \mid X_{t_0}=x_0] - f(x_0)}{h}$ | Local (infinitesimal) dynamics |
| Extended generator $\tilde{\mathcal{L}}$ | $\partial_t + \mathcal{L}_t$ | Time-dependent functions |
| Transition operator $P_{t_0, t}$ | $\mathbb{E}[f(X_t) \mid X_{t_0} = x_0]$ | Global (finite-time) evolution |
| Adjoint $\mathcal{L}^*_t$ | Defined by duality | Density evolution |

$$
\boxed{
\mathcal{L}_t = \mu(x, t)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x, t)\frac{\partial^2}{\partial x^2}
}
$$

**The infinitesimal generator is the bridge between stochastic processes (SDEs) and partial differential equations (PDEs).**

---

??? note "Quick Reference: Key Formulas"
    **1D Generator**:
    $$\mathcal{L}_t f = \mu(x,t) f'(x) + \frac{\sigma^2(x,t)}{2} f''(x)$$
    
    **Extended Generator** (for $f(x,t)$):
    $$\tilde{\mathcal{L}} f = \partial_t f + \mathcal{L}_t f$$
    
    **Multi-D Generator**:
    $$\mathcal{L}_t f = \sum_i \mu^i \partial_i f + \frac{1}{2}\sum_{i,j} a^{ij} \partial_i \partial_j f$$
    
    **Adjoint**:
    $$\mathcal{L}^*_t f = -\partial_x[\mu f] + \frac{1}{2}\partial_x^2[\sigma^2 f]$$
    
    **Transition Operator**:
    $$(P_{t_0, t} f)(x_0) = \mathbb{E}[f(X_t) \mid X_{t_0} = x_0]$$
    
    **Dynkin's Martingale**:
    $$M_t = f(X_t) - f(X_0) - \int_0^t (\mathcal{L}_s f)(X_s) \, ds$$
    
    **Kolmogorov Backward**:
    $$\partial_{t_0} u + \mathcal{L}_{t_0} u = 0$$
    
    **Fokker–Planck**:
    $$\partial_t p = \mathcal{L}^*_t p$$

---

## See Also

- [Dynkin's Formula](dynkin_formula.md) — integral form connecting generator to expectations
- [Generator and Martingales](generator_and_martingales.md) — martingale characterization
- [Fokker–Planck Equation](fokker_planck.md) — forward equation using $\mathcal{L}^*$
- [Kolmogorov Backward Equation](../../ch03/kolmogorov_equations/kolmogorov_backward.md) — backward equation using $\mathcal{L}$
- [Feynman–Kac Formula](../../ch03/feynman_kac/feynman_kac_formula.md) — discounted expectations
- [Martingale Problem](../diffusion_process/martingale_problem_stroock_varadhan.md) — characterization via generator
