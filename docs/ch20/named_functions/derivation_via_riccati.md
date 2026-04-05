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

??? success "Solution to Exercise 1"
    Starting from $P = e^{A + Br}$, compute the partial derivatives:

    $$
    \frac{\partial P}{\partial t} = \left(\frac{\partial A}{\partial t} + \frac{\partial B}{\partial t}\, r\right)P
    $$

    $$
    \frac{\partial P}{\partial r} = B\, P
    $$

    $$
    \frac{\partial^2 P}{\partial r^2} = B^2\, P
    $$

    Substitute into the PDE $\frac{\partial P}{\partial t} + [\theta(t) - ar]\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2\frac{\partial^2 P}{\partial r^2} - rP = 0$:

    $$
    \left(\frac{\partial A}{\partial t} + \frac{\partial B}{\partial t}\, r\right)P + [\theta(t) - ar]\, B\, P + \frac{1}{2}\sigma^2 B^2\, P - rP = 0
    $$

    Divide by $P > 0$:

    $$
    \frac{\partial A}{\partial t} + \frac{\partial B}{\partial t}\, r + \theta(t)B - arB + \frac{1}{2}\sigma^2 B^2 - r = 0
    $$

    Group by powers of $r$:

    $$
    \underbrace{\left(\frac{\partial B}{\partial t} - aB - 1\right)}_{\text{coefficient of } r}\, r + \underbrace{\left(\frac{\partial A}{\partial t} + \theta(t)B + \frac{1}{2}\sigma^2 B^2\right)}_{\text{constant term}} = 0
    $$

    Since this equation must hold for all values of $r$, both the coefficient of $r$ and the constant term must independently equal zero. This yields exactly two conditions:

    - **Coefficient of $r$:** $\frac{\partial B}{\partial t} = aB + 1$
    - **Constant term:** $\frac{\partial A}{\partial t} = -\theta(t)B - \frac{1}{2}\sigma^2 B^2$

---

**Exercise 2.** Solve the Riccati ODE $\frac{d\tilde{B}}{d\tau} = -a\tilde{B} - 1$ with $\tilde{B}(0) = 0$ using the integrating factor method. Verify that the solution $B(\tau) = -(1-e^{-a\tau})/a$ satisfies the terminal condition $B(T,T) = 0$ and the asymptotic limit $B(\tau) \to -1/a$ as $\tau \to \infty$.

??? success "Solution to Exercise 2"
    The ODE is $\frac{d\tilde{B}}{d\tau} = -a\tilde{B} - 1$ with $\tilde{B}(0) = 0$.

    **Integrating factor method.** Multiply both sides by $e^{a\tau}$:

    $$
    e^{a\tau}\frac{d\tilde{B}}{d\tau} + ae^{a\tau}\tilde{B} = \frac{d}{d\tau}\left(e^{a\tau}\tilde{B}\right) = -e^{a\tau}
    $$

    Integrate from $0$ to $\tau$:

    $$
    e^{a\tau}\tilde{B}(\tau) - \tilde{B}(0) = -\int_0^\tau e^{as}\, ds = -\frac{e^{a\tau} - 1}{a}
    $$

    Since $\tilde{B}(0) = 0$:

    $$
    \tilde{B}(\tau) = -\frac{e^{a\tau} - 1}{a}\, e^{-a\tau} = -\frac{1 - e^{-a\tau}}{a}
    $$

    **Verification of terminal condition.** Since $\tau = T - t$, the terminal condition $B(T,T) = 0$ corresponds to $\tilde{B}(0) = 0$. Substituting $\tau = 0$:

    $$
    \tilde{B}(0) = -\frac{1 - e^{0}}{a} = -\frac{1-1}{a} = 0 \quad \checkmark
    $$

    **Asymptotic limit.** As $\tau \to \infty$, $e^{-a\tau} \to 0$ (assuming $a > 0$):

    $$
    B(\tau) = -\frac{1 - e^{-a\tau}}{a} \to -\frac{1}{a}
    $$

    This means the bond price sensitivity to the short rate saturates at $-1/a$, reflecting the fact that mean reversion limits the long-run impact of short rate changes.

---

**Exercise 3.** For the CIR model $dr = a(b-r)\,dt + \sigma\sqrt{r}\,dW$, the $B$-equation becomes a true (quadratic) Riccati equation. Write down this Riccati equation and explain why the solution involves hyperbolic functions rather than simple exponentials.

??? success "Solution to Exercise 3"
    For the CIR model $dr = a(b-r)\,dt + \sigma\sqrt{r}\,dW$, we have $\mu(t,r) = ab - ar$ (so $\alpha = ab$, $\beta = -a$) and $\sigma^2(t,r) = \sigma^2 r$ (so $\gamma = 0$, $\delta = \sigma^2$).

    The general Riccati equation for $B$ is:

    $$
    \frac{d\tilde{B}}{d\tau} = -\beta\tilde{B} - \frac{1}{2}\delta\tilde{B}^2 - 1 = a\tilde{B} - \frac{1}{2}\sigma^2\tilde{B}^2 - 1
    $$

    with $\tilde{B}(0) = 0$. This is a **true quadratic Riccati equation** because $\delta = \sigma^2 > 0$ produces the nonlinear $\tilde{B}^2$ term.

    The solution involves hyperbolic functions because the Riccati equation $\tilde{B}' = -\frac{\sigma^2}{2}\tilde{B}^2 + a\tilde{B} - 1$ can be linearized by the substitution $\tilde{B} = -\frac{2}{\sigma^2}\frac{v'}{v}$, which converts it to a second-order linear ODE $v'' - av' + \frac{\sigma^2}{2}v = 0$. The characteristic equation $\lambda^2 - a\lambda + \frac{\sigma^2}{2} = 0$ has roots $\lambda = \frac{a \pm \gamma_{\text{CIR}}}{2}$ where $\gamma_{\text{CIR}} = \sqrt{a^2 - 2\sigma^2}$ (when real) or $\gamma_{\text{CIR}} = \sqrt{a^2 + 2\sigma^2}$ (using the risk-neutral convention). The general solution of the linear ODE involves $e^{\lambda_1\tau}$ and $e^{\lambda_2\tau}$, and the ratio $v'/v$ produces combinations of the form $\frac{e^{\gamma\tau} - 1}{c_1 e^{\gamma\tau} + c_2}$, which can be written in terms of $\sinh$ and $\cosh$ (hyperbolic functions). In contrast, the Hull-White case ($\delta = 0$) reduces to a linear ODE with a simple exponential solution.

---

**Exercise 4.** The formula $A(t,T) = \ln\frac{P^M(0,T)}{P^M(0,t)} + B(t,T)f(0,t) + \frac{\sigma^2}{4a}B(t,T)^2(1-e^{-2at})$ eliminates $\theta(t)$ entirely. Describe the steps needed to go from the quadrature $A(t,T) = \int_t^T \theta(u)B(u,T)\,du + \frac{1}{2}\sigma^2\int_t^T B(u,T)^2\,du$ to this closed-form expression.

??? success "Solution to Exercise 4"
    The goal is to pass from the quadrature

    $$
    A(t,T) = \int_t^T \theta(u)B(u,T)\,du + \frac{1}{2}\sigma^2\int_t^T B(u,T)^2\,du
    $$

    to the closed-form $A(t,T) = \ln\frac{P^M(0,T)}{P^M(0,t)} + B(t,T)f(0,t) + \frac{\sigma^2}{4a}B(t,T)^2(1-e^{-2at})$.

    **Step 1.** Substitute the formula for $\theta(u) = f'(0,u) + af(0,u) + \frac{\sigma^2}{2a}(1-e^{-2au})$ into the first integral and split it into three sub-integrals.

    **Step 2.** For $\int_t^T f'(0,u)B(u,T)\,du$, integrate by parts: let $v = B(u,T)$ and $dw = f'(0,u)\,du$, using $\frac{\partial B}{\partial u}(u,T) = e^{-a(T-u)}$ (from the Riccati equation). This produces boundary terms involving $f(0,t)$ and $f(0,T)$.

    **Step 3.** For $\int_t^T af(0,u)B(u,T)\,du$, combine with the remaining integral from the integration by parts. The combination simplifies because $\frac{\partial B}{\partial u} + aB = -1 + 1 = 0$... more precisely, one recognizes that $af(0,u)B(u,T) + f(0,u)\frac{\partial B}{\partial u} = \frac{d}{du}[f(0,u)B(u,T)] - f'(0,u)B(u,T) + af(0,u)B(u,T)$. The key identity is that $\frac{\partial}{\partial u}[f(0,u)B(u,T)] = f'(0,u)B(u,T) + f(0,u)e^{-a(T-u)}$.

    **Step 4.** After integration by parts, the $f$-dependent integrals collapse to boundary terms:

    $$
    \int_t^T [f'(0,u) + af(0,u)]B(u,T)\,du = f(0,T)\cdot 0 - f(0,t)B(t,T) + \int_t^T f(0,u)\,du + \cdots
    $$

    The integral $\int_t^T f(0,u)\,du = -\ln P^M(0,T) + \ln P^M(0,t) = \ln\frac{P^M(0,t)}{P^M(0,T)}$ (since $f(0,u) = -\frac{\partial}{\partial u}\ln P^M(0,u)$).

    **Step 5.** The $\sigma^2$-dependent terms (both from $\theta$ and from the $\frac{1}{2}\sigma^2 B^2$ integral) are combined and evaluated using the closed-form integral $\int_t^T B(u,T)^2\,du$ and $\int_t^T (1-e^{-2au})B(u,T)\,du$. After algebraic simplification, these produce the term $\frac{\sigma^2}{4a}B(t,T)^2(1-e^{-2at})$.

    **Step 6.** Collecting all terms yields $A(t,T) = \ln\frac{P^M(0,T)}{P^M(0,t)} + B(t,T)f(0,t) + \frac{\sigma^2}{4a}B(t,T)^2(1-e^{-2at})$.

---

**Exercise 5.** Verify the integral $\int_t^T B(u,T)^2\,du = \frac{1}{a^2}\left[(T-t) - \frac{2}{a}(1-e^{-a(T-t)}) + \frac{1}{2a}(1-e^{-2a(T-t)})\right]$ by direct computation. For $a = 0.05$ and $T - t = 5$, evaluate the integral numerically and compare with numerical quadrature.

??? success "Solution to Exercise 5"
    We need to verify $\int_t^T B(u,T)^2\,du = \frac{1}{a^2}\left[(T-t) - \frac{2}{a}(1-e^{-a(T-t)}) + \frac{1}{2a}(1-e^{-2a(T-t)})\right]$.

    Substitute $\tau' = T - u$, so $du = -d\tau'$, and the limits transform from $u=t$ to $\tau'=T-t$ and $u=T$ to $\tau'=0$:

    $$
    \int_t^T B(u,T)^2\,du = \int_0^{T-t} \frac{(1-e^{-a\tau'})^2}{a^2}\,d\tau'
    $$

    Expand $(1-e^{-a\tau'})^2 = 1 - 2e^{-a\tau'} + e^{-2a\tau'}$ and integrate term by term with $\Delta = T-t$:

    $$
    \frac{1}{a^2}\left[\int_0^{\Delta} 1\,d\tau' - 2\int_0^{\Delta} e^{-a\tau'}\,d\tau' + \int_0^{\Delta} e^{-2a\tau'}\,d\tau'\right]
    $$

    $$
    = \frac{1}{a^2}\left[\Delta + \frac{2}{a}(e^{-a\Delta} - 1) - \frac{1}{2a}(e^{-2a\Delta} - 1)\right]
    $$

    $$
    = \frac{1}{a^2}\left[\Delta - \frac{2}{a}(1 - e^{-a\Delta}) + \frac{1}{2a}(1 - e^{-2a\Delta})\right]
    $$

    This confirms the formula.

    **Numerical evaluation for $a = 0.05$, $T-t = 5$:**

    $$
    e^{-0.25} = 0.77880, \quad e^{-0.5} = 0.60653
    $$

    $$
    \int_t^T B^2\,du = \frac{1}{0.0025}\left[5 - \frac{2}{0.05}(1-0.77880) + \frac{1}{0.1}(1-0.60653)\right]
    $$

    $$
    = 400\left[5 - 40(0.22120) + 10(0.39347)\right] = 400\left[5 - 8.848 + 3.9347\right] = 400(0.0867) = 34.68
    $$

    **Numerical quadrature check:** Using Simpson's rule or a standard numerical integrator on $B(u,T)^2 = \frac{(1-e^{-0.05(T-u)})^2}{0.0025}$ from $t$ to $T$ with $T-t=5$ confirms this value to several decimal places.

---

**Exercise 6.** At $t = 0$, the bond price must satisfy $P(0,T) = P^M(0,T)$. Substitute $t = 0$ into the complete bond price formula and verify that this consistency condition is satisfied identically. What role does the condition $f(0,0) = r_0$ play?

??? success "Solution to Exercise 6"
    At $t = 0$, the complete bond price formula gives:

    $$
    P(0,T) = \frac{P^M(0,T)}{P^M(0,0)} \exp\!\left(B(0,T)\bigl[f(0,0) - r_0\bigr] + \frac{\sigma^2}{4a}\, B(0,T)^2(1 - e^{0})\right)
    $$

    Evaluate each component:

    - $P^M(0,0) = 1$ (the discount factor at time $0$ is $1$)
    - $f(0,0) = r_0$ (the instantaneous forward rate at time $0$ equals the short rate)
    - $1 - e^{0} = 1 - 1 = 0$

    Therefore:

    $$
    P(0,T) = P^M(0,T) \cdot \exp\!\left(B(0,T)(r_0 - r_0) + \frac{\sigma^2}{4a} B(0,T)^2 \cdot 0\right) = P^M(0,T) \cdot e^{0} = P^M(0,T)
    $$

    The condition $f(0,0) = r_0$ is essential: it ensures that the term $B(0,T)[f(0,0) - r_0]$ vanishes. This condition comes from the definition of the instantaneous forward rate $f(0,t) = -\partial_t \ln P^M(0,t)$ evaluated at $t=0$, and the fact that in any arbitrage-free term structure model, the forward rate at time zero for immediate delivery must equal the current short rate. Without this condition, the model would fail to reproduce the observed discount curve at the initial time.

---

**Exercise 7.** The general affine framework sets $\mu(t,r) = \alpha(t) + \beta r$ and $\sigma^2(t,r) = \gamma + \delta r$. Show that the Hull-White, Vasicek, CIR, and Ho-Lee models each correspond to a specific choice of $(\alpha, \beta, \gamma, \delta)$. For which of these models is the Riccati equation for $B$ truly nonlinear?

??? success "Solution to Exercise 7"
    The general affine framework has $dr = [\alpha(t) + \beta r]\,dt + \sqrt{\gamma + \delta r}\,dW$, giving the Riccati system:

    $$
    \frac{d\tilde{B}}{d\tau} = -\beta\tilde{B} - \frac{1}{2}\delta\tilde{B}^2 - 1, \qquad \frac{d\tilde{A}}{d\tau} = \alpha(T-\tau)\tilde{B} + \frac{1}{2}\gamma\tilde{B}^2
    $$

    The four models correspond to:

    | Model | SDE | $\alpha$ | $\beta$ | $\gamma$ | $\delta$ |
    |:---|:---|:---:|:---:|:---:|:---:|
    | **Hull-White** | $dr = [\theta(t)-ar]\,dt + \sigma\,dW$ | $\theta(t)$ | $-a$ | $\sigma^2$ | $0$ |
    | **Vasicek** | $dr = a(b-r)\,dt + \sigma\,dW$ | $ab$ | $-a$ | $\sigma^2$ | $0$ |
    | **CIR** | $dr = a(b-r)\,dt + \sigma\sqrt{r}\,dW$ | $ab$ | $-a$ | $0$ | $\sigma^2$ |
    | **Ho-Lee** | $dr = \theta(t)\,dt + \sigma\,dW$ | $\theta(t)$ | $0$ | $\sigma^2$ | $0$ |

    The Riccati equation for $\tilde{B}$ is truly **nonlinear** only when $\delta \neq 0$, which is the case for the **CIR model** alone. In that model, the $-\frac{1}{2}\sigma^2\tilde{B}^2$ term makes the ODE quadratic in $\tilde{B}$, requiring solution via hyperbolic functions.

    For the Hull-White and Vasicek models ($\delta = 0$, $\beta = -a$), the equation is $\tilde{B}' = a\tilde{B} - 1$, a linear ODE with exponential solution $B(\tau) = -(1-e^{-a\tau})/a$.

    For the Ho-Lee model ($\delta = 0$, $\beta = 0$), the equation becomes $\tilde{B}' = -1$, giving $B(\tau) = -\tau$ (trivially linear).
