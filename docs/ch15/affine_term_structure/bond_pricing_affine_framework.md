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

Recall (see [§ Discounted Transform](../discounted_transform/discounted_characteristic_function.md)): the bond price is the discounted transform $\mathcal{T}(\tau, u, x)$ evaluated at $u = 0$,

$$
P(t, T) = \mathcal{T}(\tau, 0, x) = \exp\!\left(A(\tau) + \langle B(\tau), x \rangle\right),
$$

with $A(\tau) = \tilde{\phi}(\tau, 0)$ and $B(\tau) = \tilde{\psi}(\tau, 0)$.

### The Bond Pricing Riccati System

Specializing the extended Riccati system (see [§ Characteristic Function](../characteristic_function/characteristic_function.md)) to $\tilde{\psi}(0) = 0$:

$$
B'(\tau) = R(B(\tau)) - \rho_1, \qquad B(0) = 0
$$

$$
A'(\tau) = F(B(\tau)) - \rho_0, \qquad A(0) = 0
$$

where $F$ and $R$ are determined by the affine parameters of $X_t$.

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

Recall (see [§ Vasicek and CIR as Affine](../examples/gbm_as_affine.md), [§ Vasicek Model](../../ch18/vasicek_model/vasicek_sde_and_ou_process.md), [§ CIR Model](../../ch18/cir_model/cir_sde_and_square_root_process.md)): closed-form solutions for Vasicek ($\sigma_1=0$) and CIR ($\sigma_1=\xi^2$, discriminant $\gamma = \sqrt{\kappa^2 + 2\xi^2}$).

---

## Yields and the Term Structure

Recall (see [§ Yield Curve Dynamics](yield_curve_dynamics.md)): the yield and instantaneous forward rate are affine in the state,

$$
y(t, T) = \bar{a}(\tau) + \langle \bar{b}(\tau), X_t \rangle, \qquad f(t, T) = -A'(\tau) - \langle B'(\tau), X_t \rangle,
$$

with $\bar{a}(\tau) = -A(\tau)/\tau$, $\bar{b}(\tau) = -B(\tau)/\tau$. The consistency check $f(t, t) = r(X_t)$ follows from the Riccati initial conditions $B'(0) = -\rho_1$, $A'(0) = -\rho_0$.

### Long Rate

As $\tau \to \infty$ (for models where $B(\tau)/\tau \to 0$), the long rate $y(\infty) = \lim_{\tau \to \infty} y(t, T)$ depends only on the model parameters, not on $X_t$. Recall (see [§ Vasicek Model](../../ch18/vasicek_model/vasicek_sde_and_ou_process.md), [§ CIR Model](../../ch18/cir_model/cir_sde_and_square_root_process.md)): Vasicek gives $y(\infty) = \theta - \sigma^2/(2\kappa^2)$; CIR gives $y(\infty) = 2\kappa\theta/(\gamma+\kappa)$.

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

??? success "Solution to Exercise 1"
    With $\kappa = 0.8$, $\theta = 0.04$, $\sigma = 0.015$, $r_0 = 0.06$, and $\tau = 3$:

    **Step 1: Compute $B(3)$.**

    $$
    B(3) = -\frac{1 - e^{-0.8 \times 3}}{0.8} = -\frac{1 - e^{-2.4}}{0.8} = -\frac{1 - 0.09072}{0.8} = -\frac{0.90928}{0.8} = -1.1366
    $$

    **Step 2: Compute $A(3)$.**

    $$
    A(3) = \left(\frac{\sigma^2}{2\kappa^2} - \theta\right)(B(3) + \tau) - \frac{\sigma^2}{4\kappa}B(3)^2
    $$

    $$
    = \left(\frac{0.000225}{1.28} - 0.04\right)(-1.1366 + 3) - \frac{0.000225}{3.2}(1.1366)^2
    $$

    $$
    = (0.0001758 - 0.04)(1.8634) - 0.0000703 \times 1.2919
    $$

    $$
    = (-0.03982)(1.8634) - 0.0000908 = -0.07420 - 0.0000908 = -0.07429
    $$

    **Step 3: Compute $P(0, 3)$.**

    $$
    P(0, 3) = e^{A(3) + B(3) \cdot r_0} = e^{-0.07429 + (-1.1366)(0.06)} = e^{-0.07429 - 0.06820} = e^{-0.14249} = 0.8673
    $$

    **Step 4: Compute $y(0, 3)$.**

    $$
    y(0, 3) = -\frac{\ln P(0, 3)}{3} = -\frac{\ln 0.8673}{3} = -\frac{-0.14249}{3} = 0.04750 = 4.75\%
    $$

    The 3-year yield of 4.75% lies between the current short rate $r_0 = 6\%$ and the long-run mean $\theta = 4\%$, reflecting the mean-reverting pull of the Vasicek model.

---

**Exercise 2.** Starting from the bond pricing Riccati equation $B'(\tau) = -\kappa B(\tau) - 1$ with $B(0) = 0$ (Vasicek case), verify that $B(\tau) \to -1/\kappa$ as $\tau \to \infty$. Explain the financial meaning of this saturation in terms of mean reversion.

??? success "Solution to Exercise 2"
    The Vasicek Riccati ODE for $B(\tau)$ is $B'(\tau) = -\kappa B(\tau) - 1$ with $B(0) = 0$. The solution is $B(\tau) = -(1 - e^{-\kappa\tau})/\kappa$.

    **Limiting behavior as $\tau \to \infty$:**

    $$
    \lim_{\tau \to \infty} B(\tau) = \lim_{\tau \to \infty} -\frac{1 - e^{-\kappa\tau}}{\kappa} = -\frac{1 - 0}{\kappa} = -\frac{1}{\kappa}
    $$

    **Verification via the ODE:** At the steady state $B^* = -1/\kappa$, the ODE gives $B'(\infty) = -\kappa(-1/\kappa) - 1 = 1 - 1 = 0$, confirming that $B^* = -1/\kappa$ is a fixed point.

    **Financial interpretation:** The saturation $|B(\tau)| \to 1/\kappa$ means that the sensitivity of the log bond price to the current short rate is bounded. This is a direct consequence of mean reversion: a shock to $r_t$ decays at rate $\kappa$, so the cumulative effect on the integrated discount factor $\int_t^T r_s\,ds$ is finite even as $T \to \infty$. Specifically, the impulse response of the short rate to a unit shock is $e^{-\kappa s}$, and the total integrated effect is $\int_0^\infty e^{-\kappa s}\,ds = 1/\kappa$, which equals the saturation level $|B(\infty)|$.

---

**Exercise 3.** In the CIR model with $\kappa = 0.5$, $\theta = 0.05$, $\xi = 0.15$, compute $\gamma = \sqrt{\kappa^2 + 2\xi^2}$ and evaluate $B(10)$ and $A(10)$. Then determine the 10-year yield as a function of $r_0$.

??? success "Solution to Exercise 3"
    **Step 1: Compute $\gamma$.**

    $$
    \gamma = \sqrt{\kappa^2 + 2\xi^2} = \sqrt{0.25 + 2(0.0225)} = \sqrt{0.25 + 0.045} = \sqrt{0.295} = 0.5431
    $$

    **Step 2: Compute $B(10)$.**

    $$
    e^{\gamma \cdot 10} = e^{5.431} = 228.4
    $$

    $$
    B(10) = \frac{-2(228.4 - 1)}{(0.5431 + 0.5)(228.4 - 1) + 2(0.5431)} = \frac{-2(227.4)}{1.0431 \times 227.4 + 1.0862}
    $$

    $$
    = \frac{-454.8}{237.2 + 1.086} = \frac{-454.8}{238.3} = -1.908
    $$

    **Step 3: Compute $A(10)$.**

    $$
    A(10) = \frac{2\kappa\theta}{\xi^2}\ln\!\left(\frac{2\gamma\,e^{(\gamma+\kappa)\tau/2}}{(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma}\right)
    $$

    $$
    = \frac{2(0.5)(0.05)}{0.0225}\ln\!\left(\frac{2(0.5431)\,e^{(1.0431)(5)}}{238.3}\right)
    $$

    $$
    = 2.222\,\ln\!\left(\frac{1.0862\,e^{5.216}}{238.3}\right) = 2.222\,\ln\!\left(\frac{1.0862 \times 184.5}{238.3}\right)
    $$

    $$
    = 2.222\,\ln\!\left(\frac{200.4}{238.3}\right) = 2.222\,\ln(0.8411) = 2.222 \times (-0.1731) = -0.3846
    $$

    **Step 4: 10-year yield as a function of $r_0$.**

    $$
    y(0, 10) = -\frac{A(10)}{10} - \frac{B(10)}{10}\,r_0 = \frac{0.3846}{10} + \frac{1.908}{10}\,r_0 = 0.03846 + 0.1908\,r_0
    $$

    The yield is an affine function of the initial short rate $r_0$.

---

**Exercise 4.** For a two-factor model with independent factors $X_t^{(1)}$ (Vasicek with $\kappa_1 = 0.5$, $\sigma_1 = 0.01$) and $X_t^{(2)}$ (CIR with $\kappa_2 = 0.3$, $\xi_2 = 0.1$), and short rate $r_t = X_t^{(1)} + X_t^{(2)}$, write the decoupled Riccati systems for $B_1(\tau)$ and $B_2(\tau)$. Show that the two-factor bond price is $P(t, T) = P_1(t, T) \cdot P_2(t, T)$, where $P_i$ are the one-factor bond prices.

??? success "Solution to Exercise 4"
    **Decoupled Riccati systems.** Since the factors are independent and the short rate is $r_t = X_t^{(1)} + X_t^{(2)}$, we have $\rho_0 = 0$, $\rho_1 = (1, 1)^\top$.

    **Factor 1** (Vasicek with $\kappa_1 = 0.5$, $\sigma_1 = 0.01$): The Riccati ODE is linear:

    $$
    B_1'(\tau) = -\kappa_1 B_1(\tau) - 1, \quad B_1(0) = 0
    $$

    $$
    B_1(\tau) = -\frac{1 - e^{-\kappa_1\tau}}{\kappa_1}
    $$

    $$
    A_1'(\tau) = \frac{1}{2}\sigma_1^2 B_1(\tau)^2, \quad A_1(0) = 0
    $$

    (Note: $K_0^{(1)} = 0$ if we use $X_t^{(1)}$ centered; otherwise $A_1$ also picks up the drift term $\kappa_1\theta_1 B_1$.)

    **Factor 2** (CIR with $\kappa_2 = 0.3$, $\xi_2 = 0.1$): The Riccati ODE is nonlinear:

    $$
    B_2'(\tau) = -\kappa_2 B_2(\tau) + \frac{1}{2}\xi_2^2 B_2(\tau)^2 - 1, \quad B_2(0) = 0
    $$

    with $\gamma_2 = \sqrt{\kappa_2^2 + 2\xi_2^2}$, solved by the CIR formula for $B_2(\tau)$.

    **Factorization of the bond price.** Since the factors are independent:

    $$
    P(t, T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T (X_s^{(1)} + X_s^{(2)})\,ds} \mid \mathcal{F}_t\right]
    $$

    By independence of $X^{(1)}$ and $X^{(2)}$, the expectation factors:

    $$
    = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T X_s^{(1)}\,ds} \mid \mathcal{F}_t\right] \cdot \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T X_s^{(2)}\,ds} \mid \mathcal{F}_t\right]
    $$

    $$
    = P_1(t, T) \cdot P_2(t, T)
    $$

    where $P_i(t, T) = \exp(A_i(\tau) + B_i(\tau) X_t^{(i)})$ is the one-factor bond price for each component. The total bond price satisfies $A(\tau) = A_1(\tau) + A_2(\tau)$ and $B(\tau) = (B_1(\tau), B_2(\tau))^\top$.

---

**Exercise 5.** Derive the Vasicek long rate $y(\infty) = \theta - \sigma^2 / (2\kappa^2)$ by computing $\lim_{\tau \to \infty} y(t, t+\tau)$ using the explicit expressions for $A(\tau)$ and $B(\tau)$. Under what condition on the parameters is the long rate negative?

??? success "Solution to Exercise 5"
    **Vasicek yield formula.** With $B(\tau) = -(1 - e^{-\kappa\tau})/\kappa$ and $A(\tau) = (\theta - \sigma^2/(2\kappa^2))(B(\tau) + \tau) - \sigma^2 B(\tau)^2/(4\kappa)$:

    $$
    y(t, t+\tau) = -\frac{A(\tau)}{\tau} - \frac{B(\tau)}{\tau}\,r_t
    $$

    **Factor loading term:**

    $$
    -\frac{B(\tau)}{\tau} = \frac{1 - e^{-\kappa\tau}}{\kappa\tau} \to 0 \quad \text{as } \tau \to \infty
    $$

    **Intercept term:** Define $\ell = \theta - \sigma^2/(2\kappa^2)$.

    $$
    -\frac{A(\tau)}{\tau} = -\frac{\ell(B(\tau) + \tau)}{\tau} + \frac{\sigma^2 B(\tau)^2}{4\kappa\tau}
    $$

    $$
    = -\ell\frac{B(\tau)}{\tau} - \ell + \frac{\sigma^2 B(\tau)^2}{4\kappa\tau}
    $$

    As $\tau \to \infty$: $B(\tau)/\tau \to 0$, $B(\tau)^2/\tau \to 1/(\kappa^2 \tau) \to 0$, so

    $$
    \lim_{\tau \to \infty} y(t, t+\tau) = 0 - \ell + 0 + \ell \cdot 0 = -(-\theta + \sigma^2/(2\kappa^2)) = \theta - \frac{\sigma^2}{2\kappa^2}
    $$

    **Condition for negative long rate:** The long rate is negative when

    $$
    \theta - \frac{\sigma^2}{2\kappa^2} < 0 \quad \Longleftrightarrow \quad \sigma^2 > 2\kappa^2\theta \quad \Longleftrightarrow \quad \frac{\sigma}{\kappa} > \sqrt{2\theta}
    $$

    This occurs when volatility is high relative to mean reversion and the long-run mean. For example, with $\theta = 0.05$ and $\kappa = 0.1$, the long rate is negative if $\sigma > 0.1\sqrt{0.1} \approx 0.0316$.

---

**Exercise 6.** Prove that the instantaneous forward rate $f(t, T) = -A'(\tau) - B'(\tau) X_t$ satisfies $f(t, t) = r(X_t)$ by evaluating $A'(0)$ and $B'(0)$ from the Riccati initial conditions.

??? success "Solution to Exercise 6"
    The forward rate at $\tau = T - t$ is $f(t, T) = -A'(\tau) - B'(\tau) X_t$.

    **Step 1: Evaluate $A'(0)$ using the Riccati ODE.**

    $$
    A'(\tau) = F(B(\tau)) - \rho_0 = K_0^\top B(\tau) + \frac{1}{2}B(\tau)^\top H_0 B(\tau) - \rho_0
    $$

    At $\tau = 0$, with $B(0) = 0$:

    $$
    A'(0) = K_0^\top \cdot 0 + \frac{1}{2} \cdot 0^\top H_0 \cdot 0 - \rho_0 = -\rho_0
    $$

    **Step 2: Evaluate $B'(0)$ using the Riccati ODE.**

    $$
    B'(\tau) = R(B(\tau)) - \rho_1 = K_1^\top B(\tau) + \frac{1}{2}\sum_{i=1}^d (B^\top H_i B)\,e_i - \rho_1
    $$

    At $\tau = 0$, with $B(0) = 0$:

    $$
    B'(0) = K_1^\top \cdot 0 + 0 - \rho_1 = -\rho_1
    $$

    **Step 3: Compute $f(t, t)$.**

    $$
    f(t, t) = -A'(0) - B'(0)^\top X_t = -(-\rho_0) - (-\rho_1)^\top X_t = \rho_0 + \rho_1^\top X_t = r(X_t)
    $$

    This confirms the consistency condition: the instantaneous forward rate at the current date equals the short rate. $\square$

---

**Exercise 7.** Consider the CIR bond pricing formula. Show that $P(t, T)$ is a **convex** function of $r_t$ by computing $\partial^2 P / \partial r_t^2$ and verifying it is positive. Interpret this convexity in terms of Jensen's inequality applied to the discount factor $e^{-\int_t^T r_s\,ds}$.

??? success "Solution to Exercise 7"
    The CIR bond price is $P(t, T) = \exp(A(\tau) + B(\tau) r_t)$ where $B(\tau) < 0$ for $\tau > 0$.

    **Step 1: First derivative.**

    $$
    \frac{\partial P}{\partial r_t} = B(\tau)\,P(t, T)
    $$

    Since $B(\tau) < 0$ and $P > 0$, this is negative, confirming that bond prices decrease with higher rates.

    **Step 2: Second derivative.**

    $$
    \frac{\partial^2 P}{\partial r_t^2} = B(\tau)^2\,P(t, T)
    $$

    Since $B(\tau)^2 > 0$ and $P(t, T) > 0$, we have $\partial^2 P / \partial r_t^2 > 0$ for all $\tau > 0$ and all $r_t \geq 0$. Therefore $P(t, T)$ is a **convex** function of $r_t$.

    **Jensen's inequality interpretation.** The bond price is defined as

    $$
    P(t, T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds} \;\Big|\; r_t\right]
    $$

    The function $r \mapsto e^{-\int_t^T r_s\,ds}$ is convex in the path of rates. By Jensen's inequality applied to this convex functional:

    $$
    \mathbb{E}\!\left[e^{-\int_t^T r_s\,ds}\right] \geq e^{-\mathbb{E}[\int_t^T r_s\,ds]}
    $$

    The left side is the bond price; the right side is the price that would obtain if rates followed their expected path with no randomness. The difference is the **convexity adjustment** --- it is always non-negative and increases with the volatility of rates. In the CIR model, this convexity is captured by the interplay between $A(\tau)$ (which includes the variance effect) and $B(\tau)$ (which is more negative than in a zero-volatility model). Bondholders benefit from rate volatility precisely because of this convexity effect.
