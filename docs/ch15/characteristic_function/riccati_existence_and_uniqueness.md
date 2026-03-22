# Existence and Uniqueness of Riccati Solutions

The generalized Riccati ODE system $\psi' = R(\psi)$, $\phi' = F(\psi)$ is the computational engine of affine processes, but like any nonlinear ODE, it may fail to have a global solution. The quadratic nonlinearity in $R$ can cause solutions to blow up in finite time---a phenomenon with direct financial consequences for moment generating functions and long-maturity pricing. This section establishes local and global existence conditions, characterizes explosion times, and presents the key regularity results of Filipovic.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the Picard-Lindelof theorem for local existence and uniqueness of the Riccati system
    2. Identify when finite-time explosion occurs and compute the explosion time
    3. State sufficient conditions for global existence on $[0, \infty)$
    4. Apply Filipovic's regularity results to affine processes
    5. Distinguish between the characteristic function domain (always global) and the MGF domain (possibly finite)

---

## Intuition

A scalar Riccati equation $\psi' = \alpha + \beta\psi + \gamma\psi^2$ with $\gamma > 0$ behaves like a quadratic growth ODE. For large $\psi$, the $\gamma\psi^2$ term dominates, and the solution can grow without bound in finite time---just as the simple ODE $y' = y^2$ has the solution $y(t) = 1/(c - t)$ that blows up at $t = c$. Whether explosion actually occurs depends on the initial condition $\psi(0) = u$ and the balance between the stabilizing drift term $\beta\psi$ (which is mean-reverting when $\beta < 0$) and the destabilizing quadratic term.

For the characteristic function ($u = iv$, purely imaginary), the solution remains bounded for all time---this is guaranteed by the probabilistic interpretation (the characteristic function is bounded by 1). For the moment generating function ($u$ real and positive), explosion can occur, and the explosion time determines the maximal maturity for which the MGF exists.

---

## Local Existence and Uniqueness

### The Picard-Lindelof Theorem Applied

The functions $F$ and $R$ defining the Riccati system are locally Lipschitz on $\mathbb{C}^d$ (they are polynomial in $w$ for pure diffusion models, or smooth for jump-diffusion models with well-behaved Levy measures). The standard Picard-Lindelof theorem therefore guarantees:

**Theorem (Local Existence and Uniqueness).** For every $u$ in the admissible domain $\mathcal{U} \subseteq \mathbb{C}^d$, there exists a maximal time $T^*(u) \in (0, \infty]$ such that the Riccati system

$$
\psi'(\tau) = R(\psi(\tau)), \qquad \psi(0) = u
$$

$$
\phi'(\tau) = F(\psi(\tau)), \qquad \phi(0) = 0
$$

has a unique solution $(\phi, \psi) \in C^1([0, T^*(u)); \mathbb{C} \times \mathbb{C}^d)$.

If $T^*(u) < \infty$, then $\|\psi(\tau)\| \to \infty$ as $\tau \to T^*(u)^-$ (the solution explodes).

The maximal existence time $T^*(u)$ depends on the initial value $u$ and the model parameters. Note that the $\phi$-equation cannot cause explosion independently: since $\phi' = F(\psi)$ and $F$ is locally bounded, $\phi$ blows up if and only if $\psi$ does.

---

## Explosion Analysis for the Scalar Riccati Equation

### The Standard Scalar Case

Consider the scalar Riccati equation arising from a CIR-type component:

$$
\psi'(\tau) = \beta\psi(\tau) + \frac{1}{2}\gamma\psi(\tau)^2, \qquad \psi(0) = u
$$

where $\beta = \kappa_1$ (typically $\beta < 0$ for mean-reverting models) and $\gamma = \sigma_1 > 0$.

**Proposition (Explosion Time).** The maximal existence time for real initial data $u > 0$ is:

$$
T^*(u) = \begin{cases} +\infty & \text{if } u \leq -2\beta/\gamma = 2|\beta|/\gamma \text{ and } \beta < 0 \\ \displaystyle \frac{1}{\delta}\log\!\left(\frac{u\gamma + \beta + \delta}{u\gamma + \beta - \delta}\right) & \text{if } u > -2\beta/\gamma \text{ or } \beta \geq 0 \end{cases}
$$

where $\delta = \sqrt{\beta^2 + u\beta\gamma}$ when this expression applies.

*Proof sketch.* The Riccati equation $\psi' = \beta\psi + \frac{1}{2}\gamma\psi^2 = \frac{1}{2}\gamma\psi(\psi + 2\beta/\gamma)$ has equilibria at $\psi = 0$ and $\psi = -2\beta/\gamma$. For $\beta < 0$, the equilibrium $\psi^* = 2|\beta|/\gamma > 0$ is stable from below: if $0 < u < \psi^*$, the solution converges to $\psi^*$ as $\tau \to \infty$. If $u > \psi^*$, the quadratic term dominates and the solution escapes to $+\infty$ in finite time. The explosion time is computed by separation of variables:

$$
\int_u^{\psi(\tau)} \frac{d\psi}{\beta\psi + \frac{1}{2}\gamma\psi^2} = \tau
$$

Partial fractions and integration yield the formula above. $\square$

### Financial Interpretation

For the CIR process with $\beta = -\kappa$ and $\gamma = \xi^2$, the critical threshold is $u^* = 2\kappa/\xi^2$. This means:

- The moment generating function $\mathbb{E}[e^{u r_T}]$ exists for all $T > 0$ if and only if $u < u^*$
- At $u = u^*$, the MGF is finite for finite $T$ but diverges as $T \to \infty$
- For $u > u^*$, the MGF explodes at a finite time $T^*(u)$

This phenomenon, called **moment explosion**, constrains the use of moment methods for heavy-tailed applications of CIR-type models.

!!! warning "Moment Explosion in the Heston Model"
    In the Heston stochastic volatility model, moment explosion of the variance process $V_t$ translates into restrictions on the moments of the stock price. Specifically, $\mathbb{E}[S_T^p] < \infty$ only for $p$ in a bounded interval $[p_-, p_+]$ that depends on $\kappa$, $\xi$, $\rho$, and $T$. This has practical consequences for the Lee moment formula, which relates the slope of the implied volatility smile at extreme strikes to the maximal finite moment.

---

## Global Existence for the Characteristic Function

### Purely Imaginary Initial Data

When $u = iv$ for $v \in \mathbb{R}^d$, the Riccati system has a global solution on $[0, \infty)$.

**Theorem (Global Existence for the CF).** For every $v \in \mathbb{R}^d$, the Riccati system with initial condition $\psi(0) = iv$ has a unique global solution on $[0, \infty)$, and $|\exp(\phi(\tau, iv) + \langle \psi(\tau, iv), x \rangle)| \leq 1$ for all $\tau \geq 0$ and $x \in D$.

*Proof.* The characteristic function $\mathbb{E}[e^{i\langle v, X_T \rangle} \mid X_t = x]$ is bounded by 1 in absolute value for all $T \geq t$. Since $\exp(\phi(\tau, iv) + \langle \psi(\tau, iv), x \rangle)$ equals this characteristic function, it must remain bounded, which precludes explosion of $\psi$. Therefore $T^*(iv) = \infty$. $\square$

This probabilistic argument provides a global existence result without analyzing the ODE directly. The key insight is that the Riccati equation inherits global existence from the boundedness of the characteristic function.

---

## Filipovic's Regularity Results

### The DFS Framework

Duffie, Filipovic, and Schachermayer (2003) established a comprehensive regularity theory for affine processes. Their results connect the properties of the stochastic process to the analytic properties of the Riccati solutions.

**Theorem (Filipovic Regularity).** Let $X$ be a stochastically continuous affine process on $D = \mathbb{R}^m_+ \times \mathbb{R}^{d-m}$ with admissible parameters. Then:

1. **Analyticity**: The functions $\phi(\tau, u)$ and $\psi(\tau, u)$ are analytic in $u$ on the interior of the admissible set $\mathcal{U}$, for each fixed $\tau \geq 0$.

2. **Continuity in $\tau$**: The functions $\tau \mapsto \phi(\tau, u)$ and $\tau \mapsto \psi(\tau, u)$ are continuously differentiable on $[0, T^*(u))$.

3. **Maximal domain**: The admissible set $\mathcal{U}(\tau) = \{u \in \mathbb{C}^d : T^*(u) > \tau\}$ is open and convex, and contains $i\mathbb{R}^d$ for all $\tau$.

4. **Semiflow**: On the admissible domain, $\psi$ satisfies the semiflow property $\psi(t+s, u) = \psi(t, \psi(s, u))$.

### Implications for Numerical Methods

The analyticity of $\phi$ and $\psi$ in $u$ is essential for Fourier pricing methods. It guarantees that the characteristic function is smooth in the frequency variable $v$, which ensures rapid convergence of Fourier series and FFT-based methods.

The openness of $\mathcal{U}(\tau)$ means that if the Riccati solution exists at some $u_0$, it also exists in a neighborhood of $u_0$. This provides robustness for numerical integration along contours in the complex plane.

---

## Comparison Theorems

### Monotonicity

For real-valued initial data, comparison theorems provide useful bounds on the Riccati solution.

**Proposition (Comparison).** Let $\psi_1$ and $\psi_2$ be solutions of $\psi' = R(\psi)$ with real initial data $\psi_1(0) \leq \psi_2(0)$. If $R$ is locally Lipschitz and quasi-monotone increasing, then $\psi_1(\tau) \leq \psi_2(\tau)$ for all $\tau$ in the common domain of existence.

This is useful for bounding the explosion time: if we can find a simpler Riccati equation whose explosion time is known, comparison gives a bound on $T^*$ for the original equation.

??? example "Explosion Time for the CIR Riccati Equation"
    For the CIR process with $\kappa = 2$, $\xi = 1$, the critical threshold is $u^* = 2\kappa/\xi^2 = 4$. Consider initial values:

    - $u = 3 < u^* = 4$: The solution converges to $u^* = 4$ as $\tau \to \infty$. Global existence.
    - $u = 5 > u^* = 4$: The solution explodes. The explosion time is

    $$
    T^*(5) = \frac{1}{\delta}\log\!\left(\frac{5 \cdot 1 + (-2) + \delta}{5 \cdot 1 + (-2) - \delta}\right)
    $$

    where $\delta = \sqrt{4 + 5 \cdot (-2) \cdot 1} = \sqrt{-6}$, which requires complex analysis. In fact, for $u > u^*$, the denominator in the closed-form solution $\psi(\tau) = 2\kappa(e^{\delta\tau}-1)/[(\delta+\kappa)(e^{\delta\tau}-1)+2\delta]$ with $\delta = \sqrt{\kappa^2 + 2\xi^2 u}$ vanishes at $T^* = \frac{1}{\delta}\log(1 + 2\delta/(\delta + \kappa))$. For the numerical values, $\delta = \sqrt{4 + 10} = \sqrt{14} \approx 3.742$, giving $T^* \approx 0.504$. $\square$

---

## Numerical Considerations

When closed-form solutions are unavailable, the Riccati system must be solved numerically. Key considerations include:

1. **Runge-Kutta methods**: Standard fourth-order Runge-Kutta (RK4) is adequate for most applications. Adaptive step-size control is recommended near explosion.

2. **Complex arithmetic**: For the characteristic function, $\psi(\tau)$ is complex-valued. The numerical solver must handle complex arithmetic consistently.

3. **Branch cuts**: The closed-form CIR solution involves $\sqrt{\kappa^2 + 2\xi^2 iv}$ and $\log(\cdots)$, both of which have branch cuts. Numerical evaluation must use consistent branch choices---typically the principal square root with positive real part and the principal logarithm.

4. **Stiffness**: For large $|\kappa|$ (strong mean reversion), the Riccati system can be stiff, requiring implicit methods or small step sizes.

---

## Summary

Local existence and uniqueness of the Riccati system follow from the Picard-Lindelof theorem, since $F$ and $R$ are locally Lipschitz. For purely imaginary initial data $u = iv$ (the characteristic function case), the solution exists globally on $[0, \infty)$, as guaranteed by the boundedness of the characteristic function. For real initial data $u > 0$ (the moment generating function case), finite-time explosion can occur when $u$ exceeds a critical threshold determined by the balance between mean reversion and diffusion strength. The Filipovic regularity theory establishes analyticity in $u$, continuous differentiability in $\tau$, and convexity of the admissible domain---properties essential for Fourier-based pricing methods.

---

## Further Reading

- Filipovic, D. *Term-Structure Models: A Graduate Course*. Springer, 2009, Chapters 10-11.
- Duffie, D., Filipovic, D., & Schachermayer, W. (2003). "Affine Processes and Applications in Finance." *Annals of Applied Probability*, 13(3), 984-1053.
- Keller-Ressel, M. (2011). "Moment Explosions and Long-Term Behavior of Affine Stochastic Volatility Models." *Mathematical Finance*, 21(1), 73-98.
- Andersen, L. B. G. & Piterbarg, V. V. (2007). "Moment Explosions in Stochastic Volatility Models." *Finance and Stochastics*, 11(1), 29-50.
