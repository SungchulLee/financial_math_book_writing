# Applications of Dynkin's Formula

Dynkin's formula is a powerful tool for computing expectations involving stopping times. This page covers the main applications: exit times, hitting probabilities, and boundary value problems.

!!! warning "Dynkin is a Bridge, Not a Solver"
    Dynkin's formula **connects** probabilistic problems to PDEs. The actual work is done by PDE theory (existence, uniqueness, regularity) and boundary conditions (encoding the problem constraints). Dynkin tells us *why* the PDE solution equals the expected value — it does not magically produce solutions.

    **Scope**: All examples here involve **diffusion processes** (continuous paths, second-order generators). For jump processes, the corresponding equations become integro-differential.

---

## The General Strategy

To compute $\mathbb{E}_x[\cdot]$ involving a stopping time $\tau$:

| Want to find | Solve this PDE | Boundary conditions | Result |
|--------------|----------------|---------------------|--------|
| $\mathbb{E}_x[\tau]$ | $\mathcal{L}u = -1$ | $u = 0$ on $\partial D$ | $u(x) = \mathbb{E}_x[\tau]$ |
| $\mathbb{E}_x[g(X_\tau)]$ | $\mathcal{L}f = 0$ | $f = g$ on $\partial D$ | $f(x) = \mathbb{E}_x[g(X_\tau)]$ |

For discounted expectations $\mathbb{E}_x[e^{-\lambda\tau}]$, the corresponding equation $\mathcal{L}f = \lambda f$ is a Feynman–Kac problem, not Dynkin alone. See [Feynman–Kac Formula](../../ch05/feynman_kac/feynman_kac_formula.md).

!!! note "Fine Print"
    These correspondences hold when the PDE admits a sufficiently regular solution. In degenerate cases, viscosity or weak solutions may be required. Uniqueness of the PDE solution must be established independently; Dynkin identifies the probabilistic representation.

**Recipe**:

1. Identify what you want to compute
2. Set up the appropriate PDE with boundary conditions
3. Solve the PDE (this is where the real work happens)
4. Dynkin's formula justifies why the PDE solution equals the expectation

The justification in step 4 rests on: if $\mathcal{L}f = 0$, the integral in Dynkin's formula vanishes and $\mathbb{E}_x[f(X_\tau)] = f(x)$; if $\mathcal{L}f = -1$, the integral equals $-\mathbb{E}_x[\tau]$.

---

## Exit Times

### The PDE Approach

**Setup**: Diffusion $X_t$ in domain $D$, exit time $\tau = \inf\{t : X_t \notin D\}$.

**Goal**: Find $u(x) = \mathbb{E}_x[\tau]$.

**Derivation**: Apply Dynkin to $u$ itself. Since $u(X_\tau) = 0$ (expected remaining time at the boundary is zero):

$$0 = u(x) + \mathbb{E}_x\left[\int_0^\tau (\mathcal{L}u)(X_s)\,ds\right]$$

If $\mathcal{L}u = -1$ everywhere in $D$, this gives $0 = u(x) - \mathbb{E}_x[\tau]$.

**Result**: The expected exit time solves the **Poisson equation**:

$$\boxed{\mathcal{L}u = -1 \text{ in } D, \quad u = 0 \text{ on } \partial D}$$

---

### Brownian Motion on (a, b)

**Process**: $dX_t = dW_t$, generator $\mathcal{L} = \frac{1}{2}\frac{d^2}{dx^2}$

**PDE**: $\frac{1}{2}u'' = -1$ with $u(a) = u(b) = 0$

**Solve**: $u'' = -2 \implies u(x) = -x^2 + Cx + D$

Boundary conditions give $C = a + b$ and $D = -ab$, so:

$$\boxed{\mathbb{E}_x[\tau] = (x - a)(b - x)}$$

Recall (see [§ Expected Exit Time from (a, b)](dynkin_formula.md#expected-exit-time-from-a-b)): the same answer is reached directly from Dynkin's formula using exit probabilities and $\mathbb{E}_x[X_\tau^2]$. The two routes are equivalent — here we cast it as a PDE boundary value problem.

---

### Brownian Motion on (0, ∞): Hitting Zero

**Setup**: $X_0 = x > 0$, $\tau_0 = \inf\{t : X_t = 0\}$

**PDE**: $\frac{1}{2}u'' = -1$ on $(0, \infty)$ with $u(0) = 0$

General solution with $u(0) = 0$: $u(x) = -x^2 + Cx = x(C - x)$. Since $D = (0, \infty)$ is unbounded, we need $u(x) \geq 0$ for all $x > 0$. But for any fixed $C$, the expression $x(C - x)$ becomes negative for $x > C$. No choice of $C$ produces a nonnegative solution on all of $(0, \infty)$, so the growth conditions needed for Dynkin to apply cannot be satisfied.

**Conclusion**:

$$\boxed{\mathbb{E}_x[\tau_0] = \infty \text{ for BM on } (0, \infty)}$$

!!! info "Interpretation"
    BM started at $x > 0$ hits $0$ **almost surely** (1D BM is recurrent), but the **expected time is infinite**. The particle keeps wandering away before returning.

---

## Exit Probabilities

### Hitting b Before a (Brownian Motion)

**Setup**: $X_0 = x \in (a, b)$, find $p(x) = \mathbb{P}_x(X_\tau = b)$

By Dynkin with $\mathcal{L}p = 0$, we have $\mathbb{E}_x[p(X_\tau)] = p(x)$.

**PDE**: $\frac{1}{2}p'' = 0$ with $p(a) = 0$, $p(b) = 1$

**Solution**: $p'' = 0 \implies p(x) = Ax + B$. Boundary conditions give $A = \frac{1}{b-a}$, $B = -\frac{a}{b-a}$:

$$\boxed{\mathbb{P}_x(X_\tau = b) = \frac{x - a}{b - a}}$$

---

### Gambler's Ruin

A gambler starts with $\$x$. Each round: win $\$1$ (prob $\frac{1}{2}$) or lose $\$1$ (prob $\frac{1}{2}$). Game ends at $\$0$ (ruin) or $\$b$ (target). Taking the continuous limit (BM on $(0, b)$):

$$\mathbb{P}(\text{ruin}) = \frac{b - x}{b}, \qquad \mathbb{P}(\text{reach target}) = \frac{x}{b}$$

In the discrete setting, this follows from the optional stopping theorem applied to the martingale $X_n$; the continuous formula is the limiting case.

---

### Brownian Motion with Drift

**Process**: $dX_t = \mu\,dt + \sigma\,dW_t$, generator $\mathcal{L}f = \mu f' + \frac{\sigma^2}{2}f''$

**PDE**: $\mu p' + \frac{\sigma^2}{2}p'' = 0$ with $p(a) = 0$, $p(b) = 1$

**Characteristic equation**: $\frac{\sigma^2}{2}r^2 + \mu r = 0 \implies r(r + 2\mu/\sigma^2) = 0$, giving $r_1 = 0$ (constant term) and $r_2 = -2\mu/\sigma^2$ (exponential term).

**General solution**: $p(x) = A + B e^{-2\mu x/\sigma^2}$. Applying boundary conditions:

$$p(x) = \frac{e^{-2\mu x/\sigma^2} - e^{-2\mu a/\sigma^2}}{e^{-2\mu b/\sigma^2} - e^{-2\mu a/\sigma^2}}$$

!!! success "Limit Check"
    As $\mu \to 0$: by L'Hôpital, $p(x) \to \frac{x - a}{b - a}$ $\checkmark$

---

## Boundary Value Problems

!!! warning "Standing Assumptions"
    Throughout this section, $D$ is a **bounded** domain with **regular boundary** (smooth or Lipschitz), the diffusion is **non-explosive**, and the integrability conditions for Dynkin's formula hold.

### Dirichlet Problem

**Problem**: Given boundary data $g$, find $f$ such that $\mathcal{L}f = 0$ in $D$ and $f = g$ on $\partial D$.

**Probabilistic Solution** (Kakutani):

$$\boxed{f(x) = \mathbb{E}_x[g(X_\tau)]}$$

where $\tau = \inf\{t : X_t \notin D\}$.

??? note "Why This Works"

    By Dynkin with $\mathcal{L}f = 0$:

    $$f(x) = \mathbb{E}_x[f(X_\tau)] = \mathbb{E}_x[g(X_\tau)]$$

    since $f = g$ on $\partial D$ and $X_\tau \in \partial D$.

---

### Poisson Problem

**Problem**: Given source $h$, find $f$ such that $\mathcal{L}f = -h$ in $D$ and $f = 0$ on $\partial D$.

**Probabilistic Solution**:

$$\boxed{f(x) = \mathbb{E}_x\left[\int_0^\tau h(X_s)\,ds\right]}$$

??? note "Why This Works"

    By Dynkin:

    $$0 = \mathbb{E}_x[f(X_\tau)] = f(x) + \mathbb{E}_x\left[\int_0^\tau (\mathcal{L}f)(X_s)\,ds\right] = f(x) - \mathbb{E}_x\left[\int_0^\tau h(X_s)\,ds\right]$$

**Special case**: $h \equiv 1$ gives $f(x) = \mathbb{E}_x[\tau]$ (expected exit time).

---

## Laplace Transforms of Hitting Times

**Goal**: Compute $\mathbb{E}_x[e^{-\lambda\tau}]$ for $\lambda > 0$.

The functional $e^{-\lambda\tau}$ is multiplicative in $\tau$, so Dynkin's formula ($\mathcal{L}f = -1$ or $\mathcal{L}f = 0$) does not apply directly. Recall (see [§ Feynman–Kac Formula](../../ch05/feynman_kac/feynman_kac_formula.md)): $v(x) = \mathbb{E}_x[e^{-\lambda\tau}]$ satisfies the eigenvalue equation $\mathcal{L}v = \lambda v$, with $v = 1$ on the target boundary.

### BM Hitting Time of Level a

Let $\tau_a = \inf\{t : X_t = a\}$ for BM starting at $x > a$.

**ODE** (Feynman–Kac eigenvalue equation with $\mathcal{L} = \frac{1}{2}\partial_{xx}$): $\frac{1}{2}v'' = \lambda v$, with $v(a) = 1$ and $v(x) \to 0$ as $x \to \infty$.

**Solve**: Characteristic equation $\frac{1}{2}r^2 = \lambda \implies r = \pm\sqrt{2\lambda}$. Boundary condition $v(\infty) = 0$ forces the coefficient of $e^{\sqrt{2\lambda}x}$ to zero; $v(a) = 1$ then gives:

$$\boxed{\mathbb{E}_x[e^{-\lambda\tau_a}] = e^{-\sqrt{2\lambda}(x - a)}}$$

!!! success "Sanity Checks"

    - $x = a$: result is $1$ $\checkmark$ (already there)
    - $x \to \infty$: result $\to 0$ $\checkmark$ (takes forever)
    - $\lambda \to 0$: result $\to 1$ $\checkmark$ (no discounting; BM hits every level a.s.)

---

## Summary

| Application | PDE | Boundary Conditions | Probabilistic Meaning |
|-------------|-----|---------------------|----------------------|
| Expected exit time | $\mathcal{L}u = -1$ | $u = 0$ on $\partial D$ | $u(x) = \mathbb{E}_x[\tau]$ |
| Exit probability | $\mathcal{L}p = 0$ | $p = g$ on $\partial D$ | $p(x) = \mathbb{E}_x[g(X_\tau)]$ |
| Laplace transform of $\tau$ | $\mathcal{L}v = \lambda v$ (Feynman–Kac) | $v = 1$ on target | $v(x) = \mathbb{E}_x[e^{-\lambda\tau}]$ |

**The Dynkin–PDE correspondence**:

$$
\text{Probabilistic problem}
\;\stackrel{\text{Dynkin}}{\longleftrightarrow}\;
\text{PDE boundary value problem}
$$

!!! abstract "Key Takeaway"
    Dynkin's formula **justifies** why PDE solutions equal probabilistic expectations. The PDE machinery (existence, uniqueness, regularity) does the heavy lifting. Dynkin is the **bridge** connecting the two worlds.

---

## See Also

- [Dynkin's Formula](dynkin_formula.md) — the core formula and direct derivation
- [Generator and Martingales](generator_and_martingales.md) — martingale characterization
- [Feynman–Kac Formula](../../ch05/feynman_kac/feynman_kac_formula.md) — discounted expectations, killing
- [Kolmogorov Backward Equation](../../ch05/kolmogorov_equations/kolmogorov_backward.md) — PDE for transition probabilities

---

## Exercises

**Exercise 1.** Let $dX_t = \mu\,dt + \sigma\,dW_t$ (Brownian motion with constant drift $\mu$ and volatility $\sigma$) on the interval $(a, b)$. Set up and solve the Poisson equation $\mathcal{L}u = -1$ with $u(a) = u(b) = 0$ to find the expected exit time $\mathbb{E}_x[\tau]$. Verify that your answer reduces to $(x - a)(b - x)$ when $\mu = 0$ and $\sigma = 1$.

??? success "Solution to Exercise 1"
    The generator for BM with drift is $\mathcal{L}f = \mu f' + \frac{\sigma^2}{2}f''$. The Poisson equation is:

    $$
    \mu u' + \frac{\sigma^2}{2}u'' = -1, \qquad u(a) = 0, \quad u(b) = 0
    $$

    **Solve the homogeneous equation** $\mu u' + \frac{\sigma^2}{2}u'' = 0$: the characteristic equation $\frac{\sigma^2}{2}r^2 + \mu r = 0$ gives $r = 0$ and $r = -2\mu/\sigma^2$. So the homogeneous solution is $u_h = A + B e^{-2\mu x/\sigma^2}$.

    **Particular solution**: Try $u_p = Cx$. Then $u_p' = C$, $u_p'' = 0$, so $\mu C = -1$, giving $C = -1/\mu$ (assuming $\mu \neq 0$). So $u_p = -x/\mu$.

    **General solution**: $u(x) = A + B e^{-2\mu x/\sigma^2} - x/\mu$.

    **Apply boundary conditions**:

    - $u(a) = 0$: $A + B e^{-2\mu a/\sigma^2} - a/\mu = 0$
    - $u(b) = 0$: $A + B e^{-2\mu b/\sigma^2} - b/\mu = 0$

    Subtracting: $B(e^{-2\mu a/\sigma^2} - e^{-2\mu b/\sigma^2}) = (b-a)/\mu$, so:

    $$
    B = \frac{b - a}{\mu(e^{-2\mu a/\sigma^2} - e^{-2\mu b/\sigma^2})}
    $$

    and $A = a/\mu - B e^{-2\mu a/\sigma^2}$.

    The expected exit time is:

    $$
    \mathbb{E}_x[\tau] = \frac{b - x}{\mu} - \frac{b - a}{\mu}\cdot\frac{e^{-2\mu x/\sigma^2} - e^{-2\mu b/\sigma^2}}{e^{-2\mu a/\sigma^2} - e^{-2\mu b/\sigma^2}}
    $$

    **Verification** ($\mu = 0$, $\sigma = 1$): As $\mu \to 0$, set $\gamma = 2\mu/\sigma^2 \to 0$. Using $e^{-\gamma x} \approx 1 - \gamma x + \gamma^2 x^2/2$:

    $$
    \frac{e^{-\gamma x} - e^{-\gamma b}}{e^{-\gamma a} - e^{-\gamma b}} \approx \frac{\gamma(b - x)}{\gamma(b - a)} = \frac{b - x}{b - a}
    $$

    and $\frac{b-x}{\mu} - \frac{b-a}{\mu}\cdot\frac{b-x}{b-a} = \frac{b-x}{\mu} - \frac{b-x}{\mu} = 0$. This is $0/0$, so we need a more careful expansion. Expanding to second order and using L'Hopital's rule in $\mu$, one recovers $(x-a)(b-x)$, matching the driftless BM result.

---

**Exercise 2.** For the Ornstein--Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ on the interval $(-a, a)$ with $a > 0$, write down the Poisson equation $\mathcal{L}u = -1$ with $u(-a) = u(a) = 0$ for the expected exit time. You do not need to solve the ODE explicitly, but:

(a) Explain why $u(x)$ must be an even function of $x$ (use the symmetry of the problem).

(b) Show that $u(0) > u(x)$ for all $x \neq 0$ in $(-a, a)$, i.e., the expected exit time is maximized at the origin.

??? success "Solution to Exercise 2"
    The OU generator is $\mathcal{L}f = -\kappa x\,f' + \frac{\sigma^2}{2}f''$. The Poisson equation is:

    $$
    -\kappa x\,u'(x) + \frac{\sigma^2}{2}u''(x) = -1, \qquad u(-a) = u(a) = 0
    $$

    **(a)** The OU process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ has a symmetric law: if $X_0 = -x_0$, then $-X_t$ has the same law as $X_t$ starting from $x_0$ (since $d(-X_t) = -\kappa(-X_t)\,dt + \sigma\,d(-W_t)$ and $-W_t$ is also a standard BM). The domain $(-a, a)$ is symmetric about the origin. Therefore, by the symmetry of the process and domain, $u(x) = \mathbb{E}_x[\tau]$ must satisfy $u(-x) = u(x)$, i.e., $u$ is an even function.

    This can also be verified from the ODE: if $u(x)$ is a solution, then $\tilde{u}(x) := u(-x)$ satisfies $-\kappa(-x)\tilde{u}'(-x)\cdot(-1) + \frac{\sigma^2}{2}\tilde{u}''(-x) = -\kappa x\,u'(-x)(-1)(-1) + \frac{\sigma^2}{2}u''(-x) = -\kappa x u'(-x) + \frac{\sigma^2}{2}u''(-x) = -1$ (evaluating the ODE at $-x$). So $\tilde{u}$ also solves the same ODE with the same boundary conditions, and by uniqueness $u(x) = u(-x)$.

    **(b)** Since $u$ is even and satisfies $u(-a) = u(a) = 0$ with $u \geq 0$ on $(-a,a)$, we show $u(0) \geq u(x)$ for all $x \in (-a,a)$. The maximum of $u$ occurs at some interior point $x^*$. At $x^*$, $u'(x^*) = 0$ and $u''(x^*) \leq 0$, so from the ODE:

    $$
    -\kappa x^* \cdot 0 + \frac{\sigma^2}{2}u''(x^*) = -1 \implies u''(x^*) = -\frac{2}{\sigma^2} < 0
    $$

    This is consistent. Since $u$ is even, $u'(0) = 0$, and from the ODE at $x = 0$: $u''(0) = -2/\sigma^2 < 0$, so $x = 0$ is a local maximum. Since $u$ is even and smooth with $u(0) > 0 = u(\pm a)$, and the ODE has a unique solution, $x = 0$ must be the global maximum on $(-a, a)$. Therefore $u(0) > u(x)$ for all $x \neq 0$ in $(-a, a)$.

---

**Exercise 3.** A stock price follows $dS_t = rS_t\,dt + \sigma S_t\,dW_t$ under the risk-neutral measure. A trader enters a position at price $S_0 = s$ and will exit when $S_t$ first hits either $L$ (stop-loss) or $U$ (take-profit), where $0 < L < s < U$. Using the exit probability formula for BM with drift, compute the probability $\mathbb{P}_s(S_\tau = U)$ that the trader hits the take-profit level before the stop-loss. (Hint: apply the change of variable $Y_t = \ln S_t$ to reduce to BM with drift on $(\ln L, \ln U)$.)

??? success "Solution to Exercise 3"
    Apply the change of variable $Y_t = \ln S_t$. By Ito's lemma:

    $$
    dY_t = \left(r - \frac{\sigma^2}{2}\right)dt + \sigma\,dW_t
    $$

    So $Y_t$ is BM with drift $\mu_Y = r - \sigma^2/2$ and volatility $\sigma_Y = \sigma$ on the interval $(\ln L, \ln U)$, starting at $y = \ln s$.

    The exit probability formula for BM with drift on $(a_Y, b_Y) = (\ln L, \ln U)$ is:

    $$
    \mathbb{P}_y(Y_\tau = b_Y) = \frac{e^{-2\mu_Y y/\sigma_Y^2} - e^{-2\mu_Y a_Y/\sigma_Y^2}}{e^{-2\mu_Y b_Y/\sigma_Y^2} - e^{-2\mu_Y a_Y/\sigma_Y^2}}
    $$

    Setting $\gamma = 2\mu_Y/\sigma_Y^2 = 2(r - \sigma^2/2)/\sigma^2 = 2r/\sigma^2 - 1$:

    $$
    \mathbb{P}_s(S_\tau = U) = \frac{e^{-\gamma \ln s} - e^{-\gamma \ln L}}{e^{-\gamma \ln U} - e^{-\gamma \ln L}} = \frac{s^{-\gamma} - L^{-\gamma}}{U^{-\gamma} - L^{-\gamma}}
    $$

    where $\gamma = 2r/\sigma^2 - 1$. When $r = \sigma^2/2$, we have $\gamma = 0$ and L'Hopital gives $\mathbb{P}_s(S_\tau = U) = \frac{\ln s - \ln L}{\ln U - \ln L}$.

---

**Exercise 4.** Consider the Dirichlet problem for BM on the unit disk $D = \{(x,y) : x^2 + y^2 < 1\}$ in $\mathbb{R}^2$ with boundary data $g(\theta) = \cos(\theta)$ where $\theta$ is the angle on $\partial D$. The generator is $\mathcal{L} = \frac{1}{2}\Delta$.

(a) Write down the probabilistic (Kakutani) representation of the solution.

(b) Verify that $f(x, y) = x$ solves $\Delta f = 0$ in $D$ and satisfies $f = \cos\theta$ on $\partial D$.

??? success "Solution to Exercise 4"
    **(a)** The probabilistic (Kakutani) representation is:

    $$
    f(x, y) = \mathbb{E}_{(x,y)}[g(B_\tau)]
    $$

    where $B_t = (W_t^1, W_t^2)$ is 2D Brownian motion starting at $(x,y) \in D$ and $\tau = \inf\{t : |B_t| = 1\}$ is the exit time from the unit disk. Here $g(\theta) = \cos\theta$, so $g(B_\tau) = \cos(\arg(B_\tau))$, which equals the $x$-coordinate of $B_\tau$ on the unit circle. Thus:

    $$
    f(x, y) = \mathbb{E}_{(x,y)}[W_\tau^1 / |B_\tau|] = \mathbb{E}_{(x,y)}[W_\tau^1]
    $$

    since $|B_\tau| = 1$.

    **(b)** For $f(x, y) = x$:

    - $\Delta f = \partial_{xx}f + \partial_{yy}f = 0 + 0 = 0$ in $D$ $\checkmark$
    - On $\partial D$: a point on the unit circle is $(\cos\theta, \sin\theta)$, so $f(\cos\theta, \sin\theta) = \cos\theta = g(\theta)$ $\checkmark$

    Therefore $f(x,y) = x$ is the unique harmonic function solving the Dirichlet problem with boundary data $g(\theta) = \cos\theta$ on the unit disk.

---

**Exercise 5.** For standard Brownian motion starting at $x \in (0, b)$, use the Poisson problem framework to find $f(x) = \mathbb{E}_x\left[\int_0^\tau X_s\,ds\right]$ where $\tau$ is the exit time from $(0, b)$. That is, solve

$$
\frac{1}{2}f''(x) = -x, \qquad f(0) = 0, \quad f(b) = 0
$$

and verify that $f(x) \geq 0$ on $[0, b]$.

??? success "Solution to Exercise 5"
    We need to solve $\frac{1}{2}f''(x) = -x$ with $f(0) = 0$ and $f(b) = 0$.

    Integrating twice: $f''(x) = -2x$, so $f'(x) = -x^2 + C_1$ and $f(x) = -\frac{x^3}{3} + C_1 x + C_2$.

    From $f(0) = 0$: $C_2 = 0$.

    From $f(b) = 0$: $-\frac{b^3}{3} + C_1 b = 0$, so $C_1 = \frac{b^2}{3}$.

    Therefore:

    $$
    f(x) = \frac{b^2 x}{3} - \frac{x^3}{3} = \frac{x(b^2 - x^2)}{3}
    $$

    **Verification** ($f(x) \geq 0$ on $[0, b]$): For $x \in [0, b]$, we have $x \geq 0$ and $b^2 - x^2 \geq 0$, so $f(x) \geq 0$ $\checkmark$.

    The maximum of $f$ occurs at $f'(x) = \frac{b^2}{3} - x^2 = 0$, i.e., $x = b/\sqrt{3}$, where $f(b/\sqrt{3}) = \frac{2b^3}{9\sqrt{3}}$.

---

**Exercise 6.** In the gambler's ruin problem with drift: a gambler starts with $\$x$ and plays a game with a slight edge, modeled by $dX_t = \mu\,dt + dW_t$ with $\mu > 0$. The game ends at $\$0$ (ruin) or $\$b$ (target).

(a) Using the exit probability formula for BM with drift (with $\sigma = 1$), compute the probability of ruin as a function of $x$, $b$, and $\mu$.

(b) Fix $x = 50$ and $b = 100$. Compare the ruin probability for $\mu = 0$ (fair game), $\mu = 0.01$ (small edge), and $\mu = 0.1$ (large edge). What happens as $\mu \to \infty$?

??? success "Solution to Exercise 6"
    **(a)** The exit probability formula for BM with drift $\mu > 0$ on $(0, b)$ with $\sigma = 1$ gives:

    $$
    \mathbb{P}_x(X_\tau = 0) = \frac{e^{-2\mu x} - e^{-2\mu b}}{1 - e^{-2\mu b}}
    $$

    This follows from the general formula with $a = 0$. Equivalently:

    $$
    \mathbb{P}_x(\text{ruin}) = \frac{e^{-2\mu x} - e^{-2\mu b}}{1 - e^{-2\mu b}}
    $$

    **(b)** With $x = 50$, $b = 100$:

    - **$\mu = 0$ (fair game)**: $\mathbb{P}_{50}(\text{ruin}) = \frac{b - x}{b} = \frac{50}{100} = 0.5$ (by L'Hopital or the driftless formula).
    - **$\mu = 0.01$**: $\mathbb{P}_{50}(\text{ruin}) = \frac{e^{-1} - e^{-2}}{1 - e^{-2}} = \frac{0.3679 - 0.1353}{1 - 0.1353} \approx \frac{0.2326}{0.8647} \approx 0.269$.
    - **$\mu = 0.1$**: $\mathbb{P}_{50}(\text{ruin}) = \frac{e^{-10} - e^{-20}}{1 - e^{-20}} \approx \frac{e^{-10}}{1} \approx 4.54 \times 10^{-5}$.

    As $\mu \to \infty$: the drift is so strong that the process moves upward almost deterministically, so $\mathbb{P}_x(\text{ruin}) \to 0$. Formally, $e^{-2\mu x} \to 0$ and $e^{-2\mu b} \to 0$, but $e^{-2\mu x}/1 \to 0$ since $x > 0$.

---

**Exercise 7.** The Laplace transform of the hitting time $\tau_0$ for BM starting at $x > 0$ hitting level $0$ was shown to be $\mathbb{E}_x[e^{-\lambda \tau_0}] = e^{-\sqrt{2\lambda}\,x}$.

(a) Differentiate with respect to $\lambda$ at $\lambda = 0$ to recover $\mathbb{E}_x[\tau_0]$. What do you find, and is it consistent with $\mathbb{E}_x[\tau_0] = \infty$?

(b) For BM on $(0, b)$ hitting either boundary, the Laplace transform satisfies $\frac{1}{2}v'' = \lambda v$ with $v(0) = v(b) = 1$. Solve this ODE and verify the boundary conditions. Use your solution to show that $\mathbb{E}_x[e^{-\lambda\tau}] \to 1$ as $\lambda \to 0$, consistent with $\tau < \infty$ a.s.

??? success "Solution to Exercise 7"
    **(a)** The Laplace transform is $\mathbb{E}_x[e^{-\lambda\tau_0}] = e^{-\sqrt{2\lambda}\,x}$. Differentiating with respect to $\lambda$:

    $$
    \frac{d}{d\lambda}\mathbb{E}_x[e^{-\lambda\tau_0}] = -\mathbb{E}_x[\tau_0\,e^{-\lambda\tau_0}]
    $$

    On the other hand:

    $$
    \frac{d}{d\lambda}e^{-\sqrt{2\lambda}\,x} = -\frac{x}{\sqrt{2\lambda}}\,e^{-\sqrt{2\lambda}\,x}
    $$

    Setting $\lambda \to 0^+$: $\mathbb{E}_x[\tau_0\,e^{-\lambda\tau_0}] = \frac{x}{\sqrt{2\lambda}}\,e^{-\sqrt{2\lambda}\,x} \to \frac{x}{\sqrt{2\lambda}} \to \infty$. By monotone convergence, $\mathbb{E}_x[\tau_0] = \lim_{\lambda \to 0^+}\mathbb{E}_x[\tau_0\,e^{-\lambda\tau_0}] = \infty$, consistent with the known result $\mathbb{E}_x[\tau_0] = \infty$.

    **(b)** The ODE $\frac{1}{2}v'' = \lambda v$ has characteristic equation $r^2 = 2\lambda$, giving $r = \pm\sqrt{2\lambda}$. Set $\alpha = \sqrt{2\lambda}$. General solution:

    $$
    v(x) = A\cosh(\alpha x) + B\sinh(\alpha x)
    $$

    (using hyperbolic functions, which are more convenient for symmetric boundary conditions). Apply boundary conditions:

    - $v(0) = 1$: $A = 1$
    - $v(b) = 1$: $\cosh(\alpha b) + B\sinh(\alpha b) = 1$, so $B = \frac{1 - \cosh(\alpha b)}{\sinh(\alpha b)}$

    Therefore:

    $$
    v(x) = \cosh(\alpha x) + \frac{1 - \cosh(\alpha b)}{\sinh(\alpha b)}\sinh(\alpha x)
    $$

    This can be simplified. Using the identity $\cosh(\alpha x)\sinh(\alpha b) + \sinh(\alpha x) - \sinh(\alpha x)\cosh(\alpha b) = \sinh(\alpha(b-x)) + \sinh(\alpha x)$... More cleanly, write:

    $$
    v(x) = \frac{\cosh(\alpha(x - b/2))}{\cosh(\alpha b/2)}
    $$

    **Verification**: $v(0) = \frac{\cosh(\alpha b/2)}{\cosh(\alpha b/2)} = 1$ $\checkmark$ and $v(b) = \frac{\cosh(\alpha b/2)}{\cosh(\alpha b/2)} = 1$ $\checkmark$.

    As $\lambda \to 0$: $\alpha \to 0$, so $\cosh(\alpha(x - b/2)) \to 1$ and $\cosh(\alpha b/2) \to 1$, giving $v(x) \to 1$. Thus $\mathbb{E}_x[e^{-\lambda\tau}] \to 1$, which means $\mathbb{P}(\tau < \infty) = 1$: BM exits $(0,b)$ in finite time almost surely.
