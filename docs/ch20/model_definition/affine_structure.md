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

---

## Exercises

**Exercise 1.** Verify that the Hull-White model satisfies the sufficient conditions for affine structure by identifying $\alpha(t) = \theta(t)$, $\beta(t) = -a$, $\gamma(t) = \sigma^2$, and $\delta(t) = 0$. Which of these conditions would fail for the CIR model $dr_t = a(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$?

??? success "Solution to Exercise 1"
    The sufficient conditions for affine structure require the drift to be affine in $r$ and the squared diffusion to be affine in $r$:

    $$
    dr_t = [\alpha(t) + \beta(t)\,r_t]\,dt + \sqrt{\gamma(t) + \delta(t)\,r_t}\;dW_t
    $$

    **Hull-White model** $dr_t = [\theta(t) - ar_t]\,dt + \sigma\,dW_t$:

    - $\alpha(t) = \theta(t)$: time-dependent, deterministic -- satisfies the affine requirement
    - $\beta(t) = -a$: constant -- satisfies the affine requirement
    - $\gamma(t) = \sigma^2$: constant -- satisfies the affine requirement
    - $\delta(t) = 0$: the diffusion is independent of $r_t$ -- satisfies the affine requirement

    All four conditions hold, so the Hull-White model is affine.

    **CIR model** $dr_t = a(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$:

    - $\alpha(t) = a\theta$: constant -- satisfies the affine requirement
    - $\beta(t) = -a$: constant -- satisfies the affine requirement
    - $\gamma(t) = 0$: satisfies the affine requirement
    - $\delta(t) = \sigma^2$: constant and **nonzero** -- still satisfies the affine requirement

    The CIR model is also affine because $\delta(t) = \sigma^2 \neq 0$ is permitted in the affine class. However, the nonzero $\delta$ makes the Riccati ODE for $B$ genuinely nonlinear (see Exercise 6), unlike the Hull-White case where it is linear. The key structural difference is in the diffusion coefficient: Hull-White has $\delta = 0$ (constant volatility), while CIR has $\delta \neq 0$ (state-dependent volatility). Neither condition "fails" -- both models are affine -- but the CIR model's Riccati equation is harder to solve.

---

**Exercise 2.** Solve the Riccati ODE $\frac{dB}{d\tau} = -aB - 1$ with $B(0) = 0$ using Laplace transforms instead of the integrating factor method. Verify the same result $B(\tau) = -(1 - e^{-a\tau})/a$.

??? success "Solution to Exercise 2"
    The ODE is $\frac{dB}{d\tau} = -aB - 1$ with $B(0) = 0$.

    **Laplace transform method:** Let $\hat{B}(s) = \int_0^\infty e^{-s\tau}B(\tau)\,d\tau$ be the Laplace transform.

    Taking the Laplace transform of both sides of $B'(\tau) = -aB(\tau) - 1$:

    $$
    s\hat{B}(s) - B(0) = -a\hat{B}(s) - \frac{1}{s}
    $$

    Since $B(0) = 0$:

    $$
    s\hat{B}(s) = -a\hat{B}(s) - \frac{1}{s}
    $$

    $$
    (s + a)\hat{B}(s) = -\frac{1}{s}
    $$

    $$
    \hat{B}(s) = -\frac{1}{s(s+a)}
    $$

    Partial fraction decomposition:

    $$
    -\frac{1}{s(s+a)} = -\frac{1}{a}\left(\frac{1}{s} - \frac{1}{s+a}\right)
    $$

    Inverting the Laplace transform term by term ($\mathcal{L}^{-1}[1/s] = 1$ and $\mathcal{L}^{-1}[1/(s+a)] = e^{-a\tau}$):

    $$
    B(\tau) = -\frac{1}{a}(1 - e^{-a\tau}) = -\frac{1 - e^{-a\tau}}{a}
    $$

    This matches the result obtained by the integrating factor method.

---

**Exercise 3.** Show that $|B(\tau)| \approx \tau$ for small $a\tau$ and $|B(\tau)| \to 1/a$ as $\tau \to \infty$. For $a = 0.05$, at what maturity $\tau$ does $|B(\tau)|$ reach 90% of its asymptotic value?

??? success "Solution to Exercise 3"
    The function $|B(\tau)| = (1 - e^{-a\tau})/a$.

    **Small $a\tau$ approximation:** Taylor expand $e^{-a\tau} = 1 - a\tau + \frac{(a\tau)^2}{2} - \cdots$:

    $$
    |B(\tau)| = \frac{1 - (1 - a\tau + \frac{a^2\tau^2}{2} - \cdots)}{a} = \frac{a\tau - \frac{a^2\tau^2}{2} + \cdots}{a} = \tau - \frac{a\tau^2}{2} + \cdots \approx \tau
    $$

    So $|B(\tau)| \approx \tau$ when $a\tau \ll 1$, i.e., for short maturities relative to $1/a$.

    **Large $\tau$ limit:** As $\tau \to \infty$, $e^{-a\tau} \to 0$, so $|B(\tau)| \to 1/a$.

    **90% of asymptotic value for $a = 0.05$:** We need $|B(\tau)| = 0.9/a = 0.9/0.05 = 18$:

    $$
    \frac{1 - e^{-0.05\tau}}{0.05} = 18 \implies 1 - e^{-0.05\tau} = 0.9 \implies e^{-0.05\tau} = 0.1
    $$

    $$
    \tau = \frac{\ln 10}{0.05} = \frac{2.3026}{0.05} \approx 46.05 \text{ years}
    $$

    At approximately 46 years to maturity, $|B(\tau)|$ reaches 90% of its limiting value $1/a = 20$. This slow convergence reflects the weak mean reversion ($a = 0.05$, half-life of about 14 years).

---

**Exercise 4.** The yield $y(t,T) = -\frac{A(t,T)}{T-t} - \frac{B(t,T)}{T-t}r_t$ is affine in $r_t$. For the numerical example ($a = 0.05$, $\sigma = 0.01$, $f(0,t) = 0.03$), compute the 5-year and 30-year yields for $r_t = 0.03$ and $r_t = 0.05$. Verify that the yield difference is proportional to $B(t,T)/(T-t)$.

??? success "Solution to Exercise 4"
    With $a = 0.05$, $\sigma = 0.01$, $f(0,t) = 0.03$ (flat initial curve), and $t = 0$:

    $$
    B(0,T) = -\frac{1 - e^{-0.05T}}{0.05}
    $$

    $$
    A(0,T) = \ln\frac{P(0,T)}{P(0,0)} + B(0,T)\cdot f(0,0) + \frac{\sigma^2}{4a}B(0,T)^2(1 - e^{0}) = -0.03T + B(0,T)\cdot 0.03 + 0
    $$

    Since $P(0,T) = e^{-0.03T}$, $P(0,0) = 1$, and $e^{-2a\cdot 0} = 1$, the last term vanishes.

    The yield is $y(0,T) = -\frac{A(0,T)}{T} - \frac{B(0,T)}{T}\,r_0$.

    **5-year yield ($T = 5$):**

    $B(0,5) = -(1 - e^{-0.25})/0.05 = -(1 - 0.7788)/0.05 = -4.424$

    For $r_0 = 0.03$: $y(0,5) = -\frac{A(0,5)}{5} - \frac{-4.424}{5}\times 0.03$

    Since $P(0,5) = e^{A(0,5) + B(0,5)\times 0.03}$, and for a flat curve $P(0,5) = e^{-0.15}$:

    $A(0,5) = -0.15 - (-4.424)(0.03) = -0.15 + 0.1327 = -0.0173$

    $y(0,5) = -\frac{-0.0173}{5} - \frac{-4.424}{5}\times 0.03 = 0.00346 + 0.02654 = 0.03000$

    For $r_0 = 0.05$: $y(0,5) = -\frac{-0.0173}{5} - \frac{-4.424}{5}\times 0.05 = 0.00346 + 0.04424 = 0.04770$

    **30-year yield ($T = 30$):**

    $B(0,30) = -(1 - e^{-1.5})/0.05 = -(1 - 0.2231)/0.05 = -15.538$

    $A(0,30) = -0.90 - (-15.538)(0.03) = -0.90 + 0.4661 = -0.4339$

    For $r_0 = 0.03$: $y(0,30) = -\frac{-0.4339}{30} - \frac{-15.538}{30}\times 0.03 = 0.01446 + 0.01554 = 0.03000$

    For $r_0 = 0.05$: $y(0,30) = 0.01446 + \frac{15.538}{30}\times 0.05 = 0.01446 + 0.02590 = 0.04036$

    **Yield difference verification:**

    The yield difference between $r_0 = 0.05$ and $r_0 = 0.03$ is $\Delta y = -\frac{B(0,T)}{T}\Delta r$ where $\Delta r = 0.02$:

    - 5-year: $\Delta y = \frac{4.424}{5}\times 0.02 = 0.01770$. Check: $0.04770 - 0.03000 = 0.01770$. Confirmed.
    - 30-year: $\Delta y = \frac{15.538}{30}\times 0.02 = 0.01036$. Check: $0.04036 - 0.03000 = 0.01036$. Confirmed.

    The yield difference is indeed proportional to $|B(t,T)|/(T-t)$, confirming the affine structure. The sensitivity $|B|/T$ is larger for shorter maturities (0.885 for 5Y vs 0.518 for 30Y), reflecting the bounded effective duration of the mean-reverting model.

---

**Exercise 5.** Explain why Jamshidian's trick works for affine models. Specifically, show that the exercise boundary for a coupon bond option can be expressed as a critical value $r^*$ of the short rate, because all zero-coupon bond prices are monotone in $r_T$.

??? success "Solution to Exercise 5"
    Jamshidian's trick decomposes a coupon bond option into a portfolio of zero-coupon bond options. The key insight relies on the affine structure.

    **Step 1: Coupon bond value.** A coupon bond paying $c_i$ at times $T_i$ ($i = 1, \ldots, n$) has value

    $$
    V(T) = \sum_{i=1}^n c_i\, P(T, T_i) = \sum_{i=1}^n c_i\, e^{A(T,T_i) + B(T,T_i)\,r_T}
    $$

    **Step 2: Monotonicity.** Since $B(T,T_i) < 0$ for all $T_i > T$, each term $P(T,T_i) = e^{A(T,T_i) + B(T,T_i)\,r_T}$ is a strictly decreasing function of $r_T$. Therefore the sum $V(T)$ is also strictly decreasing in $r_T$.

    **Step 3: Critical rate $r^*$.** For a European call option on the coupon bond with strike $K$, the option is in the money when $V(T) > K$. Since $V(T)$ is monotonically decreasing in $r_T$, there exists a unique critical rate $r^*$ such that

    $$
    V(T)\big|_{r_T = r^*} = K \quad \iff \quad \sum_{i=1}^n c_i\, e^{A(T,T_i) + B(T,T_i)\,r^*} = K
    $$

    The option is exercised if and only if $r_T < r^*$.

    **Step 4: Decomposition.** Define $K_i = P(T,T_i)\big|_{r_T = r^*} = e^{A(T,T_i) + B(T,T_i)\,r^*}$. Then $\sum c_i K_i = K$, and

    $$
    (V(T) - K)^+ = \sum_{i=1}^n c_i(P(T,T_i) - K_i)^+
    $$

    This equality holds because all terms $P(T,T_i) - K_i$ change sign at exactly the same $r^* = r_T$ (by monotonicity). The coupon bond option is therefore a portfolio of $n$ zero-coupon bond options with strikes $K_i$, each of which can be priced in closed form using the Hull-White bond option formula.

    The trick works for any affine model because monotonicity of $P(T,T_i)$ in $r_T$ is guaranteed by the sign of $B(T,T_i)$, which is always negative (or always positive, depending on convention) for all maturities.

---

**Exercise 6.** The CIR model has $\delta(t) \neq 0$, meaning the diffusion depends on $r_t$. Show that the CIR model is still affine but its Riccati ODE for $B$ is genuinely nonlinear: $\frac{dB}{d\tau} = -aB - \frac{1}{2}\sigma^2 B^2 - 1$. Why does this make the $B$-equation harder to solve?

??? success "Solution to Exercise 6"
    The CIR model is $dr_t = a(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$. The bond pricing PDE is

    $$
    \frac{\partial P}{\partial t} + a(\theta - r)\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2 r\frac{\partial^2 P}{\partial r^2} = rP
    $$

    Substituting the affine ansatz $P = e^{A + Br}$ with derivatives $\partial_t P = (A_t + B_t r)P$, $\partial_r P = BP$, $\partial_r^2 P = B^2 P$:

    $$
    A_t + B_t r + a(\theta - r)B + \frac{1}{2}\sigma^2 r B^2 = r
    $$

    Collecting by powers of $r$:

    $$
    \underbrace{\left(B_t - aB + \frac{1}{2}\sigma^2 B^2 - 1\right)}_{\text{coefficient of } r}\,r + \underbrace{(A_t + a\theta B)}_{\text{constant}} = 0
    $$

    Setting the coefficient of $r$ to zero (in the $\tau = T-t$ variable with $dB/d\tau = -\partial_t B$):

    $$
    \frac{dB}{d\tau} = -aB - \frac{1}{2}\sigma^2 B^2 - 1, \qquad B(0) = 0
    $$

    This is a **genuinely nonlinear** Riccati equation because of the $\frac{1}{2}\sigma^2 B^2$ term. Compare with the Hull-White case $dB/d\tau = -aB - 1$, which is linear (the $B^2$ term vanishes because $\delta = 0$).

    **Why this is harder to solve:** The CIR Riccati ODE is a quadratic ODE, and while it does have a closed-form solution involving hyperbolic functions:

    $$
    B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + a)(e^{\gamma\tau} - 1) + 2\gamma}, \qquad \gamma = \sqrt{a^2 + 2\sigma^2}
    $$

    this solution requires computing the discriminant $\gamma$ and is more complex than the simple exponential $B(\tau) = -(1-e^{-a\tau})/a$ of Hull-White. General Riccati equations may not have closed-form solutions at all; the CIR case works because the coefficients are constants. For time-dependent coefficients, numerical integration of the Riccati ODE would be required.

---

**Exercise 7.** Use the affine bond price formula to compute the bond price sensitivity $\frac{\partial P}{\partial r} = B(t,T)\,P(t,T)$. For $a = 0.05$ and maturity $\tau = 10$, compute the dollar duration $|B|\times P$ and compare it with the Macaulay duration $\tau$ of a zero-coupon bond.

??? success "Solution to Exercise 7"
    The affine bond price is $P(t,T) = e^{A(t,T) + B(t,T)\,r_t}$, so

    $$
    \frac{\partial P}{\partial r} = B(t,T)\,e^{A(t,T) + B(t,T)\,r_t} = B(t,T)\,P(t,T)
    $$

    For $a = 0.05$ and $\tau = T - t = 10$:

    $$
    B(t,T) = -\frac{1 - e^{-0.05 \times 10}}{0.05} = -\frac{1 - e^{-0.5}}{0.05} = -\frac{1 - 0.6065}{0.05} = -\frac{0.3935}{0.05} = -7.869
    $$

    The **dollar duration** (sensitivity of bond price to a unit change in $r$) is

    $$
    |B(t,T)| \times P(t,T) = 7.869 \times P(t,T)
    $$

    For a typical bond price (say $r_t = 0.03$ with a flat curve, so $P \approx e^{-0.03\times 10} = 0.7408$):

    $$
    |B| \times P \approx 7.869 \times 0.7408 = 5.829
    $$

    **Comparison with Macaulay duration:** The Macaulay duration of a zero-coupon bond with maturity $\tau$ is simply $\tau = 10$ years. The Hull-White effective duration $|B(\tau)| = 7.87$ years is **less than** the Macaulay duration.

    This discrepancy arises because mean reversion reduces the effective impact of a rate change on long-dated bond prices. In a non-mean-reverting model (e.g., Ho-Lee with $a = 0$), $|B(\tau)| = \tau$ exactly, and the effective duration equals the Macaulay duration. With mean reversion ($a > 0$), rate shocks decay exponentially, so a change in $r_t$ today has a diminished effect on distant cash flows. The ratio $|B(\tau)|/\tau = 7.87/10 = 78.7\%$ measures how much mean reversion reduces the effective duration relative to the maturity.

    In the limit $\tau \to \infty$, $|B| \to 1/a = 20$ while $\tau \to \infty$, so $|B|/\tau \to 0$: mean reversion makes very long-dated bonds much less sensitive to rate shocks than their maturity would suggest.
