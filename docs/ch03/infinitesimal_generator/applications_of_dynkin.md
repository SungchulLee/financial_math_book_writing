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

### Brownian Motion on $(a, b)$

**Process**: $dX_t = dW_t$, generator $\mathcal{L} = \frac{1}{2}\frac{d^2}{dx^2}$

**PDE**: $\frac{1}{2}u'' = -1$ with $u(a) = u(b) = 0$

**Solve**: $u'' = -2 \implies u(x) = -x^2 + Cx + D$

Boundary conditions give $C = a + b$ and $D = -ab$, so:

$$\boxed{\mathbb{E}_x[\tau] = (x - a)(b - x)}$$

!!! check "Verification"
    - $x = a$: $\mathbb{E}_a[\tau] = 0$ $\checkmark$
    - $x = b$: $\mathbb{E}_b[\tau] = 0$ $\checkmark$
    - Maximum at $x = \frac{a+b}{2}$: $\mathbb{E}_{(a+b)/2}[\tau] = \frac{(b-a)^2}{4}$ $\checkmark$

!!! note "Connection to Dynkin Formula Page"
    [Dynkin's Formula](dynkin_formula.md) derives this same result directly from the formula using exit probabilities and $\mathbb{E}_x[X_\tau^2]$. The two approaches are equivalent; this page frames it as a PDE boundary value problem.

---

### Brownian Motion on $(0, \infty)$: Hitting Zero

**Setup**: $X_0 = x > 0$, $\tau_0 = \inf\{t : X_t = 0\}$

**PDE**: $\frac{1}{2}u'' = -1$ on $(0, \infty)$ with $u(0) = 0$

General solution with $u(0) = 0$: $u(x) = -x^2 + Cx = x(C - x)$. Since $D = (0, \infty)$ is unbounded, we need $u(x) \geq 0$ for all $x > 0$. But for any fixed $C$, the expression $x(C - x)$ becomes negative for $x > C$. No choice of $C$ produces a nonnegative solution on all of $(0, \infty)$, so the growth conditions needed for Dynkin to apply cannot be satisfied.

**Conclusion**:

$$\boxed{\mathbb{E}_x[\tau_0] = \infty \text{ for BM on } (0, \infty)}$$

!!! info "Interpretation"
    BM started at $x > 0$ hits $0$ **almost surely** (1D BM is recurrent), but the **expected time is infinite**. The particle keeps wandering away before returning.

---

## Exit Probabilities

### Hitting $b$ Before $a$ (Brownian Motion)

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

!!! check "Limit Check"
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

The functional $e^{-\lambda\tau}$ is multiplicative in $\tau$, so Dynkin's formula ($\mathcal{L}f = -1$ or $\mathcal{L}f = 0$) does not apply directly. The correct framework is the **Feynman–Kac formula**: one shows that $v(x) = \mathbb{E}_x[e^{-\lambda\tau}]$ must satisfy $\mathcal{L}v = \lambda v$ by verifying that $e^{-\lambda t}v(X_t)$ is a local martingale — which requires $\tilde{\mathcal{L}}(e^{-\lambda t}v) = 0$, i.e.\ $-\lambda v + \mathcal{L}v = 0$. This is a Feynman–Kac eigenvalue equation, not a Dynkin equation. See [Feynman–Kac Formula](../../ch05/feynman_kac/feynman_kac_formula.md) for the full derivation.

**Strategy**: Find $v$ solving $\mathcal{L}v = \lambda v$ in $D$, $v = 1$ on target boundary. Then $v(x) = \mathbb{E}_x[e^{-\lambda\tau}]$.

### BM Hitting Time of Level $a$

Let $\tau_a = \inf\{t : X_t = a\}$ for BM starting at $x > a$.

**ODE** (Feynman–Kac eigenvalue equation with $\mathcal{L} = \frac{1}{2}\partial_{xx}$): $\frac{1}{2}v'' = \lambda v$, with $v(a) = 1$ and $v(x) \to 0$ as $x \to \infty$.

**Solve**: Characteristic equation $\frac{1}{2}r^2 = \lambda \implies r = \pm\sqrt{2\lambda}$. Boundary condition $v(\infty) = 0$ forces the coefficient of $e^{\sqrt{2\lambda}x}$ to zero; $v(a) = 1$ then gives:

$$\boxed{\mathbb{E}_x[e^{-\lambda\tau_a}] = e^{-\sqrt{2\lambda}(x - a)}}$$

!!! check "Sanity Checks"
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
