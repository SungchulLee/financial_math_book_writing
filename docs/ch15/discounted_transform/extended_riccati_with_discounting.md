# Extended Riccati System with Discounting

Derivative pricing requires not only the distribution of the future state $X_T$ but also the discount factor $e^{-\int_t^T r(X_s)\,ds}$ that translates future payoffs into present values. When the short rate is affine in the state, $r(x) = \rho_0 + \langle \rho_1, x \rangle$, the discounted expectation retains the exponential-affine form, but the Riccati system acquires additional terms from the discounting. This section derives the extended Riccati equations, connects them to bond pricing, and works through the key examples.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the discounted transform formula with exponential-affine structure
    2. Derive the extended Riccati ODEs incorporating the discount rate coefficients $\rho_0$ and $\rho_1$
    3. Specialize the system to zero-coupon bond pricing
    4. Solve the extended system for Vasicek and CIR models

---

## Intuition

In the undiscounted setting, the Riccati system governs the characteristic function $\mathbb{E}[e^{\langle u, X_T \rangle} \mid X_t = x]$. For pricing, we need $\mathbb{E}[e^{-\int_t^T r_s\,ds + \langle u, X_T \rangle} \mid X_t = x]$, which combines time-discounting with a terminal payoff. The discount factor $e^{-\int_t^T r_s\,ds}$ acts as a running "penalty" that accumulates along the path. When $r(x)$ is affine, this penalty introduces additional linear terms into the backward Kolmogorov PDE, which propagate into the Riccati system as additive corrections to the $\phi$- and $\psi$-equations.

The result is elegant: discounting modifies the Riccati system by subtracting $\rho_0$ from the $\phi$-equation and subtracting $\rho_1$ from the $\psi$-equation. The exponential-affine structure is preserved.

---

## The Discounted Transform

### Statement

**Definition (Discounted Transform).** Let $X_t$ be an affine process on $D$ with short rate $r(x) = \rho_0 + \langle \rho_1, x \rangle$. The *discounted transform* is

$$
\mathcal{T}(\tau, u, x) := \mathbb{E}\!\left[e^{-\int_t^T r(X_s)\,ds + \langle u, X_T \rangle} \mid X_t = x\right]
$$

where $\tau = T - t$. For an affine process, this has the exponential-affine form:

$$
\mathcal{T}(\tau, u, x) = \exp\!\left(\tilde{\phi}(\tau, u) + \langle \tilde{\psi}(\tau, u), x \rangle\right)
$$

with initial conditions $\tilde{\phi}(0, u) = 0$ and $\tilde{\psi}(0, u) = u$.

### Derivation

Define $g(\tau, x) = \mathcal{T}(\tau, u, x)$. The function $g$ satisfies the PDE:

$$
\frac{\partial g}{\partial \tau} = \mathcal{A}g - r(x)\,g
$$

where $\mathcal{A}$ is the infinitesimal generator of $X_t$. The term $-r(x)g$ comes from the discount factor: the Feynman-Kac theorem states that the discounted conditional expectation satisfies a PDE with a "killing" rate $r(x)$.

Substituting the ansatz $g = \exp(\tilde{\phi} + \langle \tilde{\psi}, x \rangle)$ and using the affine structure of $\mathcal{A}$ and $r(x)$:

$$
\tilde{\phi}' + \langle \tilde{\psi}', x \rangle = F(\tilde{\psi}) + \langle R(\tilde{\psi}), x \rangle - \rho_0 - \langle \rho_1, x \rangle
$$

Matching constant and linear terms:

$$
\tilde{\phi}'(\tau) = F(\tilde{\psi}(\tau)) - \rho_0
$$

$$
\tilde{\psi}'(\tau) = R(\tilde{\psi}(\tau)) - \rho_1
$$

---

## The Extended Riccati System

### General Form

The extended Riccati system with discounting is:

$$
\frac{\partial \tilde{\phi}}{\partial \tau} = F(\tilde{\psi}) - \rho_0, \qquad \tilde{\phi}(0, u) = 0
$$

$$
\frac{\partial \tilde{\psi}}{\partial \tau} = R(\tilde{\psi}) - \rho_1, \qquad \tilde{\psi}(0, u) = u
$$

The only difference from the undiscounted system is the subtraction of $\rho_0$ and $\rho_1$. This modification shifts the equilibria of the $\tilde{\psi}$-equation and changes the integration constant in $\tilde{\phi}$, but preserves the overall structure.

### Scalar Case

For a one-dimensional affine process with $r(x) = \rho_0 + \rho_1 x$:

$$
\tilde{\psi}'(\tau) = \kappa_1\tilde{\psi}(\tau) + \frac{1}{2}\sigma_1\tilde{\psi}(\tau)^2 - \rho_1, \qquad \tilde{\psi}(0) = u
$$

$$
\tilde{\phi}'(\tau) = \kappa_0\tilde{\psi}(\tau) + \frac{1}{2}\sigma_0\tilde{\psi}(\tau)^2 - \rho_0, \qquad \tilde{\phi}(0) = 0
$$

The $\tilde{\psi}$-equation is now a *full* Riccati equation $\tilde{\psi}' = \alpha + \beta\tilde{\psi} + \frac{1}{2}\gamma\tilde{\psi}^2$ with constant term $\alpha = -\rho_1$, linear term $\beta = \kappa_1$, and quadratic term $\gamma = \sigma_1$.

---

## Bond Pricing Application

### Zero-Coupon Bond Price

The zero-coupon bond price is the discounted transform with $u = 0$:

$$
P(t, T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(X_s)\,ds} \mid X_t = x\right] = \exp\!\left(A(\tau) + \langle B(\tau), x \rangle\right)
$$

where $A(\tau) = \tilde{\phi}(\tau, 0)$ and $B(\tau) = \tilde{\psi}(\tau, 0)$ satisfy:

$$
A'(\tau) = F(B(\tau)) - \rho_0, \qquad A(0) = 0
$$

$$
B'(\tau) = R(B(\tau)) - \rho_1, \qquad B(0) = 0
$$

The initial condition $B(0) = 0$ reflects the fact that at maturity, the bond pays $\$1$ regardless of the state.

### One-Factor Short Rate Models

For a one-factor model where $X_t = r_t$ and $r(x) = x$ (so $\rho_0 = 0$, $\rho_1 = 1$):

$$
B'(\tau) = \kappa_1 B(\tau) + \frac{1}{2}\sigma_1 B(\tau)^2 - 1, \qquad B(0) = 0
$$

$$
A'(\tau) = \kappa_0 B(\tau) + \frac{1}{2}\sigma_0 B(\tau)^2, \qquad A(0) = 0
$$

??? example "Vasicek Bond Pricing"
    For the Vasicek model ($\kappa_1 = -\kappa$, $\sigma_1 = 0$):

    $$
    B'(\tau) = -\kappa B(\tau) - 1, \qquad B(0) = 0
    $$

    This linear ODE has the solution:

    $$
    B(\tau) = -\frac{1 - e^{-\kappa\tau}}{\kappa}
    $$

    Note $B(\tau) < 0$, so the bond price $P = e^{A + Br}$ is decreasing in $r$, as expected (higher rates mean lower bond prices).

    The $A$-equation gives:

    $$
    A(\tau) = \kappa\theta \int_0^\tau B(s)\,ds + \frac{\sigma^2}{2}\int_0^\tau B(s)^2\,ds
    $$

    After integration:

    $$
    A(\tau) = -\theta\!\left(\tau + \frac{e^{-\kappa\tau} - 1}{\kappa}\right) + \frac{\sigma^2}{2\kappa^2}\!\left(\tau + \frac{2(e^{-\kappa\tau} - 1)}{\kappa} + \frac{1 - e^{-2\kappa\tau}}{2\kappa}\right)
    $$

    which can be simplified to the standard Vasicek bond price formula. $\square$

??? example "CIR Bond Pricing"
    For the CIR model ($\kappa_1 = -\kappa$, $\sigma_1 = \xi^2$, $\kappa_0 = \kappa\theta$, $\sigma_0 = 0$):

    $$
    B'(\tau) = -\kappa B(\tau) + \frac{\xi^2}{2}B(\tau)^2 - 1, \qquad B(0) = 0
    $$

    This is a full Riccati equation. Define $\gamma = \sqrt{\kappa^2 + 2\xi^2}$. The solution is:

    $$
    B(\tau) = \frac{-2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
    $$

    The $A$-equation integrates to:

    $$
    A(\tau) = \frac{2\kappa\theta}{\xi^2}\log\!\left(\frac{2\gamma\,e^{(\gamma+\kappa)\tau/2}}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right)
    $$

    The bond price is $P(t, T) = e^{A(\tau) + B(\tau)r_t}$, which is always positive and decreasing in $r_t$. When $2\kappa\theta \geq \xi^2$ (Feller condition), the short rate stays positive, ensuring economically meaningful yields. $\square$

---

## Yield and Forward Rate

### Continuously Compounded Yield

The yield $y(t, T)$ is defined by $P(t, T) = e^{-y(t,T)\tau}$, so:

$$
y(t, T) = -\frac{A(\tau) + \langle B(\tau), x \rangle}{\tau}
$$

Since $A$ and $B$ are deterministic functions of $\tau$, the yield is affine in the state:

$$
y(t, T) = -\frac{A(\tau)}{\tau} - \frac{\langle B(\tau), x \rangle}{\tau}
$$

This is the **affine yield** property: the entire yield curve is a linear function of the current state $x$.

### Instantaneous Forward Rate

The forward rate $f(t, T) = -\frac{\partial}{\partial T}\log P(t, T)$ is:

$$
f(t, T) = -A'(\tau) - \langle B'(\tau), x \rangle
$$

which is also affine in $x$. The short rate is recovered as $f(t, t) = -A'(0) - \langle B'(0), x \rangle = \rho_0 + \langle \rho_1, x \rangle = r(x)$, confirming consistency.

---

## Discounted Characteristic Function

For derivative pricing (not just bonds), we need the full discounted characteristic function with $u \neq 0$. Setting $u = iv$ gives:

$$
\mathbb{E}\!\left[e^{-\int_t^T r_s\,ds + i\langle v, X_T \rangle} \mid X_t = x\right] = \exp\!\left(\tilde{\phi}(\tau, iv) + \langle \tilde{\psi}(\tau, iv), x \rangle\right)
$$

This is the building block for Fourier inversion pricing of European options. The extended Riccati system must be solved with complex initial data $\tilde{\psi}(0) = iv$, producing complex-valued solutions for $\tilde{\phi}$ and $\tilde{\psi}$.

---

## Summary

The extended Riccati system with discounting modifies the standard system by subtracting the short rate coefficients: $\tilde{\phi}' = F(\tilde{\psi}) - \rho_0$ and $\tilde{\psi}' = R(\tilde{\psi}) - \rho_1$. For bond pricing, setting $u = 0$ gives the exponential-affine bond price $P(t, T) = e^{A(\tau) + B(\tau)^\top x}$, where $A$ and $B$ satisfy the bond-pricing Riccati system. The Vasicek model yields a linear ODE for $B$ with exponential solution, while the CIR model yields a genuine Riccati equation with a solution involving the discriminant $\gamma = \sqrt{\kappa^2 + 2\xi^2}$. Yields and forward rates inherit the affine structure, giving the entire term structure as a linear function of the state.

---

## Further Reading

- Duffie, D. & Kan, R. (1996). "A Yield-Factor Model of Interest Rates." *Mathematical Finance*, 6(4), 379-406.
- Cox, J. C., Ingersoll, J. E., & Ross, S. A. (1985). "A Theory of the Term Structure of Interest Rates." *Econometrica*, 53(2), 385-407.
- Filipovic, D. *Term-Structure Models: A Graduate Course*. Springer, 2009, Chapter 5.
