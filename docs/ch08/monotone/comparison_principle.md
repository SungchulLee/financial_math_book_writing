# Comparison Principle

The comparison principle is the central uniqueness and ordering result for viscosity solutions. It states that if a subsolution lies below a supersolution on the boundary, then this ordering persists throughout the domain. This immediately implies uniqueness: the viscosity solution is the only function that is simultaneously a sub- and supersolution.

---

## Statement for Parabolic Problems

Consider the degenerate parabolic PDE:

$$
u_\tau + F(\tau, x, u, Du, D^2u) = 0 \quad \text{in } (0, T] \times \Omega
$$

where $F$ is degenerate elliptic (non-increasing in the $D^2u$ argument) and proper (non-decreasing in the $u$ argument, i.e., $F(\tau, x, r, p, X) \leq F(\tau, x, s, p, X)$ whenever $r \leq s$).

!!! abstract "Theorem (Comparison Principle)"
    Let $u$ be a viscosity subsolution and $v$ a viscosity supersolution of $u_\tau + F = 0$ on $(0, T] \times \Omega$. If $u \leq v$ on the **parabolic boundary** (i.e., at $\tau = 0$ and on $\partial\Omega$), then:

    $$
    \boxed{u(\tau, x) \leq v(\tau, x) \quad \text{for all } (\tau, x) \in [0, T] \times \overline{\Omega}}
    $$

The parabolic boundary consists of the initial data ($\tau = 0$) and the spatial boundary ($x \in \partial\Omega$).

---

## Consequences

### Uniqueness

**Corollary**: If the comparison principle holds, then the viscosity solution is **unique**.

*Proof*: Let $u$ and $v$ both be viscosity solutions with the same boundary data. Then $u$ is a subsolution and $v$ is a supersolution, so $u \leq v$. By symmetry (swapping the roles), $v \leq u$. Therefore $u = v$. $\square$

### Stability

**Corollary**: If $u_n$ are viscosity solutions with boundary data $g_n$ and $g_n \to g$ uniformly, then $u_n \to u$ uniformly, where $u$ is the viscosity solution with boundary data $g$.

This stability under perturbation of boundary data is essential for numerical analysis: it ensures that small errors in the boundary conditions do not lead to large errors in the solution.

### Ordering and Bounds

The comparison principle gives a priori bounds. If $\underline{u}$ and $\overline{u}$ are explicit sub- and supersolutions (barriers) with known formulas, then the true solution satisfies:

$$
\underline{u}(\tau, x) \leq u(\tau, x) \leq \overline{u}(\tau, x)
$$

For European options, taking $\underline{u} = 0$ and $\overline{u} = S$ (for calls) gives the obvious bound $0 \leq V \leq S$.

---

## Proof Sketch: Doubling of Variables

The standard proof technique is the **Ishii-Lions doubling of variables** method. We outline the key steps.

### Setup

Suppose, for contradiction, that

$$
M = \sup_{(\tau, x) \in [0,T] \times \overline\Omega} (u - v)(\tau, x) > 0
$$

We want to show this leads to a contradiction with the sub/supersolution properties.

### Step 1: Penalized Supremum

The direct approach of testing at the supremum point fails because $u$ and $v$ may not be differentiable there. Instead, consider the **doubled function**:

$$
\Phi_\alpha(\tau, x, \sigma, y) = u(\tau, x) - v(\sigma, y) - \frac{\alpha}{2}|x - y|^2 - \frac{\alpha}{2}(\tau - \sigma)^2
$$

where $\alpha > 0$ is a large parameter. The quadratic penalty forces the supremum to occur near the diagonal $x = y$, $\tau = \sigma$.

### Step 2: Supremum Point

Let $(\tau_\alpha, x_\alpha, \sigma_\alpha, y_\alpha)$ be a point where $\Phi_\alpha$ attains its supremum. Standard arguments show:

- As $\alpha \to \infty$: $|x_\alpha - y_\alpha| \to 0$ and $|\tau_\alpha - \sigma_\alpha| \to 0$
- $\alpha|x_\alpha - y_\alpha|^2 \to 0$
- $u(\tau_\alpha, x_\alpha) - v(\sigma_\alpha, y_\alpha) \to M > 0$

For large $\alpha$, the supremum point is in the interior (not on the parabolic boundary, where $u \leq v$ by assumption).

### Step 3: Applying the Definitions

At $(\tau_\alpha, x_\alpha)$, the function $(\tau, x) \mapsto v(\sigma_\alpha, y_\alpha) + \frac{\alpha}{2}|x - y_\alpha|^2 + \frac{\alpha}{2}(\tau - \sigma_\alpha)^2$ is a smooth test function touching $u$ from above. By the subsolution property:

$$
\alpha(\tau_\alpha - \sigma_\alpha) + F(\tau_\alpha, x_\alpha, u(\tau_\alpha, x_\alpha), \alpha(x_\alpha - y_\alpha), X_\alpha) \leq 0
$$

Similarly, at $(\sigma_\alpha, y_\alpha)$, the supersolution property gives:

$$
\alpha(\tau_\alpha - \sigma_\alpha) + F(\sigma_\alpha, y_\alpha, v(\sigma_\alpha, y_\alpha), \alpha(x_\alpha - y_\alpha), Y_\alpha) \geq 0
$$

Here $X_\alpha$ and $Y_\alpha$ are matrices satisfying certain bounds (from the **Ishii lemma**).

### Step 4: Contradiction

Subtracting the two inequalities and using the properness of $F$ (the fact that $F$ is non-decreasing in $u$, so $u > v$ can be exploited) and the regularity of $F$ in the other variables, one obtains:

$$
0 < \omega(\alpha|x_\alpha - y_\alpha|^2 + |\tau_\alpha - \sigma_\alpha|)
$$

where $\omega$ is a modulus of continuity that vanishes as its argument tends to zero. Since $\alpha|x_\alpha - y_\alpha|^2 \to 0$, this yields $0 \leq 0$, a contradiction. $\square$

---

## Assumptions and Conditions

The comparison principle requires specific structural conditions on $F$.

### Degenerate Ellipticity

$$
F(\tau, x, r, p, X) \leq F(\tau, x, r, p, Y) \quad \text{whenever } X \geq Y
$$

(Here $X \geq Y$ means $X - Y$ is positive semidefinite.) This ensures the PDE has a parabolic or elliptic character.

For the Black-Scholes operator $F = -\frac{1}{2}\sigma^2 S^2 \text{tr}(D^2u) - rS Du + ru$, the diffusion coefficient $\frac{1}{2}\sigma^2 S^2 \geq 0$, so degenerate ellipticity holds.

### Properness

$$
F(\tau, x, r, p, X) \leq F(\tau, x, s, p, X) \quad \text{whenever } r \leq s
$$

The operator is non-decreasing in $u$. For Black-Scholes, the $-rV$ term means the operator contains $+ru$, which is indeed non-decreasing in $u$ (provided $r \geq 0$).

### Continuity of $F$

The function $F$ must be continuous in all its arguments (or at least satisfy appropriate semicontinuity conditions).

### Growth Conditions

For unbounded domains, growth conditions at infinity are needed. For Black-Scholes on $[0, \infty)$, one typically assumes solutions grow at most polynomially: $|u(\tau, S)| \leq C(1 + S^p)$ for some $p > 0$.

---

## Application to Black-Scholes

### European Options

The Black-Scholes PDE satisfies all conditions for the comparison principle:

- Degenerate ellipticity: $\frac{1}{2}\sigma^2 S^2 \geq 0$
- Properness: The $rV$ term (after rearranging as $F = 0$) gives the correct monotonicity
- Continuity: All coefficients are smooth

**Consequence**: The Black-Scholes formula gives the **unique** viscosity solution for European options.

### American Options

For the obstacle problem $\min(-u_\tau + \mathcal{L}u,\; u - \Phi) = 0$, the comparison principle holds under the same conditions, with the additional requirement that sub- and supersolutions satisfy the obstacle constraint appropriately.

**Consequence**: The American option value function is the unique viscosity solution of the variational inequality, and it can be characterized as the **smallest supersolution** that dominates the payoff.

---

## The Discrete Comparison Principle

For numerical schemes, the comparison principle has a discrete analog.

### Definition

A numerical scheme $S_h[u] = 0$ satisfies the **discrete comparison principle** if:

$$
S_h[u] \leq S_h[v] \quad \text{at all nodes} \quad \Longrightarrow \quad u \leq v \quad \text{at all nodes}
$$

(given appropriate boundary ordering).

### Monotone Schemes

A scheme is **monotone** if $S_h[\cdot]$ is a non-decreasing function of each of its arguments (the values at neighboring nodes). For explicit schemes, this corresponds to **non-negative stencil coefficients**.

Monotone schemes automatically satisfy the discrete comparison principle, which is the discrete analog of the continuous comparison principle. This connection is the foundation of the Barles-Souganidis convergence theorem.

### Example: Explicit Scheme

The explicit scheme $u_j^{n+1} = a_j u_{j-1}^n + b_j u_j^n + c_j u_{j+1}^n$ is monotone if and only if $a_j, b_j, c_j \geq 0$. This is precisely the CFL condition combined with the positivity requirement on all coefficients.

---

## Maximum Principle Connection

The comparison principle generalizes the classical **maximum principle** for parabolic PDEs.

**Classical maximum principle**: If $u_\tau - \mathcal{L}u \leq 0$ (subsolution) in a domain, then $u$ attains its maximum on the parabolic boundary.

**Viscosity comparison principle**: Extends this to non-smooth functions and degenerate operators, providing ordering between any subsolution and supersolution.

For monotone schemes, the discrete maximum principle states:

$$
\min_j u_j^n \leq u_j^{n+1} \leq \max_j u_j^n
$$

This is the discrete analog that ensures no new extrema are created by the scheme, and it implies $L^\infty$ stability.

---

## Summary

$$
\boxed{
u \text{ subsolution},\; v \text{ supersolution},\; u \leq v \text{ on boundary} \quad \Longrightarrow \quad u \leq v \text{ everywhere}
}
$$

| Role | Detail |
|------|--------|
| **Uniqueness** | Sub + super with same data $\Rightarrow$ equality |
| **Stability** | Small boundary perturbations $\Rightarrow$ small solution changes |
| **Bounds** | Explicit barriers give a priori estimates |
| **Proof technique** | Doubling of variables (Ishii-Lions) |
| **Key assumptions** | Degenerate ellipticity, properness, continuity |
| **For Black-Scholes** | All conditions satisfied; solution is unique |
| **Discrete version** | Monotone schemes preserve ordering |

The comparison principle is the cornerstone of viscosity solution theory. It guarantees that the option pricing PDE (or variational inequality for American options) has a unique answer, and it provides the theoretical foundation for proving that monotone numerical schemes converge to this unique answer.

---

## Exercises

**Exercise 1.** State the comparison principle for viscosity sub- and supersolutions. Prove the uniqueness corollary: if $u$ and $v$ are both viscosity solutions with the same boundary data, then $u = v$.

---

**Exercise 2.** For a European call, construct explicit sub- and supersolutions (barriers): $\underline{u}(S) = 0$ and $\overline{u}(S) = S$. Verify that $\underline{u}$ is a viscosity subsolution and $\overline{u}$ is a viscosity supersolution of the Black-Scholes PDE, and conclude that $0 \leq V(t, S) \leq S$.

---

**Exercise 3.** The stability corollary states that small perturbations in boundary data produce small changes in the solution. If the terminal payoff is perturbed by $\epsilon$ (i.e., $\Phi_\epsilon(S) = (S - K)^+ + \epsilon$), bound the change in the option price using the comparison principle.

---

**Exercise 4.** Verify the four assumptions required for the comparison principle to hold for the Black-Scholes operator: degenerate ellipticity, properness, continuity, and growth conditions. For the properness condition, explain why $r \geq 0$ is essential.

---

**Exercise 5.** The discrete comparison principle states: if $S_h[u] \leq S_h[v]$ at all nodes, then $u \leq v$ at all nodes. Show that the explicit scheme satisfies this property when all stencil coefficients are non-negative (monotone scheme).

---

**Exercise 6.** The "doubling of variables" proof technique introduces a penalized supremum $\Phi_\alpha(\tau, x, \sigma, y) = u(\tau, x) - v(\sigma, y) - \frac{\alpha}{2}|x-y|^2 - \frac{\alpha}{2}(\tau - \sigma)^2$. Explain the role of the quadratic penalty terms: why do they force the supremum to occur near the diagonal $x = y$, $\tau = \sigma$?
