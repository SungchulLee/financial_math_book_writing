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

Recall (see [§ Feynman-Kac Formula](../../ch05/feynman_kac/feynman_kac_formula.md)): for an Ito diffusion with generator $\mathcal{A}$, continuous killing rate $c(x)$, and terminal payoff $h$, the function

$$
V(t, x) = \mathbb{E}\!\left[e^{-\int_t^T c(X_s)\,ds}\,h(X_T) \mid X_t = x\right]
$$

is the unique classical solution of $\partial_t V + \mathcal{A}V - c(x)V = 0$ with $V(T, x) = h(x)$. In finance, $c(x) = r(x)$ is the short rate. Switching to time-to-maturity $\tau = T - t$, the backward form is

$$
\frac{\partial V}{\partial \tau}(\tau, x) = \mathcal{A}V(\tau, x) - c(x)\,V(\tau, x), \qquad V(0, x) = h(x)
$$

which is most convenient for the Riccati derivation.

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

Recall (see [§ Discounted Characteristic Function](discounted_characteristic_function.md)): the BS Riccati system with $b_0 = r - \tfrac{1}{2}\sigma^2$, $a_0 = \sigma^2$, $\rho_0 = r$, $\rho_1 = 0$ yields $\tilde{\psi}(\tau) = u$ and $\tilde{\phi}(\tau) = [(r - \tfrac{1}{2}\sigma^2)u + \tfrac{1}{2}\sigma^2 u^2 - r]\tau$, recovering the standard discounted Gaussian characteristic function with $\log S_T \sim N(x + (r - \tfrac{1}{2}\sigma^2)\tau, \sigma^2\tau)$ under $\mathbb{Q}$.

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

---

## Exercises

**Exercise 1.** State the Feynman-Kac theorem for the function $V(t, x) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r(X_s)\,ds}\,h(X_T) \mid X_t = x]$. Write down the PDE that $V$ satisfies, including the terminal condition. For the Black-Scholes model with $h(x) = (e^x - K)^+$, identify the generator $\mathcal{A}$ and the discount rate $r$.

??? success "Solution to Exercise 1"
    **Feynman-Kac Theorem.** Let $X_t$ be an Ito diffusion with generator $\mathcal{A}$ and let $r(x)$ be the short rate. Define

    $$
    V(t, x) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(X_s)\,ds}\,h(X_T) \;\middle|\; X_t = x\right]
    $$

    Under suitable regularity conditions, $V$ is the unique classical solution of the PDE

    $$
    \frac{\partial V}{\partial t}(t, x) + \mathcal{A}V(t, x) - r(x)\,V(t, x) = 0, \qquad V(T, x) = h(x)
    $$

    For the Black-Scholes model with $X_t = \log S_t$, the dynamics are $dX_t = (r - \frac{1}{2}\sigma^2)\,dt + \sigma\,dW_t$. The generator is

    $$
    \mathcal{A} = (r - \tfrac{1}{2}\sigma^2)\frac{\partial}{\partial x} + \tfrac{1}{2}\sigma^2\frac{\partial^2}{\partial x^2}
    $$

    The discount rate is the constant $r(x) = r$, and the terminal condition for a call is $h(x) = (e^x - K)^+$. The Feynman-Kac PDE therefore reads

    $$
    \frac{\partial V}{\partial t} + (r - \tfrac{1}{2}\sigma^2)\frac{\partial V}{\partial x} + \tfrac{1}{2}\sigma^2\frac{\partial^2 V}{\partial x^2} - rV = 0, \qquad V(T, x) = (e^x - K)^+
    $$

---

**Exercise 2.** For a one-dimensional affine diffusion $dX_t = (\kappa_0 + \kappa_1 X_t)\,dt + \sqrt{\sigma_0 + \sigma_1 X_t}\,dW_t$ with short rate $r(x) = \rho_0 + \rho_1 x$, substitute the exponential-affine ansatz $V(\tau, x) = e^{\phi(\tau) + \psi(\tau)x}$ into the Feynman-Kac PDE $\frac{\partial V}{\partial \tau} = \mathcal{A}V - rV$ and derive the extended Riccati system by matching constant and linear terms in $x$.

??? success "Solution to Exercise 2"
    The generator for the one-dimensional affine diffusion is

    $$
    \mathcal{A} = (\kappa_0 + \kappa_1 x)\frac{\partial}{\partial x} + \frac{1}{2}(\sigma_0 + \sigma_1 x)\frac{\partial^2}{\partial x^2}
    $$

    With $r(x) = \rho_0 + \rho_1 x$, the Feynman-Kac PDE in backward time $\tau = T - t$ is

    $$
    \frac{\partial V}{\partial \tau} = (\kappa_0 + \kappa_1 x)\frac{\partial V}{\partial x} + \frac{1}{2}(\sigma_0 + \sigma_1 x)\frac{\partial^2 V}{\partial x^2} - (\rho_0 + \rho_1 x)V
    $$

    Substituting the ansatz $V = e^{\phi(\tau) + \psi(\tau)x}$, the derivatives are $\frac{\partial V}{\partial \tau} = (\phi' + \psi' x)V$, $\frac{\partial V}{\partial x} = \psi V$, and $\frac{\partial^2 V}{\partial x^2} = \psi^2 V$. Dividing through by $V > 0$:

    $$
    \phi' + \psi' x = (\kappa_0 + \kappa_1 x)\psi + \frac{1}{2}(\sigma_0 + \sigma_1 x)\psi^2 - \rho_0 - \rho_1 x
    $$

    **Constant terms ($x^0$):**

    $$
    \phi'(\tau) = \kappa_0 \psi + \frac{1}{2}\sigma_0 \psi^2 - \rho_0
    $$

    **Linear terms (coefficient of $x$):**

    $$
    \psi'(\tau) = \kappa_1 \psi + \frac{1}{2}\sigma_1 \psi^2 - \rho_1
    $$

    This is the extended Riccati system. The $\psi$-equation is a scalar Riccati ODE with constant term $-\rho_1$, linear term $\kappa_1$, and quadratic coefficient $\frac{1}{2}\sigma_1$. Once $\psi(\tau)$ is obtained, $\phi(\tau)$ is found by direct integration.

---

**Exercise 3.** Verify the Feynman-Kac solution for the Vasicek bond price. Starting from $V(\tau, x) = P(t, T) = e^{A(\tau) + B(\tau)x}$ with the Vasicek generator, show that $V$ satisfies $\frac{\partial V}{\partial \tau} = \kappa(\theta - x)\frac{\partial V}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 V}{\partial x^2} - xV$ by computing each derivative and substituting.

??? success "Solution to Exercise 3"
    For the Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$, the generator is $\mathcal{A} = \kappa(\theta - x)\frac{\partial}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2}{\partial x^2}$ and the killing rate is $c(x) = x$.

    With $V = e^{A(\tau) + B(\tau)x}$, compute each term:

    - $\frac{\partial V}{\partial \tau} = (A' + B' x)V$
    - $\frac{\partial V}{\partial x} = BV$
    - $\frac{\partial^2 V}{\partial x^2} = B^2 V$

    Substituting into $\frac{\partial V}{\partial \tau} = \mathcal{A}V - xV$:

    $$
    (A' + B'x)V = \kappa(\theta - x)BV + \frac{1}{2}\sigma^2 B^2 V - xV
    $$

    Dividing by $V > 0$ and collecting terms:

    **Constant terms:** $A' = \kappa\theta B + \frac{1}{2}\sigma^2 B^2$

    **Coefficient of $x$:** $B' = -\kappa B - 1$

    The $B$-equation $B' = -\kappa B - 1$ with $B(0) = 0$ has solution $B(\tau) = -\frac{1 - e^{-\kappa\tau}}{\kappa}$. One can verify: $B'(\tau) = -e^{-\kappa\tau}$ and $-\kappa B(\tau) - 1 = -\kappa \cdot \left(-\frac{1 - e^{-\kappa\tau}}{\kappa}\right) - 1 = (1 - e^{-\kappa\tau}) - 1 = -e^{-\kappa\tau}$, confirming equality. Also $B(0) = -\frac{1 - 1}{\kappa} = 0$, matching the initial condition.

---

**Exercise 4.** Explain why the Feynman-Kac approach converts the computational cost from "exponential in dimension $d$" (for PDE grid methods) to "polynomial in $d$" (for Riccati ODE methods) when the process is affine. What is the dominant cost in the Riccati approach as the number of factors $d$ increases?

??? success "Solution to Exercise 4"
    **PDE grid methods** discretize the spatial domain on a grid with $N$ points per dimension. For a $d$-dimensional PDE, the total number of grid points is $N^d$. Each time step of an implicit finite difference scheme requires solving a linear system of size $N^d$, giving cost $O(N^d)$ per time step and $O(N_\tau \cdot N^d)$ total. For $d = 5$ and $N = 100$, this is $10^{10}$---prohibitively expensive.

    **Riccati ODE methods** solve a system of $d + 1$ scalar ODEs (one for $\tilde{\phi}$ and $d$ for $\tilde{\psi}_1, \ldots, \tilde{\psi}_d$). Each ODE is one-dimensional, and standard ODE solvers (e.g., Runge-Kutta) have cost $O(N_\tau)$ per equation, giving total cost $O((d+1) \cdot N_\tau)$---linear in $d$.

    The dominant cost as $d$ increases is the evaluation of the quadratic form $\frac{1}{2}\langle \tilde{\psi}, a_j \tilde{\psi} \rangle$ in each $\tilde{\psi}_j$-equation, which involves $O(d^2)$ operations per evaluation (matrix-vector product). Thus the total cost scales as $O(d^2 \cdot N_\tau)$, which is polynomial in $d$ rather than exponential.

---

**Exercise 5.** The Feynman-Kac theorem requires regularity conditions on the coefficients and the terminal function $h$. For the payoff $h(x) = (e^x - K)^+$, explain why $h$ is not smooth at $x = \log K$ and discuss how this affects the validity of the Feynman-Kac representation. Does the exponential-affine form still apply?

??? success "Solution to Exercise 5"
    The payoff $h(x) = (e^x - K)^+$ has a kink at $x = \log K$: it equals $0$ for $x < \log K$ and $e^x - K$ for $x \geq \log K$. The function is continuous but not differentiable at $x = \log K$ (the left derivative is $0$ and the right derivative is $K$), so $h$ is not a $C^2$ function.

    The classical Feynman-Kac theorem requires $h$ to have sufficient smoothness (or polynomial growth conditions) for the solution $V(t, x)$ to be a classical solution of the PDE. Since $h$ is not smooth at $x = \log K$, the PDE solution $V(t, x)$ may not be classical at $t = T$. However, for $t < T$ (strictly before maturity), the diffusion process smooths the terminal condition, and $V(t, x)$ is indeed $C^{1,2}$ and satisfies the PDE classically.

    The exponential-affine form $V = e^{\tilde{\phi} + \langle \tilde{\psi}, x \rangle}$ does **not** directly apply to the call payoff because this ansatz corresponds to the specific terminal condition $h(x) = e^{\langle u, x \rangle}$, not $(e^x - K)^+$. To price the call, one uses Fourier inversion: express $h$ as an integral of exponential functions, apply the exponential-affine formula to each, and integrate. The Feynman-Kac representation remains valid (in the mild/viscosity sense), but the affine form is used indirectly through the characteristic function, not directly for the call payoff.

---

**Exercise 6.** For a two-factor affine model with state vector $(r_t, V_t)$ and short rate $r(x) = x_1$, write down the Feynman-Kac PDE in two spatial dimensions. Show that the exponential-affine ansatz $V(\tau, x_1, x_2) = e^{\phi(\tau) + \psi_1(\tau)x_1 + \psi_2(\tau)x_2}$ reduces this PDE to a system of three ODEs.

??? success "Solution to Exercise 6"
    Let the two-factor affine model have state $(X_t^{(1)}, X_t^{(2)}) = (r_t, V_t)$ with dynamics

    $$
    dX^{(1)} = b_1(x)\,dt + \sigma_{11}(x)\,dW_1 + \sigma_{12}(x)\,dW_2
    $$

    $$
    dX^{(2)} = b_2(x)\,dt + \sigma_{21}(x)\,dW_1 + \sigma_{22}(x)\,dW_2
    $$

    With $r(x) = x_1$ (so $\rho_0 = 0$, $\rho_1 = (1, 0)^T$), the Feynman-Kac PDE in two spatial dimensions is

    $$
    \frac{\partial V}{\partial \tau} = b_1(x)\frac{\partial V}{\partial x_1} + b_2(x)\frac{\partial V}{\partial x_2} + \frac{1}{2}a_{11}(x)\frac{\partial^2 V}{\partial x_1^2} + a_{12}(x)\frac{\partial^2 V}{\partial x_1 \partial x_2} + \frac{1}{2}a_{22}(x)\frac{\partial^2 V}{\partial x_2^2} - x_1 V
    $$

    where $a_{ij}(x) = \sum_k \sigma_{ik}(x)\sigma_{jk}(x)$ are the diffusion matrix entries, all affine in $x$.

    Substituting the ansatz $V = e^{\phi(\tau) + \psi_1(\tau)x_1 + \psi_2(\tau)x_2}$ and dividing by $V$:

    $$
    \phi' + \psi_1' x_1 + \psi_2' x_2 = b_1 \psi_1 + b_2 \psi_2 + \frac{1}{2}a_{11}\psi_1^2 + a_{12}\psi_1\psi_2 + \frac{1}{2}a_{22}\psi_2^2 - x_1
    $$

    Since all coefficients are affine in $(x_1, x_2)$, collecting constant, $x_1$-, and $x_2$-terms yields three ODEs:

    **ODE for $\phi$:** $\phi'(\tau) = F(\psi_1, \psi_2) - 0$ (constant terms)

    **ODE for $\psi_1$:** $\psi_1'(\tau) = R_1(\psi_1, \psi_2) - 1$ (coefficient of $x_1$, with $-\rho_{1,1} = -1$)

    **ODE for $\psi_2$:** $\psi_2'(\tau) = R_2(\psi_1, \psi_2) - 0$ (coefficient of $x_2$, with $-\rho_{1,2} = 0$)

    This is a system of three scalar ODEs (two coupled for $\psi_1, \psi_2$, plus one quadrature for $\phi$), replacing the original three-dimensional PDE ($\tau, x_1, x_2$). The initial conditions are $\phi(0) = 0$, $\psi_1(0) = u_1$, $\psi_2(0) = u_2$.
