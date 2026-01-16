# The Infinitesimal Generator

The **infinitesimal generator** is the fundamental object that characterizes a Markov process. It captures the local dynamics of the process and connects stochastic differential equations to partial differential equations. Understanding generators is essential for Dynkin's formula, Kolmogorov equations, the Feynman-Kac formula, and the martingale problem.

---

## Motivation

Consider a diffusion process $X_t$ and a smooth function $f$. We want to understand how $\mathbb{E}_x[f(X_t)]$ changes with time, starting from $X_0 = x$.

**Key question**: What is the instantaneous rate of change?

$$
\lim_{t \to 0} \frac{\mathbb{E}_x[f(X_t)] - f(x)}{t} = \, ?
$$

The answer is the **generator** acting on $f$.

---

## Definition

Let $X_t$ be a Markov process on $\mathbb{R}^d$.

**Definition**: The **infinitesimal generator** $\mathcal{L}$ is the operator defined by:

$$
\boxed{
(\mathcal{L}f)(x) := \lim_{t \downarrow 0} \frac{\mathbb{E}_x[f(X_t)] - f(x)}{t}
}
$$

for functions $f$ in the **domain** of $\mathcal{L}$:

$$
\text{Dom}(\mathcal{L}) = \left\{ f : \lim_{t \downarrow 0} \frac{\mathbb{E}_x[f(X_t)] - f(x)}{t} \text{ exists for all } x \right\}
$$

**Interpretation**: $(\mathcal{L}f)(x)$ is the **instantaneous expected rate of change** of $f$ at position $x$.

---

## Generator of a Diffusion Process

For a diffusion process solving the SDE:

$$
dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t
$$

the generator is:

$$
\boxed{
(\mathcal{L}f)(x) = \mu(x)f'(x) + \frac{1}{2}\sigma^2(x)f''(x)
}
$$

### Derivation via Itô's Lemma

Apply Itô's lemma to $f(X_t)$:

$$
df(X_t) = f'(X_t)\,dX_t + \frac{1}{2}f''(X_t)(dX_t)^2
$$

$$
= f'(X_t)[\mu(X_t)\,dt + \sigma(X_t)\,dW_t] + \frac{1}{2}f''(X_t)\sigma^2(X_t)\,dt
$$

$$
= \left[\mu(X_t)f'(X_t) + \frac{1}{2}\sigma^2(X_t)f''(X_t)\right]dt + f'(X_t)\sigma(X_t)\,dW_t
$$

Taking expectations (the Itô integral has zero expectation):

$$
\frac{d}{dt}\mathbb{E}_x[f(X_t)] = \mathbb{E}_x[\mathcal{L}f(X_t)]
$$

At $t = 0$:

$$
\lim_{t \to 0} \frac{\mathbb{E}_x[f(X_t)] - f(x)}{t} = (\mathcal{L}f)(x)
$$

---

## Multidimensional Generator

For a $d$-dimensional diffusion:

$$
dX_t^i = \mu^i(X_t)\,dt + \sigma^{i\alpha}(X_t)\,dW_t^\alpha
$$

the generator is:

$$
\boxed{
(\mathcal{L}f)(x) = \mu^i(x)\frac{\partial f}{\partial x_i}(x) + \frac{1}{2}a^{ij}(x)\frac{\partial^2 f}{\partial x_i \partial x_j}(x)
}
$$

where $a^{ij} = \sigma^{i\alpha}\sigma^{j\alpha}$ is the diffusion matrix.

**In vector notation**:

$$
\mathcal{L}f = \mu \cdot \nabla f + \frac{1}{2}\text{tr}(a \cdot \nabla^2 f)
$$

---

## Examples

### Example 1: Brownian Motion

For $dX_t = dW_t$ (i.e., $\mu = 0$, $\sigma = 1$):

$$
\mathcal{L} = \frac{1}{2}\frac{d^2}{dx^2}
$$

This is the **Laplacian** (up to a factor of 2), explaining the connection between Brownian motion and the heat equation.

### Example 2: Brownian Motion with Drift

For $dX_t = \mu\,dt + \sigma\,dW_t$ (constant coefficients):

$$
\mathcal{L} = \mu\frac{d}{dx} + \frac{\sigma^2}{2}\frac{d^2}{dx^2}
$$

### Example 3: Ornstein-Uhlenbeck Process

For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$:

$$
\mathcal{L} = -\kappa x\frac{d}{dx} + \frac{\sigma^2}{2}\frac{d^2}{dx^2}
$$

### Example 4: Geometric Brownian Motion

For $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$:

$$
\mathcal{L} = \mu x\frac{d}{dx} + \frac{\sigma^2 x^2}{2}\frac{d^2}{dx^2}
$$

---

## The Semigroup and Generator

The generator is intimately connected to the **transition semigroup** $P_t$:

$$
(P_t f)(x) = \mathbb{E}_x[f(X_t)]
$$

**Semigroup property**: $P_{t+s} = P_t \circ P_s$

**Generator as derivative**:

$$
\mathcal{L} = \lim_{t \to 0} \frac{P_t - I}{t} = \frac{d}{dt}\Big|_{t=0} P_t
$$

**Exponential relationship** (formal):

$$
P_t = e^{t\mathcal{L}}
$$

This means:

$$
\mathbb{E}_x[f(X_t)] = (e^{t\mathcal{L}}f)(x) = f(x) + t(\mathcal{L}f)(x) + \frac{t^2}{2}(\mathcal{L}^2 f)(x) + \cdots
$$

---

## Key Properties

### 1. Linearity

$$
\mathcal{L}(\alpha f + \beta g) = \alpha \mathcal{L}f + \beta \mathcal{L}g
$$

### 2. Maximum Principle

If $f$ attains a maximum at $x_0$ and $f \in \text{Dom}(\mathcal{L})$:

$$
(\mathcal{L}f)(x_0) \leq 0
$$

**Proof**: At a maximum, $f'(x_0) = 0$ and $f''(x_0) \leq 0$. Therefore:

$$
(\mathcal{L}f)(x_0) = \mu(x_0) \cdot 0 + \frac{1}{2}\sigma^2(x_0) \cdot f''(x_0) \leq 0
$$

### 3. Characterizes the Process

Under mild regularity conditions, the generator **uniquely determines** the law of the process. This is the basis of the martingale problem approach.

---

## The Generator and Martingales

**Fundamental result**: For $f \in \text{Dom}(\mathcal{L})$, the process:

$$
M_t^f := f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,ds
$$

is a **martingale**.

**Proof**: This follows directly from Itô's lemma and the fact that the Itô integral is a martingale.

### Harmonic Functions

A function $f$ is **harmonic** for $X_t$ if:

$$
\mathcal{L}f = 0
$$

**Consequence**: If $\mathcal{L}f = 0$, then $f(X_t)$ is a martingale.

---

## Connection to PDEs

### Kolmogorov Backward Equation

The function $u(t, x) = \mathbb{E}_x[g(X_T) | X_t = x] = \mathbb{E}_x[g(X_{T-t})]$ satisfies:

$$
\frac{\partial u}{\partial t} + \mathcal{L}u = 0, \quad u(T, x) = g(x)
$$

### Kolmogorov Forward (Fokker-Planck) Equation

The transition density $p(t, x, y)$ satisfies:

$$
\frac{\partial p}{\partial t} = \mathcal{L}^*_y p
$$

where $\mathcal{L}^*$ is the **adjoint** of $\mathcal{L}$.

### Feynman-Kac Formula

The function:

$$
u(t, x) = \mathbb{E}_x\left[e^{-\int_t^T r(X_s)\,ds} g(X_T)\right]
$$

satisfies:

$$
\frac{\partial u}{\partial t} + \mathcal{L}u - ru = 0, \quad u(T, x) = g(x)
$$

---

## The Adjoint Generator

The **adjoint** $\mathcal{L}^*$ is defined by:

$$
\int f(x)(\mathcal{L}g)(x)\,dx = \int (\mathcal{L}^* f)(x)g(x)\,dx
$$

For a diffusion:

$$
\mathcal{L}^* f = -\frac{\partial}{\partial x}(\mu f) + \frac{1}{2}\frac{\partial^2}{\partial x^2}(\sigma^2 f)
$$

The adjoint appears in:
- Fokker-Planck equation
- Invariant measures: $\mathcal{L}^* \pi = 0$

---

## Domain Considerations

The generator is only defined on its **domain** $\text{Dom}(\mathcal{L})$.

**Typical domain**: $C_0^2(\mathbb{R}^d)$ (twice continuously differentiable functions vanishing at infinity) or $C_c^\infty(\mathbb{R}^d)$ (smooth compactly supported functions).

**Core**: A subset $D \subset \text{Dom}(\mathcal{L})$ is a **core** if $\mathcal{L}$ is uniquely determined by its values on $D$.

---

## Summary

| Object | Definition | Role |
|--------|------------|------|
| Generator $\mathcal{L}$ | $\lim_{t \to 0} \frac{\mathbb{E}_x[f(X_t)] - f(x)}{t}$ | Local dynamics |
| Semigroup $P_t$ | $\mathbb{E}_x[f(X_t)]$ | Global evolution |
| Adjoint $\mathcal{L}^*$ | Defined by duality | Density evolution |

$$
\boxed{
\mathcal{L} = \mu(x)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2}{\partial x^2}
}
$$

**The infinitesimal generator is the bridge between stochastic processes (SDEs) and partial differential equations (PDEs).**
