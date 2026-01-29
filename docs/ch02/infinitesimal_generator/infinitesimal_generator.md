# The Infinitesimal Generator

The **infinitesimal generator** is the fundamental object that characterizes a Markov process. It captures the local dynamics of the process and connects stochastic differential equations to partial differential equations. Understanding generators is essential for Dynkin's formula, Kolmogorov equations, the Feynman–Kac formula, and the martingale problem.

!!! tip "Related Content"
    - [Dynkin's Formula](dynkin_formula.md) — integral form of the generator
    - [Generator and Martingales](generator_and_martingales.md) — martingale characterization
    - [Fokker–Planck Equation](fokker_planck.md) — the adjoint generator and density evolution
    - [Kolmogorov Backward Equation](kolmogorov_backward.md) — PDE for expectations

---

## Motivation

Consider a diffusion process $X_t$ and a smooth function $f$. We want to understand how $\mathbb{E}[f(X_t) \mid X_{t_0} = x_0]$ changes with time, starting from position $x_0$ at time $t_0$.

**Key question**: What is the instantaneous rate of change?

$$
\lim_{h \downarrow 0} \frac{\mathbb{E}[f(X_{t_0+h}) \mid X_{t_0} = x_0] - f(x_0)}{h} = \, ?
$$

The answer is the **generator** acting on $f$.

---

## Definition

Let $X_t$ be a Markov process on $\mathbb{R}^d$.

!!! abstract "Definition (Infinitesimal Generator)"
    The **infinitesimal generator** $\mathcal{L}$ is the operator defined by:

    $$
    \boxed{
    (\mathcal{L}f)(x_0) := \lim_{h \downarrow 0} \frac{\mathbb{E}[f(X_{t_0+h}) \mid X_{t_0} = x_0] - f(x_0)}{h}
    }
    $$

    for functions $f$ in the **domain** of $\mathcal{L}$:

    $$
    \mathrm{Dom}(\mathcal{L}) = \left\{ f : \text{the limit exists for all } x_0 \right\}
    $$

**Interpretation**: $(\mathcal{L}f)(x_0)$ is the **instantaneous expected rate of change** of $f$ at position $x_0$.

!!! note "Notation"
    For time-homogeneous processes, the generator does not depend on $t_0$, so we simply write $(\mathcal{L}f)(x)$. The subscript notation $\mathbb{E}_{x}[\cdot]$ is also common:
    
    $$(\mathcal{L}f)(x) = \lim_{h \downarrow 0} \frac{\mathbb{E}_x[f(X_h)] - f(x)}{h}$$

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

The subscript $t$ on $\mathcal{L}_t$ indicates that the generator may depend on time through the coefficients $\mu(x,t)$ and $\sigma(x,t)$.

!!! note "Time-Homogeneous Case"
    When coefficients are independent of time, i.e., $\mu(x,t) = \mu(x)$ and $\sigma(x,t) = \sigma(x)$, the generator simplifies to:
    
    $$(\mathcal{L}f)(x) = \mu(x)f'(x) + \frac{1}{2}\sigma^2(x)f''(x)$$
    
    and we drop the subscript $t$.

### Derivation via Itô's Lemma

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

Taking expectations (the Itô integral has zero expectation):

$$
\frac{d}{dh}\mathbb{E}[f(X_{t_0+h}) \mid X_{t_0} = x_0]\Big|_{h=0} = (\mathcal{L}_{t_0} f)(x_0)
$$

More generally:

$$
\frac{d}{dt}\mathbb{E}[f(X_t) \mid X_{t_0} = x_0] = \mathbb{E}[(\mathcal{L}_t f)(X_t) \mid X_{t_0} = x_0]
$$

---

## Multidimensional Generator

For a $d$-dimensional diffusion:

$$
dX_t^i = \mu^i(X_t, t)\,dt + \sum_{\alpha}\sigma^{i\alpha}(X_t, t)\,dW_t^\alpha
$$

the generator is:

$$
\boxed{
(\mathcal{L}_t f)(x) = \sum_{i=1}^d \mu^i(x, t)\frac{\partial f}{\partial x_i}(x) + \frac{1}{2}\sum_{i,j=1}^d a^{ij}(x, t)\frac{\partial^2 f}{\partial x_i \partial x_j}(x)
}
$$

where $a^{ij}(x,t) = \sum_{\alpha}\sigma^{i\alpha}(x,t)\sigma^{j\alpha}(x,t)$ is the diffusion matrix.

**In vector notation**:

$$
\mathcal{L}_t f = \mu \cdot \nabla f + \frac{1}{2} a : \nabla^2 f
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

### Example 4: Geometric Brownian Motion

For $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$:

$$
\mathcal{L} = \mu S\frac{d}{dS} + \frac{\sigma^2 S^2}{2}\frac{d^2}{dS^2}
$$

---

## The Semigroup and Generator

The generator is intimately connected to the **transition operators**.

### Time-Homogeneous Case

For time-homogeneous processes, define the **semigroup** $P_h$:

$$
(P_h f)(x_0) = \mathbb{E}[f(X_{t_0+h}) \mid X_{t_0} = x_0]
$$

**Semigroup property**: $P_{h_1+h_2} = P_{h_1} \circ P_{h_2}$

**Generator as derivative**:

$$
\mathcal{L} = \lim_{h \downarrow 0} \frac{P_h - I}{h} = \frac{d}{dh}\Big|_{h=0} P_h
$$

**Exponential relationship**:

$$
P_h = e^{h\mathcal{L}}
$$

This means:

$$
\mathbb{E}[f(X_{t_0+h}) \mid X_{t_0} = x_0] = (e^{h\mathcal{L}}f)(x_0) = f(x_0) + h(\mathcal{L}f)(x_0) + \frac{h^2}{2}(\mathcal{L}^2 f)(x_0) + \cdots
$$

where $\mathcal{L}^2 f = \mathcal{L}(\mathcal{L}f)$ means applying the generator twice.

### Time-Inhomogeneous Case

For time-inhomogeneous processes, the semigroup property **fails** because $\mathcal{L}_t$ changes with time. Instead, we have a **two-parameter family** of operators:

$$
(P_{t_0, t} f)(x_0) = \mathbb{E}[f(X_t) \mid X_{t_0} = x_0]
$$

**Chapman–Kolmogorov equation**: For $t_0 < s < t$:

$$
P_{t_0, t} = P_{s, t} \circ P_{t_0, s}
$$

**Time-ordered exponential (Dyson series)**:

The simple exponential $e^{(t-t_0)\mathcal{L}}$ no longer works. Instead:

$$
P_{t_0, t} = \mathcal{T} \exp\left(\int_{t_0}^{t} \mathcal{L}_s \, ds\right)
$$

where $\mathcal{T}$ denotes **time-ordering**. Expanding this gives:

$$
P_{t_0, t} = I + \int_{t_0}^{t} \mathcal{L}_{s_1} \, ds_1 + \int_{t_0}^{t} \int_{t_0}^{s_1} \mathcal{L}_{s_1} \mathcal{L}_{s_2} \, ds_2 \, ds_1 + \cdots
$$

!!! info "Why Time-Ordering?"
    In the time-homogeneous case, $\mathcal{L}$ commutes with itself at different times (trivially, since it's the same operator). But when $\mathcal{L}_t$ depends on $t$, we generally have:
    
    $$\mathcal{L}_{t_1} \mathcal{L}_{t_2} \neq \mathcal{L}_{t_2} \mathcal{L}_{t_1}$$
    
    The time-ordering $\mathcal{T}$ ensures operators are applied in the correct chronological sequence: later times act first (to the left).

### Comparison

| Aspect | Time-Homogeneous | Time-Inhomogeneous |
|--------|------------------|-------------------|
| Operator family | One-parameter $P_h$ | Two-parameter $P_{t_0, t}$ |
| Key property | Semigroup: $P_{h_1+h_2} = P_{h_1} P_{h_2}$ | Chapman–Kolmogorov: $P_{t_0,t} = P_{s,t} P_{t_0,s}$ |
| Exponential formula | $P_h = e^{h\mathcal{L}}$ | $P_{t_0,t} = \mathcal{T}\exp\left(\int_{t_0}^t \mathcal{L}_s \, ds\right)$ |
| Generator | Constant $\mathcal{L}$ | Time-dependent $\mathcal{L}_t$ |

---

## Key Properties

### 1. Linearity

$$
\mathcal{L}(\alpha f + \beta g) = \alpha \mathcal{L}f + \beta \mathcal{L}g
$$

### 2. Maximum Principle

If $f$ attains a maximum at $x^*$ and $f \in \mathrm{Dom}(\mathcal{L})$:

$$
(\mathcal{L}f)(x^*) \leq 0
$$

??? abstract "Proof"
    At a maximum, $f'(x^*) = 0$ and $f''(x^*) \leq 0$. Therefore:

    $$(\mathcal{L}f)(x^*) = \mu(x^*) \cdot 0 + \frac{1}{2}\sigma^2(x^*) \cdot f''(x^*) \leq 0$$

    since $\sigma^2(x^*) \geq 0$.

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
    For $f \in \mathrm{Dom}(\mathcal{L})$, the process:

    $$
    M_t^f := f(X_t) - f(X_{t_0}) - \int_{t_0}^t (\mathcal{L}f)(X_s)\,ds
    $$

    is a **martingale** with respect to the natural filtration.

**Proof**: This follows directly from Itô's lemma—the drift term is $(\mathcal{L}f)(X_s)\,ds$, and the Itô integral $\int f'(X_s)\sigma(X_s)\,dW_s$ is a martingale.

See [Generator and Martingales](generator_and_martingales.md) for details.

### Harmonic Functions

A function $f$ is **$\mathcal{L}$-harmonic** if:

$$
\mathcal{L}f = 0
$$

**Consequence**: If $\mathcal{L}f = 0$, then $f(X_t)$ is a martingale.

---

## Connection to PDEs

The generator connects stochastic processes to partial differential equations.

### Kolmogorov Backward Equation

The function $u(x_0, t_0) = \mathbb{E}[g(X_T) \mid X_{t_0} = x_0]$ satisfies:

$$
\frac{\partial u}{\partial t_0} + \mathcal{L}_{t_0} u = 0, \quad u(x_0, T) = g(x_0)
$$

where $\mathcal{L}_{t_0}$ acts on $x_0$ with coefficients evaluated at time $t_0$.

See [Kolmogorov Backward Equation](kolmogorov_backward.md).

### Kolmogorov Forward (Fokker–Planck) Equation

The transition density $p(x, t \mid x_0, t_0)$ satisfies:

$$
\frac{\partial p}{\partial t} = \mathcal{L}^*_t p
$$

where $\mathcal{L}^*_t$ is the **adjoint** of $\mathcal{L}_t$, acting on $x$ with coefficients evaluated at time $t$. See [Fokker–Planck Equation](fokker_planck.md).

### Feynman–Kac Formula

The function:

$$
u(x_0, t_0) = \mathbb{E}\left[e^{-\int_{t_0}^T r(X_s, s)\,ds} g(X_T) \,\Big|\, X_{t_0} = x_0\right]
$$

satisfies:

$$
\frac{\partial u}{\partial t_0} + \mathcal{L}_{t_0} u - r(x_0, t_0) u = 0, \quad u(x_0, T) = g(x_0)
$$

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

| Operator | Acts on | Formula |
|----------|---------|---------|
| $\mathcal{L}_t$ | Test functions | $\mu(x,t) f'(x) + \frac{1}{2}\sigma^2(x,t) f''(x)$ |
| $\mathcal{L}^*_t$ | Densities | $-[\mu(x,t) f]' + \frac{1}{2}[\sigma^2(x,t) f]''$ |

The adjoint appears in:

- **Fokker–Planck equation**: $\partial_t p = \mathcal{L}^*_t p$
- **Invariant measures** (time-homogeneous case): $\mathcal{L}^* \pi = 0$

---

---

## Domain Considerations

The generator is only defined on its **domain** $\mathrm{Dom}(\mathcal{L})$.

**Typical domains**:

- $C_0^2(\mathbb{R}^d)$: twice continuously differentiable functions vanishing at infinity
- $C_c^\infty(\mathbb{R}^d)$: smooth compactly supported functions

**Core**: A subset $D \subset \mathrm{Dom}(\mathcal{L})$ is a **core** if $\mathcal{L}$ is uniquely determined by its values on $D$. Finding a core is important for the well-posedness of the martingale problem.

---

## Summary

| Object | Definition | Role |
|--------|------------|------|
| Generator $\mathcal{L}_t$ | $\lim_{h \downarrow 0} \frac{\mathbb{E}[f(X_{t_0+h}) \mid X_{t_0}=x_0] - f(x_0)}{h}$ | Local dynamics |
| Semigroup $P_{t_0, t}$ | $\mathbb{E}[f(X_t) \mid X_{t_0} = x_0]$ | Global evolution |
| Adjoint $\mathcal{L}^*_t$ | Defined by duality | Density evolution |

$$
\boxed{
\mathcal{L}_t = \mu(x, t)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x, t)\frac{\partial^2}{\partial x^2}
}
$$

**The infinitesimal generator is the bridge between stochastic processes (SDEs) and partial differential equations (PDEs).**

---

## See Also

- [Dynkin's Formula](dynkin_formula.md) — integral form connecting generator to expectations
- [Generator and Martingales](generator_and_martingales.md) — martingale characterization
- [Fokker–Planck Equation](fokker_planck.md) — forward equation using $\mathcal{L}^*$
- [Kolmogorov Backward Equation](kolmogorov_backward.md) — backward equation using $\mathcal{L}$
- [Feynman–Kac Formula](feynman_kac.md) — discounted expectations
- [Martingale Problem](../diffusion_process/martingale_problem_stroock_varadhan.md) — characterization via generator
