# Applications of Dynkin's Formula

Dynkin's formula is a powerful tool for computing expectations involving stopping times. This page covers the main applications: exit times, hitting probabilities, boundary value problems, and financial applications.

!!! warning "Dynkin is a Bridge, Not a Solver"
    Dynkin's formula **connects** probabilistic problems to PDEs. The actual work is done by:
    
    - **PDE theory**: existence, uniqueness, regularity of solutions
    - **Boundary conditions**: encoding the problem constraints
    
    Dynkin tells us *why* the PDE solution equals the expected value — it does not magically produce solutions.
    
    **Scope**: All examples in this chapter involve **diffusion processes** (continuous paths, second-order generators). For jump processes, the corresponding equations become integro-differential.

---

## The General Strategy

To compute $\mathbb{E}_x[\cdot]$ involving a stopping time $\tau$:

| Want to find | Solve this PDE | Boundary conditions | Result |
|--------------|----------------|---------------------|--------|
| $\mathbb{E}_x[\tau]$ | $\mathcal{L}u = -1$ | $u = 0$ on $\partial D$ | $u(x) = \mathbb{E}_x[\tau]$ |
| $\mathbb{E}_x[g(X_\tau)]$ | $\mathcal{L}f = 0$ | $f = g$ on $\partial D$ | $f(x) = \mathbb{E}_x[g(X_\tau)]$ |
| $\mathbb{E}_x[e^{-\lambda\tau}]$ | $\mathcal{L}f = \lambda f$ | $f = 1$ on target | $f(x) = \mathbb{E}_x[e^{-\lambda\tau}]$ |

!!! note "Fine Print"
    These correspondences hold when the PDE admits a sufficiently regular solution. In degenerate cases, viscosity or weak solutions may be required. Uniqueness of the PDE solution must be established independently; Dynkin identifies the probabilistic representation.

**Recipe**:

1. Identify what you want to compute
2. Set up the appropriate PDE with boundary conditions
3. Solve the PDE (this is where the real work happens)
4. Dynkin's formula justifies why the PDE solution equals the expectation

!!! note "Why This Works"
    Dynkin's formula says:
    $$\mathbb{E}_x[f(X_\tau)] = f(x) + \mathbb{E}_x\left[\int_0^\tau (\mathcal{L}f)(X_s)\,ds\right]$$
    
    - If $\mathcal{L}f = 0$: the integral vanishes → $\mathbb{E}_x[f(X_\tau)] = f(x)$
    - If $\mathcal{L}f = -1$: the integral equals $-\mathbb{E}_x[\tau]$ → get expected exit time
    - If $\mathcal{L}f = \lambda f$: leads to Feynman–Kac (see below)

---

## Exit Times

### The PDE Approach (Primary Method)

**Setup**: Diffusion $X_t$ in domain $D$, exit time $\tau = \inf\{t : X_t \notin D\}$.

**Goal**: Find $u(x) = \mathbb{E}_x[\tau]$.

**Key observation**: At the boundary, the expected remaining time is zero: $u = 0$ on $\partial D$.

**Derivation**: Apply Dynkin to $u$ itself:

$$\mathbb{E}_x[u(X_\tau)] = u(x) + \mathbb{E}_x\left[\int_0^\tau (\mathcal{L}u)(X_s)\,ds\right]$$

Since $u(X_\tau) = 0$ (boundary condition):

$$0 = u(x) + \mathbb{E}_x\left[\int_0^\tau (\mathcal{L}u)(X_s)\,ds\right]$$

If $\mathcal{L}u = -1$ everywhere in $D$:

$$0 = u(x) - \mathbb{E}_x[\tau]$$

**Result**: The expected exit time solves the **Poisson equation**:

$$\boxed{\mathcal{L}u = -1 \text{ in } D, \quad u = 0 \text{ on } \partial D}$$

---

### Brownian Motion on $(a, b)$

**Process**: $dX_t = dW_t$, generator $\mathcal{L} = \frac{1}{2}\frac{d^2}{dx^2}$

**PDE**: $\frac{1}{2}u'' = -1$ with $u(a) = u(b) = 0$

**Solve**:

$$u'' = -2 \implies u(x) = -x^2 + Cx + D$$

Boundary conditions:

- $u(a) = 0$: $-a^2 + Ca + D = 0$
- $u(b) = 0$: $-b^2 + Cb + D = 0$

Subtracting: $-(b^2 - a^2) + C(b - a) = 0 \implies C = a + b$

Then: $D = a^2 - a(a+b) = -ab$

**Solution**:

$$u(x) = -x^2 + (a+b)x - ab = (x-a)(b-x)$$

$$\boxed{\mathbb{E}_x[\tau] = (x - a)(b - x)}$$

!!! check "Verification"

    - $x = a$: $\mathbb{E}_a[\tau] = 0$ ✓
    - $x = b$: $\mathbb{E}_b[\tau] = 0$ ✓  
    - Maximum at $x = \frac{a+b}{2}$: $\mathbb{E}_{(a+b)/2}[\tau] = \frac{(b-a)^2}{4}$ ✓

---

### Brownian Motion on $(0, \infty)$: Hitting Zero

**Setup**: $X_0 = x > 0$, $\tau_0 = \inf\{t : X_t = 0\}$

**Question**: Is $\mathbb{E}_x[\tau_0] < \infty$?

**PDE**: $\frac{1}{2}u'' = -1$ on $(0, \infty)$ with $u(0) = 0$

General solution: $u(x) = -x^2 + Cx + D$

With $u(0) = 0$: $D = 0$, so $u(x) = -x^2 + Cx$

**Problem**: For Dynkin's formula to apply, we need $u \geq 0$ (it represents an expected time) and appropriate growth conditions (e.g., at most linear growth, ensuring the local martingale is integrable). But:

- If $C > 0$: $u(x) = x(C - x) < 0$ for $x > C$
- If $C \leq 0$: $u(x) < 0$ for all $x > 0$

There is **no nonnegative solution** with the required growth conditions for Dynkin to apply.

**Conclusion**:

$$\boxed{\mathbb{E}_x[\tau_0] = \infty \text{ for BM on } (0, \infty)}$$

!!! info "Interpretation"
    BM started at $x > 0$ hits $0$ **almost surely** (1D BM is recurrent), but the **expected time is infinite**. The particle keeps wandering away before returning.

---

### Ornstein–Uhlenbeck Exit Time

**Process**: $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$

**Generator**: $\mathcal{L}f = -\kappa x f' + \frac{\sigma^2}{2}f''$

**Problem**: Exit time from $(-a, a)$ starting at $x = 0$.

**PDE**: $-\kappa x u' + \frac{\sigma^2}{2}u'' = -1$ with $u(-a) = u(a) = 0$

This ODE does not have a simple closed form.

!!! note "Heuristic Comparison with BM"
    Qualitatively, OU exits faster than BM from a symmetric interval:
    
    - BM: $\mathbb{E}_0[\tau] = a^2$
    - OU: $\mathbb{E}_0[\tau] < a^2$
    
    **Reason**: Mean reversion pushes $X_t$ back toward 0, but the boundaries are symmetric around 0, so the "restoring force" doesn't help — it actually accelerates exit by preventing the particle from lingering far from boundaries.
    
    *This is intuition, not a rigorous bound.*

---

## Exit Probabilities

### Hitting $b$ Before $a$ (Brownian Motion)

**Setup**: $X_0 = x \in (a, b)$, find $p(x) = \mathbb{P}_x(X_\tau = b)$

**Observation**: $p(X_\tau) = \mathbf{1}_{X_\tau = b}$, so $p(x) = \mathbb{E}_x[p(X_\tau)]$

By Dynkin with $\mathcal{L}p = 0$:
$$\mathbb{E}_x[p(X_\tau)] = p(x)$$

**PDE**: $\frac{1}{2}p'' = 0$ with $p(a) = 0$, $p(b) = 1$

**Solution**: $p'' = 0 \implies p(x) = Ax + B$

- $p(a) = Aa + B = 0$
- $p(b) = Ab + B = 1$

Solving: $A = \frac{1}{b-a}$, $B = -\frac{a}{b-a}$

$$\boxed{\mathbb{P}_x(X_\tau = b) = \frac{x - a}{b - a}}$$

---

### Gambler's Ruin Connection

A gambler starts with \$$x$. Each round: win \$1 (prob $\frac{1}{2}$) or lose \$1 (prob $\frac{1}{2}$). Game ends at \$0 (ruin) or \$$b$ (target).

**Continuous limit**: Brownian motion on $(0, b)$.

$$\mathbb{P}(\text{ruin}) = \frac{b - x}{b}, \quad \mathbb{P}(\text{reach target}) = \frac{x}{b}$$

---

### Brownian Motion with Drift

**Process**: $dX_t = \mu\,dt + \sigma\,dW_t$

**Generator**: $\mathcal{L}f = \mu f' + \frac{\sigma^2}{2}f''$

**PDE**: $\mu p' + \frac{\sigma^2}{2}p'' = 0$ with $p(a) = 0$, $p(b) = 1$

**Characteristic equation**: $\frac{\sigma^2}{2}r^2 + \mu r = 0 \implies r = 0$ or $r = -\frac{2\mu}{\sigma^2}$

**General solution**: $p(x) = A + B e^{-2\mu x/\sigma^2}$

With boundary conditions:

$$\displaystyle p(x) = \frac{e^{-2\mu x/\sigma^2} - e^{-2\mu a/\sigma^2}}{e^{-2\mu b/\sigma^2} - e^{-2\mu a/\sigma^2}}$$

!!! check "Limit Check"
    As $\mu \to 0$: By L'Hôpital, $p(x) \to \frac{x - a}{b - a}$ ✓

---

## Boundary Value Problems

!!! warning "Standing Assumptions"
    Throughout this section, assume:
    
    - $D$ is a **bounded** domain with **regular boundary** (e.g., smooth or Lipschitz)
    - The diffusion is **non-explosive** (doesn't blow up in finite time)
    - Appropriate **integrability conditions** for Dynkin's formula hold

### Dirichlet Problem

**Problem**: Given boundary data $g$, find $f$ such that:

$$\mathcal{L}f = 0 \text{ in } D, \quad f = g \text{ on } \partial D$$

**Probabilistic Solution** (Kakutani):

$$\boxed{f(x) = \mathbb{E}_x[g(X_\tau)]}$$

where $\tau = \inf\{t : X_t \notin D\}$.

??? note "Why This Works"
    By Dynkin with $\mathcal{L}f = 0$:
    $$\mathbb{E}_x[f(X_\tau)] = f(x) + 0 = f(x)$$
    
    Since $f = g$ on $\partial D$ and $X_\tau \in \partial D$:
    $$f(x) = \mathbb{E}_x[f(X_\tau)] = \mathbb{E}_x[g(X_\tau)]$$

---

### Poisson Problem

**Problem**: Given source $h$, find $f$ such that:

$$\mathcal{L}f = -h \text{ in } D, \quad f = 0 \text{ on } \partial D$$

**Probabilistic Solution**:

$$\boxed{f(x) = \mathbb{E}_x\left[\int_0^\tau h(X_s)\,ds\right]}$$

??? note "Why This Works"
    By Dynkin:

    $$\mathbb{E}_x[f(X_\tau)] = f(x) + \mathbb{E}_x\left[\int_0^\tau \mathcal{L}f(X_s)\,ds\right]$$

    $$0 = f(x) - \mathbb{E}_x\left[\int_0^\tau h(X_s)\,ds\right]$$

**Special case**: $h \equiv 1$ gives $f(x) = \mathbb{E}_x[\tau]$ (expected exit time).

---

## Laplace Transforms of Hitting Times

**Goal**: Compute $\mathbb{E}_x[e^{-\lambda\tau}]$ for $\lambda > 0$.

!!! info "Why Dynkin Alone Doesn't Suffice"
    The functional $e^{-\lambda\tau}$ is **not linear** in $\tau$, so we can't directly use $\mathcal{L}f = -1$.
    
    Instead, we need the **Feynman–Kac formula**, which handles multiplicative functionals. The key equation becomes $\mathcal{L}f = \lambda f$ (an eigenvalue problem).

**Strategy**: Find $f$ solving:

$$\mathcal{L}f = \lambda f \text{ in } D, \quad f = 1 \text{ on target boundary}$$

Then $f(x) = \mathbb{E}_x[e^{-\lambda\tau}]$.

### BM Hitting Time of Level $a$

Let $\tau_a = \inf\{t : X_t = a\}$ for BM starting at $x > a$.

**PDE**: $\frac{1}{2}f'' = \lambda f$ on $(a, \infty)$ with $f(a) = 1$, $f(\infty) = 0$

**Solve**: Characteristic equation $\frac{1}{2}r^2 = \lambda \implies r = \pm\sqrt{2\lambda}$

General solution: $f(x) = Ae^{\sqrt{2\lambda}x} + Be^{-\sqrt{2\lambda}x}$

- $f(\infty) = 0$: need $A = 0$
- $f(a) = 1$: $Be^{-\sqrt{2\lambda}a} = 1 \implies B = e^{\sqrt{2\lambda}a}$

**Result**:

$$\boxed{\mathbb{E}_x[e^{-\lambda\tau_a}] = e^{-\sqrt{2\lambda}(x - a)}}$$

!!! check "Sanity Checks"

    - $x = a$: $\mathbb{E}_a[e^{-\lambda\tau_a}] = 1$ ✓ (already there)
    - $x \to \infty$: $\mathbb{E}_x[e^{-\lambda\tau_a}] \to 0$ ✓ (takes forever)
    - $\lambda \to 0$: $\mathbb{E}_x[e^{-\lambda\tau_a}] \to 1$ ✓ (no discounting)

---

## Finance Applications

!!! warning "Results Stated Without Full Derivation"
    The following results involve **optimal stopping theory** and **free boundary problems**, which go beyond Dynkin's formula alone. We state the results to illustrate the connection; full derivations require additional machinery.

### Perpetual American Put

**Setup**: Stock follows $dS_t = rS_t\,dt + \sigma S_t\,dW_t$ (risk-neutral). Perpetual put with strike $K$.

**Problem**: Find optimal exercise boundary $S^*$ and option value $V(S)$.

**Structure of the solution**:

- **Exercise region** $(0, S^*)$: $V(S) = K - S$ (exercise immediately)
- **Continuation region** $(S^*, \infty)$: $V$ solves $\mathcal{L}V = rV$

**Boundary conditions at $S^*$**:

| Condition | Meaning |
|-----------|---------|
| $V(S^*) = K - S^*$ | **Value matching**: no arbitrage at boundary |
| $V'(S^*) = -1$ | **Smooth pasting**: $V$ is $C^1$ (from optimal stopping theory) |

**Result** (stated without proof):

$$V(S) = (K - S^*)\left(\frac{S}{S^*}\right)^{-2r/\sigma^2} \quad \text{for } S > S^*$$

$$S^* = \frac{2r}{2r + \sigma^2}K$$

---

### Barrier Option: Down-and-Out Call

**Setup**: Call option that becomes worthless if $S_t$ hits barrier $H < S_0$ before expiry.

**Payoff**: $(S_T - K)^+$ if $\min_{t \leq T} S_t > H$, else $0$.

**Valuation** requires:

- Exit probability (Dynkin)
- Joint distribution of $(S_T, \min_{t \leq T} S_t)$ (reflection principle)
- Risk-neutral expectation (Feynman–Kac)

This is a standard application combining the tools from this chapter.

---

## Summary

| Application | PDE | Boundary Conditions | Probabilistic Meaning |
|-------------|-----|---------------------|----------------------|
| Expected exit time | $\mathcal{L}u = -1$ | $u = 0$ on $\partial D$ | $u(x) = \mathbb{E}_x[\tau]$ |
| Exit probability | $\mathcal{L}p = 0$ | $p = g$ on $\partial D$ | $p(x) = \mathbb{E}_x[g(X_\tau)]$ |
| Laplace transform | $\mathcal{L}f = \lambda f$ | $f = 1$ on target | $f(x) = \mathbb{E}_x[e^{-\lambda\tau}]$ |

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

- [Dynkin's Formula](dynkin_formula.md) — the core formula
- [Generator and Martingales](generator_and_martingales.md) — martingale characterization
- [Feynman–Kac Formula](../../ch03/feynman_kac/feynman_kac_formula.md) — discounted expectations, killing
- [Kolmogorov Backward Equation](../../ch03/kolmogorov_equations/kolmogorov_backward.md) — PDE for transition probabilities
