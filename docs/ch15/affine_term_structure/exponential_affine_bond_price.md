# Exponential-Affine Bond Price Formula

The price of a zero-coupon bond in an affine term structure model admits a remarkably simple closed-form expression: the logarithm of the bond price is an **affine function** of the current state. This exponential-affine structure transforms the problem of computing expectations of path-dependent functionals into solving a system of ordinary differential equations --- the Riccati equations --- which can often be solved explicitly. The formula is the computational engine behind the entire affine term structure framework developed by Duffie and Kan (1996) and extended by Dai and Singleton (2000).

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State and derive the exponential-affine bond price formula from the risk-neutral pricing equation
    2. Derive the Riccati ODE system for the functions $A(\tau)$ and $B(\tau)$ by substituting the affine ansatz into the backward Kolmogorov equation
    3. Solve the Riccati ODEs explicitly for the Vasicek and CIR short-rate models
    4. Interpret the functions $A(\tau)$ and $B(\tau)$ in terms of factor loadings and convexity corrections

---

## Motivation

### From Expectation to ODE

Computing the price of a zero-coupon bond requires evaluating the conditional expectation

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds} \;\Big|\; \mathcal{F}_t\right]
$$

where $r_s$ is the short rate and $\mathbb{Q}$ is the risk-neutral measure. For a general short-rate model, this expectation involves the entire future path of $r_s$ and typically has no closed-form solution. However, when the short rate is an **affine function** of a Markov state vector $X_t$ whose dynamics are themselves affine, the expectation collapses to an exponential-affine function of the current state $X_t$.

This reduction is analogous to how the characteristic function of an affine process is exponential-affine in the state. The key mechanism is the same: substituting an exponential-affine ansatz into the backward Kolmogorov PDE separates the state dependence from the time dependence, reducing the PDE to a system of Riccati ODEs.

### Financial Significance

The exponential-affine bond price formula has three major consequences for fixed-income modeling:

1. **Yield curves** become affine functions of the state, enabling fast calibration and real-time pricing
2. **Factor loadings** $B(\tau)$ quantify how each state variable affects bond prices at each maturity
3. **Analytical derivatives** (duration, convexity, Greeks) follow directly from the closed-form expression

---

## Setup and Assumptions

### Affine Short-Rate Specification

Let $X_t \in D \subseteq \mathbb{R}^d$ be a $d$-dimensional affine process under the risk-neutral measure $\mathbb{Q}$ with dynamics

$$
dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t
$$

where the drift and instantaneous covariance are affine in the state:

$$
\mu(X_t) = K_0 + K_1 X_t, \qquad \sigma(X_t)\sigma(X_t)^\top = H_0 + \sum_{i=1}^d H_i\,X_t^{(i)}
$$

Here $K_0 \in \mathbb{R}^d$, $K_1 \in \mathbb{R}^{d \times d}$, $H_0 \in \mathbb{R}^{d \times d}$, and $H_i \in \mathbb{R}^{d \times d}$ for $i = 1, \ldots, d$.

The **short rate** is affine in the state:

$$
r(X_t) = \rho_0 + \rho_1^\top X_t
$$

where $\rho_0 \in \mathbb{R}$ and $\rho_1 \in \mathbb{R}^d$ are constants.

---

## The Exponential-Affine Bond Price

### Statement of the Main Result

!!! info "Theorem: Exponential-Affine Bond Price Formula"
    Under the affine short-rate specification above, the zero-coupon bond price is

    $$
    P(t,T) = \exp\!\bigl(A(\tau) + B(\tau)^\top X_t\bigr)
    $$

    where $\tau = T - t$ is the time to maturity, and the functions $A : \mathbb{R}_+ \to \mathbb{R}$ and $B : \mathbb{R}_+ \to \mathbb{R}^d$ satisfy the **Riccati ODE system**

    $$
    \frac{dB}{d\tau} = -\rho_1 + K_1^\top B(\tau) + \frac{1}{2}\sum_{i=1}^d B(\tau)^\top H_i\,B(\tau)\,e_i
    $$

    $$
    \frac{dA}{d\tau} = -\rho_0 + K_0^\top B(\tau) + \frac{1}{2}B(\tau)^\top H_0\,B(\tau)
    $$

    with initial conditions $A(0) = 0$ and $B(0) = \mathbf{0} \in \mathbb{R}^d$, where $e_i$ is the $i$-th standard basis vector.

### Derivation

The derivation proceeds by substituting the exponential-affine ansatz into the fundamental pricing PDE and matching terms.

**Step 1: The fundamental PDE.** Define $f(t, x) = P(t, T)$ viewed as a function of the current time $t$ and state $x$. By the Feynman-Kac theorem, $f$ satisfies

$$
\frac{\partial f}{\partial t} + \mu(x)^\top \nabla_x f + \frac{1}{2}\operatorname{tr}\!\left[\sigma(x)\sigma(x)^\top \nabla_x^2 f\right] - r(x)\,f = 0
$$

with terminal condition $f(T, x) = 1$ for all $x$.

**Step 2: Affine ansatz.** Substitute $f(t, x) = \exp(A(\tau) + B(\tau)^\top x)$ with $\tau = T - t$. Computing the partial derivatives:

$$
\frac{\partial f}{\partial t} = \left(-\frac{dA}{d\tau} - \frac{dB}{d\tau}^\top x\right) f
$$

$$
\nabla_x f = B(\tau)\,f, \qquad \nabla_x^2 f = B(\tau)\,B(\tau)^\top f
$$

**Step 3: Substitution.** Inserting into the PDE and dividing by $f$ (which is strictly positive):

$$
-\frac{dA}{d\tau} - \frac{dB}{d\tau}^\top x + (K_0 + K_1 x)^\top B + \frac{1}{2}B^\top\!\left(H_0 + \sum_{i=1}^d H_i\,x^{(i)}\right)\!B - \rho_0 - \rho_1^\top x = 0
$$

**Step 4: Separation.** Collecting terms constant in $x$ and terms linear in $x$ separately:

- **Constant terms** (independent of $x$):

$$
-\frac{dA}{d\tau} + K_0^\top B + \frac{1}{2}B^\top H_0\,B - \rho_0 = 0
$$

- **Linear terms** (coefficient of $x$):

$$
-\frac{dB}{d\tau} + K_1^\top B + \frac{1}{2}\sum_{i=1}^d (B^\top H_i\,B)\,e_i - \rho_1 = 0
$$

Since these equations must hold for **all** $x \in D$, the constant part and the linear part must each vanish identically. This gives the Riccati system. The terminal condition $P(T,T) = 1$ translates to $A(0) = 0$ and $B(0) = \mathbf{0}$. $\square$

!!! tip "Why the Separation Works"
    The separation into constant and linear terms succeeds precisely because the drift, diffusion, and short rate are all affine in $x$. If any of these were nonlinear in $x$, the substitution would produce terms quadratic or higher in $x$, and no ODE system for $A$ and $B$ alone could satisfy the PDE for all $x$.

---

## Explicit Solutions for Classical Models

### Vasicek Model

The Vasicek model has a single state variable $X_t = r_t$ with dynamics

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t
$$

The affine parameters are $K_0 = \kappa\theta$, $K_1 = -\kappa$, $H_0 = \sigma^2$, $H_1 = 0$, $\rho_0 = 0$, and $\rho_1 = 1$.

The Riccati equation for $B(\tau)$ becomes

$$
\frac{dB}{d\tau} = -1 - \kappa\,B(\tau), \qquad B(0) = 0
$$

This is a first-order linear ODE with the explicit solution

$$
B(\tau) = -\frac{1 - e^{-\kappa\tau}}{\kappa}
$$

!!! example "Derivation of $B(\tau)$ for Vasicek"
    The ODE $B' = -1 - \kappa B$ has integrating factor $e^{\kappa\tau}$. Multiplying both sides:

    $$
    \frac{d}{d\tau}\!\left[e^{\kappa\tau}B\right] = -e^{\kappa\tau}
    $$

    Integrating from $0$ to $\tau$ with $B(0) = 0$:

    $$
    e^{\kappa\tau}B(\tau) = -\frac{e^{\kappa\tau} - 1}{\kappa}
    $$

    Dividing by $e^{\kappa\tau}$ gives $B(\tau) = -(1 - e^{-\kappa\tau})/\kappa$. $\square$

The equation for $A(\tau)$ is

$$
\frac{dA}{d\tau} = \kappa\theta\,B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2
$$

Integrating explicitly:

$$
A(\tau) = \left(\theta - \frac{\sigma^2}{2\kappa^2}\right)\!\bigl(B(\tau) + \tau\bigr) - \frac{\sigma^2}{4\kappa}B(\tau)^2
$$

The Vasicek bond price is therefore

$$
P(t,T) = \exp\!\left(A(\tau) + B(\tau)\,r_t\right)
$$

where $B(\tau) < 0$ for all $\tau > 0$, confirming that the bond price decreases when the short rate increases.

### Cox-Ingersoll-Ross Model

The CIR model has dynamics

$$
dr_t = \kappa(\theta - r_t)\,dt + \xi\sqrt{r_t}\,dW_t
$$

The affine parameters are $K_0 = \kappa\theta$, $K_1 = -\kappa$, $H_0 = 0$, $H_1 = \xi^2$, $\rho_0 = 0$, and $\rho_1 = 1$.

The Riccati equation for $B(\tau)$ is now **nonlinear**:

$$
\frac{dB}{d\tau} = -1 - \kappa\,B(\tau) + \frac{1}{2}\xi^2 B(\tau)^2, \qquad B(0) = 0
$$

!!! info "Theorem: CIR Bond Price Coefficients"
    Define $\gamma = \sqrt{\kappa^2 + 2\xi^2}$. The solution is

    $$
    B(\tau) = \frac{-2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
    $$

    $$
    A(\tau) = \frac{2\kappa\theta}{\xi^2}\ln\!\left(\frac{2\gamma\,e^{(\gamma+\kappa)\tau/2}}{(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma}\right)
    $$

!!! example "Verification of the CIR Solution"
    To verify, differentiate $B(\tau)$. Write $D(\tau) = (\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma$ so that $B = -2(e^{\gamma\tau} - 1)/D$. Then

    $$
    B'(\tau) = \frac{-2\gamma e^{\gamma\tau}\,D + 2(e^{\gamma\tau}-1)(\gamma+\kappa)\gamma e^{\gamma\tau}}{D^2}
    $$

    After simplification, one can verify that $B' = -1 - \kappa B + \frac{1}{2}\xi^2 B^2$ holds identically, with $B(0) = 0$ since the numerator vanishes at $\tau = 0$. $\square$

!!! warning "Sign Convention"
    Note that $B(\tau) < 0$ for all $\tau > 0$ in both models. Some references define $B$ with the opposite sign convention, writing $P = \exp(A - B\,r_t)$ with $B > 0$. Always check the sign convention when comparing across sources.

---

## Interpretation of A and B

### Factor Loading B

The function $B(\tau)$ quantifies the **sensitivity** of the log bond price to the state variable:

$$
\frac{\partial \ln P(t,T)}{\partial X_t^{(i)}} = B_i(\tau)
$$

In a one-factor model, $B(\tau)$ is the negative of the bond's duration with respect to the short rate (up to sign convention). For the Vasicek model, $|B(\tau)| = (1 - e^{-\kappa\tau})/\kappa$ increases monotonically from $0$ toward $1/\kappa$ as $\tau \to \infty$. This saturation reflects the mean-reversion of the short rate: very long-term bond prices are insensitive to the current short rate because the rate reverts to its long-run mean.

For the CIR model, $|B(\tau)|$ also saturates, approaching $2/(\gamma + \kappa)$ as $\tau \to \infty$.

### Convexity Correction A

The function $A(\tau)$ captures the **convexity correction** --- the contribution to the bond price that arises from the volatility of the state variable. Even if $X_t = 0$, the bond price $\exp(A(\tau))$ differs from $1$ because the randomness of the future path of $X_s$ creates a Jensen's inequality effect that systematically biases bond prices.

In the Vasicek model, $A(\tau)$ is determined by two effects:

1. The long-run drift $\kappa\theta$ pulling the rate toward $\theta$
2. The variance $\sigma^2$ creating a convexity benefit (bond prices are convex in yields, so volatility raises the expected bond price)

---

## Multifactor Extension

For a $d$-dimensional affine state vector, the Riccati system becomes a system of $d + 1$ coupled ODEs. The equation for $B(\tau) \in \mathbb{R}^d$ couples through the quadratic terms $B^\top H_i\,B$, while the equation for $A(\tau) \in \mathbb{R}$ is driven by $B(\tau)$.

!!! note "Computational Strategy"
    In multi-factor models, the Riccati system for $B(\tau)$ is generally **nonlinear** and must be solved numerically. The standard approach is:

    1. Solve the $d$-dimensional ODE for $B(\tau)$ first (e.g., using a fourth-order Runge-Kutta scheme)
    2. Then integrate the scalar ODE for $A(\tau)$ by quadrature, since it depends only on the already-computed $B(\tau)$

    This two-step procedure avoids solving a $(d+1)$-dimensional system and is numerically more stable.

For a two-factor model with state $X_t = (r_t, v_t)^\top$ where $v_t$ drives stochastic volatility, the bond price takes the form

$$
P(t,T) = \exp\!\bigl(A(\tau) + B_1(\tau)\,r_t + B_2(\tau)\,v_t\bigr)
$$

If $r_t$ appears in the short-rate specification but $v_t$ does not (i.e., $\rho_1 = (1, 0)^\top$), then $B_2(\tau)$ captures the indirect effect of stochastic volatility on bond prices through its influence on the risk-neutral dynamics of $r_t$.

---

## Connection to General Affine Transform

The bond price formula is a special case of the general affine transform. Setting $u = \mathbf{0}$ in the discounted characteristic function

$$
\mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds + u^\top X_T}\;\Big|\; X_t = x\right] = \exp\!\bigl(\tilde{\phi}(\tau, u) + \tilde{\psi}(\tau, u)^\top x\bigr)
$$

recovers the bond price: $P(t,T) = \exp(\tilde{\phi}(\tau, \mathbf{0}) + \tilde{\psi}(\tau, \mathbf{0})^\top x)$, so $A(\tau) = \tilde{\phi}(\tau, \mathbf{0})$ and $B(\tau) = \tilde{\psi}(\tau, \mathbf{0})$. The Riccati system for $(A, B)$ is precisely the extended Riccati system evaluated at $u = \mathbf{0}$.

---

## Summary

The exponential-affine bond price formula $P(t,T) = \exp(A(\tau) + B(\tau)^\top X_t)$ is the central result of the affine term structure framework. It reduces bond pricing from evaluating a path integral to solving a deterministic ODE system. The Riccati equation for $B(\tau)$ determines the factor loadings --- how each state variable influences bond prices at each maturity --- while the equation for $A(\tau)$ captures the convexity correction. For the Vasicek model, the Riccati system is linear and yields explicit exponential solutions; for the CIR model, the nonlinear Riccati equation produces a more complex but still closed-form expression involving $\gamma = \sqrt{\kappa^2 + 2\xi^2}$. In higher dimensions, the same structural result holds, with the Riccati system solved numerically when closed-form solutions are unavailable.

---

## Further Reading

- Duffie, D. and Kan, R. (1996). "A Yield-Factor Model of Interest Rates." *Mathematical Finance*, 6(4), 379--406.
- Dai, Q. and Singleton, K. (2000). "Specification Analysis of Affine Term Structure Models." *Journal of Finance*, 55(5), 1943--1978.
- Filipovic, D. (2009). *Term-Structure Models: A Graduate Course*. Springer.
- Brigo, D. and Mercurio, F. (2007). *Interest Rate Models --- Theory and Practice*. Springer.
