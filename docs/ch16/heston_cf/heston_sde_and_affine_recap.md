# Heston SDE and Affine Structure Recap

This section serves as the entry point to the characteristic function derivation, recapping the essential elements from the model definition that are needed in the subsequent technical sections. Rather than repeating full proofs, we collect the key formulas, fix notation for the remainder of the characteristic function chapter, and clearly state the mathematical problem to be solved: finding the conditional characteristic function $\phi(u, \tau)$ of the log-price in closed form.

The derivation of the characteristic function is the central analytical achievement of the Heston model, and it proceeds in three stages: (1) setting up the Feynman-Kac PDE (this section), (2) deriving the [Riccati ODE system](riccati_ode_system.md), and (3) solving the Riccati ODEs in [closed form](closed_form_characteristic_function.md). Readers already familiar with the model definition may use this section as a quick reference.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Write the Heston bivariate SDE in log-price and variance form
    - State the affine drift and covariance conditions for the Heston model
    - Define the conditional characteristic function and explain its role in pricing
    - Write the Feynman-Kac PDE for the characteristic function
    - State the exponential-affine ansatz and the initial conditions

---

## The Heston Bivariate SDE

Under the risk-neutral measure $\mathbb{Q}$, the log-price $x_t = \ln S_t$ and variance $v_t$ satisfy (see [Heston SDE and Parameters](../model_definition/heston_sde_and_parameters.md)):

$$
dx_t = \left(r - q - \tfrac{1}{2}\,v_t\right)dt + \sqrt{v_t}\,dW_t^{(1)}
$$

$$
dv_t = \kappa(\theta - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t^{(2)}
$$

$$
d\langle W^{(1)}, W^{(2)} \rangle_t = \rho\,dt
$$

The parameters are: $\kappa > 0$ (mean-reversion speed), $\theta > 0$ (long-run variance), $\sigma_v > 0$ (vol-of-vol), $\rho \in [-1, 1]$ (correlation), and $v_0 > 0$ (initial variance). The constants $r \geq 0$ and $q \geq 0$ are the risk-free rate and continuous dividend yield.

---

## Affine Property Summary

The Heston model is an **affine diffusion** (see [Affine Structure and Riccati System](../model_definition/affine_structure_and_riccati.md)). For the characteristic function derivation, the relevant affine properties are:

!!! note "Affine Conditions for the Characteristic Function"
    The characteristic function has an exponential-affine form because:

    1. **Drift is affine in $v$**: The $x$-drift is $(r - q - \frac{1}{2}v)$ and the $v$-drift is $\kappa\theta - \kappa v$, both affine in $v$
    2. **Covariance is affine in $v$**: The instantaneous covariance matrix

    $$
    \Sigma\Sigma^\top = v \begin{pmatrix} 1 & \rho\sigma_v \\ \rho\sigma_v & \sigma_v^2 \end{pmatrix}
    $$

    is proportional to $v$ (affine with zero constant term)

    3. **No dependence on $x$**: Neither the drift of $v$ nor the covariance depends on $x$

    Property 3 is crucial: because the coefficients of the SDE are functions of $v$ alone (not of $x$), the characteristic function's dependence on $x$ is trivially through the factor $e^{iux}$, and the Riccati system involves only $v$-related terms.

---

## The Characteristic Function

### Definition

!!! info "Definition: Conditional Characteristic Function"
    The **conditional characteristic function** of the log-price at maturity $T$ is:

    $$
    \phi(u, \tau; x, v) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{iu\,x_T} \;\middle|\; x_t = x,\; v_t = v\right]
    $$

    where $\tau = T - t$ is the time to maturity and $u \in \mathbb{R}$ (or more generally, $u$ in the strip of analyticity).

The characteristic function encodes the full probability distribution of $x_T$: the density can be recovered via Fourier inversion, moments via differentiation at $u = 0$, and option prices via the Gil-Pelaez or COS methods.

### Why the Characteristic Function?

In the Black-Scholes model, the log-price distribution is Gaussian and the density is known explicitly. In the Heston model, the log-price distribution is no longer Gaussian (it has stochastic variance), and the density has no simple closed form. However, the characteristic function does have a closed form, thanks to the affine structure. Since Fourier methods can convert a characteristic function into option prices via a one-dimensional numerical integral, the characteristic function is the natural object to compute.

---

## The Feynman-Kac PDE

### Derivation

By the Feynman-Kac theorem, $\phi$ satisfies the backward Kolmogorov equation associated with the bivariate diffusion $(x_t, v_t)$. The generator of the Heston diffusion is:

$$
\mathcal{L} = \left(r - q - \tfrac{1}{2}v\right)\frac{\partial}{\partial x} + \kappa(\theta - v)\frac{\partial}{\partial v} + \tfrac{1}{2}v\frac{\partial^2}{\partial x^2} + \rho\sigma_v v\frac{\partial^2}{\partial x\,\partial v} + \tfrac{1}{2}\sigma_v^2 v\frac{\partial^2}{\partial v^2}
$$

The PDE for $\phi$ written in terms of $\tau = T - t$ (time to maturity) is:

$$
\frac{\partial \phi}{\partial \tau} = \mathcal{L}\,\phi
$$

with initial condition $\phi(u, 0; x, v) = e^{iux}$.

!!! warning "Sign Convention"
    With the convention $\tau = T - t$ (time to maturity increasing forward), the PDE becomes $\partial\phi/\partial\tau = \mathcal{L}\phi$ with an initial condition at $\tau = 0$. In the backward time variable $t$, the PDE would be $-\partial\phi/\partial t = \mathcal{L}\phi$ with a terminal condition at $t = T$. Both formulations are equivalent; we use the $\tau$ convention throughout the characteristic function chapter.

### Key Observations

Each term in the generator has a clear origin:

| PDE Term | SDE Origin | Coefficient |
|:---|:---|:---:|
| $(r-q-\frac{1}{2}v)\,\partial_x\phi$ | Log-price drift | Affine in $v$ |
| $\kappa(\theta-v)\,\partial_v\phi$ | Variance drift | Affine in $v$ |
| $\frac{1}{2}v\,\partial_{xx}\phi$ | Log-price diffusion squared | Linear in $v$ |
| $\rho\sigma_v v\,\partial_{xv}\phi$ | Cross-covariation | Linear in $v$ |
| $\frac{1}{2}\sigma_v^2 v\,\partial_{vv}\phi$ | Variance diffusion squared | Linear in $v$ |

Every coefficient is either constant or linear in $v$, and none depend on $x$. This is the affine property in PDE form.

---

## The Exponential-Affine Ansatz

### Statement

Because all PDE coefficients are at most affine in $v$ and independent of $x$, we seek a solution of the form:

$$
\phi(u, \tau; x, v) = \exp\!\bigl(C(\tau, u) + D(\tau, u)\,v + iu\,x\bigr)
$$

where $C$ and $D$ are complex-valued functions of $\tau$ and $u$, independent of the state $(x, v)$.

### Initial Conditions

At $\tau = 0$ (the observation time equals the maturity), $\phi(u, 0; x, v) = e^{iux}$, which requires:

$$
C(0, u) = 0, \qquad D(0, u) = 0
$$

### Substitution Strategy

Substituting the ansatz into the PDE and dividing by $\phi$ converts the PDE into an algebraic equation in $v$:

$$
C'(\tau, u) + D'(\tau, u)\,v = \text{terms involving } C, D, u \text{ and powers of } v
$$

Since this must hold for all $v \geq 0$, matching coefficients of $v^0$ and $v^1$ gives two ODEs: one for $C'$ and one for $D'$. This reduction from a PDE to ODEs is the core computational advantage of the affine approach.

The explicit derivation of these ODEs -- the Riccati system -- is carried out in the [next section](riccati_ode_system.md).

---

## Notation Summary for the CF Chapter

For convenience, we collect the notation used throughout the characteristic function derivation:

| Symbol | Meaning |
|:---|:---|
| $\phi(u, \tau; x, v)$ | Conditional characteristic function of $x_T$ |
| $C(\tau, u)$ | $v$-independent term in the exponent |
| $D(\tau, u)$ | Coefficient of $v$ in the exponent |
| $\tau = T - t$ | Time to maturity |
| $u \in \mathbb{R}$ | Fourier (transform) variable |
| $\gamma$ | Discriminant: $\gamma = \sqrt{(\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)}$ |
| $g$ | Ratio: $g = (\kappa - i\rho\sigma_v u - \gamma)/(\kappa - i\rho\sigma_v u + \gamma)$ |

---

## Summary

This section has collected the Heston bivariate SDE in log-price form, summarized the affine conditions that make the characteristic function tractable, defined the conditional characteristic function, written the Feynman-Kac PDE, and stated the exponential-affine ansatz with its initial conditions. The stage is set for the [Riccati ODE derivation](riccati_ode_system.md), where we substitute the ansatz into the PDE and extract the ODE system for $C(\tau, u)$ and $D(\tau, u)$.

---

---

## Exercises

**Exercise 1.** Write the Heston bivariate SDE in log-price form: $dx_t = (r - q - \frac{1}{2}v_t)\,dt + \sqrt{v_t}\,dW_t^{(1)}$ and $dv_t = \kappa(\theta - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t^{(2)}$ with $\operatorname{Corr}(dW^{(1)}, dW^{(2)}) = \rho\,dt$. Identify the drift vector and diffusion matrix as functions of the state $(x, v)$ and verify the affine property.

---

**Exercise 2.** The conditional characteristic function is defined as $\varphi(u, \tau; x, v) = \mathbb{E}[e^{iux_T} \mid x_t = x, v_t = v]$. Show that the initial condition is $\varphi(u, 0; x, v) = e^{iux}$ by setting $\tau = 0$.

---

**Exercise 3.** Write the Feynman-Kac PDE for $\varphi$ including all terms: the time derivative, the drift terms, the diffusion terms (including the cross-derivative $\rho\sigma_v v \frac{\partial^2 \varphi}{\partial x \partial v}$), and the discounting term. Verify that there are six terms in total.

---

**Exercise 4.** Substitute the exponential-affine ansatz $\varphi = \exp(C(\tau, u) + D(\tau, u)v + iux)$ into the PDE and show that the $x$-dependence cancels, leaving ODEs in $\tau$ only.

---

**Exercise 5.** State the initial conditions for the Riccati system: $C(0, u) = 0$ and $D(0, u) = 0$. Explain why these follow from $\varphi(u, 0; x, v) = e^{iux}$.
