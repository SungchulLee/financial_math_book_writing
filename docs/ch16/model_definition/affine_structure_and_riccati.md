# Affine Structure and Riccati System

The analytical tractability of the Heston model rests on a single structural property: the bivariate process $(x_t, v_t)$ is an **affine diffusion**. This means the drift vector and the diffusion matrix of the state process are affine (linear plus constant) functions of the state. The consequence is profound -- the conditional characteristic function of the log-price admits an exponential-affine form, reducing the pricing PDE in two spatial dimensions to a pair of ordinary differential equations (the Riccati system). This reduction from PDE to ODE is what makes Fourier-based pricing feasible.

This section defines affine diffusions, verifies that the Heston state process qualifies, derives the Riccati ODE system from the Feynman-Kac theorem, and states the initial conditions. The closed-form solution of this Riccati system is presented in the [characteristic function section](../heston_cf/closed_form_characteristic_function.md).

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Define what it means for a diffusion process to be affine
    - Verify that the Heston bivariate process $(x_t, v_t)$ satisfies the affine conditions
    - Write the exponential-affine ansatz for the characteristic function
    - Derive the Riccati ODEs for $C(\tau, u)$ and $D(\tau, u)$ from the Feynman-Kac PDE
    - State the initial conditions $C(0, u) = 0$ and $D(0, u) = 0$ and explain their meaning

---

## Affine Diffusions

### Intuition

Consider a general bivariate diffusion $(Y_t^{(1)}, Y_t^{(2)})$. Its drift and diffusion coefficients are functions of the state. If these functions happen to be affine -- that is, at most linear in the state variables -- then the characteristic function of $Y_T$ conditional on $Y_t$ takes an exponential form in which the exponent is itself affine in the current state. This exponential-affine structure transforms the problem of computing expectations (which typically requires solving a PDE) into solving a system of ODEs for the coefficients in the exponent. The ODEs are of Riccati type: first-order, quadratic in the unknown.

### Definition

!!! info "Definition: Affine Diffusion"
    A Markov diffusion process $Y_t \in \mathbb{R}^n$ with dynamics $dY_t = \mu(Y_t)\,dt + \Sigma(Y_t)\,dW_t$ is **affine** if:

    1. The drift vector is affine in the state: $\mu(y) = a_0 + A\,y$ for some $a_0 \in \mathbb{R}^n$ and $A \in \mathbb{R}^{n \times n}$
    2. The diffusion matrix $\Sigma(y)\Sigma(y)^\top$ has entries that are affine in the state: $[\Sigma(y)\Sigma(y)^\top]_{ij} = [\alpha_0]_{ij} + \sum_{k=1}^n [\alpha_k]_{ij}\,y_k$ for constant matrices $\alpha_0, \alpha_1, \ldots, \alpha_n$

    When these conditions hold, the conditional characteristic function satisfies:

    $$
    \mathbb{E}\!\left[e^{i\,u^\top Y_T} \,\middle|\, Y_t = y\right] = \exp\!\bigl(\Phi(\tau, u) + \Psi(\tau, u)^\top y\bigr)
    $$

    where $\tau = T - t$, and $\Phi : \mathbb{R}_+ \times \mathbb{R}^n \to \mathbb{C}$ and $\Psi : \mathbb{R}_+ \times \mathbb{R}^n \to \mathbb{C}^n$ satisfy a system of Riccati ODEs.

The key point is that the exponent is linear in the current state $y$. The functions $\Phi$ and $\Psi$ depend on $\tau$ and the transform variable $u$ but not on the state. This is the source of computational efficiency: once $\Phi$ and $\Psi$ are computed (by solving the Riccati ODEs), the characteristic function at any state $y$ is obtained by a simple dot product.

---

## Verifying the Affine Property for Heston

### The Heston State Vector

Recall from the [Heston SDE section](heston_sde_and_parameters.md) that the log-price $x_t = \ln S_t$ and variance $v_t$ satisfy:

$$
dx_t = \left(r - q - \tfrac{1}{2}\,v_t\right)dt + \sqrt{v_t}\,dW_t^{(1)}
$$

$$
dv_t = \kappa\,(\theta - v_t)\,dt + \sigma_v\,\sqrt{v_t}\,dW_t^{(2)}
$$

Define the state vector $Y_t = (x_t, v_t)^\top \in \mathbb{R}^2$.

### Checking the Drift

The drift vector is:

$$
\mu(Y_t) = \begin{pmatrix} r - q - \frac{1}{2}\,v_t \\ \kappa\theta - \kappa\,v_t \end{pmatrix} = \underbrace{\begin{pmatrix} r - q \\ \kappa\theta \end{pmatrix}}_{a_0} + \underbrace{\begin{pmatrix} 0 & -\frac{1}{2} \\ 0 & -\kappa \end{pmatrix}}_{A} \begin{pmatrix} x_t \\ v_t \end{pmatrix}
$$

This is affine in $Y_t = (x_t, v_t)^\top$. The drift of $x_t$ depends linearly on $v_t$ (through the $-\frac{1}{2}v_t$ term), the drift of $v_t$ depends linearly on $v_t$ (through the $-\kappa v_t$ term), and neither depends on $x_t$.

### Checking the Diffusion Matrix

The diffusion coefficient matrix for the Cholesky-decomposed system (using independent Brownian motions $Z_t^{(1)}, Z_t^{(2)}$) is:

$$
\Sigma(Y_t) = \begin{pmatrix} \sqrt{v_t} & 0 \\ \sigma_v\rho\sqrt{v_t} & \sigma_v\sqrt{1-\rho^2}\sqrt{v_t} \end{pmatrix}
$$

The instantaneous covariance matrix is:

$$
\Sigma(Y_t)\Sigma(Y_t)^\top = \begin{pmatrix} v_t & \sigma_v\rho\,v_t \\ \sigma_v\rho\,v_t & \sigma_v^2\,v_t \end{pmatrix} = \underbrace{\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}}_{\alpha_0} + v_t \underbrace{\begin{pmatrix} 1 & \sigma_v\rho \\ \sigma_v\rho & \sigma_v^2 \end{pmatrix}}_{\alpha_2}
$$

Every entry is affine in $v_t$ (with no dependence on $x_t$). The matrix $\alpha_1$ corresponding to $x_t$ is zero, and $\alpha_0$ is zero. The affine condition is satisfied.

!!! success "Proposition: Heston Is Affine"
    The Heston state process $Y_t = (x_t, v_t)^\top$ is an affine diffusion. Its drift is affine in $Y_t$ with coefficients:

    $$
    a_0 = \begin{pmatrix} r - q \\ \kappa\theta \end{pmatrix}, \qquad A = \begin{pmatrix} 0 & -\frac{1}{2} \\ 0 & -\kappa \end{pmatrix}
    $$

    Its covariance matrix is affine in $Y_t$ with $\alpha_0 = 0$ and:

    $$
    \alpha_2 = \begin{pmatrix} 1 & \sigma_v\rho \\ \sigma_v\rho & \sigma_v^2 \end{pmatrix}
    $$

---

## The Characteristic Function Ansatz

### Setting Up the PDE

We seek the conditional characteristic function of the log-price at maturity $T$:

$$
\phi(u, \tau; x, v) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{iu\,x_T} \,\middle|\, x_t = x,\; v_t = v\right]
$$

where $\tau = T - t$ is time to maturity. By the Feynman-Kac theorem, $\phi$ satisfies the backward Kolmogorov (or pricing) PDE:

$$
-\frac{\partial \phi}{\partial \tau} = \left(r - q - \tfrac{1}{2}v\right)\frac{\partial \phi}{\partial x} + \kappa(\theta - v)\frac{\partial \phi}{\partial v} + \tfrac{1}{2}v\frac{\partial^2 \phi}{\partial x^2} + \rho\sigma_v v\frac{\partial^2 \phi}{\partial x \partial v} + \tfrac{1}{2}\sigma_v^2 v\frac{\partial^2 \phi}{\partial v^2}
$$

with terminal condition $\phi(u, 0; x, v) = e^{iux}$.

!!! note "Sign Convention"
    We write the PDE in terms of $\tau = T - t$ (time to maturity), so the time derivative carries a minus sign. The terminal condition becomes the initial condition $\phi(u, 0; x, v) = e^{iux}$ at $\tau = 0$.

### The Exponential-Affine Ansatz

Because the Heston process is affine, we guess that $\phi$ takes the form:

$$
\phi(u, \tau; x, v) = \exp\!\bigl(C(\tau, u) + D(\tau, u)\,v + iu\,x\bigr)
$$

where $C(\tau, u)$ and $D(\tau, u)$ are functions of time to maturity and the transform variable, independent of the state $(x, v)$. The term $iu\,x$ is present because the terminal condition $\phi(u, 0; x, v) = e^{iux}$ requires $C(0, u) = 0$, $D(0, u) = 0$.

---

## Derivation of the Riccati System

### Computing Partial Derivatives

With the ansatz $\phi = \exp(C + Dv + iux)$, the partial derivatives are:

$$
\frac{\partial \phi}{\partial \tau} = (C' + D'v)\,\phi, \qquad \frac{\partial \phi}{\partial x} = iu\,\phi, \qquad \frac{\partial^2 \phi}{\partial x^2} = (iu)^2\,\phi = -u^2\,\phi
$$

$$
\frac{\partial \phi}{\partial v} = D\,\phi, \qquad \frac{\partial^2 \phi}{\partial v^2} = D^2\,\phi, \qquad \frac{\partial^2 \phi}{\partial x \partial v} = iu\,D\,\phi
$$

where $C' = dC/d\tau$ and $D' = dD/d\tau$.

### Substituting into the PDE

Substituting into the Feynman-Kac PDE and dividing both sides by $\phi$ (which is never zero):

$$
-(C' + D'v) = (r - q - \tfrac{1}{2}v)(iu) + \kappa(\theta - v)D + \tfrac{1}{2}v(-u^2) + \rho\sigma_v v(iu\,D) + \tfrac{1}{2}\sigma_v^2 v\,D^2
$$

Rearranging and grouping terms by powers of $v$:

$$
-(C' + D'v) = \bigl[(r-q)(iu) + \kappa\theta D\bigr] + v\bigl[-\tfrac{1}{2}(iu) - \kappa D - \tfrac{1}{2}u^2 + \rho\sigma_v(iu)D + \tfrac{1}{2}\sigma_v^2 D^2\bigr]
$$

Since this must hold for all values of $v$, the coefficients of $v^0$ and $v^1$ must match independently.

### The Riccati ODE System

!!! success "Theorem: Riccati ODEs for the Heston Characteristic Function"
    The functions $C(\tau, u)$ and $D(\tau, u)$ in the exponential-affine characteristic function $\phi = \exp(C + Dv + iux)$ satisfy:

    $$
    D'(\tau, u) = \tfrac{1}{2}\sigma_v^2\,D^2 + (\rho\sigma_v\,iu - \kappa)\,D + \tfrac{1}{2}(iu - u^2)
    $$

    $$
    C'(\tau, u) = (r - q)\,iu + \kappa\theta\,D
    $$

    with initial conditions $C(0, u) = 0$ and $D(0, u) = 0$.

**Proof.** Matching the $v^0$ terms gives $-C' = (r-q)(iu) + \kappa\theta D$, hence $C' = -(r-q)(iu) - \kappa\theta D$. With the convention that the PDE has $-\partial\phi/\partial\tau$ on the left, rearranging yields $C' = (r-q)\,iu + \kappa\theta\,D$.

Matching the $v^1$ terms gives $-D' = -\frac{1}{2}(iu) - \kappa D - \frac{1}{2}u^2 + \rho\sigma_v(iu)D + \frac{1}{2}\sigma_v^2 D^2$, hence:

$$
D' = \tfrac{1}{2}(iu) + \kappa D + \tfrac{1}{2}u^2 - \rho\sigma_v(iu)D - \tfrac{1}{2}\sigma_v^2 D^2
$$

which rearranges to:

$$
D' = \tfrac{1}{2}\sigma_v^2 D^2 + (\rho\sigma_v\,iu - \kappa)D + \tfrac{1}{2}(iu - u^2)
$$

The initial conditions follow from the terminal condition $\phi(u, 0; x, v) = e^{iux}$, which requires $C(0, u) = 0$ and $D(0, u) = 0$. $\square$

!!! tip "Structure of the Riccati System"
    The $D$-equation is a **scalar Riccati ODE** -- first order, quadratic in $D$. It can be solved independently of $C$. Once $D(\tau, u)$ is known, $C(\tau, u)$ is obtained by a single integration:

    $$
    C(\tau, u) = (r - q)\,iu\,\tau + \kappa\theta \int_0^{\tau} D(s, u)\,ds
    $$

    The Riccati ODE for $D$ has a closed-form solution involving a discriminant $\gamma = \sqrt{(\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)}$. This solution is derived in the [Riccati ODE System](../heston_cf/riccati_ode_system.md) section and the [Closed-Form Characteristic Function](../heston_cf/closed_form_characteristic_function.md) section.

---

## Worked Example: Riccati Coefficients at a Specific Point

??? example "Evaluating D'(0, u) and C'(0, u)"
    At $\tau = 0$, we have $D(0, u) = 0$ and $C(0, u) = 0$. The initial rates of change are:

    $$
    D'(0, u) = \tfrac{1}{2}\sigma_v^2 \cdot 0 + (\rho\sigma_v\,iu - \kappa) \cdot 0 + \tfrac{1}{2}(iu - u^2) = \tfrac{1}{2}(iu - u^2)
    $$

    $$
    C'(0, u) = (r - q)\,iu + \kappa\theta \cdot 0 = (r - q)\,iu
    $$

    For small $\tau$, the Taylor expansion gives:

    $$
    D(\tau, u) \approx \tfrac{1}{2}(iu - u^2)\,\tau, \qquad C(\tau, u) \approx (r - q)\,iu\,\tau
    $$

    Substituting into the characteristic function:

    $$
    \phi(u, \tau; x, v) \approx \exp\!\bigl((r - q)\,iu\,\tau + \tfrac{1}{2}(iu - u^2)\,v\,\tau + iu\,x\bigr)
    $$

    Setting $u = -i$ (so $iu = 1$ and $u^2 = -1$): $\phi(-i, \tau) = \exp((r-q)\tau + v\tau + x) = S\,e^{(r-q+v)\tau}$. In the limit $\tau \to 0$, this recovers $\phi(-i, 0) = e^x = S$, as expected.

---

## Why Affine Structure Matters for Pricing

The practical consequence of the affine structure is that European option pricing reduces to a one-dimensional numerical integration (Fourier inversion) rather than solving a two-dimensional PDE or running Monte Carlo simulation.

The pricing formula for a European call with strike $K$ and maturity $T$ is:

$$
C(S, v, T) = e^{-r\tau}\frac{1}{\pi}\int_0^{\infty} \text{Re}\!\left[\frac{e^{-iu\ln K}\,\phi(u - i, \tau; x, v)}{iu\,\phi(-i, \tau; x, v)}\right]du
$$

Because $\phi$ has a closed form (via the Riccati solution), this integral can be evaluated by standard quadrature in milliseconds. Without affine structure, $\phi$ would itself require a numerical PDE solve for each value of $u$, making the Fourier approach impractical.

---

## Summary

The Heston model is an affine diffusion because both the drift and the instantaneous covariance of the state vector $(x_t, v_t)$ are affine functions of $v_t$. This structure implies that the conditional characteristic function of the log-price takes the exponential-affine form $\phi = \exp(C + Dv + iux)$, where $C$ and $D$ satisfy Riccati ODEs. The $D$-equation is a scalar Riccati ODE (quadratic in $D$) that can be solved in closed form, and $C$ is then obtained by integration. This dimensional reduction -- from a two-dimensional PDE to a pair of ODEs -- is the foundation of all Fourier-based pricing methods for the Heston model.

The derivation of the closed-form solutions for $C(\tau, u)$ and $D(\tau, u)$ is carried out in the [Riccati ODE System](../heston_cf/riccati_ode_system.md) and [Closed-Form Characteristic Function](../heston_cf/closed_form_characteristic_function.md) sections.

---
