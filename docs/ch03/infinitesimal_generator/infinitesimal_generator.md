# The Infinitesimal Generator

The **infinitesimal generator** is the fundamental object that characterizes a Markov process. It captures the local dynamics of the process and connects stochastic differential equations to partial differential equations. Understanding generators is essential for Dynkin's formula, Kolmogorov equations, the Feynman–Kac formula, and the martingale problem.

!!! warning "Scope"
    This page focuses on **diffusion processes** — continuous Markov processes driven by Brownian motion. The generator takes the form of a second-order differential operator. For **jump processes** (Lévy processes, compound Poisson), the generator includes an integral term and becomes an integro-differential operator.

!!! tip "Related Pages"
    - [Dynkin's Formula](dynkin_formula.md) — integral form of the generator
    - [Generator and Martingales](generator_and_martingales.md) — martingale characterization
    - [Fokker–Planck Equation](../../ch05/kolmogorov_equations/kolmogorov_forward.md) — the adjoint generator and density evolution
    - [Kolmogorov Backward Equation](../../ch05/kolmogorov_equations/kolmogorov_backward.md) — PDE for expectations

---

## Motivation

Consider a diffusion process $X_t$ and a smooth function $f$. We want to understand how $\mathbb{E}[f(X_t) \mid X_{t_0} = x_0]$ changes with time. The **key question** is the instantaneous rate of change:

$$
\lim_{h \downarrow 0} \frac{\mathbb{E}[f(X_{t_0+h}) \mid X_{t_0} = x_0] - f(x_0)}{h} = \, ?
$$

The answer is the **generator** acting on $f$.

**A financial example.** Consider geometric Brownian motion $dS_t = rS_t\,dt + \sigma S_t\,dW_t$ under the risk-neutral measure (drift equals risk-free rate $r$). Its generator is:

$$
\mathcal{L} = rS \frac{\partial}{\partial S} + \frac{\sigma^2 S^2}{2} \frac{\partial^2}{\partial S^2}
$$

The **Black–Scholes PDE** for option pricing is then exactly $\partial_t V + \mathcal{L}V - rV = 0$. The generator is the bridge connecting the stochastic model to the pricing PDE.

---

## Definition

Let $X_t$ be a Markov process on $\mathbb{R}^d$.

!!! abstract "Definition (Infinitesimal Generator)"
    The **infinitesimal generator** $\mathcal{L}_{t_0}$ at time $t_0$ is the operator:

    $$
    \boxed{
    (\mathcal{L}_{t_0} f)(x_0) := \lim_{h \downarrow 0} \frac{\mathbb{E}[f(X_{t_0+h}) \mid X_{t_0} = x_0] - f(x_0)}{h}
    }
    $$

    for functions $f$ in the **domain** $\mathrm{Dom}(\mathcal{L}) = \{ f : \text{the limit exists for all } x_0 \}$.

**Interpretation**: $(\mathcal{L}_{t_0} f)(x_0)$ is the **instantaneous expected rate of change** of $f$ at position $x_0$, starting at time $t_0$.

---

## Generator of a Diffusion Process

For a diffusion solving the SDE $dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t$, the generator is:

$$
\boxed{
(\mathcal{L}_t f)(x) = \mu(x, t)f'(x) + \frac{1}{2}\sigma^2(x, t)f''(x)
}
$$

!!! info "Time-Homogeneous Case"
    When coefficients are independent of time, $\mu(x,t) = \mu(x)$ and $\sigma(x,t) = \sigma(x)$, we drop the subscript $t$ and write:

    $$(\mathcal{L}f)(x) = \mu(x)f'(x) + \frac{1}{2}\sigma^2(x)f''(x)$$

### Derivation via Itô's Lemma

!!! warning "Regularity Assumptions"
    Requires $f \in C^2(\mathbb{R})$, the SDE to have a strong solution, and
    $\mathbb{E}\left[\int_{t_0}^{t_0+h} |f'(X_s)|^2 \sigma^2(X_s, s) \, ds\right] < \infty$
    so the Itô integral is a martingale.

Apply Itô's lemma to $f(X_t)$:

$$
df(X_t) = \underbrace{\left[\mu f'(X_t) + \frac{1}{2}\sigma^2 f''(X_t)\right]}_{(\mathcal{L}_t f)(X_t)}dt + f'(X_t)\sigma(X_t, t)\,dW_t
$$

Taking expectations (the Itô integral has zero mean):

$$
\frac{d}{dh}\mathbb{E}[f(X_{t_0+h}) \mid X_{t_0} = x_0]\Big|_{h=0} = (\mathcal{L}_{t_0} f)(x_0)
$$

---

## Extended Generator for Time-Dependent Functions

For $f(x, t)$ depending explicitly on both space and time:

!!! abstract "Definition (Extended Generator)"
    For $f \in C^{2,1}$ (twice in $x$, once in $t$):

    $$
    \boxed{
    (\tilde{\mathcal{L}} f)(x, t) = \frac{\partial f}{\partial t}(x, t) + (\mathcal{L}_t f)(x, t) = \frac{\partial f}{\partial t} + \mu\frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 f}{\partial x^2}
    }
    $$

The extended generator appears in:

- **Feynman–Kac formula**: The PDE $\tilde{\mathcal{L}} u - r u = 0$ connects to discounted expectations
- **Kolmogorov backward equation**: Written compactly as $\tilde{\mathcal{L}} u = 0$

See [Feynman–Kac Formula](../../ch05/feynman_kac/feynman_kac_formula.md).

---

## Multidimensional Generator

For a $d$-dimensional diffusion driven by $m$ independent Brownian motions, $dX_t^i = \mu^i(X_t, t)\,dt + \sum_{\alpha=1}^{m}\sigma^{i\alpha}(X_t, t)\,dW_t^\alpha$:

$$
\boxed{
(\mathcal{L}_t f)(x) = \sum_{i=1}^d \mu^i(x, t)\frac{\partial f}{\partial x_i} + \frac{1}{2}\sum_{i,j=1}^d a^{ij}(x, t)\frac{\partial^2 f}{\partial x_i \partial x_j}
}
$$

where the **diffusion matrix** $a^{ij} = (\sigma \sigma^\top)^{ij} = \sum_{\alpha}\sigma^{i\alpha}\sigma^{j\alpha}$.

---

## Examples (Time-Homogeneous)

### Brownian Motion

For $dX_t = dW_t$ ($\mu = 0$, $\sigma = 1$):

$$
\mathcal{L} = \frac{1}{2}\frac{d^2}{dx^2}
$$

This is half the Laplacian. Setting $u(x,t) = \mathbb{E}_x[f(X_t)]$, Dynkin's formula gives $\partial_t u = \mathcal{L}u = \frac{1}{2}\partial_{xx}u$ — exactly the heat equation. The generator is thus the spatial operator in the heat equation. See [Fokker–Planck Equation](../../ch05/kolmogorov_equations/kolmogorov_forward.md).

??? example "Worked Example: $\mathcal{L}f$ for $f(x) = x^2$"

    - $f'(x) = 2x$, $f''(x) = 2$

    $$(\mathcal{L}f)(x) = 0 \cdot 2x + \frac{1}{2} \cdot 2 = 1$$

    So $\mathbb{E}_x[X_t^2] = x^2 + t$ — reflecting the linear variance growth of BM. $\square$

### Brownian Motion with Drift

For $dX_t = \mu\,dt + \sigma\,dW_t$ (constant coefficients):

$$
\mathcal{L} = \mu\frac{d}{dx} + \frac{\sigma^2}{2}\frac{d^2}{dx^2}
$$

??? example "Worked Example: $\mathcal{L}f$ for $f(x) = e^{\theta x}$"

    $$(\mathcal{L}f)(x) = \mu \theta e^{\theta x} + \frac{\sigma^2}{2}\theta^2 e^{\theta x} = \left(\mu\theta + \frac{\sigma^2\theta^2}{2}\right)e^{\theta x}$$

    So $\frac{d}{dt}\mathbb{E}[e^{\theta X_t}] = \left(\mu\theta + \frac{\sigma^2\theta^2}{2}\right)\mathbb{E}[e^{\theta X_t}]$, recovering the cumulant generating function $\log\mathbb{E}[e^{\theta X_t}] = \left(\mu\theta + \frac{\sigma^2\theta^2}{2}\right)t$. $\square$

### Ornstein–Uhlenbeck Process

For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$:

$$
\mathcal{L} = -\kappa x\frac{d}{dx} + \frac{\sigma^2}{2}\frac{d^2}{dx^2}
$$

??? example "Worked Example: $\mathcal{L}f$ for $f(x) = x^2$"

    - $f'(x) = 2x$, $f''(x) = 2$

    $$(\mathcal{L}f)(x) = -\kappa x \cdot 2x + \frac{\sigma^2}{2} \cdot 2 = -2\kappa x^2 + \sigma^2$$

    **Verification**: Dynkin's formula gives $\mathbb{E}[X_h^2 \mid X_0 = x_0] \approx x_0^2 + h(-2\kappa x_0^2 + \sigma^2)$, which matches the exact formula $x_0^2 e^{-2\kappa h} + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa h})$ to first order in $h$. $\square$

### Geometric Brownian Motion

For $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ on $(0,\infty)$:

$$
\mathcal{L} = \mu S\frac{d}{dS} + \frac{\sigma^2 S^2}{2}\frac{d^2}{dS^2}
$$

!!! note "Domain Restriction"
    GBM lives on $(0,\infty)$. Functions in $\mathrm{Dom}(\mathcal{L})$ must satisfy appropriate boundary conditions as $S \to 0^+$ and $S \to \infty$. For option pricing, payoff functions such as $(S-K)^+$ are not in $C^2$ and require extra care.

??? example "Worked Example: $\mathcal{L}f$ for $f(s) = s$"

    $$(\mathcal{L}f)(s) = \mu s \cdot 1 + \frac{\sigma^2 s^2}{2} \cdot 0 = \mu s$$

    So $\frac{d}{dt}\mathbb{E}[S_t] = \mu\mathbb{E}[S_t]$, confirming $\mathbb{E}[S_t] = s_0 e^{\mu t}$. $\square$

---

## Domain Considerations

The generator is only defined for functions where the limit exists. Typical function spaces:

| Space | Notation | Description |
|-------|----------|-------------|
| Smooth compact support | $C_c^\infty(\mathbb{R}^d)$ | Infinitely differentiable, zero outside compact set |
| Vanishing at infinity | $C_0^2(\mathbb{R}^d)$ | Twice differentiable, $f(x) \to 0$ as $\|x\| \to \infty$ |
| Schwartz space | $\mathcal{S}(\mathbb{R}^d)$ | Rapidly decreasing with all derivatives |

!!! warning "Boundary and Growth Conditions"
    The precise domain depends on boundary behavior (reflection, absorption, killing), coefficient degeneracy ($\sigma(x) \to 0$), and growth conditions at infinity. For example, the generator of reflecting BM on $[0, \infty)$ requires $f'(0) = 0$.

---

## Transition Operators

The generator describes **local** (infinitesimal) dynamics; the **transition operator** describes **global** (finite-time) evolution.

!!! abstract "Definition (Transition Operator)"

    $$(P_{t_0, t} f)(x_0) = \mathbb{E}[f(X_t) \mid X_{t_0} = x_0]$$

The generator is the infinitesimal version: $(\mathcal{L}_{t_0} f)(x_0) = \lim_{h \downarrow 0} \frac{(P_{t_0, t_0+h} f)(x_0) - f(x_0)}{h}$.

The transition operators satisfy the **Chapman–Kolmogorov equation**: for $t_0 < s < t$,

$$P_{t_0, t} = P_{s, t} \circ P_{t_0, s}$$

This is the Markov property in operator form. In the time-homogeneous case: $P_{h_1 + h_2} = P_{h_1} \circ P_{h_2}$.

---

## Key Properties

### 1. Linearity

$$\mathcal{L}(\alpha f + \beta g) = \alpha \mathcal{L}f + \beta \mathcal{L}g$$

### 2. Maximum Principle (Diffusions Only)

For diffusion generators (no jumps), if $f$ attains a maximum at $x^*$:

$$(\mathcal{L}f)(x^*) \leq 0$$

??? abstract "Proof"

    At a maximum, $f'(x^*) = 0$ and $f''(x^*) \leq 0$:

    $$(\mathcal{L}f)(x^*) = \mu(x^*) \cdot 0 + \frac{1}{2}\sigma^2(x^*) \cdot f''(x^*) \leq 0 \qquad \square$$

!!! warning "Failure for Jump Processes"
    For processes with jumps, the integral term $\int [f(x+y) - f(x) - yf'(x)\mathbf{1}_{|y|<1}]\nu(dy)$ can be positive at a maximum of $f$, violating the principle.

### 3. Characterizes the Process

Under mild regularity conditions, the generator **uniquely determines** the law of the process (Stroock–Varadhan martingale problem). See [Martingale Problem](../diffusion_process/martingale_problem_stroock_varadhan.md).

---

## The Generator and Martingales

!!! abstract "Theorem (Dynkin's Martingale)"
    For $f \in C^2$ with appropriate integrability, the process

    $$M_t^f := f(X_t) - f(X_{t_0}) - \int_{t_0}^t (\mathcal{L}_s f)(X_s)\,ds$$

    is a martingale.

**Proof**: By Itô's lemma, $M_t^f = \int_{t_0}^t f'(X_s)\sigma(X_s,s)\,dW_s$, which is a martingale under the integrability condition. $\square$

A function $f$ is **$\mathcal{L}$-harmonic** if $\mathcal{L}f = 0$, which implies $f(X_t)$ is a local martingale.

See [Generator and Martingales](generator_and_martingales.md) for the full development.

---

## Connection to PDEs

| PDE | Formula | Probabilistic meaning |
|-----|---------|----------------------|
| Kolmogorov backward | $\partial_{t_0} u + \mathcal{L}_{t_0} u = 0$, $u(x_0,T) = g(x_0)$ | $u(x_0,t_0) = \mathbb{E}[g(X_T) \mid X_{t_0}=x_0]$ |
| Fokker–Planck | $\partial_t p = \mathcal{L}^*_t p$ | Density evolution |
| Feynman–Kac | $\tilde{\mathcal{L}} u - r u = 0$ | Discounted expectation |

The **adjoint generator** $\mathcal{L}^*_t$ governs density evolution:

$$\mathcal{L}^*_t f = -\frac{\partial}{\partial x}[\mu(x, t) f] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x, t) f]$$

See [Fokker–Planck Equation](../../ch05/kolmogorov_equations/kolmogorov_forward.md) for the full derivation.

---

## Summary

| Object | Definition | Role |
|--------|------------|------|
| Generator $\mathcal{L}_t$ | $\lim_{h \downarrow 0} \frac{(P_{t_0,t_0+h}f)(x_0) - f(x_0)}{h}$ | Local (infinitesimal) dynamics |
| Extended generator $\tilde{\mathcal{L}}$ | $\partial_t + \mathcal{L}_t$ | Time-dependent functions |
| Transition operator $P_{t_0, t}$ | $\mathbb{E}[f(X_t) \mid X_{t_0} = x_0]$ | Global (finite-time) evolution |
| Adjoint $\mathcal{L}^*_t$ | Defined by duality | Density evolution (Fokker–Planck) |

$$
\boxed{
\mathcal{L}_t = \mu(x, t)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x, t)\frac{\partial^2}{\partial x^2}
}
$$

**The infinitesimal generator is the bridge between stochastic processes (SDEs) and partial differential equations (PDEs).**

??? abstract "Quick Reference: Key Formulas"

    **1D Generator**: $\mathcal{L}_t f = \mu(x,t) f'(x) + \frac{\sigma^2(x,t)}{2} f''(x)$

    **Extended Generator**: $\tilde{\mathcal{L}} f = \partial_t f + \mathcal{L}_t f$

    **Multi-D Generator**: $\mathcal{L}_t f = \sum_i \mu^i \partial_i f + \frac{1}{2}\sum_{i,j} a^{ij} \partial_i \partial_j f$

    **Adjoint**: $\mathcal{L}^*_t f = -\partial_x[\mu f] + \frac{1}{2}\partial_x^2[\sigma^2 f]$

    **Dynkin's Martingale**: $M_t = f(X_t) - f(X_0) - \int_0^t (\mathcal{L}_s f)(X_s) \, ds$

    **Kolmogorov Backward**: $\partial_{t_0} u + \mathcal{L}_{t_0} u = 0$

    **Fokker–Planck**: $\partial_t p = \mathcal{L}^*_t p$

---

## See Also

- [Dynkin's Formula](dynkin_formula.md) — integral form connecting generator to expectations
- [Generator and Martingales](generator_and_martingales.md) — martingale characterization
- [Fokker–Planck Equation](../../ch05/kolmogorov_equations/kolmogorov_forward.md) — forward equation using $\mathcal{L}^*$
- [Kolmogorov Backward Equation](../../ch05/kolmogorov_equations/kolmogorov_backward.md) — backward equation using $\mathcal{L}$
- [Feynman–Kac Formula](../../ch05/feynman_kac/feynman_kac_formula.md) — discounted expectations
- [Martingale Problem](../diffusion_process/martingale_problem_stroock_varadhan.md) — characterization via generator

---

## Exercises

**Exercise 1.** Let $dX_t = 3X_t\,dt + 2X_t\,dW_t$ (geometric Brownian motion with $\mu = 3$, $\sigma = 2$). Write down the infinitesimal generator $\mathcal{L}$ and compute $\mathcal{L}f$ for $f(x) = x^2$.

??? success "Solution to Exercise 1"
    The SDE is $dX_t = 3X_t\,dt + 2X_t\,dW_t$, so $\mu(x) = 3x$ and $\sigma(x) = 2x$. The generator is:

    $$
    \mathcal{L}f(x) = \mu(x)f'(x) + \frac{1}{2}\sigma^2(x)f''(x) = 3x\,f'(x) + \frac{1}{2}(2x)^2 f''(x) = 3x\,f'(x) + 2x^2 f''(x)
    $$

    For $f(x) = x^2$, we have $f'(x) = 2x$ and $f''(x) = 2$:

    $$
    \mathcal{L}f(x) = 3x \cdot 2x + 2x^2 \cdot 2 = 6x^2 + 4x^2 = 10x^2
    $$

    This means $\frac{d}{dt}\mathbb{E}[X_t^2 \mid X_0 = x] = 10\,\mathbb{E}[X_t^2 \mid X_0 = x]$, so $\mathbb{E}[X_t^2] = x^2 e^{10t}$.

---

**Exercise 2.** For the Ornstein--Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, compute $\mathcal{L}f$ for $f(x) = e^{\alpha x}$ where $\alpha$ is a constant. Use the result to find an ODE for $m(t) = \mathbb{E}_x[e^{\alpha X_t}]$ by applying the generator to the moment generating function.

??? success "Solution to Exercise 2"
    The OU generator is $\mathcal{L}f = -\kappa x\,f'(x) + \frac{\sigma^2}{2}f''(x)$. For $f(x) = e^{\alpha x}$:

    - $f'(x) = \alpha e^{\alpha x}$, $f''(x) = \alpha^2 e^{\alpha x}$

    $$
    \mathcal{L}f(x) = -\kappa x \cdot \alpha e^{\alpha x} + \frac{\sigma^2}{2}\alpha^2 e^{\alpha x} = \left(-\kappa \alpha x + \frac{\sigma^2 \alpha^2}{2}\right)e^{\alpha x}
    $$

    Now set $m(t) = \mathbb{E}_x[e^{\alpha X_t}]$. By Dynkin's formula:

    $$
    m(t) = e^{\alpha x} + \int_0^t \mathbb{E}_x\!\left[\left(-\kappa \alpha X_s + \frac{\sigma^2 \alpha^2}{2}\right)e^{\alpha X_s}\right]ds
    $$

    Differentiating:

    $$
    m'(t) = -\kappa \alpha\,\mathbb{E}_x[X_t\,e^{\alpha X_t}] + \frac{\sigma^2 \alpha^2}{2}m(t)
    $$

    Note that $\mathbb{E}_x[X_t\,e^{\alpha X_t}] = \frac{\partial}{\partial \alpha}m(t)$, so:

    $$
    m'(t) = -\kappa \alpha \frac{\partial m}{\partial \alpha}(t) + \frac{\sigma^2 \alpha^2}{2}m(t)
    $$

    This is a PDE in $(\alpha, t)$ for the moment generating function. In the special case where we only want the ODE for the mean ($\alpha \to 0$), we differentiate $m(t)$ with respect to $\alpha$ and set $\alpha = 0$. Writing $\mu_1(t) = \mathbb{E}_x[X_t]$: differentiating the Dynkin integral equation with $f(x) = x$ (i.e., the $\alpha$-derivative at $\alpha = 0$) gives $\mu_1'(t) = -\kappa \mu_1(t)$, yielding $\mu_1(t) = x\,e^{-\kappa t}$.

---

**Exercise 3.** Consider the two-dimensional diffusion $(X_t, Y_t)$ driven by independent Brownian motions $W_t^1, W_t^2$:

$$
dX_t = Y_t\,dt + dW_t^1, \qquad dY_t = -X_t\,dt + dW_t^2
$$

Write down the multidimensional generator $\mathcal{L}$ and compute $\mathcal{L}f$ for $f(x,y) = x^2 + y^2$.

??? success "Solution to Exercise 3"
    The drift and diffusion coefficients are $\mu^1(x,y) = y$, $\mu^2(x,y) = -x$, $\sigma^{1,1} = 1$, $\sigma^{2,2} = 1$, with $\sigma^{1,2} = \sigma^{2,1} = 0$. The diffusion matrix is $a = \sigma\sigma^\top = I$ (the identity). The multidimensional generator is:

    $$
    \mathcal{L}f = y\frac{\partial f}{\partial x} - x\frac{\partial f}{\partial y} + \frac{1}{2}\frac{\partial^2 f}{\partial x^2} + \frac{1}{2}\frac{\partial^2 f}{\partial y^2}
    $$

    For $f(x,y) = x^2 + y^2$:

    - $\frac{\partial f}{\partial x} = 2x$, $\frac{\partial f}{\partial y} = 2y$
    - $\frac{\partial^2 f}{\partial x^2} = 2$, $\frac{\partial^2 f}{\partial y^2} = 2$

    $$
    \mathcal{L}f = y \cdot 2x + (-x) \cdot 2y + \frac{1}{2}\cdot 2 + \frac{1}{2}\cdot 2 = 2xy - 2xy + 1 + 1 = 2
    $$

    By Dynkin's formula, $\mathbb{E}[X_t^2 + Y_t^2] = (x_0^2 + y_0^2) + 2t$, showing the radius squared grows linearly on average. The cross terms from the drift cancel exactly, and only the diffusion contributes.

---

**Exercise 4.** Prove that the maximum principle fails for jump processes. Specifically, let $X_t$ be a compound Poisson process with generator

$$
(\mathcal{L}f)(x) = \lambda \int_{\mathbb{R}} [f(x+y) - f(x)]\,\nu(dy)
$$

where $\nu$ is a probability measure on $\mathbb{R}$. Find a function $f$ that attains a maximum at $x^*$ yet $(\mathcal{L}f)(x^*) > 0$. (Hint: try $f(x) = -x^2$ and a suitable $\nu$.)

??? success "Solution to Exercise 4"
    Let $f(x) = -x^2$. This function attains a global maximum at $x^* = 0$ with $f(0) = 0$. For $x \neq 0$, $f(x) < 0$.

    The generator of the compound Poisson process gives:

    $$
    (\mathcal{L}f)(0) = \lambda \int_{\mathbb{R}} [f(0+y) - f(0)]\,\nu(dy) = \lambda \int_{\mathbb{R}} (-y^2)\,\nu(dy) = -\lambda\int_{\mathbb{R}} y^2\,\nu(dy)
    $$

    Wait — this is $-\lambda \mathbb{E}_\nu[Y^2] \leq 0$, so the maximum principle actually holds for this choice. We need a different construction.

    Instead, let $\nu = \delta_0$ (point mass at zero — the trivial case where jumps have size zero). Then $(\mathcal{L}f)(x^*) = \lambda[f(x^*) - f(x^*)] = 0$, which does not violate the principle.

    The correct approach: take $f(x) = -(x-1)^2$, which has a maximum at $x^* = 1$ with $f(1) = 0$. Choose $\nu = \delta_{-1}$ (all jumps of size $-1$):

    $$
    (\mathcal{L}f)(1) = \lambda[f(1 + (-1)) - f(1)] = \lambda[f(0) - f(1)] = \lambda[-(0-1)^2 - 0] = -\lambda < 0
    $$

    This still does not violate. Let us try more carefully. Take $f(x) = \mathbf{1}_{x=0}$ — but this is not smooth. We need a smooth function.

    Take $f(x) = e^{-x^2}$, which has a maximum at $x^* = 0$ with $f(0) = 1$. Let $\nu = \frac{1}{2}\delta_{-\epsilon} + \frac{1}{2}\delta_{\epsilon}$ for small $\epsilon > 0$:

    $$
    (\mathcal{L}f)(0) = \lambda\left[\frac{1}{2}f(-\epsilon) + \frac{1}{2}f(\epsilon) - f(0)\right] = \lambda\left[e^{-\epsilon^2} - 1\right] < 0
    $$

    This is still negative. In fact, for **any** function with a strict maximum, $f(x^* + y) \leq f(x^*)$ for all $y$, so $\int [f(x^*+y) - f(x^*)]\,\nu(dy) \leq 0$. If $f$ has a **global** maximum, the principle holds even for jump processes.

    The maximum principle for diffusions states: if $f$ has a **local interior** maximum at $x^*$ in a domain $D$, then $\mathcal{L}f(x^*) \leq 0$. For jump processes, this fails because jumps can reach outside the local neighborhood. Consider $f$ defined on $\mathbb{R}$ by:

    $$
    f(x) = \begin{cases} 1 - x^2 & |x| \leq 1 \\ 2e^{-(x-2)^2} & x > 1 \\ 0 & x < -1 \end{cases}
    $$

    smoothly interpolated, with a local maximum at $x^* = 0$ where $f(0) = 1$, and a global maximum at $x = 2$ where $f(2) = 2$. Now take $\nu = \delta_2$ (jumps of size $2$):

    $$
    (\mathcal{L}f)(0) = \lambda[f(2) - f(0)] = \lambda[2 - 1] = \lambda > 0
    $$

    This violates the maximum principle: $f$ has a local maximum at $x^* = 0$, but $(\mathcal{L}f)(0) = \lambda > 0$. The jump process can "see" the higher value at $x = 2$, which a diffusion (being continuous) cannot reach instantly.

---

**Exercise 5.** For standard Brownian motion ($\mathcal{L} = \frac{1}{2}\frac{d^2}{dx^2}$), determine which of the following functions belong to the domain of the generator by computing $\mathcal{L}f$ and checking whether the result is well-defined:

(a) $f(x) = |x|$

(b) $f(x) = x^3$

(c) $f(x) = \sin(x)$

(d) $f(x) = (x - 1)^+$

??? success "Solution to Exercise 5"
    The generator of BM is $\mathcal{L}f = \frac{1}{2}f''$.

    **(a)** $f(x) = |x|$. This function is not differentiable at $x = 0$, so $f \notin C^2(\mathbb{R})$. At $x \neq 0$, $f''(x) = 0$, so $\mathcal{L}f(x) = 0$ away from the origin. However, $f''$ does not exist at $x = 0$ (as a classical derivative), so $f \notin \mathrm{Dom}(\mathcal{L})$ in the classical sense.

    **(b)** $f(x) = x^3$. We have $f'(x) = 3x^2$ and $f''(x) = 6x$, both well-defined and continuous. Thus:

    $$
    \mathcal{L}f(x) = \frac{1}{2}\cdot 6x = 3x
    $$

    This is well-defined for all $x$, so $f \in \mathrm{Dom}(\mathcal{L})$.

    **(c)** $f(x) = \sin(x)$. We have $f''(x) = -\sin(x)$, which is smooth and bounded. Thus:

    $$
    \mathcal{L}f(x) = -\frac{1}{2}\sin(x)
    $$

    This is well-defined for all $x$, so $f \in \mathrm{Dom}(\mathcal{L})$.

    **(d)** $f(x) = (x-1)^+ = \max(x-1, 0)$. This function has a kink at $x = 1$: $f'$ has a jump discontinuity at $x = 1$ and $f''$ does not exist there (in the classical sense). So $f \notin C^2(\mathbb{R})$ and $f \notin \mathrm{Dom}(\mathcal{L})$ classically. This is the call option payoff, illustrating why option pricing requires regularization or weak solutions.

---

**Exercise 6.** Consider the extended generator $\tilde{\mathcal{L}} = \partial_t + \mathcal{L}_t$ for a diffusion $dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t$. Show that if $V(x,t)$ satisfies the Black--Scholes PDE

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

then $\tilde{\mathcal{L}}V - rV = 0$, where $\mathcal{L}$ is the generator of geometric Brownian motion under the risk-neutral measure ($\mu = r$). Explain why this means $e^{-rt}V(S_t, t)$ is a martingale.

??? success "Solution to Exercise 6"
    Under the risk-neutral measure, $dS_t = rS_t\,dt + \sigma S_t\,dW_t$, so the generator of GBM is:

    $$
    \mathcal{L}f = rS\frac{\partial f}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 f}{\partial S^2}
    $$

    The extended generator is $\tilde{\mathcal{L}}f = \frac{\partial f}{\partial t} + \mathcal{L}f$. For $V(S,t)$:

    $$
    \tilde{\mathcal{L}}V = \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2}
    $$

    The Black--Scholes PDE states exactly that this expression equals $rV$:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} = rV
    $$

    Therefore $\tilde{\mathcal{L}}V - rV = 0$.

    To see why $e^{-rt}V(S_t, t)$ is a martingale, apply Ito's lemma to $g(S,t) = e^{-rt}V(S,t)$:

    $$
    dg = e^{-rt}\!\left[-rV\,dt + \frac{\partial V}{\partial t}\,dt + rS\frac{\partial V}{\partial S}\,dt + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2}\,dt + \sigma S\frac{\partial V}{\partial S}\,dW_t\right]
    $$

    The $dt$ terms combine to $e^{-rt}(\tilde{\mathcal{L}}V - rV)\,dt = 0$ by the Black--Scholes PDE. The only surviving term is:

    $$
    dg = e^{-rt}\sigma S_t \frac{\partial V}{\partial S}(S_t, t)\,dW_t
    $$

    This is a (local) martingale since it is a stochastic integral with respect to $W_t$. Under appropriate integrability conditions (which hold for standard option payoffs), it is a true martingale. Therefore $e^{-rt}V(S_t, t)$ is a martingale, confirming the risk-neutral pricing formula $V(S_0, 0) = \mathbb{E}[e^{-rT}V(S_T, T)]$.

---

**Exercise 7.** Let $dX_t = \sigma(X_t)\,dW_t$ (a driftless diffusion with state-dependent volatility). Write down the generator $\mathcal{L}$ and show that every affine function $f(x) = ax + b$ satisfies $\mathcal{L}f = 0$. What does this imply about $f(X_t)$ as a stochastic process?

??? success "Solution to Exercise 7"
    The SDE is $dX_t = \sigma(X_t)\,dW_t$, so $\mu(x) = 0$ and the generator is:

    $$
    \mathcal{L}f(x) = 0 \cdot f'(x) + \frac{1}{2}\sigma^2(x)f''(x) = \frac{1}{2}\sigma^2(x)f''(x)
    $$

    For $f(x) = ax + b$, we have $f'(x) = a$ and $f''(x) = 0$. Therefore:

    $$
    \mathcal{L}f(x) = \frac{1}{2}\sigma^2(x) \cdot 0 = 0
    $$

    for any choice of $\sigma(x)$, confirming $f$ is $\mathcal{L}$-harmonic.

    Since $\mathcal{L}f = 0$, the Dynkin martingale becomes $M_t = f(X_t) - f(X_0) - 0 = f(X_t) - f(X_0)$. Therefore $f(X_t) = aX_t + b$ is a local martingale. In particular, $X_t$ itself (taking $a = 1$, $b = 0$) is a local martingale, which is expected since the SDE has zero drift. Under appropriate integrability conditions on $\sigma$, $X_t$ is a true martingale.
