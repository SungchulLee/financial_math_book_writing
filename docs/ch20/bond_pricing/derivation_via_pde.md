# Bond Price Derivation via PDE

The expectation-based derivation of the Hull-White bond price exploits the Gaussian structure of the short rate integral. An independent route to the same formula starts from the Feynman-Kac theorem, which converts the pricing problem into a partial differential equation. Substituting an exponential-affine ansatz reduces the PDE to a system of ordinary differential equations -- a linear ODE for $B(\tau)$ and a quadrature for $A(t,T)$ -- that can be solved explicitly. This section carries out the PDE derivation from start to finish, filling in every algebraic step.

!!! info "Prerequisites"
    - Hull-White SDE: $dr(t) = [\theta(t) - ar(t)]\,dt + \sigma\,dW^{\mathbb{Q}}(t)$
    - Feynman-Kac theorem connecting conditional expectations to PDEs
    - Bond price formula from the expectation derivation (sibling section) for cross-verification

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the bond pricing PDE from the Feynman-Kac theorem
    2. Substitute the exponential-affine ansatz and separate variables
    3. Solve the Riccati ODE for $B(\tau)$ and the quadrature for $A(t,T)$
    4. Express the complete bond price in terms of market observables
    5. Verify consistency with the expectation-based derivation

---

## From Feynman-Kac to the Bond Pricing PDE

The zero-coupon bond price satisfies the risk-neutral pricing identity

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(s)\,ds}\,\Big|\,\mathcal{F}(t)\right]
$$

By the Feynman-Kac theorem, any function $P(t,r)$ satisfying this conditional expectation also satisfies a backward PDE with the short rate dynamics providing the drift and diffusion coefficients.

!!! info "Theorem: Hull-White Bond Pricing PDE"
    Under the Hull-White model, the zero-coupon bond price $P(t,T)$ satisfies

    $$
    \frac{\partial P}{\partial t} + \bigl[\theta(t) - ar\bigr]\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2\frac{\partial^2 P}{\partial r^2} - rP = 0
    $$

    with terminal condition $P(T,T) = 1$.

???+ note "Derivation"
    The Feynman-Kac theorem states that if $X_t$ satisfies $dX_t = \mu(t,X_t)\,dt + \sigma(t,X_t)\,dW_t$, then

    $$
    u(t,x) = \mathbb{E}\!\left[e^{-\int_t^T c(s,X_s)\,ds}\,g(X_T)\,\Big|\,X_t = x\right]
    $$

    solves $\frac{\partial u}{\partial t} + \mu\frac{\partial u}{\partial x} + \frac{1}{2}\sigma^2\frac{\partial^2 u}{\partial x^2} - c(t,x)\,u = 0$ with $u(T,x) = g(x)$.

    For the zero-coupon bond: $X_t = r(t)$, $\mu(t,r) = \theta(t) - ar$, $\sigma(t,r) = \sigma$ (constant), $c(t,r) = r$, and $g(r) = 1$. Substitution gives the stated PDE. The terminal condition $P(T,T) = 1$ reflects the \$1 payoff at maturity. $\square$

---

## The Exponential-Affine Ansatz

The PDE is linear in $r$ (the drift $\theta(t) - ar$ is affine and the diffusion $\sigma$ is constant), suggesting that the solution may be exponential-affine in $r$.

!!! info "Ansatz"
    Assume the bond price has the form

    $$
    P(t,T) = \exp\!\bigl(A(t,T) + B(t,T)\,r\bigr)
    $$

    where $A(t,T)$ and $B(t,T)$ are deterministic functions to be determined, subject to the terminal conditions $A(T,T) = 0$ and $B(T,T) = 0$.

The terminal conditions follow from $P(T,T) = e^{A(T,T) + B(T,T)r} = 1$ for all $r$, which requires both $A(T,T) = 0$ and $B(T,T) = 0$.

---

## Substitution into the PDE

Compute the required partial derivatives of $P = e^{A + Br}$:

$$
\frac{\partial P}{\partial t} = \left(\frac{\partial A}{\partial t} + \frac{\partial B}{\partial t}\,r\right)P
$$

$$
\frac{\partial P}{\partial r} = B\,P
$$

$$
\frac{\partial^2 P}{\partial r^2} = B^2\,P
$$

Substitute into the PDE and divide by $P > 0$:

$$
\frac{\partial A}{\partial t} + \frac{\partial B}{\partial t}\,r + [\theta(t) - ar]\,B + \frac{1}{2}\sigma^2 B^2 - r = 0
$$

Collect terms by powers of $r$:

$$
\underbrace{\left(\frac{\partial B}{\partial t} - aB - 1\right)}_{\text{coefficient of }r}\,r + \underbrace{\left(\frac{\partial A}{\partial t} + \theta(t)\,B + \frac{1}{2}\sigma^2 B^2\right)}_{\text{constant term}} = 0
$$

Since this must hold for all values of $r$, both the coefficient of $r$ and the constant term must vanish independently.

---

## The ODE for B

Setting the coefficient of $r$ to zero yields a first-order linear ODE.

!!! info "Theorem: ODE for $B(t,T)$"

    $$
    \frac{\partial B}{\partial t}(t,T) = aB(t,T) + 1, \qquad B(T,T) = 0
    $$

**Change to time-to-maturity.** Let $\tau = T - t$ and write $\tilde{B}(\tau) = B(t,T)$. Since $\frac{\partial B}{\partial t} = -\frac{d\tilde{B}}{d\tau}$, the ODE becomes

$$
\frac{d\tilde{B}}{d\tau} = -a\tilde{B} - 1, \qquad \tilde{B}(0) = 0
$$

!!! info "Theorem: Solution for $B(\tau)$"

    $$
    B(\tau) = -\frac{1 - e^{-a\tau}}{a}
    $$

???+ note "Proof"
    The ODE $\tilde{B}' + a\tilde{B} = -1$ is solved by the integrating factor $\mu(\tau) = e^{a\tau}$:

    $$
    \frac{d}{d\tau}\!\left(e^{a\tau}\tilde{B}\right) = e^{a\tau}\!\left(\tilde{B}' + a\tilde{B}\right) = -e^{a\tau}
    $$

    Integrating from $0$ to $\tau$:

    $$
    e^{a\tau}\tilde{B}(\tau) - \tilde{B}(0) = -\int_0^{\tau} e^{as}\,ds = -\frac{e^{a\tau} - 1}{a}
    $$

    Using $\tilde{B}(0) = 0$:

    $$
    \tilde{B}(\tau) = -\frac{e^{a\tau} - 1}{a}\,e^{-a\tau} = -\frac{1 - e^{-a\tau}}{a}
    $$

    $\square$

**Properties of $B(\tau)$:**

- $B(0) = 0$: the terminal condition is satisfied
- $B(\tau) < 0$ for $\tau > 0$: bond prices decrease when rates increase
- $B(\tau) \to -1/a$ as $\tau \to \infty$: the sensitivity saturates due to mean reversion
- $B(\tau) \approx -\tau$ for $a\tau \ll 1$: recovers the zero-mean-reversion (Ho-Lee) limit

The magnitude $|B(\tau)| = (1 - e^{-a\tau})/a$ is the duration-like function used in the positive-$B$ convention where the bond price is written $P = e^{A - |B|\,r}$.

---

## The ODE for A

Setting the constant term to zero:

!!! info "Theorem: ODE for $A(t,T)$"

    $$
    \frac{\partial A}{\partial t}(t,T) = -\theta(t)\,B(t,T) - \frac{1}{2}\sigma^2\,B(t,T)^2, \qquad A(T,T) = 0
    $$

In the $\tau$ variable:

$$
\frac{d\tilde{A}}{d\tau} = \theta(T - \tau)\,B(\tau) + \frac{1}{2}\sigma^2\,B(\tau)^2, \qquad \tilde{A}(0) = 0
$$

Since $B(\tau)$ is already known, this is a quadrature (direct integration), not a differential equation in the usual sense.

!!! info "Theorem: Solution for $A$ via Quadrature"

    $$
    A(t,T) = \int_t^T \theta(u)\,B(u,T)\,du + \frac{1}{2}\sigma^2 \int_t^T B(u,T)^2\,du
    $$

???+ note "Proof"
    Integrating the ODE for $A$ from $t$ to $T$ (equivalently, from $\tau = T - t$ down to $0$):

    $$
    A(T,T) - A(t,T) = -\int_t^T \theta(u)\,B(u,T)\,du - \frac{1}{2}\sigma^2\int_t^T B(u,T)^2\,du
    $$

    Since $A(T,T) = 0$:

    $$
    A(t,T) = \int_t^T \theta(u)\,B(u,T)\,du + \frac{1}{2}\sigma^2\int_t^T B(u,T)^2\,du
    $$

    $\square$

---

## Evaluating the Integrals

### The $B^2$ Integral

The second integral can be computed in closed form.

!!! info "Proposition: Integral of $B^2$"

    $$
    \frac{1}{2}\sigma^2\int_t^T B(u,T)^2\,du = \frac{\sigma^2}{2a^2}\left[\tau - \frac{2}{a}(1 - e^{-a\tau}) + \frac{1}{2a}(1 - e^{-2a\tau})\right]
    $$

    where $\tau = T - t$.

???+ note "Proof"
    Substituting $v = T - u$ and using $B(u,T) = -(1 - e^{-av})/a$:

    $$
    \int_t^T B(u,T)^2\,du = \frac{1}{a^2}\int_0^{\tau}(1 - e^{-av})^2\,dv
    $$

    Expanding and integrating term by term:

    $$
    = \frac{1}{a^2}\int_0^{\tau}\!\left(1 - 2e^{-av} + e^{-2av}\right)dv = \frac{1}{a^2}\left[\tau + \frac{2}{a}(e^{-a\tau} - 1) - \frac{1}{2a}(e^{-2a\tau} - 1)\right]
    $$

    $$
    = \frac{1}{a^2}\left[\tau - \frac{2}{a}(1 - e^{-a\tau}) + \frac{1}{2a}(1 - e^{-2a\tau})\right]
    $$

    $\square$

### The theta Integral and the Market Curve

The integral $\int_t^T \theta(u) B(u,T)\,du$ involves the time-dependent drift $\theta(t)$, which encodes the market yield curve. Using

$$
\theta(t) = \frac{\partial f^M(0,t)}{\partial t} + a\,f^M(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})
$$

and performing integration by parts (details in the sibling section on Riccati equations), the $\theta$-integral combines with the $B^2$-integral to give a formula involving only market observables.

!!! info "Theorem: $A(t,T)$ in Terms of the Market Curve"

    $$
    A(t,T) = \ln\frac{P^M(0,T)}{P^M(0,t)} + B(t,T)\,f^M(0,t) + \frac{\sigma^2}{4a}\,B(t,T)^2\left(1 - e^{-2at}\right)
    $$

    where $B(t,T) = -(1 - e^{-a\tau})/a$ and $f^M(0,t) = -\partial_t \ln P^M(0,t)$.

???+ note "Proof Sketch"
    The key step is eliminating $\theta(u)$ in favor of $P^M$. Starting from $\theta(u) = f'(0,u) + af(0,u) + \frac{\sigma^2}{2a}(1 - e^{-2au})$ and integrating $\theta(u) B(u,T)$ from $t$ to $T$:

    The $f'(0,u)B(u,T)$ term is integrated by parts. The $af(0,u)B(u,T)$ term combines with the boundary term from integration by parts. After collecting all contributions with the $B^2$-integral, one obtains

    $$
    A(t,T) = -\int_t^T f^M(0,u)\,du + \int_0^t f^M(0,u)\,du + B(t,T) f^M(0,t) + \frac{\sigma^2}{4a} B(t,T)^2(1 - e^{-2at})
    $$

    Using $\int_0^T f^M(0,u)\,du = -\ln P^M(0,T)$ and $\int_0^t f^M(0,u)\,du = -\ln P^M(0,t)$, this simplifies to the stated formula. $\square$

---

## The Complete Bond Price

Combining $A(t,T)$ and $B(t,T)$:

!!! info "Corollary: Hull-White Bond Price (PDE Derivation)"
    The zero-coupon bond price is

    $$
    P(t,T) = \frac{P^M(0,T)}{P^M(0,t)}\exp\!\left(B(t,T)\bigl[f^M(0,t) - r(t)\bigr] + \frac{\sigma^2}{4a}\,B(t,T)^2(1 - e^{-2at})\right)
    $$

    where $B(t,T) = -(1 - e^{-a(T-t)})/a$.

???+ note "Verification at $t = 0$"
    At $t = 0$: $P^M(0,0) = 1$, $f^M(0,0) = r(0)$, and $1 - e^0 = 0$. Therefore

    $$
    P(0,T) = P^M(0,T)\exp\!\bigl(B(0,T)(r(0) - r(0)) + 0\bigr) = P^M(0,T)
    $$

    confirming exact calibration to the initial curve. $\square$

---

## Equivalence with the Expectation Derivation

The bond price derived via the PDE method is identical to the one obtained by computing $\mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r(s)\,ds} \mid \mathcal{F}(t)]$ directly (see the sibling section). Both routes exploit the same structural feature -- the affine dependence of the Hull-White drift on $r$ -- but through different mathematical machinery:

| Method | Key tool | Role of Gaussian structure |
|:---|:---|:---|
| **Expectation** | MGF of $\mathcal{N}(\mu, \sigma^2)$: $\mathbb{E}[e^{-X}] = e^{-\mu + \sigma^2/2}$ | Evaluates the exponential expectation directly |
| **PDE** | Variable separation via affine ansatz | Reduces the PDE to ODEs that can be solved explicitly |

The agreement between the two derivations serves as a consistency check: any error in either calculation would produce a discrepancy.

---

## Numerical Example

Consider a Hull-White model with $a = 0.05$, $\sigma = 0.01$, flat forward curve $f^M(0,t) = 0.03$, and current short rate $r(2) = 0.035$ at time $t = 2$. Compute the price of a zero-coupon bond maturing at $T = 12$ ($\tau = 10$ years).

**Step 1: Compute $B(2, 12)$.**

$$
B(2,12) = -\frac{1 - e^{-0.05 \times 10}}{0.05} = -\frac{1 - e^{-0.5}}{0.05} = -\frac{1 - 0.6065}{0.05} \approx -7.869
$$

**Step 2: Compute $A(2, 12)$.**

With a flat forward curve: $P^M(0,T) = e^{-0.03T}$.

$$
\ln\frac{P^M(0,12)}{P^M(0,2)} = -0.03(12) + 0.03(2) = -0.30
$$

$$
B(2,12)\,f^M(0,2) = (-7.869)(0.03) = -0.2361
$$

$$
\frac{\sigma^2}{4a}\,B^2(1 - e^{-2at}) = \frac{0.0001}{0.2}(61.92)(1 - e^{-0.2}) = 0.0005 \times 61.92 \times 0.1813 \approx 0.00561
$$

$$
A(2,12) = -0.30 + (-0.2361) + 0.00561 \approx -0.5305
$$

**Step 3: Compute the bond price.**

$$
P(2,12) = e^{A + Br} = e^{-0.5305 + (-7.869)(0.035)} = e^{-0.5305 - 0.2754} = e^{-0.8059} \approx 0.4466
$$

For comparison, the market discount factor is $P^M(0,12)/P^M(0,2) = e^{-0.30} \approx 0.7408/1.0 = 0.7408$. The model price is lower because $r(2) = 0.035 > f^M(0,2) = 0.03$: the short rate is above the forward rate, depressing bond prices.

---

## Summary

The PDE derivation of the Hull-White bond price proceeds by applying the Feynman-Kac theorem to obtain the backward pricing equation, substituting the exponential-affine ansatz $P = e^{A + Br}$, and separating the resulting equation into a linear ODE for $B(\tau)$ with solution $B(\tau) = -(1 - e^{-a\tau})/a$ and a quadrature for $A(t,T)$ that reduces to $A(t,T) = \ln(P^M(0,T)/P^M(0,t)) + B(t,T)f^M(0,t) + \frac{\sigma^2}{4a}B(t,T)^2(1-e^{-2at})$ when $\theta(t)$ is eliminated via the market curve. The result is identical to the expectation-based derivation, confirming the internal consistency of the Hull-White framework.

---

## Exercises

**Exercise 1.** State the Feynman-Kac theorem precisely. Identify the functions $\mu(t,x)$, $\sigma(t,x)$, $c(t,x)$, and $g(x)$ that correspond to the Hull-White zero-coupon bond pricing problem.

---

**Exercise 2.** The ODE for $B(\tau)$ is $\tilde{B}' + a\tilde{B} = -1$ with $\tilde{B}(0) = 0$. Solve this ODE using the method of variation of parameters instead of the integrating factor. Verify you obtain the same solution $B(\tau) = -(1 - e^{-a\tau})/a$.

---

**Exercise 3.** Show that $B(\tau) \approx -\tau + \frac{a\tau^2}{2}$ for small $a\tau$ by Taylor expanding $e^{-a\tau}$. Use this to estimate the error in approximating $B(\tau) \approx -\tau$ (the Ho-Lee limit) when $a = 0.05$ and $\tau = 10$.

---

**Exercise 4.** Explain why the $A$-equation is a quadrature rather than a genuine ODE. What structural property of the Hull-White model makes this simplification possible, and how would the situation change for a model with state-dependent volatility (e.g., CIR)?

---

**Exercise 5.** Using the numerical example with $a = 0.05$, $\sigma = 0.01$, $f^M(0,t) = 0.03$, and $r(2) = 0.035$, compute $P(2, 12)$ step by step. Then recompute for $r(2) = 0.025$ and comment on the sensitivity of the bond price to the current short rate.

---

**Exercise 6.** Verify the consistency check at $t = 0$: show that $P(0,T) = P^M(0,T)$ by substituting $t = 0$ into the complete bond price formula. Which terms simplify or vanish, and why?

---

**Exercise 7.** Compare the PDE and expectation derivations from a computational perspective. For a model where closed-form solutions are not available, which approach (numerical PDE vs. Monte Carlo) would you prefer for computing bond prices? Discuss the trade-offs in terms of accuracy, computational cost, and dimensionality.
