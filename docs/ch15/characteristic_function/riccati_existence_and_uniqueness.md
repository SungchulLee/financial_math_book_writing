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
    Variance-process moment explosion bounds $\mathbb{E}[S_T^p] < \infty$ to $p \in [p_-, p_+]$, with implications for the Lee moment formula. Recall (see [Heston CF](../../ch16/heston_cf/heston_sde_and_affine_recap.md)).

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

---

## Exercises

**Exercise 1.** For the scalar Riccati equation $\psi' = -\kappa\psi + \frac{\xi^2}{2}\psi^2$ with $\kappa = 3$ and $\xi = 1$, compute the critical threshold $u^* = 2\kappa/\xi^2$. For the initial condition $u = 7 > u^*$, compute the explosion time $T^*(7)$ using the closed-form formula. Verify your answer by numerically integrating the ODE and observing when the solution diverges.

??? success "Solution to Exercise 1"
    The critical threshold is $u^* = 2\kappa/\xi^2 = 2 \cdot 3 / 1 = 6$. Since $u = 7 > 6 = u^*$, the solution explodes in finite time.

    The Riccati equation $\psi' = -3\psi + \frac{1}{2}\psi^2$ can be written as $\psi' = \frac{1}{2}\psi(\psi - 6)$. For $\psi > 6$, both factors are positive, so $\psi' > 0$ and the solution grows. The discriminant for the closed-form solution is

    $$
    \gamma = \sqrt{\kappa^2 + 2\xi^2 u} = \sqrt{9 + 2 \cdot 1 \cdot 7} = \sqrt{23} \approx 4.796
    $$

    (using the bond-pricing discriminant convention where $u$ enters with a positive sign due to the explosion analysis). The explosion time is determined by when the denominator in the closed-form solution vanishes. Using the standard formula for the CIR Riccati:

    $$
    \psi(\tau) = \frac{2\gamma u\,e^{\gamma\tau}}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma - u\xi^2(e^{\gamma\tau}-1)}
    $$

    The denominator vanishes when $[(\gamma + \kappa) - u\xi^2](e^{\gamma\tau} - 1) + 2\gamma = 0$, i.e.,

    $$
    e^{\gamma\tau} - 1 = \frac{2\gamma}{u\xi^2 - \gamma - \kappa} = \frac{2\sqrt{23}}{7 - \sqrt{23} - 3}
    $$

    With $\sqrt{23} \approx 4.796$: the denominator is $7 - 4.796 - 3 = -0.796$, so

    $$
    e^{\gamma T^*} - 1 = \frac{2(4.796)}{-0.796} \approx -12.05
    $$

    Since this gives a negative value, we re-examine: $e^{\gamma T^*} = 1 - 12.05 < 0$, which is impossible for real $T^*$. This indicates that for the CIR Riccati with negative $\beta = -\kappa$ and initial data above $u^*$, the explosion formula requires the alternative branch. By separation of variables:

    $$
    T^* = \int_7^\infty \frac{d\psi}{\frac{1}{2}\psi(\psi - 6)} = 2\int_7^\infty \frac{d\psi}{\psi(\psi-6)}
    $$

    Using partial fractions $\frac{1}{\psi(\psi-6)} = \frac{1}{6}\!\left(\frac{1}{\psi-6} - \frac{1}{\psi}\right)$:

    $$
    T^* = \frac{1}{3}\!\left[\log(\psi - 6) - \log\psi\right]_7^\infty = \frac{1}{3}\!\left[\log\frac{\psi - 6}{\psi}\right]_7^\infty = \frac{1}{3}\!\left(\log 1 - \log\frac{1}{7}\right) = \frac{\log 7}{3} \approx 0.6486
    $$

    Numerical integration of the ODE (e.g., via RK4) confirms that $\psi(\tau)$ diverges near $\tau \approx 0.649$.

---

**Exercise 2.** Prove that for the simple ODE $y' = y^2$ with initial condition $y(0) = c > 0$, the solution is $y(t) = c/(1 - ct)$ and the explosion time is $T^* = 1/c$. Use this as a comparison function: if $\psi' \leq \psi^2$ for $\psi > 0$, show that $\psi(\tau) \leq u/(1 - u\tau)$ and deduce that $T^*(\psi) \geq 1/u$.

??? success "Solution to Exercise 2"
    **Part 1:** For $y' = y^2$ with $y(0) = c > 0$, separate variables:

    $$
    \frac{dy}{y^2} = dt \implies -\frac{1}{y} = t + C
    $$

    From $y(0) = c$: $C = -1/c$, so $-1/y = t - 1/c$, giving

    $$
    y(t) = \frac{c}{1 - ct}
    $$

    This blows up when $1 - ct = 0$, i.e., $T^* = 1/c$.

    **Part 2 (Comparison):** Suppose $\psi' \leq \psi^2$ for $\psi > 0$ with $\psi(0) = u > 0$. Let $y(t) = u/(1-ut)$ be the solution of $y' = y^2$ with $y(0) = u$. By the comparison theorem for scalar ODEs (if $f(\psi) \leq g(\psi)$ and $\psi(0) = y(0)$, then $\psi(t) \leq y(t)$), we have

    $$
    \psi(\tau) \leq \frac{u}{1 - u\tau}
    $$

    for all $\tau$ in the common domain of existence. Since $y(\tau)$ blows up at $T^*_y = 1/u$, and $\psi(\tau) \leq y(\tau)$, the solution $\psi$ cannot blow up before $y$ does. Therefore $T^*(\psi) \geq T^*_y = 1/u$.

    This provides a useful lower bound on the explosion time: no matter how complicated the Riccati equation, if its right-hand side is bounded above by $\psi^2$, the explosion time is at least $1/u$.

---

**Exercise 3.** For the CIR process with $\kappa = 2$, $\xi^2 = 1$, show that the equilibrium $\psi^* = 2\kappa/\xi^2 = 4$ of the Riccati equation $\psi' = -2\psi + \frac{1}{2}\psi^2$ is stable from below but unstable from above. Sketch the phase portrait of $\psi' = R(\psi)$ for $\psi \in (-\infty, \infty)$ and identify all equilibria.

??? success "Solution to Exercise 3"
    The Riccati equation is $\psi' = R(\psi) = -2\psi + \frac{1}{2}\psi^2 = \frac{1}{2}\psi(\psi - 4)$.

    **Equilibria:** $R(\psi) = 0$ when $\psi = 0$ or $\psi = 4$.

    **Phase portrait analysis:**

    - For $\psi < 0$: $\psi < 0$ and $\psi - 4 < 0$, so $R(\psi) = \frac{1}{2}\psi(\psi-4) > 0$. The solution increases toward $0$.
    - For $0 < \psi < 4$: $\psi > 0$ and $\psi - 4 < 0$, so $R(\psi) < 0$. The solution decreases toward $0$.
    - For $\psi = 4$: $R(4) = 0$. This is an equilibrium.
    - For $\psi > 4$: $\psi > 0$ and $\psi - 4 > 0$, so $R(\psi) > 0$. The solution increases toward $+\infty$.

    **Stability of $\psi^* = 4$:** Compute $R'(\psi) = -2 + \psi$, so $R'(4) = 2 > 0$. Since the derivative is positive, $\psi^* = 4$ is an **unstable** equilibrium. However, solutions approaching from below ($0 < \psi < 4$) initially decrease (moving away from 4), while solutions starting just below 4 are pushed toward 0 by the negative $R(\psi)$. More precisely:

    - From below ($\psi \uparrow 4$): solutions starting with $0 < u < 4$ satisfy $R(u) < 0$, so $\psi$ decreases; these solutions never reach $\psi^* = 4$. The statement that $\psi^* = 4$ is "stable from below" means that solutions with $u$ just below 4 remain bounded (they decrease toward 0), so there is no explosion.
    - From above ($\psi > 4$): $R(\psi) > 0$, so the solution increases without bound. It escapes to $+\infty$ in finite time---this is the explosion phenomenon.

    The equilibrium $\psi^* = 0$ satisfies $R'(0) = -2 < 0$, making it locally stable. Solutions with $-\infty < \psi < 4$ are attracted toward $0$ (those with $\psi < 0$ increase toward it, those with $0 < \psi < 4$ decrease toward it).

---

**Exercise 4.** Using Filipovic's regularity results, explain why the admissible set $\mathcal{U}(\tau)$ shrinks as $\tau$ increases. For the CIR model, describe how $\mathcal{U}(\tau) \cap \mathbb{R}$ changes: what is the maximal real $u$ for which the Riccati solution exists up to time $\tau$?

??? success "Solution to Exercise 4"
    The admissible set $\mathcal{U}(\tau) = \{u \in \mathbb{C}^d : T^*(u) > \tau\}$ shrinks as $\tau$ increases because a larger $\tau$ requires the Riccati solution to exist for a longer time interval. If the solution explodes at $T^*(u)$, then $u \in \mathcal{U}(\tau)$ only for $\tau < T^*(u)$. As $\tau$ grows, more initial values $u$ are excluded.

    For the CIR model with $\beta = -\kappa$ and $\gamma = \xi^2$, the critical threshold for global existence is $u^* = 2\kappa/\xi^2$. For real $u$:

    - If $u \leq u^*$: $T^*(u) = \infty$, so $u \in \mathcal{U}(\tau)$ for all $\tau$
    - If $u > u^*$: $T^*(u) < \infty$, and $T^*(u)$ decreases as $u$ increases (larger initial data explodes sooner)

    Therefore $\mathcal{U}(\tau) \cap \mathbb{R} = (-\infty, u_{\max}(\tau)]$ where $u_{\max}(\tau)$ is defined by $T^*(u_{\max}(\tau)) = \tau$. Explicitly, $u_{\max}(\tau) = u^*$ for all $\tau$ from the left side (the boundary is always $u^*$ for the half-line $(-\infty, u^*]$), but from the right, the maximal $u$ for which the solution survives to time $\tau$ satisfies

    $$
    u_{\max}(\tau) \to u^* \text{ as } \tau \to \infty
    $$

    For finite $\tau$, $u_{\max}(\tau) > u^*$ (we can tolerate initial data slightly above the equilibrium if we do not need the solution to exist forever), but $u_{\max}(\tau) \downarrow u^*$ monotonically as $\tau \to \infty$.

---

**Exercise 5.** Explain why the characteristic function (with $u = iv$, $v$ real) is guaranteed to have a global Riccati solution, while the moment generating function (with $u$ real and positive) may not. Provide both the probabilistic argument (boundedness of $|\mathbb{E}[e^{ivX}]|$) and the ODE argument (the imaginary initial condition prevents the quadratic term from driving the real part to infinity).

??? success "Solution to Exercise 5"
    **Probabilistic argument:** For $u = iv$ with $v \in \mathbb{R}$, the Riccati solution computes $\phi(\tau, iv)$ and $\psi(\tau, iv)$ such that $e^{\phi + \psi x} = \mathbb{E}[e^{ivX_T} \mid X_t = x]$. Since $|e^{ivX_T}| = 1$ almost surely, we have $|e^{\phi + \psi x}| \leq 1$ for all $x \in D$ and all $\tau \geq 0$. Boundedness precludes explosion, so $T^*(iv) = \infty$.

    For real $u > 0$, the Riccati solution computes $\mathbb{E}[e^{uX_T} \mid X_t = x]$. The random variable $e^{uX_T}$ is unbounded, and its expectation may be infinite for large $T$. When the expectation diverges, the Riccati solution must blow up---the two phenomena are equivalent.

    **ODE argument:** Write $\psi(\tau) = a(\tau) + ib(\tau)$ with $\psi(0) = iv$, so $a(0) = 0$ and $b(0) = v$. The Riccati equation $\psi' = \beta\psi + \frac{\gamma}{2}\psi^2$ with $\beta < 0$ and $\gamma > 0$ gives

    $$
    a' = \beta a + \frac{\gamma}{2}(a^2 - b^2), \qquad b' = \beta b + \gamma ab
    $$

    At $\tau = 0$: $a'(0) = -\frac{\gamma}{2}v^2 < 0$, so the real part initially decreases (becomes negative). A negative real part in $\psi$ keeps $|e^{\psi x}|$ bounded for $x \geq 0$. The quadratic term $\frac{\gamma}{2}\psi^2 = \frac{\gamma}{2}(a^2 - b^2 + 2iab)$ has real part $\frac{\gamma}{2}(a^2 - b^2)$, which can be negative when $|b| > |a|$---precisely the situation for purely imaginary initial data. This negative feedback prevents the real part from growing unboundedly, ensuring global existence.

    For real $u > 0$, $b(0) = 0$ and $a(0) = u > 0$. The real part of the quadratic term is $\frac{\gamma}{2}a^2 > 0$, providing positive feedback that can drive $a(\tau) \to \infty$ in finite time when $u$ is large enough to overcome the stabilizing $\beta a$ term.

---

**Exercise 6.** For the Heston model, the critical moment $p^+$ satisfies $\mathbb{E}[S_T^{p^+}] = \infty$. Without deriving the exact formula, explain qualitatively how $p^+$ depends on each of the parameters $\kappa$ (mean reversion speed), $\xi$ (vol-of-vol), and $\rho$ (correlation). Which parameter changes would increase $p^+$ and thus reduce the risk of moment explosion?

??? success "Solution to Exercise 6"
    The critical moment $p^+$ is the supremum of $p > 1$ such that $\mathbb{E}[S_T^p] < \infty$. Qualitatively:

    **Dependence on $\kappa$ (mean reversion speed):** Increasing $\kappa$ strengthens mean reversion of the variance process, keeping $V_t$ closer to $\theta$ and reducing the probability of extreme variance excursions. This makes $S_T$ lighter-tailed, so $p^+$ increases. Stronger mean reversion mitigates moment explosion.

    **Dependence on $\xi$ (vol-of-vol):** Increasing $\xi$ makes the variance process more volatile, allowing it to reach higher values and creating heavier tails in $S_T$. This decreases $p^+$. In the extreme, as $\xi \to \infty$, $p^+ \to 1$ (only the first moment survives).

    **Dependence on $\rho$ (correlation):** Negative $\rho$ (leverage effect) creates negative skew: when $V_t$ increases, $S_t$ tends to decrease. For large positive moments $\mathbb{E}[S_T^p]$, we need $S_T$ to not have too heavy a right tail. Negative $\rho$ reduces the right tail thickness (and increases the left tail), so more negative $\rho$ generally increases $p^+$. Positive $\rho$ fattens the right tail and decreases $p^+$.

    **To increase $p^+$ (reduce explosion risk):** increase $\kappa$, decrease $\xi$, or make $\rho$ more negative. The Feller condition $2\kappa\theta > \xi^2$ is necessary for the variance to stay strictly positive but is not sufficient to prevent moment explosion---the critical moment $p^+$ depends on the full parameter set.

---

**Exercise 7.** Implement a numerical RK4 solver for the complex Riccati equation $\psi' = -\kappa\psi + \frac{\xi^2}{2}\psi^2$ with $\psi(0) = iv$, $\kappa = 2$, $\xi = 0.5$. Compute $\psi(\tau)$ for $\tau \in [0, 5]$ at $v = 1$ and $v = 10$, and plot $\operatorname{Re}(\psi(\tau))$ and $\operatorname{Im}(\psi(\tau))$. Verify that $|\psi(\tau)|$ remains bounded for all $\tau$.

??? success "Solution to Exercise 7"
    The RK4 method for $\psi' = f(\psi)$ where $f(\psi) = -\kappa\psi + \frac{\xi^2}{2}\psi^2$ proceeds as follows. With step size $h$ and $\psi_n \approx \psi(n h)$:

    $$
    k_1 = f(\psi_n), \quad k_2 = f(\psi_n + \tfrac{h}{2}k_1), \quad k_3 = f(\psi_n + \tfrac{h}{2}k_2), \quad k_4 = f(\psi_n + hk_3)
    $$

    $$
    \psi_{n+1} = \psi_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)
    $$

    All arithmetic is in $\mathbb{C}$. With $\kappa = 2$, $\xi = 0.5$, and $h = 0.01$:

    **For $v = 1$** ($\psi(0) = i$): The solution starts purely imaginary and acquires a negative real part. The imaginary part decays exponentially due to mean reversion ($\kappa = 2$ is strong). As $\tau \to \infty$, $\psi(\tau) \to 0$ (the equilibrium). The trajectory spirals toward the origin in the complex plane. $|\psi(\tau)| \leq 1$ for all $\tau$.

    **For $v = 10$** ($\psi(0) = 10i$): The initial imaginary part is larger, so the quadratic term $\frac{\xi^2}{2}\psi^2 = \frac{0.125}{1}(-100) = -12.5$ initially drives the real part strongly negative. The solution exhibits larger oscillations but still converges to $0$ as $\tau \to \infty$. $|\psi(\tau)|$ is bounded above by $|v| = 10$ and decays.

    In both cases, $|\psi(\tau)|$ remains bounded for all $\tau \in [0, 5]$, confirming the global existence theorem for purely imaginary initial data. The boundedness follows from the probabilistic argument: since $|e^{\psi x}| = e^{\operatorname{Re}(\psi)x}$ and $\operatorname{Re}(\psi) \leq 0$ for $x \geq 0$, the characteristic function stays bounded by 1, precluding explosion.
