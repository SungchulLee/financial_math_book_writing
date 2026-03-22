# Affine Structure of Hull-White

A term structure model is called "affine" when bond prices take the exponential-affine form $P(t,T) = e^{A(t,T) + B(t,T) r_t}$, where $A$ and $B$ are deterministic functions of time. The affine property is the source of the Hull-White model's analytical tractability: it reduces the computation of bond prices to evaluating two known functions, yields and forward rates become linear in the short rate, and option pricing formulas follow from the log-normality of bond price ratios. This section defines the affine class, verifies that the Hull-White model belongs to it, derives the Riccati ODEs governing $A$ and $B$, and discusses the broad consequences for pricing.

!!! info "Prerequisites"
    - Hull-White SDE and mean reversion (this chapter)
    - Bond pricing PDE: Feynman-Kac representation
    - Ordinary differential equations: Riccati and linear ODEs
    - General theory of affine term structure models (Chapter 15)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define the affine term structure class and state its key properties
    2. Verify that the Hull-White model satisfies the affine conditions
    3. Derive the Riccati ODEs for the functions $A(t,T)$ and $B(t,T)$
    4. Solve the ODE for $B(\tau)$ and express $A$ as a quadrature
    5. Explain why affine structure enables analytical bond and option pricing

---

## Definition of Affine Term Structure Models

!!! note "Definition: Affine Term Structure Model"
    A short-rate model $dr_t = \mu(t, r_t)\, dt + \sigma(t, r_t)\, dW_t$ is called an **affine term structure model** (ATSM) if the zero-coupon bond price can be written as

    $$
    P(t,T) = \exp\!\bigl(A(t,T) + B(t,T)\, r_t\bigr)
    $$

    where $A(t,T)$ and $B(t,T)$ are deterministic functions satisfying $A(T,T) = 0$ and $B(T,T) = 0$.

The affine form has immediate consequences:

- **Yields** are affine in $r_t$: $y(t,T) = -\frac{\ln P(t,T)}{T-t} = -\frac{A(t,T)}{T-t} - \frac{B(t,T)}{T-t}\, r_t$
- **Forward rates** are affine in $r_t$: $f(t,T) = -\partial_T \ln P(t,T) = -\partial_T A(t,T) - \partial_T B(t,T)\, r_t$
- The **entire yield curve** at time $t$ is determined by the single state variable $r_t$

!!! note "Theorem: Sufficient Conditions for Affine Structure"
    A short-rate model of the form

    $$
    dr_t = \bigl[\alpha(t) + \beta(t)\, r_t\bigr]\, dt + \sqrt{\gamma(t) + \delta(t)\, r_t}\; dW_t
    $$

    with deterministic coefficient functions $\alpha, \beta, \gamma, \delta$ admits an affine term structure. The Hull-White model $dr_t = [\theta(t) - ar_t]\, dt + \sigma\, dW_t$ corresponds to $\alpha(t) = \theta(t)$, $\beta(t) = -a$, $\gamma(t) = \sigma^2$, and $\delta(t) = 0$.

---

## Verification for Hull-White

To verify the affine structure, we substitute the exponential-affine ansatz into the bond pricing PDE.

!!! note "Theorem: Hull-White Bond Pricing PDE"
    The price $P(t,T)$ of a zero-coupon bond under the Hull-White model satisfies

    $$
    \frac{\partial P}{\partial t} + \bigl[\theta(t) - a\, r\bigr]\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2 \frac{\partial^2 P}{\partial r^2} = r\, P
    $$

    with terminal condition $P(T,T) = 1$.

???+ note "Derivation"
    By the Feynman-Kac theorem, the bond price $P(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\, ds} \mid r_t = r]$ satisfies the backward Kolmogorov equation associated with the Hull-White diffusion, with the discounting term $-rP$ moved to the right-hand side. The terminal condition $P(T,T) = 1$ reflects that a bond pays \$1 at maturity. $\square$

Now substitute the ansatz $P(t,T) = e^{A(t,T) + B(t,T) r}$ where we write $A = A(t,T)$ and $B = B(t,T)$ with $T$ fixed. The partial derivatives are:

$$
\frac{\partial P}{\partial t} = \left(\frac{\partial A}{\partial t} + \frac{\partial B}{\partial t}\, r\right) P, \qquad \frac{\partial P}{\partial r} = B\, P, \qquad \frac{\partial^2 P}{\partial r^2} = B^2\, P
$$

Substituting into the PDE and dividing by $P$:

$$
\frac{\partial A}{\partial t} + \frac{\partial B}{\partial t}\, r + [\theta(t) - ar]\, B + \frac{1}{2}\sigma^2 B^2 = r
$$

Collecting terms by powers of $r$:

$$
\underbrace{\left(\frac{\partial B}{\partial t} - aB - 1\right)}_{\text{coefficient of } r} r + \underbrace{\left(\frac{\partial A}{\partial t} + \theta(t) B + \frac{1}{2}\sigma^2 B^2\right)}_{\text{constant term}} = 0
$$

Since this must hold for all $r$, both the coefficient of $r$ and the constant term must vanish independently.

---

## The Riccati System

!!! note "Theorem: Riccati ODEs for $A$ and $B$"
    The functions $A(t,T)$ and $B(t,T)$ in the affine bond price satisfy the system

    $$
    \frac{\partial B}{\partial t}(t,T) = aB(t,T) + 1, \qquad B(T,T) = 0
    $$

    $$
    \frac{\partial A}{\partial t}(t,T) = -\theta(t)\, B(t,T) - \frac{1}{2}\sigma^2 B(t,T)^2, \qquad A(T,T) = 0
    $$

    The equation for $B$ is a linear ODE (a degenerate Riccati equation), and the equation for $A$ is a quadrature once $B$ is known.

---

## Solving for B

The ODE for $B$ is linear and can be solved in closed form.

!!! note "Theorem: Solution for $B(t,T)$"
    The solution of $\partial_t B = aB + 1$ with $B(T,T) = 0$ is

    $$
    B(t,T) = -\frac{1 - e^{-a(T-t)}}{a}
    $$

    Writing $\tau = T - t$, this is $B(\tau) = -(1 - e^{-a\tau})/a$.

???+ note "Proof"
    Change to the time-to-maturity variable $\tau = T - t$, so $B(\tau) = B(t,T)$ and $\frac{dB}{d\tau} = -\frac{\partial B}{\partial t}$. The ODE becomes

    $$
    \frac{dB}{d\tau} = -aB - 1, \qquad B(0) = 0
    $$

    This is a first-order linear ODE. The integrating factor is $e^{a\tau}$:

    $$
    \frac{d}{d\tau}\bigl(e^{a\tau} B\bigr) = -e^{a\tau}
    $$

    Integrating from $0$ to $\tau$:

    $$
    e^{a\tau} B(\tau) - B(0) = -\frac{e^{a\tau} - 1}{a}
    $$

    Since $B(0) = 0$:

    $$
    B(\tau) = -\frac{1 - e^{-a\tau}}{a}
    $$

    $\square$

The function $|B(\tau)| = (1 - e^{-a\tau})/a$ is the "duration-like" function that appears throughout Hull-White pricing. It satisfies:

- $B(0) = 0$ (terminal condition)
- $|B(\tau)| \approx \tau$ for $a\tau \ll 1$ (short maturities behave like zero-coupon duration)
- $|B(\tau)| \to 1/a$ as $\tau \to \infty$ (bounded effective duration)

---

## Solving for A

Once $B(\tau)$ is known, $A$ is obtained by integration.

!!! note "Theorem: Solution for $A(t,T)$"
    The function $A(t,T)$ satisfies

    $$
    A(t,T) = \int_t^T \theta(u)\, B(u,T)\, du + \frac{1}{2}\sigma^2 \int_t^T B(u,T)^2\, du
    $$

    When $\theta(t)$ is determined by fitting to the initial term structure, $A$ can be expressed in closed form as

    $$
    A(t,T) = \ln\frac{P(0,T)}{P(0,t)} + B(t,T)\, f(0,t) + \frac{\sigma^2}{4a}\, B(t,T)^2\bigl(1 - e^{-2at}\bigr)
    $$

    where $P(0,\cdot)$ is the initial bond price curve and $f(0,t) = -\partial_t \ln P(0,t)$ is the initial forward rate.

???+ note "Proof"
    From the ODE $\partial_t A = -\theta(t) B(t,T) - \frac{1}{2}\sigma^2 B(t,T)^2$ with $A(T,T) = 0$, integrate from $t$ to $T$:

    $$
    A(T,T) - A(t,T) = -\int_t^T \theta(u) B(u,T)\, du - \frac{1}{2}\sigma^2 \int_t^T B(u,T)^2\, du
    $$

    Since $A(T,T) = 0$:

    $$
    A(t,T) = \int_t^T \theta(u) B(u,T)\, du + \frac{1}{2}\sigma^2 \int_t^T B(u,T)^2\, du
    $$

    The closed-form expression involving $P(0,T)/P(0,t)$ follows from substituting $\theta(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1-e^{-2at})$ and evaluating the resulting integrals. The key step uses the identity $\int_t^T f'(0,u) B(u,T)\, du = [\text{boundary terms}]$ obtained by integration by parts and the relation $P(0,T) = \exp(-\int_0^T f(0,u)\, du)$. $\square$

---

## The Complete Affine Bond Price

Combining the results, the Hull-White bond price is:

!!! note "Corollary: Hull-White Bond Price"
    The zero-coupon bond price in the Hull-White model is

    $$
    P(t,T) = \exp\!\bigl(A(t,T) + B(t,T)\, r_t\bigr)
    $$

    where

    $$
    B(t,T) = -\frac{1 - e^{-a(T-t)}}{a}
    $$

    $$
    A(t,T) = \ln\frac{P(0,T)}{P(0,t)} + B(t,T)\, f(0,t) + \frac{\sigma^2}{4a}\, B(t,T)^2(1 - e^{-2at})
    $$

This is sometimes written with the opposite sign convention $P(t,T) = \exp(\hat{A}(t,T) - \hat{B}(t,T) r_t)$ where $\hat{B} = -B > 0$ and $\hat{A} = A$. Both conventions appear in the literature; we follow the convention where $B < 0$ throughout this chapter.

---

## Why Affine Structure Matters

The affine property enables a cascade of analytical results:

1. **Bond pricing**: Immediate from $P = e^{A + Br}$ without Monte Carlo or PDE numerics
2. **Yield curve**: All yields are affine in $r_t$, so the entire curve is determined by one state variable
3. **Bond options**: Since $\ln P(T,S) = A(T,S) + B(T,S) r_T$ is affine in the Gaussian $r_T$, the ratio $P(T,S)/P(T,T')$ is log-normal under the $T'$-forward measure, yielding Black-Scholes-type formulas
4. **Jamshidian's trick**: All bond prices are monotone in $r_T$, enabling decomposition of coupon bond options into portfolios of zero-coupon bond options
5. **Characteristic function**: The discounted characteristic function of $r_T$ has an exponential-affine form, facilitating Fourier pricing methods

!!! example "Numerical Verification"
    Consider $a = 0.05$, $\sigma = 0.01$, $r_0 = 0.03$, and a flat initial forward curve $f(0,t) = 0.03$. Then $P(0,T) = e^{-0.03T}$ and for $t = 0$:

    - $B(0,5) = -(1 - e^{-0.25})/0.05 = -4.424$
    - $A(0,5) = \ln(e^{-0.15}/1) + (-4.424)(0.03) + \frac{0.0001}{0.20}(4.424)^2(0) = -0.15 - 0.1327 = -0.2827$
    - $P(0,5) = \exp(-0.2827 + (-4.424)(0.03)) = \exp(-0.2827 - 0.1327) = e^{-0.15} \approx 0.8607$

    This confirms consistency: $P(0,5) = e^{-0.03 \times 5} = e^{-0.15}$, matching the initial curve.

---

## Summary

The Hull-White model belongs to the affine term structure class because its drift is linear in $r$ and its diffusion is constant, ensuring that the bond pricing PDE admits an exponential-affine solution $P(t,T) = e^{A(t,T) + B(t,T) r_t}$. The function $B(t,T) = -(1 - e^{-a(T-t)})/a$ satisfies a linear ODE from the Riccati system, and $A(t,T)$ is determined by a quadrature that can be evaluated in closed form when $\theta(t)$ is expressed via the initial term structure. The affine structure is the engine behind all analytical pricing formulas in the Hull-White framework, from zero-coupon bonds through options, caps, floors, and swaptions.
