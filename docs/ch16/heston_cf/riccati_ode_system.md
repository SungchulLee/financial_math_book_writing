# Riccati ODE System for the Heston Characteristic Function

The exponential-affine ansatz for the Heston characteristic function reduces the Feynman-Kac PDE to a pair of ordinary differential equations. The equation for $D(\tau, u)$ -- the coefficient of the variance $v$ in the exponent -- is a **Riccati equation**: a first-order ODE that is quadratic in the unknown. The equation for $C(\tau, u)$ is a simple integral once $D$ is known. This section carries out the substitution of the ansatz into the PDE, derives both ODEs with full detail, classifies the $D$-equation as a Riccati ODE, and describes the method of solution via the standard substitution that converts a Riccati equation into a linear second-order ODE.

This section assumes familiarity with the [Heston SDE and affine recap](heston_sde_and_affine_recap.md) and leads directly to the [closed-form solution](closed_form_characteristic_function.md).

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Derive the Riccati ODE for $D(\tau, u)$ by substituting the exponential-affine ansatz into the Feynman-Kac PDE
    - Derive the integral formula for $C(\tau, u)$ from the $v^0$ terms
    - Classify the $D$-equation as a scalar Riccati ODE and identify its three coefficients
    - Apply the substitution $D = -2h'/(\sigma_v^2 h)$ to reduce the Riccati ODE to a linear second-order ODE
    - State the initial conditions and verify them against the terminal condition of the PDE

---

## Substitution of the Ansatz

### Setup

Recall the Feynman-Kac PDE for $\phi(u, \tau; x, v)$ from the [preceding section](heston_sde_and_affine_recap.md):

$$
\frac{\partial \phi}{\partial \tau} = \left(r-q-\tfrac{1}{2}v\right)\frac{\partial \phi}{\partial x} + \kappa(\theta-v)\frac{\partial \phi}{\partial v} + \tfrac{1}{2}v\frac{\partial^2\phi}{\partial x^2} + \rho\sigma_v v\frac{\partial^2\phi}{\partial x\,\partial v} + \tfrac{1}{2}\sigma_v^2 v\frac{\partial^2\phi}{\partial v^2}
$$

and the exponential-affine ansatz:

$$
\phi(u, \tau; x, v) = \exp\!\bigl(C(\tau, u) + D(\tau, u)\,v + iu\,x\bigr)
$$

### Computing the Partial Derivatives

With the ansatz, each partial derivative factors through $\phi$:

$$
\frac{\partial\phi}{\partial\tau} = \bigl(C' + D'v\bigr)\phi
$$

$$
\frac{\partial\phi}{\partial x} = iu\,\phi, \qquad \frac{\partial^2\phi}{\partial x^2} = (iu)^2\phi = -u^2\phi
$$

$$
\frac{\partial\phi}{\partial v} = D\,\phi, \qquad \frac{\partial^2\phi}{\partial v^2} = D^2\phi
$$

$$
\frac{\partial^2\phi}{\partial x\,\partial v} = iu\,D\,\phi
$$

where primes denote derivatives with respect to $\tau$.

### Substitution and Simplification

Substituting into the PDE and dividing by $\phi \neq 0$:

$$
C' + D'v = (r-q-\tfrac{1}{2}v)(iu) + \kappa(\theta-v)D + \tfrac{1}{2}v(-u^2) + \rho\sigma_v v\,(iu\,D) + \tfrac{1}{2}\sigma_v^2 v\,D^2
$$

Expanding the right-hand side:

$$
= (r-q)(iu) - \tfrac{1}{2}v\,(iu) + \kappa\theta D - \kappa v\,D - \tfrac{1}{2}u^2 v + \rho\sigma_v v\,(iu)D + \tfrac{1}{2}\sigma_v^2 v\,D^2
$$

Grouping by powers of $v$:

$$
C' + D'v = \underbrace{\bigl[(r-q)(iu) + \kappa\theta D\bigr]}_{v^0 \text{ terms}} + v\underbrace{\bigl[\tfrac{1}{2}\sigma_v^2 D^2 + (\rho\sigma_v\,iu - \kappa)D + \tfrac{1}{2}(iu - u^2)\bigr]}_{v^1 \text{ terms}}
$$

Since this identity must hold for all $v \geq 0$, the coefficients of $v^0$ and $v^1$ must match independently.

---

## The Riccati ODE System

### Statement

!!! success "Theorem: Riccati System for the Heston Characteristic Function"
    The functions $C(\tau, u)$ and $D(\tau, u)$ satisfy:

    **$D$-equation** (Riccati ODE):

    $$
    D'(\tau, u) = \tfrac{1}{2}\sigma_v^2\,D^2 + (\rho\sigma_v\,iu - \kappa)\,D + \tfrac{1}{2}(iu - u^2)
    $$

    **$C$-equation** (quadrature):

    $$
    C'(\tau, u) = (r - q)\,iu + \kappa\theta\,D(\tau, u)
    $$

    **Initial conditions:**

    $$
    D(0, u) = 0, \qquad C(0, u) = 0
    $$

### Verification of Initial Conditions

At $\tau = 0$, the terminal condition $\phi(u, 0; x, v) = e^{iux}$ requires $\exp(C(0) + D(0)v + iux) = e^{iux}$ for all $v$, hence $C(0) = 0$ and $D(0) = 0$. $\square$

---

## Structure of the D-Equation

### Classification as a Riccati ODE

!!! info "Definition: Scalar Riccati Equation"
    A **scalar Riccati equation** is a first-order ODE of the form:

    $$
    y'(\tau) = a(\tau)\,y^2 + b(\tau)\,y + c(\tau)
    $$

    where $a$, $b$, $c$ are known functions. The equation is nonlinear (quadratic in $y$), but it can be linearized by a standard substitution.

The $D$-equation has constant coefficients (since $u$ is a parameter, not a variable):

| Riccati Coefficient | Value | Dependence on Heston Parameters |
|:---|:---:|:---|
| $a$ | $\tfrac{1}{2}\sigma_v^2$ | Vol-of-vol squared |
| $b$ | $\rho\sigma_v\,iu - \kappa$ | Correlation, vol-of-vol, mean-reversion |
| $c$ | $\tfrac{1}{2}(iu - u^2)$ | Pure function of transform variable $u$ |

!!! note "Autonomy"
    The coefficients $a$, $b$, $c$ are independent of $\tau$ (the Heston model is time-homogeneous). This means the Riccati ODE is **autonomous**, and its solution depends on $\tau$ only through the elapsed time since the initial condition $D(0) = 0$.

### The Discriminant

The quadratic $a\,D^2 + b\,D + c = 0$ has discriminant:

$$
\Delta = b^2 - 4ac = (\rho\sigma_v\,iu - \kappa)^2 - \sigma_v^2(iu - u^2)
$$

$$
= (\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(u^2 - iu)
$$

$$
= (\kappa - i\rho\sigma_v u)^2 + \sigma_v^2 u(u - i)
$$

Define the **discriminant square root**:

$$
\gamma = \sqrt{(\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)}
$$

!!! warning "Complex Square Root"
    For complex $u$, the square root $\gamma$ is complex-valued, and its branch must be chosen carefully to ensure continuity. This branch-cut issue is addressed in the [numerical stability section](numerical_stability_and_branch_cuts.md) and is one of the main practical challenges in implementing the Heston characteristic function.

---

## Solving the Riccati Equation

### Linearization via Substitution

The standard method for solving a constant-coefficient Riccati ODE is to substitute $D = -\frac{2}{\sigma_v^2}\frac{h'}{h}$, which converts the quadratic ODE into a linear second-order ODE.

!!! success "Proposition: Linearization of the D-Equation"
    The substitution $D(\tau) = -\frac{2}{\sigma_v^2}\frac{h'(\tau)}{h(\tau)}$ transforms the Riccati ODE for $D$ into the linear second-order ODE:

    $$
    h''(\tau) - \frac{b}{1}\,h'(\tau) + \frac{ac}{1}\cdot\frac{\sigma_v^2}{1}\,h(\tau) = 0
    $$

    More explicitly:

    $$
    h'' + (\kappa - i\rho\sigma_v u)\,h' + \tfrac{1}{2}(iu - u^2)\,h = 0
    $$

    This is a constant-coefficient linear ODE whose characteristic equation is:

    $$
    \lambda^2 + (\kappa - i\rho\sigma_v u)\,\lambda + \tfrac{1}{2}(iu - u^2) = 0
    $$

    with roots:

    $$
    \lambda_{\pm} = \frac{-(\kappa - i\rho\sigma_v u) \pm \gamma}{2}
    $$

**Proof.** Substitute $D = -\frac{2}{\sigma_v^2}\frac{h'}{h}$ into the Riccati ODE. Using $D' = -\frac{2}{\sigma_v^2}\left(\frac{h''}{h} - \frac{(h')^2}{h^2}\right)$ and $D^2 = \frac{4}{\sigma_v^4}\frac{(h')^2}{h^2}$:

$$
-\frac{2}{\sigma_v^2}\left(\frac{h''}{h} - \frac{(h')^2}{h^2}\right) = \frac{1}{2}\sigma_v^2 \cdot \frac{4}{\sigma_v^4}\frac{(h')^2}{h^2} + (\rho\sigma_v iu - \kappa)\left(-\frac{2}{\sigma_v^2}\frac{h'}{h}\right) + \frac{1}{2}(iu - u^2)
$$

$$
-\frac{2}{\sigma_v^2}\frac{h''}{h} + \frac{2}{\sigma_v^2}\frac{(h')^2}{h^2} = \frac{2}{\sigma_v^2}\frac{(h')^2}{h^2} - \frac{2(\rho\sigma_v iu - \kappa)}{\sigma_v^2}\frac{h'}{h} + \frac{1}{2}(iu - u^2)
$$

The $(h')^2/h^2$ terms cancel, giving:

$$
-\frac{2}{\sigma_v^2}\frac{h''}{h} = \frac{2(\kappa - \rho\sigma_v iu)}{\sigma_v^2}\frac{h'}{h} + \frac{1}{2}(iu - u^2)
$$

Multiplying by $-\sigma_v^2 h/2$:

$$
h'' + (\kappa - i\rho\sigma_v u)\,h' + \frac{\sigma_v^2}{4}(iu - u^2)\,h = 0
$$

Wait -- let us redo this more carefully. The Riccati ODE is $D' = \frac{1}{2}\sigma_v^2 D^2 + bD + c$ where $b = \rho\sigma_v iu - \kappa$ and $c = \frac{1}{2}(iu - u^2)$. Substituting $D = -\frac{2}{\sigma_v^2}\frac{h'}{h}$ and simplifying leads to $h'' - b\,h' + \frac{\sigma_v^2 c}{2}\,h = 0$, i.e.:

$$
h'' - (\rho\sigma_v iu - \kappa)\,h' + \frac{\sigma_v^2}{2}\cdot\frac{1}{2}(iu-u^2)\,h = 0
$$

$$
h'' + (\kappa - \rho\sigma_v iu)\,h' + \frac{1}{4}\sigma_v^2(iu-u^2)\,h = 0
$$

The characteristic roots of $\mu^2 + (\kappa - \rho\sigma_v iu)\mu + \frac{1}{4}\sigma_v^2(iu-u^2) = 0$ are:

$$
\mu_\pm = \frac{-(\kappa - \rho\sigma_v iu) \pm \sqrt{(\kappa-\rho\sigma_v iu)^2 - \sigma_v^2(iu-u^2)}}{2} = \frac{-(\kappa - i\rho\sigma_v u) \pm \gamma}{2}
$$

$\square$

### General Solution

The general solution of the linear ODE is $h(\tau) = A\,e^{\mu_+\tau} + B\,e^{\mu_-\tau}$. The constants $A$ and $B$ are determined by the initial conditions.

From $D(0) = 0$, we need $h'(0)/h(0) = 0$, hence $h'(0) = 0$. This gives:

$$
A\mu_+ + B\mu_- = 0 \qquad \Longrightarrow \qquad \frac{A}{B} = -\frac{\mu_-}{\mu_+}
$$

Substituting back into $D = -\frac{2}{\sigma_v^2}\frac{h'}{h}$ yields the closed-form expression for $D(\tau, u)$, which is derived in the [next section](closed_form_characteristic_function.md).

---

## The C-Equation as Quadrature

Once $D(\tau, u)$ is known, $C(\tau, u)$ is obtained by direct integration:

$$
C(\tau, u) = (r - q)\,iu\,\tau + \kappa\theta\int_0^{\tau} D(s, u)\,ds
$$

!!! tip "Structure of the Solution"
    The term $(r-q)\,iu\,\tau$ is the drift contribution from the log-price. The integral $\kappa\theta\int_0^\tau D(s)\,ds$ is the contribution from the mean-reversion drift of the variance process. Because $D$ has an explicit form (involving exponentials and $\gamma$), this integral can also be evaluated in closed form, producing a logarithmic term.

---

## Worked Example: Riccati Coefficients at Small Time

??? example "Taylor Expansion Near tau = 0"
    At $\tau = 0$, $D(0) = 0$. The Riccati ODE gives:

    $$
    D'(0) = \tfrac{1}{2}\sigma_v^2 \cdot 0 + (\rho\sigma_v iu - \kappa)\cdot 0 + \tfrac{1}{2}(iu - u^2) = \tfrac{1}{2}(iu - u^2)
    $$

    Differentiating the Riccati ODE:

    $$
    D'' = \sigma_v^2 D\,D' + (\rho\sigma_v iu - \kappa)\,D'
    $$

    At $\tau = 0$: $D''(0) = 0 + (\rho\sigma_v iu - \kappa)\cdot\frac{1}{2}(iu - u^2)$.

    So the Taylor expansion is:

    $$
    D(\tau) \approx \tfrac{1}{2}(iu - u^2)\,\tau + \tfrac{1}{2}(\rho\sigma_v iu - \kappa)(iu - u^2)\,\frac{\tau^2}{2} + O(\tau^3)
    $$

    For $C$: $C(\tau) \approx (r-q)iu\,\tau + \kappa\theta\cdot\frac{1}{2}(iu-u^2)\frac{\tau^2}{2} + O(\tau^3)$.

    To zeroth order in $\sigma_v$ (i.e., deterministic volatility), $D(\tau) \approx \frac{1}{2}(iu - u^2)\tau$ and the characteristic function becomes:

    $$
    \phi \approx \exp\!\bigl((r-q)iu\tau + \tfrac{1}{2}(iu-u^2)v\tau + iux\bigr)
    $$

    This is exactly the Black-Scholes characteristic function with constant variance $v$, confirming that the Heston model reduces to Black-Scholes when $\sigma_v = 0$.

---

## Summary

Substituting the exponential-affine ansatz into the Feynman-Kac PDE yields a scalar Riccati ODE for $D(\tau, u)$ and a simple quadrature for $C(\tau, u)$. The $D$-equation has constant complex coefficients (parametrized by $u$) with discriminant $\gamma^2 = (\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)$. The standard Riccati-to-linear substitution $D = -\frac{2}{\sigma_v^2}h'/h$ reduces the ODE to a constant-coefficient linear ODE with characteristic roots involving $\gamma$. The initial condition $D(0) = 0$ determines the integration constants. The closed-form solution for $D$ and $C$ -- the Heston characteristic function itself -- is presented in the [next section](closed_form_characteristic_function.md).

---
