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

---

## Exercises

**Exercise 1.** For the Vasicek model with short rate $r_t = X_t$, write the extended Riccati system $\tilde{\phi}' = F(\tilde{\psi}) - \rho_0$ and $\tilde{\psi}' = R(\tilde{\psi}) - \rho_1$ with $\rho_0 = 0$ and $\rho_1 = 1$. Solve for the bond pricing functions $A(\tau)$ and $B(\tau)$ with initial conditions $A(0) = 0$, $B(0) = 0$ and verify the well-known Vasicek bond price formula.

??? success "Solution to Exercise 1"
    For the Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ with $r_t = X_t$, the affine parameters are $\kappa_0 = \kappa\theta$, $\kappa_1 = -\kappa$, $\sigma_0 = \sigma^2$, $\sigma_1 = 0$, $\rho_0 = 0$, $\rho_1 = 1$.

    The extended Riccati system is:

    $$
    \tilde{\psi}'(\tau) = \kappa_1 \tilde{\psi} + \tfrac{1}{2}\sigma_1 \tilde{\psi}^2 - \rho_1 = -\kappa \tilde{\psi} - 1, \qquad \tilde{\psi}(0) = 0
    $$

    $$
    \tilde{\phi}'(\tau) = \kappa_0 \tilde{\psi} + \tfrac{1}{2}\sigma_0 \tilde{\psi}^2 - \rho_0 = \kappa\theta \tilde{\psi} + \tfrac{1}{2}\sigma^2 \tilde{\psi}^2, \qquad \tilde{\phi}(0) = 0
    $$

    **Solving for $B(\tau) = \tilde{\psi}(\tau)$:** The linear ODE $B' = -\kappa B - 1$ with $B(0) = 0$ has the integrating factor $e^{\kappa\tau}$. Multiplying: $(e^{\kappa\tau}B)' = -e^{\kappa\tau}$, so $e^{\kappa\tau}B = -\frac{e^{\kappa\tau} - 1}{\kappa}$, giving

    $$
    B(\tau) = -\frac{1 - e^{-\kappa\tau}}{\kappa}
    $$

    **Solving for $A(\tau) = \tilde{\phi}(\tau)$:** Integrating $A' = \kappa\theta B + \frac{1}{2}\sigma^2 B^2$:

    $$
    A(\tau) = \kappa\theta\int_0^\tau B(s)\,ds + \frac{\sigma^2}{2}\int_0^\tau B(s)^2\,ds
    $$

    Computing each integral with $B(s) = -\frac{1 - e^{-\kappa s}}{\kappa}$:

    $$
    \int_0^\tau B(s)\,ds = -\frac{1}{\kappa}\left(\tau - \frac{1 - e^{-\kappa\tau}}{\kappa}\right) = -\frac{\tau}{\kappa} + \frac{1 - e^{-\kappa\tau}}{\kappa^2}
    $$

    $$
    \int_0^\tau B(s)^2\,ds = \frac{1}{\kappa^2}\left(\tau - \frac{2(1 - e^{-\kappa\tau})}{\kappa} + \frac{1 - e^{-2\kappa\tau}}{2\kappa}\right)
    $$

    Combining:

    $$
    A(\tau) = -\theta\!\left(\tau + \frac{e^{-\kappa\tau} - 1}{\kappa}\right) + \frac{\sigma^2}{2\kappa^2}\!\left(\tau + \frac{2(e^{-\kappa\tau} - 1)}{\kappa} + \frac{1 - e^{-2\kappa\tau}}{2\kappa}\right)
    $$

    The bond price is $P(t, T) = e^{A(\tau) + B(\tau)r_t}$, which is the standard Vasicek formula.

---

**Exercise 2.** For the CIR model, the bond pricing Riccati equation is $B'(\tau) = -1 - \kappa B + \frac{\xi^2}{2}B^2$. Define $\gamma = \sqrt{\kappa^2 + 2\xi^2}$ and verify by direct substitution that

$$
B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
$$

satisfies this ODE with $B(0) = 0$.

??? success "Solution to Exercise 2"
    We need to verify that $B(\tau) = \frac{-2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}$ satisfies $B' = -1 - \kappa B + \frac{\xi^2}{2}B^2$ with $B(0) = 0$.

    **Initial condition:** At $\tau = 0$, $e^{\gamma \cdot 0} - 1 = 0$, so $B(0) = \frac{-2 \cdot 0}{0 + 2\gamma} = 0$. Verified.

    **ODE verification:** Write $B = -2N/D$ where $N = e^{\gamma\tau} - 1$ and $D = (\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma$. Then $N' = \gamma e^{\gamma\tau}$ and $D' = (\gamma + \kappa)\gamma e^{\gamma\tau}$.

    $$
    B' = -2\frac{N'D - ND'}{D^2} = -2\frac{\gamma e^{\gamma\tau} D - (e^{\gamma\tau} - 1)(\gamma + \kappa)\gamma e^{\gamma\tau}}{D^2}
    $$

    The numerator simplifies to $-2\gamma e^{\gamma\tau}[D - (\gamma + \kappa)(e^{\gamma\tau} - 1)] = -2\gamma e^{\gamma\tau} \cdot 2\gamma = -4\gamma^2 e^{\gamma\tau}$.

    So $B' = -4\gamma^2 e^{\gamma\tau}/D^2$. On the other hand, computing $-1 - \kappa B + \frac{\xi^2}{2}B^2$:

    $$
    -1 + \frac{2\kappa N}{D} + \frac{\xi^2}{2}\cdot\frac{4N^2}{D^2} = \frac{-D^2 + 2\kappa ND + 2\xi^2 N^2}{D^2}
    $$

    Expanding the numerator with $\gamma^2 = \kappa^2 + 2\xi^2$ and $D = (\gamma + \kappa)N + 2\gamma$:

    $$
    -D^2 + 2\kappa ND + 2\xi^2 N^2 = -[(\gamma+\kappa)N + 2\gamma]^2 + 2\kappa N[(\gamma+\kappa)N + 2\gamma] + 2\xi^2 N^2
    $$

    Expanding: $-(\gamma+\kappa)^2 N^2 - 4\gamma(\gamma+\kappa)N - 4\gamma^2 + 2\kappa(\gamma+\kappa)N^2 + 4\kappa\gamma N + 2\xi^2 N^2$.

    The $N^2$ coefficient: $-(\gamma+\kappa)^2 + 2\kappa(\gamma+\kappa) + 2\xi^2 = -\gamma^2 + \kappa^2 + 2\xi^2 = -\gamma^2 + \gamma^2 = 0$.

    The $N$ coefficient: $-4\gamma(\gamma+\kappa) + 4\kappa\gamma = -4\gamma^2$.

    The constant: $-4\gamma^2$.

    So the numerator is $-4\gamma^2 N - 4\gamma^2 = -4\gamma^2(N + 1) = -4\gamma^2 e^{\gamma\tau}$, confirming $B' = -4\gamma^2 e^{\gamma\tau}/D^2$. The ODE is satisfied.

---

**Exercise 3.** Show that the yield $y(t, T) = -\frac{A(\tau)}{\tau} - \frac{B(\tau)}{\tau}x$ for the CIR model converges to a finite limit as $\tau \to \infty$. Compute this long-run yield $y_\infty$ in terms of $\kappa$, $\theta$, $\xi$, and $\gamma$.

??? success "Solution to Exercise 3"
    The yield is $y(t, T) = -\frac{A(\tau)}{\tau} - \frac{B(\tau)}{\tau}x$. We need the limits of $B(\tau)/\tau$ and $A(\tau)/\tau$ as $\tau \to \infty$.

    **Limit of $B(\tau)/\tau$:** Since $B(\tau) = \frac{-2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}$, for large $\tau$ the $e^{\gamma\tau}$ terms dominate:

    $$
    B(\tau) \to \frac{-2e^{\gamma\tau}}{(\gamma + \kappa)e^{\gamma\tau}} = \frac{-2}{\gamma + \kappa}
    $$

    So $B(\tau)/\tau \to 0$ as $\tau \to \infty$, and $B(\tau)$ converges to the finite limit $B_\infty = \frac{-2}{\gamma + \kappa}$.

    **Limit of $A(\tau)/\tau$:** From $A' = \kappa\theta B + \frac{1}{2} \cdot 0 \cdot B^2 = \kappa\theta B$ (since $\sigma_0 = 0$ in CIR), we have by L'Hopital's rule

    $$
    \lim_{\tau \to \infty}\frac{A(\tau)}{\tau} = \lim_{\tau \to \infty} A'(\tau) = \kappa\theta B_\infty = \frac{-2\kappa\theta}{\gamma + \kappa}
    $$

    Therefore the long-run yield is

    $$
    y_\infty = \lim_{\tau \to \infty} y(t, T) = -\lim_{\tau\to\infty}\frac{A(\tau)}{\tau} = \frac{2\kappa\theta}{\gamma + \kappa}
    $$

    This is finite and independent of $x$ (the current short rate). It depends only on the long-run mean $\theta$, the speed of mean reversion $\kappa$, the volatility $\xi$ (through $\gamma = \sqrt{\kappa^2 + 2\xi^2}$), and represents the yield on an infinitely long zero-coupon bond.

---

**Exercise 4.** Verify that the instantaneous forward rate $f(t, T) = -A'(\tau) - B'(\tau)x$ recovers the short rate at $\tau = 0$: $f(t, t) = -A'(0) - B'(0)x = \rho_0 + \rho_1 x = r(x)$.

??? success "Solution to Exercise 4"
    At $\tau = 0$, the bond matures and pays $\$1$, so $P(t, t) = 1$, $A(0) = 0$, and $B(0) = 0$. We need to verify $f(t, t) = -A'(0) - B'(0)x = r(x)$.

    From the Riccati system:

    $$
    A'(0) = F(B(0)) - \rho_0 = F(0) - \rho_0
    $$

    Since $F(0) = \langle b_0, 0 \rangle + \frac{1}{2}\langle 0, a_0 \cdot 0 \rangle = 0$, we get $A'(0) = -\rho_0$.

    $$
    B_j'(0) = R_j(B(0)) - \rho_{1,j} = R_j(0) - \rho_{1,j}
    $$

    Since $R_j(0) = \langle b_j, 0 \rangle + \frac{1}{2}\langle 0, a_j \cdot 0 \rangle = 0$, we get $B_j'(0) = -\rho_{1,j}$.

    Therefore

    $$
    f(t, t) = -A'(0) - \langle B'(0), x \rangle = \rho_0 + \langle \rho_1, x \rangle = r(x)
    $$

    This confirms that the instantaneous forward rate at $\tau = 0$ equals the current short rate, which is the fundamental consistency condition for the term structure.

---

**Exercise 5.** Consider a two-factor model where $r_t = X_t^{(1)} + X_t^{(2)}$ with independent Vasicek factors. Write down the extended Riccati system for the bond price $P(t, T) = e^{A(\tau) + B_1(\tau)x_1 + B_2(\tau)x_2}$ and show that $B_1$ and $B_2$ satisfy independent linear ODEs. Derive the two-factor bond price formula.

??? success "Solution to Exercise 5"
    With $r_t = X_t^{(1)} + X_t^{(2)}$, we have $\rho_0 = 0$ and $\rho_1 = (1, 1)^T$. Each factor follows an independent Vasicek process: $dX_t^{(i)} = \kappa_i(\theta_i - X_t^{(i)})\,dt + \sigma_i\,dW_t^{(i)}$ for $i = 1, 2$.

    The affine parameters for each factor are $b_{0,i} = \kappa_i\theta_i$, $b_{i,i} = -\kappa_i$ (with $b_{i,j} = 0$ for $i \neq j$), $a_{0,ii} = \sigma_i^2$, $a_{j,ik} = 0$ for all $j$. Setting $u = 0$ for bond pricing:

    $$
    B_i'(\tau) = -\kappa_i B_i - 1, \qquad B_i(0) = 0, \quad i = 1, 2
    $$

    $$
    A'(\tau) = \kappa_1\theta_1 B_1 + \kappa_2\theta_2 B_2 + \tfrac{1}{2}\sigma_1^2 B_1^2 + \tfrac{1}{2}\sigma_2^2 B_2^2, \qquad A(0) = 0
    $$

    Since the $B_i$-equations are decoupled, each is an independent linear ODE with solution

    $$
    B_i(\tau) = -\frac{1 - e^{-\kappa_i\tau}}{\kappa_i}, \quad i = 1, 2
    $$

    The $A$-equation is then integrated directly:

    $$
    A(\tau) = \sum_{i=1}^{2}\left[\kappa_i\theta_i\int_0^\tau B_i(s)\,ds + \frac{\sigma_i^2}{2}\int_0^\tau B_i(s)^2\,ds\right]
    $$

    Each integral is the same as in the one-factor Vasicek case. Writing $A_i(\tau)$ for the one-factor $A$-function of factor $i$, we get $A(\tau) = A_1(\tau) + A_2(\tau)$. The two-factor bond price is

    $$
    P(t, T) = e^{A_1(\tau) + A_2(\tau) + B_1(\tau)x_1 + B_2(\tau)x_2}
    $$

    which is the product of two independent Vasicek bond prices: $P = P_1(t, T) \cdot P_2(t, T)$. This factorization is a direct consequence of the independence of the two factors.

---

**Exercise 6.** For the discounted characteristic function ($u = iv \neq 0$), the extended Riccati system must be solved with complex initial data $\tilde{\psi}(0) = iv$. Taking the CIR model, write down the discriminant for the $\tilde{\psi}$-equation with discounting and compare it to the discriminant $\gamma = \sqrt{\kappa^2 - 2\xi^2 iv}$ from the undiscounted case. How does the discounting term $\rho_1 = 1$ modify the discriminant?

??? success "Solution to Exercise 6"
    For the CIR model with discounting ($\rho_1 = 1$), the $\tilde{\psi}$-equation is

    $$
    \tilde{\psi}' = -\kappa\tilde{\psi} + \frac{\xi^2}{2}\tilde{\psi}^2 - 1
    $$

    This is a Riccati equation $\tilde{\psi}' = \alpha + \beta\tilde{\psi} + \frac{1}{2}\gamma\tilde{\psi}^2$ with $\alpha = -1$, $\beta = -\kappa$, $\gamma = \xi^2$. The discriminant of this equation is

    $$
    \tilde{\gamma}^2 = \beta^2 - 2\alpha\gamma = \kappa^2 + 2\xi^2
    $$

    so $\tilde{\gamma} = \sqrt{\kappa^2 + 2\xi^2}$.

    For the **undiscounted** characteristic function (no killing, $\rho_1 = 0$) with initial condition $\tilde{\psi}(0) = iv$, the $\tilde{\psi}$-equation is

    $$
    \tilde{\psi}' = -\kappa\tilde{\psi} + \frac{\xi^2}{2}\tilde{\psi}^2
    $$

    with $\alpha = 0$, giving discriminant $\gamma_{\text{undiscounted}}^2 = \kappa^2$, and the characteristic function involves $\gamma_{\text{undiscounted}} = \kappa$. However, if we look at the combined equation for bond pricing plus characteristic function (with $\tilde{\psi}(0) = iv$ and $\rho_1 = 1$), the full discriminant is

    $$
    \tilde{\gamma}(v) = \sqrt{\kappa^2 + 2\xi^2 - 2\xi^2 iv + 2\xi^2} = \sqrt{(\kappa^2 + 2\xi^2) - 2\xi^2 iv}
    $$

    Comparing with the undiscounted case where the discriminant would be $\gamma(v) = \sqrt{\kappa^2 - 2\xi^2 iv}$, the discounting adds $+2\xi^2$ inside the square root. This shifts the real part of the discriminant upward, which improves the numerical stability of the Riccati solution for complex arguments and ensures that the bond-pricing component ($v = 0$) gives $\tilde{\gamma}(0) = \sqrt{\kappa^2 + 2\xi^2}$, matching the standard CIR bond discriminant.
