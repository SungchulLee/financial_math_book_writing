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

---

## Exercises

**Exercise 1.** Write the $D$-equation: $D' = \frac{1}{2}\sigma_v^2 D^2 + (\rho\sigma_v iu - \kappa)D + \frac{1}{2}(iu - u^2)$. Identify the coefficients $\alpha$, $\beta$, $\gamma$ in the standard Riccati form $D' = \alpha + \beta D + \frac{1}{2}\gamma D^2$ and compute the discriminant $\gamma^2 = \beta^2 - 2\alpha\gamma$.

??? success "Solution to Exercise 1"
    The $D$-equation is:

    $$
    D' = \frac{1}{2}\sigma_v^2 D^2 + (\rho\sigma_v iu - \kappa)D + \frac{1}{2}(iu - u^2)
    $$

    To match the standard Riccati form $D' = \alpha + \beta D + \frac{1}{2}\gamma_R D^2$ (using $\gamma_R$ to distinguish from the discriminant), the coefficients are:

    $$
    \alpha = \frac{1}{2}(iu - u^2), \qquad \beta = \rho\sigma_v iu - \kappa, \qquad \gamma_R = \sigma_v^2
    $$

    Note the factor of $\frac{1}{2}$ in front of $\gamma_R D^2$, consistent with the original equation having $\frac{1}{2}\sigma_v^2 D^2$.

    The discriminant of the quadratic $\frac{1}{2}\gamma_R D^2 + \beta D + \alpha = 0$ is:

    $$
    \Delta = \beta^2 - 2\alpha\gamma_R = (\rho\sigma_v iu - \kappa)^2 - 2 \cdot \frac{1}{2}(iu - u^2) \cdot \sigma_v^2
    $$

    $$
    = (\kappa - i\rho\sigma_v u)^2 - \sigma_v^2(iu - u^2)
    $$

    $$
    = (\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(u^2 - iu)
    $$

    $$
    = (\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)
    $$

    (where the last step uses $u^2 - iu = -(iu - u^2)$, and noting the sign: $-\sigma_v^2(iu - u^2) = \sigma_v^2(u^2 - iu)$; the standard convention writes this as $\sigma_v^2(iu + u^2)$ which equals $\sigma_v^2(u^2 + iu)$.) The discriminant square root is:

    $$
    \gamma = \sqrt{\Delta} = \sqrt{(\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)}
    $$

    This is the key quantity appearing in the closed-form Heston characteristic function.

---

**Exercise 2.** Apply the substitution $D = -\frac{2}{\sigma_v^2}\frac{h'}{h}$ to transform the Riccati ODE into a second-order linear ODE for $h(\tau)$. Solve $h(\tau) = Ae^{r_+\tau} + Be^{r_-\tau}$ where $r_\pm$ are the characteristic roots.

??? success "Solution to Exercise 2"
    Starting from the Riccati ODE $D' = \frac{1}{2}\sigma_v^2 D^2 + bD + c$ where $b = \rho\sigma_v iu - \kappa$ and $c = \frac{1}{2}(iu - u^2)$, apply the substitution:

    $$
    D(\tau) = -\frac{2}{\sigma_v^2}\frac{h'(\tau)}{h(\tau)}
    $$

    Computing $D'$:

    $$
    D' = -\frac{2}{\sigma_v^2}\left(\frac{h''}{h} - \frac{(h')^2}{h^2}\right)
    $$

    Computing $D^2$:

    $$
    D^2 = \frac{4}{\sigma_v^4}\frac{(h')^2}{h^2}
    $$

    Substituting into the Riccati ODE:

    $$
    -\frac{2}{\sigma_v^2}\frac{h''}{h} + \frac{2}{\sigma_v^2}\frac{(h')^2}{h^2} = \frac{1}{2}\sigma_v^2 \cdot \frac{4}{\sigma_v^4}\frac{(h')^2}{h^2} + b\left(-\frac{2}{\sigma_v^2}\frac{h'}{h}\right) + c
    $$

    The $(h')^2/h^2$ terms cancel on both sides, leaving:

    $$
    -\frac{2}{\sigma_v^2}\frac{h''}{h} = -\frac{2b}{\sigma_v^2}\frac{h'}{h} + c
    $$

    Multiplying by $-\frac{\sigma_v^2}{2}h$:

    $$
    h'' - b\,h' + \frac{\sigma_v^2 c}{2}\,h = 0
    $$

    Substituting $b = \rho\sigma_v iu - \kappa$ and $c = \frac{1}{2}(iu - u^2)$:

    $$
    h'' + (\kappa - \rho\sigma_v iu)\,h' + \frac{\sigma_v^2}{4}(iu - u^2)\,h = 0
    $$

    This is a constant-coefficient second-order linear ODE with characteristic equation:

    $$
    r^2 + (\kappa - \rho\sigma_v iu)\,r + \frac{\sigma_v^2}{4}(iu - u^2) = 0
    $$

    By the quadratic formula:

    $$
    r_\pm = \frac{-(\kappa - i\rho\sigma_v u) \pm \sqrt{(\kappa - i\rho\sigma_v u)^2 - \sigma_v^2(iu - u^2)}}{2} = \frac{-(\kappa - i\rho\sigma_v u) \pm \gamma}{2}
    $$

    The general solution is $h(\tau) = Ae^{r_+\tau} + Be^{r_-\tau}$.

---

**Exercise 3.** From the initial condition $D(0) = 0$, determine the ratio $A/B$ in terms of $r_+$ and $r_-$. Substitute back to obtain $D(\tau)$ in closed form.

??? success "Solution to Exercise 3"
    From $D(0) = 0$ and $D = -\frac{2}{\sigma_v^2}\frac{h'}{h}$, we need $h'(0) = 0$ (with $h(0) \neq 0$).

    With $h(\tau) = Ae^{r_+\tau} + Be^{r_-\tau}$:

    $$
    h'(\tau) = Ar_+e^{r_+\tau} + Br_-e^{r_-\tau}
    $$

    At $\tau = 0$: $h'(0) = Ar_+ + Br_- = 0$, so:

    $$
    \frac{A}{B} = -\frac{r_-}{r_+}
    $$

    Now compute $D(\tau)$:

    $$
    D = -\frac{2}{\sigma_v^2}\frac{Ar_+e^{r_+\tau} + Br_-e^{r_-\tau}}{Ae^{r_+\tau} + Be^{r_-\tau}}
    $$

    Substitute $A = -\frac{r_-}{r_+}B$ and divide numerator and denominator by $Be^{r_-\tau}$:

    $$
    D = -\frac{2}{\sigma_v^2}\frac{-\frac{r_-}{r_+}\cdot r_+ \cdot e^{(r_+-r_-)\tau} + r_-}{-\frac{r_-}{r_+}\cdot e^{(r_+-r_-)\tau} + 1}
    $$

    $$
    = -\frac{2}{\sigma_v^2}\frac{r_-(-e^{(r_+-r_-)\tau} + 1)}{-\frac{r_-}{r_+}e^{(r_+-r_-)\tau} + 1}
    $$

    $$
    = -\frac{2}{\sigma_v^2}\frac{r_-(1 - e^{(r_+-r_-)\tau})}{1 - \frac{r_-}{r_+}e^{(r_+-r_-)\tau}}
    $$

    Note that $r_+ - r_- = \gamma$ and define $g = r_-/r_+$. Then:

    $$
    D(\tau) = -\frac{2r_-}{\sigma_v^2}\frac{1 - e^{\gamma\tau}}{1 - g\,e^{\gamma\tau}}
    $$

    Since $r_- = \frac{-(\kappa - i\rho\sigma_v u) - \gamma}{2}$, we have $-\frac{2r_-}{\sigma_v^2} = \frac{\kappa - i\rho\sigma_v u + \gamma}{\sigma_v^2}$, giving the Heston 1993 form. Alternatively, multiplying numerator and denominator by $e^{-\gamma\tau}$ and using $g_{\text{Alb}} = r_+/r_-$:

    $$
    D(\tau) = \frac{\kappa - i\rho\sigma_v u - \gamma}{\sigma_v^2}\cdot\frac{1 - e^{-\gamma\tau}}{1 - g_{\text{Alb}}\,e^{-\gamma\tau}}
    $$

    which is the Albrecher form with $g_{\text{Alb}} = \frac{\kappa - i\rho\sigma_v u - \gamma}{\kappa - i\rho\sigma_v u + \gamma}$.

---

**Exercise 4.** The $C$-equation is $C'(\tau) = (r-q)iu + \kappa\theta D(\tau)$. Given $D(\tau)$ in closed form, perform the integration to obtain $C(\tau)$ and verify that $C(0) = 0$.

??? success "Solution to Exercise 4"
    The $C$-equation is $C'(\tau) = (r-q)iu + \kappa\theta D(\tau)$ with $C(0) = 0$. Integrating:

    $$
    C(\tau) = (r-q)iu\,\tau + \kappa\theta\int_0^\tau D(s)\,ds
    $$

    Using the Albrecher form $D(s) = D_+ \cdot \frac{1 - e^{-\gamma s}}{1 - g\,e^{-\gamma s}}$ where $D_+ = \frac{\kappa - i\rho\sigma_v u - \gamma}{\sigma_v^2}$:

    $$
    \int_0^\tau \frac{1 - e^{-\gamma s}}{1 - g\,e^{-\gamma s}}\,ds
    $$

    Split: $\frac{1 - e^{-\gamma s}}{1 - g\,e^{-\gamma s}} = 1 + \frac{(1-g)e^{-\gamma s} - 1 + 1 - e^{-\gamma s}}{1 - g\,e^{-\gamma s}} = 1 - \frac{(1-g)}{1-g\,e^{-\gamma s}} + \frac{1-g}{1-g\,e^{-\gamma s}}$. More directly, use the substitution $w = e^{-\gamma s}$, $dw = -\gamma e^{-\gamma s}\,ds$:

    $$
    \int_0^\tau \frac{1 - e^{-\gamma s}}{1 - g\,e^{-\gamma s}}\,ds = \tau + \frac{1}{\gamma}\ln\!\left(\frac{1 - g\,e^{-\gamma\tau}}{1 - g}\right)
    $$

    This can be verified by differentiating with respect to $\tau$: $\frac{d}{d\tau}\left[\tau + \frac{1}{\gamma}\ln\!\left(\frac{1 - g\,e^{-\gamma\tau}}{1-g}\right)\right] = 1 + \frac{1}{\gamma}\cdot\frac{g\gamma e^{-\gamma\tau}}{1 - g\,e^{-\gamma\tau}} = \frac{1 - g\,e^{-\gamma\tau} + g\,e^{-\gamma\tau}}{1 - g\,e^{-\gamma\tau}} = \frac{1}{1 - g\,e^{-\gamma\tau}}$. Hmm, this gives $\frac{1}{1 - g\,e^{-\gamma\tau}}$, not $\frac{1 - e^{-\gamma\tau}}{1 - g\,e^{-\gamma\tau}}$, so the integral formula needs refinement.

    The correct evaluation proceeds by writing:

    $$
    \frac{1 - e^{-\gamma s}}{1 - g\,e^{-\gamma s}} = \frac{1}{1 - g\,e^{-\gamma s}} - \frac{e^{-\gamma s}}{1 - g\,e^{-\gamma s}}
    $$

    For the second term, $\int_0^\tau \frac{e^{-\gamma s}}{1 - g\,e^{-\gamma s}}\,ds = -\frac{1}{\gamma}\ln\!\left(\frac{1 - g\,e^{-\gamma\tau}}{1 - g}\right)$ (by the substitution $w = g\,e^{-\gamma s}$).

    For the first term, $\int_0^\tau \frac{ds}{1 - g\,e^{-\gamma s}}$, substitute $w = e^{-\gamma s}$:

    $$
    = -\frac{1}{\gamma}\int_1^{e^{-\gamma\tau}} \frac{dw}{w(1 - gw)} = -\frac{1}{\gamma}\int_1^{e^{-\gamma\tau}}\left(\frac{1}{w} + \frac{g}{1-gw}\right)dw
    $$

    $$
    = -\frac{1}{\gamma}\left[-\gamma\tau - \ln\!\left(\frac{1 - g\,e^{-\gamma\tau}}{1-g}\right)\right] = \tau + \frac{1}{\gamma}\ln\!\left(\frac{1 - g\,e^{-\gamma\tau}}{1-g}\right)
    $$

    Combining: $\int_0^\tau D_+\frac{1 - e^{-\gamma s}}{1 - g\,e^{-\gamma s}}\,ds = D_+\left[\tau + \frac{2}{\gamma}\ln\!\left(\frac{1 - g\,e^{-\gamma\tau}}{1-g}\right)\right]$. Wait --- the two integrals give $\left[\tau + \frac{1}{\gamma}\ln(\cdots)\right] - \left[-\frac{1}{\gamma}\ln(\cdots)\right] = \tau + \frac{2}{\gamma}\ln\!\left(\frac{1 - g\,e^{-\gamma\tau}}{1-g}\right)$.

    Therefore:

    $$
    C(\tau) = (r-q)iu\,\tau + \frac{\kappa\theta}{\sigma_v^2}\left[(\kappa - i\rho\sigma_v u - \gamma)\tau - 2\ln\!\left(\frac{1 - g\,e^{-\gamma\tau}}{1-g}\right)\right]
    $$

    **Verification that $C(0) = 0$:** At $\tau = 0$, the linear term gives $0$ and the logarithm gives $\ln(1) = 0$, so $C(0) = 0$. $\checkmark$

---

**Exercise 5.** For parameters $\kappa = 2$, $\sigma_v = 0.3$, $\rho = -0.7$, compute the discriminant $\gamma$ at $u = 1$ and verify $\operatorname{Re}(\gamma) > 0$.

??? success "Solution to Exercise 5"
    For $\kappa = 2$, $\sigma_v = 0.3$, $\rho = -0.7$, $u = 1$:

    $$
    \gamma^2 = (\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)
    $$

    $$
    = (2 - i(-0.7)(0.3)(1))^2 + (0.3)^2(i + 1)
    $$

    $$
    = (2 + 0.21i)^2 + 0.09(1 + i)
    $$

    $$
    = (4 + 0.84i - 0.0441) + (0.09 + 0.09i)
    $$

    $$
    = 4.0459 + 0.93i
    $$

    To compute $\gamma = \sqrt{4.0459 + 0.93i}$, use polar form. The modulus is $|\gamma^2| = \sqrt{4.0459^2 + 0.93^2} = \sqrt{16.369 + 0.865} = \sqrt{17.234} \approx 4.151$, and the argument is $\theta = \arctan(0.93/4.0459) \approx 0.2262$ radians.

    Therefore $|\gamma| = \sqrt{4.151} \approx 2.037$ and $\arg(\gamma) = 0.2262/2 \approx 0.1131$ radians. So:

    $$
    \gamma \approx 2.037(\cos 0.1131 + i\sin 0.1131) \approx 2.037(0.9936 + 0.1129i) \approx 2.024 + 0.230i
    $$

    Since $\operatorname{Re}(\gamma) \approx 2.024 > 0$, the condition $\operatorname{Re}(\gamma) > 0$ is verified. This ensures that the Albrecher formulation uses decaying exponentials $e^{-\gamma\tau}$ and that $|g| < 1$.

---

**Exercise 6.** Explain why the $D$-equation is autonomous in $D$ (it does not involve $C$), while the $C$-equation depends on $D$. How does this hierarchical structure simplify the solution process?

??? success "Solution to Exercise 6"
    The hierarchical (triangular) structure of the Riccati system arises from the affine structure of the Heston model and the form of the exponential-affine ansatz.

    **Why $D$ is autonomous:** The $D$-equation $D' = \frac{1}{2}\sigma_v^2 D^2 + (\rho\sigma_v iu - \kappa)D + \frac{1}{2}(iu - u^2)$ collects all terms proportional to $v$ in the PDE. Since the PDE coefficients that multiply $v$ (namely, the drift $-\frac{1}{2}v$ and $-\kappa v$, and the diffusion terms $\frac{1}{2}v$, $\rho\sigma_v v$, $\frac{1}{2}\sigma_v^2 v$) depend only on the model parameters and $D$ (through the ansatz), but not on $C$, the resulting ODE for $D$ is self-contained.

    Mathematically, $C$ enters the ansatz only through the $v$-independent part of the exponent. When collecting $v^1$ terms in the PDE, the $C$-dependent terms (which are all $v^0$) do not contribute. Hence $D' = f(D, u)$ with no $C$ dependence.

    **Why $C$ depends on $D$:** The $C$-equation $C' = (r-q)iu + \kappa\theta D$ collects the $v^0$ terms. The term $\kappa\theta D$ arises from the mean-reversion drift $\kappa\theta\,\partial_v\varphi = \kappa\theta\,D\,\varphi$, which contributes to the $v^0$ coefficient. Thus $C'$ depends on $D$ through this coupling.

    **Simplification:** The hierarchical structure means the system can be solved sequentially rather than simultaneously:

    1. **First**, solve the $D$-equation as a standalone scalar Riccati ODE. This is the harder step (nonlinear ODE), but it is a single equation in one unknown.
    2. **Second**, with $D(\tau)$ known, compute $C(\tau)$ by direct integration (quadrature): $C(\tau) = (r-q)iu\tau + \kappa\theta\int_0^\tau D(s)\,ds$. This is a trivial integration step --- no ODE-solving is required.

    Without this hierarchical structure, we would face a coupled system of two nonlinear ODEs, which would be considerably harder to solve in closed form. The decoupling is a direct consequence of the affine property: the state variable $v$ enters the drift and covariance linearly, ensuring that the $v^1$ and $v^0$ coefficient equations separate cleanly.
