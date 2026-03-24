# Bond Pricing in the Affine Framework

The exponential-affine bond price formula $P(t, T) = \exp(A(\tau) + B(\tau)^\top X_t)$ is one of the most important results in fixed-income mathematics. It provides closed-form (or semi-closed-form) bond prices as a direct consequence of the affine structure of the short rate and state dynamics. This section derives the formula from the discounted expectation, presents the Riccati system for $A$ and $B$, develops the yield formula, and illustrates the framework with the Vasicek, CIR, and two-factor models.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive $P(t, T) = \exp(A(\tau) + B(\tau)^\top X_t)$ from the risk-neutral pricing formula
    2. Write the Riccati ODEs for $A(\tau)$ and $B(\tau)$ in terms of the affine parameters
    3. Compute yields, forward rates, and the yield curve as functions of the state
    4. Solve the bond pricing Riccati for Vasicek, CIR, and multi-factor models

---

## Intuition

A zero-coupon bond paying $\$1$ at maturity $T$ is worth $P(t, T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\,ds} \mid \mathcal{F}_t]$ today. If the short rate $r_t$ depends on a state vector $X_t$ through $r(X_t) = \rho_0 + \langle \rho_1, X_t \rangle$ and $X_t$ is an affine process, then the discounted expectation is a special case of the discounted transform with $u = 0$. The log-affine property guarantees that the bond price is exponential-affine in $X_t$, with the functions $A(\tau)$ and $B(\tau)$ determined by the extended Riccati system.

The financial content is simple: the bond price depends on the current state $X_t$ through a linear combination $B(\tau)^\top X_t$ whose coefficients $B(\tau)$ encode how each state variable affects the term structure at horizon $\tau$. The term $A(\tau)$ captures the convexity adjustment---the effect of randomness on the expected discount factor.

---

## Derivation of the Bond Price Formula

### The Risk-Neutral Pricing Formula

Under the risk-neutral measure $\mathbb{Q}$:

$$
P(t, T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(X_s)\,ds} \mid X_t = x\right]
$$

where $r(x) = \rho_0 + \langle \rho_1, x \rangle$ is the affine short rate.

### Application of the Discounted Transform

This is the discounted transform $\mathcal{T}(\tau, u, x)$ evaluated at $u = 0$:

$$
P(t, T) = \mathcal{T}(\tau, 0, x) = \exp\!\left(A(\tau) + \langle B(\tau), x \rangle\right)
$$

where $A(\tau) = \tilde{\phi}(\tau, 0)$ and $B(\tau) = \tilde{\psi}(\tau, 0)$.

### The Bond Pricing Riccati System

From the extended Riccati equations with $\tilde{\psi}(0) = 0$:

$$
B'(\tau) = R(B(\tau)) - \rho_1, \qquad B(0) = 0
$$

$$
A'(\tau) = F(B(\tau)) - \rho_0, \qquad A(0) = 0
$$

where $F$ and $R$ are the functions determined by the affine parameters of $X_t$.

**Theorem (Affine Bond Pricing).** Let $X_t$ be an affine process on $D = \mathbb{R}^m_+ \times \mathbb{R}^{d-m}$ with short rate $r(x) = \rho_0 + \langle \rho_1, x \rangle$. Then the zero-coupon bond price is

$$
P(t, T) = \exp\!\left(A(\tau) + \langle B(\tau), X_t \rangle\right)
$$

where $\tau = T - t$ and $A : \mathbb{R}_+ \to \mathbb{R}$, $B : \mathbb{R}_+ \to \mathbb{R}^d$ satisfy the bond pricing Riccati system above.

*Proof.* This follows directly from the Feynman-Kac theorem applied to the discounted expectation with terminal condition $h(x) = 1$ (equivalently, $u = 0$ in the exponential-affine transform). The PDE $\partial_\tau V = \mathcal{A}V - r(x)V$ with initial condition $V(0, x) = 1$ is solved by the ansatz $V(\tau, x) = \exp(A(\tau) + \langle B(\tau), x \rangle)$ with $A(0) = 0$ and $B(0) = 0$, yielding the Riccati system after separation of constant and linear terms. $\square$

---

## Explicit Solutions

### One-Factor Model with r_t = X_t

For a one-factor model with $\rho_0 = 0$, $\rho_1 = 1$, the Riccati system simplifies to:

$$
B'(\tau) = \kappa_1 B(\tau) + \frac{1}{2}\sigma_1 B(\tau)^2 - 1, \qquad B(0) = 0
$$

$$
A'(\tau) = \kappa_0 B(\tau) + \frac{1}{2}\sigma_0 B(\tau)^2, \qquad A(0) = 0
$$

**Vasicek** ($\kappa_1 = -\kappa$, $\sigma_1 = 0$, $\kappa_0 = \kappa\theta$, $\sigma_0 = \sigma^2$):

$$
B(\tau) = -\frac{1 - e^{-\kappa\tau}}{\kappa}
$$

$$
A(\tau) = \left(\frac{\sigma^2}{2\kappa^2} - \theta\right)(B(\tau) + \tau) - \frac{\sigma^2}{4\kappa}B(\tau)^2
$$

**CIR** ($\kappa_1 = -\kappa$, $\sigma_1 = \xi^2$, $\kappa_0 = \kappa\theta$, $\sigma_0 = 0$):

$$
B(\tau) = \frac{-2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}, \qquad \gamma = \sqrt{\kappa^2 + 2\xi^2}
$$

$$
A(\tau) = \frac{2\kappa\theta}{\xi^2}\log\!\left(\frac{2\gamma\,e^{(\gamma+\kappa)\tau/2}}{(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma}\right)
$$

---

## Yields and the Term Structure

### Continuously Compounded Yield

The yield $y(t, T)$ for maturity $\tau = T - t$ is:

$$
y(t, T) = -\frac{\log P(t, T)}{\tau} = -\frac{A(\tau)}{\tau} - \frac{\langle B(\tau), X_t \rangle}{\tau}
$$

Since $A$ and $B$ are deterministic functions of $\tau$, the yield is **affine in the state**:

$$
y(t, T) = \bar{a}(\tau) + \langle \bar{b}(\tau), X_t \rangle
$$

where $\bar{a}(\tau) = -A(\tau)/\tau$ and $\bar{b}(\tau) = -B(\tau)/\tau$.

### Instantaneous Forward Rate

$$
f(t, T) = -\frac{\partial}{\partial T}\log P(t, T) = -A'(\tau) - \langle B'(\tau), X_t \rangle
$$

At $T = t$ (i.e., $\tau = 0$): $f(t, t) = -A'(0) - \langle B'(0), X_t \rangle$. Using the Riccati initial conditions $B(0) = 0$:

$$
B'(0) = R(0) - \rho_1 = -\rho_1, \qquad A'(0) = F(0) - \rho_0 = -\rho_0
$$

Therefore $f(t, t) = \rho_0 + \langle \rho_1, X_t \rangle = r(X_t)$, confirming consistency.

### Long Rate

As $\tau \to \infty$ (for models where $B(\tau)/\tau \to 0$), the long rate $y(\infty) = \lim_{\tau \to \infty} y(t, T)$ depends only on the model parameters, not on $X_t$:

**Vasicek long rate**:

$$
y(\infty) = \theta - \frac{\sigma^2}{2\kappa^2}
$$

**CIR long rate**:

$$
y(\infty) = \frac{2\kappa\theta}{\gamma + \kappa}
$$

---

## Multi-Factor Bond Pricing

### Two-Factor Model

For a two-factor model with $X_t = (X_t^{(1)}, X_t^{(2)})$ and $r_t = \rho_0 + \rho_{1,1} X_t^{(1)} + \rho_{1,2} X_t^{(2)}$:

$$
P(t, T) = \exp\!\left(A(\tau) + B_1(\tau) X_t^{(1)} + B_2(\tau) X_t^{(2)}\right)
$$

The functions $B_1, B_2$ satisfy a coupled $2 \times 2$ ODE system:

$$
\begin{pmatrix} B_1' \\ B_2' \end{pmatrix} = R\!\begin{pmatrix} B_1 \\ B_2 \end{pmatrix} - \begin{pmatrix} \rho_{1,1} \\ \rho_{1,2} \end{pmatrix}
$$

If the factors are independent and $R$ is diagonal, the system decouples and each $B_i$ has its own scalar Riccati solution.

### The Yield Curve as a Function of State

The yield curve at time $t$ is the function $\tau \mapsto y(t, t+\tau)$:

$$
y(t, t+\tau) = \bar{a}(\tau) + \bar{b}_1(\tau) X_t^{(1)} + \bar{b}_2(\tau) X_t^{(2)}
$$

The shape of the yield curve is determined by the functions $\bar{a}$, $\bar{b}_1$, $\bar{b}_2$:

- $X_t^{(1)}$ might represent a "level" factor that shifts the entire curve up or down
- $X_t^{(2)}$ might represent a "slope" factor that tilts the curve

??? example "Vasicek Bond Price Calculation"
    Parameters: $\kappa = 0.5$, $\theta = 0.05$, $\sigma = 0.02$, $r_0 = 0.03$, $\tau = 5$ years.

    $$
    B(5) = -\frac{1 - e^{-2.5}}{0.5} = -\frac{1 - 0.0821}{0.5} = -1.836
    $$

    $$
    A(5) = \left(\frac{0.0004}{0.5} - 0.05\right)(-1.836 + 5) - \frac{0.0004}{2}(-1.836)^2
    $$

    $$
    = (-0.0492)(3.164) - 0.000672 = -0.1559 - 0.0007 = -0.1566
    $$

    $$
    P(0, 5) = e^{-0.1566 + (-1.836)(0.03)} = e^{-0.1566 - 0.0551} = e^{-0.2117} = 0.8092
    $$

    The 5-year yield is $y(5) = -\log(0.8092)/5 = 0.0423 = 4.23\%$. $\square$

??? example "CIR Bond Price Calculation"
    Parameters: $\kappa = 0.5$, $\theta = 0.05$, $\xi = 0.1$, $r_0 = 0.03$, $\tau = 5$ years.

    $$
    \gamma = \sqrt{0.25 + 0.02} = \sqrt{0.27} = 0.5196
    $$

    $$
    e^{\gamma \cdot 5} = e^{2.598} = 13.44
    $$

    $$
    B(5) = \frac{-2(13.44 - 1)}{(0.5196 + 0.5)(13.44 - 1) + 2(0.5196)} = \frac{-24.88}{12.68 + 1.039} = \frac{-24.88}{13.72} = -1.813
    $$

    $$
    A(5) = \frac{2(0.5)(0.05)}{0.01}\log\!\left(\frac{2(0.5196)\,e^{(1.0196)(2.5)}}{13.72}\right) = 5\log\!\left(\frac{1.039 \cdot e^{2.549}}{13.72}\right)
    $$

    $$
    = 5\log\!\left(\frac{1.039 \cdot 12.80}{13.72}\right) = 5\log(0.969) = 5(-0.0315) = -0.1575
    $$

    $$
    P(0, 5) = e^{-0.1575 + (-1.813)(0.03)} = e^{-0.1575 - 0.0544} = e^{-0.2119} = 0.8090
    $$

    The CIR and Vasicek bond prices are nearly identical for these parameter values, but they differ in their response to rate changes (the CIR convexity adjustment differs from Vasicek's). $\square$

---

## Properties of the Bond Price

### Monotonicity in the State

Since $B(\tau) < 0$ componentwise for models where $\rho_1 > 0$ (which includes all standard short-rate models), the bond price is **decreasing in the state variables**: higher rates mean lower bond prices.

### Convexity

The bond price is **convex** in the state for CIR-type models (due to the quadratic term in the Riccati equation) and **log-linear** for Vasicek-type models. This convexity has a financial meaning: uncertainty in future rates benefits the bondholder (Jensen's inequality applied to the convex function $e^{-\int r_s\,ds}$), creating a positive convexity adjustment.

### Boundary Behavior

- At $\tau = 0$: $P(t, t) = e^{A(0) + B(0)^\top x} = e^0 = 1$ (a bond at maturity pays $\$1$)
- As $\tau \to \infty$: $P(t, T) \to 0$ for positive short rates (no perpetual bond has positive value)

---

## Summary

The affine bond pricing formula $P(t, T) = \exp(A(\tau) + B(\tau)^\top X_t)$ follows from the discounted transform with terminal argument $u = 0$. The functions $A$ and $B$ satisfy the bond pricing Riccati system $B' = R(B) - \rho_1$, $A' = F(B) - \rho_0$, which has closed-form solutions for Vasicek (exponential) and CIR (ratio of exponentials with discriminant $\gamma = \sqrt{\kappa^2 + 2\xi^2}$). Yields and forward rates are affine in the state vector, producing tractable expressions for the entire term structure. Multi-factor models extend the framework by solving coupled Riccati systems, enabling the yield curve to exhibit level, slope, and curvature dynamics.

---

## Further Reading

- Duffie, D. & Kan, R. (1996). "A Yield-Factor Model of Interest Rates." *Mathematical Finance*, 6(4), 379-406.
- Brigo, D. & Mercurio, F. *Interest Rate Models - Theory and Practice*. Springer, 2007, Chapters 3-4.
- Filipovic, D. *Term-Structure Models: A Graduate Course*. Springer, 2009.
- Piazzesi, M. (2010). "Affine Term Structure Models." *Handbook of Financial Econometrics*, Volume 1, 691-766.

---

## Exercises

**Exercise 1.** Consider the Vasicek model with parameters $\kappa = 0.8$, $\theta = 0.04$, $\sigma = 0.015$, and current short rate $r_0 = 0.06$. Compute the bond price $P(0, 3)$ and the continuously compounded 3-year yield $y(0, 3)$.

---

**Exercise 2.** Starting from the bond pricing Riccati equation $B'(\tau) = -\kappa B(\tau) - 1$ with $B(0) = 0$ (Vasicek case), verify that $B(\tau) \to -1/\kappa$ as $\tau \to \infty$. Explain the financial meaning of this saturation in terms of mean reversion.

---

**Exercise 3.** In the CIR model with $\kappa = 0.5$, $\theta = 0.05$, $\xi = 0.15$, compute $\gamma = \sqrt{\kappa^2 + 2\xi^2}$ and evaluate $B(10)$ and $A(10)$. Then determine the 10-year yield as a function of $r_0$.

---

**Exercise 4.** For a two-factor model with independent factors $X_t^{(1)}$ (Vasicek with $\kappa_1 = 0.5$, $\sigma_1 = 0.01$) and $X_t^{(2)}$ (CIR with $\kappa_2 = 0.3$, $\xi_2 = 0.1$), and short rate $r_t = X_t^{(1)} + X_t^{(2)}$, write the decoupled Riccati systems for $B_1(\tau)$ and $B_2(\tau)$. Show that the two-factor bond price is $P(t, T) = P_1(t, T) \cdot P_2(t, T)$, where $P_i$ are the one-factor bond prices.

---

**Exercise 5.** Derive the Vasicek long rate $y(\infty) = \theta - \sigma^2 / (2\kappa^2)$ by computing $\lim_{\tau \to \infty} y(t, t+\tau)$ using the explicit expressions for $A(\tau)$ and $B(\tau)$. Under what condition on the parameters is the long rate negative?

---

**Exercise 6.** Prove that the instantaneous forward rate $f(t, T) = -A'(\tau) - B'(\tau) X_t$ satisfies $f(t, t) = r(X_t)$ by evaluating $A'(0)$ and $B'(0)$ from the Riccati initial conditions.

---

**Exercise 7.** Consider the CIR bond pricing formula. Show that $P(t, T)$ is a **convex** function of $r_t$ by computing $\partial^2 P / \partial r_t^2$ and verifying it is positive. Interpret this convexity in terms of Jensen's inequality applied to the discount factor $e^{-\int_t^T r_s\,ds}$.
