# Infinitesimal Generator of Affine Processes

The infinitesimal generator is the differential operator that encodes the local behavior of a Markov process. For a diffusion, it involves the drift and the second-order diffusion term; for a jump-diffusion, it adds an integral over jump sizes. The defining property of an affine process is that every coefficient appearing in the generator --- drift, diffusion, and jump intensity --- is an **affine function** of the state. This affine structure is what makes the generator act so simply on exponential functions, producing the functions $F$ and $R$ that drive the Riccati ODE system for the characteristic function.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Write down the infinitesimal generator of a general affine jump-diffusion and identify each component
    2. Verify the affine structure of the drift, diffusion, and jump compensator
    3. Compute the generator applied to exponential-affine functions and derive the functions $F(u)$ and $R(u)$
    4. Explain the domain of the generator and the regularity conditions required
    5. Connect the generator to the Riccati system via the Kolmogorov backward equation

---

## Motivation

### Why the Generator Matters

The transition semigroup $(P_t)_{t \geq 0}$ of a Markov process encodes the entire probabilistic evolution: $P_t f(x) = \mathbb{E}^x[f(X_t)]$. The infinitesimal generator $\mathcal{A}$ captures the **instantaneous rate of change** of this semigroup:

$$
\mathcal{A}f(x) = \lim_{t \downarrow 0} \frac{P_t f(x) - f(x)}{t}
$$

Knowing $\mathcal{A}$ is equivalent to knowing the semigroup (under mild conditions), just as knowing the derivative of a function determines the function up to initial conditions. For pricing and hedging, the generator appears directly in the **Kolmogorov backward equation**: if $u(t,x) = \mathbb{E}^x[g(X_T) \mid X_t = x]$, then $\partial_t u + \mathcal{A}u = 0$. For affine processes, the affine structure of $\mathcal{A}$ is precisely what converts this PDE into a system of Riccati ODEs.

---

## The General Infinitesimal Generator

### Diffusion Case

For a $d$-dimensional diffusion $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$ with drift $\mu : \mathbb{R}^d \to \mathbb{R}^d$ and diffusion matrix $a(x) = \sigma(x)\sigma(x)^\top$, the generator acts on twice continuously differentiable functions $f \in C^2(\mathbb{R}^d)$ as

$$
\mathcal{A}f(x) = \sum_{i=1}^d \mu_i(x)\,\frac{\partial f}{\partial x_i}(x) + \frac{1}{2}\sum_{i,j=1}^d a_{ij}(x)\,\frac{\partial^2 f}{\partial x_i \partial x_j}(x)
$$

In compact notation:

$$
\mathcal{A}f(x) = \mu(x)^\top \nabla f(x) + \frac{1}{2}\operatorname{tr}\!\bigl[a(x)\,\nabla^2 f(x)\bigr]
$$

### Jump-Diffusion Case

When the process also has jumps with compensator $m(x, dz)$ (the Levy-type jump measure that may depend on the state), the generator gains an integral term:

!!! info "Definition: Generator of a Jump-Diffusion"
    The infinitesimal generator of a jump-diffusion is

    $$
    \mathcal{A}f(x) = \mu(x)^\top \nabla f(x) + \frac{1}{2}\operatorname{tr}\!\bigl[a(x)\,\nabla^2 f(x)\bigr] + \int_{\mathbb{R}^d \setminus \{0\}} \!\bigl[f(x+z) - f(x) - z^\top \nabla f(x)\,\mathbf{1}_{\{|z| \leq 1\}}\bigr]\,m(x, dz)
    $$

    The three terms represent:

    - **Drift**: the deterministic component of the infinitesimal evolution
    - **Diffusion**: the second-order contribution from the continuous martingale part
    - **Jumps**: the contribution from discontinuous movements, with the truncation function $\mathbf{1}_{\{|z| \leq 1\}}$ ensuring integrability

---

## Affine Structure of the Generator

### Affine Coefficients

For an affine process on the state space $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$, the generator coefficients are affine functions of the state:

$$
\mu(x) = b_0 + B x
$$

$$
a(x) = a_0 + \sum_{i=1}^d \alpha_i\,x^{(i)}
$$

$$
m(x, dz) = m_0(dz) + \sum_{i=1}^d x^{(i)}\,m_i(dz)
$$

where:

- $b_0 \in \mathbb{R}^d$ and $B \in \mathbb{R}^{d \times d}$ define the affine drift
- $a_0 \in \mathbb{R}^{d \times d}$ (symmetric, positive semi-definite) and $\alpha_i \in \mathbb{R}^{d \times d}$ (symmetric, positive semi-definite) define the affine diffusion
- $m_0(dz)$ and $m_i(dz)$ are Levy measures on $\mathbb{R}^d \setminus \{0\}$ defining the affine jump structure

!!! info "Theorem: Generator of an Affine Process"
    The infinitesimal generator of an affine process takes the form

    $$
    \mathcal{A}f(x) = (b_0 + Bx)^\top \nabla f(x) + \frac{1}{2}\operatorname{tr}\!\left[\left(a_0 + \sum_{i=1}^d \alpha_i\,x^{(i)}\right)\nabla^2 f(x)\right] + \int_{\mathbb{R}^d \setminus \{0\}} \bigl[f(x+z) - f(x) - h(z)^\top \nabla f(x)\bigr]\left(m_0(dz) + \sum_{i=1}^d x^{(i)}\,m_i(dz)\right)
    $$

    where $h(z) = z\,\mathbf{1}_{\{|z| \leq 1\}}$ is the truncation function.

The affine dependence on $x$ in every term is the structural property that distinguishes affine processes from general Markov processes.

---

## Action on Exponential Functions

### The Key Computation

The characteristic function of an affine process has the exponential-affine form precisely because the generator acts on exponential functions in a particularly simple way. This computation is the technical heart of the affine theory.

!!! info "Proposition: Generator Applied to Exponentials"
    For $e_u(x) = e^{u^\top x}$ with $u \in \mathbb{C}^d$ in the appropriate domain, the generator satisfies

    $$
    \mathcal{A}e_u(x) = \bigl[F(u) + R(u)^\top x\bigr]\,e_u(x)
    $$

    where

    $$
    F(u) = b_0^\top u + \frac{1}{2}u^\top a_0\,u + \int_{\mathbb{R}^d \setminus \{0\}} \bigl(e^{u^\top z} - 1 - u^\top h(z)\bigr)\,m_0(dz)
    $$

    $$
    R_i(u) = (Bu)_i + \frac{1}{2}u^\top \alpha_i\,u + \int_{\mathbb{R}^d \setminus \{0\}} \bigl(e^{u^\top z} - 1 - u^\top h(z)\bigr)\,m_i(dz)
    $$

    for $i = 1, \ldots, d$.

**Proof.** Applying the generator to $e_u(x)$:

**Drift term:**

$$
(b_0 + Bx)^\top \nabla e_u(x) = (b_0 + Bx)^\top u\,e_u(x) = \bigl(b_0^\top u + (Bx)^\top u\bigr)\,e_u(x)
$$

**Diffusion term:**

$$
\frac{1}{2}\operatorname{tr}\!\left[\left(a_0 + \sum_i \alpha_i x^{(i)}\right) u\,u^\top\right] e_u(x) = \frac{1}{2}\left(u^\top a_0\,u + \sum_i u^\top \alpha_i\,u\,x^{(i)}\right) e_u(x)
$$

**Jump term:**

$$
\int \bigl[e^{u^\top(x+z)} - e^{u^\top x} - h(z)^\top u\,e^{u^\top x}\bigr]\left(m_0(dz) + \sum_i x^{(i)}m_i(dz)\right)
$$

$$
= e_u(x)\int\bigl(e^{u^\top z} - 1 - u^\top h(z)\bigr)\left(m_0(dz) + \sum_i x^{(i)}m_i(dz)\right)
$$

Collecting terms independent of $x$ into $F(u)$ and terms proportional to $x^{(i)}$ into $R_i(u)$ gives the result. $\square$

### Connection to the Riccati System

The functions $F$ and $R$ are precisely the right-hand sides of the Riccati ODEs for the characteristic function. If $\phi(\tau, u)$ and $\psi(\tau, u)$ satisfy

$$
\frac{d\psi}{d\tau} = R(\psi), \qquad \frac{d\phi}{d\tau} = F(\psi)
$$

with $\psi(0, u) = u$ and $\phi(0, u) = 0$, then

$$
\mathbb{E}\!\left[e^{u^\top X_T} \mid X_t = x\right] = \exp\!\bigl(\phi(\tau, u) + \psi(\tau, u)^\top x\bigr)
$$

This follows because the process $M_s = \exp(\phi(T-s, u) + \psi(T-s, u)^\top X_s)$ is a martingale on $[t, T]$, which requires $\partial_s M_s + \mathcal{A}M_s = 0$ --- and the Riccati system is precisely the condition for this cancellation.

---

## Domain of the Generator

### Core Domain

The generator $\mathcal{A}$ is defined on a domain $\mathcal{D}(\mathcal{A}) \subset C_0(\mathbb{R}^d)$ (continuous functions vanishing at infinity) that is dense in $C_0(\mathbb{R}^d)$. For affine diffusions (no jumps), the domain contains $C_c^2(\mathbb{R}^d)$ (twice continuously differentiable functions with compact support).

For affine jump-diffusions, the domain must additionally satisfy integrability conditions with respect to the jump measures $m_0$ and $m_i$: the function $f$ must be such that the integral term in the generator converges.

### Extended Generator

In practice, the exponential functions $e_u(x) = e^{u^\top x}$ do not belong to $C_0(\mathbb{R}^d)$ (they grow without bound). The computation above uses the **extended generator**, which acts on a larger class of functions satisfying appropriate growth conditions. The extended generator coincides with $\mathcal{A}$ on the core domain and satisfies the same formula on exponential functions provided the moments $\int |z|^2\,(m_0(dz) + \sum_i |x^{(i)}|\,m_i(dz))$ are finite.

!!! warning "Growth Conditions"
    The exponential function $e_u$ belongs to the domain of the extended generator only when $u$ lies in the set $\mathcal{U} = \{u \in \mathbb{C}^d : \mathbb{E}[e^{\operatorname{Re}(u)^\top X_t}] < \infty\}$. For CIR-type components ($x^{(i)} \geq 0$), this restricts $\operatorname{Re}(u_i) \leq 0$ for the corresponding coordinates.

---

## Example: CIR Process

Consider the one-dimensional CIR process

$$
dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t
$$

on $D = \mathbb{R}_+$, with no jumps. The affine coefficients are:

- $b_0 = \kappa\theta$, $B = -\kappa$ (scalar)
- $a_0 = 0$, $\alpha_1 = \xi^2$
- $m_0 = m_1 = 0$ (no jumps)

The generator is

$$
\mathcal{A}f(x) = \kappa(\theta - x)\,f'(x) + \frac{1}{2}\xi^2 x\,f''(x)
$$

Applying to $e_u(x) = e^{ux}$:

$$
\mathcal{A}e^{ux} = \left[\kappa\theta\,u + \left(-\kappa u + \frac{1}{2}\xi^2 u^2\right)x\right]e^{ux}
$$

Reading off:

$$
F(u) = \kappa\theta\,u, \qquad R(u) = -\kappa u + \frac{1}{2}\xi^2 u^2
$$

The Riccati equation $\psi' = R(\psi) = -\kappa\psi + \frac{1}{2}\xi^2\psi^2$ is the familiar CIR Riccati equation, whose solution gives the CIR characteristic function and bond price formula.

---

## Example: Affine Jump-Diffusion

Consider a one-dimensional affine process with constant-intensity compound Poisson jumps:

$$
dX_t = \kappa(\theta - X_t)\,dt + \sigma\,dW_t + dJ_t
$$

where $J_t = \sum_{k=1}^{N_t} Z_k$ is a compound Poisson process with intensity $\lambda$ and jump size distribution $\nu(dz)$. Here the jumps are state-independent, so $m_0(dz) = \lambda\,\nu(dz)$ and $m_1 = 0$.

The generator is

$$
\mathcal{A}f(x) = \kappa(\theta - x)f'(x) + \frac{1}{2}\sigma^2 f''(x) + \lambda\int_{\mathbb{R} \setminus \{0\}}\bigl[f(x+z) - f(x)\bigr]\,\nu(dz)
$$

where the truncation function is absorbed since $\int |z|\,\nu(dz) < \infty$ for compound Poisson processes. Applying to $e^{ux}$:

$$
F(u) = \kappa\theta\,u + \frac{1}{2}\sigma^2 u^2 + \lambda\bigl(\hat{\nu}(u) - 1\bigr)
$$

$$
R(u) = -\kappa u
$$

where $\hat{\nu}(u) = \int e^{uz}\,\nu(dz)$ is the moment generating function of the jump size distribution. The jump contribution $\lambda(\hat{\nu}(u) - 1)$ adds to the $F$ function because the jump intensity is state-independent.

---

## Summary

The infinitesimal generator of an affine process has three components --- drift, diffusion, and jumps --- each affine in the state variable $x$. The key computation is the action of the generator on exponential functions: $\mathcal{A}e^{u^\top x} = [F(u) + R(u)^\top x]\,e^{u^\top x}$, where $F$ collects the state-independent contributions and $R$ collects the state-dependent ones. The functions $F$ and $R$ are precisely the right-hand sides of the Riccati ODE system that governs the characteristic function. This connection --- from the generator to exponentials to Riccati equations --- is the fundamental mechanism that makes affine processes analytically tractable.

---

## Further Reading

- Duffie, D., Filipovic, D., and Schachermayer, W. (2003). "Affine Processes and Applications in Finance." *Annals of Applied Probability*, 13(3), 984--1053.
- Filipovic, D. (2009). *Term-Structure Models: A Graduate Course*. Springer.
- Sato, K. (1999). *Levy Processes and Infinitely Divisible Distributions*. Cambridge University Press.

---

## Exercises

**Exercise 1.** For the Vasicek model $dX_t = \kappa(\theta - X_t)\,dt + \sigma\,dW_t$, write down the infinitesimal generator $\mathcal{A}$ and compute $\mathcal{A}f$ for $f(x) = x^2$. Verify that $\mathcal{A}f(x) = 2\kappa(\theta - x)x + \sigma^2$, and explain why this result does not have the form $[F(u) + R(u)x]\,f(x)$ (i.e., polynomial test functions do not simplify in the same way as exponentials).

---

**Exercise 2.** For the CIR process, compute $\mathcal{A}e^{ux}$ directly by evaluating $\kappa(\theta - x)(ue^{ux}) + \frac{1}{2}\xi^2 x(u^2 e^{ux})$. Collect terms to identify $F(u) = \kappa\theta u$ and $R(u) = -\kappa u + \frac{1}{2}\xi^2 u^2$. Verify that these match the Riccati ODE right-hand sides.

---

**Exercise 3.** Consider a two-dimensional affine process where $X_t^{(1)}$ follows a CIR process and $X_t^{(2)}$ follows a Vasicek process, with no cross-diffusion. Write down the generator $\mathcal{A}$ and compute $\mathcal{A}e^{u_1 x_1 + u_2 x_2}$. Show that $F$ and $R = (R_1, R_2)$ decompose into independent scalar contributions.

---

**Exercise 4.** For the affine jump-diffusion $dX_t = \kappa(\theta - X_t)\,dt + \sigma\,dW_t + dJ_t$ with compound Poisson jumps of intensity $\lambda$ and exponential jump sizes with parameter $\eta$, compute $\hat{\nu}(u) = \int_0^\infty e^{uz}\eta e^{-\eta z}\,dz$ and identify the domain of $u$ for which the integral converges. Write down $F(u)$ incorporating the jump term $\lambda(\hat{\nu}(u) - 1)$.

---

**Exercise 5.** The extended generator allows $\mathcal{A}$ to act on exponential functions that do not vanish at infinity. Explain why the standard generator defined on $C_0(\mathbb{R}^d)$ cannot handle $e_u(x) = e^{u^\top x}$, and state the growth condition that $u$ must satisfy for $e_u$ to belong to the domain of the extended generator when $X_t$ has CIR-type components on $\mathbb{R}_+$.

---

**Exercise 6.** Using the generator definition $\mathcal{A}f(x) = \lim_{t \downarrow 0}\frac{P_t f(x) - f(x)}{t}$, verify $\mathcal{A}e^{ux} = [F(u) + R(u)x]e^{ux}$ for the OU process by first computing $P_t e^{ux} = \mathbb{E}[e^{uX_t} \mid X_0 = x]$ using the known Gaussian transition density, then differentiating at $t = 0$.
