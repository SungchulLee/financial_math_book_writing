# Derivation via Riccati Equations

The named functions $A(t,T)$ and $B(t,T)$ that define the Hull-White bond price $P(t,T) = e^{A(t,T) + B(t,T) r_t}$ are not guessed or postulated; they arise systematically from solving the bond pricing PDE with an exponential-affine ansatz. The substitution reduces the PDE to a system of ordinary differential equations, with $B$ satisfying a Riccati equation (which in the Hull-White case is linear) and $A$ determined by a subsequent quadrature. This section carries out the derivation step by step, solves both ODEs explicitly, and connects the solutions to the named functions collected in the reference section.

!!! info "Prerequisites"
    - Hull-White SDE: $dr_t = [\theta(t) - ar_t]\, dt + \sigma\, dW_t$
    - Bond pricing PDE from Feynman-Kac theorem
    - Ordinary differential equations: integrating factor, variation of constants
    - Named functions definition (sibling section)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Set up the bond pricing PDE for the Hull-White model
    2. Substitute the exponential-affine ansatz and separate variables
    3. Derive the Riccati ODE for $B(\tau)$ and solve it
    4. Derive the ODE for $A(\tau)$ and solve it as a quadrature
    5. Express the complete bond price in terms of market observables

---

## Bond Pricing PDE

The zero-coupon bond price $P(t,T)$ satisfies the backward Kolmogorov equation with discounting.

!!! note "Theorem: Hull-White Bond Pricing PDE"
    Under the Hull-White model, the ZCB price satisfies

    $$
    \frac{\partial P}{\partial t} + [\theta(t) - ar]\,\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2\,\frac{\partial^2 P}{\partial r^2} - rP = 0
    $$

    with terminal condition $P(T,T) = 1$.

???+ note "Derivation"
    By the Feynman-Kac theorem, $P(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\, ds} \mid r_t = r]$ satisfies the PDE

    $$
    \frac{\partial P}{\partial t} + \mu(t,r)\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2(t,r)\frac{\partial^2 P}{\partial r^2} - rP = 0
    $$

    where $\mu(t,r) = \theta(t) - ar$ is the drift and $\sigma^2(t,r) = \sigma^2$ is the diffusion coefficient of the Hull-White model. The terminal condition $P(T,T) = 1$ states that a zero-coupon bond pays \$1 at maturity. $\square$

---

## The Exponential-Affine Ansatz

We seek a solution of the form:

!!! note "Ansatz"
    Assume the bond price has the exponential-affine form

    $$
    P(t,T) = \exp\!\bigl(A(t,T) + B(t,T)\, r\bigr)
    $$

    where $A(t,T)$ and $B(t,T)$ are functions to be determined, with $A(T,T) = 0$ and $B(T,T) = 0$.

The motivation for this ansatz comes from the general theory of affine term structure models: when the drift is affine in $r$ and the diffusion coefficient is independent of $r$ (or affine in $r$), the bond price PDE separates cleanly.

---

## Substitution into the PDE

Compute the partial derivatives of $P = e^{A + Br}$:

$$
\frac{\partial P}{\partial t} = \left(\frac{\partial A}{\partial t} + \frac{\partial B}{\partial t}\, r\right)P
$$

$$
\frac{\partial P}{\partial r} = B\, P
$$

$$
\frac{\partial^2 P}{\partial r^2} = B^2\, P
$$

Substitute into the PDE and divide by $P$ (which is strictly positive):

$$
\frac{\partial A}{\partial t} + \frac{\partial B}{\partial t}\, r + [\theta(t) - ar]\, B + \frac{1}{2}\sigma^2 B^2 - r = 0
$$

Rearranging by powers of $r$:

$$
\left(\frac{\partial B}{\partial t} - aB - 1\right)r + \left(\frac{\partial A}{\partial t} + \theta(t)B + \frac{1}{2}\sigma^2 B^2\right) = 0
$$

Since this must hold for **all** values of $r$, both the coefficient of $r$ and the constant term must vanish independently.

---

## The Riccati ODE for B

Setting the coefficient of $r$ to zero:

!!! note "Theorem: Riccati Equation for $B$"
    The function $B(t,T)$ satisfies the ordinary differential equation

    $$
    \frac{\partial B}{\partial t}(t,T) = aB(t,T) + 1, \qquad B(T,T) = 0
    $$

    This is a linear first-order ODE (a degenerate Riccati equation, since no $B^2$ term appears).

**Change of variables.** It is convenient to work with $\tau = T - t$ (time to maturity). Writing $\tilde{B}(\tau) = B(t,T)$ and noting $\frac{\partial B}{\partial t} = -\frac{d\tilde{B}}{d\tau}$:

$$
-\frac{d\tilde{B}}{d\tau} = a\tilde{B} + 1, \qquad \tilde{B}(0) = 0
$$

or equivalently

$$
\frac{d\tilde{B}}{d\tau} = -a\tilde{B} - 1, \qquad \tilde{B}(0) = 0
$$

!!! note "Theorem: Solution for $B(\tau)$"

    $$
    B(\tau) = -\frac{1 - e^{-a\tau}}{a}
    $$

???+ note "Proof"
    The ODE $\tilde{B}' = -a\tilde{B} - 1$ is linear. Using the integrating factor $e^{a\tau}$:

    $$
    \frac{d}{d\tau}\bigl(e^{a\tau}\tilde{B}\bigr) = e^{a\tau}\tilde{B}' + ae^{a\tau}\tilde{B} = e^{a\tau}(-a\tilde{B} - 1) + ae^{a\tau}\tilde{B} = -e^{a\tau}
    $$

    Integrating from $0$ to $\tau$:

    $$
    e^{a\tau}\tilde{B}(\tau) - \tilde{B}(0) = -\int_0^{\tau} e^{as}\, ds = -\frac{e^{a\tau} - 1}{a}
    $$

    Since $\tilde{B}(0) = 0$:

    $$
    \tilde{B}(\tau) = -\frac{e^{a\tau} - 1}{a}\, e^{-a\tau} = -\frac{1 - e^{-a\tau}}{a}
    $$

    $\square$

**Key properties of $B(\tau)$:**

- $B(0) = 0$ (terminal condition satisfied)
- $B(\tau) < 0$ for all $\tau > 0$ (bond prices decrease when rates increase)
- $B(\tau) \to -1/a$ as $\tau \to \infty$ (bounded effective duration)
- $B(\tau) \approx -\tau$ for $a\tau \ll 1$ (recovers Macaulay duration for short maturities)
- $|B(\tau)| = (1 - e^{-a\tau})/a$ is the standard duration-like function

---

## The ODE for A

Setting the constant term to zero:

!!! note "Theorem: ODE for $A$"
    The function $A(t,T)$ satisfies

    $$
    \frac{\partial A}{\partial t}(t,T) = -\theta(t)\, B(t,T) - \frac{1}{2}\sigma^2\, B(t,T)^2, \qquad A(T,T) = 0
    $$

In the $\tau$ variable, writing $\tilde{A}(\tau; T) = A(t,T) = A(T-\tau, T)$:

$$
\frac{d\tilde{A}}{d\tau} = \theta(T-\tau)\, B(\tau) + \frac{1}{2}\sigma^2\, B(\tau)^2, \qquad \tilde{A}(0) = 0
$$

This is not an ODE in the usual sense but a **quadrature**: since $B(\tau)$ is already known, $A$ is obtained by direct integration.

!!! note "Theorem: Solution for $A$ via Quadrature"

    $$
    A(t,T) = \int_t^T \theta(u)\, B(u,T)\, du + \frac{1}{2}\sigma^2 \int_t^T B(u,T)^2\, du
    $$

    Note that $B(u,T) = -(1 - e^{-a(T-u)})/a$.

???+ note "Proof"
    Integrating the ODE from $t$ to $T$ (equivalently, from $\tau = T-t$ down to $\tau = 0$):

    $$
    A(T,T) - A(t,T) = -\int_t^T \theta(u) B(u,T)\, du - \frac{1}{2}\sigma^2 \int_t^T B(u,T)^2\, du
    $$

    Since $A(T,T) = 0$:

    $$
    A(t,T) = \int_t^T \theta(u) B(u,T)\, du + \frac{1}{2}\sigma^2 \int_t^T B(u,T)^2\, du
    $$

    $\square$

---

## Evaluating the B-Squared Integral

The second integral in $A$ can be computed in closed form.

!!! note "Proposition: Integral of $B^2$"

    $$
    \int_t^T B(u,T)^2\, du = \frac{1}{a^2}\left[(T-t) - \frac{2}{a}(1 - e^{-a(T-t)}) + \frac{1}{2a}(1 - e^{-2a(T-t)})\right]
    $$

???+ note "Proof"
    With $\tau' = T - u$:

    $$
    \int_t^T B(u,T)^2\, du = \int_0^{T-t} \frac{(1-e^{-a\tau'})^2}{a^2}\, d\tau' = \frac{1}{a^2}\int_0^{T-t}(1 - 2e^{-a\tau'} + e^{-2a\tau'})\, d\tau'
    $$

    $$
    = \frac{1}{a^2}\left[(T-t) + \frac{2}{a}(e^{-a(T-t)} - 1) - \frac{1}{2a}(e^{-2a(T-t)} - 1)\right]
    $$

    $$
    = \frac{1}{a^2}\left[(T-t) - \frac{2}{a}(1 - e^{-a(T-t)}) + \frac{1}{2a}(1 - e^{-2a(T-t)})\right]
    $$

    $\square$

---

## Closed-Form A Using the Initial Curve

When $\theta(t)$ is expressed via the initial term structure, the $\theta$-integral can also be evaluated to give a formula involving only market observables.

!!! note "Theorem: $A(t,T)$ in Terms of Market Data"

    $$
    A(t,T) = \ln\frac{P^M(0,T)}{P^M(0,t)} + B(t,T)\, f(0,t) + \frac{\sigma^2}{4a}\, B(t,T)^2\,(1 - e^{-2at})
    $$

    where $B(t,T) = -(1-e^{-a(T-t)})/a$, $P^M(0,\cdot)$ is the market discount curve, and $f(0,t) = -\partial_t \ln P^M(0,t)$.

This formula is the key computational result: it expresses $A(t,T)$ entirely in terms of quantities available from the market (discount factors, forward rates) and model parameters ($a$, $\sigma$), without needing to evaluate $\theta(t)$ or perform numerical integration.

---

## The Complete Bond Price

!!! note "Corollary: Hull-White Bond Price (Riccati Derivation)"
    Combining the solutions:

    $$
    P(t,T) = \frac{P^M(0,T)}{P^M(0,t)} \exp\!\left(B(t,T)\bigl[f(0,t) - r_t\bigr] + \frac{\sigma^2}{4a}\, B(t,T)^2(1 - e^{-2at})\right)
    $$

    where $B(t,T) = -(1-e^{-a(T-t)})/a$.

???+ note "Verification at $t = 0$"
    At $t = 0$: $B(0,T) = -(1-e^{-aT})/a$, $f(0,0) = r_0$, $(1-e^0) = 0$. Therefore:

    $$
    P(0,T) = \frac{P^M(0,T)}{1} \exp\!\bigl(B(0,T)(r_0 - r_0) + 0\bigr) = P^M(0,T)
    $$

    confirming exact calibration to the initial curve. $\square$

---

## Connection to General Affine Models

The Hull-White Riccati system is a special case of the general affine framework. For a model $dr = (\alpha + \beta r)\, dt + \sqrt{\gamma + \delta r}\, dW$, the Riccati system is:

$$
\frac{d\tilde{B}}{d\tau} = -\beta \tilde{B} - \frac{1}{2}\delta \tilde{B}^2 - 1
$$

$$
\frac{d\tilde{A}}{d\tau} = \alpha(T-\tau) \tilde{B} + \frac{1}{2}\gamma \tilde{B}^2
$$

For Hull-White: $\beta = -a$, $\delta = 0$, $\alpha(t) = \theta(t)$, $\gamma = \sigma^2$. The $\delta = 0$ condition eliminates the quadratic term in the $B$-equation, making it linear (hence "degenerate Riccati"). For the CIR model ($\delta > 0$), the $B$-equation becomes a true Riccati equation with a different (non-exponential) solution.

---

## Summary

The named functions $A(t,T)$ and $B(t,T)$ are derived by substituting the exponential-affine ansatz $P = e^{A+Br}$ into the Hull-White bond pricing PDE. The coefficient of $r$ yields the linear ODE $\partial_t B = aB + 1$ with solution $B(\tau) = -(1-e^{-a\tau})/a$, which is a degenerate Riccati equation. The constant term yields an ODE for $A$ that reduces to a quadrature given $B$, producing $A(t,T) = \ln(P^M(0,T)/P^M(0,t)) + B(t,T) f(0,t) + \frac{\sigma^2}{4a} B(t,T)^2(1-e^{-2at})$ when $\theta(t)$ is eliminated via the initial curve. The complete bond price is then available in closed form as a function of $r_t$ and market observables.

---

## Exercises

**Exercise 1.** Carry out the substitution of $P = e^{A + Br}$ into the Hull-White bond pricing PDE explicitly. Show that after dividing by $P$ and grouping by powers of $r$, you obtain exactly two conditions: one for the coefficient of $r$ and one for the constant term.

---

**Exercise 2.** Solve the Riccati ODE $\frac{d\tilde{B}}{d\tau} = -a\tilde{B} - 1$ with $\tilde{B}(0) = 0$ using the integrating factor method. Verify that the solution $B(\tau) = -(1-e^{-a\tau})/a$ satisfies the terminal condition $B(T,T) = 0$ and the asymptotic limit $B(\tau) \to -1/a$ as $\tau \to \infty$.

---

**Exercise 3.** For the CIR model $dr = a(b-r)\,dt + \sigma\sqrt{r}\,dW$, the $B$-equation becomes a true (quadratic) Riccati equation. Write down this Riccati equation and explain why the solution involves hyperbolic functions rather than simple exponentials.

---

**Exercise 4.** The formula $A(t,T) = \ln\frac{P^M(0,T)}{P^M(0,t)} + B(t,T)f(0,t) + \frac{\sigma^2}{4a}B(t,T)^2(1-e^{-2at})$ eliminates $\theta(t)$ entirely. Describe the steps needed to go from the quadrature $A(t,T) = \int_t^T \theta(u)B(u,T)\,du + \frac{1}{2}\sigma^2\int_t^T B(u,T)^2\,du$ to this closed-form expression.

---

**Exercise 5.** Verify the integral $\int_t^T B(u,T)^2\,du = \frac{1}{a^2}\left[(T-t) - \frac{2}{a}(1-e^{-a(T-t)}) + \frac{1}{2a}(1-e^{-2a(T-t)})\right]$ by direct computation. For $a = 0.05$ and $T - t = 5$, evaluate the integral numerically and compare with numerical quadrature.

---

**Exercise 6.** At $t = 0$, the bond price must satisfy $P(0,T) = P^M(0,T)$. Substitute $t = 0$ into the complete bond price formula and verify that this consistency condition is satisfied identically. What role does the condition $f(0,0) = r_0$ play?

---

**Exercise 7.** The general affine framework sets $\mu(t,r) = \alpha(t) + \beta r$ and $\sigma^2(t,r) = \gamma + \delta r$. Show that the Hull-White, Vasicek, CIR, and Ho-Lee models each correspond to a specific choice of $(\alpha, \beta, \gamma, \delta)$. For which of these models is the Riccati equation for $B$ truly nonlinear?
