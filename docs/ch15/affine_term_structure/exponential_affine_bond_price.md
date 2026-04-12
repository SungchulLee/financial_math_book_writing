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

---

## Exercises

**Exercise 1.** For the Vasicek model with $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.02$, compute $B(\tau)$ and $A(\tau)$ at $\tau = 1, 5, 10$ years. Verify that $B(\tau) < 0$ for all three maturities and that $|B(\tau)|$ is increasing.

??? success "Solution to Exercise 1"
    With $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.02$:

    **$B(\tau)$ computation.** Using $B(\tau) = -(1 - e^{-\kappa\tau})/\kappa$:

    | $\tau$ | $e^{-\kappa\tau}$ | $1 - e^{-\kappa\tau}$ | $B(\tau)$ |
    |---|---|---|---|
    | 1 | $e^{-0.3} = 0.7408$ | 0.2592 | $-0.2592/0.3 = -0.8640$ |
    | 5 | $e^{-1.5} = 0.2231$ | 0.7769 | $-0.7769/0.3 = -2.5897$ |
    | 10 | $e^{-3.0} = 0.04979$ | 0.9502 | $-0.9502/0.3 = -3.1674$ |

    Verification: $B(\tau) < 0$ for all three maturities, and $|B(\tau)|$ increases: $0.8640 < 2.5897 < 3.1674$.

    **$A(\tau)$ computation.** Using $A(\tau) = (\theta - \sigma^2/(2\kappa^2))(B(\tau) + \tau) - \sigma^2 B(\tau)^2/(4\kappa)$:

    First, $\sigma^2/(2\kappa^2) = 0.0004/0.18 = 0.002222$, so $\theta - \sigma^2/(2\kappa^2) = 0.05 - 0.002222 = 0.04778$. Also, $\sigma^2/(4\kappa) = 0.0004/1.2 = 0.000333$.

    | $\tau$ | $B + \tau$ | $B^2$ | $A(\tau)$ |
    |---|---|---|---|
    | 1 | 0.1360 | 0.7465 | $0.04778(0.1360) - 0.000333(0.7465) = 0.006498 - 0.000249 = 0.006249$ |
    | 5 | 2.4103 | 6.7065 | $0.04778(2.4103) - 0.000333(6.7065) = 0.1152 - 0.002235 = 0.1129$ |
    | 10 | 6.8326 | 10.033 | $0.04778(6.8326) - 0.000333(10.033) = 0.3265 - 0.003344 = 0.3231$ |

    The function $|B(\tau)|$ is monotonically increasing and bounded above by $1/\kappa = 3.333$, with the 10-year value $3.1674$ already close to this saturation level.

---

**Exercise 2.** Starting from the Feynman-Kac PDE $\partial f/\partial t + \mu(x)^\top \nabla_x f + \frac{1}{2}\operatorname{tr}[\sigma(x)\sigma(x)^\top \nabla_x^2 f] - r(x)f = 0$ with terminal condition $f(T,x) = 1$, carry out the full derivation of the Riccati system by substituting $f(t,x) = \exp(A(\tau) + B(\tau)^\top x)$ for a general $d$-dimensional affine model. Identify explicitly the constant and linear terms in $x$.

??? success "Solution to Exercise 2"
    Starting from the Feynman-Kac PDE with terminal condition $f(T, x) = 1$:

    $$
    \frac{\partial f}{\partial t} + \mu(x)^\top \nabla_x f + \frac{1}{2}\operatorname{tr}\!\left[\sigma(x)\sigma(x)^\top \nabla_x^2 f\right] - r(x)\,f = 0
    $$

    **Ansatz.** Substitute $f(t, x) = \exp(A(\tau) + B(\tau)^\top x)$ with $\tau = T - t$.

    **Derivatives:**

    $$
    \frac{\partial f}{\partial t} = \left(-A'(\tau) - B'(\tau)^\top x\right)f
    $$

    $$
    \frac{\partial f}{\partial x_i} = B_i(\tau)\,f, \qquad \frac{\partial^2 f}{\partial x_i \partial x_j} = B_i(\tau)\,B_j(\tau)\,f
    $$

    **Substitution.** Using $\mu(x) = K_0 + K_1 x$, $\sigma(x)\sigma(x)^\top = H_0 + \sum_{i=1}^d H_i x^{(i)}$, and $r(x) = \rho_0 + \rho_1^\top x$:

    $$
    \left(-A' - B'^\top x\right)f + (K_0 + K_1 x)^\top B\,f + \frac{1}{2}B^\top\!\left(H_0 + \sum_{i=1}^d H_i x^{(i)}\right)\!B\,f - (\rho_0 + \rho_1^\top x)\,f = 0
    $$

    Dividing by $f > 0$:

    $$
    -A' - B'^\top x + K_0^\top B + x^\top K_1^\top B + \frac{1}{2}B^\top H_0 B + \frac{1}{2}\sum_{i=1}^d (B^\top H_i B)\,x^{(i)} - \rho_0 - \rho_1^\top x = 0
    $$

    **Separation.** Constant terms (independent of $x$):

    $$
    -A'(\tau) + K_0^\top B(\tau) + \frac{1}{2}B(\tau)^\top H_0\,B(\tau) - \rho_0 = 0
    $$

    Linear terms (coefficient of $x^{(i)}$ for each $i$):

    $$
    -B_i'(\tau) + [K_1^\top B(\tau)]_i + \frac{1}{2}B(\tau)^\top H_i\,B(\tau) - (\rho_1)_i = 0
    $$

    In vector form:

    $$
    -B'(\tau) + K_1^\top B(\tau) + \frac{1}{2}\sum_{i=1}^d (B^\top H_i B)\,e_i - \rho_1 = 0
    $$

    These must hold for all $x$, yielding the Riccati system. The terminal condition $f(T, x) = 1$ gives $A(0) = 0$, $B(0) = \mathbf{0}$. $\square$

---

**Exercise 3.** In the CIR model, define $\gamma = \sqrt{\kappa^2 + 2\xi^2}$. Show that $\gamma > \kappa$ and use this to prove that the denominator $(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma > 0$ for all $\tau > 0$. This guarantees that $B(\tau)$ is well-defined and finite for all maturities.

??? success "Solution to Exercise 3"
    **Step 1: Show $\gamma > \kappa$.**

    $$
    \gamma = \sqrt{\kappa^2 + 2\xi^2}
    $$

    Since $\xi > 0$, we have $2\xi^2 > 0$, so $\kappa^2 + 2\xi^2 > \kappa^2$, and therefore $\gamma > |\kappa| \geq \kappa$ (with $\kappa > 0$ in the CIR model).

    **Step 2: Show $D(\tau) = (\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma > 0$ for all $\tau > 0$.**

    Since $\gamma > 0$ and $\kappa > 0$ (mean reversion), $\gamma + \kappa > 0$. For $\tau > 0$, $e^{\gamma\tau} > 1$, so $e^{\gamma\tau} - 1 > 0$. Therefore:

    $$
    (\gamma + \kappa)(e^{\gamma\tau} - 1) > 0
    $$

    Adding $2\gamma > 0$:

    $$
    D(\tau) = (\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma > 0
    $$

    At $\tau = 0$: $D(0) = 0 + 2\gamma = 2\gamma > 0$. For $\tau > 0$, $D(\tau)$ is strictly increasing (since its derivative $(\gamma + \kappa)\gamma e^{\gamma\tau} > 0$), so $D(\tau) > D(0) > 0$.

    This guarantees the CIR bond pricing formula $B(\tau) = -2(e^{\gamma\tau} - 1)/D(\tau)$ is well-defined and finite for all maturities $\tau \geq 0$. There is no finite-time explosion, unlike what can occur for certain parameter values in more general affine models. $\square$

---

**Exercise 4.** Compute the limiting factor loading $\lim_{\tau \to \infty} |B(\tau)|$ for both the Vasicek model and the CIR model. Express the CIR limit in terms of $\kappa$, $\xi$, and $\gamma$. Explain why the CIR saturation level $2/(\gamma + \kappa)$ is always less than the Vasicek saturation level $1/\kappa$.

??? success "Solution to Exercise 4"
    **Vasicek limiting factor loading.** With $B(\tau) = -(1 - e^{-\kappa\tau})/\kappa$:

    $$
    \lim_{\tau \to \infty} |B(\tau)| = \lim_{\tau \to \infty} \frac{1 - e^{-\kappa\tau}}{\kappa} = \frac{1}{\kappa}
    $$

    **CIR limiting factor loading.** With $B(\tau) = -2(e^{\gamma\tau} - 1)/[(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma]$:

    $$
    \lim_{\tau \to \infty} |B(\tau)| = \lim_{\tau \to \infty} \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
    $$

    Dividing numerator and denominator by $e^{\gamma\tau} - 1$ (which $\to \infty$):

    $$
    = \frac{2}{\gamma + \kappa + 2\gamma/(e^{\gamma\tau} - 1)} \to \frac{2}{\gamma + \kappa}
    $$

    **Comparison.** We need to show $2/(\gamma + \kappa) < 1/\kappa$, i.e., $2\kappa < \gamma + \kappa$, i.e., $\kappa < \gamma$. This holds because $\gamma = \sqrt{\kappa^2 + 2\xi^2} > \kappa$ (as shown in Exercise 3).

    **Interpretation.** The CIR saturation level is strictly smaller because the state-dependent volatility $\xi\sqrt{r_t}$ introduces an additional risk-adjustment effect. The quadratic term $\frac{1}{2}\xi^2 B^2$ in the CIR Riccati equation creates an additional "pull" that limits $|B(\tau)|$ to a value smaller than the Vasicek limit. Financially, the CIR convexity adjustment partially offsets the rate sensitivity for very long maturities.

---

**Exercise 5.** Consider a two-factor model with $X_t = (r_t, v_t)^\top$, short rate $r_t = X_t^{(1)}$, and dynamics

$$
dr_t = \kappa_r(\theta_r - r_t)\,dt + \sqrt{v_t}\,dW_t^{(1)}, \qquad dv_t = \kappa_v(\theta_v - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
$$

Write the Riccati system for $B_1(\tau)$ and $B_2(\tau)$, and explain why $B_2(\tau) \neq 0$ even though $v_t$ does not appear directly in the short rate specification.

??? success "Solution to Exercise 5"
    The short rate is $r_t = X_t^{(1)}$, so $\rho_0 = 0$ and $\rho_1 = (1, 0)^\top$.

    The affine parameters for the diffusion are: $H_0 = 0$ (no constant covariance) and

    $$
    H_1 = 0, \qquad H_2 = \begin{pmatrix} 1 & 0 \\ 0 & \xi^2 \end{pmatrix}
    $$

    (since $v_t = X_t^{(2)}$ enters both diffusion coefficients). The drift parameters are $K_0 = (\kappa_r\theta_r,\, \kappa_v\theta_v)^\top$ and $K_1 = \operatorname{diag}(-\kappa_r, -\kappa_v)$.

    **Riccati system for $B(\tau) = (B_1(\tau), B_2(\tau))^\top$:**

    $$
    B_1'(\tau) = -1 - \kappa_r B_1(\tau), \quad B_1(0) = 0
    $$

    $$
    B_2'(\tau) = -\kappa_v B_2(\tau) + \frac{1}{2}B_1(\tau)^2 + \frac{1}{2}\xi^2 B_2(\tau)^2, \quad B_2(0) = 0
    $$

    The $B_1$ equation is a standard linear ODE with solution $B_1(\tau) = -(1 - e^{-\kappa_r\tau})/\kappa_r$.

    **Why $B_2(\tau) \neq 0$:** Even though $v_t$ does not appear directly in the short rate ($\rho_1 = (1, 0)^\top$), the $B_2$ equation is driven by the term $\frac{1}{2}B_1(\tau)^2 > 0$. This term arises because $v_t$ enters the diffusion of $r_t$ (through $\sqrt{v_t}\,dW_t^{(1)}$), so the conditional variance of the discount factor depends on $v_t$. The quadratic driving term $\frac{1}{2}B_1^2$ represents the convexity effect: uncertainty about future rates (which is governed by $v_t$) affects the expected discount factor through Jensen's inequality. Since $B_1(\tau)^2 > 0$ for $\tau > 0$ and $B_2(0) = 0$, the function $B_2(\tau)$ becomes nonzero immediately for $\tau > 0$.

---

**Exercise 6.** The convexity correction $A(\tau)$ in the Vasicek model can be decomposed as $A(\tau) = A_{\text{drift}}(\tau) + A_{\text{vol}}(\tau)$ where $A_{\text{drift}} = \kappa\theta \int_0^\tau B(s)\,ds$ and $A_{\text{vol}} = \frac{1}{2}\sigma^2 \int_0^\tau B(s)^2\,ds$. Evaluate both integrals in closed form and verify that $A_{\text{vol}}(\tau) > 0$ for all $\tau > 0$.

??? success "Solution to Exercise 6"
    The Vasicek convexity correction is $A(\tau) = \kappa\theta\int_0^\tau B(s)\,ds + \frac{1}{2}\sigma^2\int_0^\tau B(s)^2\,ds$, since $K_0 = \kappa\theta$, $H_0 = \sigma^2$, and $B(\tau) = -(1 - e^{-\kappa\tau})/\kappa$.

    **Drift integral $A_{\text{drift}}(\tau) = \kappa\theta\int_0^\tau B(s)\,ds$:**

    $$
    \int_0^\tau B(s)\,ds = \int_0^\tau -\frac{1 - e^{-\kappa s}}{\kappa}\,ds = -\frac{1}{\kappa}\left[\tau - \frac{1 - e^{-\kappa\tau}}{\kappa}\right] = -\frac{1}{\kappa}\left[\tau + \frac{e^{-\kappa\tau} - 1}{\kappa}\right]
    $$

    $$
    = -\frac{\tau}{\kappa} + \frac{1 - e^{-\kappa\tau}}{\kappa^2} = \frac{B(\tau) + \tau \cdot 0}{\,} = B(\tau)/\kappa + ..
    $$

    More directly: $\int_0^\tau B(s)\,ds = -\frac{1}{\kappa}[\tau + B(\tau)]$ since $\int_0^\tau (1 - e^{-\kappa s})\,ds = \tau - (1 - e^{-\kappa\tau})/\kappa = \tau + B(\tau)\kappa/1$... Let me compute carefully:

    $$
    \int_0^\tau (1 - e^{-\kappa s})\,ds = \tau - \left[-\frac{e^{-\kappa s}}{\kappa}\right]_0^\tau = \tau - \frac{1 - e^{-\kappa\tau}}{\kappa} = \tau + B(\tau)
    $$

    Therefore

    $$
    \int_0^\tau B(s)\,ds = -\frac{1}{\kappa}(\tau + B(\tau))
    $$

    $$
    A_{\text{drift}}(\tau) = \kappa\theta \cdot \left(-\frac{\tau + B(\tau)}{\kappa}\right) = -\theta(\tau + B(\tau))
    $$

    **Volatility integral $A_{\text{vol}}(\tau) = \frac{1}{2}\sigma^2\int_0^\tau B(s)^2\,ds$:**

    $$
    B(s)^2 = \frac{(1 - e^{-\kappa s})^2}{\kappa^2}
    $$

    $$
    \int_0^\tau (1 - e^{-\kappa s})^2\,ds = \int_0^\tau \left(1 - 2e^{-\kappa s} + e^{-2\kappa s}\right)ds
    $$

    $$
    = \tau + \frac{2}{\kappa}(e^{-\kappa\tau} - 1) + \frac{1}{2\kappa}(1 - e^{-2\kappa\tau})
    $$

    $$
    = \tau + 2B(\tau) - \frac{B(\tau)^2\kappa}{2} \cdot \frac{2}{\kappa} + \ldots
    $$

    Let me use the known final result. We have $\int_0^\tau B(s)^2\,ds = \frac{1}{\kappa^2}[\tau + 2B(\tau) + \frac{1}{2\kappa}(1 - e^{-2\kappa\tau})]$.

    Note $1 - e^{-2\kappa\tau} = (1 - e^{-\kappa\tau})(1 + e^{-\kappa\tau})$, and $1 - e^{-\kappa\tau} = -\kappa B(\tau)$, so

    $$
    \frac{1 - e^{-2\kappa\tau}}{2\kappa} = \frac{-\kappa B(\tau)(1 + e^{-\kappa\tau})}{2\kappa} = -\frac{B(\tau)(1 + e^{-\kappa\tau})}{2}
    $$

    Therefore

    $$
    \int_0^\tau B(s)^2\,ds = \frac{1}{\kappa^2}\left[\tau + 2B(\tau) - \frac{B(\tau)(1 + e^{-\kappa\tau})}{2}\right]
    $$

    $$
    = \frac{1}{\kappa^2}\left[\tau + B(\tau)\left(2 - \frac{1 + e^{-\kappa\tau}}{2}\right)\right]
    $$

    $$
    = \frac{1}{\kappa^2}\left[\tau + B(\tau)\frac{3 - e^{-\kappa\tau}}{2}\right]
    $$

    Then

    $$
    A_{\text{vol}}(\tau) = \frac{\sigma^2}{2\kappa^2}\left[\tau + B(\tau)\frac{3 - e^{-\kappa\tau}}{2}\right]
    $$

    **Positivity of $A_{\text{vol}}$:** Since $B(s)^2 > 0$ for $s > 0$ and $\sigma^2 > 0$, the integral $\int_0^\tau B(s)^2\,ds > 0$ for all $\tau > 0$. Therefore $A_{\text{vol}}(\tau) = \frac{1}{2}\sigma^2 \int_0^\tau B(s)^2\,ds > 0$ for all $\tau > 0$. This positivity reflects the convexity benefit: volatility always increases bond prices through Jensen's inequality. $\square$

---

**Exercise 7.** Show that the bond price formula $P(t,T) = \exp(A(\tau) + B(\tau)^\top X_t)$ is a special case of the general discounted affine transform by setting $u = \mathbf{0}$ in the transform $\mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds + u^\top X_T} \mid X_t = x]$. What do the functions $\tilde{\phi}(\tau, \mathbf{0})$ and $\tilde{\psi}(\tau, \mathbf{0})$ correspond to?

??? success "Solution to Exercise 7"
    The general discounted affine transform is

    $$
    \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds + u^\top X_T} \;\Big|\; X_t = x\right] = \exp\!\bigl(\tilde{\phi}(\tau, u) + \tilde{\psi}(\tau, u)^\top x\bigr)
    $$

    where $\tilde{\phi}$ and $\tilde{\psi}$ satisfy the extended Riccati system with initial conditions $\tilde{\phi}(0, u) = 0$ and $\tilde{\psi}(0, u) = u$.

    **Setting $u = \mathbf{0}$:** The bond price is

    $$
    P(t, T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds} \cdot 1 \;\Big|\; X_t = x\right] = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds + \mathbf{0}^\top X_T} \;\Big|\; X_t = x\right]
    $$

    $$
    = \exp\!\bigl(\tilde{\phi}(\tau, \mathbf{0}) + \tilde{\psi}(\tau, \mathbf{0})^\top x\bigr)
    $$

    Comparing with $P(t, T) = \exp(A(\tau) + B(\tau)^\top x)$, we identify:

    $$
    A(\tau) = \tilde{\phi}(\tau, \mathbf{0}), \qquad B(\tau) = \tilde{\psi}(\tau, \mathbf{0})
    $$

    The initial conditions become $\tilde{\psi}(0, \mathbf{0}) = \mathbf{0} = B(0)$ and $\tilde{\phi}(0, \mathbf{0}) = 0 = A(0)$, which match the bond pricing Riccati initial conditions.

    The extended Riccati system at $u = \mathbf{0}$ reduces to the bond pricing Riccati system:

    $$
    B'(\tau) = R(B(\tau)) - \rho_1, \qquad A'(\tau) = F(B(\tau)) - \rho_0
    $$

    This confirms that $A(\tau)$ is the time-homogeneous part of the discounted log-moment generating function evaluated at zero, and $B(\tau)$ is the state-loading part. The bond price formula is the special case where the terminal payoff is $e^{\mathbf{0}^\top X_T} = 1$, i.e., the bond pays one unit of currency regardless of the terminal state. $\square$
