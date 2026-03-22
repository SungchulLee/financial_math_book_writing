# Connection to Feynman-Kac

The Feynman-Kac theorem provides the bridge between probabilistic expectations and partial differential equations. For affine processes, this bridge has a remarkable consequence: the exponential-affine ansatz reduces the Feynman-Kac PDE to the Riccati ODE system, giving a complete and explicit connection between the probabilistic and analytical approaches to derivative pricing. This section develops the affine Feynman-Kac framework, derives the PDE, and shows how the ansatz produces the Riccati equations.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the Feynman-Kac theorem for discounted expectations
    2. Write the associated PDE for the discounted transform of an affine process
    3. Reduce the PDE to the Riccati system using the exponential-affine ansatz
    4. Verify the Feynman-Kac solution for the Black-Scholes model

---

## Intuition

Derivative pricing has two equivalent formulations. The *probabilistic* approach computes $V(t, x) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds}\,h(X_T) \mid X_t = x]$ as a conditional expectation. The *analytical* approach solves the PDE $\frac{\partial V}{\partial t} + \mathcal{A}V - rV = 0$ with terminal condition $V(T, x) = h(x)$. The Feynman-Kac theorem says these are the same object.

For general processes, solving the PDE numerically is expensive---finite difference or finite element methods scale poorly with dimension. For affine processes, the exponential-affine ansatz transforms the PDE into ODEs, collapsing the computational cost from exponential in $d$ to polynomial. This is why affine models dominate in multi-factor applications.

---

## The Feynman-Kac Theorem

### General Statement

**Theorem (Feynman-Kac).** Let $X_t$ be an Ito diffusion on $\mathbb{R}^d$ with generator

$$
\mathcal{A} = \sum_{i=1}^d b_i(x)\frac{\partial}{\partial x_i} + \frac{1}{2}\sum_{i,j=1}^d a_{ij}(x)\frac{\partial^2}{\partial x_i \partial x_j}
$$

Let $c : \mathbb{R}^d \to \mathbb{R}$ be a continuous function (the "killing rate") and $h : \mathbb{R}^d \to \mathbb{R}$ a measurable terminal condition. Define

$$
V(t, x) = \mathbb{E}\!\left[e^{-\int_t^T c(X_s)\,ds}\,h(X_T) \mid X_t = x\right]
$$

Under suitable regularity conditions (Lipschitz coefficients, polynomial growth of $h$), $V$ is the unique classical solution of the PDE:

$$
\frac{\partial V}{\partial t}(t, x) + \mathcal{A}V(t, x) - c(x)\,V(t, x) = 0, \qquad V(T, x) = h(x)
$$

The term $-c(x)V$ is the "killing" or "discounting" term. In finance, $c(x) = r(x)$ is the short rate, and $V$ is the time-$t$ value of a claim paying $h(X_T)$ at time $T$.

### Backward Formulation

Switching to time-to-maturity $\tau = T - t$:

$$
\frac{\partial V}{\partial \tau}(\tau, x) = \mathcal{A}V(\tau, x) - c(x)\,V(\tau, x), \qquad V(0, x) = h(x)
$$

This is the form most convenient for the Riccati derivation, since $\tau$ increases from the terminal condition.

---

## Affine Feynman-Kac PDE

### Setup for Affine Processes

For an affine process on $D = \mathbb{R}^m_+ \times \mathbb{R}^{d-m}$ with affine drift $b(x) = b_0 + \sum_j b_j x_j$, affine diffusion $a(x) = a_0 + \sum_j a_j x_j$, and affine killing rate $c(x) = \rho_0 + \langle \rho_1, x \rangle$, the Feynman-Kac PDE becomes:

$$
\frac{\partial V}{\partial \tau} = \sum_{i=1}^d \left(b_{0,i} + \sum_{j=1}^d b_{j,i}\,x_j\right)\frac{\partial V}{\partial x_i} + \frac{1}{2}\sum_{i,k=1}^d \left(a_{0,ik} + \sum_{j=1}^d a_{j,ik}\,x_j\right)\frac{\partial^2 V}{\partial x_i \partial x_k} - (\rho_0 + \langle \rho_1, x \rangle)\,V
$$

### Exponential-Affine Terminal Condition

For the discounted transform, the terminal condition is $h(x) = e^{\langle u, x \rangle}$. The PDE becomes:

$$
\frac{\partial V}{\partial \tau} = \mathcal{A}V - c(x)\,V, \qquad V(0, x) = e^{\langle u, x \rangle}
$$

---

## Reduction to the Riccati System

### The Ansatz

Motivated by the terminal condition, substitute $V(\tau, x) = \exp(\tilde{\phi}(\tau) + \langle \tilde{\psi}(\tau), x \rangle)$ with $\tilde{\phi}(0) = 0$ and $\tilde{\psi}(0) = u$.

Computing the derivatives:

$$
\frac{\partial V}{\partial \tau} = (\tilde{\phi}' + \langle \tilde{\psi}', x \rangle)\,V
$$

$$
\frac{\partial V}{\partial x_i} = \tilde{\psi}_i\,V, \qquad \frac{\partial^2 V}{\partial x_i \partial x_k} = \tilde{\psi}_i\,\tilde{\psi}_k\,V
$$

### Substitution

Substituting into the PDE and dividing by $V > 0$:

$$
\tilde{\phi}' + \langle \tilde{\psi}', x \rangle = \sum_i (b_{0,i} + \sum_j b_{j,i} x_j)\tilde{\psi}_i + \frac{1}{2}\sum_{i,k}(a_{0,ik} + \sum_j a_{j,ik} x_j)\tilde{\psi}_i\tilde{\psi}_k - \rho_0 - \langle \rho_1, x \rangle
$$

### Collecting Terms

Grouping by powers of $x$:

**Constant terms ($x^0$):**

$$
\tilde{\phi}'(\tau) = \langle b_0, \tilde{\psi} \rangle + \frac{1}{2}\langle \tilde{\psi}, a_0\tilde{\psi} \rangle - \rho_0 = F(\tilde{\psi}) - \rho_0
$$

**Linear terms (coefficient of $x_j$):**

$$
\tilde{\psi}_j'(\tau) = \langle b_j, \tilde{\psi} \rangle + \frac{1}{2}\langle \tilde{\psi}, a_j\tilde{\psi} \rangle - \rho_{1,j} = R_j(\tilde{\psi}) - \rho_{1,j}
$$

This recovers the extended Riccati system with discounting:

$$
\tilde{\phi}' = F(\tilde{\psi}) - \rho_0, \qquad \tilde{\psi}' = R(\tilde{\psi}) - \rho_1
$$

The Feynman-Kac PDE, which is a $(d+1)$-dimensional partial differential equation, has been reduced to a $(d+1)$-dimensional system of ordinary differential equations. For $d = 1$, this reduces the PDE to two scalar ODEs; for $d = 2$ (e.g., Heston), to three scalar ODEs.

---

## Verification for the Black-Scholes Model

### Setup

In the Black-Scholes model, $X_t = \log S_t$ with $dX_t = (r - \frac{1}{2}\sigma^2)\,dt + \sigma\,dW_t$ and $c(x) = r$ (constant short rate). The affine parameters are $b_0 = r - \frac{1}{2}\sigma^2$, $b_1 = 0$, $a_0 = \sigma^2$, $a_1 = 0$, $\rho_0 = r$, $\rho_1 = 0$.

### Riccati System

$$
\tilde{\psi}'(\tau) = 0, \qquad \tilde{\psi}(0) = u
$$

$$
\tilde{\phi}'(\tau) = (r - \tfrac{1}{2}\sigma^2)\tilde{\psi} + \tfrac{1}{2}\sigma^2\tilde{\psi}^2 - r, \qquad \tilde{\phi}(0) = 0
$$

### Solution

$\tilde{\psi}(\tau) = u$ (constant), and:

$$
\tilde{\phi}(\tau) = \left[(r - \tfrac{1}{2}\sigma^2)u + \tfrac{1}{2}\sigma^2 u^2 - r\right]\tau
$$

### The Discounted Characteristic Function

Setting $u = iv$:

$$
\tilde{\phi}(\tau, iv) = \left[(r - \tfrac{1}{2}\sigma^2)iv - \tfrac{1}{2}\sigma^2 v^2 - r\right]\tau
$$

$$
\tilde{\psi}(\tau, iv) = iv
$$

The discounted characteristic function is:

$$
\mathbb{E}\!\left[e^{-r\tau + iv\log S_T} \mid \log S_t = x\right] = \exp\!\left(\left[(r - \tfrac{1}{2}\sigma^2)iv - \tfrac{1}{2}\sigma^2 v^2 - r\right]\tau + ivx\right)
$$

This is the standard Black-Scholes result: under $\mathbb{Q}$, $\log S_T \sim N(x + (r - \frac{1}{2}\sigma^2)\tau, \sigma^2\tau)$, and the discount factor contributes $e^{-r\tau}$.

---

## General Payoffs via Fourier Inversion

The Feynman-Kac framework handles not only exponential payoffs $h(x) = e^{\langle u, x \rangle}$ but also general payoffs through the Fourier representation:

$$
V(t, x) = \mathbb{E}\!\left[e^{-\int_t^T r_s\,ds}\,h(X_T) \mid X_t = x\right]
$$

If $h$ has a Fourier transform $\hat{h}(v) = \int e^{ivx}h(x)\,dx$, then:

$$
V(t, x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} \hat{h}(v)\,\mathcal{T}(\tau, -iv, x)\,dv
$$

where $\mathcal{T}$ is the discounted transform. Since $\mathcal{T}$ has exponential-affine form, the only numerical step is evaluating the Fourier integral.

!!! note "PDE vs ODE Dimensionality"
    The Feynman-Kac PDE is $(d+1)$-dimensional (time plus $d$ spatial dimensions). Finite difference methods have cost $O(N^d)$ where $N$ is the grid size per dimension. The affine Riccati approach replaces this with a system of $d+1$ ODEs, each one-dimensional. For $d = 5$ (a five-factor model), the PDE approach is computationally prohibitive, while the ODE approach remains trivial. This dimensional reduction is the fundamental reason affine models are preferred for multi-factor applications.

---

## Summary

The Feynman-Kac theorem connects the discounted conditional expectation $V(t, x) = \mathbb{E}[e^{-\int_t^T c(X_s)\,ds}\,h(X_T) \mid X_t = x]$ to the PDE $\partial_t V + \mathcal{A}V - cV = 0$. For affine processes with exponential terminal conditions, the exponential-affine ansatz reduces this PDE to the extended Riccati system $\tilde{\phi}' = F(\tilde{\psi}) - \rho_0$, $\tilde{\psi}' = R(\tilde{\psi}) - \rho_1$. This reduction from PDE to ODE is the core computational advantage of the affine framework, and it extends to general payoffs through Fourier inversion of the discounted characteristic function.

---

## Further Reading

- Duffie, D., Pan, J., & Singleton, K. (2000). "Transform Analysis and Asset Pricing for Affine Jump-Diffusions." *Econometrica*, 68(6), 1343-1376.
- Karatzas, I. & Shreve, S. E. *Brownian Motion and Stochastic Calculus*. Springer, 1991, Section 4.4.
- Filipovic, D. *Term-Structure Models: A Graduate Course*. Springer, 2009.
